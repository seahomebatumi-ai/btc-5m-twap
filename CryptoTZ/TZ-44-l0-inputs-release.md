# TZ-44 — L0's inputs off the host: one Release of the reward book's days to 2026-11-08 — their selections, slot records and reward polls — and of TZ-43's work files; and the venue's own reading of the host's address

**Canonical filename:** `TZ-44-l0-inputs-release.md`. The committed file takes this name and no other.

**Executor model: Claude Opus 5.5.** A store under a reserve read for publication, the reserve enforced at every open, a credential's block, and its proof by anonymous download.

**Required System Map revision:** `2026-11-12-a`. The Boss's request named `2026-11-11-a` and its §7 item 154; `main` has carried `2026-11-12-a` since `53771a4`, 2026-11-12 06:35:21 UTC, under PR #41's merge, `7f7d7b1`, item 154 unchanged in it, and this TZ is written against it. **No map revision ships with this TZ.**

**Map sections this TZ rests on**, copied from §10's C8 (map §7 item 141): §0, the fingerprint gate and its table; §1, the refs; §2.5, the pair book's idle stretch and its archive's calendar run; §2.6, the reward book — its store, its archive, the reserve and L0; §3, the forensic store, the worktrees, the directories TZ-43's session left and the code trees; §6, its rows host, host identity, language, git remote, disk, process supervision, memory, sandbox limit — network, GitHub Releases, sandbox limit — destructive actions, and harness; §7 items 115, 118, 119, 120, 124, 129, 131, 132, 137, 138, 140, 141, 143, 144, 149, 150 to 157 and 159.

**Required anchors**, from map §0. A mismatch on any one is BLOCKED before any work:

| anchor | required |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `0f6c90451cbd` |
| `A6` — pricer | `729f0bcdbee3` |

**Host gate:** §0.3. This TZ runs on the capture host for the reward book's store, the forensic store and the repository's credential; it opens no stream and nothing of a reserved day.

**Before `EXECUTE TZ-44`:** the Boss uploads this file into `CryptoTZ/`, and nothing else. No step of his is a precondition of the run (map §7 item 132). **The Boss is needed at the VPS while it runs: B-UPLOAD, §3.6, is his block by its own text** — one line, pasted into a root shell, at the point that needs it.

**When: on any day, begun at 07:30:00 to 21:00:00 UTC.** §0.0 reads the clock before anything else and, outside that band, begins nothing. 07:30 is clear of the package manager's morning run, from 06:00 UTC with up to an hour's delay, which restarts capture units (map §7 items 120 and 143); a run begun by 21:00 ends before the next unless B-UPLOAD's wait for the Boss or an incident at GitHub holds it, and G-STILL then reads what that morning restarted (§4). Both archives' calendar runs, 01:30:20 and 03:00:20 UTC, and their runs off the calendar are held by the instrument itself (§5). About 1 h of the session's wall clock, and the time the Boss takes to run B-UPLOAD (§6).

**What this TZ is.** L0 read UNDECIDABLE (TZ-43; map §2.6, §7 item 153), and the Architect could not re-derive its money: every day's selections, slot records and reward polls sit in `/var/lib/btc-rewardbook/` and nowhere else, and TZ-43's own work files in the forensic store (map §7 item 154). CANON hard rule 16 asks that a reading's inputs leave the host with it. This TZ moves them: **one Release, on the tag `tz-44-l0-inputs`, holding one archive a day of every file of the store's day directory but its streams — and but any file of stored replies in which the venue answered with something other than a JSON document under status 200, an error page among them, which can carry the host's address (§1) — for the twelve days before the reserve, 2026-10-28 to 2026-11-08; the 34 files of TZ-43's `fetch/` and `days/`, its `set.json` and its `reading.json`, by the bytes and SHA-256 its report names; and a manifest of every asset and every member.** From those public bytes the Architect re-derives L0's money, measures the parameters that moved under its replay (map §7 item 155) and explores the eight days for a second rule (map §7 item 153). **It scores nothing and decides no track.** And it reads the venue's geoblock once from the host, because L1 would place orders and the venue's documentation lists the host's country among those from which orders may only close (§1).

---

## 0. Gates

### 0.0 The instant, then the work tree

After contract §1 steps 1 and 2, and before anything else, in the session:

```
t=$(date -u +%s); s=$(( t % 86400 )); echo "now $t $(date -u -d @$t +%FT%TZ), second of the day $s"; [ "$s" -ge 27000 ] && [ "$s" -le 75600 ]; echo "inside=$?"
```

**`inside=0` begins the run. Anything else begins nothing:** no directory is made, nothing is written, committed or pushed and no report is written — this TZ has not executed (CANON hard rule 5) — and the Executor tells the Boss in one line, in Russian, the next 07:30 UTC, and stops. This is not BLOCKED and owes no report (contract §5); a later `EXECUTE TZ-44` inside the band starts the TZ afresh. Then:

```
mkdir /root/tz44-work /root/tz44-work/logs; echo "exit=$?"
```

`exit=0` proves neither existed; anything else is BLOCKED. The clock line is run again into `logs/00-instant.log`. **From here every command's output goes to `/root/tz44-work/logs/`, one file per step, under the names §3's table fixes**, and nothing to the session's scratchpad; B-RECLAIM-OWN, §9, is the one exception.

Three abbreviations: **`P`** is `nice -n 19 /root/tz04a-env/venv/bin/python -B`; **`I0`** is `P /root/tz44-work/stage/research/tz44-l0-inputs-release.py`, the staged copy, for §0 alone; and **`I`**, from §3.1 on, is `P /root/tz44-work/wt/research/tz44-l0-inputs-release.py`, the committed copy. Every mode runs from `/root/tz44-work` — `main` asserts it (line 1228). **In every block handed to the Boss, both are written out in full.**

### 0.1 The instrument, staged

Extract Appendix A from this TZ as the primary checkout carries it after contract §1's pull, and place TZ-27's instrument beside it — the instrument loads `research/tz27-pairbook-archive.py` from its own directory by its SHA-256 (lines 316 to 327 and line 330) — with this script, verbatim, its one argument the destination, its output into `logs/01-stage.log`:

```
/root/tz04a-env/venv/bin/python -B - /root/tz44-work/stage <<'EOF2'
import hashlib, os, sys
SRC = "/root/btc-5m-twap/CryptoTZ/TZ-44-l0-inputs-release.md"
TZ27 = "/root/btc-5m-twap/research/tz27-pairbook-archive.py"
DEST = sys.argv[1]
WANT = {
    "research/tz44-l0-inputs-release.py": "0b78807d9c5dec087138b0c9a329cb8c976157ab5c8a3fd4deee7cb31e89e190",
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
| `research/tz44-l0-inputs-release.py` | 1,616 | 90,703 | `0b78807d9c5dec087138b0c9a329cb8c976157ab5c8a3fd4deee7cb31e89e190` |
| `research/tz27-pairbook-archive.py` | 2,078 | 106,284 | `2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673` — map §0's `frozen` row |

A failed assert or another hash is BLOCKED. The staged copy runs §0.2's `fingerprint` and §0.5's and §3.1's `number`, and nothing else.

### 0.2 Fingerprint

`I0 fingerprint`, into `logs/02-fingerprint.log`, performs contract §1 steps 3 and 4 inside the instrument and asserts them, against `SYSTEM-MAP.md` and the files of its §0 table in the primary checkout `/root/btc-5m-twap`: revision `2026-11-12-a`; the six anchors; `A2`, `A4`, `A5` and `A6` re-derived as the first 12 hex characters of those files' SHA-256; the table's **62** rows, each printed in lines, bytes and SHA-256 — **59** `frozen` rows asserted equal to the map, **2** `tracked` and **1** `reported`; and the map's own lines, bytes and SHA-256 (lines 788 to 815). It prints `FINGERPRINT PASS` or stops at the first mismatch, which is BLOCKED.

### 0.3 Host gate

From `/root/btc-5m-twap`, with `S` first set to the scratchpad directory the session's system prompt names, output verbatim into `logs/03-host-gate.log`:

```
date -u; date -u +%s; uptime -s; journalctl --list-boots --no-pager | tail -n 3
nproc; grep -E '^(MemTotal|MemAvailable|SwapTotal|SwapFree):' /proc/meminfo
df -B1 --output=source,size,avail /var/lib/btc-recorder
find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
grep -c e3975b5da44c5328adf3bf3914634cd878842c73 /var/lib/btc-recorder/runtime.jsonl
/root/tz04a-env/venv/bin/python -c 'import sys; print(sys.version.split()[0])'
stat -c '%F %n' /var/lib/btc-pairbook-archive/ledger.jsonl; for d in $(seq 1793145600 86400 1794096000); do stat -c '%F %n' /var/lib/btc-rewardbook/$d; done
TZ=UTC systemctl show btc-recorder.service btc-pairbook.service btc-rewardbook.service adv3-bot.service btc-pairbook-archive.service btc-pairbook-archive.timer btc-rewardbook-archive.service btc-rewardbook-archive.timer btc-chainbook.service -p Id -p MainPID -p NRestarts -p ActiveState -p SubState -p UnitFileState -p ActiveEnterTimestamp -p Result
TZ=UTC systemctl list-timers btc-pairbook-archive.timer btc-rewardbook-archive.timer apt-daily-upgrade.timer apt-daily.timer --all --no-pager
journalctl _PID=1 -o short-iso --since 2026-11-10 --no-pager | grep -E 'Reload|btc-|adv3' | tail -n 80
grep -E '^(Start-Date|Commandline|Upgrade|End-Date)' /var/log/apt/history.log | tail -n 40
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
systemctl is-active telemetry-watch.service; echo "exit=$?"
cat /root/adv3-bot-svc/commit.txt
test -e /root/tz43-work; echo "/root/tz43-work exit=$?"
for t in /root/btc-recorder-svc /root/btc-pairbook-svc /root/btc-pairbook-archive-svc /root/btc-rewardbook-svc /root/btc-rewardbook-archive-svc /root/adv3-bot-svc; do test -e $t; echo "$t exit=$?"; done
find /root/btc-forensics -type f | wc -l; ls -1 /root/btc-forensics | grep -cE '^tz43-work--(fetch|days)--[0-9]{10}\.'
git -C /root/btc-5m-twap worktree list
du -sb /var/lib/btc-rewardbook /var/lib/btc-pairbook /root/btc-forensics /root/.claude-8j 2>&1; journalctl --disk-usage
echo "$S"; ls -la "$(dirname "$(dirname "$S")")"
```

then the memory gate's own reads, appended to the same log:

```
for k in 1 2 3 4 5; do m=$(( $(awk '/^MemAvailable:/ {print $2}' /proc/meminfo) * 1024 )); echo "MemAvailable read $k $(date -u +%T): $m"; [ "$m" -ge 98319394 ] && break; [ "$k" -lt 5 ] && sleep 60; done
```

- **H1** — `find` prints exactly one path.
- **H2** — `df` names source `/dev/vda2` and size `31612203008`; `grep -c` prints at least `1`. With H1 this is map §6's host identity.
- **H3** — the interpreter prints `3.12.`.
- **H4** — `stat` prints 13 lines: `regular file /var/lib/btc-pairbook-archive/ledger.jsonl`, which G-STILL reads, and `directory /var/lib/btc-rewardbook/<D0>` for each of the twelve `D0` from `1793145600` to `1794096000`, which `I pack` reads.
- **Memory gate** — the last `MemAvailable read` at least `98,319,394` bytes: a read below it is read again 60 s later, five reads at most, the first at or above it passing (§0.4; map §7 item 137).
- **Disk gate** — `avail` at least `8,200,000,000` bytes (§0.4).

These are seven checks — H2 two — and any one failing is BLOCKED. **The rest is printed and carries no threshold:** the boots; the units and the timers, both archives' and the package manager's among them; systemd's reload records since 2026-11-10 and the package history, beside which the instrument's holds read either archive's runs off its calendar (map §7 items 115 and 129); the consumer's two states, on which map §6's headroom is conditional; **the advisor's `commit.txt`, against `4e6db2d16dda3da14957120d636f537dfc0bcc87`, the head of `tz-42-advisor-registry`, which map §3 names for the service copy** (map §7 item 159) — a difference is reported first and BLOCKS nothing, because this TZ's work needs no advisor; `/root/tz43-work` gone, by map §3, and the code trees present; the forensic store's count, map §3's `2,487`, and its 32 `tz43-work--fetch--` and `tz43-work--days--` files; the worktrees, map §3's two; `du` of both stores, as map §2.5 and §2.6 ask, of the forensic store and of the sessions' configuration directory, and the journal's size, beside `df`; and the listing of the directory that holds the session's own, whose UUID directories `I scratch` names live or earlier (§3.3). **The units' states are printed and BLOCK nothing:** whether a capture process runs is a state (CANON, fingerprint gates), this TZ's work needs none running, and G-STILL compares them (§4).

### 0.4 Resource floors, in exact bytes

**Disk — three bounds on the free bytes of `/dev/vda2`, each derived from map §6's disk row and map §2.6.** **`7,400,000,000` after any write of this TZ's** (`DISK_FLOOR`, line 118): the reward book's `STREAM_FLOOR`, `7,300,000,000`, below which no stream of it opens for a slot, plus `100,000,000`, one slot of its streams at the cut (`research/tz33-reward-book-capture.py` lines 190 and 192). `pack` reads free space before each day's archive and BLOCKS where the archive would leave less (lines 704 to 706), and `reclaim` before each copy (lines 1210 to 1212), so nothing this TZ writes can pause the reward book. **`7,800,000,000` at the start of `pack`, `upload` and `verify`** (`DISK_GATE`, line 120; `floor_check`, lines 421 to 435): that floor and `400,000,000` for what the session may still write then — its archives and, in §9, their copies. **`8,200,000,000` at the host gate:** that gate, which `upload` and `verify` read once the archives are written, and `400,000,000`, twice the archives' expected bytes, so that a host on which the run could not reach its upload stops it before anything is written. **What the session writes:** the day archives, about `16,300,000` bytes a day — what TZ-33's day writes outside its streams (map §2.6) — for twelve days, `195,600,000`; the manifest and the set, under `1,000,000`; the worktree's checkout, `7f7d7b1`'s tracked files, `14,281,610` bytes, with this file and the instrument; the logs; and in §9 the copies of what the report names by hash, the archives among them — **about `196,000,000` bytes the forensic store keeps** (CANON hard rule 15). Every free-space read from TZ-36's to TZ-43's found `9,459,564,544` bytes or more; TZ-43 read `10,555,289,600` at its host gate, `10,328,178,688` at its closing read and `10,327,752,704` after its §9 (map §6, disk).

**Memory.** `MemAvailable` at least **`98,319,394`** bytes (`MEM_FLOOR`, line 114) — twice `49,159,697`, the host peak modelled from `41,000,000` at the ratio TZ-37 measured between the host's peak and the Architect's for one code, `58,953,728 / 49,168,384` (map §6, memory; §7 items 131 and 156). **`41,000,000` is the Architect's bound on any mode's peak under Python 3.12.3, set above the largest sum his runs gave, `40,456,192`:** the largest peak of a mode run as the host runs it, `geoblock`'s `38,465,536`, and `1,990,656`, by which the largest of `pack`, `upload` and `verify` — `verify`'s `34,037,760` — exceeded `number`'s `32,047,104` under the harness. Those three ran under a harness alone, which stands in for the host's `hold`, for TZ-43's literals, for the credential and for GitHub, and reads about `5,000,000` bytes below a direct run. That sum was read on these bytes less the floor's own literal — the constant, its comment and the self-test's check of it; **the bytes sent read under the bound at every mode:** run directly, `geoblock` `38,051,840` to `38,219,776`, three runs; `selftest` `37,859,328` to `37,953,536`, three; `fingerprint` `37,167,104`; `number` `37,171,200`; `still` `36,925,440`, twice; `scratch` `37,167,104`; `reclaim` `37,068,800`; and under the harness `pack` `33,476,608` and `33,886,208`, `upload` `32,731,136` and `verify` `33,902,592`, beside `number`'s `31,952,896` to `31,961,088` there — `38,219,776` and `1,949,696`, `40,169,472` (§6). No mode holds more than one block of a file, or one line of a file of replies, at a time: `pack` reads a file of replies a line at a time — the longest in the Architect's store a listing page of `459,743` bytes — and streams each member into its archive, `upload` streams each asset from its file and `verify` hashes each download as it arrives. The host's `MemAvailable` ran from `180,871,168` to `353,366,016` bytes at TZ-43's seven floor reads (map §6, memory). **`pack`, `upload` and `verify` read `MemAvailable` and free space at their start** (`floor_check`, lines 421 to 435; `memory_gate`, lines 414 to 418): a memory read below the floor is read again every 60 s, five reads at most, the first at or above it passing and five below it BLOCKING; free space below `7,800,000,000` BLOCKS; and glibc's mmap threshold and arena count are asserted taken (lines 66 to 72 and line 75). The other modes read no floor of their own; the host gate's reads stand before them, and every mode prints its peak on every exit (§5).

### 0.5 Refs and the number

`I0 number`, into `logs/05-number.log`, and `git -C /root/btc-5m-twap ls-remote origin`, into `logs/05-refs.log`, after §0.4, every ref reported; both again in §3.1 — `I0 number` after its fetch, `git ls-remote origin` before its push. Map §1's last record is its revision's own, 2026-11-11 22:16 UTC, 138 ref lines. **The Architect read 139 on 2026-11-12 at 15:11 UTC and the same 139 at 20:29 UTC:** `HEAD` and `refs/heads/main` at `7f7d7b1`, PR #41's merge, above `53771a4`, revision `2026-11-12-a`; nineteen `tz-*` branches; forty-two pull heads and no merge ref — no pull request open; fifty `pairbook-streams-*` and twenty-two `rewardbook-streams-*` tags, the last of each that day's; and the two annotated tags with their peeled lines. Every run of either archive that takes a new set adds one tag, at 01:30:20 and 03:00:20 UTC, and each possibly 1,800 s and 600 s after a start of its timer (map §2.5, §2.6; §7 items 115 and 129). Every commit on `main`'s first-parent line above `7f7d7b1` is reported with the paths it changed, the upload that carries this TZ among them. A difference is recorded, not BLOCKING, unless `refs/heads/tz-44-l0-inputs-release` or `refs/tags/tz-44-l0-inputs` already exists — either is BLOCKED; a `main` that does not carry revision `2026-11-12-a` is §0.2's BLOCK.

**NUMBER — CANON hard rule 2.** `I0 number` reads, in the primary checkout, `git ls-tree --name-only origin/main -- CryptoTZ/ CryptoReports/` and must print `NUMBER PASS - 2 of 2`: `CryptoTZ/` holds `TZ-44-l0-inputs-release.md` and no other file whose name begins with `TZ-44-`, and `CryptoReports/` no report whose name does (lines 818 to 823 and 826 to 833). Anything else is BLOCKED, here and in §3.1 alike. Map §7 item 154 gave this work the number 44, the next free: `CryptoTZ/` and `CryptoReports/` end at TZ-43's files.

---

## 1. Why this TZ exists

**L0's money rests on inputs the host alone holds** (map §7 item 154). Its replay took each member's minimum size and maximum spread from the day's selection and its rate from each poll, and both are in the store's `select.<a>.json` and `<S>.<k>.rewards.jsonl.gz`, never in a Release: the reward book's archive moves streams only (map §2.6). TZ-43 printed no member's figure, as the reserve then asked, and published no input; so the Architect re-derived its stream-level counts from the archive's Releases and not its money (CANON §1.5). Hard rule 16 now asks every reading's inputs to leave the host with it. **Three questions wait on these bytes** (map §7 items 153 to 155): L0's money re-derived, a difference reported before anything else; the member-days a minimum size or a maximum spread moved under a replay that held the evening's selection all day; and where the rule is paid and where it only takes fills, by market and by its place behind the touch — the exploration a second rule comes from, fixed in a TZ before any day from 2026-11-09 is read.

**What the Release holds** (§4, G-PACK and G-SOURCE):

- **One archive a day, `rewardbook-inputs-<D0>.tar`, for the twelve UTC days `1793145600` to `1794096000`, 2026-10-28 to 2026-11-08:** every file of the day's directory `/var/lib/btc-rewardbook/<D0>/` but its streams — each selection, `select.<a>.json`, with its stored replies, `select.<a>.replies.jsonl.gz`, each slot's record, `<S>.<k>.slot.json`, and each slot's reward polls, `<S>.<k>.rewards.jsonl.gz`, one line a poll with the venue's reply verbatim (map §2.6; the names `research/tz33-reward-book-capture.py` lines 228, 229, 984 and 1096 to 1098 fix) — stored verbatim in name order as `<D0>/<file>`, a plain POSIX tar, so the archives unpack into the store's own layout. **A file of stored replies is left out where a line of it carries a body the venue did not serve as a JSON document under status 200:** the store keeps the body of every try, an error's among them (`research/tz33-reward-book-capture.py` lines 590 to 617), and an error page of the venue's edge can carry the address it was served to — the host's. `pack` reads each file of replies once, a line at a time, before it archives it, and the manifest names a file withheld by its bytes and by that line's number, never its content (lines 634 to 651 and 654 to 672). On TZ-43's eight days 5 polls of 345,600 were not served (its report, its `fetch` lines), so the files withheld should be few; a selection's own document and a slot's record hold no body and are never withheld. **The streams are not in it:** the `rewardbook-streams-*` Releases hold them, and a stream file still on the host is listed by its bytes and never opened. **Never a log:** the store's root — `runtime.jsonl`, `service.pid` and `service.log` — is neither opened nor listed by the instrument. **Twelve days, where item 154 named nine:** 2026-10-28 to 2026-10-30, the Architect's exploration, are read already (CANON PART II, the L track), and the second rule's exploration gains three days at no cost to any reserve. 2026-10-28 is the store's first day, captured from 11:30:16 UTC.
- **The 34 files of TZ-43's tree that its reading rests on** — `fetch/<D0>.json`, `fetch/<D0>.polls.jsonl`, `days/<D0>.json` and `days/<D0>.slots.txt` for its eight member days, its `set.json` and its `reading.json` — **each the bytes and SHA-256 TZ-43's report names** in its §2.6, copied by TZ-43's §9 into the forensic store as `tz43-work--<path, / as -->` (map §3), and published as `tz43-<path, / as ->`.
- **The manifest, `tz44-manifest.json`:** every day's archive with its bytes and SHA-256, each member's name, bytes and SHA-256, the day's names counted by kind, every file of replies withheld with its bytes and its reason, and every other name left out with its bytes; every TZ-43 file with its path, its forensic name, its bytes and SHA-256; TZ-43's report's SHA-256; and the instrument's commit and SHA-256 — so any single member is traced to its source without a run of anything (lines 745 to 748).

**The reserve stands** (map §2.6; CANON PART II): every day from 2026-11-09, `D0` at or above `1794182400`, is reserved for L0's next gate, and nothing of such a day is opened, listed or published. The twelve days are read already, by TZ-43 and by the Architect's exploration: an exploration's from now on, gating nothing (CANON PART VI). **The audit hook enforces it at the open** (lines 257 to 299 and 302 to 310): under `/var/lib/btc-rewardbook/` only `pack` lists, and only the twelve day directories, and only `pack` opens, for reading, and only a selection, a slot record or a poll file of those days — never a stream, never a file of the root — and `pack` asserts the store opened once a member and listed once a day (G-RESERVE).

**The geoblock, read once from the host.** The venue's documentation lists Poland among the countries from which orders may only close positions, on its website and through its API alike, and gives an endpoint that returns the venue's own reading of an address — whether it is blocked, and its country and region [read by the Architect on 2026-11-12 at `docs.polymarket.com/api-reference/geoblock`; not measured]. The capture host is a Vultr VPS in Warsaw (map §6, host), and L1, the L track's live step, would place orders (CANON PART II). **`I geoblock` makes one `GET https://polymarket.com/api/geoblock` from the host, gates nothing, and prints `blocked`, `country` and `region` and the reply's key names — never the address the reply carries, which is the host's own** (lines 777 to 783 and 1111 to 1138). It reads no market, places no order and holds no key; a failure is printed by its kind alone. The reading is for the choice of L1's host, and decides nothing here: no order of ours is placed before an L0 gate reads EARN (CANON PART II).

**Why the upload is the Boss's.** A Release is written with the repository's credential, and the session refuses calls that read the git token and send it to `api.github.com` (map §6, sandbox limit — network; contract §5.1). TZ-27's B-UPLOAD was the Boss's block for that reason, under the token the primary checkout's remote URL carries or else the one `gh` holds (map §6, GitHub Releases); this TZ's is the same, through the same function, `credential` (TZ-27 lines 725 to 739), and the same client, TZ-27's `GitHub` and `upload_set` (§5). Its proof needs no credential: every asset's bytes, state and digest from the API's record, and every asset downloaded whole and hashed, anonymously, 120 s or more after the upload completes.

---

## 2. Scope

**Repository paths this TZ may write, and no others:**

1. `research/tz44-l0-inputs-release.py` — new, byte for byte Appendix A's, on the branch `tz-44-l0-inputs-release`, then a pull request. Not merged by the Executor.
2. `CryptoReports/TZ-44-l0-inputs-release-report.md` — straight to `main`, in one commit. **The one path pushed to `main`, and the exemption to item 9 below.**

**Host paths this TZ may write:** `/root/tz44-work/**`; `/root/btc-forensics/`, by exclusive create only (§9); and in the primary checkout `/root/btc-5m-twap`, its `.git` for the branch and the worktree, and its `CryptoReports/` for the report. **Host paths it removes, under §3.3 and §9 and nothing else:** `/root/tz44-work/` with its worktree, and the directories `I scratch` names earlier.

**Remote objects it creates:** the branch `tz-44-l0-inputs-release` and its pull request; **and, by B-UPLOAD alone, the Release on the lightweight tag `tz-44-l0-inputs` at the instrument's commit, published and not the latest, with its 47 assets** (§3.6). **The named exemption to items 3 and 4 below:** the assets carry the twelve days' selections, slot records and polls and TZ-43's work files — prices, sizes, rates, competitiveness and outcomes among them — because publishing them is this TZ's purpose (CANON hard rule 16); the reserve on those days ended with TZ-43's reading (map §2.6).

**Prohibited, each absolutely:**

1. No committed file is modified; every `frozen` row of map §0 is byte-identical at run end.
2. **Nothing under `/var/lib/btc-recorder/`, `/var/lib/btc-chainbook/`, `/var/lib/btc-pairbook/`, `/var/lib/adv3-bot/`, `/etc/adv3-bot/` or `/var/lib/btc-rewardbook-archive/` is opened, listed or written** — the instrument's hook refuses every open and listing there (lines 257 to 299); the Executor's own commands touch the recorder's root with `df`, in §0.3, §3.9 and §9, and with §0.3's `find` and `grep -c`, and the pair book's with §0.3's `du -sb`, and nothing else. **Under `/var/lib/btc-pairbook-archive/` nothing is written or listed, and `ledger.jsonl` is opened by `I still` alone** — the named exemption — beside §0.3's `stat` of it.
3. **Under `/var/lib/btc-rewardbook/` nothing is written, and the instrument opens or lists nothing but in `pack`, for reading, and only a day's directory `<D0>/` for `D0` from `1793145600` to `1794096000`: its listing, its `select.<a>.json` and `select.<a>.replies.jsonl.gz`, and its `<S>.<k>.slot.json` and `<S>.<k>.rewards.jsonl.gz`** — the named exemption. **No stream file there is opened by anything; nothing of a day from `1794182400` is opened or named by anything; no file of the root is opened.** The Executor's own commands touch the store with §0.3's `stat` of the twelve day directories and with `du -sb`, in §0.3 and §3.9, which walks the store and prints one sum, and nothing else.
4. **No content of a store file, an archive, a TZ-43 file or the manifest is printed**, by the instrument or by any command of the Executor's — no `cat`, `head`, `less`, `zcat`, `gzip -d`, `tar -x`, `tar -t`, `jq` or `python -c` on one. The instrument prints names, counts, bytes and hashes alone, and of the geoblock's reply its three fields and its key names (item 6); §3.9's `sha256sum`, `ls -la` and `wc -l` are the Executor's reads of this TZ's files. The Claude Code transcript keeps every command's output (map §7 item 118).
5. **No credential is printed, written or read by the Executor:** never `git remote get-url`, `git config --get-regexp url`, `gh auth token` or `gh auth status --show-token`, and never the advisor's token. B-UPLOAD's instrument reads the repository's credential in the Boss's shell and prints its source alone (TZ-27 lines 725 to 739).
6. **The host's public address is never printed, written or published:** the geoblock reply's `ip` is neither printed nor written (lines 777 to 783), no command asks any service for it, and **no stored reply's body leaves the host but a JSON document the venue served under status 200** — a file of replies holding any other body is in no archive (§1; lines 634 to 651).
7. **No unit is signalled, started, stopped, enabled, disabled, reloaded or changed**, and nothing under `/etc/systemd/` is touched. `systemctl show`, `is-active`, `is-enabled` and `list-timers` and `journalctl` are this TZ's only reads of a unit and of systemd.
8. **Requests.** To GitHub through TZ-27's client alone — in `I upload`, `api.github.com` and `uploads.github.com` with the credential; in `I verify`, `api.github.com`, `github.com` and the hosts a download is redirected to, `release-assets.githubusercontent.com` and `objects.githubusercontent.com`, with no credential — every one under `User-Agent: btc-5m-twap-tz27`, `Accept` and `X-GitHub-Api-Version: 2022-11-28` (TZ-27 lines 509 to 519), and held to the pair book's idle stretch away from both archives' runs (lines 469 to 483 and 502 to 543). **And one `GET https://polymarket.com/api/geoblock`, in `I geoblock` alone, with `User-Agent: btc-5m-twap-tz44` and `Accept: application/json`, no redirect followed, no credential: this TZ authorizes that one request in writing (contract §10).** No other host is reached by the instrument — its hook refuses one (lines 221 to 225 and 259 to 261) — and the Executor's commands reach GitHub by `git` and `gh pr create` alone; GitHub's status page, where §3.7 reads it, is read by the session's own web tool and by no request from the host. **No order is placed, signed or cancelled; no authenticated venue endpoint is called; no key of any venue is held.**
9. **No Release, tag or asset but this TZ's is created, changed or deleted, and this TZ's only by `I upload`.** Nothing is pushed to `main` but the report; nothing is merged.
10. `/root/tz04a-env/`, `/root/tz01-env/` and the code trees `/root/btc-recorder-svc/`, `/root/btc-pairbook-svc/`, `/root/btc-pairbook-archive-svc/`, `/root/btc-rewardbook-svc/`, `/root/btc-rewardbook-archive-svc/` and `/root/adv3-bot-svc/` are not modified — §0.3 reads `commit.txt` of the last and nothing else of them; `/root/btc-forensics/` is written only by §9's exclusive create, its 34 TZ-43 files read by `pack` and `upload`, and nothing in it is removed.
11. **Nothing is removed from the reward book's store or the forensic store, and from a Release nothing but an asset of this TZ's own that `I upload` replaces** (§3.6).

---

## 3. The work, in this order

Every command's output goes to `logs/`, one file per step under the names below, and is quoted in the report; a step run again appends to its own log under a `date -u` line. **B-RECLAIM-SCRATCH runs inside §3.3 and holds back nothing after it — no later step reads what it removes (map §7 item 140); B-RECLAIM-OWN runs last (§9).** On a BLOCK before §3.1, B-RECLAIM-OWN runs with `I0` in place of `I` and without its `git worktree remove` line; on a BLOCK or a FAIL after it, the run goes to §3.9 and §9, skipping every step that needs a PASS it lacks — §3.5 needs none.

| step | logs |
|---|---|
| §0.0 to §0.5 | `00-instant.log`, `01-stage.log`, `02-fingerprint.log`, `03-host-gate.log`, `05-number.log`, `05-refs.log` |
| §3.1 | `10-number.log`, `11-worktree.log`, `12-fingerprint.log`, `13-push.log`, `14-pr.log` |
| §3.2 | `20-selftest.log` |
| §3.3 | `30-still.log`, `31-scratch.log`, `32-reclaim-scratch.log` |
| §3.4 | `40-pack.log`, `41-pack-again.log` |
| §3.5 | `50-geoblock.log` |
| §3.6 | `60-upload.log`, written by the Boss's paste; `61-upload-wait.log`, the Executor's reads of it |
| §3.7 | `70-verify.log` |
| §3.8 | `80-still.log` |
| §3.9 | `90-host-gate-again.log`, `91-closing.log`, `92-selfcheck.log` |

**Where the session's permission classifier refuses a command of a block named B-…**, the Executor tries the block once and hands the Boss its paste, unchanged, once, in plain words (CANON hard rule 14; map §6, sandbox limit — destructive actions; §7 items 124 and 138); the Boss runs it verbatim in a root shell on the VPS, every step chained to the one before it and appended to its log under a `date -u` line, and the Executor verifies it from that log and through the reads this TZ names — never from the Boss's account — and runs no step of the paste again (map §7 item 144). **B-UPLOAD is the Boss's by its own text and is not tried by the Executor** (§3.6).

### 3.1 The branch and its file

```
git -C /root/btc-5m-twap fetch origin
I0 number
git -C /root/btc-5m-twap worktree add -b tz-44-l0-inputs-release /root/tz44-work/wt origin/main
```

Into `10-number.log` the fetch and `I0 number`, which must print `NUMBER PASS - 2 of 2` again (§0.5), or BLOCKED; into `11-worktree.log` the worktree and §0.1's script again, verbatim but for its argument, `/root/tz44-work/wt` — it writes the instrument and finds TZ-27's file there already, from `origin/main`, and must print the same two lines of lines, bytes and SHA-256 as at §0.1; into `12-fingerprint.log` `I fingerprint`, which must print `FINGERPRINT PASS` again, from the worktree's file. Into `13-push.log`: commit the one file alone on the branch, `research/tz44-l0-inputs-release.py`; `git -C /root/btc-5m-twap ls-remote origin` (§0.5); push with `git -C /root/tz44-work/wt push -u origin tz-44-l0-inputs-release` — through `credential.helper=!gh auth git-credential` where the URL's credential is refused (map §6, git remote) — then:

```
date -u +%FT%T.%NZ; git -C /root/tz44-work/wt ls-remote origin refs/heads/tz-44-l0-inputs-release
git -C /root/tz44-work/wt rev-parse HEAD
```

— the instant the commit is on `origin`, and its hash there, which must be the worktree's `HEAD`: **the Release's tag is made at this commit** (§3.6), and `pack` and `upload` assert it (lines 935 to 937 and 1040 to 1041). Into `14-pr.log` the pull request against `main`, opened with `gh pr create`. A failed assert or a non-zero exit here is BLOCKED.

### 3.2 The self-test

`I selftest`, into `20-selftest.log`, must print `SELFTEST PASS: 38 checks`. It reaches no network but a listener of its own on `127.0.0.1` — TZ-27's own stand-in for GitHub, `_FakeGitHub` (TZ-27 lines 1550 to 1656) — and runs on literals, on a synthetic day directory and on temporary trees under `/root/tz44-work/selftest-tmp/`, which it removes (lines 1251 to 1608). It proves the hook's every decision this TZ relies on, the floors, the clock, the readings, a day's archive built from two trees and once again to the same bytes, every member verbatim and every stream and stray name left out, a stored reply's body judged and a file of replies withheld by its line and absent from its archive, and the whole request path — the Release created on the tag at the commit, three assets uploaded, every one proved by the API's record and a full anonymous download, a second upload holding all three, and a changed byte served read as a failed download. A red self-test stops the run here, and it goes to §3.9 and §9.

### 3.3 The units, the directories beside this session, and B-RECLAIM-SCRATCH

`I still`, into `30-still.log`, records the recorder's, the pair book's, the reward book's and the advisor's `MainPID`, `NRestarts` and `ActiveState` in `state.json`, with the instant, and prints their `MemoryCurrent` and `MemoryPeak` and both archives' units' states (lines 865 to 887). Then `I scratch "$(dirname "$S")"`, into `31-scratch.log`, lists every UUID directory beside this session's own and names each **live** — born from 1 s before to 60 s after the start of a running process whose `argv[0]` is `claude` or ends in `/claude.exe` — or **earlier** (lines 890 to 907 and 916 to 928). Map §3 expects TZ-43's session's own, `fd099d3c-2537-55ea-a4a0-314ac50cff1f`, and `8e3e58b1-5f4a-46d7-8814-25078c677104` and `c78295f5-9a1d-4177-ac5a-b93cd56a49da`, live at TZ-43's run, unless a reboot of the host emptied `/tmp`. **The rule alone decides:** every directory `scratch` names earlier is reclaimed, whatever a map or a report said of it before (map §7 item 150).

**B-RECLAIM-SCRATCH**, for every directory `I scratch` names **earlier** — none it named live, and never this session's own — into `32-reclaim-scratch.log`:

```
cd /root/tz44-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz44-work/wt/research/tz44-l0-inputs-release.py reclaim <each earlier directory, by its full path>
rm -rf <one such directory>; echo "exit=$?"
test -e <that directory>; echo "exit=$?"
```

One `reclaim` names every earlier directory and must print `RECLAIM PASS` before any removal; then one `rm -rf` and one `test -e` a directory, the last reading `exit=1`. `reclaim` refuses a directory born from 1 s before to 60 s after a running claude process started, and any path but `/root/tz44-work` that is not a UUID directory under `/tmp/` whose parent's name carries `btc-5m-twap` (lines 1164 to 1169 and 1172 to 1221). If `I scratch` names none earlier, the block is recorded as empty and skipped. **Its paste**, where the classifier refuses it (map §7 item 152) — the Executor writes in every earlier directory's full path, one `rm -rf` and one `test -e` a directory, all chained to the `reclaim`'s `exit=0`, which it reaches only after `RECLAIM PASS`:

```
{ date -u +%FT%T.%NZ; (cd /root/tz44-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz44-work/wt/research/tz44-l0-inputs-release.py reclaim <D1> <D2>); echo "exit=$?"; } >> /root/tz44-work/logs/32-reclaim-scratch.log 2>&1 && tail -n 1 /root/tz44-work/logs/32-reclaim-scratch.log | grep -qx 'exit=0' && { date -u +%FT%T.%NZ; rm -rf <D1>; echo "exit=$?"; test -e <D1>; echo "exit=$?"; rm -rf <D2>; echo "exit=$?"; test -e <D2>; echo "exit=$?"; } >> /root/tz44-work/logs/32-reclaim-scratch.log 2>&1
```

**It holds back nothing of §3.4 to §3.9**, which read none of what it removes: the Executor goes on while the paste waits for the Boss, and hands B-UPLOAD's paste beside it if both wait at once.

### 3.4 The pack — G-SOURCE, G-PACK, G-RESERVE and DETERMINISM

`I pack`, into `40-pack.log`, then `I pack` again, into `41-pack-again.log` (lines 931 to 1001). Each run reads the floors, asserts the worktree's `HEAD` is its upstream's, then **G-SOURCE**: every one of the 34 literal rows of TZ-43's files (lines 138 to 171) is found in TZ-43's committed report as its §2.6 table prints it (lines 595 to 598), and each file in the forensic store is a regular file of those bytes and that SHA-256 — held as one unit to the idle stretch (lines 601 to 618). Then **G-PACK**, one unit a day: the day directory listed once and every name classified (lines 675 to 694 and 582 to 592); the unit held for `30` s and its members' bytes at `500,000` a second (lines 629 to 631); free space read; every file of replies read once, a line at a time, and withheld where a line says so (lines 654 to 672); and the members kept read whole into the day's archive (lines 697 to 742); then the manifest and the set, `set.json`, the Release's 47 assets in upload order — the twelve archives, the 34 files, the manifest (lines 751 to 763) — and `state.json`'s `pack` record: the commit, the instrument's SHA-256, the set's and the manifest's. **G-RESERVE:** the store opened once a member kept and once a file of replies scanned, listed once a day, and nothing else under it (lines 994 to 999). The second run must print every one of its 14 outputs `unchanged` — twelve archives, the manifest and `set.json` — and `DETERMINISM PASS: 14 of 14 outputs unchanged`: each is built again and compared, never written again (lines 366 to 375 and 731 to 738). A failed assert is BLOCKED. **The twelve days are closed:** the last writes of a day's directory are its last slot's, 910 s after that slot's start, and the archive's removals of its streams; a name that changes between the two runs changes the manifest, and DETERMINISM fails on it.

### 3.5 The venue's geoblock

`I geoblock`, into `50-geoblock.log`, once (lines 1111 to 1138): the addresses `polymarket.com` resolves to, then one `GET https://polymarket.com/api/geoblock`, no redirect followed, a reply read to `65,536` bytes at most, `30` s at most; it prints one `GEOBLOCK READ:` line — the status, a redirect's host, the bytes, the seconds, `blocked`, `country`, `region` and the reply's key names — and never the reply's `ip`. **It gates nothing:** any status, a redirect or no reply is printed and the run goes on. It is not run again. Where the classifier refuses it, its paste, once:

```
{ date -u +%FT%T.%NZ; (cd /root/tz44-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz44-work/wt/research/tz44-l0-inputs-release.py geoblock); echo "exit=$?"; } >> /root/tz44-work/logs/50-geoblock.log 2>&1
```

### 3.6 B-UPLOAD — the Boss's block

**After §3.4's two PASSES and §3.5, the Executor hands the Boss this paste, once, and does not run it** (§1, why the upload is the Boss's) — in plain words, in Russian: that it is the upload of the Release, which only his shell may run; that it is one line for a root shell on the VPS; that the terminal shows nothing until the run's last lines and `exit=` appear, some minutes, longer across an archive's run; and that no key is pressed meanwhile:

```
(trap '' HUP; date -u +%FT%T.%NZ; echo "run begun"; (cd /root/tz44-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz44-work/wt/research/tz44-l0-inputs-release.py upload); echo "exit=$?") >> /root/tz44-work/logs/60-upload.log 2>&1; tail -n 5 /root/tz44-work/logs/60-upload.log
```

**The paste ignores the end of its login.** `upload` waits minutes for an idle stretch, where a block handed to the Boss is to wait seconds (map §7 item 124): a connection that drops under it must not end the run, which goes on and writes its `exit=` line all the same.

`I upload` (lines 1034 to 1066) reads the floors; asserts the set `pack` wrote, the worktree's `HEAD` the pack's commit, `origin`'s branch at it and every asset's file its set's bytes; reads the credential through TZ-27's `credential` and prints its source alone; finds the Release on `tz-44-l0-inputs` or creates it — `tag_name` the tag, `target_commitish` the pack's commit, `draft` `false`, `prerelease` `false`, `make_latest` `"false"` (lines 536 to 543) — and sends every asset through TZ-27's `upload_set`, which stops where the Release holds an asset outside the set, keeps an asset already matching, removes and sends again one that does not, sends each file at most four times, hashes every byte as it is sent and asserts the Release's record of each — its name, its size, `state` `uploaded` and its digest where the API gives one (TZ-27 lines 765 to 812); each write follows the last by 1 s or more. **Every request waits for the pair book's idle stretch and for both archives to be idle and away from their calendar runs** (lines 469 to 483, 486 to 497 and 510 to 521), and is recorded in `transfers.jsonl`; every step of the upload is a line of `upload.jsonl`, the last its completion. It prints the transfers' places in their windows on every exit (map §7 item 157), and `UPLOAD COMPLETE`.

**The Executor writes the instant of each hand-over into `61-upload-wait.log`, by `date -u +%FT%TZ`, and waits for that run's `exit=` line** with this block, `K` one more than the `exit=` lines `60-upload.log` held at the hand-over, run again while it prints fewer — reads alone, in the foreground (map §6, harness), into the same log:

```
K=1; for i in 1 2 3 4 5 6 7 8 9; do n=$(grep -c '^exit=' /root/tz44-work/logs/60-upload.log 2>/dev/null); [ "${n:-0}" -ge "$K" ] && break; sleep 60; done; date -u +%FT%TZ; echo "exit lines ${n:-0} of $K; runs begun $(grep -c '^run begun$' /root/tz44-work/logs/60-upload.log 2>/dev/null); upload processes $(pgrep -fxc '/root/tz04a-env/venv/bin/python -B /root/tz44-work/wt/research/tz44-l0-inputs-release.py upload')"; tail -n 6 /root/tz44-work/logs/60-upload.log
```

`exit=0` under an `UPLOAD COMPLETE` line of that run goes to §3.7. **A run whose lines name `UPLOAD REFUSED` or `status 401` is BLOCKED at once** — no token in the remote URL and none held by `gh`, a refusal that is not a rate limit, or a token GitHub does not take, which no further run changes (TZ-27 lines 739, 800 and 586 to 589). Any other exit is read from the log, and the same paste is handed over again, `600` s or more after that run's `exit=` line: `upload` resumes, keeping every asset already matching. **A run that ended without its line** — a key pressed under it, a reboot: the block printing, at two runs of it, more `runs begun` than `exit lines` and `upload processes 0` — **is one of the runs, and the same paste is handed over again at once.** **B-UPLOAD runs at most three times in all, and all within `21,600` s of its first hand-over**; a third run that does not complete, or that time passed without an `UPLOAD COMPLETE`, is BLOCKED. On a BLOCK the Release and its tag stay as they stand, named in the report (§2 item 11).

### 3.7 The proof — G-TAG, G-UPLOAD and G-DOWNLOAD

`I verify`, into `70-verify.log` (lines 1069 to 1108): no credential; it waits until 120 s after `upload.jsonl`'s completion record — an anonymous reply may be cached for 60 s (map §6, GitHub Releases) — then reads the Release on the tag through TZ-27's `verify_release` — the API's record of every asset, and, where every record is the set's, a full download of each, hashed as it arrives (TZ-27 lines 685 to 700, 641 to 653 and 656 to 669) — and TZ-27's `release_reading` (TZ-27 lines 703 to 709), and reads the tag on `origin` with TZ-27's `ls_remote_tag` (TZ-27 lines 1139 to 1146). It must print `G-UPLOAD PASS: 47 of 47 …`, `G-DOWNLOAD PASS: 47 of 47 …` and `G-TAG PASS`, and writes `verify.json`. Each request is held as `upload`'s are. **`I verify` runs at most three times, `600` s or more apart**, and its last run may wait, at most 6 h, until GitHub's status page — read by the session's own web tool, never from the host — shows an incident of unauthenticated traffic resolved (map §7 item 149). Where a run's `VERIFY FAIL` names `no asset missing` or `every asset uploaded, its bytes and digest the set's`, B-UPLOAD's paste is handed over once more, within its three and its `21,600` s, before the next `I verify`: `upload` sends what is missing and replaces what does not match. A third `I verify` that does not pass is BLOCKED, and the Release stands as uploaded, named in the report. Where the classifier refuses `I verify`, its paste, in B-UPLOAD's form — the Executor waits for its `exit=` line with §3.6's block, `70-verify.log` and `verify` in the place of `60-upload.log` and `upload`, and reads the run from that log:

```
(trap '' HUP; date -u +%FT%T.%NZ; echo "run begun"; (cd /root/tz44-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz44-work/wt/research/tz44-l0-inputs-release.py verify); echo "exit=$?") >> /root/tz44-work/logs/70-verify.log 2>&1; tail -n 5 /root/tz44-work/logs/70-verify.log
```

### 3.8 The units again — G-STILL

`I still`, into `80-still.log`, reads the four units again against `state.json`'s record and prints `G-STILL PASS` or `G-STILL FAIL` with the reason (lines 844 to 862 and 865 to 887; §4). This TZ signals nothing, so a FAIL runs no block, and the report names what changed beside the reload records and the package history of §3.9 (map §7 item 120).

### 3.9 The closing reads

§0.3's block again, verbatim, the memory gate's reads among it, into `90-host-gate-again.log`: H1 to H4 are checked again, and its memory and disk reads are recorded with their instants and carry no threshold there — the modes' own floor reads were the gates. Then, into `91-closing.log`:

```
cd /root/tz44-work && ls -la out/ && sha256sum out/* set.json state.json upload.jsonl transfers.jsonl verify.json; wc -l upload.jsonl transfers.jsonl
du -sb /root/tz44-work /var/lib/btc-rewardbook /root/btc-forensics; df -B1 --output=source,size,avail /var/lib/btc-recorder; grep -E '^(MemAvailable|SwapFree):' /proc/meminfo
git -C /root/btc-5m-twap ls-remote origin refs/tags/tz-44-l0-inputs 'refs/tags/tz-44-l0-inputs^{}' refs/heads/tz-44-l0-inputs-release
```

A file a BLOCK left unwritten is named as absent. Then contract §4.2's self-check, `C` the instrument's commit, into `92-selfcheck.log`, with two lines more — the diff's counts, and no archive in git history:

```
git -C /root/btc-5m-twap fetch origin
git -C /root/btc-5m-twap rev-list origin/main | grep -c "$C"
git -C /root/btc-5m-twap diff --name-only origin/main origin/tz-44-l0-inputs-release
git -C /root/btc-5m-twap diff --numstat origin/main origin/tz-44-l0-inputs-release
git -C /root/btc-5m-twap ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
for r in origin/main origin/tz-44-l0-inputs-release; do git -C /root/btc-5m-twap ls-tree -r --name-only $r; done | grep -cE '\.tar$|tz44-manifest'
```

Then the report is drafted (§8), and §9 runs.

---

## 4. The gates — fixed here, before any of their data exists

| gate | population | PASS | false failure | power |
|---|---|---|---|---|
| **G-SOURCE** | the 34 files of TZ-43's tree its report's §2.6 names — `fetch/`, `days/`, `set.json` and `reading.json` — in the forensic store | each literal row found in the committed report, and each file a regular file of that row's bytes and SHA-256: 34 of 34 | 0 — a hash of bytes | 1 against any changed byte |
| **G-PACK** | the twelve day directories `1793145600` to `1794096000` of the reward book's store | every name classified; every selection, slot record and poll file read whole and stored verbatim, but a file of replies a line of which withholds it, named and left out; every stream and other name left out and never opened; 12 archives, the manifest and the set written | 0 | 1 |
| **G-RESERVE** | every open and listing under `/var/lib/btc-rewardbook/` in `pack` | opens equal to the members kept and the files of replies scanned, listings to the days, and the hook refusing nothing | 0 — the hook counts every one | 1 |
| **DETERMINISM** | `pack`'s 14 outputs | the second run's bytes equal to the first's, 14 of 14 | 0 on a closed day (§3.4) | 1 |
| **G-UPLOAD** | the 47 assets of the set, on `tz-44-l0-inputs` | each in the API's record by name, its size the set's, `state` `uploaded`, its digest `sha256:` the set's, its download URL the tag's; none missing, none beyond the set; the Release published on the tag | 0 — the host of the bytes records it | 1 |
| **G-DOWNLOAD** | the same 47 | each downloaded anonymously, whole, its bytes and SHA-256 the set's | 0 | 1 |
| **G-TAG** | the tag `tz-44-l0-inputs` on `origin` | lightweight, at the pack's commit | 0 | 1 |
| **G-STILL** | the recorder, the pair book, the reward book and the advisor | every unit's `MainPID`, `NRestarts` and `ActiveState` unchanged — or every unit but the pair book unchanged and its change its archive's own restarts alone, from its ledger | not 0: a restart by the package manager or by another project's reload reads FAIL with no fault of this TZ (map §6, process supervision; §7 item 120) | 1 against a restart of ours |
| **GEO** | the host's address, as the venue reads it | printed — `blocked`, `country`, `region` — and no threshold | — | — |

Each gate but G-STILL and GEO is an identity of bytes or counts: it cannot read PASS where its condition fails, and it fails at every change of what it names. **None of them judges a market:** this TZ reads no price, scores nothing and decides no track. A FAIL of G-SOURCE, G-PACK, G-RESERVE or DETERMINISM is BLOCKED before any upload; of G-UPLOAD, G-DOWNLOAD or G-TAG after §3.7's runs, BLOCKED with the Release as it stands, named. A G-STILL FAIL blocks nothing: the report names its cause.

---

## 5. The instrument

`research/tz44-l0-inputs-release.py`, Appendix A, standard library only, run under `/root/tz04a-env` (map §6, language). **It loads TZ-27's instrument from beside itself, executed from the bytes whose SHA-256 it asserts** (lines 316 to 327), as TZ-28's and TZ-34's do; TZ-27's audit hook is installed then (TZ-27 lines 214 to 259 and 262 to 272), its work tree set to `/root/tz44-work` and its mode to this run's (lines 331 and 1230), and TZ-27's `CONTENT_TYPE` set to `application/octet-stream`, which its `upload` reads at each call (line 332; TZ-27 line 625), so that no asset is labelled gzip. **Its own audit hook** (lines 257 to 299 and 302 to 310) refuses every open, listing, request and process §2 does not give the running mode — processes are `git`, `systemctl` and `stat`, and `gh` in `upload` alone, for TZ-27's `credential` (lines 226 to 227) — and counts every open and listing under the reward book's store. Its closing lines — glibc's settings, the peak memory, the refusals by either hook, the store's opens and listings — are printed on every exit (lines 1242 to 1246; map §7 item 151).

| mode | what it does | lines |
|---|---|---|
| `fingerprint` | contract §1 steps 3 and 4, asserted | 788 to 815 |
| `number` | CANON hard rule 2 | 818 to 823, 826 to 833 |
| `selftest` | 38 checks | 1251 to 1608 |
| `still` | the four units, recorded, then compared; G-STILL | 836 to 841, 844 to 862, 865 to 887 |
| `scratch OWN` | the UUID directories beside OWN, live or earlier | 890 to 907, 910 to 913, 916 to 928 |
| `pack` | G-SOURCE, G-PACK, G-RESERVE; a second run DETERMINISM | 572 to 772, 931 to 1001 |
| `upload` | B-UPLOAD: the Release and its 47 assets, through TZ-27's `credential`, `GitHub` and `upload_set` | 502 to 543, 546 to 562, 1004 to 1031, 1034 to 1066 |
| `verify` | G-TAG, G-UPLOAD, G-DOWNLOAD, through TZ-27's `verify_release`, `release_reading` and `ls_remote_tag` | 565 to 567, 1069 to 1108 |
| `geoblock` | the venue's reading of the host's address, printed | 777 to 783, 1111 to 1138 |
| `reclaim TREE...` | §9 | 1141 to 1221 |

**The clock** (lines 464 to 466, 469 to 483 and 486 to 497): a unit of `budget` seconds — a request at TZ-28's budget, `5 + ⌈bytes / 2,000,000⌉` s (`research/tz28-pairbook-archive-timer.py` lines 135 to 137), the 34 sources of `pack` `60` s, a day of it `30 + ⌈bytes / 500,000⌉` s for its members' bytes (lines 629 to 631) — starts at second 15 of a 900-s window or later and by its second `590 − budget`, inside the pair book's idle stretch (map §2.5); never from `budget + 60` s before either archive's calendar run to 60 s after it; and never while either archive's service is running — the runs off their calendar included (map §7 items 115 and 129). It waits a second at a time — `324 + budget` s at most between two stretches — and BLOCKS after `7,200` s.

**A day's archive** (lines 675 to 694, 621 to 626 and 697 to 742): the day directory is listed once; each file of replies, a name ending `.jsonl.gz`, is read once as gzip, a line at a time, and withheld at its first line that is no JSON record or whose body is anything but a JSON object or array under status `200` — or where it is no whole gzip file (lines 634 to 651 and 654 to 672); the members kept go, in name order, into a POSIX `ustar` tar, each `<D0>/<name>`, its `mtime` `D0`, mode `0644`, owner and group `0` and no owner names — so the same files give the same bytes — each member's size taken before its read, read once through TZ-27's `HashingReader` (TZ-27 lines 546 to 556), and the file asserted not to have grown. It is written as `<name>.part` and renamed, or, where the archive exists, built again, compared and its part removed. A day whose members exceed `200,000,000` bytes, twelve times TZ-33's `16.3` MB, BLOCKS (line 101), and so does a day with every member withheld.

---

## 6. Cost

**Measured on the Architect's stand-in host under Python 3.12.3, on the bytes sent** — the primary checkout at `7f7d7b1`, a synthetic store of twelve days of the store's own shapes, `2,238` members of `258,860,337` bytes — every file of replies gzip lines of records with their bodies, four of them carrying a body that withholds them, `5,133,030` bytes — with two stream files and the root's three, the 34 sources at TZ-43's sizes, and TZ-27's `_FakeGitHub` in another process: `selftest` `0.71` to `0.78` s; `fingerprint` `0.19` s; `number`, `still` and `scratch` under `0.2` s each; `pack` `13.77` s with the cache dropped and `11.90` s again, a day `0.67` to `1.34` s against its budget of `58` to `75` s, its archives `255,375,360` bytes, and `29.30` s the slowest of seven runs of this code; `upload` `47.2` s for 47 assets and `297,939,439` bytes, of it `47` s TZ-27's one-second gap between writes; `verify` `2.93` s; `geoblock` `0.34` to `0.57` s; `reclaim` `0.79` s for the work tree, 37 files copied. **On the host**, at map §6's rates — uploads about `9,300,000` bytes a second, downloads about `13,000,000` — about `238,000,000` bytes of assets are about `26` s of upload with `47` s of gaps and about `18` s of download, and `pack` some tens of seconds of the processor; **the holds add the wait for an idle stretch**, `387` s at most before a day of `16,300,000` bytes, budgeted `63` s, and `338` s before its archive is sent, budgeted `14` s, against the stretch's `575`; `pack` prints how many days ran past their budget, expected `0`. About 1 h of the session's wall clock, and B-UPLOAD's wait for the Boss.

**At the population's upper bound (CANON PART VI, C4):** a day of members at its BLOCK, `200,000,000` bytes, twelve days — `2,400,000,000` bytes scanned, read, written and hashed by each run of `pack`, `278` s at `8,659,635` bytes a second, the slowest run above, `556` s for the two, a day `24` s against its budget of `430`; G-SOURCE's constant `42,169,992` bytes, `5` s; the archives and the 34 sources, `2,442,169,992` bytes, uploaded in `263` s at `9,297,801` bytes a second, with `47` s of gaps, and downloaded in `188` s at `13,000,000`; the archives copied by `reclaim`, each file hashed, copied and hashed again, in `832` s; its largest transfer, a day's archive, budgeted `105` s for its members' bytes and a second more with its headers, inside one stretch — `1,891` s in all, under `3,600`, and nothing is sampled. The disk stops such a store before the processor does: `pack` BLOCKS before the archive that would leave less than `7,400,000,000` bytes free. **The fail-fast bounds, each a constant:** a hold `7,200` s (line 113); the memory floor's reads `240` s at each of `pack`, `upload` and `verify` (lines 116 to 117); the geoblock read `30` s (line 130); TZ-27's `60` s an API request, `300` s an upload and `120` s a download, four attempts a file with waits of `900` s at most and three a download (TZ-27 lines 118 to 124); the Executor's wait for B-UPLOAD `21,600` s from its first hand-over; and a last `I verify` 6 h for GitHub's status page.

---

## 7. Validation

| # | check | expected |
|---|---|---|
| **V1** | `I0 fingerprint` and `I fingerprint`, §0.2 and §3.1 | `FINGERPRINT PASS: revision 2026-11-12-a; anchors 6 of 6, 4 re-derived; rows 62: frozen 59 of 59 equal, tracked 2, reported 1`, twice |
| **V2** | §0.3's host gate, at §0.3 and §3.9 | at §0.3 H1 to H4, the memory and the disk gate — 7 checks; at §3.9 H1 to H4 — 5 checks — and the two reads recorded; every memory read with its instant; the rest printed |
| **V3** | `I0 number`, §0.5 and §3.1 | `NUMBER PASS - 2 of 2`, twice |
| **V4** | §0.1's script, at §0.1 and §3.1 | two lines a run: 1,616 lines, 90,703 bytes, `0b78807d…`; 2,078 lines, 106,284 bytes, `2cba96bc…` |
| **V5** | `I selftest` | `SELFTEST PASS: 38 checks` |
| **V6** | G-SOURCE, both `pack` runs | TZ-43's report's rows found `34 of 34`; `G-SOURCE PASS: 34 of 34 equal to TZ-43's report, 42169992 bytes` |
| **V7** | G-PACK, both runs | `12 days of 12`; for each day its names by kind, its members and bytes, the files of replies scanned, each file withheld with its bytes and its reason, its archive's bytes and SHA-256 and every excluded name with its bytes; `days over their budget 0`; `47 assets`; the outputs `wrote` 14, then `unchanged` 14 |
| **V8** | G-RESERVE, both runs | `G-RESERVE PASS`: opens equal to the members kept and the files of replies scanned, `listed 12 times` |
| **V9** | DETERMINISM | `DETERMINISM PASS: 14 of 14 outputs unchanged` |
| **V10** | `I geoblock` | one `GEOBLOCK READ:` line — the status, `blocked`, `country`, `region` and the reply's key names — and nothing else of the reply |
| **V11** | B-UPLOAD | each run's `exit=` and its last lines; `credential:` its source; `UPLOAD COMPLETE: Release <id> on tz-44-l0-inputs, 47 assets`; `upload.jsonl`'s last line `complete`, `assets` 47; the transfers' line |
| **V12** | `I verify` | `G-UPLOAD PASS: 47 of 47 …; G-DOWNLOAD PASS: 47 of 47 downloads, <bytes>; G-TAG PASS: tz-44-l0-inputs at <the pack's commit>`, the bytes equal to `set.json`'s `bytes_total`; the transfers' line |
| **V13** | `I still`, §3.8 | `G-STILL PASS`, or FAIL with what changed, named beside §3.9's reads of systemd and the package history |
| **V14** | contract §4.2's self-check, and its two lines more | its first count `0`; the diff naming `research/tz44-l0-inputs-release.py` alone, `1616` lines added and `0` removed; nothing `.parquet` or `.zip`; the last count `0` |
| **V15** | the hook | `opens refused: 0, by TZ-27's hook: 0` at every mode, its closing lines printed on every exit; `reward book opens` above `0` at `pack` alone |
| **V16** | memory and disk | every mode's printed peak, against §0.4's `49,159,697`; every `MemAvailable` and free-space read `pack`, `upload` and `verify` printed, none passing below `98,319,394` or `7,800,000,000`; `malloc tuned: True` at every mode |
| **V17** | §9's `reclaim` runs, B-RECLAIM-SCRATCH's and B-RECLAIM-OWN's | files considered, named by a report, kept by name, copied and already held; the store's count after equal to before plus the copies; every line of each `reclaim`'s output quoted unfiltered (map §7 item 119) |
| **V18** | the removals | `git worktree remove` without `--force` exit `0`; `test -e` exit `1` for `/root/tz44-work` and each directory removed; `git worktree list` naming `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else |
| **V19** | the classifier | every block it refused, with the paste handed over, the instant the Boss ran it and the log lines that verify it |

**Barred from every gate:** the members' and bytes' counts — they are the store's, printed and not expected — and the geoblock's reading.

---

## 8. The report

`CryptoReports/TZ-44-l0-inputs-release-report.md`, in contract §8's order. **In its first lines:** the Release — its id, the tag, its commit, 47 assets and their bytes — with G-UPLOAD, G-DOWNLOAD and G-TAG; G-SOURCE, G-PACK, G-RESERVE and DETERMINISM; **the geoblock's line as printed**; the advisor's `commit.txt` where it differs from `4e6db2d…`; G-STILL; and every block the classifier refused and who ran it. **Every asset by name, bytes and SHA-256**, as `pack` printed the set — contract §5.1's local hash, with `verify`'s line of each as its record and its download — and the manifest's SHA-256 named as such. Beyond what V1 to V19 print: §0.0's clock line; every day as `pack` printed it, and **every file withheld, by its name, bytes and reason**; who ran B-UPLOAD and when, its `credential:` line, each run's last lines and the transfers' lines of `upload` and `verify`; every free-space and `MemAvailable` read with its instant and bound, and every mode's printed peak; §0.3's `du` and journal lines at both runs; §9's counts and removals; and every file the run wrote, by SHA-256. **It prints no member's content and no figure from one** (§2 item 4), no credential (§2 item 5) and no address of the host (§2 item 6). **The report is drafted in the primary checkout `/root/btc-5m-twap` after §3.9 and before B-RECLAIM-OWN, and committed after it**, so the removal of this TZ's tree is in it. **A BLOCKED report is contract §9's, and beside it — this TZ's own exception, said so in the report — the `GEOBLOCK READ:` line where §3.5 ran, the Release's state where B-UPLOAD ran, and §9's lines.**

---

## 9. Reclaim — the host left clean (CANON hard rule 15)

**What a file is kept for:** a committed report prints its SHA-256, whole or as a prefix of 16 to 64 hex characters, or it is kept by name: `state.json` and every file under `logs/` (lines 1141 to 1147 and 1150 to 1151). `reclaim` copies each into `/root/btc-forensics/` as `<tree>--<path with / as -->`, by exclusive create, and verifies its hash; a name already there with the same hash is counted as held, and with another hash is a failed assert; **before each copy it reads free space and BLOCKS where the copy would leave less than `7,400,000,000` bytes** (lines 1172 to 1221). **The report names every asset by its hash, so the twelve archives and the manifest are copied with the rest** — about `196,000,000` bytes the forensic store keeps (§0.4); the 34 TZ-43 files were never in this tree. The branch worktree is not copied: `reclaim` asserts that `git status --porcelain --ignored` in it prints nothing and that its `HEAD` is its upstream's (lines 1154 to 1161), so `git worktree remove` needs no `--force`. The report's draft in `CryptoReports/` counts as a report. **No `reclaim`'s output is filtered** (map §7 item 119): every line it prints is quoted. B-RECLAIM-SCRATCH is §3.3.

**B-RECLAIM-OWN**, last, after §3.9 and with the report drafted. **Its output is written to no file; the report quotes it verbatim from the session**, every line of it:

```
cd /root/tz44-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz44-work/wt/research/tz44-l0-inputs-release.py reclaim /root/tz44-work
cd /root/btc-5m-twap && git -C /root/btc-5m-twap worktree remove /root/tz44-work/wt; echo "exit=$?"
rm -rf /root/tz44-work; echo "exit=$?"
test -e /root/tz44-work; echo "exit=$?"
git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
find /root/btc-forensics -type f | wc -l
df -B1 --output=source,size,avail /var/lib/btc-recorder
```

`reclaim` must print `RECLAIM PASS` before the removals. **Its paste**, where the classifier refuses any line of it — every step chained to the one before it, the removals reached only after `RECLAIM PASS`; its output goes to the Boss's terminal, the tree its log would be in being removed:

```
(cd /root/tz44-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz44-work/wt/research/tz44-l0-inputs-release.py reclaim /root/tz44-work) && cd /root/btc-5m-twap && git -C /root/btc-5m-twap worktree remove /root/tz44-work/wt && rm -rf /root/tz44-work; test -e /root/tz44-work; echo "exit=$?"; git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list; find /root/btc-forensics -type f | wc -l
```

Where the Boss ran it, the Executor verifies it by its own reads — `test -e /root/tz44-work; echo "exit=$?"`, `git -C /root/btc-5m-twap worktree list`, `find /root/btc-forensics -type f | wc -l` and `sha256sum /root/btc-forensics/tz44-work--*`, each copy's hash against the report's — and the report quotes those reads; a refused first attempt is quoted too. The branch `tz-44-l0-inputs-release` stays on `origin` and as a local ref; only its working tree goes. **Kept:** the running units' code trees, the capture roots, both archives' state, the forensic store and the Release — data and code, never scratch.

---

## 10. Pre-send checks

Performed by the Architect on 2026-11-12, against this file as sent and read start to end in a pass apart from its writing (CANON PART VI), with `origin/main` at `7f7d7b1` — map revision `2026-11-12-a`, 2,082 lines, 588,791 bytes, SHA-256 `58b771df…` — cloned in the session. Line numbers of the instrument are those of Appendix A's file; of TZ-27's, of `research/tz27-pairbook-archive.py` at `7f7d7b1`, SHA-256 `2cba96bc…`. Every line reference to those two files, in §0 to §9 and in this section, was resolved from them by their syntax trees and by text, not typed; the lines of other files were read with `grep -n`.

**What the Architect ran, and on what.** §0.1's script against this file as sent, in a stand-in checkout at `7f7d7b1` with this file added, printing §0.1's two rows; then `I0 fingerprint` against the map and the 62 files of `7f7d7b1` — `FINGERPRINT PASS: revision 2026-11-12-a; anchors 6 of 6, 4 re-derived; rows 62: frozen 59 of 59 equal, tracked 2, reported 1` — and `I0 number`, `NUMBER PASS - 2 of 2`. Every mode on a stand-in host under Python 3.12.3 (§6): a synthetic store of the twelve days with a thirteenth, reserved, beside them — every file of replies gzip lines of records with their bodies, at about the store's sizes, four of them carrying an error page, a rate limit's text or a status-200 page that is no JSON, and the reserved day one more — the 34 sources at TZ-43's sizes, TZ-27's `_FakeGitHub` in another process, and the clock's rule itself in place for one `upload` and `verify` — begun at second 595 of a window, its first request held `320.1` s to second 15 of the next, all 99 requests of the two inside the stretch — and replaced by an immediate return for the other runs. **The four files were withheld, each named by its line, and no body of theirs is in any archive:** every member of the twelve archives was read back, `2,234` of them and `921,940,280` bytes once decompressed, for the page's address, its marker, the rate limit's text and the reserved day's and the root's bytes, and none was found, nor in the manifest. `literal_rows_missing` on TZ-43's committed report itself: 34 of 34 rows found, the report 97,435 bytes, SHA-256 `606b7ff6…`. TZ-27's `credential` under both audit hooks with a stand-in `gh` and stand-in tokens: in `upload` it returned from the remote URL and from `gh`, and in `verify` this file's hook refused `gh`. `geoblock` against the venue from the session, three runs on the bytes sent and four kept from the bytes before them: status `200`, 66 or 67 bytes, the four keys `blocked`, `country`, `ip` and `region`. `reclaim` with free space read `1,000,000` bytes above the floor: 24 small files copied, then a BLOCK at the first archive, none copied. **B-UPLOAD's paste and its wait block**, a stand-in command in the instrument's place, in an interactive shell on a pseudo-terminal: run to its end, `exit=0` and its last five lines printed; the terminal closed under it, and it ran on and wrote `exit=0`; and an interrupt key under it, which left `run begun` once, no `exit=` line and no process — the case §3.6 hands over again; `pgrep -fxc` counted the stand-in's whole command line `1` while it ran and `0` after, and never the shell that asked.

| # | check | result |
|---|---|---|
| **C1** | scope against body | **Repository paths the body names.** Written: `research/tz44-l0-inputs-release.py`, new, and `CryptoReports/TZ-44-l0-inputs-release-report.md` — §2's two. Read: this file; `SYSTEM-MAP.md` and the 62 files of its §0 table; `research/tz27-pairbook-archive.py`; `CryptoReports/TZ-43-l0-our-quote-report.md`, by `pack`, which prints its bytes, its SHA-256 and a count; every `.md` of `CryptoReports/`, by `reclaim`, for its hex tokens. Cited and not read by the run: `research/tz28-pairbook-archive-timer.py`, `research/tz33-reward-book-capture.py`. **Committed entry points:** TZ-27's `credential`, `GitHub`, `build_request`, `upload_set`, `verify_release`, `release_reading`, `ls_remote_tag`, `upload_ready`, `store_path`, `HashingReader`, `opener`, `json_bytes`, `forbid`, `_FakeGitHub` and its audit hook — C7. **Output files:** under `/root/tz44-work/`, `logs/*`, `stage/research/*`, the worktree, `state.json`, `out/rewardbook-inputs-<D0>.tar` twelve times — by content class: bodies of the venue's replies — `out/tz44-manifest.json`, `set.json`, `upload.jsonl`, `transfers.jsonl`, `verify.json` and the self-test's temporary tree; their copies in the forensic store; the report; and on `origin` the branch, the pull request, the tag and the Release's 47 assets. **Intersections with §2's prohibitions, by path and by content class, each removed or exempted in §2's text:** item 2 — the recorder's root is read by `df` in §0.3, §3.9 and §9 and by §0.3's `find` and `grep -c`, the pair book's by §0.3's `du -sb`, and the pair book archive's `ledger.jsonl` by §0.3's `stat` and `I still`: all named there; item 3 — `pack`'s reads, §0.3's `stat` and the `du -sb` of §0.3 and §3.9: named there; items 3 and 4 by content class — the assets carry prices, sizes, rates, competitiveness and outcomes of the twelve days: the exemption stated above the list, and no log, print or report line carries one; item 4 — the geoblock's reply is printed by three fields and its key names: named there, with item 6; item 5 — `credential` runs `git remote get-url` and `gh auth token` inside `I upload`, in the Boss's shell: named there; item 8 — the Executor's `git` and `gh pr create`, the session's web tool for GitHub's status page and the one request to the venue: named there; item 9 — the report on `main` and the Release by `I upload`: named in §2's two lists; item 10 — §0.3's `cat` of the advisor's `commit.txt`: named there; item 11 — `upload_set` removes an asset of this Release that does not match before sending it again: named there. **Found by this check and corrected before sending: item 6 by content class** — the store keeps the body of every try, an error's among them, and an error page of the venue's edge can carry the host's address, so an archive of the store's files verbatim could have published what item 6 bars from every log: `pack` now reads every file of replies and leaves out one that holds any body but a JSON document served under status 200 (§1), and the self-test and the Architect's store prove a file so withheld is in no archive. **And in §2's wording:** items 2 and 3 named §0.3's reads alone where §3.9 and §9 repeat `df` and `du`; item 4 barred "a reply" where the geoblock's is printed in part; item 8 said `github.com` where `gh` reaches GitHub's API; item 11 barred every removal from a Release where `upload_set` replaces a mismatching asset. |
| **C2** | origin of every expectation | **Quoted from a committed artifact at `7f7d7b1`:** revision `2026-11-12-a`, the six anchors, `62`, `59`, `2` and `1` — map §0, which states what a later fingerprint expects; TZ-27's file's 2,078 lines, 106,284 bytes and SHA-256 — map §0's row; the 34 rows of `TZ43_FILES` — TZ-43's report §2.6, each found there by `literal_rows_missing` in the Architect's run, their sum `42,169,992` computed from the report's rows by `awk`; `31612203008` and the recorder's commit of H2 — map §6, host identity; `2,487`, the three UUIDs, `4e6db2d…` — map §3, the commit's forty characters from `origin`'s `refs/heads/tz-42-advisor-registry`; `7,300,000,000` and `100,000,000` — `research/tz33-reward-book-capture.py` lines 190 and 192; `58,953,728 / 49,168,384` — map §6, memory; the free-space and `MemAvailable` reads of §0.4 — map §6, disk and memory; the idle stretch's seconds, both calendar runs and TZ-28's budget — map §2.5, §2.6 and `research/tz28-pairbook-archive-timer.py` lines 99 to 101 and 135 to 137; TZ-27's messages `UPLOAD REFUSED`, `UPLOAD INCOMPLETE` and `release by tag … status` — its lines 739, 800, 810 and 588. **Computed by an implementation independent of the one under test:** the instrument's 1,616 lines, 90,703 bytes and SHA-256, by `wc` and `sha256sum` against §0.1's script; `14,281,610`, by `git ls-tree -r -l`; `49,159,697` and `98,319,394`, integer arithmetic on the quoted ratio and the bound. **The Architect's measurements, named as his:** the bound `41,000,000` and every peak and time of §0.4 and §6; `38 checks`, the self-test's own count, equal to its `ok` lines in the Architect's logs; TZ-43's 5 polls not served of 345,600, summed from the eight `fetch` lines of its committed report. **Counts of sets this TZ defines** (C5): `12`, `13`, `14`, `32`, `34`, `47`, `7` and `5`, `2 of 2`, `3`. **Identities, holding for every value the run takes:** opens equal to members and listings to days; the second run's bytes equal to the first's; `verify`'s bytes equal to `set.json`'s `bytes_total`; the store's count after `reclaim` equal to before plus the copies. **Barred from expectation:** the members' counts and bytes and every archive's hash — the store's, printed — and the geoblock's reading. No expectation depends on a quantity this TZ measures. |
| **C3** | shape of every diff | One file added, `research/tz44-l0-inputs-release.py`, absent at `7f7d7b1` (`git cat-file -e` exits 128); the report's path absent there too. **Committed lines replaced: none.** The words "insertions only" appear nowhere but in this row. |
| **C4** | cost of every check | At the population's upper bound — twelve days of `200,000,000` bytes of members, `2,400,000,000` in all, where §6's store held `258,860,337`: `pack` `278` s a run at `8,659,635` bytes a second, the slowest of the Architect's seven runs, `556` s for G-PACK and DETERMINISM together, the scan of the replies inside it; G-SOURCE `42,169,992` bytes, a constant, `5` s at that rate; the upload of the archives and the 34 sources, `2,442,169,992` bytes, `263` s at the host's `9,297,801` bytes a second with `47` s of TZ-27's gaps; their downloads `188` s at `13,000,000`; `reclaim`'s copies of the archives, each hashed, copied and hashed again, `832` s at the first rate — `1,891` s in all, under `3,600`, nothing sampled; the fingerprint, the number, the self-test, `still`, `scratch` and `geoblock` do not grow with the data: `0.78` s the largest measured, `30` s the geoblock's bound. A store at that bound does not finish on this host: the disk floor BLOCKS `pack` first. **Fail-fast bounds, term by term:** a hold `7,200` s, TZ-43's bound for the same rule (`research/tz43-l0-our-quote.py` line 126), where a stretch opens every 900 s — `324 + budget` s at most between two — and an archive's own unit may run to its `TimeoutStartSec`, 21,600 s (`deploy/systemd/btc-pairbook-archive.service` line 13), beyond which a hold BLOCKS rather than waits; a transfer's budget `5 + ⌈bytes / 2,000,000⌉` s, `105` s at the bound for an archive's members and a second more with its headers, and a day's `30 + ⌈bytes / 500,000⌉` s, `430` s at the bound where the Architect's slowest run needs `24`, each inside the stretch's `575` s; the memory floor `4 × 60` s a mode; the geoblock `30` s; TZ-27's request timeouts `60`, `300` and `120` s, four attempts a file with waits to `900` s, three a download; B-UPLOAD `21,600` s from its first hand-over, three runs, the Executor's wait block `9 × 60` s a run of it; `I verify` three runs `600` s apart, the last waiting 6 h at most. |
| **C5** | every count | `62` rows, `59` + `2` + `1` — map §0's table at `7f7d7b1`, counted by the instrument's own run there. `6` anchors, `4` re-derived — `A2`, `A4`, `A5`, `A6`. Host gate `7` — H1, H2 twice, H3, H4, memory, disk — and `5` at §3.9, H1 to H4. H4's `13` lines — the ledger and twelve directories. `12` days — `D0` from `1793145600` to `1794096000` in steps of 86,400. `34` files — TZ-43's 8 member days times `fetch/<D0>.json`, `fetch/<D0>.polls.jsonl`, `days/<D0>.json` and `days/<D0>.slots.txt`, with `set.json` and `reading.json`; `32` of them under `fetch/` and `days/`. `14` outputs — 12 archives, the manifest, `set.json`. `47` assets — 12 + 34 + 1. `2 of 2` — NUMBER's two conditions. `38` self-test checks. `139` ref lines — `HEAD`, `main`, 19 branches, 42 pull heads, 50 and 22 tags, 2 annotated tags with their 2 peeled lines. `19` validation rows. |
| **C6** | every population | G-SOURCE: the 34 files. G-PACK: every name of the twelve day directories; the members are every selection, reply file, slot record and poll file among them, and the files scanned every member whose name ends `.jsonl.gz`. G-RESERVE: every open and listing under the store by `pack` — one a member kept, one a file scanned, one listing a day. DETERMINISM: `pack`'s 14 outputs. G-UPLOAD, G-DOWNLOAD: the set's 47 assets. G-TAG: the one tag. G-STILL: the four units, and the pair book archive's restart records since the first read. GEO: one request. The transfers' lines: every record of `transfers.jsonl` — `upload`'s requests, then `upload`'s and `verify`'s. Peaks: each run of each mode. Floor reads: the host gate's, and each start of `pack`, `upload` and `verify`. `reclaim`'s counts: every regular file under the trees it names, the branch worktree aside. §6's times and §0.4's peaks: the Architect's runs named there. |
| **C7** | every signature and every behaviour | Read at `7f7d7b1`. **`def credential():`** (line 725) — "under the token the remote URL carries or else the one `gh` holds; `upload` prints its source alone": `return tok, "the primary checkout's remote URL"` (732), `return tok, "gh auth token"` (738), `raise AssertionError("UPLOAD REFUSED: no credential - the remote URL carries none and gh holds none")` (739); it runs `git -C PRIMARY remote get-url origin` and `gh auth token --hostname github.com`, which this file's hook gives `upload` alone. **`def build_request(method, url, token=None, accept=ACCEPT_API, data=None, ctype=None, length=None):`** (509) — "every request under TZ-27's agent, `Accept` and the API version": `headers = {"Accept": accept, "User-Agent": UA, "X-GitHub-Api-Version": API_VERSION}` (512), `UA = "btc-5m-twap-tz27"` (78). **`class GitHub:`** (559), `def __init__(self, token=None, api=API_BASE, uploads=UPLOAD_BASE, web=WEB_BASE):`, `def _json(self, method, url, body=None):`, `def upload(self, rid, name, path, nbytes):`, `def download(self, url):`, `def create_release(self, tag, name, body):` — `Gh44` overrides those four with the same parameters, and `__init__`, which passes `token`, `api`, `uploads` and `web` on; "its `upload` reads `CONTENT_TYPE` at each call": `req = build_request("POST", url, token=self.token, data=rd, ctype=CONTENT_TYPE, length=nbytes)` (625); "each write follows the last by 1 s or more": `pace` (580 to 584) with `UPLOAD_GAP_S = 1.0`, called by TZ-27's `upload` and `delete_asset` and by `Gh44.create_release`; "a download sends no credential": `req = build_request("GET", url, accept=ACCEPT_BLOB)` (643); TZ-27's `create_release` sends no `target_commitish` (591 to 599), so `Gh44`'s replaces it, as TZ-28's `Gh28` does. **`def upload_set(gh, rel, doc, root, log, wait_min=WAIT_MIN_S):`** (765) — "stops where the Release holds an asset outside the set": `assert not beyond, "the Release holds assets outside the set: %r" % beyond[:5]`; "keeps an asset already matching": `if a is not None and matches(a, x):` with `matches` (758 to 762) — `state` `uploaded`, the set's size, the digest `None` or the set's; "removes and sends again one that does not, at most four times a file": `for attempt in range(1, UPLOAD_ATTEMPTS + 1):`, `gh.delete_asset(int(a["id"]))`, `UPLOAD_ATTEMPTS = 4`; "hashes every byte as it is sent and asserts the Release's record": `assert sent_n == x["bytes"] and sent_sha == x["sha256"]`, `assert doc_.get("name") == x["asset"] and doc_.get("size") == x["bytes"]`, continued on its next line by `and doc_.get("state") == "uploaded"`, `assert doc_.get("digest") in (None, "sha256:" + x["sha256"])`; "a refusal that is not a rate limit": `assert w is not None, "UPLOAD REFUSED: %s status %r" % (x["asset"], status)` with `wait_for` (742 to 755) returning a wait for 403, 429, no status, 5xx and 422 and `None` otherwise; it returns `sent, held`. **`def verify_release(gh, tag, doc, download=True):`** (685) — "a full download of each where every record is the set's": `if download and not missing and not extra and all(r["api_ok"] for r in rows):`, `api_ok` being `state` `uploaded`, the set's bytes, the digest `"sha256:" + x["sha256"]` and the tag's download URL (`asset_row`, 672 to 682); it returns `rel, rows, missing, extra`. **`def release_reading(rel, tag, rows, missing, extra):`** (703) — five checks, whose names §3.7 quotes: `"no asset missing"`, `"every asset uploaded, its bytes and digest the set's"` among them. **`def ls_remote_tag(tag):`** (1139) returns the tag's object and its peeled commit, `None` where `origin` gives no peeled line — `tag_reading` asks the first equal to the pack's commit and the second `None`. **`def upload_ready(records, assets_n, now_ns):`** (1219) — `None` once `upload`'s last record is its completion for every asset, `UPLOAD_SETTLE_S`, 120 s, or more before now. **`def store_path(root, x):`** — `os.path.join(root, str(x["T"]), x["file"])`: the set's `T` is `tz44-work/out` or `btc-forensics` under `/root`. **`class HashingReader:`**, `def read(self, size=-1):` — hashes and counts what it returns. **`def opener(follow):`**, `def json_bytes(obj):`, `def forbid(obj, what, depth=0):` — `upload.jsonl`'s keys are `asset`, `action`, `id`, `bytes`, `sha256`, `digest`, `state`, `status`, `attempt`, `wait_s`, `assets`, `sent`, `held`, `release_id`, `created`, `credential`, `wall_ns` and `at`, none of them forbidden. **TZ-27's hook**, `def policy(mode, event, args, work, allowed):` (214) — with `WORK[0]` `/root/tz44-work` it allows a write and a change under that tree alone and an exclusive create in the forensic store in mode `reclaim`, and refuses no process in this file's modes: `NO_PROCESS = ("inventory", "delete")`; every mode ran under it in the Architect's runs with `by TZ-27's hook: 0`. **`research/tz28-pairbook-archive-timer.py`** `def budget_s(nbytes):` — `return MARGIN_S + -(-int(nbytes) // RATE_FLOOR)`, `MARGIN_S = 5`, `RATE_FLOOR = 2000000`, `IDLE = (15, 590)`: this file's are equal. **`research/tz33-reward-book-capture.py`** — `STREAM_FLOOR = 7300000000` (190), `SLOT_STREAM_MAX = 100000000` (192), `SLOT_FILE_RE` and `SELECT_FILE_RE` (228, 229), equal to this file's; `select_paths` (984) and `slot_paths` (1096 to 1098) give the five names; `SLOT_JSON_AT = 910` (171); and "the store keeps the body of every try, an error's among them": `def http_get(url, timeout=READ_TIMEOUT_S):` (590), `body = exc.read()` under `except urllib.error.HTTPError` (602) and `"raw": raw` in the record it returns (617), no reply header and no address of either end stored (`REPLY_KEYS`, `POLL_KEYS`, `SLOT_JSON_KEYS`, lines 233 to 242). **`research/tz43-l0-our-quote.py`** `def polls_text(polls):` (1666) writes each poll as its instant, its market and its two parsed figures, so TZ-43's 34 files hold no body of a reply and are published whole. **Found by this check and corrected before sending:** §3.6 named a message `no credential` that TZ-27 prints as `UPLOAD REFUSED: no credential …`; §3.7 sent every `VERIFY FAIL` back to B-UPLOAD, where `upload_set` stops at an asset beyond the set; §1 and §5 cited TZ-27's spans from memory, five of them wrong by lines; and the header promised an end before the next morning's package run, which B-UPLOAD's wait can pass. |
| **C8** | every cross-reference | **Map `2026-11-12-a`, each read in the clone:** §0 — the revision, the anchors, the table, what a later fingerprint expects; §1 — its revision's refs record, 138 lines; §2.5 — the pair book's idle stretch, seconds 15 to 590, and its archive's run at 03:00:20 UTC and 600 s after a start of its timer; §2.6 — the store's files and layout, `16.3` MB a day beside its streams, its first day from 11:30:16 UTC, its archive's run at 01:30:20 UTC removing each stream once proven, the reserve from `1794182400` and the nine candidates read; §3 — the forensic store's `2,487` files and TZ-43's 70 copies under `tz43-work--`, the two worktrees, the three UUID directories, the code trees and the advisor's `commit.txt` `4e6db2d…`; §6 — host (a Vultr VPS in Warsaw), host identity, language (Python 3.12.3 under `/root/tz04a-env`), git remote, disk, process supervision, memory, sandbox limit — network, GitHub Releases, sandbox limit — destructive actions, harness; §7 items 115, 118, 119, 120, 124, 129, 131, 132, 137, 138, 140, 141, 143, 144, 149, 150 to 157 and 159, each beside the sentence that cites it. **CANON `2026-11-12-a`:** hard rules 2, 5, 14, 15 and 16; fingerprint gates — a process's state is not host identity; PART II — the L track's reserve and days read, and no order before an L0 gate reads EARN; PART VI — C4's `3,600` s and a set read being an exploration; §1.5 — L0's money not re-derived. Hard rule 17: this TZ replaces no `frozen` row, and no uploaded TZ waits to run. **Contract** (`A4`, `437b45ea196b`): §1, §4.2, §5, §5.1, §8, §9 and §10 — where this TZ differs it says so: `I verify` in place of §5.1's `curl`, the paste's `exit=` line in place of the Boss's confirmation, and §8's addition to a BLOCKED report. **The venue's documentation**, `docs.polymarket.com/api-reference/geoblock`, read on 2026-11-12: the endpoint, its four fields, and Poland in its list of countries where positions may only be closed, on the website and in the API. **The Boss's words:** none is quoted; his request is named by its map revision and item. **This file's own references**, §0 to §9 and Appendix A, each resolved by reading. |

**What the session could not check, and the condition that stands in its place (CANON hard rule 13):**

- **The store's twelve directories** — their names, sizes, state and the bodies inside their files are the host's alone. `pack` classifies every name and BLOCKS on a slot of another day, a member that is not a regular file, a day with no member, with every member withheld or above `200,000,000` bytes, and a file that changes while read (582 to 592, 675 to 694, 697 to 742); **how many files it withholds is the store's, printed**, and the rule that withholds them was proved on the Architect's store alone.
- **The 34 files in the forensic store** — G-SOURCE, by bytes and SHA-256.
- **GitHub's own behaviour** — the session is refused this repository's Release API (map §6, GitHub Releases), so the request path ran against TZ-27's `_FakeGitHub` alone: that a Release created with `target_commitish` makes a lightweight tag at that commit is TZ-28's daily practice on the host and is asserted by G-TAG; that each asset's record carries a `digest` is asserted by G-UPLOAD.
- **The credential in the Boss's shell** — `upload` stops with `UPLOAD REFUSED` where there is none; both archives read it through the same function every night.
- **The Boss's terminal** — the paste's wrapper ran on a pseudo-terminal of the session's alone. A marker his terminal may write into a log's first line (map §7 item 138) moves nothing: §3.6's block counts `run begun` and `exit=` lines, each on a line of its own below the first.
- **The venue's reply to the host** — the endpoint was read from the session's own address alone; `I geoblock` reads it from the host and prints its three fields.
- **The host's memory and disk at the run** — §0.3's gates and each mode's floor reads.
- **The classifier** — each block it may refuse has its paste.

---

## Appendix A — the instrument, byte for byte

`research/tz44-l0-inputs-release.py` — 1,616 lines, 90,703 bytes, SHA-256 `0b78807d9c5dec087138b0c9a329cb8c976157ab5c8a3fd4deee7cb31e89e190`. §0.1's script extracts it; nothing below the fence's last line is part of it.

```python file=research/tz44-l0-inputs-release.py
#!/usr/bin/env python3
"""TZ-44 - L0's inputs off the host: one Release of the reward book's days before the reserve - every file of a day's
directory but its streams: its selections with their replies, its slot records and its reward polls - and of the 34
files of TZ-43's fetch/ and days/, its set.json and its reading.json, as the forensic store holds them.

    fingerprint       contract section 1 steps 3 and 4, asserted: the map's revision, anchors and rows
    number            CANON hard rule 2: no other TZ-44 specification or report on origin/main
    selftest          every rule of this file, on literals, on temporary trees and on a loopback GitHub
    still             the four units' MainPID, NRestarts and ActiveState: the first run records them, the second
                      compares, the pair book archive's own restarts read from its ledger (G-STILL)
    scratch OWN       the UUID directories beside OWN, this session's, each named live or earlier
    pack              G-SOURCE - TZ-43's 34 files by the bytes and SHA-256 its report names - then G-PACK: one tar a
                      day of the store's day directory but its streams and but every file of stored replies that
                      carries a body the venue did not serve as JSON under status 200; the manifest and the set; a
                      second run asserts every output unchanged (DETERMINISM)
    upload            B-UPLOAD, the Boss's block: the Release on tz-44-l0-inputs at this file's commit, and the set's
                      assets, through TZ-27's own client, every request held
    verify            G-TAG, G-UPLOAD and G-DOWNLOAD, with no token: the tag on origin, the API's record of every
                      asset and a full download of each
    geoblock          the venue's own reading of the host's address, printed: blocked, country, region - never the
                      address
    reclaim TREE...   section 9

It loads TZ-27's instrument, research/tz27-pairbook-archive.py, from beside itself by its SHA-256, and sends every
GitHub request through TZ-27's client - build_request, GitHub, upload_set, verify_release, credential - each one held
to the pair book's idle stretch and away from both archives' runs. TZ-27's audit hook is installed then; this file's
own refuses every open, listing, request and process TZ-44 section 2 does not give the running mode: under
/var/lib/btc-rewardbook/ it lets pack list the twelve day directories and read their selections, slot records and
reward polls, and nothing else - no stream file, no day from 2026-11-09, no file of the store's root. It writes under
/root/tz44-work/ and, in reclaim, new files in /root/btc-forensics/ by exclusive create. It prints names, counts,
bytes and hashes, never a file's content. An error page can carry the address it was served to, so a file of stored
replies is published only where every body in it is a JSON document the venue served under status 200. Exit 0: every
assert of the mode held. Exit 1: an assert failed, and its message names it. Run it with the recorder's interpreter,
/root/tz04a-env.

Written for CryptoTZ/TZ-44-l0-inputs-release.md. The TZ is the specification.
"""

import collections
import ctypes
import datetime
import gzip
import hashlib
import json
import os
import re
import resource
import shutil
import socket
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

if not __debug__:
    sys.stderr.write("tz44: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(2)


def _malloc_tune():
    """glibc's mmap threshold at 128 KiB and two arenas, as TZ-23's, TZ-33's and TZ-43's instruments fix them."""
    try:
        libc = ctypes.CDLL("libc.so.6")
        return libc.mallopt(-3, 131072) == 1 and libc.mallopt(-8, 2) == 1
    except OSError:
        return False


MALLOC_TUNED = _malloc_tune()
HERE = os.path.dirname(os.path.abspath(__file__))

# ---- the TZ's constants: none of them is measured by this run -----------------------------------------------

MAP_REVISION = "2026-11-12-a"
ANCHORS = {"A1": "229a944f2d51", "A2": "6c5089330629",
           "A3": "0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable",
           "A4": "437b45ea196b", "A5": "0f6c90451cbd", "A6": "729f0bcdbee3"}
ANCHOR_FILES = {"A2": "research/twap-divergence.py", "A4": "BTC-EXECUTOR-INSTRUCTIONS.md",
                "A5": "research/recorder/recorder.py", "A6": "research/pfair.py"}
MAP_ROWS = {"frozen": 59, "tracked": 2, "reported": 1}
ROW = re.compile(r"^\| `([^`]+)` \| ([0-9,]+|—) \| ([0-9,]+|—) \| (frozen|tracked|reported) \| "
                 r"(?:`([0-9a-f]{64})`|[^|]*) \|$", re.M)
ANCHOR_ROW = re.compile(r"^\| `(A[0-9])` — [^|]*\| `([^`]+)` \|$", re.M)
NUMBER = "TZ-44-"
OWN_TZ = "CryptoTZ/TZ-44-l0-inputs-release.md"

DAY = 86400
SLOT = 900
FIRST_D0 = 1793145600        # 2026-10-28 00:00:00 UTC: the reward book's first day (TZ-33)
LAST_D0 = 1794096000         # 2026-11-08 00:00:00 UTC: the last day before the reserve
RESERVE_D0 = 1794182400      # 2026-11-09 00:00:00 UTC: every day from it is reserved for L0's next gate
DAYS = tuple(range(FIRST_D0, LAST_D0 + DAY, DAY))
MEMBER_KINDS = ("select", "slot", "rewards")
KINDS = ("select", "slot", "rewards", "stream", "other")
DAY_MAX_BYTES = 200000000    # a day's members above this BLOCK: twelve times TZ-33's 16.3 MB a day
UNIT_BUDGET_S = 60           # the 34 sources, one unit of pack, are held for this many seconds
UNIT_BASE_S = 30             # a day, one unit of pack, is held for this many seconds and for its members' bytes at
SCAN_RATE = 500000           # this many stored bytes a second: its scan of the replies, its archive and its hashes
SCANNED = ".jsonl.gz"        # a member of stored replies: scanned, and published only where no line withholds it
RATE_FLOOR = 2000000         # bytes a second a transfer is budgeted at, TZ-28's
MARGIN_S = 5                 # seconds every request is budgeted beyond its bytes, TZ-28's
IDLE = (15, 590)             # the pair book's idle stretch: a unit starts at second 15 or later, ends by 590
CALENDAR = ((5420, "the reward book archive's calendar run at 01:30:20 UTC"),
            (10820, "the pair book archive's calendar run at 03:00:20 UTC"))
CALENDAR_LEAD_S = 60
RUNNING = ("active", "activating", "deactivating", "reloading", "refreshing")
HOLD_MAX_S = 7200
MEM_FLOOR = 98319394         # MemAvailable: twice the host peak modelled for the Architect's bound on any mode's
#                              peak, 41,000,000, at the ratio TZ-37 measured, 58,953,728 / 49,168,384 (section 0.4)
MEM_RETRY_S = 60             # a MemAvailable read below the floor is read again this much later,
MEM_READS = 5                # five reads at most
DISK_FLOOR = 7400000000      # free bytes on /dev/vda2 once a day's archive is written: the reward book's
#                              STREAM_FLOOR, 7,300,000,000, and one slot of its streams at the cut, 100,000,000
DISK_GATE = 7800000000       # free bytes at a mode's start: DISK_FLOOR and 400,000,000 for what this session may
#                              still write then, its archives and their copies (section 0.4)

TAG = "tz-44-l0-inputs"
MANIFEST = "tz44-manifest.json"
ARCHIVE_FMT = "rewardbook-inputs-%d.tar"
UA = "btc-5m-twap-tz44"
GEO_URL = "https://polymarket.com/api/geoblock"
GEO_HOST = "polymarket.com"
GEO_HEADERS = {"User-Agent": UA, "Accept": "application/json"}
GEO_TIMEOUT_S = 30
GEO_READ_MAX = 65536
CONTENT_TYPE = "application/octet-stream"

# TZ-43's work files, as its report's section 2.6 names them: path in its tree, bytes, SHA-256
TZ43_REPORT = "CryptoReports/TZ-43-l0-our-quote-report.md"
TZ43_MEMBERS = (1793404800, 1793491200, 1793577600, 1793664000, 1793750400, 1793836800, 1794009600, 1794096000)
TZ43_FILES = (
    ("fetch/1793404800.json", 55310, "5f56487e44aadcba1df2bc1316a889605baf83a4fcafc965b5ee4a18a6fec9b2"),
    ("fetch/1793404800.polls.jsonl", 4990923, "53ae4e79d354b3f8b35d497654159162b9c2290deb0d69b6f62b79c3fe8c1d71"),
    ("fetch/1793491200.json", 55330, "55f95448c4ba6abe1d1b154ff0e014ef190ffb7be861a7f6cb1a3bcddec7a1bd"),
    ("fetch/1793491200.polls.jsonl", 5010687, "1aac9148f26b55664b248be60b62394defc1b117b63bcd952c632bf96b3ebf54"),
    ("fetch/1793577600.json", 55447, "8589729bfe267feb57208833064bc71006e592e22edd8290d70bbc2b4474d9b5"),
    ("fetch/1793577600.polls.jsonl", 5027379, "19d765c78c93e9d4175328615ae3dc27b3e2f0c1dd7f6084eeab672a9e56427c"),
    ("fetch/1793664000.json", 55449, "1405b48ac2459f052b5b36dea8e85dd6cb0e112b49ac21030955d96f890eec02"),
    ("fetch/1793664000.polls.jsonl", 5014920, "4a5ef449ed6b1d2bf1378b817671b9bb3cac477c5a9fa6e5068d9673b24977cb"),
    ("fetch/1793750400.json", 55543, "1ed8768bd80b54220c0437e15fc424943a8829b716d7ba70f2b586f5ae14099c"),
    ("fetch/1793750400.polls.jsonl", 4967708, "f06145aa32845b9f3a65b8616e5842218b03869a3fc18d5a4bf1aaaa57fec920"),
    ("fetch/1793836800.json", 55625, "7d502a56ad2a4a3f95150bbcfc8c52c1190f2b977d9d1a72e2e1c4b3c2f5ba25"),
    ("fetch/1793836800.polls.jsonl", 5055307, "7918f3b6629489fcff4fd22cdb049a89e1e1ef63b86738c73ec680e17e5eff5d"),
    ("fetch/1794009600.json", 55639, "29e17ecde5f5d705e297bdc2be7e5e150aa50d06c3ac66ba9b1c4c13225b5708"),
    ("fetch/1794009600.polls.jsonl", 5037697, "91582ccfb9145559277d196f61e804e6be205d0b18d6168a1db6975711d6cf15"),
    ("fetch/1794096000.json", 55660, "a3ebc56744facb5c00f862c1f5d70a564672b68b5cc276398f32ae7f1bc0c552"),
    ("fetch/1794096000.polls.jsonl", 5047340, "7b0d86338359fbb4d5f4f7b54c6f36e0d45f2ed5c4d6d5731358c8e4e3099a82"),
    ("days/1793404800.json", 145864, "d93f998fba7795f30379c06e2058c55f4eba9d0c340536a3d5a4d1636b765ee6"),
    ("days/1793404800.slots.txt", 47260, "ec4494031d22891f22ec2822287c0127c4f96f39dac1337f3980419813052400"),
    ("days/1793491200.json", 147006, "50e19969a8196ef3fe8b069056b75bb3ff5f5ba1c41a9ad70a48bd7e88ebaaae"),
    ("days/1793491200.slots.txt", 47077, "5a7169dbcdb3186b588e2bd77ef5017dc792f1ead7cc8d2b9c11a55cee90f763"),
    ("days/1793577600.json", 146744, "93c76d1594b1edef03e192c02cc67b0264e43ca4b77b6d49939845f5876dc57c"),
    ("days/1793577600.slots.txt", 46799, "aae9a59997c591b90672bec21ea2489e2f7e654eba03590bc8d1ff411a186e1c"),
    ("days/1793664000.json", 147691, "a80c3d721fce47537ff927c42b989cd4409d25b7c3a1e2c4e024a2463d48c54d"),
    ("days/1793664000.slots.txt", 46785, "dc9dff0e13153ee045ada2cb805c9567ce9bb4b490f88c40aa0821442fe8660b"),
    ("days/1793750400.json", 155059, "4f9ca91d2798fb9f7b496e98baa02d4fe9f6efb5f60f979540f682fb7fdadfa9"),
    ("days/1793750400.slots.txt", 47105, "71101c5d670141ce064c671824d5c8c8c1615ffce4801b1a422baa3df4281cdc"),
    ("days/1793836800.json", 149722, "e7266b1d2d05e1191095e9cd184e6bb15571ea7380fa1e4f51db90a5342e200d"),
    ("days/1793836800.slots.txt", 46750, "ec5792be99ff4169b4574b3a8ce04855ad7a5fcd51aba1b51baf4cc9d8ce44e5"),
    ("days/1794009600.json", 146104, "f3018bb242bff3b1d7483622cd4065074cc42faa90b1e8357d223c2796a6dfd5"),
    ("days/1794009600.slots.txt", 46914, "a0fdb71edc318fb7e41989c1aca3b591c9b3e4db39274e87588354639725c1e6"),
    ("days/1794096000.json", 144626, "910ed69e85ab28dc81a334538d229a66ba17107260325c1afe5eae95de02e91f"),
    ("days/1794096000.slots.txt", 46970, "00caaab0888d85779398751281da3e9219cfdf9742c77b5914499cf0c4421436"),
    ("reading.json", 9377, "175d366101cd825437a1cd393aa57642965f7ffb9fe831746c2d9b2187d50be1"),
    ("set.json", 6175, "904f1b9b8244a15fe48549e39ffc879f68ad31de6963a41c05f5afc607edf0f7"),
)

UPLOAD_ROOT = "/root"
WORK = UPLOAD_ROOT + "/tz44-work"
WT = WORK + "/wt"
OUT = WORK + "/out"
STATE = WORK + "/state.json"
SET_FILE = WORK + "/set.json"
UPLOAD_LOG = WORK + "/upload.jsonl"
TRANSFERS = WORK + "/transfers.jsonl"
VERIFY_FILE = WORK + "/verify.json"
PRIMARY = "/root/btc-5m-twap"
REPORTS = PRIMARY + "/CryptoReports"
FORENSICS = UPLOAD_ROOT + "/btc-forensics"
BRANCH = "tz-44-l0-inputs-release"
RB_ROOT = "/var/lib/btc-rewardbook"
RB_ARCHIVE = "/var/lib/btc-rewardbook-archive"
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
SHA_RE = re.compile(r"[0-9a-f]{64}")
SHA40 = re.compile(r"[0-9a-f]{40}")
SLOT_FILE_RE = re.compile(r"([0-9]{10})\.([0-9]+)\.(stream\.jsonl\.gz|rewards\.jsonl\.gz|slot\.json)")
SELECT_FILE_RE = re.compile(r"select\.([0-9]+)\.(json|replies\.jsonl\.gz)")
LIVE_S = 60
PYFILE = "tz44-l0-inputs-release.py"
TZ27_NAME = "tz27-pairbook-archive.py"
TZ27_SHA256 = "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673"

# ---- the audit hook: TZ-44 section 2's reads, writes, requests and processes -----------------------------

MODE = [None]
REFUSED = []
COUNTS = collections.Counter()
WRITE_FLAGS = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC
RB_DAY = re.compile(re.escape(RB_ROOT) + r"/([0-9]{10})")
RB_FILE = re.compile(re.escape(RB_ROOT) + r"/([0-9]{10})/([0-9]{10}\.[0-9]+\.(?:slot\.json|rewards\.jsonl\.gz)|"
                     r"select\.[0-9]+\.(?:json|replies\.jsonl\.gz))")
HOSTS = {"upload": ("api.github.com", "uploads.github.com"),
         "verify": ("api.github.com", "github.com", "release-assets.githubusercontent.com",
                    "objects.githubusercontent.com"),
         "geoblock": (GEO_HOST,),
         "selftest": ("127.0.0.1",)}
PROCESSES = {"git", "systemctl", "stat"}
UPLOAD_PROCESSES = {"gh"}
CLOSED = (RECORDER, CHAINBOOK, PAIRBOOK, ADVISOR, ADVISOR_ETC, RB_ARCHIVE)


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


def policy(mode, event, args):
    """None where TZ-44 section 2 allows the event in this mode; otherwise the reason it is refused. Pure."""
    if event == "urllib.Request":
        host = urllib.parse.urlsplit(args[0]).hostname if args and isinstance(args[0], str) else None
        return None if host in HOSTS.get(mode, ()) else "a request to %s" % host
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
        if any(_under(p, r) for r in CLOSED + (PB_ARCHIVE,)):
            return "a listing under a capture root, the advisor's or an archive's state"
        if _under(p, RB_ROOT):
            m = RB_DAY.fullmatch(p)
            if mode == "pack" and m is not None and int(m.group(1)) in DAYS:
                return None
            return "a listing under the reward book's root"
        return None
    wm, fl = (args[1] if len(args) > 1 else None), (args[2] if len(args) > 2 else None)
    w = _writing(wm, fl)
    if any(_under(p, r) for r in CLOSED):
        return "an open under a capture root, the advisor's or the reward book archive's state"
    if _under(p, RB_ROOT):
        m = RB_FILE.fullmatch(p)
        if not w and mode == "pack" and m is not None and int(m.group(1)) in DAYS:
            return None
        return "an open under the reward book's root"
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
assert tz27.REPO == "seahomebatumi-ai/btc-5m-twap" and tz27.UPLOAD_SETTLE_S == 120, "TZ-27's constants"

# ---- small helpers ----------------------------------------------------------------------------------------


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
        out("unchanged %s %d bytes sha256 %s" % (path, len(data), got))
        return "unchanged"
    write_atomic(path, data)
    out("wrote %s %d bytes sha256 %s" % (path, len(data), sha256_bytes(data)))
    return "wrote"


def load_state():
    if not os.path.exists(STATE):
        return {}
    with open(STATE, encoding="utf-8") as fh:
        return json.load(fh)


def save_state(st):
    write_atomic(STATE, (json.dumps(st, sort_keys=True, indent=1) + "\n").encode("utf-8"))


def jsonl_append(path, rec):
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, sort_keys=True) + "\n")


def jsonl_read(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as fh:
        return [json.loads(ln) for ln in fh if ln.strip()]


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
    """Before a mode that reads the store, the forensic store or the network: glibc's two settings, the memory floor -
    a read below it read again every MEM_RETRY_S, MEM_READS reads at most, the last deciding - and the disk gate."""
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

# ---- the clock: the pair book's idle stretch and both archives' runs -----------------------------------------


def archives_state():
    return {k: is_active(svc) for k, (svc, _timer) in sorted(ARCHIVES.items())}


def budget_s(nbytes):
    """The seconds a request or a unit is held for: MARGIN_S, and its bytes at RATE_FLOOR, rounded up (TZ-28's)."""
    return MARGIN_S + -(-int(nbytes) // RATE_FLOOR)


def quiet(now, budget, state_of=None):
    """None where a unit of `budget` seconds may start at `now`; otherwise why not: it starts inside the pair book's
    idle stretch and ends by its second 590, never near or during either archive's run (TZ-43's rule)."""
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

# ---- GitHub: TZ-27's client, every request held ------------------------------------------------------------


class Gh44(tz27.GitHub):
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


def release_text(doc, commit):
    name = "%s: L0's inputs - the reward book's days %s to %s and TZ-43's work files" % (
        doc["tag"], utc(FIRST_D0)[:10], utc(LAST_D0)[:10])
    body = ("Every file of /var/lib/btc-rewardbook/<D0>/ but its streams, for the %d UTC days %d to %d - each day's "
            "selections with their replies, its slot records and its reward polls, stored verbatim - one tar a day, "
            "rewardbook-inputs-<D0>.tar, its members named <D0>/<file>; and the %d files of TZ-43's fetch/ and days/, "
            "its set.json and its reading.json, as /root/btc-forensics/ holds them, each asset the bytes TZ-43's "
            "report names under its path in TZ-43's tree, tz43-<path> with - for /. %s lists every asset and every "
            "member by its bytes and SHA-256, and each TZ-43 file's path and forensic name. A file of stored replies "
            "is left out, and named there with its bytes and the line that withheld it, where a line of it carries a "
            "body the venue did not serve as a JSON document under status 200: an error page can carry the address "
            "it was served to. The streams are the rewardbook-streams-* Releases'. Every day from %d (2026-11-09) is "
            "reserved for L0's next gate and is not here. %d assets, %d bytes, made by research/%s at commit %s "
            "(TZ-44). Each asset's SHA-256 is its "
            "digest here." % (len(DAYS), FIRST_D0, LAST_D0, len(TZ43_FILES), MANIFEST, RESERVE_D0, doc["assets_n"],
                              doc["bytes_total"], PYFILE, commit))
    return name, body


def tag_reading(obj, peeled, commit):
    """G-TAG: the tag on origin is lightweight and names the instrument's commit. Pure."""
    return obj is not None and obj == commit and peeled is None

# ---- the pack: TZ-43's files checked, one tar a day, the manifest and the set ---------------------------------


def forensic_name(path):
    """The name TZ-43's reclaim gave a file of its tree in the forensic store."""
    return "tz43-work--" + path.replace("/", "--")


def asset_name(path):
    """The Release's name of a file of TZ-43's tree: one hyphen between parts, so the venue of the bytes keeps it."""
    return "tz43-" + path.replace("/", "-")


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


def literal_rows_missing(text, files=None):
    """The literals of TZ43_FILES not printed in TZ-43's report as its section 2.6 table prints them. Pure."""
    files = TZ43_FILES if files is None else files
    return [p for p, n, h in files if ("| `%s` | %d | `%s` |" % (p, n, h)) not in text]


def check_sources(root=None, files=None):
    """G-SOURCE: each of TZ-43's files in the forensic store, a regular file of the bytes and SHA-256 its report
    names."""
    root, files = FORENSICS if root is None else root, TZ43_FILES if files is None else files
    rows, bad = [], []
    for path, nbytes, sha in files:
        name = forensic_name(path)
        p = os.path.join(root, name)
        st = os.lstat(p)
        assert stat.S_ISREG(st.st_mode), "BLOCKED: %s is not a regular file" % p
        h = sha256_file(p)
        good = st.st_size == nbytes and h == sha
        out("G-SOURCE %s %d bytes sha256 %s %s" % (name, st.st_size, h, "equal" if good else "DIFFERS"))
        if not good:
            bad.append(name)
        rows.append({"asset": asset_name(path), "source": name, "path": path, "bytes": st.st_size, "sha256": h})
    assert not bad, "BLOCKED: G-SOURCE %d of %d differ from TZ-43's report: %s" % (len(bad), len(files), bad)
    return rows


def member_info(arcname, size, mtime):
    ti = tarfile.TarInfo(arcname)
    ti.size, ti.mtime, ti.mode, ti.type = size, mtime, 0o644, tarfile.REGTYPE
    ti.uid = ti.gid = 0
    ti.uname = ti.gname = ""
    return ti


def day_budget(member_bytes):
    """The seconds a day's unit is held for: UNIT_BASE_S, and its members' bytes at SCAN_RATE, rounded up. Pure."""
    return UNIT_BASE_S + -(-int(member_bytes) // SCAN_RATE)


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


def manifest_doc(commit, file_sha, days, sources, report_sha):
    return {"tag": TAG, "made_by": "research/" + PYFILE, "commit": commit, "file_sha256": file_sha, "store": RB_ROOT,
            "first_D0": FIRST_D0, "last_D0": LAST_D0, "reserve_from_D0": RESERVE_D0, "days": days,
            "tz43": {"report": TZ43_REPORT, "report_sha256": report_sha, "files": sources}}


def set_doc(days, sources, manifest_bytes, manifest_sha):
    """The Release's set, in upload order: the day archives, TZ-43's files, the manifest. Each entry's T and file
    place it under UPLOAD_ROOT for TZ-27's upload_set (store_path)."""
    out_t = os.path.relpath(OUT, UPLOAD_ROOT)
    src_t = os.path.relpath(FORENSICS, UPLOAD_ROOT)
    assets = [{"T": out_t, "file": d["archive"], "asset": d["archive"], "bytes": d["bytes"], "sha256": d["sha256"]}
              for d in days]
    assets += [{"T": src_t, "file": s["source"], "asset": s["asset"], "bytes": s["bytes"], "sha256": s["sha256"]}
               for s in sources]
    assets.append({"T": out_t, "file": MANIFEST, "asset": MANIFEST, "bytes": manifest_bytes, "sha256": manifest_sha})
    names = [x["asset"] for x in assets]
    assert len(set(names)) == len(names), "two assets of one name"
    return {"tag": TAG, "assets": assets, "assets_n": len(assets), "bytes_total": sum(x["bytes"] for x in assets)}


def read_set(st):
    p = st.get("pack")
    assert p, "no set: pack has not run"
    with open(SET_FILE, "rb") as fh:
        raw = fh.read()
    assert sha256_bytes(raw) == p["set_sha256"], "set.json is not the set pack wrote"
    return json.loads(raw), raw

# ---- the venue's geoblock: what may be printed of its reply ----------------------------------------------------


def geo_fields(doc):
    """What the report may print of the venue's reply: blocked, country and region, and the reply's key names - never
    the address it carries. Pure."""
    if not isinstance(doc, dict):
        return None
    return {"blocked": doc.get("blocked"), "country": doc.get("country"), "region": doc.get("region"),
            "keys": sorted(str(k) for k in doc)}

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


def ledger_records(path):
    with open(path, "rb") as fh:
        raw = fh.read()
    lines = raw.split(b"\n")
    tail = lines.pop()
    return raw, [json.loads(ln) for ln in lines if ln.strip()], tail


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


def mode_pack():
    """G-SOURCE, then G-PACK: the 34 sources as one held unit, each day as one, held for its members' bytes; the
    manifest and the set written once; a second run asserts all of it unchanged (DETERMINISM)."""
    floor_check()
    commit, up = git("rev-parse", "HEAD"), git("rev-parse", "@{u}")
    assert SHA40.fullmatch(commit) and commit == up, "BLOCKED: the branch head %s is not its upstream's %s" % (
        commit, up)
    file_sha = sha256_file(os.path.join(HERE, PYFILE))
    with open(os.path.join(PRIMARY, TZ43_REPORT), "rb") as fh:
        report = fh.read()
    missing = literal_rows_missing(report.decode("utf-8"))
    assert not missing, "BLOCKED: rows not in TZ-43's report: %s" % missing
    out("TZ-43's report %s, %d bytes, sha256 %s: the rows of its %d files found %d of %d" % (
        TZ43_REPORT, len(report), sha256_bytes(report), len(TZ43_FILES), len(TZ43_FILES) - len(missing),
        len(TZ43_FILES)))
    at, waited = hold(UNIT_BUDGET_S)
    t0 = time.time()
    sources = check_sources()
    out("G-SOURCE PASS: %d of %d equal to TZ-43's report, %d bytes; held %.1f s, from second %d, %.2f s" % (
        len(sources), len(TZ43_FILES), sum(s["bytes"] for s in sources), waited, int(at) % SLOT, time.time() - t0))
    os.makedirs(OUT, exist_ok=True)
    days, states, over = [], collections.Counter(), 0
    for d0 in DAYS:
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
    report_sha = sha256_bytes(report)
    mraw = tz27.json_bytes(manifest_doc(commit, file_sha, days, sources, report_sha))
    states[write_once(os.path.join(OUT, MANIFEST), mraw)] += 1
    doc = set_doc(days, sources, len(mraw), sha256_bytes(mraw))
    raw = tz27.json_bytes(doc)
    states[write_once(SET_FILE, raw)] += 1
    st = load_state()
    st["pack"] = {"commit": commit, "file_sha256": file_sha, "set_sha256": sha256_bytes(raw),
                  "manifest_sha256": sha256_bytes(mraw), "assets_n": doc["assets_n"], "bytes_total": doc["bytes_total"]}
    save_state(st)
    for x in doc["assets"]:
        out("S %s %d %s" % (x["asset"], x["bytes"], x["sha256"]))
    members, scanned = sum(d["members_n"] for d in days), sum(d["scanned_n"] for d in days)
    out("G-PACK PASS: %d days of %d, %d members, %d bytes of members, %d bytes of archives; withheld %d files of "
        "replies, %d bytes; streams %d and other names %d never opened; %d assets, %d bytes; days over their budget "
        "%d; outputs %s" % (
            len(days), len(DAYS), members, sum(d["member_bytes"] for d in days), sum(d["bytes"] for d in days),
            sum(d["withheld_n"] for d in days), sum(d["withheld_bytes"] for d in days),
            sum(d["counts"]["stream"] for d in days), sum(d["counts"]["other"] for d in days), doc["assets_n"],
            doc["bytes_total"], over, dict(sorted(states.items()))))
    assert COUNTS["reward book opens"] == members + scanned and COUNTS["reward book listings"] == len(DAYS), \
        "BLOCKED: the store opened %d times and listed %d, for %d members, %d files scanned and %d days" % (
            COUNTS["reward book opens"], COUNTS["reward book listings"], members, scanned, len(DAYS))
    out("G-RESERVE PASS: the store opened %d times - once a member kept, %d, and once a file of replies scanned, %d "
        "- and listed %d times, one a day; no other open or listing under %s" % (
            COUNTS["reward book opens"], members, scanned, COUNTS["reward book listings"], RB_ROOT))
    if states["unchanged"] == len(DAYS) + 2:
        out("DETERMINISM PASS: %d of %d outputs unchanged" % (states["unchanged"], len(DAYS) + 2))


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
    gh = Gh44(token=tok, record=transfer_logger(), commit=commit)
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
    anon = Gh44(token=None, record=transfer_logger())
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


def mode_geoblock():
    """One read of the venue's geoblock endpoint from the host, printed and gating nothing; the address its reply
    carries is never printed or written."""
    try:
        addrs = sorted({ai[4][0] for ai in socket.getaddrinfo(GEO_HOST, 443, type=socket.SOCK_STREAM)})
        out("DNS %s: %s" % (GEO_HOST, addrs))
    except OSError as exc:
        out("DNS %s: %s %s" % (GEO_HOST, type(exc).__name__, getattr(exc, "errno", None)))
    req = urllib.request.Request(GEO_URL, headers=dict(GEO_HEADERS), method="GET")
    status, body, where = None, b"", None
    t0 = time.time()
    try:
        with tz27.opener(follow=False).open(req, timeout=GEO_TIMEOUT_S) as resp:
            status, body = int(resp.status), resp.read(GEO_READ_MAX)
    except urllib.error.HTTPError as exc:
        status = int(exc.code)
        loc = exc.headers.get("Location") if exc.headers is not None else None
        where = urllib.parse.urlsplit(loc).hostname if loc else None
    except Exception as exc:     # the read gates nothing: every failure is printed by its kind alone
        out("GEOBLOCK no reply: %s" % type(exc).__name__)
    try:
        doc = json.loads(body) if body else None
    except ValueError:
        doc = None
    f = geo_fields(doc)
    out("GEOBLOCK READ: %s, status %s%s, %d bytes in %.2f s; blocked %r, country %r, region %r; reply keys %s" % (
        GEO_URL, status, (", redirect to host %s" % where) if where else "", len(body), time.time() - t0,
        f and f["blocked"], f and f["country"], f and f["region"], f and f["keys"]))


def report_tokens():
    tokens = set()
    for name in sorted(os.listdir(REPORTS)):
        if name.endswith(".md"):
            with open(os.path.join(REPORTS, name), encoding="utf-8", errors="replace") as fh:
                tokens.update(TOKEN.findall(fh.read()))
    return tokens


def by_name(tree, rel):
    return tree == WORK and (rel == "state.json" or rel.startswith("logs/"))


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
    before = sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    out("reclaim: %d report tokens; forensic store holds %d files" % (len(tokens), before))
    considered = named = kept = copied = held = 0
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
    out("RECLAIM PASS: %d files considered, %d named by a report, %d kept by name, %d copied, %d already held; "
        "forensic store %d -> %d files" % (considered, named, kept, copied, held, before, after))


def main(argv):
    if not argv:
        sys.exit("usage: %s MODE [ARG...]" % PYFILE)
    mode, rest = argv[0], argv[1:]
    assert os.getcwd() == WORK, "run from %s, not %s" % (WORK, os.getcwd())
    MODE[0] = mode
    tz27.MODE[0] = mode
    table = {"fingerprint": mode_fingerprint, "number": mode_number, "selftest": mode_selftest, "still": mode_still,
             "pack": mode_pack, "upload": mode_upload, "verify": mode_verify, "geoblock": mode_geoblock}
    try:
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

# ---- the self-test: literals, temporary trees under the work tree and a loopback GitHub -----------------------


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
    ok(len(DAYS) == 12 and DAYS[0] == FIRST_D0 and DAYS[-1] == LAST_D0 and RESERVE_D0 == LAST_D0 + DAY and
       utc(FIRST_D0) == "2026-10-28T00:00:00Z" and utc(LAST_D0) == "2026-11-08T00:00:00Z" and
       utc(RESERVE_D0) == "2026-11-09T00:00:00Z" and all(d % DAY == 0 for d in DAYS),
       "twelve UTC days, 2026-10-28 to 2026-11-08, the last the day before the reserve's first, 2026-11-09")
    paths = [p for p, _n, _h in TZ43_FILES]
    want = sorted(["fetch/%d.json" % d for d in TZ43_MEMBERS] + ["fetch/%d.polls.jsonl" % d for d in TZ43_MEMBERS] +
                  ["days/%d.json" % d for d in TZ43_MEMBERS] + ["days/%d.slots.txt" % d for d in TZ43_MEMBERS] +
                  ["set.json", "reading.json"])
    ok(len(TZ43_FILES) == 34 and sorted(paths) == want and len(set(paths)) == 34 and
       all(SHA_RE.fullmatch(h) and n > 0 for _p, n, h in TZ43_FILES) and set(TZ43_MEMBERS) <= set(DAYS) and
       sum(n for _p, n, _h in TZ43_FILES) == 42169992,
       "TZ-43's 34 files: fetch/ and days/ of its 8 member days, set.json and reading.json, 42,169,992 bytes")
    ok(forensic_name("fetch/1793404800.json") == "tz43-work--fetch--1793404800.json" and
       forensic_name("set.json") == "tz43-work--set.json" and len({forensic_name(p) for p in paths}) == 34 and
       asset_name("fetch/1793404800.polls.jsonl") == "tz43-fetch-1793404800.polls.jsonl" and
       asset_name("reading.json") == "tz43-reading.json" and len({asset_name(p) for p in paths}) == 34 and
       all("--" not in asset_name(p) and re.fullmatch(r"[a-z0-9][a-z0-9.-]*", asset_name(p)) for p in paths),
       "each file's name in the forensic store, as TZ-43's reclaim made it, and in the Release, one hyphen apart")
    ok(UA == "btc-5m-twap-tz44" and GEO_HEADERS == {"User-Agent": UA, "Accept": "application/json"} and
       tz27.UA == "btc-5m-twap-tz27" and tz27.CONTENT_TYPE == "application/octet-stream" and tz27.WORK[0] == WORK,
       "the geoblock read under this TZ's agent; GitHub's under TZ-27's, every asset octet-stream; TZ-27's work tree")
    lo = MEM_FLOOR - 1
    ok(MEM_FLOOR == 2 * -(-41000000 * 58953728 // 49168384) == 98319394 and DISK_FLOOR == 7400000000 and
       DISK_GATE == 7800000000, "the floors: memory 98,319,394 bytes, disk 7,400,000,000 after a write and "
       "7,800,000,000 at a mode's start")
    ok(memory_gate([MEM_FLOOR]) == (True, MEM_FLOOR) and memory_gate([lo, lo, MEM_FLOOR]) == (True, MEM_FLOOR) and
       memory_gate([lo] * 5) == (False, lo) and fails(lambda: memory_gate([MEM_FLOOR, lo])) and
       fails(lambda: memory_gate([lo] * 6)),
       "the memory gate: a read at the floor or above passes; below it the next read decides, five reads at most")
    reads, slept = iter([lo, lo - 7, MEM_FLOOR + 3]), []
    floor_check(read=lambda: next(reads), sleep=slept.append, freef=lambda: DISK_GATE)
    reads2, slept2 = iter([lo] * 5), []
    ok(slept == [MEM_RETRY_S] * 2 and
       fails(lambda: floor_check(read=lambda: next(reads2), sleep=slept2.append, freef=lambda: DISK_GATE)) and
       slept2 == [MEM_RETRY_S] * 4 and
       fails(lambda: floor_check(read=lambda: MEM_FLOOR, sleep=slept2.append, freef=lambda: DISK_GATE - 1)),
       "floor_check reads again every 60 s while below its floor and BLOCKS after five; it BLOCKS below the disk gate")
    # the hook
    d1, dr = RB_ROOT + "/%d" % FIRST_D0, RB_ROOT + "/%d" % RESERVE_D0
    ok(policy("pack", "os.listdir", (d1,)) is None and
       policy("pack", "os.listdir", (RB_ROOT + "/%d" % LAST_D0,)) is None and
       policy("pack", "os.listdir", (dr,)) is not None and policy("pack", "os.listdir", (RB_ROOT,)) is not None
       and policy("upload", "os.listdir", (d1,)) is not None and policy("pack", "os.scandir", (d1,)) is None,
       "pack alone lists a day directory, of the twelve only: not the store's root, not a day from 2026-11-09")
    ok(policy("pack", "open", (d1 + "/select.0.json", "rb", 0)) is None and
       policy("pack", "open", (d1 + "/select.1.replies.jsonl.gz", "rb", 0)) is None and
       policy("pack", "open", (d1 + "/1793149200.0.slot.json", "rb", 0)) is None and
       policy("pack", "open", (d1 + "/1793149200.1.rewards.jsonl.gz", "rb", 0)) is None and
       policy("pack", "open", (d1 + "/1793149200.0.stream.jsonl.gz", "rb", 0)) is not None and
       policy("pack", "open", (dr + "/select.0.json", "rb", 0)) is not None and
       policy("pack", "open", (RB_ROOT + "/runtime.jsonl", "rb", 0)) is not None and
       policy("pack", "open", (RB_ROOT + "/service.log", "rb", 0)) is not None and
       policy("pack", "open", (d1 + "/select.0.json", "wb", 0)) is not None and
       policy("verify", "open", (d1 + "/select.0.json", "rb", 0)) is not None,
       "pack alone reads a day's selections, slot records and polls; never a stream, a reserved day, the root or a "
       "write")
    ok(policy("upload", "urllib.Request", ("https://api.github.com/repos/x",)) is None and
       policy("upload", "urllib.Request", ("https://uploads.github.com/repos/x",)) is None and
       policy("upload", "urllib.Request", ("https://github.com/x",)) is not None and
       policy("verify", "urllib.Request", ("https://github.com/x/releases/download/t/a",)) is None and
       policy("verify", "urllib.Request", ("https://release-assets.githubusercontent.com/x",)) is None and
       policy("verify", "urllib.Request", ("https://objects.githubusercontent.com/x",)) is None and
       policy("verify", "urllib.Request", ("https://uploads.github.com/x",)) is not None and
       policy("geoblock", "urllib.Request", (GEO_URL,)) is None and
       policy("geoblock", "urllib.Request", ("https://www.polymarket.com/api/geoblock",)) is not None and
       policy("geoblock", "urllib.Request", ("https://clob.polymarket.com/x",)) is not None and
       policy("pack", "urllib.Request", ("https://api.github.com/x",)) is not None and
       policy("still", "urllib.Request", ("https://api.github.com/x",)) is not None,
       "requests: upload to GitHub's API and upload host, verify to the API and the download hosts, geoblock to "
       "polymarket.com alone; no other mode reaches the network")
    ok(policy("pack", "subprocess.Popen", ("git", ["git"], None, None)) is None and
       policy("still", "subprocess.Popen", ("/usr/bin/systemctl", ["systemctl"], None, None)) is None and
       policy("upload", "subprocess.Popen", ("/usr/bin/gh", ["gh"], None, None)) is None and
       policy("verify", "subprocess.Popen", ("/usr/bin/gh", ["gh"], None, None)) is not None and
       policy("pack", "subprocess.Popen", ("/usr/bin/curl", ["curl"], None, None)) is not None,
       "processes: git, systemctl and stat; gh in upload alone, for TZ-27's credential")
    ok(policy("reclaim", "open", (FORENSICS + "/x", "xb", 0)) is None and
       policy("reclaim", "open", (FORENSICS + "/x", "wb", 0)) is not None and
       policy("pack", "open", (FORENSICS + "/x", "xb", 0)) is not None and
       policy("pack", "open", (FORENSICS + "/tz43-work--set.json", "rb", 0)) is None and
       policy("pack", "open", ("/root/elsewhere", "wb", 0)) is not None and
       policy("pack", "open", (OUT + "/x.part", "wb", 0)) is None and
       policy("still", "open", (PB_LEDGER, "rb", 0)) is None and
       policy("pack", "open", (PB_LEDGER, "rb", 0)) is not None and
       policy("still", "open", (RB_ARCHIVE + "/ledger.jsonl", "rb", 0)) is not None and
       policy("pack", "open", (RECORDER + "/runtime.jsonl", "rb", 0)) is not None and
       policy("pack", "open", (ADVISOR_ETC + "/token", "rb", 0)) is not None and
       policy("pack", "os.listdir", (PAIRBOOK,)) is not None,
       "writes: the work tree, and the forensic store by reclaim's exclusive create; the captures and the advisor shut")
    # the clock
    base = 1794400000 - 1794400000 % DAY + 10 * 3600     # a 10:00 UTC
    idle = {"pairbook": "inactive", "rewardbook": "inactive"}
    ok(quiet(base + 14, 60, lambda: idle) is not None and quiet(base + 15, 60, lambda: idle) is None and
       quiet(base + 530, 60, lambda: idle) is None and quiet(base + 531, 60, lambda: idle) is not None and
       quiet(base - 10 * 3600 + 5420, 5, lambda: idle) is not None and
       quiet(base - 10 * 3600 + 5481, 5, lambda: idle) is None and
       quiet(base - 10 * 3600 + 10850, 5, lambda: idle) is not None and
       quiet(base - 10 * 3600 + 10881, 5, lambda: idle) is None and
       quiet(base + 15, 5, lambda: {"pairbook": "active", "rewardbook": "inactive"}) is not None and
       budget_s(0) == 5 and budget_s(2000000) == 6 and budget_s(2000001) == 7 and budget_s(200000000) == 105,
       "a unit starts at second 15 of a window or later and ends by 590, away from both calendar runs and from a "
       "running archive; its budget 5 s and its bytes at 2,000,000 a second")
    clock = [base + 600.0]
    t, waited = hold(5, clock=lambda: clock[0], sleep=lambda s: clock.__setitem__(0, clock[0] + s),
                     state_of=lambda: idle)
    ok(int(t) % SLOT == 15 and round(waited) == 315 and
       fails(lambda: hold(5, clock=lambda: clock[0], sleep=lambda s: clock.__setitem__(0, clock[0] + s),
                          state_of=lambda: {"pairbook": "active", "rewardbook": "inactive"})),
       "hold waits for the next idle stretch, and BLOCKS after 7,200 s of a running archive")
    # the readings
    ok(number_reading([OWN_TZ, "CryptoTZ/TZ-43-l0-our-quote.md"], OWN_TZ)[0] and
       not number_reading([OWN_TZ, "CryptoTZ/TZ-44-other.md"], OWN_TZ)[0] and
       not number_reading([OWN_TZ, "CryptoReports/TZ-44-l0-inputs-release-report.md"], OWN_TZ)[0] and
       not number_reading([], OWN_TZ)[0], "NUMBER: this TZ's file alone of its number, and no report of it")
    u = {"MainPID": "5", "NRestarts": "1", "ActiveState": "active"}
    v = {"MainPID": "9", "NRestarts": "2", "ActiveState": "active"}
    bef = {"recorder": u, "pairbook": u, "rewardbook": u, "advisor": u}
    aft = dict(bef, pairbook=v)
    ok(still_reading(bef, dict(bef), []) == (True, "unchanged") and
       still_reading(bef, aft, [{"stopped": "5", "NRestarts": "2", "pid": "9"}])[0] and
       not still_reading(bef, aft, [])[0] and not still_reading(bef, dict(bef, recorder=v), [])[0] and
       not still_reading(bef, aft, [{"stopped": "4", "NRestarts": "2", "pid": "9"}])[0],
       "G-STILL: unchanged, or the pair book moved by its archive's own restarts alone")
    t0_ = 1794391200
    rec = lambda a, b: {"start_ns": int(a * 1e9), "end_ns": int(b * 1e9), "waited_s": 1.5}
    ok(transfer_summary([rec(t0_ + 15, t0_ + 20), rec(t0_ + 14, t0_ + 20), rec(t0_ + 580, t0_ + 591),
                         rec(t0_ + 580, t0_ + 905)]) == (4, 1, 2, 6.0),
       "a transfer's place: started at second 15 to 590 of its window, ended in it by 590")
    ok(tag_reading("a" * 40, None, "a" * 40) and not tag_reading("a" * 40, "b" * 40, "a" * 40) and
       not tag_reading("b" * 40, None, "a" * 40) and not tag_reading(None, None, "a" * 40),
       "G-TAG: a lightweight tag at the instrument's commit")
    gf = geo_fields({"blocked": True, "ip": "192.0.2.7", "country": "PL", "region": "14"})
    ok(gf == {"blocked": True, "country": "PL", "region": "14", "keys": ["blocked", "country", "ip", "region"]} and
       "192.0.2.7" not in json.dumps(gf) and geo_fields(None) is None and geo_fields([1]) is None,
       "the geoblock reply: blocked, country and region printed, the address never")
    ok(reclaimable(WORK) and not reclaimable("/tmp") and not reclaimable("/root/tz43-work") and
       not reclaimable("/tmp/x/" + "0" * 8 + "-0000-0000-0000-" + "0" * 12),
       "reclaim: this TZ's tree, or a UUID directory beside a btc-5m-twap session's, and nothing else")
    # the store's names
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
    txt = "\n".join("| `%s` | %d | `%s` |" % row for row in TZ43_FILES[:33])
    ok(literal_rows_missing(txt) == [TZ43_FILES[33][0]] and literal_rows_missing(txt + "\n| `set.json` | 6175 | `%s` |"
                                                                                % TZ43_FILES[33][2]) == [],
       "each literal is found only as TZ-43's report prints its row")
    # a synthetic store: one day, its members, a stream and a stray name
    store, outd, outd2 = os.path.join(tmp, "store"), os.path.join(tmp, "out"), os.path.join(tmp, "out2")
    for p in (outd, outd2):
        os.makedirs(p)
    ddir = os.path.join(store, str(d0))
    os.makedirs(ddir)
    def gz_lines(recs):
        return gzip.compress("".join(json.dumps(r) + "\n" for r in recs).encode("utf-8"), mtime=0)

    page = "<html><span id=cf-footer-ip>203.0.113.7</span></html>"
    served = [{"status": 200, "raw": json.dumps({"data": [{"condition_id": "0x01"}]})}, {"status": None, "raw": ""},
              {"status": 200, "raw": "[]"}, {"status": 503, "raw": None}]
    ok(all(body_reason(r) is None for r in served) and body_reason({"status": 200}) is None and
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
    for k, v in list(blobs.items()) + list(held_back.items()) + list(others.items()):
        with open(os.path.join(ddir, k), "wb") as fh:
            fh.write(v)
    why = {k: withhold_reason(os.path.join(ddir, k)) for k in sorted(held_back)}
    ok(all(withhold_reason(os.path.join(ddir, k)) is None for k in blobs if k.endswith(SCANNED)) and
       [why[k] for k in sorted(held_back)] == ["line 5: a body under status 502",
                                                "line 1: a status-200 body that is not JSON",
                                                "not a whole gzip file: EOFError",
                                                "not a whole gzip file: BadGzipFile"] and
       not any("203.0.113.7" in w or "cf-footer-ip" in w for w in why.values()),
       "a file of replies is withheld by its first line that carries another body, or where it is no whole gzip file, "
       "and the reason names a line's number, never its content")
    ok(day_budget(0) == UNIT_BASE_S == 30 and day_budget(1) == 31 and day_budget(16300000) == 63 and
       day_budget(DAY_MAX_BYTES) == 430 <= IDLE[1] - IDLE[0] and SCAN_RATE == 500000,
       "a day's unit is held for 30 s and its members' bytes at 500,000 a second, 430 s at the day's bound")
    e1, s1 = pack_day(store, d0, outd, freef=lambda: DISK_FLOOR + 10 ** 7)
    e2, s2 = pack_day(store, d0, outd2, freef=lambda: DISK_FLOOR + 10 ** 7)
    e3, s3 = pack_day(store, d0, outd, freef=lambda: DISK_FLOOR + 10 ** 7)
    with open(os.path.join(outd, ARCHIVE_FMT % d0), "rb") as fh:
        tar_bytes = fh.read()
    with tarfile.open(os.path.join(outd, ARCHIVE_FMT % d0)) as tf:
        got = {m.name: (m.mtime, m.uid, m.gid, m.mode, m.isreg(), tf.extractfile(m).read()) for m in tf.getmembers()}
    ok(s1 == s2 == "wrote" and s3 == "unchanged" and e1["sha256"] == e2["sha256"] == e3["sha256"] and
       e1 == e3 and len(tar_bytes) == e1["bytes"] and sha256_bytes(tar_bytes) == e1["sha256"] and
       not os.path.exists(os.path.join(outd, ARCHIVE_FMT % d0 + ".part")),
       "a day's archive: the same bytes from two trees and from a second run, written once, no part left")
    ok(sorted(got) == sorted("%d/%s" % (d0, k) for k in blobs) and
       all(got["%d/%s" % (d0, k)][5] == v for k, v in blobs.items()) and
       all(g[:5] == (d0, 0, 0, 0o644, True) for g in got.values()) and
       [r["name"] for r in e1["members"]] == sorted("%d/%s" % (d0, k) for k in blobs) and
       all(r["sha256"] == sha256_bytes(blobs[r["name"].split("/", 1)[1]]) and
           r["bytes"] == len(blobs[r["name"].split("/", 1)[1]]) for r in e1["members"]),
       "every member stored verbatim under <D0>/<name>, in name order, its mtime D0, mode 644, owner 0, and its "
       "bytes and SHA-256 in the manifest's entry")
    ok(b"STREAM-BYTES" not in tar_bytes and b"OTHER-BYTES" not in tar_bytes and
       e1["counts"] == {"select": 3, "slot": 2, "rewards": 5, "stream": 1, "other": 1} and
       sorted((x["kind"], x["name"], x["bytes"]) for x in e1["excluded"]) ==
       [("other", "notes.txt", 11), ("stream", "%d.0.stream.jsonl.gz" % (d0 + 41400), 1200)],
       "the stream and the stray name are listed by their bytes and never stored")
    ok(e1["members_n"] == len(blobs) == 6 and e1["scanned_n"] == 7 and e1["withheld_n"] == 4 and
       e1["member_bytes"] == sum(len(v) for v in blobs.values()) and
       e1["withheld_bytes"] == sum(len(v) for v in held_back.values()) and
       [(w["name"], w["bytes"], w["reason"]) for w in e1["withheld"]] ==
       [(k, len(held_back[k]), why[k]) for k in sorted(held_back)] and
       not any(("%d/%s" % (d0, k)) in got for k in held_back) and
       not any(v in tar_bytes for v in held_back.values()),
       "a withheld file is in no archive: the entry names it by its bytes and its reason, and counts the files scanned")
    ok(fails(lambda: pack_day(store, d0, outd2, freef=lambda: DISK_FLOOR)) and
       fails(lambda: pack_day(store, d0 + DAY, outd2, freef=lambda: DISK_FLOOR + 10 ** 7)),
       "a day BLOCKS where its archive would leave free space under the floor, and where its directory is absent")
    # the sources and the set, on synthetic files
    srcd = os.path.join(tmp, "forensics")
    os.makedirs(srcd)
    fake = []
    for i, p in enumerate(("fetch/1793404800.json", "set.json")):
        data = ("synthetic %d\n" % i).encode("utf-8")
        with open(os.path.join(srcd, forensic_name(p)), "wb") as fh:
            fh.write(data)
        fake.append((p, len(data), sha256_bytes(data)))
    rows = check_sources(srcd, tuple(fake))
    with open(os.path.join(srcd, forensic_name("set.json")), "ab") as fh:
        fh.write(b"!")
    ok([r["asset"] for r in rows] == ["tz43-fetch-1793404800.json", "tz43-set.json"] and
       [r["source"] for r in rows] == ["tz43-work--fetch--1793404800.json", "tz43-work--set.json"] and
       fails(lambda: check_sources(srcd, tuple(fake))),
       "G-SOURCE: each file equal to its row, and one byte more is a BLOCK")
    sdoc = set_doc([e1], rows, 99, "f" * 64)
    ok(sdoc["assets_n"] == 4 and [x["asset"] for x in sdoc["assets"]] == [ARCHIVE_FMT % d0,
                                                                         "tz43-fetch-1793404800.json",
                                                                         "tz43-set.json", MANIFEST] and
       tz27.store_path(UPLOAD_ROOT, sdoc["assets"][0]) == os.path.join(OUT, ARCHIVE_FMT % d0) and
       tz27.store_path(UPLOAD_ROOT, sdoc["assets"][1]) == os.path.join(FORENSICS, "tz43-work--fetch--1793404800.json")
       and sdoc["bytes_total"] == e1["bytes"] + rows[0]["bytes"] + rows[1]["bytes"] + 99,
       "the set: the archives, TZ-43's files from the forensic store and the manifest, each found by TZ-27's "
       "store_path")
    mdoc = manifest_doc("c" * 40, "f" * 64, [e1], rows, "e" * 64)
    ok(tz27.json_bytes(mdoc) == tz27.json_bytes(manifest_doc("c" * 40, "f" * 64, [e1], rows, "e" * 64)) and
       mdoc["reserve_from_D0"] == RESERVE_D0 and mdoc["tz43"]["report"] == TZ43_REPORT,
       "the manifest: the same bytes from the same inputs")
    # the loopback GitHub: TZ-27's own stand-in, our client, our set
    for k in [k for k in list(os.environ) if k.lower() in ("http_proxy", "https_proxy", "all_proxy", "no_proxy")]:
        del os.environ[k]
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
        files = {"one.tar": os.urandom(3000), "tz43-set.json": b'{"x": 1}\n', MANIFEST: b"{}\n"}
        assets = []
        for name, data in files.items():
            with open(os.path.join(root, "a", name), "wb") as fh:
                fh.write(data)
            assets.append({"T": "a", "file": name, "asset": name, "bytes": len(data), "sha256": sha256_bytes(data)})
        doc = {"tag": TAG, "assets": assets, "assets_n": 3, "bytes_total": sum(x["bytes"] for x in assets)}
        trs, logs = [], []
        nowait = lambda budget: (time.time(), 0.0)
        gh = Gh44(token=tok, record=trs.append, held=nowait, commit="c" * 40, api=lb, uploads=lb, web=lb)
        gh.gap_s = 0.0
        rel = gh.create_release(TAG, *release_text(doc, "c" * 40))
        sent, held_n = tz27.upload_set(gh, rel, doc, root, logs.append, wait_min=0)
        anon = Gh44(token=None, record=trs.append, held=nowait, api=lb, uploads=lb, web=lb)
        anon.sizes = {x["asset"]: x["bytes"] for x in assets}
        rel2, vrows, missing, extra = tz27.verify_release(anon, TAG, doc)
        checks = tz27.release_reading(rel2, TAG, vrows, missing, extra)
        ok(bodies and bodies[-1]["tag_name"] == TAG and bodies[-1]["target_commitish"] == "c" * 40 and
           bodies[-1]["draft"] is False and bodies[-1]["make_latest"] == "false" and sent == 3 and held_n == 0 and
           all(checks.values()) and len(vrows) == 3 and all(r["download_ok"] for r in vrows),
           "loopback: the Release on the tag at the commit, three assets sent, and every one proved by the API's "
           "record and a full download with no token")
        ok(all(h[2] == tz27.UA for h in Fake.hits) and
           all(h[3] is None for h in Fake.hits if "/releases/download/" in h[1] or h[1].startswith("/blob/")) and
           len([t for t in trs if t["kind"] == "upload"]) == 3 and
           len([t for t in trs if t["kind"] == "download"]) == 3 and all(t["ok"] for t in trs),
           "every request under TZ-27's agent, every read with no token, every transfer held and recorded")
        sent2, held2 = tz27.upload_set(gh, rel, doc, root, logs.append, wait_min=0)
        aid = [a for a, x in Fake.assets.items() if x["name"] == "one.tar"][0]
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
    ok(not os.path.exists(tmp) and not REFUSED, "the temporary tree removed; no open, listing, request or process "
                                               "refused by this file's hook")
    out("SELFTEST PASS: %d checks" % n[0])


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except GuardError as exc:
        out("refused: %s" % exc)
        raise
```
