# TZ-04b — Market and Oracle Recorder, scoring set corrected

**Canonical filename:** `TZ-04b-market-recorder-scoring.md` — the Executor names the committed
file from this line and from no other source.

| item | value |
|---|---|
| supersedes | `TZ-04a-market-recorder-corrected.md`, and through it `TZ-04-market-recorder.md`. Both stay committed and unedited. |
| destination | `CryptoTZ/TZ-04b-market-recorder-scoring.md` |
| report | `CryptoReports/TZ-04b-market-recorder-scoring-report.md` → straight to `main` |
| code | `research/recorder/**` → branch `tz-04b-market-recorder`, created from `origin/tz-04a-market-recorder` at `3895356` → PR. **Never straight to `main`.** PR #2 is closed unmerged, superseded by this TZ. |
| Executor model | **Opus** — network, clock discipline, multi-file, and the result decides the project |

## 0. Fingerprint gate

| anchor | required value |
|---|---|
| System Map revision | `2026-09-11-a` |
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-reopened / 1-reopened / 2-not-started` |
| `A4` — executor contract | `437b45ea196b` |

Any mismatch → **BLOCKED** before any work, with the computed values reported and nothing else
done.

---

## 1. What changed, and what did not

TZ-04a was blocked on its own §6, which required the scoring set to be **consecutive**. The venue
closes every RTDS websocket 7,200 seconds after it opens — measured twice, at 7,199.997 s and
7,199.985 s, each a server-initiated `1001 Going away`, with the timer restarting on every new
connection. S1 and S3 share one socket, so every close is a disconnect, and a run of `k`
consecutive complete intervals needs `300·(k − 1) + 420` seconds without one. Two hundred need
60,120 s against a 7,200 s ceiling, which caps any run at 23. The observed maximum was exactly 23.
The requirement was unsatisfiable, and unsatisfiable for a reason with no bearing on what V1 and V2
measure.

**One word changes: `consecutive` is deleted.** V1 and V2 are per-interval tests. Consecutiveness
was never a statistical requirement — it was a crude guard against picking a favourable stretch.
§6 replaces it with a stronger guard: ordered disclosure of every interval in the window, so the
Architect re-derives the counts instead of trusting them.

**The gate is carried across word for word — at least 199 of every 200.** It may be, because **no
score exists**: the TZ-04a report states no V1–V7 result and no agreement count has been computed
by anyone. A sampling rule changed before any score is seen cannot be tuned to one. Changed after,
it would be laundering the gate, and would be refused.

Three further points, so this does not become TZ-04c:

- **The recorder already exists.** It has run since 2026-09-10 10:21:09 UTC on commit `3895356`. It
  is not rebuilt, not restarted and not stopped. Intervals already written are valid capture under
  unchanged definitions and are scored.
- **The Tier B probe has already executed**, once, for 60 minutes. It is not re-run.
- **No overlapped reconnect.** Opening a second socket before the venue closes the first would
  remove the gap and put duplicate frames into the raw capture at exactly the point where V2 takes
  a mean over S3. A ~6% interval loss is cheaper than that risk. Architect's decision; the
  discarded alternative is the dual-socket overlap.

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

**Known venue behaviour, measured under TZ-04a and now recorded in System Map §6:** the RTDS server
closes every connection 7,200 seconds after it opens, with `1001 Going away`, and the timer
restarts on each new connection. It is undocumented. Reconnect promptly, log the disconnect exactly
as §4 requires, and **do not pre-empt the close with an overlapping second socket**.

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

## 5. The Tier B probe — already executed, not re-run

The probe ran once under TZ-04a, for 60 minutes, and its counters and its one retained interval are
on disk under `/var/lib/btc-recorder/`. **It is not run again.** V7 is reported from those existing
counters. If a counter V7 needs was not persisted, report that field as unavailable and name it —
do not re-subscribe S5 to recover it.

## 6. Validation

**Written by the Architect. The Executor runs these and does not design, extend, relax or
substitute them. A red result is a finding, not a thing to fix.** Every result below is a
**count**; "checks passed" is not a result.

V1 and V2 are scored over a **scoring set** defined mechanically as follows, and over no other
intervals:

- **Start.** The first interval whose whole `[T0 − 90, T0 + 330]` window lies after the recorder
  process start on commit `3895356`, 2026-09-10 10:21:09 UTC. Nothing captured by an earlier build
  is scored.
- **Membership.** Every interval from that start, in chronological order, that has `complete: true`
  and a venue resolution present.
- **Size.** The first **200** members — 200 members, not 200 consecutive intervals.
- **Nothing is excluded for any other reason.** An interval is a member, or it fails `complete`, or
  it has no resolution. There is no fourth case.

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

**Ordered disclosure, which replaces the consecutiveness guard.** The report carries one row for
every interval from the §6 start through the last member of the scoring set — **non-members
included** — with: `T0`, `complete`, the reason when not complete, whether a resolution was
present, the membership index when a member, and the three per-rule agreements. The Architect
re-derives all three counts from that table. A count stated without the table it came from is not
evidence.

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

## 7. Run and deliverable

Tier A is already running and **continues**. There is no new proving run. The report is written as
soon as the §6 scoring set is full — from intervals already on disk, if they suffice, with no
waiting at all.

If the set is not full 48 hours after the recorder start on `3895356`, stop waiting and report a
BLOCKED finding carrying the measured completion rate, the resolution-lag distribution, and the
counts as far as they go. The 48 hours is a reporting deadline derived from the grid — 576
intervals, so 200 members needs a 35% survival rate — and it is not a gate.

Resolution lag is measured, never assumed: poll S7 for each closed interval until a resolution
appears, and report the lag distribution under V7.

The report contains, and contains nothing else of substance:

1. The fingerprint table — `wc -l` and `sha256sum` for `SYSTEM-MAP.md` and for every file the
   map's fingerprint table lists at authoring time, read from that table.
2. V1–V7, as counts.
3. The §6 ordered-disclosure table in full.
4. The exact CLOB websocket URL, RTDS topics, and resolution endpoint used.

Publication is part of execution: a run that exists only on the VPS has not been delivered.

## 8. What this TZ deliberately does not contain

**No Phase 2 gate.** The Phase 2 threshold compares executable quotes against `p_fair`, and
`p_fair` is being corrected in TZ-05. A gate written now would be written against a pricer that
is about to change, and the CANON forbids redefining a gate once its number is known.

**No continuous order-book capture, and no storage decision for it.** Both wait on V7.

**No retention or rotation policy.** The recorder stops at a floor; it never deletes. Retention
is specified once V7 has produced a measured daily footprint.

**No re-run of the Tier B probe, and no overlapped reconnect.** Both are ruled out in §1.
