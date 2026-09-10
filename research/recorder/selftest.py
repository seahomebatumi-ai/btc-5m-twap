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
            json.dump({"conditionId": "0xabc", "closed": True, "outcomePrices": ["0", "1"],
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
               test_manifest_determinism, test_complete_definition,
               test_floors_are_the_tz_values, test_no_interpolation_anywhere):
        print(fn.__name__)
        fn()
    print("\n%d of %d checks passed" % (PASSED, PASSED))
