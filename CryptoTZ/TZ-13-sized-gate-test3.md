# TZ-13 — the sized gate on test 3

**Canonical filename:** `TZ-13-sized-gate-test3.md`. The committed file takes this name and no
other.

**Executor model: Opus.** Gate arithmetic, causality and a label read.

**Required System Map revision:** `2026-09-17-a`.

**Required anchors**, from map §0. A mismatch on any one is BLOCKED before any work:

| anchor | required |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-answered-no / 2-not-started` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` |
| `A6` — pricer | `729f0bcdbee3` |

---

## 0. Gates, host, interpreter, floor

**0.1 Fingerprint.** Read `SYSTEM-MAP.md` from `origin/main`. Its revision string must read
`2026-09-17-a` and its six anchors must equal the table above. Compute `wc -l`, `wc -c` and
`sha256sum` for every row of its §0 fingerprint table: the 19 `frozen` rows must equal the hashes
printed there, the 2 `tracked` rows are reported with no expectation, and `SYSTEM-MAP.md` itself is
reported. Any `frozen` mismatch is BLOCKED.

**0.2 Host gate**, all three or this is not the capture host and the run is BLOCKED:

- `/var/lib/btc-recorder/btc-updown-5m/` exists and holds interval directories; report the count and
  the first and last `T0`.
- A recorder process is running and the newest `runtime.jsonl` start record carries sha
  `4216c04673ced76b5b2ac60ef57c9abedc46f9b9`; report the pid and the `recv_ns`.
- The filesystem holding it is `/dev/vda2`, total `31,612,203,008` bytes.

**0.3 Interpreter.** Every command of the instrument runs on `/root/tz01-env/venv/bin/python` —
Python 3.12.x with `numpy`. If `import numpy` fails the run is BLOCKED. Scratch scripts that need
only the standard library may run on the system `python3`; none of them computes a measurement.

**0.4 Resource floor, in exact bytes, derived from map §6.** Free space on `/dev/vda2` at run start
must be at least `tz11a.FLOOR_START_BYTES` = `2,060,000,000`; every later read must be at least
`tz11a.FLOOR_BYTES` = `2,000,000,000`. Both are asserted, not compared by eye. Report every read
with its UTC instant, its reader and its bound.

**0.5 Preflight, twice, at least `1,800` s apart**, the first before the build and the second before
the first full run. Each records: `df -B1` on `/dev/vda2`; `du -sb /root/PROJECT_GAMING_PS5`; the
exit codes of `systemctl is-enabled telemetry-watch.service` and `systemctl is-active
telemetry-watch.service`. Report both, the elapsed seconds, and the implied bytes/day of each
quantity. **This run's own footprint — `/root/tz13-work` and `/root/.claude` — is stated separately
at both reads** (map §7 item 29). The preflight gates nothing beyond §0.4.

**0.6 The set must exist.** §3.1 forms test 3 by a count of qualifying units. If the capture does not
yet hold `750` qualifying slots with `T0 > 1789427700`, the run is **BLOCKED**, and the report states
the count reached, the number of units considered and the first and last `T0` examined. It is not an
error and no file is committed to `research/` in that case.

---

## 1. Why this TZ exists

TZ-11a closed the Student pricer with a gate that had no stated error rate. TZ-12 measured those
rates from the pricer's own predictions and fixed a **sized gate**: each of G1 … G4 carries a
false-failure probability under the frozen pricer — `0.048` family-wise by Bonferroni — and a power
against a named alternative, a 1.5× overconfidence. A gate without that power reads UNDECIDABLE.

**This TZ applies that gate, once, to a set no one has scored and whose labels no one has read.**
Nothing is fitted here: `SD_SCALE`, `corrected_sd`, `ADMIT`, `LINK_NU`, `LINK_SCALE` and
`SIGMA_LOG_NU` are read from the committed files and never recomputed as constants. The answer this
TZ can give is **per `tau`**: NOT DISQUALIFIED, DISQUALIFIED, or UNDECIDABLE. **It cannot confirm an
edge** — Phase 1 can only disqualify — and a `tau` that survives is admitted to Phase 2 and to
nothing else.

The TZ also measures, from predictions alone, **how the gate's power grows with the size of the
scored population**, so the set size for Phase 2 is a measurement rather than the Architect's
extrapolation.

---

## 2. Scope

**Repository paths this TZ may write, and no others:**

1. `research/tz13-sized-gate-test3.py` — new file, on branch `tz-13-sized-gate-test3`, then a pull
   request. Not merged by the Executor.
2. `CryptoReports/TZ-13-sized-gate-test3-report.md` — straight to `main`, in one commit, as contract
   §4.1 requires. **This is the one path this TZ pushes to `main`, and it is an exemption to item 4
   of the prohibitions below.**

**Prohibited, each absolutely:**

1. No committed file is modified. Every `frozen` row of map §0 is byte-identical at run end.
2. Nothing under `/var/lib/btc-recorder/` is created, written, moved or removed. The recorder process
   is never signalled, stopped or restarted.
3. `/root/tz04a-env/`, `/root/tz01-env/` and `/root/btc-forensics/` are never removed or emptied.
   **Exemption:** §9 copies files *into* `/root/btc-forensics/` by exclusive create and removes
   nothing there.
4. Nothing is pushed to `main` except the report of item 2 above.
5. No quote file (`quotes.jsonl.gz`) and no market document (`gamma.json`) is opened, anywhere, for
   any interval.
6. No Release is created and no dataset, archive or binary enters git history.
7. **No label of test 3 is read before §3.3's constants are written to disk.** A label is the venue's
   resolved outcome for an interval. **Three exemptions, each named here because the TZ's own body
   calls them:** `tz06.qualification`, which `tz06.scoring_set` and `tz11a.the_sets` call for every
   unit considered and which reads `resolved_up` and `priceToBeat` to decide membership; the same
   read inside V4's re-formation of the three committed sets; and `tz10b.m2_labels`, which is the one
   label reader this TZ calls and which runs only at §3.4, after §3.3 has written its output and
   after the instrument has asserted every row still carries `label is None`.
8. No fit produces a constant. `tz11a.fit_student` is called at §3.5 and §3.6 and its output enters a
   gate reading and a disclosure table; it never enters a literal, a table frozen into a file, or a
   threshold.

---

## 3. The measurements

### 3.1 Test 3

Formed by the committed set rule, called exactly as the file holds it:

```
tz06.scoring_set(manifests, 750, after=1789427700)
```

**Assertions, each aborting the run:**

1. It returns exactly `750` members and every member's `T0` is strictly greater than `1789427700`.
2. The member set is disjoint from each of the three committed sets, which are formed in the same
   run by `tz11a.the_sets(manifests)`: three pairwise intersections, each empty.
3. `tz06.scoring_set(manifests, 400, after=1789427700)` returns exactly the first `400` members of
   test 3, in the same order. **Test 3 is a superset of the set map revision `2026-09-15-a` defined,
   and this asserts it.**
4. The member-list SHA-256 is `tz07b.member_list_sha(members)` over the sorted `T0` list. It is
   reported, not compared: no committed artifact names it.

**Disclosure, in the report:** every unit considered, in ascending `T0`, member and non-member alike,
with the reason each non-member was excluded; the count considered, the count of members, the count
of non-members by reason, and the qualifying rate. The three committed sets' member-list hashes are
asserted equal to `tz11a.FIT_SHA256`, `tz11a.TEST1_SHA256` and `tz12.TEST2_SHA256`.

### 3.2 The walk, the rows, the domain

Every member is walked by `tz11a.walk_member(t0, manifests, guard)` with `guard` false, in ascending
`T0`, and every member at every `tau` in `pfair.TAUS` becomes one row through
`tz11a.checkpoint_row(t0, name, tau, row)` with `name` `"test3"` — **`750 × 7 = 5,250` rows, every
one carrying `label = None` until §3.4.**

**The guarded pass** (map §7 item 24: a guard on an implementation shortcut samples across the scored
set and includes the pathological members by construction). `tz11a.walk_member` is run a second time
with `guard` true over a sample formed mechanically: the first `25` members in ascending `T0`, the
last `25`, and the `25` members with the largest count of excluded seconds in their run-up window as
`tz07a.excluded_seconds(t0, manifests)` returns it, ties broken by ascending `T0`. The three lists
are unioned, so the sample is at most `75` members; **its size is re-derived at run time and
reported**, and every row it produces is asserted identical to the unguarded row for the same member
and `tau`.

**The domain.** A row is admissible when its `sigma_hat` is at or above the committed literal
`pfair.ADMIT[tau]`. The admissible members per `tau` are
`tz11a.admissible_members(walked, members, pfair.ADMIT)[tau]`; report each count, each list's
`tz07b.member_list_sha`, and the admissible share of `750`. **Every statistic below names the
population it is computed over, and every gate reads the admissible rows of test 3 at that `tau`.**

### 3.3 The constants, from predictions alone, written before any label is read

For each `tau` in `pfair.TAUS`, over test 3's admissible rows at that `tau`:

```
tz12.constants(rows, tau, tz12.SET_CODES["test3"])
```

This is the frozen sizing arithmetic and it is called unchanged: `R_NULL = 20,000` null replicates
with labels drawn from the pricer's own `p_t`, `R_POWER = 2,000` replicates at each of
`LAMBDA_OVER = 1.5`, `LAMBDA_UNDER = 1/1.5` and `LAMBDA_DOUBLE = 2`, `2,000` coin replicates, the λ
grid, `k2_of`, `crit_of` and `g4_constants`. It yields, per `tau`: `E`, `k2`, the null failing-bin
distribution, `P0`, `P1`, `crit3`, `P3`, `P_under`, `P_double`, `c4`, `s` and `P4`.

**The whole of §3.3 is a property of the predictions. No label exists in the process when it runs**,
and the instrument asserts that: immediately before the first `tz12.constants` call and immediately
after the last, every one of the `5,250` rows carries `label is None`. The constants are written to
the run's output files **before** §3.4 begins, and the report states the two instants.

### 3.4 The labels, read once

`tz10b.m2_labels(members)` is called once, for test 3's `750` members, after §3.3's output is on
disk. Report the count returned and the count of members for which no label was available; a member
with no label is excluded from every observed statistic and named in the disclosure.

### 3.5 The observed statistics and the readings

Per `tau`, over test 3's admissible rows, with the labels of §3.4:

- **Brier**, `tz06.brier(pairs)`, against `tz11a.G1_BRIER` = `0.2496`.
- **Bins**, `tz06.calibration(pairs)` and `tz06.table_for(tau, rows, key, constant_brier)`: the
  eligible-bin count and the failing-bin count, by the committed definitions.
- **Scale**, `tz07a.lambda_hat(pairs, tz11a.student_log_cdf(nu))` with `nu` = `pfair.LINK_NU[tau]` —
  the committed function with the committed Student log CDF, the keyword parameter the file already
  holds.
- **Shape**, `tz11a.fit_student(r)` over `tz11a.population(walked, members, tau)` for test 3's
  admissible members: `ν̂` and `ŝ`, with the search-edge status read through
  `tz11a.bound_note(fit)`. **No search constant is named by this TZ.**

The readings are produced by `tz12.readings(consts, observed)` and the per-`tau` verdict by
`tz12.verdict(per_tau)`, both called as the file holds them, and then weakened by §4.3 and by nothing
else.

**Influence** (map §7 items 27 and 40): every statistic a verdict table reads is reported a second
time, recomputed without its single most influential member — `λ̂` through
`tz11a.lambda_with_influence(pairs, held, log_cdf)` and `ν̂` through
`tz11a.influence_refit(r, offsets, members, fit)`. Both figures are **reported, not asserted**, and
the gate is judged on the value §4 defines.

### 3.6 How the gate's power grows with the population — a projection, label-free

For each `tau`, `tz12.constants` is called two more times on row multisets built by repeating test
3's admissible rows for that `tau` twice and three times. Report `P3`, `P1` and `P4` at `1×`, `2×`
and `3×`, and the smallest multiple at which `P3` reaches `tz12.POWER_TO_PASS`.

**This is a projection and it is barred from every gate reading.** A repeated row is not a new
observation: it holds the scale of the likelihood fixed while multiplying its weight, which is what a
larger set would do to the non-centrality and is not what a larger set would do to anything else. The
report says so in the same table, and no verdict, threshold or admission reads it.

---

## 4. The gate

Fixed here, before any label of test 3 is read. Per `tau`, over test 3's admissible rows. The
thresholds are TZ-12's and are not restated as new numbers: they are read from the committed files.

**G1 — discrimination.** FAIL if the observed Brier is at or above `tz11a.G1_BRIER`. UNDECIDABLE if
`P1 < tz12.POWER_TO_PASS`, that is if a coin-flip pricer would not be caught at least half the time.

**G2 — bins.** FAIL if the failing-bin count is at or above `k2`. UNDECIDABLE if `E = 0`, at any
`tau`. Gated at `pfair.GATED_TAUS`; `tau = 10` is computed, printed and gates nothing.

**G3 — scale.** FAIL if the likelihood ratio at `λ̂` exceeds `crit3`. UNDECIDABLE if
`P3 < tz12.POWER_TO_PASS`.

**G4 — shape transfer.** FAIL if `|log(ν̂ / pfair.LINK_NU[tau])|` exceeds `c4`. UNDECIDABLE if
`P4 < tz12.POWER_TO_PASS`, if `tau` is in `tz12.SIGMA_LOG_NU_CENSORED`, or if the fit lands on a
search edge as `tz11a.bound_note` reports it.

**4.1 The verdict per `tau`.** DISQUALIFIED if any gate FAILs. NOT DISQUALIFIED only if G1 and G3
both PASS with power and no gate FAILs. UNDECIDABLE otherwise. **A `tau` that reads UNDECIDABLE
closes nothing and admits nothing**, and the report says which gate left it there.

**4.2 The family-wise rate.** `tz12.FAMILY_ALPHA` = `0.048`, as `7 × 0.001` for G1, `6 × 0.001` for
G2 and `7 × 0.0025` each for G3 and G4. It is stated, not recomputed; the report quotes
`tz12.ALPHA`, `tz12.COUNT_BOUND` and `tz12.CRIT_RANK` as the file holds them.

**4.3 The straddle rule — the one correction this TZ makes, and it is to the sizing rule alone.** A
power estimate is a fraction of `tz12.R_POWER = 2,000` replicates and carries simulation error. Where
that error covers the floor, the reading is not a decision. **For each gate whose power `P` decides
UNDECIDABLE above, the `tau` reads UNDECIDABLE whenever**

```
|P − tz12.POWER_TO_PASS|  <=  1.96 * sqrt(P * (1 − P) / tz12.R_POWER)
```

At `P = 0.5` that band is `0.5 ± 0.021913466179498`. The rule is applied **after**
`tz12.verdict(per_tau)` and can only weaken it: PASS or FAIL may become UNDECIDABLE, and UNDECIDABLE
never becomes anything else. No threshold moves, no constant moves, and `research/tz12-sized-gate.py`
is not modified.

**This correction is legitimate and this sentence is the statement CANON PART II requires: no score
under this gate exists, on any set, computed by anyone — TZ-12 read no label and produced no observed
statistic — and no label of test 3 has been read by anyone.** Tests 1 and 2 are never scored under
this gate.

**4.4 The pre-registered prediction**, written before the set exists. It is recorded beside what was
measured, and it decides nothing.

| # | predicted |
|---|---|
| 1 | test 3 forms from `810` to `840` units considered, a qualifying rate between `0.88` and `0.93` |
| 2 | the admissible share of `750` lies between `0.50` and `0.65` at every `tau` |
| 3 | `P3 >= 0.8` at `tau` 180, 120, 90 and 60; `P3` between `0.45` and `0.70` at 240; `P3 < 0.3` at 30; `P3 < 0.1` at 10 |
| 4 | `P0 <= 0.001` and `P1 >= 0.95` at every `tau` |
| 5 | the verdict reads NOT DISQUALIFIED at `tau` 180, 120 and 90; DISQUALIFIED at 60, through G3, with `λ̂ > 1`; UNDECIDABLE at 240, 30 and 10 |
| 6 | in §3.6, `tau = 10` does not reach `tz12.POWER_TO_PASS` at `3×` |

---

## 5. Implementation

### 5.1 The file, and the fixed order of the run

One new file, `research/tz13-sized-gate-test3.py`. It loads `tz12-sized-gate.py` once through an
`importlib` helper of the same shape as `tz11a._load`, and takes `tz11a`, `tz10b`, `tz08a`, `tz07b`,
`tz07a`, `tz06` and `pfair` from that module rather than loading any of them a second time. It sets
`OPENBLAS_NUM_THREADS`, `OMP_NUM_THREADS` and `MKL_NUM_THREADS` to `"1"` before its first
`import numpy`, and writes no other environment variable.

**Functions, each with the contract named here:** `the_set` (§3.1), `walk` (§3.2), `guard_sample`
(§3.2), `admissible` (§3.2), `sizing` (§3.3), `labels` (§3.4), `observed` (§3.5), `straddle` (§4.3),
`weaken` (§4.3), `projection` (§3.6), `selftests` (§5.2), `v2_static`, `v6`, `build`, `tables`,
`csv_text`, `main`.

**The order of a full run, and the instrument asserts it:**

1. host read 1, at the `tz11a.FLOOR_START_BYTES` floor, through `tz11a.host_read(when, t0s, floor)`;
2. self-tests, §5.2, all six before anything is read from the capture;
3. `v6` and the static half of `v2_static`, over the instrument's own syntax tree;
4. the three committed sets and test 3, §3.1, with every assertion of that section;
5. the walk and the guarded pass, §3.2; host read 2;
6. the domain, §3.2;
7. **the assertion that all `5,250` rows carry `label is None`**;
8. `tz12.constants` for the seven `tau`, §3.3, and its output written to disk;
9. the second `label is None` assertion, over the same rows;
10. §3.6's projection — still label-free;
11. `tz10b.m2_labels`, §3.4 — **the first label read of the run**;
12. the observed statistics, the readings, `tz12.verdict`, §4.3's weakening, and the influence
    figures;
13. host read 3, and V9's four assertions between read 1 and read 3.

### 5.2 Self-tests — six items, run before the capture is touched, each an `assert`

1. **The straddle band.** `straddle(0.5, 2000)` is true; `straddle(0.478086, 2000)` and
   `straddle(0.521914, 2000)` are false; `straddle(0.48, 2000)` and `straddle(0.52, 2000)` are true.
   The half-width at `P = 0.5` equals `0.021913466179498` to a relative `1e-12`. **The literal was
   computed by the Architect as `1.96 * sqrt(0.25 / 2000)` in IEEE double and cross-checked at 40
   decimal digits in `mpmath`, agreeing to 16 significant digits.**
2. **Weakening only.** Over nine fixed rows — each of PASS, FAIL and UNDECIDABLE crossed with a power
   inside the band, above it and below it — `weaken` never turns UNDECIDABLE into PASS or FAIL, never
   turns FAIL into PASS, and leaves every reading whose power is outside the band unchanged. Nine
   assertions.
3. **The set-formation call shape.** `tz06.scoring_set(manifests, 400, after=1789296300)` produces a
   member list whose `tz07b.member_list_sha` equals `tz12.TEST2_SHA256`. **Quoted from a committed
   artifact:** that constant is in `research/tz12-sized-gate.py` and the same value is stated in
   TZ-11a's report §1.0 and in map §2.3. This proves the `need` / `after` call shape before §3.1
   uses it.
4. **The Student CDF against closed forms independent of the implementation under test.**
   `pfair.t_cdf(z, 1)` equals `0.5 + atan(z)/π` and `pfair.t_cdf(z, 2)` equals
   `0.5 * (1 + z / sqrt(2 + z²))`, at `z` in `(−2, −0.5)`, to a relative `1e-12`. Four fixed
   literals, each computed by the Architect at 25 significant digits in `mpmath` from the closed
   form, which uses no incomplete beta: `t_cdf(−2, 1) = 0.1475836176504332741754011`,
   `t_cdf(−0.5, 1) = 0.3524163823495667258245989`,
   `t_cdf(−2, 2) = 0.09175170953613698363378599`, `t_cdf(−0.5, 2) = 1/3` exactly. Four further
   assertions of the symmetry `t_cdf(−z, ν) = 1 − t_cdf(z, ν)` at the same four points, which fix no
   literal. **Eight assertions, four literals.**
5. **`tz12.g4_power` at fixed arguments.** `g4_power(log 2, 0.1)` is `0.5` and `g4_power(0, 0.1)` is
   `1.0` — **quoted from the TZ-12 report, §4 V7, item 4, verbatim**. `g4_power(2.668167, 0.709080)`
   equals `0.00267475310692794` to a relative `1e-9`; the Architect computed it from
   `2 − Φ((c − log 2)/s) − Φ((c + log 2)/s)` in an independent implementation, and TZ-12's report §2
   prints the same quantity rounded to `0.0027`.
6. **Stream separation.** `tz12.stream(tz12.SET_CODES["test3"], 60, p)` called twice yields identical
   first `1,000` doubles; the same call with `tz12.SET_CODES["test2"]` yields a different first
   double; and two different purposes `p` yield different first doubles. Four assertions.

### 5.3 The shape of the diff

**One new file and nothing else.** No committed line is replaced: the list of replaced lines, read
from `origin/main`, is **empty**, so the diff is additive in the strict sense and `git diff
--name-only` against the merge base prints exactly `research/tz13-sized-gate-test3.py`.

---

## 6. Cost

Derived from TZ-12's measured rates, not from a mean (map §7 item 52 — each figure below is taken at
the maximum of the population it bounds).

| step | basis | seconds |
|---|---|---|
| self-tests | TZ-12 measured `6.1` | ~10 |
| `v6`, static `v2`, four set formations | TZ-12 measured `23.3` for three | ~35 |
| walk of 1,150 members, plus a guarded pass of at most 75 | TZ-12 measured `91.6` for 1,200 | ~150 |
| `tz12.constants`, 7 `tau` at ~436 admissible members | TZ-12 measured `76.1` for 14 `tau` at ~130 | ~75 |
| V4: `tz12.constants`, 7 `tau` on test 2's rows | the same, at 231–237 | ~40 |
| §3.6's projection, `2×` and `3×` | five times the base | ~375 |
| seven fits and seven influence refits | TZ-12 measured `16.2` for seven | ~55 |
| labels, observed statistics, readings, tables | — | ~30 |
| **one full run** | | **~770** |
| **the session: two full runs** | against `tz12.SESSION_CEILING_S` = `3,600` | **~1,540** |

**Fail-fast, asserted:** the first `tz12.constants` call is timed; if it exceeds `120` s the run is
BLOCKED. After it, the run projects `35 * t_first + 500` s and is BLOCKED if that exceeds `3,000` s.
No check here is sampled: every one is run in full.

---

## 7. Validation

Each check states a count. Everything called **asserted** is a Python `assert` or a `SystemExit` in
the instrument that produces the numbers; everything else is **recorded, not asserted**.

| # | check | what it must produce |
|---|---|---|
| **V1** | gates — asserted | 6 of 6 anchors; 19 of 19 `frozen` rows and 2 of 2 `tracked`; host 3 of 3; the interpreter and its `numpy` version; every free-space read with its bound, and how many were asserted |
| **V2** | label isolation — asserted two ways | **Static**, over the instrument's own syntax tree: the count of string constants scanned with docstrings exempt, the count carrying any of `resolution`, `resolved_up`, `priceToBeat`, `quotes.jsonl`, `gamma.json` (**0**), the count of calls scanned, and the count of calls of a label entry point outside §3.4 (**0**). **At run time:** `5,250` of `5,250` rows carry `label is None` at step 7 and again at step 9, and `tz10b.m2_labels` is called exactly once in the run, at step 11 |
| **V3** | determinism — asserted | two full runs from fresh processes on the same commit; the three deterministic outputs byte-identical, by `cmp` and by SHA-256 pairs. Wall clock and peak RSS per run, reported. A file holding a clock reading is not compared and is named |
| **V4** | the instrument reproduces what is committed — asserted | `pfair.ADMIT` 7 of 7, `LINK_NU` 7 of 7, `LINK_SCALE` 7 of 7 re-measured on the fit set through `tz11a.measure_admit` and `tz11a.check_literals`; `tz12.SIGMA_LOG_NU` 7 of 7 equal to the frozen literals; and **`tz12.constants` on test 2's admissible rows reproduces the TZ-12 report's §2 test-2 table exactly at 7 of 7 `tau` — `E`, `k2`, `P0`, `P1`, `crit3`, `P3`, `P_under`, `P_double`, `c4`, `s` and `P4`, 77 values.** This is what proves the gate is applied unchanged; a mismatch is BLOCKED |
| **V5** | set identity — asserted | the three committed member-list hashes equal `tz11a.FIT_SHA256`, `tz11a.TEST1_SHA256` and `tz12.TEST2_SHA256`; the four sets pairwise disjoint; §3.1's four assertions, including the first-400 superset check; test 3's own hash reported |
| **V6** | the diff — asserted | merge base and head; `git status --porcelain` for the two scoped paths; `git diff --name-only` naming one file; no attribute store, no `global`, no `nonlocal`; the `os.environ` writes, exactly the three of §5.1; the replaced-line list, **empty** |
| **V7** | the self-tests — asserted | 6 of 6 items, their assertion counts, and their output verbatim |
| **V8** | the frozen literals are not moved — asserted | `research/pfair.py` and `research/tz12-sized-gate.py` hash equal to map §0 at run start and at run end; `tz12.SIGMA_LOG_NU` and `tz12.SIGMA_LOG_NU_CENSORED` printed as read |
| **V9** | the capture is untouched — asserted | `tz11a.host_read` at run start, after the walk and at run end, with four assertions between the first and the last: the recorder pid unchanged, the newest start record unchanged, the interval count not fallen, and the read-set hash unchanged. The read set, its directory and file counts. Plus the enumeration of everything the instrument can write |
| **V10** | the fingerprint table | every row of map §0 in lines, bytes and SHA-256, with the new file beside them as it stands on the branch |
| **V11** | disclosure | test 3's units considered in ascending `T0`, members and non-members with reasons; per `tau` the admissible `T0` list's `tz07b.member_list_sha` and its count; the per-member observations file, one row per member per `tau`, sufficient to reconstruct any single row without re-running |
| **V12** | influence — recorded | per `tau`, `λ̂` and `ν̂` recomputed without the single most influential member, beside the value §4 reads; and `crit3` from the first `10,000` null replicates beside the value from `20,000` |

**Causality is not re-tested and this is why:** every quantity this TZ computes at decision time —
`state`, `sigma_hat`, `sd`, `p_t` — is produced by `tz11a.walk_member` and
`tz11a.checkpoint_row` unchanged, and TZ-11a V2 and TZ-10b V2 each proved them bit-identical under
perturbation strictly after the checkpoint instant, 140 of 140 with 140 of 140 negative controls.
This TZ adds no quantity computed at decision time. `Y`, the settlement residual, is a function of
the future by construction and is never a subject of a causality check (map §7 item 36).

---

## 8. The report

`CryptoReports/TZ-13-sized-gate-test3-report.md`, straight to `main` in one commit, and immutable
once committed.

It states, in this order: §0's gates, host, interpreter and every free-space read; §1's measurements
in §3's order, per `tau` and per population, with §3.6's projection in its own table marked as a
projection; §2's verdict table, per `tau`, naming for every UNDECIDABLE which gate left it there and
whether §4.3's band did; §3's implementation, the file's hash on the branch and the commit; §4's V1 …
V12 with their counts; §5's publication and §9; and a final section listing **every point where the
text needed a reading and every workaround chosen**, in the shape TZ-11a and TZ-12 used.

The report states `wc -l` and `sha256sum` for the map and for every file the map's fingerprint table
lists. **A report is evidence, not acceptance**, and no verdict of this TZ is final until the
Architect has re-derived its gate arithmetic.

---

## 9. Retention

In this order, each step only after the previous one exited 0:

1. **Copy first.** Every file under `/root/tz12-work/` whose SHA-256 is named by any committed report
   on `main`, and which `/root/btc-forensics/` does not already hold by hash, is copied there by
   exclusive create, with the hash asserted at source and destination. Assert that every file already
   in `/root/btc-forensics/` is unchanged. Report the counts before and after.
2. **Then the worktree**, `git worktree remove` without `--force`.
3. **Then the tree**, `rm -rf /root/tz12-work`, one command naming one tree, verified by `test -e`.
   **If the session's permission classifier refuses it, hand the Boss one exact block and verify the
   outcome from `test -e` afterwards, never from his report** (map §6).

`/root/tz13-work/` is the next TZ's to reclaim on the same terms. The capture is never deleted.

---

## 10. Pre-send checks

Performed against this file, start to end, as a separate reading after its last section was written.

**C1 — scope against body.** Enumerated: **2** repository paths this TZ may write, **7** other
repository paths it names (`SYSTEM-MAP.md`, `BTC-EXECUTOR-INSTRUCTIONS.md`, `research/pfair.py`,
`research/tz06-calibration.py`, `research/tz07a-variance-time.py`,
`research/tz11a-student-link.py`, `research/tz12-sized-gate.py`), **5** host paths, and **51**
committed entry points, counted from the finished file. Intersections with §2's prohibition list:
**3** — the label read of `tz06.qualification` inside set formation, the same read inside V4, and
`tz10b.m2_labels` at §3.4; each is written into §2 as a named exemption, and `/root/btc-forensics/`
carries a fourth, for §9's copy. The push of the report to `main` is a fifth, named in §2 item 2.
The diff was performed, not intended.

**C2 — origin of every expectation.** **32** fixed numeric expectations in §5 and §7. **8** computed
by an implementation independent of the one under test and cross-checked at 25 to 40 decimal digits
in `mpmath`: the straddle half-width and its two band endpoints, the four Student-CDF literals at
`ν` 1 and 2 — closed forms that use no incomplete beta and no normal quadrature from the file under
test — and `g4_power(2.668167, 0.709080)`. **16** quoted from committed artifacts, named in place:
`tz12.TEST2_SHA256`, the two `g4_power` values from the TZ-12 report's V7 item 4, V4's 77 values from
that report's §2 test-2 table, the six anchors, `tz11a.FLOOR_START_BYTES` and `tz11a.FLOOR_BYTES`,
the filesystem total and the recorder sha from map §6, and `1789427700` and `1789296300` from map
§2.3. **2** tolerances between two implementations, `1e-12` in items 1 and 4 and `1e-9` in item 5.
**6** exact by construction, each re-derived under C5. **None depends on a quantity this TZ
measures.** §4's thresholds are not literals in this TZ at all: they are read from the committed
files at run time.

**C3 — shape of every diff.** One new file. The committed lines the change replaces, read from
`origin/main` at `44d77008a7cf5625c0c19b2e02250e18a8bed51c`: **none**. The words "insertions only"
are used in §5.3 and are correct because the replaced-line list is empty.

**C4 — cost of every check.** §6 states each step in seconds at TZ-12's measured rate, each derived
from the maximum of the population it bounds: **~770 s per run, ~1,540 s for the session**, against
`3,600`. Nothing is above `3,600` s and nothing is sampled: the one sampled quantity, §3.2's guarded
pass, is sampled under a rule stated in §3.2 and is a guard, not a measurement. The fail-fast bounds
the run at `3,000` s projected.

**C5 — every count.** Re-derived from the sets §3 defines, each named beside its source: `750`
members and `5,250` rows from §3.1 and §3.2; `400` in §3.1 item 3 and in self-test item 3, from map
§2.3 and `tz12.TEST2_SHA256`; `1,150` walked members from §3.1 plus test 2's 400 in V4; `at most 75`
in §3.2's guarded sample, `25 + 25 + 25` before the union, re-derived at run time; `20,000` and
`2,000` from `tz12.R_NULL` and `tz12.R_POWER`; `19` `frozen` and `2` `tracked` rows from map §0's
table as this revision holds it; **77** values in V4, counted from the TZ-12 report's §2 test-2
table, which has 7 rows and 11 gated columns.

**C6 — every population.** Named for each statistic: §3.3's constants, §3.5's Brier, bins, `λ̂` and
`ν̂`, and §4's four gates all read **test 3's admissible rows at that `tau`**; §3.6's projection reads
**the same rows repeated twice and three times**; V4's reproduction reads **test 2's admissible rows
at that `tau`**; V4's `ADMIT`, `LINK_NU` and `LINK_SCALE` read **the fit set's admissible rows**;
§3.2's guard reads **the 75-member sample of test 3**.

**C7 — every signature.** All **51** committed entry points were read from `origin/main` at
`44d77008a7cf5625c0c19b2e02250e18a8bed51c` through `git show`, and every one this TZ writes as a call
is quoted as the file holds it — among them
`tz06.scoring_set(manifests, need=SET_SIZE, *, after=None)`, so §3.1's positional `750` and
keyword-only `after` are correct; `tz07a.lambda_hat(pairs, log_cdf=None)`;
`tz11a.walk_member(t0, manifests, guard)`; `tz11a.checkpoint_row(t0, name, tau, row)`;
`tz11a.host_read(when, t0s, floor)`, which takes a floor where `tz10b.host_read(when, t0s)` does not;
`tz11a.admissible_members(walked, members, admit)`; `tz11a.population(walked, members, tau)`;
`tz11a.influence_refit(r, offsets, members, fit)`;
`tz11a.lambda_with_influence(pairs, held, log_cdf)`; `tz11a.bound_note(fit)`;
`tz12.constants(rows, tau, set_code)`; `tz12.readings(consts, observed)`; `tz12.verdict(per_tau)`;
`tz12.g4_power(c4, s)`; `tz12.stream(set_code, tau, purpose)`; `tz10b.m2_labels(members)`;
`tz07b.member_list_sha(members)`; `tz07a.excluded_seconds(t0, manifests)`. **No search-bound constant
is named**: §3.5 reads the edge status through `tz11a.bound_note` instead, because the bounds are not
module-level plain assignments and a name written from memory is exactly the defect this check
exists to stop.

**C8 — every cross-reference.** **19** resolved by reading the referenced text: CANON PART II's
sampling-rule clause (§4.3), PART III hard rules 1, 2, 5, 8 and 9 (§0, §0.6, §8), the CANON's
priority 1 (§1), map §0 (§0.1, V1, V10), §2.3 (§3.1, C5), §6 (§0.4, §9), §7 items 24, 27, 29, 36, 40,
52 and 56 (§3.2, §3.5, §0.5, V7's note, §6, §4.3), and contract §3.2 and §4.1 (§2, §8). Each supports
the sentence that makes it.
