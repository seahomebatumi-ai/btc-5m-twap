# TZ-12 — the gate's own error rates

**Canonical filename: `TZ-12-sized-gate.md`.** The Executor names the committed file from this line
and from nothing else.

**This TZ reads no label.** It measures, from the frozen Student pricer's own predictions, how often
each gate of TZ-11a §4 fails a pricer that is exactly right. It measures the one table a
shape-transfer test needs, and it fixes the replacement gate, §4, which TZ-13 applies unchanged to
test 3. It scores nothing and judges nothing: the TZ-11a verdict stands (System Map §4, §7 item 49).

**Executor model: Opus.** This is gate arithmetic over a frozen pricer.

---

## 0. Fingerprint gate, host gate, resource floor, interpreter

The Executor compares every row below before doing any work. A mismatch on any one is **BLOCKED**
before the first file is read.

**Required System Map revision:** `2026-09-15-a`.

| anchor | required |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-answered-no / 2-not-started` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` |
| `A6` — pricer | `729f0bcdbee3` |

`A6` is `research/pfair.py` after PR #12. **This TZ moves no anchor and no `frozen` row**; it adds one
file.

**Host gate.** All three, or this is not the capture host and the run is BLOCKED:

1. `/var/lib/btc-recorder/btc-updown-5m/` exists and holds interval directories.
2. The recorder process is running and the newest `runtime.jsonl` start record carries sha
   `4216c04673ced76b5b2ac60ef57c9abedc46f9b9`.
3. The filesystem holding it is `/dev/vda2`, total `31,612,203,008` bytes.

**Resource floor, in exact bytes, derived from System Map §6.** §6 measured `14,264,078,336` bytes
free. This run's scratch is bounded by `60,000,000` bytes: four outputs of about `3,000,000` bytes
per run, and §9's copies of TZ-11a's six run outputs, `12,038,440` bytes together.

- Free space at run start, on `/dev/vda2`: at least **`2,060,000,000`** bytes.
- Free space at every later read: at least **`2,000,000,000`** bytes.
- Both are `assert`s in the instrument that abort the run. Every read is reported with its UTC time.

**Host preflight, reported and gating nothing beyond the floor** (System Map §6). At run start and
again at least `1,800` s later, take and report:

- `df -B1 /dev/vda2`;
- `du -x -B1 -s /root/PROJECT_GAMING_PS5`;
- `systemctl is-enabled telemetry-watch.service` and `systemctl is-active telemetry-watch.service`,
  each captured with its exit status rather than asserted.

Report the implied bytes/day of the tree and of free space. State this run's own scratch —
`/root/tz12-work` and `/root/.claude` — separately (System Map §7 item 29). No file of that project is
opened.

**Interpreter.** Every Python command of this TZ runs on `/root/tz01-env/venv/bin/python` (System Map
§6). It must report Python 3.12 and import `numpy`; the report states both versions. If `numpy` does
not import, the run is BLOCKED at §0.

The instrument sets `OPENBLAS_NUM_THREADS`, `OMP_NUM_THREADS` and `MKL_NUM_THREADS` to `"1"` in
`os.environ` before its first `import numpy`, so every matrix product is computed the same way on
every run. These three are the only environment writes it makes.

---

## 1. Why

**TZ-11a closed the Student pricer by its own §4, and that closure stands.** The Architect's audit
found that §4 fixed thresholds with no error rates (System Map §7 items 49 to 51):

- Under an exactly correct pricer, G3 fails some `tau` with probability at least `0.71` on every
  population TZ-11a scored. That is an approximation built from the report's bin tables.
- G2 read `pass` with nothing eligible.
- G4 was read on 28 to 35 members.

On test 2's admissible rows, the only adequately sized population, three things held:

- the shape transferred at 7 of 7 `tau`;
- the bins passed with 24 eligible;
- no scale p-value fell below `0.019`.

Test 1 is the weekend, where the absolute domain rule admits 6% to 8% of intervals. **Whether the
Student pricer is calibrated is not known.**

Three things follow, and all three can be done before anyone reads another label:

1. measure TZ-11a's gate error rates exactly, from the pricer's own predictions, with the committed
   code rather than an approximation;
2. measure the spread of `log ν̂` that a shape-transfer test needs, on the fit set alone;
3. fix a gate whose false-failure probability and power are stated in advance, for one set no one has
   read: test 3 (System Map §2.3).

`[решение принято мной]` **Two TZs, not one:** TZ-12 now, reading no label; TZ-13 after the
Architect's audit of TZ-12, once test 3 has formed. Discarded alternative: one TZ that measures the
gate's constants and scores test 3 in the same session. It would wait about 30 hours inside one
session and bind a gate to constants no one had audited.

**What does not move:** all of `pfair.py`, including `ADMIT`, `LINK_NU` and `LINK_SCALE`; every
committed file; TZ-11a's verdict; and TZ-07a §8's band, which stays the gate `p_fair` was judged by.

---

## 2. Scope

**Repository paths this TZ authorizes to change, and no others:**

| path | change | current state in map §0 |
|---|---|---|
| `research/tz12-sized-gate.py` | new: the sized gate and this TZ's instrument | does not exist |
| `CryptoReports/TZ-12-sized-gate-report.md` | new | does not exist |

No `frozen` row moves. The map's next revision adds the new file's row.

**The build happens in a worktree**, `/root/tz12-work/wt`, on branch `tz-12-sized-gate`. The
primary checkout `/root/btc-5m-twap` stays on `main` throughout.

**What may not be touched, and the exemptions, named here in this section** (System Map §7 items 23,
39 and 44):

- `/var/lib/btc-recorder/**` — read-only, always. No exemption.
- The recorder process — never signalled, never restarted. No exemption.
- `/root/tz04a-env/` and `/root/tz01-env/` — never altered. The second is executed and never written.
- `/root/btc-forensics/` — **exempt for §9's copies alone.** They add files by exclusive create
  (`open(..., "xb")`) and overwrite nothing; nothing else there is created, altered or removed.
- `/root/tz11a-work/` and `/root/tz09-work/` — **exempt for §9 alone:**
  - their files are copied out first;
  - then their three git worktrees are removed with `git worktree remove`;
  - then each tree is removed by one command.
- Every committed file, every report, every other `research/` script, and `pfair.py` entirely.
- Git: no branch is deleted, and nothing is pushed except branch `tz-12-sized-gate` and the one
  report commit on `main` that §9 requires.
- **Test 3 is not formed, not walked and not read.** In directories with `T0 > 1789427700`, the only
  files this TZ opens are the `manifest.json` files `analyze.load_manifests` reads for every interval
  directory. No `resolution.json`, feed file, quote file or `gamma.json` of any such directory is
  opened.

**Outcomes.** `resolution.json`, `resolved_up` and `priceToBeat` are read in exactly **one** place,
named here: inside `tz06.qualification`. `tz11a.the_sets` reaches it through `tz06.scoring_set` and
`tz08a.the_set` for every unit the three set formations consider, members and non-members alike —
1,314 units, none after `1789427700`.

**No label enters any number this TZ prints**, because none is ever attached to a row:

- every checkpoint row keeps `label = None`;
- `tz10b.m2_labels` is never called;
- `tz07a.lambda_hat` is called only on simulated or synthetic labels, and always with `log_cdf` given.

V2 proves all three, statically and at run time. No pass of any kind reads a test-set label, so the
rule of System Map §7 item 54 holds by construction.

**Signatures, as the files hold them, read from `origin/main` at `3452fb8`:**

```
analyze.load_manifests()
pfair.log_t_cdf(z, nu)                        pfair.t_cdf(z, nu)
pfair.ADMIT, pfair.LINK_NU, pfair.LINK_SCALE  keys == pfair.TAUS
pfair.GATED_TAUS = (240, 180, 120, 90, 60, 30)      pfair.TAUS = GATED_TAUS + (10,)
tz06.brier(pairs)                             tz06.bin_of(p)
tz06.calibration(pairs)                       tz06.BIN_MIN_N = 20   tz06.MAX_FAILING_BINS = 2
tz07a.log_likelihood(pairs, lam, log_cdf=None)
tz07a.lambda_hat(pairs, log_cdf=None)         tz07a.six_significant(value)
tz07a.LAMBDA_LO, tz07a.LAMBDA_HI, tz07a.LAMBDA_TOL = 0.5, 3.0, 1e-9
tz07b.member_list_sha(members)
tz10b.git(*args)
tz11a.host_read(when, t0s, floor)             tz11a.fit_set(manifests)
tz11a.the_sets(manifests)                     tz11a.walk_member(t0, manifests, guard)
tz11a.measure_admit(walked, fit)              tz11a.admissible_members(walked, members, admit)
tz11a.check_literals(name, literal, measured) tz11a.population(walked, members, tau)
tz11a.fit_student(r)                          tz11a.student_log_cdf(nu)
tz11a.checkpoint_row(t0, name, tau, row)
tz11a.NU_LO, tz11a.NU_HI = 2.05, 60.0         tz11a.G1_BRIER = 0.2496
tz11a.G3_BAND = 0.15                          tz11a.G4_BAND = math.log(2.0)
tz11a.FLOOR_START_BYTES = 2060000000          tz11a.FLOOR_BYTES = 2000000000
tz11a.tz10b, tz11a.tz08a, tz11a.tz07b, tz11a.tz07a, tz11a.tz06    the modules tz11a loaded
```

**Loading.** The instrument loads `tz11a-student-link.py` with an `importlib` helper of the same
shape as `tz11a._load`. It then takes `tz10b`, `tz08a`, `tz07b`, `tz07a` and `tz06` from the loaded
module, never loading any of them a second time: that would create a second module object.

---

## 3. The measurement

### 3.0 The sets, the walk, the rows

1. `manifests = analyze.load_manifests()`.
2. `sets, set_doc = tz11a.the_sets(manifests)`. This forms the fit set, test 1 and test 2 and asserts
   what TZ-11a asserted: the two committed hashes and pairwise disjointness.
3. The instrument then asserts that test 2's member-list hash is
   `2dd0fcc4dc2cf379e08c21a4524c3eab799aad7bff3136c37e32910cecb8fa70`, the value TZ-11a's committed
   report states in its §1.0. Test 2's units were all written before 2026-09-14 23:27 UTC, and
   manifests do not change once written.
4. Walk every member of the three sets with `tz11a.walk_member(t0, manifests, False)`: the fit set
   first, then test 1, then test 2, each in ascending `T0`.
5. For every member and every `tau`, `row = tz11a.checkpoint_row(t0, name, tau, walked[t0][tau])`. A
   row's `label` stays `None` and is never assigned.
6. **The admissible rows** of a set at `tau` are its rows whose `admissible` is `True` — `sigma_hat`
   at or above the committed literal `pfair.ADMIT[tau]` — in ascending `T0`. For each set and `tau`,
   assert:
   - their `T0` list equals `tz11a.admissible_members(walked, members, pfair.ADMIT)[tau]`;
   - their count equals TZ-11a's §1.2, at `tau` 240 … 10 — 21 counts in all:

     | set | counts |
     |---|---|
     | fit | 280 at 7 of 7 |
     | test 1 | 35 / 29 / 28 / 28 / 28 / 28 / 30 |
     | test 2 | 231 / 237 / 233 / 234 / 233 / 235 / 235 |
7. **The 14 populations** of §3.2 and §3.3 are test 1's and test 2's admissible rows at each `tau`.
   The fit set's admissible members feed §3.1 and V4, and nothing else.

### 3.1 M1 — the member-bootstrap spread of `log ν̂`, on the fit set alone

At each `tau` in `pfair.TAUS`, `A_tau` is the fit set's 280 admissible members in ascending `T0`, and
`B_BOOT = 24`.

1. Create the stream
   `numpy.random.Generator(numpy.random.PCG64(numpy.random.SeedSequence([20260915, 0, tau, 9])))`.
2. For each replicate `b = 0 … 23`:
   - draw `idx = rng.integers(0, 280, size=280)` in one call;
   - form `drawn = sorted(A_tau[i] for i in idx)`, duplicates kept and adjacent;
   - fit `tz11a.fit_student(tz11a.population(walked, drawn, tau)[0])`, the committed search
     unchanged.
3. Record per replicate:
   - `tz07b.member_list_sha(drawn)` and the number of distinct members;
   - the anchors, `ν̂*`, `ŝ*` and the four bound flags;
   - the evaluations and seconds;
   - `x_b = math.log(ν̂*)`.
4. **`SIGMA_LOG_NU[tau]` = `statistics.stdev` of the 24 values `x_b`**, the sample standard deviation
   with denominator 23.

The table is frozen into the new file as one Decimal literal per `tau`, rounded by
`tz07a.six_significant`, with keys exactly `pfair.TAUS`. The instrument asserts it against its own
measurement through `tz11a.check_literals` before M2 starts (V8) — the pattern TZ-07b §5 set.

**Censoring, fixed here:**

- A `tau` is **censored** when more than 2 of its 24 replicates put `ν̂*` on a search bound, that is,
  `nu_at_lower_bound` or `nu_at_upper_bound` is set.
- The set of censored `tau` is frozen beside the table as `SIGMA_LOG_NU_CENSORED`, a `frozenset`
  literal, and asserted the same way.

**Report per `tau`:**

- the table value;
- the mean of `x_b`, `log LINK_NU[tau]` and their difference;
- the smallest and largest `ν̂*`;
- the sample skewness of `x_b`, `g1 = m3 / m2**1.5` with population moments;
- the bound hits;
- the evaluations, anchors and seconds.

**No outcome is read**; M1's inputs are the feed and the manifests.

**Cost** (CANON PART VI C4). M1 is `24 × 7 = 168` fits.

- Each replicate's seven resamples hold about `971,187` anchors together: the admissible fit total,
  TZ-11a M1.
- On those populations the committed search spent `2,024` to `2,300` evaluations per fit,
  `2,061,924,102` anchor-evaluations in all.
- TZ-11a measured about `9.2e-9` s per anchor-evaluation: 158.7 s over its 63 fits.
- That is about `19` s per replicate and `457` s for M1.
- **This TZ runs M1 three times:** once in `--emit` and once in each full run.

**Fail-fast.** V4's seven fits run first, over the same seven populations. Let `t` be their seconds
together. The session then needs about `75 × t + 500` s. **If `t` exceeds `40` s, the run is
BLOCKED**, stating `t` and that projection against CANON's `3,600` s.

### 3.2 M2 — TZ-11a's gate, sized after the fact, from predictions alone

Each of the 14 populations gets its null replicates, §3.4, with labels drawn from the pricer's own
`p_t`. The instrument reports:

- **old G1:** the fraction of null replicates whose `tz06.brier` is at or above `0.2496`;
- **old G2:**
  - per gated `tau`, the distribution of the replicate's failing bins and its fraction at or above 1;
  - per set, the probability that the six-`tau` total reaches `tz06.MAX_FAILING_BINS + 1 = 3`, by
    exact convolution of the six per-`tau` distributions.

  The second figure is labelled "under independent per-`tau` draws": a member's label is shared across
  `tau`, and the true joint cannot be simulated from marginal predictions;
- **old G3:**
  - the fraction with `abs(λ̂*_grid − 1) > tz11a.G3_BAND`;
  - per set, two bounds on "some `tau` fails": the largest per-`tau` fraction, and
    `1 − Π(1 − fraction)`;
- **old G4**, under a normal approximation:
  - `2 × (1 − Φ(tz11a.G4_BAND / s))`;
  - `s = SIGMA_LOG_NU[tau] × sqrt(1 + 280 / m)`, where `m` is the population's member count.

These describe a committed verdict. **They change nothing about it.**

### 3.3 M3 — §4's constants on the same predictions

For each of the 14 populations, the instrument reports every label-free constant §4 defines:

- G1: `P0` and `P1`;
- G2, at gated `tau` (at `tau = 10`, printed only): `E`, `k2` and the null count at `k2`;
- G3: `crit3`, `P3`, `P_under` and `P_double`;
- G4:
  - `m`, `c4`, `s` and `P4`;
  - whether `LINK_NU[tau] / 2` lies below `tz11a.NU_LO`;
  - the censored flag;
- whether G1 and G3 **could** read PASS on that population: `P1 >= 0.5` and `P3 >= 0.5`.

**No observed statistic of either test set is computed under §4.** Tests 1 and 2 were judged by
TZ-11a §4, and no gate is redefined after its number is known (CANON PART II).

### 3.4 The arithmetic, fixed here

For one population, the rows are in ascending `T0`, with `z_i = row["z_student"]`,
`p_i = row["p_t"]`, `n` rows, and `nu = float(pfair.LINK_NU[tau])`.

1. **Streams.** One fresh generator per set, `tau` and purpose:
   `numpy.random.Generator(numpy.random.PCG64(numpy.random.SeedSequence([20260915, set_code, tau, purpose])))`.

   | `set_code` | set |
   |---|---|
   | 0 | fit |
   | 1 | test 1 |
   | 2 | test 2 |
   | 3 | test 3 |

   | `purpose` | name | rows `R` |
   |---|---|---|
   | 0 | null | `20,000` |
   | 1 | over | `2,000` |
   | 2 | under | `2,000` |
   | 3 | double | `2,000` |
   | 4 | coin | `2,000` |
   | 9 | member bootstrap | M1 only |
2. **Labels.** `Y = (rng.random((R, n)) < q).astype(numpy.float64)`, where `q` is the vector of row
   probabilities:

   | purpose | `q_i` |
   |---|---|
   | null | `p_i` |
   | over | `pfair.t_cdf(z_i / 1.5, nu)` |
   | under | `pfair.t_cdf(z_i / (1.0 / 1.5), nu)` |
   | double | `pfair.t_cdf(z_i / 2.0, nu)` |
   | coin | `0.5` |

   `Y` may be generated in consecutive row blocks, which gives the same stream.
3. **The λ grid.** `lam_j = (500 + j) / 1000.0` for `j = 0 … 2500`. That is 2,501 values over the
   committed interval `[tz07a.LAMBDA_LO, tz07a.LAMBDA_HI]`, with `lam_500 = 1.0` exactly. The tables
   are computed once per population, in `numpy.float64`, each `n × 2501`:
   - `A[i, j] = pfair.log_t_cdf(z_i / lam_j, nu)`;
   - `B[i, j] = pfair.log_t_cdf(-z_i / lam_j, nu)`.
4. **The likelihood ratio.** `L = Y @ (A − B) + B.sum(axis=0)`.
   - `L` is each replicate's log-likelihood at every grid value: the committed
     `tz07a.log_likelihood` with `log_cdf` given, evaluated on the grid.
   - `LR = 2 × (L.max(axis=1) − L[:, 500])`.
   - `λ̂_grid` is the grid value at the first maximum.
5. **Brier.** `tz06.brier(list(zip(p, y)))` per replicate, where `p` is the float predictions and `y`
   the replicate's labels as `int`.
6. **Failing bins.**
   - Call `tz06.calibration([(p_i, 0) for each row])` once. Its bins' `n`, `eligible` and `region`
     depend on the predictions alone.
   - Take `b_i = tz06.bin_of(p_i)`.
   - A replicate's `F` is the number of eligible bins whose Up count, the sum of `Y[r, i]` over the
     rows in that bin, lies outside `[lo, hi]` — the comparison `tz06.calibration` makes.
   - `E` is the number of eligible bins.
7. **Guards, asserted.**
   - For the first 100 null replicates of every population, `tz06.calibration` on that replicate's own
     pairs returns item 6's failing count: **1,400 comparisons**.
   - For the first 20,
     `tz07a.lambda_hat(pairs, tz11a.student_log_cdf(nu))["likelihood_ratio"]` differs from item 4's
     `LR` by at most `0.02`: **280 comparisons**.
   - The largest difference in `LR` and in `λ̂` is reported.
8. **Cost.** Per population the work is:
   - `2 × n × 2,501` calls of `pfair.log_t_cdf`: at most `1,185,474` at `n = 237`, about `6` s at the
     `5` µs per call the Architect measured;
   - `28,000` label rows, of which the `26,000` of the null, over, under and double purposes enter
     one matrix product of at most `26,000 × 237 × 2,501` elements.

   Over the 14 populations, guards included, that is about `100` s per run.

---

## 4. The sized gate — fixed here, applied by TZ-13 to test 3 and to nothing else

**Fixed before anyone has read any label of test 3.** TZ-13 applies this section without change. Any
change is a new TZ that names this section. Nothing here is re-fitted: `ADMIT`, `LINK_NU`,
`LINK_SCALE`, `SIGMA_LOG_NU` and `SIGMA_LOG_NU_CENSORED` are committed literals.

**Population.** At each `tau` of `pfair.TAUS`, the population is the scored set's admissible
checkpoint rows, as §3.0 defines rows, with `m` the admissible member count.

**Null model.** The frozen pricer is exactly right, so each row's label is drawn independently from
its own `p_t`.

- Every critical value and power below is computed by §3.4 from the rows' predictions alone.
- **TZ-13 prints them all before it reads any label of the scored set.**

**Error budget.**

| gate | α per `tau` | `tau` gated | total |
|---|---|---|---|
| G1 | `0.001` | 7 | `0.007` |
| G2 | `0.001` | 6 | `0.006` |
| G3 | `0.0025` | 7 | `0.0175` |
| G4 | `0.0025` | 7 | `0.0175` |

By Bonferroni, **`0.048`** bounds the probability that any gate FAILs an exactly correct pricer. The
bound holds up to Monte Carlo error on G1 to G3 and a normal approximation on G4.

The four possible readings are FAIL, PASS, NO FAIL and UNDECIDABLE.

| gate | statistic | critical value | power | reading |
|---|---|---|---|---|
| **G1** — discrimination | `tz06.brier` of `p_t` | `0.2496`, TZ-06's constant. `P0` = null fraction at or above it | `P1`: coin, labels at `1/2`; fraction at or above `0.2496` | **FAIL** if Brier `>= 0.2496` and `P0 <= 0.001` — at most 20 of 20,000. **PASS** if Brier `< 0.2496` and `P1 >= 0.5`. Otherwise **UNDECIDABLE** |
| **G2** — bin calibration, `pfair.GATED_TAUS` only | failing bins `F`, as `tz06.calibration` counts them | `k2` = the smallest integer `k`, `1 <= k <= E`, with at most 20 of the 20,000 null `F` at or above `k` | none | **FAIL** if `F >= k2`. **UNDECIDABLE** if `E = 0` or no `k2` exists. Otherwise **NO FAIL**. **G2 never admits a `tau`.** At `tau = 10` it is printed, not gated |
| **G3** — scale | `LR` of §3.4 item 4 on the observed labels | `crit3` = the 19,950th smallest of the 20,000 null `LR` | `P3`: overconfidence, `λ = 1.5`; fraction of 2,000 with `LR > crit3`. Reported beside it: `λ = 1/1.5` and `λ = 2` | **FAIL** if `LR > crit3`. **PASS** if `LR <= crit3` and `P3 >= 0.5`. Otherwise **UNDECIDABLE** |
| **G4** — shape transfer | `d = log(ν̂_set / LINK_NU[tau])`, with `ν̂_set` from `tz11a.fit_student` over the scored set's admissible members' anchors, `tz11a.population` | `c4 = Z4 × SIGMA_LOG_NU[tau] × U_BOOT × sqrt(1 + 280 / m)` | `P4`, against tails twice as heavy: `Φ((log 2 − c4) / s) + 1 − Φ((c4 + log 2) / s)`, `s = SIGMA_LOG_NU[tau] × sqrt(1 + 280 / m)`. Reported | **UNDECIDABLE** at a censored `tau`. Otherwise **FAIL** if `abs(d) > c4`, else **NO FAIL**. **G4 never admits a `tau`**, and whether `ν̂_set` sits on a search bound is reported |

**Constants.**

- `Z4 = statistics.NormalDist().inv_cdf(1 − 0.0025 / 2) = 3.02334143973915`.
- `U_BOOT = math.sqrt(23 / 14.8479557992677) = 1.24460225924042`. This is the factor that turns a
  standard deviation estimated from 24 replicates into its upper 90% confidence bound, so the
  bootstrap's own sampling error cannot shrink `c4`.
- `280` is the fit set's admissible member count at every `tau`.

**Why these alternatives.** The error that loses money is overconfidence: predictions that are too
sure.

- At `tau = 60`, `λ = 1.5` moves a `0.83` prediction to about `0.74`. That is nine probability points,
  against a taker fee near one.
- The Architect's approximation puts `P3` at or above `0.5` for weekday-sized populations at `tau`
  180 to 60 only. **A PASS does not rule out smaller errors.**
- Underconfidence at short `tau` is invisible to labels, because predictions there already sit near 0
  or 1, and it costs no money. It is reported and never required.
- Shape and bins are disqualifiers: a failure closes, and silence admits nothing.

**The verdict, applied by TZ-13:**

- **CLOSED** if any gate reads FAIL at any `tau`.
- Otherwise, the **admitted domain** is every `tau` at which G1 and G3 both read PASS.
  - The pricer is **NOT DISQUALIFIED** on the admitted domain; Phase 1 cannot confirm.
  - It is **UNDECIDED** at every other `tau`.
  - If the admitted domain is empty, the pricer is UNDECIDED.
- Tests 1 and 2 are never scored under this section.

### 4.1 The pre-registered prediction — the Architect's, `[решение принято мной]`

| quantity | predicted |
|---|---|
| M1 | each `SIGMA_LOG_NU` at `tau` 240, 180 and 120 is larger than each at 90, 60 and 30. `tau = 10` is censored |
| M2, old G3 | on test 2's admissible rows, the per-`tau` false-failure fraction lies in `0.15 … 0.40` at `tau` 240 … 60 and above `0.40` at 30 and at 10. On test 1's, it is above `0.60` at every `tau` |
| M3, G1 | `P0 <= 0.001` at every `tau` on test 2. Above `0.001` at `tau = 240` on test 1 |
| M3, G3 | `P3 >= 0.5` at `tau` 180, 120, 90 and 60 on test 2, and below `0.5` at 240, 30 and 10. Below `0.5` at every `tau` on test 1 |
| TZ-13 | no gate FAILs on test 3, and the admitted domain is `tau` 180, 120, 90 and 60 |

**The reasoning.** Three sources:

- the Architect's bin-level simulation of the audit gives the M2 and M3 rows;
- TZ-11a's influence refits give the M1 row;
- test 3 runs on two weekdays, like test 2's admissible rows.

**Discarded alternative:** `λ = 1.3` as the named alternative. It was rejected because at 230 to 240
rows its power stays below `0.35` at every `tau`, so G3 could not admit anything.

---

## 5. The code

### 5.1 `research/tz12-sized-gate.py` — new

One file. Importing it has no side effects beyond the environment writes of §0 and loading its
dependencies, so TZ-13 can load it with the same `importlib` helper and call §4 from it. It keeps
the loaded module as `tz11a`, so a later instrument takes every committed module from this one
and loads none a second time.

**Constants, named here:**

```
SEED = 20260915
SET_CODES = {"fit": 0, "test1": 1, "test2": 2, "test3": 3}
PURPOSES = {"null": 0, "over": 1, "under": 2, "double": 3, "coin": 4, "bootstrap": 9}
R_NULL = 20000                 R_POWER = 2000
ALPHA = {"G1": 0.001, "G2": 0.001, "G3": 0.0025, "G4": 0.0025}      FAMILY_ALPHA = 0.048
COUNT_BOUND = 20               CRIT_RANK = 19950          # 1-based rank of crit3
LAMBDA_K = (500, 3000)         LAMBDA_ONE_COLUMN = 500
LAMBDA_OVER = 1.5              LAMBDA_UNDER = 1.0 / 1.5   LAMBDA_DOUBLE = 2.0
POWER_TO_PASS = 0.5
B_BOOT = 24                    BOUND_HITS_ALLOWED = 2     FIT_ADMISSIBLE = 280
Z4 = statistics.NormalDist().inv_cdf(1 - ALPHA["G4"] / 2)
U_BOOT = math.sqrt(23 / 14.8479557992677)
SIGMA_LOG_NU = {240: D("…"), 180: D("…"), 120: D("…"), 90: D("…"), 60: D("…"), 30: D("…"), 10: D("…")}
SIGMA_LOG_NU_CENSORED = frozenset({…})
TEST2_SHA256 = "2dd0fcc4dc2cf379e08c21a4524c3eab799aad7bff3136c37e32910cecb8fa70"
ADMISSIBLE_COUNTS = {"fit": {...}, "test1": {...}, "test2": {...}}   # §3.0 item 6
FIRST_FITS_LIMIT_S = 40.0
GUARD_BINS = 100               GUARD_LR = 20              GUARD_LR_TOL = 0.02
```

G1's threshold, the old bands and the floors are read from `tz11a`, not retyped:
`tz11a.G1_BRIER`, `tz11a.G3_BAND`, `tz11a.G4_BAND`, `tz11a.FLOOR_START_BYTES` and
`tz11a.FLOOR_BYTES`.

**Functions — names and contracts fixed here, bodies the Executor's:**

| function | returns |
|---|---|
| `lambda_grid()` | §3.4 item 3's 2,501 floats |
| `grid_tables(zs, nu)` | `(A − B, B.sum(axis=0))` for one population |
| `draw(set_code, tau, purpose, q, rows)` | §3.4 items 1 and 2 |
| `grid_lr(Y, diff, base)` | `(LR, lambda_hat)` for each row of `Y` |
| `bin_counter(ps)` | item 6's label-free bin structure, as `(E, count)`, where `count(Y)` gives each row's `F` |
| `k2_of(null_f, eligible)` | §4's `k2`, or `None` |
| `crit_of(null_lr)` | the `CRIT_RANK`-th smallest value |
| `g4_power(c4, s)` | §4's `P4` formula |
| `g4_constants(tau, m)` | `c4`, `s`, `P4`, the censored flag and the below-floor flag |
| `constants(rows, tau, set_code)` | every §4 constant and every per-`tau` §3.2 diagnostic for one population, label-free, with the two guards run inside |
| `readings(consts, observed)` | §4's four readings at one `tau`. `observed` holds `brier`, `failing_bins`, `lr`, `log_ratio` and `nu_on_bound` |
| `verdict(per_tau)` | §4's verdict from the seven `tau`'s readings |
| `bootstrap(walked, fit_admissible)` | M1 |
| `emit()` | the `--emit` pass: a host read at the start floor, the fit set through `tz11a.fit_set`, its walk, V4's seven timed fits with the fail-fast, and M1. It prints the two literals for pasting |
| `build()`, `tables(doc)`, `main(argv)` | the run |

`readings` and `verdict` are called in this TZ only by self-test item 5. Until `--emit` has run, the
two frozen literals may be empty placeholders: `--emit` never reads them, and `--out` asserts them
(V8).

**Run, from the worktree:**

```
/root/tz01-env/venv/bin/python -B tz12-sized-gate.py --emit
/root/tz01-env/venv/bin/python -B tz12-sized-gate.py --out <directory>
```

`--out` writes four files:

- `tz12-results.json`, `tz12-tables.md` and `tz12-bootstrap.csv`, none of which carries a wall-clock
  time or a path;
- `tz12-host.json`, the run's own reads and timings.

`tz12-bootstrap.csv` holds one row per replicate per `tau` — 168 rows — with columns `tau`,
`replicate`, `draws_sha256`, `distinct_members`, `anchors`, `nu`, `s`, `nu_at_lower_bound`,
`nu_at_upper_bound`, `s_at_lower_bound`, `s_at_upper_bound`, `evaluations`, `log_nu`.

**Order inside `build()`, fixed:**

1. host read 1;
2. the self-tests (§5.2);
3. V6;
4. the sets and V5;
5. the walk;
6. host read 2;
7. V4, with the fail-fast;
8. M1, then V8;
9. M2 and M3;
10. V2's run-time check;
11. host read 3, and V9's assertions.

### 5.2 Self-tests — six items, inside the instrument, run before the walk; each an `assert`

**Item 1 — the two constants.**

- `Z4` equals `3.02334143973915` within `1e-12` relative.
- `U_BOOT` equals `1.24460225924042` within `1e-12` relative.

The Architect computed both literals with `mpmath` at 40 digits, an implementation independent of
the one under test, and cross-checked each by a second route:

- the normal quantile by `mpmath.erfinv`, cross-checked by `statistics.NormalDist`, which agrees to
  `2.1e-15` relative;
- the chi-square quantile `14.8479557992677` by root-finding on `mpmath`'s regularized gamma,
  cross-checked by `scipy.stats.chi2.ppf`, which agrees below `1e-16`.

The printed 15-digit literals are exact to about `1e-15`, which is well inside the `1e-12`
tolerance.

**Item 2 — the rank rules.**

- `crit_of(list(range(19999, -1, -1)))` is `19949`.
- `k2_of` returns:

  | `null_f` | `eligible` | `k2_of` |
  |---|---|---|
  | 19,000 zeros, 900 ones, 80 twos, 15 threes, 5 fours | 4 | `3` |
  | 20,000 zeros | 3 | `1` |
  | 19,975 zeros and 25 ones | 1 | `None` |

**Item 3 — the grid against the committed search.** Take 201 synthetic pairs, `i = 0 … 200`:

- `z_i = -5 + i / 20`;
- `y_i = int((z_i > 0) != (i % 7 == 0))`;
- `nu = float(pfair.LINK_NU[30])`.

`tz07a.lambda_hat(pairs, tz11a.student_log_cdf(nu))` and `grid_lr` must agree to
`abs(ΔLR) <= 0.02` and `abs(Δλ̂) <= 0.002`.

The Architect's run of this case gave:

| route | `λ̂` | `LR` |
|---|---|---|
| committed search | `2.52455` | `51.3573` |
| grid | `2.525` | `51.3573` |

The differences are `1.5e-6` in `LR` and `4.5e-4` in `λ̂`. Every input is synthetic or a committed
literal.

**Item 4 — the power formula.**

- `g4_power(math.log(2.0), 0.1)` is `0.5` within `1e-12`.
- `g4_power(0.0, 0.1)` is `1.0` within `1e-12`.

**Item 5 — the readings and the verdict.** `readings` returns exactly these 19 readings:

| gate | inputs | reading |
|---|---|---|
| G1 | Brier `0.26`, `P0 = 0.0005` | FAIL |
| G1 | Brier `0.26`, `P0 = 0.002` | UNDECIDABLE |
| G1 | Brier `0.2496`, `P0 = 0.001` | FAIL |
| G1 | Brier `0.20`, `P1 = 0.7` | PASS |
| G1 | Brier `0.20`, `P1 = 0.3` | UNDECIDABLE |
| G1 | Brier `0.20`, `P1 = 0.5` | PASS |
| G2 | `F = 2`, `k2 = 2`, `E = 3` | FAIL |
| G2 | `F = 1`, `k2 = 2`, `E = 3` | NO FAIL |
| G2 | `E = 0` | UNDECIDABLE |
| G2 | `E = 1`, `k2 = None` | UNDECIDABLE |
| G3 | `LR = 10`, `crit3 = 9` | FAIL |
| G3 | `LR = 5`, `crit3 = 9`, `P3 = 0.6` | PASS |
| G3 | `LR = 5`, `crit3 = 9`, `P3 = 0.4` | UNDECIDABLE |
| G3 | `LR = 9`, `crit3 = 9`, `P3 = 0.5` | PASS |
| G4 | `abs(d) = 1.0`, `c4 = 0.8`, not censored | FAIL |
| G4 | `abs(d) = 1.0`, `c4 = 0.8`, censored | UNDECIDABLE |
| G4 | `abs(d) = 0.5`, `c4 = 0.8`, not censored | NO FAIL |
| G4 | `abs(d) = 0.8`, `c4 = 0.8`, not censored | NO FAIL |
| G4 | `abs(d) = 1.0`, `c4 = 0.8`, on a search bound, not censored | FAIL |

`verdict` returns exactly these three verdicts:

| input | verdict |
|---|---|
| one FAIL at one `tau` | CLOSED |
| no FAIL, with G1 and G3 both PASS at `tau` 90 and 60 only | NOT DISQUALIFIED on `{90, 60}` |
| no FAIL and no `tau` with both PASS | UNDECIDED |

That is 22 assertions in one item.

**Item 6 — the streams.**

- Two generators built from `SeedSequence([20260915, 2, 60, 0])` give identical first 1,000 doubles.
- The generator for purpose 1 differs from purpose 0 in its first double.

---

## 6. Retention

System Map §6 and TZ-09 §5 govern, and the capture is never deleted.

- This run's scratch is `/root/tz12-work/`. TZ-13 reclaims it once this report is on `main`, after
  every file this report names by SHA-256 is copied to `/root/btc-forensics/`.
- `/root/tz11a-work/` and `/root/tz09-work/` are reclaimed by §9 (System Map §7 item 55).

---

## 7. Validation

Each check states its count. "All checks passed" is not a result.

- **V1 — gates.**
  - The map §0 fingerprint table is recomputed row by row, and the frozen count is asserted.
  - Also checked: the six anchors, the three host checks, the interpreter's two versions, and the
    resource floor at every read, each floor read an `assert`.
  - Every free-space read is reported with its UTC time.
- **V2 — label isolation, asserted two ways.**
  - **Static.** The instrument's own `ast` holds:
    - no `Call` whose function is an attribute named `m2_labels`, `venue`, `qualification`,
      `score_member`, `score`, `table_for`, `score_rows`, `lambda_with_influence`, `m4`, `m5`, `v4`,
      `fits` or `build` — the committed entry points that read or carry a label;
    - no string constant, other than a module or function docstring, containing `resolution`,
      `resolved_up`, `priceToBeat`, `quotes.jsonl` or `gamma.json`;
    - every call to an attribute named `lambda_hat` passes exactly two positional arguments.
  - **Run time.** After M3, all 8,400 checkpoint rows (1,200 members × 7 `tau`) still carry
    `label is None`.
  - `tz06.qualification`'s reads are the exemption §2 names.
  - **Causality is not re-tested.** `p_t` and `sigma_hat` are TZ-11a's, whose V2 established them at
    140 of 140, and this TZ adds no quantity computed at decision time.
- **V3 — determinism.**
  - Two full runs from fresh processes on the same commit.
  - `tz12-results.json`, `tz12-tables.md` and `tz12-bootstrap.csv` must be byte-identical, asserted by
    the report's assembler on SHA-256.
  - The literals `--emit` printed equal both runs' measurements (V8).
  - The timings are reported beside §3.1's and §3.4's cost statements.
- **V4 — the instrument reproduces what is committed.** Three assertions, each a count:
  1. `ADMIT` at **7 of 7**, through `tz11a.measure_admit` and `tz11a.check_literals`;
  2. `LINK_NU` and `LINK_SCALE` at **14 of 14**, from seven `tz11a.fit_student` fits over the fit
     set's admissible populations, through `tz11a.check_literals`. These seven fits are timed
     together and carry §3.1's fail-fast;
  3. the **21** admissible counts of §3.0.
- **V5 — set identity.**
  - The fit set's and test 1's hashes are asserted inside `tz11a.the_sets`.
  - Test 2's hash is asserted against `TEST2_SHA256`.
  - The three sets are asserted pairwise disjoint inside `tz11a.the_sets`.
  - **3 hashes asserted.** No other set is formed.
- **V6 — the diff.**
  - `git status --porcelain` is empty for the two paths.
  - `git diff --name-only $(git merge-base HEAD main) HEAD` lists exactly
    `research/tz12-sized-gate.py`.
  - The instrument's `ast` holds no attribute store or delete, no `setattr` or `delattr` call, and no
    `global` or `nonlocal`.
  - Its only subscript assignments to `os.environ` are the three of §0.
  - `SIGMA_LOG_NU`'s keys are exactly `pfair.TAUS`.
- **V7 — the self-tests.** **6 of 6**, run before the walk, their output printed verbatim.
- **V8 — the frozen literals.**
  - `SIGMA_LOG_NU` at **7 of 7**, through `tz11a.check_literals`.
  - `SIGMA_LOG_NU_CENSORED` equal to this run's censored set.
  - **8 assertions**, all made before M2 starts.
- **V9 — the capture is untouched.**
  - `tz11a.host_read` runs at run start, after the walk and at run end, with TZ-11a's four
    assertions between the first read and the last.
  - The read set is every unit the three set formations consider and each member's predecessor.
  - Enumerate what the instrument can write:
    - four files into `--out`, which is asserted to lie outside the capture;
    - `git` subprocesses in read-only forms through `tz10b.git`, with fixed argument lists and no
      shell;
    - nothing else.
- **V10 — the fingerprint table.** Every row of map §0 in lines, bytes and SHA-256: 18 `frozen` and
  2 `tracked`. The new file is reported beside them as it stands on the branch.
- **V11 — disclosure.**
  - The three member-list hashes, and the three sets' units considered with their non-member reasons,
    as `tz11a.the_sets` returns them. The unit-by-unit listing is TZ-11a's V11, identical by hash.
  - Per set and `tau`: the admissible `T0` list's `tz07b.member_list_sha` and its count.
  - Per bootstrap replicate: its draw hash, distinct-member count and anchors in the CSV, and its full
    drawn list in the JSON.
- **V12 — influence, recorded, not asserted.**
  - For each `tau`, `SIGMA_LOG_NU` recomputed leaving out each replicate once: the smallest and the
    largest of the 24 values.
  - For each of the 14 populations, `crit3` recomputed from the first 10,000 null replicates, beside
    the full value.
  - Neither moves anything.

---

## 8. The report

The report is `CryptoReports/TZ-12-sized-gate-report.md`, with sections `## 0` … `## 6`:

| section | contents |
|---|---|
| `0` | fingerprint, host, interpreter and every free-space read |
| `1` | the measurements in §3's order, per set before pooled |
| `2` | §4's constants per population, and the prediction beside what was measured |
| `3` | the implementation, the two frozen literals, and where every quantity comes from |
| `4` | validation V1 … V12 |
| `5` | publication and §9 |
| `6` | what could not be implemented as written, and every reading chosen |

Section numbers are asserted unique. **There is no verdict section, and no observed statistic of any
set appears under §4.** The report states its own line count and SHA-256 for every file in map §0's
table and for the new file.

---

## 9. Publication

- Branch `tz-12-sized-gate`: one commit, one file, pushed.
- A pull request against `main`, **not merged** — merge is the Boss's, after the Architect's verdict.
- The report goes straight to `main`.
- Run the contract §4.2 separation self-check verbatim and print all three results.
- No Release, no dataset, no archive, no binary in git history.

**Then, in this order, each step only after the previous one succeeded:**

1. **Copy.**
   - Hash every file under `/root/tz11a-work/` and `/root/tz09-work/`.
   - Copy into `/root/btc-forensics/`, by exclusive create, every file whose SHA-256 a committed
     report on `main` names and which that tree does not already hold by hash. Name each copy by its
     path relative to `/root`, with `/` replaced by `--`, as TZ-11a did.
   - Assert each hash at both ends, and assert that every file already there hashes unchanged.
2. **Worktrees.**
   - Run `git -C /root/btc-5m-twap worktree remove` for `/root/tz11a-work/wt`, `/root/tz09-work/wt`
     and `/root/tz09-work/wt-report`: one command each, never `--force`.
   - If git refuses any of them, stop this list and hand the Boss one exact block for what remains
     (System Map §6).
3. **Trees.**
   - Remove `/root/tz11a-work/` and `/root/tz09-work/`: one command naming one tree each, each verified
     with `test -e`.
   - If a command is refused, hand the Boss one exact block, and verify the outcome with `test -e`
     afterwards.

No branch is deleted.

---

## 10. Pre-send checks

CANON PART VI, performed against this file, start to end, as a separate reading after §9 was
written.

- **C1 — scope against body.** The body names the two authorized paths, 49 committed entry points
  (C7), and 20 other paths, enumerated from the file:
  - repository and code: `research/pfair.py` and `tz11a-student-link.py`;
  - capture: `/var/lib/btc-recorder/**` and `/var/lib/btc-recorder/btc-updown-5m/`;
  - host: `/dev/vda2`, `/root/PROJECT_GAMING_PS5`, `/root/.claude`, `/root/btc-5m-twap`, and `/root`
    as §9's naming base;
  - environments: `/root/tz01-env/`, `/root/tz01-env/venv/bin/python` and `/root/tz04a-env/`;
  - scratch: `/root/tz12-work/` and `/root/tz12-work/wt`;
  - reclaimed: `/root/tz11a-work/`, `/root/tz11a-work/wt`, `/root/tz09-work/`,
    `/root/tz09-work/wt` and `/root/tz09-work/wt-report`;
  - evidence: `/root/btc-forensics/`.

  **Seven intersections with §2's prohibition list, each now a named exemption in §2:**
  1. `/root/btc-forensics/`, for §9's copies;
  2. `/root/tz11a-work/`, for §9's reclamation;
  3. `/root/tz09-work/`, for §9's reclamation;
  4. `/root/tz01-env/`, executed and never written;
  5. `tz06.qualification`'s outcome reads;
  6. `tz07a.lambda_hat`, on simulated and synthetic labels only;
  7. the report commit pushed to `main`. **This one was found in this reading:** §2 first said
     nothing but the branch is pushed, and §2 has been rewritten.

  The `manifest.json` reads of test-3 directories by `analyze.load_manifests` are named in §2 as the
  only files of those directories opened. The capture reads of the host gate are what "read-only"
  permits.
- **C2 — origin of every expectation.** 75 fixed expectations in §5 and §7:
  - **2 computed independently:** `Z4` and `U_BOOT`, with `mpmath` at 40 digits and cross-checked by
    a second route (item 1);
  - **28 exact by construction:** item 2's `19949`, `3`, `1` and `None`; item 4's `0.5` and `1.0`;
    item 5's 22 readings and verdicts;
  - **2 bounds between two implementations:** item 3's `0.02` and `0.002`, against the Architect's
    `1.5e-6` and `4.5e-4`;
  - **43 quoted from committed artifacts:** test 2's hash and the 21 admissible counts (TZ-11a report
    §1.0 and §1.2), and the 21 `pfair.py` literals V4 checks through `tz11a.check_literals`.

  **Zero depend on a quantity this TZ measures.** `SIGMA_LOG_NU` and `SIGMA_LOG_NU_CENSORED` are
  asserted against this run's own measurement (V8), never against a value written here. Item 6
  asserts equality and inequality of streams and carries no number.
- **C3 — shape of every diff.** One new file; replaced lines: none. No section of this TZ describes a
  change to a committed file, because it makes none.
- **C4 — cost of every check.** Per full run:
  - **M1:** 168 fits, about 457 s — `2,061,924,102` anchor-evaluations per replicate-set at TZ-11a's
    `9.2e-9` s. It runs three times: once in `--emit` and once in each full run.
  - **V4's seven fits:** about 19 s each time.
  - **M2 and M3:** 14 populations, at most `1,185,474` `log_t_cdf` calls and one product of
    `26,000 × 237 × 2,501` elements each, about 100 s with the guards.
  - **Sets and walk:** about 120 s, from TZ-11a's 123.2 s over the same 1,200 members.
  - **Self-test item 3:** `1,005,402` `log_t_cdf` calls, about 5 s.

  The session is about `1,900` s. The fail-fast (§3.1) stops the run before the session can exceed
  about `3,500` s, against the `3,600` s ceiling. Nothing is sampled, because nothing needs to be.
- **C5 — every count, with the table it was counted from.**

  | count | derivation | source |
  |---|---|---|
  | `1,314` | `443 + 433 + 438` | TZ-11a report §1.0 |
  | `21` admissible counts | 3 sets × 7 `tau` | TZ-11a report §1.2, the three "admissible" columns |
  | `280` | "280 of 400" at every `tau` | TZ-11a report §1.2 |
  | `168` | `24 × 7` | — |
  | `14` | 2 test sets × 7 `tau` | — |
  | `1,400` | `100 × 14` | — |
  | `280` guards | `20 × 14` | — |
  | `8,400` | `1,200 × 7` | TZ-11a report §1.6, "1,200 members by 7 `tau`" |
  | `14 of 14` | 2 tables × 7 | TZ-11a report V8, 21 rows less the 7 `ADMIT` rows |
  | `3` | V5's hashes | — |
  | `8` | V8's `7 + 1` | — |
  | `22` | `19 + 3` | §5.2 item 5's two tables |
  | `18` and `2` | `frozen` and `tracked` rows | map `2026-09-15-a` §0 |
  | `12,038,440` bytes | `2 × (1,332,123 + 273,814 + 4,413,283)` | TZ-11a report V3 table |
  | `971,187` anchors, `2,024` to `2,300` evaluations | — | TZ-11a report §1.1, "Fit (TZ-06 400), admissible members" |
  | `158.7` s over 63 fits | — | TZ-11a report V3 cost table |
  | `2,501` | `3000 − 500 + 1` | — |
  | `28,000` | `20,000 + 4 × 2,000` | — |
  | `26,000` | `20,000 + 3 × 2,000` | — |
  | `1,185,474` | `2 × 237 × 2,501` | 237 is test 2's largest admissible count, TZ-11a report §1.2 |
- **C6 — every population.**

  | statistic | population |
  |---|---|
  | M1 | the fit set's 280 admissible members at each `tau`, resampled with replacement |
  | M2 and M3 | the 14 populations — test 1's and test 2's admissible checkpoint rows at each `tau` |
  | M2's per-set bounds and convolution | one test set's seven, or six gated, populations |
  | V4 | the fit set: 400 members for `ADMIT`, the admissible populations for `LINK_NU` and `LINK_SCALE` |
  | V12 | M1's 24 replicates; the first 10,000 null replicates of each of the 14 populations |
  | §4 | the scored set's admissible checkpoint rows at each `tau`, and for G4 their members' anchors |
  | self-tests | synthetic inputs only |
- **C7 — every signature.** 49 committed names, read from `origin/main` at `3452fb8` by `ast`:
  - the 44 in §2's block;
  - `tz06.qualification`, `tz06.scoring_set`, `tz08a.the_set`, `tz10b.m2_labels` and `tz11a._load`,
    named in the body.

  All 49 exist as quoted. Three signatures matter most: `tz07a.lambda_hat` takes `log_cdf` as its
  second parameter; `tz11a.host_read` takes the floor as its third; and `tz11a.walk_member` takes
  `guard` as its third, passed `False` here.
- **C8 — every cross-reference.** 25 references, each resolved by reading the referenced text:
  - System Map §2.3, §4, §6, and §7 items 23, 29, 39, 44, 49, 50, 51, 54 and 55 — all in revision
    `2026-09-15-a`;
  - TZ-11a §4, and its report's §1.0, §1.1, §1.2, V2, V3 and V11;
  - TZ-07a §8 ("The TZ-08 gate"), TZ-07b §5 ("M2 — the freeze") and TZ-09 §5 ("The retention rule");
  - CANON PART II and PART VI C4;
  - the Executor contract §4.2.

  Each supports the sentence that cites it.

**Two further readings, per PART VI:**

- Every §4 critical value was checked against the function that computes it. `crit3` is a rank of
  `grid_lr`'s output, and `grid_lr` reproduces the committed `tz07a.lambda_hat` search within item 3's
  bounds. `c4` reads the committed `tz11a.fit_student`, whose search bounds are `tz11a.NU_LO` and
  `tz11a.NU_HI`.
- **Four defects were found in this reading and repaired before sending:**
  1. the push exemption (C1);
  2. two signatures the body did not use, removed from §2's block;
  3. V2's docstring exception;
  4. the matrix-product row count in §3.4, which first counted the coin draws that never enter it.
