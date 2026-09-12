# SYSTEM MAP — btc-5m-twap

**Revision 2026-09-11-b.** Written by the Architect; the Executor never edits it. This is a
**state** document: what exists right now. It holds no mission, no rules and no history.

- The CANON (Architect's project instructions, not in this repository) holds the mission, the
  fair-value model, the measured facts and the phase gates.
- `BTC-EXECUTOR-INSTRUCTIONS.md` holds how the Executor works.
- **This map never restates a CANON §1.2 formula.**

---

## 0. Fingerprint gate

Every TZ header states the required revision string and the anchors below. The Executor compares
before doing any work; a mismatch is BLOCKED.

**Revision string:** `2026-09-11-b`

| anchor | value |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-open / 2-not-started` |
| `A4` — executor contract | `437b45ea196b` |

Anchors are the first 12 hex characters of the SHA-256 of the named artifact, except `A3`.

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
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` |

Hashes are of the file as committed on `main` at revision date, verified by the Architect against
`origin/main` — not copied from a report. Changing a `frozen` row requires a TZ that authorizes
it and a new map revision.

---

## 1. Repository

`github.com/seahomebatumi-ai/btc-5m-twap` — **public**. No dataset, archive or binary has ever
entered git history; the pack is under 300 KB and stays that way.

| path | contents |
|---|---|
| `CryptoTZ/` | specifications, Architect → Boss upload |
| `CryptoReports/` | reports, Executor → straight to `main` |
| `research/` | measurement code, Executor → branch + PR |
| `research/recorder/` | live capture and its analyzer — six files, on `main` since PR #3 |
| `engine/` | live engine — **does not exist yet** |
| root | `SYSTEM-MAP.md`, `BTC-EXECUTOR-INSTRUCTIONS.md`, `.gitignore` |

**Branches**

| branch | head | state |
|---|---|---|
| `main` | — | moves with every report; the head is never a gate |
| `tz-04b-market-recorder` | `ee2f632` | the recorder and its analyzer. Merged by PR #3 after the TZ-04b verdict. `tz-04a-market-recorder` was closed unmerged and deleted. |
| `tz-03-repo-hygiene` | `d9e58e8` | merged by PR #1 — the rename and the two deletions |
| `tz-02-divergence-distribution` | `a772d19` | contained in `main`; nothing to merge |
| `tz-01a-twap-divergence-corrected` | `ea9290b` | the commit the dataset tag points at |
| `tz-01-twap-divergence` | — | superseded, kept for forensics |

**Tag:** `tz-01a-dataset` → `ea9290b92b9fa50c22d0560d5d01dfa392af44df`.

A read-only mirror of this map also sits in the Architect's project files. The repository copy is
the authority; the mirror is never edited and never quoted as state.

**Files on `main`:** eight TZ files (`TZ-01` … `TZ-04b`, `TZ-05`), seven reports, three
`research/` scripts, six `research/recorder/` files, `.gitignore`.

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

Correct labels require either the venue's own resolution (TZ-04 S7, forward only) or a
recomputation of the true rule's shape over the Binance bars (TZ-05, a proxy, and named as one).

### 2.3 Live capture — running, unread

Tier A of the recorder has been capturing since **2026-09-10 10:21:09 UTC** on commit `3895356`,
into `/var/lib/btc-recorder/**` on the VPS — outside the repository, never in git history. Streams:
the Chainlink 60-second and 30-second TWAP feeds, the non-TWAP Chainlink feed, the Binance
cross-check feed, market metadata and venue resolutions. The Tier B order-book probe ran once, for
60 minutes, and retained exactly one interval.

**Read once, by TZ-04b.** The first 215 intervals from the start record — T0 `1789035900` to
`1789100100` — were disclosed in order; 200 were `complete`, carried a venue resolution, and formed
the Phase 0 scoring set. All 15 non-members failed on `disconnect`. Eleven disconnects touched the
span: seven venue closes at ~7,200 s, two 30-second receive timeouts, two connection losses with no
close frame. Nothing else in the capture has been read, scored or aggregated.

**Measured footprint, TZ-04b V7.** Tier A costs `76,643` bytes per interval on disk, `22,073,069`
per day. The Tier B order book, captured continuously, would cost `1,913,827,421` bytes per day
compressed and `19,764,344,212` raw — which is why it is not. Venue resolution reaches the recorder
a median of `318` s after interval close; the venue's own `closedTime` is a median of `55` s.

### 2.4 What is not in the data

**No oracle data. No market data.** There is no Chainlink tick, no Polymarket quote, no
order-book depth, no fill and no fee-paid figure anywhere in this repository. Everything measured
to date compares two of the Architect's own models against labels that match no venue rule.

---

## 3. Pipeline

| file | role |
|---|---|
| `research/twap-divergence.py` | the collector. Downloads and verifies the monthly archives, walks the 1-second bars, writes one row per checkpoint. The only implementation of the superseded `p_interval` arithmetic, in `checkpoint_quantities`; it reads no bars itself, so the causal reading and the superseded TZ-01 reading share one implementation and differ only in which bars they are handed. |
| `research/selftest-twap-divergence.py` | its analytic self-tests |
| `research/tz02-distribution.py` | aggregation over the observation set. Reads the Parquet columns only; contains no `erf`, `norm`, `sqrt` or sigma arithmetic. |

Outputs go to `research/out/**`, git-ignored except `twap-divergence-summary.md` and
`twap-divergence-contamination.md`. `research/out/tz02-summary.md` is ignored.
`/root/tz01-out-archive/` holds the superseded TZ-01 output — present, untouched, never read.

---

## 4. What is validated, and by what

| claim | established by | status |
|---|---|---|
| the venue settles on a trailing-TWAP comparison — the 60-second feed at the close against the same feed at the open | TZ-04b V2: R1 agrees with the venue's resolved outcome on **200 of 200**, against a 199-of-200 gate fixed before any data was seen | **stands.** The first artifact here validated against a Polymarket settlement rule. |
| the interval-average reading is wrong, and so is the pre-August snapshot reading | TZ-04b V2: R2 175 of 200, R3 181 of 200 | **stands.** Wrong on one interval in eight and one in ten — not near-misses. |
| the price to beat equals the settlement feed's reading at the open | TZ-04b V1: 198 of 200 as a double against the venue's published `priceToBeat`; median residual 3.6e-12 USD, worst 3.65 USD | **stands, with a ~1% failure rate every later result carries.** V1 is `unresolved` as the TZ worded it — no pre-settlement field carries the number. |
| the causal reading is genuinely causal | TZ-01a perturbation test: 22,500 comparisons bit-identical, 7,500 negative controls all moved | **stands.** The methodology is reused unchanged. |
| the collector was not modified between TZ-01a and TZ-02 | hash equality, `6c5089…` read from `origin/main` | **stands** |
| the sign of `D = p_interval − p_naive` has no preferred direction | TZ-02 measurement 1: 49.6% / 50.3% over 1,051,170 observations, every `tau`, both variants | **stands, and is now of no consequence** |
| the TWAP model beats the endpoint model | Gate B, Brier 0.0781 vs 0.1145 | **WITHDRAWN** — scored against §2.2 labels |
| divergence is abundant at money-relevant size | Gate A2, 171.492 events/day | **WITHDRAWN** — a gap between two models, one of which prices a quantity the venue does not settle on |
| inversions are the rare tail — 86 and 137 over 730 days | TZ-02 | **WITHDRAWN** as a claim about the market; reproducible as a fact about two models |

**Nothing in this repository is currently validated against a Polymarket settlement rule.** The
first artifact that will be is the TZ-04 V2 count.

---

## 5. Phase state

| phase | question | state |
|---|---|---|
| 0 | is the settlement rule what the CANON §1.1 says it is? | **CLOSED 2026-09-11 — yes. TZ-04b: 200 of 200 against a 199-of-200 gate** |
| 1 | is the corrected `p_fair` calibrated against true-rule labels? | **open — TZ-06, not yet written** |
| 2 | does the **market price** deviate from `p_fair`, and by how much? | not started — the decision point |
| 3 | is the deviation capturable after fee, spread, depth, 50 ms taker delay, oracle basis? | not started |
| 4 | live, minimum size, fixed loss limit | not started |

**This project has a pricer whose settlement variable is now correctly identified but not yet
validated against it, and no known edge.** Phases 0 and 1 could only ever disqualify.

---

## 6. Environment

| item | value |
|---|---|
| host | Vultr VPS (Warsaw); the Executor runs Claude Code CLI on the VPS itself |
| language | Python 3.12 |
| stack | Parquet storage, pandas/pyarrow, DuckDB for aggregation |
| auth | CLI subscription auth; `ANTHROPIC_API_KEY` must not be set |
| git remote | HTTPS with the repository token embedded in the remote URL |
| egress, **verified 2026-09-10** | DNS resolves and TCP/443 is open to `ws-live-data.polymarket.com`, `gamma-api.polymarket.com`, `clob.polymarket.com`, `ws-subscriptions-clob.polymarket.com`; anonymous `GET /markets?limit=1` on Gamma returned HTTP 200. No credentials of any kind. |
| **disk, measured 2026-09-11 17:45 UTC** | one writable filesystem `/dev/vda2`, total `31,612,203,008` bytes, free `8,489,132,032`. `/var/lib`, `/root` and `/var/www` are all on it. **Any TZ that states a resource floor states it in exact bytes and derives it from this row.** |
| **capture cost, measured** | Tier A `22,073,069` bytes/day. Full order book `1,913,827,421` bytes/day compressed — 4.4 days of headroom, so it is never captured continuously on this host. |
| **price to beat** | published by Gamma only after settlement, at `events[0].eventMetadata.priceToBeat`. Not available before the close; a live pricer reconstructs it from the feed. |
| **resolution endpoint** | `GET https://gamma-api.polymarket.com/markets/slug/btc-updown-5m-{T0}`, polled from `T0+333` every 15 s |
| **CLOB websocket** | `wss://ws-subscriptions-clob.polymarket.com/ws/market` |
| host is shared | unrelated production services live on the same filesystem — `crypto-auto`, `my_real_estate_bot`, `seahome_webapp.git`, `/var/www`, `/var/log`. The recorder never deletes anything it did not write. |
| capture path | `/var/lib/btc-recorder/**` — outside the repository by design, so no capture can reach git history |
| **RTDS session limit, measured 2026-09-10** | the server closes every websocket `7,200` s after it opens, `1001 Going away`, timer restarting on each new connection. Undocumented. **No TZ may require an unbroken socket for longer than this.** |
| clock | NTP-disciplined; offset is reported, and > 50 ms invalidates latency claims |
| **sandbox limit** | calls that read the git token and send it to `api.github.com` are refused. `git` push/pull work. Release creation and asset upload cannot be done from inside the session — hand the upload to the Boss and verify by anonymous download. |

Not yet decided by any TZ and therefore not present: systemd units, the Parquet decision journal,
capture retention policy, any deployment.

---

## 7. Open defects

| # | defect | disposition |
|---|---|---|
| 1 | `research/tz02-distribution.py` records the collector-hash comparison into `checks["collector_sha_matches"]` but never asserts it. The run completes on a mismatch. | the guard does not exist. Fix in the next TZ that touches that file; do not edit the committed report. |
| 2 | The TZ-02 report was amended after commit (`356c29a`). Verified to touch no measurement, table or verdict. | closed by rule: `BTC-EXECUTOR-INSTRUCTIONS.md` §3.2 and §5.2. Both versions stay in history. |
| 3 | The TZ-02 implementation commit `f8a0c37` (1,850 lines) reached `main` without a merge and without a verdict. | closed by rule: `BTC-EXECUTOR-INSTRUCTIONS.md` §4.1 and the §4.2 self-check. `main` is left as it is. |
| 4 | The Executor contract carried a space before its extension and both governance files were duplicated inside `research/`; the duplicated map was revision `2026-09-10-a`, 25 lines adrift. | closed by TZ-03, PR #1: contract renamed with blob identity preserved, both duplicates deleted, `git ls-files \| grep -c " "` now `0`. Deleted blobs stay in history at `76d4d9f`. |
| 5 | **The settlement mechanic was wrong from inception.** CANON §1.1 stated resolution as an average over the whole interval; the venue compares two readings of a Chainlink trailing-TWAP feed, and before 2026-08-07 compared a single close against a single open. Every label and every calibration score in the repository was built on the wrong rule. | CANON replaced (revision `2026-09-10-b`), labels withdrawn (§2.2), Phases 0 and 1 reopened. Closed by rule: the CANON now requires a venue mechanic to be established by measurement against resolved outcomes, and bars any label built from the Architect's reading of a rule. **The class is closed by TZ-04 V2, not by this entry.** |
| 6 | **TZ-04 §4 set a 20 GB free-space floor written from assumption.** The capture host has 9,620,611,072 bytes free of 31,612,203,008 on its only writable filesystem, so the stop condition was true before the first frame and the §6 proving run could never begin. The unit was also ambiguous — decimal or binary was never stated. | TZ-04 superseded by TZ-04a; TZ-04 stays committed and unedited. Closed by rule: §6 of this map now carries the host's measured capacity, and every resource floor is stated in exact bytes derived from it. Reported by the Executor, not found in production. |
| 7 | Two executions of TZ-04 wrote two different reports to `CryptoReports/TZ-04-market-recorder-report.md`. The first survives only in git history at `28e4444`. | closed by rule: a re-execution never reuses a report path. A correction carries a new TZ number and therefore a new report path — `TZ-04a-…-report.md`. Both versions stay in history. |
| 8 | **TZ-04a §6 required a scoring set of 200 *consecutive* complete intervals**, across a socket the venue closes every 7,200 s. The ceiling is 23, so the set could never form. | TZ-04a superseded by TZ-04b: `consecutive` deleted, the set redefined as the first 200 qualifying members, the 199-of-200 gate carried across word for word before any score existed. Closed by rule: a requirement is a count of qualifying units, never an unbroken run across a third-party boundary. |
| 9 | **The V4 read-only proof is a bad instrument.** It returns 5 matching lines: two are the regex itself, held in the analyzer that runs the grep, and three are docstring sentences that *deny* the capability. It cannot reach zero however read-only the code is. | open. The substantive claim is carried instead by the merge-base diff and by the absence of any CLOB auth path. TZ-05 W5 replaces the instrument: the file holding the pattern is excluded and the match is on code tokens, not prose. The committed TZ-04b report is not edited. |
| 10 | **The recorder's SNTP client accepts an invalid reply.** Three `pool.ntp.org` replies carried NTP-era-origin transmit timestamps; with no stratum, leap-indicator or zero-timestamp check they dominated the offset statistics and spuriously flagged 6 intervals over 50 ms. | open, and it does not touch V1/V2, which read venue payload timestamps rather than the local clock. The host's own server shows a maximum absolute offset of `7.872` ms. Fixed by TZ-05 before any latency claim is possible. |

---

## 8. What does not exist yet

No order-book history, no Polymarket client code, no execution path, no capital at risk. Nothing in
this repository can place an order. The recorder reads; it cannot write to any venue.

The recorder exists, is merged, and is running. Its oracle tier has produced exactly one
conclusion — the Phase 0 answer — and nothing else in it has been read.
