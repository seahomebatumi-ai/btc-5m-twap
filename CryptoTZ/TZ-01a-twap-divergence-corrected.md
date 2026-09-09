# TZ-01a — TWAP divergence measurement, corrected re-run

**Canonical filename: `TZ-01a-twap-divergence-corrected.md`** — commit the file under this
name in `CryptoTZ/`, regardless of the name it arrived with.

**Supersedes TZ-01.** TZ-01 executed correctly against its own text, but that text contained
a defect and its §7.3 causality test could not detect it. This TZ replaces §3's `S_t`
definition, §7.2's expectations for tests 3 and 4, §7.3 in full, and §5's Gate A. Everything
else in TZ-01 stands unchanged and is not restated here — read TZ-01 alongside this file.

**Repository:** `btc-5m-twap`. **Model: Opus.**

**Fingerprint gate: not applicable.** Still no System Map; it is authored after this report.

---

## 0. The defect

At a checkpoint with `t` seconds elapsed, TZ-01's expectations forced this implementation:

```
twap_so_far = mean(interval_closes[0:t])   # bars 0..t-1, last close at T0 + t
S_t         = interval_closes[t]           # bar t,       close at T0 + t + 1
```

The two ranges do not overlap, and non-overlap was reported as proof that no look-ahead
exists. **Non-overlap is not the test.** A 1-second bar with index `i` opens at `T0 + i` and
closes at `T0 + i + 1`. At the checkpoint instant `T0 + t`, bar `t` has not closed. Its close
is one second in the future.

`twap_so_far` therefore ends exactly at the checkpoint and `S_t` ends one second past it —
two different boundaries inside one function. The averaging side was right; the price side
reads the future.

The injected information is worth `sqrt(3/tau)` of a standard deviation in `state`: 0.158 at
`tau = 120`, 0.224 at `tau = 60`. It resolves `3/tau` of the remaining variance — 2.5% at
`tau = 120` — that a live system cannot have. It also favours `p_twap` over `p_naive` by a
factor of `sqrt(3)`, which means the Gate B margin is inflated in the direction that flatters
the model being tested. That is why this is re-run rather than reasoned about.

---

## 1. Corrected definition — replaces the corresponding lines of TZ-01 §3

At a checkpoint with `t` seconds elapsed and `tau = 300 - t` seconds remaining, the readable
bars are `0 .. t-1` and no others:

```
S_t         = interval_closes[t-1]         # last bar closed at or before T0 + t
twap_so_far = mean(interval_closes[0:t])   # the same t bars, unchanged
```

**Both quantities are computed from the identical slice `interval_closes[0:t]`.** One
boundary, one slice, no second index anywhere in `compute_observation`. Every other formula
in TZ-01 §3 is unchanged.

The general rule, which governs any future checkpoint quantity: **a value timestamped
`T0 + t` may be computed only from bars whose close timestamp is less than or equal to
`T0 + t`.**

---

## 2. Corrected self-tests — replaces TZ-01 §7.2 items 3 and 4

The step must land on bar `t-1`, not bar `t`, or the path is unobservable at the checkpoint.

- **Step-up path:** bars `0..178` at `K`, bars `179..299` at `K + 70`. At `tau = 120`:
  `twap_so_far == K + 70/180`, `S_t == K + 70`, **`state == 8470`** exactly.
- **Round-trip path:** bars `0..178` at `K + 40`, bars `179..299` at `K`. At `tau = 120`:
  `twap_so_far == K + 40*179/180`, `S_t == K`, **`state == 7160`** exactly, and
  `p_twap - p_naive > 0.10`.

Items 1 and 2 of TZ-01 §7.2 (flat path, linear ramp) are unchanged and must still pass.

These are fixed expectations, derived from the causal definition in §1. **If any of them is
unsatisfiable under a correct implementation, stop and file a BLOCKED report.** TZ-01 §0
item 3 required exactly this and it was not done; the reasoning offered instead was
articulate and wrong, and 24 months were collected under it. An unsatisfiable fixed
expectation is a defect in the specification and only the Architect may resolve it.

---

## 3. Causality test — replaces TZ-01 §7.3 in full

The truncation test is withdrawn. It cut the data at the same boundary the implementation
read from, so it could only ever confirm that the code agreed with itself. It returned 22 500
bit-identical comparisons on a pipeline that was reading the future.

**Perturbation test.** For a random sample of at least 500 intervals, at every checkpoint:

1. Compute every §3 quantity normally.
2. Take a copy of the interval and replace the close of **every bar with index `>= t`** with
   `close * 3.0`.
3. Recompute every §3 quantity from the perturbed copy.
4. Assert the two results are **bit-identical** on IEEE-754 bits for `naive_move`,
   `twap_so_far`, `state`, `sigma_pre`, `sigma_live`, `p_twap`, `p_naive`.

A perturbation cannot be satisfied by a boundary convention: if the code touches any bar at
or after the checkpoint, the value changes. Report the comparison count and the mismatch
count. **Any mismatch blocks the report.**

Additionally assert the negative control: perturbing bar `t-1` **does** change `S_t`,
`twap_so_far` and `state`. A test that passes on both the perturbed future and the perturbed
past is testing nothing.

---

## 4. Gate A — replaces TZ-01 §5 Gate A

The old Gate A counted `|p_twap - p_naive| >= 0.15`, which is dominated by the two models
scaling remaining variance differently (`tau**1.5` against `tau**0.5`). Most of what it
counted is the two models being confident in the **same** direction by different amounts.
That is not tradeable and the 37% it produced is not an opportunity rate.

**Gate A, corrected — directional inversions only.** Count observations where
`p_naive >= 0.85 and p_twap <= 0.60`, or `p_naive <= 0.15 and p_twap >= 0.40`, at
`tau` in `{120, 180}`. The gate passes at **0.15%** of all observations.

Report the inversion count as an absolute number and as events per day, alongside the
percentage. The per-day figure is what decides whether this is a business.

---

## 5. Contamination measurement — new, and the reason a re-run is worth its cost

For one month of data (the most recent complete month), compute every observation **twice**:
once under §1's corrected reading, once under TZ-01's reading (`S_t = interval_closes[t]`).

Report for that month, under both readings: Brier score for each model, the corrected Gate A
inversion count, and the realised frequency inside the inversion cells.

This measures what one second of look-ahead was worth. It is the empirical check on §0's
arithmetic and it tells the Architect how much of TZ-01's reported margin was a gift.

---

## 6. Scope, data and deliverables

Full 24-month re-run, same window and same source as TZ-01. Everything in TZ-01 §2, §4 and
§6 applies unchanged, except:

- **`research/out/**` is git-ignored and must not be committed** — not the partitions, not
  the combined Parquet. Add it to `.gitignore` in this branch. The summary Markdown is
  committed; the data is not, until the numbers are accepted.
- Add `research/out/twap-divergence-contamination.md` for §5, summary committed as above.
- Branch: `tz-01a-twap-divergence-corrected`. Report:
  `CryptoReports/TZ-01a-twap-divergence-corrected-report.md`, straight to `main`.

**The TZ-01 report is still missing from `main`.** Commit it there unchanged before starting
this work — it is the record of what was measured under the defective reading and it is not
rewritten, superseded or deleted. A report is immutable once committed and is not corrected
in place; TZ-01a's report supersedes it by reference, not by edit.

---

## 7. Validation

TZ-01 §7 items 1, 4, 5 and 6 unchanged. Item 2 as amended by §2 above. Item 3 replaced by §3
above. Additionally:

- Assert that `compute_observation` contains exactly one slice expression indexing
  `interval_closes` at a checkpoint, and that `S_t` and `twap_so_far` are both derived from
  it. State the line numbers in the report.
- Report the §5 contamination tables in full.

---

## 8. Report

`CryptoReports/TZ-01a-twap-divergence-corrected-report.md`, straight to `main`, same
requirements as TZ-01 §8, plus: the §5 contamination comparison, and a one-line statement of
whether the corrected Gate A and Gate B verdicts differ from TZ-01's.

Do not interpret the result or recommend a next step.
