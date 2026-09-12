# SYSTEM MAP — btc-5m-twap

**Revision 2026-09-12-a.** Written by the Architect; the Executor never edits it. This is a
**state** document: what exists right now. It holds no mission, no rules and no history.

- The CANON (Architect's project instructions, not in this repository) holds the mission, the
  fair-value model, the measured facts and the phase gates.
- `BTC-EXECUTOR-INSTRUCTIONS.md` holds how the Executor works.
- **This map never restates a CANON §1.2 formula.**

---

## 0. Fingerprint gate

Every TZ header states the required revision string and the anchors below. The Executor compares
before doing any work; a mismatch is BLOCKED.

**Revision string:** `2026-09-12-a`

| anchor | value |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-open / 2-not-started` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` |

Anchors are the first 12 hex characters of the SHA-256 of the named artifact, except `A3`.
`A5` is `research/recorder/recorder.py`, the code the live capture runs.

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
| `research/recorder/recorder.py` | 608 | 25,658 | frozen | `9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03` |
| `research/recorder/config.py` | 112 | 4,773 | frozen | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` |
| `research/recorder/manifest.py` | 254 | 10,002 | frozen | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` |
| `research/recorder/probe.py` | 227 | 9,324 | frozen | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` |
| `research/recorder/analyze.py` | 788 | 33,323 | frozen | `5bade9ff56669f2c862f81e98af1050b53233d2b07e3c260e04bf64233c03230` |
| `research/recorder/selftest.py` | 516 | 27,693 | frozen | `3678c0b4f95a063c5b44c18eb13cdedc6e9adbee3afc6adab0884de615b09cbb` |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` |

Hashes are of the file as committed on `main` at revision date, verified by the Architect against
`origin/main` — not copied from a report. Changing a `frozen` row requires a TZ that authorizes
it and a new map revision. **The six recorder files are frozen because the live capture runs
them**: an unauthorized edit is a change to a running instrument.

---

## 1. Repository

`github.com/seahomebatumi-ai/btc-5m-twap` — **public**. No dataset, archive or binary has ever
entered git history; the pack is under 300 KB and stays that way.

| path | contents |
|---|---|
| `CryptoTZ/` | specifications, Architect → Boss upload |
| `CryptoReports/` | reports, Executor → straight to `main` |
| `research/` | measurement code, Executor → branch + PR |
| `research/recorder/` | live capture and its analyzer — six files, all on `main` |
| `engine/` | live engine — **does not exist yet** |
| root | `SYSTEM-MAP.md`, `BTC-EXECUTOR-INSTRUCTIONS.md`, `.gitignore` |

**Branches: none but `main`.** Every working branch has been merged and deleted. The head of
`main` is never a gate; commits are named where they matter.

| pull request | head | disposition |
|---|---|---|
| PR #5 | `4216c04` | Tier C and the SNTP repair. **Merged 2026-09-12** into `main` at `c3dab7d`, after the TZ-05a verdict. Branch deleted. |
| PR #4 | `0e13a5c` | the TZ-05 BLOCKED report. Closed; its branch `claude/gifted-hawking-22knfr` deleted 2026-09-12. |
| PR #3 | `ee2f632` | the recorder and its analyzer, merged after the TZ-04b verdict |
| PR #1 | `d9e58e8` | TZ-03, the rename and the two deletions |

Commits still named by an artifact: `ea9290b` — the commit the dataset tag points at; `a772d19` —
TZ-02; `3895356` — the recorder commit TZ-04b scored; `4216c04` — the commit the capture now runs.

**Tag:** `tz-01a-dataset` → `ea9290b92b9fa50c22d0560d5d01dfa392af44df`.

A read-only mirror of this map also sits in the Architect's project files. The repository copy is
the authority; the mirror is never edited and never quoted as state.

**Files on `main`:** nine TZ files (`TZ-01` … `TZ-05a`), nine reports, three `research/` scripts,
six `research/recorder/` files, two governance files, `.gitignore`.

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
the superseded `p_interval` model and the `outcome_*` columns are invalid labels — see §2.2.

**The two sigma variants**, both carried through every measurement:

- `sigma_pre` — from the 30 one-minute bars **before** the interval open, per-second dollars,
  fixed for the interval.
- `sigma_live` — from a 1-second window: 300 seconds of run-up plus the bars already closed
  inside the interval. Causal, and it moves as the interval runs.

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

Correct labels are the venue's own resolutions, captured per interval as `resolution.json` and
already read once by TZ-04b.

### 2.3 Live capture — two tiers running, almost entirely unread

**Tier A** has been capturing since **2026-09-10 10:21:09 UTC**, into `/var/lib/btc-recorder/**`
on the VPS — outside the repository, never in git history. Streams, one gzipped file per interval:
`twap60`, `twap30`, `chainlink`, `binance`, plus `gamma.json` (S6, the market document at
`T0 + 5`), `resolution.json` (S7, the venue's settled document), `runtime.jsonl` and
`manifest.json`. Reports carry the venue payload's own `timestamp` in milliseconds and
`full_accuracy_value` at full precision; the manifest is a pure function of the directory.

**Tier C** — seven order-book snapshots per interval per token id, fourteen reads, at
`tau ∈ {240, 180, 120, 90, 60, 30, 10}` — was added **2026-09-12 09:53:05 UTC** on commit
`4216c04`, pid `228592`. It stores each reply verbatim with its HTTP status in
`quotes.jsonl.gz`, and the manifest gained `quotes_complete` and `quote_offsets_ms`, both
independent of `complete`. The Tier B order-book probe ran once, for 60 minutes, and retained
exactly one interval.

**What has been read.** TZ-04b read the first 215 intervals from the Tier A start record — T0
`1789035900` to `1789100100` — in order; 200 were `complete`, carried a venue resolution, and
formed the Phase 0 scoring set. All 15 non-members failed on `disconnect`. TZ-05a read the four
intervals `1789206900`–`1789207800` for deployment proof only: 56 of 56 reads at HTTP 200, 4 of 4
`quotes_complete`, 4 of 4 manifests rebuilding byte-identically. **No quote has been aggregated
and no market statistic has ever been computed.** Everything else in the capture is unread.

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

### 2.4 What is not in the data

**Nothing in the repository is market data**: there is no Chainlink tick, no Polymarket quote, no
order-book depth, no fill and no fee-paid figure in git history, and there never will be.

On the host, oracle data and order-book snapshots now both exist. **No aggregation of either has
been performed.** Every measurement scored to date compares the Architect's models against either
withdrawn labels (§2.2) or, for TZ-04b, the venue's own resolutions.

---

## 3. Code

| file | role |
|---|---|
| `research/twap-divergence.py` | the collector. Downloads and verifies the monthly archives, walks the 1-second bars, writes one row per checkpoint. The only implementation of the superseded `p_interval` arithmetic, in `checkpoint_quantities`; it reads no bars itself, so the causal reading and the superseded TZ-01 reading share one implementation and differ only in which bars they are handed. |
| `research/selftest-twap-divergence.py` | its analytic self-tests |
| `research/tz02-distribution.py` | aggregation over the observation set. Reads the Parquet columns only; contains no `erf`, `norm`, `sqrt` or sigma arithmetic. |
| `research/recorder/recorder.py` | the live capture, Tier A and Tier C in one process. Read-only: no order path, no CLOB authentication, no credential, no pricing arithmetic. |
| `research/recorder/config.py` | every constant the capture uses, each traced to the TZ that fixed it |
| `research/recorder/manifest.py` | the per-interval manifest, a pure function of the interval directory |
| `research/recorder/analyze.py` | the TZ-04b analyzer and the only stream reader — `reports`, `last_at_or_before`, `first_at_or_after`, `venue`, `published_equal`, `scoring_set`. **Currently cannot run: §7 item 12.** |
| `research/recorder/probe.py` | the Tier B order-book probe, run once |
| `research/recorder/selftest.py` | the recorder's self-tests — 105 asserts, each aborting the run |

**There is no implementation of the current CANON §1.2 pricer anywhere.** Everything in
`research/` implements the superseded reading. The first implementation is TZ-06's.

Outputs go to `research/out/**`, git-ignored except `twap-divergence-summary.md` and
`twap-divergence-contamination.md`. `research/out/tz02-summary.md` is ignored.
`/root/tz01-out-archive/` holds the superseded TZ-01 output — present, untouched, never read.

---

## 4. What is validated, and by what

| claim | established by | status |
|---|---|---|
| the venue settles on a trailing-TWAP comparison — the 60-second feed at the close against the same feed at the open | TZ-04b V2: R1 agrees with the venue's resolved outcome on **200 of 200**, against a 199-of-200 gate fixed before any data was seen | **stands.** The only artifact here validated against a Polymarket settlement rule. |
| the interval-average reading is wrong, and so is the pre-August snapshot reading | TZ-04b V2: R2 175 of 200, R3 181 of 200 | **stands.** Wrong on one interval in eight and one in ten — not near-misses. |
| the price to beat equals the settlement feed's reading at the open | TZ-04b V1: 198 of 200 as a double against the venue's published `priceToBeat`; median residual 3.6e-12 USD, worst 3.65 USD | **stands, with a ~1% failure rate every later result carries.** |
| the causal reading is genuinely causal | TZ-01a perturbation test: 22,500 comparisons bit-identical, 7,500 negative controls all moved | **stands.** The methodology is reused unchanged. |
| Tier C captures the book at seven checkpoints without loss | TZ-05a: 56 of 56 reads at HTTP 200 over four intervals, 4 of 4 `quotes_complete`, offsets 43.977–101.448 ms against a 20 s slot | **stands as a deployment fact.** It is not a market observation and supports no market claim. |
| the collector was not modified between TZ-01a and TZ-02 | hash equality, `6c5089…` read from `origin/main` | **stands** |
| the sign of `D = p_interval − p_naive` has no preferred direction | TZ-02 measurement 1: 49.6% / 50.3% over 1,051,170 observations | **stands, and is now of no consequence** |
| the TWAP model beats the endpoint model | Gate B, Brier 0.0781 vs 0.1145 | **WITHDRAWN** — scored against §2.2 labels |
| divergence is abundant at money-relevant size | Gate A2, 171.492 events/day | **WITHDRAWN** — a gap between two models, one of which prices a quantity the venue does not settle on |
| inversions are the rare tail — 86 and 137 over 730 days | TZ-02 | **WITHDRAWN** as a claim about the market; reproducible as a fact about two models |

**No pricer has ever been scored against a venue-resolved label.** TZ-06 is the first that will be.

---

## 5. Phase state

| phase | question | state |
|---|---|---|
| 0 | is the settlement rule what the CANON §1.1 says it is? | **CLOSED 2026-09-11 — yes. TZ-04b: 200 of 200 against a 199-of-200 gate** |
| 1 | is the corrected `p_fair` calibrated against true-rule labels? | **open — TZ-06 issued 2026-09-12, gate stated in that file before any data was seen** |
| 2 | does the **market price** deviate from `p_fair`, and by how much? | not started — the decision point. Tier C is accumulating the input; nothing has been read. |
| 3 | is the deviation capturable after fee, spread, depth, 50 ms taker delay, oracle basis? | not started |
| 4 | live, minimum size, fixed loss limit | not started |

**This project has a pricer whose settlement variable is correctly identified but not yet
validated against it, and no known edge.** Phases 0 and 1 could only ever disqualify.

---

## 6. Environment

| item | value |
|---|---|
| host | Vultr VPS (Warsaw); the Executor runs Claude Code CLI **on the VPS itself**. A cloud Claude Code session is not this host and cannot execute anything that touches the capture. |
| **host identity, for TZ host gates** | `/var/lib/btc-recorder/` exists and holds interval directories · the recorder process is running and the newest `runtime.jsonl` start record carries sha `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` · the filesystem holding it is `/dev/vda2`, total `31,612,203,008` bytes. All three, or it is not the capture host. |
| language | Python 3.12 |
| stack | Parquet storage, pandas/pyarrow, DuckDB for aggregation |
| auth | CLI subscription auth; `ANTHROPIC_API_KEY` must not be set |
| git remote | HTTPS with the repository token embedded in the remote URL |
| egress, **verified 2026-09-12** | DNS and TCP/443 open to `ws-live-data.polymarket.com`, `gamma-api.polymarket.com`, `clob.polymarket.com`, `ws-subscriptions-clob.polymarket.com`, `docs.polymarket.com`. Anonymous only; no credentials of any kind are held. |
| **disk, measured 2026-09-12** | one writable filesystem `/dev/vda2`, total `31,612,203,008` bytes, free `7,855,497,216`. `/var/lib`, `/root` and `/var/www` are all on it. **Any TZ that states a resource floor states it in exact bytes and derives it from this row.** |
| **capture cost, measured** | Tier A + Tier C `23,850,461` bytes/day against a `2,000,000,000` byte floor — headroom `5,855,497,216` bytes, about **245 days**. Neither floor is near. |
| **price to beat** | published by Gamma only after settlement, at `events[0].eventMetadata.priceToBeat`, and captured per interval in `resolution.json`. Not available before the close; a live pricer reconstructs it from the feed. |
| **resolution endpoint** | `GET https://gamma-api.polymarket.com/markets/slug/btc-updown-5m-{T0}`, polled from `T0+333` every 15 s |
| **CLOB websocket** | `wss://ws-subscriptions-clob.polymarket.com/ws/market` |
| **CLOB order book, REST** | `GET https://clob.polymarket.com/book?token_id={token_id}` — public, unauthenticated, read on 2026-09-12 from `docs.polymarket.com/api-reference/market-data/get-order-book` |
| **venue constants, measured TZ-05a** | minimum tick size `0.01`, agreeing across `orderPriceMinTickSize` (Gamma), `tick_size` (`/book`) and `minimum_tick_size` (`/markets/{condition_id}`) · minimum order size `5` · fee schedule `{"exponent": 1, "rate": 0.07, "rebateRate": 0.2, "takerOnly": true}`, `feeType` `crypto_fees_v2` · outcome mapping resolved from `tokens[].outcome`, not from array position |
| host is shared | unrelated production services live on the same filesystem — `crypto-auto`, `my_real_estate_bot`, `seahome_webapp.git`, `/var/www`, `/var/log`. The recorder never deletes anything it did not write. |
| capture path | `/var/lib/btc-recorder/**` — outside the repository by design, so no capture can reach git history |
| **RTDS session limit, measured 2026-09-10** | the server closes every websocket `7,200` s after it opens, `1001 Going away`, timer restarting on each new connection. Undocumented. **No TZ may require an unbroken socket for longer than this.** |
| clock | NTP-disciplined; SNTP replies are validated at reception since `4216c04`. Maximum absolute offset measured over the TZ-05a window: `18.789` ms. An offset above 50 ms invalidates a latency claim; it is not a membership condition for anything. |
| **sandbox limit — network** | calls that read the git token and send it to `api.github.com` are refused. `git` push/pull work. Release creation and asset upload cannot be done from inside the session — hand the upload to the Boss and verify by anonymous download. |
| **sandbox limit — process signals** | `kill` is refused by the permission classifier, alone or inside a compound command. **Any TZ that must restart the recorder hands the Boss two exact commands** and verifies the outcome from `runtime.jsonl`, `ps` and the log rather than from his report. |

Not yet decided by any TZ and therefore not present: systemd units, the Parquet decision journal,
capture retention policy, any deployment.

---

## 7. Open defects

| # | defect | disposition |
|---|---|---|
| 1 | `research/tz02-distribution.py` records the collector-hash comparison into `checks["collector_sha_matches"]` but never asserts it. The run completes on a mismatch. | open. Fix in the next TZ that touches that file; do not edit the committed report. |
| 2 | The TZ-02 report was amended after commit (`356c29a`). Verified to touch no measurement, table or verdict. | closed by rule: contract §3.2 and §5.2. Both versions stay in history. |
| 3 | The TZ-02 implementation commit `f8a0c37` (1,850 lines) reached `main` without a merge and without a verdict. | closed by rule: contract §4.1 and the §4.2 self-check. `main` is left as it is. |
| 4 | The Executor contract carried a space before its extension and both governance files were duplicated inside `research/`. | closed by TZ-03, PR #1. Deleted blobs stay in history at `76d4d9f`. |
| 5 | **The settlement mechanic was wrong from inception.** Every label and every calibration score in the repository was built on the wrong rule. | CANON replaced, labels withdrawn (§2.2), Phases 0 and 1 reopened. **The class is closed by TZ-04b V2**, not by this entry. |
| 6 | **TZ-04 §4 set a 20 GB free-space floor written from assumption**, true before the first frame, so the proving run could never begin. | closed by rule: §6 carries the host's measured capacity and every resource floor is stated in exact bytes derived from it. |
| 7 | Two executions of TZ-04 wrote two different reports to one path. | closed by rule: a re-execution never reuses a report path. Both versions stay in history. |
| 8 | **TZ-04a §6 required 200 *consecutive* complete intervals** across a socket the venue closes every 7,200 s; the ceiling is 23. | closed by rule: a requirement is a count of qualifying units, never an unbroken run across a third-party boundary. |
| 9 | **The V4 read-only proof was a bad instrument** — it matched its own regex and three docstrings that deny the capability, so it could never reach zero. | **closed by TZ-05a R-a and by ruling.** The instrument now excludes the file holding the pattern and returns 3, all three prose denials, unchanged before and after the TZ. Ruling: a text search cannot prove the absence of a capability. The standing carrier of the claim is the merge-base diff plus the absence of any CLOB auth path, both re-verified at merge. |
| 10 | **The recorder's SNTP client accepted invalid replies** — NTP-era transmit timestamps dominated the offset statistics and spuriously flagged 6 intervals over 50 ms. | **closed by TZ-05a R-b, merged.** Leap indicator 3, stratum 0 or above 15, a zero transmit timestamp and a skew beyond `86,400` s are rejected at reception and counted per server. Twelve self-tests, including a reconstruction of the exact observed reply, reproduced independently by the Architect. Live rejections over the 22-minute proving window: zero — a longer window belongs to whichever TZ next reads the clock. |
| 11 | **TZ-05 could not be executed in one session on any host**, and was triggered in a cloud container. | closed by TZ-05a and by CANON hard rule 11; every TZ touching the capture now carries a host gate derived from §6. |
| 12 | **`research/recorder/analyze.py:207` now aborts every run.** It asserts that no start record follows the `3895356` start; the TZ-05a restart made that false. The TZ-04b analysis — the sole instrument behind the 200-of-200 Phase 0 count — can no longer be re-run, though every input remains on disk. | open. Repaired by TZ-06 R-c: the analysis anchors on the identity of its own start record and bounds its span at the next one, instead of asserting that none exists. Acceptance is exact reproduction of the TZ-04b counts. |
| 13 | The TZ-05a report's exclusion line gives `1789206600`'s window as opening at 09:58:30; it opens at 09:48:30 — the second member's time was transcribed into it. | closed by rule: the report is immutable, and set membership is re-derived by the Architect from epochs rather than read from the report. Membership was re-derived and is correct. |
| 14 | TZ-05a carries two sections numbered `## 7`. Architect's defect. | closed by rule: section numbers are asserted unique in the pre-delivery change list, alongside the revision string. |

---

## 8. What does not exist yet

No pricer implementing the current model, no order-book history beyond the seven-checkpoint
snapshots now accumulating, no Polymarket client code, no execution path, no capital at risk.
Nothing in this repository can place an order. The recorder reads; it cannot write to any venue.

The recorder exists, is merged, and is running on `4216c04` with both tiers. It has produced
exactly one conclusion — the Phase 0 answer — and one deployment proof. Everything else it holds
is unread.
