#!/usr/bin/env python3
"""TZ-04b validation: V1 through V7, as counts, over the section 6 scoring set.

The tests in TZ-04b section 6 are the Architect's. This file runs them and reports what they
return. It does not design, extend, relax or substitute them, and it does not stop on a red
result - a red result is a finding. It does abort, by assert, when the capture contradicts a
premise the scoring set rests on: one recorder process on 3895356, never restarted, and every
disclosed interval captured by it.

TZ-04b deletes one word from TZ-04a section 6: the scoring set is no longer consecutive. It is
the first 200 members counted from the section 6 start, and every interval from the start to
the last member - member or not - is disclosed in order, so the counts can be re-derived.

Run:  python3 -B analyze.py           > results.json   # deterministic: two runs, one hash
      python3 -B analyze.py --tables  > tables.md      # ordered disclosure, V3, disconnects
      python3 -B analyze.py --disk                     # free and captured bytes, measured now
"""

import calendar
import collections
import decimal
import glob
import gzip
import hashlib
import json
import os
import re
import shutil
import statistics
import subprocess
import sys
import tempfile
import time

import config
import manifest

decimal.getcontext().prec = 60
SCALE = decimal.Decimal(10) ** 18
MS = 1000
NS = 10 ** 9

# TZ-04b section 6: a rule is the settlement rule only if it agrees on at least 199 of every
# 200 intervals scored. Carried across from TZ-04 word for word, before any score existed.
ACCEPT_NUM, ACCEPT_DEN = 199, 200
SET_SIZE = 200

# TZ-04b section 6, "Start": the recorder process on this commit, 2026-09-10 10:21:09 UTC.
RECORDER_SHA = "3895356aff853f2fcb1b030b1502acb95b16f0a5"
RECORDER_START_UTC = "2026-09-10T10:21:09Z"

RUNTIME_PATH = os.path.join(config.ROOT, "runtime.jsonl")
LOG_PATH = os.path.join(config.ROOT, "recorder.log")
PROBE_PATH = os.path.join(config.ROOT, "tier-b-probe.json")


def load_manifests():
    out = {}
    for path in glob.glob(os.path.join(config.ROOT, config.SERIES, "*", "manifest.json")):
        with open(path, encoding="utf-8") as fh:
            doc = json.load(fh)
        out[doc["T0_epoch"]] = doc
    return dict(sorted(out.items()))


def load_json(path):
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as fh:
        doc = json.load(fh, parse_float=decimal.Decimal)
    return doc[0] if isinstance(doc, list) else doc


def utc(epoch_s, fmt="%Y-%m-%d %H:%M"):
    return time.strftime(fmt, time.gmtime(epoch_s))


def utc_ms(ns):
    return "%s.%03d" % (utc(ns // NS, "%Y-%m-%d %H:%M:%S"), (ns % NS) // 10 ** 6)


def reports(t0, stream):
    """The venue's published readings for one stream inside one interval directory.

    A report is a `type == "update"` frame: one reading, as the live feed published it. The
    `subscribe` snapshot frames are stored verbatim on disk but are not treated as reports -
    they are a backfill batch delivered at connect, and using them to cover a hole would be
    filling a gap, which TZ-04a section 4 forbids.
    """
    path = os.path.join(config.interval_dir(t0), stream + ".jsonl.gz")
    out = []
    if not os.path.exists(path):
        return out
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                frame = json.loads(json.loads(line)["raw"], parse_float=decimal.Decimal)
            except (ValueError, KeyError):
                continue                    # a torn line is counted by the manifest, not read
            if frame.get("type") != "update":
                continue
            payload = frame.get("payload") or {}
            fav = payload.get("full_accuracy_value")
            ts = payload.get("timestamp")
            if fav is None or ts is None:
                continue
            # full precision: the integer string, never the convenience float
            value = decimal.Decimal(fav) / SCALE if len(str(fav)) > 15 else decimal.Decimal(fav)
            out.append((int(ts), value))
    out.sort(key=lambda r: r[0])
    return out


def published_equal(candidate, venue_value):
    """Equality at the precision the venue publishes.

    The venue serialises its price to beat as an IEEE-754 double - about 17 significant
    digits - while the oracle feed carries a 23-digit integer scaled by 1e18. Decimal equality
    between the two can never hold even when they are the same number: on 2026-09-10 the S1
    report at T0 = 1789034100 differed from the published price to beat by 2.49e-12, below one
    double ulp at that magnitude. The full available precision is therefore the double, and
    that is where exactness is judged. Strict Decimal equality is reported alongside.
    """
    return float(candidate) == float(venue_value)


def last_at_or_before(rows, ts_ms):
    hit = None
    for ts, value in rows:
        if ts <= ts_ms:
            hit = value
        else:
            break
    return hit


def first_at_or_after(rows, ts_ms):
    for ts, value in rows:
        if ts >= ts_ms:
            return value
    return None


def venue(t0):
    """The venue's own numbers from the S7 capture: price to beat and resolved outcome.

    A number the venue did not publish stays None. It is never filled with a default.
    """
    market = load_json(os.path.join(config.interval_dir(t0), "resolution.json"))
    if market is None:
        return None
    meta = (market.get("events") or [{}])[0].get("eventMetadata") or {}
    outcome = manifest.resolved_outcome(market)
    ptb = meta.get("priceToBeat")
    return {"price_to_beat": decimal.Decimal(str(ptb)) if ptb is not None else None,
            "resolved_up": (outcome == "Up") if outcome is not None else None}


PTB_KEY = re.compile(r"price.?to.?beat", re.I)


def _keys_like(node, pattern):
    """Every (key, value) pair anywhere in a JSON tree whose key matches `pattern`."""
    if isinstance(node, dict):
        for key, value in node.items():
            if pattern.search(key):
                yield key, value
            yield from _keys_like(value, pattern)
    elif isinstance(node, list):
        for value in node:
            yield from _keys_like(value, pattern)


def s6_carries_price_to_beat(t0):
    """Whether the S6 capture - the market as fetched at T0 + 5 s - has a non-null price to beat.

    None when there is no S6 capture at all.
    """
    path = os.path.join(config.interval_dir(t0), "gamma.json")
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as fh:
        doc = json.load(fh)
    return any(value is not None for _key, value in _keys_like(doc, PTB_KEY))


# ---- scoring set ----------------------------------------------------------------

def recorder_start():
    """The start record of the one process on 3895356, from the recorder's runtime log."""
    starts = []
    with open(RUNTIME_PATH, encoding="utf-8") as fh:
        for line in fh:
            try:
                rec = json.loads(line)
            except ValueError:
                continue
            if rec.get("kind") == "start":
                starts.append(rec)
    ours = [r for r in starts if r["sha"] == RECORDER_SHA]
    assert len(ours) == 1, "expected one process start on %s, found %d" % (RECORDER_SHA,
                                                                           len(ours))
    later = [r for r in starts if r["recv_ns"] > ours[0]["recv_ns"]]
    assert not later, "the recorder was restarted after the %s start: %r" % (RECORDER_SHA, later)
    return ours[0]


def first_scoring_t0(start_epoch):
    """The first T0 whose whole window [T0 - 90, T0 + 330] lies after `start_epoch`."""
    t0 = (int(start_epoch) // config.INTERVAL_S) * config.INTERVAL_S
    while t0 - config.PRE_S <= start_epoch:
        t0 += config.INTERVAL_S
    return t0


def reasons_for(doc):
    """Why an interval fails `complete`, read from its manifest; empty when it does not."""
    if doc is None:
        return ["no manifest"]
    why = []
    if doc["disconnect_count"]:
        why.append("disconnect")
    if not doc["gamma_present"]:
        why.append("no S6")
    if not doc["resolution_present"]:
        why.append("no S7")
    # The manifest's verdict and the three facts it is built from must agree.
    assert doc["complete"] == (not why), "manifest %d: complete=%s but reasons %s" % (
        doc["T0_epoch"], doc["complete"], why)
    return why


def scoring_set(manifests, start_t0, need=SET_SIZE):
    """TZ-04b section 6: every interval from the start, in order, until `need` members.

    A member has `complete: true` and a venue resolution present. Nothing is excluded for any
    other reason. The rows carry every non-member between the start and the last member. The
    walk is over the 300 s grid, not over the manifests, so an interval with no directory still
    gets a row. When the capture runs out before `need` members, `full` is False.
    """
    rows, members = [], 0
    last = max(manifests) if manifests else start_t0 - config.INTERVAL_S
    t0 = start_t0
    while members < need and t0 <= last:
        doc = manifests.get(t0)
        why = reasons_for(doc)
        resolved = bool(doc and doc["resolution_present"])
        member = not why and resolved
        if member:
            members += 1
        rows.append({"T0": t0, "complete": bool(doc and doc["complete"]), "reasons": why,
                     "resolution_present": resolved, "member": members if member else None})
        t0 += config.INTERVAL_S
    return rows, members == need


def clears(agree, n):
    """At least 199 of every 200, in integers."""
    return n > 0 and agree * ACCEPT_DEN >= ACCEPT_NUM * n


# ---- V1 and V2 ------------------------------------------------------------------

CANDIDATES = [("S1", config.S1_STREAM, "last<=T0"), ("S1", config.S1_STREAM, "first>=T0"),
              ("S2", "twap30", "last<=T0"), ("S2", "twap30", "first>=T0"),
              ("S3", config.S3_STREAM, "last<=T0"), ("S3", config.S3_STREAM, "first>=T0")]
V1_NAMES = ["%s %s" % (s, k) for s, _f, k in CANDIDATES]
RULES = ("R1", "R2", "R3")


def candidate_values(streams, t0):
    """The six V1 candidates, in CANDIDATES order; None where the stream has no such report."""
    out = []
    for _source, stream, kind in CANDIDATES:
        rows = streams[stream]
        out.append(last_at_or_before(rows, t0 * MS) if kind == "last<=T0"
                   else first_at_or_after(rows, t0 * MS))
    return out


def rules(s1, s3, t0, price_to_beat):
    """R1, R2 and R3 for one interval, each True for Up; None where the data cannot decide it.

    R1 reads S1 "at/after T0 + 300": the first report at or after that instant, compared with
    the price to beat at the precision the venue publishes, exactly as V1 judges equality. R2
    and R3 read S3 "at T0" and "at T0 + 300" as the reading in force at that instant: the last
    report at or before it. R2's mean is over every S3 report timestamped in [T0, T0 + 300].
    """
    close_ms = (t0 + config.INTERVAL_S) * MS
    r1_val = first_at_or_after(s1, close_ms)
    r1 = (float(r1_val) >= float(price_to_beat)
          if r1_val is not None and price_to_beat is not None else None)
    s3_open = last_at_or_before(s3, t0 * MS)
    window = [v for ts, v in s3 if t0 * MS <= ts <= close_ms]
    r2 = (sum(window) / len(window) >= s3_open) if window and s3_open is not None else None
    s3_close = last_at_or_before(s3, close_ms)
    r3 = (s3_close >= s3_open) if s3_close is not None and s3_open is not None else None
    return {"R1": r1, "R2": r2, "R3": r3}, r1_val


def distribution(values):
    if not values:
        return None
    ordered = sorted(values)
    def pct(p):
        return ordered[min(len(ordered) - 1, int(p * len(ordered)))]
    return {"n": len(ordered), "min": ordered[0], "p50": pct(0.50), "p90": pct(0.90),
            "p99": pct(0.99), "max": ordered[-1], "mean": statistics.fmean(ordered),
            "zero_count": sum(1 for v in ordered if v == 0.0)}


def score(rows):
    """V1 and V2 over the members. Each member's row gains its per-interval results."""
    matches = {n: 0 for n in V1_NAMES}
    strict = {n: 0 for n in V1_NAMES}
    unavailable = {n: 0 for n in V1_NAMES}
    diffs = {n: [] for n in V1_NAMES}
    agree = {r: 0 for r in RULES}
    undecidable = {r: 0 for r in RULES}
    n = ptb_absent = s6_ptb = s6_missing = ties = precision_sensitive = 0
    for row in rows:
        if row["member"] is None:
            continue
        n += 1
        t0 = row["T0"]
        info = venue(t0)
        assert info is not None and info["resolved_up"] is not None, "member %d unresolved" % t0
        ptb = info["price_to_beat"]
        if ptb is None:
            ptb_absent += 1
        s6 = s6_carries_price_to_beat(t0)
        s6_missing += s6 is None
        s6_ptb += bool(s6)

        streams = {s: reports(t0, s) for s in (config.S1_STREAM, "twap30", config.S3_STREAM)}
        flags = []
        for name, value in zip(V1_NAMES, candidate_values(streams, t0)):
            if value is None:
                unavailable[name] += 1
            hit = value is not None and ptb is not None and published_equal(value, ptb)
            flags.append(hit)
            matches[name] += hit
            if value is not None and ptb is not None:
                strict[name] += value == ptb
                diffs[name].append(abs(value - ptb))

        preds, r1_val = rules(streams[config.S1_STREAM], streams[config.S3_STREAM], t0, ptb)
        if r1_val is not None and ptb is not None:
            ties += published_equal(r1_val, ptb)
            precision_sensitive += (r1_val >= ptb) != preds["R1"]
        verdicts = {}
        for rule, pred in preds.items():
            if pred is None:
                undecidable[rule] += 1
                verdicts[rule] = None
            else:
                verdicts[rule] = pred == info["resolved_up"]
                agree[rule] += verdicts[rule]
        row["outcome"] = "Up" if info["resolved_up"] else "Down"
        row["rules"] = verdicts
        row["v1"] = "".join("x" if f else "." for f in flags)

    best = sorted(V1_NAMES, key=lambda k: (-matches[k], V1_NAMES.index(k)))[:2]
    v1 = {
        "n": n,
        "price_to_beat_source": "resolution.json (S7 capture): events[0].eventMetadata.priceToBeat",
        "price_to_beat_absent_in_s7": ptb_absent,
        "s6_captures_carrying_a_price_to_beat": s6_ptb,
        "s6_captures_missing": s6_missing,
        "match_definition": "equal as the IEEE-754 double the venue publishes",
        "matches": matches,
        "strict_decimal_matches": strict,
        "candidate_unavailable": unavailable,
        "best_two": best,
        "abs_difference_distribution": {k: distribution([float(d) for d in diffs[k]])
                                        for k in best},
    }
    v2 = {
        "n": n,
        "agreements": agree,
        "disagreements": {r: n - agree[r] - undecidable[r] for r in RULES},
        "undecidable": undecidable,
        "agreement_rate_3dp": {r: ("%.3f" % (agree[r] / n)) if n else None for r in RULES},
        "acceptance": "at least %d of every %d" % (ACCEPT_NUM, ACCEPT_DEN),
        "clears_acceptance": {r: clears(agree[r], n) for r in RULES},
        "r1_ties_with_price_to_beat": ties,
        "r1_verdicts_that_differ_between_double_and_decimal": precision_sensitive,
    }
    return v1, v2


# ---- V3 -------------------------------------------------------------------------

DROP = re.compile(r"^(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ) RTDS drop: (.*)$")


def drop_causes():
    """The exception each socket drop logged, keyed by the whole UTC second of the log line."""
    out = {}
    if not os.path.exists(LOG_PATH):
        return out
    with open(LOG_PATH, encoding="utf-8") as fh:
        for line in fh:
            m = DROP.match(line.rstrip("\n"))
            if m:
                out[calendar.timegm(time.strptime(m.group(1), "%Y-%m-%dT%H:%M:%SZ"))] = m.group(2)
    return out


def cause_class(text):
    if text is None:
        return "not logged"
    if "code=1001" in text:
        return "server close 1001 Going away"
    if text.startswith("TimeoutError"):
        return "no frame for 30 s (receive timeout)"
    if text.startswith("ConnectionClosedError(None, None, None)"):
        return "connection lost, no close frame"
    return text


def disconnect_events(rows):
    """Every disconnect touching the proving run, with the session it ended and its logged cause.

    `session_s` runs from the previous resubscribe to this drop's detection.
    """
    lo = (rows[0]["T0"] - config.PRE_S) * NS
    hi = (rows[-1]["T0"] + config.POST_S) * NS
    records = []
    with open(RUNTIME_PATH, encoding="utf-8") as fh:
        for line in fh:
            try:
                rec = json.loads(line)
            except ValueError:
                continue
            if rec.get("kind") == "disconnect":
                records.append(rec)
    records.sort(key=lambda r: r["end_recv_ns"])
    causes = drop_causes()
    out, prev_up = [], None
    for rec in records:
        detected = rec.get("detected_recv_ns", rec["start_recv_ns"])
        if rec["start_recv_ns"] <= hi and rec["end_recv_ns"] >= lo:
            sec = detected // NS
            text = causes.get(sec, causes.get(sec - 1))
            touched = [r["T0"] for r in rows
                       if rec["start_recv_ns"] <= (r["T0"] + config.POST_S) * NS
                       and rec["end_recv_ns"] >= (r["T0"] - config.PRE_S) * NS]
            out.append({"start_recv_ns": rec["start_recv_ns"], "detected_recv_ns": detected,
                        "end_recv_ns": rec["end_recv_ns"],
                        "outage_ms": (rec["end_recv_ns"] - rec["start_recv_ns"]) / 1e6,
                        "session_s": (detected - prev_up) / NS if prev_up else None,
                        "cause": cause_class(text), "logged": text, "intervals": touched})
        prev_up = rec["end_recv_ns"]
    return out


def v3(manifests, rows):
    per_interval = []
    for r in rows:
        doc = manifests.get(r["T0"])
        per_interval.append({
            "T0": r["T0"],
            "streams": None if doc is None else {
                s: {"messages": doc["streams"][s]["messages"],
                    "max_inter_message_gap_ms": doc["streams"][s]["max_inter_message_gap_ms"]}
                for s in config.STREAM_FILES},
            "disconnect_count": None if doc is None else doc["disconnect_count"],
            "disconnected_ms": None if doc is None else doc["disconnected_ms"],
        })
    docs = [manifests[r["T0"]] for r in rows if r["T0"] in manifests]
    per_stream = {}
    for stream in config.STREAM_FILES:
        per_stream[stream] = {
            "messages": distribution([float(d["streams"][stream]["messages"]) for d in docs]),
            "max_inter_message_gap_ms": distribution(
                [d["streams"][stream]["max_inter_message_gap_ms"] for d in docs
                 if d["streams"][stream]["max_inter_message_gap_ms"] is not None]),
        }
    events = disconnect_events(rows)
    members = sum(1 for r in rows if r["member"])
    return {
        "intervals_in_proving_run": len(rows),
        "intervals_with_a_manifest": len(docs),
        "incomplete_intervals": sum(1 for r in rows if not r["complete"]),
        "incomplete_reason_distribution": dict(sorted(collections.Counter(
            "+".join(r["reasons"]) for r in rows if r["reasons"]).items())),
        "members": members,
        "excluded_from_v1_v2": len(rows) - members,
        "per_stream": per_stream,
        "disconnects_touching_proving_run": len(events),
        "disconnect_cause_distribution": dict(sorted(collections.Counter(
            e["cause"] for e in events).items())),
        "disconnect_events": events,
        "per_interval": per_interval,
    }


# ---- V4 -------------------------------------------------------------------------

V4_PATTERN = ("(private[_-]?key|signer|create[_-]?order|post[_-]?order|api[_-]?secret|"
              "passphrase|l1[_-]?auth|l2[_-]?auth|wallet)")


def v4():
    """The TZ's grep, verbatim, run from the repository root."""
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = subprocess.run(["grep", "-rniE", V4_PATTERN, "research/recorder/"], cwd=root,
                         capture_output=True, text=True)
    lines = sorted(l for l in out.stdout.splitlines() if l.strip())
    return {"command": 'grep -rniE "%s" research/recorder/' % V4_PATTERN,
            "exit_status": out.returncode, "matching_lines": len(lines), "matches": lines}


# ---- V5 -------------------------------------------------------------------------

def _sha256(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def rebuild(t0):
    """Rebuild manifest.json from a copy of an already-captured directory; hash before, after."""
    src = config.interval_dir(t0)
    before = _sha256(os.path.join(src, manifest.MANIFEST_NAME))
    with tempfile.TemporaryDirectory() as tmp:
        copy = os.path.join(tmp, str(t0))
        shutil.copytree(src, copy)
        os.remove(os.path.join(copy, manifest.MANIFEST_NAME))
        manifest.write(copy)
        after = _sha256(os.path.join(copy, manifest.MANIFEST_NAME))
    return before, after


def v5(manifests, rows):
    members = [r["T0"] for r in rows if r["member"]]
    if not members:
        return {"status": "no member available"}
    t0 = members[0]
    before, after = rebuild(t0)
    span = [r["T0"] for r in rows if r["T0"] in manifests]
    equal = sum(1 for t in span if len(set(rebuild(t))) == 1)
    return {"interval": t0, "sha256_before": before, "sha256_after": after,
            "equal": before == after,
            "proving_run_rebuilds_equal": equal, "proving_run_rebuilds": len(span)}


# ---- V6 -------------------------------------------------------------------------

def v6(manifests, rows):
    """Clock offset across the proving run. Windows overlap, so samples are de-duplicated."""
    samples, over = {}, {}
    for r in rows:
        doc = manifests.get(r["T0"])
        for s in (doc or {}).get("clock_offset_samples", []):
            samples[(s["recv_ns"], s["server"])] = s["offset_ms"]
            if abs(s["offset_ms"]) > config.CLOCK_OFFSET_LIMIT_MS:
                over[(s["recv_ns"], s["server"])] = s

    def stats(values):
        if not values:
            return None
        return {"samples": len(values), "mean_offset_ms": statistics.fmean(values),
                "mean_abs_offset_ms": statistics.fmean(abs(v) for v in values),
                "max_abs_offset_ms": max(abs(v) for v in values)}

    servers = sorted({k[1] for k in samples})
    flagged = [r["T0"] for r in rows if r["T0"] in manifests
               and manifests[r["T0"]]["clock_offset_abs_max_ms"] is not None
               and manifests[r["T0"]]["clock_offset_abs_max_ms"] > config.CLOCK_OFFSET_LIMIT_MS]
    unsampled = [r["T0"] for r in rows if r["T0"] in manifests
                 and manifests[r["T0"]]["clock_offset_abs_max_ms"] is None]
    return {"all_servers": stats(list(samples.values())),
            "per_server": {s: stats([v for k, v in samples.items() if k[1] == s])
                           for s in servers},
            "limit_ms": config.CLOCK_OFFSET_LIMIT_MS,
            "intervals_over_limit": len(flagged), "intervals_over_limit_list": flagged,
            "intervals_without_a_sample": len(unsampled),
            "samples_over_limit": [over[k] for k in sorted(over)]}


# ---- V7 -------------------------------------------------------------------------

def byte_summary(values):
    if not values:
        return None
    return {"n": len(values), "mean": statistics.fmean(values),
            "median": statistics.median(values), "max": max(values),
            "per_day_from_mean": statistics.fmean(values) * 288,
            "per_day_from_median": statistics.median(values) * 288}


def dir_bytes(path):
    return sum(os.lstat(os.path.join(path, f)).st_size for f in sorted(os.listdir(path)))


CLOSED_TIME = re.compile(r"^(\d{4}-\d\d-\d\d \d\d:\d\d:\d\d)(\.\d+)?\+00$")


def resolution_lags(rows):
    """S7 lag, measured: when resolution.json was written, less the interval end T0 + 300.

    The recorder starts polling at T0 + 333 and polls every 15 s, so this is the lag to first
    sight at that cadence. The venue's own `closedTime`, less T0 + 300, is given alongside.
    """
    seen, stamped, missing, unstamped = [], [], 0, 0
    for r in rows:
        path = os.path.join(config.interval_dir(r["T0"]), "resolution.json")
        if not os.path.exists(path):
            missing += 1
            continue
        end = r["T0"] + config.INTERVAL_S
        seen.append(os.stat(path).st_mtime_ns / NS - end)
        m = CLOSED_TIME.match(str(load_json(path).get("closedTime") or ""))
        if m is None:
            unstamped += 1
            continue
        closed = calendar.timegm(time.strptime(m.group(1), "%Y-%m-%d %H:%M:%S"))
        stamped.append(closed + float(m.group(2) or 0) - end)
    return {"first_seen_by_recorder_s": distribution(seen),
            "venue_closedTime_s": distribution(stamped),
            "intervals_without_resolution": missing,
            "resolutions_without_closedTime": unstamped}


def tier_b():
    with open(PROBE_PATH, encoding="utf-8") as fh:
        probe = json.load(fh)
    retained = []
    for path in sorted(glob.glob(os.path.join(config.ROOT, config.SERIES, "*", "clob.jsonl.gz"))):
        raw, lines = 0, 0
        with gzip.open(path, "rb") as fh:
            for chunk in iter(lambda: fh.read(1 << 20), b""):
                raw += len(chunk)
                lines += chunk.count(b"\n")
        retained.append({"path": path, "compressed_bytes": os.path.getsize(path),
                         "raw_bytes": raw, "lines": lines})
    ratio = (retained[0]["compressed_bytes"] / retained[0]["raw_bytes"]
             if len(retained) == 1 and retained[0]["raw_bytes"] else None)
    raw_per = probe["raw_bytes_per_interval"]
    return {
        "counters_file": PROBE_PATH,
        "clob_ws_url": probe["clob_ws_url"],
        "probe_start_epoch": probe["probe_start_epoch"],
        "probe_end_epoch": probe["probe_end_epoch"],
        "whole_intervals": probe["whole_intervals"],
        "frames_total": probe["frames_total"],
        "bytes_total": probe["bytes_total"],
        "frames_per_interval": probe["frames_per_interval"],
        "raw_bytes_per_interval": raw_per,
        "retained_counter": probe["retained_interval"],
        "retained_files_on_disk": len(retained),
        "retained_measured": retained,
        "gzip_ratio_measured": ratio,
        "raw_bytes_per_day_projected": {k: float(raw_per[k]) * 288 for k in ("mean", "median")},
        "compressed_bytes_per_day_projected": (
            {k: float(raw_per[k]) * 288 * ratio for k in ("mean", "median")} if ratio else None),
    }


def v7(manifests, rows, start):
    docs = [manifests[r["T0"]] for r in rows if r["T0"] in manifests]
    return {
        "tier_a_intervals_measured": len(docs),
        "tier_a_stream_raw_bytes_per_interval": byte_summary(
            [sum(d["streams"][s]["raw_bytes"] for s in config.STREAM_FILES) for d in docs]),
        "tier_a_stream_gzipped_bytes_per_interval": byte_summary(
            [sum(d["streams"][s]["stored_bytes"] for s in config.STREAM_FILES) for d in docs]),
        "tier_a_directory_bytes_on_disk_per_interval": byte_summary(
            [dir_bytes(config.interval_dir(d["T0_epoch"])) for d in docs]),
        "tier_b": tier_b(),
        "free_space_at_start": {"recv_ns": start["recv_ns"], "utc": utc_ms(start["recv_ns"]),
                                "free_bytes": start["free_bytes"],
                                "captured_bytes": start["captured_bytes"]},
        "resolution_lag": resolution_lags(rows),
    }


def disk_now():
    """Volatile, and therefore kept out of the deterministic result."""
    now = time.time_ns()
    captured = sum(os.lstat(os.path.join(dp, f)).st_size
                   for dp, _dn, fn in os.walk(config.ROOT) for f in fn)
    return {"recv_ns": now, "utc": utc_ms(now),
            "free_bytes": shutil.disk_usage(config.ROOT).free, "captured_bytes": captured,
            "free_space_floor_bytes": config.FREE_SPACE_FLOOR_BYTES,
            "self_cap_bytes": config.SELF_CAP_BYTES}


# ---- run ------------------------------------------------------------------------

def build():
    manifests = load_manifests()
    start = recorder_start()
    tz_start = calendar.timegm(time.strptime(RECORDER_START_UTC, "%Y-%m-%dT%H:%M:%SZ"))
    start_t0 = first_scoring_t0(start["recv_ns"] / NS)
    assert start_t0 == first_scoring_t0(tz_start), (
        "the logged start %d and the TZ's %s give different first intervals"
        % (start["recv_ns"], RECORDER_START_UTC))
    rows, full = scoring_set(manifests, start_t0)
    for row in rows:
        doc = manifests.get(row["T0"])
        assert doc is None or doc["recorder_git_sha"] == RECORDER_SHA, (
            "interval %d was captured by %r" % (row["T0"], doc["recorder_git_sha"]))
    v1, v2 = score(rows)
    members = [r["T0"] for r in rows if r["member"]]
    return {
        "start": {"tz_utc": RECORDER_START_UTC, "logged_recv_ns": start["recv_ns"],
                  "logged_utc": utc_ms(start["recv_ns"]), "sha": start["sha"],
                  "first_T0": start_t0},
        "scoring_set": {"full": full, "size_required": SET_SIZE, "members": len(members),
                        "first_T0": rows[0]["T0"] if rows else None,
                        "last_member_T0": members[-1] if members else None,
                        "rows_disclosed": len(rows)},
        "rows": rows,
        "V1_price_to_beat_identity": v1,
        "V2_settlement_rule": v2,
        "V3_gap_accounting": v3(manifests, rows),
        "V4_read_only_proof": v4(),
        "V5_determinism": v5(manifests, rows),
        "V6_clock_discipline": v6(manifests, rows),
        "V7_footprint": v7(manifests, rows, start),
    }


def _mark(value):
    return "—" if value is None else ("Y" if value else "N")


def tables(doc):
    """The report's three long tables, generated from the result rather than typed."""
    out = ["### Ordered disclosure", "",
           "| # | T0 | open (UTC) | complete | reason not complete | S7 | member | outcome "
           "| R1 | R2 | R3 | V1 |",
           "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(doc["rows"], 1):
        rl = r.get("rules") or {}
        out.append("| %d | %d | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            i, r["T0"], utc(r["T0"]), "yes" if r["complete"] else "no",
            " + ".join(r["reasons"]) or "—", "yes" if r["resolution_present"] else "no",
            r["member"] or "—", r.get("outcome", "—"), _mark(rl.get("R1")),
            _mark(rl.get("R2")), _mark(rl.get("R3")), r.get("v1", "—")))
    names = {"twap60": "S1", "twap30": "S2", "chainlink": "S3", "binance": "S4"}
    head = " | ".join("%s msgs | %s max gap ms" % (names[s], names[s])
                      for s in config.STREAM_FILES)
    out += ["", "### V3 per interval", "",
            "| T0 | %s | disconnects | disconnected ms |" % head,
            "|---|" + "---|" * (2 * len(config.STREAM_FILES) + 2)]
    for p in doc["V3_gap_accounting"]["per_interval"]:
        if p["streams"] is None:
            out.append("| %d |%s — | — |" % (p["T0"], " — |" * (2 * len(config.STREAM_FILES))))
            continue
        cells = []
        for s in config.STREAM_FILES:
            g = p["streams"][s]["max_inter_message_gap_ms"]
            cells += [str(p["streams"][s]["messages"]), "—" if g is None else "%.1f" % g]
        out.append("| %d | %s | %d | %.1f |" % (p["T0"], " | ".join(cells),
                                               p["disconnect_count"], p["disconnected_ms"]))
    out += ["", "### Disconnects touching the proving run", "",
            "| # | last frame (UTC) | drop detected (UTC) | resubscribed (UTC) | outage ms "
            "| session s | cause | intervals touched |",
            "|---|---|---|---|---|---|---|---|"]
    for i, e in enumerate(doc["V3_gap_accounting"]["disconnect_events"], 1):
        out.append("| %d | %s | %s | %s | %.1f | %s | %s | %s |" % (
            i, utc_ms(e["start_recv_ns"]), utc_ms(e["detected_recv_ns"]),
            utc_ms(e["end_recv_ns"]), e["outage_ms"],
            "—" if e["session_s"] is None else "%.3f" % e["session_s"], e["cause"],
            ", ".join(str(t) for t in e["intervals"])))
    return "\n".join(out) + "\n"


def main(argv):
    if argv[1:] == ["--disk"]:
        sys.stdout.write(json.dumps(disk_now(), sort_keys=True, indent=2) + "\n")
        return 0
    doc = build()
    if argv[1:] == ["--tables"]:
        sys.stdout.write(tables(doc))
    else:
        sys.stdout.write(json.dumps(doc, sort_keys=True, indent=2, default=str) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
