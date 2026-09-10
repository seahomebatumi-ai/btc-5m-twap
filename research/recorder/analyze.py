#!/usr/bin/env python3
"""TZ-04a validation: V1 through V7, as counts.

The tests in TZ-04a section 6 are the Architect's. This file runs them and reports what they
return. It does not design, extend, relax or substitute them, and it does not stop on a red
result - a red result is a finding.

Run:  python3 analyze.py > /path/to/results.json
"""

import decimal
import glob
import gzip
import json
import os
import shutil
import statistics
import subprocess
import sys
import hashlib
import tempfile

import config
import manifest

decimal.getcontext().prec = 60
SCALE = decimal.Decimal(10) ** 18
MS = 1000

# TZ-04a section 6: a rule is the settlement rule only if it agrees on at least 199 of every
# 200 intervals scored. Fixed before any data was seen; carried across from TZ-04 word for word.
ACCEPTANCE = decimal.Decimal(199) / decimal.Decimal(200)


def load_manifests():
    out = {}
    for path in glob.glob(os.path.join(config.ROOT, config.SERIES, "*", "manifest.json")):
        with open(path, encoding="utf-8") as fh:
            doc = json.load(fh)
        out[doc["T0_epoch"]] = doc
    return dict(sorted(out.items()))


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
            frame = json.loads(json.loads(line)["raw"], parse_float=decimal.Decimal)
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
    """The venue's own numbers: price to beat, final price, resolved outcome."""
    path = os.path.join(config.interval_dir(t0), "resolution.json")
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as fh:
        doc = json.load(fh, parse_float=decimal.Decimal)
    market = doc[0] if isinstance(doc, list) else doc
    meta = (market.get("events") or [{}])[0].get("eventMetadata") or {}
    outcome = manifest.resolved_outcome(market)
    if outcome is None or meta.get("priceToBeat") is None:
        return None
    return {"price_to_beat": decimal.Decimal(str(meta["priceToBeat"])),
            "final_price": decimal.Decimal(str(meta.get("finalPrice", "0"))),
            "resolved_up": outcome == "Up"}


# ---- scoring set ----------------------------------------------------------------

def scoring_run(manifests, need=200):
    """The first >= 200 consecutive intervals with complete: true."""
    run = []
    for t0, doc in manifests.items():
        if doc["complete"] and (not run or t0 == run[-1] + config.INTERVAL_S):
            run.append(t0)
        elif doc["complete"]:
            run = [t0]
        else:
            if len(run) >= need:
                return run
            run = []
    return run if len(run) >= need else []


# ---- V1 -------------------------------------------------------------------------

CANDIDATES = [("S1", config.S1_STREAM, "last<=T0"), ("S1", config.S1_STREAM, "first>=T0"),
              ("S2", "twap30", "last<=T0"), ("S2", "twap30", "first>=T0"),
              ("S3", config.S3_STREAM, "last<=T0"), ("S3", config.S3_STREAM, "first>=T0")]


def v1(run):
    names = ["%s %s" % (s, k) for s, _f, k in CANDIDATES]
    matches = {n: 0 for n in names}
    diffs = {n: [] for n in names}
    scored = 0
    for t0 in run:
        info = venue(t0)
        if info is None:
            continue
        scored += 1
        for (source, stream, kind), name in zip(CANDIDATES, names):
            rows = reports(t0, stream)
            value = (last_at_or_before(rows, t0 * MS) if kind == "last<=T0"
                     else first_at_or_after(rows, t0 * MS))
            if value is None:
                continue
            if value == info["price_to_beat"]:
                matches[name] += 1
            diffs[name].append(abs(value - info["price_to_beat"]))
    best = sorted(names, key=lambda n: -matches[n])[:2]
    return {
        "n": scored,
        "matches": matches,
        "match_rate": {n: (matches[n] / scored if scored else None) for n in names},
        "best_two": best,
        "abs_difference_distribution": {
            n: distribution([float(d) for d in diffs[n]]) for n in best
        },
    }


def distribution(values):
    if not values:
        return None
    ordered = sorted(values)
    def pct(p):
        return ordered[min(len(ordered) - 1, int(p * len(ordered)))]
    return {"n": len(ordered), "min": ordered[0], "p50": pct(0.50), "p90": pct(0.90),
            "p99": pct(0.99), "max": ordered[-1], "mean": statistics.fmean(ordered),
            "zero_count": sum(1 for v in ordered if v == 0.0)}


# ---- V2 -------------------------------------------------------------------------

def v2(run):
    """R1, R2 and R3 against the venue's resolved outcome.

    R1 reads S1 "at/after T0 + 300": the first report at or after that instant. R2 and R3 read
    S3 "at T0" and "at T0 + 300": the reading in force at that instant, i.e. the last report at
    or before it. Both conventions are stated in the report.
    """
    agree = {"R1": 0, "R2": 0, "R3": 0}
    undecidable = {"R1": 0, "R2": 0, "R3": 0}
    scored = 0
    for t0 in run:
        info = venue(t0)
        if info is None:
            continue
        scored += 1
        s1 = reports(t0, config.S1_STREAM)
        s3 = reports(t0, config.S3_STREAM)
        close_ms = (t0 + config.INTERVAL_S) * MS

        r1_val = first_at_or_after(s1, close_ms)
        preds = {"R1": (r1_val >= info["price_to_beat"]) if r1_val is not None else None}

        s3_open = last_at_or_before(s3, t0 * MS)
        window = [v for ts, v in s3 if t0 * MS <= ts <= close_ms]
        preds["R2"] = ((sum(window) / len(window) >= s3_open)
                       if window and s3_open is not None else None)

        s3_close = last_at_or_before(s3, close_ms)
        preds["R3"] = ((s3_close >= s3_open)
                       if s3_close is not None and s3_open is not None else None)

        for rule, pred in preds.items():
            if pred is None:
                undecidable[rule] += 1
            elif pred == info["resolved_up"]:
                agree[rule] += 1
    rates = {r: (agree[r] / scored if scored else None) for r in agree}
    return {"n": scored, "agreements": agree, "undecidable": undecidable,
            "agreement_rate": rates,
            "acceptance": "at least 199 of every 200 = %.3f" % float(ACCEPTANCE),
            "clears_acceptance": {r: (rates[r] is not None and rates[r] >= float(ACCEPTANCE))
                                  for r in agree}}


# ---- V3 -------------------------------------------------------------------------

def v3(manifests, run):
    incomplete, reasons = 0, {}
    for doc in manifests.values():
        if doc["complete"]:
            continue
        incomplete += 1
        why = []
        if doc["disconnect_count"]:
            why.append("disconnect")
        if not doc["gamma_present"]:
            why.append("no S6")
        if not doc["resolution_present"]:
            why.append("no S7")
        key = "+".join(why) or "unknown"
        reasons[key] = reasons.get(key, 0) + 1
    per_stream = {}
    for stream in config.STREAM_FILES:
        msgs = [d["streams"][stream]["messages"] for d in manifests.values()]
        gaps = [d["streams"][stream]["max_inter_message_gap_ms"] for d in manifests.values()
                if d["streams"][stream]["max_inter_message_gap_ms"] is not None]
        per_stream[stream] = {
            "messages": distribution([float(m) for m in msgs]),
            "max_inter_message_gap_ms": distribution(gaps),
        }
    return {"intervals_with_a_manifest": len(manifests),
            "incomplete_intervals": incomplete,
            "incomplete_reason_distribution": reasons,
            "excluded_from_v1_v2": len(manifests) - len(run),
            "scored_intervals": len(run),
            "per_stream": per_stream,
            "disconnect_count_total": sum(d["disconnect_count"] for d in manifests.values()),
            "disconnected_ms_total": sum(d["disconnected_ms"] for d in manifests.values())}


# ---- V4 -------------------------------------------------------------------------

V4_PATTERN = ("(private[_-]?key|signer|create[_-]?order|post[_-]?order|api[_-]?secret|"
              "passphrase|l1[_-]?auth|l2[_-]?auth|wallet)")


def v4():
    here = os.path.dirname(os.path.abspath(__file__))
    cmd = ["grep", "-rniE", V4_PATTERN, here + "/"]
    out = subprocess.run(cmd, capture_output=True, text=True)
    lines = [l for l in out.stdout.splitlines() if l.strip()]
    return {"command": 'grep -rniE "%s" research/recorder/' % V4_PATTERN,
            "matching_lines": len(lines), "matches": lines[:50]}


# ---- V5 -------------------------------------------------------------------------

def v5(run):
    """Rebuild manifest.json from an already-captured interval directory, hash before and after."""
    if not run:
        return {"status": "no scored interval available"}
    t0 = run[0]
    src = config.interval_dir(t0)
    path = os.path.join(src, manifest.MANIFEST_NAME)
    before = hashlib.sha256(open(path, "rb").read()).hexdigest()
    with tempfile.TemporaryDirectory() as tmp:
        copy = os.path.join(tmp, str(t0))
        shutil.copytree(src, copy)
        os.remove(os.path.join(copy, manifest.MANIFEST_NAME))
        manifest.write(copy)
        after = hashlib.sha256(
            open(os.path.join(copy, manifest.MANIFEST_NAME), "rb").read()).hexdigest()
    return {"interval": t0, "sha256_before": before, "sha256_after": after,
            "equal": before == after}


# ---- V6 -------------------------------------------------------------------------

def v6(manifests):
    samples = [s["offset_ms"] for d in manifests.values() for s in d["clock_offset_samples"]]
    absolute = [abs(v) for v in samples]
    flagged = [t0 for t0, d in manifests.items()
               if d["clock_offset_abs_max_ms"] is not None
               and d["clock_offset_abs_max_ms"] > config.CLOCK_OFFSET_LIMIT_MS]
    return {"samples": len(samples),
            "mean_offset_ms": statistics.fmean(samples) if samples else None,
            "mean_abs_offset_ms": statistics.fmean(absolute) if absolute else None,
            "max_abs_offset_ms": max(absolute) if absolute else None,
            "limit_ms": config.CLOCK_OFFSET_LIMIT_MS,
            "intervals_over_limit": len(flagged),
            "intervals_over_limit_list": flagged[:50]}


# ---- V7 -------------------------------------------------------------------------

def v7(manifests, run):
    scored = [manifests[t] for t in run] or list(manifests.values())
    raw = [sum(d["streams"][s]["raw_bytes"] for s in config.STREAM_FILES) for d in scored]
    gz = [sum(d["streams"][s]["stored_bytes"] for s in config.STREAM_FILES) for d in scored]
    probe_path = os.path.join(config.ROOT, "tier-b-probe.json")
    probe = json.load(open(probe_path)) if os.path.exists(probe_path) else None
    tier_b = None
    if probe:
        ret = probe["retained_interval"]
        raw_per = probe["raw_bytes_per_interval"]["mean"]
        tier_b = {
            "frames_per_interval": probe["frames_per_interval"],
            "raw_bytes_per_interval": probe["raw_bytes_per_interval"],
            "retained_interval": ret,
            "gzip_ratio_on_retained": (ret["gzipped_bytes"] / ret["raw_bytes"]
                                       if ret["raw_bytes"] else None),
            "raw_bytes_per_day": raw_per * 288 if raw_per else None,
            "compressed_bytes_per_day": (
                raw_per * 288 * (ret["gzipped_bytes"] / ret["raw_bytes"])
                if raw_per and ret["raw_bytes"] else None),
            "whole_intervals": probe["whole_intervals"],
            "frames_total": probe["frames_total"],
            "bytes_total": probe["bytes_total"],
        }
    return {
        "tier_a_intervals_measured": len(scored),
        "tier_a_raw_bytes_per_interval": distribution([float(v) for v in raw]),
        "tier_a_gzipped_bytes_per_interval": distribution([float(v) for v in gz]),
        "tier_a_raw_bytes_per_day": statistics.fmean(raw) * 288 if raw else None,
        "tier_a_gzipped_bytes_per_day": statistics.fmean(gz) * 288 if gz else None,
        "tier_b": tier_b,
        "free_space_bytes_now": shutil.disk_usage(config.ROOT).free,
        "captured_bytes_now": sum(
            os.lstat(os.path.join(dp, f)).st_size
            for dp, _dn, fn in os.walk(config.ROOT) for f in fn),
    }


def main():
    manifests = load_manifests()
    run = scoring_run(manifests)
    doc = {
        "intervals_with_a_manifest": len(manifests),
        "scoring_run": {"length": len(run),
                        "first_T0": run[0] if run else None,
                        "last_T0": run[-1] if run else None},
        "V1_price_to_beat_identity": v1(run),
        "V2_settlement_rule": v2(run),
        "V3_gap_accounting": v3(manifests, run),
        "V4_read_only_proof": v4(),
        "V5_determinism": v5(run),
        "V6_clock_discipline": v6(manifests),
        "V7_footprint": v7(manifests, run),
    }
    sys.stdout.write(json.dumps(doc, sort_keys=True, indent=2, default=str) + "\n")


if __name__ == "__main__":
    main()
