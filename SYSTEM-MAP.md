# SYSTEM MAP — btc-5m-twap

**Revision 2026-09-13-b.** Written by the Architect; the Executor never edits it. This is a
**state** document: what exists right now. It holds no mission, no rules and no history.

- The CANON (Architect's project instructions, not in this repository) holds the mission, the
  fair-value model, the measured facts and the phase gates.
- `BTC-EXECUTOR-INSTRUCTIONS.md` holds how the Executor works.
- **This map never restates a CANON §1.2 formula.**

---

## 0. Fingerprint gate

Every TZ header states the required revision string and the anchors below. The Executor compares
before doing any work; a mismatch is BLOCKED.

**Revision string:** `2026-09-13-b`

| anchor | value |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-open / 2-not-started` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` |
| `A6` — pricer | `cb72abb8dd8a` |

Anchors are the first 12 hex characters of the SHA-256 of the named artifact, except `A3`.
`A5` is `research/recorder/recorder.py`, the code the live capture runs. `A6` is
`research/pfair.py`, the only implementation of the model: **any TZ that scores a pricer states
`A6`, so what was scored is never in doubt.** `A6` changed at `fb5c426` when PR #8 replaced
`G_RATIO` with `SD_SCALE`: the §1.2 formulas and `state` are byte-identical inside it and only the
constant multiplying `sigma * sqrt(H(tau))` moved. `9bd4213a60a3` is the value TZ-07a and TZ-07b
were both gated against, and nothing scored under it is re-opened by this revision.

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
| `research/tz06-calibration.py` | 569 | 26,548 | frozen | `a6aaed94964775f34a9b26dba448ff0f998f32ad952e244bff834b67439ef123` |
| `research/tz07a-variance-time.py` | 619 | 28,219 | frozen | `4321637751a3b847fa7e59309555b802dcc9d5ba68c7407a8ec20ab76c1b3d5e` |
| `research/tz07b-settlement-dispersion.py` | 515 | 24,926 | frozen | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` |
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
every score this project will ever quote comes out of it**, and `tz07a-variance-time.py` and
`tz07b-settlement-dispersion.py` because a committed measurement came out of each.

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

**Branches: `main`, and nothing else.** `tz-07b-settlement-dispersion` merged at `fb5c426` and
was deleted, `tz-07a-variance-time` before it; neither retained anything that is not on `main`.
The head of `main` is never a gate; commits are named where they matter.

| pull request | head | disposition |
|---|---|---|
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
`SD_SCALE` literals.

**Tag:** `tz-01a-dataset` → `ea9290b92b9fa50c22d0560d5d01dfa392af44df`.

A read-only mirror of this map also sits in the Architect's project files. The repository copy is
the authority; the mirror is never edited and never quoted as state.

**Files on `main`:** thirteen TZ files (`TZ-01` … `TZ-07b`), thirteen reports, eight `research/`
scripts, six `research/recorder/` files, two governance files, `.gitignore` — 43 paths in all.

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

**No quote has been aggregated and no market statistic has ever been computed.** Everything the
capture holds after `1789166400`, and every byte of Tier C, is unread.

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
is the conservative one. Venue resolution reaches the recorder a median of `318` s after interval
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

**Available to TZ-08, counted 2026-09-12 22:00 UTC by TZ-07b V6:** `280` interval directories
with `T0 > 1789166400`, spanning `1789166700` … `1789250400`, of which **253** satisfy TZ-06 §4's
five conditions — 24 failing on `disconnect`, 3 carrying neither manifest nor S7 document. TZ-08's
set is the first 400 that qualify and is never shrunk. At one directory per 300 s and the measured
90% qualifying rate the remaining `147` need about `13.5` hours of capture from that count, so
**TZ-08 is not issued before they exist** and its own set formation BLOCKS below 400.

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
| `research/tz06-calibration.py` | the Phase 1 pipeline: set formation, P, V1–V10, the gate tables. Carries no formula; calls `pfair.py` for every one. |
| `research/tz07a-variance-time.py` | the variance–time instrument: the fifteen-lag curve, M6's disconnect rule, the in-sample diagnostics, the `gamma.json` key read. Its `G_RATIO` cross-check is removed; its `--emit-g` path still prints a table the pricer no longer has a place for. |
| `research/tz07b-settlement-dispersion.py` | the settlement-dispersion instrument: `Y(a, tau)` at every admissible anchor, the `Λ` table and its diagnostics, and the per-tau assert that the literal in `pfair.py` equals its own measurement to six significant digits. Imports M6's rule from `tz07a-variance-time.py` rather than reimplementing it, and opens no settled document. |
| `research/recorder/recorder.py` | the live capture, Tier A and Tier C in one process. Read-only: no order path, no CLOB authentication, no credential, no pricing arithmetic. |
| `research/recorder/config.py` | every constant the capture uses, each traced to the TZ that fixed it |
| `research/recorder/manifest.py` | the per-interval manifest, a pure function of the interval directory |
| `research/recorder/analyze.py` | the TZ-04b analyzer and the only stream reader — `reports`, `last_at_or_before`, `first_at_or_after`, `venue`, `published_equal`, `scoring_set`. Repaired by TZ-06 R-c; runs. |
| `research/recorder/probe.py` | the Tier B order-book probe, run once |
| `research/recorder/selftest.py` | the recorder's self-tests — 115 asserts, each aborting the run |

Outputs go to `research/out/**`, git-ignored except `twap-divergence-summary.md` and
`twap-divergence-contamination.md`. `/root/tz01-out-archive/` holds the superseded TZ-01 output.
`/root/tz06-work/tz06-observations.csv` holds the Phase 1 per-observation rows — 2,801 lines,
`843,788` bytes, SHA-256 `4e20c4fafbe60fe64c48ce1833a8da55f7fce2c0bad87e93b55ba95a2a4f85bb`,
outside the repository and re-derivable from the pipeline. `/root/tz07-work/` and
`/root/tz07b-work/` hold TZ-07a's and TZ-07b's scratch and outputs, likewise outside the
repository.

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
| **the dispersion of the settlement quantity, measured on the variable the `sd` divides** | TZ-07b M1, V1: `1,384,934` anchors of `1,390,800` over the 400 TZ-06 members at seven taus, `Λ` frozen into `pfair.py` as seven literals, each asserted against the measurement before anything was printed | **stands as a measurement of the feed.** It scores nothing, it is in-sample on the set that produced the finding it repairs, and it has never been tested out of sample. |
| the corrected pricer is causal and the pipeline still reproduces | TZ-07b V2 120 of 120 bit-identical under perturbation and 120 of 120 negative controls; V3 two full runs byte-identical; V4 TZ-06's six `Brier` values to all six decimals with P at 397 of 400, and TZ-07a's fifteen pooled `g(h)` to six significant digits | **stands** |
| **the frozen scale is predicted to fail TZ-07a §8 G3 at `tau` 90 and 60** | Architect's arithmetic, recorded here **before the TZ-08 set exists**: `λ̂` is a fitted multiplicative scale, so `λ̂_new = λ̂_uncorrected / SD_SCALE` identically — an identity that reproduces all six of TZ-07a's published corrected values to four decimals. It gives **0.999 / 0.946 / 0.945 / 0.761 / 0.787 / 1.012** at 240 / 180 / 120 / 90 / 60 / 30, the last two at −3.4 and −2.4 standard errors from 1 | **a pre-registered prediction, not a result.** In-sample-equivalent. TZ-08 tests it on a disjoint 400; the gate does not move and no constant is touched before it. See §7 item 22. |
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
| 1 | is the corrected `p_fair` calibrated against true-rule labels? | **open.** TZ-06's gate passed and therefore did not disqualify. **TZ-07a** measured the feed's variance–time curve and froze a correction from it that was mis-composed. **TZ-07b** measured the dispersion of the settlement quantity itself, replaced the constants with `SD_SCALE` and closed items 19 and 20. **TZ-08** scores out of sample against the gate TZ-07a §8 fixed, which does not move — and which the Architect has predicted **in writing and before that set exists** will fail G3 at `tau` 90 and 60 (item 22). |
| 2 | does the **market price** deviate from `p_fair`, and by how much? | not started — the decision point. Tier C is accumulating the input; nothing has been read. |
| 3 | is the deviation capturable after fee, spread, depth, 50 ms taker delay, oracle basis? | not started |
| 4 | live, minimum size, fixed loss limit | not started |

**This project has a pricer whose settlement variable is correctly identified, whose scale is now
measured on that variable and has never been tested out of sample, and no known edge.** Phases 0
and 1 could only ever disqualify.

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
| **disk, measured 2026-09-12** | one writable filesystem `/dev/vda2`, total `31,612,203,008` bytes, free `7,855,497,216`. `/var/lib`, `/root` and `/var/www` are all on it. **Any TZ that states a resource floor states it in exact bytes and derives it from this row.** |
| **capture cost, measured** | Tier A + Tier C `23,850,461` bytes/day against a `2,000,000,000` byte floor — headroom `5,855,497,216` bytes, about **245 days**. Neither floor is near. |
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
| **sandbox limit — process signals** | `kill` is refused by the permission classifier, alone or inside a compound command. **Any TZ that must restart the recorder hands the Boss two exact commands** and verifies the outcome from `runtime.jsonl`, `ps` and the log rather than from his report. |

Not yet decided by any TZ and therefore not present: systemd units, the Parquet decision journal,
capture retention policy, any deployment.

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
| 22 | **TZ-07b §4 justified the root mean square as the maximum-likelihood scale of a Gaussian, and the measurement it commissioned refutes the premise.** The report's own tail table shows `r` is lighter than normal at one `Λ` and heavier at three, at every tau and increasingly so as `tau` falls. The root mean square therefore overstates the calibrating scale by more where the RMS-to-robust gap is wider — which is exactly where the predicted `λ̂` sits furthest from 1. A robust constant is no answer either: it would predict 0.836 at `tau = 90` and 1.337 at 30. The open question is the residual's **shape**, and no single constant per tau addresses it. Architect's defect. | open. **Nothing changes before TZ-08**: editing a constant after seeing that it would fail a gate is tuning, and neither the gate nor `SD_SCALE` moves. The §4 prediction is recorded first so that TZ-08 is a genuine out-of-sample test of it. Repaired by rule: **a scale estimator is justified by a distributional assumption, and the report that freezes the estimator reports the check of that assumption in the same document.** |
| 23 | **TZ-07b §2 forbade reading any outcome while §7 V4 required re-running two pipelines that read outcomes internally.** The Executor read the two sections as governing different things, carried only counts of exact matches out of the subprocesses, and disclosed the reading. Architect's defect. | closed by ruling — the Executor's reading is upheld: V4's subprocesses are exempt and no calibration statistic left them. Repaired by rule: **a scope prohibition names, in its own section, the checks that are exempt from it.** |
| 24 | TZ-07b's V1 guard — the `bisect`ed window handed to `pfair.time_weighted_mean` — was verified on the **first member only**, 175 of 175. The members carrying a recorded disconnect are the ones a bounded slice would break on, and none was sampled. | closed by rule: **a guard on an implementation shortcut samples across the scored set and includes the pathological members by construction.** No re-run: the shortcut narrows an argument the function would otherwise have scanned to the same rows, the disconnect rule drops those anchors before the call, and V3 reproduced byte-identically over three full runs. |
| 21 | The TZ-07a report's §2.5 summary carries one `eligible bins` column for two estimators whose eligibility differs — 10 / 9 / 6 / 5 / 2 / 2 uncorrected against 8 / 10 / 9 / 7 / 3 / 2 corrected. The per-tau tables are correct; only the summary is ambiguous, and G2 counts failures over eligible bins. | closed by rule: **a summary table reporting two estimators reports eligibility per estimator.** The committed report is not edited. |

---

## 8. What does not exist yet

No validated volatility scale, no order-book history beyond the seven-checkpoint snapshots
accumulating unread, no Polymarket client code, no execution path, no capital at risk. Nothing in
this repository can place an order. The recorder reads; it cannot write to any venue.

The pricer exists and has been scored once, against 400 labels the venue itself produced. Its
scale is now measured on the variable it describes and merged at `fb5c426`, and it has never been
tested out of sample. The recorder is running on `4216c04` with both tiers. Between them they have
produced two conclusions — the Phase 0 answer and the Phase 1 finding — one deployment proof, two
measurements of the feed's own dispersion, and one written prediction awaiting the set that tests
it.
