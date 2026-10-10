# TZ-26 — B3's capture: the nested pair's four books, streamed

**Canonical filename:** `TZ-26-nesting-b3-capture.md`. The committed file takes this name and no other.

**Executor model: Opus.** Network capture, a long-lived process deployed as a system unit, the stop of another,
clock discipline.

**Required System Map revision:** `2026-10-10-b`.

**Required anchors**, from map §0. A mismatch on any one is BLOCKED before any work:

| anchor | required |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `0f6c90451cbd` |
| `A6` — pricer | `729f0bcdbee3` |

**Host gate:** §0.3. This TZ runs on the capture host and nowhere else.

**When:** any time after the upload that carries this TZ and revision `2026-10-10-b`. It takes about two hours of wall
clock, most of it waiting for windows to close (§6).

**What this TZ is.** B2 read VIOLATION (TZ-24), so B3 is open (CANON PART II): can a violation be captured? Its
measurement needs what seven snapshots a window cannot show — how long an episode lasts, the episodes between
checkpoints, the depth below break-even, and the book 150 ms after a detection, where a taker's order would land.
**This TZ deploys the capture that records it, and measures nothing** (CANON hard rule 11). One service,
`btc-pairbook.service`, streams the CLOB market websocket for the four tokens of `btc-updown-15m-{T}` and
`btc-updown-5m-{T+600}` from `T+595` to `T+905` of every fifteen-minute window `T`, every frame stored verbatim with its
receive stamps, and keeps the chain book's seven `/book` checkpoints in the chain book's own line format. **It
replaces `btc-chainbook.service`**, which this TZ stops and disables, so the host runs two capture units after it, as
before. It reads no price, size, side or outcome; its proof is by counts, shapes and times. One instrument,
`research/tz26-nesting-b3-capture.py`, and one unit, `deploy/systemd/btc-pairbook.service`, Appendix A.

---

## 0. Gates

### 0.0 The work tree, first

After contract §1 steps 1 and 2, and before anything else:

```
mkdir /root/tz26-work /root/tz26-work/logs; echo "exit=$?"
```

`exit=0` proves neither existed; anything else is BLOCKED. **From here every command's output goes to
`/root/tz26-work/logs/`, one file per step, §0's included**, and nothing to the session's scratchpad. The one
exception is B-RECLAIM-OWN, §9.

### 0.1 The instrument and the unit, staged

Extract Appendix A from this TZ as the primary checkout carries it after contract §1's pull, with this script,
verbatim, its one argument the destination:

```
/root/tz04a-env/venv/bin/python -B - /root/tz26-work/stage <<'EOF'
import hashlib, os, sys
SRC = "/root/btc-5m-twap/CryptoTZ/TZ-26-nesting-b3-capture.md"
DEST = sys.argv[1]
WANT = {
    "deploy/systemd/btc-pairbook.service": "ba02fe4175b961c387ea8066eb084704e69efc7fd0a48d8f623a0198334f8dd8",
    "research/tz26-nesting-b3-capture.py": "caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec",
}
with open(SRC, encoding="utf-8") as fh:
    lines = fh.read().split("\n")
found, i = {}, 0
while i < len(lines):
    if lines[i].startswith("```") and " file=" in lines[i]:
        name, j = lines[i].split(" file=", 1)[1].strip(), i + 1
        while lines[j] != "```":
            j += 1
        found[name] = ("\n".join(lines[i + 1:j]) + "\n").encode("utf-8")
        i = j
    i += 1
assert sorted(found) == sorted(WANT), sorted(found)
for name in sorted(found):
    data = found[name]
    assert hashlib.sha256(data).hexdigest() == WANT[name], name
    path = os.path.join(DEST, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "xb") as fh:
        fh.write(data)
    print(path, data.count(b"\n"), len(data), hashlib.sha256(data).hexdigest())
EOF
```

| path | lines | bytes | SHA-256 |
|---|---|---|---|
| `deploy/systemd/btc-pairbook.service` | 22 | 761 | `ba02fe4175b961c387ea8066eb084704e69efc7fd0a48d8f623a0198334f8dd8` |
| `research/tz26-nesting-b3-capture.py` | 2,492 | 118,466 | `caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec` |

A failed assert is BLOCKED. The staged copy runs one mode only, §0.2's `fingerprint`, and is written **`I0`**:
`nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz26-work/stage/research/tz26-nesting-b3-capture.py`.

### 0.2 Fingerprint

`I0 fingerprint` performs contract §1 steps 3 and 4 inside the instrument and asserts them, against `SYSTEM-MAP.md`
and the files of its §0 table in the primary checkout `/root/btc-5m-twap`: revision `2026-10-10-b`; the six anchors;
`A2`, `A4`, `A5` and `A6` re-derived as the first 12 hex characters of those files' SHA-256; the table's **34** rows,
each printed in lines, bytes and SHA-256 — **31** `frozen` rows asserted equal to the map, **2** `tracked` and **1**
`reported`; and the map's own lines, bytes and SHA-256. It prints `FINGERPRINT PASS` or stops at the first mismatch,
which is BLOCKED.

### 0.3 Host gate

From `/root/btc-5m-twap`, with `S` first set to the scratchpad directory the session's system prompt names, output
verbatim into `logs/03-host-gate.log`:

```
date -u; date -u +%s
nproc; grep -E '^(MemTotal|MemAvailable|SwapTotal|SwapFree):' /proc/meminfo
df -B1 --output=source,size,avail /var/lib/btc-recorder
find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
grep -c e3975b5da44c5328adf3bf3914634cd878842c73 /var/lib/btc-recorder/runtime.jsonl
test -d /var/lib/btc-chainbook/1790184600; echo "chainbook exit=$?"
systemctl is-active btc-recorder.service btc-chainbook.service; echo "exit=$?"
systemctl is-enabled btc-recorder.service btc-chainbook.service; echo "exit=$?"
systemctl cat btc-pairbook.service >/dev/null 2>&1; echo "pairbook unit exit=$?"
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
systemctl is-active telemetry-watch.service; echo "exit=$?"
git -C /root/btc-recorder-svc rev-parse HEAD
for d in /root/tz24-work /root/tz18a-svc /root/btc-recorder-svc /root/btc-pairbook-svc /var/lib/btc-pairbook; do test -e "$d"; echo "$d exit=$?"; done
find /root/btc-forensics -type f | wc -l
/root/tz04a-env/venv/bin/python -c 'import sys, websockets; print(sys.version.split()[0], websockets.__version__)'
git worktree list
du -sb /root/.claude /root/PROJECT_GAMING_PS5
echo "$S"; ls -la "$(dirname "$(dirname "$S")")"
```

- **H1** — `find` prints exactly one path.
- **H2** — `df` names source `/dev/vda2` and size `31612203008`; `grep -c` prints at least `1`. With H1 this is map
  §6's host identity.
- **H3** — the interpreter prints `3.12.` and `17.1`, the `websockets` the recorder runs (map §6).
- **H4** — `chainbook exit=0`, and both capture units read `active` and `enabled`, `exit=0` at both reads: the switch
  of §3.7 stops a chain book that runs.
- **H5** — `pairbook unit exit` is not `0`, and `/root/btc-pairbook-svc` and `/var/lib/btc-pairbook` both read
  `exit=1`: nothing of the pair book exists yet.
- **Memory gate** — `MemAvailable` at least `107,503,616` bytes (§0.4).
- **Disk gate** — `avail` at least `5,100,000,000` bytes (§0.4).

Any of these seven failing is BLOCKED. **The rest is printed and carries no threshold:** `telemetry-watch.service`'s
two states, on which map §6's headroom is conditional; the recorder's tree, which map §6 puts at `e3975b5…`;
`/root/tz24-work` absent and `/root/tz18a-svc` and `/root/btc-recorder-svc` present, by map §3; the forensic store's
count, map §3's `1,725`; the worktrees; `du`; and the listing of the directory that holds the session's own, whose
UUID directories `I scratch` names live or earlier (§9).

### 0.4 Resource floors, in exact bytes

**Disk.** `/dev/vda2` free at least **`5,100,000,000`** bytes: the service's stream floor, `STREAM_FLOOR` =
`4,500,000,000` — below it no stream opens and the proof could only read FAIL — plus `500,000,000` for the proof's
streams at their upper bound, five windows each cut at `WINDOW_STREAM_MAX` = `100,000,000` stored bytes, plus
`100,000,000` for this session: the worktree, `5,382,115` bytes of tracked files at `11a0179` before this upload, the
logs under `2,000,000`, the request-path proof's two files about `90,000`, each proof file about `10,000` (§6).

**Memory.** `MemAvailable` at least **`107,503,616`** bytes: twice the largest peak any mode reached in the Architect's
runs under Python 3.12.3 with `websockets` 17.1 — `selftest`, `53,751,808` bytes. The others: `prove` `42,758,144` over
six live windows of the ETH pair and `41,648,128` over five windows each at the cut, 1,270,001 frames a window;
`prestart` `40,038,400`; the service `38,694,912` over two live windows of the ETH pair at 281 and 336 frames a second,
and `33,624,064` storing 1,000 frames a second for 90 s; every systemd read under `36,000,000`. **`prestart` and `prove`
re-read `MemAvailable` at their start and stop BLOCKED below the floor.** The service itself runs under its unit's
`MemoryMax=128M`, `134,217,728` bytes, `3.5` times its larger measured peak. Map §6 records the host: `1,002,127,360`
bytes in all, one processor; TZ-24 read `261,439,488` to `300,302,336` available with its session open. Every mode runs
under `nice -n 19`, the service under systemd at the default priority, as the recorder.

### 0.5 Refs

`git ls-remote origin` before §3.1's push, every ref reported. Map §1 records `main` at
`11a01799ceb43fe050603caf1a19233c59b68a55`, PR #24's merge, `tz-23-maker-m0` at `7f5ae3f`, `tz-24-nesting-b2` at
`6f045cf`, and **30** ref lines. The upload that carries revision `2026-10-10-b` and this TZ sits above `11a0179`, in
one commit or more; every commit on `main`'s first-parent line above it is reported with the paths it changed. A
difference is recorded, not BLOCKING, unless `main` does not carry revision `2026-10-10-b` or
`refs/heads/tz-26-nesting-b3-capture` already exists — either is BLOCKED.

---

## 1. Why this TZ exists

**The question.** CANON PART II, B3: can a violation be captured — depth at the ask, the 150 ms taker delay, both legs
filled together, the strikes known live? B2 measured existence at the chain book's seven instants a window: 7 firm
violations in 7 of 1,079 windows (TZ-24). Seven snapshots cannot see how long an episode lasts, nor the episodes
between checkpoints, nor the book 150 ms after a detection. **B3's measurement needs every change of the four books.**
It is its own TZ, after M0's second look (below, the reserve).

**The protocol, verified by the Architect on 2026-10-10, outside M0's span** — on ETH nested pairs, and by counts
alone on `btc-updown-15m`; no five-minute BTC market was opened (map §5):

- `wss://ws-subscriptions-clob.polymarket.com/ws/market` (map §6), public, no credential. The subscribe frame is
  `{"assets_ids": [...], "type": "market"}`; the text frame `PING` is sent every 10 s and answered `PONG`.
- After the subscribe, one list frame holding a `book` of every subscribed token — 124 ms after it, in the window
  measured, and for markets whose window had not yet opened — then four event types and no other: `book`;
  `price_change`, every frame naming one market and carrying one entry for each of its two tokens; `last_trade_price`;
  and `tick_size_change`. A token subscribed alone receives its market's `price_change` frames, both entries, and only
  its own `book` frames.
- The handshake is answered `101`, with no extension where none is offered, under this file's `User-Agent`.
- The five-minute market's document and `/book` are served before its window opens, the document about a day ahead,
  so at `T+545` both documents carry their token ids.
- In the Architect's windows: the ETH pair streamed `115` to `336` frames a second over whole windows inside
  `[T+595, T+905]`; `btc-updown-15m` alone `140.5`; stored at gzip level 9, `75` to `82` bytes a frame.

**One process, not two** [decision]. The chain book is small — `MemoryCurrent` `7,090,176` and `6,778,880` bytes,
`MemoryPeak` `18,735,104` (TZ-24 report §2.9) — and the pair book's measured peak is `38,694,912`. A third unit beside
the chain book would read every checkpoint's books twice over REST, on a host with one processor and 261 to 300 MB
available. **So the pair book replaces the chain book**: it keeps the chain book's seven checkpoints, five seconds
before each Tier C read of the same five-minute market, in the chain book's exact line format, and adds the stream.
Discarded: a third unit. The chain book's unit file and `/root/tz18a-svc/` stay, disabled — the fallback
B-RESTORE-CB starts on a FAIL (§4.7); TZ-22 reclaims both once the pair book has run for days.

**The window.** For each `T` ≡ 0 (mod 900), `btc-updown-15m-{T}` and `btc-updown-5m-{T+600}`:

| instant | what |
|---|---|
| `T+545` | the two documents, through `http_get`, each retried every 5 s until it carries two token ids, to `T+880`; every reply stored verbatim in `documents.jsonl` |
| `T+595` to `T+905` | the stream: one connection for the four tokens; every frame one line; `PING` every 10 s; after a drop, a reconnect 1, 2, 4 and 8 s later |
| `T+655` … `T+885` | the chain book's seven checkpoints, four `/book` reads released together, `books.jsonl.gz` |
| `T+910` | `window.json`: counts, times, token ids, the stream's counts |

The recorder's own requests fall in other seconds: S6 at `T+605`; Tier C at `T+360` … `T+590`, of the five-minute market
before, and at `T+660` … `T+890`, of this one, each 5 s after a checkpoint. The stream opens after Tier C's last read of
the interval before. A process starting inside a window joins it until `T+880` — the documents at once, the stream from
then, the checkpoints still ahead — unless an earlier process wrote the window's books or its `window.json`; after
`T+880` it waits for the next window.

**The stream file.** `stream.jsonl.gz`, gzip level 9, one member, a sync flush at least every 10 s of frames, so a
process killed inside a window leaves a file readable to its last flush. One JSON line per frame — `recv_ns`,
`mono_ns` and `raw`, the recorder's own line format (TZ-04a §4), or `raw_b64` for a binary frame — and one per session
event: `connect`, `open` with the handshake's status and extensions, `subscribe` with the frame sent, `ping`, `close`
with its reason and code, and a last `end` line with the counts. A second process in a window writes
`stream.1.jsonl.gz`.

**Bounds, in exact bytes.** No stream opens for a window below **`4,500,000,000`** bytes free (`STREAM_FLOOR`), or once
the stream files under the root reach **`8,000,000,000`** (`STREAM_CAP`); a window's stream is cut at **`100,000,000`**
stored bytes; the service halts, exit `1`, below `2,200,000,000` free — the chain book's own `RESOURCE_FLOOR`
(`research/tz18a-chainbook-capture.py` line 79) — or past `200,000,000` bytes written by one process outside its stream
files, the chain book's own cap (line 80). The REST checkpoints and the documents go on below the stream floor and past
the stream cap. **At the BTC pair's rate the cap is reached in about three days** [modelled]: `btc-updown-15m` streamed
`140.5` frames a second, and if `btc-updown-5m` carries the 179 price changes a trade `btc-updown-15m` carried, at the
`4.98` taker fills a second TZ-23 counted inside `[T0, T0 + 240)` — `4,820,537` over 4,032 markets — the pair streams
about `1,032` frames a second: `26.2` MB a window, `2.52` GB a day, `3.2` days to the cap. The proof measures the rate
(§4.2); B3's measurement reads what the cap holds. The floor leaves `2,500,000,000` bytes above the recorder's own floor,
`2,000,000,000`: 13 days at map §6's fastest measured drain.

**The reserve.** Everything under `/var/lib/btc-pairbook/` is **reserved from its first byte**, on Tier C's terms (map
§2.5): until B3's measurement — its own TZ, which reads nothing before M0's second look has reported, because the
five-minute legs are M0's next markets (CANON PART II) — no TZ extracts a price, size, side, book hash or outcome from a
stored body, and no report prints one. A deployment proof reads a stored line's status, byte count, SHA-256 and times;
whether a body parses; and of a stream frame its JSON shape, its event types, its token ids and the venue's timestamp.
`window.json`, `runtime.jsonl` and `service.log` carry counts, times and token ids and are excepted. Nothing of it
enters git history.

**What this TZ decides.**

1. **The instrument and the unit**, on the branch `tz-26-nesting-b3-capture`; `main` carries them once the Boss merges
   after the verdict.
2. **The service's copy** at `/root/btc-pairbook-svc/`, byte for byte the branch's file, which the unit runs.
3. **The switch:** the chain book stopped and disabled through systemd, the pair book enabled and started.
4. **The readings** — P-START, G-CB-STOP, G-UNIT, G-START, G-STREAM, G-BOOKS, G-TIERC, G-LOAD, G-RESTART and G-STILL.
   Under PASS the pair book keeps running after the session; on a FAIL of any of them after the switch, K-26 stops it
   and B-RESTORE-CB starts the chain book again (§4.7).
5. **Nothing else on the host is touched** but the paths of §2.

---

## 2. Scope

**Repository paths this TZ may write, and no others:**

1. `research/tz26-nesting-b3-capture.py` and `deploy/systemd/btc-pairbook.service` — new, byte for byte Appendix A's,
   on branch `tz-26-nesting-b3-capture`, then a pull request. Not merged by the Executor.
2. `CryptoReports/TZ-26-nesting-b3-capture-report.md` — straight to `main`, in one commit. **The one path pushed to
   `main`, and the exemption to item 7 below.**

**Host paths this TZ may write:** `/root/tz26-work/**`; `/root/btc-pairbook-svc/`, the service's copy and its
`commit.txt`; `/etc/systemd/system/btc-pairbook.service`, byte-identical to the branch's unit, with the link `systemctl
enable` makes; `/var/lib/btc-pairbook/`, created empty by B-INSTALL and from then written by the unit alone;
`/root/btc-forensics/`, by exclusive create only (§9); and in the primary checkout `/root/btc-5m-twap`, its `.git` for
the branch and the worktree, and its `CryptoReports/` for the report. **The chain book's unit is disabled** by B-SWITCH,
which removes its enable link. **Host paths it removes, under §9 and B-UNINSTALL and nothing else:** `/root/tz26-work/`
with its worktree; the directories `I scratch` names earlier; and, on a BLOCK after §3.4 and before B-SWITCH, the
service's copy, the unit file and the empty root.

**Prohibited, each absolutely:**

1. No committed file is modified; every `frozen` row of map §0 is byte-identical at run end.
2. **Under `/var/lib/btc-recorder/` nothing is opened but a `manifest.json`, read only — by `prestart`, the week of its
   base rate, and by `prove`, the exposed and control intervals of its proof — and nothing is listed.** A manifest
   carries the capture's own accounting and no price, size, fill or outcome (map §2.3's exception). The instrument's
   audit hook refuses every other open there. Outside it only §0.3's `df`, `find` and `grep -c`, at both of its runs,
   and B-RECLAIM-OWN's `df` touch the root.
3. **Under `/var/lib/btc-chainbook/` nothing is written or listed, and nothing opened but `runtime.jsonl`, read only,
   by `chainbook` and `restored`;** outside the instrument only §0.3's `test -d`, at both of its runs. The stored
   windows — B2's and the later ones — are not touched. **Exempt:** what the chain book's own process writes there
   when systemd stops it at B-SWITCH — its `stop` record and its last log lines — and, on a FAIL, when B-RESTORE-CB
   starts it again; those writes are the unit's, as they were at TZ-20's restarts.
4. **Under `/var/lib/btc-pairbook/` nothing is written but by the unit, and nothing read but by the modes `prove`,
   `load`, `unit`, `restart`, `final` and `restored`**, and outside the instrument by §3.11's `tail` of `service.log` and
   `du`; no price, size, side, book hash or outcome is extracted from a stored body (§1, the reserve). The audit hook
   refuses every other open there and every listing outside `serve` and `prove`.
5. **No unit is created, started, stopped, enabled, disabled, signalled or changed but by B-INSTALL, B-SWITCH,
   B-KILL-SVC and, on a FAIL, K-26 and B-RESTORE-CB, or on a BLOCK B-UNINSTALL.** `systemctl show`, `is-active`,
   `is-enabled`, `cat` and `journalctl -u` are this TZ's only other reads of a unit. The recorder is never signalled.
6. `/root/tz04a-env/`, `/root/tz01-env/`, `/root/tz18a-svc/` and `/root/btc-recorder-svc/` are not modified, and
   `/root/btc-forensics/` only by §9's exclusive create.
7. Nothing is pushed to `main` except the report of item 2.
8. **Requests:** `prestart`'s two ETH documents and one ETH book through `http_get`, and its one 25 s stream session on
   the ETH pair through `stream_window`; the unit's own; `git` against `origin`; and `gh` for the pull request. No other
   request — no authenticated call, no BTC market outside the unit — and no command but the instrument's modes opens a
   stored body.
9. **No price, size, side, book hash or outcome of any market is printed or written** outside the capture's own store
   and §9's byte-for-byte copies, with one exemption: `prestart`'s 25 s session on the ETH pair, stored verbatim in
   `stream.jsonl.gz` under `/root/tz26-work/prestart/` or `prestart-2/` and read by the instrument for its shapes,
   counts and times alone — ETH markets, outside every span a gate reserves. The instrument prints counts, times,
   statuses, token ids and SHA-256 of files.
10. No Release is created, and no dataset, archive or binary enters git history.

---

## 3. The work, in this order

From §3.1 on, `nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz26-work/wt/research/tz26-nesting-b3-capture.py`
is written **`I`**; a mode is `I <mode>`, run from `/root/tz26-work`. Every command's output goes to `logs/`, one file
per step, and is quoted in the report. **§9's B-RECLAIM-SCRATCH runs after §3.3 and before §3.4; B-RECLAIM-OWN runs
last, after §3.11.** On a BLOCK before §3.1, B-RECLAIM-OWN runs with `I0` in place of `I` and without its `git worktree
remove` line; on a BLOCK after §3.4 and before B-SWITCH, B-UNINSTALL runs first (§4.7).

**Where the session's permission classifier refuses a command of a block named B-… or K-…**, the Executor prints the
block, the Boss runs it verbatim in a root shell on the VPS, and the Executor verifies it through the reads this TZ
names — never from the Boss's account. **Every `mark` is the Executor's**, taken before its block is run or handed
over. TZ-20 found `systemctl enable --now` refused as "Unauthorized Persistence" (map §6).

### 3.1 The branch and its two files

```
git -C /root/btc-5m-twap fetch origin
git -C /root/btc-5m-twap worktree add -b tz-26-nesting-b3-capture /root/tz26-work/wt origin/main
```

Then §0.1's script again, verbatim but for its argument, `/root/tz26-work/wt`; it must print the same lines, bytes and
SHA-256 as at §0.1. Commit those two files alone on the branch, push it with `git push -u origin
tz-26-nesting-b3-capture`, and open the pull request against `main`. A failed assert here is BLOCKED.

### 3.2 The self-test

`I selftest` must print `74 of 74 checks passed`. It reaches `127.0.0.1` alone. A red self-test stops the run here,
and it goes to §3.11 and §9.

### 3.3 The units, and the directories beside this session

`I still` records the recorder's `MainPID`, `NRestarts` and `ActiveState` in `state.json` and prints all three capture
units' state and memory — a unit `systemctl show` cannot read is printed as unread, and only the recorder's is
required. Then `I scratch "$(dirname "$S")"` lists every UUID directory beside this session's own and
names each **live** — born from 1 s before to 60 s after the start of a running process whose `argv[0]` is `claude` or
ends in `/claude.exe` — or **earlier**.

### 3.4 The service's copy

```
mkdir /root/btc-pairbook-svc; echo "exit=$?"
git -C /root/tz26-work/wt show origin/tz-26-nesting-b3-capture:research/tz26-nesting-b3-capture.py > /root/btc-pairbook-svc/tz26-nesting-b3-capture.py
git -C /root/tz26-work/wt rev-parse origin/tz-26-nesting-b3-capture > /root/btc-pairbook-svc/commit.txt
sha256sum /root/btc-pairbook-svc/tz26-nesting-b3-capture.py /root/tz26-work/wt/research/tz26-nesting-b3-capture.py
cat /root/btc-pairbook-svc/commit.txt; git -C /root/tz26-work/wt rev-parse HEAD
```

`mkdir` exits `0`; both hashes equal Appendix A's; `commit.txt` is the branch head's 40 hex characters and a newline,
equal to the worktree's `HEAD`. Anything else is BLOCKED.

### 3.5 The request path — P-START

From `/root/tz26-work`, the copy itself:

```
nice -n 19 /root/tz04a-env/venv/bin/python -B /root/btc-pairbook-svc/tz26-nesting-b3-capture.py prestart
```

It must print `READING P-START: served` (§4.1). **A failed assert is BLOCKED, and nothing is installed or started.**

### 3.6 Install — B-INSTALL

```
install -m 0644 /root/tz26-work/wt/deploy/systemd/btc-pairbook.service /etc/systemd/system/btc-pairbook.service; echo "exit=$?"
cmp /root/tz26-work/wt/deploy/systemd/btc-pairbook.service /etc/systemd/system/btc-pairbook.service; echo "exit=$?"
install -d -m 0755 /var/lib/btc-pairbook; echo "exit=$?"
systemctl daemon-reload; echo "exit=$?"
systemd-analyze verify /etc/systemd/system/btc-pairbook.service; echo "exit=$?"
```

Both `install`, `cmp` and `daemon-reload` must exit `0`, or BLOCKED and nothing is started. `systemd-analyze verify` is
recorded: its findings may name other units on this host, and G-UNIT decides. **The root is created here, before the
first start**, because systemd opens the unit's `append:` log under it before the process runs.

### 3.7 The switch — B-SWITCH

At the first instant at which `$(( $(date +%s) % 900 ))` lies between `15` and `420`, and within `3,600` s of
P-START's exit — the chain book between its `window.json` at `T+905` and its next documents at `T+1525`, and the pair
book's first window ahead, its documents at `T+545` more than 60 s away — after `I mark stop-cb` and then `I mark
start-svc`:

```
systemctl disable --now btc-chainbook.service; echo "exit=$?"
systemctl enable --now btc-pairbook.service; echo "exit=$?"
```

If `3,600` s pass after P-START's exit before the block runs, §3.5 runs again once, into `prestart-2`, first. At least
30 s after the block: `I chainbook` — **G-CB-STOP**. At least 60 s after it: `I unit 0` — **G-UNIT** and **G-START**.
The block's first line is TZ-20's K-20C, the chain book's stop.

### 3.8 The proof — G-STREAM, G-BOOKS, G-TIERC, then G-LOAD

`I prove A` with `A` = `$(date +%s)` at that run: first at or after `T1 + 4,020`, where `T1` is the first window whose
`T + 545` lies at or after the service's start plus 60 s; then every 300 s while it prints `NOT YET` and exits `3`.
`T1 + 3,610` is the fourth qualifying window's `window.json`; its exposed interval closes at `T1 + 3,600`, and the
recorder writes that interval's manifest once the venue's resolution has come, a median of 318 s after a close (map
§2.3). The run that decides prints the three readings and writes `proof/proof-A.json`; then `I prove A` again with
the same `A`, which must print `unchanged` — contract §6's determinism. Then `I load` — **G-LOAD**.

### 3.9 The restart — G-RESTART

Only after every reading of §3.7 and §3.8 is PASS. At the first instant at which `$(( $(date +%s) % 900 ))` lies
between `15` and `480` — the pair book between its `window.json` at `T+910` and its next documents at `T+1445` — after
`I mark kill-svc`, **B-KILL-SVC**:

```
systemctl kill --signal=SIGTERM btc-pairbook.service; echo "exit=$?"
```

At least 30 s later: `I restart` — **G-RESTART**.

### 3.10 Final — G-UNIT at one restart, and G-STILL

`I final`.

### 3.11 The closing reads

§0.3's block again — H4 and H5 now read the switch, and are printed — then:

```
systemctl show btc-recorder.service btc-chainbook.service btc-pairbook.service -p MainPID -p NRestarts -p ActiveState -p MemoryCurrent -p MemoryPeak
systemctl is-enabled btc-pairbook.service btc-chainbook.service; echo "exit=$?"
journalctl -u btc-pairbook.service -u btc-chainbook.service --since "@$(( $(/root/tz04a-env/venv/bin/python -c 'import json; print(json.load(open("/root/tz26-work/state.json"))["marks"]["stop-cb"]["ns"] // 10**9)') - 5 ))" --no-pager -o short-iso
tail -n 40 /var/lib/btc-pairbook/service.log
free -b
du -sb /root/tz26-work /root/btc-pairbook-svc /var/lib/btc-pairbook /root/.claude
cat /root/tz26-work/state.json
```

The journal holds systemd's own lines for both units; `service.log` holds the service's start and stop lines and two
lines a window, its opening and its close, counts and times only.

---

## 4. The gates — fixed here, before any of their data exists

| gate | population | PASS | false failure | power, against |
|---|---|---|---|---|
| **P-START** | the ETH pair: 3 requests, 1 session | §4.1 | `0` — the venue read directly | `1`, a refused request or a format not the verified one |
| **G-CB-STOP** | the chain book, after B-SWITCH | §4.1 | `0` — systemd, `/proc` and its record | `1`, a chain book still running or stopped outside systemd |
| **G-UNIT**, **G-START** | the pair book at `0` and `1` restarts; its start record | §4.1 | `0` | `1`, a process outside its unit, under another argv, beside a second instance, or not the branch's file |
| **G-STREAM** | the first `4` qualifying windows | at least `3` of `4` complete (§4.2) | `0.00059203` if 1 window in 100 fails independently | `0.26171875` at 1 in 4, `0.6875` at 1 in 2 |
| **G-BOOKS** | their `28` checkpoints | at least `26` of `28` complete (§4.3) | `0.0027171219` at 1 checkpoint in 100 | `0.9833852515` at 1 in 4, `0.5406170777` at 1 in 10 |
| **G-TIERC** | their `4` exposed intervals | §4.4 | `1 − (1 − f/m)^4`, printed by `prestart` | `0.68359375` against a disturbance breaking 1 in 4, `0.9375` at 1 in 2 |
| **G-LOAD** | the pair book's process, from its start to `load` | its processor time at most a quarter of the wall time | `0` — `/proc` read directly | `1`, a process above it |
| **G-RESTART** | its records after the kill mark | §4.6 | `0` | `1`, a `SIGTERM` not restarted |
| **G-STILL** | the recorder's unit, §3.3 to §3.10 | `MainPID`, `NRestarts` and `ActiveState` unchanged | `0` | `1`, a restart or a stop |

**Family-wise false failure at most `0.0033091519` plus G-TIERC's printed figure**, the sum of G-STREAM's and
G-BOOKS'. The 1-in-100 rates are stated, not measured for the pair book: the chain book's own record — 5 incomplete
windows besides its stop among the 1,085 B2 found stored (TZ-24 report §2.6), 0.46% of windows — lies below them. **A
deployment proof does not see a low loss rate**; B3's measurement re-reads completeness over its whole set first.

### 4.1 P-START, G-CB-STOP, G-UNIT and G-START

**P-START** — CANON hard rule 14's proof, on the ETH nested pair of the current window, through the service's own
functions: the two documents through `http_get`, `200`, non-empty, two token ids each; the fifteen-minute market's
first token's `/book` through `http_get`, `200`, JSON; exactly `3` requests; then one session of 25 s through
`stream_window`, which must hold `1` session, the handshake answered `101` with no extension, the subscription sent, a
`book` of each of the four tokens within 5 s of it, at least `1` `PONG` and `2` `PING`, every frame conforming to §1's
four event types and the four tokens, and the file whole with its `end` line. Every header fixed: HTTP `Accept:
application/json` and `User-Agent: btc-5m-twap-tz26`, beside `urllib`'s own `Accept-Encoding: identity`, `Host` and
`Connection: close`; the websocket handshake `Host`, `Upgrade`, `Connection`, `Sec-WebSocket-Key`,
`Sec-WebSocket-Version` and `User-Agent: btc-5m-twap-tz26`, and no `Sec-WebSocket-Extensions` — the self-test asserts
both blocks on loopback listeners. It also asserts that no process runs under the service's argv, and prints the chain
book's, and G-TIERC's base rate: of the 2,016 five-minute slots closing in the week before it, the manifests read, `m`,
and those whose `quotes_complete` is not `true`, `f`, with `1 − (1 − f/m)^4` exactly and to ten decimals.

**G-CB-STOP** — `is-active` reads `inactive` or `failed`, `is-enabled` reads `disabled`, no process runs under the chain
book's exact argv, and its `runtime.jsonl` ends with a `stop` of the `MainPID` the `stop-cb` mark read, at or after the
mark. Printed beside it: how many seconds into its window the stop fell, and whether inside its idle stretch.

**G-UNIT**, at `N` restarts: `ActiveState` `active` and `SubState` `running`, `UnitFileState` `enabled`, `FragmentPath`
`/etc/systemd/system/btc-pairbook.service`, `ControlGroup` `/system.slice/btc-pairbook.service`, `MemoryMax`
`134217728`, `NRestarts` `N`; `/proc/<MainPID>/cmdline` equal field for field to `/root/tz04a-env/venv/bin/python -B -u
/root/btc-pairbook-svc/tz26-nesting-b3-capture.py serve`; its `cwd` `/root/btc-pairbook-svc`; its `cgroup` naming
`/system.slice/btc-pairbook.service` and no path under `/user.slice`; and the `MainPID` the only process under that
argv. **G-START**, with `unit 0`: exactly one `start` record in `/var/lib/btc-pairbook/runtime.jsonl`, at or after the
`start-svc` mark, its `pid` the `MainPID`, its `commit` `commit.txt`'s, its `file_sha256` the copy's, its `argv` the
file and `serve`, and its `config.headers` the two of P-START.

### 4.2 G-STREAM

**The unit is a window.** `s` is the first `start` record's instant. A window is **considered** where `T + 880 >= s` and
`T + 910 <= A`, and **qualifies** where also `T + 545 >= s + 60` and `T + 910 <= s + 6,000`; the first four that
qualify are G-STREAM's. A qualifying window's stream is **complete** when every one of these holds, and each that
fails is printed by name:

- its `window.json` reads both documents served, the window not joined late and not stopped, and the stream opened;
- every stream file `window.json` lists exists, is whole — its gzip trailer present, nothing after it — and ends with
  its `end` line, and every line parses as one of §1's two shapes;
- every frame is `PONG` or JSON of §1's four event types, naming only the window's four tokens;
- the first `subscribe` at or before `T+600`; a `book` of each of the four tokens within 5 s of it;
- no two consecutive instants among the first `subscribe`, every later frame and every `close` more than 15 s apart —
  the `PING` period plus 5 s;
- the last `close` at or after `T+900`;
- the frames counted equal to `window.json`'s.

**NOT YET:** before `s + 6,000`, `prove` reads no stream and exits `3` while fewer than four qualifying windows have
closed or an exposed manifest of one of them is not yet counted (§4.4); at or after it, it decides on what exists, and
a reading short of its count is UNDECIDABLE. **Printed per window, barred from every reading:** its frames by market,
bytes by market, stored bytes, its sessions' subscribes and closes, the largest gap, the subscribe offset, the last
close, and the venue-to-host lag of the `price_change` frames in milliseconds — the receive instant less the frame's
own `timestamp`, counted between −1,000 and 60,000 — as minimum, median, 99th percentile and maximum.

### 4.3 G-BOOKS

The chain book's rule, unchanged (`research/tz18a-chainbook-capture.py` lines 296 to 314): a checkpoint is complete
when its four stored replies are `200`, non-empty, JSON, and received within one second of one another. Over the 28
checkpoints of G-STREAM's four windows, at least 26 complete is PASS, fewer is FAIL; a window without `books.jsonl.gz`
counts its seven as incomplete.

### 4.4 G-TIERC

**Exposed interval:** `E = T + 600` of each of G-STREAM's four windows — the five-minute market the stream and the
checkpoints load, whose Tier C reads at `E+60` … `E+290` fall inside the stream. **Fully loaded** when that window's
stream subscribed by `T+600` and ran to `T+900` and each of its seven checkpoints received a status for all four reads.
**Counted** when `E`'s `manifest.json` exists with `st_mtime_ns <= A · 10^9`. **FAIL:** any counted exposed interval
whose `quotes_complete` is not `true`. **PASS:** no FAIL, and at least two counted fully loaded exposed intervals.
**UNDECIDABLE:** otherwise. Printed beside it, not gated: each exposed interval's `complete`, and Tier C's read offsets
— minimum, median, 99th percentile, maximum — for the exposed intervals and for the control intervals, `T0` ≡ 0 or 300
(mod 900) inside `(s, s + 6,000]` with `T0 + 330 <= A`, which the stream never loads.

### 4.5 G-LOAD

`load` reads `/proc/<MainPID>/stat`: the process's user and system time since it started, over the wall time since,
**at most `1/4`** of one core — the host has one processor (map §6). At the measured `148` to `226` µs a frame and the
modelled `1,032` frames a second, the stream takes 15% to 23% of the core while it runs and 5% to 8% over a window
[modelled]. Printed beside it: the unit's `memory.current`, `memory.peak`, swap and `memory.stat`'s `anon`, `file`,
`kernel` and `sock`, and the process's `VmRSS`, `VmHWM`, `VmSwap` and threads, for TZ-22.

### 4.6 G-RESTART and G-STILL

**G-RESTART:** after the `kill-svc` mark, the service's records are exactly a `stop` of the marked `MainPID` and a
`start` of another, at most 60 s later, with the first `start`'s `commit` and `file_sha256`; and G-UNIT holds at `1`
restart. **G-STILL:** from §3.3 to §3.10 the recorder's unit keeps its `MainPID`, `NRestarts` and `ActiveState`.

### 4.7 The stops — CANON hard rule 14

**On a FAIL of G-CB-STOP, G-UNIT, G-START, G-STREAM, G-BOOKS, G-TIERC, G-LOAD, G-RESTART or G-STILL, after B-SWITCH,
the pair book's stop is authorized and run at once, and the chain book started again**, by the classifier route of §3
where refused — after `I mark restore`, one block:

**K-26 and B-RESTORE-CB:**

```
systemctl disable --now btc-pairbook.service; echo "exit=$?"
systemctl enable --now btc-chainbook.service; echo "exit=$?"
```

**Verification is the Executor's**, at least 30 s after the block: `I restored` must print `RESTORED PASS` — the pair
book `inactive` or `failed` and `disabled`, no process under its argv, its record ending with a `stop`; the chain book
`active` and `enabled`, one process under its exact argv, its record ending with a `start` of that pid after the mark.
The run then goes to §3.11 and §9, skipping every step that needs a PASS it lacks. **Under PASS neither block is run.**
A recorder that G-STILL finds restarted stops the pair book too: the capture that matters most is the recorder's.

**B-UNINSTALL**, on a BLOCK after §3.4 and before B-SWITCH, so that nothing of the pair book stays:

```
rm -f /etc/systemd/system/btc-pairbook.service; echo "exit=$?"
systemctl daemon-reload; echo "exit=$?"
rmdir /var/lib/btc-pairbook; echo "exit=$?"
rm -rf /root/btc-pairbook-svc; echo "exit=$?"
test -e /etc/systemd/system/btc-pairbook.service; echo "exit=$?"; test -e /var/lib/btc-pairbook; echo "exit=$?"; test -e /root/btc-pairbook-svc; echo "exit=$?"
```

The three `test -e` read `exit=1`. A `rmdir` of a root that does not exist yet is recorded and harmless.

### 4.8 What a PASS establishes, and what it does not

The pair book runs as a system unit outside every session, streams the four books of each window without a gap above
15 s, stores the chain book's checkpoints, holds its processor load under a quarter of the host's one core, leaves Tier
C intact at four exposed intervals, and is restarted by systemd after a stray `SIGTERM`. **Not established:** anything
of a price, a book or a violation — B3's measurement's, after M0's second look; that a book rebuilt from the stream
equals the checkpoint read at the same instant — B3's measurement checks it first; and completeness over days, which
TZ-22 and B3's measurement re-read. A logout and a reboot are not exercised: the unit's control group and
`WantedBy=multi-user.target` carry them, as TZ-20's units.

---

## 5. The instrument and the unit

`research/tz26-nesting-b3-capture.py`, Appendix A, fixed by the Architect as this TZ's Validation and written byte for
byte; and `deploy/systemd/btc-pairbook.service`, the chain book's unit with 8 of its 22 lines changed — the two comment
lines, the description, the working directory, the command line, the two log lines, and the ceiling `MemoryMax=128M`
in place of `192M` — and the rest equal:
`Restart=always`, `RestartSec=5`, `RestartPreventExitStatus=1 2 3`, `StartLimitIntervalSec=3600`,
`StartLimitBurst=5`, `WantedBy=multi-user.target`. **The service's exits:** `0` after a `SIGTERM`, which systemd
restarts unless it ordered the stop itself; `1` at a floor, the write cap or a refused open, which it does not
restart; `2` under another command line; `3` beside another instance. An error inside a window — an exception, an
assert on a stored format — is written as an `error` record, and the next window runs. Its stop is K-26,
`systemctl disable --now`.

The instrument is the standard library and `websockets` 17.1, run under `/root/tz04a-env`, the recorder's interpreter,
which nothing in this TZ modifies; it imports nothing from the repository. One mode a run; each but `serve` prints its
findings with UTC stamps, its peak memory, the opens its audit hook refused, and its manifest and chain book opens, its
requests and its stream sessions. **The audit hook enforces §2:** under the three roots it refuses every open and
listing a mode is not given, before it happens; outside them every write but under `/root/tz26-work/` and `reclaim`'s
exclusive creates in the forensic store; and under `serve` every write outside the pair book's root and every
process. **After the first frame of a window nothing the stream can carry raises:** an unparseable line, a frame of
another shape, a torn file is a counted reason in G-STREAM's unit. Exit `0` is every assert held; exit `1` a
failed assert, named, or a BLOCK whose message says so; `3` NOT YET. Run with `-O` it refuses to start.

---

## 6. Cost

Measured in the Architect's runs under Python 3.12.3 with `websockets` 17.1 on one core of an Intel Xeon at 2.10 GHz,
and taken at the population's upper bound.

| check | population | measured | bound |
|---|---|---|---|
| `selftest` | 74 checks, two loopback servers | `3` s | `60` s |
| `prestart` | 2,016 manifests; 3 requests; one 25 s session | `26` s, the base rate empty in the Architect's run | `660` s: the scan's fail-fast, `0.3` s an open after its first 100, 2,016 × `0.3` = `605` s, plus 25 s and three requests at their 5 s timeout |
| `prove`, a deciding run | at most 7 considered windows — `T` from `s − 880` to `s + 5,390`, the deciding run at most 300 s past `s + 6,000` — each cut at 100,000,000 stored bytes, 1,270,001 frames | `63.3` to `87.3` s for 5 such windows, at most `17.5` s a window; `4.7` s for six live ETH windows | `122` s for seven; two deciding runs `244` s |
| `prove`, NOT YET | the window list and four manifests | `0.2` s | `5` s a run; at most 9 runs, from `T1 + 4,020 >= s + 3,535` to `s + 6,000` every 300 s, `45` s |
| `fingerprint`, `still`, `mark`, `chainbook`, `unit`, `load`, `restart`, `final`, `restored`, `scratch`, each `reclaim` | — | under 1 s each | `30` s a run |
| **the service** | one window: 2 documents, 28 book reads, a 310 s stream | `148` to `226` µs of processor a frame on the live ETH pair, with its REST reads; `171` µs storing 1,000 frames a second on loopback | G-LOAD, a quarter of the core |

**Single-session processor at most `2,089` s at those bounds** — `selftest` `60`, `prestart` twice `1,320`, two
deciding `prove` runs `244`, nine NOT YET `45`, fourteen runs of the other modes `420` — **under `3,600`, so nothing is
sampled.** **Wall clock at most about `6,500` s:** §0 to §3.6 about 10 minutes; B-SWITCH waits at most `495` s for its
band of 405 s in 900; the proof decides by `T1 + 4,020` to `T1 + 4,320`, and `T1`, the switch's own window, opens 15 to
420 s before it; B-KILL-SVC waits at most `435` s for its band of 465 s; the rest about 10 minutes. The
fail-fast bound of `prestart`'s scan, 30 s for its first 100 manifests, is TZ-18a's (its §10 C4). **The
host pays, after the session:** about `26.2` MB of stream and `23,000` bytes of the rest a window at the modelled rate,
until the cap; 30 REST requests a window, as the chain book; one websocket of about 670,000 bytes a second inbound for
310 s of every 900.

---

## 7. Validation

| # | check | count |
|---|---|---|
| **V1** | §0.2's fingerprint | `FINGERPRINT PASS`: revision `2026-10-10-b`; anchors 6 of 6, 4 re-derived; 34 rows, 31 of 31 `frozen` equal |
| **V2** | §0.3's host gate | H1 to H5, the memory and the disk gate; the rest printed |
| **V3** | §0.1's and §3.1's files | 2 of 2 hashes asserted at each, lines and bytes; the branch's diff against `origin/main` names exactly these two paths, both `A` |
| **V4** | the self-test | `74 of 74` |
| **V5** | §3.4's copy | 2 of 2 hashes equal to Appendix A's; `commit.txt` equal to the branch head |
| **V6** | P-START | `READING P-START: served`; 3 requests, 1 session; the seven session checks; `m`, `f` and the false alarm |
| **V7** | B-INSTALL | `cmp` exit `0`; `daemon-reload` exit `0`; `verify` recorded |
| **V8** | G-CB-STOP | the four checks; the stop's instant and its phase |
| **V9** | G-UNIT and G-START at `unit 0`; G-UNIT at `unit 1` | 10 checks at 0 restarts and 7 more for G-START; 10 at 1 restart |
| **V10** | G-STREAM, G-BOOKS, G-TIERC | each reading with its count; every considered window disclosed with its reasons, its checkpoints and its counts; every exposed and control interval |
| **V11** | determinism | the proof file `unchanged` at the second run with the same `A`; its SHA-256 |
| **V12** | G-LOAD | the fraction, against `0.25`; the memory reads |
| **V13** | G-RESTART | the two records, the pids, the gap |
| **V14** | G-STILL | the recorder unchanged, or the change named |
| **V15** | opens under the capture roots | refused `0` at every mode; manifest opens `2,016` attempted by `prestart`, at most `4` by each NOT YET `prove` and at most `25` by each deciding one — `4`, one for each of at most `7` considered windows, and at most `14` control intervals; chain book opens `1` by `chainbook` and by `restored`, `0` elsewhere |
| **V16** | contract §4.2's self-check | run after the push and the pull request and before the report's commit |
| **V17** | §3.11's closing reads | every read printed |
| **V18** | §9's `reclaim` runs | files considered, named by a report, kept by name, copied and already held; the store's count after equal to before plus the copies |
| **V19** | §9's removals | `git worktree remove` without `--force` exit `0`; `test -e` exit `1` for `/root/tz26-work` and each directory removed; `git worktree list` naming `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else |

---

## 8. The report

`CryptoReports/TZ-26-nesting-b3-capture-report.md`, in contract §8's order. **In its first ten lines:** P-START; the
switch and G-CB-STOP; G-STREAM, G-BOOKS, G-TIERC and G-LOAD with their counts; G-RESTART and G-STILL; whether the pair
book runs, and how that was verified. Beyond what V1 to V19 print: every mark's instant; every block the classifier
refused, who ran it and when; the units' journal lines; **the BTC pair's measured rate** — frames a second by market and
stored bytes a window over G-STREAM's four windows — and the days to `STREAM_CAP` at that rate; each unit's memory at
every read; every free-space and `MemAvailable` read with its instant and bound; the commit and the pull request; §9's
counts and removals; and every file the run wrote, by SHA-256, but the capture's own. **The report is drafted in the
primary checkout `/root/btc-5m-twap` before B-RECLAIM-OWN and committed after it**, so the removal of this TZ's tree is
in it.

---

## 9. Reclaim — the host left clean (CANON hard rule 15)

**What a file is kept for:** a committed report prints its SHA-256, whole or as a prefix of 16 to 64 hex characters, or
it is kept by name: `state.json`, every file under `logs/`, `prestart/` and `prestart-2/`, and `proof/`. `reclaim`
copies each into `/root/btc-forensics/` as `<tree>--<path with / as -->`, by exclusive create, and verifies its hash; a
name already there with the same hash is counted as held, and with another hash is a failed assert. The branch worktree
is not copied: `reclaim` asserts that `git status --porcelain --ignored` in it prints nothing and that its `HEAD` is its
upstream's, so `git worktree remove` needs no `--force`.

**B-RECLAIM-SCRATCH**, after §3.3 and before §3.4, for every directory `I scratch` named **earlier** — none it named
live, and never this session's own; map §3 names TZ-24's pair, `5c15abf7…` and `65948b60…`:

```
I reclaim <each earlier directory, by its full path>
rm -rf <one such directory>; echo "exit=$?"
test -e <that directory>; echo "exit=$?"
```

One `I reclaim` names every earlier directory; then one `rm -rf` and one `test -e` a directory. `reclaim` refuses a
directory born from 1 s before to 60 s after a running claude process started, and any path but `/root/tz26-work` that
is not a UUID directory under `/tmp/` whose parent's name carries `btc-5m-twap`; it prints `RECLAIM PASS` before any
removal. If `I scratch` names none earlier, the block is recorded as empty and skipped.

**B-RECLAIM-OWN**, last, after §3.11 and with the report drafted. **Its output is written to no file; the report
quotes it verbatim from the session**, the checks after the removal included:

```
I reclaim /root/tz26-work
git -C /root/btc-5m-twap worktree remove /root/tz26-work/wt; echo "exit=$?"
rm -rf /root/tz26-work; echo "exit=$?"
test -e /root/tz26-work; echo "exit=$?"
git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
find /root/btc-forensics -type f | wc -l
df -B1 --output=source,size,avail /var/lib/btc-recorder
```

The branch `tz-26-nesting-b3-capture` stays on `origin` and as a local ref; only its working tree goes. **Kept:**
`/root/btc-pairbook-svc/` and `/root/btc-recorder-svc/` are the running units' code, `/root/tz18a-svc/` the disabled
chain book's, which B-RESTORE-CB needs; the three capture roots and the forensic store are data, never scratch. **A
refused `rm -rf` is handed to the Boss** by §3's route, one tree per command, and verified by `test -e`.

---

## 10. Pre-send checks

Performed by the Architect on 2026-10-10 against this file as sent, in a reading separate from its writing, with the
repository at `origin/main` `11a01799ceb43fe050603caf1a19233c59b68a55` and map revision `2026-10-10-b` as it ships with
this TZ. Line numbers of Appendix A are the extracted file's.

| # | check | result |
|---|---|---|
| **C1** | scope against body | **Repository paths the body names, 13, and the 33 files of the map's table:** `CryptoTZ/TZ-26-nesting-b3-capture.md`, read by §0.1's script; `SYSTEM-MAP.md` and its table's files, read by `I0 fingerprint`; `BTC-EXECUTOR-INSTRUCTIONS.md`, cited for §1, §4.2, §6 and §8; `research/tz26-nesting-b3-capture.py` and `deploy/systemd/btc-pairbook.service`, written on the branch, staged, copied to `/root/btc-pairbook-svc/` and to `/etc/systemd/system/`; `research/tz18a-chainbook-capture.py`, cited for lines 79, 80 and 296 to 314, never imported or run; `deploy/systemd/btc-chainbook.service`, the unit the new one derives from, its installed copy disabled by B-SWITCH and never edited; `CryptoTZ/TZ-04a-market-recorder-corrected.md`, `CryptoTZ/TZ-18a-chainbook-capture-redeploy.md`, `CryptoTZ/TZ-20-capture-under-systemd.md` and `CryptoReports/TZ-24-nesting-b2-report.md`, cited and read by no step; every `CryptoReports/*.md`, read by `reclaim` for hashes; `CryptoReports/TZ-26-nesting-b3-capture-report.md`, written to `main`. **Entry points:** Appendix A's fifteen modes — `serve`, `prestart`, `prove`, `load`, `fingerprint`, `selftest`, `still`, `mark`, `chainbook`, `unit`, `restart`, `restored`, `final`, `scratch`, `reclaim` — §0.1's script, `git`, `gh`, `systemctl` (`show`, `is-active`, `is-enabled`, `cat`, `daemon-reload`, `enable --now`, `disable --now`, `kill`), `systemd-analyze verify`, `journalctl -u`, and the shell reads of §0.3, §3.4, §3.6, §3.11, §4.7 and §9. **Outputs:** under `/root/tz26-work/` `logs/`, `state.json`, `stage/`, `wt/`, `prestart/` or `prestart-2/` with `prestart.json` and `stream.jsonl.gz`, `proof/proof-A.json` and the self-test's transient `selftest-tmp/`; `/root/btc-pairbook-svc/` with `commit.txt`; the installed unit and its enable link; under `/var/lib/btc-pairbook/`, by the unit, `runtime.jsonl`, `service.pid`, `service.log` and each window's `documents.jsonl`, `books.jsonl.gz`, `stream*.jsonl.gz` and `window.json`; the chain book's own `stop` record, and on a FAIL its `start`; the forensic store's copies; the report, the branch and the pull request. **Intersections with §2, by path and by content class, 8, each named in §2:** the report on `main` — paths item 2, prohibited item 7's exemption; the unit's store, which holds prices, sizes, books and live documents — item 4 and item 9's "the capture's own store"; the chain book's own writes at its stop and restart — item 3's exemption; `prestart`'s ETH stream file, which holds prices — item 9's exemption; §9's copies of `prestart/`, `logs/`, `state.json`, `proof/` and `stage/` — items 6 and 9; §0.3's `df`, `find`, `grep -c` and `test -d` and B-RECLAIM-OWN's `df` under the capture roots — items 2 and 3; the self-test's three deliberate opens under the three roots, refused before they happen — items 2 to 4; the pull request — item 8 names `gh`. **Classes checked and intersecting nothing:** `prestart.json` and `proof-A.json` carry no price, size, book or hash key, asserted by `assert_keys` against `FORBIDDEN_KEYS` (Appendix A lines 179 to 182, 379 to 394, 1784 and 1909); the manifests read carry no price, size, fill or outcome (map §2.3, the manifest exception); no settled document is fetched. |
| **C2** | origin of every expectation | **§5's literals are the unit's own text and Appendix A's exits**, fixed by the Architect and measured by nothing: `Restart=always`, `RestartSec=5`, `RestartPreventExitStatus=1 2 3`, `StartLimitIntervalSec=3600`, `StartLimitBurst=5`, `MemoryMax=128M`; "8 of its 22 lines" is `diff` of Appendix A's unit against `deploy/systemd/btc-chainbook.service` at `11a0179`, exact. **§7's, by kind.** Quoted from a committed artifact: V1's revision, `6`, `4`, `34` and `31`, map `2026-10-10-b` §0, which ships in this upload; V2's `/dev/vda2`, `31612203008` and H3's `17.1`, map §6; V19's two worktrees, map §3. Computed by an implementation independent of the one under test: V3's and V5's SHA-256, lines and bytes, by `sha256sum` and `wc` over Appendix A, exact. Fixed by Appendix A's code, which this TZ measures nothing to set: V4's `74`, V6's `3` requests, `1` session and `7` checks, V8's `4` checks, V9's `10` and `7`. Derived from §4's definitions: V12's `0.25`; V15's `2,016` = 604,800 / 300, `4`, and `25` = 4 + 7 + 14. **§4's error rates**, by an mpmath binomial at 60 digits outside the instrument: `0.00059203`, `0.26171875`, `0.6875`, `0.0027171218677…` printed as `0.0027171219`, `0.9833852514627…` as `0.9833852515`, `0.5406170776759…` as `0.5406170777`, `0.68359375`, `0.9375`, and their family sum `0.0033091518677…` bounded by `0.0033091519`; the self-test asserts the same values from `Fraction` arithmetic, exact. **The self-test's literals:** the schedule's instants for `T = 1791627300` and Tier C's, integers computed outside the instrument; `44136fa3…`, the SHA-256 of `{}`, by `hashlib` outside it. §0.4's floors: `5,100,000,000` = `4,500,000,000` + `500,000,000` + `100,000,000`; `107,503,616` = 2 × `53,751,808`, the Architect's measured peak, made before this TZ was sent. **No expectation depends on a quantity this TZ measures:** every gate compares a measured count with a threshold fixed in §4, and `m`, `f`, the false alarm, the rate and the load are printed, not expected. |
| **C3** | shape of every diff | Two paths, both new: `git cat-file -e 11a0179:research/tz26-nesting-b3-capture.py` and `…:deploy/systemd/btc-pairbook.service` exit `128`, so the change replaces **none** of their lines; V3 asserts both `A`. The report's path is new too, exit `128`. The words "insertions only" appear nowhere in this TZ: `grep -c` prints `0`. |
| **C4** | cost of every check | §6, at the population's upper bound. `selftest` `60` s; `prestart` `660` s, twice at most — the scan's 2,016 opens at the fail-fast edge, `0.3` s each after its first 100 (`2,016 × 0.3 = 604.8`), the 25 s session and three requests at their 5 s timeout, each process scan one read per pid; a deciding `prove` `122` s — at most 7 considered windows, `T` in `[s − 880, s + 5,390]`, a span of 6,270 s, each at the cut, at `17.5` s a window, the slowest of four measured runs of `63.3` to `87.3` s for five; a NOT YET `prove` `5` s, at most 9 runs, from `T1 + 4,020 >= s + 3,535` to `s + 6,000` every 300 s; each other mode `30` s, 14 runs. **Single-session processor at most `2,089` s, under `3,600`; nothing is sampled.** The fail-fast bounds: the base-rate scan's `30` s for its first 100 opens, TZ-18a's own, Appendix A line 1833; the stream cut at `100,000,000` stored bytes, `WINDOW_STREAM_MAX`, which bounds `prove`'s read of a window, line 134. Wall clock at most about `6,500` s, derived term by term in §6. |
| **C5** | every count | V1's `34` = 31 + 2 + 1, read from map `2026-10-10-b` §0; its `4` re-derived anchors `A2`, `A4`, `A5`, `A6`. V3's and V5's `2`: Appendix A's two files. V4's `74`: the count Appendix A's self-test prints, re-run by the Architect on the frozen file, three runs. V6: `3` requests = 2 documents + 1 book; `7` session checks, the keys of `checks` at lines 1891 to 1897. V8's `4`: lines 1488 to 1491. V9's `10`: `unit_reads`' keys, lines 1533 to 1541; `7` more for G-START, lines 1559 to 1565. G-STREAM's `4` windows; G-BOOKS' `28` = 4 × 7 checkpoints; G-TIERC's `4` exposed intervals, one a window. V15's `2,016` = the slots `base_rate` lists, line 1805, `604,800 / 300`; a deciding `prove`'s `25` = 4 counted exposed manifests (line 1737) + one per considered window (line 1691), at most 7 by C4's span, + at most 14 control intervals — 20 slots of 300 s in `(s, s + 6,000]`, of which at least 6 are ≡ 600 (mod 900) and never control (line 1759); a NOT YET run's `4`. §0.3's seven BLOCKING conditions: H1 to H5, memory, disk. §0.5's `30` ref lines, map §1. The proof's 7 windows, 9 NOT YET runs and 14 other mode runs, as C4. |
| **C6** | every population | P-START: the ETH nested pair of the current window, its 3 requests and 1 session. `m` and `f`: the 2,016 five-minute slots closing in the week before `prestart`. G-CB-STOP: the chain book's unit, its argv's processes and its `runtime.jsonl`. G-UNIT: the pair book's unit at `0` and at `1` restarts; G-START: its `start` records. G-STREAM: the first 4 qualifying windows; G-BOOKS: their 28 checkpoints; G-TIERC: their 4 exposed intervals. The printed rows: every considered window; the lag quantiles: one window's `price_change` frames, clamped to `[−1,000, 60,000]` ms; Tier C's offsets: each exposed and control interval's `quote_offsets_ms`. G-LOAD: the service's process from its start to `load`. G-RESTART: the service's records after the `kill-svc` mark. G-STILL: the recorder's unit, §3.3 to §3.10. The BTC pair's measured rate (§8): G-STREAM's four windows. Each memory peak: one mode's process. `MemAvailable` and free space: the host at each read. |
| **C7** | every signature and every behaviour | **Committed code the TZ cites, read at `11a0179`:** `research/tz18a-chainbook-capture.py` line 79 `RESOURCE_FLOOR = 2200000000` and line 80 `WRITE_CAP = 200000000`; `def checkpoint_is_complete(entries):` at line 296, its body at lines 297 to 314 — four entries, each `status == 200`, `bytes` non-empty, `json.loads` of `raw` not raising, `skew_of` not `None` and at most `SKEW_BOUND_NS = 1000000000` (line 90) — which Appendix A lines 521 to 539 repeat statement for statement, a docstring and one variable name apart; `BOOK_KEYS` at lines 675 to 677 and `json_line` at lines 233 to 235, `ensure_ascii=False`, `sort_keys=True`, compact separators — equal to Appendix A's at lines 163, 164 and 327, 328, so its book lines are the chain book's byte for byte; the chain book's stop on `SIGTERM`, `signal.signal(signal.SIGTERM, _sigterm)` at line 810 and `runtime_record("stop", …)` in the `finally` at line 824, which G-CB-STOP reads; its records' `event`, `pid` and `wall_ns`, lines 586 to 589. `research/recorder/manifest.py` lines 230 to 232, `complete`, `quotes_complete` and `quote_offsets_ms` with each entry's `offset_ms` (line 207), which `manifest_of` reads (Appendix A lines 1661 to 1674); `research/recorder/recorder.py` lines 371 to 380, `close_interval` writing the manifest after `fetch_s7`, which §3.8 relies on. **`websockets` 17.1's `connect`**, read from the library: `compression` default `deflate`, `user_agent_header` `Python/3.12 websockets/17.1`, `proxy` `True`, `ping_interval` `20`, `close_timeout` `10`, `open_timeout` `10`, `max_size` `1048576`, `max_queue` `16`; Appendix A lines 594 to 599 pass `None`, its own agent, the default proxy, `None`, `2`, `10`, `1048576` and `16`. **Every behaviour this TZ attributes to Appendix A:** `-O` refused, lines 65 to 67; the three endpoints, lines 71 to 73, asserted the only ones at line 2450; the audit hook, `policy` lines 240 to 283 applied before each event at lines 286 to 301; the floors, lines 131 to 136, `floor_check` at 372 to 376, called by `prove` and `prestart` at lines 1725 and 1819; `build_request` and `http_get`, lines 459 to 491, stamps only where a status came back, lines 482 to 484; the documents' retry to `T+880`, lines 937 to 940; the four reads released together, lines 564 to 584; the subscribe frame, lines 589 to 591; the session's events, lines 707 to 746, `101` and the extensions at 712 and 713; the reconnect ladder, line 775; the stream file's line shapes, lines 652 to 690, its sync flush at 641, its cut at 649 and 650, its `end` line at 685; the stream floor and cap, lines 809 to 817; a second process's file name, lines 750 to 756; joining late, lines 437 to 449 and 1050 to 1055; the window's order — the floor at 976, the stream at 984 to 987, an error kept at 996 and 997, the books at 999 and 1000, `window.json` asserted against its keys at 1014 and written at 1015; the exits — `0` after `SIGTERM` (lines 1034, 1035 and 1072), `1` at a floor or the write cap (1059 to 1063, and 331 to 336), `1` on a refused open (1064 to 1066), an error record and the next window (1067 to 1070), `2` at lines 1085 to 1088, `3` at 1042 and 1043; equality with the exact argv, lines 828 to 837; G-STREAM's unit, lines 1178 to 1303 — late subscribe 1289, initial books 1273 and 1291, gap 1294, short 1296, count 1300, the lag 1271 — and its totality, `stream_rows` lines 1094 to 1127 and `window_row` lines 1677 to 1721; the readings, lines 1324 to 1343; `considered` and `qualifies`, lines 1653 to 1658; NOT YET, lines 1738 to 1742; determinism's `unchanged`, line 1791; no request by `prove`, line 1785; G-TIERC's counting by `st_mtime_ns`, line 1668, and fully loaded, lines 1718 to 1720; the control intervals, lines 1756 to 1763; G-LOAD, lines 1615 to 1641; G-UNIT and G-START, lines 1524 to 1573; G-CB-STOP, lines 1472 to 1496; G-RESTART, lines 1576 to 1594; RESTORED, lines 1499 to 1521; G-STILL, lines 1426 to 1448, an unreadable unit other than the recorder printed at 1433 to 1436; P-START, lines 1816 to 1916 — the service's argv absent at 1827, the fail-fast at 1833, three requests at 1876, the seven checks at 1891 to 1897; the self-test's five HTTP header fields at line 2209 and six handshake fields at 2259; `scratch`'s live rule, line 1954, and `reclaim`'s, line 1997, its paths at 1983 to 1988, its kept names at 1967 to 1970, its pristine worktree at 1973 to 1980, its store count at 2034. **Three sentences were rewritten before sending:** §5 had the unit differ in "four lines", and `diff` names eight; §5 had a failed assert end the service, and inside a window it is an `error` record; §4.4 had a fully loaded checkpoint "issue" four reads, and line 1720 counts four statuses. |
| **C8** | every cross-reference | Resolved by reading the text referenced. **Map `2026-10-10-b`:** §0's anchors and 34 rows, 31 / 2 / 1; §1's `11a0179`, `tz-23-maker-m0` at `7f5ae3f`, `tz-24-nesting-b2` at `6f045cf` and 30 ref lines; §2.3's manifest exception and the resolution's median of `318` s; §2.5's terms of the reserve and the pair book; §3's store at `1,725`, the two worktrees and TZ-24's pair `5c15abf7…` / `65948b60…`; §5's record of the protocol's verification; §6's host identity, `/root/tz04a-env` with `websockets` 17.1, one processor, `1,002,127,360` bytes, TZ-24's `261,439,488` to `300,302,336`, the `2,000,000,000` floor and the fastest drain `187,760,570` bytes a day, which makes `2,500,000,000` thirteen days, and "Unauthorized Persistence". **CANON `2026-10-10-b`:** PART II's B3 question, its row and M0's rule on `T0 > 1791241800`; §1.1's 150 ms taker delay; hard rules 11, 13, 14 and 15. **Contract:** §1 steps 1 to 4, §4.2's self-check, §6's determinism, §8's order. **Other artifacts:** TZ-04a §4's line, `recv_ns`, `mono_ns`, `raw`; TZ-18a §10 C4's fail-fast and its line 288; TZ-20's K-20C, `systemctl disable --now btc-chainbook.service`; TZ-24 report §2.6, the six incomplete windows, and §2.9, the chain book's `MemoryCurrent` and `MemoryPeak`; TZ-23's `4,820,537` fills over 4,032 markets inside `[T0, T0 + 240)`, map §4. **This TZ:** §0.1 to §0.5, §1, §2's items, §3.1 to §3.11, §4.1 to §4.8, §5, §6, §9 and Appendix A, each supporting the sentence that cites it. Two references were corrected before sending: the TZ-24 report's sections were cited as §3.8 and §2, and are §2.9 and §2.6. **None unresolved.** |

**Three checks could not be performed from this session, because it is not the capture host** (map §6), and each is a
BLOCK condition of this TZ under CANON hard rule 13: the host's reach of the market websocket and of both REST
endpoints under this file's `User-Agent` — P-START, §3.5, before anything is installed; the host's interpreter and its
`websockets` — H3; and the host's own state, its free space, memory, units and trees — §0.3. Everything else above was
performed here, on the frozen files, under Python 3.12.3 with `websockets` 17.1.

---

## Appendix A — the two files, byte for byte

Extracted by §0.1's script; each block's content is its file.

```ini file=deploy/systemd/btc-pairbook.service
# btc-5m-twap: the pair book, B3's capture of the nested pair's four books, as a system unit (TZ-26).
# Installed byte for byte as /etc/systemd/system/btc-pairbook.service.
[Unit]
Description=btc-5m-twap pair book, the nested pair's four books streamed
Wants=network-online.target
After=network-online.target time-sync.target
StartLimitIntervalSec=3600
StartLimitBurst=5

[Service]
Type=simple
WorkingDirectory=/root/btc-pairbook-svc
ExecStart=/root/tz04a-env/venv/bin/python -B -u /root/btc-pairbook-svc/tz26-nesting-b3-capture.py serve
Restart=always
RestartSec=5
RestartPreventExitStatus=1 2 3
MemoryMax=128M
StandardOutput=append:/var/lib/btc-pairbook/service.log
StandardError=append:/var/lib/btc-pairbook/service.log

[Install]
WantedBy=multi-user.target
```

```python file=research/tz26-nesting-b3-capture.py
#!/usr/bin/env python3
"""TZ-26 - the backup track's B3, its capture: the four books of the nested pair, streamed.

    serve             the service. For each 900 s window T: the documents of btc-updown-15m-{T} and
                      btc-updown-5m-{T+600} from T+545; the market websocket for their four tokens from
                      T+595 to T+905, every frame stored verbatim with its receive stamps; the chain
                      book's seven /book checkpoints, T+655 to T+885; window.json at T+910
    prestart          the request path on this host before the service starts, on the ETH nested pair:
                      two documents and one book through http_get, one stream session of 25 s through
                      the service's own stream code; the processes; G-TIERC's base rate
    prove A           G-STREAM, G-BOOKS and G-TIERC as of the epoch A; exit 3 is NOT YET
    load              G-LOAD: the service's processor time and memory since its start
    fingerprint       map section 0 against the primary checkout
    selftest          every rule of this file, on literals and on loopback servers only
    still             the recorder's unit: the first run records it, a later run compares (G-STILL)
    mark NAME         an instant, and the state of the unit it concerns, into state.json
    chainbook         the chain book's stop, from systemd, /proc and its own record (G-CB-STOP)
    unit N            G-UNIT for btc-pairbook.service at N restarts; at 0, G-START too
    restart           G-RESTART, from the service's own record
    restored          after a FAIL's two blocks: the pair book stopped, the chain book running again
    final             G-UNIT at one restart, G-STILL, and the unit's memory
    scratch OWN       the UUID directories beside OWN, this session's directory: live or earlier
    reclaim TREE...   section 9

It requests gamma-api.polymarket.com/markets/slug/, clob.polymarket.com/book and the market websocket
of ws-subscriptions-clob.polymarket.com, and nothing else, every request with the headers this file
fixes. It never authenticates, holds no credential and can place no order. The service writes what it
receives byte for byte and reads none of it back; no mode prints a price, a size, a side, a book's hash or
an outcome. An audit hook enforces section 2 of the TZ: under /var/lib/btc-recorder only a manifest.json is
opened, read only, by prestart and prove; under /var/lib/btc-chainbook only runtime.jsonl, read only, by
chainbook and restored; under /var/lib/btc-pairbook only serve writes; serve starts no process. Exit 0: every assert
held. Exit 1: an assert or a floor, named. Exit 2: serve refused its command line. Exit 3: another
instance runs, or NOT YET. Run it with /root/tz04a-env, whose websockets it needs.

Written for CryptoTZ/TZ-26-nesting-b3-capture.md. The TZ is the specification.
"""

import ast
import asyncio
import base64
import datetime
import errno
import gzip
import hashlib
import http.server
import json
import os
import re
import resource
import shutil
import signal
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request
import zlib
from fractions import Fraction

import websockets
from websockets.asyncio.client import connect as ws_connect
from websockets.asyncio.server import serve as ws_serve

if not __debug__:
    sys.stderr.write("tz26: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(1)

# ---- the endpoints, and nothing else: three string constants carry a scheme separator ----------

GAMMA_MARKET_URL = "https://gamma-api.polymarket.com/markets/slug/{slug}"
CLOB_BOOK_URL = "https://clob.polymarket.com/book?token_id={token_id}"
CLOB_WS_URL = "wss://ws-subscriptions-clob.polymarket.com/ws/market"

# ---- the TZ's constants: none of them is measured by this run -----------------------------------

MAP_REVISION = "2026-10-10-b"
ANCHORS = {"A1": "229a944f2d51", "A2": "6c5089330629",
           "A3": "0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable",
           "A4": "437b45ea196b", "A5": "0f6c90451cbd", "A6": "729f0bcdbee3"}
ANCHOR_FILES = {"A2": "research/twap-divergence.py", "A4": "BTC-EXECUTOR-INSTRUCTIONS.md",
                "A5": "research/recorder/recorder.py", "A6": "research/pfair.py"}
MAP_ROWS = {"frozen": 31, "tracked": 2, "reported": 1}

ROOT = "/var/lib/btc-pairbook"
RECORDER = "/var/lib/btc-recorder"
CHAINBOOK = "/var/lib/btc-chainbook"
SVC = "/root/btc-pairbook-svc"
WORK = "/root/tz26-work"
PRIMARY = "/root/btc-5m-twap"
REPORTS = PRIMARY + "/CryptoReports"
FORENSICS = "/root/btc-forensics"
WT = WORK + "/wt"
STATE = WORK + "/state.json"
DISK_PATH = "/var/lib"

UNIT = "btc-pairbook.service"
UNITS = {"recorder": "btc-recorder.service", "chainbook": "btc-chainbook.service", "pairbook": UNIT}
PYTHON = "/root/tz04a-env/venv/bin/python"
SERVICE_FILE = SVC + "/tz26-nesting-b3-capture.py"
SERVICE_ARGV = (PYTHON, "-B", "-u", SERVICE_FILE, "serve")
CHAINBOOK_ARGV = ("/root/tz01-env/venv/bin/python", "-B", "-u",
                  "/root/tz18a-svc/tz18a-chainbook-capture.py", "--serve")
MEMORY_MAX = 134217728       # MemoryMax=128M, the unit's ceiling (TZ-26 section 0.4)

UA = "btc-5m-twap-tz26"
ACCEPT = "application/json"

WINDOW = 900
DOC_OFFSET = 545             # the documents, from T+545, every DOC_RETRY_S until both carry token ids
DOC_RETRY_S = 5
DOC_GAP_S = 0.200            # >= 200 ms between two document requests
DOC_LAST = 880               # no document attempt starts after T+880
STREAM_OPEN = 595            # the stream, T+595 to T+905: the five-minute market's whole window, 5 s each side
STREAM_CLOSE = 905
CHECKPOINT_OFFSETS = (655, 715, 775, 805, 835, 865, 885)   # the chain book's seven
CLOSE_OFFSET = 910           # window.json
JOIN_LAST = 880              # a process starting inside a window joins it until T+880
READ_TIMEOUT_S = 5.0
GZ_LEVEL = 6                 # books.jsonl.gz, at the chain book's level
GZ_STREAM = 9                # stream files (TZ-26 section 6)
FLUSH_S = 10                 # a sync flush of the stream file at least every 10 s of frames
PING_S = 10                  # the venue's heartbeat: the text frame PING every 10 s
OPEN_TIMEOUT_S = 10
CLOSE_TIMEOUT_S = 2
MAX_FRAME = 1048576          # websockets' own default, 2 ** 20
MAX_QUEUE = 16               # and its queue: memory bounded at 16 frames of 1 MiB
BACKOFF_S = (1, 2, 4, 8)     # before a reconnect inside a window
SKEW_BOUND_NS = 1000000000   # a checkpoint's four replies within one second (the chain book's rule)

RESOURCE_FLOOR = 2200000000  # free bytes below which the service halts, exit 1
STREAM_FLOOR = 4500000000    # free bytes below which no stream opens for a window
STREAM_CAP = 8000000000      # stream bytes under ROOT at which no stream opens
WINDOW_STREAM_MAX = 100000000    # stored bytes of one window's stream at which it is cut
WRITE_CAP = 200000000        # bytes one process writes but its stream files
MEM_FLOOR = 107503616        # MemAvailable floor of prestart and prove: twice the self-test's peak (TZ-26 0.4)

# section 4 - the gates, fixed before their data
GATE_WINDOWS = 4             # G-STREAM and G-BOOKS: the first four qualifying windows
GATE_STREAM_PASS = 3         # >= 3 of 4 complete
GATE_CHECKPOINTS = 28        # G-BOOKS: their 28 checkpoints
GATE_BOOKS_PASS = 26         # >= 26 of 28 complete
TIERC_MIN = 2                # G-TIERC: at least two counted fully loaded exposed intervals
LOAD_MAX = Fraction(1, 4)    # G-LOAD: at most a quarter of the one processor, since the start
QUALIFY_LEAD_S = 60          # a window qualifies when T+545 >= s + 60
BUDGET_S = 6000              # the proof decides by s + 6,000
SUBSCRIBE_BY = 600           # the first subscribe at or before T+600
INITIAL_S = 5                # a book of each of the four tokens within 5 s of it
END_BY = 900                 # the stream's last close at or after T+900
GAP_MAX_NS = 15000000000     # no two consecutive received instants more than 15 s apart
LAG_RANGE_MS = (-1000, 60000)  # the venue-to-host lag, counted in ms and clamped to this range
BASE_RATE_S = 604800         # G-TIERC's base rate: the week before prestart
FA_UNITS = 4                 # four exposed intervals are judged
RESTART_MAX_S = 60
KNOWN = ("book", "price_change", "last_trade_price", "tick_size_change")

TOKEN = re.compile(r"[0-9a-f]{16,64}")
UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
MANIFEST_RE = re.compile(re.escape(RECORDER) + r"/btc-updown-5m/[0-9]{10}/manifest\.json")
LIVE_S = 60

# the stored formats, and the allow-lists every output is asserted against before it is written
BOOK_KEYS = ("T", "tau_prime", "market", "slug", "token_id", "outcome_label", "url", "status",
             "send_mono_ns", "recv_mono_ns", "recv_wall_ns", "bytes", "sha256", "raw", "reason")
DOC_KEYS = ("slug", "url", "status", "send_mono_ns", "recv_mono_ns", "recv_wall_ns", "bytes",
            "sha256", "raw", "attempt", "pid")
WINDOW_JSON_KEYS = frozenset(("T", "document_instant", "documents_ok", "document_attempts",
                              "documents_ready_wall_ns", "closed_wall_ns", "checkpoints_complete",
                              "status_counts", "skews_ns", "missed", "markets", "stream", "joined_late",
                              "stopped", "pid"))
WINDOW_MARKET_KEYS = frozenset(("slug", "clobTokenIds", "outcomes", "conditionId"))
STREAM_KEYS = frozenset(("opened", "off_reason", "files", "segments", "frames", "frame_bytes", "pongs",
                         "pings", "first_frame_wall_ns", "last_frame_wall_ns", "max_gap_ns",
                         "subscribed_wall_ns", "stored_bytes", "cut"))
PRESTART_JSON_KEYS = frozenset(("mode", "p_wall", "file_sha256", "processes", "proxy_variables",
                                "base_rate", "requests", "stream", "counters"))
PROOF_JSON_KEYS = frozenset(("mode", "as_of", "start", "windows", "g_stream", "g_books", "g_tierc",
                             "control", "counters"))
FORBIDDEN_KEYS = frozenset(("price", "prices", "bid", "bids", "ask", "asks", "mid", "midpoint", "size",
                            "sizes", "level", "levels", "book", "books", "spread", "raw", "priceToBeat",
                            "finalPrice", "best_bid", "best_ask", "amount", "quote", "quotes", "side",
                            "outcomePrices", "hash"))
FRAME_KEYS = frozenset(("recv_ns", "mono_ns", "raw"))
FRAME_B64_KEYS = frozenset(("recv_ns", "mono_ns", "raw_b64"))

HERE = os.path.dirname(os.path.abspath(__file__))
MODE = [None]
COUNTERS = {"requests": 0, "sessions": 0, "bytes_written": 0, "stream_bytes": 0, "frames": 0}
_LOCK = threading.Lock()
STOP_FLAG = threading.Event()
STOP_EVENT = [None]


class GuardError(RuntimeError):
    pass


class FloorStop(Exception):
    pass


def bump(name, by=1):
    with _LOCK:
        COUNTERS[name] += by
        return COUNTERS[name]

# ---- the audit hook: TZ-26 section 2 as a pure function, and the hook that applies it ------------


WRITE_FLAGS = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC
REFUSED = []
OPENS = {"manifest.json": 0, "chainbook": 0}
HOOKED = ("open", "os.listdir", "os.scandir", "subprocess.Popen", "os.system", "os.exec", "os.spawn",
          "os.posix_spawn", "os.fork", "os.forkpty")


def _under(p, root):
    return p == root or p.startswith(root + "/")


def _writing(wmode, flags):
    if isinstance(wmode, str):
        return bool(set(wmode) & set("wax+"))
    return isinstance(flags, int) and bool(flags & WRITE_FLAGS)


def _exclusive(wmode, flags):
    if isinstance(wmode, str):
        return "x" in wmode
    return isinstance(flags, int) and bool(flags & os.O_EXCL)


def _path(args):
    p = args[0] if args else None
    if isinstance(p, bytes):
        p = os.fsdecode(p)
    return os.path.abspath(p) if isinstance(p, str) else None


def policy(mode, event, args):
    """None where section 2 allows the event in this mode; otherwise the reason it is refused."""
    if event == "open":
        p = _path(args)
        if p is None:
            return None
        wm, fl = (args[1] if len(args) > 1 else None), (args[2] if len(args) > 2 else None)
        w = _writing(wm, fl)
        if _under(p, RECORDER):
            if mode in ("prestart", "prove") and not w and MANIFEST_RE.fullmatch(p):
                return None
            return "the recorder's root"
        if _under(p, CHAINBOOK):
            if mode in ("chainbook", "restored") and not w and p == CHAINBOOK + "/runtime.jsonl":
                return None
            return "the chain book's root"
        if _under(p, ROOT):
            if w:
                return None if mode == "serve" else "a write under the pair book's root"
            return None if mode in ("serve", "prove", "load", "unit", "restart", "final", "restored") else \
                "a read under the pair book's root"
        if w:
            if mode == "serve":
                return "a write outside the pair book's root"
            if _under(p, WORK):
                return None
            if mode == "reclaim" and _under(p, FORENSICS) and _exclusive(wm, fl):
                return None
            return "a write outside the work tree"
        return None
    if event in ("os.listdir", "os.scandir"):
        p = _path(args)
        if p is None:
            return None
        if _under(p, RECORDER):
            return "a listing under the recorder's root"
        if _under(p, CHAINBOOK):
            return "a listing under the chain book's root"
        if _under(p, ROOT):
            return None if mode in ("serve", "prove") else "a listing under the pair book's root"
        return None
    if event in HOOKED:
        return "a process started by the service" if mode == "serve" else None
    return None


def _audit(event, args):
    if event not in HOOKED:
        return
    why = policy(MODE[0], event, args)
    if why is not None:
        REFUSED.append((event, str(args[0]) if args else ""))
        raise GuardError("%s refused in mode %s, %s: %r" % (event, MODE[0], why, args[0] if args else None))
    if event == "open":
        p = _path(args)
        if p is not None and _under(p, RECORDER):
            OPENS["manifest.json"] += 1
        elif p is not None and _under(p, CHAINBOOK):
            OPENS["chainbook"] += 1


sys.addaudithook(_audit)

# ---- small helpers -------------------------------------------------------------------------------


def out(msg):
    sys.stdout.write("[%s] %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    sys.stdout.flush()


def utc(t):
    return datetime.datetime.fromtimestamp(float(t), datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def json_line(obj):
    return (json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def account(n):
    """Every byte a process writes but its stream files, against WRITE_CAP."""
    total = bump("bytes_written", n)
    if total > WRITE_CAP:
        raise FloorStop("write cap: %d bytes written, above %d" % (total, WRITE_CAP))
    return total


def append_bytes(path, data):
    with open(path, "ab") as fh:
        fh.write(data)
    account(len(data))


def write_new(path, data):
    """A file that must not exist yet: exclusive create."""
    with open(path, "xb") as fh:
        fh.write(data)
    account(len(data))


def free_bytes():
    st = os.statvfs(DISK_PATH)
    return st.f_bavail * st.f_frsize


def guard_resources():
    free = free_bytes()
    if free < RESOURCE_FLOOR:
        raise FloorStop("free %d bytes, below the floor %d" % (free, RESOURCE_FLOOR))
    return free


def mem_available():
    with open("/proc/meminfo", encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("MemAvailable:"):
                return int(line.split()[1]) * 1024
    raise AssertionError("no MemAvailable")


def floor_check():
    """Before a mode that reads the venue or the capture: the host's memory floor (section 0.4)."""
    avail = mem_available()
    out("MemAvailable %d bytes, floor %d" % (avail, MEM_FLOOR))
    assert avail >= MEM_FLOOR, "BLOCKED: MemAvailable %d bytes, below %d" % (avail, MEM_FLOOR)


def assert_keys(obj, allowed, what):
    got = frozenset(obj)
    assert got == allowed, "%s key set %s, required %s" % (what, sorted(got), sorted(allowed))
    forbid(obj, what)


def forbid(obj, what, depth=0):
    """No price, size, level, side or hash leaves the store through an output file."""
    assert depth < 12, "%s nested too deep" % what
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert k not in FORBIDDEN_KEYS, "%s carries a forbidden key: %s" % (what, k)
            forbid(v, what, depth + 1)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            forbid(v, what, depth + 1)


def load_state():
    if not os.path.exists(STATE):
        return {}
    with open(STATE, encoding="utf-8") as fh:
        return json.load(fh)


def save_state(state):
    tmp = STATE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(state, sort_keys=True, indent=1) + "\n")
    os.replace(tmp, STATE)


def quantiles(values):
    if not values:
        return None
    v = sorted(values)
    return {"n": len(v), "min": v[0], "median": v[(len(v) - 1) // 2], "p99": v[(len(v) * 99) // 100],
            "max": v[-1]}

# ---- the schedule -------------------------------------------------------------------------------


def slug15(t, asset="btc"):
    return "%s-updown-15m-%d" % (asset, t)


def slug5(t, asset="btc"):
    return "%s-updown-5m-%d" % (asset, t)


def schedule_for(T):
    assert T % WINDOW == 0, "a window starts on a 900-second boundary: %d" % T
    return {"T": T, "document_instant": T + DOC_OFFSET, "stream_open": T + STREAM_OPEN,
            "stream_close": T + STREAM_CLOSE,
            "checkpoints": [(T + off, WINDOW - off) for off in CHECKPOINT_OFFSETS],
            "close_instant": T + CLOSE_OFFSET}


def next_window(now):
    """The window to run next and whether it is joined late: the current 900 s window until T+880,
    after that the next one."""
    c = int(now) // WINDOW * WINDOW
    if now <= c + JOIN_LAST:
        return c, now > c + DOC_OFFSET
    return c + WINDOW, False


def joinable(wdir):
    """A window a process may still run: no earlier process closed it or wrote its books."""
    return not (os.path.exists(os.path.join(wdir, "window.json")) or
                os.path.exists(os.path.join(wdir, "books.jsonl.gz")))


def tierc_instants(T):
    """The recorder's seven Tier C reads of btc-updown-5m-{T+600} (config.py line 93)."""
    return [T + 600 + 300 - tau for tau in (240, 180, 120, 90, 60, 30, 10)]

# ---- the network: two REST endpoints -------------------------------------------------------------


def build_request(url):
    """The one builder of every HTTP request: GET with Accept and this file's User-Agent."""
    return urllib.request.Request(url, method="GET", headers={"Accept": ACCEPT, "User-Agent": UA})


def http_get(url, timeout=READ_TIMEOUT_S):
    """One GET through build_request. No retry. Both receive stamps only where a status came back."""
    bump("requests")
    send_mono = time.monotonic_ns()
    status, body, reason = None, b"", None
    try:
        with urllib.request.urlopen(build_request(url), timeout=timeout) as resp:
            status = int(resp.status)
            body = resp.read()
    except urllib.error.HTTPError as exc:
        status = int(exc.code)
        try:
            body = exc.read()
        except Exception:
            body = b""
        reason = "http_error"
    except Exception as exc:
        reason = type(exc).__name__
    recv_mono, recv_wall = time.monotonic_ns(), time.time_ns()
    if status is None:
        recv_mono = recv_wall = None
    try:
        raw = body.decode("utf-8")
    except UnicodeDecodeError:
        raw = body.decode("latin-1")
    return {"url": url, "status": status, "send_mono_ns": send_mono, "recv_mono_ns": recv_mono,
            "recv_wall_ns": recv_wall, "bytes": len(body), "sha256": sha256_bytes(body), "raw": raw,
            "reason": reason}


def parse_maybe_string(v):
    if isinstance(v, str):
        try:
            return json.loads(v)
        except ValueError:
            return v
    return v


def token_ids_of(doc_raw):
    """clobTokenIds, outcomes and conditionId exactly as the document carries them, and the two ids."""
    doc = json.loads(doc_raw)
    if isinstance(doc, list):
        doc = doc[0] if doc else {}
    if not isinstance(doc, dict):
        return None, None, {"clobTokenIds": None, "outcomes": None, "conditionId": None}
    verbatim = {"clobTokenIds": doc.get("clobTokenIds"), "outcomes": doc.get("outcomes"),
                "conditionId": doc.get("conditionId")}
    ids, outs = parse_maybe_string(verbatim["clobTokenIds"]), parse_maybe_string(verbatim["outcomes"])
    if not isinstance(ids, list) or not isinstance(outs, list):
        return None, None, verbatim
    ids, outs = [str(i) for i in ids], [str(o) for o in outs]
    if len(ids) != 2 or len(set(ids)) != 2 or not all(ids):
        return None, None, verbatim
    return ids, (outs[:2] if len(outs) >= 2 else [None, None]), verbatim


def checkpoint_is_complete(entries):
    """The chain book's rule: four replies, all 200, each non-empty and JSON, within one second."""
    if len(entries) != 4:
        return False, "not_four_entries"
    for e in entries:
        if e.get("status") != 200:
            return False, "status_not_200"
        if not e.get("bytes"):
            return False, "empty_body"
        try:
            json.loads(e.get("raw") or "")
        except Exception:
            return False, "body_not_json"
    sk = skew_of(entries)
    if sk is None:
        return False, "no_skew"
    if sk > SKEW_BOUND_NS:
        return False, "skew_above_bound"
    return True, "complete"


def skew_of(entries):
    recvs = [e["recv_mono_ns"] for e in entries if e.get("recv_mono_ns") is not None]
    return (max(recvs) - min(recvs)) if recvs else None


def entry(spec, T, tau, **kw):
    e = dict(spec, T=T, tau_prime=tau, url=None, status=None, send_mono_ns=None, recv_mono_ns=None,
             recv_wall_ns=None, bytes=0, sha256=None, raw="", reason=None)
    e.update(kw)
    return e


def specs_of(plan):
    out_ = []
    for m in ("m15", "m5"):
        ids, labels = plan[m]["ids"], plan[m]["labels"]
        for i in range(2):
            out_.append({"market": m, "slug": plan[m]["slug"], "token_id": None if ids is None else ids[i],
                         "outcome_label": None if labels is None else labels[i]})
    return out_


def fetch_books(T, tau, plan):
    """Four GETs, one per token, each in its own thread, released together (the chain book's design)."""
    specs = specs_of(plan)
    if any(s["token_id"] is None for s in specs):
        return [entry(s, T, tau, reason="no_token_ids") for s in specs]
    entries = [None] * 4
    gate = threading.Event()

    def worker(i, s):
        gate.wait()
        entries[i] = dict(s, T=T, tau_prime=tau, **http_get(CLOB_BOOK_URL.format(token_id=s["token_id"])))

    threads = [threading.Thread(target=worker, args=(i, s), daemon=True) for i, s in enumerate(specs)]
    for th in threads:
        th.start()
    gate.set()
    deadline = time.monotonic() + READ_TIMEOUT_S + 2.0
    for th in threads:
        th.join(max(0.0, deadline - time.monotonic()))
    return [entries[i] if entries[i] is not None else entry(s, T, tau, reason="thread_deadline")
            for i, s in enumerate(specs)]

# ---- the network: the stream ---------------------------------------------------------------------


def subscription(tokens):
    """The documented subscribe frame, compact, the four tokens in the documents' order."""
    return json.dumps({"assets_ids": list(tokens), "type": "market"}, separators=(",", ":"))


def connect_kwargs(proxy=True):
    """Every option of the opening handshake, fixed: no compression offered, no protocol ping, this
    file's User-Agent; `proxy` is websockets' own default, the environment's; None on the loopback."""
    return {"open_timeout": OPEN_TIMEOUT_S, "close_timeout": CLOSE_TIMEOUT_S, "ping_interval": None,
            "max_size": MAX_FRAME, "max_queue": MAX_QUEUE, "compression": None, "user_agent_header": UA,
            "proxy": proxy}


def stopping():
    return STOP_FLAG.is_set()


async def sleep_until(t):
    """True at t; False at once where the service is stopping."""
    while True:
        if stopping():
            return False
        left = t - time.time()
        if left <= 0:
            return True
        ev = STOP_EVENT[0]
        if ev is None:
            await asyncio.sleep(min(left, 0.5))
        else:
            try:
                await asyncio.wait_for(ev.wait(), timeout=min(left, 0.5))
            except TimeoutError:
                pass


class StreamWriter:
    """One stream file: gzip, a sync flush at least every FLUSH_S, one JSON line per received frame -
    recv_ns, mono_ns and raw, the frame verbatim - and one per session event; the last an `end` line."""

    def __init__(self, path, level=GZ_STREAM, window_max=WINDOW_STREAM_MAX, flush_s=FLUSH_S):
        self.path = path
        self.fh = open(path, "xb")
        self.gz = gzip.GzipFile(filename="", mode="wb", fileobj=self.fh, compresslevel=level, mtime=0)
        self.window_max, self.flush_s = window_max, flush_s
        self.last_flush = time.monotonic()
        self.frames = self.frame_bytes = self.pongs = self.pings = 0
        self.first = self.last = self.max_gap = self.subscribed = None
        self.cut = False
        self.stored = 0

    def _line(self, b):
        self.gz.write(b)
        if time.monotonic() - self.last_flush >= self.flush_s:
            self.flush()

    def flush(self):
        self.gz.flush()
        self.fh.flush()
        self.last_flush = time.monotonic()
        self.stored = self.fh.tell()
        if self.stored >= self.window_max:
            self.cut = True

    def frame(self, msg):
        wall, mono = time.time_ns(), time.monotonic_ns()
        if isinstance(msg, (bytes, bytearray)):
            self._line((json.dumps({"recv_ns": wall, "mono_ns": mono,
                                    "raw_b64": base64.b64encode(bytes(msg)).decode("ascii")},
                                   separators=(",", ":")) + "\n").encode("utf-8"))
            n = len(msg)
        else:
            self._line((json.dumps({"recv_ns": wall, "mono_ns": mono, "raw": msg}, ensure_ascii=False,
                                   separators=(",", ":")) + "\n").encode("utf-8"))
            n = len(msg.encode("utf-8"))
            if msg == "PONG":
                self.pongs += 1
        self.frames += 1
        self.frame_bytes += n
        if self.last is not None:
            gap = wall - self.last
            self.max_gap = gap if self.max_gap is None else max(self.max_gap, gap)
        if self.first is None:
            self.first = wall
        self.last = wall

    def event(self, name, **kw):
        obj = {"recv_ns": time.time_ns(), "mono_ns": time.monotonic_ns(), "event": name}
        for k in sorted(kw):
            obj[k] = kw[k]
        if name == "ping":
            self.pings += 1
        if name == "subscribe" and self.subscribed is None:
            self.subscribed = obj["recv_ns"]
        self._line((json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8"))

    def close(self):
        self.event("end", frames=self.frames, frame_bytes=self.frame_bytes, pongs=self.pongs, pings=self.pings)
        self.gz.close()
        self.fh.close()
        self.stored = os.path.getsize(self.path)
        bump("stream_bytes", self.stored)
        bump("frames", self.frames)

    def summary(self):
        return {"frames": self.frames, "frame_bytes": self.frame_bytes, "pongs": self.pongs,
                "pings": self.pings, "first_frame_wall_ns": self.first, "last_frame_wall_ns": self.last,
                "max_gap_ns": self.max_gap, "subscribed_wall_ns": self.subscribed, "cut": self.cut}


async def ping_loop(ws, w, seg, ping_s):
    while True:
        await asyncio.sleep(ping_s)
        await ws.send("PING")
        w.event("ping", seg=seg)


async def one_session(w, seg, tokens, end, url, ping_s, kw):
    """One connection: open, subscribe, every frame to the writer until `end`, a stop, a cut or a drop."""
    w.event("connect", seg=seg, url=url, pid=os.getpid())
    bump("sessions")
    reason, code = None, None
    try:
        async with ws_connect(url, **kw) as ws:
            w.event("open", seg=seg, status=ws.response.status_code,
                    extensions=ws.response.headers.get("Sec-WebSocket-Extensions"))
            msg = subscription(tokens)
            await ws.send(msg)
            w.event("subscribe", seg=seg, message=msg)
            pinger = asyncio.create_task(ping_loop(ws, w, seg, ping_s))
            try:
                while True:
                    left = end - time.time()
                    if left <= 0:
                        reason = "end"
                        break
                    if stopping():
                        reason = "stop"
                        break
                    try:
                        frame = await asyncio.wait_for(ws.recv(), timeout=min(left, 0.5))
                    except TimeoutError:
                        continue
                    w.frame(frame)
                    if w.cut:
                        reason = "cut"
                        break
            finally:
                pinger.cancel()
                try:
                    await pinger
                except BaseException:
                    pass
    except websockets.ConnectionClosed as exc:
        reason = "closed"
        code = exc.rcvd.code if exc.rcvd is not None else None
    except Exception as exc:
        reason = "%s: %s" % (type(exc).__name__, str(exc)[:200])
    w.event("close", seg=seg, reason=reason, code=code)
    return reason


def next_stream_path(wdir):
    k = 0
    while True:
        p = os.path.join(wdir, "stream.jsonl.gz" if k == 0 else "stream.%d.jsonl.gz" % k)
        if not os.path.exists(p):
            return p
        k += 1


async def stream_window(wdir, tokens, start, end, stats, url=CLOB_WS_URL, ping_s=PING_S, kw=None,
                        backoff=BACKOFF_S, level=GZ_STREAM, window_max=WINDOW_STREAM_MAX):
    """The stream of one window: sessions from `start` to `end`, a reconnect after each drop."""
    if not await sleep_until(start):
        return
    kw = connect_kwargs() if kw is None else kw
    w = StreamWriter(next_stream_path(wdir), level=level, window_max=window_max)
    stats["opened"] = True
    stats["files"].append(os.path.basename(w.path))
    seg = 0
    try:
        while not stopping() and time.time() < end and not w.cut:
            await one_session(w, seg, tokens, end, url, ping_s, kw)
            seg += 1
            if stopping() or time.time() >= end or w.cut:
                break
            await sleep_until(min(end, time.time() + backoff[min(seg - 1, len(backoff) - 1)]))
    finally:
        w.close()
        stats["segments"] += seg
        s = w.summary()
        for k in ("frames", "frame_bytes", "pongs", "pings"):
            stats[k] += s[k]
        for k in ("first_frame_wall_ns", "subscribed_wall_ns"):
            if stats[k] is None:
                stats[k] = s[k]
        if s["last_frame_wall_ns"] is not None:
            stats["last_frame_wall_ns"] = s["last_frame_wall_ns"]
        if s["max_gap_ns"] is not None:
            stats["max_gap_ns"] = s["max_gap_ns"] if stats["max_gap_ns"] is None else max(
                stats["max_gap_ns"], s["max_gap_ns"])
        stats["stored_bytes"] += w.stored
        stats["cut"] = stats["cut"] or s["cut"]


def stream_bytes_total(root):
    """The bytes of every stream file under root, by directory entries alone."""
    total = 0
    if not os.path.isdir(root):
        return 0
    with os.scandir(root) as it:
        dirs = [d.path for d in it if d.is_dir(follow_symlinks=False) and d.name.isdigit()]
    for d in dirs:
        with os.scandir(d) as it:
            for f in it:
                if f.name.startswith("stream") and f.name.endswith(".jsonl.gz"):
                    total += f.stat(follow_symlinks=False).st_size
    return total


def stream_off_reason(docs_ok, free, total):
    """Why no stream opens for a window, or None: the documents, the stream floor, the stream cap."""
    if not docs_ok:
        return "documents"
    if free < STREAM_FLOOR:
        return "floor"
    if total >= STREAM_CAP:
        return "cap"
    return None


def new_stream_stats():
    return {"opened": False, "off_reason": None, "files": [], "segments": 0, "frames": 0, "frame_bytes": 0,
            "pongs": 0, "pings": 0, "first_frame_wall_ns": None, "last_frame_wall_ns": None,
            "max_gap_ns": None, "subscribed_wall_ns": None, "stored_bytes": 0, "cut": False}

# ---- the service ---------------------------------------------------------------------------------


def same_service(cmdline_bytes, argv):
    """Equality with the exact argv, field for field, never a substring."""
    fields = cmdline_bytes.split(b"\x00")
    if fields and fields[-1] == b"":
        fields = fields[:-1]
    try:
        decoded = [f.decode("utf-8") for f in fields]
    except UnicodeDecodeError:
        return False
    return decoded == list(argv)


def processes_with(argv):
    found = []
    for pid in sorted((p for p in os.listdir("/proc") if p.isdigit()), key=int):
        try:
            with open("/proc/%s/cmdline" % pid, "rb") as fh:
                cmd = fh.read()
        except OSError:
            continue
        if same_service(cmd, argv):
            found.append(int(pid))
    return found


def read_commit(directory):
    try:
        with open(os.path.join(directory, "commit.txt"), "rb") as fh:
            return fh.read().decode("ascii").strip()
    except OSError:
        return None


def runtime_record(root, event, extra=None):
    with open(os.path.abspath(__file__), "rb") as fh:
        own = sha256_bytes(fh.read())
    rec = {"event": event, "pid": os.getpid(), "wall_ns": time.time_ns(), "mono_ns": time.monotonic_ns(),
           "commit": read_commit(HERE), "file_sha256": own, "argv": list(sys.argv),
           "config": {"root": root, "headers": [["Accept", ACCEPT], ["User-Agent", UA]],
                      "service_argv": list(SERVICE_ARGV), "ws_url": CLOB_WS_URL, "doc_offset": DOC_OFFSET,
                      "stream": [STREAM_OPEN, STREAM_CLOSE], "checkpoint_offsets": list(CHECKPOINT_OFFSETS),
                      "close_offset": CLOSE_OFFSET, "ping_s": PING_S, "gz_stream": GZ_STREAM,
                      "flush_s": FLUSH_S, "max_frame": MAX_FRAME, "max_queue": MAX_QUEUE,
                      "resource_floor": RESOURCE_FLOOR, "stream_floor": STREAM_FLOOR, "stream_cap": STREAM_CAP,
                      "window_stream_max": WINDOW_STREAM_MAX, "write_cap": WRITE_CAP}}
    if extra:
        rec.update(extra)
    append_bytes(os.path.join(root, "runtime.jsonl"), json_line(rec))
    return rec


def acquire_single_instance(root):
    """O_CREAT | O_EXCL; a live sibling, identified by equality with SERVICE_ARGV, wins."""
    pidfile = os.path.join(root, "service.pid")
    while True:
        try:
            fd = os.open(pidfile, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o644)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
            try:
                with open(pidfile, "rb") as fh:
                    other = int(fh.read().decode("ascii").strip() or "0")
            except (OSError, ValueError):
                other = 0
            try:
                with open("/proc/%d/cmdline" % other, "rb") as fh:
                    cmd = fh.read()
            except OSError:
                cmd = b""
            if other != os.getpid() and same_service(cmd, SERVICE_ARGV):
                out("another instance runs as pid %d" % other)
                return None
            out("stale pid file (pid %d) replaced" % other)
            os.unlink(pidfile)
            continue
        data = ("%d\n" % os.getpid()).encode("ascii")
        os.write(fd, data)
        os.close(fd)
        account(len(data))
        return pidfile


async def fetch_documents(T, wdir, slugs, plan):
    """Both documents, from now, every DOC_RETRY_S, until both carry two token ids or T+880; every
    attempt stored verbatim in documents.jsonl."""
    attempts = 0
    path = os.path.join(wdir, "documents.jsonl")
    while True:
        for m in ("m15", "m5"):
            if plan[m]["ids"] is not None:
                continue
            if attempts:
                await asyncio.sleep(DOC_GAP_S)
            res = await asyncio.to_thread(http_get, GAMMA_MARKET_URL.format(slug=slugs[m]))
            attempts += 1
            rec = {k: res.get(k) for k in DOC_KEYS if k not in ("attempt", "pid")}
            rec.update({"slug": slugs[m], "attempt": attempts, "pid": os.getpid()})
            append_bytes(path, json_line(rec))
            if res["status"] == 200 and res["bytes"]:
                try:
                    ids, labels, verbatim = token_ids_of(res["raw"])
                except ValueError:
                    ids, labels, verbatim = None, None, plan[m]["verbatim"]
                plan[m]["verbatim"] = verbatim
                if ids is not None:
                    plan[m]["ids"], plan[m]["labels"] = ids, labels
        if all(plan[m]["ids"] is not None for m in ("m15", "m5")):
            return attempts, time.time_ns()
        if stopping() or time.time() + DOC_RETRY_S > T + DOC_LAST:
            return attempts, None
        if not await sleep_until(time.time() + DOC_RETRY_S):
            return attempts, None


async def checkpoints(T, plan, sched):
    lines, status_counts, skews = [], {}, []
    complete = missed = 0
    for instant, tau in sched["checkpoints"]:
        if stopping():
            ents = [entry(s, T, tau, reason="stopped") for s in specs_of(plan)]
        elif time.time() > instant:
            missed += 1
            ents = [entry(s, T, tau, reason="missed_scheduled_%d" % instant) for s in specs_of(plan)]
        elif not await sleep_until(instant):
            ents = [entry(s, T, tau, reason="stopped") for s in specs_of(plan)]
        else:
            ents = await asyncio.to_thread(fetch_books, T, tau, plan)
        ok, _why = checkpoint_is_complete(ents)
        complete += 1 if ok else 0
        skews.append(skew_of(ents))
        for e in ents:
            key = "null" if e["status"] is None else str(e["status"])
            status_counts[key] = status_counts.get(key, 0) + 1
            lines.append(json_line({k: e.get(k) for k in BOOK_KEYS}))
    return lines, complete, missed, status_counts, skews


async def run_window(T, late, store, asset="btc", root=None):
    """One window, the whole of it; window.json last. `store` carries the stream bytes under root."""
    root = ROOT if root is None else root
    sched = schedule_for(T)
    slugs = {"m15": slug15(T, asset), "m5": slug5(T + 600, asset)}
    plan = {m: {"slug": slugs[m], "ids": None, "labels": None,
                "verbatim": {"clobTokenIds": None, "outcomes": None, "conditionId": None}} for m in slugs}
    out("window %d (%s): documents from %s%s" % (T, utc(T), utc(T + DOC_OFFSET), ", joined late" if late else ""))
    if not await sleep_until(T + DOC_OFFSET):
        return None
    free = guard_resources()
    wdir = os.path.join(root, str(T))
    os.makedirs(wdir, exist_ok=True)
    attempts, ready = await fetch_documents(T, wdir, slugs, plan)
    docs_ok = ready is not None
    stats = new_stream_stats()
    stats["off_reason"] = stream_off_reason(docs_ok, free, store["stream_bytes"])
    task = None
    if stats["off_reason"] is None:
        tokens = plan["m15"]["ids"] + plan["m5"]["ids"]
        task = asyncio.create_task(stream_window(wdir, tokens, max(T + STREAM_OPEN, time.time()),
                                                 T + STREAM_CLOSE, stats))
    try:
        lines, complete, missed, status_counts, skews = await checkpoints(T, plan, sched)
    finally:
        if task is not None:
            try:
                await task
            except GuardError:
                raise
            except Exception as exc:
                stats["off_reason"] = "error: %s" % type(exc).__name__
            store["stream_bytes"] += stats["stored_bytes"]
    if lines:
        write_new(os.path.join(wdir, "books.jsonl.gz"), gzip.compress(b"".join(lines), compresslevel=GZ_LEVEL, mtime=0))
    await sleep_until(sched["close_instant"])
    markets = {}
    for m in ("m15", "m5"):
        mk = {"slug": slugs[m]}
        mk.update({k: plan[m]["verbatim"].get(k) for k in ("clobTokenIds", "outcomes", "conditionId")})
        assert frozenset(mk) == WINDOW_MARKET_KEYS, "window.json market keys"
        markets[m] = mk
    assert frozenset(stats) == STREAM_KEYS, "window.json stream keys"
    wj = {"T": T, "document_instant": sched["document_instant"], "documents_ok": docs_ok,
          "document_attempts": attempts, "documents_ready_wall_ns": ready, "closed_wall_ns": time.time_ns(),
          "checkpoints_complete": complete, "status_counts": status_counts, "skews_ns": skews,
          "missed": missed, "markets": markets, "stream": stats, "joined_late": late, "stopped": stopping(),
          "pid": os.getpid()}
    assert_keys(wj, WINDOW_JSON_KEYS, "window.json")
    write_new(os.path.join(wdir, "window.json"), json_line(wj))
    out("window %d closed: documents %s in %d attempts; checkpoints %d of 7, missed %d; stream %s, %d frames, "
        "%d segments, %d bytes stored%s" % (
            T, docs_ok, attempts, complete, missed, "opened" if stats["opened"] else "off (%s)" % stats["off_reason"],
            stats["frames"], stats["segments"], stats["stored_bytes"], ", stopped" if wj["stopped"] else ""))
    return wj


def request_stop():
    STOP_FLAG.set()
    if STOP_EVENT[0] is not None:
        STOP_EVENT[0].set()


async def serve_main(root=None, asset="btc", windows=None):
    """The service's loop. `windows` bounds the number of windows; None in the service."""
    root = ROOT if root is None else root
    loop = asyncio.get_running_loop()
    STOP_EVENT[0] = asyncio.Event()
    for sig in (signal.SIGTERM, signal.SIGINT):
        loop.add_signal_handler(sig, request_stop)
    try:
        free = guard_resources()
    except FloorStop as exc:
        out("refusing to start: %s" % exc)
        return 1
    os.makedirs(root, exist_ok=True)
    if acquire_single_instance(root) is None:
        return 3
    store = {"stream_bytes": stream_bytes_total(root)}
    rec = runtime_record(root, "start", {"free_bytes": free, "stream_bytes": store["stream_bytes"]})
    out("start record: pid %d commit %s file_sha256 %s; free %d bytes, streams %d bytes" % (
        rec["pid"], rec["commit"], rec["file_sha256"], free, store["stream_bytes"]))
    rc, done = 0, 0
    try:
        while not stopping() and (windows is None or done < windows):
            T, late = next_window(time.time())
            if late and not joinable(os.path.join(root, str(T))):
                out("window %d already closed by an earlier process: not rejoined" % T)
                await sleep_until(T + CLOSE_OFFSET)
                continue
            try:
                await run_window(T, late, store, asset, root)
                done += 1
            except FloorStop as exc:
                rc = 1
                runtime_record(root, "halt", {"T": T, "reason": str(exc)})
                out("halt: %s" % exc)
                break
            except GuardError:
                rc = 1
                raise
            except Exception as exc:
                runtime_record(root, "error", {"T": T, "error": "%s: %s" % (type(exc).__name__, str(exc)[:300])})
                out("window %d error: %r" % (T, exc))
                await sleep_until(T + CLOSE_OFFSET)
    finally:
        runtime_record(root, "stop", {"counters": dict(COUNTERS), "code": rc})
        out("stop record written; requests %d, sessions %d, frames %d, stream bytes %d, other bytes %d" % (
            COUNTERS["requests"], COUNTERS["sessions"], COUNTERS["frames"], COUNTERS["stream_bytes"],
            COUNTERS["bytes_written"]))
    return rc


def mode_serve():
    try:
        with open("/proc/self/cmdline", "rb") as fh:
            mine = fh.read()
    except OSError:
        mine = b""
    if not same_service(mine, SERVICE_ARGV):
        out("refuses to serve: /proc/self/cmdline %r is not %r; nothing written" % (
            mine.decode("utf-8", "replace").replace("\x00", " "), list(SERVICE_ARGV)))
        return 2
    return asyncio.run(serve_main())

# ---- reading what the service stored: total, it never raises on data ------------------------------


def stream_rows(path, report):
    """Every complete line of a stream file, parsed, read incrementally in pieces of at most 4 MiB;
    `report` gets `torn` - cut before its trailer, or with bytes past it - and `bad`, the lines that do
    not parse."""
    d = zlib.decompressobj(16 + zlib.MAX_WBITS)
    buf, torn = b"", False
    with open(path, "rb") as fh:
        pending = b""
        while True:
            if not pending:
                pending = fh.read(1 << 16)
                if not pending:
                    break
            try:
                data = d.decompress(pending, 1 << 22)
            except zlib.error:
                torn = True
                break
            pending = d.unconsumed_tail
            buf += data
            lines = buf.split(b"\n")
            buf = lines.pop()
            for ln in lines:
                try:
                    yield json.loads(ln)
                except ValueError:
                    report["bad"] += 1
            if d.eof:
                if d.unused_data or pending or fh.read(1):
                    torn = True
                break
    if not d.eof or buf:
        torn = True
    report["torn"] = report["torn"] or torn


def counted_quantiles(counter):
    """min, the nearest-rank median, p99 and max of the values a Counter counts, or None where empty."""
    n = sum(counter.values())
    if not n:
        return None
    keys = sorted(counter)
    res, seen = {"n": n, "min": keys[0], "max": keys[-1]}, 0
    marks = {"median": (n - 1) // 2, "p99": (n * 99) // 100}
    for k in keys:
        lo, seen = seen, seen + counter[k]
        for name, idx in marks.items():
            if lo <= idx < seen:
                res[name] = k
    return {k: res[k] for k in ("n", "min", "median", "p99", "max")}


def frame_tokens(obj):
    """The event types and token ids a parsed frame names, and the venue time of a price_change, or
    None where the frame does not conform to the documented market channel."""
    items = obj if isinstance(obj, list) else [obj]
    if not items:
        return None
    types, toks, ts = [], set(), None
    for it in items:
        if not isinstance(it, dict):
            return None
        et = it.get("event_type")
        if et not in KNOWN:
            return None
        if et == "price_change":
            pcs = it.get("price_changes")
            if not isinstance(pcs, list) or not pcs:
                return None
            for pc in pcs:
                if not (isinstance(pc, dict) and isinstance(pc.get("asset_id"), str)):
                    return None
                toks.add(pc["asset_id"])
            t = it.get("timestamp")
            if isinstance(t, str) and t.isascii() and t.isdigit():
                ts = int(t)
        else:
            if not isinstance(it.get("asset_id"), str):
                return None
            toks.add(it["asset_id"])
        types.append(et)
    return types, toks, ts


def stream_unit(T, wdir, wj, tokens15, tokens5):
    """G-STREAM's unit: the reasons a window's stream is not complete, none where it is, and its counts.
    Reads a frame for its JSON shape, event types, token ids and the venue's time, and nothing else."""
    st = wj.get("stream") if isinstance(wj, dict) else None
    if not isinstance(st, dict) or frozenset(st) != STREAM_KEYS:
        return ["window.json"], {}
    why = []
    if not wj.get("documents_ok"):
        why.append("documents")
    if wj.get("joined_late"):
        why.append("joined late")
    if wj.get("stopped"):
        why.append("stopped")
    if not st["opened"] or not st["files"]:
        why.append("no stream (%s)" % st["off_reason"])
        return why, {}
    m15, m5 = set(tokens15), set(tokens5)
    four = m15 | m5
    s = {"files": len(st["files"]), "frames": 0, "pongs": 0, "frames_m15": 0, "frames_m5": 0, "bytes_m15": 0,
         "bytes_m5": 0, "nonconforming": 0, "foreign": 0, "torn": 0, "bad_lines": 0, "stored_bytes": 0,
         "subscribes": 0, "closes": 0, "pings": 0, "max_gap_ns": None, "subscribe_offset_ms": None,
         "last_close_offset_ms": None, "lag_ms": None}
    lags, early, sub0, last, end = {}, set(), None, None, None
    gap = 0
    for name in st["files"]:
        p = os.path.join(wdir, name)
        if not os.path.isfile(p):
            why.append("missing %s" % name)
            continue
        s["stored_bytes"] += os.path.getsize(p)
        rep = {"torn": False, "bad": 0}
        ended = False
        for r in stream_rows(p, rep):
            ended = False
            if not isinstance(r, dict) or type(r.get("recv_ns")) is not int:
                s["bad_lines"] += 1
                continue
            t = r["recv_ns"]
            ev = r.get("event")
            if ev is not None:
                if ev == "subscribe":
                    s["subscribes"] += 1
                    if sub0 is None:
                        sub0 = t
                elif ev == "close":
                    s["closes"] += 1
                    end = t
                elif ev == "ping":
                    s["pings"] += 1
                elif ev == "end":
                    ended = True
                if ev in ("subscribe", "close") and last is not None:
                    gap = max(gap, t - last)
                if ev in ("subscribe", "close") and sub0 is not None:
                    last = t
                continue
            keys = frozenset(r)
            if keys == FRAME_B64_KEYS:
                s["nonconforming"] += 1
            elif keys != FRAME_KEYS or not isinstance(r["raw"], str):
                s["bad_lines"] += 1
                continue
            s["frames"] += 1
            if sub0 is not None:
                if last is not None:
                    gap = max(gap, t - last)
                last = t
            if keys == FRAME_B64_KEYS:
                continue
            raw = r["raw"]
            if raw == "PONG":
                s["pongs"] += 1
                continue
            try:
                obj = json.loads(raw)
            except ValueError:
                s["nonconforming"] += 1
                continue
            got = frame_tokens(obj)
            if got is None:
                s["nonconforming"] += 1
                continue
            types, toks, ts = got
            if not toks <= four:
                s["foreign"] += 1
            n = len(raw.encode("utf-8"))
            if toks <= m15:
                s["frames_m15"] += 1
                s["bytes_m15"] += n
            elif toks <= m5:
                s["frames_m5"] += 1
                s["bytes_m5"] += n
            if ts is not None:
                lag = min(max(t // 1000000 - ts, LAG_RANGE_MS[0]), LAG_RANGE_MS[1])
                lags[lag] = lags.get(lag, 0) + 1
            if "book" in types and sub0 is not None and t <= sub0 + INITIAL_S * 10 ** 9:
                for it in (obj if isinstance(obj, list) else [obj]):
                    if it.get("event_type") == "book":
                        early.add(it["asset_id"])
        s["torn"] += 1 if rep["torn"] else 0
        s["bad_lines"] += rep["bad"]
        if not ended:
            why.append("no end line in %s" % name)
    for k, flag in (("torn", "torn"), ("bad_lines", "bad lines"), ("nonconforming", "nonconforming frames"),
                    ("foreign", "foreign tokens")):
        if s[k]:
            why.append(flag)
    if sub0 is None:
        why.append("no subscribe")
    else:
        s["subscribe_offset_ms"] = (sub0 - T * 10 ** 9) // 1000000
        if sub0 > (T + SUBSCRIBE_BY) * 10 ** 9:
            why.append("late subscribe")
        if not four <= early:
            why.append("initial books")
        s["max_gap_ns"] = gap
        if gap > GAP_MAX_NS:
            why.append("gap")
    if end is None or end < (T + END_BY) * 10 ** 9:
        why.append("short")
    if end is not None:
        s["last_close_offset_ms"] = (end - T * 10 ** 9) // 1000000
    if s["frames"] != st["frames"]:
        why.append("count")
    s["lag_ms"] = counted_quantiles(lags)
    return why, s


def books_of(wdir):
    """The window's stored checkpoint reads grouped by tau', or None where the file is unreadable."""
    p = os.path.join(wdir, "books.jsonl.gz")
    if not os.path.isfile(p):
        return None
    try:
        with gzip.open(p, "rb") as fh:
            text = fh.read().decode("utf-8")
        lines = [json.loads(ln) for ln in text.split("\n") if ln]
    except (OSError, EOFError, ValueError, zlib.error):
        return None
    by = {}
    for ln in lines:
        if isinstance(ln, dict):
            by.setdefault(ln.get("tau_prime"), []).append(ln)
    return by


def read_g_stream(units):
    """units: whether each of the first qualifying windows is complete, in order."""
    if len(units) < GATE_WINDOWS:
        return "UNDECIDABLE"
    return "PASS" if sum(1 for u in units[:GATE_WINDOWS] if u) >= GATE_STREAM_PASS else "FAIL"


def read_g_books(n_checkpoints, n_complete):
    if n_checkpoints < GATE_CHECKPOINTS:
        return "UNDECIDABLE"
    return "PASS" if n_complete >= GATE_BOOKS_PASS else "FAIL"


def read_g_tierc(rows):
    """rows: (fully loaded, counted, quotes_complete) per exposed interval."""
    if any(c and q is not True for _f, c, q in rows):
        return "FAIL"
    if sum(1 for f, c, q in rows if f and c and q is True) >= TIERC_MIN:
        return "PASS"
    return "UNDECIDABLE"


def comb(n, k):
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c


def p_fail_at_least(n, k, p):
    """P(at least k of n independent units fail, each with probability p), exact."""
    return sum(comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(k, n + 1))


def p_false_alarm(f, m, units):
    if m == 0:
        return None
    return 1 - (1 - Fraction(f, m)) ** units


def decimals(fr, places=10):
    if fr is None:
        return None
    scale = 10 ** places
    q, r = divmod(fr.numerator * scale, fr.denominator)
    if 2 * r >= fr.denominator:
        q += 1
    s = str(q).rjust(places + 1, "0")
    return s[:-places] + "." + s[-places:]

# ---- the modes -----------------------------------------------------------------------------------


ROW = re.compile(r"^\| `([^`]+)` \| ([0-9,]+|—) \| ([0-9,]+|—) \| (frozen|tracked|reported) \| "
                 r"`?([0-9a-f]{64}|self-reference[^|]*?)`? \|$", re.M)
ANCHOR_ROW = re.compile(r"^\| `(A[0-9])` — [^|]*\| `([^`]+)` \|$", re.M)


def mode_fingerprint():
    with open(os.path.join(PRIMARY, "SYSTEM-MAP.md"), "rb") as fh:
        raw = fh.read()
    txt = raw.decode("utf-8")
    rev = re.findall(r"^\*\*Revision string:\*\* `([^`]+)`$", txt, re.M)
    assert rev == [MAP_REVISION], "map revision %r, required %s" % (rev, MAP_REVISION)
    found = dict(ANCHOR_ROW.findall(txt))
    assert found == ANCHORS, "anchors %r" % found
    for k, rel in sorted(ANCHOR_FILES.items()):
        h = sha256_file(os.path.join(PRIMARY, rel))[:12]
        assert h == ANCHORS[k], "re-derived %s %s, the map %s" % (k, h, ANCHORS[k])
        out("re-derived %s %s sha256[:12] %s equal" % (k, rel, h))
    rows = ROW.findall(txt)
    states = {k: sum(1 for r in rows if r[3] == k) for k in MAP_ROWS}
    assert states == MAP_ROWS and len(rows) == sum(MAP_ROWS.values()), "rows %r" % states
    for path, lines, nbytes, state, sha in rows:
        with open(os.path.join(PRIMARY, path), "rb") as fh:
            blob = fh.read()
        got = (blob.count(b"\n"), len(blob), sha256_bytes(blob))
        if state == "frozen":
            want = (int(lines.replace(",", "")), int(nbytes.replace(",", "")), sha)
            assert got == want, "frozen row %s: %r, the map %r" % (path, got, want)
        out("%-44s %6d lines %8d bytes %s %s%s" % (path, got[0], got[1], got[2], state,
                                                  " equal" if state == "frozen" else ""))
    out("SYSTEM-MAP.md %d lines %d bytes sha256 %s" % (raw.count(b"\n"), len(raw), sha256_bytes(raw)))
    out("FINGERPRINT PASS: revision %s; anchors 6 of 6, 4 re-derived; rows %d: frozen %d of %d equal, "
        "tracked %d, reported %d" % (MAP_REVISION, len(rows), states["frozen"], MAP_ROWS["frozen"],
                                     states["tracked"], states["reported"]))


def systemctl_show(unit, props):
    args = ["systemctl", "show", unit]
    for prop in props:
        args += ["-p", prop]
    cp = subprocess.run(args, capture_output=True, text=True)
    assert cp.returncode == 0, "systemctl show %s: %s" % (unit, cp.stderr.strip())
    return dict(line.split("=", 1) for line in cp.stdout.split("\n") if "=" in line)


def systemctl_word(verb, unit):
    cp = subprocess.run(["systemctl", verb, unit], capture_output=True, text=True)
    return cp.stdout.strip()


def mode_still():
    st = load_state()
    now = {}
    for key, unit in sorted(UNITS.items()):
        try:
            kv = systemctl_show(unit, ["MainPID", "NRestarts", "ActiveState", "MemoryCurrent", "MemoryPeak"])
        except AssertionError as exc:
            if key == "recorder":
                raise
            out("%s unread: %s" % (unit, exc))
            continue
        now[key] = {k: kv.get(k) for k in ("MainPID", "NRestarts", "ActiveState")}
        out("%s %s, MemoryCurrent %s, MemoryPeak %s" % (unit, now[key], kv.get("MemoryCurrent"), kv.get("MemoryPeak")))
    if "still" not in st:
        st["still"] = {"at": utc(time.time()), "recorder": now["recorder"]}
        save_state(st)
        out("still: the recorder recorded")
        return
    same = now["recorder"] == st["still"]["recorder"]
    out("G-STILL %s: the recorder %s since %s" % ("PASS" if same else "FAIL", "unchanged" if same else "changed",
                                                  st["still"]["at"]))
    assert same, "G-STILL FAIL: the recorder's unit %r, then %r" % (st["still"]["recorder"], now["recorder"])


def mode_mark(name):
    assert name in ("stop-cb", "start-svc", "kill-svc", "restore"), "mark %r" % name
    st = load_state()
    marks = st.setdefault("marks", {})
    assert name not in marks, "mark %s already taken" % name
    unit = UNITS["chainbook"] if name in ("stop-cb", "restore") else UNIT
    kv = systemctl_show(unit, ["MainPID", "NRestarts", "ActiveState"])
    marks[name] = {"ns": time.time_ns(), "unit": unit, "MainPID": kv.get("MainPID"), "NRestarts": kv.get("NRestarts"),
                   "ActiveState": kv.get("ActiveState")}
    save_state(st)
    out("mark %s at %s: %s %r" % (name, utc(marks[name]["ns"] / 1e9), unit, marks[name]))


def read_runtime(path):
    recs = []
    with open(path, "rb") as fh:
        for ln in fh.read().split(b"\n"):
            if ln.strip():
                recs.append(json.loads(ln))
    return recs


def mode_chainbook():
    """G-CB-STOP: the chain book stopped through systemd, disabled, no process left, and its own record
    ending in a stop of the MainPID the mark read, at or after the mark."""
    st = load_state()
    mark = st.get("marks", {}).get("stop-cb")
    assert mark is not None, "chainbook: no stop-cb mark"
    active = systemctl_word("is-active", UNITS["chainbook"])
    enabled = systemctl_word("is-enabled", UNITS["chainbook"])
    procs = processes_with(CHAINBOOK_ARGV)
    recs = read_runtime(CHAINBOOK + "/runtime.jsonl")
    last = recs[-1]
    stop_s = last.get("wall_ns", 0) / 1e9
    phase = int(stop_s) % WINDOW
    out("chain book: is-active %s, is-enabled %s, processes %r; %d runtime records, the last %s of pid %s at %s, "
        "%d s into its window, %s" % (active, enabled, procs, len(recs), last.get("event"), last.get("pid"), utc(stop_s),
                                      phase, "inside its idle stretch" if 5 <= phase < 625 else "inside a window"))
    checks = {"inactive": active in ("inactive", "failed"), "disabled": enabled == "disabled",
              "no process": procs == [],
              "stop record": last.get("event") == "stop" and str(last.get("pid")) == str(mark["MainPID"])
              and last.get("wall_ns", 0) >= mark["ns"]}
    for k, v in checks.items():
        out("G-CB-STOP %-12s %s" % (k, v))
    assert all(checks.values()), "G-CB-STOP FAIL: %r" % checks
    out("G-CB-STOP PASS: stopped at %s, its MainPID %s, the mark at %s" % (utc(stop_s), mark["MainPID"],
                                                                         utc(mark["ns"] / 1e9)))


def mode_restored():
    """After K-26 and B-RESTORE-CB: the pair book stopped through systemd, disabled, no process left, its own
    record ending in a stop; the chain book active, enabled, one process under its argv, and its own record
    ending in a start after the restore mark."""
    st = load_state()
    mark = st.get("marks", {}).get("restore")
    assert mark is not None, "restored: no restore mark"
    pb = read_runtime(ROOT + "/runtime.jsonl")
    cb = read_runtime(CHAINBOOK + "/runtime.jsonl")
    checks = {"pair book inactive": systemctl_word("is-active", UNIT) in ("inactive", "failed"),
              "pair book disabled": systemctl_word("is-enabled", UNIT) == "disabled",
              "pair book no process": processes_with(SERVICE_ARGV) == [],
              "pair book stop record": bool(pb) and pb[-1].get("event") == "stop",
              "chain book active": systemctl_word("is-active", UNITS["chainbook"]) == "active",
              "chain book enabled": systemctl_word("is-enabled", UNITS["chainbook"]) == "enabled",
              "chain book one process": len(processes_with(CHAINBOOK_ARGV)) == 1,
              "chain book start record": bool(cb) and cb[-1].get("event") == "start" and cb[-1].get("wall_ns", 0) >= mark["ns"]
              and [cb[-1].get("pid")] == processes_with(CHAINBOOK_ARGV)}
    for k, v in checks.items():
        out("RESTORED %-24s %s" % (k, v))
    assert all(checks.values()), "RESTORED FAIL: %r" % {k: v for k, v in checks.items() if not v}
    out("RESTORED PASS: the pair book stopped at %s; the chain book started as pid %s at %s" % (
        utc(pb[-1]["wall_ns"] / 1e9), cb[-1]["pid"], utc(cb[-1]["wall_ns"] / 1e9)))


def unit_reads(n_restarts):
    kv = systemctl_show(UNIT, ["ActiveState", "SubState", "UnitFileState", "FragmentPath", "ControlGroup",
                               "MemoryMax", "NRestarts", "MainPID", "MemoryCurrent", "MemoryPeak"])
    pid = int(kv["MainPID"])
    with open("/proc/%d/cmdline" % pid, "rb") as fh:
        cmd = fh.read()
    cwd = os.readlink("/proc/%d/cwd" % pid)
    with open("/proc/%d/cgroup" % pid, encoding="utf-8") as fh:
        cg = fh.read()
    checks = {"active": kv["ActiveState"] == "active" and kv["SubState"] == "running",
              "enabled": kv["UnitFileState"] == "enabled",
              "fragment": kv["FragmentPath"] == "/etc/systemd/system/" + UNIT,
              "control group": kv["ControlGroup"] == "/system.slice/" + UNIT,
              "ceiling": kv["MemoryMax"] == str(MEMORY_MAX),
              "restarts": kv["NRestarts"] == str(n_restarts),
              "argv": same_service(cmd, SERVICE_ARGV), "cwd": cwd == SVC,
              "cgroup": ("/system.slice/" + UNIT) in cg and "/user.slice" not in cg,
              "sole instance": processes_with(SERVICE_ARGV) == [pid]}
    return kv, checks, pid


def svc_blob():
    with open(SERVICE_FILE, "rb") as fh:
        return sha256_bytes(fh.read())


def mode_unit(n):
    kv, checks, pid = unit_reads(n)
    if n == 0:
        st = load_state()
        mark = st.get("marks", {}).get("start-svc")
        assert mark is not None, "unit 0: no start-svc mark"
        starts = [r for r in read_runtime(ROOT + "/runtime.jsonl") if r.get("event") == "start"]
        first = starts[0] if starts else {}
        checks.update({
            "one start": len(starts) == 1, "start pid": first.get("pid") == pid,
            "start after mark": first.get("wall_ns", 0) >= mark["ns"],
            "commit": first.get("commit") == read_commit(SVC) and isinstance(first.get("commit"), str)
            and re.fullmatch(r"[0-9a-f]{40}", first.get("commit") or "") is not None,
            "file": first.get("file_sha256") == svc_blob(),
            "start argv": first.get("argv") == list(SERVICE_ARGV[3:]),
            "headers": first.get("config", {}).get("headers") == [["Accept", ACCEPT], ["User-Agent", UA]]})
        out("G-START: the start record of pid %s at %s, commit %s, file %s" % (
            first.get("pid"), utc(first.get("wall_ns", 0) / 1e9), first.get("commit"), first.get("file_sha256")))
    for k, v in checks.items():
        out("G-UNIT %-16s %s" % (k, v))
    out("%s MainPID %d, NRestarts %s, MemoryMax %s, MemoryCurrent %s, MemoryPeak %s" % (
        UNIT, pid, kv["NRestarts"], kv["MemoryMax"], kv["MemoryCurrent"], kv["MemoryPeak"]))
    assert all(checks.values()), "G-UNIT FAIL: %r" % {k: v for k, v in checks.items() if not v}
    out("G-UNIT PASS at %d restarts%s" % (n, "; G-START PASS" if n == 0 else ""))


def mode_restart():
    """G-RESTART: since the kill mark, the records are a stop of the marked MainPID and a start of
    another, within RESTART_MAX_S, on the same commit and file; G-UNIT at one restart."""
    st = load_state()
    mark = st.get("marks", {}).get("kill-svc")
    assert mark is not None, "restart: no kill-svc mark"
    recs = read_runtime(ROOT + "/runtime.jsonl")
    after = [r for r in recs if r.get("wall_ns", 0) >= mark["ns"]]
    for r in after:
        out("record %s pid %s at %s" % (r.get("event"), r.get("pid"), utc(r["wall_ns"] / 1e9)))
    ok = (len(after) == 2 and after[0].get("event") == "stop" and str(after[0].get("pid")) == str(mark["MainPID"])
          and after[1].get("event") == "start" and after[1].get("pid") != after[0].get("pid")
          and after[1]["wall_ns"] - after[0]["wall_ns"] <= RESTART_MAX_S * 10 ** 9
          and after[1].get("commit") == recs[0].get("commit") and after[1].get("file_sha256") == recs[0].get("file_sha256"))
    assert ok, "G-RESTART FAIL: the records since the mark are %r" % [(r.get("event"), r.get("pid")) for r in after]
    out("G-RESTART: the stop of %s, the start of %s %.3f s later" % (
        after[0]["pid"], after[1]["pid"], (after[1]["wall_ns"] - after[0]["wall_ns"]) / 1e9))
    mode_unit(1)
    out("G-RESTART PASS")


def cgroup_memory(cg):
    vals = {}
    for name in ("memory.current", "memory.peak", "memory.swap.current", "memory.swap.peak"):
        try:
            with open(os.path.join(cg, name), encoding="utf-8") as fh:
                vals[name] = fh.read().strip()
        except OSError as exc:
            vals[name] = "unread: %s" % type(exc).__name__
    try:
        with open(os.path.join(cg, "memory.stat"), encoding="utf-8") as fh:
            stat = dict(ln.split() for ln in fh if ln.strip())
        for k in ("anon", "file", "kernel", "sock", "file_dirty", "file_writeback"):
            vals["stat." + k] = stat.get(k)
    except OSError as exc:
        vals["memory.stat"] = "unread: %s" % type(exc).__name__
    return vals


def process_cpu(pid):
    with open("/proc/%d/stat" % pid, encoding="utf-8") as fh:
        f = fh.read().rsplit(")", 1)[1].split()
    hz = os.sysconf("SC_CLK_TCK")
    with open("/proc/stat", encoding="utf-8") as fh:
        btime = int([ln for ln in fh.read().split("\n") if ln.startswith("btime ")][0].split()[1])
    return Fraction(int(f[11]) + int(f[12]), hz), btime + Fraction(int(f[19]), hz)


def mode_load():
    """G-LOAD: the service's processor time since its process started, at most LOAD_MAX of the elapsed
    wall time; its memory printed."""
    kv = systemctl_show(UNIT, ["MainPID", "ControlGroup", "MemoryCurrent", "MemoryPeak"])
    pid = int(kv["MainPID"])
    cpu, began = process_cpu(pid)
    elapsed = Fraction(time.time_ns(), 10 ** 9) - began
    frac = cpu / elapsed
    for k, v in cgroup_memory("/sys/fs/cgroup" + kv["ControlGroup"]).items():
        out("%s %s" % (k, v))
    with open("/proc/%d/status" % pid, encoding="utf-8") as fh:
        for ln in fh:
            if ln.split(":")[0] in ("VmRSS", "VmHWM", "VmSwap", "Threads"):
                out("process %d %s" % (pid, ln.strip()))
    out("G-LOAD: process %d, processor %s s over %s s since %s: %s of one core, bound %s" % (
        pid, decimals(cpu, 2), decimals(elapsed, 1), utc(began), decimals(frac, 4), decimals(LOAD_MAX, 2)))
    assert frac <= LOAD_MAX, "G-LOAD FAIL: %s of one core, above %s" % (decimals(frac, 4), decimals(LOAD_MAX, 2))
    out("G-LOAD PASS")


def mode_final():
    mode_unit(1)
    mode_still()
    kv = systemctl_show(UNIT, ["MainPID", "ControlGroup"])
    for k, v in cgroup_memory("/sys/fs/cgroup" + kv["ControlGroup"]).items():
        out("%s %s" % (k, v))
    out("FINAL PASS")


def considered(T, s, a):
    return T + JOIN_LAST >= s and T + CLOSE_OFFSET <= a


def qualifies(T, s, a):
    return T + DOC_OFFSET >= s + QUALIFY_LEAD_S and T + CLOSE_OFFSET <= min(a, s + BUDGET_S)


def manifest_of(T0, a):
    """A five-minute interval's manifest as of a: (counted, quotes_complete, complete, Tier C offsets)."""
    p = "%s/btc-updown-5m/%d/manifest.json" % (RECORDER, T0)
    try:
        st = os.stat(p)
    except OSError:
        return False, None, None, []
    if st.st_mtime_ns > a * 10 ** 9:
        return False, None, None, []
    with open(p, "rb") as fh:
        m = json.loads(fh.read())
    offs = [q.get("offset_ms") for q in m.get("quote_offsets_ms", []) if isinstance(q, dict)
            and isinstance(q.get("offset_ms"), (int, float))]
    return True, m.get("quotes_complete"), m.get("complete"), offs


def window_row(t, q, a):
    """One considered window, read: its row, and the unit, the complete checkpoints and the exposed
    interval it contributes where it qualifies."""
    wdir = os.path.join(ROOT, str(t))
    row = {"T": t, "qualifying": q}
    by = books_of(wdir) or {}
    cks = []
    for off in CHECKPOINT_OFFSETS:
        ents = by.get(WINDOW - off, [])
        okc, whyc = checkpoint_is_complete(ents)
        cks.append({"tau_prime": WINDOW - off, "complete": okc, "why": whyc,
                    "statuses": [e.get("status") for e in ents], "skew_ns": skew_of(ents)})
    row["checkpoints"] = cks
    n_ok = sum(1 for c in cks if c["complete"])
    counted, qc, comp, offs = manifest_of(t + 600, a)
    trow = {"E": t + 600, "fully_loaded": False, "counted": counted, "quotes_complete": qc, "complete": comp,
            "offsets_ms": quantiles(offs)}
    wjp = os.path.join(wdir, "window.json")
    if not os.path.isfile(wjp):
        row["why"] = ["no window.json"]
        return row, False, n_ok, trow
    try:
        with open(wjp, "rb") as fh:
            wj = json.loads(fh.read())
    except ValueError:
        wj = None
    if not isinstance(wj, dict):
        row["why"] = ["window.json unreadable"]
        return row, False, n_ok, trow
    mk = wj.get("markets") if isinstance(wj.get("markets"), dict) else {}
    toks = []
    for m in ("m15", "m5"):
        ids = parse_maybe_string((mk.get(m) or {}).get("clobTokenIds"))
        toks.append([str(x) for x in ids] if isinstance(ids, list) else [])
    why, stats = stream_unit(t, wdir, wj, toks[0], toks[1])
    st = wj.get("stream") if isinstance(wj.get("stream"), dict) else {}
    row.update({"why": why, "stream": stats, "checkpoints_complete": wj.get("checkpoints_complete"),
                "missed": wj.get("missed"), "documents_ok": wj.get("documents_ok"),
                "document_attempts": wj.get("document_attempts"), "joined_late": wj.get("joined_late"),
                "stream_opened": st.get("opened"), "stream_off": st.get("off_reason"),
                "stored_bytes_window": sum(os.path.getsize(os.path.join(wdir, n)) for n in sorted(os.listdir(wdir)))})
    trow["fully_loaded"] = (bool(st.get("opened")) and stats.get("subscribe_offset_ms") is not None
                            and stats["subscribe_offset_ms"] <= SUBSCRIBE_BY * 1000 and "short" not in why
                            and all(len(c["statuses"]) == 4 and None not in c["statuses"] for c in cks))
    return row, not why, n_ok, trow


def mode_prove(a):
    floor_check()
    starts = [r for r in read_runtime(ROOT + "/runtime.jsonl") if r.get("event") == "start"]
    assert starts, "prove: no start record"
    s = starts[0]["wall_ns"] / 1e9
    assert s <= a <= time.time(), "prove: as-of %d outside [%s, now]" % (a, s)
    out("the service's first start: pid %s at %s" % (starts[0]["pid"], utc(s)))
    plan, t = [], (int(s) // WINDOW) * WINDOW - WINDOW
    while t + CLOSE_OFFSET <= a:
        if considered(t, s, a):
            plan.append((t, qualifies(t, s, a) and sum(1 for _t, q in plan if q) < GATE_WINDOWS))
        t += WINDOW
    quals = [t for t, q in plan if q]
    counted_now = sum(1 for t in quals if manifest_of(t + 600, a)[0])
    if (len(quals) < GATE_WINDOWS or counted_now < len(quals)) and a < s + BUDGET_S:
        nxt = int(a) + 300
        out("NOT YET: %d of %d qualifying windows closed, %d of %d exposed manifests counted, as of %d; run again "
            "at or after %d (%s)" % (len(quals), GATE_WINDOWS, counted_now, len(quals), a, nxt, utc(nxt)))
        return 3
    windows, units, ckpts, ckpt_ok, tierc = [], [], 0, 0, []
    for t, q in plan:
        row, unit, n_ok, trow = window_row(t, q, a)
        windows.append(row)
        if q:
            units.append(unit)
            ckpts += len(CHECKPOINT_OFFSETS)
            ckpt_ok += n_ok
            tierc.append(trow)
    g_stream = read_g_stream(units)
    g_books = read_g_books(ckpts, ckpt_ok)
    g_tierc = read_g_tierc([(r["fully_loaded"], r["counted"], r["quotes_complete"]) for r in tierc])
    exposed = {r["E"] for r in tierc}
    control = []
    T0 = (int(s) // 300 + 1) * 300
    while T0 + 330 <= a and T0 <= s + BUDGET_S:
        if T0 not in exposed and T0 % WINDOW != 600:
            counted, qc, comp, offs = manifest_of(T0, a)
            if counted:
                control.append({"T0": T0, "quotes_complete": qc, "complete": comp, "offsets_ms": quantiles(offs)})
        T0 += 300
    for row in windows:
        out("window %d %s qualifying %s: %s; stream %s" % (row["T"], utc(row["T"]), row["qualifying"],
                                                           "complete" if not row.get("why") else row["why"],
                                                           json.dumps(row.get("stream"), sort_keys=True)))
        for c in row.get("checkpoints", []):
            out("  checkpoint tau' %3d: %s %s statuses %s skew_ns %s" % (c["tau_prime"], c["complete"], c["why"],
                                                                      c["statuses"], c["skew_ns"]))
    for r in tierc:
        out("exposed %d %s: fully loaded %s, counted %s, quotes_complete %s, complete %s, Tier C offsets %s" % (
            r["E"], utc(r["E"]), r["fully_loaded"], r["counted"], r["quotes_complete"], r["complete"], r["offsets_ms"]))
    for r in control:
        out("control %d %s: quotes_complete %s, complete %s, Tier C offsets %s" % (
            r["T0"], utc(r["T0"]), r["quotes_complete"], r["complete"], r["offsets_ms"]))
    proof = {"mode": "prove", "as_of": a, "start": {"pid": starts[0]["pid"], "wall_ns": starts[0]["wall_ns"],
                                                    "commit": starts[0].get("commit"),
                                                    "file_sha256": starts[0].get("file_sha256")},
             "windows": windows, "g_stream": {"units": units, "reading": g_stream},
             "g_books": {"checkpoints": ckpts, "complete": ckpt_ok, "reading": g_books},
             "g_tierc": {"rows": tierc, "reading": g_tierc}, "control": control,
             "counters": {"requests": COUNTERS["requests"], "sessions": COUNTERS["sessions"]}}
    assert_keys(proof, PROOF_JSON_KEYS, "proof.json")
    assert COUNTERS["requests"] == 0 and COUNTERS["sessions"] == 0, "prove made a request"
    os.makedirs(os.path.join(WORK, "proof"), exist_ok=True)
    path = os.path.join(WORK, "proof", "proof-%d.json" % a)
    body = json_line(proof)
    if os.path.exists(path):
        assert sha256_file(path) == sha256_bytes(body), "prove: %s differs from the first run" % path
        out("unchanged %s sha256 %s" % (path, sha256_bytes(body)))
    else:
        with open(path, "xb") as fh:
            fh.write(body)
        out("wrote %s sha256 %s, %d bytes" % (path, sha256_bytes(body), len(body)))
    out("READING G-STREAM: %s, %d of %d complete" % (g_stream, sum(1 for u in units if u), len(units)))
    out("READING G-BOOKS: %s, %d of %d checkpoints complete" % (g_books, ckpt_ok, ckpts))
    out("READING G-TIERC: %s, %d counted fully loaded exposed intervals with quotes_complete true" % (
        g_tierc, sum(1 for r in tierc if r["fully_loaded"] and r["counted"] and r["quotes_complete"] is True)))
    return 0


def base_rate(p, span_s=BASE_RATE_S, step=300):
    """The T0 of every five-minute interval closing in [p - span_s, p)."""
    return list(range(p - span_s - step, p - step, step))


async def prestart_session(wdir, tokens, seconds):
    stats = new_stream_stats()
    STOP_FLAG.clear()
    t0 = time.time()
    await stream_window(wdir, tokens, t0, t0 + seconds, stats)
    return stats


def mode_prestart():
    """CANON hard rule 14's proof, on the ETH nested pair: two documents and one book through http_get, one
    stream session through stream_window; the processes; G-TIERC's base rate. Prints counts only."""
    floor_check()
    with open(os.path.abspath(__file__), "rb") as fh:
        own = sha256_bytes(fh.read())
    out("file %s sha256 %s" % (os.path.abspath(__file__), own))
    proxies = sorted(k for k in os.environ if k.lower() in ("http_proxy", "https_proxy", "all_proxy"))
    out("free %d bytes at %s; proxy variables in the environment: %d" % (free_bytes(), DISK_PATH, len(proxies)))
    procs = {"service": processes_with(SERVICE_ARGV), "chainbook": processes_with(CHAINBOOK_ARGV)}
    out("processes: the service's argv %r, the chain book's %r" % (procs["service"], procs["chainbook"]))
    assert procs["service"] == [], "prestart: an instance of the service already runs"
    p = int(time.time()) // 300 * 300
    slots = base_rate(p)
    m = f = 0
    t_scan = time.monotonic()
    for k, T0 in enumerate(slots):
        if k == 100:
            assert time.monotonic() - t_scan <= 30, "prestart: the base-rate scan's first 100 slots took over 30 s"
        try:
            with open("%s/btc-updown-5m/%d/manifest.json" % (RECORDER, T0), "rb") as fh:
                mm = json.loads(fh.read())
        except OSError:
            continue
        m += 1
        f += 0 if mm.get("quotes_complete") is True else 1
    fa = p_false_alarm(f, m, FA_UNITS)
    out("base rate: %d slots, %d manifests read, %d without quotes_complete true; G-TIERC's false alarm "
        "1 - (1 - f/m)^4 = %s = %s" % (len(slots), m, f, fa, decimals(fa)))
    now = time.time()
    T = int(now) // WINDOW * WINDOW
    if now > T + 840:
        T += WINDOW
    slugs = {"m15": slug15(T, "eth"), "m5": slug5(T + 600, "eth")}
    reqs, toks = [], {}
    for k in ("m15", "m5"):
        res = http_get(GAMMA_MARKET_URL.format(slug=slugs[k]))
        ids = None
        if res["status"] == 200:
            try:
                ids = token_ids_of(res["raw"])[0]
            except ValueError:
                ids = None
        assert res["status"] == 200 and res["bytes"] > 0 and ids is not None, \
            "prestart: %s %s, %d bytes" % (slugs[k], res["status"], res["bytes"])
        toks[k] = ids
        reqs.append({"method": "GET", "url": res["url"], "headers": [["Accept", ACCEPT], ["User-Agent", UA]],
                     "status": res["status"], "bytes": res["bytes"], "sha256": res["sha256"], "parses_json": True,
                     "elapsed_ns": res["recv_mono_ns"] - res["send_mono_ns"], "token_ids": ids})
        time.sleep(DOC_GAP_S)
    res = http_get(CLOB_BOOK_URL.format(token_id=toks["m15"][0]))
    try:
        json.loads(res["raw"])
        pj = True
    except ValueError:
        pj = False
    assert res["status"] == 200 and res["bytes"] > 0 and pj, "prestart: the book %s, %d bytes" % (res["status"], res["bytes"])
    reqs.append({"method": "GET", "url": res["url"], "headers": [["Accept", ACCEPT], ["User-Agent", UA]],
                 "status": res["status"], "bytes": res["bytes"], "sha256": res["sha256"], "parses_json": pj,
                 "elapsed_ns": res["recv_mono_ns"] - res["send_mono_ns"]})
    assert COUNTERS["requests"] == 3, "prestart: %d requests" % COUNTERS["requests"]
    for name in ("prestart", "prestart-2"):
        d = os.path.join(WORK, name)
        if not os.path.exists(d):
            break
    else:
        raise AssertionError("prestart: prestart and prestart-2 both exist")
    os.makedirs(d)
    tokens = toks["m15"] + toks["m5"]
    stats = asyncio.run(prestart_session(d, tokens, 25))
    wj = {"documents_ok": True, "joined_late": False, "stopped": False, "stream": stats}
    why, sst = stream_unit(T, d, wj, toks["m15"], toks["m5"])
    path = os.path.join(d, "stream.jsonl.gz")
    rep = {"torn": False, "bad": 0}
    opens = [r for r in stream_rows(path, rep) if isinstance(r, dict) and r.get("event") == "open"]
    checks = {"one session": stats["segments"] == 1 and COUNTERS["sessions"] == 1,
              "101": len(opens) == 1 and opens[0].get("status") == 101 and opens[0].get("extensions") is None,
              "subscribed": stats["subscribed_wall_ns"] is not None,
              "initial books": "initial books" not in why,
              "heartbeat": stats["pongs"] >= 1 and stats["pings"] >= 2,
              "conforming": not ({"nonconforming frames", "foreign tokens", "bad lines", "torn", "count"} & set(why)),
              "whole file": not rep["torn"] and rep["bad"] == 0 and "no end line in stream.jsonl.gz" not in why}
    for k, v in checks.items():
        out("P-START %-14s %s" % (k, v))
    out("the session: %d frames, %d frame bytes, %d pongs, %d pings, %d stored bytes, largest gap %s ns, "
        "frames m15 %s m5 %s" % (stats["frames"], stats["frame_bytes"], stats["pongs"], stats["pings"],
                                 stats["stored_bytes"], sst.get("max_gap_ns"), sst.get("frames_m15"), sst.get("frames_m5")))
    doc = {"mode": "prestart", "p_wall": p, "file_sha256": own, "processes": procs, "proxy_variables": len(proxies),
           "base_rate": {"slots": len(slots), "manifests": m, "f": f, "false_alarm": str(fa) if fa is not None else None,
                         "false_alarm_decimal": decimals(fa)},
           "requests": reqs, "stream": {"slugs": slugs, "tokens": tokens, "stats": stats, "checks": checks,
                                        "frames_m15": sst.get("frames_m15"), "frames_m5": sst.get("frames_m5")},
           "counters": {"requests": COUNTERS["requests"], "sessions": COUNTERS["sessions"]}}
    assert_keys(doc, PRESTART_JSON_KEYS, "prestart.json")
    body = json_line(doc)
    with open(os.path.join(d, "prestart.json"), "xb") as fh:
        fh.write(body)
    out("wrote %s sha256 %s" % (os.path.join(d, "prestart.json"), sha256_bytes(body)))
    out("wrote %s sha256 %s, %d bytes" % (path, sha256_file(path), os.path.getsize(path)))
    assert all(checks.values()), "P-START FAIL: %r" % {k: v for k, v in checks.items() if not v}
    out("READING P-START: served")


def proc_start_times():
    with open("/proc/stat", encoding="utf-8") as fh:
        btime = int([ln for ln in fh.read().split("\n") if ln.startswith("btime ")][0].split()[1])
    hz = os.sysconf("SC_CLK_TCK")
    found = []
    for pid in sorted((p for p in os.listdir("/proc") if p.isdigit()), key=int):
        try:
            with open("/proc/%s/cmdline" % pid, "rb") as fh:
                argv = fh.read().split(b"\0")
            with open("/proc/%s/stat" % pid, encoding="utf-8") as fh:
                fields = fh.read().rsplit(")", 1)[1].split()
        except OSError:
            continue
        a0 = argv[0].decode("utf-8", "replace") if argv else ""
        if a0 == "claude" or a0.endswith("/claude.exe"):
            found.append((int(pid), btime + int(fields[19]) / hz, a0))
    return found


def birth(path):
    cp = subprocess.run(["stat", "-c", "%W", path], capture_output=True, text=True)
    assert cp.returncode == 0, cp.stderr
    return int(cp.stdout.strip())


def mode_scratch(own):
    parent = os.path.dirname(own)
    procs = proc_start_times()
    for pid, t, a0 in procs:
        out("running %d started %s %s" % (pid, utc(t), a0))
    for name in sorted(os.listdir(parent)):
        path = os.path.join(parent, name)
        if path == own or not UUID.fullmatch(name) or not os.path.isdir(path):
            continue
        b = birth(path)
        owner = [pid for pid, t, _a in procs if t - 1 <= b <= t + LIVE_S]
        out("%s born %s: %s" % (name, utc(b), ("live, process %s" % owner) if owner else "earlier"))


def report_tokens():
    tokens = set()
    for name in sorted(os.listdir(REPORTS)):
        if name.endswith(".md"):
            with open(os.path.join(REPORTS, name), encoding="utf-8", errors="replace") as fh:
                tokens.update(TOKEN.findall(fh.read()))
    return tokens


def by_name(tree, rel):
    """Kept whatever a report prints: the state, the logs, the request-path proof and the proofs."""
    return tree == WORK and (rel == "state.json" or rel.startswith("logs/") or rel.startswith("prestart")
                             or rel.startswith("proof/"))


def pristine(tree):
    cp = subprocess.run(["git", "-C", tree, "status", "--porcelain", "--ignored"], capture_output=True, text=True)
    assert cp.returncode == 0 and cp.stdout == "", "reclaim: %s holds %r" % (tree, cp.stdout[:400])
    head = subprocess.run(["git", "-C", tree, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    up = subprocess.run(["git", "-C", tree, "rev-parse", "@{u}"], capture_output=True, text=True)
    assert up.returncode == 0 and up.stdout.strip() == head, \
        "reclaim: %s is at %s, its upstream at %r" % (tree, head, up.stdout.strip())
    out("reclaim: %s skipped: no file but its HEAD's, and HEAD %s is its upstream's" % (tree, head))


def reclaimable(tree):
    if tree == WORK:
        return True
    return (tree.startswith("/tmp/") and os.path.isdir(tree) and not os.path.islink(tree)
            and UUID.fullmatch(os.path.basename(tree)) is not None
            and "btc-5m-twap" in os.path.basename(os.path.dirname(tree)))


def mode_reclaim(trees):
    assert trees and all(reclaimable(t) for t in trees), "reclaim: %r" % (trees,)
    procs = proc_start_times()
    for t in trees:
        if t != WORK:
            b = birth(t)
            assert not [p for p, s, _a in procs if s - 1 <= b <= s + LIVE_S], "reclaim: %s belongs to a running process" % t
    tokens = report_tokens()
    lengths = sorted({len(t) for t in tokens})
    before = sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    out("reclaim: %d report tokens; forensic store holds %d files" % (len(tokens), before))
    considered_n = named = kept = copied = held = 0
    for tree in trees:
        if tree == WORK and os.path.isdir(WT):
            pristine(WT)
        for dirpath, dirnames, filenames in os.walk(tree):
            dirnames[:] = sorted(d for d in dirnames if os.path.join(dirpath, d) != WT)
            for name in sorted(filenames):
                path = os.path.join(dirpath, name)
                if os.path.islink(path) or not os.path.isfile(path):
                    continue
                considered_n += 1
                rel = os.path.relpath(path, tree)
                h = sha256_file(path)
                is_named = any(h[:k] in tokens for k in lengths)
                is_kept = by_name(tree, rel)
                if not (is_named or is_kept):
                    continue
                named += 1 if is_named else 0
                kept += 1 if is_kept and not is_named else 0
                dest = os.path.join(FORENSICS, os.path.basename(tree) + "--" + rel.replace("/", "--"))
                if os.path.exists(dest):
                    got = sha256_file(dest)
                    assert got == h, "reclaim: %s exists with sha256 %s, source %s" % (dest, got, h)
                    held += 1
                    out("R held   %s %s" % (h, dest))
                    continue
                with open(path, "rb") as src, open(dest, "xb") as dst:
                    shutil.copyfileobj(src, dst, 1 << 20)
                assert sha256_file(dest) == h, "reclaim: %s did not copy whole" % dest
                copied += 1
                out("R copied %s %s" % (h, dest))
    after = sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    assert after == before + copied, "reclaim: store %d, expected %d" % (after, before + copied)
    out("RECLAIM PASS: %d files considered, %d named by a report, %d kept by name, %d copied, %d already held; "
        "forensic store %d -> %d files" % (considered_n, named, kept, copied, held, before, after))

# ---- the self-test: literals and loopback servers only -------------------------------------------


class _Http(http.server.BaseHTTPRequestHandler):
    seen = []

    def do_GET(self):
        _Http.seen.append((self.requestline, sorted((k.lower(), v) for k, v in self.headers.items())))
        body, code = (b"error code: 1010\n", 403) if self.path.startswith("/refused") else (b"{}", 200)
        self.send_response(code)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *a):
        pass


def synth_book(tok, cond):
    return {"event_type": "book", "asset_id": tok, "market": cond, "timestamp": "1791000000000", "hash": "ab" * 20,
            "bids": [{"price": "0.48", "size": "10"}], "asks": [{"price": "0.52", "size": "10"}]}


def synth_change(toks, cond, ms):
    return {"event_type": "price_change", "market": cond, "timestamp": str(ms),
            "price_changes": [{"asset_id": t, "price": "0.5", "size": "1", "side": "BUY", "hash": "cd" * 20,
                               "best_bid": "0.49", "best_ask": "0.51"} for t in toks]}


async def loopback_venue(state, close_first_after=None):
    """A venue on 127.0.0.1: the subscription read, the four books sent as one list frame, a price change
    every 5 ms, one in seven for the second market; PONG to PING; the first connection closed by the
    venue after `close_first_after` seconds."""
    conds = {"m15": "0x" + "1" * 64, "m5": "0x" + "2" * 64}

    async def handler(ws):
        state["connections"] += 1
        k = state["connections"]
        state["headers"].append(sorted((n.lower(), v) for n, v in ws.request.headers.raw_items()))
        msg = await ws.recv()
        state["subs"].append(msg)
        toks = json.loads(msg)["assets_ids"]
        await ws.send(json.dumps([synth_book(t, conds["m15"] if i < 2 else conds["m5"]) for i, t in enumerate(toks)]))

        async def sender():
            n = 0
            while True:
                await asyncio.sleep(0.005)
                n += 1
                if n % 7 == 0:
                    await ws.send(json.dumps(synth_change(toks[2:], conds["m5"], 1791000000000 + n)))
                else:
                    await ws.send(json.dumps(synth_change(toks[:2], conds["m15"], 1791000000000 + n)))

        task = asyncio.create_task(sender())
        closer = None
        try:
            if close_first_after is not None and k == 1:
                async def close_later():
                    await asyncio.sleep(close_first_after)
                    await ws.close(code=1011, reason="test")
                closer = asyncio.create_task(close_later())
            async for m in ws:
                if m == "PING":
                    state["pings"] += 1
                    await ws.send("PONG")
        except websockets.ConnectionClosed:
            pass
        finally:
            task.cancel()
            if closer is not None:
                closer.cancel()

    return await ws_serve(handler, "127.0.0.1", 0, compression=None)


def mode_selftest():
    n = [0]

    def ok(cond, what):
        assert cond, "selftest: " + what
        n[0] += 1
        out("  ok  " + what)

    # the schedule, against integers computed outside this file
    T = 1791627300
    sch = schedule_for(T)
    ok(sch["document_instant"] == 1791627845 and sch["stream_open"] == 1791627895
       and sch["stream_close"] == 1791628205 and sch["close_instant"] == 1791628210,
       "documents at T+545, the stream T+595 to T+905, window.json at T+910")
    ok([c for c, _t in sch["checkpoints"]] == [1791627955, 1791628015, 1791628075, 1791628105, 1791628135,
                                               1791628165, 1791628185]
       and [t for _c, t in sch["checkpoints"]] == [245, 185, 125, 95, 65, 35, 15],
       "the chain book's seven checkpoints, tau' 245 to 15")
    ok(tierc_instants(T) == [1791627960, 1791628020, 1791628080, 1791628110, 1791628140, 1791628170, 1791628190]
       and not set(tierc_instants(T)) & {c for c, _t in sch["checkpoints"]},
       "Tier C reads the same five-minute market 5 s after each checkpoint, never in its second")
    ok(sch["stream_open"] < T + 600 and sch["stream_close"] > T + 900 and sch["document_instant"] < T + 605,
       "the stream covers the five-minute market's whole window; the documents precede the recorder's S6 at T+605")
    ok(next_window(T + 10) == (T, False) and next_window(T + 545) == (T, False) and next_window(T + 546) == (T, True)
       and next_window(T + 880) == (T, True) and next_window(T + 881) == (T + 900, False)
       and next_window(T + 910) == (T + 900, False) and next_window(T + 899.5) == (T + 900, False),
       "next_window: scheduled to T+545, joined late to T+880, then the next window")
    ok(stream_off_reason(False, 10 ** 10, 0) == "documents" and stream_off_reason(True, STREAM_FLOOR - 1, 0) == "floor"
       and stream_off_reason(True, STREAM_FLOOR, STREAM_CAP) == "cap"
       and stream_off_reason(True, STREAM_FLOOR, STREAM_CAP - 1) is None,
       "the stream opens only with both documents, free at or above the floor, the store below the cap")
    # equality, never a substring
    good = ("\x00".join(SERVICE_ARGV) + "\x00").encode()
    ok(same_service(good, SERVICE_ARGV), "same_service: the exact argv")
    ok(not same_service(("bash\x00-c\x00" + " ".join(SERVICE_ARGV) + "\x00").encode(), SERVICE_ARGV),
       "same_service: a shell carrying the argv as text is not the service")
    ok(not same_service(good + b"--x\x00", SERVICE_ARGV) and not same_service(b"", SERVICE_ARGV),
       "same_service: a sixth field, and nothing, are not the service")
    # the audit policy, as a pure function, and the hook itself
    man = RECORDER + "/btc-updown-5m/1791628200/manifest.json"
    ok(policy("serve", "open", (ROOT + "/1791627300/stream.jsonl.gz", "xb", 0)) is None,
       "serve writes under the pair book's root")
    ok(policy("serve", "open", (WORK + "/x", "wb", 0)) is not None and policy("serve", "open", ("/tmp/x", "wb", 0)) is not None,
       "serve writes nowhere else")
    ok(policy("serve", "subprocess.Popen", ("systemctl",)) is not None and policy("serve", "os.fork", ()) is not None
       and policy("unit", "subprocess.Popen", ("systemctl",)) is None,
       "serve starts no process; the systemd reads may")
    ok(policy("prove", "open", (man, "rb", 0)) is None and policy("prestart", "open", (man, "rb", 0)) is None
       and policy("prove", "open", (man.replace("manifest.json", "quotes.jsonl.gz"), "rb", 0)) is not None
       and policy("prove", "open", (RECORDER + "/runtime.jsonl", "rb", 0)) is not None
       and policy("serve", "open", (man, "rb", 0)) is not None,
       "under the recorder's root only a manifest, read only, by prestart and prove")
    ok(policy("prove", "open", (man, "r+b", 0)) is not None and policy("prove", "os.scandir", (RECORDER + "/btc-updown-5m",)) is not None,
       "no manifest is opened for writing, and the recorder's root is never listed")
    ok(policy("chainbook", "open", (CHAINBOOK + "/runtime.jsonl", "rb", 0)) is None
       and policy("chainbook", "open", (CHAINBOOK + "/1791627300/window.json", "rb", 0)) is not None
       and policy("chainbook", "os.listdir", (CHAINBOOK,)) is not None
       and policy("prove", "open", (CHAINBOOK + "/runtime.jsonl", "rb", 0)) is not None,
       "under the chain book's root only its runtime.jsonl, by chainbook; nothing listed")
    ok(policy("prove", "open", (ROOT + "/1791627300/window.json", "rb", 0)) is None
       and policy("prove", "open", (ROOT + "/1791627300/window.json", "wb", 0)) is not None
       and policy("prestart", "open", (ROOT + "/runtime.jsonl", "rb", 0)) is not None,
       "the pair book's root is written by serve alone and read by the modes that judge it")
    ok(policy("reclaim", "open", (FORENSICS + "/x", "xb", 0)) is None
       and policy("reclaim", "open", (FORENSICS + "/x", "wb", 0)) is not None,
       "the forensic store takes new files by exclusive create alone")
    MODE[0] = "selftest"
    for p in (RECORDER + "/runtime.jsonl", CHAINBOOK + "/runtime.jsonl", ROOT + "/runtime.jsonl"):
        try:
            open(p, "rb")
            refused = False
        except GuardError:
            refused = True
        except OSError:
            refused = False
        ok(refused and REFUSED[-1][1] == p, "the hook refuses %s before it is opened" % p)
    REFUSED.clear()
    # the request, on a loopback listener, with every proxy variable removed from this process
    removed = [k for k in list(os.environ) if k.lower() in ("http_proxy", "https_proxy", "all_proxy", "no_proxy")]
    for k in removed:
        del os.environ[k]
    out("  proxy variables removed: %d" % len(removed))
    req = build_request("http" + ":" + "//example.invalid/")
    ok(req.get_method() == "GET" and sorted((k.lower(), v) for k, v in req.header_items()) ==
       [("accept", "application/json"), ("user-agent", UA)], "build_request: GET, Accept and this file's User-Agent")
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), _Http)
    th = threading.Thread(target=srv.serve_forever, daemon=True)
    th.start()
    port = srv.server_address[1]
    base = "http" + ":" + "//127.0.0.1:%d" % port
    before = COUNTERS["requests"]
    r = http_get(base + "/book?token_id=1")
    line, hdrs = _Http.seen[-1]
    ok(line.startswith("GET /book?token_id=1 ") and hdrs == sorted([
        ("accept", "application/json"), ("accept-encoding", "identity"), ("connection", "close"),
        ("host", "127.0.0.1:%d" % port), ("user-agent", UA)]), "the wire: exactly five header fields")
    ok(r["status"] == 200 and r["bytes"] == 2 and r["sha256"] == "44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a"
       and r["recv_mono_ns"] >= r["send_mono_ns"], "http_get records 200, 2 bytes, the body's SHA-256 and both stamps")
    r = http_get(base + "/refused")
    ok(r["status"] == 403 and r["bytes"] == 17 and r["reason"] == "http_error" and r["recv_wall_ns"] is not None,
       "a refusal is a stored reply with its status")
    srv.shutdown()
    srv.server_close()
    r = http_get(base + "/closed")
    ok(r["status"] is None and r["bytes"] == 0 and r["recv_mono_ns"] is None and r["recv_wall_ns"] is None,
       "no reply: no status and no receive stamp")
    ok(COUNTERS["requests"] - before == 3, "three loopback requests counted")
    ok(skew_of([{"recv_mono_ns": None}, {"recv_mono_ns": 7}, {"recv_mono_ns": 12}]) == 5, "skew over the replies that came")
    four = [{"status": 200, "bytes": 2, "raw": "{}", "recv_mono_ns": 10 ** 9 + i} for i in range(4)]
    ok(checkpoint_is_complete(four) == (True, "complete") and checkpoint_is_complete(four[:3])[0] is False
       and checkpoint_is_complete(four[:3] + [dict(four[3], recv_mono_ns=2 * 10 ** 9 + 1)])[1] == "skew_above_bound",
       "a checkpoint: four replies within one second")
    ok(token_ids_of('{"clobTokenIds": "[\\"11\\", \\"22\\"]", "outcomes": "[\\"Up\\", \\"Down\\"]", "conditionId": "0xab"}')[:2]
       == (["11", "22"], ["Up", "Down"]) and token_ids_of('{"clobTokenIds": "[\\"11\\"]"}')[0] is None
       and token_ids_of("[]")[0] is None, "token_ids_of: two distinct ids from the JSON-in-JSON fields, or none")
    tmp = os.path.join(WORK, "selftest-tmp")
    shutil.rmtree(tmp, ignore_errors=True)
    os.makedirs(tmp)
    try:
        toks = ["101", "102", "103", "104"]

        async def run_stream(close_first_after, seconds, stop_after=None):
            state = {"connections": 0, "headers": [], "subs": [], "pings": 0}
            server = await loopback_venue(state, close_first_after)
            port_ = server.sockets[0].getsockname()[1]
            url = "ws" + ":" + "//127.0.0.1:%d/ws/market" % port_
            stats = new_stream_stats()
            t0 = time.time()
            STOP_FLAG.clear()
            if stop_after is not None:
                asyncio.get_running_loop().call_later(stop_after, STOP_FLAG.set)
            await stream_window(tmp, toks, t0, t0 + seconds, stats, url=url, ping_s=0.2,
                                kw=connect_kwargs(proxy=None), backoff=(0.1,))
            server.close()
            await server.wait_closed()
            return state, stats

        state, stats = asyncio.run(run_stream(0.6, 1.6))
        ok(state["connections"] == 2 and stats["segments"] == 2, "a close by the venue, then one reconnect")
        ok(all(x == subscription(toks) for x in state["subs"])
           and state["subs"][0] == '{"assets_ids":["101","102","103","104"],"type":"market"}',
           "the subscription: the documented frame, compact")
        ok(sorted(k for k, _v in state["headers"][0]) == ["connection", "host", "sec-websocket-key",
                                                          "sec-websocket-version", "upgrade", "user-agent"]
           and dict(state["headers"][0])["user-agent"] == UA,
           "the handshake: six header fields, this file's User-Agent, no extension offered")
        ok(stats["pings"] >= 4 and stats["pongs"] >= 2 and state["pings"] >= stats["pongs"],
           "the heartbeat: PING on its period, PONG stored")
        path = os.path.join(tmp, stats["files"][0])
        rep = {"torn": False, "bad": 0}
        rows = list(stream_rows(path, rep))
        evs = [r["event"] for r in rows if "event" in r]
        ok(not rep["torn"] and rep["bad"] == 0 and evs[:3] == ["connect", "open", "subscribe"] and evs[-1] == "end"
           and evs.count("close") == 2 and evs.count("connect") == 2,
           "the file: connect, open, subscribe, frames, close, the same again, end")
        closes = [r for r in rows if r.get("event") == "close"]
        ok(closes[0]["reason"] == "closed" and closes[0]["code"] == 1011 and closes[1]["reason"] == "end",
           "the venue's close is recorded with its code, the window's end as end")
        fr = [r for r in rows if "raw" in r]
        ok(len(fr) == stats["frames"] and all(frozenset(r) == FRAME_KEYS for r in fr)
           and fr[0]["raw"].startswith('[{"event_type": "book"'),
           "every frame a line of recv_ns, mono_ns and the frame verbatim; the first the four books")
        wj = {"documents_ok": True, "joined_late": False, "stopped": False, "stream": stats}
        T_ok = (min(r["recv_ns"] for r in rows) // 10 ** 9) // WINDOW * WINDOW
        why, sst = stream_unit(T_ok, tmp, wj, toks[:2], toks[2:])
        ok(sst["frames"] == stats["frames"] and sst["nonconforming"] == 0 and sst["foreign"] == 0
           and sst["frames_m15"] > sst["frames_m5"] > 0 and sst["subscribes"] == 2 and "initial books" not in why
           and "count" not in why, "the unit reads the stream back: every frame conforms, both markets, both sessions")
        ok("short" in why, "a stream that ends before its window's T+900 reads short")
        os.remove(path)
        t1 = time.time()
        state, stats = asyncio.run(run_stream(None, 30, stop_after=0.5))
        STOP_FLAG.clear()
        rep = {"torn": False, "bad": 0}
        rows = list(stream_rows(os.path.join(tmp, stats["files"][0]), rep))
        ok(time.time() - t1 < 5 and not rep["torn"] and rows[-1]["event"] == "end"
           and [r for r in rows if r.get("event") == "close"][0]["reason"] == "stop",
           "a stop closes the session at once and the file whole")
        os.remove(os.path.join(tmp, stats["files"][0]))
        # the writer: a sync flush makes a cut file readable to its last flush; the window maximum cuts
        p = os.path.join(tmp, "w.jsonl.gz")
        w = StreamWriter(p, flush_s=3600)
        for k in range(50):
            w.frame('{"k": %d}' % k)
        w.flush()
        with open(p, "rb") as fh:
            partial = fh.read()
        for k in range(50, 60):
            w.frame('{"k": %d}' % k)
        w.close()
        q = os.path.join(tmp, "torn.jsonl.gz")
        with open(q, "wb") as fh:
            fh.write(partial)
        rep = {"torn": False, "bad": 0}
        rows = list(stream_rows(q, rep))
        ok(rep["torn"] and len(rows) == 50 and rows[-1]["raw"] == '{"k": 49}', "a file cut after a sync flush reads to it, torn")
        rep = {"torn": False, "bad": 0}
        rows = list(stream_rows(p, rep))
        ok(not rep["torn"] and len(rows) == 61 and rows[-1]["event"] == "end" and rows[-1]["frames"] == 60,
           "the whole file: 60 frames and the end line")
        with open(q, "wb") as fh:
            fh.write(partial[:len(partial) // 2])
        rep = {"torn": False, "bad": 0}
        rows2 = list(stream_rows(q, rep))
        ok(rep["torn"] and len(rows2) < 50, "a file cut mid-block is torn, read to its last whole line")
        with open(q, "wb") as fh:
            with open(p, "rb") as src:
                fh.write(src.read() + b"\x00")
        rep = {"torn": False, "bad": 0}
        rows3 = list(stream_rows(q, rep))
        ok(rep["torn"] and len(rows3) == 61, "bytes past the trailer read torn")
        w = StreamWriter(os.path.join(tmp, "cap.jsonl.gz"), window_max=200, flush_s=0)
        w.frame("".join(sha256_bytes(b"%d" % i) for i in range(40)))
        ok(w.cut, "the window maximum cuts the stream")
        w.close()
        w = StreamWriter(os.path.join(tmp, "bin.jsonl.gz"))
        w.frame(b"\x00\xff")
        w.close()
        rep = {"torn": False, "bad": 0}
        rows = list(stream_rows(os.path.join(tmp, "bin.jsonl.gz"), rep))
        ok(rows[0]["raw_b64"] == "AP8=", "a binary frame is stored as base64, verbatim")
        ok(next_stream_path(tmp) == os.path.join(tmp, "stream.jsonl.gz"), "the first stream file of a window")
        open(os.path.join(tmp, "stream.jsonl.gz"), "wb").close()
        ok(next_stream_path(tmp) == os.path.join(tmp, "stream.1.jsonl.gz"), "a second process writes the next name")
        ok(joinable(tmp), "a directory without window.json or books is joinable")
        open(os.path.join(tmp, "books.jsonl.gz"), "wb").close()
        ok(not joinable(tmp), "a directory holding books is not rejoined")
        # the unit, on synthetic windows: every reason it names
        t = 1791627300
        four_toks = ["11", "12", "13", "14"]
        ns = 10 ** 9

        def synth(name, sub_at, frames, end_at, close_ok=True, extra=None, declared=None):
            d = os.path.join(tmp, name)
            os.makedirs(d)
            lines = [{"recv_ns": sub_at - 10 ** 6, "mono_ns": 1, "event": "connect", "seg": 0},
                     {"recv_ns": sub_at, "mono_ns": 2, "event": "subscribe", "seg": 0, "message": "m"}]
            lines += frames
            if close_ok:
                lines.append({"recv_ns": end_at, "mono_ns": 3, "event": "close", "seg": 0, "reason": "end", "code": None})
                lines.append({"recv_ns": end_at + 1, "mono_ns": 4, "event": "end", "frames": len(frames)})
            body = "".join(json.dumps(x) + "\n" for x in lines).encode()
            with open(os.path.join(d, "stream.jsonl.gz"), "wb") as fh:
                fh.write(gzip.compress(body, mtime=0))
            st = new_stream_stats()
            st.update({"opened": True, "files": ["stream.jsonl.gz"], "frames": len(frames) if declared is None else declared})
            wj_ = {"documents_ok": True, "joined_late": False, "stopped": False, "stream": st}
            if extra:
                wj_.update(extra)
            return stream_unit(t, d, wj_, four_toks[:2], four_toks[2:])

        books = [{"recv_ns": (t + 595) * ns + 10 ** 8, "mono_ns": 0,
                  "raw": json.dumps([synth_book(x, "0xc") for x in four_toks])}]
        steady = [{"recv_ns": (t + 596 + k) * ns, "mono_ns": 0,
                   "raw": json.dumps(synth_change(four_toks[:2] if k % 2 else four_toks[2:], "0xc", (t + 596 + k) * 1000))}
                  for k in range(309)]
        why, sst = synth("good", (t + 595) * ns, books + steady, (t + 905) * ns)
        ok(why == [] and sst["frames"] == 310 and sst["max_gap_ns"] == ns and sst["lag_ms"]["median"] == 0
           and sst["subscribe_offset_ms"] == 595000 and sst["last_close_offset_ms"] == 905000,
           "a window streamed from T+595 to T+905: complete, its largest gap 1 s")
        why, _s = synth("late", (t + 601) * ns, [dict(books[0], recv_ns=(t + 601) * ns + 1)] + steady[6:], (t + 905) * ns)
        ok(why == ["late subscribe"], "a subscription after T+600 reads late subscribe, and nothing else")
        why, _s = synth("nobook", (t + 595) * ns, steady, (t + 905) * ns)
        ok(why == ["initial books"], "no book of the four tokens within 5 s of it reads initial books")
        holed = books + [x for x in steady if not ((t + 700) * ns <= x["recv_ns"] <= (t + 716) * ns)]
        why, _s = synth("gap", (t + 595) * ns, holed, (t + 905) * ns)
        ok(why == ["gap"], "18 s without a frame reads gap")
        why, _s = synth("torn", (t + 595) * ns, books + steady, (t + 905) * ns, close_ok=False)
        ok(why == ["no end line in stream.jsonl.gz", "short"], "a file without its end line and its close reads so")
        why, _s = synth("early", (t + 595) * ns, books + steady[:290], (t + 890) * ns)
        ok(why == ["short"], "a stream whose last close is before T+900 reads short")
        odd = books + steady + [{"recv_ns": (t + 904) * ns + 1, "mono_ns": 0, "raw": '{"event_type": "new_market", "asset_id": "11"}'},
                                {"recv_ns": (t + 904) * ns + 2, "mono_ns": 0, "raw": json.dumps(synth_book("99", "0xd"))}]
        why, _s = synth("odd", (t + 595) * ns, odd, (t + 905) * ns, declared=len(odd) - 1)
        ok(why == ["nonconforming frames", "foreign tokens", "count"],
           "an undocumented event type, a token not subscribed and a count off its window.json are named")
        why, _s = synth("joined", (t + 595) * ns, books + steady, (t + 905) * ns, extra={"joined_late": True})
        ok(why == ["joined late"], "a window joined late is no unit")
        why, _s = synth("nodocs", (t + 595) * ns, books + steady, (t + 905) * ns, extra={"documents_ok": False})
        ok(why == ["documents"], "a window without both documents is no unit")
        off = new_stream_stats()
        off["off_reason"] = "cap"
        ok(stream_unit(t, tmp, {"documents_ok": True, "stream": off}, four_toks[:2], four_toks[2:])[0] == ["no stream (cap)"],
           "a window whose stream did not open names why")
        ok(frame_tokens([synth_book("11", "0xc")]) == (["book"], {"11"}, None)
           and frame_tokens(synth_change(["11", "12"], "0xc", 5))[1:] == ({"11", "12"}, 5)
           and frame_tokens({"event_type": "tick_size_change", "asset_id": "11"}) == (["tick_size_change"], {"11"}, None)
           and frame_tokens({"event_type": "last_trade_price", "asset_id": "12"})[1] == {"12"}
           and frame_tokens([]) is None and frame_tokens({"event_type": "book"}) is None
           and frame_tokens({"event_type": "price_change", "price_changes": []}) is None and frame_tokens(7) is None,
           "frame_tokens: the four documented types and their token ids, nothing else")
        good_wj = {k: None for k in WINDOW_JSON_KEYS}
        assert_keys(good_wj, WINDOW_JSON_KEYS, "window.json")
        try:
            assert_keys(dict(good_wj, stream={"best_ask": 1}), WINDOW_JSON_KEYS, "window.json")
            caught = False
        except AssertionError:
            caught = True
        ok(caught, "a forbidden key at any depth fails the allow-list")
        ok(not (STREAM_KEYS | WINDOW_JSON_KEYS | WINDOW_MARKET_KEYS | PROOF_JSON_KEYS | PRESTART_JSON_KEYS) & FORBIDDEN_KEYS,
           "no allowed key is a forbidden one")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    # the readings, on synthetic counts, and their error rates against fractions computed outside this file
    ok([read_g_stream(u) for u in ([True] * 4, [True, True, True, False], [True, True, False, False], [True] * 3)]
       == ["PASS", "PASS", "FAIL", "UNDECIDABLE"], "G-STREAM: 4 and 3 of 4, 2 of 4, fewer than 4")
    ok([read_g_books(28, 26), read_g_books(28, 25), read_g_books(27, 27)] == ["PASS", "FAIL", "UNDECIDABLE"],
       "G-BOOKS: 26 of 28, 25 of 28, fewer than 28")
    ok([read_g_tierc(r) for r in ([(True, True, True)] * 2, [(True, True, True)] * 2 + [(False, True, False)],
                                 [(True, True, True), (True, False, None)], [(True, True, True), (False, True, True)])]
       == ["PASS", "FAIL", "UNDECIDABLE", "UNDECIDABLE"], "G-TIERC: two loaded, any failure, too few loaded")
    ok(p_fail_at_least(4, 2, Fraction(1, 100)) == Fraction(59203, 100000000), "G-STREAM's false failure at 1 in 100")
    ok(p_fail_at_least(4, 2, Fraction(1, 4)) == Fraction(67, 256) and p_fail_at_least(4, 2, Fraction(1, 2)) == Fraction(11, 16),
       "G-STREAM's power at 1 in 4 and 1 in 2")
    ok(p_fail_at_least(28, 3, Fraction(1, 100)) == Fraction(1, 1) - Fraction(99, 100) ** 28 - 28 * Fraction(1, 100)
       * Fraction(99, 100) ** 27 - 378 * Fraction(1, 100) ** 2 * Fraction(99, 100) ** 26
       and decimals(p_fail_at_least(28, 3, Fraction(1, 100)), 10) == "0.0027171219",
       "G-BOOKS' false failure at 1 in 100")
    ok(decimals(p_fail_at_least(28, 3, Fraction(1, 4)), 10) == "0.9833852515"
       and decimals(p_fail_at_least(28, 3, Fraction(1, 10)), 10) == "0.5406170777", "G-BOOKS' power at 1 in 4 and 1 in 10")
    ok(p_false_alarm(0, 2016, 4) == 0 and p_false_alarm(1, 2016, 4) == 1 - Fraction(2015, 2016) ** 4
       and p_false_alarm(0, 0, 4) is None, "G-TIERC's false alarm, exact")
    ok(decimals(Fraction(1, 3), 4) == "0.3333" and decimals(Fraction(2, 3), 4) == "0.6667", "decimals: half up")
    # this file's own syntax: its imports and its endpoints
    with open(os.path.abspath(__file__), encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    mods = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            mods |= {a.name.split(".")[0] for a in node.names}
        elif isinstance(node, ast.ImportFrom):
            mods.add((node.module or "").split(".")[0])
    ok(mods - set(sys.stdlib_module_names) == {"websockets"}, "imports: the standard library and websockets")
    sep = ":" + "//"
    urls = sorted({c.value for c in ast.walk(tree) if isinstance(c, ast.Constant) and isinstance(c.value, str)
                   and sep in c.value})
    ok(urls == sorted([GAMMA_MARKET_URL, CLOB_BOOK_URL, CLOB_WS_URL]), "exactly three endpoints in the file's text")
    ok(websockets.__version__ == "17.1", "websockets 17.1, the recorder's")
    out("%d of %d checks passed" % (n[0], n[0]))


def main(argv):
    if not argv:
        sys.exit("usage: tz26-nesting-b3-capture.py MODE [ARG...]")
    mode, rest = argv[0], argv[1:]
    MODE[0] = mode
    rc = 0
    if mode == "serve":
        assert not rest, "serve takes no argument"
        rc = mode_serve()
    elif mode == "prove":
        assert len(rest) == 1 and rest[0].isdigit(), "prove A"
        rc = mode_prove(int(rest[0]))
    elif mode == "unit":
        assert len(rest) == 1 and rest[0] in ("0", "1"), "unit N"
        mode_unit(int(rest[0]))
    elif mode == "mark":
        assert len(rest) == 1, "mark NAME"
        mode_mark(rest[0])
    elif mode == "scratch":
        assert len(rest) == 1, "scratch OWN"
        mode_scratch(rest[0])
    elif mode == "reclaim":
        mode_reclaim(rest)
    else:
        table = {"fingerprint": mode_fingerprint, "selftest": mode_selftest, "still": mode_still,
                 "chainbook": mode_chainbook, "restart": mode_restart, "final": mode_final,
                 "prestart": mode_prestart, "load": mode_load, "restored": mode_restored}
        assert mode in table and not rest, "unknown mode %r" % (argv,)
        table[mode]()
    if mode != "serve":
        out("peak memory of this run: %d bytes" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024))
        out("opens refused: %d; manifest opens attempted %d; chain book opens %d; requests %d, stream sessions %d" % (
            len(REFUSED), OPENS["manifest.json"], OPENS["chainbook"], COUNTERS["requests"], COUNTERS["sessions"]))
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
```
