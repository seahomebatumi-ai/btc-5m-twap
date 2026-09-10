# TZ-04a — Market and Oracle Recorder, corrected — REPORT

**Status: BLOCKED.** The §0 fingerprint gate **passes**. The run is blocked because the scoring set
that V1 and V2 require cannot exist: the RTDS server closes every websocket connection 7,200 seconds
after it opens, so no run of 200 consecutive `complete: true` intervals can form. **No V1–V7 result
is reported.**

Executor model: **Opus** (`claude-opus-5`), as the TZ requires.

---

## 0. Fingerprint

Read from `SYSTEM-MAP.md` at `origin/main` = `6bf734f6efcbae3271790a48adff35d3f315002c`, at authoring
time.

**Revision string read:** `2026-09-10-e`. TZ-04a requires `2026-09-10-e`, so it matches.

| anchor | required by TZ-04a §0 | computed | match |
|---|---|---|---|
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` | yes |
| `A2` — collector | `6c5089330629` | `6c5089330629` | yes |
| `A3` — phase | `0-reopened / 1-reopened / 2-not-started` | `0-reopened / 1-reopened / 2-not-started` | yes |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b` | yes |

`A1` was not copied from the map. At the start of execution the Release asset was fetched
anonymously and hashed: 76,818,669 bytes, SHA-256
`229a944f2d5111c3e68b1fa0630f8e8658356147f9669d18665e575b60f3716b`. `A2` and `A4` are the first
12 hex characters of the SHA-256 values below. `A3` was read from map §5.

### Fingerprint table

The table covers `wc -l`, bytes and `sha256sum` for `SYSTEM-MAP.md` and for every file the map's §0
table lists. The values are read from `origin/main` at authoring time.

| path | lines | bytes | state | SHA-256 | matches map |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 230 | 14,822 | reported | `3e867547ccf1794ffbb939a6e7357a5eae95f13aec4a4734e3b0c2bf53298ae5` | self-reference |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | yes |
| `research/twap-divergence.py` | 1,135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | yes |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | yes |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | yes |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | yes |

All three `frozen` rows match the hashes printed in the map, so the contract §1.4 check passes.

---

## 1. The blocker

TZ-04a §6 scores V1 and V2 "over the first **≥ 200 consecutive intervals with `complete: true`**".
§4 defines `complete` as "**zero disconnects on S1 and S3 across the whole window**, with S6 and S7
both present". §3 requires that "One RTDS socket carries S1–S4".

The RTDS server closes every connection 7,200 seconds after it opens. This was measured on two
consecutive sessions, at 7,199.997 s and 7,199.985 s, each ended by a server-initiated close frame
`1001 Going away`.

The consequences follow from the TZ's own definitions:
- **Every close is a disconnect on S1 and S3.** They share the one socket.
- **Every close makes at least one interval incomplete.** Each interval's window is 420 s on a
  300 s grid, so every instant lies inside at least one window.
- **A run of k consecutive complete intervals needs 300·(k − 1) + 420 seconds with no
  disconnect.** 200 intervals need 60,120 s. The venue allows at most 7,200 s, which caps any run
  at 23 intervals.

The scoring set therefore cannot exist. V1 and V2 cannot be scored, and the Phase 0 acceptance of at
least 199 of every 200 cannot be evaluated.

This is not repairable inside TZ-04a:
- A reconnect, however fast, is still a disconnect.
- Carrying S1–S4 on a second socket departs from §3.
- Not counting a venue-initiated close as a disconnect changes the definition of `complete`.
  Contract §10 forbids that "not even to fix an obvious error".

Under contract §2 and §9, the specification is unsatisfiable as written.

## 2. Evidence

**Instrument.** The measurements come from `research/recorder/recorder.py` at commit `3895356`, on
branch `tz-04a-market-recorder`. The recorder opens one websocket to
`wss://ws-live-data.polymarket.com` and sends a single `subscribe` message. That message carries
`crypto_prices_twap_sixty`, `crypto_prices_twap_thirty` and `crypto_prices_chainlink`, each with
`filters` `{"symbol":"btc/usd"}`, and `crypto_prices` with `{"symbol":"btcusdt"}`. It sends the text
frame `PING` every 5 seconds. Each disconnect is written to `/var/lib/btc-recorder/runtime.jsonl`
with three timestamps:

- `start_recv_ns`: the last frame received.
- `detected_recv_ns`: the moment the drop was seen.
- `end_recv_ns`: the moment the new socket was subscribed.

**The two sessions.** Verbatim records:

```
{"detected_recv_ns": 1789035670282048465, "end_recv_ns": 1789035670495282454, "kind": "disconnect", "reason": "startup", "start_recv_ns": 1789035667899090234}
{"detected_recv_ns": 1789042870491834413, "end_recv_ns": 1789042872711001432, "kind": "disconnect", "reason": "reconnect", "start_recv_ns": 1789042870304587198}
{"detected_recv_ns": 1789050072695827128, "end_recv_ns": 1789050074945134098, "kind": "disconnect", "reason": "reconnect", "start_recv_ns": 1789050072350640983}
```

The recorder log shows the close each time. `rcvd_then_sent=True` means the server's close frame
arrived first.

```
2026-09-10T12:21:10Z RTDS drop: ConnectionClosedOK(Close(code=1001, reason='Going away'), Close(code=1001, reason='Going away'), True)
2026-09-10T14:21:12Z RTDS drop: ConnectionClosedOK(Close(code=1001, reason='Going away'), Close(code=1001, reason='Going away'), True)
```

| session | socket up (UTC) | server close (UTC) | length | close frame |
|---|---|---|---|---|
| 1 | 10:21:10.495 | 12:21:10.491 | **7,199.997 s** | `1001 Going away` |
| 2 | 12:21:12.711 | 14:21:12.695 | **7,199.985 s** | `1001 Going away` |

The two lengths agree to 12 ms. The close is timer-driven, not a random fault, and the timer
restarts with each new connection.

**What it does to `complete`.** These are the runs of consecutive `complete: true` intervals in the
interval manifests on disk at authoring time:

| run | first `T0` (UTC) | last `T0` (UTC) | length | ended by |
|---|---|---|---|---|
| a | 10:10 | 10:15 | 2 | an Executor restart at 10:21:09, which deployed a recorder fix |
| b | 10:25 | 12:15 | **23** | the session-1 server close at 12:21:10 |
| c | 12:25 | 14:10 | **22** | the session-2 server close at 14:21:12 |

Run b covers the whole of session 1. Its first window opens at 10:23:30 and its last closes at
12:20:30, a disconnect-free span of 7,020 s = 300·22 + 420. That is the largest span a 7,200 s
session admits. For run c, the 14:15 interval's window closed before the 14:21:12 close. Its S7 had
not been published when this report was written, and it cannot extend the run past the bound. Every
incomplete interval in the manifests is incomplete because of a disconnect: S6 and S7 are present
in all of them.

**The rest of the disconnect history, for completeness.** None of these is a venue close.
- Three records mark Executor process starts, at 09:53:11, 10:00:55 and 10:21:10. The first two
  carry `start_recv_ns` 0, which was the convention of those two builds.
- One record marks a silent stall. The last frame arrived at 10:04:25.035, the recorder's 30 s
  receive timeout fired, and it reconnected at 10:04:58.373. That build logged the stall's start at
  detection, 10:04:56.124, rather than at the last frame.

**Not documented.** The Polymarket RTDS documentation, <https://docs.polymarket.com/market-data/websocket/rtds>,
states no maximum connection duration, session limit or forced-disconnect interval. The handshake
is answered by Cloudflare (`Server: cloudflare`, `CF-RAY …-WAW`) and carries no statement of a limit
either. The cap is established by measurement only.

### State at filing

- **Implementation.** The code is on branch `tz-04a-market-recorder`, head
  `3895356aff853f2fcb1b030b1502acb95b16f0a5`, pushed. PR #2 is open and **not merged**.
  `research/recorder/` exists only on that branch.
- **Separation self-check (contract §4.2).** Run against `origin/main` = `6bf734f`, before this
  report was committed:

  ```
  $ git rev-list origin/main | grep -c b21c14c
  0
  $ git rev-list origin/main | grep -c 29470e0
  0
  $ git rev-list origin/main | grep -c 6ee0c5f
  0
  $ git rev-list origin/main | grep -c 3895356
  0
  $ git diff --name-only origin/main origin/tz-04a-market-recorder
  research/recorder/analyze.py
  research/recorder/config.py
  research/recorder/manifest.py
  research/recorder/probe.py
  research/recorder/recorder.py
  research/recorder/selftest.py
  $ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
  ```

  The last command prints nothing.
- **Tier A is still running.** It has been up since 10:21:09 UTC on `3895356`, writing only under
  `/var/lib/btc-recorder/`, outside the repository. It was not stopped, because TZ-04a §7 says:
  "Tier A is not stopped when this TZ closes. It keeps running until a floor in §4 is reached or a
  later TZ changes it." It never deletes anything.
- **Tier B probe.** It ran once, for 60 minutes, 09:57:33–10:57:47 UTC, then unsubscribed and
  exited. Its counters and its one retained interval stay on disk under `/var/lib/btc-recorder/`.
  They are not reported here (contract §9).
- **Nothing else changed.**
  - No file on `main` outside `CryptoReports/` was created or modified.
  - No frozen file was touched; see the hashes in §0.
  - `research/__pycache__/` is pre-existing and untracked.
  - The scratch directory `/root/tz04a-work` was removed.
  - The recorder's virtualenv `/root/tz04a-env` stays, because the running recorder uses it.
