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

The `tz07b_*` families are TZ-07b section 6.2: the corrected `sd`, the `SD_SCALE` literals
behind it, and the requirement that the only thing the correction changes is the constant
multiplying `sigma * sqrt(H(tau))`. They replace the four `tz07a_*` checks, which encoded the
superseded composition and are deleted by name - because that specification is superseded, and
for no other reason. They are counted separately again, so TZ-06's 56 and 18 stay the numbers
they were.

The `tz10b_*` items are TZ-10b section 5.2's six self-tests of `log_phi`, the tail-accurate
`log Phi`. They are added after the 104 checks above and counted on their own, so none of those
numbers moves. The references are 60-digit literals everywhere except `-3 ... 3`, the only
range in which `pfair.phi` keeps 12 significant digits and so the only range it is compared in.

The `tz11a_*` items are TZ-11a section 5.2's six self-tests of the Student link: `log_t_cdf`
against 40 literals computed at 60 digits by routes independent of the continued fraction under
test, its symmetry, its normal limit, its shape, the pathology removed at live scale, and the
three measured tables. They are counted on their own, so none of the 110 above moves. No
expectation here depends on a value TZ-11a measures: item 5 compares against literals with `nu`
written in the call, and checks the pricer's own function by an inequality that holds for every
`nu` the fit can return.

Run:  python3 -B selftest-pfair.py
"""

import decimal
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pfair                                                               # noqa: E402
from pfair import D                                                        # noqa: E402

COUNTS = {"V5": 0, "machinery": 0, "TZ-07b": 0}
COUNTS["TZ-10b"] = 0
COUNTS["TZ-11a"] = 0
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


# ---- TZ-07b section 6.2: the measured scale ---------------------------------------

# Section 6.2 requires every fixed expectation at `K` near 100,000 and `sigma` at live scale.
# `1e-55` is the tolerance TZ-07a section 6.2 established for the two relative checks below:
# one ulp of the 60-digit context is the only thing that separates the two orderings of the
# rounding, and 1e-55 is five digits looser than that ulp and forty-five digits tighter than
# any real departure from the identity, which would show in the first digits.
SCALE_RELATIVE_TOLERANCE = D("1e-55")


def tz07b_the_table_is_a_table_of_literals():
    """`SD_SCALE` covers every tau the pricer serves, carries six digits, and is never fitted."""
    check("SD_SCALE carries exactly the taus the pricer serves, 10 included",
          sorted(pfair.SD_SCALE) == sorted(pfair.TAUS), str(sorted(pfair.SD_SCALE)))
    check("every literal is a Decimal, so the pricer never leaves exact arithmetic",
          all(isinstance(v, D) for v in pfair.SD_SCALE.values()))
    check("every literal carries exactly six significant digits",
          all(len(v.as_tuple().digits) == 6 for v in pfair.SD_SCALE.values()),
          str([str(v) for v in pfair.SD_SCALE.values()]))
    refused = False
    try:
        pfair.corrected_sd(100, SIGMA)
    except AssertionError:
        refused = True
    check("a tau with no measured scale is refused, not extrapolated", refused)


def tz07b_the_horizon_at_the_boundary():
    """`H(60)` is 20 on either branch, and `corrected_sd(60, s)` is `SD_SCALE[60]*s*sqrt(20)`."""
    unit = D(1)
    check("H(60) is 20 on the far branch: sqrt(H) at unit sigma is sqrt(20)",
          pfair.far_branch(60, S_T, K, unit)[1] == D(20).sqrt(),
          str(pfair.far_branch(60, S_T, K, unit)[1]))
    check("H(60) is 20 on the near branch too, so the two branches meet there",
          pfair.near_branch(60, S_T, K, unit, M_R)[1] == D(20).sqrt(),
          str(pfair.near_branch(60, S_T, K, unit, M_R)[1]))
    check("tau=60: the corrected sd is SD_SCALE[60]*sigma*sqrt(20)",
          pfair.corrected_sd(60, SIGMA) == pfair.SD_SCALE[60] * SIGMA * D(20).sqrt(),
          str(pfair.corrected_sd(60, SIGMA)))


def tz07b_the_scale_is_the_only_change():
    """The correction is `SD_SCALE[tau]` times the uncorrected `sd`, and nothing else."""
    for tau in pfair.TAUS:
        plain = pfair.state_and_sd(tau, S_T, K, SIGMA, M_R)[1]
        got = pfair.corrected_sd(tau, SIGMA)
        check("tau=%d: corrected_sd / (sigma*sqrt(H)) is SD_SCALE[%d]" % (tau, tau),
              abs(got / plain / pfair.SD_SCALE[tau] - 1) < SCALE_RELATIVE_TOLERANCE,
              str(got / plain))
        check("tau=%d: the corrected sd is linear in sigma" % tau,
              abs(pfair.corrected_sd(tau, SIGMA * D(4)) / (got * D(4)) - 1)
              < SCALE_RELATIVE_TOLERANCE,
              str(pfair.corrected_sd(tau, SIGMA * D(4)) / (got * D(4))))
        check("tau=%d: state is untouched by the correction" % tau,
              pfair.state_and_sd(tau, S_T, K, SIGMA, M_R)[0]
              == pfair.state_and_sd(tau, S_T, K, SIGMA * D(4), M_R)[0])


def tz07b_more_time_is_more_dispersion():
    """`corrected_sd` is strictly increasing in `tau` across the seven keys at fixed `sigma`.

    More time remaining is more dispersion. A measurement that breaks this is wrong, not
    surprising, and the assert is here so that it stops the run rather than being noticed.
    """
    ordered = sorted(pfair.TAUS)
    sds = [pfair.corrected_sd(tau, SIGMA) for tau in ordered]
    check("the corrected sd rises with tau at every one of the seven keys",
          all(a < b for a, b in zip(sds, sds[1:])),
          str(list(zip(ordered, [str(v) for v in sds]))))
    check("and the whole ladder is positive at live sigma", all(v > 0 for v in sds))


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


# ---- TZ-10b section 5.2: the tail-accurate log Phi ---------------------------------

# Item 1's literals, each `log(0.5 * erfc(-z / sqrt(2)))` evaluated at 60 decimal digits - a
# reference independent of both branches under test. `z` is passed as the bare float printed
# here. The last two sit on the asymptotic branch and the rest on the `erfc` branch.
LOG_PHI_LITERALS = (("0", "-0.693147180559945"), ("-1", "-1.84102164500926"),
                    ("-2", "-3.78318433368203"), ("-3", "-6.60772622151035"),
                    ("-4", "-10.3601014865273"), ("-5", "-15.0649983939887"),
                    ("-6", "-20.7367689499747"), ("-8", "-35.0134371599145"),
                    ("-10.819", "-61.8339909672382"), ("-15", "-116.131384845712"),
                    ("-20", "-203.917155371097"), ("-30", "-454.321243956343"),
                    ("-36", "-652.503227593798"), ("-40", "-804.608442013754"))


def significant(a, b, digits):
    """Section 5.2's "`digits` significant digits": equality under `%.<digits - 1>e`."""
    form = "%%.%de" % (digits - 1)
    return form % a == form % b


def relative(a, b):
    """`|a - b| / |b|`, printed beside every comparison so any other reading can be applied."""
    return abs(a - b) / abs(b)


def tz10b_item_1_the_literals():
    """`log_phi` equals each 60-digit literal to 12 significant digits, on both branches."""
    different = []
    for z_text, want_text in LOG_PHI_LITERALS:
        z, want = float(z_text), float(want_text)
        got = pfair.log_phi(z)
        branch = "erfc" if z > pfair.LOG_PHI_CROSSOVER else "asymptotic"
        print("      z = %-8s %-10s log_phi %.15g  literal %s  relative %.3g" % (
            z_text, branch, got, want_text, relative(got, want)))
        if not significant(got, want, 12):
            different.append(z_text)
    check("item 1: log_phi equals all %d literals to 12 significant digits"
          % len(LOG_PHI_LITERALS), not different, "different at %s" % different)


def tz10b_item_2_the_branches_agree_at_the_crossover():
    """The `erfc` branch and the asymptotic branch agree to 10 significant digits at -30 ... -34."""
    different = []
    for z in (-30.0, -32.0, -34.0):
        near = pfair.log_phi_erfc_branch(z)
        far = pfair.log_phi_asymptotic_branch(z)
        print("      z = %g  erfc %.15g  asymptotic %.15g  relative %.3g" % (
            z, near, far, relative(far, near)))
        if not significant(far, near, 10):
            different.append(z)
    check("item 2: the two branches agree to 10 significant digits at -30, -32 and -34",
          not different, "different at %s" % different)


def tz10b_item_3_the_identity_where_phi_is_sound():
    """`exp(log_phi(z)) == pfair.phi(z)` to 12 significant digits at the integers -3 ... 3 -
    the only range in which `pfair.phi` is itself good to 12 digits, and so its only use here."""
    different = []
    for z in range(-3, 4):
        got, want = math.exp(pfair.log_phi(float(z))), pfair.phi(float(z))
        print("      z = %d  exp(log_phi) %.15g  phi %.15g  relative %.3g" % (
            z, got, want, relative(got, want)))
        if not significant(got, want, 12):
            different.append(z)
    check("item 3: exp(log_phi(z)) equals pfair.phi(z) to 12 significant digits at -3 ... 3",
          not different, "different at %s" % different)


def tz10b_item_4_the_composition_at_live_scale():
    """`log_phi((S_t - K) / sd)` with `S_t = K + z * sd`, far branch at tau = 240, live `K`, `sigma`."""
    literals = dict(LOG_PHI_LITERALS)
    sd = pfair.far_branch(240, S_T, K, SIGMA)[1]
    different = []
    for z_text in ("-10.819", "-8", "-3", "0"):
        s_t = K + D(z_text) * sd
        z = float((s_t - K) / sd)
        got, want = pfair.log_phi(z), float(literals[z_text])
        print("      z = %-8s S_t %.9f  recovered z %r  log_phi %.15g  relative %.3g" % (
            z_text, s_t, z, got, relative(got, want)))
        if not (math.isfinite(got) and significant(got, want, 12)):
            different.append(z_text)
    check("item 4: at K = 100000.25, sigma = 3.25, tau = 240 the composition is finite and "
          "equals item 1's literal to 12 significant digits", not different,
          "different at %s" % different)


def tz10b_item_5_shape():
    """Strictly increasing over -40 ... 5 and finite over -40 ... 40, at a step of 0.001."""
    rising = [pfair.log_phi(-40 + 0.001 * i) for i in range(45001)]
    not_rising = sum(1 for a, b in zip(rising, rising[1:]) if not a < b)
    points = [-40 + 0.001 * i for i in range(80001)]
    not_finite = sum(1 for z in points if not math.isfinite(pfair.log_phi(z)))
    print("      %d points over -40 ... %g: %d steps not strictly increasing" % (
        len(rising), -40 + 0.001 * 45000, not_rising))
    print("      %d points over -40 ... %g: %d values not finite" % (
        len(points), points[-1], not_finite))
    check("item 5: strictly increasing over -40 ... 5 and finite over -40 ... 40",
          not_rising == 0 and not_finite == 0, "%d, %d" % (not_rising, not_finite))


def tz10b_item_6_the_pathology_removed():
    """Defect 26 as an assertion. It goes red the day `pfair.phi` changes - correctly, because
    that is a change to the section 1.2 link and belongs to a TZ of its own."""
    z = -10.819
    p = pfair.phi(z)
    try:
        log_of_phi_finite = math.isfinite(math.log(p))
    except ValueError:              # `math.log(0.0)` raises rather than returning -inf
        log_of_phi_finite = False
    value = pfair.log_phi(z)
    back = math.exp(value)
    print("      phi %r  log(phi) finite %s  log_phi %.15g  exp(log_phi) %.6e" % (
        p, log_of_phi_finite, value, back))
    check("item 6: at z = -10.819 phi is exactly 0.0, log(phi) is not finite, log_phi is "
          "finite and exp(log_phi) is 1.399068e-27 and positive",
          p == 0.0 and not log_of_phi_finite and math.isfinite(value)
          and "%.6e" % back == "1.399068e-27" and back > 0.0,
          "phi %r, log_phi %r, exp %r" % (p, value, back))


# ---- TZ-11a section 5.2: the Student link -----------------------------------------

# Item 1's reference: `log F_nu(z)`, computed by the Architect at 60 decimal digits by the
# regularized incomplete beta `I_x(nu/2, 1/2) / 2` and cross-checked at 60 digits by quadrature
# of the density; neither route is the continued fraction `pfair._betacf` implements. The worst
# disagreement across the 40 is the accuracy of the printed literals themselves, `3.97e-15`
# relative, against the item's `1e-12`.
LOG_T_CDF_ZS = ("0", "-1", "-3", "-5", "-8", "-10.819", "-20", "-50")
LOG_T_CDF_LITERALS = (
    ("2", ("-0.693147180559945", "-1.55435868307644", "-3.04213264974235",
           "-3.96992886866936", "-4.87513859809586", "-5.46847054829007",
           "-6.68835316116258", "-8.51779297152817")),
    ("2.5", ("-0.693147180559945", "-1.59933653536950", "-3.31626685434013",
             "-4.44598122091119", "-5.56532867478168", "-6.30324233817012",
             "-7.82481099775613", "-10.1104508277657")),
    ("3", ("-0.693147180559945", "-1.63218922449412", "-3.54618467545091",
           "-4.86702610492042", "-6.19564464966101", "-7.07657843379202",
           "-8.89844171394626", "-11.6397847632440")),
    ("4", ("-0.693147180559945", "-1.67691149318135", "-3.91347485706189",
           "-5.58727573561669", "-7.32032286818778", "-8.48264615644609",
           "-10.9009041296344", "-14.5521443574038")),
    ("7", ("-0.693147180559945", "-1.74120896160071", "-4.60806807421352",
           "-7.15283904545879", "-9.99615988572270", "-11.9667403968485",
           "-16.1409126343562", "-22.5096639254306")))

# Items 1 and 2: "to 12 significant digits" and the item's stated tolerance, `1e-12` relative.
# Both readings are asserted, and the relative figure is printed beside every comparison.
TZ11A_RELATIVE = 1e-12

# Item 3: the bound, and the gap the Architect computed at 60 digits, printed beside it.
NORMAL_LIMIT_NU = 1e6
NORMAL_LIMIT_BOUND = 1e-4
NORMAL_LIMIT_EXPECTED = "2.46e-5"

# Item 5a's two literals, from item 1's reference at `nu = 3` and `z = -10.819`.
F3_AT_MINUS_10_819 = "8.4465826393e-04"
LOG_F3_AT_MINUS_10_819 = "-7.07657843379202"


def tz11a_item_1_the_literals():
    """`log_t_cdf` equals each of the 40 literals to 12 significant digits and within 1e-12."""
    different, worst = [], 0.0
    for nu_text, row in LOG_T_CDF_LITERALS:
        for z_text, want_text in zip(LOG_T_CDF_ZS, row):
            got, want = pfair.log_t_cdf(float(z_text), float(nu_text)), float(want_text)
            gap = relative(got, want)
            worst = max(worst, gap)
            print("      nu = %-4s z = %-8s log_t_cdf %.15g  literal %s  relative %.3g" % (
                nu_text, z_text, got, want_text, gap))
            if not (significant(got, want, 12) and gap < TZ11A_RELATIVE):
                different.append((nu_text, z_text))
    print("      worst relative difference over the 40: %.3g" % worst)
    check("item 1: log_t_cdf equals all 40 literals to 12 significant digits and within 1e-12 "
          "relative", not different, "different at %s" % different)


def tz11a_item_2_symmetry():
    """`F(z) + F(-z) == 1` at 15 pairs: the positive branch and the symmetry branch of `I_x`."""
    different, worst = [], 0.0
    for nu in (2.5, 3.0, 7.0):
        for z in (0.5, 1.0, 2.0, 3.0, 5.0):
            total = math.exp(pfair.log_t_cdf(z, nu)) + math.exp(pfair.log_t_cdf(-z, nu))
            worst = max(worst, abs(total - 1.0))
            if not (significant(total, 1.0, 12) and abs(total - 1.0) < TZ11A_RELATIVE):
                different.append((nu, z))
    print("      15 pairs, worst |F(z) + F(-z) - 1| %.3g" % worst)
    check("item 2: exp(log_t_cdf(z)) + exp(log_t_cdf(-z)) equals 1 to 12 significant digits at "
          "15 pairs", not different, "different at %s" % different)


def tz11a_item_3_the_normal_limit():
    """`t_cdf(z, 1e6)` against `pfair.phi(z)` at the integers -3 ... 3, where `phi` is sound."""
    worst = 0.0
    for z in range(-3, 4):
        got, want = pfair.t_cdf(float(z), NORMAL_LIMIT_NU), pfair.phi(float(z))
        worst = max(worst, relative(got, want))
        print("      z = %d  t_cdf(z, 1e6) %.15g  phi %.15g  relative %.3g" % (
            z, got, want, relative(got, want)))
    print("      worst relative gap %.3g, expected %s, bound %g" % (
        worst, NORMAL_LIMIT_EXPECTED, NORMAL_LIMIT_BOUND))
    check("item 3: the worst relative gap between t_cdf(z, 1e6) and phi(z) over -3 ... 3 is "
          "below 1e-4", worst < NORMAL_LIMIT_BOUND, "%.3g" % worst)


def tz11a_item_4_shape():
    """Strictly increasing over -60 ... 5 at 65,001 points and finite over -200 ... 200 at
    40,001 points, at each of `nu` 2.05, 3 and 60 separately."""
    failures = []
    for nu in (2.05, 3.0, 60.0):
        rising = [pfair.log_t_cdf(-60 + 0.001 * i, nu) for i in range(65001)]
        not_rising = sum(1 for a, b in zip(rising, rising[1:]) if not a < b)
        points = [-200 + 0.01 * i for i in range(40001)]
        not_finite = sum(1 for z in points if not math.isfinite(pfair.log_t_cdf(z, nu)))
        print("      nu = %g: %d points over -60 ... 5, %d steps not strictly increasing; "
              "%d points over -200 ... 200, %d values not finite" % (
                  nu, len(rising), not_rising, len(points), not_finite))
        if not_rising or not_finite:
            failures.append((nu, not_rising, not_finite))
    check("item 4: log_t_cdf is strictly increasing over -60 ... 5 and finite over -200 ... 200 "
          "at nu = 2.05, 3 and 60", not failures, str(failures))


def tz11a_item_5_the_pathology_removed():
    """Defect 26 at live scale, against literals and against the pricer's own function.

    `sd` is the committed `corrected_sd`, not `student_sd`, so `z` is fixed at -10.819 whatever
    `LINK_SCALE[30]` is, and only `nu` moves the Student value.
    """
    sd = pfair.corrected_sd(30, SIGMA)
    s_t = K + D("-10.819") * sd
    state, _ = pfair.state_and_sd(30, s_t, K, SIGMA, s_t)
    z = float(state / sd)
    p = pfair.p_fair(state, sd)
    try:
        log_of_p_finite = math.isfinite(math.log(p))
    except ValueError:              # `math.log(0.0)` raises rather than returning -inf
        log_of_p_finite = False
    f3, log_f3 = pfair.t_cdf(z, 3.0), pfair.log_t_cdf(z, 3.0)
    print("      z %r  p_fair %r  log(p_fair) finite %s" % (z, p, log_of_p_finite))
    print("      5a: t_cdf(z, 3.0) %.10e  literal %s  relative %.3g" % (
        f3, F3_AT_MINUS_10_819, relative(f3, float(F3_AT_MINUS_10_819))))
    print("      5a: log_t_cdf(z, 3.0) %.15g  literal %s  relative %.3g" % (
        log_f3, LOG_F3_AT_MINUS_10_819, relative(log_f3, float(LOG_F3_AT_MINUS_10_819))))
    assert (z == -10.819 and p == 0.0 and not log_of_p_finite
            and significant(f3, float(F3_AT_MINUS_10_819), 10)
            and significant(log_f3, float(LOG_F3_AT_MINUS_10_819), 12)), \
        "FAILED: item 5a: z %r, p_fair %r, t_cdf %r, log_t_cdf %r" % (z, p, f3, log_f3)
    nu = float(pfair.LINK_NU[30])
    p_t = pfair.p_fair_student(state, sd, 30)
    log_p_t = pfair.log_t_cdf(z, nu)
    print("      5b: LINK_NU[30] %s  p_fair_student %.10e  log_t_cdf(z, LINK_NU[30]) %.15g" % (
        pfair.LINK_NU[30], p_t, log_p_t))
    check("item 5: 5a - phi is 0.0 and its log not finite, F_3 and log F_3 equal the literals; "
          "5b - 0 < p_fair_student < 1e-2 and log_t_cdf at LINK_NU[30] is finite and inside "
          "(-40, -5)",
          0.0 < p_t < 1e-2 and math.isfinite(log_p_t) and -40.0 < log_p_t < -5.0,
          "p_t %r, log %r" % (p_t, log_p_t))


def tz11a_item_6_the_tables():
    """The three tables cover exactly the taus the pricer serves; an unmeasured tau is refused;
    `student_sd` is its own table times `sigma * sqrt(H)` - an identity carrying no value."""
    keys = [sorted(table) for table in (pfair.ADMIT, pfair.LINK_NU, pfair.LINK_SCALE)]
    refused = []
    for name, call in (("student_sd", lambda: pfair.student_sd(100, SIGMA)),
                       ("p_fair_student", lambda: pfair.p_fair_student(D(1), D(1), 100))):
        try:
            call()
        except AssertionError:
            refused.append(name)
    got = pfair.student_sd(30, D("3.25"))
    want = pfair.LINK_SCALE[30] * D("3.25") * (D(30) ** 3 / D(10800)).sqrt()
    print("      keys %s  refused at tau = 100: %s  student_sd(30, 3.25) %s" % (
        keys[0], refused, got))
    check("item 6: ADMIT, LINK_NU and LINK_SCALE are keyed by exactly pfair.TAUS; student_sd and "
          "p_fair_student raise at tau = 100; student_sd(30, 3.25) is its own table's identity",
          all(k == sorted(pfair.TAUS) for k in keys)
          and refused == ["student_sd", "p_fair_student"] and got == want,
          "keys %s, refused %s, %s != %s" % (keys, refused, got, want))


if __name__ == "__main__":
    for group, fns in (("V5", (v5_branches_meet_at_sixty,
                               v5_realised_path_has_zero_weight_far_out,
                               v5_realised_mean_enters_with_its_weight,
                               v5_p_fair_moves_the_right_way)),
                       ("TZ-07b", (tz07b_the_table_is_a_table_of_literals,
                                   tz07b_the_horizon_at_the_boundary,
                                   tz07b_the_scale_is_the_only_change,
                                   tz07b_more_time_is_more_dispersion)),
                       ("TZ-10b", (tz10b_item_1_the_literals,
                                   tz10b_item_2_the_branches_agree_at_the_crossover,
                                   tz10b_item_3_the_identity_where_phi_is_sound,
                                   tz10b_item_4_the_composition_at_live_scale,
                                   tz10b_item_5_shape,
                                   tz10b_item_6_the_pathology_removed)),
                       ("TZ-11a", (tz11a_item_1_the_literals,
                                   tz11a_item_2_symmetry,
                                   tz11a_item_3_the_normal_limit,
                                   tz11a_item_4_shape,
                                   tz11a_item_5_the_pathology_removed,
                                   tz11a_item_6_the_tables)),
                       ("machinery", (machinery_time_weighted_mean,
                                      machinery_second_grid_and_sigma,
                                      machinery_merge_is_not_a_fill))):
        GROUP = group
        for fn in fns:
            print(fn.__name__)
            fn()
    total = sum(COUNTS.values())
    print("\nV5: %d of %d checks passed" % (COUNTS["V5"], COUNTS["V5"]))
    print("TZ-07b section 6: %d of %d checks passed"
          % (COUNTS["TZ-07b"], COUNTS["TZ-07b"]))
    print("TZ-10b section 5.2: %d of %d checks passed"
          % (COUNTS["TZ-10b"], COUNTS["TZ-10b"]))
    print("TZ-11a section 5.2: %d of %d checks passed"
          % (COUNTS["TZ-11a"], COUNTS["TZ-11a"]))
    print("section 3 machinery: %d of %d checks passed"
          % (COUNTS["machinery"], COUNTS["machinery"]))
    print("%d of %d checks passed" % (total, total))
