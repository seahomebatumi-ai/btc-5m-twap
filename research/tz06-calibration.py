#!/usr/bin/env python3
"""TZ-06: p_fair calibration against venue-resolved labels. P and V1-V10, as counts.

The tests in TZ-06 section 6 are the Architect's. This file runs them and reports what they
return. It does not design, extend, relax or substitute them, and a red result is a finding,
not something to correct. It does abort, by assert, when the capture contradicts a premise
the scoring set rests on.

Every formula lives in `pfair.py` and every stream read goes through `analyze.py`; there is
no arithmetic of the model here. Read-only over the capture: nothing under
`/var/lib/btc-recorder/` is written, moved or deleted.

Run:  python3 -B tz06-calibration.py                 > results.json
      python3 -B tz06-calibration.py --tables        > tables.md
      python3 -B tz06-calibration.py --csv <path>    # the section 6 forensics file
"""

import collections
import decimal
import fractions
import json
import math
import os
import statistics
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pfair                                                               # noqa: E402
from pfair import D, MS, config                                           # noqa: E402
from pfair import first_at_or_after, last_at_or_before, published_equal    # noqa: E402
from analyze import load_manifests, reasons_for, venue                     # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
RECORDER = os.path.join(HERE, "recorder")

# TZ-06 section 4. The set is never shrunk to fit what is there.
SET_SIZE = 400

# TZ-06 section 6, P. At least 396 of the 400 reconstructions must agree with the venue.
P_REQUIRED = 396

# TZ-06 section 6, V4. The first 20 members, every scored tau. The factor is a ten-dollar move
# at BTC scale - the order of the interval's own moves, so the control is a realistic
# perturbation rather than a blow-up, and any leak of a future report would move the output by
# far more than rounding.
V4_MEMBERS = 20
PERTURBATION = D("1.0001")

# TZ-06 section 6, G2. Fixed bins, fixed eligibility, fixed region. None of this moves.
BIN_COUNT = 10
BIN_MIN_N = 20
REGION_TAIL = fractions.Fraction(1, 200)          # 0.005 in each tail: the central 99%
MAX_FAILING_BINS = 2


# ---- the scoring set, TZ-06 section 4 --------------------------------------------

def qualification(t0, manifests):
    """Section 4's five conditions for one interval: the reasons it fails, empty when it does not.

    Every condition that can be evaluated is evaluated, so a non-member discloses everything
    that is wrong with it rather than the first thing. `quotes_complete` is not read here and
    neither is the clock offset: section 4 makes neither a condition.
    """
    why = list(reasons_for(manifests.get(t0)))                       # condition 1
    info = venue(t0) if manifests.get(t0) else None
    if info is None:
        why.append("no S7 document")
    else:
        if info["resolved_up"] is None:                              # condition 2
            why.append("no resolved outcome")
        if info["price_to_beat"] is None:                            # condition 3
            why.append("no priceToBeat")
    if manifests.get(t0) is not None:
        if pfair.price_to_beat(t0, pfair.reports(t0, config.S1_STREAM)) is None:
            why.append("no twap60 at or after T0")                   # condition 4
        s3 = pfair.merged_stream(t0, config.S3_STREAM)               # condition 5
        if last_at_or_before(s3, (t0 - pfair.RUNUP_S) * MS) is None:
            why.append("no chainlink at or before T0-300")
        if last_at_or_before(s3, (t0 + config.INTERVAL_S - min(pfair.TAUS)) * MS) is None:
            why.append("no chainlink at or before T0+290")
    return why


def scoring_set(manifests, need=SET_SIZE):
    """Section 4: from the earliest interval directory, in T0 order, until `need` members.

    Every unit considered gets a row, member or not. The walk is over the 300 s grid rather
    than over the manifests, so an interval with no directory at all still gets one.
    """
    first = min(int(name) for name in os.listdir(os.path.join(config.ROOT, config.SERIES)))
    last = max(manifests) if manifests else first
    rows, members, t0 = [], 0, first
    while members < need and t0 <= last:
        why = qualification(t0, manifests)
        if not why:
            members += 1
        rows.append({"T0": t0, "reasons": why, "member": members if not why else None})
        t0 += config.INTERVAL_S
    return rows, members == need


# ---- scoring ---------------------------------------------------------------------

def score_member(t0):
    """Every scored observation for one member, plus what P and V2/V3 read from the same pass."""
    s1 = pfair.reports(t0, config.S1_STREAM)
    s3 = pfair.merged_stream(t0, config.S3_STREAM)
    info = venue(t0)
    rows = pfair.observations(t0, s1, s3)
    close_ms = (t0 + config.INTERVAL_S) * MS
    return {
        "T0": t0,
        "label": 1 if info["resolved_up"] else 0,
        "K": rows[0]["K"],
        "price_to_beat": info["price_to_beat"],
        "m_close": pfair.settlement_mean(t0, s3),
        "venue_twap60_at_close": first_at_or_after(s1, close_ms),
        "observations": rows,
        "gaps": {config.S3_STREAM: window_gaps(s3, t0),
                 config.S1_STREAM: window_gaps(pfair.merged_stream(t0, config.S1_STREAM), t0)},
    }


def window_gaps(rows, t0):
    """Gaps in ms between consecutive report timestamps inside [T0 - 300, T0 + 300]."""
    lo, hi = (t0 - pfair.RUNUP_S) * MS, (t0 + config.INTERVAL_S) * MS
    inside = [ts for ts, _v in rows if lo <= ts <= hi]
    return [inside[i + 1] - inside[i] for i in range(len(inside) - 1)]


# ---- the gate arithmetic, TZ-06 section 6 ----------------------------------------

def brier(pairs):
    """Mean squared error of a prediction against a 0/1 label."""
    assert pairs, "a Brier score over nothing is not a number"
    return sum((p - y) ** 2 for p, y in pairs) / len(pairs)


def bin_of(p):
    """The fixed bin `[0, 0.1), [0.1, 0.2), ... [0.9, 1.0]` that holds `p`."""
    for i in range(BIN_COUNT):
        if p < (i + 1) / BIN_COUNT:
            return i
    return BIN_COUNT - 1


def central_region(n, p):
    """The central 99% region of Binomial(n, p), computed exactly - never by approximation.

    `p` is an IEEE-754 double, so it is exactly the rational `a / b`. Every binomial term is
    then the integer `C(n, i) * a**i * (b - a)**(n - i)` over the common denominator `b**n`,
    and the whole comparison is integer arithmetic with no rounding anywhere. The region is
    `[lo, hi]` with at most 0.005 of the mass strictly below `lo` and at most 0.005 strictly
    above `hi`.
    """
    frac = fractions.Fraction(p)
    a, b = frac.numerator, frac.denominator
    c = b - a
    terms = [math.comb(n, i) * a ** i * c ** (n - i) for i in range(n + 1)]
    total = b ** n
    assert sum(terms) == total, "the binomial terms do not sum to one at n=%d" % n
    lo, run = n, 0
    for i, term in enumerate(terms):
        if (run + term) * REGION_TAIL.denominator > total * REGION_TAIL.numerator:
            lo = i
            break
        run += term
    hi, run = 0, 0
    for i in range(n, -1, -1):
        if (run + terms[i]) * REGION_TAIL.denominator > total * REGION_TAIL.numerator:
            hi = i
            break
        run += terms[i]
    return lo, hi


def calibration(pairs):
    """One tau's calibration table: the ten fixed bins, each with its exact region."""
    bins = [{"bin": i, "lo": i / BIN_COUNT, "hi": (i + 1) / BIN_COUNT, "n": 0,
             "mean_prediction": None, "observed_up": 0, "region": None, "eligible": False,
             "fails": False} for i in range(BIN_COUNT)]
    held = collections.defaultdict(list)
    for p, y in pairs:
        idx = bin_of(p)
        held[idx].append(p)
        bins[idx]["n"] += 1
        bins[idx]["observed_up"] += y
    for idx, ps in held.items():
        row = bins[idx]
        row["mean_prediction"] = statistics.fmean(ps)
        row["eligible"] = row["n"] >= BIN_MIN_N
        if row["eligible"]:
            row["region"] = list(central_region(row["n"], row["mean_prediction"]))
            row["fails"] = not (row["region"][0] <= row["observed_up"] <= row["region"][1])
    return bins


def table_for(tau, rows, key, constant_brier):
    """V6, V7 and V8 all report this shape; only the prediction column differs."""
    pairs = [(r[key], r["label"]) for r in rows]
    bins = calibration(pairs)
    return {
        "tau": tau, "n": len(pairs),
        "observed_up_rate": sum(y for _p, y in pairs) / len(pairs),
        "brier": brier(pairs), "brier_constant": constant_brier,
        "beats_constant": brier(pairs) < constant_brier,
        "eligible_bins": sum(1 for b in bins if b["eligible"]),
        "failing_bins": sum(1 for b in bins if b["fails"]),
        "bins": bins,
    }


# ---- V4 --------------------------------------------------------------------------

def perturb_after(rows, ts_ms):
    """Every report timestamped after `ts_ms`, multiplied by the constant. A new list."""
    return [(ts, v * PERTURBATION if ts > ts_ms else v) for ts, v in rows]


def perturb_one(rows, idx):
    """One report multiplied by the constant. A new list."""
    return [(ts, v * PERTURBATION if i == idx else v) for i, (ts, v) in enumerate(rows)]


def last_readable(rows, ts_ms):
    """The index of the last report at or before `ts_ms`."""
    hit = None
    for i, (ts, _v) in enumerate(rows):
        if ts <= ts_ms:
            hit = i
        else:
            break
    return hit


def v4(members):
    """Causality by perturbation: bit-identical under the future, moved by the last readable.

    The control is reported twice. `..._p_fair_moved` is the count section 6 names. `..._moved`
    is the same control judged on the model's output as a whole - `state`, `sd`, `p_fair` - and
    it is the one that proves the reader is read, because `Phi` saturates: once `state / sd` is
    beyond about eight, `p_fair` is exactly 1.0 as a double and no perturbation of any size can
    move it further. `saturated_observations` counts those, so the two figures reconcile.
    """
    identical = moved = moved_k = considered = 0
    moved_p = moved_k_p = saturated = 0
    survivors = []
    for t0 in members[:V4_MEMBERS]:
        s1 = pfair.reports(t0, config.S1_STREAM)
        s3 = pfair.merged_stream(t0, config.S3_STREAM)
        k_idx = next(i for i, (ts, _v) in enumerate(s1) if ts >= t0 * MS)
        for tau in pfair.TAUS:
            considered += 1
            at = (t0 + config.INTERVAL_S - tau) * MS
            base = pfair.observations(t0, s1, s3, taus=(tau,))[0]
            future = pfair.observations(t0, perturb_after(s1, at), perturb_after(s3, at),
                                        taus=(tau,))[0]
            same = (future["p_fair"] == base["p_fair"] and future["state"] == base["state"]
                    and future["sd"] == base["sd"])
            identical += same
            if not same:
                survivors.append({"T0": t0, "tau": tau, "base": base["p_fair"],
                                  "perturbed": future["p_fair"]})
            saturated += base["p_fair"] in (0.0, 1.0)
            control = pfair.observations(t0, s1, perturb_one(s3, last_readable(s3, at)),
                                         taus=(tau,))[0]
            moved_p += control["p_fair"] != base["p_fair"]
            moved += (control["p_fair"], control["state"]) != (base["p_fair"], base["state"])
            k_control = pfair.observations(t0, perturb_one(s1, k_idx), s3, taus=(tau,))[0]
            moved_k_p += k_control["p_fair"] != base["p_fair"]
            moved_k += (k_control["p_fair"], k_control["state"]) != (base["p_fair"],
                                                                    base["state"])
    return {
        "members": len(members[:V4_MEMBERS]), "taus": list(pfair.TAUS),
        "comparisons": considered,
        "bit_identical_under_future_perturbation": identical,
        "leaks": considered - identical,
        "leaking_observations": survivors,
        "negative_control_last_readable_chainlink_moved": moved,
        "negative_control_last_readable_chainlink_p_fair_moved": moved_p,
        "negative_control_K_report_moved": moved_k,
        "negative_control_K_report_p_fair_moved": moved_k_p,
        "saturated_observations": saturated,
        "factor": str(PERTURBATION),
    }


# ---- V5 and V9: counts taken from the runs of the two other instruments ----------

def run(cmd, cwd):
    out = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return out.returncode, out.stdout, out.stderr


def v5():
    """The analytic self-tests of section 6 V5, run and counted - never transcribed."""
    code, out, err = run([sys.executable, "-B", "selftest-pfair.py"], HERE)
    counts = {}
    for line in out.splitlines():
        if line.endswith("checks passed") and ":" in line:
            name, rest = line.split(":", 1)
            counts[name.strip()] = int(rest.split()[0])
    return {"command": "python3 -B selftest-pfair.py", "exit_status": code,
            "V5_checks_passed": counts.get("V5"), "machinery_checks_passed":
            counts.get("section 3 machinery"), "stderr_tail": err.strip().splitlines()[-1:]}


def v9():
    """R-c: the repaired analyzer, run, with the TZ-04b counts it must reproduce."""
    code, out, err = run([sys.executable, "-B", "analyze.py"], RECORDER)
    doc = json.loads(out) if code == 0 else None
    expected = {"units_considered": 215, "members": 200, "non_members": 15,
                "R1": 200, "R2": 175, "R3": 181}
    got = None
    if doc is not None:
        rules = doc["V2_settlement_rule"]["agreements"]
        got = {"units_considered": doc["scoring_set"]["rows_disclosed"],
               "members": doc["scoring_set"]["members"],
               "non_members": sum(1 for r in doc["rows"] if r["member"] is None),
               "R1": rules["R1"], "R2": rules["R2"], "R3": rules["R3"]}
    reasons = (dict(sorted(collections.Counter(
        "+".join(r["reasons"]) for r in doc["rows"] if r["reasons"]).items()))
        if doc is not None else None)
    return {"command": "python3 -B analyze.py", "exit_status": code,
            "expected_TZ_04b": expected, "observed": got,
            "reproduces": got == expected,
            "differences": None if got == expected else
            {k: [expected[k], got[k]] for k in expected if got is None or got[k] != expected[k]},
            "non_member_reasons": reasons,
            "next_start_recv_ns": doc["start"]["next_start_recv_ns"] if doc else None,
            "stderr_tail": err.strip().splitlines()[-1:]}


# ---- the document ----------------------------------------------------------------

CSV_HEADER = ["T0", "tau", "K", "S_t", "m_r", "sigma_live", "sigma_pre", "state", "sd",
              "p_fair", "label"]


def csv_text(scored):
    """Section 6's forensics file: one row per scored observation, in T0 then tau order.

    `sd` and `p_fair` are the `sigma_live` figures, which are the ones the gate reads. The
    `sigma_pre` pair is re-derivable by hand from `sigma_pre`, `tau` and `state` alone, which
    is why section 6 names eleven columns and not thirteen.
    """
    lines = [",".join(CSV_HEADER)]
    for member in scored:
        for row in member["observations"]:
            lines.append(",".join([
                str(row["T0"]), str(row["tau"]), str(row["K"]), str(row["S_t"]),
                "" if row["m_r"] is None else str(row["m_r"]), str(row["sigma_live"]),
                str(row["sigma_pre"]), str(row["state"]), str(row["sd"]),
                repr(row["p_fair"]), str(member["label"])]))
    return "\n".join(lines) + "\n"


def build():
    manifests = load_manifests()
    rows, full = scoring_set(manifests)
    members = [r["T0"] for r in rows if r["member"]]
    assert full, "section 4: only %d of %d intervals qualify; the set is never shrunk" % (
        len(members), SET_SIZE)

    scored = [score_member(t0) for t0 in members]
    labels = [m["label"] for m in scored]
    up_rate = sum(labels) / len(labels)
    constant_brier = brier([(up_rate, y) for y in labels])

    # P, evaluated and reported before any calibration score exists.
    agree = sum(1 for m in scored if (m["m_close"] >= m["K"]) == bool(m["label"]))
    double_agree = sum(1 for m in scored
                       if (float(m["m_close"]) >= float(m["K"])) == bool(m["label"]))
    residuals = [abs(m["m_close"] - m["venue_twap60_at_close"]) for m in scored]
    p_doc = {
        "definition": "sign of the chainlink-reconstructed [T0+240, T0+300] mean against K, "
                      "compared with the venue's resolved outcome",
        "n": len(scored), "agree": agree, "disagree": len(scored) - agree,
        "required": P_REQUIRED, "passes": agree >= P_REQUIRED,
        "agreement_rate_3dp": "%.3f" % (agree / len(scored)),
        "agree_when_compared_as_doubles": double_agree,
        "disagreeing_intervals": [{"T0": m["T0"], "m_close_minus_K": str(m["m_close"] - m["K"]),
                                   "label": m["label"]}
                                  for m in scored
                                  if (m["m_close"] >= m["K"]) != bool(m["label"])],
        "reconstruction_residual_usd": {
            "median_abs": str(statistics.median(sorted(residuals))),
            "worst_abs": str(max(residuals)),
            "worst_at_T0": scored[residuals.index(max(residuals))]["T0"],
            "median_signed": str(statistics.median(sorted(
                m["m_close"] - m["venue_twap60_at_close"] for m in scored))),
        },
    }

    doc = {
        "scoring_set": {
            "size_required": SET_SIZE, "full": full, "members": len(members),
            "units_considered": len(rows),
            "first_T0": rows[0]["T0"], "last_T0": rows[-1]["T0"],
            "first_member_T0": members[0], "last_member_T0": members[-1],
            "non_members": len(rows) - len(members),
            "reason_counts": dict(sorted(collections.Counter(
                "+".join(r["reasons"]) for r in rows if r["reasons"]).items())),
        },
        "rows": rows,
        "P_precondition": p_doc,
        "V3_K_reconstruction": None,
        "V4_causality": None,
        "V5_model_self_tests": None,
        "V9_R_c": None,
    }

    # V3 - K against the venue's published price to beat.
    k_res = [abs(m["K"] - m["price_to_beat"]) for m in scored]
    doc["V3_K_reconstruction"] = {
        "n": len(scored),
        "equal_at_published_precision": sum(1 for m in scored
                                            if published_equal(m["K"], m["price_to_beat"])),
        "strict_decimal_equal": sum(1 for m in scored if m["K"] == m["price_to_beat"]),
        "median_abs_residual_usd": str(statistics.median(sorted(k_res))),
        "worst_residual_usd": str(max(k_res)),
        "worst_at_T0": scored[k_res.index(max(k_res))]["T0"],
    }

    # V2 - feed adequacy, plus P's counts and the reconstruction residual.
    per_stream = {}
    for stream in (config.S3_STREAM, config.S1_STREAM):
        pooled = [g for m in scored for g in m["gaps"][stream]]
        worst = max(scored, key=lambda m: max(m["gaps"][stream], default=0))
        per_stream[stream] = {
            "window": "[T0-300, T0+300]", "members": len(scored), "gaps": len(pooled),
            "median_gap_ms": statistics.median(sorted(pooled)),
            "max_gap_ms": max(pooled), "max_gap_at_T0": worst["T0"],
            "reports_per_member_median": statistics.median(
                sorted(len(m["gaps"][stream]) + 1 for m in scored)),
        }
    # A member's own directory is clean by condition 1, but its run-up window [T0-300, T0-90]
    # is covered only by the preceding directory, whose manifest may record a disconnect of its
    # own. Section 4 does not make that a condition and the set is never shrunk, so these stay
    # members; the count is disclosed here because section 3 says no value is carried across a
    # gap the manifest records as a disconnect, and for these intervals the step function does.
    inherited = [m["T0"] for m in scored
                 if (manifests.get(m["T0"] - config.INTERVAL_S) or {}).get("disconnect_count")]
    doc["V2_feed_adequacy"] = {
        "per_stream": per_stream, "P": p_doc,
        "members_reading_run_up_from_a_directory_that_recorded_a_disconnect": len(inherited),
        "their_T0s": inherited,
    }

    if not p_doc["passes"]:
        # Section 6: if P fails the gate is not evaluated, Phase 1 stays open, and the report
        # proposes nothing. The instruments that do not depend on a calibration score still run.
        doc["V4_causality"] = v4(members)
        doc["V5_model_self_tests"] = v5()
        doc["V9_R_c"] = v9()
        doc["gate"] = {"evaluated": False,
                       "reason": "P failed: %d of %d, %d required" % (agree, len(scored),
                                                                     P_REQUIRED)}
        return doc, scored

    taus = list(pfair.TAUS)
    at_tau = {tau: [dict(r, label=m["label"]) for m in scored
                    for r in m["observations"] if r["tau"] == tau] for tau in taus}
    live = {tau: table_for(tau, at_tau[tau], "p_fair", constant_brier) for tau in taus}
    pre = {tau: table_for(tau, at_tau[tau], "p_fair_pre", constant_brier) for tau in taus}

    gated = list(pfair.GATED_TAUS)
    g1 = {tau: live[tau]["beats_constant"] for tau in gated}
    failing = {tau: live[tau]["failing_bins"] for tau in gated}
    g2_total = sum(failing.values())
    doc["V4_causality"] = v4(members)
    doc["V5_model_self_tests"] = v5()
    doc["V6_calibration_sigma_live"] = {"gated_taus": gated,
                                        "constant": up_rate,
                                        "brier_constant": constant_brier,
                                        "per_tau": {tau: live[tau] for tau in gated}}
    doc["V6_calibration_sigma_live"]["saturated_p_fair"] = {
        tau: sum(1 for r in at_tau[tau] if r["p_fair"] in (0.0, 1.0)) for tau in gated}
    doc["V7_tau_10"] = {"tau": 10, "threshold": None, "table": live[10],
                        "saturated_p_fair": sum(1 for r in at_tau[10]
                                                if r["p_fair"] in (0.0, 1.0))}
    doc["V8_sigma_pre"] = {"threshold": None,
                           "per_tau": {tau: {"brier": pre[tau]["brier"],
                                             "beats_constant": pre[tau]["beats_constant"],
                                             "eligible_bins": pre[tau]["eligible_bins"],
                                             "failing_bins": pre[tau]["failing_bins"]}
                                       for tau in taus},
                           "tables": pre}
    doc["V9_R_c"] = v9()
    doc["gate"] = {
        "evaluated": True,
        "G1": {"rule": "Brier(p_fair) < Brier(c) at every gated tau",
               "constant_c": up_rate, "brier_constant": constant_brier,
               "brier_p_fair": {tau: live[tau]["brier"] for tau in gated},
               "per_tau": g1, "passes": all(g1.values()),
               "margin": {tau: constant_brier - live[tau]["brier"] for tau in gated}},
        "G2": {"rule": "at most %d eligible bins may fail across the six taus" % MAX_FAILING_BINS,
               "eligible_bins": {tau: live[tau]["eligible_bins"] for tau in gated},
               "failing_bins": failing, "total_failing": g2_total,
               "allowed": MAX_FAILING_BINS, "passes": g2_total <= MAX_FAILING_BINS},
        "passes": all(g1.values()) and g2_total <= MAX_FAILING_BINS,
    }
    return doc, scored


# ---- output ----------------------------------------------------------------------

def bin_rows(table):
    out = []
    for b in table["bins"]:
        region = "—" if b["region"] is None else "[%d, %d]" % tuple(b["region"])
        out.append("| %.1f–%.1f | %d | %s | %d | %s | %s | %s |" % (
            b["lo"], b["hi"], b["n"],
            "—" if b["mean_prediction"] is None else "%.4f" % b["mean_prediction"],
            b["observed_up"], region, "yes" if b["eligible"] else "no",
            "FAIL" if b["fails"] else ("ok" if b["eligible"] else "—")))
    return out


BIN_HEAD = ["| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |",
            "|---|---|---|---|---|---|---|"]


def tables(doc):
    out = ["### V1 — set formation, every unit considered", "",
           "| # | T0 | open (UTC) | member | reason not a member |", "|---|---|---|---|---|"]
    for i, r in enumerate(doc["rows"], 1):
        out.append("| %d | %d | %s | %s | %s |" % (
            i, r["T0"], time.strftime("%Y-%m-%d %H:%M", time.gmtime(r["T0"])),
            r["member"] or "—", " + ".join(r["reasons"]) or "—"))
    if not doc["gate"]["evaluated"]:
        return "\n".join(out) + "\n"
    for name, block, key in (("V6 — calibration, sigma_live", doc["V6_calibration_sigma_live"],
                              "per_tau"),
                             ("V8 — calibration, sigma_pre", doc["V8_sigma_pre"], "tables")):
        for tau, table in sorted(block[key].items(), key=lambda kv: -int(kv[0])):
            out += ["", "### %s, tau = %s" % (name, tau), "",
                    "n = %d · observed Up rate %.4f · Brier %.6f · Brier(constant) %.6f"
                    % (table["n"], table["observed_up_rate"], table["brier"],
                       table["brier_constant"]), ""] + BIN_HEAD + bin_rows(table)
    t7 = doc["V7_tau_10"]["table"]
    out += ["", "### V7 — tau = 10, sigma_live, no threshold", "",
            "n = %d · observed Up rate %.4f · Brier %.6f · Brier(constant) %.6f"
            % (t7["n"], t7["observed_up_rate"], t7["brier"], t7["brier_constant"]),
            ""] + BIN_HEAD + bin_rows(t7)
    return "\n".join(out) + "\n"


def main(argv):
    doc, scored = build()
    if argv[1:2] == ["--csv"]:
        path = argv[2]
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(csv_text(scored))
        sys.stdout.write("%s\n%d lines\n" % (path, len(csv_text(scored).splitlines())))
        return 0
    if argv[1:] == ["--tables"]:
        sys.stdout.write(tables(doc))
        return 0
    sys.stdout.write(json.dumps(doc, sort_keys=True, indent=2, default=str) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
