# TZ-46 — the capture's room: the reward book's streams kept above their floor through every evening — its archive every three hours, the pair book stopped after its last archive run, the forensic copies a public Release holds removed

**Canonical filename:** `TZ-46-capture-room.md`. The committed file takes this name and no other.

**Executor model: Claude Opus 5.5.** A capture stopped, a running archive's timer replaced beside it, a forensic store pruned by proof, every block held to another unit's clock.

**Required System Map revision:** `2026-11-16-a` — `main` at `53e5690`, PR #45's merge, above `4342383`, which carries it; the Boss's request named it with its §6 disk rows and its §7 item 170. **No map revision ships with this TZ.** Its merge replaces map §0's `frozen` row of `deploy/systemd/btc-rewardbook-archive.timer`, TZ-34's `bf5af025…`, and lands with the map revision that carries Appendix A's: no other TZ is uploaded between this one's upload and its report (CANON hard rule 17), and from B-TIMER to the merge the host's timer is ahead of `main`.

**Map sections this TZ rests on**, copied from §10's C8 (map §7 item 141): §0, the fingerprint gate and its table; §1, the refs; §2.5, the pair book, its archive, its idle stretch, its restart and the reserve; §2.6, the reward book — its store's bounds as its code reads them, its archive, the reserve; §3, the forensic store, the worktrees and the code trees; §6, its rows host, host identity, language, git remote, both disk rows, capture cost, headroom, process supervision, memory, GitHub Releases, sandbox limit — network, sandbox limit — destructive actions, and harness; §7 items 106, 115, 119, 120, 124, 125, 128, 129, 131, 132, 137, 138, 140, 141, 143, 144, 150, 156, 166, 167 and 170.

**Required anchors**, from map §0. A mismatch on any one is BLOCKED before any work:

| anchor | required |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `0f6c90451cbd` |
| `A6` — pricer | `729f0bcdbee3` |

**Host gate:** §0.3. This TZ runs on the capture host and nowhere else: it changes that host's units and stores.

**Before `EXECUTE TZ-46`:** the Boss uploads this file into `CryptoTZ/`, and nothing else. No step of his is a precondition of the run (map §7 item 132). **He is needed at the VPS only for a block the session's classifier refuses** (§3), each handed over as one paste.

**When: on any day from the upload, begun between 07:30:00 and 17:30:00 UTC — 11:30 to 21:30 in Batumi.** §0.0 reads the clock, both archives' ledgers, the units and the free space before anything else and, outside that band, with an archive halted or its last run not ended, a unit down or the disk short, begins nothing and owes no report: it is tried again later, and no start can spend this TZ. 07:30 is clear of the package manager's morning run (map §7 item 143). B-PAIR-OFF runs inside 07:30:00 to 19:00:00 UTC; B-TIMER waits for one of four bands, 25 to 10 minutes before an elapse of the new calendar — 10:05:20 to 10:20:20, 13:05:20 to 13:20:20, 16:05:20 to 16:20:20 or 19:05:20 to 19:20:20 UTC. **Fewest idle minutes: begun about 75 minutes before one of those bands** — at 08:50, 11:50 or 14:50 UTC, or by 17:30 for the band of 19:05 — because §0 to §3.5 take about 30 minutes and B-PAIR-OFF's last run of the pair book's archive 20 to 45. About 2 to 5 h of the session's wall clock in all (§6).

**What this TZ is.** L1 compares the venue's payouts to an address of ours with a replay of the same days, and a replay needs every slot's stream (CANON PART II; map §7 item 170). **The reward book lost its evening to the disk:** from 21:15 UTC on 2026-11-13 it opened no stream, every slot record naming the floor, until its archive's night run freed the room — measured (map §2.6, §6 disk). This TZ gives the capture its room by three changes, each measured, none touching another project, and proves them on the host: **(a)** the pair book's archive runs once more, by hand, and then the pair book and its archive's timer are stopped and disabled — the largest term of the daily wave, a capture no open question reads (§1); **(b)** the reward book's archive's timer runs it every three hours, `*-*-* 01/3:30:20 UTC`, with no run on a start of the timer (map §7 item 166), so its store never holds more than fourteen slots of stream; **(c)** the forensic store's files that a public Release holds by bytes and SHA-256 — TZ-44's thirteen among them (map §7 item 167) — are removed, each proved first by the Release's own record and a full anonymous download. It deploys and proves its deployment, and measures nothing the deployment is for (CANON hard rule 11): whether L1's days are whole is read by the TZ that measures them, from their slot records. One instrument, `research/tz46-capture-room.py`, and one unit file, `deploy/systemd/btc-rewardbook-archive.timer`, replacing TZ-34's: Appendix A. **No order is placed, no key of any venue is held, and no stream, rewards file or selection of the reward book is opened.**

---

## 0. Gates

### 0.0 The instant and the readiness, then the work tree

After contract §1 steps 1 and 2, and before anything else, in the session — verbatim, read-only, of the archives' state their ledgers alone and of the units their states:

```
/root/tz04a-env/venv/bin/python -B - <<'EOF2'
import json, os, subprocess, time
now = int(time.time()); s = now % 86400
v = os.statvfs("/var/lib"); free = v.f_bavail * v.f_frsize
ready = 27000 <= s <= 63000 and free >= 7600000000
for name in ("rewardbook", "pairbook"):
    with open("/var/lib/btc-%s-archive/ledger.jsonl" % name, encoding="utf-8") as fh:
        recs = [json.loads(ln) for ln in fh.read().split("\n")[:-1] if ln.strip()]
    flags = [r["event"] for r in recs if r.get("event") in ("halt", "clear")]
    halted = bool(flags) and flags[-1] == "halt"
    idx = [i for i, r in enumerate(recs) if r.get("event") == "start"]
    a = recs[idx[-1]]["run"] if idx else None
    ends = [r["event"] for r in recs[idx[-1] + 1:] if r.get("run") == a and r.get("event") in ("complete", "empty", "halt", "deferred")] if idx else []
    last = ends[-1] if ends else "running"
    print("the %s archive: %d records; its last run %s, %s; halted %s" % (name, len(recs), a, last, halted))
    ready = ready and not halted and last in ("complete", "empty")
for u in ("btc-recorder.service", "btc-pairbook.service", "btc-rewardbook.service", "adv3-bot.service", "btc-pairbook-archive.timer", "btc-rewardbook-archive.timer"):
    act = subprocess.run(["systemctl", "is-active", u], capture_output=True, text=True).stdout.strip()
    ena = subprocess.run(["systemctl", "is-enabled", u], capture_output=True, text=True).stdout.strip()
    print("%s %s %s" % (u, act, ena))
    ready = ready and act == "active" and ena == "enabled"
print("ready=%d: second %d of the day, the band 27000 to 63000; %d bytes free, 7600000000 needed; at %d %s" % (ready, s, free, now, time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now))))
EOF2
```

**`ready=1` begins the run. `ready=0`, or a read that ends without its `ready=` line, begins nothing:** no directory is made, nothing is written, committed or pushed and no report is written — this TZ has not executed (CANON hard rule 5) — and the Executor gives the Boss the read's lines as printed and, in one line, in Russian, the next instant to send `EXECUTE TZ-46`: the next 07:30 UTC, or the same day's where only the clock stopped it. This is not BLOCKED and owes no report (contract §5); a later `EXECUTE TZ-46` starts the TZ afresh, as often as it takes. **The read asks of each archive what B-PAIR-OFF and B-TIMER need of it:** not halted — a halted archive refuses every run until a TZ appends a `clear` (map §3), so the pair book's last run could not run, nor the reward book's first on the new calendar — and its last run ended, `complete` or `empty`, so that neither block starts beside a set left pending; **of the units, that the four running units and both timers are active and enabled, as the TZs that deployed them left them; and the disk, `7,600,000,000` bytes free** (§0.4). Then:

```
mkdir /root/tz46-work /root/tz46-work/logs; echo "exit=$?"
```

`exit=0` proves neither existed; anything else is BLOCKED. The readiness read is run again into `logs/00-ready.log`. **From here every command's output goes to `/root/tz46-work/logs/`, one file per step, under the names §3's table fixes**, and nothing to the session's scratchpad; B-RECLAIM-OWN, §9, is the one exception.

Three abbreviations: **`P`** is `nice -n 19 /root/tz04a-env/venv/bin/python -B`; **`I0`** is `P /root/tz46-work/stage/research/tz46-capture-room.py`, the staged copy, for §0 alone; and **`I`**, from §3.1 on, is `P /root/tz46-work/wt/research/tz46-capture-room.py`, the committed copy. Every mode runs from `/root/tz46-work` — `main` asserts it (lines 1615 to 1640). **In every block handed to the Boss both are written out in full.**

### 0.1 The instrument and the timer, staged

Extract Appendix A from this TZ as the primary checkout carries it after contract §1's pull, with this script, verbatim, its one argument the destination, its output into `logs/01-stage.log`:

```
/root/tz04a-env/venv/bin/python -B - /root/tz46-work/stage <<'EOF2'
import hashlib, os, sys
SRC = "/root/btc-5m-twap/CryptoTZ/TZ-46-capture-room.md"
DEST = sys.argv[1]
WANT = {
    "research/tz46-capture-room.py": "363b269c462d14da1656feb7bad92fec43adb1593209131fe5ca6e5c9f6755f6",
    "deploy/systemd/btc-rewardbook-archive.timer": "7b0804285af6987340838bd59573897d013cf97edc5d4132cda7f3f9ba3e3824",
}
OLD = {"deploy/systemd/btc-rewardbook-archive.timer": "bf5af0252c420d8db1579b82e5da21472cdb6bc871fa8035ecf6f1edc9720a0f"}
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
    mode = "xb"
    if os.path.exists(path):
        with open(path, "rb") as fh:
            assert hashlib.sha256(fh.read()).hexdigest() == OLD.get(name), "%s is not the file this one replaces" % path
        mode = "wb"
    with open(path, mode) as fh:
        fh.write(data)
    print(path, data.count(b"\n"), len(data), hashlib.sha256(data).hexdigest(), "created" if mode == "xb" else "replaced")
EOF2
```

| path | lines | bytes | SHA-256 |
|---|---|---|---|
| `research/tz46-capture-room.py` | 1,644 | 88,254 | `363b269c462d14da1656feb7bad92fec43adb1593209131fe5ca6e5c9f6755f6` |
| `deploy/systemd/btc-rewardbook-archive.timer` | 12 | 435 | `7b0804285af6987340838bd59573897d013cf97edc5d4132cda7f3f9ba3e3824` |

Into the stage both are `created`; into the worktree, §3.1, the instrument is `created` and the timer `replaced`, the file it replaces asserted TZ-34's, `bf5af025…`, map §0's `frozen` row. A failed assert or another hash is BLOCKED. The staged copy runs §0.2's `fingerprint` and §0.5's `number`, and nothing else.

### 0.2 Fingerprint

`I0 fingerprint`, into `logs/02-fingerprint.log`, performs contract §1 steps 3 and 4 inside the instrument and asserts them, against `SYSTEM-MAP.md` and the files of its §0 table in the primary checkout `/root/btc-5m-twap`: revision `2026-11-16-a`; the six anchors; `A2`, `A4`, `A5` and `A6` re-derived as the first 12 hex characters of those files' SHA-256; the table's **64** rows, each printed in lines, bytes and SHA-256 — **61** `frozen` rows asserted equal to the map, **2** `tracked` and **1** `reported`; and the map's own lines, bytes and SHA-256 (`mode_fingerprint`, lines 734 to 761). It prints `FINGERPRINT PASS` or stops at the first mismatch, which is BLOCKED.

### 0.3 Host gate

From `/root/btc-5m-twap`, with `S` first set to the scratchpad directory the session's system prompt names, output verbatim into `logs/03-host-gate.log`:

```
date -u; date -u +%s; uptime -s; journalctl --list-boots --no-pager | tail -n 3
nproc; grep -E '^(MemTotal|MemAvailable|SwapTotal|SwapFree):' /proc/meminfo
df -B1 --output=source,size,avail /var/lib/btc-recorder
find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
grep -c e3975b5da44c5328adf3bf3914634cd878842c73 /var/lib/btc-recorder/runtime.jsonl
/root/tz04a-env/venv/bin/python -c 'import sys; print(sys.version.split()[0])'
for u in btc-pairbook.service btc-pairbook-archive.service btc-pairbook-archive.timer btc-rewardbook-archive.service btc-rewardbook-archive.timer; do cmp deploy/systemd/$u /etc/systemd/system/$u; echo "$u cmp exit=$?"; done
cat /root/btc-rewardbook-archive-svc/commit.txt /root/btc-pairbook-archive-svc/commit.txt
sha256sum /root/btc-rewardbook-archive-svc/tz34-rewardbook-archive-timer.py /root/btc-pairbook-archive-svc/tz28-pairbook-archive-timer.py /root/btc-rewardbook-svc/tz33-reward-book-capture.py /root/btc-pairbook-svc/tz26-nesting-b3-capture.py
TZ=UTC systemctl show btc-recorder.service btc-pairbook.service btc-rewardbook.service adv3-bot.service btc-pairbook-archive.service btc-pairbook-archive.timer btc-rewardbook-archive.service btc-rewardbook-archive.timer btc-chainbook.service -p Id -p MainPID -p NRestarts -p ActiveState -p SubState -p UnitFileState -p ActiveEnterTimestamp -p Result
TZ=UTC systemctl list-timers btc-pairbook-archive.timer btc-rewardbook-archive.timer apt-daily-upgrade.timer apt-daily.timer --all --no-pager
journalctl _PID=1 -o short-iso --since -3d --no-pager | grep -E 'Reload|btc-|adv3' | tail -n 60
du -xsb /root /var/lib /var/log /var/cache /usr /home /opt /srv /tmp 2>/dev/null; du -xsb /var/lib/* /root/* 2>/dev/null | sort -n | tail -n 16
du -sb /var/lib/btc-rewardbook /var/lib/btc-pairbook /var/lib/btc-rewardbook-archive /var/lib/btc-pairbook-archive /var/lib/btc-recorder /root/btc-forensics /root/.claude-8j 2>&1; find /root/btc-forensics -type f | wc -l
journalctl --disk-usage; grep -vE '^[[:space:]]*(#|$)' /etc/systemd/journald.conf; ls -la /etc/systemd/journald.conf.d 2>&1
grep -vE '^[[:space:]]*(#|$)' /etc/needrestart/needrestart.conf 2>&1 | head -n 20; ls -la /etc/needrestart/conf.d 2>&1
grep -E '^(Start-Date|Commandline|Upgrade|End-Date)' /var/log/apt/history.log | tail -n 20
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
systemctl is-active telemetry-watch.service; echo "exit=$?"
for t in /root/btc-recorder-svc /root/btc-pairbook-svc /root/btc-pairbook-archive-svc /root/btc-rewardbook-svc /root/btc-rewardbook-archive-svc /root/adv3-bot-svc; do test -e $t; echo "$t exit=$?"; done
test -e /root/tz45-work; echo "/root/tz45-work exit=$?"
git -C /root/btc-5m-twap worktree list
echo "$S"; ls -la "$(dirname "$(dirname "$S")")"
```

then the memory gate's own reads, appended to the same log:

```
for k in 1 2 3 4 5; do m=$(( $(awk '/^MemAvailable:/ {print $2}' /proc/meminfo) * 1024 )); echo "MemAvailable read $k $(date -u +%T): $m"; [ "$m" -ge 133073162 ] && break; [ "$k" -lt 5 ] && sleep 60; done
```

- **H1** — `find` prints exactly one path.
- **H2** — `df` names source `/dev/vda2` and size `31612203008`; `grep -c` prints at least `1`. With H1 this is map §6's host identity.
- **H3** — the interpreter prints `3.12.`.
- **H4** — the archives and both captures' code as TZ-26, TZ-28, TZ-33 and TZ-34 left them, because B-PAIR-OFF runs the pair book's archive's own code and B-TIMER replaces the reward book's archive's timer beside its unchanged service: `cmp` exits `0` for the five units; the two `commit.txt` print `6a615257277d3c94dafd4d39783499560a344648` and `d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3`, each the commit its archive's tags point at (§0.5); `sha256sum` prints `1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72`, `46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4`, `a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670` and `caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec`, map §0's rows.
- **H5** — `btc-recorder.service`, `btc-pairbook.service`, `btc-rewardbook.service` and `adv3-bot.service` each read `ActiveState=active` and `UnitFileState=enabled`, and both archives' timers `active` and `enabled`: G-STILL reads the four units (§4.6), and the blocks change both timers.
- **Memory gate** — the last `MemAvailable read` at least `133,073,162` bytes: a read below it is read again 60 s later, five reads at most, the first at or above it passing (§0.4; map §7 item 137).
- **Disk gate** — `avail` at least `7,600,000,000` bytes, §0.0's bound read again (§0.4).

These are twelve checks — H2 two, H4 four (the `cmp`s, each `commit.txt`, the `sha256sum`), H5 two — and any one failing is BLOCKED. **The rest is printed and carries no threshold:** the boots; the units and the timers, both archives' and the package manager's among them; systemd's reload records of three days and the package history, beside which the report sets every archive run off its calendar (map §7 items 115, 129 and 166); **every tree of the disk by `du -xsb`, the sixteen largest of `/var/lib` and `/root` by name, both stores, both archives' state, the recorder's store, the forensic store and its count, and the sessions' configuration directory** — so that the report says again what holds the room; **the journal's size, journald's configuration and its drop-in directory**, which §1 leaves alone and reads; **needrestart's configuration and its drop-in directory**, which decides whether a library's upgrade restarts a capture (§4.8); the consumer's two states, on which map §6's headroom is conditional; the code trees present; `/root/tz45-work` gone, by map §3; the worktrees, map §3's two; and the listing of the directory that holds the session's own, whose UUID directories `I scratch` names live or earlier (§3.3).

### 0.4 Resource floors, in exact bytes

**Disk — three bounds on the free bytes of `/dev/vda2`, each derived from map §6's disk rows and map §2.6.** **`7,600,000,000` at §0.0's read and again at the host gate:** the reward book's `STREAM_FLOOR`, `7,300,000,000`, below which no stream of it opens for a slot (`research/tz33-reward-book-capture.py` line 190, read at each slot's decision, line 1531), plus `300,000,000`, which holds the session's own writes, `50,000,000` at most (below), and an hour and a quarter of both stores at their heaviest measured rates — `74,127,110` bytes an hour for the reward book on the heaviest day read (TZ-45 §0.4) and `115,007,779` for the pair book over TZ-45's two reads of 2026-11-16 (map §6, disk; `296,688,123` bytes in `9,287` s), `236,418,611` — `286,418,611` together, until B-PAIR-OFF's last run of the pair book's archive, about an hour after the start, takes the pair book's store off the disk. So a run that starts cannot itself take the reward book below its floor before its first block frees room. **`2,300,000,000` at the start of every mode that reads the stores, the forensic store or GitHub** (`DISK_FLOOR`, line 132; `floors`, lines 284 to 297): the reward book's `RESOURCE_FLOOR`, `2,200,000,000`, below which it halts and its unit does not restart it (line 189 of its file; map §2.6), plus `100,000,000`. A mode never BLOCKS on the reward book's stream floor: below it that capture is paused already, and this TZ is what lifts it — as TZ-34 §0.4 held. **`7,400,000,000` after each copy §9's `reclaim` makes** (`RECLAIM_FLOOR`, line 133): the stream floor and one slot of the reward book's streams at its cut, `100,000,000`. **What the session writes:** the worktree's checkout, about `15,700,000` bytes — `53e5690`'s tracked files, `15,407,350`, with this file and the instrument; the stage's two files, `88,689`; `state.json`, both room files and `forensics-plan.json`, under `2,000,000` together — the plan's rows carry each matched file's path, bytes, SHA-256 and its asset's record; the logs, under `5,000,000`; and in §9 only the files the report names by hash and those kept by name. Under `50,000,000` at its peak. **No download is stored:** `forensics` hashes each in pieces of 1 MiB as it arrives (`download`, lines 499 to 509).

**Memory.** `MemAvailable` at least **`133,073,162`** bytes at the host gate and at the start of every mode that reads the stores, the forensic store or GitHub (`MEM_FLOOR`, line 134; `floors`, lines 284 to 297) — twice `66,536,581`, the host peak modelled from the largest of the Architect's runs at the ratio TZ-37 measured between the host's peak and the Architect's for one code, `58,953,728 / 49,168,384` (map §6, memory; §7 items 131 and 156): `forensics` peaked at `55,152,640` to `55,492,608` bytes over eight runs under Python 3.12.3, against a loopback GitHub in another process, over a stand-in of 140 Releases and `13,072` assets — every archive Release given 96, the most a daily run of either archive has moved (TZ-45 report §2.8), and the assets in all more than twice the repository's at its refs [estimated] — each asset's record as GitHub serves it, uploader and all, and a forensic store of 2,613 files, `191,729,532` bytes, 13 of them the matches; `selftest` `29,032,448` to `29,282,304` over its runs; `fingerprint` `29,077,504` to `29,229,056`; and `reclaim` `31,129,600` over a stand-in tree. A page of Releases carries every asset's record, so `forensics` reads twenty Releases a page (`RELEASES_PER_PAGE`, line 112) and keeps of each only its id, tag, draft flag and its assets' id, name, size, state, digest and URL (`slim_release`, lines 534 to 537); at fifty a page the same stand-in peaked at `78,286,848`. A read below the floor is read again every 60 s, five reads at most, the first at or above it passing and five below it BLOCKING (map §7 item 137). The host's `MemAvailable` read `188,846,080` to `494,649,344` bytes across TZ-45's session (its report §2.13). Every mode prints its peak on every exit (`main`, lines 1635 to 1639), and runs under `nice -n 19`: the host has one processor (map §6).

### 0.5 Refs and the number

`I0 number`, into `logs/05-number.log`, and `git -C /root/btc-5m-twap ls-remote origin`, into `logs/05-refs.log`, after §0.4, every ref reported; both again in §3.1 — `I0 number` after its fetch, `git ls-remote origin` before its push. **The Architect read 160 ref lines on 2026-11-16 at 23:05 UTC:** `HEAD` and `refs/heads/main` at `53e5690`, PR #45's merge, above `4342383`, revision `2026-11-16-a`; twenty-one `tz-*` branches; forty-four pull heads and no merge ref — no pull request open; fifty-seven `pairbook-streams-*` tags at `d8194fd`, the last `pairbook-streams-1794798020`, and thirty `rewardbook-streams-*` at `6a61525`, the last `rewardbook-streams-1794792620`, the calendar run of 2026-11-16; the lightweight `tz-44-l0-inputs` and `tz-45-l0-rule-w-inputs`; and the two annotated tags with their peeled lines. Every run of either archive that takes a set adds one tag — on their calendars, at 01:30:20 and 03:00:20 UTC, and possibly 1,800 s and 600 s after a reload of systemd (map §7 items 115, 129 and 166). Every commit on `main`'s first-parent line above `53e5690` is reported with the paths it changed, the upload that carries this TZ among them. A difference is recorded, not BLOCKING, unless `refs/heads/tz-46-capture-room` already exists — BLOCKED; a `main` that does not carry revision `2026-11-16-a` is §0.2's BLOCK.

**NUMBER — CANON hard rule 2.** `I0 number` reads, in the primary checkout, `git ls-tree --name-only origin/main -- CryptoTZ/ CryptoReports/` and must print `NUMBER PASS - 2 of 2`: `CryptoTZ/` holds `TZ-46-capture-room.md` and no other file whose name begins with `TZ-46-`, and `CryptoReports/` no report whose name does (`number_reading` and `mode_number`, lines 724 to 729 and lines 764 to 771). Anything else is BLOCKED, here and in §3.1 alike. Map §7 item 170 asks a TZ for this work before L1's measurement days; `CryptoTZ/` and `CryptoReports/` end at TZ-45's files, so its number is 46.

---

## 1. Why this TZ exists, and what it changes

Line numbers in this section are Appendix A's instrument's unless a file is named; `tz33` is `research/tz33-reward-book-capture.py`, `tz34` `research/tz34-rewardbook-archive-timer.py`, `tz28` `research/tz28-pairbook-archive-timer.py` and `tz26` `research/tz26-nesting-b3-capture.py`, each at `53e5690`.

**The bound, as the code evaluates it** (map §7 item 106's rule). At every slot `S` the reward book decides whether its stream opens: `stream_off_reason` (tz33 lines 1294 to 1304), called at the slot's decision, `S − 6`, with `book.free()` — `statvfs` of `/var/lib`, tz33 lines 439 to 441 and 1453 — and the store's stream bytes summed from their directory entries (tz33 lines 1279 to 1291), at tz33 line 1531. **Below `7,300,000,000` bytes free the slot stores no stream** (`STREAM_FLOOR`, tz33 line 190) and its record names `floor`; the polls go on. A slot without its stream is a slot no replay can read, so the day it falls in is not whole for L1. Free space read again at the next slot's decision lets the stream open again; nothing restarts.

**What filled the disk is a daily wave, and its larger half is the pair book's.** Both stores grow between their archives' runs, once a day each — the reward book's at 01:30:20 UTC (map §2.6), the pair book's at 03:00:20 (map §2.5) — and between them the disk holds every stream since. TZ-45's two reads on 2026-11-16 (map §6, disk) measured the reward book's store growing `1,320,783,710` bytes a day and the pair book's `2,760,186,694`, the pair book's runs having read `1.47` to `2.42` GB a day to 2026-10-23 (map §2.5) and the reward book's about `1.0` GB a day at its first runs (map §2.6) and `1,779,050,648` bytes on the heaviest of L0's days (TZ-45 §0.4). Free space with both stores' streams taken off — the bytes both archives give back, called **the room** below — stood at about `10,630,000,000` bytes on 2026-11-16 [modelled: TZ-45's read at 10:23:57 UTC, `9,206,390,784` free, plus both stores less the files beside their streams — the reward book's about `16,300,000` bytes a day since 2026-10-28 (TZ-33's figure, map §2.6), the pair book's `2,363,002` a day since 2026-10-10 (map §6, headroom) — plus TZ-45's own tree, `125,680,659`]. At 22:00 UTC the stores hold about 20 h and 19 h of streams, `1.1` to `1.5` and about `2.2` GB, and free space meets the floor; by 01:30 they hold about 24 h and 22.5 h, `3.9` to `4.4` GB, and the floor holds the streams off until the reward book's archive runs [modelled, at those rates]. That is what happened on 2026-11-13 (map §7 item 170).

**Item 170's own list is weak on its largest term, and this TZ does the stronger thing.** The map names three levers: the reward book's archive more often, the forensic store's copies of files a Release holds, the journal. Run every three hours, the reward book's archive takes its store's peak from about a day of streams to fourteen slots; but the pair book's store, about `2.6` to `2.8` GB before its own run at 03:00:20, then sets the daily low alone — the room less `2.76` GB less the reward book's fourteen slots is about `7.42` GB, `120,000,000` above the floor, and below it on a heavier day [modelled]. The journal, `2.9G` by `journalctl --disk-usage` (map §6, disk) — about `3,100,000,000` bytes in systemd's units of 1,024 — is near journald's own cap already: by default 10% of the file system, `3,161,220,300` bytes, at most 4 GiB, past which it rotates [read from journald.conf(5), not measured; §0.3 prints its configuration], so it adds little more; and it holds every project's records, so pruning it touches other projects. **The pair book is the term to remove — the Architect's decision:**

- **No open question reads it.** The backup track closed on its streams (TZ-30, NO CAPTURE) and the W track on its legs (TZ-32, W1-NO-EARN); each re-opens only on windows no TZ has read (CANON §1.6), and every window after `1793013300` is unread and already in the archive's public Releases — about 2,100 fifteen-minute windows from 2026-10-26 to the stop (map §2.5). A later question that wants more captures them fresh; nothing measured is lost by stopping now.
- **While it runs, its archive's one bad night costs the reward book its room.** Its store grows `2.76` GB a day; one deferred run (map §7 item 166 records one, `status=75/TEMPFAIL`) leaves two days of it on the disk, and the reward book's floor meets it first, because TZ-33 §1 set that floor above the pair book's own — `7,300,000,000` against `4,500,000,000` (tz26 line 132) — precisely so that the pair book kept its room: a priority the tracks have since inverted.
- **Discarded:** archiving the pair book every three hours too — eight restarts a day of a capture nothing reads (tz28 `restart_phase`, lines 532 to 568), and each of its deferrals still able to take the reward book's room within a day.

**The three changes, in the order they run.**

- **B-PAIR-OFF (§3.6):** one more run of the pair book's archive, started by hand — its own code, which moves every closed window's streams to that run's Release by its own proofs, restarts the pair book inside its band and reads the next window streamed (tz28 `run`, lines 608 to 669) — then its timer and the pair book disabled and stopped, `systemctl disable --now`, the stops TZ-28 and TZ-26 fixed (map §2.5; §6, process supervision). **The order is forced:** the run's restart asserts the pair book active and halts the archive otherwise (tz28 line 536), so the capture stops only after its last run ends. The windows the pair book streams during and after that run stay in its store as data, unarchived — a few, about `29,000,000` bytes a window at its 2026-11-16 rate — and a later run of its archive takes them first. **Map §7 item 166 asks a TZ that touches the timers to remove `OnActiveSec` from both;** this one removes it from the reward book's archive's and disables the pair book's archive's, whose file keeps it unchanged: a disabled timer is never started by a reload, and a TZ that enables it again removes it first.
- **B-TIMER (§3.7):** the reward book's archive's timer replaced by Appendix A's: `OnCalendar=*-*-* 01/3:30:20 UTC` — 01:30:20 UTC and every third hour, eight elapses a day, which `systemd-analyze calendar` on systemd 255 normalizes to the same text and iterates as 01:30:20, 04:30:20 … 22:30:20 [run by the Architect] — `AccuracySec=1s`, the same service, and **no `OnActiveSec`** (map §7 item 166): no reload of another project's starts a run, and the timer's start sets none off. The service and its code are TZ-34's, unchanged: a run takes every stream file of every slot whose `slot.json` was due at least 60 s before it, at most 400 (tz34 `inventory`, lines 271 to 305, the rule at line 281), and nothing in it reads its calendar (tz34 `run`, lines 752 to 806). So a run at `hh:30:20` takes the slots to `hh:00`, and the store between two runs holds at most thirteen closed slots and the one being written — **fourteen slots, `445,535,636` bytes at the heaviest slot of L0's eight days, `31,823,974`** (`PEAK`, lines 127 to 129) — and a deferred run costs three hours of the store, not a day.
- **B-FORENSICS (§3.5):** every file of `/root/btc-forensics/` that a published Release holds by bytes and SHA-256, removed — each proved first by the Release's own record of the asset, uploaded with those bytes and that digest at its download URL, and by a full anonymous download hashing equal, then hashed again on the host right before its removal (`mode_forensics` and `mode_forensics_remove`, lines 916 to 1024). CANON hard rule 15 leaves such a file to its Release; TZ-44's §9 copied twelve day archives and their manifest, `186,490,880` bytes and more, that `tz-44-l0-inputs` holds by the same hashes (map §7 item 167), and the plan must find at least those thirteen or nothing is removed (`PLAN_MIN`, line 114).

**Not done, and why.** The journal: above. **The reward book's `STREAM_FLOOR`:** its derivation names the pair book's room (TZ-33 §1), which this TZ ends, so a lower floor would be justified — but it lives in a running capture's frozen code (map §0), and the room below does not need it now; a later TZ lowers it when the room requires, and it is the next lever. **The recorder's store**, `1,628,979,449` bytes at TZ-45's host gate (its report §2.9) and `33,632,842` a day on disk by TZ-09 (map §6, capture cost): its own capture, not this TZ's. **Another project's files and units:** none is read beyond `du`, none changed.

**What the room becomes** [modelled]. After this TZ the reward book's store is the only one the disk refills, and it never holds more than `PEAK`; the room is about `10,630,000,000` bytes, plus what B-FORENSICS frees — at least `186,490,880` — less the pair book's residual and the drift since 2026-11-16. Its daily low is the room less `PEAK`, about `2,900,000,000` bytes above the floor. Beside the streams the disk fills about `65,000,000` bytes a day [modelled: the room at TZ-28's closing read of 2026-10-11 against TZ-45's of 2026-11-16, 36 days apart, each store's files beside its streams taken at the rates above] — about 45 days of margin — and `187,760,570` at the fastest window map §6 records, about 15. **G-ROOM** (§4.7) asks the closing read for at least `2,000,000,000` bytes above the floor and `PEAK`, about ten days at that fastest drain: a margin the next TZs can watch and act on. `room after` prints the days at both of map §6's figures, `43,500,000` and `187,760,570` bytes a day (`DRIFTS`, line 131).

**What this TZ is not.** It measures nothing of L1's question and reads no stream: whether L1's days are whole is read from their slot records by the TZ that measures them, which counts a day by its longest run of whole slots (CANON hard rule 8). It proves its deployment on the new timer's first run, which the timer fires (CANON hard rule 14), and on the pair book's last archive run.

---

## 2. Scope

Allowed, and nothing else:

1. **The branch `tz-46-capture-room`** carries two files: `research/tz46-capture-room.py`, new, and `deploy/systemd/btc-rewardbook-archive.timer`, replacing TZ-34's (§10 C3). No other repository file changes. The report goes to `main` (contract §4).
2. **Units.** `btc-pairbook-archive.service` started by hand once, twice on a deferral, by B-PAIR-OFF; `btc-pairbook-archive.timer` and `btc-pairbook.service` disabled and stopped by B-PAIR-OFF, after that run; `/etc/systemd/system/btc-rewardbook-archive.timer` replaced by B-TIMER with Appendix A's and back by K-46T where §4.8 authorizes it; `systemctl daemon-reload` and `systemctl restart btc-rewardbook-archive.timer` by B-TIMER and K-46T; `btc-rewardbook-archive.service` started by hand once by B-RETRY, only on a deferral; `btc-rewardbook.service` started by B-START-RB, only where §4.8 authorizes it. **No other unit is started, stopped, signalled, enabled, disabled or edited**, the recorder's, the reward book's and the advisor's among them, and no unit file but the one timer is written.
3. **The capture stores.** The session writes, removes or renames nothing under `/var/lib/btc-rewardbook/`, `/var/lib/btc-pairbook/`, `/var/lib/btc-recorder/` or `/var/lib/btc-chainbook/`; the archives' own runs move stream files by their own proofs. **Of the reward book's store** the instrument reads the names and sizes of its directory entries and opens its `slot.json` files and `runtime.jsonl` alone, which the reserve excepts (map §2.6) — no stream, rewards file or selection is opened, as its hook refuses (`policy`, lines 185 to 223); **of the pair book's store** names and sizes alone, nothing opened; of the recorder's and the chain book's nothing but §0.3's `du`. §3.10's closing reads print the last lines of both captures' `service.log`, which the reserve excepts (map §2.5, §2.6). Every day from 2026-11-14 stays reserved (map §2.6).
4. **The archives' state.** Both ledgers, both `archive.log`, `runs/<A>/delete.jsonl` of the reward book's archive's first run on the new calendar and both `commit.txt` are read; nothing under either archive's state or code tree is written by the session.
5. **The forensic store.** Nothing in `/root/btc-forensics/` is removed but the files `forensics-plan.json` proves a published Release holds, by B-FORENSICS (`policy`, the removal allowed only in `forensics-remove` and only for a planned path); nothing is written there but `reclaim`'s copies, §3.3's and §9's, by exclusive create.
6. **Another project:** nothing under `/root/PROJECT_GAMING_PS5`, `/root/crypto-auto`, `/root/my_real_estate_bot`, `/root/seahome_webapp.git`, `/var/lib/cryptorun`, `/var/lib/cryptopaper`, `/var/lib/containerd`, `/home`, `/srv` or `/var/www` is read but by §0.3's `du`, or changed; no unit of another project is touched; **the journal and journald's and needrestart's configuration are read and not changed** — no `journalctl --vacuum-*`, no edit under `/etc/systemd/` but the one timer, none under `/etc/needrestart/`. **Of the host besides**, the session reads `/proc` — `meminfo` and the pair book's command line — systemd's records and the journal of this project's units and of PID 1, the package manager's timers and history, and `du` of every tree (§0.3, §3.10), and changes nothing.
7. **The network.** Anonymous requests to GitHub alone, each with `User-Agent: btc-5m-twap-tz46` (`build_request`, lines 481 to 484): the repository's Releases and a matched Release's assets, read through the API, and each matched asset downloaded — at most `40` API requests a run (`API_MAX`, line 111), under the `60` an hour GitHub allows one address without a token (map §6, GitHub Releases). The hook refuses a lookup of any host but `api.github.com`, `github.com`, a `*.githubusercontent.com` host the downloads redirect to and the loopback (`policy`). **No request of the instrument carries a credential**; the archives' own runs use theirs, and `git ls-remote`, the branch's push and `gh pr create` are the session's (§3.1).
8. **Prints:** no price, size, side, book hash, rate, competitiveness or outcome — of a slot record a `first` line prints its process, flags and counts alone (lines 1141 to 1219). The plan and the report name each removed file by path, bytes and SHA-256, and its asset by tag, name and id.
9. **No order** is placed, signed or cancelled, and no key of any venue is held or read.
10. **The session's own trees.** `/root/tz46-work/**` and the branch worktree under it, written and removed by §9; the UUID directories `I scratch` names earlier, removed by B-RECLAIM-SCRATCH (§3.3); copies into `/root/btc-forensics/` by `reclaim` alone (item 5; CANON hard rule 15).

---

## 3. The work, in this order

Every command's output goes to `logs/`, one file per step under the names below, and is quoted in the report; a step run again appends to its own log under a `date -u` line. **B-RECLAIM-SCRATCH runs inside §3.3 and holds back nothing after it; B-FORENSICS holds back nothing of §3.6 to §3.10, none of which reads the forensic store but `room after`'s count; B-RECLAIM-OWN runs last (§9).** On a BLOCK before §3.1, B-RECLAIM-OWN runs with `I0` in place of `I` and without its `git worktree remove` line; on a BLOCK or a FAIL after it, the run takes the stop §4.8 authorizes, then §3.10 and §9, skipping every step that needs a PASS it lacks.

| step | logs |
|---|---|
| §0.0 to §0.5 | `00-ready.log`, `01-stage.log`, `02-fingerprint.log`, `03-host-gate.log`, `05-number.log`, `05-refs.log` |
| §3.1 | `10-number.log`, `11-worktree.log`, `12-fingerprint.log`, `13-push.log`, `14-pr.log` |
| §3.2 | `20-selftest.log` |
| §3.3 | `30-still.log`, `31-scratch.log`, `32-reclaim-scratch.log` |
| §3.4 | `35-room-before.log` |
| §3.5 | `40-forensics.log`; `41-B-FORENSICS.log`, the block's |
| §3.6 | `50-B-PAIR-OFF.log`, the block's |
| §3.7 | `60-band-timer.log`, the Executor's wait; `61-B-TIMER.log`, the block's |
| §3.8 | `70-first.log`; `71-B-RETRY.log`, the block's, where it runs |
| §3.9 | `80-still.log`, `81-timer-again.log` |
| §3.10 | `90-room-after.log`, `91-host-gate-again.log`, `92-closing.log`, `99-selfcheck.log` |

**Where the session's permission classifier refuses a command of a block named B-… or K-…**, the Executor tries the block once and hands the Boss its paste, unchanged, once, in plain words, only once its band is open (CANON hard rule 14; map §6, sandbox limit — destructive actions; §7 items 124, 138 and 144): every block below is its own paste — one command line, every step after its band gated on the one before it, its output appended to its log under a `date -u` line, and its gate's own reads as its last step, so that the Executor verifies it from that log and runs none of its steps again. Map §6 records `systemctl disable --now` refused as "[Production Deploy]" at TZ-26, `install` and `daemon-reload` never, `systemctl restart` not yet tried, `systemctl start --no-block` run at TZ-34's B-RETRY, and `reclaim` refused at TZ-37 to TZ-43 and let through at TZ-44 and TZ-45 (map §3; TZ-45 report §5). **A read-only mode the classifier refuses is handed over the same way**, as its own paste appending to its log. **A block handed to the Boss holds back only the steps that read what it changes** (map §7 item 140), named at each block.

**This session's systemd steps, and what each sets off** (map §7 items 115, 125, 129 and 166). B-PAIR-OFF's two `disable --now`, at an instant `D`, reload systemd: the pair book's archive's timer is stopped by the same command and sets nothing off, and **the reward book's archive's timer, TZ-34's with `OnActiveSec=1800`, may run that archive at `D + 1,800`** — a run off its calendar that moves the store's closed slots and restarts nothing; B-TIMER's band waits for it to end. B-TIMER's `daemon-reload` and `restart`, at `T`, set nothing off of this project: after them no timer of its carries `OnActiveSec` — the pair book's archive's is disabled, the reward book's archive's new file has none — and the restart drops the old file's pending trigger. K-46T's, where it runs, brings TZ-34's file back and with it a run 1,800 s later. A reload of ours re-arms another project's timers as theirs re-arm ours (map §7 item 166); nothing of theirs is changed. G-STILL counts the pair book's restarts from its archive's ledger (§4.6).

### 3.1 The branch and its files

```
git -C /root/btc-5m-twap fetch origin
I0 number
git -C /root/btc-5m-twap worktree add -b tz-46-capture-room /root/tz46-work/wt origin/main
```

Into `10-number.log` the fetch and `I0 number`, which must print `NUMBER PASS - 2 of 2` again (§0.5), or BLOCKED; into `11-worktree.log` the worktree and §0.1's script again, verbatim but for its argument, `/root/tz46-work/wt` — it must print the same two lines of lines, bytes and SHA-256 as at §0.1, the instrument `created` and the timer `replaced`; into `12-fingerprint.log` `I fingerprint`, which must print `FINGERPRINT PASS` again, from the worktree's file. Into `13-push.log`: commit the two files alone on the branch, `research/tz46-capture-room.py` and `deploy/systemd/btc-rewardbook-archive.timer`; `git -C /root/btc-5m-twap ls-remote origin` (§0.5); push with `git -C /root/tz46-work/wt push -u origin tz-46-capture-room` — through `credential.helper=!gh auth git-credential` where the URL's credential is refused (map §6, git remote) — then:

```
date -u +%FT%T.%NZ; git -C /root/tz46-work/wt ls-remote origin refs/heads/tz-46-capture-room
git -C /root/tz46-work/wt rev-parse HEAD
git -C /root/tz46-work/wt diff --numstat origin/main HEAD
```

— the instant the commit is on `origin`, its hash there, which must be the worktree's `HEAD`, and the diff: `1644 0` for the instrument and `3 4` for the timer, two paths and no other; into `14-pr.log` the pull request against `main`, opened with `gh pr create`. A failed assert or a non-zero exit here is BLOCKED. **B-TIMER installs the timer from this worktree, at this commit**, so what systemd runs is the file the branch holds.

### 3.2 The self-test

`I selftest`, into `20-selftest.log`, must print `SELFTEST PASS: 29 checks`. It reaches no network but a listener of its own on `127.0.0.1`, `_FakeGitHub` (lines 1307 to 1337), and runs on literals and on temporary trees under `/root/tz46-work/selftest-tmp/`, which it removes (`mode_selftest`, lines 1340 to 1612). It proves the new calendar's eight elapses and the next one across midnight; both blocks' bands; G-TIMER's eleven checks on literals, and each of eight wrong readings failing; systemctl's stamps; G-TRIGGER, a ledger's first start since an instant — a pending set resumed counting by its new start — and a run's state; G-NEXT's slots and verdicts; G-STILL unchanged, moved by its archive's restarts and stopped after B-PAIR-OFF, and four wrong readings; G-PAIR's eight checks and eight wrong readings; G-ROOM at its bound and a byte under it; NUMBER; reclaim's predicates; the branch's timer by its SHA-256 and its lines; `STREAM_FLOOR` as the reward book's own file holds it at line 190, that file asserted by its SHA-256 `a276bbb9…`; the hook's every decision this TZ relies on; every request's own `User-Agent`, and no credential on any; both stores' views by their own names; and the forensic plan and removal end to end against `_FakeGitHub` — a file and its copy held by one asset and downloaded once, an asset of other bytes, one not uploaded, a draft, an empty file and a download of other bytes left out, fewer files than a named Release must prove BLOCKED with no plan written, a planned file changed after its proof BLOCKED with nothing removed, the proved files removed and every other kept, a second run removing nothing, and the hook refusing a removal in the real forensic store outside `forensics-remove`. **Its `opens refused: 1` is that last check's own refusal.** A red self-test stops the run here, and it goes to §3.10 and §9.

### 3.3 The units, the directories beside this session, and B-RECLAIM-SCRATCH

`I still`, into `30-still.log`, records the recorder's, the pair book's, the reward book's and the advisor's `MainPID`, `NRestarts` and `ActiveState` in `state.json`, with the instant, and prints their `UnitFileState`, `MemoryCurrent` and `MemoryPeak` and both archives' units (`mode_still`, lines 793 to 813). Then `I scratch "$(dirname "$S")"`, into `31-scratch.log`, lists every UUID directory beside this session's own and names each **live** — born from 1 s before to 60 s after the start of a running process whose `argv[0]` is `claude` or ends in `/claude.exe` — or **earlier** (`mode_scratch`, lines 842 to 855). Map §3 expects TZ-45's session's own, unless a reboot of the host emptied `/tmp`. **The rule alone decides:** every directory `scratch` names earlier is reclaimed (map §7 item 150).

**B-RECLAIM-SCRATCH**, for every directory `I scratch` names **earlier** — none it named live, and never this session's own — into `32-reclaim-scratch.log`:

```
cd /root/tz46-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz46-work/wt/research/tz46-capture-room.py reclaim <each earlier directory, by its full path>
rm -rf <one such directory>; echo "exit=$?"
test -e <that directory>; echo "exit=$?"
```

One `reclaim` names every earlier directory and must print `RECLAIM PASS` before any removal; then one `rm -rf` and one `test -e` a directory, the last reading `exit=1`. `reclaim` refuses a directory born from 1 s before to 60 s after a running claude process started, and any path but `/root/tz46-work` that is not a UUID directory under `/tmp/` whose parent's name carries `btc-5m-twap` (`reclaimable`, lines 1246 to 1251; `mode_reclaim`, lines 1254 to 1302). If `I scratch` names none earlier, the block is recorded as empty and skipped. **Its paste**, where the classifier refuses it — the Executor writes in every earlier directory's full path, one `rm -rf` and one `test -e` a directory, all chained to the `reclaim`'s `exit=0`, which it reaches only after `RECLAIM PASS`:

```
{ date -u +%FT%T.%NZ; (cd /root/tz46-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz46-work/wt/research/tz46-capture-room.py reclaim <D1> <D2>); echo "exit=$?"; } >> /root/tz46-work/logs/32-reclaim-scratch.log 2>&1 && tail -n 1 /root/tz46-work/logs/32-reclaim-scratch.log | grep -qx 'exit=0' && { date -u +%FT%T.%NZ; rm -rf <D1>; echo "exit=$?"; test -e <D1>; echo "exit=$?"; rm -rf <D2>; echo "exit=$?"; test -e <D2>; echo "exit=$?"; } >> /root/tz46-work/logs/32-reclaim-scratch.log 2>&1
```

It holds back nothing of §3.4 to §3.10, which read none of what it removes.

### 3.4 The room, before

`I room before`, into `35-room-before.log` (`mode_room`, lines 877 to 913): free space; of each store its directories, its stream files and every other file, counts and bytes, by directory entries alone (`store_view`, lines 421 to 448); the forensic store's files and bytes; both archives' last ten runs from their ledgers — each run's state, files, bytes, free space before and after its removal, its store's streams at its end and its rate a day (`runs_line`, lines 858 to 874); and the room — free space plus the reward book's stream files — its margin over the floor and `PEAK`, the room with the pair book's stream files too, and the margin's days at both of map §6's drifts [modelled]. It writes `room-before.json`. **It carries no threshold:** it is the baseline §3.10 is read against.

### 3.5 The forensic store — `forensics`, then B-FORENSICS

`I forensics`, into `40-forensics.log` (`mode_forensics`, lines 916 to 967): every regular non-empty file of `/root/btc-forensics/`, hashed (`forensic_files`, lines 451 to 465); the repository's Releases, twenty a page, through the API without a token (`paged`, lines 540 to 549; `slim_release`, lines 534 to 537); every uploaded asset of a published Release whose record carries a SHA-256 digest, indexed by bytes and digest (`index_assets`, lines 558 to 572); each forensic file some asset holds by both, with the first such asset by tag and name (`plan_rows`, lines 575 to 579); for each Release holding one, its asset list read again through its own paged endpoint and the asset's record asserted — `uploaded`, the file's bytes, `sha256:` and the file's SHA-256, its download URL (`asset_ok`, lines 582 to 585); and each such asset downloaded once, in full, anonymously, hashed as it arrives and compared (`download_checked`, lines 512 to 524). One `P` line a matched file — its path, bytes and SHA-256, the asset, its tag and id, the record's verdict and the download's. **It BLOCKS, and writes no plan, where fewer than 13 files are proved against `tz-44-l0-inputs`** (`PLAN_MIN`, line 114; lines 948 to 952) — the twelve day archives and the manifest map §7 item 167 names — because a plan short of them would mean the Releases' records or the store are not what the map says; and at more than `40` API requests (`get_json`, lines 487 to 496). Otherwise it writes `forensics-plan.json` and its SHA-256 into `state.json`, and prints `FORENSICS PLAN:` with its counts. **The repository stays public** (map §7 item 128): a private one serves no Release without a token, and `forensics` BLOCKS at its first page. **A BLOCK of `forensics` skips B-FORENSICS and holds back nothing after it:** the report says why, and §3.6 runs.

**B-FORENSICS**, the Executor's first, into `41-B-FORENSICS.log` — its paste where the classifier refuses it:

```
cd /root/tz46-work && { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz46-work/wt/research/tz46-capture-room.py forensics-remove; echo "exit=$?"; } >> /root/tz46-work/logs/41-B-FORENSICS.log 2>&1; tail -n 12 /root/tz46-work/logs/41-B-FORENSICS.log
```

`forensics-remove` (lines 970 to 1024) asserts `forensics-plan.json` the plan `state.json` names; hashes every planned file and BLOCKS, removing nothing, where one is not the bytes the plan proved; then, file by file, hashes it again, removes it — the hook allowing that one path for that one call — asserts it gone and appends its row to `forensics-removed.jsonl`: path, bytes, SHA-256, tag, Release id, asset, asset id and the downloaded SHA-256. **G-FORENSIC** (§4.1) closes it. Run again, it removes nothing it has recorded. It holds back nothing of §3.6 to §3.10.

### 3.6 The pair book — B-PAIR-OFF, then G-PAIR

**B-PAIR-OFF**, the Executor's first and the Boss's paste where the classifier refuses it, its output into `50-B-PAIR-OFF.log`. Its band — 07:30:00 to 19:00:00 UTC and neither archive's service running (`band_reading`, lines 394 to 406) — is open at once on any day the run began; the block waits for it in its own text all the same, and **takes its `pairoff` mark inside it** (`mode_mark`, lines 1027 to 1035), right before it starts the run, so that the first start record after the mark is that run's:

```
cd /root/tz46-work && { date -u +%FT%T.%NZ; until nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz46-work/wt/research/tz46-capture-room.py band pairoff >/dev/null 2>&1; do sleep 5; done; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz46-work/wt/research/tz46-capture-room.py band pairoff && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz46-work/wt/research/tz46-capture-room.py mark pairoff && date -u +%FT%T.%NZ && systemctl start --no-block btc-pairbook-archive.service && { nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz46-work/wt/research/tz46-capture-room.py pairwait; r=$?; if [ "$r" -eq 75 ]; then sleep 60; systemctl start --no-block btc-pairbook-archive.service && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz46-work/wt/research/tz46-capture-room.py pairwait; r=$?; fi; echo "pairwait=$r"; date -u +%FT%T.%NZ; if [ "$r" -ne 75 ]; then systemctl disable --now btc-pairbook-archive.timer; echo "timer exit=$?"; systemctl disable --now btc-pairbook.service; echo "pairbook exit=$?"; fi; date -u +%FT%T.%NZ; sleep 30; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz46-work/wt/research/tz46-capture-room.py pair; echo "pair exit=$?"; }; echo "exit=$?"; } >> /root/tz46-work/logs/50-B-PAIR-OFF.log 2>&1; tail -n 60 /root/tz46-work/logs/50-B-PAIR-OFF.log
```

The run is the archive's own, by its own code (§1); `pairwait` (lines 1046 to 1075) waits for its start record, at most 120 s, then for a terminal record with the service idle, at most 3,600 s — the archive's runs took `750` to `2,181` s by its ledger to 2026-10-23 (TZ-32 §6) — and exits `0` on `complete`, `75` on `deferred` and `1` on a halt, an interrupted run, no start or the bound. **A deferral is tried once more, 60 s later:** the archive resumes the same set (tz28 `pending`, lines 229 to 235). **Then the stops, by what the run left.** On `0` the run moved every closed window's streams and restarted the pair book: its timer and the pair book are disabled and stopped. On `1` the archive is halted or cannot finish, and a halted archive has disabled its own timer already (tz28 `halt`, lines 599 to 605): both stops run, because the pair book must not grow a store no archive moves. **On `75` twice nothing is stopped:** the set is pending, the timer's next calendar run resumes it at 03:00:20 UTC, and the pair book and its daily archive go on as before — G-PAIR reads FAIL and the report says so; a later TZ stops it. **Each stop is `systemctl disable --now`**, the documented stop of each unit (map §2.5; §6, process supervision): `Restart=always` restarts no unit systemd was asked to stop. The block ends with **G-PAIR**, `I pair`, 30 s after the stops (§4.2). It holds back nothing of §3.7 but B-TIMER's band, which waits for both archives' services to be idle.

### 3.7 The timer — B-TIMER, with G-TIMER in it

The Executor waits until the band is open — `I band timer` every 60 s, into `60-band-timer.log`, until it exits `0`: **25 to 10 minutes before an elapse of the new calendar, from 10:05:20 to 19:20:20 UTC, neither archive's service running** (`TIMER_BAND` and `TIMER_DAY`, lines 119 to 120; `band_reading`). The reward book's archive's own run off its calendar after B-PAIR-OFF's reloads (§3, its systemd steps) may hold the band closed for minutes. Then **B-TIMER**, the Executor's first and, refused, the Boss's paste at once, its band still open, into `61-B-TIMER.log`:

```
cd /root/tz46-work && { date -u +%FT%T.%NZ; until nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz46-work/wt/research/tz46-capture-room.py band timer >/dev/null 2>&1; do sleep 5; done; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz46-work/wt/research/tz46-capture-room.py band timer && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz46-work/wt/research/tz46-capture-room.py mark timer && date -u +%FT%T.%NZ && install -m 0644 /root/tz46-work/wt/deploy/systemd/btc-rewardbook-archive.timer /etc/systemd/system/btc-rewardbook-archive.timer && systemctl daemon-reload && systemctl restart btc-rewardbook-archive.timer && date -u +%FT%T.%NZ && sleep 5 && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz46-work/wt/research/tz46-capture-room.py timer; echo "exit=$?"; } >> /root/tz46-work/logs/61-B-TIMER.log 2>&1; tail -n 30 /root/tz46-work/logs/61-B-TIMER.log
```

**The `timer` mark is the block's own, taken inside its band** right before the copy, because the first run is the first elapse after it (§4.4) and only the block knows when its band opened. The copy, the reload and the timer's restart follow, each on the one before it; then **G-TIMER**, `I timer` (§4.3), as the block's last step. **A G-TIMER FAIL runs K-46T at once** (§4.8), before the first elapse. B-TIMER holds back nothing of §3.8 but its own first elapse, 10 to 25 minutes later.

### 3.8 The first run — G-TRIGGER, G-RUN, G-TAG and G-NEXT

From the first elapse after the `timer` mark plus 60 s, `I first` every 300 s, appended to `70-first.log`, while it prints `NOT YET` and exits `3` (`mode_first`, lines 1141 to 1219): the run has not begun — at most until 600 s after the elapse, after which it reads `READING G-TRIGGER: FAIL` — or has not ended, or G-NEXT's last slot is not yet due its `slot.json` and 30 s more. **B-RETRY**, only where `first` prints `READING G-RUN: DEFERRED` — the run deferred, the timer still enabled — once, into `71-B-RETRY.log`:

```
cd /root/tz46-work && { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz46-work/wt/research/tz46-capture-room.py mark retry && systemctl start --no-block btc-rewardbook-archive.service; echo "exit=$?"; } >> /root/tz46-work/logs/71-B-RETRY.log 2>&1; tail -n 6 /root/tz46-work/logs/71-B-RETRY.log
```

and `I first` every 300 s again: the archive resumes the same set (tz34 `run`, lines 752 to 806). **B-RETRY runs at most once**; a second `DEFERRED`, a halt, or a run that never begins is G-RUN's or G-TRIGGER's FAIL. `first` exits `0` and prints `FIRST PASS: 4 of 4`, or `FIRST FAIL:` naming every gate that read FAIL, and exits `1` (§4.4); **a FAIL runs K-46T at once** (§4.8).

### 3.9 The units again — G-STILL, and G-TIMER once more

`I still`, into `80-still.log`, reads G-STILL against §3.3's record (§4.6), and prints both archives' runs since that record. `I timer`, into `81-timer-again.log`, must print `G-TIMER PASS: 11 of 11` again, its next elapse the calendar's next; a FAIL runs K-46T.

### 3.10 The room after, and the closing reads

`I room after`, into `90-room-after.log` — §3.4's reads again, with every window the pair book's store keeps and its bytes of stream, and **G-ROOM** (§4.7): exit `0` PASS, `4` FAIL. It writes `room-after.json`. §0.3's block again, verbatim, the memory gate's reads among it, into `91-host-gate-again.log`: H1 to H3 are checked again; H4 and H5 are printed — B-PAIR-OFF and B-TIMER changed what they read — and the memory and disk reads are recorded with their instants and carry no threshold there. Then, into `92-closing.log`:

```
cd /root/tz46-work && ls -la && sha256sum state.json room-before.json room-after.json forensics-plan.json forensics-removed.jsonl; wc -l forensics-removed.jsonl
cat /root/tz46-work/state.json
TZ=UTC systemctl show btc-recorder.service btc-pairbook.service btc-rewardbook.service adv3-bot.service btc-pairbook-archive.service btc-pairbook-archive.timer btc-rewardbook-archive.service btc-rewardbook-archive.timer -p Id -p MainPID -p NRestarts -p ActiveState -p SubState -p UnitFileState -p Result -p MemoryCurrent -p MemoryPeak
TZ=UTC systemctl list-timers btc-rewardbook-archive.timer btc-pairbook-archive.timer --all --no-pager
cmp /root/tz46-work/wt/deploy/systemd/btc-rewardbook-archive.timer /etc/systemd/system/btc-rewardbook-archive.timer; echo "cmp exit=$?"
journalctl -u btc-rewardbook-archive.service -u btc-rewardbook-archive.timer -u btc-pairbook-archive.service -u btc-pairbook-archive.timer -u btc-pairbook.service -o short-iso --since -12h --no-pager | tail -n 80
journalctl -u btc-recorder.service -u btc-rewardbook.service -u adv3-bot.service -o short-iso --since -12h --no-pager | tail -n 40
tail -n 120 /var/lib/btc-rewardbook-archive/archive.log; tail -n 120 /var/lib/btc-pairbook-archive/archive.log
tail -n 20 /var/lib/btc-rewardbook/service.log; tail -n 20 /var/lib/btc-pairbook/service.log
du -sb /root/tz46-work /var/lib/btc-rewardbook /var/lib/btc-pairbook /root/btc-forensics; find /root/btc-forensics -type f | wc -l; df -B1 --output=source,size,avail /var/lib/btc-recorder; free -b
git -C /root/btc-5m-twap ls-remote origin refs/heads/tz-46-capture-room 'refs/tags/rewardbook-streams-*' 'refs/tags/pairbook-streams-*' | tail -n 6
```

`archive.log` of either archive holds its run's own lines — counts, names, times, statuses, process ids and SHA-256 of files — and `service.log` the captures' start and stop lines and one line a slot or a window; none holds a price, a size, a side or a rate. A file a BLOCK left unwritten is named as absent. Then contract §4.2's self-check, `C` the branch's commit, into `99-selfcheck.log`:

```
git -C /root/btc-5m-twap fetch origin
git -C /root/btc-5m-twap rev-list origin/main | grep -c "$C"
git -C /root/btc-5m-twap diff --name-only origin/main origin/tz-46-capture-room
git -C /root/btc-5m-twap diff --numstat origin/main origin/tz-46-capture-room
git -C /root/btc-5m-twap ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
```

Then the report is drafted (§8), and §9 runs.

---

## 4. The gates — fixed here, before any of their data exists

| gate | population | PASS | false failure | power, against |
|---|---|---|---|---|
| **G-FORENSIC** | the files `forensics-plan.json` proves a published Release holds | §4.1 | `0` | `1`: a planned file left, a removal unrecorded or recorded twice, a file of the store removed beyond the plan; a planned file changed since its proof BLOCKS before any removal |
| **G-PAIR** | the pair book's archive's run begun or resumed after the `pairoff` mark; then the pair book, its archive's timer and its service | §4.2 | `0` | `1`: the run not complete, no restart or a FAIL on its resume, a request outside the idle stretch, its tag not at the archive's commit, the pair book or its archive's timer still enabled or active, a process of the pair book left |
| **G-TIMER** | the reward book's archive's timer, in B-TIMER and at §3.9 | §4.3 | `0` | `1`: another file, another or a second calendar, a monotonic trigger, the timer not enabled or not waiting, another next elapse, another unit, the pair book's archive's timer enabled |
| **G-TRIGGER** | the reward book's archive's first start record at or after the first elapse after the `timer` mark | §4.4 | `0`, unless the host's clock steps across the elapse | `1`: no run by 600 s after the elapse; a run by hand, by another timer or off the calendar |
| **G-RUN** | that run's records from that start on, and the service's last result | §4.4 | `0` | `1`: a halt, a second deferral, a request or removal outside the idle stretch, a failed result |
| **G-TAG** | that run's tag on `origin` | §4.4 | `0` | `1`: no tag, a tag at another commit, an annotated tag |
| **G-NEXT** | the slots the reward book decided from that run's first removal to 900 s after its last | §4.4 | `0` while nothing but the run touches the reward book | `1` against a slot left without its `slot.json` or with its task's error record |
| **G-STILL** | the four units, §3.3 to §3.9 | §4.6 | `0` while no other cause restarts them | `1`: a restart or a stop of the recorder, the reward book or the advisor; a change of the pair book but its archive's restarts and B-PAIR-OFF's stop |
| **G-ROOM** | free space and the reward book's stream files at §3.10 | §4.7 | `0` | `1` against a margin under `2,000,000,000` bytes |

**Every gate is exact** — a direct read of the files' bytes, of GitHub's records and downloads, of systemd, of git and of the archives' and the reward book's own records — so its false-failure probability under the model it judges is `0`, and the family's too, under the conditions named. **Nothing is removed before G-FORENSIC's plan is proved; nothing is stopped before the pair book's last archive run has ended; and the timer is replaced only inside its band, its old file one command away** (§4.8).

### 4.1 G-FORENSIC

`forensics-remove` (lines 970 to 1024) after `forensics` (lines 916 to 967). **The plan:** a row a file of the store that some published Release's asset holds by bytes and SHA-256 digest; the row planned only where the Release's own asset list, read through its paged endpoint, records that asset `uploaded` with the file's bytes, `sha256:` and its SHA-256 and the download URL the repository's would be (`asset_ok`, lines 582 to 585), and a full anonymous download of it hashes equal (lines 930 to 946); at least 13 planned rows against `tz-44-l0-inputs`, or no plan (lines 948 to 952). **The removal:** the plan the one `state.json` names by SHA-256 (line 975); every planned file still its proved bytes before the first removal, else BLOCKED with nothing removed (lines 983 to 988), and again right before its own (line 994); each removed by the hook's allowance for that path alone (lines 995 to 999), asserted gone (line 1001), its row appended (lines 1003 to 1007). **PASS** is three checks (lines 1014 to 1017): every planned file absent; every removal recorded exactly once; and the store, by the plan's own count of its files, less exactly the planned ones. It prints `G-FORENSIC PASS: n of n removed` with the bytes, and free space before and after.

### 4.2 G-PAIR

`pair` (lines 1078 to 1108), 30 s after B-PAIR-OFF's stops: the pair book's archive's first start record at or after the `pairoff` mark and that run's records from it on (`first_start`, lines 618 to 624) — every record printed — its tag `pairbook-streams-<A>` read by `git ls-remote`, both units and the service read by `systemctl show`, and `/proc` read for a process of the pair book's exact command line (`processes_with`, lines 352 to 368). **PASS** is eight checks (`pair_reading`, lines 681 to 699): the run `complete`; a `restart` record and a `resume` record that is not `FAIL` — the pair book restarted inside its band and the next window streamed (tz28 `restart_phase` and `resume_phase`, lines 532 to 581); its `complete` record's `started_outside` and `ended_outside` both `0` — every request inside the idle stretch; its tag lightweight at the archive's `commit.txt`, `d8194fd…`; the pair book `inactive` or `failed`, `MainPID` `0`, `disabled`; no process of it; its archive's timer `inactive` and `disabled`; its archive's service not running. Printed beside it: every window the store keeps that holds stream bytes — the residual, `RESIDUAL` lines — and the store's stream and other files. **A G-PAIR FAIL stops nothing further:** B-PAIR-OFF's own branches already stopped what a halted archive cannot move, and left running what a deferral leaves pending (§3.6). Where B-PAIR-OFF's log ends without its `pair` step — its band or its start not reached — the Executor runs `I pair` once and quotes it.

### 4.3 G-TIMER

`timer` (lines 1111 to 1125), read under `TZ=UTC`: eleven checks (`timer_checks`, lines 598 to 615) — `loaded`; `active`, `waiting` or `running`; `enabled`; its fragment `/etc/systemd/system/btc-rewardbook-archive.timer`; its unit `btc-rewardbook-archive.service`; `TimersCalendar` holding one `OnCalendar=` and that one `*-*-* 01/3:30:20 UTC`; `TimersMonotonic` holding no trigger, `USec=` absent; `AccuracyUSec` `1s`; `NextElapseUSecRealtime` exactly the first elapse of the new calendar after the read (`next_calendar`, lines 380 to 387); the installed file's SHA-256 Appendix A's, `7b080428…`; and the pair book's archive's timer `inactive` and `disabled`. **PASS** prints `G-TIMER PASS: 11 of 11` and the next run's instant; a FAIL is a failed assert, exit `1`.

### 4.4 The first run on the new calendar — `first`

`first` (lines 1141 to 1219) takes the first elapse after the `timer` mark, `E`, and the archive's first start record at or after `E − 1` — a run begun then, or a set left pending and resumed then, which counts by that start (`first_start`, lines 618 to 624) — and reads it back **from its records, the archive's `delete.jsonl`, systemd, git and the reward book's own slot records, never from the run's verdicts alone.** Start records between the mark and `E` are printed, each a run off the calendar the block's band should have kept away.

- **G-TRIGGER** (`trigger_reading`, lines 635 to 644) — the trigger systemd handed the run, recorded in that start record (tz34 lines 505 to 507 and 772): `TRIGGER_UNIT` `btc-rewardbook-archive.timer`, its `TRIGGER_TIMER_REALTIME_USEC` from `E` to `E + 60`, and the record within 60 s after it, a second before for whole-second stamps; where systemd set no trigger, the timer's `LastTriggerUSec` read the same way. Printed: which it read, and whether the run took a new set or resumed one.
- **G-RUN** (lines 1189 to 1191) — the run `complete`; at most one deferral, B-RETRY's; no halt; the service's `Result` `success` and `ExecMainStatus` `0`; its `complete` record's `started_outside` and `ended_outside` both `0` (tz34 `final_phase`, lines 734 to 749). Printed: its requests, removals, files and bytes.
- **G-TAG** (line 1201) — `rewardbook-streams-<A>` on `origin`, lightweight, at the archive's `commit.txt`, `6a61525…`.
- **G-NEXT** (lines 1203 to 1212) — the slots whose decision `S − 6` lies from the run's first removal to 900 s after its last (`next_slots`, lines 647 to 654), each read 30 s after its `slot.json` is due: **FAIL** where its task left an `error` record in the reward book's `runtime.jsonl` or the slot has no `slot.json`; **PASS** where a `slot.json` of the process the run began beside shows the stream opened, with no off reason, no error and not stopped; **UNDECIDABLE** otherwise (`next_verdict`, lines 657 to 673). It reads the worst over its slots and fails on FAIL, or on no slot at all.

**PASS** is all four: `FIRST PASS: 4 of 4`. **Exit `3`** while the run has not begun — to `E + 600` — or not ended, while it reads `DEFERRED`, or while G-NEXT's last slot is not yet due; **exit `1`** on any FAIL.

### 4.5 What the timer's first run proves of the calendar

A run fired by the timer at a new-calendar elapse, complete, its streams on a Release under its tag and the next slots streamed by the same process: the archive runs unattended on its new cadence. **Not established:** the seven other elapses of a day — the next TZ that touches the host reads the archive's ledger, whose every run records its trigger and its store's streams at its end; and the store's peak between two runs, which `room after` reads once and the ledger's `complete` records read at every run.

### 4.6 G-STILL

From §3.3 to §3.9 the recorder's, the reward book's and the advisor's units keep their `MainPID`, `NRestarts` and `ActiveState`; the pair book's keeps them, or changes by its archive's own restart records alone — a chain from the recorded `MainPID` to the current one, `NRestarts` one higher at each — and is then, once the `pairoff` mark is taken, stopped: `MainPID` `0`, `inactive` or `failed` (`still_reading`, lines 702 to 721; `mode_still`, lines 793 to 813). **A FAIL names its cause from the units' journal**, §3.10's (map §7 item 120), and stops nothing.

### 4.7 G-ROOM

`room after` (lines 877 to 913): the room — free space plus the reward book's stream files by their directory entries, the bytes its archive gives back — less `STREAM_FLOOR`, `7,300,000,000`, and `PEAK`, `445,535,636`, is the margin (`room_reading`, lines 590 to 595). **PASS** where the margin is at least `2,000,000,000` bytes (`ROOM_MIN`, line 130): about ten days at the fastest drift beside the streams map §6 records, `187,760,570` bytes a day, and about 46 at TZ-26's base, `43,500,000`. The pair book's residual stream files are not in the room: no archive takes them while it stays stopped. Printed beside it: the margin's days at both drifts [modelled], and every window the pair book's store keeps. **A FAIL stops nothing:** the report gives every tree's bytes (§3.10) and the next TZ takes the next lever (§1).

### 4.8 The stops — CANON hard rule 14

**K-46T** returns the reward book's archive to TZ-34's calendar, the deployment proved by 30 complete runs from 2026-10-29 to 2026-11-16 (TZ-45 report §2.8), and changes nothing else: the archive's code and state are untouched by this TZ, so the stop that leaves the capture its proven room is the revert, not the archive's own stop — K-34, `systemctl disable --now btc-rewardbook-archive.timer`, would leave the reward book's store to the floor within days (map §2.6). **Authorized and run at once, and once,** on the first FAIL of G-TIMER, G-TRIGGER, G-RUN, G-TAG or G-NEXT, the gates that judge the new calendar; the Executor's first, its paste where the classifier refuses it, into `K-46T.log`:

```
cd /root/tz46-work && { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz46-work/wt/research/tz46-capture-room.py mark revert && install -m 0644 /root/btc-5m-twap/deploy/systemd/btc-rewardbook-archive.timer /etc/systemd/system/btc-rewardbook-archive.timer && systemctl daemon-reload && systemctl restart btc-rewardbook-archive.timer && sha256sum /etc/systemd/system/btc-rewardbook-archive.timer && TZ=UTC systemctl show btc-rewardbook-archive.timer -p ActiveState -p SubState -p UnitFileState -p TimersCalendar -p TimersMonotonic -p NextElapseUSecRealtime; echo "exit=$?"; } >> /root/tz46-work/logs/K-46T.log 2>&1; tail -n 14 /root/tz46-work/logs/K-46T.log
```

The primary checkout's file is TZ-34's, `bf5af025…`, map §0's `frozen` row, which `sha256sum` prints; systemd's reads must show `OnCalendar=*-*-* 01:30:20 UTC` and `OnActiveUSec=30min`, and TZ-34's `OnActiveSec` runs the archive 1,800 s after the restart. **Where the archive itself halted**, K-46T restores its calendar and not its runs: a halt refuses every run until a TZ appends a `clear` (map §3), and the report says so first — the store then fills to the floor within days.

**B-START-RB**, only on a G-NEXT FAIL and only where `systemctl is-active btc-rewardbook.service` then reads other than `active` — the reward book halted, which its unit does not restart (map §2.6) — after K-46T, into `K-46T.log`:

```
cd /root/tz46-work && { date -u +%FT%T.%NZ; systemctl start btc-rewardbook.service; echo "exit=$?"; sleep 60; systemctl is-active btc-rewardbook.service; TZ=UTC systemctl show btc-rewardbook.service -p MainPID -p NRestarts -p ActiveState -p ActiveEnterTimestamp; } >> /root/tz46-work/logs/K-46T.log 2>&1; tail -n 8 /root/tz46-work/logs/K-46T.log
```

It runs at most once. **B-PAIR-OFF carries its own stops** (§3.6): `systemctl disable --now` of the pair book's archive's timer and of the pair book, the documented stop of each, after its last archive run or its archive's halt — and none after a second deferral, which leaves both as they were. **G-FORENSIC, G-PAIR, G-STILL and G-ROOM authorize no stop**: a removal proved before it is made needs no undoing, and the rest read what the blocks left. **Under PASS no block of this section is run.**

### 4.9 What a PASS establishes, and what it does not

The reward book's store is the only one the disk refills; its archive runs eight times a day, its first run on the new calendar fired by the timer and complete; the pair book is stopped, its last archive run complete; the forensic store keeps no file the plan found a public Release to hold; and the room stands at least `2,000,000,000` bytes above the floor and the store's peak. **Not established:** that every slot of a later day streams — the reward book can still lose a slot to the venue's socket (map §2.6, 2026-11-06), to the package manager's restart of its unit (map §7 item 120; §0.3 prints needrestart's configuration) or to the host; that the margin lasts as modelled — the drift beside the streams is two reads' estimate, and every later TZ reads the room again; and anything of a stream's content.

---

## 5. The instrument and the timer

`research/tz46-capture-room.py`, Appendix A, fixed by the Architect as this TZ's Validation and written byte for byte. **The standard library alone**, run under `/root/tz04a-env` — Python 3.12.3, the captures' interpreter, which nothing here modifies. **It loads no other instrument.** TZ-27's file, which TZ-28's and TZ-34's load, installs an audit hook that refuses every change under the forensic store (`research/tz27-pairbook-archive.py` lines 214 to 259), so this file carries its own hook, `policy` (lines 185 to 223) applied by `_audit` (lines 226 to 236) from line 239: writes inside the work tree alone; of the reward book's store, its `slot.json` files and `runtime.jsonl` opened and nothing else; nothing of the pair book's, the recorder's or the chain book's store opened; a file of the forensic store removed only by `forensics-remove`, only where planned and only for its own call, and written only by `reclaim`'s exclusive create; and no host looked up but GitHub's, its download hosts and the loopback. **Its own code:** the TZ's constants (lines 58 to 145); the hook (lines 147 to 239); helpers — `floors`, `show` under `TZ=UTC`, `stamp_of`, `ledger`, `processes_with` and `ls_remote_tag` (lines 241 to 375); the calendar and the bands (lines 377 to 406); the stores by their directory entries and the forensic store (lines 408 to 476); GitHub, anonymous, every header fixed (lines 478 to 553); the plan's pure functions (lines 555 to 585); the readings as pure functions — G-ROOM, G-TIMER, a run's start and state, G-TRIGGER, G-NEXT, G-PAIR, G-STILL and NUMBER (lines 587 to 729); the modes (lines 731 to 1302); the self-test and its loopback GitHub (lines 1304 to 1612); and `main` (lines 1615 to 1644). It writes no second implementation of an archive's run, upload, proof, removal, idle stretch or ledger: both archives run their own code, and it reads their records. **Exits:** `0` every assert held; `1` a failed assert, named, a BLOCK whose message says so, or `first`'s FAIL; `3` NOT YET, or a band closed; `4` a reading's FAIL that stops nothing — G-STILL, G-PAIR, G-ROOM; `pairwait`'s `75` deferred. Every mode prints, on every exit, its peak memory, the opens its hook refused, its opens under the reward book's store, its API requests, downloads and bytes, and its files removed (lines 1635 to 1639). Run with `-O` it refuses to start (lines 51 to 53).

`deploy/systemd/btc-rewardbook-archive.timer`, Appendix A, replacing TZ-34's: its first and fourth lines' words, `OnCalendar=*-*-* 01/3:30:20 UTC` in place of `OnCalendar=*-*-* 01:30:20 UTC`, and no `OnActiveSec=1800`; `AccuracySec=1s`, `Unit=btc-rewardbook-archive.service` and `WantedBy=timers.target` unchanged. `systemd-analyze verify` on systemd 255 reads it without a word, and refuses a calendar spec that does not parse [run by the Architect]. **The service it starts is TZ-34's, unchanged** — a oneshot, `Restart=no`, `TimeoutStartSec=21600`, `Nice=19`, `MemoryMax=128M` — and its stop is `systemctl disable --now btc-rewardbook-archive.timer`, as before (CANON hard rule 14).

---

## 6. Cost

At the populations' upper bounds (§10 C4): `selftest` `0.64` to `0.68` s; `fingerprint` `0.11` s over 64 rows; `still`, `scratch`, `mark`, `band`, `timer`, `pair` and `first` under 1 s each; `room` under 2 s, listing at most about 3,700 window directories of the pair book's store — one a window since 2026-10-10 — and about 21 day directories of the reward book's; **`forensics`** — the store hashed, `583,581,855` bytes at 2,532 files by TZ-45's reads and the 47 its §9 added, at about `200,000,000` bytes a second, under 4 s; at most `40` API requests — the repository's Releases, at most 91, one a tag at the Architect's read of its refs, five pages of twenty, and one asset list a Release that holds a match — and the matched assets downloaded once each, at most the store's bytes, about `229,000,000` if TZ-43's files match too, at `14,140,406` bytes a second, TZ-27's measured download rate (map §6, GitHub Releases), about 16 s; `forensics-remove` hashing the plan's files twice, under 6 s at the store's whole size; `reclaim` under 2 s. **The blocks' wall clock:** B-PAIR-OFF's last archive run, 20 to 45 minutes — its upload and proof of about seven hours of the pair book's streams, its restart inside the band and the next window read — bounded at `3,600` s a try by `pairwait`; B-TIMER's band, up to 3 h away, and its first elapse 10 to 25 minutes after it; the first run about 5 minutes and G-NEXT's last slot up to about 30 minutes after it; the closing reads and §9 about 15 minutes. **About 2 to 5 h in all**, most of it waiting.

---

## 7. Validation

The report shows each, with its count, and says whether it is asserted:

- **V1** — `FINGERPRINT PASS` at §0.2 and §3.1: revision `2026-11-16-a`; anchors 6, 4 re-derived; rows `64` = `61` + `2` + `1`, 61 `frozen` equal. Asserted.
- **V2** — `NUMBER PASS - 2 of 2` at §0.5 and §3.1; the refs reported against §0.5's 160 lines, every difference named. Asserted.
- **V3** — §0.1's script at §0.1 and §3.1: two files, each its lines, bytes and SHA-256 of §0.1's table; in the worktree the timer `replaced` from `bf5af025…`. Asserted.
- **V4** — the branch: two paths, `--numstat` `1644 0` and `3 4`, the commit on `origin` the worktree's `HEAD`. Asserted by §3.1's reads.
- **V5** — `SELFTEST PASS: 29 checks`, its `opens refused: 1` its own. Asserted.
- **V6** — §3.3: `still: recorded`; `scratch`'s listing; `RECLAIM PASS` where it named any directory earlier, each removal's `test -e` `exit=1`. Asserted where it runs.
- **V7** — `room before`: every count printed. Recorded, not asserted: a baseline.
- **V8** — `FORENSICS PLAN:` — files proved against `tz-44-l0-inputs` at least 13, API requests at most 40 — then `G-FORENSIC PASS: n of n`, the bytes freed, and free space before and after. Asserted; or `forensics` BLOCKED and B-FORENSICS skipped, with the reason.
- **V9** — B-PAIR-OFF: `pairwait=0`, both stops' `exit=0`, `G-PAIR PASS: 8 of 8`, and the residual's windows and bytes. G-PAIR's verdict printed, the stops' exits recorded.
- **V10** — B-TIMER inside its band: the `timer` mark, the copy, the reload and the restart each `exit=0`, then `G-TIMER PASS: 11 of 11`. Asserted.
- **V11** — `FIRST PASS: 4 of 4`, with every `NOT YET` line before it and B-RETRY where it ran. Printed, exit `0`.
- **V12** — `G-STILL PASS`, its cause where it FAILs; `G-TIMER PASS: 11 of 11` again. Printed; G-TIMER asserted.
- **V13** — `G-ROOM PASS`, the room, the margin and its days at both drifts [modelled]. Printed, exit `0` or `4`.
- **V14** — every mode's printed peak, each under `66,536,581`, and every memory read with its instant and its floor. Recorded.
- **V15** — every free-space read with its instant: §0.0, §0.3, every mode's `floors`, `room` twice, both host gates. Recorded.
- **V16** — contract §4.2's self-check: `0`; the two paths; their `--numstat`; nothing. Asserted.
- **V17** — §9: `RECLAIM PASS`; `/root/tz46-work` gone, `test -e` `exit=1`; the worktrees the primary checkout and `/root/btc-recorder-svc`; the forensic store's count — `2,579` at TZ-45's close, less G-FORENSIC's removals, plus §9's copies and B-RECLAIM-SCRATCH's. Asserted where a command asserts it.

---

## 8. The report

`CryptoReports/TZ-46-capture-room-report.md`, contract §8's sections in their order. **§2 Measurements** gives, beside §7's lines: **the room** — `room before` and `room after` side by side, every count; **the trees** — every `du -xsb` line of both host gates, the sixteen largest by name, and the journal's size and journald's and needrestart's configuration as printed; **the forensic store** — every `P` row of the plan and every `X` row of the removal, each file by path, bytes and SHA-256 and its asset by tag, name and id, with the store's files and bytes before and after; **the pair book** — B-PAIR-OFF's log whole, the final run's every record, its tag, G-PAIR's eight lines and every `RESIDUAL` window; **the timer** — B-TIMER's log whole and both G-TIMER reads, its eleven lines each; **the first run** — every `first` read, its records, G-TRIGGER's evidence, G-RUN's figures, G-TAG's object and G-NEXT's slots; **both archives' runs since §3.3** — on the calendar or off it, each beside the systemd reload it followed (map §7 items 115, 129 and 166); **G-STILL's two reads**, the units' memory at each; and **every free-space and `MemAvailable` read**, with its instant and its bound. **§6** names every departure, every refusal by the classifier with the block, its words and who ran it, and every block run by the Boss with the instant. The report prints no price, size, side, book hash, rate, competitiveness or outcome.

---

## 9. Reclaim — the host left clean (CANON hard rule 15)

**What a file is kept for:** a committed report prints its SHA-256, whole or as a prefix of 16 to 64 hex characters, or it is kept by name: `state.json`, `forensics-plan.json`, `forensics-removed.jsonl`, `room-before.json`, `room-after.json` and every file under `logs/` (`by_name`, lines 1231 to 1233). `reclaim` copies each into `/root/btc-forensics/` as `<tree>--<path with / as -->`, by exclusive create, and verifies its hash; a name already there with the same hash is counted as held, and with another hash is a failed assert; after each copy free space stays at or above `7,400,000,000` bytes or it BLOCKS (`mode_reclaim`, lines 1254 to 1302). **No file of this run is held by a Release**, so none is left to one. The branch worktree is not copied: `reclaim` asserts that `git status --porcelain --ignored` in it prints nothing and that its `HEAD` is its upstream's (`pristine`, lines 1236 to 1243), so `git worktree remove` needs no `--force`; the stage's two files, whose SHA-256 the report prints, are copied like any other, and `selftest-tmp`, which the self-test removes, is not walked. The report's draft in `CryptoReports/` counts as a report. **No `reclaim`'s output is filtered** (map §7 item 119). B-RECLAIM-SCRATCH is §3.3.

**B-RECLAIM-OWN**, last, after §3.10 and with the report drafted. **Its output is written to no file; the report quotes it verbatim from the session**, every line of it:

```
cd /root/tz46-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz46-work/wt/research/tz46-capture-room.py reclaim /root/tz46-work
cd /root/btc-5m-twap && git -C /root/btc-5m-twap worktree remove /root/tz46-work/wt; echo "exit=$?"
rm -rf /root/tz46-work; echo "exit=$?"
test -e /root/tz46-work; echo "exit=$?"
git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
find /root/btc-forensics -type f | wc -l
df -B1 --output=source,size,avail /var/lib/btc-recorder
```

`reclaim` must print `RECLAIM PASS` before the removals. **Its paste**, where the classifier refuses any line of it — every step chained to the one before it, the removals reached only after `RECLAIM PASS`; its output goes to the Boss's terminal, the tree its log would be in being removed:

```
(cd /root/tz46-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz46-work/wt/research/tz46-capture-room.py reclaim /root/tz46-work) && cd /root/btc-5m-twap && git -C /root/btc-5m-twap worktree remove /root/tz46-work/wt && rm -rf /root/tz46-work; test -e /root/tz46-work; echo "exit=$?"; git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list; find /root/btc-forensics -type f | wc -l
```

Where the Boss ran it, the Executor verifies it by its own reads — `test -e /root/tz46-work; echo "exit=$?"`, `git -C /root/btc-5m-twap worktree list`, `find /root/btc-forensics -type f | wc -l` and `sha256sum /root/btc-forensics/tz46-work--*`, each copy's hash against the report's — and the report quotes those reads; a refused first attempt is quoted too. The branch `tz-46-capture-room` stays on `origin` and as a local ref; only its working tree goes. **Kept:** the running units' code trees, the stopped pair book's code tree `/root/btc-pairbook-svc` and its archive's `/root/btc-pairbook-archive-svc` and `/var/lib/btc-pairbook-archive`, the capture roots — the pair book's residual windows among them — the forensic store and the Releases: data and code, never scratch.

---

## 10. Pre-send checks

Performed by the Architect on 2026-11-16 against this file, start to end, in a reading separate from its writing. Every committed file was read at `origin/main` `53e5690354d0febc3abbbfefb4836385eaeadbc3`; Appendix A's two files at §0.1's SHA-256.

| # | check | result |
|---|---|---|
| **C1** | scope against body | **Named by the body.** *Repository, written:* `research/tz46-capture-room.py` and `deploy/systemd/btc-rewardbook-archive.timer` on the branch, `CryptoReports/TZ-46-capture-room-report.md` on `main` — §2 item 1. *Repository, read:* this TZ, `SYSTEM-MAP.md` and the 64 files of its §0 table by `fingerprint`; `research/tz33-reward-book-capture.py` by `selftest`; the five unit files §0.3 compares; `research/tz26-…`, `tz28-…`, `tz33-…` and `tz34-…` hashed in their host copies by §0.3, and `tz27-…` cited. *Host, written:* `/root/tz46-work/**` and the worktree under it — §2 item 10; `/etc/systemd/system/btc-rewardbook-archive.timer` by B-TIMER and K-46T — §2 item 2; files of `/root/btc-forensics/` removed by B-FORENSICS and copied by `reclaim` — §2 item 5; earlier session directories under `/tmp/` removed by B-RECLAIM-SCRATCH — §2 item 10. *Units acted on:* the six of §2 item 2, each by the block it names. *Host, read:* both stores by names and sizes, the reward book's `slot.json` files and `runtime.jsonl`, both captures' `service.log` — §2 item 3; both archives' ledgers, `archive.log`, `delete.jsonl` and `commit.txt` — §2 item 4; `/proc`, systemd's records and the journal, the package manager's timers and history, journald's and needrestart's configuration and `du` of every tree — §2 item 6. *Outputs, by content class:* `forensics-plan.json` and `forensics-removed.jsonl` carry paths, bytes, SHA-256 and assets' tags, names and ids; both room files counts and bytes; `first` a slot record's process, flags and counts; the closing reads' `service.log` and `archive.log` lines counts, names, times, statuses and hashes; none carries a price, a size, a side, a book's hash, a rate, a competitiveness or an outcome — §2 item 8. *Network:* the instrument's anonymous GitHub requests — §2 item 7. **Five intersections found in this reading, each resolved by naming it in §2:** both captures' `service.log` (item 3); both `archive.log` (item 4); the host's other reads (item 6); `gh pr create`, which carries `gh`'s credential, against item 7's "no request carries a credential" (item 7); and the session's own trees with B-RECLAIM-SCRATCH's removals (item 10, new). None left. |
| **C2** | origin of every expectation | **Every fixed literal of §5 and §7, of two kinds and no third.** *Quoted from a committed artifact, named:* revision `2026-11-16-a`, the six anchors and rows `64` = `61` + `2` + `1` (map §0, counted by an independent parse); `bf5af025…`, `1d8aa514…`, `46a019d6…`, `a276bbb9…` and `caed70d9…` (map §0, each equal to `sha256sum` of `origin/main`'s file); `6a615257…` and `d8194fd5…` (the tags `git ls-remote origin` printed; map §2.5 and §3); `7,300,000,000` and `2,200,000,000` (tz33 lines 190 and 189); `4,500,000,000` (tz26 line 132); `31,823,974`, `74,127,110` and `1,779,050,648` (TZ-45 §0.4); `296,688,123` bytes between reads at 07:49:10 and 10:23:57 UTC, `9,287` s (map §6, disk; TZ-45 report §2.9); `43,500,000` and `187,760,570` (map §6, headroom); `58,953,728` and `49,168,384` (map §6, memory); `14,140,406` and `60` an hour (map §6, GitHub Releases); `13` and `186,490,880` (map §3 and §7 item 167: twelve archives and their manifest); `2,579` (map §3). *Computed by an implementation independent of the one under test:* both files' lines, bytes and SHA-256 by `wc` and `sha256sum`; `--numstat` `1644 0` and `3 4` by `git diff --no-index`; `29`, `11` and `8` by counting `ok(` calls and the returned dicts' keys with `ast`; `PEAK` `445,535,636` = 14 × `31,823,974`; `115,007,779` = ⌈`296,688,123` × 3,600 / `9,287`⌉ and `236,418,611` = ⌊1.25 × (`74,127,110` + `115,007,779`)⌋ by `Fraction`; `133,073,162` = 2 × ⌈`55,492,608` × `58,953,728` / `49,168,384`⌉ by `Fraction`; the calendar's eight elapses a day by `systemd-analyze calendar --iterations=9`. *Fixed by the Architect and derived in §0.4 and §4.7:* `7,600,000,000`, `2,300,000,000`, `7,400,000,000`, `2,000,000,000`, `40`, `20` and the bands. **No expectation depends on a quantity this TZ measures:** G-ROOM compares the measured room with a fixed literal, and every other gate is an identity of records. |
| **C3** | shape of every diff | **One file replaced.** `research/tz46-capture-room.py` is absent from `origin/main` (`git cat-file -e` exit `128`) and is new. `deploy/systemd/btc-rewardbook-archive.timer` replaces TZ-34's, `13` lines, `428` bytes, `bf5af025…`: its line 1, the comment; its line 4, `Description=`; and its lines 7 and 8, `OnCalendar=*-*-* 01:30:20 UTC` and `OnActiveSec=1800`, replaced by `OnCalendar=*-*-* 01/3:30:20 UTC` — `3` lines added, `4` removed, by `git diff --no-index`; its other 9 lines unchanged. The words "insertions only" appear nowhere in this file. The report is new on `main`. |
| **C4** | cost of every check | At the populations' upper bounds (§6): `selftest` `0.64` to `0.68` s and `fingerprint` `0.11` s over 64 rows, measured; `room` over at most about 3,700 window directories and 21 day directories, under 2 s; `forensics` over the whole forensic store — `583,581,855` bytes at 2,532 files by TZ-45's reads, and the 47 its §9 added; the store's size bounds the population, not a predicted share of it — hashed under 4 s at about `200,000,000` bytes a second, at most `40` API requests, downloads at most the store's bytes, about 41 s at `14,140,406` bytes a second, and about 13 s at the thirteen known matches; `forensics-remove` twice the planned bytes hashed, under 6 s at the store's size; every other mode under 1 s. **Waits, not compute:** `pairwait` at most `3,600` s a try, two tries; B-TIMER's band at most 3 h away; `first` at most 600 s past the elapse for the run to begin, then the run's own length. **No check reaches `3,600` s of compute.** Fail-fast bounds: `PAIRWAIT` start `120` s — a start record is written within seconds of `systemctl start`; `FIRST_LATE_S` `600` — the timer's `AccuracySec=1s`; `API_MAX` `40` — five pages at the repository's at most 91 Releases and one asset list a Release that holds a match, a few, under GitHub's `60` an hour. |
| **C5** | every count | V1: `64 = 61 + 2 + 1`, over map §0's table at `53e5690` by an independent parse, equal to the instrument's `fingerprint`. V2: `2 of 2`, over `CryptoTZ/` and `CryptoReports/` at `origin/main` — no `TZ-46-` file today, `TZ-46-capture-room.md` alone after the upload. V2's `160` refs: `HEAD` 1, branches 22 (`main` and 21 `tz-*`), pull heads 44, `pairbook-streams-*` 57, `rewardbook-streams-*` 30, two annotated tags with their peeled lines 4, two lightweight tags 2. V3: `2` files over Appendix A's fenced blocks, which §0.1's script finds. V4: `2` paths over the branch's diff. V5: `29` over `mode_selftest`'s `ok(` calls. §0.3: `12` = H1 1 + H2 2 + H3 1 + H4 4 + H5 2 + memory 1 + disk 1. G-TIMER `11` over `timer_checks`' keys; G-PAIR `8` over `pair_reading`'s; FIRST `4` over `mode_first`'s readings; G-FORENSIC `3` over its checks (lines 1014 to 1017). The calendar's `8` elapses a day: `CAL_FIRST_S + k · CAL_STEP_S`, `k` 0 to 7. `PEAK_SLOTS` `14`: a run at `hh:30:20` takes the slots to `hh:00`, `S + 910 + 60 ≤ A` (tz34 lines 119, 132 and 281), so before the next run the store holds the twelve that run will take, the closed `hh+3:15` and the open `hh+3:30` — 14 at most. |
| **C6** | every population | Each of §4's nine gates names its population in its own column. §0.4's peaks: `forensics` over eight runs against a loopback GitHub in another process, on the stand-in of 140 Releases and 13,072 assets; `selftest` and `fingerprint` over their runs on these bytes; `reclaim` one run over a stand-in tree. §1's rates: over TZ-45's two reads of 2026-11-16 and map §2.5's and §2.6's runs; the room over TZ-45's 10:23:57 UTC read; the drift over the room at TZ-28's closing read of 2026-10-11 and TZ-45's of 2026-11-16 [modelled]. §6's figures: per mode, at its population's upper bound. |
| **C7** | every signature and every behaviour | **Read at `53e5690`, as the files hold them.** tz33: `def stream_off_reason(selected, n_members, free, total):` (1294) — `if free < STREAM_FLOOR: return "floor"` (1300 to 1301); `def stream_bytes_total(root):` (1279) — `f.name.endswith(".stream.jsonl.gz") and SLOT_FILE_RE.fullmatch(f.name)` (1289); `def free_bytes():` (439) — `st = os.statvfs(DISK_PATH)` (440), `DISK_PATH = "/var/lib"` (127); `self.free = free_bytes` (1453); the call `stream_off_reason(sel is not None, len(members), book.free(), stream_bytes_total(book.root))` (1531); `STREAM_FLOOR = 7300000000` (190), `RESOURCE_FLOOR = 2200000000` (189). tz26: `STREAM_FLOOR = 4500000000` (132); `def stream_bytes_total(root):` (794) — `f.name.startswith("stream") and f.name.endswith(".jsonl.gz")` (804). tz34: `def inventory(root, a, max_assets=tz27.RUN_MAX_ASSETS):` (271) — `if s + SLOT_JSON_AT + SETTLE_S > a:` (281), `SLOT_JSON_AT = 910` (119), `SETTLE_S = 60` (132); `def run(env):` (752) — the start record's `"trigger": env.trigger` (772), `self.trigger = {"unit": os.environ.get("TRIGGER_UNIT"), "realtime_usec": os.environ.get("TRIGGER_TIMER_REALTIME_USEC"), …}` (505 to 507); `def hold(env, led, a, phase):` (613) — `while env.archive_active():` (617), `archive_active` the pair book's archive's `ActiveState` in `RUNNING` (539 to 540); `def final_phase(env, led, a, rdir, doc, reward0):` (734) — `"started_outside"` and `"ended_outside"` in its `complete` record (745 to 746). tz28: `def run(env):` (608); `def restart_phase(env, led, a, doc):` (532) — `assert kv.get("ActiveState") == "active", "the pair book is %r: not restarted"` (536); `def resume_phase(env, led, a, W, pid):` (571) — its record `{"event": "resume", "run": a, "reading": reading, "T": T}` (580) and `assert reading != "FAIL"` (581); `def final_phase(env, led, a, rdir, doc):` (584) — `"started_outside"` and `"ended_outside"` (593 to 594); `def pending(recs):` (229) — the last start's run where no terminal record follows (231 to 235), `TERMINAL = ("complete", "empty", "halt")` (109); `def halt(env, led, a, phase, reason):` (599) — `rc = env.disable_timer()` (602). tz27: `def policy(mode, event, args, work, allowed):` (214) — `if _protected(q) or _under(q, FORENSICS): return "a change under a protected root"` (254 to 255). **Appendix A:** 43 function spans this file cites, each equal to the span Python's `ast` gives; the code's sections from their headers (58, 147, 241, 377, 408, 478, 555, 587, 731 and 1304) and `main` (1615 to 1644), its `finally` printing at 1635 to 1639; and every in-function line §4 cites — 930 to 952, 975, 983 to 1020 and 1189 to 1212 — re-read. **Five citations were corrected in this reading:** §4.1's asset-list re-read begins at 930, not 932; G-RUN spans 1189 to 1191; §5's code sections run from their headers; `main`'s prints are 1635 to 1639; and the resume record is tz28's line 580. |
| **C8** | every cross-reference | Resolved by reading each referenced text in this session, never from memory. **Map `2026-11-16-a`, the list the header copies (map §7 item 141):** §0, the fingerprint gate and its table; §1, the refs; §2.5, the pair book, its archive, its idle stretch, its restart and the reserve; §2.6, the reward book — its store's bounds as its code reads them, its archive, the reserve; §3, the forensic store, the worktrees and the code trees; §6, its rows host, host identity, language, git remote, both disk rows, capture cost, headroom, process supervision, memory, GitHub Releases, sandbox limit — network, sandbox limit — destructive actions, and harness; §7 items 106, 115, 119, 120, 124, 125, 128, 129, 131, 132, 137, 138, 140, 141, 143, 144, 150, 156, 166, 167 and 170, each read whole, its disposition column included, each supporting the sentence that cites it. **CANON `2026-11-16-a`:** PART II's L track — L1 and its first step, the capture's room; §1.6's re-opening rule; hard rules 2, 5, 8, 11, 13, 14, 15 and 17, the last added in this reading for the timer's `frozen` row. **Contract:** §1, §4, §4.2, §5 and §8. **Other artifacts:** TZ-33 §1's floor derivation; TZ-34 §0.4; TZ-32 §6, the archive's runs of `750` to `2,181` s; TZ-45 §0.4 and its report §2.8, §2.9 and §2.13. **This TZ:** §0.0 to §0.5, §1 to §9 and Appendix A, each supporting the sentence that cites it. **PART VI's fifth rule:** item 170's "Before L1's measurement days, a TZ gives the capture room" is this TZ, and its three levers are weighed in §1; item 167's wording of hard rule 15 is in CANON `2026-11-16-a`, and its housekeeping step is §3.5; item 166's removal of `OnActiveSec` from both timers is done for the reward book's archive's by B-TIMER, and for the pair book's archive's replaced by its disabling, said so in §1. No quotation of the Boss's words. **None unresolved.** |

**Performed in the Architect's session, on these bytes:** §0.1's script on this file — both files `created` into an empty tree, and the timer `replaced` over TZ-34's, at Appendix A's hashes; `selftest`, `SELFTEST PASS: 29 checks`, under Python 3.12.3; `fingerprint` against a clone of `origin/main` at `53e5690`, `FINGERPRINT PASS`, 61 of 61 `frozen` rows equal; `number`, BLOCKED as it must be before the upload, `CryptoTZ/` holding no `TZ-46-` file; `timer`, `first`, `pair`, `still`, `band`, `mark`, `room before`, `room after` and `pairwait`, complete and deferred, against stand-in stores, ledgers and units with `systemctl`, `git ls-remote` and `/proc` stood in — `G-TIMER PASS: 11 of 11`, `FIRST PASS: 4 of 4`, `G-PAIR PASS: 8 of 8`, `G-STILL PASS`, `G-ROOM PASS`; `forensics` against a loopback GitHub in another process at 140 Releases and 13,072 assets, eight runs, 13 files planned at each, the plan byte for byte the same between runs against one server; §0.0's readiness read on stand-in ledgers, a deferred run among them, `ready=0`; `reclaim` over a stand-in tree; `systemd-analyze verify` on systemd 255 over Appendix A's timer, silent, and over a copy with a broken calendar, refused; and `systemd-analyze calendar` over the new calendar, its normalized form itself and eight elapses a day.

**Not performable in this session, and converted to conditions the Executor evaluates and BLOCKS on** (CANON hard rule 13): the host — H1 to H5, the memory and disk gates (§0.3), §0.0's readiness and §0.5's refs; the repository's Releases through GitHub's API — this session's proxy refuses the API for the repository and the harness refused attaching it with a credential, so the Releases' count, their assets' digests and whether a list carries every asset were not read here: `forensics` writes no plan below 13 files proved against `tz-44-l0-inputs`, re-reads each matched Release's assets through their own paged endpoint and proves each by a full anonymous download (§3.5), and a BLOCK of it holds back nothing after it; the forensic store's contents — the same condition; the host's systemd reading of the new timer — G-TIMER inside B-TIMER, K-46T on its FAIL (§3.7); whether the host's systemd hands a timer's service `TRIGGER_UNIT` — G-TRIGGER reads `LastTriggerUSec` where it does not, and prints which it read (§4.4); the pair book's archive's last run on the host — `pairwait`, B-PAIR-OFF's branches and G-PAIR (§3.6); and the reward book's own records across the removals — G-NEXT, K-46T on its FAIL and B-START-RB where the reward book is down (§4.8).

---

## Appendix A — the instrument and the timer, byte for byte

Extracted by §0.1's script; each block's content is the file.

### `research/tz46-capture-room.py`

```python file=research/tz46-capture-room.py
#!/usr/bin/env python3
"""TZ-46 - the capture's room: the reward book's archive every three hours, the pair book stopped after its last
archive run, the forensic store's copies of what a public Release holds removed, and the room above the reward
book's stream floor read before and after.

    fingerprint       map section 0 against the primary checkout
    number            CANON hard rule 2: of the number TZ-46, this TZ's file alone under CryptoTZ/, no report
    selftest          every rule of this file, on literals, temporary trees and a loopback server only
    still             the four units: the first call records them, a later one reads G-STILL
    scratch OWN       the UUID directories beside this session's own, each named live or earlier
    room LABEL        the disk, before or after: free space, both stores' stream and other bytes, the forensic
                      store and both archives' recent runs; after, G-ROOM, exit 4 where it reads FAIL
    forensics         every file of the forensic store that a public Release holds by bytes and SHA-256, each
                      proved by the Release's own record and a full anonymous download: forensics-plan.json
    forensics-remove  each planned file hashed again and removed: G-FORENSIC
    mark NAME         an instant and the units' states into state.json: pairoff, timer, retry, revert
    band NAME         exit 0 inside the band its block waits for, 3 outside it: pairoff or timer
    pairwait          until the pair book archive's run begun by B-PAIR-OFF ends: exit 0, 75 deferred, else 1
    pair              G-PAIR: that run, its tag, and the pair book and its archive's timer stopped and disabled
    timer             G-TIMER: the reward book archive's timer as installed and as systemd reads it
    first             that archive's first run on the new calendar: G-TRIGGER, G-RUN, G-TAG and G-NEXT;
                      exit 3 NOT YET
    reclaim TREE...   section 9: every file a committed report names by hash into the forensic store

No mode opens a stream, rewards or selection file of the reward book, or any file of the pair book's store: of
either store it reads the names and sizes of its directory entries, and of the reward book's also its slot records
and runtime.jsonl, which the reserve excepts. No mode prints a price, a size, a side, a book's hash, a rate, a
competitiveness or an outcome. No request carries a credential, and none goes to a host but GitHub's. No mode
changes a unit: the TZ's blocks do. Run it with /root/tz04a-env; it needs the standard library alone.

Written for CryptoTZ/TZ-46-capture-room.md. The TZ is the specification.
"""

import datetime
import hashlib
import http.client
import http.server
import json
import os
import re
import resource
import shutil
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request

if not __debug__:
    sys.stderr.write("tz46: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(2)

HERE = os.path.dirname(os.path.abspath(__file__))
PYFILE = "tz46-capture-room.py"

# ---- the TZ's constants: none of them is measured by this run -----------------------------------------------

MAP_REVISION = "2026-11-16-a"
ANCHORS = {"A1": "229a944f2d51", "A2": "6c5089330629",
           "A3": "0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable",
           "A4": "437b45ea196b", "A5": "0f6c90451cbd", "A6": "729f0bcdbee3"}
ANCHOR_FILES = {"A2": "research/twap-divergence.py", "A4": "BTC-EXECUTOR-INSTRUCTIONS.md",
                "A5": "research/recorder/recorder.py", "A6": "research/pfair.py"}
MAP_ROWS = {"frozen": 61, "tracked": 2, "reported": 1}
ROW = re.compile(r"^\| `([^`]+)` \| ([0-9,]+|—) \| ([0-9,]+|—) \| (frozen|tracked|reported) \| "
                 r"(?:`([0-9a-f]{64})`|[^|]*) \|$", re.M)
ANCHOR_ROW = re.compile(r"^\| `(A[0-9])` — [^|]*\| `([^`]+)` \|$", re.M)
NUMBER = "TZ-46-"
OWN_TZ = "CryptoTZ/TZ-46-capture-room.md"

PRIMARY = "/root/btc-5m-twap"
REPORTS = PRIMARY + "/CryptoReports"
WORK = "/root/tz46-work"
WT = WORK + "/wt"
TMP = WORK + "/selftest-tmp"
STATE = WORK + "/state.json"
PLAN = WORK + "/forensics-plan.json"
REMOVED = WORK + "/forensics-removed.jsonl"
FORENSICS = "/root/btc-forensics"
RB = "/var/lib/btc-rewardbook"
RB_ARCH = "/var/lib/btc-rewardbook-archive"
RB_ASVC = "/root/btc-rewardbook-archive-svc"
PB = "/var/lib/btc-pairbook"
PB_ARCH = "/var/lib/btc-pairbook-archive"
PB_ASVC = "/root/btc-pairbook-archive-svc"
RECORDER = "/var/lib/btc-recorder"
CHAINBOOK = "/var/lib/btc-chainbook"
DISK_PATH = "/var/lib"
UNIT_DIR = "/etc/systemd/system"
TIMER_REL = "deploy/systemd/btc-rewardbook-archive.timer"
TIMER_SHA256 = "7b0804285af6987340838bd59573897d013cf97edc5d4132cda7f3f9ba3e3824"       # Appendix A's timer
OLD_TIMER_SHA256 = "bf5af0252c420d8db1579b82e5da21472cdb6bc871fa8035ecf6f1edc9720a0f"   # TZ-34's, map section 0
TZ33_REL = "research/tz33-reward-book-capture.py"
TZ33_SHA256 = "a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670"
UNITS = {"recorder": "btc-recorder.service", "pairbook": "btc-pairbook.service",
         "rewardbook": "btc-rewardbook.service", "advisor": "adv3-bot.service"}
RB_SVC, RB_TIMER = "btc-rewardbook-archive.service", "btc-rewardbook-archive.timer"
PB_SVC, PB_TIMER = "btc-pairbook-archive.service", "btc-pairbook-archive.timer"
PB_ARGV = ("/root/tz04a-env/venv/bin/python", "-B", "-u", "/root/btc-pairbook-svc/tz26-nesting-b3-capture.py",
           "serve")
RUNNING = ("active", "activating", "deactivating", "reloading", "refreshing")
TERMINAL = ("complete", "empty", "halt", "deferred")

REPO = "seahomebatumi-ai/btc-5m-twap"
API_BASE, WEB_BASE = "https://api.github.com", "https://github.com"
UA = "btc-5m-twap-tz46"
API_VERSION = "2022-11-28"
API_TIMEOUT_S, DOWNLOAD_TIMEOUT_S, DOWNLOAD_ATTEMPTS = 60, 300, 3
API_MAX = 40                 # API requests a run of `forensics` makes at most: GitHub allows one address 60 an hour
RELEASES_PER_PAGE = 20       # a page of Releases carries every asset's record: twenty keep one page's parse small
HOSTS = ("api.github.com", "github.com", "127.0.0.1")
PLAN_MIN = {"tz-44-l0-inputs": 13}    # map section 7 item 167: the twelve archives and the manifest its Release holds

DAY, SLOT = 86400, 900
CALENDAR = "*-*-* 01/3:30:20 UTC"
CAL_FIRST_S, CAL_STEP_S = 5420, 10800    # 01:30:20 UTC, then every third hour: eight elapses a day
TIMER_BAND = (3920, 4820)                # B-TIMER: from 25 to 10 minutes before an elapse, as seconds of its step
TIMER_DAY = (36320, 69620)               # ... from 10:05:20 to 19:20:20 UTC
PAIR_DAY = (27000, 68400)                # B-PAIR-OFF: from 07:30:00 to 19:00:00 UTC
SLOT_JSON_AT, SETTLE_S, DECIDE_S = 910, 60, 6
NEXT_AFTER_S, NEXT_SETTLE_S = 900, 30
FIRST_LATE_S = 600           # G-TRIGGER: no run begun 600 s after the first elapse reads FAIL
PAIRWAIT_START_S, PAIRWAIT_MAX_S, PAIRWAIT_STEP_S = 120, 3600, 30
STREAM_FLOOR = 7300000000    # research/tz33-reward-book-capture.py line 190
HEAVIEST_SLOT = 31823974     # stored stream bytes of the heaviest slot of L0's eight days (TZ-45 section 0.4)
PEAK_SLOTS = 14              # the most slots of stream the store holds between two runs every three hours
PEAK = PEAK_SLOTS * HEAVIEST_SLOT
ROOM_MIN = 2000000000        # G-ROOM
DRIFTS = (43500000, 187760570)    # map section 6: bytes a day beside the streams, TZ-26's base and the fastest
DISK_FLOOR = 2300000000      # every mode's free-space floor: the reward book's halt floor and 100,000,000
RECLAIM_FLOOR = STREAM_FLOOR + 100000000    # reclaim's floor after each copy: the stream floor and one slot at the cut
MEM_FLOOR = 133073162        # MemAvailable at a mode's start: twice 66,536,581, the host peak modelled (section 0.4)
MEM_READS, MEM_WAIT_S = 5, 60

DIR_RE = re.compile(r"[0-9]{10}")
RB_STREAM_RE = re.compile(r"([0-9]{10})\.([0-9]+)\.stream\.jsonl\.gz")
RB_SLOT_RE = re.compile(r"([0-9]{10})\.([0-9]+)\.slot\.json")
SHA_RE = re.compile(r"[0-9a-f]{64}")
TOKEN = re.compile(r"[0-9a-f]{16,64}")
UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
STAMP_RE = re.compile(r"[A-Z][a-z]{2} ([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}) UTC")
SHOW_ENV = {"TZ": "UTC", "LC_ALL": "C", "SYSTEMD_COLORS": "0", "SYSTEMD_PAGER": ""}
LIVE_S = 60

# ---- the audit hook: TZ-46 section 2 as a pure function, and the hook that applies it -------------------------

MODE = [None]
ALLOWED_REMOVE = set()
REFUSED = []
COUNTS = {"requests": 0, "downloads": 0, "download_bytes": 0, "removed": 0, "reward book opens": 0}
WRITE_FLAGS = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC
CHANGE_EVENTS = ("os.remove", "os.rename", "os.rmdir", "os.mkdir", "os.truncate", "os.chmod", "os.chown",
                 "os.utime", "os.link", "os.symlink", "shutil.rmtree", "shutil.move", "shutil.copyfile")
HOOKED = ("open", "os.listdir", "os.scandir", "socket.getaddrinfo") + CHANGE_EVENTS


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


def policy(mode, event, args, allowed):
    """None where TZ-46 section 2 allows the event in this mode; otherwise why it is refused. Pure."""
    if event == "socket.getaddrinfo":
        host = args[0] if args else None
        if isinstance(host, bytes):
            host = host.decode("ascii", "replace")
        ok = host in HOSTS or (isinstance(host, str) and host.endswith(".githubusercontent.com"))
        return None if ok else "a connection to %r" % (host,)
    p = _path(args[0]) if args else None
    if p is None:
        return None
    if event == "open":
        wm, fl = (args[1] if len(args) > 1 else None), (args[2] if len(args) > 2 else None)
        w = _writing(wm, fl)
        if _under(p, RECORDER) or _under(p, CHAINBOOK) or _under(p, PB):
            return "an open under another capture's store"
        if _under(p, RB):
            if w:
                return "a write under the reward book's store"
            ok = RB_SLOT_RE.fullmatch(os.path.basename(p)) is not None or p == RB + "/runtime.jsonl"
            return None if ok else "an open of the reward book's %s" % os.path.basename(p)
        if _under(p, FORENSICS) and w:
            return None if mode == "reclaim" and _exclusive(wm, fl) else "a write into the forensic store"
        if w and not _under(p, WORK):
            return "a write outside the work tree"
        return None
    if event in ("os.listdir", "os.scandir"):
        return "a listing under another capture's root" if _under(p, RECORDER) or _under(p, CHAINBOOK) else None
    paths = [p]
    if event in ("os.rename", "os.link", "os.symlink", "shutil.move", "shutil.copyfile") and len(args) > 1:
        paths.append(_path(args[1]))
    for q in paths:
        if q is None:
            continue
        if event == "os.remove" and mode == "forensics-remove" and q in allowed and _under(q, FORENSICS):
            continue
        if not _under(q, WORK):
            return "a change outside the work tree"
    return None


def _audit(event, args):
    if event not in HOOKED:
        return
    why = policy(MODE[0], event, args, ALLOWED_REMOVE)
    if why is not None:
        REFUSED.append((event, str(args[0]) if args else ""))
        raise GuardError("%s refused in mode %s, %s: %r" % (event, MODE[0], why, args[0] if args else None))
    if event == "open" and args:
        p = _path(args[0])
        if p is not None and _under(p, RB):
            COUNTS["reward book opens"] += 1


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


def json_bytes(obj):
    return (json.dumps(obj, sort_keys=True, indent=1) + "\n").encode("utf-8")


def free_bytes():
    st = os.statvfs(DISK_PATH)
    return st.f_bavail * st.f_frsize


def mem_available():
    with open("/proc/meminfo", encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("MemAvailable:"):
                return int(line.split()[1]) * 1024
    raise AssertionError("no MemAvailable")


def floors(read=mem_available, sleep=time.sleep, freef=free_bytes):
    """At a mode's start: MemAvailable read up to five times 60 s apart, the first at or above MEM_FLOOR passing;
    free space at or above DISK_FLOOR."""
    for k in range(1, MEM_READS + 1):
        m = read()
        out("MemAvailable read %d: %d bytes, floor %d" % (k, m, MEM_FLOOR))
        if m >= MEM_FLOOR:
            break
        assert k < MEM_READS, "BLOCKED: MemAvailable below %d at %d reads" % (MEM_FLOOR, MEM_READS)
        sleep(MEM_WAIT_S)
    f = freef()
    out("free %d bytes, floor %d" % (f, DISK_FLOOR))
    assert f >= DISK_FLOOR, "BLOCKED: free %d bytes, below %d" % (f, DISK_FLOOR)
    return f


def load_state(path=STATE):
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def save_state(st, path=STATE):
    with open(path + ".new", "w", encoding="utf-8") as fh:
        json.dump(st, fh, sort_keys=True, indent=1)
        fh.write("\n")
    os.replace(path + ".new", path)


def show(unit, props):
    """systemctl show under TZ=UTC and the C locale: {property: value}, a repeated property's values joined."""
    args = ["systemctl", "show", unit]
    for p in props:
        args += ["-p", p]
    cp = subprocess.run(args, capture_output=True, text=True, env=dict(os.environ, **SHOW_ENV))
    assert cp.returncode == 0, "systemctl show %s: %s" % (unit, cp.stderr.strip())
    kv = {}
    for line in cp.stdout.split("\n"):
        if "=" in line:
            k, v = line.split("=", 1)
            kv[k] = v if k not in kv else kv[k] + "\n" + v
    return kv


def stamp_of(text):
    """An epoch from systemctl's own stamp printed under TZ=UTC; None where it prints none."""
    m = STAMP_RE.fullmatch((text or "").strip())
    if m is None:
        return None
    dt = datetime.datetime.strptime(m.group(1), "%Y-%m-%d %H:%M:%S").replace(tzinfo=datetime.timezone.utc)
    return int(dt.timestamp())


def git(*args, tree=PRIMARY):
    cp = subprocess.run(["git", "-C", tree] + list(args), capture_output=True, text=True)
    assert cp.returncode == 0, "git %s: %s" % (" ".join(args), cp.stderr.strip()[:300])
    return cp.stdout.strip()


def ledger(path):
    """A ledger's complete lines, parsed, and the bytes of a line still being written."""
    with open(path, "rb") as fh:
        raw = fh.read()
    parts = raw.split(b"\n")
    return [json.loads(ln) for ln in parts[:-1] if ln.strip()], parts[-1]


def processes_with(argv):
    """Every process whose command line is argv exactly, field for field."""
    found = []
    for pid in sorted((p for p in os.listdir("/proc") if p.isdigit()), key=int):
        try:
            with open("/proc/%s/cmdline" % pid, "rb") as fh:
                fields = fh.read().split(b"\0")
        except OSError:
            continue
        if fields and fields[-1] == b"":
            fields = fields[:-1]
        try:
            if [f.decode("utf-8") for f in fields] == list(argv):
                found.append(int(pid))
        except UnicodeDecodeError:
            continue
    return found


def ls_remote_tag(tag):
    """The object a tag names on origin, and its peeled commit where it is annotated."""
    lines = git("ls-remote", "origin", "refs/tags/%s" % tag, "refs/tags/%s^{}" % tag).split("\n")
    rows = dict(reversed(ln.split("\t")) for ln in lines if "\t" in ln)
    return rows.get("refs/tags/%s" % tag), rows.get("refs/tags/%s^{}" % tag)

# ---- the clock: the new calendar and the blocks' bands --------------------------------------------------------


def next_calendar(now):
    """The first elapse of `*-*-* 01/3:30:20 UTC` strictly after now: 01:30:20 UTC and every 10,800 s after it."""
    d0 = int(now) // DAY * DAY
    for k in range(8):
        t = d0 + CAL_FIRST_S + k * CAL_STEP_S
        if t > now:
            return t
    return d0 + DAY + CAL_FIRST_S


def is_calendar(t):
    return int(t) == t and (int(t) % DAY - CAL_FIRST_S) % CAL_STEP_S == 0 and int(t) % DAY >= CAL_FIRST_S


def band_reading(name, now, rb_state, pb_state):
    """(True, why) where the band B-PAIR-OFF or B-TIMER waits for holds at `now`, given both archives' services'
    ActiveState; else (False, why). Pure."""
    s = int(now) % DAY
    if rb_state in RUNNING or pb_state in RUNNING:
        return False, "an archive runs: the reward book's %s, the pair book's %s" % (rb_state, pb_state)
    if name == "pairoff":
        ok = PAIR_DAY[0] <= s <= PAIR_DAY[1]
        return ok, "second %d of the day, the band %d to %d" % (s, PAIR_DAY[0], PAIR_DAY[1])
    assert name == "timer", "band %r" % name
    r = s % CAL_STEP_S
    ok = TIMER_DAY[0] <= s <= TIMER_DAY[1] and TIMER_BAND[0] <= r <= TIMER_BAND[1]
    return ok, "second %d of the day, %d of its step; the next elapse %s" % (s, r, utc(next_calendar(now)))

# ---- the stores, by their directory entries alone -------------------------------------------------------------


def is_stream(kind, name):
    """A stream file by the store's own names: the reward book's <S>.<k>.stream.jsonl.gz, as its stream_bytes_total
    counts them (research/tz33-reward-book-capture.py lines 1279 to 1291), or the pair book's stream*.jsonl.gz, as
    its own does (research/tz26-nesting-b3-capture.py lines 794 to 806)."""
    if kind == "rb":
        return name.endswith(".stream.jsonl.gz") and RB_STREAM_RE.fullmatch(name) is not None
    assert kind == "pb", "kind %r" % kind
    return name.startswith("stream") and name.endswith(".jsonl.gz")


def store_view(root, kind):
    """A capture's store by directory entries alone: its stream files and every other file, counts and bytes, and
    the stream bytes of each numbered directory. Nothing is opened."""
    v = {"streams_n": 0, "streams_bytes": 0, "other_n": 0, "other_bytes": 0, "dirs": 0, "by_dir": {}}
    if not os.path.isdir(root):
        return v
    with os.scandir(root) as it:
        entries = sorted(it, key=lambda e: e.name)
    for e in entries:
        if e.is_dir(follow_symlinks=False) and DIR_RE.fullmatch(e.name):
            v["dirs"] += 1
            with os.scandir(e.path) as it2:
                files = sorted(it2, key=lambda x: x.name)
            for f in files:
                if not f.is_file(follow_symlinks=False):
                    continue
                size = f.stat(follow_symlinks=False).st_size
                if is_stream(kind, f.name):
                    v["streams_n"] += 1
                    v["streams_bytes"] += size
                    v["by_dir"][int(e.name)] = v["by_dir"].get(int(e.name), 0) + size
                else:
                    v["other_n"] += 1
                    v["other_bytes"] += size
        elif e.is_file(follow_symlinks=False):
            v["other_n"] += 1
            v["other_bytes"] += e.stat(follow_symlinks=False).st_size
    return v


def forensic_files(root, hashed=True):
    """Every regular file under root but links and empty files, in path order: {path, bytes, sha256}."""
    found = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames.sort()
        for name in sorted(filenames):
            p = os.path.join(dirpath, name)
            if os.path.islink(p) or not os.path.isfile(p) or os.path.getsize(p) == 0:
                continue
            if hashed:
                h, n = sha256_file(p)
                found.append({"path": p, "bytes": n, "sha256": h})
            else:
                found.append({"path": p, "bytes": os.path.getsize(p), "sha256": None})
    return found


def tree_count(root):
    n = b = 0
    for dirpath, _dirnames, filenames in os.walk(root):
        for name in filenames:
            p = os.path.join(dirpath, name)
            if not os.path.islink(p) and os.path.isfile(p):
                n += 1
                b += os.path.getsize(p)
    return n, b

# ---- GitHub, anonymous: every header fixed --------------------------------------------------------------------


def build_request(url, accept="application/vnd.github+json"):
    """The one builder of every request: Accept, this file's User-Agent and the API version; never a credential."""
    return urllib.request.Request(url, method="GET", headers={"Accept": accept, "User-Agent": UA,
                                                               "X-GitHub-Api-Version": API_VERSION})


def get_json(url):
    """One API request, no retry: (status, document)."""
    COUNTS["requests"] += 1
    assert COUNTS["requests"] <= API_MAX, "BLOCKED: more than %d API requests" % API_MAX
    try:
        with urllib.request.urlopen(build_request(url), timeout=API_TIMEOUT_S) as resp:
            raw = resp.read()
            return int(resp.status), json.loads(raw) if raw else None
    except urllib.error.HTTPError as exc:
        return int(exc.code), None


def download(url):
    """A download streamed into SHA-256 and a byte count, nothing stored: (status, bytes, sha256)."""
    COUNTS["downloads"] += 1
    h, n = hashlib.sha256(), 0
    with urllib.request.urlopen(build_request(url, "application/octet-stream"), timeout=DOWNLOAD_TIMEOUT_S) as resp:
        status = int(resp.status)
        for b in iter(lambda: resp.read(1 << 20), b""):
            h.update(b)
            n += len(b)
    COUNTS["download_bytes"] += n
    return status, n, h.hexdigest()


def download_checked(url, attempts=DOWNLOAD_ATTEMPTS, backoff_s=10):
    """A download with up to `attempts` tries where the transfer breaks; a whole reply is never retried."""
    for k in range(1, attempts + 1):
        try:
            return download(url)
        except urllib.error.HTTPError as exc:
            return int(exc.code), 0, None
        except (urllib.error.URLError, OSError, http.client.HTTPException) as exc:
            out("download %s broke: %s, attempt %d of %d" % (url.rsplit("/", 1)[-1], type(exc).__name__, k, attempts))
            if k == attempts:
                return None, 0, None
        time.sleep(backoff_s * k)
    return None, 0, None


ASSET_KEYS = ("id", "name", "size", "state", "digest", "browser_download_url")


def slim_asset(a):
    return {k: a.get(k) for k in ASSET_KEYS}


def slim_release(rel):
    """A Release's record cut to what the plan reads: its id, tag, draft flag and its assets' own records."""
    return {"id": rel.get("id"), "tag_name": rel.get("tag_name"), "draft": rel.get("draft"),
            "assets": [slim_asset(a) for a in rel.get("assets") or []]}


def paged(url, per, keep):
    """Every item of a list endpoint, `per` a page until a shorter page, each cut by `keep` as its page arrives."""
    found, page = [], 1
    while True:
        status, doc = get_json("%s%sper_page=%d&page=%d" % (url, "&" if "?" in url else "?", per, page))
        assert status == 200 and isinstance(doc, list), "BLOCKED: %s page %d: status %r" % (url, page, status)
        found.extend(keep(x) for x in doc)
        if len(doc) < per:
            return found
        page += 1


def download_url(web, tag, name):
    return "%s/%s/releases/download/%s/%s" % (web, REPO, urllib.parse.quote(tag), urllib.parse.quote(name))

# ---- the forensic store against the Releases: pure --------------------------------------------------------------


def index_assets(rels):
    """(bytes, sha256) -> [(tag, release id, asset)] over every uploaded asset of a published Release whose record
    carries a SHA-256 digest, each list in order of tag and name. Pure."""
    idx = {}
    for rel in rels:
        if rel.get("draft") is not False or not isinstance(rel.get("tag_name"), str):
            continue
        for a in rel.get("assets") or []:
            d = a.get("digest") or ""
            if a.get("state") == "uploaded" and isinstance(a.get("size"), int) and d.startswith("sha256:") \
                    and SHA_RE.fullmatch(d[7:]):
                idx.setdefault((a["size"], d[7:]), []).append((rel["tag_name"], rel.get("id"), a))
    for v in idx.values():
        v.sort(key=lambda x: (x[0], str(x[2].get("name"))))
    return idx


def plan_rows(files, idx):
    """The forensic files some Release holds by bytes and SHA-256, each with its first candidate, and the count of
    those none holds. Pure."""
    held = [(f, idx[(f["bytes"], f["sha256"])][0]) for f in files if (f["bytes"], f["sha256"]) in idx]
    return held, len(files) - len(held)


def asset_ok(a, size, sha, url):
    """The Release's own record of one asset against a file: uploaded, its bytes, its digest, its URL. Pure."""
    return (isinstance(a, dict) and a.get("state") == "uploaded" and a.get("size") == size
            and a.get("digest") == "sha256:" + sha and a.get("browser_download_url") == url)

# ---- the readings: pure --------------------------------------------------------------------------------------


def room_reading(free, rb_streams):
    """G-ROOM, pure: the free space with the reward book's stream files gone - the bytes its archive gives back -
    less its stream floor and the most its store holds between two runs, against ROOM_MIN. (room, margin, PASS)."""
    room = free + rb_streams
    margin = room - STREAM_FLOOR - PEAK
    return room, margin, margin >= ROOM_MIN


def timer_checks(kv, now, installed_sha, pb):
    """G-TIMER, pure: the timer as systemd reads it under TZ=UTC, the installed file's SHA-256, and the pair book
    archive's timer."""
    cal, mono = kv.get("TimersCalendar") or "", kv.get("TimersMonotonic") or ""
    return {"loaded": kv.get("LoadState") == "loaded",
            "active, waiting or running": kv.get("ActiveState") == "active" and kv.get("SubState") in ("waiting",
                                                                                                   "running"),
            "enabled": kv.get("UnitFileState") == "enabled",
            "its fragment": kv.get("FragmentPath") == UNIT_DIR + "/" + RB_TIMER,
            "its unit": kv.get("Unit") == RB_SVC,
            "one calendar, every third hour from 01:30:20 UTC": cal.count("OnCalendar=") == 1
            and ("OnCalendar=%s ;" % CALENDAR) in cal,
            "no run on a start of the timer": "USec=" not in mono,
            "accuracy 1 s": kv.get("AccuracyUSec") == "1s",
            "the next elapse the calendar's": stamp_of(kv.get("NextElapseUSecRealtime")) == next_calendar(now),
            "installed byte for byte": installed_sha == TIMER_SHA256,
            "the pair book archive's timer stopped and disabled": pb.get("ActiveState") == "inactive"
            and pb.get("UnitFileState") == "disabled"}


def first_start(recs, since_ns):
    """The first start record at or after since_ns - a run begun then, or a pending set resumed then - its run, and
    that run's records from that start on: (run, start, records). Pure."""
    for i, r in enumerate(recs):
        if r.get("event") == "start" and r.get("wall_ns", 0) >= since_ns:
            return r.get("run"), r, [x for x in recs[i:] if x.get("run") == r.get("run")]
    return None, None, []


def run_state(mine):
    """A run's state from its records: 'running' where no terminal record follows its last start, else that
    record's event. Pure."""
    last = max(i for i, r in enumerate(mine) if r.get("event") == "start")
    terms = [r.get("event") for r in mine[last + 1:] if r.get("event") in TERMINAL]
    return terms[-1] if terms else "running"


def trigger_reading(trg, elapse, s0, last_trigger):
    """G-TRIGGER, pure: the trigger systemd handed the run, its first start record's - TRIGGER_UNIT this timer, its
    realtime from the elapse to 60 s after it, the record within 60 s after it - else the timer's LastTriggerUSec
    read the same way. (PASS, the evidence read, the trigger's second)."""
    if trg and trg.get("unit") is not None:
        t = int(trg.get("realtime_usec") or 0) // 10 ** 6
        return (trg["unit"] == RB_TIMER and elapse <= t <= elapse + 60 and t - 1 <= s0 <= t + 60), \
            "TRIGGER_UNIT %s" % trg["unit"], t
    t = last_trigger
    return (t is not None and elapse <= t <= elapse + 60 and t - 1 <= s0 <= t + 60), "LastTriggerUSec", t


def next_slots(first_ns, last_ns):
    """The slots whose decision instant S - 6 lies from a run's first removal to 900 s after its last."""
    s = -(-(first_ns + DECIDE_S * 10 ** 9) // (SLOT * 10 ** 9)) * SLOT
    found = []
    while (s - DECIDE_S) * 10 ** 9 < last_ns + NEXT_AFTER_S * 10 ** 9:
        found.append(s)
        s += SLOT
    return found


def next_verdict(sjs, errors, pid0):
    """One slot across the removals, from its slot.json files [(k, doc)] and its task's error records: FAIL where an
    error record or no slot.json; PASS where the process the run began beside streamed it with no reason to keep it
    off; UNDECIDABLE otherwise. Pure."""
    if errors:
        return "FAIL", "an error record of its task: %s" % str(errors[0].get("error"))[:160]
    if not sjs:
        return "FAIL", "no slot.json"
    why = []
    for k, sj in sjs:
        st = sj.get("stream") if isinstance(sj.get("stream"), dict) else {}
        if (str(sj.get("pid")) == str(pid0) and st.get("opened") is True and st.get("off_reason") is None
                and sj.get("error") is None and sj.get("stopped") is False):
            return "PASS", "index %d streamed by %s" % (k, pid0)
        why.append("index %d: pid %s, opened %s, off %s, stopped %s, error %s" % (
            k, sj.get("pid"), st.get("opened"), st.get("off_reason"), sj.get("stopped"), sj.get("error")))
    return "UNDECIDABLE", "; ".join(why)


def next_reading(verdicts):
    vs = [v for v, _w in verdicts]
    return "FAIL" if "FAIL" in vs else ("UNDECIDABLE" if "UNDECIDABLE" in vs or not vs else "PASS")


def pair_reading(mine, tag_obj, commit, pb, tmr, svc, procs):
    """G-PAIR, pure: the pair book archive's run begun by B-PAIR-OFF complete - its set moved, the pair book
    restarted and resumed, every request inside the idle stretch - and its tag at the archive's commit; then the
    pair book stopped and disabled, no process of it left, and its archive's timer stopped and disabled."""
    ev = [r.get("event") for r in mine]
    comp = [r for r in mine if r.get("event") == "complete"]
    res = [r for r in mine if r.get("event") == "resume"]
    return {"the run complete": bool(mine) and run_state(mine) == "complete",
            "the pair book restarted and resumed by it": "restart" in ev and bool(res)
            and res[-1].get("reading") != "FAIL",
            "every request inside the idle stretch": bool(comp) and comp[-1].get("started_outside") == 0
            and comp[-1].get("ended_outside") == 0,
            "its tag at the archive's commit": tag_obj is not None and tag_obj == commit,
            "the pair book stopped and disabled": pb.get("ActiveState") in ("inactive", "failed")
            and pb.get("MainPID") == "0" and pb.get("UnitFileState") == "disabled",
            "no process of the pair book": not procs,
            "its archive's timer stopped and disabled": tmr.get("ActiveState") == "inactive"
            and tmr.get("UnitFileState") == "disabled",
            "its archive's service idle": svc.get("ActiveState") not in RUNNING}


def still_reading(before, now, restarts, stopped_ok):
    """G-STILL, pure: every unit but the pair book unchanged; the pair book unchanged, or moved by its archive's own
    restart records alone - a chain from the recorded MainPID, NRestarts one higher at each - and active, or, where
    stopped_ok, after that chain stopped: MainPID 0 and not active."""
    for k in sorted(now):
        if k != "pairbook" and now[k] != before.get(k):
            return False, "the %s changed" % k
    b, n = before["pairbook"], now["pairbook"]
    pid, count = b["MainPID"], int(b["NRestarts"])
    for r in restarts:
        if str(r.get("stopped")) != pid or str(r.get("NRestarts")) != str(count + 1):
            return False, "a restart record that does not follow %s at NRestarts %d: %r" % (pid, count, r)
        pid, count = str(r.get("pid")), count + 1
    if n == b and not restarts:
        return True, "unchanged"
    if stopped_ok and n["MainPID"] == "0" and n["ActiveState"] in ("inactive", "failed"):
        return True, "the pair book stopped by B-PAIR-OFF after %d restart records of its archive" % len(restarts)
    if restarts and pid == n["MainPID"] and str(count) == n["NRestarts"] and n["ActiveState"] == "active":
        return True, "the pair book moved by its archive's own restarts alone: %d" % len(restarts)
    return False, "the pair book changed, %d restart records of its archive since the first read" % len(restarts)


def number_reading(names, own):
    """NUMBER, CANON hard rule 2: CryptoTZ/ holds this TZ's file and no other of its number; CryptoReports/ no report
    of it. Pure."""
    tz = [n for n in names if n.startswith("CryptoTZ/" + NUMBER)]
    rp = [n for n in names if n.startswith("CryptoReports/" + NUMBER)]
    return tz == [own] and not rp, tz, rp

# ---- the modes ------------------------------------------------------------------------------------------------


def mode_fingerprint():
    with open(os.path.join(PRIMARY, "SYSTEM-MAP.md"), "rb") as fh:
        raw = fh.read()
    txt = raw.decode("utf-8")
    rev = re.findall(r"^\*\*Revision string:\*\* `([^`]+)`$", txt, re.M)
    assert rev == [MAP_REVISION], "map revision %r, required %s" % (rev, MAP_REVISION)
    found = dict(ANCHOR_ROW.findall(txt))
    assert found == ANCHORS, "anchors %r" % found
    for k, rel in sorted(ANCHOR_FILES.items()):
        h = sha256_file(os.path.join(PRIMARY, rel))[0][:12]
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
        out("%-48s %6d lines %8d bytes %s %s%s" % (path, got[0], got[1], got[2], state,
                                                  " equal" if state == "frozen" else ""))
    out("SYSTEM-MAP.md %d lines %d bytes sha256 %s" % (raw.count(b"\n"), len(raw), sha256_bytes(raw)))
    out("FINGERPRINT PASS: revision %s; anchors 6 of 6, 4 re-derived; rows %d: frozen %d of %d equal, tracked %d, "
        "reported %d" % (MAP_REVISION, len(rows), states["frozen"], MAP_ROWS["frozen"], states["tracked"],
                         states["reported"]))


def mode_number():
    names = git("ls-tree", "--name-only", "origin/main", "--", "CryptoTZ/", "CryptoReports/").split("\n")
    head = git("rev-parse", "origin/main")
    ok, tz, rp = number_reading(names, OWN_TZ)
    out("origin/main %s: %d paths under CryptoTZ/ and CryptoReports/; of the number %s: %s and %s" % (
        head, len(names), NUMBER, tz, rp))
    out("NUMBER %s" % ("PASS - 2 of 2" if ok else "FAIL"))
    assert ok, "BLOCKED: of the number %s, CryptoTZ/ holds %s and CryptoReports/ %s" % (NUMBER, tz, rp)


def units_now():
    now = {}
    for key, unit in sorted(UNITS.items()):
        kv = show(unit, ["MainPID", "NRestarts", "ActiveState", "UnitFileState", "MemoryCurrent", "MemoryPeak"])
        now[key] = {k: kv.get(k) for k in ("MainPID", "NRestarts", "ActiveState")}
        out("%s %s, UnitFileState %s, MemoryCurrent %s, MemoryPeak %s" % (
            unit, now[key], kv.get("UnitFileState"), kv.get("MemoryCurrent"), kv.get("MemoryPeak")))
    return now


def archives_now():
    found = {}
    for unit in (RB_TIMER, RB_SVC, PB_TIMER, PB_SVC):
        found[unit] = show(unit, ["ActiveState", "SubState", "UnitFileState", "Result", "NextElapseUSecRealtime",
                                  "LastTriggerUSec"])
        out("%s %s" % (unit, found[unit]))
    return found


def mode_still():
    st = load_state()
    now = units_now()
    archives_now()
    if "still" not in st:
        st["still"] = {"at": utc(time.time()), "at_ns": time.time_ns(), "units": now}
        save_state(st)
        out("still: recorded")
        return 0
    since = st["still"]["at_ns"]
    recs, _tail = ledger(PB_ARCH + "/ledger.jsonl")
    restarts = [r for r in recs if r.get("event") == "restart" and r.get("wall_ns", 0) >= since]
    for r in restarts:
        out("the pair book archive's restart record %s: run %s, pid %s after %s, NRestarts %s" % (
            utc(r["wall_ns"] / 1e9), r.get("run"), r.get("pid"), r.get("stopped"), r.get("NRestarts")))
    rrecs, _tail = ledger(RB_ARCH + "/ledger.jsonl")
    runs = sorted({r.get("run") for r in rrecs if r.get("wall_ns", 0) >= since and isinstance(r.get("run"), int)})
    out("the reward book archive's runs with records since the first read: %s" % runs)
    ok, why = still_reading(st["still"]["units"], now, restarts, "pairoff" in st.get("marks", {}))
    out("G-STILL %s: %s since %s" % ("PASS" if ok else "FAIL", why, st["still"]["at"]))
    return 0 if ok else 4


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
    cp = subprocess.run(["stat", "-c", "%W", path], capture_output=True, text=True)
    assert cp.returncode == 0, cp.stderr
    return int(cp.stdout.strip())


def mode_scratch(own):
    """Lists the UUID directories beside `own`, this session's, and names each live or earlier."""
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


def runs_line(recs, n=10):
    """The last n runs of an archive, from its ledger: terminal, set, free space and rate."""
    by = {}
    for r in recs:
        if isinstance(r.get("run"), int):
            by.setdefault(r["run"], []).append(r)
    lines = []
    for a in sorted(by)[-n:]:
        mine = by[a]
        c = ([r for r in mine if r.get("event") == "complete"] or [{}])[-1]
        d = ([r for r in mine if r.get("event") == "delete"] or [{}])[-1]
        st = run_state(mine) if any(r.get("event") == "start" for r in mine) else "no start"
        lines.append("run %d %s %s: %s files %s bytes; free before removal %s, after %s; store's streams at its end "
                     "%s; rate a day %s" % (a, utc(a), st, c.get("assets_n"), c.get("bytes_total"),
                                            d.get("free_before"), d.get("free_after"), c.get("store_stream_bytes"),
                                            c.get("rate_per_day")))
    return lines


def mode_room(label):
    assert label in ("before", "after"), "room %r" % label
    floors()
    free = free_bytes()
    rb, pb = store_view(RB, "rb"), store_view(PB, "pb")
    fz = tree_count(FORENSICS)
    out("free %d bytes on %s at %s" % (free, DISK_PATH, utc(time.time())))
    for name, v in (("the reward book's store", rb), ("the pair book's store", pb)):
        out("%s: %d directories; %d stream files, %d bytes; %d other files, %d bytes" % (
            name, v["dirs"], v["streams_n"], v["streams_bytes"], v["other_n"], v["other_bytes"]))
    for t in sorted(pb["by_dir"]):
        if label == "after":
            out("the pair book's window %d %s: %d bytes of stream" % (t, utc(t), pb["by_dir"][t]))
    out("the forensic store: %d files, %d bytes" % fz)
    for name, path in (("reward", RB_ARCH), ("pair", PB_ARCH)):
        recs, tail = ledger(path + "/ledger.jsonl")
        out("the %s book archive's ledger: %d records, %d bytes of a line still written" % (name, len(recs),
                                                                                           len(tail)))
        for line in runs_line(recs):
            out("  %s" % line)
    room, margin, ok = room_reading(free, rb["streams_bytes"])
    out("room: free %d + the reward book's stream files %d = %d; less its stream floor %d and the most its store "
        "holds between two runs, %d = %d slots of %d, the margin %d; with the pair book's %d stream files %d" % (
            free, rb["streams_bytes"], room, STREAM_FLOOR, PEAK, PEAK_SLOTS, HEAVIEST_SLOT, margin, pb["streams_n"],
            room + pb["streams_bytes"]))
    for d in DRIFTS:
        days = margin / d if margin > 0 else 0.0
        out("at %d bytes a day beside the streams the margin lasts %.1f days, to %s [modelled]" % (
            d, days, utc(time.time() + days * DAY)))
    doc = {"label": label, "at": utc(time.time()), "free": free, "reward": rb, "pair": pb,
           "forensics": {"files": fz[0], "bytes": fz[1]}, "room": room, "margin": margin}
    with open(os.path.join(WORK, "room-%s.json" % label), "wb") as fh:
        fh.write(json_bytes(doc))
    if label == "after":
        out("G-ROOM %s: the margin %d bytes, at least %d asked" % ("PASS" if ok else "FAIL", margin, ROOM_MIN))
        return 0 if ok else 4
    return 0


def mode_forensics(root=FORENSICS, api=API_BASE, web=WEB_BASE, plan_path=PLAN, state_path=STATE, least=None):
    floors()
    t0 = time.time()
    files = forensic_files(root)
    out("the forensic store %s: %d files, %d bytes, hashed in %.1f s" % (root, len(files),
                                                                       sum(f["bytes"] for f in files),
                                                                       time.time() - t0))
    rels = paged("%s/repos/%s/releases" % (api, REPO), RELEASES_PER_PAGE, slim_release)
    idx = index_assets(rels)
    out("the repository's Releases read anonymously: %d, %d assets with a digest" % (
        len(rels), sum(len(v) for v in idx.values())))
    held, kept = plan_rows(files, idx)
    out("files a Release holds by bytes and SHA-256: %d; held by none: %d" % (len(held), kept))
    exact, proven, rows = {}, {}, []
    for f, (tag, rid, a) in held:
        if rid not in exact:
            exact[rid] = {x.get("id"): x for x in paged("%s/repos/%s/releases/%d/assets" % (api, REPO, rid), 100,
                                                        slim_asset)}
        url = download_url(web, tag, a.get("name"))
        api_ok = asset_ok(exact[rid].get(a.get("id")), f["bytes"], f["sha256"], url)
        if api_ok and a.get("id") not in proven:
            proven[a.get("id")] = download_checked(url)
        status, n, h = proven.get(a.get("id"), (None, 0, None))
        dl_ok = api_ok and status == 200 and n == f["bytes"] and h == f["sha256"]
        row = {"path": f["path"], "bytes": f["bytes"], "sha256": f["sha256"], "tag": tag, "release_id": rid,
               "asset": a.get("name"), "asset_id": a.get("id"), "url": url, "api_ok": api_ok,
               "download_status": status, "download_bytes": n, "download_sha256": h, "download_ok": dl_ok}
        rows.append(row)
        out("P %s %d %s: %s of %s, asset %s, api %s, download %s %s" % (
            f["path"], f["bytes"], f["sha256"], a.get("name"), tag, a.get("id"), api_ok, status,
            "equal" if dl_ok else "NOT EQUAL"))
    planned = [r for r in rows if r["api_ok"] and r["download_ok"]]
    least = PLAN_MIN if least is None else least
    for tag, n in sorted(least.items()):
        got = sum(1 for r in planned if r["tag"] == tag)
        out("files proved against %s: %d, at least %d expected" % (tag, got, n))
        assert got >= n, "BLOCKED: %d files proved against %s, at least %d expected; no plan written" % (got, tag, n)
    doc = {"root": root, "files_n": len(files), "files_bytes": sum(f["bytes"] for f in files),
           "releases_n": len(rels), "rows": rows, "planned_n": len(planned),
           "planned_bytes": sum(r["bytes"] for r in planned), "requests": COUNTS["requests"],
           "downloads": COUNTS["downloads"], "download_bytes": COUNTS["download_bytes"]}
    raw = json_bytes(doc)
    with open(plan_path, "wb") as fh:
        fh.write(raw)
    st = load_state(state_path)
    st["forensics"] = {"at": utc(time.time()), "plan_sha256": sha256_bytes(raw), "planned_n": len(planned)}
    save_state(st, state_path)
    out("FORENSICS PLAN: %d files, %d bytes, each held by a public Release and proved; %d rows, %d not proved; "
        "%d API requests, %d downloads, %d bytes; forensics-plan.json sha256 %s" % (
            len(planned), doc["planned_bytes"], len(rows), len(rows) - len(planned), COUNTS["requests"],
            COUNTS["downloads"], COUNTS["download_bytes"], sha256_bytes(raw)))
    return 0


def mode_forensics_remove(root=FORENSICS, plan_path=PLAN, removed_path=REMOVED, state_path=STATE):
    floors()
    st = load_state(state_path)
    with open(plan_path, "rb") as fh:
        raw = fh.read()
    assert sha256_bytes(raw) == st.get("forensics", {}).get("plan_sha256"), "forensics-plan.json is not the plan"
    doc = json.loads(raw)
    planned = [r for r in doc["rows"] if r["api_ok"] and r["download_ok"]]
    assert len(planned) == doc["planned_n"] and all(_under(r["path"], root) for r in planned), "the plan's rows"
    done = set()
    if os.path.exists(removed_path):
        with open(removed_path, encoding="utf-8") as fh:
            done = {json.loads(ln)["path"] for ln in fh if ln.strip()}
    for r in planned:
        if r["path"] in done:
            assert not os.path.lexists(r["path"]), "%s recorded removed and present" % r["path"]
            continue
        assert sha256_file(r["path"]) == (r["sha256"], r["bytes"]), \
            "BLOCKED: %s is not the file the plan proved; nothing removed by this run" % r["path"]
    free0, freed = free_bytes(), 0
    for r in planned:
        p = r["path"]
        if p in done:
            continue
        assert sha256_file(p) == (r["sha256"], r["bytes"]), "%s changed" % p
        ALLOWED_REMOVE.add(p)
        try:
            os.remove(p)
        finally:
            ALLOWED_REMOVE.discard(p)
        COUNTS["removed"] += 1
        assert not os.path.lexists(p), "%s is still there" % p
        freed += r["bytes"]
        row = {"path": p, "bytes": r["bytes"], "sha256": r["sha256"], "tag": r["tag"], "release_id": r["release_id"],
               "asset": r["asset"], "asset_id": r["asset_id"], "download_sha256": r["download_sha256"],
               "removed_ns": time.time_ns()}
        with open(removed_path, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(row, sort_keys=True) + "\n")
        out("X %s %d %s removed: %s of %s" % (p, r["bytes"], r["sha256"], r["asset"], r["tag"]))
    with open(removed_path, "a", encoding="utf-8"):
        pass
    with open(removed_path, encoding="utf-8") as fh:
        recorded = [json.loads(ln) for ln in fh if ln.strip()]
    left = forensic_files(root, hashed=False)
    checks = {"every planned file absent": all(not os.path.lexists(r["path"]) for r in planned),
              "every removal recorded once": sorted(x["path"] for x in recorded) == sorted(r["path"]
                                                                                        for r in planned),
              "the store less exactly the planned files": len(left) == doc["files_n"] - len(planned)}
    for k, v in checks.items():
        out("G-FORENSIC %-44s %s" % (k, v))
    assert all(checks.values()), "G-FORENSIC FAIL: %r" % sorted(k for k, v in checks.items() if not v)
    out("G-FORENSIC PASS: %d of %d removed, %d bytes; this run %d files, %d bytes; free %d before, %d after" % (
        len(recorded), len(planned), sum(x["bytes"] for x in recorded), COUNTS["removed"], freed, free0,
        free_bytes()))
    return 0


def mode_mark(name):
    assert name in ("pairoff", "timer", "retry", "revert"), "mark %r" % name
    st = load_state()
    marks = st.setdefault("marks", {})
    assert name not in marks, "mark %s already taken" % name
    marks[name] = {"ns": time.time_ns(), "units": units_now(), "archives": archives_now()}
    save_state(st)
    out("mark %s at %s" % (name, utc(marks[name]["ns"] / 1e9)))
    return 0


def mode_band(name):
    now = time.time()
    rb, pb = show(RB_SVC, ["ActiveState"]).get("ActiveState"), show(PB_SVC, ["ActiveState"]).get("ActiveState")
    ok, why = band_reading(name, now, rb, pb)
    out("band %s %s: %s" % (name, "OPEN" if ok else "closed", why))
    return 0 if ok else 3


def mode_pairwait():
    """Until the pair book archive's run begun after this mode's start - or resumed - reaches a terminal record and
    its service is idle: exit 0 complete or empty, 75 deferred, 1 halted, not begun within 120 s or still running
    after 3,600 s."""
    st = load_state()
    assert "pairoff" in st.get("marks", {}), "pairwait: no pairoff mark"
    t0 = time.time_ns()
    deadline = time.time() + PAIRWAIT_MAX_S
    while True:
        recs, _tail = ledger(PB_ARCH + "/ledger.jsonl")
        starts = [r for r in recs if r.get("event") == "start" and r.get("wall_ns", 0) >= t0 - 5 * 10 ** 9]
        svc = show(PB_SVC, ["ActiveState", "Result", "ExecMainStatus"])
        if starts:
            a = starts[-1]["run"]
            mine = [r for r in recs if r.get("run") == a]
            state = run_state(mine)
            if svc.get("ActiveState") not in RUNNING:
                for r in mine:
                    out("R %s" % json.dumps(r, sort_keys=True))
                out("PAIRWAIT run %d: %s; the service %s, Result %s, ExecMainStatus %s" % (
                    a, "INTERRUPTED" if state == "running" else state, svc.get("ActiveState"), svc.get("Result"),
                    svc.get("ExecMainStatus")))
                return {"complete": 0, "empty": 0, "deferred": 75}.get(state, 1)
        elif time.time_ns() > t0 + PAIRWAIT_START_S * 10 ** 9:
            out("PAIRWAIT: no run begun within %d s; the service %s" % (PAIRWAIT_START_S, svc))
            return 1
        if time.time() > deadline:
            out("PAIRWAIT: still running after %d s; the service %s" % (PAIRWAIT_MAX_S, svc))
            return 1
        time.sleep(PAIRWAIT_STEP_S)


def mode_pair():
    st = load_state()
    mark = st.get("marks", {}).get("pairoff")
    assert mark is not None, "pair: no pairoff mark"
    recs, _tail = ledger(PB_ARCH + "/ledger.jsonl")
    a, _start, mine = first_start(recs, mark["ns"])
    for r in mine:
        out("R %s" % json.dumps(r, sort_keys=True))
    with open(PB_ASVC + "/commit.txt", encoding="utf-8") as fh:
        commit = fh.read().strip()
    tag = "pairbook-streams-%d" % a if a is not None else None
    obj, peeled = ls_remote_tag(tag) if tag else (None, None)
    pb = show(UNITS["pairbook"], ["MainPID", "NRestarts", "ActiveState", "SubState", "UnitFileState", "Result"])
    tmr = show(PB_TIMER, ["ActiveState", "SubState", "UnitFileState", "NextElapseUSecRealtime"])
    svc = show(PB_SVC, ["ActiveState", "Result", "ExecMainStatus"])
    procs = processes_with(PB_ARGV)
    out("the run begun or resumed after the pairoff mark: %s; the tag %s at %s, peeled %s; the archive's commit %s" % (
        a, tag, obj, peeled, commit))
    out("the pair book %s; its archive's timer %s; its archive's service %s; processes of the pair book %s" % (
        pb, tmr, svc, procs))
    view = store_view(PB, "pb")
    for t in sorted(view["by_dir"]):
        out("RESIDUAL window %d %s: %d bytes of stream" % (t, utc(t), view["by_dir"][t]))
    out("the pair book's store: %d stream files, %d bytes, in %d windows; %d other files, %d bytes" % (
        view["streams_n"], view["streams_bytes"], len(view["by_dir"]), view["other_n"], view["other_bytes"]))
    checks = pair_reading(mine, obj, commit, pb, tmr, svc, procs)
    for k, v in checks.items():
        out("G-PAIR %-46s %s" % (k, v))
    bad = sorted(k for k, v in checks.items() if not v)
    out("G-PAIR %s" % ("PASS: %d of %d" % (len(checks), len(checks)) if not bad else "FAIL: %r" % bad))
    return 0 if not bad else 4


def mode_timer():
    now = time.time()
    kv = show(RB_TIMER, ["LoadState", "ActiveState", "SubState", "UnitFileState", "FragmentPath", "Unit",
                         "TimersCalendar", "TimersMonotonic", "NextElapseUSecRealtime", "NextElapseUSecMonotonic",
                         "AccuracyUSec", "LastTriggerUSec", "ActiveEnterTimestamp"])
    pb = show(PB_TIMER, ["ActiveState", "UnitFileState"])
    installed = sha256_file(UNIT_DIR + "/" + RB_TIMER)[0]
    out("the timer: %r; installed sha256 %s; the pair book archive's timer %r" % (kv, installed, pb))
    checks = timer_checks(kv, now, installed, pb)
    for k, v in checks.items():
        out("G-TIMER %-52s %s" % (k, v))
    bad = sorted(k for k, v in checks.items() if not v)
    assert not bad, "G-TIMER FAIL: %r" % bad
    out("G-TIMER PASS: %d of %d; the next run at %s" % (len(checks), len(checks), utc(next_calendar(now))))
    return 0


def read_slot(root, s):
    """Every slot.json of slot s, by index: [(k, doc)]."""
    d = os.path.join(root, str(s // DAY * DAY))
    found = []
    if os.path.isdir(d):
        for n in sorted(os.listdir(d)):
            m = RB_SLOT_RE.fullmatch(n)
            if m is not None and int(m.group(1)) == s:
                with open(os.path.join(d, n), "rb") as fh:
                    found.append((int(m.group(2)), json.loads(fh.read())))
    return sorted(found, key=lambda x: x[0])


def mode_first():
    """The reward book archive's first run on the new calendar, re-read: exit 3 while it has not ended or G-NEXT's
    slots are not yet due; on a deferral, READING G-RUN: DEFERRED and exit 3 until B-RETRY's run ends."""
    st = load_state()
    mark = st.get("marks", {}).get("timer")
    assert mark is not None, "first: no timer mark"
    elapse = next_calendar(mark["ns"] / 1e9)
    now = time.time()
    recs, _tail = ledger(RB_ARCH + "/ledger.jsonl")
    for r in recs:
        if r.get("event") == "start" and mark["ns"] <= r.get("wall_ns", 0) < (elapse - 1) * 10 ** 9:
            out("a run begun before the first elapse: %s at %s" % (r.get("run"), utc(r["wall_ns"] / 1e9)))
    a, start, mine = first_start(recs, (elapse - 1) * 10 ** 9)
    svc = show(RB_SVC, ["ActiveState", "Result", "ExecMainStatus", "ExecMainStartTimestamp", "ExecMainExitTimestamp"])
    if a is None:
        if now < elapse + FIRST_LATE_S:
            out("NOT YET: no run since %s, the first elapse; the service %s" % (utc(elapse), svc.get("ActiveState")))
            return 3
        out("READING G-TRIGGER: FAIL - no run begun by %s" % utc(elapse + FIRST_LATE_S))
        return 1
    state = run_state(mine)
    if state == "running" or svc.get("ActiveState") in RUNNING:
        out("NOT YET: run %d %s; the service %s" % (a, state, svc.get("ActiveState")))
        return 3
    for r in mine:
        out("R %s" % json.dumps(r, sort_keys=True))
    defers = sum(1 for r in mine if r.get("event") == "deferred")
    if state == "deferred":
        out("READING G-RUN: DEFERRED - run %d, deferral %d" % (a, defers))
        return 3
    drecs = []
    dpath = os.path.join(RB_ARCH, "runs", str(a), "delete.jsonl")
    if os.path.exists(dpath):
        with open(dpath, encoding="utf-8") as fh:
            drecs = [json.loads(ln) for ln in fh if ln.strip()]
    slots = next_slots(drecs[0]["start_ns"], drecs[-1]["removed_wall_ns"]) if drecs else []
    if state == "complete" and slots and now < slots[-1] + SLOT_JSON_AT + NEXT_SETTLE_S:
        out("NOT YET: run %d complete; G-NEXT's last slot %d is due at %s" % (
            a, slots[-1], utc(slots[-1] + SLOT_JSON_AT + NEXT_SETTLE_S)))
        return 3
    readings = {}
    tmr = show(RB_TIMER, ["LastTriggerUSec"])
    s0 = start["wall_ns"] // 10 ** 9
    readings["G-TRIGGER"], source, trig = trigger_reading(start.get("trigger"), elapse, s0,
                                                          stamp_of(tmr.get("LastTriggerUSec")))
    out("G-TRIGGER, by %s: the elapse %s, the trigger %s, the run's start record %s, %s" % (
        source, utc(elapse), utc(trig or 0), utc(s0), "a pending set resumed" if start.get("resumed") else "a new set"))
    comp = ([r for r in mine if r.get("event") == "complete"] or [{}])[-1]
    readings["G-RUN"] = (state == "complete" and defers <= 1 and not any(r.get("event") == "halt" for r in mine)
                         and svc.get("Result") == "success" and svc.get("ExecMainStatus") == "0"
                         and comp.get("started_outside") == 0 and comp.get("ended_outside") == 0)
    out("G-RUN: run %d %s, %d deferrals; the service Result %s, ExecMainStatus %s, %s to %s; %s requests and %s "
        "removals, %s started and %s ended outside the idle stretch; %s files, %s bytes" % (
            a, state, defers, svc.get("Result"), svc.get("ExecMainStatus"), svc.get("ExecMainStartTimestamp"),
            svc.get("ExecMainExitTimestamp"), comp.get("requests"), comp.get("removals"), comp.get("started_outside"),
            comp.get("ended_outside"), comp.get("assets_n"), comp.get("bytes_total")))
    with open(RB_ASVC + "/commit.txt", encoding="utf-8") as fh:
        commit = fh.read().strip()
    tag = "rewardbook-streams-%d" % a
    obj, peeled = ls_remote_tag(tag)
    readings["G-TAG"] = state == "complete" and obj == commit and peeled is None
    out("G-TAG: %s at %s, peeled %s; the archive's commit %s" % (tag, obj, peeled, commit))
    pid0 = (start.get("rewardbook") or {}).get("MainPID")
    rt, _tail = ledger(RB + "/runtime.jsonl")
    verdicts = []
    for s in slots:
        errs = [r for r in rt if r.get("event") == "error" and r.get("what") == "slot %d" % s]
        v, why = next_verdict(read_slot(RB, s), errs, pid0)
        verdicts.append((v, why))
        out("G-NEXT slot %d %s, decided at %s: %s - %s" % (s, utc(s), utc(s - DECIDE_S), v, why))
    reading = next_reading(verdicts)
    readings["G-NEXT"] = reading != "FAIL" and bool(slots)
    out("READING G-NEXT: %s over %d slots, the reward book's process at the run's start %s" % (reading, len(slots),
                                                                                              pid0))
    for k, v in readings.items():
        out("READING %-10s %s" % (k, "PASS" if v else "FAIL"))
    bad = sorted(k for k, v in readings.items() if not v)
    out("FIRST %s" % ("PASS: %d of %d" % (len(readings), len(readings)) if not bad else "FAIL: %r" % bad))
    return 0 if not bad else 1


def report_tokens():
    tokens = set()
    for name in sorted(os.listdir(REPORTS)):
        if name.endswith(".md"):
            with open(os.path.join(REPORTS, name), encoding="utf-8", errors="replace") as fh:
                tokens.update(TOKEN.findall(fh.read()))
    return tokens


def by_name(tree, rel):
    return tree == WORK and (rel in ("state.json", "forensics-plan.json", "forensics-removed.jsonl",
                                     "room-before.json", "room-after.json") or rel.startswith("logs/"))


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
            owner = [p for p, s, _a in procs if s - 1 <= b <= s + LIVE_S]
            assert not owner, "reclaim: %s belongs to the running process %s" % (t, owner)
    tokens = report_tokens()
    lengths = sorted({len(t) for t in tokens})
    before = tree_count(FORENSICS)[0]
    out("reclaim: %d report tokens; the forensic store holds %d files" % (len(tokens), before))
    considered = named = kept = copied = held = 0
    for tree in trees:
        if tree == WORK and os.path.isdir(WT):
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
                is_named = any(h[:k] in tokens for k in lengths)
                is_kept = by_name(tree, rel)
                if not (is_named or is_kept):
                    continue
                named += 1 if is_named else 0
                kept += 1 if is_kept and not is_named else 0
                dest = os.path.join(FORENSICS, os.path.basename(tree) + "--" + rel.replace("/", "--"))
                if os.path.exists(dest):
                    assert sha256_file(dest)[0] == h, "reclaim: %s exists with another sha256" % dest
                    held += 1
                    out("R held   %s %s" % (h, dest))
                    continue
                size, free = os.path.getsize(path), free_bytes()
                assert free - size >= RECLAIM_FLOOR, "BLOCKED: reclaim: %d bytes free, %s is %d" % (free, path, size)
                with open(path, "rb") as src, open(dest, "xb") as dst:
                    shutil.copyfileobj(src, dst, 1 << 20)
                assert sha256_file(dest)[0] == h, "reclaim: %s did not copy whole" % dest
                copied += 1
                out("R copied %s %s" % (h, dest))
    after = tree_count(FORENSICS)[0]
    assert after == before + copied, "reclaim: store %d, expected %d" % (after, before + copied)
    out("RECLAIM PASS: %d files considered, %d named by a report, %d kept by name, %d copied, %d already held; "
        "the forensic store %d -> %d files" % (considered, named, kept, copied, held, before, after))
    return 0

# ---- the self-test: literals, temporary trees under the work tree and a loopback server -----------------------


class _FakeGitHub(http.server.BaseHTTPRequestHandler):
    """GitHub's list endpoints and downloads for the self-test, from the class's `rels` and `blobs`."""
    rels, blobs, seen = [], {}, []

    def log_message(self, *args):
        pass

    def do_GET(self):
        u = urllib.parse.urlsplit(self.path)
        q = dict(urllib.parse.parse_qsl(u.query))
        type(self).seen.append((self.headers.get("User-Agent"), self.headers.get("Authorization"), u.path))
        page, per = int(q.get("page", "1")), int(q.get("per_page", "30"))
        body, ctype = None, "application/json"
        if u.path == "/repos/%s/releases" % REPO:
            body = json.dumps(self.rels[(page - 1) * per:page * per]).encode()
        m = re.fullmatch(r"/repos/%s/releases/([0-9]+)/assets" % re.escape(REPO), u.path)
        if m:
            rel = [r for r in self.rels if r["id"] == int(m.group(1))]
            assets = rel[0]["assets"] if rel else []
            body = json.dumps(assets[(page - 1) * per:page * per]).encode()
        if u.path.startswith("/%s/releases/download/" % REPO):
            body, ctype = self.blobs.get(urllib.parse.unquote(u.path)), "application/octet-stream"
        if body is None:
            self.send_response(404)
            self.end_headers()
            return
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def mode_selftest():
    checks = []

    def ok(cond, what):
        assert cond, "SELFTEST FAIL: %s" % what
        checks.append(what)
        out("ok %d %s" % (len(checks), what))

    if os.path.exists(TMP):
        shutil.rmtree(TMP)
    os.makedirs(TMP)
    d0 = 1794873600                                   # 2026-11-17 00:00:00 UTC
    # the calendar and the bands
    day = [d0 + CAL_FIRST_S + k * CAL_STEP_S for k in range(8)]
    ok([time.strftime("%H:%M:%S", time.gmtime(t)) for t in day] == ["01:30:20", "04:30:20", "07:30:20", "10:30:20",
                                                                    "13:30:20", "16:30:20", "19:30:20", "22:30:20"]
       and all(is_calendar(t) for t in day) and is_calendar(d0 - 5380) and not is_calendar(d0 + 5421)
       and not is_calendar(d0 + 1820),
       "the eight elapses of a day are systemd's iterations of *-*-* 01/3:30:20 UTC")
    ok(next_calendar(d0) == d0 + 5420 and next_calendar(d0 + 5420) == d0 + 16220
       and next_calendar(d0 + 81020) == d0 + DAY + 5420 and next_calendar(d0 + 37819.5) == d0 + 37820,
       "the next elapse is strictly after the instant, across midnight too")
    tb = lambda s, rb="inactive", pb="inactive": band_reading("timer", d0 + s, rb, pb)[0]
    ok(tb(36320) and tb(37220) and tb(69620) and not tb(36319) and not tb(37221) and not tb(25520)
       and not tb(80120) and not tb(36500, rb="activating") and not tb(36500, pb="active") and tb(36500, rb="failed"),
       "B-TIMER's band: 25 to 10 minutes before an elapse, 10:05:20 to 19:20:20 UTC, neither archive running")
    pbnd = lambda s, rb="inactive", pb="inactive": band_reading("pairoff", d0 + s, rb, pb)[0]
    ok(pbnd(27000) and pbnd(68400) and not pbnd(26999) and not pbnd(68401) and not pbnd(40000, pb="activating")
       and not pbnd(40000, rb="active"), "B-PAIR-OFF's band: 07:30:00 to 19:00:00 UTC, neither archive running")
    # G-TIMER on literals
    now = d0 + 36400
    kv = {"LoadState": "loaded", "ActiveState": "active", "SubState": "waiting", "UnitFileState": "enabled",
          "FragmentPath": "/etc/systemd/system/btc-rewardbook-archive.timer", "Unit": RB_SVC,
          "TimersCalendar": "{ OnCalendar=*-*-* 01/3:30:20 UTC ; next_elapse=Tue 2026-11-17 10:30:20 UTC }",
          "NextElapseUSecRealtime": "Tue 2026-11-17 10:30:20 UTC", "AccuracyUSec": "1s"}
    pbt = {"ActiveState": "inactive", "UnitFileState": "disabled"}
    good = timer_checks(kv, now, TIMER_SHA256, pbt)
    variants = [dict(kv, TimersMonotonic="{ OnActiveUSec=30min ; next_elapse=1h }"),
                dict(kv, TimersCalendar=kv["TimersCalendar"] + "\n{ OnCalendar=*-*-* 01:30:20 UTC ; next_elapse=x }"),
                dict(kv, NextElapseUSecRealtime="Wed 2026-11-18 01:30:20 UTC"), dict(kv, UnitFileState="disabled"),
                dict(kv, AccuracyUSec="1min"), dict(kv, Unit="other.service")]
    ok(all(good.values()) and len(good) == 11 and not any(all(timer_checks(v, now, TIMER_SHA256, pbt).values())
                                                          for v in variants)
       and not all(timer_checks(kv, now, OLD_TIMER_SHA256, pbt).values())
       and not all(timer_checks(kv, now, TIMER_SHA256, {"ActiveState": "active", "UnitFileState": "enabled"}).values()),
       "G-TIMER: 11 checks; a run on a start, a second calendar, another elapse, the unit disabled, another accuracy, "
       "another unit, TZ-34's file or the pair book archive's timer enabled each read FAIL")
    ok(stamp_of("Tue 2026-11-17 10:30:20 UTC") == d0 + 37820 and stamp_of("n/a") is None and stamp_of("") is None,
       "systemctl's stamps under TZ=UTC")
    # G-TRIGGER
    e = d0 + 37820
    trg = {"unit": RB_TIMER, "realtime_usec": str((e + 1) * 10 ** 6), "monotonic_usec": "1"}
    ok(trigger_reading(trg, e, e + 1, None)[0] and not trigger_reading(dict(trg, unit=RB_SVC), e, e + 1, None)[0]
       and not trigger_reading(dict(trg, realtime_usec=str((e - 1800) * 10 ** 6)), e, e - 1799, None)[0]
       and not trigger_reading(trg, e, e + 70, None)[0] and trigger_reading({"unit": None}, e, e, e)[0]
       and not trigger_reading({"unit": None}, e, e, None)[0],
       "G-TRIGGER: the timer's own trigger at the elapse; another unit, a trigger 1,800 s early, a late record and "
       "no trigger at all each read FAIL; LastTriggerUSec where systemd set none")
    # the runs of a ledger
    recs = [{"event": "start", "run": 5, "wall_ns": 100}, {"event": "complete", "run": 5, "wall_ns": 110},
            {"event": "start", "run": 9, "wall_ns": 200}, {"event": "deferred", "run": 9, "wall_ns": 210},
            {"event": "start", "run": 9, "wall_ns": 300}]
    a9, s9, m9 = first_start(recs, 150)
    a9b, s9b, m9b = first_start(recs, 250)
    ok(first_start(recs, 0)[0] == 5 and (a9, s9["wall_ns"], len(m9)) == (9, 200, 3) and run_state(m9) == "running"
       and run_state(m9[:2]) == "deferred" and run_state(recs[:2]) == "complete"
       and (a9b, s9b["wall_ns"], len(m9b)) == (9, 300, 1) and first_start(recs, 301)[0] is None,
       "a ledger's first start since an instant - a pending set resumed counts by its new start - and a run's "
       "state from its last start")
    # G-NEXT
    ok(next_slots(1000 * 10 ** 9, 1000 * 10 ** 9) == [1800] and next_slots(890 * 10 ** 9, 900 * 10 ** 9) == [900, 1800]
       and next_reading([("PASS", ""), ("UNDECIDABLE", "")]) == "UNDECIDABLE" and next_reading([]) == "UNDECIDABLE",
       "G-NEXT's slots across the removals, and its reading the worst")
    sj = {"pid": 77, "stream": {"opened": True, "off_reason": None}, "error": None, "stopped": False}
    ok(next_verdict([(0, sj)], [], "77")[0] == "PASS" and next_verdict([], [], "77")[0] == "FAIL"
       and next_verdict([(0, sj)], [{"error": "x"}], "77")[0] == "FAIL"
       and next_verdict([(0, dict(sj, stream={"opened": False, "off_reason": "floor"}))], [], "77")[0] == "UNDECIDABLE"
       and next_verdict([(0, sj)], [], "78")[0] == "UNDECIDABLE", "G-NEXT's verdict of one slot")
    # G-STILL
    u = {"recorder": {"MainPID": "1", "NRestarts": "0", "ActiveState": "active"},
         "pairbook": {"MainPID": "10", "NRestarts": "5", "ActiveState": "active"},
         "rewardbook": {"MainPID": "2", "NRestarts": "0", "ActiveState": "active"},
         "advisor": {"MainPID": "3", "NRestarts": "0", "ActiveState": "active"}}
    rs = [{"stopped": "10", "pid": "11", "NRestarts": "6"}]
    stopped = dict(u, pairbook={"MainPID": "0", "NRestarts": "6", "ActiveState": "inactive"})
    moved = dict(u, pairbook={"MainPID": "11", "NRestarts": "6", "ActiveState": "active"})
    ok(still_reading(u, u, [], False)[0] and still_reading(u, moved, rs, False)[0]
       and still_reading(u, stopped, rs, True)[0] and still_reading(u, stopped, [], True)[0]
       and not still_reading(u, stopped, rs, False)[0]
       and not still_reading(u, dict(u, recorder={"MainPID": "4", "NRestarts": "1", "ActiveState": "active"}), [], True)[0]
       and not still_reading(u, moved, [{"stopped": "9", "pid": "11", "NRestarts": "6"}], True)[0]
       and not still_reading(u, moved, [], False)[0],
       "G-STILL: unchanged; moved by its archive's restarts; stopped after B-PAIR-OFF alone; anything else FAIL")
    # G-PAIR
    run = [{"event": "start", "run": 7}, {"event": "set", "run": 7}, {"event": "delete", "run": 7},
           {"event": "restart", "run": 7}, {"event": "resume", "run": 7, "reading": "PASS"},
           {"event": "complete", "run": 7, "started_outside": 0, "ended_outside": 0}]
    off = {"MainPID": "0", "ActiveState": "inactive", "UnitFileState": "disabled"}
    toff = {"ActiveState": "inactive", "UnitFileState": "disabled"}
    sidle = {"ActiveState": "inactive"}
    gp = pair_reading(run, "c" * 40, "c" * 40, off, toff, sidle, [])
    bads = [pair_reading(run[:-1] + [{"event": "deferred", "run": 7}], "c" * 40, "c" * 40, off, toff, sidle, []),
            pair_reading(run, "d" * 40, "c" * 40, off, toff, sidle, []),
            pair_reading(run, "c" * 40, "c" * 40, dict(off, UnitFileState="enabled"), toff, sidle, []),
            pair_reading(run, "c" * 40, "c" * 40, off, toff, sidle, [4242]),
            pair_reading(run, "c" * 40, "c" * 40, off, dict(toff, UnitFileState="enabled"), sidle, []),
            pair_reading(run[:3] + run[5:], "c" * 40, "c" * 40, off, toff, sidle, []),
            pair_reading(run[:5] + [dict(run[5], started_outside=1)], "c" * 40, "c" * 40, off, toff, sidle, []),
            pair_reading(run, "c" * 40, "c" * 40, off, toff, {"ActiveState": "activating"}, [])]
    ok(all(gp.values()) and len(gp) == 8 and not any(all(b.values()) for b in bads),
       "G-PAIR: 8 checks; a deferred run, another tag, the pair book enabled or running, its timer enabled, no "
       "restart, a request outside the idle stretch or the service running each read FAIL")
    # G-ROOM
    base = STREAM_FLOOR + PEAK + ROOM_MIN
    ok(PEAK == 445535636 and room_reading(base - 10, 10) == (base, ROOM_MIN, True)
       and not room_reading(base - 11, 10)[2], "G-ROOM at its bound, and a byte below it")
    # NUMBER, reclaim's predicates, the timer file and the reward book's floor
    names = ["CryptoTZ/TZ-45-l0-rule-w.md", OWN_TZ, "CryptoReports/TZ-45-l0-rule-w-report.md"]
    ok(number_reading(names, OWN_TZ)[0] and not number_reading(names + ["CryptoTZ/TZ-46-other.md"], OWN_TZ)[0]
       and not number_reading(names + ["CryptoReports/TZ-46-capture-room-report.md"], OWN_TZ)[0],
       "NUMBER: this TZ's file alone of its number, and no report")
    ok(by_name(WORK, "logs/01.log") and by_name(WORK, "forensics-plan.json") and not by_name(WORK, "wt/x")
       and reclaimable(WORK) and not reclaimable("/root") and not reclaimable("/tmp/x"),
       "reclaim keeps by name the state, the plan, the removals, both room files and the logs")
    tfile = os.path.join(os.path.dirname(HERE), TIMER_REL)
    with open(tfile, "rb") as fh:
        traw = fh.read()
    tl = traw.decode("utf-8").split("\n")
    ok(sha256_bytes(traw) == TIMER_SHA256 and "OnCalendar=" + CALENDAR in tl and "AccuracySec=1s" in tl
       and "Unit=" + RB_SVC in tl and not any(x.startswith(("OnActiveSec", "OnBootSec", "OnStartupSec",
                                                             "OnUnitActiveSec", "OnUnitInactiveSec", "Persistent"))
                                              for x in tl),
       "the branch's timer: its SHA-256, one calendar, accuracy 1 s, its unit, no monotonic trigger")
    with open(os.path.join(os.path.dirname(HERE), TZ33_REL), "rb") as fh:
        t33 = fh.read()
    ok(sha256_bytes(t33) == TZ33_SHA256 and t33.split(b"\n")[189].startswith(b"STREAM_FLOOR = %d " % STREAM_FLOOR),
       "STREAM_FLOOR is the reward book's own, line 190 of its file as its unit runs it")
    # the hook's decisions
    al = {FORENSICS + "/a"}
    pol = lambda mode, ev, args: policy(mode, ev, args, al) is None
    ok(pol("room", "open", (WORK + "/room-after.json", "wb", 0)) and not pol("room", "open", ("/root/x", "w", 0))
       and pol("first", "open", (RB + "/1794873600/1794873600.0.slot.json", "rb", 0))
       and pol("first", "open", (RB + "/runtime.jsonl", "rb", 0))
       and not pol("first", "open", (RB + "/1794873600/1794873600.0.stream.jsonl.gz", "rb", 0))
       and not pol("first", "open", (RB + "/1794873600/1794873600.0.rewards.jsonl.gz", "rb", 0))
       and not pol("first", "open", (RB + "/1794873600/select.0.json", "rb", 0))
       and not pol("first", "open", (RB + "/runtime.jsonl", "ab", 0))
       and not pol("pair", "open", (PB + "/1794873600/window.json", "rb", 0))
       and not pol("room", "open", (RECORDER + "/runtime.jsonl", "rb", 0))
       and not pol("room", "os.scandir", (RECORDER,)) and pol("room", "os.scandir", (RB,))
       and pol("room", "os.scandir", (PB,)),
       "the hook: writes in the work tree alone; of the reward book its slot records and runtime.jsonl read, nothing "
       "else opened; nothing of the pair book or the recorder opened")
    ok(pol("forensics-remove", "os.remove", (FORENSICS + "/a", None))
       and not pol("forensics-remove", "os.remove", (FORENSICS + "/b", None))
       and not pol("forensics", "os.remove", (FORENSICS + "/a", None))
       and not pol("forensics-remove", "os.remove", (RB + "/1794873600/1794873600.0.slot.json", None))
       and pol("reclaim", "open", (FORENSICS + "/tz46-work--state.json", "xb", 0))
       and not pol("reclaim", "open", (FORENSICS + "/tz46-work--state.json", "wb", 0))
       and not pol("forensics", "open", (FORENSICS + "/a", "ab", 0)) and pol("forensics", "open", (FORENSICS + "/a", "rb", 0))
       and pol("selftest", "shutil.rmtree", (TMP, None)) and not pol("selftest", "shutil.rmtree", (FORENSICS, None)),
       "the hook: a forensic file removed only by forensics-remove and only where planned; the store written only "
       "by reclaim's exclusive create")
    ok(pol("forensics", "socket.getaddrinfo", ("api.github.com", 443)) and
       pol("forensics", "socket.getaddrinfo", ("release-assets.githubusercontent.com", 443))
       and not pol("forensics", "socket.getaddrinfo", ("clob.polymarket.com", 443))
       and not pol("forensics", "socket.getaddrinfo", ("fapi.binance.com", 443)),
       "the hook: GitHub's hosts alone are reached")
    # the stores by their directory entries
    rbt, pbt2 = os.path.join(TMP, "rb"), os.path.join(TMP, "pb")
    for p, n in ((rbt + "/1794873600/1794873600.0.stream.jsonl.gz", 100), (rbt + "/1794873600/1794873600.1.stream.jsonl.gz", 7),
                 (rbt + "/1794873600/1794873600.0.slot.json", 3), (rbt + "/1794873600/1794873600.0.rewards.jsonl.gz", 5),
                 (rbt + "/1794873600/select.0.json", 11), (rbt + "/runtime.jsonl", 13),
                 (pbt2 + "/1794873600/stream.jsonl.gz", 50), (pbt2 + "/1794873600/stream.1.jsonl.gz", 9),
                 (pbt2 + "/1794873600/window.json", 2), (pbt2 + "/1794874500/books.jsonl.gz", 4)):
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "wb") as fh:
            fh.write(b"x" * n)
    v1, v2 = store_view(rbt, "rb"), store_view(pbt2, "pb")
    ok((v1["streams_n"], v1["streams_bytes"], v1["other_n"], v1["other_bytes"], v1["dirs"]) == (2, 107, 4, 32, 1)
       and (v2["streams_n"], v2["streams_bytes"], v2["other_n"], v2["other_bytes"], v2["dirs"]) == (2, 59, 2, 6, 2)
       and v2["by_dir"] == {1794873600: 59}, "both stores' stream and other files by their own names")
    # the forensic store against a loopback GitHub
    fz = os.path.join(TMP, "forensics")
    files = {"a.tar": b"A" * 3000, "b.json": b"B" * 70, "c.log": b"C" * 9, "sub/d.copy": b"A" * 3000,
             "e.empty": b"", "f.bin": b"F" * 40, "g.bin": b"G" * 41, "h.bin": b"H" * 42}
    for name, data in files.items():
        os.makedirs(os.path.dirname(os.path.join(fz, name)), exist_ok=True)
        with open(os.path.join(fz, name), "wb") as fh:
            fh.write(data)
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), _FakeGitHub)
    port = srv.server_address[1]
    base = "http://127.0.0.1:%d" % port
    th = threading.Thread(target=srv.serve_forever, daemon=True)
    th.start()
    dig = lambda b: "sha256:" + sha256_bytes(b)

    def asset(aid, tag, name, data, state="uploaded", digest=None):
        return {"id": aid, "name": name, "size": len(data), "state": state, "digest": digest or dig(data),
                "browser_download_url": download_url(base, tag, name)}
    _FakeGitHub.rels = [{"id": 1, "tag_name": "tz-44-l0-inputs", "draft": False,
                         "assets": [asset(11, "tz-44-l0-inputs", "a.tar", files["a.tar"]),
                                    asset(12, "tz-44-l0-inputs", "f.bin", files["f.bin"], state="starter")]},
                        {"id": 2, "tag_name": "rewardbook-streams-1", "draft": False,
                         "assets": [asset(21, "rewardbook-streams-1", "b.json", files["b.json"], digest=dig(b"other")),
                                    asset(22, "rewardbook-streams-1", "g.bin", files["g.bin"]),
                                    asset(23, "rewardbook-streams-1", "h.bin", files["h.bin"])]},
                        {"id": 3, "tag_name": "draft", "draft": True,
                         "assets": [asset(31, "draft", "c.log", files["c.log"])]}]
    _FakeGitHub.rels += [{"id": 100 + k, "tag_name": "pairbook-streams-%d" % k, "draft": False, "assets": []}
                         for k in range(120)]
    _FakeGitHub.blobs = {"/%s/releases/download/tz-44-l0-inputs/a.tar" % REPO: files["a.tar"],
                         "/%s/releases/download/rewardbook-streams-1/g.bin" % REPO: b"G" * 40 + b"g",
                         "/%s/releases/download/rewardbook-streams-1/h.bin" % REPO: files["h.bin"]}
    _FakeGitHub.seen = []
    plan, removed, sp = os.path.join(TMP, "plan.json"), os.path.join(TMP, "removed.jsonl"), os.path.join(TMP, "st.json")
    COUNTS.update({"requests": 0, "downloads": 0, "download_bytes": 0, "removed": 0})
    try:
        short = False
        try:
            mode_forensics(fz, base, base, plan, sp, least={"tz-44-l0-inputs": 3})
        except AssertionError as exc:
            short = "no plan written" in str(exc)
        ok(short and not os.path.exists(plan) and not os.path.exists(sp),
           "forensics: fewer files proved against a named Release than expected is BLOCKED, and no plan is written")
        COUNTS.update({"requests": 0, "downloads": 0, "download_bytes": 0, "removed": 0})
        mode_forensics(fz, base, base, plan, sp, least={"tz-44-l0-inputs": 2})
        with open(plan, "rb") as fh:
            pdoc = json.loads(fh.read())
        got = sorted((os.path.relpath(r["path"], fz), r["api_ok"], r["download_ok"]) for r in pdoc["rows"])
        ok(got == [("a.tar", True, True), ("g.bin", True, False), ("h.bin", True, True), ("sub/d.copy", True, True)]
           and pdoc["planned_n"] == 3 and pdoc["files_n"] == 7 and pdoc["releases_n"] == 123
           and COUNTS["downloads"] == 3 and COUNTS["requests"] == 9,
           "forensics: a file and its copy held by one asset, downloaded once; a digest of other bytes, an asset not "
           "uploaded, a draft and an empty file left; a download of other bytes not planned; 7 pages, 2 asset lists")
        ok(all(ua == UA and auth is None for ua, auth, _p in _FakeGitHub.seen),
           "every request names this file's User-Agent and carries no credential")
        with open(os.path.join(fz, "h.bin"), "ab") as fh:
            fh.write(b"!")
        blocked = False
        MODE[0] = "forensics-remove"
        try:
            mode_forensics_remove(fz, plan, removed, sp)
        except AssertionError as exc:
            blocked = "nothing removed" in str(exc)
        ok(blocked and all(os.path.exists(os.path.join(fz, n)) for n in ("a.tar", "sub/d.copy", "h.bin"))
           and not os.path.exists(removed), "a planned file changed after its proof: BLOCKED, nothing removed")
        with open(os.path.join(fz, "h.bin"), "wb") as fh:
            fh.write(files["h.bin"])
        mode_forensics_remove(fz, plan, removed, sp)
        left = sorted(os.path.relpath(f["path"], fz) for f in forensic_files(fz, hashed=False))
        ok(left == ["b.json", "c.log", "f.bin", "g.bin"] and os.path.exists(os.path.join(fz, "e.empty"))
           and COUNTS["removed"] == 3, "forensics-remove: the three proved files gone, every other file kept")
        COUNTS["removed"] = 0
        mode_forensics_remove(fz, plan, removed, sp)
        with open(removed, encoding="utf-8") as fh:
            rows = [json.loads(ln) for ln in fh if ln.strip()]
        ok(COUNTS["removed"] == 0 and len(rows) == 3, "forensics-remove again removes nothing and records nothing twice")
        guarded = False
        MODE[0] = "forensics"
        try:
            os.remove(os.path.join(FORENSICS, "never-there"))
        except GuardError:
            guarded = True
        ok(guarded, "the hook refuses a removal in the real forensic store outside forensics-remove")
    finally:
        MODE[0] = "selftest"
        srv.shutdown()
        srv.server_close()
    shutil.rmtree(TMP)
    ok(not os.path.exists(TMP), "the temporary trees removed")
    out("SELFTEST PASS: %d checks" % len(checks))
    return 0


def main(argv):
    if not argv:
        sys.exit("usage: %s MODE [ARG...]" % PYFILE)
    mode, rest = argv[0], argv[1:]
    assert os.getcwd() == WORK, "run from %s, not %s" % (WORK, os.getcwd())
    MODE[0] = mode
    table = {"fingerprint": mode_fingerprint, "number": mode_number, "selftest": mode_selftest,
             "still": mode_still, "forensics": mode_forensics, "forensics-remove": mode_forensics_remove,
             "pairwait": mode_pairwait, "pair": mode_pair, "timer": mode_timer, "first": mode_first}
    one = {"scratch": mode_scratch, "room": mode_room, "mark": mode_mark, "band": mode_band}
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
        out("opens refused: %d; reward book opens: %d; API requests %d, downloads %d, %d bytes; files removed %d" % (
            len(REFUSED), COUNTS["reward book opens"], COUNTS["requests"], COUNTS["downloads"],
            COUNTS["download_bytes"], COUNTS["removed"]))
    return rc or 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
```

### `deploy/systemd/btc-rewardbook-archive.timer`

```ini file=deploy/systemd/btc-rewardbook-archive.timer
# btc-5m-twap: the reward book's archive, every three hours from 01:30:20 UTC, and no run on a start of the timer (TZ-46).
# Installed byte for byte as /etc/systemd/system/btc-rewardbook-archive.timer; its stop is systemctl disable --now.
[Unit]
Description=btc-5m-twap reward book archive, every three hours

[Timer]
OnCalendar=*-*-* 01/3:30:20 UTC
AccuracySec=1s
Unit=btc-rewardbook-archive.service

[Install]
WantedBy=timers.target
```
