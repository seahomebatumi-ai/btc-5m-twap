# SYSTEM MAP — btc-5m-twap

**Revision 2026-09-10-a.** Written by the Architect; the Executor never edits it. This is a
**state** document: what exists right now. It holds no mission, no rules and no history.

- The CANON (Architect's project instructions, not in this repository) holds the mission, the
  fair-value model, the measured facts and the phase gates.
- `EXECUTOR-INSTRUCTIONS.md` holds how the Executor works.
- **This map never restates a CANON §1.2 formula.** The CANON is the only statement of it,
  and `research/twap-divergence.py` is the only implementation of it.

---

## 0. Fingerprint gate

Every TZ header states the required revision string and the anchors below. The Executor
compares before doing any work; a mismatch is BLOCKED.

**Revision string:** `2026-09-10-a`

| anchor | value |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `1-complete / 2-not-started` |
| `A4` — executor contract | `437b45ea196b` |

Anchors are the first 12 hex characters of the SHA-256 of the named artifact, except `A3`.

### Fingerprint table

Every report states `wc -l` and `sha256sum` for each row. `frozen` rows must match the hash
printed here or the run is BLOCKED. `tracked` rows are reported with no expectation.

| path | lines | bytes | state | SHA-256 |
|---|---|---|---|---|
| `SYSTEM-MAP.md` | — | — | reported | self-reference; report the value you compute |
| `EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` |
| `research/twap-divergence.py` | 1,135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` |

Hashes are of the file as committed on `main` at revision date, verified by the Architect
against `origin/main` — not copied from a report. Changing a `frozen` row requires a TZ that
authorizes it and a new map revision. Line counts are `wc -l`.

---

## 1. Repository

`github.com/seahomebatumi-ai/btc-5m-twap` — **public**. No dataset, archive or binary has ever
entered git history; the pack is under 300 KB and stays that way.

| path | contents |
|---|---|
| `CryptoTZ/` | specifications, Architect → Boss upload |
| `CryptoReports/` | reports, Executor → straight to `main` |
| `research/` | measurement code, Executor → branch + PR |
| `engine/` | live engine — **does not exist yet** |
| root | `SYSTEM-MAP.md`, `EXECUTOR-INSTRUCTIONS.md`, `.gitignore` |

**Branches**

| branch | head | state |
|---|---|---|
| `main` | `356c29a` | current |
| `tz-02-divergence-distribution` | `a772d19` | contained in `main`; nothing to merge |
| `tz-01a-twap-divergence-corrected` | `ea9290b` | the commit the dataset tag points at |
| `tz-01-twap-divergence` | — | superseded, kept for forensics |

**Tag:** `tz-01a-dataset` → `ea9290b92b9fa50c22d0560d5d01dfa392af44df`.

**Files on `main`:** three TZ files (`TZ-01`, `TZ-01a`, `TZ-02`), three reports of the same
numbers, three `research/` scripts, `.gitignore`.

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

**Columns (25).** Keys `interval_open_ts`, `month`, `tau`, `t`. Inputs `K`, `S_t`,
`naive_move`, `twap_so_far`, `state`. Volatility `sigma_pre`, `sigma_live`,
`sd_remaining_pre`, `sd_remaining_live`. Prices `p_twap_pre`, `p_naive_pre`, `p_twap_live`,
`p_naive_live`. Settlement proxies `twap_1s`, `twap_30s`, `twap_60s`, `outcome_1s`,
`outcome_30s`, `outcome_60s`. Integrity `n_missing_bars`, `prior_filled_bars`.

**The two sigma variants**, both carried through every measurement:

- `sigma_pre` — from the 30 one-minute bars **before** the interval open, converted to a
  per-second dollar figure. Fixed for the whole interval.
- `sigma_live` — from a 1-second window: 300 seconds of run-up before the open plus the bars
  already closed inside the interval. Causal, and it moves as the interval runs.

### 2.2 What the outcome labels are, and are not

All three labels are **exchange-derived proxies** computed from Binance 1-second klines at
1 / 30 / 60-second sampling. They are not oracle labels. They disagree with each other:
`outcome_1s` vs `outcome_60s` differ on **8,719 of 210,234 intervals (4.147%)**, and the
disagreement lands precisely on the marginal cases.

Settlement now reads a 60-second Chainlink stream, so **`outcome_60s` is the closest proxy
and is the label any new work uses.** The published gate results were computed on
`outcome_1s`; the label-sensitivity table in the TZ-01a report shows the verdicts hold under
`outcome_60s` (Brier for `p_twap` improves to 0.0732 / 0.0726). No conclusion in this project
currently depends on the choice — check that this is still true before relying on it.

### 2.3 What is not in the data

**No oracle data. No market data.** There is no Chainlink tick, no Polymarket quote, no
order-book depth, no fill, no fee-paid figure anywhere in this repository. Everything measured
to date compares two of the Architect's own models against exchange-derived labels.

---

## 3. Pipeline

| file | role |
|---|---|
| `research/twap-divergence.py` | the collector. Downloads and verifies the monthly archives, walks the 1-second bars, writes one row per checkpoint. **The only implementation of the CANON §1.2 arithmetic**, in `checkpoint_quantities`; it reads no bars itself, so the causal reading and the superseded TZ-01 reading share one implementation and differ only in which bars they are handed. |
| `research/selftest-twap-divergence.py` | its analytic self-tests |
| `research/tz02-distribution.py` | aggregation over the observation set. Reads the Parquet columns only; contains no `erf`, `norm`, `sqrt` or sigma arithmetic. |

Outputs go to `research/out/**`, git-ignored except `twap-divergence-summary.md` and
`twap-divergence-contamination.md`. `research/out/tz02-summary.md` is ignored.
`/root/tz01-out-archive/` holds the superseded TZ-01 output — present, untouched, never read.

---

## 4. What is validated, and by what

| claim | established by | verified independently by the Architect |
|---|---|---|
| the causal reading is genuinely causal | TZ-01a perturbation test: 22,500 comparisons bit-identical, 7,500 negative controls all moved | yes — truncation test withdrawn and not run |
| the TWAP model beats the endpoint model | Gate B PASS both variants; Brier 0.0781 vs 0.1145 (`sigma_pre`), 0.0785 vs 0.1057 (`sigma_live`) | yes |
| divergence is abundant at money-relevant size | Gate A2 PASS: **171.492 events/day**, tradeable, `T = 0.05`, `tau` ∈ {60, 90, 120, 180}, de-duplicated per interval; weakest of six readings 73.864/day | yes — re-derived from the published bytes with independent SQL, exact to three decimals |
| the collector was not modified between TZ-01a and TZ-02 | hash equality | yes — `6c5089…` read from `origin/main` |
| the sign of `D = p_twap − p_naive` has **no** preferred direction | TZ-02 measurement 1: 49.6% positive / 50.3% negative over 1,051,170 observations, at every `tau`, under both variants | yes |

The last row **supersedes the first bullet of CANON §1.4**, which predicted that the abundant
divergence runs `p_twap > p_naive`. The ramp argument does not generalise to the population.
Replacement text was issued to the Boss on 2026-09-10; until it is pasted into the project
instructions, the CANON is stale on that one point and this map is correct.

**Inversions remain the rare tail:** 86 (`sigma_pre`) and 137 (`sigma_live`) over 730 days,
reproduced exactly by the TZ-02 pipeline.

---

## 5. Phase state

| phase | question | state |
|---|---|---|
| 0 | do the two models disagree, and is the TWAP model calibrated? | complete — yes, and yes |
| 1 | at what divergence threshold, and how often? | **complete — Gate A2 PASS, 171.492/day** |
| 2 | does the **market price** deviate from `p_fair`, and by how much? | **not started — the decision point** |
| 3 | is the deviation capturable after fees, spread, depth, latency? | not started |
| 4 | live, minimum size, fixed loss limit | not started |

**This project has a validated pricer and no known edge.** Phases 0 and 1 could only
disqualify; neither can confirm one. Phase 2 needs executable Polymarket quotes and the oracle
basis, and neither exists in this repository.

---

## 6. Environment

| item | value |
|---|---|
| host | Vultr VPS (Warsaw); the Executor runs Claude Code CLI on the VPS itself |
| language | Python 3.12 |
| stack | Parquet storage, pandas/pyarrow, DuckDB for aggregation |
| auth | CLI subscription auth; `ANTHROPIC_API_KEY` must not be set |
| git remote | HTTPS with the repository token embedded in the remote URL |
| **sandbox limit** | calls that read that token and send it to `api.github.com` are refused. `git` push/pull work. Release creation and asset upload therefore cannot be done from inside the session — hand the upload to the Boss and verify the result by anonymous download. |

Not yet decided by any TZ and therefore not present: systemd units, the Parquet decision
journal, any deployment.

---

## 7. Open defects

| # | defect | disposition |
|---|---|---|
| 1 | `research/tz02-distribution.py` records the collector-hash comparison into a table (`checks["collector_sha_matches"]`) but never asserts it. The run completes on a mismatch. The other three checks are asserted properly. | harmless for TZ-02 — the hash was verified independently — but the guard does not exist. Fix in the next TZ that touches that file; do not edit the committed report. |
| 2 | The TZ-02 report was amended after commit (`356c29a`, §3 and §6 item 1). Verified to touch no measurement, table or verdict. | closed by rule: `EXECUTOR-INSTRUCTIONS.md` §3.2 and §5.2 make the class impossible. Both versions stay in history. |
| 3 | The TZ-02 implementation commit `f8a0c37` (1,850 lines) is on `main`, though the TZ routed code to a branch. It reached `main` without a merge and without a verdict. | closed by rule: `EXECUTOR-INSTRUCTIONS.md` §4.1 and the §4.2 self-check. `main` is left as it is; rewriting history would cost more than the defect. |

---

## 8. What does not exist yet

No live engine, no oracle feed, no quote recorder, no order-book data, no Polymarket client
code, no execution path, no capital at risk. Nothing in this repository can place an order.

Per the CANON, a component built ahead of its gate is deleted, not deferred.
