# TZ-11 — the Student link and the domain it is priced on

**Canonical filename: `TZ-11-student-link-and-domain.md`.** The Executor names the committed file
from this line and from nothing else.

**Executor model: Opus.** This touches the §1.2 link, gate arithmetic and a frozen pricer.

---

## 0. Fingerprint gate, host gate, resource floor

The Executor compares every row below before doing any work. A mismatch on any one is **BLOCKED**
before the first file is read.

**Required System Map revision:** `2026-09-14-d`.

| anchor | required |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-answered-no / 2-not-started` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` |
| `A6` — pricer | `45b307b221d4` |

`A6` is `research/pfair.py` after PR #11. **This TZ scores a pricer and moves `A6`**; the report
states the value before and after.

**Host gate.** All three, or this is not the capture host and the run is BLOCKED:

1. `/var/lib/btc-recorder/btc-updown-5m/` exists and holds interval directories.
2. The recorder process is running and the newest `runtime.jsonl` start record carries sha
   `4216c04673ced76b5b2ac60ef57c9abedc46f9b9`.
3. The filesystem holding it is `/dev/vda2`, total `31,612,203,008` bytes.

**Resource floor, in exact bytes, derived from System Map §6.**

- Free space at run start, on `/dev/vda2`: at least **`2,060,000,000`** bytes — the map's own
  project floor `2,000,000,000` plus `60,000,000` for this run's scratch, which is
  `20,221,952` measured for TZ-10b scaled by the 1.5× larger observations file and doubled for two
  full runs.
- Free space at every later read, asserted by the instrument: at least **`2,000,000,000`** bytes.
- Both are `assert`s that abort the run, not comparisons made by reading. Every read is reported
  with its UTC timestamp.

**Host preflight, reported and gating nothing beyond the floor.** System Map §6 records that the
Boss stopped `telemetry-watch.service`, terminated the logging processes and purged the `.pcap`
files, and records that as **reported, not measured**. This TZ measures it. At run start and again
at least `1,800` s later, take and report: `df -B1 /dev/vda2`; `du -x -B1 -s
/root/PROJECT_GAMING_PS5`; and `systemctl is-enabled telemetry-watch.service` together with
`systemctl is-active telemetry-watch.service`, each captured with its exit status rather than
asserted. Report the implied bytes/day of both the tree and of free space, and state this run's own
scratch separately (System Map §7 item 29). **No file of that project is opened**; names, sizes and
modification times only.

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
`F_3(−10.819)` is `8.4465826393e-04` and its log is `−7.0765784338`.

**Second, the domain.** Every per-`tau` constant this project has frozen has failed to transfer
between two adjacent day-and-a-half windows — `G_RATIO`, then `SD_SCALE`, and now `κ` itself,
whose implied `ν` is `17.06` on the TZ-06 window against `4.69` on the TZ-08a window at
`tau = 240`. A fourth constant fitted over all members would fail the same way. TZ-10b M3 shows
where the instability lives: the heavy tail sits in the **low-`sigma_hat`** deciles — `κ` `3.227`
in decile 1 against `1.119` in decile 10 at `tau = 30`. `sigma_hat` is causal and known at
decision time, so it can be an admissibility rule rather than a lament. **A pricer that declines
to quote is a pricer; a pricer that quotes a number it cannot stand behind is not.**

This TZ fits both on the TZ-06 400 alone and scores them on **two** disjoint out-of-sample sets.
Nothing is re-fitted afterwards. `SD_SCALE`, `corrected_sd`, `phi`, `p_fair`, `state` and TZ-07a
§8's threshold do not move.

---

## 2. Scope

**Repository paths this TZ authorizes to change, and no others:**

| path | change | current state in map §0 |
|---|---|---|
| `research/pfair.py` | additive only: §5.1's new names | `frozen`, anchor `A6` — moves |
| `research/selftest-pfair.py` | additive only: §5.2's family | `frozen` — moves |
| `research/tz07a-variance-time.py` | additive only: §5.3's one keyword parameter on two functions | `frozen` — moves |
| `research/tz11-student-link.py` | new: the instrument | does not exist |
| `CryptoReports/TZ-11-student-link-and-domain-report.md` | new | does not exist |

Every `frozen` row this TZ moves is named here by path, and the map's next revision carries each
new line count, byte count and hash (System Map §7 item 35).

**What may not be touched, and the exemptions, named here in this section** (System Map §7 items
23, 39 and 44):

- `/var/lib/btc-recorder/**` — read-only, always. No exemption.
- The recorder process — never signalled, never restarted. No exemption.
- `/root/tz04a-env/` and `/root/btc-forensics/` — **exempt for §9's copies alone**, which add
  files by exclusive create (`open(..., "xb")`) and overwrite nothing. Nothing else in either tree
  may be created, altered or removed.
- Every other committed file, including every report and every other `research/` script.
- **`SD_SCALE`, `corrected_sd`, `phi`, `p_fair`, `far_branch`, `near_branch`, `state_and_sd` and
  `TAUS` in `pfair.py` are byte-identical after this TZ**, asserted by V6.

**Outcomes.** `resolution.json`, `resolved_up` and `priceToBeat` are read in exactly two places,
and both are named here: inside `tz06.qualification`, which every set-formation call reaches for
every unit it considers, member and non-member alike; and inside **M4 and M5**, which are the
only places a label enters a number this TZ prints. **M1, M2, M3 and the whole of §5 read no
outcome of any kind.** M5 needs the label because it reports a likelihood contribution; that is
stated here rather than left to be inferred from §3.5.

**Signatures, as the files hold them.** `pfair.corrected_sd(tau, sigma)` — `tau` first.
`pfair.state_and_sd(tau, s_t, k, sigma, m_r=None)`. `pfair.p_fair(state, sd)`.
`pfair.realised_sigma(grid)`. `pfair.observations(t0, s1_rows, s3_rows, taus=TAUS)`.
`tz06.scoring_set(manifests, need=SET_SIZE, *, after=None)` — `after` is keyword-only.
`tz07a.excluded_seconds(t0, manifests)`. `tz07a.lambda_hat(pairs)`.
`tz07b.residual(rows, keys, t0, grid, a, tau)`. `tz07b.member_r(t0, manifests)`.
`tz07b.horizon_sd(tau, sigma)`. `tz07b.member_list_sha(members)`. `tz08a.the_set(manifests)`.

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
alike, with the reason for each exclusion (CANON hard rule 8). If fewer than 400 qualify at run
time the run is **BLOCKED**, stating the count, the last slot on disk and nothing else.

The three sets are asserted pairwise disjoint.

### 3.1 M1 — the link, fitted on the fit set, with no label

For each `tau` in `pfair.TAUS`, over every admissible anchor of every member of the fit set, form

```
r(a, tau) = Y(a, tau) / (sigma * sqrt(H(tau)))
```

through `tz07b.residual` and `tz07b.horizon_sd`, walked exactly as `tz07b.member_r` walks it, with
M6's disconnect rule imported from `tz07a` through `tz07b` and never reimplemented. This is the
same `r` whose root mean square TZ-07b froze as `SD_SCALE` and whose out-of-sample RMS TZ-08a V8
measured: **the quantity is unchanged and only the law fitted to it is new.**

Fit a symmetric Student's `t` with degrees of freedom `ν` and scale `s` by maximum likelihood:

```
log f(r) = lgamma((nu+1)/2) - lgamma(nu/2) - 0.5*log(nu*pi) - log(s)
           - ((nu+1)/2) * log1p((r/s)**2 / nu)
```

- **Search, fixed here:** `ν` over `[2.05, 60.0]` by golden section to a relative tolerance of
  `1e-9`; at each `ν`, `s` over `[0.10, 10.0]` by golden section to the same tolerance — the
  profile likelihood. Both bounds are reported with the fit; **a `ν̂` or `ŝ` landing on a bound is
  disclosed as such in the same table and is the edge of the search, not a maximiser.**
- The log-likelihood is accumulated in ascending `T0`, then ascending anchor, so the sum is
  determinate. `float` throughout; the inputs are the Decimal `r` converted once, at the point of
  accumulation, and the conversion is stated.
- **No outcome is read.** M1's input is the feed and the manifests.

Report per `tau`: `n` anchors, `ν̂`, `ŝ`, the log-likelihood at the optimum, the log-likelihood of
the best-fitting *normal* on the same anchors, and `κ` as TZ-10b defines it. Report the same table
for the admissible subset of the fit set once §3.2 has it.

### 3.2 M2 — the domain, measured on the fit set

**The admissibility predicate, fixed here before any data is seen.** A member is **admissible at
`tau`** when its `sigma_hat` at that `tau` — `pfair.realised_sigma` over the causal window, the
identical value the pricer already feeds `corrected_sd` — is at or above `ADMIT[tau]`, where

```
ADMIT[tau] = the 30th percentile of sigma_hat over the 400 members of the fit set at that tau,
             statistics.quantiles(values, n=10, method="inclusive")[2]
```

The threshold is 30 per cent because TZ-10b M3 measured `κ` by decile of `sigma_hat` and the
excess is concentrated in deciles 1 to 3 at every `tau` — `2.611 / 2.514 / 2.108` against a pooled
`1.5005` at `tau = 60`. The rule is causal, needs one comparison at decision time, and costs the
pricer 30 per cent of intervals by construction on the fit set. **What it costs on the two test
sets is measured, not assumed, and is reported.**

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

This is the reading G4 judges. It is the one property this project has never yet required of a
constant before freezing it.

### 3.4 M4 — the scoring, the only place a label is read

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
`student_sd`, `z` under each, `p_fair`, `p_t`, `log Phi(z)`, `log F_nu(z)`, and each one's
contribution to `ll(λ̂)` and to `ll(1)`. **No conclusion is drawn from one observation.** It is
reported because the whole of System Map §7 items 26, 27 and 40 rests on it and the reader must
see what the new link does with it.

---

## 4. The gate, and the verdict

**Fixed here, before test 1 is scored and before test 2 exists. Nothing below is redefined after
any number is known, and nothing is tuned to make it pass.**

Scored `tau`: all seven of `pfair.TAUS`. Every one carries a measured constant, so every one is
gated (System Map §7 item 20). Both a scale statistic and a shape statistic are present (item 15).

| gate | statistic | threshold | judged on |
|---|---|---|---|
| **G1** — discrimination | `Brier` of `p_t` | strictly below `0.2496`, the constant-prediction baseline TZ-06 fixed | every scored `tau`, each test set |
| **G2** — bin calibration | `tz06.calibration`, unmodified | at most `tz06.MAX_FAILING_BINS` = 2 failing bins of the eligible bins | each test set, pooled over `tau` as TZ-06 pools it |
| **G3** — scale | `λ̂` under the Student likelihood | `\|λ̂ − 1\| <= 0.15`, TZ-07a §8's threshold unchanged | every scored `tau`, each test set |
| **G4** — shape transfer | `ν̂` refitted on the set | `\|log(ν̂_set / LINK_NU[tau])\| <= log(2)` | every scored `tau`, each test set |

**Why `log(2)` and not a round band.** The two windows already measured differ in implied `ν` by a
factor of `3.64` at `tau = 240` — `17.06` against `4.69` — with no domain rule applied. A factor of
2 is therefore a real requirement: it is passed only if the admissibility rule cuts the measured
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
long-`tau` estimate is the fragile one, and the domain rule attacks the short-`tau` tail rather
than that. Discarded alternative: fit `ν` on the pooled 800 and test on test 2 alone — rejected,
because it spends the only clean stationarity reading this project has in order to buy one extra
window of fit data.

---

## 5. The code

### 5.1 `research/pfair.py` — additive, after `log_phi`

Eleven new top-level names and nothing else. No existing line is removed or altered.

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

**The tail is accurate by construction, and that is the point of taking the leading factor in
logs.** `phi` was `0.5 * (1 + erf)` and lost the tail to cancellation; `log_betainc_reg` never
forms a probability it then has to take the log of, so `log_t_cdf(-200, 3)` is an ordinary finite
number. `phi`, `log_phi` and `p_fair` are not touched: they are the old link and every committed
measurement is quoted from them.

### 5.2 `research/selftest-pfair.py` — additive, family `TZ-11 section 5.2`

Six items, each an `assert` that aborts the file. The existing families are unchanged and their
counts are asserted (V7).

**Item 1 — `log_t_cdf` against 40 fixed literals, to 12 significant digits.** Columns are `z` =
`0`, `−1`, `−3`, `−5`, `−8`, `−10.819`, `−20`, `−50`.

| `ν` | `log F_ν(z)` |
|---|---|
| 2 | `-0.693147180559945` · `-1.55435868307644` · `-3.04213264974235` · `-3.96992886866936` · `-4.87513859809586` · `-5.46847054829007` · `-6.68835316116258` · `-8.51779297152817` |
| 2.5 | `-0.693147180559945` · `-1.59933653536950` · `-3.31626685434013` · `-4.44598122091119` · `-5.56532867478168` · `-6.30324233817012` · `-7.82481099775613` · `-10.1104508277657` |
| 3 | `-0.693147180559945` · `-1.63218922449412` · `-3.54618467545091` · `-4.86702610492042` · `-6.19564464966101` · `-7.07657843379202` · `-8.89844171394626` · `-11.6397847632440` |
| 4 | `-0.693147180559945` · `-1.67691149318135` · `-3.91347485706189` · `-5.58727573561669` · `-7.32032286818778` · `-8.48264615644609` · `-10.9009041296344` · `-14.5521443574038` |
| 7 | `-0.693147180559945` · `-1.74120896160071` · `-4.60806807421352` · `-7.15283904545879` · `-9.99615988572270` · `-11.9667403968485` · `-16.1409126343562` · `-22.5096639254306` |

**The reference, and the margin** (System Map §7 item 37). Every literal was computed by the
Architect at 60 decimal digits **twice, by two implementations that share no code path**: the
regularized incomplete beta `I_x(ν/2, 1/2)/2`, and 60-digit numerical quadrature of the density
over `(−∞, z]`. The two routes disagree by at most `7.04e-61` relative across all 40 points. The
item's tolerance is `1e-12` relative, so the reference is better than the tolerance by 48 decades,
and neither route is the continued fraction §5.1 implements.

**Item 2 — symmetry.** `exp(log_t_cdf(z, ν)) + exp(log_t_cdf(-z, ν))` equals `1` to 12 significant
digits at `z` in `{0.5, 1, 2, 3, 5}` and `ν` in `{2.5, 3, 7}` — 15 pairs. This exercises the
positive branch and the `log_betainc_reg` symmetry branch, neither of which item 1 reaches.

**Item 3 — the normal limit.** The worst relative gap between `t_cdf(z, 1e6)` and `pfair.phi(z)`
over `z` in `{−3, −2, −1, 0, 1, 2, 3}` is below `1e-4`. **Expected `2.46e-5`**, computed at 60
digits; the bound is a factor of `4.1` above it. The check is confined to `|z| <= 3`, where `phi`
keeps 12 significant digits with margin — `phi` is never the reference in the region that
motivated replacing it (System Map §7 item 34).

**Item 4 — shape.** `log_t_cdf(·, 3)` is strictly increasing over `−60 … 5` at 65,001 points and
finite at every one of 40,001 points over `−200 … 200`, at `ν` in `{2.05, 3, 60}`.

**Item 5 — the pathology removed, at live scale.** At `K = 100000.25`, `sigma = 3.25`, `tau = 30`,
built through `state_and_sd`, `student_sd` and `p_fair_student` at `ν = 3`: at the `S_t` that
recovers `z = −10.819`, `p_fair` is exactly `0.0` and its log is not finite, while `p_t` is
`8.4465826393e-04` to 10 significant digits and `log_t_cdf` is `-7.07657843379202`. The literals
come from item 1's reference.

**Item 6 — the tables.** The keys of `ADMIT`, `LINK_NU` and `LINK_SCALE` are exactly `pfair.TAUS`,
and `student_sd` and `p_fair_student` each raise on a `tau` that is not in them.

### 5.3 `research/tz07a-variance-time.py` — additive, one keyword parameter

System Map §7 item 43. `log_likelihood` and `lambda_hat` each gain a keyword parameter
`log_cdf=None`.

- **`log_cdf=None` is the committed path, byte-for-byte**: the expression `tz07a` holds today is
  not edited, only guarded by the branch. V4 asserts that at the default `lambda_hat` returns
  TZ-08a's `2.0418426092` at `tau = 30` on the TZ-08a 400, to ten decimals.
- When `log_cdf` is given, the two terms become `log_cdf(u)` for a resolved-Up label and
  `log_cdf(-u)` for a resolved-Down label, where `u = z / lam`. **Both links are symmetric**, so
  that substitution is exact for `Φ` and for `F_ν` alike; the TZ states it rather than leaving it
  to be inferred.
- The search interval `[0.5, 3.0]`, the tolerance `1e-9` and the returned fields are the committed
  ones and are not parameters.
- **No name is rebound at run time anywhere in this TZ**, and V6 asserts that the instrument
  contains no assignment to an attribute of an imported module.

---

## 6. Retention

System Map §6 and TZ-09 §5 are unchanged and govern. The capture is never deleted. This run's
scratch is `/root/tz11-work/`, reclaimed by the next TZ once this report is on `main`, and every
file this report names by SHA-256 is copied to `/root/btc-forensics/` first, by exclusive create,
with each hash asserted equal at source and destination.

---

## 7. Validation

Each check states its count. "All checks passed" is not a result.

- **V1 — gates.** The fingerprint table of map §0 recomputed row by row, the frozen count
  asserted; the six anchors; the three host checks; the resource floor at run start and at every
  later read, each an `assert`. Report every free-space read with its UTC timestamp.
- **V2 — causality, by perturbation.** The tested quantity is **`sigma_hat` and
  `pfair.student_sd(tau, sigma_hat)`, and nothing else** — the causal inputs to `p_t`. `Y`, `r`,
  `ν̂`, `ŝ` and every realised outcome are **exempt and are named exempt here**: each is a function
  of the future by construction (System Map §7 item 36). Over the first 20 members of the fit set
  at all seven `tau`, multiply by `tz06.PERTURBATION` every `chainlink` report stamped **strictly
  after** `T0 + (300 − tau)` through `tz06.perturb_after`, and require both quantities
  bit-identical. Negative control: `tz06.perturb_one` on `tz06.last_readable` must move both.
  Before counting, assert per checkpoint that the control's report lies outside the perturbed set
  and that at least one report was perturbed. **140 of 140 both ways.**
- **V3 — determinism.** Two full runs from fresh processes on the same commit; every output except
  the host file byte-identical, asserted by the report's assembler on SHA-256.
- **V4 — the instrument reproduces what is committed.** Four assertions, each a count: TZ-07b's
  `Λ` at 7 of 7 on the fit set and TZ-08a V8's seven `RMS(u)` at 7 of 7, both from this
  instrument's own walk of `r`; `tz07a.lambda_hat` at its default returning `2.0418426092` at
  `tau = 30` on the TZ-08a 400; and the committed `tz07b.member_r` called beside this run's walk on
  50 members — the first 20 of the fit set plus every member whose grid M6 drops a second of —
  with every `r`, the Decimal sum of squares, the dropped count and the checkpoint `r` identical
  (System Map §7 item 24).
- **V5 — set identity.** The two committed member-list hashes asserted equal to §3.0's values;
  test 2's hash computed and reported; the three sets asserted pairwise disjoint. **2 asserted, 1
  reported.**
- **V6 — additive only.** `git status --porcelain` empty for the four files; the diff against
  `git merge-base HEAD main` holds insertions only for the three that already exist; every
  top-level object each of them held before asserted byte-identical after by its exact source text
  through `ast` — naming `SD_SCALE`, `corrected_sd`, `phi`, `p_fair`, `far_branch`, `near_branch`,
  `state_and_sd` and `TAUS` explicitly, except `tz07a.log_likelihood` and `tz07a.lambda_hat`,
  whose diffs are printed in full in the report. Assert that the instrument contains no assignment
  to an attribute of an imported module.
- **V7 — the self-tests.** `selftest-pfair.py` run as a subprocess, exit status 0, with the family
  counts asserted: `TZ-07b section 6` 30, `TZ-10b section 5.2` 6, `TZ-11 section 5.2` 6, `V5` 56,
  `section 3 machinery` 18 — **116 in all**. The six new items' output is printed verbatim.
- **V8 — the frozen literals.** For each of `ADMIT`, `LINK_NU` and `LINK_SCALE`, and for each
  `tau`, assert the committed literal equals this run's own measurement to six significant digits,
  **before any table is printed**. **21 of 21.**
- **V9 — the capture is untouched.** At the start and end of each full run: the same recorder pid;
  the same newest start record, sha and `recv_ns`; an interval count that does not fall; and an
  equal SHA-256 over the name, size and modification time of every file in every interval
  directory the run reads. Enumerate what the instrument can write — files, subprocesses with
  their exact argv and the absence of a shell, and its read paths — as System Map §7 item 32
  requires.
- **V10 — the fingerprint table**, every row, in lines, bytes and SHA-256, with the four changed
  or added rows reported beside them as they stand on the branch.
- **V11 — disclosure.** Every unit each of the three walks considered, in order, members and
  non-members alike, with the reason for each non-member; then every member's admissibility at
  every `tau`, with its `sigma_hat` and the `ADMIT[tau]` it was compared against.
- **V12 — influence.** Every `λ̂` reported with its value recomputed without its single most
  influential observation, that observation named by `T0`, label and `z`, and every `ν̂` reported
  with the same, the influential member named. Recorded, not asserted (System Map §7 items 27 and
  40).

---

## 8. The report

`CryptoReports/TZ-11-student-link-and-domain-report.md`, structure `## 0` … `## 6`:
`0` fingerprint, host and every free-space read; `1` the measurements in §3's order; `2` the gate
tables and the prediction; `3` the implementation and the three frozen tables; `4` validation
V1 … V12; `5` publication; `6` what could not be implemented as written and every reading chosen.
Section numbers asserted unique. **There is no verdict section: §4's verdict is the Architect's.**

The report states its own line count and SHA-256 for every file in map §0's fingerprint table.

---

## 9. Publication

Branch `tz-11-student-link`, one commit, four files, pushed; a pull request against `main`, **not
merged** — merge is the Boss's, after the Architect's verdict. The report goes straight to `main`.
Run the contract §4.2 separation self-check verbatim and print all three results. No Release, no
dataset, no archive, no binary in git history.

**Before anything is reclaimed**, copy into `/root/btc-forensics/` every file a committed report
names by SHA-256 that is not already there, asserting each hash at both ends and asserting that
every file already in that tree is unchanged. Then reclaim `/root/tz10b-work/`, one command naming
one tree, and verify with `test -e` rather than from any report.
