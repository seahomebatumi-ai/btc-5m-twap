# TZ-01 - TWAP divergence measurement - report

Phase 0 measurement of how often, and by how much, a TWAP-settled probability and an
endpoint-settled probability disagree on real BTC price history.

Both gates were evaluated. **Gate A PASS. Gate B PASS.** The deciding numbers are in
section 4.

---

## 1. What was run

| field | value |
|---|---|
| window | 2024-09 to 2026-08, the 24 calendar months ending with the last complete month before the run date (2026-09-08) |
| source | `data.binance.vision`, public archive, spot `BTCUSDT`, 1-second klines |
| archives downloaded | 24, each verified against its published `.CHECKSUM` before use |
| raw 1-second bars read | 63,072,000 |
| intervals found | 210,240 |
| checkpoint observations written | 1,051,170 |
| network access | the public archive only; no exchange keys, no order placement, no Polymarket or trading-venue API calls |

Processing was one month at a time: download, verify checksum, process, write the month's
Parquet partition, rewrite the combined Parquet and the partial summary, delete the raw
archive. All 24 raw archives were deleted; the run is resumable from any month because each
month's partition and the 1800-second carry tail that feeds the next month are on disk.

---

## 2. Files created

SHA-256 over file bytes. The report itself cannot state its own hash.

| path | lines | bytes | SHA-256 |
|---|---|---|---|
| `research/twap-divergence.py` | 929 | 40,373 | `2a4c67d5d07d41d27aadd705441b6c9747323276b573547a5ee677eb7936b7d6` |
| `research/selftest-twap-divergence.py` | 241 | 9,933 | `8da59b6bd14cc6426a4d3ac3211ad430a598fe73f873d2b8d87291825cfbd100` |
| `research/out/twap-divergence-observations.parquet` | 315,802 | 76,810,985 | `0dc121291b897857ff87d9a1f85a3fc29a340d7c62829f2b21cf371d3c380f1e` |
| `research/out/twap-divergence-summary.md` | 854 | 41,445 | `170c4c666e0dcee6c2b2eff51bc8702c6314cbda979cb24edbb89e6252d5b0c6` |
| `research/out/state/coverage.json` | 292 | 10,293 | `83de2b2a778a8ba2960b413b12af413af4f405b1966e92ce8de7330f8fc38d13` |
| `research/out/partitions/` (24 files, 24 monthly Parquet partitions) | n/a (binary) | 77,377,211 | `e3116f11742f69a598e65a6762ad4efb7dd012e94b990870b0037e03b98aa603` |
| `research/out/state/` (24 files, 24 carry-tail state files) | n/a (binary) | 758,736 | `b9da26b9942e54fea21b73e770dc36aca608929f27aae71b46019ff29e580dbe` |

Nothing else was created. The Python virtual environment and the raw-archive scratch space
live outside the repository, at `/root/tz01-env/`.

---

## 3. Validation (section 7)

### 7.1 Compilation

`python3 -m py_compile` on `research/twap-divergence.py` and
`research/selftest-twap-divergence.py`: clean, no output, exit 0 for both.

### 7.2 Analytic self-tests

24 assertions, 24 passed, 0 failed. Each is a fixed expectation from the TZ, not a value
read back from the implementation.

| path | checkpoint | expectation | result |
|---|---|---|---|
| flat at exactly `K` | all 5 taus | `state == 0` | exact `0.0` at all 5 |
| flat at exactly `K` | all 5 taus | `p_twap == 0.5` | exact `0.5` at all 5, under both sigma variants (10 assertions) |
| linear ramp `K` to `K+100` | all 5 taus | `twap_so_far == K + 50*t/300` to 1e-9 | max error 1.455e-11 (0.0 at four of five) |
| held at `K` 180 s, stepped to `K+70` | tau=120 | `state == 8400` | exact `8400.0` |
| held at `K+40` 180 s, returned to `K` | tau=120 | `state == 7200` | exact `7200.0` |
| held at `K+40` 180 s, returned to `K` | tau=120 | `p_twap - p_naive > 0.10` | 0.5000 under both sigma variants |

### 7.3 Look-ahead truncation test

500 randomly sampled intervals from 2026-08 (seed 20260908), each evaluated at all 5
checkpoints, each compared on all 9 required fields - `naive_move`, `twap_so_far`, `state`,
`sigma_pre`, `sigma_live`, `p_twap_pre`, `p_naive_pre`, `p_twap_live`, `p_naive_live`.

**500 intervals x 5 checkpoints x 9 fields = 22 500 value comparisons. 0 mismatches.**

Comparison was bit-identity on the IEEE-754 representation (`float.hex()`), not a
tolerance. The full interval and a copy with every bar strictly after the checkpoint removed
produce the same bits in every one of the 22 500 cases.

### 7.4 Coverage counts

| count | value |
|---|---|
| months processed | 24 |
| raw 1-second bars read | 63,072,000 |
| 1-second bars missing from the archive | 0 |
| intervals found | 210,240 |
| intervals skipped for gaps (more than 5 of 300 bars missing) | 0 |
| intervals skipped for missing 30-minute run-up | 6 |
| intervals used | 210,234 |
| bars forward-filled inside used intervals | 0 |
| used intervals with a forward-filled bar in their prior window | 0 |
| checkpoint observations written | 1,051,170 |

The archive was complete: 63 072 000 bars is exactly 730 days x 86 400, with zero bars
missing across the whole 24 months. No interval was skipped for gaps and no bar was
forward-filled. The gap-handling and forward-fill code paths are implemented and exercised
by the grid builder, but on this data they never fired. The 6 skipped intervals are the
first 30 minutes of 2024-09, which have no 30-minute run-up inside the window.

### 7.5 Determinism

Re-processing 2026-08 from the stored carry tail produced a Parquet partition with
SHA-256 `2570ed2ea4e6c48d...`, byte-identical to the partition written during the run.

### 7.6 No-regression statement

**Nothing outside `research/` and `CryptoReports/` was created or modified.** `git status`
on a clean checkout reports exactly two top-level paths, `research/` and `CryptoReports/`.
No existing file was modified; `CryptoTZ/TZ-01-twap-divergence.md` is untouched.

---

## 4. Gate verdicts (section 5)

Every result is produced twice, once under `sigma_pre` and once under `sigma_live`. They are
reported separately and neither is averaged with nor preferred to the other, so each gate
carries a verdict per variant.

### Gate A - is there anything to trade? **PASS under both variants**

Threshold: disagreement rate at `tau` in {120, 180} is at least 3% of observations.

| variant | tau | observations | disagreements | rate | verdict |
|---|---|---|---|---|---|
| `sigma_pre` | 120 | 210,234 | 97,826 | **46.532%** | PASS |
| `sigma_pre` | 180 | 210,234 | 89,421 | **42.534%** | PASS |
| `sigma_live` | 120 | 210,234 | 77,833 | **37.022%** | PASS |
| `sigma_live` | 180 | 210,234 | 79,031 | **37.592%** | PASS |

The deciding number is the smallest of the four: **37.022%**, against a 3% threshold.

### Gate B - is the TWAP model correct? **PASS under both variants**

Two conditions, both required: `p_twap` has a strictly lower Brier score than `p_naive`,
and inside the inversion cells the realised frequency is within 0.05 of the mean `p_twap`
of those cells.

| variant | Brier `p_twap` | Brier `p_naive` | Brier test | inversion cell obs | mean `p_twap` | realised | absolute error | calibration test | Gate B |
|---|---|---|---|---|---|---|---|---|---|
| `sigma_pre` | **0.0770** | 0.1140 | PASS | 3,196 | 0.5019 | 0.5094 | **0.0075** | PASS | **PASS** |
| `sigma_live` | **0.0773** | 0.1051 | PASS | 5,829 | 0.5068 | 0.5114 | **0.0046** | PASS | **PASS** |

The calibration condition is evaluated on the union of the two inversion cells, as written.
Each cell also satisfies it separately:

| variant | cell | observations | mean `p_twap` | mean `p_naive` | realised | absolute error |
|---|---|---|---|---|---|---|
| `sigma_pre` | `p_naive`>=0.85 & `p_twap`<=0.60 | 1,562 | 0.1933 | 0.9116 | 0.2273 | 0.0339 |
| `sigma_pre` | `p_naive`<=0.15 & `p_twap`>=0.40 | 1,634 | 0.7969 | 0.0895 | 0.7791 | 0.0179 |
| `sigma_live` | `p_naive`>=0.85 & `p_twap`<=0.60 | 2,839 | 0.1857 | 0.9156 | 0.2265 | 0.0408 |
| `sigma_live` | `p_naive`<=0.15 & `p_twap`>=0.40 | 2,990 | 0.8116 | 0.0869 | 0.7819 | 0.0297 |

---

## 5. Measurements (section 4), in full

Label is `outcome_1s` throughout except where a table names another. The same tables are in
`research/out/twap-divergence-summary.md`; both files are generated from the same Parquet.

## Coverage counts (section 7.4)

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

## Outcome label cadence (section 3)

Pairwise disagreement between the three settlement labels, one row per interval.

| pair | intervals | disagreements | share |
|---|---|---|---|
| outcome_1s vs outcome_30s | 210,234 | 4,018 | 1.911% |
| outcome_1s vs outcome_60s | 210,234 | 8,719 | 4.147% |
| outcome_30s vs outcome_60s | 210,234 | 6,439 | 3.063% |

## Measurements 1 to 5 under sigma_pre

#### All 24 months
Measurement 1 - disagreement rate (|p_twap - p_naive| >= 0.15)
| tau | observations | disagreements | share | mean gap | 99th pct gap |
|---|---|---|---|---|---|
| 240 | 210,234 | 36,194 | 17.216% | 0.0940 | 0.1765 |
| 180 | 210,234 | 89,421 | 42.534% | 0.1276 | 0.2752 |
| 120 | 210,234 | 97,826 | 46.532% | 0.1507 | 0.4597 |
| 90 | 210,234 | 92,280 | 43.894% | 0.1585 | 0.6072 |
| 60 | 210,234 | 82,060 | 39.033% | 0.1627 | 0.7907 |
| all | 1,051,170 | 397,781 | 37.842% | 0.1387 | 0.6074 |

Measurement 2 - inversion rate
| tau | observations | p_naive>=0.85 & p_twap<=0.60 | share | p_naive<=0.15 & p_twap>=0.40 | share | either | share |
|---|---|---|---|---|---|---|---|
| 240 | 210,234 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 180 | 210,234 | 1 | 0.000% | 0 | 0.000% | 1 | 0.000% |
| 120 | 210,234 | 37 | 0.018% | 49 | 0.023% | 86 | 0.041% |
| 90 | 210,234 | 290 | 0.138% | 319 | 0.152% | 609 | 0.290% |
| 60 | 210,234 | 1,234 | 0.587% | 1,266 | 0.602% | 2,500 | 1.189% |
| all | 1,051,170 | 1,562 | 0.149% | 1,634 | 0.155% | 3,196 | 0.304% |

Measurement 3 - calibration of p_twap (label outcome_1s)
| predicted bucket | observations | mean predicted | realised frequency | note |
|---|---|---|---|---|
| [0.00, 0.05) | 298,130 | 0.0052 | 0.0083 |  |
| [0.05, 0.10) | 35,742 | 0.0737 | 0.0708 |  |
| [0.10, 0.15) | 28,263 | 0.1244 | 0.1100 |  |
| [0.15, 0.20) | 25,199 | 0.1746 | 0.1455 |  |
| [0.20, 0.25) | 23,487 | 0.2249 | 0.1973 |  |
| [0.25, 0.30) | 22,553 | 0.2747 | 0.2402 |  |
| [0.30, 0.35) | 22,096 | 0.3248 | 0.2920 |  |
| [0.35, 0.40) | 21,570 | 0.3750 | 0.3418 |  |
| [0.40, 0.45) | 20,816 | 0.4250 | 0.4019 |  |
| [0.45, 0.50) | 30,330 | 0.4828 | 0.4387 |  |
| [0.50, 0.55) | 29,622 | 0.5176 | 0.5587 |  |
| [0.55, 0.60) | 20,823 | 0.5750 | 0.6027 |  |
| [0.60, 0.65) | 21,503 | 0.6252 | 0.6560 |  |
| [0.65, 0.70) | 21,680 | 0.6752 | 0.7143 |  |
| [0.70, 0.75) | 22,737 | 0.7252 | 0.7586 |  |
| [0.75, 0.80) | 23,381 | 0.7751 | 0.8081 |  |
| [0.80, 0.85) | 25,010 | 0.8254 | 0.8461 |  |
| [0.85, 0.90) | 28,013 | 0.8757 | 0.8870 |  |
| [0.90, 0.95) | 35,498 | 0.9264 | 0.9282 |  |
| [0.95, 1.00] | 294,717 | 0.9947 | 0.9914 |  |

Measurement 3 - calibration of p_naive (label outcome_1s)
| predicted bucket | observations | mean predicted | realised frequency | note |
|---|---|---|---|---|
| [0.00, 0.05) | 100,702 | 0.0144 | 0.0043 |  |
| [0.05, 0.10) | 42,950 | 0.0743 | 0.0159 |  |
| [0.10, 0.15) | 40,096 | 0.1250 | 0.0278 |  |
| [0.15, 0.20) | 40,757 | 0.1751 | 0.0466 |  |
| [0.20, 0.25) | 42,319 | 0.2251 | 0.0681 |  |
| [0.25, 0.30) | 45,318 | 0.2753 | 0.1052 |  |
| [0.30, 0.35) | 48,004 | 0.3253 | 0.1576 |  |
| [0.35, 0.40) | 51,291 | 0.3752 | 0.2303 |  |
| [0.40, 0.45) | 52,682 | 0.4251 | 0.3148 |  |
| [0.45, 0.50) | 57,924 | 0.4774 | 0.4205 |  |
| [0.50, 0.55) | 68,635 | 0.5189 | 0.5628 |  |
| [0.55, 0.60) | 52,776 | 0.5750 | 0.6807 |  |
| [0.60, 0.65) | 50,822 | 0.6248 | 0.7725 |  |
| [0.65, 0.70) | 48,201 | 0.6747 | 0.8408 |  |
| [0.70, 0.75) | 44,924 | 0.7247 | 0.8935 |  |
| [0.75, 0.80) | 42,476 | 0.7747 | 0.9287 |  |
| [0.80, 0.85) | 39,601 | 0.8248 | 0.9537 |  |
| [0.85, 0.90) | 39,555 | 0.8751 | 0.9714 |  |
| [0.90, 0.95) | 42,069 | 0.9257 | 0.9856 |  |
| [0.95, 1.00] | 100,068 | 0.9857 | 0.9958 |  |

Measurement 4 - Brier score (label outcome_1s)
| tau | observations | brier p_twap | brier p_naive | naive minus twap |
|---|---|---|---|---|
| 240 | 210,234 | 0.1683 | 0.1799 | 0.0116 |
| 180 | 210,234 | 0.1059 | 0.1283 | 0.0224 |
| 120 | 210,234 | 0.0561 | 0.0933 | 0.0372 |
| 90 | 210,234 | 0.0352 | 0.0847 | 0.0495 |
| 60 | 210,234 | 0.0198 | 0.0839 | 0.0642 |
| all | 1,051,170 | 0.0770 | 0.1140 | 0.0370 |

Measurement 5 - realised frequency inside the inversion cells (label outcome_1s)
| cell | observations | mean p_twap | mean p_naive | realised frequency | |realised - mean p_twap| |
|---|---|---|---|---|---|
| p_naive high / p_twap low | 1,562 | 0.1933 | 0.9116 | 0.2273 | 0.0339 |
| p_naive low / p_twap high | 1,634 | 0.7969 | 0.0895 | 0.7791 | 0.0179 |
| both cells | 3,196 | 0.5019 | 0.4913 | 0.5094 | 0.0075 |

## Measurements 1 to 5 under sigma_live

#### All 24 months
Measurement 1 - disagreement rate (|p_twap - p_naive| >= 0.15)
| tau | observations | disagreements | share | mean gap | 99th pct gap |
|---|---|---|---|---|---|
| 240 | 210,234 | 42,750 | 20.334% | 0.1008 | 0.1813 |
| 180 | 210,234 | 79,031 | 37.592% | 0.1208 | 0.2954 |
| 120 | 210,234 | 77,833 | 37.022% | 0.1322 | 0.5069 |
| 90 | 210,234 | 72,244 | 34.364% | 0.1375 | 0.6767 |
| 60 | 210,234 | 64,257 | 30.565% | 0.1421 | 0.8603 |
| all | 1,051,170 | 336,115 | 31.975% | 0.1267 | 0.6732 |

Measurement 2 - inversion rate
| tau | observations | p_naive>=0.85 & p_twap<=0.60 | share | p_naive<=0.15 & p_twap>=0.40 | share | either | share |
|---|---|---|---|---|---|---|---|
| 240 | 210,234 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 180 | 210,234 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 120 | 210,234 | 74 | 0.035% | 64 | 0.030% | 138 | 0.066% |
| 90 | 210,234 | 620 | 0.295% | 672 | 0.320% | 1,292 | 0.615% |
| 60 | 210,234 | 2,145 | 1.020% | 2,254 | 1.072% | 4,399 | 2.092% |
| all | 1,051,170 | 2,839 | 0.270% | 2,990 | 0.284% | 5,829 | 0.555% |

Measurement 3 - calibration of p_twap (label outcome_1s)
| predicted bucket | observations | mean predicted | realised frequency | note |
|---|---|---|---|---|
| [0.00, 0.05) | 343,316 | 0.0045 | 0.0172 |  |
| [0.05, 0.10) | 32,856 | 0.0735 | 0.1227 |  |
| [0.10, 0.15) | 24,335 | 0.1240 | 0.1716 |  |
| [0.15, 0.20) | 20,872 | 0.1745 | 0.2211 |  |
| [0.20, 0.25) | 18,584 | 0.2248 | 0.2581 |  |
| [0.25, 0.30) | 17,417 | 0.2748 | 0.3035 |  |
| [0.30, 0.35) | 16,530 | 0.3249 | 0.3392 |  |
| [0.35, 0.40) | 15,382 | 0.3750 | 0.3830 |  |
| [0.40, 0.45) | 14,995 | 0.4248 | 0.4183 |  |
| [0.45, 0.50) | 23,899 | 0.4838 | 0.4505 |  |
| [0.50, 0.55) | 23,270 | 0.5166 | 0.5528 |  |
| [0.55, 0.60) | 15,089 | 0.5752 | 0.5727 |  |
| [0.60, 0.65) | 15,440 | 0.6251 | 0.6157 |  |
| [0.65, 0.70) | 16,296 | 0.6751 | 0.6593 |  |
| [0.70, 0.75) | 17,148 | 0.7254 | 0.7046 |  |
| [0.75, 0.80) | 18,473 | 0.7755 | 0.7434 |  |
| [0.80, 0.85) | 20,670 | 0.8256 | 0.7871 |  |
| [0.85, 0.90) | 24,230 | 0.8758 | 0.8236 |  |
| [0.90, 0.95) | 32,253 | 0.9267 | 0.8727 |  |
| [0.95, 1.00] | 340,115 | 0.9955 | 0.9822 |  |

Measurement 3 - calibration of p_naive (label outcome_1s)
| predicted bucket | observations | mean predicted | realised frequency | note |
|---|---|---|---|---|
| [0.00, 0.05) | 151,593 | 0.0127 | 0.0067 |  |
| [0.05, 0.10) | 49,860 | 0.0740 | 0.0303 |  |
| [0.10, 0.15) | 42,853 | 0.1245 | 0.0557 |  |
| [0.15, 0.20) | 40,228 | 0.1749 | 0.0852 |  |
| [0.20, 0.25) | 39,605 | 0.2249 | 0.1186 |  |
| [0.25, 0.30) | 39,091 | 0.2750 | 0.1682 |  |
| [0.30, 0.35) | 38,817 | 0.3250 | 0.2254 |  |
| [0.35, 0.40) | 38,845 | 0.3750 | 0.2887 |  |
| [0.40, 0.45) | 38,545 | 0.4249 | 0.3574 |  |
| [0.45, 0.50) | 42,606 | 0.4781 | 0.4398 |  |
| [0.50, 0.55) | 53,621 | 0.5174 | 0.5478 |  |
| [0.55, 0.60) | 38,165 | 0.5751 | 0.6326 |  |
| [0.60, 0.65) | 38,729 | 0.6250 | 0.7103 |  |
| [0.65, 0.70) | 38,723 | 0.6750 | 0.7716 |  |
| [0.70, 0.75) | 38,582 | 0.7250 | 0.8331 |  |
| [0.75, 0.80) | 39,018 | 0.7751 | 0.8764 |  |
| [0.80, 0.85) | 40,341 | 0.8251 | 0.9146 |  |
| [0.85, 0.90) | 42,297 | 0.8754 | 0.9455 |  |
| [0.90, 0.95) | 49,088 | 0.9259 | 0.9690 |  |
| [0.95, 1.00] | 150,563 | 0.9874 | 0.9931 |  |

Measurement 4 - Brier score (label outcome_1s)
| tau | observations | brier p_twap | brier p_naive | naive minus twap |
|---|---|---|---|---|
| 240 | 210,234 | 0.1703 | 0.1725 | 0.0022 |
| 180 | 210,234 | 0.1065 | 0.1167 | 0.0103 |
| 120 | 210,234 | 0.0559 | 0.0815 | 0.0257 |
| 90 | 210,234 | 0.0345 | 0.0755 | 0.0409 |
| 60 | 210,234 | 0.0192 | 0.0795 | 0.0602 |
| all | 1,051,170 | 0.0773 | 0.1051 | 0.0279 |

Measurement 5 - realised frequency inside the inversion cells (label outcome_1s)
| cell | observations | mean p_twap | mean p_naive | realised frequency | |realised - mean p_twap| |
|---|---|---|---|---|---|
| p_naive high / p_twap low | 2,839 | 0.1857 | 0.9156 | 0.2265 | 0.0408 |
| p_naive low / p_twap high | 2,990 | 0.8116 | 0.0869 | 0.7819 | 0.0297 |
| both cells | 5,829 | 0.5068 | 0.4905 | 0.5114 | 0.0046 |

## Measurement 6 - stability


### sigma_pre

#### first 12 months (2024-09 to 2025-08)
Measurement 1 - disagreement rate (|p_twap - p_naive| >= 0.15)
| tau | observations | disagreements | share | mean gap | 99th pct gap |
|---|---|---|---|---|---|
| 240 | 105,114 | 18,312 | 17.421% | 0.0954 | 0.1761 |
| 180 | 105,114 | 45,106 | 42.912% | 0.1286 | 0.2749 |
| 120 | 105,114 | 48,192 | 45.847% | 0.1498 | 0.4586 |
| 90 | 105,114 | 45,364 | 43.157% | 0.1572 | 0.6085 |
| 60 | 105,114 | 40,122 | 38.170% | 0.1611 | 0.7940 |
| all | 525,570 | 197,096 | 37.501% | 0.1384 | 0.6146 |

Measurement 2 - inversion rate
| tau | observations | p_naive>=0.85 & p_twap<=0.60 | share | p_naive<=0.15 & p_twap>=0.40 | share | either | share |
|---|---|---|---|---|---|---|---|
| 240 | 105,114 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 180 | 105,114 | 1 | 0.001% | 0 | 0.000% | 1 | 0.001% |
| 120 | 105,114 | 24 | 0.023% | 23 | 0.022% | 47 | 0.045% |
| 90 | 105,114 | 153 | 0.146% | 158 | 0.150% | 311 | 0.296% |
| 60 | 105,114 | 671 | 0.638% | 629 | 0.598% | 1,300 | 1.237% |
| all | 525,570 | 849 | 0.162% | 810 | 0.154% | 1,659 | 0.316% |

Measurement 3 - calibration of p_twap (label outcome_1s)
| predicted bucket | observations | mean predicted | realised frequency | note |
|---|---|---|---|---|
| [0.00, 0.05) | 150,509 | 0.0052 | 0.0089 |  |
| [0.05, 0.10) | 18,028 | 0.0737 | 0.0757 |  |
| [0.10, 0.15) | 14,189 | 0.1245 | 0.1159 |  |
| [0.15, 0.20) | 12,497 | 0.1746 | 0.1524 |  |
| [0.20, 0.25) | 11,605 | 0.2249 | 0.2091 |  |
| [0.25, 0.30) | 11,131 | 0.2748 | 0.2445 |  |
| [0.30, 0.35) | 10,828 | 0.3248 | 0.2997 |  |
| [0.35, 0.40) | 10,639 | 0.3750 | 0.3421 |  |
| [0.40, 0.45) | 10,232 | 0.4250 | 0.4044 |  |
| [0.45, 0.50) | 13,817 | 0.4814 | 0.4568 |  |
| [0.50, 0.55) | 13,837 | 0.5182 | 0.5476 |  |
| [0.55, 0.60) | 10,263 | 0.5750 | 0.5949 |  |
| [0.60, 0.65) | 10,466 | 0.6251 | 0.6531 |  |
| [0.65, 0.70) | 10,774 | 0.6752 | 0.7092 |  |
| [0.70, 0.75) | 11,339 | 0.7253 | 0.7514 |  |
| [0.75, 0.80) | 11,682 | 0.7751 | 0.7980 |  |
| [0.80, 0.85) | 12,499 | 0.8255 | 0.8398 |  |
| [0.85, 0.90) | 14,024 | 0.8758 | 0.8838 |  |
| [0.90, 0.95) | 17,862 | 0.9264 | 0.9236 |  |
| [0.95, 1.00] | 149,349 | 0.9948 | 0.9912 |  |

Measurement 3 - calibration of p_naive (label outcome_1s)
| predicted bucket | observations | mean predicted | realised frequency | note |
|---|---|---|---|---|
| [0.00, 0.05) | 51,195 | 0.0146 | 0.0039 |  |
| [0.05, 0.10) | 22,000 | 0.0744 | 0.0155 |  |
| [0.10, 0.15) | 20,519 | 0.1250 | 0.0286 |  |
| [0.15, 0.20) | 20,677 | 0.1751 | 0.0487 |  |
| [0.20, 0.25) | 21,481 | 0.2251 | 0.0738 |  |
| [0.25, 0.30) | 22,761 | 0.2752 | 0.1110 |  |
| [0.30, 0.35) | 23,724 | 0.3252 | 0.1662 |  |
| [0.35, 0.40) | 25,121 | 0.3753 | 0.2378 |  |
| [0.40, 0.45) | 25,859 | 0.4251 | 0.3191 |  |
| [0.45, 0.50) | 27,719 | 0.4770 | 0.4256 |  |
| [0.50, 0.55) | 32,084 | 0.5195 | 0.5577 |  |
| [0.55, 0.60) | 25,675 | 0.5751 | 0.6758 |  |
| [0.60, 0.65) | 25,111 | 0.6248 | 0.7660 |  |
| [0.65, 0.70) | 23,963 | 0.6748 | 0.8349 |  |
| [0.70, 0.75) | 22,702 | 0.7247 | 0.8898 |  |
| [0.75, 0.80) | 21,503 | 0.7748 | 0.9242 |  |
| [0.80, 0.85) | 20,142 | 0.8247 | 0.9523 |  |
| [0.85, 0.90) | 20,230 | 0.8752 | 0.9699 |  |
| [0.90, 0.95) | 21,624 | 0.9258 | 0.9853 |  |
| [0.95, 1.00] | 51,480 | 0.9855 | 0.9960 |  |

Measurement 4 - Brier score (label outcome_1s)
| tau | observations | brier p_twap | brier p_naive | naive minus twap |
|---|---|---|---|---|
| 240 | 105,114 | 0.1697 | 0.1803 | 0.0106 |
| 180 | 105,114 | 0.1057 | 0.1270 | 0.0213 |
| 120 | 105,114 | 0.0553 | 0.0911 | 0.0357 |
| 90 | 105,114 | 0.0345 | 0.0828 | 0.0484 |
| 60 | 105,114 | 0.0192 | 0.0828 | 0.0635 |
| all | 525,570 | 0.0769 | 0.1128 | 0.0359 |

Measurement 5 - realised frequency inside the inversion cells (label outcome_1s)
| cell | observations | mean p_twap | mean p_naive | realised frequency | |realised - mean p_twap| |
|---|---|---|---|---|---|
| p_naive high / p_twap low | 849 | 0.1963 | 0.9108 | 0.2379 | 0.0416 |
| p_naive low / p_twap high | 810 | 0.7947 | 0.0905 | 0.7556 | 0.0392 |
| both cells | 1,659 | 0.4885 | 0.5103 | 0.4907 | 0.0022 |
#### last 12 months (2025-09 to 2026-08)
Measurement 1 - disagreement rate (|p_twap - p_naive| >= 0.15)
| tau | observations | disagreements | share | mean gap | 99th pct gap |
|---|---|---|---|---|---|
| 240 | 105,120 | 17,882 | 17.011% | 0.0926 | 0.1769 |
| 180 | 105,120 | 44,315 | 42.157% | 0.1267 | 0.2757 |
| 120 | 105,120 | 49,634 | 47.217% | 0.1516 | 0.4614 |
| 90 | 105,120 | 46,916 | 44.631% | 0.1598 | 0.6052 |
| 60 | 105,120 | 41,938 | 39.895% | 0.1644 | 0.7867 |
| all | 525,600 | 200,685 | 38.182% | 0.1390 | 0.6011 |

Measurement 2 - inversion rate
| tau | observations | p_naive>=0.85 & p_twap<=0.60 | share | p_naive<=0.15 & p_twap>=0.40 | share | either | share |
|---|---|---|---|---|---|---|---|
| 240 | 105,120 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 180 | 105,120 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 120 | 105,120 | 13 | 0.012% | 26 | 0.025% | 39 | 0.037% |
| 90 | 105,120 | 137 | 0.130% | 161 | 0.153% | 298 | 0.283% |
| 60 | 105,120 | 563 | 0.536% | 637 | 0.606% | 1,200 | 1.142% |
| all | 525,600 | 713 | 0.136% | 824 | 0.157% | 1,537 | 0.292% |

Measurement 3 - calibration of p_twap (label outcome_1s)
| predicted bucket | observations | mean predicted | realised frequency | note |
|---|---|---|---|---|
| [0.00, 0.05) | 147,621 | 0.0053 | 0.0078 |  |
| [0.05, 0.10) | 17,714 | 0.0736 | 0.0658 |  |
| [0.10, 0.15) | 14,074 | 0.1244 | 0.1040 |  |
| [0.15, 0.20) | 12,702 | 0.1747 | 0.1386 |  |
| [0.20, 0.25) | 11,882 | 0.2249 | 0.1857 |  |
| [0.25, 0.30) | 11,422 | 0.2746 | 0.2360 |  |
| [0.30, 0.35) | 11,268 | 0.3249 | 0.2845 |  |
| [0.35, 0.40) | 10,931 | 0.3751 | 0.3414 |  |
| [0.40, 0.45) | 10,584 | 0.4251 | 0.3995 |  |
| [0.45, 0.50) | 16,513 | 0.4839 | 0.4236 |  |
| [0.50, 0.55) | 15,785 | 0.5171 | 0.5685 |  |
| [0.55, 0.60) | 10,560 | 0.5750 | 0.6102 |  |
| [0.60, 0.65) | 11,037 | 0.6254 | 0.6587 |  |
| [0.65, 0.70) | 10,906 | 0.6752 | 0.7194 |  |
| [0.70, 0.75) | 11,398 | 0.7252 | 0.7657 |  |
| [0.75, 0.80) | 11,699 | 0.7751 | 0.8183 |  |
| [0.80, 0.85) | 12,511 | 0.8254 | 0.8523 |  |
| [0.85, 0.90) | 13,989 | 0.8755 | 0.8903 |  |
| [0.90, 0.95) | 17,636 | 0.9264 | 0.9328 |  |
| [0.95, 1.00] | 145,368 | 0.9947 | 0.9917 |  |

Measurement 3 - calibration of p_naive (label outcome_1s)
| predicted bucket | observations | mean predicted | realised frequency | note |
|---|---|---|---|---|
| [0.00, 0.05) | 49,507 | 0.0142 | 0.0047 |  |
| [0.05, 0.10) | 20,950 | 0.0743 | 0.0162 |  |
| [0.10, 0.15) | 19,577 | 0.1250 | 0.0270 |  |
| [0.15, 0.20) | 20,080 | 0.1751 | 0.0445 |  |
| [0.20, 0.25) | 20,838 | 0.2252 | 0.0623 |  |
| [0.25, 0.30) | 22,557 | 0.2755 | 0.0994 |  |
| [0.30, 0.35) | 24,280 | 0.3254 | 0.1491 |  |
| [0.35, 0.40) | 26,170 | 0.3752 | 0.2230 |  |
| [0.40, 0.45) | 26,823 | 0.4250 | 0.3107 |  |
| [0.45, 0.50) | 30,205 | 0.4778 | 0.4158 |  |
| [0.50, 0.55) | 36,551 | 0.5184 | 0.5673 |  |
| [0.55, 0.60) | 27,101 | 0.5749 | 0.6853 |  |
| [0.60, 0.65) | 25,711 | 0.6247 | 0.7788 |  |
| [0.65, 0.70) | 24,238 | 0.6746 | 0.8467 |  |
| [0.70, 0.75) | 22,222 | 0.7246 | 0.8972 |  |
| [0.75, 0.80) | 20,973 | 0.7747 | 0.9333 |  |
| [0.80, 0.85) | 19,459 | 0.8250 | 0.9551 |  |
| [0.85, 0.90) | 19,325 | 0.8750 | 0.9730 |  |
| [0.90, 0.95) | 20,445 | 0.9255 | 0.9858 |  |
| [0.95, 1.00] | 48,588 | 0.9859 | 0.9957 |  |

Measurement 4 - Brier score (label outcome_1s)
| tau | observations | brier p_twap | brier p_naive | naive minus twap |
|---|---|---|---|---|
| 240 | 105,120 | 0.1668 | 0.1794 | 0.0126 |
| 180 | 105,120 | 0.1061 | 0.1296 | 0.0235 |
| 120 | 105,120 | 0.0568 | 0.0955 | 0.0387 |
| 90 | 105,120 | 0.0359 | 0.0865 | 0.0506 |
| 60 | 105,120 | 0.0203 | 0.0851 | 0.0648 |
| all | 525,600 | 0.0772 | 0.1152 | 0.0380 |

Measurement 5 - realised frequency inside the inversion cells (label outcome_1s)
| cell | observations | mean p_twap | mean p_naive | realised frequency | |realised - mean p_twap| |
|---|---|---|---|---|---|
| p_naive high / p_twap low | 713 | 0.1898 | 0.9125 | 0.2146 | 0.0248 |
| p_naive low / p_twap high | 824 | 0.7991 | 0.0886 | 0.8022 | 0.0031 |
| both cells | 1,537 | 0.5165 | 0.4708 | 0.5296 | 0.0132 |

### sigma_live

#### first 12 months (2024-09 to 2025-08)
Measurement 1 - disagreement rate (|p_twap - p_naive| >= 0.15)
| tau | observations | disagreements | share | mean gap | 99th pct gap |
|---|---|---|---|---|---|
| 240 | 105,114 | 21,323 | 20.286% | 0.1017 | 0.1811 |
| 180 | 105,114 | 38,883 | 36.991% | 0.1200 | 0.2979 |
| 120 | 105,114 | 37,638 | 35.807% | 0.1296 | 0.5159 |
| 90 | 105,114 | 35,065 | 33.359% | 0.1352 | 0.6843 |
| 60 | 105,114 | 31,107 | 29.594% | 0.1403 | 0.8713 |
| all | 525,570 | 164,016 | 31.207% | 0.1253 | 0.6854 |

Measurement 2 - inversion rate
| tau | observations | p_naive>=0.85 & p_twap<=0.60 | share | p_naive<=0.15 & p_twap>=0.40 | share | either | share |
|---|---|---|---|---|---|---|---|
| 240 | 105,114 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 180 | 105,114 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 120 | 105,114 | 51 | 0.049% | 32 | 0.030% | 83 | 0.079% |
| 90 | 105,114 | 362 | 0.344% | 362 | 0.344% | 724 | 0.689% |
| 60 | 105,114 | 1,197 | 1.139% | 1,227 | 1.167% | 2,424 | 2.306% |
| all | 525,570 | 1,610 | 0.306% | 1,621 | 0.308% | 3,231 | 0.615% |

Measurement 3 - calibration of p_twap (label outcome_1s)
| predicted bucket | observations | mean predicted | realised frequency | note |
|---|---|---|---|---|
| [0.00, 0.05) | 174,219 | 0.0044 | 0.0187 |  |
| [0.05, 0.10) | 16,244 | 0.0735 | 0.1323 |  |
| [0.10, 0.15) | 11,986 | 0.1240 | 0.1862 |  |
| [0.15, 0.20) | 10,307 | 0.1745 | 0.2320 |  |
| [0.20, 0.25) | 8,991 | 0.2247 | 0.2676 |  |
| [0.25, 0.30) | 8,471 | 0.2748 | 0.3104 |  |
| [0.30, 0.35) | 7,901 | 0.3249 | 0.3463 |  |
| [0.35, 0.40) | 7,439 | 0.3749 | 0.3867 |  |
| [0.40, 0.45) | 7,217 | 0.4250 | 0.4254 |  |
| [0.45, 0.50) | 10,700 | 0.4828 | 0.4665 |  |
| [0.50, 0.55) | 10,768 | 0.5171 | 0.5443 |  |
| [0.55, 0.60) | 7,193 | 0.5752 | 0.5653 |  |
| [0.60, 0.65) | 7,408 | 0.6252 | 0.6060 |  |
| [0.65, 0.70) | 7,912 | 0.6752 | 0.6491 |  |
| [0.70, 0.75) | 8,396 | 0.7256 | 0.6997 |  |
| [0.75, 0.80) | 8,995 | 0.7756 | 0.7369 |  |
| [0.80, 0.85) | 10,195 | 0.8257 | 0.7759 |  |
| [0.85, 0.90) | 11,982 | 0.8758 | 0.8067 |  |
| [0.90, 0.95) | 16,144 | 0.9267 | 0.8663 |  |
| [0.95, 1.00] | 173,102 | 0.9956 | 0.9809 |  |

Measurement 3 - calibration of p_naive (label outcome_1s)
| predicted bucket | observations | mean predicted | realised frequency | note |
|---|---|---|---|---|
| [0.00, 0.05) | 79,116 | 0.0124 | 0.0072 |  |
| [0.05, 0.10) | 25,304 | 0.0740 | 0.0335 |  |
| [0.10, 0.15) | 21,498 | 0.1245 | 0.0601 |  |
| [0.15, 0.20) | 20,111 | 0.1749 | 0.0915 |  |
| [0.20, 0.25) | 19,550 | 0.2249 | 0.1284 |  |
| [0.25, 0.30) | 19,227 | 0.2749 | 0.1816 |  |
| [0.30, 0.35) | 18,912 | 0.3250 | 0.2382 |  |
| [0.35, 0.40) | 18,678 | 0.3750 | 0.2960 |  |
| [0.40, 0.45) | 18,613 | 0.4249 | 0.3610 |  |
| [0.45, 0.50) | 20,047 | 0.4778 | 0.4444 |  |
| [0.50, 0.55) | 24,572 | 0.5179 | 0.5436 |  |
| [0.55, 0.60) | 18,191 | 0.5751 | 0.6243 |  |
| [0.60, 0.65) | 18,680 | 0.6252 | 0.7011 |  |
| [0.65, 0.70) | 18,958 | 0.6751 | 0.7635 |  |
| [0.70, 0.75) | 19,136 | 0.7249 | 0.8211 |  |
| [0.75, 0.80) | 19,464 | 0.7753 | 0.8705 |  |
| [0.80, 0.85) | 20,141 | 0.8251 | 0.9099 |  |
| [0.85, 0.90) | 21,255 | 0.8754 | 0.9407 |  |
| [0.90, 0.95) | 25,092 | 0.9260 | 0.9649 |  |
| [0.95, 1.00] | 79,025 | 0.9878 | 0.9930 |  |

Measurement 4 - Brier score (label outcome_1s)
| tau | observations | brier p_twap | brier p_naive | naive minus twap |
|---|---|---|---|---|
| 240 | 105,114 | 0.1727 | 0.1729 | 0.0003 |
| 180 | 105,114 | 0.1069 | 0.1152 | 0.0083 |
| 120 | 105,114 | 0.0555 | 0.0793 | 0.0238 |
| 90 | 105,114 | 0.0340 | 0.0737 | 0.0397 |
| 60 | 105,114 | 0.0189 | 0.0790 | 0.0601 |
| all | 525,570 | 0.0776 | 0.1040 | 0.0264 |

Measurement 5 - realised frequency inside the inversion cells (label outcome_1s)
| cell | observations | mean p_twap | mean p_naive | realised frequency | |realised - mean p_twap| |
|---|---|---|---|---|---|
| p_naive high / p_twap low | 1,610 | 0.1873 | 0.9162 | 0.2398 | 0.0524 |
| p_naive low / p_twap high | 1,621 | 0.8160 | 0.0872 | 0.7680 | 0.0480 |
| both cells | 3,231 | 0.5028 | 0.5003 | 0.5048 | 0.0020 |
#### last 12 months (2025-09 to 2026-08)
Measurement 1 - disagreement rate (|p_twap - p_naive| >= 0.15)
| tau | observations | disagreements | share | mean gap | 99th pct gap |
|---|---|---|---|---|---|
| 240 | 105,120 | 21,427 | 20.383% | 0.0999 | 0.1815 |
| 180 | 105,120 | 40,148 | 38.193% | 0.1216 | 0.2927 |
| 120 | 105,120 | 40,195 | 38.237% | 0.1347 | 0.4986 |
| 90 | 105,120 | 37,179 | 35.368% | 0.1399 | 0.6693 |
| 60 | 105,120 | 33,150 | 31.535% | 0.1439 | 0.8504 |
| all | 525,600 | 172,099 | 32.743% | 0.1280 | 0.6606 |

Measurement 2 - inversion rate
| tau | observations | p_naive>=0.85 & p_twap<=0.60 | share | p_naive<=0.15 & p_twap>=0.40 | share | either | share |
|---|---|---|---|---|---|---|---|
| 240 | 105,120 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 180 | 105,120 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 120 | 105,120 | 23 | 0.022% | 32 | 0.030% | 55 | 0.052% |
| 90 | 105,120 | 258 | 0.245% | 310 | 0.295% | 568 | 0.540% |
| 60 | 105,120 | 948 | 0.902% | 1,027 | 0.977% | 1,975 | 1.879% |
| all | 525,600 | 1,229 | 0.234% | 1,369 | 0.260% | 2,598 | 0.494% |

Measurement 3 - calibration of p_twap (label outcome_1s)
| predicted bucket | observations | mean predicted | realised frequency | note |
|---|---|---|---|---|
| [0.00, 0.05) | 169,097 | 0.0045 | 0.0157 |  |
| [0.05, 0.10) | 16,612 | 0.0734 | 0.1132 |  |
| [0.10, 0.15) | 12,349 | 0.1241 | 0.1573 |  |
| [0.15, 0.20) | 10,565 | 0.1745 | 0.2105 |  |
| [0.20, 0.25) | 9,593 | 0.2248 | 0.2491 |  |
| [0.25, 0.30) | 8,946 | 0.2748 | 0.2970 |  |
| [0.30, 0.35) | 8,629 | 0.3248 | 0.3327 |  |
| [0.35, 0.40) | 7,943 | 0.3750 | 0.3795 |  |
| [0.40, 0.45) | 7,778 | 0.4247 | 0.4117 |  |
| [0.45, 0.50) | 13,199 | 0.4846 | 0.4375 |  |
| [0.50, 0.55) | 12,502 | 0.5162 | 0.5602 |  |
| [0.55, 0.60) | 7,896 | 0.5753 | 0.5794 |  |
| [0.60, 0.65) | 8,032 | 0.6250 | 0.6246 |  |
| [0.65, 0.70) | 8,384 | 0.6751 | 0.6689 |  |
| [0.70, 0.75) | 8,752 | 0.7253 | 0.7093 |  |
| [0.75, 0.80) | 9,478 | 0.7755 | 0.7496 |  |
| [0.80, 0.85) | 10,475 | 0.8256 | 0.7981 |  |
| [0.85, 0.90) | 12,248 | 0.8759 | 0.8401 |  |
| [0.90, 0.95) | 16,109 | 0.9267 | 0.8791 |  |
| [0.95, 1.00] | 167,013 | 0.9954 | 0.9834 |  |

Measurement 3 - calibration of p_naive (label outcome_1s)
| predicted bucket | observations | mean predicted | realised frequency | note |
|---|---|---|---|---|
| [0.00, 0.05) | 72,477 | 0.0129 | 0.0062 |  |
| [0.05, 0.10) | 24,556 | 0.0740 | 0.0271 |  |
| [0.10, 0.15) | 21,355 | 0.1245 | 0.0514 |  |
| [0.15, 0.20) | 20,117 | 0.1749 | 0.0789 |  |
| [0.20, 0.25) | 20,055 | 0.2249 | 0.1090 |  |
| [0.25, 0.30) | 19,864 | 0.2751 | 0.1553 |  |
| [0.30, 0.35) | 19,905 | 0.3250 | 0.2133 |  |
| [0.35, 0.40) | 20,167 | 0.3750 | 0.2819 |  |
| [0.40, 0.45) | 19,932 | 0.4249 | 0.3541 |  |
| [0.45, 0.50) | 22,559 | 0.4784 | 0.4356 |  |
| [0.50, 0.55) | 29,049 | 0.5169 | 0.5514 |  |
| [0.55, 0.60) | 19,974 | 0.5751 | 0.6402 |  |
| [0.60, 0.65) | 20,049 | 0.6249 | 0.7189 |  |
| [0.65, 0.70) | 19,765 | 0.6749 | 0.7794 |  |
| [0.70, 0.75) | 19,446 | 0.7250 | 0.8450 |  |
| [0.75, 0.80) | 19,554 | 0.7748 | 0.8823 |  |
| [0.80, 0.85) | 20,200 | 0.8251 | 0.9194 |  |
| [0.85, 0.90) | 21,042 | 0.8754 | 0.9504 |  |
| [0.90, 0.95) | 23,996 | 0.9258 | 0.9732 |  |
| [0.95, 1.00] | 71,538 | 0.9870 | 0.9933 |  |

Measurement 4 - Brier score (label outcome_1s)
| tau | observations | brier p_twap | brier p_naive | naive minus twap |
|---|---|---|---|---|
| 240 | 105,120 | 0.1679 | 0.1721 | 0.0042 |
| 180 | 105,120 | 0.1060 | 0.1182 | 0.0122 |
| 120 | 105,120 | 0.0562 | 0.0838 | 0.0276 |
| 90 | 105,120 | 0.0350 | 0.0772 | 0.0422 |
| 60 | 105,120 | 0.0196 | 0.0800 | 0.0604 |
| all | 525,600 | 0.0769 | 0.1063 | 0.0293 |

Measurement 5 - realised frequency inside the inversion cells (label outcome_1s)
| cell | observations | mean p_twap | mean p_naive | realised frequency | |realised - mean p_twap| |
|---|---|---|---|---|---|
| p_naive high / p_twap low | 1,229 | 0.1836 | 0.9147 | 0.2091 | 0.0255 |
| p_naive low / p_twap high | 1,369 | 0.8065 | 0.0865 | 0.7984 | 0.0081 |
| both cells | 2,598 | 0.5118 | 0.4783 | 0.5196 | 0.0078 |

## Measurement 7 - volatility regime split (terciles of sigma_pre)

Tercile edges of `sigma_pre` in dollars per sqrt(second): 3.764808 and 6.236466.

### sigma_pre

#### low tercile (sigma_pre < 3.764808)
Measurement 1 - disagreement rate (|p_twap - p_naive| >= 0.15)
| tau | observations | disagreements | share | mean gap | 99th pct gap |
|---|---|---|---|---|---|
| 240 | 70,078 | 11,597 | 16.549% | 0.0880 | 0.1772 |
| 180 | 70,078 | 27,383 | 39.075% | 0.1198 | 0.2787 |
| 120 | 70,078 | 30,098 | 42.949% | 0.1414 | 0.4774 |
| 90 | 70,078 | 28,578 | 40.780% | 0.1487 | 0.6255 |
| 60 | 70,078 | 25,543 | 36.449% | 0.1534 | 0.8080 |
| all | 350,390 | 123,199 | 35.161% | 0.1303 | 0.6147 |

Measurement 2 - inversion rate
| tau | observations | p_naive>=0.85 & p_twap<=0.60 | share | p_naive<=0.15 & p_twap>=0.40 | share | either | share |
|---|---|---|---|---|---|---|---|
| 240 | 70,078 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 180 | 70,078 | 1 | 0.001% | 0 | 0.000% | 1 | 0.001% |
| 120 | 70,078 | 18 | 0.026% | 24 | 0.034% | 42 | 0.060% |
| 90 | 70,078 | 128 | 0.183% | 141 | 0.201% | 269 | 0.384% |
| 60 | 70,078 | 460 | 0.656% | 486 | 0.694% | 946 | 1.350% |
| all | 350,390 | 607 | 0.173% | 651 | 0.186% | 1,258 | 0.359% |

Measurement 4 - Brier score (label outcome_1s)
| tau | observations | brier p_twap | brier p_naive | naive minus twap |
|---|---|---|---|---|
| 240 | 70,078 | 0.1691 | 0.1790 | 0.0099 |
| 180 | 70,078 | 0.1083 | 0.1279 | 0.0196 |
| 120 | 70,078 | 0.0576 | 0.0916 | 0.0340 |
| 90 | 70,078 | 0.0373 | 0.0830 | 0.0456 |
| 60 | 70,078 | 0.0217 | 0.0824 | 0.0607 |
| all | 350,390 | 0.0788 | 0.1128 | 0.0340 |

Measurement 5 - realised frequency inside the inversion cells (label outcome_1s)
| cell | observations | mean p_twap | mean p_naive | realised frequency | |realised - mean p_twap| |
|---|---|---|---|---|---|
| p_naive high / p_twap low | 607 | 0.1808 | 0.9177 | 0.2586 | 0.0778 |
| p_naive low / p_twap high | 651 | 0.8076 | 0.0847 | 0.7696 | 0.0380 |
| both cells | 1,258 | 0.5052 | 0.4866 | 0.5231 | 0.0179 |
#### mid tercile (3.764808 <= sigma_pre < 6.236466)
Measurement 1 - disagreement rate (|p_twap - p_naive| >= 0.15)
| tau | observations | disagreements | share | mean gap | 99th pct gap |
|---|---|---|---|---|---|
| 240 | 70,078 | 12,389 | 17.679% | 0.0967 | 0.1765 |
| 180 | 70,078 | 30,400 | 43.380% | 0.1301 | 0.2762 |
| 120 | 70,078 | 33,075 | 47.197% | 0.1530 | 0.4593 |
| 90 | 70,078 | 31,141 | 44.438% | 0.1610 | 0.6060 |
| 60 | 70,078 | 27,673 | 39.489% | 0.1654 | 0.7933 |
| all | 350,390 | 134,678 | 38.437% | 0.1412 | 0.6148 |

Measurement 2 - inversion rate
| tau | observations | p_naive>=0.85 & p_twap<=0.60 | share | p_naive<=0.15 & p_twap>=0.40 | share | either | share |
|---|---|---|---|---|---|---|---|
| 240 | 70,078 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 180 | 70,078 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 120 | 70,078 | 12 | 0.017% | 14 | 0.020% | 26 | 0.037% |
| 90 | 70,078 | 94 | 0.134% | 102 | 0.146% | 196 | 0.280% |
| 60 | 70,078 | 432 | 0.616% | 416 | 0.594% | 848 | 1.210% |
| all | 350,390 | 538 | 0.154% | 532 | 0.152% | 1,070 | 0.305% |

Measurement 4 - Brier score (label outcome_1s)
| tau | observations | brier p_twap | brier p_naive | naive minus twap |
|---|---|---|---|---|
| 240 | 70,078 | 0.1676 | 0.1792 | 0.0116 |
| 180 | 70,078 | 0.1050 | 0.1274 | 0.0224 |
| 120 | 70,078 | 0.0558 | 0.0932 | 0.0375 |
| 90 | 70,078 | 0.0345 | 0.0846 | 0.0501 |
| 60 | 70,078 | 0.0190 | 0.0842 | 0.0652 |
| all | 350,390 | 0.0764 | 0.1137 | 0.0374 |

Measurement 5 - realised frequency inside the inversion cells (label outcome_1s)
| cell | observations | mean p_twap | mean p_naive | realised frequency | |realised - mean p_twap| |
|---|---|---|---|---|---|
| p_naive high / p_twap low | 538 | 0.2049 | 0.9105 | 0.2138 | 0.0089 |
| p_naive low / p_twap high | 532 | 0.7974 | 0.0899 | 0.7688 | 0.0286 |
| both cells | 1,070 | 0.4995 | 0.5025 | 0.4897 | 0.0098 |
#### high tercile (sigma_pre >= 6.236466)
Measurement 1 - disagreement rate (|p_twap - p_naive| >= 0.15)
| tau | observations | disagreements | share | mean gap | 99th pct gap |
|---|---|---|---|---|---|
| 240 | 70,078 | 12,208 | 17.421% | 0.0972 | 0.1757 |
| 180 | 70,078 | 31,638 | 45.147% | 0.1329 | 0.2710 |
| 120 | 70,078 | 34,653 | 49.449% | 0.1576 | 0.4417 |
| 90 | 70,078 | 32,561 | 46.464% | 0.1657 | 0.5932 |
| 60 | 70,078 | 28,844 | 41.160% | 0.1694 | 0.7683 |
| all | 350,390 | 139,904 | 39.928% | 0.1446 | 0.5965 |

Measurement 2 - inversion rate
| tau | observations | p_naive>=0.85 & p_twap<=0.60 | share | p_naive<=0.15 & p_twap>=0.40 | share | either | share |
|---|---|---|---|---|---|---|---|
| 240 | 70,078 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 180 | 70,078 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 120 | 70,078 | 7 | 0.010% | 11 | 0.016% | 18 | 0.026% |
| 90 | 70,078 | 68 | 0.097% | 76 | 0.108% | 144 | 0.205% |
| 60 | 70,078 | 342 | 0.488% | 364 | 0.519% | 706 | 1.007% |
| all | 350,390 | 417 | 0.119% | 451 | 0.129% | 868 | 0.248% |

Measurement 4 - Brier score (label outcome_1s)
| tau | observations | brier p_twap | brier p_naive | naive minus twap |
|---|---|---|---|---|
| 240 | 70,078 | 0.1681 | 0.1813 | 0.0132 |
| 180 | 70,078 | 0.1043 | 0.1297 | 0.0253 |
| 120 | 70,078 | 0.0548 | 0.0950 | 0.0402 |
| 90 | 70,078 | 0.0338 | 0.0865 | 0.0527 |
| 60 | 70,078 | 0.0186 | 0.0853 | 0.0667 |
| all | 350,390 | 0.0759 | 0.1156 | 0.0396 |

Measurement 5 - realised frequency inside the inversion cells (label outcome_1s)
| cell | observations | mean p_twap | mean p_naive | realised frequency | |realised - mean p_twap| |
|---|---|---|---|---|---|
| p_naive high / p_twap low | 417 | 0.1966 | 0.9042 | 0.1990 | 0.0025 |
| p_naive low / p_twap high | 451 | 0.7810 | 0.0961 | 0.8049 | 0.0239 |
| both cells | 868 | 0.5002 | 0.4843 | 0.5138 | 0.0136 |

### sigma_live

#### low tercile (sigma_pre < 3.764808)
Measurement 1 - disagreement rate (|p_twap - p_naive| >= 0.15)
| tau | observations | disagreements | share | mean gap | 99th pct gap |
|---|---|---|---|---|---|
| 240 | 70,078 | 12,980 | 18.522% | 0.0930 | 0.1812 |
| 180 | 70,078 | 23,823 | 33.995% | 0.1120 | 0.2995 |
| 120 | 70,078 | 23,713 | 33.838% | 0.1227 | 0.5164 |
| 90 | 70,078 | 22,207 | 31.689% | 0.1280 | 0.6854 |
| 60 | 70,078 | 19,989 | 28.524% | 0.1332 | 0.8709 |
| all | 350,390 | 102,712 | 29.314% | 0.1178 | 0.6748 |

Measurement 2 - inversion rate
| tau | observations | p_naive>=0.85 & p_twap<=0.60 | share | p_naive<=0.15 & p_twap>=0.40 | share | either | share |
|---|---|---|---|---|---|---|---|
| 240 | 70,078 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 180 | 70,078 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 120 | 70,078 | 34 | 0.049% | 29 | 0.041% | 63 | 0.090% |
| 90 | 70,078 | 231 | 0.330% | 269 | 0.384% | 500 | 0.713% |
| 60 | 70,078 | 751 | 1.072% | 784 | 1.119% | 1,535 | 2.190% |
| all | 350,390 | 1,016 | 0.290% | 1,082 | 0.309% | 2,098 | 0.599% |

Measurement 4 - Brier score (label outcome_1s)
| tau | observations | brier p_twap | brier p_naive | naive minus twap |
|---|---|---|---|---|
| 240 | 70,078 | 0.1714 | 0.1725 | 0.0011 |
| 180 | 70,078 | 0.1092 | 0.1172 | 0.0081 |
| 120 | 70,078 | 0.0572 | 0.0802 | 0.0231 |
| 90 | 70,078 | 0.0365 | 0.0738 | 0.0374 |
| 60 | 70,078 | 0.0207 | 0.0774 | 0.0568 |
| all | 350,390 | 0.0790 | 0.1042 | 0.0253 |

Measurement 5 - realised frequency inside the inversion cells (label outcome_1s)
| cell | observations | mean p_twap | mean p_naive | realised frequency | |realised - mean p_twap| |
|---|---|---|---|---|---|
| p_naive high / p_twap low | 1,016 | 0.1772 | 0.9170 | 0.2431 | 0.0659 |
| p_naive low / p_twap high | 1,082 | 0.8147 | 0.0854 | 0.7745 | 0.0402 |
| both cells | 2,098 | 0.5060 | 0.4881 | 0.5172 | 0.0112 |
#### mid tercile (3.764808 <= sigma_pre < 6.236466)
Measurement 1 - disagreement rate (|p_twap - p_naive| >= 0.15)
| tau | observations | disagreements | share | mean gap | 99th pct gap |
|---|---|---|---|---|---|
| 240 | 70,078 | 14,773 | 21.081% | 0.1038 | 0.1822 |
| 180 | 70,078 | 26,670 | 38.058% | 0.1224 | 0.2983 |
| 120 | 70,078 | 26,206 | 37.395% | 0.1338 | 0.5106 |
| 90 | 70,078 | 24,269 | 34.631% | 0.1395 | 0.6820 |
| 60 | 70,078 | 21,692 | 30.954% | 0.1445 | 0.8678 |
| all | 350,390 | 113,610 | 32.424% | 0.1288 | 0.6827 |

Measurement 2 - inversion rate
| tau | observations | p_naive>=0.85 & p_twap<=0.60 | share | p_naive<=0.15 & p_twap>=0.40 | share | either | share |
|---|---|---|---|---|---|---|---|
| 240 | 70,078 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 180 | 70,078 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 120 | 70,078 | 22 | 0.031% | 21 | 0.030% | 43 | 0.061% |
| 90 | 70,078 | 211 | 0.301% | 213 | 0.304% | 424 | 0.605% |
| 60 | 70,078 | 756 | 1.079% | 764 | 1.090% | 1,520 | 2.169% |
| all | 350,390 | 989 | 0.282% | 998 | 0.285% | 1,987 | 0.567% |

Measurement 4 - Brier score (label outcome_1s)
| tau | observations | brier p_twap | brier p_naive | naive minus twap |
|---|---|---|---|---|
| 240 | 70,078 | 0.1702 | 0.1717 | 0.0015 |
| 180 | 70,078 | 0.1059 | 0.1156 | 0.0096 |
| 120 | 70,078 | 0.0559 | 0.0815 | 0.0256 |
| 90 | 70,078 | 0.0341 | 0.0756 | 0.0415 |
| 60 | 70,078 | 0.0188 | 0.0801 | 0.0613 |
| all | 350,390 | 0.0770 | 0.1049 | 0.0279 |

Measurement 5 - realised frequency inside the inversion cells (label outcome_1s)
| cell | observations | mean p_twap | mean p_naive | realised frequency | |realised - mean p_twap| |
|---|---|---|---|---|---|
| p_naive high / p_twap low | 989 | 0.1740 | 0.9181 | 0.2063 | 0.0323 |
| p_naive low / p_twap high | 998 | 0.8145 | 0.0850 | 0.7675 | 0.0470 |
| both cells | 1,987 | 0.4957 | 0.4997 | 0.4882 | 0.0075 |
#### high tercile (sigma_pre >= 6.236466)
Measurement 1 - disagreement rate (|p_twap - p_naive| >= 0.15)
| tau | observations | disagreements | share | mean gap | 99th pct gap |
|---|---|---|---|---|---|
| 240 | 70,078 | 14,997 | 21.400% | 0.1057 | 0.1802 |
| 180 | 70,078 | 28,538 | 40.723% | 0.1279 | 0.2885 |
| 120 | 70,078 | 27,914 | 39.833% | 0.1400 | 0.4946 |
| 90 | 70,078 | 25,768 | 36.770% | 0.1451 | 0.6630 |
| 60 | 70,078 | 22,576 | 32.216% | 0.1486 | 0.8410 |
| all | 350,390 | 119,793 | 34.188% | 0.1335 | 0.6633 |

Measurement 2 - inversion rate
| tau | observations | p_naive>=0.85 & p_twap<=0.60 | share | p_naive<=0.15 & p_twap>=0.40 | share | either | share |
|---|---|---|---|---|---|---|---|
| 240 | 70,078 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 180 | 70,078 | 0 | 0.000% | 0 | 0.000% | 0 | 0.000% |
| 120 | 70,078 | 18 | 0.026% | 14 | 0.020% | 32 | 0.046% |
| 90 | 70,078 | 178 | 0.254% | 190 | 0.271% | 368 | 0.525% |
| 60 | 70,078 | 638 | 0.910% | 706 | 1.007% | 1,344 | 1.918% |
| all | 350,390 | 834 | 0.238% | 910 | 0.260% | 1,744 | 0.498% |

Measurement 4 - Brier score (label outcome_1s)
| tau | observations | brier p_twap | brier p_naive | naive minus twap |
|---|---|---|---|---|
| 240 | 70,078 | 0.1692 | 0.1733 | 0.0041 |
| 180 | 70,078 | 0.1043 | 0.1174 | 0.0131 |
| 120 | 70,078 | 0.0545 | 0.0829 | 0.0284 |
| 90 | 70,078 | 0.0330 | 0.0770 | 0.0440 |
| 60 | 70,078 | 0.0183 | 0.0810 | 0.0627 |
| all | 350,390 | 0.0759 | 0.1063 | 0.0304 |

Measurement 5 - realised frequency inside the inversion cells (label outcome_1s)
| cell | observations | mean p_twap | mean p_naive | realised frequency | |realised - mean p_twap| |
|---|---|---|---|---|---|
| p_naive high / p_twap low | 834 | 0.2101 | 0.9108 | 0.2302 | 0.0202 |
| p_naive low / p_twap high | 910 | 0.8049 | 0.0908 | 0.8066 | 0.0017 |
| both cells | 1,744 | 0.5204 | 0.4829 | 0.5310 | 0.0105 |

## Label sensitivity - the same numbers under outcome_60s

Measurements 1 and 2 do not use the label and are unchanged. Measurements 4 and 5 under `outcome_60s`, with the `outcome_1s` value beside each.

| variant | quantity | under outcome_1s | under outcome_60s | delta |
|---|---|---|---|---|
| sigma_pre | brier p_twap | 0.0770 | 0.0720 | -0.0050 |
| sigma_pre | brier p_naive | 0.1140 | 0.1142 | 0.0002 |
| sigma_pre | realised frequency in inversion cells | 0.5094 | 0.5091 | -0.0003 |
| sigma_pre | |realised - mean p_twap| in inversion cells | 0.0075 | 0.0071 | -0.0003 |
| sigma_live | brier p_twap | 0.0773 | 0.0712 | -0.0061 |
| sigma_live | brier p_naive | 0.1051 | 0.1051 | -0.0001 |
| sigma_live | realised frequency in inversion cells | 0.5114 | 0.5159 | 0.0045 |
| sigma_live | |realised - mean p_twap| in inversion cells | 0.0046 | 0.0091 | 0.0045 |

Calibration under `outcome_60s`, summarised as the mean absolute gap between predicted and realised frequency across populated buckets.

| variant | model | under outcome_1s | under outcome_60s | delta |
|---|---|---|---|---|
| sigma_pre | p_twap | 0.0129 | 0.0190 | 0.0061 |
| sigma_pre | p_naive | 0.0973 | 0.1004 | 0.0031 |
| sigma_live | p_twap | 0.0200 | 0.0133 | -0.0067 |
| sigma_live | p_naive | 0.0552 | 0.0583 | 0.0031 |


---

## 6. Named plainly: everything that could not be implemented exactly as written

### 6.1 `twap_so_far` - the TZ's own self-tests contradict the literal reading of `[0, t]`

Section 3 defines `twap_so_far = mean(close of every bar in [0, t])`. Read as bar indices
0 to t **inclusive**, two of the four fixed section 7.2 expectations become unsatisfiable
under any construction of the stated path:

- "held at `K` for 180 s then stepped to `K + 70`, `state == 8400` at `tau = 120`" requires
  `state = 180 * (twap_so_far - K) + 120 * (S_t - K) = 8400`. Since `8400 = 120 * 70`, it
  requires `S_t = K + 70` **and** `twap_so_far = K` exactly. If the bar carrying
  `S_t = K + 70` is inside the averaging window, `twap_so_far` cannot equal `K`. Computed
  under the inclusive reading the value is 8469.613, not 8400.
- "held at `K + 40` for 180 s then returned to `K`", `state == 7200` at `tau = 120`, gives
  7160.221 under the inclusive reading, not 7200.

Read as the `t` bars covering elapsed seconds `[0, t)` - bar `i` occupies `[i, i+1)`, so the
bars lying in the elapsed interval are `0` to `t-1` - both land exactly on 8400.0 and
7200.0. This reading was adopted. Three further facts support it:

1. **Dimensional consistency.** `state` is documented as expected total price-seconds above
   the open. The elapsed part is `t * (twap_so_far - K)`, which is only price-seconds if the
   average is taken over exactly `t` bars of one second each. Under the inclusive reading
   `t` seconds are multiplied by an average over `t+1` seconds.
2. **`S_t` is the checkpoint bar.** Section 7.3 removes "every bar strictly after the
   checkpoint", and `sigma_live` runs "up to and including the checkpoint bar". Both fix the
   checkpoint bar at index `t`, and the self-tests fix `S_t` as its close. A bar cannot
   simultaneously be the not-yet-averaged current price and a member of the elapsed average.
3. **The label agrees.** Under this reading `twap_so_far` evaluated at `t = 300` is exactly
   `outcome_1s`'s settlement TWAP, the mean of all 300 closes. Under the inclusive reading
   it would need a 301st bar that does not exist.

This is an interpretation of an ambiguous definition, resolved by the TZ's own fixed
expectations rather than by choice. It is the single most consequential decision in this
report: every number here depends on it. If the Architect intended the inclusive reading,
the self-test expectations in section 7.2 are the thing that must change, and this
measurement must be re-run.

### 6.2 The linear-ramp self-test needs a stated discretisation

"Linear ramp from `K` to `K + 100`" does not say where on each bar the ramp is sampled. The
expectation `twap_so_far == K + 50 * t / 300` at **every** checkpoint holds exactly for one
discretisation only: bar `i` closes at `K + 100 * (i + 0.5) / 300`, the ramp sampled at bar
midpoints. Sampling at bar opens (`100*i/300`) or bar closes (`100*(i+1)/300`) misses by
0.167 and 0.333 dollars respectively at some checkpoint. Midpoint sampling is also the
natural one - a bar's price level represents the second it covers. Max error achieved:
1.455e-11.

### 6.3 `Phi` of a zero scale

The flat-path self-test requires `p_twap == 0.5` on a path with zero volatility. There
`sigma_dollar = 0`, so `sd_remaining = 0` and `state = 0`, and `Phi(state / sd_remaining)`
is `Phi(0/0)`. The TZ does not define this. One function, `normal_probability`, applies the
limit as the scale goes to zero from above: 1.0 for a positive numerator, 0.0 for a
negative one, 0.5 when the numerator is also zero. On the 24 months of real data this
branch is never taken - `sigma_pre` and `sigma_live` are strictly positive in all
1 051 170 observations.

### 6.4 `sigma_pre` yields 29 log returns, not 30

"1-minute log returns over the 30 minutes strictly before the interval open": the 30 minutes
strictly before the open contain 30 one-minute bars, whose 30 closes give 29 consecutive log
returns. Sample standard deviation with `ddof=1` over those 29 returns, converted with
`sigma_pre = K * sd / sqrt(60)`. Reaching 30 returns would require the close of a bar 31
minutes before the open, which is outside the stated window.

### 6.5 `sigma_live`'s dollar conversion price is unstated

Section 3 says `sigma_pre` is converted to dollars "at price `K`" but says nothing for
`sigma_live`. `K` is used for both, so the two variants differ only in their return series
and not in their price level, and so that the dollar scale is fixed at the interval open
rather than moving with the checkpoint. `sigma_live = K * sd` of the 1-second log returns
over `[open - 300 s, checkpoint bar]` inclusive, `ddof=1`.

### 6.6 Label sampling marks

`outcome_30s` and `outcome_60s` are "the 10 closes at 30-second marks" and "the 5 closes at
60-second marks". Marks are taken at elapsed seconds 0, 30, ... 270 and 0, 60, ... 240,
which gives exactly the 10 and 5 closes the TZ states and nests inside `outcome_1s`'s marks
at 0 ... 299. This matches the convention forced elsewhere by `S_t` being the close of the
bar at elapsed second `t`.

### 6.7 The first 6 intervals of the window have no run-up

`sigma_pre` needs 30 minutes of history before the interval open. The first 6 intervals of
2024-09 have none, and are skipped and counted (`intervals_skipped_no_history` = 6). Every
later month gets its run-up from a 1800-second carry tail handed over by the previous month,
so no interval anywhere else in the window is lost to a month boundary.

### 6.8 Venue limitation, as instructed

This measures Binance spot `BTCUSDT`, not the Chainlink oracle stream that Polymarket
actually settles on. The geometric property being measured - whether a running average and
an endpoint disagree - does not depend on the venue, but the labels here are not
settlement-accurate. Settlement-accurate labelling is TZ-02's problem and was not worked
around. The size of the effect that cadence alone contributes is measured and reported: the
1-second and 60-second labels disagree on 8 719 of 210 234 intervals, 4.147%.

### 6.9 Gate evaluation with two volatility variants

Section 5 states each gate as a single threshold, but section 3 requires every result twice
and forbids picking a winner. Both gates are therefore reported per variant. Both pass under
both, so no tie-break was needed and none was invented.

### 6.10 Gate B's calibration condition is evaluated on the union of the cells

"Inside the inversion cells the realised frequency is within 0.05 of the mean `p_twap` of
those cells" is read as the union of the two cells, which is what the plural says. Because
the two cells sit on opposite sides of 0.5, the union's realised frequency is close to 0.5
by construction and the union is the easier test. The per-cell numbers are therefore also
reported in section 4; the condition holds in every cell separately as well, the largest
absolute error being 0.0408.

### 6.11 Deliverable file size

`research/out/twap-divergence-observations.parquet` is 76 810 985 bytes. That is under
GitHub's 100 MB per-file hard limit but above its 50 MB warning threshold. Float columns are
byte-stream-split and compressed with zstd at a fixed level, which is what keeps it under
the limit; the settings are fixed so the file is reproducible byte-for-byte. Every section 3
quantity reconstructs exactly from the stored columns alone, with no re-run of the pipeline
and no floating-point drift - verified for all 24 partitions.

### 6.12 Nothing was tuned

No gate threshold, no formula and no parameter was adjusted at any point. `p_naive` is
computed exactly as written in section 3. Both gates passed on the first and only full run.

### 6.13 The branch was committed but could not be pushed, and no pull request exists

Operating rule 1 requires the implementation to go to a branch named
`tz-01-twap-divergence` and a pull request, with the report going straight to `main`.

The branch exists locally and carries the full implementation as commit `66b8c9d`
(53 files, 2 316 insertions). It was **not pushed**, and **no pull request was opened**,
because this environment has no GitHub credentials: `git push` fails with
`could not read Username for 'https://github.com'`, the `gh` CLI is not installed, and the
GitHub MCP server is unauthenticated and cannot complete an OAuth flow in a non-interactive
session. Nothing was merged.

Both commits are on disk and ready. To publish them, from the repository root:

```
git push -u origin tz-01-twap-divergence
git push origin main
```

then open the pull request from `tz-01-twap-divergence` into `main`. Do not merge it; the
Architect's verdict comes first.
