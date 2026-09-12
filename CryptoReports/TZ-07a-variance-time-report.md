# TZ-07a — the oracle feed's variance–time curve, the corrected sigma, and the maker programme's own numbers

**Executed 2026-09-12 on the capture host.** Both gates pass. The curve is measured at fifteen lags over the 400 TZ-06 members, the five constants it implies are frozen into `research/pfair.py` as literals, and V1–V9 are below as counts.

**No calibration claim about the corrected pricer appears in this report.** §2.5's tables are in-sample on the set that produced the finding and are labelled so; they support nothing. The out-of-sample test is TZ-08's, against the gate the TZ's §8 fixes and this branch commits to git unchanged, before the intervals it will score have happened.

---

## 0. Fingerprint

### 0.1 The anchors TZ-07a §0 requires, against `SYSTEM-MAP.md` §0 on `main`

| anchor | required by TZ-07a §0 | read from the map | match |
|---|---|---|---|
| System Map revision | `2026-09-12-c` | `2026-09-12-c` | **yes** |
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` | **yes** |
| `A2` — collector | `6c5089330629` | `6c5089330629` | **yes** |
| `A3` — phase | `0-complete / 1-open / 2-not-started` | `0-complete / 1-open / 2-not-started` | **yes** |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b` | **yes** |
| `A5` — recorder | `9fd1c7de0f74` | `9fd1c7de0f74` | **yes** |
| `A6` — pricer | `18be5d185fee` | `18be5d185fee` | **yes** |

The map read is `SYSTEM-MAP.md` at `main` = `fed99e4`, which the Architect re-uploaded as revision `2026-09-12-c`. `A2`, `A4`, `A5` and `A6` are the first twelve hex characters of the SHA-256 of the artifacts in §0.2 below and were recomputed there, not copied. `A1` and `A3` are declarations of the map and are compared as strings; no Release asset was downloaded, because TZ-07a reads no dataset.

### 0.2 The map's §0 fingerprint table, as committed on `main`

| path | `wc -l` | bytes | state | SHA-256 | matches the map |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 335 | 28,136 | reported | `81607e537fbce78fb0c32d5773d496b8547966e8b302f966f6f44860e1a56657` | self-reference |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | **yes** |
| `research/twap-divergence.py` | 1135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | **yes** |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | **yes** |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | **yes** |
| `research/pfair.py` | 233 | 9,844 | frozen | `18be5d185fee807fef9a840ab965dc42fa41c3a7a0b01b27c359afce96289676` | **yes** |
| `research/selftest-pfair.py` | 221 | 10,939 | frozen | `f4b4f8287f3ebb0c9cbabaee40e87580bddab6d23ad0fe0e44aa87bc09bc3842` | **yes** |
| `research/tz06-calibration.py` | 569 | 26,548 | frozen | `a6aaed94964775f34a9b26dba448ff0f998f32ad952e244bff834b67439ef123` | **yes** |
| `research/recorder/recorder.py` | 608 | 25,658 | frozen | `9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03` | **yes** |
| `research/recorder/config.py` | 112 | 4,773 | frozen | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | **yes** |
| `research/recorder/manifest.py` | 254 | 10,002 | frozen | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | **yes** |
| `research/recorder/analyze.py` | 813 | 34,705 | frozen | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` | **yes** |
| `research/recorder/probe.py` | 227 | 9,324 | frozen | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | **yes** |
| `research/recorder/selftest.py` | 573 | 30,591 | frozen | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` | **yes** |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | **yes** |

All **12** `frozen` rows match the hash printed in the map, and every `wc -l` and byte count matches it too. The two `tracked` rows match as well and are reported with no expectation, as the map directs. Contract §1.4 is satisfied and no row was BLOCKED.

### 0.3 The two authorized frozen rows after the change, and the new file

| path | `wc -l` | bytes | SHA-256 |
|---|---|---|---|
| `research/pfair.py` | 275 | 12,150 | `9bd4213a60a3a25657d5ab8e507f7fc2205147b15e676cf47544a8bea8c7a8c1` |
| `research/selftest-pfair.py` | 327 | 17,060 | `ea3750df706d4375f42cb42f9d06e73268225f1eb79e216185329ca169d73da6` |
| `research/tz07a-variance-time.py` | 636 | 29,039 | `18c259523ee0b7ca60ec70dd6a5cbe401a2bb71420ccdfa1f0ff517c9e242cb4` |

`research/tz07a-variance-time.py` is new and carries no prior hash. The other two are the rows the TZ header authorizes, **additively**; §6.1 states exactly what moved in each.

### 0.4 The host gate

| check | required | observed | verdict |
|---|---|---|---|
| `/var/lib/btc-recorder/` | exists, holds interval directories | exists; `btc-updown-5m/` held **664** interval directories when the gate was performed at 17:08Z and **666** by the determinism runs at 17:17Z, the capture gaining one every 300 s | **pass** |
| the recorder process | running, newest `runtime.jsonl` start record carries sha `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` | pid `228592`, started 2026-09-12 09:53:04Z; newest `runtime.jsonl` is `1789232100/runtime.jsonl`, whose start record is `recv_ns` `1789206785264516934`, `sha` `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` | **pass** |
| the filesystem holding that path | device `/dev/vda2`, total exactly `31,612,203,008` bytes | `/dev/vda2`, total `31,612,203,008` bytes (`findmnt -bno SOURCE,SIZE`) | **pass** |

**Model.** TZ-07a names **Opus**. This session runs Opus 5 and executed the whole task.

---

## 1. Input

Everything read is the live capture under `/var/lib/btc-recorder/btc-updown-5m/`. **Nothing was re-collected and nothing was written, moved or deleted under that path** — the instrument has no filesystem write path at all; its only outputs are stdout. Scratch and outputs live under `/root/tz07-work/`, outside the repository.

| item | value |
|---|---|
| member set | TZ-06 §4's five conditions, **re-derived** by calling `tz06-calibration.scoring_set`; never transcribed |
| units considered | 443 |
| members | **400** |
| first / last member `T0` | `1789035000` / `1789166400` |
| observed Up rate over the 400 | 0.4800 |
| `Brier(c)`, the constant | 0.249600 |
| streams read | `chainlink` (merged, §3) and `twap60` (`K` alone), through `analyze.reports` — the only stream reader |
| grid | `pfair.second_grid` over `[T0 - 300, T0 + 300]`, 601 points per member |
| `gamma.json` | 400 of 400 members, read by the §6 key list alone |
| **`quotes.jsonl.gz`** | **not opened.** The string `quote` does not appear in `tz07a-variance-time.py` |
| dependencies | Python 3.12.3, standard library only |

The set matches TZ-07a §3's declared span exactly: `T0` `1789035000` … `1789166400`, 400 members out of 443 units considered.

---

## 2. Measurements

### 2.1 M1 — the variance–time curve, V1

Pooled over every overlapping increment of all 400 members, on the one-second grid of the merged `chainlink` step function over `[T0 - 300, T0 + 300]`. `sigma_h_squared = sum(dP^2) / (N_h * h)` and `g(h) = sigma_h_squared / sigma_1_squared`.

| `h` (s) | increments taken | dropped | possible | `sigma_h^2` (USD²/s) | **`g(h)` pooled** | `g(h)` median of members |
|---|---|---|---|---|---|---|
| 1 | 239,839 | 161 | 240,000 | 20.3113 | **1.000000** | 1.000000 |
| 2 | 239,426 | 174 | 239,600 | 25.9305 | **1.276654** | 1.273178 |
| 5 | 238,187 | 213 | 238,400 | 32.7179 | **1.610822** | 1.595898 |
| 10 | 236,125 | 275 | 236,400 | 36.9369 | **1.818539** | 1.836705 |
| 20 | 232,020 | 380 | 232,400 | 39.7307 | **1.956092** | 1.993967 |
| 30 | 227,920 | 480 | 228,400 | 39.6174 | **1.950510** | 2.005850 |
| 50 | 219,720 | 680 | 220,400 | 39.5443 | **1.946911** | 2.038734 |
| 60 | 215,620 | 780 | 216,400 | 39.9642 | **1.967584** | 2.038012 |
| 80 | 207,456 | 944 | 208,400 | 41.8787 | **2.061844** | 1.994456 |
| 100 | 199,385 | 1015 | 200,400 | 42.5005 | **2.092458** | 1.940795 |
| 140 | 183,303 | 1097 | 184,400 | 43.3587 | **2.134709** | 1.851507 |
| 180 | 167,255 | 1145 | 168,400 | 44.177 | **2.174995** | 1.710275 |
| 200 | 159,255 | 1145 | 160,400 | 44.3395 | **2.182997** | 1.599127 |
| 240 | 143,255 | 1145 | 144,400 | 44.6444 | **2.198011** | 1.463809 |
| 300 | 119,255 | 1145 | 120,400 | 44.7315 | **2.202299** | 1.334364 |

Every one of the 400 members contributed a ratio at every lag. The pooled column is the reading §4 freezes; the median column is §3's robustness reading and **has no role in the constants and no threshold**.

Two features of the table are stated as measured and nothing is concluded from them here. The pooled curve rises steeply to `h = 20` and is then almost flat — `1.9561` at 20 against `2.2023` at 300 — so the understatement is not a property of the long extrapolation alone; it is present in full by twenty seconds. And the two columns part company as `h` grows: at `h = 300` the pooled reading is `2.2023` and the median member's is `1.3344`. Pooling weights each member by its own variance, the median does not; the divergence is what that difference produces on this data and it is reported, not interpreted.

### 2.2 M6 — the disconnect rule, V6

| quantity | count |
|---|---|
| members whose **own** manifest records a disconnect | 0 |
| members whose **predecessor's** manifest records one | 25 |
| of those, outage falls outside `[T0 - 300, T0 + 300]` and excludes no second | 10 |
| **members contributing at least one dropped increment** | **15** |
| increments dropped, all fifteen lags | 10,779 |
| increments taken, all fifteen lags | 3,028,021 |

Per-lag drops are the third column of §2.1. The 15 members are `1789035900`, `1789043100`, `1789050300`, `1789057500`, `1789064700`, `1789071900`, `1789073100`, `1789080300`, `1789102500`, `1789128300`, `1789131600`, `1789138800`, `1789141800`, `1789149000`, `1789162500`.

This is the resolution of **System Map §7 item 16**, and the counts explain the item's own figure. TZ-06 disclosed 25 members reading their run-up from a directory that recorded a disconnect; all 25 are here. Zero members record a disconnect in their own manifest, because TZ-06 §4's first condition excludes any interval that does — so the rule bites entirely through predecessors, exactly as the defect said. Of the 25, 10 have an outage lying before `T0 - 300`: the predecessor's window opens at `T0 - 390`, so an outage in its first 90 seconds is outside this member's grid and excludes no second of it. The remaining 15 do overlap the grid, and the step function is no longer read across those gaps.

### 2.3 M2 — the correction, frozen as literals

Written into `research/pfair.py` as `G_RATIO`, to six significant digits, exactly as M1's pooled column reads them:

```python
G_RATIO = {200: D("2.18300"), 140: D("2.13471"), 80: D("2.06184"), 50: D("1.94691"),
           20: D("1.95609")}
```

| `tau` | horizon `tau - 40` | `G_RATIO` | `sqrt(G_RATIO)` — the factor on `sd` |
|---|---|---|---|
| 240 | 200 | `2.18300` | 1.477498 |
| 180 | 140 | `2.13471` | 1.461065 |
| 120 | 80 | `2.06184` | 1.435911 |
| 90 | 50 | `1.94691` | 1.395317 |
| 60 | 20 | `1.95609` | 1.398603 |
| 30 | — | exactly 1, by §4 | 1.000000 |
| 10 | — | exactly 1, by §4 | 1.000000 |

The new function is `pfair.corrected_sd(tau, sigma)`:

```
tau >= 60:   sd = sigma * sqrt((tau - 40) * G_RATIO[tau - 40])
tau <  60:   sd = sigma * sqrt(tau**3 / 10800)          # unchanged: G is exactly 1 here
```

`sigma` is `realised_sigma` over the causal window `[T0 - 300, T0 + t]`, unchanged, and `state` is untouched on both branches. The CANON §1.2 formula is not modified: only the horizon the one-second reading is carried to changes. The table is **literals, never recomputed at run time** — `tz07a-variance-time.py` asserts, per lag, that what is in `pfair.py` equals what M1 measured rounded to six significant digits, and aborts if it does not. A `tau` at or above 60 with no measured horizon raises rather than extrapolating.

### 2.4 M4 — the maker programme's published terms, V9

Read from each member's own `gamma.json` by this key list and by no other means. No price-bearing field of that document was read.

| key | result across the 400 members |
|---|---|
| `conditionId` | present in 400 |
| `slug` | present in 400 |
| `rewards` | **absent entirely in 400**, present but null in 0, non-null in **0** |
| `rewards.rewardsMinSize` | not reached: no `rewards` block exists |
| `rewards.rewardsMaxSpread` | not reached: no `rewards` block exists |
| `rewards.clobRewards[].rewardsAmount` | not reached |
| `rewards.clobRewards[].rewardsDailyRate` | not reached |
| `rewards.clobRewards[].startDate` | not reached |
| `rewards.clobRewards[].endDate` | not reached |

All 400 documents parsed and 400 of 400 carry `conditionId` and `slug`, so the documents are present and well formed; the `rewards` key is simply not in any of them. §6 of the TZ governs this case in terms: *a key that is absent is reported absent and nothing is inferred from its absence.* Accordingly this section reports the counts and stops. No threshold, no gate, no strategy conclusion, and no inference about the venue's programme from the shape of a captured document.

### 2.5 M3 — in-sample diagnostics, V7

> **Every number in this section is in-sample on the 400 members that produced the finding, and they confirm nothing.** They are printed to show the fit did what it was meant to do before the out-of-sample test is spent, and they support no claim about the corrected pricer whatsoever.

`λ̂` is §8 G3's: the maximiser of `sum( y*log Phi(z/λ) + (1-y)*log(1 - Phi(z/λ)) )` over `λ ∈ [0.5, 3.0]` by ternary search to `1e-9`, with `z = state / sd`. It carries no threshold here.

| `tau` | `Brier` uncorrected | `Brier` corrected | `Brier(c)` | eligible bins | failing bins unc. | failing bins corr. | `λ̂` unc. | `λ̂` corr. | median `sd` ratio |
|---|---|---|---|---|---|---|---|---|---|
| 240 | 0.210741 | 0.206146 | 0.249600 | 8 | 0 | 0 | 1.5220 | 1.0301 | 1.4775 |
| 180 | 0.165723 | 0.162098 | 0.249600 | 10 | 0 | 0 | 1.4155 | 0.9688 | 1.4611 |
| 120 | 0.125644 | 0.123485 | 0.249600 | 9 | 0 | 0 | 1.4139 | 0.9846 | 1.4359 |
| 90 | 0.086705 | 0.085900 | 0.249600 | 7 | 0 | 0 | 1.1260 | 0.8070 | 1.3953 |
| 60 | 0.053946 | 0.053151 | 0.249600 | 3 | 0 | 0 | 1.1368 | 0.8128 | 1.3986 |
| 30 | 0.010501 | 0.010501 | 0.249600 | 2 | 0 | 0 | 1.4027 | 1.4027 | 1.0000 |

At `tau = 30` the two columns are identical to every printed digit, which is the arithmetic consequence of `G` being exactly 1 below `tau = 60` and is asserted independently in the self-tests.

The ten fixed bins, per tau, both estimators:


**`tau = 240`, uncorrected — in sample** — n 400 · `Brier` 0.210741 · `λ̂` 1.5220 · likelihood ratio 16.389 · `chi-square` 1 d.f. p 0.0001

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| `[0.0, 0.1)` | 38 | 0.0554 | 6 | [0, 6] | yes | ok |
| `[0.1, 0.2)` | 43 | 0.1452 | 13 | [1, 13] | yes | ok |
| `[0.2, 0.3)` | 37 | 0.2538 | 10 | [3, 17] | yes | ok |
| `[0.3, 0.4)` | 41 | 0.3549 | 16 | [7, 23] | yes | ok |
| `[0.4, 0.5)` | 49 | 0.4464 | 20 | [13, 31] | yes | ok |
| `[0.5, 0.6)` | 53 | 0.5514 | 22 | [20, 38] | yes | ok |
| `[0.6, 0.7)` | 34 | 0.6548 | 23 | [15, 29] | yes | ok |
| `[0.7, 0.8)` | 39 | 0.7506 | 30 | [22, 36] | yes | ok |
| `[0.8, 0.9)` | 32 | 0.8504 | 22 | [21, 32] | yes | ok |
| `[0.9, 1.0]` | 34 | 0.9437 | 30 | [28, 34] | yes | ok |

**`tau = 240`, corrected — in sample** — n 400 · `Brier` 0.206146 · `λ̂` 1.0301 · likelihood ratio 0.059 · `chi-square` 1 d.f. p 0.8082

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| `[0.0, 0.1)` | 7 | 0.0632 | 0 | — | no | — |
| `[0.1, 0.2)` | 33 | 0.1532 | 7 | [1, 11] | yes | ok |
| `[0.2, 0.3)` | 49 | 0.2471 | 15 | [5, 20] | yes | ok |
| `[0.3, 0.4)` | 46 | 0.3499 | 16 | [8, 25] | yes | ok |
| `[0.4, 0.5)` | 73 | 0.4489 | 27 | [22, 44] | yes | ok |
| `[0.5, 0.6)` | 68 | 0.5456 | 32 | [27, 48] | yes | ok |
| `[0.6, 0.7)` | 50 | 0.6522 | 38 | [24, 41] | yes | ok |
| `[0.7, 0.8)` | 37 | 0.7449 | 25 | [20, 34] | yes | ok |
| `[0.8, 0.9)` | 30 | 0.8422 | 25 | [20, 30] | yes | ok |
| `[0.9, 1.0]` | 7 | 0.9355 | 7 | — | no | — |

**`tau = 180`, uncorrected — in sample** — n 400 · `Brier` 0.165723 · `λ̂` 1.4155 · likelihood ratio 16.802 · `chi-square` 1 d.f. p 0.0000

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| `[0.0, 0.1)` | 80 | 0.0340 | 8 | [0, 8] | yes | ok |
| `[0.1, 0.2)` | 42 | 0.1477 | 10 | [1, 13] | yes | ok |
| `[0.2, 0.3)` | 34 | 0.2498 | 7 | [3, 15] | yes | ok |
| `[0.3, 0.4)` | 40 | 0.3455 | 17 | [6, 22] | yes | ok |
| `[0.4, 0.5)` | 21 | 0.4535 | 11 | [4, 15] | yes | ok |
| `[0.5, 0.6)` | 24 | 0.5481 | 16 | [7, 19] | yes | ok |
| `[0.6, 0.7)` | 30 | 0.6456 | 15 | [12, 26] | yes | ok |
| `[0.7, 0.8)` | 19 | 0.7435 | 11 | — | no | — |
| `[0.8, 0.9)` | 33 | 0.8564 | 26 | [23, 33] | yes | ok |
| `[0.9, 1.0]` | 77 | 0.9635 | 71 | [69, 77] | yes | ok |

**`tau = 180`, corrected — in sample** — n 400 · `Brier` 0.162098 · `λ̂` 0.9688 · likelihood ratio 0.109 · `chi-square` 1 d.f. p 0.7409

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| `[0.0, 0.1)` | 42 | 0.0472 | 4 | [0, 6] | yes | ok |
| `[0.1, 0.2)` | 45 | 0.1511 | 5 | [1, 14] | yes | ok |
| `[0.2, 0.3)` | 42 | 0.2515 | 9 | [4, 18] | yes | ok |
| `[0.3, 0.4)` | 54 | 0.3552 | 17 | [10, 28] | yes | ok |
| `[0.4, 0.5)` | 34 | 0.4492 | 18 | [8, 23] | yes | ok |
| `[0.5, 0.6)` | 42 | 0.5553 | 25 | [15, 31] | yes | ok |
| `[0.6, 0.7)` | 28 | 0.6487 | 16 | [11, 24] | yes | ok |
| `[0.7, 0.8)` | 32 | 0.7578 | 24 | [18, 30] | yes | ok |
| `[0.8, 0.9)` | 42 | 0.8499 | 36 | [29, 41] | yes | ok |
| `[0.9, 1.0]` | 39 | 0.9489 | 38 | [33, 39] | yes | ok |

**`tau = 120`, uncorrected — in sample** — n 400 · `Brier` 0.125644 · `λ̂` 1.4139 · likelihood ratio 17.746 · `chi-square` 1 d.f. p 0.0000

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| `[0.0, 0.1)` | 123 | 0.0243 | 8 | [0, 8] | yes | ok |
| `[0.1, 0.2)` | 25 | 0.1419 | 4 | [0, 9] | yes | ok |
| `[0.2, 0.3)` | 28 | 0.2458 | 7 | [2, 13] | yes | ok |
| `[0.3, 0.4)` | 30 | 0.3501 | 15 | [4, 17] | yes | ok |
| `[0.4, 0.5)` | 16 | 0.4470 | 8 | — | no | — |
| `[0.5, 0.6)` | 19 | 0.5489 | 15 | — | no | — |
| `[0.6, 0.7)` | 15 | 0.6467 | 8 | — | no | — |
| `[0.7, 0.8)` | 16 | 0.7577 | 11 | — | no | — |
| `[0.8, 0.9)` | 25 | 0.8551 | 19 | [16, 25] | yes | ok |
| `[0.9, 1.0]` | 103 | 0.9784 | 97 | [96, 103] | yes | ok |

**`tau = 120`, corrected — in sample** — n 400 · `Brier` 0.123485 · `λ̂` 0.9846 · likelihood ratio 0.030 · `chi-square` 1 d.f. p 0.8629

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| `[0.0, 0.1)` | 88 | 0.0326 | 4 | [0, 8] | yes | ok |
| `[0.1, 0.2)` | 41 | 0.1562 | 5 | [1, 13] | yes | ok |
| `[0.2, 0.3)` | 26 | 0.2510 | 6 | [1, 13] | yes | ok |
| `[0.3, 0.4)` | 40 | 0.3513 | 13 | [7, 22] | yes | ok |
| `[0.4, 0.5)` | 27 | 0.4444 | 14 | [6, 19] | yes | ok |
| `[0.5, 0.6)` | 27 | 0.5497 | 20 | [8, 21] | yes | ok |
| `[0.6, 0.7)` | 19 | 0.6589 | 11 | — | no | — |
| `[0.7, 0.8)` | 24 | 0.7526 | 17 | [12, 23] | yes | ok |
| `[0.8, 0.9)` | 32 | 0.8490 | 28 | [21, 32] | yes | ok |
| `[0.9, 1.0]` | 76 | 0.9671 | 74 | [69, 76] | yes | ok |

**`tau = 90`, uncorrected — in sample** — n 400 · `Brier` 0.086705 · `λ̂` 1.1260 · likelihood ratio 1.434 · `chi-square` 1 d.f. p 0.2311

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| `[0.0, 0.1)` | 148 | 0.0157 | 3 | [0, 7] | yes | ok |
| `[0.1, 0.2)` | 26 | 0.1428 | 9 | [0, 9] | yes | ok |
| `[0.2, 0.3)` | 21 | 0.2499 | 6 | [1, 11] | yes | ok |
| `[0.3, 0.4)` | 13 | 0.3337 | 6 | — | no | — |
| `[0.4, 0.5)` | 13 | 0.4495 | 8 | — | no | — |
| `[0.5, 0.6)` | 11 | 0.5611 | 8 | — | no | — |
| `[0.6, 0.7)` | 21 | 0.6507 | 14 | [8, 19] | yes | ok |
| `[0.7, 0.8)` | 15 | 0.7459 | 11 | — | no | — |
| `[0.8, 0.9)` | 16 | 0.8563 | 12 | — | no | — |
| `[0.9, 1.0]` | 116 | 0.9816 | 115 | [109, 116] | yes | ok |

**`tau = 90`, corrected — in sample** — n 400 · `Brier` 0.085900 · `λ̂` 0.8070 · likelihood ratio 4.266 · `chi-square` 1 d.f. p 0.0389

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| `[0.0, 0.1)` | 122 | 0.0220 | 1 | [0, 8] | yes | ok |
| `[0.1, 0.2)` | 33 | 0.1488 | 3 | [1, 11] | yes | ok |
| `[0.2, 0.3)` | 24 | 0.2435 | 9 | [1, 12] | yes | ok |
| `[0.3, 0.4)` | 27 | 0.3438 | 10 | [3, 16] | yes | ok |
| `[0.4, 0.5)` | 15 | 0.4564 | 9 | — | no | — |
| `[0.5, 0.6)` | 19 | 0.5608 | 12 | — | no | — |
| `[0.6, 0.7)` | 23 | 0.6430 | 17 | [9, 20] | yes | ok |
| `[0.7, 0.8)` | 17 | 0.7533 | 14 | — | no | — |
| `[0.8, 0.9)` | 28 | 0.8459 | 25 | [18, 28] | yes | ok |
| `[0.9, 1.0]` | 92 | 0.9803 | 92 | [86, 92] | yes | ok |

**`tau = 60`, uncorrected — in sample** — n 400 · `Brier` 0.053946 · `λ̂` 1.1368 · likelihood ratio 1.150 · `chi-square` 1 d.f. p 0.2835

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| `[0.0, 0.1)` | 174 | 0.0087 | 1 | [0, 5] | yes | ok |
| `[0.1, 0.2)` | 14 | 0.1407 | 4 | — | no | — |
| `[0.2, 0.3)` | 15 | 0.2442 | 8 | — | no | — |
| `[0.3, 0.4)` | 7 | 0.3430 | 2 | — | no | — |
| `[0.4, 0.5)` | 10 | 0.4496 | 6 | — | no | — |
| `[0.5, 0.6)` | 6 | 0.5380 | 4 | — | no | — |
| `[0.6, 0.7)` | 9 | 0.6537 | 8 | — | no | — |
| `[0.7, 0.8)` | 7 | 0.7522 | 6 | — | no | — |
| `[0.8, 0.9)` | 16 | 0.8353 | 12 | — | no | — |
| `[0.9, 1.0]` | 142 | 0.9928 | 141 | [138, 142] | yes | ok |

**`tau = 60`, corrected — in sample** — n 400 · `Brier` 0.053151 · `λ̂` 0.8128 · likelihood ratio 2.827 · `chi-square` 1 d.f. p 0.0927

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| `[0.0, 0.1)` | 159 | 0.0117 | 0 | [0, 6] | yes | ok |
| `[0.1, 0.2)` | 21 | 0.1618 | 2 | [0, 8] | yes | ok |
| `[0.2, 0.3)` | 12 | 0.2559 | 5 | — | no | — |
| `[0.3, 0.4)` | 16 | 0.3366 | 8 | — | no | — |
| `[0.4, 0.5)` | 12 | 0.4552 | 6 | — | no | — |
| `[0.5, 0.6)` | 7 | 0.5343 | 5 | — | no | — |
| `[0.6, 0.7)` | 14 | 0.6438 | 12 | — | no | — |
| `[0.7, 0.8)` | 16 | 0.7519 | 13 | — | no | — |
| `[0.8, 0.9)` | 11 | 0.8599 | 10 | — | no | — |
| `[0.9, 1.0]` | 132 | 0.9864 | 131 | [126, 132] | yes | ok |

**`tau = 30`, uncorrected — in sample** — n 400 · `Brier` 0.010501 · `λ̂` 1.4027 · likelihood ratio 4.325 · `chi-square` 1 d.f. p 0.0376

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| `[0.0, 0.1)` | 200 | 0.0025 | 1 | [0, 3] | yes | ok |
| `[0.1, 0.2)` | 3 | 0.1371 | 0 | — | no | — |
| `[0.2, 0.3)` | 2 | 0.2629 | 0 | — | no | — |
| `[0.3, 0.4)` | 2 | 0.3869 | 1 | — | no | — |
| `[0.4, 0.5)` | 2 | 0.4107 | 1 | — | no | — |
| `[0.5, 0.6)` | 3 | 0.5659 | 1 | — | no | — |
| `[0.6, 0.7)` | 4 | 0.6326 | 4 | — | no | — |
| `[0.7, 0.8)` | 7 | 0.7485 | 7 | — | no | — |
| `[0.8, 0.9)` | 5 | 0.8816 | 5 | — | no | — |
| `[0.9, 1.0]` | 172 | 0.9976 | 172 | [169, 172] | yes | ok |

**`tau = 30`, corrected — in sample** — n 400 · `Brier` 0.010501 · `λ̂` 1.4027 · likelihood ratio 4.325 · `chi-square` 1 d.f. p 0.0376

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| `[0.0, 0.1)` | 200 | 0.0025 | 1 | [0, 3] | yes | ok |
| `[0.1, 0.2)` | 3 | 0.1371 | 0 | — | no | — |
| `[0.2, 0.3)` | 2 | 0.2629 | 0 | — | no | — |
| `[0.3, 0.4)` | 2 | 0.3869 | 1 | — | no | — |
| `[0.4, 0.5)` | 2 | 0.4107 | 1 | — | no | — |
| `[0.5, 0.6)` | 3 | 0.5659 | 1 | — | no | — |
| `[0.6, 0.7)` | 4 | 0.6326 | 4 | — | no | — |
| `[0.7, 0.8)` | 7 | 0.7485 | 7 | — | no | — |
| `[0.8, 0.9)` | 5 | 0.8816 | 5 | — | no | — |
| `[0.9, 1.0]` | 172 | 0.9976 | 172 | [169, 172] | yes | ok |

### 2.6 V8 — how much test data exists

| quantity | value |
|---|---|
| interval directories on disk with `T0 > 1789166400` | **223** |
| first / last such `T0` | `1789166700` / `1789233300` |
| of those, satisfying TZ-06 §4's five conditions | **201** |
| required by §8 for TZ-08 | 400 |
| short by | **199** |

| reason for non-qualification | count |
|---|---|
| `disconnect` | 20 |
| `no manifest+no S7 document` | 2 |

This is the count at the moment of the run, on a capture that is still growing at one interval every 300 seconds. §8 requires 400 qualifying intervals and forbids shrinking the set, so **TZ-08 cannot be issued yet**: at the observed qualification rate the remaining 199 intervals are on the order of a day of further capture. The figure is reported so the Architect does not have to ask; the decision is not this TZ's.

---

## 3. Publication

| item | value |
|---|---|
| branch | `tz-07a-variance-time`, cut from `main` at `fed99e4` |
| implementation commit | `c44af687203d14d5d485d4297c04cfb827096af9` |
| files in the commit | `research/tz07a-variance-time.py` (new), `research/pfair.py`, `research/selftest-pfair.py` |
| pull request | https://github.com/seahomebatumi-ai/btc-5m-twap/pull/7 |
| Release asset | **none.** TZ-07a produces no dataset and requires no upload. |

The report is committed straight to `main` and the implementation is not. Contract §4.2, run before finishing, pasted verbatim:

```
$ git rev-list origin/main | grep -c c44af687203d14d5d485d4297c04cfb827096af9
0

$ git diff --name-only origin/main origin/tz-07a-variance-time
research/pfair.py
research/selftest-pfair.py
research/tz07a-variance-time.py

$ git ls-tree -r --name-only origin/main | grep -E "\.parquet|\.zip"
(no output)
```

The first line prints `0`: the implementation commit is not an ancestor of `origin/main`. The second lists the three implementation files and nothing else. The third prints nothing: no dataset or archive is in git history.

---

## 4. Gate

**TZ-07a fixes a gate; it does not face one.** §7 makes V1, V2, V3 and V4 pass-or-BLOCKED conditions, and §8 fixes the gate TZ-08 will face. There is no threshold anywhere in this TZ against which this run's measurements are scored, and none is invented here.

| §7 condition | rule, quoted | deciding number | verdict |
|---|---|---|---|
| V1 | *the curve* — `g(h)` at all fifteen lags, pooled and median, with `N_h` taken and dropped, and the member count | 15 lags reported, 400 members, 3,028,021 increments taken, 10,779 dropped | **PASS** |
| V2 | *causality of the corrected pricer* — 120 of 120 bit-identical, plus the negative control 120 of 120 | **120 of 120** and **120 of 120** | **PASS** |
| V3 | *determinism* — two full runs, every output byte-identical, by `cmp` | byte-identical, `cmp` silent | **PASS** |
| V4 | *regression* — `tz06-calibration.py` unmodified, reproducing §2.8's six `Brier` values to six decimals and P at 397 of 400 | 6 of 6 `Brier` values reproduced; P **397 of 400** | **PASS** |

**The §8 gate for TZ-08 is committed to git in this branch, unchanged and unread against any number.** It fixes the set (the first 400 qualifying intervals with `T0 > 1789166400`), the scored taus, G1 discrimination, G2 shape with at most 2 failing eligible bins across the six taus, and G3 scale at `|λ̂ - 1| <= 0.15`. No threshold in it was chosen, moved or reinterpreted by this run, and §2.6 shows the intervals it will score have not happened yet.

---

## 5. Validation

Every count below is produced by the run and printed by the instrument; none is typed by hand. Where a condition is an `assert` that aborts the run, it says so.

### V1 — the curve

§2.1 in full: `g(h)` at all fifteen lags, pooled and median, `N_h` taken and dropped per lag, over **400 members**. **Asserted:** the grid is 601 points and carries no `None` at any member, and the pooled one-second variance is positive — each an `assert` that aborts.

### V2 — causality of the corrected pricer

| check | count |
|---|---|
| members × gated taus | 20 × 6 = **120** |
| corrected `p_fair`, `state` and `sd` bit-identical under perturbation of the entire future by `1.0001` | **120 of 120** |
| leaks | 0 |
| negative control — perturbing the last readable `chainlink` report moves `state`, `sd`, `p_fair` | **120 of 120** |
| the same control judged on `p_fair` alone | 108 of 120 |
| observations where `Phi` is saturated at exactly 0.0 or 1.0 | 13 |

The last two rows reconcile the middle one and are why §7 V2 judges the control on the model output as a whole. `Phi` saturates: past roughly eight sigma the double is exactly `1.0` and no perturbation can move it further, so a control judged on `p_fair` alone under-counts a reader that is genuinely read. Judged on `state`, `sd` and `p_fair` together the control moves **120 of 120**. **Recorded, not asserted:** the counts are returned and reported; the run does not abort on them.

### V3 — determinism

Two full runs of `python3 -B tz07a-variance-time.py`, back to back, compared with `cmp`:

```
run 1 start 2026-09-12T17:16:02Z epoch 1789233362
run 1 exit 0 end 2026-09-12T17:16:43Z epoch 1789233403
run 2 start 2026-09-12T17:16:43Z epoch 1789233403
run 2 exit 0 end 2026-09-12T17:17:24Z epoch 1789233444
--- cmp ---
IDENTICAL
1aab3a00b2a8617342d53d082e0f75c3c6cd50f17ac47510545715f4f22697e7  run-1.json
1aab3a00b2a8617342d53d082e0f75c3c6cd50f17ac47510545715f4f22697e7  run-2.json
```

`cmp` produced no output and exited 0: **every byte identical**. The two runs were placed inside one 300-second interval deliberately — see §6.3.

### V4 — regression

| check | expected | observed | verdict |
|---|---|---|---|
| `research/tz06-calibration.py` unmodified | `a6aaed94964775f34a9b26dba448ff0f998f32ad952e244bff834b67439ef123` | `a6aaed94964775f34a9b26dba448ff0f998f32ad952e244bff834b67439ef123` | **equal** |
| exit status | 0 | 0 | ok |
| `Brier(p_fair)` at `tau = 240` | `0.210741` | `0.210741` | **equal** |
| `Brier(p_fair)` at `tau = 180` | `0.165723` | `0.165723` | **equal** |
| `Brier(p_fair)` at `tau = 120` | `0.125644` | `0.125644` | **equal** |
| `Brier(p_fair)` at `tau = 90` | `0.086705` | `0.086705` | **equal** |
| `Brier(p_fair)` at `tau = 60` | `0.053946` | `0.053946` | **equal** |
| `Brier(p_fair)` at `tau = 30` | `0.010501` | `0.010501` | **equal** |
| P | 397 of 400 | **397 of 400** | **equal** |

The pipeline was run as a subprocess and its JSON parsed: the **observed** column is read out of that document and the hash is computed in the same pass. The **expected** column is TZ-06 §2.8's and §2.2's own printed figures, transcribed into `TZ06_BRIER` and `TZ06_P_AGREE` in the source — that is what a regression is, and it is the only place in this run where a number from a committed report is typed in. **Recorded, not asserted:** the comparison is reported as booleans and counts rather than aborting the run — a red regression here is a finding the Architect must see in full, not a stack trace.

### V5 — self-tests

| group | count | unchanged from TZ-06 |
|---|---|---|
| `V5` — the model at realistic magnitudes | **56 of 56** | yes, 56 |
| `section 3 machinery` | **18 of 18** | yes, 18 |
| `TZ-07a section 4` — new | **48 of 48** | new |
| total | **122 of 122** | |

`selftest-pfair.py` exits 0 and passes whole. **Asserted:** every one of the 122 is an `assert` that aborts the file. The two counts TZ-06 established are unchanged at 56 and 18; the new group is counted separately so neither is inflated by the other.

The new group includes both checks §7 V5 names by hand: that below `tau = 60` the corrected `sd` equals the uncorrected `sd` **exactly** — asserted at `tau` 59, 30, 10 and 1, against `near_branch` and against `state_and_sd` — and that at `tau = 60` the corrected `sd` is `sigma * sqrt(20 * G_RATIO[20])`, asserted both symbolically and against a twenty-decimal live-scale literal.

### V6 — the disconnect rule

§2.2 in full: 10,779 increments dropped in total, per lag in §2.1's third column, and **15 members** contributing at least one dropped increment, listed by `T0`. **Recorded, not asserted.**

### V7 — in-sample diagnostics

§2.5 in full, labelled in-sample in its first line, with no threshold anywhere. **Asserted:** that the `G_RATIO` literals in `pfair.py` equal M1's measurement rounded to six significant digits, per lag, and that the table's keys are exactly the five far-branch horizons — each an `assert` that aborts the run before a single diagnostic is computed.

### V8 — how much test data exists

§2.6 in full: **223** interval directories with `T0 > 1789166400`, of which **201** satisfy TZ-06 §4's five conditions, at the moment of the run. **Recorded, not asserted.**

### V9 — the maker terms

§2.4 in full, with the key list actually extracted printed there and in the source as `GAMMA_MARKET_KEYS`, `GAMMA_REWARDS_KEYS` and `GAMMA_CLOB_KEYS`. **0 of 400** members carry a non-null `rewards` block. **Recorded, not asserted.**

---

## 6. What could not be implemented as written

### 6.1 What moved in the two authorized frozen rows

`research/pfair.py` — **purely additive, 1 file changed, 42 insertions(+).** `git diff` removes no line and alters none: `realised_sigma`, `far_branch`, `near_branch`, `state_and_sd` and `p_fair` are byte-for-byte what TZ-06 scored. The addition is one block between `p_fair` and the section-3 readers: the `G_RATIO` literals and `corrected_sd`.

`research/selftest-pfair.py` — **1 file changed, 107 insertions(+), 1 deletion(-).** One existing line is replaced: `COUNTS = {"V5": 0, "machinery": 0}` becomes `COUNTS = {"V5": 0, "machinery": 0, "TZ-07a": 0}`, so the new group has a counter of its own. Every other change is an insertion — the new `tz07a_*` family, three lines added to the runner tuple, one `print`, and a paragraph in the module docstring. No existing check was edited, reordered or removed, and the V5 and machinery counts are unchanged at 56 and 18. This is disclosed rather than called purely additive because one line does change.

### 6.2 A check of mine was red while I was writing it, and I corrected the expectation

A self-test I drafted asserted that `corrected_sd(tau, 4*sigma)` equals `4*corrected_sd(tau, sigma)` **bit for bit**. It failed at `tau` 180 and 60, by a relative `4.45e-60` and `2.46e-60` — one unit in the last place of the 60-digit Decimal context. The cause is not the pricer: `(4*sigma)*sqrt(X)` rounds once where `4*(sigma*sqrt(X))` rounds twice, so linearity holds in the reals and to the width of the context, not to the last bit. `pfair.py`'s own comment on `TAU_CUBED_DIVISOR` records the same effect for the near branch. **The expectation was mine and defective, and no committed test and no product behaviour was touched**; the check now requires relative agreement inside `1e-55`, five digits looser than that ulp and forty-five tighter than any real non-linearity. It is recorded here because it happened.

### 6.3 V3's determinism and V8's moving target are in tension, and the runs were placed around it

V3 requires two full runs byte-identical. V8 requires a count of interval directories **at the moment of the run**, on a capture that gains a directory every 300 seconds and gains manifests and venue resolutions continuously. The two are satisfiable together only inside one interval, so the two runs were started at `T0 + 60` of one interval — after the previous interval's manifest is written and before the next directory appears — and both completed inside it. They are byte-identical, and §5's `cmp` block prints the start and end epoch of each so the placement is checkable. **Everything in the document other than V8 is a function of the closed 400-member set and cannot move**; V8 alone is a snapshot, and a third run in a later interval would differ in that block by design, not by non-determinism.

### 6.4 §5 points at §7 for `λ̂`, which §8 defines

§5 asks for `λ̂` *as §7 defines it*. §7 is the validation table and defines no `λ̂`; the only definition in the TZ is §8 G3's — ternary search to `1e-9` over `λ ∈ [0.5, 3.0]` maximising `sum( y*log Phi(z/λ) + (1-y)*log(1 - Phi(z/λ)) )`. That is the one implemented and the one §2.5 reports, with no threshold. Reading it any other way would require inventing a definition, which is not the Executor's to do.

### 6.5 The `rewards` block §6 expects is not in the capture

§6 states the terms are published in the Gamma market document and that the recorder has captured that document since 2026-09-10, and System Map §6 says our `gamma.json` captures hold these fields. **They do not.** All 400 documents are present and well formed and every one carries `conditionId` and `slug`, but the `rewards` key is absent entirely from all 400 — not null, not empty: not a key of the document. §6 anticipates exactly this case and rules it: an absent key is reported absent and nothing is inferred from its absence. So §2.4 reports the counts and draws nothing. **This is not a blocker** — §6 carries no threshold and no gate — but the Architect should know that the terms cannot be read out of this capture as it stands, and that whether that is the endpoint, the query or the venue is not something this TZ authorized me to investigate.

### 6.6 Everything else

Nothing else. The lag grid, the pooling rule, M6, the six-significant-digit freeze, the `G = 1` decision below `tau = 60`, V1–V9 and the §8 gate were all implemented exactly as written. No threshold was changed, no test was edited to pass, no quote was read, no price-bearing field of `gamma.json` was touched, and nothing under `/var/lib/btc-recorder/` was written, moved or deleted.
