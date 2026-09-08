# TZ-01 — TWAP divergence measurement (Phase 0)

**Canonical filename: `TZ-01-twap-divergence.md`** — commit the file under this name in
`CryptoTZ/`, regardless of the name it arrived with.

**Repository:** `btc-5m-twap` — a new, standalone project. It is NOT part of `crypto-auto`
and shares no code, data or configuration with it.

**Model: Opus.** Data volume, no-look-ahead discipline and a closed-form probability
model make this a correctness-critical task, not a mechanical edit.

**Fingerprint gate: not applicable to this TZ.** No System Map exists for this repository
yet. It will be authored by the Architect after this report, because a map written before
the first measurement would only record assumptions. From TZ-02 onward the normal gate
applies.

---

## 0. Operating rules for this repository

This repository has no `EXECUTOR-INSTRUCTIONS.md` yet, so the rules that apply to this TZ
are stated here and are binding.

1. **Branch, then report.** Implementation goes to a branch named `tz-01-twap-divergence`
   and a pull request. The report goes straight to `main`. Do not merge; the Architect's
   verdict comes first.
2. **English and clean Markdown** in every file, comment and report.
3. **No scope expansion.** If something in this TZ is impossible or contradictory, stop and
   write a BLOCKED report naming the contradiction. Do not improvise a substitute.
4. **No order placement, no exchange keys, no Polymarket API calls, no network access to
   any trading venue.** This phase reads historical public price files and nothing else.
5. **No second implementation of any formula.** Every quantity defined in §3 is computed in
   exactly one function, called from everywhere it is needed, including the self-tests.
6. **Report every number as a count.** "All intervals passed" is not a result; "104 218
   intervals processed, 137 skipped for gaps" is.

---

## 1. Purpose

Polymarket's BTC 5-minute Up/Down markets settle on the **time-weighted average price
(TWAP) of the whole interval, compared against the price at the interval open** — not on
the closing price. The published strategies for these markets read a different variable:
the *current* price minus the open.

Under TWAP settlement those two variables can point in opposite directions. This TZ
measures how often, and by how much, on real BTC price history.

**No trading logic, no model fitting, no parameter search is in scope.** This is one
measurement against two closed-form models.

---

## 2. Data

**Source:** `data.binance.vision`, public archive, spot `BTCUSDT`, **1-second klines**.

**Window:** the 24 calendar months ending with the last complete month before the run date.

**Processing:** one month at a time — download, process, append results, write the partial
summary, delete the raw file, continue. A run interrupted after month 9 must leave 9 months
of valid results on disk, not nothing.

**Why Binance and not the Chainlink oracle.** This phase measures a geometric property of
price paths — whether a running average and an endpoint disagree. That property does not
depend on which venue's feed is used. Settlement-accurate labelling from the oracle stream
is TZ-02's problem and is deliberately out of scope here. State this limitation in the
report; do not work around it.

**Intervals:** 5-minute windows aligned to UTC clock boundaries (`00:00:00`, `00:05:00`, …).

**Gap handling:** an interval missing more than 5 of its 300 one-second bars is skipped and
counted. Missing bars inside the tolerance are forward-filled from the previous bar. Report
both counts.

---

## 3. Quantities — one definition each

For an interval with open price `K` (the open of the first 1-second bar of the window) and
checkpoints at `tau ∈ {240, 180, 120, 90, 60}` seconds remaining, with `t = 300 - tau`
seconds elapsed and `S_t` the close of the last bar at or before the checkpoint:

```
naive_move    = S_t - K
twap_so_far   = mean(close of every bar in [0, t])
state         = t * (twap_so_far - K) + tau * (S_t - K)
sd_remaining  = sigma_dollar * tau**1.5 / sqrt(3)
p_twap        = Phi(state / sd_remaining)
p_naive       = Phi((S_t - K) / (sigma_dollar * sqrt(tau)))
```

`Phi` is the standard normal CDF. `state` is the expected total price-seconds above the
open; `sd_remaining` is the standard deviation of the not-yet-realised part of that
integral for driftless Brownian motion. `p_naive` is the model an endpoint-settled market
would use — it is the benchmark being tested, not a straw man, and it must be computed
exactly as written.

**Volatility, two variants, both reported separately:**

- `sigma_pre` — from 1-**minute** log returns over the 30 minutes strictly before the
  interval open, converted to dollars per sqrt(second) at price `K`.
- `sigma_live` — from 1-**second** log returns over the elapsed part of the interval plus
  the 5 minutes before it, up to and including the checkpoint bar and no further.

Every result in §4 is produced twice, once under each. Do not average them and do not pick
a winner in the code.

**Outcome label**, computed three ways to measure how much the oracle's sampling cadence
matters:

- `outcome_1s` — mean of all 300 one-second closes ≥ `K`
- `outcome_30s` — mean of the 10 closes at 30-second marks ≥ `K`
- `outcome_60s` — mean of the 5 closes at 60-second marks ≥ `K`

Report the pairwise disagreement counts between the three. This number decides how precise
TZ-02's oracle reconstruction has to be.

---

## 4. Measurements

Use `outcome_1s` as the label for everything below; report the deltas under `outcome_60s`
in a single table.

1. **Disagreement rate.** Count and percentage of checkpoint observations where
   `|p_twap - p_naive| >= 0.15`, broken out by `tau`.
2. **Inversion rate.** Count and percentage where `p_naive >= 0.85` and `p_twap <= 0.60`,
   and the mirror case (`p_naive <= 0.15` and `p_twap >= 0.40`), by `tau`.
3. **Calibration.** For each model, bucket observations by predicted probability in steps of
   0.05 and report bucket count and realised frequency. Buckets with fewer than 200
   observations are reported as such, not merged away.
4. **Brier score** for each model, overall and by `tau`.
5. **Realised frequency inside the inversion cells** from measurement 2 — the single number
   that says which model is telling the truth when they disagree.
6. **Stability.** Every number above, repeated separately for the first 12 months and the
   last 12 months.
7. **Volatility regime split.** Measurements 1, 2 and 4 split into terciles of `sigma_pre`.

---

## 5. Gates — both must be evaluated, neither may be adjusted

**Gate A — is there anything to trade?**
The disagreement rate (measurement 1) at `tau ∈ {120, 180}` is at least **3%** of
observations.

**Gate B — is the TWAP model correct?**
`p_twap` has a strictly lower Brier score than `p_naive`, AND inside the inversion cells the
realised frequency is within **±0.05** of the mean `p_twap` of those cells.

A failed gate is a valid and useful result. **Report the failure; do not tune anything to
make a gate pass.** Gate B failing means the Architect's probability model is wrong, which
is more valuable to know now than later.

---

## 6. Deliverables

| Path | Contents |
|---|---|
| `research/twap-divergence.py` | the measurement, single implementation of §3 |
| `research/selftest-twap-divergence.py` | the tests from §7 |
| `research/out/twap-divergence-observations.parquet` | one row per checkpoint observation, every field from §3 plus the labels |
| `research/out/twap-divergence-summary.md` | every table from §4, gate results from §5 |
| `CryptoReports/TZ-01-twap-divergence-report.md` | the report |

The Parquet file must permit full forensic reconstruction of any single observation without
re-running the pipeline. Include `interval_open_ts`, `tau`, `K`, `S_t`, `twap_so_far`,
`state`, both sigmas, both probabilities and all three labels.

---

## 7. Validation

Written by the Architect. Run these; do not design substitutes.

1. `python3 -m py_compile` on both scripts — clean.

2. **Analytic self-tests.** Construct synthetic 300-second paths and assert the computed
   values against hand-derived answers:
   - flat path at exactly `K` → `state == 0`, `p_twap == 0.5` at every checkpoint;
   - linear ramp from `K` to `K + 100` → `twap_so_far` equals `K + 50 * t / 300` at every
     checkpoint, to 1e-9;
   - path held at `K` for 180 s then stepped to `K + 70` → `state == 8400` at `tau = 120`;
   - path held at `K + 40` for 180 s then returned to `K` → `state == 7200` at `tau = 120`
     and `p_twap > p_naive` by more than 0.10.

   These are fixed expectations. A failing self-test is a defect in the implementation, not
   a stale expectation.

3. **Look-ahead truncation test — the decisive one.** For a random sample of at least 500
   intervals, compute every §3 quantity twice: once from the full interval, once from a copy
   of the data with every bar strictly after the checkpoint removed. Assert the two results
   are **bit-identical** for `naive_move`, `twap_so_far`, `state`, both sigmas and both
   probabilities. Any difference is look-ahead bias and blocks the report.

4. **Coverage counts.** Report: months processed, intervals found, intervals skipped for
   gaps, bars forward-filled, checkpoint observations written. Counts, not statements.

5. **Determinism.** Re-running one month twice produces a byte-identical Parquet partition.

6. **No-regression statement.** Explicit line confirming nothing outside `research/` and
   `CryptoReports/` was created or modified.

---

## 8. Report

`CryptoReports/TZ-01-twap-divergence-report.md`, straight to `main`. It must contain:

- line count and SHA-256 of every file created;
- the §7 validation results, each with its count;
- the §4 tables in full;
- both §5 gate verdicts, stated as PASS or FAIL with the number that decided each;
- anything that was impossible to implement as specified, named plainly.

Do not interpret the result or recommend a next step. The verdict is the Architect's.
