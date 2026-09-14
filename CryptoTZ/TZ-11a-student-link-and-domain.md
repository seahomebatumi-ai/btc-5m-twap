# TZ-11a — the Student link and the domain it is priced on

**Canonical filename: `TZ-11a-student-link-and-domain.md`.** The Executor names the committed file
from this line and from nothing else.

**This TZ replaces TZ-11**, which was BLOCKED at its own §5.2 item 5 before anything was built
(CANON hard rule 4). It carries four repairs — System Map §7 items 45, 46, 47 and 48 — and changes
the measurement itself in one place only: §3.3 is now reported per set before it is reported
pooled, which closes §7 item 41.

**Executor model: Opus.** This touches the §1.2 link, gate arithmetic and a frozen pricer.

---

## 0. Fingerprint gate, host gate, resource floor

The Executor compares every row below before doing any work. A mismatch on any one is **BLOCKED**
before the first file is read.

**Required System Map revision:** `2026-09-14-e`.

| anchor | required |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-answered-no / 2-not-started` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` |
| `A6` — pricer | `45b307b221d4` |

`A6` is `research/pfair.py` after PR #11 and is the value TZ-11 read and did not move. **This TZ
scores a pricer and moves `A6`**; the report states the value before and after.

**Host gate.** All three, or this is not the capture host and the run is BLOCKED:

1. `/var/lib/btc-recorder/btc-updown-5m/` exists and holds interval directories.
2. The recorder process is running and the newest `runtime.jsonl` start record carries sha
   `4216c04673ced76b5b2ac60ef57c9abedc46f9b9`.
3. The filesystem holding it is `/dev/vda2`, total `31,612,203,008` bytes.

**Resource floor, in exact bytes, derived from System Map §6.**

- Free space at run start, on `/dev/vda2`: at least **`2,060,000,000`** bytes — the project floor
  `2,000,000,000` plus `60,000,000` for this run's scratch.
- Free space at every later read, asserted by the instrument: at least **`2,000,000,000`** bytes.
- Both are `assert`s that abort the run, not comparisons made by reading. Every read is reported
  with its UTC timestamp.

**Host preflight, reported and gating nothing beyond the floor.** System Map §6 now carries a
measured headroom of `151` days that is **conditional on `telemetry-watch.service` staying
disabled**, so this TZ re-measures the condition. At run start and again at least `1,800` s later,
take and report: `df -B1 /dev/vda2`; `du -x -B1 -s /root/PROJECT_GAMING_PS5`; and `systemctl
is-enabled telemetry-watch.service` together with `systemctl is-active telemetry-watch.service`,
each captured with its exit status rather than asserted. Report the implied bytes/day of both the
tree and of free space, and state this run's own scratch separately (System Map §7 item 29). **No
file of that project is opened**; names, sizes and modification times only.

---

## 1. Why

Phase 1 answered **no**, and TZ-10b answered why: the link. `Φ` is not the law of the settlement
residual, the deviation grows monotonically as `tau` falls, and the `sigma`-lag alternative is
closed three ways — a non-causal scale free of any lag makes the shape worse, conditioning on the
realised scale error does not collapse it, and the scale error is not forecastable from causal
inputs.

Two things follow, and this TZ does both at once because either alone is known to fail.

**First, the link.** `κ` maps exactly to a Student's `t` degrees of freedom. TZ-10b's measured `κ`
implies `ν` of about `7.06` at `tau = 240` falling to `2.14` at 10. A `t` link with a measured
`ν(tau)` is therefore the replacement `Φ` needs, and it removes the pathology that produced
`λ̂ = 2.0418`: at `z = −10.819`, `Φ` returns exactly `0.0` and its log is `−inf`, while
`F_3(−10.819)` is `8.4465826393e-04` and its log is `−7.07657843379202`.

**Second, the domain.** Every per-`tau` constant this project has frozen has failed to transfer
between two adjacent day-and-a-half windows — `G_RATIO`, then `SD_SCALE`, and now `κ` itself, whose
implied `ν` is `17.1` on the TZ-06 window against `4.69` on the TZ-08a window at `tau = 240`. A
fourth constant fitted over all members would fail the same way. TZ-10b M3 shows where the
instability lives: the heavy tail sits in the **low-`sigma_hat`** deciles — `κ` `3.227` in decile 1
against `1.119` in decile 10 at `tau = 30`. `sigma_hat` is causal and known at decision time, so it
can be an admissibility rule rather than a lament. **A pricer that declines to quote is a pricer; a
pricer that quotes a number it cannot stand behind is not.**

This TZ fits both on the TZ-06 400 alone and scores them on **two** disjoint out-of-sample sets.
Nothing is re-fitted afterwards. `SD_SCALE`, `corrected_sd`, `phi`, `log_phi`, `p_fair`, `state` and
TZ-07a §8's threshold do not move.

**What changed from TZ-11.** §5.2 item 5 no longer fixes an expectation on a quantity this TZ
measures (§7 item 45); §5.3's diff shape is stated as it really is and V6 asserts it (item 46); V12
defines influence for a profile fit, requires one refit instead of several hundred, and states its
cost (item 47); V4 is named as an outcome-reading place, its member rule is scoped, G2's pooling is
named and M5's population is named (item 48). Nothing in §3's measurement or §4's gate is weakened.

---

## 2. Scope

**Repository paths this TZ authorizes to change, and no others:**

| path | change | current state in map §0 |
|---|---|---|
| `research/pfair.py` | **insertions only**: §5.1's twelve new names, appended after `log_phi` | `frozen`, anchor `A6` — moves |
| `research/selftest-pfair.py` | **insertions only**: §5.2's family of six | `frozen` — moves |
| `research/tz07a-variance-time.py` | **insertions, plus exactly the four replaced lines named in §5.3 and no others** | `frozen` — moves |
| `research/tz11a-student-link.py` | new: the instrument | does not exist |
| `CryptoReports/TZ-11a-student-link-and-domain-report.md` | new | does not exist |

Every `frozen` row this TZ moves is named here by path, and the map's next revision carries each new
line count, byte count and hash (System Map §7 item 35).

**What may not be touched, and the exemptions, named here in this section** (System Map §7 items 23,
39 and 44):

- `/var/lib/btc-recorder/**` — read-only, always. No exemption.
- The recorder process — never signalled, never restarted. No exemption.
- `/root/tz04a-env/` and `/root/btc-forensics/` — **exempt for §9's copies alone**, which add files
  by exclusive create (`open(..., "xb")`) and overwrite nothing. Nothing else in either tree may be
  created, altered or removed.
- Every other committed file, including every report and every other `research/` script.
- **`SD_SCALE`, `corrected_sd`, `phi`, `log_phi`, `p_fair`, `far_branch`, `near_branch`,
  `state_and_sd`, `TAUS` and `GATED_TAUS` in `pfair.py` are byte-identical after this TZ**, asserted
  by V6.

**Outcomes.** `resolution.json`, `resolved_up` and `priceToBeat` are read in exactly **three**
places, and all three are named here:

1. inside `tz06.qualification`, which every set-formation call reaches for every unit it considers,
   member and non-member alike;
2. inside **M4 and M5**, which are the only places a label enters a number this TZ prints as a
   measurement;
3. inside **V4's third assertion**, which calls the committed `tz07a.lambda_hat` at its default on
   the TZ-08a 400 and therefore reads those 400 labels in order to reproduce a committed figure.

**M1, M2, M3 and the whole of §5 read no outcome of any kind.**

**Signatures, as the files hold them, read from `origin/main` at `ecc5a0b`:**

```
pfair.phi(z)                                  pfair.log_phi(z)
pfair.far_branch(tau, s_t, k, sigma)          pfair.near_branch(tau, s_t, k, sigma, m_r)
pfair.state_and_sd(tau, s_t, k, sigma, m_r=None)
pfair.p_fair(state, sd)                       pfair.corrected_sd(tau, sigma)
pfair.realised_sigma(grid)                    pfair.second_grid(rows, first_s, last_s)
pfair.settlement_mean(t0, s3_rows, t=config.INTERVAL_S)
pfair.observations(t0, s1_rows, s3_rows, taus=TAUS)
pfair.SETTLEMENT_S = 60   pfair.TAU_CUBED_DIVISOR = 10800
pfair.GATED_TAUS = (240, 180, 120, 90, 60, 30)      pfair.TAUS = GATED_TAUS + (10,)
tz06.qualification(t0, manifests)             tz06.scoring_set(manifests, need=SET_SIZE, *, after=None)
tz06.calibration(pairs)                       tz06.brier(pairs)
tz06.perturb_after(rows, ts_ms)               tz06.perturb_one(rows, idx)
tz06.last_readable(rows, ts_ms)               tz06.build(*, after=None, need=SET_SIZE)
tz06.SET_SIZE = 400  tz06.MAX_FAILING_BINS = 2  tz06.BIN_MIN_N = 20  tz06.PERTURBATION = D("1.0001")
tz07a.excluded_seconds(t0, manifests)         tz07a.log_likelihood(pairs, lam)
tz07a.lambda_hat(pairs)
tz07b.residual(rows, keys, t0, grid, a, tau)  tz07b.member_r(t0, manifests)
tz07b.horizon_sd(tau, sigma)                  tz07b.member_list_sha(members)
tz08a.the_set(manifests)
```

---

## 3. The measurement

### 3.0 The three sets

| set | rule | member-list SHA-256 |
|---|---|---|
| **fit** | the TZ-06 400, through `tz06.scoring_set` at its defaults | `6d94a346a47a04a1a0849968effd9023d7585fe628b304ba2ae7a15953ee67f9` |
| **test 1** | the TZ-08a 400, through `tz08a.the_set` with every assertion it makes | `3b17729c050e5fbf8fed1bd0877d5dd5c229370609cd672c84eeed1ddc3d5762` |
| **test 2** | the first **400** grid slots with `T0 > 1789296300`, in ascending `T0` order, that qualify under `tz06.qualification` — `tz06.scoring_set(manifests, need=400, after=1789296300)` | **not stated here: this set does not exist yet.** The report states it, computed by `tz07b.member_list_sha` |

The two committed hashes are asserted (V5). **Test 2 cannot be hash-gated in advance and is not**:
anti-cherry-picking is by ordered disclosure of every unit considered, members and non-members
alike, with the reason for each exclusion (CANON hard rule 8). At 2026-09-14 15:45 UTC, `318` of the
400 already qualified (System Map §2.3). If fewer than 400 qualify at run time the run is
**BLOCKED**, stating the count, the last slot on disk and nothing else.

The three sets are asserted pairwise disjoint.

### 3.1 M1 — the link, fitted on the fit set, with no label

For each `tau` in `pfair.TAUS`, over every admissible anchor of every member of the fit set, form

```
r(a, tau) = Y(a, tau) / (sigma * sqrt(H(tau)))
```

through `tz07b.residual` and `tz07b.horizon_sd`, walked exactly as `tz07b.member_r` walks it, with
M6's disconnect rule imported from `tz07a` through `tz07b` and never reimplemented. This is the same
`r` whose root mean square TZ-07b froze as `SD_SCALE` and whose out-of-sample RMS TZ-08a V8
measured: **the quantity is unchanged and only the law fitted to it is new.**

Fit a symmetric Student's `t` with degrees of freedom `ν` and scale `s` by maximum likelihood:

```
log f(r) = lgamma((nu+1)/2) - lgamma(nu/2) - 0.5*log(nu*pi) - log(s)
           - ((nu+1)/2) * log1p((r/s)**2 / nu)
```

- **Arithmetic, fixed here.** Per `tau` and per population, the Decimal `r` values are converted to
  `float` **once**, in ascending `T0` then ascending anchor, into a single `numpy.float64` array
  built before the search starts; every likelihood is one vectorised pass over that array summed by
  `numpy.sum`. The order is fixed by construction, so two runs on this host give bit-identical sums
  (V3). `numpy` is a dependency of the committed stack; if it is absent the run is BLOCKED at §0
  rather than falling back to a loop.
- **Search, fixed here:** `ν` over `[2.05, 60.0]` by golden section to a relative tolerance of
  `1e-8`; at each `ν`, `s` over `[0.10, 10.0]` by golden section to the same tolerance — the profile
  likelihood. Both bounds are reported with the fit; **a `ν̂` or `ŝ` landing on a bound is disclosed
  as such in the same table and is the edge of the search, not a maximiser.**
- **Cost, and the fail-fast** (CANON PART VI C4). One fit is about `2,200` likelihood evaluations —
  45 outer by 48 inner — each over at most `198,000` anchors, so at most `4.4e8` element operations
  per fit. This TZ requires `63` fits in all: `42` primary (six populations by seven `tau`) and `21`
  influence refits (§7 V12). That is at most `2.8e10` element operations, about `550` s at a
  vectorised rate of `5e7` log1p per second, against CANON's ceiling of `3,600` s. **The instrument
  times its first fit and BLOCKS, stating the measured seconds and the projection, if that fit
  exceeds `60` s.**
- **No outcome is read.** M1's input is the feed and the manifests.

Report per `tau`: `n` anchors, `ν̂`, `ŝ`, the log-likelihood at the optimum, the log-likelihood of
the best-fitting *normal* on the same anchors, and `κ` as TZ-10b defines it.

### 3.2 M2 — the domain, measured on the fit set

**The admissibility predicate, fixed here before any data is seen.** A member is **admissible at
`tau`** when its `sigma_hat` at that `tau` — `pfair.realised_sigma` over the causal window, the
identical value the pricer already feeds `corrected_sd` — is at or above `ADMIT[tau]`, where

```
ADMIT[tau] = the 30th percentile of sigma_hat over the 400 members of the fit set at that tau,
             statistics.quantiles(values, n=10, method="inclusive")[2]
```

The threshold is 30 per cent because TZ-10b M3 measured `κ` by decile of `sigma_hat` and the excess
is concentrated in deciles 1 to 3 at every `tau` — `2.611 / 2.514 / 2.108` against a pooled `1.5005`
at `tau = 60`. The rule is causal, needs one comparison at decision time, and costs the pricer 30
per cent of intervals by construction on the fit set. **What it costs on the two test sets is
measured, not assumed, and is reported.**

`ADMIT` is measured on the fit set and on nothing else. It is frozen into `pfair.py` as one Decimal
literal per `tau`, at six significant digits, with a per-`tau` `assert` inside the instrument that
the committed literal equals this run's own measurement to six significant digits before any table
is printed — the pattern TZ-07b §5 established for `SD_SCALE`.

**M1 is then repeated on the admissible members of the fit set**, and those two tables — `ν̂(tau)`
and `ŝ(tau)` — are frozen into `pfair.py` as `LINK_NU` and `LINK_SCALE`, six significant digits,
under the same per-`tau` assert. The all-member fit of §3.1 is reported beside them and **is not
frozen and is not scored.**

The keys of all three tables are exactly `pfair.TAUS`, `10` included. A `tau` with no measured
constant raises inside `student_sd` and inside `p_fair_student` (System Map §7 item 20).

### 3.3 M3 — does the link transfer? The stationarity reading

Refit `ν̂(tau)` and `ŝ(tau)` **independently on test 1 and on test 2**, admissible members only, by
the identical search of §3.1, reading no label. Report both tables beside `LINK_NU` and
`LINK_SCALE`, with `log(ν̂_set / LINK_NU[tau])` in its own column. Report the same three fits over
**all** members of each set, so the effect of the domain rule on the spread is visible.

**Per set before pooled** (System Map §7 item 41): `κ`, `ν̂` and `ŝ` are reported for each of the six
populations separately — fit-all, fit-admissible, test1-all, test1-admissible, test2-all,
test2-admissible — and any pooled figure is printed after them and never instead of them.

This is the reading G4 judges. It is the one property this project has never yet required of a
constant before freezing it.

### 3.4 M4 — the scoring, and a place a label is read

With `ADMIT`, `LINK_NU` and `LINK_SCALE` frozen, score, at the checkpoint of every **admissible**
member of test 1 and of test 2, against the venue's resolved outcome:

```
sd_t     = LINK_SCALE[tau] * sigma * sqrt(H(tau))            # pfair.student_sd(tau, sigma)
p_t      = F_nu(state / sd_t), nu = LINK_NU[tau]             # pfair.p_fair_student(state, sd_t, tau)
```

`state` and `H(tau)` are the committed §1.2 quantities, untouched. Report per set and per `tau`:

1. `Brier` of `p_t`, and of `p_fair` with `corrected_sd` on the identical admissible rows, so the
   two links are compared on one set of observations.
2. The `tz06.calibration` bin table, unmodified, with eligible bins and failing bins counted as
   `tz06` counts them.
3. `λ̂` through `tz07a.lambda_hat` with `log_cdf` bound to the Student log CDF at `LINK_NU[tau]`
   (§5.3), with `ll` at `λ̂` and at `1`, the likelihood ratio and its p-value, **and the value
   recomputed without its single most influential observation** (System Map §7 items 27 and 40).
4. `κ` of `r / ŝ` on the admissible rows.
5. The same five rows on **all** members of each set, reported and not gated, so the cost of the
   domain rule is visible rather than argued.

### 3.5 M5 — the observation the old gate hung on

`T0 1789268400` at `tau = 30`. Report, side by side: `state`, `sd` under `corrected_sd` and under
`student_sd`, `z` under each, `p_fair`, `p_t`, `log Phi(z)`, `log F_nu(z)`, and its contribution to
`ll(λ̂)` and to `ll(1)`.

**The population is named here** (System Map §7 item 48): the `λ̂` whose contribution is reported is
the one fitted in §3.4 item 3 **on the admissible rows of test 1 at `tau = 30`**. The same two
contributions under the all-member `λ̂` of §3.4 item 5 are reported beside them, labelled. Whether
`1789268400` is itself admissible at `tau = 30` is a measurement and is stated; if it is not, the
admissible-row contributions are reported as `not a member` and the all-member pair carries the
section. **No conclusion is drawn from one observation.** It is reported because the whole of System
Map §7 items 26, 27 and 40 rests on it.

---

## 4. The gate, and the verdict

**Fixed here, before test 1 is scored and before test 2 exists. Nothing below is redefined after any
number is known, and nothing is tuned to make it pass.**

Scored `tau`: all seven of `pfair.TAUS`. Every one carries a measured constant, so every one is
gated by G1, G3 and G4 (System Map §7 item 20). Both a scale statistic and a shape statistic are
present (item 15).

| gate | statistic | threshold | judged on |
|---|---|---|---|
| **G1** — discrimination | `Brier` of `p_t` | strictly below `0.2496`, the constant-prediction baseline TZ-06 fixed | every scored `tau`, each test set |
| **G2** — bin calibration | `tz06.calibration`, unmodified | at most `tz06.MAX_FAILING_BINS` = 2 failing bins, summed over `pfair.GATED_TAUS` | **six `tau`, exactly as `tz06.build` pools them**, each test set |
| **G3** — scale | `λ̂` under the Student likelihood | `\|λ̂ − 1\| <= 0.15`, TZ-07a §8's threshold unchanged | every scored `tau`, each test set |
| **G4** — shape transfer | `ν̂` refitted on the set | `\|log(ν̂_set / LINK_NU[tau])\| <= log(2)` | every scored `tau`, each test set |

**G2 pools six `tau` and not seven**, because `tz06.build` sums `failing_bins` over
`pfair.GATED_TAUS` and reports `tau = 10` separately as `V7_tau_10` with no threshold. The `tau = 10`
bin table is reported here the same way: **printed, not pooled, not gated by G2.** G1, G3 and G4 do
score `tau = 10`.

**Why `log(2)` and not a round band.** The two windows already measured differ in implied `ν` by a
factor of `3.64` at `tau = 240` — `17.1` against `4.69` — with no domain rule applied. A factor of 2
is therefore a real requirement: it is passed only if the admissibility rule cuts the measured
spread by more than half. It is derived from measurement, and it was written before the domain rule
had produced a number.

**Any one of G1, G2, G3, G4 violated at either test set closes this pricer.** Phase 1 stays closed
for `p_fair`; this is the Student pricer's own Phase 1, and like every Phase 0 and Phase 1 gate it
**can only disqualify — passing it confirms no edge.**

### 4.1 The pre-registered prediction — the Architect's, `[решение принято мной]`

| quantity | predicted |
|---|---|
| G1 | passes, 7 of 7, on both test sets |
| G2 | passes on both test sets |
| G3 | holds at `tau` 240, 180, 120 and 90 on both sets; fails at 30 or at 10 on at least one |
| G4 | holds at `tau <= 120`; **fails at `tau = 240` on test 1** |
| overall | **NO**, and the failing gate is G4 at long `tau` |

The reasoning, in one line: `ν` is weakly identified where the residual is nearly normal, so the
long-`tau` estimate is the fragile one, and the domain rule attacks the short-`tau` tail rather than
that. Discarded alternative: fit `ν` on the pooled 800 and test on test 2 alone — rejected, because
it spends the only clean stationarity reading this project has in order to buy one extra window of
fit data.

---

## 5. The code

### 5.1 `research/pfair.py` — insertions only, after `log_phi`

**Twelve** new top-level names and nothing else. No existing line is removed or altered.

```
LOG_BETA_CF_MAX = 300          # continued-fraction iterations before raising
LOG_BETA_TOL    = 1e-16        # its relative convergence tolerance

log_beta(a, b)                 lgamma(a) + lgamma(b) - lgamma(a + b)
_betacf(a, b, x)               the modified Lentz continued fraction for I_x(a, b);
                               raises if it has not converged within LOG_BETA_CF_MAX
log_betainc_reg(a, b, x)       log I_x(a, b):
                                 x >= 1                      ->  0.0
                                 x <= 0                      ->  raises
                                 x <  (a + 1)/(a + b + 2)    ->  a*log(x) + b*log1p(-x)
                                                                 - log(a) - log_beta(a, b)
                                                                 + log(_betacf(a, b, x))
                                 otherwise                   ->  log1p(-exp(log_betainc_reg(b, a, 1 - x)))
log_t_cdf(z, nu)               z <= 0 -> log_betainc_reg(nu/2, 0.5, nu/(nu + z*z)) - log(2)
                               z >  0 -> log1p(-exp(log_t_cdf(-z, nu)))
t_cdf(z, nu)                   exp(log_t_cdf(z, nu))
ADMIT, LINK_NU, LINK_SCALE     the three measured tables, Decimal literals, keys = TAUS
student_sd(tau, sigma)         LINK_SCALE[tau] * sigma * H(tau).sqrt(), H as corrected_sd has it
p_fair_student(state, sd, tau) t_cdf(float(state / sd), float(LINK_NU[tau]))
```

That is two constants, five functions, three tables and two functions — **twelve names, counted
here so the count in a report can be checked against it.**

**The tail is accurate by construction, and that is the point of taking the leading factor in
logs.** `phi` was `0.5 * (1 + erf)` and lost the tail to cancellation; `log_betainc_reg` never forms
a probability it then has to take the log of, so `log_t_cdf(-200, 3)` is an ordinary finite number.
`phi`, `log_phi` and `p_fair` are not touched: they are the old link and every committed measurement
is quoted from them.

### 5.2 `research/selftest-pfair.py` — insertions only, family `TZ-11a section 5.2`

Six items, each an `assert` that aborts the file. The existing families are unchanged and their
counts are asserted (V7).

**Item 1 — `log_t_cdf` against 40 fixed literals, to 12 significant digits.** Columns are `z` = `0`,
`−1`, `−3`, `−5`, `−8`, `−10.819`, `−20`, `−50`.

| `ν` | `log F_ν(z)` |
|---|---|
| 2 | `-0.693147180559945` · `-1.55435868307644` · `-3.04213264974235` · `-3.96992886866936` · `-4.87513859809586` · `-5.46847054829007` · `-6.68835316116258` · `-8.51779297152817` |
| 2.5 | `-0.693147180559945` · `-1.59933653536950` · `-3.31626685434013` · `-4.44598122091119` · `-5.56532867478168` · `-6.30324233817012` · `-7.82481099775613` · `-10.1104508277657` |
| 3 | `-0.693147180559945` · `-1.63218922449412` · `-3.54618467545091` · `-4.86702610492042` · `-6.19564464966101` · `-7.07657843379202` · `-8.89844171394626` · `-11.6397847632440` |
| 4 | `-0.693147180559945` · `-1.67691149318135` · `-3.91347485706189` · `-5.58727573561669` · `-7.32032286818778` · `-8.48264615644609` · `-10.9009041296344` · `-14.5521443574038` |
| 7 | `-0.693147180559945` · `-1.74120896160071` · `-4.60806807421352` · `-7.15283904545879` · `-9.99615988572270` · `-11.9667403968485` · `-16.1409126343562` · `-22.5096639254306` |

**The reference, and the margin** (System Map §7 item 37). Every literal was computed by the
Architect at 60 decimal digits by the regularized incomplete beta `I_x(ν/2, 1/2)/2` and
cross-checked at 60 digits by quadrature of the density; the two routes agree to `7.04e-61`
relative. The table was then **re-verified at 60 digits a third time while TZ-11a was written**:
worst relative disagreement across all 40 points `3.97e-15`, which is the accuracy of the printed
15-digit literals themselves. The item's tolerance is `1e-12` relative, so the reference is better
than the tolerance by decades, and no route used is the continued fraction §5.1 implements.

**Item 2 — symmetry.** `exp(log_t_cdf(z, ν)) + exp(log_t_cdf(-z, ν))` equals `1` to 12 significant
digits at `z` in `{0.5, 1, 2, 3, 5}` and `ν` in `{2.5, 3, 7}` — 15 pairs. This exercises the
positive branch and the `log_betainc_reg` symmetry branch, neither of which item 1 reaches.

**Item 3 — the normal limit.** The worst relative gap between `t_cdf(z, 1e6)` and `pfair.phi(z)`
over `z` in `{−3, −2, −1, 0, 1, 2, 3}` is below `1e-4`. **Expected `2.46e-5`**, computed at 60
digits; the bound is a factor of `4.1` above it. The check is confined to `|z| <= 3`, where `phi`
keeps 12 significant digits with margin — `phi` is never the reference in the region that motivated
replacing it (System Map §7 item 34).

**Item 4 — shape.** `log_t_cdf(·, ν)` is strictly increasing over `−60 … 5` at 65,001 points and
finite at every one of 40,001 points over `−200 … 200`, at each `ν` in `{2.05, 3, 60}` separately.

**Item 5 — the pathology removed, at live scale. Two asserts, and neither reads a table this TZ
measures** (System Map §7 item 45). At `K = 100000.25`, `sigma = 3.25`, `tau = 30`, with
`sd = pfair.corrected_sd(30, sigma)` — the committed, frozen scale — and `S_t = K + D("-10.819") *
sd`, so that `state, _ = state_and_sd(30, S_t, K, sigma, S_t)` gives `z = float(state / sd)` exactly
`-10.819`:

- **5a, against literals, with `ν` written in the call.** `pfair.p_fair(state, sd)` is exactly `0.0`
  and `math.log` of it is not finite; `t_cdf(z, 3.0)` is `8.4465826393e-04` to 10 significant digits
  and `log_t_cdf(z, 3.0)` is `-7.07657843379202` to 12 significant digits. Both literals come from
  item 1's reference and neither depends on anything this TZ measures.
- **5b, against the pricer's own function, as an inequality that holds for every admissible `ν`.**
  `p_t = pfair.p_fair_student(state, sd, 30)`, which reads the frozen `LINK_NU[30]`, satisfies
  `0.0 < p_t < 1e-2`, and `pfair.log_t_cdf(z, float(pfair.LINK_NU[30]))` is finite and lies strictly
  between `-40.0` and `-5.0`. §3.1's search returns `ν` in `[2.05, 60.0]` and nowhere else; over
  that whole interval the Architect computed at 60 digits `F_ν(-10.819)` ∈ `[4.99e-16, 3.87e-3]` and
  `log F_ν(-10.819)` ∈ `[-35.24, -5.556]`, so both bounds hold for every value the fit can produce,
  with a factor of `2.6` of margin at the upper end and `0.556` and `4.76` at the two log ends.
  **`sd` is the committed `corrected_sd` and not `student_sd`, so `z` is fixed at `-10.819`
  whatever `LINK_SCALE[30]` turns out to be**, and only `ν` moves the value.

**Item 6 — the tables.** The keys of `ADMIT`, `LINK_NU` and `LINK_SCALE` are exactly `pfair.TAUS`;
`student_sd` and `p_fair_student` each raise on a `tau` that is not in them; and
`student_sd(30, D("3.25"))` equals `LINK_SCALE[30] * D("3.25") * (D(30) ** 3 / D(10800)).sqrt()`
recomputed from the table — an identity between the function and its own table, carrying no value.

### 5.3 `research/tz07a-variance-time.py` — insertions, plus four replaced lines

System Map §7 items 43 and 46. `log_likelihood` and `lambda_hat` each gain a keyword parameter
`log_cdf=None`.

**The four committed lines this change replaces, read from `origin/main` at `ecc5a0b`, by number and
by text** (CANON PART VI C3):

| line | committed text | after |
|---|---|---|
| 270 | `def log_likelihood(pairs, lam):` | `def log_likelihood(pairs, lam, log_cdf=None):` |
| 282 | `def lambda_hat(pairs):` | `def lambda_hat(pairs, log_cdf=None):` |
| 292 | `        if log_likelihood(pairs, a) < log_likelihood(pairs, b):` | the same with `, log_cdf` in both calls |
| 297 | `    ll_hat, ll_one = log_likelihood(pairs, lam), log_likelihood(pairs, 1.0)` | the same with `, log_cdf` in both calls |

**No other line is replaced**, and in particular line 274, `        p = pfair.phi(z / lam)`, is
untouched: the substitution is a four-line insertion at the top of the loop body, immediately after
`    for z, y in pairs:` —

```
        if log_cdf is not None:
            u = z / lam
            total += log_cdf(u) if y else log_cdf(-u)
            continue
```

- **`log_cdf=None` is the committed path, byte-for-byte**: the `Φ` expression is never entered when
  the parameter is given and is never edited when it is not. V4 asserts that at the default
  `lambda_hat` returns TZ-08a's `2.0418426092` at `tau = 30` on the TZ-08a 400, to ten decimals.
- When `log_cdf` is given, the two terms become `log_cdf(u)` for a resolved-Up label and
  `log_cdf(-u)` for a resolved-Down label, where `u = z / lam`. **Both links are symmetric**, so that
  substitution is exact for `Φ` and for `F_ν` alike; the TZ states it rather than leaving it to be
  inferred.
- The search interval `[0.5, 3.0]`, the tolerance `1e-9` and the returned fields are the committed
  ones and are not parameters.
- **No name is rebound at run time anywhere in this TZ**, and V6 asserts that the instrument
  contains no assignment to an attribute of an imported module.

---

## 6. Retention

System Map §6 and TZ-09 §5 are unchanged and govern. The capture is never deleted. This run's
scratch is `/root/tz11a-work/`, reclaimed by the next TZ once this report is on `main`, and every
file this report names by SHA-256 is copied to `/root/btc-forensics/` first, by exclusive create,
with each hash asserted equal at source and destination.

`/root/tz10b-work/` and `/root/tz11-work/` are reclaimed by §9, in that order, after the copies.

---

## 7. Validation

Each check states its count. "All checks passed" is not a result.

- **V1 — gates.** The fingerprint table of map §0 recomputed row by row, the frozen count asserted;
  the six anchors; the three host checks; the resource floor at run start and at every later read,
  each an `assert`. Report every free-space read with its UTC timestamp.
- **V2 — causality, by perturbation.** The tested quantity is **`sigma_hat` and
  `pfair.student_sd(tau, sigma_hat)`, and nothing else** — the causal inputs to `p_t`. `Y`, `r`,
  `ν̂`, `ŝ` and every realised outcome are **exempt and are named exempt here**: each is a function of
  the future by construction (System Map §7 item 36). Over the first 20 members of the fit set at all
  seven `tau`, multiply by `tz06.PERTURBATION` every `chainlink` report stamped **strictly after**
  `T0 + (300 − tau)` through `tz06.perturb_after`, and require both quantities bit-identical.
  Negative control: `tz06.perturb_one` on `tz06.last_readable` must move both. Before counting,
  assert per checkpoint that the control's report lies outside the perturbed set and that at least
  one report was perturbed. **140 of 140 both ways.**
- **V3 — determinism.** Two full runs from fresh processes on the same commit; every output except
  the host file byte-identical, asserted by the report's assembler on SHA-256.
- **V4 — the instrument reproduces what is committed. Four assertions, each a count:**
  1. TZ-07b's `Λ` at **7 of 7** on the fit set, from this instrument's own walk of `r`;
  2. TZ-08a V8's seven `RMS(u)` at **7 of 7**, from the same walk;
  3. `tz07a.lambda_hat` at its default returning `2.0418426092` at `tau = 30` on the TZ-08a 400
     — **this reads those 400 labels and §2 names it as the third place an outcome is read**;
  4. the committed `tz07b.member_r` called beside this run's walk on **50 members**, with every `r`,
     the Decimal sum of squares, the dropped count and the checkpoint `r` identical (System Map §7
     item 24).
  **The 50 are defined here and counted over two sets only** (System Map §7 item 48): the first 20
  members of the **fit set**, plus every member of the **fit set** and of **test 1** for which
  `tz07a.excluded_seconds` is non-empty. Test 2 is not in this rule. At authoring time that is
  `20 + 15 + 16 − 1 = 50`, the one overlap being `1789035900`, which is among the first 20. The run
  re-derives the count, reports the member list in ascending `T0`, and **asserts it equals 50**; if
  it does not, the run is BLOCKED stating the three components.
- **V5 — set identity.** The two committed member-list hashes asserted equal to §3.0's values; test
  2's hash computed and reported; the three sets asserted pairwise disjoint. **2 asserted, 1
  reported.**
- **V6 — the diff, in its real shape.** `git status --porcelain` empty for the five paths. Against
  `git merge-base HEAD main`: `pfair.py` and `selftest-pfair.py` hold **insertions only**;
  `tz07a-variance-time.py` holds insertions **plus exactly four removed lines**, and the set of
  removed lines is asserted equal, string for string, to the four texts §5.3 names. Every top-level
  object each file held before is asserted byte-identical after by its exact source text through
  `ast` — naming `SD_SCALE`, `corrected_sd`, `phi`, `log_phi`, `p_fair`, `far_branch`,
  `near_branch`, `state_and_sd`, `TAUS` and `GATED_TAUS` explicitly, except `tz07a.log_likelihood`
  and `tz07a.lambda_hat`, whose diffs are printed in full in the report. Assert that the instrument
  contains no assignment to an attribute of an imported module.
- **V7 — the self-tests.** `selftest-pfair.py` run as a subprocess, exit status 0, with the family
  counts asserted: `TZ-07b section 6` 30, `TZ-10b section 5.2` 6, `TZ-11a section 5.2` 6, `V5` 56,
  `section 3 machinery` 18 — **116 in all**, against the **110** the file holds today. The six new
  items' output is printed verbatim.
- **V8 — the frozen literals.** For each of `ADMIT`, `LINK_NU` and `LINK_SCALE`, and for each `tau`,
  assert the committed literal equals this run's own measurement to six significant digits,
  **before any table is printed**. **21 of 21.**
- **V9 — the capture is untouched.** At the start and end of each full run: the same recorder pid;
  the same newest start record, sha and `recv_ns`; an interval count that does not fall; and an
  equal SHA-256 over the name, size and modification time of every file in every interval directory
  the run reads. Enumerate what the instrument can write — files, subprocesses with their exact argv
  and the absence of a shell, and its read paths — as System Map §7 item 32 requires.
- **V10 — the fingerprint table**, every row, in lines, bytes and SHA-256, with the four changed or
  added rows reported beside them as they stand on the branch.
- **V11 — disclosure.** Every unit each of the three walks considered, in order, members and
  non-members alike, with the reason for each non-member; then every member's admissibility at every
  `tau`, with its `sigma_hat` and the `ADMIT[tau]` it was compared against.
- **V12 — influence, defined here and priced here** (System Map §7 items 27, 40 and 47).
  1. For `λ̂`: every reported `λ̂` is accompanied by its value recomputed without its single most
     influential observation, that observation named by `T0`, label and `z`. Influence is the
     observation's own contribution to `ll(λ̂) − ll(1)`, and the recomputation is an exact refit.
     This is cheap: `lambda_hat` searches one dimension over at most 400 pairs.
  2. For `ν̂`: **influence of a member is its own contribution to the log-likelihood at `(ν̂, ŝ)`**,
     summed over that member's anchors, and the reported figure is **one exact refit with the single
     largest-magnitude contributor removed** — not a leave-one-out sweep. One refit per population
     per `tau`, applied to the three admissible populations only: `21` refits, inside §3.1's cost
     statement.
  3. Both are **recorded, not asserted**, and neither moves a gate: G3 and G4 are judged on the
     values §4 defines.

---

## 8. The report

`CryptoReports/TZ-11a-student-link-and-domain-report.md`, structure `## 0` … `## 6`: `0`
fingerprint, host and every free-space read; `1` the measurements in §3's order, per set before
pooled; `2` the gate tables and the prediction; `3` the implementation and the three frozen tables;
`4` validation V1 … V12; `5` publication; `6` what could not be implemented as written and every
reading chosen. Section numbers asserted unique. **There is no verdict section: §4's verdict is the
Architect's.**

The report states its own line count and SHA-256 for every file in map §0's fingerprint table.

---

## 9. Publication

Branch `tz-11a-student-link`, one commit, four files, pushed; a pull request against `main`, **not
merged** — merge is the Boss's, after the Architect's verdict. The report goes straight to `main`.
Run the contract §4.2 separation self-check verbatim and print all three results. No Release, no
dataset, no archive, no binary in git history.

**Before anything is reclaimed**, copy into `/root/btc-forensics/` every file a committed report
names by SHA-256 that is not already there, asserting each hash at both ends and asserting that
every file already in that tree is unchanged. Then reclaim `/root/tz10b-work/` and `/root/tz11-work/`,
one command naming one tree each, and verify with `test -e` rather than from any report.

---

## 10. Pre-send checks

CANON PART VI, performed against this file, start to end, as a separate reading.

- **C1 — scope against body.** 21 repository paths and committed entry points enumerated from the
  body: the five paths of §2; `pfair.py`'s ten named objects; `tz06.qualification`,
  `tz06.scoring_set`, `tz06.calibration`, `tz06.build`, `tz06.perturb_after`, `tz06.perturb_one`,
  `tz06.last_readable`; `tz07a.excluded_seconds`, `tz07a.log_likelihood`, `tz07a.lambda_hat`;
  `tz07b.residual`, `tz07b.member_r`, `tz07b.horizon_sd`, `tz07b.member_list_sha`;
  `tz08a.the_set`; `/var/lib/btc-recorder/**`, `/root/tz04a-env/`, `/root/btc-forensics/`,
  `/root/tz10b-work/`, `/root/tz11-work/`. **Three intersections with §2's prohibition list, all
  three written into §2 as named exemptions:** `/root/btc-forensics/` for §9's copies;
  `tz06.qualification`'s outcome reads; and **V4 assertion 3**, which was the unnamed one in TZ-11.
- **C2 — origin of every expectation.** 47 fixed literals. 40 are item 1's table, computed at 60
  digits by two independent routes and re-verified a third time (worst `3.97e-15` against a `1e-12`
  tolerance). 4 are quoted from committed artifacts by name: `2.0418426092` (TZ-08a),
  `0.2496` (TZ-06), `1.38581` via `corrected_sd` (TZ-07b), `2.46e-5` (computed at 60 digits). 3 are
  item 5b's inequality bounds, each verified against the extremes of §3.1's search range. **Zero
  literals depend on a quantity this TZ measures** — TZ-11's item 5 was the one that did, and it is
  now split into 5a and 5b.
- **C3 — shape of every diff.** `pfair.py`: none replaced. `selftest-pfair.py`: none replaced.
  `tz07a-variance-time.py`: **four replaced lines — 270, 282, 292, 297** — named by text in §5.3 and
  asserted as a set by V6. The words "insertions only" appear in §2 and §5.1 for the two files where
  the list is empty, and nowhere else.
- **C4 — cost of every check.** The only cost that grows with the data is the profile fit: `63` fits,
  about `2,200` likelihood evaluations each, at most `198,000` anchors per evaluation — at most
  `2.8e10` element operations, about `550` s at `5e7` log1p per second, against a `3,600` s ceiling.
  A fail-fast BLOCKS the run if the first fit exceeds `60` s. Every other check is bounded by the
  400-member sets or by fixed point counts (65,001 and 40,001 in item 4).
- **C5 — every count.** `140` = 20 members × 7 `tau` (V2). `50` = 20 + 15 + 16 − 1 over the fit set
  and test 1, re-derived at run time (V4). `21` = 3 tables × 7 `tau` (V8). `116` = 30 + 6 + 6 + 56 +
  18 (V7), against the 110 the file holds today. `63` = 42 + 21 fits (§3.1, V12). `7 of 7` and
  `6 of 6` in V4 are `pfair.TAUS` and TZ-08a V8's six ratios. `12` names in §5.1, enumerated in the
  section.
- **C6 — every population.** M1: anchors of the fit set, all and admissible. M2: the 400 fit members
  at each `tau`. M3: six populations, named one by one in §3.3. M4: admissible checkpoints of test 1
  and of test 2, and all checkpoints of each. M5: **the admissible rows of test 1 at `tau = 30`**,
  with the all-member value beside it. G2: `pfair.GATED_TAUS`, six `tau`.
- **C7 — every signature.** 30 committed names read from `origin/main` at `ecc5a0b` and quoted in
  §2 as the files hold them, including the two this TZ changes. `corrected_sd(tau, sigma)` takes
  `tau` first; `scoring_set`'s `after` is keyword-only; `state_and_sd`'s `m_r` defaults to `None`.
- **C8 — every cross-reference.** 24 references resolved by reading the referenced text: CANON hard
  rules 4 and 8, CANON PART VI C2–C6, PART III's model-selection and audit rules; System Map §0,
  §2.3, §3, §6 and §7 items 15, 20, 23, 24, 26, 27, 29, 32, 34–37, 39–41, 43–48; the Executor
  contract §4.2 and §6. Each supports the sentence that makes it. **§7 item 20's rule — every `tau`
  a gate scores carries a measured constant — is satisfied at `tau = 10`: it carries `ADMIT`,
  `LINK_NU` and `LINK_SCALE` and is scored by G1, G3 and G4; G2 does not score it, matching
  `tz06.build`.**
