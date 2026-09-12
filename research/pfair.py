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


# ---- TZ-07a section 4: the measured variance-time correction ---------------------

# TZ-07a M1, measured over the 400 TZ-06 members: the oracle feed's variance does not grow
# linearly in the lag it is read at. `sigma` is estimated on one-second increments of a
# smoothed, aggregated feed, and one-second increments understate the diffusion; extrapolating
# them by `sqrt` out to 260 seconds understates it further, and by more the further it goes.
# `G_RATIO[h]` is `sigma_h^2 / sigma_1^2` at lag `h`, pooled over every overlapping increment
# of every member, to six significant digits.
#
# These are **literals, not a fit performed at run time**. A pricer that re-derives its
# constants from whatever data it is pointed at cannot be tested out of sample, and TZ-08
# scores this file as it stands here. Changing a value is a new TZ and a new map revision.
#
# The keys are the far branch's variance horizons `tau - 40` at the five gated taus at or
# above 60: `tau` 240 / 180 / 120 / 90 / 60.
G_RATIO = {200: D("2.18300"), 140: D("2.13471"), 80: D("2.06184"), 50: D("1.94691"),
           20: D("1.95609")}


def corrected_sd(tau, sigma):
    """TZ-07a section 4's `sd`: the same model, with `sigma` read at the scale it is used at.

        tau >= 60:   sd = sigma * sqrt((tau - 40) * G_RATIO[tau - 40])
        tau <  60:   sd = sigma * sqrt(tau**3 / 10800)

    The CANON section 1.2 formula is not modified and neither is `sigma`: `realised_sigma`
    over the causal window `[T0 - 300, T0 + t]` is the input here exactly as it is to
    `state_and_sd`. Only the horizon the one-second reading is carried to changes.

    Below `tau = 60` `G` is exactly 1, fixed by TZ-07a section 4 and not after the fact: the
    near branch's horizon is 2.5 s at `tau = 30` and 0.09 s at `tau = 10`, at or below the
    feed's own 1 Hz cadence, where no ratio is measurable. The near branch is therefore
    returned unchanged, and `selftest-pfair.py` asserts that it is the same value bit for bit.
    """
    if tau < SETTLEMENT_S:
        return sigma * (D(tau) ** 3 / D(TAU_CUBED_DIVISOR)).sqrt()
    horizon = tau - 40
    assert horizon in G_RATIO, \
        "tau = %s needs G_RATIO[%s]; TZ-07a measured %s" % (tau, horizon, sorted(G_RATIO))
    return sigma * (D(horizon) * G_RATIO[horizon]).sqrt()


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
