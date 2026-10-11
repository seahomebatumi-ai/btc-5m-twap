# TZ-28 — the pair book's archive on a timer: TZ-27's steps, once a day, unattended

**Canonical filename:** `TZ-28-pairbook-archive-timer.md`. The committed file takes this name and no other.

**Executor model: Opus.** A unit that moves capture off the host, restarts the pair book and holds a credential is
deployed, and its first run is proved.

**Required System Map revision:** `2026-10-11-b`.

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

**When:** after the upload that carries this TZ and revision `2026-10-11-b`, and **started before 2026-10-13 18:00
UTC**: at TZ-26's modelled weekday rate the pair book's streams reach the cap about 2026-10-14 12:42 UTC (map §6,
headroom), and the first run must have moved them first. About three hours of wall clock (§6), most of it waiting
for the first run. **The Boss is needed at the VPS while it runs:** B-PATH-TOKEN is his block, and every block the
session's classifier refuses becomes his (§3).

**What this TZ is.** TZ-27 moved the pair book's closed windows' stream files to a Release by hand, in a session, with
the Boss's upload. The store refills at `1.3` to `2.5` GB a day, and the unit's count of it resets only at a restart
(map §2.5, §7 item 106). **This TZ deploys a systemd timer that does TZ-27's work unattended once a day** — the set as
of the run's start, each file uploaded to that run's own Release, each proved by the Release's digest and a full
anonymous download, each hashed again and removed, the unit restarted inside its band and its next window read —
through TZ-27's own functions, which its instrument loads byte for byte; **with every request held to the pair book's
idle stretch**, which TZ-27's were not (map §7 item 109). It proves the deployment on the timer's own first run, fired
600 s after the timer starts, and measures nothing (CANON hard rule 11). One instrument,
`research/tz28-pairbook-archive-timer.py`, and two units, `deploy/systemd/btc-pairbook-archive.service` and
`deploy/systemd/btc-pairbook-archive.timer`: Appendix A.

---

## 0. Gates

### 0.0 The work tree, first

After contract §1 steps 1 and 2, and before anything else:

```
mkdir /root/tz28-work /root/tz28-work/logs; echo "exit=$?"
```

`exit=0` proves neither existed; anything else is BLOCKED. **From here every command's output goes to
`/root/tz28-work/logs/`, one file per step, §0's included**, and nothing to the session's scratchpad. The one
exception is B-RECLAIM-OWN, §9.

### 0.1 The instrument, staged

Extract Appendix A from this TZ as the primary checkout carries it after contract §1's pull, with this script,
verbatim, its one argument the destination:

```
/root/tz04a-env/venv/bin/python -B - /root/tz28-work/stage <<'EOF'
import hashlib, os, sys
SRC = "/root/btc-5m-twap/CryptoTZ/TZ-28-pairbook-archive-timer.md"
DEST = sys.argv[1]
WANT = {
    "research/tz28-pairbook-archive-timer.py": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4",
    "deploy/systemd/btc-pairbook-archive.service": "2e7fd45382af3da3b2ec29ced8d69870ef3d4481da4c6f327b90fc6cb5af78e7",
    "deploy/systemd/btc-pairbook-archive.timer": "07581f4f331fbf9d2a1113cac42a2872d65ac69a872991bff7d2bda235eac913",
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
| `research/tz28-pairbook-archive-timer.py` | 1,438 | 74,576 | `46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4` |
| `deploy/systemd/btc-pairbook-archive.service` | 17 | 794 | `2e7fd45382af3da3b2ec29ced8d69870ef3d4481da4c6f327b90fc6cb5af78e7` |
| `deploy/systemd/btc-pairbook-archive.timer` | 13 | 417 | `07581f4f331fbf9d2a1113cac42a2872d65ac69a872991bff7d2bda235eac913` |

Then the instrument's one dependency beside it, TZ-27's file as `main` carries it:

```
install -m 0644 /root/btc-5m-twap/research/tz27-pairbook-archive.py /root/tz28-work/stage/research/; echo "exit=$?"
sha256sum /root/tz28-work/stage/research/tz27-pairbook-archive.py
```

which must print `2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673` — map §0's row; the instrument
asserts it again each time it loads the file (Appendix A lines 63 to 73). A failed assert or another hash is
BLOCKED. The staged copy runs two modes only, §0.2's `fingerprint` and §0.6's `tz27-release`, and is written
**`I0`**: `nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz28-work/stage/research/tz28-pairbook-archive-timer.py`,
run from `/root/tz28-work` — every mode but `run` asserts that its current directory is a work tree
`/root/tzNN-work` (Appendix A line 1409).

### 0.2 Fingerprint

`I0 fingerprint` performs contract §1 steps 3 and 4 inside the instrument and asserts them, against `SYSTEM-MAP.md`
and the files of its §0 table in the primary checkout `/root/btc-5m-twap`: revision `2026-10-11-b`; the six anchors;
`A2`, `A4`, `A5` and `A6` re-derived as the first 12 hex characters of those files' SHA-256; the table's **37** rows,
each printed in lines, bytes and SHA-256 — **34** `frozen` rows asserted equal to the map, **2** `tracked` and **1**
`reported`; and the map's own lines, bytes and SHA-256 (lines 693 to 722). It prints `FINGERPRINT PASS` or stops at
the first mismatch, which is BLOCKED. **TZ-27's own `fingerprint` cannot read this revision** — it holds
`2026-10-11-a` and 33 `frozen` rows as constants (`research/tz27-pairbook-archive.py` lines 69 and 75) — so it is
never run.

### 0.3 Host gate

From `/root/btc-5m-twap`, with `S` first set to the scratchpad directory the session's system prompt names, output
verbatim into `logs/03-host-gate.log`:

```
date -u; date -u +%s
nproc; grep -E '^(MemTotal|MemAvailable|SwapTotal|SwapFree):' /proc/meminfo
systemctl --version | head -n 1
df -B1 --output=source,size,avail /var/lib/btc-recorder
find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
grep -c e3975b5da44c5328adf3bf3914634cd878842c73 /var/lib/btc-recorder/runtime.jsonl
systemctl is-active btc-pairbook.service; echo "exit=$?"
systemctl is-enabled btc-pairbook.service; echo "exit=$?"
cmp /root/btc-5m-twap/deploy/systemd/btc-pairbook.service /etc/systemd/system/btc-pairbook.service; echo "cmp exit=$?"
cat /root/btc-pairbook-svc/commit.txt
sha256sum /root/btc-pairbook-svc/tz26-nesting-b3-capture.py
systemctl show btc-pairbook.service -p MainPID -p NRestarts
/root/tz04a-env/venv/bin/python -c 'import sys; print(sys.version.split()[0])'
systemctl is-active btc-recorder.service btc-chainbook.service; echo "exit=$?"
systemctl is-enabled btc-recorder.service btc-chainbook.service; echo "exit=$?"
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
systemctl is-active telemetry-watch.service; echo "exit=$?"
git -C /root/btc-recorder-svc rev-parse HEAD
for d in /root/btc-pairbook-archive-svc /var/lib/btc-pairbook-archive /etc/systemd/system/btc-pairbook-archive.service /etc/systemd/system/btc-pairbook-archive.timer; do test -e "$d"; echo "$d exit=$?"; done
for d in /root/tz27-work /root/tz18a-svc /root/btc-recorder-svc /root/btc-pairbook-svc; do test -e "$d"; echo "$d exit=$?"; done
sha256sum /root/btc-forensics/tz27-work--archive--set.json
find /root/btc-forensics -type f | wc -l
git worktree list
du -sb /var/lib/btc-pairbook /root/.claude /root/PROJECT_GAMING_PS5
echo "$S"; ls -la "$(dirname "$(dirname "$S")")"
```

- **H1** — `find` prints exactly one path.
- **H2** — `df` names source `/dev/vda2` and size `31612203008`; `grep -c` prints at least `1`. With H1 this is map
  §6's host identity.
- **H3** — the pair book as TZ-27 left it: `active` and `exit=0`; `enabled` and `exit=0`; `cmp exit=0`;
  `commit.txt` prints `e8b46a85d61e1a17841962846f6d3012046c2d70`; `sha256sum` prints
  `caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec`. The archive's run restarts that unit and reads
  its records, so this TZ's work needs this state.
- **H4** — the interpreter prints `3.12.`.
- **H5** — the archive is not installed: each of the first `for` line's four paths prints `exit=1`; and TZ-27's set is
  in the forensic store: `sha256sum` prints `ec71b1a7ce7db37ff29a49156006541dd5729c1df2c829c481eb64181228e4dd`.
- **Memory gate** — `MemAvailable` at least `106,086,400` bytes (§0.4).
- **Disk gate** — `avail` at least `2,300,000,000` bytes (§0.4).

Any of these seven failing is BLOCKED. **The rest is printed and carries no threshold:** systemd's version; the pair
book's `MainPID` and `NRestarts`, which map §6 puts at `815823` and `2`; the recorder's and the chain book's states,
`active` and `enabled`, and `inactive` and `disabled`, of which G-STILL reads the recorder's from §3.3;
`telemetry-watch.service`'s two states, on which map §6's headroom is conditional; the recorder's tree, `e3975b5…`;
`/root/tz27-work` absent and the three code trees present, by map §3; the forensic store's count, map §3's `1,810`;
the worktrees, map §3's two; `du` of the store beside `df`, as map §2.5 asks; and the listing of the directory that
holds the session's own, whose UUID directories `I scratch` names live or earlier (§9).

### 0.4 Resource floors, in exact bytes

**Disk.** `/dev/vda2` free at least **`2,300,000,000`** bytes, TZ-27's floor: the pair book's `RESOURCE_FLOOR`,
`2,200,000,000` (`research/tz26-nesting-b3-capture.py` line 131), below which it halts with exit `1`, which its unit
does not restart, plus `100,000,000` for this session — the worktree, `6,270,784` bytes of tracked files at `2c1fcd0`
before this upload; the logs under `2,000,000`; the service's code, `74,576 + 106,284 + 41` bytes; and the first
run's records under `1,000,000` (map §6, disk). **No copy of a stream file is written:** the run hashes, sends and
downloads each in pieces (`research/tz27-pairbook-archive.py` lines 293 to 304, 618 to 636 and 641 to 653). **The
run's own floor is `2,001,000,000`** (Appendix A line 106): the recorder's floor, `2,000,000,000` — `4,500,000,000`,
the stream floor, less the `2,500,000,000` map §6 puts between them — plus the `1,000,000` bytes a run writes at most.
Below it a run defers, having written its start record alone.

**Memory.** `MemAvailable` at least **`106,086,400`** bytes: twice the largest peak of the archive's run in the
Architect's six runs under Python 3.12.3 — `53,043,200` bytes over 400 stream files and `2,190,000,000` bytes against
a loopback server in another process (map §6, memory). It is the run's own floor too (Appendix A line 107; checked at
lines 407 to 411), because the first run happens inside this session. The session's modes peak lower — `selftest`
`43,257,856` at the largest of six runs, `fingerprint` `35,971,072` — and `path`, `path-token` and `tz27-release`
re-read `MemAvailable` at their start and stop BLOCKED below TZ-27's floor, `93,454,336`, twice `selftest`'s
`46,727,168` of TZ-27 and above twice this file's `43,257,856` (`research/tz27-pairbook-archive.py` lines 125 and 324
to 328). The unit's ceiling, `MemoryMax=128M`, is `134,217,728` bytes, `2.53` times the run's largest peak. Map §6
records the host: `1,002,127,360` bytes in all, one processor; TZ-27 read `252,850,176` to `313,114,624` available
with its session open. Every session mode runs under `nice -n 19`, and the unit under `Nice=19`.

### 0.5 Refs

`git ls-remote origin` before §3.1's push, every ref reported. Map §1 records `main` at
`2c1fcd0e99112890de4a1f733dd3d6dfb7031cd0`, PR #26's merge, five branches, two tags and **36** ref lines. The upload
that carries revision `2026-10-11-b` and this TZ sits above `2c1fcd0`, in one commit or more; every commit on
`main`'s first-parent line above it is reported with the paths it changed. A difference is recorded, not BLOCKING,
unless `main` does not carry revision `2026-10-11-b`, or `refs/heads/tz-28-pairbook-archive-timer` or any
`refs/tags/pairbook-streams-*` already exists — each is BLOCKED.

### 0.6 TZ-27's Release — G-TZ27, a BLOCK condition

The Architect's session could not read the API's record of TZ-27's Release (map §4, CANON hard rule 13). `I0
tz27-release` reads it from the host, with no token, through `api.github.com` — the Release on
`tz-27-pairbook-streams` and one page of its assets, **2 requests** — against `/root/btc-forensics/tz27-work--archive--set.json`,
asserted `16,570` bytes and `ec71b1a7…`: the Release id `409534533`, published on the tag; its 51 assets exactly the
set's, none missing and none beyond; each `uploaded`, with the set's bytes, the `digest` `sha256:` with the set's
SHA-256 and the expected download URL (Appendix A lines 725 to 748). **It must print `G-TZ27 PASS`; anything else is
BLOCKED**, with nothing built: a Release that does not hold TZ-27's files is not the archive this TZ continues.

---

## 1. Why this TZ exists, and what the timer does

Line numbers in this section are Appendix A's unless a file is named. `tz27` is `research/tz27-pairbook-archive.py`
at `2c1fcd0`; a service line is `research/tz26-nesting-b3-capture.py`'s.

**The deadline.** TZ-27 restarted the pair book at 08:37:11 UTC on 2026-10-11 with `10,095,699` bytes in its count of
stream files (map §2.5). No stream opens once that count reaches `8,000,000,000`, `STREAM_CAP`, or free space falls
below `4,500,000,000`, `STREAM_FLOOR` (service lines 132, 133 and 809 to 817), and the count falls only at a restart.
At the Saturday rate TZ-27 measured, `1,277,627,302` bytes a day, that is 2026-10-17; at TZ-26's modelled `2.52` GB a
day on weekdays it is about **2026-10-14 12:42 UTC** [modelled] (map §6, headroom) — before M0's second look, and so
before B3's measurement. A manual archive every two to four days is eight or more sessions and B-UPLOADs before B3
reads anything. **The archive runs itself.**

**What a run does — TZ-27's work, through TZ-27's functions** (`run`, lines 608 to 669). The instrument loads `tz27`
from beside itself, executed from the bytes whose SHA-256 it asserts (lines 63 to 76), so the set rule, the proofs and
the readings exist once, in `tz27`, and are not written again here.

1. **Resume or begin.** A run whose ledger holds a run without a terminal record — `complete`, `empty` or `halt` —
   resumes it, with its set; otherwise it begins a new one as of `A`, its own start second, at least one second after
   every earlier run's (lines 619 to 626, `pending` lines 229 to 235).
2. **The set:** `tz27.inventory(ROOT, A)` (tz27 lines 430 to 460) — every stream file of every window whose
   `window.json` exists and was due at least 60 s before `A`, at most 400, oldest first, each hashed with its size
   and time unchanged — under TZ-27's tag rule's complement: **one Release a run, on the tag `pairbook-streams-<A>`**,
   which `tz27.TAG_RE` does not cover, so no TZ-27 mode can act on it (lines 357 to 377). A set with no file records
   `empty` and ends (lines 423 to 425).
3. **Upload:** the credential `tz27.credential()` reads from the primary checkout's remote URL (tz27 lines 725 to
   739); the Release on the tag, created at the commit the run's code is from — `target_commitish`, `commit.txt`'s —
   published and never the latest (lines 306 to 309 and 346 to 352), or resumed; then `tz27.upload_set` (tz27 lines
   765 to 812): each asset sent whole and hashed as sent, one kept where it already matches, 1 s between writes.
4. **Verify,** 120 s after the upload's completion record: `tz27.verify_release` and `tz27.release_reading` (tz27
   lines 685 to 709) with no token — every asset `uploaded` with the set's bytes and `digest`, then every asset
   downloaded whole and hashed (lines 479 to 508).
5. **Delete:** `tz27.delete_set` (tz27 lines 815 to 846), each file hashed again immediately before its removal and
   logged at once, then `tz27.removed_reading` (lines 511 to 529).
6. **Restart:** inside seconds 15 to 470 of a window — `band_wait` (lines 153 to 161) — the pair book's `MainPID`,
   `NRestarts` and `ActiveState` taken as the mark, `systemctl kill --signal=SIGTERM btc-pairbook.service`, then
   `tz27.restart_reading`, `tz27.counter_reading` and `tz27.unit_reads` at the mark's `NRestarts` plus 1 (lines 532
   to 568) — TZ-27's G-RESTART, G-COUNTER and G-UNIT, the same reasoning about the band as TZ-27 §1.
7. **Resume:** `tz27.resume_decision` on the restart's window, from its `window.json` (lines 571 to 581): TZ-27's
   G-RESUME.
8. **Complete:** the run's requests read against the idle stretch, the store's count and the projection
   `tz27.projection` prints, recorded (lines 584 to 596).

Each step under **TZ-27's own §2**: before each, the run sets `tz27.MODE` to the TZ-27 mode that did that step —
`inventory`, `upload`, `verify`, `delete`, `restart`, `resume`, `final` — so TZ-27's audit hook, installed when `tz27`
is loaded (tz27 line 275), refuses what TZ-27 §2 refused it; `tz27.WORK` is the archive's state directory, so the
hook refuses every write outside it (tz27 lines 214 to 259). Each step writes a record to
`/var/lib/btc-pairbook-archive/ledger.jsonl`, and each run's set, upload, verify, delete and request records go under
`runs/<A>/` there, every one asserted against TZ-27's forbidden keys (lines 212 to 220 and 242 to 245).

**The idle stretch — every request.** TZ-27's upload ran at seconds 569 to 642 of window `1791706500` and its verify at
766 to 814, across that window's stream, which streamed in two segments (map §7 item 109). The pair book streams from
`T+595` to `T+905` and writes `window.json` at `T+910` (service lines 114, 115 and 117); between `T+910` and
`T'+595` it fetches the next window's two documents from `T'+545` and nothing else (service line 110). **Every request
the run makes** — API, upload or download — goes through `Gh28`, TZ-27's `GitHub` with one change: before it starts,
`idle_wait` holds it until a second of the window from 15 to `590 − budget`, its budget `5 + ⌈bytes / 2,000,000⌉`
seconds, so at `2,000,000` bytes a second or faster it ends by second 590 (lines 99 to 101, 135 to 150 and 312 to
352); and each is timed into `runs/<A>/transfers.jsonl`. `2,000,000` bytes a second is under a quarter of the slower of
the host's two measured rates, `9,297,801` up and `14,140,406` down (map §6, GitHub Releases); the largest stream file
the service writes, a cut window at `100,000,000` stored bytes and one flush, is budgeted under 60 s, and a file above
`1,140,000,000` bytes, which no idle stretch carries, stops the set (lines 113, 366 and 367). Every header of every
request is `tz27.build_request`'s (tz27 lines 509 to 519), `User-Agent: btc-5m-twap-tz27`.

**When a run fails.** Before any removal — the set, the upload, the verify — a failure **defers** the run: exit `75`,
nothing removed, a `deferred` record, and the next run resumes the same set, its upload keeping every matching asset
and its verify reading every asset again (lines 659 to 669). **The third deferral of one set halts the archive.** From
the removal on, any failure **halts** it, and so does a refusal by TZ-27's hook at any step: a `halt` record, and the
run disables its own timer — `systemctl disable --now btc-pairbook-archive.timer`, K-28 — recording its exit (lines
599 to 605). A halted archive refuses every later run until a TZ appends a `clear` record (lines 223 to 226 and 612
to 618). **The run never stops or starts the pair book:** a pair book not `active` at the restart halts the archive
with the files already archived (line 536), and what happens to the capture is a TZ's decision.

**The timer.** `OnCalendar=*-*-* 03:00:20 UTC` — second 20 of its window, inside the idle stretch — and
`OnActiveSec=600`, so the first run fires 600 s after the timer starts, at B-ENABLE and at every boot; `AccuracySec=1s`.
The service: `Type=oneshot`, `Restart=no` — no exit is retried by systemd, because the next day's run resumes what
this one left — `TimeoutStartSec=21600`, `Nice=19`, `MemoryMax=128M`, output appended to
`/var/lib/btc-pairbook-archive/archive.log`, no `[Install]`: the timer starts it (Appendix A's two units). Its exits:
`0` complete or empty, `75` deferred, `1` halted or an assert before the run began, `2` another run holds the lock
(lines 95, 96 and 672 to 688). A run checks that systemd started it — `INVOCATION_ID` set, its directory and file the
unit's (lines 673 to 676). **6 h** bounds the slowest run this TZ allows (§6).

**The credential.** The run reads the token from the primary checkout's remote URL, as TZ-27's B-UPLOAD did, through
`tz27.credential`, and prints only its source; it sends the token to `api.github.com` and `uploads.github.com` alone
and follows no redirect with it (tz27 lines 498 to 506 and 712 to 739). A unit is not the session, so the classifier
that refuses the session's token (map §6; contract §5.1) does not bind it. **The Executor never reads, prints or
stores the credential:** B-PATH-TOKEN, the Boss's block, is this session's only process that reads it.

**The reserve stands** (CANON PART II, B3; map §2.5): no run decompresses a stream file or extracts anything from one,
and each Release's body says its assets are reserved for B3's measurement (lines 380 to 389). `window.json` and
`runtime.jsonl` are the reserve's exceptions, as in TZ-26 and TZ-27.

**Discarded:** a manual archive every two to four days — eight or more sessions and B-UPLOADs before B3 can read; a
long-lived service with its own daily loop — a process alive all day for a minutes' task, and a sleep loop in place of
the scheduler systemd already has; one Release for every run — up to 1,000 assets a Release (map §6), filled in about
ten days; importing nothing from TZ-27 and re-implementing its steps — a second implementation of the archive's proofs,
which CANON PART III forbids.

**What this TZ decides.**

1. **The instrument and the two units**, on the branch `tz-28-pairbook-archive-timer`; `main` carries them once the
   Boss merges after the verdict.
2. **The deployment:** the service's code in `/root/btc-pairbook-archive-svc/`, its state directory
   `/var/lib/btc-pairbook-archive/`, and the two units under `/etc/systemd/system/`, by B-INSTALL; the timer enabled
   by B-ENABLE.
3. **The proof:** the timer's first run, fired 600 s after B-ENABLE, read back by `first` — and every gate of §4.
4. **The stops:** K-28, and on a G-UNIT FAIL TZ-26's K-26 and B-RESTORE-CB (§4.8).
5. **Nothing else on the host is touched** but the paths of §2.

---

## 2. Scope

**Repository paths and refs this TZ may write, and no others:**

1. `research/tz28-pairbook-archive-timer.py`, `deploy/systemd/btc-pairbook-archive.service` and
   `deploy/systemd/btc-pairbook-archive.timer` — new, byte for byte Appendix A's, on branch
   `tz-28-pairbook-archive-timer`, then a pull request. Not merged by the Executor.
2. `CryptoReports/TZ-28-pairbook-archive-timer-report.md` — straight to `main`, in one commit. **The one path pushed
   to `main`.**
3. **The first run's Release, on its lightweight tag `pairbook-streams-<A>`, holding exactly that run's set**, written
   by the unit alone, under the credential the unit reads — **the exemption to prohibited item 10**. A Release or tag
   a run wrote stays; none is deleted (contract §3.3).

**Host paths this TZ may write:** `/root/tz28-work/**`; `/root/btc-forensics/`, by exclusive create only (§9); in the
primary checkout `/root/btc-5m-twap`, its `.git` for the branch and the worktree and its `CryptoReports/` for the
report; and, by B-INSTALL alone, `/root/btc-pairbook-archive-svc/` — the instrument, TZ-27's file and `commit.txt` —
the empty directory `/var/lib/btc-pairbook-archive/`, and the two unit files under `/etc/systemd/system/`. **The unit
writes**, and only under `/var/lib/btc-pairbook-archive/`: its ledger, `runs/<A>/`, `run.lock` and `archive.log` —
**the named exemption to prohibited item 3**. **Host paths removed, and nothing else:** **the first run's set's
stream files under `/var/lib/btc-pairbook/<T>/`, by the unit's run alone, each proved first (§1) — the named exemption
to prohibited item 3: the capture is moved, never reclaimed**; `/root/tz28-work/` with its worktree, and the
directories `I scratch` names earlier (§9).

**Prohibited, each absolutely:**

1. No committed file is modified; every `frozen` row of map §0 is byte-identical at run end.
2. **Under `/var/lib/btc-recorder/` nothing is opened, listed or written**; only §0.3's `df`, `find` and `grep -c`, at
   both of its runs, touch the root. TZ-27's audit hook refuses every open and listing there, in every mode of this
   instrument and in the run.
3. **Under `/var/lib/btc-pairbook/` nothing is written but by the pair book's unit, and nothing removed but the first
   run's set's stream files, by the archive's run.** In the session, `first` reads `runtime.jsonl` and the `window.json`
   of the restart's window or the next, and lists directory entries; `started` reads `runtime.jsonl`; `final` lists
   them; nothing else of the store is opened by a session mode. Outside the instrument, only `du -sb` at §0.3 and §3.10,
   §3.10's `tail` of `service.log`, and §4.8's `tail` of `runtime.jsonl` on a G-UNIT FAIL. **No file is decompressed,
   and no price, size, side, book hash or outcome is extracted from a stored body or from a Release asset** (§1, the
   reserve). Under `/var/lib/btc-pairbook-archive/` the session reads and writes nothing but by the instrument's reads,
   §3.10's `tail` and `du`, §4.8's `tail` of the ledger, and B-INSTALL's creation of the directory.
4. **Under `/var/lib/btc-chainbook/` nothing is opened, listed or written.** **Exempt:** what the chain book's own
   process writes there if B-RESTORE-CB starts it on a G-UNIT FAIL (§4.8).
5. **No unit is created, started, stopped, enabled, disabled, signalled or changed but by B-INSTALL, B-ENABLE,
   B-RETRY, the archive's run — its daily restart of the pair book and, on a halt, K-28 — and on a FAIL K-28, K-26
   and B-RESTORE-CB (§4.8); and B-START-SVC where the pair book is down after the run.** `systemctl show`,
   `is-active`, `is-enabled`, `list-timers`, `systemd-analyze verify`, `daemon-reload` and `journalctl -u` are this
   TZ's only other reads and acts on a unit. The recorder is never signalled.
6. `/root/tz04a-env/`, `/root/tz01-env/`, `/root/tz18a-svc/`, `/root/btc-recorder-svc/` and `/root/btc-pairbook-svc/`
   are not modified, and `/root/btc-forensics/` only by §9's exclusive create.
7. Nothing is pushed to `main` except the report of item 2.
8. **Requests:** `tz27-release`'s, `path`'s and `first`'s anonymous reads of `api.github.com` and the downloads of
   `path` through `github.com`'s redirect; B-PATH-TOKEN's two reads of `api.github.com` under the credential; the
   unit's run, as §1 says; the self-test's, to `127.0.0.1` alone; `git` against `origin`; and `gh` for the pull
   request. No other request, and **none to a venue host** — the pair book's own are the pair book's.
9. **The Executor never reads, prints or stores the credential.** Only `path-token`, run by the Boss, and the unit's
   run read it, through `tz27.credential` (tz27 lines 725 to 739), and no message names it; no step prints
   `git remote -v`, `git remote get-url` or `gh auth token`.
10. **No price, size, side, book hash or outcome of any market is printed or written** outside the capture's own
    store, a Release's assets — its files, byte for byte — and §9's copies; downloads are hashed as they arrive and
    written nowhere. Every record the run and the instrument write is asserted against TZ-27's forbidden keys
    (`research/tz27-pairbook-archive.py` lines 151 to 154 and 331 to 345). No other Release is created or changed,
    `tz-01a-dataset`'s and `tz-27-pairbook-streams`'s are only read, and no dataset, archive or binary enters git
    history.

---

## 3. The work, in this order

From §3.1 on, `nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz28-work/wt/research/tz28-pairbook-archive-timer.py`
is written **`I`**; a mode is `I <mode>`, run from `/root/tz28-work`. Every command's output goes to `logs/`, one file
per step, and is quoted in the report. **§9's B-RECLAIM-SCRATCH runs after §3.3 and before §3.4; B-RECLAIM-OWN runs
last, after §3.10.** On a BLOCK before §3.1, B-RECLAIM-OWN runs with `I0` in place of `I` and without its `git
worktree remove` line; on a BLOCK or a FAIL after it, the run goes to §3.10 and §9, skipping every step that needs a
PASS it lacks.

**Where the session's permission classifier refuses a command of a block named B-… or K-…**, the Executor prints the
block, the Boss runs it verbatim in a root shell on the VPS, and the Executor verifies it through the reads this TZ
names — never from the Boss's account. **Every `mark` is the Executor's**, taken before its block is run or handed
over. **B-PATH-TOKEN is the Boss's from the start** (§3.5). **A block timed to a band waits for that band in its own
text**, so whoever runs it cannot run it outside the band.

### 3.1 The branch and its files

```
git -C /root/btc-5m-twap fetch origin
git -C /root/btc-5m-twap worktree add -b tz-28-pairbook-archive-timer /root/tz28-work/wt origin/main
```

Then §0.1's script again, verbatim but for its argument, `/root/tz28-work/wt`; it must print the same three lines as at
§0.1. Commit those three files alone on the branch, push it with `git push -u origin tz-28-pairbook-archive-timer`
from the worktree, and open the pull request against `main`. A failed assert here is BLOCKED.

### 3.2 The self-test

`I selftest` must print `34 of 34 checks passed`. It reaches `127.0.0.1` alone, and runs the archive whole on
temporary stores under `/root/tz28-work/selftest-tmp/`, a simulated pair book and a loopback server — a complete run;
an empty one; a refused credential deferred and resumed; three deferrals halting the archive and a halt refusing the
next run until a clear; a flipped bit in one asset deferring before any removal; a G-COUNTER FAIL after the removal
halting it; a pair book not running left alone — and removes them (lines 1129 to 1397). A red self-test stops the run
here, and it goes to §3.10 and §9.

### 3.3 The units, and the directories beside this session

`I still` records the recorder's `MainPID`, `NRestarts` and `ActiveState` in `state.json` and prints the three capture
units' state and memory — TZ-27's `still` (tz27 lines 1041 to 1062). Then `I scratch "$(dirname "$S")"` lists every
UUID directory beside this session's own and names each **live** or **earlier** — TZ-27's `scratch` (tz27 lines 1453
to 1464).

### 3.4 The token-free path — P-PATH

`I path` must print `READING P-PATH: served` (§4.1). It waits for the idle stretch, at most `900` s. **A failed assert
is BLOCKED, and nothing is installed.**

### 3.5 The path with the token — B-PATH-TOKEN

The Executor hands the Boss **B-PATH-TOKEN**, which he runs verbatim in a bash root shell on the VPS:

```
cd /root/tz28-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz28-work/wt/research/tz28-pairbook-archive-timer.py path-token 2>&1 | tee -a /root/tz28-work/logs/B-PATH-TOKEN.log; echo "exit=${PIPESTATUS[0]}"
```

It must print `READING P-TOKEN: served` and `exit=0` (§4.2). **Anything else is BLOCKED** (contract §5.3), with
nothing installed. The Executor reads `logs/B-PATH-TOKEN.log` from the session.

### 3.6 The installation — B-INSTALL, then G-INSTALL

```
install -d -m 0755 /root/btc-pairbook-archive-svc; echo "exit=$?"
install -m 0644 /root/tz28-work/wt/research/tz28-pairbook-archive-timer.py /root/tz28-work/wt/research/tz27-pairbook-archive.py /root/btc-pairbook-archive-svc/; echo "exit=$?"
git -C /root/tz28-work/wt rev-parse HEAD > /root/btc-pairbook-archive-svc/commit.txt; echo "exit=$?"
install -d -m 0700 /var/lib/btc-pairbook-archive; echo "exit=$?"
install -m 0644 /root/tz28-work/wt/deploy/systemd/btc-pairbook-archive.service /root/tz28-work/wt/deploy/systemd/btc-pairbook-archive.timer /etc/systemd/system/; echo "exit=$?"
systemctl daemon-reload; echo "exit=$?"
systemd-analyze verify /etc/systemd/system/btc-pairbook-archive.service /etc/systemd/system/btc-pairbook-archive.timer; echo "exit=$?"
```

Every `exit=0`. Then `I installed` must print `G-INSTALL PASS: 8 of 8` (§4.4). A FAIL is BLOCKED, and §4.8's K-28 is
not needed: nothing is enabled.

### 3.7 The timer — B-ENABLE, then G-TIMER

`I mark enable`, then **B-ENABLE**:

```
while :; do s=$(( $(date +%s) % 86400 )); [ "$s" -ge 11100 ] && [ "$s" -le 73200 ] && break; sleep 30; done; echo "second of the day=$s"; systemctl enable --now btc-pairbook-archive.timer; echo "exit=$?"
```

It waits in its own text for 03:05:00 to 20:20:00 UTC, so that the first run, 600 s after it and at most `21,600` s
long, ends before the calendar's 03:00:20 UTC and is the timer's 600 s elapse alone: `73,200 + 600 + 21,600 =
95,400` s, 02:30:00 UTC the next day. Then, within 300 s of B-ENABLE, `I timer` must print `G-TIMER PASS` (§4.5);
**a FAIL runs K-28 at once** (§4.8), before the first run fires.

### 3.8 The first run — G-TRIGGER, G-RUN and its readings

From `600` s after B-ENABLE, `I first` every 300 s while it prints `NOT YET` and exits `3` (§4.6). Where it still
prints `no run since the mark` at `900` s after B-ENABLE, **G-TRIGGER reads FAIL**, and K-28 runs.

**B-RETRY**, only where `first` prints `READING G-RUN: DEFERRED` — the run deferred, nothing removed, the timer still
enabled: `I mark retry`, then

```
systemctl start --no-block btc-pairbook-archive.service; echo "exit=$?"
```

and `I first` every 300 s again. The unit resumes the same set (§1). **B-RETRY runs at most once.** A second
`DEFERRED`, an `INTERRUPTED`, or a run that halted, is **G-RUN FAIL** — K-28 at once.

`I first` exits `0` and prints `FIRST PASS: 11 of 11`, or stops naming every gate that read FAIL (§4.6), and §4.8 runs
the stop that FAIL authorizes.

**B-START-SVC**, only where `first` reads G-UNIT FAIL and `systemctl is-active btc-pairbook.service` reads other than
`active`, before §4.8's block: `I mark start-svc`, then `systemctl start btc-pairbook.service; echo "exit=$?"`, and at
least 30 s later `I started`, which must print `STARTED PASS` — TZ-27's `started` (tz27 lines 1394 to 1404). A FAIL
there goes to §4.8's G-UNIT block.

### 3.9 Final — G-UNIT, G-STILL, G-TIMER

`I final` must print `FINAL PASS`: G-UNIT at the run's mark's `NRestarts` plus 1 — or unread for restarts where
B-START-SVC ran — G-STILL, G-TIMER again, and the store, free space and the next stop projected at the run's set's
rate (lines 1033 to 1060). A G-UNIT FAIL runs §4.8's G-UNIT block; a G-TIMER FAIL, K-28; a G-STILL FAIL is reported
and stops nothing.

### 3.10 The closing reads

§0.3's block again, then:

```
systemctl show btc-recorder.service btc-pairbook.service btc-chainbook.service btc-pairbook-archive.service btc-pairbook-archive.timer -p MainPID -p NRestarts -p ActiveState -p UnitFileState -p MemoryCurrent -p MemoryPeak
systemctl list-timers btc-pairbook-archive.timer --all --no-pager
journalctl -u btc-pairbook-archive.service --no-pager -o short-iso | tail -n 40
tail -n 80 /var/lib/btc-pairbook-archive/archive.log
tail -n 20 /var/lib/btc-pairbook/service.log
free -b
df -B1 --output=source,size,avail /var/lib; du -sb /root/tz28-work /var/lib/btc-pairbook /var/lib/btc-pairbook-archive /root/.claude
cat /root/tz28-work/state.json
```

`archive.log` and `service.log` hold counts, names, times, statuses and SHA-256 of files alone (§2 item 10).

---

## 4. The gates — fixed here, before any of their data exists

| gate | population | PASS | false failure | power, against |
|---|---|---|---|---|
| **G-TZ27** | TZ-27's Release by the API, 2 requests | §0.6 | `0` — GitHub read directly | `1`, a missing, partial or foreign asset, a digest not the set's |
| **P-PATH** | `tz-01a-dataset`'s Release through `Gh28`: 2 API requests and 1 download | §4.1 | `0` | `1`, a refused request, a record without its digest, a download not served, a request outside the idle stretch |
| **P-TOKEN** | the credential: 2 API requests | §4.2 | `0` | `1`, no credential, one from another source, no push right |
| **G-INSTALL** | the service's three files, the two units, the state directory | §4.4 | `0` | `1`, a byte changed, a unit systemd parsed otherwise, a directory not empty or not root's |
| **G-TIMER** | the timer, after B-ENABLE and at `final` | §4.5 | `0` | `1`, a timer not enabled, another schedule, another unit |
| **G-TRIGGER** | the first run after the enable mark | §4.6 | `0`, under B-ENABLE's band | `1`, no run, a run by hand or by the calendar |
| **G-RUN** | that run's ledger and the service's last result | §4.6 | `0` | `1`, a deferral twice, a halt, an interruption |
| **G-SET** | the run's set, as `set.json` and its record hold it | §4.6 | `0` | `1`, a set not TZ-27's rule's, two set records, another file |
| **G-UPLOAD** | the run's Release, by its own record, read again from the session | §4.6 | `0` | `1`, an asset missing, beyond the set, not its digest; a tag not at the run's commit |
| **G-DOWNLOAD** | the run's own full downloads, `verify.json` | §4.6 | `0` | `1`, one asset's bytes not the set's |
| **G-DELETE** | the set's files on the host | §4.6 | `0` | `1`, a file left, a removal unrecorded, a window's `window.json` lost |
| **G-RESTART** | the pair book's records after the run's mark | §4.6 | `0` | `1`, TZ-27 §4.5's |
| **G-COUNTER** | the restarted process's `start` record and the store | §4.6 | `0` | `1`, TZ-27 §4.5's |
| **G-UNIT** | the pair book's unit at the run's mark's `NRestarts` plus 1, at `first` and `final` | §4.6 | `0` | `1`, TZ-27 §4.5's |
| **G-RESUME** | the restart's window, or the next | §4.6 | `0` | `1`, a stream kept off by the cap, the floor or an error |
| **G-IDLE** | every request of the run, `transfers.jsonl` | §4.7 | `0` while the host serves `2,000,000` bytes a second | `1`, a request started outside the idle stretch or ending past second 590 |
| **G-STILL** | the recorder's unit, §3.3 to §3.9 | `MainPID`, `NRestarts` and `ActiveState` unchanged | `0` | `1`, a restart or a stop |

**Every gate is exact** — a direct read of GitHub, of the files' bytes, of systemd and of the service's and the
run's own records — so its false-failure probability under the model it judges is `0`, and the family's too, under
the one condition G-IDLE names. **A FAIL before §3.7 enables nothing; a FAIL before the run's removal removes
nothing.**

### 4.1 P-PATH

The run's own request path without a token, proved before anything is installed (CANON hard rule 14): `Gh28`, as the
run builds it, with no token, on the one Release whose bytes map §2.1 fixes — `GET
/repos/seahomebatumi-ai/btc-5m-twap/releases/tags/tz-01a-dataset`, one page of its assets, then the asset's download
URL through `github.com`'s redirect: the asset `uploaded`, `76818669` bytes, `digest` `sha256:229a944f…`, the expected
URL; the download `200`, `76,818,669` bytes, SHA-256 equal; **3 requests, each started inside the idle stretch and
ended by second 590** (lines 756 to 782). Every header is `tz27.build_request`'s (tz27 lines 509 to 519):
`Accept: application/vnd.github+json`, or `application/octet-stream` for a download; `User-Agent: btc-5m-twap-tz27`;
`X-GitHub-Api-Version: 2022-11-28`; and only where given `Authorization: Bearer` and the token, and a body's
`Content-Type` and `Content-Length` — beside `urllib`'s own `Accept-Encoding: identity`, `Host` and `Connection:
close`. A request that carries the token follows no redirect (tz27 lines 498 to 506).

### 4.2 P-TOKEN

The credential half, by the Boss's block: `tz27.credential()` as the run calls it, **its source asserted to be the
primary checkout's remote URL** — the source the unit has, because a unit's environment has no `HOME` for `gh`;
`GET /repos/seahomebatumi-ai/btc-5m-twap` with it, `200`, `full_name` this repository and `permissions.push` true; and
the Release on `tz-27-pairbook-streams` read with it, id `409534533` — **2 requests** (lines 785 to 804). **The write
half cannot be proved without writing:** its first request is the first run's own creation of its Release, and a
refusal there defers the run with nothing removed (§1), which G-RUN reads.

### 4.3 G-TZ27

§0.6.

### 4.4 G-INSTALL

Eight checks (lines 813 to 857): `commit.txt` the branch head, which is its upstream's; the service's copy of the
instrument the branch's, byte for byte by SHA-256; the service's copy of TZ-27's file the branch's and `2cba96bc…`;
both units under `/etc/systemd/system/` byte for byte the branch's; `/var/lib/btc-pairbook-archive/` a directory,
root's, mode `0700`, empty; the service `loaded`, `inactive` and `static`; the service a `oneshot`, `Restart=no`,
`MemoryMax` `134217728`, `TimeoutStartUSec` `6h`, its working directory the state directory, its `ExecStart` argv
`/root/tz04a-env/venv/bin/python -B -u /root/btc-pairbook-archive-svc/tz28-pairbook-archive-timer.py run` and its
fragment under `/etc/systemd/system/`; the timer `loaded`, `inactive` and `disabled`, its fragment there.

### 4.5 G-TIMER

Nine checks, read under `TZ=UTC` (lines 876 to 902): `loaded`; `active`, `waiting` or `running`; `enabled`; its
fragment under `/etc/systemd/system/`; its unit `btc-pairbook-archive.service`; `OnCalendar=*-*-* 03:00:20 UTC`;
`OnActiveUSec=10min`; `AccuracyUSec` `1s`; and `NextElapseUSecRealtime` exactly the next 03:00:20 UTC after the read.

### 4.6 The first run, re-read — `first`

`first` (lines 914 to 1030) finds the first run whose `start` record is at or after the enable mark, prints every
record of it, and reads it back **from the run's files, the store, the pair book's own record, systemd and the
Release — never from the run's own verdicts alone**:

- **G-TRIGGER** — the timer's `LastTriggerUSec` within 2 s of its `ActiveEnterTimestamp` plus 600 s, and the run's
  first record within 60 s after that trigger.
- **G-RUN** — the run's terminal record `complete`, the service's last `Result` `success` and `ExecMainStatus` `0`.
- **G-SET** — one set record, `set.json` its SHA-256, and the document TZ-28's rule rebuilds from it equal to it;
  every considered window and every taken file printed, `W` and `S` lines.
- **G-UPLOAD** — the Release on the run's tag read again with no token: published on the tag, no asset missing or
  beyond the set, each `uploaded` with the set's bytes and `digest`; and `git ls-remote` reading the tag a lightweight
  one at the run's commit.
- **G-DOWNLOAD** — `verify.json` the SHA-256 its record names, its rows the set's, every download `200` and equal.
- **G-DELETE** — `tz27.removed_reading` on the store: every file of the set absent, each removal recorded in
  `delete.jsonl`, every window still holding its `window.json`.
- **G-RESTART**, **G-COUNTER** — `tz27.restart_reading` and `tz27.counter_reading` on the pair book's
  `runtime.jsonl` and the store, from the run's mark: TZ-27 §4.5's five checks and four, and the start record's
  `stream_bytes` the store's windows `T <= W − 900`.
- **G-UNIT** — `tz27.unit_reads` at the mark's `NRestarts` plus 1, its ten checks, and the `MainPID` the restarted
  `start` record's.
- **G-RESUME** — `tz27.resume_decision` on the restart's window: PASS, or UNDECIDABLE where neither window's documents
  were served — the venue's matter, not the archive's — and FAIL otherwise.
- **G-IDLE** — §4.7.

**PASS** is all eleven. One `ROW` line an asset prints its name, bytes, the set's SHA-256, the Release's `digest`, the
downloaded SHA-256 and the removed file's — the per-asset table §8 asks for, from the instrument itself.

### 4.7 G-IDLE

Every request of the run, from `transfers.jsonl`: started at a second from 15 to `590 − its budget` of its window, and
ended by second 590 of that window (lines 164 to 169). **PASS** where every request holds both. Printed beside it:
each request's kind, name, bytes, budget, second and duration. The run's `complete` record carries both counts (lines
592 to 596).

### 4.8 The stops — CANON hard rule 14

**K-28** stops the archive and nothing else: future runs. It lets a run in progress end — `disable --now` stops the
timer, not the service it started — so it never cuts a run between a removal and its record:

```
systemctl disable --now btc-pairbook-archive.timer; echo "exit=$?"
```

**Authorized and run at once, and once,** on the first FAIL of G-TIMER, G-TRIGGER, G-RUN, G-SET, G-UPLOAD,
G-DOWNLOAD, G-DELETE, G-RESTART, G-COUNTER, G-RESUME or G-IDLE — **the gates that judge the archive's process**, which
on any of them is not proved. **The run applies K-28 to itself on a halt** (§1); the session then runs it again,
harmless. Verified by the Executor at least 30 s after, from the timer and the run's own record:

```
systemctl is-enabled btc-pairbook-archive.timer; echo "exit=$?"
systemctl is-active btc-pairbook-archive.timer btc-pairbook-archive.service; echo "exit=$?"
tail -n 3 /var/lib/btc-pairbook-archive/ledger.jsonl
```

— the timer `disabled` and `inactive`; the service `inactive` or `failed`, no run in progress; the ledger's last
records the run's own. **On a G-UNIT FAIL**, at `first` or `final`, the pair book's stop is authorized too — TZ-26
§4.7's block, as TZ-27 §4.7 carried it, with K-28 before it, so that no later run restarts it:

**K-28, K-26 and B-RESTORE-CB:**

```
systemctl disable --now btc-pairbook-archive.timer; echo "exit=$?"
systemctl disable --now btc-pairbook.service; echo "exit=$?"
systemctl enable --now btc-chainbook.service; echo "exit=$?"
```

Verified at least 30 s after: `systemctl is-active` and `is-enabled` of the three units, `systemctl show
btc-pairbook.service btc-chainbook.service -p MainPID -p ActiveState`, and `tail -n 1
/var/lib/btc-pairbook/runtime.jsonl` — the archive's timer `disabled`, the pair book `inactive` or `failed`,
`disabled`, `MainPID` `0` and its record's last line a `stop`; the chain book `active` and `enabled` with a
`MainPID`. **G-STILL judges the recorder** and stops nothing. **Under PASS no block of this section is run.**

### 4.9 What a PASS establishes, and what it does not

The archive's timer runs unattended, outside every session; its first run, fired by the timer, moved its set to its
own Release byte for byte — by the Release's digest, a full download and a hash before each removal — restarted the
pair book with its count the store's, saw its next window stream, and made every request inside the pair book's idle
stretch. **Not established:** the daily calendar run itself — the next TZ that touches the host reads its ledger
records; a run's behaviour under a deferral or a halt on the host — the self-test's, on a simulated pair book; anything
of a stream's content — B3's measurement's; and whether the idle stretch removes the reconnect map §7 item 109 records
— B3's measurement reads the streams' segments beside the run's request times.

---

## 5. The instrument and the units

`research/tz28-pairbook-archive-timer.py`, Appendix A, fixed by the Architect as this TZ's Validation and written byte
for byte. **The standard library alone**, run under `/root/tz04a-env` — Python 3.12.3, the pair book's interpreter,
which nothing here modifies. It imports nothing from the repository: it **loads** `research/tz27-pairbook-archive.py`
from its own directory, asserts its SHA-256 `2cba96bc…` and executes those very bytes (lines 63 to 76), so TZ-27's
audit hook is installed and TZ-27's functions are the ones every step calls; each mode sets `tz27.MODE` and
`tz27.WORK` before it acts (lines 415, 455, 480, 512, 533, 572, 585, 601, 610, 679 and 1410). **Its own code** is the
idle stretch (lines 131 to 170), the calendar and systemd's stamps (lines 172 to 194), the ledger and the resume rule
(lines 199 to 252), `Gh28` (lines 312 to 352), the set document under this TZ's tag (lines 357 to 377), the run's
steps (lines 407 to 688), the deployment's readings (lines 693 to 1060) and the self-test (lines 1063 to 1397). It
writes no second implementation of TZ-27's set rule, its proofs or its readings. One mode a run; each prints its
findings with UTC stamps, its peak memory, the opens TZ-27's hook refused, its opens under the store, its requests,
uploads and downloads with their bytes, and its files removed (lines 1430 to 1433). Exit `0` is every assert held;
`1` a failed assert, named, or a BLOCK whose message says so; `3` NOT YET; and the run's own `75` and `2` (§1). Run
with `-O` it refuses to start (lines 53 to 55).

**The two units** are Appendix A's, installed byte for byte, and the self-test asserts the lines of each that the
instrument depends on (lines 1207 to 1215).

---

## 6. Cost

Measured by the Architect on 2026-10-11 under Python 3.12.3 on one core of an Intel Xeon at 2.10 GHz, and taken at the
population's upper bound: **a run's set at most 400 files and `8,100,000,000` bytes** — TZ-27 §6's bound, `STREAM_CAP`
plus one window's cut and its last flush.

| check | population | measured | bound |
|---|---|---|---|
| `selftest` | 34 checks, seven simulated runs, one loopback server | `1.17` to `1.29` s, six runs | `60` s |
| `fingerprint` | 37 rows, the map | under 1 s | `30` s |
| `tz27-release` | 2 API requests, 51 rows | not measured against GitHub | `60` s a request (tz27 line 122) |
| `path` | 2 API requests and 76,818,669 bytes, held to the idle stretch | the download under 4 s from the Architect's session (map §6) | its wait at most `900` s; `60` s a request, `120` s a read of the download (tz27 lines 122 and 124) |
| `path-token` | 2 API requests | — | `60` s a request |
| `installed`, `mark`, `timer`, `still`, `scratch`, `started`, `final`, each `reclaim`, a `first` that prints NOT YET | — | under 1 s each | `30` s a run |
| `first`, the deciding run | the run's records, the store's listing, the Release's record: at most 1 + 5 API pages for 400 assets | under 1 s in a harness over 5 assets | `60` s a request; its reads under `30` s |
| **the run, in the unit** | 400 files, `8,100,000,000` bytes | `19.4` to `20.9` s wall and `22.4` to `23.5` s of processor over 400 files and `2,190,000,000` bytes on loopback, six runs — four passes over the set's bytes | **`21,600` s, `TimeoutStartSec`** |

**Single-session processor, at the measured rates and the upper bound, under `165` s** — `selftest` `1.3`, the
`path` download's hashing of `76,818,669` bytes at TZ-27's `317,200,000` bytes a second `0.25`, `installed`'s of two
files under `0.01`, and at most `160` runs of the other modes under 1 s each: `first` at most `145` of them — every
300 s from 600 s after B-ENABLE to the end of a run at its `21,600` s bound, `(22,200 − 600) / 300 + 1 = 73`, and
`72` more after B-RETRY — with `fingerprint`, `tz27-release`, `path`, `path-token`, `installed`, `timer`, `still`,
`scratch`, `started`, `final`, three `mark`s and two `reclaim`s, `15` — **under `3,600`, so nothing is sampled.**
Nothing the session runs hashes the set; no fail-fast is needed. **The run is
the unit's, not the session's,** and is bounded by `TimeoutStartSec`, derived at the upper bound and at
`RATE_FLOOR`: its hashing, two passes in the run's process — the set and the removal — at TZ-27's measured
`317,200,000` bytes a second, `51` s; its upload, `8,100,000,000 / 2,000,000 = 4,050` s of transfer and `400` s of
gaps, inside at least `519` s of each 900 s window — the stretch's `575` s less the largest file's budget, `56` s —
so at most 9 windows, `8,100` s; the settle, `120` s; the verify, 9 windows again, `8,100` s; the band's wait, at
most `900 − 471 + 15 = 444` s, and the reads after the signal, `120` s; G-RESUME at most `1,840 − 15 + 1 = 1,826` s
after the signal: **`18,761` s in all, under `21,600`.** A run longer than `21,600` s is stopped by systemd and the next
run resumes it (§1). **At the host's measured rates** — `9,297,801` bytes a second up, `14,140,406` down (map §6) —
a weekday's `2,520,000,000` bytes take about `271` s up and `178` s down, one idle stretch each, and a run about
40 minutes with its waits; the first run, with up to two and a half days of streams, about an hour [modelled].
**Wall clock about three hours:** §0 to §3.6 about 45 minutes, `path`'s wait among them; B-ENABLE's band; the first
run from 600 s after it; `first`, `final` and §9 about 20 minutes. **The host pays** each set's bytes sent once and
received once a day, inside the idle stretch.

---

## 7. Validation

| # | check | count |
|---|---|---|
| **V1** | §0.2's fingerprint | `FINGERPRINT PASS`: revision `2026-10-11-b`; anchors 6 of 6, 4 re-derived; 37 rows, 34 of 34 `frozen` equal |
| **V2** | §0.3's host gate | H1 to H5, the memory and the disk gate; the rest printed |
| **V3** | §0.1's and §3.1's files | 3 of 3 hashes asserted at each, lines and bytes; TZ-27's staged copy `2cba96bc…`; the branch's diff against `origin/main` names exactly the three paths, each `A` |
| **V4** | the self-test | `34 of 34` |
| **V5** | G-TZ27 | `G-TZ27 PASS`, 51 of 51 assets, Release `409534533`, 2 requests |
| **V6** | P-PATH | `READING P-PATH: served`, 3 requests, each inside the idle stretch; the record's state, size, digest and URL; the download's status, bytes and SHA-256 |
| **V7** | P-TOKEN | `READING P-TOKEN: served`, the source the primary checkout's remote URL, push true, Release `409534533`, 2 requests; `exit=0` |
| **V8** | B-INSTALL and G-INSTALL | 7 of 7 `exit=0`; `G-INSTALL PASS: 8 of 8` |
| **V9** | B-ENABLE and G-TIMER | the second of the day inside 11,100 to 73,200 and `exit=0`; `G-TIMER PASS`, 9 checks, at §3.7 and at `final` |
| **V10** | the first run | `FIRST PASS: 11 of 11` — G-TRIGGER, G-RUN, G-SET, G-UPLOAD, G-DOWNLOAD, G-DELETE, G-RESTART, G-COUNTER, G-UNIT, G-RESUME and G-IDLE; every `R` record of the run; the `W` and `S` lines; `ROW` n of n |
| **V11** | B-RETRY | not run, or run once, its mark and `exit=0` |
| **V12** | final | `FINAL PASS`: G-UNIT 10 checks at the run's mark's `NRestarts` plus 1 — 9, the restarts unread, where B-START-SVC ran — G-STILL, G-TIMER; the projection |
| **V13** | the hook and the counters | opens refused `0` at every mode; requests `2` at `tz27-release`, `3` at `path`, `2` at `path-token`, `2 + ⌊n/100⌋` at a deciding `first` for a set of `n`; store opens `0` at every mode but `first`, `2` or `3` there, and `started`, `1`; files removed `0` at every session mode but `selftest`, whose `10` are its temporary stores' |
| **V14** | contract §4.2's self-check, and the line below | its first line `0`; the diff naming the three paths alone; nothing `.parquet` or `.zip`; the line below `0` |
| **V15** | §3.10's closing reads | every read printed |
| **V16** | §9's `reclaim` runs | files considered, named by a report, kept by name, copied and already held; the store's count after equal to before plus the copies |
| **V17** | §9's removals | `git worktree remove` without `--force` exit `0`; `test -e` exit `1` for `/root/tz28-work` and each directory removed; `git worktree list` naming `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else |

V14's further line, run beside contract §4.2's three — no stream file entered git history:

```
git ls-tree -r --name-only origin/main | grep -c -e '\.gz$' -e '\.jsonl$'
```

---

## 8. The report

`CryptoReports/TZ-28-pairbook-archive-timer-report.md`, in contract §8's order. **In its first ten lines:** G-TZ27;
P-PATH and P-TOKEN; G-INSTALL; G-TIMER and the next calendar run; the first run — its `A`, its files, windows and
bytes, its Release's id and tag; G-UPLOAD, G-DOWNLOAD and G-DELETE and the bytes freed; G-RESTART, G-COUNTER, G-UNIT
and G-RESUME; G-IDLE; G-STILL; and whether the timer, the pair book and the recorder run, and how that was verified.
**Its §3, Publication,** holds the branch, its commit, the pull request, the first run's tag and Release id, contract
§4.2's self-check, and **every `ROW` line `first` printed** — contract §5.1's local hash, the downloaded hash and
that they are equal, here the unit's, re-read by the session. Beyond what V1 to V17 print: every mark's instant;
every block the classifier refused, who ran it and when; **the run's first and last stamped line of each step — its
`L` records in `archive.log` — and every `T` line `first` printed, so that B3's measurement can set the streams'
segments beside the run's request times** (map §7 item 109); every free-space and `MemAvailable` read with its instant
and bound; the run's `peak_rss`; each unit's memory at every read; §9's counts and removals; and every file the run
and the session wrote, by SHA-256, but a Release's assets. **The report is drafted in the primary checkout
`/root/btc-5m-twap` before B-RECLAIM-OWN and committed after it**, so the removal of this TZ's tree is in it.

---

## 9. Reclaim — the host left clean (CANON hard rule 15)

**What a file is kept for:** a committed report prints its SHA-256, whole or as a prefix of 16 to 64 hex characters,
or it is kept by name: `state.json` and every file under `logs/`. TZ-27's `reclaim` (tz27 lines 1467 to 1545) copies
each into `/root/btc-forensics/` as `<tree>--<path with / as -->`, by exclusive create, and verifies its hash; a name
already there with the same hash is counted as held, and with another hash is a failed assert. The branch worktree is
not copied: `reclaim` asserts that `git status --porcelain --ignored` in it prints nothing and that its `HEAD` is its
upstream's, so `git worktree remove` needs no `--force`. The report draft in `CryptoReports/` counts as a report.
**Not scratch, and not reclaimed:** `/root/btc-pairbook-archive-svc/` and `/var/lib/btc-pairbook-archive/` — the
archive's code and state, which its timer runs from and writes (map §3).

**B-RECLAIM-SCRATCH**, after §3.3 and before §3.4, for every directory `I scratch` named **earlier** — none it named
live, and never this session's own; map §3 names TZ-27's pair, `70b5ba7a…` and `952e88f3…`:

```
I reclaim <each earlier directory, by its full path>
rm -rf <one such directory>; echo "exit=$?"
test -e <that directory>; echo "exit=$?"
```

One `I reclaim` names every earlier directory; then one `rm -rf` and one `test -e` a directory. `reclaim` refuses a
directory born from 1 s before to 60 s after a running claude process started, and any path but `/root/tz28-work` that
is not a UUID directory under `/tmp/` whose parent's name carries `btc-5m-twap` (tz27 lines 1491 to 1505); it prints
`RECLAIM PASS` before any removal. If `I scratch` names none earlier, the block is recorded as empty and skipped.

**B-RECLAIM-OWN**, last, after §3.10 and with the report drafted. **Its output is written to no file; the report
quotes it verbatim from the session**, the checks after the removal included:

```
I reclaim /root/tz28-work
git -C /root/btc-5m-twap worktree remove /root/tz28-work/wt; echo "exit=$?"
rm -rf /root/tz28-work; echo "exit=$?"
test -e /root/tz28-work; echo "exit=$?"
git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
find /root/btc-forensics -type f | wc -l
df -B1 --output=source,size,avail /var/lib
```

The branch `tz-28-pairbook-archive-timer` stays on `origin` and as a local ref, and the run's tag and Release stay;
only the working tree goes. **Kept:** `/root/btc-pairbook-archive-svc/`, `/root/btc-pairbook-svc/` and
`/root/btc-recorder-svc/` are the running units' code, `/root/tz18a-svc/` the disabled chain book's, which
B-RESTORE-CB needs; the three capture roots, the archive's state and the forensic store are data, never scratch. **A
refused `rm -rf` is handed to the Boss** by §3's route, one tree per command, and verified by `test -e`.

---

## 10. Pre-send checks

Performed by the Architect on 2026-10-11 against this file as sent, in a reading separate from its writing, with the
repository at `origin/main` `2c1fcd0e99112890de4a1f733dd3d6dfb7031cd0` and map revision `2026-10-11-b` as it ships with
this TZ. `tz27` is `research/tz27-pairbook-archive.py` at that commit, `2cba96bc…`; a service line is
`research/tz26-nesting-b3-capture.py`'s there; any other line number is Appendix A's, the extracted file's.

| # | check | result |
|---|---|---|
| **C1** | scope against body | **Repository paths the body names, 13, and the 37 files of the map's table:** `CryptoTZ/TZ-28-pairbook-archive-timer.md`, read by §0.1's script; `SYSTEM-MAP.md` and its table's files, read by `I0 fingerprint`; `BTC-EXECUTOR-INSTRUCTIONS.md`, cited for §1, §3.3, §4.2, §5.1, §5.3 and §8; `research/tz28-pairbook-archive-timer.py`, `deploy/systemd/btc-pairbook-archive.service` and `deploy/systemd/btc-pairbook-archive.timer`, written on the branch, staged and installed; `research/tz27-pairbook-archive.py`, staged and installed as a copy and loaded by its bytes, never modified; `research/tz26-nesting-b3-capture.py`, cited for its lines, its host copy hashed by §0.3's `sha256sum`, never imported or run; `deploy/systemd/btc-pairbook.service`, compared by §0.3's `cmp`; `CryptoTZ/TZ-27-pairbook-archive.md` and `CryptoTZ/TZ-26-nesting-b3-capture.md`, cited and read by no step; every `CryptoReports/*.md`, read by `reclaim` for hashes (tz27 line 1467); `CryptoReports/TZ-28-pairbook-archive-timer-report.md`, written to `main`. **Entry points:** Appendix A's fifteen modes — `run`, `fingerprint`, `tz27-release`, `selftest`, `still`, `scratch`, `reclaim`, `path`, `path-token`, `installed`, `mark`, `timer`, `first`, `started`, `final` (lines 1399 to 1429); §0.1's script; `git` (`fetch`, `worktree add`, `remove`, `prune` and `list`, `add`, `commit`, `push`, `ls-remote`, `rev-parse`); `gh` for the pull request; `install`; `systemctl` (`daemon-reload`, `show`, `is-active`, `is-enabled`, `list-timers`, `enable --now`, `disable --now`, `start`, `start --no-block`, and the run's `kill --signal=SIGTERM`); `systemd-analyze verify`; `journalctl -u`; and the shell reads of §0.3, §3.10, §4.8 and §9. **Outputs:** under `/root/tz28-work/` `logs/` with `B-PATH-TOKEN.log`, `stage/`, `wt/`, `state.json` and the self-test's transient `selftest-tmp/`; `/root/btc-pairbook-archive-svc/`'s two files and `commit.txt`; the two units under `/etc/systemd/system/`; under `/var/lib/btc-pairbook-archive/` `ledger.jsonl`, `run.lock`, `archive.log` and `runs/<A>/` `set.json`, `upload.jsonl`, `verify.json`, `delete.jsonl` and `transfers.jsonl`; the branch, its commit and the pull request; the first run's Release, its assets and its tag; the report; the forensic store's copies; the pair book's own records at the run's restart; and on a FAIL the chain book's own writes. **Intersections with §2, by path and by content class, 14, each named in §2:** the report on `main` — paths item 2, prohibited item 7; the first run's Release, whose assets carry prices, sizes and books — paths item 3, prohibited item 10's exemption, which names a Release's assets, and item 3, which forbids extraction; the run's removals of its set's stream files — the host paths' named exemption to prohibited item 3; the run's reads of those files, which carry prices — item 3, as bytes, hashed and sent verbatim, never decompressed (§1, the reserve: CANON PART II's B3 store moved whole, as TZ-27 moved it); the run's and P-PATH's downloads, which carry prices, the second Binance's — item 10, hashed as they arrive and written nowhere; the unit's own writes under `/var/lib/btc-pairbook-archive/` — item 3's named exemption; the pair book's own records at its restart — item 3, the pair book's unit; `first`'s and `started`'s reads under the store — item 3, named; the shell reads under the capture roots, §0.3's, §3.10's and §4.8's — items 2 and 3, named, none under the chain book's; B-INSTALL, B-ENABLE, B-RETRY, B-START-SVC, the run's restart and its own K-28, and K-28, K-26 and B-RESTORE-CB — item 5, each named, and the chain book's own writes — item 4's exemption; the unit's interpreter `/root/tz04a-env/` — item 6, run and never modified; §9's copies of `logs/` and `state.json` — items 6 and 10; every request class — `tz27-release`'s, `path`'s, `path-token`'s, `first`'s, the run's, the self-test's loopback, `git` and `gh` — item 8; the credential — item 9, read by `path-token`, the Boss's, and the unit's run alone (lines 297, 456 and 789 are `credential()`'s only calls). **Classes checked and intersecting nothing:** `set.json`, `upload.jsonl`, `verify.json`, `delete.jsonl`, `transfers.jsonl` and the ledger carry no price, size, book or hash key, each asserted by `tz27.forbid` or `tz27.assert_keys` before it is written (lines 215, 243, 371 to 376, 500 and 502; tz27 lines 151 to 154 and 331 to 345); `window.json` and `runtime.jsonl` are the reserve's exceptions, and of `window.json` only `documents_ok`, `pid` and the stream's state are read (tz27 lines 895 to 920); `books.jsonl.gz` and `documents.jsonl` are never opened — the set takes `is_stream` names alone (tz27 lines 387 to 389 and 441); no settled document is fetched and no five-minute market is read, so M0's reserve is not touched. **One sentence was corrected in this reading:** prohibited item 3 now names `started`'s read of `runtime.jsonl` and §4.8's two `tail` reads, of `runtime.jsonl` and of the ledger, which it had left out. |
| **C2** | origin of every expectation | **§5's literals** are Appendix A's, fixed by the Architect and measured by nothing: exits `0`, `1`, `3`, `75` and `2` (lines 95, 96, 672 to 688 and 1399 to 1438), `-O` refused (lines 53 to 55); `2cba96bc…` and Python `3.12.3`, quoted from map §0 and §6. **§7's, by kind.** Quoted from a committed artifact: V1's revision `2026-10-11-b`, `6` anchors, `4` re-derived, `37` rows and `34` `frozen`, map `2026-10-11-b` §0, which ships in this upload; V3's `2cba96bc…`, map §0; V5's `51`, `409534533` and `678,739,504`, map §2.5 and §4 and TZ-27's report; V6's `76818669` and `229a944f…`, map §2.1; V17's two worktrees, map §3. Computed by an implementation independent of the one under test: V3's three SHA-256, lines and bytes, by `sha256sum` and `wc` over Appendix A's files, against the extraction script's `hashlib`, exact; V9's `11,100` = 3 × 3,600 + 300 and `73,200` = 20 × 3,600 + 1,200, and `95,400` = 73,200 + 600 + 21,600, exact. Fixed by Appendix A's and `tz27`'s code, which this TZ measures nothing to set: V4's `34`, V5's and V7's `2` requests, V6's `3`, V8's `7` and `8`, V9's `9`, V10's `11`, V12's `10` or `9`, V13's counts and the self-test's `10` removals, V14's `0`. **§0.4's floors:** `2,300,000,000` = `2,200,000,000`, service line 131, + `100,000,000`; `2,001,000,000` = `2,000,000,000` + `1,000,000`; `106,086,400` = 2 × `53,043,200`, the Architect's measured peak, made before this TZ was sent; `134,217,728` = 128 × 2^20, exact. **No expectation depends on a quantity this TZ measures:** `n`, the first run's set, enters only identities — `ROW n of n`, `2 + ⌊n/100⌋` requests — never a literal; the run's `A`, its bytes, rate, projection, free space and memory are printed, not expected. |
| **C3** | shape of every diff | Three paths, each new: `git cat-file -e 2c1fcd0:<path>` exits `128` for `research/tz28-pairbook-archive-timer.py`, `deploy/systemd/btc-pairbook-archive.service` and `deploy/systemd/btc-pairbook-archive.timer`, so the change replaces **none** of their lines; V3 asserts each `A`. The report's path is new too, exit `128`. PART VI's two words for an additive diff appear nowhere in this TZ — `grep -c` of them prints `0` — since none is needed. |
| **C4** | cost of every check | §6, at the population's upper bound: a run's set at 400 files and `8,100,000,000` bytes, TZ-27 §6's bound — `STREAM_CAP` plus one window's cut and its last flush (service lines 133 and 134). **Single-session processor under `165` s** — `selftest` `1.3`, `path`'s hashing of `76,818,669` bytes at `317,200,000` bytes a second `0.25`, `installed`'s of two files under `0.01`, and at most `160` runs of the other modes under 1 s each: `first` at most `145` — `(22,200 − 600) / 300 + 1 = 73` before B-RETRY and `72` after it — and `15` others — **under `3,600`; nothing is sampled.** The session hashes no file of the set. **The run's fail-fast is `TimeoutStartSec=21600`**, derived term by term at the upper bound and `RATE_FLOOR`: hashing, two passes at `317,200,000` bytes a second, `51` s; upload, `4,050` s of transfer and `400` s of gaps inside at least `519` s of each window — `575` s of stretch less the largest file's `56` s budget — `9` windows, `8,100` s; settle `120` s; verify `8,100` s; the band's wait `900 − 471 + 15 = 444` s; the restart's reads `120` s; G-RESUME at most `1,840 − 15 + 1 = 1,826` s — **`18,761` s, under `21,600`.** B-ENABLE's band, `11,100` to `73,200`, keeps the first run, `600 + 21,600` s after it, before the next 03:00:20 UTC. The session's own bounds: `path`'s wait `900` s; `60` s a request (tz27 line 122) and `120` s a download read (tz27 line 124); G-TRIGGER's `900` s = `600` + one `300` s poll. Wall clock about three hours [modelled], §6. |
| **C5** | every count | V1's `37` = 34 + 2 + 1, read from map `2026-10-11-b` §0 by `fingerprint` itself on a clone of `2c1fcd0` carrying this map — `rows 37: frozen 34 of 34 equal, tracked 2, reported 1`; its `4` re-derived anchors `A2`, `A4`, `A5`, `A6` (lines 703 to 706; `tz27.ANCHOR_FILES`). V3's `3`: Appendix A's three files. V4's `34`: 33 `ok(` call sites in `mode_selftest`, one inside a loop of the two units (lines 1207 to 1215), and printed `34 of 34 checks passed` by every run. V5's `2` = the Release by tag + one page of its 51 assets (tz27 lines 601 to 610: a page under 100 ends the listing). V6's `3` = the Release by tag, one asset page, the download (lines 764, 766 and 772), asserted `len(trs) == 3` (line 780). V7's `2` = the repository and the Release by tag (lines 795 and 801). V8's `7`: §3.6's seven commands; `8`: `mode_installed`'s eight keys (lines 835 to 850). V9's `9`: `timer_reading`'s nine keys (lines 881 to 889). V10's `11`: `mode_first`'s eleven readings (lines 943 to 1020). V12's `10`: `tz27.unit_reads`' nine keys and `restarts` (tz27 lines 1017 to 1026), `9` with `n` `None` after B-START-SVC (line 1038). V13's: `first` `2 + ⌊n/100⌋` requests — the Release by tag and `⌊n/100⌋ + 1` pages (tz27 lines 601 to 610); its store opens `runtime.jsonl` once and `window.json` once or twice (lines 997 and 1010 to 1011; tz27 lines 908 to 911); `started` one (tz27 line 1399); the self-test's `10` removals — `4 + 1 + 1 + 2 + 1 + 1` over its six worlds that reach the removal (lines 1265 to 1376), `files removed 10` printed by the Architect's run of the frozen file. V14's `0`: `git ls-tree -r --name-only 2c1fcd0` with `.gz` or `.jsonl` prints `0`, and the three paths add none. §0.3's seven BLOCKING conditions: H1 to H5, memory, disk. §0.5's `36` ref lines, map §1. §6's `160` other-mode runs: `145` of `first`, and `fingerprint`, `tz27-release`, `path`, `path-token`, `installed`, `timer`, `still`, `scratch`, `started`, `final`, three `mark`s and two `reclaim`s, `15`. |
| **C6** | every population | G-TZ27: TZ-27's Release on `tz-27-pairbook-streams` and one page of its 51 assets, against `/root/btc-forensics/tz27-work--archive--set.json`. P-PATH: the Release `tz-01a-dataset`, its one asset, 2 API requests and 1 download. P-TOKEN: the repository's record and TZ-27's Release, 2 requests. G-INSTALL: the service's three files, the two units, the state directory. G-TIMER: the timer, at §3.7 and at `final`. G-TRIGGER: the first `start` record at or after the enable mark, and the timer's own stamps. G-RUN: that run's ledger records and the service's last invocation. G-SET: every window directory of the store as of `A`, the considered ones `T + 970 <= A`, the set at most 400 of their stream files. G-UPLOAD and G-DOWNLOAD: the set's assets in the Release on `pairbook-streams-<A>`, and its tag. G-DELETE: the set's files on the host. G-RESTART: the pair book's `runtime.jsonl` records at or after the run's mark. G-COUNTER: the restarted process's `start` record and the store's windows `T <= W − 900`. G-UNIT: the pair book's unit at the mark's `NRestarts` plus 1, at the run's restart, `first` and `final`; without the restarts check after B-START-SVC. G-RESUME: window `W`, or `W + 900` where `W`'s documents were not served. G-IDLE: every request of the run, `transfers.jsonl`. G-STILL: the recorder's unit, §3.3 to §3.9. Printed, not gated: the projection — the set's bytes over its span, the store's streams and free space at the run's end and at `final`; each memory peak — one process; `MemAvailable` and free space — the host at each read; `du` — the store at each read. |
| **C7** | every signature and every behaviour | **`tz27` at `2c1fcd0`, every function the TZ names, as the file holds it:** `def inventory(root, a, max_assets=RUN_MAX_ASSETS, asset_max=ASSET_MAX_BYTES):` (430) — due 60 s before `A`, `if T + CLOSE_OFFSET + SETTLE_S > a:` (437) with `SETTLE_S = 60` (108); closed, `"window.json" in names` (443); oldest first and at most 400, `window_dirs` in order, `sorted(…, key=stream_index)` (441) and `files[:max_assets]` (448); size and time unchanged, the assert at 454; `return assets, windows, len(files) - len(taken), open_n` (460). `def credential():` (725) — the remote URL first, `return tok, "the primary checkout's remote URL"` (731 to 732), `gh` second (733 to 738). `def build_request(method, url, token=None, accept=ACCEPT_API, data=None, ctype=None, length=None):` (509), its headers at 512 to 518; `class _NoRedirect` (498), `opener(follow=token is None)` (565). `def upload_set(gh, rel, doc, root, log, wait_min=WAIT_MIN_S):` (765) — assets beyond the set refused (770 to 771), one kept where it matches (775), sent and hashed as sent (787 to 790), each write paced 1 s (`pace`, 580 to 584; `UPLOAD_GAP_S = 1.0`, 117); `return sent, held` (812). `def verify_release(gh, tag, doc, download=True):` (685), every asset downloaded only where every record holds (694 to 699); `def release_reading(rel, tag, rows, missing, extra):` (703), five keys (704 to 708). `def delete_set(root, doc, done, now, log):` (815) — hashed again before removal (829 to 830), `os.remove(p)` (833), logged at once (844). `def removed_reading(root, doc, done):` (1313). `def restart_reading(recs, mark):` (860), five keys (869 to 876); `def counter_reading(root, start, doc):` (880), four keys (888 to 891); `def unit_reads(n_restarts):` (1007), nine keys and `restarts` where `n_restarts is not None` (1017 to 1026); `def resume_decision(W, pid, now, read):` (903) — `NOT YET`, `W + 900` where `W`'s documents were not served, `UNDECIDABLE` where neither's were (908 to 919); `def projection(bytes_total, first_T, last_T, counter, free, now):` (923). `def mode_still():` (1041), `def mode_started():` (1394), `def mode_mark(name):` (1065) with `assert name in ("kill-svc", "start-svc")` (1066), `def mode_scratch(own):` (1453), `def reclaimable(tree):` (1491), `def mode_reclaim(trees):` (1499), `def ls_remote_tag(tag):` (1139), `def floor_check():` (324), `def forbid(obj, what, depth=0):` (331), `def policy(mode, event, args, work, allowed):` (214), `sys.addaudithook(_audit)` (275), `def sha256_file(path, chunk=1 << 20):` (293), `def upload_ready(records, assets_n, now_ns):` (1219), `def stream_bytes_view(root, upto=None):` (416), `def systemctl_show(unit, props):` (973), `class GitHub:` (559) with `def __init__(self, token=None, api=API_BASE, uploads=UPLOAD_BASE, web=WEB_BASE):` (563). **Service lines:** `DOC_OFFSET = 545` (110), `STREAM_OPEN = 595` (114), `STREAM_CLOSE = 905` (115), `CLOSE_OFFSET = 910` (117), `RESOURCE_FLOOR = 2200000000` (131), `STREAM_FLOOR = 4500000000` (132), `STREAM_CAP = 8000000000` (133), `WINDOW_STREAM_MAX = 100000000` (134), `def stream_off_reason(docs_ok, free, total):` (809). **Every behaviour this TZ attributes to Appendix A,** by line: `-O`, 53 to 55; `tz27` executed from its asserted bytes, 63 to 76; the idle stretch and each request's budget, 99 to 101 and 131 to 150; the band, 102 and 153 to 161; G-IDLE, 164 to 169; the calendar, 90 to 93 and 172 to 175; the ledger and its keys, 199 to 220; a halt refusing until a clear, 223 to 226 and 612 to 618; resume or a new `A`, 229 to 235 and 619 to 626; `Gh28` timing every request, 312 to 344; the Release published at `commit.txt`'s commit and never the latest, 306 to 309 and 346 to 352; the tag outside TZ-27's rule and the 1,140,000,000-byte bound, 113, 361 and 366 to 367; the Release's body, 380 to 389; the floors, 106, 107 and 407 to 411; `empty`, 423 to 425; verify 120 s after the upload's record, 481 to 486; delete only after this run's `verify.json`, 513 to 514; the restart refusing a pair book not `active`, 536, its mark inside the band, 537 to 540; deferral before the removal and halt after it, 108 and 659 to 669; the run disabling its own timer, 599 to 605; the unit's checks of systemd's start, 672 to 688; `fingerprint`, 693 to 722; G-TZ27, 725 to 748; P-PATH, 756 to 782; P-TOKEN and its source, 785 to 804; G-INSTALL, 813 to 857; the marks, 860 to 873; G-TIMER, 876 to 902; `first`, 914 to 1030; `final`, 1033 to 1060; the units' lines the self-test asserts, 1207 to 1215; the work-tree rule, 1409; the counters printed, 1430 to 1433. **Two sentences were rewritten in this reading:** V12 had `10` G-UNIT checks at `final` whatever ran, and `final` passes `None` after B-START-SVC (line 1038) — `9`; prohibited item 3 had no session mode but `first` open the store, and `started` reads `runtime.jsonl` (tz27 line 1399) — C1 names its other two omissions. |
| **C8** | every cross-reference | Resolved by reading the text referenced. **Map `2026-10-11-b`:** §0's anchors and 37 rows, 34 / 2 / 1, and `tz27`'s row `2cba96bc…` `frozen`; §1's `2c1fcd0`, five branches, two tags and 36 ref lines; §2.1's asset, `76,818,669` bytes and `229a944f…`; §2.5's pair book — its root, its files, the count summed at a start, TZ-27's restart and `10,095,699`, the reserve, and `du` beside `df`; §3's store at `1,810`, the two worktrees, TZ-27's pair `70b5ba7a…` / `952e88f3…`, and the archive's code and state not scratch; §4's TZ-27 row, the Release's API record unread from the Architect's session; §6's host identity, `1,002,127,360` bytes and one processor, the disk row, the headroom's `2026-10-14 12:42 UTC` [modelled], the memory row's peaks, process supervision, the GitHub Releases row's limits and rates, and the sandbox's network limit; §7 items 106 and 109. **CANON `2026-10-11-b`:** PART II's B3 row — the store reserved on the host and in every Release asset made from it — and M0's second look; PART III's one implementation of every formula and its canonical locations, the timer row added in this revision; hard rules 11, 13, 14 — its band and timer clauses — and 15. **Contract:** §1 steps 1 to 4, §3.3's tags, §4.2's self-check, §5.1's token-free verification, §5.3's credentials, §8's order. **TZ-27:** §1's band, §2's prohibitions as its hook enforces them, §4.5's G-RESTART, G-COUNTER and G-UNIT, §4.7's stops, §6's bound. **TZ-26:** §4.7's K-26 and B-RESTORE-CB block, verbatim. **This TZ:** §0.1 to §0.6, §1, §2's items, §3.1 to §3.10, §4.1 to §4.9, §5 to §9 and Appendix A, each supporting the sentence that cites it. **None unresolved.** |

**Five checks could not be performed from this session, because it is not the capture host** (map §6), and each is a
BLOCK condition or a gate of this TZ under CANON hard rule 13: the API's record of TZ-27's Release — G-TZ27, §0.6,
before anything is built; the host's reach of `api.github.com` and `github.com` without a token, inside the idle
stretch — P-PATH, §3.4, before anything is installed; the credential's source and push right — P-TOKEN, §3.5, before
anything is installed; its right to write a Release and the reach of `uploads.github.com` — the first run's own first
write, a refusal of which defers with nothing removed and, twice, reads G-RUN FAIL and stops the timer, §3.8; and
systemd's reading of the two units and the host's own state — B-INSTALL's `systemd-analyze verify`, G-INSTALL and
G-TIMER, §3.6 and §3.7, and §0.3. Everything else above was performed here, on the frozen file under Python 3.12.3:
the self-test, `34 of 34`, seven runs; `fingerprint` against this revision of the map on a clone of `main` at `2c1fcd0`;
the run whole, six times, against a store of 400 stream files and a loopback server in another process; and every
other mode in a harness that stands in for systemd.

---

## Appendix A — the instrument and the two units, byte for byte

Extracted by §0.1's script; each block's content is the file.

### `research/tz28-pairbook-archive-timer.py`

```python file=research/tz28-pairbook-archive-timer.py
#!/usr/bin/env python3
"""TZ-28 - the pair book's archive on a timer: TZ-27's set, proofs, removal and restart, run unattended once a day
by btc-pairbook-archive.timer, every request inside the pair book's idle stretch.

    run               the unit's one mode, ExecStart of btc-pairbook-archive.service: a new set as of now, or the
                      pending one resumed; upload, verify, delete, restart and resume through TZ-27's own functions,
                      each under TZ-27's own section 2; one record a step in /var/lib/btc-pairbook-archive/
                      ledger.jsonl. Exit 0 complete or empty; 75 deferred - nothing removed, the next run resumes it;
                      1 halted - the run disables its own timer; 2 not started
    fingerprint       map section 0 against the primary checkout
    selftest          every rule of this file, on literals, temporary stores, a simulated pair book and a loopback
                      server only
    tz27-release      G-TZ27: the Release on tz-27-pairbook-streams against TZ-27's set.json in the forensic store,
                      by the API with no token
    path              P-PATH: the run's own request path, with no token and held to the idle stretch, on
                      tz-01a-dataset's asset: the API and a download
    path-token        B-PATH-TOKEN, the Boss's block and nobody else's: the run's credential reads the repository,
                      with push, and the TZ-27 Release; nothing prints it
    installed         G-INSTALL: the service's three files, the two units and the empty state directory
    mark NAME         enable or retry: an instant and the archive's two units into state.json; start-svc: TZ-27's
    timer             G-TIMER: the timer as installed and enabled, and its next calendar elapse
    first             the first run after the enable mark, re-read: G-TRIGGER, G-RUN and the run's own readings;
                      exit 3 NOT YET
    final             G-UNIT, G-STILL and G-TIMER; the store and the next stop, projected
    still, started, scratch OWN, reclaim TREE...   TZ-27's own modes, unchanged

TZ-27's instrument, research/tz27-pairbook-archive.py, is loaded from beside this file and asserted by its SHA-256;
it installs its own audit hook, and every mode here sets that hook's mode and work tree before it acts. Every
request goes through TZ-27's GitHub class and build_request. No mode decompresses a stream file or prints a price,
a size, a side, a book's hash or an outcome. Run it with /root/tz04a-env, the pair book's interpreter; it needs the
standard library alone.

Written for CryptoTZ/TZ-28-pairbook-archive-timer.md. The TZ is the specification.
"""

import ast
import datetime
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
import urllib.parse

if not __debug__:
    sys.stderr.write("tz28: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(1)

HERE = os.path.dirname(os.path.abspath(__file__))
SELF_NAME = "tz28-pairbook-archive-timer.py"
TZ27_NAME = "tz27-pairbook-archive.py"
TZ27_SHA256 = "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673"


def load_tz27(path):
    """TZ-27's instrument, executed from the very bytes whose SHA-256 is asserted. It installs its audit hook."""
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
out = tz27.out

# ---- the TZ's constants: none of them is measured by this run -----------------------------------

MAP_REVISION = "2026-10-11-b"
MAP_ROWS = {"frozen": 34, "tracked": 2, "reported": 1}

STATE = "/var/lib/btc-pairbook-archive"
ASVC = "/root/btc-pairbook-archive-svc"
ARCHIVE = "btc-pairbook-archive.service"
TIMER = "btc-pairbook-archive.timer"
UNIT_DIR = "/etc/systemd/system"
RUN_ARGV = (tz27.PYTHON, "-B", "-u", ASVC + "/" + SELF_NAME, "run")
CALENDAR = "*-*-* 03:00:20 UTC"
CALENDAR_S = 3 * 3600 + 20       # the calendar elapse, seconds after 00:00 UTC
ACTIVE_S = 600                   # OnActiveSec: the first run, 600 s after the timer starts
TIMEOUT_S = 21600                # TimeoutStartSec of the service
ARCHIVE_MEMORY_MAX = 134217728   # MemoryMax=128M
EXIT_DEFERRED = 75
EXIT_NOT_STARTED = 2

WINDOW = tz27.WINDOW
IDLE = (15, 590)                 # every request starts at second 15 or later of a window, and is due to end by 590
RATE_FLOOR = 2000000             # bytes a second a transfer is budgeted at (TZ-28 section 1)
MARGIN_S = 5                     # seconds every request is budgeted beyond its bytes
KILL_BAND = (15, 470)            # the restart's SIGTERM: TZ-27's B-KILL-SVC band
RESTART_READ_S = 30              # the service's records are read 30 s after the SIGTERM, then every 10 s
RESTART_WAIT_S = 120             # until 120 s after it
DEFER_LIMIT = 3                  # the third deferral of one set halts the archive
DISK_FLOOR = 2001000000          # the recorder's floor, 2,000,000,000, plus 1,000,000 a run writes at most
RUN_MEM_FLOOR = 106086400        # MemAvailable: twice the run's measured peak (TZ-28 section 0.4)
PRE_DELETE = ("set", "upload", "verify")
TERMINAL = ("complete", "empty", "halt")

TAG_PREFIX = "pairbook-streams-"
TAG_RE = re.compile(r"pairbook-streams-[0-9]{10}")
IDLE_MAX_BYTES = (IDLE[1] - IDLE[0] - MARGIN_S) * RATE_FLOOR    # the largest file one idle stretch can carry

# G-TZ27: TZ-27's Release and its set, by the report of that TZ
TAG27 = "tz-27-pairbook-streams"
RELEASE27_ID = 409534533
SET27_PATH = "/root/btc-forensics/tz27-work--archive--set.json"
SET27_SHA256 = "ec71b1a7ce7db37ff29a49156006541dd5729c1df2c829c481eb64181228e4dd"
SET27_BYTES = 16570
SET27_N = 51
SET27_TOTAL = 678739504

LEDGER_KEYS = frozenset(("event", "run", "wall_ns"))
SHOW_ENV = {"TZ": "UTC", "LC_ALL": "C", "SYSTEMD_COLORS": "0", "SYSTEMD_PAGER": ""}
STAMP_RE = re.compile(r"[A-Z][a-z]{2} ([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}) UTC")

# ---- the clock: the idle stretch, the restart's band and the calendar -------------------------------


def phase_of(t):
    return int(t) % WINDOW


def budget_s(nbytes):
    """The seconds a request is held to: MARGIN_S, and its bytes at RATE_FLOOR, rounded up."""
    return MARGIN_S + -(-int(nbytes) // RATE_FLOOR)


def idle_wait(env, budget):
    """Until a second of the window at which a request of `budget` seconds starts at IDLE[0] or later and is due
    to end by IDLE[1]: the pair book's idle stretch, from its window.json at T+910 to its stream at T'+595."""
    assert 0 < budget <= IDLE[1] - IDLE[0], "a request budgeted %d s fits no idle stretch" % budget
    while True:
        now = env.time()
        p = phase_of(now)
        if IDLE[0] <= p <= IDLE[1] - budget:
            return now
        wait = IDLE[0] - p if p < IDLE[0] else WINDOW - p + IDLE[0]
        env.sleep(max(wait - (now - int(now)), 0.05))


def band_wait(env):
    """Until a second inside KILL_BAND of the window."""
    while True:
        now = env.time()
        p = phase_of(now)
        if KILL_BAND[0] <= p <= KILL_BAND[1]:
            return now
        wait = KILL_BAND[0] - p if p < KILL_BAND[0] else WINDOW - p + KILL_BAND[0]
        env.sleep(max(wait - (now - int(now)), 0.05))


def transfer_ok(t):
    """G-IDLE on one recorded request: (started inside the stretch its budget allows, ended by IDLE[1] of the
    window it started in)."""
    s = t["start_ns"] // 10 ** 9
    w0 = s // WINDOW * WINDOW
    return (IDLE[0] <= s - w0 <= IDLE[1] - t["budget_s"]), t["end_ns"] <= (w0 + IDLE[1]) * 10 ** 9


def next_calendar(now):
    """The first instant after now at 03:00:20 UTC."""
    d = int(now) // 86400 * 86400 + CALENDAR_S
    return d if d > now else d + 86400


def stamp_of(text):
    """An epoch from systemctl's own stamp, printed under TZ=UTC; None where it prints none."""
    m = STAMP_RE.fullmatch((text or "").strip())
    if m is None:
        return None
    dt = datetime.datetime.strptime(m.group(1), "%Y-%m-%d %H:%M:%S").replace(tzinfo=datetime.timezone.utc)
    return int(dt.timestamp())


def show_utc(unit, props):
    """systemctl show, every stamp printed in UTC and C locale."""
    args = ["systemctl", "show", unit]
    for prop in props:
        args += ["-p", prop]
    cp = subprocess.run(args, capture_output=True, text=True, env=dict(os.environ, **SHOW_ENV))
    assert cp.returncode == 0, "systemctl show %s: %s" % (unit, cp.stderr.strip())
    return dict(line.split("=", 1) for line in cp.stdout.split("\n") if "=" in line)

# ---- the run's record ------------------------------------------------------------------------------


class Ledger:
    """ledger.jsonl: one line a step of every run, appended and never rewritten."""

    def __init__(self, state):
        self.path = os.path.join(state, "ledger.jsonl")
        self.recs = self.read()

    def read(self):
        if not os.path.exists(self.path):
            return []
        with open(self.path, encoding="utf-8") as fh:
            return [json.loads(ln) for ln in fh if ln.strip()]

    def write(self, env, rec):
        rec = dict(rec, wall_ns=env.time_ns())
        assert LEDGER_KEYS <= frozenset(rec), "a ledger record without %r" % sorted(LEDGER_KEYS - frozenset(rec))
        tz27.forbid(rec, "ledger.jsonl")
        with open(self.path, "ab") as fh:
            fh.write((json.dumps(rec, sort_keys=True) + "\n").encode("utf-8"))
        self.recs.append(rec)
        out("L %s" % json.dumps(rec, sort_keys=True))
        return rec


def halted(recs):
    """True where the last halt is not followed by a clear, which only a TZ writes."""
    flags = [r["event"] for r in recs if r.get("event") in ("halt", "clear")]
    return bool(flags) and flags[-1] == "halt"


def pending(recs):
    """The run of the last start record, where that run has no terminal record; else None."""
    starts = [r for r in recs if r.get("event") == "start"]
    if not starts:
        return None
    a = starts[-1]["run"]
    return None if any(r.get("run") == a and r.get("event") in TERMINAL for r in recs) else a


def events(recs, a, name):
    return [r for r in recs if r.get("run") == a and r.get("event") == name]


def jsonl_append(path, rec, what):
    tz27.forbid(rec, what)
    with open(path, "ab") as fh:
        fh.write((json.dumps(rec, sort_keys=True) + "\n").encode("utf-8"))


def jsonl_read(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as fh:
        return [json.loads(ln) for ln in fh if ln.strip()]


# ---- what the run touches outside its own files ------------------------------------------------------


class Env:
    """The clock, systemd, the store and GitHub, as the unit's run meets them."""

    def __init__(self, work=STATE):
        self.root, self.state, self.work = tz27.ROOT, STATE, work
        self.wait_min, self.gap_s = tz27.WAIT_MIN_S, tz27.UPLOAD_GAP_S
        self.api, self.uploads, self.web = tz27.API_BASE, tz27.UPLOAD_BASE, tz27.WEB_BASE
        self.invocation = os.environ.get("INVOCATION_ID")
        self.commit, self.file_sha = None, None

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

    def show(self, unit, props):
        return tz27.systemctl_show(unit, props)

    def kill(self):
        return subprocess.run(["systemctl", "kill", "--signal=SIGTERM", tz27.UNIT]).returncode

    def unit_reads(self, n):
        return tz27.unit_reads(n)

    def disable_timer(self):
        return subprocess.run(["systemctl", "disable", "--now", TIMER]).returncode

    def credential(self):
        return tz27.credential()

    def free(self):
        return tz27.free_bytes()

    def mem(self):
        return tz27.mem_available()


def release_request(tag, commit, name, body):
    """The Release's creation: on the tag, at the commit the run's code is from, published, never the latest."""
    return {"tag_name": tag, "target_commitish": commit, "name": name, "body": body, "draft": False,
            "prerelease": False, "make_latest": "false"}


class Gh28(tz27.GitHub):
    """TZ-27's GitHub, every request held to the idle stretch and timed into the run's record."""

    def __init__(self, env, token=None, record=None):
        super().__init__(token, env.api, env.uploads, env.web)
        self.env, self.record, self.sizes = env, record, {}
        self.gap_s = env.gap_s

    def _timed(self, kind, name, nbytes, fn):
        budget = budget_s(nbytes)
        idle_wait(self.env, budget)
        t0, ok = self.env.time_ns(), False
        try:
            res = fn()
            ok = True
            return res
        finally:
            if self.record is not None:
                self.record({"kind": kind, "name": name, "bytes": int(nbytes), "budget_s": budget, "start_ns": t0,
                             "end_ns": self.env.time_ns(), "ok": ok})

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
        assert self.token is not None and self.env.commit is not None
        self.pace()
        status, doc, _h = self._json("POST", "%s/repos/%s/releases" % (self.api, tz27.REPO),
                                     release_request(tag, self.env.commit, name, body))
        assert status == 201 and isinstance(doc, dict), "create release %s: status %r" % (tag, status)
        return doc

# ---- the set -----------------------------------------------------------------------------------------


def set_document(tag, a, root, assets, windows, deferred):
    """TZ-27's set document under this TZ's tag, which TZ-27's own tag rule does not cover, and with every file
    small enough for one idle stretch."""
    names = [x["asset"] for x in assets]
    assert TAG_RE.fullmatch(tag) and tz27.TAG_RE.fullmatch(tag) is None, "a tag named %r" % tag
    assert assets, "no stream file of a closed window"
    assert len(set(names)) == len(names), "two assets share a name"
    assert all(tz27.ASSET_RE.fullmatch(n) for n in names), "an asset name outside %s" % tz27.ASSET_RE.pattern
    assert len(assets) <= tz27.RUN_MAX_ASSETS, "%d assets, above %d" % (len(assets), tz27.RUN_MAX_ASSETS)
    big = [x["asset"] for x in assets if x["bytes"] > IDLE_MAX_BYTES]
    assert not big, "files above the %d bytes one idle stretch carries: %r" % (IDLE_MAX_BYTES, big[:3])
    doc = {"tag": tag, "as_of": a, "root": root, "repo": tz27.REPO, "assets": assets, "assets_n": len(assets),
           "bytes_total": sum(x["bytes"] for x in assets), "first_T": assets[0]["T"], "last_T": assets[-1]["T"],
           "windows": windows, "deferred": deferred}
    tz27.assert_keys(doc, tz27.SET_KEYS, "set.json")
    for x in assets:
        tz27.assert_keys(x, tz27.SET_ASSET_KEYS, "set.json asset")
        assert tz27.SHA_RE.fullmatch(x["sha256"])
    for w in windows:
        tz27.assert_keys(w, tz27.SET_WINDOW_KEYS, "set.json window")
    return doc


def release_text(doc, commit):
    name = "%s: the pair book's streams, windows %d to %d" % (doc["tag"], doc["first_T"], doc["last_T"])
    body = ("Verbatim stream files of btc-pairbook.service (research/tz26-nesting-b3-capture.py), one asset per file, "
            "named <T>-<file>: the market websocket's frames for the four books of btc-updown-15m-{T} and "
            "btc-updown-5m-{T+600}, T+595 to T+905. %d files, %d bytes, windows %d to %d, taken as of %d by "
            "btc-pairbook-archive.service at commit %s (research/tz28-pairbook-archive-timer.py, TZ-28). Reserved "
            "for B3's measurement: no TZ reads them before M0's second look has reported (CANON PART II). Each "
            "asset's SHA-256 is its digest here." % (doc["assets_n"], doc["bytes_total"], doc["first_T"],
                                                     doc["last_T"], doc["as_of"], commit))
    return name, body


def window_json(root, T):
    path = os.path.join(root, str(T), "window.json")
    if not os.path.exists(path):
        return None
    with open(path, "rb") as fh:
        wj = json.loads(fh.read())
    s = wj.get("stream") if isinstance(wj.get("stream"), dict) else {}
    out("window %d: pid %s, documents %s; stream opened %s, off_reason %s, files %s, segments %s, frames %s, "
        "stored_bytes %s" % (T, wj.get("pid"), wj.get("documents_ok"), s.get("opened"), s.get("off_reason"),
                             s.get("files"), s.get("segments"), s.get("frames"), s.get("stored_bytes")))
    return wj

# ---- the run: its phases -------------------------------------------------------------------------------


def floors(env):
    mem, free = env.mem(), env.free()
    out("MemAvailable %d bytes, floor %d; free %d bytes, floor %d" % (mem, RUN_MEM_FLOOR, free, DISK_FLOOR))
    assert mem >= RUN_MEM_FLOOR, "MemAvailable %d bytes, below %d" % (mem, RUN_MEM_FLOOR)
    assert free >= DISK_FLOOR, "free %d bytes, below %d" % (free, DISK_FLOOR)


def new_set(env, led, a, rdir):
    tz27.MODE[0] = "inventory"
    assets, windows, deferred, open_n = tz27.inventory(env.root, a)
    for w in windows:
        out("W %d %s %-8s stream files %d, %d bytes, taken %d" % (w["T"], tz27.utc(w["T"]), w["disposition"],
                                                               w["streams"], w["stream_bytes"], w["taken"]))
    counts = {"windows_considered": len(windows), "open": open_n, "deferred": deferred,
              "closed": sum(1 for w in windows if w["disposition"] == "closed"),
              "unclosed": sum(1 for w in windows if w["disposition"] == "unclosed")}
    if not assets:
        led.write(env, dict({"event": "empty", "run": a}, **counts))
        return None
    doc = set_document(TAG_PREFIX + str(a), a, env.root, assets, windows, deferred)
    for x in assets:
        out("S %s %d %s" % (x["asset"], x["bytes"], x["sha256"]))
    raw = tz27.json_bytes(doc)
    with open(os.path.join(rdir, "set.json"), "wb") as fh:
        fh.write(raw)
    led.write(env, dict({"event": "set", "run": a, "tag": doc["tag"], "sha256": tz27.sha256_bytes(raw),
                         "assets_n": doc["assets_n"], "bytes_total": doc["bytes_total"], "first_T": doc["first_T"],
                         "last_T": doc["last_T"]}, **counts))
    return doc


def load_set(led, a, rdir):
    """The pending run's set, asserted by the SHA-256 its set record carries; None where it has none yet."""
    recs = events(led.recs, a, "set")
    if not recs:
        return None
    with open(os.path.join(rdir, "set.json"), "rb") as fh:
        raw = fh.read()
    assert tz27.sha256_bytes(raw) == recs[-1]["sha256"], "set.json is not the set its record names"
    return json.loads(raw)


def transfers_logger(rdir):
    path = os.path.join(rdir, "transfers.jsonl")
    return lambda rec: jsonl_append(path, rec, "transfers.jsonl")


def upload_phase(env, led, a, rdir, doc):
    tz27.MODE[0] = "upload"
    tok, source = env.credential()
    out("credential: %s" % source)
    gh = Gh28(env, tok, transfers_logger(rdir))
    rel = gh.release_by_tag(doc["tag"])
    created = rel is None
    if created:
        rel = gh.create_release(doc["tag"], *release_text(doc, env.commit))
        out("created the Release on %s, id %s" % (doc["tag"], rel.get("id")))
    assert rel.get("tag_name") == doc["tag"] and rel.get("draft") is False, "the Release is not published on the tag"
    path = os.path.join(rdir, "upload.jsonl")

    def log(rec):
        rec = dict(rec, at=tz27.utc(env.time()))
        jsonl_append(path, rec, "upload.jsonl")
        out("U %s" % json.dumps(rec, sort_keys=True))

    sent, held = tz27.upload_set(gh, rel, doc, env.root, log, wait_min=env.wait_min)
    log({"action": "complete", "assets": sent + held, "sent": sent, "held": held, "release_id": int(rel["id"]),
         "credential": source, "wall_ns": env.time_ns()})
    led.write(env, {"event": "upload", "run": a, "release_id": int(rel["id"]), "created": created, "sent": sent,
                    "held": held, "credential": source})


def verify_phase(env, led, a, rdir, doc):
    tz27.MODE[0] = "verify"
    records = jsonl_read(os.path.join(rdir, "upload.jsonl"))
    assert records and records[-1].get("action") == "complete" and records[-1].get("assets") == doc["assets_n"], \
        "verify: upload has not completed the set"
    ready_ns = records[-1]["wall_ns"] + tz27.UPLOAD_SETTLE_S * 10 ** 9
    while tz27.upload_ready(records, doc["assets_n"], env.time_ns()) is not None:
        env.sleep((ready_ns - env.time_ns()) / 1e9 + 0.5)
    anon = Gh28(env, None, transfers_logger(rdir))
    anon.sizes = {x["asset"]: x["bytes"] for x in doc["assets"]}
    rel, rows, missing, extra = tz27.verify_release(anon, doc["tag"], doc)
    for r in rows:
        out("V %s id %s state %s api %s bytes %s digest %s url %s download %s" % (
            r["asset"], r["id"], r["state"], r["api_ok"], r["api_bytes"], r["digest"], r["url_ok"], r["download_ok"]))
    checks = tz27.release_reading(rel, doc["tag"], rows, missing, extra)
    for k, v in checks.items():
        out("G-UPLOAD/G-DOWNLOAD %-52s %s" % (k, v))
    assert all(checks.values()), "VERIFY FAIL: %r; missing %r; beyond %r" % (
        sorted(k for k, v in checks.items() if not v), missing[:5], extra[:5])
    vdoc = {"tag": doc["tag"], "release_id": int(rel["id"]), "set_sha256": tz27.sha256_bytes(tz27.json_bytes(doc)),
            "assets": rows, "assets_n": len(rows), "bytes_total": sum(r["download_bytes"] for r in rows)}
    tz27.assert_keys(vdoc, tz27.VERIFY_KEYS, "verify.json")
    for r in rows:
        tz27.assert_keys(r, tz27.VERIFY_ROW_KEYS, "verify.json row")
    vraw = tz27.json_bytes(vdoc)
    with open(os.path.join(rdir, "verify.json"), "wb") as fh:
        fh.write(vraw)
    led.write(env, {"event": "verify", "run": a, "release_id": int(rel["id"]), "assets_n": len(rows),
                    "bytes_total": vdoc["bytes_total"], "verify_sha256": tz27.sha256_bytes(vraw)})
    return tz27.sha256_bytes(vraw)


def delete_phase(env, led, a, rdir, doc, vsha):
    tz27.MODE[0] = "delete"
    with open(os.path.join(rdir, "verify.json"), "rb") as fh:
        assert tz27.sha256_bytes(fh.read()) == vsha, "delete: verify.json is not this run's"
    path = os.path.join(rdir, "delete.jsonl")

    def log(row):
        jsonl_append(path, row, "delete.jsonl")
        out("X %s %d %s removed" % (row["asset"], row["bytes"], row["sha256"]))

    done = {r["asset"] for r in jsonl_read(path)}
    free_before = env.free()
    _rows, removed, freed, already = tz27.delete_set(env.root, doc, done, int(env.time()), log)
    checks, gone, kept = tz27.removed_reading(env.root, doc, {r["asset"] for r in jsonl_read(path)})
    for k, v in checks.items():
        out("G-DELETE %-36s %s" % (k, v))
    assert all(checks.values()), "REMOVED FAIL: %r" % sorted(k for k, v in checks.items() if not v)
    led.write(env, {"event": "delete", "run": a, "removed": removed, "already": already, "freed": freed,
                    "gone": gone, "windows_kept": kept, "free_before": free_before, "free_after": env.free()})


def restart_phase(env, led, a, doc):
    tz27.MODE[0] = "restart"
    band_wait(env)
    kv = env.show(tz27.UNIT, ["MainPID", "NRestarts", "ActiveState"])
    assert kv.get("ActiveState") == "active", "the pair book is %r: not restarted" % kv.get("ActiveState")
    mark = {"ns": env.time_ns(), "MainPID": kv["MainPID"], "NRestarts": kv["NRestarts"],
            "ActiveState": kv["ActiveState"]}
    p = phase_of(mark["ns"] // 10 ** 9)
    assert KILL_BAND[0] <= p <= KILL_BAND[1], "the mark at second %d, outside the band" % p
    led.write(env, {"event": "mark", "run": a, "mark": mark, "phase": p})
    rc = env.kill()
    led.write(env, {"event": "kill", "run": a, "exit": rc, "phase": phase_of(env.time())})
    assert rc == 0, "systemctl kill: exit %r" % rc
    deadline = env.time() + RESTART_WAIT_S
    env.sleep(RESTART_READ_S)
    while True:
        recs = tz27.read_runtime(os.path.join(env.root, "runtime.jsonl"))
        checks, stop, start, _after = tz27.restart_reading(recs, mark)
        if all(checks.values()) or env.time() >= deadline:
            break
        env.sleep(10)
    for k, v in checks.items():
        out("G-RESTART %-30s %s" % (k, v))
    assert all(checks.values()), "G-RESTART FAIL: %r" % sorted(k for k, v in checks.items() if not v)
    c, W, view, left = tz27.counter_reading(env.root, start, doc)
    for k, v in c.items():
        out("G-COUNTER %-40s %s" % (k, v))
    assert all(c.values()), "G-COUNTER FAIL: %r; left %r" % (sorted(k for k, v in c.items() if not v), left[:5])
    kvu, uchecks, pid = env.unit_reads(int(mark["NRestarts"]) + 1)
    uchecks = dict(uchecks, **{"the new start's process": pid == start.get("pid")})
    for k, v in uchecks.items():
        out("G-UNIT %-24s %s" % (k, v))
    assert all(uchecks.values()), "G-UNIT FAIL: %r" % sorted(k for k, v in uchecks.items() if not v)
    led.write(env, {"event": "restart", "run": a, "W": W, "pid": start["pid"], "stopped": stop["pid"],
                    "gap_ns": start["wall_ns"] - stop["wall_ns"], "stream_bytes": view,
                    "free_bytes": start.get("free_bytes"), "NRestarts": kvu.get("NRestarts")})
    return W, start["pid"]


def resume_phase(env, led, a, W, pid):
    tz27.MODE[0] = "resume"
    while True:
        reading, T, checks = tz27.resume_decision(W, pid, int(env.time()), lambda t: window_json(env.root, t))
        if reading != "NOT YET":
            break
        env.sleep(T + tz27.CLOSE_OFFSET + tz27.RESUME_AFTER_S - env.time() + 1)
    for k, v in checks.items():
        out("G-RESUME %-30s %s" % (k, v))
    led.write(env, {"event": "resume", "run": a, "reading": reading, "T": T})
    assert reading != "FAIL", "G-RESUME FAIL at window %d" % T


def final_phase(env, led, a, rdir, doc):
    tz27.MODE[0] = "final"
    trs = jsonl_read(os.path.join(rdir, "transfers.jsonl"))
    idle = [transfer_ok(t) for t in trs]
    counter, free = tz27.stream_bytes_view(env.root), env.free()
    rate, rows = tz27.projection(doc["bytes_total"], doc["first_T"], doc["last_T"], counter, free, int(env.time()))
    for what, d, when in rows:
        out("at the set's rate %s stops the streams in %s days, at %s" % (what, tz27.decimals(d, 2), tz27.utc(when)))
    led.write(env, {"event": "complete", "run": a, "assets_n": doc["assets_n"], "bytes_total": doc["bytes_total"],
                    "requests": len(trs), "started_outside": sum(1 for s, _e in idle if not s),
                    "ended_outside": sum(1 for _s, e in idle if not e), "store_stream_bytes": counter,
                    "free_bytes": free, "rate_per_day": int(rate), "stops": [[w, int(t)] for w, _d, t in rows],
                    "peak_rss": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024})


def halt(env, led, a, phase, reason):
    led.write(env, {"event": "halt", "run": a, "phase": phase, "reason": reason[:400]})
    tz27.MODE[0] = "final"
    rc = env.disable_timer()
    led.write(env, {"event": "timer-disabled", "run": a, "exit": rc})
    out("HALTED in %s: %s; the timer disabled, exit %r" % (phase, reason[:400], rc))
    return 1


def run(env):
    """One run: the pending set resumed, or a new one as of now; exit 0, EXIT_DEFERRED or 1."""
    tz27.WORK[0], tz27.MODE[0] = env.work, "run"
    led = Ledger(env.state)
    if halted(led.recs):
        last = [r for r in led.recs if r.get("event") == "halt"][-1]
        out("HALTED since run %s, %s: %s; nothing done" % (last.get("run"), last.get("phase"), last.get("reason")))
        tz27.MODE[0] = "final"
        rc = env.disable_timer()
        led.write(env, {"event": "refused", "run": last.get("run"), "exit": rc})
        return 1
    a = pending(led.recs)
    resumed = a is not None
    if not resumed:
        a = max([int(env.time())] + [r["run"] + 1 for r in led.recs if r.get("event") == "start"])
    rdir = os.path.join(env.state, "runs", str(a))
    os.makedirs(rdir, exist_ok=True)
    led.write(env, {"event": "start", "run": a, "resumed": resumed, "commit": env.commit, "file_sha256": env.file_sha,
                    "tz27_sha256": TZ27_SHA256, "invocation": env.invocation, "phase_at": phase_of(env.time())})
    phase = "set"
    try:
        floors(env)
        doc = load_set(led, a, rdir)
        if doc is None:
            doc = new_set(env, led, a, rdir)
            if doc is None:
                out("EMPTY: no stream file of a closed window as of %d" % a)
                return 0
        if not events(led.recs, a, "delete"):
            phase = "upload"
            upload_phase(env, led, a, rdir, doc)
            phase = "verify"
            vsha = verify_phase(env, led, a, rdir, doc)
            phase = "delete"
            delete_phase(env, led, a, rdir, doc, vsha)
        phase = "restart"
        if events(led.recs, a, "restart"):
            r = events(led.recs, a, "restart")[-1]
            W, pid = r["W"], r["pid"]
        else:
            W, pid = restart_phase(env, led, a, doc)
        phase = "resume"
        if not events(led.recs, a, "resume"):
            resume_phase(env, led, a, W, pid)
        phase = "final"
        final_phase(env, led, a, rdir, doc)
        out("COMPLETE: run %d, %d files, %d bytes, Release %s" % (a, doc["assets_n"], doc["bytes_total"],
                                                                 doc["tag"]))
        return 0
    except tz27.GuardError as exc:
        return halt(env, led, a, phase, "GuardError: %s" % exc)
    except Exception as exc:
        reason = "%s: %s" % (type(exc).__name__, str(exc))
        if phase not in PRE_DELETE:
            return halt(env, led, a, phase, reason)
        n = len(events(led.recs, a, "deferred")) + 1
        if n >= DEFER_LIMIT:
            return halt(env, led, a, phase, "deferral %d of %d: %s" % (n, DEFER_LIMIT, reason))
        led.write(env, {"event": "deferred", "run": a, "phase": phase, "reason": reason[:400], "count": n})
        out("DEFERRED in %s, %d of %d: %s; nothing removed, the next run resumes this set" % (
            phase, n, DEFER_LIMIT, reason[:400]))
        return EXIT_DEFERRED


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
        return EXIT_NOT_STARTED
    out("run: pid %d, commit %s, file sha256 %s, invocation %s" % (os.getpid(), env.commit, env.file_sha,
                                                                   env.invocation))
    return run(env)

# ---- the deployment's readings: the session's modes ------------------------------------------------------


def mode_fingerprint():
    tz27.MODE[0] = "fingerprint"
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


def mode_tz27_release():
    """G-TZ27: TZ-27's Release, read anonymously through the API, against the set.json TZ-27 froze."""
    tz27.MODE[0] = "tz27-release"
    tz27.floor_check()
    with open(SET27_PATH, "rb") as fh:
        raw = fh.read()
    assert len(raw) == SET27_BYTES and tz27.sha256_bytes(raw) == SET27_SHA256, "%s is not TZ-27's set" % SET27_PATH
    doc = json.loads(raw)
    assert doc["tag"] == TAG27 and doc["assets_n"] == SET27_N and doc["bytes_total"] == SET27_TOTAL, "TZ-27's set"
    rel, rows, missing, extra = tz27.verify_release(tz27.GitHub(), TAG27, doc, download=False)
    for r in rows:
        out("V %s id %s state %s bytes %s digest %s url %s: %s" % (r["asset"], r["id"], r["state"], r["api_bytes"],
                                                                  r["digest"], r["url_ok"], r["api_ok"]))
    checks = {k: v for k, v in tz27.release_reading(rel, TAG27, rows, missing, extra).items()
              if not k.startswith("every download")}
    checks["the Release TZ-27 created"] = rel is not None and rel.get("id") == RELEASE27_ID
    for k, v in checks.items():
        out("G-TZ27 %-52s %s" % (k, v))
    if missing or extra:
        out("missing %r; beyond the set %r" % (missing[:10], extra[:10]))
    assert all(checks.values()), "G-TZ27 FAIL: %r" % sorted(k for k, v in checks.items() if not v)
    out("G-TZ27 PASS: Release %d on %s, %d of %d assets uploaded with the set's bytes and digest, nothing beyond "
        "the set; %d requests" % (RELEASE27_ID, TAG27, sum(r["api_ok"] for r in rows), SET27_N,
                                  tz27.COUNTERS["requests"]))


def session_env():
    env = Env(work=tz27.WORK[0])
    return env


def mode_path():
    """P-PATH: the run's own Gh28, with no token, on the asset whose bytes map 2.1 fixes: 3 requests."""
    tz27.MODE[0] = "path"
    tz27.floor_check()
    env = session_env()
    trs = []
    gh = Gh28(env, None, trs.append)
    gh.sizes[tz27.PATH_ASSET] = tz27.PATH_BYTES
    rel = gh.release_by_tag(tz27.PATH_TAG)
    assert rel is not None, "P-PATH: no release on %s" % tz27.PATH_TAG
    a = {x.get("name"): x for x in gh.assets(int(rel["id"]))}.get(tz27.PATH_ASSET)
    url = gh.download_url(tz27.PATH_TAG, tz27.PATH_ASSET)
    row = tz27.asset_row({"asset": tz27.PATH_ASSET, "bytes": tz27.PATH_BYTES, "sha256": tz27.PATH_SHA256}, a, url)
    out("P-PATH release %s id %s; asset %s state %s, %s bytes, digest %s, url %s" % (
        tz27.PATH_TAG, rel.get("id"), tz27.PATH_ASSET, row["state"], row["api_bytes"], row["digest"], row["url_ok"]))
    assert row["api_ok"], "P-PATH: the API's record of %s is not the map's" % tz27.PATH_ASSET
    status, n, h = tz27.download_checked(gh, url)
    out("P-PATH download: status %r, %d bytes, sha256 %s" % (status, n, h))
    assert status == 200 and n == tz27.PATH_BYTES and h == tz27.PATH_SHA256, "P-PATH: not the map's bytes"
    for t in trs:
        s, e = transfer_ok(t)
        out("T %s %s: %d bytes, budget %d s, second %d, %.1f s, inside %s %s" % (
            t["kind"], t["name"], t["bytes"], t["budget_s"], phase_of(t["start_ns"] // 10 ** 9),
            (t["end_ns"] - t["start_ns"]) / 1e9, s, e))
    assert len(trs) == 3 and all(all(transfer_ok(t)) for t in trs), "P-PATH: a request outside the idle stretch"
    out("READING P-PATH: served - 3 requests through the run's own path, each inside the idle stretch; the digest "
        "present and equal; %d bytes downloaded and equal" % n)


def mode_path_token():
    """B-PATH-TOKEN: the Boss's. The run's credential, as the run reads it; nothing prints it."""
    tz27.MODE[0] = "upload"
    tz27.floor_check()
    tok, source = tz27.credential()
    out("credential: %s" % source)
    assert source == "the primary checkout's remote URL", "P-TOKEN: the run reads the remote URL's credential, not %s" % (
        source,)
    env = session_env()
    gh = Gh28(env, tok, None)
    status, doc, _h = gh._json("GET", "%s/repos/%s" % (gh.api, tz27.REPO))
    perms = (doc or {}).get("permissions") if isinstance(doc, dict) else None
    out("repository: status %r, full_name %r, push %r" % (status, (doc or {}).get("full_name") if isinstance(doc, dict)
                                                           else None, (perms or {}).get("push")))
    assert status == 200 and doc.get("full_name") == tz27.REPO and (perms or {}).get("push") is True, \
        "P-TOKEN: the credential does not write this repository"
    rel = gh.release_by_tag(TAG27)
    assert rel is not None and rel.get("id") == RELEASE27_ID, "P-TOKEN: the Release on %s" % TAG27
    out("READING P-TOKEN: served - the credential from %s reads %s with push, and the Release %d; %d requests" % (
        source, tz27.REPO, RELEASE27_ID, tz27.COUNTERS["requests"]))


def git_out(*args):
    cp = subprocess.run(["git"] + list(args), capture_output=True, text=True)
    assert cp.returncode == 0, "git %s: exit %d" % (" ".join(args), cp.returncode)
    return cp.stdout.strip()


def mode_installed():
    """G-INSTALL: what B-INSTALL put on the host, against the branch's worktree."""
    tz27.MODE[0] = "installed"
    wt = tz27.wpath("wt")
    head, up = git_out("-C", wt, "rev-parse", "HEAD"), git_out("-C", wt, "rev-parse", "@{u}")
    with open(os.path.join(ASVC, "commit.txt"), encoding="utf-8") as fh:
        commit = fh.read().strip()
    files = {}
    for name in (SELF_NAME, TZ27_NAME):
        files[name] = (tz27.sha256_file(os.path.join(ASVC, name))[0],
                       tz27.sha256_file(os.path.join(wt, "research", name))[0])
    units = {}
    for name in (ARCHIVE, TIMER):
        with open(os.path.join(UNIT_DIR, name), "rb") as a_:
            installed = a_.read()
        with open(os.path.join(wt, "deploy", "systemd", name), "rb") as b_:
            units[name] = installed == b_.read()
    st = os.stat(STATE)
    svc = show_utc(ARCHIVE, ["LoadState", "ActiveState", "UnitFileState", "FragmentPath", "Type", "Restart",
                             "MemoryMax", "TimeoutStartUSec", "WorkingDirectory", "ExecStart"])
    tmr = show_utc(TIMER, ["LoadState", "ActiveState", "UnitFileState", "FragmentPath"])
    argv = "argv[]=%s ;" % " ".join(RUN_ARGV)
    checks = {"commit.txt the branch head, pushed": commit == head == up,
              "the service's copy of this file the branch's": files[SELF_NAME][0] == files[SELF_NAME][1],
              "the service's copy of TZ-27's file, %s" % TZ27_SHA256[:12]: files[TZ27_NAME][0] == files[TZ27_NAME][1]
              == TZ27_SHA256,
              "the two units byte for byte": all(units.values()),
              "the state directory, root's, 0700, empty": os.path.isdir(STATE) and st.st_uid == 0
              and (st.st_mode & 0o777) == 0o700 and not os.listdir(STATE),
              "the service loaded, inactive, static": (svc["LoadState"], svc["ActiveState"], svc["UnitFileState"])
              == ("loaded", "inactive", "static"),
              "the service a oneshot, Restart=no, 128M, 6h, its argv and directory": svc["Type"] == "oneshot"
              and svc["Restart"] == "no" and svc["MemoryMax"] == str(ARCHIVE_MEMORY_MAX)
              and svc["TimeoutStartUSec"] == "6h" and svc["WorkingDirectory"] == STATE and argv in svc["ExecStart"]
              and svc["FragmentPath"] == UNIT_DIR + "/" + ARCHIVE,
              "the timer loaded, inactive, disabled": (tmr["LoadState"], tmr["ActiveState"], tmr["UnitFileState"],
                                                       tmr["FragmentPath"]) == ("loaded", "inactive", "disabled",
                                                                                UNIT_DIR + "/" + TIMER)}
    for name, (a_, b_) in sorted(files.items()):
        out("%s/%s sha256 %s; the branch's %s" % (ASVC, name, a_, b_))
    out("commit.txt %s; the branch head %s, its upstream %s" % (commit, head, up))
    for k, v in checks.items():
        out("G-INSTALL %-66s %s" % (k, v))
    assert all(checks.values()), "G-INSTALL FAIL: %r" % sorted(k for k, v in checks.items() if not v)
    out("G-INSTALL PASS: %d of %d" % (len(checks), len(checks)))


def mode_mark(name):
    if name == "start-svc":
        tz27.MODE[0] = "mark"
        return tz27.mode_mark(name)
    assert name in ("enable", "retry"), "mark %r" % name
    tz27.MODE[0] = "mark"
    st = tz27.load_state()
    marks = st.setdefault("marks28", {})
    assert name not in marks, "mark %s already taken" % name
    tmr = show_utc(TIMER, ["ActiveState", "UnitFileState"])
    svc = show_utc(ARCHIVE, ["ActiveState", "Result"])
    marks[name] = {"ns": time.time_ns(), "timer": tmr, "service": svc}
    tz27.save_state(st)
    out("mark %s at %s: the timer %r, the service %r" % (name, tz27.utc(marks[name]["ns"] / 1e9), tmr, svc))


def timer_reading(now):
    kv = show_utc(TIMER, ["LoadState", "ActiveState", "SubState", "UnitFileState", "FragmentPath", "Unit",
                          "TimersCalendar", "TimersMonotonic", "NextElapseUSecRealtime", "AccuracyUSec",
                          "LastTriggerUSec", "ActiveEnterTimestamp"])
    nxt = stamp_of(kv.get("NextElapseUSecRealtime"))
    checks = {"loaded": kv["LoadState"] == "loaded",
              "active": kv["ActiveState"] == "active" and kv["SubState"] in ("waiting", "running"),
              "enabled": kv["UnitFileState"] == "enabled",
              "fragment": kv["FragmentPath"] == UNIT_DIR + "/" + TIMER,
              "its unit": kv["Unit"] == ARCHIVE,
              "the calendar": ("OnCalendar=%s ;" % CALENDAR) in kv["TimersCalendar"],
              "600 s after it starts": "OnActiveUSec=10min" in kv["TimersMonotonic"],
              "accuracy 1 s": kv["AccuracyUSec"] == "1s",
              "the next calendar elapse": nxt == next_calendar(now)}
    return kv, checks, nxt


def mode_timer():
    tz27.MODE[0] = "timer"
    now = time.time()
    kv, checks, nxt = timer_reading(now)
    out("the timer: %r" % kv)
    for k, v in checks.items():
        out("G-TIMER %-24s %s" % (k, v))
    assert all(checks.values()), "G-TIMER FAIL: %r" % sorted(k for k, v in checks.items() if not v)
    out("G-TIMER PASS: the next calendar run at %s, the run after the start at %s" % (
        tz27.utc(nxt), tz27.utc((stamp_of(kv.get("ActiveEnterTimestamp")) or 0) + ACTIVE_S)))


def first_run(recs, since_ns):
    """The run of the first start record at or after since_ns, and every record of that run."""
    starts = [r for r in recs if r.get("event") == "start" and r["wall_ns"] >= since_ns]
    if not starts:
        return None, []
    a = starts[0]["run"]
    return a, [r for r in recs if r.get("run") == a]


def mode_first():
    """The first run after the enable mark, re-read from its records, the store, the service's record, systemd and
    the Release: exit 3 while it has not ended."""
    tz27.MODE[0] = "final"
    st = tz27.load_state()
    mark = st.get("marks28", {}).get("enable")
    assert mark is not None, "first: no enable mark"
    svc = show_utc(ARCHIVE, ["ActiveState", "Result", "ExecMainStatus", "ExecMainStartTimestamp",
                             "ExecMainExitTimestamp", "InvocationID"])
    recs = Ledger(STATE).recs
    a, mine = first_run(recs, mark["ns"])
    if a is None or svc["ActiveState"] in ("activating", "active", "deactivating"):
        out("NOT YET: %s; the service %s" % ("no run since the mark" if a is None else "run %d" % a,
                                              svc["ActiveState"]))
        return 3
    for r in mine:
        out("R %s" % json.dumps(r, sort_keys=True))
    out("run %d: %d records, %s" % (a, len(mine), [r["event"] for r in mine]))
    terms = [r["event"] for r in mine if r["event"] in TERMINAL]
    if not terms:
        last = mine[-1]["event"]
        out("READING G-RUN: %s - the run's last record %s, in its phase %r" % (
            "DEFERRED" if last == "deferred" else "INTERRUPTED", last, mine[-1].get("phase")))
        return 1
    last = terms[-1]
    readings = {}
    tmr = show_utc(TIMER, ["LastTriggerUSec", "ActiveEnterTimestamp"])
    trig, enter = stamp_of(tmr.get("LastTriggerUSec")), stamp_of(tmr.get("ActiveEnterTimestamp"))
    s0 = mine[0]["wall_ns"] // 10 ** 9
    readings["G-TRIGGER"] = (trig is not None and enter is not None and abs(trig - (enter + ACTIVE_S)) <= 2
                             and trig <= s0 <= trig + 60)
    out("G-TRIGGER: the timer started %s, triggered %s, the run's first record %s" % (
        tz27.utc(enter or 0), tz27.utc(trig or 0), tz27.utc(s0)))
    readings["G-RUN"] = last == "complete" and svc["Result"] == "success" and svc["ExecMainStatus"] == "0"
    out("G-RUN: the run %s; the service's last invocation %s, Result %s, ExecMainStatus %s, %s to %s" % (
        last, svc["InvocationID"], svc["Result"], svc["ExecMainStatus"], svc["ExecMainStartTimestamp"],
        svc["ExecMainExitTimestamp"]))
    if last == "complete":
        rdir = os.path.join(STATE, "runs", str(a))
        with open(os.path.join(rdir, "set.json"), "rb") as fh:
            raw = fh.read()
        sets = [r for r in mine if r["event"] == "set"]
        doc = json.loads(raw)
        readings["G-SET"] = len(sets) == 1 and tz27.sha256_bytes(raw) == sets[0]["sha256"] and \
            set_document(doc["tag"], doc["as_of"], doc["root"], doc["assets"], doc["windows"], doc["deferred"]) == doc
        for w in doc["windows"]:
            out("W %d %s %-8s stream files %d, %d bytes, taken %d" % (w["T"], tz27.utc(w["T"]), w["disposition"],
                                                                   w["streams"], w["stream_bytes"], w["taken"]))
        for x in doc["assets"]:
            out("S %s %d %s" % (x["asset"], x["bytes"], x["sha256"]))
        out("G-SET: %d files, %d bytes, windows %d to %d, as of %d, deferred %d; set.json sha256 %s" % (
            doc["assets_n"], doc["bytes_total"], doc["first_T"], doc["last_T"], doc["as_of"], doc["deferred"],
            tz27.sha256_bytes(raw)))
        rel, rows, missing, extra = tz27.verify_release(tz27.GitHub(), doc["tag"], doc, download=False)
        up = tz27.release_reading(rel, doc["tag"], rows, missing, extra)
        obj, peeled = tz27.ls_remote_tag(doc["tag"])
        started = [r for r in mine if r["event"] == "start"]
        readings["G-UPLOAD"] = all(v for k, v in up.items() if not k.startswith("every download")) and \
            obj == started[0]["commit"] and peeled is None
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
        drecs = jsonl_read(os.path.join(rdir, "delete.jsonl"))
        done = {r["asset"] for r in drecs}
        aby, vby = {r["asset"]: r for r in rows}, {r["asset"]: r for r in vdoc["assets"]}
        dby = {r["asset"]: r for r in drecs}
        for x in doc["assets"]:
            out("ROW %s %d %s digest %s download %s removed %s" % (
                x["asset"], x["bytes"], x["sha256"], aby.get(x["asset"], {}).get("digest"),
                vby.get(x["asset"], {}).get("download_sha256"), dby.get(x["asset"], {}).get("sha256")))
        dchecks, gone, kept = tz27.removed_reading(tz27.ROOT, doc, done)
        readings["G-DELETE"] = all(dchecks.values())
        out("G-DELETE: %r; %d gone, %d removals recorded, %d windows kept" % (dchecks, gone, len(done), kept))
        mk = [r for r in mine if r["event"] == "mark"][-1]["mark"]
        rr = tz27.read_runtime(tz27.ROOT + "/runtime.jsonl")
        rchecks, stop, start, _after = tz27.restart_reading(rr, mk)
        readings["G-RESTART"] = all(rchecks.values())
        out("G-RESTART: %r; the stop of %s at second %d, the start of %s %.3f s later" % (
            rchecks, stop.get("pid"), phase_of(stop.get("wall_ns", 0) // 10 ** 9), start.get("pid"),
            (start.get("wall_ns", 0) - stop.get("wall_ns", 0)) / 1e9))
        cchecks, W, view, _left = tz27.counter_reading(tz27.ROOT, start, doc)
        readings["G-COUNTER"] = all(cchecks.values()) and start.get("stream_bytes") == view
        out("G-COUNTER: %r; stream_bytes %s, the store's windows up to %d %d bytes" % (
            cchecks, start.get("stream_bytes"), W - WINDOW, view))
        kvu, uchecks, pid = tz27.unit_reads(int(mk["NRestarts"]) + 1)
        readings["G-UNIT"] = all(uchecks.values()) and pid == start.get("pid")
        out("G-UNIT: %r; MainPID %d" % (uchecks, pid))
        reading, T, _c = tz27.resume_decision(W, start.get("pid"), int(time.time()),
                                              lambda t: window_json(tz27.ROOT, t))
        readings["G-RESUME"] = reading in ("PASS", "UNDECIDABLE")
        out("READING G-RESUME: %s, window %d" % (reading, T))
        trs = jsonl_read(os.path.join(rdir, "transfers.jsonl"))
        for t in trs:
            s, e = transfer_ok(t)
            out("T %s %s: %d bytes, budget %d s, second %d, %.1f s, inside %s %s" % (
                t["kind"], t["name"], t["bytes"], t["budget_s"], phase_of(t["start_ns"] // 10 ** 9),
                (t["end_ns"] - t["start_ns"]) / 1e9, s, e))
        readings["G-IDLE"] = bool(trs) and all(all(transfer_ok(t)) for t in trs)
        out("G-IDLE: %d requests, %d started outside, %d ended outside" % (
            len(trs), sum(1 for t in trs if not transfer_ok(t)[0]), sum(1 for t in trs if not transfer_ok(t)[1])))
        comp = mine[-1]
        out("the run's own record: %s" % json.dumps(comp, sort_keys=True))
    for k, v in readings.items():
        out("READING %-11s %s" % (k, "PASS" if v else "FAIL"))
    bad = sorted(k for k, v in readings.items() if not v)
    assert not bad, "FIRST FAIL: %r" % bad
    out("FIRST PASS: %d of %d" % (len(readings), len(readings)))
    return 0


def mode_final():
    tz27.MODE[0] = "final"
    recs = Ledger(STATE).recs
    marks = [r for r in recs if r.get("event") == "mark"]
    st = tz27.load_state()
    n = int(marks[-1]["mark"]["NRestarts"]) + 1 if marks and "start-svc" not in st.get("marks", {}) else None
    tz27.mode_unit(n)
    tz27.mode_still()
    now = time.time()
    kv, checks, nxt = timer_reading(now)
    for k, v in checks.items():
        out("G-TIMER %-24s %s" % (k, v))
    assert all(checks.values()), "G-TIMER FAIL: %r" % sorted(k for k, v in checks.items() if not v)
    counter, free = tz27.stream_bytes_view(tz27.ROOT), tz27.free_bytes()
    dirs = tz27.window_dirs(tz27.ROOT)
    out("the store: %d window directories, %d to %d; its stream files %d bytes; free %d bytes" % (
        len(dirs), dirs[0] if dirs else 0, dirs[-1] if dirs else 0, counter, free))
    done = [r for r in recs if r.get("event") == "complete"]
    if done:
        sets = [r for r in recs if r.get("event") == "set" and r["run"] == done[-1]["run"]][-1]
        rate, rows = tz27.projection(sets["bytes_total"], sets["first_T"], sets["last_T"], counter, free, int(now))
        out("the last set's rate: %s bytes a day" % tz27.decimals(rate, 0))
        for what, d, when in rows:
            out("at that rate %s stops the streams in %s days, at %s" % (what, tz27.decimals(d, 2), tz27.utc(when)))
    out("the next run at %s; the ledger %d records" % (tz27.utc(nxt), len(recs)))
    out("FINAL PASS")

# ---- the self-test: literals, temporary stores, a simulated pair book and a loopback server only --------------


class FakeEnv(Env):
    """The run's world in a temporary directory: a clock that moves only when the run sleeps, a pair book that
    restarts on a SIGTERM and writes its records, and GitHub on 127.0.0.1."""

    def __init__(self, work, root, state, base, t0, token):
        self.root, self.state, self.work = root, state, work
        self.wait_min, self.gap_s = 0, 0.0
        self.api = self.uploads = self.web = base
        self.invocation, self.commit, self.file_sha = "selftest", "c" * 40, "f" * 64
        self.clock, self.token, self.cred_ok = float(t0), token, True
        self.pid, self.nrestarts, self.kills, self.disabled = 815823, 2, 0, 0
        self.skew, self.on_sleep, self.active = 0, None, "active"

    def time(self):
        return self.clock

    def time_ns(self):
        return int(round(self.clock * 1e9))

    def sleep(self, s):
        self.clock += max(0.0, s)
        if self.on_sleep is not None:
            self.on_sleep(self)

    def show(self, unit, props):
        return {"MainPID": str(self.pid), "NRestarts": str(self.nrestarts), "ActiveState": self.active}

    def record(self, rec):
        with open(os.path.join(self.root, "runtime.jsonl"), "ab") as fh:
            fh.write((json.dumps(rec, sort_keys=True) + "\n").encode("utf-8"))

    def kill(self):
        t = self.clock
        W = int(t + 5.6) // WINDOW * WINDOW
        self.record({"event": "stop", "pid": self.pid, "wall_ns": int((t + 0.2) * 1e9)})
        self.pid, self.nrestarts, self.kills = self.pid + 1, self.nrestarts + 1, self.kills + 1
        self.record({"event": "start", "pid": self.pid, "wall_ns": int((t + 5.6) * 1e9), "commit": "e8b4",
                     "file_sha256": "caed", "free_bytes": 12931072000,
                     "stream_bytes": tz27.stream_bytes_view(self.root, upto=W - WINDOW) + self.skew})
        d = os.path.join(self.root, str(W))
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "window.json"), "w", encoding="utf-8") as fh:
            json.dump({"pid": self.pid, "documents_ok": True, "stream": {"opened": True, "off_reason": None,
                                                                         "files": ["stream.jsonl.gz"]}}, fh)
        return 0

    def unit_reads(self, n):
        checks = {"active": True, "argv": True, "sole instance": True, "restarts": self.nrestarts == n}
        return {"NRestarts": str(self.nrestarts)}, checks, self.pid

    def disable_timer(self):
        self.disabled += 1
        return 0

    def credential(self):
        if not self.cred_ok:
            raise AssertionError("UPLOAD REFUSED: no credential (selftest)")
        return self.token, "the selftest's"

    def free(self):
        return 12931072000

    def mem(self):
        return 300000000


def mode_selftest():
    n = [0]

    def ok(cond, what):
        assert cond, "selftest: " + what
        n[0] += 1
        out("  ok  " + what)

    sep = ":" + "//"
    # the clock, against integers computed outside this file
    ok([budget_s(0), budget_s(1), budget_s(2000000), budget_s(2000001), budget_s(100000000)] == [5, 6, 6, 7, 55]
       and IDLE_MAX_BYTES == 1140000000, "the budget: 5 s and the bytes at 2,000,000 a second, rounded up")
    ok(next_calendar(1791720000) == 1791774020 and next_calendar(1791774019) == 1791774020
       and next_calendar(1791774020) == 1791860420, "the calendar: 03:00:20 UTC, the next after now")
    ok(stamp_of("Mon 2026-10-12 03:00:20 UTC") == 1791774020 and stamp_of("n/a") is None and stamp_of("") is None
       and stamp_of("Mon 2026-10-12 03:00:20 CEST") is None, "systemctl's stamps, read in UTC alone")
    T = 1791747000
    ok([transfer_ok({"start_ns": (T + p) * 10 ** 9, "end_ns": (T + q) * 10 ** 9, "budget_s": b})
        for p, q, b in ((15, 20, 5), (14, 20, 5), (585, 590, 5), (586, 590, 5), (15, 591, 5), (540, 600, 55))]
       == [(True, True), (False, True), (True, True), (False, True), (True, False), (False, False)],
       "G-IDLE: a request starts at second 15 to 590 less its budget, and ends by second 590")

    class Clock:
        def __init__(self, t):
            self.t, self.slept = float(t), []

        def time(self):
            return self.t

        def sleep(self, s):
            self.slept.append(s)
            self.t += s

    c = Clock(T + 585.25)
    idle_wait(c, 5)
    c2 = Clock(T + 3)
    idle_wait(c2, 55)
    c3 = Clock(T + 540)
    idle_wait(c3, 55)
    c4 = Clock(T + 471)
    band_wait(c4)
    c5 = Clock(T + 200)
    band_wait(c5)
    ok(phase_of(c.t) == 585 and c.slept == [] and phase_of(c2.t) == 15 and phase_of(c3.t) == 15
       and int(c3.t) == T + 900 + 15 and phase_of(c4.t) == 15 and int(c4.t) == T + 915 and c5.slept == [],
       "idle_wait and band_wait: now where the second allows, else the next allowed second")
    try:
        idle_wait(Clock(T), 576)
        big = False
    except AssertionError:
        big = True
    ok(big, "a request longer than the idle stretch stops the run")
    ok(TAG_RE.fullmatch("pairbook-streams-1791747020") and tz27.TAG_RE.fullmatch("pairbook-streams-1791747020") is None
       and TAG_RE.fullmatch("tz-27-pairbook-streams") is None, "this TZ's tags, which TZ-27's rule does not cover")
    rq = release_request("pairbook-streams-1791747020", "c" * 40, "n", "b")
    ok(rq["target_commitish"] == "c" * 40 and rq["draft"] is False and rq["make_latest"] == "false"
       and sorted(rq) == ["body", "draft", "make_latest", "name", "prerelease", "tag_name", "target_commitish"],
       "the Release is created at the run's commit, published, never the latest")
    recs = [{"event": "start", "run": 1}, {"event": "deferred", "run": 1}, {"event": "start", "run": 1}]
    ok(pending(recs) == 1 and pending(recs + [{"event": "complete", "run": 1}]) is None and pending([]) is None
       and halted(recs + [{"event": "halt", "run": 1}]) and not halted(recs + [{"event": "halt", "run": 1},
                                                                               {"event": "clear", "run": None}]),
       "the ledger: a run without a terminal record is resumed; a halt holds until a clear")
    # TZ-27's hook, under the modes the run gives it
    w, s0 = STATE, tz27.ROOT + "/1791747000/stream.jsonl.gz"
    P = tz27.policy
    ok(P("upload", "open", (w + "/ledger.jsonl", "ab", 0), w, set()) is None
       and P("verify", "open", (w + "/runs/1/verify.json", "wb", 0), w, set()) is None
       and P("verify", "open", ("/root/tz28-work/x", "wb", 0), w, set()) is not None
       and P("verify", "open", (s0, "rb", 0), w, set()) is not None
       and P("delete", "os.remove", (s0, None), w, {s0}) is None
       and P("restart", "os.remove", (s0, None), w, {s0}) is not None
       and P("inventory", "subprocess.Popen", ("systemctl",), w, set()) is not None
       and P("final", "subprocess.Popen", ("systemctl",), w, set()) is None
       and P("run", "open", (tz27.RECORDER + "/runtime.jsonl", "rb", 0), w, set()) is not None,
       "the run writes under its state alone, reads the store where TZ-27 did, and starts no process in "
       "inventory or delete")
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
    ok(128 * 2 ** 20 == ARCHIVE_MEMORY_MAX and 6 * 3600 == TIMEOUT_S, "128M and 6h in bytes and seconds")
    # the run on temporary stores, a simulated pair book and the loopback server
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

    def put(root, T_, name, nbytes):
        d = os.path.join(root, str(T_))
        os.makedirs(d, exist_ok=True)
        data = (hashlib.sha256(("%d/%s" % (T_, name)).encode()).digest() * (nbytes // 32 + 1))[:nbytes]
        with open(os.path.join(d, name), "wb") as fh:
            fh.write(data)
        blobs[(T_, name)] = data

    def closed(root, T_, streams):
        for k_, nb in enumerate(streams):
            put(root, T_, "stream.jsonl.gz" if k_ == 0 else "stream.%d.jsonl.gz" % k_, nb)
        put(root, T_, "books.jsonl.gz", 900)
        put(root, T_, "window.json", 300)

    def world(name, t0):
        root, state = os.path.join(tmp, name, "store"), os.path.join(tmp, name, "state")
        os.makedirs(root)
        os.makedirs(state)
        env = FakeEnv(tz27.WORK[0], root, state, base, t0, tok)
        env.record({"event": "start", "pid": env.pid, "wall_ns": int((t0 - 86400) * 1e9), "commit": "e8b4",
                    "file_sha256": "caed", "stream_bytes": 0})
        return env

    def evs(env):
        return [r["event"] for r in Ledger(env.state).recs]

    try:
        # 1. a whole run: three closed windows, one unclosed, one open
        env = world("one", T + 3600 + 80)
        closed(env.root, T, [70001])
        closed(env.root, T + 900, [50000, 33333])
        closed(env.root, T + 1800, [40000])
        put(env.root, T + 2700, "stream.jsonl.gz", 777)
        rc = run(env)
        led = Ledger(env.state).recs
        a = led[0]["run"]
        ok(rc == 0 and evs(env) == ["start", "set", "upload", "verify", "delete", "mark", "kill", "restart", "resume",
                                    "complete"] and a == T + 3680, "a run: every step recorded, in order, exit 0")
        setr = events(led, a, "set")[0]
        ok(setr["assets_n"] == 4 and setr["bytes_total"] == 193334 and setr["first_T"] == T
           and setr["last_T"] == T + 1800
           and setr["tag"] == "pairbook-streams-%d" % a and setr["open"] == 0 and setr["unclosed"] == 1,
           "the set: TZ-27's rule as of the run's start, under this TZ's tag")
        rel = Fake.releases["pairbook-streams-%d" % a]
        held = sorted(v["name"] for v in Fake.assets.values() if v["rid"] == rel["id"])
        ok(held == sorted(["%d-stream.jsonl.gz" % T, "%d-stream.jsonl.gz" % (T + 900),
                           "%d-stream.1.jsonl.gz" % (T + 900), "%d-stream.jsonl.gz" % (T + 1800)])
           and all(v["data"] == blobs[(int(v["name"][:10]), v["name"][11:])] for v in Fake.assets.values()),
           "the Release holds the set's four files, byte for byte")
        ok(sorted(os.listdir(os.path.join(env.root, str(T)))) == ["books.jsonl.gz", "window.json"]
           and sorted(os.listdir(os.path.join(env.root, str(T + 900)))) == ["books.jsonl.gz", "window.json"]
           and os.path.exists(os.path.join(env.root, str(T + 2700), "stream.jsonl.gz")),
           "the store: the set's files gone, every other entry kept")
        mk = events(led, a, "mark")[0]
        rs = events(led, a, "restart")[0]
        ok(env.kills == 1 and KILL_BAND[0] <= mk["phase"] <= KILL_BAND[1] and rs["W"] == T + 3600
           and rs["pid"] == 815824 and events(led, a, "resume")[0]["reading"] == "PASS",
           "the restart inside its band, its counter the store's, and the stream resumed")
        trs = jsonl_read(os.path.join(env.state, "runs", str(a), "transfers.jsonl"))
        comp = events(led, a, "complete")[0]
        ok(len([t for t in trs if t["kind"] == "upload"]) == 4 and len([t for t in trs if t["kind"] == "download"]) == 4
           and all(all(transfer_ok(t)) for t in trs) and comp["started_outside"] == 0 and comp["ended_outside"] == 0
           and all(h[2] == tz27.UA for h in Fake.hits)
           and all(h[3] is None for h in Fake.hits if "/releases/download/" in h[1] or h[1].startswith("/blob/")),
           "every request timed and inside the idle stretch; reads with no token, every request under TZ-27's agent")
        # 2. a second run with no closed window left: empty
        env.clock += 300
        rc2 = run(env)
        ok(rc2 == 0 and evs(env)[-2:] == ["start", "empty"], "a run with nothing closed records empty and exits 0")
        # 3. a refused credential defers, and the next run resumes the same set
        env3 = world("defer", T + 86400 + 3600 + 588)
        closed(env3.root, T, [1000])
        env3.cred_ok = False
        rc3 = run(env3)
        a3 = Ledger(env3.state).recs[0]["run"]
        ok(rc3 == EXIT_DEFERRED and evs(env3) == ["start", "set", "deferred"]
           and os.path.exists(os.path.join(env3.root, str(T), "stream.jsonl.gz")),
           "a refused credential: deferred, exit 75, nothing removed")
        env3.cred_ok = True
        env3.clock += 86400
        rc3b = run(env3)
        led3 = Ledger(env3.state).recs
        ok(rc3b == 0 and [r["run"] for r in led3 if r["event"] == "start"] == [a3, a3]
           and events(led3, a3, "start")[1]["resumed"] is True and evs(env3)[-1] == "complete",
           "the next run resumes the deferred set and completes it")
        trs3 = jsonl_read(os.path.join(env3.state, "runs", str(a3), "transfers.jsonl"))
        ok(phase_of(trs3[0]["start_ns"] // 10 ** 9) == 15 and all(all(transfer_ok(t)) for t in trs3),
           "a request due at second 588 waits for the next idle stretch")
        # 4. three deferrals halt the archive; a halted archive refuses until a clear
        env4 = world("halt", T + 3 * 86400 + 3600 + 20)
        closed(env4.root, T, [1000])
        env4.cred_ok = False
        rcs = [run(env4) for _k in range(3)]
        ok(rcs == [EXIT_DEFERRED, EXIT_DEFERRED, 1] and evs(env4)[-2:] == ["halt", "timer-disabled"]
           and env4.disabled == 1, "the third deferral of one set halts, and the run disables its timer")
        env4.cred_ok = True
        ok(run(env4) == 1 and evs(env4)[-1] == "refused" and env4.disabled == 2
           and os.path.exists(os.path.join(env4.root, str(T), "stream.jsonl.gz")),
           "a halted archive refuses the next run, and removes nothing")
        jsonl_append(os.path.join(env4.state, "ledger.jsonl"), {"event": "clear", "run": None, "wall_ns": 0}, "x")
        env4.clock += 60
        ok(run(env4) == 0 and evs(env4)[-1] == "complete", "after a clear the next run takes a new set")
        # 5. a corrupted asset fails the verify: deferred, nothing removed; mended, the next run completes
        env5 = world("verify", T + 5 * 86400 + 3600 + 20)
        closed(env5.root, T, [5000, 6000])

        def corrupt(e):
            if e.on_sleep is corrupt:
                e.on_sleep = None
                k = sorted(Fake.assets)[-1]
                good = Fake.assets[k]["data"]
                Fake.assets[k]["data"] = good[:-1] + bytes([good[-1] ^ 1])
                corrupt.saved = (k, good)

        env5.on_sleep = corrupt
        rc5 = run(env5)
        ok(rc5 == EXIT_DEFERRED and evs(env5)[-1] == "deferred"
           and "VERIFY FAIL" in Ledger(env5.state).recs[-1]["reason"]
           and os.path.exists(os.path.join(env5.root, str(T), "stream.1.jsonl.gz")),
           "a flipped bit in one asset: VERIFY FAIL, deferred, nothing removed")
        k5, good5 = corrupt.saved
        Fake.assets[k5]["data"] = good5
        ok(run(env5) == 0 and evs(env5)[-1] == "complete", "the asset mended, the next run verifies and completes")
        # 6. a failure after the removal halts: the files archived, the timer disabled
        env6 = world("counter", T + 6 * 86400 + 3600 + 20)
        closed(env6.root, T, [2000])
        env6.skew = 1
        rc6 = run(env6)
        led6 = Ledger(env6.state).recs
        ok(rc6 == 1 and [r["event"] for r in led6][-3:] == ["kill", "halt", "timer-disabled"]
           and "G-COUNTER FAIL" in led6[-2]["reason"] and env6.disabled == 1
           and not os.path.exists(os.path.join(env6.root, str(T), "stream.jsonl.gz")),
           "G-COUNTER FAIL after the removal: halted, the files already archived, the timer disabled")
        # 7. a pair book that is not running is not restarted
        env7 = world("down", T + 7 * 86400 + 3600 + 20)
        closed(env7.root, T, [2000])
        env7.active = "failed"
        ok(run(env7) == 1 and env7.kills == 0 and "not restarted" in Ledger(env7.state).recs[-2]["reason"],
           "a pair book not active: the archive halts after its removal and signals nothing")
        ok(not [h for h in Fake.hits if h[3] not in (None, "Bearer " + tok)],
           "the loopback server saw no credential but the run's")
    finally:
        srv.shutdown()
        srv.server_close()
    shutil.rmtree(tmp)
    ok(not os.path.lexists(tmp), "the temporary stores removed")
    # this file's own syntax: its imports, and no endpoint of its own
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
        sys.exit("usage: tz28-pairbook-archive-timer.py MODE [ARG...]")
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
        elif mode == "first":
            assert not rest, "first takes no argument"
            rc = mode_first()
        else:
            table = {"fingerprint": mode_fingerprint, "selftest": mode_selftest, "tz27-release": mode_tz27_release,
                     "path": mode_path, "path-token": mode_path_token, "installed": mode_installed,
                     "timer": mode_timer, "final": mode_final, "still": tz27.mode_still, "started": tz27.mode_started}
            assert mode in table and not rest, "unknown mode %r" % (argv,)
            if mode in ("still", "started"):
                tz27.MODE[0] = "started" if mode == "started" else "still"
            table[mode]()
    out("peak memory of this run: %d bytes" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024))
    out("opens refused: %d; store opens %d; requests %d, uploads %d, downloads %d (%d bytes); files removed %d" % (
        len(tz27.REFUSED), tz27.STORE_OPENS[0], tz27.COUNTERS["requests"], tz27.COUNTERS["uploads"],
        tz27.COUNTERS["downloads"], tz27.COUNTERS["download_bytes"], tz27.COUNTERS["removed"]))
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
```

### `deploy/systemd/btc-pairbook-archive.service`

```ini file=deploy/systemd/btc-pairbook-archive.service
# btc-5m-twap: the pair book's archive, its closed windows' stream files moved verbatim to a Release (TZ-28).
# Started by btc-pairbook-archive.timer alone; installed byte for byte as /etc/systemd/system/btc-pairbook-archive.service.
[Unit]
Description=btc-5m-twap pair book archive, the stream files of closed windows to a Release
Wants=network-online.target
After=network-online.target time-sync.target btc-pairbook.service

[Service]
Type=oneshot
WorkingDirectory=/var/lib/btc-pairbook-archive
ExecStart=/root/tz04a-env/venv/bin/python -B -u /root/btc-pairbook-archive-svc/tz28-pairbook-archive-timer.py run
Restart=no
TimeoutStartSec=21600
Nice=19
MemoryMax=128M
StandardOutput=append:/var/lib/btc-pairbook-archive/archive.log
StandardError=append:/var/lib/btc-pairbook-archive/archive.log
```

### `deploy/systemd/btc-pairbook-archive.timer`

```ini file=deploy/systemd/btc-pairbook-archive.timer
# btc-5m-twap: the pair book's archive, daily at 03:00:20 UTC and 600 s after the timer starts (TZ-28).
# Installed byte for byte as /etc/systemd/system/btc-pairbook-archive.timer; its stop is systemctl disable --now.
[Unit]
Description=btc-5m-twap pair book archive, once a day

[Timer]
OnCalendar=*-*-* 03:00:20 UTC
OnActiveSec=600
AccuracySec=1s
Unit=btc-pairbook-archive.service

[Install]
WantedBy=timers.target
```
