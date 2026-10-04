# TZ-21 — the recorder's memory, bounded

**Canonical filename:** `TZ-21-recorder-memory.md`. The committed file takes this name and no other.

**Executor model: Opus.** A change to the running capture's code, its restart, and the data a wrong slice
would corrupt.

**Required System Map revision:** `2026-10-04-b`.

**Required anchors**, from map §0. A mismatch on any one is BLOCKED before any work:

| anchor | required |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` |
| `A6` — pricer | `729f0bcdbee3` |

**Host gate:** §0.2. This TZ touches the capture host and runs nowhere else.

**What this TZ is.** The recorder keeps every runtime record it has ever read or written in one list for the
life of the process, so its memory grows by about `3.2` MB a day and never falls. This TZ changes
`research/recorder/recorder.py` so the process holds only the records a slice served from memory can still
read — two hours of clock samples, every `start` record and the disconnects that end inside those two hours —
and slices an older window from `runtime.jsonl` on disk, **so every slice it writes is byte for byte the one
the old code writes.** It proves that before the code runs, twice: on synthetic histories (G-SYNTH) and on a
snapshot of the capture's own `runtime.jsonl` (G-EQUIV). It then moves the unit's tree to the branch, proves
the new code's request path (G-PATH), restarts the recorder once by `SIGTERM` (G-RESTART), and proves the new
process captures and slices as the old one did (G-REC, G-FINAL). **It changes no unit file and no memory
ceiling:** TZ-22 sets both units' ceilings from what the bounded process measures. The chain book is read and
never touched.

---

## 0. Gates

### 0.0 The work tree, first

After contract §1 steps 1 and 2, and before anything else:

```
mkdir /root/tz21-work /root/tz21-work/logs; echo "exit=$?"
```

`exit=0` proves neither existed; anything else is BLOCKED. **From here every command's output goes to
`/root/tz21-work/logs/`, one file per step, §0's included**, and nothing to the session's scratchpad — so no
output of this TZ lives outside the tree §9 reclaims (TZ-20 report §6 item 2). The one exception is
B-RECLAIM-OWN, §9.

### 0.1 Fingerprint

Contract §1 steps 3 and 4, against `SYSTEM-MAP.md` at `main` after contract §1's pull: revision string
`2026-10-04-b`; the six anchors above, `A2`, `A4`, `A5` and `A6` re-derived as the first 12 hex characters of
those files' SHA-256; the §0 table's **31** rows hashed in lines, bytes and SHA-256 — **28** `frozen` rows equal
to the map, **2** `tracked` and **1** `reported` row printed. Any mismatch is BLOCKED.

### 0.2 Host gate

From `/root/btc-5m-twap`, with `S` first set to this session's scratchpad directory as the session's own
environment names it, output verbatim into `logs/01-host-gate.log`:

```
date -u; date -u +%s
nproc; grep -E '^(MemTotal|MemAvailable|SwapTotal|SwapFree):' /proc/meminfo
df -B1 --output=source,size,avail /var/lib/btc-recorder
find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
grep -c 4216c04673ced76b5b2ac60ef57c9abedc46f9b9 /var/lib/btc-recorder/runtime.jsonl
systemctl --version | head -1
systemctl is-enabled btc-recorder.service btc-chainbook.service; echo "exit=$?"
systemctl is-active btc-recorder.service btc-chainbook.service; echo "exit=$?"
pgrep -fx '/root/tz04a-env/venv/bin/python -B -u recorder.py'; echo "exit=$?"
pgrep -fx '/root/tz01-env/venv/bin/python -B -u /root/tz18a-svc/tz18a-chainbook-capture.py --serve'; echo "exit=$?"
cmp deploy/systemd/btc-recorder.service /etc/systemd/system/btc-recorder.service; echo "exit=$?"
cmp deploy/systemd/btc-chainbook.service /etc/systemd/system/btc-chainbook.service; echo "exit=$?"
git -C /root/btc-recorder-svc rev-parse HEAD
journalctl -u btc-recorder.service -u btc-chainbook.service --since @1791102470 --no-pager -o short-iso
du -sb /root/PROJECT_GAMING_PS5
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
systemctl is-active telemetry-watch.service; echo "exit=$?"
for d in /root/tz16a-work /root/tz19-work /root/tz20-work /root/tz18a-svc /root/btc-recorder-svc; do test -e "$d"; echo "$d exit=$?"; done
find /root/btc-forensics -type f | wc -l
/root/tz04a-env/venv/bin/python -c 'import sys, websockets; print(sys.version.split()[0], websockets.__version__)'
git worktree list
du -sb /root/.claude
echo "$S"; ls -la "$(dirname "$(dirname "$S")")"
```

- **H1** — `find` prints exactly one path.
- **H2** — `df` names source `/dev/vda2` and size `31612203008`; `grep -c` prints at least `1`. With H1 this is map
  §6's host identity.
- **H3 — both units run.** `is-enabled` prints `enabled` twice and `exit=0`; `is-active` prints `active` twice and
  `exit=0`; each `pgrep -fx` prints exactly one pid and `exit=0`. This TZ restarts the recorder and reads the chain
  book across the session, so either down is BLOCKED.
- **H4** — both `cmp` exit `0`: the installed units are `main`'s `deploy/systemd/` byte for byte, TZ-20's.
- **H5** — `/root/btc-recorder-svc` is at `4216c04673ced76b5b2ac60ef57c9abedc46f9b9`.
- **H6 — trees.** `/root/tz16a-work`, `/root/tz19-work` and `/root/tz20-work` exit `1`; `/root/tz18a-svc` and
  `/root/btc-recorder-svc` exit `0`. Anything else is BLOCKED.
- **H7** — the forensic store holds exactly `1,438` files (TZ-20 report §2.17).
- **H8** — the interpreter prints `3.12.` and a `websockets` version; an import error is BLOCKED.
- **H9** — `git worktree list` names `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else.
- **Memory gate** — `MemAvailable` at least `110,000,000` bytes (§0.3).
- **Disk gate** — `avail` at least `2,300,000,000` bytes (§0.3).
- `date`, `nproc`, the other three `/proc/meminfo` lines, `systemctl --version`, the journal since TZ-20's
  `I final`, `du` and both `systemctl` reads of `telemetry-watch.service`, `du` of `/root/.claude`, `S` and its
  parent's listing are printed and carry no threshold. **The listing names the scratch directories earlier
  sessions left** — every directory beside this session's own whose name is a UUID — which §9's
  B-RECLAIM-SCRATCH removes.

**S1 to S7**, the instrument's `state` mode, complete the gate (§3.2). They are asserts, and any failure is
BLOCKED with nothing moved and nothing restarted.

### 0.3 Resource floors, in exact bytes, derived from map §6

**Disk.** Free space on `/dev/vda2` at least **`2,300,000,000`** bytes: the chain book's own floor,
`RESOURCE_FLOOR` = `2,200,000,000` (`research/tz18a-chainbook-capture.py` line 79), which it asserts before
every window, plus `100,000,000` for this session. The session's writes stay well inside that: the branch
worktree about `4,500,000` bytes (`origin/main`'s tree is `4,400,253`); G-SYNTH's synthetic tree `19,660,884`;
G-EQUIV's snapshot the size of `runtime.jsonl` — about `25,300,000` bytes at S3's bound of `120,000` records,
removed by G-EQUIV itself once it passes; `/root/btc-recorder-svc` growing from `608,103` bytes at `4216c04` to
about `4,500,000` at the branch head; the logs under `2,000,000`; and the capture's own growth over three hours,
`4,204,105` at map §6's `33,632,842` bytes a day. The recorder's own floor, `FREE_SPACE_FLOOR_BYTES` =
`2,000,000,000` (`config.py` line 21), sits below it. Every free-space read is reported with its UTC instant,
its reader and this bound.

**Memory.** `MemAvailable` at least **`110,000,000`** bytes: twice the largest peak any mode of the instrument
reached in the Architect's run of it under the host's interpreter, Python 3.12.3 — G-SYNTH's `54,984,704`
bytes. G-EQUIV reached `40,513,536` on a `runtime.jsonl` of `66,502` records: it never holds the old list,
only the records its windows can select (§4.2). Map §6 records the host's memory: `1,002,127,360` bytes in
all, `271,712,256` available at TZ-20's close. **`synth` and `equiv` re-read `MemAvailable` at their start
and stop, BLOCKED, below this floor.** Every mode runs under `nice -n 19`, so the instrument yields the CPU to
the capture whenever both want it.

### 0.4 Refs

`git ls-remote origin` before the branch of §3.1 exists, every ref reported. Map §1 records `main` at
`c7a45ff2d8a6e78b36215107e0c055eb296e5d8b`, PR #21's merge, `main` the only branch, and 25 ref lines. The upload
that carries this TZ and revision `2026-10-04-b` sits above it. A difference is recorded, not BLOCKING, unless
`main` does not carry revision `2026-10-04-b` or `refs/heads/tz-21-recorder-memory` already exists — either is
BLOCKED.

---

## 1. Why this TZ exists

**The mechanism** — `recorder.py` at `4216c04`, the code the unit runs. `load_runtime` reads every line of
`runtime.jsonl` into `self.runtime` at start (lines 233–242), and `record` appends every record the process
writes to the same list before it writes it to the file (lines 244–247). Nothing ever removes one. The process
writes two `clock` records a minute — one per server of `config.NTP_SERVERS`, every `NTP_SAMPLE_S` = `60` s
(`config.py` lines 73–74; `recorder.py` lines 511–526) — `2,880` a day, and a `disconnect` at each reconnect.
The list is read in one place, `write_runtime_slice` (lines 481–494), which takes from it the `start` records
active over a window and the `clock` and `disconnect` records inside it.

**What it costs, measured.** Under the host's interpreter, Python 3.12.3, the Architect measured `68,251,648`
bytes of resident memory for a list of the `60,786` records TZ-20's `I final` counted — `1,122.8` bytes a record,
**about `3,233,717` bytes more every day, for the life of the process, and all of it again at every start.**
Running the old and the new code side by side for an hour on copies of one `66,502`-record file, each capturing
the live venue, the old process ended the hour at `108,130,304` bytes resident and the new at `33,247,232`
(§10). TZ-20 read the unit's control group at `91,164,672` bytes 30 s after its second start, page cache included
(TZ-20 report §2.14); what share of that is the process's own heap was not read, and this TZ's reads add it
(`memory.stat`, §3.8).

**Why a ceiling is not the repair.** A ceiling only schedules the failure. Under TZ-20's `MemoryMax=512M` the
list alone fills it at about `457,700` records, some `138` days after TZ-20's close [modelled]; the kernel then
kills the process, systemd restarts it, and the new process reloads the whole file into a ceiling it no longer
fits — five starts in an hour, and the unit is `failed`. A tighter ceiling brings that day closer. TZ-20's two
ceilings were written from an assumption, not from a measurement (map §7 item 88), and **no ceiling can be
derived from a process whose memory grows with its age.** So this TZ bounds the memory, and TZ-22 sizes the
ceilings on the bounded process.

**The repair** — the new `recorder.py`, Appendix A.1, `0f6c9045…`:

1. `RUNTIME_KEEP_S` = `7200` (line 42), and `self.runtime_from_ns` beside `self.runtime` (lines 233–234).
2. `load_runtime` sets `runtime_from_ns` two hours before the load and keeps a record only if `kept` accepts it
   (lines 239–249); `runtime_file_records` is the old parse, line for line, as a generator (lines 251–261).
3. `kept` refuses a `clock` with `recv_ns` below `runtime_from_ns` and a `disconnect` with `end_recv_ns` below
   it, and accepts every other record — every `start` among them (lines 263–276).
4. `prune_runtime` raises `runtime_from_ns` to two hours before now and filters the list at once (lines
   278–282); `close_interval` calls it after each slice (line 379).
5. `write_runtime_slice` reads its `clock` and `disconnect` records from memory when the window's `lo` is at or
   above `runtime_from_ns`, and from `runtime.jsonl` otherwise (lines 529–531). **Nothing else in it moved.**

`config.py` and `manifest.py` are unchanged, and no other line of `recorder.py` moved: the diff is 49
insertions and the 6 replaced lines §10 C3 names.

**Why every slice is unchanged — the whole argument.** A slice of a window `[lo, hi]` is the `start` records
active over it, then, in list order, every `disconnect` with `start_recv_ns <= hi` and `end_recv_ns >= lo` and
every `clock` with `lo <= recv_ns <= hi` (old lines 479–494, new 520–537). The new list lacks only a `clock`
below `runtime_from_ns` and a `disconnect` that ended below it, and `runtime_from_ns` only rises, each rise
filtering at once.

- **From memory**, `lo >= runtime_from_ns`: every record the window selects has `recv_ns >= lo` or
  `end_recv_ns >= lo`, so none was dropped; a filter keeps order; every `start` is kept. The same bytes.
- **From disk**, `lo < runtime_from_ns`: `runtime.jsonl` holds every record the old list held, in its order,
  because both are the file's records at load followed by every record `record` appended to both. **One
  exception, and it cannot reach a slice:** a line torn by a dying process absorbs the next process's first
  record, its `start`, which the old list held and the file cannot parse — and the slice takes its `start`
  records from memory on both paths (new line 522), only `clock` and `disconnect` records from the file.
- **A live window is always served from memory:** it is sliced by about `T0 + 3,630` — S7's deadline at
  `T0 + 3,600` (new line 437) and one last fetch and poll (lines 440 and 450) — `3,720` s after its `lo`, against
  `7,200`. Only a window recovered after an outage of more than about two hours is read from disk. **The
  argument does not depend on that bound:** a later slice takes the other path and writes the same bytes.

**What this TZ decides.**

1. **The new `recorder.py` on the branch `tz-21-recorder-memory`, with the instrument
   `research/tz21-recorder-memory.py`.** Main carries both only once the Boss merges after the verdict.
2. **Equivalence before deployment.** G-SYNTH compares the old and the new code slice for slice on four
   synthetic histories — a steady run with late and out-of-order closes, a 158,581 s outage and the recovery
   after it, a torn tail, ten days of one process — with two negative controls; G-EQUIV does the same over a
   snapshot of the capture's own `runtime.jsonl`, on both paths.
3. **Deployment by one checkout.** B-MOVE moves `/root/btc-recorder-svc` to the branch head. The unit file, its
   argv, its working directory and its ceiling do not change; `git_sha()` then names the branch head in every
   `start` record (lines 55–62). The running process is untouched by the move: it loaded its code at its
   start, and nothing it runs opens a file of its tree.
4. **One restart.** B-KILL-REC sends `SIGTERM` at the instant TZ-20's B-KILL-REC used, after the `tau = 180` read
   and inside one window alone, so one interval loses `complete`; systemd starts the new code 5 s later.
5. **The proof in production.** G-REC reads the first five qualifying intervals of the new process and compares
   every slice it wrote — those five and every interval it closed before them — with the old code's slice over
   the same records.
6. **The unit runs the branch head from B-KILL-REC on**, as TZ-18a's and TZ-20's processes ran theirs before their
   merges. On a FAIL, K-21 puts it back on `4216c04` (§4.7). The revision after the merge moves `A5` and the
   recorder's frozen row.
7. **Nothing this work no longer needs stays on the host** (CANON hard rule 15): §9 removes this TZ's tree and the
   scratch directories earlier sessions left under `/tmp`.

---

## 2. Scope

**Repository paths this TZ may write, and no others:**

1. `research/recorder/recorder.py`, replaced, and `research/tz21-recorder-memory.py`, new — byte for byte
   Appendix A's, on branch `tz-21-recorder-memory`, then a pull request. Not merged by the Executor.
2. `CryptoReports/TZ-21-recorder-memory-report.md` — straight to `main`, in one commit. **The one path pushed to
   `main`, and the exemption to item 5 below.**

**Host paths this TZ may write:** `/root/tz21-work/**` — the branch worktree `wt`, `logs/`, `state.json` and
`scratch/`; `/root/btc-recorder-svc`, whose checkout B-MOVE moves to the branch head and K-21a or K-21 moves back
on a FAIL, and nothing else of it; and `/root/btc-forensics/`, by exclusive create only (§9). **Host paths it
removes, under §9 and nothing else:** `/root/tz21-work/` with its worktree, and the earlier sessions' scratch
directories §0.2's listing names. **The recorder writes its own tree**, as it always has:
`/var/lib/btc-recorder/**`, its log included. That is the capture's work, not this TZ's.

**Prohibited, each absolutely:**

1. No committed file but `research/recorder/recorder.py` is modified, and that one only on the branch. **That is
   the exemption this TZ names to map §0's `frozen` rule:** every other `frozen` row is byte-identical at run end.
2. **Under `/var/lib/btc-recorder/` this TZ opens only the top-level `runtime.jsonl` and, of the intervals G-REC
   compares, `manifest.json` and `runtime.jsonl`** — read-only — and it stats, without
   opening, the `manifest.json` of each interval that opens in the `3,900` s before the restart. **Under
   `/var/lib/btc-chainbook/` it opens nothing.** The instrument's audit hook refuses any other open there (V12).
   **Exemptions, each named because this TZ's body requires it:** (a) §0.2's `grep -c` and `find`; (b) §3.8's
   `tail -n 40` of `recorder.log`, whose lines carry statuses, counts and times and no price (`recorder.py`
   lines 340–342 at `4216c04`, 381–383 on the branch). No quote file, `gamma.json`, `resolution.json`, stream or
   `window.json` is opened by this TZ. The recorder's own reads at its start — `load_runtime`, `last_frame_ns`
   and `recover` — are the capture's work, and nothing of them is printed.
3. Nothing under either capture root is created, moved or removed by this TZ's commands.
4. `/root/tz04a-env/`, `/root/tz01-env/`, `/root/btc-forensics/` and `/root/tz18a-svc/` are not modified, emptied
   or removed. **Exemption:** §9 adds files to `/root/btc-forensics/` by exclusive create.
5. Nothing is pushed to `main` except the report of item 2 above.
6. **No price, size, spread, mid, book level, outcome or label is read, printed or written.** G-PATH prints status,
   byte count, whether a body parses and token ids, SNTP offsets and round trips, and of RTDS frames their count
   and topics — map §2.5's deployment exception — and nothing else of any body. The runtime records the
   instrument reads carry clock offsets, times and disconnects, and no price. **Two further exemptions, both
   §9's:** `reclaim` reads the reports for runs of hex characters alone, and it hashes and copies whole files,
   without extracting or printing any value from them.
7. **Requests:** G-PATH's two HTTP requests, two SNTP bursts and one RTDS subscription of at most 30 s, each
   through the new recorder's own functions, and `git` against `origin` with the pull request. Nothing else is
   requested by this TZ; the unit's traffic is the capture's.
8. **No process is signalled** except by B-KILL-REC and, on a FAIL, §4.7's blocks. The chain book is never
   signalled.
9. **No unit is created, changed, enabled, disabled, started or stopped**, except, on a FAIL alone, K-21's
   `systemctl restart btc-recorder.service` and K-20R's `systemctl disable --now btc-recorder.service`. The chain
   book's unit and `telemetry-watch.service` are read only.
10. No Release is created, and no dataset, archive or binary enters git history.

---

## 3. The work, in this order

Every command's output goes to `/root/tz21-work/logs/`, one file per step, and is quoted in the report.
`nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz21-work/wt/research/tz21-recorder-memory.py` is written
`I` below; a mode is `I <mode>`. It is the recorder's own interpreter, so the instrument loads both recorders
exactly as the unit does, and `-B` leaves no `__pycache__` in any tree.

**§9's B-RECLAIM-SCRATCH runs after §3.2 and before §3.3; its B-RECLAIM-OWN runs last, after §3.8.**

**Where the session's permission classifier refuses a command of a block named B-… or K-…**, the Executor
prints the block, the Boss runs it verbatim in a root shell on the VPS, and the Executor waits and then verifies
it through the reads this TZ names — never from the Boss's account. **Every `mark` is the Executor's**, taken
before its block is run or handed over.

### 3.1 The branch and its two files

```
git -C /root/btc-5m-twap fetch origin
git -C /root/btc-5m-twap worktree add -b tz-21-recorder-memory /root/tz21-work/wt origin/main
```

Then extract Appendix A from this TZ as `main` carries it, with this script, verbatim:

```
/root/tz04a-env/venv/bin/python -B - <<'EOF'
import hashlib, os
SRC = "/root/tz21-work/wt/CryptoTZ/TZ-21-recorder-memory.md"
WANT = {
    "research/recorder/recorder.py": "0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7",
    "research/tz21-recorder-memory.py": "d6d2dc195809f2160fda7856980d8ccfbf0006ba0836943ff789c877f9d5795f",
}
REPLACES = {
    "research/recorder/recorder.py": "9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03",
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
    path = os.path.join("/root/tz21-work/wt", name)
    if name in REPLACES:
        with open(path, "rb") as fh:
            assert hashlib.sha256(fh.read()).hexdigest() == REPLACES[name], name + " is not the frozen file"
        mode = "wb"
    else:
        mode = "xb"
    with open(path, mode) as fh:
        fh.write(data)
    print(name, data.count(b"\n"), len(data), hashlib.sha256(data).hexdigest())
EOF
```

| path | lines | bytes | SHA-256 |
|---|---|---|---|
| `research/recorder/recorder.py` | 651 | 27,821 | `0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7` |
| `research/tz21-recorder-memory.py` | 1,284 | 59,009 | `d6d2dc195809f2160fda7856980d8ccfbf0006ba0836943ff789c877f9d5795f` |

Commit the two files alone on the branch, push it with `git push -u origin tz-21-recorder-memory`, and open the
pull request against `main`. A failed assert here is BLOCKED.

### 3.2 State — the rest of the host gate

`I state`, before anything is moved. It must print `STATE PASS: S1 to S7`:

- **S1, S2** — G-UNIT of TZ-20 §4.1 for both units, at TZ-20's `MemoryMax`, `NRestarts` read and not asserted, and
  each MainPID the only process with an argument ending in `recorder.py`, or in `tz18a-chainbook-capture.py`.
- **S3** — `runtime.jsonl` read whole: its newest `start` names `4216c04673ced76b5b2ac60ef57c9abedc46f9b9`, and it
  holds at most `120,000` records, the bound §6 costs G-EQUIV at.
- **S4** — `/root/btc-recorder-svc` is at `4216c04…`, its three recorder files are map §0's frozen rows, and it
  has no local change.
- **S5** — the primary checkout's three recorder files are the frozen rows: they are the old code G-SYNTH, G-EQUIV
  and G-REC run.
- **S6** — the branch's `recorder.py` is `0f6c9045…` and its `config.py` and `manifest.py` the frozen rows.
- **S7** — both interpreters are executable.

It prints each unit's control-group memory — `memory.current`, `memory.peak`, the swap files and nine
`memory.stat` keys — and `/proc/meminfo`, recorded: **the old code's footprint after its days of running, the
first half of TZ-22's measurement.** It writes `state.json` with the branch head and both units' MainPID and
`NRestarts`.

### 3.3 The self-test, G-SYNTH and G-EQUIV — before anything is deployed

```
cd /root/tz21-work/wt/research/recorder && TMPDIR=/root/tz21-work/scratch nice -n 19 /root/tz04a-env/venv/bin/python -B selftest.py
I synth
I equiv
```

The recorder's self-test must print `115 of 115 checks passed` against the new `recorder.py`; its temporary trees
land under `scratch/` and are removed by the test itself. `I synth` must print `G-SYNTH PASS` and `I equiv`
`G-EQUIV PASS`. **A red self-test, a G-SYNTH FAIL or a G-EQUIV FAIL stops the run here**: nothing is moved, the
running recorder is the old code, and the run goes to §3.8 and §9. An exit whose message begins `G-EQUIV BLOCKED`
or `BLOCKED` is BLOCKED, not FAIL, and stops the run the same way.

### 3.4 B-MOVE, then G-PATH — CANON hard rule 14's proof before the restart

**B-MOVE:**

```
git -C /root/btc-recorder-svc checkout --detach "$(git -C /root/tz21-work/wt rev-parse HEAD)"; echo "exit=$?"
git -C /root/btc-recorder-svc rev-parse HEAD
sha256sum /root/btc-recorder-svc/research/recorder/recorder.py /root/btc-recorder-svc/research/recorder/config.py /root/btc-recorder-svc/research/recorder/manifest.py
git -C /root/btc-recorder-svc status --porcelain --ignored | wc -l
du -sb /root/btc-recorder-svc
```

`HEAD` must be `state.json`'s branch head; the three hashes `0f6c9045…`, `8111dfe4…` and `79c99010…`; the count
`0`. Anything else runs K-21a. Then:

```
I path
```

- **P0** — `/root/btc-recorder-svc` is at the branch head; `recorder.py`, `config.py` and `manifest.py` load from
  `/root/btc-recorder-svc/research/recorder` with their hashes asserted; `git_sha()` names the branch head.
- **P1** — the market document of the five-minute interval open for at least 30 s, through `recorder.fetch`,
  served, parsed, carrying two token ids.
- **P2** — the first token's book through `recorder.fetch_status`, Tier C's function: `200` and a JSON body.
- **P3** — both SNTP servers through `recorder.sntp_best`; at least one accepted reply.
- **P4** — RTDS exactly as `rtds()` subscribes — `config.TIER_A`'s message, `config.RTDS_URL`, the same connect
  arguments (new lines 574–582) — and `crypto_prices_twap_sixty` and `crypto_prices_chainlink`, the two streams
  `complete` depends on, within 30 s. The other two topics are printed.

**Every header is fixed:** the recorder sends `User-Agent: btc-5m-twap-recorder/TZ-04a` (`config.py` line 43),
beside urllib's own `Accept-Encoding: identity`, `Host` and `Connection: close`; RTDS receives the `websockets`
library's opening handshake, as the recorder has sent since 2026-09-10. **G-PATH is read once more 300 s after
a first failure, and FAILs only if both runs fail:** one unanswered request is the venue's, not the code's, and
the code that serves these requests is unchanged by this TZ.

### 3.5 B-KILL-REC, then G-RESTART

Only after G-PATH reads PASS. **B-KILL-REC**, one command, which waits at most `320` s:

```
while :; do s=$(( $(date +%s) % 300 )); [ "$s" -ge 112 ] && [ "$s" -le 118 ] && break; sleep 1; done
I mark kill-rec
while :; do s=$(( $(date +%s) % 300 )); [ "$s" -ge 122 ] && [ "$s" -le 128 ] && break; sleep 0.2; done
date -u +%s.%N; echo "now%300=$s"
systemctl kill --signal=SIGTERM btc-recorder.service; echo "exit=$?"
```

The signal goes after the interval's `tau = 180` read at `T0 + 120` and inside that interval's window alone — the
one before closed at `T0 + 30` and the next opens at `T0 + 210` — so one interval loses `complete`, and its Tier C
reads from `tau = 120` on are taken by the new process (`config.quote_checkpoints_ahead`, `config.py` lines
96–104). If the classifier refuses the command, the Executor confirms that `state.json` holds no `kill-rec` mark,
runs `I mark kill-rec` alone, and hands the Boss the last three lines.

At least 30 s after the signal, `I restart` — **G-RESTART**.

### 3.6 G-REC

`I rec` until it prints PASS or FAIL, at most 600 s apart; exit `3` is NOT YET and names the instant to run it
again. The fifth interval's manifest lands about 40 min after the restart, and never later than its `T0 + 3,900`.

### 3.7 G-FINAL and G-CB-STILL

`I final`, at least 600 s after G-REC's PASS, so the new process's memory is read after a further two intervals.

### 3.8 The closing reads

§0.2's block again, then:

```
systemctl show btc-recorder.service btc-chainbook.service -p MainPID -p NRestarts -p MemoryCurrent -p MemoryPeak -p MemoryMax
grep -E '^(anon|file|kernel|sock|shmem) ' /sys/fs/cgroup/system.slice/btc-recorder.service/memory.stat
journalctl -u btc-recorder.service --since "@$(( $(python3 -c 'import json; print(json.load(open("/root/tz21-work/state.json"))["state_ns"] // 10**9)') - 5 ))" --no-pager -o short-iso
tail -n 40 /var/lib/btc-recorder/recorder.log
cat /root/tz21-work/state.json
free -b
du -sb /root/tz21-work /root/btc-recorder-svc /root/.claude
```

The journal holds systemd's own lines for the recorder since `I state`: the `SIGTERM`, the deactivation and its
memory peak, the scheduled restart and the start. **The report sets each unit's memory at `I state`, after the
restart and at `I final` side by side: that table is what TZ-22 sizes the ceilings from.**

---

## 4. The gates — fixed here, before any of their data exists

| gate | population | PASS | false failure | power, against |
|---|---|---|---|---|
| **G-SYNTH** | §4.1's four synthetic histories and two controls | every slice compared byte-identical, at least `600` from memory and `60` from disk; both controls detected; at most `2,000` records held after any load or prune | `0` — a deterministic comparison of bytes | `1`, any byte of any compared slice that differs |
| **G-EQUIV** | §4.2's windows over a snapshot of `runtime.jsonl` | every window byte-identical, at least `12` from memory and `200` from disk; the old load's count and digest equal the parse's; at most `2,000` records held; the snapshot the file's first bytes | `0` | `1`, the same |
| **G-PATH** | P0 to P4 | every assert, at one of two runs 300 s apart | the venue's unavailability over two runs, not measured | `1`, a path the new code cannot serve |
| **G-RESTART** | the recorder's records since the `kill-rec` mark | §4.3 | `0` — systemd and `/proc` read directly | `1`, a restart that does not happen, runs other code, or leaves its gap unrecorded |
| **G-REC** | the first `5` intervals `T0 ≡ 0 (mod 300)` with `T0 − 90 >= start + 60`, `start` the new `start` record; and every interval the new process closed before them | §4.4 | at most `0.0102` | `1`, a slice that differs; `0.5`, `complete` failing 1 in 2 |
| **G-FINAL** | the recorder at `I final` | §4.5 | `0` | `1`, a crash or a restart after G-RESTART |
| **G-CB-STILL** | the chain book from `I state` to `I final` | §4.6 | `0` | `1`, any restart of the chain book in the session |

**Family-wise false failure at most `0.0102`**, G-REC's: every other gate compares bytes, hashes or what systemd
and `/proc` state, and has no chance term.

### 4.1 G-SYNTH

The old code is the primary checkout's `recorder.py`, `9fd1c7de…`; the new is the branch's. Each runs as its own
`Recorder` over its own copy of one `runtime.jsonl`, both fed the same records through their own `record`, and
each window is sliced by both through their own `write_runtime_slice`; the new one prunes after each slice, as
`close_interval` does. **The histories**, from `random.Random(21)` and a fixed epoch, so a re-run prints the same
counts: (1) three days on disk, then two days of one process, windows closed late and out of order at six
delays from `333` to `3,633` s after their open, and a window a day old sliced at every tenth close; (2) an
outage of `158,581` s — TZ-20's measured gap — then a restart that recovers three windows from before it and
runs three hours; (3) a line torn mid-record, the next start written onto it, and the windows on both sides;
(4) ten days of one process. **Two negative controls:** a `clock` removed from the new process's memory on the
memory path, and from the file on the disk path, must each make the comparison fail. The Architect's run
printed `913` slices equal, `836` from memory and `77` from disk, at most `242` records held against the old
copy's `28,673`; the gate is the inequality, and the count is recorded.

### 4.2 G-EQUIV

`runtime.jsonl` is copied to `scratch/` in one pass, its bytes and SHA-256 printed. **The new recorder** loads the
copy through its own `load_runtime` at the copy's instant. **The old recorder's own `load_runtime`** runs into a
sink that keeps a count and a digest of what it appends instead of the list, and one parse of the copy must give
the same two — so the old code's list is known exactly without being held. **The windows**, all ending before
the copy: every 25th of the span from the first `start` record, every window served from memory, the first and
the last window each `disconnect` overlaps, and every window within 600 s of a `start`. **The old slices** read
only the records those windows can select — every `start`, every `clock` inside a chosen window, every
`disconnect` overlapping one, in file order — from which the old code's own filter picks exactly what it picks
from the whole list. Each window is sliced by both and compared byte for byte. **Then the first bytes of the
live file must hash to the copy's SHA-256** — the capture appends and never rewrites — and the copy is removed;
anyone re-derives it with `head -c <bytes> /var/lib/btc-recorder/runtime.jsonl`. After the tenth window read
from disk the run projects its own time, and a projection above `3,000` s is `G-EQUIV BLOCKED` (§6).

### 4.3 G-RESTART

Since the `kill-rec` mark: exactly one `start` record, its sha the branch head; exactly one `disconnect` with
reason `startup` detected since the mark, whose start is no earlier than 5 s before the mark and no later than
the `start` record, which is no later than its detection, which is no later than its end — **the gap, recorded
and not filled — lasting at most 60 s**; no `halt`; `NRestarts` one above the mark's; a MainPID other than the
mark's, the only process with an argument ending in `recorder.py`; and TZ-20 §4.1's unit checks at TZ-20's
`MemoryMax`. The chain book's MainPID and `NRestarts` are printed; G-CB-STILL judges them. **One reading of FAIL
would not be this TZ's code:** if the new process's first RTDS connection fails, the recorder — at both commits —
writes its gap as a `reconnect` from the failure instead of a `startup` gap from the last frame (branch lines
603–609, lines 560–566 at `4216c04`). Neither of TZ-20's two restarts met it; K-21 then restores code with the same
defect, which map §7 item 90 carries for the next TZ that changes the recorder.

### 4.4 G-REC

**The five members:** the first five `T0 ≡ 0 (mod 300)` with `T0 − 90` at least 60 s after the new `start`
record — TZ-20's rule — each `manifest.json` present by `T0 + 3,900`, `quotes_complete` true at 5 of 5,
`recorder_git_sha` the branch head at 5 of 5, and `complete` true at **at least 3 of 5**. **The earlier
intervals:** every `T0` from `3,900` s before the new start up to the first member, whose `manifest.json` was
written at or after that start — the windows recovered at the start and the one open across the restart. **The slice
differential, over both:** each stored `runtime.jsonl` must equal byte for byte the old code's slice of that
window, computed by the primary checkout's `write_runtime_slice` over the records `runtime.jsonl` held when the
stored slice was written — every record whose own stamp is at or before the stored file's modification time.

**False failure:** `complete` fails binomially at `207 / 2,608` — TZ-16a's span, every non-member of it but one
on `disconnect` (map §2.3) — so 3 or more of 5 fail with probability `0.00442`; `quotes_complete` failed at 0 of
TZ-16a's 2,608, at most `3 / 2,608` a unit at 95%, so any of 5 fails with probability at most `0.00574`. **The
slice differential's own false failure** is a reconnect ending within one kernel tick, at most 4 ms, before a
slice is written, while overlapping its window — at the measured one reconnect in `7,200` s and about seven
slices, below `1e-5` [modelled]. In all at most `0.0102`. The five close within `2,000` s of the start, before
RTDS first closes the socket at `7,200` s (map §6), so the base rate overstates. **Power:** `1` against a slice
that differs, since every slice the new process wrote in the span is compared; `0.5` against `complete` failing
1 in 2.

### 4.5 G-FINAL

At `I final`: the unit's checks at TZ-20's `MemoryMax`, `NRestarts` and MainPID those G-RESTART read, the only
process with an argument ending in `recorder.py`; `/root/btc-recorder-svc` at the branch head with its three
files at `0f6c9045…`, `8111dfe4…` and `79c99010…`; and the newest `start` record G-RESTART's. Each unit's memory
and `/proc/meminfo` are printed.

### 4.6 G-CB-STILL

From `I state` to `I final` the chain book keeps its MainPID and its `NRestarts`, remains the only process with
an argument ending in `tz18a-chainbook-capture.py`, and passes TZ-20 §4.1's unit checks. **This TZ changes nothing
of the chain book**, so a FAIL here runs no block: its unit restarts it under `Restart=always`, and the report
carries the reading for the next TZ.

### 4.7 The stops — CANON hard rule 14

**K-21a — on a G-PATH FAIL, or a B-MOVE whose reads are wrong.** The running process is still the old code, so
the tree goes back and nothing is signalled:

```
git -C /root/btc-recorder-svc checkout --detach 4216c04673ced76b5b2ac60ef57c9abedc46f9b9; echo "exit=$?"
git -C /root/btc-recorder-svc rev-parse HEAD
sha256sum /root/btc-recorder-svc/research/recorder/recorder.py /root/btc-recorder-svc/research/recorder/config.py /root/btc-recorder-svc/research/recorder/manifest.py
git -C /root/btc-recorder-svc status --porcelain --ignored | wc -l
systemctl show btc-recorder.service -p MainPID -p NRestarts
```

`HEAD` `4216c04…`, the three frozen hashes, `0` lines, and MainPID and `NRestarts` those `state.json` holds: the old
process never stopped. If MainPID or `NRestarts` moved, the unit restarted onto the new code in between, and
K-21 follows.

**K-21 — on a FAIL of G-RESTART, G-REC or G-FINAL.** The tree goes back and the unit restarts onto it:

```
git -C /root/btc-recorder-svc checkout --detach 4216c04673ced76b5b2ac60ef57c9abedc46f9b9; echo "exit=$?"
I mark revert
systemctl reset-failed btc-recorder.service; systemctl restart btc-recorder.service; echo "exit=$?"
```

At least 30 s later, `I revert` must print `REVERT PASS`: the tree at `4216c04…` with its three frozen hashes and no
change; since the `revert` mark exactly one `start` on `4216c04…`; no `halt`; a MainPID other than the mark's, the
only recorder process; and the unit's checks. **`NRestarts` and the startup gaps are recorded, not asserted:** an
explicit restart is not one of systemd's own, and a revert must not stop the capture on the venue's socket.

**K-20R — if `I revert` fails:**

```
systemctl disable --now btc-recorder.service; echo "exit=$?"
```

**Verification is the Executor's,** at least 30 s after the block: `systemctl is-active btc-recorder.service`
prints `inactive` or `failed`; `systemctl is-enabled btc-recorder.service` prints `disabled`; the recorder's
`pgrep -fx` prints no line and `exit=1`. The recorder writes no `stop` record, and its absence is expected.
**Under PASS no block of this section is ever run. A FAIL before B-MOVE needs none.** After any of them the run goes
to §3.8 and §9.

### 4.8 What a PASS establishes, and what it does not

The recorder runs `0f6c9045…` as a system unit, holds about two hours of runtime records instead of every record
since 2026-09-10, and writes slices byte-identical to the old code's — on synthetic histories, on the capture's
own file, and live. **Not exercised in production:** a slice read from disk, which only a recovery after an outage
of more than two hours takes — G-SYNTH, G-EQUIV and the Architect's side-by-side run exercise it (§10) — and the
process's memory over days, which TZ-22's host gate reads before it sets a ceiling.

---

## 5. The instrument

`research/tz21-recorder-memory.py`, Appendix A.2, fixed by the Architect as this TZ's Validation and written byte
for byte. Standard library and the recorder's own modules, run under the recorder's interpreter. One mode per
run; each prints its findings with UTC stamps and ends with its PASS line and its own peak memory. **An audit hook
refuses any open under either capture root but the files §2 item 2 names, and any open there for writing**, and
every mode prints its count of such opens, a NOT YET included. It writes nothing but under `/root/tz21-work/`
and, in `reclaim`, new files in `/root/btc-forensics/`; the one file it removes is G-EQUIV's own copy, once that
gate has passed. Exit `0` is a PASS; exit `1` a failed assert, named, or a BLOCK whose message says so; exit `3`
NOT YET. Run with `-O` it refuses to start, because every check is an assert.

---

## 6. Cost

**Compute,** measured in the Architect's run on two cores under Python 3.12.3, and bounded for a host three times
slower:

| check | population at its upper bound | measured | bound |
|---|---|---|---|
| G-SYNTH | fixed: four histories, `913` slices | `9` s | `30` s |
| G-EQUIV | the windows at S3's bound of `120,000` records — about `1,600`, about `1,580` of them from disk, each reading the whole copy once [modelled] | `211.8` s for `849` windows, `826` from disk, over `66,502` records | about `730` s at the bound, `2,190` on a host three times slower; **the run projects itself after its tenth window from disk and stops BLOCKED above `3,000` s** |
| G-REC | one pass over `runtime.jsonl` a run, at most `11` runs | under `1` s a run | `11` s |
| `state`, `restart`, `final`, `revert` | one pass each | under `1` s | `4` s |
| `reclaim` | this TZ's tree but its worktree, and the earlier scratch directories | under `1` s | `3` s |
| the self-test | `115` checks | `2` s | `6` s |

**At most `2,244` s of compute in all**, the bounds summed, under `3,600`, every second of it at `nice 19`. The
fail-fast bound is G-EQUIV's: `3,000` s, above its own bound at the host factor of three, `2,190`, with room.

**Wall clock:** B-KILL-REC waits at most `320` s; G-REC's fifth interval opens no later than `start + 1,650` s and
its manifest lands about `650` s after that, at worst `start + 5,550`; `I final` follows by `600` s. **About two
hours from §0 to §9, at most `9,000` s.**

---

## 7. Validation

| # | check | count |
|---|---|---|
| **V1** | §0.1's fingerprint | 6 anchors, 4 re-derived, 28 of 28 `frozen` equal |
| **V2** | §0.2's host gate | H1 to H9, the memory and the disk gate, each read named |
| **V3** | `I state` | S1 to S7 |
| **V4** | §3.1's two files | 2 of 2 hashes, lines and bytes equal; the frozen hash asserted before the replacement; the branch's diff against `origin/main` names exactly these two paths, `M` and `A`, the first with `49` insertions and `6` deletions |
| **V5** | the self-test | `115 of 115` |
| **V6** | G-SYNTH | slices equal, from memory and from disk, against `600` and `60`; records held, against `2,000`; 2 of 2 controls |
| **V7** | G-EQUIV | windows equal, from memory and from disk, against `12` and `200`; the count and digest equality; records held; the prefix's hash |
| **V8** | B-MOVE | `HEAD` equal; 3 of 3 hashes; `0` status lines |
| **V9** | G-PATH | P0 to P4; 2 HTTP requests, SNTP at least 1 of 2, RTDS at least 2 of 4 topics |
| **V10** | G-RESTART | 1 start, 1 gap of at most 60 s, `NRestarts` one up, a new pid |
| **V11** | G-REC | 5 members and their four counts; every slice compared equal, the count of earlier intervals and of members |
| **V12** | opens under the capture roots | every mode's printed count, a NOT YET's included; any refusal is a failed run |
| **V13** | G-FINAL | the unit, its pid and `NRestarts`, its tree, its newest `start` |
| **V14** | G-CB-STILL | pid and `NRestarts` unchanged |
| **V15** | contract §4.2's self-check | run after the push and the pull request and before the report's commit |
| **V16** | §3.8's closing reads | every read printed |
| **V17** | §9's `reclaim` runs | files considered, named by a report, kept by name, copied and already held, each counted; the worktree skipped by name; the store's count after equal to before plus the copies |
| **V18** | §9's removals | `git worktree remove` without `--force` exit `0`; `test -e` exit `1` for `/root/tz21-work` and each scratch directory removed; `git worktree list` naming the primary checkout and `/root/btc-recorder-svc` and nothing else |
| **V19** | memory | each unit's `memory.current`, `memory.peak` and `memory.stat` at `I state`, `I restart` and `I final`, and `MemAvailable` at each, in one table |

---

## 8. The report

`CryptoReports/TZ-21-recorder-memory-report.md`, in contract §8's order. Beyond what V1 to V19 print: every instant
of `state.json`; every block the classifier refused, who ran it and when; each gate's reading with its deciding
numbers; **the gap**: the start and end of the `startup` record G-RESTART read, in `recv_ns` and UTC; the
recorder's journal lines; **the memory table of V19**, the old code beside the new; the commit and the pull
request; §9's counts and removals; and §0.3's free-space reads with their instants and bound. A FAIL names the
gate, the block run and its verification. **The report is drafted in the primary checkout `/root/btc-5m-twap`
before B-RECLAIM-OWN and committed after it**, so the removal of this TZ's own tree is in it.

---

## 9. Reclaim — the host left clean (CANON hard rule 15)

**What a file is kept for:** a committed report prints its SHA-256, whole or as a prefix of 16 to 64 hex
characters, or it is named below. `reclaim` copies each such file into `/root/btc-forensics/` as
`<tree>--<path with / as -->`, by exclusive create, and verifies its hash; a name already there with the same hash
is counted as held, and with another hash is a failed assert. **Kept by name:** `/root/tz21-work/state.json` and
every file under `/root/tz21-work/logs/`. **The branch worktree is not copied:** `reclaim` first asserts that
`git status --porcelain --ignored` in it prints nothing and that its `HEAD` is its upstream's, so every byte of it
is in git at a pushed commit — and `git worktree remove` then needs no `--force`. Everything else in a reclaimed
tree is scratch no report cites, and goes.

**B-RECLAIM-SCRATCH**, after §3.2 and before §3.3, for each directory §0.2's listing shows beside this session's
own whose name is a UUID — earlier sessions' scratch, under the `btc-5m-twap` project's directory of `/tmp` —
first all of them in one run, then one removal per directory:

```
I reclaim <each such directory>
rm -rf <one such directory>; echo "exit=$?"
test -e <that directory>; echo "exit=$?"
```

`reclaim` refuses any path that is not such a directory, and must print `RECLAIM PASS` before any removal. **This
session's own directory is never named.** If the listing shows none, the block is recorded as empty and skipped.

**B-RECLAIM-OWN**, last, after §3.8 and with the report drafted. **Its output is written to no file**: the Executor
quotes it from the session, because a log growing inside the tree `reclaim` copies would fail its own whole-copy
assert, and one outside it would be left behind:

```
I reclaim /root/tz21-work
git -C /root/btc-5m-twap worktree remove /root/tz21-work/wt; echo "exit=$?"
rm -rf /root/tz21-work; echo "exit=$?"
test -e /root/tz21-work; echo "exit=$?"
git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
find /root/btc-forensics -type f | wc -l
df -B1 --output=source,size,avail /var/lib/btc-recorder
```

If `reclaim` refuses the worktree because it holds an untracked `__pycache__`, the Executor deletes that directory
— no report names it, and it is regenerated by any import — and runs `reclaim` again; anything else it lists stops
§9 there, and the report names it for the next TZ. The branch `tz-21-recorder-memory` stays, on `origin` and as a
local ref; only its working tree goes. **Kept:** `/root/btc-recorder-svc` and `/root/tz18a-svc` are the two units'
code — no TZ removes either while its unit is enabled — and the capture and the forensic store are data, never
scratch (map §6, TZ-09 §5). **A refused `rm -rf` is handed to the Boss** by §3's route, one tree per command, and
verified by `test -e`.

---

## 10. Pre-send checks

Performed on 2026-10-04 against this file, in a reading separate from its writing, with `origin/main` at
`c7a45ff2d8a6e78b36215107e0c055eb296e5d8b` read directly, and against `SYSTEM-MAP.md` revision `2026-10-04-b`,
the file uploaded with this TZ. Line numbers are `origin/main`'s, except where they are said to be the branch's —
Appendix A.1's.

### C1 — scope against body

| named in the body | how | intersects, by path or by content class | resolution |
|---|---|---|---|
| `research/recorder/recorder.py` | replaced, branch | P1 by path; map §0's `frozen` rule | P1's own exemption, named in it |
| `research/tz21-recorder-memory.py` | written, branch | — | a new file |
| `CryptoReports/TZ-21-recorder-memory-report.md` | written, `main` | P5 | P5's own exemption |
| this TZ, `SYSTEM-MAP.md`, the 31 table paths | read, hashed | — | — |
| the primary checkout's `recorder.py`, `config.py`, `manifest.py` | hashed; imported by `synth`, `equiv`, `rec` | P1 by path | read and executed, never modified |
| `/root/btc-recorder-svc` and its three recorder files | checkout moved by B-MOVE, back by K-21a or K-21; hashed; imported by `path` | — | §2's host paths name both moves and nothing else of it |
| `/var/lib/btc-recorder/runtime.jsonl` | read; copied to `scratch/` by `equiv`, the copy removed | P2 by path; P6 by class: clock offsets, times, disconnects | P2's own text; no price in a runtime record |
| G-REC's `manifest.json` and `runtime.jsonl`; the manifests of the 3,900 s before the restart | read; stat'ed | P2 by path; P6 by class: counts, times, flags, shas | P2's own text; a manifest carries no price and no outcome (`manifest.py` lines 217–233) |
| `recorder.log` | `tail -n 40` | P2 by path | P2's exemption (b) |
| `/var/lib/btc-recorder/**` | written by the unit | P3 | P3 names "this TZ's commands"; §2's host paths name the unit's writes |
| the live document, book, SNTP and RTDS frames of G-PATH | requested, parsed | P6 by class: prices, outcomes | P6's text: status, bytes, parse, token ids, offsets, frame count and topics |
| `/etc/systemd/system/btc-*.service` | `cmp` | P9 | read only |
| B-KILL-REC, K-21a, K-21, K-20R | signal, restart, stop | P8, P9 | P8's and P9's own text |
| `btc-chainbook.service`, `telemetry-watch.service` | `systemctl` reads, `show` | P9 | read only |
| `/root/tz21-work/**`, `/root/btc-5m-twap/.git` | written | — | §2's host paths; one `git worktree add` |
| `/root/tz16a-work`, `/root/tz19-work`, `/root/tz20-work`, `/root/tz18a-svc`, `/root/btc-forensics`, `/root/PROJECT_GAMING_PS5`, `/root/.claude` | `test -e`, `find`, `du` | P4 | reads only |
| the earlier sessions' scratch directories under `/tmp` | hashed, named files copied, then removed | §2's removal list; P6 by class: unknown content | named in the removal list; P6's §9 exemption, whole files, no value extracted |
| `/proc/**`, `/sys/fs/cgroup/system.slice/*/memory.*` | read | — | reads |
| `/root/btc-5m-twap/CryptoReports/*.md` | read by `reclaim` for hex tokens | P6 by class: reports print prices and outcomes | P6's §9 exemption, hex runs alone |
| `/root/btc-forensics/` | exclusive create; counted | P4 | P4's exemption |
| the report | output | P6 by class | instants, pids, counts, statuses, hashes, token ids, memory figures; no price, outcome or label |

**21 entries. 16 intersections, each closed by a prohibition's own text, a named exemption or §2's lists** — the
frozen recorder, the report's path, the old code read, the runtime file and its copy, G-REC's files, the log, the
unit's writes, the live bodies, the installed units, the signals and restarts, the two units read, the trees and
directories only read, the scratch directories removed, the reports' tokens, the store, and the report's content.
None open.

### C2 — origin of every expectation

| class | the fixed expectations of §3, §4 and §7 |
|---|---|
| computed by an implementation independent of the one under test, exact | the two Appendix A hashes, lines and bytes — `sha256sum` and `wc` on the files this session wrote, and the extraction script run against this file; `49` and `6` — `git diff --numstat`; `0.00442`, `0.00574`, `0.0102` and the power `0.5` — binomial sums in `Fraction`; `110,000,000` ≥ `2 × 54,984,704` = `109,969,408`; `2,300,000,000` = `2,200,000,000 + 100,000,000`; `4,204,105` = `⌊33,632,842 × 3 / 24⌋`; `3,720` = `3,630 + 90`; the window rules — `T0 − 90 >= start + 60`, `T0 + 3,900`, `3,900` s back, `now % 300` in `[112, 118]` and `[122, 128]` — integer arithmetic |
| quoted from a committed artifact, named | `4216c04673ced76b5b2ac60ef57c9abedc46f9b9`, `9fd1c7de…`, `8111dfe4…`, `79c99010…` — map §0 and §6; `536870912` and `201326592` — TZ-20 §4.1; `1,438` — TZ-20 report §2.17; `1791102470` — TZ-20 report §2.12, `I final` at 08:27:50 UTC; `207 / 2,608` — map §2.3; `3 / 2,608` — TZ-20 §4.4; `/dev/vda2`, `31612203008`, `33,632,842` — map §6; `2,200,000,000` — `tz18a-chainbook-capture.py` line 79; `2,000,000,000` — `config.py` line 21; `1,002,127,360`, `271,712,256`, `91,164,672` — TZ-20 report §2.14; `158,581` — TZ-20 report §2.13, `158,580.698` s; `60,786` — TZ-20 report §2.12; `608,103` — TZ-20 report §2.4; `115` — map §3 and `selftest.py` line 573; `c7a45ff…` and 25 ref lines — map §1 |
| depending on a quantity this TZ measures | **none.** G-REC's slice differential is an equality between two computations over the same records; every count a gate reads is held to a fixed threshold, and the Architect's own counts — G-SYNTH's `913`, the peaks, the timings — are recorded beside the gates and judged by none |

The gates' thresholds — `600` and `60`, `12` and `200`, `2,000` records, `60` s, `5` s, 3 of 5, `3,000` s and
`120,000` records — are fixed choices, each stated with its reason in §4 and §6, and none is a value this TZ
measures. The measurements that size this TZ — `68,251,648` bytes for `60,786` records, the peaks `54,984,704` and
`40,513,536`, `211.8` s, `108,130,304` and `33,247,232` bytes — are the Architect's, in this session, under the host's
interpreter; they set floors and budgets, never an expectation.

### C3 — shape of every diff

`research/recorder/recorder.py` replaces **six** committed lines, read from `origin/main`:

| line | committed text |
|---|---|
| 228 | `        self.runtime = []            # every runtime record, including earlier processes'` |
| 233 | `    def load_runtime(self):` |
| 234 | `        """Earlier processes' records, so a slice spanning a restart is still whole."""` |
| 240 | `                    self.runtime.append(json.loads(line))` |
| 242 | `                    pass` |
| 488 | `        for rec in self.runtime:` |

`research/tz21-recorder-memory.py` is new: none. Nowhere does this TZ call the first diff additive, and V4
asserts its shape: `M` with `49` insertions and `6` deletions, and `A`.

### C4 — cost of every check

§6's table is this check's figure, each row at its population's upper bound: G-SYNTH fixed; G-EQUIV at S3's
bound of `120,000` records, which `state` asserts; G-REC at most `11` runs, one per 600 s from the restart to the
fifth member's deadline at `start + 5,550` s; the rest one pass each. **G-EQUIV's bound, term by term:** `211.8` s
over `826` windows from disk and `66,502` records is `3.856` µs a record a window; at the bound about `1,580`
windows from disk times `120,000` records times `3.856` µs is about `731` s, `2,193` on a host three times slower
[modelled]; the windows from memory are a few milliseconds each. The fail-fast bound, `3,000` s, sits above that
and below `3,600`, and the run tests itself against it after its tenth window from disk, about `2.6` s into the
loop at today's size. **The sum, `2,244` s, is under `3,600`.**

### C5 — every count

V1: 6 anchors, 4 re-derivable — `A2`, `A4`, `A5`, `A6` — and 28 `frozen` of the map's 31 rows, counted in revision
`2026-10-04-b`'s table: TZ-20's 25, the two unit files and `tz20-capture-under-systemd.py`. V3: S1 to S7, seven,
`mode_state`'s seven labelled groups. V4: 2, Appendix A's two blocks. V8: 3 hashes, B-MOVE's `sha256sum` line.
V9: P0 to P4, five; HTTP `2`, P1 and P2; SNTP over `config.NTP_SERVERS`, 2; RTDS over `config.TIER_A`, 4 topics.
V10: 1 start, 1 gap. V11: 5 members, four counts each — manifest present, `quotes_complete`, sha, `complete`; the
earlier intervals counted by the run. V18: 1 worktree removed, `/root/tz21-work/wt`, of the 3 registered once §3.1
has added one to the 2 H9 reads, leaving 2. V19: 3 instants, 2 units.

### C6 — every population

G-SYNTH: §4.1's four histories and two controls, every window each closes or recovers. G-EQUIV: the windows
§4.2 chooses over the snapshot, every one ending before it. G-PATH: one request per endpoint. G-RESTART: the
recorder's `runtime.jsonl` records since the `kill-rec` mark. G-REC: the five members and the earlier intervals of
§4.4, with the records `runtime.jsonl` held when each stored slice was written. G-FINAL: the recorder at `I final`.
G-CB-STILL: the chain book's unit at `I state` and at `I final`. The false-failure rate: Bernoulli over G-REC's 5
members, at the base rates of TZ-16a's 2,608 units considered. V12: every open under the two capture roots in each
run. S3: the runtime file whole. `reclaim`: every regular file under the trees it is given, the branch worktree
excepted by name, against the hex runs of every report in `CryptoReports/`.

### C7 — every signature and every behaviour

Read at `c7a45ff`.

- `recorder.py:233` `def load_runtime(self):` — "reads every line into `self.runtime`": 235–242,
  `if not os.path.exists(self.runtime_path):` … `self.runtime.append(json.loads(line))` … `except ValueError:`
  `pass`.
- `recorder.py:244` `def record(self, rec):` — "appends … before it writes it to the file": 245
  `self.runtime.append(rec)`, 246–247 the `"at"` open and the write of `json.dumps(rec, sort_keys=True) + "\n"`.
- `recorder.py:511` `async def clock_sampler(self):` — "two `clock` records a minute": 513
  `for host in config.NTP_SERVERS:`, 520 `self.record({"kind": "clock", "recv_ns": time.time_ns(), …`, 526
  `await asyncio.sleep(config.NTP_SAMPLE_S)`; `config.py` 73 `NTP_SERVERS = ["108.61.73.243", "pool.ntp.org"]`,
  74 `NTP_SAMPLE_S = 60`.
- `recorder.py:473` `def write_runtime_slice(self, t0, path):` — "the list is read in one place" and the slice's
  definition: 479–480 `lo`, `hi`; 481–484 `starts` and `active` from `self.runtime`; 486–487 the fallback line;
  488–494 the `disconnect` and `clock` conditions; 495–497 the write. `self.runtime` occurs at lines 228, 240, 245,
  481 and 488 and nowhere else.
- `recorder.py:331` `async def close_interval(self, t0, path):` — 337 `await self.fetch_s7(t0, path)`, 338 the
  slice, 339 `doc = manifest.write(path)`, 340–342 the `closed` log line.
- `recorder.py:392` `async def fetch_s7(self, t0, path):` — "a live window is sliced by about `T0 + 3,630`": 396
  `deadline = t0 + S7_DEADLINE_S`, 397 `while time.time() < deadline:`, 399 the fetch, 409
  `await asyncio.sleep(S7_POLL_S)`; 33–34 `S7_DEADLINE_S = 3600`, `S7_POLL_S = 15`; `fetch`'s timeout `15` (196).
  The branch's lines are 437, 438, 440 and 450.
- `recorder.py:576` `async def main(self):` — 578 `self.load_runtime()`, 582–583 the `start` record, 586–588 the
  floors, 589 `await self.recover()`; and the imports of lines 19–33, with `import urllib.request` and
  `urllib.error` inside `fetch` and `fetch_status` (197, 209–210) — "nothing it runs opens a file of its tree": every
  `open` in the file (lines 191, 237, 246, 286, 385, 404, 422, 465, 495), and `last_frame_ns`'s `opener` (163),
  names a path under `config.ROOT` or the runtime file, and `git_sha()` (50–57) runs once, from `__init__` (226).
- `recorder.py:530` `async def rtds(self):` — 531–533 the subscription message, 535 the `startup` reason from
  `last_frame_ns(config.ROOT)`, 538–539 `websockets.connect(config.RTDS_URL, open_timeout=20, ping_interval=None,
  max_size=None)`, 542–544 the `disconnect` record; the branch's 574–582, copied by `path`.
- `recorder.py:196` `def fetch(url, timeout=15):`, `:203` `def fetch_status(url, timeout=15):`, `:123`
  `def sntp_best(host, burst=NTP_BURST):` — unchanged on the branch, at 201, 208 and 128.
- `config.py:96` `def quote_checkpoints_ahead(t0, now):` — 103–104, the checkpoints at or after `now`; 43
  `USER_AGENT`; 21 `FREE_SPACE_FLOOR_BYTES`; 17–18 `PRE_S = 90`, `POST_S = 330`.
- `manifest.py:241` `def write(dirpath):` — 242 `doc = build(dirpath)`, 245–247 the temporary file and
  `os.replace`, so the manifest's modification time is its writing's; 203–204 `quotes_complete`; 214 `complete`;
  225 `recorder_git_sha`; 217–233 the keys, none a price or an outcome.
- `selftest.py:573` `print("\n%d of %d checks passed" % (PASSED, PASSED))`.
- `tz18a-chainbook-capture.py:79` `RESOURCE_FLOOR = 2_200_000_000`.
- The branch's `recorder.py`, Appendix A.1: 239 `def load_runtime(self, now_ns=None):` with 246
  `self.runtime_from_ns = now_ns - RUNTIME_KEEP_S * 10 ** 9`; 251 `def runtime_file_records(self):`, 253–261; 263
  `def kept(self, rec):`, 268–276; 278 `def prune_runtime(self, now_ns=None):`, 281 the `max`, 282 the filter; 378
  the slice and 379 `self.prune_runtime()` in `close_interval`; 522–523 the starts from `self.runtime`; 530
  `source = self.runtime if lo >= self.runtime_from_ns else self.runtime_file_records()`.

Every sentence of the body that attributes a behaviour to one of these was checked against the lines above.

### C8 — every cross-reference

TZ-20 §4.1 (the unit checks), §4.4 (G-REC's base rates); the TZ-20 report §2.4 (`608,103`), §2.12 (`I final`,
`60,786`), §2.13 (the gap), §2.14 (memory, the host), §2.17 (`1,438`) and §6 item 2 (outputs outside the tree);
map §0, §1, §2.3, §2.5, §3, §6 and §7 items 88 and 90 of revision `2026-10-04-b`; TZ-09 §5 (the capture is never deleted);
CANON PART III hard rules 14 and 15 and PART IV, of revision `2026-10-04-a`; contract §1, §4.2 and §8; and this
TZ's §0 to §9 and Appendix A. Each was read, and each supports the sentence that cites it.

### Checks this session could not perform, and what replaces each

- **The host's own state** — both units, the trees, the runtime file, the store — is S1 to S7 and H1 to H9, and
  BLOCKS.
- **SNTP from this session:** its sandbox passes no UDP, so P3 failed here as it must; P0 to P2 passed through the
  instrument, and the RTDS path was exercised by the side-by-side run below. §3.4 runs every path on the host and
  restarts nothing on a FAIL.
- **systemd and control groups** were simulated — a stand-in `systemctl`, dummy processes under the exact argv,
  fixture cgroup files — through every mode in order, the NOT YET paths, a tampered slice that G-REC must FAIL, a
  stray file in the worktree that `reclaim` must refuse, and the revert. `SIMRUN PASS` on the final instrument,
  `d6d2dc19…`.
- **The side-by-side run** — the measurement §1 and §4.8 cite. The old and the new recorder ran as real processes
  under Python 3.12.3 and `websockets` 17.1, each capturing the live venue from this session from 12:34:01 UTC,
  each on its own copy of one `66,502`-record `runtime.jsonl` with an unfinished interval four and a half hours old
  to recover. The old process started at `105,148,416` bytes resident and ended the hour at `108,130,304`; the
  new started at `31,096,832` and ended at `33,247,232`, its peak `33,325,056`. **Every one of the `13` slices the
  new process wrote — `12` from memory and the recovered interval's from disk — equals byte for byte the old code's
  slice over the same records**, compared as G-REC compares them. SNTP was unanswered there, so its clock records
  carry null offsets; nothing else of the run differs from the host's.

---

## Appendix A — the two files, byte for byte

Extracted by §3.1's script; each block's content is the file.

### A.1 `research/recorder/recorder.py`

```python file=research/recorder/recorder.py
#!/usr/bin/env python3
"""TZ-04a Tier A recorder: continuous read-only capture of S1-S4, S6 and S7.

TZ-05a adds Tier C to the same process: seven order-book snapshots per interval per token id,
issued as plain GETs to the public CLOB endpoint and stored exactly as returned. It also
applies TZ-05a section 5 R-b, which rejects an invalid SNTP reply at the point of reception.

TZ-21 bounds what the process holds in memory: a runtime record that no slice served from
memory can read again is forgotten, and a window older than what memory holds is sliced from
runtime.jsonl on disk, record for record, so every slice is the one it always was.

Read-only by construction. There is no order path, no CLOB authentication, no wallet, key,
signer or credential anywhere in this file, and no pricing arithmetic: frames are routed by
topic and written byte-for-byte as received.

Run:  python3 recorder.py            # runs until a section 4 floor is reached
"""

import asyncio
import gzip
import json
import os
import shutil
import socket
import struct
import subprocess
import sys
import time

import websockets

import config
import manifest

GRACE_S = 3                 # let in-flight frames land before a window's files are closed
S6_FETCH_OFFSET_S = 5       # the market is live a moment after T0
S7_DEADLINE_S = 3600        # stop polling for the venue's outcome at T0 + 3600
S7_POLL_S = 15
RECV_TIMEOUT_S = 30         # no frame for this long means the socket is dead
NTP_BURST = 4               # SNTP queries per server per round; the lowest-delay reply is kept
QUOTE_TIMEOUT_S = 8         # shorter than the 20 s between the two closest Tier C checkpoints
RUNTIME_KEEP_S = 7200       # a live window is sliced by T0 + S7_DEADLINE_S plus one last poll


def log(msg):
    sys.stderr.write("%s %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    sys.stderr.flush()


def now_pair():
    """The two clocks every captured line carries."""
    return time.time_ns(), time.monotonic_ns()


def git_sha():
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        out = subprocess.run(["git", "-C", here, "rev-parse", "HEAD"],
                             capture_output=True, text=True, timeout=10)
        return out.stdout.strip() if out.returncode == 0 else "unknown"
    except Exception:
        return "unknown"


class SntpRejected(Exception):
    """An SNTP reply that TZ-05a section 5 R-b forbids turning into an offset."""

    def __init__(self, reason):
        super().__init__(reason)
        self.reason = reason


def sntp_reject_reason(fields, t3, host_now):
    """Why this reply must be rejected, or None when it may be used.

    TZ-05a section 5 R-b, in the order the TZ lists the conditions. The check is here, at
    reception, and not on the samples afterwards: a reply that fails it never becomes an
    offset and is counted as a rejection instead.
    """
    leap = (fields[0] >> 30) & 0x3
    stratum = (fields[0] >> 16) & 0xFF
    if leap == 3:
        return "leap-indicator-3"
    if stratum == 0:
        return "stratum-0"
    if stratum > 15:
        return "stratum-above-15"
    if fields[10] == 0 and fields[11] == 0:
        return "zero-transmit-timestamp"
    if abs(t3 - host_now) > config.SNTP_MAX_SKEW_S:
        return "transmit-timestamp-beyond-%ds" % config.SNTP_MAX_SKEW_S
    return None


def sntp_offset(host, timeout=5):
    """One SNTP round trip. Returns (offset_seconds, round_trip_seconds).

    Raises SntpRejected when the reply fails the R-b validation above.
    """
    pkt = b"\x1b" + 47 * b"\0"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(timeout)
    try:
        t1 = time.time()
        sock.sendto(pkt, (host, 123))
        data, _ = sock.recvfrom(48)
        t4 = time.time()
    finally:
        sock.close()
    fields = struct.unpack("!12I", data)
    t2 = fields[8] + fields[9] / 2 ** 32 - 2208988800
    t3 = fields[10] + fields[11] / 2 ** 32 - 2208988800
    reason = sntp_reject_reason(fields, t3, t4)
    if reason is not None:
        raise SntpRejected(reason)
    return ((t2 - t1) + (t3 - t4)) / 2, (t4 - t1) - (t3 - t2)


def best_sample(samples):
    """The standard NTP clock filter: of (offset, round_trip) pairs, keep the lowest delay.

    One SNTP reply is only accurate to half its round trip, so the lowest-delay reply of a
    burst is the one least contaminated by path asymmetry.
    """
    return min(samples, key=lambda s: s[1])


def sntp_best(host, burst=NTP_BURST):
    """A burst against one resolved address.

    Returns (ip, offset_s, rtt_s, accepted, rejected), where `rejected` maps each R-b reason
    to the number of replies it rejected. A burst whose every reply is rejected still returns,
    with `offset_s` and `rtt_s` None, so that the rejections are recorded rather than lost.
    """
    ip = socket.gethostbyname(host)
    samples, rejected = [], {}
    for _ in range(burst):
        try:
            samples.append(sntp_offset(ip))
        except SntpRejected as exc:
            rejected[exc.reason] = rejected.get(exc.reason, 0) + 1
        except Exception:
            pass
    if not samples:
        return ip, None, None, 0, rejected
    offset, rtt = best_sample(samples)
    return ip, offset, rtt, len(samples), rejected


def last_frame_ns(root):
    """The newest recv_ns any earlier process wrote, read back off disk; 0 when there is none.

    A restart's outage begins at the last frame actually captured, not at the moment the new
    process happens to start and not at the beginning of time.
    """
    base = os.path.join(root, config.SERIES)
    if not os.path.isdir(base):
        return 0
    newest = 0
    for name in sorted((n for n in os.listdir(base) if n.isdigit()), key=int)[-4:]:
        for stream in config.STREAM_FILES:
            for suffix in (".jsonl", ".jsonl.gz"):
                path = os.path.join(base, name, stream + suffix)
                if not os.path.exists(path):
                    continue
                opener = gzip.open if suffix.endswith(".gz") else open
                try:
                    with opener(path, "rt", encoding="utf-8") as fh:
                        for line in fh:
                            try:
                                newest = max(newest, json.loads(line)["recv_ns"])
                            except (ValueError, KeyError):
                                pass            # a line torn by the previous process's death
                except (OSError, EOFError):
                    pass
    return newest


def disk_free_bytes():
    return shutil.disk_usage(config.ROOT).free


def tree_bytes(root):
    total = 0
    for dirpath, _dirnames, filenames in os.walk(root):
        for name in filenames:
            try:
                total += os.lstat(os.path.join(dirpath, name)).st_size
            except OSError:
                pass
    return total


def gzip_file(src, dst):
    """Compress with a zeroed header so the same input always gives the same bytes."""
    with open(src, "rb") as fin, open(dst, "wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, compresslevel=9, mtime=0) as fout:
            shutil.copyfileobj(fin, fout)


def fetch(url, timeout=15):
    import urllib.request
    req = urllib.request.Request(url, headers={"User-Agent": config.USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def fetch_status(url, timeout=15):
    """One GET. Returns (http_status, body_text).

    TZ-05a section 3 stores a non-200 reply as received, with its status, so a 4xx or 5xx is
    a result here and not an exception. Only a read that produced no reply at all raises.
    """
    import urllib.error
    import urllib.request
    req = urllib.request.Request(url, headers={"User-Agent": config.USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as err:
        return err.code, err.read().decode("utf-8", "replace")


class Recorder:
    def __init__(self):
        self.writers = {}            # (t0, stream) -> file handle
        self.live = set()            # intervals with a lifecycle task running
        self.done = set()            # intervals already closed; never reopened
        self.stopping = False
        self.stop_reason = None
        self.sha = git_sha()
        self.runtime_path = os.path.join(config.ROOT, "runtime.jsonl")
        self.runtime = []            # the runtime records a slice served from memory can read
        self.runtime_from_ns = 0     # older clock samples and disconnects are on disk only
        self.last_rx_ns = 0          # the last moment anything arrived on the socket

    # ---- runtime log -------------------------------------------------------------

    def load_runtime(self, now_ns=None):
        """Earlier processes' records that memory must hold, read off disk once.

        The file keeps every record. A window older than runtime_from_ns is sliced from the
        file itself (write_runtime_slice), so a slice spanning a restart is still whole.
        """
        now_ns = time.time_ns() if now_ns is None else now_ns
        self.runtime_from_ns = now_ns - RUNTIME_KEEP_S * 10 ** 9
        for rec in self.runtime_file_records():
            if self.kept(rec):
                self.runtime.append(rec)

    def runtime_file_records(self):
        """Every record on disk, in file order, parsed as load_runtime has always parsed them."""
        if not os.path.exists(self.runtime_path):
            return
        with open(self.runtime_path, "rt", encoding="utf-8") as fh:
            for line in fh:
                try:
                    rec = json.loads(line)
                except ValueError:
                    continue
                yield rec

    def kept(self, rec):
        """False only for a clock sample taken, or a disconnect ended, before runtime_from_ns.

        No window that write_runtime_slice serves from memory reads either of them.
        """
        if not isinstance(rec, dict):
            return True
        if rec.get("kind") == "clock":
            key = rec.get("recv_ns")
        elif rec.get("kind") == "disconnect":
            key = rec.get("end_recv_ns")
        else:
            return True
        return not isinstance(key, int) or key >= self.runtime_from_ns

    def prune_runtime(self, now_ns=None):
        """Forget what no slice served from memory can read again (RUNTIME_KEEP_S)."""
        now_ns = time.time_ns() if now_ns is None else now_ns
        self.runtime_from_ns = max(self.runtime_from_ns, now_ns - RUNTIME_KEEP_S * 10 ** 9)
        self.runtime = [r for r in self.runtime if self.kept(r)]

    def record(self, rec):
        self.runtime.append(rec)
        with open(self.runtime_path, "at", encoding="utf-8") as fh:
            fh.write(json.dumps(rec, sort_keys=True) + "\n")

    # ---- resource floors ---------------------------------------------------------

    def check_floors(self, where):
        """TZ-04a section 4. Two independent stops, whichever is reached first."""
        free = disk_free_bytes()
        used = tree_bytes(config.ROOT)
        if free < config.FREE_SPACE_FLOOR_BYTES:
            self.halt("free-space floor reached at %s: %d bytes free, floor is %d"
                      % (where, free, config.FREE_SPACE_FLOOR_BYTES))
            return False
        if used >= config.SELF_CAP_BYTES:
            self.halt("self-cap reached at %s: %d bytes captured, cap is %d"
                      % (where, used, config.SELF_CAP_BYTES))
            return False
        return True

    def halt(self, reason):
        if self.stopping:
            return
        self.stopping = True
        self.stop_reason = reason
        log("!!! STOP " + reason)
        log("!!! no new interval is opened; open intervals finish and are closed cleanly")
        log("!!! nothing is deleted - retention is an Architect decision (TZ-04a section 4)")
        self.record({"kind": "halt", "recv_ns": time.time_ns(), "reason": reason})

    # ---- capture -----------------------------------------------------------------

    def writer(self, t0, stream):
        key = (t0, stream)
        fh = self.writers.get(key)
        if fh is not None:
            return fh
        if t0 in self.done or (self.stopping and t0 not in self.live):
            return None
        path = config.interval_dir(t0)
        os.makedirs(path, exist_ok=True)
        fh = open(os.path.join(path, stream + ".jsonl"), "at", encoding="utf-8", buffering=1)
        self.writers[key] = fh
        return fh

    def store(self, raw, recv_ns, mono_ns):
        try:
            topic = json.loads(raw).get("topic")
        except Exception:
            return
        entry = config.TIER_A.get(topic)
        if entry is None:
            return
        stream = entry[1]
        # The line format is fixed by TZ-04a section 4: these three keys and nothing else.
        line = json.dumps({"recv_ns": recv_ns, "mono_ns": mono_ns, "raw": raw},
                          ensure_ascii=False, separators=(",", ":")) + "\n"
        for t0 in config.intervals_for(recv_ns / 1e9):
            fh = self.writer(t0, stream)
            if fh is not None:
                fh.write(line)

    # ---- interval lifecycle ------------------------------------------------------

    async def run_interval(self, t0):
        self.live.add(t0)
        path = config.interval_dir(t0)
        os.makedirs(path, exist_ok=True)
        try:
            await self.fetch_s6(t0, path)
            # Tier C reads the S6 document the line above captured, so it starts after it.
            # Its last checkpoint is T0 + 290, well inside the window closing at T0 + 333.
            quotes = asyncio.create_task(self.quotes(t0, path))
            await sleep_until(t0 + config.POST_S + GRACE_S)
            await asyncio.gather(quotes, return_exceptions=True)
            for stream in config.STREAM_FILES:
                fh = self.writers.pop((t0, stream), None)
                if fh is not None:
                    fh.close()
            self.done.add(t0)
            await self.close_interval(t0, path)
        except Exception as exc:            # a bad interval must not take the run down
            log("interval %d failed to close: %r" % (t0, exc))
        finally:
            self.live.discard(t0)

    async def close_interval(self, t0, path):
        for stream in config.STREAM_FILES + [config.QUOTES_STEM]:
            src = os.path.join(path, stream + ".jsonl")
            if os.path.exists(src):
                gzip_file(src, src + ".gz")
                os.remove(src)
        await self.fetch_s7(t0, path)
        self.write_runtime_slice(t0, path)
        self.prune_runtime()
        doc = manifest.write(path)
        log("closed %d complete=%s quotes_complete=%s msgs=%s" % (
            t0, doc["complete"], doc["quotes_complete"],
            {s: doc["streams"][s]["messages"] for s in config.STREAM_FILES}))
        self.check_floors("close of interval %d" % t0)

    async def recover(self):
        """Close intervals an earlier process captured but never finished.

        A restart must not orphan data. A directory whose window has ended but which has no
        manifest is gzipped, given its S7 and its runtime slice, and closed like any other.
        Its S6 is never fetched late: a directory that missed it at the open stays without it.
        """
        base = os.path.join(config.ROOT, config.SERIES)
        if not os.path.isdir(base):
            return
        now = time.time()
        for name in sorted((n for n in os.listdir(base) if n.isdigit()), key=int):
            t0, path = int(name), os.path.join(base, name)
            if os.path.exists(os.path.join(path, manifest.MANIFEST_NAME)):
                continue
            if t0 + config.POST_S + GRACE_S > now:
                continue                    # window still open: the scheduler reopens it
            self.done.add(t0)
            log("recovering interval %d" % t0)
            asyncio.create_task(self.recover_one(t0, path))

    async def recover_one(self, t0, path):
        self.live.add(t0)
        try:
            await self.close_interval(t0, path)
        except Exception as exc:
            log("interval %d failed to recover: %r" % (t0, exc))
        finally:
            self.live.discard(t0)

    async def fetch_s6(self, t0, path):
        target = os.path.join(path, "gamma.json")
        if os.path.exists(target):
            return                          # captured at the open by an earlier process
        await sleep_until(t0 + S6_FETCH_OFFSET_S)
        url = config.GAMMA_MARKET_BY_SLUG.format(slug=config.slug_for(t0))
        for _ in range(5):
            try:
                body = await asyncio.to_thread(fetch, url)
                # Stored whole and unparsed, exactly as the venue returned it.
                with open(target, "wb") as fh:
                    fh.write(body)
                return
            except Exception:
                await asyncio.sleep(3)
        log("S6 fetch failed for %d" % t0)

    async def fetch_s7(self, t0, path):
        if manifest.resolution_present(path):
            return
        url = config.GAMMA_MARKET_BY_SLUG.format(slug=config.slug_for(t0))
        deadline = t0 + S7_DEADLINE_S
        while time.time() < deadline:
            try:
                body = await asyncio.to_thread(fetch, url)
                doc = json.loads(body)
                market = doc[0] if isinstance(doc, list) else doc
                meta = (market.get("events") or [{}])[0].get("eventMetadata")
                if manifest.resolved_outcome(market) is not None and meta:
                    with open(os.path.join(path, "resolution.json"), "wb") as fh:
                        fh.write(body)
                    return
            except Exception:
                pass
            await asyncio.sleep(S7_POLL_S)
        log("S7 unresolved at deadline for %d" % t0)

    # ---- Tier C ------------------------------------------------------------------

    def tokens_for(self, t0, path):
        """The market's token ids, read out of the S6 document this interval already holds.

        TZ-05a section 3 names the source: the Gamma document captured as S6, which carries
        `clobTokenIds` and `outcomes` as parallel JSON-encoded arrays. Nothing is fetched
        again for this, and nothing about the ids is interpreted here.
        """
        try:
            with open(os.path.join(path, "gamma.json"), "rt", encoding="utf-8") as fh:
                doc = json.load(fh)
        except (OSError, ValueError):
            return []
        market = doc[0] if isinstance(doc, list) else doc
        try:
            ids = json.loads(market["clobTokenIds"])
        except (KeyError, TypeError, ValueError):
            return []
        return [str(i) for i in ids] if isinstance(ids, list) else []

    async def one_quote(self, tau, token_id):
        """One checkpoint read, returned as the line that will be written for it.

        `recv_ns` is stamped when the reply lands, exactly as every other stream stamps it.
        A read that produced no reply is recorded with a null status and null body: TZ-05a
        section 3 forbids retrying it into the next checkpoint's slot and forbids inventing
        a value for it.
        """
        url = config.CLOB_BOOK_BY_TOKEN.format(token_id=token_id)
        try:
            status, body = await asyncio.to_thread(fetch_status, url, QUOTE_TIMEOUT_S)
        except Exception as exc:
            recv_ns, mono_ns = now_pair()
            rec = {"recv_ns": recv_ns, "mono_ns": mono_ns, "tau": tau, "token_id": token_id,
                   "status": None, "raw": None, "error": repr(exc)}
        else:
            recv_ns, mono_ns = now_pair()
            rec = {"recv_ns": recv_ns, "mono_ns": mono_ns, "tau": tau, "token_id": token_id,
                   "status": status, "raw": body}
        return json.dumps(rec, ensure_ascii=False, separators=(",", ":")) + "\n"

    async def quotes(self, t0, path):
        """TZ-05a section 3: seven checkpoints, one read per token id at each of them."""
        tokens = self.tokens_for(t0, path)
        if not tokens:
            log("interval %d has no token ids: Tier C reads nothing" % t0)
            return
        ahead = config.quote_checkpoints_ahead(t0, time.time())
        if len(ahead) < len(config.QUOTE_TAUS):
            log("interval %d: %d checkpoints had already passed and are not read"
                % (t0, len(config.QUOTE_TAUS) - len(ahead)))
        out = os.path.join(path, config.QUOTES_STEM + ".jsonl")
        with open(out, "at", encoding="utf-8", buffering=1) as fh:
            for tau, when in ahead:
                await sleep_until(when)
                lines = await asyncio.gather(
                    *(self.one_quote(tau, token_id) for token_id in tokens))
                for line in lines:
                    fh.write(line)

    def write_runtime_slice(self, t0, path):
        """The recorder state this interval's manifest needs, copied into the directory.

        Without this the manifest could not be rebuilt from the directory alone and V5 would
        be testing nothing. The sha is that of every process that captured part of the window.
        """
        lo = (t0 - config.PRE_S) * 10 ** 9
        hi = (t0 + config.POST_S) * 10 ** 9
        starts = sorted((r for r in self.runtime if r.get("kind") == "start"),
                        key=lambda r: r["recv_ns"])
        active = ([r for r in starts if r["recv_ns"] <= lo][-1:]
                  + [r for r in starts if lo < r["recv_ns"] <= hi])
        out = [{"kind": "recorder", "recv_ns": r["recv_ns"], "sha": r["sha"]} for r in active]
        if not out:
            out = [{"kind": "recorder", "recv_ns": lo, "sha": self.sha}]
        # A window older than what memory holds is read back off disk, in the same order.
        source = self.runtime if lo >= self.runtime_from_ns else self.runtime_file_records()
        for rec in source:
            if rec.get("kind") == "disconnect":
                if rec["start_recv_ns"] <= hi and rec["end_recv_ns"] >= lo:
                    out.append(rec)
            elif rec.get("kind") == "clock":
                if lo <= rec["recv_ns"] <= hi:
                    out.append(rec)
        with open(os.path.join(path, manifest.RUNTIME_NAME), "wt", encoding="utf-8") as fh:
            for rec in out:
                fh.write(json.dumps(rec, sort_keys=True) + "\n")

    async def scheduler(self):
        while True:
            if not self.stopping:
                for t0 in config.intervals_for(time.time()):
                    if t0 not in self.live and t0 not in self.done:
                        asyncio.create_task(self.run_interval(t0))
            elif not self.live:
                return
            await asyncio.sleep(1)

    # ---- clock -------------------------------------------------------------------

    async def clock_sampler(self):
        while True:
            for host in config.NTP_SERVERS:
                try:
                    got = await asyncio.to_thread(sntp_best, host)
                except Exception:
                    got = None
                if got is not None:
                    ip, offset, rtt, replies, rejected = got
                    self.record({"kind": "clock", "recv_ns": time.time_ns(), "server": host,
                                 "ip": ip, "burst": replies,
                                 "offset_ms": None if offset is None else offset * 1000.0,
                                 "rtt_ms": None if rtt is None else rtt * 1000.0,
                                 "rejected": rejected,
                                 "rejected_count": sum(rejected.values())})
            await asyncio.sleep(config.NTP_SAMPLE_S)

    # ---- socket ------------------------------------------------------------------

    async def rtds(self):
        subs = [{"topic": t, "type": "*", "filters": f}
                for t, (f, _s) in config.TIER_A.items()]
        message = json.dumps({"action": "subscribe", "subscriptions": subs})
        # The start-up outage runs from the last frame any earlier process wrote to disk.
        down_since, detected, reason = last_frame_ns(config.ROOT), time.time_ns(), "startup"
        while not (self.stopping and not self.live):
            try:
                async with websockets.connect(config.RTDS_URL, open_timeout=20,
                                              ping_interval=None, max_size=None) as ws:
                    await ws.send(message)
                    up_ns = time.time_ns()
                    self.record({"kind": "disconnect", "start_recv_ns": down_since,
                                 "detected_recv_ns": detected, "end_recv_ns": up_ns,
                                 "reason": reason})
                    self.last_rx_ns = up_ns
                    log("RTDS connected")
                    pinger = asyncio.create_task(self.ping(ws))
                    try:
                        while True:
                            raw = await asyncio.wait_for(ws.recv(), timeout=RECV_TIMEOUT_S)
                            recv_ns, mono_ns = now_pair()
                            self.last_rx_ns = recv_ns
                            if isinstance(raw, bytes):
                                raw = raw.decode("utf-8", "replace")
                            if not raw or raw.strip() in ("PONG", "PING"):
                                continue
                            self.store(raw, recv_ns, mono_ns)
                    finally:
                        pinger.cancel()
            except Exception as exc:
                log("RTDS drop: %r" % (exc,))
            # The outage began at the last thing received, not when the silence was noticed.
            detected = time.time_ns()
            down_since = self.last_rx_ns or detected
            reason = "reconnect"
            await asyncio.sleep(2)

    async def ping(self, ws):
        try:
            while True:
                await asyncio.sleep(config.RTDS_PING_S)
                await ws.send("PING")
        except Exception:
            return

    async def main(self):
        os.makedirs(config.ROOT, exist_ok=True)
        self.load_runtime()
        log("recorder sha=%s root=%s" % (self.sha, config.ROOT))
        # TZ-04a section 4: both floors are checked before the first frame is written.
        free, used = disk_free_bytes(), tree_bytes(config.ROOT)
        self.record({"kind": "start", "recv_ns": time.time_ns(), "sha": self.sha,
                     "free_bytes": free, "captured_bytes": used})
        log("pre-run floors: free=%d (floor %d) captured=%d (cap %d)"
            % (free, config.FREE_SPACE_FLOOR_BYTES, used, config.SELF_CAP_BYTES))
        if not self.check_floors("start-up"):
            log("refusing to start: a section 4 floor is already breached")
            return 1
        await self.recover()
        side = [asyncio.create_task(self.rtds()), asyncio.create_task(self.clock_sampler())]
        try:
            await self.scheduler()      # returns only once a floor stopped the run
        finally:
            for task in side:
                task.cancel()
            await asyncio.gather(*side, return_exceptions=True)
        log("stopped: %s" % (self.stop_reason or "scheduler exit"))
        return 0


async def sleep_until(epoch_s):
    delay = epoch_s - time.time()
    if delay > 0:
        await asyncio.sleep(delay)


if __name__ == "__main__":
    sys.exit(asyncio.run(Recorder().main()))
```

### A.2 `research/tz21-recorder-memory.py`

```python file=research/tz21-recorder-memory.py
#!/usr/bin/env python3
"""TZ-21 - the recorder's memory, bounded: every check the TZ fixes, one mode per run.

    state            section 3.2  both units, both recorder trees, every copy of the three files
    synth            G-SYNTH      the old and the new recorder on synthetic histories, by slice
    equiv            G-EQUIV      the old and the new recorder on a snapshot of runtime.jsonl
    path             G-PATH       one live request per endpoint through the new recorder's functions
    mark NAME        section 3.5  an instant, with each unit's MainPID and NRestarts, in state.json
    restart          G-RESTART    one SIGTERM to the recorder, and systemd's start of the new code
    rec              G-REC        the first five qualifying intervals the new code captured, and
                                  every interval it closed before them
    final            G-FINAL      the recorder at the end of the session, then
                     G-CB-STILL   the chain book, untouched from `state` to the end
    revert           K-21         the recorder back on 4216c04 after the revert block
    reclaim TREE...  section 9    copies into the forensic store what a report names by hash

Under the recorder's capture root it opens the top-level runtime.jsonl, and a manifest.json or a
runtime.jsonl inside an interval directory G-REC compares, read-only; under the chain book's root,
nothing. An audit hook refuses any other open there and any open there for writing. It writes
under /root/tz21-work/ and, in `reclaim`, new files under /root/btc-forensics/ by exclusive
create; nothing else. The one file it removes is its own G-EQUIV snapshot, once that mode has
passed and the snapshot is shown to be the first bytes of the file it copied. It prints no
price, size, spread, mid, book level or outcome. Exit 0: every assert of the mode held. Exit 1:
an assert failed, and its message names it. Exit 3: NOT YET, with the instant to run the mode
again. Run it with the recorder's interpreter, /root/tz04a-env.

Written for CryptoTZ/TZ-21-recorder-memory.md. The TZ is the specification.
"""

import hashlib
import importlib.util
import json
import math
import os
import random
import re
import resource
import subprocess
import sys
import time
import urllib.error

if not __debug__:
    sys.stderr.write("tz21: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(2)

REC_UNIT = "btc-recorder.service"
CB_UNIT = "btc-chainbook.service"
REC_ARGV = ["/root/tz04a-env/venv/bin/python", "-B", "-u", "recorder.py"]
CB_ARGV = ["/root/tz01-env/venv/bin/python", "-B", "-u",
           "/root/tz18a-svc/tz18a-chainbook-capture.py", "--serve"]
SVC = "/root/btc-recorder-svc"
REC_CWD = SVC + "/research/recorder"
PRIMARY = "/root/btc-5m-twap"
OLD_DIR = PRIMARY + "/research/recorder"
WORK = "/root/tz21-work"
WT = WORK + "/wt"
NEW_DIR = WT + "/research/recorder"
STATE = WORK + "/state.json"
SCRATCH = WORK + "/scratch"
REC_ROOT = "/var/lib/btc-recorder"
REC_RUNTIME = REC_ROOT + "/runtime.jsonl"
REC_SERIES = REC_ROOT + "/btc-updown-5m"
CB_ROOT = "/var/lib/btc-chainbook"
UNIT_DIR = "/etc/systemd/system"
CGROUP = "/sys/fs/cgroup/system.slice/"
FORENSICS = "/root/btc-forensics"
REPORTS = PRIMARY + "/CryptoReports"

OLD_SHA = "4216c04673ced76b5b2ac60ef57c9abedc46f9b9"
OLD_FILES = {
    "recorder.py": "9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03",
    "config.py": "8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d",
    "manifest.py": "79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045",
}
NEW_FILES = dict(OLD_FILES)
NEW_FILES["recorder.py"] = "0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7"
MEMORY_MAX = {REC_UNIT: "536870912", CB_UNIT: "201326592"}   # TZ-20's ceilings, unchanged here

KEEP_S = 7200                # RUNTIME_KEEP_S in the new recorder.py
HELD_MAX = 2000              # records the new recorder may hold after any load or prune
SYNTH_FAST_MIN = 600
SYNTH_SLOW_MIN = 60
EQUIV_STEP = 25
EQUIV_FAST_MIN = 12
EQUIV_SLOW_MIN = 200
EQUIV_RECORDS_MAX = 120000   # the most runtime records the TZ's cost bound is stated at
EQUIV_BUDGET_S = 3000        # G-EQUIV's compute budget; a run projected past it is BLOCKED
EQUIV_PROBE = 10             # slow windows timed before the projection
MEM_FLOOR = 110000000        # MemAvailable below which synth and equiv do not start
REC_UNITS = 5
REC_COMPLETE_MIN = 3
REC_LEAD_S = 60
REC_DEADLINE_S = 3900
REC_BACK_S = 3900            # how far before the restart an interval the new code closed can open
RESTART_GAP_NS = 60 * 10 ** 9
KILL_SLACK_NS = 5 * 10 ** 9
UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")

OPENS = []
REC_MEMBERS = set()          # the intervals G-REC compares, once mode_rec has formed them


def _allowed(path):
    """The only files this instrument opens under a capture root."""
    if path == REC_RUNTIME:
        return True
    head, name = os.path.split(path)
    parent, interval = os.path.split(head)
    return (parent == REC_SERIES and interval.isdigit() and int(interval) in REC_MEMBERS
            and name in ("manifest.json", "runtime.jsonl"))


def _audit(event, args):
    """V12 - under either capture root only the named files are opened, and only to read."""
    if event != "open" or not args or not isinstance(args[0], str):
        return
    path = os.path.abspath(args[0])
    for root in (REC_ROOT, CB_ROOT):
        if path == root or path.startswith(root + "/"):
            mode = args[1] if len(args) > 1 else None
            flags = args[2] if len(args) > 2 else 0
            writing = (isinstance(mode, str) and any(c in mode for c in "wax+")) or \
                (isinstance(flags, int) and flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT
                                                     | os.O_APPEND | os.O_TRUNC))
            if not _allowed(path) or writing:
                raise RuntimeError("V12: open refused under a capture root: %s %r" % (path, mode))
            OPENS.append(path)


sys.addaudithook(_audit)


def out(msg):
    sys.stdout.write("[%s] %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    sys.stdout.flush()


def utc(seconds):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(seconds))


def sha256_file(path):
    """A file's SHA-256, read a mebibyte at a time, so no file is ever held whole."""
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def read_text(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def scan_runtime(path, keep=lambda rec: False):
    """One pass over a runtime.jsonl, one line in memory at a time: only the records `keep`
    accepts, in file order, the count of each kind, the torn-line count, the newline count and
    whether the file ends with a newline."""
    kept, kinds, torn, newlines, last = [], {}, 0, 0, b""
    with open(path, "rb") as fh:
        for line in fh:
            newlines += 1 if line.endswith(b"\n") else 0
            last = line
            if not line.strip():
                continue
            try:
                rec = json.loads(line)
            except ValueError:
                torn += 1
                continue
            kind = rec.get("kind") if isinstance(rec, dict) else None
            kinds[kind] = kinds.get(kind, 0) + 1
            if keep(rec):
                kept.append(rec)
    return kept, kinds, torn, newlines, last.endswith(b"\n")


def is_start(rec):
    return isinstance(rec, dict) and rec.get("kind") == "start"


def head_of(tree):
    cp = subprocess.run(["git", "-C", tree, "rev-parse", "HEAD"], capture_output=True, text=True)
    assert cp.returncode == 0, "git rev-parse in %s exited %d" % (tree, cp.returncode)
    return cp.stdout.strip()


def clean(tree):
    cp = subprocess.run(["git", "-C", tree, "status", "--porcelain"], capture_output=True,
                        text=True)
    assert cp.returncode == 0, "git status in %s exited %d" % (tree, cp.returncode)
    return cp.stdout == ""


def files_equal(directory, files, label):
    for name, want in sorted(files.items()):
        got = sha256_file(os.path.join(directory, name))
        assert got == want, "%s: %s/%s sha256 %s, expected %s" % (label, directory, name, got,
                                                                  want)
    out("%s: %s, %d of %d files equal" % (label, directory, len(files), len(files)))


def not_yet(again_s, what):
    out("NOT YET: %s; run this mode again at or after %s" % (what, utc(again_s)))
    out("opens under the capture roots: %d" % len(OPENS))
    sys.exit(3)


# ---- systemd, /proc and the control group -------------------------------------------------

PROPS = ("ActiveState", "SubState", "UnitFileState", "FragmentPath", "ControlGroup", "MainPID",
         "NRestarts", "Result", "ExecMainStartTimestamp", "MemoryMax", "MemoryCurrent",
         "MemoryPeak")
MEM_FILES = ("memory.current", "memory.peak", "memory.max", "memory.swap.current",
             "memory.swap.peak", "memory.swap.max")
STAT_KEYS = ("anon", "file", "kernel", "kernel_stack", "pagetables", "sock", "shmem",
             "slab_reclaimable", "slab_unreclaimable")


def show(unit):
    cp = subprocess.run(["systemctl", "show", unit] + ["--property=" + p for p in PROPS],
                        capture_output=True, text=True)
    assert cp.returncode == 0, "systemctl show %s exited %d: %s" % (unit, cp.returncode,
                                                                    cp.stderr.strip())
    props = {}
    for line in cp.stdout.splitlines():
        key, _, value = line.partition("=")
        props[key] = value
    return props


def proc_argv(pid):
    with open("/proc/%d/cmdline" % pid, "rb") as fh:
        fields = fh.read().split(b"\0")
    if fields and fields[-1] == b"":
        fields = fields[:-1]
    return fields


def proc_argvs():
    found = {}
    for name in os.listdir("/proc"):
        if not name.isdigit():
            continue
        try:
            found[int(name)] = proc_argv(int(name))
        except OSError:
            continue
    return found


def recorder_like(found):
    """tz10b.recorder_pids's rule: every process with an argument ending in recorder.py."""
    return sorted(p for p, a in found.items() if any(x.endswith(b"recorder.py") for x in a))


def chainbook_like(found):
    return sorted(p for p, a in found.items()
                  if any(x.endswith(b"tz18a-chainbook-capture.py") for x in a))


def cgroup_paths(pid):
    with open("/proc/%d/cgroup" % pid) as fh:
        lines = fh.read().splitlines()
    return [line.split(":", 2)[2] for line in lines if line.count(":") >= 2]


def check_unit(unit, argv, cwd, restarts):
    """G-UNIT for one unit: TZ-20 section 4.1's checks, at TZ-20's MemoryMax. `restarts` None
    reads NRestarts without asserting it. Returns (MainPID, NRestarts)."""
    props = show(unit)
    out("U %s %s" % (unit, json.dumps(props, sort_keys=True)))
    for key, want in (("ActiveState", "active"), ("SubState", "running"),
                      ("UnitFileState", "enabled"), ("FragmentPath", UNIT_DIR + "/" + unit),
                      ("ControlGroup", "/system.slice/" + unit), ("MemoryMax", MEMORY_MAX[unit])):
        assert props.get(key) == want, "G-UNIT %s: %s %r, expected %r" % (unit, key,
                                                                         props.get(key), want)
    n = int(props.get("NRestarts") or -1)
    assert n >= 0, "G-UNIT %s: NRestarts %r" % (unit, props.get("NRestarts"))
    if restarts is not None:
        assert n == restarts, "G-UNIT %s: NRestarts %d, expected %d" % (unit, n, restarts)
    pid = int(props.get("MainPID") or 0)
    assert pid > 0, "G-UNIT %s: no MainPID" % unit
    got = [f.decode("utf-8") for f in proc_argv(pid)]
    assert got == argv, "G-UNIT %s: pid %d argv %r is not %r" % (unit, pid, got, argv)
    if cwd is not None:
        here = os.readlink("/proc/%d/cwd" % pid)
        assert here == cwd, "G-UNIT %s: pid %d cwd %r is not %r" % (unit, pid, here, cwd)
    paths = cgroup_paths(pid)
    assert "/system.slice/" + unit in paths, "G-UNIT %s: pid %d cgroups %r" % (unit, pid, paths)
    assert not any(p.startswith("/user.slice") for p in paths), \
        "G-UNIT %s: pid %d is inside a user slice: %r" % (unit, pid, paths)
    out("G-UNIT %s: pid %d, argv equal, cgroup /system.slice/%s, NRestarts %d, MemoryMax %s"
        % (unit, pid, unit, n, MEMORY_MAX[unit]))
    return pid, n


def sole_recorder(rec_pid):
    found = recorder_like(proc_argvs())
    assert found == [rec_pid], "recorder processes %r, expected [%d]" % (found, rec_pid)
    out("sole instance: recorder %d" % rec_pid)


def sole_chainbook(cb_pid):
    found = chainbook_like(proc_argvs())
    assert found == [cb_pid], "chain book processes %r, expected [%d]" % (found, cb_pid)
    out("sole instance: chain book %d" % cb_pid)


def meminfo():
    """The host's memory as /proc/meminfo states it, in bytes, recorded and not gated."""
    got = {}
    for line in read_text("/proc/meminfo").splitlines():
        key, _, rest = line.partition(":")
        if key in ("MemTotal", "MemAvailable", "SwapTotal", "SwapFree"):
            got[key] = int(rest.split()[0]) * 1024
    out("H /proc/meminfo %s" % json.dumps(got, sort_keys=True))
    return got


def memory(unit):
    """The unit's control-group memory files as the kernel writes them, recorded and not gated."""
    base = CGROUP + unit + "/"
    got = {}
    for name in MEM_FILES:
        path = base + name
        got[name] = read_text(path).strip() if os.path.exists(path) else None
    stat = {}
    if os.path.exists(base + "memory.stat"):
        for line in read_text(base + "memory.stat").splitlines():
            key, _, value = line.partition(" ")
            if key in STAT_KEYS:
                stat[key] = int(value)
    got["memory.stat"] = stat
    out("M %s %s" % (unit, json.dumps(got, sort_keys=True)))
    return got


# ---- state.json ----------------------------------------------------------------------------

def load_state():
    with open(STATE, encoding="utf-8") as fh:
        return json.load(fh)


def save_state(state):
    tmp = STATE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(state, sort_keys=True) + "\n")
    os.replace(tmp, STATE)


# ---- the two recorders ---------------------------------------------------------------------

def load_recorder(directory, name, files):
    """recorder.py from one directory under its own module name, every file hash-asserted first.
    config and manifest are imported once and shared: they are byte-identical in both copies."""
    files_equal(directory, files, "load %s" % name)
    if directory not in sys.path:
        sys.path.insert(0, directory)
    spec = importlib.util.spec_from_file_location(name, os.path.join(directory, "recorder.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for dep in ("config", "manifest"):
        loaded = os.path.realpath(sys.modules[dep].__file__)
        assert sha256_file(loaded) == files[dep + ".py"], "%s loaded from %s" % (dep, loaded)
    return mod


def instance(mod, runtime_path, sha):
    """A Recorder of `mod` reading `runtime_path`; nothing else of it runs. `sha` is the start
    record a window with no start before it would name: the same string for both copies."""
    rec = mod.Recorder()
    rec.runtime_path = runtime_path
    rec.sha = sha
    return rec


def slice_bytes(rec, t0, directory):
    os.makedirs(directory, exist_ok=True)
    rec.write_runtime_slice(t0, directory)
    with open(os.path.join(directory, "runtime.jsonl"), "rb") as fh:
        return fh.read()


def window_of(t0):
    return (t0 - 90) * 10 ** 9, (t0 + 330) * 10 ** 9


# ---- G-SYNTH ---------------------------------------------------------------------------------

SYN_BASE = 1791000000        # a synthetic epoch on the 300 s grid


def syn_clock(t_ns, i, rng):
    return {"kind": "clock", "recv_ns": t_ns, "server": ("108.61.73.243", "pool.ntp.org")[i % 2],
            "ip": "193.70.94.%d" % (i % 250), "burst": 4,
            "offset_ms": rng.uniform(-30.0, 30.0), "rtt_ms": rng.uniform(0.5, 100.0),
            "rejected": {}, "rejected_count": 0}


def syn_events(t_from, t_to, rng, first=0):
    """(write_ns, record) in write order: a clock sample every 30 s, a reconnect every 7,200 s."""
    events, i = [], first
    t = t_from
    while t < t_to:
        t_ns = t * 10 ** 9 + rng.randrange(10 ** 9)
        events.append((t_ns, syn_clock(t_ns, i, rng)))
        if (t - SYN_BASE) % 7200 == 3570:
            end = t_ns + 2 * 10 ** 9
            events.append((end, {"kind": "disconnect", "start_recv_ns": t_ns - 10 ** 9,
                                 "detected_recv_ns": t_ns + 10 ** 9, "end_recv_ns": end,
                                 "reason": "reconnect"}))
        i += 1
        t += 30
    return events, i


class Pair:
    """An old and a new recorder process, each writing its own copy of one runtime.jsonl."""

    def __init__(self, old_mod, new_mod, base, now_ns):
        self.base = base
        for side in ("old", "new"):
            os.makedirs(os.path.join(base, side), exist_ok=True)
        self.old = instance(old_mod, os.path.join(base, "old", "runtime.jsonl"), "s" * 40)
        self.new = instance(new_mod, os.path.join(base, "new", "runtime.jsonl"), "s" * 40)
        self.old.load_runtime()
        self.new.load_runtime(now_ns=now_ns)
        self.fast = self.slow = self.held = 0
        self.check_held()

    def record(self, rec):
        self.old.record(dict(rec))
        self.new.record(dict(rec))

    def check_held(self):
        self.held = max(self.held, len(self.new.runtime))
        assert len(self.new.runtime) <= HELD_MAX, "G-SYNTH: the new recorder holds %d records" % (
            len(self.new.runtime))

    def compare(self, t0, now_ns, prune=True):
        lo, _hi = window_of(t0)
        fast = lo >= self.new.runtime_from_ns
        a = slice_bytes(self.old, t0, os.path.join(self.base, "slice-old"))
        b = slice_bytes(self.new, t0, os.path.join(self.base, "slice-new"))
        assert a == b, "G-SYNTH: window %d differs (%s path)" % (t0, "fast" if fast else "slow")
        if fast:
            self.fast += 1
        else:
            self.slow += 1
        if prune:
            self.new.prune_runtime(now_ns=now_ns)
            self.check_held()

    def files_equal(self):
        with open(self.old.runtime_path, "rb") as fa, open(self.new.runtime_path, "rb") as fb:
            assert fa.read() == fb.read(), "G-SYNTH: the two runtime files differ"


def write_raw(path, lines):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", encoding="utf-8") as fh:
        for line in lines:
            fh.write(line)


def run_live(pair, events, t0_from, t0_to, rng, delays, old_every=0):
    """Replays `events` and closes every window T0 in [t0_from, t0_to) at T0 + a delay, in time
    order, as close_interval does: the slice, then the prune. Every `old_every`-th close also
    slices a window a day older, which the new recorder serves from disk."""
    closes = []
    for k, t0 in enumerate(range(t0_from, t0_to, 300)):
        closes.append(((t0 + delays[k % len(delays)]) * 10 ** 9, t0))
    queue = sorted([(t, 0, r) for t, r in events] + [(t, 1, t0) for t, t0 in closes],
                   key=lambda e: (e[0], e[1]))
    n = 0
    for t_ns, kind, item in queue:
        if kind == 0:
            pair.record(item)
        else:
            pair.compare(item, t_ns)
            n += 1
            if old_every and n % old_every == 0:
                pair.compare(item - 86400, t_ns, prune=False)
    return n


def mode_synth():
    avail = meminfo()["MemAvailable"]
    assert avail >= MEM_FLOOR, "BLOCKED: MemAvailable %d bytes, below the floor of %d" % (
        avail, MEM_FLOOR)
    old = load_recorder(OLD_DIR, "recorder_old", OLD_FILES)
    new = load_recorder(NEW_DIR, "recorder_new", NEW_FILES)
    assert new.RUNTIME_KEEP_S == KEEP_S, "G-SYNTH: RUNTIME_KEEP_S %r" % new.RUNTIME_KEEP_S
    assert not hasattr(old.Recorder, "prune_runtime"), "G-SYNTH: the old copy is not 4216c04's"
    rng = random.Random(21)
    base = os.path.join(SCRATCH, "synth-%d" % time.time_ns())    # a fresh tree for every run
    os.makedirs(base)
    delays = (333, 633, 1833, 3633, 348, 3333)
    totals = {"fast": 0, "slow": 0, "held": 0, "old_held": 0}

    def tally(p):
        totals["fast"] += p.fast
        totals["slow"] += p.slow
        totals["held"] = max(totals["held"], p.held)
        totals["old_held"] = max(totals["old_held"], len(p.old.runtime))

    # 1. steady: three days already on disk, a process starts, two days run, windows close late
    #    and out of order, and a day-old window is sliced at every tenth close.
    s1 = os.path.join(base, "steady")
    t_start = SYN_BASE + 3 * 86400
    pre, i = syn_events(SYN_BASE, t_start, rng)
    start = {"kind": "start", "recv_ns": t_start * 10 ** 9, "sha": "a" * 40,
             "free_bytes": 1, "captured_bytes": 1}
    lines = [json.dumps(r, sort_keys=True) + "\n" for _t, r in pre]
    for side in ("old", "new"):
        write_raw(os.path.join(s1, side, "runtime.jsonl"), lines)
    del pre, lines
    pair = Pair(old, new, s1, t_start * 10 ** 9 + 5 * 10 ** 8)
    pair.record(start)
    live, i = syn_events(t_start, t_start + 2 * 86400, rng, i)
    n1 = run_live(pair, live, t_start + 300, t_start + 2 * 86400 - 3900, rng, delays, 10)
    pair.files_equal()
    out("G-SYNTH steady: %d closes, %d fast and %d slow slices equal; held at most %d records, "
        "the old recorder %d" % (n1, pair.fast, pair.slow, pair.held, len(pair.old.runtime)))
    last_frame = live[-1][0]
    tally(pair)
    del pair, live

    # 2. an outage of 158,581 s, then a restart: both recover the two windows open at the crash
    #    and the one before them, from disk, then run three hours.
    crash = t_start + 2 * 86400
    restart = crash + 158581
    t_restart = restart * 10 ** 9
    pair2 = Pair(old, new, s1, t_restart)
    pair2.record({"kind": "start", "recv_ns": t_restart, "sha": "b" * 40, "free_bytes": 1,
                  "captured_bytes": 1})
    for t0 in (crash - crash % 300 - 300, crash - crash % 300, crash - crash % 300 - 600):
        pair2.compare(t0, t_restart + 10 ** 9)
    pair2.record({"kind": "disconnect", "start_recv_ns": last_frame,
                  "detected_recv_ns": t_restart + 10 ** 9, "end_recv_ns": t_restart + 3 * 10 ** 9,
                  "reason": "startup"})
    later, i = syn_events(restart + 3, restart + 3 * 3600 + 3, rng, i)
    t0_first = restart - restart % 300 + 300
    n2 = run_live(pair2, later, t0_first, restart + 3 * 3600 - 3900, rng, delays, 4)
    for t0 in range(crash - crash % 300 - 1500, crash - crash % 300 + 300, 300):
        pair2.compare(t0, (restart + 3 * 3600) * 10 ** 9, prune=False)
    pair2.files_equal()
    out("G-SYNTH outage: %d recovered and %d live closes, %d fast and %d slow slices equal; held "
        "at most %d records" % (3, n2, pair2.fast, pair2.slow, pair2.held))
    tear_paths = (pair2.old.runtime_path, pair2.new.runtime_path)
    tally(pair2)
    del pair2, later

    # 3. a torn tail: the old process dies mid-line, the next start lands on the same line, and the
    #    windows on both sides of it are sliced by both.
    tear = restart + 3 * 3600 + 3
    for path in tear_paths:
        write_raw(path, ['{"kind": "clock", "recv_ns": %d, "ser' % (tear * 10 ** 9)])
    t_ns3 = (tear + 600) * 10 ** 9
    pair3 = Pair(old, new, s1, t_ns3)
    pair3.record({"kind": "start", "recv_ns": t_ns3, "sha": "c" * 40, "free_bytes": 1,
                  "captured_bytes": 1})
    more, i = syn_events(tear + 601, tear + 601 + 2 * 3600, rng, i)
    n3 = run_live(pair3, more, tear - tear % 300 + 900, tear + 601 + 2 * 3600 - 3900, rng,
                  delays, 3)
    for t0 in range(tear - tear % 300 - 900, tear - tear % 300 + 900, 300):
        pair3.compare(t0, (tear + 601 + 2 * 3600) * 10 ** 9, prune=False)
    _kept, _kinds, torn, _n, _t = scan_runtime(pair3.new.runtime_path)
    assert torn == 1, "G-SYNTH: the torn tail left %d torn lines" % torn
    pair3.files_equal()
    out("G-SYNTH torn tail: %d closes, %d fast and %d slow slices equal" % (n3, pair3.fast,
                                                                              pair3.slow))
    tally(pair3)
    del pair3, more

    # 4. ten days of one process: what it holds stays bounded while the old copy grows.
    s4 = os.path.join(base, "days")
    t4 = SYN_BASE
    pair4 = Pair(old, new, s4, t4 * 10 ** 9)
    pair4.record({"kind": "start", "recv_ns": t4 * 10 ** 9, "sha": "d" * 40, "free_bytes": 1,
                  "captured_bytes": 1})
    # The events are generated a day at a time, so only one day of them is ever held; the days
    # draw from the generator in the same order a single call would, so every value is the same.
    days = [(t4 + 1 + d * 86400, min(t4 + 1 + (d + 1) * 86400, t4 + 10 * 86400))
            for d in range(10)]
    queue, j, k = [], 0, 0
    for t0 in range(t4 + 300, t4 + 10 * 86400 - 3900, 300):
        close_ns = (t0 + 333) * 10 ** 9
        while True:
            if j == len(queue):
                if not days:
                    break
                queue, i = syn_events(days[0][0], days[0][1], rng, i)
                days.pop(0)
                j = 0
                continue
            if queue[j][0] > close_ns:
                break
            pair4.record(queue[j][1])
            j += 1
        k += 1
        if k % 12 == 0:
            pair4.compare(t0, close_ns)
        else:
            pair4.new.prune_runtime(now_ns=close_ns)
            pair4.check_held()
    while days:                     # the draws the days not reached take, as one call made them
        _rest, i = syn_events(days[0][0], days[0][1], rng, i)
        days.pop(0)
    pair4.files_equal()
    assert len(pair4.old.runtime) >= 9 * 2880, "G-SYNTH: the old copy holds %d" % (
        len(pair4.old.runtime))
    out("G-SYNTH ten days: %d closes, %d slices equal; the new recorder held at most %d records, "
        "the old %d at the end" % (k, pair4.fast + pair4.slow, pair4.held, len(pair4.old.runtime)))
    tally(pair4)
    del pair4, queue

    # 5. negative controls: the comparison sees a record missing from memory on the fast path,
    #    and a record missing from the file on the slow path.
    s5 = os.path.join(base, "controls")
    t5 = SYN_BASE + 86400
    pre5, i = syn_events(SYN_BASE, t5, rng, i)
    lines5 = [json.dumps(r, sort_keys=True) + "\n" for _t, r in pre5]
    for side in ("old", "new"):
        write_raw(os.path.join(s5, side, "runtime.jsonl"), lines5)
    pair5 = Pair(old, new, s5, t5 * 10 ** 9)
    pair5.record({"kind": "start", "recv_ns": t5 * 10 ** 9, "sha": "e" * 40, "free_bytes": 1,
                  "captured_bytes": 1})
    tail5, i = syn_events(t5 + 1, t5 + 3600, rng, i)
    for _t, r in tail5:
        pair5.record(r)
    recent, aged = t5 + 1800 - (t5 + 1800) % 300, t5 - 43200 - (t5 - 43200) % 300
    pair5.compare(recent, (t5 + 3600) * 10 ** 9, prune=False)
    pair5.compare(aged, (t5 + 3600) * 10 ** 9, prune=False)
    held = pair5.new.runtime
    pair5.new.runtime = [r for r in held if r.get("kind") != "clock"]
    try:
        pair5.compare(recent, (t5 + 3600) * 10 ** 9, prune=False)
        nc1 = False
    except AssertionError:
        nc1 = True
    pair5.new.runtime = held
    with open(pair5.new.runtime_path, encoding="utf-8") as fh:
        kept_lines = fh.readlines()
    dropped = [ln for ln in kept_lines
               if not (json.loads(ln).get("kind") == "clock"
                       and (aged - 90) * 10 ** 9 <= json.loads(ln)["recv_ns"]
                       <= (aged + 330) * 10 ** 9)]
    with open(pair5.new.runtime_path, "w", encoding="utf-8") as fh:
        fh.writelines(dropped)
    try:
        pair5.compare(aged, (t5 + 3600) * 10 ** 9, prune=False)
        nc2 = False
    except AssertionError:
        nc2 = True
    assert nc1 and nc2, "G-SYNTH: a negative control was not detected (fast %s, slow %s)" % (
        nc1, nc2)
    out("G-SYNTH negative controls: a clock missing from memory on the fast path and from the "
        "file on the slow path are each detected, 2 of 2 (%d lines removed)"
        % (len(kept_lines) - len(dropped)))

    assert totals["fast"] >= SYNTH_FAST_MIN and totals["slow"] >= SYNTH_SLOW_MIN, \
        "G-SYNTH: only %d fast and %d slow slices" % (totals["fast"], totals["slow"])
    out("G-SYNTH PASS: %d slices equal, %d fast and %d slow; the new recorder held at most %d "
        "records, the old %d" % (totals["fast"] + totals["slow"], totals["fast"], totals["slow"],
                                 totals["held"], totals["old_held"]))


# ---- G-EQUIV --------------------------------------------------------------------------------

class Sink:
    """Takes what load_runtime appends and keeps a count and a digest of it, not the list."""

    def __init__(self):
        self.n = 0
        self._h = hashlib.sha256()

    def append(self, rec):
        self.n += 1
        self._h.update(json.dumps(rec, sort_keys=True).encode("utf-8") + b"\n")

    def digest(self):
        return self._h.hexdigest()


def equiv_windows(records, snap_s):
    """The windows G-EQUIV slices, every one ending before the snapshot: every EQUIV_STEP-th of
    the capture's span, every one the new recorder serves from memory, the first and the last
    window each disconnect overlaps, and every window within 600 s of a start record."""
    starts = sorted(r["recv_ns"] for r in records if r.get("kind") == "start")
    assert starts, "G-EQUIV: no start record"
    first = (starts[0] // 10 ** 9) - (starts[0] // 10 ** 9) % 300 + 300
    last = snap_s - 330
    last -= last % 300
    span = list(range(first, last + 1, 300))
    chosen = set(span[::EQUIV_STEP])
    chosen.update(t for t in span if (t - 90) * 10 ** 9 >= snap_s * 10 ** 9 - KEEP_S * 10 ** 9)
    for r in records:
        if r.get("kind") != "disconnect":
            continue
        a, c = r["start_recv_ns"] // 10 ** 9, r["end_recv_ns"] // 10 ** 9
        hit = [t for t in span if t - 90 <= c and t + 330 >= a]
        chosen.update(hit[:1] + hit[-1:])
    for s in starts:
        s //= 10 ** 9
        chosen.update(t for t in span if t - 90 <= s + 600 and t + 330 >= s - 600)
    return sorted(chosen), len(span)


def mode_equiv():
    avail = meminfo()["MemAvailable"]
    assert avail >= MEM_FLOOR, "BLOCKED: MemAvailable %d bytes, below the floor of %d" % (
        avail, MEM_FLOOR)
    old = load_recorder(OLD_DIR, "recorder_old", OLD_FILES)
    new = load_recorder(NEW_DIR, "recorder_new", NEW_FILES)
    assert new.RUNTIME_KEEP_S == KEEP_S, "G-EQUIV: RUNTIME_KEEP_S %r" % new.RUNTIME_KEEP_S
    base = os.path.join(SCRATCH, "equiv-%d" % time.time_ns())    # a fresh tree for every run
    os.makedirs(base)
    snap = os.path.join(base, "runtime.jsonl")
    snap_ns = time.time_ns()
    h, size = hashlib.sha256(), 0
    with open(REC_RUNTIME, "rb") as src, open(snap, "xb") as dst:
        for chunk in iter(lambda: src.read(1 << 20), b""):
            dst.write(chunk)
            h.update(chunk)
            size += len(chunk)
    digest = h.hexdigest()
    out("G-EQUIV snapshot of %s at %s: %d bytes, sha256 %s"
        % (REC_RUNTIME, utc(snap_ns / 1e9), size, digest))
    n = instance(new, snap, OLD_SHA)
    n.load_runtime(now_ns=snap_ns)
    assert len(n.runtime) <= HELD_MAX, "G-EQUIV: the new recorder holds %d" % len(n.runtime)
    # The old recorder's own load_runtime, into a sink that keeps the count and a digest of the
    # list it builds rather than the list; one parse of the snapshot must give the same two.
    o = instance(old, snap, OLD_SHA)
    o.runtime = Sink()
    o.load_runtime()
    parsed = Sink()

    def marks(rec):
        parsed.append(rec)
        return isinstance(rec, dict) and rec.get("kind") in ("start", "disconnect")
    starts_and_gaps, _kinds, torn, _newlines, _t = scan_runtime(snap, marks)
    assert (o.runtime.n, o.runtime.digest()) == (parsed.n, parsed.digest()), \
        "G-EQUIV: the old load holds %d records, the parse %d" % (o.runtime.n, parsed.n)
    old_held = o.runtime.n
    windows, span = equiv_windows(starts_and_gaps, snap_ns // 10 ** 9)
    # Every record any chosen window's old slice can select, in file order: every start, every
    # clock inside a chosen window, every disconnect overlapping one. The old code's own filter
    # then picks from these exactly what it picks from the whole list.
    chosen = set(windows)
    bounds = [window_of(t) for t in windows]

    def selectable(rec):
        if not isinstance(rec, dict):
            return True
        kind = rec.get("kind")
        if kind == "start":
            return True
        if kind == "clock":
            x = rec.get("recv_ns")
            if not isinstance(x, int):
                return True             # the old code meets it as it would in the whole list
            base = (x // 10 ** 9) - (x // 10 ** 9) % 300
            return any(t in chosen and window_of(t)[0] <= x <= window_of(t)[1]
                       for t in (base - 300, base, base + 300))
        if kind == "disconnect":
            a, c = rec.get("start_recv_ns"), rec.get("end_recv_ns")
            if not (isinstance(a, int) and isinstance(c, int)):
                return True
            return any(a <= hi and c >= lo for lo, hi in bounds)
        return False
    o.runtime, _kinds, _torn, _newlines, _t = scan_runtime(snap, selectable)
    out("G-EQUIV loaded: the old load holds %d records (%d torn lines skipped), count and digest "
        "equal to the parse; the old slices read the %d of them the chosen windows can select; "
        "the new recorder holds %d, from %s on" % (old_held, torn, len(o.runtime), len(n.runtime),
                                                   utc(n.runtime_from_ns / 1e9)))
    fast = slow = 0
    slow_total = sum(1 for t in windows if window_of(t)[0] < n.runtime_from_ns)
    t_start = time.monotonic()
    for t0 in windows:
        lo, _hi = window_of(t0)
        a = slice_bytes(o, t0, os.path.join(base, "slice-old"))
        b = slice_bytes(n, t0, os.path.join(base, "slice-new"))
        assert a == b, "G-EQUIV: window %d %s differs" % (t0, utc(t0))
        if lo >= n.runtime_from_ns:
            fast += 1
        else:
            slow += 1
            if slow == EQUIV_PROBE:
                spent = time.monotonic() - t_start
                projected = spent / (fast + slow) * len(windows)
                out("G-EQUIV projected %.0f s for %d windows, %d of them slow, after %.1f s"
                    % (projected, len(windows), slow_total, spent))
                if projected > EQUIV_BUDGET_S:
                    raise SystemExit("G-EQUIV BLOCKED: projected %.0f s against the budget of %d s"
                                     % (projected, EQUIV_BUDGET_S))
    out("G-EQUIV windows: %d of the span's %d, %s to %s, in %.1f s"
        % (len(windows), span, utc(windows[0]), utc(windows[-1]), time.monotonic() - t_start))
    assert fast >= EQUIV_FAST_MIN and slow >= EQUIV_SLOW_MIN, \
        "G-EQUIV: only %d fast and %d slow windows" % (fast, slow)
    # The capture appends and never rewrites, so the snapshot is the file's first `size` bytes
    # for good: shown here, then the copy goes, and anyone re-derives it from the capture.
    h, left = hashlib.sha256(), size
    with open(REC_RUNTIME, "rb") as fh:
        for chunk in iter(lambda: fh.read(min(left, 1 << 20)), b""):
            h.update(chunk)
            left -= len(chunk)
    assert left == 0 and h.hexdigest() == digest, \
        "G-EQUIV: %s no longer begins with the snapshot" % REC_RUNTIME
    os.remove(snap)
    out("G-EQUIV the snapshot is the first %d bytes of %s, sha256 %s; the copy is removed"
        % (size, REC_RUNTIME, digest))
    out("G-EQUIV PASS: %d windows equal, %d fast and %d slow; the new recorder holds %d records "
        "against the old %d" % (fast + slow, fast, slow, len(n.runtime), old_held))


# ---- G-PATH ---------------------------------------------------------------------------------

def mode_path():
    import asyncio
    head = load_state()["branch_head"]
    got = head_of(SVC)
    assert got == head, "P0: %s is at %s, the branch at %s" % (SVC, got, head)
    rec = load_recorder(REC_CWD, "recorder", NEW_FILES)
    import config
    import websockets
    src = os.path.realpath(rec.__file__)
    assert src == os.path.join(REC_CWD, "recorder.py"), "P0: recorder loaded from %s" % src
    sha = rec.git_sha()
    assert sha == head, "P0: git_sha() %r" % sha
    out("P0 recorder.py %s, git_sha %s, websockets %s, User-Agent %r"
        % (src, sha, websockets.__version__, config.USER_AGENT))

    now = int(time.time())
    t0 = now - now % config.INTERVAL_S
    if now - t0 < 30:
        t0 -= config.INTERVAL_S
    url = config.GAMMA_MARKET_BY_SLUG.format(slug=config.slug_for(t0))
    try:
        body = rec.fetch(url)
    except urllib.error.HTTPError as exc:
        raise AssertionError("P1: %s answered HTTP %d" % (url, exc.code))
    doc = json.loads(body)
    market = doc[0] if isinstance(doc, list) else doc
    ids = json.loads(market["clobTokenIds"])
    assert isinstance(ids, list) and len(ids) == 2 and all(ids), "P1: clobTokenIds %r" % (ids,)
    out("P1 %s: served, %d bytes, JSON, token ids %s" % (url, len(body), ids))

    book = config.CLOB_BOOK_BY_TOKEN.format(token_id=ids[0])
    status, text = rec.fetch_status(book, rec.QUOTE_TIMEOUT_S)
    assert status == 200, "P2: %s status %r" % (book, status)
    json.loads(text)
    out("P2 %s: status %d, %d bytes, JSON" % (book, status, len(text.encode("utf-8"))))

    answered = 0
    for host in config.NTP_SERVERS:
        try:
            ip, offset, rtt, accepted, rejected = rec.sntp_best(host)
        except Exception as exc:
            out("P3 SNTP %s: no reply (%s)" % (host, type(exc).__name__))
            continue
        if offset is None:
            out("P3 SNTP %s (%s): 0 accepted, rejected %s" % (host, ip, rejected))
            continue
        answered += 1
        out("P3 SNTP %s (%s): %d accepted, offset %.3f ms, rtt %.3f ms, rejected %s"
            % (host, ip, accepted, offset * 1000.0, rtt * 1000.0, rejected))
    assert answered >= 1, "P3: no SNTP server answered"

    async def rtds():
        # recorder.py's rtds(), in effect: the same subscription message from config.TIER_A,
        # the same URL and the same connect arguments.
        subs = [{"topic": t, "type": "*", "filters": f}
                for t, (f, _s) in config.TIER_A.items()]
        message = json.dumps({"action": "subscribe", "subscriptions": subs})
        topics, frames = set(), 0
        async with websockets.connect(config.RTDS_URL, open_timeout=20,
                                      ping_interval=None, max_size=None) as ws:
            await ws.send(message)
            deadline = time.monotonic() + 30
            while time.monotonic() < deadline and topics != set(config.TIER_A):
                try:
                    raw = await asyncio.wait_for(ws.recv(),
                                                 timeout=max(0.1, deadline - time.monotonic()))
                except asyncio.TimeoutError:
                    break
                if isinstance(raw, bytes):
                    raw = raw.decode("utf-8", "replace")
                if not raw or raw.strip() in ("PONG", "PING"):
                    continue
                frames += 1
                try:
                    topic = json.loads(raw).get("topic")
                except Exception:
                    continue
                if topic in config.TIER_A:
                    topics.add(topic)
        return topics, frames

    topics, frames = asyncio.run(rtds())
    out("P4 %s: %d frames in at most 30 s, topics %s" % (config.RTDS_URL, frames, sorted(topics)))
    need = {"crypto_prices_twap_sixty", "crypto_prices_chainlink"}
    assert need <= topics, "P4: topics %r lack %r" % (sorted(topics), sorted(need - topics))
    out("G-PATH PASS: P0 to P4")


# ---- state, marks, the restart, G-REC, the end ----------------------------------------------

def mode_state():
    assert not os.path.exists(STATE), "state: %s exists" % STATE
    head = head_of(WT)
    assert head != OLD_SHA, "S6: the branch is at %s" % head
    rec_pid, rec_n = check_unit(REC_UNIT, REC_ARGV, REC_CWD, None)
    cb_pid, cb_n = check_unit(CB_UNIT, CB_ARGV, None, None)
    sole_recorder(rec_pid)
    sole_chainbook(cb_pid)
    out("S1 S2 both units active: recorder pid %d NRestarts %d, chain book pid %d NRestarts %d"
        % (rec_pid, rec_n, cb_pid, cb_n))
    starts, kinds, torn, newlines, terminated = scan_runtime(REC_RUNTIME, is_start)
    assert starts, "S3: %s holds no start record" % REC_RUNTIME
    records = sum(kinds.values())
    starts.sort(key=lambda r: r["recv_ns"])
    out("S3 %s: %d newlines, %d records %s, %d torn, ends with a newline %s"
        % (REC_RUNTIME, newlines, records, json.dumps(kinds, sort_keys=True), torn, terminated))
    out("S3 newest start %s" % json.dumps(starts[-1], sort_keys=True))
    assert starts[-1].get("sha") == OLD_SHA, "S3: the newest start names %r" % starts[-1]
    assert records <= EQUIV_RECORDS_MAX, "S3: %d records, above the %d the TZ is costed at" % (
        records, EQUIV_RECORDS_MAX)
    got = head_of(SVC)
    assert got == OLD_SHA, "S4: %s is at %s" % (SVC, got)
    files_equal(REC_CWD, OLD_FILES, "S4 the unit's tree")
    assert clean(SVC), "S4: %s has local changes" % SVC
    files_equal(OLD_DIR, OLD_FILES, "S5 the primary checkout")
    files_equal(NEW_DIR, NEW_FILES, "S6 the branch")
    for path in (REC_ARGV[0], CB_ARGV[0]):
        assert os.access(path, os.X_OK), "S7: %s is not executable" % path
        out("S7 %s executable" % path)
    memory(REC_UNIT)
    memory(CB_UNIT)
    meminfo()
    os.makedirs(SCRATCH, exist_ok=True)
    save_state({"branch_head": head, "state_ns": time.time_ns(), "rec_pid": rec_pid,
                "rec_restarts": rec_n, "cb_pid": cb_pid, "cb_restarts": cb_n,
                "records": records, "marks": {}})
    out("STATE PASS: S1 to S7, the branch at %s" % head)


def mode_mark(name):
    assert name in ("kill-rec", "revert"), "mark %r" % name
    state = load_state()
    assert name not in state["marks"], "mark %r already recorded" % name
    rp, cp = show(REC_UNIT), show(CB_UNIT)
    state["marks"][name] = {"ns": time.time_ns(), "rec_pid": int(rp.get("MainPID") or 0),
                            "rec_restarts": int(rp.get("NRestarts") or 0),
                            "cb_pid": int(cp.get("MainPID") or 0),
                            "cb_restarts": int(cp.get("NRestarts") or 0)}
    save_state(state)
    out("MARK %s %s (%s)" % (name, json.dumps(state["marks"][name], sort_keys=True),
                             utc(state["marks"][name]["ns"] / 1e9)))


def records_since(since_ns):
    def keep(r):
        if not isinstance(r, dict):
            return False
        if r.get("kind") in ("start", "halt"):
            return r.get("recv_ns", 0) >= since_ns
        return (r.get("kind") == "disconnect" and r.get("reason") == "startup"
                and r.get("detected_recv_ns", 0) >= since_ns)
    recs, _kinds, torn, _n, _t = scan_runtime(REC_RUNTIME, keep)
    starts = sorted((r for r in recs if r["kind"] == "start"), key=lambda r: r["recv_ns"])
    ups = sorted((r for r in recs if r["kind"] == "disconnect"),
                 key=lambda r: r["detected_recv_ns"])
    halts = [r for r in recs if r["kind"] == "halt"]
    for r in starts + ups + halts:
        out("R %s" % json.dumps(r, sort_keys=True))
    return starts, ups, halts, torn


def check_restart(label, mark, sha, restarts, gap_from_ns, gap_max_ns):
    """One start record since the mark, on `sha`; no halt; a MainPID other than the mark's;
    NRestarts `restarts` (None: recorded). With gap_from_ns, also one startup gap detected since
    the mark, which began no earlier than gap_from_ns and lasted at most gap_max_ns; without it,
    the gaps are printed and not asserted."""
    starts, ups, halts, torn = records_since(mark["ns"])
    assert len(starts) == 1, "%s: %d start records since the mark" % (label, len(starts))
    st = starts[0]
    assert st.get("sha") == sha, "%s: the start record names %r" % (label, st.get("sha"))
    if gap_from_ns is not None:
        assert len(ups) == 1, "%s: %d startup gaps since the mark" % (label, len(ups))
        up = ups[0]
        assert gap_from_ns <= up["start_recv_ns"] <= st["recv_ns"] \
            <= up["detected_recv_ns"] <= up["end_recv_ns"], "%s: gap %r, start %d, bound %d" % (
                label, up, st["recv_ns"], gap_from_ns)
        gap = up["end_recv_ns"] - up["start_recv_ns"]
        assert 0 <= gap <= gap_max_ns, "%s: the gap is %d ns" % (label, gap)
        gaps = "the gap %s to %s, %.3f s" % (utc(up["start_recv_ns"] / 1e9),
                                            utc(up["end_recv_ns"] / 1e9), gap / 1e9)
    else:
        gaps = "%d startup gaps since the mark, recorded" % len(ups)
    assert not halts, "%s: halt records %r" % (label, halts)
    pid, n = check_unit(REC_UNIT, REC_ARGV, REC_CWD, restarts)
    assert pid != mark["rec_pid"], "%s: the same pid %d" % (label, pid)
    out("%s: pid %d replaced by %d, NRestarts %d; the start %s on %s; %s; %d torn"
        % (label, mark["rec_pid"], pid, n, utc(st["recv_ns"] / 1e9), sha, gaps, torn))
    return pid, st


def mode_restart():
    state = load_state()
    mark, head = state["marks"]["kill-rec"], state["branch_head"]
    assert head_of(SVC) == head, "G-RESTART: %s is not at the branch" % SVC
    pid, st = check_restart("G-RESTART", mark, head, mark["rec_restarts"] + 1,
                            mark["ns"] - KILL_SLACK_NS, RESTART_GAP_NS)
    sole_recorder(pid)
    memory(REC_UNIT)
    state["restart"] = {"pid": pid, "start_ns": st["recv_ns"],
                        "restarts": mark["rec_restarts"] + 1}
    save_state(state)
    cb = show(CB_UNIT)
    out("G-RESTART the chain book, recorded and judged by G-CB-STILL: pid %s, NRestarts %s"
        % (cb.get("MainPID"), cb.get("NRestarts")))
    out("G-RESTART PASS: the recorder runs the new code as pid %d" % pid)


def written_ns(rec):
    """The instant a record reached runtime.jsonl: each kind is written when its stamp is taken."""
    if rec.get("kind") == "disconnect":
        return rec.get("end_recv_ns", 0)
    return rec.get("recv_ns", 0)


def manifest_path(t):
    return "%s/%d/manifest.json" % (REC_SERIES, t)


def mode_rec():
    state = load_state()
    r, head = state["restart"], state["branch_head"]
    r0 = r["start_ns"] / 1e9
    first = math.ceil((r0 + REC_LEAD_S + 90) / 300) * 300
    members = [first + 300 * k for k in range(REC_UNITS)]
    missing = [t for t in members if not os.path.exists(manifest_path(t))]
    if missing and time.time() < max(t + REC_DEADLINE_S for t in missing):
        not_yet(time.time() + 300, "intervals %s pending, the last deadline %s"
                % (missing, utc(max(t + REC_DEADLINE_S for t in missing))))
    # Every interval the new code closed before the members: recovered at its start, or open
    # across the restart. Its manifest was written at or after the new start record.
    earlier = []
    t = int(r0 - REC_BACK_S) - int(r0 - REC_BACK_S) % 300
    while t < first:
        path = manifest_path(t)
        if os.path.exists(path) and os.stat(path).st_mtime_ns >= r["start_ns"]:
            earlier.append(t)
        t += 300
    present_members = [t for t in members if t not in missing]
    compared = earlier + present_members
    REC_MEMBERS.update(compared)
    old = load_recorder(OLD_DIR, "recorder_old", OLD_FILES)
    o = instance(old, REC_RUNTIME, head)
    windows = [window_of(t) for t in compared]

    def selectable(rec):
        """Every record the old slice of a compared interval can select, a superset of it: a
        start, a clock sample inside a compared window, a disconnect overlapping one. The old
        code's own filter then picks from them, in file order, as it picks from the whole file."""
        if not isinstance(rec, dict):
            return False
        kind = rec.get("kind")
        if kind == "start":
            return True
        if kind == "clock":
            return any(lo <= rec.get("recv_ns", -1) <= hi for lo, hi in windows)
        if kind == "disconnect":
            return any(rec.get("start_recv_ns", hi + 1) <= hi and rec.get("end_recv_ns", -1) >= lo
                       for lo, hi in windows)
        return False
    every, _kinds, _torn, _n, _t = scan_runtime(REC_RUNTIME, selectable)

    def same_slice(t):
        """The stored slice against the old recorder's, over the records written by then."""
        stored_path = "%s/%d/runtime.jsonl" % (REC_SERIES, t)
        mtime_ns = os.stat(stored_path).st_mtime_ns
        o.runtime = [x for x in every if written_ns(x) <= mtime_ns]
        mine = slice_bytes(o, t, os.path.join(SCRATCH, "rec"))
        with open(stored_path, "rb") as fh:
            return mine == fh.read()

    equal = 0
    for t in earlier:
        with open(manifest_path(t), encoding="utf-8") as fh:
            m = json.loads(fh.read())
        assert m.get("T0_epoch") == t, "G-REC: %s carries T0_epoch %r" % (manifest_path(t),
                                                                         m.get("T0_epoch"))
        same = same_slice(t)
        equal += 1 if same else 0
        out("G-REC earlier interval %d %s: closed by the new code, complete %s, disconnects %s, "
            "sha %s, slice equal to the old recorder's %s" % (t, utc(t), m.get("complete"),
                                                               m.get("disconnect_count"),
                                                               m.get("recorder_git_sha"), same))
    present = complete = quotes = shas = 0
    for t in members:
        if t in missing:
            out("G-REC interval %d %s: no manifest by %s" % (t, utc(t), utc(t + REC_DEADLINE_S)))
            continue
        with open(manifest_path(t), encoding="utf-8") as fh:
            m = json.loads(fh.read())
        assert m.get("T0_epoch") == t, "G-REC: %s carries T0_epoch %r" % (manifest_path(t),
                                                                         m.get("T0_epoch"))
        present += 1
        complete += 1 if m.get("complete") is True else 0
        quotes += 1 if m.get("quotes_complete") is True else 0
        shas += 1 if m.get("recorder_git_sha") == head else 0
        same = same_slice(t)
        equal += 1 if same else 0
        out("G-REC interval %d %s: complete %s, quotes_complete %s, disconnects %s, sha %s, "
            "slice equal to the old recorder's %s" % (t, utc(t), m.get("complete"),
                                                       m.get("quotes_complete"),
                                                       m.get("disconnect_count"),
                                                       m.get("recorder_git_sha"), same))
    ok = (present == REC_UNITS and quotes == REC_UNITS and shas == REC_UNITS
          and complete >= REC_COMPLETE_MIN and equal == len(compared))
    out("G-REC %s: manifests %d of %d, quotes_complete %d of %d, sha %d of %d, complete %d of %d "
        "(PASS at %d or more), slices equal %d of %d compared (%d earlier, %d members)"
        % ("PASS" if ok else "FAIL", present, REC_UNITS, quotes, REC_UNITS, shas, REC_UNITS,
           complete, REC_UNITS, REC_COMPLETE_MIN, equal, len(compared), len(earlier), present))
    assert ok, "G-REC FAIL"


def mode_final():
    state = load_state()
    r, head = state["restart"], state["branch_head"]
    pid, _n = check_unit(REC_UNIT, REC_ARGV, REC_CWD, r["restarts"])
    assert pid == r["pid"], "G-FINAL: the recorder's pid moved to %d" % pid
    assert head_of(SVC) == head, "G-FINAL: %s is not at the branch" % SVC
    files_equal(REC_CWD, NEW_FILES, "G-FINAL the unit's tree")
    starts, _kinds, torn, newlines, _t = scan_runtime(REC_RUNTIME, is_start)
    starts.sort(key=lambda x: x["recv_ns"])
    assert starts[-1]["recv_ns"] == r["start_ns"] and starts[-1]["sha"] == head, \
        "G-FINAL: the newest start %r" % starts[-1]
    out("G-FINAL %s: %d newlines, %d torn, newest start %s on %s"
        % (REC_RUNTIME, newlines, torn, utc(r["start_ns"] / 1e9), head))
    sole_recorder(pid)
    memory(REC_UNIT)
    memory(CB_UNIT)
    meminfo()
    out("G-FINAL PASS: recorder pid %d on %s" % (pid, head))
    cb_pid, _n = check_unit(CB_UNIT, CB_ARGV, None, state["cb_restarts"])
    assert cb_pid == state["cb_pid"], "G-CB-STILL: the chain book's pid moved from %d to %d" % (
        state["cb_pid"], cb_pid)
    sole_chainbook(cb_pid)
    out("G-CB-STILL PASS: the chain book ran as pid %d, NRestarts %d, from state to the end"
        % (cb_pid, state["cb_restarts"]))


def mode_revert():
    state = load_state()
    mark = state["marks"]["revert"]
    got = head_of(SVC)
    assert got == OLD_SHA, "K-21: %s is at %s" % (SVC, got)
    files_equal(REC_CWD, OLD_FILES, "K-21 the unit's tree")
    assert clean(SVC), "K-21: %s has local changes" % SVC
    # An explicit restart is not one of systemd's own, and a revert must not stop on the venue's
    # socket, so NRestarts and the startup gaps are recorded, not asserted.
    pid, _st = check_restart("K-21", mark, OLD_SHA, None, None, None)
    sole_recorder(pid)
    memory(REC_UNIT)
    out("REVERT PASS: the recorder runs 4216c04 again as pid %d" % pid)


# ---- section 9 ------------------------------------------------------------------------------

TOKEN = re.compile(r"(?<![0-9a-f])[0-9a-f]{16,64}(?![0-9a-f])")


def report_tokens():
    """Every run of 16 to 64 lowercase hex characters in a report under CryptoReports/."""
    tokens = set()
    for name in sorted(os.listdir(REPORTS)):
        if name.endswith(".md"):
            tokens.update(TOKEN.findall(read_text(os.path.join(REPORTS, name))))
    return tokens


def reclaimable(tree):
    """This TZ's tree, or an earlier session's directory beside this session's under /tmp."""
    if tree == WORK:
        return True
    return (tree.startswith("/tmp/") and os.path.isdir(tree) and not os.path.islink(tree)
            and UUID.fullmatch(os.path.basename(tree)) is not None
            and "btc-5m-twap" in os.path.basename(os.path.dirname(tree)))


def by_name(tree, rel):
    return tree == WORK and (rel == "state.json" or rel.startswith("logs/"))


def pristine(tree):
    """A worktree holding exactly its HEAD's tracked files, with HEAD on its upstream: git keeps
    every byte of it, so nothing in it is copied and `git worktree remove` needs no --force."""
    cp = subprocess.run(["git", "-C", tree, "status", "--porcelain", "--ignored"],
                        capture_output=True, text=True)
    assert cp.returncode == 0 and cp.stdout == "", "reclaim: %s holds %r" % (tree, cp.stdout[:400])
    head = head_of(tree)
    up = subprocess.run(["git", "-C", tree, "rev-parse", "@{u}"], capture_output=True, text=True)
    assert up.returncode == 0 and up.stdout.strip() == head, \
        "reclaim: %s is at %s, its upstream at %r" % (tree, head, up.stdout.strip())
    out("reclaim: %s skipped: no file but its HEAD's, and HEAD %s is its upstream's" % (tree, head))


def mode_reclaim(trees):
    assert trees and all(reclaimable(t) for t in trees), "reclaim: %r" % (trees,)
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
                dest = os.path.join(FORENSICS, os.path.basename(tree) + "--"
                                    + rel.replace("/", "--"))
                if os.path.exists(dest):
                    got = sha256_file(dest)
                    assert got == h, "reclaim: %s exists with sha256 %s, source %s" % (dest, got,
                                                                                       h)
                    held += 1
                    out("R held   %s %s" % (h, dest))
                    continue
                with open(path, "rb") as src, open(dest, "xb") as dst:
                    for chunk in iter(lambda: src.read(1 << 20), b""):
                        dst.write(chunk)
                assert sha256_file(dest) == h, "reclaim: %s did not copy whole" % dest
                copied += 1
                out("R copied %s %s" % (h, dest))
    after = sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    assert after == before + copied, "reclaim: store %d, expected %d" % (after, before + copied)
    out("RECLAIM PASS: %d files considered, %d named by a report, %d kept by name, %d copied, "
        "%d already held; forensic store %d -> %d files" % (considered, named, kept, copied, held,
                                                           before, after))


def main(argv):
    if not argv:
        sys.exit("usage: tz21-recorder-memory.py MODE [ARG...]")
    mode, rest = argv[0], argv[1:]
    table = {"state": mode_state, "synth": mode_synth, "equiv": mode_equiv, "path": mode_path,
             "restart": mode_restart, "rec": mode_rec, "final": mode_final,
             "revert": mode_revert}
    if mode == "mark":
        assert len(rest) == 1, "mark NAME"
        mode_mark(rest[0])
    elif mode == "reclaim":
        mode_reclaim(rest)
    else:
        assert mode in table and not rest, "unknown mode %r" % (argv,)
        table[mode]()
    out("peak memory of this run: %d bytes" % (
        resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024))
    out("opens under the capture roots: %d" % len(OPENS))


if __name__ == "__main__":
    main(sys.argv[1:])
```
