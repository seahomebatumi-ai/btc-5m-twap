# SYSTEM MAP — btc-5m-twap

**Revision 2026-09-12-c.** Written by the Architect; the Executor never edits it. This is a
**state** document: what exists right now. It holds no mission, no rules and no history.

- The CANON (Architect's project instructions, not in this repository) holds the mission, the
  fair-value model, the measured facts and the phase gates.
- `BTC-EXECUTOR-INSTRUCTIONS.md` holds how the Executor works.
- **This map never restates a CANON §1.2 formula.**

---

## 0. Fingerprint gate

Every TZ header states the required revision string and the anchors below. The Executor compares
before doing any work; a mismatch is BLOCKED.

**Revision string:** `2026-09-12-c`

| anchor | value |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-open / 2-not-started` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` |
| `A6` — pricer | `18be5d185fee` |

Anchors are the first 12 hex characters of the SHA-256 of the named artifact, except `A3`.
`A5` is `research/recorder/recorder.py`, the code the live capture runs. `A6` is
`research/pfair.py`, the only implementation of the model: **any TZ that scores a pricer states
`A6`, so what was scored is never in doubt.**

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
| `research/pfair.py` | 233 | 9,844 | frozen | `18be5d185fee807fef9a840ab965dc42fa41c3a7a0b01b27c359afce96289676` |
| `research/selftest-pfair.py` | 221 | 10,939 | frozen | `f4b4f8287f3ebb0c9cbabaee40e87580bddab6d23ad0fe0e44aa87bc09bc3842` |
| `research/tz06-calibration.py` | 569 | 26,548 | frozen | `a6aaed94964775f34a9b26dba448ff0f998f32ad952e244bff834b67439ef123` |
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
every score this project will ever quote comes out of it.**

---

## 1. Repository

`github.com/seahomebatumi-ai/btc-5m-twap` — **public**. No dataset, archive or binary has ever
entered git history; the pack is under 300 KB and stays that way.

| path | contents |
|---|---|
| `CryptoTZ/` | specifications, Architect → Boss upload |
| `CryptoReports/` | reports, Executor → straight to `main` |
| `research/` | measurement code and the pricer, Executor → branch + PR |
| `research/recorder/` | live capture and its analyzer — six files, all on `main` |
| `engine/` | live engine — **does not exist yet** |
| root | `SYSTEM-MAP.md`, `BTC-EXECUTOR-INSTRUCTIONS.md`, `.gitignore` |

**Branches: none but `main`.** Every working branch is merged and deleted. The head of `main` is
never a gate; commits are named where they matter.

| pull request | head | disposition |
|---|---|---|
| PR #6 | `5ed667a` | the pricer, its calibration pipeline and R-c. **Merged 2026-09-12** into `main` at `4b3723a`, after the TZ-06 verdict. Branch deleted. |
| PR #5 | `4216c04` | Tier C and the SNTP repair. Merged 2026-09-12 at `c3dab7d`. |
| PR #4 | `0e13a5c` | the TZ-05 BLOCKED report. Closed. |
| PR #3 | `ee2f632` | the recorder and its analyzer, merged after the TZ-04b verdict |
| PR #1 | `d9e58e8` | TZ-03, the rename and the two deletions |

Commits still named by an artifact: `ea9290b` — the commit the dataset tag points at; `a772d19` —
TZ-02; `3895356` — the recorder commit TZ-04b scored; `4216c04` — the commit the capture runs;
`5ed667a` — the commit that first implemented the pricer.

**Tag:** `tz-01a-dataset` → `ea9290b92b9fa50c22d0560d5d01dfa392af44df`.

A read-only mirror of this map also sits in the Architect's project files. The repository copy is
the authority; the mirror is never edited and never quoted as state.

**Files on `main`:** eleven TZ files (`TZ-01` … `TZ-07`), eleven reports, six `research/` scripts, six
`research/recorder/` files, two governance files, `.gitignore`.

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
| `research/pfair.py` | **the pricer — the only implementation of the CANON §1.2 model, in any language.** Also the quantities it is fed: the merged stream, the time-weighted step-function mean, the one-second grid, the realised-sigma estimator. Imports its reader from `analyze.py` and carries no reader of its own. |
| `research/selftest-pfair.py` | its analytic self-tests — 56 model checks plus 18 machinery checks, each an assert, every fixed expectation taken at `K` near 100,000 |
| `research/tz06-calibration.py` | the Phase 1 pipeline: set formation, P, V1–V10, the gate tables. Carries no formula; calls `pfair.py` for every one. |
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
outside the repository and re-derivable from the pipeline.

---

## 4. What is validated, and by what

| claim | established by | status |
|---|---|---|
| the venue settles on a trailing-TWAP comparison — the 60-second feed at the close against the same feed at the open | TZ-04b V2: R1 agrees with the venue's resolved outcome on **200 of 200**, against a 199-of-200 gate fixed before any data was seen; re-run by TZ-06 R-c and reproduced exactly | **stands.** The only artifact here validated against a Polymarket settlement rule. |
| the interval-average reading is wrong, and so is the pre-August snapshot reading | TZ-04b V2: R2 175 of 200, R3 181 of 200; both reproduced by TZ-06 R-c | **stands.** Wrong on one interval in eight and one in ten — not near-misses. |
| the price to beat equals the settlement feed's reading at the open | TZ-04b V1 198 of 200; TZ-06 V3 **396 of 400**, median residual 3.78e-12 USD, worst 25.49 USD | **stands, with a ~1% failure rate every later result carries.** |
| the causal reading is genuinely causal | TZ-01a perturbation test; TZ-06 V4: 140 of 140 bit-identical under perturbation of the entire future, 140 of 140 negative controls move the model output | **stands.** |
| the oracle feed supports reconstructing the settlement average | TZ-06 P: the reconstructed close TWAP agrees in sign with the venue's outcome on **397 of 400**, against a floor of 396 fixed before any data was seen | **stands as a precondition.** Median absolute residual against the venue's own report `0.53` USD, worst `11.87`. |
| `p_fair` is not disqualified by the TZ-06 gate | TZ-06: G1 6 of 6, `Brier` 0.2107 … 0.0105 against 0.2496; G2 0 failing bins of 34 eligible | **stands as stated and for nothing more.** Phase 1 can only disqualify; it did not. |
| **`p_fair` is overconfident at `tau >= 120`** | Architect's audit of TZ-06's own tables: implied sd multiplier **1.50 / 1.36 / 1.30** at `tau` 240 / 180 / 120 and 1.08 / 1.04 / 0.93 at 90 / 60 / 30; at the three longest taus the lowest bin realises about three times the Up outcomes predicted and the top bin fewer; the joint statistic rejects calibration at those three taus | **stands as a finding, not as a gate result.** The statistic is post-hoc and closes nothing. TZ-08 tests it out of sample against a gate fixed in TZ-07a §8. |
| Tier C captures the book at seven checkpoints without loss | TZ-05a: 56 of 56 reads at HTTP 200, 4 of 4 `quotes_complete` | **stands as a deployment fact.** Not a market observation. |
| the collector was not modified between TZ-01a and TZ-02 | hash equality, `6c5089…` read from `origin/main` | **stands** |
| the sign of `D = p_interval − p_naive` has no preferred direction | TZ-02 measurement 1 | **stands, and is of no consequence** |
| the TWAP model beats the endpoint model · divergence is abundant · inversions are the rare tail | Gate B, Gate A2, TZ-02 | **WITHDRAWN** — all scored against §2.2 labels |

---

## 5. Phase state

| phase | question | state |
|---|---|---|
| 0 | is the settlement rule what the CANON §1.1 says it is? | **CLOSED 2026-09-11 — yes. TZ-04b: 200 of 200 against a 199-of-200 gate**, reproduced by TZ-06 R-c |
| 1 | is the corrected `p_fair` calibrated against true-rule labels? | **open.** TZ-06's gate passed and therefore did not disqualify; the Architect's audit then found scale miscalibration at `tau >= 120` that the gate was not built to see. **TZ-07a** measures the oracle feed's variance–time curve and freezes the corrected estimator — TZ-07 was BLOCKED at its fingerprint gate and did no work; **TZ-08** scores the estimator out of sample against the gate TZ-07a §8 fixes. |
| 2 | does the **market price** deviate from `p_fair`, and by how much? | not started — the decision point. Tier C is accumulating the input; nothing has been read. |
| 3 | is the deviation capturable after fee, spread, depth, 50 ms taker delay, oracle basis? | not started |
| 4 | live, minimum size, fixed loss limit | not started |

**This project has a pricer whose settlement variable is correctly identified, whose calibration
is confirmed at `tau <= 90` and rejected at `tau >= 120`, and no known edge.** Phases 0 and 1
could only ever disqualify.

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
| **maker incentives, read from the venue's documentation 2026-09-12** | makers pay no fee; the measured `rebateRate` `0.2` is a share of the taker fee paid on a fill. Separately the venue runs a liquidity-rewards programme that pays for resting orders near the midpoint whether or not they fill, scored quadratically in distance and linearly in size, sampled once a minute. Per-market configuration is published in the Gamma market document as `rewards.rewardsMinSize`, `rewards.rewardsMaxSpread` and `clobRewards[].rewardsDailyRate`. **Our own `gamma.json` captures hold these fields for every interval since 2026-09-10 and none has been read.** |
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
| 12 | **`analyze.py:207` aborted every run** after the TZ-05a restart, killing the instrument behind the Phase 0 count. | **closed by TZ-06 R-c, merged.** The span is now bounded by the next start record instead of denying one exists, `within_span` is asserted per scored interval, and the repaired analyzer reproduces TZ-04b on every count — 215 / 200 / 15 / 200 / 175 / 181. |
| 13 | The TZ-05a report's exclusion line gives the wrong window-opening time for `1789206600`. | closed by rule: membership is re-derived by the Architect from epochs rather than read from the report. |
| 14 | TZ-05a carries two sections numbered `## 7`. | closed by rule: section numbers are asserted unique in the pre-delivery change list. |
| 15 | **TZ-06's calibration gate was marginal only** — a per-bin interval with a two-bin allowance cannot see a coherent one-sided pattern, and it passed a pricer whose sd is understated by half at `tau = 240`. Architect's defect. | open until TZ-08 scores against the replacement. Repaired by rule: **every calibration gate carries a scale statistic and a shape statistic, both fixed before any data is seen.** TZ-07a §8 fixes both for TZ-08. |
| 16 | **TZ-06 §3 and §4 pull in opposite directions for 25 of the 400 members**: §3 forbids carrying a value across a recorded disconnect, §4 makes only the interval's own manifest a condition, and the run-up window is covered by the preceding directory. The step function was read across those gaps. | open. Resolved by TZ-07a M6: an increment whose span contains a recorded disconnect is excluded from every variance estimate and counted. |
| 17 | **`analyze.py`'s `V5_determinism` fell from 215 of 215 to 0 of 215.** Rebuilding a 2026-09-10 manifest with today's `manifest.py` adds the two keys TZ-05a introduced; every field the old manifests carry rebuilds identically. | open. Repaired by rule in the next TZ that touches `analyze.py`: a determinism check compares a rebuild against a rebuild, never against an artifact written under an older schema. |

| 18 | **`SYSTEM-MAP.md` on `main` was replaced by a chat message.** Commit `891d161` overwrote the 314-line map with the seventeen-line upload note, so revision `2026-09-12-b` never existed in the repository and TZ-07's fingerprint gate had nothing to read. | closed by rule: **after every upload the Architect reads `origin/main` and confirms the file that landed before `EXECUTE` is sent.** The check costs one turn; the failure costs an Executor run. TZ-07 blocked correctly and did no work. |

---

## 8. What does not exist yet

No corrected volatility estimator, no order-book history beyond the seven-checkpoint snapshots
accumulating unread, no Polymarket client code, no execution path, no capital at risk. Nothing in
this repository can place an order. The recorder reads; it cannot write to any venue.

The pricer exists and has been scored once, against 400 labels the venue itself produced. The
recorder is running on `4216c04` with both tiers. Between them they have produced two conclusions
— the Phase 0 answer and the Phase 1 finding — and one deployment proof.
