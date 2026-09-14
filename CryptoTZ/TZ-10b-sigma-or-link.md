# TZ-10b — `sigma` or the link: the discriminating measurement

**Canonical filename: `CryptoTZ/TZ-10b-sigma-or-link.md`.** The Executor names the committed file
from this line. Report: `CryptoReports/TZ-10b-sigma-or-link-report.md`.

**This TZ replaces TZ-10a, which is BLOCKED, and TZ-10 before it.** Both reports stand on `main` and
neither is edited. TZ-10a's §7 V2 required `u = Y / sd` to be bit-identical under perturbation of the
very reports `Y` is built from, and no correct implementation can pass it; the Executor stopped
before building anything, which is what the contract asks for. The audit of that stop found three
more defects in the same TZ — System Map §7 items 36, 37, 38 and 39.

**The measurement, the sets, the discriminator and the pre-registered prediction are carried over
unchanged, and the `log_phi` formula is byte-identical to TZ-10's.** Four places differ and nothing
else: §2's outcome prohibition, §3.0's definition of the standardized residual, §5.2 item 1's two
asymptotic literals, and §7 V2 and V4.

**Model: Opus.** It touches the pricer, gate arithmetic and multi-file diagnosis.

## 0. Fingerprint gate — compare before doing any work

**Required System Map revision: `2026-09-14-c`.** Required anchors:

| anchor | required value |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-answered-no / 2-not-started` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` |
| `A6` — pricer | `cb72abb8dd8a` |

Any mismatch → BLOCKED before any work, with a report saying which row failed and nothing else.

**Host gate, all three or it is not the capture host:** `/var/lib/btc-recorder/` exists and holds
interval directories · the recorder process is running and the newest `runtime.jsonl` start record
carries sha `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` · the filesystem holding it is `/dev/vda2`,
total `31,612,203,008` bytes.

**Resource floor, in exact bytes, derived from System Map §6.** Free space on `/dev/vda2` at run
start must be at least `10,327,051,118` bytes — `2,000,000,000` plus three days at
`2,775,683,706` bytes/day, the **pessimistic** rate of §6's headroom range. The pessimistic end is
the gate because the consumer that produced it is another project's process and can resume without
notice. Below the floor → BLOCKED. Every `df` read during the run asserts at or above
`3,000,000,000`.

**Worktree hygiene, asserted at start.** `git worktree list --porcelain` is reported verbatim and
asserted to contain no `prunable` entry; the branch of the primary checkout `/root/btc-5m-twap` is
reported by name. Not a gate — a disclosure, because the running recorder executes from that
checkout.

## 1. Why

Phase 1 answered no. TZ-08a's G3 failed at `tau` 60 and 30 with `λ̂` `1.2949` and `2.0418`, and V9
showed why: the settlement residual has a sharp centre and a tail 8 to 10 times the normal's below
`tau = 90`, with the robust scale 56 to 81 per cent under the RMS. A sharp centre with a heavy tail
is not a normal at any scale, so **no constant per `tau` closes that gate.**

Two explanations survive, and the data in hand cannot separate them.

- **H-link.** The conditional law of the settlement quantity is not Gaussian. It is heavy-tailed —
  Student's `t` the leading candidate — and `Phi` is the wrong link.
- **H-sigma.** The law is Gaussian given the volatility actually in force, and the estimate of that
  volatility lags the move. On the observation that carries `λ̂` at `tau = 30`, `T0 1789268400`,
  `sigma_live` reads `0.689` at `tau = 30` and `1.408` at `tau = 10` — a doubling inside twenty
  seconds, an estimator catching up rather than predicting.

**They are indistinguishable in the unconditional residual, and that is not an accident:** a
Student's `t` *is* a scale mixture of normals. A pool of correct Gaussians with a floating `sigma`
reproduces V9's picture exactly — sharp centre, heavy tail. Measuring the unconditional shape again,
at any sample size, cannot decide this. **The measurement must be conditional**, and this TZ is that
measurement and nothing else.

It fits no pricer, adopts no link, and moves neither `SD_SCALE` nor the TZ-07a §8 gate.

## 2. Scope

**May be touched.**

- One new file, `research/tz10b-sigma-or-link.py`, on branch `tz-10b-sigma-or-link`.
- `research/pfair.py`, **additively and only to add `log_phi`** (§5.2). The §1.2 branches, `state`,
  `SD_SCALE`, `corrected_sd`, `phi` and `TAUS` are byte-identical before and after, asserted by V6.
  `A6` moves; the next map revision records the change and its additive nature, as it did for PR #7.
- **`research/selftest-pfair.py`, additively**, for §5.2's six self-tests. The map's §0 table lists
  it `frozen`; **this TZ authorizes that row to move**, it is not an anchor, and the next map
  revision carries its new line count, byte count and SHA-256. The 104 asserts already in the file
  are not edited, reordered or removed.
- Scratch under `/root/tz10b-work/` only.

**May not be touched.**

- `SD_SCALE`, the §1.2 formulas, the §8 gate, the two committed member lists. No pricer is fitted,
  proposed or adopted by this TZ, whatever it finds.
- Any file under `/var/lib/btc-recorder/**` — read-only, and no quote file is opened at all. Tier C
  is Phase 2's input and a Phase 1 diagnostic does not spend it.
- `/root/btc-forensics/` and `/root/tz04a-env/`.
- Any committed report.

**Outcomes are read in exactly two places, and both are named here**, so that no later section has
to be read against a prohibition that does not exist.

1. **M2**, for `λ̂` alone.
2. **Set formation.** §3.0 calls `tz06-calibration.scoring_set`; its `qualification` calls
   `analyze.venue`, which opens `resolution.json` and reads `resolved_up` and `priceToBeat` for
   every unit it considers, member and non-member alike — conditions 2 and 3 of the committed TZ-06
   set rule. **That rule is not modified and it is exempt from every prohibition in this section.**

**No outcome enters any other statistic:** `Λ`, `κ`, the robust scales, the tail fraction, `f`, `g`
and `R²` are computed without one. System Map §7 items 23 and 39 are why this list is explicit.

**No formula is reimplemented.** `Y(a, tau)` and the anchor enumeration come from
`tz07b-settlement-dispersion.py`; the disconnect rule from `tz07a-variance-time.py` through it; set
formation from `tz06-calibration.scoring_set`; `corrected_sd`, `phi`, `log_phi`, `TAUS`, the
realised-sigma estimator and the stream reader from `pfair.py` and `analyze.py`. **The committed
signature is `corrected_sd(tau, sigma)` — `tau` first.** Substituting a different `sigma` is calling
it with a different **second** argument, and nothing more.

## 3. Measurements

### 3.0 The sets and the three `sigma`s

**The set is the 800** — TZ-06's 400 and TZ-08a's 400 — re-derived by calling
`tz06-calibration.scoring_set`, with the member-list SHA-256s asserted equal to
`6d94a346a47a04a1a0849968effd9023d7585fe628b304ba2ae7a15953ee67f9` and
`3b17729c050e5fbf8fed1bd0877d5dd5c229370609cd672c84eeed1ddc3d5762`. No set is re-formed.

**Two standardizations of the same residual, and the identity between them.** `Y(a, tau)` and the
anchor enumeration are TZ-07b's, unmodified. With `H(tau)` the pricer's own horizon —
`tau − 40` at `tau >= 60`, `tau³ / 10800` below it — write

- `r(a, tau) = Y(a, tau) / (sigma_hat · sqrt(H(tau)))` — **TZ-07b's own quantity**, whose uncentred
  RMS over the TZ-06 400 is exactly TZ-07b's `Λ`;
- `u(a, tau, s) = Y(a, tau) / pfair.corrected_sd(tau, s)` — the residual standardized by the `sd`
  the pricer actually divides by.

`pfair.corrected_sd(tau, s) = SD_SCALE[tau] · s · sqrt(H(tau))`, so **`u = r / SD_SCALE[tau]`
identically**, and the RMS of `u` under `sigma_hat` is `1` to within the rounding of a six-digit
literal — not `Λ`. **Everything §4's verdict reads is computed on `u`:** `κ`, the robust scales, the
tail fraction and `λ̂`. **`r` exists for V4 and for nothing else.** System Map §7 item 38 is why this
paragraph replaces one line.

| `s` | window it is estimated over | causal? |
|---|---|---|
| `sigma_hat` | what the pricer uses, unchanged — `pfair.realised_sigma` over `[T0 − 300, T0 + 300 − tau]`, one per member per `tau` | **at the checkpoint anchor only**, and V2 tests exactly that |
| `sigma_post` | `chainlink`, `[T0 + 300, T0 + 600]` — the successor interval | no |
| `sigma_win` | `chainlink`, `[a, a + tau]` — the span that generates `Y` | no |

All three use `pfair`'s own realised-sigma estimator on the one-second grid; only the span differs.

**`sigma_post` is the primary non-causal arm, and the reason is statistical.** It is estimated on a
path disjoint from the one that produced `Y`, so `u` carries no self-normalization. `sigma_win`
divides a realization by its own realized scale, which shrinks tails mechanically; it is reported as
an **upper bound** on how much scale error can explain and is labelled as such everywhere it
appears. No verdict in §4 reads `sigma_win`.

**Qualification for the `sigma_post` arm** is a count of qualifying units, not a run: a member
qualifies if its successor interval directory exists, its manifest is complete, and the disconnect
rule admits the whole `[T0 + 300, T0 + 600]` span. Non-qualifiers are excluded **from that arm
only**, disclosed in order with the reason, and counted.

**The intersection set** is the members admissible in all three arms. §4's verdict is computed on
the intersection and on nothing else, so the three arms are never compared across different
members. M1 additionally reports the `sigma_hat` arm over the full 800, for V4.

### 3.1 M1 — the shape, three ways

At each `tau` in `pfair.TAUS`, for each of the three `sigma`s, over the intersection set:

- `Λ_u` — uncentred root mean square of `u`. **It is not TZ-07b's `Λ`:** under `sigma_hat` it is `1`
  by construction, and `Λ_u · SD_SCALE[tau]` is TZ-07b's `Λ`, which is V4's business (§3.0).
- `MAD / 0.674490` and `IQR / 1.348980`
- **`κ = Λ_u / (MAD / 0.674490)`** — the shape statistic, scale-free. A normal gives `κ = 1`
  exactly.
- `P(|u| > 3 · MAD / 0.674490)`, against the normal's `0.0027`
- admissible anchors, dropped anchors, and the members contributing each drop

For reference, TZ-08a V9's out-of-sample readings imply `κ_hat` of about `1.22 / 1.28 / 1.43 /
1.69 / 2.27 / 3.45 / 5.26` at `tau` 240 / 180 / 120 / 90 / 60 / 30 / 10. That is a published
expectation, not a threshold; the run reports what it measures.

### 3.2 M2 — `λ̂`, three ways

The TZ-07a §8 scale statistic, recomputed with each `sigma`: the maximiser over `λ` of the Bernoulli
log-likelihood of the venue's resolutions under `p = phi(state / (λ · corrected_sd(s, tau)))`.

Report per `tau`, per `sigma`, and separately for the TZ-06 400, the TZ-08a 400 and the pooled set.
The likelihood uses `log_phi` (§5.2) and never `log(phi(...))`.

**Per the standing rule from defect 27, every `λ̂` is reported together with its value recomputed
without its single most influential observation, and that observation is named by `T0` and `tau`.**

### 3.3 M3 — where the heavy tail lives

Stratify the intersection set two ways and recompute `κ` and the tail statistic **within** each
stratum, under `sigma_hat`:

1. deciles of `sigma_hat` at the anchor — **causal**, so a finding here can inform a pricer;
2. deciles of `log(sigma_post / sigma_hat)` — non-causal, diagnostic only.

Report per `tau` the size-weighted mean and the median of the per-stratum `κ`, and the pooled `κ`
beside them. If the excess kurtosis lives **between** strata, within-stratum `κ` falls toward 1 and
the pooled value does not. If it lives **within**, both stay put.

### 3.4 M4 — is the scale error knowable in advance?

Regress `log(sigma_post / sigma_hat)` on this fixed set of causal, decision-time regressors, named
here before any data is seen:

1. `log(sigma_60 / sigma_300)` — the same estimator at 60 s and 300 s
2. `log sigma_hat`
3. `|feed move over the last 30 s| / (sigma_hat · sqrt(30))`
4. `tau`

Ordinary least squares, fitted on the **TZ-06 400** and evaluated on the **TZ-08a 400**. Report
in-sample `R²` and out-of-sample `R²` computed against the in-sample mean, so it may be negative.
**No model is adopted.** This measures whether the mixing variable is forecastable, which §4.3 needs
and nothing else does.

### 3.5 M5 — the observation the gate hangs on

One row: `T0 1789268400` at `tau` 30 and at `tau` 10 — `sigma_hat`, `sigma_post`, `sigma_win`, `Y`,
`u` under each `sigma`, `state`, `z`, `p_fair`, `log_phi(z)` and the venue's resolution. Reported
because a committed gate statistic hangs on it. **No conclusion is drawn from one point.**

## 4. The discriminator — fixed before any data is seen

### 4.1 The primary reading

With `κ_hat(tau)` and `κ_post(tau)` from M1 over the intersection set, define the explained fraction

`f(tau) = (κ_hat(tau) − κ_post(tau)) / (κ_hat(tau) − 1)`

`f = 1`: a scale that does not lag makes the residual exactly as sharp as a normal. `f = 0`: it
changes nothing. The verdict is read at `tau` 60 and `tau` 30 — the two the gate failed at.

| `f` at **both** 60 and 30 | verdict |
|---|---|
| `>= 0.50` | **σ-dominant.** The link is not the defect; TZ-11 estimates `sigma`. |
| `<= 0.20` | **link-dominant.** The estimator is not the defect; TZ-11 replaces `Phi`. |
| anything else, or the two `tau`s disagree | **mixed** — §4.3 decides what comes next. |

### 4.2 The second reading, independent of the first

The same verdict on `λ̂` instead of `κ`:

`g(tau) = (|λ̂_hat(tau) − 1| − |λ̂_post(tau) − 1|) / |λ̂_hat(tau) − 1|`, same thresholds, same two
`tau`s.

**Both are reported. Where they disagree, the verdict is mixed, and the disagreement is the
finding.** Two functionals of the same distribution pointing opposite ways is exactly what happened
between `Λ` and `λ̂` in TZ-08a; this TZ expects it and does not resolve it by choosing one.

### 4.3 Mixed

Then M4 decides the next TZ, not the model. **Ruling, stated now so it is not chosen after the
data:** a scale mixture whose mixing variable cannot be forecast at decision time **is**, for
pricing purposes, a heavy-tailed link — the distinction only pays if the mixing variable is
predictable.

- out-of-sample `R² >= 0.10` → TZ-11 estimates `sigma`.
- below `0.10` → TZ-11 replaces the link.

### 4.4 The Architect's pre-registered prediction

Written before the run, and recorded so it can fail: **`f(60)` between 0.5 and 0.7, `f(30)` between
0.6 and 0.8, out-of-sample `R²` between 0.05 and 0.15 — that is, mixed, leaning σ.**

The reasoning, in one line each. For σ: a doubling of `sigma` inside twenty seconds cannot be
tracked by any estimator with a 60-second window, and the failure sits exactly where windows are
shortest. Against σ being the whole story: V9's tail at `tau = 240` is `0.0125` against the normal's
`0.0027` — 4.6 times — and at `tau = 240` the estimator has 240 seconds of fresh data and the
settlement window is 200 seconds away, which is where a lag story is weakest.

**If the prediction fails, how it fails is the finding, and the gate is judged on §4.1 and §4.2 as
written.**

## 5. Implementation

### 5.1 The instrument

`research/tz10b-sigma-or-link.py`, on branch `tz-10b-sigma-or-link`, delivered as a pull request. It
carries no threshold of its own: `κ`, `Λ_u` and the robust scales come from the TZ-07b instrument's
definitions, `λ̂` from the TZ-07a instrument's, the sets from `tz06-calibration.py`, and §4's
verdict is judged by the Architect from the reported numbers.

Every scratch output goes to `/root/tz10b-work/`. The per-observation rows are written to
`/root/tz10b-work/tz10b-observations.csv` with enough columns to reconstruct any single row without
re-running the pipeline, and the report names that file by line count, byte count and SHA-256.

### 5.2 `log_phi`, added to `pfair.py`

TZ-07a §8 fixed a likelihood over `Phi` and no tail-accurate `log Phi`; `pfair.phi` returns exactly
`0.0` below `z ≈ −8.37`, which sent `ll(1)` to `-inf` at `tau = 30` in TZ-08a. **This TZ fixes the
tail-accurate `log Phi` in the same section that uses it**, as the repair rule for defect 26
requires. It is added to `pfair.py` because one formula has one implementation.

```
log_phi(z):
    z > -35 :  log(0.5 * erfc(-z / sqrt(2)))
    z <= -35:  -0.5*z*z - 0.5*log(2*pi) - log(-z) + log1p(-1/z**2 + 3/z**4 - 15/z**6)
```

**The formula is unchanged from TZ-10 and it is correct.** The Architect verified both branches
against a 60-decimal-digit reference at fourteen points from `0` to `−40`; they agree to 12
significant digits at every one. TZ-10 was stopped by its expectations, not by this.

**The expectations below are literals computed from a 60-decimal-digit reference** — the same
`log(0.5 · erfc(−z / sqrt(2)))` evaluated at 60 digits, which is independent of **both** branches of
the function under test — **and they are compared against `pfair.phi` only where that function is
itself sound.** `pfair.phi` is `0.5*(1 + erf(z/sqrt(2)))`; below about `z = −4.5` it is the sum of two
doubles near 1, so its relative error grows as `Phi` shrinks — `3.9e-11` at `z = −5` and `1.8%` at
`z = −8`. It is the reference in `−3 … 3` and nowhere else.

Six self-tests, each aborting the run, added to `research/selftest-pfair.py`.

**Item 1 — the literals.** `log_phi(z)` equals each value below to 12 significant digits, with `z`
passed as the bare float printed here.

| `z` | `log_phi(z)` |
|---|---|
| `0` | `-0.693147180559945` |
| `-1` | `-1.84102164500926` |
| `-2` | `-3.78318433368203` |
| `-3` | `-6.60772622151035` |
| `-4` | `-10.3601014865273` |
| `-5` | `-15.0649983939887` |
| `-6` | `-20.7367689499747` |
| `-8` | `-35.0134371599145` |
| `-10.819` | `-61.8339909672382` |
| `-15` | `-116.131384845712` |
| `-20` | `-203.917155371097` |
| `-30` | `-454.321243956343` |
| `-36` | `-652.503227593798` |
| `-40` | `-804.608442013754` |

The last two are on the asymptotic branch and the rest on the `erfc` branch, so item 1 exercises
both. **The two asymptotic literals are not that branch's own output, and that is the point.** The
branch truncates after `−15/z⁶`, so it sits above the reference by the dropped `105/z⁸` term —
`5.67e-14` relative at `z = −36` and `1.98e-14` at `z = −40`. Both are inside 12 significant digits
with about a decade to spare, which is why the tolerance is 12 and not more. TZ-10a carried
`-652.503227593835` and `-804.60844201377` here, which are the truncated series' own values: they
passed, and they could not have failed. **A literal that reproduces the implementation it tests
proves nothing** — System Map §7 item 37.

"12 significant digits" is equality under `%.11e` formatting, and the relative difference is printed
beside each row so any other reading can be applied to the same numbers.

**Item 2 — branch agreement at the crossover.** The two branches agree to 10 significant digits at
`z` = `−30`, `−32`, `−34`. TZ-10's evidence already shows 3 of 3, at relative differences `3.49e-13`,
`1.84e-13` and `1.01e-13`.

**Item 3 — the identity, where the reference is sound.** `exp(log_phi(z)) == pfair.phi(z)` to 12
significant digits at the seven integers `−3 … 3`. Verified by the Architect over `−3 … 3` at a step
of `0.01`: worst relative disagreement `1.6e-14`, no failing grid point.

**Item 4 — realistic magnitude.** With `K = 100000.25`, `sigma = 3.25` and `sd` taken from the far
branch at `tau = 240`, form `S_t = K + z · sd` for `z` = `−10.819`, `−8`, `−3`, `0`. Then
`log_phi((S_t − K) / sd)` is finite and equals item 1's literal for that `z` to 12 significant
digits. Item 1 fixes the function; **item 4 fixes the composition**, which is what CANON's
realistic-magnitude rule asks for. `z` itself carries no units, so item 1 is stated in bare floats
deliberately.

**Item 5 — shape.** `log_phi` is strictly increasing over `−40 … 5` at a step of `0.001`, and finite
at every point of `−40 … 40` at the same step.

**Item 6 — the pathology this function exists to remove, asserted as a test.** At `z = −10.819`:
`pfair.phi(z)` is exactly `0.0`, `log(pfair.phi(z))` is not finite, `log_phi(z)` is finite, and
`exp(log_phi(z))` is `1.399068e-27` to seven significant digits and strictly positive. **This is
defect 26 written down as an assertion.** It is expected to fail the day `pfair.phi` is changed —
correctly, because that would be a change to the §1.2 link and belongs to a TZ of its own.

The diff to `pfair.py` is insertions only. The diff to `selftest-pfair.py` is insertions only.

**If any item goes red, the run is BLOCKED and no test is edited to make it pass.** That is what
TZ-10 asked for and got, and it is what this TZ asks for again.

## 6. Preflight the run records but does not gate on

Two `df` reads at least `1,800` s apart, plus `du -x -B1 -s /root/PROJECT_GAMING_PS5` at each, in
exact bytes with UTC timestamps. **The Boss reports that project's telemetry stopped; no TZ has
measured the stop**, and System Map §6 carries a range because of it. This read is how the next map
revision collapses that range. It gates nothing beyond the §0 floor.

## 7. Validation

| # | check | requirement |
|---|---|---|
| V1 | gates | fingerprint 6 of 6 · host 3 of 3 · resource floor in exact bytes at every read |
| V2 | causality of the causal arm | **What is tested is the denominator, and this row says so.** `Y(a, tau)` is the settlement average after the anchor minus the reading in force at it, so `Y` — and therefore `u` — moves under any perturbation of the future in any correct implementation: **the numerator is exempt from bit-identity by construction and no check in this TZ requires it.** The sample is the first **20 members of the TZ-06 set in `T0` order at all seven `tau` — 140 checkpoints**, named here so the count is a count. Perturb every `chainlink` report stamped **strictly after** the checkpoint instant `T0 + (300 − tau)` with the committed `tz06.perturb_after`: `sigma_hat` and `pfair.corrected_sd(tau, sigma_hat)` bit-identical, **140 of 140**. Negative control: `tz06.perturb_one` on `tz06.last_readable` moves `sigma_hat`, **140 of 140**. **"At or after" is not used and may not be substituted** — it moves `sigma_hat` wherever a report is stamped at the anchor instant, which is the TZ-08 defect TZ-08a §7 V2 repaired and TZ-10a reintroduced (§7 item 36). **The `sigma_post` and `sigma_win` arms are non-causal by construction and are exempt from V2.** |
| V3 | determinism | two full runs byte-identical |
| V4 | the instrument reproduces the committed measurement | **On `r`, not on `u`** (§3.0): the uncentred RMS of `r` under `sigma_hat` equals TZ-07b's `Λ` table to six significant digits on the TZ-06 400, and TZ-08a V8's `Λ_oos` on the TZ-08a 400. The instrument computes `u` and prints `RMS(u) · SD_SCALE[tau]` beside `RMS(r)`; the two agree by construction and any disagreement is itself a failure. **An instrument that cannot reproduce these is wrong and the run is BLOCKED** |
| V5 | set identity | both member-list SHA-256s equal the committed values, computed the same way |
| V6 | `pfair.py` additive only | `git diff` against the merge base shows insertions only; `SD_SCALE`, `corrected_sd`, `phi`, `state`, `TAUS` and the §1.2 branches byte-identical. The diff is printed in the report |
| V7 | `log_phi` | the six self-tests of §5.2, each aborting · and `λ̂` at `tau = 30` under `sigma_hat` recomputed with `log_phi`, compared against TZ-08a's `2.0418` and expected to agree past the sixth decimal |
| V8 | the capture is untouched | recorder pid and start-record sha unchanged from run start to run end, interval count not fallen, and no file under `/var/lib/btc-recorder/**` written |
| V9 | fingerprint table | every row of map §0 reported in lines, bytes and SHA-256; the frozen rows must match |
| V10 | disclosure | every unit considered, in order, members and non-members alike, with the reason for each non-member — for the 800 and separately for the `sigma_post` arm |
| V11 | influence | every `λ̂` in M2 reported with its value recomputed without its single most influential observation, that observation named |

## 8. Report structure

`## 1` the measurements in §3's order · `## 2` §4's two readings, the numbers, and whether the
prediction held · `## 3` implementation and `log_phi` · `## 4` validation, V1 … V11 · `## 5`
publication · `## 6` what could not be implemented as written, including every reading chosen where
this TZ leaves room.

**Counts are counts.** "All checks passed" is not a result. Section numbers are asserted unique
before delivery.

## 9. Publication

- Report straight to `main` at `CryptoReports/TZ-10b-sigma-or-link-report.md`.
- Code on `tz-10b-sigma-or-link`, pull request opened, **not merged** — merge is the Boss's, after
  the Architect's verdict.
- No Release. No dataset, archive or binary enters git history.
- **Three scratch files are named by SHA-256 in committed reports and are preserved first**, each
  copied to `/root/btc-forensics/` and verified equal at both ends against the hash its report
  names, before anything is reclaimed:

  | source | destination | SHA-256 the report names |
  |---|---|---|
  | `/root/tz10-work/probe-log-phi.py` | `tz10-work--probe-log-phi.py` | `5eef7ae91f1ac0fbd70b2b6b724c6f4688194c537f3c09d89f42d3b2298fd481` |
  | `/root/tz10a-work/probe-v2.py` | `tz10a-work--probe-v2.py` | `523cfca70e32d7f19357fd6a3023c19fd79b56c20d16651ca06d5e6f30508468` |
  | `/root/tz10a-work/probe-selftests.py` | `tz10a-work--probe-selftests.py` | `b67ee8b24a103a38467b69d7df424309862a5567e07d6340a53d527d37a4e747` |

- Then `/root/tz10-work/` and `/root/tz10a-work/` are reclaimed, as the retention rule directs.
  **A single tree has not been tested against the permission classifier** — only a block of five
  was, in TZ-09. If a removal is refused, disclose it and leave the directory; both hold a few
  kilobytes and neither is worth a hands-on action from the Boss.
- `/root/tz10b-work/` is reclaimed by the next TZ once this report is on `main`, on the same terms.
