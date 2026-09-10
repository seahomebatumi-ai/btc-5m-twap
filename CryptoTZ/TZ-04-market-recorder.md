# TZ-04 — Market and Oracle Recorder

**Canonical filename:** `TZ-04-market-recorder.md` — the Executor names the committed file from
this line and from no other source.

| item | value |
|---|---|
| destination | `CryptoTZ/TZ-04-market-recorder.md` |
| report | `CryptoReports/TZ-04-market-recorder-report.md` → straight to `main` |
| code | `research/recorder/**` → branch `tz-04-market-recorder` → PR. **Never straight to `main`.** |
| Executor model | **Opus** — network, clock discipline, multi-file, and the result decides the project |
| supersedes | nothing |

## 0. Fingerprint gate

| anchor | required value |
|---|---|
| System Map revision | `2026-09-10-d` |
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-reopened / 1-reopened / 2-not-started` |
| `A4` — executor contract | `437b45ea196b` |

Any mismatch → **BLOCKED** before any work, with the computed values reported and nothing else
done.

---

## 1. Why this TZ exists

On 2026-09-10 the settlement mechanic recorded in CANON §1.1 was found to be wrong. The venue
does not resolve on an average over the whole interval. It compares two readings of a Chainlink
trailing-TWAP feed — one at the open, one at the close. The CANON and the System Map have been
replaced accordingly.

Two consequences drive this specification:

1. **The settlement feed has never been recorded.** Chainlink TWAP reports are not archived
   publicly, and Polymarket RTDS explicitly offers no snapshot, no history and no replay after a
   disconnect. Every hour not recorded is an hour that cannot be reconstructed later at any
   price. This is the only artifact in the project whose cost is irreversible, which is why it
   goes first.
2. **The mechanic must be established by measurement, not by reading.** Reading it is what
   failed. §5 V2 therefore identifies the settlement rule empirically, against resolved
   outcomes, with the acceptance threshold fixed below before any data is seen.

## 2. Scope

Read-only capture and integrity accounting. Nothing else.

**Not in scope, and their appearance in the diff is grounds for rejection:** any order path, any
CLOB authentication, any wallet, key, signer or credential; any pricing arithmetic; any label;
any aggregation, summary statistic or chart beyond the counts required in §5; any Parquet
conversion; any file under `engine/`; any edit to `research/twap-divergence.py` or
`research/selftest-twap-divergence.py` (both frozen); any Release or asset upload.

## 3. Streams

One RTDS socket carries S1–S4. Subscribe to all four on the same connection.

| # | source | subscription | role |
|---|---|---|---|
| S1 | RTDS `wss://ws-live-data.polymarket.com` | topic `crypto_prices_twap_sixty`, `filters` exactly `{"symbol":"btc/usd"}` | **the settlement feed.** Primary. |
| S2 | same socket | `crypto_prices_twap_thirty`, same filter | alternative hypothesis, and the only thing that will catch a silent revert to the 30-second window |
| S3 | same socket | `crypto_prices_chainlink`, `{"symbol":"btc/usd"}` | non-TWAP Chainlink reference; candidate source of the price to beat |
| S4 | same socket | `crypto_prices`, `{"symbol":"btcusdt"}` | Binance cross-check only. **Never a pricing input** — CANON Part IV. |
| S5 | CLOB websocket, `market` channel | both `token_id`s of the live `btc-updown-5m-*` market, `initial_dump: true` | book snapshot plus every `book`, `price_change`, `last_trade_price` and `tick_size_change` frame |
| S6 | Gamma REST | the market by slug `btc-updown-5m-{epoch}` | metadata stored **whole and unparsed**: condition id, token ids, start/end, fee schedule, tick size, and whatever field carries the price to beat |
| S7 | Gamma / Data REST | the same market after close | the venue's resolved outcome — required by V2 |

`filters` must be the exact compact JSON form with one lowercase symbol and no spaces. RTDS uses
an application-level heartbeat: send the text frame `PING` every 5 seconds.

**The CLOB websocket URL and the resolution endpoint are read from the current Polymarket
documentation at implementation time and stated verbatim in the report.** Do not carry a URL
from memory or from an example repository.

## 4. Capture, layout and integrity

**Window.** For interval opening at `T0`, capture `[T0 − 90, T0 + 330]`. The 90 seconds before
the open are mandatory: the price to beat is a trailing average and cannot be reconstructed
without them.

**Layout.** Outside the repository, so nothing can reach git history:

```
/var/lib/btc-recorder/btc-updown-5m/<T0_epoch>/
    twap60.jsonl.gz  twap30.jsonl.gz  chainlink.jsonl.gz  binance.jsonl.gz
    clob.jsonl.gz    gamma.json       resolution.json     manifest.json
```

Streams run continuously; each frame is written to every interval directory whose window
contains it, so a frame lands in at most two. Each directory is self-contained and replayable on
its own. Compress at interval close.

**Line format.** One JSON object per line, and only these three keys:

```
{"recv_ns": <CLOCK_REALTIME ns>, "mono_ns": <CLOCK_MONOTONIC ns>, "raw": "<frame text verbatim>"}
```

The frame is stored as received. It is never re-serialised, re-ordered, type-converted, rounded
or normalised. Where a payload carries `full_accuracy_value`, that string is what survives; the
convenience float is not a substitute.

**`manifest.json` per interval.** `T0_epoch`; per stream: first and last `recv_ns`, message
count, longest inter-message gap in ms; every disconnect with start and end `recv_ns`; recorder
git sha; host clock offset samples; `complete`, defined as **zero disconnects on S1 and S5
across the whole window**.

**Gaps are recorded, never filled.** No interpolation, no forward-fill, no carry-forward, at any
point, for any reason.

**Disk.** Log free space each interval; stop cleanly, loudly and without truncating a partial
interval below 20 GB free. Do not invent a retention policy — measure the footprint and report
it; retention is an Architect decision made from the measured number.

## 5. Validation

**Written by the Architect. The Executor runs these and does not design, extend, relax or
substitute them. A red result is a finding, not a thing to fix.** Every result below is a
**count**; "checks passed" is not a result.

Scored over the first **≥ 200 consecutive intervals with `complete: true`** in the proving run.

**V1 — price-to-beat identity.** For each interval, compare the venue's published price to beat
against six candidates, at full available precision: from S1, S2 and S3, the last report with
`payload.timestamp <= T0` and the first with `payload.timestamp >= T0`. Report, per candidate,
the count of exact matches out of N, and for the best two the distribution of absolute
differences. If no S6 field carries the price to beat, state that plainly and report V1 as
unresolved — do not substitute a screen reading.

**V2 — settlement rule identification.** For each interval, evaluate three candidate rules and
compare each against the resolved outcome from S7:

| rule | statement |
|---|---|
| `R1` | `S1` at/after `T0 + 300` ≥ price to beat |
| `R2` | mean of `S3` over `[T0, T0 + 300]` ≥ `S3` at `T0` — the superseded reading |
| `R3` | `S3` at `T0 + 300` ≥ `S3` at `T0` — the pre-August rule |

Report three agreement counts out of N.

**Acceptance, fixed here before any data is seen:** a rule is declared the settlement rule only
if it agrees on **at least 199 of every 200** intervals scored. If no candidate clears that, the
report states the counts, declares the mechanic **unresolved**, and proposes nothing further —
the next test is the Architect's to specify.

**V3 — gap accounting.** Per stream per interval: message count, longest gap in ms, disconnect
count, total disconnected ms. Report how many intervals in the proving run were `complete:
false`, and the reason distribution. Incomplete intervals are excluded from V1 and V2 and the
exclusion count is stated.

**V4 — read-only proof.**
`grep -rniE "(private[_-]?key|signer|create[_-]?order|post[_-]?order|api[_-]?secret|passphrase|l1[_-]?auth|l2[_-]?auth|wallet)" research/recorder/`
Report the command and the number of matching lines. The expected number is zero and a non-zero
result is reported as-is, not silenced.

**V5 — determinism.** Rebuild `manifest.json` from an already-captured interval directory and
report `sha256sum` before and after. They are equal or the run has a defect.

**V6 — clock discipline.** The host is NTP-disciplined. Report mean and maximum offset across
the proving run. Flag every interval captured while the offset exceeded **50 ms** — the venue's
crypto taker delay is now 50 ms, so a looser clock cannot support any later latency claim.

## 6. Proving run and deliverable

Run continuously for **24 hours**, yielding **≥ 280 intervals**, then report. **The recorder is
not stopped when this TZ closes.** It keeps running.

The report contains, and contains nothing else of substance:

1. The fingerprint table — `wc -l` and `sha256sum` for `SYSTEM-MAP.md` and for every file the
   map's fingerprint table lists at authoring time, read from that table.
2. V1–V6, as counts.
3. Measured bytes per interval and projected bytes per day, before and after compression.
4. The exact CLOB websocket URL, RTDS topics, and resolution endpoint used.

Publication is part of execution: a run that exists only on the VPS has not been delivered.

## 7. What this TZ deliberately does not contain

**No Phase 2 gate.** The Phase 2 threshold compares executable quotes against `p_fair`, and
`p_fair` is being corrected in TZ-05. A gate written now would be written against a pricer that
is about to change, and the CANON forbids redefining a gate once its number is known. TZ-04
therefore produces no aggregation whatsoever — the recorded bytes stay unread until TZ-05 fixes
the pricer and a TZ states the Phase 2 gate before the first aggregation runs.
