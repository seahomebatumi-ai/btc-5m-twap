#!/usr/bin/env python3
"""TZ-11a: the Student link, and the domain it is priced on.

Phase 1 answered no for `p_fair`, and TZ-10b answered why: the link. This file fits a Student's
`t` to the settlement residual `r` on the TZ-06 400 alone, measures a causal admissibility rule
on the same 400 - `sigma_hat` at or above its 30th percentile - checks that the three tables
frozen into `pfair.py` are what it measured, and scores the Student pricer on two disjoint
out-of-sample sets against the gate TZ-11a section 4 fixed before the second of them existed.
Nothing is re-fitted after the freeze except the stationarity refits section 3.3 names, and
none of those moves a constant.

This file is a driver. It holds the set rules, the profile-likelihood search, the admissibility
comparison, the influence refits, the gate arithmetic and the report tables. `r(a, tau)`, the
anchor enumeration and the horizon come from `tz07b-settlement-dispersion.py`; M6's disconnect
rule from `tz07a-variance-time.py` through it; set formation from `tz06-calibration.scoring_set`
and TZ-08a's own `the_set`; the calibration table, `brier` and the perturbation helpers from
`tz06-calibration.py`; `lambda_hat` from `tz07a-variance-time.py`, given the Student log CDF
through its `log_cdf` parameter; `kappa`, the one-second grid reader and the host reads from
`tz10b-sigma-or-link.py`; the Student link, both scales and the realised-sigma estimator from
`pfair.py`; the stream reader from `analyze.py`.

Outcomes are read in exactly the three places TZ-11a section 2 names: inside the committed
`tz06-calibration.qualification`, which every set formation calls; in M4 and M5, whose labels
`tz10b.m2_labels` reads for the two test sets alone; and in V4's third assertion, which calls
`tz07a.lambda_hat` at its default on the TZ-08a 400. No label of the fit set is read at all, and
M1, M2, M3 and section 5 read none.

Read-only over the capture: nothing under `/var/lib/btc-recorder/` is written, moved or deleted,
and neither `quotes.jsonl.gz` nor `gamma.json` is opened. The only files written are the four
outputs, into a directory asserted to lie outside the capture. The only subprocesses are `git`
and `selftest-pfair.py`, each a fixed argument list with no shell.

Run, on an interpreter that carries `numpy`:

      python -B tz11a-student-link.py --out <directory>
      python -B tz11a-student-link.py --emit        # the three tables, for pfair.py

`--out` writes `tz11a-results.json`, `tz11a-tables.md` and `tz11a-observations.csv`, none of
which carries a wall-clock time or a path, so two runs compare by `cmp`; and `tz11a-host.json`,
the run's own reads of the host and its timings, which differ from run to run by construction.
"""

import array
import ast
import collections
import hashlib
import importlib.util
import json
import math
import os
import statistics
import subprocess
import sys
import time

import numpy

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


# TZ-10b's instrument loads TZ-08a's, which loads TZ-07b's, TZ-07a's and TZ-06's, so all five
# come through it: loading any of them a second time would be two module objects.
tz10b = _load("tz10bsigmaorlink", "tz10b-sigma-or-link.py")
tz08a = tz10b.tz08a
tz07b = tz10b.tz07b
tz07a = tz10b.tz07a
tz06 = tz10b.tz06

# Section 3.0: the three sets. The two committed ones are identified by their member-list hashes;
# test 2 does not exist until the run forms it.
FIT_SHA256 = "6d94a346a47a04a1a0849968effd9023d7585fe628b304ba2ae7a15953ee67f9"
TEST1_SHA256 = "3b17729c050e5fbf8fed1bd0877d5dd5c229370609cd672c84eeed1ddc3d5762"
TEST2_AFTER = 1789296300
TEST2_NEED = 400
SETS = ("fit", "test1", "test2")
TEST_SETS = ("test1", "test2")
SET_NAMES = {"fit": "fit (TZ-06 400)", "test1": "test 1 (TZ-08a 400)",
             "test2": "test 2 (first 400 after 1789296300)"}

# Section 3.3: the six populations, in the order every table prints them.
POPULATIONS = tuple((name, kind) for name in SETS for kind in ("all", "admissible"))

# Section 3.0: TZ-07b's grid, [T0 - 300, T0 + 300] inclusive, and its anchor enumeration.
GRID_LO, GRID_HI, GRID_POINTS = tz07b.GRID_LO, tz07b.GRID_HI, tz07b.GRID_POINTS

# Section 3.1: the search, fixed before any data was seen.
NU_LO, NU_HI = 2.05, 60.0
S_LO, S_HI = 0.10, 10.0
SEARCH_REL_TOL = 1e-8
GOLDEN = (math.sqrt(5.0) - 1.0) / 2.0

# Section 3.1: the cost statement and its fail-fast.
FIRST_FIT_LIMIT_S = 60.0
FITS_REQUIRED = 63
PRIMARY_FITS = 42
INFLUENCE_FITS = 21

# Section 3.2: `ADMIT[tau]` is `statistics.quantiles(values, n=10, method="inclusive")[2]`.
ADMIT_QUANTILES = 10
ADMIT_INDEX = 2

# Section 4: the gate, quoted. G2's allowance is `tz06.MAX_FAILING_BINS`, read from the code.
G1_BRIER = 0.2496
G3_BAND = 0.15
G4_BAND = math.log(2.0)

# Section 4.1: the Architect's pre-registered prediction, printed beside what is measured.
PREDICTION = (("G1", "passes, 7 of 7, on both test sets"),
              ("G2", "passes on both test sets"),
              ("G3", "holds at tau 240, 180, 120 and 90 on both sets; fails at 30 or at 10 on "
                     "at least one"),
              ("G4", "holds at tau <= 120; fails at tau = 240 on test 1"),
              ("overall", "NO, and the failing gate is G4 at long tau"))

# Section 3.5: the observation the old gate hung on.
M5_T0, M5_TAU = 1789268400, 30

# Section 7 V2: the first 20 fit members at all seven taus.
V2_MEMBERS = 20

# Section 7 V4: TZ-07b's `Lambda`, TZ-08a V8's `Lambda_oos` and its seven `Lambda_oos / SD_SCALE`
# - the RMS of `u` - each exactly as its committed report printed it; TZ-08a's `lambda_hat` at
# tau = 30 as TZ-10b printed it to ten decimals; and the guard's member count.
TZ07B_LAMBDA = tz10b.TZ07B_LAMBDA
TZ08A_LAMBDA_OOS = tz10b.TZ08A_LAMBDA_OOS
TZ08A_RMS_U = {240: "1.045872", 180: "1.019185", 120: "0.928947", 90: "0.913252",
               60: "0.910412", 30: "0.913030", 10: "0.918385"}
V4_LAMBDA_TAU = 30
V4_LAMBDA = "2.0418426092"
V4_GUARD = 50

# Section 7 V7: the self-test counts, the 110 already there and the six added.
SELFTEST_COUNTS = {"V5": 56, "TZ-07b section 6": 30, "TZ-10b section 5.2": 6,
                   "TZ-11a section 5.2": 6, "section 3 machinery": 18}

# Section 7 V6: the five paths, the objects named, the twelve names `pfair.py` gains, and the
# four committed lines of `tz07a-variance-time.py` section 5.3 replaces, by their text.
FIVE_PATHS = ("pfair.py", "selftest-pfair.py", "tz07a-variance-time.py",
              "tz11a-student-link.py",
              "../CryptoReports/TZ-11a-student-link-and-domain-report.md")
PFAIR_NAMED = ("SD_SCALE", "corrected_sd", "phi", "log_phi", "p_fair", "far_branch",
               "near_branch", "state_and_sd", "TAUS", "GATED_TAUS")
PFAIR_ADDED = ("LOG_BETA_CF_MAX", "LOG_BETA_TOL", "log_beta", "_betacf", "log_betainc_reg",
               "log_t_cdf", "t_cdf", "ADMIT", "LINK_NU", "LINK_SCALE", "student_sd",
               "p_fair_student")
TZ07A_FILE = "tz07a-variance-time.py"
TZ07A_REPLACED = (
    "def log_likelihood(pairs, lam):",
    "def lambda_hat(pairs):",
    "        if log_likelihood(pairs, a) < log_likelihood(pairs, b):",
    "    ll_hat, ll_one = log_likelihood(pairs, lam), log_likelihood(pairs, 1.0)")
TZ07A_EXEMPT = ("lambda_hat", "log_likelihood")

# Section 0 and V1: free space at run start, and at every later read, asserted.
FLOOR_START_BYTES = 2060000000
FLOOR_BYTES = 2000000000

# One row per member per tau, at its checkpoint.
CSV_HEADER = ["T0", "set", "tau", "admissible", "label", "K", "S_t", "m_r", "state", "sigma_hat",
              "ADMIT", "sd_corrected", "sd_student", "z_corrected", "z_student",
              "p_fair_corrected", "p_t", "log_phi_z_corrected", "log_t_cdf_z_student", "Y", "r"]


# ---- V1 and V9: the host, read at the start, after the walk and at the end ------------

def host_read(when, t0s, floor):
    """The floor and V9's four facts at one instant. Asserted, so a breach stops the run."""
    free = tz10b.free_bytes()
    start = tz10b.newest_start()
    digest, files = tz10b.read_set(t0s)
    doc = {"when": when, "utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           "free_bytes": free, "floor_bytes": floor, "recorder_pids": tz10b.recorder_pids(),
           "newest_start_recv_ns": start["recv_ns"], "newest_start_sha": start["sha"],
           "interval_directories": len(os.listdir(os.path.join(config.ROOT, config.SERIES))),
           "read_set_sha256": digest, "read_set_files": files}
    assert free >= floor, "V1: %d bytes free at %s, below %d" % (free, when, floor)
    assert doc["recorder_pids"], "V9: no recorder process at %s" % when
    return doc


# ---- section 3.0 and V5: the sets --------------------------------------------------

def fit_set(manifests):
    """The TZ-06 400, through `tz06.scoring_set` at its defaults, asserted by its hash."""
    rows, full = tz06.scoring_set(manifests)
    members = [r["T0"] for r in rows if r["member"]]
    assert full and len(members) == tz06.SET_SIZE, \
        "section 3.0: %d fit members; the set is never shrunk" % len(members)
    assert tz07b.member_list_sha(members) == FIT_SHA256 == tz08a.TZ06_SHA256, \
        "V5: the fit set hashes to %s" % tz07b.member_list_sha(members)
    return rows, members


def the_sets(manifests):
    """All three sets, each formed by the committed code and never re-cut.

    Test 2 cannot be hash-gated and is not: it is disclosed unit by unit instead. If fewer than
    400 qualify the run stops, stating the count and the last slot on disk and nothing else.
    """
    rows_fit, fit = fit_set(manifests)
    rows1, test1, _doc = tz08a.the_set(manifests)
    rows2, full2 = tz06.scoring_set(manifests, need=TEST2_NEED, after=TEST2_AFTER)
    test2 = [r["T0"] for r in rows2 if r["member"]]
    if not full2:
        last = max(int(name) for name in os.listdir(os.path.join(config.ROOT, config.SERIES)))
        raise SystemExit("BLOCKED at section 3.0: %d of %d test-2 members qualify; the last "
                         "slot on disk is %d" % (len(test2), TEST2_NEED, last))
    sha = {"fit": tz07b.member_list_sha(fit), "test1": tz07b.member_list_sha(test1),
           "test2": tz07b.member_list_sha(test2)}
    assert sha["test1"] == TEST1_SHA256 == tz08a.SET_SHA256, \
        "V5: test 1 hashes to %s" % sha["test1"]
    assert min(test2) > TEST2_AFTER and len(test2) == TEST2_NEED, "section 3.0: test 2 is wrong"
    assert not set(fit) & set(test1), "section 3.0: fit and test 1 overlap"
    assert not set(fit) & set(test2), "section 3.0: fit and test 2 overlap"
    assert not set(test1) & set(test2), "section 3.0: test 1 and test 2 overlap"
    sets = {"fit": (rows_fit, fit), "test1": (rows1, test1), "test2": (rows2, test2)}
    doc = {}
    for name in SETS:
        rows, members = sets[name]
        outside = [r for r in rows if not r["member"]]
        doc[name] = {"units_considered": len(rows), "members": len(members),
                     "non_members": len(outside),
                     "non_member_reasons": dict(sorted(collections.Counter(
                         " + ".join(r["reasons"]) for r in outside).items())),
                     "first_unit": rows[0]["T0"], "last_unit": rows[-1]["T0"],
                     "first_member": members[0], "last_member": members[-1],
                     "member_list_sha256": sha[name]}
    doc["hashes_asserted"] = 2
    doc["hashes_reported"] = 1
    doc["pairwise_disjoint_asserted"] = 3
    return sets, doc


# ---- M1's raw material: one member, every anchor, the committed walk ---------------------

def walk_member(t0, manifests, guard):
    """One member: `r` at every admissible anchor at every tau, and what its checkpoint reads.

    The walk is `tz07b.member_r`'s step for step - the same stream, grid, horizon, enumeration
    and M6 rule, with `Y` from `tz07b.residual` - and each Decimal `r` becomes a float once,
    here, in ascending anchor order. Where `guard` is set, `member_r` itself is called beside
    this walk and every `r`, the Decimal sum of squares, the dropped count and the checkpoint
    `r` are asserted identical (V4, fourth assertion).

    `sigma_hat` is the pricer's own `sigma_live` at the checkpoint, asserted equal here.
    """
    s1 = pfair.reports(t0, config.S1_STREAM)
    s3 = pfair.merged_stream(t0, config.S3_STREAM)
    keys = [ts for ts, _value in s3]
    grid = tz10b.grid_of(s3, t0)
    pre = tz07a.excluded_prefix(tz07a.excluded_seconds(t0, manifests))
    priced = {row["tau"]: row for row in pfair.observations(t0, s1, s3)}
    reference = tz07b.member_r(t0, manifests) if guard else None
    out = {}
    for tau in pfair.TAUS:
        sigma_hat = tz10b.sigma_hat_of(grid, tau)
        assert sigma_hat == priced[tau]["sigma_live"], \
            "interval %d tau %d: sigma_hat is not the pricer's sigma_live" % (t0, tau)
        horizon = tz07b.horizon_sd(tau, sigma_hat)
        assert horizon > 0, "interval %d at tau %d has no scale to divide by" % (t0, tau)
        values, squares, dropped, at_checkpoint = array.array("d"), D(0), 0, None
        for a in range(GRID_LO, GRID_HI - tau + 1):
            i = a - GRID_LO
            if pre[i + tau + 1] - pre[i] > 0:
                dropped += 1
                continue
            y = tz07b.residual(s3, keys, t0, grid, a, tau)
            assert y is not None, "interval %d at tau %d anchor %d has no mean" % (t0, tau, a)
            r = y / horizon
            values.append(float(r))
            squares += r * r
            if a == GRID_HI - tau:
                at_checkpoint = (y, r)
        assert values, "interval %d at tau %d kept no anchor" % (t0, tau)
        if reference is not None:
            ref = reference[tau]
            assert (ref["values"] == values and ref["sum_squares"] == squares
                    and ref["dropped"] == dropped
                    and ref["checkpoint"] == (at_checkpoint or (None, None))[1]), \
                "V4: interval %d tau %d: r is not tz07b.member_r's" % (t0, tau)
        out[tau] = {"values": values, "squares": squares, "dropped": dropped,
                    "sigma_hat": sigma_hat, "priced": priced[tau],
                    "Y": None if at_checkpoint is None else at_checkpoint[0],
                    "r": None if at_checkpoint is None else at_checkpoint[1]}
    return out


def guard_members(fit, test1, manifests):
    """V4's fourth assertion: the 50, over the fit set and test 1 only (System Map item 48).

    The first 20 fit members, plus every member of the fit set and of test 1 whose grid M6
    drops a second of. If the union is not 50 the run stops, stating the three components.
    """
    first = fit[:V2_MEMBERS]
    fit_m6 = [t0 for t0 in fit if tz07a.excluded_seconds(t0, manifests)]
    test1_m6 = [t0 for t0 in test1 if tz07a.excluded_seconds(t0, manifests)]
    guard = sorted(set(first) | set(fit_m6) | set(test1_m6))
    doc = {"first_fit_members": len(first), "fit_members_M6_drops_a_second_of": len(fit_m6),
           "test1_members_M6_drops_a_second_of": len(test1_m6),
           "overlap_with_the_first_20": sorted(set(first) & (set(fit_m6) | set(test1_m6))),
           "members": guard, "count": len(guard), "required": V4_GUARD}
    if len(guard) != V4_GUARD:
        raise SystemExit("BLOCKED at V4: the guard holds %d members, not %d - %d first fit "
                         "members, %d fit members and %d test-1 members M6 drops a second of"
                         % (len(guard), V4_GUARD, len(first), len(fit_m6), len(test1_m6)))
    return guard, doc


# ---- M2: the domain ----------------------------------------------------------------

def measure_admit(walked, fit):
    """Section 3.2: the 30th percentile of `sigma_hat` over the 400 fit members, per tau."""
    out = {}
    for tau in pfair.TAUS:
        values = [walked[t0][tau]["sigma_hat"] for t0 in fit]
        cut = statistics.quantiles(values, n=ADMIT_QUANTILES, method="inclusive")[ADMIT_INDEX]
        out[tau] = {"members": len(values), "measured": cut,
                    "six_significant": tz07a.six_significant(cut)}
    return out


def admissible_members(walked, members, admit):
    """Per tau, the members whose `sigma_hat` is at or above `admit[tau]`, in `T0` order."""
    return {tau: [t0 for t0 in members if walked[t0][tau]["sigma_hat"] >= admit[tau]]
            for tau in pfair.TAUS}


def check_literals(name, literal, measured):
    """V8: one table's committed literals equal this run's measurement to six significant digits."""
    rows = []
    assert sorted(literal) == sorted(pfair.TAUS), \
        "V8: pfair.%s carries %s; the pricer serves %s" % (name, sorted(literal),
                                                           sorted(pfair.TAUS))
    for tau in pfair.TAUS:
        want = tz07a.six_significant(D(measured[tau]))
        assert literal[tau] == want, "V8: pfair.%s[%d] is %s; this run measures %s" % (
            name, tau, literal[tau], want)
        rows.append({"table": name, "tau": tau, "measured": measured[tau],
                     "measured_6sd": want, "in_pfair": literal[tau], "equal": True})
    return rows


# ---- M1 and M3: the Student fit ----------------------------------------------------

def population(walked, members, tau):
    """One population's `r` at one tau: ascending `T0`, then ascending anchor, one array.

    Returns the float64 array the search reads, the offset of each member's first anchor in it,
    the same values as an `array`, and their Decimal sum of squares for `kappa`.
    """
    flat, offsets, squares = array.array("d"), [], D(0)
    for t0 in members:
        row = walked[t0][tau]
        offsets.append(len(flat))
        flat.extend(row["values"])
        squares += row["squares"]
    return numpy.array(flat, dtype=numpy.float64), offsets, flat, squares


def log_density(r, nu, s):
    """Section 3.1's `log f(r)` of a symmetric Student's `t` at every anchor, one vectorised pass."""
    const = (math.lgamma((nu + 1.0) / 2.0) - math.lgamma(nu / 2.0)
             - 0.5 * math.log(nu * math.pi) - math.log(s))
    return const - ((nu + 1.0) / 2.0) * numpy.log1p((r / s) ** 2 / nu)


def golden(f, lo, hi):
    """Golden-section maximisation of `f` over `[lo, hi]` to `SEARCH_REL_TOL` relative width.

    The bracket shrinks until its width is at most `SEARCH_REL_TOL` times its midpoint. An end
    of the bracket that never moved off its bound is reported: the maximiser is then the edge of
    the search, not an interior point.
    """
    a, b = lo, hi
    c, d = b - GOLDEN * (b - a), a + GOLDEN * (b - a)
    fc, fd = f(c), f(d)
    steps = 0
    while b - a > SEARCH_REL_TOL * (a + b) / 2.0:
        if fc >= fd:
            b, d, fd = d, c, fc
            c = b - GOLDEN * (b - a)
            fc = f(c)
        else:
            a, c, fc = c, d, fd
            d = a + GOLDEN * (b - a)
            fd = f(d)
        steps += 1
    return {"x": (a + b) / 2.0, "at_lower": a == lo, "at_upper": b == hi, "steps": steps}


def fit_student(r):
    """Section 3.1: `nu` by golden section over `[2.05, 60]`, `s` profiled out at each `nu`."""
    count = [0]

    def ll(nu, s):
        count[0] += 1
        return float(numpy.sum(log_density(r, nu, s)))

    def profile(nu):
        best = golden(lambda s: ll(nu, s), S_LO, S_HI)
        return best, ll(nu, best["x"])

    outer = golden(lambda nu: profile(nu)[1], NU_LO, NU_HI)
    inner, value = profile(outer["x"])
    square_mean = float(numpy.sum(r * r)) / r.size
    return {"n": int(r.size), "nu": outer["x"], "s": inner["x"], "ll": value,
            "nu_at_lower_bound": outer["at_lower"], "nu_at_upper_bound": outer["at_upper"],
            "s_at_lower_bound": inner["at_lower"], "s_at_upper_bound": inner["at_upper"],
            "outer_steps": outer["steps"], "inner_steps_at_optimum": inner["steps"],
            "evaluations": count[0],
            "normal_scale": math.sqrt(square_mean),
            "ll_normal": -0.5 * r.size * (math.log(2.0 * math.pi * square_mean) + 1.0)}


def influence_refit(r, offsets, members, fit):
    """V12 item 2: a member's influence is its own contribution to the log-likelihood at
    `(nu_hat, s_hat)`, summed over its anchors; one exact refit drops the single largest in
    magnitude (on a tie, the first in `T0` order)."""
    sums = numpy.add.reduceat(log_density(r, fit["nu"], fit["s"]), numpy.array(offsets))
    k = int(numpy.argmax(numpy.abs(sums)))
    end = offsets[k + 1] if k + 1 < len(offsets) else int(r.size)
    refit = fit_student(numpy.concatenate((r[:offsets[k]], r[end:])))
    return {"T0": members[k], "anchors": end - offsets[k], "contribution": float(sums[k]),
            "members": len(members), "refit": refit,
            "nu_without": refit["nu"], "s_without": refit["s"],
            "nu_shift": refit["nu"] - fit["nu"], "s_shift": refit["s"] - fit["s"]}


def fits(walked, sets, admit, timing):
    """M1, M2's refit and M3: the six populations at seven taus, the V8 freeze check, and the
    21 influence refits. The fit-set admissible population goes first, so the first fit timed
    is the one the pricer's tables come from."""
    members = {"all": {name: {tau: sets[name][1] for tau in pfair.TAUS} for name in SETS},
               "admissible": {name: admissible_members(walked, sets[name][1], admit)
                              for name in SETS}}
    order = [("fit", "admissible")] + [p for p in POPULATIONS if p != ("fit", "admissible")]
    out = {name: {} for name in SETS}
    arrays = {}
    for name, kind in order:
        out[name][kind] = {}
        for tau in pfair.TAUS:
            held = members[kind][name][tau]
            r, offsets, flat, squares = population(walked, held, tau)
            started = time.monotonic()
            fit = fit_student(r)
            seconds = time.monotonic() - started
            timing["fits"].append({"population": "%s-%s" % (name, kind), "tau": tau,
                                   "anchors": fit["n"], "evaluations": fit["evaluations"],
                                   "seconds": seconds})
            if len(timing["fits"]) == 1:
                timing["first_fit_seconds"] = seconds
                timing["projection_seconds_for_63_fits"] = seconds * FITS_REQUIRED
                if seconds > FIRST_FIT_LIMIT_S:
                    raise SystemExit("BLOCKED at section 3.1: the first fit took %.1f s, above "
                                     "%.0f s; %d fits project to %.0f s" % (
                                         seconds, FIRST_FIT_LIMIT_S, FITS_REQUIRED,
                                         seconds * FITS_REQUIRED))
            fit["members"] = len(held)
            fit["kappa"] = tz10b.shape(flat, squares)
            fit["log_nu_over_LINK_NU"] = math.log(fit["nu"] / float(pfair.LINK_NU[tau]))
            out[name][kind][tau] = fit
            arrays[(name, kind, tau)] = (r, offsets, held)
        if (name, kind) == ("fit", "admissible"):
            timing["literals_checked_after_fit"] = len(timing["fits"])
            literals = (check_literals("LINK_NU", pfair.LINK_NU,
                                       {tau: out["fit"]["admissible"][tau]["nu"]
                                        for tau in pfair.TAUS})
                        + check_literals("LINK_SCALE", pfair.LINK_SCALE,
                                         {tau: out["fit"]["admissible"][tau]["s"]
                                          for tau in pfair.TAUS}))
    for name in SETS:
        for tau in pfair.TAUS:
            r, offsets, held = arrays[(name, "admissible", tau)]
            started = time.monotonic()
            out[name]["admissible"][tau]["influence"] = influence_refit(
                r, offsets, held, out[name]["admissible"][tau])
            timing["fits"].append({"population": "%s-admissible, influence refit" % name,
                                   "tau": tau, "anchors": int(r.size) - out[name]["admissible"][
                                       tau]["influence"]["anchors"],
                                   "evaluations": out[name]["admissible"][tau]["influence"][
                                       "refit"]["evaluations"],
                                   "seconds": time.monotonic() - started})
    assert len(timing["fits"]) == FITS_REQUIRED == PRIMARY_FITS + INFLUENCE_FITS, \
        "section 3.1: %d fits, not %d" % (len(timing["fits"]), FITS_REQUIRED)
    counts = {name: {kind: {tau: len(members[kind][name][tau]) for tau in pfair.TAUS}
                     for kind in ("all", "admissible")} for name in SETS}
    return out, literals, counts, members["admissible"]


# ---- M4 and V12 item 1: scoring, and lambda-hat with its influence -------------------

def student_log_cdf(nu):
    """`u -> log F_nu(u)` at one frozen `nu`: the `log_cdf` section 5.3 hands `lambda_hat`."""
    def log_cdf(u):
        return pfair.log_t_cdf(u, nu)
    return log_cdf


def lambda_with_influence(pairs, held, log_cdf):
    """`tz07a.lambda_hat` under the Student likelihood, and V12 item 1: its value refitted
    without the single most influential observation - the one whose own contribution to
    `ll(lambda_hat) - ll(1)` is largest in magnitude, first in `T0` order on a tie."""
    fit = tz07a.lambda_hat(pairs, log_cdf)
    lam = fit["lambda_hat"]
    contributions = [tz07a.log_likelihood([pair], lam, log_cdf)
                     - tz07a.log_likelihood([pair], 1.0, log_cdf) for pair in pairs]
    k = min(range(len(pairs)), key=lambda i: (-abs(contributions[i]), i))
    signed = min(range(len(pairs)), key=lambda i: (-contributions[i], i))
    without = tz07a.lambda_hat(pairs[:k] + pairs[k + 1:], log_cdf)
    return dict(fit, most_influential={
        "T0": held[k], "label": pairs[k][1], "z": pairs[k][0],
        "contribution_to_ll_hat_minus_ll_one": contributions[k],
        "lambda_hat_without": without["lambda_hat"],
        "shift": without["lambda_hat"] - lam,
        "is_also_the_largest_signed_contribution": k == signed,
        "largest_signed_contribution_T0": held[signed]})


def score_rows(rows, tau):
    """Section 3.4 items 1 to 4 on one list of checkpoint rows at one tau."""
    table = tz06.table_for(tau, rows, "p_t", G1_BRIER)
    nu = float(pfair.LINK_NU[tau])
    pairs = [(r["z_student"], r["label"]) for r in rows]
    lam = lambda_with_influence(pairs, [r["T0"] for r in rows], student_log_cdf(nu))
    scale = pfair.LINK_SCALE[tau]
    held = [r for r in rows if r["r"] is not None]
    u = array.array("d", (float(r["r"] / scale) for r in held))
    squares = sum(((r["r"] / scale) ** 2 for r in held), D(0))
    return {"n": len(rows), "brier_p_t": table["brier"],
            "brier_p_fair_corrected": tz06.brier([(r["p_fair_corrected"], r["label"])
                                                  for r in rows]),
            "table": table, "lambda_hat": lam,
            "kappa_of_r_over_LINK_SCALE": tz10b.shape(u, squares),
            "rows_without_a_checkpoint_r": len(rows) - len(held),
            "saturated_p_t": sum(1 for r in rows if r["p_t"] in (0.0, 1.0)),
            "saturated_p_fair_corrected": sum(1 for r in rows
                                              if r["p_fair_corrected"] in (0.0, 1.0))}


def m4(checkpoints, sets):
    """Section 3.4 on both test sets, admissible checkpoints and all checkpoints, per tau."""
    out = {}
    for name in TEST_SETS:
        out[name] = {}
        for kind in ("admissible", "all"):
            out[name][kind] = {}
            for tau in pfair.TAUS:
                rows = [checkpoints[t0][tau] for t0 in sets[name][1]
                        if kind == "all" or checkpoints[t0][tau]["admissible"]]
                out[name][kind][tau] = score_rows(rows, tau)
    return out


def gates(m4_doc, fit_doc):
    """Section 4's four gates, each row an arithmetic comparison against the quoted threshold.

    G2 pools the six `pfair.GATED_TAUS` exactly as `tz06.build` does; `tau = 10`'s failing bins
    are printed beside it and not pooled.
    """
    out = {}
    for name in TEST_SETS:
        adm = m4_doc[name]["admissible"]
        g1 = {tau: {"brier": adm[tau]["brier_p_t"], "threshold": G1_BRIER,
                    "passes": adm[tau]["brier_p_t"] < G1_BRIER} for tau in pfair.TAUS}
        failing = {tau: adm[tau]["table"]["failing_bins"] for tau in pfair.GATED_TAUS}
        g3 = {tau: {"lambda_hat": adm[tau]["lambda_hat"]["lambda_hat"],
                    "distance": abs(adm[tau]["lambda_hat"]["lambda_hat"] - 1.0),
                    "passes": abs(adm[tau]["lambda_hat"]["lambda_hat"] - 1.0) <= G3_BAND}
              for tau in pfair.TAUS}
        g4 = {tau: {"nu_set": fit_doc[name]["admissible"][tau]["nu"],
                    "LINK_NU": pfair.LINK_NU[tau],
                    "abs_log_ratio": abs(fit_doc[name]["admissible"][tau]["log_nu_over_LINK_NU"]),
                    "passes": abs(fit_doc[name]["admissible"][tau]["log_nu_over_LINK_NU"])
                    <= G4_BAND} for tau in pfair.TAUS}
        out[name] = {
            "G1": {"per_tau": g1, "passing": sum(v["passes"] for v in g1.values()),
                   "taus": len(g1), "passes": all(v["passes"] for v in g1.values())},
            "G2": {"failing_bins": failing, "total_failing": sum(failing.values()),
                   "eligible_bins": {tau: adm[tau]["table"]["eligible_bins"]
                                     for tau in pfair.GATED_TAUS},
                   "allowed": tz06.MAX_FAILING_BINS,
                   "tau_10_failing_not_pooled": adm[10]["table"]["failing_bins"],
                   "tau_10_eligible_not_pooled": adm[10]["table"]["eligible_bins"],
                   "passes": sum(failing.values()) <= tz06.MAX_FAILING_BINS},
            "G3": {"per_tau": g3, "band": G3_BAND,
                   "passing": sum(v["passes"] for v in g3.values()), "taus": len(g3),
                   "passes": all(v["passes"] for v in g3.values())},
            "G4": {"per_tau": g4, "band": G4_BAND,
                   "passing": sum(v["passes"] for v in g4.values()), "taus": len(g4),
                   "passes": all(v["passes"] for v in g4.values())}}
    return out


# ---- the checkpoint rows -------------------------------------------------------------

def checkpoint_row(t0, name, tau, row):
    """One member at `T0 + 300 - tau`: both links on the identical `state` and `sigma_hat`."""
    priced = row["priced"]
    sd_c, p_c = tz07a.corrected(priced)
    sd_t = pfair.student_sd(tau, row["sigma_hat"])
    z_c = float(priced["state"] / sd_c)
    z_t = float(priced["state"] / sd_t)
    return {"T0": t0, "set": name, "tau": tau, "K": priced["K"], "S_t": priced["S_t"],
            "m_r": priced["m_r"], "state": priced["state"], "sigma_hat": row["sigma_hat"],
            "ADMIT": pfair.ADMIT[tau], "admissible": row["sigma_hat"] >= pfair.ADMIT[tau],
            "sd_corrected": sd_c, "sd_student": sd_t, "z_corrected": z_c, "z_student": z_t,
            "p_fair_corrected": p_c, "p_t": pfair.p_fair_student(priced["state"], sd_t, tau),
            "log_phi_z_corrected": pfair.log_phi(z_c),
            "log_t_cdf_z_student": pfair.log_t_cdf(z_t, float(pfair.LINK_NU[tau])),
            "Y": row["Y"], "r": row["r"], "label": None}


# ---- M5: the observation the old gate hung on ------------------------------------------

def m5(checkpoints, m4_doc):
    cp = checkpoints[M5_T0][M5_TAU]
    assert cp["set"] == "test1", "M5: T0 %d is not in test 1" % M5_T0
    log_cdf = student_log_cdf(float(pfair.LINK_NU[M5_TAU]))
    pair = [(cp["z_student"], cp["label"])]
    doc = {"T0": M5_T0, "tau": M5_TAU, "state": cp["state"], "sigma_hat": cp["sigma_hat"],
           "ADMIT": cp["ADMIT"], "admissible": cp["admissible"],
           "sd_corrected": cp["sd_corrected"], "sd_student": cp["sd_student"],
           "z_corrected": cp["z_corrected"], "z_student": cp["z_student"],
           "p_fair": cp["p_fair_corrected"], "p_t": cp["p_t"],
           "log_phi_z_corrected": cp["log_phi_z_corrected"],
           "log_t_cdf_z_student": cp["log_t_cdf_z_student"],
           "LINK_NU": pfair.LINK_NU[M5_TAU], "resolved_up": cp["label"]}
    for kind in ("admissible", "all"):
        if kind == "admissible" and not cp["admissible"]:
            doc["under_the_%s_member_lambda_hat" % kind] = "not a member"
            continue
        lam = m4_doc["test1"][kind][M5_TAU]["lambda_hat"]["lambda_hat"]
        doc["under_the_%s_member_lambda_hat" % kind] = {"lambda_hat": lam,
                     "contribution_to_ll_at_lambda_hat": tz07a.log_likelihood(pair, lam, log_cdf),
                     "contribution_to_ll_at_one": tz07a.log_likelihood(pair, 1.0, log_cdf)}
    return doc


# ---- V2: causality of the causal inputs to p_t -----------------------------------------

def v2(fit):
    """`sigma_hat` and `student_sd(tau, sigma_hat)`, and nothing else: bit-identical when every
    `chainlink` report stamped strictly after `T0 + (300 - tau)` is perturbed by the committed
    `tz06.perturb_after`; moved by `tz06.perturb_one` on `tz06.last_readable`. `Y`, `r`, `nu_hat`,
    `s_hat` and every outcome are functions of the future by construction and are exempt."""
    sample = fit[:V2_MEMBERS]
    n = same_sigma = same_sd = moved_sigma = moved_sd = at_instant = 0
    fewest = None
    for t0 in sample:
        s3 = pfair.merged_stream(t0, config.S3_STREAM)
        base_grid = tz10b.grid_of(s3, t0)
        for tau in pfair.TAUS:
            n += 1
            at = (t0 + config.INTERVAL_S - tau) * MS
            future = tz06.perturb_after(s3, at)
            subject = tz06.last_readable(s3, at)
            perturbed = {i for i in range(len(s3)) if future[i] != s3[i]}
            assert subject is not None and subject not in perturbed and perturbed, \
                "V2: T0 %d tau %d: the perturbation and the control overlap or are empty" % (
                    t0, tau)
            fewest = len(perturbed) if fewest is None else min(fewest, len(perturbed))
            at_instant += s3[subject][0] == at
            base = tz10b.sigma_hat_of(base_grid, tau)
            after = tz10b.sigma_hat_of(tz10b.grid_of(future, t0), tau)
            control = tz10b.sigma_hat_of(
                tz10b.grid_of(tz06.perturb_one(s3, subject), t0), tau)
            same_sigma += after == base
            same_sd += pfair.student_sd(tau, after) == pfair.student_sd(tau, base)
            moved_sigma += control != base
            moved_sd += pfair.student_sd(tau, control) != pfair.student_sd(tau, base)
    doc = {"sample": sample, "members": len(sample), "taus": list(pfair.TAUS),
           "checkpoints": n, "factor": str(tz06.PERTURBATION),
           "perturbation": "tz06-calibration.perturb_after on the merged chainlink stream: "
                           "every report with ts > T0 + (300 - tau), in ms",
           "negative_control": "tz06-calibration.perturb_one on the report "
                               "tz06-calibration.last_readable returns, ts <= that instant",
           "sigma_hat_bit_identical": same_sigma, "student_sd_bit_identical": same_sd,
           "control_moved_sigma_hat": moved_sigma, "control_moved_student_sd": moved_sd,
           "control_subject_stamped_at_the_checkpoint_instant": at_instant,
           "fewest_reports_perturbed_in_one_checkpoint": fewest}
    assert (same_sigma, same_sd) == (n, n), \
        "V2: sigma_hat bit-identical %d of %d, student_sd %d of %d" % (same_sigma, n, same_sd, n)
    assert (moved_sigma, moved_sd) == (n, n), \
        "V2: the control moved sigma_hat %d of %d, student_sd %d of %d" % (
            moved_sigma, n, moved_sd, n)
    return doc


# ---- V4: the instrument reproduces what is committed ------------------------------------

def rms(walked, members, tau):
    n = sum(len(walked[t0][tau]["values"]) for t0 in members)
    return (sum((walked[t0][tau]["squares"] for t0 in members), D(0)) / D(n)).sqrt(), n


def v4(walked, fit, test1, checkpoints, labels, guard_doc):
    """Four assertions, each a count. The third reads the TZ-08a 400's labels - the third place
    section 2 names - to reproduce a committed figure and for nothing else."""
    one, two = {}, {}
    for tau in pfair.TAUS:
        lam, n = rms(walked, fit, tau)
        one[tau] = {"anchors": n, "rms_r": lam, "printed": "%.6f" % lam,
                    "published": TZ07B_LAMBDA[tau]}
        assert one[tau]["printed"] == TZ07B_LAMBDA[tau], \
            "V4: fit tau %d: RMS(r) %s, TZ-07b printed %s" % (tau, lam, TZ07B_LAMBDA[tau])
        lam, n = rms(walked, test1, tau)
        ratio = lam / pfair.SD_SCALE[tau]
        two[tau] = {"anchors": n, "rms_r": lam, "printed": "%.6f" % lam,
                    "published": TZ08A_LAMBDA_OOS[tau], "rms_u": ratio,
                    "rms_u_printed": "%.6f" % ratio, "rms_u_published": TZ08A_RMS_U[tau]}
        assert two[tau]["printed"] == TZ08A_LAMBDA_OOS[tau] \
            and two[tau]["rms_u_printed"] == TZ08A_RMS_U[tau], \
            "V4: test 1 tau %d: RMS(r) %s, RMS(u) %s" % (tau, lam, ratio)
    pairs = [(checkpoints[t0][V4_LAMBDA_TAU]["z_corrected"], labels[t0]) for t0 in test1]
    committed = tz07a.lambda_hat(pairs)
    assert "%.10f" % committed["lambda_hat"] == V4_LAMBDA, \
        "V4: tz07a.lambda_hat at its default returns %r at tau 30" % committed["lambda_hat"]
    return {"lambda_fit_set": one, "lambda_fit_set_reproduced": len(one),
            "rms_test1": two, "rms_test1_reproduced": len(two),
            "lambda_hat_default": {"tau": V4_LAMBDA_TAU, "n": len(pairs),
                                   "lambda_hat": committed["lambda_hat"],
                                   "printed": "%.10f" % committed["lambda_hat"],
                                   "expected": V4_LAMBDA, "ll_at_one": committed["ll_at_one"]},
            "member_r_guard": guard_doc}


# ---- V6: the diff, in its real shape ---------------------------------------------------

def attribute_assignments():
    """Every assignment to, or deletion of, an attribute in this file, and every `setattr` or
    `delattr` call: the instrument must rebind no name of an imported module."""
    with open(os.path.abspath(__file__), encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    found, stores = [], 0
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and isinstance(node.ctx, (ast.Store, ast.Del)):
            found.append(node.lineno)
        elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            stores += 1
        elif (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
              and node.func.id in ("setattr", "delattr")):
            found.append(node.lineno)
    return found, stores


def v6():
    base = tz10b.git("merge-base", "HEAD", "main").strip()
    head = tz10b.git("rev-parse", "HEAD").strip()
    status = tz10b.git("status", "--porcelain", "--", *FIVE_PATHS)
    assert not status.strip(), "V6: the run is not of committed files: %s" % status
    files = {}
    for name in ("pfair.py", "selftest-pfair.py", TZ07A_FILE):
        body = [line for line in tz10b.git("diff", "--unified=0", base, "HEAD", "--",
                                           name).splitlines()
                if not line.startswith(("---", "+++"))]
        removed = [line[1:] for line in body if line.startswith("-")]
        added = [line[1:] for line in body if line.startswith("+")]
        before = tz10b.top_level(tz10b.git("show", "%s:research/%s" % (base, name)))
        with open(os.path.join(HERE, name), encoding="utf-8") as fh:
            after = tz10b.top_level(fh.read())
        exempt = TZ07A_EXEMPT if name == TZ07A_FILE else ()
        changed = sorted(n for n in before if n not in exempt and after.get(n) != before[n])
        assert not changed, "V6: %s changes %s" % (name, changed)
        if name == TZ07A_FILE:
            assert sorted(removed) == sorted(TZ07A_REPLACED), \
                "V6: %s removes %s" % (name, removed)
            assert all(after.get(n) != before[n] for n in exempt), \
                "V6: %s leaves an exempt function unchanged" % name
        else:
            assert added and not removed, "V6: %s removes %d lines" % (name, len(removed))
        files[name] = {"lines_added": len(added), "lines_removed": len(removed),
                       "removed_lines": removed, "objects_before": len(before),
                       "objects_byte_identical": len(before) - len(exempt),
                       "objects_exempt": list(exempt),
                       "objects_added": sorted(set(after) - set(before))}
    pfair_before = tz10b.top_level(tz10b.git("show", "%s:research/pfair.py" % base))
    with open(os.path.join(HERE, "pfair.py"), encoding="utf-8") as fh:
        pfair_after = tz10b.top_level(fh.read())
    named = [n for n in PFAIR_NAMED if pfair_before.get(n) is not None
             and pfair_after.get(n) == pfair_before[n]]
    assert named == list(PFAIR_NAMED), "V6: named objects not byte-identical: %s" % (
        sorted(set(PFAIR_NAMED) - set(named)))
    assert files["pfair.py"]["objects_added"] == sorted(PFAIR_ADDED), \
        "V6: pfair.py gains %s" % files["pfair.py"]["objects_added"]
    assert not files[TZ07A_FILE]["objects_added"], "V6: tz07a gains a top-level object"
    found, stores = attribute_assignments()
    assert not found, "V6: the instrument assigns an attribute at lines %s" % found
    return {"merge_base": base, "head": head, "files": files, "named": list(PFAIR_NAMED),
            "named_byte_identical": len(named), "pfair_added": sorted(PFAIR_ADDED),
            "tz07a_replaced": list(TZ07A_REPLACED),
            "attribute_assignments_in_the_instrument": found,
            "name_bindings_scanned": stores,
            "pfair_diff": tz10b.git("diff", base, "HEAD", "--", "pfair.py"),
            "tz07a_diff": tz10b.git("diff", base, "HEAD", "--", TZ07A_FILE)}


# ---- V7: the self-tests ---------------------------------------------------------------

def v7():
    """`selftest-pfair.py`, run and counted - never transcribed. Each item aborts that run."""
    out = subprocess.run([sys.executable, "-B", "selftest-pfair.py"], cwd=HERE,
                         capture_output=True, text=True)
    assert out.returncode == 0, "V7: selftest-pfair.py exited %d: %s" % (
        out.returncode, out.stderr.strip().splitlines()[-1:])
    counts, lines, inside = {}, [], False
    for line in out.stdout.splitlines():
        if line.endswith("checks passed") and ":" in line:
            label, rest = line.split(":", 1)
            counts[label.strip()] = int(rest.split()[0])
        if line.startswith("tz11a_"):
            inside = True
        elif line.startswith("machinery_"):
            inside = False
        if inside:
            lines.append(line)
    assert counts == SELFTEST_COUNTS, "V7: the self-tests count %s" % counts
    return {"command": "python -B selftest-pfair.py", "exit_status": out.returncode,
            "counts": counts, "total": sum(counts.values()), "tz11a_output": lines}


# ---- --emit: the three tables, measured, for pfair.py ---------------------------------------

def emit():
    """The literals exactly as they are written into `pfair.py`: the fit set alone, no label."""
    manifests = load_manifests()
    _rows, fit = fit_set(manifests)
    walked = {t0: walk_member(t0, manifests, False) for t0 in fit}
    measured = measure_admit(walked, fit)
    admit = {tau: measured[tau]["six_significant"] for tau in pfair.TAUS}
    held = admissible_members(walked, fit, admit)
    nu, scale = {}, {}
    for tau in pfair.TAUS:
        started = time.monotonic()
        fit_doc = fit_student(population(walked, held[tau], tau)[0])
        nu[tau] = tz07a.six_significant(D(fit_doc["nu"]))
        scale[tau] = tz07a.six_significant(D(fit_doc["s"]))
        sys.stderr.write("tau %d: %d members, %d anchors, nu %r s %r, bounds %s, %d evaluations, "
                         "%.1f s\n" % (tau, len(held[tau]), fit_doc["n"], fit_doc["nu"],
                                       fit_doc["s"],
                                       [fit_doc[k] for k in ("nu_at_lower_bound",
                                                             "nu_at_upper_bound",
                                                             "s_at_lower_bound",
                                                             "s_at_upper_bound")],
                                       fit_doc["evaluations"], time.monotonic() - started))
    for name, table in (("ADMIT", admit), ("LINK_NU", nu), ("LINK_SCALE", scale)):
        sys.stdout.write("%s = {%s}\n" % (name, ", ".join(
            '%d: D("%s")' % (tau, table[tau]) for tau in pfair.TAUS)))


# ---- the document ------------------------------------------------------------------

def build():
    started = time.monotonic()
    timing = {"fits": []}
    manifests = load_manifests()
    sets, set_doc = the_sets(manifests)
    fit, test1, test2 = (sets[name][1] for name in SETS)
    members = fit + test1 + test2
    reads = sorted({r["T0"] for name in SETS for r in sets[name][0]}
                   | {t0 - config.INTERVAL_S for t0 in members})
    host = [host_read("run start", reads, FLOOR_START_BYTES)]

    # Everything that stops the run on a defect of the instrument comes before any measurement.
    additive = v6()
    selftests = v7()
    causality = v2(fit)
    guard, guard_doc = guard_members(fit, test1, manifests)

    walked = {}
    for t0 in members:
        walked[t0] = walk_member(t0, manifests, t0 in guard)
    timing["walk_seconds"] = time.monotonic() - started
    host.append(host_read("after the walk", reads, FLOOR_BYTES))

    # M2 and V8: the domain is measured on the fit set alone and asserted against the literal
    # before anything is scored; from here on the committed literal is the threshold.
    measured = measure_admit(walked, fit)
    literals = check_literals("ADMIT", pfair.ADMIT,
                              {tau: measured[tau]["measured"] for tau in pfair.TAUS})
    fitted, link_literals, counts, admissible = fits(walked, sets, pfair.ADMIT, timing)
    literals += link_literals
    assert len(literals) == 21, "V8: %d literals checked, not 21" % len(literals)
    timing["fit_seconds_total"] = sum(f["seconds"] for f in timing["fits"])

    # M4 and M5 read the labels of the two test sets, and nothing else here reads one.
    labels = tz10b.m2_labels(test1 + test2)
    checkpoints = {}
    set_of = {t0: name for name in SETS for t0 in sets[name][1]}
    for t0 in members:
        checkpoints[t0] = {tau: checkpoint_row(t0, set_of[t0], tau, walked[t0][tau])
                           for tau in pfair.TAUS}
        if t0 in labels:
            for tau in pfair.TAUS:
                checkpoints[t0][tau]["label"] = labels[t0]
    for name in SETS:
        for tau in pfair.TAUS:
            assert [t0 for t0 in sets[name][1] if checkpoints[t0][tau]["admissible"]] \
                == admissible[name][tau], "the admissible rows are not the fitted population"
    reproduction = v4(walked, fit, test1, checkpoints, labels, guard_doc)
    scoring_started = time.monotonic()
    m4_doc = m4(checkpoints, sets)
    timing["m4_seconds"] = time.monotonic() - scoring_started
    gate_doc = gates(m4_doc, fitted)
    m5_doc = m5(checkpoints, m4_doc)
    csv = csv_text(members, checkpoints)

    host.append(host_read("run end", reads, FLOOR_BYTES))
    start, end = host[0], host[-1]
    assert end["recorder_pids"] == start["recorder_pids"], "V9: the recorder pid changed"
    assert end["newest_start_sha"] == start["newest_start_sha"] \
        and end["newest_start_recv_ns"] == start["newest_start_recv_ns"], \
        "V9: the recorder restarted during the run"
    assert end["interval_directories"] >= start["interval_directories"], \
        "V9: the interval count fell"
    assert end["read_set_sha256"] == start["read_set_sha256"], \
        "V9: a file this run reads changed during the run"
    timing["total_seconds"] = time.monotonic() - started

    doc = {
        "tz": "TZ-11a",
        "sets": set_doc,
        "disclosure": {name: sets[name][0] for name in SETS},
        "M2_admit": {tau: dict(measured[tau], literal=pfair.ADMIT[tau]) for tau in pfair.TAUS},
        "admissible_counts": counts,
        "fits": fitted,
        "search": {"nu": [NU_LO, NU_HI], "s": [S_LO, S_HI], "relative_tolerance": SEARCH_REL_TOL,
                   "fits": FITS_REQUIRED},
        "LINK_NU": {tau: pfair.LINK_NU[tau] for tau in pfair.TAUS},
        "LINK_SCALE": {tau: pfair.LINK_SCALE[tau] for tau in pfair.TAUS},
        "ADMIT": {tau: pfair.ADMIT[tau] for tau in pfair.TAUS},
        "M4": m4_doc, "gates": gate_doc, "M5": m5_doc,
        "prediction": [list(row) for row in PREDICTION],
        "V2": causality, "V4": reproduction, "V6": additive, "V7": selftests,
        "V8": literals,
        "observations_file": {"lines": len(csv.splitlines()),
                              "bytes": len(csv.encode("utf-8")),
                              "sha256": hashlib.sha256(csv.encode("utf-8")).hexdigest()},
        "admissibility": {t0: {tau: [checkpoints[t0][tau]["sigma_hat"],
                                     checkpoints[t0][tau]["admissible"]]
                               for tau in pfair.TAUS} for t0 in members},
    }
    return doc, csv, {"reads": host, "read_set_directories": len(reads), "timing": timing}


def cell(value):
    if value is None:
        return ""
    if isinstance(value, bool):
        return "1" if value else "0"
    if isinstance(value, float):
        return repr(value)
    return str(value)


def csv_text(members, checkpoints):
    """One row per member per tau, in set then `T0` then tau order. Labels on the test sets only."""
    lines = [",".join(CSV_HEADER)]
    for t0 in members:
        for tau in pfair.TAUS:
            cp = checkpoints[t0][tau]
            lines.append(",".join(cell(cp[key]) for key in CSV_HEADER))
    return "\n".join(lines) + "\n"


# ---- output --------------------------------------------------------------------------

def f6(value):
    return "%.6f" % value


def bound_note(fit):
    marks = [label for key, label in (("nu_at_lower_bound", "nu at 2.05"),
                                      ("nu_at_upper_bound", "nu at 60"),
                                      ("s_at_lower_bound", "s at 0.10"),
                                      ("s_at_upper_bound", "s at 10"))
             if fit[key]]
    return ", ".join(marks) or "interior"


def fit_table(doc, name, kind):
    out = ["", "#### %s, %s members" % (SET_NAMES[name], kind), "",
           "| tau | members | anchors | `ν̂` | `ŝ` | search edge | `ll` at optimum | `ll`, "
           "best normal | normal scale | **`κ`** | `log(ν̂ / LINK_NU)` | evaluations |",
           "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for tau in pfair.TAUS:
        f = doc["fits"][name][kind][tau]
        out.append("| %d | %d | %d | %.6f | %.6f | %s | %.3f | %.3f | %.6f | **%.4f** | %+.4f | "
                   "%d |" % (tau, f["members"], f["n"], f["nu"], f["s"], bound_note(f), f["ll"],
                             f["ll_normal"], f["normal_scale"], f["kappa"]["kappa"],
                             f["log_nu_over_LINK_NU"], f["evaluations"]))
    return out


def lambda_rows(block):
    out = ["| tau | n | `λ̂` | `ll(λ̂)` | `ll(1)` | LR | p | most influential (T0, label, z) | "
           "its contribution | `λ̂` without it | shift |",
           "|---|---|---|---|---|---|---|---|---|---|---|"]
    for tau in pfair.TAUS:
        lam = block[tau]["lambda_hat"]
        mi = lam["most_influential"]
        out.append("| %d | %d | %.6f | %.6f | %.6f | %.6f | %.6g | %d, %d, %.4f | %+.4f | %.6f | "
                   "%+.6f |" % (tau, lam["n"], lam["lambda_hat"], lam["ll_at_lambda_hat"],
                                lam["ll_at_one"], lam["likelihood_ratio"],
                                lam["chi_square_1df_p"], mi["T0"], mi["label"], mi["z"],
                                mi["contribution_to_ll_hat_minus_ll_one"],
                                mi["lambda_hat_without"], mi["shift"]))
    return out


def tables(doc):
    s = doc["sets"]
    out = ["## Sets", ""]
    for name in SETS:
        d = s[name]
        out.append("- %s: %d units considered (%d … %d), %d members (%d … %d), %d non-members "
                   "(%s); member list `%s`" % (
                       SET_NAMES[name], d["units_considered"], d["first_unit"], d["last_unit"],
                       d["members"], d["first_member"], d["last_member"], d["non_members"],
                       ", ".join("%s: %d" % kv for kv in d["non_member_reasons"].items())
                       or "none", d["member_list_sha256"]))

    out += ["", "## M2 — the domain", "",
            "| tau | `ADMIT` measured | six significant digits | `pfair.ADMIT` | admissible, fit "
            "| admissible, test 1 | admissible, test 2 |", "|---|---|---|---|---|---|---|"]
    for tau in pfair.TAUS:
        a = doc["M2_admit"][tau]
        c = doc["admissible_counts"]
        out.append("| %d | %.9f | %s | %s | %d of %d | %d of %d | %d of %d |" % (
            tau, a["measured"], a["six_significant"], a["literal"],
            c["fit"]["admissible"][tau], c["fit"]["all"][tau],
            c["test1"]["admissible"][tau], c["test1"]["all"][tau],
            c["test2"]["admissible"][tau], c["test2"]["all"][tau]))

    out += ["", "## M1 and M3 — the Student fit, per set before pooled"]
    for name, kind in POPULATIONS:
        out += fit_table(doc, name, kind)
    out += ["", "#### V12 item 2 — `ν̂` without its most influential member, admissible "
            "populations", "",
            "| population | tau | members | most influential T0 | its anchors | its contribution "
            "| `ν̂` | `ν̂` without | `ŝ` | `ŝ` without | search edge without |",
            "|---|---|---|---|---|---|---|---|---|---|---|"]
    for name in SETS:
        for tau in pfair.TAUS:
            f = doc["fits"][name]["admissible"][tau]
            i = f["influence"]
            out.append("| %s | %d | %d | %d | %d | %+.3f | %.6f | %.6f | %.6f | %.6f | %s |" % (
                name, tau, i["members"], i["T0"], i["anchors"], i["contribution"], f["nu"],
                i["nu_without"], f["s"], i["s_without"], bound_note(i["refit"])))

    out += ["", "## M4 — the scoring"]
    for name in TEST_SETS:
        for kind in ("admissible", "all"):
            block = doc["M4"][name][kind]
            title = "%s, %s checkpoints%s" % (SET_NAMES[name], kind,
                                             "" if kind == "admissible"
                                             else " — reported, not gated")
            out += ["", "### %s" % title, "",
                    "| tau | n | `Brier(p_t)` | `Brier(p_fair)`, `corrected_sd` | eligible bins | "
                    "failing bins | `κ` of `r / LINK_SCALE` | rows with no checkpoint `r` | "
                    "saturated `p_t` | saturated `p_fair` |",
                    "|---|---|---|---|---|---|---|---|---|---|"]
            for tau in pfair.TAUS:
                b = block[tau]
                out.append("| %d | %d | %.6f | %.6f | %d | %d | %.4f | %d | %d | %d |" % (
                    tau, b["n"], b["brier_p_t"], b["brier_p_fair_corrected"],
                    b["table"]["eligible_bins"], b["table"]["failing_bins"],
                    b["kappa_of_r_over_LINK_SCALE"]["kappa"], b["rows_without_a_checkpoint_r"],
                    b["saturated_p_t"], b["saturated_p_fair_corrected"]))
            out += ["", "`λ̂` under the Student likelihood at `LINK_NU[tau]`:", ""]
            out += lambda_rows(block)
            for tau in pfair.TAUS:
                t = block[tau]["table"]
                out += ["", "#### %s, %s, tau = %d — `p_t`%s" % (
                    SET_NAMES[name], kind, tau, " (printed, not pooled by G2)" if tau == 10
                    else ""), "",
                    "n = %d · observed Up rate %.4f · Brier %.6f" % (
                        t["n"], t["observed_up_rate"], t["brier"]), ""]
                out += tz06.BIN_HEAD + tz06.bin_rows(t)

    out += ["", "## Gates", ""]
    for name in TEST_SETS:
        g = doc["gates"][name]
        out += ["### %s" % SET_NAMES[name], "",
                "| tau | G1 `Brier(p_t)` | G1 | G3 `λ̂` | `\\|λ̂ − 1\\|` | G3 | G4 `ν̂_set` | "
                "`LINK_NU` | `\\|log(ν̂_set / LINK_NU)\\|` | G4 |",
                "|---|---|---|---|---|---|---|---|---|---|"]
        for tau in pfair.TAUS:
            g1, g3, g4 = g["G1"]["per_tau"][tau], g["G3"]["per_tau"][tau], g["G4"]["per_tau"][tau]
            out.append("| %d | %.6f | %s | %.6f | %.6f | %s | %.6f | %s | %.6f | %s |" % (
                tau, g1["brier"], "pass" if g1["passes"] else "FAIL", g3["lambda_hat"],
                g3["distance"], "pass" if g3["passes"] else "FAIL", g4["nu_set"], g4["LINK_NU"],
                g4["abs_log_ratio"], "pass" if g4["passes"] else "FAIL"))
        g2 = g["G2"]
        out += ["", "G2: failing bins over `pfair.GATED_TAUS` %s — total **%d** of %d eligible, "
                "allowance %d: **%s**. `tau = 10`, printed and not pooled: %d failing of %d "
                "eligible." % (", ".join("%d: %d" % kv for kv in g2["failing_bins"].items()),
                               g2["total_failing"], sum(g2["eligible_bins"].values()),
                               g2["allowed"], "pass" if g2["passes"] else "FAIL",
                               g2["tau_10_failing_not_pooled"],
                               g2["tau_10_eligible_not_pooled"]),
                "", "G1 %d of %d · G3 %d of %d · G4 %d of %d" % (
                    g["G1"]["passing"], g["G1"]["taus"], g["G3"]["passing"], g["G3"]["taus"],
                    g["G4"]["passing"], g["G4"]["taus"]), ""]

    m = doc["M5"]
    out += ["## M5 — T0 %d at tau = %d" % (m["T0"], m["tau"]), "",
            "| quantity | value |", "|---|---|"]
    for key in ("state", "sigma_hat", "ADMIT", "admissible", "sd_corrected", "sd_student",
                "z_corrected", "z_student", "p_fair", "p_t", "log_phi_z_corrected",
                "log_t_cdf_z_student", "LINK_NU", "resolved_up"):
        out.append("| `%s` | %s |" % (key, m[key]))
    for kind in ("admissible", "all"):
        v = m["under_the_%s_member_lambda_hat" % kind]
        if isinstance(v, str):
            out.append("| contribution under the %s-member `λ̂` | %s |" % (kind, v))
        else:
            out.append("| %s-member `λ̂` · contribution to `ll(λ̂)` · to `ll(1)` | %.6f · %.6f · "
                       "%.6f |" % (kind, v["lambda_hat"], v["contribution_to_ll_at_lambda_hat"],
                                   v["contribution_to_ll_at_one"]))

    v2 = doc["V2"]
    out += ["", "## V2", "", "| count | value |", "|---|---|"]
    for key in ("members", "checkpoints", "sigma_hat_bit_identical", "student_sd_bit_identical",
                "control_moved_sigma_hat", "control_moved_student_sd",
                "control_subject_stamped_at_the_checkpoint_instant",
                "fewest_reports_perturbed_in_one_checkpoint"):
        out.append("| `%s` | %s |" % (key, v2[key]))
    out += ["", "Sample: %s" % ", ".join(str(t) for t in v2["sample"])]

    v4 = doc["V4"]
    out += ["", "## V4", "", "| tau | fit anchors | `RMS(r)`, fit | TZ-07b printed | test-1 "
            "anchors | `RMS(r)`, test 1 | TZ-08a printed | `RMS(u)`, test 1 | TZ-08a printed |",
            "|---|---|---|---|---|---|---|---|---|"]
    for tau in pfair.TAUS:
        a, b = v4["lambda_fit_set"][tau], v4["rms_test1"][tau]
        out.append("| %d | %d | %.9f | %s | %d | %.9f | %s | %.9f | %s |" % (
            tau, a["anchors"], a["rms_r"], a["published"], b["anchors"], b["rms_r"],
            b["published"], b["rms_u"], b["rms_u_published"]))
    lam = v4["lambda_hat_default"]
    g = v4["member_r_guard"]
    out += ["", "`tz07a.lambda_hat` at its default, tau = %d, n = %d: %s (expected %s)" % (
        lam["tau"], lam["n"], lam["printed"], lam["expected"]),
        "", "`tz07b.member_r` guard: %d members = %d first fit members + %d fit and %d test-1 "
            "members M6 drops a second of, overlap %s: %s" % (
                g["count"], g["first_fit_members"], g["fit_members_M6_drops_a_second_of"],
                g["test1_members_M6_drops_a_second_of"],
                ", ".join(str(t) for t in g["overlap_with_the_first_20"]) or "none",
                ", ".join(str(t) for t in g["members"]))]

    v6 = doc["V6"]
    out += ["", "## V6", "", "merge base `%s` · head `%s`" % (v6["merge_base"], v6["head"]), "",
            "| file | lines added | lines removed | top-level objects before | byte-identical "
            "after | exempt | objects added |", "|---|---|---|---|---|---|---|"]
    for name, f in v6["files"].items():
        out.append("| `%s` | %d | %d | %d | %d | %s | %s |" % (
            name, f["lines_added"], f["lines_removed"], f["objects_before"],
            f["objects_byte_identical"], ", ".join("`%s`" % n for n in f["objects_exempt"])
            or "—", ", ".join("`%s`" % n for n in f["objects_added"]) or "—"))
    out += ["", "Attribute assignments in the instrument: %s · name bindings scanned: %d" % (
        v6["attribute_assignments_in_the_instrument"] or "none", v6["name_bindings_scanned"]),
        "", "```diff", v6["tz07a_diff"].rstrip("\n"), "```"]

    v7 = doc["V7"]
    out += ["", "## V7", "", "Self-test counts: %s · total %d · exit %d" % (
        ", ".join("%s %d" % kv for kv in v7["counts"].items()), v7["total"],
        v7["exit_status"]), "", "```"] + v7["tz11a_output"] + ["```"]

    out += ["", "## V8", "", "| table | tau | measured | six significant digits | `pfair.py` | "
            "equal |", "|---|---|---|---|---|---|"]
    for row in doc["V8"]:
        out.append("| `%s` | %d | %s | %s | %s | %s |" % (
            row["table"], row["tau"], row["measured"], row["measured_6sd"], row["in_pfair"],
            "yes" if row["equal"] else "no"))

    for name in SETS:
        out += ["", "## V11 — the %s walk" % SET_NAMES[name], ""] + tz10b.disclosure(
            doc["disclosure"][name])
    out += ["", "## V11 — admissibility, every member at every tau", "",
            "`ADMIT`: %s. Each cell is `sigma_hat`, then `yes` when it is at or above "
            "`ADMIT[tau]`." % " · ".join("%d: %s" % (tau, doc["ADMIT"][tau])
                                         for tau in pfair.TAUS), "",
            "| T0 | set | %s |" % " | ".join(str(tau) for tau in pfair.TAUS),
            "|---|---|%s" % ("---|" * len(pfair.TAUS))]
    set_of = {r["T0"]: name for name in SETS for r in doc["disclosure"][name] if r["member"]}
    for t0, row in doc["admissibility"].items():
        out.append("| %d | %s | %s |" % (t0, set_of[t0], " | ".join(
            "%.6f %s" % (row[tau][0], "yes" if row[tau][1] else "no") for tau in pfair.TAUS)))
    f = doc["observations_file"]
    out += ["", "## Observations file", "",
            "%d lines · %d bytes · SHA-256 `%s`" % (f["lines"], f["bytes"], f["sha256"])]
    return "\n".join(out) + "\n"


def main(argv):
    if argv[1:] == ["--emit"]:
        emit()
        return 0
    if argv[1:2] != ["--out"] or len(argv) != 3:
        sys.stderr.write("usage: python -B tz11a-student-link.py --out <directory> | --emit\n")
        return 2
    target = os.path.realpath(argv[2])
    capture = os.path.realpath(config.ROOT)
    assert os.path.isdir(target), "no directory %s" % target
    assert not (target + os.sep).startswith(capture + os.sep), \
        "V9: %s is inside the capture" % target
    doc, csv, host = build()
    outputs = {"tz11a-results.json": json.dumps(doc, sort_keys=True, indent=2, default=str) + "\n",
               "tz11a-tables.md": tables(doc),
               "tz11a-observations.csv": csv,
               "tz11a-host.json": json.dumps(host, sort_keys=True, indent=2, default=str) + "\n"}
    for name, text in outputs.items():
        with open(os.path.join(target, name), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
