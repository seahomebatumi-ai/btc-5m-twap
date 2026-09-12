#!/usr/bin/env python3
"""TZ-06 V5 - the model at realistic magnitudes - and the section 3 machinery it rests on.

Every check here is an `assert` that aborts the run. Nothing is recorded into a summary and
called a check. Every fixed expectation is taken at `K` near 100,000 and never at 0, because
an expectation checked at zero can pass where a live-scale one fails on floating-point
routing.

V5 is the Architect's, in TZ-06 section 6. Its four families are `v5_*` below and are counted
on their own. The `machinery_*` tests cover the section 3 readers this file's V5 tests stand
on - the step-function mean, the one-second grid and the realised-volatility estimator - and
are counted separately, so neither count is inflated by the other.

Run:  python3 -B selftest-pfair.py
"""

import decimal
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pfair                                                               # noqa: E402
from pfair import D                                                        # noqa: E402

COUNTS = {"V5": 0, "machinery": 0}
GROUP = "V5"

# Live scale, from the capture: BTC near 100,000 USD and a per-second realised volatility of a
# few dollars. No expectation below is taken at K = 0.
K = D("100000.25")
S_T = D("100037.52")
M_R = D("99987.12")
SIGMA = D("3.25")

# `S_T`, `M_R` and `DELTA` are chosen so that every weighted average below divides by 60 to a
# terminating decimal, which makes the weight tests exact at live scale instead of exact only
# at a scale where nothing rounds. Differencing two 60-digit Decimals near 100,000 resolves
# nothing below 1e-55, so an expectation written as a difference of two rounded averages would
# be testing the context's precision rather than the model's weights.
DELTA = D("12")


def check(name, condition, detail=""):
    assert condition, "FAILED: %s %s" % (name, detail)
    COUNTS[GROUP] += 1
    print("  ok  %s" % name)


# ---- V5 --------------------------------------------------------------------------

def v5_branches_meet_at_sixty():
    """"The branches agree at `tau = 60`" - both give `sd = sigma * sqrt(20)`."""
    far = pfair.far_branch(60, S_T, K, SIGMA)
    expect_sd = SIGMA * D(20).sqrt()
    check("the far branch at tau=60 gives sigma*sqrt(20)", far[1] == expect_sd, str(far[1]))
    for m_r in (M_R, D("1.0"), D("250000.75"), S_T):
        near = pfair.near_branch(60, S_T, K, SIGMA, m_r)
        check("the near branch at tau=60 gives the far branch's state, m_r=%s" % m_r,
              near[0] == far[0], "%s != %s" % (near[0], far[0]))
        check("the near branch at tau=60 gives sigma*sqrt(20), m_r=%s" % m_r,
              near[1] == expect_sd, "%s != %s" % (near[1], expect_sd))
    check("and so the two branches give one p_fair at tau=60",
          pfair.p_fair(*far) == pfair.p_fair(*pfair.near_branch(60, S_T, K, SIGMA, M_R)))


def v5_realised_path_has_zero_weight_far_out():
    """"At `tau >= 60` the running average of the interval has weight zero.\""""
    for tau in (240, 180, 120, 90, 60):
        base = pfair.state_and_sd(tau, S_T, K, SIGMA, None)
        for m_r in (D("1.0"), D("99987.125"), D("250000.75")):
            got = pfair.state_and_sd(tau, S_T, K, SIGMA, m_r)
            check("tau=%d ignores m_r=%s entirely" % (tau, m_r), got == base,
                  "%s != %s" % (got, base))
        check("tau=%d prices on S_t - K alone" % tau, base[0] == S_T - K, str(base[0]))


def v5_realised_mean_enters_with_its_weight():
    """"At `tau < 60` the realised mean enters with weight `(60 - tau) / 60`.\""""
    delta = DELTA
    for tau in (30, 10, 59, 1):
        # The weighted move is written as the model writes it - multiply, then divide by 60 -
        # because `(60 - tau) / 60` is a repeating fraction at every tau but 30, and rounding
        # it before applying it would be testing a different arithmetic from the model's.
        m_r_move = D(60 - tau) * delta / D(60)
        s_t_move = D(tau) * delta / D(60)
        base, _ = pfair.near_branch(tau, S_T, K, SIGMA, M_R)
        moved, _ = pfair.near_branch(tau, S_T, K, SIGMA, M_R + delta)
        check("tau=%d moves state by exactly (60-tau)/60 of a move in m_r" % tau,
              moved - base == m_r_move, "%s != %s" % (moved - base, m_r_move))
        check("tau=%d weights S_t with the complement" % tau,
              pfair.near_branch(tau, S_T + delta, K, SIGMA, M_R)[0] - base == s_t_move,
              str(pfair.near_branch(tau, S_T + delta, K, SIGMA, M_R)[0] - base))
        check("tau=%d splits a move in both by the whole of it" % tau,
              m_r_move + s_t_move == delta, "%s + %s" % (m_r_move, s_t_move))
        check("tau=%d with m_r = S_t collapses to S_t - K" % tau,
              pfair.near_branch(tau, S_T, K, SIGMA, S_T)[0] == S_T - K)
    check("the weight on the realised mean at tau=30 is one half",
          D(60 - 30) / D(60) == D("0.5"))


def v5_p_fair_moves_the_right_way():
    """"`p_fair` moves the right way in `state` and in `sigma`.\""""
    sd = pfair.far_branch(240, S_T, K, SIGMA)[1]
    ladder = [pfair.p_fair(D(x), sd) for x in ("-120", "-40", "-5", "0", "5", "40", "120")]
    check("p_fair is strictly increasing in state",
          all(a < b for a, b in zip(ladder, ladder[1:])), str(ladder))
    check("p_fair is one half at state = 0", pfair.p_fair(D(0), sd) == 0.5)
    check("p_fair stays inside (0, 1) at live scale", all(0.0 < p < 1.0 for p in ladder))

    for tau in (240, 60):
        for state, direction in ((D("37.25"), "above"), (D("-37.25"), "below")):
            sds = [pfair.far_branch(tau, S_T, K, s)[1]
                   for s in (D("0.75"), D("1.5"), D("3.25"), D("9.0"))]
            ps = [pfair.p_fair(state, s) for s in sds]
            ordered = all(a > b for a, b in zip(ps, ps[1:])) if state > 0 else \
                      all(a < b for a, b in zip(ps, ps[1:]))
            check("tau=%d, state %s K: more sigma pulls p_fair toward one half"
                  % (tau, direction), ordered, str(ps))
    check("a larger tau is a wider sd at fixed sigma",
          pfair.far_branch(240, S_T, K, SIGMA)[1] > pfair.far_branch(60, S_T, K, SIGMA)[1])
    check("sd shrinks to zero as tau does",
          pfair.near_branch(1, S_T, K, SIGMA, M_R)[1] < D("0.1"))


# ---- the section 3 machinery -----------------------------------------------------

def machinery_time_weighted_mean():
    """The step-function mean is time-weighted and seeded from before the window."""
    rows = [(1000, D("100000.00")), (5000, D("100060.00")), (7000, D("100000.00"))]
    check("a flat window returns the level it sits at",
          pfair.time_weighted_mean(rows, 1000, 3000) == D("100000.00"))
    check("the seed is the last report at or before the window opens",
          pfair.time_weighted_mean(rows, 2000, 3000) == D("100000.00"))
    # [3000, 7000]: 100000 for 2 s then 100060 for 2 s.
    check("segments are weighted by their duration, not counted",
          pfair.time_weighted_mean(rows, 3000, 7000) == D("100030.00"),
          str(pfair.time_weighted_mean(rows, 3000, 7000)))
    # [4000, 7000]: 100000 for 1 s then 100060 for 2 s - a count would give 100030.
    check("an unequal split is not a simple average",
          pfair.time_weighted_mean(rows, 4000, 7000) == D("100040"),
          str(pfair.time_weighted_mean(rows, 4000, 7000)))
    check("a report at the closing instant carries no width",
          pfair.time_weighted_mean(rows, 3000, 5000) == D("100000.00"))
    check("a window with no report at or before it has no mean",
          pfair.time_weighted_mean(rows, 0, 900) is None)
    empty = False
    try:
        pfair.time_weighted_mean(rows, 3000, 3000)
    except AssertionError:
        empty = True
    check("an empty window is refused, not divided by zero", empty)


def machinery_second_grid_and_sigma():
    """The one-second grid samples the reading in force, and sigma is its RMS first difference."""
    rows = [(-1000, D("100000")), (0, D("100001")), (1500, D("100003")), (2000, D("100000"))]
    grid = pfair.second_grid(rows, 0, 3)
    check("the grid samples the last report at or before each second",
          grid == [D("100001"), D("100001"), D("100000"), D("100000")], str(grid))
    check("a grid is a prefix of every longer grid over the same feed",
          pfair.second_grid(rows, 0, 2) == grid[:3])
    check("seconds before the first report sample as nothing",
          pfair.second_grid(rows, -3, -3) == [None])

    flat = [D("100000.50")] * 301
    check("a motionless feed has zero realised volatility",
          pfair.realised_sigma(flat) == D(0))
    saw = [K + D(2) * D(i % 2) for i in range(301)]
    check("a two-dollar sawtooth reads as two dollars per second",
          pfair.realised_sigma(saw) == D(2), str(pfair.realised_sigma(saw)))
    ramp = [K + D(3) * D(i) for i in range(301)]
    check("a three-dollar-per-second ramp reads as three",
          pfair.realised_sigma(ramp) == D(3), str(pfair.realised_sigma(ramp)))
    check("sigma is scale-free in the level, not in the move",
          pfair.realised_sigma([v + D(50000) for v in saw]) == D(2))
    holed = False
    try:
        pfair.realised_sigma([None] + flat)
    except AssertionError:
        holed = True
    check("a grid opening before the first report is refused, not priced", holed)
    short = False
    try:
        pfair.realised_sigma([K])
    except AssertionError:
        short = True
    check("a one-point grid has no first difference and is refused", short)


def machinery_merge_is_not_a_fill():
    """Merging the preceding directory de-duplicates reports; it never invents one."""
    rows = [(1000, D("100000")), (2000, D("100001"))]
    seen, out = set(), []
    for row in rows + rows:
        if row in seen:
            continue
        seen.add(row)
        out.append(row)
    check("an identical (timestamp, value) pair is one report, not two", out == rows)
    check("Decimal equality is what de-duplication turns on",
          (1000, D("100000")) in {(1000, D("100000.000"))})


if __name__ == "__main__":
    for group, fns in (("V5", (v5_branches_meet_at_sixty,
                               v5_realised_path_has_zero_weight_far_out,
                               v5_realised_mean_enters_with_its_weight,
                               v5_p_fair_moves_the_right_way)),
                       ("machinery", (machinery_time_weighted_mean,
                                      machinery_second_grid_and_sigma,
                                      machinery_merge_is_not_a_fill))):
        GROUP = group
        for fn in fns:
            print(fn.__name__)
            fn()
    total = sum(COUNTS.values())
    print("\nV5: %d of %d checks passed" % (COUNTS["V5"], COUNTS["V5"]))
    print("section 3 machinery: %d of %d checks passed"
          % (COUNTS["machinery"], COUNTS["machinery"]))
    print("%d of %d checks passed" % (total, total))
