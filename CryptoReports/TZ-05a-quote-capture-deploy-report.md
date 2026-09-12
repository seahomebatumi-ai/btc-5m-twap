# TZ-05a — Quote Capture, deployment only — REPORT

**Status: executed.** The §0 fingerprint gate **passes** and so does the host gate. Tier C is
deployed, both §5 repairs are applied, the recorder was restarted onto the new commit and left
running, and the four intervals whose whole window lies after the restart record have closed.

- **Acceptance passes.** The rule fixed in §6 before any data was seen is *at least one of the
  four intervals must have all 14 reads at HTTP 200*. **Four of four** did — 56 of 56 reads
  returned HTTP 200 with a body that parses as JSON.
- All four intervals also carry `complete = true`, so the restart cost the scoring set nothing.
- **W7 carries no rejection.** R-b rejected nothing over this 22-minute window; the invalid
  replies System Map §7 item 10 records are intermittent. The repair is evidenced by self-test
  against the exact reply that was observed, not by a live rejection here. Reported as it is.

Executor model: **Opus** (`claude-opus-5`), as the TZ requires.

---

## 0. Fingerprint

Read from `SYSTEM-MAP.md` at `origin/main` = `3c8c86c057bbab6569743683cdf27ba98026028a`, at
authoring time.

**Revision string read:** `2026-09-11-c`. TZ-05a §0 requires `2026-09-11-c`. Match.

| anchor | required by TZ-05a §0 | computed | match |
|---|---|---|---|
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` | yes |
| `A2` — collector | `6c5089330629` | `6c5089330629` | yes |
| `A3` — phase | `0-complete / 1-open / 2-not-started` | `0-complete / 1-open / 2-not-started` | yes |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b` | yes |

`A1` was not copied from the map. Before any other work the Release asset was fetched
anonymously and hashed: 76,818,669 bytes, SHA-256
`229a944f2d5111c3e68b1fa0630f8e8658356147f9669d18665e575b60f3716b`. The downloaded copy was then
deleted from scratch space. `A2` and `A4` are the first 12 hex characters of the SHA-256 values
below. `A3` was read from map §5.

### Fingerprint table

`wc -l`, bytes and `sha256sum` for `SYSTEM-MAP.md` and for every file the map's §0 table lists at
authoring time, read from `origin/main`.

| path | lines | bytes | state | SHA-256 | matches map |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 262 | 20,504 | reported | `45ed830069a75fb2c1781c30a5f9c9f0a5d7c5f9c9821eab25041041bed4045b` | self-reference |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | yes |
| `research/twap-divergence.py` | 1,135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | yes |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | yes |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | yes |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | yes |

All three `frozen` rows match the hashes printed in the map, so the contract §1.4 check passes.

### Host gate — the three observed values

Checked mechanically before any other work, at `2026-09-12T08:53Z`.

| check | required by TZ-05a §0 | observed | match |
|---|---|---|---|
| `/var/lib/btc-recorder/` | exists, holds interval directories | exists; **565** interval directories under `btc-updown-5m/` | yes |
| the recorder process | running, its commit in the newest `runtime.jsonl` start record | pid `3762200`, up 1 d 22:31; newest start record `sha = 3895356aff853f2fcb1b030b1502acb95b16f0a5` | yes |
| the filesystem | device `/dev/vda2`, total exactly `31,612,203,008` bytes | `/dev/vda2`, `31,612,203,008` bytes | yes |

This is the capture host. TZ-05's routing blocker does not recur.

---

## 1. Input

**Tier A was not re-collected, and nothing already on disk was re-read for a measurement.** The
four scored intervals are capture this deployment produced; that is the point of the TZ.

| input | what it supplies |
|---|---|
| `/var/lib/btc-recorder/runtime.jsonl` | W1, and the clock records for W7 |
| `/var/lib/btc-recorder/btc-updown-5m/{1789206900, 1789207200, 1789207500, 1789207800}/` | W2–W5 and W8, each directory read through its own `manifest.json`, `quotes.jsonl.gz` and `gamma.json` |
| `/var/lib/btc-recorder/recorder.log` | the close lines quoted in W1 |
| `origin/main` at `3c8c86c` | the §0 fingerprint table |

**Network reads made by this execution**, all anonymous and read-only, none of them a capture:

1. the `A1` Release asset, once, for the anchor;
2. `https://docs.polymarket.com/api-reference/market-data/get-order-book`, for §3's endpoint;
3. a pre-deployment dry run off the capture path — two live `/book` reads plus one deliberate
   read of a non-existent token id, to prove the 200 and non-200 paths before touching the
   recorder;
4. one `GET https://gamma-api.polymarket.com/markets/slug/btc-updown-5m-1789206900` and one
   `GET https://clob.polymarket.com/markets/0x927a2c05aad42f746dfb7facf305c373a4383ef91e19fd1189f46f68aed2ac98`
   at authoring, for the W4 token-to-outcome mapping.

No credential of any kind was presented on any of them. The recorder sends no header beyond its
`User-Agent`.

**The order-book endpoint, verbatim.**

```
GET https://clob.polymarket.com/book?token_id={token_id}
```

Read on 2026-09-12 from the current documentation at
`https://docs.polymarket.com/api-reference/market-data/get-order-book`, which gives the method
and path as `GET /book`, the production base host as `https://clob.polymarket.com`, and
`token_id` — "Token ID (asset ID)" — as the one required query parameter. It is not carried from
memory. It is held in `config.CLOB_BOOK_BY_TOKEN`.

---

## 2. Measurements

The scoring set is fixed by §6: the first four intervals whose **whole window** `[T0-90, T0+330]`
lies after the Tier C restart record at `recv_ns = 1789206785264516934`.

| # | `T0` | window (UTC) |
|---|---|---|
| 1 | `1789206900` | 09:53:30 → 10:00:30 |
| 2 | `1789207200` | 09:58:30 → 10:05:30 |
| 3 | `1789207500` | 10:03:30 → 10:10:30 |
| 4 | `1789207800` | 10:08:30 → 10:15:30 |

`1789206600` is excluded: its window opens at 09:58:30 — before the restart — and the log shows
Tier C correctly refused to read its three already-past checkpoints.

### W1 — the restart

The restart record, verbatim from `/var/lib/btc-recorder/runtime.jsonl`:

```json
{"captured_bytes": 55159600, "free_bytes": 7871356928, "kind": "start", "recv_ns": 1789206785264516934, "sha": "4216c04673ced76b5b2ac60ef57c9abedc46f9b9"}
```

| item | value |
|---|---|
| new commit | `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` |
| process id | `228592` |
| start time | `2026-09-12T09:53:04Z` (`ps`), first log line `09:53:05Z`, record `recv_ns` `1789206785264516934` = `09:53:05.264516934Z` |
| command | `/root/tz04a-env/venv/bin/python -B -u recorder.py`, cwd `/root/btc-5m-twap/research/recorder` |
| start records on that commit | **1 of 1** — asserted |
| start records in the log, total | 4 |
| start records after this one | **0** — asserted |

The predecessor was pid `3762200` on `3895356`, up 1 d 23:25. The first log lines of the new
process:

```
2026-09-12T09:53:05Z recorder sha=4216c04673ced76b5b2ac60ef57c9abedc46f9b9 root=/var/lib/btc-recorder
2026-09-12T09:53:05Z pre-run floors: free=7871356928 (floor 2000000000) captured=55159600 (cap 4000000000)
2026-09-12T09:53:05Z recovering interval 1789206300
2026-09-12T09:53:05Z interval 1789206600: 3 checkpoints had already passed and are not read
2026-09-12T09:53:05Z RTDS connected
```

### W2 — reads

14 reads per interval: two token ids at each of `tau ∈ {240, 180, 120, 90, 60, 30, 10}`.

| `T0` | reads | HTTP 200 | non-200 | failed | `quotes_complete` | `complete` |
|---|---|---|---|---|---|---|
| `1789206900` | 14 | 14 | 0 | 0 | **true** | true |
| `1789207200` | 14 | 14 | 0 | 0 | **true** | true |
| `1789207500` | 14 | 14 | 0 | 0 | **true** | true |
| `1789207800` | 14 | 14 | 0 | 0 | **true** | true |

Per `tau`, per interval, both token ids returned HTTP 200 — every one of the 28 `(interval, tau)`
cells is `[200, 200]`:

| `T0` | τ=240 | τ=180 | τ=120 | τ=90 | τ=60 | τ=30 | τ=10 |
|---|---|---|---|---|---|---|---|
| `1789206900` | 200, 200 | 200, 200 | 200, 200 | 200, 200 | 200, 200 | 200, 200 | 200, 200 |
| `1789207200` | 200, 200 | 200, 200 | 200, 200 | 200, 200 | 200, 200 | 200, 200 | 200, 200 |
| `1789207500` | 200, 200 | 200, 200 | 200, 200 | 200, 200 | 200, 200 | 200, 200 | 200, 200 |
| `1789207800` | 200, 200 | 200, 200 | 200, 200 | 200, 200 | 200, 200 | 200, 200 | 200, 200 |

**Intervals with `quotes_complete`: 4 of 4.** Total reads 56, HTTP 200 56, bodies parsing as
JSON 56.

### W3 — checkpoint timing

`quote_offsets_ms` is the signed difference between a read's `recv_ns` and its intended
checkpoint instant. `recv_ns` is stamped when the reply lands, exactly as every other stream
stamps it, so each figure includes the HTTP round trip and is positive by construction. All 56
reads succeeded, so all 56 are included, 8 per `tau`.

| `tau` | n | min (ms) | median (ms) | max (ms) |
|---|---|---|---|---|
| 240 | 8 | 45.460 | 54.123 | 64.969 |
| 180 | 8 | 47.790 | 55.175 | 62.073 |
| 120 | 8 | 48.923 | 52.803 | 101.448 |
| 90 | 8 | 46.835 | 52.047 | 72.588 |
| 60 | 8 | 49.873 | 53.811 | 87.377 |
| 30 | 8 | 43.977 | 50.093 | 56.625 |
| 10 | 8 | 44.925 | 49.102 | 76.096 |
| **all** | **56** | **43.977** | **52.386** | **101.448** |

No read landed in another checkpoint's slot; the smallest gap between checkpoints is 20 s and the
largest offset is 0.101 s.

### W4 — venue parameters

Each value as returned, once, with its source field named. Read from interval `1789206900`
(`conditionId = 0x927a2c05aad42f746dfb7facf305c373a4383ef91e19fd1189f46f68aed2ac98`).

| parameter | value as returned | source field |
|---|---|---|
| minimum tick size | `0.01` | `orderPriceMinTickSize`, S6 Gamma document |
| minimum tick size | `"0.01"` | `tick_size`, CLOB `/book` response body |
| minimum tick size | `0.01` | `minimum_tick_size`, CLOB `/markets/{condition_id}` |
| minimum order size | `"5"` | `min_order_size`, CLOB `/book` response body |
| fee schedule | `{"exponent": 1, "rate": 0.07, "rebateRate": 0.2, "takerOnly": true}` | `feeSchedule`, S6 Gamma document |
| fee type | `"crypto_fees_v2"` | `feeType`, S6 Gamma document |
| token ids | `["74577154929024372271612024448481753193867361649708699696968359704437987224792", "35574989141509485488780368137706303331558920352459466517295639310386343011250"]` | `clobTokenIds`, S6 Gamma document |
| outcome labels | `["Up", "Down"]` | `outcomes`, S6 Gamma document |

**Which field maps to which outcome.** `clobTokenIds` and `outcomes` are parallel JSON-encoded
arrays on the Gamma document, and index *i* of one is the token for index *i* of the other. That
correspondence is not assumed from position here: the venue names it explicitly, and the naming
agrees with the Gamma ordering.

| token id | outcome | source field |
|---|---|---|
| `74577154929024372271612024448481753193867361649708699696968359704437987224792` | `Up` | `tokens[0].token_id` / `tokens[0].outcome`, `GET https://clob.polymarket.com/markets/{condition_id}` |
| `35574989141509485488780368137706303331558920352459466517295639310386343011250` | `Down` | `tokens[1].token_id` / `tokens[1].outcome`, same document |

The `/book` reply for the first token carries `asset_id` equal to that token id and `market`
equal to the market's `conditionId`, so the stored bodies are self-identifying.

The published fee rate is recorded here because CANON §1.4 lists it as unverified. **No fee is
applied to anything in this report**, and nothing here is a market observation.

### W5 — footprint

| `T0` | `quotes.jsonl.gz` raw (bytes) | `quotes.jsonl.gz` stored (bytes) | Tier A stored (bytes) |
|---|---|---|---|
| `1789206900` | 61,965 | 6,176 | 58,814 |
| `1789207200` | 61,735 | 5,595 | 58,845 |
| `1789207500` | 61,933 | 6,601 | 58,777 |
| `1789207800` | 61,953 | 6,314 | 58,168 |
| **total** | **247,586** | **24,686** | **234,604** |
| **mean per interval** | 61,896.5 | 6,171.5 | 58,651 |

| quantity | exact bytes |
|---|---|
| Tier C projected per day (288 intervals × stored mean) | `1,777,392` |
| Tier C projected per day, raw | `17,826,192` |
| Tier A measured per day (System Map §2.3) | `22,073,069` |
| Tier A + Tier C projected per day | `23,850,461` |
| free before the restart, 08:58:16Z, old process still running | `7,881,748,480` |
| free recorded by the new process at start, before its first frame | `7,871,356,928` |
| free at authoring | `7,855,497,216` |
| free-space floor | `2,000,000,000` |
| cumulative capture at restart, against the `4,000,000,000` self-cap | `55,159,600` |

Tier C costs `1,777,392` bytes per day, below the `~2.4` MB the TZ estimated. Headroom above the
free-space floor is `5,855,497,216` bytes, which at `23,850,461` bytes per day is about **245
days**. Neither floor is near.

### W6 — read-only proof

The §5 R-a command, exactly as the TZ states it:

```
grep -rniE "(private[_-]?key|signer|create[_-]?order|post[_-]?order|api[_-]?secret|passphrase|l1[_-]?auth|l2[_-]?auth|wallet)" \
  research/recorder/ --include=*.py --exclude=analyze.py | grep -vE ':[[:space:]]*#|"""'
```

**Match count: 3.** Reported as returned, not reworded.

```
research/recorder/probe.py:9:Read-only: the `market` channel is public and unauthenticated. No key, signer or order path.
research/recorder/recorder.py:8:Read-only by construction. There is no order path, no CLOB authentication, no wallet, key,
research/recorder/recorder.py:9:signer or credential anywhere in this file, and no pricing arithmetic: frames are routed by
```

All three are prose inside module docstrings that deny the capability; the filter drops a
docstring line only when the `"""` marker is on that same line, which it is not for a multi-line
docstring body. The instrument is better than TZ-04b's — the file holding the pattern is excluded
and the count fell from 5 to 3 — but it is still not zero, and it is reported at 3. Tier C added
none of the three: the count was 3 before this TZ's changes and 3 after.

The excluded file is **`research/recorder/analyze.py`**. Its own read-only status is carried by
the merge-base diff in §3, which shows `analyze.py` is not in this branch's diff at all.

### W7 — clock, after R-b

Window `[1789206810, 1789208130]` — the first interval's window open to the last interval's
window close, 1,320 s. `NTP_BURST` is 4 replies per server per round and a round runs every 60 s.

| server | ip | rounds | replies attempted | accepted | **rejected** | rejection reasons | no reply | rounds with no offset |
|---|---|---|---|---|---|---|---|---|
| `108.61.73.243` | `108.61.73.243` | 20 | 80 | 80 | **0** | — | 0 | 0 |
| `pool.ntp.org` | `91.212.242.21` | 20 | 80 | 63 | **0** | — | 17 | 0 |

`no reply` counts UDP attempts that timed out or errored before a reply arrived; those are not
rejections and are not counted as such.

Resulting offsets, which R-b's absence of rejections means are unfiltered:

| server | median offset (ms) | max absolute offset (ms) |
|---|---|---|
| `108.61.73.243` | −5.065 | 8.571 |
| `pool.ntp.org` | −4.096 | 18.789 |

Per-interval `clock_offset_abs_max_ms`: `18.045`, `17.550`, `18.789`, `15.188` — all below the
`50` ms limit in `config.CLOCK_OFFSET_LIMIT_MS`, and none of them the `−3.998e12` ms artefact.

**Nothing was rejected in this window.** The window is 22 minutes and the invalid replies System
Map §7 item 10 records were intermittent over 18 hours, so this is what there is and it is
reported as such. The repair's correctness is carried by §5 below, which reconstructs the exact
reply that was observed and shows both that it would have produced an offset near `−3.998e12` ms
and that it is now rejected before it can.

### W8 — determinism

Each of the four manifests was hashed, rebuilt in place by `manifest.write()` from the interval
directory alone, and hashed again.

| `T0` | `sha256sum` before | `sha256sum` after | identical |
|---|---|---|---|
| `1789206900` | `94803def06842430e1e089a5c64e46c399751965ba84edf4b74bc58682b86e48` | `94803def06842430e1e089a5c64e46c399751965ba84edf4b74bc58682b86e48` | yes |
| `1789207200` | `a4a3961a2cdea9568929b30fb3e7b4f6dd430d9259253fefb2af9397d4e89ad4` | `a4a3961a2cdea9568929b30fb3e7b4f6dd430d9259253fefb2af9397d4e89ad4` | yes |
| `1789207500` | `4f11037208f2b96977f264b0cca89dbc7857e66382830d42ff6a56c036c46670` | `4f11037208f2b96977f264b0cca89dbc7857e66382830d42ff6a56c036c46670` | yes |
| `1789207800` | `9558d02125a47358fb5fcff7068903dabff93a817d5f57fad4c16617da27f63c` | `9558d02125a47358fb5fcff7068903dabff93a817d5f57fad4c16617da27f63c` | yes |

**4 of 4 identical**, and the equality is an `assert` that aborts the collector.

---

## 3. Publication

| item | value |
|---|---|
| branch | `tz-05a-quote-capture` |
| implementation commit | `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` |
| pull request | **#5**, open and unmerged, awaiting the Architect's verdict |
| files changed | `research/recorder/config.py`, `manifest.py`, `recorder.py`, `selftest.py` |
| Release tag / asset | none — this TZ produces no dataset |

Merge is deployment and is the Boss's action after the verdict. The **running process** is on
`4216c04` from the branch checkout; that is the deployment §3 of the TZ mandates, and it is not a
merge.

### Contract §4.2 separation self-check, verbatim

```
$ git rev-list origin/main | grep -c 4216c04673ced76b5b2ac60ef57c9abedc46f9b9
0

$ git diff --name-only origin/main origin/tz-05a-quote-capture
research/recorder/config.py
research/recorder/manifest.py
research/recorder/recorder.py
research/recorder/selftest.py

$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
(no output)
```

The first line prints `0`: the implementation is not on `main`. The diff is implementation files
only, all under `research/recorder/`. No dataset or archive is in history.

Nothing outside `research/recorder/` and `CryptoReports/` was created or modified in the
repository. All tooling and scratch space is outside it, at `/root/tz05a-work/`. The capture
itself is at `/var/lib/btc-recorder/**`, outside the repository by design.

---

## 4. Gate

The acceptance, quoted from TZ-05a §6:

> **Acceptance, fixed here before any data is seen: at least one of the four intervals must have
> all 14 reads at HTTP 200.**

| quantity | value |
|---|---|
| intervals required with 14 of 14 at HTTP 200 | 1 |
| intervals observed with 14 of 14 at HTTP 200 | **4.000** |
| reads at HTTP 200, of 56 | 56 — a rate of **1.000** |

**PASS.** Nothing was tuned to reach it; the rule and the scoring set were both fixed by the TZ
before the restart was issued. The condition is an `assert` in the collector and aborts the run
when false.

The other three intervals are reported above as counts with no threshold attached, as §6
requires: this is a deployment check, not a gate, and nothing in it is a market observation.

---

## 5. Validation

| check | count | asserted? |
|---|---|---|
| W1 — restart | 1 of 1 start record on `4216c04`; 0 start records after it | **asserted** — three asserts in the collector: the count, the record's identity, and the absence of any later start |
| W2 — reads | 56 of 56 at HTTP 200; 4 of 4 intervals `quotes_complete` | recorded, not asserted — §6 requires counts |
| W3 — checkpoint timing | 56 offsets, 8 per `tau` | recorded, not asserted |
| W4 — venue parameters | 8 parameters, each with its source field named | recorded, not asserted |
| W5 — footprint | 4 intervals, in exact bytes | recorded, not asserted |
| W6 — read-only proof | 3 matching lines | recorded, not asserted — **and it must not be**: §5 R-a requires a non-zero result to be reported as returned, so asserting zero here would be a test edited to pass |
| W7 — clock | 40 clock records, 143 replies accepted, 0 rejected, 17 with no reply | recorded, not asserted |
| W8 — determinism | 4 of 4 manifests byte-identical after rebuild | **asserted** — inequality aborts the collector |
| acceptance | 4 of 4 intervals with 14 of 14 at HTTP 200 | **asserted** |

### Self-tests

`research/recorder/selftest.py` — every check is an `assert` that aborts the run.

```
105 of 105 checks passed
```

64 of those are the pre-TZ-05a suite, unchanged and still green. The 41 added by this TZ cover:

- **Tier C geometry** — that `tau ∈ {240, 180, 120, 90, 60, 30, 10}` maps to the `t ∈ {60, 120,
  180, 210, 240, 270, 290}` the TZ prints as the same thing; that there are 14 reads per
  interval; that the HTTP timeout is strictly below the smallest gap between checkpoints, so a
  read can never run into the next slot; that a process starting mid-interval reads only the
  checkpoints still ahead, reads one that falls exactly on its instant, and reads none at all
  after the last.
- **`quotes_complete`** — true only for 14 reads, all HTTP 200, every body parsing; false on a
  single non-200, on a body that is not JSON, on fewer than 14 reads, and on no Tier C file at
  all. Each of those four cases also checks that `complete` is **unchanged**, which is what makes
  the two flags independent rather than merely differently named.
- **`quote_offsets_ms`** — that the value is signed, measured against the intended instant, and
  carries the `tau` it belongs to.
- **Determinism** — a manifest carrying Tier C rebuilds byte-identically.
- **R-b** — that the skew limit is exactly `86_400`; each of leap indicator `3`, stratum `0`,
  stratum `16`, a zero transmit timestamp and an `86_401` s skew is rejected; stratum `15` and an
  `86_399` s skew are not; the rejection reasons are counted per server; a burst rejected outright
  yields no offset rather than a spurious one; and a manifest carries a sample with no offset
  instead of dropping it. One test reconstructs the reply that actually reached this host,
  confirms it would have carried an offset near `−3.998e12` ms, and confirms it is now rejected.

---

## 6. What could not be implemented as written

**1. The restart could not be issued from inside the session.** `kill 3762200` was refused by the
Claude Code permission classifier, both on its own and inside the restart command. Nothing ran —
the old process was untouched and still had three start records at that point. The Boss ran the
two commands, which is a routing action under contract §2, and this report verifies the result
independently from `runtime.jsonl`, `ps` and the log rather than from his say-so. This is a new
sandbox limit of the same class as the Release-upload limit in map §6, and it is not a defect in
the TZ.

**2. `analyze.py` stops being re-runnable, by design.** `research/recorder/analyze.py:207`
asserts that no start record follows the `3895356` start. That assert is now false, so the TZ-04b
analysis can no longer be re-run. TZ-05a §3 sanctions the restart — "the Phase 0 scoring set is
closed and reported, so no set in flight depends on continuity" — and §2 puts `analyze.py` out of
scope, so it was **not** touched. The TZ-04b report stands as committed; its inputs are all still
on disk and any single row remains reconstructible from the interval directories. Flagged for the
Architect because the next TZ to read `analyze.py` will hit it.

**3. Manifests written before `4216c04` no longer rebuild byte-identically.** They gain
`quotes_complete` and `quote_offsets_ms`, which is exactly what §3 instructs, so this is inherent
to the TZ rather than avoidable. W8 covers the four intervals this deployment produced. No older
manifest was rebuilt or modified.

**4. A failed read needs two fields the TZ's line format does not name.** §3 fixes the line as
`recv_ns`, `mono_ns`, the body, `tau`, `token_id` and the HTTP status — but a read that produced
no reply has no status and no body. Such a line is written with `"status": null`, `"raw": null`
and an added `"error"` naming the exception; a successful line carries exactly the six fields the
TZ names and nothing else. **No failed read occurred** in the four intervals, so no such line
exists in the scored capture.

**5. A checkpoint whose instant has already passed is skipped, not read late.** §3 forbids a
failed read being retried into the next checkpoint's slot and forbids filling it; reading a
checkpoint 140 s after its instant would be the same defect wearing a different name. A process
that starts mid-interval therefore reads only the checkpoints still ahead. This fired once, on
`1789206600`, which is not in the scoring set, and is logged verbatim in W1.

**6. The token-to-outcome mapping was read from a second venue document.** §3 names the S6 Gamma
document as the source of the token ids, and it is. But Gamma gives `clobTokenIds` and `outcomes`
as parallel arrays without stating that they correspond by index, and §2 forbids reporting any
market statistic — which rules out inferring the mapping from quoted prices. One read of
`GET https://clob.polymarket.com/markets/{condition_id}` at authoring resolves it from the
venue's own `tokens[].outcome` field. That read is **not** part of the capture and is not issued
per interval; Tier C reads the order-book endpoint and nothing else.

**7. W7 has no rejection to report.** Stated in the summary and in W7 itself rather than dressed
up: over 1,320 s, 143 replies were accepted, 0 rejected and 17 never arrived. The repair is at
the point of reception and is evidenced by self-test against the observed reply. A live rejection
count needs a longer window and belongs to whichever TZ next reads the clock over one.

**8. "Free space before the restart" is reported as three figures**, because the honest answer
depends on which instant is meant: `7,881,748,480` measured at 08:58:16Z with the old process
running, `7,871,356,928` recorded by the new process at start before its first frame, and
`7,855,497,216` at authoring. All three are in W5 in exact bytes.

Nothing else. No Phase 2 gate, no scoring set, no pricer, no depth or latency work, no
aggregation, and no market statistic of any kind — not a spread, not a mid, not a depth figure.
The stored bodies contain quotes; **this report derives nothing from them**, and the first
aggregation of them is TZ-05b's, after its rule is fixed.

**The recorder is left running**, pid `228592` on `4216c04`.
