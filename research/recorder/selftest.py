#!/usr/bin/env python3
"""Self-tests for the TZ-04a recorder, the TZ-05a Tier C and clock repairs, and TZ-06 R-c.

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


def _quote_lines(t0, kind="complete"):
    """The Tier C read lines a synthetic interval holds, one per token id per checkpoint."""
    tokens = ["77" * 8, "99" * 8]
    lines, n = [], 0
    for tau in config.QUOTE_TAUS:
        for token_id in tokens:
            n += 1
            if kind == "short" and n > config.QUOTE_READS_PER_INTERVAL - 2:
                continue
            status, body = 200, '{"asset_id":"%s","tick_size":"0.01"}' % token_id
            if kind == "one-404" and n == 5:
                status, body = 404, '{"error":"no orderbook exists"}'
            if kind == "bad-body" and n == 5:
                body = '{"asset_id": tr'          # a reply that is not JSON
            # 41 ms after the checkpoint, so the offset is a known non-zero number
            recv_ns = config.quote_checkpoint_epoch(t0, tau) * 10 ** 9 + 41 * 10 ** 6
            lines.append(json.dumps({"recv_ns": recv_ns, "mono_ns": n, "tau": tau,
                                     "token_id": token_id, "status": status, "raw": body},
                                    ensure_ascii=False, separators=(",", ":")) + "\n")
    return lines


def _synthetic_interval(root, t0, disconnect=False, gamma=True, resolution=True,
                        quotes="complete"):
    path = os.path.join(root, str(t0))
    os.makedirs(path, exist_ok=True)
    base = t0 * 10 ** 9
    if quotes != "none":
        plain = os.path.join(path, config.QUOTES_STEM + ".jsonl")
        with open(plain, "w", encoding="utf-8") as fh:
            fh.writelines(_quote_lines(t0, quotes))
        recorder.gzip_file(plain, plain + ".gz")
        os.remove(plain)
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


def test_tier_c_checkpoints():
    """TZ-05a section 3 states the checkpoints twice, as tau and as t. They must agree."""
    t0 = 1789033200
    check("the seven checkpoints are the TZ's tau values",
          tuple(config.QUOTE_TAUS) == (240, 180, 120, 90, 60, 30, 10), str(config.QUOTE_TAUS))
    got = [config.quote_checkpoint_epoch(t0, tau) - t0 for tau in config.QUOTE_TAUS]
    check("tau maps to the t values the TZ prints", got == [60, 120, 180, 210, 240, 270, 290],
          str(got))
    check("every checkpoint is inside the interval",
          all(0 < t < config.INTERVAL_S for t in got))
    check("the last checkpoint is inside the window the recorder keeps open",
          max(got) < config.POST_S)
    check("there are fourteen reads per interval",
          config.QUOTE_READS_PER_INTERVAL == 14, str(config.QUOTE_READS_PER_INTERVAL))
    # The two closest checkpoints are 20 s apart, so a read may never be allowed to run into
    # the next one's slot.
    gaps = [b - a for a, b in zip(got, got[1:])]
    check("no read may outlive the gap to the next checkpoint",
          recorder.QUOTE_TIMEOUT_S < min(gaps),
          "timeout=%s min gap=%s" % (recorder.QUOTE_TIMEOUT_S, min(gaps)))

    # A process that starts mid-interval reads what is left, and never reads a checkpoint
    # whose instant has gone by.
    ahead = config.quote_checkpoints_ahead(t0, t0 - 90)
    check("a process running from the window's open reads all seven",
          [tau for tau, _w in ahead] == list(config.QUOTE_TAUS))
    ahead = config.quote_checkpoints_ahead(t0, t0 + 211)
    check("a process starting at T0 + 211 reads only the three still ahead",
          [tau for tau, _w in ahead] == [60, 30, 10], str(ahead))
    check("a checkpoint is read at its own instant, not skipped there",
          [tau for tau, _w in config.quote_checkpoints_ahead(t0, t0 + 210)][0] == 90)
    check("a process starting after the last checkpoint reads nothing",
          config.quote_checkpoints_ahead(t0, t0 + 291) == [])


def test_tier_c_line_and_manifest():
    """quotes_complete is 14 reads, all HTTP 200, every body parsing as JSON. Nothing less."""
    t0 = 1789033200
    with tempfile.TemporaryDirectory() as tmp:
        doc = manifest.build(_synthetic_interval(tmp, t0))
        check("a clean interval has quotes_complete", doc["quotes_complete"] is True)
        check("every read is carried in quote_offsets_ms",
              len(doc["quote_offsets_ms"]) == 14, str(len(doc["quote_offsets_ms"])))
        check("the offset is signed and measured against the intended instant",
              {round(o["offset_ms"], 6) for o in doc["quote_offsets_ms"]} == {41.0},
              str(doc["quote_offsets_ms"][:1]))
        check("each offset carries the checkpoint it belongs to",
              sorted({o["tau"] for o in doc["quote_offsets_ms"]})
              == sorted(config.QUOTE_TAUS))
        cases = [("a single non-200 read", "one-404"),
                 ("a body that is not JSON", "bad-body"),
                 ("fewer than fourteen reads", "short"),
                 ("no Tier C file at all", "none")]
        for i, (name, kind) in enumerate(cases):
            d = manifest.build(_synthetic_interval(tmp, 1789050000 + i * 300, quotes=kind))
            check("%s makes quotes_complete false" % name, d["quotes_complete"] is False)
            check("%s leaves complete untouched" % name, d["complete"] is True)
        early = manifest.build(_synthetic_interval(tmp, 1789060000, quotes="none"))
        check("an interval with no Tier C file has no offsets",
              early["quote_offsets_ms"] == [])


def test_tier_c_manifest_determinism():
    """The Tier C keys must rebuild byte-identically from the directory, like everything else."""
    with tempfile.TemporaryDirectory() as tmp:
        path = _synthetic_interval(tmp, 1789033200)
        manifest.write(path)
        h1 = hashlib.sha256(open(os.path.join(path, "manifest.json"), "rb").read()).hexdigest()
        manifest.write(path)
        h2 = hashlib.sha256(open(os.path.join(path, "manifest.json"), "rb").read()).hexdigest()
        check("a manifest carrying Tier C rebuilds byte-identically", h1 == h2,
              "%s %s" % (h1, h2))


def _sntp_fields(leap=0, stratum=2, transmit_raw=None, host_now=1789203300.0):
    """A 12-word SNTP reply, as struct.unpack('!12I') returns one."""
    if transmit_raw is None:
        transmit_raw = int(host_now + 2208988800)
    first = (leap << 30) | (4 << 27) | (4 << 24) | (stratum << 16) | (6 << 8) | 0xEC
    return (first, 0, 0, 0, 0, 0, 0, 0, transmit_raw, 0, transmit_raw, 0)


def _reason(fields, host_now=1789203300.0):
    t3 = fields[10] + fields[11] / 2 ** 32 - 2208988800
    return recorder.sntp_reject_reason(fields, t3, host_now)


def test_sntp_reply_validation():
    """TZ-05a section 5 R-b, condition by condition, at the host's real clock magnitude."""
    check("the skew limit is exactly 86_400 seconds", config.SNTP_MAX_SKEW_S == 86400,
          str(config.SNTP_MAX_SKEW_S))
    check("a well-formed reply is accepted", _reason(_sntp_fields()) is None)
    check("leap indicator 3 is rejected",
          _reason(_sntp_fields(leap=3)) == "leap-indicator-3")
    check("stratum 0 is rejected", _reason(_sntp_fields(stratum=0)) == "stratum-0")
    check("stratum 16 is rejected", _reason(_sntp_fields(stratum=16)) == "stratum-above-15")
    check("stratum 15 is still accepted", _reason(_sntp_fields(stratum=15)) is None)
    check("a zero transmit timestamp is rejected",
          _reason(_sntp_fields(transmit_raw=0)) == "zero-transmit-timestamp")
    far = _sntp_fields(transmit_raw=int(1789203300.0 + 2208988800 - 86401))
    check("a transmit timestamp 86_401 s adrift is rejected",
          _reason(far) == "transmit-timestamp-beyond-86400s", str(_reason(far)))
    near = _sntp_fields(transmit_raw=int(1789203300.0 + 2208988800 - 86399))
    check("a transmit timestamp 86_399 s adrift is not", _reason(near) is None)

    # The reply that actually reached this host: NTP-era-origin timestamps, which the TZ-04b
    # client turned into an offset near -3.998e12 ms and let dominate the statistics.
    era_zero = _sntp_fields(transmit_raw=0)
    t3 = era_zero[10] + era_zero[11] / 2 ** 32 - 2208988800
    offset_ms = ((t3 - 1789203300.0) + (t3 - 1789203300.0)) / 2 * 1000.0
    check("that reply would have carried an offset near -3.998e12 ms",
          -4.0e12 < offset_ms < -3.9e12, str(offset_ms))
    check("it is rejected before it can become one", _reason(era_zero) is not None)


def test_sntp_rejections_are_counted():
    """A rejection is counted per server, not silently dropped and not filtered afterwards."""
    real_offset, real_lookup = recorder.sntp_offset, recorder.socket.gethostbyname
    calls = []

    def fake_offset(_host, timeout=5):
        calls.append(1)
        if len(calls) == 2:
            return 0.001234, 0.002000
        raise recorder.SntpRejected("zero-transmit-timestamp")

    try:
        recorder.socket.gethostbyname = lambda h: "203.0.113.1"
        recorder.sntp_offset = fake_offset
        ip, offset, rtt, accepted, rejected = recorder.sntp_best("pool.example", burst=4)
        check("the one accepted reply is the offset", offset == 0.001234 and accepted == 1,
              "%s %s" % (offset, accepted))
        check("the other three are counted by reason",
              rejected == {"zero-transmit-timestamp": 3}, str(rejected))
        calls.clear()
        recorder.sntp_offset = lambda _h, timeout=5: (_ for _ in ()).throw(
            recorder.SntpRejected("leap-indicator-3"))
        ip, offset, rtt, accepted, rejected = recorder.sntp_best("pool.example", burst=4)
        check("a burst rejected outright yields no offset at all",
              offset is None and rtt is None and accepted == 0)
        check("and its rejections are still reported",
              rejected == {"leap-indicator-3": 4}, str(rejected))
    finally:
        recorder.sntp_offset, recorder.socket.gethostbyname = real_offset, real_lookup

    # A manifest must survive a clock record that carries no offset.
    with tempfile.TemporaryDirectory() as tmp:
        path = _synthetic_interval(tmp, 1789033200)
        with open(os.path.join(path, manifest.RUNTIME_NAME), "a", encoding="utf-8") as fh:
            fh.write(json.dumps({"kind": "clock", "recv_ns": 1789033200 * 10 ** 9,
                                 "server": "pool.example", "offset_ms": None, "rtt_ms": None,
                                 "rejected": {"zero-transmit-timestamp": 4}},
                                sort_keys=True) + "\n")
        doc = manifest.build(path)
        check("a sample with no offset is carried, not dropped",
              len(doc["clock_offset_samples"]) == 2)
        check("it does not become the largest offset",
              doc["clock_offset_abs_max_ms"] == 1.25, str(doc["clock_offset_abs_max_ms"]))


def _runtime_file(path, records):
    with open(path, "w", encoding="utf-8") as fh:
        for rec in records:
            fh.write(json.dumps(rec, sort_keys=True) + "\n")


def test_span_is_bounded_not_denied():
    """TZ-06 R-c: the analysed span ends at the next start; it is not asserted to have none."""
    ours = {"kind": "start", "recv_ns": 1789035670180046788, "sha": analyze.RECORDER_SHA}
    earlier = {"kind": "start", "recv_ns": 1789033991738343639, "sha": "b2" + "1" * 38}
    later = {"kind": "start", "recv_ns": 1789206785264516934, "sha": "42" * 20}
    real = analyze.RUNTIME_PATH
    try:
        with tempfile.TemporaryDirectory() as tmp:
            analyze.RUNTIME_PATH = os.path.join(tmp, "runtime.jsonl")
            _runtime_file(analyze.RUNTIME_PATH, [earlier, ours])
            check("with no later start the span is unbounded",
                  analyze.recorder_start()["next_start_recv_ns"] is None)

            _runtime_file(analyze.RUNTIME_PATH, [earlier, ours, later])
            start = analyze.recorder_start()
            check("a restart after ours no longer aborts the analysis",
                  start["recv_ns"] == ours["recv_ns"], str(start["recv_ns"]))
            check("the span ends at the first start after ours",
                  start["next_start_recv_ns"] == later["recv_ns"],
                  str(start["next_start_recv_ns"]))

            third = dict(later, recv_ns=later["recv_ns"] + 10 ** 9)
            _runtime_file(analyze.RUNTIME_PATH, [earlier, ours, third, later])
            check("a third start does not move the bound, whatever the file order",
                  analyze.recorder_start()["next_start_recv_ns"] == later["recv_ns"])

            _runtime_file(analyze.RUNTIME_PATH,
                          [ours, dict(ours, recv_ns=ours["recv_ns"] + 1)])
            try:
                analyze.recorder_start()
                one_only = False
            except AssertionError:
                one_only = True
            check("two starts on the analysed commit still abort the run", one_only)
    finally:
        analyze.RUNTIME_PATH = real

    bound = later["recv_ns"]
    check("the last TZ-04b member closes long before the TZ-05a restart",
          analyze.within_span(1789100100, bound))
    edge = bound // 10 ** 9 - config.POST_S
    check("a window closing exactly at the next start is inside the span",
          analyze.within_span(edge, (edge + config.POST_S) * 10 ** 9))
    check("a window closing one nanosecond after it is not",
          not analyze.within_span(edge, (edge + config.POST_S) * 10 ** 9 - 1))
    check("an interval opening after the next start is not in the span",
          not analyze.within_span(edge + config.INTERVAL_S, bound))
    check("an unbounded span contains every interval",
          analyze.within_span(edge + 10 ** 6, None))


if __name__ == "__main__":
    for fn in (test_window_geometry, test_line_format, test_gzip_determinism,
               test_manifest_determinism, test_complete_definition, test_resolved_outcome,
               test_published_precision, test_clock_filter, test_restart_edges,
               test_floors_are_the_tz_values, test_scoring_set, test_rules_at_live_scale,
               test_tier_c_checkpoints, test_tier_c_line_and_manifest,
               test_tier_c_manifest_determinism, test_sntp_reply_validation,
               test_sntp_rejections_are_counted, test_span_is_bounded_not_denied,
               test_no_interpolation_anywhere):
        print(fn.__name__)
        fn()
    print("\n%d of %d checks passed" % (PASSED, PASSED))
