# TZ-10 — `sigma` or the link: the discriminating measurement

**Canonical filename: `CryptoTZ/TZ-10-sigma-or-link.md`.** The Executor names the committed file
from this line. Report: `CryptoReports/TZ-10-sigma-or-link-report.md`.

**Model: Opus.** It touches the pricer, gate arithmetic and multi-file diagnosis.

## 0. Fingerprint gate — compare before doing any work

**Required System Map revision: `2026-09-14-a`.** Required anchors:

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

- One new file, `research/tz10-sigma-or-link.py`, on branch `tz-10-sigma-or-link`.
- `research/pfair.py`, **additively and only to add `log_phi`** (§5.2). The §1.2 branches, `state`,
  `SD_SCALE`, `corrected_sd`, `phi` and `TAUS` are byte-identical before and after, asserted by V6.
  `A6` moves; the next map revision records the change and its additive nature, as it did for PR #7.
- Scratch under `/root/tz10-work/` only.

**May not be touched.**

- `SD_SCALE`, the §1.2 formulas, the §8 gate, the two committed member lists. No pricer is fitted,
  proposed or adopted by this TZ, whatever it finds.
- Any file under `/var/lib/btc-recorder/**` — read-only, and no quote file is opened at all. Tier C
  is Phase 2's input and a Phase 1 diagnostic does not spend it.
- `/root/btc-forensics/` and `/root/tz04a-env/`.
- Any committed report.

**Outcomes are read**, by M2 and by nothing else, for `λ̂` alone. This section names that, so no
later section has to be read against a prohibition that does not exist.

**No formula is reimplemented.** `Y(a, tau)` and the anchor enumeration come from
`tz07b-settlement-dispersion.py`; the disconnect rule from `tz07a-variance-time.py` through it; set
formation from `tz06-calibration.scoring_set`; `corrected_sd`, `phi`, `log_phi`, `TAUS`, the
realised-sigma estimator and the stream reader from `pfair.py` and `analyze.py`. Substituting a
different `sigma` is calling `pfair.corrected_sd` with a different first argument — nothing more.

## 3. Measurements

### 3.0 The sets and the three `sigma`s

**The set is the 800** — TZ-06's 400 and TZ-08a's 400 — re-derived by calling
`tz06-calibration.scoring_set`, with the member-list SHA-256s asserted equal to
`6d94a346a47a04a1a0849968effd9023d7585fe628b304ba2ae7a15953ee67f9` and
`3b17729c050e5fbf8fed1bd0877d5dd5c229370609cd672c84eeed1ddc3d5762`. No set is re-formed.

Write `u(a, tau, s) = Y(a, tau) / pfair.corrected_sd(s, tau)` — the standardized settlement
residual, whose uncentred RMS under the pricer's own `sigma` is exactly TZ-07b's `Λ`.

| `s` | window it is estimated over | causal? |
|---|---|---|
| `sigma_hat` | what the pricer uses, unchanged | **yes** |
| `sigma_post` | `chainlink`, `[close, close + 300]` — the successor interval | no |
| `sigma_win` | `chainlink`, `[a, close]` — the window that generates `Y` | no |

All three use `pfair`'s own realised-sigma estimator on the one-second grid; only the span differs.

**`sigma_post` is the primary non-causal arm, and the reason is statistical.** It is estimated on a
path disjoint from the one that produced `Y`, so `u` carries no self-normalization. `sigma_win`
divides a realization by its own realized scale, which shrinks tails mechanically; it is reported as
an **upper bound** on how much scale error can explain and is labelled as such everywhere it
appears. No verdict in §4 reads `sigma_win`.

**Qualification for the `sigma_post` arm** is a count of qualifying units, not a run: a member
qualifies if its successor interval directory exists, its manifest is complete, and the disconnect
rule admits the whole `[close, close + 300]` span. Non-qualifiers are excluded **from that arm
only**, disclosed in order with the reason, and counted.

**The intersection set** is the members admissible in all three arms. §4's verdict is computed on
the intersection and on nothing else, so the three arms are never compared across different
members. M1 additionally reports the `sigma_hat` arm over the full 800, for V4.

### 3.1 M1 — the shape, three ways

At each `tau` in `pfair.TAUS`, for each of the three `sigma`s, over the intersection set:

- `Λ` — uncentred root mean square of `u`
- `MAD / 0.674490` and `IQR / 1.348980`
- **`κ = Λ / (MAD / 0.674490)`** — the shape statistic. A normal gives `κ = 1` exactly.
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

`research/tz10-sigma-or-link.py`, on branch `tz-10-sigma-or-link`, delivered as a pull request. It
carries no threshold of its own: `κ`, `Λ` and the robust scales come from the TZ-07b instrument's
definitions, `λ̂` from the TZ-07a instrument's, the sets from `tz06-calibration.py`, and §4's
verdict is judged by the Architect from the reported numbers.

Every scratch output goes to `/root/tz10-work/`. The per-observation rows are written to
`/root/tz10-work/tz10-observations.csv` with enough columns to reconstruct any single row without
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

Self-tests, each aborting the run, added to `selftest-pfair.py`:

1. the two branches agree to 10 significant digits at `z` = `−30`, `−32`, `−34`;
2. `log_phi(z)` agrees with `log(phi(z))` to 12 significant digits for `z` in `−8 … 0`, at eleven
   points, at realistic magnitude — the arguments arise from `K = 100000.25` and `sigma = 3.25`,
   matching every other fixed expectation in that file;
3. `log_phi` is strictly increasing over `−40 … 5`;
4. `log_phi(−10.819)` is finite and lies between `−60.0` and `−55.0`;
5. `exp(log_phi(z)) == phi(z)` to 12 significant digits for `z` in `−8 … 8`.

The diff to `pfair.py` is insertions only.

## 6. Preflight the run records but does not gate on

Two `df` reads at least `1,800` s apart, plus `du -x -B1 -s /root/PROJECT_GAMING_PS5` at each, in
exact bytes with UTC timestamps. **The Boss reports that project's telemetry stopped; no TZ has
measured the stop**, and System Map §6 carries a range because of it. This read is how the next map
revision collapses that range. It gates nothing beyond the §0 floor.

## 7. Validation

| # | check | requirement |
|---|---|---|
| V1 | gates | fingerprint 6 of 6 · host 3 of 3 · resource floor in exact bytes at every read |
| V2 | causality of the causal arm | perturb every feed report at or after the anchor: `u` under `sigma_hat` bit-identical, 120 of 120; negative control, perturbing the last readable report moves it, 120 of 120. **The `sigma_post` and `sigma_win` arms are non-causal by construction and are exempt from V2** — this row names the exemption so no other section has to imply it |
| V3 | determinism | two full runs byte-identical |
| V4 | the instrument reproduces the committed measurement | under `sigma_hat`, TZ-07b's `Λ` table to six significant digits on the TZ-06 400, and TZ-08a V8's `Λ_oos` on the TZ-08a 400. **An instrument that cannot reproduce these is wrong and the run is BLOCKED** |
| V5 | set identity | both member-list SHA-256s equal the committed values, computed the same way |
| V6 | `pfair.py` additive only | `git diff` against the merge base shows insertions only; `SD_SCALE`, `corrected_sd`, `phi`, `state`, `TAUS` and the §1.2 branches byte-identical. The diff is printed in the report |
| V7 | `log_phi` | the five self-tests of §5.2, each aborting · and `λ̂` at `tau = 30` under `sigma_hat` recomputed with `log_phi`, compared against TZ-08a's `2.0418` and expected to agree past the sixth decimal |
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

- Report straight to `main` at `CryptoReports/TZ-10-sigma-or-link-report.md`.
- Code on `tz-10-sigma-or-link`, pull request opened, **not merged** — merge is the Boss's, after
  the Architect's verdict.
- No Release. No dataset, archive or binary enters git history.
- `/root/tz10-work/` is reclaimed by the next TZ once this report is on `main`, per the retention
  rule in System Map §6; anything this report names by SHA-256 is copied to `/root/btc-forensics/`
  first.
