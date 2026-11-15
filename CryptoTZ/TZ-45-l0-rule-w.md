# TZ-45 — L0's second rule, rule W: does a two-sided quote of ours at a reward market's minimum size, alone inside the band of a wide touch, simulated on the reward book's streams of five days no one has read, collect more in liquidity rewards and maker rebates than its fills lose — and the reading's inputs, off the host with it

**Canonical filename:** `TZ-45-l0-rule-w.md`. The committed file takes this name and no other.

**Executor model: Claude Opus 5.5.** Gate arithmetic on days no one has read, a store under a reserve, a replay held to another unit's idle stretch, a credential's block and its proof by anonymous download.

**Required System Map revision:** `2026-11-13-a` — `main` at `5192aff`, PR #44's merge, above `56d343b`, which carries it; the Boss's request named it with its §2.6 and its §7 item 164. **No map revision ships with this TZ.**

**Map sections this TZ rests on**, copied from §10's C8 (map §7 item 141): §0, the fingerprint gate and its table; §1, the refs; §2.5, the pair book's idle stretch and its archive's calendar run; §2.6, the reward book — its store, its archive, the reserve, L0's reading, the Architect's exploration and rule W; §3, the forensic store, the worktrees and the code trees; §6, its rows host, host identity, language, git remote, disk, process supervision, memory, venue geoblock, sandbox limit — network, GitHub Releases, sandbox limit — destructive actions, and harness; §7 items 115, 118 to 120, 124, 129, 131, 132, 137, 138, 140, 141, 143, 144, 149 to 157 and 162 to 167.

**Required anchors**, from map §0. A mismatch on any one is BLOCKED before any work:

| anchor | required |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `0f6c90451cbd` |
| `A6` — pricer | `729f0bcdbee3` |

**Host gate:** §0.3. This TZ runs on the capture host for the reward book's store and its archive's record, the forensic store and the repository's credential; it downloads every stream it replays from the archive's public Releases.

**Before `EXECUTE TZ-45`:** the Boss uploads this file into `CryptoTZ/`, and nothing else. No step of his is a precondition of the run (map §7 item 132). **The Boss is needed at the VPS once while it runs: B-UPLOAD, §3.11, is his block by its own text** — one line, pasted into a root shell, about two hours after the start.

**When: on any day from 2026-11-15, begun at 07:30:00 to 21:00:00 UTC, once five candidate days are whole.** §0.0 reads the clock and then the store's slot records before anything else and, outside that band or short of five whole days, begins nothing and owes no report. Six candidates have ended, 2026-11-09 to 2026-11-14, and the sixth's streams left the host with the archive's run of 2026-11-15 01:30:20 UTC — its tag `rewardbook-streams-1794706220` is on `origin` — so a run begun on 2026-11-15 completes its set where five of the six qualify, and each day later absorbs one non-member more, to three (§1, when). 07:30 is clear of the package manager's morning run, from 06:00 UTC with up to an hour's delay, which restarts capture units (map §7 items 120 and 143); a run begun by 21:00 ends before the next unless B-UPLOAD's wait for the Boss or an incident at GitHub holds it, and G-STILL then reads what that morning restarted (§4.7). About 2 h 45 min of the session's wall clock, and the time the Boss takes to run B-UPLOAD (§6).

**What this TZ is.** L0 read UNDECIDABLE on its first rule (TZ-43; CANON §1.5): the quote was paid on a fifth of its markets and lost about what it was paid. From L0's inputs, public since TZ-44, the Architect explored the eight days already read and found where the venue's pool goes unclaimed — markets whose touch is wider than their reward band, where no displayed order scores — and one rule that the replay pays on every one of those eight days under every bracket (map §2.6; §7 item 164) — and, before fixing it, measured that the venue moves a market's minimum size inside a day, which the rule now reads at every poll (§1; map §7 item 155). **A rule chosen on eight days is gated on none of them.** This TZ fixes that rule, rule W, in its own text, and measures it on the first five qualifying days from 2026-11-09, which no TZ and no session of the Architect has read: **EARN** where, on each of the five days, the least of the four variants whose competitors score the most — each less one adverse fill in every market it quoted — reaches `10` USDC; **NO EARN** where on none of the five the most of the four whose competitors score the least reaches it; **UNDECIDABLE** otherwise (§1, §4.5). And it sends the reading's inputs off the host in its own run (CANON hard rule 16; map §7 item 154): **one Release, on the tag `tz-45-l0-rule-w-inputs`**, of every candidate day's selections, slot records and reward polls and of this run's own work files, so that the Architect re-derives the reading from public bytes. **No order is placed, signed or cancelled, no key of any venue is held, and nothing of L1 is built:** an EARN opens a live step of a fixed loss limit, in a TZ of its own, and proves no income (§1).

---

## 0. Gates

### 0.0 The instant, the set's readiness, then the work tree

After contract §1 steps 1 and 2, and before anything else, in the session:

```
t=$(date -u +%s); s=$(( t % 86400 )); echo "now $t $(date -u -d @$t +%FT%TZ), second of the day $s"; [ "$s" -ge 27000 ] && [ "$s" -le 75600 ]; echo "inside=$?"
```

Then, where it printed `inside=0`, the readiness read — verbatim, read-only, of the reward book's slot records alone, which the reserve excepts (map §2.6):

```
/root/tz04a-env/venv/bin/python -B - <<'EOF2'
import json, os, time
ROOT, FIRST, DAY, SLOT, NEED, LAST, GAP = "/var/lib/btc-rewardbook", 1794182400, 86400, 900, 5, 1794787200, 15 * 10 ** 9
now, whole, d0 = int(time.time()), [], FIRST
while d0 <= LAST and d0 + DAY <= now and len(whole) < NEED:
    why = None
    for S in range(d0, d0 + DAY, SLOT):
        k, end = 0, None
        while why is None:
            p = "%s/%d/%d.%d.slot.json" % (ROOT, d0, S, k)
            if not os.path.exists(p):
                break
            with open(p, "rb") as fh:
                sj = json.loads(fh.read())
            st = sj.get("stream") or {}
            g, a, b, sub = (st.get(x) for x in ("max_gap_ns", "first_frame_wall_ns", "last_frame_wall_ns", "subscribed_wall_ns"))
            if sj.get("error") is not None or st.get("opened") is not True or st.get("cut") is not False \
                    or type(g) is not int or g > GAP or type(a) is not int or type(b) is not int:
                why = "slot %d, its record %d" % (S, k)
            elif k == 0 and (sj.get("joined_late") is not False or type(sub) is not int or sub > S * 10 ** 9):
                why = "slot %d, subscribed late" % S
            elif end is not None and a - end > GAP:
                why = "slot %d, a gap between its files" % S
            else:
                end, k = b, k + 1
        if why is None and k == 0:
            why = "slot %d, no record" % S
        if why is None and end < (S + SLOT) * 10 ** 9:
            why = "slot %d, ended early" % S
        if why is not None:
            break
    print("candidate %d %s: %s" % (d0, time.strftime("%Y-%m-%d", time.gmtime(d0)), "whole" if why is None else "not whole - " + why))
    whole += [d0] if why is None else []
    d0 += DAY
print("ready=%d: %d whole days of %d, candidates to %s, at %d" % (len(whole) >= NEED, len(whole), NEED, time.strftime("%Y-%m-%d", time.gmtime(d0 - DAY)), now))
EOF2
```

**`inside=0` and `ready=1` begin the run. `inside=1`, or `ready=0`, begins nothing:** no directory is made, nothing is written, committed or pushed and no report is written — this TZ has not executed (CANON hard rule 5) — and the Executor tells the Boss in one line, in Russian, the next instant to send `EXECUTE TZ-45` — the next 07:30 UTC, and after `ready=0` the first 07:30 UTC after the next candidate day has ended — and stops. This is not BLOCKED and owes no report (contract §5); a later `EXECUTE TZ-45` starts the TZ afresh. **The readiness read is a courtesy and gates nothing but the start:** it reads, of each slot record, the fields `fetch`'s slot rule reads but the selection's hash and the archive's assets (`slot_problem`, lines 738 to 777), so a day `fetch` takes is whole here; where it ends without a `ready=` line, or the classifier refuses it, the run begins all the same and `fetch`'s own rule decides (§4.2). Then:

```
mkdir /root/tz45-work /root/tz45-work/logs; echo "exit=$?"
```

`exit=0` proves neither existed; anything else is BLOCKED. The clock line and the readiness read are run again into `logs/00-instant.log` and `logs/00-ready.log`. **From here every command's output goes to `/root/tz45-work/logs/`, one file per step, under the names §3's table fixes**, and nothing to the session's scratchpad; B-RECLAIM-OWN, §9, is the one exception.

Three abbreviations: **`P`** is `nice -n 19 /root/tz04a-env/venv/bin/python -B`; **`I0`** is `P /root/tz45-work/stage/research/tz45-l0-rule-w.py`, the staged copy, for §0 alone; and **`I`**, from §3.1 on, is `P /root/tz45-work/wt/research/tz45-l0-rule-w.py`, the committed copy. Every mode runs from `/root/tz45-work` — `main` asserts it (lines 3234 to 3260). **In every block handed to the Boss, both are written out in full.**

### 0.1 The instrument, staged

Extract Appendix A from this TZ as the primary checkout carries it after contract §1's pull, and place TZ-27's instrument beside it — the instrument loads `research/tz27-pairbook-archive.py` from its own directory by its SHA-256 (lines 373 to 384) — with this script, verbatim, its one argument the destination, its output into `logs/01-stage.log`:

```
/root/tz04a-env/venv/bin/python -B - /root/tz45-work/stage <<'EOF2'
import hashlib, os, sys
SRC = "/root/btc-5m-twap/CryptoTZ/TZ-45-l0-rule-w.md"
TZ27 = "/root/btc-5m-twap/research/tz27-pairbook-archive.py"
DEST = sys.argv[1]
WANT = {
    "research/tz45-l0-rule-w.py": "1d415754615a1c037d0b9f695bbff4b3a246ddc62868d50e9e9448ccc55f7484",
}
WANT27 = "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673"
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
path = os.path.join(DEST, "research/tz27-pairbook-archive.py")
if not os.path.exists(path):
    with open(TZ27, "rb") as fh:
        data = fh.read()
    assert hashlib.sha256(data).hexdigest() == WANT27, TZ27
    with open(path, "xb") as fh:
        fh.write(data)
with open(path, "rb") as fh:
    data = fh.read()
assert hashlib.sha256(data).hexdigest() == WANT27, path
print(path, data.count(b"\n"), len(data), hashlib.sha256(data).hexdigest())
EOF2
```

| path | lines | bytes | SHA-256 |
|---|---|---|---|
| `research/tz45-l0-rule-w.py` | 4,230 | 229,313 | `1d415754615a1c037d0b9f695bbff4b3a246ddc62868d50e9e9448ccc55f7484` |
| `research/tz27-pairbook-archive.py` | 2,078 | 106,284 | `2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673` — map §0's `frozen` row |

A failed assert or another hash is BLOCKED. The staged copy runs §0.2's `fingerprint` and §0.5's and §3.1's `number`, and nothing else.

### 0.2 Fingerprint

`I0 fingerprint`, into `logs/02-fingerprint.log`, performs contract §1 steps 3 and 4 inside the instrument and asserts them, against `SYSTEM-MAP.md` and the files of its §0 table in the primary checkout `/root/btc-5m-twap`: revision `2026-11-13-a`; the six anchors; `A2`, `A4`, `A5` and `A6` re-derived as the first 12 hex characters of those files' SHA-256; the table's **63** rows, each printed in lines, bytes and SHA-256 — **60** `frozen` rows asserted equal to the map, **2** `tracked` and **1** `reported`; and the map's own lines, bytes and SHA-256 (lines 2943 to 2970). It prints `FINGERPRINT PASS` or stops at the first mismatch, which is BLOCKED.

### 0.3 Host gate

From `/root/btc-5m-twap`, with `S` first set to the scratchpad directory the session's system prompt names, output verbatim into `logs/03-host-gate.log`:

```
date -u; date -u +%s; uptime -s; journalctl --list-boots --no-pager | tail -n 3
nproc; grep -E '^(MemTotal|MemAvailable|SwapTotal|SwapFree):' /proc/meminfo
df -B1 --output=source,size,avail /var/lib/btc-recorder
find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
grep -c e3975b5da44c5328adf3bf3914634cd878842c73 /var/lib/btc-recorder/runtime.jsonl
/root/tz04a-env/venv/bin/python -c 'import sys; print(sys.version.split()[0])'
stat -c '%s %n' /var/lib/btc-rewardbook-archive/ledger.jsonl /var/lib/btc-rewardbook-archive/runs/1793263627/set.json /var/lib/btc-pairbook-archive/ledger.jsonl
TZ=UTC systemctl show btc-recorder.service btc-pairbook.service btc-rewardbook.service adv3-bot.service btc-pairbook-archive.service btc-pairbook-archive.timer btc-rewardbook-archive.service btc-rewardbook-archive.timer btc-chainbook.service -p Id -p MainPID -p NRestarts -p ActiveState -p SubState -p UnitFileState -p ActiveEnterTimestamp -p Result
TZ=UTC systemctl list-timers btc-pairbook-archive.timer btc-rewardbook-archive.timer apt-daily-upgrade.timer apt-daily.timer --all --no-pager
journalctl _PID=1 -o short-iso --since 2026-11-12 --no-pager | grep -E 'Reload|btc-|adv3' | tail -n 80
grep -E '^(Start-Date|Commandline|Upgrade|End-Date)' /var/log/apt/history.log | tail -n 40
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
systemctl is-active telemetry-watch.service; echo "exit=$?"
cat /root/adv3-bot-svc/commit.txt
test -e /root/tz44-work; echo "/root/tz44-work exit=$?"
for t in /root/btc-recorder-svc /root/btc-pairbook-svc /root/btc-pairbook-archive-svc /root/btc-rewardbook-svc /root/btc-rewardbook-archive-svc /root/adv3-bot-svc; do test -e $t; echo "$t exit=$?"; done
find /root/btc-forensics -type f | wc -l
git -C /root/btc-5m-twap worktree list
du -sb /var/lib/btc-rewardbook /var/lib/btc-pairbook /var/lib/btc-rewardbook-archive /root/btc-forensics /root/.claude-8j 2>&1; journalctl --disk-usage
echo "$S"; ls -la "$(dirname "$(dirname "$S")")"
```

then the memory gate's own reads, appended to the same log:

```
for k in 1 2 3 4 5; do m=$(( $(awk '/^MemAvailable:/ {print $2}' /proc/meminfo) * 1024 )); echo "MemAvailable read $k $(date -u +%T): $m"; [ "$m" -ge 172658448 ] && break; [ "$k" -lt 5 ] && sleep 60; done
```

- **H1** — `find` prints exactly one path.
- **H2** — `df` names source `/dev/vda2` and size `31612203008`; `grep -c` prints at least `1`. With H1 this is map §6's host identity.
- **H3** — the interpreter prints `3.12.`.
- **H4** — `stat` prints all three files: the reward book archive's ledger and its first run's `set.json`, which §3.4 and §3.5 read, and the pair book archive's ledger, which G-STILL reads.
- **H5** — `btc-recorder.service`, `btc-pairbook.service`, `btc-rewardbook.service` and `adv3-bot.service` each read `ActiveState=active` and `UnitFileState=enabled`: G-STILL reads all four (§4.7).
- **Memory gate** — the last `MemAvailable read` at least `172,658,448` bytes: a read below it is read again 60 s later, five reads at most, the first at or above it passing (§0.4; map §7 item 137).
- **Disk gate** — `avail` at least `8,200,000,000` bytes (§0.4).

These are eleven checks — H2 two, H5 four — and any one failing is BLOCKED. **The rest is printed and carries no threshold:** the boots; the units and the timers, both archives' and the package manager's among them; systemd's reload records since 2026-11-12 and the package history, beside which §3.4 reads the reward book archive's runs off its calendar (map §7 items 115, 129 and 166); the consumer's two states, on which map §6's headroom is conditional; the advisor's `commit.txt`, which map §3 names for the service copy — a difference is reported first and BLOCKS nothing, because this TZ's work needs no advisor; `/root/tz44-work` gone, by map §3, and the code trees present; the forensic store's count, map §3's `2,532`; the worktrees, map §3's two; `du` of both stores, as map §2.5 and §2.6 ask, of the reward book archive's state, of the forensic store and of the sessions' configuration directory, and the journal's size, beside `df` (map §7 item 167); and the listing of the directory that holds the session's own, whose UUID directories `I scratch` names live or earlier (§3.3).

### 0.4 Resource floors, in exact bytes

**Disk — three bounds on the free bytes of `/dev/vda2`, each derived from map §6's disk row and map §2.6.** **`7,400,000,000` after any write of this TZ's** (`DISK_FLOOR`, line 164): the reward book's `STREAM_FLOOR`, `7,300,000,000`, below which no stream of it opens for a slot, plus `100,000,000`, one slot of its streams at the cut (`research/tz33-reward-book-capture.py` lines 190 and 192). Every unit re-reads free space before its download and BLOCKS where the download would leave less (`run_unit`, lines 2098 to 2132), `pack` before each day's archive (`pack_day`, lines 2636 to 2681) and `reclaim` before each copy (`mode_reclaim`, lines 3163 to 3219), so nothing this TZ writes can pause the reward book. **`7,800,000,000` at the start of every mode that reads the store, a Release or the set** (`DISK_GATE`, line 166; `floor_check`, lines 523 to 537): that floor and `400,000,000` for what the session may still write then. **`8,200,000,000` at the host gate:** that gate and `400,000,000` more, so that a host on which the run could not reach its pack stops before anything is written. **What the session writes:** the worktree's checkout, about `15,300,000` bytes — `5192aff`'s tracked files, `14,648,863`, with this file and the instrument; the fetch records and polls of five member days, about `29,000,000` — `5,800,000` a day in the Architect's stand-in, a poll's line now carrying its row's terms; the day files, about `2,700,000` — nine variants where TZ-43's held three; one unit's download at a time, removed as the unit ends, `100,000,000` at the reward book's cut and `31,823,974` at the heaviest slot of the eight days read; the rehearsal's four assets, `47,329,972`, which come and go before `fetch`; the day archives, about `16,300,000` a candidate day — what TZ-33's day writes outside its streams (map §2.6) — `130,400,000` at the walk's eight; the logs; **and in §9 only the files the report names by hash that the Release does not hold** (map §7 item 167) — the logs and the state, a few megabytes. About `300,000,000` bytes at the session's peak. TZ-44 read `9,410,662,400` bytes free at its close (map §7 item 167), and free space falls about `43,000,000` a day beside the streams.

**Memory.** `MemAvailable` at least **`172,658,448`** bytes (`MEM_FLOOR`, line 160) — twice `86,329,224`, the host peak modelled from `72,000,000` at the ratio TZ-37 measured between the host's peak and the Architect's for one code, `58,953,728 / 49,168,384` (map §6, memory; §7 items 131 and 156). **`72,000,000` is the Architect's bound on any mode's peak under Python 3.12.3, set above the largest his runs of these bytes gave** (§6): `fetch` `69,021,696` over six candidates, five of them members; `replay` `54,747,136` over five days in one process; `rehearse` `53,673,984`; `rescore` `52,715,520`; `selftest` `47,886,336` to `48,074,752`, three direct runs; `score` `46,907,392` and `47,050,752`; and `upload` `41,533,440`, `verify` `41,357,312`, `pack` `41,246,720`, `still` `40,812,544`, `fingerprint` `40,747,008`, `reclaim` `40,652,800` and `archive` `40,620,032` at most — every mode but `selftest` under the stand-in's wrapper (§6). The replay holds one day at a time and reads a day's polls from its file one line at a time; `fetch` holds one day's polls at a time; `pack` reads a file of replies a line at a time and streams each member into its archive; `upload` streams each asset from its file and `verify` hashes each download as it arrives. The host's `MemAvailable` read `217,313,280` bytes at TZ-43's `fetch` and `239,050,752` at TZ-44's `pack`, each with its session open, and `380,186,624` and `454,987,776` at TZ-44's two host gates (their reports). **Every mode that reads the store, a Release or the set reads `MemAvailable` and free space at its start** (`floor_check`, lines 523 to 537; `memory_gate`, lines 516 to 520): a memory read below the floor is read again every 60 s, five reads at most, the first at or above it passing and five below it BLOCKING; free space below `7,800,000,000` BLOCKS; and glibc's mmap threshold and arena count are asserted taken (lines 77 to 83). Every mode prints its peak on every exit (§5), and runs under `nice -n 19`: the host has one processor (map §6).

### 0.5 Refs and the number

`I0 number`, into `logs/05-number.log`, and `git -C /root/btc-5m-twap ls-remote origin`, into `logs/05-refs.log`, after §0.4, every ref reported; both again in §3.1 — `I0 number` after its fetch, `git ls-remote origin` before its push. **The Architect read 151 ref lines on 2026-11-15 at 05:24 UTC:** `HEAD` and `refs/heads/main` at `5192aff`, PR #44's merge, above `56d343b`, revision `2026-11-13-a`; twenty `tz-*` branches; forty-three pull heads and no merge ref — no pull request open; fifty-four `pairbook-streams-*` and twenty-seven `rewardbook-streams-*` tags, the last `rewardbook-streams-1794706220`, the calendar's run of 2026-11-15, after `rewardbook-streams-1794638496`, a run off the calendar at 06:41:36 UTC on 2026-11-14; the lightweight `tz-44-l0-inputs`; and the two annotated tags with their peeled lines. Every run of either archive that takes a new set adds one tag, at 01:30:20 and 03:00:20 UTC, and each possibly 1,800 s and 600 s after a start of its timer (map §2.5, §2.6; §7 items 115, 129 and 166). Every commit on `main`'s first-parent line above `5192aff` is reported with the paths it changed, the upload that carries this TZ among them. A difference is recorded, not BLOCKING, unless `refs/heads/tz-45-l0-rule-w` or `refs/tags/tz-45-l0-rule-w-inputs` already exists — either is BLOCKED; a `main` that does not carry revision `2026-11-13-a` is §0.2's BLOCK.

**NUMBER — CANON hard rule 2.** `I0 number` reads, in the primary checkout, `git ls-tree --name-only origin/main -- CryptoTZ/ CryptoReports/` and must print `NUMBER PASS - 2 of 2`: `CryptoTZ/` holds `TZ-45-l0-rule-w.md` and no other file whose name begins with `TZ-45-`, and `CryptoReports/` no report whose name does (`number_reading` and `mode_number`, lines 2973 to 2978 and lines 2981 to 2988). Anything else is BLOCKED, here and in §3.1 alike. Map §2.6 and §7 item 164 gave this work the number 45, the next free: `CryptoTZ/` and `CryptoReports/` end at TZ-44's files.

---

## 1. Why this TZ exists

Line numbers here are Appendix A's unless a file is named.

**The question** — CANON PART II, the L track, L0's second rule: does a second quoting rule, explored on the eight days already read and fixed before any later day is read, earn under both brackets on days no one has read? L0's first rule — a quote alone one tick inside a touch at least five ticks wide — read UNDECIDABLE (TZ-43): with every assumption against it the quote was paid `588` pUSD of reward over eight days and lost `634` at its marks, and with every assumption for it `3,388`; what separated the two was the competitors' score, which no stream shows (CANON §1.5). No further day of the same replay could decide that rule (map §7 item 153). TZ-44 put L0's inputs in a Release, the Architect re-derived its money from them (map §2.6; §7 item 162), and then read where the first rule is paid and where it only takes fills (map §2.6; §7 item 164).

**What the eight days showed — an exploration, in sample, barred from every gate** (CANON PART VI; map §2.6). The first rule speaks only where the touch is five ticks wide and one tick inside it is in the reward band, a median of `0.06` h of a market-day. **Where the touch is wider than the band it is silent, no displayed order scores, and the venue's own figure for the competitors' score is near zero: a pool is offered and no one takes it.** A quote placed there, inside the band and well inside the touch, is alone at its prices, and its share of the pool does not hang on what the competitors score. Rule W is that quote, with two bounds the eight days chose: markets whose minimum size is 20 shares or less — larger clips added nothing and lost on some days — and prices no more than `0.10` inside the touch.

**And the venue moves a market's terms inside a day — measured by the Architect on the same eight days on 2026-11-15, before this rule was fixed: the measurement map §7 item 155 asks for.** Every served poll's row carries the market's minimum size and maximum spread as the venue holds them at that instant, and a member is polled every 300 s. Of L0's 1,200 member-days, on **292** a served poll carried another minimum size or maximum spread than the day's selection, read at 23:45 UTC the evening before — `41,080` of the `345,595` served polls — and of the **437** member-days whose selection read 20 shares or less, on **156**, 133 of them later than the day's first hour: on 154 the venue raised the minimum size — to 50 shares on 106, to 40 or 60 on 45 [exploration]. **An order under the minimum size scores nothing.** A replay that holds the selection's terms all day — TZ-43's did, and so did the exploration map §2.6 records — credits such an order a reward the venue does not pay. Rule W therefore reads the row's own terms at every poll (item 1), and the replay credits a market accordingly (the reward, below). TZ-43's reading is not re-opened by this: its `pess` was overpaid by it, and UNDECIDABLE admitted nothing.

**Rule W, ours, fixed here before any stream, selection, slot record or poll of a day from 2026-11-09 has been read by anyone** (`w_targets`, lines 949 to 961; `Day.decide`, lines 1394 to 1467; `Day.poll`, lines 1497 to 1533). On each member market of a day, on its first token's book, from the day's first instant to its last. `tick` is the market's tick size, `v` its maximum spread and `m` its minimum size, as the day's selection gives them; `b` and `a` are the best bid and the best ask the book displays, at any size.

1. **Which markets, and when.** A member whose minimum size is **at most 20 shares** and whose maximum spread and minimum size are above zero, **while every served reward poll of that market on that day has carried a row with the selection's own minimum size and maximum spread, and the last of them a `market_competitiveness` of at most `1`**. Before the day's first served poll, and after a served poll whose page holds no row until the next that holds one, there is no quote. **From the first served poll whose row carries another minimum size or maximum spread — or states either as no number — to the day's end there is none either:** the venue has moved the market's terms, the quote is not sized for them, and the rule does not return to that market that day, whatever a later row says.
2. **The width.** `w` is the largest multiple of `tick` that is at most **`0.9` of `2v`**: `8` cents under a maximum spread of `4.5` cents on a tick of one cent, `8.1` cents on a tick of a tenth of a cent. No quote where `w` is under one tick.
3. **Where.** Where `a − b` is at least **`w + 2·tick`**: a bid at `(a + b − w) / 2` **floored to a multiple of `tick`**, and an ask `w` above the bid, each of `m` shares, at prices strictly between `0` and `1`. Each then stands at least one tick inside the touch, alone at its price unless an order joins it later; the two are `w` apart, so each scores `((v − w/2) / v)²` a share against a midpoint the two themselves set, `0.01` or more of a full share.
4. **How far inside.** **No quote on either side unless both prices stand at most `0.10` inside the touch** — the bid at most `0.10` above `b` and the ask at most `0.10` below `a`.
5. **The position:** no bid while the position the host knows of is `m` long or more, no ask while it is `m` short or more — TZ-43's cap, one minimum size.
6. **Otherwise nothing:** a live quote whose target is gone is cancelled; one whose price is no longer the target is cancelled and a new one sent at the target, the same instant; a quote the host has learned is filled, cancelled or refused, or partly filled below `m`, is replaced at the next decision. **A decision is made after every frame of the market the host receives, at each slot's first instant, after a seed — and at the host instant of every served reward poll of the market**, the one decision TZ-43's rule did not make, because this rule reads the poll.
7. **Post-only**, a refusal where the order would cross when it arrives; **a disconnect** — a close of the stream other than a slot's end — cancels every live quote at the host's instant. Both are TZ-43's.

By hand, in thousandths (`w_targets`, and the self-test's two checks of it): a touch of `0.30` to `0.42` under `v = 0.045` gives `0.32` and `0.40`; `0.30` to `0.40`, the narrowest that leaves room, `0.31` and `0.39`; `0.30` to `0.399` none; `0.30` to `0.43` gives `0.32` and `0.40`, the bid floored; `0.15` to `0.42` gives `0.24` and `0.32`, the ask exactly `0.10` inside; `0.15` to `0.44` none, the ask `0.11` inside; and on a tick of `0.001`, `0.305` to `0.42` gives `0.322` and `0.403`.

**The replay is TZ-43's, unchanged** (TZ-43 §1; `Day`, lines 1108 to 1795): each line's `recv_ns` the host's clock and each frame's `timestamp` the venue's; a latency of `L = 50` ms one way; no taker delay; the book seeded by each subscription's `book` frame of the first token and moved by every `price_change` entry, every later `book` frame compared with the book rebuilt to it (G-BOOK); a slot's files joined at the slot's instant; a match where a block of entries is closed by the token's own `book` frame of the same stamp, a resting order filled where the sweep reaches its price beyond the size queued ahead of it; an order joining behind the size displayed at its level; and a crossing order where the opposite side comes to a resting order's price with no match. **The reward is TZ-43's**, the venue's published formula taken as the time-average of our share over the day: the midpoint of the best bid and ask among the displayed levels of at least the minimum size and our own orders; our score; the competitors' bracketed between the most and the least the displayed levels can score under any split among makers, with the venue's own figure — each poll's `market_competitiveness` times its daily rate — beside them; the rate the selection's, then each served poll's; the `1`-pUSD minimum. **One thing is added, because the venue's terms move between two polls at an instant no stream shows** (`Day.poll` and `Day.finish`, lines 1497 to 1533 and lines 1760 to 1795): a market's reward stops at the poll whose row shows its terms moved; and the four `pess` variants and `central` are credited only through the last served poll whose row confirmed the selection's terms — what a market accrued after that poll and before a page with no row, a row of other terms or the day's end is given back — while the four `opt` variants keep it. A member is polled every 300 s, so each such poll costs a market's `pess` reward about 300 s, and more where a poll before it was not served. **The rebate and the marks are TZ-43's**: a fee-enabled member's `rate` times `rebateRate` times `C·p·(1 − p)` a fill; a position valued at the day's end at its market's outcome where its document states one, else at the day's last midpoint — **a proxy, named so wherever it is used** — else by liquidation into the book. Positions start at zero each day. **The engine's lines that differ from TZ-43's committed instrument are rule W's, the poll's decision, the terms a poll's row carries with the credit they govern, and the adverse hit, and nothing else** (§5; §10, C3): under TZ-43's own rule this instrument prints TZ-43's lines, byte for byte (§4.1).

**The brackets — every corner, because this rule's money is not ordered by them.** What the stream cannot show is where in a level's queue our order stands, whether an order that came to ours was a taker, and the competitors' true score. TZ-43 gated two variants, `pess` and `opt`, as the least and the most. **For rule W they are neither:** on the eight days read, a quote never met by a crossing order earned `30` USDC less than one met by them on 2026-11-02 and `5` to `132` more on the other seven — a crossing order that fills us can end a position that would otherwise hold one side of the quote out all day, and outside `[0.10, 0.90]` a one-sided quote scores nothing [exploration]. The reward alone is ordered: it falls as the competitors' score rises. So the queue place and the crossing orders are taken at both values under each end of the competitors' score, **nine variants of one rule on the same frames** (line 129 to line 139):

| variant | queue | crossing orders | competitors | 1-pUSD minimum | rebate | role |
|---|---|---|---|---|---|---|
| **`pess-bt`** | behind the displayed size | takers | the larger of the book's most and the venue's figure | per member-day | none | **gated for EARN, the four together** — TZ-43's `pess` |
| **`pess-br`** | behind | refused, never takers | the same | per member-day | none | |
| **`pess-ft`** | first at its level | takers | the same | per member-day | none | |
| **`pess-fr`** | first | refused | the same | per member-day | none | |
| **`opt-bt`** | behind | takers | the smaller of the book's least and the venue's figure | per day | counted | **gated for NO EARN, the four together** |
| **`opt-br`** | behind | refused | the same | per day | counted | |
| **`opt-ft`** | first | takers | the same | per day | counted | |
| **`opt-fr`** | first | refused | the same | per day | counted | TZ-43's `opt` |
| `central` | behind | takers | the venue's figure | per member-day | counted | barred |

Before a member's first poll the venue's figure is absent — and rule W does not quote. The credit through the last confirming poll is the `pess` variants' and `central`'s; the `opt` variants keep what a market accrued up to the poll that ends it (the reward, above).

**The adverse hit — what the replay cannot see, charged to the EARN side.** A quote placed inside a wide touch may be sold into, or bought from, by a taker who showed no order while it was absent, and no stream holds that order (map §7 item 164). Each of the four `pess` variants is charged, on every market-day in which it set a target at all, **one fill of the market's minimum size at the largest distance any of its targets stood inside the touch that day** — the bid's above `b` or the ask's below `a`, at the decision that set or kept it: at most `0.10` a share, `2` USDC a market-day at 20 shares (`hit_d` and `hit`, lines 1760 to 1795; `day_money`, lines 2291 to 2316). The `opt` variants and `central` are charged nothing, and print the figure all the same. **A hit that also ends the market's reward for the day is charged by nothing here**, and neither is a second hit: that is L1's to measure.

**The set** (`mode_fetch`, lines 1978 to 2040; `day_verdict`, lines 1834 to 1860; `slot_problem`, lines 738 to 777) — TZ-43's rule, from the reserve's first day. The candidates are the UTC days from **2026-11-09**, `1794182400`, in order. A candidate is a **member** where the reward book's store holds its selection — the first attempt whose record reads `ok`, its replies' SHA-256 the record's — of at least one market, and each of its **96 slots** qualifies: the slot's records consecutive from `k = 0`, each of that selection and its member count, no error, its stream opened and not cut, its file named by the record; the first subscribed by `S` and not joined late; the last's last frame at or after `S + 900`; no gap above 15 s within a file or between two; and every stream file among the assets of a complete run of the reward book's archive, by its name. **The members are the first 5**; the walk stops BLOCKED past 3 non-members before the fifth — at 2026-11-16 — and every candidate is disclosed in order with its reason. Each member's polls are the served replies of its 96 slots' reward files, in the order received; its markets, minimum sizes, maximum spreads, rates and fee schedules are its own selection's, so a parameter that moved between days moves with its day (map §7 item 155).

**The test — five days, each a block.** A day's money for a variant is its total over the day's members: the reward paid, the rebate where it is counted and the marks. A day's **least** is the smallest, over the four `pess` variants, of that money less the variant's adverse hits; its **most** is the largest over the four `opt` variants. **EARN** where the least reaches **`θ = 10` USDC on every one of the 5 days**; **NO EARN** where the most stays below `θ` on every one; **UNDECIDABLE** otherwise, and where both hold (`day_brackets`, lines 2333 to 2336; `l0_reading`, lines 2319 to 2326). Under independent days, a rule whose day's least reaches `θ` with probability at most `1/2` reads EARN with probability at most **`2⁻⁵ = 0.03125`**, and one whose day's most reaches it with probability at least `1/2` reads NO EARN with at most the same — the sign test of TZ-30's B3 on day-blocks, exact under that assumption. **The assumption is named, not measured:** the days share markets, so they are less independent than the test takes them to be, and `0.03125` is the figure's best case. **Five days, where L0 took eight, are accepted for one reason** (map §2.6): an EARN here opens a step whose whole loss is fixed in its own TZ, and nothing more. **Power**, printed before any money is read: EARN's is `q⁵` where each day's least reaches `θ` with probability `q` — `0.590490` at `0.90`, `0.773781` at `0.95`, `0.950990` at `0.99`. `θ` is TZ-30's and TZ-43's.

**What a reading establishes, and what it does not.** EARN says that on 5 days no one had read, rule W's quotes — at every corner of the queue place and the crossing orders, the competitors at the most the book or the venue allows, the reward unpaid on any member-day under `1` and counted only through the last poll that confirmed the market's terms, no rebate, and one adverse fill charged in every market quoted — kept at least `10` USDC a day, positions marked to each market's midpoint at the day's end. **It proves no income.** The replay holds the book fixed while our quote stands in it; it does not see the taker our own quote calls out, the venue's actual sampling, or its payouts; and its reward rests on the venue's formula as published and on its competitiveness figure as the Architect read it (CANON §1.7). Those are measured by one thing only, the venue's payouts to an address of ours against this replay's reward for the same markets and days: **L1**, rule W live at the minimum size from an address the venue does not restrict (map §6, venue geoblock; §7 item 163), with a loss limit fixed in its TZ. NO EARN says that even at the best corner, the competitors at the least, the quote kept under `10` USDC a day. UNDECIDABLE closes nothing and admits nothing, and L1 does not open (CANON PART II). None speaks of another rule, size, latency or market.

**Exploration — on the eight days already read, by this instrument's own code, barred from every gate and cited in support of nothing** (CANON PART VI). On 2026-11-15 the Architect replayed the eight member days of L0 — 2026-10-31 to 2026-11-05, 2026-11-07 and 2026-11-08, the 768 stream assets downloaded anonymously, each day's members and polls read by Appendix A's own code from the day archives of the Release `tz-44-l0-inputs`, every poll with its row's own terms, and equal to TZ-43's published files in every member and in every poll's instant, market, rate and figure, `345,595` of `345,595` — with the engine of Appendix A under the nine variants:

| | 10-31 | 11-01 | 11-02 | 11-03 | 11-04 | 11-05 | 11-07 | 11-08 |
|---|---|---|---|---|---|---|---|---|
| `pess-bt`, money | `585.9` | `279.8` | `180.5` | `85.6` | `157.2` | `251.1` | `112.7` | `69.6` |
| `pess-br`, money | `597.0` | `411.3` | `150.9` | `117.6` | `181.4` | `263.5` | `118.2` | `79.5` |
| **the day's least**, hits charged | **`514.2`** | **`184.6`** | **`94.3`** | **`25.1`** | **`59.7`** | **`210.6`** | **`68.8`** | **`43.2`** |
| **the day's most** | **`606.1`** | **`427.6`** | **`191.0`** | **`127.3`** | **`202.1`** | **`269.6`** | **`123.2`** | **`84.5`** |
| markets whose terms moved, of 150 | `23` | `31` | `32` | `30` | `54` | `32` | `34` | `56` |

`pess-bt` took `436` fills, was paid `1,788` pUSD of the `1,813` it was credited, lost `66` USDC at its marks and was charged `492` of hits over `295` market-days quoted; the queue place moved no day's money by more than `2`; the least is `pess-bt`'s on seven days and `pess-br`'s on 2026-11-02, the most `opt-fr`'s on seven and `opt-ft`'s on that day. **With each market's terms held at its selection's all day, the same engine gave `pess-bt` `597.3 285.7 213.0 87.1 194.7 263.7 183.7 165.5`** — map §2.6's own `597 285 213 87 191 263 184 165`, the earlier session's patched copy of TZ-43's engine, within `3.7` USDC on one day and `1.5` on the rest: reading the terms at every poll takes `2` to `96` USDC off a day, `71` and `96` off the last two, and those were never the venue's to pay. **None of these numbers supports anything: they chose a rule and the form of its gate, and both are gated on days no one has read.** The four assets of G-REHEARSAL are 2026-10-29's (§4.1), read by TZ-43 and by the Architect before.

**What the Architect has not read:** no stream asset, selection, slot record or poll of any day from 2026-11-09, and no Release listing of a run of the archive after 2026-11-10 but the tags' names on `origin` (§0.5).

**When.** The archive moves each day's streams at 01:30:20 UTC the next day (map §2.6). The run begins from 2026-11-15 07:30:00 UTC, inside a band of 07:30 to 21:00 UTC, and only once §0.0's read finds five whole days; `fetch` then waits for the archive's assets to reach each candidate's last slot, re-reading its ledger every 60 s, and stops BLOCKED `10,800` s after its start (`wait_archive`, lines 1814 to 1831). One stall in the nine candidates of L0 makes about one day in nine a non-member [modelled, on one event]: all five of 2026-11-09 to 2026-11-13 are whole with probability about `0.55`, five of the first six about `0.86` and five of the first seven about `0.97` [modelled, days independent] — which is why §0.0 reads before it begins, and a day short begins nothing, costs nothing and is tried again the next day.

---

## 2. Scope

**Repository paths this TZ may write, and no others:**

1. `research/tz45-l0-rule-w.py` — new, byte for byte Appendix A's, on the branch `tz-45-l0-rule-w`, then a pull request. Not merged by the Executor.
2. `CryptoReports/TZ-45-l0-rule-w-report.md` — straight to `main`, in one commit. **The one path pushed to `main`, and the exemption to item 9 below.**

**Host paths this TZ may write:** `/root/tz45-work/**`; `/root/btc-forensics/`, by exclusive create only (§9); and in the primary checkout `/root/btc-5m-twap`, its `.git` for the branch and the worktree, and its `CryptoReports/` for the report. **Host paths it removes, under §3.3 and §9 and nothing else:** `/root/tz45-work/` with its worktree, and the directories `I scratch` names earlier.

**Remote objects it creates:** the branch `tz-45-l0-rule-w` and its pull request; **and, by B-UPLOAD alone, the Release on the lightweight tag `tz-45-l0-rule-w-inputs` at the instrument's commit, published and not the latest, with its assets** (§3.11). **The named exemption to items 3 and 10 below:** the assets carry the candidate days' selections, slot records and polls and this run's work files — prices, sizes, rates, competitiveness, fills and outcomes among them — because publishing a reading's inputs is CANON hard rule 16; the reserve on those days ends with this TZ's reading.

**Prohibited, each absolutely:**

1. No committed file is modified; every `frozen` row of map §0 is byte-identical at run end.
2. **Nothing under `/var/lib/btc-recorder/`, `/var/lib/btc-chainbook/`, `/var/lib/btc-pairbook/`, `/var/lib/adv3-bot/` or `/etc/adv3-bot/` is opened, listed or written** — the instrument's audit hook refuses every open and listing there (`policy`, lines 304 to 356); the Executor's own commands touch the recorder's root with `df`, in §0.3, §3.14 and §9, and with §0.3's `find` and `grep -c`, and the pair book's with §0.3's `du -sb`, and nothing else.
3. **Under `/var/lib/btc-rewardbook/` nothing is written, and nothing is opened or listed but: by §0.0's read, a candidate day's `<S>.<k>.slot.json`; by `I fetch`, for reading, a candidate day's directory `<D0>/`, `D0` from `1794182400` to `1794787200` — its listing, its `select.<a>.json` and `select.<a>.replies.jsonl.gz`, and its `<S>.<k>.slot.json` and `<S>.<k>.rewards.jsonl.gz`; and by `I pack`, for reading, the same files of the days `fetch` considered and of no other** (`store_day`, lines 298 to 301) — the named exemptions, and the reserve's end for those days (map §2.6): this TZ is the gate the reserve was kept for. **No stream file stored there is opened by anything; no file of the store's root is opened; no day before `1794182400` and no day the walk did not reach is opened or listed.** `du -sb`, in §0.3 and §3.14, walks the store and prints one sum.
4. **Under `/var/lib/btc-rewardbook-archive/` nothing is written or listed; `ledger.jsonl` is opened for reading by `I archive`, `I fetch` and `I still`, and every complete run's `runs/<A>/set.json` by `I archive` and `I fetch`. Under `/var/lib/btc-pairbook-archive/` nothing is written or listed, and `ledger.jsonl` is opened by `I still` alone** — the named exemptions; nothing else in either is touched but by §0.3's `stat` and `du -sb`.
5. **No credential is printed, written or read by the Executor:** never `git remote get-url`, `git config --get-regexp url`, `gh auth token` or `gh auth status --show-token`, and never the advisor's token. B-UPLOAD's instrument reads the repository's credential in the Boss's shell and prints its source alone (TZ-27's `credential`).
6. **The host's public address is never printed, written or published:** no command asks any service for it, and **no stored reply's body leaves the host but a JSON document the venue served under status 200** — a file of replies holding any other body is in no archive (§3.10; `body_reason` and `withhold_reason`, lines 2576 to 2593 and lines 2595 to 2613).
7. **No unit is signalled, started, stopped, enabled, disabled, reloaded or changed**, and nothing under `/etc/systemd/` is touched. `systemctl show`, `is-active`, `is-enabled` and `list-timers` and `journalctl` are this TZ's only reads of a unit and of systemd.
8. **Requests.** `gamma-api.polymarket.com/markets`, with `User-Agent: btc-5m-twap-tz45` and `Accept: application/json`, in `I fetch` alone — the members' documents, once, each request held to the idle stretch (`gamma_get` and `documents`, lines 1914 to 1933 and lines 1950 to 1975). **The reward book archive's Release assets**, from `github.com` and the hosts it redirects a download to, `release-assets.githubusercontent.com` and `objects.githubusercontent.com`, anonymously, with `User-Agent: btc-5m-twap-tz45` and `Accept: application/octet-stream`, in `I rehearse`, `I replay` and `I rescore` alone, each held to the idle stretch (`download` and `run_unit`, lines 2062 to 2093 and lines 2098 to 2132). **GitHub through TZ-27's client alone** — in `I upload`, `api.github.com` and `uploads.github.com` with the credential; in `I verify`, `api.github.com`, `github.com` and the two hosts a download is redirected to, with no credential — every one under `User-Agent: btc-5m-twap-tz27`, `Accept` and `X-GitHub-Api-Version: 2022-11-28`, and held to the idle stretch away from both archives' runs (`Gh45`, lines 2506 to 2547). `git` against `origin`, and `gh` for the pull request and for git's credential alone. **No other request** — no CLOB, no websocket, no Data API, no geoblock read, no authenticated call to the venue — and the hook refuses any other host in every mode (`policy`, lines 304 to 356). GitHub's status page, where §3.5, §3.7 or §3.12 waits on it, is read by the session's own web tool and never by a request from the host (map §7 item 149). **No order is placed, signed or cancelled; no key of any venue is held.**
9. **No Release, tag or asset but this TZ's is created, changed or deleted, and this TZ's only by `I upload`.** Nothing is pushed to `main` but the report; nothing is merged.
10. **No single member's, fill's or poll's price, size, rate, competitiveness or outcome is printed, or written outside `/root/tz45-work/`, the Release and — the named exemption, CANON hard rule 15's — §9's copy in `/root/btc-forensics/` of a file the report names by hash that the Release does not hold**: the instrument prints sums over a day or a set, and the report quotes them. **This binds the Executor's own reads as strictly as the instrument** (map §7 item 118): no file under `/root/tz45-work/fetch/`, `/root/tz45-work/days/`, `/root/tz45-work/dl/` or `/root/tz45-work/out/`, nor `set.json`, `reading.json`, `rehearsal-base.txt`, `rehearsal-w.txt` or `rescore.txt`, is printed, whole or in part, by any command but the instrument's modes and `sha256sum`, `stat`, `ls -la`, `wc -l` and `du`, which print hashes, sizes and counts — no `cat`, `head`, `less`, `zcat`, `tar -x`, `tar -t`, `jq` or `python -c` on one; the timing files carry slots, seconds and bytes and may be printed, and so may `state.json`, `read-ledger.jsonl`, `release-set.json`, `upload.jsonl`, `transfers.jsonl`, `verify.json` and every file under `logs/`.
11. `/root/tz04a-env/`, `/root/tz01-env/` and the code trees `/root/btc-recorder-svc/`, `/root/btc-pairbook-svc/`, `/root/btc-pairbook-archive-svc/`, `/root/btc-rewardbook-svc/`, `/root/btc-rewardbook-archive-svc/` and `/root/adv3-bot-svc/` are not modified — §0.3 reads `commit.txt` of the last and nothing else of them; `/root/btc-forensics/` is written only by §9's exclusive create, and nothing in it is removed.
12. **No stream asset is downloaded but a member day's and the rehearsal's four**, and none is read but by the instrument's replay, in its unit, before its removal. Nothing is removed from the reward book's store, and from a Release nothing but an asset of this TZ's own that `I upload` replaces (§3.11). No dataset, archive or binary enters git history.

---

## 3. The work, in this order

Every command's output goes to `logs/`, one file per step under the names below, and is quoted in the report; a step run again appends to its own log under a `date -u` line. **B-RECLAIM-SCRATCH runs inside §3.3 and holds back nothing after it — no later step reads what it removes (map §7 item 140); B-RECLAIM-OWN runs last (§9).** On a BLOCK before §3.1, B-RECLAIM-OWN runs with `I0` in place of `I` and without its `git worktree remove` line; on a BLOCK or a FAIL after it, the run goes to §3.14 and §9, skipping every step that needs a PASS it lacks.

| step | logs |
|---|---|
| §0.0 to §0.5 | `00-instant.log`, `00-ready.log`, `01-stage.log`, `02-fingerprint.log`, `03-host-gate.log`, `05-number.log`, `05-refs.log` |
| §3.1 | `10-number.log`, `11-worktree.log`, `12-fingerprint.log`, `13-push.log`, `14-pr.log` |
| §3.2 | `20-selftest.log` |
| §3.3 | `30-still.log`, `31-scratch.log`, `32-reclaim-scratch.log` |
| §3.4 | `40-archive.log` |
| §3.5 | `50-rehearse.log` |
| §3.6 | `60-fetch.log` |
| §3.7 | `70-replay.log`, `71-replay-again.log` |
| §3.8 | `75-rescore.log` |
| §3.9 | `80-score.log`, `81-score-again.log` |
| §3.10 | `82-pack.log`, `83-pack-again.log` |
| §3.11 | `85-upload.log`, written by the Boss's paste; `86-upload-wait.log`, the Executor's reads of it |
| §3.12 | `88-verify.log` |
| §3.13 | `95-still.log` |
| §3.14 | `96-host-gate-again.log`, `97-archive-again.log`, `98-closing.log`, `99-selfcheck.log` |

**Where the session's permission classifier refuses a command of a block named B-…**, the Executor tries the block once and hands the Boss its paste, unchanged, once, in plain words (CANON hard rule 14; map §6, sandbox limit — destructive actions; §7 items 124 and 138); the Boss runs it verbatim in a root shell on the VPS, every step chained to the one before it and appended to its log under a `date -u` line, and the Executor verifies it from that log and through the reads this TZ names — never from the Boss's account — and runs no step of the paste again (map §7 item 144). **B-UPLOAD is the Boss's by its own text and is not tried by the Executor** (§3.11).

### 3.1 The branch and its file

```
git -C /root/btc-5m-twap fetch origin
I0 number
git -C /root/btc-5m-twap worktree add -b tz-45-l0-rule-w /root/tz45-work/wt origin/main
```

Into `10-number.log` the fetch and `I0 number`, which must print `NUMBER PASS - 2 of 2` again (§0.5), or BLOCKED; into `11-worktree.log` the worktree and §0.1's script again, verbatim but for its argument, `/root/tz45-work/wt` — it writes the instrument and finds TZ-27's file there already, from `origin/main`, and must print the same two lines of lines, bytes and SHA-256 as at §0.1; into `12-fingerprint.log` `I fingerprint`, which must print `FINGERPRINT PASS` again, from the worktree's file. Into `13-push.log`: commit the one file alone on the branch, `research/tz45-l0-rule-w.py`; `git -C /root/btc-5m-twap ls-remote origin` (§0.5); push with `git -C /root/tz45-work/wt push -u origin tz-45-l0-rule-w` — through `credential.helper=!gh auth git-credential` where the URL's credential is refused (map §6, git remote) — then:

```
date -u +%FT%T.%NZ; git -C /root/tz45-work/wt ls-remote origin refs/heads/tz-45-l0-rule-w
git -C /root/tz45-work/wt rev-parse HEAD
```

— the instant the commit is on `origin`, and its hash there, which must be the worktree's `HEAD`; into `14-pr.log` the pull request against `main`, opened with `gh pr create`. A failed assert or a non-zero exit here is BLOCKED. **The commit on `origin` comes before any stream, selection or poll of the set is read:** every mode that reads the store, a Release or the set writes the worktree's `HEAD` and its own SHA-256 into `read-ledger.jsonl` (`read_ledger`, lines 3222 to 3231), **and the Release's tag is made at this commit** (§3.11), which `pack` and `upload` assert (lines 2868 to 2937 and lines 2717 to 2749).

### 3.2 The self-test

`I selftest`, into `20-selftest.log`, must print `SELFTEST PASS: 71 checks`. It reaches no network but listeners of its own on `127.0.0.1` — a download server, and TZ-27's own stand-in for GitHub, `_FakeGitHub` — and runs on literals, on two synthetic days of two slots and on temporary trees under `/root/tz45-work/selftest-tmp/`, which it removes (`mode_selftest`, lines 3473 to 4222). It proves TZ-43's rule on TZ-43's synthetic day against TZ-43's own reference; rule W's two prices by hand, and rule W on its own synthetic day against the Architect's second implementation and by hand — the poll's decision, the position cap, a crossing order met and refused, the bound on how far inside the touch, the adverse hit, a row of other terms ending a market's quote for the day and the credit through the last poll that confirmed them; a poll's row read with its own terms; the day's money with its hits and the reading; the set's and the store's rules; the hook's every decision this TZ relies on; a day's archive built from two trees and once again to the same bytes, every member verbatim and every stream and stray name left out, a stored reply's body judged and a file of replies withheld by its line; G-SOURCE on a synthetic tree; and the whole request path — the Release created on the tag at the commit, three assets uploaded, every one proved by the API's record and a full anonymous download, a second upload holding all three, a changed byte served read as a failed download. A red self-test stops the run here, and it goes to §3.14 and §9.

### 3.3 The units, the directories beside this session, and B-RECLAIM-SCRATCH

`I still`, into `30-still.log`, records the recorder's, the pair book's, the reward book's and the advisor's `MainPID`, `NRestarts` and `ActiveState` in `state.json`, with the instant, and prints their `MemoryCurrent` and `MemoryPeak` and both archives' units' states (`mode_still`, lines 3012 to 3037). Then `I scratch "$(dirname "$S")"`, into `31-scratch.log`, lists every UUID directory beside this session's own and names each **live** — born from 1 s before to 60 s after the start of a running process whose `argv[0]` is `claude` or ends in `/claude.exe` — or **earlier** (`mode_scratch`, lines 3066 to 3078). Map §3 expects TZ-44's session's own, unless a reboot of the host emptied `/tmp`. **The rule alone decides:** every directory `scratch` names earlier is reclaimed, whatever a map or a report said of it before (map §7 item 150).

**B-RECLAIM-SCRATCH**, for every directory `I scratch` names **earlier** — none it named live, and never this session's own — into `32-reclaim-scratch.log`:

```
cd /root/tz45-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz45-work/wt/research/tz45-l0-rule-w.py reclaim <each earlier directory, by its full path>
rm -rf <one such directory>; echo "exit=$?"
test -e <that directory>; echo "exit=$?"
```

One `reclaim` names every earlier directory and must print `RECLAIM PASS` before any removal; then one `rm -rf` and one `test -e` a directory, the last reading `exit=1`. `reclaim` refuses a directory born from 1 s before to 60 s after a running claude process started, and any path but `/root/tz45-work` that is not a UUID directory under `/tmp/` whose parent's name carries `btc-5m-twap` (`reclaimable`, lines 3146 to 3151; `mode_reclaim`, lines 3163 to 3219). If `I scratch` names none earlier, the block is recorded as empty and skipped. **Its paste**, where the classifier refuses it (map §7 item 152) — the Executor writes in every earlier directory's full path, one `rm -rf` and one `test -e` a directory, all chained to the `reclaim`'s `exit=0`, which it reaches only after `RECLAIM PASS`:

```
{ date -u +%FT%T.%NZ; (cd /root/tz45-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz45-work/wt/research/tz45-l0-rule-w.py reclaim <D1> <D2>); echo "exit=$?"; } >> /root/tz45-work/logs/32-reclaim-scratch.log 2>&1 && tail -n 1 /root/tz45-work/logs/32-reclaim-scratch.log | grep -qx 'exit=0' && { date -u +%FT%T.%NZ; rm -rf <D1>; echo "exit=$?"; test -e <D1>; echo "exit=$?"; rm -rf <D2>; echo "exit=$?"; test -e <D2>; echo "exit=$?"; } >> /root/tz45-work/logs/32-reclaim-scratch.log 2>&1
```

**It holds back nothing of §3.4 to §3.14**, which read none of what it removes: the Executor goes on while the paste waits for the Boss.

### 3.4 The archive's record

`I archive`, into `40-archive.log`: the reward book archive's two units by `systemctl show`; its `ledger.jsonl` read whole, its size and SHA-256, every complete record printed with its UTC stamp; every run summarized — on the calendar or off it, its set, its deferrals and its terminal record; every complete run's `set.json` asserted by the SHA-256 its set record carries, with its files, bytes and slots; the slots the assets reach, at and after `1794182400`; the tags `origin` carries beside the sets; whether the archive is halted; and **the rehearsal's four assets in the set of `rewardbook-streams-1793263627` by name, bytes and SHA-256**, or BLOCKED (`mode_archive`, lines 3081 to 3119). The rest is printed facts and gates nothing: the report sets each run off the calendar beside §0.3's reads of systemd's reloads (map §7 items 115, 129 and 166). **It prints, of a day from 2026-11-09, slots, file counts, bytes and hashes alone.**

### 3.5 G-REHEARSAL

`I rehearse`, into `50-rehearse.log`: the four assets downloaded from `rewardbook-streams-1793263627` by the bytes and SHA-256 Appendix A fixes — TZ-34's report's, and §3.4's set's — each held to the idle stretch, replayed twice as one stand-in hour under fixed parameters, removed, and compared (§4.1): **under TZ-43's rule against TZ-43's own lines, and under rule W against the Architect's second implementation.** **A network failure is resumable:** `I rehearse` may be run again twice, each try at least 600 s after the one before, and **the last waits, where GitHub's status page reads an incident of unauthenticated traffic open, until it reads that incident resolved — at most 6 h after the failure before it** — the page read by the session's own web tool, never by a request from the host (§2 item 8; map §7 item 149); a third failure is BLOCKED. A FAIL stops the run here, and it goes to §3.14 and §9.

### 3.6 The set — G-SET

`I fetch`, in the background, its output to `logs/60-fetch.log`, read until it prints `G-SET PASS` or fails (§4.2). For each candidate in order it waits for the archive's assets to reach the day's last slot, then reads the day from the store held to the idle stretch; then the members' documents, each request held. `set.json`, each member's `fetch/<D0>.json` and its polls are written once, and `state.json` records the set's SHA-256. **A network failure is resumable:** `I fetch` may be run again twice, each try at least 600 s after the one before, and a third failure is BLOCKED; a run after `set.json` exists reads nothing and asserts the records unchanged. **A BLOCK at the set reads no stream and computes no money:** the files `fetch` wrote go with the tree in §9, the report names them by their count alone, and the set stays unread (CANON PART VI) — a later TZ walks the same rule from the same day.

### 3.7 The replay — G-BOOK

`I replay`, in the background, its output to `logs/70-replay.log`, read until it prints G-BOOK or fails: every member day, slot by slot, each slot a unit held to the idle stretch, its files downloaded, replayed and removed; after its first 24 units it projects its replays' processor time over the set's bytes and stops BLOCKED above `3,000` s; each day's `days/<D0>.slots.txt` and `days/<D0>.json` written once at its end; then G-BOOK (§4.3). **A network failure is resumable:** the days on disk are kept, a day cut short is replayed again from its first slot, and `I replay` may be run again twice, spaced and waiting as §3.5's tries; a third failure is BLOCKED. Then `I replay` again, into `logs/71-replay-again.log`, which replays nothing and prints G-BOOK again.

### 3.8 The rescore — DETERMINISM

`I rescore`, into `75-rescore.log`: the set's first day's first 24 slots downloaded again and replayed again; their lines must be byte for byte the replay's (§4.4).

### 3.9 The score, twice

`I score`, into `80-score.log`, then `I score` again, into `81-score-again.log`. The first prints the power, G-BOOK, every day's money by variant with its hits, each day's least and most, and the reading, and records `reading.json`'s SHA-256 in `state.json`; the second must print `unchanged` for `reading.json`.

### 3.10 The pack — G-SOURCE, G-PACK, G-RESERVE and DETERMINISM

`I pack`, into `82-pack.log`, then `I pack` again, into `83-pack-again.log` (`mode_pack`, lines 2868 to 2937) — **after §3.9, whatever the reading is**: an EARN's, a NO EARN's and an UNDECIDABLE's inputs leave the host alike. Each run reads the floors and asserts the worktree's `HEAD` is its upstream's; takes the candidate days from `set.json` — every day the walk considered, members and non-members, in order from `1794182400` — and gives the hook those days and no other (`store_day`, lines 298 to 301). Then **G-SOURCE**, one unit held to the idle stretch (`work_sources`, lines 2798 to 2823): the files of this run the reading rests on — `set.json`, `reading.json` and, for each member day, `fetch/<D0>.json`, `fetch/<D0>.polls.jsonl`, `days/<D0>.json` and `days/<D0>.slots.txt`, **22 files at five members** — each a regular file whose SHA-256 is the one this run's own record names: `state.json`'s for the set and the reading, the set's for a day's record, that record's for its polls, the reading's for the day's rows and slot lines. Then **G-PACK**, one unit a day, as TZ-44's: the day directory listed once and every name classified (`list_day` and `classify`, lines 2615 to 2634 and lines 2553 to 2563); the unit held for `30` s and its members' bytes at `500,000` a second (`day_budget`, lines 2572 to 2574); free space read; every file of replies read once, a line at a time, and withheld where a line carries a body the venue did not serve as a JSON document under status `200` (`withhold_reason`, lines 2595 to 2613); and the members kept read whole into the day's archive, `out/rewardbook-inputs-<D0>.tar` (`pack_day`, lines 2636 to 2681); then the manifest, `out/tz45-manifest.json`, and the Release's set, `release-set.json` — the archives, the 22 files, the manifest, in upload order (`set_doc`, lines 2832 to 2845) — and `state.json`'s `pack` record: the commit, the instrument's SHA-256, the set's and the manifest's. **G-RESERVE:** the store opened once a member kept and once a file of replies scanned, listed once a day, and nothing else under it (lines 2868 to 2937). The second run must print every output `unchanged` — the archives, the manifest and `release-set.json` — and `DETERMINISM PASS`. A failed assert is BLOCKED. **The candidate days are closed:** each ended before `fetch` took it, the last writes of a day's directory are its last slot's, 910 s after that slot's start, and the archive's removals of its streams; a name that changes between the two runs changes the manifest, and DETERMINISM fails on it.

### 3.11 B-UPLOAD — the Boss's block

**After §3.10's two PASSES, the Executor hands the Boss this paste, once, and does not run it** — in plain words, in Russian: that it is the upload of the Release, which only his shell may run, because a Release is written with the repository's credential and the session refuses calls that read it (map §6, sandbox limit — network; contract §5.1); that it is one line for a root shell on the VPS; that the terminal shows nothing until the run's last lines and `exit=` appear, some minutes, longer across an archive's run; and that no key is pressed meanwhile:

```
(trap '' HUP; date -u +%FT%T.%NZ; echo "run begun"; (cd /root/tz45-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz45-work/wt/research/tz45-l0-rule-w.py upload); echo "exit=$?") >> /root/tz45-work/logs/85-upload.log 2>&1; tail -n 5 /root/tz45-work/logs/85-upload.log
```

**The paste ignores the end of its login** (map §7 item 124): a connection that drops under it does not end the run, which goes on and writes its `exit=` line all the same.

`I upload` (`mode_upload`, lines 2717 to 2749) reads the floors; asserts the set `pack` wrote, the worktree's `HEAD` the pack's commit, `origin`'s branch at it and every asset's file its set's bytes; reads the credential through TZ-27's `credential` and prints its source alone; finds the Release on `tz-45-l0-rule-w-inputs` or creates it — `tag_name` the tag, `target_commitish` the pack's commit, `draft` `false`, `prerelease` `false`, `make_latest` `"false"` (`Gh45.create_release`, lines 2506 to 2547) — and sends every asset through TZ-27's `upload_set`, which stops where the Release holds an asset outside the set, keeps an asset already matching, removes and sends again one that does not, sends each file at most four times, hashes every byte as it is sent and asserts the Release's record of each. **Every request waits for the pair book's idle stretch and for both archives to be idle and away from their calendar runs** (`quiet` and `hold`, lines 571 to 585 and lines 588 to 599), and is recorded in `transfers.jsonl`; every step of the upload is a line of `upload.jsonl`, the last its completion. It prints the transfers' places in their windows on every exit, and `UPLOAD COMPLETE`.

**The Executor writes the instant of each hand-over into `86-upload-wait.log`, by `date -u +%FT%TZ`, and waits for that run's `exit=` line** with this block, `K` one more than the `exit=` lines `85-upload.log` held at the hand-over — **in the foreground, one run of it at a time, never inside a loop or a background task of the Executor's own, and run again while it prints fewer exit lines than `K`** (map §6, harness; §7 item 165), into the same log. **Every count it prints is read after its last sleep:**

```
K=1; for i in 1 2 3 4 5 6 7 8 9 10; do n=$(grep -c '^exit=' /root/tz45-work/logs/85-upload.log 2>/dev/null); [ "${n:-0}" -ge "$K" ] && break; [ "$i" -lt 10 ] && sleep 60; done; n=$(grep -c '^exit=' /root/tz45-work/logs/85-upload.log 2>/dev/null); b=$(grep -c '^run begun$' /root/tz45-work/logs/85-upload.log 2>/dev/null); p=$(pgrep -fxc '/root/tz04a-env/venv/bin/python -B /root/tz45-work/wt/research/tz45-l0-rule-w.py upload'); date -u +%FT%TZ; echo "exit lines ${n:-0} of $K; runs begun ${b:-0}; upload processes ${p:-0}"; tail -n 6 /root/tz45-work/logs/85-upload.log
```

`exit=0` under an `UPLOAD COMPLETE` line of that run goes to §3.12. **A run whose lines name `UPLOAD REFUSED` or `status 401` is BLOCKED at once** — no token in the remote URL and none held by `gh`, a refusal that is not a rate limit, or a token GitHub does not take, which no further run changes. Any other exit is read from the log, and the same paste is handed over again, `600` s or more after that run's `exit=` line: `upload` resumes, keeping every asset already matching. **A run that ended without its line** — a key pressed under it, a reboot: the block printing, at two runs of it, more `runs begun` than `exit lines` and `upload processes 0` — **is one of the runs, and the same paste is handed over again at once.** **B-UPLOAD runs at most three times in all, and all within `21,600` s of its first hand-over**; a third run that does not complete, or that time passed without an `UPLOAD COMPLETE`, is BLOCKED. On a BLOCK the Release and its tag stay as they stand, named in the report (§2 item 9), **and the reading stands as read: its inputs are then on the host alone, and the report says so in its first lines** (CANON hard rule 16).

### 3.12 The proof — G-TAG, G-UPLOAD and G-DOWNLOAD

`I verify`, into `88-verify.log` (`mode_verify`, lines 2751 to 2790): no credential; it waits until 120 s after `upload.jsonl`'s completion record — an anonymous reply may be cached for 60 s (map §6, GitHub Releases) — then reads the Release on the tag through TZ-27's `verify_release` — the API's record of every asset, and, where every record is the set's, a full download of each, hashed as it arrives — and TZ-27's `release_reading`, and reads the tag on `origin` with TZ-27's `ls_remote_tag`. It must print `G-UPLOAD PASS`, `G-DOWNLOAD PASS` and `G-TAG PASS` in one line, every asset counted, and writes `verify.json`. Each request is held as `upload`'s are. **`I verify` runs at most three times, `600` s or more apart**, and its last run may wait, at most 6 h, until GitHub's status page — read by the session's own web tool, never from the host — shows an incident of unauthenticated traffic resolved (map §7 item 149). Where a run's `VERIFY FAIL` names `no asset missing` or `every asset uploaded, its bytes and digest the set's`, B-UPLOAD's paste is handed over once more, within its three and its `21,600` s, before the next `I verify`. A third `I verify` that does not pass is BLOCKED, and the Release stands as uploaded, named in the report. Where the classifier refuses `I verify`, its paste, in B-UPLOAD's form — the Executor waits for its `exit=` line with §3.11's block, `88-verify.log` and `verify` in the place of `85-upload.log` and `upload`, and reads the run from that log:

```
(trap '' HUP; date -u +%FT%T.%NZ; echo "run begun"; (cd /root/tz45-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz45-work/wt/research/tz45-l0-rule-w.py verify); echo "exit=$?") >> /root/tz45-work/logs/88-verify.log 2>&1; tail -n 5 /root/tz45-work/logs/88-verify.log
```

### 3.13 The units again — G-STILL

`I still`, into `95-still.log`, reads the four units again against `state.json`'s record and prints `G-STILL PASS` or `G-STILL FAIL` with the reason (§4.7). This TZ signals nothing, so a FAIL runs no block, and the report names what changed beside the reload records and the package history of §3.14 (map §7 items 120 and 166).

### 3.14 The closing reads

§0.3's block again, verbatim, the memory gate's reads among it, into `96-host-gate-again.log`: H1 to H5 are checked again, and its memory and disk reads are recorded with their instants and carry no threshold there — the modes' own floor reads were the gates. `I archive` again, into `97-archive-again.log`. Then, into `98-closing.log`:

```
cd /root/tz45-work && ls -la out/ fetch/ days/ && sha256sum out/* fetch/* days/* set.json reading.json rehearsal-base.txt rehearsal-w.txt rescore.txt release-set.json state.json read-ledger.jsonl upload.jsonl transfers.jsonl verify.json; wc -l upload.jsonl transfers.jsonl timing-replay.jsonl timing-rescore.jsonl read-ledger.jsonl
cat /root/tz45-work/state.json /root/tz45-work/read-ledger.jsonl
TZ=UTC systemctl show btc-recorder.service btc-pairbook.service btc-rewardbook.service adv3-bot.service btc-pairbook-archive.service btc-rewardbook-archive.service -p MainPID -p NRestarts -p ActiveState -p MemoryCurrent -p MemoryPeak
journalctl -u btc-recorder.service -u btc-pairbook.service -u btc-rewardbook.service -o short-iso --since -24h --no-pager | tail -n 60
du -sb /root/tz45-work /var/lib/btc-rewardbook /root/btc-forensics; df -B1 --output=source,size,avail /var/lib/btc-recorder; free -b
git -C /root/btc-5m-twap ls-remote origin refs/tags/tz-45-l0-rule-w-inputs 'refs/tags/tz-45-l0-rule-w-inputs^{}' refs/heads/tz-45-l0-rule-w
```

A file a BLOCK left unwritten is named as absent. Then contract §4.2's self-check, `C` the instrument's commit, into `99-selfcheck.log`, with two lines more — the diff's counts, and no archive in git history:

```
git -C /root/btc-5m-twap fetch origin
git -C /root/btc-5m-twap rev-list origin/main | grep -c "$C"
git -C /root/btc-5m-twap diff --name-only origin/main origin/tz-45-l0-rule-w
git -C /root/btc-5m-twap diff --numstat origin/main origin/tz-45-l0-rule-w
git -C /root/btc-5m-twap ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
for r in origin/main origin/tz-45-l0-rule-w; do git -C /root/btc-5m-twap ls-tree -r --name-only $r; done | grep -cE '\.tar$|tz45-manifest'
```

Then the report is drafted (§8), and §9 runs.

---

## 4. The gates — fixed here, before any of their data exists

| gate | population | PASS | false failure | power, against |
|---|---|---|---|---|
| **G-REHEARSAL** | the four assets of `rewardbook-streams-1793263627`, 2026-10-29 00:00 to 01:00 UTC, 150 markets, replayed twice | §4.1's two sets of lines byte for byte TZ-43's and the Architect's | `0` — the same stored bytes replayed by the same rules | `1`, any change in an asset, a decision, a fill, a queue, a crossing, a share, a sum or the arithmetic |
| **G-SET** | the walk from `1794182400` | 5 members, at most 3 non-members before the fifth | `0` | — |
| **G-BOOK** | every `book` frame of the members' first tokens but a seed, over the 5 days | the rebuilt touch equal to the venue's own at no fewer than 99 in 100 | a count, not an estimate: equal at `60,078` of `60,089` frames over L0's eight days (TZ-43's report) | `1`, a lost frame, a misread entry or a missed session |
| **DETERMINISM** | the first member day's first 24 slots; and `pack`'s outputs | each slot's line byte for byte the replay's; the second pack's bytes the first's | `0` on closed days (§3.10) | `1`, any difference between two downloads, two replays or two packs |
| **L0-W** | each of the 5 days' least and most (§1, the test) | §4.5 | `2⁻⁵ = 0.03125` for each answer, under independent days — named, not measured (§1) | EARN `0.590490`, `0.773781` and `0.950990` where each day's least reaches `θ` with probability `0.90`, `0.95` and `0.99` |
| **G-SOURCE** | this run's files the reading rests on, 22 at five members | each a regular file whose SHA-256 this run's own record names | `0` — a hash of bytes | `1` against any changed byte |
| **G-PACK** | the day directories of every candidate the walk considered | every name classified; every selection, slot record and poll file read whole and stored verbatim, but a file of replies a line of which withholds it, named and left out; every stream and other name left out and never opened; the archives, the manifest and the set written | `0` | `1` |
| **G-RESERVE** | every open and listing under `/var/lib/btc-rewardbook/` in `pack` | opens equal to the members kept and the files of replies scanned, listings to the days, and the hook refusing nothing | `0` — the hook counts every one | `1` |
| **G-UPLOAD** | the assets of the set, on `tz-45-l0-rule-w-inputs` | each in the API's record by name, its size the set's, `state` `uploaded`, its digest `sha256:` the set's, its download URL the tag's; none missing, none beyond the set; the Release published on the tag | `0` — the host of the bytes records it | `1` |
| **G-DOWNLOAD** | the same assets | each downloaded anonymously, whole, its bytes and SHA-256 the set's | `0` | `1` |
| **G-TAG** | the tag `tz-45-l0-rule-w-inputs` on `origin` | lightweight, at the pack's commit | `0` | `1` |
| **G-STILL** | the recorder, the pair book, the reward book and the advisor, §3.3 to §3.13 | unchanged, or the pair book moved by its archive's own restarts alone | not `0`: a restart by the package manager or by another project's reload reads FAIL with no fault of this TZ (map §6, process supervision; §7 items 120 and 166) | `1`, a restart or a stop that is not that archive's |

A FAIL of G-REHEARSAL, G-SET or G-BOOK, or a DETERMINISM FAIL of the replay, leaves the reading unread. A FAIL of G-SOURCE, G-PACK, G-RESERVE or the pack's DETERMINISM is BLOCKED before any upload; of G-UPLOAD, G-DOWNLOAD or G-TAG after §3.12's runs, BLOCKED with the Release as it stands, named. **A publication's BLOCK leaves the reading as read** — its inputs then on the host alone, said so in the report's first lines — and the Architect's verdict names the step that moves them. A G-STILL FAIL blocks nothing: the report names its cause.

### 4.1 G-REHEARSAL

The four assets — 2026-10-29 00:00 to 01:00 UTC, `47,329,972` bytes — are one stand-in hour: every market of the first seed after the first subscribe, 150, each with its first `book` item's token as its first token, under fixed parameters, so that nothing of the store is read for it (`rehearsal_members`, `rehearsal_polls` and `mode_rehearse`, lines 2389 to 2410, lines 2440 to 2459 and lines 2462 to 2501). `compare_lines` prints, per member and variant, its reward, rebate and marks at twelve places and its position, cost, fills, shares, crossed shares, scored nanoseconds, sends, cancels, refusals, crossings and mark — and, under rule W, the day's largest distance inside the touch and the hit — then the book's counts (lines 2413 to 2427). Two replays:

- **TZ-43's rule, TZ-43's three variants and TZ-43's parameters** — minimum size `50` shares, maximum spread `4.5` cents, a rate of `100` a day, no fee and no poll: **451 lines, SHA-256 `1ab40f4b2a9b4f263e92959dc78a67dc9583731889cce70b22edad59091944cd`** — the digest `research/tz43-l0-our-quote.py` fixes at its line 160 and TZ-43's run printed on the host. **The engine under rule W is the engine that reproduces TZ-43**: on 2026-11-15 the Architect also replayed the whole of 2026-11-02 under TZ-43's rule with this engine, on the public bytes, and its `days/1793577600.json` and `days/1793577600.slots.txt` were byte for byte the files TZ-43 wrote on the host — SHA-256 `93c76d15…` and `aae9a599…`, the Release `tz-44-l0-inputs`'s `tz43-days-1793577600.json` and `tz43-days-1793577600.slots.txt`.
- **Rule W, its nine variants** — minimum size `20` shares, maximum spread `2` cents, a rate of `100` a day, a rebate coefficient of `1/80`, and polls the instrument makes itself: for slot `j` and member `i` a poll at `S + 30 + i` s whose figure is `((i + j) mod 5) / 2` and whose row carries the rehearsal's own terms — but in the third slot, for a member whose index is 3 mod 7, a page with no row; in the second slot, for an index that is 5 mod 11, a minimum size of 50 shares, the rehearsal's own again in the slots after it; and in the fourth slot, for an index that is 9 mod 13, a row that states no maximum spread: **1,351 lines, SHA-256 `9c8c1a343a5a95be0ade7c4a017ff51707fac11bb55d8d8904b1e20024f85bf6`**. **The Architect's lines come from a second implementation of rule W** — the rule, the poll's decision, the terms with the credit they govern and the adverse hit written again from §1 as a subclass over TZ-43's committed engine, `research/tz43-l0-our-quote.py` at `5192aff`: its targets by `Fraction`s, a full decision at every call with none of the engine's shortcuts for an unchanged touch, the markets whose terms moved and each variant's credit kept in tables of its own, its hits kept apart, a read day's terms parsed by its own code from the raw replies of the Release `tz-44-l0-inputs`, no line shared with Appendix A's changed lines. It equals the instrument byte for byte under Python 3.12.3 on this hour — 36 markets quoted, 20 fills, 4 crossing orders and 6 refusals under `pess-bt` — on this hour at maximum spreads of `3` and `4.5` cents, on the self-test's synthetic day, **and on the whole of 2026-11-04 and of 2026-11-08 under all nine variants — the two days on which the venue moved the most markets' terms, 54 and 56 of the day's 150 — each day's own members and polls, `6,417,117` and `15,448,742` lines of stream, its day file and its slot lines byte for byte the instrument's: SHA-256 `810eda47…` and `ca267379…` for the first day, `8057924c…` and `a03cd0f5…` for the second**. **The engine beneath both is TZ-43's**, whose own independent reference TZ-43 §4.1 records; what the second implementation checks is everything this TZ changed in it.

`rehearse` prints each replay's lines and digest beside the expected, and `G-REHEARSAL PASS: 2 of 2`. **A FAIL means the stored record differs from what the Architect replayed, or that the instrument replays otherwise**, and the reading would not be what §1 describes.

### 4.2 G-SET

`fetch` prints `G-SET PASS` when the walk from `1794182400` has formed 5 members with at most 3 non-members before the fifth; every member's stream files are among the archive's assets by their own names, and the bytes and SHA-256 the replay downloads them by are the archive's; every member's document is found once, open or closed; and `set.json` is written. Every candidate is listed in order, a non-member with its first failing reason.

### 4.3 G-BOOK

At every `book` frame of a member's first token but a subscription's seed, the touch the replay rebuilt — the best bid and its size and the best ask and its size — equals the frame's at **no fewer than 99 in 100** over the set (`g_book`, lines 2254 to 2266). `replay` and `score` print the counts by day, and the count of frames equal at every level beside them, barred. `score` reads no reading where G-BOOK fails: a FAIL means the replay's book is not the venue's, and its fills are not ours.

### 4.4 DETERMINISM

`rescore` downloads the set's first day's first 24 slots again and replays them again from the day's start; each slot's line — the stream's counts and each variant's fills, shares, position, cost and reward with a SHA-256 of every member's state — must be byte for byte the replay's: 24 of 24 (`slot_line`, lines 2155 to 2178; `mode_rescore`, lines 2269 to 2286). The pack's is §3.10's.

### 4.5 The reading

| condition, on each day's least and most over the set's 5 days (§1) | reading |
|---|---|
| every day's least at or above `θ = 10` USDC, and some day's most at or above it | **EARN** |
| every day's most below `θ`, and some day's least below it | **NO EARN** |
| otherwise | **UNDECIDABLE** |

Pure arithmetic on the day files (`day_money`, `day_brackets` and `l0_reading`, lines 2291 to 2316, lines 2333 to 2336 and lines 2319 to 2326); `score` prints all nine variants' money on every day — the gated figure, the total, the reward paid, the reward before the `1`-pUSD minimum, the rebate, the marks, the hits and the markets quoted, with the members paid, the fills, the shares, the crossed shares, the hours scored and the marks by kind — each day's least and most with the variant that gives each, and, barred from every reading, `central`'s and each variant's total and mean day. **No row reads a power.** The marks are a proxy, named so (§1).

### 4.6 The publication's gates

G-SOURCE, G-PACK, G-RESERVE and the pack's DETERMINISM are §3.10's; G-UPLOAD, G-DOWNLOAD and G-TAG §3.12's. Each is an identity of bytes or counts: it cannot read PASS where its condition fails, and it fails at every change of what it names. None of them judges a market.

### 4.7 G-STILL

From §3.3 to §3.13 the recorder, the reward book and the advisor keep their `MainPID`, `NRestarts` and `ActiveState`, and the pair book keeps them or is moved by its archive's own restarts alone — its ledger's `restart` records since §3.3's read, a chain from the recorded `MainPID` to the current one, `NRestarts` one higher at each, the unit `active` (`still_reading`, lines 2991 to 3009). The reward book's archive restarts nothing (map §2.6). **This TZ signals nothing**, so a FAIL runs no block, and the report names what changed beside §3.14's journal of the units.

---

## 5. The instrument

`research/tz45-l0-rule-w.py`, Appendix A, fixed by the Architect as this TZ's Validation and written byte for byte. **The standard library alone**, run under `/root/tz04a-env` — Python 3.12.3, the capture units' interpreter, which nothing here modifies. **It is two committed instruments joined, and what this TZ adds** (§10, C3):

- **TZ-43's, `research/tz43-l0-our-quote.py`** — the audit hook, the floors, the idle stretch and both archives' runs, the reward book archive's ledger, sets and asset map, the store's selection, slot records, members and polls and the slot rule, the replay, the set, its documents, the downloads, the units held, the rehearsal, G-STILL, NUMBER, the modes and the self-test: **2,873 of its 3,056 lines stand here unchanged.** Changed in it: its constants — the map's revision and rows, the number, the walk's first day, its `5` and `3`, the names, the work tree; the nine variants; rule W's function and its branch of `Day.decide`; the decision `Day.poll` calls, the terms it reads and the credit it keeps; a poll's row with its own terms — `terms_of`, `polls_of`, the polls file's lines and their reader; the hit and the credit in `Day.finish`, the day file and the compared lines; the rehearsal's second replay; the rescore's timing line (map §7 item 157); the day's money, the brackets and the score; `reclaim`, which leaves to the Release what the Release holds (map §7 item 167); and the self-test's literals.
- **TZ-44's, `research/tz44-l0-inputs-release.py`** — a day's archive, a stored reply's body judged, the Release's client over TZ-27's, the upload and its proof: `Gh44` as `Gh45`, `tag_reading`, `classify`, `member_info`, `day_budget`, `body_reason`, `withhold_reason`, `list_day`, `pack_day`, `read_set`, `upload_logger`, `transfer_logger`, `transfer_summary`, `branch_on_origin`, `mode_upload`, `mode_verify`, `load_tz27`, `jsonl_append`, `jsonl_read` and `budget_s`, **each TZ-44's text but for four names** — `Gh45`, `PACK_BASE_S`, `RELEASE_SET` and the set's file's name in one message. New beside them: `work_sources`, `manifest_doc`, `set_doc`, `release_text` and `mode_pack`, for this run's own files in the place of TZ-43's.
- **It loads TZ-27's instrument from beside itself, executed from the bytes whose SHA-256 it asserts** (`load_tz27`, lines 373 to 384), as TZ-28's, TZ-34's and TZ-44's do; TZ-27's audit hook is installed then, its work tree set to `/root/tz45-work` and its mode to this run's, and TZ-27's `CONTENT_TYPE` set to `application/octet-stream`, which its `upload` reads at each call, so that no asset is labelled gzip.

**Its own audit hook** (`policy` and `_audit`, lines 304 to 356 and lines 359 to 367) refuses every open, listing, request and process §2 does not give the running mode — processes are `git`, `systemctl` and `stat`, and `gh` in `upload` alone, for TZ-27's `credential` — and counts every open and listing under the reward book's store. One mode a run; each prints its findings with UTC stamps and, on every exit — a BLOCK's and a failed assert's included — whether glibc took its two settings, its peak memory, the refusals by either hook and the store's opens and listings (`main`, lines 3234 to 3260; map §7 item 151). A price is an integer of thousandths and a size of hundredths from the venue's own text; a score is an integer; a share is a pair of integers; the reward a `Decimal` sum of 50-digit quotients; every position, cost, rebate, mark and hit a `Fraction`; and every printed figure has twelve decimals, half-even. Exit `0` is every assert held; exit `1` a failed assert, named, or a BLOCK whose message says so. Run with `-O` it refuses to start.

| mode | what it does | lines |
|---|---|---|
| `fingerprint` | contract §1 steps 3 and 4, asserted | 2943 to 2970 |
| `number` | CANON hard rule 2 | 2973 to 2978, 2981 to 2988 |
| `selftest` | 71 checks | 3473 to 4222 |
| `still` | the four units, recorded, then compared; G-STILL | 2991 to 3009, 3012 to 3037 |
| `scratch OWN` | the UUID directories beside OWN, live or earlier | 3040 to 3057, 3066 to 3078 |
| `archive` | the reward book archive's record, printed; the rehearsal's four assets in their set | 3081 to 3119 |
| `rehearse` | G-REHEARSAL: TZ-43's rule against TZ-43's lines, rule W against the second implementation | 2389 to 2410, 2440 to 2459, 2462 to 2501 |
| `fetch` | the walk, each member's record and polls, the documents, the set; G-SET | 1834 to 1860, 1978 to 2040 |
| `replay` | every member day, slot by slot; G-BOOK | 2098 to 2132, 2195 to 2207, 2229 to 2251 |
| `rescore` | DETERMINISM | 2269 to 2286 |
| `score` | the days' money, the least and the most, the reading | 2291 to 2316, 2333 to 2336, 2319 to 2326, 2339 to 2384 |
| `pack` | G-SOURCE, G-PACK, G-RESERVE; a second run DETERMINISM | 2798 to 2823, 2636 to 2681, 2868 to 2937 |
| `upload` | B-UPLOAD: the Release and its assets, through TZ-27's `credential`, `GitHub` and `upload_set` | 2506 to 2547, 2848 to 2865, 2717 to 2749 |
| `verify` | G-TAG, G-UPLOAD, G-DOWNLOAD, through TZ-27's `verify_release`, `release_reading` and `ls_remote_tag` | 2549 to 2551, 2751 to 2790 |
| `reclaim TREE...` | §9 | 3154 to 3160, 3163 to 3219 |

**The clock** (`budget_s`, `quiet` and `hold`, lines 560 to 562, lines 571 to 585 and lines 588 to 599): a unit of `budget` seconds — a slot's download and replay `5 + ⌈bytes / 2,000,000⌉ + 45` s, a document request `120` s, a day's read of the store `60` s, this run's files in `pack` `60` s, a day of `pack` `30 + ⌈bytes / 500,000⌉` s, a transfer of the Release `5 + ⌈bytes / 2,000,000⌉` s — starts at second 15 of a 900-s window or later and by its second `590 − budget`, inside the pair book's idle stretch (map §2.5); never from `budget + 60` s before either archive's calendar run to 60 s after it; and never while either archive's service is running — the runs off their calendar included (map §7 items 115, 129 and 166). It waits a second at a time and BLOCKS after `7,200` s.

---

## 6. Cost

**Measured by the Architect on 2026-11-15 under Python 3.12.3, on two cores of an Intel Xeon at 2.70 GHz, on the bytes sent**, in a stand-in host built from public bytes alone: the primary checkout at `5192aff`; a store of the six days 2026-11-03 to 2026-11-08 unpacked from the Release `tz-44-l0-inputs` — one of them, 2026-11-06, the non-member TZ-43 found — with the walk begun at 2026-11-03 in a copy of the instrument that differs in that one constant; an archive record written from TZ-43's published `fetch` files; the 480 stream assets of the five member days, `6,107,963,040` bytes, as the archive's Releases serve them; TZ-27's `_FakeGitHub` in another process; and stand-ins for `systemctl`, `gh`, the venue's documents and the idle stretch's wait. The host has one processor and ran TZ-43's replay at `0.1437` s a megabyte (its report) where the Architect's ran the same code at `0.105`: a ratio of `1.37`.

| check | population, at its upper bound | measured | at the bound |
|---|---|---|---|
| `selftest` | literals, two synthetic days of two slots, temporary trees, a loopback GitHub | `0.78` to `1.30` s of wall clock, three runs | fixed, `2` s |
| `fetch` | 8 candidates: 5 members, each its selection, 96 slot records and 96 reward files of 450 polls; 3 non-members, each its slot records; at most 750 markets and ⌈750 / 50⌉ × 2 = 30 document requests | `8.1` s over 6 candidates, 5 of them members, the requests answered by a stand-in | **`30` s**, every read held |
| `rehearse` | the four assets, `47,329,972` bytes, replayed twice | `4.0` to `4.3` s and `3.8` to `3.9` s of processor, two runs | **`12` s** at the host's ratio; each BLOCKED above `60` s |
| `replay` | 480 units, 5 days of 96 slots, each as heavy as the heaviest of the eight days read, `31,823,974` bytes — `15,275,507,520` bytes | `0.0889` s a megabyte over the stand-in's 480 units, `6,107,963,040` bytes, `543.2` s of processor; the slowest unit `0.1495`, the fastest `0.0751`, every unit above 5 MB | **`1,861` s** — those bytes at the mean rate times `1.37`; at the slowest unit's rate `3,129` s, which the projection stops: **projected over the set's own bytes after its first 24 units, BLOCKED above `3,000` s** |
| `rescore` | 24 units of the first day at that slot, `763,775,376` bytes | `17.3` s of processor over the stand-in's 24, `193,972,636` bytes | **`157` s** at the slowest unit's rate times `1.37`; projected after its first 6 units, BLOCKED above `200` s |
| `score` | 5 day files of 1,350 rows | `0.2` s | under `2` s |
| `pack`, twice | 8 candidate days, each at its BLOCK, `60,000,000` bytes of members — `480,000,000` bytes scanned, read, written and hashed a run | `4.9` and `4.8` s a run over 6 days, `95,133,558` bytes of members | **`111` s** for the two, at `8,659,635` bytes a second, the slowest of the Architect's runs of TZ-44's `pack` (TZ-44 §10, C4) |
| `fingerprint`, `number`, `still`, `scratch`, `archive` twice, `reclaim` | systemd, git, the ledgers, the map's 63 files | under `1` s each | about `60` s together |

**Processor at those bounds at most `2 + 30 + 12 + 1,861 + 157 + 2 + 111 + 60 = 2,235` s**, under `3,600`, so nothing is sampled; **with every fail-fast bound reached together** — the replay's `3,000`, the rescore's `200`, the rehearsal's two of `60` — and the rest's `205`, `3,525` s, under `3,600`: a set heavier or slower than that stops BLOCKED at the projection and does not run on. The set's own bytes are not known before `fetch`: the eight days read grew from `706,996,816` to `1,779,050,648` bytes a day, and five days at the last, `8,895,253,240` bytes, project to about `1,083` s on the host. `upload` and `verify` move bytes and hash them: about `112,000,000` bytes of assets at five candidate days and `160,000,000` at eight — `12` to `17` s of upload at the host's `9,297,801` bytes a second, with one second's gap after each of the 28 to 31 assets, and `8` to `11` s of download at `14,140,406` (map §6, GitHub Releases).

**Wall clock** from §0.0, at the measured rates: §0 and §3.1 to §3.4 about 15 minutes; the rehearsal and `fetch` minutes each, once the idle stretch opens — at most 900 s apiece to wait for it; the replay's 480 units, each about 5 s of download and replay at 20 MB a slot, held to the idle stretch — `575` s of every `900` — about 70 minutes; the rescore, the score and the pack minutes more; B-UPLOAD's wait for the Boss; the proof and the report about 40 minutes: **about 2 h 45 min, and the Boss's paste**. At its bounds — the replay at `3,000` s of processor, `fetch` waiting its `10,800` s for an archive that has not moved a day, every memory gate reading five times, B-UPLOAD its `21,600` s — about 12 h, so that a run begun late in the band may meet the package manager's morning run, from 06:00 UTC, and G-STILL then names it (§4.7; map §7 items 120 and 143). **A wait on GitHub's status page adds at most 6 h to the step that meets it** (§3.5, §3.7, §3.12). A hold's `7,200` s is the idle stretch's longest wait, the calendar guard and either archive's longest run together twice over.

**The fail-fast bounds, each a constant:** a hold `7,200` s (line 158); the memory floor's reads `240` s a mode (line 162 and line 163); `fetch`'s wait for the archive `10,800` s (line 112); a download six tries with waits of `5` to `60` s (line 149; `download`, lines 2062 to 2093); TZ-27's `60` s an API request, `300` s an upload and `120` s a download, four attempts a file with waits of `900` s at most and three a download (TZ-27 lines 118 to 124); the Executor's wait for B-UPLOAD `21,600` s from its first hand-over, its wait block `9 × 60` s a run; and a last `I rehearse`, `I replay` or `I verify` 6 h for GitHub's status page.

**Disk** and **memory:** §0.4.

---

## 7. Validation

| # | check | expected |
|---|---|---|
| **V1** | `I0 fingerprint` and `I fingerprint`, §0.2 and §3.1 | `FINGERPRINT PASS: revision 2026-11-13-a; anchors 6 of 6, 4 re-derived; rows 63: frozen 60 of 60 equal, tracked 2, reported 1`, twice |
| **V2** | §0.3's host gate, at §0.3 and §3.14 | at §0.3 H1 to H5, the memory and the disk gate — 11 checks; at §3.14 H1 to H5 — 9 checks — and the two reads recorded; every memory read with its instant; the rest printed |
| **V3** | `I0 number`, §0.5 and §3.1 | `NUMBER PASS - 2 of 2`, twice |
| **V4** | §0.1's script, at §0.1 and §3.1 | two lines a run: 4,230 lines, 229,313 bytes, `1d415754…`; 2,078 lines, 106,284 bytes, `2cba96bc…` |
| **V5** | `I selftest` | `SELFTEST PASS: 71 checks` |
| **V6** | the archive's record, at §3.4 and §3.14 | the ledger's size, SHA-256 and records, every run's line, every complete run's set, the slots the assets reach, the tags; the rehearsal's four assets in their set by name, bytes and SHA-256 |
| **V7** | G-REHEARSAL | TZ-43's rule `451` lines, SHA-256 `1ab40f4b2a9b4f263e92959dc78a67dc9583731889cce70b22edad59091944cd`; rule W `1351` lines, SHA-256 `9c8c1a343a5a95be0ade7c4a017ff51707fac11bb55d8d8904b1e20024f85bf6`; `G-REHEARSAL PASS: 2 of 2` |
| **V8** | G-SET | 5 members; every candidate considered with its verdict; each member's markets, slots, files, bytes and polls; the document requests and the members resolved |
| **V9** | the replay, twice | every unit inside the idle stretch or listed; the projection after 24 units against `3,000` s; every day's two files; G-BOOK; no day replayed at the second run |
| **V10** | DETERMINISM of the replay | `24 of 24` |
| **V11** | the score, twice | the power's three lines and the false reading's; all nine variants on each of the five days; each day's least and most; the reading; `reading.json` `unchanged` at the second; the read ledger's lines; the instant §3.1's `ls-remote` printed the instrument's commit on `origin`, before the read ledger's first `fetch` line |
| **V12** | G-SOURCE, both `pack` runs | `G-SOURCE PASS: 22 of 22 equal to this run's own record` |
| **V13** | G-PACK, G-RESERVE and DETERMINISM | every candidate day with its names by kind, its members and bytes, the files of replies scanned, each file withheld with its bytes and its reason, its archive's bytes and SHA-256 and every excluded name with its bytes; `days over their budget 0`; the assets, `23` and one a candidate day; `G-RESERVE PASS`, listings one a day; the outputs `wrote`, then `unchanged`, each two and one a candidate day; `DETERMINISM PASS` |
| **V14** | B-UPLOAD | each run's `exit=` and its last lines; `credential:` its source; `UPLOAD COMPLETE: Release <id> on tz-45-l0-rule-w-inputs`, the set's assets; `upload.jsonl`'s last line `complete`; the transfers' line |
| **V15** | `I verify` | `G-UPLOAD PASS: n of n …; G-DOWNLOAD PASS: n of n downloads, <bytes>; G-TAG PASS: tz-45-l0-rule-w-inputs at <the pack's commit>`, `n` the set's assets and the bytes `release-set.json`'s `bytes_total`; the transfers' line |
| **V16** | `I still`, §3.13 | `G-STILL PASS`, or FAIL with what changed, named beside §3.14's reads of systemd, the units' journal and the package history |
| **V17** | contract §4.2's self-check, and its two lines more | its first count `0`; the diff naming `research/tz45-l0-rule-w.py` alone, `4230` lines added and `0` removed; nothing `.parquet` or `.zip`; the last count `0` |
| **V18** | the hook | `opens refused: 0, by TZ-27's hook: 0` at every mode, its closing lines printed on every exit; `reward book opens` above `0` at `fetch` and `pack` alone |
| **V19** | memory and disk | every mode's printed peak, against §0.4's `86,329,224`; every `MemAvailable` and free-space read a mode printed, none passing below `172,658,448` or `7,800,000,000`; `malloc tuned: True` at every mode |
| **V20** | §9's `reclaim` runs, B-RECLAIM-SCRATCH's and B-RECLAIM-OWN's | files considered, named by a report, kept by name, copied, already held and left to the Release; the store's count after equal to before plus the copies; every line of each `reclaim`'s output quoted unfiltered (map §7 item 119) |
| **V21** | the removals | `git worktree remove` without `--force` exit `0`; `test -e` exit `1` for `/root/tz45-work` and each directory removed; `git worktree list` naming `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else |
| **V22** | the classifier | every block it refused, with the paste handed over, the instant the Boss ran it and the log lines that verify it |

**Barred from every gate:** `central`; each variant's total and mean day; the count of book frames equal at every level; the members' and bytes' counts of `pack` — the store's, printed and not expected.

---

## 8. The report

`CryptoReports/TZ-45-l0-rule-w-report.md`, in contract §8's order. **In its first lines:** the reading, with each of the five days' least and most and the variant that gives each, and every day's money of the eight gated variants with its parts and its hits; G-REHEARSAL, G-SET, G-BOOK and DETERMINISM; the set — candidates considered, members, non-members with their reasons; **the Release — its id, the tag, its commit, its assets and their bytes — with G-SOURCE, G-PACK, G-RESERVE, G-UPLOAD, G-DOWNLOAD and G-TAG, or, where the publication BLOCKED, that the reading's inputs are on the host alone**; the instant the instrument's commit reached `origin` beside the read ledger's first line; G-STILL; the advisor's `commit.txt` where it differs from map §3's; and every block the classifier refused and who ran it. **Every asset by name, bytes and SHA-256**, as `pack` printed the set — contract §5.1's local hash, with `verify`'s line of each as its record and its download. Beyond what V1 to V22 print: §0.0's clock line and its readiness read, at both runs; the set as `fetch` printed it; every day's money by variant as `score` printed it, `central`'s barred; the G-BOOK counts by day; the timing files' counts, and every unit that ended after second 590, as `replay` and `rescore` printed them; every day as `pack` printed it, and every file withheld, by its name, bytes and reason; who ran B-UPLOAD and when, its `credential:` line, each run's last lines and the transfers' lines of `upload` and `verify`; the archive's record as `I archive` printed it, at both reads, each run off the calendar beside §0.3's reads of systemd; the four units at both reads, memory included; the read ledger's lines; every free-space and `MemAvailable` read with its instant and bound, and every mode's printed peak; §0.3's `du` and journal lines at both runs; §9's counts and removals; and every file the run wrote, by SHA-256 — on a BLOCK at the set, all but the files of `fetch/` (§3.6). **It prints no single member's, fill's or poll's price, size, rate, competitiveness or outcome** (§2 item 10), no credential (§2 item 5) and no address of the host (§2 item 6). **The report is drafted in the primary checkout `/root/btc-5m-twap` after §3.14 and before B-RECLAIM-OWN, and committed after it**, so the removal of this TZ's tree is in it. **A BLOCKED report is contract §9's, and beside it — this TZ's own exception, said so in the report — the Release's state where B-UPLOAD ran, the reading where `score` read one, and §9's lines.**

---

## 9. Reclaim — the host left clean (CANON hard rule 15)

**What a file is kept for:** a committed report prints its SHA-256, whole or as a prefix of 16 to 64 hex characters, or it is kept by name: `state.json`, `read-ledger.jsonl`, `release-set.json`, `upload.jsonl`, `transfers.jsonl`, `verify.json` and every file under `logs/` (`by_name`, lines 3131 to 3133). `reclaim` copies each into `/root/btc-forensics/` as `<tree>--<path with / as -->`, by exclusive create, and verifies its hash; a name already there with the same hash is counted as held, and with another hash is a failed assert; before each copy it reads free space and BLOCKS where the copy would leave less than `7,400,000,000` bytes (`mode_reclaim`, lines 3163 to 3219). **A file the report names by hash that the Release holds is not copied** (map §7 item 167): where `verify.json` records an asset of that SHA-256 proved by a full anonymous download, `reclaim` prints `R release`, its hash, its path and the asset's name on `tz-45-l0-rule-w-inputs`, and leaves it to the Release (`released_by`, lines 3154 to 3160) — the day archives, the manifest and this run's 22 files; where `verify` did not pass, `verify.json` is absent and every such file is copied as before. The branch worktree is not copied: `reclaim` asserts that `git status --porcelain --ignored` in it prints nothing and that its `HEAD` is its upstream's (`pristine`, lines 3136 to 3143), so `git worktree remove` needs no `--force`. The report's draft in `CryptoReports/` counts as a report. The downloads are removed by each unit as it ends. **No `reclaim`'s output is filtered** (map §7 item 119): every line it prints is quoted. B-RECLAIM-SCRATCH is §3.3.

**B-RECLAIM-OWN**, last, after §3.14 and with the report drafted. **Its output is written to no file; the report quotes it verbatim from the session**, every line of it:

```
cd /root/tz45-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz45-work/wt/research/tz45-l0-rule-w.py reclaim /root/tz45-work
cd /root/btc-5m-twap && git -C /root/btc-5m-twap worktree remove /root/tz45-work/wt; echo "exit=$?"
rm -rf /root/tz45-work; echo "exit=$?"
test -e /root/tz45-work; echo "exit=$?"
git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
find /root/btc-forensics -type f | wc -l
df -B1 --output=source,size,avail /var/lib/btc-recorder
```

`reclaim` must print `RECLAIM PASS` before the removals. **Its paste**, where the classifier refuses any line of it — every step chained to the one before it, the removals reached only after `RECLAIM PASS`; its output goes to the Boss's terminal, the tree its log would be in being removed:

```
(cd /root/tz45-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz45-work/wt/research/tz45-l0-rule-w.py reclaim /root/tz45-work) && cd /root/btc-5m-twap && git -C /root/btc-5m-twap worktree remove /root/tz45-work/wt && rm -rf /root/tz45-work; test -e /root/tz45-work; echo "exit=$?"; git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list; find /root/btc-forensics -type f | wc -l
```

Where the Boss ran it, the Executor verifies it by its own reads — `test -e /root/tz45-work; echo "exit=$?"`, `git -C /root/btc-5m-twap worktree list`, `find /root/btc-forensics -type f | wc -l` and `sha256sum /root/btc-forensics/tz45-work--*`, each copy's hash against the report's — and the report quotes those reads; a refused first attempt is quoted too. The branch `tz-45-l0-rule-w` stays on `origin` and as a local ref; only its working tree goes. **Kept:** the running units' code trees, the capture roots, both archives' state, the forensic store and the Release — data and code, never scratch.

---

## 10. Pre-send checks

Performed by the Architect on 2026-11-15, against this file as sent (CANON PART VI), with `origin/main` at `5192aff` — map revision `2026-11-13-a`, 2,105 lines, 610,703 bytes, SHA-256 `3c8455a7…` — cloned in the session. §0 to §9 were read start to end in a pass apart from their writing; that reading found the defect row C8 records, and every paragraph changed after it was read again in the assembled file. Line numbers of the instrument are Appendix A's; of TZ-27's, TZ-33's, TZ-43's and TZ-44's files, those of `5192aff`. Every line reference to Appendix A, in §0 to §9 and here, was resolved from its syntax tree when this file was assembled, not typed; **the header's list of map items is computed from the items this file cites**, not typed either.

**What the Architect ran, and on what.** §0.1's script against this file as sent, in a stand-in checkout at `5192aff` with this file added to `CryptoTZ/`, printing §0.1's two rows; then `I0 fingerprint` against the map and the 63 files of its table — `FINGERPRINT PASS: revision 2026-11-13-a; anchors 6 of 6, 4 re-derived; rows 63: frozen 60 of 60 equal, tracked 2, reported 1` — and `I0 number`, `NUMBER PASS - 2 of 2`. `I selftest`, `71` checks. **Every mode, end to end, on the stand-in host of §6** — a store of six days already read, the walk begun at 2026-11-03 in a copy of the instrument that differs in that one constant: `fingerprint`, `still`, `archive`, `rehearse`, `fetch`, `replay` twice, `rescore`, `score` twice, `pack` twice, `upload` against TZ-27's `_FakeGitHub` in another process, `verify`, `still` and `reclaim`, every one exit `0` — G-REHEARSAL 2 of 2; G-SET 5 members of 6 candidates, 368 markets, 480 stream files, `6,107,963,040` bytes; G-BOOK `42,084` of `42,088`; DETERMINISM 24 of 24; `score` twice, the second `unchanged` — on days already read, which is no reading; G-SOURCE 22 of 22; G-PACK 6 days, 1,164 members, **each day's archive byte for byte the one the Release `tz-44-l0-inputs` holds for that day, 6 of 6**; G-RESERVE 1,746 opens and 6 listings; the pack's DETERMINISM 8 of 8; `UPLOAD COMPLETE`, 29 assets, `127,871,430` bytes; G-UPLOAD, G-DOWNLOAD and G-TAG 29 of 29; G-STILL; `RECLAIM PASS`, 23 files copied and 29 left to the Release; no open, listing, request or process refused by either hook in any mode. §0.0's readiness read on that store — `candidate 1793923200 2026-11-06: not whole`, `ready=1: 5 whole days of 5` — and §3.11's wait block on a log with no line, with a run in progress and with a run ended without its line. **The engine, three ways:** under TZ-43's rule the whole of 2026-11-02 byte for byte TZ-43's own published day file and slot lines (§4.1); under rule W byte for byte the second implementation on the synthetic day, on the rehearsal's hour at three spreads and on the whole of 2026-11-04 and 2026-11-08 (§4.1); and the eight read days under the nine variants (§1's table). **All of it on days already read or on synthetic bytes: no asset, selection, slot record or poll of a day from 2026-11-09 was read.**

| # | check | result |
|---|---|---|
| **C1** | scope against body | **Repository paths the body names.** Written: `research/tz45-l0-rule-w.py`, new, and `CryptoReports/TZ-45-l0-rule-w-report.md` — §2's two. Read by the run: this file; `SYSTEM-MAP.md` and the 63 files of its §0 table; `research/tz27-pairbook-archive.py`; every `.md` of `CryptoReports/`, by `reclaim`, for its hex tokens. Cited and not read by the run: `research/tz43-l0-our-quote.py`, `research/tz44-l0-inputs-release.py`, `research/tz33-reward-book-capture.py`. **Committed entry points:** TZ-27's `credential`, `GitHub`, `upload_set`, `verify_release`, `release_reading`, `ls_remote_tag`, `upload_ready`, `store_path`, `HashingReader`, `json_bytes`, `forbid`, `_FakeGitHub` and its audit hook — C7. **Output files:** under `/root/tz45-work/`, `logs/*`, `stage/`, `wt/`, `selftest-tmp/`, `state.json`, `read-ledger.jsonl`, `rehearsal-dl/`, `rehearsal-base.txt`, `rehearsal-w.txt`, `fetch/<D0>.json`, `fetch/<D0>.polls.jsonl`, `set.json`, `dl/`, `days/<D0>.json`, `days/<D0>.slots.txt`, `timing-replay.jsonl`, `timing-rescore.jsonl`, `rescore.txt`, `reading.json`, `out/rewardbook-inputs-<D0>.tar`, `out/tz45-manifest.json`, `release-set.json`, `upload.jsonl`, `transfers.jsonl`, `verify.json`; `/root/btc-forensics/tz45-work--*`; the report; the branch, its pull request, the tag and the Release's assets. **Intersections with §2, by path and by content class, each a named exemption there:** the report on `main` — item 9; the Release, whose assets carry prices, sizes, rates, competitiveness, fills and outcomes — items 3 and 10, by "Remote objects"; the store's reads by §0.0, `fetch` and `pack` — item 3; both archives' ledgers and sets — item 4; `df`, `find`, `grep -c` and `du -sb` on the capture roots — items 2, 3 and 4; the advisor's `commit.txt` — item 11; the credential read in the Boss's shell — item 5; **and §9's forensic copy of a file that carries a member's figures, where the Release does not hold it — item 10, an exemption this check added: TZ-43's §2 had the same intersection unnamed.** A log is no asset: it is a host's record (map §7 item 154). |
| **C2** | origin of every expectation | **Quoted from a committed artifact at `5192aff`:** revision `2026-11-13-a`, the six anchors, `63`, `60`, `2`, `1` — map §0; TZ-27's 2,078 lines, 106,284 bytes and SHA-256 — map §0's row; `31612203008` and the recorder's commit — map §6, host identity; `2,532` and the two worktrees — map §3; `7,300,000,000` and `100,000,000` — `research/tz33-reward-book-capture.py` lines 190 and 192; `58,953,728 / 49,168,384` — map §6, memory; `9,410,662,400` and 43 MB a day — map §7 item 167; `9,297,801` and `14,140,406` — map §6, GitHub Releases; `451` and `1ab40f4b…` — `research/tz43-l0-our-quote.py` line 160; `60,078` of `60,089`, `0.1437`, `217313280`, `706996816` and `1779050648` — TZ-43's report; `239050752`, `380186624` and `454987776` — TZ-44's report; `8,659,635` — TZ-44 §10; the four rehearsal assets' bytes and SHA-256 — `research/tz43-l0-our-quote.py`, TZ-34's report's. **Computed by an implementation independent of the one under test:** rule W's `1351` lines and `9c8c1a34…`, and the synthetic day's 19 — the second implementation (§4.1), an identity of bytes; §1's seven touches — the second implementation's `Fraction` arithmetic, 7 of 7; the power, `9⁵/10⁵`, `19⁵/20⁵`, `99⁵/100⁵`, and `2⁻⁵` — exact rationals, by hand; the self-test's credit `100 × 2,400,000 / 488,400,000 × 4.98 / 86,400` — by hand, from the synthetic day's instants; the floors — sums of the artifacts' figures; the assets `23` and one a candidate — counted in C5. **Measured by the Architect, stated as measured:** §6's rates and peaks; §1's exploration, barred. **No expectation depends on a quantity this TZ measures:** the set's size, the money and the store's counts are printed, not expected, and where a check is wanted on them it is an inequality — G-BOOK's `99` in `100`, the projection's `3,000` s, a day's `60,000,000` bytes. |
| **C3** | shape of every diff | One file added, `research/tz45-l0-rule-w.py`, absent at `5192aff` (`git cat-file -e` exits 128); the report's path absent there too. **Committed lines replaced: none.** Of `research/tz43-l0-our-quote.py`'s 3,056 lines, 2,873 stand in Appendix A unchanged, by `difflib`'s matching blocks; of the twenty definitions taken from `research/tz44-l0-inputs-release.py`, 15 are identical, 4 equal after the three renames and `read_set` differs in one message — compared by their syntax trees' line ranges. The words "insertions only" appear nowhere but in this row. |
| **C4** | cost of every check | §6's table, at each population's upper bound and at the host's ratio `1.37`: `2 + 30 + 14 + 1,861 + 157 + 2 + 111 + 60 = 2,235` s of processor, under `3,600`, nothing sampled; the fail-fast bounds together `3,000 + 200 + 2 × 60 + 205 = 3,525` s, under `3,600` — the replay's population is the set's own bytes, not known before `fetch`, so its bound is the projection after 24 units and not a prediction. Each bound's derivation is beside it in §6. |
| **C5** | every count | `63` rows, `60` + `2` + `1` — counted by the instrument's own run at `5192aff`. `6` anchors, `4` re-derived. Host gate `11` — H1, H2 twice, H3, H4, H5 four times, memory, disk — and `9` at §3.14. `5` members, `3` non-members, `8` candidates to 2026-11-16. `96` slots a day; `288` polls a member-day at most, one every 300 s. `9` variants — 4, 4 and `central`. `22` files — 5 member days times four, with `set.json` and `reading.json`. Assets `23` and one a candidate day: the 22, the manifest, the archives — 28 to 31. Outputs of `pack` `2` and one a candidate day. `1351` lines — 150 markets times 9 and the book's one; `451` — 150 times 3 and one. `71` self-test checks — the `ok` calls of `mode_selftest`, counted in its syntax tree, and the run's own count. `12` prohibitions, `12` gates, `22` validation rows, `15` modes. `151` ref lines — `HEAD`, `main`, 20 branches, 43 pull heads, 54 and 27 archive tags, `tz-44-l0-inputs`, 2 annotated tags with their 2 peeled lines. `20` definitions from TZ-44's file. |
| **C6** | every population | G-REHEARSAL: the four assets' frames, 150 markets, each rule's variants. G-SET: the candidates from `1794182400` in order. G-BOOK: every `book` frame of a member's first token but a seed, over the five days. DETERMINISM: the first member day's first 24 slots; `pack`'s outputs. **L0-W: the five member days; a day's money is over every member of its selection, its least over the four `pess` variants less their hits, its most over the four `opt` variants; a hit is charged on every market-day in which the variant set a target.** The power and the false reading: five days taken as independent, named so. G-SOURCE: the 22 files. G-PACK and G-RESERVE: every name, open and listing of the candidate days' directories. G-UPLOAD, G-DOWNLOAD: the set's assets. G-STILL: the four units. §6's rates: the stand-in's 480 units and 24; its peaks: each run of each mode. §1's exploration: L0's eight member days, 1,200 member-days, `345,595` served polls; the 437 are the member-days whose selection read 20 shares or less. |
| **C7** | every signature and every behaviour | Read at `5192aff`, `research/tz27-pairbook-archive.py`. **`def credential():`** (725) — "reads the repository's credential and prints its source alone": it returns the token and `"the primary checkout's remote URL"` or the one `gh` holds; its docstring, "Only upload calls this; no message names the token". **`class GitHub:`** (559), `def __init__(self, token=None, api=API_BASE, uploads=UPLOAD_BASE, web=WEB_BASE):` — "anonymous where token is None"; `def upload(self, rid, name, path, nbytes):` (618) builds its request with `ctype=CONTENT_TYPE` (625), a global read at each call — so setting `tz27.CONTENT_TYPE` labels every asset `application/octet-stream`, where line 82 holds `"application/gzip"`. **`def upload_set(gh, rel, doc, root, log, wait_min=WAIT_MIN_S):`** (765) — `assert not beyond, "the Release holds assets outside the set…"`; "kept where it already matches, otherwise any asset under its name removed and the file sent again; at most UPLOAD_ATTEMPTS a file". **`def verify_release(gh, tag, doc, download=True):`** (685) — "G-UPLOAD, then G-DOWNLOAD where G-UPLOAD holds: (release, rows, missing, extra)". **`def release_reading(rel, tag, rows, missing, extra):`** (703) — its checks' names are §3.12's two quoted strings, `"no asset missing"` and `"every asset uploaded, its bytes and digest the set's"`. **`def ls_remote_tag(tag):`** (1139) — "The tag object and the commit it peels to, from origin". `UPLOAD_ATTEMPTS = 4`, `DOWNLOAD_ATTEMPTS = 3`, `WAIT_MAX_S = 900`, `API_TIMEOUT_S = 60`, `UPLOAD_TIMEOUT_S = 300`, `DOWNLOAD_TIMEOUT_S = 120` — lines 118 to 124; `UPLOAD_SETTLE_S = 120` — line 112; `UA = "btc-5m-twap-tz27"` — line 78; `class _FakeGitHub` — line 1550. `research/tz43-l0-our-quote.py` line 160, `REF = {"lines": 451, "digest": "1ab40f4b…"}`; `research/tz33-reward-book-capture.py` line 190, `STREAM_FLOOR = 7300000000`, and 192, `SLOT_STREAM_MAX = 100000000`. `upload_ready`, `store_path`, `HashingReader`, `json_bytes` and `forbid` are called by TZ-44's functions, taken verbatim (C3), and no sentence of this file describes them. **Every sentence about Appendix A's own functions names lines resolved from its syntax tree; what each does was proved by the self-test and the stand-in run, not read alone.** |
| **C8** | every cross-reference | **Map `2026-11-13-a`, each read in the clone:** §0; §2.5 — the idle stretch, seconds 15 to 590, and the pair book archive's run at 03:00:20 UTC; §2.6 — the store, its archive's run at 01:30:20 UTC, the reserve from `1794182400`, L0's reading, the exploration and rule W; §3; §6's rows named in the header; §7 items 115, 118 to 120, 124, 129, 131, 132, 137, 138, 140, 141, 143, 144, 149 to 157 and 162 to 167, each read in full against the sentence that cites it. **Contract:** §1 steps 1 to 4, §4.2, §5, §5.1, §8, §9. **CANON:** hard rules 2, 5, 14, 15 and 16; PART II, the L track; PART VI; §1.5; §1.7. **This file's own references** — §-numbers, gate names, log names and item numbers — resolved by text. **The Boss's words:** his request of 2026-11-13, "TZ-45 — W rule on the first five days starting 2026-11-09 (Map 2026-11-13-a, §2.6 and §7 item 164)", is the header's, character for character in its three references. **What this check found, and what was done:** item 155 asks the Architect to measure, before a second gate's rule is fixed, the member-days whose reward terms moved under the replay — it had not been measured. It was, on the eight read days (§1): on 156 of the 437 member-days rule W would quote the venue moved the terms inside the day, on 154 of them to a larger minimum size. **The rule and the engine were changed for it before sending** — rule W reads each poll's row and leaves a market whose terms moved; the `pess` variants are credited through the last confirming poll — the second implementation was written again for it, and every figure of §1, §4.1 and §6 is from the changed engine. Item 157 asks a summary line for every timing file §8 names: `rescore` now prints one. Item 163 left the venue's rule for Georgia "his to read": the Architect read it — the venue's own list restricts neither its API nor its interface there [read 2026-11-13 from the venue's documentation and help centre, not measured] — and the CANON revision delivered with this file moves the live step there; nothing of it is this TZ's. |

**What the session could not check, and the condition that stands in its place (CANON hard rule 13):**

- **The five days themselves** — reserved. Every rule that reads them was proved on days already read: the set's rules on the stand-in's six, one of them the non-member TZ-43 found; the replay and the terms on L0's eight. **How many markets rule W quotes, and how many of them the venue moves, on a day from 2026-11-09 is the reading's, printed.** A day's selection of no market at or under 20 shares, or a day on which every such market's terms move, reads a least of nothing: that is an answer, not a defect.
- **A poll's row on those days** — `terms_of` takes a minimum size and a maximum spread that the row states as numbers and treats any other as moved terms, so a row of another shape quotes nothing rather than stopping the run; `polls_of` stops on a row with no `market_competitiveness` or `rewards_config`, as TZ-43's did on nine days.
- **The host's rates** — §6's are the Architect's at a ratio of `1.37`; the replay projects its own after 24 units and BLOCKS above `3,000` s.
- **The host's peaks** — §0.4's floor is twice the Architect's bound modelled at TZ-37's ratio; every mode prints its peak, and V19 sets it beside the model.
- **GitHub's own behaviour** — the session is refused this repository's Release API (map §6, GitHub Releases), so the request path ran against TZ-27's `_FakeGitHub` alone; G-TAG, G-UPLOAD and G-DOWNLOAD assert what a Release must then be, anonymously. TZ-44's run on the host proved the same path on 47 assets.
- **The credential in the Boss's shell** — `upload` stops with `UPLOAD REFUSED` where there is none.
- **The Boss's terminal** — a marker it may write into a log's first line (map §7 item 138) moves nothing: §3.11's block counts `run begun` and `exit=` lines, each on a line of its own.
- **The store's state at the run, the host's memory and disk, the classifier** — §0.0's read and `fetch`'s rule; §0.3's gates and each mode's floor reads; each block it may refuse has its paste.

---

## Appendix A — the instrument, byte for byte

`research/tz45-l0-rule-w.py` — 4,230 lines, 229,313 bytes, SHA-256 `1d415754615a1c037d0b9f695bbff4b3a246ddc62868d50e9e9448ccc55f7484`. §0.1's script extracts it; nothing below the fence's last line is part of it.

```python file=research/tz45-l0-rule-w.py
#!/usr/bin/env python3
"""TZ-45 - L0's second rule, rule W, on days no one has read: does a two-sided quote of ours at a reward market's
minimum size, alone inside the band of a wide touch, simulated on the reward book's streams, collect more in
liquidity rewards and maker rebates than its fills lose - and the reading's inputs, published as a Release.

    fingerprint       contract section 1 steps 3 and 4, asserted: the map's revision, anchors and rows
    number            CANON hard rule 2: no other TZ-45 specification or report on origin/main
    selftest          every rule of this file, on literals, on synthetic streams, on temporary trees and on TZ-27's
                      loopback GitHub
    still             the four units' MainPID, NRestarts and ActiveState: the first run records them, the second
                      compares, the pair book archive's own restarts read from its ledger (G-STILL)
    scratch OWN       the UUID directories beside OWN, this session's, each named live or earlier
    archive           the reward book archive's ledger and the set.json of every complete run, read and printed
    rehearse          four of the archive's first assets replayed twice under fixed parameters, every unit held:
                      TZ-43's rule against TZ-43's own lines, then rule W against the Architect's second
                      implementation of it (G-REHEARSAL)
    fetch             the candidate days from 2026-11-09, once the archive has moved them: each day's selection,
                      slot records, polls and fee schedules, the members' documents, and the set (G-SET)
    replay            every member day's slots downloaded, replayed and removed, every unit held; the days' money
                      on disk (G-BOOK)
    rescore           the set's first day's first slots replayed again, from a second download (DETERMINISM)
    score             the reading from the replay's day files
    pack              the reading's inputs: one archive a candidate day of its selections, slot records and reward
                      polls, this run's own work files, the manifest and the Release's set (G-SOURCE, G-PACK,
                      G-RESERVE); a second run builds the same bytes (DETERMINISM)
    upload            B-UPLOAD, the Boss's block: the Release on its tag at this file's commit, and its assets
    verify            G-TAG, G-UPLOAD and G-DOWNLOAD, with no credential
    reclaim TREE...   section 9

Its own code is the whole of the reading's arithmetic - the replay of a day's streams, every member market's book
rebuilt, our quote placed, queued, filled and cancelled at venue time, its reward share by the venue's published
formula, its rebate, its fills marked to the market and the adverse hit - TZ-43's, line for line but for rule W, the
decision a poll now calls, the terms a poll's row carries and the hit; and the reward book's record, the downloads
held to the pair book's idle stretch, the pack and G-STILL. It loads TZ-27's instrument from beside itself, by its SHA-256, for the Release's
client. Its requests: gamma-api.polymarket.com, the members' documents, in fetch alone; downloads of Release assets
from github.com; api.github.com and uploads.github.com in upload, and api.github.com and the download hosts in
verify; and git against origin. An audit hook refuses every open, listing, request and process TZ-45 section 2 does
not give the running mode. It writes under /root/tz45-work/ and, in reclaim, new files in /root/btc-forensics/ by
exclusive create. Exit 0: every assert of the mode held. Exit 1: an assert failed, and its message names it. Run it
with the recorder's interpreter, /root/tz04a-env.

Written for CryptoTZ/TZ-45-l0-rule-w.md. The TZ is the specification.
"""

import bisect
import collections
import ctypes
import datetime
import decimal
import gzip
import hashlib
import heapq
import http.client
import json
import os
import re
import resource
import shutil
import stat
import subprocess
import sys
import tarfile
import time
import types
import urllib.error
import urllib.parse
import urllib.request
import zlib
from decimal import Decimal as D
from fractions import Fraction as Fr

if not __debug__:
    sys.stderr.write("tz45: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(2)


def _malloc_tune():
    """glibc's mmap threshold at 128 KiB and two arenas, as TZ-23's and TZ-33's instruments fix them."""
    try:
        libc = ctypes.CDLL("libc.so.6")
        return libc.mallopt(-3, 131072) == 1 and libc.mallopt(-8, 2) == 1
    except OSError:
        return False


MALLOC_TUNED = _malloc_tune()
HERE = os.path.dirname(os.path.abspath(__file__))

# ---- the TZ's constants: none of them is measured by this run -----------------------------------------------

MAP_REVISION = "2026-11-13-a"
ANCHORS = {"A1": "229a944f2d51", "A2": "6c5089330629",
           "A3": "0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable",
           "A4": "437b45ea196b", "A5": "0f6c90451cbd", "A6": "729f0bcdbee3"}
ANCHOR_FILES = {"A2": "research/twap-divergence.py", "A4": "BTC-EXECUTOR-INSTRUCTIONS.md",
                "A5": "research/recorder/recorder.py", "A6": "research/pfair.py"}
MAP_ROWS = {"frozen": 60, "tracked": 2, "reported": 1}
ROW = re.compile(r"^\| `([^`]+)` \| ([0-9,]+|—) \| ([0-9,]+|—) \| (frozen|tracked|reported) \| "
                 r"(?:`([0-9a-f]{64})`|[^|]*) \|$", re.M)
ANCHOR_ROW = re.compile(r"^\| `(A[0-9])` — [^|]*\| `([^`]+)` \|$", re.M)
NUMBER = "TZ-45-"
OWN_TZ = "CryptoTZ/TZ-45-l0-rule-w.md"

DAY = 86400
SLOT = 900
SLOTS_A_DAY = 96
FIRST_D0 = 1794182400        # 2026-11-09 00:00:00 UTC: the first candidate day, the first of the reserve (map 2.6)
NEED = 5                     # member days: the reading's five blocks
NONMEMBER_MAX = 3            # the walk is BLOCKED past three non-member days before the fifth member
LAST_D0 = FIRST_D0 + (NEED + NONMEMBER_MAX - 1) * DAY    # 1794787200, 2026-11-16: the eighth candidate
GAP_MAX_NS = 15 * 10 ** 9    # no gap between received frames of a slot above 15 s
WAIT_MAX_S = 10800           # fetch waits at most three hours for the archive to reach a candidate day

# Rule W (TZ-45 section 1): on a member whose minimum size is at most 20 shares, while every served poll of the day
# has carried the selection's minimum size and maximum spread and the last one a competitiveness of at most 1, a bid
# and an ask W_BAND of twice the maximum spread apart, centred in a touch that leaves a tick on each side, neither
# more than 0.10 inside it; the position cap in minimum-size clips; the latency.
LATENCY_MS = 50
CAP_CLIPS = 1
W_MS_MAX = 2000              # hundredths of a share: 20 shares
W_COMP_MAX = Fr(1)           # the venue's competitiveness figure
W_BAND = (9, 10)             # the quote's width: the largest multiple of the tick at most 9/10 of twice the spread
W_INSIDE_MAX = 100           # thousandths: 0.10
SPREAD_TICKS = 5             # TZ-43's rule, `alone`: the baseline G-REHEARSAL and the self-test replay
# (name, rule, first in its level's queue, a crossing order a taker, the competitors' score). What the stream cannot
# show is bracketed corner by corner, because rule W's money is not monotone in the first two (TZ-45 section 1):
# the four whose competitors score the most are gated together for EARN, each less its adverse hits; the four whose
# competitors score the least for NO EARN; central, the venue's own figure, is barred.
VARIANTS = (("pess-bt", "w", False, True, "pess"), ("pess-br", "w", False, False, "pess"),
            ("pess-ft", "w", True, True, "pess"), ("pess-fr", "w", True, False, "pess"),
            ("opt-bt", "w", False, True, "opt"), ("opt-br", "w", False, False, "opt"),
            ("opt-ft", "w", True, True, "opt"), ("opt-fr", "w", True, False, "opt"),
            ("central", "w", False, True, "venue"))
BASE_VARIANTS = (("pess", "alone", False, True, "pess"), ("opt", "alone", True, False, "opt"),
                 ("central", "alone", False, True, "venue"))     # TZ-43's three, for its own lines (section 4.1)
DENOM_OF = {v[0]: v[4] for v in VARIANTS + BASE_VARIANTS}
EARN_FAMILY = tuple(v[0] for v in VARIANTS if v[4] == "pess")
NO_EARN_FAMILY = tuple(v[0] for v in VARIANTS if v[4] == "opt")
GATED = EARN_FAMILY + NO_EARN_FAMILY
THETA = D("10")              # USDC a day: EARN where every day's least gated figure reaches it, NO EARN where
#                              no day's most does
BOOK_EQUAL_MIN = Fr(99, 100) # G-BOOK: the rebuilt touch equals the venue's own at 99 in 100 of its book frames
REPLAY_CPU_MAX = 3000        # processor seconds the set's replay may take, projected after its first 24 units
RESCORE_CPU_MAX = 200
REHEARSAL_CPU_MAX = 60       # each of the rehearsal's two replays
PROJECT_AFTER = 24
UNIT_BUDGET_S = 45           # a unit's budget beside its download: replay and deletion
DL_RATE = 2000000            # bytes a second a download is budgeted at, TZ-28's
DL_TRIES = 6
DOC_BUDGET_S = 120           # a document request's budget in the idle stretch
STORE_BUDGET_S = 60          # a candidate day's read of the store's files, its selection, slots and polls
DOC_CHUNK = 50               # condition ids a gamma request carries: TZ-33's batch
IDLE = (15, 590)             # the pair book's idle stretch: a unit starts at second 15 or later, ends by 590
CALENDAR = ((5420, "the reward book archive's calendar run at 01:30:20 UTC"),
            (10820, "the pair book archive's calendar run at 03:00:20 UTC"))
CALENDAR_LEAD_S = 60
RUNNING = ("active", "activating", "deactivating", "reloading", "refreshing")
HOLD_MAX_S = 7200
PEAK_BOUND = 72000000        # bytes: the Architect's bound on any mode's peak, above the largest his runs gave
MEM_FLOOR = 172658448        # MemAvailable: twice that bound modelled at the host's ratio TZ-37 measured,
#                              58,953,728 / 49,168,384 (section 0.4)
MEM_RETRY_S = 60             # a MemAvailable read below the floor is read again this much later,
MEM_READS = 5                # five reads at most
DISK_FLOOR = 7400000000      # free bytes on /dev/vda2 once a unit's download lands: the reward book's STREAM_FLOOR,
#                              7,300,000,000, and one slot of its streams at the cut, 100,000,000 (section 0.4)
DISK_GATE = 7800000000       # free bytes at a mode's start: DISK_FLOOR and this session's tree twice over (section 0.4)

UA = "btc-5m-twap-tz45"
DL_HEADERS = {"User-Agent": UA, "Accept": "application/octet-stream"}
GAMMA_HEADERS = {"User-Agent": UA, "Accept": "application/json"}
REPO = "seahomebatumi-ai/btc-5m-twap"
DL_URL = "https://github.com/" + REPO + "/releases/download/%s/%s"
DL_HOSTS = ("github.com", "release-assets.githubusercontent.com", "objects.githubusercontent.com")
GAMMA_HOST = "gamma-api.polymarket.com"
GAMMA_URL = "https://gamma-api.polymarket.com/markets?%s"
ASSET_RE = re.compile(r"([0-9]{10})-(([0-9]{10})\.([0-9]+)\.stream\.jsonl\.gz)")
SLOT_FILE_RE = re.compile(r"([0-9]{10})\.([0-9]+)\.(stream\.jsonl\.gz|rewards\.jsonl\.gz|slot\.json)")
SELECT_FILE_RE = re.compile(r"select\.([0-9]+)\.(json|replies\.jsonl\.gz)")
CID_RE = re.compile(r"0x[0-9a-f]{64}")
TOKEN_RE = re.compile(r"[0-9]{1,100}")
SHA_RE = re.compile(r"[0-9a-f]{64}")

# G-REHEARSAL: four of the reward book archive's first Release's assets, their bytes and SHA-256 as TZ-34's report
# printed them, replayed as one stand-in hour under fixed parameters (TZ-45 section 4.1)
REHEARSAL_TAG = "rewardbook-streams-1793263627"
REHEARSAL_D0 = 1793232000
REHEARSAL_ASSETS = (
    ("1793232000-1793232000.0.stream.jsonl.gz", 11579610, "bafa2d5e0ed6293ab1a4a8466431db62100413766eac72c5c6a13d18a591271f"),
    ("1793232000-1793232900.0.stream.jsonl.gz", 10715152, "46076896c752257334186cf66c256d6c76685dccd274dbd7f6ab9d1b5917e370"),
    ("1793232000-1793233800.0.stream.jsonl.gz", 11443056, "2881148ced021d3c865fdc976183de94869fbe4876f9e70d3b6747394834a4a9"),
    ("1793232000-1793234700.0.stream.jsonl.gz", 13592154, "ca030bcb13717dd12c41d485f8abf83c1f8c4ac92fbef2625cbd6a6aecca9496"))
REHEARSAL_PARAMS = {"ms": 5000, "vu": 90, "rate": Fr(100), "fee": Fr(0)}   # 50 shares, 4.5 cents, 100 a day, no fee
REF_BASE = {"lines": 451, "digest": "1ab40f4b2a9b4f263e92959dc78a67dc9583731889cce70b22edad59091944cd"}   # TZ-43's REF
REHEARSAL_W = {"ms": 2000, "vu": 40, "rate": Fr(100), "fee": Fr(1, 80)}     # 20 shares, 2 cents, 100 a day, 1.25%
REF_W = {"lines": 1351, "digest": "9c8c1a343a5a95be0ade7c4a017ff51707fac11bb55d8d8904b1e20024f85bf6"}

WORK = "/root/tz45-work"
WT = WORK + "/wt"
STATE = WORK + "/state.json"
LEDGER = WORK + "/read-ledger.jsonl"
PRIMARY = "/root/btc-5m-twap"
REPORTS = PRIMARY + "/CryptoReports"
FORENSICS = "/root/btc-forensics"
BRANCH = "tz-45-l0-rule-w"
RB_ROOT = "/var/lib/btc-rewardbook"
RB_ARCHIVE = "/var/lib/btc-rewardbook-archive"
RB_LEDGER = RB_ARCHIVE + "/ledger.jsonl"
PB_ARCHIVE = "/var/lib/btc-pairbook-archive"
PB_LEDGER = PB_ARCHIVE + "/ledger.jsonl"
RECORDER = "/var/lib/btc-recorder"
PAIRBOOK = "/var/lib/btc-pairbook"
CHAINBOOK = "/var/lib/btc-chainbook"
ADVISOR = "/var/lib/adv3-bot"
ADVISOR_ETC = "/etc/adv3-bot"
UNITS = {"recorder": "btc-recorder.service", "pairbook": "btc-pairbook.service", "rewardbook": "btc-rewardbook.service",
         "advisor": "adv3-bot.service"}
ARCHIVES = {"pairbook": ("btc-pairbook-archive.service", "btc-pairbook-archive.timer"),
            "rewardbook": ("btc-rewardbook-archive.service", "btc-rewardbook-archive.timer")}
SHOW_ENV = {"TZ": "UTC", "LC_ALL": "C", "SYSTEMD_COLORS": "0", "SYSTEMD_PAGER": ""}
UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
TOKEN = re.compile(r"[0-9a-f]{16,64}")
LIVE_S = 60
PYFILE = "tz45-l0-rule-w.py"

# The Release of the reading's inputs (TZ-45 sections 3.10 to 3.12, CANON hard rule 16): TZ-44's pack, its names
TAG = "tz-45-l0-rule-w-inputs"
MANIFEST = "tz45-manifest.json"
ARCHIVE_FMT = "rewardbook-inputs-%d.tar"
CONTENT_TYPE = "application/octet-stream"
MEMBER_KINDS = ("select", "slot", "rewards")
KINDS = ("select", "slot", "rewards", "stream", "other")
DAY_MAX_BYTES = 60000000     # a day's members above this BLOCK: more than three times TZ-33's 16.3 MB a day
SOURCE_BUDGET_S = 60         # this run's own files, one unit of pack, are held for this many seconds
PACK_BASE_S = 30             # a day, one unit of pack, is held for this many seconds and for its members' bytes at
SCAN_RATE = 500000           # this many stored bytes a second: its scan of the replies, its archive and its hashes
SCANNED = ".jsonl.gz"        # a member of stored replies: scanned, and published only where no line withholds it
RATE_FLOOR = 2000000         # bytes a second a transfer is budgeted at, TZ-28's
MARGIN_S = 5                 # seconds every request is budgeted beyond its bytes, TZ-28's
UPLOAD_ROOT = "/root"
OUT = WORK + "/out"
RELEASE_SET = WORK + "/release-set.json"
UPLOAD_LOG = WORK + "/upload.jsonl"
TRANSFERS = WORK + "/transfers.jsonl"
VERIFY_FILE = WORK + "/verify.json"
SHA40 = re.compile(r"[0-9a-f]{40}")
TZ27_NAME = "tz27-pairbook-archive.py"
TZ27_SHA256 = "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673"

# ---- the audit hook: TZ-45 section 2's reads, writes, requests and processes -----------------------------

MODE = [None]
REFUSED = []
COUNTS = collections.Counter()
WRITE_FLAGS = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC
RB_SET = re.compile(re.escape(RB_ARCHIVE) + r"/runs/([0-9]{10})/set\.json")
RB_DAY = re.compile(re.escape(RB_ROOT) + r"/([0-9]{10})")
RB_FILE = re.compile(re.escape(RB_ROOT) + r"/([0-9]{10})/([0-9]{10}\.[0-9]+\.(?:slot\.json|rewards\.jsonl\.gz)|"
                     r"select\.[0-9]+\.(?:json|replies\.jsonl\.gz))")
PROCESSES = {"git", "systemctl", "stat"}
UPLOAD_PROCESSES = {"gh"}
HOSTS = {"upload": ("api.github.com", "uploads.github.com"),
         "verify": ("api.github.com", "github.com", "release-assets.githubusercontent.com",
                    "objects.githubusercontent.com"),
         "selftest": ("127.0.0.1",)}
PACK_DAYS = []               # the candidate days the set considered: pack fills it before it lists the store


class GuardError(RuntimeError):
    pass


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


def _path(p):
    if isinstance(p, bytes):
        p = os.fsdecode(p)
    return os.path.abspath(p) if isinstance(p, str) else None


def day_in_span(d0):
    return FIRST_D0 <= d0 <= LAST_D0 and (d0 - FIRST_D0) % DAY == 0


def store_day(mode, d0):
    """Whether a mode may read day d0 of the reward book's store: fetch the span's candidates, pack the days the set
    considered. Pure."""
    return (mode == "fetch" and day_in_span(d0)) or (mode == "pack" and d0 in PACK_DAYS)


def policy(mode, event, args):
    """None where TZ-45 section 2 allows the event in this mode; otherwise the reason it is refused."""
    if event == "urllib.Request":
        host = urllib.parse.urlsplit(args[0]).hostname if args and isinstance(args[0], str) else None
        if mode in ("rehearse", "replay", "rescore") and host in DL_HOSTS:
            return None
        if mode == "fetch" and host == GAMMA_HOST:
            return None
        if host in HOSTS.get(mode, ()):
            return None
        return "a request to %s" % host
    if event == "subprocess.Popen":
        exe = args[0] if args and args[0] else (args[1][0] if len(args) > 1 and args[1] else "")
        exe = os.path.basename(os.fsdecode(exe) if isinstance(exe, bytes) else str(exe))
        if exe in PROCESSES or (mode == "upload" and exe in UPLOAD_PROCESSES):
            return None
        return "a process %s" % exe
    p = _path(args[0]) if args else None
    if p is None:
        return None
    if event in ("os.listdir", "os.scandir"):
        if any(_under(p, r) for r in (RECORDER, CHAINBOOK, PAIRBOOK, PB_ARCHIVE, RB_ARCHIVE, ADVISOR, ADVISOR_ETC)):
            return "a listing under a capture root or an archive's state"
        if _under(p, RB_ROOT):
            m = RB_DAY.fullmatch(p)
            if m is not None and store_day(mode, int(m.group(1))):
                return None
            return "a listing under the reward book's root"
        return None
    wm, fl = (args[1] if len(args) > 1 else None), (args[2] if len(args) > 2 else None)
    w = _writing(wm, fl)
    if any(_under(p, r) for r in (RECORDER, CHAINBOOK, PAIRBOOK, ADVISOR, ADVISOR_ETC)):
        return "an open under a capture root or the advisor's"
    if _under(p, RB_ROOT):
        m = RB_FILE.fullmatch(p)
        if not w and m is not None and store_day(mode, int(m.group(1))):
            return None
        return "an open under the reward book's root"
    if _under(p, RB_ARCHIVE):
        if not w and mode in ("archive", "fetch", "still") and (p == RB_LEDGER or RB_SET.fullmatch(p)):
            return None
        return "an open under the reward book archive's state"
    if _under(p, PB_ARCHIVE):
        if not w and mode == "still" and p == PB_LEDGER:
            return None
        return "an open under the pair book archive's state"
    if _under(p, FORENSICS):
        if w:
            return None if mode == "reclaim" and _exclusive(wm, fl) else "a write into the forensic store"
        return None
    if w and not _under(p, WORK):
        return "a write outside the work tree"
    return None


def _audit(event, args):
    if event not in ("open", "os.listdir", "os.scandir", "urllib.Request", "subprocess.Popen"):
        return
    why = policy(MODE[0], event, args)
    if why is not None:
        REFUSED.append((event, str(args[0]) if args else ""))
        raise GuardError("%s refused in mode %s, %s: %r" % (event, MODE[0], why, args[0] if args else None))
    if event in ("open", "os.listdir", "os.scandir") and _under(_path(args[0]) or "", RB_ROOT):
        COUNTS["reward book opens" if event == "open" else "reward book listings"] += 1


sys.addaudithook(_audit)


def load_tz27(path):
    """TZ-27's instrument, executed from the very bytes whose SHA-256 is asserted; its own audit hook is installed
    then, and governs this process beside this file's."""
    with open(path, "rb") as fh:
        raw = fh.read()
    got = hashlib.sha256(raw).hexdigest()
    assert got == TZ27_SHA256, "%s sha256 %s, required %s" % (path, got, TZ27_SHA256)
    mod = types.ModuleType("tz27")
    mod.__file__ = path
    sys.modules["tz27"] = mod
    exec(compile(raw, path, "exec"), mod.__dict__)
    return mod


tz27 = load_tz27(os.path.join(HERE, TZ27_NAME))
tz27.WORK[0] = WORK                  # TZ-27's hook: every write and change inside this TZ's work tree
tz27.CONTENT_TYPE = CONTENT_TYPE     # TZ-27's upload reads it at each call: no asset is labelled gzip
assert tz27.REPO == REPO and tz27.UPLOAD_SETTLE_S == 120 and tz27.FORENSICS == FORENSICS, "TZ-27's constants"

# ---- small helpers ----------------------------------------------------------------------------------------


def out(msg):
    sys.stdout.write("[%s] %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    sys.stdout.flush()


def utc(t):
    return datetime.datetime.fromtimestamp(float(t), datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


C50 = decimal.Context(prec=50)        # every reward term and sum at 50 significant digits
Q12 = D("0.000000000001")


def q12(x):
    """A figure for print, half-even to 12 places; every sum and comparison is made on the exact figure."""
    if isinstance(x, Fr):
        x = C50.divide(D(x.numerator), D(x.denominator))
    s = format(D(x).quantize(Q12, rounding=decimal.ROUND_HALF_EVEN), "f")
    return "0.000000000000" if s.lstrip("-") == "0.000000000000" else s


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def write_atomic(path, data):
    tmp = path + ".tmp"
    with open(tmp, "wb") as fh:
        fh.write(data)
    os.replace(tmp, path)


def write_once(path, data):
    """The first run writes; a later run must produce the same bytes (contract section 6)."""
    if os.path.exists(path):
        got = sha256_file(path)
        assert got == sha256_bytes(data), "determinism: %s differs from the first run" % path
        out("unchanged %s sha256 %s" % (path, got))
        return got
    write_atomic(path, data)
    out("wrote %s %d bytes sha256 %s" % (path, len(data), sha256_bytes(data)))
    return sha256_bytes(data)


def dumps(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), default=_dec) + "\n"


def _dec(o):
    if isinstance(o, D):
        return format(o, "f")
    if isinstance(o, Fr):
        return "%d/%d" % (o.numerator, o.denominator)
    raise TypeError(type(o))


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh, parse_float=D)


def load_state():
    return load_json(STATE) if os.path.exists(STATE) else {}


def save_state(st):
    write_atomic(STATE, (json.dumps(st, sort_keys=True, indent=1, default=_dec) + "\n").encode("utf-8"))


def jsonl_append(path, rec):
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, sort_keys=True) + "\n")


def jsonl_read(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as fh:
        return [json.loads(ln) for ln in fh if ln.strip()]


def write_same(path, data):
    """write_once, returning `wrote` or `unchanged`: pack counts its outputs by them."""
    if os.path.exists(path):
        got = sha256_file(path)
        assert got == sha256_bytes(data), "determinism: %s differs from the first run" % path
        out("unchanged %s %d bytes sha256 %s" % (path, len(data), got))
        return "unchanged"
    write_atomic(path, data)
    out("wrote %s %d bytes sha256 %s" % (path, len(data), sha256_bytes(data)))
    return "wrote"


def record(key, doc):
    """state.json's record of what a mode wrote: G-SOURCE reads this run's files against it (TZ-45 section 4.6)."""
    st = load_state()
    st[key] = doc
    save_state(st)


def mem_available():
    with open("/proc/meminfo", encoding="ascii") as fh:
        for ln in fh:
            if ln.startswith("MemAvailable:"):
                return int(ln.split()[1]) * 1024
    raise AssertionError("no MemAvailable in /proc/meminfo")


def free_bytes(path="/var/lib"):
    st = os.statvfs(path)
    return st.f_bavail * st.f_frsize


def memory_gate(reads):
    """MemAvailable at a mode's reads, in order: the first, and one every MEM_RETRY_S after it while every read before
    fell below MEM_FLOOR, MEM_READS at most (map section 7 item 137). The last decides: (passes, it). Pure."""
    assert 1 <= len(reads) <= MEM_READS and all(r < MEM_FLOOR for r in reads[:-1]), reads
    return reads[-1] >= MEM_FLOOR, reads[-1]


def floor_check(read=None, sleep=None, freef=None):
    """Before a mode that reads the venue, the archive's Releases or the set: glibc's two settings, the memory floor -
    a read below it read again every MEM_RETRY_S, MEM_READS reads at most, the last deciding - and the disk floor."""
    read, sleep, freef = read or mem_available, sleep or time.sleep, freef or free_bytes
    assert MALLOC_TUNED, "BLOCKED: glibc did not take the mmap threshold and the arena count"
    reads, free = [read()], freef()
    out("MemAvailable %d bytes, floor %d; free %d bytes, floor %d" % (reads[0], MEM_FLOOR, free, DISK_GATE))
    while reads[-1] < MEM_FLOOR and len(reads) < MEM_READS:
        sleep(MEM_RETRY_S)
        reads.append(read())
        out("MemAvailable read %d of %d at most, %d s after a read below the floor: %d bytes" % (
            len(reads), MEM_READS, MEM_RETRY_S, reads[-1]))
    passes, final = memory_gate(reads)
    assert passes, "BLOCKED: MemAvailable %d bytes at read %d, every read below %d" % (final, len(reads), MEM_FLOOR)
    assert free >= DISK_GATE, "BLOCKED: %d bytes free, below %d" % (free, DISK_GATE)


def show(unit, props):
    args = ["systemctl", "show", unit]
    for prop in props:
        args += ["-p", prop]
    cp = subprocess.run(args, capture_output=True, text=True, env=dict(os.environ, **SHOW_ENV))
    assert cp.returncode == 0, "systemctl show %s: %s" % (unit, cp.stderr.strip())
    return dict(line.split("=", 1) for line in cp.stdout.split("\n") if "=" in line)


def git(*args, tree=WT):
    cp = subprocess.run(["git", "-C", tree] + list(args), capture_output=True, text=True)
    assert cp.returncode == 0, "git %s: %s" % (" ".join(args), cp.stderr.strip())
    return cp.stdout.strip()


def is_active(unit):
    cp = subprocess.run(["systemctl", "is-active", unit], capture_output=True, text=True)
    return cp.stdout.strip()


def budget_s(nbytes):
    """The seconds a request or a unit is held for: MARGIN_S, and its bytes at RATE_FLOOR, rounded up (TZ-28's)."""
    return MARGIN_S + -(-int(nbytes) // RATE_FLOOR)

# ---- the clock: the pair book's idle stretch and both archives' runs -----------------------------------------


def archives_state():
    return {k: is_active(svc) for k, (svc, _timer) in sorted(ARCHIVES.items())}


def quiet(now, budget, state_of=None):
    """None where a unit of `budget` seconds may start at `now`; otherwise why not: it starts inside the pair book's
    idle stretch and ends by its second 590, never near or during either archive's run."""
    state_of = state_of or archives_state
    p = int(now) % SLOT
    if not IDLE[0] <= p <= IDLE[1] - budget:
        return "second %d of the window" % p
    d = int(now) % DAY
    for at, what in CALENDAR:
        if at - budget - CALENDAR_LEAD_S <= d <= at + CALENDAR_LEAD_S:
            return what
    for k, st in sorted(state_of().items()):
        if st in RUNNING:
            return "the %s archive's service is %s" % (k, st)
    return None


def hold(budget, clock=None, sleep=None, state_of=None):
    """Until a unit of `budget` seconds may start; returns that instant and the seconds waited."""
    clock, sleep = clock or time.time, sleep or time.sleep
    assert budget <= IDLE[1] - IDLE[0], "a unit of %d s fits no idle stretch" % budget
    t0 = clock()
    while True:
        now = clock()
        why = quiet(now, budget, state_of)
        if why is None:
            return now, now - t0
        assert now - t0 <= HOLD_MAX_S, "BLOCKED: held %.0f s, the last reason %s" % (now - t0, why)
        sleep(1.0)

# ---- the reward book archive's record: its ledger, every complete run's set.json, every stream file's asset -------


def ledger_records(path):
    with open(path, "rb") as fh:
        raw = fh.read()
    lines = raw.split(b"\n")
    tail = lines.pop()
    return raw, [json.loads(ln) for ln in lines if ln.strip()], tail


def runs_of(recs):
    runs, order = {}, []
    for r in recs:
        a = r.get("run")
        if a not in runs:
            runs[a] = []
            order.append(a)
        runs[a].append(r)
    return runs, order


def archived_sets(recs, state=None):
    """Every run whose ledger holds a complete record: its set.json, asserted by the SHA-256 its last set record
    carries, its tag, assets and counts against that record."""
    state = state or RB_ARCHIVE
    runs, order = runs_of(recs)
    found = []
    for a in order:
        if "complete" not in [r.get("event") for r in runs[a]]:
            continue
        sets = [r for r in runs[a] if r.get("event") == "set"]
        assert sets and isinstance(a, int), "run %r: complete without a set record" % a
        with open(os.path.join(state, "runs", str(a), "set.json"), "rb") as fh:
            raw = fh.read()
        sha = sha256_bytes(raw)
        assert sha == sets[-1]["sha256"], "run %d: set.json sha256 %s, its set record %s" % (a, sha, sets[-1]["sha256"])
        doc = json.loads(raw)
        assert doc["tag"] == sets[-1]["tag"] and doc["assets_n"] == sets[-1]["assets_n"] == len(doc["assets"]) \
            and doc["bytes_total"] == sets[-1]["bytes_total"], "run %d: set.json against its set record" % a
        found.append({"run": a, "tag": doc["tag"], "sha256": sha, "doc": doc})
    return found


def asset_map(sets):
    """(D0, file) -> {tag, asset, bytes, sha256}, every stream file once; a file in two sets is a failed assert."""
    m = {}
    for s in sets:
        for x in s["doc"]["assets"]:
            mt = ASSET_RE.fullmatch(x["asset"])
            assert mt and int(mt.group(1)) == x["T"] and mt.group(2) == x["file"] and int(mt.group(3)) == x["S"] \
                and int(mt.group(4)) == x["k"] and x["T"] == x["S"] // DAY * DAY, "an asset named %r" % x["asset"]
            key = (x["T"], x["file"])
            assert key not in m, "%s in two sets" % x["asset"]
            m[key] = {"tag": s["tag"], "asset": x["asset"], "bytes": x["bytes"], "sha256": x["sha256"]}
    return m


def archived_to(state=None):
    """The asset map of every complete run and the last slot its assets reach."""
    state = state or RB_ARCHIVE
    _raw, recs, _tail = ledger_records(os.path.join(state, "ledger.jsonl"))
    amap = asset_map(archived_sets(recs, state))
    last = max(int(ASSET_RE.fullmatch(v["asset"]).group(3)) for v in amap.values()) if amap else 0
    return amap, last


def ledger_summary(recs):
    """The archive's runs from its own records: each run's set and terminal record, and whether it began on the
    calendar; whether the archive is halted."""
    runs, order = runs_of(recs)
    lines = []
    for a in order:
        rs = runs[a]
        ev = [r.get("event") for r in rs]
        term = [e for e in ev if e in ("complete", "empty", "halt")]
        sec = a % DAY if isinstance(a, int) else None
        when = "calendar" if sec == CALENDAR[0][0] else ("off-calendar, second %s of the day" % sec)
        parts = ["run %s %s, %s: %d records; terminal %s" % (a, utc(a) if isinstance(a, int) else "-", when, len(rs),
                                                            term[-1] if term else "none")]
        for r in [r for r in rs if r.get("event") == "set"][-1:]:
            parts.append("set %s: %s files, %s bytes, slots %s to %s" % (
                r.get("tag"), r.get("assets_n"), r.get("bytes_total"), r.get("first_S"), r.get("last_S")))
        for r in rs:
            if r.get("event") in ("deferred", "halt", "refused", "timer-disabled"):
                parts.append("%s in %s: %s" % (r.get("event"), r.get("phase"), r.get("reason", r.get("exit"))))
        lines.append("; ".join(parts))
    flags = [r.get("event") for r in recs if r.get("event") in ("halt", "clear")]
    return {"runs": order, "lines": lines, "halted": bool(flags) and flags[-1] == "halt",
            "terminal": {a: [r.get("event") for r in runs[a] if r.get("event") in ("complete", "empty", "halt")]
                         for a in order}}

# ---- the reward book's store: a day's selection, slot records and polls (fetch alone reads them) -----------------


def day_dir(d0, root=None):
    return os.path.join(root or RB_ROOT, str(d0))


def selection_of(d0, root=None):
    """The day's first ok attempt and its replies' bytes, asserted against its record (TZ-33's load_selection rule),
    with the SHA-256 of its select.<a>.json; None where the day holds none."""
    ddir = day_dir(d0, root)
    if not os.path.isdir(ddir):
        return None
    a = 0
    while True:
        jp, rp = (os.path.join(ddir, "select.%d.json" % a), os.path.join(ddir, "select.%d.replies.jsonl.gz" % a))
        if not os.path.exists(jp):
            if os.path.exists(rp):
                a += 1
                continue
            return None
        with open(jp, "rb") as fh:
            jraw = fh.read()
        rec = json.loads(jraw)
        if rec.get("ok") is True:
            with open(rp, "rb") as fh:
                rraw = fh.read()
            assert sha256_bytes(rraw) == rec["replies"]["sha256"], "%s: replies differ from their record" % rp
            return {"attempt": a, "rec": rec, "sha256": sha256_bytes(jraw), "replies": rraw}
        a += 1


def slot_records(d0, root=None):
    """S -> [slot.json of k = 0, 1, ...] for every slot of the day the store holds a record of, by its listing."""
    by = {}
    for name in sorted(os.listdir(day_dir(d0, root))):
        m = SLOT_FILE_RE.fullmatch(name)
        if m is None or m.group(3) != "slot.json":
            continue
        s, k = int(m.group(1)), int(m.group(2))
        with open(os.path.join(day_dir(d0, root), name), "rb") as fh:
            by.setdefault(s, {})[k] = json.loads(fh.read())
    return {s: [v[k] for k in sorted(v)] for s, v in by.items()}


def slot_problem(s, recs, sel_sha, n_members, assets, d0):
    """The first rule slot s fails, or None: its records consecutive from k = 0, each of the day's selection and
    every member, its stream opened and not cut, the first subscribed by S, the last's last frame at or after S + 900,
    no gap above 15 s within a file or between two, and every stream file in the archive's assets."""
    if not recs:
        return "no slot record"
    files = []
    for k, sj in enumerate(recs):
        if sj.get("S") != s or sj.get("index") != k or sj.get("day") != d0:
            return "records: index %d" % k
        if (sj.get("selection") or {}).get("sha256") != sel_sha or sj.get("markets") != n_members:
            return "records: another selection"
        if sj.get("error") is not None:
            return "records: an error"
        st = sj.get("stream") or {}
        if st.get("opened") is not True or st.get("off_reason") is not None or st.get("file") is None:
            return "stream: not opened"
        if st.get("cut") is not False:
            return "stream: cut"
        if st.get("file") != "%d.%d.stream.jsonl.gz" % (s, k):
            return "stream: its file"
        g = st.get("max_gap_ns")
        if not (type(g) is int and g <= GAP_MAX_NS):
            return "stream: a gap above 15 s"
        a, b = st.get("first_frame_wall_ns"), st.get("last_frame_wall_ns")
        if not (type(a) is int and type(b) is int and a <= b):
            return "stream: no frame"
        files.append((a, b, st["file"]))
    sub = (recs[0].get("stream") or {}).get("subscribed_wall_ns")
    if recs[0].get("joined_late") is not False or not (type(sub) is int and sub <= s * 10 ** 9):
        return "stream: subscribed late"
    if files[-1][1] < (s + SLOT) * 10 ** 9:
        return "stream: ended early"
    for (_a0, b0, _f0), (a1, _b1, _f1) in zip(files, files[1:]):
        if a1 - b0 > GAP_MAX_NS:
            return "stream: a gap above 15 s between files"
    for _a, _b, f in files:
        if (d0, f) not in assets:
            return "stream: not archived"
    return None


def fee_of(doc):
    """A member's maker rebate coefficient, the fee rate times the rebate rate, from its gamma document as the
    selection stored it: 0 where fees are not enabled or the schedule is not the venue's taker-only form."""
    if not isinstance(doc, dict) or doc.get("feesEnabled") is not True:
        return Fr(0)
    fs = doc.get("feeSchedule")
    if not isinstance(fs, dict) or fs.get("takerOnly") is not True or str(fs.get("exponent")) != "1":
        return Fr(0)
    return Fr(str(fs.get("rate"))) * Fr(str(fs.get("rebateRate")))


def gamma_docs_of(replies):
    """conditionId -> [documents] of every served gamma reply an attempt stored, numbers as Decimals of their text."""
    by = {}
    with gzip.open(__import__("io").BytesIO(replies), "rt", encoding="utf-8") as fh:
        for ln in fh:
            if not ln.strip():
                continue
            r = json.loads(ln)
            if r.get("kind") != "gamma" or r.get("status") != 200:
                continue
            for d in json.loads(r["raw"], parse_float=D):
                if isinstance(d, dict) and isinstance(d.get("conditionId"), str):
                    by.setdefault(d["conditionId"], []).append(d)
    return by


def members_of(sel):
    """The day's members as the replay takes them: condition id, its first token, the minimum size in hundredths of
    a share, the maximum spread in half-thousandths, the selection's daily rate and the rebate coefficient."""
    docs = gamma_docs_of(sel["replies"])
    out_ = []
    for m in sel["rec"]["members"]:
        cid, toks = m["condition_id"], m["token_ids"]
        assert CID_RE.fullmatch(cid) and len(toks) == 2 and all(TOKEN_RE.fullmatch(t) for t in toks), cid
        ms, vu = Fr(m["min_size"]) * 100, Fr(m["max_spread"]) * 20
        assert ms.denominator == 1 and vu.denominator == 1 and ms >= 0 and vu >= 0, "%s: size or spread" % cid
        fees = {fee_of(x) for x in docs.get(cid, [])}
        assert len(fees) == 1, "%s: %d fee terms in the selection's documents" % (cid, len(fees))
        out_.append({"cid": cid, "tok": toks[0], "ms": int(ms), "vu": int(vu), "rate": Fr(m["rate"]),
                     "fee": fees.pop()})
    return out_


_TERM = {}                   # a term's text and unit -> its Fraction: a day's polls repeat a few values


def terms_of(d):
    """A poll row's own terms: its minimum size in hundredths of a share and its maximum spread in half-thousandths,
    each the Fraction of its decimal text, or None where the row does not state it as a finite number."""
    out_ = []
    for x, k in ((d.get("rewards_min_size"), SIZE_UNIT), (d.get("rewards_max_spread"), 20)):
        if type(x) is int or (type(x) is D and x.is_finite()):
            key = (str(x), k)
            if key not in _TERM:
                _TERM[key] = Fr(key[0]) * k
            out_.append(_TERM[key])
        else:
            out_.append(None)
    return tuple(out_)


def polls_of(d0, recs_by_slot, root=None):
    """Every served poll of the day's slots, in the order received: (recv_ns, condition id, row), row None where the
    page held no row, else (the daily rate, the competitiveness, the row's minimum size, the row's maximum spread),
    each the Fraction of its decimal text - the rate the sum over the row's reward configurations in force on the
    poll's UTC date, from start_date to end_date; the last two as terms_of gives them."""
    polls, counts = [], collections.Counter()
    for s in sorted(recs_by_slot):
        for sj in recs_by_slot[s]:
            f = (sj.get("rewards") or {}).get("file")
            if f is None:
                continue
            with gzip.open(os.path.join(day_dir(d0, root), f), "rt", encoding="utf-8") as fh:
                for ln in fh:
                    if not ln.strip():
                        continue
                    r = json.loads(ln)
                    counts["polls"] += 1
                    if r.get("status") != 200 or r.get("raw") is None:
                        counts["unserved"] += 1
                        continue
                    data = json.loads(r["raw"], parse_float=D).get("data")
                    row = None
                    if data:
                        d = data[0]
                        day = utc(r["recv_wall_ns"] // 10 ** 9)[:10]
                        rate = sum((Fr(str(c["rate_per_day"])) for c in d["rewards_config"]
                                    if (c.get("start_date") is None or str(c["start_date"])[:10] <= day) and
                                    (c.get("end_date") is None or day <= str(c["end_date"])[:10])), Fr(0))
                        row = (rate, Fr(str(d["market_competitiveness"]))) + terms_of(d)
                    else:
                        counts["no row"] += 1
                    polls.append((r["recv_wall_ns"], sys.intern(r["condition_id"]), row))
    polls.sort(key=lambda p: (p[0], p[1]))
    return polls, counts

# ---- the replay: one UTC day of the reward book's streams, our quote on every member (TZ-45 section 1) -------------

MS_NS = 10 ** 6
S_NS = 10 ** 9
PRICE_UNIT = 1000            # a price as an integer of thousandths
SIZE_UNIT = 100              # a size as an integer of hundredths of a share
STALE_NS = S_NS              # a market's pending order events are resolved once any line's host instant passes them by 1 s
INSIDE = (200, 1800)         # the qualifying midpoint, in half-thousandths, inside [0.10, 0.90]: one side scores a third
SEND, CANCEL = 0, 1
ZERO = (0, 1)
NEVER = 1 << 62

_PRICE = re.compile(r"(0|[1-9][0-9]*)(?:\.([0-9]{1,3}))?")
_SIZE = re.compile(r"(0|[1-9][0-9]*)(?:\.([0-9]{1,2}))?")
_PRICES, _SIZES = {}, {}


def price_int(s):
    v = _PRICES.get(s)
    if v is None:
        m = _PRICE.fullmatch(s)
        assert m, "a price %r" % (s,)
        v = _PRICES[s] = int(m.group(1)) * PRICE_UNIT + int((m.group(2) or "").ljust(3, "0"))
    return v


def size_int(s):
    v = _SIZES.get(s)
    if v is None:
        m = _SIZE.fullmatch(s)
        assert m, "a size %r" % (s,)
        v = int(m.group(1)) * SIZE_UNIT + int((m.group(2) or "").ljust(2, "0"))
        if len(_SIZES) < 1 << 16:
            _SIZES[s] = v
    return v


# A price_change frame as the venue sends it and the reward book stores it, matched whole: two entries, each field a
# run of digits, hex or BUY/SELL, where no escape can occur (TZ-30's and TZ-32's PC_LINE).
_ENTRY = (r'\{\\"asset_id\\":\\"([0-9]+)\\", \\"price\\":\\"([0-9.]+)\\", \\"size\\":\\"([0-9.]+)\\", '
          r'\\"side\\":\\"(BUY|SELL)\\", \\"hash\\":\\"[0-9a-f]*\\", \\"best_bid\\":\\"[0-9.]+\\", '
          r'\\"best_ask\\":\\"[0-9.]+\\"\}')
PC_LINE = re.compile(r'\{"recv_ns":([0-9]+),"mono_ns":-?[0-9]+,"raw":"\{\\"market\\":\\"(0x[0-9a-f]{64})\\", '
                     r'\\"price_changes\\":\[' + _ENTRY + ', ' + _ENTRY + r'\], \\"timestamp\\":\\"([0-9]+)\\", '
                     r'\\"event_type\\":\\"price_change\\"\}"\}\n?')


class Order:
    __slots__ = ("side", "p", "s", "q", "state", "done_at", "xc", "fill_vt")

    def __init__(self, side, p, s):
        self.side, self.p, self.s, self.q = side, p, s, None
        self.state = "sent"        # sent, resting, filled, cancelled, refused
        self.done_at = None        # the venue instant it left the book or was refused
        self.xc = 0                # the crossing size already counted against it
        self.fill_vt = None        # the venue instant of its last fill


class Spec:
    """A variant (TZ-45 section 1): its rule, its queue place, the crossing orders, the competitors' score."""
    __slots__ = ("name", "rule", "front", "takers", "denom", "L")

    def __init__(self, name, rule, front, takers, denom):
        assert rule in ("w", "alone", "touch") and denom in ("pess", "opt", "venue"), (rule, denom)
        self.name, self.rule, self.front, self.takers, self.denom = name, rule, front, takers, denom
        self.L = LATENCY_MS * MS_NS


SPECS = tuple(Spec(*v) for v in VARIANTS)
BASE_SPECS = tuple(Spec(*v) for v in BASE_VARIANTS)


def w_targets(bb, ba, tick, vu):
    """Rule W's bid and ask on a touch bb, ba - thousandths; vu twice the maximum spread in them - or (None, None):
    w the largest multiple of the tick at most 9/10 of vu; the touch at least w and two ticks wide; the bid the
    midpoint less half of w, floored to the tick's grid, the ask w above it; neither more than 0.10 inside the touch.
    Pure."""
    w = W_BAND[0] * vu // (W_BAND[1] * tick) * tick
    if w < tick or ba - bb < w + 2 * tick:
        return None, None
    tb = (bb + ba - w) // (2 * tick) * tick
    ta = tb + w
    if tb - bb > W_INSIDE_MAX or ba - ta > W_INSIDE_MAX:
        return None, None
    return tb, ta


class MV:
    """One market in one variant: our orders, their events, our fills, the host's knowledge, the reward."""
    __slots__ = ("sp", "live", "resting", "pend", "fills", "unknown", "x_known", "x", "cost", "rew", "share", "t",
                 "acc", "n", "scored_ns", "touch", "hit", "kept")

    def __init__(self, sp):
        self.sp = sp
        self.live = {"b": None, "a": None}
        self.resting = []
        self.pend = []
        self.fills = []
        self.unknown = []
        self.x_known = 0
        self.x = 0                 # hundredths of a share of the market's first token, + long
        self.cost = 0              # thousandths x hundredths: a bid filled at p costs +p f, an ask -p f
        self.rew = D(0)
        self.share = ZERO
        self.t = None              # the last instant the variant's clock reached
        self.acc = 0               # nanoseconds at the share in force, not yet added to the reward
        self.n = {"sent": 0, "cancels": 0, "refused": 0, "crossings": 0, "fills": 0}
        self.scored_ns = 0
        self.touch = None          # the qualifying touch of its last share; None: any entry can move it
        self.hit = 0               # thousandths: the day's largest distance of a target of rule W inside the touch
        self.kept = (D(0), 0)      # rule W: the reward and the scored time at the last poll that confirmed the terms


class Market:
    __slots__ = ("cid", "tok", "ms", "vu", "fee", "rate", "ven", "bids", "asks", "bp", "ap", "block", "bvt",
                 "touch0", "seeded", "mvs", "c", "shadow", "dirty", "dtouch", "wake", "tick", "lastmid", "comp",
                 "moved")

    def __init__(self, m, specs):
        self.cid, self.tok, self.ms, self.vu, self.fee = m["cid"], m["tok"], m["ms"], m["vu"], m["fee"]
        self.rate = (m["rate"].numerator, m["rate"].denominator)
        self.ven = (None, 1)       # the venue's score of every maker, x 12 over vu^2 * 100: none before a poll
        self.comp = None           # the last served poll's competitiveness: none before one, none after a page of no row
        self.moved = False         # rule W: a served poll's row carried another minimum size or maximum spread
        self.bids, self.asks, self.bp, self.ap = {}, {}, [], []
        self.block, self.bvt, self.touch0 = [], None, (None, None)
        self.seeded = False
        self.mvs = [MV(sp) for sp in specs]
        self.c = {"snapshots": 0, "touch_equal": 0, "book_equal": 0, "matches": 0}
        self.shadow = None
        self.dirty = False
        self.dtouch = None         # the touch the quoting rule last decided on
        self.wake = 0              # the first host instant the host learns of a fill, a refusal or a cancel
        self.tick = 10             # thousandths: the seed's tick_size, 0.01 until one is read
        self.lastmid = None        # twice the last midpoint of a two-sided book, in thousandths: the day's mark

    # -- the book ---------------------------------------------------------------------------------------------
    def set_level(self, side, p, s):
        bk, pl = (self.bids, self.bp) if side == "b" else (self.asks, self.ap)
        old = bk.get(p, 0)
        if s:
            if not old:
                bisect.insort(pl, p)
            bk[p] = s
        elif old:
            del bk[p]
            del pl[bisect.bisect_left(pl, p)]
        return old

    def replace(self, bids, asks):
        self.bids, self.asks = bids, asks
        self.bp, self.ap = sorted(bids), sorted(asks)

    def best(self, side):
        if side == "b":
            return self.bp[-1] if self.bp else None
        return self.ap[0] if self.ap else None

    def qual_best(self, side, ours):
        """The best displayed level whose size reaches the minimum size, or our own qualifying order's price."""
        ms = self.ms
        if side == "b":
            for p in reversed(self.bp):
                if self.bids[p] >= ms:
                    return p if ours is None or p > ours else ours
            return ours
        for p in self.ap:
            if self.asks[p] >= ms:
                return p if ours is None or p < ours else ours
        return ours

    def others(self, mid_u):
        """A and B: the displayed levels of at least the minimum size inside the band around mid_u, each side's sum
        of d^2 times size, over vu^2 * 100."""
        vu, ms = self.vu, self.ms
        A = 0
        lo = mid_u - vu                          # a bid scores where 2p > mid_u - vu
        i = len(self.bp) - 1
        while i >= 0:
            p = self.bp[i]
            if 2 * p <= lo:
                break
            s = self.bids[p]
            if s >= ms:
                d = vu - (mid_u - 2 * p)
                A += d * d * s
            i -= 1
        B = 0
        hi = mid_u + vu
        for p in self.ap:
            if 2 * p >= hi:
                break
            s = self.asks[p]
            if s >= ms:
                d = vu - (2 * p - mid_u)
                B += d * d * s
        return A, B

    def liquidation(self, x):
        """Thousandths x hundredths: the proceeds of selling x > 0 into the bids, or minus the cost of buying -x from
        the asks, the remainder beyond the book at 0 or at 1."""
        if x == 0:
            return 0
        if x > 0:
            left, val = x, 0
            for p in reversed(self.bp):
                f = min(left, self.bids[p])
                val += f * p
                left -= f
                if not left:
                    break
            return val
        left, val = -x, 0
        for p in self.ap:
            f = min(left, self.asks[p])
            val -= f * p
            left -= f
            if not left:
                break
        return val - left * PRICE_UNIT


def envelope(A, B, inside):
    """The competitors' score, x 12 over vu^2 * 100, from the displayed sides' sums A and B: (hi, lo), the most and
    the least the levels can score, split among makers in any way (TZ-45 section 1, the reward)."""
    m, M = min(A, B), max(A, B)
    if inside:
        return 4 * (2 * m + M), max(3 * (A + B), 4 * M)
    return 12 * m, 0


class Day:
    """The replay of one day's streams and polls (TZ-45 section 1). Members: dicts with cid, tok (the market's first
    token), ms (minimum size, hundredths), vu (maximum spread, half-thousandths), fee (Fraction: the fee rate times the
    rebate rate) and rate (the selection's daily rate, Fraction)."""

    def __init__(self, d0, members, specs=SPECS):
        self.d0, self.specs = d0, specs
        self.rule = specs[0].rule
        assert all(sp.rule == self.rule for sp in specs), "one rule a day"
        self.mk = [Market(m, specs) for m in members]
        self.by_cid = {M.cid: M for M in self.mk}
        assert len(self.by_cid) == len(self.mk), "a member twice"
        self.idx = {M.cid: i for i, M in enumerate(self.mk)}
        self.stale = []            # (tau, seq, market index)
        self.seq = 0
        self.live = False          # decisions, fills and rewards run from the day's first slot instant
        self.c = {"lines": 0, "frames": 0, "fast": 0, "skipped": 0, "polls": 0, "switches": 0, "subscribes": 0,
                  "closes": 0}

    # -- rewards ------------------------------------------------------------------------------------------------
    def integrate(self, M, t):
        for mv in M.mvs:
            self.integrate_one(M, mv, t)

    def integrate_one(self, M, mv, t):
        """The variant's clock advanced to t where t is later: the time passes at the share and the rate in force."""
        if mv.t is None:
            mv.t = t
        elif t > mv.t:
            mv.acc += t - mv.t
            mv.t = t

    def flush(self, M, mv):
        """The time at the share and the rate in force added to the reward: rate * share * dt / 86,400 s, a Decimal
        quotient at 50 significant digits, summed in order - before either changes."""
        if mv.acc:
            num, den = mv.share
            if num:
                rn, rd = M.rate
                if rn:
                    mv.rew = C50.add(mv.rew, C50.divide(D(rn * num * mv.acc), D(rd * den * DAY * S_NS)))
                mv.scored_ns += mv.acc
            mv.acc = 0

    def set_share(self, M, mv, sh):
        if sh != mv.share:
            self.flush(M, mv)
            mv.share = sh

    def refresh(self, M, ents=None, t=None):
        """Every variant's clock advanced to host instant t, then its share recomputed - or, given a frame's entries,
        only the shares an entry can move: a variant's with resting orders whose entries reach its band or its
        qualifying touch."""
        cache = {}
        for mv in M.mvs:
            if t is not None:
                self.integrate_one(M, mv, t)
            if ents is not None:
                if not mv.resting:
                    continue
                tch = mv.touch
                if tch is not None:
                    qb, qa = tch
                    lo, hi = qb + qa - M.vu, qb + qa + M.vu
                    for side, p, _s in ents:
                        if (2 * p > lo or p >= qb) if side == "b" else (2 * p < hi or p <= qa):
                            break
                    else:
                        continue
            self.set_share(M, mv, self.share_of(M, mv, cache))

    def share_of(self, M, mv, cache):
        """Our share of the market's score at this instant, as (numerator, denominator); (0, 1) where we score
        nothing. `cache` keeps, for one book state, each set of our resting orders' parts."""
        if not M.seeded or not mv.resting:
            mv.touch = None
            return ZERO
        key = tuple((o.side, o.p, o.s) for o in mv.resting)
        parts = cache.get(key)
        if parts is None:
            parts = cache[key] = self.parts_of(M, mv.resting)
        if parts is None:
            mv.touch = None
            return ZERO
        touch, Q, hi, lo = parts
        mv.touch = touch
        if Q == 0:
            return ZERO
        vn, vd = M.ven
        den = mv.sp.denom
        if vn is None:
            O_n, O_d = (lo if den == "opt" else hi), 1
        elif den == "pess":
            O_n, O_d = (hi, 1) if hi * vd >= vn else (vn, vd)
        elif den == "opt":
            O_n, O_d = (lo, 1) if lo * vd <= vn else (vn, vd)
        else:
            O_n, O_d = vn, vd
        return (Q * O_d, Q * O_d + O_n)

    def parts_of(self, M, resting):
        """For one set of our resting orders on the book as it stands: the qualifying touch, our score Q and the
        competitors' hi and lo, all x 12 over vu^2 * 100; None where no qualifying touch exists."""
        ms, vu = M.ms, M.vu
        ob = oa = None
        for o in resting:
            if o.s >= ms:
                if o.side == "b":
                    ob = o.p if ob is None or o.p > ob else ob
                else:
                    oa = o.p if oa is None or o.p < oa else oa
        if ob is None and oa is None:
            return None
        qb, qa = M.qual_best("b", ob), M.qual_best("a", oa)
        if qb is None or qa is None or qb >= qa:
            return None
        mid_u = qb + qa
        q1 = q2 = 0
        for o in resting:
            if o.s < ms:
                continue
            su = (mid_u - 2 * o.p) if o.side == "b" else (2 * o.p - mid_u)
            if 0 <= su < vu:
                d = vu - su
                if o.side == "b":
                    q1 += d * d * o.s
                else:
                    q2 += d * d * o.s
        inside = INSIDE[0] <= mid_u <= INSIDE[1]
        Q = 4 * max(3 * min(q1, q2), max(q1, q2)) if inside else 12 * min(q1, q2)
        if Q == 0:
            return ((qb, qa), 0, 0, 0)
        hi, lo = envelope(*M.others(mid_u), inside)
        return ((qb, qa), Q, hi, lo)

    # -- our orders' events ---------------------------------------------------------------------------------------
    def push(self, mi, mv, tau, kind, o):
        self.seq += 1
        heapq.heappush(mv.pend, (tau, self.seq, kind, o))
        heapq.heappush(self.stale, (tau, self.seq, mi))

    def resolve(self, M, before):
        """Every variant's events of M due before `before`, in their order; the reward integrated to each."""
        for mv in M.mvs:
            P = mv.pend
            while P and P[0][0] < before:
                tau, _s, kind, o = heapq.heappop(P)
                self.integrate_one(M, mv, tau)
                if kind == SEND:
                    opp = M.best("a" if o.side == "b" else "b")
                    if opp is not None and (o.p >= opp if o.side == "b" else o.p <= opp):
                        o.state, o.done_at = "refused", tau
                        mv.n["refused"] += 1
                        if tau + mv.sp.L < M.wake:
                            M.wake = tau + mv.sp.L
                    else:
                        o.q = 0 if mv.sp.front else (M.bids if o.side == "b" else M.asks).get(o.p, 0)
                        o.state = "resting"
                        mv.resting.append(o)
                elif o.state in ("sent", "resting"):
                    o.state, o.done_at = "cancelled", tau
                    if tau + mv.sp.L < M.wake:
                        M.wake = tau + mv.sp.L
                    mv.resting = [x for x in mv.resting if x.state == "resting"]
                self.set_share(M, mv, self.share_of(M, mv, {}))

    def resolve_stale(self, h):
        S = self.stale
        lim = h - STALE_NS
        while S and S[0][0] < lim:
            tau, _s, mi = heapq.heappop(S)
            M = self.mk[mi]
            if M.block:
                self.close_block(M, False)
            self.resolve(M, tau + 1)

    # -- fills ----------------------------------------------------------------------------------------------------
    def fill(self, M, mv, o, vt, f, kind):
        M.dirty = True
        if vt + mv.sp.L < M.wake:
            M.wake = vt + mv.sp.L
        o.s -= f
        o.fill_vt = vt
        mv.fills.append((vt, o.side, o.p, f, kind))
        dx = f if o.side == "b" else -f
        mv.x += dx
        mv.cost += dx * o.p
        heapq.heappush(mv.unknown, (vt, dx))
        mv.n["fills"] += 1
        if o.s == 0:
            o.state, o.done_at = "filled", vt

    def known_x(self, mv, h):
        u = mv.unknown
        while u and u[0][0] + mv.sp.L <= h:
            mv.x_known += heapq.heappop(u)[1]
        return mv.x_known

    def sweep(self, M, side, t0):
        """A match's sweep of one side from its touch before the block: [(price, size taken)], best first, through
        the last level it reached."""
        cur = M.bids if side == "b" else M.asks
        first, dec = {}, {}
        for sd, p, old, new in M.block:
            if sd != side:
                continue
            if p not in first:
                first[p] = old
            dec[p] = first[p] - new
        if t0 is None or dec.get(t0, 0) <= 0:
            return []
        levels = sorted((p for p in set(first) | set(cur) if (p <= t0 if side == "b" else p >= t0)),
                        reverse=(side == "b"))
        sw = []
        for p in levels:
            pre = first[p] if p in first else cur.get(p, 0)
            if pre <= 0:
                continue
            c = dec.get(p, 0)
            if c <= 0:
                break
            sw.append((p, c))
            if c < pre:
                break
        return sw

    def close_block(self, M, match):
        """A block of entries with one venue stamp ends; where the venue's book frame of the same stamp followed it,
        a match: every resting order the sweep reached fills beyond its queue place."""
        if match and M.block:
            hit = 0
            for side, t0 in (("b", M.touch0[0]), ("a", M.touch0[1])):
                sw = self.sweep(M, side, t0)
                if not sw:
                    continue
                hit += 1
                last = sw[-1][0]
                at = dict(sw)
                for mv in M.mvs:
                    for o in mv.resting:
                        if o.side != side or o.state != "resting":
                            continue
                        f = 0
                        if (last <= o.p) if side == "b" else (last >= o.p):
                            tot = sum(c for p, c in sw if (p <= o.p if side == "b" else p >= o.p))
                            f = min(o.s, max(0, tot - o.q))
                        o.q = max(0, o.q - at.get(o.p, 0))
                        if f > 0:
                            self.fill(M, mv, o, M.bvt, f, "m")
                    mv.resting = [x for x in mv.resting if x.state == "resting"]
            if hit:
                M.c["matches"] += 1
        for mv in M.mvs:
            for o in mv.resting:
                lv = (M.bids if o.side == "b" else M.asks).get(o.p, 0)
                if lv < o.q:
                    o.q = lv
        t = M.bvt
        M.block, M.bvt = [], None
        self.cross(M, t)

    def cross(self, M, vt):
        """Where the opposite side reaches a resting order's price with no match, the orders there would have met
        ours: in a variant that counts them takers, our order fills at once for their size not yet counted."""
        bb, ba = M.best("b"), M.best("a")
        for mv in M.mvs:
            if not mv.sp.takers:
                continue
            gone = False
            for o in mv.resting:
                if o.state != "resting":
                    continue
                if o.side == "b":
                    c = sum(s for p, s in M.asks.items() if p <= o.p) if ba is not None and ba <= o.p else 0
                else:
                    c = sum(s for p, s in M.bids.items() if p >= o.p) if bb is not None and bb >= o.p else 0
                if c > o.xc:
                    f = min(o.s, c - o.xc)
                    mv.n["crossings"] += 1
                    self.fill(M, mv, o, vt, f, "x")
                    gone = gone or o.state != "resting"
                o.xc = c
            if gone:
                mv.resting = [x for x in mv.resting if x.state == "resting"]

    # -- the quoting rule -------------------------------------------------------------------------------------------
    def decide(self, M, h):
        """The quoting rule after a frame of the market reaches the host at h. Where the touch is the one it last
        decided on and the host has learned nothing since, it would decide the same, and returns."""
        if not (self.live and M.seeded):
            return
        bb, ba = M.best("b"), M.best("a")
        if (bb, ba) == M.dtouch and h < M.wake:
            return
        M.dtouch = (bb, ba)
        mi = self.idx[M.cid]
        for mv in M.mvs:
            cap = CAP_CLIPS * M.ms
            L = mv.sp.L
            x = None
            tb = ta = None
            if bb is not None and ba is not None:
                if mv.sp.rule == "alone":
                    if ba - bb >= SPREAD_TICKS * M.tick:
                        tb, ta = bb + M.tick, ba - M.tick
                elif mv.sp.rule == "w":
                    if M.ms <= W_MS_MAX and not M.moved and M.comp is not None and M.comp <= W_COMP_MAX:
                        tb, ta = w_targets(bb, ba, M.tick, M.vu)
                else:
                    tb, ta = bb, ba
            band = tb is not None and ta - tb < M.vu and M.ms > 0
            for side in ("b", "a"):
                o = mv.live[side]
                if o is not None and o.done_at is not None and o.done_at + L <= h:
                    o = mv.live[side] = None
                tgt = None
                if band:
                    tgt = tb if side == "b" else ta
                    if not 0 < tgt < PRICE_UNIT:
                        tgt = None
                if tgt is not None:
                    if x is None:
                        x = self.known_x(mv, h)
                    if x >= cap if side == "b" else x <= -cap:
                        tgt = None
                if tgt is not None and mv.sp.rule == "w":
                    dist = tgt - bb if side == "b" else ba - tgt
                    if dist > mv.hit:
                        mv.hit = dist
                stale = (o is not None and o.state == "resting" and o.fill_vt is not None and o.fill_vt + L <= h
                         and o.s < M.ms)
                if tgt is None:
                    if o is not None:
                        self.push(mi, mv, h + L, CANCEL, o)
                        mv.n["cancels"] += 1
                        mv.live[side] = None
                elif o is None:
                    n = Order(side, tgt, M.ms)
                    mv.live[side] = n
                    self.push(mi, mv, h + L, SEND, n)
                    mv.n["sent"] += 1
                elif o.p != tgt or stale:
                    self.push(mi, mv, h + L, CANCEL, o)
                    mv.n["cancels"] += 1
                    n = Order(side, tgt, M.ms)
                    mv.live[side] = n
                    self.push(mi, mv, h + L, SEND, n)
                    mv.n["sent"] += 1
        w = NEVER
        for mv in M.mvs:
            L = mv.sp.L
            for o in mv.live.values():
                if o is None:
                    continue
                for t in (o.done_at, o.fill_vt):
                    if t is not None and t + L < w:
                        w = t + L
            if mv.unknown and mv.unknown[0][0] + L < w:
                w = mv.unknown[0][0] + L
        M.wake = w

    # -- the stream ---------------------------------------------------------------------------------------------
    def session(self, ev, h, reason):
        """A session event of the live stream: every market's book cleared at a connect or subscribe; at a close
        other than the slot's end, every live order of ours cancelled."""
        if ev == "subscribe":
            self.c["subscribes"] += 1
        elif ev == "close" and reason != "end":
            self.c["closes"] += 1
        for M in self.mk:
            if M.block:
                self.close_block(M, False)
            self.resolve(M, h)
            self.integrate(M, h)
        if ev in ("connect", "subscribe"):
            for M in self.mk:
                M.replace({}, {})
                M.seeded = False
                self.refresh(M, None, h)
        elif ev == "close" and reason != "end":
            for mi, M in enumerate(self.mk):
                for mv in M.mvs:
                    for side in ("b", "a"):
                        o = mv.live[side]
                        if o is not None:
                            self.push(mi, mv, h + mv.sp.L, CANCEL, o)
                            mv.n["cancels"] += 1
                            mv.live[side] = None

    def poll(self, t, cid, row):
        """A served reward poll of a member: its daily rate and the venue's figure from then on; a page with no row
        stops the reward (rate 0). Under rule W the row's own minimum size and maximum spread are read too: the first
        row that carries another of either ends the market's quote and its reward for the day, and every variant but
        the opt family is credited only through the last poll whose row confirmed the selection's terms."""
        M = self.by_cid.get(cid)
        if M is None:
            return
        if self.live:
            if M.block:
                self.close_block(M, False)
            self.resolve(M, t)
            self.integrate(M, t)
            for mv in M.mvs:
                self.flush(M, mv)
        if self.rule == "w":       # rule W reads the row's own terms (TZ-45 section 1, the venue's terms)
            if row is not None and not M.moved and tuple(row[2:]) != (M.ms, M.vu):
                M.moved = True     # from this poll to the day's end: no quote, no reward
            for mv in M.mvs:
                if row is not None and not M.moved:
                    mv.kept = (mv.rew, mv.scored_ns)
                elif mv.sp.denom != "opt":
                    mv.rew, mv.scored_ns = mv.kept
        if row is None:
            M.rate, M.ven, M.comp = (0, 1), (None, 1), None
        else:
            rate, comp = (Fr(0) if M.moved else row[0]), row[1]
            M.rate = (rate.numerator, rate.denominator)
            v = comp * rate * M.vu * M.vu * SIZE_UNIT * 12
            M.ven = (v.numerator, v.denominator)
            M.comp = comp
        self.c["polls"] += 1
        if self.live:
            if self.rule == "w":   # rule W reads the poll: a decision at the poll's own host instant
                M.dtouch = None
                self.decide(M, t)
            self.refresh(M, None, t)

    def frame_items(self, fr, h, shadow):
        seed = isinstance(fr, list)
        touched = []
        for it in (fr if seed else (fr,)):
            if not isinstance(it, dict):
                continue
            M = self.by_cid.get(it.get("market"))
            if M is None:
                continue
            et = it.get("event_type")
            if et == "book":
                if it.get("asset_id") != M.tok:
                    continue
                bids = {}
                for lv in it["bids"]:
                    bids[price_int(lv["price"])] = size_int(lv["size"])
                asks = {}
                for lv in it["asks"]:
                    asks[price_int(lv["price"])] = size_int(lv["size"])
                bids = {p: s for p, s in bids.items() if s}
                asks = {p: s for p, s in asks.items() if s}
                ts = it.get("tick_size")
                if seed and ts in ("0.1", "0.01", "0.001"):
                    M.tick = price_int(ts)
                if shadow:
                    M.shadow = [bids, asks, True]
                    continue
                vt = int(it["timestamp"]) * MS_NS
                if M.block and vt != M.bvt:
                    self.close_block(M, False)
                self.resolve(M, vt)
                if seed:
                    if M.block:
                        self.close_block(M, False)
                    M.seeded = True
                else:
                    M.c["snapshots"] += 1
                    if M.block:
                        self.close_block(M, vt == M.bvt)
                    bb, ba = M.best("b"), M.best("a")
                    nb = max(bids) if bids else None
                    na = min(asks) if asks else None
                    if (bb, M.bids.get(bb), ba, M.asks.get(ba)) == (nb, bids.get(nb), na, asks.get(na)):
                        M.c["touch_equal"] += 1
                    if M.bids == bids and M.asks == asks:
                        M.c["book_equal"] += 1
                M.replace(bids, asks)
                for mv in M.mvs:
                    for o in mv.resting:
                        lv = (M.bids if o.side == "b" else M.asks).get(o.p, 0)
                        if lv < o.q:
                            o.q = lv
                self.cross(M, vt)
                touched.append((M, None))
            elif et == "tick_size_change":
                ts = it.get("new_tick_size")
                if it.get("asset_id") == M.tok and ts in ("0.1", "0.01", "0.001"):
                    M.tick = price_int(ts)
                    M.dtouch = None
            elif et == "price_change":
                ents = [(("b" if pc["side"] == "BUY" else "a"), price_int(pc["price"]), size_int(pc["size"]))
                        for pc in it["price_changes"] if pc.get("asset_id") == M.tok]
                if not ents:
                    continue
                if shadow:
                    self.shadow_apply(M, ents)
                    continue
                touched.append(self.entries(M, int(it["timestamp"]) * MS_NS, ents))
        return touched

    def shadow_apply(self, M, ents):
        sh = M.shadow
        if sh is None or not sh[2]:
            return
        for side, p, s in ents:
            bk = sh[0] if side == "b" else sh[1]
            if s:
                bk[p] = s
            else:
                bk.pop(p, None)

    def entries(self, M, vt, ents):
        if M.block and vt != M.bvt:
            self.close_block(M, False)
        self.resolve(M, vt)
        if not M.block:
            M.bvt = vt
            M.touch0 = (M.best("b"), M.best("a"))
        for side, p, s in ents:
            old = M.set_level(side, p, s)
            M.block.append((side, p, old, s))
        return (M, ents)

    def pc_fast(self, g, shadow):
        """A price_change line matched whole by PC_LINE: the same as frame_items on its parsed frame."""
        M = self.by_cid.get(g[1])
        if M is None:
            return None
        ents = [("b" if g[j + 3] == "BUY" else "a", price_int(g[j + 1]), size_int(g[j + 2])) for j in (2, 6)
                if g[j] == M.tok]
        if not ents:
            return None
        if shadow:
            self.shadow_apply(M, ents)
            return None
        return self.entries(M, int(g[10]) * MS_NS, ents)

    def after(self, tm, h):
        """After a frame of a market: the quoting rule, then the shares it can have moved."""
        M, ents = tm
        if M.bp and M.ap:
            M.lastmid = M.bp[-1] + M.ap[0]
        self.decide(M, h)
        if M.dirty:
            M.dirty = False
            self.refresh(M, None, h)
        else:
            self.refresh(M, ents, h)

    def switch(self, S_ns):
        """The slot's instant: every market's book becomes the one the new slot's file has built to it."""
        self.c["switches"] += 1
        for M in self.mk:
            if M.block:
                self.close_block(M, False)
            self.resolve(M, S_ns)
            self.integrate(M, S_ns)
            sh = M.shadow
            M.shadow = None
            if sh is None:
                M.replace({}, {})
                M.seeded = False
            else:
                M.replace(sh[0], sh[1])
                M.seeded = sh[2]
            for mv in M.mvs:
                for o in mv.resting:
                    lv = (M.bids if o.side == "b" else M.asks).get(o.p, 0)
                    if lv < o.q:
                        o.q = lv
            if M.seeded:
                self.cross(M, S_ns)
        self.live = True
        for M in self.mk:
            if M.bp and M.ap:
                M.lastmid = M.bp[-1] + M.ap[0]
            M.dtouch = None
            self.decide(M, S_ns)
            self.refresh(M, None, S_ns)

    def at_host(self, h, shadow, switched, S_ns, polls):
        if not shadow and not switched:
            self.switch(S_ns)
        if not shadow:
            while polls and polls[0][0] <= h:
                t, cid, row = polls.popleft()
                self.poll(t, cid, row)
            self.resolve_stale(h)
        return switched or not shadow

    def feed_slot(self, S, paths, polls):
        """Every line of slot S's stream files, in the order stored: lines received before S build each market's
        next book; from S to S + 900 they run the day; later lines belong to the next slot's file. `polls`: a deque
        of the day's served polls (recv_ns, condition id, row) in order, consumed from the front."""
        S_ns, E_ns = S * S_NS, (S + SLOT) * S_NS
        switched = False
        for M in self.mk:
            M.shadow = None
        for path in paths:
            with gzip.open(path, "rt", encoding="utf-8") as fh:
                for line in fh:
                    self.c["lines"] += 1
                    mt = PC_LINE.fullmatch(line)
                    if mt is not None:
                        g = mt.groups()
                        h = int(g[0])
                        if h >= E_ns:
                            continue
                        shadow = h < S_ns
                        switched = self.at_host(h, shadow, switched, S_ns, polls)
                        self.c["frames"] += 1
                        self.c["fast"] += 1
                        tm = self.pc_fast(g, shadow)
                        if tm is not None:
                            self.after(tm, h)
                        continue
                    if not line.strip():
                        continue
                    o = json.loads(line)
                    h = o.get("recv_ns")
                    assert type(h) is int, "a line without its host receipt"
                    if h >= E_ns:
                        continue
                    shadow = h < S_ns
                    switched = self.at_host(h, shadow, switched, S_ns, polls)
                    if "event" in o:
                        ev = o["event"]
                        if ev in ("connect", "subscribe", "close"):
                            if shadow:
                                if ev != "close":
                                    for M in self.mk:
                                        M.shadow = [{}, {}, False]
                            else:
                                self.session(ev, h, o.get("reason"))
                        continue
                    raw = o.get("raw")
                    if raw is None or raw == "PONG":
                        self.c["skipped"] += 1
                        continue
                    try:
                        fr = json.loads(raw)
                    except ValueError:
                        self.c["skipped"] += 1
                        continue
                    self.c["frames"] += 1
                    touched = self.frame_items(fr, h, shadow)
                    if not shadow:
                        for tm in touched:
                            self.after(tm, h)
        if not switched:
            self.switch(S_ns)
        while polls and polls[0][0] < E_ns:
            t, cid, row = polls.popleft()
            self.poll(t, cid, row)

    def finish(self, end_ns, outcomes):
        """The day's end: every event and reward integrated to it, every position valued at the market's last
        midpoint of the day - or at its outcome, where `outcomes` holds one (thousandths a share of the first token)
        - or, where the market never showed a two-sided book, by liquidation into the book as it stands."""
        rows = []
        for M in self.mk:
            if M.block:
                self.close_block(M, False)
            self.resolve(M, end_ns)
            self.integrate(M, end_ns)
            for mv in M.mvs:
                self.flush(M, mv)
            if self.rule == "w":   # but for the opt family, credited through the last poll that confirmed the terms
                for mv in M.mvs:
                    if mv.sp.denom != "opt":
                        mv.rew, mv.scored_ns = mv.kept
            mark = outcomes.get(M.cid)
            how = "outcome"
            if mark is None and M.lastmid is not None:
                mark, how = Fr(M.lastmid, 2), "mid"
            for mv in M.mvs:
                if mark is not None:
                    val = mv.x * Fr(mark)
                else:
                    val, how = Fr(M.liquidation(mv.x)), "book"
                reb = sum((M.fee * f * p * (PRICE_UNIT - p) for _vt, _sd, p, f, _k in mv.fills), Fr(0)) \
                    / (SIZE_UNIT * PRICE_UNIT * PRICE_UNIT)
                pnl = (val - mv.cost) / (SIZE_UNIT * PRICE_UNIT)
                rows.append({"cid": M.cid, "variant": mv.sp.name, "rew": mv.rew, "reb": reb, "pnl": pnl, "x": mv.x,
                             "cost": mv.cost, "mark": how, "fills": len(mv.fills),
                             "fill_hu": sum(f for _a, _b, _c, f, _d in mv.fills),
                             "crossed_hu": sum(f for _a, _b, _c, f, k in mv.fills if k == "x"),
                             "scored_ns": mv.scored_ns, "n": dict(mv.n)})
                if mv.sp.rule == "w":  # the adverse hit: one minimum size at the day's largest distance inside
                    rows[-1].update(hit_d=mv.hit, hit=M.ms * mv.hit)
        return rows

# ---- the set: the candidate days in order, each a member or not by TZ-45 section 1's rules --------------------------

RESCORE_SLOTS = 24           # the rescore replays the set's first day's first 24 slots (TZ-45 section 4.4)
DAY_FILE_KEYS = ("cid", "variant", "rew", "reb", "pnl", "x", "cost", "mark", "fills", "fill_hu", "crossed_hu",
                 "scored_ns", "n", "hit_d", "hit")


def fr_text(x):
    x = Fr(x)
    return "%d/%d" % (x.numerator, x.denominator)


def fr_of(s):
    n, d = s.split("/")
    return Fr(int(n), int(d))


def wait_archive(d0, t_start, clock=None, sleep=None, read=None):
    """Until the reward book archive's assets reach the last slot of day d0: its ledger read again every 60 s,
    BLOCKED once WAIT_MAX_S have passed since `t_start`. Returns the asset map."""
    clock, sleep, read = clock or time.time, sleep or time.sleep, read or archived_to
    amap, last = read()
    said = None
    need = d0 + DAY - SLOT
    while last < need:
        now = clock()
        assert now - t_start <= WAIT_MAX_S, "BLOCKED: the archive's assets reach slot %d, below %d, at %s" % (
            last, need, utc(now))
        if said is None or now - said >= 1800:
            out("the archive's assets reach slot %d (%s); day %d needs %d; its ledger read again every 60 s" % (
                last, utc(last) if last else "-", d0, need))
            said = now
        sleep(60)
        amap, last = read()
    return amap


def day_verdict(d0, amap, root=None):
    """One candidate day: (None, its record, its polls) where it is a member, else (the first reason it is not,
    None, None) - no selection; a slot without its records or failing a rule, the first such slot named."""
    sel = selection_of(d0, root)
    if sel is None:
        return "no selection", None, None
    members = members_of(sel)
    if not members:
        return "a selection of no market", None, None
    recs = slot_records(d0, root)
    slots = []
    for S in range(d0, d0 + DAY, SLOT):
        why = slot_problem(S, recs.get(S, []), sel["sha256"], len(members), amap, d0)
        if why is not None:
            return "slot %d (%s): %s" % (S, utc(S), why), None, None
        files = []
        for sj in recs[S]:
            a = amap[(d0, sj["stream"]["file"])]
            files.append({"file": sj["stream"]["file"], "tag": a["tag"], "asset": a["asset"], "bytes": a["bytes"],
                          "sha256": a["sha256"]})
        slots.append({"S": S, "files": files})
    polls, counts = polls_of(d0, {S: recs[S] for S in range(d0, d0 + DAY, SLOT)}, root)
    rec = {"d0": d0, "selection": {"attempt": sel["attempt"], "sha256": sel["sha256"], "members": len(members)},
           "members": [dict(m, rate=fr_text(m["rate"]), fee=fr_text(m["fee"])) for m in members], "slots": slots,
           "polls": {"n": len(polls), "polls": counts["polls"], "unserved": counts["unserved"],
                     "no_row": counts["no row"]}}
    return None, rec, polls


def polls_text(polls):
    return "".join(json.dumps([t, cid, None if row is None else [None if x is None else fr_text(x) for x in row]],
                              separators=(",", ":")) + "\n" for t, cid, row in polls)


class PollFile:
    """A member day's polls file read in order, one line at a time: the front poll as `[0]`, `popleft()`, truth while
    a poll is left, and iteration over the rest - a deque's interface, so that a day's polls are never all held."""

    def __init__(self, path):
        self.fh = open(path, encoding="utf-8")
        self.head = None
        self._advance()

    def _advance(self):
        ln = self.fh.readline() if self.fh is not None else ""
        if not ln:
            self.head = None
            if self.fh is not None:
                self.fh.close()
                self.fh = None
            return
        t, cid, row = json.loads(ln)
        self.head = (t, sys.intern(cid), None if row is None else tuple(None if x is None else fr_of(x) for x in row))

    def __bool__(self):
        return self.head is not None

    def __getitem__(self, i):
        assert i == 0 and self.head is not None, "PollFile: only the front poll"
        return self.head

    def popleft(self):
        assert self.head is not None, "PollFile: no poll left"
        h = self.head
        self._advance()
        return h

    def __iter__(self):
        while self.head is not None:
            yield self.popleft()


def polls_read(path):
    return PollFile(path)


def members_read(rec):
    return [dict(m, rate=fr_of(m["rate"]), fee=fr_of(m["fee"])) for m in rec["members"]]


def gamma_get(query, tries=DL_TRIES, sleep=None):
    sleep = sleep or time.sleep
    url = GAMMA_URL % query
    last = None
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers=GAMMA_HEADERS, method="GET")
            with urllib.request.urlopen(req, timeout=60) as r:
                body = r.read()
                assert r.status == 200, "HTTP %d" % r.status
            return json.loads(body, parse_float=D), len(body), sha256_bytes(body), k
        except urllib.error.HTTPError as e:
            last = "HTTP %d" % e.code
            if e.code not in (429, 500, 502, 503, 504):
                break
        except (urllib.error.URLError, http.client.HTTPException, TimeoutError, ConnectionError, OSError,
                ValueError) as e:
            last = "%s %s" % (type(e).__name__, e)
        sleep(min(60.0, 5.0 * 2 ** k))
    raise AssertionError("BLOCKED: gamma %s: %d attempts, the last %s" % (query[:80], tries, last))


def outcome_of(doc, tok):
    """The first token's outcome in thousandths, 1000 or 0, where the document reads the market closed with prices of
    exactly 0 and 1; otherwise None."""
    if doc.get("closed") is not True:
        return None
    try:
        prices, toks = json.loads(doc.get("outcomePrices")), json.loads(doc.get("clobTokenIds"))
    except (TypeError, ValueError):
        return None
    if sorted(map(str, prices)) != ["0", "1"] or len(toks) != 2 or tok not in toks:
        return None
    return PRICE_UNIT if str(prices[toks.index(tok)]) == "1" else 0


def documents(toks, holdf=None, get=None):
    """Every member's gamma document, read open and closed, DOC_CHUNK condition ids a request, each request held to
    the idle stretch; each member's document found exactly once, and only its outcome kept. Returns ({cid: outcome},
    requests)."""
    holdf, get = holdf or hold, get or gamma_get
    cids = sorted(toks)
    found, reqs = {}, []
    for i in range(0, len(cids), DOC_CHUNK):
        chunk = cids[i:i + DOC_CHUNK]
        for closed in (False, True):
            q = [("limit", 2 * DOC_CHUNK)] + [("condition_ids", c) for c in chunk] + (
                [("closed", "true")] if closed else [])
            holdf(DOC_BUDGET_S)
            docs, n, sha, k = get(urllib.parse.urlencode(q))
            assert isinstance(docs, list) and len(docs) <= len(chunk), "gamma: %d documents for %d ids" % (
                len(docs), len(chunk))
            reqs.append({"ids": len(chunk), "closed": closed, "bytes": n, "sha256": sha, "docs": len(docs),
                         "retries": k})
            for d in docs:
                cid = d.get("conditionId")
                assert cid in toks and cid not in found, "gamma: a document of %r" % cid
                found[cid] = outcome_of(d, toks[cid])
            del docs
    missing = sorted(set(cids) - set(found))
    assert not missing, "BLOCKED: no gamma document of %d members: %s" % (len(missing), missing[:3])
    return {c: found[c] for c in cids}, reqs


def mode_fetch():
    """The set (TZ-45 section 3.6): the candidate days in order from FIRST_D0, each read from the reward book's store
    and the archive's record once the archive has moved it, until NEED members; the members' documents; every
    candidate disclosed."""
    floor_check()
    os.makedirs(os.path.join(WORK, "fetch"), exist_ok=True)
    sp = os.path.join(WORK, "set.json")
    if os.path.exists(sp):
        s = load_json(sp)
        for d0 in s["members"]:
            got = sha256_file(os.path.join(WORK, "fetch", "%d.json" % d0))
            assert got == s["days"][str(d0)]["sha256"], "the set's day %d differs from its record" % d0
        out("the set is on disk: %s sha256 %s, %d members, every day's record unchanged" % (
            sp, sha256_file(sp), len(s["members"])))
        record("fetch", {"set_sha256": sha256_file(sp)})
        return
    assert time.time() >= FIRST_D0 + NEED * DAY, "BLOCKED: before the fifth candidate day has ended"
    t_start = time.time()
    considered, member_days, days = [], [], {}
    d0 = FIRST_D0
    while len(member_days) < NEED:
        assert d0 <= LAST_D0, "BLOCKED: %d non-member days before the fifth member, the bound %d" % (
            len(considered) - len(member_days), NONMEMBER_MAX)
        assert time.time() >= d0 + DAY, "BLOCKED: day %d (%s) has not ended; the set needs it" % (d0, utc(d0))
        amap = wait_archive(d0, t_start)
        hold(STORE_BUDGET_S)
        why, rec, polls = day_verdict(d0, amap)
        considered.append({"d0": d0, "member": why is None, "reason": why})
        if why is None:
            ptxt = polls_text(polls).encode("utf-8")
            rec["polls"]["sha256"] = write_once(os.path.join(WORK, "fetch", "%d.polls.jsonl" % d0), ptxt)
            body = dumps(rec).encode("utf-8")
            days[str(d0)] = {"sha256": write_once(os.path.join(WORK, "fetch", "%d.json" % d0), body),
                             "bytes": sum(f["bytes"] for s in rec["slots"] for f in s["files"]),
                             "files": sum(len(s["files"]) for s in rec["slots"]),
                             "members": len(rec["members"])}
            member_days.append(d0)
            out("candidate %d (%s): MEMBER %d of %d - %d markets, %d slots, %d stream files, %d bytes; polls %d "
                "served of %d, %d without a row" % (
                    d0, utc(d0), len(member_days), NEED, len(rec["members"]), len(rec["slots"]), days[str(d0)]["files"],
                    days[str(d0)]["bytes"], rec["polls"]["n"], rec["polls"]["polls"], rec["polls"]["no_row"]))
        else:
            out("candidate %d (%s): not a member - %s" % (d0, utc(d0), why))
        rec = polls = ptxt = body = None    # one day's polls held at a time
        d0 += DAY
    toks = {}
    for d in member_days:
        for m in load_json(os.path.join(WORK, "fetch", "%d.json" % d))["members"]:
            assert toks.get(m["cid"], m["tok"]) == m["tok"], "%s: two first tokens" % m["cid"]
            toks[m["cid"]] = m["tok"]
    outcomes, reqs = documents(toks)
    for r in reqs:
        out("gamma request: %d ids, closed %s, %d documents, %d bytes, sha256 %s, retries %d" % (
            r["ids"], r["closed"], r["docs"], r["bytes"], r["sha256"], r["retries"]))
    s = {"first_d0": FIRST_D0, "need": NEED, "considered": considered, "members": member_days, "days": days,
         "markets": len(toks), "outcomes": {c: v for c, v in sorted(outcomes.items()) if v is not None},
         "requests": reqs}
    sha = write_once(sp, dumps(s).encode("utf-8"))
    record("fetch", {"set_sha256": sha})
    out("G-SET PASS: %d members of %d candidates considered, %d to %d; %d distinct markets, %d resolved by their "
        "documents; %d stream files, %d bytes; set.json sha256 %s" % (
            len(member_days), len(considered), member_days[0], member_days[-1], len(toks), len(s["outcomes"]),
            sum(v["files"] for v in days.values()), sum(v["bytes"] for v in days.values()), sha))


def day_inputs(d0):
    """A member day's record and its polls, the polls file asserted by the SHA-256 its record carries."""
    rec = load_json(os.path.join(WORK, "fetch", "%d.json" % d0))
    path = os.path.join(WORK, "fetch", "%d.polls.jsonl" % d0)
    assert sha256_file(path) == rec["polls"]["sha256"], "day %d: its polls differ from its record" % d0
    return rec, polls_read(path)


def the_set():
    s = load_json(os.path.join(WORK, "set.json"))
    assert len(s["members"]) == NEED, "the set holds %d members" % len(s["members"])
    for d0 in s["members"]:
        got = sha256_file(os.path.join(WORK, "fetch", "%d.json" % d0))
        assert got == s["days"][str(d0)]["sha256"], "the set's day %d differs from its record" % d0
    return s

# ---- downloads: one Release asset, by its tag and name, verified by its bytes and SHA-256 ----------------------


def download(tag, asset, nbytes, sha, dest, url_of=None, tries=DL_TRIES, sleep=None):
    sleep = sleep or time.sleep
    url = (url_of or (lambda t, a: DL_URL % (urllib.parse.quote(t), urllib.parse.quote(a))))(tag, asset)
    last = None
    for k in range(tries):
        t0 = time.time()
        try:
            req = urllib.request.Request(url, headers=DL_HEADERS, method="GET")
            h, n = hashlib.sha256(), 0
            with urllib.request.urlopen(req, timeout=120) as r, open(dest + ".part", "wb") as fh:
                assert r.status == 200, "HTTP %d" % r.status
                while True:
                    b = r.read(1 << 20)
                    if not b:
                        break
                    h.update(b)
                    fh.write(b)
                    n += len(b)
            if n == nbytes and h.hexdigest() == sha:
                os.replace(dest + ".part", dest)
                return n, time.time() - t0, k
            last = "%d bytes sha256 %s, the set's %d %s" % (n, h.hexdigest(), nbytes, sha)
        except urllib.error.HTTPError as e:
            last = "HTTP %d" % e.code
            if e.code not in (403, 404, 429, 500, 502, 503, 504):
                break
        except (urllib.error.URLError, http.client.HTTPException, TimeoutError, ConnectionError, OSError) as e:
            last = "%s %s" % (type(e).__name__, e)
        if os.path.exists(dest + ".part"):
            os.remove(dest + ".part")
        sleep(min(60.0, 5.0 * 2 ** k))
    raise AssertionError("BLOCKED: %s/%s: %d attempts, the last %s" % (tag, asset, tries, last))

# ---- units: one slot held to the idle stretch, its streams downloaded, replayed and removed -------------------------


def run_unit(S, files, dl_dir, feed, timing, holdf=None, dl=None):
    """One slot: started where `holdf` allows, its stream files downloaded in index order and verified by bytes and
    SHA-256, fed to the day by `feed(paths)`, and removed whatever the replay did; its record appended to `timing`."""
    holdf, dl = holdf or hold, dl or download
    nbytes = sum(f["bytes"] for f in files)
    budget = 5 + -(-nbytes // DL_RATE) + UNIT_BUDGET_S
    start, waited = holdf(budget)
    free = free_bytes()
    assert free - nbytes >= DISK_FLOOR, "BLOCKED: %d bytes free, %d to download, the floor %d" % (
        free, nbytes, DISK_FLOOR)
    os.makedirs(dl_dir, exist_ok=True)
    paths, retries = [], 0
    t0 = time.time()
    try:
        for f in sorted(files, key=lambda f: int(SLOT_FILE_RE.fullmatch(f["file"]).group(2))):
            dest = os.path.join(dl_dir, f["asset"])
            _n, _secs, k = dl(f["tag"], f["asset"], f["bytes"], f["sha256"], dest)
            retries += k
            paths.append(dest)
        t1, c1 = time.time(), time.process_time()
        feed(paths)
        cpu = time.process_time() - c1
    finally:
        for p in paths:
            if os.path.exists(p):
                os.remove(p)
    end = time.time()
    W = int(start) // SLOT * SLOT
    rec = {"S": S, "window": W, "start_second": round(start - W, 3), "end_second": round(end - W, 3),
           "waited_s": round(waited, 3), "download_s": round(t1 - t0, 3), "replay_s": round(end - t1, 3),
           "cpu_s": round(cpu, 3), "bytes": nbytes, "retries": retries, "budget_s": budget,
           "inside": end <= W + IDLE[1]}
    with open(timing, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, sort_keys=True) + "\n")
    return rec


def timing_summary(path):
    recs = []
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            recs = [json.loads(ln) for ln in fh if ln.strip()]
    outside = [r for r in recs if not r["inside"]]
    if recs:
        out("units %d: inside the idle stretch %d, ending after second %d %d; longest %.1f s, download %.1f s and "
            "replay %.1f s at most; %.0f s waited; processor %.1f s; %d bytes downloaded; retries %d; windows %s to "
            "%s" % (len(recs), len(recs) - len(outside), IDLE[1], len(outside),
                    max(r["end_second"] - r["start_second"] for r in recs), max(r["download_s"] for r in recs),
                    max(r["replay_s"] for r in recs), sum(r["waited_s"] for r in recs),
                    sum(r["cpu_s"] for r in recs), sum(r["bytes"] for r in recs), sum(r["retries"] for r in recs),
                    utc(min(r["window"] for r in recs)), utc(max(r["window"] for r in recs))))
    for r in outside:
        out("unit %d started at second %.1f of window %d and ended at second %.1f" % (
            r["S"], r["start_second"], r["window"], r["end_second"]))
    return recs, outside


def slot_line(day, S):
    """A slot's record once the day has run to its end: the stream's counts, and each variant's sums over the
    members with a SHA-256 of every member's state - its position, cost, fills and reward."""
    c = day.c
    parts = ["%d lines %d frames %d fast %d skipped %d polls %d subscribes %d closes %d" % (
        S, c["lines"], c["frames"], c["fast"], c["skipped"], c["polls"], c["subscribes"], c["closes"])]
    for M in day.mk:
        for mv in M.mvs:
            day.flush(M, mv)
    for vi, sp in enumerate(day.specs):
        h = hashlib.sha256()
        nf = fhu = x = cost = 0
        rew = D(0)
        for M in day.mk:
            mv = M.mvs[vi]
            h.update(("%s %d %d %d %s\n" % (M.cid, mv.x, mv.cost, len(mv.fills), format(mv.rew, "f"))).encode())
            nf += len(mv.fills)
            fhu += sum(f for _a, _b, _c, f, _d in mv.fills)
            x += mv.x
            cost += mv.cost
            rew = C50.add(rew, mv.rew)
        parts.append("%s fills %d hu %d x %d cost %d rew %s state %s" % (sp.name, nf, fhu, x, cost, format(rew, "f"),
                                                                        h.hexdigest()[:16]))
    return " | ".join(parts)


def book_counts(day):
    book = {k: sum(M.c[k] for M in day.mk) for k in ("snapshots", "touch_equal", "book_equal", "matches")}
    book.update(subscribes=day.c["subscribes"], closes=day.c["closes"])
    return book


def day_rows_text(d0, rows, day):
    book = book_counts(day)
    doc = {"d0": d0, "counts": dict(day.c), "book": book,
           "rows": [{k: (format(r[k], "f") if k == "rew" else fr_text(r[k]) if k in ("reb", "pnl") else r[k])
                     for k in DAY_FILE_KEYS if k in r} for r in rows]}
    return dumps(doc).encode("utf-8")


def replay_day(d0, rec, polls, outcomes, dl_dir, timing, slots=None, holdf=None, dl=None, on_unit=None):
    """One member day replayed slot by slot; returns its slot lines and, where every slot ran, its rows."""
    day = Day(d0, members_read(rec))
    lines = []
    for s in rec["slots"][:slots]:
        u = run_unit(s["S"], s["files"], dl_dir, lambda paths, S=s["S"]: day.feed_slot(S, paths, polls), timing,
                     holdf, dl)
        lines.append(slot_line(day, s["S"]))
        if on_unit is not None:
            on_unit(u)
    if slots is not None and slots < len(rec["slots"]):
        return lines, None, day
    return lines, day.finish((d0 + DAY) * S_NS, {c: v for c, v in outcomes.items()}), day


class Projection:
    """After the first `after` units of this run, the replays' processor time projected over `total` bytes,
    BLOCKED above `cpu_max`."""

    def __init__(self, total, cpu_max, after=PROJECT_AFTER):
        self.total, self.cpu_max, self.after = total, cpu_max, after
        self.n, self.cpu, self.nb = 0, 0.0, 0

    def __call__(self, u):
        self.n += 1
        self.cpu += u["cpu_s"]
        self.nb += u["bytes"]
        if self.n == self.after:
            proj = self.cpu / self.nb * self.total
            out("projected %.0f s of replay for %d bytes after %d units at %.4f s a megabyte" % (
                proj, self.total, self.n, self.cpu / self.nb * 1e6))
            assert proj <= self.cpu_max, "BLOCKED: replay projected at %.0f s, above %d" % (proj, self.cpu_max)


def mode_replay():
    """Every member day not yet on disk, slot by slot (TZ-45 section 3.7); then G-BOOK over the days on disk."""
    floor_check()
    s = the_set()
    ddir = os.path.join(WORK, "days")
    os.makedirs(ddir, exist_ok=True)
    timing = os.path.join(WORK, "timing-replay.jsonl")
    todo = [d0 for d0 in s["members"] if not os.path.exists(os.path.join(ddir, "%d.json" % d0))]
    total = sum(s["days"][str(d0)]["bytes"] for d0 in todo)
    out("days to replay %d of %d, %d bytes of streams" % (len(todo), NEED, total))
    proj = Projection(total, REPLAY_CPU_MAX)
    for d0 in todo:
        rec, polls = day_inputs(d0)
        t0 = time.time()
        lines, rows, day = replay_day(d0, rec, polls, s["outcomes"], os.path.join(WORK, "dl"), timing, on_unit=proj)
        assert all(t >= (d0 + DAY) * S_NS for t, _c, _r in polls), "day %d: a poll left before its end" % d0
        st = write_once(os.path.join(ddir, "%d.slots.txt" % d0), ("\n".join(lines) + "\n").encode("utf-8"))
        sd = write_once(os.path.join(ddir, "%d.json" % d0), day_rows_text(d0, rows, day))
        out("day %d (%s) replayed in %.0f s: %d slots, %d lines; slots sha256 %s, day sha256 %s" % (
            d0, utc(d0), time.time() - t0, len(lines), day.c["lines"], st, sd))
        rec = polls = lines = rows = day = None    # one day held at a time
    timing_summary(timing)
    g_book(s)


def g_book(s):
    tot = collections.Counter()
    for d0 in s["members"]:
        b = load_json(os.path.join(WORK, "days", "%d.json" % d0))["book"]
        tot.update(b)
        out("day %d: book frames %d, the rebuilt touch equal at %d, every level equal at %d; matches %d; "
            "subscribes %d, closes %d" % (d0, b["snapshots"], b["touch_equal"], b["book_equal"], b["matches"],
                                          b["subscribes"], b["closes"]))
    ok = tot["snapshots"] > 0 and Fr(tot["touch_equal"], tot["snapshots"]) >= BOOK_EQUAL_MIN
    out("G-BOOK %s: the rebuilt touch equal to the venue's book frame at %d of %d frames, at least %s required; "
        "barred: every level equal at %d" % ("PASS" if ok else "FAIL", tot["touch_equal"], tot["snapshots"],
                                            BOOK_EQUAL_MIN, tot["book_equal"]))
    return ok


def mode_rescore():
    """DETERMINISM (TZ-45 section 4.4): the set's first day's first RESCORE_SLOTS slots replayed again from a second
    download; their lines equal the replay's."""
    floor_check()
    s = the_set()
    d0 = s["members"][0]
    with open(os.path.join(WORK, "days", "%d.slots.txt" % d0), encoding="utf-8") as fh:
        first = fh.read().split("\n")[:RESCORE_SLOTS]
    rec, polls = day_inputs(d0)
    total = sum(f["bytes"] for sl in rec["slots"][:RESCORE_SLOTS] for f in sl["files"])
    proj = Projection(total, RESCORE_CPU_MAX, after=6)
    lines, _rows, _day = replay_day(d0, rec, polls, s["outcomes"], os.path.join(WORK, "dl"),
                                    os.path.join(WORK, "timing-rescore.jsonl"), slots=RESCORE_SLOTS, on_unit=proj)
    write_once(os.path.join(WORK, "rescore.txt"), ("\n".join(lines) + "\n").encode("utf-8"))
    timing_summary(os.path.join(WORK, "timing-rescore.jsonl"))      # map section 7 item 157
    same = sum(1 for a, b in zip(lines, first) if a == b)
    out("DETERMINISM %s: %d of %d slot lines of day %d equal to the replay's" % (
        "PASS" if same == RESCORE_SLOTS == len(lines) else "FAIL", same, RESCORE_SLOTS, d0))

# ---- the reading: each day's money by variant, and L0's reading (TZ-45 section 4.5) ---------------------------------


def day_money(rows, name):
    """A day's money for one variant: the reward with the venue's 1-pUSD minimum, the rebate, the marks and the
    adverse hits. Where the competitors score the most, a member's reward is paid only where it reaches 1 on the day
    and no rebate is counted; where they score the venue's figure, the same and the rebate; where they score the
    least, the day's sum where it reaches 1 and the rebate. `gated` is the figure the reading takes: the total, less
    the hits where the competitors score the most."""
    den = DENOM_OF[name]
    rs = [r for r in rows if r["variant"] == name]
    rew = [D(r["rew"]) for r in rs]
    if den == "opt":
        tot = sum(rew, D(0))
        paid = tot if tot >= 1 else D(0)
    else:
        paid = sum((x for x in rew if x >= 1), D(0))
    reb = sum((fr_of(r["reb"]) for r in rs), Fr(0)) if den != "pess" else Fr(0)
    pnl = sum((fr_of(r["pnl"]) for r in rs), Fr(0))
    total = Fr(paid) + reb + pnl
    hits = Fr(sum(r.get("hit", 0) for r in rs), SIZE_UNIT * PRICE_UNIT)
    return {"reward": sum(rew, D(0)), "paid": paid, "rebate": reb, "marks": pnl, "total": total, "hits": hits,
            "gated": total - hits if den == "pess" else total,
            "quoting": sum(1 for r in rs if r.get("hit", 0) > 0),
            "markets": len(rs), "paying": sum(1 for x in rew if x >= 1), "fills": sum(r["fills"] for r in rs),
            "shares": Fr(sum(r["fill_hu"] for r in rs), SIZE_UNIT),
            "crossed": Fr(sum(r["crossed_hu"] for r in rs), SIZE_UNIT),
            "scored_h": Fr(sum(r["scored_ns"] for r in rs), 3600 * S_NS),
            "marks_by": dict(collections.Counter(r["mark"] for r in rs))}


def l0_reading(pess_days, opt_days, theta=THETA):
    """EARN where every day's least gated figure reaches theta, NO EARN where no day's most does, UNDECIDABLE
    otherwise; each false reading at most 2^-5 over five independent days (TZ-45 section 4.5). Pure."""
    assert len(pess_days) == len(opt_days) == NEED
    earn = all(t >= theta for t in pess_days)
    no_earn = all(t < theta for t in opt_days)
    word = "EARN" if earn and not no_earn else "NO EARN" if no_earn and not earn else "UNDECIDABLE"
    return word, earn, no_earn


def power(q, n=NEED):
    return Fr(q) ** n


def day_brackets(e_by):
    """A day's two gated figures: the least of the EARN family, each less its adverse hits, and the most of the
    NO EARN family - each with the variant that gives it. Pure."""
    return (min((e_by[n]["gated"], n) for n in EARN_FAMILY), max((e_by[n]["gated"], n) for n in NO_EARN_FAMILY))


def mode_score():
    floor_check()
    s = the_set()
    rows_by, inputs = {}, {}
    for d0 in s["members"]:
        pj, ps = (os.path.join(WORK, "days", "%d.%s" % (d0, x)) for x in ("json", "slots.txt"))
        rows_by[d0] = load_json(pj)["rows"]
        inputs[str(d0)] = {"day": sha256_file(pj), "slots": sha256_file(ps)}
    for name, q in (("0.90", Fr(9, 10)), ("0.95", Fr(19, 20)), ("0.99", Fr(99, 100))):
        out("power: every day's least at or above %s with probability %s each: %s" % (THETA, name, q12(power(q))))
    out("false reading: 2^-%d = %s for each answer, under independent days" % (NEED, q12(Fr(1, 2 ** NEED))))
    book = g_book(s)
    names = [v[0] for v in VARIANTS]
    res = {"days": {}, "variants": {}, "inputs": inputs, "least": {}, "most": {}}
    least, most = [], []
    for d0 in s["members"]:
        e_by = res["days"][str(d0)] = {name: day_money(rows_by[d0], name) for name in names}
        for name in names:
            e = e_by[name]
            out("day %d %-7s gated %s: total %s = paid %s of reward %s on %d of %d markets + rebate %s + marks %s; "
                "hits %s on %d quoting markets; fills %d, %s shares, %s against crossing orders; scored %s h; marks "
                "%s%s" % (d0, name, q12(e["gated"]), q12(e["total"]), q12(e["paid"]), q12(e["reward"]), e["paying"],
                          e["markets"], q12(e["rebate"]), q12(e["marks"]), q12(e["hits"]), e["quoting"], e["fills"],
                          q12(e["shares"]), q12(e["crossed"]), q12(e["scored_h"]), e["marks_by"],
                          "" if name in GATED else ", barred"))
        (lo, lo_n), (hi, hi_n) = day_brackets(e_by)
        least.append(lo)
        most.append(hi)
        res["least"][str(d0)], res["most"][str(d0)] = {"gated": lo, "variant": lo_n}, {"gated": hi, "variant": hi_n}
        out("day %d: the least of %s, each less its hits, %s (%s); the most of %s, %s (%s)" % (
            d0, "/".join(EARN_FAMILY), q12(lo), lo_n, "/".join(NO_EARN_FAMILY), q12(hi), hi_n))
    word, earn, no_earn = l0_reading(least, most)
    out("days whose least is at or above %s: %d of %d, the least %s; days whose most is below it: %d of %d, the most "
        "%s" % (THETA, sum(1 for t in least if t >= THETA), NEED, q12(min(least)),
                sum(1 for t in most if t < THETA), NEED, q12(max(most))))
    for name in names:
        tot = sum((res["days"][str(d0)][name]["gated"] for d0 in s["members"]), Fr(0))
        res["variants"][name] = {"gated": tot, "per_day": tot / NEED}
        out("%s: over the %d days %s, a day %s%s" % (name, NEED, q12(tot), q12(tot / NEED),
                                                     "" if name in GATED else ", barred"))
    res["reading"] = word if book else None
    res["g_book"] = "PASS" if book else "FAIL"
    sha = write_once(os.path.join(WORK, "reading.json"), dumps(res).encode("utf-8"))
    record("score", {"reading_sha256": sha})
    out("L0-W %s: EARN %s, NO EARN %s; reading.json sha256 %s" % (word if book else "not read, G-BOOK FAIL", earn,
                                                                 no_earn, sha))

# ---- G-REHEARSAL: four of the archive's first assets, replayed as one stand-in hour (TZ-45 section 4.1) ----------------


def rehearsal_members(path, params=REHEARSAL_PARAMS):
    """The markets of the first seed after the first subscribe of `path`, in order of first appearance, each with
    its first book item's token as its first token, under the rehearsal's fixed parameters."""
    seen, order = {}, []
    subscribed = False
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        for line in fh:
            o = json.loads(line)
            if o.get("event") == "subscribe":
                subscribed = True
                continue
            raw = o.get("raw")
            if not subscribed or raw is None or not raw.startswith("["):
                continue
            for it in json.loads(raw):
                if isinstance(it, dict) and it.get("event_type") == "book" and it.get("market") not in seen:
                    seen[it["market"]] = it["asset_id"]
                    order.append(it["market"])
            break
    assert order, "%s: no seed after a subscribe" % path
    return [{"cid": c, "tok": seen[c], "ms": params["ms"], "vu": params["vu"], "rate": params["rate"],
             "fee": params["fee"]} for c in order]


def compare_lines(rows, book):
    """The figures G-REHEARSAL and the self-test compare with the Architect's independent replay: per member and
    variant, in the members' order, every figure at twelve places or as an integer; then the book's counts."""
    lines = []
    for r in rows:
        n = r["n"]
        lines.append("%s %s rew %s reb %s pnl %s x %d cost %d fills %d hu %d crossed %d scored_ns %d sent %d "
                     "cancels %d refused %d crossings %d mark %s" % (
                         r["cid"], r["variant"], q12(r["rew"]), q12(r["reb"]), q12(r["pnl"]), r["x"], r["cost"],
                         r["fills"], r["fill_hu"], r["crossed_hu"], r["scored_ns"], n["sent"], n["cancels"],
                         n["refused"], n["crossings"], r["mark"]) + (
                             " hit_d %d hit %d" % (r["hit_d"], r["hit"]) if "hit" in r else ""))
    lines.append("book snapshots %d touch_equal %d book_equal %d matches %d subscribes %d closes %d" % tuple(
        book[k] for k in ("snapshots", "touch_equal", "book_equal", "matches", "subscribes", "closes")))
    return lines


def replay_paths(d0, members, slot_paths, end_s, polls=None, specs=None):
    """A stand-in day: every slot's local files, in order; its rows at end_s and the book's counts."""
    day = Day(d0, members, specs or SPECS)
    pq = collections.deque(polls or ())
    for S, paths in slot_paths:
        day.feed_slot(S, paths, pq)
    rows = day.finish(end_s * S_NS, {})
    return rows, book_counts(day), day


def rehearsal_polls(members, d0, slots=4):
    """Rule W reads each poll's row, and the stand-in hour takes none from the store: for slot j and member i a poll
    at S + 30 + i s - the rate 100 a day, the figure ((i + j) mod 5) / 2, so 0, 1/2, 1, 3/2 and 2, and the
    rehearsal's own minimum size and maximum spread - but in the third slot, for a member whose index is 3 mod 7, a
    page with no row; in the second slot, for an index that is 5 mod 11, a minimum size of 50 shares, the
    rehearsal's own again in the slots after it; and in the fourth slot, for an index that is 9 mod 13, a row that
    states no maximum spread. Pure."""
    own = (Fr(REHEARSAL_W["ms"]), Fr(REHEARSAL_W["vu"]))
    polls = []
    for j in range(slots):
        for i, m in enumerate(members):
            if j == 2 and i % 7 == 3:
                row = None
            else:
                terms = (Fr(5000), own[1]) if (j == 1 and i % 11 == 5) else \
                    (own[0], None) if (j == 3 and i % 13 == 9) else own
                row = (REHEARSAL_W["rate"], Fr((i + j) % 5, 2)) + terms
            polls.append(((d0 + j * SLOT + 30 + i) * S_NS, m["cid"], row))
    polls.sort(key=lambda p: (p[0], p[1]))
    return polls


def mode_rehearse():
    floor_check()
    dl_dir = os.path.join(WORK, "rehearsal-dl")
    os.makedirs(dl_dir, exist_ok=True)
    paths, done = [], []
    try:
        for name, nbytes, sha in REHEARSAL_ASSETS:
            dest = os.path.join(dl_dir, name)
            start, waited = hold(5 + -(-nbytes // DL_RATE) + 5)
            assert free_bytes() - nbytes >= DISK_FLOOR, "BLOCKED: the disk floor"
            n, secs, k = download(REHEARSAL_TAG, name, nbytes, sha, dest)
            out("downloaded %s: %d bytes in %.1f s, sha256 %s, retries %d, held %.0f s" % (name, n, secs, sha, k,
                                                                                          waited))
            paths.append(dest)
        slots = [(int(ASSET_RE.fullmatch(p.rsplit("/", 1)[1]).group(3)), [p]) for p in paths]
        for key, label, params, specs, ref in (("base", "TZ-43's rule", REHEARSAL_PARAMS, BASE_SPECS, REF_BASE),
                                               ("w", "rule W", REHEARSAL_W, SPECS, REF_W)):
            members = rehearsal_members(paths[0], params)
            polls = rehearsal_polls(members, REHEARSAL_D0) if key == "w" else None
            start, waited = hold(UNIT_BUDGET_S)
            c1 = time.process_time()
            rows, book, day = replay_paths(REHEARSAL_D0, members, slots, REHEARSAL_D0 + 4 * SLOT, polls, specs)
            cpu = time.process_time() - c1
            assert cpu <= REHEARSAL_CPU_MAX, "BLOCKED: the rehearsal's replay of %s took %.0f s" % (label, cpu)
            done.append((key, label, ref, len(members), day.c["lines"], compare_lines(rows, book), cpu, waited))
    finally:
        for p in paths:
            if os.path.exists(p):
                os.remove(p)
    passed = 0
    for key, label, ref, n_members, n_lines, lines, cpu, waited in done:
        body = ("\n".join(lines) + "\n").encode("utf-8")
        write_once(os.path.join(WORK, "rehearsal-%s.txt" % key), body)
        same = len(lines) == ref["lines"] and sha256_bytes(body) == ref["digest"]
        passed += 1 if same else 0
        out("rehearsal of %s: %d markets, %d lines of stream, %.1f s of processor, held %.0f s; %d lines sha256 %s "
            "against %d lines sha256 %s: %s" % (label, n_members, n_lines, cpu, waited, len(lines), sha256_bytes(body),
                                              ref["lines"], ref["digest"], "equal" if same else "DIFFERS"))
    out("G-REHEARSAL %s: %d of %d replays equal - TZ-43's rule to TZ-43's own lines, rule W to the Architect's second "
        "implementation" % ("PASS" if passed == len(done) == 2 else "FAIL", passed, 2))

# ---- the Release of the reading's inputs: one archive a candidate day, this run's files, the manifest ---------------


class Gh45(tz27.GitHub):
    """TZ-27's GitHub, every request held by `held` - the pair book's idle stretch, away from both archives' runs -
    and recorded; the Release created on its tag at the instrument's commit, published, never the latest."""

    def __init__(self, token=None, record=None, held=None, commit=None, api=None, uploads=None, web=None):
        super().__init__(token, api or tz27.API_BASE, uploads or tz27.UPLOAD_BASE, web or tz27.WEB_BASE)
        self.record, self.held, self.commit, self.sizes = record, held or hold, commit, {}

    def _timed(self, kind, name, nbytes, fn):
        budget = budget_s(nbytes)
        _at, waited = self.held(budget)
        t0, ok = time.time_ns(), False
        try:
            res = fn()
            ok = True
            return res
        finally:
            if self.record is not None:
                self.record({"kind": kind, "name": name, "bytes": int(nbytes), "budget_s": budget,
                             "waited_s": round(waited, 3), "start_ns": t0, "end_ns": time.time_ns(), "ok": ok})

    def _json(self, method, url, body=None):
        path, parent = urllib.parse.urlsplit(url).path, super()._json
        return self._timed("api", "%s %s" % (method, path), 0, lambda: parent(method, url, body))

    def upload(self, rid, name, path, nbytes):
        parent = super().upload
        return self._timed("upload", name, nbytes, lambda: parent(rid, name, path, nbytes))

    def download(self, url):
        name = urllib.parse.unquote(url.rsplit("/", 1)[-1])
        nbytes, parent = self.sizes.get(name, 0), super().download
        return self._timed("download", name, nbytes, lambda: parent(url))

    def create_release(self, tag, name, body):
        assert self.token is not None and SHA40.fullmatch(self.commit or ""), "create_release: token and commit"
        self.pace()
        status, doc, _h = self._json("POST", "%s/repos/%s/releases" % (self.api, tz27.REPO),
                                     {"tag_name": tag, "target_commitish": self.commit, "name": name, "body": body,
                                      "draft": False, "prerelease": False, "make_latest": "false"})
        assert status == 201 and isinstance(doc, dict), "create release %s: status %r" % (tag, status)
        return doc

def tag_reading(obj, peeled, commit):
    """G-TAG: the tag on origin is lightweight and names the instrument's commit. Pure."""
    return obj is not None and obj == commit and peeled is None

def classify(d0, name):
    """A name of the day directory d0: select, slot or rewards - a member - or stream or other, never opened. A slot's
    file under another day's directory is a failed assert. Pure."""
    if SELECT_FILE_RE.fullmatch(name):
        return "select"
    m = SLOT_FILE_RE.fullmatch(name)
    if m is None:
        return "other"
    s = int(m.group(1))
    assert d0 <= s < d0 + DAY and s % SLOT == 0, "BLOCKED: %s under %d is a slot of another day" % (name, d0)
    return {"stream.jsonl.gz": "stream", "rewards.jsonl.gz": "rewards", "slot.json": "slot"}[m.group(3)]

def member_info(arcname, size, mtime):
    ti = tarfile.TarInfo(arcname)
    ti.size, ti.mtime, ti.mode, ti.type = size, mtime, 0o644, tarfile.REGTYPE
    ti.uid = ti.gid = 0
    ti.uname = ti.gname = ""
    return ti

def day_budget(member_bytes):
    """The seconds a day's unit is held for: PACK_BASE_S, and its members' bytes at SCAN_RATE, rounded up. Pure."""
    return PACK_BASE_S + -(-int(member_bytes) // SCAN_RATE)

def body_reason(rec):
    """Why one stored reply keeps its file out of the Release, or None. A body is published only where the venue
    served it as a JSON document under status 200: any other body - an error page among them - can carry the address
    it was served to. Pure."""
    if not isinstance(rec, dict):
        return "not a record"
    raw = rec.get("raw")
    if raw is None or raw == "":
        return None
    if rec.get("status") != 200:
        return "a body under status %s" % (rec.get("status") if isinstance(rec.get("status"), int) else "of no number")
    if not isinstance(raw, str):
        return "a body that is not text"
    try:
        doc = json.loads(raw)
    except (ValueError, RecursionError):
        return "a status-200 body that is not JSON"
    return None if isinstance(doc, (dict, list)) else "a status-200 body that is not a JSON document"

def withhold_reason(path):
    """Why a file of stored replies is left out of the Release, or None where every line of it is a record whose
    body, where it has one, is a JSON document the venue served under status 200. One read, a line at a time; the
    reason names a line by its number and never by its content."""
    try:
        with gzip.open(path, "rb") as fh:
            for k, ln in enumerate(fh, 1):
                if not ln.strip():
                    continue
                try:
                    rec = json.loads(ln)
                except (ValueError, RecursionError):
                    return "line %d: not JSON" % k
                why = body_reason(rec)
                if why is not None:
                    return "line %d: %s" % (k, why)
    except (OSError, EOFError, zlib.error) as exc:
        return "not a whole gzip file: %s" % type(exc).__name__
    return None

def list_day(root, d0):
    """A day directory's names, listed once: its members by name and bytes, every other name by its bytes and kind -
    a stream or a stray name, never opened - the members' bytes and the names counted by kind."""
    ddir = os.path.join(root, str(d0))
    assert os.path.isdir(ddir) and not os.path.islink(ddir), "BLOCKED: %s is not a directory" % ddir
    names = sorted(os.listdir(ddir))
    kinds = {n: classify(d0, n) for n in names}
    members, excluded, total = [], [], 0
    for n in names:
        st = os.lstat(os.path.join(ddir, n))
        if kinds[n] in MEMBER_KINDS:
            assert stat.S_ISREG(st.st_mode), "BLOCKED: %s/%s is not a regular file" % (ddir, n)
            members.append((n, st.st_size))
            total += st.st_size
        else:
            excluded.append({"name": n, "bytes": st.st_size, "kind": kinds[n]})
    assert members, "BLOCKED: %s holds no member" % ddir
    assert total <= DAY_MAX_BYTES, "BLOCKED: %s holds %d bytes of members, above %d" % (ddir, total, DAY_MAX_BYTES)
    return {"members": members, "excluded": excluded, "total": total,
            "counts": {k: sum(1 for n in names if kinds[n] == k) for k in KINDS}}

def pack_day(root, d0, outdir, listing=None, freef=None):
    """One day's archive, outdir/rewardbook-inputs-<D0>.tar: every member of root/<D0>/ in name order, stored verbatim
    as <D0>/<name>, its mtime D0, mode 644, owner 0 - but a file of stored replies one of whose lines withholds it,
    named with its bytes and that line and left out. Written once; a later run must build the same bytes. Returns
    (its manifest entry, wrote or unchanged)."""
    ddir = os.path.join(root, str(d0))
    lst = listing or list_day(root, d0)
    need = lst["total"] + 2 * tarfile.BLOCKSIZE * (len(lst["members"]) + 1) + tarfile.RECORDSIZE
    free = (freef or free_bytes)()
    assert free - need >= DISK_FLOOR, "BLOCKED: %d bytes free, %d needed, the floor %d" % (free, need, DISK_FLOOR)
    kept, withheld, scanned = [], [], 0
    for n, size in lst["members"]:
        why = None
        if n.endswith(SCANNED):
            scanned += 1
            why = withhold_reason(os.path.join(ddir, n))
        if why is None:
            kept.append((n, size))
        else:
            withheld.append({"name": n, "bytes": size, "reason": why})
    assert kept, "BLOCKED: %s: every member withheld" % ddir
    name = ARCHIVE_FMT % d0
    part, final = os.path.join(outdir, name + ".part"), os.path.join(outdir, name)
    rows = []
    with open(part, "wb") as fh:
        with tarfile.open(fileobj=fh, mode="w", format=tarfile.USTAR_FORMAT) as tf:
            for n, size in kept:
                with open(os.path.join(ddir, n), "rb") as src:
                    assert os.fstat(src.fileno()).st_size == size, "BLOCKED: %s/%s changed size" % (ddir, n)
                    rd = tz27.HashingReader(src)
                    tf.addfile(member_info("%d/%s" % (d0, n), size, d0), rd)
                    assert rd.n == size and src.read(1) == b"", "BLOCKED: %s/%s changed while read" % (ddir, n)
                rows.append({"name": "%d/%s" % (d0, n), "bytes": size, "sha256": rd.h.hexdigest()})
    sha, nbytes = sha256_file(part), os.stat(part).st_size
    if os.path.exists(final):
        got = sha256_file(final)
        assert got == sha, "determinism: %s sha256 %s, this run's %s" % (final, got, sha)
        os.remove(part)
        state = "unchanged"
    else:
        os.rename(part, final)
        state = "wrote"
    return {"D0": d0, "date": utc(d0)[:10], "archive": name, "bytes": nbytes, "sha256": sha, "members_n": len(rows),
            "member_bytes": sum(size for _n, size in kept), "scanned_n": scanned, "withheld_n": len(withheld),
            "withheld_bytes": sum(w["bytes"] for w in withheld), "counts": lst["counts"], "members": rows,
            "withheld": withheld, "excluded": lst["excluded"]}, state

def read_set(st):
    p = st.get("pack")
    assert p, "no set: pack has not run"
    with open(RELEASE_SET, "rb") as fh:
        raw = fh.read()
    assert sha256_bytes(raw) == p["set_sha256"], "release-set.json is not the set pack wrote"
    return json.loads(raw), raw

def upload_logger():
    def log(rec):
        rec = dict(rec, at=utc(time.time()), wall_ns=rec.get("wall_ns", time.time_ns()))
        tz27.forbid(rec, "upload.jsonl")
        jsonl_append(UPLOAD_LOG, rec)
        out("U %s" % json.dumps(rec, sort_keys=True))
    return log

def transfer_logger():
    return lambda rec: jsonl_append(TRANSFERS, rec)

def transfer_summary(recs):
    """The transfers' places in their windows: (count, started outside the idle stretch, ended after its second 590
    or in a later window, seconds waited). Pure."""
    outside = late = 0
    for r in recs:
        s0, s1 = r["start_ns"] / 1e9, r["end_ns"] / 1e9
        outside += 0 if IDLE[0] <= int(s0) % SLOT <= IDLE[1] else 1
        late += 0 if int(s1) - int(s1) % SLOT == int(s0) - int(s0) % SLOT and int(s1) % SLOT <= IDLE[1] else 1
    return len(recs), outside, late, round(sum(r["waited_s"] for r in recs), 1)

def branch_on_origin():
    lines = [ln.split("\t") for ln in git("ls-remote", "origin", "refs/heads/" + BRANCH, tree=PRIMARY).split("\n")
             if "\t" in ln]
    return lines[0][0] if len(lines) == 1 else None

def mode_upload():
    """B-UPLOAD, the Boss's block: the credential, the Release on TAG at the pack's commit, the set's assets."""
    floor_check()
    st = load_state()
    doc, raw = read_set(st)
    commit = st["pack"]["commit"]
    assert git("rev-parse", "HEAD") == commit, "BLOCKED: the worktree's HEAD is not the pack's commit %s" % commit
    assert branch_on_origin() == commit, "BLOCKED: origin's %s is not the pack's commit %s" % (BRANCH, commit)
    for x in doc["assets"]:
        p = tz27.store_path(UPLOAD_ROOT, x)
        assert os.path.isfile(p) and os.stat(p).st_size == x["bytes"], "BLOCKED: %s is not the set's %d bytes" % (
            p, x["bytes"])
    out("set %s: %d assets, %d bytes, at commit %s" % (sha256_bytes(raw), doc["assets_n"], doc["bytes_total"], commit))
    tok, source = tz27.credential()
    out("credential: %s" % source)
    log = upload_logger()
    gh = Gh45(token=tok, record=transfer_logger(), commit=commit)
    try:
        rel = gh.release_by_tag(TAG)
        created = rel is None
        if created:
            rel = gh.create_release(TAG, *release_text(doc, commit))
            out("created the Release on %s, id %s, target %s" % (TAG, rel.get("id"), rel.get("target_commitish")))
        assert rel.get("tag_name") == TAG and rel.get("draft") is False, "the Release is not published on the tag"
        sent, held = tz27.upload_set(gh, rel, doc, UPLOAD_ROOT, log)
        log({"action": "complete", "assets": sent + held, "sent": sent, "held": held, "release_id": int(rel["id"]),
             "created": created, "credential": source, "wall_ns": time.time_ns()})
    finally:    # printed on every exit of the upload, a refusal's and a failed assert's included
        n, outside, late, waited = transfer_summary(jsonl_read(TRANSFERS))
        out("transfers so far %d: %d started outside the idle stretch, %d ended after its second %d; %.1f s held" % (
            n, outside, late, IDLE[1], waited))
    out("UPLOAD COMPLETE: Release %s on %s, %d assets - %d sent, %d already held - %d bytes" % (
        rel["id"], TAG, sent + held, sent, held, doc["bytes_total"]))

def mode_verify():
    """G-TAG, G-UPLOAD and G-DOWNLOAD, with no token, 120 s or more after the upload's completion record."""
    floor_check()
    st = load_state()
    doc, raw = read_set(st)
    commit = st["pack"]["commit"]
    recs = jsonl_read(UPLOAD_LOG)
    why = tz27.upload_ready(recs, doc["assets_n"], time.time_ns())
    if why is not None and recs and recs[-1].get("action") == "complete":
        time.sleep(max(0.0, (recs[-1]["wall_ns"] + tz27.UPLOAD_SETTLE_S * 10 ** 9 - time.time_ns()) / 1e9 + 0.5))
        why = tz27.upload_ready(recs, doc["assets_n"], time.time_ns())
    assert why is None, "BLOCKED: %s" % why
    anon = Gh45(token=None, record=transfer_logger())
    anon.sizes = {x["asset"]: x["bytes"] for x in doc["assets"]}
    try:
        rel, rows, missing, extra = tz27.verify_release(anon, TAG, doc)
        for r in rows:
            out("V %s id %s state %s api %s bytes %s digest %s url %s download %s" % (
                r["asset"], r["id"], r["state"], r["api_ok"], r["api_bytes"], r["digest"], r["url_ok"],
                r["download_ok"]))
        checks = tz27.release_reading(rel, TAG, rows, missing, extra)
        obj, peeled = tz27.ls_remote_tag(TAG)
        out("tag %s on origin: %s, peeled %s; the pack's commit %s; the Release's target %s" % (
            TAG, obj, peeled, commit, (rel or {}).get("target_commitish")))
        checks["the tag on origin lightweight, at the pack's commit"] = tag_reading(obj, peeled, commit)
        for k, v in checks.items():
            out("G-TAG/G-UPLOAD/G-DOWNLOAD %-56s %s" % (k, v))
        assert all(checks.values()), "VERIFY FAIL: %r; missing %r; beyond %r" % (
            sorted(k for k, v in checks.items() if not v), missing[:5], extra[:5])
        vdoc = {"tag": TAG, "release_id": int(rel["id"]), "set_sha256": sha256_bytes(raw), "commit": commit,
                "assets": rows, "assets_n": len(rows), "bytes_total": sum(r["download_bytes"] for r in rows)}
        write_once(VERIFY_FILE, tz27.json_bytes(vdoc))
    finally:    # printed on every exit of the proof, a failed download's and a failed assert's included
        n, outside, late, waited = transfer_summary(jsonl_read(TRANSFERS))
        out("transfers %d, upload's and verify's: %d started outside the idle stretch, %d ended after its second %d; "
            "%.1f s held" % (n, outside, late, IDLE[1], waited))
    out("G-UPLOAD PASS: %d of %d assets by name, bytes, state and digest; G-DOWNLOAD PASS: %d of %d downloads, "
        "%d bytes; G-TAG PASS: %s at %s" % (sum(r["api_ok"] for r in rows), doc["assets_n"],
                                           sum(r["download_ok"] for r in rows), doc["assets_n"], vdoc["bytes_total"],
                                           TAG, commit))


def asset_name(path):
    """The Release's name of a file of this run's tree: tz45- and its path, one hyphen between its parts. Pure."""
    return "tz45-" + path.replace("/", "-")


def work_sources(s, st, root=None):
    """G-SOURCE: the files of this run the reading rests on - the set and the reading, and each member day's record,
    polls, rows and slot lines - each a regular file whose SHA-256 is the one this run's own record names: state.json's
    for the set and the reading, the set's for a day's record, that record's for its polls, the reading's for the
    day's rows and slot lines."""
    root = WORK if root is None else root
    reading = load_json(os.path.join(root, "reading.json"))
    want = [("set.json", st["fetch"]["set_sha256"]), ("reading.json", st["score"]["reading_sha256"])]
    for d0 in s["members"]:
        rec = load_json(os.path.join(root, "fetch", "%d.json" % d0))
        want += [("fetch/%d.json" % d0, s["days"][str(d0)]["sha256"]),
                 ("fetch/%d.polls.jsonl" % d0, rec["polls"]["sha256"]),
                 ("days/%d.json" % d0, reading["inputs"][str(d0)]["day"]),
                 ("days/%d.slots.txt" % d0, reading["inputs"][str(d0)]["slots"])]
    rows, bad = [], []
    for path, sha in want:
        p = os.path.join(root, path)
        stt = os.lstat(p)
        assert stat.S_ISREG(stt.st_mode), "BLOCKED: %s is not a regular file" % p
        h = sha256_file(p)
        out("G-SOURCE %s %d bytes sha256 %s %s" % (path, stt.st_size, h, "equal" if h == sha else "DIFFERS"))
        if h != sha:
            bad.append(path)
        rows.append({"asset": asset_name(path), "path": path, "bytes": stt.st_size, "sha256": h})
    assert not bad, "BLOCKED: G-SOURCE %d of %d differ from this run's own record: %s" % (len(bad), len(want), bad)
    return rows


def manifest_doc(commit, file_sha, days, sources, s):
    return {"tag": TAG, "made_by": "research/" + PYFILE, "commit": commit, "file_sha256": file_sha, "store": RB_ROOT,
            "first_D0": FIRST_D0, "considered": s["considered"], "members": s["members"],
            "unread_from_D0": s["considered"][-1]["d0"] + DAY, "days": days, "tz45": {"files": sources}}


def set_doc(days, sources, manifest_bytes, manifest_sha):
    """The Release's set, in upload order: the day archives, this run's files, the manifest. Each entry's T and file
    place it under UPLOAD_ROOT for TZ-27's upload_set (store_path)."""
    out_t = os.path.relpath(OUT, UPLOAD_ROOT)
    assets = [{"T": out_t, "file": d["archive"], "asset": d["archive"], "bytes": d["bytes"], "sha256": d["sha256"]}
              for d in days]
    for x in sources:
        p = os.path.join(WORK, x["path"])
        assets.append({"T": os.path.relpath(os.path.dirname(p), UPLOAD_ROOT), "file": os.path.basename(p),
                       "asset": x["asset"], "bytes": x["bytes"], "sha256": x["sha256"]})
    assets.append({"T": out_t, "file": MANIFEST, "asset": MANIFEST, "bytes": manifest_bytes, "sha256": manifest_sha})
    names = [x["asset"] for x in assets]
    assert len(set(names)) == len(names), "two assets of one name"
    return {"tag": TAG, "assets": assets, "assets_n": len(assets), "bytes_total": sum(x["bytes"] for x in assets)}


def release_text(doc, commit, man=None):
    man = load_json(os.path.join(OUT, MANIFEST)) if man is None else man
    cons, mem = [c["d0"] for c in man["considered"]], man["members"]
    name = "%s: the inputs of L0's second gate - the reward book's days %s to %s and TZ-45's work files" % (
        doc["tag"], utc(cons[0])[:10], utc(cons[-1])[:10])
    body = ("Every file of /var/lib/btc-rewardbook/<D0>/ but its streams, for the %d candidate days %d to %d that "
            "TZ-45's walk considered, %d of them the members of its set - each day's selections with their replies, "
            "its slot records and its reward polls, stored verbatim - one tar a day, rewardbook-inputs-<D0>.tar, its "
            "members named <D0>/<file>; and the %d files of TZ-45's own run its reading rests on - set.json, "
            "reading.json and each member day's fetch/ and days/ files - each asset tz45-<path> with - for /. %s lists "
            "every asset and every member by its bytes and SHA-256. A file of stored replies is left out, and named "
            "there with its bytes and the line that withheld it, where a line of it carries a body the venue did not "
            "serve as a JSON document under status 200: an error page can carry the address it was served to. The "
            "streams are the rewardbook-streams-* Releases'. No day from %d is here: none has been read. %d assets, "
            "%d bytes, made by research/%s at commit %s (TZ-45). Each asset's SHA-256 is its digest here." % (
                len(cons), cons[0], cons[-1], len(mem), len(man["tz45"]["files"]), MANIFEST, man["unread_from_D0"],
                doc["assets_n"], doc["bytes_total"], PYFILE, commit))
    return name, body


def mode_pack():
    """G-SOURCE, then G-PACK: this run's own files as one held unit, each candidate day the set considered as one,
    held for its members' bytes; the manifest and the Release's set written once; a second run asserts all of it
    unchanged (DETERMINISM)."""
    floor_check()
    commit, up = git("rev-parse", "HEAD"), git("rev-parse", "@{u}")
    assert SHA40.fullmatch(commit) and commit == up, "BLOCKED: the branch head %s is not its upstream's %s" % (
        commit, up)
    file_sha = sha256_file(os.path.join(HERE, PYFILE))
    s, st = the_set(), load_state()
    assert "fetch" in st and "score" in st, "BLOCKED: pack before the set and the reading are recorded"
    cons = [c["d0"] for c in s["considered"]]
    assert cons == list(range(FIRST_D0, FIRST_D0 + len(cons) * DAY, DAY)) and all(day_in_span(d) for d in cons) \
        and set(s["members"]) <= set(cons), "BLOCKED: the set's candidates are not the span's first days"
    PACK_DAYS[:] = cons
    at, waited = hold(SOURCE_BUDGET_S)
    t0 = time.time()
    sources = work_sources(s, st)
    out("G-SOURCE PASS: %d of %d equal to this run's own record, %d bytes; held %.1f s, from second %d, %.2f s" % (
        len(sources), 2 + 4 * len(s["members"]), sum(x["bytes"] for x in sources), waited, int(at) % SLOT,
        time.time() - t0))
    os.makedirs(OUT, exist_ok=True)
    days, states, over = [], collections.Counter(), 0
    for d0 in cons:
        listing = list_day(RB_ROOT, d0)
        budget = day_budget(listing["total"])
        at, waited = hold(budget)
        t0 = time.time()
        entry, state = pack_day(RB_ROOT, d0, OUT, listing)
        took = time.time() - t0
        over += 1 if took > budget else 0
        states[state] += 1
        c = entry["counts"]
        out("day %d (%s): %d names - select %d, slot %d, rewards %d, stream %d and other %d never opened; %s %d "
            "members, %d bytes, of %d files of replies scanned; withheld %d, %d bytes; %s %d bytes sha256 %s; budget "
            "%d s, held %.1f s, from second %d, %.2f s" % (
                d0, entry["date"], sum(c.values()), c["select"], c["slot"], c["rewards"], c["stream"], c["other"],
                entry["archive"], entry["members_n"], entry["member_bytes"], entry["scanned_n"], entry["withheld_n"],
                entry["withheld_bytes"], state, entry["bytes"], entry["sha256"], budget, waited, int(at) % SLOT, took))
        for x in entry["withheld"]:
            out("  withheld %s, %d bytes: %s" % (x["name"], x["bytes"], x["reason"]))
        for x in entry["excluded"]:
            out("  excluded %s %s, %d bytes, never opened" % (x["kind"], x["name"], x["bytes"]))
        days.append(entry)
    mraw = tz27.json_bytes(manifest_doc(commit, file_sha, days, sources, s))
    states[write_same(os.path.join(OUT, MANIFEST), mraw)] += 1
    doc = set_doc(days, sources, len(mraw), sha256_bytes(mraw))
    raw = tz27.json_bytes(doc)
    states[write_same(RELEASE_SET, raw)] += 1
    record("pack", {"commit": commit, "file_sha256": file_sha, "set_sha256": sha256_bytes(raw),
                    "manifest_sha256": sha256_bytes(mraw), "assets_n": doc["assets_n"],
                    "bytes_total": doc["bytes_total"]})
    for x in doc["assets"]:
        out("S %s %d %s" % (x["asset"], x["bytes"], x["sha256"]))
    members, scanned = sum(d["members_n"] for d in days), sum(d["scanned_n"] for d in days)
    out("G-PACK PASS: %d days of %d, %d members, %d bytes of members, %d bytes of archives; withheld %d files of "
        "replies, %d bytes; streams %d and other names %d never opened; %d assets, %d bytes; days over their budget "
        "%d; outputs %s" % (
            len(days), len(cons), members, sum(d["member_bytes"] for d in days), sum(d["bytes"] for d in days),
            sum(d["withheld_n"] for d in days), sum(d["withheld_bytes"] for d in days),
            sum(d["counts"]["stream"] for d in days), sum(d["counts"]["other"] for d in days), doc["assets_n"],
            doc["bytes_total"], over, dict(sorted(states.items()))))
    assert COUNTS["reward book opens"] == members + scanned and COUNTS["reward book listings"] == len(cons), \
        "BLOCKED: the store opened %d times and listed %d, for %d members, %d files scanned and %d days" % (
            COUNTS["reward book opens"], COUNTS["reward book listings"], members, scanned, len(cons))
    out("G-RESERVE PASS: the store opened %d times - once a member kept, %d, and once a file of replies scanned, %d "
        "- and listed %d times, one a day; no other open or listing under %s" % (
            COUNTS["reward book opens"], members, scanned, COUNTS["reward book listings"], RB_ROOT))
    if states["unchanged"] == len(cons) + 2:
        out("DETERMINISM PASS: %d of %d outputs unchanged" % (states["unchanged"], len(cons) + 2))


# ---- the session's modes ------------------------------------------------------------------------------------


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
        out("%-48s %6d lines %8d bytes %s %s%s" % (path, got[0], got[1], got[2], state,
                                                  " equal" if state == "frozen" else ""))
    out("SYSTEM-MAP.md %d lines %d bytes sha256 %s" % (raw.count(b"\n"), len(raw), sha256_bytes(raw)))
    out("FINGERPRINT PASS: revision %s; anchors 6 of 6, 4 re-derived; rows %d: frozen %d of %d equal, tracked %d, "
        "reported %d" % (MAP_REVISION, len(rows), states["frozen"], MAP_ROWS["frozen"], states["tracked"],
                         states["reported"]))


def number_reading(names, own):
    """NUMBER, CANON hard rule 2: CryptoTZ/ holds this TZ's file and no other of its number; CryptoReports/ no report
    of it. Pure."""
    tz = [n for n in names if n.startswith("CryptoTZ/" + NUMBER)]
    rp = [n for n in names if n.startswith("CryptoReports/" + NUMBER)]
    return tz == [own] and not rp, tz, rp


def mode_number():
    names = git("ls-tree", "--name-only", "origin/main", "--", "CryptoTZ/", "CryptoReports/", tree=PRIMARY).split("\n")
    head = git("rev-parse", "origin/main", tree=PRIMARY)
    ok, tz, rp = number_reading(names, OWN_TZ)
    out("origin/main %s: %d paths under CryptoTZ/ and CryptoReports/; of the number %s: %s and %s" % (
        head, len(names), NUMBER, tz, rp))
    out("NUMBER %s" % ("PASS - 2 of 2" if ok else "FAIL"))
    assert ok, "BLOCKED: of the number %s, CryptoTZ/ holds %s and CryptoReports/ %s" % (NUMBER, tz, rp)


def still_reading(before, now, restarts):
    """G-STILL from two reads and the pair book archive's restart records between them, in order: PASS where every
    unit is unchanged, or where every unit but the pair book is unchanged and its change is that archive's own
    restarts alone - a chain from the recorded MainPID to the current one, NRestarts one higher at each, the unit
    active. Pure."""
    if now == before:
        return True, "unchanged"
    for k in sorted(now):
        if k != "pairbook" and now[k] != before.get(k):
            return False, "the %s changed" % k
    b, n = before["pairbook"], now["pairbook"]
    pid, count = b["MainPID"], int(b["NRestarts"])
    for r in restarts:
        if str(r.get("stopped")) != pid or str(r.get("NRestarts")) != str(count + 1):
            return False, "a restart record that does not follow %s at NRestarts %d: %r" % (pid, count, r)
        pid, count = str(r.get("pid")), count + 1
    if restarts and pid == n["MainPID"] and str(count) == n["NRestarts"] and n["ActiveState"] == "active":
        return True, "changed by the pair book archive's own restarts alone: %d" % len(restarts)
    return False, "the pair book changed, %d restart records of its archive since the first read" % len(restarts)


def mode_still():
    st = load_state()
    now = {}
    for key, unit in sorted(UNITS.items()):
        kv = show(unit, ["MainPID", "NRestarts", "ActiveState", "MemoryCurrent", "MemoryPeak"])
        now[key] = {k: kv[k] for k in ("MainPID", "NRestarts", "ActiveState")}
        out("%s %s, MemoryCurrent %s, MemoryPeak %s" % (unit, now[key], kv.get("MemoryCurrent"), kv.get("MemoryPeak")))
    for key, (svc, timer) in sorted(ARCHIVES.items()):
        for unit in (timer, svc):
            out("%s %s" % (unit, show(unit, ["ActiveState", "SubState", "UnitFileState", "Result"])))
    if "still" not in st:
        st["still"] = {"at": utc(time.time()), "at_ns": time.time_ns(), "units": now}
        save_state(st)
        out("still: recorded")
        return
    _raw, recs, _tail = ledger_records(PB_LEDGER)
    since = st["still"]["at_ns"]
    restarts = [r for r in recs if r.get("event") == "restart" and r.get("wall_ns", 0) >= since]
    for r in restarts:
        out("the pair book archive's restart record %s: run %s, window %s, pid %s after %s, NRestarts %s" % (
            utc(r["wall_ns"] / 1e9), r.get("run"), r.get("W"), r.get("pid"), r.get("stopped"), r.get("NRestarts")))
    _raw, rrecs, _tail = ledger_records(RB_LEDGER)
    runs = sorted({r.get("run") for r in rrecs if r.get("wall_ns", 0) >= since and isinstance(r.get("run"), int)})
    out("the reward book archive's runs with records since the first read: %s" % runs)
    ok, why = still_reading(st["still"]["units"], now, restarts)
    out("G-STILL %s: %s since %s" % ("PASS" if ok else "FAIL", why, st["still"]["at"]))


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


def mode_archive():
    """The reward book archive's own record, read whole: its complete lines, its runs summarized, every complete
    run's set.json asserted by its set record's SHA-256, and the slots its assets reach."""
    svc, timer = ARCHIVES["rewardbook"]
    for unit in (timer, svc):
        out("%s %s" % (unit, show(unit, ["ActiveState", "SubState", "UnitFileState", "Result", "ExecMainStatus",
                                         "LastTriggerUSec", "NextElapseUSecRealtime"])))
    raw, recs, tail = ledger_records(RB_LEDGER)
    out("ledger %s: %d bytes sha256 %s, %d complete records, %d bytes of a line still written" % (
        RB_LEDGER, len(raw), sha256_bytes(raw), len(recs), len(tail)))
    for r in recs:
        out("L %s %s" % (utc(r["wall_ns"] / 1e9) if isinstance(r.get("wall_ns"), int) else "-",
                         json.dumps(r, sort_keys=True)))
    summ = ledger_summary(recs)
    for ln in summ["lines"]:
        out(ln)
    sets = archived_sets(recs)
    amap = asset_map(sets)
    for s in sets:
        ss = sorted(x["S"] for x in s["doc"]["assets"])
        out("set %s run %d sha256 %s: %d files, %d bytes, slots %s to %s" % (
            s["tag"], s["run"], s["sha256"], s["doc"]["assets_n"], s["doc"]["bytes_total"], ss[0] if ss else "-",
            ss[-1] if ss else "-"))
    slots = sorted({int(ASSET_RE.fullmatch(v["asset"]).group(3)) for v in amap.values()})
    after = [s for s in slots if s >= FIRST_D0]
    out("the archive's assets: %d files of %d slots, to slot %s; at or after %d: %d slots, to %s" % (
        len(amap), len(slots), slots[-1] if slots else "-", FIRST_D0, len(after), after[-1] if after else "-"))
    tags = sorted(ln.split("\t")[1][len("refs/tags/"):] for ln in git(
        "ls-remote", "origin", "refs/tags/rewardbook-streams-*", tree=PRIMARY).split("\n") if "\t" in ln)
    stags = [s["tag"] for s in sets]
    out("tags on origin %d: %s" % (len(tags), tags))
    out("complete runs' sets %d; their tags not on origin %s; halted %s; runs without a terminal record %s" % (
        len(stags), sorted(set(stags) - set(tags)), summ["halted"],
        [a for a, t in summ["terminal"].items() if not t]))
    assert REHEARSAL_TAG in stags, "BLOCKED: the rehearsal's set %s is not a complete run's" % REHEARSAL_TAG
    held = {(x["asset"], x["bytes"], x["sha256"]) for s in sets if s["tag"] == REHEARSAL_TAG
            for x in s["doc"]["assets"]}
    assert all(a in held for a in REHEARSAL_ASSETS), "BLOCKED: the rehearsal's assets differ from its set"
    out("the rehearsal's four assets are in set %s, bytes and SHA-256 equal" % REHEARSAL_TAG)


def report_tokens():
    tokens = set()
    for name in sorted(os.listdir(REPORTS)):
        if name.endswith(".md"):
            with open(os.path.join(REPORTS, name), encoding="utf-8", errors="replace") as fh:
                tokens.update(TOKEN.findall(fh.read()))
    return tokens


def by_name(tree, rel):
    return tree == WORK and (rel in ("state.json", "read-ledger.jsonl", "upload.jsonl", "transfers.jsonl",
                                     "verify.json", "release-set.json") or rel.startswith("logs/"))


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


def released_by(path=None):
    """SHA-256 -> asset, for every asset verify proved by a full anonymous download: verify.json, where it exists.
    reclaim copies no file the Release holds by the SHA-256 the report names (map section 7 item 167)."""
    path = VERIFY_FILE if path is None else path
    if not os.path.exists(path):
        return {}
    return {a["sha256"]: a["asset"] for a in load_json(path)["assets"] if a.get("download_ok") is True}


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
    released = released_by() if WORK in trees else {}
    before = sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    out("reclaim: %d report tokens; forensic store holds %d files; the Release %s proved %d assets" % (
        len(tokens), before, TAG, len(released)))
    considered = named = kept = copied = held = in_release = 0
    for tree in trees:
        if tree == WORK and os.path.isdir(WT):
            pristine(WT)
        for dirpath, dirnames, filenames in os.walk(tree):
            dirnames[:] = sorted(d for d in dirnames if os.path.join(dirpath, d) != WT)
            for name in sorted(filenames):
                path = os.path.join(dirpath, name)
                if os.path.islink(path) or not os.path.isfile(path):
                    continue
                considered += 1
                rel = os.path.relpath(path, tree)
                h = sha256_file(path)
                is_named = any(h[:k] in tokens for k in lengths)
                is_kept = by_name(tree, rel)
                if not (is_named or is_kept):
                    continue
                named += 1 if is_named else 0
                kept += 1 if is_kept and not is_named else 0
                if h in released and not is_kept:
                    in_release += 1
                    out("R release %s %s is %s of %s" % (h, path, released[h], TAG))
                    continue
                dest = os.path.join(FORENSICS, os.path.basename(tree) + "--" + rel.replace("/", "--"))
                if os.path.exists(dest):
                    got = sha256_file(dest)
                    assert got == h, "reclaim: %s exists with sha256 %s, source %s" % (dest, got, h)
                    held += 1
                    out("R held   %s %s" % (h, dest))
                    continue
                size, free = os.path.getsize(path), free_bytes()
                assert free - size >= DISK_FLOOR, "BLOCKED: reclaim: %d bytes free, %s is %d, the floor %d" % (
                    free, path, size, DISK_FLOOR)
                with open(path, "rb") as src, open(dest, "xb") as dst:
                    shutil.copyfileobj(src, dst, 1 << 20)
                assert sha256_file(dest) == h, "reclaim: %s did not copy whole" % dest
                copied += 1
                out("R copied %s %s" % (h, dest))
    after = sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    assert after == before + copied, "reclaim: store %d, expected %d" % (after, before + copied)
    out("RECLAIM PASS: %d files considered, %d named by a report, %d kept by name, %d copied, %d already held, %d left "
        "to the Release %s that holds them; forensic store %d -> %d files" % (
            considered, named, kept, copied, held, in_release, TAG, before, after))


def read_ledger(mode):
    """The read ledger: one line a mode that reads the store, the archive's Releases or the set, with this file's
    SHA-256 and the work tree's HEAD."""
    with open(os.path.join(HERE, PYFILE), "rb") as fh:
        mine = sha256_bytes(fh.read())
    head = git("rev-parse", "HEAD") if os.path.isdir(WT) else None
    rec = {"mode": mode, "at": utc(time.time()), "at_ns": time.time_ns(), "file_sha256": mine, "head": head}
    with open(LEDGER, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, sort_keys=True) + "\n")
    out("read ledger: %s" % json.dumps(rec, sort_keys=True))


def main(argv):
    if not argv:
        sys.exit("usage: %s MODE [ARG...]" % PYFILE)
    mode, rest = argv[0], argv[1:]
    assert os.getcwd() == WORK, "run from %s, not %s" % (WORK, os.getcwd())
    MODE[0] = mode
    tz27.MODE[0] = mode
    table = {"fingerprint": mode_fingerprint, "number": mode_number, "selftest": mode_selftest,
             "still": mode_still, "archive": mode_archive, "rehearse": mode_rehearse, "fetch": mode_fetch,
             "replay": mode_replay, "rescore": mode_rescore, "score": mode_score, "pack": mode_pack,
             "upload": mode_upload, "verify": mode_verify}
    try:
        if mode in ("rehearse", "fetch", "replay", "rescore", "score", "pack"):
            read_ledger(mode)
        if mode == "reclaim":
            mode_reclaim(rest)
        elif mode == "scratch":
            assert len(rest) == 1, "scratch OWN"
            mode_scratch(rest[0])
        else:
            assert mode in table and not rest, "unknown mode %r" % (argv,)
            table[mode]()
    finally:    # printed on every exit, a BLOCK's and a failed assert's included
        out("malloc tuned: %s" % MALLOC_TUNED)
        out("peak memory of this run: %d bytes" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024))
        out("opens refused: %d, by TZ-27's hook: %d; reward book opens: %d, listings: %d" % (
            len(REFUSED), len(tz27.REFUSED), COUNTS["reward book opens"], COUNTS["reward book listings"]))

# ---- the self-test: literals, a synthetic day and temporary trees under the work tree ------------------------------

SYN_D0 = 1792800000          # 2026-10-24 00:00:00 UTC: a synthetic day, two slots
SYN = {"A": {"cid": "0x" + "a1" * 32, "tok": "1001", "other": "1002", "ms": 2000, "vu": 90, "rate": Fr(100),
             "fee": Fr(1, 80)},
       "B": {"cid": "0x" + "b2" * 32, "tok": "2001", "other": "2002", "ms": 5000, "vu": 70, "rate": Fr(50),
             "fee": Fr(0)}}


def _side(levels):
    return [{"price": p, "size": s} for p, s in levels]


def _book(m, ts, bids, asks, tick="0.01", tok=None):
    return {"market": m["cid"], "asset_id": tok or m["tok"], "timestamp": str(ts), "hash": "ab" * 20,
            "bids": _side(bids), "asks": _side(asks), "tick_size": tick, "event_type": "book",
            "last_trade_price": "0.5"}


def _pc(m, ts, side, price, size):
    """A price_change frame of market m: the first token's entry and its mirror on the other token, in the venue's
    key order and separators."""
    mirror = format(D(1) - D(price), "f").rstrip("0").rstrip(".") if D(price) != 0 else "1"
    other = "SELL" if side == "BUY" else "BUY"
    return {"market": m["cid"], "price_changes": [
        {"asset_id": m["tok"], "price": price, "size": size, "side": side, "hash": "cd" * 20, "best_bid": "0.4",
         "best_ask": "0.46"},
        {"asset_id": m["other"], "price": mirror, "size": size, "side": other, "hash": "ef" * 20, "best_bid": "0.54",
         "best_ask": "0.6"}], "timestamp": str(ts), "event_type": "price_change"}


def _line(h, frame=None, event=None, **kw):
    if event is not None:
        return json.dumps(dict({"recv_ns": h, "mono_ns": h - 10 ** 9, "event": event}, **kw), separators=(",", ":"))
    raw = frame if isinstance(frame, str) else json.dumps(frame, separators=(", ", ":"))
    return json.dumps({"recv_ns": h, "mono_ns": h - 10 ** 9, "raw": raw}, separators=(",", ":"))


def synth_lines(S, first):
    """Slot S's synthetic stream (TZ-45 section 4.1): host instants in ms after S, venue stamps 20 ms before."""
    A, B = SYN["A"], SYN["B"]
    ms = lambda off: S * 1000 + off
    hn = lambda off: (S * 1000 + off) * MS_NS
    out_ = [_line(hn(-5000), event="connect", seg=0), _line(hn(-4900), event="open", seg=0),
            _line(hn(-4800), event="subscribe", seg=0, tokens=4)]
    if first:
        seed = [_book(A, ms(-4020), [("0.4", "100"), ("0.38", "500")], [("0.46", "100"), ("0.48", "300")]),
                _book(A, ms(-4020), [("0.52", "300")], [("0.6", "100")], tok=A["other"]),
                _book(B, ms(-4020), [("0.6", "200")], [("0.62", "200")]),
                _book(B, ms(-4020), [("0.38", "200")], [("0.4", "200")], tok=B["other"])]
        out_.append(_line(hn(-4000), seed))
        steps = [(1000, _pc(A, ms(1000), "BUY", "0.39", "50")),
                 (10000, _pc(A, ms(10000), "BUY", "0.4", "70")),
                 (10010, _book(A, ms(10000), [("0.4", "70"), ("0.39", "50"), ("0.38", "500")],
                               [("0.46", "100"), ("0.48", "300")])),
                 (10011, _book(A, ms(10000), [("0.52", "300")], [("0.6", "70")], tok=A["other"])),
                 (10020, {"market": A["cid"], "asset_id": A["tok"], "price": "0.4", "size": "30", "fee_rate_bps": "0",
                          "side": "SELL", "timestamp": str(ms(10000)), "event_type": "last_trade_price"}),
                 (20000, _pc(A, ms(20000), "SELL", "0.47", "10")),
                 (30000, _pc(A, ms(30000), "SELL", "0.41", "50")),
                 (40000, _pc(A, ms(40000), "SELL", "0.41", "0")),
                 (50000, _pc(A, ms(50000), "BUY", "0.45", "10")),
                 (60000, _pc(A, ms(60000), "BUY", "0.45", "0")),
                 (60050, _pc(A, ms(60050), "BUY", "0.45", "5")),
                 (60200, _pc(A, ms(60200), "BUY", "0.45", "0")),
                 (61000, _pc(B, ms(61000), "SELL", "0.62", "150")),
                 (62000, _pc(B, ms(62000), "SELL", "0.66", "100")),
                 (62100, _pc(B, ms(62100), "SELL", "0.62", "0"))]
        for off, fr in steps:
            out_.append(_line(hn(off + 20), fr))
        out_.append(_line(hn(70020), event="close", code=1006, reason="closed", seg=0))
        out_ += [_line(hn(71000), event="connect", seg=1), _line(hn(71100), event="open", seg=1),
                 _line(hn(71200), event="subscribe", seg=1, tokens=4)]
        out_.append(_line(hn(72000), [
            _book(A, ms(71980), [("0.4", "70"), ("0.39", "50"), ("0.38", "500")],
                  [("0.46", "100"), ("0.47", "10"), ("0.48", "300")]),
            _book(B, ms(71980), [("0.6", "200")], [("0.66", "100")])]))
        out_.append(_line(hn(80020), "PONG"))
        out_.append(_line(hn(100020), _pc(B, ms(100000), "SELL", "0.65", "30")))
        out_.append(_line(hn(110020), _pc(B, ms(110000), "SELL", "0.65", "0")))
        out_.append(_line(hn(110030), _book(B, ms(110000), [("0.6", "200")], [("0.66", "100")])))
        out_.append(_line(hn(900500), _pc(A, ms(900480), "BUY", "0.4", "999")))
        out_.append(_line(hn(905000), event="close", code=1000, reason="end", seg=1))
    else:
        out_.append(_line(hn(-4000), [
            _book(A, ms(-4020), [("0.4", "80"), ("0.39", "50"), ("0.38", "500")],
                  [("0.46", "100"), ("0.47", "10"), ("0.48", "300")]),
            _book(B, ms(-4020), [("0.6", "200")], [("0.66", "100")])]))
        out_.append(_line(hn(-2000), _pc(A, ms(-2020), "BUY", "0.4", "90")))
        steps = [(20, _pc(A, ms(20), "BUY", "0.4", "85")),
                 (300000, {"market": A["cid"], "asset_id": A["tok"], "old_tick_size": "0.01",
                           "new_tick_size": "0.001", "timestamp": str(ms(300000)), "event_type": "tick_size_change"}),
                 (300100, _pc(A, ms(300100), "BUY", "0.39", "60")),
                 (600000, _pc(B, ms(600000), "BUY", "0.59", "40")),
                 (700000, _pc(B, ms(700000), "BUY", "0.63", "20"))]
        for off, fr in steps:
            out_.append(_line(hn(off + 20), fr))
        out_.append(_line(hn(905000), event="close", code=1000, reason="end", seg=0))
    return out_


def synth_day(dirpath, d0=SYN_D0, slow=False):
    """The synthetic day's two stream files under `dirpath`; with `slow`, every line written with a space after
    each colon, out of PC_LINE's reach, so that only the JSON path reads it."""
    paths = []
    for k, S in enumerate((d0, d0 + SLOT)):
        lines = synth_lines(S, k == 0)
        if slow:
            lines = [json.dumps(json.loads(ln), separators=(", ", ": ")) for ln in lines]
        p = os.path.join(dirpath, "%d.0.stream.jsonl.gz" % S)
        with open(p, "wb") as raw, gzip.GzipFile(fileobj=raw, mode="wb", compresslevel=9, mtime=0) as fh:
            fh.write(("\n".join(lines) + "\n").encode("utf-8"))
        paths.append((S, [p]))
    return paths


def synth_polls(d0=SYN_D0):
    A, B = SYN["A"]["cid"], SYN["B"]["cid"]
    t = lambda s: (d0 + s) * S_NS
    return [(t(5), A, (Fr(100), Fr(2))), (t(35), B, (Fr(50), Fr(1, 2))), (t(65), A, None), (t(80), A, (Fr(120), Fr(3))),
            (t(930), A, (Fr(120), Fr(3))), (t(931), B, (Fr(50), Fr(1, 2)))]


def synth_members():
    return [{k: m[k] for k in ("cid", "tok", "ms", "vu", "rate", "fee")} for m in (SYN["A"], SYN["B"])]


def synth_w_lines(S, first):
    """Slot S's synthetic stream for rule W (TZ-45 section 4.1): market A's touch leaves room for the rule's quote,
    market B's minimum size is above the rule's; host instants in ms after S, venue stamps 20 ms before."""
    A, B = SYN["A"], SYN["B"]
    ms = lambda off: S * 1000 + off
    hn = lambda off: (S * 1000 + off) * MS_NS
    out_ = [_line(hn(-5000), event="connect", seg=0), _line(hn(-4900), event="open", seg=0),
            _line(hn(-4800), event="subscribe", seg=0, tokens=4)]
    if first:
        out_.append(_line(hn(-4000), [
            _book(A, ms(-4020), [("0.3", "100"), ("0.28", "500")], [("0.42", "100"), ("0.44", "300")]),
            _book(A, ms(-4020), [("0.56", "300")], [("0.7", "100")], tok=A["other"]),
            _book(B, ms(-4020), [("0.6", "200")], [("0.75", "200")]),
            _book(B, ms(-4020), [("0.25", "200")], [("0.4", "200")], tok=B["other"])]))
        steps = [(10000, _pc(A, ms(10000), "BUY", "0.3", "70")),
                 (10010, _book(A, ms(10000), [("0.3", "70"), ("0.28", "500")], [("0.42", "100"), ("0.44", "300")])),
                 (20000, _pc(A, ms(20000), "SELL", "0.44", "310")),
                 (40000, _pc(A, ms(40000), "BUY", "0.4", "10")),
                 (50000, _pc(A, ms(50000), "BUY", "0.4", "0")),
                 (60000, _pc(A, ms(60000), "BUY", "0.3", "0")),
                 (61000, _pc(A, ms(61000), "BUY", "0.28", "0")),
                 (62000, _pc(A, ms(62000), "BUY", "0.15", "500")),
                 (63000, _pc(A, ms(63000), "SELL", "0.42", "0")),
                 (64000, _pc(A, ms(64000), "SELL", "0.42", "100")),
                 (65000, _pc(A, ms(65000), "SELL", "0.42", "60")),
                 (65010, _book(A, ms(65000), [("0.15", "500")], [("0.42", "60"), ("0.44", "310")])),
                 (66000, _pc(A, ms(66000), "SELL", "0.44", "305"))]
        for off, fr in steps:
            out_.append(_line(hn(off + 20), fr))
        out_.append(_line(hn(70020), event="close", code=1006, reason="closed", seg=0))
        out_ += [_line(hn(71000), event="connect", seg=1), _line(hn(71100), event="open", seg=1),
                 _line(hn(71200), event="subscribe", seg=1, tokens=4)]
        out_.append(_line(hn(72000), [
            _book(A, ms(71980), [("0.15", "500")], [("0.42", "60"), ("0.44", "305")]),
            _book(B, ms(71980), [("0.6", "200")], [("0.75", "200")])]))
        out_.append(_line(hn(80020), "PONG"))
        out_.append(_line(hn(100020), _pc(B, ms(100000), "SELL", "0.7", "30")))
        out_.append(_line(hn(900500), _pc(A, ms(900480), "BUY", "0.15", "999")))
        out_.append(_line(hn(905000), event="close", code=1000, reason="end", seg=1))
    else:
        out_.append(_line(hn(-4000), [
            _book(A, ms(-4020), [("0.3", "100"), ("0.15", "500")], [("0.42", "60"), ("0.44", "305")]),
            _book(B, ms(-4020), [("0.6", "200")], [("0.75", "200")])]))
        steps = [(300000, {"market": A["cid"], "asset_id": A["tok"], "old_tick_size": "0.01",
                           "new_tick_size": "0.001", "timestamp": str(ms(300000)), "event_type": "tick_size_change"}),
                 (300100, _pc(A, ms(300100), "BUY", "0.305", "60")),
                 (600000, _pc(B, ms(600000), "BUY", "0.59", "40")),
                 (700000, _pc(A, ms(700000), "BUY", "0.305", "0")),
                 (700010, _book(A, ms(700000), [("0.3", "100"), ("0.15", "500")], [("0.42", "60"), ("0.44", "305")],
                                tick="0.001"))]
        for off, fr in steps:
            out_.append(_line(hn(off + 20), fr))
        out_.append(_line(hn(905000), event="close", code=1000, reason="end", seg=0))
    return out_


def synth_w_day(dirpath, d0=SYN_D0):
    paths = []
    for k, S in enumerate((d0, d0 + SLOT)):
        p = os.path.join(dirpath, "%d.0.stream.jsonl.gz" % S)
        with open(p, "wb") as raw, gzip.GzipFile(fileobj=raw, mode="wb", compresslevel=9, mtime=0) as fh:
            fh.write(("\n".join(synth_w_lines(S, k == 0)) + "\n").encode("utf-8"))
        paths.append((S, [p]))
    return paths


def synth_w_polls(d0=SYN_D0):
    A, B = SYN["A"]["cid"], SYN["B"]["cid"]
    t = lambda s: (d0 + s) * S_NS
    ta, tb = (Fr(2000), Fr(90)), (Fr(5000), Fr(70))     # each market's terms as its selection holds them
    return [(t(5), A, (Fr(100), Fr(1, 2)) + ta), (t(6), B, (Fr(50), Fr(1, 2)) + tb),
            (t(25), A, (Fr(100), Fr(3, 2)) + ta), (t(30), A, (Fr(100), Fr(1)) + ta), (t(930), A, None),
            (t(960), A, (Fr(120), Fr(1, 4)) + ta), (t(961), B, (Fr(50), Fr(1, 2)) + tb),
            (t(1700), A, (Fr(120), Fr(1, 4), Fr(5000), Fr(90))), (t(1750), A, (Fr(120), Fr(1, 4)) + ta)]


# the Architect's second implementation of rule W over the synthetic day: its lines and their SHA-256
SYN_W_REF = {"lines": 19, "digest": "04f7311ba7e277815b62b25c1d21f8414050eedbf59a1f780f796531d08d4b34"}


# TZ-43's reference over TZ-43's synthetic day, its own rule: its lines and their SHA-256 (TZ-43's SYN_REF)
SYN_REF = {"lines": 7, "digest": "04e6917ef2efbe42590a82967ef4e590033adefef27d41b8a278021330bd157b"}


def mode_selftest():
    import http.server
    import threading
    n = [0]

    def ok(cond, what):
        assert cond, "selftest: " + what
        n[0] += 1
        out("  ok  " + what)

    def fails(fn, exc=AssertionError):
        try:
            fn()
        except exc:
            return True
        return False

    tmp = os.path.join(WORK, "selftest-tmp")
    shutil.rmtree(tmp, ignore_errors=True)
    os.makedirs(tmp)
    # the constants
    ok(MALLOC_TUNED, "glibc took the 128 KiB mmap threshold and the two arenas")
    ok(utc(FIRST_D0) == "2026-11-09T00:00:00Z" and utc(LAST_D0) == "2026-11-16T00:00:00Z" and NEED == 5 and
       NONMEMBER_MAX == 3 and (LAST_D0 - FIRST_D0) // DAY + 1 == NEED + NONMEMBER_MAX,
       "candidates from 2026-11-09, at most 8 days to 2026-11-16, for 5 members")
    ok([s.name for s in SPECS] == ["pess-bt", "pess-br", "pess-ft", "pess-fr", "opt-bt", "opt-br", "opt-ft", "opt-fr",
                                   "central"] and all(s.rule == "w" and s.L == 50 * MS_NS for s in SPECS) and
       [(s.front, s.takers, s.denom) for s in SPECS] == [
           (False, True, "pess"), (False, False, "pess"), (True, True, "pess"), (True, False, "pess"),
           (False, True, "opt"), (False, False, "opt"), (True, True, "opt"), (True, False, "opt"),
           (False, True, "venue")] and EARN_FAMILY == ("pess-bt", "pess-br", "pess-ft", "pess-fr") and
       NO_EARN_FAMILY == ("opt-bt", "opt-br", "opt-ft", "opt-fr") and GATED == EARN_FAMILY + NO_EARN_FAMILY,
       "nine variants of rule W: every corner of the queue place and the crossing orders under the competitors' most "
       "and under their least, and the venue's figure")
    ok([(s.name, s.rule, s.front, s.takers, s.denom, s.L) for s in BASE_SPECS] == [
        ("pess", "alone", False, True, "pess", 50 * MS_NS), ("opt", "alone", True, False, "opt", 50 * MS_NS),
        ("central", "alone", False, True, "venue", 50 * MS_NS)] and
       (W_MS_MAX, W_COMP_MAX, W_BAND, W_INSIDE_MAX, CAP_CLIPS, SPREAD_TICKS) == (2000, Fr(1), (9, 10), 100, 1, 5),
       "TZ-43's three variants of its own rule, for its own lines; rule W's four constants")
    ok(THETA == D("10") and power(Fr(9, 10)) == Fr(59049, 100000) and
       q12(power(Fr(19, 20))) == "0.773780937500" and q12(power(Fr(99, 100))) == "0.950990049900" and
       Fr(1, 2 ** NEED) == Fr(1, 32) and q12(Fr(1, 32)) == "0.031250000000",
       "power 0.590490, 0.773781 and 0.950990 at 0.90, 0.95 and 0.99; each false reading 1/32")
    ok(DL_HEADERS == {"User-Agent": "btc-5m-twap-tz45", "Accept": "application/octet-stream"} and
       GAMMA_HEADERS == {"User-Agent": "btc-5m-twap-tz45", "Accept": "application/json"},
       "every request carries the TZ's two headers")
    lo = MEM_FLOOR - 1
    ok(MEM_FLOOR == 2 * -(-PEAK_BOUND * 58953728 // 49168384) == 172658448 and
       memory_gate([MEM_FLOOR]) == (True, MEM_FLOOR) and
       memory_gate([lo, lo, MEM_FLOOR]) == (True, MEM_FLOOR) and memory_gate([lo] * 5) == (False, lo) and
       fails(lambda: memory_gate([MEM_FLOOR, lo])) and fails(lambda: memory_gate([lo] * 6)),
       "the memory gate: a read at the floor or above passes; below it the next read decides, five reads at most")
    reads, slept = iter([lo, lo - 7, MEM_FLOOR + 3, lo]), []
    floor_check(read=lambda: next(reads), sleep=slept.append, freef=lambda: DISK_GATE)
    reads2, slept2 = iter([lo] * 5), []
    ok(slept == [MEM_RETRY_S] * 2 and (MEM_RETRY_S, MEM_READS) == (60, 5) and
       fails(lambda: floor_check(read=lambda: next(reads2), sleep=slept2.append, freef=lambda: DISK_GATE)) and
       slept2 == [MEM_RETRY_S] * 4 and
       fails(lambda: floor_check(read=lambda: MEM_FLOOR, sleep=slept2.append, freef=lambda: DISK_GATE - 1)),
       "floor_check reads MemAvailable again every 60 s while below its floor, passes at the first read at it or "
       "above, BLOCKS where five reads are below; it BLOCKS below the disk gate")
    # the venue's numbers as exact integers
    ok([price_int(x) for x in ("0.5", "0.505", "1", "0", "0.07")] == [500, 505, 1000, 0, 70] and
       [size_int(x) for x in ("12.34", "5", "0.1", "1000000")] == [1234, 500, 10, 100000000],
       "prices in thousandths and sizes in hundredths, exactly")
    ok(all(fails(lambda t=t: price_int(t)) for t in ("0.5051", "1e-3", "-0.5", ".5", "0.5 ")) and
       all(fails(lambda t=t: size_int(t)) for t in ("1.234", "1e2", "-1", "")),
       "any other text of a price or a size is a failed assert")
    # the competitors' bounds against every split of the displayed sides among two and three makers
    def f12(a, b, inside):
        return 4 * max(3 * min(a, b), max(a, b)) if inside else 12 * min(a, b)
    worst = []
    for A_, B_ in ((4, 4), (3, 9), (12, 4), (6, 1), (0, 5), (8, 8)):
        for inside in (True, False):
            sums = set()
            for a1 in range(A_ + 1):
                for b1 in range(B_ + 1):
                    for a2 in range(A_ - a1 + 1):
                        for b2 in range(B_ - b1 + 1):
                            sums.add(f12(a1, b1, inside) + f12(a2, b2, inside) +
                                     f12(A_ - a1 - a2, B_ - b1 - b2, inside))
            hi, lo = envelope(A_, B_, inside)
            worst.append((max(sums) == hi, min(sums) == lo))
    ok(all(a and b for a, b in worst), "the competitors' most and least, x 12, equal the extremes over every split "
                                       "of six pairs of sides among three makers, inside [0.10, 0.90] and outside")
    # one share by hand: market A's book, our bid at 0.41 and ask at 0.45, 20 shares each
    m = Market(dict(SYN["A"]), BASE_SPECS)
    m.replace({400: 10000, 380: 50000}, {460: 10000, 480: 30000})
    m.seeded = True
    o_b, o_a = Order("b", 410, 2000), Order("a", 450, 2000)
    for mv in m.mvs:
        mv.resting = [o_b, o_a]
    dd = Day(SYN_D0, [], BASE_SPECS)
    # mid 0.43; our distances 0.02, v 0.045: S = (25/45)^2; the book's 0.40 and 0.46 at 0.03: S = (15/45)^2
    sh = [Fr(*dd.share_of(m, mv, {})) for mv in m.mvs]
    q_ours = Fr(25, 45) ** 2 * 20
    A1 = B1 = Fr(15, 45) ** 2 * 100
    ok(sh[0] == q_ours / (q_ours + (2 * A1 + B1) / 3) and sh[1] == q_ours / (q_ours + (A1 + B1) / 4) and
       sh[2] == sh[0], "a share by hand: ours 20 (5/9)^2; the book's sides 100 (1/3)^2 each; pess against "
                       "(2A + B)/3, opt against (A + B)/4, the venue's before its first poll pess's")
    m.ven = ((Fr(2) * Fr(100) * m.vu * m.vu * SIZE_UNIT * 12).numerator, 1)
    sh = [Fr(*dd.share_of(m, mv, {})) for mv in m.mvs]
    ok(sh[0] == q_ours / (q_ours + 200) and sh[1] == q_ours / (q_ours + (A1 + B1) / 4) and
       sh[2] == q_ours / (q_ours + 200), "after a poll of competitiveness 2 at rate 100, the venue's 200: pess and "
                                          "central against it, opt against the book's least")
    # the synthetic day, against the Architect's reference and against its own rules by hand
    paths = synth_day(tmp)
    rows, book, day = replay_paths(SYN_D0, synth_members(), paths, SYN_D0 + 2 * SLOT, polls=synth_polls(),
                                   specs=BASE_SPECS)
    lines = compare_lines(rows, book)
    body = ("\n".join(lines) + "\n").encode("utf-8")
    ok(len(lines) == SYN_REF["lines"] and sha256_bytes(body) == SYN_REF["digest"],
       "TZ-43's rule on TZ-43's synthetic day, %d lines, byte for byte TZ-43's reference" % SYN_REF["lines"])
    f = {(M.cid[2:4], mv.sp.name): [(t // MS_NS - SYN_D0 * 1000, s, p, q, k) for t, s, p, q, k in mv.fills]
         for M in day.mk for mv in M.mvs}
    ok(f[("a1", "pess")] == [(10000, "b", 410, 2000, "m"), (50000, "a", 450, 1000, "x")] and
       f[("a1", "opt")] == [(10000, "b", 410, 2000, "m")] and f[("a1", "central")] == f[("a1", "pess")],
       "A: a sale of 30 at 0.40 fills our bid of 20 at 0.41, first; one minimum size long, no bid follows, so the ask "
       "placed at 0.41 meets none; a bid placed at 0.45 fills pess's and central's ask as a crossing order, never opt's")
    ok(f[("b2", "pess")] == f[("b2", "opt")] == [(110000, "a", 640, 3000, "m")],
       "B: once a 0.65 ask narrows the touch to five ticks and moves our ask to 0.64, a purchase of the 30 at 0.65 "
       "fills ours, 30 of 50")
    r = {(x["cid"][2:4], x["variant"]): x for x in rows}
    ok(r[("a1", "pess")]["n"]["refused"] == 1 and r[("a1", "opt")]["n"]["refused"] == 1 and
       r[("a1", "pess")]["x"] == 1000 and r[("a1", "pess")]["cost"] == 370000 and
       r[("a1", "pess")]["pnl"] == Fr(3, 5) and r[("a1", "pess")]["reb"] == Fr(73130, 80 * 10000),
       "A: an ask arriving after a bid of 0.45 came up is refused; pess long 10 at a cost of 3.70, marked at the "
       "day's last mid 0.43 for 0.60, its rebate 7.313 / 80")
    ok(r[("b2", "pess")]["pnl"] == Fr(-3, 20) and r[("b2", "pess")]["mark"] == "mid" and
       r[("a1", "pess")]["scored_ns"] == 1777770000000 and r[("a1", "opt")]["scored_ns"] == 1777720000000,
       "B: short 30 at 0.64 marked at 0.645; A scored 1,777.77 s of the 1,800 under pess and 1,777.72 under opt, "
       "unseeded from the close to the seed")
    ok(book == {"snapshots": 2, "touch_equal": 2, "book_equal": 2, "matches": 2, "subscribes": 1, "closes": 1} and
       day.c["polls"] == 6 and day.c["switches"] == 2 and day.c["skipped"] == 1,
       "2 book frames, both equal to the rebuilt book, 2 matches; 1 subscribe and 1 close inside the day, the "
       "slots' own before their instants not counted; 6 polls; the PONG skipped")
    slow = os.path.join(tmp, "slow")
    os.makedirs(slow)
    rows2, book2, day2 = replay_paths(SYN_D0, synth_members(), synth_day(slow, slow=True), SYN_D0 + 2 * SLOT,
                                      polls=synth_polls(), specs=BASE_SPECS)
    ok(compare_lines(rows2, book2) == lines and day2.c["fast"] == 0 and day.c["fast"] == 19,
       "the same lines through the JSON path alone: the fast path read 19 frames, the slow 0")
    rows3, book3, _d3 = replay_paths(SYN_D0, synth_members(), paths, SYN_D0 + 2 * SLOT, polls=synth_polls(),
                                     specs=BASE_SPECS)
    ok(compare_lines(rows3, book3) == lines, "a second replay of the same files: the same lines")
    # the day's money and L0's reading
    lit = [{"variant": v, "rew": "%s" % rw, "reb": "1/10", "pnl": "-1/2", "fills": 1, "fill_hu": 500,
            "crossed_hu": 0, "scored_ns": 3600 * S_NS, "mark": "mid", "cid": c}
           for v in ("pess", "opt", "central") for c, rw in (("x", "0.6"), ("y", "1.5"), ("z", "0.9"))]
    mp, mo, mc = (day_money(lit, v) for v in ("pess", "opt", "central"))
    ok(mp["total"] == Fr(3, 2) - Fr(3, 2) and mo["total"] == Fr(3) + Fr(3, 10) - Fr(3, 2) and
       mc["total"] == Fr(3, 2) + Fr(3, 10) - Fr(3, 2) and mp["paying"] == 1,
       "the 1-pUSD minimum: pess and central pay only a member's day at 1 or more, opt the day's sum; pess counts "
       "no rebate")
    T = THETA
    ok(l0_reading([T] * 5, [T] * 5) == ("EARN", True, False) and
       l0_reading([T] * 4 + [T - D("0.000001")], [T + 1] * 5) == ("UNDECIDABLE", False, False) and
       l0_reading([T - 1] * 5, [T - D("0.000001")] * 5) == ("NO EARN", False, True) and
       l0_reading([T] * 5, [T - 1] * 5) == ("UNDECIDABLE", True, True) and
       fails(lambda: l0_reading([T] * 4, [T] * 4)),
       "EARN where every day's least is 10 or more; NO EARN where every day's most is below; both or neither "
       "UNDECIDABLE; five days, never four")
    # the slot rules
    good = {"S": SYN_D0, "index": 0, "day": SYN_D0, "selection": {"sha256": "s"}, "markets": 2, "error": None,
            "joined_late": False, "stream": {"opened": True, "off_reason": None, "file": "%d.0.stream.jsonl.gz" % SYN_D0,
                                             "cut": False, "max_gap_ns": GAP_MAX_NS, "subscribed_wall_ns":
                                                 SYN_D0 * S_NS - 1, "first_frame_wall_ns": SYN_D0 * S_NS,
                                             "last_frame_wall_ns": (SYN_D0 + SLOT) * S_NS}}
    am = {(SYN_D0, "%d.0.stream.jsonl.gz" % SYN_D0): {}}
    sp_ = lambda **kw: slot_problem(SYN_D0, [dict(good, **kw)], "s", 2, am, SYN_D0)
    st_ = lambda **kw: sp_(stream=dict(good["stream"], **kw))
    ok(sp_() is None and sp_(index=1) == "records: index 0" and sp_(markets=3) == "records: another selection" and
       sp_(error="x") == "records: an error" and st_(cut=True) == "stream: cut" and
       st_(max_gap_ns=GAP_MAX_NS + 1) == "stream: a gap above 15 s" and
       st_(subscribed_wall_ns=SYN_D0 * S_NS + 1) == "stream: subscribed late" and
       st_(last_frame_wall_ns=(SYN_D0 + SLOT) * S_NS - 1) == "stream: ended early" and
       slot_problem(SYN_D0, [good], "s", 2, {}, SYN_D0) == "stream: not archived" and
       slot_problem(SYN_D0, [], "s", 2, am, SYN_D0) == "no slot record",
       "a slot qualifies with its records whole, subscribed by S, to S + 900, no gap above 15 s, archived")
    g2 = dict(good, index=1, stream=dict(good["stream"], file="%d.1.stream.jsonl.gz" % SYN_D0,
                                          first_frame_wall_ns=(SYN_D0 + 20) * S_NS))
    g1 = dict(good, stream=dict(good["stream"], last_frame_wall_ns=(SYN_D0 + 4) * S_NS))
    am2 = dict(am)
    am2[(SYN_D0, "%d.1.stream.jsonl.gz" % SYN_D0)] = {}
    ok(slot_problem(SYN_D0, [g1, g2], "s", 2, am2, SYN_D0) == "stream: a gap above 15 s between files" and
       slot_problem(SYN_D0, [g1, dict(g2, stream=dict(g2["stream"], first_frame_wall_ns=(SYN_D0 + 19) * S_NS))],
                    "s", 2, am2, SYN_D0) is None, "two files: a gap above 15 s between them fails, 15 s does not")
    # the archive's record on a temporary tree
    state = os.path.join(tmp, "archive")
    os.makedirs(os.path.join(state, "runs", "1793263627"))
    doc = {"tag": "rewardbook-streams-1793263627", "assets_n": 1, "bytes_total": 7, "assets": [
        {"T": 1793232000, "S": 1793232000, "k": 0, "file": "1793232000.0.stream.jsonl.gz",
         "asset": "1793232000-1793232000.0.stream.jsonl.gz", "bytes": 7, "sha256": "aa" * 32}]}
    raw = json.dumps(doc).encode()
    with open(os.path.join(state, "runs", "1793263627", "set.json"), "wb") as fh:
        fh.write(raw)
    recs = [{"run": 1793263627, "event": "set", "sha256": sha256_bytes(raw), "tag": doc["tag"], "assets_n": 1,
             "bytes_total": 7, "wall_ns": 1}, {"run": 1793263627, "event": "complete", "wall_ns": 2},
            {"run": 1793300000, "event": "set", "sha256": "bb" * 32, "tag": "x", "assets_n": 0, "bytes_total": 0,
             "wall_ns": 3}]
    sets = archived_sets(recs, state)
    ok(len(sets) == 1 and asset_map(sets) == {(1793232000, "1793232000.0.stream.jsonl.gz"): {
        "tag": doc["tag"], "asset": doc["assets"][0]["asset"], "bytes": 7, "sha256": "aa" * 32}},
       "a complete run's set.json, asserted by its set record's SHA-256, maps its file; a run with no complete "
       "record maps nothing")
    ok(fails(lambda: asset_map(sets + sets)) and
       fails(lambda: archived_sets([dict(recs[0], sha256="cc" * 32), recs[1]], state)),
       "a file in two sets, or a set.json other than its record's, is a failed assert")
    # the store's readers on a temporary day
    store = os.path.join(tmp, "store")
    dday = os.path.join(store, str(SYN_D0))
    os.makedirs(dday)
    A, B = SYN["A"], SYN["B"]
    gdocs = [{"conditionId": c["cid"], "feesEnabled": c is A,
              "feeSchedule": {"rate": 0.05, "rebateRate": 0.25, "takerOnly": True, "exponent": 1}} for c in (A, B)]
    rep = (json.dumps({"kind": "gamma", "status": 200, "raw": json.dumps(gdocs)}) + "\n").encode()
    rgz = os.path.join(dday, "select.0.replies.jsonl.gz")
    with open(rgz, "wb") as raw_, gzip.GzipFile(fileobj=raw_, mode="wb", mtime=0) as fh:
        fh.write(rep)
    selrec = {"ok": True, "replies": {"sha256": sha256_file(rgz)}, "members": [
        {"condition_id": c["cid"], "token_ids": [c["tok"], c["other"]], "min_size": str(Fr(c["ms"], 100)),
         "max_spread": str(D(c["vu"]) / 20), "rate": str(c["rate"])} for c in (A, B)]}
    with open(os.path.join(dday, "select.0.json"), "w") as fh:
        fh.write(json.dumps(selrec))
    sel = selection_of(SYN_D0, store)
    mem = members_of(sel)
    ok(sel["attempt"] == 0 and [(x["cid"], x["tok"], x["ms"], x["vu"], x["rate"], x["fee"]) for x in mem] == [
        (A["cid"], "1001", 2000, 90, Fr(100), Fr(1, 80)), (B["cid"], "2001", 5000, 70, Fr(50), Fr(0))],
       "the selection's members: first token, size and spread as integers, the rate, and the rebate coefficient "
       "0.05 x 0.25 where fees are enabled, 0 where not")
    os.remove(os.path.join(dday, "select.0.json"))
    with open(os.path.join(dday, "select.0.json"), "w") as fh:
        fh.write(json.dumps(dict(selrec, ok=False)))
    ok(selection_of(SYN_D0, store) is None, "a day whose only attempt is not ok has no selection")
    pz = os.path.join(dday, "%d.0.rewards.jsonl.gz" % SYN_D0)
    prow = lambda c, rate, comp, more=(), **terms: json.dumps({"data": [dict(
        {"condition_id": c, "market_competitiveness": comp, "rewards_config": [{"rate_per_day": rate}] + list(more)},
        **terms)]})
    cfgs = ({"rate_per_day": 999, "start_date": "1970-01-02", "end_date": "2500-12-31"},
            {"rate_per_day": 0.5, "start_date": "1969-12-31", "end_date": "1970-01-01"})
    lines_p = [{"recv_wall_ns": 7, "condition_id": B["cid"], "status": 200,
                "raw": prow(B["cid"], 50, 0.5, rewards_min_size=50, rewards_max_spread=3.5)},
               {"recv_wall_ns": 5, "condition_id": A["cid"], "status": 200,
                "raw": prow(A["cid"], 100, 2.25, cfgs, rewards_min_size=20.5, rewards_max_spread="4.5")},
               {"recv_wall_ns": 6, "condition_id": A["cid"], "status": 503, "raw": None},
               {"recv_wall_ns": 8, "condition_id": A["cid"], "status": 200, "raw": json.dumps({"data": []})}]
    with open(pz, "wb") as raw_, gzip.GzipFile(fileobj=raw_, mode="wb", mtime=0) as fh:
        fh.write(("\n".join(json.dumps(x) for x in lines_p) + "\n").encode())
    pls, cnt = polls_of(SYN_D0, {SYN_D0: [{"rewards": {"file": os.path.basename(pz)}}]}, store)
    ok(pls == [(5, A["cid"], (Fr(201, 2), Fr(9, 4), Fr(2050), None)),
               (7, B["cid"], (Fr(50), Fr(1, 2), Fr(5000), Fr(70))), (8, A["cid"], None)] and
       cnt == {"polls": 4, "unserved": 1, "no row": 1} and terms_of({}) == (None, None) and
       terms_of({"rewards_min_size": 20, "rewards_max_spread": D("4.5")}) == (Fr(2000), Fr(90)) and
       terms_of({"rewards_min_size": True, "rewards_max_spread": D("NaN")}) == (None, None),
       "the polls in order received: rate and competitiveness exact from their text, the rate summed over the "
       "configurations in force on the poll's date, and the row's own minimum size and maximum spread, none where "
       "the row states no number; an unserved poll dropped, a page with no row kept as the end of the reward")
    pf_path = os.path.join(tmp, "polls.jsonl")
    with open(pf_path, "w", encoding="utf-8") as fh:
        fh.write(polls_text(pls))
    pf = polls_read(pf_path)
    seen = [bool(pf), pf[0]]
    first = pf.popleft()
    ok(isinstance(pf, PollFile) and seen == [True, pls[0]] and first == pls[0] and pf[0] == pls[1] and
       list(pf) == pls[1:] and not pf and pf.fh is None and fails(lambda: pf.popleft()) and
       fails(lambda: polls_read(pf_path)[1]),
       "a day's polls read back from their file one line at a time, as a deque: the front, popleft, the rest in "
       "order, the file closed at its end")
    # the documents: an outcome only where a market reads closed with prices exactly 0 and 1
    dc = lambda closed, prices: {"closed": closed, "outcomePrices": json.dumps(prices),
                                 "clobTokenIds": json.dumps(["1001", "1002"])}
    ok(outcome_of(dc(True, ["1", "0"]), "1001") == 1000 and outcome_of(dc(True, ["1", "0"]), "1002") == 0 and
       outcome_of(dc(True, ["0.5", "0.5"]), "1001") is None and outcome_of(dc(False, ["1", "0"]), "1001") is None,
       "the first token's outcome, 1 or 0, from a closed document's prices; none otherwise")
    calls = []

    def fake_get(q):
        qs = urllib.parse.parse_qs(q)
        calls.append(qs)
        ids = qs["condition_ids"]
        closed = qs.get("closed") == ["true"]
        docs = [dict(dc(closed, ["0", "1"]), conditionId=i) for i in ids if i.endswith("1") == closed]
        return docs, 10, "dd" * 32, 0
    toks = {"0x" + "%063x1" % k if k % 2 else "0x" + "%063x2" % k: "1001" for k in range(60)}
    oc, reqs = documents(toks, holdf=lambda b: (0, 0), get=fake_get)
    ok(len(calls) == 4 and len(reqs) == 4 and all(len(c["condition_ids"]) <= DOC_CHUNK for c in calls) and
       sum(1 for v in oc.values() if v == 0) == 30 and sum(1 for v in oc.values() if v is None) == 30,
       "60 members in chunks of 50, each read open and closed: 30 closed at 0 for the first token, 30 open")
    ok(fails(lambda: documents(toks, holdf=lambda b: (0, 0), get=lambda q: ([], 2, "ee" * 32, 0))),
       "a member whose document neither request returns is a failed assert")
    # the clock
    st_idle = lambda: {"pairbook": "inactive", "rewardbook": "inactive"}
    ok(quiet(SYN_D0 + 900 * 10 + 15, 45, st_idle) is None and
       quiet(SYN_D0 + 900 * 10 + 14, 45, st_idle) == "second 14 of the window" and
       quiet(SYN_D0 + 900 * 10 + 546, 45, st_idle) == "second 546 of the window" and
       quiet(SYN_D0 + 900 * 4 + 20, 45, st_idle) is None and
       quiet(SYN_D0 + 5430, 20, st_idle) == CALENDAR[0][1] and
       quiet(SYN_D0 + 10820 + 10, 20, st_idle) == CALENDAR[1][1] and
       quiet(SYN_D0 + 900 * 10 + 15, 45, lambda: {"pairbook": "activating"}) is not None,
       "a unit starts from second 15 and ends by 590, clear of both archives' calendar runs and of their services")
    clk = [float(SYN_D0 + 900 * 10 + 580)]
    t_, w_ = hold(45, clock=lambda: clk[0], sleep=lambda s: clk.__setitem__(0, clk[0] + s), state_of=st_idle)
    ok(t_ == SYN_D0 + 900 * 11 + 15 and w_ == 335, "held from second 580 to the next window's second 15")
    # the reading's purity: G-STILL and NUMBER
    u = {"recorder": {"MainPID": "1", "NRestarts": "0", "ActiveState": "active"},
         "pairbook": {"MainPID": "2", "NRestarts": "3", "ActiveState": "active"},
         "rewardbook": {"MainPID": "4", "NRestarts": "1", "ActiveState": "active"},
         "advisor": {"MainPID": "5", "NRestarts": "0", "ActiveState": "active"}}
    u2 = json.loads(json.dumps(u))
    u2["pairbook"] = {"MainPID": "9", "NRestarts": "4", "ActiveState": "active"}
    u3 = json.loads(json.dumps(u2))
    u3["rewardbook"]["MainPID"] = "6"
    ok(still_reading(u, u, [])[0] and still_reading(u, u2, [{"stopped": "2", "NRestarts": "4", "pid": "9"}])[0] and
       not still_reading(u, u2, [])[0] and not still_reading(u, u3, [{"stopped": "2", "NRestarts": "4", "pid": "9"}])[0],
       "G-STILL: unchanged, or the pair book moved by its archive's restarts alone; any other change fails")
    names = ["CryptoTZ/TZ-44-l0-inputs-release.md", OWN_TZ, "CryptoReports/TZ-44-l0-inputs-release-report.md"]
    ok(OWN_TZ == "CryptoTZ/TZ-45-l0-rule-w.md" and number_reading(names, OWN_TZ)[0] and
       not number_reading(names + ["CryptoTZ/TZ-45-other.md"], OWN_TZ)[0] and
       not number_reading(names + ["CryptoReports/TZ-45-l0-rule-w-report.md"], OWN_TZ)[0] and
       not number_reading(names[:1], OWN_TZ)[0], "NUMBER: this file alone of its number, no report")
    # the hook
    ok(policy("fetch", "open", (RB_ROOT + "/%d/select.0.json" % FIRST_D0, "rb")) is None and
       policy("fetch", "open", (RB_ROOT + "/%d/select.0.json" % (FIRST_D0 - DAY), "rb")) is not None and
       policy("replay", "open", (RB_ROOT + "/%d/select.0.json" % FIRST_D0, "rb")) is not None and
       policy("fetch", "open", (RB_ROOT + "/%d/%d.0.stream.jsonl.gz" % (FIRST_D0, FIRST_D0), "rb")) is not None and
       policy("fetch", "os.listdir", (RB_ROOT + "/%d" % FIRST_D0,)) is None and
       policy("fetch", "os.listdir", (RB_ROOT,)) is not None and
       policy("archive", "open", (RB_LEDGER, "rb")) is None and policy("score", "open", (RB_LEDGER, "rb")) is not None
       and policy("still", "open", (PB_LEDGER, "rb")) is None and
       policy("replay", "urllib.Request", ("https://github.com/x",)) is None and
       policy("fetch", "urllib.Request", ("https://github.com/x",)) is not None and
       policy("fetch", "urllib.Request", ("https://gamma-api.polymarket.com/markets?x",)) is None and
       policy("replay", "urllib.Request", ("https://clob.polymarket.com/x",)) is not None and
       policy("replay", "open", (RECORDER + "/x", "rb")) is not None and
       policy("replay", "open", ("/root/elsewhere", "wb")) is not None and
       policy("reclaim", "open", (FORENSICS + "/x", "xb")) is None and
       policy("reclaim", "open", (FORENSICS + "/x", "wb")) is not None and
       policy("replay", "subprocess.Popen", ("curl", ["curl"])) is not None,
       "the hook: the store's day files to fetch alone and for the span's days, never a stream; each archive's "
       "record to its modes; Release downloads, gamma and nothing else; no write outside the work tree but the "
       "forensic store's exclusive creates; no process but git, systemctl and stat")
    # downloads on the loopback: a good asset, a corrupt reply retried, a 404 given up
    blob = b"stream bytes" * 1000
    hits = collections.Counter()

    class H(http.server.BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_GET(self):
            hits[self.path] += 1
            if self.path == "/t/bad" and hits[self.path] == 1:
                body = b"x" * len(blob)
            elif self.path in ("/t/good", "/t/bad"):
                body = blob
            else:
                self.send_response(404)
                self.end_headers()
                return
            self.send_response(200)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
    srv = http.server.HTTPServer(("127.0.0.1", 0), H)
    th = threading.Thread(target=srv.serve_forever, daemon=True)
    th.start()
    try:
        url_of = lambda t, a: "http://127.0.0.1:%d/%s/%s" % (srv.server_port, t, a)
        dest = os.path.join(tmp, "dl")
        n1 = download("t", "good", len(blob), sha256_bytes(blob), dest, url_of=url_of, sleep=lambda s: None)
        n2 = download("t", "bad", len(blob), sha256_bytes(blob), dest + "2", url_of=url_of, sleep=lambda s: None)
        ok(n1[0] == n2[0] == len(blob) and n1[2] == 0 and n2[2] == 1 and sha256_file(dest) == sha256_bytes(blob) and
           not os.path.exists(dest + "2.part"), "a download verified by bytes and SHA-256; a corrupt reply retried")
        ok(fails(lambda: download("t", "gone", 1, "ff" * 32, dest + "3", url_of=url_of, sleep=lambda s: None)) and
           hits["/t/gone"] == DL_TRIES, "a 404, as a repository not serving its Releases answers, is tried %d times, "
                                        "then BLOCKED" % DL_TRIES)
    finally:
        srv.shutdown()
        srv.server_close()
    # a unit removes its files whatever the replay does, and the projection blocks
    fake = lambda t, a, nb, sha, dst: (open(dst, "wb").close(), (0, 0.0, 0))[1]
    tim = os.path.join(tmp, "timing.jsonl")
    fl = [{"file": "%d.0.stream.jsonl.gz" % SYN_D0, "tag": "t", "asset": "a0", "bytes": 1, "sha256": "x"}]
    ok(fails(lambda: run_unit(SYN_D0, fl, os.path.join(tmp, "u"), lambda p: 1 / 0, tim, holdf=lambda b: (0.0, 0),
                              dl=fake), ZeroDivisionError) and not os.listdir(os.path.join(tmp, "u")),
       "a unit whose replay fails leaves no file behind")
    pj = Projection(10 ** 9, 100, after=2)
    pj({"cpu_s": 1.0, "bytes": 10 ** 6})
    ok(fails(lambda: pj({"cpu_s": 1.0, "bytes": 10 ** 6})), "a replay projected above its bound stops BLOCKED")
    # ---- rule W: its two prices by hand, its synthetic day against the second implementation and by hand --------------
    ok(w_targets(300, 420, 10, 90) == (320, 400) and w_targets(300, 400, 10, 90) == (310, 390) and
       w_targets(300, 399, 10, 90) == (None, None) and w_targets(300, 430, 10, 90) == (320, 400) and
       w_targets(305, 420, 1, 90) == (322, 403) and w_targets(300, 420, 10, 70) == (330, 390) and
       w_targets(300, 420, 10, 40) == (340, 370),
       "rule W by hand: 8 cents wide under a spread of 4.5, 6 under 3.5 and 3 under 2; a touch of 10 ticks is the least "
       "that leaves a tick on each side; the bid floored to the grid; 8.1 cents on a tick of a tenth of a cent")
    ok(w_targets(140, 420, 10, 90) == (240, 320) and w_targets(150, 420, 10, 90) == (240, 320) and
       w_targets(130, 420, 10, 90) == (None, None) and w_targets(150, 440, 10, 90) == (None, None) and
       w_targets(300, 420, 100, 90) == (None, None) and w_targets(300, 420, 10, 9) == (None, None),
       "rule W by hand: a price 0.10 inside the touch stands, one further in does not, on either side; no quote "
       "where 9/10 of twice the spread is under a tick")
    wdir = os.path.join(tmp, "w")
    os.makedirs(wdir)
    wpaths = synth_w_day(wdir)
    wrows, wbook, wday = replay_paths(SYN_D0, synth_members(), wpaths, SYN_D0 + 2 * SLOT, polls=synth_w_polls())
    wlines = compare_lines(wrows, wbook)
    wbody = ("\n".join(wlines) + "\n").encode("utf-8")
    ok(len(wlines) == SYN_W_REF["lines"] and sha256_bytes(wbody) == SYN_W_REF["digest"],
       "rule W's synthetic day, %d lines, byte for byte the Architect's second implementation" % SYN_W_REF["lines"])
    wf = {(M.cid[2:4], mv.sp.name): [(t // MS_NS - SYN_D0 * 1000, s, p, q, k) for t, s, p, q, k in mv.fills]
          for M in wday.mk for mv in M.mvs}
    met = [(10000, "b", 320, 2000, "m"), (40000, "a", 400, 1000, "x"), (65000, "a", 320, 2000, "m"),
           (1600000, "b", 322, 2000, "m")]
    ok(all(wf[("a1", v)] == met for v in ("pess-bt", "pess-ft", "opt-bt", "opt-ft", "central")) and
       all(wf[("a1", v)] == met[:1] + met[2:] for v in ("pess-br", "pess-fr", "opt-br", "opt-fr")) and
       all(wf[("b2", v[0])] == [] for v in VARIANTS),
       "A under rule W: no quote before its first poll; a sale of 30 at 0.30 fills the bid of 20 at 0.32; one minimum "
       "size long, no bid follows; a bid arriving at 0.40 takes 10 of the ask where crossing orders are takers and "
       "nothing where they are refused; a purchase at 0.42 fills the ask at 0.32; on a tick of 0.001 the bid at 0.322 "
       "is sold into. B, 50 shares a clip, is never quoted")
    wr = {(x["cid"][2:4], x["variant"]): x for x in wrows}
    ok(all(wr[("a1", v[0])]["hit_d"] == 100 and wr[("a1", v[0])]["hit"] == 200000 for v in VARIANTS) and
       all(wr[("b2", v[0])]["hit"] == 0 and wr[("b2", v[0])]["n"]["sent"] == 0 for v in VARIANTS) and
       (wr[("a1", "pess-bt")]["x"], wr[("a1", "pess-bt")]["cost"], wr[("a1", "pess-bt")]["pnl"]) ==
       (1000, 244000, Fr(29, 25)) and
       (wr[("a1", "pess-br")]["x"], wr[("a1", "pess-br")]["cost"], wr[("a1", "pess-br")]["pnl"]) ==
       (2000, 644000, Fr(19, 25)) and wr[("a1", "pess-bt")]["reb"] == Fr(1547032, 8000000) and
       wr[("a1", "pess-bt")]["n"] == {"sent": 22, "cancels": 20, "refused": 0, "crossings": 1, "fills": 4} and
       wr[("a1", "pess-br")]["n"] == {"sent": 19, "cancels": 17, "refused": 0, "crossings": 0, "fills": 3},
       "A's adverse hit: the ask at 0.32 under a touch of 0.15 to 0.42 stands 0.10 inside it, 20 shares, 2.00; met by "
       "the crossing order long 10 at a cost of 2.44, marked at the last mid 0.36 for 1.16, not met long 20 for 0.76; "
       "the row of 50 shares at 1,700 s cancels the two quotes then live, and the row of 20 after it sends none")
    kept_ = Fr(100 * 2400000 * 498, 488400000 * 8640000)
    dw_ = Day(SYN_D0, synth_members(), SPECS)
    dw_.poll(SYN_D0 * S_NS, SYN["A"]["cid"], (Fr(100), Fr(1, 2)))
    dw_.poll(SYN_D0 * S_NS, SYN["B"]["cid"], (Fr(50), Fr(1, 2), Fr(5000), Fr(70)))
    ok(all(wr[("a1", v)]["scored_ns"] == 5030 * MS_NS and abs(Fr(wr[("a1", v)]["rew"]) - kept_) < Fr(1, 10 ** 40)
           for v in EARN_FAMILY + ("central",)) and
       all(wr[("a1", v)]["rew"] > 2 and wr[("a1", v)]["scored_ns"] > 1600 * S_NS for v in NO_EARN_FAMILY) and
       [M.moved for M in wday.mk] == [True, False] and [M.moved for M in dw_.mk] == [True, False] and
       [M.moved for M in day.mk] == [False, False],
       "the venue's terms: but for the opt family A is credited through the last poll whose row confirmed them - "
       "4.98 s of both quotes at a share of 2.4 in 488.4 under the first poll's figure, and the 0.05 s a quote "
       "outlives the page with no row, at no rate - and nothing of the fifteen minutes before that page, nor of "
       "what came before the row of 50 shares; the opt family keeps both; a row that states no terms is a row of "
       "other terms; TZ-43's rule reads none")
    ok(wbook == {"snapshots": 3, "touch_equal": 3, "book_equal": 3, "matches": 3, "subscribes": 1, "closes": 1} and
       wday.c["polls"] == 9 and wday.rule == "w" and day.rule == "alone" and
       fails(lambda: Day(SYN_D0, [], (SPECS[0], BASE_SPECS[0]))),
       "3 book frames, each equal to the rebuilt book, 3 matches; 9 polls; a day replays one rule, never two")
    hl = [{"variant": v, "rew": rw, "reb": "1/4", "pnl": "-1/2", "fills": 1, "fill_hu": 500, "crossed_hu": 0,
           "scored_ns": 3600 * S_NS, "mark": "mid", "cid": c, "hit": h_, "hit_d": 10}
          for v in ("pess-bt", "pess-br", "pess-ft", "pess-fr", "opt-bt", "opt-br", "opt-ft", "opt-fr", "central")
          for c, rw, h_ in (("x", "0.6", 20000), ("y", "12.5" if v != "pess-br" else "11.5", 0),
                            ("z", "0.9" if v != "opt-ft" else "1.9", 150000))]
    hm = {v[0]: day_money(hl, v[0]) for v in VARIANTS}
    (lo_, lo_n), (hi_, hi_n) = day_brackets(hm)
    ok(hm["pess-bt"]["total"] == Fr(25, 2) - Fr(3, 2) and hm["pess-bt"]["hits"] == Fr(17, 10) and
       hm["pess-bt"]["gated"] == Fr(11) - Fr(17, 10) and hm["pess-bt"]["quoting"] == 2 and
       hm["opt-bt"]["total"] == Fr(14) + Fr(3, 4) - Fr(3, 2) == hm["opt-bt"]["gated"] and
       hm["central"]["gated"] == Fr(25, 2) + Fr(3, 4) - Fr(3, 2) and
       (lo_, lo_n) == (Fr(10) - Fr(17, 10), "pess-br") and (hi_, hi_n) == (Fr(15) + Fr(3, 4) - Fr(3, 2), "opt-ft"),
       "a day's money with its hits: the EARN family is gated less one minimum size at the day's largest distance "
       "in every quoting market, the NO EARN family and central are not; the day's least and most, by variant")
    rp_ = rehearsal_polls([{"cid": "c%03d" % i} for i in range(150)], REHEARSAL_D0)
    own_ = (Fr(2000), Fr(40))
    ok(len(rp_) == 600 and rp_[0] == ((REHEARSAL_D0 + 30) * S_NS, "c000", (Fr(100), Fr(0)) + own_) and
       rp_[152] == ((REHEARSAL_D0 + SLOT + 32) * S_NS, "c002", (Fr(100), Fr(3, 2)) + own_) and
       rp_[155] == ((REHEARSAL_D0 + SLOT + 35) * S_NS, "c005", (Fr(100), Fr(1, 2), Fr(5000), own_[1])) and
       rp_[303] == ((REHEARSAL_D0 + 2 * SLOT + 33) * S_NS, "c003", None) and
       rp_[305] == ((REHEARSAL_D0 + 2 * SLOT + 35) * S_NS, "c005", (Fr(100), Fr(1)) + own_) and
       rp_[459] == ((REHEARSAL_D0 + 3 * SLOT + 39) * S_NS, "c009", (Fr(100), Fr(1), own_[0], None)) and
       sum(1 for p_ in rp_ if p_[2] is None) == 21 and
       sum(1 for p_ in rp_ if p_[2] is not None and p_[2][2:] != own_) == 14 + 11 and
       rp_ == sorted(rp_, key=lambda p_: (p_[0], p_[1])) and
       REHEARSAL_W == {"ms": 2000, "vu": 40, "rate": Fr(100), "fee": Fr(1, 80)} and
       REF_BASE == {"lines": 451, "digest": "1ab40f4b2a9b4f263e92959dc78a67dc9583731889cce70b22edad59091944cd"},
       "the rehearsal's polls for rule W: 150 members a slot, four slots, the figure 0 to 2 by halves, the "
       "rehearsal's own terms but 14 rows of 50 shares in the second slot and 11 of no spread in the fourth, 21 "
       "pages with no row; TZ-43's rule against TZ-43's own digest")
    # ---- the Release: the hook's decisions for pack, upload and verify -----------------------------------------------------
    PACK_DAYS[:] = [FIRST_D0, FIRST_D0 + DAY]
    d1, dr = RB_ROOT + "/%d" % FIRST_D0, RB_ROOT + "/%d" % (FIRST_D0 + 2 * DAY)
    ok(policy("pack", "os.listdir", (d1,)) is None and
       policy("pack", "os.listdir", (RB_ROOT + "/%d" % (FIRST_D0 + DAY),)) is None and
       policy("pack", "os.listdir", (dr,)) is not None and policy("pack", "os.listdir", (RB_ROOT,)) is not None and
       policy("upload", "os.listdir", (d1,)) is not None and policy("pack", "os.scandir", (d1,)) is None and
       policy("pack", "open", (d1 + "/select.0.json", "rb", 0)) is None and
       policy("pack", "open", (d1 + "/select.1.replies.jsonl.gz", "rb", 0)) is None and
       policy("pack", "open", (d1 + "/%d.0.slot.json" % (FIRST_D0 + 900), "rb", 0)) is None and
       policy("pack", "open", (d1 + "/%d.1.rewards.jsonl.gz" % (FIRST_D0 + 900), "rb", 0)) is None and
       policy("pack", "open", (d1 + "/%d.0.stream.jsonl.gz" % (FIRST_D0 + 900), "rb", 0)) is not None and
       policy("pack", "open", (dr + "/select.0.json", "rb", 0)) is not None and
       policy("pack", "open", (RB_ROOT + "/runtime.jsonl", "rb", 0)) is not None and
       policy("pack", "open", (d1 + "/select.0.json", "wb", 0)) is not None and
       policy("verify", "open", (d1 + "/select.0.json", "rb", 0)) is not None and
       policy("fetch", "open", (dr + "/select.0.json", "rb", 0)) is None,
       "pack lists and reads the days the set considered and no other: a selection, a slot record or a poll file, "
       "never a stream, the root or a write; fetch reads the span's")
    PACK_DAYS[:] = []
    ok(policy("pack", "os.listdir", (d1,)) is not None and policy("pack", "open", (d1 + "/select.0.json", "rb", 0))
       is not None and policy("upload", "urllib.Request", ("https://api.github.com/repos/x",)) is None and
       policy("upload", "urllib.Request", ("https://uploads.github.com/repos/x",)) is None and
       policy("upload", "urllib.Request", ("https://github.com/x",)) is not None and
       policy("verify", "urllib.Request", ("https://github.com/x/releases/download/t/a",)) is None and
       policy("verify", "urllib.Request", ("https://release-assets.githubusercontent.com/x",)) is None and
       policy("verify", "urllib.Request", ("https://objects.githubusercontent.com/x",)) is None and
       policy("verify", "urllib.Request", ("https://uploads.github.com/x",)) is not None and
       policy("pack", "urllib.Request", ("https://api.github.com/x",)) is not None and
       policy("score", "urllib.Request", ("https://github.com/x",)) is not None and
       policy("upload", "subprocess.Popen", ("/usr/bin/gh", ["gh"], None, None)) is None and
       policy("verify", "subprocess.Popen", ("/usr/bin/gh", ["gh"], None, None)) is not None and
       policy("pack", "open", (OUT + "/x.part", "wb", 0)) is None and
       policy("pack", "open", (FORENSICS + "/x", "xb", 0)) is not None,
       "before the set names its days pack reads none; upload reaches GitHub's API and upload host, verify the API "
       "and the download hosts, no other mode either; gh in upload alone, for TZ-27's credential")
    ok(tz27.UA == "btc-5m-twap-tz27" and tz27.CONTENT_TYPE == "application/octet-stream" and tz27.WORK[0] == WORK and
       TAG == "tz-45-l0-rule-w-inputs" and asset_name("fetch/1794182400.polls.jsonl") == "tz45-fetch-1794182400.polls.jsonl"
       and asset_name("reading.json") == "tz45-reading.json" and
       re.fullmatch(r"[a-z0-9][a-z0-9.-]*", asset_name("days/1794182400.slots.txt")) is not None and
       budget_s(0) == 5 and budget_s(2000000) == 6 and budget_s(2000001) == 7 and budget_s(200000000) == 105,
       "GitHub's requests under TZ-27's agent, every asset octet-stream, TZ-27's work tree this one; a file's name in "
       "the Release; a transfer's budget 5 s and its bytes at 2,000,000 a second")
    t0_ = 1794391200
    rec_ = lambda a, b: {"start_ns": int(a * 1e9), "end_ns": int(b * 1e9), "waited_s": 1.5}
    ok(transfer_summary([rec_(t0_ + 15, t0_ + 20), rec_(t0_ + 14, t0_ + 20), rec_(t0_ + 580, t0_ + 591),
                         rec_(t0_ + 580, t0_ + 905)]) == (4, 1, 2, 6.0) and
       tag_reading("a" * 40, None, "a" * 40) and not tag_reading("a" * 40, "b" * 40, "a" * 40) and
       not tag_reading("b" * 40, None, "a" * 40) and not tag_reading(None, None, "a" * 40),
       "a transfer's place: started at second 15 to 590 of its window, ended in it by 590; G-TAG: a lightweight tag "
       "at the instrument's commit")
    # ---- the store's names, a stored reply's body, a day's archive ---------------------------------------------------------
    d0 = FIRST_D0
    ok(classify(d0, "select.0.json") == "select" and classify(d0, "select.12.replies.jsonl.gz") == "select" and
       classify(d0, "%d.0.slot.json" % (d0 + 900)) == "slot" and
       classify(d0, "%d.1.rewards.jsonl.gz" % (d0 + 85500)) == "rewards" and
       classify(d0, "%d.0.stream.jsonl.gz" % d0) == "stream" and classify(d0, "runtime.jsonl") == "other" and
       classify(d0, "select.0.json.tmp") == "other" and classify(d0, "x") == "other" and
       fails(lambda: classify(d0, "%d.0.slot.json" % (d0 + DAY))) and
       fails(lambda: classify(d0, "%d.0.slot.json" % (d0 + 450))),
       "a day's names: selections, slot records and polls are members; streams and every other name are not; a slot "
       "of another day or off the 900 s grid is a failed assert")
    pstore, outd, outd2 = os.path.join(tmp, "pstore"), os.path.join(tmp, "out"), os.path.join(tmp, "out2")
    for p_ in (outd, outd2):
        os.makedirs(p_)
    ddir = os.path.join(pstore, str(d0))
    os.makedirs(ddir)

    def gz_lines(recs_):
        return gzip.compress("".join(json.dumps(r_) + "\n" for r_ in recs_).encode("utf-8"), mtime=0)

    page = "<html><span id=cf-footer-ip>203.0.113.7</span></html>"
    served = [{"status": 200, "raw": json.dumps({"data": [{"condition_id": "0x01"}]})}, {"status": None, "raw": ""},
              {"status": 200, "raw": "[]"}, {"status": 503, "raw": None}]
    ok(all(body_reason(r_) is None for r_ in served) and body_reason({"status": 200}) is None and
       body_reason({"status": 502, "raw": page}) == "a body under status 502" and
       body_reason({"status": None, "raw": page}) == "a body under status of no number" and
       body_reason({"status": 200, "raw": page}) == "a status-200 body that is not JSON" and
       body_reason({"status": 200, "raw": "7"}) == "a status-200 body that is not a JSON document" and
       body_reason({"status": 200, "raw": 7}) == "a body that is not text" and body_reason([1]) == "not a record",
       "a stored reply's body is published only where the venue served it as a JSON document under status 200")
    blobs = {"select.0.json": b'{"day": 1}\n', "select.0.replies.jsonl.gz": gz_lines(served * 300),
             "%d.0.slot.json" % (d0 + 41400): b'{"S": 1}\n', "%d.0.rewards.jsonl.gz" % (d0 + 41400): gz_lines(served),
             "%d.1.slot.json" % (d0 + 46800): b'{"S": 2}\n',
             "%d.1.rewards.jsonl.gz" % (d0 + 46800): gz_lines(served[:1])}
    held_back = {"%d.0.rewards.jsonl.gz" % (d0 + 42300): gz_lines(served + [{"status": 502, "raw": page}]),
                 "%d.0.rewards.jsonl.gz" % (d0 + 43200): gz_lines([{"status": 200, "raw": page}]),
                 "%d.0.rewards.jsonl.gz" % (d0 + 44100): gz_lines(served * 50)[:-9],
                 "select.1.replies.jsonl.gz": b"no gzip stream at all\n" + gz_lines(served)}
    others = {"%d.0.stream.jsonl.gz" % (d0 + 41400): b"STREAM-BYTES" * 100, "notes.txt": b"OTHER-BYTES"}
    for k_, v_ in list(blobs.items()) + list(held_back.items()) + list(others.items()):
        with open(os.path.join(ddir, k_), "wb") as fh:
            fh.write(v_)
    why = {k_: withhold_reason(os.path.join(ddir, k_)) for k_ in sorted(held_back)}
    ok(all(withhold_reason(os.path.join(ddir, k_)) is None for k_ in blobs if k_.endswith(SCANNED)) and
       [why[k_] for k_ in sorted(held_back)] == ["line 5: a body under status 502",
                                                "line 1: a status-200 body that is not JSON",
                                                "not a whole gzip file: EOFError",
                                                "not a whole gzip file: BadGzipFile"] and
       not any("203.0.113.7" in w_ or "cf-footer-ip" in w_ for w_ in why.values()),
       "a file of replies is withheld by its first line that carries another body, or where it is no whole gzip file, "
       "and the reason names a line's number, never its content")
    ok(day_budget(0) == PACK_BASE_S == 30 and day_budget(1) == 31 and day_budget(16300000) == 63 and
       DAY_MAX_BYTES == 60000000 and day_budget(DAY_MAX_BYTES) == 150 <= IDLE[1] - IDLE[0] and
       SCAN_RATE == 500000 and SOURCE_BUDGET_S == 60,
       "a day's unit is held for 30 s and its members' bytes at 500,000 a second, 150 s at the day's bound")
    e1, s1 = pack_day(pstore, d0, outd, freef=lambda: DISK_FLOOR + 10 ** 7)
    e2, s2 = pack_day(pstore, d0, outd2, freef=lambda: DISK_FLOOR + 10 ** 7)
    e3, s3 = pack_day(pstore, d0, outd, freef=lambda: DISK_FLOOR + 10 ** 7)
    with open(os.path.join(outd, ARCHIVE_FMT % d0), "rb") as fh:
        tar_bytes = fh.read()
    with tarfile.open(os.path.join(outd, ARCHIVE_FMT % d0)) as tf:
        got = {m_.name: (m_.mtime, m_.uid, m_.gid, m_.mode, m_.isreg(), tf.extractfile(m_).read())
               for m_ in tf.getmembers()}
    ok(s1 == s2 == "wrote" and s3 == "unchanged" and e1["sha256"] == e2["sha256"] == e3["sha256"] and
       e1 == e3 and len(tar_bytes) == e1["bytes"] and sha256_bytes(tar_bytes) == e1["sha256"] and
       not os.path.exists(os.path.join(outd, ARCHIVE_FMT % d0 + ".part")),
       "a day's archive: the same bytes from two trees and from a second run, written once, no part left")
    ok(sorted(got) == sorted("%d/%s" % (d0, k_) for k_ in blobs) and
       all(got["%d/%s" % (d0, k_)][5] == v_ for k_, v_ in blobs.items()) and
       all(g_[:5] == (d0, 0, 0, 0o644, True) for g_ in got.values()) and
       [r_["name"] for r_ in e1["members"]] == sorted("%d/%s" % (d0, k_) for k_ in blobs) and
       all(r_["sha256"] == sha256_bytes(blobs[r_["name"].split("/", 1)[1]]) and
           r_["bytes"] == len(blobs[r_["name"].split("/", 1)[1]]) for r_ in e1["members"]),
       "every member stored verbatim under <D0>/<name>, in name order, its mtime D0, mode 644, owner 0, and its "
       "bytes and SHA-256 in the manifest's entry")
    ok(b"STREAM-BYTES" not in tar_bytes and b"OTHER-BYTES" not in tar_bytes and
       e1["counts"] == {"select": 3, "slot": 2, "rewards": 5, "stream": 1, "other": 1} and
       sorted((x_["kind"], x_["name"], x_["bytes"]) for x_ in e1["excluded"]) ==
       [("other", "notes.txt", 11), ("stream", "%d.0.stream.jsonl.gz" % (d0 + 41400), 1200)] and
       e1["members_n"] == len(blobs) == 6 and e1["scanned_n"] == 7 and e1["withheld_n"] == 4 and
       e1["member_bytes"] == sum(len(v_) for v_ in blobs.values()) and
       [(w_["name"], w_["bytes"], w_["reason"]) for w_ in e1["withheld"]] ==
       [(k_, len(held_back[k_]), why[k_]) for k_ in sorted(held_back)] and
       not any(("%d/%s" % (d0, k_)) in got for k_ in held_back) and
       not any(v_ in tar_bytes for v_ in held_back.values()),
       "the stream and the stray name are listed by their bytes and never stored; a withheld file is in no archive, "
       "named by its bytes and its reason")
    ok(fails(lambda: pack_day(pstore, d0, outd2, freef=lambda: DISK_FLOOR)) and
       fails(lambda: pack_day(pstore, d0 + DAY, outd2, freef=lambda: DISK_FLOOR + 10 ** 7)),
       "a day BLOCKS where its archive would leave free space under the floor, and where its directory is absent")
    # ---- this run's own files, the set and the manifest, on a synthetic tree -------------------------------------------------
    srcd = os.path.join(tmp, "worktree")
    for sub in ("fetch", "days"):
        os.makedirs(os.path.join(srcd, sub))

    def put(rel_, data_):
        with open(os.path.join(srcd, rel_), "wb") as fh_:
            fh_.write(data_)
        return sha256_bytes(data_)

    sp_sha = put("fetch/%d.polls.jsonl" % d0, b"[1]\n")
    rec_sha = put("fetch/%d.json" % d0, dumps({"polls": {"sha256": sp_sha}}).encode("utf-8"))
    dj, ds = put("days/%d.json" % d0, b'{"rows": []}\n'), put("days/%d.slots.txt" % d0, b"slot line\n")
    sdoc_ = {"members": [d0], "days": {str(d0): {"sha256": rec_sha}},
             "considered": [{"d0": d0, "member": True, "reason": None},
                            {"d0": d0 + DAY, "member": False, "reason": "slot"}]}
    st_ = {"fetch": {"set_sha256": put("set.json", dumps(sdoc_).encode("utf-8"))},
           "score": {"reading_sha256": put("reading.json", dumps({"inputs": {str(d0): {"day": dj, "slots": ds}}})
                                           .encode("utf-8"))}}
    srows = work_sources(sdoc_, st_, root=srcd)
    put("days/%d.slots.txt" % d0, b"slot line!\n")
    ok([r_["asset"] for r_ in srows] == ["tz45-set.json", "tz45-reading.json", "tz45-fetch-%d.json" % d0,
                                        "tz45-fetch-%d.polls.jsonl" % d0, "tz45-days-%d.json" % d0,
                                        "tz45-days-%d.slots.txt" % d0] and
       [r_["sha256"] for r_ in srows][2:] == [rec_sha, sp_sha, dj, ds] and
       fails(lambda: work_sources(sdoc_, st_, root=srcd)) and
       fails(lambda: work_sources(sdoc_, dict(st_, fetch={"set_sha256": "0" * 64}), root=srcd)),
       "G-SOURCE: the set, the reading and a member day's four files, each equal to this run's own record of it; one "
       "byte more is a BLOCK")
    rdoc = set_doc([e1], srows, 99, "f" * 64)
    mdoc = manifest_doc("c" * 40, "f" * 64, [e1], srows, sdoc_)
    rname, rbody = release_text(rdoc, "c" * 40, mdoc)
    ok(rdoc["assets_n"] == 8 and [x_["asset"] for x_ in rdoc["assets"]] == [ARCHIVE_FMT % d0] +
       [r_["asset"] for r_ in srows] + [MANIFEST] and
       tz27.store_path(UPLOAD_ROOT, rdoc["assets"][0]) == os.path.join(OUT, ARCHIVE_FMT % d0) and
       tz27.store_path(UPLOAD_ROOT, rdoc["assets"][1]) == os.path.join(WORK, "set.json") and
       tz27.store_path(UPLOAD_ROOT, rdoc["assets"][4]) == os.path.join(WORK, "fetch", "%d.polls.jsonl" % d0) and
       rdoc["bytes_total"] == e1["bytes"] + sum(r_["bytes"] for r_ in srows) + 99 and
       tz27.json_bytes(mdoc) == tz27.json_bytes(manifest_doc("c" * 40, "f" * 64, [e1], srows, sdoc_)) and
       mdoc["unread_from_D0"] == d0 + 2 * DAY and mdoc["members"] == [d0] and
       rname == "%s: the inputs of L0's second gate - the reward book's days 2026-11-09 to 2026-11-10 and TZ-45's "
       "work files" % TAG and "2 candidate days" in rbody and "No day from %d is here" % (d0 + 2 * DAY) in rbody,
       "the Release's set: the archives, this run's files and the manifest, each found by TZ-27's store_path; the "
       "manifest the same bytes from the same inputs, naming the first day no one has read")
    vp = os.path.join(tmp, "verify.json")
    with open(vp, "wb") as fh:
        fh.write(dumps({"assets": [{"asset": "a", "sha256": "1" * 64, "download_ok": True},
                                   {"asset": "b", "sha256": "2" * 64, "download_ok": False}]}).encode("utf-8"))
    ok(released_by(vp) == {"1" * 64: "a"} and released_by(os.path.join(tmp, "absent.json")) == {} and
       by_name(WORK, "verify.json") and by_name(WORK, "logs/40-fetch.log") and not by_name(WORK, "out/x.tar") and
       reclaimable(WORK) and not reclaimable("/tmp") and not reclaimable("/root/tz44-work"),
       "reclaim leaves to the Release a file verify proved it holds, and copies it where verify did not; this TZ's "
       "tree, or a UUID directory beside a btc-5m-twap session's, and nothing else")
    # ---- the loopback GitHub: TZ-27's own stand-in, our client, our set ----------------------------------------------------
    for k_ in [k_ for k_ in list(os.environ) if k_.lower() in ("http_proxy", "https_proxy", "all_proxy", "no_proxy")]:
        del os.environ[k_]
    tok = "ghp_" + "Ab3" * 12
    Fake = tz27._FakeGitHub
    Fake.releases.clear()
    Fake.assets.clear()
    Fake.hits.clear()
    Fake.refuse_once.clear()
    Fake.omit_digest[0] = False
    Fake.token = tok
    bodies = []
    orig_post = Fake.do_POST

    def do_post(handler):
        if handler.path.endswith("/releases"):
            n_ = int(handler.headers.get("Content-Length") or 0)
            raw_ = handler.rfile.read(n_)
            bodies.append(json.loads(raw_))
            import io
            handler.rfile = io.BytesIO(raw_)
        return orig_post(handler)

    Fake.do_POST = do_post
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Fake)
    th = threading.Thread(target=srv.serve_forever, daemon=True)
    th.start()
    sep = ":" + "//"
    lb = "http" + sep + "127.0.0.1:%d" % srv.server_address[1]
    Fake.web = lb
    try:
        root = os.path.join(tmp, "up")
        os.makedirs(os.path.join(root, "a"))
        files = {"one.tar": os.urandom(3000), "tz45-set.json": b'{"x": 1}\n', MANIFEST: b"{}\n"}
        assets = []
        for name, data in files.items():
            with open(os.path.join(root, "a", name), "wb") as fh:
                fh.write(data)
            assets.append({"T": "a", "file": name, "asset": name, "bytes": len(data), "sha256": sha256_bytes(data)})
        doc = {"tag": TAG, "assets": assets, "assets_n": 3, "bytes_total": sum(x_["bytes"] for x_ in assets)}
        trs, logs = [], []
        nowait = lambda budget: (time.time(), 0.0)
        gh = Gh45(token=tok, record=trs.append, held=nowait, commit="c" * 40, api=lb, uploads=lb, web=lb)
        gh.gap_s = 0.0
        rel = gh.create_release(TAG, *release_text(doc, "c" * 40, mdoc))
        sent, held_n = tz27.upload_set(gh, rel, doc, root, logs.append, wait_min=0)
        anon = Gh45(token=None, record=trs.append, held=nowait, api=lb, uploads=lb, web=lb)
        anon.sizes = {x_["asset"]: x_["bytes"] for x_ in assets}
        rel2, vrows, missing, extra = tz27.verify_release(anon, TAG, doc)
        checks = tz27.release_reading(rel2, TAG, vrows, missing, extra)
        ok(bodies and bodies[-1]["tag_name"] == TAG and bodies[-1]["target_commitish"] == "c" * 40 and
           bodies[-1]["draft"] is False and bodies[-1]["make_latest"] == "false" and sent == 3 and held_n == 0 and
           all(checks.values()) and len(vrows) == 3 and all(r_["download_ok"] for r_ in vrows),
           "loopback: the Release on the tag at the commit, three assets sent, and every one proved by the API's "
           "record and a full download with no token")
        ok(all(h_[2] == tz27.UA for h_ in Fake.hits) and
           all(h_[3] is None for h_ in Fake.hits if "/releases/download/" in h_[1] or h_[1].startswith("/blob/")) and
           len([t_ for t_ in trs if t_["kind"] == "upload"]) == 3 and
           len([t_ for t_ in trs if t_["kind"] == "download"]) == 3 and all(t_["ok"] for t_ in trs),
           "every request under TZ-27's agent, every read with no token, every transfer held and recorded")
        sent2, held2 = tz27.upload_set(gh, rel, doc, root, logs.append, wait_min=0)
        aid = [a_ for a_, x_ in Fake.assets.items() if x_["name"] == "one.tar"][0]
        Fake.assets[aid]["data"] = b"x" + Fake.assets[aid]["data"][1:]
        rel3, vrows3, m3, x3 = tz27.verify_release(anon, TAG, doc)
        checks3 = tz27.release_reading(rel3, TAG, vrows3, m3, x3)
        ok(sent2 == 0 and held2 == 3 and not checks3["every download the set's bytes and SHA-256"] and
           not all(checks3.values()),
           "a second upload holds all three; a changed byte served is a failed download")
    finally:
        Fake.do_POST = orig_post
        srv.shutdown()
        srv.server_close()
    shutil.rmtree(tmp)
    ok(not os.path.exists(tmp) and not REFUSED and not tz27.REFUSED,
       "the temporary tree removed; no open, listing, request or process refused by either hook")
    out("SELFTEST PASS: %d checks" % n[0])


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except GuardError as exc:
        out("refused: %s" % exc)
        raise
```
