# TZ-47 — the live host: the server in Sofia reached by the Executor over SSH, its swap and its system journal bounded, and the venue's geoblock, network path and latency, its memory and its disk read from it before any key exists

**Canonical filename:** `TZ-47-live-host.md`. The committed file takes this name and no other.

**Executor model: Claude Opus 5.5.** A second host reached over SSH and configured, and the venue's network path measured from it.

**Required System Map revision:** `2026-11-18-a` — `main` at `1519f9f`, which carries it. **No map revision ships with this TZ.** Its merge adds one `frozen` row, `research/tz47-live-host.py`, which the map revision attached to its verdict carries; it replaces no row (CANON hard rule 17). **Map §5's L1 row and map §8 name Georgia for the live host, as CANON `2026-11-16-a` does; the Boss moved it to Sofia (§1.1), and both are revised with this TZ's verdict.**

**Map sections this TZ rests on**, copied from §10's C8 (map §7 item 174): §0, the fingerprint gate and its table; §1, the repository and its TZs; §2.6, the reward book — its store's bounds, rule W's latency and its reserve; §2.7, the advisor's token; §3, the units, the trees on the host and the session directories; §5, L1's row; §6, its rows host; host identity, for TZ host gates; language; git remote; egress; venue edge — the `User-Agent`; venue geoblock — measured from the host, 2026-11-13, TZ-44; disk; disk floors and caps, as each code reads them; headroom — measured on total free space, and conditional; the consumer; process supervision; memory; clock; sandbox limit — destructive actions; and harness — background output; §7 items 86, 89, 91, 95, 98, 119, 124, 127, 132, 137, 138, 140, 143, 144, 150, 156, 163, 169, 174, 175, 176 and 177; §8.

**Required anchors**, from map §0. A mismatch on any one is BLOCKED before any work:

| anchor | required |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` |
| `A4` — executor contract | `6ac6e10aeabc` |
| `A5` — recorder | `0f6c90451cbd` |
| `A6` — pricer | `729f0bcdbee3` |

**Host gates:** §0.3, the capture host, where the Executor runs and the branch is made, and of whose capture nothing is touched; §0.6, the live host, reached as `live-host`.

**Before `EXECUTE TZ-47`:** the Boss uploads this file into `CryptoTZ/`, and nothing else. **His one hands-on step sits inside the run, at the point that needs it (map §7 item 132): B-ACCESS, §0.6 — one paste in a terminal on the capture host that writes the live host's address under the alias `live-host` and authorizes the Executor's key there with that host's root password, typed once.** He is needed besides only for a block the session's classifier refuses (§3), each handed over as one paste.

**When: begun at any hour but from 03:00:00 to 07:30:00 UTC** — 07:00 to 11:30 in Batumi: the package manager's morning on the capture host, `apt-daily-upgrade.timer` about 06:00 to 06:30 UTC, which restarts the captures (map §6, process supervision; §7 items 143 and 176), less about three hours — the room's wait, B-ACCESS's bound and the work at their longest. §0.0 reads the clock and, inside that window, begins nothing and owes no report. A run a slow handover carries into that morning goes on: §3.9 names a capture's restart from its journal, and the live host's own package manager is read before each of its measurements (§3.4). **By 2026-11-24, for the refund:** the server was bought on 2026-11-18 and is refundable for seven days, and §4.8 decides from this TZ's readings whether it is kept. About 45 minutes of the session's wall clock beside B-ACCESS (§6).

**What this TZ is.** The first of L1's live-host steps (CANON PART II, L1; map §7 item 169): the server L1's orders will come from, read and prepared before any key of any venue exists. The Boss bought it on 2026-11-18 — xServer (XServer OÜ), Sofia, Bulgaria: one processor, 2 GB of memory, a 20 GB disk, Ubuntu 24.04, host name `vs-2348` — and moved the live host there from Georgia (§1.1). This TZ **(a)** gives the Executor its access to it: a key of its own on the capture host, authorized once by the Boss, the host reached as `live-host`; **(b)** reads the venue's geoblock from its address before anything else and BLOCKS where the venue blocks or does not read it; **(c)** reads from it the venue's CLOB and market websocket, and the time to the first byte of the CLOB's `/time` over one kept connection against the replays' one-way latency of 50 ms; **(d)** reads its memory, its disk and the rest of its state; **(e)** gives it a swap file of 1 GiB and bounds its system journal, with rsyslog off. It deploys no unit and starts no process that outlives it (CANON hard rule 14). One instrument, `research/tz47-live-host.py`: Appendix A. **No order is placed, no key of any venue is created, held or read, no request is authenticated, and no money moves** — everything inside the server's seven days of refund.

---

## 0. Gates

### 0.0 The instant and the readiness, then the work tree

After contract §1 steps 1 and 2, and before anything else, in the session — verbatim, read-only:

```
/root/tz04a-env/venv/bin/python -B - <<'EOF2'
import os, time
now = int(time.time()); s = now % 86400
v = os.statvfs("/var/lib"); free = v.f_bavail * v.f_frsize
with open("/proc/meminfo", encoding="utf-8") as fh:
    mem = [int(ln.split()[1]) * 1024 for ln in fh if ln.startswith("MemAvailable:")][0]
ready = not (10800 <= s < 27000) and free >= 7795535636 and mem >= 70092270
print("ready=%d: second %d of the day, outside 10800 to 27000; %d bytes free on /var/lib, 7795535636 needed; MemAvailable %d, 70092270 needed; at %d %s" % (ready, s, free, mem, now, time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now))))
EOF2
```

**`ready=1` begins the run. `ready=0`, or a read that ends without its `ready=` line, begins nothing:** no directory is made, nothing is written, committed or pushed and no report is written — this TZ has not executed (CANON hard rule 5) — and the Executor gives the Boss the read's line as printed and, in one line, in Russian, the next instant to send `EXECUTE TZ-47`: 07:30 UTC where the clock stopped it, an hour later where memory or the disk did. This is not BLOCKED and owes no report (contract §5); a later `EXECUTE TZ-47` starts the TZ afresh. Then:

```
mkdir /root/tz47-work /root/tz47-work/logs; echo "exit=$?"
```

`exit=0` proves neither existed; anything else is BLOCKED. The readiness read is run again into `logs/00-ready.log`. **From here every command's output goes to a log, one file per step, under the names §3's table fixes** — the capture host's under `/root/tz47-work/logs/`, the live host's under its own `/root/tz47-work/logs/` until §3.9 copies them — and nothing to the session's scratchpad; B-RECLAIM-OWN, §9, is the one exception (map §7 item 89).

Six abbreviations, written out in full in every block handed to the Boss:

- **`P`** — `nice -n 19 /root/tz04a-env/venv/bin/python -B`, on the capture host.
- **`I0`** — `P /root/tz47-work/stage/research/tz47-live-host.py`, the staged copy, for §0 alone.
- **`I`** — `P /root/tz47-work/wt/research/tz47-live-host.py`, the committed copy, from §3.1 on.
- **`R`** — `ssh -o BatchMode=yes -o ConnectTimeout=20 -o LogLevel=QUIET live-host`: a command on the live host, never asking for anything and never printing an error of its own, whose text would carry the host's address (§2 item 5); its exit tells.
- **`L M NN`** — the live host's mode `M` into its log `NN`, run with the session's tool timeout at its maximum, 600 s: `R 'cd /root/tz47-work && { date -u +%FT%T.%NZ; /usr/bin/python3 -B /root/tz47-work/tz47-live-host.py M; echo "exit=$?"; } >> /root/tz47-work/logs/NN.log 2>&1; tail -n 60 /root/tz47-work/logs/NN.log'`. **Its paste**, where the classifier refuses it, is the quoted part alone, run by the Boss in a terminal on the live host; the Executor then reads that log with `R 'tail -n 60 /root/tz47-work/logs/NN.log'` and runs none of it again (map §7 item 144).
- **`S`** — the scratchpad directory the session's system prompt names (map §7 item 98's form).

Every mode of the instrument runs from `/root/tz47-work` on its host — `main` asserts it (lines 1786 to 1810).

### 0.1 The instrument, staged

Extract Appendix A from this TZ as the primary checkout carries it after contract §1's pull, with this script, verbatim, its one argument the destination, its output into `logs/01-stage.log`:

```
/root/tz04a-env/venv/bin/python -B - /root/tz47-work/stage <<'EOF2'
import hashlib, os, sys
SRC = "/root/btc-5m-twap/CryptoTZ/TZ-47-live-host.md"
DEST = sys.argv[1]
WANT = {"research/tz47-live-host.py": "5e2e7a7fbae23895589cf80a1bd032b4e2a82ba8bce0c2f469412a99b3ff2dbc"}
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
    print(path, data.count(b"\n"), len(data), hashlib.sha256(data).hexdigest(), "created")
EOF2
```

| path | lines | bytes | SHA-256 |
|---|---|---|---|
| `research/tz47-live-host.py` | 1,814 | 91,865 | `5e2e7a7fbae23895589cf80a1bd032b4e2a82ba8bce0c2f469412a99b3ff2dbc` |

A failed assert or another hash is BLOCKED. The staged copy runs §0.2's `fingerprint`, §0.3's `room`, §0.5's `number` and `refs`, and is the copy §0.6 sends to the live host.

### 0.2 Fingerprint

`I0 fingerprint`, into `logs/02-fingerprint.log`, performs contract §1 steps 3 and 4 inside the instrument and asserts them, against `SYSTEM-MAP.md` and the files of its §0 table in the primary checkout `/root/btc-5m-twap`: revision `2026-11-18-a`; the six anchors; `A2`, `A4`, `A5` and `A6` re-derived as the first 12 hex characters of those files' SHA-256; the table's **65** rows, each printed in lines, bytes and SHA-256 — **62** `frozen` rows asserted equal to the map, **2** `tracked` and **1** `reported`; and the map's own lines, bytes and SHA-256 (`mode_fingerprint`, lines 802 to 831). It prints `FINGERPRINT PASS` or stops at the first mismatch, which is BLOCKED.

### 0.3 Host gate — the capture host

From `/root/btc-5m-twap`, output verbatim into `logs/03-host-gate.log`:

```
date -u; date -u +%s; uptime -s; nproc; grep -E '^(MemTotal|MemAvailable|SwapTotal|SwapFree):' /proc/meminfo
df -B1 --output=source,size,avail /var/lib/btc-recorder
find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
grep -c e3975b5da44c5328adf3bf3914634cd878842c73 /var/lib/btc-recorder/runtime.jsonl
/root/tz04a-env/venv/bin/python -c 'import sys; print(sys.version.split()[0])'
command -v ssh ssh-keygen ssh-copy-id scp
TZ=UTC systemctl show btc-recorder.service btc-rewardbook.service adv3-bot.service btc-rewardbook-archive.service btc-rewardbook-archive.timer -p Id -p MainPID -p NRestarts -p ActiveState -p UnitFileState -p ActiveEnterTimestamp
du -sb /var/lib/btc-rewardbook /root/btc-forensics /root/.claude-8j 2>&1; find /root/btc-forensics -type f | wc -l
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
systemctl is-active telemetry-watch.service; echo "exit=$?"
test -e /root/tz46-work; echo "/root/tz46-work exit=$?"
test -e /root/.ssh/live-host; echo "/root/.ssh/live-host exit=$?"
git -C /root/btc-5m-twap worktree list
echo "$S"; ls -la "$(dirname "$(dirname "$S")")"
```

then the memory gate's own reads, appended to the same log:

```
for k in 1 2 3 4 5; do m=$(( $(awk '/^MemAvailable:/ {print $2}' /proc/meminfo) * 1024 )); echo "MemAvailable read $k $(date -u +%T): $m"; [ "$m" -ge 70092270 ] && break; [ "$k" -lt 5 ] && sleep 60; done
```

- **H1** — `find` prints exactly one path.
- **H2** — `df` names source `/dev/vda2` and size `31612203008` (map §6, disk); `grep -c` prints at least `1`. With H1 this is map §6's host identity (map §7 item 86).
- **H3** — the interpreter prints `3.12.`.
- **H4** — `command -v` prints four paths, one each for `ssh`, `ssh-keygen`, `ssh-copy-id` and `scp`: the access's tools.
- **Memory gate** — the last `MemAvailable read` at least `70,092,270` bytes: a read below it is read again 60 s later, five reads at most, the first at or above it passing (§0.4; map §7 item 137).
- **Disk gate** — `avail` at least `7,795,535,636` bytes, §0.0's bound read again (§0.4).

These are seven checks — H2 two — and any one failing is BLOCKED. **The rest is printed and carries no threshold:** the units this TZ leaves alone, whose states the closing reads print again (§3.9); the reward book's store, the forensic store and its count and the sessions' configuration directory by `du`, as every TZ after TZ-33 reads them (map §2.6); the consumer's two states, on which map §6's headroom is conditional; `/root/tz46-work` gone, as TZ-46's report §5.1 read it; whether the Executor's key exists already; the worktrees, map §3's two; and the listing of the directory that holds the session's own (map §7 item 150). Then `I0 room`, into `logs/04-room.log` (`mode_room`, lines 873 to 893): `btc-rewardbook-archive.service` read until it reads `inactive`, at most 30 reads 60 s apart, as map §3, the units, asks of a TZ that reads a capture's store — still running at the last read, the room is not read — then free space on `/var/lib`, the reward book's stream files by their directory entries alone, the room and **its margin over `STREAM_FLOOR` and `PEAK`** — printed, no threshold, as map §7 item 175 asks of every TZ that touches the host; a margin under `1,000,000,000` is flagged in the line itself. **Its wait can pass one call's 600 s:** it runs in the background with `echo "exit=$?"` after it, the harness keeping a background command's output (map §6, harness — background output), and its log is read at most every 570 s until that line; a log that stops without it is run again, once.

### 0.4 Resource floors, in exact bytes

**The capture host's disk: `7,795,535,636` bytes available on `/var/lib`, at §0.0 and §0.3 and at the start of `room`** (`CAPTURE_FLOOR`, line 143): the reward book's `STREAM_FLOOR`, `7,300,000,000`, below which no stream of it opens for a slot (`research/tz33-reward-book-capture.py` line 190), plus `PEAK`, `445,535,636`, the most its store holds between two runs of its archive (map §6, disk floors and caps), plus `50,000,000`, this session's writes there at most — the worktree, `main`'s 177 files of `15,444,768` bytes at `1519f9f` [counted by the Architect, 2026-11-18] with this file and the instrument, about `15,800,000`; the stage, `91,865`; both hosts' logs, under `5,000,000`. So nothing this session writes can take the reward book below its stream floor, even at its store's peak. **The live host's disk: `3,589,660,928` bytes available on `/`, at `host before`, `disk` and `files`** (`LIVE_FLOOR`, line 146), and the live work tree's bound, `100,000,000`, at `latency` (`LIVE_WORK_MAX`, line 145): the swap file, `1,073,741,824`; the write test, `268,435,456`; journald's `SystemKeepFree`, `2,147,483,648`, under which the journal itself writes nothing (§1.4); and the live work tree, `100,000,000` at most. So neither the swap file nor the write test can take that disk under the floor the journal keeps.

**Memory, on both hosts: `MemAvailable` at least `70,092,270` bytes at each host gate — §0.3's and `host before` — and at the start of `room`, `latency`, `disk` and `files`** (`MEM_FLOOR`, line 148; `floors`, lines 310 to 323) — twice `35,046,135`, the host peak modelled from the largest of the Architect's runs of the instrument and its drafts at the ratio TZ-37 measured between a host's peak and the Architect's for one code, `58,953,728 / 49,168,384` (map §6, memory; §7 item 156): `latency` peaked at `29,229,056` bytes over its full 605 requests against a loopback server, every line printed, under Python 3.12.3; every other mode, the network's against the venue, `25,833,472` to `28,930,048`. A read below the floor is read again every 60 s, five reads at most, the first at or above it passing and five below it BLOCKING (map §7 item 137). The capture host's `MemAvailable` read `136,404,992` to `562,360,320` across the TZs since 2026-10-31 (map §6, memory). Every mode prints its peak on every exit (`main`, lines 1806 to 1809), and runs under `nice -n 19` on the capture host: it has one processor.

### 0.5 Refs and the number

`I0 number`, into `logs/05-number.log`, and `I0 refs`, into `logs/05-refs.log`, after §0.4; both again in §3.1 — `I0 number` after its fetch, `I0 refs` before its push. **NUMBER — CANON hard rule 2:** `I0 number` reads `git ls-tree --name-only origin/main -- CryptoTZ/ CryptoReports/` in the primary checkout and must print `NUMBER PASS - 2 of 2`: `CryptoTZ/` holds `TZ-47-live-host.md` and no other file whose name begins with `TZ-47-`, and `CryptoReports/` no report whose name does (`number_reading` and `mode_number`, lines 532 to 537 and 834 to 842; map §7 item 127). Anything else is BLOCKED, here and in §3.1 alike. `CryptoTZ/` and `CryptoReports/` end at TZ-46's files (map §1), so this TZ's number is 47. **`I0 refs`** prints `HEAD` and `refs/heads/main` and every other ref counted by kind — never every tag (map §7 item 177) — and BLOCKS where `refs/heads/tz-47-live-host` exists (`refs_reading` and `mode_refs`, lines 540 to 559 and 845 to 856). **The Architect read 176 ref lines on 2026-11-18 at 21:34 UTC:** `HEAD` and `refs/heads/main` at `1519f9f`; 22 `tz-*` branches; 45 pull heads and no merge ref; 59 `pairbook-streams-*` and 42 `rewardbook-streams-*` tags; `tz-01a-dataset` and `tz-27-pairbook-streams` with their peeled lines; `tz-44-l0-inputs` and `tz-45-l0-rule-w-inputs`. The reward book's archive adds a tag every three hours (map §7 item 177) and the upload of this file a commit: the report names each kind whose count differs from this read, and `main`'s new commit — a difference is recorded, not BLOCKING.

### 0.6 The live host — access, its gate and the geoblock

**Access.** Into `logs/06-access.log`, `R true; echo "exit=$?"`. **`exit=0`** — the Boss ran B-ACCESS before — goes to the reads below. **Otherwise** the Executor runs `test -e /root/.ssh/live-host || ssh-keygen -q -t ed25519 -N '' -C 'btc-5m-twap executor, capture host to live host' -f /root/.ssh/live-host` itself — the key of its own; where the classifier refuses it, B-ACCESS makes it — and hands the Boss **B-ACCESS** once, in plain words: run in a terminal on the capture host, it asks for the live host's IPv4 address and then for its root password, each typed once:

```
install -d -m 0700 /root/.ssh && { test -e /root/.ssh/live-host || ssh-keygen -q -t ed25519 -N '' -C 'btc-5m-twap executor, capture host to live host' -f /root/.ssh/live-host; } && { grep -qx 'Host live-host' /root/.ssh/config 2>/dev/null || { read -r -p 'live host IPv4 address: ' A && [ -n "$A" ] && printf '\nHost live-host\n  HostName %s\n  HostKeyAlias live-host\n  User root\n  IdentityFile /root/.ssh/live-host\n  IdentitiesOnly yes\n  ServerAliveInterval 15\n  ServerAliveCountMax 4\n' "$A" >> /root/.ssh/config; }; } && chmod 0600 /root/.ssh/config && ssh-copy-id -o StrictHostKeyChecking=accept-new -o LogLevel=ERROR -i /root/.ssh/live-host.pub live-host && ssh -o BatchMode=yes live-host hostname
```

With it, and only for the case where its `ssh-copy-id` answers `Permission denied (publickey)` — the live host refusing root's password — **B-ACCESS-KEY**, run in a terminal on the live host, the Executor writing in the one line `/root/.ssh/live-host.pub` holds, once the key exists:

```
install -d -m 0700 /root/.ssh && printf '%s\n' '<the line of /root/.ssh/live-host.pub>' >> /root/.ssh/authorized_keys && chmod 0600 /root/.ssh/authorized_keys && echo authorized
```

The Executor then reads `R true` every 30 s, in calls of at most 570 s each, for at most 120 minutes from the handover, each read with its instant into `logs/06-access.log`; the first `exit=0` ends the wait, and **at the bound the run is BLOCKED** (map §7 item 132). **Then, into the same log:**

```
ssh-keygen -lf /root/.ssh/live-host.pub
ssh -G live-host | grep -E '^(user|hostkeyalias|identityfile|identitiesonly|serveraliveinterval) '
ssh-keygen -lF live-host
R 'hostname; id -un; test -e /root/tz47-work; echo "work tree exit=$?"'
```

They print the key's fingerprint, the alias's settings without its `hostname` line — the address, which no file of this TZ's run writes into a log (§2 item 5) — the live host's key as pinned under the alias, and `vs-2348`, `root` and `work tree exit=1`; anything else on the last line is BLOCKED. **The copy**, into `logs/07-copy.log`:

```
R 'mkdir /root/tz47-work /root/tz47-work/logs; echo "exit=$?"'
scp -q -o BatchMode=yes -o LogLevel=QUIET /root/tz47-work/stage/research/tz47-live-host.py live-host:/root/tz47-work/tz47-live-host.py; echo "scp exit=$?"
R 'sha256sum /root/tz47-work/tz47-live-host.py; wc -lc /root/tz47-work/tz47-live-host.py'
```

`exit=0`, `scp exit=0`, and §0.1's line count, bytes and SHA-256 — anything else is BLOCKED. **The live host's gate:** `L` of `host before` into `40-host-before` (`mode_host`, lines 1084 to 1172): the four checks of `live_gate` (lines 638 to 644) — **LH1** host name `vs-2348`, **LH2** Ubuntu 24.04 by `/etc/os-release`, **LH3** Python 3.12, **LH4** neither `/var/lib/btc-recorder` nor `/root/btc-5m-twap` present, so not the capture host — and §0.4's floors: any failing is BLOCKED, `exit=1`. It prints the host's facts (§1.5) and **G-SPEC** (§4.2): `exit=0` PASS, `exit=4` FAIL, which stops nothing here. **The geoblock, before anything else changes:** `L geoblock 41-geoblock` (`mode_geoblock`, lines 1213 to 1229): **G-GEO** (§4.1). `exit=0` PASS; **`exit=1` is BLOCKED** — the venue blocks this address or did not read it — and the run goes to §3.9's copy and §9 as §3 says, nothing having been changed on the live host but its `authorized_keys` and its work tree.

---

## 1. Why this TZ exists, and what it changes

Line numbers in this section are Appendix A's instrument's unless a file is named.

### 1.1 The Boss's request

His words: "Decision from the previous chat: the live server is in Sofia, not Georgia." — and — "In the TZ: Claude Code access to the new server, 1 GB swap, log size limits, geoblock from the server's IP address (BLOCK if blocked), latency to clob.polymarket.com versus 50 ms one-way, memory and disk measurements. No keys and no orders, everything within the 7-day refund period." CANON PART IV fixed the live host in Georgia on 2026-11-14 and map §5 and §8 repeat it; **this TZ follows the Boss's later decision**, and both documents are revised with its verdict. Georgia stays the place the Boss is; the venue lists neither Bulgaria nor Georgia among its restricted or close-only countries [read by the Architect at `docs.polymarket.com/api-reference/geoblock` on 2026-11-18; not measured], and the read from the host's own address is the measurement (§4.1).

### 1.2 Access: the Executor stays on the capture host — the Architect's decision

**The Executor runs where it runs — on the capture host, spawned by the remote-control session there (map §6, harness — background output) — and reaches the live host over SSH with a key of its own.** Claude Code is not installed on the live host, so that the host which will hold L1's trading key holds no agent's login, no GitHub credential and no checkout of the repository, and the Executor's contract, credentials, forensic store and logs stay one. **Discarded:** Claude Code on the live host under its own remote control — two logins of the Boss's to make on a phone, a GitHub credential beside the trading key, and a second Executor environment to keep. The key is ed25519, `/root/.ssh/live-host`, root's on the capture host; the alias `live-host` in root's `~/.ssh/config` carries the address, which **no file of the repository and no log of this run holds**: the repository is public (map §1), and the map's rule for the capture host's address holds for this one — never printed, written or published (map §6, venue geoblock). The live host's own key is pinned under the alias at the first connection — `HostKeyAlias live-host`, `StrictHostKeyChecking=accept-new` — and every later connection is `BatchMode=yes`: it fails rather than asks. **What the access does not yet have, before any key of any venue reaches the host, is §1.6 item 3.**

### 1.3 Swap

**1 GiB — `1,073,741,824` bytes, the Boss's "1 GB" in the binary unit (CANON hard rule 9) — as `/swapfile`, `0600`, root's,** written whole by `dd` from `/dev/zero` — no holes, whatever the file system — formatted by `mkswap`, listed in `/etc/fstab` as `/swapfile none swap sw 0 0`, and proved from that line by `swapoff` and `swapon -a`. **`vm.swappiness = 10`**, from `/etc/sysctl.d/zz-btc-5m-twap-swap.conf`: the kernel drops page cache before it swaps a process out, so the engine's pages stay in memory while the swap guards the host against running out (CANON PART IV: one process). A swap that existed before this TZ is not touched: B-CONFIGURE's swap part runs only where `/swapfile` is absent, and G-SWAP reads what is there (§4.5).

### 1.4 The logs' bounds

**One store, bounded.** The system journal is the live host's only log store: `Storage=persistent`, `SystemMaxUse=512M` — `536,870,912` bytes — `SystemKeepFree=2G` — `2,147,483,648` — `SystemMaxFileSize=64M`, `RuntimeMaxUse=64M` and `ForwardToSyslog=no`, from `/etc/systemd/journald.conf.d/zz-btc-5m-twap-limits.conf`; rsyslog, where it is installed, disabled and stopped with its socket. **The sizes are the disk's budget, not a rate — no rate of this host exists yet:** of the 20 GB sold the journal takes at most 512 MiB and never writes into the last 2 GiB, beside the system's own files, about 3.2 GB — 16.3% of 19.35 GB by its login banner of 2026-11-18 — the swap file and the engine's records, which are files of its own and never this journal (CANON PART IV: a Parquet journal of every decision). journald's default would be a tenth of the file system, and rsyslog would write every line a second time under `/var/log`, rotated weekly, kept four weeks and bounded in no size — the class of fault, a store with no bound of its own reaching the disk's floor, that took the capture host's evening of 2026-11-13, when the reward book opened no stream from 21:15 UTC, every slot record naming the disk's floor (CANON §1.5). **Why `zz-`:** Ubuntu 24.04's systemd ships `/usr/lib/systemd/journald.conf.d/syslog.conf`, `ForwardToSyslog=yes`, and journald applies its drop-ins in the lexical order of their names across directories, the last winning, so a name beginning with a digit sorts before it and loses [read by the Architect on Ubuntu 24.04.5 with systemd 255, `systemd-analyze cat-config systemd/journald.conf`, 2026-11-18]; the sysctl file is named the same way. **G-LOG reads the configuration in force by the same command, and journald's own account of its limits** — `MAX_USE` and `DISK_KEEP_FREE` in the usage message systemd 255 logs at every start of journald, after `Journal started` [read by the Architect in systemd's source at `v255`, `src/journal/journald.c` and `src/journal/journald-server.c`, 2026-11-18].

### 1.5 What is measured, and how

- **G-GEO — the venue's geoblock from the host's own address, first** (CANON PART IV; map §7 item 163): `GET https://polymarket.com/api/geoblock`, `User-Agent: btc-5m-twap-tz47`, `Accept: application/json`, over IPv4, and over IPv6 too where the host has a global IPv6 address and the venue's host an IPv6 address; up to three reads 30 s apart while a reply is not readable (`geo_read`, lines 1180 to 1210). Printed of each reply: its status, `blocked`, `country`, `region`, its keys, and whether the address the venue saw is the connection's own source address — a comparison, never the address (`geo_fields`, lines 569 to 575).
- **G-NET — the venue's paths from the host** (`mode_net`, lines 1246 to 1301): the CLOB's root, `"OK"`, and its `/time`, each over HTTPS through a named Cloudflare data centre, and the market websocket's opening handshake, `101` with the accept key its own key asks for, closed at once with status 1000 and no subscription; each read up to three times 30 s apart. Besides, printed: 60 TCP handshakes with the CLOB's edge, 0.5 s apart and each bounded at 2 s, after G-NET's PASS alone.
- **G-LAT — the time to the first byte of the CLOB's `/time`, against the replays' 50 ms one way** (`probe`, lines 451 to 481; `lat_reading`, lines 600 to 623). `/time` is the venue's origin's own reply — `cf-cache-status: DYNAMIC`, through the data centre the `cf-ray` header names [read by the Architect, three requests, 2026-11-18] — so over one connection kept open the time from a request's first byte to its reply's head is the round trip to the origin through the edge plus the origin's own time, and half of it is an upper bound of the one-way latency an order meets, which TZ-45's replay of rule W took as 50 ms (map §2.6). 605 requests one every 0.75 s, the first five a warm-up, each timed on the monotonic clock, which no offset of the wall clock enters (map §6, clock); a counted reply is valid where it is not the connection's first, carries status 200, ten digits, a named data centre and a cache status the origin served. **PASS where the nearest-rank median of at least 570 valid replies is at most `100,000,000` ns** — a one-way bound of 50 ms. The venue's servers are in `eu-west-2` (map §6, venue geoblock). The Architect's rehearsal of these bytes from a host in the United States read a median of 123.735 ms through Chicago, 61.867 ms one way [65 requests on 2026-11-18 at 21:39 UTC; no host of this project]: the reading is the path's.
- **Memory and disk.** **G-SPEC** (`spec_reading`, lines 631 to 635): `MemTotal` at least `1,800,000,000` bytes and the root file system at least `18,000,000,000` — nine tenths of the 2 GB and the 20 GB sold, the rest left to the kernel's reservation and the file system's own blocks. Printed, no threshold: every field of the host's memory before and after the swap; the root file system's bytes and inodes; 256 MiB written in 1 MiB pieces and synced, as bytes a second, and 200 appends of 4 KiB each followed by `fsync`, their median, 99th percentile and maximum (`mode_disk`, lines 1370 to 1383) — the engine's journal is the first thing that will lean on them, and no bound for it exists before it does.
- **The rest of the host, printed** (`mode_host`): its kernel, processors, vendor and boot; `/var/log` and the journal's size and configuration; its units — rsyslog and its socket, journald, timesyncd, chrony, ssh and its socket, the package manager's; the clock's NTP state; `sshd`'s settings and root's authorized keys by type and fingerprint; every listening TCP and bound UDP port by class of address — any, loopback or other — and its process; how many global IPv6 addresses it has; its ten largest processes; and where unattended upgrades may reboot it. These are the facts L1's next TZ starts from.

### 1.6 What L1's next TZ inherits — fixed here

1. **The bot's key.** The Boss's words: "The bot will later need a Polymarket session key — it can trade but cannot withdraw funds; this must be included in the L1 stage TZ." The venue offers it: **Session Keys, in beta** — a separate key that a Deposit Wallet's owner authorizes, by an EIP-712 signature submitted with a Builder API key, to trade for the wallet on the scopes it grants, `CLOB`, `COMBOSRFQ` or `ALL`, for 180 days and no other term, revocable at any time, its revocation cancelling its open orders, and which **cannot withdraw funds from the Deposit Wallet**; it derives CLOB credentials of its own, and its orders carry `signatureType` 3 with the Deposit Wallet as maker and signer; during the rollout a Builder API key is enabled for session keys by builder@polymarket.com [read by the Architect at `docs.polymarket.com/trading/session-keys` on 2026-11-18; not measured]. **L1's key TZ therefore holds on the live host the session key alone, scope `CLOB` and nothing wider, in a file of its own under `/etc/`, `600`, root's, which no command prints, hashes or copies — as the advisor's token (map §2.7); the owner's MetaMask key never reaches any host of this project, and signs the authorization where it lives, on the Boss's own device; and the session key's revocation is the stop of every order path.** The Boss's account, his words: "A Polymarket account was created using a separate MetaMask wallet exclusively for the bot: the deposit wallet has been deployed, tokens have been approved, API keys have not been created, automatic payout has not been enabled, and there is no money in it."
2. **The withdrawal allowlist, before the first deposit.** On accounts with a Deposit Wallet, withdrawals go only to addresses the owner saved, and a change to the list takes 48 hours [read by the Architect at `help.polymarket.com/en/articles/18323576-withdrawal-allowlist` on 2026-11-18]: neither a stolen session nor a signature tricked out of the owner then moves the funds elsewhere.
3. **SSH by key alone, before any key of any venue reaches the live host:** root's password login off, once the Boss's own key is in place; this TZ prints `sshd`'s settings and root's authorized keys.
4. **IPv4 alone,** where the host has a global IPv6 address and G-GEO read IPv4 only.
5. **The clock NTP-synchronized** before the first order; this TZ prints its state.
6. **The latency of L1's replay:** 50 ms one way where G-LAT reads PASS; the one-way bound measured here, rounded up to the millisecond, where it reads FAIL; read again by the next TZ where it reads UNDECIDABLE.
7. **Ubuntu 24.04 kept:** its Python is 3.12 (CANON PART IV); `do-release-upgrade`, which the host's login banner offers, is never run on it.

---

## 2. Scope

Allowed, and nothing else:

1. **The branch `tz-47-live-host`** carries one file, `research/tz47-live-host.py`, new (§10 C3). No other repository file changes. The report goes to `main` (contract §4).
2. **The capture host.** *Written:* `/root/tz47-work/**` — logs, the stage, the live host's logs as copied, the branch worktree and the self-test's temporary tree — removed by §9; **the Executor's access, kept:** `/root/.ssh/live-host` and its `.pub`, the `Host live-host` block appended to `/root/.ssh/config` and the line `ssh-copy-id` pins in `/root/.ssh/known_hosts`, by the Executor's `ssh-keygen` or B-ACCESS; copies into `/root/btc-forensics/` by `reclaim`'s exclusive create alone (§9); earlier session directories under `/tmp/` by B-RECLAIM-SCRATCH (§3.3). *Read:* the primary checkout and `origin`'s refs; the reward book's store by the names and sizes of its directory entries alone, while its archive is not running — no file of it opened (`policy`, lines 203 to 242; `rb_streams`, lines 859 to 870) — every day from 2026-11-14 staying reserved (map §2.6); the recorder's store by §0.3's `find` of one manifest's path and `grep -c` of one commit in its `runtime.jsonl`, as every host gate reads them (map §6, host identity); systemd's records of this project's units, and the two states of `telemetry-watch.service`, another project's unit on which map §6's headroom is conditional; the directory that holds this session's own, listed by `scratch` with its directories' birth instants; root's SSH files of the access, by `ssh -G` and `ssh-keygen`, and the access's tools by `command -v`; `/proc`; `df` and `statvfs` of `/var/lib`; `du` and `test -e` of the trees §0.3 names. **No unit of the capture host is started, stopped, signalled, enabled, disabled or edited, and no store of it is written.**
3. **The live host.** *Written:* one line of `/root/.ssh/authorized_keys`, by B-ACCESS or B-ACCESS-KEY; `/root/tz47-work/**`, removed by §9; **kept:** `/swapfile`, one line of `/etc/fstab`, `/etc/sysctl.d/zz-btc-5m-twap-swap.conf` and `/etc/systemd/journald.conf.d/zz-btc-5m-twap-limits.conf`, by B-CONFIGURE. *Units:* `systemd-journald.service` restarted, and `rsyslog.service` disabled and stopped and `syslog.socket` stopped where rsyslog is installed, by B-CONFIGURE; no other unit started, stopped, enabled, disabled or edited. *Kernel:* `vm.swappiness` set and the swap file activated, by B-CONFIGURE. *The journal:* one message tagged `tz47-probe`, by `verify`. *Read:* `/proc`; `/sys`'s DMI names; `/etc`'s `os-release`, `fstab`, `sshd` and `apt` files; sysctl's and journald's files wherever systemd reads them, under `/etc`, `/run`, `/usr/lib`, `/usr/local/lib` and `/lib`; `sshd -T`'s and `timedatectl`'s prints; root's authorized keys by type and fingerprint; `/var/log` by its files' sizes, and the last MiB of `/var/log/syslog` for the probe alone; systemd's records; the journal's usage messages and the probe.
4. **The network.** From the live host, anonymous, every HTTP request and the websocket handshake with `User-Agent: btc-5m-twap-tz47` (`HEADERS`, line 92; `ws_request`, lines 492 to 494; map §6, venue edge — the `User-Agent`): `https://polymarket.com/api/geoblock`, at most three reads a family; `https://clob.polymarket.com/` and `/time`, at most three reads each and the 605 of the latency probe; 60 TCP handshakes with the CLOB's edge; at most three websocket handshakes with `wss://ws-subscriptions-clob.polymarket.com/ws/market`, no subscription. **The hook refuses a lookup of any other host and a connection to any address this process did not resolve from an allowed name** (`policy`, lines 203 to 242). From the capture host: `git` with GitHub — the fetch, `ls-remote`, the push — and `gh pr create`, which carries `gh`'s credential; `ssh` and `scp` with the live host.
5. **Prints.** No address of either host: the geoblock's `ip` is compared with the connection's own source address and never printed, written or published; the alias's `hostname` line is never printed (§0.6); `ssh` and `scp` run with `LogLevel=QUIET`, so that no error of theirs writes the address into a log; the live host's listening ports carry a class of address, never an address. No password, no private key; the Executor's key by fingerprint. No price, size, side, book hash, rate, competitiveness or outcome of any market.
6. **No order** is placed, signed or cancelled; **no key of any venue** is created, held or read; no request is authenticated; no wallet, account, allowlist or Telegram token is touched.
7. **The session's own trees** — `/root/tz47-work/**` on both hosts — written and removed by §9 (CANON hard rule 15).

---

## 3. The work, in this order

Every command's output goes to its log, one file per step under the names below, and is quoted in the report; a step run again appends to its own log under a `date -u` line. **After a BLOCK, §3.9's copy runs where the live host is reachable and holds its work tree, then §9 — before §3.1 without its `git worktree remove` line and with `I0` in place of `I`.** **G-SPEC or G-NET reading FAIL skips §3.7 and §3.8's `verify`:** the host is returned (§4.8), and nothing is configured on it.

| step | the capture host's logs | the live host's logs |
|---|---|---|
| §0.0 to §0.5 | `00-ready.log`, `01-stage.log`, `02-fingerprint.log`, `03-host-gate.log`, `04-room.log`, `05-number.log`, `05-refs.log` | — |
| §0.6 | `06-access.log`, `07-copy.log` | `40-host-before.log`, `41-geoblock.log` |
| §3.1 | `10-number.log`, `11-worktree.log`, `12-fingerprint.log`, `13-push.log`, `14-pr.log` | — |
| §3.2 | `20-selftest.log` | `50-selftest.log` |
| §3.3 | `30-scratch.log`, `32-reclaim-scratch.log` | — |
| §3.4 to §3.6 | — | `51-net.log`, `52-latency.log`, `53-disk.log` |
| §3.7, §3.8 | — | `60-B-CONFIGURE.log`, `61-verify.log`, `62-host-after.log` |
| §3.9 | `80-live-copy.log`, `90-closing.log`, `99-selfcheck.log` | — |

**Where the session's permission classifier refuses a command of a block named B-… or of a live host's step `L`**, the Executor tries it once and hands the Boss its paste, unchanged, once, in plain words (CANON hard rule 14; map §6, sandbox limit — destructive actions; §7 items 124, 138 and 144): every paste is one command line, every step after the first gated on the one before it, its output appended to its log under a `date -u` line, so that the Executor verifies it from that log and runs none of it again. **A block handed to the Boss holds back only the steps that read what it changes** (map §7 item 140): B-CONFIGURE holds back §3.8; B-RECLAIM-LIVE nothing but §9's last reads; a refused `L` holds back the steps after it on the live host alone.

### 3.1 The branch and its file

```
git -C /root/btc-5m-twap fetch origin
I0 number
git -C /root/btc-5m-twap worktree add -b tz-47-live-host /root/tz47-work/wt origin/main
```

Into `10-number.log` the fetch and `I0 number`, which must print `NUMBER PASS - 2 of 2` again (§0.5), or BLOCKED; into `11-worktree.log` the worktree and §0.1's script again, verbatim but for its argument, `/root/tz47-work/wt` — it must print §0.1's line again, the instrument `created`; into `12-fingerprint.log` `I fingerprint`, which must print `FINGERPRINT PASS` again, from the worktree's file. Into `13-push.log`: `I0 refs` (§0.5); commit the one file alone on the branch; push with `git -C /root/tz47-work/wt push -u origin tz-47-live-host` — through `credential.helper=!gh auth git-credential` where the URL's credential is refused (map §6, git remote) — then:

```
date -u +%FT%T.%NZ; git -C /root/tz47-work/wt ls-remote origin refs/heads/tz-47-live-host
git -C /root/tz47-work/wt rev-parse HEAD
git -C /root/tz47-work/wt diff --numstat origin/main HEAD
```

— the instant the commit is on `origin`, its hash there, which must be the worktree's `HEAD`, and the diff: `1814 0` for the instrument, one path and no other; into `14-pr.log` the pull request against `main`, opened with `gh pr create`. A failed assert or a non-zero exit here is BLOCKED.

### 3.2 The self-test, on both hosts

`I selftest`, into `20-selftest.log`, and `L selftest 50-selftest` must each print `SELFTEST PASS: 42 checks, 42 passed` and `refused by the hook: 1` — the self-test's own refusal of a write outside the work tree, its last check of the hook. It reaches no network but listeners of its own on `127.0.0.1` and runs on literals and on a temporary tree under `/root/tz47-work/selftest-tmp/`, which it removes (`mode_selftest`, lines 1524 to 1783). It proves the nearest-rank percentile; G-LAT at its bound, a nanosecond over it and under its count of valid replies, and which replies count; G-GEO's three readings and that its printed fields never carry the address; G-SPEC at its bounds; the live host gate's four checks, each failing alone; `/proc/swaps` and `fstab` parsed; G-SWAP and ten wrong readings; journald's usage message — this process's System Journal's alone, the last; the configuration in force and a comment that only looks like a file's header; G-LOG and twelve wrong readings; both files' bytes and SHA-256 and the keys they set; NUMBER; the refs by kind; the room and the floors; listening sockets by class; authorized keys by fingerprint, never their comments; `reclaim`'s predicate; the hook's decisions on files, the network and commands, and its live refusal; the probe over one kept loopback connection with every request carrying this TZ's agent, a server that closes every connection, a cached reply and the budget; a request's own source address; TCP handshakes with a closed port; the websocket handshake against a loopback server, valid and with a wrong accept key; the disk's two measurements on a stand-in of 4 MiB; `/proc/meminfo` in bytes; and `systemctl`'s stamp. A red self-test stops the run here, and it goes to §3.9 and §9.

### 3.3 The directories beside this session, and B-RECLAIM-SCRATCH

`I scratch "$(dirname "$S")"`, into `30-scratch.log`, lists every UUID directory beside this session's own and names each **live** — born from 1 s before to 60 s after the start of a running process whose `argv[0]` is `claude` or ends in `/claude.exe` — or **earlier** (`mode_scratch`, lines 922 to 936; map §7 items 91 and 150). Map §3 expects TZ-46's session's own, `ccca2df8-e51d-56bc-8205-06299775095a`, among the earlier, and `95cf58d2-1ec6-4c73-a622-38d04665f5ae` live. **The rule alone decides:** every directory `scratch` names earlier is reclaimed (map §7 item 95).

**B-RECLAIM-SCRATCH**, for every directory `I scratch` names **earlier** — none it named live, and never this session's own — into `32-reclaim-scratch.log`:

```
cd /root/tz47-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz47-work/wt/research/tz47-live-host.py reclaim <each earlier directory, by its full path>
rm -rf <one such directory>; echo "exit=$?"
test -e <that directory>; echo "exit=$?"
```

One `reclaim` names every earlier directory and must print `RECLAIM PASS` before any removal; then one `rm -rf` and one `test -e` a directory, the last reading `exit=1`. `reclaim` refuses a directory born from 1 s before to 60 s after a running claude process started, and any path but `/root/tz47-work` that is not a UUID directory under `/tmp/` whose parent's name carries `btc-5m-twap` (`reclaimable`, lines 792 to 797; `mode_reclaim`, lines 955 to 1002), and keeps nothing of such a directory. If `I scratch` names none earlier, the block is recorded as empty and skipped. **Its paste**, where the classifier refuses it — the Executor writes in every earlier directory's full path, one `rm -rf` and one `test -e` a directory, all chained to the `reclaim`'s `exit=0`:

```
{ date -u +%FT%T.%NZ; (cd /root/tz47-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz47-work/wt/research/tz47-live-host.py reclaim <D1> <D2>); echo "exit=$?"; } >> /root/tz47-work/logs/32-reclaim-scratch.log 2>&1 && tail -n 1 /root/tz47-work/logs/32-reclaim-scratch.log | grep -qx 'exit=0' && { date -u +%FT%T.%NZ; rm -rf <D1>; echo "exit=$?"; test -e <D1>; echo "exit=$?"; rm -rf <D2>; echo "exit=$?"; test -e <D2>; echo "exit=$?"; } >> /root/tz47-work/logs/32-reclaim-scratch.log 2>&1
```

It holds back nothing of §3.4 to §3.9, which read none of what it removes.

### 3.4 G-NET

**Each of §3.4, §3.5 and §3.6 begins with the live host's package manager idle**, read into its step's log `NN` first:

```
R '{ date -u +%FT%T.%NZ; systemctl is-active apt-daily.service apt-daily-upgrade.service; } >> /root/tz47-work/logs/NN.log 2>&1; tail -n 3 /root/tz47-work/logs/NN.log'
```

read again every 60 s while either line reads `activating` or `active`, at most 30 reads in calls of at most 570 s — its paste, where refused, the quoted part alone, as `L`'s; past the 30th the step runs all the same and the report names it — a package run on one processor can only slow what is measured, so a PASS beside one stands. Then `L net 51-net`: its worst case — every check passing only at its third read, each failed read at its two timeouts of 10 s, and the 60 handshakes each at its bound of 2 s — is about 453 s. **G-NET** (§4.3) — `exit=0` PASS, `exit=4` FAIL.

### 3.5 G-LAT

`L latency 52-latency`: the mode begins no request after 540 s (`LAT_BUDGET_S`, line 100), so it ends by about 560 s, its last request at its two timeouts of 10 s; its 605 requests take about 455 s. **G-LAT** (§4.4) — `exit=0` PASS, `exit=4` FAIL or UNDECIDABLE, each named in its last lines. The log holds every request's own line — its index, warm-up or counted, fresh, status, time to the first byte in microseconds, data centre, cache status, body and the venue's seconds less the host's — so that any reading is re-derived from it (contract §6).

### 3.6 The disk

`L disk 53-disk` — the write rate and the fsync latency, printed (§1.5); its two test files removed by the mode itself.

### 3.7 B-CONFIGURE

**Only where G-SPEC and G-NET read PASS.** The Executor's first, as `R 'bash -s'` with the block on its standard input; its paste, the same block run by the Boss in a terminal on the live host:

```
cd /root/tz47-work && { date -u +%FT%T.%NZ; /usr/bin/python3 -B /root/tz47-work/tz47-live-host.py files && install -m 0644 -D /root/tz47-work/files/journald.conf /etc/systemd/journald.conf.d/zz-btc-5m-twap-limits.conf && install -m 0644 /root/tz47-work/files/sysctl.conf /etc/sysctl.d/zz-btc-5m-twap-swap.conf && sysctl -p /etc/sysctl.d/zz-btc-5m-twap-swap.conf && systemctl restart systemd-journald.service; f=$?; echo "files exit=$f"; if systemctl cat rsyslog.service >/dev/null 2>&1; then systemctl disable --now rsyslog.service && systemctl stop syslog.socket; else echo "rsyslog.service: not installed"; fi; echo "rsyslog exit=$?"; [ "$f" = 0 ] && test ! -e /swapfile && (umask 077 && dd if=/dev/zero of=/swapfile bs=1M count=1024 status=none) && mkswap /swapfile && { [ -z "$(tail -c 1 /etc/fstab)" ] || echo >> /etc/fstab; } && { grep -qxF '/swapfile none swap sw 0 0' /etc/fstab || echo '/swapfile none swap sw 0 0' >> /etc/fstab; } && swapon /swapfile && swapoff /swapfile && swapon -a && cat /proc/swaps; echo "swap exit=$?"; } >> /root/tz47-work/logs/60-B-CONFIGURE.log 2>&1; tail -n 30 /root/tz47-work/logs/60-B-CONFIGURE.log
```

**Three parts, each with its own exit.** *The files:* `files` writes the journald and sysctl files into `files/` from the instrument's constants, each asserted to its SHA-256 (`mode_files`, lines 1386 to 1400), after §0.4's floors; each is installed byte for byte, `sysctl -p` sets `vm.swappiness` now, and journald is restarted onto its new limits. *rsyslog:* disabled and stopped, and its socket stopped, where `systemctl cat` finds it installed. *The swap:* only after the files part's `exit=0` and where `/swapfile` is absent — 1 GiB written whole, `0600` from its first byte, formatted, its `fstab` line appended once after a newline the file may lack, and proved from that line by `swapoff` and `swapon -a`. The Architect ran the block on Ubuntu 24.04.5 under Python 3.12.3, with a stand-in for `systemctl` and `python3.12` for `python3`, which is 3.13 there: `files exit=0`, `rsyslog exit=0`, `swap exit=0`, and `/proc/swaps` listing `/swapfile`, `file`, `1048572` KiB (§10).

### 3.8 G-SWAP, G-LOG and the host after

`L verify 61-verify` (`mode_verify`, lines 1423 to 1476): **G-SWAP** (§4.5) and **G-LOG** (§4.6) — `exit=0` both PASS, `exit=4` otherwise, every check's line printed. Then `L` of `host after` into `62-host-after`: the live host gate again, its facts after the change and G-SPEC again, printed.

### 3.9 The live host's logs, and the closing reads

Into `80-live-copy.log`:

```
scp -q -r -o BatchMode=yes -o LogLevel=QUIET live-host:/root/tz47-work/logs /root/tz47-work/live-logs; echo "scp exit=$?"
diff <(R 'cd /root/tz47-work/logs && sha256sum *') <(cd /root/tz47-work/live-logs && sha256sum *); echo "diff exit=$?"
ls -la /root/tz47-work/live-logs
```

`scp exit=0` and `diff exit=0`: every log of the live host on the capture host, byte for byte. Then into `90-closing.log`:

```
R 'date -u; swapon --show --bytes; free -b; df -B1 --output=source,size,avail /; systemctl is-active systemd-journald.service rsyslog.service syslog.socket; systemctl is-enabled rsyslog.service; journalctl --disk-usage; ls -la /etc/systemd/journald.conf.d /etc/sysctl.d/zz-btc-5m-twap-swap.conf'
TZ=UTC systemctl show btc-recorder.service btc-rewardbook.service adv3-bot.service btc-rewardbook-archive.service btc-rewardbook-archive.timer -p Id -p MainPID -p NRestarts -p ActiveState -p UnitFileState -p ActiveEnterTimestamp
df -B1 --output=source,size,avail /var/lib/btc-recorder; du -sb /root/tz47-work /var/lib/btc-rewardbook; free -b
git -C /root/btc-5m-twap ls-remote origin refs/heads/tz-47-live-host
```

Every line is quoted. **The capture host's units read as at §0.3** — the same `MainPID`, `NRestarts` and `ActiveState` — or the report names the cause from their journal: this TZ touches none of them. Then contract §4.2's self-check, `C` the branch's commit, into `99-selfcheck.log`:

```
git -C /root/btc-5m-twap fetch origin
git -C /root/btc-5m-twap rev-list origin/main | grep -c "$C"
git -C /root/btc-5m-twap diff --name-only origin/main origin/tz-47-live-host
git -C /root/btc-5m-twap diff --numstat origin/main origin/tz-47-live-host
git -C /root/btc-5m-twap ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
```

Then the report is drafted (§8), and §9 runs.

---

## 4. The gates — fixed here, before any of their data exists

| gate | population | PASS | false failure | power, against |
|---|---|---|---|---|
| **G-GEO** | the geoblock reads of the live host, IPv4, and IPv6 where §1.5 says | every family read: status 200, `blocked` the boolean `false`, `country` two capital letters | `0`: the venue's own reading of the address | `1`: an address the venue blocks or restricts to closing; an unreadable reply BLOCKS as well |
| **G-SPEC** | the live host's `MemTotal` and its root file system's size | at least `1,800,000,000` and `18,000,000,000` bytes | `0`: exact reads | `1`: either under nine tenths of what was sold |
| **G-NET** | the CLOB's root, its `/time` and the market websocket's handshake, from the live host | each passes at one of at most three reads 30 s apart | a fault of the venue or the path lasting a minute [not measured] | `1`: a host the venue's edge refuses or cannot be reached from |
| **G-LAT** | the counted replies of the probe: the 600 after the warm-up | at least 570 valid, and their nearest-rank median time to the first byte at most `100,000,000` ns | not measured: the two halves' medians are printed beside it as its spread | `1` against a route whose median is above 100 ms by more than the halves differ; **UNDECIDABLE** under 570 valid |
| **G-SWAP** | the live host after B-CONFIGURE | six checks, §4.5 | `0`: exact reads | `1`: any one of the six |
| **G-LOG** | the live host after B-CONFIGURE | six checks, §4.6 | `0`: exact reads | `1`: any one of the six |

### 4.1 G-GEO

`mode_geoblock` (lines 1213 to 1229) over `geo_read` (lines 1180 to 1210), `geo_reading` (lines 578 to 585) and `geo_overall` (lines 588 to 592). A family is read where the host has an address in it — IPv4 always, IPv6 where `/proc/net/if_inet6` lists a global address (`has_global_ipv6`, lines 1175 to 1177) and `polymarket.com` resolves in it — at most three times 30 s apart while the reply is UNREAD: not status 200, not a JSON object, `blocked` not a boolean, or `country` not two capital letters. **PASS** where every family read passes; **BLOCKED** where one reads `blocked` true; **UNREAD** otherwise. **Both BLOCKED and UNREAD are this TZ's BLOCK** — the Boss's own words, "BLOCK if blocked", and an address the venue did not read is not an address L1 can stand on: `exit=1`, and §0.6 says what runs then.

### 4.2 G-SPEC

`spec_reading` (lines 631 to 635), in `host before` and again in `host after`: `MemTotal` from `/proc/meminfo` at least `1,800,000,000` bytes and the root file system's `f_blocks × f_frsize` at least `18,000,000,000`. `exit=4` on FAIL, which stops nothing but §3.7 (§3).

### 4.3 G-NET

`mode_net` (lines 1246 to 1301) over `net_try` (lines 1232 to 1243), three checks: **N1** — `GET https://clob.polymarket.com/` status 200, its body `"OK"`, a named data centre; **N2** — `GET https://clob.polymarket.com/time` status 200, ten digits, a named data centre and a cache status the origin served, the venue's seconds less the host's printed beside it; **N3** — the websocket handshake with `wss://ws-subscriptions-clob.polymarket.com/ws/market`: status 101 and the accept key its own key asks for (`ws_handshake`, lines 515 to 527). **PASS** where each passes at one of its three reads. `exit=4` on FAIL.

### 4.4 G-LAT

`mode_latency` (lines 1304 to 1333) over `probe` and `lat_reading`, §1.5. Printed beside the reading: the counts of counted, valid, fresh, failed, non-200 and cached replies; the data centres; the 5th, 50th, 95th and 99th percentiles and the maximum; the median of each half of the valid replies in time order; the venue's seconds less the host's, their least and greatest; and **the one-way bound, half the median, against 50.000 ms**. `exit=4` on FAIL or UNDECIDABLE.

### 4.5 G-SWAP

`swap_reading` (lines 671 to 684), six checks: **S1** `/swapfile` a regular file of `1,073,741,824` bytes, mode `0600`, root's; **S2** `/proc/swaps` lists one swap, this file, of type `file`, its size in KiB times 1,024 plus one page — `mkswap`'s header — `1,073,741,824` bytes; **S3** `/etc/fstab`'s lines of swap, every line neither blank nor a comment whose first field is `/swapfile` or whose third is `swap`, exactly one: `/swapfile none swap sw 0 0`; **S4** `SwapTotal` that swap's size; **S5** `vm.swappiness` `10`; **S6** the sysctl file's SHA-256 Appendix A's constant's, `a1b2e411…`, mode `0644`. B-CONFIGURE's `swapoff` and `swapon -a`, chained, make S2 a proof that the `fstab` line activates the swap at a boot.

### 4.6 G-LOG

`log_reading` (lines 728 to 745), six checks: **G1** the journald file's SHA-256 Appendix A's constant's, `0e565d1e…`, mode `0644`; **G2** the running journald's usage message — of its own process, `_PID` its `MainPID` (`journal_usage`, lines 687 to 705) — stamped at or after the journald file's last change, in microseconds: journald read the file at its start; **G3** that message's `MAX_USE` `536,870,912` and `DISK_KEEP_FREE` `2,147,483,648` — journald's own account of the limits in force; **G4** a probe logged with `logger -t tz47-probe` found in the journal and not in the last MiB of `/var/log/syslog`; **G5** rsyslog not installed, or `inactive` and `disabled` or `masked`, and its socket not installed or `inactive`; **G6** every key of the journald file in force from it, by `systemd-analyze cat-config systemd/journald.conf`, each key's last value and the file it comes from (`effective_config`, lines 713 to 725).

### 4.7 The stops — CANON hard rule 14

**This TZ starts no long-lived process and deploys no unit:** nothing it starts outlives it, so it names no unit's stop. **No revert is authorized:** on a FAIL of G-SWAP or G-LOG the live host carries no workload and no key, and the next TZ corrects it from this report; on G-GEO's BLOCK nothing of the live host has been changed but its `authorized_keys` and its work tree, which §9 removes. **Under PASS no block of this section runs.**

### 4.8 What the readings decide — KEEP or REFUND

**The Architect's rule, fixed before any of its data exists:**

- **REFUND** where G-GEO reads BLOCKED or UNREAD — the report is BLOCKED — or G-SPEC or G-NET reads FAIL: the host cannot carry L1, and the Boss returns it inside its seven days.
- **KEEP** where G-GEO, G-SPEC and G-NET read PASS, **whatever G-LAT reads**: rule W's cadence is the venue's one-minute sampling of the book, not a race (CANON PART IV), so G-LAT sets the latency of L1's replay (§1.6 item 6) and does not decide the host. **Discarded:** returning the host on a one-way bound above 50 ms — no other host has been measured against which it could be weighed, and the venue's own region, `eu-west-2`, is in the United Kingdom, a country the venue restricts to closing positions [its geoblock documentation, read 2026-11-18].
- **G-SWAP and G-LOG decide nothing of the refund:** a FAIL is corrected by the next TZ.

### 4.9 What a PASS establishes, and what it does not

The venue reads the live host's address as not blocked; its CLOB, its `/time` and its market websocket answer from there; the host is the memory and disk sold; its swap is 1 GiB, active and in `fstab`; its journal is bounded and the only log store; and its one-way latency to the venue's origin is bounded by half the median measured. **Not established:** that the venue accepts an order from the address — an order needs a key, and its round trip at the minimum size is L1's next TZ (map §7 item 169); that the address stays unblocked — the venue's lists and Bulgaria's regulator can change, and the engine reads the geoblock before it quotes; the latency of an order rather than of `/time`, and of the websocket's frames; and anything about a market.

---

## 5. The instrument

`research/tz47-live-host.py`, Appendix A, fixed by the Architect as this TZ's Validation and written byte for byte. **The standard library alone**, run on the capture host under `/root/tz04a-env` — Python 3.12.3, the captures' interpreter, which nothing here modifies — and on the live host under its system `/usr/bin/python3`, Python 3.12 (LH3). **It loads no other instrument.** It carries its own hook, `policy` (lines 203 to 242), applied by `_audit` (lines 245 to 251) from line 254: writes inside the work tree alone, and into the forensic store by `reclaim`'s exclusive create alone; no file of a capture's store or of the advisor's credentials opened in any mode, and the reward book's store listed by `room` alone; a lookup of a host only where the mode's list names it, and a connection only to an address this process resolved from such a name; and a command only where the mode's list of read-only commands names it — no mode changes the host: B-CONFIGURE does. **Its code:** the TZ's constants (lines 59 to 158); the hook (lines 160 to 254); helpers (lines 256 to 383); the network, IPv4 unless a family is named, every request with this TZ's agent (lines 384 to 528); the readings as pure functions (lines 529 to 798); the capture host's modes (lines 799 to 1003); the live host's modes (lines 1004 to 1477); the self-test and its loopback servers (lines 1478 to 1783); and `main` (lines 1786 to 1810). **Exits:** `0` every assert held; `1` a failed assert, named, or a BLOCK whose message says so; `2` run with `-O`; `4` a reading's FAIL that stops nothing — G-SPEC, G-NET, G-LAT, G-SWAP, G-LOG. Every mode prints, on every exit, its peak memory and the hook's refusals and its counts of lookups, requests, handshakes and TCP connects (lines 1806 to 1809). Run with `-O` it refuses to start (lines 53 to 55). **Each live read is a measurement of its instant and is made once; the pure functions under every reading are checked against literals by the self-test, on both hosts** (contract §6).

---

## 6. Cost

At the populations' upper bounds (§10 C4): `selftest` about 3 s on each host; `fingerprint` under 1 s over 65 rows; `number`, `refs`, `scratch` and `files` about 1 s each; `room` under 1 s over the reward book's store's directory entries — at most the fourteen slots of `PEAK` and their day directories — beside its wait for the archive, at most 30 reads 60 s apart; `reclaim` under 2 s over the work tree, about `20,000,000` bytes without its worktree; `geoblock` under 2 s, at most 120 s a family over three reads, each at its two timeouts of 10 s, 30 s apart — 240 s over both; `net` about 31 s — three requests, then 60 handshakes 0.5 s apart — and at most about 453 s (§3.4); **`latency` about 455 s, at most 540 s by its budget and about 560 s with its last request's two timeouts, under the tool's 600 s**; `host` about 1 s, and at most 300 s with its fifteen commands at their bound of 20 s; `disk` the time to write and sync 256 MiB — 0.38 s in the Architect's rehearsal, about 3 s at 100,000,000 bytes a second — and 200 fsyncs; `verify` under 12 s, its probe waiting at most 10 s, and at most about 350 s with its seventeen commands at their bound of 20 s; B-CONFIGURE the time to write 1 GiB and a journald restart, under 30 s at 100,000,000 bytes a second. **Waits, not compute:** B-ACCESS at most 120 minutes; the room's archive at most 30 minutes; the live host's package manager at most 30 minutes before each of §3.4 to §3.6. **No check reaches `3,600` s of compute.** About 45 minutes of wall clock beside B-ACCESS.

---

## 7. Validation

The report shows each, with its count, and says whether it is asserted:

- **V1** — `FINGERPRINT PASS` at §0.2 and §3.1: revision `2026-11-18-a`; anchors 6, 4 re-derived; rows `65` = `62` + `2` + `1`, 62 `frozen` equal. Asserted.
- **V2** — `NUMBER PASS - 2 of 2` at §0.5 and §3.1; `refs` printed by kind against §0.5's 176 lines, each kind that differs named, `refs/heads/tz-47-live-host` absent before the push. Asserted.
- **V3** — §0.1's script at §0.1 and §3.1: one file, its lines, bytes and SHA-256 of §0.1's table, `created`; the live host's copy the same SHA-256 (§0.6). Asserted by the script and by §0.6's reads.
- **V4** — the branch: one path, `--numstat` `1814 0`, the commit on `origin` the worktree's `HEAD`. Asserted by §3.1's reads.
- **V5** — the capture host gate: H1 to H4, the memory and the disk gate, seven checks; the room and its margin printed. Asserted.
- **V6** — the access: `R true` `exit=0`, at once or within its bound, every read with its instant; the key's fingerprint; the alias's settings without its address; `vs-2348`, `root`, `work tree exit=1`. Asserted by §0.6's reads; B-ACCESS's and B-ACCESS-KEY's handover instants recorded.
- **V7** — the live host gate: LH1 to LH4, four checks, and its floors. Asserted.
- **V8** — `G-GEO PASS` over the families read, each read's line. Asserted; BLOCKED otherwise.
- **V9** — `SELFTEST PASS: 42 checks, 42 passed` on both hosts, `refused by the hook: 1` its own. Asserted.
- **V10** — §3.3: `scratch`'s listing; `RECLAIM PASS` where it named any directory earlier, each removal's `test -e` `exit=1`. Asserted where it runs.
- **V11** — `G-SPEC PASS: 2 of 2` before and after. Printed, exit `0` or `4`.
- **V12** — the package manager's reads before §3.4, §3.5 and §3.6, each with its instant; `G-NET PASS: 3 of 3`, every read's line, and the 60 handshakes' summary. Printed, exit `0` or `4`.
- **V13** — G-LAT's reading, its counts, its percentiles, both halves' medians and the one-way bound against 50.000 ms; every request's line in the report (§8). Printed, exit `0` or `4`.
- **V14** — the disk's write rate and fsync percentiles, its test files removed. Recorded, not asserted.
- **V15** — B-CONFIGURE: `files exit=0`, `rsyslog exit=0`, `swap exit=0`, `/proc/swaps` after `swapon -a`; then `G-SWAP PASS: 6 of 6` and `G-LOG PASS: 6 of 6`. Printed, exit `0` or `4`; skipped with its reason where §3 skips it.
- **V16** — §3.9: `scp exit=0` and `diff exit=0`; the capture host's units as at §0.3, or the cause named; contract §4.2's self-check: `0`, one path, `1814 0`, nothing. Asserted where a command asserts it.
- **V17** — every mode's printed peak, each under `35,046,135`, and every memory and free-space read with its instant and its floor. Recorded.
- **V18** — §9: `RECLAIM PASS`; `/root/tz47-work` gone on both hosts, `test -e` `exit=1` each; the capture host's worktrees the primary checkout and `/root/btc-recorder-svc`; the forensic store's count. Asserted where a command asserts it.

---

## 8. The report

`CryptoReports/TZ-47-live-host-report.md`, contract §8's sections in their order. **§2 Measurements** gives, beside §7's lines: **the live host** — `host before` and `host after` whole, side by side where they differ; **the geoblock** — every read's line; **the network** — the package manager's reads, every read of G-NET and the handshakes' summary; **the latency** — G-LAT's summary lines whole and, after them, every request line of `52-latency.log` verbatim in one block, so that the reading is re-derived from the repository (CANON hard rule 16); **the disk**; **B-CONFIGURE's log whole and `verify`'s every line**; **the access** — `06-access.log` whole, the handover instants, and who ran B-ACCESS and B-ACCESS-KEY; **the capture host** — §0.3's and §3.9's reads, the room and its margin; and **every free-space and `MemAvailable` read**, with its instant and its bound. **§6** names every departure, every refusal by the classifier with the block, its words and who ran it, and every block run by the Boss with its instant. The report prints no address of either host, no password and no private key.

---

## 9. Reclaim — both hosts left clean (CANON hard rule 15)

**B-RECLAIM-LIVE**, after §3.9's copy read `diff exit=0` — or, after a BLOCK, after the copy where the live host is reachable — the Executor's first:

```
R 'rm -rf /root/tz47-work; test -e /root/tz47-work; echo "exit=$?"'
```

It must print `exit=1`. **Its paste**, run by the Boss in a terminal on the live host: `rm -rf /root/tz47-work; test -e /root/tz47-work; echo "exit=$?"`. Nothing of the live host's work tree is kept there: its logs are on the capture host byte for byte (§3.9), its copy of the instrument is the stage's by SHA-256, and its two files are the installed ones, whose SHA-256 G-SWAP and G-LOG read. **Kept on the live host:** the swap file, its `fstab` line, the two installed files, rsyslog's state and root's authorized key — this TZ's deployment.

**What the capture host keeps:** `reclaim` copies every regular file of `/root/tz47-work` but the branch worktree's and the self-test's temporary tree's — the logs, the live host's logs and the stage's instrument — into `/root/btc-forensics/` as `tz47-work--<path with / as -->`, by exclusive create, its hash verified; a name already there with the same hash is counted as held, and with another hash is a failed assert; after each copy free space stays at or above `7,400,000,000` bytes or it BLOCKS (`mode_reclaim`, lines 955 to 1002; `RECLAIM_FLOOR`, line 147). **No file of this run is held by a Release**, so none is left to one. The branch worktree is not copied: `reclaim` asserts that `git status --porcelain --ignored` in it prints nothing and that its `HEAD` is its upstream's (`pristine`, lines 939 to 945), so `git worktree remove` needs no `--force` (map §7 item 89). The report's draft in `CryptoReports/` counts as the report. **No `reclaim`'s output is filtered** (map §7 item 119).

**B-RECLAIM-OWN**, last, after B-RECLAIM-LIVE and with the report drafted. **Its output is written to no file; the report quotes it verbatim from the session**, every line of it:

```
cd /root/tz47-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz47-work/wt/research/tz47-live-host.py reclaim /root/tz47-work
cd /root/btc-5m-twap && git -C /root/btc-5m-twap worktree remove /root/tz47-work/wt; echo "exit=$?"
rm -rf /root/tz47-work; echo "exit=$?"
test -e /root/tz47-work; echo "exit=$?"
git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
find /root/btc-forensics -type f | wc -l
df -B1 --output=source,size,avail /var/lib/btc-recorder
```

`reclaim` must print `RECLAIM PASS` before the removals. **Its paste**, where the classifier refuses any line of it — every step chained to the one before it, the removals reached only after `RECLAIM PASS`; its output goes to the Boss's terminal, the tree its log would be in being removed:

```
(cd /root/tz47-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz47-work/wt/research/tz47-live-host.py reclaim /root/tz47-work) && cd /root/btc-5m-twap && git -C /root/btc-5m-twap worktree remove /root/tz47-work/wt && rm -rf /root/tz47-work; test -e /root/tz47-work; echo "exit=$?"; git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list; find /root/btc-forensics -type f | wc -l
```

Where the Boss ran it, the Executor verifies it by its own reads — `test -e /root/tz47-work; echo "exit=$?"`, `git -C /root/btc-5m-twap worktree list`, `find /root/btc-forensics -type f | wc -l` and `sha256sum /root/btc-forensics/tz47-work--*` against the report's hashes — and the report quotes those reads; a refused first attempt is quoted too. The branch `tz-47-live-host` stays on `origin` and as a local ref; only its working tree goes. **Kept on the capture host:** the Executor's key, the alias and the pinned host key — the access — and the forensic store; nothing of the capture was touched.

---

## 10. Pre-send checks

Performed by the Architect on 2026-11-18 against this file, start to end, in a reading separate from its writing. Every committed file was read at `origin/main` `1519f9f12cc8efb26d3e1c857bc43d768cbb1e0f`; Appendix A's file at §0.1's SHA-256.

| # | check | result |
|---|---|---|
| **C1** | scope against body | **Named by the body, each inside §2.** *Repository, written:* `research/tz47-live-host.py` on the branch, `CryptoReports/TZ-47-live-host-report.md` on `main` — §2 item 1. *Repository, read:* this file by §0.1's script; `SYSTEM-MAP.md` and the 65 files of its §0 table by `fingerprint`; `CryptoTZ/` and `CryptoReports/` by `number`; `origin`'s refs by `refs` and §3.1's `ls-remote`; `research/tz33-reward-book-capture.py` line 190 cited, never opened. *Capture host, written:* `/root/tz47-work/**` — the logs, the stage, the worktree, the live host's logs as copied and the self-test's tree — §2 items 2 and 7; `/root/.ssh/live-host`, its `.pub`, the `Host live-host` block of `/root/.ssh/config` and the alias's line of `/root/.ssh/known_hosts` — §2 item 2; `/root/btc-forensics/tz47-work--*` by `reclaim` — §2 item 2; earlier session directories under `/tmp/` by B-RECLAIM-SCRATCH — §2 item 2. *Capture host, read:* §0.0's, §0.3's, §0.6's and §3.9's reads — the clock, `/proc`, `df` and `statvfs` of `/var/lib`, one manifest's path and one commit's count in the recorder's store, `command -v` of the access's four tools, five units' records, `telemetry-watch.service`'s two states, `du` of three trees, `test -e` of two paths, the worktrees, the directory that holds the session's own, root's SSH files by `ssh -G` and `ssh-keygen` — and the reward book's store by its directory entries alone — §2 item 2. *Live host, written:* one line of `authorized_keys`; `/root/tz47-work/**` — the instrument's copy, the logs, `files/`, the self-test's tree and the disk's two test files, each test file removed by its mode; `/swapfile`, one `fstab` line and the two drop-ins; journald restarted, rsyslog disabled and stopped with its socket; `vm.swappiness` and the swap; one journal message — §2 item 3. *Live host, read:* `/proc`, `/sys`'s DMI names, `/etc`'s files, sysctl's and journald's files under `/etc`, `/run`, `/usr/lib`, `/usr/local/lib` and `/lib`, `sshd -T`, `timedatectl`, root's authorized keys by fingerprint, `/var/log` by sizes and the last MiB of `/var/log/syslog`, systemd's records — the package manager's two services among them — and the journal — §2 item 3. *Network:* the geoblock, the CLOB's root and `/time`, the market websocket's handshake and 60 TCP handshakes, from the live host; GitHub and the live host, from the capture host — §2 item 4. **By content class:** no output carries a price, a size, a side, a book hash, a rate, a competitiveness or an outcome of a market — the reward book's store is read by names and sizes, and map §2.6's reserve is not touched; no output carries an address of either host — the geoblock's `ip` compared and never printed, which the self-test asserts of G-GEO's printed fields; the alias's `hostname` line left out by §0.6's filter; `ssh` and `scp` quiet; sockets by class (§2 item 5). **Found and fixed in this reading:** the reads of `telemetry-watch.service`, of the session's directory, of root's SSH files, of `df` and `statvfs`, and of sysctl's and journald's files outside `/etc`, each now named in §2; `ssh`'s and `scp`'s own errors, which name the address, now quiet. |
| **C2** | origin of every expectation | **Every fixed literal of §5 and §7, of two kinds and no third.** *Quoted from a committed artifact, named:* revision `2026-11-18-a`, the six anchors and rows `65` = `62` + `2` + `1` (map §0, counted by an independent parse); `31612203008` and `e3975b5da44c5328adf3bf3914634cd878842c73` (map §6, disk and host identity); `7,300,000,000` (tz33 line 190); `445,535,636` (map §6, disk floors and caps); `58,953,728` and `49,168,384` (map §6, memory); `ccca2df8-…` and `95cf58d2-…` (map §3); the 176 ref lines (`git ls-remote origin`, 2026-11-18 21:34 UTC). *Computed by an implementation independent of the one under test:* the instrument's lines, bytes and SHA-256 by `wc` and `sha256sum`; `--numstat` `1814 0` by `git diff --no-index --numstat`; the journald file's `0e565d1e…`, 410 bytes, and the sysctl file's `a1b2e411…`, 210 bytes, by `sha256sum` over texts written apart from the instrument's constants; `536,870,912` = 512 · 2²⁰ and `2,147,483,648` = 2 · 2³⁰; `1,073,741,824` = 2³⁰ = `1,048,572` · 1,024 + 4,096; `7,795,535,636` = 7,300,000,000 + 445,535,636 + 50,000,000; `3,589,660,928` = 1,073,741,824 + 268,435,456 + 2,147,483,648 + 100,000,000; `7,400,000,000` = 7,300,000,000 + 100,000,000; `42` over `mode_selftest`'s `ok(` calls by `ast`. *Measured by the kernel, not by the code under test:* `29,229,056`, the `ru_maxrss` of the largest of the Architect's runs, and from it `35,046,135` = ⌈29,229,056 · 58,953,728 / 49,168,384⌉ and `70,092,270` = 2 · 35,046,135 — V17 records the peaks against it and asserts nothing. **No expectation depends on a quantity this TZ measures.** Not expectations, and named: `vs-2348` and Ubuntu 24.04, the host's identity, from the Boss's request and his screenshot of its terminal of 2026-11-18; `1,800,000,000` and `18,000,000,000`, G-SPEC's thresholds, nine tenths of the 2 GB and 20 GB he bought; `100,000,000` ns, G-LAT's, twice the replays' 50 ms. |
| **C3** | shape of every diff | **One file, new.** `research/tz47-live-host.py` is absent from `origin/main` (`git cat-file -e` exit `128`): `1814` lines added and `0` removed by `git diff --no-index --numstat`; no committed line is replaced. The report is new on `main`. No other repository file changes. |
| **C4** | cost of every check | At the populations' upper bounds (§6): `selftest` `2.78` to `2.80` s over three runs on these bytes; `fingerprint` under 1 s over 65 files of `3,768,070` bytes and the map's `153,764`; `number` and `scratch` under 1 s; `refs` one `ls-remote`, at most 120 s by `git`'s bound; `room` under 1 s over the store's directory entries — about 22 day directories and at most `PEAK`'s fourteen slots of streams; `reclaim` under 2 s over at most `20,000,000` bytes, hashed twice and copied once; `geoblock` at most 240 s; `net` at most about 453 s; `latency` at most about 560 s; `host` at most 300 s; `disk` about 3 s at `100,000,000` bytes a second; `verify` at most about 350 s; B-CONFIGURE under 30 s. **Waits, not compute:** B-ACCESS at most 120 minutes in calls of at most 570 s; the room at most 30 minutes, in the background; the package manager at most 30 minutes before each of three steps. **No check reaches `3,600` s of compute, and every `L` ends inside the tool's 600 s.** Fail-fast bounds, each derived: `TIMEOUT_S` `10`, connect and read — the venue's edge answered the Architect's rehearsal in a median of 0.124 s, so 10 s is about eighty times a reply; `EDGE_TIMEOUT_S` `2` — a TCP handshake is one round trip; `LAT_BUDGET_S` `540` — 605 requests 0.75 s apart begin within 453 s, and 540 s with the last request's two timeouts ends at about 560 s; `run`'s `20` s — each command reads a small host's configuration or journal, and one past 20 s has hung; `git`'s `120` s — one `ls-remote` of about 176 refs; `TRIES` `3`, `30` s apart — a fault of a minute is outlasted; `ARCHIVE_READS` `30`, `60` s apart — an archive run moves at most `PEAK`, `445,535,636` bytes, up and verified down at the archives' budget of `2,000,000` bytes a second in about 446 s (map §6, GitHub Releases), so 30 minutes holds about four such runs; `MEM_READS` `5`, `60` s apart — map §7 item 137; `PROBE_WAIT_S` `10` — journald writes a `logger` line within a second; B-ACCESS's 120 minutes — map §7 item 132's bound for a hands-on step; the package manager's 30 reads — its runs take minutes [not measured on this host]. |
| **C5** | every count | V1: `65 = 62 + 2 + 1`, over map §0's table at `1519f9f` by an independent parse, equal to `fingerprint`'s. V2: `2 of 2`, over `CryptoTZ/` and `CryptoReports/` at `origin/main` — no `TZ-47-` file today, `TZ-47-live-host.md` alone after the upload; the 176 refs: `HEAD` 1, `main` 1, `tz-*` 22, pull heads 45, `pairbook-streams-*` 59, `rewardbook-streams-*` 42, two annotated tags with their peeled lines 4, two lightweight tags 2. V3: `1` file over Appendix A's fenced blocks, which §0.1's script finds. V4: `1` path. V5: `7` = H1 1 + H2 2 + H3 1 + H4 1 + memory 1 + disk 1. V7: `4` over `live_gate`'s keys. V9: `42` over `mode_selftest`'s `ok(` calls. V11: `2` over `spec_reading`'s keys. V12: `3` over N1 to N3; `60` = `EDGE_N`. V13: `605` = `LAT_WARM` 5 + `LAT_N` 600; `570` = `LAT_VALID_MIN`, 95% of 600. V15: `6` over `swap_reading`'s keys and `6` over `log_reading`'s. §0.4's fourteen slots: `PEAK` = 14 · `31,823,974` (map §2.6). §6's fifteen commands of `host`: 5 `run` and 10 `show` calls; seventeen of `verify`: 7 and at most 10 reads of the probe. |
| **C6** | every population | Each of §4's six gates names its population in its own column. G-LAT's percentiles, maximum and halves: over the valid replies, the halves in time order; its counts over the 600 counted. The handshakes' median, 95th percentile and maximum: over those of the 60 that completed. The disk's rate: over one write of 256 MiB; its fsync percentiles: over 200 appends of 4 KiB. The venue's seconds less the host's: over N2's read and over the valid replies. §0.4's peaks: over the Architect's runs of the instrument and its drafts on Ubuntu 24.04.5 under Python 3.12.3 — `latency` over its full 605 requests against a loopback server, `geoblock`, `net` and a 65-request `latency` against the venue, every other mode on stand-ins. §1.5's rehearsal: 65 requests from a host in the United States. `MemAvailable`'s range: map §6's reads since 2026-10-31. |
| **C7** | every signature and every behaviour | **Committed, read at `1519f9f`:** `research/tz33-reward-book-capture.py` line 190, `STREAM_FLOOR = 7300000000    # free bytes below which no stream opens for a slot` — the only committed code this TZ names; it calls no committed function. **Appendix A's own, each sentence of the body against the lines it cites:** `live_gate` (638 to 644) — four keys, `hostname == LIVE_HOSTNAME`, `osrel.get("ID") == "ubuntu" and osrel.get("VERSION_ID") == "24.04"`, `tuple(pyver[:2]) == (3, 12)`, `not capture_paths`; `spec_reading` (631 to 635) — `mem_total >= SPEC_MEM_MIN`, `disk_total >= SPEC_DISK_MIN`; `geo_reading` (578 to 585) — UNREAD where `status != 200 or f is None or not isinstance(f["blocked"], bool)` or `re.fullmatch(r"[A-Z]{2}", f["country"])` fails; `geo_overall` (588 to 592) — `if any(r == "BLOCKED" for r in readings)`; `lat_reading` (600 to 623) — `if len(valid) < valid_min:` before `return "UNDECIDABLE", st`, then `"PASS" if st["p50"] <= ttfb_max_ns else "FAIL"`; `valid_sample` — `not s["warm"] and not s["fresh"] and s["error"] is None and s["status"] == 200 and s["body_ok"]`, a data centre and `s["cache"] in ORIGIN_CACHE`; `probe` (451 to 481) — `due = start + int(i * gap_s * 1e9)`, `break` once `budget_s` is past; `swap_reading` (671 to 684) — six keys, `swaps[0][2] * 1024 + page == SWAP_BYTES`; `log_reading` (728 to 745) — six keys, `usage["realtime_us"] >= dropin_mtime_us`, `effective.get(k) == (v, JOURNALD_DROPIN) for k, v in settings(JOURNALD_TEXT)`; `journal_usage` (687 to 705) — `e.get("MESSAGE_ID") == USAGE_ID and e.get("JOURNAL_NAME") == "System Journal"`, `e.get("_PID") == str(pid)`, the last kept; `floors` (310 to 323) — `for k in range(1, MEM_READS + 1)`, `assert k < MEM_READS`, `assert avail >= disk_floor`; `mode_room` (873 to 893) — `if state == "inactive":`; `reclaimable` (792 to 797) and `mode_reclaim` (955 to 1002) — `UUID.fullmatch(os.path.basename(tree))`, `"btc-5m-twap" in os.path.basename(os.path.dirname(tree))`, `s - 1 <= b <= s + LIVE_S`, `if os.path.isdir(WT):` before `pristine(WT)`, `open(dest, "xb")`, `avail - size >= RECLAIM_FLOOR`; `mode_net` (1246 to 1301) — `edge_probe(clob[0], 443, EDGE_N, EDGE_GAP_S) if g else []`; `mode_files` (1386 to 1400) — `assert sha256_bytes(data) == want` before the write and `assert h == want` after it. **Found and fixed in this reading:** §0.4 had the memory floor read at every mode that reads the network, where `floors` is called by `host before`, `room`, `latency`, `disk` and `files` alone — §0.4 now names them, and `latency`'s disk bound, `LIVE_WORK_MAX`; §1.5 had "counted" for `lat_reading`'s "valid"; `mode_room` had read `failed` as idle against map §3's `inactive`, and reads `inactive` alone; `mode_latency` printed its spacing at one decimal, `0.8 s`, and prints `0.75 s`. |
| **C8** | every cross-reference | Resolved by reading each referenced text in this session, never from memory. **Map `2026-11-18-a`, the list the header copies (map §7 item 174):** §0, the fingerprint gate and its table; §1 — public, and its TZs to TZ-46; §2.6 — `PEAK`, rule W's 50 ms one-way latency, every day from 2026-11-14 reserved; §2.7, the advisor's token; §3 — the archive's `inactive`, the two worktrees and the two session directories; §5's L1 row and §8, Georgia; §6's rows host, host identity, language, git remote, egress, venue edge — the `User-Agent`, venue geoblock — `eu-west-2`, the `ip` never printed, a live step's address read the same way — disk, disk floors and caps, headroom, the consumer, process supervision — `apt-daily-upgrade.timer` near 06:00 to 06:30 UTC — memory, clock — an offset above 50 ms invalidates a latency claim — sandbox limit — destructive actions, and harness — background output; §7 items 86, 89, 91, 95, 98, 119, 124, 127, 132, 137, 138, 140, 143, 144, 150, 156, 163, 169, 174, 175, 176 and 177, each read whole, its disposition column included, each supporting the sentence that cites it. **Withdrawn in this reading:** item 104, which binds a block timed to a band, and this TZ times none; item 170, which does not describe the fault §1.4 names — CANON §1.5 does. **Items 175, 176 and 178** leave their duties to a TZ before L1's measurement days, not to this one: 175's margin is printed here (§0.3), and nothing of 176 or 178 is the live host's (CANON PART VI). **CANON `2026-11-16-a`:** §1.1, the geoblock and the `User-Agent`; §1.5, the capture's lost evening; PART II, L1; PART IV — one process on a live host of its own, Georgia, the geoblock read first, the reward cadence; PART VI; hard rules 2, 5, 9, 13, 14, 15, 16 and 17. **Contract:** §1 steps 1 to 4, §4, §4.2, §5, §6 — determinism and forensic reconstruction — and §8. **The Boss's words**, compared character by character with his file of 2026-11-18: §1.1's two quotations, §1.6 item 1's two, and §4.1's "BLOCK if blocked" — each equal. **Other texts, read on 2026-11-18:** `docs.polymarket.com/api-reference/geoblock`; `docs.polymarket.com/trading/session-keys`; `help.polymarket.com/en/articles/18323576-withdrawal-allowlist`; systemd `v255`'s `src/journal/journald.c` and `src/journal/journald-server.c`. |

**Performed in the Architect's session, on these bytes,** under Python 3.12.3 on Ubuntu 24.04.5: §0.1's script on this file — the instrument `created` into an empty tree at Appendix A's hash; `selftest`, three runs, `SELFTEST PASS: 42 checks, 42 passed` and `refused by the hook: 1`; `fingerprint` against a clone of `origin/main` at `1519f9f`, `FINGERPRINT PASS`, 62 of 62 `frozen` rows equal; `number`, BLOCKED as it must be before the upload, and `NUMBER PASS - 2 of 2` against a local commit carrying this file; `refs` against `origin`, 176 lines, the branch absent; `room` on a stand-in store, the archive read `inactive`; `scratch` over two stand-in session directories; `reclaim` over the work tree and an earlier stand-in directory, `RECLAIM PASS`, 22 files copied and all 22 held at a second run; with the host's name stood in and stand-ins for `systemctl`, `journalctl`, `logger`, `timedatectl` and `sshd`: `host before` and `host after`, LH1 to LH4 and `G-SPEC PASS: 2 of 2`, `disk`, `files`, B-CONFIGURE's block — `files exit=0`, `rsyslog exit=0`, `swap exit=0`, `/proc/swaps` listing `/swapfile`, `file`, `1048572` KiB — and `verify`, `G-SWAP PASS: 6 of 6` and `G-LOG PASS: 6 of 6`, G6 read from systemd 255's own `systemd-analyze cat-config` with the journald file installed after Ubuntu's `syslog.conf`; `geoblock`, `net` and a 65-request `latency` against the venue from a host in the United States — `G-GEO BLOCKED` there, the BLOCK it must read; `G-NET PASS: 3 of 3`; G-LAT UNDECIDABLE at 60 valid replies, as it must be under 570; B-ACCESS, twice, with stand-ins for `ssh-keygen`, `ssh-copy-id` and `ssh` in a stand-in directory — one key, one `Host live-host` block, `0600`, the address written into the file alone; and `python3 -O`, refused at its start with exit `2`.

**Not performable in this session, and converted to conditions the Executor evaluates and BLOCKS on** (CANON hard rule 13): the capture host — §0.0's readiness, H1 to H4 and the memory and disk gates (§0.3), and §0.5's refs at the run's instant; B-ACCESS and B-ACCESS-KEY against a real second host — §0.6's reads after them, `vs-2348`, `root` and `work tree exit=1`, and its bound; the live host — whether its root password logs in over SSH, B-ACCESS-KEY its fallback; whether the capture host reaches its port 22, the map's egress row naming TCP/443 alone — `R true` and §0.6's bound; the live host gate LH1 to LH4 and its floors; G-GEO from its address, which BLOCKS; whether its systemd and journald behave as systemd 255's source and Ubuntu 24.04.5's packages do — G-LOG's six checks, G2, G3 and G6 among them, read on the host; whether rsyslog is installed — B-CONFIGURE's branch and G5; and the latency from Sofia, which only G-LAT can read.

---

## Appendix A — the instrument, byte for byte

Extracted by §0.1's script; the block's content is the file.

### `research/tz47-live-host.py`

```python file=research/tz47-live-host.py
#!/usr/bin/env python3
"""TZ-47 - the live host: the server in Sofia reached from the capture host over SSH, its swap and its system journal
bounded, and the venue's geoblock, network path and latency, its memory and its disk read from it before any key
exists.

On the capture host, from /root/tz47-work, under /root/tz04a-env:
    fingerprint       map section 0 against the primary checkout
    number            CANON hard rule 2: of the number TZ-47, this TZ's file alone under CryptoTZ/, no report
    refs              origin's refs by kind; no branch of this TZ yet
    room              free space of /var/lib and the reward book's stream files by their directory entries alone,
                      and the margin over its stream floor and PEAK (map section 7 item 175); no threshold
    scratch OWN       the UUID directories beside this session's own, each named live or earlier
    reclaim TREE...   section 9: the work tree's files into the forensic store; an earlier session's directory
                      checked reclaimable
On the live host, from /root/tz47-work, under its system python3:
    host LABEL        the live host gate and the host's facts, before or after B-CONFIGURE; G-SPEC, exit 4 on FAIL
    geoblock          G-GEO: the venue's geoblock read from this host's address; exit 1 BLOCKED where blocked or
                      unread
    net               G-NET: the CLOB's root and time over HTTPS and its market websocket's handshake; exit 4 on FAIL
    latency           G-LAT: the time to the first byte of the CLOB's /time over one kept connection; exit 4 on FAIL
                      or UNDECIDABLE
    disk              the root file system's write rate with fsync, and its fsync latency; no threshold
    files             B-CONFIGURE's two files into files/, from this file's constants
    verify            G-SWAP and G-LOG after B-CONFIGURE; exit 4 on FAIL
On either host:
    selftest          every rule of this file, on literals, temporary trees under the work tree and loopback servers

No mode places, signs or cancels an order, holds or reads a key of any venue, or makes an authenticated request. No
mode prints an address of either host: of the geoblock's reply it prints blocked, country, region and whether the
address the venue saw is the connection's own. No mode opens a file of a capture's store or of the advisor's
credentials. The standard library alone.

Written for CryptoTZ/TZ-47-live-host.md. The TZ is the specification.
"""

import base64
import datetime
import hashlib
import http.client
import http.server
import json
import os
import re
import resource
import shutil
import socket
import ssl
import subprocess
import sys
import threading
import time

if not __debug__:
    sys.stderr.write("tz47: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(2)

PYFILE = "tz47-live-host.py"

# ---- the TZ's constants: none of them is measured by this run -----------------------------------------------

MAP_REVISION = "2026-11-18-a"
ANCHORS = {"A1": "229a944f2d51", "A2": "6c5089330629",
           "A3": "0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable",
           "A4": "6ac6e10aeabc", "A5": "0f6c90451cbd", "A6": "729f0bcdbee3"}
ANCHOR_FILES = {"A2": "research/twap-divergence.py", "A4": "BTC-EXECUTOR-INSTRUCTIONS.md",
                "A5": "research/recorder/recorder.py", "A6": "research/pfair.py"}
MAP_ROWS = {"frozen": 62, "tracked": 2, "reported": 1}
ROW = re.compile(r"^\| `([^`]+)` \| ([0-9,]+|—) \| ([0-9,]+|—) \| (frozen|tracked|reported) \| "
                 r"(?:`([0-9a-f]{64})`|[^|]*) \|$", re.M)
ANCHOR_ROW = re.compile(r"^\| `(A[0-9])` — [^|]*\| `([^`]+)` \|$", re.M)
NUMBER = "TZ-47-"
OWN_TZ = "CryptoTZ/TZ-47-live-host.md"
BRANCH = "tz-47-live-host"

PRIMARY = "/root/btc-5m-twap"
WORK = "/root/tz47-work"
WT = WORK + "/wt"
TMP = WORK + "/selftest-tmp"
FILES = WORK + "/files"
FORENSICS = "/root/btc-forensics"
RB = "/var/lib/btc-rewardbook"
RB_ARCHIVE_SVC = "btc-rewardbook-archive.service"
ARCHIVE_READS, ARCHIVE_WAIT_S = 30, 60
CAPTURE_MARK = "/var/lib/btc-recorder"     # map section 6, host identity: on the capture host alone
PROTECTED = ("/var/lib/btc-recorder", "/var/lib/btc-chainbook", "/var/lib/btc-pairbook", RB,
             "/var/lib/btc-rewardbook-archive", "/var/lib/btc-pairbook-archive", "/var/lib/adv3-bot", "/etc/adv3-bot")
LIVE_HOSTNAME = "vs-2348"
CAPTURE_DISK = "/var/lib"
LIVE_DISK = "/"

UA = "btc-5m-twap-tz47"
HEADERS = (("User-Agent", UA), ("Accept", "application/json"))
GEO_HOST, GEO_PATH = "polymarket.com", "/api/geoblock"
CLOB_HOST, OK_PATH, TIME_PATH = "clob.polymarket.com", "/", "/time"
WS_HOST, WS_PATH = "ws-subscriptions-clob.polymarket.com", "/ws/market"
WS_GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
TIMEOUT_S, READ_MAX = 10, 65536
TRIES, TRY_GAP_S = 3, 30
EDGE_N, EDGE_GAP_S, EDGE_TIMEOUT_S = 60, 0.5, 2
LAT_WARM, LAT_N, LAT_GAP_S, LAT_BUDGET_S = 5, 600, 0.75, 540
LAT_VALID_MIN = 570          # G-LAT reads UNDECIDABLE below 95 in 100 valid replies
TTFB_MAX_NS = 100000000      # G-LAT: twice the replays' one-way latency of 50 ms
ORIGIN_CACHE = ("DYNAMIC", "BYPASS", "MISS", "EXPIRED")    # cf-cache-status values of a reply the origin served

SPEC_MEM_MIN = 1800000000    # G-SPEC: nine tenths of the 2 GB sold
SPEC_DISK_MIN = 18000000000  # ... and of the 20 GB sold

SWAP_PATH = "/swapfile"
SWAP_BYTES = 1073741824
FSTAB_FIELDS = ("/swapfile", "none", "swap", "sw", "0", "0")
SWAPPINESS = 10
JOURNALD_DROPIN = "/etc/systemd/journald.conf.d/zz-btc-5m-twap-limits.conf"
SYSCTL_DROPIN = "/etc/sysctl.d/zz-btc-5m-twap-swap.conf"
JOURNALD_TEXT = ("# btc-5m-twap, TZ-47: the live host's system journal, bounded. Installed byte for byte as\n"
                 "# /etc/systemd/journald.conf.d/zz-btc-5m-twap-limits.conf from research/tz47-live-host.py; "
                 "named to sort\n"
                 "# after every vendor drop-in, so its values win. Sizes in journald's units of 1,024 bytes.\n"
                 "[Journal]\n"
                 "Storage=persistent\n"
                 "SystemMaxUse=512M\n"
                 "SystemKeepFree=2G\n"
                 "SystemMaxFileSize=64M\n"
                 "RuntimeMaxUse=64M\n"
                 "ForwardToSyslog=no\n")
SYSCTL_TEXT = ("# btc-5m-twap, TZ-47: the live host swaps only under memory pressure. Installed byte for byte as\n"
               "# /etc/sysctl.d/zz-btc-5m-twap-swap.conf from research/tz47-live-host.py; named to sort last.\n"
               "vm.swappiness = 10\n")
JOURNALD_SHA256 = "0e565d1efeb454dcbf46c5319ea9d0d310818e8cb91d0908108741ce9ef14143"
SYSCTL_SHA256 = "a1b2e41165a7b3422c2bfda17dce27c50bc40382d08ef66c81f4f733fedab369"
JOURNAL_MAX_USE = 536870912                 # SystemMaxUse=512M, as journald's own MAX_USE field carries it
USAGE_ID = "ec387f577b844b8fa948f33cad9a75e6"   # journald's usage message, SD_MESSAGE_JOURNAL_USAGE in systemd 255
SYSLOG = "/var/log/syslog"
PROBE_TAG = "tz47-probe"
PROBE_WAIT_S = 10

DISK_TEST_BYTES, DISK_CHUNK = 268435456, 1048576
FSYNC_N, FSYNC_BYTES = 200, 4096

STREAM_FLOOR = 7300000000    # research/tz33-reward-book-capture.py line 190
PEAK = 445535636             # fourteen slots of 31,823,974 bytes (TZ-46; map section 6)
MARGIN_WATCH = 1000000000    # map section 7 item 175
SESSION_WRITES = 50000000    # this session's writes on the capture host, at most
CAPTURE_FLOOR = STREAM_FLOOR + PEAK + SESSION_WRITES                       # 7,795,535,636
JOURNAL_KEEP_FREE = 2147483648                                             # SystemKeepFree=2G, DISK_KEEP_FREE
LIVE_WORK_MAX = 100000000
LIVE_FLOOR = SWAP_BYTES + DISK_TEST_BYTES + JOURNAL_KEEP_FREE + LIVE_WORK_MAX   # 3,589,660,928
RECLAIM_FLOOR = STREAM_FLOOR + 100000000
MEM_FLOOR = 70092270         # MemAvailable at a mode's start: twice 35,046,135, the host peak modelled (section 0.4)
MEM_READS, MEM_WAIT_S = 5, 60

UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
DAY_RE = re.compile(r"[0-9]{10}")
RB_STREAM_RE = re.compile(r"([0-9]{10})\.([0-9]+)\.stream\.jsonl\.gz")
STAMP_RE = re.compile(r"[A-Z][a-z]{2} ([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}) UTC")
HEADER_RE = re.compile(r"# (/[^ ]+)")
SETTING_RE = re.compile(r"([A-Za-z]+)=(.*)")
SHOW_ENV = {"TZ": "UTC", "LC_ALL": "C", "SYSTEMD_COLORS": "0", "SYSTEMD_PAGER": ""}
LIVE_S = 60

# ---- the audit hook: TZ-47 section 2 as a pure function, and the hook that applies it -------------------------

MODE = [None]
REFUSED = []
RESOLVED = set()
COUNTS = {"lookups": 0, "requests": 0, "handshakes": 0, "tcp connects": 0}
NET = {"geoblock": (GEO_HOST,), "net": (CLOB_HOST, WS_HOST), "latency": (CLOB_HOST,), "selftest": ("127.0.0.1",)}
EXECS = {"number": ("git",), "refs": ("git",), "room": ("systemctl",), "scratch": ("stat",), "reclaim": ("git", "stat"),
         "host": ("systemctl", "timedatectl", "journalctl", "sshd", "systemd-analyze"),
         "verify": ("systemctl", "journalctl", "logger", "systemd-analyze")}
WRITE_FLAGS = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC
CHANGE_EVENTS = ("os.remove", "os.rename", "os.rmdir", "os.mkdir", "os.truncate", "os.chmod", "os.chown",
                 "os.utime", "os.link", "os.symlink", "shutil.rmtree", "shutil.copyfile")
HOOKED = ("open", "os.listdir", "os.scandir", "socket.getaddrinfo", "socket.connect", "subprocess.Popen") \
    + CHANGE_EVENTS


class GuardError(RuntimeError):
    pass


def _under(p, root):
    return p == root or p.startswith(root + "/")


def _path(p):
    if isinstance(p, bytes):
        p = os.fsdecode(p)
    return os.path.abspath(p) if isinstance(p, str) else None


def _writing(wmode, flags):
    if isinstance(wmode, str):
        return bool(set(wmode) & set("wax+"))
    return isinstance(flags, int) and bool(flags & WRITE_FLAGS)


def _exclusive(wmode, flags):
    if isinstance(wmode, str):
        return "x" in wmode
    return isinstance(flags, int) and bool(flags & os.O_EXCL)


def policy(mode, event, args):
    """None where TZ-47 section 2 allows the event in this mode; otherwise why it is refused. Pure but for the
    addresses this process resolved from an allowed name."""
    if event == "socket.getaddrinfo":
        host = args[0] if args else None
        if isinstance(host, bytes):
            host = host.decode("ascii", "replace")
        return None if host in RESOLVED or host in NET.get(mode, ()) else "a lookup of %r" % (host,)
    if event == "socket.connect":
        addr = args[1] if len(args) > 1 else None
        ok = isinstance(addr, tuple) and bool(addr) and (addr[0] in RESOLVED or addr[0] in NET.get(mode, ()))
        return None if ok else "a connection to %r" % (addr,)
    if event == "subprocess.Popen":
        exe = args[0] if args and args[0] else (args[1][0] if len(args) > 1 and args[1] else None)
        name = os.path.basename(os.fsdecode(exe)) if exe is not None else None
        return None if name in EXECS.get(mode, ()) else "running %r" % (name,)
    p = _path(args[0]) if args else None
    if p is None:
        return None
    if event == "open":
        wm, fl = (args[1] if len(args) > 1 else None), (args[2] if len(args) > 2 else None)
        if any(_under(p, r) for r in PROTECTED):
            return "an open under a capture's store or the advisor's credentials"
        if _writing(wm, fl):
            if _under(p, FORENSICS):
                return None if mode == "reclaim" and _exclusive(wm, fl) else "a write into the forensic store"
            if not _under(p, WORK):
                return "a write outside the work tree"
        return None
    if event in ("os.listdir", "os.scandir"):
        if _under(p, RB):
            return None if mode == "room" else "a listing of the reward book's store"
        return "a listing under a capture's store" if any(_under(p, r) for r in PROTECTED) else None
    paths = [p]
    if event in ("os.rename", "os.link", "os.symlink", "shutil.copyfile") and len(args) > 1:
        paths.append(_path(args[1]))
    for q in paths:
        if q is not None and not _under(q, WORK):
            return "a change outside the work tree"
    return None


def _audit(event, args):
    if event not in HOOKED:
        return
    why = policy(MODE[0], event, args)
    if why is not None:
        REFUSED.append((event, MODE[0]))
        raise GuardError("%s refused in mode %s: %s" % (event, MODE[0], why))


sys.addaudithook(_audit)

# ---- small helpers ------------------------------------------------------------------------------------------


def out(msg):
    sys.stdout.write("[%s] %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    sys.stdout.flush()


def utc(t):
    return datetime.datetime.fromtimestamp(float(t), datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(path, chunk=1 << 20):
    """The SHA-256 and the byte count of a file read as bytes."""
    h, n = hashlib.sha256(), 0
    with open(path, "rb") as fh:
        for b in iter(lambda: fh.read(chunk), b""):
            h.update(b)
            n += len(b)
    return h.hexdigest(), n


def read_text(path, default=None):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except OSError:
        return default


def meminfo(text):
    """The fields of /proc/meminfo in bytes. Pure."""
    found = {}
    for line in text.split("\n"):
        f = line.split()
        if len(f) >= 2 and f[0].endswith(":") and f[1].isdigit():
            found[f[0][:-1]] = int(f[1]) * (1024 if len(f) > 2 and f[2] == "kB" else 1)
    return found


def mem_available():
    return meminfo(read_text("/proc/meminfo", ""))["MemAvailable"]


def fs_bytes(path):
    """Total, available and free bytes of the file system holding `path`."""
    st = os.statvfs(path)
    return st.f_blocks * st.f_frsize, st.f_bavail * st.f_frsize, st.f_bfree * st.f_frsize


def floors(disk, disk_floor, read=mem_available, sleep=time.sleep, statf=fs_bytes):
    """At a mode's start: MemAvailable read up to five times 60 s apart, the first at or above MEM_FLOOR passing;
    the available bytes of `disk` at or above disk_floor."""
    for k in range(1, MEM_READS + 1):
        m = read()
        out("MemAvailable read %d: %d bytes, floor %d" % (k, m, MEM_FLOOR))
        if m >= MEM_FLOOR:
            break
        assert k < MEM_READS, "BLOCKED: MemAvailable below %d at %d reads" % (MEM_FLOOR, MEM_READS)
        sleep(MEM_WAIT_S)
    avail = statf(disk)[1]
    out("available on %s: %d bytes, floor %d" % (disk, avail, disk_floor))
    assert avail >= disk_floor, "BLOCKED: %d bytes available on %s, below %d" % (avail, disk, disk_floor)
    return avail


def run(argv, timeout=20):
    """A command under TZ=UTC and the C locale: (exit, stdout, stderr)."""
    cp = subprocess.run(argv, capture_output=True, text=True, timeout=timeout, env=dict(os.environ, **SHOW_ENV))
    return cp.returncode, cp.stdout, cp.stderr


def show(unit, props):
    """systemctl show: {property: value}."""
    args = ["systemctl", "show", unit]
    for p in props:
        args += ["-p", p]
    rc, so, se = run(args)
    assert rc == 0, "systemctl show %s: %s" % (unit, se.strip())
    kv = {}
    for line in so.split("\n"):
        if "=" in line:
            k, v = line.split("=", 1)
            kv[k] = v
    return kv


def stamp_of(text):
    """An epoch from systemctl's own stamp printed under TZ=UTC; None where it prints none."""
    m = STAMP_RE.fullmatch((text or "").strip())
    if m is None:
        return None
    dt = datetime.datetime.strptime(m.group(1), "%Y-%m-%d %H:%M:%S").replace(tzinfo=datetime.timezone.utc)
    return int(dt.timestamp())


def git(*args, tree=PRIMARY):
    rc, so, se = run(["git", "-C", tree] + list(args), timeout=120)
    assert rc == 0, "git %s: %s" % (" ".join(args), se.strip()[:300])
    return so.strip()


def nearest_rank(vals, p):
    """The p-th percentile of sorted values by nearest rank: the ceil(p n / 100)-th smallest. Pure."""
    assert vals and 0 < p <= 100
    k = -(-p * len(vals) // 100)
    return vals[max(k, 1) - 1]


def ms(ns):
    return "%.3f" % (ns / 1e6)


def record(kind, obj):
    out("RECORD %s %s" % (kind, json.dumps(obj, sort_keys=True, separators=(",", ":"))))


def is_capture_host():
    return os.path.isdir(CAPTURE_MARK)


def is_live_host():
    return socket.gethostname() == LIVE_HOSTNAME and not os.path.exists(CAPTURE_MARK)

# ---- the network: IPv4 unless named, every request with this TZ's agent -------------------------------------


def family_of(addr):
    return socket.AF_INET6 if ":" in addr else socket.AF_INET


def resolve(host, family=socket.AF_INET, port=443):
    """The addresses of `host` in one family, sorted; each is the only address a later connection may use."""
    infos = socket.getaddrinfo(host, port, family, socket.SOCK_STREAM)
    addrs = sorted({ai[4][0] for ai in infos})
    RESOLVED.update(addrs)
    COUNTS["lookups"] += 1
    return addrs


def https_conn(host, addr, timeout=TIMEOUT_S, context=None):
    """An HTTPS connection to `host`, its certificate checked against the name, its socket to `addr` alone."""
    c = http.client.HTTPSConnection(host, 443, timeout=timeout, context=context or ssl.create_default_context())
    c._create_connection = lambda address, timeout=None, source_address=None: socket.create_connection(
        (addr, address[1]), timeout, source_address)
    return c


def request(conn, path):
    """One GET of `path` over `conn`, every header this TZ's: (status, headers, body, time to the first byte in ns,
    fresh, the connection's own source address). Fresh: the exchange opened the connection, so its time holds the
    handshakes. A body longer than READ_MAX closes the connection."""
    fresh = conn.sock is None
    t0 = time.perf_counter_ns()
    conn.request("GET", path, headers=dict(HEADERS))
    src = conn.sock.getsockname()[0] if conn.sock is not None else None
    resp = conn.getresponse()
    t1 = time.perf_counter_ns()
    body = resp.read(READ_MAX)
    if not resp.isclosed():
        conn.close()
    COUNTS["requests"] += 1
    return resp.status, {k.lower(): v for k, v in resp.getheaders()}, body, t1 - t0, fresh, src


def pop_of(ray):
    """The Cloudflare data centre a reply came through: the IATA code after the cf-ray header's last dash. Pure."""
    code = ray.rsplit("-", 1)[1] if isinstance(ray, str) and "-" in ray else ""
    return code if re.fullmatch(r"[A-Z]{3}", code) else ""


def edge_probe(addr, port, n, gap_s, clock=time.perf_counter_ns, sleep=time.sleep):
    """The time of n TCP handshakes with `addr`, gap_s apart, each socket closed at once; None for a failed one."""
    times = []
    for i in range(n):
        if i:
            sleep(gap_s)
        s = socket.socket(family_of(addr), socket.SOCK_STREAM)
        s.settimeout(EDGE_TIMEOUT_S)
        t0 = clock()
        try:
            s.connect((addr, port))
            times.append(clock() - t0)
        except OSError:
            times.append(None)
        finally:
            s.close()
        COUNTS["tcp connects"] += 1
    return times


def probe(make_conn, path, warm, n, gap_s, budget_s, clock=time.perf_counter_ns, wall=time.time, sleep=time.sleep):
    """`path` requested warm + n times over one kept connection, one every gap_s from the first, none begun after
    budget_s: each sample its index, warm and fresh flags, status, time to the first byte, the Cloudflare data
    centre, the cache status, whether the body is ten digits, the venue's seconds and this host's at the reply."""
    conn = make_conn()
    samples = []
    start = clock()
    try:
        for i in range(warm + n):
            now = clock()
            if now - start > budget_s * 1e9:
                break
            due = start + int(i * gap_s * 1e9)
            if due > now:
                sleep((due - now) / 1e9)
            s = {"i": i, "warm": i < warm, "fresh": conn.sock is None, "status": None, "ttfb_ns": None, "pop": "",
                 "cache": "", "body_ok": False, "venue_s": None, "host_s": None, "error": None}
            try:
                status, hdrs, body, ttfb, fresh, _src = request(conn, path)
                s.update(status=status, ttfb_ns=ttfb, fresh=fresh, pop=pop_of(hdrs.get("cf-ray")),
                         cache=(hdrs.get("cf-cache-status") or "").upper())
                txt = body.decode("ascii", "replace").strip()
                if re.fullmatch(r"[0-9]{10}", txt):
                    s.update(body_ok=True, venue_s=int(txt), host_s=int(wall()))
            except (OSError, http.client.HTTPException) as exc:
                s["error"] = type(exc).__name__
                conn.close()
            samples.append(s)
    finally:
        conn.close()
    return samples


def ws_key():
    return base64.b64encode(os.urandom(16)).decode("ascii")


def ws_accept(key):
    return base64.b64encode(hashlib.sha1((key + WS_GUID).encode("ascii")).digest()).decode("ascii")


def ws_request(host, path, key):
    return ("GET %s HTTP/1.1\r\nHost: %s\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Key: %s\r\n"
            "Sec-WebSocket-Version: 13\r\nUser-Agent: %s\r\n\r\n" % (path, host, key, UA)).encode("ascii")


def ws_head(sock, cap=16384):
    """The status code and the headers of a reply's head read from `sock`."""
    buf = b""
    while b"\r\n\r\n" not in buf and len(buf) < cap:
        chunk = sock.recv(4096)
        if not chunk:
            break
        buf += chunk
    lines = buf.split(b"\r\n\r\n", 1)[0].decode("latin-1").split("\r\n")
    m = re.match(r"HTTP/1\.[01] ([0-9]{3})", lines[0]) if lines else None
    hdrs = {}
    for ln in lines[1:]:
        if ":" in ln:
            k, v = ln.split(":", 1)
            hdrs[k.strip().lower()] = v.strip()
    return (int(m.group(1)) if m else None), hdrs


def ws_handshake(sock, host, path):
    """A websocket opening handshake over a connected socket, closed at once with status 1000 where it succeeds:
    (status, whether the reply's accept key is the one this key asks for, the reply's headers). No subscription."""
    key = ws_key()
    sock.sendall(ws_request(host, path, key))
    code, hdrs = ws_head(sock)
    ok = code == 101 and hdrs.get("sec-websocket-accept") == ws_accept(key) \
        and hdrs.get("upgrade", "").lower() == "websocket"
    if code == 101:
        mask, payload = os.urandom(4), (1000).to_bytes(2, "big")
        sock.sendall(bytes([0x88, 0x80 | len(payload)]) + mask + bytes(b ^ mask[i % 4] for i, b in enumerate(payload)))
    COUNTS["handshakes"] += 1
    return code, ok, hdrs

# ---- the readings: pure -------------------------------------------------------------------------------------


def number_reading(names, own):
    """NUMBER, CANON hard rule 2: CryptoTZ/ holds this TZ's file and no other of its number; CryptoReports/ no report
    of it. Pure."""
    tz = [n for n in names if n.startswith("CryptoTZ/" + NUMBER)]
    rp = [n for n in names if n.startswith("CryptoReports/" + NUMBER)]
    return tz == [own] and not rp, tz, rp


def refs_reading(text):
    """origin's refs counted by kind, and whether this TZ's branch is among them. Pure."""
    kinds, branch = {}, False
    for ln in text.split("\n"):
        if "\t" not in ln:
            continue
        ref = ln.split("\t", 1)[1].strip()
        branch = branch or ref == "refs/heads/" + BRANCH
        if ref in ("HEAD", "refs/heads/main"):
            k = ref
        elif ref.startswith("refs/heads/tz-"):
            k = "refs/heads/tz-*"
        elif ref.startswith("refs/pull/"):
            k = "refs/pull/*/" + ref.rsplit("/", 1)[1]
        elif ref.startswith("refs/tags/pairbook-streams-") or ref.startswith("refs/tags/rewardbook-streams-"):
            k = ref.split("-streams-", 1)[0] + "-streams-*" + ("^{}" if ref.endswith("^{}") else "")
        else:
            k = ref
        kinds[k] = kinds.get(k, 0) + 1
    return kinds, branch


def room_reading(avail, streams):
    """The room - available bytes and the reward book's stream files - and its margin over the stream floor and
    PEAK (map section 7 item 175). Pure."""
    room = avail + streams
    return room, room - STREAM_FLOOR - PEAK


def geo_fields(doc):
    """What may be printed of the venue's reply: blocked, country and region, and its keys' names - never the
    address it carries. Pure."""
    if not isinstance(doc, dict):
        return None
    return {"blocked": doc.get("blocked"), "country": doc.get("country"), "region": doc.get("region"),
            "keys": sorted(str(k) for k in doc)}


def geo_reading(status, doc):
    """One geoblock read: UNREAD unless status 200 and a reply whose blocked is a boolean and whose country is two
    capital letters; else BLOCKED where blocked is true, PASS where it is false. Pure."""
    f = geo_fields(doc)
    if status != 200 or f is None or not isinstance(f["blocked"], bool) \
            or not (isinstance(f["country"], str) and re.fullmatch(r"[A-Z]{2}", f["country"])):
        return "UNREAD"
    return "BLOCKED" if f["blocked"] else "PASS"


def geo_overall(readings):
    """G-GEO over the families read: BLOCKED where any reads blocked; PASS where every one passes; else UNREAD."""
    if any(r == "BLOCKED" for r in readings):
        return "BLOCKED"
    return "PASS" if readings and all(r == "PASS" for r in readings) else "UNREAD"


def valid_sample(s):
    return (not s["warm"] and not s["fresh"] and s["error"] is None and s["status"] == 200 and s["body_ok"]
            and s["pop"] != "" and s["cache"] in ORIGIN_CACHE)


def lat_reading(samples, valid_min=LAT_VALID_MIN, ttfb_max_ns=TTFB_MAX_NS):
    """G-LAT. Pure. Counted: every sample after the warm-up. Valid: not fresh, no error, status 200, the body the
    venue's ten digits, a named Cloudflare data centre and a cache status the origin served. UNDECIDABLE below
    valid_min valid samples; else PASS where the nearest-rank median time to the first byte is at most
    ttfb_max_ns, FAIL above it."""
    counted = [s for s in samples if not s["warm"]]
    valid = [s for s in counted if valid_sample(s)]
    st = {"counted": len(counted), "valid": len(valid),
          "fresh": sum(1 for s in counted if s["fresh"]), "errors": sum(1 for s in counted if s["error"]),
          "non-200": sum(1 for s in counted if s["status"] not in (None, 200)),
          "cache other": sum(1 for s in counted if s["status"] == 200 and s["cache"] not in ORIGIN_CACHE)}
    t = sorted(s["ttfb_ns"] for s in valid)
    if t:
        for p in (5, 50, 95, 99):
            st["p%d" % p] = nearest_rank(t, p)
        st["max"] = t[-1]
        h = len(valid) // 2
        st["p50 first half"] = nearest_rank(sorted(s["ttfb_ns"] for s in valid[:h]), 50) if h else None
        st["p50 second half"] = nearest_rank(sorted(s["ttfb_ns"] for s in valid[h:]), 50)
        offs = [s["venue_s"] - s["host_s"] for s in valid]
        st["venue less host, s"] = (min(offs), max(offs))
    if len(valid) < valid_min:
        return "UNDECIDABLE", st
    return ("PASS" if st["p50"] <= ttfb_max_ns else "FAIL"), st


def net_reading(results):
    """G-NET: every check of `results` passed. Pure."""
    return bool(results) and all(results.values())


def spec_reading(mem_total, disk_total):
    """G-SPEC's two checks against what was sold. Pure."""
    checks = {"MemTotal at least %d" % SPEC_MEM_MIN: mem_total >= SPEC_MEM_MIN,
              "the root file system at least %d" % SPEC_DISK_MIN: disk_total >= SPEC_DISK_MIN}
    return all(checks.values()), checks


def live_gate(hostname, osrel, pyver, capture_paths):
    """The live host gate's four checks. Pure."""
    checks = {"LH1 hostname %s" % LIVE_HOSTNAME: hostname == LIVE_HOSTNAME,
              "LH2 Ubuntu 24.04": osrel.get("ID") == "ubuntu" and osrel.get("VERSION_ID") == "24.04",
              "LH3 Python 3.12": tuple(pyver[:2]) == (3, 12),
              "LH4 not the capture host": not capture_paths}
    return all(checks.values()), checks


def os_release(text):
    found = {}
    for ln in text.split("\n"):
        if "=" in ln and not ln.startswith("#"):
            k, v = ln.split("=", 1)
            found[k.strip()] = v.strip().strip('"')
    return found


def proc_swaps(text):
    """The entries of /proc/swaps: (name, type, size KiB, used KiB). Pure."""
    rows = []
    for ln in text.split("\n")[1:]:
        f = ln.split()
        if len(f) >= 5 and f[2].isdigit() and f[3].isdigit():
            rows.append((f[0], f[1], int(f[2]), int(f[3])))
    return rows


def fstab_active(text):
    """The fields of every line of an fstab that is neither blank nor a comment. Pure."""
    return [tuple(ln.split()) for ln in text.split("\n") if ln.strip() and not ln.lstrip().startswith("#")]


def swap_reading(st, swaps, fstab_rows, swap_total, swappiness, sysctl, page):
    """G-SWAP's six checks. `st` the swap file's (regular, size, mode, uid) or None; `swaps` /proc/swaps' entries;
    `swap_total` SwapTotal in bytes; `sysctl` the drop-in's (SHA-256, mode) or None. Pure."""
    one = len(swaps) == 1
    checks = {"S1 the swap file, %d bytes, 0600, root's" % SWAP_BYTES:
                  st is not None and st == (True, SWAP_BYTES, 0o600, 0),
              "S2 one active swap, this file": one and swaps[0][0] == SWAP_PATH and swaps[0][1] == "file"
                  and swaps[0][2] * 1024 + page == SWAP_BYTES,
              "S3 one fstab line": [r for r in fstab_rows if r[:1] == (SWAP_PATH,) or r[2:3] == ("swap",)]
                  == [FSTAB_FIELDS],
              "S4 SwapTotal": one and swap_total == swaps[0][2] * 1024,
              "S5 vm.swappiness %d" % SWAPPINESS: swappiness == SWAPPINESS,
              "S6 the sysctl file": sysctl == (SYSCTL_SHA256, 0o644)}
    return all(checks.values()), checks


def journal_usage(text, pid):
    """journald's own account of its limits: of the usage messages its process `pid` logged for the System
    Journal, in `journalctl -o json` text, the last one's instant in microseconds, MAX_USE, DISK_KEEP_FREE and
    message; None where it logged none. systemd 255 logs one at every start of journald, after "Journal started".
    Pure."""
    found = None
    for ln in text.split("\n"):
        try:
            e = json.loads(ln)
        except ValueError:
            continue
        if isinstance(e, dict) and e.get("MESSAGE_ID") == USAGE_ID and e.get("JOURNAL_NAME") == "System Journal" \
                and e.get("_PID") == str(pid):
            try:
                found = {"realtime_us": int(e["__REALTIME_TIMESTAMP"]), "max_use": int(e["MAX_USE"]),
                         "keep_free": int(e["DISK_KEEP_FREE"]), "message": e.get("MESSAGE")}
            except (KeyError, TypeError, ValueError):
                continue
    return found


def settings(text):
    """The Key=value lines of a configuration text, in order; comments, sections and blank lines left out. Pure."""
    return [tuple(m.groups()) for m in (SETTING_RE.fullmatch(ln.strip()) for ln in text.split("\n")) if m]


def effective_config(text):
    """`systemd-analyze cat-config` text: each key's last value and the file it comes from, files in the order
    journald reads them. A file's header is a line '# ' and its absolute path, alone. Pure."""
    found, current = {}, None
    for ln in text.split("\n"):
        m = HEADER_RE.fullmatch(ln.rstrip())
        if m:
            current = m.group(1)
            continue
        m = SETTING_RE.fullmatch(ln.strip())
        if m:
            found[m.group(1)] = (m.group(2), current)
    return found


def log_reading(dropin, dropin_mtime_us, usage, in_journal, in_syslog, rsyslog, sock, effective):
    """G-LOG's six checks. `dropin` the journald file's (SHA-256, mode) or None, `dropin_mtime_us` its change in
    microseconds; `usage` journal_usage's reading; `rsyslog` and `sock` systemctl show of rsyslog.service and
    syslog.socket; `effective` effective_config's reading. Pure."""
    off = (rsyslog.get("LoadState") == "not-found" or (
        rsyslog.get("ActiveState") == "inactive" and rsyslog.get("UnitFileState") in ("disabled", "masked"))) \
        and (sock.get("LoadState") == "not-found" or sock.get("ActiveState") == "inactive")
    checks = {"G1 the journald file": dropin == (JOURNALD_SHA256, 0o644),
              "G2 the running journald started after it": usage is not None and dropin_mtime_us is not None
                  and usage["realtime_us"] >= dropin_mtime_us,
              "G3 journald's own MAX_USE %d and DISK_KEEP_FREE %d" % (JOURNAL_MAX_USE, JOURNAL_KEEP_FREE):
                  usage is not None and usage["max_use"] == JOURNAL_MAX_USE
                  and usage["keep_free"] == JOURNAL_KEEP_FREE,
              "G4 the probe in the journal alone": in_journal is True and in_syslog is False,
              "G5 rsyslog and its socket off": off,
              "G6 every key of the journald file in force from it": all(
                  effective.get(k) == (v, JOURNALD_DROPIN) for k, v in settings(JOURNALD_TEXT))}
    return all(checks.values()), checks


def addr_class(h):
    """The class of a /proc/net address: any, loopback or other - never the address. Pure."""
    if set(h) == {"0"}:
        return "any"
    if len(h) == 8:
        return "loopback" if bytes.fromhex(h)[3] == 127 else "other"
    if h == "00000000000000000000000001000000":
        return "loopback"
    if len(h) == 32 and h[:24] == "0000000000000000FFFF0000":
        return "loopback" if bytes.fromhex(h[24:])[3] == 127 else "other"
    return "other"


def listening(text, proto):
    """The listening TCP sockets, or the bound UDP sockets, of a /proc/net table: (proto, class, port, inode). Pure."""
    rows = []
    for ln in text.split("\n")[1:]:
        f = ln.split()
        if len(f) < 10 or ":" not in f[1]:
            continue
        if f[3] != ("0A" if proto.startswith("tcp") else "07"):
            continue
        a, port = f[1].split(":")
        rows.append((proto, addr_class(a), int(port, 16), int(f[9])))
    return sorted(set(rows))


def key_fingerprints(text):
    """The type and SHA256 fingerprint of each key line of an authorized_keys file, in ssh-keygen's form; never a
    key's comment. Pure."""
    found = []
    for ln in text.split("\n"):
        f = ln.split()
        for i, w in enumerate(f[:-1]):
            if w.startswith("ssh-") or w.startswith("ecdsa-") or w.startswith("sk-"):
                try:
                    blob = base64.b64decode(f[i + 1], validate=True)
                except ValueError:
                    break
                found.append((w, "SHA256:" + base64.b64encode(hashlib.sha256(blob).digest()).decode().rstrip("=")))
                break
    return found


def reclaimable(tree):
    if tree == WORK:
        return True
    return (tree.startswith("/tmp/") and os.path.isdir(tree) and not os.path.islink(tree)
            and UUID.fullmatch(os.path.basename(tree)) is not None
            and "btc-5m-twap" in os.path.basename(os.path.dirname(tree)))

# ---- the capture host's modes -------------------------------------------------------------------------------


def mode_fingerprint():
    assert is_capture_host(), "BLOCKED: fingerprint runs on the capture host"
    with open(os.path.join(PRIMARY, "SYSTEM-MAP.md"), "rb") as fh:
        raw = fh.read()
    txt = raw.decode("utf-8")
    rev = re.findall(r"^\*\*Revision string:\*\* `([^`]+)`$", txt, re.M)
    assert rev == [MAP_REVISION], "BLOCKED: map revision %r, required %s" % (rev, MAP_REVISION)
    found = dict(ANCHOR_ROW.findall(txt))
    assert found == ANCHORS, "BLOCKED: anchors %r" % found
    for k, rel in sorted(ANCHOR_FILES.items()):
        h = sha256_file(os.path.join(PRIMARY, rel))[0][:12]
        assert h == ANCHORS[k], "BLOCKED: re-derived %s %s, the map %s" % (k, h, ANCHORS[k])
        out("re-derived %s %s sha256[:12] %s equal" % (k, rel, h))
    rows = ROW.findall(txt)
    states = {k: sum(1 for r in rows if r[3] == k) for k in MAP_ROWS}
    assert states == MAP_ROWS and len(rows) == sum(MAP_ROWS.values()), "BLOCKED: rows %r" % states
    for path, lines, nbytes, state, sha in rows:
        with open(os.path.join(PRIMARY, path), "rb") as fh:
            blob = fh.read()
        got = (blob.count(b"\n"), len(blob), sha256_bytes(blob))
        if state == "frozen":
            want = (int(lines.replace(",", "")), int(nbytes.replace(",", "")), sha)
            assert got == want, "BLOCKED: frozen row %s: %r, the map %r" % (path, got, want)
        out("%-48s %6d lines %8d bytes %s %s%s" % (path, got[0], got[1], got[2], state,
                                                  " equal" if state == "frozen" else ""))
    out("SYSTEM-MAP.md %d lines %d bytes sha256 %s" % (raw.count(b"\n"), len(raw), sha256_bytes(raw)))
    out("FINGERPRINT PASS: revision %s; anchors 6 of 6, 4 re-derived; rows %d: frozen %d of %d equal, tracked %d, "
        "reported %d" % (MAP_REVISION, len(rows), states["frozen"], MAP_ROWS["frozen"], states["tracked"],
                         states["reported"]))
    return 0


def mode_number():
    assert is_capture_host(), "BLOCKED: number runs on the capture host"
    names = git("ls-tree", "--name-only", "origin/main", "--", "CryptoTZ/", "CryptoReports/").split("\n")
    ok, tz, rp = number_reading(names, OWN_TZ)
    out("origin/main %s: %d paths under CryptoTZ/ and CryptoReports/; of the number %s: %s and %s" % (
        git("rev-parse", "origin/main"), len(names), NUMBER, tz, rp))
    out("NUMBER %s" % ("PASS - 2 of 2" if ok else "FAIL"))
    assert ok, "BLOCKED: of the number %s, CryptoTZ/ holds %s and CryptoReports/ %s" % (NUMBER, tz, rp)
    return 0


def mode_refs():
    assert is_capture_host(), "BLOCKED: refs runs on the capture host"
    text = git("ls-remote", "origin")
    kinds, branch = refs_reading(text)
    for ln in text.split("\n"):
        if ln.endswith("\tHEAD") or ln.endswith("\trefs/heads/main"):
            out("REF %s" % ln)
    for k in sorted(kinds):
        out("REFS %-40s %d" % (k, kinds[k]))
    out("REFS %d lines; refs/heads/%s %s" % (sum(kinds.values()), BRANCH, "PRESENT" if branch else "absent"))
    assert not branch, "BLOCKED: refs/heads/%s exists on origin already" % BRANCH
    return 0


def rb_streams(root=RB):
    """The reward book's stream files by their directory entries alone: (bytes, files, day directories)."""
    total = files = 0
    with os.scandir(root) as it:
        days = sorted(e.name for e in it if e.is_dir(follow_symlinks=False) and DAY_RE.fullmatch(e.name))
    for d in days:
        with os.scandir(os.path.join(root, d)) as it:
            for e in it:
                if e.is_file(follow_symlinks=False) and RB_STREAM_RE.fullmatch(e.name):
                    total += e.stat(follow_symlinks=False).st_size
                    files += 1
    return total, files, len(days)


def mode_room(sleep=time.sleep):
    """The room, read while the reward book's archive is not running (map section 3, the units): its service read
    up to thirty times 60 s apart; still running at the last read, the room is not read."""
    assert is_capture_host(), "BLOCKED: room runs on the capture host"
    for k in range(1, ARCHIVE_READS + 1):
        state = show(RB_ARCHIVE_SVC, ["ActiveState"]).get("ActiveState")
        out("%s read %d: %s" % (RB_ARCHIVE_SVC, k, state))
        if state == "inactive":
            break
        if k == ARCHIVE_READS:
            out("ROOM not read: the reward book's archive was running at %d reads" % ARCHIVE_READS)
            return 0
        sleep(ARCHIVE_WAIT_S)
    avail = floors(CAPTURE_DISK, CAPTURE_FLOOR)
    streams, files, days = rb_streams()
    room, margin = room_reading(avail, streams)
    out("ROOM: %d bytes available on %s; the reward book's stream files %d bytes in %d files under %d day "
        "directories; the room %d; its margin over STREAM_FLOOR %d and PEAK %d: %d bytes%s" % (
            avail, CAPTURE_DISK, streams, files, days, room, STREAM_FLOOR, PEAK, margin,
            "" if margin >= MARGIN_WATCH else " - BELOW %d (map section 7 item 175)" % MARGIN_WATCH))
    return 0


def proc_start_times():
    """The start instant of every running process whose argv[0] is `claude` or ends in `/claude.exe`."""
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
    rc, so, se = run(["stat", "-c", "%W", path])
    assert rc == 0, se
    return int(so.strip())


def mode_scratch(own):
    """Lists the UUID directories beside `own`, this session's, and names each live or earlier."""
    assert is_capture_host(), "BLOCKED: scratch runs on the capture host"
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
    return 0


def pristine(tree):
    rc, so, _se = run(["git", "-C", tree, "status", "--porcelain", "--ignored"])
    assert rc == 0 and so == "", "reclaim: %s holds %r" % (tree, so[:400])
    head = git("rev-parse", "HEAD", tree=tree)
    up = git("rev-parse", "@{u}", tree=tree)
    assert up == head, "reclaim: %s is at %s, its upstream at %s" % (tree, head, up)
    out("reclaim: %s skipped: no file but its HEAD's, and HEAD %s is its upstream's" % (tree, head))


def tree_count(root):
    n = 0
    for _d, _s, files in os.walk(root):
        n += len(files)
    return n


def mode_reclaim(trees):
    """The work tree's every file but the worktree's into the forensic store, each by exclusive create and its
    SHA-256 checked; an earlier session's directory checked reclaimable and not live, nothing of it copied."""
    assert is_capture_host(), "BLOCKED: reclaim runs on the capture host"
    assert trees and all(reclaimable(t) for t in trees), "reclaim: %r" % (trees,)
    procs = proc_start_times()
    for t in trees:
        if t != WORK:
            b = birth(t)
            owner = [p for p, s, _a in procs if s - 1 <= b <= s + LIVE_S]
            assert not owner, "reclaim: %s belongs to the running process %s" % (t, owner)
    before = tree_count(FORENSICS)
    considered = copied = held = 0
    for tree in trees:
        if tree != WORK:
            n = sum(len(f) for _d, _s, f in os.walk(tree))
            out("reclaim: %s, an earlier session's directory of %d files: nothing of it is kept" % (tree, n))
            continue
        if os.path.isdir(WT):
            pristine(WT)
        for dirpath, dirnames, filenames in os.walk(tree):
            dirnames[:] = sorted(d for d in dirnames if os.path.join(dirpath, d) not in (WT, TMP))
            for name in sorted(filenames):
                path = os.path.join(dirpath, name)
                if os.path.islink(path) or not os.path.isfile(path):
                    continue
                considered += 1
                rel = os.path.relpath(path, tree)
                h = sha256_file(path)[0]
                dest = os.path.join(FORENSICS, os.path.basename(tree) + "--" + rel.replace("/", "--"))
                if os.path.exists(dest):
                    assert sha256_file(dest)[0] == h, "reclaim: %s exists with another sha256" % dest
                    held += 1
                    out("R held   %s %s" % (h, dest))
                    continue
                size, avail = os.path.getsize(path), fs_bytes(FORENSICS)[1]
                assert avail - size >= RECLAIM_FLOOR, "BLOCKED: reclaim: %d bytes available, %s is %d" % (
                    avail, path, size)
                with open(path, "rb") as src, open(dest, "xb") as dst:
                    shutil.copyfileobj(src, dst, 1 << 20)
                assert sha256_file(dest)[0] == h, "reclaim: %s did not copy whole" % dest
                copied += 1
                out("R copied %s %s" % (h, dest))
    after = tree_count(FORENSICS)
    assert after == before + copied, "reclaim: store %d, expected %d" % (after, before + copied)
    out("RECLAIM PASS: %d files considered, %d copied, %d already held; the forensic store %d -> %d files" % (
        considered, copied, held, before, after))
    return 0

# ---- the live host's modes ----------------------------------------------------------------------------------


def assert_live():
    assert is_live_host(), "BLOCKED: this mode runs on the live host %s and nowhere else" % LIVE_HOSTNAME


def sysctl_lines():
    """Every line of a sysctl file that sets vm.swappiness, with its file."""
    files = ["/etc/sysctl.conf"]
    for d in ("/etc/sysctl.d", "/run/sysctl.d", "/usr/local/lib/sysctl.d", "/usr/lib/sysctl.d", "/lib/sysctl.d"):
        if os.path.isdir(d) and not os.path.islink(d):
            files += [os.path.join(d, n) for n in sorted(os.listdir(d)) if n.endswith(".conf")]
    found = []
    for f in files:
        for ln in (read_text(f, "") or "").split("\n"):
            s = ln.strip()
            if "swappiness" in s and not s.startswith("#") and not s.startswith(";"):
                found.append("%s: %s" % (f, s))
    return found


def socket_owners():
    """inode -> the name of a process holding the socket, read from /proc/*/fd."""
    owners = {}
    for pid in (p for p in os.listdir("/proc") if p.isdigit()):
        try:
            comm = read_text("/proc/%s/comm" % pid, "?").strip()
            for fd in os.listdir("/proc/%s/fd" % pid):
                link = os.readlink("/proc/%s/fd/%s" % (pid, fd))
                if link.startswith("socket:["):
                    owners.setdefault(int(link[8:-1]), comm)
        except OSError:
            continue
    return owners


def sshd_lines(keys):
    """Every line of sshd's own files that sets one of `keys`, with its file: what sshd -T would apply, read
    statically."""
    files = ["/etc/ssh/sshd_config"]
    d = "/etc/ssh/sshd_config.d"
    if os.path.isdir(d):
        files += [os.path.join(d, n) for n in sorted(os.listdir(d)) if n.endswith(".conf")]
    found = []
    for f in files:
        for ln in (read_text(f, "") or "").split("\n"):
            w = ln.strip().split()
            if w and w[0].lower() in keys:
                found.append("%s: %s" % (f, ln.strip()))
    return found


def top_rss(n=10):
    rows = []
    for pid in (p for p in os.listdir("/proc") if p.isdigit()):
        st = meminfo(read_text("/proc/%s/status" % pid, "") or "")
        name = [ln.split(None, 1)[1].strip() for ln in (read_text("/proc/%s/status" % pid, "") or "").split("\n")
                if ln.startswith("Name:")]
        if "VmRSS" in st:
            rows.append((st["VmRSS"], int(pid), name[0] if name else "?"))
    return sorted(rows, reverse=True)[:n]


def var_log():
    """/var/log's files: apparent and on-disk bytes, and the eight largest on disk."""
    files, app, disk = [], 0, 0
    for d, _s, names in os.walk("/var/log"):
        for name in names:
            p = os.path.join(d, name)
            try:
                st = os.lstat(p)
            except OSError:
                continue
            app += st.st_size
            disk += st.st_blocks * 512
            files.append((st.st_blocks * 512, os.path.relpath(p, "/var/log")))
    return app, disk, sorted(files, reverse=True)[:8], len(files)


def mode_host(label):
    assert label in ("before", "after"), "host takes before or after"
    osrel = os_release(read_text("/etc/os-release", ""))
    capture = [p for p in (CAPTURE_MARK, PRIMARY) if os.path.exists(p)]
    ok, checks = live_gate(socket.gethostname(), osrel, sys.version_info, capture)
    for k, v in checks.items():
        out("%s: %s" % (k, "PASS" if v else "FAIL"))
    assert ok, "BLOCKED: the live host gate: %s" % [k for k, v in checks.items() if not v]
    if label == "before":
        floors(LIVE_DISK, LIVE_FLOOR)
    mi = meminfo(read_text("/proc/meminfo", ""))
    total, avail, free = fs_bytes(LIVE_DISK)
    vfs = os.statvfs(LIVE_DISK)
    mounts = [ln.split() for ln in read_text("/proc/self/mounts", "").split("\n") if ln.split()[1:2] == ["/"]]
    cpu = [ln.split(":", 1)[1].strip() for ln in read_text("/proc/cpuinfo", "").split("\n")
           if ln.startswith("model name")]
    btime = int([ln for ln in read_text("/proc/stat", "").split("\n") if ln.startswith("btime ")][0].split()[1])
    up = float(read_text("/proc/uptime", "0 0").split()[0])
    u = os.uname()
    out("HOST %s; %s; kernel %s %s; Python %s; processors %d, %s" % (
        socket.gethostname(), osrel.get("PRETTY_NAME"), u.release, u.machine, sys.version.split()[0],
        os.cpu_count(), cpu[0] if cpu else "?"))
    out("HOST vendor %r, product %r" % ((read_text("/sys/class/dmi/id/sys_vendor", "?") or "?").strip(),
                                        (read_text("/sys/class/dmi/id/product_name", "?") or "?").strip()))
    out("HOST booted %s, up %.0f s" % (utc(btime), up))
    out("MEMORY " + ", ".join("%s %d" % (k, mi.get(k, -1)) for k in (
        "MemTotal", "MemAvailable", "MemFree", "Buffers", "Cached", "SwapTotal", "SwapFree")))
    out("DISK / %s %s: total %d, available %d, free %d bytes; inodes %d, free %d" % (
        mounts[-1][0] if mounts else "?", mounts[-1][2] if mounts else "?", total, avail, free, vfs.f_files,
        vfs.f_favail))
    swaps = proc_swaps(read_text("/proc/swaps", ""))
    out("SWAP /proc/swaps %s; %s %s; fstab lines of swap %s" % (
        swaps, SWAP_PATH, "exists" if os.path.exists(SWAP_PATH) else "absent",
        [r for r in fstab_active(read_text("/etc/fstab", "")) if r[2:3] == ("swap",) or r[:1] == (SWAP_PATH,)]))
    out("SWAP vm.swappiness %s; set in %s" % (read_text("/proc/sys/vm/swappiness", "?").strip(), sysctl_lines()))
    for d in ("/etc/systemd/journald.conf.d", "/run/systemd/journald.conf.d", "/usr/lib/systemd/journald.conf.d",
              "/usr/local/lib/systemd/journald.conf.d"):
        if os.path.isdir(d):
            out("JOURNALD %s: %s" % (d, sorted(os.listdir(d))))
    out("JOURNALD journald.conf, set: %s" % [ln.strip() for ln in read_text("/etc/systemd/journald.conf", "").split(
        "\n") if ln.strip() and not ln.strip().startswith("#")])
    rc, so, se = run(["systemd-analyze", "cat-config", "systemd/journald.conf"])
    out("JOURNALD in force, by `systemd-analyze cat-config` exit %d: %s" % (rc, effective_config(so)))
    rc, so, se = run(["journalctl", "--disk-usage", "--no-pager"])
    out("JOURNALD disk usage: %s" % (so.strip() or se.strip()))
    app, disk, largest, nfiles = var_log()
    out("LOGS /var/log: %d files, %d bytes apparent, %d on disk; the largest on disk %s" % (nfiles, app, disk,
                                                                                         largest))
    for unit in ("rsyslog.service", "syslog.socket", "systemd-journald.service", "systemd-timesyncd.service",
                 "chrony.service", "ssh.service", "ssh.socket", "unattended-upgrades.service", "apt-daily.timer",
                 "apt-daily-upgrade.timer"):
        kv = show(unit, ["LoadState", "ActiveState", "SubState", "UnitFileState"])
        out("UNIT %s %s" % (unit, kv))
    rc, so, se = run(["timedatectl", "show"])
    out("CLOCK %s" % {k: v for k, v in (ln.split("=", 1) for ln in so.split("\n") if "=" in ln)
                      if k in ("Timezone", "LocalRTC", "NTP", "NTPSynchronized", "CanNTP")})
    rc, so, se = run(["timedatectl", "timesync-status"])
    out("CLOCK timesync-status exit %d: %s" % (rc, " | ".join(ln.strip() for ln in (so or se).split("\n")
                                                              if ln.strip())))
    rc, so, se = run(["sshd", "-T"])
    keep = ("port", "permitrootlogin", "passwordauthentication", "pubkeyauthentication", "kbdinteractiveauthentication")
    out("SSHD -T exit %d: %s%s" % (rc, [ln for ln in so.split("\n") if ln.split(" ", 1)[0] in keep],
                                   "" if rc == 0 else "; " + se.strip()[:200]))
    out("SSHD set in its files: %s" % sshd_lines(keep))
    out("SSHD authorized keys of root: %s" % key_fingerprints(read_text("/root/.ssh/authorized_keys", "") or ""))
    owners = socket_owners()
    socks = []
    for proto in ("tcp", "tcp6", "udp", "udp6"):
        for p, cls, port, inode in listening(read_text("/proc/net/" + proto, "") or "", proto):
            socks.append("%s %s:%d %s" % (p, cls, port, owners.get(inode, "?")))
    out("SOCKETS listening or bound: %s" % sorted(set(socks)))
    v6 = [ln.split() for ln in (read_text("/proc/net/if_inet6", "") or "").split("\n") if len(ln.split()) >= 6]
    out("NETWORK global IPv6 addresses: %d" % sum(1 for f in v6 if f[3] == "00"))
    out("PROCESSES by resident memory: %s" % ["%s %d %d" % (n, pid, rss) for rss, pid, n in top_rss()])
    reboot = []
    for n in sorted(os.listdir("/etc/apt/apt.conf.d")) if os.path.isdir("/etc/apt/apt.conf.d") else []:
        for ln in (read_text(os.path.join("/etc/apt/apt.conf.d", n), "") or "").split("\n"):
            if "Automatic-Reboot" in ln and not ln.strip().startswith("//"):
                reboot.append("%s: %s" % (n, ln.strip()))
    out("UPGRADES Automatic-Reboot set: %s" % (reboot or "nowhere - the package's default"))
    sok, sch = spec_reading(mi.get("MemTotal", 0), total)
    for k, v in sch.items():
        out("G-SPEC %s: %d, %s" % (k, mi.get("MemTotal", 0) if k.startswith("MemTotal") else total,
                                   "PASS" if v else "FAIL"))
    out("G-SPEC %s" % ("PASS: 2 of 2" if sok else "FAIL"))
    record("host-" + label, {"mem_total": mi.get("MemTotal"), "mem_available": mi.get("MemAvailable"),
                             "swap_total": mi.get("SwapTotal"), "disk_total": total, "disk_available": avail,
                             "swaps": swaps, "spec": sok})
    return 0 if sok else 4


def has_global_ipv6():
    v6 = [ln.split() for ln in (read_text("/proc/net/if_inet6", "") or "").split("\n") if len(ln.split()) >= 6]
    return any(f[3] == "00" for f in v6)


def geo_read(family, sleep=time.sleep):
    """G-GEO over one family: the first read that is not UNREAD, at most TRIES reads TRY_GAP_S apart."""
    name = "IPv6" if family == socket.AF_INET6 else "IPv4"
    r = "UNREAD"
    for k in range(1, TRIES + 1):
        status = doc = own = err = None
        try:
            addrs = resolve(GEO_HOST, family)
            conn = https_conn(GEO_HOST, addrs[0])
            try:
                status, _h, body, ttfb, _fresh, src = request(conn, GEO_PATH)
            finally:
                conn.close()
            try:
                doc = json.loads(body)
            except ValueError:
                doc = None
            own = isinstance(doc, dict) and src is not None and doc.get("ip") == src
        except (OSError, http.client.HTTPException) as exc:
            err = type(exc).__name__
        r = geo_reading(status, doc)
        f = geo_fields(doc)
        out("GEOBLOCK %s read %d: https://%s%s, status %s; blocked %r, country %r, region %r; reply keys %s; the "
            "address the venue saw is this connection's own: %s%s - %s" % (
                name, k, GEO_HOST, GEO_PATH, status, f and f["blocked"], f and f["country"], f and f["region"],
                f and f["keys"], own, (", " + err) if err else "", r))
        if r != "UNREAD":
            return r
        if k < TRIES:
            sleep(TRY_GAP_S)
    return r


def mode_geoblock():
    assert_live()
    families = [socket.AF_INET]
    if has_global_ipv6():
        try:
            resolve(GEO_HOST, socket.AF_INET6)
            families.append(socket.AF_INET6)
        except socket.gaierror as exc:
            out("GEOBLOCK IPv6: this host has a global IPv6 address and %s none (%s): no request of this host goes "
                "to it over IPv6, and IPv6 is not read" % (GEO_HOST, type(exc).__name__))
    readings = [geo_read(f) for f in families]
    g = geo_overall(readings)
    out("G-GEO %s over %s" % (g, ["IPv6" if f == socket.AF_INET6 else "IPv4" for f in families]))
    record("geoblock", {"readings": readings, "reading": g})
    assert g == "PASS", "BLOCKED: G-GEO %s - the venue %s this address" % (
        g, "blocks" if g == "BLOCKED" else "did not read")
    return 0


def net_try(name, fn, sleep=time.sleep):
    for k in range(1, TRIES + 1):
        try:
            ok, line = fn()
        except (OSError, http.client.HTTPException, ssl.SSLError) as exc:
            ok, line = False, type(exc).__name__
        out("%s read %d: %s - %s" % (name, k, line, "PASS" if ok else "FAIL"))
        if ok:
            return True
        if k < TRIES:
            sleep(TRY_GAP_S)
    return False


def mode_net():
    assert_live()
    clob, ws = resolve(CLOB_HOST), resolve(WS_HOST)
    out("DNS %s IPv4: %s; %s IPv4: %s" % (CLOB_HOST, clob, WS_HOST, ws))

    def root():
        conn = https_conn(CLOB_HOST, clob[0])
        try:
            st, h, body, t, _f, _s = request(conn, OK_PATH)
        finally:
            conn.close()
        pop = pop_of(h.get("cf-ray"))
        return st == 200 and body.strip() == b'"OK"' and pop != "", "GET https://%s%s: status %s, body %r, " \
            "data centre %r, %s ms" % (CLOB_HOST, OK_PATH, st, body[:20], pop, ms(t))

    def tim():
        conn = https_conn(CLOB_HOST, clob[0])
        try:
            st, h, body, t, _f, _s = request(conn, TIME_PATH)
        finally:
            conn.close()
        txt, pop, cache = body.decode("ascii", "replace").strip(), pop_of(h.get("cf-ray")), \
            (h.get("cf-cache-status") or "").upper()
        good = re.fullmatch(r"[0-9]{10}", txt) is not None
        off = (int(txt) - int(time.time())) if good else None
        return st == 200 and good and pop != "" and cache in ORIGIN_CACHE, "GET https://%s%s: status %s, ten " \
            "digits %s, data centre %r, cache %r, the venue's seconds less this host's %s" % (
                CLOB_HOST, TIME_PATH, st, good, pop, cache, off)

    def wsh():
        s = socket.create_connection((ws[0], 443), TIMEOUT_S)
        try:
            ss = ssl.create_default_context().wrap_socket(s, server_hostname=WS_HOST)
            try:
                code, good, h = ws_handshake(ss, WS_HOST, WS_PATH)
            finally:
                ss.close()
        finally:
            s.close()
        return good, "wss://%s%s handshake: status %s, accept key %s, data centre %r" % (
            WS_HOST, WS_PATH, code, "valid" if good else "not valid", pop_of(h.get("cf-ray")))

    results = {"N1 the CLOB's root": net_try("N1", root), "N2 the CLOB's time": net_try("N2", tim),
               "N3 the market websocket": net_try("N3", wsh)}
    g = net_reading(results)
    for k, v in results.items():
        out("G-NET %s: %s" % (k, "PASS" if v else "FAIL"))
    out("G-NET %s" % ("PASS: 3 of 3" if g else "FAIL"))
    times = edge_probe(clob[0], 443, EDGE_N, EDGE_GAP_S) if g else []
    ok_t = sorted(t for t in times if t is not None)
    out("EDGE %d TCP handshakes with %s:443, %.1f s apart, after G-NET's PASS alone: %d completed; median %s ms, "
        "p95 %s ms, max %s ms" % (len(times), CLOB_HOST, EDGE_GAP_S, len(ok_t),
                                  ms(nearest_rank(ok_t, 50)) if ok_t else "-",
                                  ms(nearest_rank(ok_t, 95)) if ok_t else "-", ms(ok_t[-1]) if ok_t else "-"))
    record("net", {"edge_ns": times, "results": results, "reading": g})
    return 0 if g else 4


def mode_latency():
    assert_live()
    floors(LIVE_DISK, LIVE_WORK_MAX)
    addr = resolve(CLOB_HOST)[0]
    out("LATENCY https://%s%s over one kept IPv4 connection: %d warm-up and %d counted requests, one every %.2f s, "
        "none begun after %d s" % (CLOB_HOST, TIME_PATH, LAT_WARM, LAT_N, LAT_GAP_S, LAT_BUDGET_S))
    samples = probe(lambda: https_conn(CLOB_HOST, addr), TIME_PATH, LAT_WARM, LAT_N, LAT_GAP_S, LAT_BUDGET_S)
    for s in samples:
        out("S %d %s%s status %s ttfb_us %s pop %s cache %s body %s venue-host %s%s" % (
            s["i"], "warm" if s["warm"] else "count", " fresh" if s["fresh"] else "", s["status"],
            s["ttfb_ns"] // 1000 if s["ttfb_ns"] is not None else "-", s["pop"] or "-", s["cache"] or "-",
            "ok" if s["body_ok"] else "no", (s["venue_s"] - s["host_s"]) if s["body_ok"] else "-",
            (" error " + s["error"]) if s["error"] else ""))
    reading, st = lat_reading(samples)
    pops = {}
    for s in samples:
        if valid_sample(s):
            pops[s["pop"]] = pops.get(s["pop"], 0) + 1
    out("LATENCY counted %d, valid %d (fresh %d, errors %d, non-200 %d, cache not the origin's %d); data centres %s" %
        (st["counted"], st["valid"], st["fresh"], st["errors"], st["non-200"], st["cache other"], pops))
    if st["valid"]:
        out("LATENCY time to the first byte, ms: p5 %s, p50 %s, p95 %s, p99 %s, max %s; p50 of the first half %s, "
            "of the second %s; the venue's seconds less this host's %s" % (
                ms(st["p5"]), ms(st["p50"]), ms(st["p95"]), ms(st["p99"]), ms(st["max"]),
                ms(st["p50 first half"]) if st["p50 first half"] is not None else "-", ms(st["p50 second half"]),
                st["venue less host, s"]))
        out("LATENCY one-way bound, half the median: %s ms, against 50.000 ms" % ms(st["p50"] // 2))
    out("G-LAT %s" % reading)
    record("latency", {"reading": reading, "stats": st})
    return 0 if reading == "PASS" else 4


def write_rate(path, total, chunk, clock=time.perf_counter_ns):
    """The nanoseconds to write `total` bytes of random data in `chunk`s to a new file and fsync it; the file is
    removed."""
    buf = os.urandom(chunk)
    t0 = clock()
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        left = total
        while left > 0:
            left -= os.write(fd, buf[:min(chunk, left)])
        os.fsync(fd)
    finally:
        os.close(fd)
    t1 = clock()
    os.remove(path)
    return t1 - t0


def fsync_times(path, n, size, clock=time.perf_counter_ns):
    """n writes of `size` bytes appended to a new file, each followed by fsync: their nanoseconds; the file removed."""
    buf, times = os.urandom(size), []
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        for _ in range(n):
            t0 = clock()
            assert os.write(fd, buf) == size, "a short write"
            os.fsync(fd)
            times.append(clock() - t0)
    finally:
        os.close(fd)
    os.remove(path)
    return times


def mode_disk():
    assert_live()
    a0 = floors(LIVE_DISK, LIVE_FLOOR)
    ns = write_rate(WORK + "/disk-test.bin", DISK_TEST_BYTES, DISK_CHUNK)
    out("DISK write %d bytes in %d chunks and fsync: %s ms, %d bytes a second" % (
        DISK_TEST_BYTES, DISK_TEST_BYTES // DISK_CHUNK, ms(ns), DISK_TEST_BYTES * 1000000000 // ns))
    t = sorted(fsync_times(WORK + "/fsync-test.bin", FSYNC_N, FSYNC_BYTES))
    out("DISK %d appends of %d bytes, each with fsync: p50 %s ms, p99 %s ms, max %s ms" % (
        FSYNC_N, FSYNC_BYTES, ms(nearest_rank(t, 50)), ms(nearest_rank(t, 99)), ms(t[-1])))
    a1 = fs_bytes(LIVE_DISK)[1]
    out("DISK available before %d, after %d bytes; the test files removed: %s" % (
        a0, a1, not os.path.exists(WORK + "/disk-test.bin") and not os.path.exists(WORK + "/fsync-test.bin")))
    record("disk", {"write_ns": ns, "write_bytes": DISK_TEST_BYTES, "fsync_ns": t})
    return 0


def mode_files():
    assert_live()
    floors(LIVE_DISK, LIVE_FLOOR)
    assert not os.path.exists(FILES), "BLOCKED: %s exists" % FILES
    os.mkdir(FILES)
    for name, text, want in (("journald.conf", JOURNALD_TEXT, JOURNALD_SHA256),
                             ("sysctl.conf", SYSCTL_TEXT, SYSCTL_SHA256)):
        data = text.encode("utf-8")
        assert sha256_bytes(data) == want, "%s is not the text this TZ fixed" % name
        with open(os.path.join(FILES, name), "xb") as fh:
            fh.write(data)
        h, n = sha256_file(os.path.join(FILES, name))
        assert h == want, name
        out("FILES %s %d lines %d bytes sha256 %s" % (name, data.count(b"\n"), n, h))
    return 0


def file_state(path):
    """(SHA-256, mode bits) of a regular file, or None."""
    try:
        st = os.lstat(path)
    except OSError:
        return None
    return (sha256_file(path)[0], st.st_mode & 0o7777) if os.path.isfile(path) and not os.path.islink(path) else None


def syslog_holds(needle, path=SYSLOG, tail=1 << 20):
    """Whether the last `tail` bytes of the syslog file hold `needle`; False where the file is absent."""
    try:
        with open(path, "rb") as fh:
            fh.seek(0, os.SEEK_END)
            fh.seek(max(0, fh.tell() - tail))
            return needle.encode("ascii") in fh.read()
    except FileNotFoundError:
        return False


def mode_verify(sleep=time.sleep):
    assert_live()
    try:
        st = os.lstat(SWAP_PATH)
        sw = (os.path.isfile(SWAP_PATH) and not os.path.islink(SWAP_PATH), st.st_size, st.st_mode & 0o7777,
              st.st_uid)
    except OSError:
        sw = None
    swaps = proc_swaps(read_text("/proc/swaps", ""))
    rows = fstab_active(read_text("/etc/fstab", ""))
    total = meminfo(read_text("/proc/meminfo", "")).get("SwapTotal")
    swappiness = int(read_text("/proc/sys/vm/swappiness", "-1").strip())
    sysctl = file_state(SYSCTL_DROPIN)
    page = os.sysconf("SC_PAGE_SIZE")
    out("SWAP the file %s; /proc/swaps %s; fstab's swap lines %s; SwapTotal %s; vm.swappiness %d; %s %s; page %d" % (
        sw, swaps, [r for r in rows if r[:1] == (SWAP_PATH,) or r[2:3] == ("swap",)], total, swappiness,
        SYSCTL_DROPIN, sysctl, page))
    sok, sch = swap_reading(sw, swaps, rows, total, swappiness, sysctl, page)
    for k, v in sch.items():
        out("G-SWAP %s: %s" % (k, "PASS" if v else "FAIL"))
    out("G-SWAP %s" % ("PASS: 6 of 6" if sok else "FAIL"))
    dropin = file_state(JOURNALD_DROPIN)
    mtime_us = os.lstat(JOURNALD_DROPIN).st_mtime_ns // 1000 if dropin is not None else None
    jd = show("systemd-journald.service", ["ActiveState", "ActiveEnterTimestamp", "MainPID"])
    pid = jd.get("MainPID")
    rc, so, se = run(["journalctl", "-b", "--no-pager", "-o", "json", "-t", "systemd-journald", "_PID=%s" % pid])
    usage = journal_usage(so, pid)
    out("JOURNALD %s %s, changed %s us; journald %s since %s, pid %s; its usage message %s" % (
        JOURNALD_DROPIN, dropin, mtime_us, jd.get("ActiveState"), jd.get("ActiveEnterTimestamp"), pid, usage))
    nonce = "%s-%s" % (PROBE_TAG, os.urandom(8).hex())
    rc, so, se = run(["logger", "-t", PROBE_TAG, "--", nonce])
    assert rc == 0, "logger: %s" % se.strip()
    in_journal = False
    for _k in range(PROBE_WAIT_S):
        rc, so, se = run(["journalctl", "-b", "--no-pager", "-o", "cat", "-t", PROBE_TAG])
        if nonce in so:
            in_journal = True
            break
        sleep(1)
    in_syslog = syslog_holds(nonce)
    rs = show("rsyslog.service", ["LoadState", "ActiveState", "UnitFileState"])
    sk = show("syslog.socket", ["LoadState", "ActiveState", "UnitFileState"])
    rc, so, se = run(["journalctl", "--disk-usage", "--no-pager"])
    out("JOURNALD the probe %s: in the journal %s, in %s %s; rsyslog %s; syslog.socket %s; %s" % (
        nonce, in_journal, SYSLOG, in_syslog, rs, sk, so.strip()))
    rc, so, se = run(["systemd-analyze", "cat-config", "systemd/journald.conf"])
    eff = effective_config(so)
    out("JOURNALD in force, by `systemd-analyze cat-config` exit %d: %s" % (rc, eff))
    lok, lch = log_reading(dropin, mtime_us, usage, in_journal, in_syslog, rs, sk, eff)
    for k, v in lch.items():
        out("G-LOG %s: %s" % (k, "PASS" if v else "FAIL"))
    out("G-LOG %s" % ("PASS: 6 of 6" if lok else "FAIL"))
    record("verify", {"swap": sok, "log": lok})
    return 0 if sok and lok else 4

# ---- the self-test: literals, temporary trees under the work tree and loopback servers ----------------------


class _FakeClob(http.server.BaseHTTPRequestHandler):
    """The CLOB's /time for the self-test: ten digits, a cf-ray of a named data centre and a cache status."""
    protocol_version = "HTTP/1.1"
    cache, close, agents = "DYNAMIC", False, []

    def log_message(self, *args):
        pass

    def do_GET(self):
        _FakeClob.agents.append(self.headers.get("User-Agent"))
        body = b"1795020548"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("cf-ray", "a5c8777a1d416392-SOF")
        self.send_header("cf-cache-status", _FakeClob.cache)
        if _FakeClob.close:
            self.send_header("Connection", "close")
        self.end_headers()
        self.wfile.write(body)


def _fake_ws(server, good, seen):
    """One websocket handshake answered on a loopback socket: the right accept key or a wrong one; the client's
    request and its close frame recorded."""
    conn, _a = server.accept()
    with conn:
        conn.settimeout(5)
        buf = b""
        while b"\r\n\r\n" not in buf:
            buf += conn.recv(4096)
        head = buf.decode("latin-1")
        seen["request"] = head
        key = [ln.split(":", 1)[1].strip() for ln in head.split("\r\n") if ln.lower().startswith("sec-websocket-key")]
        acc = ws_accept(key[0]) if good else ws_accept("x" + key[0])
        conn.sendall(("HTTP/1.1 101 Switching Protocols\r\nUpgrade: websocket\r\nConnection: Upgrade\r\n"
                      "Sec-WebSocket-Accept: %s\r\ncf-ray: 0123456789abcdef-SOF\r\n\r\n" % acc).encode("ascii"))
        try:
            seen["frame"] = conn.recv(16)
        except OSError:
            seen["frame"] = b""


def mode_selftest():
    results = []

    def ok(cond, what):
        results.append((bool(cond), what))
        out("%s %s" % ("ok  " if cond else "FAIL", what))

    if os.path.exists(TMP):
        shutil.rmtree(TMP)
    os.mkdir(TMP)
    try:
        v = list(range(1, 101))
        ok(nearest_rank(v, 5) == 5 and nearest_rank(v, 50) == 50 and nearest_rank(v, 95) == 95
           and nearest_rank(v, 99) == 99 and nearest_rank(v, 100) == 100 and nearest_rank(list(range(600)), 50) == 299,
           "nearest rank: 5, 50, 95, 99 and 100 of 1..100; of 600 values the median is the 300th smallest")

        def smp(i, t, **kw):
            s = {"i": i, "warm": False, "fresh": False, "status": 200, "ttfb_ns": t, "pop": "SOF", "cache": "DYNAMIC",
                 "body_ok": True, "venue_s": 1795020548, "host_s": 1795020548, "error": None}
            s.update(kw)
            return s

        at = [smp(i, 100000000 if i % 2 else 99000000) for i in range(600)]
        at[0]["ttfb_ns"] = 100000000
        r, st = lat_reading([smp(-1, 5, warm=True)] + at)
        ok(r == "PASS" and st["p50"] == 100000000 and st["counted"] == 600 and st["valid"] == 600,
           "G-LAT PASS where the median is 100,000,000 ns exactly; the warm-up not counted")
        above = [dict(s, ttfb_ns=s["ttfb_ns"] + 1) for s in at]
        ok(lat_reading(above)[0] == "FAIL", "G-LAT FAIL where the median is 100,000,001 ns")
        few = at[:569] + [smp(569 + i, 1, cache="HIT") for i in range(31)]
        r, st = lat_reading(few)
        ok(r == "UNDECIDABLE" and st["valid"] == 569 and st["cache other"] == 31,
           "G-LAT UNDECIDABLE at 569 valid of 600: a cached reply is not the origin's")
        bad = [smp(0, 1, fresh=True), smp(1, 1, status=503), smp(2, 1, body_ok=False), smp(3, 1, pop=""),
               smp(4, 1, error="TimeoutError"), smp(5, 1, cache="")]
        ok(not any(valid_sample(s) for s in bad) and valid_sample(smp(6, 1)),
           "a fresh, a 503, a body not ten digits, no data centre, an error and no cache status: none valid")
        ok(ms(100000000) == "100.000" and ms(100000000 // 2) == "50.000" and pop_of("a5c8777a1d416392-SOF") == "SOF"
           and pop_of("nodash") == "" and pop_of("x-sofia") == "" and pop_of(None) == "",
           "milliseconds to three decimals; the data centre from a cf-ray header, and none from a malformed one")
        g = {"blocked": False, "country": "BG", "ip": "192.0.2.1", "region": "22"}
        ok(geo_reading(200, g) == "PASS" and geo_reading(200, dict(g, blocked=True)) == "BLOCKED"
           and geo_reading(403, g) == "UNREAD" and geo_reading(200, dict(g, blocked="false")) == "UNREAD"
           and geo_reading(200, dict(g, country="BGR")) == "UNREAD" and geo_reading(200, None) == "UNREAD"
           and geo_reading(200, {"country": "BG"}) == "UNREAD",
           "G-GEO: PASS, BLOCKED, and UNREAD on a 403, a string, three letters, no body and no blocked")
        ok("ip" not in geo_fields(g) and "192.0.2.1" not in json.dumps(geo_fields(g)) and geo_fields(g)["keys"] ==
           ["blocked", "country", "ip", "region"], "the geoblock's printed fields carry its keys and never the address")
        ok(geo_overall(["PASS"]) == "PASS" and geo_overall(["PASS", "BLOCKED"]) == "BLOCKED"
           and geo_overall(["PASS", "UNREAD"]) == "UNREAD" and geo_overall([]) == "UNREAD",
           "G-GEO over families: one blocked blocks, one unread leaves it unread")
        ok(spec_reading(1800000000, 18000000000)[0] and not spec_reading(1799999999, 18000000000)[0]
           and not spec_reading(1800000000, 17999999999)[0], "G-SPEC at its bounds, and a byte under each")
        osr = os_release('PRETTY_NAME="Ubuntu 24.04.5 LTS"\nID=ubuntu\nVERSION_ID="24.04"\n')
        ok(live_gate(LIVE_HOSTNAME, osr, (3, 12, 3), [])[0]
           and not live_gate("vultr", osr, (3, 12, 3), [])[0]
           and not live_gate(LIVE_HOSTNAME, dict(osr, VERSION_ID="26.04"), (3, 12, 3), [])[0]
           and not live_gate(LIVE_HOSTNAME, osr, (3, 14, 0), [])[0]
           and not live_gate(LIVE_HOSTNAME, osr, (3, 12, 3), [CAPTURE_MARK])[0],
           "the live host gate: four checks, each failing alone")
        swaps1 = ("Filename\tType\tSize\tUsed\tPriority\n"
                  "/swapfile                               file\t\t1048572\t\t0\t\t-2\n")
        ok(proc_swaps(swaps1) == [("/swapfile", "file", 1048572, 0)] and proc_swaps("Filename Type\n") == [],
           "/proc/swaps parsed: one file of 1,048,572 KiB; a header alone is no swap")
        fst = "# /etc/fstab\nUUID=abc / ext4 defaults 0 1\n\n/swapfile none swap sw 0 0\n#/old none swap sw 0 0\n"
        ok(fstab_active(fst) == [("UUID=abc", "/", "ext4", "defaults", "0", "1"), FSTAB_FIELDS],
           "fstab: comments and blank lines left out")
        good = ((True, SWAP_BYTES, 0o600, 0), proc_swaps(swaps1), fstab_active(fst), 1048572 * 1024, 10,
                (SYSCTL_SHA256, 0o644), 4096)
        ok(swap_reading(*good)[0], "G-SWAP PASS on literals: the file, one swap, one fstab line, SwapTotal, "
           "swappiness, the sysctl file")
        variants = [((True, SWAP_BYTES, 0o644, 0),) + good[1:],
                    good[:1] + (proc_swaps(swaps1 + "/dev/vda3 partition 1000 0 -3\n"),) + good[2:],
                    good[:1] + (proc_swaps(swaps1.replace("1048572", "1048576")),) + good[2:],
                    good[:2] + (fstab_active(fst + "/swapfile none swap sw 0 0\n"),) + good[3:],
                    good[:2] + (fstab_active(fst + "/dev/vda3 none swap sw 0 0\n"),) + good[3:],
                    good[:2] + (fstab_active(fst.replace("sw 0 0", "defaults 0 0")),) + good[3:],
                    good[:3] + (1048572 * 1024 + 4096,) + good[4:], good[:4] + (60,) + good[5:],
                    good[:5] + ((SYSCTL_SHA256, 0o600),) + good[6:], good[:5] + (None,) + good[6:]]
        ok(all(not swap_reading(*a)[0] for a in variants) and len(variants) == 10,
           "G-SWAP FAIL on ten wrong readings, each alone")
        def ent(pid, us, name="System Journal", mid=USAGE_ID, mx="536870912", kf="2147483648"):
            return json.dumps({"MESSAGE_ID": mid, "JOURNAL_NAME": name, "_PID": str(pid), "MAX_USE": mx,
                               "DISK_KEEP_FREE": kf, "__REALTIME_TIMESTAMP": str(us), "MESSAGE": "%s is 8.0M" % name})
        jtext = "\n".join([ent(100, 1795020000000001, mx="2036000000"),
                           ent(200, 1795020600100000, name="Runtime Journal"),
                           json.dumps({"MESSAGE": "Journal started", "_PID": "200"}), ent(200, 1795020600223456),
                           "not json", ent(200, 1795020600300000, mid="x" * 32, mx="1")])
        u = journal_usage(jtext, 200)
        ok(u is not None and u["realtime_us"] == 1795020600223456 and u["max_use"] == 536870912
           and u["keep_free"] == 2147483648 and journal_usage(jtext, 100)["max_use"] == 2036000000
           and journal_usage(jtext, 300) is None,
           "journald's usage message: the System Journal's of this process alone, the last one; none of another")
        cat = ("# /etc/systemd/journald.conf\n#  Entries in this file show the compile time defaults.\n[Journal]\n"
               "#Storage=auto\n\n# /usr/lib/systemd/journald.conf.d/syslog.conf\n# /etc/ if the original file "
               "is shipped\n[Journal]\nForwardToSyslog=yes\n\n# %s\n%s" % (JOURNALD_DROPIN, JOURNALD_TEXT))
        eff = effective_config(cat)
        ok(eff["ForwardToSyslog"] == ("no", JOURNALD_DROPIN) and eff["SystemMaxUse"] == ("512M", JOURNALD_DROPIN)
           and effective_config(cat.split("# " + JOURNALD_DROPIN)[0])["ForwardToSyslog"] == (
               "yes", "/usr/lib/systemd/journald.conf.d/syslog.conf"),
           "the merged configuration: each key's last value and its file; a comment beginning '# /' no header")
        rs_off = {"LoadState": "loaded", "ActiveState": "inactive", "UnitFileState": "disabled"}
        sk_off = {"LoadState": "loaded", "ActiveState": "inactive", "UnitFileState": "static"}
        lg = ((JOURNALD_SHA256, 0o644), 1795020599700000, u, True, False, rs_off, sk_off, eff)
        nf = {"LoadState": "not-found"}
        ok(log_reading(*lg)[0] and log_reading(*(lg[:5] + (nf, nf, eff)))[0],
           "G-LOG PASS on literals, rsyslog disabled or not installed")
        lv = [((JOURNALD_SHA256, 0o600),) + lg[1:], lg[:1] + (1795020600223457,) + lg[2:],
              lg[:2] + (dict(u, max_use=536870913),) + lg[3:], lg[:2] + (dict(u, keep_free=0),) + lg[3:],
              lg[:2] + (None,) + lg[3:], lg[:3] + (False,) + lg[4:], lg[:4] + (True,) + lg[5:],
              lg[:5] + (dict(rs_off, ActiveState="active"),) + lg[6:],
              lg[:5] + (dict(rs_off, UnitFileState="enabled"),) + lg[6:],
              lg[:6] + (dict(sk_off, ActiveState="active"),) + lg[7:],
              lg[:7] + (effective_config(cat.split("# " + JOURNALD_DROPIN)[0]),),
              lg[:7] + (dict(eff, SystemMaxUse=("1G", JOURNALD_DROPIN)),)]
        ok(all(not log_reading(*a)[0] for a in lv) and len(lv) == 12,
           "G-LOG FAIL on twelve wrong readings, each alone")
        ok(sha256_bytes(JOURNALD_TEXT.encode()) == JOURNALD_SHA256 and sha256_bytes(SYSCTL_TEXT.encode())
           == SYSCTL_SHA256 and len(JOURNALD_TEXT.encode()) == 410 and len(SYSCTL_TEXT.encode()) == 210,
           "B-CONFIGURE's two files: their SHA-256 and bytes")
        ok(settings(JOURNALD_TEXT) == [("Storage", "persistent"), ("SystemMaxUse", "512M"), ("SystemKeepFree", "2G"),
                                       ("SystemMaxFileSize", "64M"), ("RuntimeMaxUse", "64M"),
                                       ("ForwardToSyslog", "no")] and JOURNALD_TEXT.count("[Journal]") == 1
           and [ln for ln in SYSCTL_TEXT.split("\n") if ln and not ln.startswith("#")] == ["vm.swappiness = 10"],
           "the journald file sets six keys under [Journal]; the sysctl file one")
        ok(number_reading(["CryptoTZ/TZ-46-capture-room.md", OWN_TZ], OWN_TZ)[0]
           and not number_reading(["CryptoTZ/TZ-46-capture-room.md"], OWN_TZ)[0]
           and not number_reading([OWN_TZ, "CryptoTZ/TZ-47-other.md"], OWN_TZ)[0]
           and not number_reading([OWN_TZ, "CryptoReports/TZ-47-live-host-report.md"], OWN_TZ)[0],
           "NUMBER: this TZ's file alone; absent, a second of the number, a report of it")
        refs = ("a\tHEAD\nb\trefs/heads/main\nc\trefs/heads/tz-46-capture-room\nd\trefs/pull/46/head\n"
                "e\trefs/tags/rewardbook-streams-1795008620\nf\trefs/tags/pairbook-streams-1794925184\n"
                "g\trefs/tags/tz-27-pairbook-streams\nh\trefs/tags/tz-27-pairbook-streams^{}\n")
        kinds, br = refs_reading(refs)
        ok(not br and kinds["refs/heads/tz-*"] == 1 and kinds["refs/tags/rewardbook-streams-*"] == 1
           and kinds["refs/tags/tz-27-pairbook-streams^{}"] == 1 and sum(kinds.values()) == 8
           and refs_reading(refs + "i\trefs/heads/tz-47-live-host\n")[1],
           "refs by kind, eight lines; this TZ's branch found where it exists")
        ok(room_reading(10000000000, 100000000) == (10100000000, 10100000000 - 7300000000 - 445535636)
           and CAPTURE_FLOOR == 7795535636 and LIVE_FLOOR == 3589660928 and PEAK == 14 * 31823974,
           "the room and its margin; the floors 7,795,535,636 and 3,589,660,928; PEAK fourteen slots")
        tcp = ("  sl  local_address rem_address   st tx_queue rx_queue tr tm->when retrnsmt   uid  timeout inode\n"
               "   0: 00000000:0016 00000000:0000 0A 00000000:00000000 00:00000000 00000000     0        0 1001\n"
               "   1: 3500007F:0035 00000000:0000 0A 00000000:00000000 00:00000000 00000000   991        0 1002\n"
               "   2: 0A0200C0:0016 0B0200C0:C350 01 00000000:00000000 00:00000000 00000000     0        0 1003\n")
        ok(listening(tcp, "tcp") == [("tcp", "any", 22, 1001), ("tcp", "loopback", 53, 1002)]
           and addr_class("00000000000000000000000001000000") == "loopback" and addr_class("0A0200C0") == "other",
           "listening sockets: ports and classes, an established one left out, no address printed")
        blob = base64.b64encode(b"\x00\x00\x00\x0bssh-ed25519" + b"\x00" * 36).decode()
        fp = key_fingerprints("ssh-ed25519 %s someone@example\n# comment\nfrom=\"x\" ssh-rsa %s y\n" % (blob, blob))
        ok(len(fp) == 2 and fp[0][0] == "ssh-ed25519" and fp[0][1].startswith("SHA256:")
           and "someone" not in json.dumps(fp),
           "authorized keys: type and SHA256 fingerprint, options skipped, comments never printed")
        ok(reclaimable(WORK) and not reclaimable("/root") and not reclaimable("/tmp/x")
           and not reclaimable("/tmp/claude-0/-root-other/1b2c3d4e-0000-0000-0000-000000000000"),
           "reclaim's predicate: the work tree; nothing outside /tmp or beside another project's sessions")
        ok(policy("selftest", "open", (WORK + "/x", "w", 0)) is None
           and policy("selftest", "open", ("/tmp/x", "w", 0)) is not None
           and policy("room", "open", (RB + "/1795000000/1.1.stream.jsonl.gz", "r", 0)) is not None
           and policy("host", "open", ("/etc/adv3-bot/token", "r", 0)) is not None
           and policy("room", "os.scandir", (RB,)) is None and policy("host", "os.scandir", (RB,)) is not None
           and policy("host", "os.scandir", ("/var/lib/btc-recorder",)) is not None
           and policy("reclaim", "open", (FORENSICS + "/a", "xb", 0)) is None
           and policy("reclaim", "open", (FORENSICS + "/a", "wb", 0)) is not None
           and policy("disk", "os.remove", (WORK + "/disk-test.bin",)) is None
           and policy("disk", "os.remove", ("/swapfile",)) is not None,
           "the hook's files: writes under the work tree alone; no store or credential opened; the reward book "
           "listed by room alone; the forensic store by reclaim's exclusive create alone")
        ok(policy("geoblock", "socket.getaddrinfo", (GEO_HOST, 443)) is None
           and policy("geoblock", "socket.getaddrinfo", (CLOB_HOST, 443)) is not None
           and policy("latency", "socket.getaddrinfo", (GEO_HOST, 443)) is not None
           and policy("net", "socket.getaddrinfo", (WS_HOST, 443)) is None
           and policy("host", "socket.getaddrinfo", (CLOB_HOST, 443)) is not None
           and policy("verify", "socket.connect", (None, ("192.0.2.1", 443))) is not None
           and policy("selftest", "socket.connect", (None, ("127.0.0.1", 1))) is None,
           "the hook's network: each mode's hosts alone, and no connection to an address it did not resolve")
        ok(policy("host", "subprocess.Popen", (None, ["sshd", "-T"], None, None)) is None
           and policy("host", "subprocess.Popen", (None, ["swapon"], None, None)) is not None
           and policy("verify", "subprocess.Popen", (None, ["logger", "x"], None, None)) is None
           and policy("latency", "subprocess.Popen", (None, ["curl"], None, None)) is not None
           and policy("files", "subprocess.Popen", (None, ["install"], None, None)) is not None,
           "the hook's commands: each mode's read-only commands alone; nothing changes the host but the blocks")
        try:
            with open("/tmp/tz47-selftest-forbidden", "w") as fh:
                fh.write("x")
            refused = False
        except GuardError:
            refused = True
        ok(refused and not os.path.exists("/tmp/tz47-selftest-forbidden"), "the hook refuses, live, a write "
           "outside the work tree")
        srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), _FakeClob)
        th = threading.Thread(target=srv.serve_forever, daemon=True)
        th.start()
        try:
            port = srv.server_address[1]
            make = lambda: http.client.HTTPConnection("127.0.0.1", port, timeout=5)
            _FakeClob.cache, _FakeClob.close, _FakeClob.agents = "DYNAMIC", False, []
            sm = probe(make, TIME_PATH, 2, 30, 0.01, 30)
            r, st = lat_reading(sm, valid_min=29)
            ok(len(sm) == 32 and sm[0]["fresh"] and not any(s["fresh"] for s in sm[1:]) and r == "PASS"
               and st["valid"] == 30 and set(_FakeClob.agents) == {UA} and len(_FakeClob.agents) == 32,
               "the probe over one kept loopback connection: the first exchange fresh, 30 counted, every request "
               "with this TZ's agent")
            _FakeClob.close = True
            sm = probe(make, TIME_PATH, 2, 10, 0.01, 30)
            ok(all(s["fresh"] for s in sm) and lat_reading(sm, valid_min=1)[0] == "UNDECIDABLE",
               "a server that closes every connection: every exchange fresh, G-LAT UNDECIDABLE")
            _FakeClob.close, _FakeClob.cache = False, "HIT"
            sm = probe(make, TIME_PATH, 0, 5, 0.01, 30)
            ok(lat_reading(sm, valid_min=1)[0] == "UNDECIDABLE", "a cached reply: G-LAT UNDECIDABLE")
            _FakeClob.cache = "DYNAMIC"
            sm = probe(make, TIME_PATH, 0, 50, 0.05, 0.5)
            ok(len(sm) < 50, "no request begun after the budget")
            conn = make()
            st0, h, body, t, fresh, src = request(conn, TIME_PATH)
            conn.close()
            ok(st0 == 200 and body == b"1795020548" and fresh and src == "127.0.0.1"
               and h.get("cf-ray") == "a5c8777a1d416392-SOF", "a request: status, body, headers, fresh and the "
               "connection's own source address")
        finally:
            srv.shutdown()
            srv.server_close()
        times = edge_probe("127.0.0.1", port, 3, 0.0)
        ok(len(times) == 3 and all(t is None for t in times), "TCP handshakes with a closed port: each None")
        for good_key in (True, False):
            ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ls.bind(("127.0.0.1", 0))
            ls.listen(1)
            seen = {}
            th = threading.Thread(target=_fake_ws, args=(ls, good_key, seen), daemon=True)
            th.start()
            c = socket.create_connection(("127.0.0.1", ls.getsockname()[1]), 5)
            code, valid, hdrs = ws_handshake(c, WS_HOST, WS_PATH)
            c.close()
            th.join(5)
            ls.close()
            if good_key:
                ok(code == 101 and valid and "User-Agent: %s\r\n" % UA in seen["request"]
                   and seen["request"].startswith("GET %s HTTP/1.1\r\nHost: %s\r\n" % (WS_PATH, WS_HOST))
                   and seen.get("frame", b"")[:2] == b"\x88\x82" and pop_of(hdrs.get("cf-ray")) == "SOF",
                   "the websocket handshake: 101, its accept key valid, this TZ's agent, closed with a masked "
                   "frame of status 1000")
            else:
                ok(code == 101 and not valid, "a wrong accept key: the handshake not valid")
        p = os.path.join(TMP, "rate.bin")
        ns = write_rate(p, 4 * DISK_CHUNK, DISK_CHUNK)
        ft = fsync_times(p, 5, FSYNC_BYTES)
        ok(ns > 0 and len(ft) == 5 and all(t > 0 for t in ft) and not os.path.exists(p),
           "the disk's write rate and fsync times on a stand-in of 4 MiB and 5 appends, its file removed")
        mi = meminfo("MemTotal:        2014412 kB\nMemAvailable:    1700000 kB\nHugePages_Total:       0\n")
        ok(mi == {"MemTotal": 2014412 * 1024, "MemAvailable": 1700000 * 1024, "HugePages_Total": 0},
           "meminfo in bytes, a count left a count")
        ok(stamp_of("Wed 2026-11-18 10:11:08 UTC") == 1794996668 and stamp_of("") is None and stamp_of("n/a") is None,
           "systemctl's stamp under TZ=UTC")
    finally:
        shutil.rmtree(TMP)
    n_ok = sum(1 for good_, _w in results if good_)
    out("SELFTEST %s: %d checks, %d passed" % ("PASS" if n_ok == len(results) else "FAIL", len(results), n_ok))
    assert n_ok == len(results), "SELFTEST FAIL: %s" % [w for good_, w in results if not good_]
    return 0


def main(argv):
    if not argv:
        sys.exit("usage: %s MODE [ARG...]" % PYFILE)
    mode, rest = argv[0], argv[1:]
    assert os.getcwd() == WORK, "run from %s, not %s" % (WORK, os.getcwd())
    MODE[0] = mode
    table = {"fingerprint": mode_fingerprint, "number": mode_number, "refs": mode_refs, "room": mode_room,
             "geoblock": mode_geoblock, "net": mode_net, "latency": mode_latency, "disk": mode_disk,
             "files": mode_files, "verify": mode_verify, "selftest": mode_selftest}
    one = {"scratch": mode_scratch, "host": mode_host}
    rc = 1
    try:
        if mode == "reclaim":
            rc = mode_reclaim(rest)
        elif mode in one:
            assert len(rest) == 1, "%s takes one argument" % mode
            rc = one[mode](rest[0])
        else:
            assert mode in table and not rest, "unknown mode %r" % (argv,)
            rc = table[mode]()
    finally:    # printed on every exit, a BLOCK's and a failed assert's included
        out("peak memory of this run: %d bytes" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024))
        out("refused by the hook: %d; lookups %d, requests %d, handshakes %d, TCP connects %d" % (
            len(REFUSED), COUNTS["lookups"], COUNTS["requests"], COUNTS["handshakes"], COUNTS["tcp connects"]))
    return rc or 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
```
