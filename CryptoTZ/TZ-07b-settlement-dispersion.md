# TZ-07b — the dispersion of the settlement quantity, measured directly, and the scale frozen from it

**Canonical filename:** `TZ-07b-settlement-dispersion.md` — the Executor names the committed file
from this line and from no other source.

| item | value |
|---|---|
| destination | `CryptoTZ/TZ-07b-settlement-dispersion.md` |
| replaces | nothing. TZ-07a executed, was accepted and is merged. This TZ **repairs the constants it froze**, which System Map §7 item 19 records as mis-composed. TZ-07a's report stays where it is and is never edited. |
| report | `CryptoReports/TZ-07b-settlement-dispersion-report.md` → straight to `main` |
| code | `research/tz07b-settlement-dispersion.py` (new) → branch `tz-07b-settlement-dispersion`, cut from `main` → PR. **Never straight to `main`.** |
| authorized frozen-row changes | `research/pfair.py`, `research/selftest-pfair.py` and `research/tz07a-variance-time.py`, **each only as §5 and §6 state, and this TZ is not additive-only**. No other frozen row may move, and the report states the new hash of each. |
| scratch and outputs | `/root/tz07b-work/`, outside the repository |
| Executor model | **Opus** — the pricer, causality and gate arithmetic |

## 0. Fingerprint gate

| anchor | required value |
|---|---|
| System Map revision | `2026-09-13-a` |
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-open / 2-not-started` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` |
| `A6` — pricer | `9bd4213a60a3` |

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

TZ-07a measured the oracle feed's variance–time curve correctly and froze a correction from it.
The measurement stands. **The composition does not.**

`g(h)` is the dispersion of a *single increment* over lag `h`. The quantity in the pricer's
denominator is not an increment. At `tau >= 60` the settlement value is the feed's mean over the
last 60 seconds, so the residual is a lead of `tau - 60` seconds **plus** a 60-second average,
and the model's horizon `tau - 40` is exactly `(tau - 60) + 20`, the `20` being the averaging
term. Multiplying the whole of `tau - 40` by `g(tau - 40)` scales the averaging part by a ratio
that belongs to the lead part alone. The error is small where the averaging term is a tenth of
the variance and total where it is all of it — which is precisely the observed pattern:
TZ-07a §2.5's own in-sample `λ̂` lands at 1.0301 / 0.9688 / 0.9846 at `tau` 240 / 180 / 120 and at
**0.8070 / 0.8128** at 90 / 60, against the `±0.15` its own §8 G3 requires at every gated tau.
Below `tau = 60` the residual is nothing but an average, `G` was fixed at exactly 1 with no
measurement, and G3 scores that tau too: `λ̂` 1.4027.

So the correction as frozen would fail its own gate at three of six taus **on the data it was fit
to**, and TZ-08 would spend the only out-of-sample set answering a question about the Architect's
substitution rather than about the model.

**The repair is to measure the exact random variable the constant divides, and nothing else.** It
needs no new capture, no label and no outcome: the residual is a functional of the oracle feed,
and the feed is on disk for the same closed 400 intervals.

---

## 2. Scope, and what this TZ may not touch

- **No outcome is read.** `resolution.json`, the venue's resolved documents, `priceToBeat` and
  every other settled field are out of scope. No `Brier`, no bin table, no `λ̂`, no calibration
  statistic of any kind appears in the report — including in-sample ones labelled as such.
- **No quote is read.** `quotes.jsonl.gz` is not opened; the string `quote` does not appear in the
  new file.
- **The CANON §1.2 model does not change.** `state`, `realised_sigma`, `far_branch`,
  `near_branch`, `state_and_sd` and `p_fair` are untouched, and the report proves it by diff.
  Only the constant multiplying `sd` in `corrected_sd` changes.
- **Nothing under `/var/lib/btc-recorder/` is written, moved or deleted.**
- One implementation of every formula: the merged stream, the one-second grid, the time-weighted
  step-function mean and the realised-sigma estimator are called from `research/pfair.py`. The
  new file carries none of its own, and the reader remains `analyze.reports`.

---

## 3. The set

TZ-06 §4's five qualifying conditions, **re-derived** by calling `tz06-calibration.scoring_set`,
never transcribed. The same closed 400 members, `T0` `1789035000` … `1789166400`, disjoint by
construction from the set TZ-08 will score.

The report states the units considered (443), the members (400), the first and last member `T0`,
and the **SHA-256 of the newline-joined sorted member `T0` list**, so any later TZ can compare the
set by one value instead of a transcription. Fewer or more than 400 members → **BLOCKED**.

---

## 4. M1 — the dispersion of the settlement quantity

For each member, build the merged `chainlink` step function and its one-second grid over
`[T0 - 300, T0 + 300]` with `pfair.second_grid` — 601 points, exactly as TZ-07a built it. Write
`P(a)` for the grid value at offset `a` seconds from `T0`, and `mean(a, b)` for
`pfair.time_weighted_mean` over `[a, b]`.

**The model's horizon**, taken from `pfair` and not rewritten:

```
H(tau) = tau - 40            for tau >= 60
H(tau) = tau**3 / 10800      for tau <  60          # H(60) = 20 on both branches
```

**The residual the model's `sd` claims to describe**, at an anchor `a`:

```
tau >= 60:   Y(a, tau) = mean(a + tau - 60, a + tau) - P(a)
tau <  60:   Y(a, tau) = (tau / 60) * ( mean(a, a + tau) - P(a) )
```

The near-branch form is the future part of the settlement average with the weight the model gives
it; the realised part carries no dispersion and is already inside `state`.

**Anchors.** Every integer `a` with `[a, a + tau]` inside `[-300, 300]` — `601 - tau` anchors per
member per tau, at `tau ∈ pfair.TAUS = (240, 180, 120, 90, 60, 30, 10)`. Using every anchor rather
than the checkpoint instant alone is deliberate: it multiplies the sample by two to three orders of
magnitude and keeps the fit away from the one instant per interval that determines an outcome.

**The disconnect rule, standing since TZ-07a M6.** An anchor is dropped if any second of
`[a, a + tau]` lies inside a recorded outage for that member. The determination is **imported**
from `research/tz07a-variance-time.py` by `importlib`, exactly as TZ-07a imported
`tz06-calibration`; it is not reimplemented. Drops are counted and reported per tau.

**Normalisation.** For each member and tau, `sigma(tau)` is `pfair.realised_sigma` over the causal
window `[T0 - 300, T0 + (300 - tau)]` — the same `sigma_live` the pricer uses at that checkpoint,
so the constant measured here is the constant that pricer needs. Then

```
r = Y(a, tau) / ( sigma(tau) * sqrt(H(tau)) )
Λ(tau) = sqrt( sum over all members and admissible anchors of r**2  /  N(tau) )
```

**`Λ` is the raw root mean square, uncentred.** The model assumes the residual has mean zero; the
pooled mean of `r` is reported as a diagnostic, not subtracted.

**Why the root mean square and not a robust scale — decided now, before the numbers exist.** The
model is `p_fair = Phi(state / sd)`; the maximum-likelihood scale of a Gaussian is the root mean
square, and it is the only scale estimator that needs no outcome and no second model. Choosing a
robust scale instead would be asserting a non-Gaussian model that this project has not specified.
[решение принято мной] The discarded alternative is a MAD-based scale; it is measured and reported
below with no threshold, so that if the next finding is tail shape rather than scale, the data to
see it already exists.

**Reported per tau, none of it with a threshold:** `N` taken and dropped; the pooled mean of `r`;
the median over members of each member's own RMS of `r`; the **checkpoint-only** reading computed
from the single anchor `a = 300 - tau` over the 400 members; `MAD(r) / 0.674490` and
`IQR(r) / 1.348980`; and the empirical fraction of `|r|` above 1, 2 and 3 times `Λ(tau)` against
the normal's `0.3173`, `0.0455`, `0.0027`.

---

## 5. M2 — the freeze

`Λ(tau)` at all seven taus, **rounded to six significant digits**, written into
`research/pfair.py` as literals:

```python
SD_SCALE = {240: D("…"), 180: D("…"), 120: D("…"), 90: D("…"),
            60: D("…"), 30: D("…"), 10: D("…")}


def corrected_sd(tau, sigma):
    assert tau in SD_SCALE, "tau = %s has no measured scale; TZ-07b measured %s" % (
        tau, sorted(SD_SCALE))
    if tau < SETTLEMENT_S:
        h = D(tau) ** 3 / D(TAU_CUBED_DIVISOR)
    else:
        h = D(tau - 40)
    return SD_SCALE[tau] * sigma * h.sqrt()
```

`G_RATIO` and the previous body of `corrected_sd` are **removed**, not kept alongside: a
superseded constant left in the pricer is a trap for whoever reads it next, and `c44af68` holds it
in history. A `tau` with no measured scale raises; nothing is ever extrapolated.

The new instrument asserts, per tau and before it prints anything, that the literal in `pfair.py`
equals its own measurement rounded to six significant digits, and aborts if it does not.

---

## 6. The three frozen rows, and exactly what moves in each

### 6.1 `research/pfair.py`

Only §5. The report shows `git diff` and states that `far_branch`, `near_branch`,
`state_and_sd`, `p_fair`, `realised_sigma`, `time_weighted_mean`, `second_grid`,
`settlement_mean` and every constant other than `G_RATIO` are byte-identical to `main`.

### 6.2 `research/selftest-pfair.py`

Four checks encode the superseded composition and are **deleted by name**:
`tz07a_the_near_branch_is_untouched`, `tz07a_the_correction_at_the_boundary`,
`tz07a_the_correction_on_the_far_branch`, `tz07a_the_table_is_a_table_of_literals`.

**This deletion is authorized because the specification they encode is superseded, and for no
other reason. No test is ever deleted or edited because it failed.** The 56 `v5_*` model checks
and the 18 machinery checks are untouched and their counts are reported unchanged at 56 and 18.

A `tz07b_*` family replaces them, counted separately, each an `assert` that aborts the file, every
fixed expectation at `K` near 100,000 and `sigma` at live scale:

1. `sorted(SD_SCALE) == sorted(pfair.TAUS)` — every tau the pricer serves carries a measured
   constant, `10` included;
2. every value is a `Decimal` carrying exactly six significant digits;
3. `H(60)` is `20` computed on either branch, and `corrected_sd(60, s)` is
   `SD_SCALE[60] * s * sqrt(20)`;
4. `corrected_sd` is **strictly increasing in `tau`** across the seven keys at fixed `sigma` — more
   time remaining is more dispersion, and a measurement that breaks this is wrong, not surprising;
5. `corrected_sd(tau, sigma) / (sigma * sqrt(H(tau)))` equals `SD_SCALE[tau]` to a relative
   `1e-55` at every key;
6. linearity in `sigma` to a relative `1e-55` — the tolerance TZ-07a §6.2 established, one ulp of
   the 60-digit context being the only thing that separates the two orderings of the rounding;
7. an unmeasured `tau` raises.

### 6.3 `research/tz07a-variance-time.py`

It asserts the `G_RATIO` literals against its own measurement and emits `G_RATIO_as_written`, so
it cannot run once `G_RATIO` is gone. **Only that cross-check and that output key are removed.**
Every other line stays byte-identical, the report shows the diff, and V4 re-runs the file to prove
the removal cost nothing.

---

## 7. Validation

**Written by the Architect. The Executor runs these and does not design, extend or relax them.**
Every result is a count. **V1, V2, V3 or V4 failing is BLOCKED, not a finding.**

| # | check | reported as |
|---|---|---|
| V1 | the dispersion | `Λ(tau)` at all seven taus with anchors taken and dropped per tau and the member count, plus every diagnostic §4 lists, none with a threshold |
| V2 | causality of the corrected pricer | the first 20 members × the six gated taus: perturb every `chainlink` and `twap60` report timestamped after the checkpoint instant by `1.0001` and require the corrected `state`, `sd` and `p_fair` bit-identical — 120 of 120; plus the negative control on the last readable report, which must move the model output taken as a whole — 120 of 120 |
| V3 | determinism | two full runs of the instrument, every output byte-identical, by `cmp`. **The compared artifact is a pure function of the closed 400-member set and contains no count of anything still growing** — V6 is a separate invocation and is not part of it. |
| V4 | regression, two files | `research/tz06-calibration.py` unmodified and still reproducing TZ-06 §2.8's six `Brier(p_fair)` values to all six decimals and P at 397 of 400; and `research/tz07a-variance-time.py`, with only §6.3's removal applied, still reproducing TZ-07a §2.1's fifteen pooled `g(h)` to six significant digits |
| V5 | self-tests | `selftest-pfair.py` passes whole; `v5_*` unchanged at 56 and machinery at 18; the four deleted names and the new `tz07b_*` names both listed, and the new group counted on its own |
| V6 | how much test data exists | the count of interval directories with `T0 > 1789166400` and how many satisfy TZ-06 §4's five conditions, at the moment of the run, from a separate invocation |

---

## 8. The TZ-08 gate

**TZ-07a §8 stands verbatim and this TZ moves nothing in it** — not the set rule, not the scored
taus, not G1, not G2, not G3's `0.15`. It is deliberately **not restated here**: a gate restated
is a gate that can drift, and it is already committed to git where TZ-08 will read it.

The single thing that changes is which estimator TZ-08 scores: the constants §5 freezes, not
`G_RATIO`. TZ-08 is issued when 400 intervals with `T0 > 1789166400` qualify — 201 at the last
count — and not before.

---

## 9. Deliverable

The report contains, and contains nothing else of substance:

1. the fingerprint table — `wc -l` and `sha256sum` for `SYSTEM-MAP.md` and every file the map's §0
   table lists, plus the post-change hashes of the three files §6 authorizes;
2. the host gate's three observed values;
3. §3's set counts and the member-list hash;
4. V1–V6 as counts, with the `SD_SCALE` literals as written into the file;
5. the branch, the implementation commit and the pull request.

Publication is part of execution. **No calibration statistic, in sample or out, appears anywhere
in this report, and no outcome is read to produce it.**
