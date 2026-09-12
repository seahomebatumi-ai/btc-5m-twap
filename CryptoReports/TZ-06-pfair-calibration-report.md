# TZ-06 — p_fair calibration against venue-resolved labels — REPORT

**Status: executed.** The §0 fingerprint gate passes, the host gate passes, the §6 precondition
**P passes 397 of 400** against a floor of 396, and the gate fixed in TZ-06 §6 before any data
was seen was therefore evaluated.

- **G1 passes at all six gated taus.** `Brier(p_fair)` is below `Brier(c)` everywhere, by
  margins from `0.039` at `tau = 240` to `0.239` at `tau = 30`.
- **G2 passes with 0 failing bins of 34 eligible**, against an allowance of 2.
- **R-c is applied and reproduces TZ-04b exactly** — 215 units considered, 200 members, 15
  non-members all `disconnect`, R1 200 of 200, R2 175, R3 181. `analyze.py` runs again.

**Phase 1 can only disqualify, and it did not.** The pricer was not caught being wrong. That is
not an edge, it is not permission to build an engine, and it says nothing about where the market
quotes. No quote was read in this execution, and the Phase 2 gate is still unwritten by anyone
who has seen a quote.

Executor model: **Opus** (`claude-opus-5`), as TZ-06's header requires.

---

## 0. Fingerprint

Read from `SYSTEM-MAP.md` at `origin/main` = `440e520`, at authoring time.

**Revision string read:** `2026-09-12-a`. TZ-06 §0 requires `2026-09-12-a`. Match.

| anchor | required by TZ-06 §0 | computed | match |
|---|---|---|---|
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` | yes |
| `A2` — collector | `6c5089330629` | `6c5089330629` | yes |
| `A3` — phase | `0-complete / 1-open / 2-not-started` | `0-complete / 1-open / 2-not-started` | yes |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b` | yes |
| `A5` — recorder | `9fd1c7de0f74` | `9fd1c7de0f74` | yes |

`A1` was not copied from the map. Before any other work the Release asset was fetched
anonymously and hashed: `76,818,669` bytes, SHA-256
`229a944f2d5111c3e68b1fa0630f8e8658356147f9669d18665e575b60f3716b`. The downloaded copy was
then deleted from scratch space. `A2`, `A4` and `A5` are the first 12 hex characters of the
SHA-256 values in the table below. `A3` was read from map §5.

### Fingerprint table

`wc -l`, bytes and `sha256sum` for `SYSTEM-MAP.md` and for every file the map's §0 table lists
at authoring time, read from `origin/main` at `440e520`.

| path | lines | bytes | state | SHA-256 | matches map |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 314 | 24,880 | reported | `83275a00e051c811c7ee186634d00b5ab01c4033302f577e0af4dfb881792768` | self-reference |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | yes |
| `research/twap-divergence.py` | 1,135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | yes |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | yes |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | yes |
| `research/recorder/recorder.py` | 608 | 25,658 | frozen | `9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03` | yes |
| `research/recorder/config.py` | 112 | 4,773 | frozen | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | yes |
| `research/recorder/manifest.py` | 254 | 10,002 | frozen | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | yes |
| `research/recorder/probe.py` | 227 | 9,324 | frozen | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | yes |
| `research/recorder/analyze.py` | 788 | 33,323 | frozen | `5bade9ff56669f2c862f81e98af1050b53233d2b07e3c260e04bf64233c03230` | yes |
| `research/recorder/selftest.py` | 516 | 27,693 | frozen | `3678c0b4f95a063c5b44c18eb13cdedc6e9adbee3afc6adab0884de615b09cbb` | yes |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | yes |

All eight `frozen` rows match the hashes printed in the map, so the contract §1.4 check passes.

### The two files §0 authorizes changing, after the change

TZ-06 §0 authorizes `research/recorder/analyze.py` and `research/recorder/selftest.py` to move
under §5 R-c and no other frozen row to move. No other frozen row moved.

| path | lines | bytes | SHA-256 after R-c |
|---|---|---|---|
| `research/recorder/analyze.py` | 813 | 34,705 | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` |
| `research/recorder/selftest.py` | 573 | 30,591 | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` |

### Host gate — the three observed values

Checked mechanically before any other work, at `2026-09-12T11:53Z`.

| check | required by TZ-06 §0 | observed | match |
|---|---|---|---|
| `/var/lib/btc-recorder/` | exists, holds interval directories | exists; **601** interval directories under `btc-updown-5m/` at the gate check, 604 by the end of the run — the recorder is live | yes |
| the recorder process | running, newest `runtime.jsonl` start record carries `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` | pid `228592`, started 2026-09-12 09:53:04Z; newest of four start records is `recv_ns` `1789206785264516934`, `sha` `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` | yes |
| the filesystem | device `/dev/vda2`, total exactly `31,612,203,008` bytes | `/dev/vda2`, `31,612,203,008` bytes | yes |

This is the capture host.

---

## 1. Input

**Nothing was re-collected and no capture was produced.** This execution is read-only over what
was already on disk. **No write of any kind was made under `/var/lib/btc-recorder/`** — the only
file this run writes is the §6 forensics CSV, at `/root/tz06-work/tz06-observations.csv`, outside
the repository.

| input | what it supplies |
|---|---|
| `/var/lib/btc-recorder/btc-updown-5m/{1789033800 … 1789166400}` | the 443 units considered: `manifest.json`, `resolution.json`, `twap60.jsonl.gz` and `chainlink.jsonl.gz` per directory |
| each member's **preceding** directory | the run-up window `[T0 - 300, T0 - 90]`, which the member's own file does not cover; §3 sends the run-up there |
| `/var/lib/btc-recorder/runtime.jsonl` | the four start records R-c reads; 5,680 lines at the time of reading, and still growing — the recorder is live |
| `origin/main` at `440e520` | the §0 fingerprint table and the TZ |

**`quotes.jsonl.gz` was not opened.** Tier C is Phase 2. The string `quotes` does not appear in
`research/pfair.py` or in `research/tz06-calibration.py`, and `quotes_complete` is read nowhere:
TZ-06 §4 excludes it as a qualifying condition and this run honours that.

**Network reads made by this execution:** one, the `A1` Release asset, anonymous and read-only.
No venue endpoint was called. No credential of any kind exists in this session.

Scratch space is `/root/tz06-work/`, outside the repository. Nothing outside `research/`,
`CryptoReports/` and `/root/tz06-work/` was created or modified.

---

## 2. Measurements

### 2.1 The scoring set — TZ-06 §4

| quantity | value |
|---|---|
| ordering | by `T0`, from the earliest interval directory on the host |
| first unit considered | `1789033800` — 2026-09-10 09:50 UTC |
| units considered | **443** |
| members | **400** — the set size §4 fixes; the set was not shrunk |
| first member | `1789035000` |
| last member | `1789166400` — 2026-09-11 22:40 UTC |
| non-members | **43** |

Counts by failure reason, over the 443 units considered:

| reason | count |
|---|---|
| `disconnect` | 41 |
| `disconnect` + `no chainlink at or before T0-300` | 2 |
| **total non-members** | **43** |

Every non-member fails §4 condition 1. The two that also fail condition 5 are the first two
units, `1789033800` and `1789034100`: the Tier A capture began at `recv_ns`
`1789033991738343639`, inside the first of them, so neither has a run-up window at all.

No unit failed conditions 2, 3 or 4: every interval whose own manifest is `complete` carried a
decided outcome, a non-null `priceToBeat`, a `twap60` report at or after its open, and chainlink
coverage of `[T0 - 300, T0 + 290]`.

The 443 units considered span **three recorder commits** — `b21c14c8` (2 units), `29470e0b`
(43) and `3895356a` (398) — and the two restarts between them. The 400 members span two:
`29470e0b` on 2 and `3895356a` on 398. Every member closed before the TZ-05a restart at
`recv_ns` `1789206785264516934`, so no member's directory carries Tier C at all. §4 permits
exactly this: anti-cherry-picking is the disclosure, never continuity.

### 2.2 P — the precondition, before any calibration score exists

The trailing 60-second average at the close, reconstructed from the `chainlink` feed alone over
`[T0 + 240, T0 + 300]` by the same machinery §3 uses for `m_r`, with its sign against `K`
compared to the venue's own resolved outcome.

| quantity | value |
|---|---|
| n | 400 |
| **agree** | **397** |
| disagree | 3 |
| agreement rate | `0.993` |
| **required by §6** | **at least 396** |
| **verdict** | **PASS** |
| agreement when the comparison is made as doubles rather than `Decimal` | 397 — the same 397 |

The three disagreements:

| T0 | open (UTC) | `m_close − K` (USD) | venue outcome |
|---|---|---|---|
| `1789046100` | 2026-09-10 13:15 | `−2.064179` | Up |
| `1789119600` | 2026-09-11 09:40 | `+0.182199` | Down |
| `1789149900` | 2026-09-11 18:05 | `−1.970169` | Up |

All three are sign errors of the reconstruction, not of the model: in each, the reconstructed
mean lands on the wrong side of `K` by less than the reconstruction's own worst residual.

**P passes, so the gate below was evaluated.** Had it failed, §6 requires the counts, no gate,
Phase 1 left open and nothing proposed.

### 2.3 V1 — set formation

The member count, the counts by failure reason and the first and last units are in §2.1. Every
unit considered is disclosed in `T0` order in **§2.11**, one row each, members and non-members
alike, with the reason for every non-member.

### 2.4 V2 — feed adequacy

Gaps between consecutive report timestamps inside `[T0 − 300, T0 + 300]`, over the 400 members.
Both streams are read as §3 merges them — the preceding interval's directory and the interval's
own — because the window opens 300 s before the open and an interval's own file starts only at
`T0 − 90`.

| stream | members | gaps measured | median gap | maximum gap | worst at | reports per member, median |
|---|---|---|---|---|---|---|
| `chainlink` | 400 | 232,924 | `1,000` ms | `34,000` ms | `1789073100` | 584 |
| `twap60` | 400 | 232,968 | `1,000` ms | `34,000` ms | `1789073100` | 584 |

Both feeds publish at 1 Hz and the median gap is exactly one second on both.

**The maximum is inherited, not the member's own.** `1789073100` has `disconnect_count = 0` and a
maximum inter-message gap of `2,466` ms inside its own directory. The 34-second hole sits in
`[T0 − 300, T0 − 90]`, which is covered only by the **preceding** directory `1789072800`, whose
manifest records one disconnect of `32,317` ms. **25 of the 400 members read their run-up window
from a directory that recorded a disconnect**; they are listed in the `results.json` under
`V2_feed_adequacy.their_T0s`. §4 does not make that a condition and the set is never shrunk, so
they are members. This is carried into §6 as an ambiguity, because §3 also says no value is
carried across a gap the manifest records as a disconnect, and for these 25 the step function
does.

**P's counts** are in §2.2. **The reconstruction residual** against the venue's own `twap60`
report at the close — the first `twap60` report at or after `T0 + 300`, the same reading TZ-04b's
R1 validated:

| quantity | USD |
|---|---|
| median absolute residual | `0.530740` |
| worst absolute residual | `11.867344` at `T0 = 1789134300` |
| median signed residual | `−0.016914` |

The signed median is essentially zero, so the reconstruction is unbiased in the middle; the
dispersion is what produces P's three sign errors. A reconstruction one step removed from the
settlement feed is allowed a 1% shortfall by §6 and used `0.75%` of it.

### 2.5 V3 — `K` reconstruction

`K` — the first `twap60` report with `timestamp >= T0 * 1000` — against the venue's published
`priceToBeat` from `resolution.json`, judged by `published_equal`.

| quantity | value |
|---|---|
| n | 400 |
| **equal at the precision the venue publishes** | **396** |
| equal as strict `Decimal` | 0 |
| median absolute residual | `3.778944e-12` USD |
| worst residual | `25.485626` USD at `T0 = 1789134600` |

No threshold is attached. This extends TZ-04b's 198 of 200 to **396 of 400** — the same rate, on
twice the set. The strict-`Decimal` count of 0 is expected and is the reason `published_equal`
exists: the oracle carries a 23-digit integer scaled by `1e18` and the venue serialises a double.

### 2.6 V4 — causality by perturbation

The first 20 members, every scored tau, 140 comparisons. Every `chainlink` and `twap60` report
timestamped **after** the checkpoint instant `T0 + t` is multiplied by `1.0001` — a ten-dollar
move at BTC scale, the order of the interval's own moves.

| check | count |
|---|---|
| **`p_fair` bit-identical under perturbation of the entire future** | **140 of 140** |
| leaks | **0** |
| negative control — the last readable `chainlink` report perturbed, model output moved | **140 of 140** |
| negative control — the `K` report perturbed, model output moved | **140 of 140** |
| negative control — the last readable `chainlink` report perturbed, `p_fair` moved | 110 of 140 |
| negative control — the `K` report perturbed, `p_fair` moved | 112 of 140 |
| observations whose `p_fair` is already exactly `0.0` or `1.0` as a double | 31 of 140 |

The two `p_fair` control counts are below 140 for one reason, and it is reported rather than
worked around: **`Phi` saturates.** Once `state / sd` passes about 8, `math.erf` returns exactly
`±1.0` and `p_fair` is exactly `0.0` or `1.0`; no perturbation of any magnitude can then move it.
All 30 controls that left `p_fair` unmoved are saturated observations, all 30 moved `state`, and
the one saturated observation that did move `p_fair` moved off saturation. Judged on the model's
output as a whole — `state`, `sd`, `p_fair` — both controls are **140 of 140**, so the reader is
proved to be read.

Saturation is not confined to the 20 V4 members. Over the whole scored set it is `0` at
`tau ∈ {240, 180, 120}`, `4` at `tau = 90`, `46` at `tau = 60`, `227` at `tau = 30` and `365` at
`tau = 10`, out of 400 each. Near the close the model is almost always certain.

### 2.7 V5 — the model at realistic magnitudes

`research/selftest-pfair.py`, run by the pipeline and counted from its output, never transcribed.
Every check is an `assert` that aborts the run, and every fixed expectation is taken at `K` near
`100,000`; none is taken at 0.

| family | checks | result |
|---|---|---|
| the branches agree at `tau = 60` | 10 | pass |
| at `tau >= 60` the realised path has zero weight | 20 | pass |
| at `tau < 60` the realised mean enters with weight `(60 − tau) / 60` | 17 | pass |
| `p_fair` moves the right way in `state` and in `sigma` | 9 | pass |
| **V5 total** | **56 of 56** | **pass** |
| §3 machinery — the step-function mean, the one-second grid, the sigma estimator, the merge | 18 of 18 | pass |

The two counts are kept apart on purpose: the second set is not V5 and does not inflate it.

### 2.8 V6 — calibration, `sigma_live` — the gate's table

Predictions are `p_fair` computed with `sigma_live`. The constant `c` is the observed Up rate
over the 400 members, **`c = 0.48`**, giving `Brier(c) = 0.249600`. The ten bins are the fixed
`[0, 0.1), [0.1, 0.2), … [0.9, 1.0]` of §6; a bin is eligible at `n >= 20`; a bin fails when its
observed Up count falls outside the central 99% region of `Binomial(n, p̄)`, computed exactly in
integer arithmetic and never by a normal approximation.


**`tau = 240`** — n 400 · observed Up rate 0.4800 · `Brier(p_fair)` **0.210741** · `Brier(c)` 0.249600 · eligible bins 10 · failing bins **0** · saturated predictions 0

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

**`tau = 180`** — n 400 · observed Up rate 0.4800 · `Brier(p_fair)` **0.165723** · `Brier(c)` 0.249600 · eligible bins 9 · failing bins **0** · saturated predictions 0

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

**`tau = 120`** — n 400 · observed Up rate 0.4800 · `Brier(p_fair)` **0.125644** · `Brier(c)` 0.249600 · eligible bins 6 · failing bins **0** · saturated predictions 0

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

**`tau = 90`** — n 400 · observed Up rate 0.4800 · `Brier(p_fair)` **0.086705** · `Brier(c)` 0.249600 · eligible bins 5 · failing bins **0** · saturated predictions 4

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

**`tau = 60`** — n 400 · observed Up rate 0.4800 · `Brier(p_fair)` **0.053946** · `Brier(c)` 0.249600 · eligible bins 2 · failing bins **0** · saturated predictions 46

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

**`tau = 30`** — n 400 · observed Up rate 0.4800 · `Brier(p_fair)` **0.010501** · `Brier(c)` 0.249600 · eligible bins 2 · failing bins **0** · saturated predictions 227

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

### 2.9 V7 — `tau = 10`, measured, no threshold attached

**`tau = 10`** — n 400 · observed Up rate 0.4800 · `Brier(p_fair)` 0.005719 · `Brier(c)` 0.249600 · eligible bins 2 · failing bins 0 · saturated predictions 365

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| `[0.0, 0.1)` | 208 | 0.0006 | 1 | [0, 2] | yes | ok |
| `[0.1, 0.2)` | 0 | — | 0 | — | no | — |
| `[0.2, 0.3)` | 0 | — | 0 | — | no | — |
| `[0.3, 0.4)` | 0 | — | 0 | — | no | — |
| `[0.4, 0.5)` | 1 | 0.4012 | 1 | — | no | — |
| `[0.5, 0.6)` | 1 | 0.5758 | 1 | — | no | — |
| `[0.6, 0.7)` | 1 | 0.6279 | 1 | — | no | — |
| `[0.7, 0.8)` | 2 | 0.7507 | 1 | — | no | — |
| `[0.8, 0.9)` | 2 | 0.8343 | 2 | — | no | — |
| `[0.9, 1.0]` | 185 | 0.9990 | 185 | [183, 185] | yes | ok |

`tau = 10` is the sharpest table in the set and it decides nothing: §6 attaches no threshold to
it and this report attaches none either.

### 2.10 V8 — `sigma_pre`, reported alongside, deciding nothing

The gate reads `sigma_live` only. `sigma_pre` is reported here and **cannot rescue or condemn
anything** — §6 fixed that before any data was seen, precisely so that gating on whichever
variant scored better could not happen.

The `eligible bins` and `failing bins` columns are `sigma_pre`'s; `Brier(sigma_live)` is carried
across from §2.8 and §2.9 for comparison only.

| tau | `Brier(sigma_pre)` | `Brier(sigma_live)` | `Brier(c)` | eligible bins (`sigma_pre`) | failing bins (`sigma_pre`) |
|---|---|---|---|---|---|
| 240 | 0.211062 | 0.210741 | 0.249600 | 10 | **1** |
| 180 | 0.165488 | 0.165723 | 0.249600 | 9 | **1** |
| 120 | 0.125905 | 0.125644 | 0.249600 | 9 | **1** |
| 90 | 0.089283 | 0.086705 | 0.249600 | 4 | 0 |
| 60 | 0.055037 | 0.053946 | 0.249600 | 2 | 0 |
| 30 | 0.010649 | 0.010501 | 0.249600 | 2 | 0 |
| 10 | 0.005720 | 0.005719 | 0.249600 | 2 | 0 |

Its three failing eligible bins, all in `[0, 0.1)`, all at the three longest taus:

| tau | bin | n | mean prediction | observed Up | central 99% region |
|---|---|---|---|---|---|
| 240 | `[0.0, 0.1)` | 39 | 0.0448 | 7 | [0, 6] |
| 180 | `[0.0, 0.1)` | 78 | 0.0278 | 8 | [0, 7] |
| 120 | `[0.0, 0.1)` | 121 | 0.0206 | 8 | [0, 7] |

**Recorded, and it changes nothing.** Had the gate read `sigma_pre`, G2 would have counted 3
failing bins against an allowance of 2 and Phase 1 would have answered no. It does not read
`sigma_pre`. The decision was fixed in the TZ before the data existed; noting after the fact
that the other variant would have failed is an observation about the variant, not a margin the
gate earned. Every `sigma_pre` Brier still beats the constant.

### 2.11 V1 — ordered disclosure, every unit considered

443 rows, in `T0` order, from the earliest interval directory on the host through the 400th
member. `member` is the member's index in the set; `—` means it is not one.

| # | T0 | open (UTC) | member | reason not a member |
|---|---|---|---|---|
| 1 | 1789033800 | 2026-09-10 09:50 | — | disconnect + no chainlink at or before T0-300 |
| 2 | 1789034100 | 2026-09-10 09:55 | — | disconnect + no chainlink at or before T0-300 |
| 3 | 1789034400 | 2026-09-10 10:00 | — | disconnect |
| 4 | 1789034700 | 2026-09-10 10:05 | — | disconnect |
| 5 | 1789035000 | 2026-09-10 10:10 | 1 | — |
| 6 | 1789035300 | 2026-09-10 10:15 | 2 | — |
| 7 | 1789035600 | 2026-09-10 10:20 | — | disconnect |
| 8 | 1789035900 | 2026-09-10 10:25 | 3 | — |
| 9 | 1789036200 | 2026-09-10 10:30 | 4 | — |
| 10 | 1789036500 | 2026-09-10 10:35 | 5 | — |
| 11 | 1789036800 | 2026-09-10 10:40 | 6 | — |
| 12 | 1789037100 | 2026-09-10 10:45 | 7 | — |
| 13 | 1789037400 | 2026-09-10 10:50 | 8 | — |
| 14 | 1789037700 | 2026-09-10 10:55 | 9 | — |
| 15 | 1789038000 | 2026-09-10 11:00 | 10 | — |
| 16 | 1789038300 | 2026-09-10 11:05 | 11 | — |
| 17 | 1789038600 | 2026-09-10 11:10 | 12 | — |
| 18 | 1789038900 | 2026-09-10 11:15 | 13 | — |
| 19 | 1789039200 | 2026-09-10 11:20 | 14 | — |
| 20 | 1789039500 | 2026-09-10 11:25 | 15 | — |
| 21 | 1789039800 | 2026-09-10 11:30 | 16 | — |
| 22 | 1789040100 | 2026-09-10 11:35 | 17 | — |
| 23 | 1789040400 | 2026-09-10 11:40 | 18 | — |
| 24 | 1789040700 | 2026-09-10 11:45 | 19 | — |
| 25 | 1789041000 | 2026-09-10 11:50 | 20 | — |
| 26 | 1789041300 | 2026-09-10 11:55 | 21 | — |
| 27 | 1789041600 | 2026-09-10 12:00 | 22 | — |
| 28 | 1789041900 | 2026-09-10 12:05 | 23 | — |
| 29 | 1789042200 | 2026-09-10 12:10 | 24 | — |
| 30 | 1789042500 | 2026-09-10 12:15 | 25 | — |
| 31 | 1789042800 | 2026-09-10 12:20 | — | disconnect |
| 32 | 1789043100 | 2026-09-10 12:25 | 26 | — |
| 33 | 1789043400 | 2026-09-10 12:30 | 27 | — |
| 34 | 1789043700 | 2026-09-10 12:35 | 28 | — |
| 35 | 1789044000 | 2026-09-10 12:40 | 29 | — |
| 36 | 1789044300 | 2026-09-10 12:45 | 30 | — |
| 37 | 1789044600 | 2026-09-10 12:50 | 31 | — |
| 38 | 1789044900 | 2026-09-10 12:55 | 32 | — |
| 39 | 1789045200 | 2026-09-10 13:00 | 33 | — |
| 40 | 1789045500 | 2026-09-10 13:05 | 34 | — |
| 41 | 1789045800 | 2026-09-10 13:10 | 35 | — |
| 42 | 1789046100 | 2026-09-10 13:15 | 36 | — |
| 43 | 1789046400 | 2026-09-10 13:20 | 37 | — |
| 44 | 1789046700 | 2026-09-10 13:25 | 38 | — |
| 45 | 1789047000 | 2026-09-10 13:30 | 39 | — |
| 46 | 1789047300 | 2026-09-10 13:35 | 40 | — |
| 47 | 1789047600 | 2026-09-10 13:40 | 41 | — |
| 48 | 1789047900 | 2026-09-10 13:45 | 42 | — |
| 49 | 1789048200 | 2026-09-10 13:50 | 43 | — |
| 50 | 1789048500 | 2026-09-10 13:55 | 44 | — |
| 51 | 1789048800 | 2026-09-10 14:00 | 45 | — |
| 52 | 1789049100 | 2026-09-10 14:05 | 46 | — |
| 53 | 1789049400 | 2026-09-10 14:10 | 47 | — |
| 54 | 1789049700 | 2026-09-10 14:15 | 48 | — |
| 55 | 1789050000 | 2026-09-10 14:20 | — | disconnect |
| 56 | 1789050300 | 2026-09-10 14:25 | 49 | — |
| 57 | 1789050600 | 2026-09-10 14:30 | 50 | — |
| 58 | 1789050900 | 2026-09-10 14:35 | 51 | — |
| 59 | 1789051200 | 2026-09-10 14:40 | 52 | — |
| 60 | 1789051500 | 2026-09-10 14:45 | 53 | — |
| 61 | 1789051800 | 2026-09-10 14:50 | 54 | — |
| 62 | 1789052100 | 2026-09-10 14:55 | 55 | — |
| 63 | 1789052400 | 2026-09-10 15:00 | 56 | — |
| 64 | 1789052700 | 2026-09-10 15:05 | 57 | — |
| 65 | 1789053000 | 2026-09-10 15:10 | 58 | — |
| 66 | 1789053300 | 2026-09-10 15:15 | 59 | — |
| 67 | 1789053600 | 2026-09-10 15:20 | 60 | — |
| 68 | 1789053900 | 2026-09-10 15:25 | 61 | — |
| 69 | 1789054200 | 2026-09-10 15:30 | 62 | — |
| 70 | 1789054500 | 2026-09-10 15:35 | 63 | — |
| 71 | 1789054800 | 2026-09-10 15:40 | 64 | — |
| 72 | 1789055100 | 2026-09-10 15:45 | 65 | — |
| 73 | 1789055400 | 2026-09-10 15:50 | 66 | — |
| 74 | 1789055700 | 2026-09-10 15:55 | 67 | — |
| 75 | 1789056000 | 2026-09-10 16:00 | 68 | — |
| 76 | 1789056300 | 2026-09-10 16:05 | 69 | — |
| 77 | 1789056600 | 2026-09-10 16:10 | 70 | — |
| 78 | 1789056900 | 2026-09-10 16:15 | 71 | — |
| 79 | 1789057200 | 2026-09-10 16:20 | — | disconnect |
| 80 | 1789057500 | 2026-09-10 16:25 | 72 | — |
| 81 | 1789057800 | 2026-09-10 16:30 | 73 | — |
| 82 | 1789058100 | 2026-09-10 16:35 | 74 | — |
| 83 | 1789058400 | 2026-09-10 16:40 | 75 | — |
| 84 | 1789058700 | 2026-09-10 16:45 | 76 | — |
| 85 | 1789059000 | 2026-09-10 16:50 | 77 | — |
| 86 | 1789059300 | 2026-09-10 16:55 | 78 | — |
| 87 | 1789059600 | 2026-09-10 17:00 | 79 | — |
| 88 | 1789059900 | 2026-09-10 17:05 | 80 | — |
| 89 | 1789060200 | 2026-09-10 17:10 | 81 | — |
| 90 | 1789060500 | 2026-09-10 17:15 | 82 | — |
| 91 | 1789060800 | 2026-09-10 17:20 | 83 | — |
| 92 | 1789061100 | 2026-09-10 17:25 | 84 | — |
| 93 | 1789061400 | 2026-09-10 17:30 | 85 | — |
| 94 | 1789061700 | 2026-09-10 17:35 | 86 | — |
| 95 | 1789062000 | 2026-09-10 17:40 | 87 | — |
| 96 | 1789062300 | 2026-09-10 17:45 | 88 | — |
| 97 | 1789062600 | 2026-09-10 17:50 | 89 | — |
| 98 | 1789062900 | 2026-09-10 17:55 | 90 | — |
| 99 | 1789063200 | 2026-09-10 18:00 | 91 | — |
| 100 | 1789063500 | 2026-09-10 18:05 | 92 | — |
| 101 | 1789063800 | 2026-09-10 18:10 | 93 | — |
| 102 | 1789064100 | 2026-09-10 18:15 | 94 | — |
| 103 | 1789064400 | 2026-09-10 18:20 | — | disconnect |
| 104 | 1789064700 | 2026-09-10 18:25 | 95 | — |
| 105 | 1789065000 | 2026-09-10 18:30 | 96 | — |
| 106 | 1789065300 | 2026-09-10 18:35 | 97 | — |
| 107 | 1789065600 | 2026-09-10 18:40 | 98 | — |
| 108 | 1789065900 | 2026-09-10 18:45 | 99 | — |
| 109 | 1789066200 | 2026-09-10 18:50 | 100 | — |
| 110 | 1789066500 | 2026-09-10 18:55 | 101 | — |
| 111 | 1789066800 | 2026-09-10 19:00 | 102 | — |
| 112 | 1789067100 | 2026-09-10 19:05 | 103 | — |
| 113 | 1789067400 | 2026-09-10 19:10 | 104 | — |
| 114 | 1789067700 | 2026-09-10 19:15 | 105 | — |
| 115 | 1789068000 | 2026-09-10 19:20 | 106 | — |
| 116 | 1789068300 | 2026-09-10 19:25 | 107 | — |
| 117 | 1789068600 | 2026-09-10 19:30 | 108 | — |
| 118 | 1789068900 | 2026-09-10 19:35 | 109 | — |
| 119 | 1789069200 | 2026-09-10 19:40 | 110 | — |
| 120 | 1789069500 | 2026-09-10 19:45 | 111 | — |
| 121 | 1789069800 | 2026-09-10 19:50 | 112 | — |
| 122 | 1789070100 | 2026-09-10 19:55 | 113 | — |
| 123 | 1789070400 | 2026-09-10 20:00 | 114 | — |
| 124 | 1789070700 | 2026-09-10 20:05 | 115 | — |
| 125 | 1789071000 | 2026-09-10 20:10 | 116 | — |
| 126 | 1789071300 | 2026-09-10 20:15 | 117 | — |
| 127 | 1789071600 | 2026-09-10 20:20 | — | disconnect |
| 128 | 1789071900 | 2026-09-10 20:25 | 118 | — |
| 129 | 1789072200 | 2026-09-10 20:30 | 119 | — |
| 130 | 1789072500 | 2026-09-10 20:35 | 120 | — |
| 131 | 1789072800 | 2026-09-10 20:40 | — | disconnect |
| 132 | 1789073100 | 2026-09-10 20:45 | 121 | — |
| 133 | 1789073400 | 2026-09-10 20:50 | 122 | — |
| 134 | 1789073700 | 2026-09-10 20:55 | 123 | — |
| 135 | 1789074000 | 2026-09-10 21:00 | 124 | — |
| 136 | 1789074300 | 2026-09-10 21:05 | 125 | — |
| 137 | 1789074600 | 2026-09-10 21:10 | 126 | — |
| 138 | 1789074900 | 2026-09-10 21:15 | 127 | — |
| 139 | 1789075200 | 2026-09-10 21:20 | 128 | — |
| 140 | 1789075500 | 2026-09-10 21:25 | 129 | — |
| 141 | 1789075800 | 2026-09-10 21:30 | 130 | — |
| 142 | 1789076100 | 2026-09-10 21:35 | 131 | — |
| 143 | 1789076400 | 2026-09-10 21:40 | 132 | — |
| 144 | 1789076700 | 2026-09-10 21:45 | 133 | — |
| 145 | 1789077000 | 2026-09-10 21:50 | 134 | — |
| 146 | 1789077300 | 2026-09-10 21:55 | 135 | — |
| 147 | 1789077600 | 2026-09-10 22:00 | 136 | — |
| 148 | 1789077900 | 2026-09-10 22:05 | 137 | — |
| 149 | 1789078200 | 2026-09-10 22:10 | 138 | — |
| 150 | 1789078500 | 2026-09-10 22:15 | 139 | — |
| 151 | 1789078800 | 2026-09-10 22:20 | 140 | — |
| 152 | 1789079100 | 2026-09-10 22:25 | 141 | — |
| 153 | 1789079400 | 2026-09-10 22:30 | 142 | — |
| 154 | 1789079700 | 2026-09-10 22:35 | 143 | — |
| 155 | 1789080000 | 2026-09-10 22:40 | — | disconnect |
| 156 | 1789080300 | 2026-09-10 22:45 | 144 | — |
| 157 | 1789080600 | 2026-09-10 22:50 | 145 | — |
| 158 | 1789080900 | 2026-09-10 22:55 | 146 | — |
| 159 | 1789081200 | 2026-09-10 23:00 | 147 | — |
| 160 | 1789081500 | 2026-09-10 23:05 | 148 | — |
| 161 | 1789081800 | 2026-09-10 23:10 | 149 | — |
| 162 | 1789082100 | 2026-09-10 23:15 | 150 | — |
| 163 | 1789082400 | 2026-09-10 23:20 | 151 | — |
| 164 | 1789082700 | 2026-09-10 23:25 | 152 | — |
| 165 | 1789083000 | 2026-09-10 23:30 | 153 | — |
| 166 | 1789083300 | 2026-09-10 23:35 | 154 | — |
| 167 | 1789083600 | 2026-09-10 23:40 | 155 | — |
| 168 | 1789083900 | 2026-09-10 23:45 | 156 | — |
| 169 | 1789084200 | 2026-09-10 23:50 | 157 | — |
| 170 | 1789084500 | 2026-09-10 23:55 | 158 | — |
| 171 | 1789084800 | 2026-09-11 00:00 | 159 | — |
| 172 | 1789085100 | 2026-09-11 00:05 | 160 | — |
| 173 | 1789085400 | 2026-09-11 00:10 | — | disconnect |
| 174 | 1789085700 | 2026-09-11 00:15 | — | disconnect |
| 175 | 1789086000 | 2026-09-11 00:20 | 161 | — |
| 176 | 1789086300 | 2026-09-11 00:25 | 162 | — |
| 177 | 1789086600 | 2026-09-11 00:30 | 163 | — |
| 178 | 1789086900 | 2026-09-11 00:35 | 164 | — |
| 179 | 1789087200 | 2026-09-11 00:40 | 165 | — |
| 180 | 1789087500 | 2026-09-11 00:45 | 166 | — |
| 181 | 1789087800 | 2026-09-11 00:50 | 167 | — |
| 182 | 1789088100 | 2026-09-11 00:55 | 168 | — |
| 183 | 1789088400 | 2026-09-11 01:00 | 169 | — |
| 184 | 1789088700 | 2026-09-11 01:05 | 170 | — |
| 185 | 1789089000 | 2026-09-11 01:10 | — | disconnect |
| 186 | 1789089300 | 2026-09-11 01:15 | — | disconnect |
| 187 | 1789089600 | 2026-09-11 01:20 | 171 | — |
| 188 | 1789089900 | 2026-09-11 01:25 | 172 | — |
| 189 | 1789090200 | 2026-09-11 01:30 | 173 | — |
| 190 | 1789090500 | 2026-09-11 01:35 | 174 | — |
| 191 | 1789090800 | 2026-09-11 01:40 | 175 | — |
| 192 | 1789091100 | 2026-09-11 01:45 | 176 | — |
| 193 | 1789091400 | 2026-09-11 01:50 | — | disconnect |
| 194 | 1789091700 | 2026-09-11 01:55 | — | disconnect |
| 195 | 1789092000 | 2026-09-11 02:00 | 177 | — |
| 196 | 1789092300 | 2026-09-11 02:05 | 178 | — |
| 197 | 1789092600 | 2026-09-11 02:10 | 179 | — |
| 198 | 1789092900 | 2026-09-11 02:15 | 180 | — |
| 199 | 1789093200 | 2026-09-11 02:20 | 181 | — |
| 200 | 1789093500 | 2026-09-11 02:25 | 182 | — |
| 201 | 1789093800 | 2026-09-11 02:30 | 183 | — |
| 202 | 1789094100 | 2026-09-11 02:35 | 184 | — |
| 203 | 1789094400 | 2026-09-11 02:40 | 185 | — |
| 204 | 1789094700 | 2026-09-11 02:45 | 186 | — |
| 205 | 1789095000 | 2026-09-11 02:50 | 187 | — |
| 206 | 1789095300 | 2026-09-11 02:55 | 188 | — |
| 207 | 1789095600 | 2026-09-11 03:00 | 189 | — |
| 208 | 1789095900 | 2026-09-11 03:05 | 190 | — |
| 209 | 1789096200 | 2026-09-11 03:10 | 191 | — |
| 210 | 1789096500 | 2026-09-11 03:15 | 192 | — |
| 211 | 1789096800 | 2026-09-11 03:20 | 193 | — |
| 212 | 1789097100 | 2026-09-11 03:25 | 194 | — |
| 213 | 1789097400 | 2026-09-11 03:30 | 195 | — |
| 214 | 1789097700 | 2026-09-11 03:35 | 196 | — |
| 215 | 1789098000 | 2026-09-11 03:40 | 197 | — |
| 216 | 1789098300 | 2026-09-11 03:45 | 198 | — |
| 217 | 1789098600 | 2026-09-11 03:50 | — | disconnect |
| 218 | 1789098900 | 2026-09-11 03:55 | — | disconnect |
| 219 | 1789099200 | 2026-09-11 04:00 | 199 | — |
| 220 | 1789099500 | 2026-09-11 04:05 | 200 | — |
| 221 | 1789099800 | 2026-09-11 04:10 | 201 | — |
| 222 | 1789100100 | 2026-09-11 04:15 | 202 | — |
| 223 | 1789100400 | 2026-09-11 04:20 | 203 | — |
| 224 | 1789100700 | 2026-09-11 04:25 | 204 | — |
| 225 | 1789101000 | 2026-09-11 04:30 | 205 | — |
| 226 | 1789101300 | 2026-09-11 04:35 | 206 | — |
| 227 | 1789101600 | 2026-09-11 04:40 | 207 | — |
| 228 | 1789101900 | 2026-09-11 04:45 | 208 | — |
| 229 | 1789102200 | 2026-09-11 04:50 | — | disconnect |
| 230 | 1789102500 | 2026-09-11 04:55 | 209 | — |
| 231 | 1789102800 | 2026-09-11 05:00 | 210 | — |
| 232 | 1789103100 | 2026-09-11 05:05 | 211 | — |
| 233 | 1789103400 | 2026-09-11 05:10 | 212 | — |
| 234 | 1789103700 | 2026-09-11 05:15 | 213 | — |
| 235 | 1789104000 | 2026-09-11 05:20 | 214 | — |
| 236 | 1789104300 | 2026-09-11 05:25 | 215 | — |
| 237 | 1789104600 | 2026-09-11 05:30 | 216 | — |
| 238 | 1789104900 | 2026-09-11 05:35 | 217 | — |
| 239 | 1789105200 | 2026-09-11 05:40 | 218 | — |
| 240 | 1789105500 | 2026-09-11 05:45 | 219 | — |
| 241 | 1789105800 | 2026-09-11 05:50 | 220 | — |
| 242 | 1789106100 | 2026-09-11 05:55 | 221 | — |
| 243 | 1789106400 | 2026-09-11 06:00 | 222 | — |
| 244 | 1789106700 | 2026-09-11 06:05 | 223 | — |
| 245 | 1789107000 | 2026-09-11 06:10 | 224 | — |
| 246 | 1789107300 | 2026-09-11 06:15 | — | disconnect |
| 247 | 1789107600 | 2026-09-11 06:20 | — | disconnect |
| 248 | 1789107900 | 2026-09-11 06:25 | 225 | — |
| 249 | 1789108200 | 2026-09-11 06:30 | 226 | — |
| 250 | 1789108500 | 2026-09-11 06:35 | 227 | — |
| 251 | 1789108800 | 2026-09-11 06:40 | 228 | — |
| 252 | 1789109100 | 2026-09-11 06:45 | 229 | — |
| 253 | 1789109400 | 2026-09-11 06:50 | 230 | — |
| 254 | 1789109700 | 2026-09-11 06:55 | 231 | — |
| 255 | 1789110000 | 2026-09-11 07:00 | 232 | — |
| 256 | 1789110300 | 2026-09-11 07:05 | 233 | — |
| 257 | 1789110600 | 2026-09-11 07:10 | 234 | — |
| 258 | 1789110900 | 2026-09-11 07:15 | 235 | — |
| 259 | 1789111200 | 2026-09-11 07:20 | 236 | — |
| 260 | 1789111500 | 2026-09-11 07:25 | 237 | — |
| 261 | 1789111800 | 2026-09-11 07:30 | 238 | — |
| 262 | 1789112100 | 2026-09-11 07:35 | 239 | — |
| 263 | 1789112400 | 2026-09-11 07:40 | 240 | — |
| 264 | 1789112700 | 2026-09-11 07:45 | 241 | — |
| 265 | 1789113000 | 2026-09-11 07:50 | 242 | — |
| 266 | 1789113300 | 2026-09-11 07:55 | 243 | — |
| 267 | 1789113600 | 2026-09-11 08:00 | 244 | — |
| 268 | 1789113900 | 2026-09-11 08:05 | 245 | — |
| 269 | 1789114200 | 2026-09-11 08:10 | 246 | — |
| 270 | 1789114500 | 2026-09-11 08:15 | — | disconnect |
| 271 | 1789114800 | 2026-09-11 08:20 | — | disconnect |
| 272 | 1789115100 | 2026-09-11 08:25 | 247 | — |
| 273 | 1789115400 | 2026-09-11 08:30 | 248 | — |
| 274 | 1789115700 | 2026-09-11 08:35 | 249 | — |
| 275 | 1789116000 | 2026-09-11 08:40 | 250 | — |
| 276 | 1789116300 | 2026-09-11 08:45 | 251 | — |
| 277 | 1789116600 | 2026-09-11 08:50 | 252 | — |
| 278 | 1789116900 | 2026-09-11 08:55 | 253 | — |
| 279 | 1789117200 | 2026-09-11 09:00 | 254 | — |
| 280 | 1789117500 | 2026-09-11 09:05 | 255 | — |
| 281 | 1789117800 | 2026-09-11 09:10 | 256 | — |
| 282 | 1789118100 | 2026-09-11 09:15 | 257 | — |
| 283 | 1789118400 | 2026-09-11 09:20 | 258 | — |
| 284 | 1789118700 | 2026-09-11 09:25 | 259 | — |
| 285 | 1789119000 | 2026-09-11 09:30 | 260 | — |
| 286 | 1789119300 | 2026-09-11 09:35 | 261 | — |
| 287 | 1789119600 | 2026-09-11 09:40 | 262 | — |
| 288 | 1789119900 | 2026-09-11 09:45 | 263 | — |
| 289 | 1789120200 | 2026-09-11 09:50 | 264 | — |
| 290 | 1789120500 | 2026-09-11 09:55 | 265 | — |
| 291 | 1789120800 | 2026-09-11 10:00 | 266 | — |
| 292 | 1789121100 | 2026-09-11 10:05 | 267 | — |
| 293 | 1789121400 | 2026-09-11 10:10 | 268 | — |
| 294 | 1789121700 | 2026-09-11 10:15 | — | disconnect |
| 295 | 1789122000 | 2026-09-11 10:20 | — | disconnect |
| 296 | 1789122300 | 2026-09-11 10:25 | 269 | — |
| 297 | 1789122600 | 2026-09-11 10:30 | 270 | — |
| 298 | 1789122900 | 2026-09-11 10:35 | 271 | — |
| 299 | 1789123200 | 2026-09-11 10:40 | 272 | — |
| 300 | 1789123500 | 2026-09-11 10:45 | 273 | — |
| 301 | 1789123800 | 2026-09-11 10:50 | 274 | — |
| 302 | 1789124100 | 2026-09-11 10:55 | 275 | — |
| 303 | 1789124400 | 2026-09-11 11:00 | 276 | — |
| 304 | 1789124700 | 2026-09-11 11:05 | 277 | — |
| 305 | 1789125000 | 2026-09-11 11:10 | 278 | — |
| 306 | 1789125300 | 2026-09-11 11:15 | 279 | — |
| 307 | 1789125600 | 2026-09-11 11:20 | 280 | — |
| 308 | 1789125900 | 2026-09-11 11:25 | 281 | — |
| 309 | 1789126200 | 2026-09-11 11:30 | 282 | — |
| 310 | 1789126500 | 2026-09-11 11:35 | 283 | — |
| 311 | 1789126800 | 2026-09-11 11:40 | 284 | — |
| 312 | 1789127100 | 2026-09-11 11:45 | 285 | — |
| 313 | 1789127400 | 2026-09-11 11:50 | 286 | — |
| 314 | 1789127700 | 2026-09-11 11:55 | — | disconnect |
| 315 | 1789128000 | 2026-09-11 12:00 | — | disconnect |
| 316 | 1789128300 | 2026-09-11 12:05 | 287 | — |
| 317 | 1789128600 | 2026-09-11 12:10 | 288 | — |
| 318 | 1789128900 | 2026-09-11 12:15 | 289 | — |
| 319 | 1789129200 | 2026-09-11 12:20 | 290 | — |
| 320 | 1789129500 | 2026-09-11 12:25 | 291 | — |
| 321 | 1789129800 | 2026-09-11 12:30 | 292 | — |
| 322 | 1789130100 | 2026-09-11 12:35 | 293 | — |
| 323 | 1789130400 | 2026-09-11 12:40 | 294 | — |
| 324 | 1789130700 | 2026-09-11 12:45 | — | disconnect |
| 325 | 1789131000 | 2026-09-11 12:50 | — | disconnect |
| 326 | 1789131300 | 2026-09-11 12:55 | — | disconnect |
| 327 | 1789131600 | 2026-09-11 13:00 | 295 | — |
| 328 | 1789131900 | 2026-09-11 13:05 | 296 | — |
| 329 | 1789132200 | 2026-09-11 13:10 | 297 | — |
| 330 | 1789132500 | 2026-09-11 13:15 | 298 | — |
| 331 | 1789132800 | 2026-09-11 13:20 | 299 | — |
| 332 | 1789133100 | 2026-09-11 13:25 | 300 | — |
| 333 | 1789133400 | 2026-09-11 13:30 | 301 | — |
| 334 | 1789133700 | 2026-09-11 13:35 | 302 | — |
| 335 | 1789134000 | 2026-09-11 13:40 | 303 | — |
| 336 | 1789134300 | 2026-09-11 13:45 | 304 | — |
| 337 | 1789134600 | 2026-09-11 13:50 | 305 | — |
| 338 | 1789134900 | 2026-09-11 13:55 | 306 | — |
| 339 | 1789135200 | 2026-09-11 14:00 | 307 | — |
| 340 | 1789135500 | 2026-09-11 14:05 | 308 | — |
| 341 | 1789135800 | 2026-09-11 14:10 | 309 | — |
| 342 | 1789136100 | 2026-09-11 14:15 | 310 | — |
| 343 | 1789136400 | 2026-09-11 14:20 | 311 | — |
| 344 | 1789136700 | 2026-09-11 14:25 | 312 | — |
| 345 | 1789137000 | 2026-09-11 14:30 | 313 | — |
| 346 | 1789137300 | 2026-09-11 14:35 | 314 | — |
| 347 | 1789137600 | 2026-09-11 14:40 | 315 | — |
| 348 | 1789137900 | 2026-09-11 14:45 | 316 | — |
| 349 | 1789138200 | 2026-09-11 14:50 | — | disconnect |
| 350 | 1789138500 | 2026-09-11 14:55 | — | disconnect |
| 351 | 1789138800 | 2026-09-11 15:00 | 317 | — |
| 352 | 1789139100 | 2026-09-11 15:05 | 318 | — |
| 353 | 1789139400 | 2026-09-11 15:10 | 319 | — |
| 354 | 1789139700 | 2026-09-11 15:15 | 320 | — |
| 355 | 1789140000 | 2026-09-11 15:20 | 321 | — |
| 356 | 1789140300 | 2026-09-11 15:25 | 322 | — |
| 357 | 1789140600 | 2026-09-11 15:30 | 323 | — |
| 358 | 1789140900 | 2026-09-11 15:35 | 324 | — |
| 359 | 1789141200 | 2026-09-11 15:40 | — | disconnect |
| 360 | 1789141500 | 2026-09-11 15:45 | — | disconnect |
| 361 | 1789141800 | 2026-09-11 15:50 | 325 | — |
| 362 | 1789142100 | 2026-09-11 15:55 | 326 | — |
| 363 | 1789142400 | 2026-09-11 16:00 | 327 | — |
| 364 | 1789142700 | 2026-09-11 16:05 | 328 | — |
| 365 | 1789143000 | 2026-09-11 16:10 | 329 | — |
| 366 | 1789143300 | 2026-09-11 16:15 | 330 | — |
| 367 | 1789143600 | 2026-09-11 16:20 | 331 | — |
| 368 | 1789143900 | 2026-09-11 16:25 | 332 | — |
| 369 | 1789144200 | 2026-09-11 16:30 | 333 | — |
| 370 | 1789144500 | 2026-09-11 16:35 | 334 | — |
| 371 | 1789144800 | 2026-09-11 16:40 | 335 | — |
| 372 | 1789145100 | 2026-09-11 16:45 | 336 | — |
| 373 | 1789145400 | 2026-09-11 16:50 | 337 | — |
| 374 | 1789145700 | 2026-09-11 16:55 | 338 | — |
| 375 | 1789146000 | 2026-09-11 17:00 | 339 | — |
| 376 | 1789146300 | 2026-09-11 17:05 | 340 | — |
| 377 | 1789146600 | 2026-09-11 17:10 | 341 | — |
| 378 | 1789146900 | 2026-09-11 17:15 | 342 | — |
| 379 | 1789147200 | 2026-09-11 17:20 | 343 | — |
| 380 | 1789147500 | 2026-09-11 17:25 | 344 | — |
| 381 | 1789147800 | 2026-09-11 17:30 | 345 | — |
| 382 | 1789148100 | 2026-09-11 17:35 | 346 | — |
| 383 | 1789148400 | 2026-09-11 17:40 | — | disconnect |
| 384 | 1789148700 | 2026-09-11 17:45 | — | disconnect |
| 385 | 1789149000 | 2026-09-11 17:50 | 347 | — |
| 386 | 1789149300 | 2026-09-11 17:55 | 348 | — |
| 387 | 1789149600 | 2026-09-11 18:00 | 349 | — |
| 388 | 1789149900 | 2026-09-11 18:05 | 350 | — |
| 389 | 1789150200 | 2026-09-11 18:10 | 351 | — |
| 390 | 1789150500 | 2026-09-11 18:15 | 352 | — |
| 391 | 1789150800 | 2026-09-11 18:20 | 353 | — |
| 392 | 1789151100 | 2026-09-11 18:25 | 354 | — |
| 393 | 1789151400 | 2026-09-11 18:30 | 355 | — |
| 394 | 1789151700 | 2026-09-11 18:35 | 356 | — |
| 395 | 1789152000 | 2026-09-11 18:40 | 357 | — |
| 396 | 1789152300 | 2026-09-11 18:45 | 358 | — |
| 397 | 1789152600 | 2026-09-11 18:50 | 359 | — |
| 398 | 1789152900 | 2026-09-11 18:55 | 360 | — |
| 399 | 1789153200 | 2026-09-11 19:00 | — | disconnect |
| 400 | 1789153500 | 2026-09-11 19:05 | — | disconnect |
| 401 | 1789153800 | 2026-09-11 19:10 | 361 | — |
| 402 | 1789154100 | 2026-09-11 19:15 | 362 | — |
| 403 | 1789154400 | 2026-09-11 19:20 | 363 | — |
| 404 | 1789154700 | 2026-09-11 19:25 | 364 | — |
| 405 | 1789155000 | 2026-09-11 19:30 | 365 | — |
| 406 | 1789155300 | 2026-09-11 19:35 | 366 | — |
| 407 | 1789155600 | 2026-09-11 19:40 | 367 | — |
| 408 | 1789155900 | 2026-09-11 19:45 | 368 | — |
| 409 | 1789156200 | 2026-09-11 19:50 | 369 | — |
| 410 | 1789156500 | 2026-09-11 19:55 | 370 | — |
| 411 | 1789156800 | 2026-09-11 20:00 | 371 | — |
| 412 | 1789157100 | 2026-09-11 20:05 | 372 | — |
| 413 | 1789157400 | 2026-09-11 20:10 | 373 | — |
| 414 | 1789157700 | 2026-09-11 20:15 | 374 | — |
| 415 | 1789158000 | 2026-09-11 20:20 | 375 | — |
| 416 | 1789158300 | 2026-09-11 20:25 | 376 | — |
| 417 | 1789158600 | 2026-09-11 20:30 | 377 | — |
| 418 | 1789158900 | 2026-09-11 20:35 | 378 | — |
| 419 | 1789159200 | 2026-09-11 20:40 | 379 | — |
| 420 | 1789159500 | 2026-09-11 20:45 | 380 | — |
| 421 | 1789159800 | 2026-09-11 20:50 | 381 | — |
| 422 | 1789160100 | 2026-09-11 20:55 | 382 | — |
| 423 | 1789160400 | 2026-09-11 21:00 | — | disconnect |
| 424 | 1789160700 | 2026-09-11 21:05 | — | disconnect |
| 425 | 1789161000 | 2026-09-11 21:10 | 383 | — |
| 426 | 1789161300 | 2026-09-11 21:15 | 384 | — |
| 427 | 1789161600 | 2026-09-11 21:20 | 385 | — |
| 428 | 1789161900 | 2026-09-11 21:25 | 386 | — |
| 429 | 1789162200 | 2026-09-11 21:30 | — | disconnect |
| 430 | 1789162500 | 2026-09-11 21:35 | 387 | — |
| 431 | 1789162800 | 2026-09-11 21:40 | 388 | — |
| 432 | 1789163100 | 2026-09-11 21:45 | 389 | — |
| 433 | 1789163400 | 2026-09-11 21:50 | 390 | — |
| 434 | 1789163700 | 2026-09-11 21:55 | 391 | — |
| 435 | 1789164000 | 2026-09-11 22:00 | 392 | — |
| 436 | 1789164300 | 2026-09-11 22:05 | 393 | — |
| 437 | 1789164600 | 2026-09-11 22:10 | 394 | — |
| 438 | 1789164900 | 2026-09-11 22:15 | 395 | — |
| 439 | 1789165200 | 2026-09-11 22:20 | 396 | — |
| 440 | 1789165500 | 2026-09-11 22:25 | 397 | — |
| 441 | 1789165800 | 2026-09-11 22:30 | 398 | — |
| 442 | 1789166100 | 2026-09-11 22:35 | 399 | — |
| 443 | 1789166400 | 2026-09-11 22:40 | 400 | — |

### 2.12 V9 — R-c

`research/recorder/analyze.py` was run by the pipeline; the counts below are parsed from its
output, not transcribed.

| count | TZ-04b | the repaired analyzer | reproduces |
|---|---|---|---|
| units considered | 215 | **215** | yes |
| members | 200 | **200** | yes |
| non-members | 15 | **15** | yes |
| non-member reasons | all `disconnect` | all `disconnect` — 15 of 15 | yes |
| R1 agreements | 200 of 200 | **200** | yes |
| R2 agreements | 175 of 200 | **175** | yes |
| R3 agreements | 181 of 200 | **181** | yes |

**Exact reproduction on every count §5 names.** `next_start_recv_ns` resolves to
`1789206785264516934`, the TZ-05a restart; the last member's window closes at
`1789100430` s, about 30 hours before it, so the span bound holds with room.

Two things in `analyze.py`'s wider output did move against the TZ-04b run. Both are reported as
counts and neither is corrected; neither is one of the counts §5 names.

1. **`V5_determinism` fell from 215 of 215 to 0 of 215.** Rebuilding a 2026-09-10 manifest with
   today's `manifest.py` no longer reproduces it byte-for-byte, because TZ-05a added
   `quotes_complete` and `quote_offsets_ms` to the manifest schema and those intervals were
   written before Tier C existed. Every field the old manifests do carry rebuilds **identically**
   — the diff is exactly two added keys, `quotes_complete: false` and `quote_offsets_ms: []`, and
   no changed value. This is a consequence of TZ-05a's merged schema change, not of R-c.
2. **`V4_read_only_proof` matched the same 5 lines at different line numbers.** `matching_lines`
   is 5 before and 5 after, `exit_status` 0 both times; the numbers moved because R-c lengthened
   `analyze.py` and TZ-05a lengthened `recorder.py`'s docstring.

The full JSON diff between the TZ-04b run and this one is those two items, the `V5_determinism`
hash they imply, and one added key, `start.next_start_recv_ns`. **Every measurement is
unchanged.** The committed TZ-04b report was not edited.

`research/recorder/selftest.py` passes **115 of 115**, of which **10 are new for R-c** and 105
are the pre-TZ-06 suite, unchanged and still passing.

### 2.13 V10 — determinism

Two full runs of each output, compared with `cmp`, which exits non-zero on any difference.

| output | run 1 | run 2 | identical |
|---|---|---|---|
| `results.json` | `15d0b0cfa699d11c87123807b7d8c979a34a554d8ae7e5f14f13f16172dee48d` | `15d0b0cfa699d11c87123807b7d8c979a34a554d8ae7e5f14f13f16172dee48d` | yes |
| `tz06-observations.csv` | `4e20c4fafbe60fe64c48ce1833a8da55f7fce2c0bad87e93b55ba95a2a4f85bb` | `4e20c4fafbe60fe64c48ce1833a8da55f7fce2c0bad87e93b55ba95a2a4f85bb` | yes |
| `tables.md` | `6827cd348262d1a4080a7ef75353f539585a6a211b28d7bc96567eb34ef1ebc6` | `6827cd348262d1a4080a7ef75353f539585a6a211b28d7bc96567eb34ef1ebc6` | yes |

**3 of 3 byte-identical.** No wall-clock value enters any output.

### 2.14 Forensics

| item | value |
|---|---|
| path | `/root/tz06-work/tz06-observations.csv` — outside the repository |
| lines | **2,801** — one header plus `400 × 7` scored observations |
| bytes | `843,788` |
| SHA-256 | `4e20c4fafbe60fe64c48ce1833a8da55f7fce2c0bad87e93b55ba95a2a4f85bb` |
| columns | `T0, tau, K, S_t, m_r, sigma_live, sigma_pre, state, sd, p_fair, label` |

`m_r` is empty at `tau >= 60`, where §3 gives the realised path zero weight. `sd` and `p_fair`
are the `sigma_live` figures — the ones the gate reads. The `sigma_pre` pair is re-derivable by
hand from `sigma_pre`, `tau` and `state` alone, which is why §6 names eleven columns and not
thirteen. Every `Decimal` is written at full working precision, so any single row is
reconstructible without re-running anything.

---

## 3. Publication

| item | value |
|---|---|
| branch | `tz-06-pfair-calibration` |
| implementation commit | `5ed667afd1b53f036b9f938fcce13c0d709cd77f` |
| pull request | **#6** — https://github.com/seahomebatumi-ai/btc-5m-twap/pull/6, open and unmerged |
| report | `CryptoReports/TZ-06-pfair-calibration-report.md`, straight to `main` |
| Release asset | none — TZ-06 requires none, and §2 forbids one |

Files on the branch, and only these:

| path | lines | bytes | SHA-256 |
|---|---|---|---|
| `research/pfair.py` | 233 | 9,844 | `18be5d185fee807fef9a840ab965dc42fa41c3a7a0b01b27c359afce96289676` |
| `research/selftest-pfair.py` | 221 | 10,939 | `f4b4f8287f3ebb0c9cbabaee40e87580bddab6d23ad0fe0e44aa87bc09bc3842` |
| `research/tz06-calibration.py` | 569 | 26,548 | `a6aaed94964775f34a9b26dba448ff0f998f32ad952e244bff834b67439ef123` |
| `research/recorder/analyze.py` | 813 | 34,705 | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` |
| `research/recorder/selftest.py` | 573 | 30,591 | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` |

**Merge is deployment.** Passing does not make `p_fair` live and there is nothing here to
deploy; the branch waits on the Architect's verdict.

### The §4.2 separation self-check, verbatim

```
$ git rev-list origin/main | grep -c 5ed667afd1b53f036b9f938fcce13c0d709cd77f
0

$ git diff --name-only origin/main origin/tz-06-pfair-calibration
research/pfair.py
research/recorder/analyze.py
research/recorder/selftest.py
research/selftest-pfair.py
research/tz06-calibration.py

$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
```

The first prints `0`: `main` does not carry the implementation commit. The second lists the five
implementation files and nothing else. The third prints nothing.

---

## 4. Gate

Quoted from TZ-06 §6, which fixed it before any data was seen. Scored taus
`{240, 180, 120, 90, 60, 30}`; `tau = 10` carries no threshold. The gate reads `sigma_live` only.

> **G1 — the pricer must beat a constant.** At every one of the six taus,
> `Brier(p_fair) < Brier(c)`, where `c` is the observed Up rate over the 400.

`c = 0.480`, `Brier(c) = 0.250` to three decimals — exactly, `0.2496`.

| tau | `Brier(p_fair)` | `Brier(c)` | margin | `Brier(p_fair) < Brier(c)` |
|---|---|---|---|---|
| 240 | 0.210741 | 0.249600 | 0.038859 | yes |
| 180 | 0.165723 | 0.249600 | 0.083877 | yes |
| 120 | 0.125644 | 0.249600 | 0.123956 | yes |
| 90 | 0.086705 | 0.249600 | 0.162895 | yes |
| 60 | 0.053946 | 0.249600 | 0.195654 | yes |
| 30 | 0.010501 | 0.249600 | 0.239099 | yes |

**G1: 6 of 6. PASS.** The deciding number is the worst margin, `tau = 240`: `0.039`.

> **G2 — calibration.** Fixed bins `[0, 0.1), [0.1, 0.2), … [0.9, 1.0]`. A bin is **eligible**
> when it holds at least 20 of the 400. An eligible bin **fails** when its observed Up count
> falls outside the central 99% region of `Binomial(n, p̄)`, `p̄` the mean prediction in that
> bin, computed exactly rather than by a normal approximation. **Across the six taus, at most 2
> eligible bins may fail.**

| tau | eligible bins | failing bins |
|---|---|---|
| 240 | 10 | 0 |
| 180 | 9 | 0 |
| 120 | 6 | 0 |
| 90 | 5 | 0 |
| 60 | 2 | 0 |
| 30 | 2 | 0 |
| **total** | **34** | **0** |

**G2: 0 failing bins of 34 eligible, against an allowance of 2. PASS.** The deciding number is
`0.000` failing bins.

The regions are re-derivable by hand from §2.8's tables: `p̄` is an IEEE-754 double, so it is
exactly a rational `a / b`; every binomial term is the integer `C(n, i) · a^i · (b − a)^(n − i)`
over the common denominator `b^n`, and the region is the `[lo, hi]` leaving at most `1/200` of
the mass strictly outside on each side. No rounding enters that comparison at any point.

### Verdict

| gate | rule | deciding number | result |
|---|---|---|---|
| P | at least 396 of 400 agree | `397` | **PASS** |
| G1 | `Brier(p_fair) < Brier(c)` at all six taus | worst margin `0.039` | **PASS** |
| G2 | at most 2 eligible bins fail | `0.000` failing | **PASS** |

**Phase 1 does not answer no.** Nothing was tuned to reach this: no bin edge, no set size, no tau
list and no threshold moved after TZ-06 was committed, and the one variant that would have failed
G2 — `sigma_pre` — is the one the TZ excluded from the gate in advance.

**What this does not mean.** Passing means the pricer was not caught being wrong against 400
labels the venue itself produced. It is not an edge, it is not evidence about where the market
quotes, and it licenses no engine work. Phase 2 remains the decision point and its gate is still
unwritten.

---

## 5. Validation

| check | what it returns | count | asserted? |
|---|---|---|---|
| **P** | reconstruction sign against the venue's outcome | **397 of 400**, floor 396 | recorded, and it gates §4 by the TZ's rule; the pipeline asserts only that the set is full |
| **V1** | set formation | 443 considered, **400 members**, 43 non-members, reasons in §2.1 and §2.11 | `assert full` aborts if fewer than 400 qualify |
| **V2** | feed adequacy | medians `1,000` ms, maxima `34,000` ms, both streams; P's counts; residual median `0.530740` USD, worst `11.867344` USD | recorded, not asserted |
| **V3** | `K` reconstruction | **396 of 400** equal at published precision; median `3.78e-12` USD, worst `25.485626` USD | recorded, not asserted — §6 attaches no threshold |
| **V4** | causality by perturbation | **140 of 140** bit-identical; **140 of 140** controls move the model output; 110 and 112 of 140 move `p_fair`, with 31 saturated | recorded, not asserted |
| **V5** | the model at realistic magnitudes | **56 of 56**, plus 18 of 18 machinery | every one an `assert` that aborts the run |
| **V6** | calibration, `sigma_live` | six tables, `Brier` `0.010501`–`0.210741`, 34 eligible bins, **0 failing** | recorded; `central_region` asserts its own binomial terms sum to one |
| **V7** | `tau = 10` | `Brier` `0.005719`, 2 eligible bins, 0 failing | recorded, no threshold |
| **V8** | `sigma_pre` | `Brier` `0.005720`–`0.211062`, **3 failing bins** across the six gated taus | recorded, no threshold |
| **V9** | R-c reproduction | **7 of 7** counts reproduce TZ-04b exactly; `selftest.py` **115 of 115** | `reproduces` is computed and reported; `selftest.py`'s 115 are each an `assert` |
| **V10** | determinism | **3 of 3** outputs byte-identical over two full runs | `cmp`, which exits non-zero on difference |

Where a check is *recorded, not asserted*, it is said here in plain words, as contract §7
requires. P, V6 and V10 decide the gate by the TZ's rule rather than by an in-script `assert`,
because §6 makes a red result a finding to report and not a run to abort.

---

## 6. What could not be implemented as written

Four items. None changed a formula, a threshold, a bin edge, a set size or a tau list.

1. **`tau**1.5 / (60 * sqrt(3))` is implemented as `sqrt(tau**3 / 10800)`.** The two are the
   same number — `60 * sqrt(3) = sqrt(10800)` — and the second form is used for one reason: §3
   states that the branches meet at `tau = 60`, both giving `sd = sigma * sqrt(20)`. Written as
   `sqrt(tau**3 / 10800)` that identity holds **exactly** in `Decimal`, because `216000 / 10800`
   is exactly `20`; written literally it rounds three times and lands one unit in the last place
   of the 60-digit context away from the far branch, and the V5 check "the branches agree at
   `tau = 60`" would have had to be written with a tolerance. The formula is unchanged; only its
   factoring is. `research/pfair.py` carries the identity and the reason in a comment above it.

2. **§3 and §4 pull in opposite directions for 25 of the 400 members.** §3 says no value is
   carried across a stream gap the manifest records as a disconnect. §4's five conditions make
   only the interval's **own** manifest a condition, and the run-up window `[T0 − 300, T0 − 90]`
   is covered only by the **preceding** directory, whose manifest may record a disconnect of its
   own. 25 members are in that position, the worst producing the 34-second gap in §2.4. §4 is
   mechanical and says the set is never shrunk, so they are members and the step function was
   read across those gaps. The count and the T0s are disclosed rather than acted on; resolving
   the tension is a new TZ's, not this one's.

3. **V4's negative control is reported on two measures, not one.** §6 asks for a control
   "perturbing the last readable report, which must change it". On `p_fair` alone it is 110 of
   140, because `Phi` saturates at double precision and 31 of the 140 observations already sit at
   exactly `0.0` or `1.0`. On the model's output as a whole — `state`, `sd`, `p_fair` — it is 140
   of 140. Both counts are printed, in §2.6, and the weaker one is not hidden behind the
   stronger. The perturbation factor, `1.0001`, was fixed in the code before the counts were
   seen and was not changed after them.

4. **Two figures in `analyze.py`'s wider output moved against the TZ-04b run**, neither of them a
   count §5 names: `V5_determinism` 215 → 0, caused by TZ-05a adding two keys to the manifest
   schema, and `V4_read_only_proof`'s matched line numbers, caused by two files growing. Both are
   in §2.12 as counts. §5 says any difference is a finding and not something to correct, and
   neither was corrected.

**Nothing else.** No file outside `research/`, `CryptoReports/` and `/root/tz06-work/` was
created or modified. Nothing under `/var/lib/btc-recorder/` was written, moved or deleted. The
recorder was not stopped, restarted or touched: pid `228592` on `4216c04` was running before this
execution and is running after it. **No quote was read**, no market statistic of any kind was
computed, no fee was applied to anything, and `engine/` still does not exist.
