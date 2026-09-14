# SYSTEM MAP — btc-5m-twap

**Revision 2026-09-14-a.** Written by the Architect; the Executor never edits it. This is a
**state** document: what exists right now. It holds no mission, no rules and no history.

- The CANON (Architect's project instructions, not in this repository) holds the mission, the
  fair-value model, the measured facts and the phase gates.
- `BTC-EXECUTOR-INSTRUCTIONS.md` holds how the Executor works.
- **This map never restates a CANON §1.2 formula.**

---

## 0. Fingerprint gate

Every TZ header states the required revision string and the anchors below. The Executor compares
before doing any work; a mismatch is BLOCKED.

**Revision string:** `2026-09-14-a`

| anchor | value |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-answered-no / 2-not-started` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` |
| `A6` — pricer | `cb72abb8dd8a` |

Anchors are the first 12 hex characters of the SHA-256 of the named artifact, except `A3`.
`A5` is `research/recorder/recorder.py`, the code the live capture runs. `A6` is
`research/pfair.py`, the only implementation of the model: **any TZ that scores a pricer states
`A6`, so what was scored is never in doubt.** `A6` changed at `fb5c426` when PR #8 replaced
`G_RATIO` with `SD_SCALE`: the §1.2 formulas and `state` are byte-identical inside it and only the
constant multiplying `sigma * sqrt(H(tau))` moved. `9bd4213a60a3` is the value TZ-07a and TZ-07b
were both gated against, and nothing scored under it is re-opened by this revision. **PR #9
touched no anchor:** `pfair.py` is byte-identical on both sides of `1b8e4a7`, so TZ-08a's scores
and every later score are gated against the same pricer. **PR #10 touched no anchor either:** it
added one file and changed none, so `A6` is unmoved across `f781dc3`.

### Fingerprint table

Every report states `wc -l` and `sha256sum` for each row. `frozen` rows must match the hash
printed here or the run is BLOCKED. `tracked` rows are reported with no expectation.

| path | lines | bytes | state | SHA-256 |
|---|---|---|---|---|
| `SYSTEM-MAP.md` | — | — | reported | self-reference; report the value you compute |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` |
| `research/twap-divergence.py` | 1,135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` |
| `research/pfair.py` | 281 | 12,499 | frozen | `cb72abb8dd8a460908d0b4cd50da472ddd1c72b57be35b4cf90303503d47e01f` |
| `research/selftest-pfair.py` | 306 | 15,647 | frozen | `97de9782d319c82ee6a7d81ddbd8e00d590d85ffe2daa41abe3d71ae92712c94` |
| `research/tz06-calibration.py` | 577 | 27,138 | frozen | `715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f` |
| `research/tz07a-variance-time.py` | 619 | 28,219 | frozen | `4321637751a3b847fa7e59309555b802dcc9d5ba68c7407a8ec20ab76c1b3d5e` |
| `research/tz07b-settlement-dispersion.py` | 515 | 24,926 | frozen | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` |
| `research/tz08a-out-of-sample.py` | 745 | 38,822 | frozen | `37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c` |
| `research/tz09-disk-inventory.py` | 894 | 41,004 | frozen | `b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6` |
| `research/recorder/recorder.py` | 608 | 25,658 | frozen | `9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03` |
| `research/recorder/config.py` | 112 | 4,773 | frozen | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` |
| `research/recorder/manifest.py` | 254 | 10,002 | frozen | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` |
| `research/recorder/analyze.py` | 813 | 34,705 | frozen | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` |
| `research/recorder/probe.py` | 227 | 9,324 | frozen | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` |
| `research/recorder/selftest.py` | 573 | 30,591 | frozen | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` |

Hashes are of the file as committed on `main` at revision date, verified by the Architect against
`origin/main` — not copied from a report. Changing a `frozen` row requires a TZ that authorizes
it and a new map revision. **The six recorder files are frozen because the live capture runs
them**: an unauthorized edit is a change to a running instrument. **`pfair.py` is frozen because
every score this project will ever quote comes out of it**, and `tz07a-variance-time.py`,
`tz07b-settlement-dispersion.py`, `tz08a-out-of-sample.py` and `tz09-disk-inventory.py` because a
committed measurement came out of each. `tz06-calibration.py` is frozen at its post-PR-#9 hash: it now carries `after` and
`need`, and at their defaults the run is the one TZ-06 ran.

---

## 1. Repository

`github.com/seahomebatumi-ai/btc-5m-twap` — **public**. No dataset, archive or binary has ever
entered git history; the pack is under 400 KB and stays that way.

| path | contents |
|---|---|
| `CryptoTZ/` | specifications, Architect → Boss upload |
| `CryptoReports/` | reports, Executor → straight to `main` |
| `research/` | measurement code and the pricer, Executor → branch + PR |
| `research/recorder/` | live capture and its analyzer — six files, all on `main` |
| `engine/` | live engine — **does not exist yet** |
| root | `SYSTEM-MAP.md`, `BTC-EXECUTOR-INSTRUCTIONS.md`, `.gitignore` |

**Branches: `main`, and nothing else.** `tz-09-disk-inventory` merged at `f781dc3` and was
deleted, `tz-08a-out-of-sample` at `1b8e4a7` before it, `tz-07b-settlement-dispersion` at `fb5c426` and `tz-07a-variance-time` before
that; none retained anything that is not on `main`.
The head of `main` is never a gate; commits are named where they matter.

| pull request | head | disposition |
|---|---|---|
| PR #10 | `e45f38e` | the disk inventory instrument. **Merged 2026-09-14** into `main` at `f781dc3`, branch deleted. One file added, none changed, no anchor moved. |
| PR #9 | `e2625ea` | the out-of-sample driver, and `after` / `need` on `scoring_set` and `build`. **Merged 2026-09-13** into `main` at `1b8e4a7`, branch deleted. 11 insertions and 3 deletions in `tz06-calibration.py`; `pfair.py` untouched on both sides. |
| PR #8 | `26bbb61` | `SD_SCALE`, the TZ-07b instrument and 30 self-tests; `G_RATIO` and the four checks that encoded it removed. **Merged 2026-09-13** into `main` at `fb5c426`, branch deleted. `pfair.py`: `state` untouched on both branches. |
| PR #7 | `c44af68` | `corrected_sd`, the TZ-07a instrument and 48 self-tests. **Merged 2026-09-13** into `main` at `467805e`. Purely additive to `pfair.py`: 42 insertions, no line removed or altered. |
| PR #6 | `5ed667a` | the pricer, its calibration pipeline and R-c. Merged 2026-09-12 at `4b3723a`. |
| PR #5 | `4216c04` | Tier C and the SNTP repair. Merged 2026-09-12 at `c3dab7d`. |
| PR #4 | `0e13a5c` | the TZ-05 BLOCKED report. Closed. |
| PR #3 | `ee2f632` | the recorder and its analyzer, merged after the TZ-04b verdict |
| PR #1 | `d9e58e8` | TZ-03, the rename and the two deletions |

Commits still named by an artifact: `ea9290b` — the commit the dataset tag points at; `a772d19` —
TZ-02; `3895356` — the recorder commit TZ-04b scored; `4216c04` — the commit the capture runs;
`5ed667a` — the commit that first implemented the pricer; `c44af68` — the commit that added
`corrected_sd` and the `G_RATIO` literals; `26bbb61` — the commit that replaced them with the
`SD_SCALE` literals; `e2625ea` — the commit TZ-08a scored from; `1b8e4a7` — the merge that put it
on `main`.

**Tag:** `tz-01a-dataset` → `ea9290b92b9fa50c22d0560d5d01dfa392af44df`.

A read-only mirror of this map also sits in the Architect's project files. The repository copy is
the authority; the mirror is never edited and never quoted as state.

**Files on `main`:** sixteen TZ files (`TZ-01` … `TZ-09`), sixteen reports, ten `research/`
scripts, six `research/recorder/` files, two governance files, `.gitignore` — 51 paths in all.

---

## 2. Data

### 2.1 The observation set — the only dataset that exists

| field | value |
|---|---|
| location | Release `TZ-01a validated observation set`, tag `tz-01a-dataset`, public |
| asset | `twap-divergence-observations.parquet` |
| size | 76,818,669 bytes |
| SHA-256 | `229a944f2d5111c3e68b1fa0630f8e8658356147f9669d18665e575b60f3716b` |
| rows | 1,051,170 — 210,234 intervals × 5 checkpoints |
| checkpoints | `tau` ∈ {240, 180, 120, 90, 60} seconds remaining |
| window | 2024-09 … 2026-08, 730 days |
| source | `data.binance.vision`, spot `BTCUSDT`, 1-second klines, 63,072,000 bars, each monthly archive checksum-verified |
| gaps | 0 missing bars, 0 forward-fills; 210,240 intervals found, 210,234 used |

Anyone can fetch and verify it with no token:
`curl -sL https://github.com/seahomebatumi-ai/btc-5m-twap/releases/download/tz-01a-dataset/twap-divergence-observations.parquet | sha256sum`

**Columns (25).** Keys `interval_open_ts`, `month`, `tau`, `t`. Inputs `K`, `S_t`, `naive_move`,
`twap_so_far`, `state`. Volatility `sigma_pre`, `sigma_live`, `sd_remaining_pre`,
`sd_remaining_live`. Prices `p_twap_pre`, `p_naive_pre`, `p_twap_live`, `p_naive_live`.
Settlement proxies `twap_1s`, `twap_30s`, `twap_60s`, `outcome_1s`, `outcome_30s`, `outcome_60s`.
Integrity `n_missing_bars`, `prior_filled_bars`.

**The price data and the integrity accounting remain valid.** The `p_twap_*` columns implement
the superseded `p_interval` model and the `outcome_*` columns are invalid labels — see §2.2. This
set is Binance data and can no longer supply a label to anything.

### 2.2 The outcome labels are invalid — withdrawn 2026-09-10

`outcome_1s`, `outcome_30s` and `outcome_60s` are all **full-interval averages** of Binance
prices compared against the interval open, at 1 / 30 / 60-second sampling.

**No Polymarket settlement rule has ever had that shape.** Before 2026-08-07 the venue compared a
single close against a single open. Since 2026-08-07 it compares two readings of a Chainlink
trailing-TWAP feed — one at the close, one at the open — with a 30-second lookback until
2026-08-14 and 60 seconds after it.

The three labels are therefore withdrawn, along with every score computed against them. They stay
in the Parquet file for forensics and are never used again. The 4.147% disagreement between
`outcome_1s` and `outcome_60s` is a fact about two invalid labels and carries no information.

Correct labels are the venue's own resolutions, captured per interval as `resolution.json`. TZ-04b
read 200 of them and TZ-06 read 400.

### 2.3 Live capture — two tiers running, the quotes entirely unread

**Tier A** has been capturing since **2026-09-10 10:21:09 UTC**, into `/var/lib/btc-recorder/**`
on the VPS — outside the repository, never in git history. Streams, one gzipped file per interval:
`twap60`, `twap30`, `chainlink`, `binance`, plus `gamma.json` (S6, the market document at
`T0 + 5`), `resolution.json` (S7, the venue's settled document), `runtime.jsonl` and
`manifest.json`. Reports carry the venue payload's own `timestamp` in milliseconds and
`full_accuracy_value` at full precision; the manifest is a pure function of the interval directory
and of the schema of the day it was written.

**Tier C** — seven order-book snapshots per interval per token id, fourteen reads, at
`tau ∈ {240, 180, 120, 90, 60, 30, 10}` — was added **2026-09-12 09:53:05 UTC** on commit
`4216c04`, pid `228592`. It stores each reply verbatim with its HTTP status in
`quotes.jsonl.gz`, and the manifest gained `quotes_complete` and `quote_offsets_ms`, both
independent of `complete`. The Tier B order-book probe ran once, for 60 minutes, and retained
exactly one interval.

**What has been read.**

| read by | span | units considered | scored |
|---|---|---|---|
| TZ-04b | T0 `1789035900` … `1789100100` | 215 | 200, the Phase 0 set; all 15 non-members failed on `disconnect` |
| TZ-05a | T0 `1789206900` … `1789207800` | 5 | 4, deployment proof only — 56 of 56 reads at HTTP 200 |
| TZ-06 | T0 `1789033800` … `1789166400` | 443 | 400, the Phase 1 set; 43 non-members, every one failing on `disconnect`. **No member carries Tier C** — all closed before the `4216c04` restart |
| TZ-07a | first member `1789035000`, last `1789166400` | 443 | the same 400, re-derived by calling `tz06-calibration.scoring_set`. Feed only: `chainlink`, `twap60` and each member's `gamma.json` |
| TZ-07b | first member `1789035000`, last `1789166400` | 443 | the same 400 again, re-derived the same way; member list SHA-256 `6d94a346a47a04a1a0849968effd9023d7585fe628b304ba2ae7a15953ee67f9`, of the sorted `T0` list as decimal ASCII joined by newlines with no trailing newline. `chainlink` only, plus `twap60` for `K` in the causality check. **No outcome read at all** — no `resolution.json`, no `priceToBeat`, no label |
| TZ-08 | — | — | **BLOCKED at its own §7 V2 before any score existed.** No branch, no driver, no set, no statistic |
| TZ-08a | T0 `1789166700` … `1789296300` | 433 | **400 — the Phase 1 out-of-sample set.** 33 non-members, every one failing on `disconnect`. Disjoint from the TZ-06 set by construction; member-list SHA-256 `3b17729c050e5fbf8fed1bd0877d5dd5c229370609cd672c84eeed1ddc3d5762`, computed the same way. `manifest.json`, `resolution.json`, `chainlink` and `twap60`; **no quote file opened** |

**No quote has been aggregated and no market statistic has ever been computed.** Everything the
capture holds after `1789296300`, and every byte of Tier C, is unread. 300 of the 434 directories
in the TZ-08a span do hold a `quotes.jsonl.gz`; not one was opened.

**Measured footprint.**

| quantity | exact bytes |
|---|---|
| Tier A per interval, TZ-04b | `76,643` |
| Tier A per interval, TZ-05a over four intervals | `58,651` |
| Tier A per day, the figure every projection uses | `22,073,069` |
| Tier C per interval, stored | `6,171.5` mean |
| Tier C per interval, raw | `61,896.5` mean |
| Tier C per day | `1,777,392` |
| Tier A + Tier C per day | `23,850,461` |
| full order book per day, compressed — why it is never captured | `1,913,827,421` |

The two Tier A per-interval figures differ by 23%; the larger is kept in the projection because it
is the conservative one. **Measured against the filesystem by TZ-09 over one hour: `33,632,842`
bytes/day on disk and `26,784,064` apparent.** The projection understates the on-disk cost by
`9,782,381` bytes/day, because every interval directory holds eight or nine small files and the
filesystem rounds each to 4,096-byte blocks. Venue resolution reaches the recorder a median of `318` s after interval
close; the venue's own `closedTime` is a median of `55` s.

**Feed cadence, measured TZ-06 over 400 intervals:** `chainlink` and `twap60` both publish at
1 Hz — median gap between consecutive reports `1,000` ms on both, over 232,924 and 232,968 gaps,
a median of 584 reports per member per stream. The maximum gap of `34,000` ms is a recorded
disconnect in a neighbouring directory, not a hole in a member's own capture.

**Feed dispersion, measured TZ-07a over the same 400:** pooled over `3,028,021` one-second-grid
increments at fifteen lags, `g(h) = sigma_h^2 / sigma_1^2` rises from 1 at `h = 1` to `1.9561` at
`h = 20`, and is nearly flat above that — `2.2023` at `h = 300`. The rise is complete by twenty
seconds, so it is not an artifact of long extrapolation. Pooled and median-member readings part
company as `h` grows: `2.2023` against `1.3344` at `h = 300`. `10,779` increments were dropped
under the disconnect rule, contributed by 15 members.

**Settlement-quantity dispersion, measured TZ-07b over the same 400:** `1,384,934` admissible
anchors of `1,390,800`, `5,866` dropped by the same imported disconnect rule and by the same 15
members. `Λ(tau)` — the raw uncentred root mean square of `Y / (sigma * sqrt(H(tau)))`, where `Y`
is the settlement average minus the reading in force at the anchor — reads `1.52376` / `1.49602` /
`1.49628` / `1.47915` / `1.44466` / `1.38581` / `1.21118` at `tau` 240 / 180 / 120 / 90 / 60 / 30 /
10. **This is the dispersion of the variable the pricer's `sd` divides, not of a proxy for it**,
and §5 of that TZ froze it into the pricer.

Three diagnostics carry no threshold and are recorded because a question about **shape** now has
its data. The checkpoint-only reading is above the pooled one at every tau — `1.8184` against
`1.5238` at 240 — and the median-member reading below it. `MAD / 0.674490` and `IQR / 1.348980`
agree with each other to the third decimal and sit below `Λ` by 4% at `tau = 240` and 49% at
`tau = 10`. The empirical tails are lighter than the normal's at one `Λ` and heavier at three, at
every tau, and the gap widens monotonically as `tau` falls.

**The TZ-08a set, formed 2026-09-13:** `433` grid slots from `1789166700` to `1789296300`, of
which **400** qualify and 33 fail on `disconnect` — a 92.4% qualifying rate, above the 90% the
projection used. The set is contiguous in wall-clock time, 2026-09-11 22:45 UTC to 2026-09-13
10:45 UTC: about a day and a half. **It is out of sample; it is not a second volatility regime.**

**A third disjoint 400** needs `T0 > 1789296300` and, at that qualifying rate, about `36` hours of
capture — complete at about `T0 1789425900`, 2026-09-14 22:45 UTC. The newest interval directory at
2026-09-14 00:03:15 UTC was `1789344000`. **§6's disk row no longer bars it.**

### 2.4 What is not in the data

**Nothing in the repository is market data**: there is no Chainlink tick, no Polymarket quote, no
order-book depth, no fill and no fee-paid figure in git history, and there never will be.

On the host, oracle data and order-book snapshots both exist. **No aggregation of the order book
has been performed.** Every measurement scored to date compares the Architect's models against
either withdrawn labels (§2.2) or the venue's own resolutions.

---

## 3. Code

| file | role |
|---|---|
| `research/twap-divergence.py` | the collector. Downloads and verifies the monthly archives, walks the 1-second bars, writes one row per checkpoint. The only implementation of the superseded `p_interval` arithmetic. |
| `research/selftest-twap-divergence.py` | its analytic self-tests |
| `research/tz02-distribution.py` | aggregation over the observation set. Reads the Parquet columns only. |
| `research/pfair.py` | **the pricer — the only implementation of the CANON §1.2 model, in any language.** Also the quantities it is fed: the merged stream, the time-weighted step-function mean, the one-second grid, the realised-sigma estimator, `settlement_mean`. Since `26bbb61` it carries `SD_SCALE` and `corrected_sd` — **the TZ-07b scale: one measured literal per tau, `10` included, and an unmeasured tau raises.** `G_RATIO` is removed rather than kept alongside; `c44af68` holds it in history. Imports its reader from `analyze.py` and carries no reader of its own. |
| `research/selftest-pfair.py` | its analytic self-tests — 104 asserts: 56 model checks, 18 machinery checks and the 30 TZ-07b checks, every fixed expectation at `K = 100000.25` and `sigma = 3.25`. The four TZ-07a checks that encoded the superseded composition were deleted with it, none of them failing at the time |
| `research/tz06-calibration.py` | the Phase 1 pipeline: set formation, P, V1–V10, the gate tables. Carries no formula; calls `pfair.py` for every one. Since `1b8e4a7` `scoring_set` and `build` take `after` and `need`; at their defaults the run is the one TZ-06 ran, asserted by TZ-08a V1 to every digit of all six `Brier` values. |
| `research/tz07a-variance-time.py` | the variance–time instrument: the fifteen-lag curve, M6's disconnect rule, the in-sample diagnostics, the `gamma.json` key read. Its `G_RATIO` cross-check is removed; its `--emit-g` path still prints a table the pricer no longer has a place for. |
| `research/tz07b-settlement-dispersion.py` | the settlement-dispersion instrument: `Y(a, tau)` at every admissible anchor, the `Λ` table and its diagnostics, and the per-tau assert that the literal in `pfair.py` equals its own measurement to six significant digits. Imports M6's rule from `tz07a-variance-time.py` rather than reimplementing it, and opens no settled document. |
| `research/tz08a-out-of-sample.py` | the out-of-sample driver: the set assertions, the corrected and uncorrected gate tables, the scale statistic, the observations file. **Carries no threshold of its own** — G1 and G2 come from `tz06-calibration.py`, the scale statistic from `tz07a-variance-time.py`, the dispersion from `tz07b-settlement-dispersion.py`, and G3 is judged by the Architect. |
| `research/tz09-disk-inventory.py` | the disk inventory instrument: the `df` and `du` reads, the rate inventory, the unlinked-open enumeration, capture and log accounting, and R1's hash enumeration. **It cannot delete** — no deletion API occurs in it, and every `subprocess` call is a fixed argv of `df`, `du`, `git` or `journalctl --disk-usage`, with no shell. |
| `research/recorder/recorder.py` | the live capture, Tier A and Tier C in one process. Read-only: no order path, no CLOB authentication, no credential, no pricing arithmetic. |
| `research/recorder/config.py` | every constant the capture uses, each traced to the TZ that fixed it |
| `research/recorder/manifest.py` | the per-interval manifest, a pure function of the interval directory |
| `research/recorder/analyze.py` | the TZ-04b analyzer and the only stream reader — `reports`, `last_at_or_before`, `first_at_or_after`, `venue`, `published_equal`, `scoring_set`. Repaired by TZ-06 R-c; runs. |
| `research/recorder/probe.py` | the Tier B order-book probe, run once |
| `research/recorder/selftest.py` | the recorder's self-tests — 115 asserts, each aborting the run |

Outputs go to `research/out/**`, git-ignored except `twap-divergence-summary.md` and
`twap-divergence-contamination.md`. **`/root/tz01-out-archive/`, `/root/tz06-work/`,
`/root/tz07-work/`, `/root/tz07b-work/` and `/root/tz08a-work/` no longer exist** — TZ-09 R4
reclaimed all five, `163,987,456` bytes recovered. Everything a committed artifact names by hash was
copied first into **`/root/btc-forensics/`**: 91 files, each verified equal at source and
destination by SHA-256. The two per-observation files are there —
`tz06-work--tz06-observations.csv`, 2,801 lines, `843,788` bytes, SHA-256
`4e20c4fafbe60fe64c48ce1833a8da55f7fce2c0bad87e93b55ba95a2a4f85bb`, and
`tz08a-work--tz08a-observations.csv`, 2,801 lines, `1,066,357` bytes, SHA-256
`b810b07165e98b29258479323a0c634ccaea1917135a3336b8d28fb4bb92fa77` — both still outside the
repository and re-derivable from the pipeline. **What was not preserved:** 23 of the 24
`partitions/` files and all 24 `state/` files of the superseded TZ-01 output, which that report
names only by one hash over each whole set. See §7 item 31.
**`/root/tz04a-env/` is the interpreter the running recorder executes from, and
`/root/btc-forensics/` is the preserved evidence TZ-09 R3 copied out before R4. Neither is scratch
and nothing may remove either.**

---

## 4. What is validated, and by what

| claim | established by | status |
|---|---|---|
| the venue settles on a trailing-TWAP comparison — the 60-second feed at the close against the same feed at the open | TZ-04b V2: R1 agrees with the venue's resolved outcome on **200 of 200**, against a 199-of-200 gate fixed before any data was seen; re-run by TZ-06 R-c and reproduced exactly | **stands.** The only artifact here validated against a Polymarket settlement rule. |
| the interval-average reading is wrong, and so is the pre-August snapshot reading | TZ-04b V2: R2 175 of 200, R3 181 of 200; both reproduced by TZ-06 R-c | **stands.** Wrong on one interval in eight and one in ten — not near-misses. |
| the price to beat equals the settlement feed's reading at the open | TZ-04b V1 198 of 200; TZ-06 V3 **396 of 400**, median residual 3.78e-12 USD, worst 25.49 USD | **stands, with a ~1% failure rate every later result carries.** |
| the causal reading is genuinely causal | TZ-01a perturbation test; TZ-06 V4: 140 of 140 bit-identical under perturbation of the entire future, 140 of 140 negative controls move the model output; TZ-07a V2 repeats it on the corrected pricer, 120 of 120 and 120 of 120 | **stands.** |
| the oracle feed supports reconstructing the settlement average | TZ-06 P: the reconstructed close TWAP agrees in sign with the venue's outcome on **397 of 400**, against a floor of 396 fixed before any data was seen | **stands as a precondition.** Median absolute residual against the venue's own report `0.53` USD, worst `11.87`. |
| the Phase 1 pipeline reproduces on a later day and a different process | TZ-07a V4: `tz06-calibration.py` unmodified, six of six `Brier` values reproduced to all six decimals, P at 397 of 400 | **stands** |
| `p_fair` is not disqualified by the TZ-06 gate | TZ-06: G1 6 of 6, `Brier` 0.2107 … 0.0105 against 0.2496; G2 0 failing bins of 34 eligible | **stands as stated and for nothing more.** Phase 1 can only disqualify; it did not. |
| **`p_fair` is overconfident at `tau >= 120`** | Architect's audit of TZ-06's tables, then TZ-07a's own `λ̂`: **1.5220 / 1.4155 / 1.4139** at `tau` 240 / 180 / 120, and 1.1260 / 1.1368 / 1.4027 at 90 / 60 / 30 | **stands as a finding.** In-sample and post-hoc; it closes nothing. |
| **the oracle feed's variance grows faster than the lag** | TZ-07a M1, V1: fifteen lags, `3,028,021` increments, 400 members — `g(20) = 1.9561`, `g(300) = 2.2023` | **stands as a measurement of the feed** and of nothing else. |
| the TZ-07a correction over-widens `sd` below `tau = 120` | Architect's audit of TZ-07a §2.5: corrected `λ̂` 1.0301 / 0.9688 / 0.9846 at 240 / 180 / 120 but 0.8070 / 0.8128 at 90 / 60 and 1.4027 at 30 | **SUPERSEDED by TZ-07b.** `G_RATIO` is out of the pricer; this finding is why. Items 19 and 20 are closed. |
| **the dispersion of the settlement quantity, measured on the variable the `sd` divides** | TZ-07b M1, V1: `1,384,934` anchors of `1,390,800` over the 400 TZ-06 members at seven taus, `Λ` frozen into `pfair.py` as seven literals, each asserted against the measurement before anything was printed | **stands as a measurement of the feed.** Tested out of sample by TZ-08a V8, and it does not transfer — see the rows below. |
| the corrected pricer is causal and the pipeline still reproduces | TZ-07b V2 120 of 120 bit-identical under perturbation and 120 of 120 negative controls; V3 two full runs byte-identical; V4 TZ-06's six `Brier` values to all six decimals with P at 397 of 400, and TZ-07a's fifteen pooled `g(h)` to six significant digits | **stands** |
| **`p_fair` passes G1 and G2 out of sample** | TZ-08a on a disjoint 400: G1 6 of 6, smallest margin `0.047` at `tau = 240`; G2 **0 failing bins of 39 eligible** against an allowance of 2. The uncorrected pricer on the same set fails **7 of 36** | **stands.** Re-derived by the Architect: all 79 eligible bins reproduced in exact integer arithmetic, region and verdict, and the member list rebuilt from the disclosure table to the same SHA-256. It confirms nothing — Phase 1 can only disqualify. |
| **`p_fair` FAILS G3 out of sample, at `tau` 60 and 30** | TZ-08a's scale statistic, judged by the Architect against TZ-07a §8's `\|λ̂ − 1\| <= 0.15`: `λ̂` = 0.8629 / 1.1397 / 1.0291 / 1.0122 / **1.2949** / **2.0418** at 240 / 180 / 120 / 90 / 60 / 30 | **PHASE 1 ANSWERS NO.** §8: any one of G1, G2, G3 violated closes it. 240 and 180 pass with 0.013 and 0.010 to spare, which is not a margin on 400 observations. |
| the pre-registered prediction of item 22 is **refuted** | it predicted 0.999 / 0.946 / 0.945 / **0.761** / **0.787** / 1.012 and a failure at 90 and 60 with `λ̂` below 1. Observed: a pass at 90, and failures at 60 and 30 with `λ̂` above 1 | **the prediction failed, and how it failed is the finding.** It assumed the uncorrected `λ̂` is stable out of sample. It is not: 1.522→1.315, 1.416→1.705, 1.414→1.540, 1.126→1.497, 1.137→**1.871**, 1.403→**2.830** between two adjacent day-and-a-half windows. |
| **the two scale measurements point in opposite directions** | TZ-08a V8 ran the TZ-07b instrument unmodified on the new 400: `Λ_oos / SD_SCALE` = 1.046 / 1.019 / 0.929 / 0.913 / 0.910 / 0.913 at 240 … 30 | **stands as a measurement.** The RMS says narrow the `sd` by ~9% at short `tau`; `λ̂` says widen it by 29% at 60 and by 104% at 30. No constant per `tau` satisfies both: they are two functionals of a distribution that is not the assumed one. |
| **the settlement residual is not Gaussian, and less so the smaller `tau` is** | TZ-08a V9 on the same 400: `P(\|r\| > 3Λ)` = 0.0125 / 0.0085 / 0.0106 / 0.0158 / 0.0219 / 0.0268 / 0.0253 at 240 … 10, against the normal's 0.0027 — **8 to 10 times the normal tail below `tau = 90`** — while `MAD / 0.674490` sits 18 / 22 / 30 / 41 / 56 / 71 / 81 per cent below `Λ` | **stands, and it is why G3 failed.** A sharp centre with a heavy tail is not a normal at any scale. Item 22 suspected this in sample; out of sample the gap is roughly twice as wide. |
| **`λ̂` at `tau = 30` is carried by one observation** | Architect's arithmetic over TZ-08a §11 item 1: at `T0 1789268400` the feed moved about 40 USD in the final 30 s, `z = −10.819`, `p_fair` exactly `0.0`, and the venue resolved Up. That single point gains **+45.2** log points between `λ = 1` and `λ̂ = 2.0418`; the other 399 **lose 14.7** | **stands as a finding about the estimator and about the tail.** `Φ` assigned about 1e-27 to something that happened once in 400. Without that point the maximiser is below 1 — which does not rescue the gate, and is not a reason to drop it. |
| Tier C captures the book at seven checkpoints without loss | TZ-05a: 56 of 56 reads at HTTP 200, 4 of 4 `quotes_complete` | **stands as a deployment fact.** Not a market observation. |
| the collector was not modified between TZ-01a and TZ-02 | hash equality, `6c5089…` read from `origin/main` | **stands** |
| the sign of `D = p_interval − p_naive` has no preferred direction | TZ-02 measurement 1 | **stands, and is of no consequence** |
| the venue's maker-rewards terms are readable from our capture | **contradicted.** TZ-07a V9: the `rewards` key is absent entirely from all 400 `gamma.json` documents, which are otherwise present and well formed | **WITHDRAWN** — the claim was read from the venue's documentation, never from the capture |
| the TWAP model beats the endpoint model · divergence is abundant · inversions are the rare tail | Gate B, Gate A2, TZ-02 | **WITHDRAWN** — all scored against §2.2 labels |

---

## 5. Phase state

| phase | question | state |
|---|---|---|
| 0 | is the settlement rule what the CANON §1.1 says it is? | **CLOSED 2026-09-11 — yes. TZ-04b: 200 of 200 against a 199-of-200 gate**, reproduced by TZ-06 R-c |
| 1 | is the corrected `p_fair` calibrated against true-rule labels? | **CLOSED 2026-09-13 — no.** TZ-06's gate could only disqualify and did not. TZ-07a's correction was mis-composed; TZ-07b measured the right variable and froze `SD_SCALE`. **TZ-08a scored it on a disjoint 400 against the gate TZ-07a §8 fixed before that set existed: G1 6 of 6, G2 0 of 39, and G3 fails at `tau` 60 and 30.** The Architect's own pre-registered prediction is refuted. `SD_SCALE` and the gate are untouched. |
| 2 | does the **market price** deviate from `p_fair`, and by how much? | not started — the decision point, **and Phase 1's answer bars entry with this pricer.** Tier C is accumulating the input; nothing has been read, and §6's disk row no longer bars it. |
| 3 | is the deviation capturable after fee, spread, depth, 50 ms taker delay, oracle basis? | not started |
| 4 | live, minimum size, fixed loss limit | not started |

**This project has a pricer whose settlement variable is correctly identified, whose scale does not
transfer out of sample, which is disqualified at `tau` 60 and 30, and no known edge.** Phases 0 and
1 could only ever disqualify, and Phase 1 now has. The open model question is **the link or
`sigma`**: either the conditional law is heavy-tailed, or the law is Gaussian and the scale estimate
lags the move. **The unconditional residual cannot tell them apart** — a Student's `t` is itself a
scale mixture of normals, so a pool of correct Gaussians with a floating `sigma` reproduces V9's
sharp centre and heavy tail exactly. TZ-10 separates them. Nothing is re-fitted, and neither
`SD_SCALE` nor the §8 gate moves.

---

## 6. Environment

| item | value |
|---|---|
| host | Vultr VPS (Warsaw); the Executor runs Claude Code CLI **on the VPS itself**. A cloud Claude Code session is not this host and cannot execute anything that touches the capture. |
| **host identity, for TZ host gates** | `/var/lib/btc-recorder/` exists and holds interval directories · the recorder process is running and the newest `runtime.jsonl` start record carries sha `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` · the filesystem holding it is `/dev/vda2`, total `31,612,203,008` bytes. All three, or it is not the capture host. |
| language | Python 3.12 |
| stack | Parquet storage, pandas/pyarrow, DuckDB for aggregation; `decimal.Decimal` at 60 digits for every price |
| auth | CLI subscription auth; `ANTHROPIC_API_KEY` must not be set |
| git remote | HTTPS with the repository token embedded in the remote URL |
| egress, **verified 2026-09-12** | DNS and TCP/443 open to `ws-live-data.polymarket.com`, `gamma-api.polymarket.com`, `clob.polymarket.com`, `ws-subscriptions-clob.polymarket.com`, `docs.polymarket.com`. Anonymous only; no credentials of any kind are held. |
| **disk, measured 2026-09-14 00:03:15 UTC by TZ-09** | one writable filesystem `/dev/vda2`, total `31,612,203,008` bytes, free **`14,416,265,216`**. `/var/lib`, `/root` and `/var/www` are all on it. **Any TZ that states a resource floor states it in exact bytes and derives it from this row.** |
| **capture cost, measured** | modelled Tier A + Tier C `23,850,461` bytes/day; **measured against the filesystem by TZ-09, `33,632,842` on disk and `26,784,064` apparent**. That is the recorder's own write rate, and **it is not the rate this filesystem is filling at.** |
| **the consumer, identified — measured 2026-09-13/14 by TZ-09** | The consumer this row could not name is **`/root/PROJECT_GAMING_PS5/netaudit/telemetry/captures`**, another project on this shared host: `6,896,218,112` bytes standing at 2026-09-13 17:55:36 UTC, and `2,547,725,419` bytes/day over an `11,440` s window three hours later. **It is intermittent** — `8,214,918` bytes/day across TZ-09's quiet deciding hour against `2,547,725,419` across the active window — and the `815,000,000` bytes/day this row used to carry is a 30.4-hour average of that mixture. Our own persistent baseline is `50,352,616` bytes/day: capture `33,342,903`, journald `8,794,795`, that project idle `8,214,918`. **The Boss reports the telemetry stopped 2026-09-14; no TZ has measured the stop, and the next TZ that touches the host re-reads this row.** |
| **headroom — a range, and never a point** | From `14,416,265,216` free to the `2,000,000,000` floor is `12,416,265,216` bytes. At our baseline `50,352,616` bytes/day that is **247 days**; if `PROJECT_GAMING_PS5`'s telemetry resumes at its measured `2,775,683,706` bytes/day it is **4.5 days**. Which end applies is decided by another project's process, not by ours. **TZ-09's own `143.87` days is not adopted**: it divides free space by a rate measured while that consumer was idle and TZ-09's own scratch was writing. The `245 days` this row carried at revision `2026-09-13-b` stays withdrawn. See §7 items 25, 29 and 30. |
| **price to beat** | published by Gamma only after settlement, at `events[0].eventMetadata.priceToBeat`, and captured per interval in `resolution.json`. Not available before the close; a live pricer reconstructs it from the feed. |
| **resolution endpoint** | `GET https://gamma-api.polymarket.com/markets/slug/btc-updown-5m-{T0}`, polled from `T0+333` every 15 s |
| **CLOB websocket** | `wss://ws-subscriptions-clob.polymarket.com/ws/market` |
| **CLOB order book, REST** | `GET https://clob.polymarket.com/book?token_id={token_id}` — public, unauthenticated |
| **venue constants, measured TZ-05a** | minimum tick size `0.01`, agreeing across `orderPriceMinTickSize` (Gamma), `tick_size` (`/book`) and `minimum_tick_size` (`/markets/{condition_id}`) · minimum order size `5` · fee schedule `{"exponent": 1, "rate": 0.07, "rebateRate": 0.2, "takerOnly": true}`, `feeType` `crypto_fees_v2` · outcome mapping resolved from `tokens[].outcome`, not from array position |
| **maker incentives** | Read from the venue's documentation 2026-09-12: makers pay no fee; the measured `rebateRate` `0.2` is a share of the taker fee paid on a fill; separately the venue runs a liquidity-rewards programme paying for resting orders near the midpoint, scored quadratically in distance and linearly in size, sampled once a minute, configured per market as `rewards.rewardsMinSize`, `rewards.rewardsMaxSpread` and `clobRewards[].rewardsDailyRate`. **Measured TZ-07a V9: none of that is in our capture.** The `rewards` key is absent entirely from all 400 `gamma.json` documents — not null, not empty. Whether that is the endpoint, the query or the venue is **unknown and uninvestigated**; no maker assumption rests on this row until a TZ measures it. |
| host is shared | unrelated production services live on the same filesystem — `crypto-auto`, `my_real_estate_bot`, `seahome_webapp.git`, `/var/www`, `/var/log`. The recorder never deletes anything it did not write. |
| capture path | `/var/lib/btc-recorder/**` — outside the repository by design, so no capture can reach git history |
| **RTDS session limit, measured 2026-09-10** | the server closes every websocket `7,200` s after it opens, `1001 Going away`, timer restarting on each new connection. Undocumented. **No TZ may require an unbroken socket for longer than this.** |
| clock | NTP-disciplined; SNTP replies validated at reception since `4216c04`. Maximum absolute offset measured over the TZ-05a window: `18.789` ms. An offset above 50 ms invalidates a latency claim; it is not a membership condition for anything. |
| **sandbox limit — network** | calls that read the git token and send it to `api.github.com` are refused. `git` push/pull work. Release creation and asset upload cannot be done from inside the session — hand the upload to the Boss and verify by anonymous download. |
| **sandbox limit — destructive actions** | `kill` is refused by the permission classifier, alone or inside a compound command, and TZ-09 established that `rm -rf` of several trees is refused the same way. **Any TZ that must restart the recorder or remove a tree hands the Boss one exact block** and verifies the outcome from `runtime.jsonl`, `ps`, `df` and `test -e` rather than from his report. |

Not yet decided by any TZ and therefore not present: systemd units, the Parquet decision journal,
any deployment. **Capture retention is fixed by TZ-09 §5:** the capture is never deleted; archiving,
if it is ever done, is its own reversible TZ; a TZ's `/root/tz<NN>-work/` is reclaimed by the next TZ
once that TZ's report is on `main`, except what a committed artifact names by hash, which is copied
to `/root/btc-forensics/` first.

---

## 7. Open defects

| # | defect | disposition |
|---|---|---|
| 1 | `research/tz02-distribution.py` records the collector-hash comparison into `checks["collector_sha_matches"]` but never asserts it. The run completes on a mismatch. | open. Fix in the next TZ that touches that file; do not edit the committed report. |
| 2 | The TZ-02 report was amended after commit (`356c29a`). | closed by rule: contract §3.2 and §5.2. Both versions stay in history. |
| 3 | The TZ-02 implementation commit `f8a0c37` reached `main` without a merge and without a verdict. | closed by rule: contract §4.1 and the §4.2 self-check. |
| 4 | The Executor contract carried a space before its extension and both governance files were duplicated inside `research/`. | closed by TZ-03, PR #1. |
| 5 | **The settlement mechanic was wrong from inception.** | CANON replaced, labels withdrawn (§2.2). **The class is closed by TZ-04b V2.** |
| 6 | **TZ-04 §4 set a 20 GB free-space floor written from assumption.** | closed by rule: every resource floor is stated in exact bytes derived from §6. |
| 7 | Two executions of TZ-04 wrote two different reports to one path. | closed by rule: a re-execution never reuses a report path. |
| 8 | **TZ-04a §6 required 200 *consecutive* complete intervals** across a socket the venue closes every 7,200 s. | closed by rule: a requirement is a count of qualifying units, never an unbroken run. |
| 9 | **The V4 read-only proof was a bad instrument.** | closed by TZ-05a R-a and by ruling: a text search cannot prove the absence of a capability. The standing carrier is the merge-base diff plus the absence of any CLOB auth path. |
| 10 | **The recorder's SNTP client accepted invalid replies.** | closed by TZ-05a R-b, merged; twelve self-tests reproduced independently by the Architect. |
| 11 | **TZ-05 could not be executed in one session on any host.** | closed by TZ-05a and by CANON hard rule 11. |
| 12 | **`analyze.py:207` aborted every run** after the TZ-05a restart, killing the instrument behind the Phase 0 count. | **closed by TZ-06 R-c, merged.** The span is now bounded by the next start record, `within_span` is asserted per scored interval, and the repaired analyzer reproduces TZ-04b on every count — 215 / 200 / 15 / 200 / 175 / 181. |
| 13 | The TZ-05a report's exclusion line gives the wrong window-opening time for `1789206600`. | closed by rule: membership is re-derived by the Architect from epochs rather than read from the report. |
| 14 | TZ-05a carries two sections numbered `## 7`. | closed by rule: section numbers are asserted unique in the pre-delivery change list. |
| 15 | **TZ-06's calibration gate was marginal only** — a per-bin interval with a two-bin allowance cannot see a coherent one-sided pattern, and it passed a pricer whose sd is understated by half at `tau = 240`. Architect's defect. | open until TZ-08 scores against the replacement. Repaired by rule: **every calibration gate carries a scale statistic and a shape statistic, both fixed before any data is seen.** TZ-07a §8 fixes both, and the scale statistic exposed item 19 within one report. |
| 16 | **TZ-06 §3 and §4 pulled in opposite directions for 25 of the 400 members**: §3 forbids carrying a value across a recorded disconnect, §4 makes only the interval's own manifest a condition. | **closed by TZ-07a M6.** Of the 25, ten have their predecessor's outage before `T0 - 300` and lose no second; the other fifteen do overlap and are now excluded increment by increment — `10,779` of `3,038,800` dropped, per lag and by member. |
| 17 | **`analyze.py`'s `V5_determinism` fell from 215 of 215 to 0 of 215.** Rebuilding a 2026-09-10 manifest with today's `manifest.py` adds the two keys TZ-05a introduced; every field the old manifests carry rebuilds identically. | open. Repaired by rule in the next TZ that touches `analyze.py`: a determinism check compares a rebuild against a rebuild, never against an artifact written under an older schema. |
| 18 | **`SYSTEM-MAP.md` on `main` was replaced by a chat message.** Commit `891d161` overwrote the map with an upload note, so revision `2026-09-12-b` never existed in the repository and TZ-07's fingerprint gate had nothing to read. | closed by rule: **after every upload the Architect reads `origin/main` and confirms the file that landed before `EXECUTE` is sent.** Exercised for `2026-09-12-c`; the map on `main` and the Architect's mirror were confirmed equal by hash. |
| 19 | **The TZ-07a correction divides the wrong random variable.** `g(h)` is the dispersion of a *single increment* over lag `h`; the pricer's `sd` describes the settlement average minus the current price, which at `tau >= 60` is a lead of `tau - 60` seconds **plus** a 60-second average contributing `20` of the `tau - 40`. Substituting `g(tau - 40)` for the whole scales the averaging part by a ratio belonging to the lead part, and the error grows as the averaging share grows: in-sample `λ̂` lands at 1.03 / 0.97 / 0.98 at `tau` 240 / 180 / 120 but 0.807 / 0.813 at 90 / 60. Architect's defect. | **closed by TZ-07b**, merged at `fb5c426`: `Y(a, tau)` is the settlement average minus the reading in force at the anchor, measured at every admissible anchor of every member, and `G_RATIO` is gone from the pricer. The rule stands: **a correction is measured on the exact random variable it divides, never substituted from a proxy horizon.** |
| 20 | **TZ-07a §8 gates six taus while §4 corrects five.** `tau = 30` is on the near branch, where `G` was fixed at exactly 1 with no measurement, and G3 scores it anyway — in-sample `λ̂` there is 1.4027. Architect's defect. | **closed by TZ-07b**: the keys of `SD_SCALE` are `pfair.TAUS`, `10` included, and a tau with no measured scale raises inside `corrected_sd`. The rule stands: **every tau a gate scores carries a measured constant.** |
| 22 | **TZ-07b §4 justified the root mean square as the maximum-likelihood scale of a Gaussian, and the measurement it commissioned refutes the premise.** The report's own tail table shows `r` is lighter than normal at one `Λ` and heavier at three, at every tau and increasingly so as `tau` falls. The root mean square therefore overstates the calibrating scale by more where the RMS-to-robust gap is wider — which is exactly where the predicted `λ̂` sits furthest from 1. A robust constant is no answer either: it would predict 0.836 at `tau = 90` and 1.337 at 30. The open question is the residual's **shape**, and no single constant per tau addresses it. Architect's defect. | **closed by TZ-08a, and the question it raised is answered: the shape is the defect.** Out of sample the tail at `3Λ` runs 8 to 10 times the normal's below `tau = 90`, and the robust scale sits 56 to 81 per cent under the RMS. No constant per tau closes that, and G3 failed at 60 and 30. `SD_SCALE` was not touched before the test and is not touched after it. The rule stands: **a scale estimator is justified by a distributional assumption, and the report that freezes the estimator reports the check of that assumption in the same document.** |
| 23 | **TZ-07b §2 forbade reading any outcome while §7 V4 required re-running two pipelines that read outcomes internally.** The Executor read the two sections as governing different things, carried only counts of exact matches out of the subprocesses, and disclosed the reading. Architect's defect. | closed by ruling — the Executor's reading is upheld: V4's subprocesses are exempt and no calibration statistic left them. Repaired by rule: **a scope prohibition names, in its own section, the checks that are exempt from it.** |
| 24 | TZ-07b's V1 guard — the `bisect`ed window handed to `pfair.time_weighted_mean` — was verified on the **first member only**, 175 of 175. The members carrying a recorded disconnect are the ones a bounded slice would break on, and none was sampled. | closed by rule: **a guard on an implementation shortcut samples across the scored set and includes the pathological members by construction.** No re-run: the shortcut narrows an argument the function would otherwise have scanned to the same rows, the disconnect rule drops those anchors before the call, and V3 reproduced byte-identically over three full runs. |
| 25 | **The Architect's §6 headroom figure was wrong by two orders of magnitude.** `245 days` divided free space by the recorder's own write rate, on a host the same section calls shared. Measured total drain is 0.84 to 1.00 GB/day and the true figure is 4.6 to 5.7 days. Architect's defect. | **closed by TZ-09 and the Architect's audit of it.** The consumer is named in §6 in exact bytes. The rule stands: **a headroom figure is derived from the measured rate of change of free space over a stated wall-clock window, never from any one process's write rate** — and §6 now carries a range rather than a point, because one window on a host with an intermittent consumer fixes neither end. |
| 26 | **TZ-07a §8's G3 fixes a likelihood over `Phi` and no tail-accurate `log Phi`.** `pfair.phi` returns exactly `0.0` below `z ≈ −8.37`, so one saturated prediction that disagrees with its label sends `ll(1)` to `-inf`, the likelihood ratio to `inf` and its p-value to `0`. It happened at `tau = 30`, on `T0 1789268400`. Architect's defect. | closed by ruling — the Executor's reading of TZ-08a §4.5 is upheld and the run is **not** BLOCKED: the only quantity §8 bounds, `λ̂`, is unaffected past its sixth decimal (2.041843 against 2.041844 evaluated tail-accurately), and only the unthresholded quantities degenerate. Repaired by rule: **a specification that fixes a likelihood over `Phi` fixes its tail-accurate `log Phi` in the same section.** |
| 27 | **A statistic a gate bounds was reported with no influence figure, and one observation set it.** `λ̂ = 2.0418` at `tau = 30` is carried by a single point; the other 399 prefer `λ = 1` by 14.7 log points. Neither TZ-07a §8 nor TZ-08a asked for it, so the report could not have shown it and the Architect had to derive it during the audit. Architect's defect. | open. Repaired by rule: **a fitted statistic a gate bounds is reported together with its value recomputed without its single most influential observation.** The committed report is not edited, and the gate is judged on the value §8 defines. |
| 28 | `tz06-calibration.build`'s set-size assert message names `SET_SIZE` where the run may now pass a different `need`. Disclosed by TZ-08a §11 item 4; exact at the default, which every run to date has used. | open. Fix in the next TZ that touches that file; do not edit the committed report. |
| 29 | **TZ-09 §3 M3's consumer rule did not exclude the measuring run's own footprint.** It named `/root` at `43,490,744` bytes/day, of which `1,490,944` of `1,843,200` — **80.9%** — is `/root/tz09-work` and `/root/.claude`, this TZ's scratch and the Executor's own session store. Strip the apparatus and the named consumer runs at about `8,300,000` bytes/day. Architect's defect. | open until a TZ re-measures the host after the telemetry stop. Repaired by rule: **a rate measurement of a shared resource subtracts the measuring run's own footprint from the quantity it attributes, and reports that footprint separately.** |
| 30 | **TZ-09 §3 fixed a one-hour deciding window on a host whose dominant consumer is intermittent.** The designed instrument missed the thing the TZ existed to find; a read the TZ did not ask for found it three hours later at `2,547,725,419` bytes/day. Architect's defect. | open until §6's range is collapsed by measurement. The Executor was right not to re-choose the window after seeing data, which would have been reinterpreting §3. Repaired by rule: **a window that must characterise an intermittent consumer is at least as long as that consumer's measured idle-to-active period, or the TZ states in its own §3 that its figure is a lower bound.** |
| 31 | **TZ-09 §5.3 defined preservation by "the SHA-256 a committed artifact names" and said nothing about a hash taken over several files.** `CryptoReports/TZ-01-…-report.md` §2 gives one SHA-256 over all of `partitions/` and one over all of `state/`; neither is any single file's hash, so R2 as written deleted 23 partition files and 24 state files, and those two rows can no longer be verified from disk. The Executor extended the rule to save an abbreviated-hash file and applied it literally here, disclosing both. Architect's defect. | closed by ruling — the Executor's reading is upheld, and the material loss is near zero: TZ-01's results are withdrawn under §2.2 and its dataset is superseded by the `tz-01a-dataset` Release asset. Repaired by rule: **a preservation rule states what an aggregate hash over several files names; where it names nothing, deleting any member is authorized only by a TZ that says so in exact counts.** |
| 32 | **TZ-09 §7 V2 proved the instrument cannot delete by grepping Python deletion APIs, and the instrument imports `subprocess`.** The check as specified could not have caught `subprocess.run(["rm", …])`; the Architect had to re-derive the proof during the audit by enumerating all four call sites. It holds — every argv is a fixed `df`, `du`, `git` or `journalctl --disk-usage`, with no shell — but the instrument did not establish it. Architect's defect, the same class as item 9. | closed by rule: **a proof that code cannot perform an action enumerates its delegation paths — `subprocess`, `shell=True`, external binaries — as well as the in-language APIs.** The committed report is not edited. |
| 21 | The TZ-07a report's §2.5 summary carries one `eligible bins` column for two estimators whose eligibility differs — 10 / 9 / 6 / 5 / 2 / 2 uncorrected against 8 / 10 / 9 / 7 / 3 / 2 corrected. The per-tau tables are correct; only the summary is ambiguous, and G2 counts failures over eligible bins. | closed by rule: **a summary table reporting two estimators reports eligibility per estimator.** The committed report is not edited. |

---

## 8. What does not exist yet

No validated volatility scale, no order-book history beyond the seven-checkpoint snapshots
accumulating unread, no Polymarket client code, no execution path, no capital at risk. Nothing in
this repository can place an order. The recorder reads; it cannot write to any venue.

The pricer exists and has now been scored twice, against 800 labels the venue itself produced, on
two disjoint sets. It discriminates, and its shape passes; its scale does not transfer, and it is
disqualified at `tau` 60 and 30. **Why it is disqualified is now the only open model question, and
it has two candidate answers that the data so far cannot separate** — a heavy-tailed link, or a
Gaussian link divided by a `sigma` estimate that lags the move.

The recorder is running on `4216c04` with both tiers. The filesystem is no longer the binding
constraint: `14,416,265,216` bytes free, the consumer that was eating it identified and reported
stopped, and headroom between **4.5 and 247 days** depending on whether it resumes. Between them the
pricer and the recorder have produced three conclusions — the Phase 0 answer, the Phase 1 answer and
the reason for it — one deployment proof, three measurements of the feed's own dispersion, one
measurement of the host, and one written prediction that the data refuted.
