# TZ-04a — Market and Oracle Recorder, corrected

**Canonical filename:** `TZ-04a-market-recorder-corrected.md` — the Executor names the committed
file from this line and from no other source.

| item | value |
|---|---|
| supersedes | `TZ-04-market-recorder.md`, which stays committed and unedited |
| destination | `CryptoTZ/TZ-04a-market-recorder-corrected.md` |
| report | `CryptoReports/TZ-04a-market-recorder-corrected-report.md` → straight to `main` |
| code | `research/recorder/**` → branch `tz-04a-market-recorder` → PR. **Never straight to `main`.** |
| Executor model | **Opus** — network, clock discipline, multi-file, and the result decides the project |

## 0. Fingerprint gate

| anchor | required value |
|---|---|
| System Map revision | `2026-09-10-e` |
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-reopened / 1-reopened / 2-not-started` |
| `A4` — executor contract | `437b45ea196b` |

Any mismatch → **BLOCKED** before any work, with the computed values reported and nothing else
done.

---

## 1. What changed, and what did not

TZ-04 was blocked at its own §4: it set a 20 GB free-space floor written from assumption, on a
host that has 9,620,611,072 bytes free of 31,612,203,008 total, on its only writable
filesystem, shared with unrelated production services. The floor was unsatisfiable and the
specification was therefore unsatisfiable. That is a defect in TZ-04, not in the report that
found it.

Two things change:

1. **Every resource threshold below is stated in exact bytes and is checked against the host
   capacity now recorded in System Map §6.** No round number, no unit ambiguity.
2. **Capture is split.** The oracle tier is small, always on, and is all that Phase 0 needs. The
   order book is not captured continuously; its volume is *measured* by a bounded probe so the
   next specification can be sized against a number instead of a guess.

One thing does not change, and may not: **V2 and its acceptance threshold are carried across
word for word.** The Phase 0 gate was stated before any data was seen and is not redefined.

---

## 2. Scope

Read-only capture and integrity accounting. Nothing else.

**Not in scope, and their appearance in the diff is grounds for rejection:** any order path, any
CLOB authentication, any wallet, key, signer or credential; any pricing arithmetic; any label;
any aggregation, summary statistic or chart beyond the counts required in §6; any Parquet
conversion; any file under `engine/`; any edit to `research/twap-divergence.py` or
`research/selftest-twap-divergence.py` (both frozen); any Release or asset upload; any deletion
of anything on the host that does not belong to this recorder.

## 3. Streams

### Tier A — continuous. Everything Phase 0 needs.

One RTDS socket carries S1–S4. Subscribe to all four on the same connection.

| # | source | subscription | role |
|---|---|---|---|
| S1 | RTDS `wss://ws-live-data.polymarket.com` | topic `crypto_prices_twap_sixty`, `filters` exactly `{"symbol":"btc/usd"}` | **the settlement feed.** Primary. |
| S2 | same socket | `crypto_prices_twap_thirty`, same filter | alternative hypothesis, and the only thing that will catch a silent revert to the 30-second window |
| S3 | same socket | `crypto_prices_chainlink`, `{"symbol":"btc/usd"}` | non-TWAP Chainlink reference; candidate source of the price to beat |
| S4 | same socket | `crypto_prices`, `{"symbol":"btcusdt"}` | Binance cross-check only. **Never a pricing input** — CANON Part IV. |
| S6 | Gamma REST | the market by slug `btc-updown-5m-{epoch}` | metadata stored **whole and unparsed**: condition id, token ids, start/end, fee schedule, tick size, and whatever field carries the price to beat |
| S7 | Gamma / Data REST | the same market after close | the venue's resolved outcome — required by V2 |

`filters` must be the exact compact JSON form with one lowercase symbol and no spaces. RTDS uses
an application-level heartbeat: send the text frame `PING` every 5 seconds.

### Tier B — S5, order book. Probe only, not continuous.

S5 is the CLOB websocket `market` channel, both `token_id`s of the live market,
`initial_dump: true`, carrying every `book`, `price_change`, `last_trade_price` and
`tick_size_change` frame. **It is not captured continuously under this TZ.** It is subscribed
once, for the bounded probe in §5, and then unsubscribed.

**The CLOB websocket URL and the resolution endpoint are read from the current Polymarket
documentation at implementation time and stated verbatim in the report.** Do not carry a URL
from memory or from an example repository.

## 4. Capture, layout, floors

**Window.** For an interval opening at `T0`, capture `[T0 − 90, T0 + 330]`. The 90 seconds
before the open are mandatory: the price to beat is a trailing average and cannot be
reconstructed without them.

**Layout.** Outside the repository, so nothing can reach git history:

```
/var/lib/btc-recorder/btc-updown-5m/<T0_epoch>/
    twap60.jsonl.gz  twap30.jsonl.gz  chainlink.jsonl.gz  binance.jsonl.gz
    gamma.json       resolution.json  manifest.json
    clob.jsonl.gz    <- present for exactly one interval, from the §5 probe
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
git sha; host clock offset samples; and `complete`, defined as **zero disconnects on S1 and S3
across the whole window, with S6 and S7 both present**.

**Gaps are recorded, never filled.** No interpolation, no forward-fill, no carry-forward, at any
point, for any reason.

**Resource floors. Two independent stops, whichever is reached first.** Both are checked before
the first frame is written and then once per interval close.

| stop | exact value | meaning |
|---|---|---|
| free-space floor | `2_000_000_000` bytes free on the filesystem holding `/var/lib/btc-recorder` | stop cleanly, without truncating a partial interval, and log loudly |
| self-cap | `4_000_000_000` bytes of cumulative data under `/var/lib/btc-recorder/**` | same stop, regardless of free space |

Both are satisfiable on the host as measured: 9,620,611,072 bytes free, and 4,000,000,000 bytes
of capture still leaves 5,620,611,072 above the floor. **The recorder never deletes anything to
stay under a floor.** It stops and reports. Retention is an Architect decision taken from the
V7 numbers.

## 5. The Tier B probe

Purpose: measure what the order book costs, without committing disk to it.

1. Subscribe S5 for **exactly 60 minutes**, following the market roll so each live
   `btc-updown-5m-*` market is subscribed as it opens and dropped as it closes.
2. For every frame: count it, add its byte length to a running total, and **discard the payload**
   — except during one single interval, chosen as the first fully-covered interval of the probe,
   whose frames are written to `clob.jsonl.gz` in that interval's directory.
3. At 60 minutes, unsubscribe and stop. Do not resubscribe.

Nothing else is derived from the probe. It produces counters and one retained interval.

## 6. Validation

**Written by the Architect. The Executor runs these and does not design, extend, relax or
substitute them. A red result is a finding, not a thing to fix.** Every result below is a
**count**; "checks passed" is not a result.

V1 and V2 are scored over the first **≥ 200 consecutive intervals with `complete: true`**.

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

**Acceptance, unchanged from TZ-04 and fixed before any data was seen:** a rule is declared the
settlement rule only if it agrees on **at least 199 of every 200** intervals scored. If no
candidate clears that, the report states the counts, declares the mechanic **unresolved**, and
proposes nothing further — the next test is the Architect's to specify.

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

**V7 — footprint.** Report, as measured and never as an estimate:

| quantity | how |
|---|---|
| Tier A bytes per interval, raw and gzipped | mean, median, maximum over the proving run |
| Tier A bytes per day, projected | from the above × 288 |
| Tier B frames per interval | from the §5 probe counters |
| Tier B bytes per interval, raw | from the §5 probe counters |
| Tier B gzip ratio | measured on the one retained interval, stated as raw bytes and compressed bytes |
| Tier B bytes per day, projected | raw and compressed |
| free space at start and at end of the proving run | exact bytes |

## 7. Proving run and deliverable

Run Tier A continuously for **24 hours**, yielding **≥ 280 intervals**, then report. The Tier B
probe runs once inside that window. **Tier A is not stopped when this TZ closes.** It keeps
running until a floor in §4 is reached or a later TZ changes it.

The report contains, and contains nothing else of substance:

1. The fingerprint table — `wc -l` and `sha256sum` for `SYSTEM-MAP.md` and for every file the
   map's fingerprint table lists at authoring time, read from that table.
2. V1–V7, as counts.
3. The exact CLOB websocket URL, RTDS topics, and resolution endpoint used.

Publication is part of execution: a run that exists only on the VPS has not been delivered.

## 8. What this TZ deliberately does not contain

**No Phase 2 gate.** The Phase 2 threshold compares executable quotes against `p_fair`, and
`p_fair` is being corrected in TZ-05. A gate written now would be written against a pricer that
is about to change, and the CANON forbids redefining a gate once its number is known.

**No continuous order-book capture, and no storage decision for it.** Both wait on V7.

**No retention or rotation policy.** The recorder stops at a floor; it never deletes. Retention
is specified once V7 has produced a measured daily footprint.
