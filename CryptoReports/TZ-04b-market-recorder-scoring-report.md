# TZ-04b — Market and Oracle Recorder, scoring set corrected — REPORT

**Status: executed.** The §0 fingerprint gate **passes**. The §6 scoring set filled from intervals
already on disk, with no waiting: 200 members inside 215 disclosed intervals, from T0 `1789035900`
to `1789100100`.

- **V2.** R1 agrees on **200 of 200**, which is 1.000 and clears the 199-of-200 acceptance. R2 agrees
  on 175 of 200 (0.875) and R3 on 181 of 200 (0.905). Neither of those clears it.
- **V1 is unresolved as written.** No S6 capture carries a price to beat. The venue publishes the
  number only in the market document after settlement, which is the S7 capture. Against that value,
  the first S1 report at or after T0 matches in 198 of 200 at the venue's published precision. See
  §6 item 1.

Executor model: **Opus** (`claude-opus-5`), as the TZ requires.

---

## 0. Fingerprint

Read from `SYSTEM-MAP.md` at `origin/main` = `833440806965106455bf97179b98dc28fd76db94`, at
authoring time.

**Revision string read:** `2026-09-11-a`. TZ-04b requires `2026-09-11-a`, so it matches.

| anchor | required by TZ-04b §0 | computed | match |
|---|---|---|---|
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` | yes |
| `A2` — collector | `6c5089330629` | `6c5089330629` | yes |
| `A3` — phase | `0-reopened / 1-reopened / 2-not-started` | `0-reopened / 1-reopened / 2-not-started` | yes |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b` | yes |

`A1` was not copied from the map. At the start of execution the Release asset was fetched
anonymously and hashed: 76,818,669 bytes, SHA-256
`229a944f2d5111c3e68b1fa0630f8e8658356147f9669d18665e575b60f3716b`. `A2` and `A4` are the first 12
hex characters of the SHA-256 values below. `A3` was read from map §5.

### Fingerprint table

The table covers `wc -l`, bytes and `sha256sum` for `SYSTEM-MAP.md` and for every file the map's §0
table lists. The values are read from `origin/main` at authoring time.

| path | lines | bytes | state | SHA-256 | matches map |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 246 | 16,641 | reported | `188600d026eb901a7001db0f2c13fb0ba0e6c9a0528aebcb3f23e44a581f5bb0` | self-reference |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | yes |
| `research/twap-divergence.py` | 1,135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | yes |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | yes |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | yes |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | yes |

All three `frozen` rows match the hashes printed in the map, so the contract §1.4 check passes.

---

## 1. Input

**Nothing was re-collected.**
- The Tier A recorder was not rebuilt, restarted or stopped. At authoring it is pid `3762200`, up
  1 d 07:24, on `3895356`.
- The Tier B probe was not re-run, and S5 was not subscribed.
- The only network read made by this execution was the anonymous `A1` download above, plus the
  two documentation pages cited in §2.9.

| input | what it supplies |
|---|---|
| `/var/lib/btc-recorder/btc-updown-5m/<T0>/` for the 215 intervals T0 = `1789035900` … `1789100100` (2026-09-10 10:25 → 2026-09-11 04:15 UTC) | the scoring set, V1–V3 and V5–V7. Each directory is read through its own `manifest.json`, the four `*.jsonl.gz` streams, `gamma.json` (S6), `resolution.json` (S7) and `runtime.jsonl` |
| `/var/lib/btc-recorder/runtime.jsonl` | the process start record and the disconnect records |
| `/var/lib/btc-recorder/recorder.log` | the exception each socket drop logged, used only for the V3 cause column |
| `/var/lib/btc-recorder/tier-b-probe.json` | the §5 probe counters for V7 |
| `/var/lib/btc-recorder/btc-updown-5m/1789034400/clob.jsonl.gz` | the one retained Tier B interval, 9,747,797 bytes, for the V7 gzip ratio |

**Start.** TZ-04b §6 gives the recorder start as 2026-09-10 10:21:09 UTC, and the recorder log line
reads `--- restart 2026-09-10T10:21:09Z on 3895356 ---`. The process's start record is `recv_ns`
`1789035670180046788`, which is 10:21:10.180. Both instants give the same first interval: T0
`1789035900` (10:25), whose window opens at 10:23:30. The window of the interval before it opens at
10:18:30, before the start. The analyzer asserts that both instants agree.

**Instrument.** `research/recorder/analyze.py` at `05c901c`, unchanged at the branch head `ee2f632`, run with `/root/tz04a-env/venv`
(Python 3.12, standard library only for this file).
- `analyze.py` was run twice at `05c901c` and once more at `ee2f632`. All three runs gave
  `results.json`, SHA-256
  `2ff7728d11f96ff823f55cfc6176a51e6ac5d09cac152bc31dbe4d6f4b554e38`.
- `analyze.py --tables` was run the same three times. All three gave `tables.md`, SHA-256
  `7f3e112628a80dd03c5dfed85a2f0835e2c52e17459afadc65003776de7d5711`.

Both files are kept at `/root/tz04b-work/`, outside the repository. Every table in §2.10–§2.12 is
that `tables.md`, pasted unedited.

---

## 2. Measurements

Every number below is computed by `analyze.py` unless marked otherwise.

### 2.1 The scoring set

| quantity | value |
|---|---|
| first interval (§6 start) | `1789035900` — 2026-09-10 10:25 UTC |
| members required | 200 |
| members found | **200** — the set is full |
| last member | `1789100100` — 2026-09-11 04:15 UTC, member #200 |
| intervals disclosed, start through last member | **215** |
| non-members | 15 — all fail `complete`, every one by `disconnect`; 0 lack S6, 0 lack S7, 0 lack a manifest |
| members captured by a build other than `3895356` | 0 of 215 disclosed intervals — asserted |

The 48-hour reporting deadline, 2026-09-12 10:21:09 UTC, was not reached.

### 2.2 V1 — price-to-beat identity

**V1 is unresolved as written. No S6 field carries the price to beat.**
- In the S6 capture — the market document fetched at T0 + 5 s — no key anywhere matches
  `price.?to.?beat` with a non-null value. That holds in 0 of 200 members (`analyze.py`).
- A one-off query outside `analyze.py` shows the `events[0].eventMetadata` object is absent from
  all 382 `gamma.json` files on disk.

The venue does publish the number, but only once the market is settled. It appears in the same
Gamma document, `events[0].eventMetadata.priceToBeat`, which is what the S7 capture stores. It is
present in 200 of 200 members and absent in 0.

This is the venue's own API field, not a screen reading. The counts below are scored against it and
labelled as such. The Architect may accept them or discard them (§6 item 1).

N = 200 members. A match means equal as the IEEE-754 double the venue publishes (§6 item 2).

| candidate | matches (double) | strict Decimal matches | candidate unavailable |
|---|---|---|---|
| S1 last report with `payload.timestamp <= T0` | 193 | 0 | 0 |
| S1 first report with `payload.timestamp >= T0` | **198** | 0 | 0 |
| S2 last report with `payload.timestamp <= T0` | 0 | 0 | 0 |
| S2 first report with `payload.timestamp >= T0` | 0 | 0 | 0 |
| S3 last report with `payload.timestamp <= T0` | 0 | 0 | 0 |
| S3 first report with `payload.timestamp >= T0` | 0 | 0 | 0 |

The best two are the two S1 candidates. Their absolute differences from the published price to
beat, in USD, over N = 200, are below. Percentiles are nearest-rank, `sorted[min(n−1, ⌊p·n⌋)]`.

| candidate | min | p50 | p90 | p99 | max | mean | exactly zero |
|---|---|---|---|---|---|---|---|
| S1 first `>= T0` | 8.192e-15 | 3.618176e-12 | 8.281344e-12 | 1.799604089993385 | 3.652664070888839 | 0.02726134080841109 | 0 |
| S1 last `<= T0` | 8.192e-15 | 4.114944e-12 | 8.737152e-12 | 1.4585839883192018 | 3.6997263141992462 | 0.03681761087565219 | 0 |

Two members match no candidate at all: #38 (`1789047300`) and #163 (`1789087200`). Five further
members match only S1 first `>= T0`: #46, #47, #66, #126 and #178. The per-member pattern is the V1
column of §2.10.

### 2.3 V2 — settlement rule identification

N = 200 members. Each rule is compared with the venue's resolved outcome in the S7 capture.

| rule | agree | disagree | undecidable | agreement, 3 dp | ≥ 199 of every 200 |
|---|---|---|---|---|---|
| `R1` — S1 at/after T0 + 300 ≥ price to beat | **200** | 0 | 0 | **1.000** | **yes** |
| `R2` — mean of S3 over [T0, T0 + 300] ≥ S3 at T0 | 175 | 25 | 0 | 0.875 | no |
| `R3` — S3 at T0 + 300 ≥ S3 at T0 | 181 | 19 | 0 | 0.905 | no |

- R1 ties, where the S1 reading is equal to the price to beat: 0.
- R1 verdicts that differ between a double comparison and a strict Decimal comparison: 0 of 200.
- The reading conventions are stated in §6 item 3.
- The per-interval verdicts are in §2.10. They re-derive all three counts.

### 2.4 V3 — gap accounting

Over the 215 disclosed intervals:
- **15** were `complete: false`. The reason distribution is `disconnect` 15, and nothing else.
- **15** intervals are excluded from V1 and V2 for that reason.
- There is no other exclusion.

| stream | messages min / p50 / max | longest inter-message gap, ms: p50 / p90 / max |
|---|---|---|
| S1 `twap60` | 375 / 406 / 416 | 2,689.1 / 8,192.9 / 33,074.7 |
| S2 `twap30` | 376 / 406 / 416 | 2,727.3 / 8,102.3 / 33,057.3 |
| S3 `chainlink` | 375 / 406 / 416 | 2,738.3 / 8,244.6 / 33,923.1 |
| S4 `binance` | 388 / 420 / 421 | 1,351.4 / 2,440.6 / 32,378.1 |

S1–S4 share one socket, so an interval's disconnect count and disconnected milliseconds are the
same for all four streams. They are stated once per interval, in §2.11. The disconnected
milliseconds are each outage's full length, from the last frame to the resubscribe, and are not
clipped to the window.

Eleven disconnects touch the 215 windows (§2.12). They fall into three causes:

| cause, from the logged exception | count | intervals made incomplete |
|---|---|---|
| server close `1001 Going away`, after sessions of 7,199.948 – 7,199.997 s | 7 | 8 |
| no frame for 30 s — the recorder's receive timeout | 2 | 3 |
| connection lost, no close frame — `ConnectionClosedError(None, None, None)` | 2 | 4 |

A disconnect makes one interval incomplete when it falls in one window. It makes two incomplete
when it falls in the 120 s overlap between adjacent windows.

### 2.5 V4 — read-only proof

```
grep -rniE "(private[_-]?key|signer|create[_-]?order|post[_-]?order|api[_-]?secret|passphrase|l1[_-]?auth|l2[_-]?auth|wallet)" research/recorder/
```

The command was run from the repository root at `ee2f632`, with no `__pycache__` present under
`research/recorder/`. **5 matching lines.** This is not the expected zero, and it is reported as
returned:

```
research/recorder/analyze.py:504:V4_PATTERN = ("(private[_-]?key|signer|create[_-]?order|post[_-]?order|api[_-]?secret|"
research/recorder/analyze.py:505:              "passphrase|l1[_-]?auth|l2[_-]?auth|wallet)")
research/recorder/probe.py:9:Read-only: the `market` channel is public and unauthenticated. No key, signer or order path.
research/recorder/recorder.py:4:Read-only by construction. There is no order path, no CLOB authentication, no wallet, key,
research/recorder/recorder.py:5:signer or credential anywhere in this file, and no pricing arithmetic: frames are routed by
```

Two lines are the V4 pattern itself, held in the analyzer that runs the grep. Three are docstring
sentences that deny the capability. None of the five was edited to change the count (§6 item 9).

### 2.6 V5 — determinism

The manifest of interval `1789035900`, the first member, was rebuilt from a copy of its directory:

| | SHA-256 |
|---|---|
| `manifest.json` before | `10833ad69e5166123ed4923630c1ed52b0be35d996236634c11bcc33aaa69ffc` |
| `manifest.json` after | `10833ad69e5166123ed4923630c1ed52b0be35d996236634c11bcc33aaa69ffc` |

The two are equal. The same rebuild over every disclosed interval gives **215 of 215** equal.

### 2.7 V6 — clock discipline

The windows overlap, so each SNTP sample is counted once. There are 2,033 samples over the 215
windows.

| server | samples | mean offset ms | mean abs offset ms | max abs offset ms |
|---|---|---|---|---|
| `108.61.73.243` — the host's configured server | 1,021 | −0.320 | 0.559 | **7.872** |
| `pool.ntp.org` | 1,012 | −11,851,965,612.180 | 11,851,965,623.878 | 3,998,084,653,855.623 |
| both | 2,033 | −5,899,748,745.624 | 5,899,748,751.567 | 3,998,084,653,855.623 |

**Intervals flagged over 50 ms: 6.** They are `1789041300`, `1789041600`, `1789085100`,
`1789085400`, `1789095600` and `1789095900`. Every flag comes from one of three `pool.ntp.org`
samples:

| sample `recv_ns` | offset ms | round trip ms |
|---|---|---|
| `1789041569232913109` | −3,998,030,359,216.835 | 12.533 |
| `1789085401711875634` | −3,998,074,191,692.032 | 18.674 |
| `1789095853861696190` | −3,998,084,653,855.623 | 11.764 |

Each offset equals −(wall clock + 2,208,988,800 s) to within 10.02 s. That means those replies
carried transmit timestamps within seconds of the NTP era origin, 1900-01-01, rather than a time.
This was checked by a one-off query against `runtime.jsonl`. The recorder's SNTP client does not
reject such a reply. The flags stand as computed (§6 item 7).

### 2.8 V7 — footprint

All values are measured. **Tier A**, over the 215 disclosed intervals:

| bytes per interval | mean | median | max | per day, mean × 288 | per day, median × 288 |
|---|---|---|---|---|---|
| streams S1–S4, raw | 564,109.5 | 563,875 | 591,111 | 162,463,527 | 162,396,000 |
| streams S1–S4, gzipped as stored | 60,226.1 | 60,114 | 63,175 | 17,345,111 | 17,312,832 |
| whole interval directory on disk | 76,642.6 | 76,500 | 80,416 | 22,073,069 | 22,032,000 |

The whole directory adds `gamma.json`, `resolution.json`, `manifest.json` and `runtime.jsonl`.
Frames in the 120 s overlap are stored in two directories, which is why the per-day figures are
larger than one day of stream.

**Tier B**, from `tier-b-probe.json`. The probe ran for 3,600 s from epoch `1789034253.829`. Each
figure is per 300 s receive-time slot over its 11 whole slots, with one market's two tokens
subscribed at a time.

| quantity | value |
|---|---|
| frames per interval | mean 98,391.1, median 104,367, max 128,609 |
| raw bytes per interval | mean 68,626,195.2, median 71,954,283, max 90,568,133 |
| gzip ratio, measured now on the one retained file `1789034400/clob.jsonl.gz` | **9,747,797 compressed / 100,666,765 raw = 0.096832**, over 114,697 lines. The probe's own counter recorded the same three numbers. |
| raw bytes per day, projected | 19,764,344,212 from the mean; 20,722,833,504 from the median |
| compressed bytes per day, projected | 1,913,827,421 from the mean; 2,006,640,168 from the median |

**Free space** on the filesystem holding `/var/lib/btc-recorder`:

| point | UTC | free bytes | bytes under `/var/lib/btc-recorder` |
|---|---|---|---|
| start — the `3895356` start record | 2026-09-10 10:21:10.180 | **9,496,645,632** | 101,278,912 |
| end — measured at authoring by `analyze.py --disk` | 2026-09-11 17:45:52.019 | **8,489,132,032** | 40,003,914 |

Free space fell by 1,007,513,600 bytes over this span. None of that is the recorder's: its tree is
61,274,998 bytes smaller than at the start, because the probe's raw CLOB file was gzipped at
10:57:47. No floor was reached, and there is no `halt` record.

**Resolution lag** is measured over the 215 disclosed intervals. S7 was present for all 215 and
missing for none.

| lag after T0 + 300, seconds | n | min | p50 | p90 | p99 | max | mean |
|---|---|---|---|---|---|---|---|
| first seen by the recorder: `resolution.json` mtime | 215 | 123.2 | 318.5 | 423.7 | 531.3 | 573.9 | 318.3 |
| the venue's own `closedTime` in that document | 215 | 54 | 55 | 88 | 151 | 154 | 67.4 |

The recorder polls from T0 + 333 every 15 s. It accepts a document only once it is closed, carries
exactly one winning outcome, and has `eventMetadata`. That is why first sight trails `closedTime`.

### 2.9 Endpoints and topics used

| item | value, verbatim |
|---|---|
| RTDS websocket | `wss://ws-live-data.polymarket.com` — one socket, with the text frame `PING` every 5 s |
| RTDS subscription | one `{"action": "subscribe", "subscriptions": [...]}` message carrying the four entries below, each with `"type": "*"` |
| S1 | topic `crypto_prices_twap_sixty`, filters `{"symbol":"btc/usd"}` |
| S2 | topic `crypto_prices_twap_thirty`, filters `{"symbol":"btc/usd"}` |
| S3 | topic `crypto_prices_chainlink`, filters `{"symbol":"btc/usd"}` |
| S4 | topic `crypto_prices`, filters `{"symbol":"btcusdt"}` |
| CLOB websocket, the Tier B probe only | `wss://ws-subscriptions-clob.polymarket.com/ws/market`, as recorded in `tier-b-probe.json`. The current page <https://docs.polymarket.com/market-data/websocket/overview> gives this URL verbatim, read 2026-09-11. |
| S6 and S7, the resolution endpoint | `GET https://gamma-api.polymarket.com/markets/slug/btc-updown-5m-{T0}`. S6 is fetched at T0 + 5 s. S7 is the same URL, polled from T0 + 333 s every 15 s until T0 + 3,600 s. |

### 2.10 Ordered disclosure — every interval from the §6 start through the last member

- `S7`: a settled venue resolution was present.
- `member`: the index in the scoring set.
- `R1`–`R3`: `Y` means the rule agrees with the venue's outcome and `N` means it does not. They are
  given for members only, as `—` elsewhere (§6 item 4).
- `V1`: one character per candidate, in the order S1 `<=T0`, S1 `>=T0`, S2 `<=T0`, S2 `>=T0`, S3
  `<=T0`, S3 `>=T0`. `x` means equal to the published price to beat as a double, and `.` means not.

| # | T0 | open (UTC) | complete | reason not complete | S7 | member | outcome | R1 | R2 | R3 | V1 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1789035900 | 2026-09-10 10:25 | yes | — | yes | 1 | Up | Y | Y | Y | xx.... |
| 2 | 1789036200 | 2026-09-10 10:30 | yes | — | yes | 2 | Down | Y | Y | Y | xx.... |
| 3 | 1789036500 | 2026-09-10 10:35 | yes | — | yes | 3 | Up | Y | Y | Y | xx.... |
| 4 | 1789036800 | 2026-09-10 10:40 | yes | — | yes | 4 | Down | Y | N | Y | xx.... |
| 5 | 1789037100 | 2026-09-10 10:45 | yes | — | yes | 5 | Down | Y | Y | Y | xx.... |
| 6 | 1789037400 | 2026-09-10 10:50 | yes | — | yes | 6 | Down | Y | Y | Y | xx.... |
| 7 | 1789037700 | 2026-09-10 10:55 | yes | — | yes | 7 | Down | Y | N | Y | xx.... |
| 8 | 1789038000 | 2026-09-10 11:00 | yes | — | yes | 8 | Down | Y | Y | Y | xx.... |
| 9 | 1789038300 | 2026-09-10 11:05 | yes | — | yes | 9 | Up | Y | Y | Y | xx.... |
| 10 | 1789038600 | 2026-09-10 11:10 | yes | — | yes | 10 | Up | Y | Y | Y | xx.... |
| 11 | 1789038900 | 2026-09-10 11:15 | yes | — | yes | 11 | Up | Y | Y | Y | xx.... |
| 12 | 1789039200 | 2026-09-10 11:20 | yes | — | yes | 12 | Up | Y | Y | Y | xx.... |
| 13 | 1789039500 | 2026-09-10 11:25 | yes | — | yes | 13 | Down | Y | Y | Y | xx.... |
| 14 | 1789039800 | 2026-09-10 11:30 | yes | — | yes | 14 | Up | Y | Y | Y | xx.... |
| 15 | 1789040100 | 2026-09-10 11:35 | yes | — | yes | 15 | Up | Y | N | N | xx.... |
| 16 | 1789040400 | 2026-09-10 11:40 | yes | — | yes | 16 | Down | Y | Y | Y | xx.... |
| 17 | 1789040700 | 2026-09-10 11:45 | yes | — | yes | 17 | Down | Y | Y | Y | xx.... |
| 18 | 1789041000 | 2026-09-10 11:50 | yes | — | yes | 18 | Down | Y | Y | Y | xx.... |
| 19 | 1789041300 | 2026-09-10 11:55 | yes | — | yes | 19 | Down | Y | Y | Y | xx.... |
| 20 | 1789041600 | 2026-09-10 12:00 | yes | — | yes | 20 | Down | Y | Y | Y | xx.... |
| 21 | 1789041900 | 2026-09-10 12:05 | yes | — | yes | 21 | Down | Y | Y | Y | xx.... |
| 22 | 1789042200 | 2026-09-10 12:10 | yes | — | yes | 22 | Up | Y | Y | Y | xx.... |
| 23 | 1789042500 | 2026-09-10 12:15 | yes | — | yes | 23 | Down | Y | Y | Y | xx.... |
| 24 | 1789042800 | 2026-09-10 12:20 | no | disconnect | yes | — | — | — | — | — | — |
| 25 | 1789043100 | 2026-09-10 12:25 | yes | — | yes | 24 | Up | Y | Y | Y | xx.... |
| 26 | 1789043400 | 2026-09-10 12:30 | yes | — | yes | 25 | Down | Y | Y | Y | xx.... |
| 27 | 1789043700 | 2026-09-10 12:35 | yes | — | yes | 26 | Down | Y | Y | Y | xx.... |
| 28 | 1789044000 | 2026-09-10 12:40 | yes | — | yes | 27 | Up | Y | Y | Y | xx.... |
| 29 | 1789044300 | 2026-09-10 12:45 | yes | — | yes | 28 | Down | Y | Y | Y | xx.... |
| 30 | 1789044600 | 2026-09-10 12:50 | yes | — | yes | 29 | Down | Y | Y | Y | xx.... |
| 31 | 1789044900 | 2026-09-10 12:55 | yes | — | yes | 30 | Up | Y | N | Y | xx.... |
| 32 | 1789045200 | 2026-09-10 13:00 | yes | — | yes | 31 | Up | Y | Y | Y | xx.... |
| 33 | 1789045500 | 2026-09-10 13:05 | yes | — | yes | 32 | Down | Y | Y | Y | xx.... |
| 34 | 1789045800 | 2026-09-10 13:10 | yes | — | yes | 33 | Down | Y | Y | Y | xx.... |
| 35 | 1789046100 | 2026-09-10 13:15 | yes | — | yes | 34 | Up | Y | N | N | xx.... |
| 36 | 1789046400 | 2026-09-10 13:20 | yes | — | yes | 35 | Up | Y | Y | Y | xx.... |
| 37 | 1789046700 | 2026-09-10 13:25 | yes | — | yes | 36 | Up | Y | Y | Y | xx.... |
| 38 | 1789047000 | 2026-09-10 13:30 | yes | — | yes | 37 | Down | Y | Y | Y | xx.... |
| 39 | 1789047300 | 2026-09-10 13:35 | yes | — | yes | 38 | Up | Y | Y | Y | ...... |
| 40 | 1789047600 | 2026-09-10 13:40 | yes | — | yes | 39 | Down | Y | Y | Y | xx.... |
| 41 | 1789047900 | 2026-09-10 13:45 | yes | — | yes | 40 | Up | Y | Y | Y | xx.... |
| 42 | 1789048200 | 2026-09-10 13:50 | yes | — | yes | 41 | Up | Y | N | Y | xx.... |
| 43 | 1789048500 | 2026-09-10 13:55 | yes | — | yes | 42 | Up | Y | Y | Y | xx.... |
| 44 | 1789048800 | 2026-09-10 14:00 | yes | — | yes | 43 | Up | Y | Y | Y | xx.... |
| 45 | 1789049100 | 2026-09-10 14:05 | yes | — | yes | 44 | Down | Y | Y | Y | xx.... |
| 46 | 1789049400 | 2026-09-10 14:10 | yes | — | yes | 45 | Up | Y | Y | Y | xx.... |
| 47 | 1789049700 | 2026-09-10 14:15 | yes | — | yes | 46 | Down | Y | Y | Y | .x.... |
| 48 | 1789050000 | 2026-09-10 14:20 | no | disconnect | yes | — | — | — | — | — | — |
| 49 | 1789050300 | 2026-09-10 14:25 | yes | — | yes | 47 | Up | Y | Y | Y | .x.... |
| 50 | 1789050600 | 2026-09-10 14:30 | yes | — | yes | 48 | Down | Y | N | N | xx.... |
| 51 | 1789050900 | 2026-09-10 14:35 | yes | — | yes | 49 | Down | Y | N | Y | xx.... |
| 52 | 1789051200 | 2026-09-10 14:40 | yes | — | yes | 50 | Up | Y | Y | Y | xx.... |
| 53 | 1789051500 | 2026-09-10 14:45 | yes | — | yes | 51 | Up | Y | Y | Y | xx.... |
| 54 | 1789051800 | 2026-09-10 14:50 | yes | — | yes | 52 | Up | Y | Y | Y | xx.... |
| 55 | 1789052100 | 2026-09-10 14:55 | yes | — | yes | 53 | Up | Y | Y | Y | xx.... |
| 56 | 1789052400 | 2026-09-10 15:00 | yes | — | yes | 54 | Down | Y | Y | Y | xx.... |
| 57 | 1789052700 | 2026-09-10 15:05 | yes | — | yes | 55 | Up | Y | Y | Y | xx.... |
| 58 | 1789053000 | 2026-09-10 15:10 | yes | — | yes | 56 | Down | Y | N | Y | xx.... |
| 59 | 1789053300 | 2026-09-10 15:15 | yes | — | yes | 57 | Down | Y | Y | Y | xx.... |
| 60 | 1789053600 | 2026-09-10 15:20 | yes | — | yes | 58 | Down | Y | Y | Y | xx.... |
| 61 | 1789053900 | 2026-09-10 15:25 | yes | — | yes | 59 | Down | Y | Y | Y | xx.... |
| 62 | 1789054200 | 2026-09-10 15:30 | yes | — | yes | 60 | Up | Y | Y | Y | xx.... |
| 63 | 1789054500 | 2026-09-10 15:35 | yes | — | yes | 61 | Up | Y | Y | Y | xx.... |
| 64 | 1789054800 | 2026-09-10 15:40 | yes | — | yes | 62 | Down | Y | Y | Y | xx.... |
| 65 | 1789055100 | 2026-09-10 15:45 | yes | — | yes | 63 | Down | Y | Y | Y | xx.... |
| 66 | 1789055400 | 2026-09-10 15:50 | yes | — | yes | 64 | Up | Y | N | N | xx.... |
| 67 | 1789055700 | 2026-09-10 15:55 | yes | — | yes | 65 | Up | Y | Y | Y | xx.... |
| 68 | 1789056000 | 2026-09-10 16:00 | yes | — | yes | 66 | Down | Y | Y | Y | .x.... |
| 69 | 1789056300 | 2026-09-10 16:05 | yes | — | yes | 67 | Down | Y | Y | Y | xx.... |
| 70 | 1789056600 | 2026-09-10 16:10 | yes | — | yes | 68 | Up | Y | Y | Y | xx.... |
| 71 | 1789056900 | 2026-09-10 16:15 | yes | — | yes | 69 | Down | Y | Y | Y | xx.... |
| 72 | 1789057200 | 2026-09-10 16:20 | no | disconnect | yes | — | — | — | — | — | — |
| 73 | 1789057500 | 2026-09-10 16:25 | yes | — | yes | 70 | Down | Y | Y | Y | xx.... |
| 74 | 1789057800 | 2026-09-10 16:30 | yes | — | yes | 71 | Down | Y | N | Y | xx.... |
| 75 | 1789058100 | 2026-09-10 16:35 | yes | — | yes | 72 | Up | Y | Y | Y | xx.... |
| 76 | 1789058400 | 2026-09-10 16:40 | yes | — | yes | 73 | Up | Y | Y | Y | xx.... |
| 77 | 1789058700 | 2026-09-10 16:45 | yes | — | yes | 74 | Up | Y | Y | Y | xx.... |
| 78 | 1789059000 | 2026-09-10 16:50 | yes | — | yes | 75 | Down | Y | Y | Y | xx.... |
| 79 | 1789059300 | 2026-09-10 16:55 | yes | — | yes | 76 | Up | Y | Y | Y | xx.... |
| 80 | 1789059600 | 2026-09-10 17:00 | yes | — | yes | 77 | Down | Y | Y | Y | xx.... |
| 81 | 1789059900 | 2026-09-10 17:05 | yes | — | yes | 78 | Up | Y | Y | Y | xx.... |
| 82 | 1789060200 | 2026-09-10 17:10 | yes | — | yes | 79 | Up | Y | Y | Y | xx.... |
| 83 | 1789060500 | 2026-09-10 17:15 | yes | — | yes | 80 | Down | Y | Y | Y | xx.... |
| 84 | 1789060800 | 2026-09-10 17:20 | yes | — | yes | 81 | Up | Y | Y | Y | xx.... |
| 85 | 1789061100 | 2026-09-10 17:25 | yes | — | yes | 82 | Up | Y | N | Y | xx.... |
| 86 | 1789061400 | 2026-09-10 17:30 | yes | — | yes | 83 | Up | Y | Y | Y | xx.... |
| 87 | 1789061700 | 2026-09-10 17:35 | yes | — | yes | 84 | Down | Y | Y | Y | xx.... |
| 88 | 1789062000 | 2026-09-10 17:40 | yes | — | yes | 85 | Down | Y | Y | Y | xx.... |
| 89 | 1789062300 | 2026-09-10 17:45 | yes | — | yes | 86 | Up | Y | Y | Y | xx.... |
| 90 | 1789062600 | 2026-09-10 17:50 | yes | — | yes | 87 | Up | Y | Y | Y | xx.... |
| 91 | 1789062900 | 2026-09-10 17:55 | yes | — | yes | 88 | Down | Y | Y | Y | xx.... |
| 92 | 1789063200 | 2026-09-10 18:00 | yes | — | yes | 89 | Down | Y | Y | Y | xx.... |
| 93 | 1789063500 | 2026-09-10 18:05 | yes | — | yes | 90 | Down | Y | Y | Y | xx.... |
| 94 | 1789063800 | 2026-09-10 18:10 | yes | — | yes | 91 | Down | Y | N | N | xx.... |
| 95 | 1789064100 | 2026-09-10 18:15 | yes | — | yes | 92 | Up | Y | Y | Y | xx.... |
| 96 | 1789064400 | 2026-09-10 18:20 | no | disconnect | yes | — | — | — | — | — | — |
| 97 | 1789064700 | 2026-09-10 18:25 | yes | — | yes | 93 | Down | Y | Y | Y | xx.... |
| 98 | 1789065000 | 2026-09-10 18:30 | yes | — | yes | 94 | Down | Y | Y | N | xx.... |
| 99 | 1789065300 | 2026-09-10 18:35 | yes | — | yes | 95 | Up | Y | Y | Y | xx.... |
| 100 | 1789065600 | 2026-09-10 18:40 | yes | — | yes | 96 | Down | Y | Y | N | xx.... |
| 101 | 1789065900 | 2026-09-10 18:45 | yes | — | yes | 97 | Down | Y | Y | Y | xx.... |
| 102 | 1789066200 | 2026-09-10 18:50 | yes | — | yes | 98 | Up | Y | Y | Y | xx.... |
| 103 | 1789066500 | 2026-09-10 18:55 | yes | — | yes | 99 | Down | Y | Y | Y | xx.... |
| 104 | 1789066800 | 2026-09-10 19:00 | yes | — | yes | 100 | Down | Y | Y | Y | xx.... |
| 105 | 1789067100 | 2026-09-10 19:05 | yes | — | yes | 101 | Down | Y | Y | Y | xx.... |
| 106 | 1789067400 | 2026-09-10 19:10 | yes | — | yes | 102 | Down | Y | Y | Y | xx.... |
| 107 | 1789067700 | 2026-09-10 19:15 | yes | — | yes | 103 | Down | Y | Y | Y | xx.... |
| 108 | 1789068000 | 2026-09-10 19:20 | yes | — | yes | 104 | Down | Y | Y | N | xx.... |
| 109 | 1789068300 | 2026-09-10 19:25 | yes | — | yes | 105 | Up | Y | Y | Y | xx.... |
| 110 | 1789068600 | 2026-09-10 19:30 | yes | — | yes | 106 | Down | Y | Y | Y | xx.... |
| 111 | 1789068900 | 2026-09-10 19:35 | yes | — | yes | 107 | Up | Y | Y | Y | xx.... |
| 112 | 1789069200 | 2026-09-10 19:40 | yes | — | yes | 108 | Up | Y | Y | Y | xx.... |
| 113 | 1789069500 | 2026-09-10 19:45 | yes | — | yes | 109 | Down | Y | Y | Y | xx.... |
| 114 | 1789069800 | 2026-09-10 19:50 | yes | — | yes | 110 | Down | Y | Y | Y | xx.... |
| 115 | 1789070100 | 2026-09-10 19:55 | yes | — | yes | 111 | Up | Y | Y | Y | xx.... |
| 116 | 1789070400 | 2026-09-10 20:00 | yes | — | yes | 112 | Up | Y | Y | Y | xx.... |
| 117 | 1789070700 | 2026-09-10 20:05 | yes | — | yes | 113 | Up | Y | Y | Y | xx.... |
| 118 | 1789071000 | 2026-09-10 20:10 | yes | — | yes | 114 | Up | Y | Y | Y | xx.... |
| 119 | 1789071300 | 2026-09-10 20:15 | yes | — | yes | 115 | Up | Y | N | Y | xx.... |
| 120 | 1789071600 | 2026-09-10 20:20 | no | disconnect | yes | — | — | — | — | — | — |
| 121 | 1789071900 | 2026-09-10 20:25 | yes | — | yes | 116 | Down | Y | N | N | xx.... |
| 122 | 1789072200 | 2026-09-10 20:30 | yes | — | yes | 117 | Down | Y | Y | Y | xx.... |
| 123 | 1789072500 | 2026-09-10 20:35 | yes | — | yes | 118 | Down | Y | Y | N | xx.... |
| 124 | 1789072800 | 2026-09-10 20:40 | no | disconnect | yes | — | — | — | — | — | — |
| 125 | 1789073100 | 2026-09-10 20:45 | yes | — | yes | 119 | Down | Y | Y | Y | xx.... |
| 126 | 1789073400 | 2026-09-10 20:50 | yes | — | yes | 120 | Up | Y | Y | Y | xx.... |
| 127 | 1789073700 | 2026-09-10 20:55 | yes | — | yes | 121 | Down | Y | Y | Y | xx.... |
| 128 | 1789074000 | 2026-09-10 21:00 | yes | — | yes | 122 | Down | Y | Y | Y | xx.... |
| 129 | 1789074300 | 2026-09-10 21:05 | yes | — | yes | 123 | Up | Y | Y | Y | xx.... |
| 130 | 1789074600 | 2026-09-10 21:10 | yes | — | yes | 124 | Down | Y | N | Y | xx.... |
| 131 | 1789074900 | 2026-09-10 21:15 | yes | — | yes | 125 | Down | Y | Y | Y | xx.... |
| 132 | 1789075200 | 2026-09-10 21:20 | yes | — | yes | 126 | Up | Y | Y | Y | .x.... |
| 133 | 1789075500 | 2026-09-10 21:25 | yes | — | yes | 127 | Up | Y | Y | Y | xx.... |
| 134 | 1789075800 | 2026-09-10 21:30 | yes | — | yes | 128 | Down | Y | Y | Y | xx.... |
| 135 | 1789076100 | 2026-09-10 21:35 | yes | — | yes | 129 | Down | Y | Y | Y | xx.... |
| 136 | 1789076400 | 2026-09-10 21:40 | yes | — | yes | 130 | Down | Y | Y | Y | xx.... |
| 137 | 1789076700 | 2026-09-10 21:45 | yes | — | yes | 131 | Up | Y | Y | Y | xx.... |
| 138 | 1789077000 | 2026-09-10 21:50 | yes | — | yes | 132 | Down | Y | N | Y | xx.... |
| 139 | 1789077300 | 2026-09-10 21:55 | yes | — | yes | 133 | Down | Y | Y | N | xx.... |
| 140 | 1789077600 | 2026-09-10 22:00 | yes | — | yes | 134 | Up | Y | N | Y | xx.... |
| 141 | 1789077900 | 2026-09-10 22:05 | yes | — | yes | 135 | Up | Y | N | Y | xx.... |
| 142 | 1789078200 | 2026-09-10 22:10 | yes | — | yes | 136 | Down | Y | Y | Y | xx.... |
| 143 | 1789078500 | 2026-09-10 22:15 | yes | — | yes | 137 | Up | Y | Y | Y | xx.... |
| 144 | 1789078800 | 2026-09-10 22:20 | yes | — | yes | 138 | Down | Y | Y | Y | xx.... |
| 145 | 1789079100 | 2026-09-10 22:25 | yes | — | yes | 139 | Down | Y | Y | Y | xx.... |
| 146 | 1789079400 | 2026-09-10 22:30 | yes | — | yes | 140 | Down | Y | Y | Y | xx.... |
| 147 | 1789079700 | 2026-09-10 22:35 | yes | — | yes | 141 | Down | Y | Y | Y | xx.... |
| 148 | 1789080000 | 2026-09-10 22:40 | no | disconnect | yes | — | — | — | — | — | — |
| 149 | 1789080300 | 2026-09-10 22:45 | yes | — | yes | 142 | Up | Y | Y | Y | xx.... |
| 150 | 1789080600 | 2026-09-10 22:50 | yes | — | yes | 143 | Down | Y | Y | Y | xx.... |
| 151 | 1789080900 | 2026-09-10 22:55 | yes | — | yes | 144 | Down | Y | Y | Y | xx.... |
| 152 | 1789081200 | 2026-09-10 23:00 | yes | — | yes | 145 | Down | Y | N | Y | xx.... |
| 153 | 1789081500 | 2026-09-10 23:05 | yes | — | yes | 146 | Down | Y | Y | Y | xx.... |
| 154 | 1789081800 | 2026-09-10 23:10 | yes | — | yes | 147 | Down | Y | Y | Y | xx.... |
| 155 | 1789082100 | 2026-09-10 23:15 | yes | — | yes | 148 | Up | Y | Y | Y | xx.... |
| 156 | 1789082400 | 2026-09-10 23:20 | yes | — | yes | 149 | Up | Y | Y | Y | xx.... |
| 157 | 1789082700 | 2026-09-10 23:25 | yes | — | yes | 150 | Up | Y | Y | Y | xx.... |
| 158 | 1789083000 | 2026-09-10 23:30 | yes | — | yes | 151 | Up | Y | Y | Y | xx.... |
| 159 | 1789083300 | 2026-09-10 23:35 | yes | — | yes | 152 | Up | Y | N | N | xx.... |
| 160 | 1789083600 | 2026-09-10 23:40 | yes | — | yes | 153 | Down | Y | Y | N | xx.... |
| 161 | 1789083900 | 2026-09-10 23:45 | yes | — | yes | 154 | Down | Y | Y | Y | xx.... |
| 162 | 1789084200 | 2026-09-10 23:50 | yes | — | yes | 155 | Down | Y | Y | Y | xx.... |
| 163 | 1789084500 | 2026-09-10 23:55 | yes | — | yes | 156 | Down | Y | Y | Y | xx.... |
| 164 | 1789084800 | 2026-09-11 00:00 | yes | — | yes | 157 | Up | Y | Y | Y | xx.... |
| 165 | 1789085100 | 2026-09-11 00:05 | yes | — | yes | 158 | Up | Y | Y | Y | xx.... |
| 166 | 1789085400 | 2026-09-11 00:10 | no | disconnect | yes | — | — | — | — | — | — |
| 167 | 1789085700 | 2026-09-11 00:15 | no | disconnect | yes | — | — | — | — | — | — |
| 168 | 1789086000 | 2026-09-11 00:20 | yes | — | yes | 159 | Up | Y | Y | Y | xx.... |
| 169 | 1789086300 | 2026-09-11 00:25 | yes | — | yes | 160 | Down | Y | Y | N | xx.... |
| 170 | 1789086600 | 2026-09-11 00:30 | yes | — | yes | 161 | Down | Y | Y | Y | xx.... |
| 171 | 1789086900 | 2026-09-11 00:35 | yes | — | yes | 162 | Up | Y | Y | Y | xx.... |
| 172 | 1789087200 | 2026-09-11 00:40 | yes | — | yes | 163 | Down | Y | Y | Y | ...... |
| 173 | 1789087500 | 2026-09-11 00:45 | yes | — | yes | 164 | Up | Y | Y | Y | xx.... |
| 174 | 1789087800 | 2026-09-11 00:50 | yes | — | yes | 165 | Up | Y | Y | Y | xx.... |
| 175 | 1789088100 | 2026-09-11 00:55 | yes | — | yes | 166 | Up | Y | Y | Y | xx.... |
| 176 | 1789088400 | 2026-09-11 01:00 | yes | — | yes | 167 | Up | Y | Y | Y | xx.... |
| 177 | 1789088700 | 2026-09-11 01:05 | yes | — | yes | 168 | Down | Y | Y | Y | xx.... |
| 178 | 1789089000 | 2026-09-11 01:10 | no | disconnect | yes | — | — | — | — | — | — |
| 179 | 1789089300 | 2026-09-11 01:15 | no | disconnect | yes | — | — | — | — | — | — |
| 180 | 1789089600 | 2026-09-11 01:20 | yes | — | yes | 169 | Down | Y | Y | Y | xx.... |
| 181 | 1789089900 | 2026-09-11 01:25 | yes | — | yes | 170 | Down | Y | Y | Y | xx.... |
| 182 | 1789090200 | 2026-09-11 01:30 | yes | — | yes | 171 | Down | Y | Y | Y | xx.... |
| 183 | 1789090500 | 2026-09-11 01:35 | yes | — | yes | 172 | Up | Y | Y | Y | xx.... |
| 184 | 1789090800 | 2026-09-11 01:40 | yes | — | yes | 173 | Up | Y | Y | Y | xx.... |
| 185 | 1789091100 | 2026-09-11 01:45 | yes | — | yes | 174 | Up | Y | N | Y | xx.... |
| 186 | 1789091400 | 2026-09-11 01:50 | no | disconnect | yes | — | — | — | — | — | — |
| 187 | 1789091700 | 2026-09-11 01:55 | no | disconnect | yes | — | — | — | — | — | — |
| 188 | 1789092000 | 2026-09-11 02:00 | yes | — | yes | 175 | Down | Y | Y | N | xx.... |
| 189 | 1789092300 | 2026-09-11 02:05 | yes | — | yes | 176 | Down | Y | Y | Y | xx.... |
| 190 | 1789092600 | 2026-09-11 02:10 | yes | — | yes | 177 | Up | Y | Y | Y | xx.... |
| 191 | 1789092900 | 2026-09-11 02:15 | yes | — | yes | 178 | Down | Y | Y | Y | .x.... |
| 192 | 1789093200 | 2026-09-11 02:20 | yes | — | yes | 179 | Down | Y | Y | Y | xx.... |
| 193 | 1789093500 | 2026-09-11 02:25 | yes | — | yes | 180 | Down | Y | Y | Y | xx.... |
| 194 | 1789093800 | 2026-09-11 02:30 | yes | — | yes | 181 | Down | Y | Y | N | xx.... |
| 195 | 1789094100 | 2026-09-11 02:35 | yes | — | yes | 182 | Up | Y | Y | Y | xx.... |
| 196 | 1789094400 | 2026-09-11 02:40 | yes | — | yes | 183 | Down | Y | Y | Y | xx.... |
| 197 | 1789094700 | 2026-09-11 02:45 | yes | — | yes | 184 | Up | Y | Y | Y | xx.... |
| 198 | 1789095000 | 2026-09-11 02:50 | yes | — | yes | 185 | Down | Y | Y | Y | xx.... |
| 199 | 1789095300 | 2026-09-11 02:55 | yes | — | yes | 186 | Up | Y | Y | N | xx.... |
| 200 | 1789095600 | 2026-09-11 03:00 | yes | — | yes | 187 | Down | Y | N | Y | xx.... |
| 201 | 1789095900 | 2026-09-11 03:05 | yes | — | yes | 188 | Down | Y | Y | Y | xx.... |
| 202 | 1789096200 | 2026-09-11 03:10 | yes | — | yes | 189 | Up | Y | Y | Y | xx.... |
| 203 | 1789096500 | 2026-09-11 03:15 | yes | — | yes | 190 | Down | Y | Y | Y | xx.... |
| 204 | 1789096800 | 2026-09-11 03:20 | yes | — | yes | 191 | Down | Y | Y | Y | xx.... |
| 205 | 1789097100 | 2026-09-11 03:25 | yes | — | yes | 192 | Up | Y | Y | Y | xx.... |
| 206 | 1789097400 | 2026-09-11 03:30 | yes | — | yes | 193 | Down | Y | Y | Y | xx.... |
| 207 | 1789097700 | 2026-09-11 03:35 | yes | — | yes | 194 | Up | Y | Y | Y | xx.... |
| 208 | 1789098000 | 2026-09-11 03:40 | yes | — | yes | 195 | Down | Y | N | N | xx.... |
| 209 | 1789098300 | 2026-09-11 03:45 | yes | — | yes | 196 | Down | Y | Y | Y | xx.... |
| 210 | 1789098600 | 2026-09-11 03:50 | no | disconnect | yes | — | — | — | — | — | — |
| 211 | 1789098900 | 2026-09-11 03:55 | no | disconnect | yes | — | — | — | — | — | — |
| 212 | 1789099200 | 2026-09-11 04:00 | yes | — | yes | 197 | Up | Y | Y | Y | xx.... |
| 213 | 1789099500 | 2026-09-11 04:05 | yes | — | yes | 198 | Up | Y | Y | Y | xx.... |
| 214 | 1789099800 | 2026-09-11 04:10 | yes | — | yes | 199 | Up | Y | N | Y | xx.... |
| 215 | 1789100100 | 2026-09-11 04:15 | yes | — | yes | 200 | Down | Y | Y | N | xx.... |

### 2.11 V3 per interval

| T0 | S1 msgs | S1 max gap ms | S2 msgs | S2 max gap ms | S3 msgs | S3 max gap ms | S4 msgs | S4 max gap ms | disconnects | disconnected ms |
|---|---|---|---|---|---|---|---|---|---|---|
| 1789035900 | 401 | 2310.7 | 400 | 3284.7 | 402 | 2416.2 | 418 | 3007.2 | 0 | 0.0 |
| 1789036200 | 402 | 2324.9 | 402 | 2454.5 | 403 | 2356.2 | 420 | 1295.0 | 0 | 0.0 |
| 1789036500 | 408 | 2971.4 | 408 | 2920.5 | 408 | 2745.0 | 420 | 1295.0 | 0 | 0.0 |
| 1789036800 | 406 | 2971.4 | 406 | 2920.5 | 406 | 2745.0 | 420 | 1292.2 | 0 | 0.0 |
| 1789037100 | 406 | 2779.2 | 405 | 2599.2 | 405 | 2841.7 | 420 | 1357.5 | 0 | 0.0 |
| 1789037400 | 409 | 2184.0 | 406 | 2201.1 | 409 | 2126.2 | 419 | 2077.1 | 0 | 0.0 |
| 1789037700 | 407 | 2306.5 | 405 | 6860.9 | 408 | 2198.8 | 419 | 2017.6 | 0 | 0.0 |
| 1789038000 | 403 | 2306.5 | 401 | 6860.9 | 403 | 2179.4 | 419 | 2017.6 | 0 | 0.0 |
| 1789038300 | 402 | 2329.4 | 402 | 2266.8 | 402 | 2171.2 | 420 | 1298.3 | 0 | 0.0 |
| 1789038600 | 397 | 8659.2 | 395 | 8336.2 | 396 | 8669.8 | 420 | 1284.0 | 0 | 0.0 |
| 1789038900 | 407 | 2878.2 | 406 | 2791.6 | 405 | 2813.1 | 420 | 1284.0 | 0 | 0.0 |
| 1789039200 | 406 | 2440.2 | 405 | 2524.6 | 405 | 2561.1 | 420 | 1275.8 | 0 | 0.0 |
| 1789039500 | 409 | 2451.5 | 409 | 2420.3 | 409 | 2367.5 | 420 | 1275.8 | 0 | 0.0 |
| 1789039800 | 401 | 2925.9 | 401 | 2824.9 | 401 | 3050.8 | 420 | 1235.0 | 0 | 0.0 |
| 1789040100 | 404 | 3484.3 | 404 | 3461.8 | 404 | 3500.7 | 420 | 1319.3 | 0 | 0.0 |
| 1789040400 | 412 | 3484.3 | 412 | 3461.8 | 411 | 3500.7 | 420 | 1241.6 | 0 | 0.0 |
| 1789040700 | 402 | 2744.0 | 402 | 2676.8 | 402 | 2724.5 | 419 | 1993.7 | 0 | 0.0 |
| 1789041000 | 393 | 8551.2 | 395 | 8553.7 | 394 | 8562.6 | 418 | 3231.5 | 0 | 0.0 |
| 1789041300 | 394 | 8551.2 | 395 | 8553.7 | 395 | 8562.6 | 418 | 3231.5 | 0 | 0.0 |
| 1789041600 | 404 | 2471.1 | 404 | 2625.0 | 404 | 2764.4 | 420 | 1166.9 | 0 | 0.0 |
| 1789041900 | 408 | 2462.5 | 408 | 2283.1 | 406 | 2229.9 | 420 | 1362.2 | 0 | 0.0 |
| 1789042200 | 407 | 2462.5 | 407 | 2283.1 | 407 | 2229.9 | 419 | 2006.5 | 0 | 0.0 |
| 1789042500 | 405 | 2441.4 | 404 | 2529.6 | 405 | 2464.1 | 419 | 1977.9 | 0 | 0.0 |
| 1789042800 | 407 | 3164.6 | 407 | 3264.4 | 406 | 3720.9 | 420 | 2551.2 | 1 | 2406.4 |
| 1789043100 | 407 | 2623.7 | 406 | 2684.1 | 407 | 2746.3 | 420 | 1279.5 | 0 | 0.0 |
| 1789043400 | 404 | 2542.9 | 403 | 2572.9 | 404 | 2715.6 | 420 | 1501.9 | 0 | 0.0 |
| 1789043700 | 403 | 2736.7 | 403 | 2704.9 | 402 | 2715.6 | 420 | 1390.0 | 0 | 0.0 |
| 1789044000 | 400 | 7463.9 | 400 | 7667.9 | 400 | 7475.9 | 420 | 1326.1 | 0 | 0.0 |
| 1789044300 | 405 | 3406.9 | 405 | 3355.5 | 404 | 3379.8 | 420 | 1494.7 | 0 | 0.0 |
| 1789044600 | 401 | 2768.8 | 401 | 2630.2 | 402 | 2873.6 | 420 | 1339.1 | 0 | 0.0 |
| 1789044900 | 402 | 2507.8 | 403 | 2455.0 | 403 | 2425.2 | 420 | 1288.8 | 0 | 0.0 |
| 1789045200 | 404 | 7807.9 | 404 | 7770.0 | 402 | 7874.7 | 420 | 1339.8 | 0 | 0.0 |
| 1789045500 | 398 | 2506.6 | 398 | 2440.0 | 397 | 2604.6 | 420 | 1339.8 | 0 | 0.0 |
| 1789045800 | 404 | 2495.2 | 404 | 2442.3 | 403 | 2558.5 | 420 | 1422.0 | 0 | 0.0 |
| 1789046100 | 406 | 2495.2 | 406 | 2442.3 | 406 | 2558.5 | 420 | 1193.9 | 0 | 0.0 |
| 1789046400 | 399 | 2651.6 | 400 | 2753.4 | 399 | 2656.9 | 419 | 2021.9 | 0 | 0.0 |
| 1789046700 | 393 | 2651.6 | 394 | 2753.4 | 395 | 2656.9 | 419 | 2077.3 | 0 | 0.0 |
| 1789047000 | 392 | 7664.3 | 393 | 7570.7 | 390 | 7506.3 | 419 | 2077.3 | 0 | 0.0 |
| 1789047300 | 396 | 7664.3 | 396 | 7570.7 | 395 | 7506.3 | 420 | 1245.7 | 0 | 0.0 |
| 1789047600 | 399 | 2297.3 | 399 | 2277.7 | 397 | 2315.4 | 420 | 1284.5 | 0 | 0.0 |
| 1789047900 | 406 | 2417.1 | 406 | 2434.9 | 404 | 2384.3 | 420 | 1284.5 | 0 | 0.0 |
| 1789048200 | 405 | 2487.2 | 405 | 2449.8 | 403 | 2442.9 | 420 | 1231.9 | 0 | 0.0 |
| 1789048500 | 400 | 8324.6 | 399 | 8412.0 | 398 | 8244.6 | 420 | 1334.9 | 0 | 0.0 |
| 1789048800 | 387 | 8324.6 | 384 | 8412.0 | 386 | 8244.6 | 420 | 1334.9 | 0 | 0.0 |
| 1789049100 | 405 | 2241.9 | 403 | 2524.5 | 404 | 2124.8 | 420 | 1318.2 | 0 | 0.0 |
| 1789049400 | 399 | 8006.1 | 399 | 7912.1 | 398 | 7919.8 | 420 | 1299.2 | 0 | 0.0 |
| 1789049700 | 408 | 2859.9 | 408 | 2836.4 | 408 | 2663.1 | 420 | 1192.2 | 0 | 0.0 |
| 1789050000 | 396 | 3389.6 | 398 | 3406.6 | 397 | 4528.6 | 420 | 2663.1 | 1 | 2594.5 |
| 1789050300 | 401 | 2495.1 | 403 | 2420.4 | 402 | 2396.0 | 420 | 1324.0 | 0 | 0.0 |
| 1789050600 | 406 | 2479.8 | 406 | 2433.3 | 405 | 2350.9 | 420 | 1324.0 | 0 | 0.0 |
| 1789050900 | 396 | 8492.0 | 395 | 8790.7 | 396 | 8697.6 | 420 | 1302.7 | 0 | 0.0 |
| 1789051200 | 397 | 8492.0 | 398 | 8790.7 | 398 | 8697.6 | 420 | 1328.5 | 0 | 0.0 |
| 1789051500 | 401 | 3023.0 | 401 | 3109.7 | 401 | 3097.4 | 420 | 1328.5 | 0 | 0.0 |
| 1789051800 | 410 | 2544.4 | 410 | 2726.5 | 407 | 2812.3 | 420 | 1493.1 | 0 | 0.0 |
| 1789052100 | 405 | 2281.1 | 405 | 2311.2 | 405 | 2329.0 | 420 | 1335.2 | 0 | 0.0 |
| 1789052400 | 401 | 7418.8 | 401 | 7385.6 | 400 | 7413.6 | 420 | 1271.6 | 0 | 0.0 |
| 1789052700 | 402 | 3564.0 | 403 | 3544.1 | 403 | 3551.3 | 420 | 1310.1 | 0 | 0.0 |
| 1789053000 | 398 | 3564.0 | 398 | 3544.1 | 397 | 3937.5 | 420 | 2431.5 | 0 | 0.0 |
| 1789053300 | 411 | 2383.6 | 410 | 2365.6 | 408 | 3937.5 | 420 | 2431.5 | 0 | 0.0 |
| 1789053600 | 402 | 9297.2 | 403 | 9189.7 | 402 | 9186.8 | 420 | 1291.1 | 0 | 0.0 |
| 1789053900 | 390 | 9297.2 | 391 | 9189.7 | 390 | 9186.8 | 420 | 1319.0 | 0 | 0.0 |
| 1789054200 | 405 | 2780.9 | 405 | 3974.9 | 406 | 2730.5 | 418 | 2187.5 | 0 | 0.0 |
| 1789054500 | 410 | 2748.5 | 407 | 3974.9 | 411 | 2394.7 | 418 | 2187.5 | 0 | 0.0 |
| 1789054800 | 398 | 7665.5 | 396 | 7716.8 | 398 | 7416.7 | 419 | 1979.4 | 0 | 0.0 |
| 1789055100 | 404 | 7458.3 | 403 | 7367.0 | 400 | 7416.7 | 419 | 1979.4 | 0 | 0.0 |
| 1789055400 | 398 | 5251.4 | 397 | 7351.4 | 398 | 3537.7 | 418 | 2130.8 | 0 | 0.0 |
| 1789055700 | 401 | 5251.4 | 400 | 7351.4 | 401 | 3374.3 | 419 | 2130.8 | 0 | 0.0 |
| 1789056000 | 402 | 2688.6 | 402 | 2712.9 | 402 | 2675.8 | 420 | 1340.2 | 0 | 0.0 |
| 1789056300 | 408 | 2197.0 | 408 | 2225.2 | 408 | 2459.8 | 419 | 1862.3 | 0 | 0.0 |
| 1789056600 | 411 | 2556.8 | 412 | 2644.4 | 412 | 2971.1 | 419 | 1862.3 | 0 | 0.0 |
| 1789056900 | 411 | 2663.3 | 410 | 2757.5 | 412 | 2540.6 | 420 | 1301.0 | 0 | 0.0 |
| 1789057200 | 407 | 2689.1 | 405 | 2682.3 | 402 | 3908.5 | 416 | 2976.3 | 1 | 2615.8 |
| 1789057500 | 399 | 7326.8 | 401 | 6825.1 | 400 | 7453.9 | 419 | 2050.3 | 0 | 0.0 |
| 1789057800 | 406 | 2656.6 | 406 | 2638.7 | 406 | 2648.9 | 420 | 1351.4 | 0 | 0.0 |
| 1789058100 | 407 | 2819.2 | 408 | 2788.1 | 408 | 2665.5 | 419 | 1952.5 | 0 | 0.0 |
| 1789058400 | 398 | 2487.8 | 393 | 3830.3 | 398 | 2594.6 | 420 | 1281.4 | 0 | 0.0 |
| 1789058700 | 401 | 2487.8 | 401 | 2554.4 | 402 | 2594.6 | 420 | 1255.4 | 0 | 0.0 |
| 1789059000 | 403 | 2518.5 | 403 | 2727.3 | 404 | 2585.1 | 418 | 2021.5 | 0 | 0.0 |
| 1789059300 | 400 | 2518.5 | 401 | 2727.3 | 401 | 2585.1 | 418 | 2021.5 | 0 | 0.0 |
| 1789059600 | 405 | 2445.9 | 405 | 2492.9 | 405 | 2465.9 | 420 | 1336.1 | 0 | 0.0 |
| 1789059900 | 407 | 2734.9 | 406 | 2659.7 | 406 | 2703.9 | 420 | 1325.2 | 0 | 0.0 |
| 1789060200 | 398 | 8821.9 | 398 | 8887.3 | 398 | 8924.6 | 420 | 1290.2 | 0 | 0.0 |
| 1789060500 | 411 | 2265.5 | 411 | 2302.1 | 411 | 2194.8 | 420 | 1287.5 | 0 | 0.0 |
| 1789060800 | 407 | 3224.3 | 407 | 3188.2 | 407 | 3262.1 | 419 | 2025.1 | 0 | 0.0 |
| 1789061100 | 406 | 2427.8 | 406 | 2337.2 | 406 | 2357.2 | 420 | 1597.8 | 0 | 0.0 |
| 1789061400 | 394 | 9316.7 | 395 | 9109.1 | 394 | 9250.8 | 420 | 1597.8 | 0 | 0.0 |
| 1789061700 | 405 | 2510.2 | 406 | 2447.1 | 406 | 2490.2 | 420 | 1357.0 | 0 | 0.0 |
| 1789062000 | 408 | 2826.8 | 407 | 2629.2 | 408 | 2765.5 | 420 | 1376.7 | 0 | 0.0 |
| 1789062300 | 409 | 2826.8 | 408 | 2629.2 | 409 | 2765.5 | 420 | 1349.6 | 0 | 0.0 |
| 1789062600 | 396 | 8598.1 | 395 | 8797.7 | 395 | 8747.5 | 419 | 2024.3 | 0 | 0.0 |
| 1789062900 | 396 | 8598.1 | 395 | 8797.7 | 395 | 8747.5 | 420 | 1511.9 | 0 | 0.0 |
| 1789063200 | 404 | 2272.7 | 404 | 2288.5 | 403 | 2254.7 | 420 | 1319.3 | 0 | 0.0 |
| 1789063500 | 411 | 2081.3 | 411 | 2027.2 | 411 | 2046.7 | 420 | 1304.1 | 0 | 0.0 |
| 1789063800 | 408 | 2706.0 | 407 | 2562.8 | 407 | 2564.4 | 420 | 1472.0 | 0 | 0.0 |
| 1789064100 | 400 | 7520.2 | 399 | 7627.2 | 399 | 7500.0 | 420 | 1213.1 | 0 | 0.0 |
| 1789064400 | 397 | 7520.2 | 397 | 7627.2 | 395 | 7500.0 | 418 | 3228.2 | 1 | 2651.5 |
| 1789064700 | 409 | 2827.5 | 409 | 2806.5 | 410 | 2830.7 | 418 | 3063.7 | 0 | 0.0 |
| 1789065000 | 406 | 7040.4 | 406 | 6924.9 | 406 | 6841.2 | 420 | 2908.8 | 0 | 0.0 |
| 1789065300 | 411 | 2521.2 | 411 | 2537.9 | 411 | 2802.4 | 420 | 1259.9 | 0 | 0.0 |
| 1789065600 | 408 | 2205.1 | 408 | 2182.8 | 408 | 2189.4 | 420 | 1288.9 | 0 | 0.0 |
| 1789065900 | 404 | 2318.8 | 406 | 2216.2 | 406 | 2383.4 | 420 | 1477.6 | 0 | 0.0 |
| 1789066200 | 406 | 3407.4 | 407 | 3435.9 | 408 | 3382.3 | 420 | 1477.6 | 0 | 0.0 |
| 1789066500 | 401 | 3407.4 | 401 | 3435.9 | 401 | 3382.3 | 420 | 1314.3 | 0 | 0.0 |
| 1789066800 | 403 | 2751.7 | 405 | 2606.0 | 405 | 2557.9 | 420 | 1300.6 | 0 | 0.0 |
| 1789067100 | 402 | 7703.9 | 404 | 7824.1 | 403 | 7678.9 | 420 | 1401.5 | 0 | 0.0 |
| 1789067400 | 405 | 7703.9 | 405 | 7824.1 | 405 | 7678.9 | 419 | 1936.3 | 0 | 0.0 |
| 1789067700 | 411 | 2224.2 | 411 | 2290.6 | 410 | 2188.3 | 420 | 1211.7 | 0 | 0.0 |
| 1789068000 | 406 | 2188.9 | 407 | 2202.3 | 406 | 2109.0 | 420 | 1268.9 | 0 | 0.0 |
| 1789068300 | 400 | 2228.8 | 399 | 2267.5 | 401 | 2258.3 | 420 | 1250.2 | 0 | 0.0 |
| 1789068600 | 414 | 2228.8 | 414 | 2267.5 | 414 | 2258.3 | 420 | 1327.9 | 0 | 0.0 |
| 1789068900 | 411 | 2230.0 | 412 | 2198.9 | 412 | 2167.3 | 420 | 1166.5 | 0 | 0.0 |
| 1789069200 | 397 | 8192.9 | 397 | 8102.3 | 396 | 8082.9 | 420 | 1276.2 | 0 | 0.0 |
| 1789069500 | 403 | 2420.3 | 402 | 2453.3 | 401 | 3710.5 | 420 | 1331.3 | 0 | 0.0 |
| 1789069800 | 408 | 2174.0 | 407 | 2475.9 | 408 | 2141.2 | 420 | 1401.0 | 0 | 0.0 |
| 1789070100 | 408 | 2148.0 | 408 | 2135.9 | 406 | 2190.9 | 420 | 1278.6 | 0 | 0.0 |
| 1789070400 | 396 | 8179.1 | 396 | 8052.2 | 396 | 8271.5 | 420 | 1212.0 | 0 | 0.0 |
| 1789070700 | 404 | 8179.1 | 403 | 8052.2 | 401 | 8271.5 | 420 | 1248.8 | 0 | 0.0 |
| 1789071000 | 408 | 2126.6 | 408 | 2292.6 | 408 | 2225.0 | 420 | 1136.4 | 0 | 0.0 |
| 1789071300 | 406 | 3985.4 | 407 | 3966.3 | 406 | 4013.2 | 420 | 1237.6 | 0 | 0.0 |
| 1789071600 | 394 | 8704.3 | 395 | 8573.6 | 394 | 8641.8 | 419 | 2440.6 | 1 | 2366.8 |
| 1789071900 | 403 | 8704.3 | 404 | 8573.6 | 404 | 8641.8 | 420 | 1451.9 | 0 | 0.0 |
| 1789072200 | 410 | 2165.1 | 410 | 2157.9 | 410 | 2139.1 | 420 | 1336.8 | 0 | 0.0 |
| 1789072500 | 415 | 2551.8 | 414 | 2495.1 | 414 | 2625.0 | 420 | 1302.4 | 0 | 0.0 |
| 1789072800 | 375 | 33074.7 | 376 | 33057.3 | 375 | 33923.1 | 390 | 32378.1 | 1 | 32316.7 |
| 1789073100 | 412 | 2376.1 | 412 | 2291.2 | 412 | 2466.0 | 419 | 1976.5 | 0 | 0.0 |
| 1789073400 | 413 | 2177.9 | 414 | 2129.3 | 413 | 2242.5 | 420 | 1346.7 | 0 | 0.0 |
| 1789073700 | 412 | 2079.7 | 412 | 2038.9 | 412 | 1981.5 | 420 | 1337.6 | 0 | 0.0 |
| 1789074000 | 405 | 2413.5 | 406 | 2253.0 | 406 | 2254.3 | 420 | 1337.6 | 0 | 0.0 |
| 1789074300 | 404 | 8056.9 | 404 | 8032.4 | 405 | 6947.6 | 420 | 1225.2 | 0 | 0.0 |
| 1789074600 | 406 | 3174.3 | 406 | 3315.8 | 406 | 3343.2 | 419 | 1985.5 | 0 | 0.0 |
| 1789074900 | 409 | 2402.4 | 409 | 2380.9 | 409 | 2415.1 | 420 | 1362.7 | 0 | 0.0 |
| 1789075200 | 404 | 2402.4 | 403 | 2295.1 | 404 | 2201.5 | 420 | 1469.3 | 0 | 0.0 |
| 1789075500 | 402 | 7867.1 | 401 | 7863.2 | 402 | 7888.6 | 420 | 1469.3 | 0 | 0.0 |
| 1789075800 | 407 | 2506.9 | 408 | 2287.9 | 408 | 2343.7 | 420 | 1309.9 | 0 | 0.0 |
| 1789076100 | 409 | 2274.4 | 410 | 2197.8 | 410 | 2246.1 | 420 | 1260.8 | 0 | 0.0 |
| 1789076400 | 409 | 2398.7 | 408 | 2374.4 | 409 | 2369.4 | 419 | 1915.2 | 0 | 0.0 |
| 1789076700 | 405 | 2398.7 | 404 | 2374.4 | 405 | 2369.4 | 419 | 1915.2 | 0 | 0.0 |
| 1789077000 | 407 | 2302.7 | 406 | 2169.5 | 406 | 2282.0 | 420 | 1286.0 | 0 | 0.0 |
| 1789077300 | 408 | 2331.8 | 409 | 2360.8 | 409 | 2306.2 | 420 | 1351.2 | 0 | 0.0 |
| 1789077600 | 410 | 2160.2 | 411 | 1913.0 | 411 | 1976.5 | 419 | 2025.6 | 0 | 0.0 |
| 1789077900 | 396 | 7610.1 | 396 | 7602.1 | 396 | 7703.9 | 419 | 2025.6 | 0 | 0.0 |
| 1789078200 | 405 | 2399.5 | 405 | 2487.0 | 405 | 2514.6 | 420 | 1275.3 | 0 | 0.0 |
| 1789078500 | 411 | 2092.2 | 412 | 1989.6 | 411 | 2059.8 | 420 | 1306.8 | 0 | 0.0 |
| 1789078800 | 401 | 7522.7 | 400 | 7540.4 | 401 | 7580.4 | 420 | 1181.0 | 0 | 0.0 |
| 1789079100 | 413 | 2186.2 | 412 | 2243.3 | 413 | 2184.4 | 420 | 1516.9 | 0 | 0.0 |
| 1789079400 | 412 | 2489.9 | 414 | 2131.6 | 414 | 2113.5 | 420 | 1516.9 | 0 | 0.0 |
| 1789079700 | 411 | 2606.1 | 413 | 2638.9 | 413 | 2631.6 | 419 | 2003.1 | 0 | 0.0 |
| 1789080000 | 402 | 7613.8 | 402 | 7605.9 | 401 | 8122.1 | 419 | 2818.6 | 1 | 2557.3 |
| 1789080300 | 404 | 7613.8 | 404 | 7605.9 | 403 | 8122.1 | 420 | 1302.8 | 0 | 0.0 |
| 1789080600 | 412 | 2202.5 | 412 | 2152.8 | 412 | 2177.3 | 420 | 1302.8 | 0 | 0.0 |
| 1789080900 | 411 | 2036.4 | 410 | 2032.6 | 411 | 1997.7 | 420 | 1275.1 | 0 | 0.0 |
| 1789081200 | 413 | 2290.7 | 412 | 2319.6 | 413 | 2251.3 | 420 | 1413.3 | 0 | 0.0 |
| 1789081500 | 412 | 2290.7 | 412 | 2319.6 | 412 | 2251.3 | 420 | 1413.3 | 0 | 0.0 |
| 1789081800 | 415 | 2409.5 | 414 | 2329.9 | 415 | 2360.4 | 420 | 1452.1 | 0 | 0.0 |
| 1789082100 | 410 | 7209.2 | 411 | 7336.9 | 411 | 7410.8 | 420 | 1452.1 | 0 | 0.0 |
| 1789082400 | 408 | 7209.2 | 409 | 7336.9 | 409 | 7410.8 | 420 | 1404.1 | 0 | 0.0 |
| 1789082700 | 414 | 2323.6 | 412 | 2274.3 | 414 | 2069.0 | 420 | 1404.1 | 0 | 0.0 |
| 1789083000 | 413 | 2245.0 | 411 | 2281.3 | 413 | 2217.7 | 419 | 2519.3 | 0 | 0.0 |
| 1789083300 | 410 | 2245.0 | 411 | 2281.3 | 410 | 2217.7 | 420 | 1262.9 | 0 | 0.0 |
| 1789083600 | 408 | 8222.7 | 408 | 8224.3 | 406 | 8312.0 | 419 | 2227.3 | 0 | 0.0 |
| 1789083900 | 413 | 3042.2 | 414 | 3045.0 | 414 | 3093.3 | 419 | 2227.3 | 0 | 0.0 |
| 1789084200 | 410 | 3042.2 | 411 | 3045.0 | 411 | 3093.3 | 420 | 1280.2 | 0 | 0.0 |
| 1789084500 | 406 | 2335.9 | 406 | 2335.1 | 406 | 2388.6 | 420 | 1283.3 | 0 | 0.0 |
| 1789084800 | 414 | 2172.7 | 414 | 2101.1 | 414 | 2212.6 | 420 | 1377.1 | 0 | 0.0 |
| 1789085100 | 411 | 2129.1 | 410 | 2114.4 | 411 | 2212.6 | 419 | 2010.3 | 0 | 0.0 |
| 1789085400 | 412 | 3549.8 | 412 | 3708.0 | 413 | 3091.2 | 418 | 2715.4 | 1 | 2365.2 |
| 1789085700 | 408 | 3549.8 | 409 | 3708.0 | 409 | 3091.2 | 419 | 2715.4 | 1 | 2365.2 |
| 1789086000 | 399 | 7175.7 | 397 | 7662.8 | 399 | 6897.0 | 420 | 1281.3 | 0 | 0.0 |
| 1789086300 | 408 | 2255.2 | 406 | 2352.1 | 408 | 2275.7 | 420 | 1276.9 | 0 | 0.0 |
| 1789086600 | 408 | 2255.2 | 408 | 2288.9 | 408 | 2294.8 | 420 | 1323.6 | 0 | 0.0 |
| 1789086900 | 406 | 7468.3 | 406 | 7492.6 | 406 | 7414.9 | 420 | 1306.5 | 0 | 0.0 |
| 1789087200 | 403 | 7468.3 | 403 | 7492.6 | 404 | 7414.9 | 420 | 1285.4 | 0 | 0.0 |
| 1789087500 | 406 | 2244.4 | 406 | 2197.2 | 405 | 2738.6 | 419 | 2023.9 | 0 | 0.0 |
| 1789087800 | 412 | 7779.8 | 412 | 7731.1 | 412 | 7046.7 | 419 | 2023.9 | 0 | 0.0 |
| 1789088100 | 412 | 7779.8 | 412 | 7731.1 | 412 | 7046.7 | 420 | 1294.0 | 0 | 0.0 |
| 1789088400 | 413 | 2130.0 | 413 | 2148.6 | 413 | 2169.4 | 420 | 1253.4 | 0 | 0.0 |
| 1789088700 | 404 | 2087.0 | 404 | 2213.8 | 404 | 2121.6 | 420 | 1304.9 | 0 | 0.0 |
| 1789089000 | 396 | 7387.7 | 396 | 7251.5 | 396 | 7290.4 | 419 | 3208.9 | 1 | 2403.8 |
| 1789089300 | 408 | 3004.2 | 409 | 2491.6 | 408 | 3668.1 | 419 | 3208.9 | 1 | 2403.8 |
| 1789089600 | 415 | 2290.6 | 416 | 2336.6 | 416 | 2241.2 | 420 | 1273.3 | 0 | 0.0 |
| 1789089900 | 411 | 7562.9 | 411 | 7555.9 | 410 | 7292.6 | 420 | 1342.4 | 0 | 0.0 |
| 1789090200 | 408 | 2063.2 | 408 | 2058.7 | 407 | 2188.2 | 420 | 1303.2 | 0 | 0.0 |
| 1789090500 | 410 | 2614.6 | 410 | 2746.1 | 410 | 2738.3 | 420 | 1382.3 | 0 | 0.0 |
| 1789090800 | 411 | 2614.6 | 411 | 2746.1 | 411 | 2738.3 | 420 | 1433.8 | 0 | 0.0 |
| 1789091100 | 416 | 2065.0 | 416 | 2076.1 | 416 | 2053.0 | 420 | 1334.9 | 0 | 0.0 |
| 1789091400 | 386 | 32421.6 | 385 | 32537.5 | 384 | 33068.9 | 388 | 32370.5 | 1 | 32308.8 |
| 1789091700 | 380 | 32421.6 | 380 | 32537.5 | 379 | 33068.9 | 388 | 32370.5 | 1 | 32308.8 |
| 1789092000 | 404 | 7730.4 | 404 | 7834.0 | 405 | 7745.2 | 420 | 1455.9 | 0 | 0.0 |
| 1789092300 | 416 | 2133.4 | 414 | 2241.7 | 416 | 2146.3 | 420 | 1306.4 | 0 | 0.0 |
| 1789092600 | 406 | 3439.8 | 405 | 3183.6 | 408 | 2361.4 | 420 | 1831.1 | 0 | 0.0 |
| 1789092900 | 404 | 6556.7 | 404 | 6429.8 | 405 | 6582.0 | 420 | 1511.6 | 0 | 0.0 |
| 1789093200 | 413 | 2608.5 | 413 | 2538.3 | 412 | 2436.9 | 420 | 1285.6 | 0 | 0.0 |
| 1789093500 | 414 | 2324.5 | 413 | 2313.0 | 414 | 2265.0 | 420 | 1251.1 | 0 | 0.0 |
| 1789093800 | 411 | 2916.1 | 411 | 3058.9 | 411 | 3258.4 | 420 | 1344.3 | 0 | 0.0 |
| 1789094100 | 405 | 2916.1 | 405 | 3058.9 | 405 | 3258.4 | 420 | 1344.3 | 0 | 0.0 |
| 1789094400 | 411 | 2271.5 | 411 | 2130.8 | 411 | 2220.1 | 420 | 1266.5 | 0 | 0.0 |
| 1789094700 | 410 | 3175.9 | 410 | 3020.3 | 411 | 3927.2 | 418 | 2553.5 | 0 | 0.0 |
| 1789095000 | 406 | 8289.9 | 405 | 8131.7 | 408 | 6961.8 | 419 | 1893.9 | 0 | 0.0 |
| 1789095300 | 415 | 3108.4 | 415 | 3043.5 | 415 | 2871.9 | 417 | 2260.9 | 0 | 0.0 |
| 1789095600 | 409 | 3108.4 | 410 | 3043.5 | 409 | 2871.9 | 418 | 2027.9 | 0 | 0.0 |
| 1789095900 | 412 | 2289.1 | 412 | 2168.4 | 412 | 2155.7 | 419 | 1875.3 | 0 | 0.0 |
| 1789096200 | 413 | 2381.9 | 412 | 2338.9 | 413 | 2279.3 | 420 | 1634.1 | 0 | 0.0 |
| 1789096500 | 413 | 2512.2 | 414 | 2462.9 | 414 | 2507.4 | 420 | 1276.0 | 0 | 0.0 |
| 1789096800 | 403 | 8375.3 | 404 | 8297.0 | 404 | 8476.0 | 420 | 1333.1 | 0 | 0.0 |
| 1789097100 | 412 | 3494.4 | 413 | 3396.1 | 413 | 3377.5 | 420 | 1318.1 | 0 | 0.0 |
| 1789097400 | 411 | 3494.4 | 411 | 3396.1 | 410 | 3377.5 | 420 | 1194.9 | 0 | 0.0 |
| 1789097700 | 406 | 2174.2 | 406 | 2121.5 | 406 | 2175.6 | 420 | 1508.2 | 0 | 0.0 |
| 1789098000 | 414 | 2468.8 | 414 | 2727.8 | 414 | 2649.6 | 421 | 1667.9 | 0 | 0.0 |
| 1789098300 | 404 | 8071.0 | 404 | 8002.8 | 403 | 8071.6 | 420 | 1500.3 | 0 | 0.0 |
| 1789098600 | 402 | 2833.8 | 402 | 2734.3 | 400 | 4169.6 | 419 | 2658.2 | 1 | 2597.4 |
| 1789098900 | 409 | 2833.8 | 410 | 2734.3 | 409 | 4169.6 | 418 | 2658.2 | 1 | 2597.4 |
| 1789099200 | 411 | 3713.3 | 412 | 3706.5 | 411 | 3586.2 | 419 | 2189.6 | 0 | 0.0 |
| 1789099500 | 408 | 7936.5 | 408 | 7614.6 | 407 | 7781.3 | 420 | 1359.0 | 0 | 0.0 |
| 1789099800 | 404 | 7936.5 | 404 | 7614.6 | 403 | 7781.3 | 420 | 1634.0 | 0 | 0.0 |
| 1789100100 | 411 | 2160.1 | 411 | 2104.4 | 411 | 2218.3 | 420 | 1438.1 | 0 | 0.0 |

### 2.12 Disconnects touching the disclosed windows

- `last frame`: the outage start.
- `drop detected`: when the recorder saw it.
- `resubscribed`: the outage end.
- `session s`: the time from the previous resubscribe to this detection.
- `cause`: the exception the recorder logged at that second.

| # | last frame (UTC) | drop detected (UTC) | resubscribed (UTC) | outage ms | session s | cause | intervals touched |
|---|---|---|---|---|---|---|---|
| 1 | 2026-09-10 12:21:10.304 | 2026-09-10 12:21:10.491 | 2026-09-10 12:21:12.711 | 2406.4 | 7199.997 | server close 1001 Going away | 1789042800 |
| 2 | 2026-09-10 14:21:12.350 | 2026-09-10 14:21:12.695 | 2026-09-10 14:21:14.945 | 2594.5 | 7199.985 | server close 1001 Going away | 1789050000 |
| 3 | 2026-09-10 16:21:14.548 | 2026-09-10 16:21:14.921 | 2026-09-10 16:21:17.164 | 2615.8 | 7199.976 | server close 1001 Going away | 1789057200 |
| 4 | 2026-09-10 18:21:16.703 | 2026-09-10 18:21:17.112 | 2026-09-10 18:21:19.355 | 2651.5 | 7199.948 | server close 1001 Going away | 1789064400 |
| 5 | 2026-09-10 20:21:19.219 | 2026-09-10 20:21:19.346 | 2026-09-10 20:21:21.585 | 2366.8 | 7199.991 | server close 1001 Going away | 1789071600 |
| 6 | 2026-09-10 20:42:27.434 | 2026-09-10 20:42:57.484 | 2026-09-10 20:42:59.751 | 32316.7 | 1295.899 | no frame for 30 s (receive timeout) | 1789072800 |
| 7 | 2026-09-10 22:42:59.423 | 2026-09-10 22:42:59.733 | 2026-09-10 22:43:01.981 | 2557.3 | 7199.983 | server close 1001 Going away | 1789080000 |
| 8 | 2026-09-11 00:14:02.637 | 2026-09-11 00:14:02.728 | 2026-09-11 00:14:05.002 | 2365.2 | 5460.748 | connection lost, no close frame | 1789085400, 1789085700 |
| 9 | 2026-09-11 01:14:52.134 | 2026-09-11 01:14:52.254 | 2026-09-11 01:14:54.538 | 2403.8 | 3647.252 | connection lost, no close frame | 1789089000, 1789089300 |
| 10 | 2026-09-11 01:53:46.434 | 2026-09-11 01:54:16.480 | 2026-09-11 01:54:18.743 | 32308.8 | 2361.942 | no frame for 30 s (receive timeout) | 1789091400, 1789091700 |
| 11 | 2026-09-11 03:54:18.398 | 2026-09-11 03:54:18.736 | 2026-09-11 03:54:20.996 | 2597.4 | 7199.993 | server close 1001 Going away | 1789098600, 1789098900 |

---

## 3. Publication

- **Branch** `tz-04b-market-recorder`, head `ee2f6327390ef4d0c6169d1fba1a2ed4ae936dc3`, pushed. It was
  created from `origin/tz-04a-market-recorder` at `3895356`, as the TZ header requires.
- It carries two TZ-04b commits:
  - `05c901c` holds the analyzer and the self-tests.
  - `ee2f632` registers the two new self-test functions in the runner. `05c901c` defined them but
    did not run them. This was found while checking this report, before anything was filed.
- **Pull request** #3, <https://github.com/seahomebatumi-ai/btc-5m-twap/pull/3>, is open and **not
  merged**.
- PR #2 was already closed, unmerged, when this TZ was executed. No action was taken on it.
- **Release / asset:** none. TZ-04b requires neither.

`research/recorder/` at `ee2f632`:

| file | lines | bytes | SHA-256 | vs `3895356` |
|---|---|---|---|---|
| `analyze.py` | 788 | 33,323 | `5bade9ff56669f2c862f81e98af1050b53233d2b07e3c260e04bf64233c03230` | changed |
| `selftest.py` | 324 | 17,079 | `e682ebff8e47d29e6c5e3b37a211f558bd1ff29c6c17c141c3011f78d7ad6c92` | changed |
| `recorder.py` | 476 | 19,417 | `3d055e369a274a464f047a51e9f9ac5d697c4f91b6cfbb2ed41e1c7cc3f03d69` | identical |
| `manifest.py` | 204 | 7,580 | `79fb2950f11ed153e4449e5991ef21dca275224489784bcbee51f7659e79b005` | identical |
| `config.py` | 73 | 2,720 | `d15e1706bec56ccb4bea478c1f3ce07f54b97483fbf1f48db38fc8b494d821e7` | identical |
| `probe.py` | 227 | 9,324 | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | identical |

**Separation self-check (contract §4.2).** It was run against `origin/main` = `8334408`, before this
report was committed. The branch carries the four TZ-04a commits and the two TZ-04b commits, and all
six were checked.

```
$ git rev-list origin/main | grep -c b21c14c
0
$ git rev-list origin/main | grep -c 29470e0
0
$ git rev-list origin/main | grep -c 6ee0c5f
0
$ git rev-list origin/main | grep -c 3895356
0
$ git rev-list origin/main | grep -c 05c901c
0
$ git rev-list origin/main | grep -c ee2f632
0
$ git diff --name-only origin/main origin/tz-04b-market-recorder
CryptoReports/TZ-04a-market-recorder-corrected-report.md
CryptoTZ/TZ-04b-market-recorder-scoring.md
SYSTEM-MAP.md
research/recorder/analyze.py
research/recorder/config.py
research/recorder/manifest.py
research/recorder/probe.py
research/recorder/recorder.py
research/recorder/selftest.py
$ git diff --name-only origin/main...origin/tz-04b-market-recorder
research/recorder/analyze.py
research/recorder/config.py
research/recorder/manifest.py
research/recorder/probe.py
research/recorder/recorder.py
research/recorder/selftest.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
```

- The last command prints nothing.
- The two-dot diff also lists three non-implementation files. They are the TZ-04a report, this
  TZ's spec and `SYSTEM-MAP.md`. All three reached `main` after `3895356`, where the branch starts,
  so they differ between the two tips without the branch having touched them.
- The three-dot diff compares against the merge base. It lists only the six implementation files
  (§6 item 10).

---

## 4. Gate

> a rule is declared the settlement rule only if it agrees on **at least 199 of every 200**
> intervals scored.

| rule | agreement over N = 200 | result |
|---|---|---|
| `R1` | **1.000** (200 of 200) | **PASS** |
| `R2` | 0.875 (175 of 200) | FAIL |
| `R3` | 0.905 (181 of 200) | FAIL |

Nothing was tuned to reach this, and the gate was not reinterpreted. R1's price to beat is the
venue's own `priceToBeat` from the S7 document. This is the same source question as V1 (§6 item 1).

---

## 5. Validation

| check | count | asserted? |
|---|---|---|
| recorder self-tests, `python3 -B selftest.py` | 64 of 64 | **asserted**: each is an `assert` that aborts the run. There are 20 new ones: the start rule and its edge, non-consecutive membership, disclosure of non-members and of a missing directory, a manifest whose verdict contradicts its fields aborting the run, the integer gate, and R1/R2/R3 plus the V1 candidates at BTC magnitude. |
| exactly one start record on `3895356`, and no start after it | 1 and 0 | **asserted** in `analyze.py` |
| the TZ's 10:21:09 and the logged 10:21:10.180 give the same first T0 | 1789035900 = 1789035900 | **asserted** |
| disclosed intervals whose manifest names `3895356` as the recorder | 215 of 215 | **asserted** |
| manifest `complete` consistent with its disconnect, S6 and S7 fields | 215 of 215 | **asserted** |
| members with a settled venue outcome | 200 of 200 | **asserted** |
| analyzer determinism: three runs each of `analyze.py` and `--tables` | 3 of 3 identical, each | recorded, not asserted; hashes in §1 |
| V1, V2, V3, V6, V7 | the counts in §2 | recorded, not asserted. They are counts, and a red result is a finding. |
| V4 | 5 matching lines | recorded, not asserted — reported as returned |
| V5 | 1 of 1 required rebuild equal; 215 of 215 across the disclosed span | recorded, not asserted |
| frozen files untouched | `research/twap-divergence.py` and `research/selftest-twap-divergence.py` are absent from the three-dot diff in §3 | recorded, not asserted |

---

## 6. What could not be implemented as written

1. **Where the price to beat comes from.** §6 V1 says: "If no S6 field carries the price to beat,
   state that plainly and report V1 as unresolved."
   - In the S6 capture fetched at T0 + 5 s, no field carries it: 0 of 200 members.
   - V1 is therefore reported **unresolved** above.
   - The venue does publish the number, in the same Gamma document, once the market is settled.
     The S7 capture holds it in 200 of 200 members. The V1 counts in §2.2 are scored against that
     field and are disclosed so they need not be recomputed.
   - They are an addition to the unresolved statement, not a substitute for it. The Architect may
     discard them.
   - R1 in V2 needs a price to beat, and §6 names no source for it there. R1 uses the same S7
     field. If that source is rejected, R1's 200 of 200 falls with it.
2. **Exact match means equal as a double.** The venue serialises `priceToBeat` as a JSON number of
   at most 17 significant digits, while S1–S3 carry a 23-digit `full_accuracy_value` scaled by
   1e18. Strict Decimal equality is 0 of 200 for every candidate. For the best candidate, the
   median residual is 3.6e-12 USD, below one double ulp at this magnitude. Equality is therefore
   judged at the double the venue publishes, as the committed TZ-04a analyzer at `3895356` already
   did. Strict counts are reported beside it, and R1 uses the same convention. 0 of 200 R1 verdicts
   would change under strict Decimal.
3. **Reading conventions.**
   - "S1 at/after T0 + 300" is the first S1 report with `payload.timestamp >= (T0 + 300)·1000`.
   - "S3 at T0" and "S3 at T0 + 300" are the last S3 report with `payload.timestamp` at or before
     that instant.
   - R2's mean is over every S3 report with `payload.timestamp` in the closed interval
     [T0, T0 + 300].
   - A report is a `type: "update"` frame. The `subscribe` snapshot batch is stored but never read
     as a report, because that would be filling a gap.
   - These are the conventions of the committed TZ-04a analyzer, stated because §6 does not fix
     them.
4. **Ordered-disclosure columns.**
   - §6 lists "the three per-rule agreements" for every row. §6 V3 excludes incomplete intervals
     from V2, so the verdicts are given for members and shown as `—` for non-members.
   - Two columns were added so the rows can be checked: the venue's outcome, and the V1 match
     pattern.
5. **"Proving run".** TZ-04b §7 has no new proving run. V3, V6 and V7 are computed over the 215
   disclosed intervals. "Free space at end" was measured at authoring, 2026-09-11 17:45:52 UTC. The
   recorder checks its floors at every interval close but never logs the value, so no reading
   exists for the moment the last member closed.
6. **V5 was run more widely than asked.** The required rebuild of one interval was done. The same
   rebuild was then run over all 215 disclosed intervals.
7. **V6 is contaminated by bad SNTP replies.** Three `pool.ntp.org` replies carried era-origin
   timestamps, and `recorder.py`'s SNTP client does no stratum, leap-indicator or zero-timestamp
   check. They set every flag and dominate the `pool.ntp.org` and both-server means.
   - The host server's samples show a maximum absolute offset of 7.872 ms.
   - Nothing was filtered, and the recorder was not changed. TZ-04b says the recorder is not
     rebuilt.
8. **V7 Tier B compressed per day.** The probe counters measure raw frame text. The retained file's
   raw bytes also include the `recv_ns`/`mono_ns` line wrapper. The measured ratio, 0.096832, comes
   from the retained file and is applied to counter bytes. It is therefore a stored-format ratio
   applied to frame bytes.
9. **V4 is non-zero and not silenced.**
   - The three docstring lines are in `recorder.py` and `probe.py`. Those files are unchanged,
     because the running recorder is that code at `3895356`.
   - The two pattern lines are the V4 regex, held in the analyzer that runs it.
   - No word was reworded to move the count.
10. **Separation self-check.** The second §4.2 command lists non-implementation files because
    `main` has advanced past the branch's base. The merge-base form is added beside it (§3). Both
    are pasted as printed.
11. **The report was written from a `main` worktree, not by `git checkout main`.**
    - Checking out `main` in the primary tree deletes `research/recorder/`, which is the directory
      the running recorder was started from.
    - A `git worktree` at `/root/tz04b-work/main-wt` was used for the report commit, then removed.
    - The commit and push sequence is otherwise contract §4.1.

**State at filing.**
- No file on `main` outside `CryptoReports/` was created or modified.
- No frozen file was touched.
- `research/__pycache__/` is pre-existing and untracked.
- The Tier A recorder is still running on `3895356` and writing only under `/var/lib/btc-recorder/`.
- `/root/tz04b-work/` holds `results-1.json`, `tables-1.md` and `separation.txt`.
