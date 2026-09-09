#!/usr/bin/env python3
"""TZ-01a - TWAP divergence measurement, corrected re-run.

Measures how often, and by how much, a TWAP-settled probability disagrees with an
endpoint-settled probability on real BTC price history.

Data source: data.binance.vision, public archive, spot BTCUSDT, 1-second klines.
No exchange keys, no order placement, no trading-venue API calls: this script reads
historical public price files and nothing else.

TZ-01a section 1 replaces TZ-01's definition of `S_t`.  At a checkpoint `t` seconds into
the interval the bars that have closed are `0 .. t-1`; TZ-01 read the close of bar `t`,
which happens one second later.  `compute_observation` now takes a single slice of the
interval and derives both `S_t` and `twap_so_far` from it.

Every formula of TZ-01 section 3 is implemented once, in `checkpoint_quantities`.  Two
readings call it: `compute_observation`, the corrected one used by the whole pipeline,
and `compute_observation_tz01_reading`, the defective one used by nothing except the
section 5 contamination measurement.
"""

import argparse
import calendar
import datetime as dt
import hashlib
import json
import math
import os
import shutil
import subprocess
import sys
import zipfile

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# --------------------------------------------------------------------------------------
# Constants - TZ-01 section 3
# --------------------------------------------------------------------------------------

INTERVAL_SECONDS = 300            # a Polymarket BTC 5-minute interval
CHECKPOINT_TAUS = (240, 180, 120, 90, 60)   # seconds remaining at each checkpoint
PRIOR_SECONDS = 1800              # history needed before an interval open (sigma_pre)
SIGMA_PRE_MINUTES = 30            # 1-minute bars used by sigma_pre
SIGMA_LIVE_PRE_SECONDS = 300      # 1-second bars before the open used by sigma_live
LABEL_CADENCES = (1, 30, 60)      # outcome_1s, outcome_30s, outcome_60s
MAX_MISSING_BARS = 5              # an interval missing more than this is skipped

BASE_URL = "https://data.binance.vision/data/spot/monthly/klines/BTCUSDT/1s"
SQRT_2 = math.sqrt(2.0)
SQRT_3 = math.sqrt(3.0)
SQRT_60 = math.sqrt(60.0)

# --------------------------------------------------------------------------------------
# Section 3 - the single implementation of every defined quantity
# --------------------------------------------------------------------------------------


def phi(x):
    """Standard normal CDF."""
    return 0.5 * math.erfc(-x / SQRT_2)


def normal_probability(numerator, scale):
    """Phi(numerator / scale), with the degenerate scale == 0 limit stated explicitly.

    A perfectly flat price path has zero volatility, so `scale` is zero and the ratio is
    undefined.  The limit of Phi(numerator / scale) as scale -> 0+ is used: 1.0 for a
    positive numerator, 0.0 for a negative one, and 0.5 when the numerator is also zero.
    Section 7.2's flat-path self-test relies on the 0/0 case being 0.5.
    """
    if scale > 0.0:
        return phi(numerator / scale)
    if numerator > 0.0:
        return 1.0
    if numerator < 0.0:
        return 0.0
    return 0.5


def sample_sd_of_log_returns(closes):
    """Sample standard deviation (ddof=1) of consecutive log returns of `closes`."""
    returns = np.diff(np.log(closes))
    if returns.size < 2:
        return 0.0
    return float(returns.std(ddof=1))


def checkpoint_quantities(K, tau, S_t, twap_so_far, prior_closes, live_closes):
    """Every section 3 formula, implemented once.

    This function reads no interval: the caller decides which bars are readable and hands
    over `S_t`, `twap_so_far` and the 1-second window `sigma_live` is measured over.  That
    is what lets the corrected reading of TZ-01a section 1 and the defective TZ-01 reading
    kept for section 5 share one implementation and differ only in which bars they read.
    """
    t = INTERVAL_SECONDS - tau
    naive_move = S_t - K
    state = t * (twap_so_far - K) + tau * naive_move

    # sigma_pre: 1-minute log returns over the 30 minutes strictly before the open.
    # prior_closes[j] is the price at (open - PRIOR_SECONDS + j); the close of minute k is
    # therefore prior_closes[60k + 59], giving 30 minute closes and 29 log returns.
    minute_closes = prior_closes[59::60]
    sigma_pre = K * sample_sd_of_log_returns(minute_closes) / SQRT_60
    sigma_live = K * sample_sd_of_log_returns(live_closes)

    tau_f = float(tau)
    observation = {
        "tau": tau,
        "t": t,
        "K": K,
        "S_t": S_t,
        "naive_move": naive_move,
        "twap_so_far": twap_so_far,
        "state": state,
        "sigma_pre": sigma_pre,
        "sigma_live": sigma_live,
    }
    for name, sigma_dollar in (("pre", sigma_pre), ("live", sigma_live)):
        sd_remaining = sigma_dollar * tau_f ** 1.5 / SQRT_3
        observation["sd_remaining_" + name] = sd_remaining
        observation["p_twap_" + name] = normal_probability(state, sd_remaining)
        observation["p_naive_" + name] = normal_probability(
            naive_move, sigma_dollar * math.sqrt(tau_f)
        )
    return observation


def check_checkpoint_inputs(prior_closes, interval_opens, interval_closes, tau, needed):
    """Shared argument checks; `needed` is the number of interval bars the caller reads."""
    if len(prior_closes) != PRIOR_SECONDS:
        raise ValueError("prior_closes must hold exactly %d bars" % PRIOR_SECONDS)
    if tau not in CHECKPOINT_TAUS:
        raise ValueError("tau %r is not a section 3 checkpoint" % (tau,))
    if len(interval_closes) < needed or len(interval_opens) < 1:
        raise ValueError("interval data does not reach the checkpoint at tau=%d" % tau)


def live_window(prior_closes, readable_closes):
    """The sigma_live window: five minutes of run-up plus the bars already closed."""
    return np.concatenate(
        (prior_closes[PRIOR_SECONDS - SIGMA_LIVE_PRE_SECONDS:], readable_closes)
    )


def compute_observation(prior_closes, interval_opens, interval_closes, tau):
    """Every section 3 quantity for one checkpoint, read causally - TZ-01a section 1.

    A 1-second bar with index `i` opens at `T0 + i` and closes at `T0 + i + 1`, so at the
    checkpoint instant `T0 + t` the bars that have closed are `0 .. t-1` and no others.
    `readable_closes` is exactly those bars, it is the only slice this function takes of
    `interval_closes`, and `S_t` and `twap_so_far` are both derived from it - one
    boundary, one slice.  `sigma_live` follows the same rule: its window ends at the last
    bar that has closed, which is bar `t-1`.

    A value timestamped `T0 + t` may be computed only from bars whose close timestamp is
    at or before `T0 + t`.  TZ-01a section 3's perturbation test is what proves this
    function obeys that rule; passing the full 300 bars and passing any truncation that
    still reaches bar `t-1` must give identical results.
    """
    t = INTERVAL_SECONDS - tau
    check_checkpoint_inputs(prior_closes, interval_opens, interval_closes, tau, t)

    readable_closes = interval_closes[:t]
    return checkpoint_quantities(
        K=float(interval_opens[0]),
        tau=tau,
        S_t=float(readable_closes[-1]),
        twap_so_far=float(readable_closes.mean()),
        prior_closes=prior_closes,
        live_closes=live_window(prior_closes, readable_closes),
    )


def compute_observation_tz01_reading(prior_closes, interval_opens, interval_closes, tau):
    """TZ-01's reading of the same checkpoint, kept only for section 5.

    This is the defect TZ-01a corrects, reproduced exactly as TZ-01 shipped it: `S_t` is
    the close of bar `t`, one second after the checkpoint, and `sigma_live` runs to the
    same bar.  `twap_so_far` is unchanged, which is what made the two boundaries in one
    function hard to see.  Nothing calls this except the contamination measurement.
    """
    t = INTERVAL_SECONDS - tau
    check_checkpoint_inputs(prior_closes, interval_opens, interval_closes, tau, t + 1)

    return checkpoint_quantities(
        K=float(interval_opens[0]),
        tau=tau,
        S_t=float(interval_closes[t]),
        twap_so_far=float(interval_closes[:t].mean()),
        prior_closes=prior_closes,
        live_closes=live_window(prior_closes, interval_closes[:t + 1]),
    )


def compute_labels(interval_closes, K):
    """The three outcome labels of section 3, from the full 300 bars of the interval.

    Sampling at cadence c takes the closes at elapsed marks 0, c, 2c, ... - 300 marks at
    1 s, 10 at 30 s, 5 at 60 s - and asks whether their mean is at or above the open.
    """
    if len(interval_closes) != INTERVAL_SECONDS:
        raise ValueError("labels need all %d bars of the interval" % INTERVAL_SECONDS)
    labels = {}
    for cadence in LABEL_CADENCES:
        sampled = interval_closes[::cadence]
        labels["twap_%ds" % cadence] = float(sampled.mean())
        labels["outcome_%ds" % cadence] = bool(float(sampled.mean()) >= K)
    return labels


# --------------------------------------------------------------------------------------
# Data - section 2
# --------------------------------------------------------------------------------------


def month_bounds(month):
    """(first second, first second of the next month) of `month`, as UTC epoch seconds."""
    year, mon = (int(part) for part in month.split("-"))
    start = calendar.timegm((year, mon, 1, 0, 0, 0))
    days = calendar.monthrange(year, mon)[1]
    return start, start + days * 86400


def previous_month(month):
    year, mon = (int(part) for part in month.split("-"))
    return "%04d-%02d" % ((year - 1, 12) if mon == 1 else (year, mon - 1))


def next_month(month):
    year, mon = (int(part) for part in month.split("-"))
    return "%04d-%02d" % ((year + 1, 1) if mon == 12 else (year, mon + 1))


def month_range(end_month, count):
    """The `count` months ending with `end_month`, oldest first."""
    months = [end_month]
    while len(months) < count:
        months.insert(0, previous_month(months[0]))
    return months


def default_end_month(today):
    """The last complete calendar month before `today`."""
    return previous_month("%04d-%02d" % (today.year, today.month))


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def download_month(month, work_dir):
    """Fetch one monthly archive and verify it against the published SHA-256."""
    os.makedirs(work_dir, exist_ok=True)
    name = "BTCUSDT-1s-%s.zip" % month
    zip_path = os.path.join(work_dir, name)
    if not os.path.exists(zip_path):
        subprocess.run(
            ["curl", "-sS", "--fail", "--retry", "3", "--max-time", "1800",
             "-o", zip_path, "%s/%s" % (BASE_URL, name)],
            check=True,
        )
    checksum_path = zip_path + ".CHECKSUM"
    if not os.path.exists(checksum_path):
        subprocess.run(
            ["curl", "-sS", "--fail", "--retry", "3", "--max-time", "120",
             "-o", checksum_path, "%s/%s.CHECKSUM" % (BASE_URL, name)],
            check=True,
        )
    with open(checksum_path) as handle:
        expected = handle.read().split()[0].strip().lower()
    actual = sha256_of(zip_path)
    if actual != expected:
        raise RuntimeError("checksum mismatch for %s: %s != %s" % (name, actual, expected))
    return zip_path, actual


def read_month_csv(zip_path):
    """Read one monthly archive into (epoch second, open, close) numpy arrays.

    Binance published these klines with millisecond open times until the end of 2024 and
    microsecond open times afterwards, and added a header row part way through the window;
    both are detected rather than assumed.
    """
    with zipfile.ZipFile(zip_path) as archive:
        member = archive.namelist()[0]
        with archive.open(member) as raw:
            first_line = raw.readline().decode("ascii", "replace")
        has_header = not first_line.split(",")[0].strip().isdigit()
        with archive.open(member) as raw:
            frame = pd.read_csv(
                raw,
                header=0 if has_header else None,
                usecols=[0, 1, 4],
                names=None if has_header else ["open_time", "open", "close"],
            )
    frame.columns = ["open_time", "open", "close"]
    open_time = frame["open_time"].to_numpy(dtype="int64")
    divisor = 1_000_000 if open_time[0] >= 10 ** 15 else 1_000
    seconds = open_time // divisor
    return seconds, frame["open"].to_numpy(dtype="float64"), frame["close"].to_numpy(dtype="float64")


def forward_fill(opens, closes, missing):
    """Forward-fill missing bars from the previous bar's close, in place.

    A filled bar has no trades of its own, so it carries the last known price: its open and
    its close are both the previous bar's close.
    """
    index = np.arange(closes.size)
    last_known = np.where(~missing, index, -1)
    np.maximum.accumulate(last_known, out=last_known)
    fillable = missing & (last_known >= 0)
    source = last_known[fillable]
    closes[fillable] = closes[source]
    opens[fillable] = closes[source]
    first_valid = int(index[~missing][0]) if (~missing).any() else closes.size
    return first_valid


def build_month_grid(month, zip_path, carry):
    """A gap-free per-second grid covering `month` plus PRIOR_SECONDS of run-up.

    Index 0 of the returned arrays is (month start - PRIOR_SECONDS).  `carry` is the tail
    handed over by the previous month, or None for the first month of the run.
    """
    start, end = month_bounds(month)
    grid_start = start - PRIOR_SECONDS
    size = end - grid_start
    opens = np.full(size, np.nan)
    closes = np.full(size, np.nan)
    missing = np.ones(size, dtype=bool)

    if carry is not None:
        if int(carry["grid_start"]) != grid_start:
            raise RuntimeError("carry tail does not abut %s" % month)
        opens[:PRIOR_SECONDS] = carry["opens"]
        closes[:PRIOR_SECONDS] = carry["closes"]
        missing[:PRIOR_SECONDS] = carry["missing"]

    seconds, raw_opens, raw_closes = read_month_csv(zip_path)
    position = seconds - grid_start
    inside = (position >= 0) & (position < size)
    position = position[inside]
    opens[position] = raw_opens[inside]
    closes[position] = raw_closes[inside]
    missing[position] = False

    raw_rows = int(inside.sum())
    missing_in_month = int(missing[PRIOR_SECONDS:].sum())
    first_valid = forward_fill(opens, closes, missing)
    carry_out = {
        "grid_start": end - PRIOR_SECONDS,
        "opens": opens[size - PRIOR_SECONDS:].copy(),
        "closes": closes[size - PRIOR_SECONDS:].copy(),
        "missing": missing[size - PRIOR_SECONDS:].copy(),
    }
    grid = {
        "month": month,
        "grid_start": grid_start,
        "month_start": start,
        "month_end": end,
        "opens": opens,
        "closes": closes,
        "missing": missing,
        "first_valid": first_valid,
        "raw_rows": raw_rows,
        "missing_in_month": missing_in_month,
    }
    return grid, carry_out


def iter_intervals(grid):
    """Yield (interval_open_ts, base index, missing count) for each 5-minute window."""
    count = (grid["month_end"] - grid["month_start"]) // INTERVAL_SECONDS
    for i in range(count):
        base = PRIOR_SECONDS + i * INTERVAL_SECONDS
        yield grid["month_start"] + i * INTERVAL_SECONDS, base, int(
            grid["missing"][base:base + INTERVAL_SECONDS].sum()
        )


def process_month(grid, observation_fn=compute_observation):
    """Every checkpoint observation of one month, plus that month's coverage counts.

    `observation_fn` is the corrected reading everywhere in the pipeline; section 5's
    contamination measurement is the only caller that passes anything else.
    """
    opens, closes, missing = grid["opens"], grid["closes"], grid["missing"]
    first_valid = grid["first_valid"]
    rows = []
    counts = {
        "intervals_found": 0,
        "intervals_skipped_gap": 0,
        "intervals_skipped_no_history": 0,
        "intervals_used": 0,
        "bars_forward_filled_in_intervals": 0,
        "intervals_with_filled_prior_window": 0,
        "observations": 0,
    }
    for open_ts, base, n_missing in iter_intervals(grid):
        counts["intervals_found"] += 1
        if n_missing > MAX_MISSING_BARS:
            counts["intervals_skipped_gap"] += 1
            continue
        if base - PRIOR_SECONDS < first_valid:
            counts["intervals_skipped_no_history"] += 1
            continue
        counts["intervals_used"] += 1
        counts["bars_forward_filled_in_intervals"] += n_missing

        prior_closes = closes[base - PRIOR_SECONDS:base]
        interval_opens = opens[base:base + INTERVAL_SECONDS]
        interval_closes = closes[base:base + INTERVAL_SECONDS]
        prior_filled = int(missing[base - PRIOR_SECONDS:base].sum())
        if prior_filled:
            counts["intervals_with_filled_prior_window"] += 1

        labels = compute_labels(interval_closes, float(interval_opens[0]))
        for tau in CHECKPOINT_TAUS:
            row = observation_fn(prior_closes, interval_opens, interval_closes, tau)
            row["interval_open_ts"] = open_ts
            row["month"] = grid["month"]
            row["n_missing_bars"] = n_missing
            row["prior_filled_bars"] = prior_filled
            row.update(labels)
            rows.append(row)
    counts["observations"] = len(rows)
    return rows, counts


OBSERVATION_COLUMNS = [
    ("interval_open_ts", "int64"), ("month", "object"), ("tau", "int16"), ("t", "int16"),
    ("K", "float64"), ("S_t", "float64"), ("naive_move", "float64"),
    ("twap_so_far", "float64"), ("state", "float64"),
    ("sigma_pre", "float64"), ("sigma_live", "float64"),
    ("sd_remaining_pre", "float64"), ("sd_remaining_live", "float64"),
    ("p_twap_pre", "float64"), ("p_naive_pre", "float64"),
    ("p_twap_live", "float64"), ("p_naive_live", "float64"),
    ("twap_1s", "float64"), ("twap_30s", "float64"), ("twap_60s", "float64"),
    ("outcome_1s", "bool"), ("outcome_30s", "bool"), ("outcome_60s", "bool"),
    ("n_missing_bars", "int16"), ("prior_filled_bars", "int16"),
]


def rows_to_frame(rows):
    frame = pd.DataFrame.from_records(rows, columns=[name for name, _ in OBSERVATION_COLUMNS])
    return frame.astype({name: dtype for name, dtype in OBSERVATION_COLUMNS if dtype != "object"})


PARQUET_COMPRESSION_LEVEL = 19


def write_parquet(frame, path):
    """Deterministic Parquet: same input frame in, byte-identical file out.

    Float columns carry almost all of the volume, so they are byte-stream-split before
    compression; that and the fixed zstd level are what keep the combined file small
    enough to live in the repository.
    """
    table = pa.Table.from_pandas(frame, preserve_index=False)
    encoding = {field.name: "BYTE_STREAM_SPLIT" for field in table.schema
                if pa.types.is_floating(field.type)}
    pq.write_table(table, path, compression="zstd",
                   compression_level=PARQUET_COMPRESSION_LEVEL, version="2.6",
                   column_encoding=encoding, use_dictionary=False, write_statistics=True)


# --------------------------------------------------------------------------------------
# Measurements - section 4
# --------------------------------------------------------------------------------------

VARIANTS = ("pre", "live")
MODELS = ("twap", "naive")
DISAGREEMENT_THRESHOLD = 0.15
GATE_A_THRESHOLD = 0.0015          # TZ-01a section 4
GATE_A_TAUS = (120, 180)           # the checkpoints the gate is counted at
BUCKET_WIDTH = 0.05
SPARSE_BUCKET = 200


def md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join(["---"] * len(headers)) + "|"]
    for row in rows:
        out.append("| " + " | ".join(str(cell) for cell in row) + " |")
    return "\n".join(out) + "\n"


def n(value):
    return format(int(value), ",")


def pct(count, total):
    return "n/a" if not total else "%.3f%%" % (100.0 * count / total)


def f4(value):
    return "n/a" if value is None or (isinstance(value, float) and math.isnan(value)) else "%.4f" % value


def disagreement_rows(frame, variant):
    gap = (frame["p_twap_" + variant] - frame["p_naive_" + variant]).abs()
    rows = []
    for tau in CHECKPOINT_TAUS + ("all",):
        mask = slice(None) if tau == "all" else (frame["tau"] == tau).to_numpy()
        sub = gap[mask]
        hit = int((sub >= DISAGREEMENT_THRESHOLD).sum())
        rows.append([tau, n(len(sub)), n(hit), pct(hit, len(sub)), f4(float(sub.mean())),
                     f4(float(sub.quantile(0.99)))])
    return rows


def inversion_masks(frame, variant):
    p_twap = frame["p_twap_" + variant]
    p_naive = frame["p_naive_" + variant]
    high = (p_naive >= 0.85) & (p_twap <= 0.60)
    low = (p_naive <= 0.15) & (p_twap >= 0.40)
    return high, low


def inversion_rows(frame, variant):
    high, low = inversion_masks(frame, variant)
    rows = []
    for tau in CHECKPOINT_TAUS + ("all",):
        mask = np.ones(len(frame), dtype=bool) if tau == "all" else (frame["tau"] == tau).to_numpy()
        total = int(mask.sum())
        n_high = int((high.to_numpy() & mask).sum())
        n_low = int((low.to_numpy() & mask).sum())
        rows.append([tau, n(total), n(n_high), pct(n_high, total), n(n_low), pct(n_low, total),
                     n(n_high + n_low), pct(n_high + n_low, total)])
    return rows


def calibration_rows(frame, variant, model, label):
    column = "p_%s_%s" % (model, variant)
    p = frame[column].to_numpy()
    y = frame[label].to_numpy().astype(float)
    bucket = np.clip((p / BUCKET_WIDTH).astype(int), 0, 19)
    rows = []
    for b in range(20):
        mask = bucket == b
        count = int(mask.sum())
        edge = "[%.2f, %.2f%s" % (b * BUCKET_WIDTH, (b + 1) * BUCKET_WIDTH, "]" if b == 19 else ")")
        if count == 0:
            rows.append([edge, "0", "n/a", "n/a", "fewer than %d" % SPARSE_BUCKET])
            continue
        rows.append([edge, n(count), f4(float(p[mask].mean())), f4(float(y[mask].mean())),
                     "fewer than %d" % SPARSE_BUCKET if count < SPARSE_BUCKET else ""])
    return rows


def brier(frame, variant, model, label):
    p = frame["p_%s_%s" % (model, variant)].to_numpy()
    y = frame[label].to_numpy().astype(float)
    return float(np.mean((p - y) ** 2)) if len(p) else float("nan")


def brier_rows(frame, variant, label):
    rows = []
    for tau in CHECKPOINT_TAUS + ("all",):
        sub = frame if tau == "all" else frame[frame["tau"] == tau]
        b_twap = brier(sub, variant, "twap", label)
        b_naive = brier(sub, variant, "naive", label)
        rows.append([tau, n(len(sub)), f4(b_twap), f4(b_naive), f4(b_naive - b_twap)])
    return rows


def inversion_cell_stats(frame, variant, label):
    """Realised frequency inside each inversion cell - measurement 5."""
    high, low = inversion_masks(frame, variant)
    stats = {}
    for name, mask in (("p_naive high / p_twap low", high),
                       ("p_naive low / p_twap high", low),
                       ("both cells", high | low)):
        sub = frame[mask.to_numpy()]
        if len(sub) == 0:
            stats[name] = {"n": 0, "mean_p_twap": float("nan"), "mean_p_naive": float("nan"),
                           "realised": float("nan"), "abs_error": float("nan")}
            continue
        mean_twap = float(sub["p_twap_" + variant].mean())
        realised = float(sub[label].to_numpy().astype(float).mean())
        stats[name] = {
            "n": len(sub),
            "mean_p_twap": mean_twap,
            "mean_p_naive": float(sub["p_naive_" + variant].mean()),
            "realised": realised,
            "abs_error": abs(realised - mean_twap),
        }
    return stats


def inversion_cell_rows(frame, variant, label):
    stats = inversion_cell_stats(frame, variant, label)
    return [[name, n(s["n"]), f4(s["mean_p_twap"]), f4(s["mean_p_naive"]), f4(s["realised"]),
             f4(s["abs_error"])] for name, s in stats.items()]


def observation_days(frame):
    """Distinct UTC calendar days covered by the intervals in `frame`."""
    return int(np.unique(frame["interval_open_ts"].to_numpy() // 86400).size)


def gate_a(frame, variant):
    """TZ-01a section 4 - directional inversions at tau in {120, 180}, at least 0.15%.

    The numerator is the inversion count of measurement 2 restricted to the two gate
    checkpoints.  TZ-01a section 4 writes the denominator as "all observations" while
    restricting the numerator to two of the five checkpoints, so both denominators are
    computed and both verdicts are reported; neither is adjusted.
    """
    high, low = inversion_masks(frame, variant)
    inverted = (high | low).to_numpy()
    tau_mask = frame["tau"].isin(GATE_A_TAUS).to_numpy()
    hit = int((inverted & tau_mask).sum())
    days = observation_days(frame)
    detail = {
        "hit": hit,
        "n_gate_taus": int(tau_mask.sum()),
        "n_all": int(len(frame)),
        "days": days,
        "per_day": (hit / days) if days else float("nan"),
        "per_tau": {},
    }
    for tau in GATE_A_TAUS:
        mask = (frame["tau"] == tau).to_numpy()
        total = int(mask.sum())
        n_hit = int((inverted & mask).sum())
        detail["per_tau"][tau] = {
            "n": total,
            "hit": n_hit,
            "rate": (n_hit / total) if total else float("nan"),
            "per_day": (n_hit / days) if days else float("nan"),
        }
    detail["rate_gate_taus"] = (hit / detail["n_gate_taus"]) if detail["n_gate_taus"] else float("nan")
    detail["rate_all"] = (hit / detail["n_all"]) if detail["n_all"] else float("nan")
    detail["passed_gate_taus"] = bool(detail["rate_gate_taus"] >= GATE_A_THRESHOLD)
    detail["passed_all"] = bool(detail["rate_all"] >= GATE_A_THRESHOLD)
    detail["passed"] = bool(detail["passed_all"])
    return detail


def gate_b(frame, variant, label):
    """Lower Brier for p_twap, and realised frequency within 0.05 of mean p_twap inside
    the inversion cells."""
    b_twap = brier(frame, variant, "twap", label)
    b_naive = brier(frame, variant, "naive", label)
    stats = inversion_cell_stats(frame, variant, label)["both cells"]
    brier_ok = b_twap < b_naive
    calib_ok = bool(stats["n"] > 0 and stats["abs_error"] <= 0.05)
    return {"brier_twap": b_twap, "brier_naive": b_naive, "brier_ok": brier_ok,
            "cells": stats, "calibration_ok": calib_ok,
            "passed": bool(brier_ok and calib_ok)}


def label_disagreement_rows(frame):
    """Pairwise disagreement between the three outcome labels, per interval."""
    intervals = frame.drop_duplicates(subset=["interval_open_ts"])
    rows = []
    total = len(intervals)
    for a, b in (("outcome_1s", "outcome_30s"), ("outcome_1s", "outcome_60s"),
                 ("outcome_30s", "outcome_60s")):
        disagree = int((intervals[a] != intervals[b]).sum())
        rows.append(["%s vs %s" % (a, b), n(total), n(disagree), pct(disagree, total)])
    return rows


def tercile_edges(frame):
    sigma = frame["sigma_pre"].to_numpy()
    return float(np.quantile(sigma, 1.0 / 3.0)), float(np.quantile(sigma, 2.0 / 3.0))


def tercile_slices(frame, low_edge, high_edge):
    sigma = frame["sigma_pre"].to_numpy()
    return [
        ("low tercile (sigma_pre < %.6f)" % low_edge, frame[sigma < low_edge]),
        ("mid tercile (%.6f <= sigma_pre < %.6f)" % (low_edge, high_edge),
         frame[(sigma >= low_edge) & (sigma < high_edge)]),
        ("high tercile (sigma_pre >= %.6f)" % high_edge, frame[sigma >= high_edge]),
    ]


def measurement_block(frame, variant, label, title, include_calibration):
    """Measurements 1 to 5 for one slice of the data under one sigma variant."""
    parts = ["#### %s\n" % title]
    parts.append("Measurement 1 - disagreement rate (|p_twap - p_naive| >= 0.15)\n")
    parts.append(md_table(["tau", "observations", "disagreements", "share", "mean gap",
                           "99th pct gap"], disagreement_rows(frame, variant)))
    parts.append("\nMeasurement 2 - inversion rate\n")
    parts.append(md_table(["tau", "observations", "p_naive>=0.85 & p_twap<=0.60", "share",
                           "p_naive<=0.15 & p_twap>=0.40", "share", "either", "share"],
                          inversion_rows(frame, variant)))
    if include_calibration:
        for model in MODELS:
            parts.append("\nMeasurement 3 - calibration of p_%s (label %s)\n" % (model, label))
            parts.append(md_table(["predicted bucket", "observations", "mean predicted",
                                   "realised frequency", "note"],
                                  calibration_rows(frame, variant, model, label)))
    parts.append("\nMeasurement 4 - Brier score (label %s)\n" % label)
    parts.append(md_table(["tau", "observations", "brier p_twap", "brier p_naive",
                           "naive minus twap"], brier_rows(frame, variant, label)))
    parts.append("\nMeasurement 5 - realised frequency inside the inversion cells (label %s)\n"
                 % label)
    parts.append(md_table(["cell", "observations", "mean p_twap", "mean p_naive",
                           "realised frequency", "|realised - mean p_twap|"],
                          inversion_cell_rows(frame, variant, label)))
    return "".join(parts)


def build_summary(frame, coverage, months, label="outcome_1s"):
    doc = ["# TZ-01a - TWAP divergence summary, corrected re-run\n",
           "\nGenerated by `research/twap-divergence.py`. Every observation is read under "
           "TZ-01a section 1: at a checkpoint `t` seconds in, the readable bars are "
           "`0 .. t-1`, and `S_t` and `twap_so_far` come from that one slice. Label for "
           "every measurement is `%s` unless a table says otherwise.\n" % label]

    processed = [m for m in months if m in coverage["months"]]
    doc.append("\n## Run\n\n")
    doc.append(md_table(["field", "value"], [
        ["window requested", "%s to %s (%d months)" % (months[0], months[-1], len(months))],
        ["months processed", "%s (%d of %d)" % (
            "%s to %s" % (processed[0], processed[-1]) if processed else "none",
            len(processed), len(months))],
        ["observations", n(len(frame))],
        ["intervals", n(frame["interval_open_ts"].nunique())],
        ["source", "data.binance.vision spot BTCUSDT 1s klines"],
        ["reading", "TZ-01a section 1 (S_t = interval_closes[t-1])"],
        ["days covered", n(observation_days(frame))],
    ]))

    doc.append("\n## Coverage counts (section 7.4)\n\n")
    totals = {k: 0 for k in ("raw_rows", "missing_in_month", "intervals_found",
                             "intervals_skipped_gap", "intervals_skipped_no_history",
                             "intervals_used", "bars_forward_filled_in_intervals",
                             "intervals_with_filled_prior_window", "observations")}
    rows = []
    for month in processed:
        c = coverage["months"][month]
        for key in totals:
            totals[key] += c[key]
        rows.append([month, n(c["raw_rows"]), n(c["intervals_found"]),
                     n(c["intervals_skipped_gap"]), n(c["intervals_skipped_no_history"]),
                     n(c["intervals_used"]), n(c["bars_forward_filled_in_intervals"]),
                     n(c["intervals_with_filled_prior_window"]), n(c["observations"])])
    rows.append(["total", n(totals["raw_rows"]), n(totals["intervals_found"]),
                 n(totals["intervals_skipped_gap"]), n(totals["intervals_skipped_no_history"]),
                 n(totals["intervals_used"]), n(totals["bars_forward_filled_in_intervals"]),
                 n(totals["intervals_with_filled_prior_window"]), n(totals["observations"])])
    doc.append(md_table(["month", "raw 1s bars", "intervals found", "skipped for gaps",
                         "skipped for missing history", "intervals used",
                         "bars forward-filled in used intervals",
                         "used intervals with a filled prior window",
                         "checkpoint observations"], rows))

    doc.append("\n## Outcome label cadence (section 3)\n\n")
    doc.append("Pairwise disagreement between the three settlement labels, one row per interval.\n\n")
    doc.append(md_table(["pair", "intervals", "disagreements", "share"],
                        label_disagreement_rows(frame)))

    for variant in VARIANTS:
        doc.append("\n## Measurements 1 to 5 under sigma_%s\n\n" % variant)
        doc.append(measurement_block(frame, variant, label, "All %s months" % len(processed), True))

    doc.append("\n## Measurement 6 - stability\n\n")
    half = len(months) // 2
    halves = [("first %d months (%s to %s)" % (half, months[0], months[half - 1]),
               frame[frame["month"].isin(months[:half])]),
              ("last %d months (%s to %s)" % (len(months) - half, months[half], months[-1]),
               frame[frame["month"].isin(months[half:])])]
    for variant in VARIANTS:
        doc.append("\n### sigma_%s\n\n" % variant)
        for title, sub in halves:
            if len(sub) == 0:
                doc.append("#### %s\n\nNo observations.\n" % title)
                continue
            doc.append(measurement_block(sub, variant, label, title, True))

    doc.append("\n## Measurement 7 - volatility regime split (terciles of sigma_pre)\n\n")
    low_edge, high_edge = tercile_edges(frame)
    doc.append("Tercile edges of `sigma_pre` in dollars per sqrt(second): %.6f and %.6f.\n"
               % (low_edge, high_edge))
    for variant in VARIANTS:
        doc.append("\n### sigma_%s\n\n" % variant)
        for title, sub in tercile_slices(frame, low_edge, high_edge):
            if len(sub) == 0:
                doc.append("#### %s\n\nNo observations.\n" % title)
                continue
            doc.append(measurement_block(sub, variant, label, title, False))

    doc.append("\n## Label sensitivity - the same numbers under outcome_60s\n\n")
    doc.append("Measurements 1 and 2 do not use the label and are unchanged. Measurements 4 "
               "and 5 under `outcome_60s`, with the `outcome_1s` value beside each.\n\n")
    rows = []
    for variant in VARIANTS:
        b1_twap = brier(frame, variant, "twap", "outcome_1s")
        b6_twap = brier(frame, variant, "twap", "outcome_60s")
        b1_naive = brier(frame, variant, "naive", "outcome_1s")
        b6_naive = brier(frame, variant, "naive", "outcome_60s")
        s1 = inversion_cell_stats(frame, variant, "outcome_1s")["both cells"]
        s6 = inversion_cell_stats(frame, variant, "outcome_60s")["both cells"]
        rows.append(["sigma_" + variant, "brier p_twap", f4(b1_twap), f4(b6_twap),
                     f4(b6_twap - b1_twap)])
        rows.append(["sigma_" + variant, "brier p_naive", f4(b1_naive), f4(b6_naive),
                     f4(b6_naive - b1_naive)])
        rows.append(["sigma_" + variant, "realised frequency in inversion cells",
                     f4(s1["realised"]), f4(s6["realised"]),
                     f4(s6["realised"] - s1["realised"])])
        rows.append(["sigma_" + variant, "|realised - mean p_twap| in inversion cells",
                     f4(s1["abs_error"]), f4(s6["abs_error"]),
                     f4(s6["abs_error"] - s1["abs_error"])])
    doc.append(md_table(["variant", "quantity", "under outcome_1s", "under outcome_60s",
                         "delta"], rows))
    doc.append("\nCalibration under `outcome_60s`, summarised as the mean absolute gap "
               "between predicted and realised frequency across populated buckets.\n\n")
    rows = []
    for variant in VARIANTS:
        for model in MODELS:
            gaps = {}
            for lab in ("outcome_1s", "outcome_60s"):
                table = calibration_rows(frame, variant, model, lab)
                diffs = [abs(float(r[2]) - float(r[3])) * int(r[1].replace(",", ""))
                         for r in table if r[1] != "0"]
                weights = [int(r[1].replace(",", "")) for r in table if r[1] != "0"]
                gaps[lab] = sum(diffs) / sum(weights) if weights else float("nan")
            rows.append(["sigma_" + variant, "p_" + model, f4(gaps["outcome_1s"]),
                         f4(gaps["outcome_60s"]),
                         f4(gaps["outcome_60s"] - gaps["outcome_1s"])])
    doc.append(md_table(["variant", "model", "under outcome_1s", "under outcome_60s", "delta"],
                        rows))

    doc.append("\n## Gates\n\n")
    doc.append("Gate A (TZ-01a section 4) - directional inversions at tau in {120, 180} "
               "are at least 0.15% of observations. An inversion is "
               "`p_naive >= 0.85 and p_twap <= 0.60` or `p_naive <= 0.15 and "
               "p_twap >= 0.40`.\n\n")
    rows = []
    for variant in VARIANTS:
        detail = gate_a(frame, variant)
        for tau in GATE_A_TAUS:
            d = detail["per_tau"][tau]
            rows.append(["sigma_" + variant, tau, n(d["n"]), n(d["hit"]),
                         pct(d["hit"], d["n"]), "%.3f" % d["per_day"], ""])
        rows.append(["sigma_" + variant, "both, / observations at those taus",
                     n(detail["n_gate_taus"]), n(detail["hit"]),
                     pct(detail["hit"], detail["n_gate_taus"]),
                     "%.3f" % detail["per_day"],
                     "PASS" if detail["passed_gate_taus"] else "FAIL"])
        rows.append(["sigma_" + variant, "both, / all observations",
                     n(detail["n_all"]), n(detail["hit"]),
                     pct(detail["hit"], detail["n_all"]),
                     "%.3f" % detail["per_day"],
                     "PASS" if detail["passed_all"] else "FAIL"])
    doc.append(md_table(["variant", "tau", "observations", "inversions", "rate",
                         "events per day", "verdict against 0.150%"], rows))
    doc.append("\nThe two denominators are both reported because TZ-01a section 4 counts "
               "the numerator at two of the five checkpoints and states the threshold "
               "against \"all observations\"; neither reading is adjusted. Events per day "
               "counts inversions at tau in {120, 180} over the %s distinct UTC days "
               "covered by the run.\n\n" % n(observation_days(frame)))
    doc.append("\nGate B - p_twap has a strictly lower Brier score than p_naive, and inside "
               "the inversion cells the realised frequency is within 0.05 of the mean "
               "p_twap of those cells.\n\n")
    rows = []
    for variant in VARIANTS:
        detail = gate_b(frame, variant, label)
        cells = detail["cells"]
        rows.append(["sigma_" + variant, f4(detail["brier_twap"]), f4(detail["brier_naive"]),
                     "PASS" if detail["brier_ok"] else "FAIL", n(cells["n"]),
                     f4(cells["mean_p_twap"]), f4(cells["realised"]), f4(cells["abs_error"]),
                     "PASS" if detail["calibration_ok"] else "FAIL",
                     "PASS" if detail["passed"] else "FAIL"])
    doc.append(md_table(["variant", "brier p_twap", "brier p_naive", "brier test",
                         "inversion cell observations", "mean p_twap", "realised frequency",
                         "absolute error", "calibration test", "gate B"], rows))
    return "".join(doc)


# --------------------------------------------------------------------------------------
# Driver - one month at a time, resumable
# --------------------------------------------------------------------------------------


def partition_path(out_dir, month):
    return os.path.join(out_dir, "partitions", "twap-divergence-%s.parquet" % month)


def carry_path(out_dir, month):
    """Carry tail holding the PRIOR_SECONDS bars immediately before `month` starts."""
    return os.path.join(out_dir, "state", "carry-%s.npz" % month)


def load_carry(out_dir, month):
    path = carry_path(out_dir, month)
    if not os.path.exists(path):
        return None
    with np.load(path) as data:
        return {"grid_start": int(data["grid_start"]), "opens": data["opens"],
                "closes": data["closes"], "missing": data["missing"]}


def save_carry(out_dir, month, carry):
    np.savez(carry_path(out_dir, month), grid_start=np.int64(carry["grid_start"]),
             opens=carry["opens"], closes=carry["closes"], missing=carry["missing"])


def coverage_path(out_dir):
    return os.path.join(out_dir, "state", "coverage.json")


def load_coverage(out_dir):
    path = coverage_path(out_dir)
    if os.path.exists(path):
        with open(path) as handle:
            return json.load(handle)
    return {"months": {}}


def save_coverage(out_dir, coverage):
    with open(coverage_path(out_dir), "w") as handle:
        json.dump(coverage, handle, indent=2, sort_keys=True)
        handle.write("\n")


def load_partitions(out_dir, months):
    frames = []
    for month in months:
        path = partition_path(out_dir, month)
        if os.path.exists(path):
            frames.append(pd.read_parquet(path))
    if not frames:
        return None
    return pd.concat(frames, ignore_index=True)


def refresh_outputs(out_dir, months, coverage):
    """Rewrite the combined Parquet and the summary from whatever partitions exist."""
    frame = load_partitions(out_dir, months)
    if frame is None:
        return None
    write_parquet(frame, os.path.join(out_dir, "twap-divergence-observations.parquet"))
    with open(os.path.join(out_dir, "twap-divergence-summary.md"), "w") as handle:
        handle.write(build_summary(frame, coverage, months))
    return frame


def collect(months, out_dir, work_dir, keep_raw=False):
    os.makedirs(os.path.join(out_dir, "partitions"), exist_ok=True)
    os.makedirs(os.path.join(out_dir, "state"), exist_ok=True)
    coverage = load_coverage(out_dir)
    for month in months:
        if month in coverage["months"] and os.path.exists(partition_path(out_dir, month)):
            print("[%s] already processed, skipping" % month, flush=True)
            continue
        print("[%s] downloading" % month, flush=True)
        zip_path, digest = download_month(month, work_dir)
        print("[%s] processing (sha256 %s)" % (month, digest[:16]), flush=True)
        grid, carry_out = build_month_grid(month, zip_path, load_carry(out_dir, month))
        rows, counts = process_month(grid)
        counts["raw_rows"] = grid["raw_rows"]
        counts["missing_in_month"] = grid["missing_in_month"]
        counts["archive_sha256"] = digest
        write_parquet(rows_to_frame(rows), partition_path(out_dir, month))
        save_carry(out_dir, next_month(month), carry_out)
        coverage["months"][month] = counts
        save_coverage(out_dir, coverage)
        refresh_outputs(out_dir, months, coverage)
        if not keep_raw:
            os.remove(zip_path)
        print("[%s] %s intervals used, %s observations, %s skipped for gaps"
              % (month, n(counts["intervals_used"]), n(counts["observations"]),
                 n(counts["intervals_skipped_gap"])), flush=True)
    return coverage


def rerun_month(month, out_dir, work_dir, destination):
    """Reprocess one month into `destination` without touching the run state.

    Used by the section 7.5 determinism check.
    """
    zip_path, _ = download_month(month, work_dir)
    grid, _ = build_month_grid(month, zip_path, load_carry(out_dir, month))
    rows, _ = process_month(grid)
    write_parquet(rows_to_frame(rows), destination)
    return destination



# --------------------------------------------------------------------------------------
# Contamination - TZ-01a section 5
# --------------------------------------------------------------------------------------

READINGS = (
    ("corrected", "TZ-01a section 1: S_t = interval_closes[t-1]", compute_observation),
    ("tz01", "TZ-01: S_t = interval_closes[t]", compute_observation_tz01_reading),
)


def build_contamination(month, frames, label="outcome_1s"):
    """Section 5 tables: one month of data read both ways."""
    doc = ["# TZ-01a section 5 - contamination measurement\n",
           "\nOne month, %s, with every observation computed twice: once under the "
           "corrected causal reading of TZ-01a section 1, once under TZ-01's reading. "
           "Nothing else differs - same bars, same intervals, same formulas. The label is "
           "`%s`.\n\n" % (month, label)]
    doc.append(md_table(["reading", "definition", "observations", "intervals"],
                        [[name, "`%s`" % text, n(len(frames[name])),
                          n(frames[name]["interval_open_ts"].nunique())]
                         for name, text, _ in READINGS]))

    doc.append("\n## Brier score by reading\n\n")
    rows = []
    for variant in VARIANTS:
        for model in MODELS:
            scores = {name: brier(frames[name], variant, model, label)
                      for name, _, _ in READINGS}
            rows.append(["sigma_" + variant, "p_" + model, f4(scores["corrected"]),
                         f4(scores["tz01"]), f4(scores["tz01"] - scores["corrected"])])
    doc.append(md_table(["variant", "model", "corrected", "TZ-01 reading",
                         "TZ-01 minus corrected"], rows))
    doc.append("\nA negative last column means the TZ-01 reading scored better - the "
               "value of one second of look-ahead, in Brier points.\n")

    doc.append("\n## Corrected Gate A inversion count by reading\n\n")
    rows = []
    for variant in VARIANTS:
        for name, _, _ in READINGS:
            d = gate_a(frames[name], variant)
            rows.append(["sigma_" + variant, name, n(d["hit"]),
                         pct(d["hit"], d["n_gate_taus"]), pct(d["hit"], d["n_all"]),
                         "%.3f" % d["per_day"]])
    doc.append(md_table(["variant", "reading", "inversions at tau in {120, 180}",
                         "rate over those taus", "rate over all observations",
                         "events per day"], rows))

    doc.append("\n## Realised frequency inside the inversion cells by reading\n\n")
    rows = []
    for variant in VARIANTS:
        for name, _, _ in READINGS:
            s = inversion_cell_stats(frames[name], variant, label)["both cells"]
            rows.append(["sigma_" + variant, name, n(s["n"]), f4(s["mean_p_twap"]),
                         f4(s["mean_p_naive"]), f4(s["realised"]), f4(s["abs_error"])])
    doc.append(md_table(["variant", "reading", "observations", "mean p_twap",
                         "mean p_naive", "realised frequency",
                         "|realised - mean p_twap|"], rows))

    doc.append("\n## Brier score by tau and reading\n\n")
    rows = []
    for variant in VARIANTS:
        for tau in CHECKPOINT_TAUS:
            cell = []
            for name, _, _ in READINGS:
                sub_frame = frames[name][frames[name]["tau"] == tau]
                cell.append(brier(sub_frame, variant, "twap", label))
                cell.append(brier(sub_frame, variant, "naive", label))
            rows.append(["sigma_" + variant, tau, f4(cell[0]), f4(cell[2]),
                         f4(cell[1]), f4(cell[3])])
    doc.append(md_table(["variant", "tau", "brier p_twap corrected",
                         "brier p_twap TZ-01", "brier p_naive corrected",
                         "brier p_naive TZ-01"], rows))
    return "".join(doc)


def contamination(month, out_dir, work_dir, keep_raw=False):
    """Reprocess one month under both readings and write the section 5 document."""
    zip_path, digest = download_month(month, work_dir)
    grid, _ = build_month_grid(month, zip_path, load_carry(out_dir, month))
    frames = {}
    for name, _, function in READINGS:
        rows, counts = process_month(grid, function)
        frames[name] = rows_to_frame(rows)
        print("[%s] %s reading: %s observations" % (month, name, n(len(rows))), flush=True)
    path = os.path.join(out_dir, "twap-divergence-contamination.md")
    with open(path, "w") as handle:
        handle.write(build_contamination(month, frames))
    if not keep_raw:
        os.remove(zip_path)
    return path, frames


def main(argv=None):
    today = dt.datetime.now(dt.timezone.utc).date()
    parser = argparse.ArgumentParser(description="TZ-01 TWAP divergence measurement")
    parser.add_argument("--stage",
                        choices=("collect", "summarize", "contaminate", "all"),
                        default="all")
    parser.add_argument("--end-month", default=default_end_month(today),
                        help="last complete calendar month of the window, YYYY-MM")
    parser.add_argument("--months", type=int, default=24, help="window length in months")
    parser.add_argument("--out-dir", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "out"))
    parser.add_argument("--work-dir", default=os.environ.get("TZ01_WORK_DIR", "/tmp/tz01-work"),
                        help="scratch space for raw archives, outside the repository")
    parser.add_argument("--keep-raw", action="store_true",
                        help="keep downloaded archives instead of deleting them")
    parser.add_argument("--contamination-month", default=None,
                        help="month for the section 5 contamination measurement, "
                             "default the last month of the window")
    parser.add_argument("--rerun-month", help="reprocess one month for the determinism check")
    parser.add_argument("--rerun-out", help="destination Parquet for --rerun-month")
    args = parser.parse_args(argv)

    months = month_range(args.end_month, args.months)
    os.makedirs(args.out_dir, exist_ok=True)

    if args.rerun_month:
        if not args.rerun_out:
            parser.error("--rerun-month requires --rerun-out")
        print(rerun_month(args.rerun_month, args.out_dir, args.work_dir, args.rerun_out))
        return 0

    coverage = load_coverage(args.out_dir)
    if args.stage in ("collect", "all"):
        coverage = collect(months, args.out_dir, args.work_dir, keep_raw=args.keep_raw)
    if args.stage in ("summarize", "all"):
        frame = refresh_outputs(args.out_dir, months, coverage)
        if frame is None:
            print("no partitions found", file=sys.stderr)
            return 1
        print("%s observations across %s intervals"
              % (n(len(frame)), n(frame["interval_open_ts"].nunique())))
    if args.stage in ("contaminate", "all"):
        path, _ = contamination(args.contamination_month or months[-1], args.out_dir,
                                args.work_dir, keep_raw=args.keep_raw)
        print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
