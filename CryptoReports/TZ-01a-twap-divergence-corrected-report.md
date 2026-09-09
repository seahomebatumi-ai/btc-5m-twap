# TZ-01a - TWAP divergence measurement, corrected re-run - report

The TZ-01 measurement re-run under the causal reading of TZ-01a section 1: at a checkpoint
`t` seconds into the interval the readable bars are `0 .. t-1`, and `S_t` and `twap_so_far`
are both derived from that one slice.

Both gates were evaluated. **Gate A FAIL under both variants. Gate B PASS under both
variants.** The deciding numbers are in section 4.

This report supersedes the TZ-01 report by reference. The TZ-01 report is committed to
`main` unchanged, as required by TZ-01a section 6; nothing in it was rewritten or deleted.

---

## 1. What was run

| field | value |
|---|---|
| window | 2024-09 to 2026-08, the 24 calendar months ending with the last complete month before the run date (2026-09-09) |
| source | `data.binance.vision`, public archive, spot `BTCUSDT`, 1-second klines |
| archives downloaded | 24, each verified against its published `.CHECKSUM` before use |
| reading | TZ-01a section 1, `S_t = interval_closes[t-1]`, one slice, one boundary |
| raw 1-second bars read | 63,072,000 |
| intervals found | 210,240 |
| intervals used | 210,234 |
| checkpoint observations written | 1,051,170 |
| days covered | 730 |
| network access | the public archive only; no exchange keys, no order placement, no Polymarket or trading-venue API calls |

Processing was one month at a time: download, verify checksum, process, write the month's
Parquet partition, rewrite the combined Parquet and the partial summary, delete the raw
archive. All 24 raw archives were deleted. The run is resumable from any month because each
month's partition and the 1800-second carry tail that feeds the next month are on disk.

The 24 partitions, the carry tails and the combined Parquet were rebuilt from scratch; no
artefact of the TZ-01 run was reused. TZ-01's `research/out/` was moved out of the
repository to `/root/tz01-out-archive/tz01-out` before the re-run started, not deleted.

---

## 2. Files created

SHA-256 over file bytes. The report cannot state its own hash. Directory rows hash the
sorted list of `sha256 filename` lines of their contents.

| path | lines | bytes | SHA-256 |
|---|---|---|---|
| `research/twap-divergence.py` | 1,135 | 50,928 | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` |
| `.gitignore` | 5 | 252 | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` |
| `research/out/twap-divergence-summary.md` | 861 | 42,356 | `af6f08e5f414a2e87209d958020e4d002890f1ab42dfed4d2603faff5955f554` |
| `research/out/twap-divergence-contamination.md` | 52 | 2,572 | `cbd8f385477d4cde6ae7fa47e1385dc7336268ce810b20a96ac47fc5d1940986` |
| `research/out/twap-divergence-observations.parquet` | 1,051,170 rows | 76,818,669 | `229a944f2d5111c3e68b1fa0630f8e8658356147f9669d18665e575b60f3716b` |
| `research/out/partitions/` (24 files) | n/a (binary) | 77,385,512 | `24c073912ec8c0982411b6c9ed441989a1cfc42e305524d80b2313f2514bcddc` |
| `research/out/state/` (25 files) | n/a (binary) | 769,029 | `4e46a99bb15aca71af9fad9c75f9df3faea582180deacb67d8c5420d0e8a3be0` |

Per TZ-01a section 6, everything under `research/out/` is git-ignored except the two
summary Markdown files. The `.gitignore` was added on this branch and is the only file
created outside `research/` and `CryptoReports/`; TZ-01a section 6 requires it.

The Parquet carries one row per checkpoint observation with `interval_open_ts`, `tau`, `t`,
`K`, `S_t`, `naive_move`, `twap_so_far`, `state`, both sigmas, both `sd_remaining`, both
probabilities under both sigmas, the three TWAPs, the three outcome labels and the per
interval gap counts - enough to reconstruct any single observation without re-running the
pipeline.

---

## 3. Validation (section 7)

37 checks were run, 37 passed, 0 failed.

### 7.1 Compilation

`python3 -m py_compile` on `research/twap-divergence.py` and
`research/selftest-twap-divergence.py`: clean, no output, exit 0 for both.

### Section 2 - analytic self-tests, as amended

28 assertions, 28 passed, 0 failed, at a fixture price of `K = 100000.0`.

| path | expectation | result |
|---|---|---|
| flat at `K` | `state == 0` and `p_twap == 0.5` at all five taus, both sigma variants | 15 assertions, exact |
| linear ramp `K` to `K + 100` | `twap_so_far == K + 50*t/300` to 1e-9 at all five taus | 5 assertions, max error 1.455e-11 |
| step up, bars 0..178 at `K`, bars 179..299 at `K + 70` | `twap_so_far == K + 70/180` | exact, error 0.000e+00 |
| step up | `S_t == K + 70` at `tau = 120` | exact |
| step up | `state == 8470` at `tau = 120` | 8470.000000000291, deviation 2.910e-10 |
| round trip, bars 0..178 at `K + 40`, bars 179..299 at `K` | `twap_so_far == K + 40*179/180` | exact, error 0.000e+00 |
| round trip | `S_t == K` at `tau = 120` | exact |
| round trip | `state == 7160` at `tau = 120` | 7160.000000000582, deviation 5.821e-10 |
| round trip | `p_twap - p_naive > 0.10` at `tau = 120` | gap 0.5000 under both variants |

The two `state` equalities are the only expectations in this TZ that could not be met as
written. They are unreachable in IEEE-754 at any realistic price and are recorded in
section 8; the Architect directed a 1e-6 tolerance and this note rather than a BLOCKED
report. Every run prints the deviation achieved.

### Section 3 - perturbation test

| check | count | result |
|---|---|---|
| intervals sampled from 2026-08, seed 20260908 | 500 | - |
| checkpoints exercised (5 taus per interval) | 2,500 | - |
| value comparisons after replacing every bar `>= t` with `close * 3.0` | 22,500 | **0 mismatches**, bit-identical on IEEE-754 bits |
| negative-control assertions, perturbing bar `t-1` | 7,500 | **0 unchanged**; `S_t`, `twap_so_far` and `state` moved every time |

The compared fields are `naive_move`, `twap_so_far`, `state`, `sigma_pre`, `sigma_live`,
`p_twap_pre`, `p_naive_pre`, `p_twap_live`, `p_naive_live` - nine fields at each of 2,500
checkpoints. The truncation test of TZ-01 section 7.3 was withdrawn and is not run.

### Section 7 - one slice, one boundary, asserted on the source

Six assertions on the parsed source of `research/twap-divergence.py`, all passed:

| assertion | line |
|---|---|
| `compute_observation` subscripts `interval_closes` exactly once | 167 |
| that expression is the checkpoint slice `interval_closes[:t]`, bound to `readable_closes` | 167 |
| `S_t` is derived from `readable_closes` | 171 |
| `twap_so_far` is derived from `readable_closes` | 172 |
| `compute_observation_tz01_reading`, kept only for section 5, subscripts it more than once | 192, 193, 195 |

Every section 3 formula lives in one function, `checkpoint_quantities` (line 91). It reads
no interval at all: the caller hands it `S_t`, `twap_so_far` and the `sigma_live` window,
so the corrected reading and the TZ-01 reading share one implementation of the arithmetic
and differ only in which bars they read.

### 7.4 Coverage counts

| count | value |
|---|---|
| months processed | 24 |
| raw 1-second bars read | 63,072,000 |
| intervals found | 210,240 |
| intervals skipped for gaps (more than 5 of 300 bars missing) | 0 |
| intervals skipped for missing 30-minute history | 6 |
| intervals used | 210,234 |
| bars forward-filled inside used intervals | 0 |
| used intervals with a forward-filled prior window | 0 |
| checkpoint observations written | 1,051,170 |

The six skipped intervals are the first 30 minutes of 2024-09-01, which have no prior
window inside the run. The archive had no missing seconds anywhere in the 24 months:
63,072,000 bars is exactly 730 days of 86,400 seconds.

### 7.5 Determinism

2026-08 reprocessed into a scratch file and compared with the partition on disk:
byte-identical, SHA-256 `a24d3720a3a47e53...` both times.

### 7.6 No-regression statement

Nothing outside `research/` and `CryptoReports/` was created or modified, except
`.gitignore`, which TZ-01a section 6 requires this branch to add. The Python virtual
environment (`/root/tz01-env/`), the raw-archive scratch space (`/tmp/tz01a-work/`) and the
archived TZ-01 output (`/root/tz01-out-archive/`) are outside the repository.

---

## 4. Gate verdicts

Every result is produced twice, once under `sigma_pre` and once under `sigma_live`. They
are reported separately, neither averaged with nor preferred to the other, so each gate
carries a verdict per variant.

### Gate A (TZ-01a section 4) - directional inversions only: **FAIL under both variants**

Threshold: inversions at `tau` in {120, 180} are at least 0.15% of observations. An
inversion is `p_naive >= 0.85 and p_twap <= 0.60`, or `p_naive <= 0.15 and p_twap >= 0.40`.

| variant | tau | observations | inversions | rate | events per day | verdict |
|---|---|---|---|---|---|---|
| `sigma_pre` | 120 | 210,234 | 85 | 0.040% | 0.116 | - |
| `sigma_pre` | 180 | 210,234 | 1 | 0.000% | 0.001 | - |
| `sigma_pre` | both, over observations at those taus | 420,468 | **86** | **0.020%** | 0.118 | FAIL |
| `sigma_pre` | both, over all observations | 1,051,170 | **86** | **0.008%** | 0.118 | FAIL |
| `sigma_live` | 120 | 210,234 | 137 | 0.065% | 0.188 | - |
| `sigma_live` | 180 | 210,234 | 0 | 0.000% | 0.000 | - |
| `sigma_live` | both, over observations at those taus | 420,468 | **137** | **0.033%** | 0.188 | FAIL |
| `sigma_live` | both, over all observations | 1,051,170 | **137** | **0.013%** | 0.188 | FAIL |

The deciding number is the largest rate any variant reaches under either denominator:
**0.033%**, against a 0.150% threshold - short by a factor of 4.5. In absolute terms the
gate counted **86 inversions under `sigma_pre` and 137 under `sigma_live` in 730 days**:
0.118 and 0.188 events per day.

Both denominators are reported because TZ-01a section 4 restricts the numerator to two of
the five checkpoints while stating the threshold against "all observations". The verdict is
FAIL under both readings and under both variants, so nothing hinges on the ambiguity.
Neither rate was adjusted.

Where the inversions are, for the record - measurement 2, all five checkpoints, `sigma_pre`
then `sigma_live`:

| tau | inversions, `sigma_pre` | share | inversions, `sigma_live` | share |
|---|---|---|---|---|
| 240 | 0 | 0.000% | 0 | 0.000% |
| 180 | 1 | 0.000% | 0 | 0.000% |
| 120 | 85 | 0.040% | 137 | 0.065% |
| 90 | 584 | 0.278% | 1,243 | 0.591% |
| 60 | 2,416 | 1.149% | 4,325 | 2.057% |
| all | 3,086 | 0.294% | 5,705 | 0.543% |

### Gate B - is the TWAP model correct? **PASS under both variants**

Two conditions, both required: `p_twap` has a strictly lower Brier score than `p_naive`,
and inside the inversion cells the realised frequency is within 0.05 of the mean `p_twap`
of those cells. Label `outcome_1s`.

| variant | Brier `p_twap` | Brier `p_naive` | Brier test | inversion cell obs | mean `p_twap` | realised | absolute error | calibration test | Gate B |
|---|---|---|---|---|---|---|---|---|---|
| `sigma_pre` | **0.0781** | 0.1145 | PASS | 3,086 | 0.4993 | 0.5049 | **0.0056** | PASS | **PASS** |
| `sigma_live` | **0.0785** | 0.1057 | PASS | 5,705 | 0.5043 | 0.5113 | **0.0070** | PASS | **PASS** |

The calibration condition is evaluated on the union of the two cells, as written. Each cell
also satisfies it separately:

| variant | cell | observations | mean `p_twap` | mean `p_naive` | realised | absolute error |
|---|---|---|---|---|---|---|
| `sigma_pre` | `p_naive`>=0.85 & `p_twap`<=0.60 | 1,518 | 0.1955 | 0.9124 | 0.2319 | 0.0364 |
| `sigma_pre` | `p_naive`<=0.15 & `p_twap`>=0.40 | 1,568 | 0.7934 | 0.0885 | 0.7691 | 0.0243 |
| `sigma_live` | `p_naive`>=0.85 & `p_twap`<=0.60 | 2,797 | 0.1875 | 0.9153 | 0.2327 | 0.0453 |
| `sigma_live` | `p_naive`<=0.15 & `p_twap`>=0.40 | 2,908 | 0.8090 | 0.0867 | 0.7792 | 0.0298 |

---

## 5. Contamination measurement (section 5)

2026-08, the most recent complete month, computed twice: once under the corrected reading
and once under TZ-01's. Same bars, same intervals, same formulas; the only difference is
which bars each reading may see. The TZ-01 reading is reproduced exactly as TZ-01 shipped
it, `S_t = interval_closes[t]` and `sigma_live` over `interval_closes[:t + 1]`.

The look-ahead was worth **0.0012 Brier points to `p_twap` and 0.0006 to `p_naive` under
`sigma_pre`** (0.0015 and 0.0007 under `sigma_live`) - it flattered the model being tested
by roughly a factor of two against its benchmark, in the direction TZ-01a section 0
predicted. Both models scored better with it than without it at every tau except
`p_naive` at `tau = 60`.

One month, 2026-08, with every observation computed twice: once under the corrected causal reading of TZ-01a section 1, once under TZ-01's reading. Nothing else differs - same bars, same intervals, same formulas. The label is `outcome_1s`.

| reading | definition | observations | intervals |
|---|---|---|---|
| corrected | `TZ-01a section 1: S_t = interval_closes[t-1]` | 44,640 | 8,928 |
| tz01 | `TZ-01: S_t = interval_closes[t]` | 44,640 | 8,928 |

### Brier score by reading

| variant | model | corrected | TZ-01 reading | TZ-01 minus corrected |
|---|---|---|---|---|
| sigma_pre | p_twap | 0.0849 | 0.0837 | -0.0012 |
| sigma_pre | p_naive | 0.1197 | 0.1191 | -0.0006 |
| sigma_live | p_twap | 0.0839 | 0.0824 | -0.0015 |
| sigma_live | p_naive | 0.1086 | 0.1079 | -0.0007 |

A negative last column means the TZ-01 reading scored better - the value of one second of look-ahead, in Brier points.

### Corrected Gate A inversion count by reading

| variant | reading | inversions at tau in {120, 180} | rate over those taus | rate over all observations | events per day |
|---|---|---|---|---|---|
| sigma_pre | corrected | 5 | 0.028% | 0.011% | 0.161 |
| sigma_pre | tz01 | 4 | 0.022% | 0.009% | 0.129 |
| sigma_live | corrected | 6 | 0.034% | 0.013% | 0.194 |
| sigma_live | tz01 | 4 | 0.022% | 0.009% | 0.129 |

### Realised frequency inside the inversion cells by reading

| variant | reading | observations | mean p_twap | mean p_naive | realised frequency | |realised - mean p_twap| |
|---|---|---|---|---|---|---|
| sigma_pre | corrected | 124 | 0.5155 | 0.4723 | 0.5565 | 0.0410 |
| sigma_pre | tz01 | 126 | 0.5125 | 0.4868 | 0.5397 | 0.0272 |
| sigma_live | corrected | 212 | 0.5087 | 0.4726 | 0.5472 | 0.0385 |
| sigma_live | tz01 | 213 | 0.5147 | 0.4825 | 0.5305 | 0.0158 |

### Brier score by tau and reading

| variant | tau | brier p_twap corrected | brier p_twap TZ-01 | brier p_naive corrected | brier p_naive TZ-01 |
|---|---|---|---|---|---|
| sigma_pre | 240 | 0.1748 | 0.1728 | 0.1857 | 0.1840 |
| sigma_pre | 180 | 0.1152 | 0.1137 | 0.1362 | 0.1351 |
| sigma_pre | 120 | 0.0644 | 0.0631 | 0.1001 | 0.0994 |
| sigma_pre | 90 | 0.0436 | 0.0429 | 0.0891 | 0.0890 |
| sigma_pre | 60 | 0.0267 | 0.0260 | 0.0875 | 0.0878 |
| sigma_live | 240 | 0.1765 | 0.1740 | 0.1779 | 0.1760 |
| sigma_live | 180 | 0.1145 | 0.1128 | 0.1231 | 0.1219 |
| sigma_live | 120 | 0.0628 | 0.0612 | 0.0857 | 0.0849 |
| sigma_live | 90 | 0.0413 | 0.0405 | 0.0770 | 0.0769 |
| sigma_live | 60 | 0.0245 | 0.0236 | 0.0794 | 0.0797 |


---

## 6. Do the corrected verdicts differ from TZ-01's?

**Gate A differs: TZ-01 PASS, TZ-01a FAIL.** Gate B does not: PASS in both.

TZ-01's Gate A counted `|p_twap - p_naive| >= 0.15` and passed on 37.022%, its smallest
per-variant rate. That quantity is not smaller under the corrected reading - it is 46.657%
and 42.753% at `tau` 120 and 180 under `sigma_pre`, 37.110% and 37.750% under `sigma_live`,
all still far above the old 3% threshold. Gate A changed verdict because TZ-01a section 4
changed what is counted, not because the causality correction moved the old number. Under
the corrected Gate A the count at `tau` in {120, 180} is 86 and 137 inversions in 730 days.

Gate B: TZ-01 reported Brier 0.0770 against 0.1140 (`sigma_pre`) and 0.0773 against 0.1051
(`sigma_live`), with inversion-cell absolute errors 0.0075 and 0.0046. TZ-01a reports
0.0781 against 0.1145 and 0.0785 against 0.1057, with errors 0.0056 and 0.0070. Both
conditions hold in both runs.

---

## 7. Named plainly: everything that could not be implemented exactly as written

**1. TZ-01a section 2's two `state` equalities are unreachable in IEEE-754.**
`state = t * (twap_so_far - K) + tau * (S_t - K)` routes the elapsed mean through
`K + 7/18` for the step-up path and `K + 40*179/180` for the round trip. Neither has an
exact binary representation at any `K`, so `t * (twap_so_far - K)` cannot land on exactly
70 or 7160. At `K = 100000` the implementation returns 8470.000000000291 and
7160.000000000582 - relative misses of 3.4e-14 and 8.1e-14. `S_t` and `twap_so_far`
themselves match their hand-derived values bit-for-bit, so the causal content of both paths
is checked exactly; only the final equality is affected. The expectations do hold exactly at
some fixture prices - `K = 1.0` is one - but that is luck of rounding, not construction, and
would break under a different summation order. This was put to the Architect, who directed
a 1e-6 absolute tolerance on `state` plus this note, rather than a BLOCKED report. The
tolerance is stated as a constant in `research/selftest-twap-divergence.py` and every run
prints the deviation achieved. Nothing else in the TZ was relaxed.

**2. Gate A's denominator is ambiguous.** TZ-01a section 4 restricts the numerator to
`tau` in {120, 180} but states the threshold against "all observations". Both denominators
are computed and reported; the verdict is FAIL under both, so the ambiguity does not decide
anything. Neither rate was adjusted.

**3. `sigma_live`'s window follows the corrected boundary.** TZ-01 section 3 defines it as
running "up to and including the checkpoint bar", which TZ-01 implemented as
`interval_closes[:t + 1]`. Under section 1's rule the last bar closed at or before the
checkpoint is bar `t-1`, so the window now ends there. TZ-01a does not restate this, but
section 3's perturbation test requires it: `sigma_live` must be bit-identical when every
bar `>= t` is perturbed, which the old window would fail. The TZ-01 reading kept for
section 5 retains the old window, so the contamination comparison reproduces what TZ-01
actually shipped.

**4. The branch could not be pushed and no pull request could be opened.** This environment
has no GitHub credentials (`fatal: could not read Username for 'https://github.com'`) and no
`gh` CLI. Branch `tz-01a-twap-divergence-corrected` and the commit on `main` carrying this
report exist locally only. Both need pushing by someone with credentials; nothing was merged.

**5. The venue limitation of TZ-01 section 2 still stands.** This is Binance spot
`BTCUSDT`, not the Chainlink oracle stream Polymarket settles on. The measurement is a
geometric property of price paths and does not depend on the venue; settlement-accurate
labelling is TZ-02's problem. No workaround was attempted.

**6. TZ-01's `research/out/` was archived, not committed and not deleted.** TZ-01 section 6
required committing its combined Parquet; that never happened, and TZ-01a section 6 forbids
committing `research/out/` now. The TZ-01 artefacts were moved to
`/root/tz01-out-archive/tz01-out` (148 MB) before this re-run rebuilt the directory from
scratch.

---

## 8. Measurements (section 4), in full

Label is `outcome_1s` throughout except where a table names another. These are the tables of
`research/out/twap-divergence-summary.md` verbatim, minus its gate section, which is
section 4 above.

### Coverage counts (section 7.4)

| month | raw 1s bars | intervals found | skipped for gaps | skipped for missing history | intervals used | bars forward-filled in used intervals | used intervals with a filled prior window | checkpoint observations |
|---|---|---|---|---|---|---|---|---|
| 2024-09 | 2,592,000 | 8,640 | 0 | 6 | 8,634 | 0 | 0 | 43,170 |
| 2024-10 | 2,678,400 | 8,928 | 0 | 0 | 8,928 | 0 | 0 | 44,640 |
| 2024-11 | 2,592,000 | 8,640 | 0 | 0 | 8,640 | 0 | 0 | 43,200 |
| 2024-12 | 2,678,400 | 8,928 | 0 | 0 | 8,928 | 0 | 0 | 44,640 |
| 2025-01 | 2,678,400 | 8,928 | 0 | 0 | 8,928 | 0 | 0 | 44,640 |
| 2025-02 | 2,419,200 | 8,064 | 0 | 0 | 8,064 | 0 | 0 | 40,320 |
| 2025-03 | 2,678,400 | 8,928 | 0 | 0 | 8,928 | 0 | 0 | 44,640 |
| 2025-04 | 2,592,000 | 8,640 | 0 | 0 | 8,640 | 0 | 0 | 43,200 |
| 2025-05 | 2,678,400 | 8,928 | 0 | 0 | 8,928 | 0 | 0 | 44,640 |
| 2025-06 | 2,592,000 | 8,640 | 0 | 0 | 8,640 | 0 | 0 | 43,200 |
| 2025-07 | 2,678,400 | 8,928 | 0 | 0 | 8,928 | 0 | 0 | 44,640 |
| 2025-08 | 2,678,400 | 8,928 | 0 | 0 | 8,928 | 0 | 0 | 44,640 |
| 2025-09 | 2,592,000 | 8,640 | 0 | 0 | 8,640 | 0 | 0 | 43,200 |
| 2025-10 | 2,678,400 | 8,928 | 0 | 0 | 8,928 | 0 | 0 | 44,640 |
| 2025-11 | 2,592,000 | 8,640 | 0 | 0 | 8,640 | 0 | 0 | 43,200 |
| 2025-12 | 2,678,400 | 8,928 | 0 | 0 | 8,928 | 0 | 0 | 44,640 |
| 2026-01 | 2,678,400 | 8,928 | 0 | 0 | 8,928 | 0 | 0 | 44,640 |
| 2026-02 | 2,419,200 | 8,064 | 0 | 0 | 8,064 | 0 | 0 | 40,320 |
| 2026-03 | 2,678,400 | 8,928 | 0 | 0 | 8,928 | 0 | 0 | 44,640 |
| 2026-04 | 2,592,000 | 8,640 | 0 | 0 | 8,640 | 0 | 0 | 43,200 |
| 2026-05 | 2,678,400 | 8,928 | 0 | 0 | 8,928 | 0 | 0 | 44,640 |
| 2026-06 | 2,592,000 | 8,640 | 0 | 0 | 8,640 | 0 | 0 | 43,200 |
| 2026-07 | 2,678,400 | 8,928 | 0 | 0 | 8,928 | 0 | 0 | 44,640 |
| 2026-08 | 2,678,400 | 8,928 | 0 | 0 | 8,928 | 0 | 0 | 44,640 |
| total | 63,072,000 | 210,240 | 0 | 6 | 210,234 | 0 | 0 | 1,051,170 |

### Outcome label cadence (section 3)

Pairwise disagreement between the three settlement labels, one row per interval.

| pair | intervals | disagreements | share |
|---|---|---|---|
| outcome_1s vs outcome_30s | 210,234 | 4,018 | 1.911% |
| outcome_1s vs outcome_60s | 210,234 | 8,719 | 4.147% |
| outcome_30s vs outcome_60s | 210,234 | 6,439 | 3.063% |

### Measurements 1 to 5 under sigma_pre

#### All 24 months
Measurement 1 - disagreement rate (|p_twap - p_naive| >= 0.15)
| tau | observations | disagreements | share | mean gap | 99th pct gap |
|---|---|---|---|---|---|
| 240 | 210,234 | 36,637 | 17.427% | 0.0939 | 0.1761 |
| 180 | 210,234 | 89,881 | 42.753% | 0.1277 | 0.2740 |
| 120 | 210,234 | 98,089 | 46.657% | 0.1506 | 0.4568 |
| 90 | 210,234 | 92,344 | 43.924% | 0.1584 | 0.6044 |
| 60 | 210,234 | 82,018 | 39.013% | 0.1623 | 0.7867 |
| all | 1,051,170 | 398,969 | 37.955% | 0.1386 | 0.6044 |

Measurement 2 - inversion rate
| tau | observations | p_naive>=0.85 & p_twap<=0.60 | share | p_naive<=0.15 & p_twap>=0.40 | share | either | share |
|---|---|---|---|---|---|---|---|
| 240 | 210,234 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 180 | 210,234 | 1 | 0.000% | 0 | 0.000% | 1 | 0.000% |
| 120 | 210,234 | 39 | 0.019% | 46 | 0.022% | 85 | 0.040% |
| 90 | 210,234 | 285 | 0.136% | 299 | 0.142% | 584 | 0.278% |
| 60 | 210,234 | 1,193 | 0.567% | 1,223 | 0.582% | 2,416 | 1.149% |
| all | 1,051,170 | 1,518 | 0.144% | 1,568 | 0.149% | 3,086 | 0.294% |

Measurement 3 - calibration of p_twap (label outcome_1s)
| predicted bucket | observations | mean predicted | realised frequency | note |
|---|---|---|---|---|
| [0.00, 0.05) | 297,797 | 0.0052 | 0.0089 |  |
| [0.05, 0.10) | 35,659 | 0.0736 | 0.0732 |  |
| [0.10, 0.15) | 28,164 | 0.1245 | 0.1144 |  |
| [0.15, 0.20) | 25,200 | 0.1746 | 0.1500 |  |
| [0.20, 0.25) | 23,432 | 0.2249 | 0.1980 |  |
| [0.25, 0.30) | 22,574 | 0.2747 | 0.2448 |  |
| [0.30, 0.35) | 22,041 | 0.3248 | 0.2935 |  |
| [0.35, 0.40) | 21,752 | 0.3751 | 0.3447 |  |
| [0.40, 0.45) | 20,891 | 0.4250 | 0.4027 |  |
| [0.45, 0.50) | 30,664 | 0.4830 | 0.4371 |  |
| [0.50, 0.55) | 29,732 | 0.5175 | 0.5590 |  |
| [0.55, 0.60) | 20,796 | 0.5749 | 0.5997 |  |
| [0.60, 0.65) | 21,697 | 0.6251 | 0.6546 |  |
| [0.65, 0.70) | 21,786 | 0.6752 | 0.7118 |  |
| [0.70, 0.75) | 22,726 | 0.7253 | 0.7568 |  |
| [0.75, 0.80) | 23,375 | 0.7752 | 0.8004 |  |
| [0.80, 0.85) | 25,065 | 0.8255 | 0.8442 |  |
| [0.85, 0.90) | 27,885 | 0.8757 | 0.8832 |  |
| [0.90, 0.95) | 35,449 | 0.9263 | 0.9252 |  |
| [0.95, 1.00] | 294,485 | 0.9947 | 0.9910 |  |

Measurement 3 - calibration of p_naive (label outcome_1s)
| predicted bucket | observations | mean predicted | realised frequency | note |
|---|---|---|---|---|
| [0.00, 0.05) | 100,292 | 0.0145 | 0.0043 |  |
| [0.05, 0.10) | 42,853 | 0.0744 | 0.0160 |  |
| [0.10, 0.15) | 40,005 | 0.1250 | 0.0275 |  |
| [0.15, 0.20) | 40,597 | 0.1752 | 0.0464 |  |
| [0.20, 0.25) | 42,278 | 0.2251 | 0.0692 |  |
| [0.25, 0.30) | 45,428 | 0.2754 | 0.1066 |  |
| [0.30, 0.35) | 47,885 | 0.3253 | 0.1610 |  |
| [0.35, 0.40) | 51,172 | 0.3752 | 0.2306 |  |
| [0.40, 0.45) | 52,995 | 0.4251 | 0.3166 |  |
| [0.45, 0.50) | 58,377 | 0.4775 | 0.4196 |  |
| [0.50, 0.55) | 68,985 | 0.5189 | 0.5619 |  |
| [0.55, 0.60) | 52,977 | 0.5750 | 0.6780 |  |
| [0.60, 0.65) | 50,914 | 0.6248 | 0.7721 |  |
| [0.65, 0.70) | 48,189 | 0.6747 | 0.8392 |  |
| [0.70, 0.75) | 45,035 | 0.7247 | 0.8905 |  |
| [0.75, 0.80) | 42,303 | 0.7747 | 0.9279 |  |
| [0.80, 0.85) | 39,591 | 0.8248 | 0.9536 |  |
| [0.85, 0.90) | 39,382 | 0.8751 | 0.9720 |  |
| [0.90, 0.95) | 42,102 | 0.9257 | 0.9848 |  |
| [0.95, 1.00] | 99,810 | 0.9857 | 0.9959 |  |

Measurement 4 - Brier score (label outcome_1s)
| tau | observations | brier p_twap | brier p_naive | naive minus twap |
|---|---|---|---|---|
| 240 | 210,234 | 0.1700 | 0.1812 | 0.0111 |
| 180 | 210,234 | 0.1073 | 0.1292 | 0.0219 |
| 120 | 210,234 | 0.0571 | 0.0937 | 0.0366 |
| 90 | 210,234 | 0.0357 | 0.0847 | 0.0490 |
| 60 | 210,234 | 0.0204 | 0.0838 | 0.0634 |
| all | 1,051,170 | 0.0781 | 0.1145 | 0.0364 |

Measurement 5 - realised frequency inside the inversion cells (label outcome_1s)
| cell | observations | mean p_twap | mean p_naive | realised frequency | |realised - mean p_twap| |
|---|---|---|---|---|---|
| p_naive high / p_twap low | 1,518 | 0.1955 | 0.9124 | 0.2319 | 0.0364 |
| p_naive low / p_twap high | 1,568 | 0.7934 | 0.0885 | 0.7691 | 0.0243 |
| both cells | 3,086 | 0.4993 | 0.4938 | 0.5049 | 0.0056 |

### Measurements 1 to 5 under sigma_live

#### All 24 months
Measurement 1 - disagreement rate (|p_twap - p_naive| >= 0.15)
| tau | observations | disagreements | share | mean gap | 99th pct gap |
|---|---|---|---|---|---|
| 240 | 210,234 | 43,369 | 20.629% | 0.1009 | 0.1806 |
| 180 | 210,234 | 79,364 | 37.750% | 0.1208 | 0.2933 |
| 120 | 210,234 | 78,017 | 37.110% | 0.1319 | 0.5041 |
| 90 | 210,234 | 72,223 | 34.354% | 0.1374 | 0.6738 |
| 60 | 210,234 | 64,135 | 30.506% | 0.1415 | 0.8572 |
| all | 1,051,170 | 337,108 | 32.070% | 0.1265 | 0.6699 |

Measurement 2 - inversion rate
| tau | observations | p_naive>=0.85 & p_twap<=0.60 | share | p_naive<=0.15 & p_twap>=0.40 | share | either | share |
|---|---|---|---|---|---|---|---|
| 240 | 210,234 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 180 | 210,234 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 120 | 210,234 | 72 | 0.034% | 65 | 0.031% | 137 | 0.065% |
| 90 | 210,234 | 606 | 0.288% | 637 | 0.303% | 1,243 | 0.591% |
| 60 | 210,234 | 2,119 | 1.008% | 2,206 | 1.049% | 4,325 | 2.057% |
| all | 1,051,170 | 2,797 | 0.266% | 2,908 | 0.277% | 5,705 | 0.543% |

Measurement 3 - calibration of p_twap (label outcome_1s)
| predicted bucket | observations | mean predicted | realised frequency | note |
|---|---|---|---|---|
| [0.00, 0.05) | 342,935 | 0.0044 | 0.0180 |  |
| [0.05, 0.10) | 32,748 | 0.0735 | 0.1276 |  |
| [0.10, 0.15) | 24,429 | 0.1240 | 0.1728 |  |
| [0.15, 0.20) | 20,662 | 0.1744 | 0.2224 |  |
| [0.20, 0.25) | 18,623 | 0.2247 | 0.2610 |  |
| [0.25, 0.30) | 17,395 | 0.2749 | 0.3076 |  |
| [0.30, 0.35) | 16,622 | 0.3248 | 0.3457 |  |
| [0.35, 0.40) | 15,497 | 0.3749 | 0.3827 |  |
| [0.40, 0.45) | 14,986 | 0.4248 | 0.4162 |  |
| [0.45, 0.50) | 24,277 | 0.4839 | 0.4490 |  |
| [0.50, 0.55) | 23,292 | 0.5163 | 0.5531 |  |
| [0.55, 0.60) | 15,168 | 0.5751 | 0.5687 |  |
| [0.60, 0.65) | 15,515 | 0.6252 | 0.6169 |  |
| [0.65, 0.70) | 16,427 | 0.6752 | 0.6580 |  |
| [0.70, 0.75) | 17,138 | 0.7254 | 0.7011 |  |
| [0.75, 0.80) | 18,537 | 0.7755 | 0.7419 |  |
| [0.80, 0.85) | 20,522 | 0.8256 | 0.7815 |  |
| [0.85, 0.90) | 24,277 | 0.8758 | 0.8206 |  |
| [0.90, 0.95) | 32,376 | 0.9268 | 0.8673 |  |
| [0.95, 1.00] | 339,744 | 0.9956 | 0.9814 |  |

Measurement 3 - calibration of p_naive (label outcome_1s)
| predicted bucket | observations | mean predicted | realised frequency | note |
|---|---|---|---|---|
| [0.00, 0.05) | 151,161 | 0.0127 | 0.0067 |  |
| [0.05, 0.10) | 49,770 | 0.0741 | 0.0307 |  |
| [0.10, 0.15) | 42,767 | 0.1246 | 0.0561 |  |
| [0.15, 0.20) | 40,071 | 0.1749 | 0.0861 |  |
| [0.20, 0.25) | 39,542 | 0.2249 | 0.1195 |  |
| [0.25, 0.30) | 39,263 | 0.2750 | 0.1692 |  |
| [0.30, 0.35) | 38,707 | 0.3250 | 0.2281 |  |
| [0.35, 0.40) | 38,833 | 0.3750 | 0.2909 |  |
| [0.40, 0.45) | 38,748 | 0.4249 | 0.3596 |  |
| [0.45, 0.50) | 43,020 | 0.4782 | 0.4375 |  |
| [0.50, 0.55) | 53,949 | 0.5173 | 0.5463 |  |
| [0.55, 0.60) | 38,182 | 0.5751 | 0.6320 |  |
| [0.60, 0.65) | 38,977 | 0.6251 | 0.7072 |  |
| [0.65, 0.70) | 38,704 | 0.6750 | 0.7723 |  |
| [0.70, 0.75) | 38,605 | 0.7249 | 0.8303 |  |
| [0.75, 0.80) | 38,951 | 0.7750 | 0.8748 |  |
| [0.80, 0.85) | 40,251 | 0.8251 | 0.9129 |  |
| [0.85, 0.90) | 42,332 | 0.8754 | 0.9449 |  |
| [0.90, 0.95) | 49,107 | 0.9259 | 0.9680 |  |
| [0.95, 1.00] | 150,230 | 0.9874 | 0.9932 |  |

Measurement 4 - Brier score (label outcome_1s)
| tau | observations | brier p_twap | brier p_naive | naive minus twap |
|---|---|---|---|---|
| 240 | 210,234 | 0.1722 | 0.1740 | 0.0018 |
| 180 | 210,234 | 0.1081 | 0.1178 | 0.0097 |
| 120 | 210,234 | 0.0571 | 0.0820 | 0.0249 |
| 90 | 210,234 | 0.0352 | 0.0755 | 0.0403 |
| 60 | 210,234 | 0.0200 | 0.0793 | 0.0593 |
| all | 1,051,170 | 0.0785 | 0.1057 | 0.0272 |

Measurement 5 - realised frequency inside the inversion cells (label outcome_1s)
| cell | observations | mean p_twap | mean p_naive | realised frequency | |realised - mean p_twap| |
|---|---|---|---|---|---|
| p_naive high / p_twap low | 2,797 | 0.1875 | 0.9153 | 0.2327 | 0.0453 |
| p_naive low / p_twap high | 2,908 | 0.8090 | 0.0867 | 0.7792 | 0.0298 |
| both cells | 5,705 | 0.5043 | 0.4929 | 0.5113 | 0.0070 |

### Measurement 6 - stability


### sigma_pre

#### first 12 months (2024-09 to 2025-08)
Measurement 1 - disagreement rate (|p_twap - p_naive| >= 0.15)
| tau | observations | disagreements | share | mean gap | 99th pct gap |
|---|---|---|---|---|---|
| 240 | 105,114 | 18,508 | 17.608% | 0.0953 | 0.1758 |
| 180 | 105,114 | 45,200 | 43.001% | 0.1286 | 0.2736 |
| 120 | 105,114 | 48,317 | 45.966% | 0.1496 | 0.4568 |
| 90 | 105,114 | 45,415 | 43.205% | 0.1570 | 0.6049 |
| 60 | 105,114 | 40,084 | 38.134% | 0.1607 | 0.7909 |
| all | 525,570 | 197,524 | 37.583% | 0.1383 | 0.6108 |

Measurement 2 - inversion rate
| tau | observations | p_naive>=0.85 & p_twap<=0.60 | share | p_naive<=0.15 & p_twap>=0.40 | share | either | share |
|---|---|---|---|---|---|---|---|
| 240 | 105,114 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 180 | 105,114 | 1 | 0.001% | 0 | 0.000% | 1 | 0.001% |
| 120 | 105,114 | 25 | 0.024% | 21 | 0.020% | 46 | 0.044% |
| 90 | 105,114 | 149 | 0.142% | 145 | 0.138% | 294 | 0.280% |
| 60 | 105,114 | 645 | 0.614% | 606 | 0.577% | 1,251 | 1.190% |
| all | 525,570 | 820 | 0.156% | 772 | 0.147% | 1,592 | 0.303% |

Measurement 3 - calibration of p_twap (label outcome_1s)
| predicted bucket | observations | mean predicted | realised frequency | note |
|---|---|---|---|---|
| [0.00, 0.05) | 150,337 | 0.0052 | 0.0094 |  |
| [0.05, 0.10) | 18,029 | 0.0736 | 0.0779 |  |
| [0.10, 0.15) | 14,069 | 0.1244 | 0.1194 |  |
| [0.15, 0.20) | 12,505 | 0.1745 | 0.1579 |  |
| [0.20, 0.25) | 11,634 | 0.2250 | 0.2116 |  |
| [0.25, 0.30) | 11,144 | 0.2748 | 0.2476 |  |
| [0.30, 0.35) | 10,727 | 0.3246 | 0.2994 |  |
| [0.35, 0.40) | 10,781 | 0.3751 | 0.3471 |  |
| [0.40, 0.45) | 10,293 | 0.4250 | 0.4044 |  |
| [0.45, 0.50) | 13,877 | 0.4817 | 0.4499 |  |
| [0.50, 0.55) | 13,830 | 0.5181 | 0.5474 |  |
| [0.55, 0.60) | 10,273 | 0.5749 | 0.5927 |  |
| [0.60, 0.65) | 10,573 | 0.6249 | 0.6557 |  |
| [0.65, 0.70) | 10,776 | 0.6750 | 0.7081 |  |
| [0.70, 0.75) | 11,350 | 0.7253 | 0.7474 |  |
| [0.75, 0.80) | 11,666 | 0.7752 | 0.7918 |  |
| [0.80, 0.85) | 12,548 | 0.8255 | 0.8361 |  |
| [0.85, 0.90) | 13,957 | 0.8759 | 0.8804 |  |
| [0.90, 0.95) | 17,863 | 0.9262 | 0.9199 |  |
| [0.95, 1.00] | 149,338 | 0.9948 | 0.9907 |  |

Measurement 3 - calibration of p_naive (label outcome_1s)
| predicted bucket | observations | mean predicted | realised frequency | note |
|---|---|---|---|---|
| [0.00, 0.05) | 50,998 | 0.0146 | 0.0038 |  |
| [0.05, 0.10) | 21,990 | 0.0744 | 0.0156 |  |
| [0.10, 0.15) | 20,467 | 0.1249 | 0.0288 |  |
| [0.15, 0.20) | 20,591 | 0.1752 | 0.0479 |  |
| [0.20, 0.25) | 21,431 | 0.2251 | 0.0748 |  |
| [0.25, 0.30) | 22,831 | 0.2753 | 0.1124 |  |
| [0.30, 0.35) | 23,609 | 0.3252 | 0.1697 |  |
| [0.35, 0.40) | 25,227 | 0.3752 | 0.2388 |  |
| [0.40, 0.45) | 25,912 | 0.4251 | 0.3215 |  |
| [0.45, 0.50) | 27,852 | 0.4771 | 0.4247 |  |
| [0.50, 0.55) | 32,234 | 0.5195 | 0.5565 |  |
| [0.55, 0.60) | 25,723 | 0.5751 | 0.6720 |  |
| [0.60, 0.65) | 25,064 | 0.6248 | 0.7648 |  |
| [0.65, 0.70) | 23,991 | 0.6748 | 0.8333 |  |
| [0.70, 0.75) | 22,765 | 0.7248 | 0.8851 |  |
| [0.75, 0.80) | 21,462 | 0.7747 | 0.9244 |  |
| [0.80, 0.85) | 20,231 | 0.8247 | 0.9519 |  |
| [0.85, 0.90) | 20,146 | 0.8751 | 0.9703 |  |
| [0.90, 0.95) | 21,667 | 0.9258 | 0.9845 |  |
| [0.95, 1.00] | 51,379 | 0.9856 | 0.9960 |  |

Measurement 4 - Brier score (label outcome_1s)
| tau | observations | brier p_twap | brier p_naive | naive minus twap |
|---|---|---|---|---|
| 240 | 105,114 | 0.1713 | 0.1814 | 0.0101 |
| 180 | 105,114 | 0.1071 | 0.1279 | 0.0208 |
| 120 | 105,114 | 0.0564 | 0.0915 | 0.0352 |
| 90 | 105,114 | 0.0350 | 0.0828 | 0.0478 |
| 60 | 105,114 | 0.0199 | 0.0827 | 0.0628 |
| all | 525,570 | 0.0779 | 0.1133 | 0.0354 |

Measurement 5 - realised frequency inside the inversion cells (label outcome_1s)
| cell | observations | mean p_twap | mean p_naive | realised frequency | |realised - mean p_twap| |
|---|---|---|---|---|---|
| p_naive high / p_twap low | 820 | 0.1988 | 0.9115 | 0.2439 | 0.0451 |
| p_naive low / p_twap high | 772 | 0.7891 | 0.0898 | 0.7500 | 0.0391 |
| both cells | 1,592 | 0.4850 | 0.5130 | 0.4893 | 0.0043 |
#### last 12 months (2025-09 to 2026-08)
Measurement 1 - disagreement rate (|p_twap - p_naive| >= 0.15)
| tau | observations | disagreements | share | mean gap | 99th pct gap |
|---|---|---|---|---|---|
| 240 | 105,120 | 18,129 | 17.246% | 0.0925 | 0.1765 |
| 180 | 105,120 | 44,681 | 42.505% | 0.1269 | 0.2746 |
| 120 | 105,120 | 49,772 | 47.348% | 0.1515 | 0.4570 |
| 90 | 105,120 | 46,929 | 44.643% | 0.1597 | 0.6033 |
| 60 | 105,120 | 41,934 | 39.892% | 0.1639 | 0.7832 |
| all | 525,600 | 201,445 | 38.327% | 0.1389 | 0.5980 |

Measurement 2 - inversion rate
| tau | observations | p_naive>=0.85 & p_twap<=0.60 | share | p_naive<=0.15 & p_twap>=0.40 | share | either | share |
|---|---|---|---|---|---|---|---|
| 240 | 105,120 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 180 | 105,120 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 120 | 105,120 | 14 | 0.013% | 25 | 0.024% | 39 | 0.037% |
| 90 | 105,120 | 136 | 0.129% | 154 | 0.146% | 290 | 0.276% |
| 60 | 105,120 | 548 | 0.521% | 617 | 0.587% | 1,165 | 1.108% |
| all | 525,600 | 698 | 0.133% | 796 | 0.151% | 1,494 | 0.284% |

Measurement 3 - calibration of p_twap (label outcome_1s)
| predicted bucket | observations | mean predicted | realised frequency | note |
|---|---|---|---|---|
| [0.00, 0.05) | 147,460 | 0.0053 | 0.0083 |  |
| [0.05, 0.10) | 17,630 | 0.0737 | 0.0685 |  |
| [0.10, 0.15) | 14,095 | 0.1245 | 0.1095 |  |
| [0.15, 0.20) | 12,695 | 0.1747 | 0.1423 |  |
| [0.20, 0.25) | 11,798 | 0.2248 | 0.1845 |  |
| [0.25, 0.30) | 11,430 | 0.2747 | 0.2421 |  |
| [0.30, 0.35) | 11,314 | 0.3249 | 0.2879 |  |
| [0.35, 0.40) | 10,971 | 0.3751 | 0.3424 |  |
| [0.40, 0.45) | 10,598 | 0.4251 | 0.4010 |  |
| [0.45, 0.50) | 16,787 | 0.4841 | 0.4265 |  |
| [0.50, 0.55) | 15,902 | 0.5170 | 0.5691 |  |
| [0.55, 0.60) | 10,523 | 0.5749 | 0.6066 |  |
| [0.60, 0.65) | 11,124 | 0.6253 | 0.6535 |  |
| [0.65, 0.70) | 11,010 | 0.6753 | 0.7154 |  |
| [0.70, 0.75) | 11,376 | 0.7253 | 0.7661 |  |
| [0.75, 0.80) | 11,709 | 0.7752 | 0.8090 |  |
| [0.80, 0.85) | 12,517 | 0.8256 | 0.8523 |  |
| [0.85, 0.90) | 13,928 | 0.8756 | 0.8861 |  |
| [0.90, 0.95) | 17,586 | 0.9263 | 0.9306 |  |
| [0.95, 1.00] | 145,147 | 0.9947 | 0.9913 |  |

Measurement 3 - calibration of p_naive (label outcome_1s)
| predicted bucket | observations | mean predicted | realised frequency | note |
|---|---|---|---|---|
| [0.00, 0.05) | 49,294 | 0.0143 | 0.0047 |  |
| [0.05, 0.10) | 20,863 | 0.0744 | 0.0164 |  |
| [0.10, 0.15) | 19,538 | 0.1251 | 0.0263 |  |
| [0.15, 0.20) | 20,006 | 0.1751 | 0.0449 |  |
| [0.20, 0.25) | 20,847 | 0.2252 | 0.0634 |  |
| [0.25, 0.30) | 22,597 | 0.2756 | 0.1008 |  |
| [0.30, 0.35) | 24,276 | 0.3254 | 0.1525 |  |
| [0.35, 0.40) | 25,945 | 0.3752 | 0.2226 |  |
| [0.40, 0.45) | 27,083 | 0.4251 | 0.3118 |  |
| [0.45, 0.50) | 30,525 | 0.4779 | 0.4149 |  |
| [0.50, 0.55) | 36,751 | 0.5183 | 0.5666 |  |
| [0.55, 0.60) | 27,254 | 0.5749 | 0.6837 |  |
| [0.60, 0.65) | 25,850 | 0.6247 | 0.7791 |  |
| [0.65, 0.70) | 24,198 | 0.6746 | 0.8451 |  |
| [0.70, 0.75) | 22,270 | 0.7245 | 0.8960 |  |
| [0.75, 0.80) | 20,841 | 0.7747 | 0.9316 |  |
| [0.80, 0.85) | 19,360 | 0.8249 | 0.9554 |  |
| [0.85, 0.90) | 19,236 | 0.8750 | 0.9737 |  |
| [0.90, 0.95) | 20,435 | 0.9256 | 0.9852 |  |
| [0.95, 1.00] | 48,431 | 0.9859 | 0.9958 |  |

Measurement 4 - Brier score (label outcome_1s)
| tau | observations | brier p_twap | brier p_naive | naive minus twap |
|---|---|---|---|---|
| 240 | 105,120 | 0.1687 | 0.1809 | 0.0122 |
| 180 | 105,120 | 0.1076 | 0.1306 | 0.0230 |
| 120 | 105,120 | 0.0579 | 0.0959 | 0.0380 |
| 90 | 105,120 | 0.0365 | 0.0866 | 0.0501 |
| 60 | 105,120 | 0.0210 | 0.0849 | 0.0639 |
| all | 525,600 | 0.0783 | 0.1158 | 0.0374 |

Measurement 5 - realised frequency inside the inversion cells (label outcome_1s)
| cell | observations | mean p_twap | mean p_naive | realised frequency | |realised - mean p_twap| |
|---|---|---|---|---|---|
| p_naive high / p_twap low | 698 | 0.1916 | 0.9134 | 0.2178 | 0.0262 |
| p_naive low / p_twap high | 796 | 0.7975 | 0.0874 | 0.7877 | 0.0099 |
| both cells | 1,494 | 0.5144 | 0.4733 | 0.5214 | 0.0070 |

### sigma_live

#### first 12 months (2024-09 to 2025-08)
Measurement 1 - disagreement rate (|p_twap - p_naive| >= 0.15)
| tau | observations | disagreements | share | mean gap | 99th pct gap |
|---|---|---|---|---|---|
| 240 | 105,114 | 21,572 | 20.522% | 0.1018 | 0.1803 |
| 180 | 105,114 | 38,923 | 37.029% | 0.1199 | 0.2966 |
| 120 | 105,114 | 37,689 | 35.855% | 0.1293 | 0.5131 |
| 90 | 105,114 | 35,015 | 33.311% | 0.1349 | 0.6806 |
| 60 | 105,114 | 31,087 | 29.575% | 0.1398 | 0.8679 |
| all | 525,570 | 164,286 | 31.259% | 0.1251 | 0.6825 |

Measurement 2 - inversion rate
| tau | observations | p_naive>=0.85 & p_twap<=0.60 | share | p_naive<=0.15 & p_twap>=0.40 | share | either | share |
|---|---|---|---|---|---|---|---|
| 240 | 105,114 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 180 | 105,114 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 120 | 105,114 | 50 | 0.048% | 33 | 0.031% | 83 | 0.079% |
| 90 | 105,114 | 351 | 0.334% | 339 | 0.323% | 690 | 0.656% |
| 60 | 105,114 | 1,176 | 1.119% | 1,197 | 1.139% | 2,373 | 2.258% |
| all | 525,570 | 1,577 | 0.300% | 1,569 | 0.299% | 3,146 | 0.599% |

Measurement 3 - calibration of p_twap (label outcome_1s)
| predicted bucket | observations | mean predicted | realised frequency | note |
|---|---|---|---|---|
| [0.00, 0.05) | 174,030 | 0.0044 | 0.0195 |  |
| [0.05, 0.10) | 16,275 | 0.0736 | 0.1371 |  |
| [0.10, 0.15) | 11,930 | 0.1239 | 0.1878 |  |
| [0.15, 0.20) | 10,199 | 0.1744 | 0.2341 |  |
| [0.20, 0.25) | 8,984 | 0.2247 | 0.2688 |  |
| [0.25, 0.30) | 8,479 | 0.2748 | 0.3161 |  |
| [0.30, 0.35) | 7,993 | 0.3249 | 0.3514 |  |
| [0.35, 0.40) | 7,496 | 0.3749 | 0.3881 |  |
| [0.40, 0.45) | 7,200 | 0.4249 | 0.4185 |  |
| [0.45, 0.50) | 10,810 | 0.4829 | 0.4601 |  |
| [0.50, 0.55) | 10,724 | 0.5168 | 0.5424 |  |
| [0.55, 0.60) | 7,255 | 0.5749 | 0.5664 |  |
| [0.60, 0.65) | 7,449 | 0.6253 | 0.6069 |  |
| [0.65, 0.70) | 7,944 | 0.6753 | 0.6523 |  |
| [0.70, 0.75) | 8,396 | 0.7252 | 0.6953 |  |
| [0.75, 0.80) | 8,974 | 0.7754 | 0.7360 |  |
| [0.80, 0.85) | 10,137 | 0.8255 | 0.7702 |  |
| [0.85, 0.90) | 12,091 | 0.8758 | 0.8035 |  |
| [0.90, 0.95) | 16,155 | 0.9268 | 0.8600 |  |
| [0.95, 1.00] | 173,049 | 0.9956 | 0.9802 |  |

Measurement 3 - calibration of p_naive (label outcome_1s)
| predicted bucket | observations | mean predicted | realised frequency | note |
|---|---|---|---|---|
| [0.00, 0.05) | 78,925 | 0.0125 | 0.0073 |  |
| [0.05, 0.10) | 25,279 | 0.0741 | 0.0335 |  |
| [0.10, 0.15) | 21,388 | 0.1246 | 0.0612 |  |
| [0.15, 0.20) | 20,048 | 0.1748 | 0.0916 |  |
| [0.20, 0.25) | 19,565 | 0.2248 | 0.1297 |  |
| [0.25, 0.30) | 19,283 | 0.2750 | 0.1805 |  |
| [0.30, 0.35) | 18,882 | 0.3249 | 0.2426 |  |
| [0.35, 0.40) | 18,753 | 0.3751 | 0.2998 |  |
| [0.40, 0.45) | 18,617 | 0.4249 | 0.3628 |  |
| [0.45, 0.50) | 20,168 | 0.4778 | 0.4426 |  |
| [0.50, 0.55) | 24,709 | 0.5179 | 0.5417 |  |
| [0.55, 0.60) | 18,148 | 0.5751 | 0.6220 |  |
| [0.60, 0.65) | 18,724 | 0.6252 | 0.6980 |  |
| [0.65, 0.70) | 18,970 | 0.6751 | 0.7630 |  |
| [0.70, 0.75) | 19,156 | 0.7250 | 0.8181 |  |
| [0.75, 0.80) | 19,403 | 0.7752 | 0.8673 |  |
| [0.80, 0.85) | 20,159 | 0.8250 | 0.9083 |  |
| [0.85, 0.90) | 21,355 | 0.8754 | 0.9402 |  |
| [0.90, 0.95) | 25,097 | 0.9260 | 0.9643 |  |
| [0.95, 1.00] | 78,941 | 0.9878 | 0.9929 |  |

Measurement 4 - Brier score (label outcome_1s)
| tau | observations | brier p_twap | brier p_naive | naive minus twap |
|---|---|---|---|---|
| 240 | 105,114 | 0.1745 | 0.1743 | -0.0002 |
| 180 | 105,114 | 0.1085 | 0.1163 | 0.0078 |
| 120 | 105,114 | 0.0567 | 0.0798 | 0.0231 |
| 90 | 105,114 | 0.0346 | 0.0736 | 0.0390 |
| 60 | 105,114 | 0.0196 | 0.0789 | 0.0592 |
| all | 525,570 | 0.0788 | 0.1046 | 0.0258 |

Measurement 5 - realised frequency inside the inversion cells (label outcome_1s)
| cell | observations | mean p_twap | mean p_naive | realised frequency | |realised - mean p_twap| |
|---|---|---|---|---|---|
| p_naive high / p_twap low | 1,577 | 0.1914 | 0.9161 | 0.2498 | 0.0584 |
| p_naive low / p_twap high | 1,569 | 0.8122 | 0.0874 | 0.7699 | 0.0422 |
| both cells | 3,146 | 0.5010 | 0.5028 | 0.5092 | 0.0082 |
#### last 12 months (2025-09 to 2026-08)
Measurement 1 - disagreement rate (|p_twap - p_naive| >= 0.15)
| tau | observations | disagreements | share | mean gap | 99th pct gap |
|---|---|---|---|---|---|
| 240 | 105,120 | 21,797 | 20.735% | 0.1000 | 0.1809 |
| 180 | 105,120 | 40,441 | 38.471% | 0.1218 | 0.2908 |
| 120 | 105,120 | 40,328 | 38.364% | 0.1345 | 0.4947 |
| 90 | 105,120 | 37,208 | 35.396% | 0.1398 | 0.6664 |
| 60 | 105,120 | 33,048 | 31.438% | 0.1433 | 0.8482 |
| all | 525,600 | 172,822 | 32.881% | 0.1279 | 0.6570 |

Measurement 2 - inversion rate
| tau | observations | p_naive>=0.85 & p_twap<=0.60 | share | p_naive<=0.15 & p_twap>=0.40 | share | either | share |
|---|---|---|---|---|---|---|---|
| 240 | 105,120 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 180 | 105,120 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 120 | 105,120 | 22 | 0.021% | 32 | 0.030% | 54 | 0.051% |
| 90 | 105,120 | 255 | 0.243% | 298 | 0.283% | 553 | 0.526% |
| 60 | 105,120 | 943 | 0.897% | 1,009 | 0.960% | 1,952 | 1.857% |
| all | 525,600 | 1,220 | 0.232% | 1,339 | 0.255% | 2,559 | 0.487% |

Measurement 3 - calibration of p_twap (label outcome_1s)
| predicted bucket | observations | mean predicted | realised frequency | note |
|---|---|---|---|---|
| [0.00, 0.05) | 168,905 | 0.0045 | 0.0165 |  |
| [0.05, 0.10) | 16,473 | 0.0734 | 0.1183 |  |
| [0.10, 0.15) | 12,499 | 0.1241 | 0.1585 |  |
| [0.15, 0.20) | 10,463 | 0.1744 | 0.2110 |  |
| [0.20, 0.25) | 9,639 | 0.2247 | 0.2537 |  |
| [0.25, 0.30) | 8,916 | 0.2749 | 0.2996 |  |
| [0.30, 0.35) | 8,629 | 0.3248 | 0.3404 |  |
| [0.35, 0.40) | 8,001 | 0.3750 | 0.3777 |  |
| [0.40, 0.45) | 7,786 | 0.4248 | 0.4141 |  |
| [0.45, 0.50) | 13,467 | 0.4847 | 0.4401 |  |
| [0.50, 0.55) | 12,568 | 0.5159 | 0.5621 |  |
| [0.55, 0.60) | 7,913 | 0.5752 | 0.5708 |  |
| [0.60, 0.65) | 8,066 | 0.6251 | 0.6261 |  |
| [0.65, 0.70) | 8,483 | 0.6751 | 0.6633 |  |
| [0.70, 0.75) | 8,742 | 0.7255 | 0.7067 |  |
| [0.75, 0.80) | 9,563 | 0.7756 | 0.7474 |  |
| [0.80, 0.85) | 10,385 | 0.8257 | 0.7924 |  |
| [0.85, 0.90) | 12,186 | 0.8758 | 0.8375 |  |
| [0.90, 0.95) | 16,221 | 0.9267 | 0.8746 |  |
| [0.95, 1.00] | 166,695 | 0.9955 | 0.9827 |  |

Measurement 3 - calibration of p_naive (label outcome_1s)
| predicted bucket | observations | mean predicted | realised frequency | note |
|---|---|---|---|---|
| [0.00, 0.05) | 72,236 | 0.0129 | 0.0061 |  |
| [0.05, 0.10) | 24,491 | 0.0741 | 0.0278 |  |
| [0.10, 0.15) | 21,379 | 0.1246 | 0.0510 |  |
| [0.15, 0.20) | 20,023 | 0.1749 | 0.0805 |  |
| [0.20, 0.25) | 19,977 | 0.2250 | 0.1096 |  |
| [0.25, 0.30) | 19,980 | 0.2751 | 0.1583 |  |
| [0.30, 0.35) | 19,825 | 0.3251 | 0.2143 |  |
| [0.35, 0.40) | 20,080 | 0.3749 | 0.2825 |  |
| [0.40, 0.45) | 20,131 | 0.4249 | 0.3566 |  |
| [0.45, 0.50) | 22,852 | 0.4785 | 0.4331 |  |
| [0.50, 0.55) | 29,240 | 0.5169 | 0.5502 |  |
| [0.55, 0.60) | 20,034 | 0.5752 | 0.6410 |  |
| [0.60, 0.65) | 20,253 | 0.6249 | 0.7157 |  |
| [0.65, 0.70) | 19,734 | 0.6749 | 0.7811 |  |
| [0.70, 0.75) | 19,449 | 0.7248 | 0.8423 |  |
| [0.75, 0.80) | 19,548 | 0.7749 | 0.8822 |  |
| [0.80, 0.85) | 20,092 | 0.8251 | 0.9175 |  |
| [0.85, 0.90) | 20,977 | 0.8754 | 0.9498 |  |
| [0.90, 0.95) | 24,010 | 0.9257 | 0.9720 |  |
| [0.95, 1.00] | 71,289 | 0.9870 | 0.9937 |  |

Measurement 4 - Brier score (label outcome_1s)
| tau | observations | brier p_twap | brier p_naive | naive minus twap |
|---|---|---|---|---|
| 240 | 105,120 | 0.1700 | 0.1737 | 0.0037 |
| 180 | 105,120 | 0.1077 | 0.1193 | 0.0116 |
| 120 | 105,120 | 0.0575 | 0.0842 | 0.0267 |
| 90 | 105,120 | 0.0357 | 0.0773 | 0.0416 |
| 60 | 105,120 | 0.0204 | 0.0798 | 0.0594 |
| all | 525,600 | 0.0782 | 0.1069 | 0.0286 |

Measurement 5 - realised frequency inside the inversion cells (label outcome_1s)
| cell | observations | mean p_twap | mean p_naive | realised frequency | |realised - mean p_twap| |
|---|---|---|---|---|---|
| p_naive high / p_twap low | 1,220 | 0.1824 | 0.9143 | 0.2107 | 0.0283 |
| p_naive low / p_twap high | 1,339 | 0.8053 | 0.0859 | 0.7901 | 0.0152 |
| both cells | 2,559 | 0.5083 | 0.4808 | 0.5139 | 0.0055 |

### Measurement 7 - volatility regime split (terciles of sigma_pre)

Tercile edges of `sigma_pre` in dollars per sqrt(second): 3.764808 and 6.236466.

### sigma_pre

#### low tercile (sigma_pre < 3.764808)
Measurement 1 - disagreement rate (|p_twap - p_naive| >= 0.15)
| tau | observations | disagreements | share | mean gap | 99th pct gap |
|---|---|---|---|---|---|
| 240 | 70,078 | 11,786 | 16.818% | 0.0877 | 0.1767 |
| 180 | 70,078 | 27,563 | 39.332% | 0.1200 | 0.2770 |
| 120 | 70,078 | 30,189 | 43.079% | 0.1413 | 0.4727 |
| 90 | 70,078 | 28,600 | 40.812% | 0.1486 | 0.6217 |
| 60 | 70,078 | 25,549 | 36.458% | 0.1529 | 0.8048 |
| all | 350,390 | 123,687 | 35.300% | 0.1301 | 0.6103 |

Measurement 2 - inversion rate
| tau | observations | p_naive>=0.85 & p_twap<=0.60 | share | p_naive<=0.15 & p_twap>=0.40 | share | either | share |
|---|---|---|---|---|---|---|---|
| 240 | 70,078 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 180 | 70,078 | 1 | 0.001% | 0 | 0.000% | 1 | 0.001% |
| 120 | 70,078 | 18 | 0.026% | 25 | 0.036% | 43 | 0.061% |
| 90 | 70,078 | 127 | 0.181% | 131 | 0.187% | 258 | 0.368% |
| 60 | 70,078 | 446 | 0.636% | 469 | 0.669% | 915 | 1.306% |
| all | 350,390 | 592 | 0.169% | 625 | 0.178% | 1,217 | 0.347% |

Measurement 4 - Brier score (label outcome_1s)
| tau | observations | brier p_twap | brier p_naive | naive minus twap |
|---|---|---|---|---|
| 240 | 70,078 | 0.1710 | 0.1805 | 0.0095 |
| 180 | 70,078 | 0.1098 | 0.1289 | 0.0191 |
| 120 | 70,078 | 0.0587 | 0.0921 | 0.0334 |
| 90 | 70,078 | 0.0379 | 0.0830 | 0.0451 |
| 60 | 70,078 | 0.0224 | 0.0823 | 0.0598 |
| all | 350,390 | 0.0800 | 0.1134 | 0.0334 |

Measurement 5 - realised frequency inside the inversion cells (label outcome_1s)
| cell | observations | mean p_twap | mean p_naive | realised frequency | |realised - mean p_twap| |
|---|---|---|---|---|---|
| p_naive high / p_twap low | 592 | 0.1780 | 0.9187 | 0.2601 | 0.0821 |
| p_naive low / p_twap high | 625 | 0.8048 | 0.0846 | 0.7664 | 0.0384 |
| both cells | 1,217 | 0.4999 | 0.4903 | 0.5201 | 0.0202 |
#### mid tercile (3.764808 <= sigma_pre < 6.236466)
Measurement 1 - disagreement rate (|p_twap - p_naive| >= 0.15)
| tau | observations | disagreements | share | mean gap | 99th pct gap |
|---|---|---|---|---|---|
| 240 | 70,078 | 12,526 | 17.874% | 0.0968 | 0.1761 |
| 180 | 70,078 | 30,524 | 43.557% | 0.1302 | 0.2749 |
| 120 | 70,078 | 33,196 | 47.370% | 0.1529 | 0.4562 |
| 90 | 70,078 | 31,153 | 44.455% | 0.1608 | 0.6031 |
| 60 | 70,078 | 27,679 | 39.497% | 0.1650 | 0.7885 |
| all | 350,390 | 135,078 | 38.551% | 0.1411 | 0.6105 |

Measurement 2 - inversion rate
| tau | observations | p_naive>=0.85 & p_twap<=0.60 | share | p_naive<=0.15 & p_twap>=0.40 | share | either | share |
|---|---|---|---|---|---|---|---|
| 240 | 70,078 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 180 | 70,078 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 120 | 70,078 | 15 | 0.021% | 9 | 0.013% | 24 | 0.034% |
| 90 | 70,078 | 89 | 0.127% | 100 | 0.143% | 189 | 0.270% |
| 60 | 70,078 | 418 | 0.596% | 398 | 0.568% | 816 | 1.164% |
| all | 350,390 | 522 | 0.149% | 507 | 0.145% | 1,029 | 0.294% |

Measurement 4 - Brier score (label outcome_1s)
| tau | observations | brier p_twap | brier p_naive | naive minus twap |
|---|---|---|---|---|
| 240 | 70,078 | 0.1692 | 0.1804 | 0.0112 |
| 180 | 70,078 | 0.1065 | 0.1283 | 0.0218 |
| 120 | 70,078 | 0.0568 | 0.0936 | 0.0368 |
| 90 | 70,078 | 0.0350 | 0.0846 | 0.0495 |
| 60 | 70,078 | 0.0197 | 0.0840 | 0.0643 |
| all | 350,390 | 0.0775 | 0.1142 | 0.0367 |

Measurement 5 - realised frequency inside the inversion cells (label outcome_1s)
| cell | observations | mean p_twap | mean p_naive | realised frequency | |realised - mean p_twap| |
|---|---|---|---|---|---|
| p_naive high / p_twap low | 522 | 0.2081 | 0.9108 | 0.2184 | 0.0103 |
| p_naive low / p_twap high | 507 | 0.7995 | 0.0881 | 0.7692 | 0.0303 |
| both cells | 1,029 | 0.4995 | 0.5054 | 0.4898 | 0.0097 |
#### high tercile (sigma_pre >= 6.236466)
Measurement 1 - disagreement rate (|p_twap - p_naive| >= 0.15)
| tau | observations | disagreements | share | mean gap | 99th pct gap |
|---|---|---|---|---|---|
| 240 | 70,078 | 12,325 | 17.588% | 0.0972 | 0.1755 |
| 180 | 70,078 | 31,794 | 45.369% | 0.1330 | 0.2706 |
| 120 | 70,078 | 34,704 | 49.522% | 0.1575 | 0.4393 |
| 90 | 70,078 | 32,591 | 46.507% | 0.1657 | 0.5918 |
| 60 | 70,078 | 28,790 | 41.083% | 0.1690 | 0.7653 |
| all | 350,390 | 140,204 | 40.014% | 0.1445 | 0.5938 |

Measurement 2 - inversion rate
| tau | observations | p_naive>=0.85 & p_twap<=0.60 | share | p_naive<=0.15 & p_twap>=0.40 | share | either | share |
|---|---|---|---|---|---|---|---|
| 240 | 70,078 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 180 | 70,078 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 120 | 70,078 | 6 | 0.009% | 12 | 0.017% | 18 | 0.026% |
| 90 | 70,078 | 69 | 0.098% | 68 | 0.097% | 137 | 0.195% |
| 60 | 70,078 | 329 | 0.469% | 356 | 0.508% | 685 | 0.977% |
| all | 350,390 | 404 | 0.115% | 436 | 0.124% | 840 | 0.240% |

Measurement 4 - Brier score (label outcome_1s)
| tau | observations | brier p_twap | brier p_naive | naive minus twap |
|---|---|---|---|---|
| 240 | 70,078 | 0.1698 | 0.1826 | 0.0127 |
| 180 | 70,078 | 0.1057 | 0.1305 | 0.0248 |
| 120 | 70,078 | 0.0558 | 0.0954 | 0.0396 |
| 90 | 70,078 | 0.0343 | 0.0865 | 0.0522 |
| 60 | 70,078 | 0.0192 | 0.0851 | 0.0660 |
| all | 350,390 | 0.0770 | 0.1160 | 0.0391 |

Measurement 5 - realised frequency inside the inversion cells (label outcome_1s)
| cell | observations | mean p_twap | mean p_naive | realised frequency | |realised - mean p_twap| |
|---|---|---|---|---|---|
| p_naive high / p_twap low | 404 | 0.2048 | 0.9052 | 0.2079 | 0.0031 |
| p_naive low / p_twap high | 436 | 0.7699 | 0.0948 | 0.7729 | 0.0030 |
| both cells | 840 | 0.4981 | 0.4846 | 0.5012 | 0.0031 |

### sigma_live

#### low tercile (sigma_pre < 3.764808)
Measurement 1 - disagreement rate (|p_twap - p_naive| >= 0.15)
| tau | observations | disagreements | share | mean gap | 99th pct gap |
|---|---|---|---|---|---|
| 240 | 70,078 | 13,178 | 18.805% | 0.0928 | 0.1804 |
| 180 | 70,078 | 23,979 | 34.218% | 0.1121 | 0.2967 |
| 120 | 70,078 | 23,777 | 33.929% | 0.1225 | 0.5123 |
| 90 | 70,078 | 22,224 | 31.713% | 0.1277 | 0.6828 |
| 60 | 70,078 | 19,957 | 28.478% | 0.1326 | 0.8673 |
| all | 350,390 | 103,115 | 29.429% | 0.1175 | 0.6698 |

Measurement 2 - inversion rate
| tau | observations | p_naive>=0.85 & p_twap<=0.60 | share | p_naive<=0.15 & p_twap>=0.40 | share | either | share |
|---|---|---|---|---|---|---|---|
| 240 | 70,078 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 180 | 70,078 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 120 | 70,078 | 34 | 0.049% | 33 | 0.047% | 67 | 0.096% |
| 90 | 70,078 | 227 | 0.324% | 251 | 0.358% | 478 | 0.682% |
| 60 | 70,078 | 733 | 1.046% | 773 | 1.103% | 1,506 | 2.149% |
| all | 350,390 | 994 | 0.284% | 1,057 | 0.302% | 2,051 | 0.585% |

Measurement 4 - Brier score (label outcome_1s)
| tau | observations | brier p_twap | brier p_naive | naive minus twap |
|---|---|---|---|---|
| 240 | 70,078 | 0.1734 | 0.1742 | 0.0008 |
| 180 | 70,078 | 0.1108 | 0.1184 | 0.0076 |
| 120 | 70,078 | 0.0584 | 0.0808 | 0.0223 |
| 90 | 70,078 | 0.0371 | 0.0738 | 0.0367 |
| 60 | 70,078 | 0.0215 | 0.0773 | 0.0558 |
| all | 350,390 | 0.0802 | 0.1049 | 0.0246 |

Measurement 5 - realised frequency inside the inversion cells (label outcome_1s)
| cell | observations | mean p_twap | mean p_naive | realised frequency | |realised - mean p_twap| |
|---|---|---|---|---|---|
| p_naive high / p_twap low | 994 | 0.1751 | 0.9168 | 0.2445 | 0.0694 |
| p_naive low / p_twap high | 1,057 | 0.8100 | 0.0860 | 0.7748 | 0.0352 |
| both cells | 2,051 | 0.5023 | 0.4886 | 0.5178 | 0.0155 |
#### mid tercile (3.764808 <= sigma_pre < 6.236466)
Measurement 1 - disagreement rate (|p_twap - p_naive| >= 0.15)
| tau | observations | disagreements | share | mean gap | 99th pct gap |
|---|---|---|---|---|---|
| 240 | 70,078 | 14,978 | 21.373% | 0.1039 | 0.1814 |
| 180 | 70,078 | 26,793 | 38.233% | 0.1225 | 0.2968 |
| 120 | 70,078 | 26,277 | 37.497% | 0.1336 | 0.5078 |
| 90 | 70,078 | 24,258 | 34.616% | 0.1392 | 0.6772 |
| 60 | 70,078 | 21,657 | 30.904% | 0.1439 | 0.8645 |
| all | 350,390 | 113,963 | 32.525% | 0.1286 | 0.6797 |

Measurement 2 - inversion rate
| tau | observations | p_naive>=0.85 & p_twap<=0.60 | share | p_naive<=0.15 & p_twap>=0.40 | share | either | share |
|---|---|---|---|---|---|---|---|
| 240 | 70,078 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 180 | 70,078 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 120 | 70,078 | 26 | 0.037% | 19 | 0.027% | 45 | 0.064% |
| 90 | 70,078 | 205 | 0.293% | 203 | 0.290% | 408 | 0.582% |
| 60 | 70,078 | 739 | 1.055% | 743 | 1.060% | 1,482 | 2.115% |
| all | 350,390 | 970 | 0.277% | 965 | 0.275% | 1,935 | 0.552% |

Measurement 4 - Brier score (label outcome_1s)
| tau | observations | brier p_twap | brier p_naive | naive minus twap |
|---|---|---|---|---|
| 240 | 70,078 | 0.1721 | 0.1731 | 0.0010 |
| 180 | 70,078 | 0.1077 | 0.1167 | 0.0090 |
| 120 | 70,078 | 0.0572 | 0.0820 | 0.0248 |
| 90 | 70,078 | 0.0348 | 0.0756 | 0.0407 |
| 60 | 70,078 | 0.0196 | 0.0799 | 0.0603 |
| all | 350,390 | 0.0783 | 0.1054 | 0.0272 |

Measurement 5 - realised frequency inside the inversion cells (label outcome_1s)
| cell | observations | mean p_twap | mean p_naive | realised frequency | |realised - mean p_twap| |
|---|---|---|---|---|---|
| p_naive high / p_twap low | 970 | 0.1817 | 0.9177 | 0.2186 | 0.0369 |
| p_naive low / p_twap high | 965 | 0.8153 | 0.0844 | 0.7731 | 0.0422 |
| both cells | 1,935 | 0.4977 | 0.5022 | 0.4951 | 0.0026 |
#### high tercile (sigma_pre >= 6.236466)
Measurement 1 - disagreement rate (|p_twap - p_naive| >= 0.15)
| tau | observations | disagreements | share | mean gap | 99th pct gap |
|---|---|---|---|---|---|
| 240 | 70,078 | 15,213 | 21.709% | 0.1059 | 0.1798 |
| 180 | 70,078 | 28,592 | 40.800% | 0.1279 | 0.2875 |
| 120 | 70,078 | 27,963 | 39.903% | 0.1397 | 0.4915 |
| 90 | 70,078 | 25,741 | 36.732% | 0.1451 | 0.6614 |
| 60 | 70,078 | 22,521 | 32.137% | 0.1481 | 0.8401 |
| all | 350,390 | 120,030 | 34.256% | 0.1333 | 0.6604 |

Measurement 2 - inversion rate
| tau | observations | p_naive>=0.85 & p_twap<=0.60 | share | p_naive<=0.15 & p_twap>=0.40 | share | either | share |
|---|---|---|---|---|---|---|---|
| 240 | 70,078 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 180 | 70,078 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 120 | 70,078 | 12 | 0.017% | 13 | 0.019% | 25 | 0.036% |
| 90 | 70,078 | 174 | 0.248% | 183 | 0.261% | 357 | 0.509% |
| 60 | 70,078 | 647 | 0.923% | 690 | 0.985% | 1,337 | 1.908% |
| all | 350,390 | 833 | 0.238% | 886 | 0.253% | 1,719 | 0.491% |

Measurement 4 - Brier score (label outcome_1s)
| tau | observations | brier p_twap | brier p_naive | naive minus twap |
|---|---|---|---|---|
| 240 | 70,078 | 0.1712 | 0.1747 | 0.0035 |
| 180 | 70,078 | 0.1058 | 0.1184 | 0.0125 |
| 120 | 70,078 | 0.0557 | 0.0833 | 0.0276 |
| 90 | 70,078 | 0.0336 | 0.0771 | 0.0435 |
| 60 | 70,078 | 0.0189 | 0.0808 | 0.0619 |
| all | 350,390 | 0.0771 | 0.1069 | 0.0298 |

Measurement 5 - realised frequency inside the inversion cells (label outcome_1s)
| cell | observations | mean p_twap | mean p_naive | realised frequency | |realised - mean p_twap| |
|---|---|---|---|---|---|
| p_naive high / p_twap low | 833 | 0.2090 | 0.9107 | 0.2353 | 0.0263 |
| p_naive low / p_twap high | 886 | 0.8010 | 0.0899 | 0.7912 | 0.0098 |
| both cells | 1,719 | 0.5141 | 0.4877 | 0.5218 | 0.0077 |

### Label sensitivity - the same numbers under outcome_60s

Measurements 1 and 2 do not use the label and are unchanged. Measurements 4 and 5 under `outcome_60s`, with the `outcome_1s` value beside each.

| variant | quantity | under outcome_1s | under outcome_60s | delta |
|---|---|---|---|---|
| sigma_pre | brier p_twap | 0.0781 | 0.0732 | -0.0049 |
| sigma_pre | brier p_naive | 0.1145 | 0.1148 | 0.0003 |
| sigma_pre | realised frequency in inversion cells | 0.5049 | 0.5036 | -0.0013 |
| sigma_pre | |realised - mean p_twap| in inversion cells | 0.0056 | 0.0043 | -0.0013 |
| sigma_live | brier p_twap | 0.0785 | 0.0726 | -0.0059 |
| sigma_live | brier p_naive | 0.1057 | 0.1057 | -0.0000 |
| sigma_live | realised frequency in inversion cells | 0.5113 | 0.5120 | 0.0007 |
| sigma_live | |realised - mean p_twap| in inversion cells | 0.0070 | 0.0077 | 0.0007 |

Calibration under `outcome_60s`, summarised as the mean absolute gap between predicted and realised frequency across populated buckets.

| variant | model | under outcome_1s | under outcome_60s | delta |
|---|---|---|---|---|
| sigma_pre | p_twap | 0.0122 | 0.0180 | 0.0058 |
| sigma_pre | p_naive | 0.0966 | 0.0994 | 0.0029 |
| sigma_live | p_twap | 0.0216 | 0.0149 | -0.0067 |
| sigma_live | p_naive | 0.0545 | 0.0573 | 0.0029 |

