#!/usr/bin/env python3
"""TZ-07b: the dispersion of the settlement quantity, measured directly, and the scale frozen from it.

TZ-07a measured the oracle feed's variance-time curve and the measurement stands. Its
composition into `sd` does not: `g(h)` is the dispersion of a single increment over lag `h`,
and the quantity the pricer's denominator describes is not an increment. At `tau >= 60` the
settlement value is the feed's mean over the last sixty seconds, so the residual is a lead of
`tau - 60` seconds plus a sixty-second average, and multiplying the whole horizon by a ratio
belonging to the lead alone scales the averaging part by the wrong number.

M1 here measures the dispersion of the exact random variable the constant divides, over the
same closed 400 members, from the oracle feed alone. M2 freezes it into `pfair.py` as
`SD_SCALE` and this file asserts, per tau and before it prints anything, that what is in the
pricer is what was measured.

Nothing here is a formula of its own. `pfair.py` holds the model, the merged stream, the
one-second grid, the time-weighted step-function mean and the realised-sigma estimator;
`analyze.py` holds the only stream reader; `tz06-calibration.py` holds set formation; and
TZ-07a's disconnect rule, causality test and data count are imported from
`tz07a-variance-time.py` rather than re-determined. Read-only over the capture: nothing under
`/var/lib/btc-recorder/` is written, moved or deleted.

No outcome is read: no `resolution.json`, no settled field, no label, no calibration
statistic. The order book is not opened.

Run:  python3 -B tz07b-settlement-dispersion.py                 > results.json
      python3 -B tz07b-settlement-dispersion.py --tables        > tables.md
      python3 -B tz07b-settlement-dispersion.py --emit-scale    # the M2 literals, for pfair.py
      python3 -B tz07b-settlement-dispersion.py --v6            # section 7 V6, on its own
"""

import array
import bisect
import hashlib
import importlib.util
import json
import os
import statistics
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import pfair                                                               # noqa: E402
from pfair import D, MS, config                                            # noqa: E402
from analyze import load_manifests                                         # noqa: E402


def _load(name, filename):
    """Import a module whose filename carries a hyphen, so it cannot be `import`ed by name."""
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# Section 4: the disconnect rule is TZ-07a M6's and is imported, never re-determined here.
# Section 7 V2 and V6 are TZ-07a's own instruments, called for the same reason. `tz06` comes
# through TZ-07a because TZ-07a already loads it; loading it twice would be two module objects
# and two copies of one set.
tz07a = _load("tz07avariancetime", "tz07a-variance-time.py")
tz06 = tz07a.tz06

# Section 4: the grid is TZ-07a's, [T0 - 300, T0 + 300] inclusive, 601 points.
GRID_LO = tz07a.GRID_LO
GRID_HI = tz07a.GRID_HI
GRID_POINTS = tz07a.GRID_POINTS

# Section 4: the two consistency constants that turn a robust spread into a Gaussian scale,
# and the normal's own tail fractions. All five are reported against, never gated on.
MAD_TO_SIGMA = D("0.674490")
IQR_TO_SIGMA = D("1.348980")
NORMAL_TAIL = {1: "0.3173", 2: "0.0455", 3: "0.0027"}

# Section 7 V4. TZ-07a section 2.1's fifteen pooled `g(h)`, as that report printed them. The
# comparison is made at six significant digits, which is what section 7 V4 requires.
TZ07A_G_POOLED = {1: "1.000000", 2: "1.276654", 5: "1.610822", 10: "1.818539",
                  20: "1.956092", 30: "1.950510", 50: "1.946911", 60: "1.967584",
                  80: "2.061844", 100: "2.092458", 140: "2.134709", 180: "2.174995",
                  200: "2.182997", 240: "2.198011", 300: "2.202299"}

# Section 7 V4. TZ-06 section 2.8's P, reproduced by the unmodified pipeline. The six Brier
# values are compared inside TZ-07a's own V4 helper and counted here; no calibration statistic
# is carried out of this file.
TZ06_P_AGREE = tz07a.TZ06_P_AGREE
TZ06_BRIER_COUNT = len(tz07a.TZ06_BRIER)

# Section 6.2. The four checks that encode the superseded composition and are deleted by name,
# and the counts the two untouched families keep.
DELETED_SELFTESTS = ("tz07a_the_near_branch_is_untouched",
                     "tz07a_the_correction_at_the_boundary",
                     "tz07a_the_correction_on_the_far_branch",
                     "tz07a_the_table_is_a_table_of_literals")
V5_EXPECTED = 56
MACHINERY_EXPECTED = 18

# Section 7 V1's guard: how many anchors per tau of the first member are priced twice, once
# through the bounded slice and once through the whole stream.
GUARD_ANCHORS = 25


# ---- the member set, TZ-06 section 4 re-derived -----------------------------------

def members_and_manifests():
    """The 400 TZ-06 members, re-derived by calling `tz06-calibration.scoring_set`.

    Section 3: never transcribed. The walk stops at the 400th member, so a set that closed on
    2026-09-12 is unaffected by every directory written since.
    """
    manifests = load_manifests()
    rows, full = tz06.scoring_set(manifests)
    members = [r["T0"] for r in rows if r["member"]]
    assert full, "section 3: only %d of %d intervals qualify; the set is TZ-06's and is not " \
                 "re-cut here" % (len(members), tz06.SET_SIZE)
    return members, manifests, rows


def member_list_sha(members):
    """SHA-256 of the sorted member `T0` list, joined by newlines, with no trailing newline.

    Section 3: one value any later TZ can compare its own set against, instead of comparing
    four hundred transcribed epochs.
    """
    text = "\n".join(str(t0) for t0 in sorted(members))
    return hashlib.sha256(text.encode("ascii")).hexdigest()


# ---- M1, the dispersion of the settlement quantity --------------------------------

def horizon_sd(tau, sigma):
    """`sigma * sqrt(H(tau))` - the denominator section 4 divides `Y` by.

    It is not written out here. `pfair.state_and_sd` already returns exactly this product as
    the uncorrected `sd`, on both branches: `sigma * sqrt(tau - 40)` at or above sixty and
    `sigma * sqrt(tau**3 / 10800)` below it. Taking it from there is what makes the horizon
    the constant is measured against and the horizon the pricer uses the same object rather
    than two agreeing copies. `state` is not used, so the three price arguments are
    placeholders and cannot reach the result.
    """
    return pfair.state_and_sd(tau, D(0), D(0), sigma, D(0))[1]


def mean_over(rows, keys, t0, a, b):
    """`pfair.time_weighted_mean` over `[T0 + a, T0 + b]`, handed the reports it reads.

    The window is bisected before the call: the slice opens at the last report at or before
    `T0 + a`, which is the seed `time_weighted_mean` would pick out of the whole stream, and
    ends before the first report at or after `T0 + b`, which that function breaks on without
    reading. The mean is therefore the mean of the whole stream, bit for bit - an argument
    narrowed, not a formula rewritten. It is narrowed because M1 takes 1.39 million means and
    each would otherwise rescan a twelve-hundred-report stream. V1's guard asserts the
    equality on a sample rather than leaving it argued.
    """
    a_ms, b_ms = (t0 + a) * MS, (t0 + b) * MS
    lo = bisect.bisect_right(keys, a_ms) - 1
    if lo < 0:
        return None
    return pfair.time_weighted_mean(rows[lo:bisect.bisect_left(keys, b_ms)], a_ms, b_ms)


def residual(rows, keys, t0, grid, a, tau):
    """Section 4's `Y(a, tau)`: the residual the model's `sd` claims to describe, at anchor `a`.

        tau >= 60:   mean(a + tau - 60, a + tau) - P(a)
        tau <  60:   (tau / 60) * ( mean(a, a + tau) - P(a) )

    Above the boundary this is the settlement average itself minus the reading in force at the
    anchor. Below it, it is the future part of that average carrying the weight the model
    gives it; the realised part carries no dispersion and is already inside `state`.
    """
    p_a = grid[a - GRID_LO]
    if tau >= pfair.SETTLEMENT_S:
        mean = mean_over(rows, keys, t0, a + tau - pfair.SETTLEMENT_S, a + tau)
        return None if mean is None else mean - p_a
    mean = mean_over(rows, keys, t0, a, a + tau)
    if mean is None:
        return None
    return (D(tau) / D(pfair.SETTLEMENT_S)) * (mean - p_a)


def member_r(t0, manifests):
    """Every admissible `r = Y / (sigma * sqrt(H))` for one member, per tau.

    `sigma(tau)` is `pfair.realised_sigma` over the causal window `[T0 - 300, T0 + (300 - tau)]`
    - the same `sigma_live` the pricer reads at that checkpoint, so the constant measured here
    is the constant that pricer needs. Anchors are every integer `a` with `[a, a + tau]` inside
    the grid, and an anchor whose closed span contains a second inside a recorded outage is
    dropped under TZ-07a M6's rule.
    """
    s3 = pfair.merged_stream(t0, config.S3_STREAM)
    keys = [ts for ts, _value in s3]
    grid = pfair.second_grid(s3, t0 + GRID_LO, t0 + GRID_HI)
    assert len(grid) == GRID_POINTS, "interval %d gave %d grid points" % (t0, len(grid))
    assert all(value is not None for value in grid), \
        "interval %d has no chainlink report at or before T0-300" % t0
    pre = tz07a.excluded_prefix(tz07a.excluded_seconds(t0, manifests))
    out = {}
    for tau in pfair.TAUS:
        sigma = pfair.realised_sigma(grid[:GRID_POINTS - tau])
        denominator = horizon_sd(tau, sigma)
        assert denominator > 0, \
            "interval %d at tau %d has sigma %s; there is no scale to divide by" % (
                t0, tau, sigma)
        values, total, pooled, dropped, checkpoint = array.array("d"), D(0), D(0), 0, None
        for a in range(GRID_LO, GRID_HI - tau + 1):
            i = a - GRID_LO
            if pre[i + tau + 1] - pre[i] > 0:
                dropped += 1
                continue
            y = residual(s3, keys, t0, grid, a, tau)
            assert y is not None, "interval %d at tau %d anchor %d has no mean" % (t0, tau, a)
            r = y / denominator
            values.append(float(r))
            total += r * r
            pooled += r
            if a == GRID_HI - tau:
                checkpoint = r
        out[tau] = {"values": values, "sum_squares": total, "sum": pooled,
                    "dropped": dropped, "checkpoint": checkpoint}
    return out


def slice_guard(t0, manifests):
    """V1's guard: the bounded slice is the stream `time_weighted_mean` would have read.

    On the first member, at every tau, `GUARD_ANCHORS` anchors spread across the grid are
    priced twice - once through the bisected slice and once through the whole merged stream -
    and required to agree exactly. An argument narrowed wrongly is a silent wrong answer, so
    it is asserted here and counted, not argued in a comment.
    """
    s3 = pfair.merged_stream(t0, config.S3_STREAM)
    keys = [ts for ts, _value in s3]
    agreed = 0
    for tau in pfair.TAUS:
        anchors = range(GRID_LO, GRID_HI - tau + 1)
        step = max(len(anchors) // GUARD_ANCHORS, 1)
        for a in list(anchors)[::step][:GUARD_ANCHORS]:
            lo, hi = (a, a + tau) if tau < pfair.SETTLEMENT_S \
                else (a + tau - pfair.SETTLEMENT_S, a + tau)
            sliced = mean_over(s3, keys, t0, lo, hi)
            whole = pfair.time_weighted_mean(s3, (t0 + lo) * MS, (t0 + hi) * MS)
            assert sliced == whole, \
                "interval %d tau %d anchor %d: the slice gives %s, the whole stream %s" % (
                    t0, tau, a, sliced, whole)
            agreed += 1
    return {"member": t0, "anchors_priced_twice": agreed,
            "identical_to_the_whole_stream": agreed}


def dispersion(members, manifests):
    """M1 over the 400 members: `Lambda(tau)`, its diagnostics, and M6's drops per tau.

    `Lambda` is the raw root mean square, uncentred: the model assumes the residual has mean
    zero and the pooled mean is reported as a diagnostic rather than subtracted. The root mean
    square is the maximum-likelihood scale of the Gaussian the model is, and it needs no
    outcome and no second model; the MAD and IQR readings beside it carry no threshold and are
    there so that a later finding about tail shape has its data already measured.
    """
    values = {tau: array.array("d") for tau in pfair.TAUS}
    total = {tau: D(0) for tau in pfair.TAUS}
    pooled = {tau: D(0) for tau in pfair.TAUS}
    dropped = {tau: 0 for tau in pfair.TAUS}
    member_rms = {tau: [] for tau in pfair.TAUS}
    checkpoint_total = {tau: D(0) for tau in pfair.TAUS}
    checkpoint_n = {tau: 0 for tau in pfair.TAUS}
    touched = set()
    for t0 in members:
        rows = member_r(t0, manifests)
        for tau in pfair.TAUS:
            row = rows[tau]
            values[tau].extend(row["values"])
            total[tau] += row["sum_squares"]
            pooled[tau] += row["sum"]
            dropped[tau] += row["dropped"]
            if row["dropped"]:
                touched.add(t0)
            if row["values"]:
                member_rms[tau].append(
                    float((row["sum_squares"] / D(len(row["values"]))).sqrt()))
            if row["checkpoint"] is not None:
                checkpoint_total[tau] += row["checkpoint"] * row["checkpoint"]
                checkpoint_n[tau] += 1
    out = {}
    for tau in pfair.TAUS:
        taken = len(values[tau])
        assert taken, "tau %d kept no anchor at all; there is nothing to take a scale of" % tau
        lam = (total[tau] / D(taken)).sqrt()
        ordered = sorted(values[tau])
        centre = statistics.median(ordered)
        mad = statistics.median(sorted(abs(v - centre) for v in ordered))
        q1, _median, q3 = statistics.quantiles(ordered, n=4, method="inclusive")
        lam_float = float(lam)
        out[tau] = {
            "tau": tau,
            "anchors_per_member": GRID_POINTS - tau,
            "anchors_taken": taken,
            "anchors_dropped": dropped[tau],
            "anchors_possible": len(members) * (GRID_POINTS - tau),
            "lambda": lam,
            "pooled_mean_of_r": pooled[tau] / D(taken),
            "median_member_rms": statistics.median(sorted(member_rms[tau])),
            "members_with_a_reading": len(member_rms[tau]),
            "checkpoint_only_rms": (checkpoint_total[tau] / D(checkpoint_n[tau])).sqrt(),
            "checkpoint_only_n": checkpoint_n[tau],
            "mad_over_0_674490": D(repr(mad)) / MAD_TO_SIGMA,
            "iqr_over_1_348980": D(repr(q3 - q1)) / IQR_TO_SIGMA,
            "tail_fractions": {
                k: sum(1 for v in values[tau] if abs(v) > k * lam_float) / taken
                for k in sorted(NORMAL_TAIL)},
            "normal_tail_fractions": NORMAL_TAIL,
        }
    return {"members": len(members), "taus": list(pfair.TAUS),
            "grid": {"window": "[T0-300, T0+300]", "points": GRID_POINTS},
            "per_tau": out,
            "members_contributing_a_dropped_anchor": len(touched),
            "their_T0s": sorted(touched),
            "anchors_dropped_total": sum(dropped[tau] for tau in pfair.TAUS),
            "anchors_taken_total": sum(out[tau]["anchors_taken"] for tau in pfair.TAUS)}


# ---- M2, the freeze ---------------------------------------------------------------

def emit_scale(per_tau):
    """The M2 literals exactly as they are written into `pfair.py`."""
    body = ", ".join('%d: D("%s")' % (tau, tz07a.six_significant(per_tau[tau]["lambda"]))
                     for tau in pfair.TAUS)
    return "SD_SCALE = {%s}\n" % body


def check_frozen_literals(per_tau):
    """Section 5: the literals in `pfair.py` are this measurement, asserted before anything prints.

    A pricer that re-derives its constants from whatever data it is pointed at cannot be
    tested out of sample, and TZ-08 scores the file as it stands.
    """
    checks = []
    for tau in pfair.TAUS:
        want = tz07a.six_significant(per_tau[tau]["lambda"])
        got = pfair.SD_SCALE[tau]
        assert got == want, "pfair.SD_SCALE[%d] is %s; M1 measures %s" % (tau, got, want)
        checks.append({"tau": tau, "measured_6sd": want, "in_pfair": got, "equal": True})
    assert sorted(pfair.SD_SCALE) == sorted(pfair.TAUS), \
        "pfair.SD_SCALE carries %s; the pricer serves %s" % (
            sorted(pfair.SD_SCALE), sorted(pfair.TAUS))
    return checks


# ---- V4, the two regressions ------------------------------------------------------

def v4_tz06():
    """TZ-06's pipeline, unmodified, still reproducing section 2.8's Briers and its P.

    TZ-07a's own V4 helper runs it and compares; only counts leave this function, because
    section 2 forbids a calibration statistic anywhere in this TZ's report.
    """
    doc = tz07a.v4()
    observed = doc["observed_brier"] or {}
    reproduced = sum(1 for tau, value in tz07a.TZ06_BRIER.items()
                     if observed.get(int(tau)) == value)
    return {"command": doc["command"], "exit_status": doc["exit_status"],
            "tz06_calibration_sha256": doc["tz06_calibration_sha256"],
            "brier_values_expected": TZ06_BRIER_COUNT,
            "brier_values_reproduced_to_six_decimals": reproduced,
            "P_agree_expected": TZ06_P_AGREE, "P_agree_observed": doc["observed_P_agree"],
            "stderr_tail": doc["stderr_tail"]}


def v4_tz07a():
    """TZ-07a's instrument, with only section 6.3's removal applied, still reproducing its curve.

    The file is run as it now stands and the fifteen pooled `g(h)` are compared at six
    significant digits against what TZ-07a section 2.1 published. Nothing else is read out of
    its output.
    """
    out = subprocess.run([sys.executable, "-B", "tz07a-variance-time.py"],
                         cwd=HERE, capture_output=True, text=True)
    doc = json.loads(out.stdout) if out.returncode == 0 else None
    lags, agreed = {}, 0
    for lag, want in sorted(TZ07A_G_POOLED.items()):
        got = None if doc is None else doc["V1_curve"]["g_pooled"][str(lag)]
        same = got is not None and tz07a.six_significant(got) == tz07a.six_significant(want)
        agreed += same
        lags[lag] = {"published": want,
                     "observed_6sd": None if got is None else str(tz07a.six_significant(got)),
                     "equal": same}
    sha = subprocess.run(["sha256sum", "tz07a-variance-time.py"], cwd=HERE,
                         capture_output=True, text=True).stdout.split()[0]
    return {"command": "python3 -B tz07a-variance-time.py", "exit_status": out.returncode,
            "tz07a_variance_time_sha256": sha,
            "lags_expected": len(TZ07A_G_POOLED), "lags_reproduced": agreed,
            "per_lag": lags, "stderr_tail": out.stderr.strip().splitlines()[-1:]}


# ---- V5, the self-tests -----------------------------------------------------------

def v5():
    """`selftest-pfair.py`, run and counted - never transcribed.

    Section 6.2 deletes four checks by name because the specification they encode is
    superseded, and for no other reason. That the four are gone is asserted against the file's
    own source, and the family that replaces them is counted on its own.
    """
    out = subprocess.run([sys.executable, "-B", "selftest-pfair.py"],
                         cwd=HERE, capture_output=True, text=True)
    counts, names = {}, []
    for line in out.stdout.splitlines():
        if line.endswith("checks passed") and ":" in line:
            label, rest = line.split(":", 1)
            counts[label.strip()] = int(rest.split()[0])
        elif line.startswith("tz07b_"):
            names.append(line.strip())
    with open(os.path.join(HERE, "selftest-pfair.py"), encoding="utf-8") as handle:
        source = handle.read()
    still_there = [name for name in DELETED_SELFTESTS if name in source]
    assert out.returncode == 0, "selftest-pfair.py exited %d" % out.returncode
    assert not still_there, "section 6.2 deletes %s; the file still carries them" % still_there
    assert counts.get("V5") == V5_EXPECTED, "V5 is %s, not %d" % (counts.get("V5"), V5_EXPECTED)
    assert counts.get("section 3 machinery") == MACHINERY_EXPECTED, \
        "the machinery family is %s, not %d" % (counts.get("section 3 machinery"),
                                                MACHINERY_EXPECTED)
    assert names, "no tz07b_* check ran"
    return {"command": "python3 -B selftest-pfair.py", "exit_status": out.returncode,
            "V5_checks_passed": counts.get("V5"), "V5_expected": V5_EXPECTED,
            "machinery_checks_passed": counts.get("section 3 machinery"),
            "machinery_expected": MACHINERY_EXPECTED,
            "TZ_07b_checks_passed": counts.get("TZ-07b section 6"),
            "TZ_07b_check_families": names,
            "deleted_by_name": list(DELETED_SELFTESTS),
            "deleted_names_still_in_the_file": still_there,
            "stderr_tail": out.stderr.strip().splitlines()[-1:]}


# ---- the document ------------------------------------------------------------------

def build():
    members, manifests, rows = members_and_manifests()
    guard = slice_guard(members[0], manifests)
    m1 = dispersion(members, manifests)
    literals = check_frozen_literals(m1["per_tau"])
    return {
        "set": {"source": "TZ-06 section 4, re-derived by tz06-calibration.scoring_set",
                "units_considered": len(rows), "members": len(members),
                "first_T0": members[0], "last_T0": members[-1],
                "member_list_sha256": member_list_sha(members),
                "member_list_form": "the sorted T0 list joined by newlines, no trailing newline"},
        "V1_dispersion": m1,
        "V1_slice_guard": guard,
        "V2_causality": tz07a.v2(members),
        "V4_regression_tz06": v4_tz06(),
        "V4_regression_tz07a": v4_tz07a(),
        "V5_self_tests": v5(),
        "M2_frozen_literals": {"SD_SCALE_as_written":
                               {tau: pfair.SD_SCALE[tau] for tau in sorted(pfair.SD_SCALE)},
                               "literals_match_measurement": literals,
                               "emitted": emit_scale(m1["per_tau"]).strip()},
    }


def v6():
    """Section 7 V6, a separate invocation: how much test data exists at the moment of the run.

    It is not part of the determinism artifact, because it counts something still growing.
    TZ-07a's own helper is called; the question and the five conditions are unchanged.
    """
    return {"V6_test_data_available": tz07a.v8(load_manifests())}


# ---- output --------------------------------------------------------------------------

def dispersion_table(doc):
    m1 = doc["V1_dispersion"]
    out = ["### V1 - the dispersion of the settlement quantity, %d members" % m1["members"], "",
           "| tau | anchors/member | taken | dropped | **`Lambda(tau)`** | pooled mean of `r` | "
           "median member RMS | checkpoint-only RMS | `MAD/0.674490` | `IQR/1.348980` |",
           "|---|---|---|---|---|---|---|---|---|---|"]
    for tau in m1["taus"]:
        row = m1["per_tau"][tau]
        out.append("| %d | %d | %d | %d | **%.6f** | %+.6f | %.6f | %.6f | %.6f | %.6f |" % (
            tau, row["anchors_per_member"], row["anchors_taken"], row["anchors_dropped"],
            row["lambda"], row["pooled_mean_of_r"], row["median_member_rms"],
            row["checkpoint_only_rms"], row["mad_over_0_674490"], row["iqr_over_1_348980"]))
    out += ["", "### V1 - the empirical tails against the normal's", "",
            "| tau | `P(|r| > Lambda)` | normal | `P(|r| > 2 Lambda)` | normal | "
            "`P(|r| > 3 Lambda)` | normal |", "|---|---|---|---|---|---|---|"]
    for tau in m1["taus"]:
        row = m1["per_tau"][tau]
        out.append("| %d | %.4f | %s | %.4f | %s | %.4f | %s |" % (
            tau, row["tail_fractions"][1], NORMAL_TAIL[1], row["tail_fractions"][2],
            NORMAL_TAIL[2], row["tail_fractions"][3], NORMAL_TAIL[3]))
    return out


def tables(doc):
    return "\n".join(dispersion_table(doc)) + "\n"


def main(argv):
    if argv[1:] == ["--emit-scale"]:
        members, manifests, _rows = members_and_manifests()
        sys.stdout.write(emit_scale(dispersion(members, manifests)["per_tau"]))
        return 0
    if argv[1:] == ["--v6"]:
        sys.stdout.write(json.dumps(v6(), sort_keys=True, indent=2, default=str) + "\n")
        return 0
    doc = build()
    if argv[1:] == ["--tables"]:
        sys.stdout.write(tables(doc))
        return 0
    sys.stdout.write(json.dumps(doc, sort_keys=True, indent=2, default=str) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
