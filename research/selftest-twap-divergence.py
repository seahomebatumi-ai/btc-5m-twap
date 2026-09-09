#!/usr/bin/env python3
"""TZ-01a - validation suite.

TZ-01 section 7 items 1, 4, 5 and 6 unchanged; item 2 as amended by TZ-01a section 2;
item 3 replaced by TZ-01a section 3's perturbation test; plus TZ-01a section 7's
structural assertion on `compute_observation`.

Every check calls the implementation in `research/twap-divergence.py`; nothing in this
file re-derives a section 3 quantity.  Run:

    python3 research/selftest-twap-divergence.py --month 2026-08
"""

import argparse
import ast
import importlib.util
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
IMPLEMENTATION = os.path.join(HERE, "twap-divergence.py")


def load_implementation():
    """Import the hyphenated measurement script as a module."""
    spec = importlib.util.spec_from_file_location("twap_divergence", IMPLEMENTATION)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


TD = load_implementation()

RESULTS = []


def check(name, condition, detail=""):
    RESULTS.append((name, bool(condition), detail))
    print("%-64s %s %s" % (name, "PASS" if condition else "FAIL", detail), flush=True)
    return bool(condition)


# --------------------------------------------------------------------------------------
# TZ-01 section 7.2 items 1 and 2, unchanged; items 3 and 4 as replaced by TZ-01a
# section 2.  The step must land on bar t-1, not bar t, or the path is unobservable at
# the checkpoint.
# --------------------------------------------------------------------------------------

DEFAULT_PRICE = 100000.0

# TZ-01a section 2 states the two `state` expectations as exact equalities.  `state` is
# computed as t * (twap_so_far - K) + tau * (S_t - K), which routes the mean through
# K + 7/18 - a value with no exact binary representation at any K - so the integer
# expectation is unreachable in IEEE-754: at K = 100000 the step-up path lands on
# 8470.000000000291, a relative miss of 3.4e-14.  `S_t` and `twap_so_far` match their
# hand-derived values bit-for-bit, so the causal content of both paths is still checked
# exactly; only the final equality carries a tolerance.  The Architect resolved this,
# directing the tolerance and a note in the report rather than a BLOCKED report; TZ-01
# section 7.2 item 2 already allows 1e-9 on twap_so_far.  Every run prints the deviation
# achieved.
STATE_TOLERANCE = 1e-6


def synthetic(price, prior_level, closes):
    """(prior_closes, interval_opens, interval_closes) for a synthetic path.

    `prior_closes` is flat at `prior_level`; the interval's first open is `price` so that
    K is exactly `price`, and each bar's open equals the previous close.
    """
    closes = np.asarray(closes, dtype="float64")
    prior = np.full(TD.PRIOR_SECONDS, float(prior_level))
    opens = np.empty(TD.INTERVAL_SECONDS)
    opens[0] = float(price)
    opens[1:] = closes[:-1]
    return prior, opens, closes


def test_flat_path(price):
    prior, opens, closes = synthetic(price, price, np.full(TD.INTERVAL_SECONDS, price))
    ok = True
    for tau in TD.CHECKPOINT_TAUS:
        obs = TD.compute_observation(prior, opens, closes, tau)
        ok &= check("7.2 flat path, tau=%d, state == 0" % tau, obs["state"] == 0.0,
                    "state=%r" % obs["state"])
        for variant in TD.VARIANTS:
            ok &= check("7.2 flat path, tau=%d, p_twap_%s == 0.5" % (tau, variant),
                        obs["p_twap_" + variant] == 0.5,
                        "p_twap=%r" % obs["p_twap_" + variant])
    return ok


def test_linear_ramp(price):
    """Ramp from K to K+100 across the interval, each bar sampling its own midpoint.

    The section 7.2 expectation twap_so_far == K + 50 * t / 300 holds exactly for this
    discretisation and for no other linear one; see the report.
    """
    closes = np.array([price + 100.0 * (i + 0.5) / 300.0
                       for i in range(TD.INTERVAL_SECONDS)])
    prior, opens, closes = synthetic(price, price, closes)
    ok = True
    for tau in TD.CHECKPOINT_TAUS:
        obs = TD.compute_observation(prior, opens, closes, tau)
        t = TD.INTERVAL_SECONDS - tau
        expected = price + 50.0 * t / 300.0
        error = abs(obs["twap_so_far"] - expected)
        ok &= check("7.2 linear ramp, tau=%d, twap_so_far to 1e-9" % tau, error < 1e-9,
                    "error=%.3e" % error)
    return ok


def step_up_path(price):
    """TZ-01a section 2: bars 0..178 at K, bars 179..299 at K + 70."""
    closes = np.full(TD.INTERVAL_SECONDS, price)
    closes[179:] = price + 70.0
    return synthetic(price, price, closes)


def round_trip_path(price):
    """TZ-01a section 2: bars 0..178 at K + 40, bars 179..299 at K."""
    closes = np.full(TD.INTERVAL_SECONDS, price + 40.0)
    closes[179:] = price
    return synthetic(price, price + 40.0, closes)


def test_step_up(price):
    prior, opens, closes = step_up_path(price)
    obs = TD.compute_observation(prior, opens, closes, 120)
    ok = check("2 step up at bar 179, twap_so_far == K + 70/180 at tau=120",
               obs["twap_so_far"] == price + 70.0 / 180.0,
               "error=%.3e" % abs(obs["twap_so_far"] - (price + 70.0 / 180.0)))
    ok &= check("2 step up at bar 179, S_t == K + 70 at tau=120",
                obs["S_t"] == price + 70.0, "S_t=%r" % obs["S_t"])
    ok &= check("2 step up at bar 179, state == 8470 at tau=120 (to %.0e)" % STATE_TOLERANCE,
                abs(obs["state"] - 8470.0) <= STATE_TOLERANCE,
                "state=%r deviation=%.3e" % (obs["state"], obs["state"] - 8470.0))
    return ok


def test_round_trip(price):
    prior, opens, closes = round_trip_path(price)
    obs = TD.compute_observation(prior, opens, closes, 120)
    expected_twap = price + 40.0 * 179.0 / 180.0
    ok = check("2 round trip at bar 179, twap_so_far == K + 40*179/180 at tau=120",
               obs["twap_so_far"] == expected_twap,
               "error=%.3e" % abs(obs["twap_so_far"] - expected_twap))
    ok &= check("2 round trip at bar 179, S_t == K at tau=120", obs["S_t"] == price,
                "S_t=%r" % obs["S_t"])
    ok &= check("2 round trip at bar 179, state == 7160 at tau=120 (to %.0e)"
                % STATE_TOLERANCE,
                abs(obs["state"] - 7160.0) <= STATE_TOLERANCE,
                "state=%r deviation=%.3e" % (obs["state"], obs["state"] - 7160.0))
    for variant in TD.VARIANTS:
        gap = obs["p_twap_" + variant] - obs["p_naive_" + variant]
        ok &= check("2 round trip, p_twap_%s exceeds p_naive_%s by > 0.10"
                    % (variant, variant), gap > 0.10, "gap=%.4f" % gap)
    return ok


# --------------------------------------------------------------------------------------
# TZ-01a section 3 - perturbation test.  A perturbation cannot be satisfied by a boundary
# convention: if the code touches any bar at or after the checkpoint, the value changes.
# --------------------------------------------------------------------------------------

PERTURBATION_FIELDS = ("naive_move", "twap_so_far", "state", "sigma_pre", "sigma_live",
                       "p_twap_pre", "p_naive_pre", "p_twap_live", "p_naive_live")
CONTROL_FIELDS = ("S_t", "twap_so_far", "state")
PERTURBATION_FACTOR = 3.0


def identical(a, b):
    """Bit-identical on IEEE-754 bits."""
    return a.hex() == b.hex() if isinstance(a, float) else a == b


def sample_intervals(grid, sample_size, seed):
    usable = [base for _, base, missing in TD.iter_intervals(grid)
              if missing <= TD.MAX_MISSING_BARS
              and base - TD.PRIOR_SECONDS >= grid["first_valid"]]
    if len(usable) < sample_size:
        return None
    rng = np.random.default_rng(seed)
    return [usable[int(i)] for i in rng.choice(len(usable), size=sample_size, replace=False)]


def test_perturbation(month, out_dir, work_dir, sample_size, seed):
    """Future bars replaced by close * 3; nothing readable at the checkpoint may move."""
    zip_path, _ = TD.download_month(month, work_dir)
    grid, _ = TD.build_month_grid(month, zip_path, TD.load_carry(out_dir, month))
    chosen = sample_intervals(grid, sample_size, seed)
    if chosen is None:
        return check("3 perturbation: at least %d intervals available" % sample_size, False)

    compared = 0
    mismatches = []
    controls = 0
    control_failures = []
    for base in chosen:
        prior = grid["closes"][base - TD.PRIOR_SECONDS:base]
        opens = grid["opens"][base:base + TD.INTERVAL_SECONDS]
        closes = grid["closes"][base:base + TD.INTERVAL_SECONDS]
        for tau in TD.CHECKPOINT_TAUS:
            t = TD.INTERVAL_SECONDS - tau
            baseline = TD.compute_observation(prior, opens, closes, tau)

            future = closes.copy()
            future[t:] = future[t:] * PERTURBATION_FACTOR
            perturbed = TD.compute_observation(prior, opens, future, tau)
            for field in PERTURBATION_FIELDS:
                compared += 1
                if not identical(baseline[field], perturbed[field]):
                    mismatches.append((base, tau, field, baseline[field], perturbed[field]))

            past = closes.copy()
            past[t - 1] = past[t - 1] * PERTURBATION_FACTOR
            control = TD.compute_observation(prior, opens, past, tau)
            for field in CONTROL_FIELDS:
                controls += 1
                if identical(baseline[field], control[field]):
                    control_failures.append((base, tau, field, baseline[field]))

    ok = check("3 perturbation of bars >= t, %d intervals, %d value comparisons"
               % (len(chosen), compared), not mismatches,
               "mismatches=%d" % len(mismatches))
    for row in mismatches[:5]:
        print("    mismatch base=%d tau=%d field=%s baseline=%r perturbed=%r" % row)
    ok &= check("3 negative control, perturbing bar t-1 moves S_t, twap_so_far and state, "
                "%d assertions" % controls, not control_failures,
                "unchanged=%d" % len(control_failures))
    for row in control_failures[:5]:
        print("    unchanged base=%d tau=%d field=%s value=%r" % row)
    return ok


# --------------------------------------------------------------------------------------
# TZ-01a section 7 - one slice, one boundary, asserted on the source itself
# --------------------------------------------------------------------------------------


def function_node(tree, name):
    return next(node for node in ast.walk(tree)
                if isinstance(node, ast.FunctionDef) and node.name == name)


def interval_close_subscripts(func):
    return [node for node in ast.walk(func) if isinstance(node, ast.Subscript)
            and isinstance(node.value, ast.Name) and node.value.id == "interval_closes"]


def test_single_slice():
    """`compute_observation` takes exactly one slice of `interval_closes`, and `S_t` and
    `twap_so_far` are both derived from it."""
    tree = ast.parse(open(IMPLEMENTATION).read())
    func = function_node(tree, "compute_observation")
    subscripts = interval_close_subscripts(func)
    ok = check("7 compute_observation indexes interval_closes exactly once",
               len(subscripts) == 1,
               "lines %s" % [node.lineno for node in subscripts])
    if not subscripts:
        return False
    node = subscripts[0]
    is_checkpoint_slice = (isinstance(node.slice, ast.Slice) and node.slice.lower is None
                           and node.slice.step is None
                           and isinstance(node.slice.upper, ast.Name)
                           and node.slice.upper.id == "t")
    ok &= check("7 the one expression is the checkpoint slice interval_closes[:t]",
                is_checkpoint_slice, "line %d" % node.lineno)

    assignment = next((a for a in ast.walk(func)
                       if isinstance(a, ast.Assign) and a.value is node), None)
    slice_name = assignment.targets[0].id if assignment else None
    ok &= check("7 the slice is bound to one name", slice_name is not None,
                "name=%s line=%s" % (slice_name, assignment.lineno if assignment else "-"))

    call = next(c for c in ast.walk(func) if isinstance(c, ast.Call)
                and isinstance(c.func, ast.Name) and c.func.id == "checkpoint_quantities")
    keywords = {kw.arg: kw.value for kw in call.keywords}
    for field in ("S_t", "twap_so_far"):
        names = {x.id for x in ast.walk(keywords[field]) if isinstance(x, ast.Name)}
        ok &= check("7 %s is derived from %s" % (field, slice_name),
                    slice_name in names,
                    "line %d" % keywords[field].lineno)

    legacy = function_node(tree, "compute_observation_tz01_reading")
    legacy_subscripts = interval_close_subscripts(legacy)
    ok &= check("7 the TZ-01 reading kept for section 5 indexes it more than once",
                len(legacy_subscripts) > 1,
                "lines %s" % [node.lineno for node in legacy_subscripts])
    return ok


# --------------------------------------------------------------------------------------
# TZ-01 section 7.5 - determinism
# --------------------------------------------------------------------------------------


def test_determinism(month, out_dir, work_dir):
    reference = TD.partition_path(out_dir, month)
    if not os.path.exists(reference):
        return check("7.5 determinism for %s" % month, False, "no partition on disk")
    scratch = os.path.join(work_dir, "determinism-%s.parquet" % month)
    TD.rerun_month(month, out_dir, work_dir, scratch)
    first, second = TD.sha256_of(reference), TD.sha256_of(scratch)
    os.remove(scratch)
    return check("7.5 determinism, %s partition byte-identical" % month, first == second,
                 "%s vs %s" % (first[:16], second[:16]))


# --------------------------------------------------------------------------------------
# TZ-01 section 7.4 - coverage counts
# --------------------------------------------------------------------------------------


def report_coverage(out_dir):
    coverage = TD.load_coverage(out_dir)
    months = sorted(coverage["months"])
    if not months:
        print("no coverage recorded")
        return True
    totals = {}
    for month in months:
        for key, value in coverage["months"][month].items():
            if isinstance(value, int):
                totals[key] = totals.get(key, 0) + value
    print("\n7.4 coverage counts")
    print("  months processed:                        %s" % TD.n(len(months)))
    for key in ("raw_rows", "intervals_found", "intervals_skipped_gap",
                "intervals_skipped_no_history", "intervals_used",
                "bars_forward_filled_in_intervals",
                "intervals_with_filled_prior_window", "observations"):
        print("  %-40s %s" % (key + ":", TD.n(totals.get(key, 0))))
    return True


def main(argv=None):
    parser = argparse.ArgumentParser(description="TZ-01a validation suite")
    parser.add_argument("--out-dir", default=os.path.join(HERE, "out"))
    parser.add_argument("--work-dir", default=os.environ.get("TZ01_WORK_DIR", "/tmp/tz01-work"))
    parser.add_argument("--month", default=None,
                        help="month used by the perturbation and determinism checks")
    parser.add_argument("--sample-size", type=int, default=500)
    parser.add_argument("--seed", type=int, default=20260908)
    parser.add_argument("--price", type=float, default=DEFAULT_PRICE,
                        help="K for the synthetic paths of section 2")
    parser.add_argument("--skip-data-tests", action="store_true",
                        help="run only the synthetic and source checks")
    args = parser.parse_args(argv)

    print("Section 2 - analytic self-tests at K = %r\n" % args.price)
    ok = test_flat_path(args.price)
    ok &= test_linear_ramp(args.price)
    ok &= test_step_up(args.price)
    ok &= test_round_trip(args.price)

    print("\nSection 7 - one slice, one boundary\n")
    ok &= test_single_slice()

    if not args.skip_data_tests:
        month = args.month or sorted(TD.load_coverage(args.out_dir)["months"])[-1]
        print("\nSection 3 - perturbation test on %s\n" % month)
        ok &= test_perturbation(month, args.out_dir, args.work_dir, args.sample_size,
                                args.seed)
        print("\nSection 7.5 - determinism on %s\n" % month)
        ok &= test_determinism(month, args.out_dir, args.work_dir)
        report_coverage(args.out_dir)

    failed = [name for name, passed, _ in RESULTS if not passed]
    print("\n%d checks run, %d passed, %d failed" % (len(RESULTS), len(RESULTS) - len(failed),
                                                     len(failed)))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
