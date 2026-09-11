#!/usr/bin/env python3
"""Self-tests for the TZ-04a recorder.

Every check here is an assert that aborts the run. Nothing is recorded into a summary and
called a check. Run:  python3 selftest.py
"""

import gzip
import hashlib
import json
import os
import shutil
import sys
import tempfile

import config
import manifest
import recorder
import analyze

PASSED = 0


def check(name, condition, detail=""):
    global PASSED
    assert condition, "FAILED: %s %s" % (name, detail)
    PASSED += 1
    print("  ok  %s" % name)


def test_window_geometry():
    """[T0-90, T0+330] on a 300 s grid: every frame lands in one or two intervals, never three."""
    t0 = 1789033200
    for offset in range(-120, 421):
        got = config.intervals_for(t0 + offset)
        expect = [t for t in (t0 - 300, t0, t0 + 300)
                  if t - 90 <= t0 + offset <= t + 330]
        check_silent(got == expect, "offset %d: %s != %s" % (offset, got, expect))
    check("window membership over [-120, +420] matches the definition", True)

    worst = max(len(config.intervals_for(t0 + s)) for s in range(0, 300))
    check("a frame lands in at most two intervals", worst == 2, "worst=%d" % worst)

    # The 90 s of run-up before the open are mandatory - they carry the trailing average.
    check("the open minus 90 s is inside the window", t0 in config.intervals_for(t0 - 90))
    check("the open minus 91 s is outside it", t0 not in config.intervals_for(t0 - 91))
    check("the open plus 330 s is inside the window", t0 in config.intervals_for(t0 + 330))
    check("the open plus 331 s is outside it", t0 not in config.intervals_for(t0 + 331))

    # Every wall-clock second is covered by at least one interval: nothing is dropped.
    covered = all(config.intervals_for(t0 + s) for s in range(-90, 331))
    check("no second inside any window is unrouted", covered)


def check_silent(condition, detail):
    assert condition, "FAILED: " + detail


def test_line_format():
    """TZ-04a section 4: one JSON object per line and only these three keys."""
    raw = '{"topic":"crypto_prices_twap_sixty","payload":{"full_accuracy_value":"77915797825165365084160","value":77915.79782516537},"quote":"a \\"quoted\\" €"}'
    line = json.dumps({"recv_ns": 1, "mono_ns": 2, "raw": raw},
                      ensure_ascii=False, separators=(",", ":"))
    doc = json.loads(line)
    check("the line carries exactly three keys", list(doc) == ["recv_ns", "mono_ns", "raw"],
          str(list(doc)))
    check("the frame text survives byte-for-byte", doc["raw"] == raw)
    check("the full-accuracy string is not turned into a float",
          '"full_accuracy_value":"77915797825165365084160"' in doc["raw"])
    # The convenience float must not be the thing that survives a round trip.
    reparsed = json.loads(doc["raw"])
    check("full_accuracy_value stays a string after reparse",
          isinstance(reparsed["payload"]["full_accuracy_value"], str))


def test_gzip_determinism():
    with tempfile.TemporaryDirectory() as tmp:
        src = os.path.join(tmp, "a.jsonl")
        with open(src, "w") as fh:
            fh.write('{"recv_ns":1,"mono_ns":2,"raw":"x"}\n' * 100)
        recorder.gzip_file(src, os.path.join(tmp, "a.gz"))
        recorder.gzip_file(src, os.path.join(tmp, "b.gz"))
        h1 = hashlib.sha256(open(os.path.join(tmp, "a.gz"), "rb").read()).hexdigest()
        h2 = hashlib.sha256(open(os.path.join(tmp, "b.gz"), "rb").read()).hexdigest()
        check("gzip output is byte-identical across runs", h1 == h2, "%s %s" % (h1, h2))


def _synthetic_interval(root, t0, disconnect=False, gamma=True, resolution=True):
    path = os.path.join(root, str(t0))
    os.makedirs(path, exist_ok=True)
    base = t0 * 10 ** 9
    for i, stream in enumerate(config.STREAM_FILES):
        plain = os.path.join(path, stream + ".jsonl")
        with open(plain, "w", encoding="utf-8") as fh:
            elapsed = 0
            for k in range(20):
                # a deliberate 4 s hole before the 10th message, so max_gap is a real number
                elapsed += 4 if k == 10 else 1
                fh.write(json.dumps({"recv_ns": base + elapsed * 10 ** 9,
                                     "mono_ns": elapsed * 10 ** 9,
                                     "raw": '{"topic":"t%d","n":%d}' % (i, k)},
                                    ensure_ascii=False, separators=(",", ":")) + "\n")
        recorder.gzip_file(plain, plain + ".gz")
        os.remove(plain)
    if gamma:
        with open(os.path.join(path, "gamma.json"), "w") as fh:
            json.dump({"conditionId": "0xabc", "slug": config.slug_for(t0)}, fh)
    if resolution:
        with open(os.path.join(path, "resolution.json"), "w") as fh:
            json.dump({"conditionId": "0xabc", "closed": True, "outcomes": '["Up", "Down"]',
                       "outcomePrices": '["0", "1"]',
                       "events": [{"eventMetadata": {"priceToBeat": 1.0, "finalPrice": 2.0}}]}, fh)
    with open(os.path.join(path, manifest.RUNTIME_NAME), "w") as fh:
        fh.write(json.dumps({"kind": "recorder", "recv_ns": base, "sha": "deadbeef"},
                            sort_keys=True) + "\n")
        fh.write(json.dumps({"kind": "clock", "recv_ns": base + 10 ** 9, "server": "x",
                             "offset_ms": 1.25, "rtt_ms": 3.5}, sort_keys=True) + "\n")
        if disconnect:
            fh.write(json.dumps({"kind": "disconnect", "start_recv_ns": base,
                                 "end_recv_ns": base + 2 * 10 ** 9, "reason": "reconnect"},
                                sort_keys=True) + "\n")
    return path


def test_manifest_determinism():
    """V5 in miniature: a rebuild from the directory alone must reproduce the same bytes."""
    with tempfile.TemporaryDirectory() as tmp:
        path = _synthetic_interval(tmp, 1789033200)
        first = manifest.write(path)
        h1 = hashlib.sha256(open(os.path.join(path, "manifest.json"), "rb").read()).hexdigest()
        manifest.write(path)
        h2 = hashlib.sha256(open(os.path.join(path, "manifest.json"), "rb").read()).hexdigest()
        check("a rebuilt manifest is byte-identical", h1 == h2, "%s %s" % (h1, h2))
        check("the manifest counts every message", first["streams"]["twap60"]["messages"] == 20)
        check("the longest inter-message gap is measured, not assumed",
              first["streams"]["twap60"]["max_inter_message_gap_ms"] == 4000.0,
              str(first["streams"]["twap60"]["max_inter_message_gap_ms"]))
        check("raw and stored bytes are both recorded",
              first["streams"]["twap60"]["raw_bytes"] > 0
              and first["streams"]["twap60"]["stored_bytes"] > 0)
        check("the recorder sha is read back from the directory",
              first["recorder_git_sha"] == "deadbeef")


def test_complete_definition():
    """complete = zero disconnects on S1/S3 across the window, with S6 and S7 both present."""
    with tempfile.TemporaryDirectory() as tmp:
        good = manifest.build(_synthetic_interval(tmp, 1789033200))
        check("a clean interval is complete", good["complete"] is True)
        cases = [("a disconnect inside the window", dict(disconnect=True)),
                 ("a missing S6", dict(gamma=False)),
                 ("a missing S7", dict(resolution=False))]
        for i, (name, kwargs) in enumerate(cases):
            doc = manifest.build(_synthetic_interval(tmp, 1789040000 + i * 300, **kwargs))
            check("%s makes the interval incomplete" % name, doc["complete"] is False)


def test_resolved_outcome():
    """Live quotes are truthy and look like prices; only a settled market is a result."""
    live = {"closed": False, "outcomes": '["Up", "Down"]', "outcomePrices": '["0.685", "0.315"]'}
    check("live quotes on an open market are not a result",
          manifest.resolved_outcome(live) is None)
    check("fractional prices on a closed market are not a result",
          manifest.resolved_outcome(dict(live, closed=True)) is None)
    up = {"closed": True, "outcomes": '["Up", "Down"]', "outcomePrices": '["1", "0"]'}
    down = {"closed": True, "outcomes": '["Up", "Down"]', "outcomePrices": '["0", "1"]'}
    check("a settled Up market reads as Up", manifest.resolved_outcome(up) == "Up")
    check("a settled Down market reads as Down", manifest.resolved_outcome(down) == "Down")
    check("two winners is not a result", manifest.resolved_outcome(
        dict(up, outcomePrices='["1", "1"]')) is None)
    check("a closed market with no prices is not a result",
          manifest.resolved_outcome(dict(up, outcomePrices=None)) is None)


def test_published_precision():
    """V1 on real values: the S1 report at T0 = 1789034100 against the venue's price to beat."""
    import decimal
    scale = decimal.Decimal(10) ** 18
    venue = decimal.Decimal("77979.98737803145")
    at_t0 = decimal.Decimal("77979987378031447506944") / scale
    one_second_early = decimal.Decimal("77980322368025738084352") / scale
    check("the S1 report at T0 is not Decimal-equal to the published double",
          at_t0 != venue)
    check("it is equal at the precision the venue publishes",
          analyze.published_equal(at_t0, venue))
    check("the report one second earlier is not equal at any precision",
          not analyze.published_equal(one_second_early, venue))
    check("the residual is below one double ulp at this magnitude",
          abs(at_t0 - venue) < decimal.Decimal(2) ** -36)


def test_clock_filter():
    """Of a burst, the lowest-delay reply wins - the 28 ms far-server reading must not."""
    burst = [(0.028110, 0.092550), (0.001367, 0.001345), (0.000941, 0.012997)]
    check("the lowest round trip is kept", recorder.best_sample(burst) == (0.001367, 0.001345))


def test_restart_edges():
    """A restart's outage starts at the last frame on disk, and a torn line breaks nothing."""
    with tempfile.TemporaryDirectory() as tmp:
        base = os.path.join(tmp, config.SERIES, "1789034700")
        os.makedirs(base)
        with open(os.path.join(base, "twap60.jsonl"), "w") as fh:
            fh.write('{"recv_ns":100,"mono_ns":1,"raw":"a"}\n')
            fh.write('{"recv_ns":300,"mono_ns":2,"raw":"b"}\n')
            fh.write('{"recv_ns":999,"mono_ns":3,"ra')          # torn by a kill mid-write
        with open(os.path.join(base, "chainlink.jsonl"), "w") as fh:
            fh.write('{"recv_ns":250,"mono_ns":1,"raw":"c"}\n')
        check("the last frame on disk is found", recorder.last_frame_ns(tmp) == 300,
              str(recorder.last_frame_ns(tmp)))
        check("an empty capture root gives 0",
              recorder.last_frame_ns(os.path.join(tmp, "none")) == 0)
        doc = manifest.build(base)
        check("a torn line is counted, not fatal",
              doc["streams"]["twap60"]["unparseable_lines"] == 1
              and doc["streams"]["twap60"]["messages"] == 2)


def test_floors_are_the_tz_values():
    """A floor that drifted from the TZ would silently change the run's stop condition."""
    check("the free-space floor is exactly 2_000_000_000 bytes",
          config.FREE_SPACE_FLOOR_BYTES == 2000000000)
    check("the self-cap is exactly 4_000_000_000 bytes", config.SELF_CAP_BYTES == 4000000000)
    check("the clock limit is exactly 50 ms", config.CLOCK_OFFSET_LIMIT_MS == 50.0)
    check("the window is [T0-90, T0+330]",
          (config.PRE_S, config.POST_S, config.INTERVAL_S) == (90, 330, 300))
    for topic, (filters, _stream) in config.TIER_A.items():
        check("%s uses the exact compact filter form" % topic,
              filters == json.dumps(json.loads(filters), separators=(",", ":"))
              and " " not in filters and filters == filters.lower(), filters)


def _doc(t0, disconnect=0, gamma=True, resolution=True):
    return {"T0_epoch": t0, "complete": not disconnect and gamma and resolution,
            "disconnect_count": disconnect, "gamma_present": gamma,
            "resolution_present": resolution, "recorder_git_sha": analyze.RECORDER_SHA}


def test_scoring_set():
    """TZ-04b section 6: members are counted, not run; every non-member in between is a row."""
    start = analyze.first_scoring_t0(1789035669)
    check("the 10:21:09 start gives the 10:25 interval first", start == 1789035900, str(start))
    check("the logged 10:21:10.18 start gives the same interval",
          analyze.first_scoring_t0(1789035670.180046788) == 1789035900)
    check("a window opening at the start instant does not lie after it",
          analyze.first_scoring_t0(1789035810) == 1789036200)
    check("a window opening just after the start does",
          analyze.first_scoring_t0(1789035809.999) == 1789035900)

    t = [start + i * 300 for i in range(10)]
    manifests = {t[0]: _doc(t[0]), t[1]: _doc(t[1], disconnect=1), t[2]: _doc(t[2]),
                 t[3]: _doc(t[3], resolution=False), t[4]: _doc(t[4]),
                 t[6]: _doc(t[6]), t[7]: _doc(t[7], gamma=False), t[8]: _doc(t[8]),
                 t[9]: _doc(t[9])}                       # t[5] has no directory at all
    rows, full = analyze.scoring_set(manifests, start, need=4)
    check("the set fills from non-consecutive members", full and len(rows) == 7,
          "full=%s rows=%d" % (full, len(rows)))
    check("members are indexed in order",
          [r["member"] for r in rows] == [1, None, 2, None, 3, None, 4],
          str([r["member"] for r in rows]))
    check("each non-member carries its reason",
          [r["reasons"] for r in rows] == [[], ["disconnect"], [], ["no S7"], [],
                                           ["no manifest"], []], str([r["reasons"] for r in rows]))
    check("the walk stops at the last member", rows[-1]["T0"] == t[6])
    rows, full = analyze.scoring_set(manifests, start, need=20)
    check("a short capture is reported as not full, through its last interval",
          not full and rows[-1]["T0"] == t[9] and len(rows) == 10)
    try:
        analyze.reasons_for(dict(_doc(t[0]), disconnect_count=1))
        consistent = False
    except AssertionError:
        consistent = True
    check("a manifest whose verdict contradicts its fields aborts the run", consistent)
    check("199 of 200 clears the gate", analyze.clears(199, 200))
    check("198 of 200 does not", not analyze.clears(198, 200))
    check("no intervals clears nothing", not analyze.clears(0, 0))


def test_rules_at_live_scale():
    """R1, R2, R3 and the V1 candidates on reports at BTC magnitude, with R2 and R3 split."""
    import decimal
    D = decimal.Decimal
    t0 = 1789035900
    ms = t0 * 1000
    s3 = [(ms - 1000, D("77900.10")), (ms, D("77900.20")), (ms + 150000, D("77950.00")),
          (ms + 300000, D("77899.90")), (ms + 301000, D("78000.00"))]
    s1 = [(ms + 299000, D("77910.00")), (ms + 300000, D("77890.50")), (ms + 301000, D("77999"))]
    preds, r1_val = analyze.rules(s1, s3, t0, D("77900.20"))
    check("R1 reads the first S1 report at or after T0 + 300", r1_val == D("77890.50"))
    check("R1 is Down when that report is below the price to beat", preds["R1"] is False)
    # mean over [T0, T0+300] = (77900.20 + 77950.00 + 77899.90) / 3 = 77916.70 >= 77900.20
    check("R2 averages only reports inside [T0, T0 + 300] and reads Up", preds["R2"] is True)
    check("R3 compares the reading in force at T0 + 300 with the one at T0", preds["R3"] is False)
    streams = {config.S1_STREAM: s1, "twap30": [], config.S3_STREAM: s3}
    values = analyze.candidate_values(streams, t0)
    check("both S3 candidates take the report stamped exactly T0",
          values[4] == D("77900.20") and values[5] == D("77900.20"), str(values))
    check("a stream with no report yields no candidate", values[2] is None and values[3] is None)
    preds, _ = analyze.rules([], s3, t0, D("77900.20"))
    check("no S1 report after the close leaves R1 undecided, not guessed", preds["R1"] is None)


def test_no_interpolation_anywhere():
    """Gaps are recorded, never filled. Prove no fill primitive is reachable in the recorder."""
    banned = ["interpolate", "ffill", "fillna", "forward_fill", "carry_forward", "pad("]
    for name in ("recorder.py", "manifest.py", "config.py", "probe.py", "analyze.py"):
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), name)
        if not os.path.exists(path):
            continue
        text = open(path, encoding="utf-8").read().lower()
        for token in banned:
            check_silent(token not in text, "%s contains %r" % (name, token))
    check("no gap-filling primitive appears in any recorder file", True)


if __name__ == "__main__":
    for fn in (test_window_geometry, test_line_format, test_gzip_determinism,
               test_manifest_determinism, test_complete_definition, test_resolved_outcome,
               test_published_precision, test_clock_filter, test_restart_edges,
               test_floors_are_the_tz_values, test_no_interpolation_anywhere):
        print(fn.__name__)
        fn()
    print("\n%d of %d checks passed" % (PASSED, PASSED))
