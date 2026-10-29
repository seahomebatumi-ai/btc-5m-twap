# TZ-34 — the reward book's archive on a timer: its closed slots' streams to a Release, once a day, unattended

**Canonical filename:** `TZ-34-rewardbook-archive-timer.md`. The committed file takes this name and no other.

**Executor model: Claude Opus 5.5.** A unit that removes a live capture's files and holds a credential is deployed
beside that capture, and its first run is proved.

**Required System Map revision:** `2026-10-28-a`.

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

**When:** after the upload that carries this TZ; revision `2026-10-28-a` is on `main` already. **The session starts
between 07:00 and 15:00 UTC, on 2026-10-30 at the latest:** at the reward book's measured rate its free space first
falls below the stream floor at about 20:00 UTC on 2026-10-30 [modelled, map §2.6], and from then its slots stream
nothing until their files leave the host — the first run must have moved them before. B-ENABLE waits in its own text
for 07:15:00 to 19:00:00 UTC (§3.6). About three hours of wall clock (§6), most of it waiting for the first run and the
slot after it. **The Boss is needed at the VPS for one block**, B-ENABLE, which carries the credential's proof
(§3.6), and for any block the session's classifier refuses (§3).

**What this TZ is.** TZ-33 put L0's capture on the host: the reward book streams each UTC day's 150 reward markets into
`/var/lib/btc-rewardbook/`, `1,016,070,120` bytes of stream files a day at its first measured rate (map §2.6). No stream
opens for a slot below `7,300,000,000` bytes free or once the stream files sum to `4,000,000,000` — both read again at
every slot — and at that rate the floor binds first, about 20:00 UTC on 2026-10-30, and the cap about 10:00 UTC on
2026-11-01 [modelled, map §2.6]. **This TZ deploys a systemd timer that moves the closed slots' stream files to a
Release once a day**, as TZ-28's moves the pair book's: the set as of the run's start, each file uploaded to that run's
own Release, proved by the Release's digest and a full anonymous download, hashed again and removed — through TZ-27's
and TZ-28's own functions, which its instrument loads byte for byte, every request held to the pair book's idle
stretch as TZ-28 holds its own. **Two things are new.** Each removal too is held to the idle stretch, and to an instant
at which the reward book is not about to sum its store's files, because a file removed under that sum costs a slot or
stops the process (§1). And nothing is restarted, because the reward book reads its sum live. It proves the deployment
on the timer's own first run, fired 1,800 s after the timer starts, and measures nothing (CANON hard rule 11). One
instrument, `research/tz34-rewardbook-archive-timer.py`, and two units, `deploy/systemd/btc-rewardbook-archive.service`
and `deploy/systemd/btc-rewardbook-archive.timer`: Appendix A.

---

## 0. Gates

### 0.0 The work tree, first

After contract §1 steps 1 and 2, and before anything else:

```
mkdir /root/tz34-work /root/tz34-work/logs; echo "exit=$?"
```

`exit=0` proves neither existed; anything else is BLOCKED. **From here every command's output goes to
`/root/tz34-work/logs/`, one file per step, §0's included**, and nothing to the session's scratchpad. The one exception
is B-RECLAIM-OWN, §9.

### 0.1 The instrument and the units, staged

Extract Appendix A from this TZ as the primary checkout carries it after contract §1's pull, with this script,
verbatim, its one argument the destination:

```
/root/tz04a-env/venv/bin/python -B - /root/tz34-work/stage <<'EOF'
import hashlib, os, sys
SRC = "/root/btc-5m-twap/CryptoTZ/TZ-34-rewardbook-archive-timer.md"
DEST = sys.argv[1]
WANT = {
    "research/tz34-rewardbook-archive-timer.py": "1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72",
    "deploy/systemd/btc-rewardbook-archive.service": "a9abb1f092b3fb8359d37ea88df00dca8557d0f0482d04c12f0fbdd32601e33f",
    "deploy/systemd/btc-rewardbook-archive.timer": "bf5af0252c420d8db1579b82e5da21472cdb6bc871fa8035ecf6f1edc9720a0f",
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
| `research/tz34-rewardbook-archive-timer.py` | 1,791 | 99,388 | `1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72` |
| `deploy/systemd/btc-rewardbook-archive.service` | 17 | 810 | `a9abb1f092b3fb8359d37ea88df00dca8557d0f0482d04c12f0fbdd32601e33f` |
| `deploy/systemd/btc-rewardbook-archive.timer` | 13 | 428 | `bf5af0252c420d8db1579b82e5da21472cdb6bc871fa8035ecf6f1edc9720a0f` |

Then the instrument's two dependencies beside it, TZ-28's and TZ-27's files as `main` carries them:

```
install -m 0644 /root/btc-5m-twap/research/tz28-pairbook-archive-timer.py /root/btc-5m-twap/research/tz27-pairbook-archive.py /root/tz34-work/stage/research/; echo "exit=$?"
sha256sum /root/tz34-work/stage/research/tz28-pairbook-archive-timer.py /root/tz34-work/stage/research/tz27-pairbook-archive.py
```

which must print `46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4` and
`2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673` — map §0's rows; the instrument asserts both again
each time it loads them (Appendix A lines 67 to 83). A failed assert or another hash is BLOCKED. The staged copy runs
one mode only, §0.2's `fingerprint`, and is written **`I0`**: `nice -n 19 /root/tz04a-env/venv/bin/python -B
/root/tz34-work/stage/research/tz34-rewardbook-archive-timer.py`, run from `/root/tz34-work` — every mode but `run`
asserts that its current directory is a work tree `/root/tzNN-work` (Appendix A line 1759).

### 0.2 Fingerprint

`I0 fingerprint` performs contract §1 steps 3 and 4 inside the instrument and asserts them, against `SYSTEM-MAP.md` and
the files of its §0 table in the primary checkout `/root/btc-5m-twap`: revision `2026-10-28-a`; the six anchors; `A2`,
`A4`, `A5` and `A6` re-derived as the first 12 hex characters of those files' SHA-256; the table's **46** rows, each
printed in lines, bytes and SHA-256 — **43** `frozen` rows asserted equal to the map, **2** `tracked` and **1**
`reported`; and the map's own lines, bytes and SHA-256 (Appendix A lines 830 to 858). It prints `FINGERPRINT PASS` or
stops at the first mismatch, which is BLOCKED.

### 0.3 Host gate

From `/root/btc-5m-twap`, with `S` first set to the scratchpad directory the session's system prompt names, output
verbatim into `logs/03-host-gate.log`:

```
date -u; date -u +%s
nproc; grep -E '^(MemTotal|MemAvailable|SwapTotal|SwapFree):' /proc/meminfo
uptime -s; journalctl --list-boots --no-pager
df -B1 --output=source,size,avail /var/lib/btc-recorder
find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
grep -c e3975b5da44c5328adf3bf3914634cd878842c73 /var/lib/btc-recorder/runtime.jsonl
/root/tz04a-env/venv/bin/python -B -c 'import sys; print(sys.version.split()[0])'
TZ=UTC systemctl show btc-recorder.service btc-pairbook.service btc-pairbook-archive.service btc-pairbook-archive.timer btc-rewardbook.service btc-chainbook.service crypto-deploy.service crypto-announce.service -p Id -p MainPID -p NRestarts -p ActiveState -p SubState -p UnitFileState -p ActiveEnterTimestamp -p Result
TZ=UTC systemctl list-timers btc-pairbook-archive.timer apt-daily-upgrade.timer apt-daily.timer --all --no-pager
for u in btc-recorder.service btc-pairbook.service btc-pairbook-archive.service btc-pairbook-archive.timer btc-rewardbook.service; do cmp deploy/systemd/$u /etc/systemd/system/$u; echo "$u cmp exit=$?"; done
cat /root/btc-rewardbook-svc/commit.txt /root/btc-pairbook-archive-svc/commit.txt
sha256sum /root/btc-rewardbook-svc/tz33-reward-book-capture.py /root/btc-pairbook-archive-svc/tz28-pairbook-archive-timer.py /root/btc-pairbook-archive-svc/tz27-pairbook-archive.py
for d in /root/btc-rewardbook-archive-svc /var/lib/btc-rewardbook-archive /etc/systemd/system/btc-rewardbook-archive.service /etc/systemd/system/btc-rewardbook-archive.timer; do test -e "$d"; echo "$d exit=$?"; done
for d in /root/tz33-work /root/tz18a-svc /root/btc-recorder-svc /root/btc-pairbook-svc /root/btc-pairbook-archive-svc /var/lib/btc-pairbook-archive /root/btc-rewardbook-svc /var/lib/btc-rewardbook; do test -e "$d"; echo "$d exit=$?"; done
stat -c '%s %n' /var/lib/btc-pairbook-archive/ledger.jsonl /var/lib/btc-rewardbook/runtime.jsonl
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
systemctl is-active telemetry-watch.service; echo "exit=$?"
git -C /root/btc-recorder-svc rev-parse HEAD
find /root/btc-forensics -type f | wc -l
git worktree list
du -sb /var/lib/btc-rewardbook /var/lib/btc-pairbook /var/lib/btc-pairbook-archive /root/.claude /root/PROJECT_GAMING_PS5
echo "$S"; ls -la "$(dirname "$(dirname "$S")")"
```

- **H1** — `find` prints exactly one path.
- **H2** — `df` names source `/dev/vda2` and size `31612203008`; `grep -c` prints at least `1`. With H1 this is map §6's
  host identity.
- **H3** — the interpreter prints `3.12.`.
- **H4** — the reward book as TZ-33 left it, and the pair book's archive as TZ-28 left it: `btc-rewardbook.service`
  reads `ActiveState=active` and `UnitFileState=enabled`; `cmp` exits `0` for `btc-rewardbook.service`,
  `btc-pairbook-archive.service` and `btc-pairbook-archive.timer`; the two `commit.txt` print
  `2dcd70e08b18b93c64bb67d9849ac1216ce40e41` and `d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3`; `sha256sum` prints
  `a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670`,
  `46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4` and
  `2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673`. The run removes the reward book's files by the
  names and the record TZ-33's code writes, and reads the pair book's archive's state and records as TZ-28's writes
  them, so this TZ's work needs both as they stand.
- **H5** — this archive is not installed: each of the first `for` line's four paths prints `exit=1`.
- **Memory gate** — `MemAvailable` at least `120,676,352` bytes (§0.4).
- **Disk gate** — `avail` at least `2,300,000,000` bytes (§0.4).

Any of these seven failing is BLOCKED. **The rest is printed and carries no threshold:** the boots; the eight units and
the three timers, among them the package manager's, whose runs stopped and started both older capture units on
2026-10-22 and 2026-10-23 (map §7 item 120); `cmp` of the recorder's and the pair book's units against `main`'s; the
sizes of the pair book's archive's ledger and of the reward book's `runtime.jsonl`; `telemetry-watch.service`'s two
states, on which map §6's headroom is conditional; the recorder's tree, `e3975b5…`; `/root/tz33-work` absent and the
code and state trees present, by map §3; the forensic store's count, map §3's `2,101`; the worktrees, map §3's two;
`du` of the reward book's store beside `df`, as map §2.6 asks, of the pair book's store and its archive's state, and of
`/root/.claude` and `/root/PROJECT_GAMING_PS5`, the Executor's session store and the consumer map §6's headroom nets
out; and the listing of the directory that holds the session's own, whose UUID directories `I scratch` names live or earlier
(§9).

### 0.4 Resource floors, in exact bytes

**Disk.** `/dev/vda2` free at least **`2,300,000,000`** bytes: the reward book's `RESOURCE_FLOOR`, `2,200,000,000`
(`research/tz33-reward-book-capture.py` line 189), below which it halts with exit `1`, which its unit does not restart
(map §2.6), plus `100,000,000` for this session — the worktree, `9,450,026` bytes of tracked files at `5efec8f`; the
logs under `2,000,000`; the service's code, `99,388 + 74,576 + 106,284 + 41` bytes; and the first run's records under
`2,000,000`. **No copy of a stream file is written:** the run hashes, sends and downloads each in pieces of at most
1 MiB (`research/tz27-pairbook-archive.py` lines 293 to 304, 618 to 636 and 641 to 653). **The run's own floor is
`2,002,000,000`** (Appendix A line 142): the recorder's floor, `2,000,000,000` (map §6), plus `2,000,000` a run writes at
most — the Architect's run over 400 stream files wrote `738,493` bytes of records and `443,340` of log. Below it a run
defers, having written its start record alone. The reward book's stream floor, `7,300,000,000`, is no gate here: below
it the streams are paused already, and this TZ is what lifts them.

**Memory.** `MemAvailable` at least **`120,676,352`** bytes: twice the largest peak any mode reached in the Architect's
runs under Python 3.12.3 — `selftest`, `60,338,176` at the largest of 25 runs, the last seven on these bytes from
`59,125,760` to `59,400,192`. The others: `fingerprint` `38,481,920` to `38,789,120`; **the run**, `36,327,424` to
`36,560,896` over nine runs of 400 stream files and `2,182,530,000` bytes against a loopback server in another process
over TLS, the last three on these bytes — it hashes, sends and downloads in pieces, so the bytes of the set do not move
its peak, and at 400 files it holds the set's largest population; `first` `34,308,096` to `34,754,560` reading such a
run back; `still`, `timer`, `final`, `stopped`, `installed` and `mark` from `32,129,024` to `32,976,896`. The runs not
made on these bytes were made on texts of this file that differ from it in the values of `RUN_MEM_FLOOR` and
`DISK_FLOOR`, in comments and in self-test code, none of which an allocation of those modes reads.
**The run's own floor is `73,121,792`** (Appendix A line 143, checked at lines 582 to 586), twice its largest peak; TZ-28's
first run on the host, the same TZ-27 and TZ-28 code, read `36,884,480` (map §6, memory). `path` and `path-token` —
TZ-28's modes — re-read `MemAvailable` at their start and stop BLOCKED below TZ-27's floor, `93,454,336`
(`research/tz27-pairbook-archive.py` lines 125 and 324 to 328). The unit's ceiling, `MemoryMax=128M`, is `134,217,728`
bytes, `3.67` times the run's largest peak. Map §6 records the host: `1,002,127,360` bytes in all, one processor; TZ-33
read `225,431,552` to `336,314,368` available with its session open. Every session mode runs under `nice -n 19`, and
the unit under `Nice=19`.

### 0.5 Refs

`git ls-remote origin` before §3.1's push, every ref reported. Map §1 records, read on 2026-10-28 at 13:38 UTC,
**79** ref lines, PR #32's merge ref among them; PR #32's merge, `a209b09`, removed that ref, and `main` stood at
`5efec8fe25f452963fc51c87c03aa9fcc9b0e985` with **78** ref lines when the Architect read it at 21:13 UTC that day —
`HEAD`, eleven branches with `main`, the two annotated tags and their peeled lines, thirty `pairbook-streams-*` tags and
thirty-two pull heads. Every run of the pair book's archive adds one tag — at 03:00:20 UTC, and 600 s after every
reload of systemd (map §7 item 115). Every commit on `main`'s first-parent line above `6467d84`, the commit that carries
revision `2026-10-28-a`, is reported with the paths it changed — five at the Architect's read: `ef6184a`, `69f27e4`,
`45280e6`, `d2ccfd4` and `5efec8f`, which add or change `ADVISOR-SKILL.md` and `.github/workflows/adv2-signal.yml`,
neither a row of map §0 — and the upload that carries this TZ above them. A difference is recorded, not BLOCKING,
unless `main` does not carry revision `2026-10-28-a`, or `refs/heads/tz-34-rewardbook-archive-timer` or any
`refs/tags/rewardbook-streams-*` already exists — each is BLOCKED.

---

## 1. Why this TZ exists, and what the timer does

Line numbers in this section are Appendix A's unless a file is named. `tz27` is `research/tz27-pairbook-archive.py`,
`tz28` is `research/tz28-pairbook-archive-timer.py` and a service line is `research/tz33-reward-book-capture.py`'s, each
at `5efec8f`.

**The deadline, as the code evaluates it** (map §7 item 106's rule). At every slot `S` the reward book decides whether
its stream opens: `stream_off_reason` (service lines 1294 to 1304), called at `S − 6` — the task starts at
`S − OPEN_BEFORE − LAUNCH_LEAD` (service lines 169, 173 and 1625) — with the free bytes of `/var/lib` read then and
`stream_bytes_total(ROOT)`, the bytes of every stream file in the store summed from its directory entries then (service
lines 1279 to 1291 and 1530 to 1531): below `STREAM_FLOOR`, `7,300,000,000`, or at `STREAM_CAP`, `4,000,000,000`, no
stream opens (service lines 190 and 191). Both are read live, so a file removed lifts either at the next slot, with no restart. At the
store's `1,016,070,120` bytes a day the floor binds first, at about **20:00 UTC on 2026-10-30**, and the cap at about
10:00 UTC on 2026-11-01 [modelled, map §2.6]. A daily archive keeps the store near one day's streams, far below both.
**The archive runs itself.**

**What a run does** (`run`, lines 752 to 806), through TZ-27's and TZ-28's functions where they exist. The instrument
loads `tz28` from beside itself, executed from the bytes whose SHA-256 it asserts, and `tz28` loads `tz27` the same way
(lines 67 to 83; tz28 lines 63 to 76), so the upload, the proofs, the idle stretch, the ledger and the resume rule exist
once, there, and are not written again here.

1. **Resume or begin.** A run whose ledger holds a run without a terminal record — `complete`, `empty` or `halt` —
   resumes it, with its set; otherwise it begins a new one as of `A`, its own start second, at least one second after
   every earlier run's (lines 763 to 766; tz28 lines 229 to 235).
2. **The set** (`inventory`, lines 271 to 305): every stream file `<S>.<k>.stream.jsonl.gz` of every slot that holds a
   `slot.json` and whose `slot.json` was due at least 60 s before `A` — `S + 910 + 60 <= A` — in order of `S` and of the
   index `k`, at most 400, each hashed with its size and time unchanged. The reward book writes a slot's `slot.json` at
   `S + 910`, after its stream file is closed (service lines 1272 to 1276, 1536 to 1553 and 1560 to 1566), so a slot that holds one streams no more.
   **The slots considered** are those due by `A` that hold a stream file, each `closed` or `unclosed` — no `slot.json`,
   a process that stopped inside it — and an unclosed slot's files are kept and listed at every run; a slot due after
   `A` is counted `open`, and one with no stream file `streamless`. The set's document carries this TZ's tag rule,
   **one Release a run on the lightweight tag `rewardbook-streams-<A>`**, which neither `tz27.TAG_RE` nor `tz28.TAG_RE`
   covers, so no TZ-27 or TZ-28 mode can act on it; each asset is named `<D0>-<S>.<k>.stream.jsonl.gz`, its day
   directory and its file (lines 146 to 148 and 324 to 348). A set with no file records `empty` and ends (lines 598 to
   600).
3. **Upload:** the credential `tz27.credential()` reads from the primary checkout's remote URL (tz27 lines 725 to 739);
   the Release on the tag, created at the commit the run's code is from — `commit.txt`'s — published and never the
   latest (tz28 lines 306 to 309 and 346 to 352), or resumed; then `tz27.upload_set` (tz27 lines 765 to 812): each
   asset sent whole and hashed as sent, one kept where it already matches, 1 s between writes (lines 628 to 650).
4. **Verify,** 120 s after the upload's completion record: `tz28.verify_phase` (tz28 lines 479 to 508) — with no
   token, every asset `uploaded` with the set's bytes and `digest`, then every asset downloaded whole and hashed.
5. **Remove** (`remove_set`, lines 669 to 708): each file of the set in order, its slot still closed and due; hashed
   again equal to the set's; removed, and its day directory's other entries left as they were; logged at once in
   `delete.jsonl` (lines 711 to 731).
6. **Complete:** every request and every removal read against the idle stretch, the store's stream bytes, free space
   and the projection to the next stop, recorded (lines 734 to 749).

**No restart.** TZ-27 and TZ-28 restart the pair book because its sum is read once, at a start (map §7 item 106); the
reward book's is read at every slot (above), and a restart would cost the slot it falls in.

**The idle stretch — every request, and every removal.** The pair book streams from `T + 595` to `T + 905` of each
900 s window, and between `T + 910` and `T' + 595` makes no request of its own but its next window's documents (map
§2.5). **Every request the run makes** goes through `tz28.Gh28`, TZ-27's `GitHub` with one change: before it starts,
`tz28.idle_wait` holds it until a second of the window from 15 to `590 − budget`, its budget `5 + ⌈bytes / 2,000,000⌉`
seconds, and each is timed into `runs/<A>/transfers.jsonl` (tz28 lines 99 to 101, 135 to 150 and 312 to 352). **Every
removal is held the same way**, its budget its file's (lines 653 to 666), and timed into `delete.jsonl`. The reward
book decides each slot at `S − 6`, second 894 of a window, outside the stretch.

**The quiet — why a removal waits, and for what.** The reward book sums its store from directory entries and then each
entry's size: a file removed between its listing and its `stat` raises `FileNotFoundError` (service lines 1284 to 1291).
At a slot's decision that exception ends the slot's task — an `error` record and no `slot.json` (service lines 1530 to
1531 and 1580 to 1594, the task wrapped at 1627 to 1628). At a process's start the sum runs before the `start` record,
outside any handler (service lines 1615 to 1616), and the exception ends the process with exit `1`, which its unit does
not restart (`deploy/systemd/btc-rewardbook.service` line 16; map §2.6). The decision falls at second 894, outside the
stretch, **but** a slot's task waits for its day's selection before it sums — up to `S + 880` where the selection is
late (service lines 1526 and 1530 to 1531) — and a process can start at any second. So **before each removal, and
again right after its hash and before its unlink, `quiet` must read the reward book quiet** (lines 406 to 421): its day's
selection recorded `ok` at least 5 s before — the task proceeds within a second of the selection being held (service
lines 1483 to 1491 and 1504 to 1511) — and no process under its exact argv but the one whose `start` record is at least
10 s old, read from `/proc` and from `runtime.jsonl` (lines 546 to 562; tz27 lines 994 to 1004). A removal waits while
it is not, at most 1,800 s over the run's removals (`QUIET_MAX_S`, line 137), then defers (below). The unlink follows
the last read within a few milliseconds; a process started after that read reaches its sum later than that, past its
interpreter's start-up.

**The hold.** The pair book's archive runs at 03:00:20 UTC and 600 s after every reload of systemd (map §7 item 115).
Before its upload and before its verify, a run waits while `btc-pairbook-archive.service` runs, at most 1,800 s
(`HOLD_MAX_S`, lines 139 and 613 to 625), so that the two archives' transfers do not share the stretch; past it, the
run defers.

**When a run fails** (lines 795 to 806). Before any removal — the set, the upload, the verify — a failure **defers**
the run: exit `75`, a `deferred` record, and the next run resumes the same set, its upload keeping every matching asset
and its verify reading every asset again. **In the removal only the quiet's timeout defers:** the files removed so far
are recorded in `delete.jsonl`, and the next run uploads nothing new, verifies again and removes the rest, counting a
file absent only where its removal is recorded (lines 678 to 683). **Any other failure from the removal on halts the
archive, and so does a refusal by either audit hook at any step; the third deferral of one set halts it too**: a
`halt` record, and the run disables its own timer — `systemctl disable --now btc-rewardbook-archive.timer`, K-34 —
recording its exit (tz28 lines 599 to 605; lines 527 and 528). A halted archive refuses every later run until a TZ
appends a `clear` record (lines 756 to 762; tz28 lines 223 to 226). **The run never stops or starts the reward book.**

**The two hooks.** TZ-27's audit hook, installed when `tz27` is loaded (tz27 line 275), reads its module's `ROOT` at
every event; this file sets it to the reward book's store before any mode acts (lines 165 to 166), so TZ-27 §2's rule
guards that store: read only by TZ-27's read modes, listed only by its list modes, written never, a file removed only in
mode `delete` and only where the run names it, no process started by the set or the removal, every write outside the
work tree refused (tz27 lines 174 to 272). This file's own hook narrows it (lines 175 to 236): under the reward book's
store a stream file is read only in the hook's modes `inventory`, `upload` and `delete` — the set, the upload and the
removal — `slot.json` only in `final`, the mode the session's `first` and `final` take and the run's end, `runtime.jsonl`
only in `delete` and `final`, nothing else at all, and only a stream file named by the run removed; nothing under the
pair book's store; under its archive's state only `ledger.jsonl`, read only in `still`. Each step of the run sets the
hook's mode — `inventory`, `upload`, `verify`, `delete`, `final`, `hold` — and the run's work tree is its state
directory, so every write outside `/var/lib/btc-rewardbook-archive/` is refused. Every record the run writes is
asserted against TZ-27's forbidden keys (tz27 lines 151 to 154 and 331 to 345; lines 342 to 348 and 705).

**The timer.** `OnCalendar=*-*-* 01:30:20 UTC` — second 20 of its window, inside the idle stretch, and 90 minutes before
the pair book's archive's 03:00:20 — and `OnActiveSec=1800`, `AccuracySec=1s` (Appendix A's timer). **`OnActiveSec` is
kept, examined as map §7 item 115 asks:** a reload of systemd re-arms it, so the archive also runs 1,800 s after every
reload — `crypto-deploy.service`'s, the package manager's, and this TZ's own; such a run takes what has closed and is
harmless, and 1,800 s puts it 1,200 s after the pair book's archive's run that the same reload sets off, which took
under 15 minutes on its first run (map §2.5) — the hold covers the rest. It is kept because the deployment must be
proved on a run the timer fires (CANON hard rule 14) before the floor binds, and the calendar's next elapse may come
after it. **The service:** `Type=oneshot`; `Restart=no` — no exit is retried by systemd, because the next run resumes
what this one left; `TimeoutStartSec=21600`; `Nice=19`; `MemoryMax=128M`; output appended to
`/var/lib/btc-rewardbook-archive/archive.log`; no `[Install]` — the timer starts it. Its exits: `0` complete or empty,
`75` deferred, `1` halted or an assert before the run began, `2` another run holds the lock (lines 795 to 825; tz28
lines 95 and 96). A run checks that systemd started it — `INVOCATION_ID` set, its directory and file the unit's — and
records the trigger systemd hands a unit it starts, `TRIGGER_UNIT` and `TRIGGER_TIMER_REALTIME_USEC`, where it sets
them (lines 500 to 509, 770 to 772 and 809 to 825). **6 h** bounds the slowest run this TZ allows (§6).

**The credential.** The run reads the token from the primary checkout's remote URL through `tz27.credential`, as
TZ-28's runs do daily, and prints only its source; it sends the token to `api.github.com` and `uploads.github.com` alone
and follows no redirect with it (tz27 lines 498 to 506, 559 to 653 and 712 to 739; tz28 lines 312 to 352; line 503).
A unit is not the session, so the classifier that refuses the session's token (map §6; contract §5.1) does not bind it.
**The Executor never reads, prints or stores the credential:** B-ENABLE's `path-token`, the Boss's, is this session's
only process that reads it.

**The reserve stands** (CANON PART II, L0; map §2.6): no run decompresses a stream file, and no mode opens a rewards
file or a selection; each Release's body says its assets are reserved for L0's measurement (lines 351 to 360).
`slot.json` and `runtime.jsonl` are the reserve's exceptions, read here for counts, flags, process ids and times.

**Discarded:** importing TZ-33's instrument for its store's names and its sum — its audit hook refuses every write
outside `/root/tz33-work` (service lines 121 and 320 to 388), so its predicates and constants are restated here and asserted
against its text by the self-test, and its `stream_bytes_total` is run from its own text on the self-test's stores
(lines 112 to 129 and 1296 to 1320); removing at any second — the reward book sums at second 894 and at a start, and a
removal under either costs a slot or the process; restarting the reward book after the removal, as TZ-28 restarts the
pair book — its sum is live, and a restart loses a slot; `OnActiveSec=600`, the pair archive's own — every reload would
start both archives together; and one Release for every run — up to 1,000 assets a Release (map §6), about ten days.

**What this TZ decides.**

1. **The instrument and the two units**, on the branch `tz-34-rewardbook-archive-timer`; `main` carries them once the
   Boss merges after the verdict.
2. **The deployment:** the service's code in `/root/btc-rewardbook-archive-svc/`, its state directory
   `/var/lib/btc-rewardbook-archive/`, and the two units under `/etc/systemd/system/`, by B-INSTALL; the timer enabled
   by B-ENABLE, after the credential's proof.
3. **The proof:** the timer's first run, fired 1,800 s after B-ENABLE, read back by `first` — and every gate of §4.
4. **The stops:** K-34; B-UNINSTALL on a BLOCK before the timer runs; and B-START-RB where the reward book is found
   down after a G-NEXT FAIL (§4.8).
5. **Nothing else on the host is touched** but the paths of §2.

---

## 2. Scope

**Repository paths and refs this TZ may write, and no others:**

1. `research/tz34-rewardbook-archive-timer.py`, `deploy/systemd/btc-rewardbook-archive.service` and
   `deploy/systemd/btc-rewardbook-archive.timer` — new, byte for byte Appendix A's, on branch
   `tz-34-rewardbook-archive-timer`, then a pull request. Not merged by the Executor.
2. `CryptoReports/TZ-34-rewardbook-archive-timer-report.md` — straight to `main`, in one commit. **The one path pushed
   to `main`.**
3. **The first run's Release, on its lightweight tag `rewardbook-streams-<A>`, holding exactly that run's set**, written
   by the unit alone, under the credential the unit reads — **the exemption to prohibited item 11**. A Release or tag a
   run wrote stays; none is deleted (contract §3.3).

**Host paths this TZ may write:** `/root/tz34-work/**`; `/root/btc-forensics/`, by exclusive create only (§9); in the
primary checkout `/root/btc-5m-twap`, its `.git` for the branch and the worktree and its `CryptoReports/` for the
report; and, by B-INSTALL alone, `/root/btc-rewardbook-archive-svc/` — the instrument, TZ-28's and TZ-27's files and
`commit.txt` — the empty directory `/var/lib/btc-rewardbook-archive/`, and the two unit files under
`/etc/systemd/system/`, with the link B-ENABLE's `systemctl enable` makes. **The unit writes**, and only under
`/var/lib/btc-rewardbook-archive/`: its ledger, `runs/<A>/`, `run.lock` and `archive.log` — **the named exemption to
prohibited item 4**. **Host paths removed, and nothing else:** **the first run's set's stream files under
`/var/lib/btc-rewardbook/<D0>/`, by the unit's run alone, each proved first (§1) — the named exemption to prohibited
item 5: the capture is moved, never reclaimed**; `/root/tz34-work/` with its worktree, and the directories `I scratch`
names earlier (§9); and on a BLOCK before the timer runs, B-UNINSTALL's installation (§4.8).

**Prohibited, each absolutely:**

1. No committed file is modified; every `frozen` row of map §0 is byte-identical at run end.
2. **Under `/var/lib/btc-recorder/` nothing is opened, listed or written**; only §0.3's `df`, `find` and `grep -c`, at
   both of its runs — §0.3 and §3.9 — touch the root. TZ-27's hook refuses every open and listing there, in every mode
   and in the run.
3. **Under `/var/lib/btc-pairbook/` and `/var/lib/btc-chainbook/` nothing is opened, listed or written**; outside the
   instrument only §0.3's and §3.9's `du` of the first. This file's hook refuses every open, listing and change under
   the first, and TZ-27's under the second.
4. **Under `/var/lib/btc-pairbook-archive/` nothing is opened but `ledger.jsonl`, read only, by `still`, and nothing is
   listed or written;** outside the instrument only §0.3's `stat` and `du`. **Under `/var/lib/btc-rewardbook-archive/`
   the session writes nothing but B-INSTALL's creation of the empty directory and, on a BLOCK, B-UNINSTALL's removal of
   it while empty; it reads nothing there but by the instrument's `installed`, `first`, `final` and `stopped`, and by
   §3.9's `tail` of `archive.log`, `sha256sum` of the run's files and `du`.** The unit's own writes there are the
   exemption above.
5. **Under `/var/lib/btc-rewardbook/` nothing is written but by the reward book's unit, and nothing removed but the
   first run's set's stream files, by the archive's run.** The run reads the stream files as bytes — the set, the upload
   and the removal — `runtime.jsonl` in the removal, and directory entries in the set, the removal and its end; in the
   session `first` reads `runtime.jsonl` and the `slot.json` of G-NEXT's slots and of the slots the run spans, and lists
   directory entries, and `final` lists them; nothing else of the store is opened by any mode — no rewards file, no
   selection, no `service.log`, no `service.pid`. Outside the instrument only §0.3's `stat` of `runtime.jsonl` and `du`,
   and §3.9's `tail` of `service.log` and `du`. **No file is decompressed, and no price, size, side, book hash, rate,
   competitiveness or outcome is extracted from a stored body or from a Release asset** (§1, the reserve). Both hooks
   refuse every other open, listing and change there.
6. **No unit is created, started, stopped, enabled, disabled, signalled or changed but by B-INSTALL, B-ENABLE,
   B-RETRY, the archive's run — on a halt its own K-34 — and K-34, B-UNINSTALL and B-START-RB where §4.8 authorizes
   them.** `systemctl show`, `is-active`, `is-enabled`, `list-timers`, `systemd-analyze verify`, B-INSTALL's
   `daemon-reload` and `journalctl -u` are this TZ's only other reads and acts on a unit. **No `daemon-reload` runs after
   B-ENABLE but the one K-34 or B-UNINSTALL makes**, because each re-arms both archives' timers (map §7 item 115). The
   recorder, the pair book, the pair book's archive and the reward book are never signalled.
7. `/root/tz04a-env/`, `/root/tz01-env/`, `/root/tz18a-svc/`, `/root/btc-recorder-svc/`, `/root/btc-pairbook-svc/`,
   `/root/btc-pairbook-archive-svc/` and `/root/btc-rewardbook-svc/` are not modified, and `/root/btc-forensics/` only
   by §9's exclusive create.
8. Nothing is pushed to `main` except the report of item 2.
9. **Requests:** `path`'s anonymous reads of `api.github.com` and its download through `github.com`'s redirect;
   `path-token`'s two reads of `api.github.com` under the credential, in the Boss's B-ENABLE; `first`'s anonymous reads
   of `api.github.com`; the unit's run, as §1 says; the self-test's, to `127.0.0.1` alone; `git` against `origin`; and
   `gh` for the pull request. No other request, and **none to a venue host** — the reward book's own are the reward
   book's.
10. **The Executor never reads, prints or stores the credential.** Only `path-token`, run by the Boss, and the unit's
    run read it, through `tz27.credential` (`research/tz27-pairbook-archive.py` lines 725 to 739), and no message names
    it; no step prints `git remote -v`, `git remote get-url` or `gh auth token`.
11. **No price, size, side, book hash, rate, competitiveness or outcome of any market is printed or written** outside
    the capture's own store, a Release's assets — its files, byte for byte — and §9's copies; downloads are hashed as
    they arrive and written nowhere. Every record the run and the instrument write is asserted against TZ-27's forbidden
    keys (`research/tz27-pairbook-archive.py` lines 151 to 154 and 331 to 345). No other Release is created or changed,
    `tz-01a-dataset`'s and `tz-27-pairbook-streams`'s are only read, and no dataset, archive or binary enters git
    history.
12. **These prohibitions bind the Executor's own reads** (map §7 item 118): no file of the work tree, of a capture's
    store or of either archive's state is printed, whole or in part, but by a command this TZ names.

---

## 3. The work, in this order

From §3.1 on, `nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz34-work/wt/research/tz34-rewardbook-archive-timer.py`
is written **`I`**; a mode is `I <mode>`, run from `/root/tz34-work`. Every command's output goes to `logs/`, one file
per step, and is quoted in the report. **§9's B-RECLAIM-SCRATCH runs after §3.3 and before §3.4; B-RECLAIM-OWN runs
last, after §3.9.** On a BLOCK before §3.1, B-RECLAIM-OWN runs with `I0` in place of `I` and without its `git worktree
remove` line; on a BLOCK after §3.5 and before the timer's first run, B-UNINSTALL runs first (§4.8); on a FAIL, the
stop §4.8 authorizes, then §3.9 and §9, skipping every step that needs a PASS it lacks.

**Where the session's permission classifier refuses a command of a block named B-… or K-…**, the Executor hands it to
the Boss, who runs it in a root shell on the VPS, and verifies it through the reads this TZ names — never from the
Boss's account. **A block handed to the Boss** (map §7 item 124) **is handed over only once its band is open, so its own
wait is seconds; is one command line, every destructive step chained by `&&` to the assertion it depends on; and
appends its output to its log under `logs/` after a `date -u` line, never overwriting it** — B-ENABLE below is written
so, and a refused block is handed over in that form: `cd /root/tz34-work && { date -u; <the block's commands joined by
&&>; echo "exit=$?"; } >> /root/tz34-work/logs/<block>.log 2>&1; tail -n 40 /root/tz34-work/logs/<block>.log`. **Every
`mark` is the Executor's**, taken before its block is run or handed over. Map §6 records `systemctl enable --now`
refused at TZ-20, TZ-26, TZ-28 and TZ-33, and `systemctl kill`, `install`, `daemon-reload` and `systemd-analyze verify`
never.

**This session's systemd steps, and what each sets off** (map §7 items 115 and 125): B-INSTALL's `daemon-reload` at an
instant `L` sets off a run of the pair book's archive at `L + 600`; B-ENABLE's `systemctl enable` at `E` sets off
another at `E + 600`, and this timer's first run at `E + 1,800`; K-34's and B-UNINSTALL's reloads, where they run, set
off one each 600 s later. Each restarts the pair book inside its band, and G-STILL reads each from that archive's ledger
(§4.7). Nothing else in the session reloads systemd.

### 3.1 The branch and its files

```
git -C /root/btc-5m-twap fetch origin
git -C /root/btc-5m-twap worktree add -b tz-34-rewardbook-archive-timer /root/tz34-work/wt origin/main
```

Then §0.1's script again, verbatim but for its argument, `/root/tz34-work/wt`; it must print the same three lines as at
§0.1 but for their directory. Commit those three files alone on the branch, push it with `git push -u origin
tz-34-rewardbook-archive-timer` from the worktree — TZ-33's push went through with the URL's own credential; where it is
refused, through `credential.helper=!gh auth git-credential`, as TZ-29 to TZ-31 pushed (map §6, git remote; §7 item
114) — and open the pull request against `main`. A failed assert here is BLOCKED.

### 3.2 The self-test

`I selftest` must print `49 of 49 checks passed`. It reaches `127.0.0.1` alone, and runs the archive whole on temporary
stores under `/root/tz34-work/selftest-tmp/`, a simulated reward book and a loopback server — a complete run held while
the pair book's archive ran; the next run, and an empty one; a refused credential deferred and resumed; a request due
at second 588 waiting for the next stretch; three deferrals halting the archive and a halt refusing the next run until
a clear; a flipped bit in one asset deferring before any removal; a removal waiting for the day's selection; the
selection never recorded, deferring in the removal; a new process without its start record, deferring with two of three
files removed and the next run removing the third; a file changed after its verify, halting; a hold past 1,800 s — and
removes them (lines 1323 to 1746). It reads the reward book's own file beside it, asserted by its SHA-256, and runs that
file's `stream_bytes_total` from its text on its stores (lines 1296 to 1320). A red self-test stops the run here, and it
goes to §3.9 and §9.

### 3.3 The units, and the directories beside this session

`I still` records the recorder's, the pair book's and the reward book's `MainPID`, `NRestarts` and `ActiveState` in
`state.json`, and prints their memory and both archives' units (lines 861 to 899). Then `I scratch "$(dirname "$S")"`
lists every UUID directory beside this session's own and names each **live** — born from 1 s before to 60 s after the
start of a running process whose `argv[0]` is `claude` or ends in `/claude.exe` — or **earlier** — TZ-27's `scratch`
(`research/tz27-pairbook-archive.py` lines 1428 to 1464).

### 3.4 The token-free path — P-PATH

`I path` must print `READING P-PATH: served` (§4.1). It waits for the idle stretch, at most `900` s. **A failed assert
is BLOCKED, and nothing is installed.**

### 3.5 The installation — B-INSTALL, then G-INSTALL

```
install -d -m 0755 /root/btc-rewardbook-archive-svc; echo "exit=$?"
install -m 0644 /root/tz34-work/wt/research/tz34-rewardbook-archive-timer.py /root/tz34-work/wt/research/tz28-pairbook-archive-timer.py /root/tz34-work/wt/research/tz27-pairbook-archive.py /root/btc-rewardbook-archive-svc/; echo "exit=$?"
git -C /root/tz34-work/wt rev-parse HEAD > /root/btc-rewardbook-archive-svc/commit.txt; echo "exit=$?"
install -d -m 0700 /var/lib/btc-rewardbook-archive; echo "exit=$?"
install -m 0644 /root/tz34-work/wt/deploy/systemd/btc-rewardbook-archive.service /root/tz34-work/wt/deploy/systemd/btc-rewardbook-archive.timer /etc/systemd/system/; echo "exit=$?"
systemctl daemon-reload; echo "exit=$?"; date -u +%FT%T.%NZ
systemd-analyze verify /etc/systemd/system/btc-rewardbook-archive.service /etc/systemd/system/btc-rewardbook-archive.timer; echo "exit=$?"
```

Every `exit=0`; the instant after `daemon-reload` is `L`, and the pair book's archive runs at `L + 600`. Then `I
installed` must print `G-INSTALL PASS: 9 of 9` (§4.3). A FAIL, or a non-zero exit, is BLOCKED, and B-UNINSTALL runs
(§4.8): nothing is enabled.

### 3.6 The timer — B-ENABLE, with the credential's proof, then G-TIMER

The Executor waits until the band is open — **second 15 to 300 of a 900 s window, from 07:15:00 to 18:55:00 UTC** — then
takes `I mark enable` and hands the Boss **B-ENABLE**, which he runs at once in a root shell on the VPS:

```
cd /root/tz34-work && { date -u; until t=$(date +%s); p=$(( t % 900 )); d=$(( t % 86400 )); [ $p -ge 15 ] && [ $p -le 480 ] && [ $d -ge 26100 ] && [ $d -le 68400 ]; do sleep 1; done; date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz34-work/wt/research/tz34-rewardbook-archive-timer.py path-token && systemctl enable --now btc-rewardbook-archive.timer; echo "exit=$?"; } >> /root/tz34-work/logs/B-ENABLE.log 2>&1; tail -n 14 /root/tz34-work/logs/B-ENABLE.log
```

It waits in its own text for second 15 to 480 of a window and for 07:15:00 to 19:00:00 UTC; it proves the credential —
**P-TOKEN**, `path-token`, which must print `READING P-TOKEN: served` (§4.2) — and only then enables the timer. Second 15
to 480: P-TOKEN's two requests, each budgeted 5 s, start inside the idle stretch at once. 07:15:00 to 19:00:00 UTC: the
package manager's morning runs — from 06:03 to 06:15 UTC on the days recorded, two of which stopped and started both
older capture units (map §6, process supervision; §7 item 120) — are over before the first run; and the first run, `1,800` s after the enable and at most `21,600` s long, ends
before the calendar's 01:30:20 UTC and is the timer's own 1,800 s elapse alone: `68,400 + 1,800 + 21,600 = 91,800` s,
01:30:00 UTC the next day. **The Executor reads `logs/B-ENABLE.log`**: `READING P-TOKEN: served` and `exit=0`; its
`%N` stamp is `E`. A missing proof or a non-zero exit with no enable is BLOCKED, and B-UNINSTALL runs. Then, within 300 s
of `E`, `I timer` must print `G-TIMER PASS` (§4.4); **a FAIL runs K-34 at once, then B-UNINSTALL** (§4.8), before the
first run fires.

### 3.7 The first run — G-TRIGGER, G-RUN and its readings

From `E + 1,800`, `I first` every 300 s while it prints `NOT YET` and exits `3` (§4.5). A reload of systemd by another
unit re-arms the timer and postpones the first run (§1, the timer); **where `first` still prints `no run since the mark`
at `E + 5,400`, G-TRIGGER reads FAIL**, and K-34 runs. Once the run completes, `first` waits — `NOT YET` — until 30 s
after the last of G-NEXT's slots is due its `slot.json` (§4.6).

**B-RETRY**, only where `first` prints `READING G-RUN: DEFERRED` — the run deferred, the timer still enabled: `I mark
retry`, then

```
systemctl start --no-block btc-rewardbook-archive.service; echo "exit=$?"
```

and `I first` every 300 s again. The unit resumes the same set (§1). **B-RETRY runs at most once.** A second
`DEFERRED`, an `INTERRUPTED`, or a run that halted, is **G-RUN FAIL** — K-34 at once.

`I first` exits `0` and prints `FIRST PASS: 8 of 8`, or stops naming every gate that read FAIL (§4.5), and §4.8 runs
the stop that FAIL authorizes.

### 3.8 Final — G-TIMER and G-STILL

`I final` must print `FINAL PASS`: G-TIMER again, G-STILL, and the store, free space and the next stop projected at
the run's set's rate (lines 1199 to 1223). A G-TIMER FAIL runs K-34; a G-STILL FAIL is reported with its cause from the
three capture units' journal, §3.9's, and stops nothing (map §7 item 120).

### 3.9 The closing reads

§0.3's block again — H5 now reads this archive installed, and is printed — then:

```
TZ=UTC systemctl show btc-recorder.service btc-pairbook.service btc-rewardbook.service btc-pairbook-archive.service btc-pairbook-archive.timer btc-rewardbook-archive.service btc-rewardbook-archive.timer -p Id -p MainPID -p NRestarts -p ActiveState -p UnitFileState -p ActiveEnterTimestamp -p MemoryCurrent -p MemoryPeak
TZ=UTC systemctl list-timers btc-rewardbook-archive.timer btc-pairbook-archive.timer --all --no-pager
journalctl -u btc-rewardbook-archive.service -u btc-rewardbook-archive.timer --no-pager -o short-iso | tail -n 40
journalctl -u btc-recorder.service -u btc-pairbook.service -u btc-rewardbook.service --since "@$(( $(/root/tz04a-env/venv/bin/python -B -c 'import json; print(json.load(open("/root/tz34-work/state.json"))["still34"]["at_ns"] // 10**9)') - 5 ))" --no-pager -o short-iso
tail -n 120 /var/lib/btc-rewardbook-archive/archive.log
find /var/lib/btc-rewardbook-archive -type f -exec sha256sum {} +
tail -n 20 /var/lib/btc-rewardbook/service.log
free -b
df -B1 --output=source,size,avail /var/lib; du -sb /root/tz34-work /var/lib/btc-rewardbook /var/lib/btc-rewardbook-archive /var/lib/btc-pairbook /root/.claude
cat /root/tz34-work/state.json
```

`archive.log` holds the run's own lines — counts, names, times, statuses, process ids and the SHA-256 of files — and
`service.log` the reward book's start and stop lines, one line a selection attempt and one a slot; neither holds a
price, a size, a side or a rate (§2 item 11).

---

## 4. The gates — fixed here, before any of their data exists

| gate | population | PASS | false failure | power, against |
|---|---|---|---|---|
| **P-PATH** | `tz-01a-dataset`'s Release through `Gh28`: 2 API requests and 1 download | §4.1 | `0` | `1`, a refused request, a record without its digest, a download not served, a request outside the idle stretch |
| **P-TOKEN** | the credential: 2 API requests | §4.2 | `0` | `1`, no credential, one from another source, no push right |
| **G-INSTALL** | the service's four files, the two units, the state directory | §4.3 | `0` | `1`, a byte changed, a unit systemd parsed otherwise, a directory not empty or not root's |
| **G-TIMER** | the timer, after B-ENABLE and at `final` | §4.4 | `0` | `1`, a timer not enabled, another schedule, another unit |
| **G-TRIGGER** | the first run after the enable mark | §4.5 | `0`, unless reloads by other units postpone it past `E + 5,400` | `1`, no run, a run by hand or by the calendar |
| **G-RUN** | that run's ledger and the service's last result | §4.5 | `0` | `1`, a deferral twice, a halt, an interruption |
| **G-SET** | the run's set, as `set.json` and its record hold it, against the store after it | §4.5 | `0` | `1`, a set not this TZ's rule's, two set records, a stream file of a closed or unrecorded slot left beyond the deferral |
| **G-UPLOAD** | the run's Release, by its own record, read again from the session; its tag | §4.5 | `0` | `1`, an asset missing, beyond the set, not its digest; a tag not at the run's commit |
| **G-DOWNLOAD** | the run's own full downloads, `verify.json` | §4.5 | `0` | `1`, one asset's bytes not the set's |
| **G-DELETE** | the set's files on the host | §4.5 | `0` | `1`, a file left, a removal unrecorded, a slot's `slot.json` lost |
| **G-IDLE** | every request and every removal of the run | §4.6 | `0` while the host serves `2,000,000` bytes a second | `1`, a request or removal started outside the idle stretch or ending past second 590 |
| **G-NEXT** | the slots the reward book decided from the run's first removal to 900 s after its last | §4.6 | `0` while nothing but the run touches the reward book | `1` against a slot of them left without its `slot.json` or with its task's error record |
| **G-STILL** | the recorder's, the pair book's and the reward book's units, §3.3 to §3.8 | §4.7 | `0` while no other cause restarts them | `1`, a restart or a stop |

**Every gate is exact** — a direct read of GitHub, of the files' bytes, of systemd and of the run's and the reward
book's own records — so its false-failure probability under the model it judges is `0`, and the family's too, under
the conditions named. **A FAIL before §3.6 enables nothing; a FAIL before the run's removal removes nothing.**

### 4.1 P-PATH

The run's own request path without a token, proved before anything is installed (CANON hard rule 14): TZ-28's `path`
(`research/tz28-pairbook-archive-timer.py` lines 756 to 782), unchanged — `Gh28`, as the run builds it, with no token,
on the one Release whose bytes map §2.1 fixes: `GET /repos/seahomebatumi-ai/btc-5m-twap/releases/tags/tz-01a-dataset`,
one page of its assets, then the asset's download URL through `github.com`'s redirect; the asset `uploaded`, `76818669`
bytes, `digest` `sha256:229a944f…`, the expected URL; the download `200`, `76,818,669` bytes, SHA-256 equal; **3
requests, each started inside the idle stretch and ended by second 590**. Every header is `tz27.build_request`'s
(`research/tz27-pairbook-archive.py` lines 509 to 519): `Accept: application/vnd.github+json`, or
`application/octet-stream` for a download; `User-Agent: btc-5m-twap-tz27`; `X-GitHub-Api-Version: 2022-11-28`; and only
where given `Authorization: Bearer` and the token, and a body's `Content-Type` and `Content-Length` — beside `urllib`'s
own `Accept-Encoding: identity`, `Host` and `Connection: close`. A request that carries the token follows no redirect
(tz27 lines 498 to 506).

### 4.2 P-TOKEN

The credential half, inside B-ENABLE: TZ-28's `path-token` (`research/tz28-pairbook-archive-timer.py` lines 785 to
804), unchanged — `tz27.credential()` as the run calls it, **its source asserted to be the primary checkout's remote
URL**, the source TZ-28's unit reads daily, as its `upload` records name it, where `gh`'s token is never proved under
systemd (map §7 item 114); `GET
/repos/seahomebatumi-ai/btc-5m-twap` with it, `200`, `full_name` this repository and `permissions.push` true; and the
Release on `tz-27-pairbook-streams` read with it, id `409534533` — **2 requests**. **The write half cannot be proved
without writing:** its first request is the first run's own creation of its Release, and a refusal there defers the run
with nothing removed (§1), which G-RUN reads.

### 4.3 G-INSTALL

Nine checks (lines 908 to 953): `commit.txt` the branch head, which is its upstream's; the service's copy of the
instrument the branch's, byte for byte by SHA-256; its copies of TZ-28's and TZ-27's files the branch's and `46a019d6…`
and `2cba96bc…`; both units under `/etc/systemd/system/` byte for byte the branch's; `/var/lib/btc-rewardbook-archive/`
a directory, root's, mode `0700`, empty; the service `loaded`, `inactive` and `static`; the service a `oneshot`,
`Restart=no`, `Nice=19`, `MemoryMax` `134217728`, `TimeoutStartUSec` `6h`, its working directory the state directory,
its `ExecStart` argv `/root/tz04a-env/venv/bin/python -B -u /root/btc-rewardbook-archive-svc/tz34-rewardbook-archive-timer.py
run` and its fragment under `/etc/systemd/system/`; the timer `loaded`, `inactive` and `disabled`, its fragment there.

### 4.4 G-TIMER

Nine checks, read under `TZ=UTC` (lines 975 to 1000): `loaded`; `active`, its sub-state `waiting` or `running`;
`enabled`; its fragment under `/etc/systemd/system/`; its unit `btc-rewardbook-archive.service`; `OnCalendar=*-*-* 01:30:20 UTC`;
`OnActiveUSec=30min`; `AccuracyUSec` `1s`; and `NextElapseUSecRealtime` exactly the next 01:30:20 UTC after the read.

### 4.5 The first run, re-read — `first`

`first` (lines 1064 to 1196) finds the first run whose `start` record is at or after the enable mark, prints every
record of it, and reads it back **from the run's files, the store, the reward book's own record, systemd and the
Release — never from the run's own verdicts alone**:

- **G-TRIGGER** (lines 461 to 470 and 1097 to 1105) — the trigger systemd handed the run, recorded in its first `start`
  record: `TRIGGER_UNIT` `btc-rewardbook-archive.timer`, its `TRIGGER_TIMER_REALTIME_USEC` at least 1,800 s after the
  enable mark less 2 s for whole-second stamps, and the run's first record within 60 s after it; where systemd set no
  trigger, the timer's `LastTriggerUSec` read the same way. Printed beside it: which of the two it read, and both.
- **G-RUN** — the run's terminal record `complete`, the service's last `Result` `success` and `ExecMainStatus` `0`.
- **G-SET** (lines 1030 to 1061) — one set record, `set.json` its SHA-256, and the document this TZ's rule rebuilds from
  it equal to it; its deferral the closed slots' stream files not taken, and the files taken its asset count; **and the
  store after the run against it:** no stream file left of a slot due by `A` that the set does not record, at most its
  deferral's files left of the slots it records closed, and every slot's `slot.json` present or absent as the set
  recorded it. Every considered slot and every taken file printed, `SLOT` and `S` lines.
- **G-UPLOAD** — the Release on the run's tag read again with no token: published on the tag, no asset missing or beyond
  the set, each `uploaded` with the set's bytes and `digest`; and `git ls-remote` reading the tag a lightweight one at
  the run's commit.
- **G-DOWNLOAD** — `verify.json` the SHA-256 its record names, its rows the set's, every download `200` and equal.
- **G-DELETE** (lines 376 to 384) — every file of the set absent, each removal recorded in `delete.jsonl`, every slot of
  the set still holding its `slot.json`.
- **G-IDLE** and **G-NEXT** — §4.6.

**PASS** is all eight. One `ROW` line an asset prints its name, bytes, the set's SHA-256, the Release's `digest`, the
downloaded SHA-256 and the removed file's — the per-asset table §8 asks for, from the instrument itself. Printed beside
the readings: every request's and every removal's second and duration (`T` and `X` lines), the `slot.json` summary of
every slot the run spanned (`ACROSS` lines) — its process, flags, segments, frames, largest gap and stored bytes — and
every hold.

### 4.6 G-IDLE and G-NEXT

**G-IDLE:** every request of the run, from `transfers.jsonl`, and every removal, from `delete.jsonl` — its start the
instant before its hash and its end the instant after its unlink — started at a second from 15 to `590 − its budget` of
its window and ended by second 590 of that window (`tz28.transfer_ok`, tz28 lines 164 to 169; lines 399 to 401).
**PASS** where every one holds both. The run's `complete` record carries both counts (lines 734 to 749).

**G-NEXT:** the slots whose decision instant `S − 6` lies from the run's first removal to 900 s after its last (lines
424 to 432) — those the reward book decided while the run removed files, and the first it decided after, whose sum is
the first to read the store without them. Each slot (lines 435 to 452): **FAIL** where its task left an `error` record
in `runtime.jsonl` — service lines 1580 to 1594, its `what` `slot <S>` — or the slot has no `slot.json`; **PASS** where
a `slot.json` of the process the run began beside — the `MainPID` its `start` record read — shows the stream opened,
with no off reason, no error and not stopped; **UNDECIDABLE** otherwise — a stream kept off by a bound the run does not
judge, or a slot run by another process, which G-STILL then reads. **G-NEXT reads the worst over its slots**, and the
gate fails on FAIL alone (lines 455 to 458 and 1170 to 1181): UNDECIDABLE is reported and stops nothing. `first`
reads it 30 s after the last slot's `slot.json` is due.

### 4.7 G-STILL

From §3.3 to §3.8 the recorder's unit and the reward book's keep their `MainPID`, `NRestarts` and `ActiveState`, and
the pair book's keeps them or changes by its archive's own restarts alone — a chain of `restart` records in that
archive's ledger from the recorded `MainPID` to the current one, `NRestarts` one higher at each, the unit `active` — as
TZ-30 to TZ-33 read it (lines 473 to 492 and 876 to 899; map §7 item 115). **A FAIL names its cause from the three units'
journal**, §3.9's (map §7 item 120), and stops nothing.

### 4.8 The stops — CANON hard rule 14

**K-34** stops the archive and nothing else: future runs. It lets a run in progress end — `disable --now` stops the
timer, not the service it started — so it never cuts a run between a removal and its record:

```
systemctl disable --now btc-rewardbook-archive.timer; echo "exit=$?"
```

**Authorized and run at once, and once,** after `I mark stop`, on the first FAIL of G-TIMER, G-TRIGGER, G-RUN, G-SET,
G-UPLOAD, G-DOWNLOAD, G-DELETE, G-IDLE or G-NEXT — **the gates that judge the archive's process**, which on any of them
is not proved. **The run applies K-34 to itself on a halt** (§1); the session then runs it again, harmless. Its reload
sets off the pair book's archive 600 s later (§3). Verified by `I stopped` at least 30 s after (lines 1226 to 1238) —
the timer `disabled` and `inactive`; the service `inactive` or `failed`, no run in progress; the ledger's last records
printed.

**B-UNINSTALL**, on a BLOCK after §3.5 and before the timer's first run — a FAIL of G-INSTALL, of P-TOKEN, or of
G-TIMER after K-34 — while `/var/lib/btc-rewardbook-archive/` is still empty:

```
rm /etc/systemd/system/btc-rewardbook-archive.service /etc/systemd/system/btc-rewardbook-archive.timer && systemctl daemon-reload && rm /root/btc-rewardbook-archive-svc/tz34-rewardbook-archive-timer.py /root/btc-rewardbook-archive-svc/tz28-pairbook-archive-timer.py /root/btc-rewardbook-archive-svc/tz27-pairbook-archive.py /root/btc-rewardbook-archive-svc/commit.txt && rmdir /root/btc-rewardbook-archive-svc /var/lib/btc-rewardbook-archive; echo "exit=$?"
```

`exit=0`, then each of the four paths `test -e` exit `1` and `systemctl show btc-rewardbook-archive.timer -p LoadState`
`not-found`. Its reload sets off the pair book's archive 600 s later (§3). `rmdir` refuses a state directory that is
not empty; it is empty here, because the timer's first run fires 1,800 s after B-ENABLE, and every case of this block
comes before that or with no enable at all.

**B-START-RB**, only on a G-NEXT FAIL and only where `systemctl is-active btc-rewardbook.service` then reads other than
`active` — the reward book stopped, which its unit does not restart after exit `1` (§1) — after K-34:

```
systemctl start btc-rewardbook.service; echo "exit=$?"
```

Verified at least 60 s after: `systemctl is-active btc-rewardbook.service` `active`, and `TZ=UTC systemctl show
btc-rewardbook.service -p MainPID -p NRestarts -p ActiveState -p ActiveEnterTimestamp` printed. It runs at most once;
the store is as the run left it, its files proved archived before each removal. **G-STILL judges the three capture
units** and stops nothing. **Under PASS no block of this section is run.**

### 4.9 What a PASS establishes, and what it does not

The archive's timer runs unattended, outside every session; its first run, fired by the timer, moved its set to its
own Release byte for byte — by the Release's digest, a full download and a hash before each removal — made every
request and every removal inside the pair book's idle stretch, and left the reward book streaming the next slot on the
same process. **Not established:** the daily calendar run itself — the next TZ that touches the host reads its ledger;
a run's behaviour under a deferral, a halt or a reward book restarting under it — the self-test's, on a simulated
reward book; that no future removal meets a sum — the quiet makes the meeting require a process to reach its sum within
milliseconds of its exec, which G-NEXT's population samples once a run; and anything of a stream's content — L0's
measurement's.

---

## 5. The instrument and the units

`research/tz34-rewardbook-archive-timer.py`, Appendix A, fixed by the Architect as this TZ's Validation and written byte
for byte. **The standard library alone**, run under `/root/tz04a-env` — Python 3.12.3, the reward book's interpreter,
which nothing here modifies. It imports nothing from the repository: it **loads** `research/tz28-pairbook-archive-timer.py`
from its own directory, asserts its SHA-256 `46a019d6…` and executes those very bytes, and TZ-28's file loads
`research/tz27-pairbook-archive.py` the same way, asserting `2cba96bc…` (lines 67 to 83; tz28 lines 63 to 76), so
TZ-27's audit hook is installed and TZ-27's and TZ-28's functions are the ones every step calls. It points TZ-27's hook
at the reward book's store and installs its own (lines 165 to 236). **Its own code** is the reward book's names,
restated (lines 112 to 129), and its store read by them (lines 241 to 321); the set document under this TZ's tag and the
Release's text (lines 324 to 360); the removal's readings and the projection (lines 363 to 401); the quiet, G-NEXT,
G-TRIGGER and G-STILL as pure functions (lines 406 to 492); the run's world (lines 497 to 569); the run's steps (lines 574 to 825); the
deployment's readings (lines 830 to 1238); and the self-test (lines 1243 to 1746). It writes no second implementation of
TZ-27's or TZ-28's upload, proofs, idle stretch, ledger or resume rule. One mode a run; each prints its findings with UTC
stamps, its peak memory, the opens either hook refused, its opens under the reward book's store, its requests, uploads
and downloads with their bytes, and its files removed (lines 1781 to 1786). Exit `0` is every assert held; `1` a failed
assert, named, or a BLOCK whose message says so; `3` NOT YET; and the run's own `75` and `2` (§1). Run with `-O` it
refuses to start (lines 53 to 55).

**The self-test reads the reward book's own file beside it** in the worktree, asserted by its SHA-256 `a276bbb9…`: the
thirteen names and constants this file restates are asserted equal to that text's, and its `stream_bytes_total` is run
from its own text on the self-test's stores and asserted equal to this file's sum (lines 1296 to 1320, 1468 to 1474 and
1537). **The two units** are Appendix A's, installed byte for byte, and the self-test asserts the lines of each that the
instrument depends on (lines 1458 to 1466).

---

## 6. Cost

Measured by the Architect on 2026-10-28 under Python 3.12.3 on a 2.80 GHz Intel Xeon, and taken at the population's
upper bound: **a run's set at most 400 files and `4,300,000,000` bytes** — `STREAM_CAP`, `4,000,000,000`, plus the two
slots that can be streaming when a decision last finds the sum under it, consecutive slots overlapping by 10 s, each cut
at `SLOT_STREAM_MAX` after a flush, `110,000,000` bytes at most, rounded up (service lines 191, 192 and 1143 to 1149); the
largest file `110,000,000` bytes, a budget of `60` s.

| check | population | measured | bound |
|---|---|---|---|
| `selftest` | 49 checks, nineteen simulated runs over nine temporary stores, one loopback server | `2.04` to `2.33` s, seven runs on these bytes | `60` s |
| `fingerprint` | 46 rows, the map | under 1 s | `30` s |
| `path` | 2 API requests and 76,818,669 bytes, held to the idle stretch | the download under 4 s from the Architect's session (map §6) | its wait at most `900` s; `60` s a request, `120` s a read of the download (tz27 lines 122 and 124) |
| `path-token` | 2 API requests | — | `60` s a request |
| `installed`, `mark`, `timer`, `still`, `scratch`, `final`, `stopped`, each `reclaim`, a `first` that prints NOT YET | — | under 1 s each | `30` s a run |
| `first`, the deciding run | the run's records, the store's listing, the Release's record: at most 1 + 5 API pages for 400 assets | under 1 s in a harness over 400 assets, its requests aside | `60` s a request; its reads under `30` s |
| **the run, in the unit** | 400 files, `4,300,000,000` bytes | `59.2` to `64.6` s wall and `46.1` to `50.8` s of processor over 400 files and `2,182,530,000` bytes against a loopback server over TLS, nine runs — four passes over the set's bytes | **`21,600` s, `TimeoutStartSec`** |

**Single-session processor, at the measured rates and the upper bound, under `190` s** — `selftest` `2.3`, the `path`
download's hashing of `76,818,669` bytes at TZ-27's `317,200,000` bytes a second `0.25`, `installed`'s of three files
twice under `0.01`, and at most `184` runs of the other modes under 1 s each: `first` at most `171` of them — every 300 s from
`E + 1,800` to a decision at most `E + 5,400 + 21,600 + 1,840` (the run's latest start, its bound, and G-NEXT's wait
after its last removal: 900 s to the next decision, 910 s to its `slot.json`, 30 s), `⌊27,040 / 300⌋ + 1 = 91`, and
`⌊(21,600 + 1,840 + 300) / 300⌋ + 1 = 80` after B-RETRY — with I0's `fingerprint`, `still`, `scratch`,
`path-token`, `installed`, `timer`, three `mark`s, `final`, `stopped` and two `reclaim`s, `13` — **under `3,600`, so
nothing is sampled.** Nothing the session runs hashes the set. **The run is the unit's, not the session's,** and is
bounded by `TimeoutStartSec`, derived term by term at the upper bound and at `RATE_FLOOR`, `2,000,000` bytes a second:
the set's hashing at TZ-27's measured `317,200,000` bytes a second, `14` s; the hold before the upload, `1,810` s —
`HOLD_MAX_S` and one `10` s poll; the upload, at most `900` s to the stretch, then `4,300,000,000 / 2,000,000 = 2,150` s
of transfer, `400` s of gaps and seven API requests at `5` s, inside at least `515` s of each 900 s window — the stretch's
`575` s less the largest file's `60` s budget — so `⌈2,585 / 515⌉ = 6` windows, `6,300` s in all; the hold before the
verify, `1,810` s; the settle, `121` s; the verify, `900` s to the stretch, then `2,150` s of downloads and six API
requests, `⌈2,180 / 515⌉ = 5` windows, `5,400` s; the removal, its hashing `14` s, `900` s to the stretch, one window of
400 removals at under 1 s each, `900` s, and the quiet's `1,800` s of waiting with at most four of the stretch's
closings inside it, `4 × 385 = 1,540` s, `5,154` s; the end, under `10` s: **`20,619` s in all, under `21,600`.** A run
longer than `21,600` s is stopped by systemd and the next run resumes it (§1); a refused upload's waits (tz27 lines 742
to 755) are not counted, and GitHub's limits are not met at 400 writes a run, 1 s apart (map §6). **At the host's
measured rates** — `9,297,801` bytes a second up and `14,140,406` down (map §6) — a day's `1,016,070,120` bytes take
about `109` s up with `96` s of gaps and `72` s down, one stretch each, and a run about 20 minutes with its waits; the
first run, with up to two days and a half of slots, about 40 minutes [modelled]. **Wall clock about three hours:** §0
to §3.5 about 45 minutes, `path`'s wait among them; B-ENABLE's band; the first run from 1,800 s after it and the slot
after it, about 90 minutes; `first`, `final` and §9 about 20 minutes. **The host pays** each set's bytes sent once and
received once a day, inside the idle stretch.

---

## 7. Validation

| # | check | count |
|---|---|---|
| **V1** | §0.2's fingerprint | `FINGERPRINT PASS`: revision `2026-10-28-a`; anchors 6 of 6, 4 re-derived; 46 rows, 43 of 43 `frozen` equal |
| **V2** | §0.3's host gate | H1 to H5, the memory and the disk gate; the rest printed |
| **V3** | §0.1's and §3.1's files | 3 of 3 hashes asserted at each, lines and bytes; TZ-28's and TZ-27's staged copies `46a019d6…` and `2cba96bc…`; the branch's diff against `origin/main` names exactly the three paths, each `A` |
| **V4** | the self-test | `49 of 49` |
| **V5** | P-PATH | `READING P-PATH: served`, 3 requests, each inside the idle stretch; the record's state, size, digest and URL; the download's status, bytes and SHA-256 |
| **V6** | B-INSTALL and G-INSTALL | 7 of 7 `exit=0`; `G-INSTALL PASS: 9 of 9` |
| **V7** | B-ENABLE, P-TOKEN and G-TIMER | its second of the window inside 15 to 480 and of the day inside 26,100 to 68,400; `READING P-TOKEN: served`, the source the primary checkout's remote URL, push true, Release `409534533`, 2 requests; `exit=0`; `G-TIMER PASS`, 9 checks, at §3.6 and at `final` |
| **V8** | the first run | `FIRST PASS: 8 of 8` — G-TRIGGER, G-RUN, G-SET, G-UPLOAD, G-DOWNLOAD, G-DELETE, G-IDLE and G-NEXT; every `R` record of the run; the `SLOT` and `S` lines; `ROW` n of n; the `T`, `X`, `G-NEXT` and `ACROSS` lines |
| **V9** | B-RETRY | not run, or run once, its mark and `exit=0` |
| **V10** | final | `FINAL PASS`: G-TIMER 9 checks, G-STILL; the projection |
| **V11** | the hooks and the counters | opens refused `0` by either hook at every mode; requests `3` at `path`, `2` at `path-token`, and at a deciding `first` from `2` to `6` — one read of the Release and `⌊n/100⌋ + 1` pages of its assets, for a set of `n` from 1 to 400 files; store opens `0` at every mode but `first`, and there at least `1` — `runtime.jsonl` and each `slot.json` its `G-NEXT` and `ACROSS` lines name; files removed `0` at every session mode but `selftest`, whose `15` are its temporary stores' — `4`, `1`, `1`, `1`, `2`, `1`, `2` and `3` of its stores' sets |
| **V12** | contract §4.2's self-check, and the line below | its first line `0`; the diff naming the three paths alone; nothing `.parquet` or `.zip`; the line below `0` |
| **V13** | §3.9's closing reads | every read printed |
| **V14** | §9's `reclaim` runs | files considered, named by a report, kept by name, copied and already held; the store's count after equal to before plus the copies |
| **V15** | §9's removals | `git worktree remove` without `--force` exit `0`; `test -e` exit `1` for `/root/tz34-work` and each directory removed; `git worktree list` naming `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else |

V12's further line, run beside contract §4.2's three — no stream file entered git history:

```
git ls-tree -r --name-only origin/main | grep -c -e '\.gz$' -e '\.jsonl$'
```

---

## 8. The report

`CryptoReports/TZ-34-rewardbook-archive-timer-report.md`, in contract §8's order. **In its first ten lines:** P-PATH
and P-TOKEN; G-INSTALL; G-TIMER and the next calendar run; the first run — its `A`, its files, slots and bytes, its
Release's id and tag; G-UPLOAD, G-DOWNLOAD and G-DELETE and the bytes freed; G-IDLE; G-NEXT; G-STILL; and whether the
timer, the reward book, the pair book and the recorder run, and how that was verified. **Its §3, Publication,** holds
the branch, its commit, the pull request, the first run's tag and Release id, contract §4.2's self-check, and **every
`ROW` line `first` printed** — contract §5.1's local hash, the downloaded hash and that they are equal, here the unit's,
re-read by the session. Beyond what V1 to V15 print: every mark's instant, and `L` and `E`; every block the classifier
refused, who ran it and when, and the runs of the pair book's archive that the session's reloads set off; **the run's
`R` records, and every `T` and `X` line `first` printed**, so that L0's measurement can set the streams beside the run's
request and removal times; every free-space and `MemAvailable` read with its instant and bound; the run's `peak_rss`;
each unit's memory at every read; §9's counts and removals; and every file the run and the session wrote, by SHA-256,
but a Release's assets. **The report is drafted in the primary checkout `/root/btc-5m-twap` before B-RECLAIM-OWN and
committed after it**, so the removal of this TZ's tree is in it.

---

## 9. Reclaim — the host left clean (CANON hard rule 15)

**What a file is kept for:** a committed report prints its SHA-256, whole or as a prefix of 16 to 64 hex characters, or
it is kept by name: `state.json` and every file under `logs/`. TZ-27's `reclaim` (`research/tz27-pairbook-archive.py`
lines 1467 to 1545) copies each into `/root/btc-forensics/` as `<tree>--<path with / as -->`, by exclusive create, and
verifies its hash; a name already there with the same hash is counted as held, and with another hash is a failed
assert. The branch worktree is not copied: `reclaim` asserts that `git status --porcelain --ignored` in it prints
nothing and that its `HEAD` is its upstream's, so `git worktree remove` needs no `--force`. The report draft in
`CryptoReports/` counts as a report. **No `reclaim`'s output is filtered** (map §7 item 119). **Not scratch, and not
reclaimed:** `/root/btc-rewardbook-archive-svc/` and `/var/lib/btc-rewardbook-archive/` — this archive's code and
state, which its timer runs from and writes.

**B-RECLAIM-SCRATCH**, after §3.3 and before §3.4, for every directory `I scratch` named **earlier** — none it named
live, and never this session's own; map §3 names TZ-33's three, `0358b0b2-9811-5291-867b-b185a7307938`,
`621e47cc-760f-4cb1-8481-c2a8f6828d9d` and `b82e3547-dd0e-46f7-abe9-4ad9e7903328`, unless a reboot emptied `/tmp`:

```
I reclaim <each earlier directory, by its full path>
rm -rf <one such directory>; echo "exit=$?"
test -e <that directory>; echo "exit=$?"
```

One `I reclaim` names every earlier directory; then one `rm -rf` and one `test -e` a directory, each only after
`RECLAIM PASS`. `reclaim` refuses a directory born from 1 s before to 60 s after a running claude process started, and
any path but `/root/tz34-work` that is not a UUID directory under `/tmp/` whose parent's name carries `btc-5m-twap`
(tz27 lines 1491 to 1505). If `I scratch` names none earlier, the block is recorded as empty and skipped. **Where the
classifier refuses it**, it goes to the Boss in §3's form, as one line: `reclaim`, then each `rm -rf` chained by `&&`
after it, then one `test -e` a directory.

**B-RECLAIM-OWN**, last, after §3.9 and with the report drafted. **Its output is written to no file; the report quotes
it verbatim from the session**, the checks after the removal included:

```
I reclaim /root/tz34-work
git -C /root/btc-5m-twap worktree remove /root/tz34-work/wt; echo "exit=$?"
rm -rf /root/tz34-work; echo "exit=$?"
test -e /root/tz34-work; echo "exit=$?"
git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
find /root/btc-forensics -type f | wc -l
df -B1 --output=source,size,avail /var/lib
```

The branch `tz-34-rewardbook-archive-timer` stays on `origin` and as a local ref, and the run's tag and Release stay;
only the working tree goes. **Kept:** `/root/btc-rewardbook-archive-svc/`, `/root/btc-rewardbook-svc/`,
`/root/btc-pairbook-archive-svc/`, `/root/btc-pairbook-svc/` and `/root/btc-recorder-svc/` are the running units' code,
`/root/tz18a-svc/` the disabled chain book's; the capture roots, both archives' state and the forensic store are data,
never scratch. **A refused `rm -rf` is handed to the Boss** by §3's route, one tree per command, and verified by
`test -e` from the session; his terminal holds its output, and the report says who ran it.

---

## 10. Pre-send checks

Performed by the Architect on 2026-10-28 and 2026-10-29 against this file, start to end, in a reading separate from its
writing. Every committed file was read at `origin/main` `5efec8fe25f452963fc51c87c03aa9fcc9b0e985`, which `main` still
carried at 03:40 UTC on 2026-10-29; Appendix A's three files at §0.1's SHA-256.

| # | check | result |
|---|---|---|
| **C1** | scope against body | **Named by the body:** 4 repository paths written — Appendix A's three on the branch, the report on `main`; 11 read by name — this TZ, `research/tz28-pairbook-archive-timer.py`, `research/tz27-pairbook-archive.py`, `research/tz33-reward-book-capture.py`, the five units §0.3 compares, `SYSTEM-MAP.md` and the contract — and the 46 files of map §0's table, by `fingerprint`; 2 reported only — `ADVISOR-SKILL.md` and `.github/workflows/adv2-signal.yml` (§0.5). Refs: the branch and `rewardbook-streams-<A>` written; `tz-01a-dataset` and `tz-27-pairbook-streams` read. Entry points: this file's 14 modes; TZ-28's `path` and `path-token`; TZ-27's `scratch` and `reclaim`; the reward book's `stream_bytes_total`, run from its text by the self-test. Outputs: `/root/tz34-work/**`; the service's four files; the unit's ledger, `runs/<A>/`'s five files, `run.lock` and `archive.log`; the two units and the enable link; §9's copies; the Release's assets; the report. **Intersections with §2's prohibitions, by path and by content class — 10, each exempted by name in §2:** the Release's assets, stream bodies, × item 11 — allowed item 3 and item 11's own text; the unit's writes × item 4 — "the named exemption"; the set's removal × item 5 — "the named exemption"; the reads of `runtime.jsonl` and `slot.json` and §3.9's `tail` of `service.log` × item 5 — named there, their content map §2.6's exceptions to the reserve; P-PATH's download, Binance prices, and the verify's, stream bodies, × item 11 — hashed as they arrive and written nowhere, item 11's text; the run's records and `archive.log` × item 11 by class — names, bytes, SHA-256, times and statuses, every record asserted against TZ-27's forbidden keys; §0.3's reads under the recorder's root × item 2; the `du` and `stat` of the pair book's store and its archive's state × items 3 and 4; the blocks of §3 and §4.8 × item 6; §9's copies, the report, the requests and P-TOKEN × items 7 to 10, each named in its item. **Removed in this reading:** item 2 counted B-RECLAIM-OWN's `df`, of `/var/lib`, among the reads of the recorder's root. |
| **C2** | origin of every expectation | **Every fixed literal of §5 and §7, of two kinds and no third.** *Quoted from a committed artifact, named:* revision `2026-10-28-a`, anchors `6` and `4` re-derived, rows `46` and `43` `frozen` (map §0; tz27 lines 70 to 74); `46a019d6…` and `2cba96bc…` (map §0); `a276bbb9…` (map §2.6); `76,818,669` bytes and `sha256:229a944f…` (map §2.1); `409534533` (map §2.5; tz28 line 117); `3` requests at `path` (tz28 line 780) and `2` at `path-token` (tz28 lines 795 and 801); exits `75` and `2` (tz28 lines 95 and 96), and `0`, `1` and `3` (Appendix A lines 1075 to 1094 and 1749 to 1791); the three paths, each `A` (§2 item 1); B-INSTALL's `7` lines, the band `15` to `480` and `26,100` to `68,400`, B-RETRY at most once, and the `0`s of V11 and V12 — this TZ's own text and contract §4.2; V2's, which are §0.3's — `/dev/vda2` and `31612203008` (map §6), the two commits and three SHA-256 of H4 (map §1, §3 and §0), and the memory and disk gates, `2 × 60,338,176` and `2,200,000,000 + 100,000,000`, derived in §0.4 from the Architect's measured peak and service line 189. *Computed by an implementation independent of the one under test:* §0.1's three SHA-256, lines and bytes — `sha256sum` and `wc` over the files, Python's `hashlib` over the blocks the script extracts; `49` — 48 `ok` sites in the self-test (lines 1335 to 1744), one inside a loop over the two units (lines 1458 to 1466), counted from the text; `9`, `9` and `8` — the keys of G-INSTALL's checks (lines 929 to 946), G-TIMER's (lines 980 to 988) and `first`'s readings (lines 1100, 1106, 1121, 1130, 1139, 1152, 1167 and 1179), counted from the text; `13` — `RESTATED`'s keys (lines 126 to 129); `15` — the self-test stores' sets, counted from their `slot` calls (lines 1530 to 1722): `4 + 1 + 1 + 1 + 2 + 1 + 2 + 3`. Each computed count is also the number of checks or files the Architect's runs print. **The third kind, found and rewritten:** V11 read `2 + ⌊n/100⌋` requests at `first`, and `1` store open and one a `slot.json` read — both on quantities the run measures; now inequalities over every admissible value: `2` to `6` for a set of 1 to 400 files, and at least `1`. V8's `ROW` n of n and V14's after-equals-before-plus-copies relate two counts the run prints and fix no literal. |
| **C3** | shape of every diff | **None replaced.** No file is called additive. The four repository files the TZ writes are each absent from `origin/main` at `5efec8f` — `git cat-file -e` exit `1` for each — Appendix A's three, `A` in V3's diff, and the report. The words "insertions only" appear nowhere. |
| **C4** | cost of every check | At the population's upper bound — a set of 400 files and `4,300,000,000` bytes, `first` at most 171 runs (§6): `selftest` `2.04` to `2.33` s, seven runs on these bytes; `fingerprint`, `installed`, `mark`, `timer`, `still`, `scratch`, `final`, `stopped`, each `reclaim` and each `first` under 1 s; `path` 3 requests and `76,818,669` bytes hashed in `0.25` s; **the session's processor under `190` s** — `2.3 + 0.25 + 0.01 + 184 × 1` — under `3,600`, so nothing is sampled. The run is the unit's: `20,619` s, derived term by term at `RATE_FLOOR` and TZ-27's measured hash rate (§6), against `TimeoutStartSec` `21,600`. **Fail-fast bounds, each derived beside it:** G-TIMER within 300 s of `E`; G-TRIGGER FAIL at `E + 5,400` — the timer's `1,800` s and `3,600` s for reloads by other units; `first`'s last read at most `E + 28,840` — `5,400 + 21,600 + 1,840`, the run's latest start, its bound, and G-NEXT's 900 s to the next decision, 910 s to its `slot.json` and 30 s; `path`'s wait at most `900` s; the hold and the quiet at most `1,800` s each, then a deferral. |
| **C5** | every count | V1: anchors `6` and `4` re-derived, over map §0's anchor table and `ANCHOR_FILES` (tz27 lines 73 and 74); rows `46 = 43 + 2 + 1`, over map §0's table, which `fingerprint` read at `5efec8f`: PASS. V3: `3`, over Appendix A's blocks and over the branch's diff. V4: `49`, over the self-test's calls of `ok`. V5: `3`, over P-PATH's requests — the Release, one page of its one asset, the download. V6: `7`, over §3.5's lines; `9`, over G-INSTALL's checks. V7: `2`, over P-TOKEN's requests — the repository, the Release on `tz-27-pairbook-streams`; `9`, over G-TIMER's checks. V8: `8`, over `first`'s readings — G-TRIGGER and G-RUN, then six under `complete`. V11: `15`, over the removals of the self-test's nineteen runs on nine stores — `one` `4 + 1`, `defer` `1`, `halt` `1`, `verify` `2`, `select` `1`, `quiet` `2`, `partial` `2 + 1`, `changed` and `hold` `0`. V15: `2`, over map §3's worktrees once §9 has run. |
| **C6** | every population | Each of §4's 13 gates names its population in its own column. §0.4's peaks: per mode, over the Architect's runs under Python 3.12.3 — `selftest` 25, the run 9, `first` 4, the six other session modes 25, `fingerprint` those of 2026-10-28. §6's figures: the self-test over its seven runs on these bytes; the run over nine runs of 400 stream files and `2,182,530,000` bytes; `first` over one 400-asset Release. V8's lines: `R` over the run's records; `SLOT` over its slots considered; `S` and `ROW` over its files; `T` over its requests; `X` over its removals; `ACROSS` over the slots its records span; G-NEXT over the slots decided from its first removal to 900 s after its last. `final`'s projection over the last `complete` run's set — printed, never gated. |
| **C7** | every signature and every behaviour | Read at `5efec8f`, as the files hold them — tz27: `def credential():` (725), `def build_request(method, url, token=None, accept=ACCEPT_API, data=None, ctype=None, length=None):` (509), `def opener(follow):` (505), `class GitHub:` (559) with `def _json(self, method, url, body=None):` (569), `def upload(self, rid, name, path, nbytes):` (618) and `def download(self, url):` (641), `def upload_set(gh, rel, doc, root, log, wait_min=WAIT_MIN_S):` (765), `def wait_for(status, hdr, attempt, wait_min=WAIT_MIN_S):` (742), `def sha256_file(path, chunk=1 << 20):` (293), `def floor_check():` (324), `def assert_keys(obj, allowed, what):` (343), `def policy(mode, event, args, work, allowed):` (212), `def processes_with(argv):` (994), `def proc_start_times():` (1428), `def mode_scratch(own):` (1453), `def reclaimable(tree):` (1491), `def mode_reclaim(trees):` (1499); tz28: `def load_tz27(path):` (63), `def budget_s(nbytes):` (135), `def idle_wait(env, budget):` (140), `def transfer_ok(t):` (164), `def halted(recs):` (223), `def pending(recs):` (229), `def release_request(tag, commit, name, body):` (306), `class Gh28(tz27.GitHub):` (312), `def verify_phase(env, led, a, rdir, doc):` (479), `def halt(env, led, a, phase, reason):` (599), `def mode_path():` (756), `def mode_path_token():` (785), `def first_run(recs, since_ns):` (905); the reward book: `def stream_bytes_total(root):` (1279), `def stream_off_reason(selected, n_members, free, total):` (1294), `async def run_slot(book, sched, ws_url=CLOB_WS_URL, kw=None, ping_s=PING_S, backoff=BACKOFF_S, poll_url=CLOB_REWARDS_URL, poll_getter=None, join_last=None):` (1514), `async def selection_for(self, d0, deadline):` (1504), `async def guarded(book, coro, what):` (1580), `async def serve_main(root=None, urls=None, slots=None):` (1597), `def flush(self):` (1143). **Each attributed behaviour against the lines that implement it:** the token's source — `tok = token_of(cp.stdout)`, `return tok, "the primary checkout's remote URL"` (tz27 730 and 732); no redirect with a token — `self.op = opener(follow=token is None)` (tz27 565); the token to the API and uploads hosts alone — `_json` on `self.api`, `upload` on `self.uploads`, `download`'s `build_request("GET", url, accept=ACCEPT_BLOB)` with none (tz27 571, 622 and 643); an asset kept where it matches — `if a is not None and matches(a, x):` `held += 1` (tz27 775 and 776); pieces of 1 MiB — `chunk=1 << 20` (tz27 293); every request held to the stretch — `idle_wait(self.env, budget)` (tz28 322), `if IDLE[0] <= p <= IDLE[1] - budget:` `return now` (tz28 147 and 148); the budget — `return MARGIN_S + -(-int(nbytes) // RATE_FLOOR)` (tz28 137); G-IDLE — tz28 169; resume — `return None if any(r.get("run") == a and r.get("event") in TERMINAL for r in recs) else a` (tz28 235); the Release at the run's commit, never the latest — `"target_commitish": commit` and `"make_latest": "false"` (tz28 308 and 309); the verify anonymous and 120 s after the upload — tz28 484 to 487; the halt disables this archive's timer — `rc = env.disable_timer()` (tz28 602) on this file's `Env.disable_timer`, `TIMER` (lines 527 and 528); P-PATH's 3 requests — `assert len(trs) == 3 and all(all(transfer_ok(t)) for t in trs)` (tz28 780); P-TOKEN's source, push and Release — tz28 791, 799 and 802; the first run after a mark — tz28 907 to 911; the sum by listing, then `stat` — `os.scandir` … `total += f.stat(follow_symlinks=False).st_size` (service 1284 to 1290); the floor and the cap — `if free < STREAM_FLOOR:` and `if total >= STREAM_CAP:` (service 1300 and 1302); the start's sum outside any handler — `total = stream_bytes_total(root)` (service 1615); a slot's error record — `runtime_record(book.root, "error", {"what": what, …})` (service 1593); the selection polled each second — `await sleep_until(min(deadline, time.time() + 1))` (service 1510); a stream cut at a flush — `if self.stored >= self.slot_max:` `self.cut = True` (service 1148 and 1149); `scratch`'s live window — `a0 == "claude" or a0.endswith("/claude.exe")` and `t - 1 <= b <= t + LIVE_S` (tz27 1442 and 1463); `reclaim`'s refusals — tz27 1494 to 1496 and 1505. **Rewritten in this reading:** four citations widened to the lines that implement their sentences — §1's credential, its halt and its trigger record, and §3.3's `scratch` — and three of §1's deadline citations named as the service's, which that section's rule would have read as Appendix A's. |
| **C8** | every cross-reference | Resolved by reading each referenced text: **51** references to the map — §0, §1, §2.1, §2.5, §2.6, §3, §6's rows (host identity, git remote, memory, process supervision, the sandbox's destructive actions, GitHub Releases, headroom, the consumer) and §7 items 106, 114, 115, 118, 119, 120, 124 and 125; **10** to the contract — §1, §3.3, §4.2, §5.1 and §8; **6** to the CANON — hard rules 11, 14 and 15 and PART II's L track; **1** to TZ-27's §2, whose rule tz27's hook states (tz27 line 171); **113** to this TZ's own sections, each to a section that exists; **111** file-and-line citations — 46 to `tz27`, `tz28`, the reward book's file and its unit, 65 to Appendix A — each read at both ends against its sentence. **Corrected in this reading:** §3.1 named TZ-29 to TZ-32 as pushing through `gh`, where map §6 and item 114 name TZ-29 to TZ-31, and TZ-33's push went through the URL's own credential; §4.2 grounded the credential's source in a unit's `HOME`, which no cited text carries — now item 114's upload records; `I` named both the instrument and the instant of B-INSTALL's `daemon-reload` (§3, §3.5, §8) — the instant is now `L`; §0.3's printed list omitted two paths its `du` reads; §0.4's peaks now carry the Architect's later runs on these bytes. |

**Performed in the Architect's session, on these bytes:** §0.1's script on this file, its three hashes; `selftest`, `49 of
49`, seven runs; `fingerprint` against a clone of `origin/main` at `5efec8f`, PASS; the run nine times — the last three
on these bytes — against stores of 400 stream files and `2,182,530,000` bytes and a loopback GitHub over TLS in another
process, every request and removal inside the idle stretch, `complete`; and `first`, `final`, `still`, `timer`,
`stopped`, `installed` and `mark` against those runs, with systemd, git and the tag stood in for.

**Not performable in this session, and converted to conditions the Executor evaluates and BLOCKS on** (CANON hard rule
13): the host — H1 to H5, the memory and the disk gates (§0.3) and §0.5's three refs conditions; the host's own path to
GitHub — P-PATH (§3.4); the credential — P-TOKEN inside B-ENABLE, chained by `&&` before the enable, B-UNINSTALL where
it fails (§3.6); systemd's reading of the two units on the host's version — `systemd-analyze verify` and G-INSTALL
(§3.5), and G-TIMER within 300 s of `E`, K-34 then B-UNINSTALL (§3.6); the credential's write half — the first run's own
creation of its Release, a refusal deferring with nothing removed, read by G-RUN, B-RETRY once, then K-34 (§3.7);
whether the host's systemd hands a unit `TRIGGER_UNIT` — G-TRIGGER reads `LastTriggerUSec` where it does not, and prints
which it read (§4.5); and the reward book's live records against the quiet — G-NEXT over the slots decided across the
removals, K-34 on FAIL, and B-START-RB where the reward book is down (§4.8).

---

## Appendix A — the instrument and the two units, byte for byte

Extracted by §0.1's script; each block's content is the file.

### `research/tz34-rewardbook-archive-timer.py`

```python file=research/tz34-rewardbook-archive-timer.py
#!/usr/bin/env python3
"""TZ-34 - the reward book's archive on a timer: the stream files of its closed slots moved verbatim to a Release
once a day by btc-rewardbook-archive.timer, through TZ-27's proofs and TZ-28's idle stretch and ledger, every
request and every removal inside the pair book's idle stretch.

    run               the unit's one mode, ExecStart of btc-rewardbook-archive.service: a new set as of now, or the
                      pending one resumed; the upload and the verify through TZ-27's and TZ-28's own functions, then
                      each file hashed again and removed while the reward book is not about to read its store's
                      sizes; one record a step in /var/lib/btc-rewardbook-archive/ledger.jsonl. Exit 0 complete or
                      empty; 75 deferred - the next run resumes it; 1 halted - the run disables its own timer; 2 not
                      started
    fingerprint       map section 0 against the primary checkout
    selftest          every rule of this file, on literals, temporary stores, a simulated reward book and a loopback
                      server only
    path              P-PATH, TZ-28's own: the run's request path with no token, held to the idle stretch
    path-token        P-TOKEN, TZ-28's own and the Boss's alone: the run's credential reads the repository, with push
    installed         G-INSTALL: the service's four files, the two units and the empty state directory
    mark NAME         enable, retry or stop: an instant and the archive's two units into state.json
    timer             G-TIMER: the timer as installed and enabled, and its next calendar elapse
    first             the first run after the enable mark, re-read: G-TRIGGER, G-RUN and the run's own readings;
                      exit 3 NOT YET
    final             G-TIMER and G-STILL; the store and the next stop, projected
    still             the recorder, the pair book and the reward book: the first run records them, a later run
                      compares (G-STILL)
    stopped           after K-34: the timer disabled, no run in progress
    scratch OWN, reclaim TREE...   TZ-27's own modes, unchanged

TZ-28's instrument, research/tz28-pairbook-archive-timer.py, is loaded from beside this file and asserted by its
SHA-256; it loads TZ-27's from beside itself the same way, and TZ-27's audit hook is installed then. This file points
that hook at the reward book's store and adds its own for the rest of TZ-34 section 2. No mode decompresses a stream
file, and none opens a rewards file or a selection; none prints a price, a size, a side, a book's hash, a rate or an
outcome. Run it with /root/tz04a-env; it needs the standard library alone.

Written for CryptoTZ/TZ-34-rewardbook-archive-timer.md. The TZ is the specification.
"""

import ast
import fcntl
import hashlib
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
import types
from fractions import Fraction

if not __debug__:
    sys.stderr.write("tz34: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(1)

HERE = os.path.dirname(os.path.abspath(__file__))
SELF_NAME = "tz34-rewardbook-archive-timer.py"
TZ28_NAME = "tz28-pairbook-archive-timer.py"
TZ28_SHA256 = "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4"
TZ27_NAME = "tz27-pairbook-archive.py"
TZ27_SHA256 = "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673"
TZ33_NAME = "tz33-reward-book-capture.py"
TZ33_SHA256 = "a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670"


def load_tz28(path):
    """TZ-28's instrument, executed from the very bytes whose SHA-256 is asserted. It loads TZ-27's from beside
    itself by TZ-27's SHA-256, and TZ-27's audit hook is installed then."""
    with open(path, "rb") as fh:
        raw = fh.read()
    got = hashlib.sha256(raw).hexdigest()
    assert got == TZ28_SHA256, "%s sha256 %s, required %s" % (path, got, TZ28_SHA256)
    mod = types.ModuleType("tz28")
    mod.__file__ = path
    sys.modules["tz28"] = mod
    exec(compile(raw, path, "exec"), mod.__dict__)
    return mod


tz28 = load_tz28(os.path.join(HERE, TZ28_NAME))
tz27 = tz28.tz27
assert tz28.TZ27_SHA256 == TZ27_SHA256 and tz27.__file__ == os.path.join(HERE, TZ27_NAME), "TZ-27's file"
out = tz27.out

# ---- the TZ's constants: none of them is measured by this run -----------------------------------------------

MAP_REVISION = "2026-10-28-a"
MAP_ROWS = {"frozen": 43, "tracked": 2, "reported": 1}

ROOT = "/var/lib/btc-rewardbook"             # the reward book's store (TZ-33 section 1)
PAIRBOOK = "/var/lib/btc-pairbook"
PAIR_STATE = "/var/lib/btc-pairbook-archive"
PAIR_LEDGER = PAIR_STATE + "/ledger.jsonl"
STATE = "/var/lib/btc-rewardbook-archive"
ASVC = "/root/btc-rewardbook-archive-svc"
ARCHIVE = "btc-rewardbook-archive.service"
TIMER = "btc-rewardbook-archive.timer"
REWARD_UNIT = "btc-rewardbook.service"
PAIR_ARCHIVE = "btc-pairbook-archive.service"
PAIR_TIMER = "btc-pairbook-archive.timer"
UNITS = {"recorder": "btc-recorder.service", "pairbook": "btc-pairbook.service", "rewardbook": REWARD_UNIT}
UNIT_DIR = "/etc/systemd/system"
RUN_ARGV = (tz27.PYTHON, "-B", "-u", ASVC + "/" + SELF_NAME, "run")
CALENDAR = "*-*-* 01:30:20 UTC"
CALENDAR_S = 1 * 3600 + 30 * 60 + 20       # the calendar elapse, seconds after 00:00 UTC
ACTIVE_S = 1800                            # OnActiveSec: the first run, 1,800 s after the timer starts
TIMEOUT_S = 21600                          # TimeoutStartSec of the service
ARCHIVE_MEMORY_MAX = 134217728             # MemoryMax=128M
RUNNING = ("active", "activating", "deactivating", "reloading", "refreshing")

# the reward book's own, restated from research/tz33-reward-book-capture.py and asserted against its text by the
# self-test: lines 114, 120, 133 to 135, 143, 168, 169, 171, 173, 190 to 192, 227 and 228
REWARD_SVC = "/root/btc-rewardbook-svc"
REWARD_ARGV = (tz27.PYTHON, "-B", "-u", REWARD_SVC + "/" + TZ33_NAME, "serve")
DAY = 86400
SLOT = 900
OPEN_BEFORE = 5
SLOT_JSON_AT = 910
LAUNCH_LEAD = 1
STREAM_FLOOR = 7300000000
STREAM_CAP = 4000000000
SLOT_STREAM_MAX = 100000000
DAY_RE = re.compile(r"[0-9]{10}")
SLOT_FILE_RE = re.compile(r"([0-9]{10})\.([0-9]+)\.(stream\.jsonl\.gz|rewards\.jsonl\.gz|slot\.json)")
RESTATED = {"ROOT": ROOT, "SVC": REWARD_SVC, "SERVICE_ARGV": REWARD_ARGV, "DAY": DAY, "SLOT": SLOT,
            "OPEN_BEFORE": OPEN_BEFORE, "SLOT_JSON_AT": SLOT_JSON_AT, "LAUNCH_LEAD": LAUNCH_LEAD,
            "STREAM_FLOOR": STREAM_FLOOR, "STREAM_CAP": STREAM_CAP, "SLOT_STREAM_MAX": SLOT_STREAM_MAX,
            "DAY_RE": DAY_RE.pattern, "SLOT_FILE_RE": SLOT_FILE_RE.pattern}

# this TZ's own
SETTLE_S = 60                     # a slot is taken once its slot.json was due at least 60 s before A
DECIDE_S = OPEN_BEFORE + LAUNCH_LEAD    # the reward book decides a slot's stream at S - 6
SELECT_AGE_S = 5                  # the day's selection recorded at least 5 s before a removal
START_AGE_S = 10                  # the reward book's process started at least 10 s before a removal
QUIET_STEP_S = 1
QUIET_MAX_S = 1800                # the removals wait at most this in all for the reward book's quiet, then defer
HOLD_STEP_S = 10
HOLD_MAX_S = 1800                 # a phase waits at most this while the pair book's archive runs, then defers
NEXT_AFTER_S = 900                # G-NEXT: the slots decided from the first removal to 900 s after the last
NEXT_SETTLE_S = 30                # read 30 s after each one's slot.json is due
DISK_FLOOR = 2002000000           # the recorder's floor, 2,000,000,000, plus 2,000,000 a run writes at most
RUN_MEM_FLOOR = 73121792          # MemAvailable: twice the run's measured peak (TZ-34 section 0.4)
PRE_DELETE = ("set", "upload", "verify")

TAG_PREFIX = "rewardbook-streams-"
TAG_RE = re.compile(r"rewardbook-streams-[0-9]{10}")
ASSET_RE = re.compile(r"([0-9]{10})-(([0-9]{10})\.([0-9]+)\.stream\.jsonl\.gz)")
STREAM_PATH_RE = re.compile(r"[0-9]{10}/[0-9]{10}\.[0-9]+\.stream\.jsonl\.gz")
SLOT_JSON_PATH_RE = re.compile(r"[0-9]{10}/[0-9]{10}\.[0-9]+\.slot\.json")

SET_KEYS = frozenset(("tag", "as_of", "root", "repo", "assets", "assets_n", "bytes_total", "first_S", "last_S",
                      "slots", "deferred"))
SET_ASSET_KEYS = frozenset(("T", "S", "k", "file", "asset", "bytes", "sha256"))
SET_SLOT_KEYS = frozenset(("S", "disposition", "streams", "stream_bytes", "taken"))
DELETE_ROW_KEYS = frozenset(("asset", "T", "S", "k", "file", "bytes", "sha256", "start_ns", "removed_wall_ns"))

# ---- TZ-27's hook, pointed at the reward book's store; and this file's own -------------------------------------
#
# TZ-27's policy reads its module's ROOT at every event: rebound here, before any mode acts, it guards the reward
# book's store as TZ-27 section 2 guarded the pair book's - read by its READ_MODES, listed by its LIST_MODES, never
# written, a file removed only in mode delete and only where the run names it - and the pair book's store, which it
# no longer names, is refused by policy34 below.

tz27.ROOT = ROOT
assert tz27.ROOT == ROOT and tz28.tz27 is tz27

REFUSED34 = []


def _rel(p, root):
    return p[len(root) + 1:] if p.startswith(root + "/") else ""


def policy34(mode, event, args):
    """None where TZ-34 section 2 allows the event in this mode, beside TZ-27's hook; otherwise the reason."""
    p = tz27._path(args[0]) if args else None
    if event == "open":
        if p is None:
            return None
        wm, fl = (args[1] if len(args) > 1 else None), (args[2] if len(args) > 2 else None)
        w = tz27._writing(wm, fl)
        if tz27._under(p, PAIRBOOK):
            return "the pair book's store"
        if tz27._under(p, PAIR_STATE):
            if p == PAIR_LEDGER and not w and mode == "still":
                return None
            return "the pair book's archive"
        if tz27._under(p, ROOT):
            if w:
                return "a write under the reward book's store"
            rel = _rel(p, ROOT)
            if STREAM_PATH_RE.fullmatch(rel):
                return None if mode in ("inventory", "upload", "delete") else "a stream file read in mode %s" % mode
            if SLOT_JSON_PATH_RE.fullmatch(rel):
                return None if mode == "final" else "a slot.json read in mode %s" % mode
            if rel == "runtime.jsonl":
                return None if mode in ("delete", "final") else "runtime.jsonl read in mode %s" % mode
            return "a file of the reward book's store this TZ never reads"
        return None
    if event in ("os.listdir", "os.scandir"):
        if p is None:
            return None
        if tz27._under(p, PAIRBOOK) or tz27._under(p, PAIR_STATE):
            return "a listing under the pair book's store or its archive"
        if tz27._under(p, ROOT):
            return None if mode in ("inventory", "delete", "final") else "a listing under the reward book's store"
        return None
    if event in tz27.CHANGE_EVENTS:
        paths = [p]
        if event in ("os.rename", "os.link", "os.symlink") and len(args) > 1:
            paths.append(tz27._path(args[1]))
        for q in paths:
            if q is None:
                continue
            if tz27._under(q, PAIRBOOK) or tz27._under(q, PAIR_STATE):
                return "a change under the pair book's store or its archive"
            if tz27._under(q, ROOT):
                if (event == "os.remove" and mode == "delete" and q in tz27.ALLOWED_REMOVE
                        and STREAM_PATH_RE.fullmatch(_rel(q, ROOT))):
                    continue
                return "a change under the reward book's store"
        return None
    return None


def _audit34(event, args):
    if event not in tz27.HOOKED:
        return
    why = policy34(tz27.MODE[0], event, args)
    if why is not None:
        REFUSED34.append((event, str(args[0]) if args else ""))
        raise tz27.GuardError("%s refused in mode %s, %s: %r" % (event, tz27.MODE[0], why, args[0] if args else None))


sys.addaudithook(_audit34)

# ---- the reward book's store, by its own names --------------------------------------------------------------


def day_of(t):
    return int(t) // DAY * DAY


def day_dirs(root):
    """The day directories under root - ten digits, a multiple of 86,400 - in order."""
    with os.scandir(root) as it:
        names = [d.name for d in it if d.is_dir(follow_symlinks=False) and DAY_RE.fullmatch(d.name)]
    for n in names:
        assert int(n) % DAY == 0, "a day directory named %r" % n
    return sorted(int(n) for n in names)


def slot_files(names, d0):
    """A day directory's slot files by slot: {S: {"streams": [(k, name)], "closed": bool}}; every slot in its day."""
    by = {}
    for n in names:
        m = SLOT_FILE_RE.fullmatch(n)
        if m is None:
            continue
        s, k, kind = int(m.group(1)), int(m.group(2)), m.group(3)
        assert s % SLOT == 0 and day_of(s) == d0, "%s in the day directory %d" % (n, d0)
        e = by.setdefault(s, {"streams": [], "closed": False})
        if kind == "stream.jsonl.gz":
            e["streams"].append((k, n))
        elif kind == "slot.json":
            e["closed"] = True
    return by


def inventory(root, a, max_assets=tz27.RUN_MAX_ASSETS):
    """The set as of the epoch a: every stream file of every slot that holds a slot.json and whose slot.json was due
    at least SETTLE_S before a - S + 910 + 60 <= a - in order of S and of the file's index; the first max_assets
    taken, each read as bytes for its SHA-256, its size and mtime equal before and after. The slots considered are the
    slots due by a that hold a stream file, each closed or unclosed; a slot due after a is counted as open, a slot due
    by a with no stream file as streamless, and neither is listed, so the set is a function of a alone."""
    slots, files, open_n, streamless = [], [], 0, 0
    for d0 in day_dirs(root):
        by = slot_files(tz27.window_names(root, d0), d0)
        for s in sorted(by):
            if s + SLOT_JSON_AT + SETTLE_S > a:
                open_n += 1
                continue
            streams = sorted(by[s]["streams"])
            if not streams:
                streamless += 1
                continue
            sizes = [os.stat(os.path.join(root, str(d0), n), follow_symlinks=False).st_size for _k, n in streams]
            disp = "closed" if by[s]["closed"] else "unclosed"
            slots.append({"S": s, "disposition": disp, "streams": len(streams), "stream_bytes": sum(sizes),
                          "taken": 0})
            if disp == "closed":
                files.extend((d0, s, k, n) for k, n in streams)
    taken, assets = files[:max_assets], []
    for d0, s, k, n in taken:
        p = os.path.join(root, str(d0), n)
        before = os.stat(p, follow_symlinks=False)
        h, nbytes = tz27.sha256_file(p)
        after = os.stat(p, follow_symlinks=False)
        assert before.st_size == nbytes == after.st_size and before.st_mtime_ns == after.st_mtime_ns, \
            "%s changed while it was read" % p
        assets.append({"T": d0, "S": s, "k": k, "file": n, "asset": "%d-%s" % (d0, n), "bytes": nbytes, "sha256": h})
    for e in slots:
        e["taken"] = sum(1 for _d, s, _k, _n in taken if s == e["S"])
    return assets, slots, len(files) - len(taken), open_n, streamless


def stream_bytes_view(root):
    """The service's own stream_bytes_total (research/tz33-reward-book-capture.py lines 1279 to 1291), restated:
    the bytes of every stream file under root, by directory entries alone."""
    total = 0
    if not os.path.isdir(root):
        return 0
    with os.scandir(root) as it:
        dirs = sorted(d.path for d in it if d.is_dir(follow_symlinks=False) and DAY_RE.fullmatch(d.name))
    for d in dirs:
        with os.scandir(d) as it:
            for f in it:
                if f.name.endswith(".stream.jsonl.gz") and SLOT_FILE_RE.fullmatch(f.name):
                    total += f.stat(follow_symlinks=False).st_size
    return total


def set_document(tag, a, root, assets, slots, deferred):
    """The set under this TZ's tag, which neither TZ-27's nor TZ-28's tag rule covers, every file small enough for one
    idle stretch."""
    names = [x["asset"] for x in assets]
    assert TAG_RE.fullmatch(tag) and tz27.TAG_RE.fullmatch(tag) is None and tz28.TAG_RE.fullmatch(tag) is None, \
        "a tag named %r" % tag
    assert assets, "no stream file of a closed slot"
    assert len(set(names)) == len(names), "two assets share a name"
    for x in assets:
        m = ASSET_RE.fullmatch(x["asset"])
        assert m is not None and int(m.group(1)) == x["T"] == day_of(x["S"]) and m.group(2) == x["file"] \
            and int(m.group(3)) == x["S"] and int(m.group(4)) == x["k"], "an asset named %r" % x["asset"]
    assert len(assets) <= tz27.RUN_MAX_ASSETS, "%d assets, above %d" % (len(assets), tz27.RUN_MAX_ASSETS)
    big = [x["asset"] for x in assets if x["bytes"] > tz28.IDLE_MAX_BYTES]
    assert not big, "files above the %d bytes one idle stretch carries: %r" % (tz28.IDLE_MAX_BYTES, big[:3])
    doc = {"tag": tag, "as_of": a, "root": root, "repo": tz27.REPO, "assets": assets, "assets_n": len(assets),
           "bytes_total": sum(x["bytes"] for x in assets), "first_S": assets[0]["S"], "last_S": assets[-1]["S"],
           "slots": slots, "deferred": deferred}
    tz27.assert_keys(doc, SET_KEYS, "set.json")
    for x in assets:
        tz27.assert_keys(x, SET_ASSET_KEYS, "set.json asset")
        assert tz27.SHA_RE.fullmatch(x["sha256"])
    for e in slots:
        tz27.assert_keys(e, SET_SLOT_KEYS, "set.json slot")
    return doc


def release_text(doc, commit):
    name = "%s: the reward book's streams, slots %d to %d" % (doc["tag"], doc["first_S"], doc["last_S"])
    body = ("Verbatim stream files of btc-rewardbook.service (research/tz33-reward-book-capture.py), one asset per "
            "file, named <D0>-<S>.<k>.stream.jsonl.gz: the CLOB market websocket's frames for both tokens of each UTC "
            "day's 150 reward markets, S-5 to S+905. %d files, %d bytes, slots %d to %d, taken as of %d by "
            "btc-rewardbook-archive.service at commit %s (research/tz34-rewardbook-archive-timer.py, TZ-34). Reserved "
            "for L0's measurement: until it, no TZ extracts a price, a size, a side, a book's hash, a rate, a "
            "competitiveness or an outcome from them (CANON PART II). Each asset's SHA-256 is its digest here." % (
                doc["assets_n"], doc["bytes_total"], doc["first_S"], doc["last_S"], doc["as_of"], commit))
    return name, body


def slot_names(root, s):
    """The slot.json names of slot s in its day directory, by index."""
    d0 = day_of(s)
    if not os.path.isdir(os.path.join(root, str(d0))):
        return []
    found = []
    for n in tz27.window_names(root, d0):
        m = SLOT_FILE_RE.fullmatch(n)
        if m is not None and int(m.group(1)) == s and m.group(3) == "slot.json":
            found.append((int(m.group(2)), n))
    return sorted(found)


def removed_reading(root, doc, done):
    """G-DELETE read back, removing nothing: every file of the set absent, its removal recorded, and each of its
    slots still holding its slot.json."""
    slots = sorted({x["S"] for x in doc["assets"]})
    gone = [x for x in doc["assets"] if not os.path.lexists(os.path.join(root, str(x["T"]), x["file"]))]
    kept = [s for s in slots if slot_names(root, s)]
    return {"every file of the set absent": len(gone) == doc["assets_n"],
            "each removal recorded": all(x["asset"] in done for x in doc["assets"]),
            "each slot keeps its slot.json": kept == slots}, len(gone), len(kept)


def projection(bytes_total, first_s, last_s, counter, free, now):
    """The streams' rate over the set's span, and the instants at which the reward book's cap and floor stop them
    again; printed, never gated."""
    rate = Fraction(bytes_total * 86400, last_s - first_s + SLOT)
    cap_days = Fraction(STREAM_CAP - counter) / rate if counter < STREAM_CAP else Fraction(0)
    rows = [("the cap", cap_days)]
    for base in tz27.BASE_DRAINS:
        d = Fraction(free - STREAM_FLOOR) / (rate + base) if free > STREAM_FLOOR else Fraction(0)
        rows.append(("the floor, base %d bytes a day" % base, d))
    return rate, [(what, d, now + int(d * 86400)) for what, d in rows]


def removal_span(row):
    """A removal as G-IDLE reads a request: its start, its end and its budget."""
    return {"start_ns": row["start_ns"], "end_ns": row["removed_wall_ns"], "budget_s": tz28.budget_s(row["bytes"])}

# ---- the reward book, read: its quiet before a removal, its slots after it, and G-STILL ------------------------


def quiet(recs, pids, now):
    """None where a removal may start at `now`; else why it waits. The reward book sums its store's stream files at a
    slot's decision, S - 6 - later only while the day's selection is missing - and at a process's start: the day of
    the slot it streams has its selection recorded at least SELECT_AGE_S ago, and no process runs under its argv but
    the one whose start record is at least START_AGE_S old."""
    d0 = day_of(now)
    sel = [r for r in recs if r.get("event") == "select" and r.get("day") == d0 and r.get("ok") is True]
    if not sel or sel[0].get("wall_ns", 0) > (now - SELECT_AGE_S) * 10 ** 9:
        return "the selection of day %d not recorded %d s before" % (d0, SELECT_AGE_S)
    if pids:
        starts = [r for r in recs if r.get("event") == "start"]
        if not starts or sorted(pids) != [starts[-1].get("pid")]:
            return "a process of the reward book, %r, without its start record" % sorted(pids)
        if starts[-1].get("wall_ns", 0) > (now - START_AGE_S) * 10 ** 9:
            return "the reward book's process started less than %d s before" % START_AGE_S
    return None


def next_slots(first_ns, last_ns):
    """The slots whose decision instant S - 6 lies from the run's first removal to NEXT_AFTER_S after its last: those
    the reward book decided while the run removed files, and the first it decided after."""
    s = -(-(first_ns + DECIDE_S * 10 ** 9) // (SLOT * 10 ** 9)) * SLOT
    found = []
    while (s - DECIDE_S) * 10 ** 9 < last_ns + NEXT_AFTER_S * 10 ** 9:
        found.append(s)
        s += SLOT
    return found


def next_verdict(sjs, errors, pid0):
    """One slot across the removal, from its slot.json files [(k, doc)] and the error records of its task: FAIL where
    its task left an error record or no slot.json; PASS where the process the run began beside streamed it with no
    reason to keep it off; UNDECIDABLE where it stayed off for a reason the run does not act on, or another process
    ran it."""
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
    """The worst over the slots: FAIL, else UNDECIDABLE, else PASS."""
    vs = [v for v, _w in verdicts]
    return "FAIL" if "FAIL" in vs else ("UNDECIDABLE" if "UNDECIDABLE" in vs or not vs else "PASS")


def trigger_reading(trg, mark_s, s0, last_trigger):
    """G-TRIGGER, pure: the run's own trigger where systemd set it - TRIGGER_UNIT this timer, its elapse at least
    ACTIVE_S after the enable mark, less 2 s for whole-second stamps, and the run's first record within 60 s after it -
    else the timer's LastTriggerUSec read the same way. (PASS, the evidence read, the trigger's second.)"""
    if trg and trg.get("unit") is not None:
        t = int(trg.get("realtime_usec") or 0) // 10 ** 6
        return (trg["unit"] == TIMER and t >= mark_s + ACTIVE_S - 2 and t <= s0 <= t + 60), "TRIGGER_UNIT %s" % (
            trg["unit"],), t
    t = last_trigger
    return (t is not None and t >= mark_s + ACTIVE_S - 2 and t <= s0 <= t + 60), "LastTriggerUSec", t


def still_reading(before, now, restarts):
    """G-STILL from two reads and the pair book's archive's restart records between them: PASS where the recorder and
    the reward book are unchanged and the pair book is unchanged or moved by that archive's own restarts alone - a
    chain of records from the recorded MainPID to the current one, NRestarts one higher at each, the unit active.
    Pure: it reads nothing but its arguments."""
    if now == before:
        return True, "unchanged"
    if now["recorder"] != before["recorder"]:
        return False, "the recorder changed"
    if now["rewardbook"] != before["rewardbook"]:
        return False, "the reward book changed"
    b, n = before["pairbook"], now["pairbook"]
    pid, count = b["MainPID"], int(b["NRestarts"])
    for r in restarts:
        if str(r.get("stopped")) != pid or str(r.get("NRestarts")) != str(count + 1):
            return False, "a restart record that does not follow %s at NRestarts %d: %r" % (pid, count, r)
        pid, count = str(r.get("pid")), count + 1
    if restarts and pid == n["MainPID"] and str(count) == n["NRestarts"] and n["ActiveState"] == "active":
        return True, "the pair book moved by its archive's own restarts alone: %d" % len(restarts)
    return False, "the pair book changed, %d restart records of its archive since the first read" % len(restarts)

# ---- what the run touches outside its own files -------------------------------------------------------------


class Env:
    """The clock, systemd, the reward book's store and record, and GitHub, as the unit's run meets them."""

    def __init__(self, work=STATE):
        self.root, self.state, self.work = ROOT, STATE, work
        self.wait_min, self.gap_s = tz27.WAIT_MIN_S, tz27.UPLOAD_GAP_S
        self.api, self.uploads, self.web = tz27.API_BASE, tz27.UPLOAD_BASE, tz27.WEB_BASE
        self.invocation = os.environ.get("INVOCATION_ID")
        self.trigger = {"unit": os.environ.get("TRIGGER_UNIT"),
                        "realtime_usec": os.environ.get("TRIGGER_TIMER_REALTIME_USEC"),
                        "monotonic_usec": os.environ.get("TRIGGER_TIMER_MONOTONIC_USEC")}
        self.commit, self.file_sha = None, None
        self._rt = (None, [])

    def identity(self):
        """The commit the service's files are from, and this file's SHA-256."""
        with open(os.path.join(ASVC, "commit.txt"), encoding="utf-8") as fh:
            self.commit = fh.read().strip()
        assert re.fullmatch(r"[0-9a-f]{40}", self.commit), "commit.txt %r" % self.commit
        self.file_sha = tz27.sha256_file(os.path.abspath(__file__))[0]

    def time(self):
        return time.time()

    def time_ns(self):
        return time.time_ns()

    def sleep(self, s):
        time.sleep(max(0.0, s))

    def disable_timer(self):
        return subprocess.run(["systemctl", "disable", "--now", TIMER]).returncode

    def credential(self):
        return tz27.credential()

    def free(self):
        return tz27.free_bytes()

    def mem(self):
        return tz27.mem_available()

    def archive_active(self):
        return tz27.systemctl_show(PAIR_ARCHIVE, ["ActiveState"]).get("ActiveState") in RUNNING

    def reward_unit(self):
        kv = tz27.systemctl_show(REWARD_UNIT, ["MainPID", "NRestarts", "ActiveState"])
        return {k: kv.get(k) for k in ("MainPID", "NRestarts", "ActiveState")}

    def runtime(self):
        """The reward book's runtime.jsonl, its complete lines, read again only where the file changed; none where it
        does not exist, so that a removal waits for it."""
        path = os.path.join(self.root, "runtime.jsonl")
        try:
            st = os.stat(path)
        except FileNotFoundError:
            return []
        key = (st.st_size, st.st_mtime_ns)
        if self._rt[0] != key:
            with open(path, "rb") as fh:
                raw = fh.read()
            self._rt = (key, [json.loads(ln) for ln in raw.split(b"\n")[:-1] if ln.strip()])
        return self._rt[1]

    def reward_pids(self):
        return tz27.processes_with(REWARD_ARGV)


def safe_unit(env):
    try:
        return env.reward_unit()
    except Exception as exc:
        return {"unread": "%s: %s" % (type(exc).__name__, str(exc)[:120])}

# ---- the run: its phases -------------------------------------------------------------------------------------


class HoldTimeout(Exception):
    pass


class QuietTimeout(Exception):
    pass


def floors(env):
    mem, free = env.mem(), env.free()
    out("MemAvailable %d bytes, floor %d; free %d bytes, floor %d" % (mem, RUN_MEM_FLOOR, free, DISK_FLOOR))
    assert mem >= RUN_MEM_FLOOR, "MemAvailable %d bytes, below %d" % (mem, RUN_MEM_FLOOR)
    assert free >= DISK_FLOOR, "free %d bytes, below %d" % (free, DISK_FLOOR)


def new_set(env, led, a, rdir):
    tz27.MODE[0] = "inventory"
    assets, slots, deferred, open_n, streamless = inventory(env.root, a)
    for e in slots:
        out("SLOT %d %s %-8s stream files %d, %d bytes, taken %d" % (e["S"], tz27.utc(e["S"]), e["disposition"],
                                                                     e["streams"], e["stream_bytes"], e["taken"]))
    counts = {"slots_considered": len(slots), "open": open_n, "streamless": streamless, "deferred": deferred,
              "closed": sum(1 for e in slots if e["disposition"] == "closed"),
              "unclosed": sum(1 for e in slots if e["disposition"] == "unclosed")}
    if not assets:
        led.write(env, dict({"event": "empty", "run": a}, **counts))
        return None
    doc = set_document(TAG_PREFIX + str(a), a, env.root, assets, slots, deferred)
    for x in assets:
        out("S %s %d %s" % (x["asset"], x["bytes"], x["sha256"]))
    raw = tz27.json_bytes(doc)
    with open(os.path.join(rdir, "set.json"), "wb") as fh:
        fh.write(raw)
    led.write(env, dict({"event": "set", "run": a, "tag": doc["tag"], "sha256": tz27.sha256_bytes(raw),
                         "assets_n": doc["assets_n"], "bytes_total": doc["bytes_total"], "first_S": doc["first_S"],
                         "last_S": doc["last_S"]}, **counts))
    return doc


def hold(env, led, a, phase):
    """While the pair book's archive runs, wait; HoldTimeout after HOLD_MAX_S."""
    tz27.MODE[0] = "hold"
    waited = 0
    while env.archive_active():
        if waited >= HOLD_MAX_S:
            raise HoldTimeout("the pair book's archive still runs after %d s before %s" % (waited, phase))
        env.sleep(HOLD_STEP_S)
        waited += HOLD_STEP_S
    if waited:
        led.write(env, {"event": "hold", "run": a, "phase": phase, "waited_s": waited})
        out("held %d s before %s: the pair book's archive ran" % (waited, phase))
    return waited


def upload_phase(env, led, a, rdir, doc):
    tz27.MODE[0] = "upload"
    tok, source = env.credential()
    out("credential: %s" % source)
    gh = tz28.Gh28(env, tok, tz28.transfers_logger(rdir))
    rel = gh.release_by_tag(doc["tag"])
    created = rel is None
    if created:
        rel = gh.create_release(doc["tag"], *release_text(doc, env.commit))
        out("created the Release on %s, id %s" % (doc["tag"], rel.get("id")))
    assert rel.get("tag_name") == doc["tag"] and rel.get("draft") is False, "the Release is not published on the tag"
    path = os.path.join(rdir, "upload.jsonl")

    def log(rec):
        rec = dict(rec, at=tz27.utc(env.time()))
        tz28.jsonl_append(path, rec, "upload.jsonl")
        out("U %s" % json.dumps(rec, sort_keys=True))

    sent, held = tz27.upload_set(gh, rel, doc, env.root, log, wait_min=env.wait_min)
    log({"action": "complete", "assets": sent + held, "sent": sent, "held": held, "release_id": int(rel["id"]),
         "credential": source, "wall_ns": env.time_ns()})
    led.write(env, {"event": "upload", "run": a, "release_id": int(rel["id"]), "created": created, "sent": sent,
                    "held": held, "credential": source})


def removal_wait(env, nbytes, waited):
    """Until a second of the pair book's idle stretch at which a removal of nbytes may start and the reward book is
    quiet; QuietTimeout once QUIET_MAX_S of waiting has passed in the phase."""
    while True:
        now = tz28.idle_wait(env, tz28.budget_s(nbytes))
        why = quiet(env.runtime(), env.reward_pids(), now)
        if why is None:
            return
        if waited[0] >= QUIET_MAX_S:
            raise QuietTimeout("the removals waited %d s: %s" % (waited[0], why))
        if waited[0] % 60 == 0:
            out("removal waits: %s" % why)
        env.sleep(QUIET_STEP_S)
        waited[0] += QUIET_STEP_S


def remove_set(env, doc, done, log, waited):
    """Each file of the set, in order - its slot closed and due, its bytes hashed again equal to the set's - removed
    inside the idle stretch while the reward book is quiet, read again after the hash and right before the unlink,
    logged at once, and its day directory's other entries left as they were. A file already absent counts only where
    the run's own log records its removal."""
    rows, removed, freed, already = [], 0, 0, 0
    for x in doc["assets"]:
        p = os.path.join(env.root, str(x["T"]), x["file"])
        names = tz27.window_names(env.root, x["T"])
        assert slot_files(names, x["T"]).get(x["S"], {}).get("closed") and \
            x["S"] + SLOT_JSON_AT + SETTLE_S <= env.time(), "slot %d is not closed" % x["S"]
        if x["file"] not in names:
            assert x["asset"] in done, "%s is absent and no removal of it is recorded" % p
            already += 1
            continue
        while True:
            removal_wait(env, x["bytes"], waited)
            t0 = env.time_ns()
            h, n = tz27.sha256_file(p)
            assert (h, n) == (x["sha256"], x["bytes"]), "%s is %d bytes, SHA-256 %s: not the set's" % (p, n, h)
            if quiet(env.runtime(), env.reward_pids(), env.time()) is None:
                break
        ap = os.path.abspath(p)
        tz27.ALLOWED_REMOVE.add(ap)
        try:
            os.remove(p)
        finally:
            tz27.ALLOWED_REMOVE.discard(ap)
        tz27.bump("removed")
        assert not os.path.lexists(p), "%s is still there" % p
        lost = sorted(set(names) - set(tz27.window_names(env.root, x["T"])) - {x["file"]})
        assert not lost, "day %d lost more than %s: %r" % (x["T"], x["file"], lost[:5])
        removed += 1
        freed += n
        row = {"asset": x["asset"], "T": x["T"], "S": x["S"], "k": x["k"], "file": x["file"], "bytes": n, "sha256": h,
               "start_ns": t0, "removed_wall_ns": env.time_ns()}
        tz27.assert_keys(row, DELETE_ROW_KEYS, "delete.jsonl row")
        log(row)
        rows.append(row)
    return rows, removed, freed, already


def delete_phase(env, led, a, rdir, doc, vsha):
    tz27.MODE[0] = "delete"
    with open(os.path.join(rdir, "verify.json"), "rb") as fh:
        assert tz27.sha256_bytes(fh.read()) == vsha, "delete: verify.json is not this run's"
    path = os.path.join(rdir, "delete.jsonl")

    def log(row):
        tz28.jsonl_append(path, row, "delete.jsonl")
        out("X %s %d %s removed at second %d" % (row["asset"], row["bytes"], row["sha256"],
                                                tz28.phase_of(row["removed_wall_ns"] // 10 ** 9)))

    done = {r["asset"] for r in tz28.jsonl_read(path)}
    free_before = env.free()
    waited = [0]
    _rows, removed, freed, already = remove_set(env, doc, done, log, waited)
    checks, gone, kept = removed_reading(env.root, doc, {r["asset"] for r in tz28.jsonl_read(path)})
    for k, v in checks.items():
        out("G-DELETE %-36s %s" % (k, v))
    assert all(checks.values()), "REMOVED FAIL: %r" % sorted(k for k, v in checks.items() if not v)
    led.write(env, {"event": "delete", "run": a, "removed": removed, "already": already, "freed": freed, "gone": gone,
                    "slots_kept": kept, "free_before": free_before, "free_after": env.free(), "quiet_s": waited[0]})


def final_phase(env, led, a, rdir, doc, reward0):
    tz27.MODE[0] = "final"
    trs = tz28.jsonl_read(os.path.join(rdir, "transfers.jsonl"))
    rms = tz28.jsonl_read(os.path.join(rdir, "delete.jsonl"))
    acts = [tz28.transfer_ok(t) for t in trs] + [tz28.transfer_ok(removal_span(r)) for r in rms]
    counter, free = stream_bytes_view(env.root), env.free()
    rate, rows = projection(doc["bytes_total"], doc["first_S"], doc["last_S"], counter, free, int(env.time()))
    for what, d, when in rows:
        out("at the set's rate %s stops the streams in %s days, at %s" % (what, tz27.decimals(d, 2), tz27.utc(when)))
    held = sum(r.get("waited_s", 0) for r in tz28.events(led.recs, a, "hold"))
    led.write(env, {"event": "complete", "run": a, "assets_n": doc["assets_n"], "bytes_total": doc["bytes_total"],
                    "requests": len(trs), "removals": len(rms), "started_outside": sum(1 for s, _e in acts if not s),
                    "ended_outside": sum(1 for _s, e in acts if not e), "store_stream_bytes": counter,
                    "free_bytes": free, "rate_per_day": int(rate), "stops": [[w, int(t)] for w, _d, t in rows],
                    "held_s": held, "rewardbook_at_start": reward0, "rewardbook_at_end": safe_unit(env),
                    "peak_rss": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024})


def run(env):
    """One run: the pending set resumed, or a new one as of now; exit 0, EXIT_DEFERRED or 1."""
    tz27.WORK[0], tz27.MODE[0] = env.work, "run"
    led = tz28.Ledger(env.state)
    if tz28.halted(led.recs):
        last = [r for r in led.recs if r.get("event") == "halt"][-1]
        out("HALTED since run %s, %s: %s; nothing done" % (last.get("run"), last.get("phase"), last.get("reason")))
        tz27.MODE[0] = "final"
        rc = env.disable_timer()
        led.write(env, {"event": "refused", "run": last.get("run"), "exit": rc})
        return 1
    a = tz28.pending(led.recs)
    resumed = a is not None
    if not resumed:
        a = max([int(env.time())] + [r["run"] + 1 for r in led.recs if r.get("event") == "start"])
    rdir = os.path.join(env.state, "runs", str(a))
    os.makedirs(rdir, exist_ok=True)
    reward0 = safe_unit(env)
    led.write(env, {"event": "start", "run": a, "resumed": resumed, "commit": env.commit, "file_sha256": env.file_sha,
                    "tz28_sha256": TZ28_SHA256, "tz27_sha256": TZ27_SHA256, "invocation": env.invocation,
                    "trigger": env.trigger, "phase_at": tz28.phase_of(env.time()), "rewardbook": reward0})
    phase = "set"
    try:
        floors(env)
        doc = tz28.load_set(led, a, rdir)
        if doc is None:
            doc = new_set(env, led, a, rdir)
            if doc is None:
                out("EMPTY: no stream file of a closed slot as of %d" % a)
                return 0
        if not tz28.events(led.recs, a, "delete"):
            phase = "upload"
            hold(env, led, a, phase)
            upload_phase(env, led, a, rdir, doc)
            phase = "verify"
            hold(env, led, a, phase)
            vsha = tz28.verify_phase(env, led, a, rdir, doc)
            phase = "delete"
            delete_phase(env, led, a, rdir, doc, vsha)
        phase = "final"
        final_phase(env, led, a, rdir, doc, reward0)
        out("COMPLETE: run %d, %d files, %d bytes, Release %s" % (a, doc["assets_n"], doc["bytes_total"], doc["tag"]))
        return 0
    except tz27.GuardError as exc:
        return tz28.halt(env, led, a, phase, "GuardError: %s" % exc)
    except Exception as exc:
        reason = "%s: %s" % (type(exc).__name__, str(exc))
        if phase not in PRE_DELETE and not isinstance(exc, QuietTimeout):
            return tz28.halt(env, led, a, phase, reason)
        n = len(tz28.events(led.recs, a, "deferred")) + 1
        if n >= tz28.DEFER_LIMIT:
            return tz28.halt(env, led, a, phase, "deferral %d of %d: %s" % (n, tz28.DEFER_LIMIT, reason))
        led.write(env, {"event": "deferred", "run": a, "phase": phase, "reason": reason[:400], "count": n})
        out("DEFERRED in %s, %d of %d: %s; the next run resumes this set" % (phase, n, tz28.DEFER_LIMIT, reason[:400]))
        return tz28.EXIT_DEFERRED


def mode_run():
    cwd = os.getcwd()
    assert cwd == STATE, "run: from %s, not %s" % (cwd, STATE)
    assert os.path.abspath(__file__) == ASVC + "/" + SELF_NAME, "run: this file is not the service's copy"
    assert os.environ.get("INVOCATION_ID"), "run: only %s runs this mode" % ARCHIVE
    env = Env()
    env.identity()
    tz27.WORK[0], tz27.MODE[0] = STATE, "run"
    lock = open(os.path.join(STATE, "run.lock"), "ab")
    try:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        out("NOT STARTED: another run holds %s/run.lock" % STATE)
        return tz28.EXIT_NOT_STARTED
    out("run: pid %d, commit %s, file sha256 %s, invocation %s" % (os.getpid(), env.commit, env.file_sha,
                                                                   env.invocation))
    return run(env)

# ---- the deployment's readings: the session's modes ---------------------------------------------------------


def mode_fingerprint():
    primary = tz27.PRIMARY
    with open(os.path.join(primary, "SYSTEM-MAP.md"), "rb") as fh:
        raw = fh.read()
    txt = raw.decode("utf-8")
    rev = re.findall(r"^\*\*Revision string:\*\* `([^`]+)`$", txt, re.M)
    assert rev == [MAP_REVISION], "map revision %r, required %s" % (rev, MAP_REVISION)
    found = dict(tz27.ANCHOR_ROW.findall(txt))
    assert found == tz27.ANCHORS, "anchors %r" % found
    for k, rel in sorted(tz27.ANCHOR_FILES.items()):
        h = tz27.sha256_file(os.path.join(primary, rel))[0][:12]
        assert h == tz27.ANCHORS[k], "re-derived %s %s, the map %s" % (k, h, tz27.ANCHORS[k])
        out("re-derived %s %s sha256[:12] %s equal" % (k, rel, h))
    rows = tz27.ROW.findall(txt)
    states = {k: sum(1 for r in rows if r[3] == k) for k in MAP_ROWS}
    assert states == MAP_ROWS and len(rows) == sum(MAP_ROWS.values()), "rows %r" % states
    for path, lines, nbytes, state, sha in rows:
        with open(os.path.join(primary, path), "rb") as fh:
            blob = fh.read()
        got = (blob.count(b"\n"), len(blob), tz27.sha256_bytes(blob))
        if state == "frozen":
            want = (int(lines.replace(",", "")), int(nbytes.replace(",", "")), sha)
            assert got == want, "frozen row %s: %r, the map %r" % (path, got, want)
        out("%-44s %6d lines %8d bytes %s %s%s" % (path, got[0], got[1], got[2], state,
                                                  " equal" if state == "frozen" else ""))
    out("SYSTEM-MAP.md %d lines %d bytes sha256 %s" % (raw.count(b"\n"), len(raw), tz27.sha256_bytes(raw)))
    out("FINGERPRINT PASS: revision %s; anchors 6 of 6, 4 re-derived; rows %d: frozen %d of %d equal, tracked %d, "
        "reported %d" % (MAP_REVISION, len(rows), states["frozen"], MAP_ROWS["frozen"], states["tracked"],
                         states["reported"]))


def units_now():
    now = {}
    for key, unit in sorted(UNITS.items()):
        kv = tz27.systemctl_show(unit, ["MainPID", "NRestarts", "ActiveState", "MemoryCurrent", "MemoryPeak"])
        now[key] = {k: kv.get(k) for k in ("MainPID", "NRestarts", "ActiveState")}
        out("%s %s, MemoryCurrent %s, MemoryPeak %s" % (unit, now[key], kv.get("MemoryCurrent"), kv.get("MemoryPeak")))
    for unit in (PAIR_TIMER, PAIR_ARCHIVE, TIMER, ARCHIVE):
        try:
            kv = tz27.systemctl_show(unit, ["ActiveState", "SubState", "UnitFileState", "Result"])
        except AssertionError as exc:
            kv = {"unread": str(exc)[:120]}
        out("%s %s" % (unit, kv))
    return now


def pair_restarts(since_ns):
    """The pair book's archive's restart records since an instant, in order, from its own ledger."""
    with open(PAIR_LEDGER, "rb") as fh:
        raw = fh.read()
    recs = [json.loads(ln) for ln in raw.split(b"\n")[:-1] if ln.strip()]
    return [r for r in recs if r.get("event") == "restart" and r.get("wall_ns", 0) >= since_ns]


def mode_still():
    """G-STILL: the first run records the three capture units; a later run compares. A FAIL runs no block."""
    st = tz27.load_state()
    now = units_now()
    if "still34" not in st:
        st["still34"] = {"at": tz27.utc(time.time()), "at_ns": time.time_ns(), "units": now}
        tz27.save_state(st)
        out("still: recorded")
        return True
    restarts = pair_restarts(st["still34"]["at_ns"])
    for r in restarts:
        out("the pair book's archive's restart record %s: run %s, window %s, pid %s after %s, NRestarts %s" % (
            tz27.utc(r["wall_ns"] / 1e9), r.get("run"), r.get("W"), r.get("pid"), r.get("stopped"), r.get("NRestarts")))
    ok, why = still_reading(st["still34"]["units"], now, restarts)
    out("G-STILL %s: %s since %s" % ("PASS" if ok else "FAIL", why, st["still34"]["at"]))
    return ok


def git_out(*args):
    cp = subprocess.run(["git"] + list(args), capture_output=True, text=True)
    assert cp.returncode == 0, "git %s: exit %d" % (" ".join(args), cp.returncode)
    return cp.stdout.strip()


def mode_installed():
    """G-INSTALL: what B-INSTALL put on the host, against the branch's worktree."""
    wt = tz27.wpath("wt")
    head, up = git_out("-C", wt, "rev-parse", "HEAD"), git_out("-C", wt, "rev-parse", "@{u}")
    with open(os.path.join(ASVC, "commit.txt"), encoding="utf-8") as fh:
        commit = fh.read().strip()
    files = {}
    for name in (SELF_NAME, TZ28_NAME, TZ27_NAME):
        files[name] = (tz27.sha256_file(os.path.join(ASVC, name))[0],
                       tz27.sha256_file(os.path.join(wt, "research", name))[0])
    units = {}
    for name in (ARCHIVE, TIMER):
        with open(os.path.join(UNIT_DIR, name), "rb") as a_:
            installed = a_.read()
        with open(os.path.join(wt, "deploy", "systemd", name), "rb") as b_:
            units[name] = installed == b_.read()
    st = os.stat(STATE)
    svc = tz28.show_utc(ARCHIVE, ["LoadState", "ActiveState", "UnitFileState", "FragmentPath", "Type", "Restart",
                                  "MemoryMax", "TimeoutStartUSec", "WorkingDirectory", "ExecStart", "Nice"])
    tmr = tz28.show_utc(TIMER, ["LoadState", "ActiveState", "UnitFileState", "FragmentPath"])
    argv = "argv[]=%s ;" % " ".join(RUN_ARGV)
    checks = {"commit.txt the branch head, pushed": commit == head == up,
              "the service's copy of this file the branch's": files[SELF_NAME][0] == files[SELF_NAME][1],
              "the service's copy of TZ-28's file, %s" % TZ28_SHA256[:12]: files[TZ28_NAME][0] == files[TZ28_NAME][1]
              == TZ28_SHA256,
              "the service's copy of TZ-27's file, %s" % TZ27_SHA256[:12]: files[TZ27_NAME][0] == files[TZ27_NAME][1]
              == TZ27_SHA256,
              "the two units byte for byte": all(units.values()),
              "the state directory, root's, 0700, empty": os.path.isdir(STATE) and st.st_uid == 0
              and (st.st_mode & 0o777) == 0o700 and not os.listdir(STATE),
              "the service loaded, inactive, static": (svc["LoadState"], svc["ActiveState"], svc["UnitFileState"])
              == ("loaded", "inactive", "static"),
              "the service a oneshot, Restart=no, Nice=19, 128M, 6h, its argv and directory": svc["Type"] == "oneshot"
              and svc["Restart"] == "no" and svc["Nice"] == "19" and svc["MemoryMax"] == str(ARCHIVE_MEMORY_MAX)
              and svc["TimeoutStartUSec"] == "6h" and svc["WorkingDirectory"] == STATE and argv in svc["ExecStart"]
              and svc["FragmentPath"] == UNIT_DIR + "/" + ARCHIVE,
              "the timer loaded, inactive, disabled": (tmr["LoadState"], tmr["ActiveState"], tmr["UnitFileState"],
                                                       tmr["FragmentPath"]) == ("loaded", "inactive", "disabled",
                                                                                UNIT_DIR + "/" + TIMER)}
    for name, (a_, b_) in sorted(files.items()):
        out("%s/%s sha256 %s; the branch's %s" % (ASVC, name, a_, b_))
    out("commit.txt %s; the branch head %s, its upstream %s" % (commit, head, up))
    for k, v in checks.items():
        out("G-INSTALL %-76s %s" % (k, v))
    assert all(checks.values()), "G-INSTALL FAIL: %r" % sorted(k for k, v in checks.items() if not v)
    out("G-INSTALL PASS: %d of %d" % (len(checks), len(checks)))


def mode_mark(name):
    assert name in ("enable", "retry", "stop"), "mark %r" % name
    st = tz27.load_state()
    marks = st.setdefault("marks34", {})
    assert name not in marks, "mark %s already taken" % name
    tmr = tz28.show_utc(TIMER, ["ActiveState", "UnitFileState"])
    svc = tz28.show_utc(ARCHIVE, ["ActiveState", "Result"])
    marks[name] = {"ns": time.time_ns(), "timer": tmr, "service": svc}
    tz27.save_state(st)
    out("mark %s at %s, second %d of its window: the timer %r, the service %r" % (
        name, tz27.utc(marks[name]["ns"] / 1e9), tz28.phase_of(marks[name]["ns"] // 10 ** 9), tmr, svc))


def next_calendar(now):
    """The first instant after now at 01:30:20 UTC."""
    d = int(now) // 86400 * 86400 + CALENDAR_S
    return d if d > now else d + 86400


def timer_reading(now):
    kv = tz28.show_utc(TIMER, ["LoadState", "ActiveState", "SubState", "UnitFileState", "FragmentPath", "Unit",
                               "TimersCalendar", "TimersMonotonic", "NextElapseUSecRealtime", "AccuracyUSec",
                               "LastTriggerUSec", "ActiveEnterTimestamp"])
    nxt = tz28.stamp_of(kv.get("NextElapseUSecRealtime"))
    checks = {"loaded": kv["LoadState"] == "loaded",
              "active": kv["ActiveState"] == "active" and kv["SubState"] in ("waiting", "running"),
              "enabled": kv["UnitFileState"] == "enabled",
              "fragment": kv["FragmentPath"] == UNIT_DIR + "/" + TIMER,
              "its unit": kv["Unit"] == ARCHIVE,
              "the calendar": ("OnCalendar=%s ;" % CALENDAR) in kv["TimersCalendar"],
              "1,800 s after it starts": "OnActiveUSec=30min" in kv["TimersMonotonic"],
              "accuracy 1 s": kv["AccuracyUSec"] == "1s",
              "the next calendar elapse": nxt == next_calendar(now)}
    return kv, checks, nxt


def mode_timer():
    now = time.time()
    kv, checks, nxt = timer_reading(now)
    out("the timer: %r" % kv)
    for k, v in checks.items():
        out("G-TIMER %-24s %s" % (k, v))
    assert all(checks.values()), "G-TIMER FAIL: %r" % sorted(k for k, v in checks.items() if not v)
    out("G-TIMER PASS: the next calendar run at %s, the run after the start at %s" % (
        tz27.utc(nxt), tz27.utc((tz28.stamp_of(kv.get("ActiveEnterTimestamp")) or 0) + ACTIVE_S)))


def read_slot(root, s):
    """Every slot.json of slot s: [(k, doc)]."""
    found = []
    for k, n in slot_names(root, s):
        with open(os.path.join(root, str(day_of(s)), n), "rb") as fh:
            found.append((k, json.loads(fh.read())))
    return found


def read_runtime(root):
    with open(os.path.join(root, "runtime.jsonl"), "rb") as fh:
        raw = fh.read()
    return [json.loads(ln) for ln in raw.split(b"\n")[:-1] if ln.strip()]


def slot_line(s, sjs):
    parts = []
    for k, sj in sjs:
        st = sj.get("stream") if isinstance(sj.get("stream"), dict) else {}
        parts.append("index %d pid %s joined_late %s stopped %s opened %s off %s segments %s frames %s max_gap_ns %s "
                     "stored_bytes %s error %s" % (k, sj.get("pid"), sj.get("joined_late"), sj.get("stopped"),
                                                   st.get("opened"), st.get("off_reason"), st.get("segments"),
                                                   st.get("frames"), st.get("max_gap_ns"), st.get("stored_bytes"),
                                                   sj.get("error")))
    return "slot %d %s: %s" % (s, tz27.utc(s), "; ".join(parts) if parts else "no slot.json")


def store_left(root, doc):
    """After the run, the store against the set: every stream file left of a slot due by A; of those the files of a
    slot the set records closed, which only its deferral may leave, and the files of a slot it does not record, which
    nothing may leave; and the set's slots whose slot.json is no longer as the set recorded it."""
    a = doc["as_of"]
    disp = {e["S"]: e["disposition"] for e in doc["slots"]}
    left, closed_left, unknown, seen = [], [], [], {}
    for d0 in day_dirs(root):
        for s, e in sorted(slot_files(tz27.window_names(root, d0), d0).items()):
            seen[s] = "closed" if e["closed"] else "unclosed"
            if s + SLOT_JSON_AT + SETTLE_S > a:
                continue
            for _k, n in sorted(e["streams"]):
                left.append(n)
                if s not in disp:
                    unknown.append(n)
                elif disp[s] == "closed":
                    closed_left.append(n)
    flipped = sorted(s for s, d in disp.items() if seen.get(s) != d)
    return left, closed_left, unknown, flipped


def set_reading(doc, raw, sets, closed_left, unknown, flipped):
    """G-SET, pure: one set record, set.json its SHA-256, the document this TZ's rule rebuilds from it equal to it, its
    deferral the closed slots' files not taken, at most that many files of closed slots left, none of a slot it does
    not record, and every slot's slot.json as recorded."""
    rebuilt = set_document(doc["tag"], doc["as_of"], doc["root"], doc["assets"], doc["slots"], doc["deferred"])
    owed = sum(e["streams"] - e["taken"] for e in doc["slots"] if e["disposition"] == "closed")
    taken = sum(e["taken"] for e in doc["slots"])
    return (len(sets) == 1 and tz27.sha256_bytes(raw) == sets[0]["sha256"] and rebuilt == doc
            and owed == doc["deferred"] and taken == doc["assets_n"] and len(closed_left) <= doc["deferred"]
            and not unknown and not flipped)


def mode_first():
    """The first run after the enable mark, re-read from its records, the store, the reward book's record, systemd and
    the Release: exit 3 while it has not ended or G-NEXT's slots are not yet due."""
    tz27.MODE[0] = "final"
    st = tz27.load_state()
    mark = st.get("marks34", {}).get("enable")
    assert mark is not None, "first: no enable mark"
    svc = tz28.show_utc(ARCHIVE, ["ActiveState", "Result", "ExecMainStatus", "ExecMainStartTimestamp",
                                  "ExecMainExitTimestamp", "InvocationID"])
    recs = tz28.Ledger(STATE).recs
    a, mine = tz28.first_run(recs, mark["ns"])
    if a is None or svc["ActiveState"] in RUNNING:
        out("NOT YET: %s; the service %s" % ("no run since the mark" if a is None else "run %d" % a,
                                              svc["ActiveState"]))
        return 3
    terms = [r["event"] for r in mine if r["event"] in tz28.TERMINAL]
    rdir = os.path.join(STATE, "runs", str(a))
    drecs = tz28.jsonl_read(os.path.join(rdir, "delete.jsonl"))
    slots = next_slots(drecs[0]["start_ns"], drecs[-1]["removed_wall_ns"]) if drecs else []
    if terms and terms[-1] == "complete" and slots and time.time() < slots[-1] + SLOT_JSON_AT + NEXT_SETTLE_S:
        out("NOT YET: run %d complete; G-NEXT's last slot %d is due at %s" % (
            a, slots[-1], tz27.utc(slots[-1] + SLOT_JSON_AT + NEXT_SETTLE_S)))
        return 3
    for r in mine:
        out("R %s" % json.dumps(r, sort_keys=True))
    out("run %d: %d records, %s" % (a, len(mine), [r["event"] for r in mine]))
    if not terms:
        last = mine[-1]["event"]
        out("READING G-RUN: %s - the run's last record %s, in its phase %r" % (
            "DEFERRED" if last == "deferred" else "INTERRUPTED", last, mine[-1].get("phase")))
        return 1
    last = terms[-1]
    readings = {}
    tmr = tz28.show_utc(TIMER, ["LastTriggerUSec", "ActiveEnterTimestamp"])
    last_trig, enter = tz28.stamp_of(tmr.get("LastTriggerUSec")), tz28.stamp_of(tmr.get("ActiveEnterTimestamp"))
    s0 = mine[0]["wall_ns"] // 10 ** 9
    readings["G-TRIGGER"], source, trig = trigger_reading(mine[0].get("trigger"), mark["ns"] // 10 ** 9, s0, last_trig)
    out("G-TRIGGER, by %s: the enable mark %s, the timer started %s, the run's trigger %s - %s s after the mark plus "
        "%d - the run's first record %s; the timer's last trigger %s" % (
            source, tz27.utc(mark["ns"] / 1e9), tz27.utc(enter or 0), tz27.utc(trig or 0),
            None if trig is None else trig - mark["ns"] // 10 ** 9 - ACTIVE_S, ACTIVE_S, tz27.utc(s0),
            tz27.utc(last_trig or 0)))
    readings["G-RUN"] = last == "complete" and svc["Result"] == "success" and svc["ExecMainStatus"] == "0"
    out("G-RUN: the run %s; the service's last invocation %s, Result %s, ExecMainStatus %s, %s to %s" % (
        last, svc["InvocationID"], svc["Result"], svc["ExecMainStatus"], svc["ExecMainStartTimestamp"],
        svc["ExecMainExitTimestamp"]))
    if last == "complete":
        with open(os.path.join(rdir, "set.json"), "rb") as fh:
            raw = fh.read()
        sets = [r for r in mine if r["event"] == "set"]
        doc = json.loads(raw)
        left, closed_left, unknown, flipped = store_left(ROOT, doc)
        for e in doc["slots"]:
            out("SLOT %d %s %-8s stream files %d, %d bytes, taken %d" % (e["S"], tz27.utc(e["S"]), e["disposition"],
                                                                         e["streams"], e["stream_bytes"], e["taken"]))
        for x in doc["assets"]:
            out("S %s %d %s" % (x["asset"], x["bytes"], x["sha256"]))
        readings["G-SET"] = set_reading(doc, raw, sets, closed_left, unknown, flipped)
        out("G-SET: %d files, %d bytes, slots %d to %d, as of %d, deferred %d; set.json sha256 %s; the store after "
            "the run holds %d stream files of slots due by A - %d of slots the set records closed, %d of slots it "
            "does not record; slots whose slot.json is not as recorded %r" % (
                doc["assets_n"], doc["bytes_total"], doc["first_S"], doc["last_S"], doc["as_of"], doc["deferred"],
                tz27.sha256_bytes(raw), len(left), len(closed_left), len(unknown), flipped))
        rel, rows, missing, extra = tz27.verify_release(tz27.GitHub(), doc["tag"], doc, download=False)
        up = tz27.release_reading(rel, doc["tag"], rows, missing, extra)
        obj, peeled = tz27.ls_remote_tag(doc["tag"])
        readings["G-UPLOAD"] = all(v for k, v in up.items() if not k.startswith("every download")) and \
            obj == mine[0]["commit"] and peeled is None
        out("G-UPLOAD: Release %s, %d of %d assets by name, bytes, state and digest, %d missing, %d beyond; the tag "
            "%s at %s" % (None if rel is None else rel.get("id"), sum(r["api_ok"] for r in rows), doc["assets_n"],
                          len(missing), len(extra), doc["tag"], obj))
        vrec = [r for r in mine if r["event"] == "verify"][-1]
        with open(os.path.join(rdir, "verify.json"), "rb") as fh:
            vraw = fh.read()
        vdoc = json.loads(vraw)
        readings["G-DOWNLOAD"] = tz27.sha256_bytes(vraw) == vrec["verify_sha256"] and vdoc["assets_n"] == \
            doc["assets_n"] and all(r["download_ok"] and r["download_sha256"] == r["sha256"] for r in vdoc["assets"])
        out("G-DOWNLOAD: verify.json sha256 %s, %d of %d downloads equal, %d bytes" % (
            tz27.sha256_bytes(vraw), sum(r["download_ok"] for r in vdoc["assets"]), doc["assets_n"],
            vdoc["bytes_total"]))
        done = {r["asset"] for r in drecs}
        aby, vby, dby = {r["asset"]: r for r in rows}, {r["asset"]: r for r in vdoc["assets"]}, \
            {r["asset"]: r for r in drecs}
        for x in doc["assets"]:
            out("ROW %s %d %s digest %s download %s removed %s" % (
                x["asset"], x["bytes"], x["sha256"], aby.get(x["asset"], {}).get("digest"),
                vby.get(x["asset"], {}).get("download_sha256"), dby.get(x["asset"], {}).get("sha256")))
        dchecks, gone, kept = removed_reading(ROOT, doc, done)
        readings["G-DELETE"] = all(dchecks.values())
        out("G-DELETE: %r; %d gone, %d removals recorded, %d slots keep their slot.json" % (dchecks, gone, len(done),
                                                                                         kept))
        trs = tz28.jsonl_read(os.path.join(rdir, "transfers.jsonl"))
        for t in trs:
            s, e = tz28.transfer_ok(t)
            out("T %s %s: %d bytes, budget %d s, second %d, %.1f s, inside %s %s" % (
                t["kind"], t["name"], t["bytes"], t["budget_s"], tz28.phase_of(t["start_ns"] // 10 ** 9),
                (t["end_ns"] - t["start_ns"]) / 1e9, s, e))
        for r in drecs:
            s, e = tz28.transfer_ok(removal_span(r))
            out("X %s: %d bytes, second %d, %.3f s, inside %s %s" % (
                r["asset"], r["bytes"], tz28.phase_of(r["start_ns"] // 10 ** 9),
                (r["removed_wall_ns"] - r["start_ns"]) / 1e9, s, e))
        acts = [tz28.transfer_ok(t) for t in trs] + [tz28.transfer_ok(removal_span(r)) for r in drecs]
        readings["G-IDLE"] = bool(trs) and bool(drecs) and all(s and e for s, e in acts)
        out("G-IDLE: %d requests and %d removals, %d started outside, %d ended outside" % (
            len(trs), len(drecs), sum(1 for s, _e in acts if not s), sum(1 for _s, e in acts if not e)))
        rt = read_runtime(ROOT)
        pid0 = (mine[0].get("rewardbook") or {}).get("MainPID")
        verdicts = []
        for s in slots:
            errs = [r for r in rt if r.get("event") == "error" and r.get("what") == "slot %d" % s]
            v, why = next_verdict(read_slot(ROOT, s), errs, pid0)
            verdicts.append((v, why))
            out("G-NEXT slot %d %s, decided at %s: %s - %s" % (s, tz27.utc(s), tz27.utc(s - DECIDE_S), v, why))
        reading = next_reading(verdicts)
        readings["G-NEXT"] = reading != "FAIL"
        out("READING G-NEXT: %s over %d slots, the reward book's process at the run's start %s" % (
            reading, len(slots), pid0))
        span = (mine[0]["wall_ns"] // 10 ** 9, mine[-1]["wall_ns"] // 10 ** 9)
        s = (span[0] + OPEN_BEFORE) // SLOT * SLOT
        while s - OPEN_BEFORE <= span[1]:
            out("ACROSS %s" % slot_line(s, read_slot(ROOT, s)))
            s += SLOT
        for r in mine:
            if r["event"] == "hold":
                out("HOLD %d s before %s" % (r["waited_s"], r["phase"]))
        out("the run's own record: %s" % json.dumps(mine[-1], sort_keys=True))
    for k, v in readings.items():
        out("READING %-11s %s" % (k, "PASS" if v else "FAIL"))
    bad = sorted(k for k, v in readings.items() if not v)
    assert not bad, "FIRST FAIL: %r" % bad
    out("FIRST PASS: %d of %d" % (len(readings), len(readings)))
    return 0


def mode_final():
    tz27.MODE[0] = "final"
    now = time.time()
    kv, checks, nxt = timer_reading(now)
    for k, v in checks.items():
        out("G-TIMER %-24s %s" % (k, v))
    assert all(checks.values()), "G-TIMER FAIL: %r" % sorted(k for k, v in checks.items() if not v)
    tz27.MODE[0] = "still"
    still = mode_still()
    tz27.MODE[0] = "final"
    recs = tz28.Ledger(STATE).recs
    counter, free = stream_bytes_view(ROOT), tz27.free_bytes()
    days = day_dirs(ROOT)
    out("the store: %d day directories, %d to %d; its stream files %d bytes; free %d bytes" % (
        len(days), days[0] if days else 0, days[-1] if days else 0, counter, free))
    done = [r for r in recs if r.get("event") == "complete"]
    if done:
        sets = [r for r in recs if r.get("event") == "set" and r["run"] == done[-1]["run"]][-1]
        rate, rows = projection(sets["bytes_total"], sets["first_S"], sets["last_S"], counter, free, int(now))
        out("the last set's rate: %s bytes a day" % tz27.decimals(rate, 0))
        for what, d, when in rows:
            out("at that rate %s stops the streams in %s days, at %s" % (what, tz27.decimals(d, 2), tz27.utc(when)))
    out("the next run at %s; the ledger %d records" % (tz27.utc(nxt), len(recs)))
    assert still, "FINAL: G-STILL FAIL"
    out("FINAL PASS")


def mode_stopped():
    """After K-34: the timer disabled and inactive, no run in progress; the ledger's last records."""
    tmr = tz28.show_utc(TIMER, ["ActiveState", "UnitFileState"])
    svc = tz28.show_utc(ARCHIVE, ["ActiveState", "Result"])
    recs = tz28.Ledger(STATE).recs if os.path.exists(os.path.join(STATE, "ledger.jsonl")) else []
    for r in recs[-3:]:
        out("L %s" % json.dumps(r, sort_keys=True))
    checks = {"the timer disabled and inactive": (tmr["UnitFileState"], tmr["ActiveState"]) == ("disabled", "inactive"),
              "no run in progress": svc["ActiveState"] in ("inactive", "failed")}
    for k, v in checks.items():
        out("STOPPED %-34s %s" % (k, v))
    assert all(checks.values()), "STOPPED FAIL: %r" % sorted(k for k, v in checks.items() if not v)
    out("STOPPED PASS: the timer %r, the service %r" % (tmr, svc))

# ---- the self-test: literals, temporary stores, a simulated reward book and a loopback server only ----------------


class FakeEnv(Env):
    """The run's world in a temporary directory: a clock that moves only when the run sleeps, a reward book's record
    the test writes, the pair book's archive running where told, and GitHub on 127.0.0.1."""

    def __init__(self, work, root, state, base, t0, token):
        self.root, self.state, self.work = root, state, work
        self.wait_min, self.gap_s = 0, 0.0
        self.api = self.uploads = self.web = base
        self.invocation, self.commit, self.file_sha = "selftest", "c" * 40, "f" * 64
        self.trigger = {"unit": None, "realtime_usec": None, "monotonic_usec": None}
        self.clock, self.token, self.cred_ok = float(t0), token, True
        self.disabled, self.busy_until, self.on_sleep = 0, None, None
        self.recs, self.pids, self.pids_fn = [], [3137952], None

    def time(self):
        return self.clock

    def time_ns(self):
        return int(round(self.clock * 1e9))

    def sleep(self, s):
        self.clock += max(0.0, s)
        if self.on_sleep is not None:
            self.on_sleep(self)

    def disable_timer(self):
        self.disabled += 1
        return 0

    def credential(self):
        if not self.cred_ok:
            raise AssertionError("UPLOAD REFUSED: no credential (selftest)")
        return self.token, "the selftest's"

    def free(self):
        return 9600000000

    def mem(self):
        return 300000000

    def archive_active(self):
        return self.busy_until is not None and self.clock < self.busy_until

    def reward_unit(self):
        return {"MainPID": str(self.pids[0]) if self.pids else "0", "NRestarts": "1", "ActiveState": "active"}

    def runtime(self):
        return list(self.recs)

    def reward_pids(self):
        return self.pids_fn(self) if self.pids_fn is not None else list(self.pids)


def tz33_text():
    path = os.path.join(HERE, TZ33_NAME)
    with open(path, "rb") as fh:
        raw = fh.read()
    assert hashlib.sha256(raw).hexdigest() == TZ33_SHA256, "%s is not the reward book's frozen file" % path
    return raw.decode("utf-8")


def tz33_values(tree, names):
    """The module-level assignments of names in TZ-33's text, executed in file order: their values."""
    ns = {"re": re, "os": os}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) \
                and node.targets[0].id in names:
            exec(compile(ast.Module(body=[node], type_ignores=[]), TZ33_NAME, "exec"), ns)
    return {k: (ns[k].pattern if isinstance(ns[k], re.Pattern) else ns[k]) for k in names if k in ns}


def tz33_function(tree, name):
    """One of TZ-33's functions, executed from its own text beside the regexes it reads."""
    ns = {"re": re, "os": os}
    ns.update({k: re.compile(v) for k, v in tz33_values(tree, ("DAY_RE", "SLOT_FILE_RE")).items()})
    node = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name][0]
    exec(compile(ast.Module(body=[node], type_ignores=[]), TZ33_NAME, "exec"), ns)
    return ns[name]


def mode_selftest():
    n = [0]

    def ok(cond, what):
        assert cond, "selftest: " + what
        n[0] += 1
        out("  ok  " + what)

    sep = ":" + "//"
    D0 = 1793145600                      # 2026-10-28 00:00:00 UTC
    D1 = D0 + DAY
    # the calendar, the names and the clock, against integers computed outside this file
    ok(next_calendar(D0) == D0 + 5420 and next_calendar(D0 + 5419) == D0 + 5420 and next_calendar(D0 + 5420)
       == D1 + 5420 and CALENDAR_S == 5420, "the calendar: 01:30:20 UTC, the next after now")
    ok(TAG_RE.fullmatch("rewardbook-streams-1793235620") is not None
       and tz27.TAG_RE.fullmatch("rewardbook-streams-1793235620") is None
       and tz28.TAG_RE.fullmatch("rewardbook-streams-1793235620") is None
       and TAG_RE.fullmatch("pairbook-streams-1793235620") is None, "this TZ's tags, which TZ-27's and TZ-28's rules "
       "do not cover, and theirs, which this TZ's does not")
    ok(ASSET_RE.fullmatch("1793145600-1793187900.0.stream.jsonl.gz") is not None
       and ASSET_RE.fullmatch("1793145600-1793187900.12.stream.jsonl.gz") is not None
       and ASSET_RE.fullmatch("1793145600-1793187900.0.rewards.jsonl.gz") is None
       and ASSET_RE.fullmatch("1793145600-1793187900.0.slot.json") is None
       and tz27.ASSET_RE.fullmatch("1793145600-1793187900.0.stream.jsonl.gz") is None, "the asset names")
    ok(day_of(D0) == D0 and day_of(D1 - 1) == D0 and day_of(D1) == D1 and DECIDE_S == 6
       and 128 * 2 ** 20 == ARCHIVE_MEMORY_MAX and 6 * 3600 == TIMEOUT_S and 30 * 60 == ACTIVE_S,
       "the day, the decision at S - 6, 128M, 6h and 30min in bytes and seconds")
    ok(next_slots((D1 + 600) * 10 ** 9, (D1 + 700) * 10 ** 9) == [D1 + 900]
       and next_slots((D1 + 894) * 10 ** 9, (D1 + 894) * 10 ** 9) == [D1 + 900]
       and next_slots((D1 + 895) * 10 ** 9, (D1 + 1000) * 10 ** 9) == [D1 + 1800]
       and next_slots((D1 + 500) * 10 ** 9, (D1 + 1000) * 10 ** 9) == [D1 + 900, D1 + 1800],
       "G-NEXT's slots: decided from the first removal to 900 s after the last")
    # the reward book's quiet before a removal
    sel = {"event": "select", "day": D1, "ok": True, "wall_ns": (D1 - 900) * 10 ** 9}
    st0 = {"event": "start", "pid": 3137952, "wall_ns": (D1 - 3600) * 10 ** 9}
    t = D1 + 3615
    ok(quiet([sel, st0], [3137952], t) is None and quiet([st0], [3137952], t) is not None
       and quiet([dict(sel, ok=False), st0], [3137952], t) is not None
       and quiet([dict(sel, wall_ns=(t - 4) * 10 ** 9), st0], [3137952], t) is not None
       and quiet([sel, st0], [3137952, 3200000], t) is not None
       and quiet([sel, st0, {"event": "start", "pid": 3200000, "wall_ns": (t - 9) * 10 ** 9}], [3200000], t)
       is not None
       and quiet([sel, st0, {"event": "start", "pid": 3200000, "wall_ns": (t - 10) * 10 ** 9}], [3200000], t)
       is None and quiet([sel], [], t) is None
       and quiet([dict(sel, day=D0), st0], [3137952], t) is not None,
       "a removal waits for the day's selection 5 s old and for a process with its start record 10 s old")
    # G-NEXT's verdicts on literal records
    good = {"pid": 3137952, "stopped": False, "error": None, "stream": {"opened": True, "off_reason": None}}
    ok(next_verdict([(0, good)], [], "3137952")[0] == "PASS"
       and next_verdict([], [], "3137952")[0] == "FAIL"
       and next_verdict([(0, good)], [{"error": "FileNotFoundError: x"}], "3137952")[0] == "FAIL"
       and next_verdict([(0, dict(good, stopped=True)), (1, dict(good, pid=3200000))], [], "3137952")[0]
       == "UNDECIDABLE"
       and next_verdict([(0, dict(good, stream={"opened": False, "off_reason": "floor"}))], [], "3137952")[0]
       == "UNDECIDABLE"
       and next_reading([("PASS", ""), ("UNDECIDABLE", "")]) == "UNDECIDABLE"
       and next_reading([("PASS", ""), ("FAIL", "")]) == "FAIL" and next_reading([("PASS", "")]) == "PASS"
       and next_reading([]) == "UNDECIDABLE",
       "G-NEXT: a slot without its slot.json or with an error record fails; the worst over the slots reads")
    # G-STILL's chain
    u = {"recorder": {"MainPID": "2388318", "NRestarts": "0", "ActiveState": "active"},
         "pairbook": {"MainPID": "3121425", "NRestarts": "11", "ActiveState": "active"},
         "rewardbook": {"MainPID": "3137952", "NRestarts": "1", "ActiveState": "active"}}
    moved = dict(u, pairbook={"MainPID": "3300002", "NRestarts": "13", "ActiveState": "active"})
    chain = [{"stopped": "3121425", "pid": "3300001", "NRestarts": 12},
             {"stopped": "3300001", "pid": "3300002", "NRestarts": 13}]
    m0 = D1 + 3600
    ok([trigger_reading(t, m0, s0_, lt)[0] for t, s0_, lt in (
        ({"unit": TIMER, "realtime_usec": str((m0 + 1800) * 10 ** 6)}, m0 + 1801, m0 + 9000),
        ({"unit": TIMER, "realtime_usec": str((m0 + 1798) * 10 ** 6)}, m0 + 1798, None),
        ({"unit": TIMER, "realtime_usec": str((m0 + 1797) * 10 ** 6)}, m0 + 1797, None),
        ({"unit": "btc-pairbook-archive.timer", "realtime_usec": str((m0 + 1800) * 10 ** 6)}, m0 + 1800, None),
        ({"unit": TIMER, "realtime_usec": str((m0 + 1800) * 10 ** 6)}, m0 + 1861, None),
        ({"unit": None}, m0 + 1800, m0 + 1800), (None, m0 + 3500, m0 + 3499), ({"unit": None}, m0 + 1800, m0 + 1805),
        ({"unit": None}, m0 + 1800, None))]
       == [True, True, False, False, False, True, True, False, False],
       "G-TRIGGER: the run's own trigger where systemd set it, else the timer's last; 1,800 s after the mark less 2")
    ok(still_reading(u, u, [])[0] and still_reading(u, moved, chain)[0]
       and not still_reading(u, moved, chain[:1])[0]
       and not still_reading(u, dict(moved, rewardbook=dict(u["rewardbook"], MainPID="3300009")), chain)[0]
       and not still_reading(u, dict(u, recorder=dict(u["recorder"], NRestarts="1")), [])[0],
       "G-STILL: the recorder and the reward book unchanged, the pair book unchanged or moved by its archive's chain")
    # both hooks, under the modes the run gives them
    s0 = ROOT + "/%d/%d.0.stream.jsonl.gz" % (D1, D1 + 900)
    j0 = ROOT + "/%d/%d.0.slot.json" % (D1, D1 + 900)
    r0 = ROOT + "/%d/%d.0.rewards.jsonl.gz" % (D1, D1 + 900)
    q0 = ROOT + "/%d/select.0.json" % D1

    def allow(mode, event, args, removable=frozenset()):
        return tz27.policy(mode, event, args, STATE, set(removable)) is None and policy34(mode, event, args) is None \
            if event != "os.remove" else (_allow_remove(mode, args, removable))

    def _allow_remove(mode, args, removable):
        saved = set(tz27.ALLOWED_REMOVE)
        tz27.ALLOWED_REMOVE.clear()
        tz27.ALLOWED_REMOVE.update(removable)
        try:
            return tz27.policy(mode, "os.remove", args, STATE, set(removable)) is None and \
                policy34(mode, "os.remove", args) is None
        finally:
            tz27.ALLOWED_REMOVE.clear()
            tz27.ALLOWED_REMOVE.update(saved)

    ok([allow(m, "open", (s0, "rb", 0)) for m in ("inventory", "upload", "delete", "verify", "final", "hold", "run")]
       == [True, True, True, False, False, False, False]
       and not any(allow(m, "open", (s0, fm, 0)) for m in ("inventory", "upload", "delete", "final")
                   for fm in ("wb", "ab", "r+b", "xb")),
       "a stream file is read by the set, the upload and the removal alone, and written by no mode")
    ok(not any(allow(m, "open", (p, "rb", 0)) for m in ("inventory", "upload", "delete", "final", "still")
               for p in (r0, q0, ROOT + "/service.log", ROOT + "/service.pid"))
       and allow("final", "open", (j0, "rb", 0)) and not allow("inventory", "open", (j0, "rb", 0))
       and allow("delete", "open", (ROOT + "/runtime.jsonl", "rb", 0))
       and allow("final", "open", (ROOT + "/runtime.jsonl", "rb", 0))
       and not allow("upload", "open", (ROOT + "/runtime.jsonl", "rb", 0)),
       "no rewards file or selection is read; slot.json by final alone; runtime.jsonl by delete and final")
    ok(allow("delete", "os.remove", (s0, None), {s0}) and not allow("delete", "os.remove", (s0, None))
       and not allow("upload", "os.remove", (s0, None), {s0}) and not allow("delete", "os.remove", (j0, None), {j0})
       and not allow("delete", "os.rename", (s0, STATE + "/x"), {s0})
       and allow("inventory", "os.scandir", (ROOT,)) and allow("final", "os.scandir", (ROOT + "/%d" % D1,))
       and not allow("upload", "os.scandir", (ROOT,)),
       "a stream file removed only by the removal, only where the run names it; the store listed by three modes")
    ok(not any(allow(m, ev, args) for m in ("inventory", "upload", "delete", "final", "still", "selftest")
               for ev, args in (("open", (PAIRBOOK + "/1793187000/window.json", "rb", 0)),
                                ("os.scandir", (PAIRBOOK,)), ("open", (PAIR_STATE + "/runs/1/set.json", "rb", 0))))
       and allow("still", "open", (PAIR_LEDGER, "rb", 0)) and not allow("final", "open", (PAIR_LEDGER, "rb", 0))
       and not allow("upload", "open", (PAIR_LEDGER, "rb", 0))
       and not allow("still", "open", (PAIR_LEDGER, "ab", 0))
       and not allow("final", "open", (tz27.RECORDER + "/runtime.jsonl", "rb", 0))
       and not allow("inventory", "subprocess.Popen", ("systemctl",)) and allow("hold", "subprocess.Popen", ("x",))
       and not allow("delete", "subprocess.Popen", ("systemctl",))
       and allow("run", "open", (STATE + "/ledger.jsonl", "ab", 0))
       and not allow("run", "open", (tz27.FORENSICS + "/x", "xb", 0)),
       "nothing of the pair book's store, its archive's ledger read by still alone, no process in the set or the "
       "removal, the run writes under its state alone")
    # the units, as this file reads them
    for unit, want in ((ARCHIVE, ["Type=oneshot", "WorkingDirectory=" + STATE, "ExecStart=" + " ".join(RUN_ARGV),
                                  "Restart=no", "TimeoutStartSec=%d" % TIMEOUT_S, "Nice=19", "MemoryMax=128M",
                                  "StandardOutput=append:%s/archive.log" % STATE,
                                  "StandardError=append:%s/archive.log" % STATE]),
                       (TIMER, ["OnCalendar=" + CALENDAR, "OnActiveSec=%d" % ACTIVE_S, "AccuracySec=1s",
                                "Unit=" + ARCHIVE, "WantedBy=timers.target"])):
        with open(os.path.join(os.path.dirname(HERE), "deploy", "systemd", unit), encoding="utf-8") as fh:
            lines = [ln for ln in fh.read().split("\n") if ln and not ln.startswith("#") and not ln.startswith("[")]
        ok(all(x in lines for x in want), "%s: %d of its lines as this file runs them" % (unit, len(want)))
    # the reward book's own constants and its own sum, read from its text
    tree = ast.parse(tz33_text())
    vals = tz33_values(tree, ("ROOT", "SVC", "PYTHON", "SERVICE_FILE", "SERVICE_ARGV", "DAY", "SLOT", "OPEN_BEFORE",
                              "SLOT_JSON_AT", "LAUNCH_LEAD", "STREAM_FLOOR", "STREAM_CAP", "SLOT_STREAM_MAX",
                              "DAY_RE", "SLOT_FILE_RE"))
    ok({k: vals[k] for k in RESTATED} == RESTATED and vals["PYTHON"] == tz27.PYTHON,
       "the reward book's %d constants this file restates, equal to its text's" % len(RESTATED))
    total33 = tz33_function(tree, "stream_bytes_total")
    # the run on temporary stores, a simulated reward book and the loopback server
    for k in [k for k in list(os.environ) if k.lower() in ("http_proxy", "https_proxy", "all_proxy", "no_proxy")]:
        del os.environ[k]
    tmp = tz27.wpath("selftest-tmp")
    if os.path.lexists(tmp):
        shutil.rmtree(tmp)
    tok = "ghp_" + "Ab3" * 12
    Fake = tz27._FakeGitHub
    Fake.releases.clear()
    Fake.assets.clear()
    Fake.hits.clear()
    Fake.refuse_once.clear()
    Fake.omit_digest[0] = False
    Fake.token = tok
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Fake)
    th = threading.Thread(target=srv.serve_forever, daemon=True)
    th.start()
    base = "http" + sep + "127.0.0.1:%d" % srv.server_address[1]
    Fake.web = base
    blobs = {}

    def put(root, s, name, nbytes):
        d = os.path.join(root, str(day_of(s)))
        os.makedirs(d, exist_ok=True)
        data = (hashlib.sha256(name.encode()).digest() * (nbytes // 32 + 1))[:nbytes]
        with open(os.path.join(d, name), "wb") as fh:
            fh.write(data)
        blobs[name] = data

    def slot(root, s, streams, closed=True):
        for k_, nb in enumerate(streams):
            if nb is not None:
                put(root, s, "%d.%d.stream.jsonl.gz" % (s, k_), nb)
            put(root, s, "%d.%d.rewards.jsonl.gz" % (s, k_), 300)
            if closed:
                put(root, s, "%d.%d.slot.json" % (s, k_), 200)

    def world(name, t0):
        root, state = os.path.join(tmp, name, "store"), os.path.join(tmp, name, "state")
        os.makedirs(root)
        os.makedirs(state)
        env = FakeEnv(tz27.WORK[0], root, state, base, t0, tok)
        for d in range(D0, D1 + 10 * DAY, DAY):
            env.recs.append({"event": "select", "day": d, "ok": True, "wall_ns": (d - 900) * 10 ** 9})
        env.recs.append({"event": "start", "pid": 3137952, "wall_ns": (D0 + 41400) * 10 ** 9})
        put(root, D0, "select.0.json", 500)
        return env

    def evs(env):
        return [r["event"] for r in tz28.Ledger(env.state).recs]

    try:
        # 1. a whole run: closed slots, a slot of two processes, a slot whose stream stayed off, an unclosed slot
        # and two open ones; the pair book's archive running at the upload phase
        env = world("one", D1 + 3600 + 20)
        slot(env.root, D1 - 1800, [70001])
        slot(env.root, D1 - 900, [50000, 33333])
        slot(env.root, D1, [None])
        slot(env.root, D1 + 900, [40000], closed=False)
        slot(env.root, D1 + 1800, [44444])
        slot(env.root, D1 + 2700, [55555])
        slot(env.root, D1 + 3600, [123], closed=False)
        ok(stream_bytes_view(env.root) == total33(env.root) == 70001 + 50000 + 33333 + 40000 + 44444 + 55555 + 123,
           "this file's sum of the store's streams equals the reward book's own, run from its text")
        env.busy_until = env.clock + 1000
        rc = run(env)
        led = tz28.Ledger(env.state).recs
        a = led[0]["run"]
        ok(rc == 0 and evs(env) == ["start", "set", "hold", "upload", "verify", "delete", "complete"]
           and a == D1 + 3620, "a run: every step recorded, in order, exit 0")
        setr = tz28.events(led, a, "set")[0]
        ok(setr["assets_n"] == 4 and setr["bytes_total"] == 197778 and setr["first_S"] == D1 - 1800
           and setr["last_S"] == D1 + 1800 and setr["tag"] == "rewardbook-streams-%d" % a
           and (setr["slots_considered"], setr["closed"], setr["unclosed"], setr["open"], setr["streamless"],
                setr["deferred"]) == (4, 3, 1, 2, 1, 0),
           "the set: every stream file of a closed slot due 60 s before A, under this TZ's tag")
        hr = tz28.events(led, a, "hold")[0]
        ok(hr["phase"] == "upload" and hr["waited_s"] == 1000, "the upload held while the pair book's archive ran")
        rel = Fake.releases["rewardbook-streams-%d" % a]
        held = sorted(v["name"] for v in Fake.assets.values() if v["rid"] == rel["id"])
        want = ["%d-%d.0.stream.jsonl.gz" % (D0, D1 - 1800), "%d-%d.0.stream.jsonl.gz" % (D0, D1 - 900),
                "%d-%d.1.stream.jsonl.gz" % (D0, D1 - 900), "%d-%d.0.stream.jsonl.gz" % (D1, D1 + 1800)]
        ok(held == sorted(want) and all(v["data"] == blobs[v["name"][11:]] for v in Fake.assets.values()
                                        if v["rid"] == rel["id"]),
           "the Release holds the set's four files, byte for byte")
        left = sorted(os.listdir(os.path.join(env.root, str(D1))))
        ok(sorted(os.listdir(os.path.join(env.root, str(D0)))) == sorted(
            ["%d.0.rewards.jsonl.gz" % (D1 - 1800), "%d.0.slot.json" % (D1 - 1800),
             "%d.0.rewards.jsonl.gz" % (D1 - 900), "%d.0.slot.json" % (D1 - 900), "%d.1.rewards.jsonl.gz" % (D1 - 900),
             "%d.1.slot.json" % (D1 - 900), "select.0.json"])
           and "%d.0.stream.jsonl.gz" % (D1 + 900) in left and "%d.0.stream.jsonl.gz" % (D1 + 2700) in left
           and "%d.0.stream.jsonl.gz" % (D1 + 3600) in left and "%d.0.stream.jsonl.gz" % (D1 + 1800) not in left
           and "%d.0.slot.json" % (D1 + 1800) in left,
           "the store: the set's files gone; slot.json, rewards, selections, the unclosed and the open streams kept")
        rdir = os.path.join(env.state, "runs", str(a))
        trs = tz28.jsonl_read(os.path.join(rdir, "transfers.jsonl"))
        rms = tz28.jsonl_read(os.path.join(rdir, "delete.jsonl"))
        comp = tz28.events(led, a, "complete")[0]
        ok(len([t for t in trs if t["kind"] == "upload"]) == 4 and len([t for t in trs if t["kind"] == "download"])
           == 4 and len(rms) == 4 and all(all(tz28.transfer_ok(t)) for t in trs)
           and all(all(tz28.transfer_ok(removal_span(r))) for r in rms)
           and comp["started_outside"] == 0 and comp["ended_outside"] == 0 and comp["removals"] == 4
           and all(h[2] == tz27.UA for h in Fake.hits)
           and all(h[3] is None for h in Fake.hits if "/releases/download/" in h[1] or h[1].startswith("/blob/")),
           "every request and every removal inside the idle stretch; reads with no token, every request TZ-27's")
        with open(os.path.join(env.state, "runs", str(a), "set.json"), "rb") as fh:
            raw1 = fh.read()
        doc1, sets1 = json.loads(raw1), tz28.events(led, a, "set")
        sl = store_left(env.root, doc1)
        ok(sl == (["%d.0.stream.jsonl.gz" % (D1 + 900)], [], [], []) and set_reading(doc1, raw1, sets1, *sl[1:]),
           "G-SET read on the store: the unclosed slot's stream left alone, nothing of a closed or unrecorded slot")
        put(env.root, D1 + 900, "%d.0.slot.json" % (D1 + 900), 200)
        put(env.root, D1 - 2700, "%d.0.stream.jsonl.gz" % (D1 - 2700), 10)
        sl2 = store_left(env.root, doc1)
        ok(sl2[2:] == (["%d.0.stream.jsonl.gz" % (D1 - 2700)], [D1 + 900]) and not set_reading(doc1, raw1, sets1,
                                                                                               *sl2[1:])
           and not set_reading(doc1, raw1, sets1 + sets1, *sl[1:])
           and not set_reading(dict(doc1, deferred=1), raw1, sets1, *sl[1:]),
           "G-SET fails on a stream of a slot it does not record, a slot.json not as recorded, two sets, a deferral")
        os.remove(os.path.join(env.root, str(day_of(D1 + 900)), "%d.0.slot.json" % (D1 + 900)))
        os.remove(os.path.join(env.root, str(day_of(D1 - 2700)), "%d.0.stream.jsonl.gz" % (D1 - 2700)))
        ok(comp["store_stream_bytes"] == 40000 + 55555 + 123 == stream_bytes_view(env.root)
           and tz28.events(led, a, "delete")[0]["freed"] == 197778
           and comp["rewardbook_at_end"]["MainPID"] == "3137952",
           "the store's streams after the run: the unclosed and the open slots' alone")
        # 2. the next run takes the slot that came due after the first run's A; the run after it finds none: empty
        env.clock += 300
        ok(run(env) == 0 and evs(env)[-1] == "complete", "the next run completes")
        set2 = [r for r in tz28.Ledger(env.state).recs if r["event"] == "set"][-1]
        ok(set2["assets_n"] == 1 and set2["bytes_total"] == 55555 and set2["first_S"] == set2["last_S"] == D1 + 2700
           and (set2["slots_considered"], set2["closed"], set2["unclosed"], set2["open"], set2["streamless"])
           == (3, 1, 2, 0, 4), "the next run takes the slot due after the first run's A, and only it")
        env.clock += 10
        ok(run(env) == 0 and evs(env)[-2:] == ["start", "empty"]
           and (tz28.Ledger(env.state).recs[-1]["slots_considered"], tz28.Ledger(env.state).recs[-1]["unclosed"])
           == (2, 2), "a run with no stream file of a closed slot records empty, exit 0")
        # 3. a refused credential defers, and the next run resumes the same set
        env3 = world("defer", D1 + 3600 + 588)
        slot(env3.root, D1 + 900, [1000])
        env3.cred_ok = False
        rc3 = run(env3)
        a3 = tz28.Ledger(env3.state).recs[0]["run"]
        ok(rc3 == tz28.EXIT_DEFERRED and evs(env3) == ["start", "set", "deferred"]
           and os.path.exists(os.path.join(env3.root, str(D1), "%d.0.stream.jsonl.gz" % (D1 + 900))),
           "a refused credential: deferred, exit 75, nothing removed")
        env3.cred_ok = True
        env3.clock += 86400
        ok(run(env3) == 0 and [r["run"] for r in tz28.Ledger(env3.state).recs if r["event"] == "start"] == [a3, a3]
           and evs(env3)[-1] == "complete", "the next run resumes the deferred set and completes it")
        trs3 = tz28.jsonl_read(os.path.join(env3.state, "runs", str(a3), "transfers.jsonl"))
        ok(tz28.phase_of(trs3[0]["start_ns"] // 10 ** 9) == 15 and all(all(tz28.transfer_ok(t)) for t in trs3),
           "a request due at second 588 waits for the next idle stretch")
        # 4. three deferrals halt the archive; a halted archive refuses until a clear
        env4 = world("halt", D1 + 3 * 86400 + 20)
        slot(env4.root, D1 + 900, [1000])
        env4.cred_ok = False
        rcs = [run(env4) for _k in range(3)]
        ok(rcs == [tz28.EXIT_DEFERRED, tz28.EXIT_DEFERRED, 1] and evs(env4)[-2:] == ["halt", "timer-disabled"]
           and env4.disabled == 1, "the third deferral of one set halts, and the run disables its timer")
        env4.cred_ok = True
        ok(run(env4) == 1 and evs(env4)[-1] == "refused" and env4.disabled == 2
           and os.path.exists(os.path.join(env4.root, str(D1), "%d.0.stream.jsonl.gz" % (D1 + 900))),
           "a halted archive refuses the next run, and removes nothing")
        tz28.jsonl_append(os.path.join(env4.state, "ledger.jsonl"), {"event": "clear", "run": None, "wall_ns": 0}, "x")
        env4.clock += 60
        ok(run(env4) == 0 and evs(env4)[-1] == "complete", "after a clear the next run takes a new set")
        # 5. a flipped bit in one asset fails the verify: deferred, nothing removed; mended, the next run completes
        env5 = world("verify", D1 + 5 * 86400 + 20)
        slot(env5.root, D1 + 900, [5000, 6000])

        def corrupt(e):
            if e.on_sleep is corrupt:
                e.on_sleep = None
                k_ = sorted(Fake.assets)[-1]
                good_ = Fake.assets[k_]["data"]
                Fake.assets[k_]["data"] = good_[:-1] + bytes([good_[-1] ^ 1])
                corrupt.saved = (k_, good_)

        env5.on_sleep = corrupt
        ok(run(env5) == tz28.EXIT_DEFERRED and evs(env5)[-1] == "deferred"
           and "VERIFY FAIL" in tz28.Ledger(env5.state).recs[-1]["reason"]
           and os.path.exists(os.path.join(env5.root, str(D1), "%d.1.stream.jsonl.gz" % (D1 + 900))),
           "a flipped bit in one asset: VERIFY FAIL, deferred, nothing removed")
        k5, good5 = corrupt.saved
        Fake.assets[k5]["data"] = good5
        ok(run(env5) == 0 and evs(env5)[-1] == "complete", "the asset mended, the next run verifies and completes")
        # 6. the day's selection missing at the removal: the removals wait for it, 5 s after its record
        env6 = world("select", D1 + DAY + 3600 + 20)
        slot(env6.root, D1 + DAY + 900, [7000])
        env6.recs = [r for r in env6.recs if r.get("day") != D1 + DAY]
        late = (D1 + DAY + 3600 + 20 + 600) * 10 ** 9

        def appear(e):
            if e.time_ns() >= late and not [r for r in e.recs if r.get("day") == D1 + DAY]:
                e.recs.append({"event": "select", "day": D1 + DAY, "ok": True, "wall_ns": late})

        env6.on_sleep = appear
        ok(run(env6) == 0 and evs(env6)[-1] == "complete", "the removal waited for the day's selection and completed")
        r6 = tz28.jsonl_read(os.path.join(env6.state, "runs", str(D1 + DAY + 3620), "delete.jsonl"))[0]
        ok(r6["start_ns"] >= late + 5 * 10 ** 9 and all(tz28.transfer_ok(removal_span(r6))),
           "the first removal 5 s or more after the selection's record, inside the idle stretch")
        # 7. the selection never recorded: the removals defer after QUIET_MAX_S; recorded, the next run completes
        env7 = world("quiet", D1 + 2 * DAY + 3600 + 20)
        slot(env7.root, D1 + 2 * DAY + 900, [7000, 8000])
        env7.recs = [r for r in env7.recs if r.get("day") != D1 + 2 * DAY]
        ok(run(env7) == tz28.EXIT_DEFERRED and tz28.Ledger(env7.state).recs[-1]["phase"] == "delete"
           and "QuietTimeout" in tz28.Ledger(env7.state).recs[-1]["reason"]
           and os.path.exists(os.path.join(env7.root, str(D1 + 2 * DAY),
                                           "%d.0.stream.jsonl.gz" % (D1 + 2 * DAY + 900))),
           "the selection never recorded: the run defers in its removal, nothing removed")
        env7.recs.append({"event": "select", "day": D1 + 2 * DAY, "ok": True, "wall_ns": (D1 + 2 * DAY) * 10 ** 9})
        env7.clock += 3600
        ok(day_of(env7.clock) == D1 + 2 * DAY and run(env7) == 0 and evs(env7)[-1] == "complete"
           and evs(env7).count("verify") == 2,
           "the next run resumes the set - its uploads held, verified again - and completes the removal")
        # 8. a removal deferred half-way: the files removed recorded, the rest removed by the next run
        env8 = world("partial", D1 + 3 * DAY + 3600 + 20)
        slot(env8.root, D1 + 3 * DAY + 900, [1000, 2000, 3000])
        p8 = os.path.join(env8.state, "runs", str(D1 + 3 * DAY + 3620), "delete.jsonl")
        env8.pids_fn = lambda e: [3300000] if len(tz28.jsonl_read(p8)) >= 2 else [3137952]
        rc8 = run(env8)
        ok(rc8 == tz28.EXIT_DEFERRED and len(tz28.jsonl_read(p8)) == 2
           and "QuietTimeout" in tz28.Ledger(env8.state).recs[-1]["reason"],
           "a new process without its start record: the removals wait, then defer with two of three files removed")
        env8.pids_fn = None
        env8.clock += 3600
        ok(run(env8) == 0 and len(tz28.jsonl_read(p8)) == 3
           and tz28.events(tz28.Ledger(env8.state).recs, D1 + 3 * DAY + 3620, "delete")[-1]["already"] == 2,
           "the next run resumes: two removals already recorded, the third removed")
        # 9. a file changed after the verify: the removal finds it is not the set's, and the archive halts
        env9 = world("changed", D1 + 4 * DAY + 3600 + 20)
        slot(env9.root, D1 + 4 * DAY + 900, [4000])
        env9.recs.append({"event": "select", "day": D1 + 4 * DAY, "ok": True, "wall_ns": 0})
        p9 = os.path.join(env9.root, str(D1 + 4 * DAY), "%d.0.stream.jsonl.gz" % (D1 + 4 * DAY + 900))

        def grow(e):
            if e.on_sleep is grow and tz28.events(tz28.Ledger(e.state).recs, D1 + 4 * DAY + 3620, "upload"):
                e.on_sleep = None
                with open(p9, "ab") as fh:
                    fh.write(b"x")

        env9.on_sleep = grow
        ok(run(env9) == 1 and evs(env9)[-2:] == ["halt", "timer-disabled"]
           and "not the set's" in tz28.Ledger(env9.state).recs[-2]["reason"] and os.path.exists(p9),
           "a stream file changed after its verify: the removal refuses it and the archive halts")
        # 10. the pair book's archive running past HOLD_MAX_S: the run defers before its upload
        env10 = world("hold", D1 + 5 * DAY + 3600 + 20)
        slot(env10.root, D1 + 5 * DAY + 900, [3000])
        env10.busy_until = env10.clock + HOLD_MAX_S + 100
        ok(run(env10) == tz28.EXIT_DEFERRED and "HoldTimeout" in tz28.Ledger(env10.state).recs[-1]["reason"]
           and tz28.Ledger(env10.state).recs[-1]["phase"] == "upload" and not Fake.releases.get(
               "rewardbook-streams-%d" % (D1 + 5 * DAY + 3620)),
           "a hold past 1,800 s defers the run before any request")
        ok(not [h for h in Fake.hits if h[3] not in (None, "Bearer " + tok)],
           "the loopback server saw no credential but the run's")
    finally:
        srv.shutdown()
        srv.server_close()
    shutil.rmtree(tmp)
    ok(not os.path.lexists(tmp), "the temporary stores removed")
    with open(os.path.abspath(__file__), encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    mods = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            mods |= {x.name.split(".")[0] for x in node.names}
        elif isinstance(node, ast.ImportFrom):
            mods.add((node.module or "").split(".")[0])
    ok(mods <= set(sys.stdlib_module_names), "imports: the standard library alone")
    ok(not [c_ for c_ in ast.walk(tree) if isinstance(c_, ast.Constant) and isinstance(c_.value, str)
            and sep in c_.value], "no endpoint in this file's text: every request is TZ-27's")
    out("%d of %d checks passed" % (n[0], n[0]))


def main(argv):
    if not argv:
        sys.exit("usage: tz34-rewardbook-archive-timer.py MODE [ARG...]")
    mode, rest = argv[0], argv[1:]
    rc = 0
    if mode == "run":
        assert not rest, "run takes no argument"
        rc = mode_run()
    else:
        cwd = os.getcwd()
        assert tz27.WORK_RE.fullmatch(cwd), "run from a work tree /root/tzNN-work, not %s" % cwd
        tz27.WORK[0], tz27.MODE[0] = cwd, mode
        if mode == "mark":
            assert len(rest) == 1, "mark NAME"
            mode_mark(rest[0])
        elif mode == "scratch":
            assert len(rest) == 1, "scratch OWN"
            tz27.mode_scratch(rest[0])
        elif mode == "reclaim":
            tz27.mode_reclaim(rest)
        elif mode == "still":
            assert not rest, "still takes no argument"
            rc = 0 if mode_still() else 1
        elif mode == "first":
            assert not rest, "first takes no argument"
            rc = mode_first()
        else:
            table = {"fingerprint": mode_fingerprint, "selftest": mode_selftest, "path": tz28.mode_path,
                     "path-token": tz28.mode_path_token, "installed": mode_installed, "timer": mode_timer,
                     "final": mode_final, "stopped": mode_stopped}
            assert mode in table and not rest, "unknown mode %r" % (argv,)
            table[mode]()
    out("peak memory of this run: %d bytes" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024))
    out("opens refused: %d by TZ-27's hook, %d by this file's; store opens %d; requests %d, uploads %d, downloads %d "
        "(%d bytes); files removed %d" % (len(tz27.REFUSED), len(REFUSED34), tz27.STORE_OPENS[0],
                                          tz27.COUNTERS["requests"], tz27.COUNTERS["uploads"],
                                          tz27.COUNTERS["downloads"], tz27.COUNTERS["download_bytes"],
                                          tz27.COUNTERS["removed"]))
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
```

### `deploy/systemd/btc-rewardbook-archive.service`

```ini file=deploy/systemd/btc-rewardbook-archive.service
# btc-5m-twap: the reward book's archive, its closed slots' stream files moved verbatim to a Release (TZ-34).
# Started by btc-rewardbook-archive.timer alone; installed byte for byte as /etc/systemd/system/btc-rewardbook-archive.service.
[Unit]
Description=btc-5m-twap reward book archive, the stream files of closed slots to a Release
Wants=network-online.target
After=network-online.target time-sync.target btc-rewardbook.service

[Service]
Type=oneshot
WorkingDirectory=/var/lib/btc-rewardbook-archive
ExecStart=/root/tz04a-env/venv/bin/python -B -u /root/btc-rewardbook-archive-svc/tz34-rewardbook-archive-timer.py run
Restart=no
TimeoutStartSec=21600
Nice=19
MemoryMax=128M
StandardOutput=append:/var/lib/btc-rewardbook-archive/archive.log
StandardError=append:/var/lib/btc-rewardbook-archive/archive.log
```

### `deploy/systemd/btc-rewardbook-archive.timer`

```ini file=deploy/systemd/btc-rewardbook-archive.timer
# btc-5m-twap: the reward book's archive, daily at 01:30:20 UTC and 1,800 s after the timer starts (TZ-34).
# Installed byte for byte as /etc/systemd/system/btc-rewardbook-archive.timer; its stop is systemctl disable --now.
[Unit]
Description=btc-5m-twap reward book archive, once a day

[Timer]
OnCalendar=*-*-* 01:30:20 UTC
OnActiveSec=1800
AccuracySec=1s
Unit=btc-rewardbook-archive.service

[Install]
WantedBy=timers.target
```
