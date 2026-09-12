# TZ-07a — the oracle feed's variance–time curve, the corrected sigma, and the maker programme's own numbers

**Canonical filename:** `TZ-07a-variance-time.md` — the Executor names the committed file from
this line and from no other source.

| item | value |
|---|---|
| destination | `CryptoTZ/TZ-07a-variance-time.md` |
| replaces | **TZ-07**, which was BLOCKED at its fingerprint gate because `SYSTEM-MAP.md` on `main` was not the map, and did no other work. Its report stays where it is and is never edited; this TZ uses its own report path. |
| report | `CryptoReports/TZ-07a-variance-time-report.md` → straight to `main` |
| code | `research/tz07a-variance-time.py` (new) → branch `tz-07a-variance-time`, from `main` → PR. **Never straight to `main`.** |
| authorized frozen-row changes | `research/pfair.py` and `research/selftest-pfair.py`, **additive only**, under §3 and §4. No other frozen row may move, and the report states the new hash of each. |
| Executor model | **Opus** — the pricer, causality and gate arithmetic |

## 0. Fingerprint gate

| anchor | required value |
|---|---|
| System Map revision | `2026-09-12-c` |
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-open / 2-not-started` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` |
| `A6` — pricer | `18be5d185fee` |

**Host gate.** Reads the capture, so it executes on the capture host and nowhere else.

| check | required |
|---|---|
| `/var/lib/btc-recorder/` | exists, and holds interval directories |
| the recorder process | running, and the newest `runtime.jsonl` start record carries sha `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` |
| the filesystem holding that path | device `/dev/vda2`, total exactly `31,612,203,008` bytes |

Any mismatch → **BLOCKED** before any work, with the observed values reported and nothing else
done.

---

## 1. Why this TZ exists

TZ-06's gate passed. The Architect's audit of TZ-06's own tables then found what the gate was not
built to see: at `tau` 240 / 180 / 120 the pricer's `sd` is understated by a factor of about
**1.50 / 1.36 / 1.30**, and at 90 / 60 / 30 by 1.08 / 1.04 / 0.93. The lowest bin realises about
three times the Up outcomes it predicts and the top bin fewer — a one-sided pattern in three
independent tables, not noise.

At `tau >= 60` the only estimated input is `sigma`: `K` is validated at 396 of 400 and `S_t` is a
direct read. So the error is in `sigma`, and its shape says what kind: **it is measured on
one-second increments of a smoothed oracle feed and then extrapolated by `sqrt` out to 260
seconds.** One-second increments of an aggregated feed understate the diffusion, and the
understatement grows with the extrapolation distance — exactly the observed monotone pattern.

This TZ **measures** that curve instead of assuming it, and freezes the correction. It does not
score the pricer: the 400 intervals that produced the finding are burnt as a test set and can only
fit. **TZ-08 scores, out of sample, against the gate §8 fixes below — committed to git before the
intervals it will score have happened.**

§6 adds one cheap measurement that needs no new capture: **what the venue's maker programme
actually pays on this exact market**, read from the Gamma documents already on disk. It decides
whether the pricer's job is to find a taker signal or to keep a resting quote from being run over,
and it is free to answer today.

**The CANON §1.2 formula is not modified.** Only the estimator of `sigma` changes, from a
one-second reading extrapolated to a reading at the scale at which it is used.

## 2. Scope

Read-only over the capture. **No write under `/var/lib/btc-recorder/`.** Scratch and outputs live
under `/root/tz07-work/`.

**Not in scope; appearance in the diff or the report is grounds for rejection:**

- **any read of `quotes.jsonl.gz`** — Tier C is Phase 2, and its gate must still be written by
  someone who has seen no quote;
- **any calibration claim about the corrected pricer.** §5's in-sample tables are a fit
  diagnostic, are labelled so in the report, and support nothing;
- any edit to `research/tz06-calibration.py`, to any `research/recorder/` file, or to
  `research/twap-divergence.py`, `research/selftest-twap-divergence.py`,
  `research/tz02-distribution.py`;
- any non-additive change to `research/pfair.py`: `realised_sigma`, `far_branch`, `near_branch`,
  `state_and_sd` and `p_fair` keep their current behaviour byte-for-byte, because TZ-06 must stay
  reproducible;
- **any price-bearing field of `gamma.json`** — `bestBid`, `bestAsk`, `spread`, `outcomePrices`,
  `lastTradePrice` and anything like them. §6 reads that document by an explicit key list and by
  nothing else;
- any other market statistic, any order path, any file under `engine/`, any Release upload.

## 3. M1 — the variance–time curve

Measured over the **400 TZ-06 members**, `T0` `1789035000` … `1789166400`, formed by TZ-06 §4's
five qualifying conditions applied unchanged. The member list is re-derived, never transcribed.

For each member, build the one-second grid of the merged `chainlink` step function over
`[T0 - 300, T0 + 300]` — 601 points — with `pfair.second_grid` and `pfair.merged_stream`, both
unchanged.

**Lag grid, fixed here:** `h ∈ {1, 2, 5, 10, 20, 30, 50, 60, 80, 100, 140, 180, 200, 240, 300}`
seconds. It contains the five horizons the model actually uses.

For each `h`, take every overlapping increment `P(s + h) − P(s)` for `s = 0 … 600 − h`, and pool
across all 400 members:

```
sigma_h_squared = sum(dP^2) / (N_h * h)
g(h)            = sigma_h_squared / sigma_1_squared
```

**M6 — the disconnect rule, which resolves System Map §7 item 16.** A second is *excluded* when it
falls inside a disconnect event recorded in the manifest of the directory that supplies it —
either the member's own or its predecessor. **An increment whose closed span `[s, s + h]` contains
an excluded second is dropped and counted.** No value is carried across a gap the manifest
records. The report states, per `h`, the increments taken and the increments dropped.

**Reported twice.** The pooled `g(h)` above is the reading that feeds §4. The **median across
members of each member's own `g(h)`** is reported alongside as a robustness reading, with no
threshold and no role in the constants.

## 4. M2 — the correction, frozen as literals

The model's variance horizon is `tau - 40` on the far branch and `tau**3 / 10800` on the near one.
For the six gated taus the far-branch horizons are `h ∈ {200, 140, 80, 50, 20}` at
`tau ∈ {240, 180, 120, 90, 60}`.

Add to `research/pfair.py`, additively:

```
G_RATIO = {200: …, 140: …, 80: …, 50: …, 20: …}      # from M1, pooled, 6 significant digits
```

and a new function giving the corrected `sd`:

```
tau >= 60:   sd = sigma * sqrt((tau - 40) * G_RATIO[tau - 40])
tau <  60:   sd = sigma * sqrt(tau**3 / 10800)          # unchanged: G is exactly 1 here
```

`sigma` is `realised_sigma` over the causal window `[T0 - 300, T0 + t]`, unchanged.

**`G_RATIO` is a table of literals written into the file, never recomputed at run time.** A pricer
whose constants are re-fitted on whatever data it is pointed at is not a frozen pricer and cannot
be tested out of sample.

**`G` is fixed at exactly 1 below `tau = 60`**, decided here and not after the fact: the near
branch's horizon is 2.5 s at `tau = 30` and 0.09 s at `tau = 10`, at or below the feed's own 1 Hz
cadence, where no ratio is measurable — and the audit already puts the multiplier there within 7%
of 1.

## 5. M3 — in-sample diagnostics only

Recompute the TZ-06 calibration tables on the same 400 members with the corrected `sd`, and print
them beside the uncorrected ones: per gated tau, `Brier`, the ten bins, and `λ̂` as §7 defines it.

**Every one of these numbers is in-sample on the set that produced the finding.** The report says
so in the same sentence as the first of them, and says that they confirm nothing. Their only
purpose is to show the fit did what it was meant to do before the out-of-sample test is spent.

## 6. M4 — the maker programme's published terms, from what is already captured

The venue pays makers twice and this project has never looked: a maker fill carries no fee, the
measured `rebateRate` of `0.2` is a share of the taker's fee, and a separate liquidity-rewards
programme pays for resting orders near the midpoint **whether or not they ever fill**. Its
per-market terms are published in the Gamma market document — and the recorder has been capturing
that document as `gamma.json` at `T0 + 5` for every interval since 2026-09-10.

For each of the 400 TZ-06 members, extract from its `gamma.json` **exactly these keys and no
others**:

`conditionId` · `slug` · `rewards.rewardsMinSize` · `rewards.rewardsMaxSpread` ·
`rewards.clobRewards[].rewardsAmount` · `rewards.clobRewards[].rewardsDailyRate` ·
`rewards.clobRewards[].startDate` · `rewards.clobRewards[].endDate`

**Extraction is by explicit key list, never by dumping or scanning the document.** A key that is
absent is reported absent and nothing is inferred from its absence.

Report, as counts only: how many of the 400 carry a non-null `rewards` block; the distinct values
of `rewardsMinSize` and of `rewardsMaxSpread`, each with its count; and the distinct
`rewardsDailyRate` values with their date ranges.

**No threshold, no gate, no strategy conclusion.** This TZ reads the terms and stops. What is done
with them is the Architect's, and it is not decided here.

---

## 7. Validation

**Written by the Architect. The Executor runs these and does not design, extend or relax them.**
Every result is a count. **V1, V2, V3 or V4 failing is BLOCKED, not a finding.**

| # | check | reported as |
|---|---|---|
| V1 | the curve | `g(h)` at all fifteen lags, pooled and median, with `N_h` taken and dropped, and the member count |
| V2 | causality of the corrected pricer | the first 20 members × six gated taus: perturb every `chainlink` and `twap60` report timestamped after the checkpoint instant by `1.0001` and require the corrected `p_fair` bit-identical — 120 of 120; plus the negative control on the last readable report, which must move the model output — `state`, `sd`, `p_fair` — 120 of 120 |
| V3 | determinism | two full runs, every output byte-identical, by `cmp` |
| V4 | **regression** | `research/tz06-calibration.py` is unmodified and still reproduces TZ-06 §2.8's six `Brier(p_fair)` values to all six printed decimals, and TZ-06's P at 397 of 400 |
| V5 | self-tests | `research/selftest-pfair.py` passes whole; its existing 56 + 18 are unchanged, and the new checks include that below `tau = 60` the corrected `sd` equals the uncorrected `sd` **exactly**, and that at `tau = 60` the corrected `sd` is `sigma * sqrt(20 * G_RATIO[20])` |
| V6 | the disconnect rule | increments dropped, per lag and in total, and the count of members contributing at least one dropped increment |
| V7 | in-sample diagnostics | §5's tables, labelled in-sample, no threshold |
| V8 | **how much test data exists** | the count of interval directories on disk with `T0 > 1789166400`, and how many of them satisfy TZ-06 §4's five conditions, at the moment of the run |
| V9 | the maker terms | §6's counts, and the key list actually extracted |

V8 exists so the Architect knows when TZ-08 can be issued and does not have to ask.

## 8. The TZ-08 gate — fixed here, before the intervals it scores have happened

**TZ-08 repeats this section verbatim and changes nothing in it.** It is committed to git now so
that no threshold can move once a number exists.

**The set.** The first **400** intervals with `T0 > 1789166400` that satisfy TZ-06 §4's five
qualifying conditions, in `T0` order — disjoint from the TZ-06 set by construction. Every unit
considered is disclosed in order, members and non-members alike, with the reason for each
non-member. Fewer than 400 qualifying → **BLOCKED**; the set is never shrunk. `quotes_complete` is
not a condition and no quote is read.

**Scored taus** `{240, 180, 120, 90, 60, 30}`; `tau = 10` measured with no threshold. Predictions
are the corrected pricer with `sigma_live`.

- **G1 — discrimination.** At every gated tau, `Brier(p_fair) < Brier(c)`, `c` the observed Up
  rate over the 400.
- **G2 — shape.** Fixed bins `[0, 0.1), … [0.9, 1.0]`; a bin is eligible at `n >= 20`; a bin fails
  when its observed Up count falls outside the central 99% region of `Binomial(n, p̄)`, computed
  exactly in integer arithmetic. **Across the six taus, at most 2 eligible bins may fail.**
- **G3 — scale.** With `z = state / sd` from the observations file, `λ̂` maximises
  `sum( y*log Phi(z/λ) + (1-y)*log(1 - Phi(z/λ)) )` over `λ ∈ [0.5, 3.0]`, by ternary search to
  `1e-9`, per tau over the 400 observations at that tau. **Require `|λ̂ - 1| <= 0.15` at every
  gated tau.** The likelihood ratio `2(ll(λ̂) - ll(1))` and its `chi-square` one-degree p-value are
  reported with no threshold.

`0.15` is derived, not chosen: CANON §1.4 already fixes 10% as the scale at which sensitivity to a
`sigma` error peaks; `0.15` is one and a half times it, and still far inside the 30 to 50% errors
TZ-06 exhibited.

**Any one of G1, G2, G3 violated → Phase 1 answers no.** TZ-08 also reports all three statistics
for the **uncorrected** pricer on the same set, with no threshold, so the correction's effect is
measured rather than asserted.

Passing all three does not confirm an edge and licenses no engine work. Phase 2 remains the
decision point.

## 9. Deliverable

The report contains, and contains nothing else of substance:

1. the fingerprint table — `wc -l` and `sha256sum` for `SYSTEM-MAP.md` and every file the map's
   §0 table lists, plus the post-change hashes of the two files §0 authorizes;
2. the host gate's three observed values;
3. V1–V9 as counts, with the `G_RATIO` literals as written into the file;
4. the branch, the implementation commit and the pull request.

Publication is part of execution. **No calibration claim about the corrected pricer appears
anywhere in this report.**
