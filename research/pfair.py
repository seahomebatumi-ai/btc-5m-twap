#!/usr/bin/env python3
"""The pricer: the only implementation of the TZ-06 section 3 model, in any language.

The model is the Architect's, quoted verbatim in TZ-06 section 3. This file implements it
once. The pipeline `tz06-calibration.py` and the self-tests `selftest-pfair.py` both call in
here, and neither carries a formula of its own.

The stream reader is not rewritten either. `reports`, `last_at_or_before`,
`first_at_or_after`, `venue`, `published_equal`, `load_manifests` and `reasons_for` come from
`research/recorder/analyze.py`, which already holds the only implementation of each.

Every timestamp used here is the venue payload's own `timestamp`, in milliseconds. The
recorder's `recv_ns` is never a pricing input and nothing in this file makes a latency claim.

Arithmetic is `decimal.Decimal` up to the final division, exactly as `analyze.py` handles
prices; only `state / sd` leaves Decimal, to be handed to `math.erf`.
"""

import decimal
import math
import os
import sys

_RECORDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "recorder")
if _RECORDER not in sys.path:
    sys.path.insert(0, _RECORDER)

import config                                                              # noqa: E402
from analyze import (MS, first_at_or_after, last_at_or_before,             # noqa: E402
                     published_equal, reports)

decimal.getcontext().prec = 60
D = decimal.Decimal

# TZ-06 section 3. The settlement window is the last 60 seconds of the interval; the run-up
# window the volatility estimators read is the 300 seconds before the open.
SETTLEMENT_S = 60
RUNUP_S = 300

# TZ-06 section 6. The six gated checkpoints plus tau = 10, which is measured and carries no
# threshold. `t = 300 - tau`.
GATED_TAUS = (240, 180, 120, 90, 60, 30)
TAUS = GATED_TAUS + (10,)


# ---- the model ------------------------------------------------------------------

def phi(z):
    """The standard normal CDF, from `math.erf`."""
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


# ---- TZ-10b section 5.2: the tail-accurate log of Phi ------------------------------

# `phi` above is `0.5 * (1 + erf)`, the sum of two doubles near 1 once `z` is far below zero:
# it loses relative accuracy below about `z = -4.5` and returns exactly 0.0 below about
# `z = -8.37`, which sent TZ-08a's `ll(1)` to `-inf` at `tau = 30`. A likelihood over `Phi`
# carries a tail-accurate `log Phi` beside it (System Map section 7 item 26), and this is that
# function. `phi` is not touched: changing it would be a change to the section 1.2 link.
#
# Two branches, as TZ-10b section 5.2 writes them. Above the crossover `erfc` of a positive
# argument keeps its relative accuracy; at and below it the asymptotic series takes over,
# truncated after `-15/z**6`. The two agree to 10 significant digits at -30, -32 and -34.
LOG_PHI_CROSSOVER = -35


def log_phi_erfc_branch(z):
    """`log(0.5 * erfc(-z / sqrt(2)))`: `log Phi(z)` for `z > LOG_PHI_CROSSOVER`."""
    return math.log(0.5 * math.erfc(-z / math.sqrt(2)))


def log_phi_asymptotic_branch(z):
    """The asymptotic series for `log Phi(z)`, for `z <= LOG_PHI_CROSSOVER`."""
    return (-0.5 * z * z - 0.5 * math.log(2 * math.pi) - math.log(-z)
            + math.log1p(-1 / z ** 2 + 3 / z ** 4 - 15 / z ** 6))


def log_phi(z):
    """`log Phi(z)`, finite at every finite `z`: the branch TZ-10b section 5.2 selects."""
    if z > LOG_PHI_CROSSOVER:
        return log_phi_erfc_branch(z)
    return log_phi_asymptotic_branch(z)


# ---- TZ-11a section 5.1: the Student link, and the domain it is priced on -------------

# `Phi` is not the law of the settlement residual (TZ-10b), and a Student's `t` with a measured
# `nu(tau)` is the replacement TZ-11a scores. Its CDF is the regularized incomplete beta,
# `F_nu(z) = I_x(nu/2, 1/2) / 2` with `x = nu / (nu + z*z)` for `z <= 0`, and the leading factor
# of `I_x` is taken in logs: `log_betainc_reg` never forms a probability it then has to take
# the log of, so the far tail stays finite where `phi` returns exactly 0.0. `phi`, `log_phi` and
# `p_fair` are not touched - they are the old link, and every committed score is quoted from
# them.
LOG_BETA_CF_MAX = 300          # continued-fraction iterations before raising
LOG_BETA_TOL = 1e-16           # its relative convergence tolerance


def log_beta(a, b):
    """`log B(a, b) = lgamma(a) + lgamma(b) - lgamma(a + b)`."""
    return math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b)


def _betacf(a, b, x):
    """The continued fraction for `I_x(a, b)`, by the modified Lentz method.

    Raises rather than returning an unconverged value when `LOG_BETA_CF_MAX` iterations do not
    bring a step within `LOG_BETA_TOL` of one.
    """
    tiny = 1e-300
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < tiny:
        d = tiny
    d = 1.0 / d
    h = d
    for m in range(1, LOG_BETA_CF_MAX + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < tiny:
            d = tiny
        c = 1.0 + aa / c
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < tiny:
            d = tiny
        c = 1.0 + aa / c
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < LOG_BETA_TOL:
            return h
    raise ArithmeticError("the continued fraction for I_x(%r, %r) at x = %r did not converge "
                          "in %d iterations" % (a, b, x, LOG_BETA_CF_MAX))


def log_betainc_reg(a, b, x):
    """`log I_x(a, b)`, the log of the regularized incomplete beta function.

    Below the mean-like split `(a + 1) / (a + b + 2)` the continued fraction converges fast and
    is used directly; above it the symmetry `I_x(a, b) = 1 - I_{1-x}(b, a)` is taken.
    """
    if x >= 1:
        return 0.0
    if x <= 0:
        raise ValueError("log I_x(a, b) needs x > 0, got %r" % (x,))
    if x < (a + 1) / (a + b + 2):
        return (a * math.log(x) + b * math.log1p(-x) - math.log(a) - log_beta(a, b)
                + math.log(_betacf(a, b, x)))
    return math.log1p(-math.exp(log_betainc_reg(b, a, 1 - x)))


def log_t_cdf(z, nu):
    """`log F_nu(z)`, the log CDF of Student's `t` with `nu` degrees of freedom."""
    if z <= 0:
        return log_betainc_reg(nu / 2, 0.5, nu / (nu + z * z)) - math.log(2)
    return math.log1p(-math.exp(log_t_cdf(-z, nu)))


def t_cdf(z, nu):
    """`F_nu(z)`."""
    return math.exp(log_t_cdf(z, nu))


# TZ-11a sections 3.1 and 3.2, measured on the TZ-06 400 alone and on nothing else, from the
# feed and the manifests - no label was read to produce any of them. `ADMIT[tau]` is the 30th
# percentile of `sigma_hat` over those 400 at that tau: the Student pricer quotes only where the
# causal `sigma_hat` is at or above it. `LINK_NU` and `LINK_SCALE` are the maximum-likelihood
# `nu` and `s` of a symmetric Student's `t` fitted to `r = Y / (sigma * sqrt(H(tau)))` over
# every admissible anchor of the admissible members. Six significant digits each.
#
# These are **literals, not a fit performed at run time**, for the reason `SD_SCALE` is: a pricer
# that re-derives its constants from the data it is pointed at cannot be tested out of sample.
# The keys are every tau the pricer serves, `10` included, and an unmeasured tau raises.
ADMIT = {240: D("2.12324"), 180: D("2.14298"), 120: D("2.18062"), 90: D("2.16098"),
         60: D("2.16725"), 30: D("2.15178"), 10: D("2.14530")}
LINK_NU = {240: D("9.62070"), 180: D("13.7083"), 120: D("20.2258"), 90: D("16.0482"),
           60: D("9.51490"), 30: D("4.79579"), 10: D("2.13489")}
LINK_SCALE = {240: D("1.30678"), 180: D("1.36658"), 120: D("1.40748"), 90: D("1.37085"),
              60: D("1.27997"), 30: D("1.08185"), 10: D("0.643873")}


def student_sd(tau, sigma):
    """TZ-11a section 3.4's `sd_t`: the same horizon, at the scale of the fitted Student law.

        sd_t = LINK_SCALE[tau] * sigma * sqrt(H(tau)),   H as `corrected_sd` has it

    `sigma` is `realised_sigma` over the causal window, exactly as `corrected_sd` receives it.
    """
    assert tau in LINK_SCALE, "tau = %s has no measured Student scale; TZ-11a measured %s" % (
        tau, sorted(LINK_SCALE))
    if tau < SETTLEMENT_S:
        h = D(tau) ** 3 / D(TAU_CUBED_DIVISOR)
    else:
        h = D(tau - 40)
    return LINK_SCALE[tau] * sigma * h.sqrt()


def p_fair_student(state, sd, tau):
    """`F_nu(state / sd)` at `nu = LINK_NU[tau]`. The division is the last Decimal operation."""
    assert tau in LINK_NU, "tau = %s has no measured degrees of freedom; TZ-11a measured %s" % (
        tau, sorted(LINK_NU))
    return t_cdf(float(state / sd), float(LINK_NU[tau]))


def far_branch(tau, s_t, k, sigma):
    """TZ-06 section 3, `tau >= 60`.

        state = S_t - K
        sd    = sigma * sqrt(tau - 40)

    The running average of the interval has weight zero here: the settlement window is the
    last 60 seconds and nothing before it enters.
    """
    return s_t - k, sigma * D(tau - 40).sqrt()


# `tau**1.5 / (60 * sqrt(3))` is `sqrt(tau**3 / 10800)`, because `60 * sqrt(3) = sqrt(10800)`.
# The second form is the one implemented, for one reason: section 3 states that the branches
# meet at `tau = 60`, both giving `sd = sigma * sqrt(20)`. Written as `sqrt(tau**3 / 10800)`
# that identity holds exactly - `216000 / 10800` is exactly `20` - where the literal form
# rounds three times and lands one unit in the last place of the 60-digit context away from
# the far branch. The formula is unchanged; only its factoring is.
TAU_CUBED_DIVISOR = 10800


def near_branch(tau, s_t, k, sigma, m_r):
    """TZ-06 section 3, `tau < 60`.

        state = ((60 - tau) * m_r + tau * S_t) / 60 - K
        sd    = sigma * tau**1.5 / (60 * sqrt(3))
    """
    state = (D(SETTLEMENT_S - tau) * m_r + D(tau) * s_t) / D(SETTLEMENT_S) - k
    sd = sigma * (D(tau) ** 3 / D(TAU_CUBED_DIVISOR)).sqrt()
    return state, sd


def state_and_sd(tau, s_t, k, sigma, m_r=None):
    """The branch TZ-06 section 3 selects at `tau`. The two meet at `tau = 60`."""
    if tau >= SETTLEMENT_S:
        return far_branch(tau, s_t, k, sigma)
    assert m_r is not None, "tau = %s is the near branch and needs the realised mean" % (tau,)
    return near_branch(tau, s_t, k, sigma, m_r)


def p_fair(state, sd):
    """`Phi(state / sd)`. The division is the last Decimal operation."""
    assert sd > 0, "sd must be positive, got %s" % (sd,)
    return phi(float(state / sd))


# ---- TZ-07b section 5: the measured scale of the settlement quantity --------------

# TZ-07b M1, measured over the same 400 TZ-06 members: the dispersion of the exact random
# variable this `sd` describes, and of nothing else. At `tau >= 60` that variable is the
# feed's mean over the last sixty seconds minus the reading in force now - a lead of
# `tau - 60` seconds plus a sixty-second average - and below 60 it is the future part of that
# average carrying the weight the model gives it. `SD_SCALE[tau]` is the root mean square of
# `Y / (sigma * sqrt(H(tau)))` pooled over every admissible anchor of every member, to six
# significant digits.
#
# It replaces TZ-07a's `G_RATIO`, which was measured correctly and composed wrongly: `g(h)` is
# the dispersion of a single increment over lag `h`, so multiplying the whole of `tau - 40` by
# `g(tau - 40)` scaled the averaging part of the horizon by a ratio belonging to the lead part
# alone. The superseded table is not kept alongside this one - a superseded constant left in
# the pricer is a trap for whoever reads it next - and `c44af68` holds it in history.
#
# These are **literals, not a fit performed at run time**. A pricer that re-derives its
# constants from whatever data it is pointed at cannot be tested out of sample, and TZ-08
# scores this file as it stands here. Changing a value is a new TZ and a new map revision.
#
# The keys are every `tau` the pricer serves, `10` included: every tau a gate scores carries a
# measured constant, and nothing is ever extrapolated to one that does not.
SD_SCALE = {240: D("1.52376"), 180: D("1.49602"), 120: D("1.49628"), 90: D("1.47915"),
            60: D("1.44466"), 30: D("1.38581"), 10: D("1.21118")}


def corrected_sd(tau, sigma):
    """TZ-07b section 5's `sd`: the same model, at the scale its own residual was measured at.

        sd = SD_SCALE[tau] * sigma * sqrt(H(tau))

        H(tau) = tau - 40            for tau >= 60
        H(tau) = tau**3 / 10800      for tau <  60          # H(60) = 20 on both branches

    The CANON section 1.2 formula is not modified and neither is `sigma`: `realised_sigma`
    over the causal window `[T0 - 300, T0 + t]` is the input here exactly as it is to
    `state_and_sd`, `state` is untouched on both branches, and `H` is the horizon those
    branches already use. Only the constant multiplying the product changes.
    """
    assert tau in SD_SCALE, "tau = %s has no measured scale; TZ-07b measured %s" % (
        tau, sorted(SD_SCALE))
    if tau < SETTLEMENT_S:
        h = D(tau) ** 3 / D(TAU_CUBED_DIVISOR)
    else:
        h = D(tau - 40)
    return SD_SCALE[tau] * sigma * h.sqrt()


# ---- the quantities the model is fed --------------------------------------------

def merged_stream(t0, name):
    """One stream over `[T0 - 390, T0 + 330]`: the preceding directory's reports and this one's.

    TZ-06 section 3: the run-up window `[T0 - 300, T0]` is read from the **preceding**
    interval's directory, whose own window extends to `T0 + 30`. Where both directories cover
    an instant they carry the same feed, so the two are merged by timestamp and duplicates -
    identical `(timestamp, value)` pairs - are dropped. A timestamp carrying two different
    values is two reports of the feed, not a duplicate, and both are kept; the sort is stable,
    so the order is the on-disk order and the result is deterministic.

    This is a merge of one feed's own reports, never a fill: a report that never arrived is
    not invented here or anywhere else.
    """
    rows = reports(t0 - config.INTERVAL_S, name) + reports(t0, name)
    seen, out = set(), []
    for row in rows:
        if row in seen:
            continue
        seen.add(row)
        out.append(row)
    out.sort(key=lambda r: r[0])
    return out


def price_to_beat(t0, s1_rows):
    """`K`: the first `twap60` report with `timestamp >= T0 * 1000`.

    Read from the interval's own `twap60.jsonl.gz`, whose window opens at `T0 - 90`. Section 3
    sends only the run-up window to the preceding directory, and `K` is not in it.
    """
    return first_at_or_after(s1_rows, t0 * MS)


def time_weighted_mean(rows, a_ms, b_ms):
    """The time-weighted mean of the step function `rows` over `[a_ms, b_ms]`.

    A step function between two reports is what an event feed's price **is** between them, so
    integrating it is a reading, not a fill. The seed is the last report at or before `a_ms`,
    as section 3 requires, and the mean is `None` when there is none - a value the feed never
    published is never invented. A report timestamped at `b_ms` bounds the window and carries
    no width, so it cannot change the answer.
    """
    assert b_ms > a_ms, "an empty window has no mean: [%d, %d]" % (a_ms, b_ms)
    value = last_at_or_before(rows, a_ms)
    if value is None:
        return None
    total, cursor = D(0), a_ms
    for ts, nxt in rows:
        if ts <= a_ms:
            continue
        if ts >= b_ms:
            break
        total += value * D(ts - cursor)
        cursor, value = ts, nxt
    total += value * D(b_ms - cursor)
    return total / D(b_ms - a_ms)


def second_grid(rows, first_s, last_s):
    """The step function `rows` sampled on the one-second grid `[first_s, last_s]`, inclusive.

    The sample at second `s` is the reading in force at `s`: the last report at or before it.
    Seconds before the first report sample as `None`; `realised_sigma` refuses such a grid
    rather than treating the hole as a price.
    """
    out, idx, value, n = [], 0, None, len(rows)
    for second in range(first_s, last_s + 1):
        ts = second * MS
        while idx < n and rows[idx][0] <= ts:
            value = rows[idx][1]
            idx += 1
        out.append(value)
    return out


def realised_sigma(grid):
    """`sqrt(sum(d^2) / n)` over the first differences of a one-second grid: dollars per second.

    `sigma_live` and `sigma_pre` differ only in the grid handed in, so this is the one
    estimator behind both. A grid is a prefix of a longer grid whenever its window is, which
    is what makes `sigma_live` causal: extending the window forward cannot change an earlier
    value.
    """
    n = len(grid) - 1
    assert n > 0, "a grid of %d points has no first differences" % len(grid)
    assert all(v is not None for v in grid), "the grid opens before the first report"
    total = D(0)
    for i in range(n):
        d = grid[i + 1] - grid[i]
        total += d * d
    return (total / D(n)).sqrt()


def settlement_mean(t0, s3_rows, t=config.INTERVAL_S):
    """The trailing 60-second average at `T0 + t`, over `[T0 + 240, T0 + t]`.

    This is `m_r` when `t < 300`, and TZ-06 section 6's P reconstruction when `t = 300`. One
    function, because they are one quantity read at two instants.
    """
    return time_weighted_mean(s3_rows, (t0 + config.INTERVAL_S - SETTLEMENT_S) * MS,
                              (t0 + t) * MS)


def observations(t0, s1_rows, s3_rows, taus=TAUS):
    """Every scored observation for one interval, priced from the two streams handed in.

    `s1_rows` is the interval's own `twap60` stream, which supplies `K` alone. `s3_rows` is
    the merged `chainlink` stream of section 3. Both arrive as arguments rather than being
    read in here, which is what makes the V4 perturbation test possible: the test hands in a
    perturbed copy of a stream and nothing else about the call changes.

    `sigma_live` reads `[T0 - 300, T0 + t]` and `sigma_pre` reads `[T0 - 300, T0]`, so the
    second is a prefix of the first and one grid serves every checkpoint.
    """
    k = price_to_beat(t0, s1_rows)
    assert k is not None, "interval %d has no twap60 report at or after the open" % t0
    last_t = max(config.INTERVAL_S - tau for tau in taus)
    grid = second_grid(s3_rows, t0 - RUNUP_S, t0 + last_t)
    sigma_pre = realised_sigma(grid[:RUNUP_S + 1])
    out = []
    for tau in taus:
        t = config.INTERVAL_S - tau
        s_t = last_at_or_before(s3_rows, (t0 + t) * MS)
        assert s_t is not None, "interval %d has no chainlink report at or before T0+%d" % (t0, t)
        m_r = settlement_mean(t0, s3_rows, t) if tau < SETTLEMENT_S else None
        sigma_live = realised_sigma(grid[:RUNUP_S + t + 1])
        state, sd = state_and_sd(tau, s_t, k, sigma_live, m_r)
        _, sd_pre = state_and_sd(tau, s_t, k, sigma_pre, m_r)
        out.append({"T0": t0, "tau": tau, "t": t, "K": k, "S_t": s_t, "m_r": m_r,
                    "sigma_live": sigma_live, "sigma_pre": sigma_pre, "state": state,
                    "sd": sd, "sd_pre": sd_pre,
                    "p_fair": p_fair(state, sd), "p_fair_pre": p_fair(state, sd_pre)})
    return out
