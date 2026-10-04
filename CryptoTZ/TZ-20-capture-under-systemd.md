# TZ-20 — the capture under systemd

**Canonical filename:** `TZ-20-capture-under-systemd.md`. The committed file takes this name and no other.

**Executor model: Opus.** Network capture, clock discipline, data loss, and the start and the stop of two
long-lived processes.

**Required System Map revision:** `2026-10-04-a`.

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

**What this TZ is.** Both capture processes are down: the recorder since 2026-10-02 about 11:36 UTC and the
chain book since 2026-10-03 08:56:15 UTC (TZ-19 report §3.2 and §3.3). Each ran inside an interactive session
and ended with it. This TZ starts each again as a **systemd system unit** — `btc-recorder.service` and
`btc-chainbook.service` — from the code each ran, each under a memory ceiling, and proves over about two hours
that each runs outside any session, captures, records its own gap, and is restarted by systemd after a stray
`SIGTERM`. **It also leaves the host clean:** the work trees of TZ-16a and TZ-19, and its own, are removed once
what the reports name by hash is in the forensic store (§9). It changes no committed file, reads no price and no
label, and scores nothing.

---

## 0. Gates

### 0.1 Fingerprint

Contract §1 steps 3 and 4, against `SYSTEM-MAP.md` at `main` after contract §1's pull: revision string
`2026-10-04-a`; the six anchors above, `A2`, `A4`, `A5` and `A6` re-derived as the first 12 hex characters of
those files' SHA-256; the §0 table's **28** rows hashed in lines, bytes and SHA-256 — **25** `frozen` rows equal
to the map, **2** `tracked` and **1** `reported` row printed. Any mismatch is BLOCKED.

### 0.2 Host gate

From `/root/btc-5m-twap`, before anything else, output verbatim into the report:

```
date -u; date -u +%s
df -B1 --output=source,size,avail /var/lib/btc-recorder
find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
grep -c 4216c04673ced76b5b2ac60ef57c9abedc46f9b9 /var/lib/btc-recorder/runtime.jsonl
pgrep -fx '/root/tz04a-env/venv/bin/python -B -u recorder.py'; echo "exit=$?"
pgrep -fx '/root/tz01-env/venv/bin/python -B -u /root/tz18a-svc/tz18a-chainbook-capture.py --serve'; echo "exit=$?"
systemctl --version | head -1
systemctl cat btc-recorder.service btc-chainbook.service >/dev/null 2>&1; echo "units exit=$?"
loginctl show-user root -p Linger; grep -hE '^[[:space:]]*#?[[:space:]]*(KillUserProcesses|KillExcludeUsers)' /etc/systemd/logind.conf
du -sb /root/PROJECT_GAMING_PS5
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
systemctl is-active telemetry-watch.service; echo "exit=$?"
for d in /root/tz16a-work /root/tz18a-svc /root/tz19-work /root/tz20-work /root/btc-recorder-svc; do test -e "$d"; echo "$d exit=$?"; done
find /root/btc-forensics -type f | wc -l
/root/tz04a-env/venv/bin/python -c 'import sys, websockets; print(sys.version.split()[0], websockets.__version__)'
/root/tz01-env/venv/bin/python -c 'import sys; print(sys.version.split()[0])'
git worktree list
```

- **H1** — `find` prints exactly one path.
- **H2** — `df` names source `/dev/vda2` and size `31612203008`; `grep -c` prints at least `1`. With H1 this is
  map §6's host identity, which no longer includes whether a process runs (map §7 item 86).
- **H3 — both processes down.** Each `pgrep -fx` prints no line and `exit=1`. `-fx` matches the whole command
  line, so the shell evaluating this block cannot match itself. A running instance of either means someone
  started it outside a TZ: BLOCKED.
- **H4** — `systemctl --version` names a version of at least `240`, the first with `append:` outputs.
- **H5** — `units exit=1`: neither unit exists anywhere systemd looks.
- **H6 — trees.** `/root/tz18a-svc` exits `0`; `/root/tz20-work` and `/root/btc-recorder-svc` exit `1`. Anything
  else is BLOCKED. `/root/tz16a-work` and `/root/tz19-work` are recorded, not BLOCKING: §9 reclaims whichever
  exists.
- **H7** — the forensic store holds exactly `1,072` files (TZ-19 report §1.1).
- **H8** — the first interpreter prints `3.12.` and a `websockets` version; the second prints `3.12.`. An import
  error is BLOCKED.
- **Resource gate** — `avail` at least `2,260,000,000` bytes (§0.3).
- `Linger`, the two `logind.conf` lines, `du`, both `systemctl` reads of `telemetry-watch.service` and
  `git worktree list` are printed and carry no threshold.

**S1 to S7**, the instrument's `state` mode, complete the gate once §3.1 has written it (§3.2). They are
asserts, and any failure is BLOCKED with nothing installed and nothing started.

### 0.3 Resource floor, in exact bytes, derived from map §6

Free space on `/dev/vda2` at the host gate at least **`2,260,000,000`** bytes: the chain book's own floor,
`RESOURCE_FLOOR` = `2,200,000,000` (`research/tz18a-chainbook-capture.py` line 79), which it asserts at start
and before every window, plus `60,000,000` bytes for what this session writes. That bound holds with room: the
branch worktree is about `4,300,000` bytes (`origin/main`'s tree is `4,121,413`), the recorder's tree
`608,045` (`4216c04`'s), this TZ's logs under `1,000,000`, the capture's own growth over three hours
`4,545,713` at map §6's measured `33,632,842` and `2,732,864` bytes a day, and §9's forensic copies at most
`27,510,104` — the two old trees whole, `22,398,514` and `4,111,590` bytes at TZ-19's closing read, and this
TZ's logs — before the trees themselves are removed. The recorder's own floor,
`FREE_SPACE_FLOOR_BYTES` = `2,000,000,000` (`config.py` line 21), sits below it. Every free-space read of this
TZ is reported with its UTC instant, its reader and this bound.

### 0.4 Refs

`git ls-remote origin` before the branch of §2 exists, every ref reported. Map §1 records `main` at
`b96be84a2a5e417a5ab8c00fbaf7591f8e4015e2`, the TZ-19 report, and `main` the only branch. The upload that
carries this TZ and revision `2026-10-04-a` sits above it. A difference is recorded, not BLOCKING, unless
`main` does not carry revision `2026-10-04-a` or `refs/heads/tz-20-capture-under-systemd` already exists —
either is BLOCKED.

---

## 1. Why this TZ exists

**What ended, and how.** TZ-19 stopped at its host gate: no process ran `recorder.py` (TZ-19 report §2). Its
evidence, read together (report §3.2 and §3.3):

- **The recorder** started 2026-09-12 09:53:05 UTC, 55 s after root's login session 7379 opened. Its last
  record is a `clock` record at 11:35:44 on 2026-10-02, and the directory of `1790941200`, which it would have
  created at 11:38:30, does not exist: it died between those instants. At 11:36:18 logind removed session 7379,
  whose scope had consumed 1 h 27 min of CPU; in the same second a process of another project on this host
  received `SIGTERM` and a `bash` process dropped the page cache. The recorder has no `SIGTERM` handler and
  writes no `stop` record, so it left none. Nothing read ties its pid to the session; the instants do.
- **The chain book** wrote its `stop` record at 08:56:15 on 2026-10-03, 11 s after root's login session 11095
  logged out. Root's `Linger` is `no`, so with no root session left its user manager began stopping 10 s after
  that logout and stopped its two tmux panes in the same second as the record. TZ-18a started the service with
  `setsid nohup` (TZ-18a §3.5), which leaves a process in its caller's control group. Nothing read ties pid
  `2699889` to a pane; the instants do.

**The Boss's account, 2026-10-04, closes the question:** after another project on this host ran out of memory,
he stopped all sessions. That stopped both captures, as the record above shows, and it will happen again
whenever memory runs short. **A capture must therefore survive any session being closed, and must never be the
process that takes the host's memory** — the two requirements this TZ meets with system units and their memory
ceilings.

**The class is one:** a long-lived capture whose lifetime was a session's and not the host's. CANON PART IV
fixes systemd for deployment, and until this revision map §6 listed systemd units as "not yet decided by any TZ".
That gap is the Architect's (map §7 item 85).

**What it cost, and what it did not.** RTDS holds no history and no replay (CANON §1.1), so every interval from
`1790941200` (2026-10-02 11:40 UTC) to this TZ's start, and every chain book window after `1791017100`, is lost.
**No measured set is among them:** TZ-19's readiness read found `3,885` complete manifests with
`T0 > 1789669800`, the 3,624th at `1790853000`, 2026-10-01 11:10 UTC — before the gap (TZ-19 report §1.2).

**What this TZ decides.**

1. **Two system units**, in `system.slice`, enabled for boot, each with `Restart=always` and `RestartSec=5`, and
   each with the exit statuses that are its own deliberate stops excluded from restart:
   - the recorder exits `0` when a resource floor stops it and `1` when a floor is already breached at start
     (`recorder.py` lines 598 and 588); `RestartPreventExitStatus=0`, so a floor stop stays stopped, and a
     breach at start is tried at most five times an hour;
   - the chain book exits `0` after `SIGTERM` (lines 509–510, 824 and 827), `1` on a failed assert — its write
     cap or its resource floor (lines 219 and 231) — and `2` or `3` when it refuses to serve (lines 802 and 809);
     `RestartPreventExitStatus=1 2 3`, so a `SIGTERM` from outside systemd is restarted and its cap is not.
   `StartLimitIntervalSec=3600` and `StartLimitBurst=5` bound any loop. **A stop ordered through systemd is never
   restarted**, which is what makes `systemctl disable --now` the stop of both (§4.6).
2. **The recorder runs from a detached worktree of its own at `4216c04`**, `/root/btc-recorder-svc`.
   `git_sha()` reads `HEAD` of the checkout `recorder.py` sits in (lines 50–55), so every start record names
   `4216c04` whatever `main` moves to, and map §6's host identity holds across restarts. `recorder.py`,
   `config.py` and `manifest.py` at `4216c04` are byte-identical to `main`'s frozen rows (§3.3). The command
   line is unchanged — `/root/tz04a-env/venv/bin/python -B -u recorder.py` — so `pgrep -fx` and
   `tz10b.recorder_pids` find it as before, and the primary checkout carries no running code any more.
3. **The chain book runs from `/root/tz18a-svc/` unchanged**, under the exact `SERVICE_ARGV` its `--serve`
   demands (lines 101–102 and 792–802).
4. **Logs stay where they were:** the recorder's stderr appends to `/var/lib/btc-recorder/recorder.log` (TZ-05a
   report), the chain book's output to `/var/lib/btc-chainbook/service.log` (TZ-18a §3.5).
5. **K-18a is retired.** Under `Restart=always` a `kill -TERM` restarts the chain book; its stop is K-20C.
6. **A memory ceiling on each unit** — `MemoryMax=512M` for the recorder and `192M` for the chain book — so a
   leak in either can never take memory from the host's other projects. The recorder's whole login session,
   itself included, peaked at `177.0M` over 20 days (TZ-19 report §3.2); the chain book is standard library and
   holds one window at a time. A process that reached its ceiling would be killed inside its own control group
   and restarted, so G-UNIT asserts each ceiling and prints each unit's memory in use and its peak at every
   read, and the report carries them, so that the ceilings are re-derived from measurement, not kept from
   assumption.
7. **Nothing this work no longer needs stays on the host** (CANON hard rule 15): §9 removes TZ-16a's and TZ-19's
   work trees and, last, this TZ's own, each only after its hashed files are in the forensic store.

---

## 2. Scope

**Repository paths this TZ may write, and no others:**

1. `deploy/systemd/btc-recorder.service`, `deploy/systemd/btc-chainbook.service` and
   `research/tz20-capture-under-systemd.py` — three new files, byte for byte Appendix A's, on branch
   `tz-20-capture-under-systemd`, then a pull request. Not merged by the Executor.
2. `CryptoReports/TZ-20-capture-under-systemd-report.md` — straight to `main`, in one commit. **The one path
   pushed to `main`, and the exemption to item 5 below.**

**Host paths this TZ may write:** `/root/tz20-work/**` — the branch worktree `wt`, `logs/` and
`instants.json`; `/root/btc-recorder-svc`, created once by `git worktree add` (§3.3);
`/etc/systemd/system/btc-recorder.service` and `/etc/systemd/system/btc-chainbook.service`, byte-identical to
item 1's two units, with the links `systemctl enable` makes for them; and `/root/btc-forensics/`, by exclusive
create only (§9). **Host paths it removes, under §9 and nothing else:** `/root/tz16a-work/` and
`/root/tz19-work/` with their three worktrees, and, last, `/root/tz20-work/` with its own. **The two units write their own trees**,
as the two processes always have: `/var/lib/btc-recorder/**` and `/var/lib/btc-chainbook/**`, both logs
included. That is the capture's work, not this TZ's.

**Prohibited, each absolutely:**

1. No committed file is modified. Every `frozen` row of map §0 is byte-identical at run end.
2. **Under `/var/lib/btc-recorder/` this TZ opens only the top-level `runtime.jsonl` and the `manifest.json` of
   G-REC's six intervals; under `/var/lib/btc-chainbook/` only `runtime.jsonl` and the `window.json` of G-CB's
   two windows** — read-only, map §2.3's and §2.5's exceptions. The instrument's audit hook refuses any other
   open there (V13). **Exemptions, each named because this TZ's body requires it:** (a) §0.2's `grep -c` and
   `find`; (b) §3.6's `tail -n 40` of `recorder.log` and `service.log`, whose lines carry statuses, counts and
   times and no price (`recorder.py` lines 340–342; `tz18a-chainbook-capture.py` lines 685–782 and 813–826). No quote file,
   `gamma.json`, `resolution.json`, stream, `books.jsonl.gz` or `documents.jsonl` is opened by this TZ. The
   recorder's own start-up reads of its newest directories (`last_frame_ns`, `recover`, lines 145–171 and
   345–373) are the capture's work, and nothing of them is printed.
3. Nothing under either capture root is created, moved or removed by this TZ's commands.
4. `/root/tz04a-env/`, `/root/tz01-env/`, `/root/btc-forensics/` and `/root/tz18a-svc/` are not modified,
   emptied or removed. **Exemption:** §9 adds files to `/root/btc-forensics/` by exclusive create.
5. Nothing is pushed to `main` except the report of item 2 above.
6. **No price, size, spread, mid, book level, outcome or label is read, printed or written.** §3.3's live
   requests print status, byte count, SHA-256, whether the body parses, and token ids, and of RTDS frames their
   count and topics — map §2.5's deployment exception — and nothing else of any body. **Two further exemptions,
   both §9's:** `reclaim` reads the committed reports for runs of hex characters alone, and it hashes and copies
   whole files of the reclaimed trees, some of which hold prices and labels, without extracting or printing any
   value from them.
7. **Requests:** §3.3's six HTTP requests, two SNTP bursts and one RTDS subscription of at most 30 s, each
   through the process's own function, and `git` against `origin` with the pull request. Nothing else is
   requested by this TZ; the units' traffic is the capture's.
8. **No process is signalled** except by §3.5's two `systemctl kill` and, on a FAIL, §4.6's stop blocks. K-18a is
   never run.
9. No unit but the two of this TZ is created, changed, started or stopped. `telemetry-watch.service` is read only.
10. No Release is created, and no dataset, archive or binary enters git history.

---

## 3. The work, in this order

Every command's output goes to `/root/tz20-work/logs/`, one file per step, and is quoted in the report.
`/root/tz01-env/venv/bin/python -B /root/tz20-work/wt/research/tz20-capture-under-systemd.py` is written
`I` below; a mode is `I <mode>`.

**§9's B-RECLAIM-OLD runs after §3.2 and before §3.3; its B-RECLAIM-OWN runs last, after §3.6.**

**Where the session's permission classifier refuses a command of a block named B-… or K-…**, the Executor
prints the block, the Boss runs it verbatim in a root shell on the VPS, and the Executor waits and then verifies
it through the reads this TZ names — never from the Boss's account. **Every `mark` is the Executor's**, taken
before its block is run or handed over.

### 3.1 The branch and its three files

```
git -C /root/btc-5m-twap fetch origin
git -C /root/btc-5m-twap worktree add -b tz-20-capture-under-systemd /root/tz20-work/wt origin/main
mkdir -p /root/tz20-work/logs
```

Then extract Appendix A from this TZ as `main` carries it, with this script, verbatim:

```
/root/tz01-env/venv/bin/python -B - <<'EOF'
import hashlib, os
SRC = "/root/tz20-work/wt/CryptoTZ/TZ-20-capture-under-systemd.md"
WANT = {
    "deploy/systemd/btc-recorder.service": "3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1",
    "deploy/systemd/btc-chainbook.service": "a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2",
    "research/tz20-capture-under-systemd.py": "104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7",
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
    path = os.path.join("/root/tz20-work/wt", name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "xb") as fh:
        fh.write(data)
    print(name, data.count(b"\n"), len(data), hashlib.sha256(data).hexdigest())
EOF
```

| path | lines | bytes | SHA-256 |
|---|---|---|---|
| `deploy/systemd/btc-recorder.service` | 23 | 707 | `3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1` |
| `deploy/systemd/btc-chainbook.service` | 22 | 724 | `a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2` |
| `research/tz20-capture-under-systemd.py` | 771 | 36,528 | `104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7` |

Commit the three files alone on the branch, push it, and open the pull request against `main`. A failed assert
here is BLOCKED.

### 3.2 State — the rest of the host gate

`I state`, before §3.3 creates anything. It must print `STATE PASS: S1 to S7`:

- **S1, S2** — no process anywhere has an argument ending in `recorder.py` (`tz10b.recorder_pids`' rule) or in
  `tz18a-chainbook-capture.py`.
- **S3** — the recorder's `runtime.jsonl` is as TZ-19 left it: `60,690` newlines and ending in one, its newest
  `start` record at `recv_ns` `1789206785264516934` with sha `4216c04673ced76b5b2ac60ef57c9abedc46f9b9`, its
  last record at `recv_ns` `1790940944342950552` (TZ-19 report §3.2).
- **S4** — the chain book's `runtime.jsonl` holds `4` records, none torn, the last a `stop` of pid `2699889` at
  `wall_ns` `1791017775066372007` (TZ-19 report §3.2).
- **S5** — neither unit file and no `/root/btc-recorder-svc` exists.
- **S6** — `/root/tz18a-svc/tz18a-chainbook-capture.py` hashes `e9cb9b47…` — map §0's frozen row — and
  `commit.txt` beside it is `ca4bbc1dd583cbb62f3c0c985938d229b526ce7e` and a newline (TZ-18a §3.5).
- **S7** — both interpreters are executable.

### 3.3 The recorder's tree, and the request paths

```
git -C /root/btc-5m-twap worktree add --detach /root/btc-recorder-svc 4216c04673ced76b5b2ac60ef57c9abedc46f9b9
git -C /root/btc-recorder-svc/research/recorder rev-parse HEAD
sha256sum /root/btc-recorder-svc/research/recorder/recorder.py /root/btc-recorder-svc/research/recorder/config.py /root/btc-recorder-svc/research/recorder/manifest.py
```

`HEAD` must be `4216c04673ced76b5b2ac60ef57c9abedc46f9b9`, and the three hashes map §0's frozen rows —
`9fd1c7de…`, `8111dfe4…` and `79c99010…`. Then, **CANON hard rule 14's proof, before either process starts:**

```
cd /root/btc-recorder-svc/research/recorder && /root/tz04a-env/venv/bin/python -B /root/tz20-work/wt/research/tz20-capture-under-systemd.py path-recorder
I path-chainbook
```

- **`path-recorder`** loads `recorder.py` and `config.py` from the new tree and asserts `git_sha()` is
  `4216c04…` (P0); fetches the market document of the five-minute interval open for at least 30 s through
  `recorder.fetch`, the function behind S6 and S7, and asserts it served, parsed and carries two token ids (P1);
  reads the first token's book through `recorder.fetch_status`, Tier C's function, and asserts `200` and a JSON
  body (P2); queries both SNTP servers through `recorder.sntp_best` and asserts at least one accepted reply — the
  recorder treats an unanswered server as a missing sample (P3); and subscribes to RTDS exactly as `rtds()` does
  — `config.TIER_A`'s message, `config.RTDS_URL`, the same connect arguments (lines 531–539) — and asserts
  `crypto_prices_twap_sixty` and `crypto_prices_chainlink`, the two streams `complete` depends on, arrive within
  30 s (P4). The other two topics are printed.
- **`path-chainbook`** loads the service's own copy, asserts its hash and `SERVICE_ARGV`, prints
  `build_request`'s headers (P5), fetches the current fifteen-minute and five-minute documents through
  `http_get`, `0.2` s apart, each served and carrying two token ids (P6), and reads one book of each, `200` and
  JSON (P7): four requests, asserted.

**Every header is fixed:** the recorder sends `User-Agent: btc-5m-twap-recorder/TZ-04a` (`config.py` line 43)
and the chain book `Accept: application/json` and `User-Agent: btc-5m-twap-tz18a` (line 420), each beside
urllib's own `Accept-Encoding: identity`, `Host` and `Connection: close`; RTDS receives the `websockets`
library's opening handshake, as the recorder has sent since 2026-09-10. **A failed assert in this section is
BLOCKED, and nothing is installed or started.**

### 3.4 Install, then start — the recorder first, because every minute of it is data

**B-INSTALL:**

```
install -m 0644 /root/tz20-work/wt/deploy/systemd/btc-recorder.service /etc/systemd/system/btc-recorder.service
install -m 0644 /root/tz20-work/wt/deploy/systemd/btc-chainbook.service /etc/systemd/system/btc-chainbook.service
cmp /root/tz20-work/wt/deploy/systemd/btc-recorder.service /etc/systemd/system/btc-recorder.service; echo "exit=$?"
cmp /root/tz20-work/wt/deploy/systemd/btc-chainbook.service /etc/systemd/system/btc-chainbook.service; echo "exit=$?"
systemctl daemon-reload; echo "exit=$?"
systemd-analyze verify /etc/systemd/system/btc-recorder.service /etc/systemd/system/btc-chainbook.service; echo "exit=$?"
```

Both `cmp` and `daemon-reload` must exit `0`, or BLOCKED and nothing is started. `systemd-analyze verify` is
recorded: its findings may name other units on this host, and G-UNIT decides.

**B-START-REC**, after `I mark start-rec`:

```
systemctl enable --now btc-recorder.service; echo "exit=$?"
```

**B-START-CB**, after `I mark start-cb`:

```
systemctl enable --now btc-chainbook.service; echo "exit=$?"
```

### 3.5 The proof, in this order

1. **At least 60 s after B-START-CB:** `I unit 0` — **G-UNIT** — then `I start` — **G-START**.
2. **`I cb` until it prints PASS or FAIL** — **G-CB** — at most 600 s apart; exit `3` is NOT YET and names the
   instant to run it again. About 30 min.
3. **B-KILL-CB**, only after G-UNIT, G-START and G-CB read PASS, at the first instant at which
   `$(( $(date +%s) % 900 ))` lies between `15` and `480` — the chain book's idle stretch between a window's close
   at `T + 905` and the next document at `T + 1525`, so no window is lost — after `I mark kill-cb`:

   ```
   systemctl kill --signal=SIGTERM btc-chainbook.service; echo "exit=$?"
   ```

   At least 30 s later, `I restart-cb` — **G-RESTART-C**.
4. **`I rec` until it prints PASS or FAIL** — **G-REC** — at most 600 s apart. The sixth interval's manifest
   lands about 11 min after it opens, and never later than `3,900` s.
5. **B-KILL-REC**, only after G-REC and G-RESTART-C read PASS, at the first instant at which
   `$(( $(date +%s) % 300 ))` lies between `122` and `128` — after the `tau` 180 read and inside one interval's
   window alone, so at most one interval loses `complete` — after `I mark kill-rec`:

   ```
   systemctl kill --signal=SIGTERM btc-recorder.service; echo "exit=$?"
   ```

   At least 30 s later, `I restart-rec` — **G-RESTART-R**.
6. `I final`.

### 3.6 The closing reads

§0.2's block again, then:

```
systemctl is-enabled btc-recorder.service btc-chainbook.service; echo "exit=$?"
systemctl is-active btc-recorder.service btc-chainbook.service; echo "exit=$?"
journalctl -u btc-recorder.service -u btc-chainbook.service --since "@$(( $(python3 -c 'import json; print(json.load(open("/root/tz20-work/instants.json"))["start-rec"]["ns"] // 10**9)') - 5 ))" --no-pager -o short-iso
tail -n 40 /var/lib/btc-recorder/recorder.log
tail -n 40 /var/lib/btc-chainbook/service.log
cat /root/tz20-work/instants.json
systemctl show btc-recorder.service btc-chainbook.service -p MemoryMax -p MemoryCurrent -p MemoryPeak
free -b
du -sb /root/tz20-work /root/btc-recorder-svc /root/.claude
```

The journal holds systemd's own lines for the two units — starts, exits, scheduled restarts — since both
processes' output goes to their logs. `free -b` gives the host's total and available memory beside the two
units' own, which the next revision of map §6 records.

---

## 4. The gates — fixed here, before any of their data exists

| gate | population | PASS | false failure | power, against |
|---|---|---|---|---|
| **G-UNIT** | both units, at §3.5 step 1 with `0` restarts and at `I final` with `1` each | every check of §4.1 | `0` — systemd and `/proc` read directly | `1`, a process outside its unit's control group, under another argv, or beside a second instance |
| **G-START** | each unit's records since its start mark | every check of §4.2 | `0` | `1`, a start record that is not the one the unit names, or a gap left unrecorded |
| **G-CB** | the first `2` windows `T ≡ 0 (mod 900)` with `T + 625 >= start + 60` | both `window.json` present by `T + 965`, `documents_ok` true at 2 of 2, `missed` `0` at 2 of 2, `checkpoints_complete` summed at least `13` of `14` | `0.0084` if 1 checkpoint in 100 fails independently | `0.899` / `0.415` / `0.153` against 1 in 4 / 10 / 20 |
| **G-REC** | the first `6` intervals `T0 ≡ 0 (mod 300)` with `T0 − 90 >= start + 60` | `manifest.json` present by `T0 + 3,900` at 6 of 6, `quotes_complete` true at 6 of 6, `recorder_git_sha` `4216c04…` at 6 of 6, `complete` true at least 4 of 6 | at most `0.0153` | `1` against a broken path; `0.656` against `complete` failing 1 in 2 |
| **G-RESTART-C** | the chain book's records since its start mark | §4.5 | `0` | `1`, a `SIGTERM` that is not restarted |
| **G-RESTART-R** | the recorder's records since its start mark | §4.5 | `0` | `1`, the same |

**Family-wise false failure at most `0.024`**, the sum of G-CB's and G-REC's.

### 4.1 G-UNIT, per unit

`systemctl show` reads `ActiveState` `active`, `SubState` `running`, `UnitFileState` `enabled`, `FragmentPath`
`/etc/systemd/system/<unit>`, `ControlGroup` `/system.slice/<unit>`, `MemoryMax` `536870912` for the recorder and
`201326592` for the chain book, and `NRestarts` the count the step names — `MemoryCurrent` and `MemoryPeak` printed
and not gated;
`/proc/<MainPID>/cmdline` equals the unit's argv field for field — `/root/tz04a-env/venv/bin/python -B -u
recorder.py`, and `/root/tz01-env/venv/bin/python -B -u /root/tz18a-svc/tz18a-chainbook-capture.py --serve`;
the recorder's `/proc/<MainPID>/cwd` is `/root/btc-recorder-svc/research/recorder`; `/proc/<MainPID>/cgroup`
names `/system.slice/<unit>` and no path under `/user.slice`; and the MainPID is the only process with an
argument ending in `recorder.py`, or in `tz18a-chainbook-capture.py`. **The control group is the repair:** a
process in `system.slice` is not a member of any login session or user manager, so neither a logout nor
`Linger=no` reaches it.

### 4.2 G-START

**The recorder:** exactly one `start` record with `recv_ns` at or after the `start-rec` mark, sha
`4216c04673ced76b5b2ac60ef57c9abedc46f9b9`; exactly one `disconnect` record with reason `startup` detected at or
after the mark, **whose start lies in `[1790940810 × 10^9, 1790941110 × 10^9)` ns** — the old process's last
frame, which `last_frame_ns` reads off disk (lines 145–171, 535): after the window of `1790940900`, the newest
directory, opened, and before the window of `1790941200`, never created, would have — whose detection is at or
after the start record and whose end at or after its detection; and no `halt` record. That record is the gap,
recorded and not filled.

**The chain book:** exactly one record with `wall_ns` at or after the `start-cb` mark, a `start` whose `pid` is
the unit's MainPID, `commit` `ca4bbc1dd583cbb62f3c0c985938d229b526ce7e`, `file_sha256` `e9cb9b47…`, `argv`
`["/root/tz18a-svc/tz18a-chainbook-capture.py", "--serve"]`, and `config.headers` and `config.service_argv` as
§3.3 and §4.1 fix them (lines 585–611).

### 4.3 G-CB

The window rule is TZ-18a's `qualifies` with its 60 s lead (lines 334–340), the threshold its G-DEPLOY's 13 of
14 (TZ-18a §4), and completeness its `checkpoint_is_complete` — four replies at `200`, each JSON, received within
1 s of one another — as `window.json` counts it (lines 296–315, 744–745 and 769–781). No failure rate of this service has been
measured beyond TZ-18a's 14 of 14, so the false-failure figure is stated at 1 in 100; the three powers are
TZ-18a §4's literals, recomputed.

### 4.4 G-REC

`complete` is zero disconnects across the window with S6 and S7 present, and `quotes_complete` all 14 Tier C
reads at `200` and JSON (`manifest.py` lines 203–214). **False failure:** `complete` fails binomially at
`207 / 2,608` — TZ-16a's span, every non-member of it but one on `disconnect` (map §2.3) — so 3 or more of 6
fail with probability `0.00833`; `quotes_complete` failed at 0 of TZ-16a's 2,608, at most `3 / 2,608` a unit at
95%, so any of 6 fails with probability at most `0.00688`. The six intervals close within `2,280` s of the
start, before RTDS first closes the socket at `7,200` s (map §6), so the base rate overstates. The manifest's
sha is the start record active over each window (`recorder.py` lines 481–487, `manifest.py` line 225).

### 4.5 G-RESTART-C and G-RESTART-R

**Chain book:** since the `start-cb` mark the records are exactly `start`, `stop`, `start`; the first two carry
the MainPID the `kill-cb` mark recorded, the stop at or after that mark; the third a new pid, no more than 60 s
after the stop, with the same commit and file hash; and G-UNIT holds with `NRestarts` `1`. **Recorder:** since
the `start-rec` mark exactly two `start` records, the second at or after the `kill-rec` mark with sha
`4216c04…`; exactly two `startup` gaps, the second starting no earlier than 5 s before that mark and no later
than the second start, and lasting at most 60 s; no `halt`; and G-UNIT holds with `NRestarts` `1` and a MainPID
other than the one the mark recorded.

### 4.6 The stops — CANON hard rule 14

**On a FAIL of any gate that judges a unit, its stop is authorized and run at once,** by the classifier route of
§3 where refused:

**K-20R:**

```
systemctl disable --now btc-recorder.service; echo "exit=$?"
```

**K-20C:**

```
systemctl disable --now btc-chainbook.service; echo "exit=$?"
```

**Verification is the Executor's,** at least 30 s after the block: `systemctl is-active <unit>` prints
`inactive` or `failed`; `systemctl is-enabled <unit>` prints `disabled`; the unit's `pgrep -fx` prints no line
and `exit=1`; and, for the chain book, its `runtime.jsonl` ends with a `stop` of the last MainPID. The recorder
writes no `stop` record (TZ-19 report §3.3), and its absence is expected. **G-UNIT, G-START and G-RESTART-R
judge the recorder, G-REC too; G-UNIT, G-START, G-CB and G-RESTART-C judge the chain book.** A FAIL stops its
unit and no other, and the run continues through the other unit's gates, skipping any step that needs a PASS it
lacks. **Under PASS neither block is ever run. A BLOCK before B-START-REC starts nothing.**

### 4.7 What a PASS establishes, and what it does not

Both captures run as system units outside every session, capture complete intervals and windows, record their
own gap, and are restarted by systemd after a stray `SIGTERM`. **Not exercised:** a logout — structural, by the
control group of §4.1; the next TZ's host gate, run after this session has ended, is its first read — and a
reboot, for which both units are enabled under `multi-user.target`.

---

## 5. The instrument

`research/tz20-capture-under-systemd.py`, Appendix A, fixed by the Architect as this TZ's Validation and written
byte for byte. Standard library only, but for `path-recorder`, which loads `recorder.py`, `config.py` and
`websockets` from the recorder's own tree and interpreter. Its `reclaim` mode is §9's copy into the forensic
store, and it removes nothing. One mode per run; each prints its findings with UTC
stamps and ends with its PASS line. **An audit hook refuses any open under either capture root but the files
§2 item 2 names, and any open there for writing**, and every mode prints its count of such opens. It writes nothing
but `/root/tz20-work/instants.json` and, in `reclaim`, new files in `/root/btc-forensics/`. Exit `0` is a PASS; exit `1` a failed assert, named; exit `3` NOT YET.
Run with `-O` it refuses to start, because every check is an assert.

---

## 6. Cost

**Compute:** the heaviest read is the recorder's `runtime.jsonl` — `60,690` lines at TZ-19's read plus about
`2,880` a day — parsed once by each of `state`, `start`, `rec`, `restart-rec` and `final`; `rec` runs at most 13
times at 600 s spacing within its `3,900` s bound, and `cb` at most 5. That is at most `20` parses, each well
under 2 s at this size, under `40` s in all; `/proc` scans and `systemctl show` are milliseconds. `reclaim`
hashes at most the two old trees and this TZ's own — `27,510,104` bytes with this TZ's logs, under 1 s — against
the hex tokens of every committed report. **Wall clock:**
G-CB decides within `2,200` s of the start; G-REC's sixth interval opens no later than `start + 1,950` s
and decides by `start + 5,850` s at worst; B-KILL-REC waits at most `300` s. **About two hours, at most
`6,500` s from B-START-REC to `I final`.** No fail-fast bound applies: every gate decides on its own count.

---

## 7. Validation

| # | check | count |
|---|---|---|
| **V1** | §0.1's fingerprint | 6 anchors, 4 re-derived, 25 of 25 `frozen` equal |
| **V2** | §0.2's host gate | H1 to H8 and the resource gate, each read named |
| **V3** | `I state` | S1 to S7 |
| **V4** | §3.1's three files | 3 of 3 hashes, lines and bytes equal; the branch's diff against `origin/main` names exactly these three paths, all added, so no committed line is replaced |
| **V5** | §3.3's recorder tree | `HEAD` equal; 3 of 3 frozen hashes equal |
| **V6** | §3.3's request paths | P0 to P4 and P5 to P7; 4 HTTP requests through the chain book's `http_get`, 2 through the recorder's functions, SNTP at least 1 of 2, RTDS at least 2 of 4 topics |
| **V7** | B-INSTALL | 2 of 2 `cmp` equal; `daemon-reload` exit `0`; `systemd-analyze verify` recorded |
| **V8** | G-UNIT | 2 of 2 units at `0` restarts; 2 of 2 at `1` in `I final` |
| **V9** | G-START | 1 start and 1 gap for the recorder; 1 start record, 6 fields equal, for the chain book |
| **V10** | G-CB | 2 windows, their three counts |
| **V11** | G-REC | 6 intervals, their four counts |
| **V12** | G-RESTART-C and G-RESTART-R | each record sequence, pid pair and gap |
| **V13** | opens under the capture roots | every mode's printed count; any refusal is a failed run |
| **V14** | `I final` | both units, `NRestarts` `1`, sole instances, newest recorder start at `4216c04…` |
| **V15** | contract §4.2's self-check | run after the push and the pull request and before the report's commit |
| **V16** | §3.6's closing reads | every read printed |
| **V17** | §9's two `reclaim` runs | files considered, named by a report, kept by name, copied and already held, each counted; the store's count after equal to before plus the copies |
| **V18** | §9's removals | each `git worktree remove` exit `0`; `test -e` exit `1` for `/root/tz16a-work`, `/root/tz19-work` and `/root/tz20-work`; `git worktree list` naming the primary checkout and `/root/btc-recorder-svc` and nothing else |

---

## 8. The report

`CryptoReports/TZ-20-capture-under-systemd-report.md`, in contract §8's order. Beyond what V1 to V16 print:
every instant of `instants.json`; every block the classifier refused, who ran it and when; each gate's reading
with its deciding numbers; **the gap**: the start and end of each `startup` record G-START and G-RESTART-R read,
in `recv_ns` and UTC; the units' journal lines; each unit's memory in use and peak at every G-UNIT read and the
host's `free -b`; the commit and pull request; §9's counts and removals; and §0.3's free-space reads with their
instants and bound. A FAIL names the gate, the stop block run and its verification. **The report is drafted in
the primary checkout `/root/btc-5m-twap` before B-RECLAIM-OWN and committed after it**, so the removal of this
TZ's own tree is in it.

---

## 9. Reclaim — the host left clean (CANON hard rule 15)

**What a file is kept for:** a committed report prints its SHA-256, whole or as a prefix of 16 to 64 hex
characters, or it is named below. `reclaim` copies each such file into `/root/btc-forensics/` as
`<tree>--<path with / as -->`, by exclusive create, and verifies its hash; a name already there with the same
hash is counted as held, and with another hash is a failed assert. **Kept by name:**
`/root/tz16a-work/label-ledger.jsonl`, and `/root/tz20-work/instants.json` and every file under
`/root/tz20-work/logs/`. Everything else in a reclaimed tree is scratch the reports never cite, and goes.

**B-RECLAIM-OLD**, after §3.2 and before §3.3:

```
I reclaim /root/tz16a-work /root/tz19-work
git -C /root/btc-5m-twap worktree remove --force /root/tz16a-work/wt; echo "exit=$?"
git -C /root/btc-5m-twap worktree remove --force /root/tz16a-work/wt-report; echo "exit=$?"
git -C /root/btc-5m-twap worktree remove --force /root/tz19-work/wt-report; echo "exit=$?"
rm -rf /root/tz16a-work; echo "exit=$?"
rm -rf /root/tz19-work; echo "exit=$?"
test -e /root/tz16a-work; echo "exit=$?"; test -e /root/tz19-work; echo "exit=$?"
```

`reclaim` must print `RECLAIM PASS` before any removal runs; a worktree or tree already absent is recorded and
skipped. `--force` is safe here and only here: `reclaim` has already preserved every file a report cites, and a
worktree's tracked files are in git.

**B-RECLAIM-OWN**, last, after §3.6 and with the report drafted:

```
I reclaim /root/tz20-work
git -C /root/btc-5m-twap worktree remove --force /root/tz20-work/wt; echo "exit=$?"
rm -rf /root/tz20-work; echo "exit=$?"
test -e /root/tz20-work; echo "exit=$?"
git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
find /root/btc-forensics -type f | wc -l
```

The branch `tz-20-capture-under-systemd` is pushed before this block and stays, on `origin` and as a local
ref; only its working tree goes. **Kept:** `/root/btc-recorder-svc` and `/root/tz18a-svc` are the two units'
code — no TZ removes either while its unit is enabled — and the capture and the forensic store are data, never
scratch (map §6, TZ-09 §5). **A refused `rm -rf` is handed to the Boss** by §3's route, one tree per command,
and verified by `test -e`.

---
## 10. Pre-send checks

Performed on 2026-10-03 against this file, in a reading separate from its writing, with `origin/main` at
`b96be84a2a5e417a5ab8c00fbaf7591f8e4015e2` read directly, and against `SYSTEM-MAP.md` revision `2026-10-04-a`,
the file uploaded with this TZ. Line numbers are `origin/main`'s.

### C1 — scope against body

| named in the body | how | intersects, by path or by content class | resolution |
|---|---|---|---|
| `deploy/systemd/btc-recorder.service`, `deploy/systemd/btc-chainbook.service`, `research/tz20-capture-under-systemd.py` | written, branch | P1 by path | new files; P1 binds committed files |
| `CryptoReports/TZ-20-capture-under-systemd-report.md` | written, `main` | P5 | P5's own exemption |
| this TZ, `SYSTEM-MAP.md`, the 28 table paths | read, hashed | — | — |
| `/root/btc-recorder-svc/research/recorder/{recorder,config,manifest}.py` | hashed, imported by `path-recorder` | — | a worktree at `4216c04`, written by §3.3 alone |
| `/root/tz18a-svc/tz18a-chainbook-capture.py`, `commit.txt` | hashed, imported by `path-chainbook`, run by the unit | P4 by path | read and executed, never modified |
| `/var/lib/btc-recorder/runtime.jsonl`, six `manifest.json` | read | P2 by path | P2's own text |
| `/var/lib/btc-chainbook/runtime.jsonl`, two `window.json` | read | P2 by path; P6 by class: token ids | P2's own text; map §2.5's exception |
| `recorder.log`, `service.log` | `tail -n 40` | P2 by path | P2's exemption (b); statuses, counts, times, no price |
| `/var/lib/btc-recorder/**`, `/var/lib/btc-chainbook/**` | written by the units | P3 | P3 names "this TZ's commands"; §2's host paths name the units' writes |
| the live documents, books and RTDS frames of §3.3 | requested, parsed | P6 by class: prices, outcomes | P6's exemption: status, bytes, SHA-256, parse, token ids, frame count and topics |
| `/etc/systemd/system/btc-*.service` and their enablement links | written | P9 | P9 names the two units as this TZ's |
| `/root/tz20-work/**`, `/root/btc-5m-twap/.git` | written | — | §2's host paths; `git worktree add` ×2 |
| `/root/tz16a-work`, `/root/tz19-work`, `/root/btc-forensics`, `/root/PROJECT_GAMING_PS5`, `/etc/systemd/logind.conf` | `test -e`, `find`, `du`, `grep` | P4 | reads only |
| `/proc/**` | `cmdline`, `cwd`, `cgroup` | — | reads |
| B-KILL-CB, B-KILL-REC, K-20R, K-20C | signal, stop | P8 | P8's own text |
| `telemetry-watch.service` | `systemctl is-enabled`, `is-active` | P9 | read only |
| the report | output | P6 by class | instants, pids, counts, statuses, hashes, token ids, memory figures; no price, outcome or label |
| `/root/btc-5m-twap/CryptoReports/*.md` | read by `reclaim` for hex tokens | P6 by class: reports print prices and outcomes | P6's §9 exemption, hex runs alone |
| `/root/tz16a-work/**`, `/root/tz19-work/**`, `/root/tz20-work/**` | hashed, named files copied, then removed | P6 by class: run outputs hold prices and labels; §2's removal list | P6's §9 exemption, whole files, no value extracted; named in the removal list |
| `/root/btc-forensics/` | exclusive create; counted | P4 | P4's exemption |

**20 entries. 9 intersections, each closed by a prohibition's own text, a named exemption or §2's removal list**
— the two `runtime.jsonl` and the eight `manifest.json` and `window.json`, the two logs, the units' writes, the
live bodies, the unit files, the two signals, the reports' tokens, the reclaimed trees, the forensic copies. None
open.

### C2 — origin of every expectation

| class | the fixed expectations |
|---|---|
| computed by an implementation independent of the one under test, exact | `536870912` = `512 × 2^20` and `201326592` = `192 × 2^20`, systemd's reading of `512M` and `192M`; `27,510,104` = `22,398,514 + 4,111,590 + 1,000,000`; the three Appendix A hashes, lines and bytes — `sha256sum`, `wc` on the files this session wrote; `GAP_LO_NS` = `(1790940900 − 90) × 10^9` and `GAP_HI_NS` = `(1790941200 − 90) × 10^9`, from `PRE_S = 90` (`config.py` line 17); `0.00833`, `0.00688`, `0.0153`, `0.0084`, `0.024`, `0.656` and the three G-CB powers in `Fraction`, the powers equal to TZ-18a §4's 30-place literals; `2,260,000,000` = `2,200,000,000 + 60,000,000`; the window and interval rules, integer arithmetic |
| quoted from a committed artifact, named | `60,690`, `1789206785264516934`, `1790940944342950552`, `4` records, `2699889`, `1791017775066372007`, `1790940900`, `3,885`, `1790853000` — TZ-19 report §1.2 and §3.2; `1,072` — §1.1; `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` — map §0 and §6; `ca4bbc1dd583cbb62f3c0c985938d229b526ce7e` — `refs/pull/19/head`, TZ-18a §3.5; `e9cb9b47…`, `9fd1c7de…`, `8111dfe4…`, `79c99010…` — map §0's frozen rows; the two headers — `tz18a-chainbook-capture.py` lines 99–100; `/dev/vda2`, `31612203008` — map §6; `207 / 2,608` — map §2.3; `240` — systemd's own release notes for `append:`; `177.0M` — TZ-19 report §3.2;
`22,398,514` and `4,111,590` — TZ-19 report §1.5 |
| depending on a quantity this TZ measures | **none.** G-START's gap bound is an inequality that holds for every instant the old process could have died at, given the newest directory and the absent one |

### C3 — shape of every diff

Three new files and no committed line replaced: **none**. V4 asserts the branch's diff names exactly those
three paths, all added.

### C4 — cost of every check

| check | population at its upper bound | evaluations | seconds |
|---|---|---|---|
| parse of the recorder's `runtime.jsonl` | `60,690` lines at TZ-19's read plus `2,880` a day of capture: at most `62,000` in this session | at most `20` parses | measured in this session at `0.232` s for `60,690` lines of `12,684,156` bytes, `54.6` MB/s; bounded at `2` s a parse for a host up to eight times slower: at most `40` |
| parse of the chain book's `runtime.jsonl` | at most `7` records | at most `20` | under `0.01` each |
| `manifest.json` and `window.json` reads | `6` and `2` files | at most `13` and `5` runs | milliseconds |
| `/proc` scans | every process on the host | at most `12` | under `0.1` each |
| `systemctl show` | two units | at most `14` calls | milliseconds |
| `reclaim`'s hashing | the two old trees and this TZ's own, at most `27,510,104` bytes, and the reports' tokens over `1,963,567` bytes of 31 reports at `b96be84` | 2 runs | under `1` each at the measured `54.6` MB/s of parsing; hashing is faster |

**At most about `47` s of compute in all**, far under `3,600`. Wall clock is §6's. No fail-fast bound exists to
derive.

### C5 — every count

V1: 6 anchors and 4 re-derivable — `A2`, `A4`, `A5`, `A6` — and 25 `frozen` of the map's 28 rows, counted in
revision `2026-10-04-a`'s table. V3: S1 to S7, seven, `mode_state`'s seven labelled groups. V4: 3, Appendix A's
three blocks. V5: 3 hashes, §3.3's `sha256sum` line. V6: P0 to P7, `mode_path_recorder`'s five and
`mode_path_chainbook`'s three; HTTP `2 + 4 = 6`, P1 and P2 and P6's two and P7's two; SNTP over
`config.NTP_SERVERS`, 2. V7: 2 `cmp`. V8: 2 units at each of two instants. V9: recorder 1 + 1; chain book 1
record and 6 fields — `pid`, `commit`, `file_sha256`, `argv`, `headers`, `service_argv`. V10: 2 windows × 7
checkpoints = 14, `CHECKPOINT_OFFSETS`' 7 (`tz18a-chainbook-capture.py` line 86). V11: 6 intervals. V17: 2
`reclaim` runs, five counts each. V18: 4 worktrees removed — `/root/tz16a-work/wt`, `/root/tz16a-work/wt-report`,
`/root/tz19-work/wt-report` and `/root/tz20-work/wt`, of the 6 registered once §3.1 and §3.3 have added two to
TZ-19's four (TZ-19 report §1.5) — leaving 2, the primary checkout and `/root/btc-recorder-svc`; 3 trees gone.

### C6 — every population

G-UNIT: the two units' MainPIDs at §3.5 step 1, `restart-cb`, `restart-rec` and `final`. G-START: each runtime
file's records at or after its start mark. G-CB: the first two windows `T ≡ 0 (mod 900)` with
`T + 625 >= start + 60`, `start` the new chain book start record. G-REC: the first six `T0 ≡ 0 (mod 300)` with
`T0 − 90 >= start + 60`, `start` the new recorder start record. G-RESTART-C and -R: each runtime file's records
since its start mark. `reclaim`: every regular file under the trees it is given, against the hex runs of every
committed report. The false-failure rates: Bernoulli models over G-REC's 6 and G-CB's 14 units, at the base
rates of TZ-16a's 2,608 units considered. V13: every open under the two capture roots in each mode run. S3 and
S4: the two runtime files whole.

### C7 — every signature and every behaviour

Read at `b96be84`.

- `recorder.py:50` `def git_sha():` — "reads `HEAD` of the checkout `recorder.py` sits in": lines 51–55,
  `here = os.path.dirname(os.path.abspath(__file__))` … `["git", "-C", here, "rev-parse", "HEAD"]` …
  `return out.stdout.strip() if out.returncode == 0 else "unknown"`.
- `recorder.py:196` `def fetch(url, timeout=15):` — "served, parsed": 198–200, the `User-Agent` header and
  `return resp.read()`; an HTTP error raises from `urlopen`, which P1 turns into its assert.
- `recorder.py:203` `def fetch_status(url, timeout=15):` — "status and body": 211–216,
  `return resp.status, resp.read().decode("utf-8", "replace")` and, on `HTTPError`,
  `return err.code, err.read().decode("utf-8", "replace")`.
- `recorder.py:123` `def sntp_best(host, burst=NTP_BURST):` — five values: line 130
  `ip = socket.gethostbyname(host)`, which can raise and which P3 catches; 140
  `return ip, None, None, 0, rejected`; 142 `return ip, offset, rtt, len(samples), rejected`.
- `recorder.py:145` `def last_frame_ns(root):` — "the old process's last frame": 151–155, the newest four
  directories of the series; 171 `return newest`; 535
  `down_since, detected, reason = last_frame_ns(config.ROOT), time.time_ns(), "startup"`; 542–544 the record.
- `Recorder.main` — start record before the socket: 582–583 the `start` record, 586–588
  `if not self.check_floors("start-up"):` … `return 1`, 589–590 `recover()` and then the `rtds()` task, 598
  `return 0`; 273 the `halt` record.
- `recorder.py:531–539` — the subscription message and `websockets.connect(config.RTDS_URL, open_timeout=20,
  ping_interval=None, max_size=None)`, copied in `path-recorder`.
- `recorder.py:481–487` and `manifest.py:225` — the manifest's sha, from the start record active over the
  window; `manifest.py:203–214` — `quotes_complete` and `complete`; 218, 230, 231 the keys G-REC reads.
- `config.py:111` `def slug_for(t0):` — `return "%s-%d" % (SERIES, t0)`; 43 `USER_AGENT`; 17 `PRE_S = 90`.
- `tz18a-chainbook-capture.py:423` `def http_get(url, timeout=READ_TIMEOUT_S):` — 429 `bump("requests")`;
  457–467 the dict with `status`, `bytes`, `sha256`, `raw` and `reason`.
- `:411` `def build_request(url):` — 419–420, `headers={"Accept": ACCEPT, "User-Agent": USER_AGENT}`.
- `:480` `def token_ids_of(doc_raw):` — 493 and 497 `return None, None, verbatim`, 499
  `return ids, labels, verbatim`; `ids is not None` means two distinct non-empty ids (494–497).
- `:792` `def mode_serve(args, out):` — 798–802 D10 `return 2`; 807–809 `return 3`; 810–811 the `SIGTERM`
  handler, 509–510 `STOP.set()`; 812 the `start` record; 820–827 the loop, the `stop` record in `finally`
  and `return 0`. 1683 `raise SystemExit(main())`, so the return value is the exit status; an assert raised
  in `run_window` — 219 the write cap, 231 the floor — leaves through `finally` as exit `1`.
- `:585` `def runtime_record(event, extra=None):` — 586–606 `pid`, `wall_ns`, `commit`, `file_sha256`,
  `argv` = `list(sys.argv)`, `config.headers`, `config.service_argv`; 611 `return rec`.
- `:334` `def qualifies(…)` — 336–340; `:296` `def checkpoint_is_complete(entries):` — 297–314; 744–745 the
  count; 769–781 `window.json`.
- `:787` `def next_window(now):` — 789 `return T0 if now <= T0 + DOC_OFFSET - 1 else T0 + WINDOW`, so a
  restart before `T + 624` runs the window at `T`: B-KILL-CB's instant loses no window.

Every sentence of the body that attributes a behaviour to one of these was checked against the lines above.

### C8 — every cross-reference

TZ-19 report §1.1 (the host gate, `1,072`), §1.2 (R-READY), §2 (the blocker), §3.2 (the stop evidence) and
§3.3 (the figures); TZ-18a §3.5 (`setsid nohup`, `commit.txt`), §4 (G-DEPLOY and its powers) and §6.1 (K-18a);
the TZ-05a report (`recorder.log`); TZ-19 report §1.5 (the trees' sizes, four worktrees); map §0, §1, §2.3, §2.5,
§3, §6 and §7 items 85 and 86 of revision `2026-10-04-a`; TZ-09 §5 (the capture is never deleted); CANON §1.1
(no replay), PART III (fingerprint gates, hard rules 14 and 15) and PART IV (systemd), of revision
`2026-10-04-a`; contract §1, §4.2 and §8; and this TZ's §0.2 to §9 and Appendix A. Each was read,
and each supports the sentence that cites it.

### Checks this session could not perform

- **The venue paths were exercised from this session at 2026-10-03 23:34–23:35 UTC**, through the instrument
  itself against `recorder.py` at `4216c04` and the chain book's frozen file: P0, P1, P2 and P4 to P7 passed —
  both documents and both books served `200` under each process's own `User-Agent`, and RTDS delivered all four
  topics within 30 s. **SNTP could not be:** this session's sandbox passes no UDP, so P3 failed here as it
  must. The host is not this session, so §3.3 runs every path again there and BLOCKS before anything is
  installed.
- **systemd on the VPS** — its version and the units' behaviour — is the host's. Both unit files passed
  `systemd-analyze verify` under systemd 255 in this session, which reported only the absent interpreters.
  H4, G-UNIT and the two restart gates are the conditions.
- **The instrument** ran in this session against a simulated host — dummy processes under the exact argv, a
  stand-in `systemctl`, fixture logs of the real shape — through every mode, both NOT YET paths, both FAIL
  boundaries and the audit hook's refusals. `/proc/<pid>/cgroup` cannot be simulated, so G-UNIT's control-group
  assertion is first evaluated on the host.
- **The host's own state** — the two runtime files, `commit.txt`, the trees — is S3 to S7 and H1 to H8. Which
  files of the old trees a report names is the host's too: `reclaim` prints every file it copies or finds held,
  and asserts the store's count.
- **The units' memory** has not been measured on the host. The ceilings stand far above the one figure read —
  `177.0M` for the recorder's whole session — and G-UNIT prints the memory in use and the peak at every read.

---

## Appendix A — the three files, byte for byte

Extracted by §3.1's script; each block's content is the file.

### A.1 `deploy/systemd/btc-recorder.service`

```text file=deploy/systemd/btc-recorder.service
# btc-5m-twap: the recorder, Tier A and Tier C, as a system unit (TZ-20).
# Installed byte for byte as /etc/systemd/system/btc-recorder.service.
[Unit]
Description=btc-5m-twap recorder, Tier A and Tier C
Wants=network-online.target
After=network-online.target time-sync.target
StartLimitIntervalSec=3600
StartLimitBurst=5

[Service]
Type=simple
WorkingDirectory=/root/btc-recorder-svc/research/recorder
Environment=HOME=/root
ExecStart=/root/tz04a-env/venv/bin/python -B -u recorder.py
Restart=always
RestartSec=5
RestartPreventExitStatus=0
MemoryMax=512M
StandardOutput=append:/var/lib/btc-recorder/recorder.log
StandardError=append:/var/lib/btc-recorder/recorder.log

[Install]
WantedBy=multi-user.target
```

### A.2 `deploy/systemd/btc-chainbook.service`

```text file=deploy/systemd/btc-chainbook.service
# btc-5m-twap: the chain book, TZ-18a's service, as a system unit (TZ-20).
# Installed byte for byte as /etc/systemd/system/btc-chainbook.service.
[Unit]
Description=btc-5m-twap chain book, fifteen-minute and five-minute books
Wants=network-online.target
After=network-online.target time-sync.target
StartLimitIntervalSec=3600
StartLimitBurst=5

[Service]
Type=simple
WorkingDirectory=/root/tz18a-svc
ExecStart=/root/tz01-env/venv/bin/python -B -u /root/tz18a-svc/tz18a-chainbook-capture.py --serve
Restart=always
RestartSec=5
RestartPreventExitStatus=1 2 3
MemoryMax=192M
StandardOutput=append:/var/lib/btc-chainbook/service.log
StandardError=append:/var/lib/btc-chainbook/service.log

[Install]
WantedBy=multi-user.target
```

### A.3 `research/tz20-capture-under-systemd.py`

```python file=research/tz20-capture-under-systemd.py
#!/usr/bin/env python3
"""TZ-20 - the capture under systemd: every check the TZ fixes, one mode per run.

    state            section 0.2   the host before anything is installed or started
    path-recorder    section 3.3   one live request per endpoint through the recorder's own functions
    path-chainbook   section 3.3   the same through the chain book's own http_get
    mark NAME        section 3.4   records an instant and both units' MainPID in instants.json
    unit N           G-UNIT        both units running from systemd, N restarts each
    start            G-START       the two new start records and the recorded gap
    cb               G-CB          the first two qualifying chain book windows
    rec              G-REC         the first six qualifying recorder intervals
    restart-cb       G-RESTART-C   one SIGTERM to the chain book, and systemd's restart
    restart-rec      G-RESTART-R   one SIGTERM to the recorder, and systemd's restart
    final            section 3.5   both units at the end of the session
    reclaim TREE...  section 9     copies into the forensic store what a committed report names by hash

Under the two capture roots it opens the two top-level runtime.jsonl files, the manifest.json of
G-REC's six intervals and the window.json of G-CB's two windows, read-only, and nothing else: an
audit hook refuses any other open there. It writes /root/tz20-work/instants.json, and in `reclaim`
new files under /root/btc-forensics/ by exclusive create; nothing else. It prints no price,
size, spread, mid, book level or outcome. Exit 0: every assert of the mode held. Exit 1: an assert
failed, and its message names it. Exit 3: NOT YET, with the instant to run the mode again.

Written for CryptoTZ/TZ-20-capture-under-systemd.md. The TZ is the specification.
"""

import hashlib
import json
import math
import os
import re
import subprocess
import sys
import time
import urllib.error

if not __debug__:
    sys.stderr.write("tz20: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(2)

REC_UNIT = "btc-recorder.service"
CB_UNIT = "btc-chainbook.service"
REC_ARGV = ["/root/tz04a-env/venv/bin/python", "-B", "-u", "recorder.py"]
CB_FILE = "/root/tz18a-svc/tz18a-chainbook-capture.py"
CB_ARGV = ["/root/tz01-env/venv/bin/python", "-B", "-u", CB_FILE, "--serve"]
REC_CWD = "/root/btc-recorder-svc/research/recorder"
REC_ROOT = "/var/lib/btc-recorder"
REC_RUNTIME = REC_ROOT + "/runtime.jsonl"
REC_SERIES = REC_ROOT + "/btc-updown-5m"
CB_ROOT = "/var/lib/btc-chainbook"
CB_RUNTIME = CB_ROOT + "/runtime.jsonl"
INSTANTS = "/root/tz20-work/instants.json"
UNIT_DIR = "/etc/systemd/system"
FORENSICS = "/root/btc-forensics"
REPORTS = "/root/btc-5m-twap/CryptoReports"
RECLAIMABLE = ("/root/tz16a-work", "/root/tz19-work", "/root/tz20-work")
REC_MEMORY_MAX = 536870912      # MemoryMax=512M in btc-recorder.service
CB_MEMORY_MAX = 201326592       # MemoryMax=192M in btc-chainbook.service

SHA_RECORDER = "4216c04673ced76b5b2ac60ef57c9abedc46f9b9"
CB_COMMIT = "ca4bbc1dd583cbb62f3c0c985938d229b526ce7e"
CB_FILE_SHA = "e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae"
CB_HEADERS = [["Accept", "application/json"], ["User-Agent", "btc-5m-twap-tz18a"]]

# The state TZ-19's report read on 2026-10-03 (its sections 3.2 and 3.3).
OLD_REC_NEWLINES = 60690
OLD_REC_START_NS = 1789206785264516934
OLD_REC_LAST_NS = 1790940944342950552
OLD_CB_RECORDS = 4
OLD_CB_PID = 2699889
OLD_CB_STOP_NS = 1791017775066372007
# The old recorder's last frame lies after the window of 1790940900 opened and before the window
# of 1790941200 would have opened: that directory was never created.
GAP_LO_NS = 1790940810 * 10 ** 9
GAP_HI_NS = 1790941110 * 10 ** 9

REC_UNITS = 6
REC_COMPLETE_MIN = 4
REC_LEAD_S = 60
REC_DEADLINE_S = 3900
CB_UNITS = 2
CB_CHECKPOINTS = 7
CB_COMPLETE_MIN = 13
CB_LEAD_S = 60
CB_DEADLINE_S = 965
RESTART_GAP_NS = 60 * 10 ** 9
KILL_SLACK_NS = 5 * 10 ** 9

OPENS = []


def _allowed(path):
    """The only files this instrument opens under the two capture roots."""
    if path in (REC_RUNTIME, CB_RUNTIME):
        return True
    head, name = os.path.split(path)
    parent, interval = os.path.split(head)
    if name == "manifest.json" and parent == REC_SERIES and interval.isdigit():
        return True
    if name == "window.json" and parent == CB_ROOT and interval.isdigit():
        return True
    return False


def _audit(event, args):
    """V13 - under either capture root only the named files are opened, and only to read."""
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
                raise RuntimeError("V13: open refused under a capture root: %s %r" % (path, mode))
            OPENS.append(path)


sys.addaudithook(_audit)


def out(msg):
    sys.stdout.write("[%s] %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    sys.stdout.flush()


def utc(seconds):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(seconds))


def sha256_file(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def read_jsonl(path):
    """Every parseable record, the torn-line count, and the newline count, in file order."""
    with open(path, "rb") as fh:
        raw = fh.read()
    recs, torn = [], 0
    for line in raw.split(b"\n"):
        if not line.strip():
            continue
        try:
            recs.append(json.loads(line))
        except ValueError:
            torn += 1
    return recs, torn, raw.count(b"\n"), raw.endswith(b"\n")


def proc_argvs():
    found = {}
    for name in os.listdir("/proc"):
        if not name.isdigit():
            continue
        try:
            with open("/proc/%s/cmdline" % name, "rb") as fh:
                raw = fh.read()
        except OSError:
            continue
        fields = raw.split(b"\0")
        if fields and fields[-1] == b"":
            fields = fields[:-1]
        found[int(name)] = fields
    return found


def recorder_like(found):
    """tz10b.recorder_pids's rule: every process with an argument ending in recorder.py."""
    return sorted(p for p, a in found.items() if any(x.endswith(b"recorder.py") for x in a))


def chainbook_like(found):
    return sorted(p for p, a in found.items()
                  if any(x.endswith(b"tz18a-chainbook-capture.py") for x in a))


PROPS = ("ActiveState", "SubState", "UnitFileState", "FragmentPath", "ControlGroup",
         "MainPID", "NRestarts", "Result", "ExecMainStartTimestamp", "MemoryMax",
         "MemoryCurrent", "MemoryPeak")


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


def main_pid(unit):
    try:
        return int(show(unit).get("MainPID") or 0)
    except AssertionError:
        return 0


def check_unit(unit, argv, cwd, restarts, memory_max):
    """G-UNIT for one unit. Returns the MainPID. Memory in use is printed, not gated."""
    props = show(unit)
    out("U %s %s" % (unit, json.dumps(props, sort_keys=True)))
    assert props.get("ActiveState") == "active", "G-UNIT %s: ActiveState %r" % (
        unit, props.get("ActiveState"))
    assert props.get("SubState") == "running", "G-UNIT %s: SubState %r" % (
        unit, props.get("SubState"))
    assert props.get("UnitFileState") == "enabled", "G-UNIT %s: UnitFileState %r" % (
        unit, props.get("UnitFileState"))
    assert props.get("FragmentPath") == UNIT_DIR + "/" + unit, "G-UNIT %s: FragmentPath %r" % (
        unit, props.get("FragmentPath"))
    assert props.get("ControlGroup") == "/system.slice/" + unit, "G-UNIT %s: ControlGroup %r" % (
        unit, props.get("ControlGroup"))
    assert props.get("NRestarts") == str(restarts), "G-UNIT %s: NRestarts %r, expected %d" % (
        unit, props.get("NRestarts"), restarts)
    assert props.get("MemoryMax") == str(memory_max), "G-UNIT %s: MemoryMax %r, expected %d" % (
        unit, props.get("MemoryMax"), memory_max)
    pid = int(props.get("MainPID") or 0)
    assert pid > 0, "G-UNIT %s: no MainPID" % unit
    with open("/proc/%d/cmdline" % pid, "rb") as fh:
        fields = fh.read().split(b"\0")
    if fields and fields[-1] == b"":
        fields = fields[:-1]
    got = [f.decode("utf-8") for f in fields]
    assert got == argv, "G-UNIT %s: pid %d argv %r is not %r" % (unit, pid, got, argv)
    if cwd is not None:
        here = os.readlink("/proc/%d/cwd" % pid)
        assert here == cwd, "G-UNIT %s: pid %d cwd %r is not %r" % (unit, pid, here, cwd)
    with open("/proc/%d/cgroup" % pid) as fh:
        lines = fh.read().splitlines()
    paths = [line.split(":", 2)[2] for line in lines if line.count(":") >= 2]
    assert "/system.slice/" + unit in paths, "G-UNIT %s: pid %d cgroups %r" % (unit, pid, paths)
    assert not any(p.startswith("/user.slice") for p in paths), \
        "G-UNIT %s: pid %d is inside a user slice: %r" % (unit, pid, paths)
    out("G-UNIT %s: pid %d, argv equal, cgroup %s, NRestarts %d, MemoryMax %d; memory in use %s, "
        "peak %s (recorded)" % (unit, pid, "/system.slice/" + unit, restarts, memory_max,
                                props.get("MemoryCurrent"), props.get("MemoryPeak")))
    return pid


def check_both(restarts):
    rec_pid = check_unit(REC_UNIT, REC_ARGV, REC_CWD, restarts, REC_MEMORY_MAX)
    cb_pid = check_unit(CB_UNIT, CB_ARGV, None, restarts, CB_MEMORY_MAX)
    found = proc_argvs()
    assert recorder_like(found) == [rec_pid], "G-UNIT: recorder processes %r, expected [%d]" % (
        recorder_like(found), rec_pid)
    assert chainbook_like(found) == [cb_pid], "G-UNIT: chain book processes %r, expected [%d]" % (
        chainbook_like(found), cb_pid)
    out("G-UNIT PASS: 2 of 2 units, sole instances %d and %d, NRestarts %d each" % (
        rec_pid, cb_pid, restarts))
    return rec_pid, cb_pid


def load_marks():
    with open(INSTANTS, encoding="utf-8") as fh:
        return json.load(fh)


def mark_ns(marks, name):
    assert name in marks, "mark %r was never recorded" % name
    return marks[name]["ns"]


def not_yet(again_s, what):
    out("NOT YET: %s; run this mode again at or after %s" % (what, utc(again_s)))
    sys.exit(3)


# ---------------------------------------------------------------------------------------------

def mode_state():
    found = proc_argvs()
    rl, cl = recorder_like(found), chainbook_like(found)
    out("S1 processes with an argument ending in recorder.py: %r" % rl)
    out("S2 processes with an argument ending in tz18a-chainbook-capture.py: %r" % cl)
    assert rl == [], "S1: a recorder process runs: %r" % rl
    assert cl == [], "S2: a chain book process runs: %r" % cl

    recs, torn, newlines, terminated = read_jsonl(REC_RUNTIME)
    starts = [r for r in recs if r.get("kind") == "start"]
    stops = [r for r in recs if r.get("kind") == "stop"]
    out("S3 %s: %d newlines, %d records, %d torn, %d start, %d stop, ends with a newline %s"
        % (REC_RUNTIME, newlines, len(recs), torn, len(starts), len(stops), terminated))
    out("S3 newest start %s" % json.dumps(starts[-1], sort_keys=True))
    out("S3 last record %s" % json.dumps(recs[-1], sort_keys=True))
    assert newlines == OLD_REC_NEWLINES, "S3: %d newlines, TZ-19 read %d" % (
        newlines, OLD_REC_NEWLINES)
    assert terminated, "S3: the recorder's runtime.jsonl does not end with a newline"
    assert starts[-1].get("recv_ns") == OLD_REC_START_NS, "S3: newest start %r" % starts[-1]
    assert starts[-1].get("sha") == SHA_RECORDER, "S3: newest start sha %r" % starts[-1]
    assert recs[-1].get("recv_ns") == OLD_REC_LAST_NS, "S3: last record %r" % recs[-1]

    cbr, cb_torn, _n, cb_terminated = read_jsonl(CB_RUNTIME)
    for i, r in enumerate(cbr, 1):
        out("S4 %d %s pid %s wall_ns %s %s" % (i, r.get("event"), r.get("pid"), r.get("wall_ns"),
                                             utc(r.get("wall_ns", 0) / 1e9)))
    assert cb_torn == 0 and cb_terminated, "S4: chain book runtime.jsonl torn %d" % cb_torn
    assert len(cbr) == OLD_CB_RECORDS, "S4: %d records, TZ-19 read %d" % (len(cbr),
                                                                        OLD_CB_RECORDS)
    last = cbr[-1]
    assert last.get("event") == "stop" and last.get("pid") == OLD_CB_PID \
        and last.get("wall_ns") == OLD_CB_STOP_NS, "S4: last record %r" % last

    for path in (UNIT_DIR + "/" + REC_UNIT, UNIT_DIR + "/" + CB_UNIT, "/root/btc-recorder-svc"):
        assert not os.path.lexists(path), "S5: %s exists" % path
        out("S5 %s absent" % path)
    got = sha256_file(CB_FILE)
    assert got == CB_FILE_SHA, "S6: %s sha256 %s" % (CB_FILE, got)
    with open("/root/tz18a-svc/commit.txt", "rb") as fh:
        commit = fh.read()
    assert commit == (CB_COMMIT + "\n").encode("ascii"), "S6: commit.txt %r" % commit
    out("S6 %s sha256 %s, commit.txt %s" % (CB_FILE, got, CB_COMMIT))
    for path in (REC_ARGV[0], CB_ARGV[0]):
        assert os.access(path, os.X_OK), "S7: %s is not executable" % path
        out("S7 %s executable" % path)
    out("STATE PASS: S1 to S7")


def mode_path_recorder():
    import asyncio
    sys.path.insert(0, REC_CWD)
    import config
    import recorder
    import websockets

    src = os.path.realpath(recorder.__file__)
    assert src == os.path.join(REC_CWD, "recorder.py"), "P0: recorder loaded from %s" % src
    assert os.path.realpath(config.__file__) == os.path.join(REC_CWD, "config.py"), \
        "P0: config loaded from %s" % config.__file__
    sha = recorder.git_sha()
    assert sha == SHA_RECORDER, "P0: git_sha() %r" % sha
    out("P0 recorder.py %s, git_sha %s, websockets %s, User-Agent %r"
        % (src, sha, websockets.__version__, config.USER_AGENT))

    now = int(time.time())
    t0 = now - now % config.INTERVAL_S
    if now - t0 < 30:
        t0 -= config.INTERVAL_S              # an interval open for at least 30 s
    url = config.GAMMA_MARKET_BY_SLUG.format(slug=config.slug_for(t0))
    try:
        body = recorder.fetch(url)
    except urllib.error.HTTPError as exc:
        raise AssertionError("P1: %s answered HTTP %d" % (url, exc.code))
    doc = json.loads(body)
    market = doc[0] if isinstance(doc, list) else doc
    ids = json.loads(market["clobTokenIds"])
    assert isinstance(ids, list) and len(ids) == 2 and all(ids), "P1: clobTokenIds %r" % (ids,)
    out("P1 %s: served, %d bytes, JSON, token ids %s" % (url, len(body), ids))

    book = config.CLOB_BOOK_BY_TOKEN.format(token_id=ids[0])
    status, text = recorder.fetch_status(book, recorder.QUOTE_TIMEOUT_S)
    assert status == 200, "P2: %s status %r" % (book, status)
    json.loads(text)
    out("P2 %s: status %d, %d bytes, JSON" % (book, status, len(text.encode("utf-8"))))

    answered = 0
    for host in config.NTP_SERVERS:
        try:
            ip, offset, rtt, accepted, rejected = recorder.sntp_best(host)
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
        # recorder.py lines 531-533 and 538-539, verbatim in effect: the same subscription
        # message from config.TIER_A, the same URL and the same connect arguments.
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
    out("PATH-RECORDER PASS: P0 to P4")


def mode_path_chainbook():
    import importlib.util
    got = sha256_file(CB_FILE)
    assert got == CB_FILE_SHA, "P5: %s sha256 %s" % (CB_FILE, got)
    spec = importlib.util.spec_from_file_location("tz18a_chainbook", CB_FILE)
    cb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cb)
    assert list(cb.SERVICE_ARGV) == CB_ARGV, "P5: SERVICE_ARGV %r" % (cb.SERVICE_ARGV,)
    req = cb.build_request(cb.GAMMA_MARKET_URL.format(slug="x"))
    out("P5 %s sha256 %s; build_request headers %s" % (CB_FILE, got, sorted(req.header_items())))

    now = int(time.time())
    t15 = now - now % 900 if now % 900 >= 30 else now - now % 900 - 900
    t5 = now - now % 300 if now % 300 >= 30 else now - now % 300 - 300
    slugs = ["btc-updown-15m-%d" % t15, "btc-updown-5m-%d" % t5]
    ids_of = {}
    for i, slug in enumerate(slugs):
        if i:
            time.sleep(cb.DOC_GAP_S)
        res = cb.http_get(cb.GAMMA_MARKET_URL.format(slug=slug))
        assert res["status"] == 200 and res["bytes"] > 0, "P6: %s status %r bytes %r reason %r" % (
            slug, res["status"], res["bytes"], res["reason"])
        ids, _labels, _verbatim = cb.token_ids_of(res["raw"])
        assert ids is not None, "P6: %s carries no two token ids" % slug
        ids_of[slug] = ids
        out("P6 document %s: status %d, %d bytes, sha256 %s, token ids %s"
            % (slug, res["status"], res["bytes"], res["sha256"], ids))
    for slug in slugs:
        res = cb.http_get(cb.CLOB_BOOK_URL.format(token_id=ids_of[slug][0]))
        assert res["status"] == 200 and res["bytes"] > 0, "P7: %s status %r reason %r" % (
            slug, res["status"], res["reason"])
        json.loads(res["raw"])
        out("P7 /book %s token %s: status %d, %d bytes, JSON"
            % (slug, ids_of[slug][0], res["status"], res["bytes"]))
    assert cb.COUNTERS["requests"] == 4, "P7: %d requests" % cb.COUNTERS["requests"]
    out("PATH-CHAINBOOK PASS: P5 to P7, 4 requests")


def mode_mark(name):
    assert name in ("start-rec", "start-cb", "kill-cb", "kill-rec"), "mark %r" % name
    os.makedirs(os.path.dirname(INSTANTS), exist_ok=True)
    marks = load_marks() if os.path.exists(INSTANTS) else {}
    assert name not in marks, "mark %r already recorded" % name
    marks[name] = {"ns": time.time_ns(), "rec_pid": main_pid(REC_UNIT),
                   "cb_pid": main_pid(CB_UNIT)}
    tmp = INSTANTS + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(marks, sort_keys=True) + "\n")
    os.replace(tmp, INSTANTS)
    out("MARK %s %s (%s)" % (name, json.dumps(marks[name], sort_keys=True),
                             utc(marks[name]["ns"] / 1e9)))


def mode_unit(restarts):
    check_both(int(restarts))


def new_recorder_records(since_ns):
    recs, torn, _n, _t = read_jsonl(REC_RUNTIME)
    starts = sorted((r for r in recs if r.get("kind") == "start"
                     and r.get("recv_ns", 0) >= since_ns), key=lambda r: r["recv_ns"])
    ups = sorted((r for r in recs if r.get("kind") == "disconnect"
                  and r.get("reason") == "startup"
                  and r.get("detected_recv_ns", 0) >= since_ns),
                 key=lambda r: r["detected_recv_ns"])
    halts = [r for r in recs if r.get("kind") == "halt" and r.get("recv_ns", 0) >= since_ns]
    return starts, ups, halts, torn


def mode_start():
    marks = load_marks()
    s_rec, s_cb = mark_ns(marks, "start-rec"), mark_ns(marks, "start-cb")
    starts, ups, halts, torn = new_recorder_records(s_rec)
    for r in starts + ups + halts:
        out("R %s" % json.dumps(r, sort_keys=True))
    assert len(starts) == 1, "G-START recorder: %d start records since the mark" % len(starts)
    st = starts[0]
    assert st.get("sha") == SHA_RECORDER, "G-START recorder: sha %r" % st.get("sha")
    assert len(ups) == 1, "G-START recorder: %d startup gaps since the mark" % len(ups)
    up = ups[0]
    assert GAP_LO_NS <= up["start_recv_ns"] < GAP_HI_NS, \
        "G-START recorder: the gap starts at %d, outside [%d, %d)" % (
            up["start_recv_ns"], GAP_LO_NS, GAP_HI_NS)
    assert st["recv_ns"] <= up["detected_recv_ns"] <= up["end_recv_ns"], \
        "G-START recorder: gap %r against start %d" % (up, st["recv_ns"])
    assert not halts, "G-START recorder: halt records %r" % halts
    out("G-START recorder: start %s sha %s, free %s, captured %s; the gap %s to %s, %.1f s"
        % (utc(st["recv_ns"] / 1e9), st["sha"], st.get("free_bytes"), st.get("captured_bytes"),
           utc(up["start_recv_ns"] / 1e9), utc(up["end_recv_ns"] / 1e9),
           (up["end_recv_ns"] - up["start_recv_ns"]) / 1e9))

    cbr, cb_torn, _n, _t = read_jsonl(CB_RUNTIME)
    new = [r for r in cbr if isinstance(r.get("wall_ns"), int) and r["wall_ns"] >= s_cb]
    for r in new:
        out("C %s" % json.dumps({k: r.get(k) for k in ("event", "pid", "wall_ns", "commit",
                                                         "file_sha256", "argv")}, sort_keys=True))
    assert cb_torn == 0, "G-START chain book: %d torn lines" % cb_torn
    assert len(new) == 1 and new[0].get("event") == "start", \
        "G-START chain book: records since the mark %r" % [r.get("event") for r in new]
    st = new[0]
    pid = main_pid(CB_UNIT)
    assert st.get("pid") == pid, "G-START chain book: start pid %r, MainPID %d" % (st.get("pid"), pid)
    assert st.get("commit") == CB_COMMIT, "G-START chain book: commit %r" % st.get("commit")
    assert st.get("file_sha256") == CB_FILE_SHA, "G-START chain book: file %r" % st.get("file_sha256")
    assert st.get("argv") == [CB_FILE, "--serve"], "G-START chain book: argv %r" % st.get("argv")
    cfg = st.get("config") or {}
    assert cfg.get("headers") == CB_HEADERS, "G-START chain book: headers %r" % cfg.get("headers")
    assert cfg.get("service_argv") == CB_ARGV, "G-START chain book: %r" % cfg.get("service_argv")
    out("G-START chain book: start %s pid %d commit %s" % (utc(st["wall_ns"] / 1e9), pid, CB_COMMIT))
    out("G-START PASS: 2 of 2")


def mode_cb():
    marks = load_marks()
    s_cb = mark_ns(marks, "start-cb")
    cbr, _torn, _n, _t = read_jsonl(CB_RUNTIME)
    starts = [r for r in cbr if r.get("event") == "start"
              and isinstance(r.get("wall_ns"), int) and r["wall_ns"] >= s_cb]
    assert starts, "G-CB: no chain book start record since the mark"
    w0 = starts[0]["wall_ns"] / 1e9
    first = math.ceil((w0 + CB_LEAD_S - 625) / 900) * 900
    windows = [first + 900 * k for k in range(CB_UNITS)]
    paths = {t: "%s/%d/window.json" % (CB_ROOT, t) for t in windows}
    missing = [t for t in windows if not os.path.exists(paths[t])]
    if missing and time.time() < max(t + CB_DEADLINE_S for t in missing):
        not_yet(time.time() + 300, "windows %s pending, the last deadline %s"
                % (missing, utc(max(t + CB_DEADLINE_S for t in missing))))
    complete = docs = clean = present = 0
    for t in windows:
        if t in missing:
            out("G-CB window %d %s: no window.json by %s" % (t, utc(t), utc(t + CB_DEADLINE_S)))
            continue
        with open(paths[t], encoding="utf-8") as fh:
            wj = json.loads(fh.read())
        assert wj.get("T") == t, "G-CB: %s carries T %r" % (paths[t], wj.get("T"))
        present += 1
        complete += int(wj.get("checkpoints_complete") or 0)
        docs += 1 if wj.get("documents_ok") is True else 0
        clean += 1 if wj.get("missed") == 0 else 0
        out("G-CB window %d %s: documents_ok %s, checkpoints_complete %s of %d, missed %s, "
            "status_counts %s" % (t, utc(t), wj.get("documents_ok"), wj.get("checkpoints_complete"),
                                  CB_CHECKPOINTS, wj.get("missed"),
                                  json.dumps(wj.get("status_counts"), sort_keys=True)))
    ok = (present == CB_UNITS and docs == CB_UNITS and clean == CB_UNITS
          and complete >= CB_COMPLETE_MIN)
    out("G-CB %s: windows %d of %d, documents_ok %d of %d, missed 0 at %d of %d, "
        "checkpoints complete %d of %d, PASS at %d or more"
        % ("PASS" if ok else "FAIL", present, CB_UNITS, docs, CB_UNITS, clean, CB_UNITS,
           complete, CB_UNITS * CB_CHECKPOINTS, CB_COMPLETE_MIN))
    assert ok, "G-CB FAIL"


def mode_rec():
    marks = load_marks()
    s_rec = mark_ns(marks, "start-rec")
    starts, _ups, _halts, _torn = new_recorder_records(s_rec)
    assert starts, "G-REC: no recorder start record since the mark"
    r0 = starts[0]["recv_ns"] / 1e9
    first = math.ceil((r0 + REC_LEAD_S + 90) / 300) * 300
    members = [first + 300 * k for k in range(REC_UNITS)]
    paths = {t: "%s/%d/manifest.json" % (REC_SERIES, t) for t in members}
    missing = [t for t in members if not os.path.exists(paths[t])]
    if missing and time.time() < max(t + REC_DEADLINE_S for t in missing):
        not_yet(time.time() + 300, "intervals %s pending, the last deadline %s"
                % (missing, utc(max(t + REC_DEADLINE_S for t in missing))))
    present = complete = quotes = shas = 0
    for t in members:
        if t in missing:
            out("G-REC interval %d %s: no manifest by %s" % (t, utc(t), utc(t + REC_DEADLINE_S)))
            continue
        with open(paths[t], encoding="utf-8") as fh:
            m = json.loads(fh.read())
        assert m.get("T0_epoch") == t, "G-REC: %s carries T0_epoch %r" % (paths[t],
                                                                         m.get("T0_epoch"))
        present += 1
        complete += 1 if m.get("complete") is True else 0
        quotes += 1 if m.get("quotes_complete") is True else 0
        shas += 1 if m.get("recorder_git_sha") == SHA_RECORDER else 0
        out("G-REC interval %d %s: complete %s, quotes_complete %s, disconnects %s, "
            "gamma_present %s, resolution_present %s, clock |offset| max %s ms, sha %s"
            % (t, utc(t), m.get("complete"), m.get("quotes_complete"), m.get("disconnect_count"),
               m.get("gamma_present"), m.get("resolution_present"),
               m.get("clock_offset_abs_max_ms"), m.get("recorder_git_sha")))
    ok = (present == REC_UNITS and quotes == REC_UNITS and shas == REC_UNITS
          and complete >= REC_COMPLETE_MIN)
    out("G-REC %s: manifests %d of %d, quotes_complete %d of %d, sha %d of %d, "
        "complete %d of %d, PASS at %d or more"
        % ("PASS" if ok else "FAIL", present, REC_UNITS, quotes, REC_UNITS, shas, REC_UNITS,
           complete, REC_UNITS, REC_COMPLETE_MIN))
    assert ok, "G-REC FAIL"


def mode_restart_cb():
    marks = load_marks()
    s_cb, k = mark_ns(marks, "start-cb"), mark_ns(marks, "kill-cb")
    old_pid = marks["kill-cb"]["cb_pid"]
    cbr, torn, _n, _t = read_jsonl(CB_RUNTIME)
    new = [r for r in cbr if isinstance(r.get("wall_ns"), int) and r["wall_ns"] >= s_cb]
    events = [(r.get("event"), r.get("pid"), r.get("wall_ns")) for r in new]
    out("G-RESTART-C records since start-cb: %s" % events)
    assert torn == 0, "G-RESTART-C: %d torn lines" % torn
    assert [e[0] for e in events] == ["start", "stop", "start"], "G-RESTART-C: %r" % events
    a, b, c = new
    assert a.get("pid") == b.get("pid") == old_pid, "G-RESTART-C: killed pid %r" % old_pid
    assert c.get("pid") != old_pid, "G-RESTART-C: the same pid restarted"
    assert b["wall_ns"] >= k, "G-RESTART-C: stop record before the mark"
    gap = c["wall_ns"] - b["wall_ns"]
    assert 0 <= gap <= RESTART_GAP_NS, "G-RESTART-C: %d ns between stop and start" % gap
    assert c.get("commit") == CB_COMMIT and c.get("file_sha256") == CB_FILE_SHA, \
        "G-RESTART-C: the restarted start record %r" % c
    pid = check_unit(CB_UNIT, CB_ARGV, None, 1, CB_MEMORY_MAX)
    assert c.get("pid") == pid, "G-RESTART-C: start pid %r, MainPID %d" % (c.get("pid"), pid)
    out("G-RESTART-C PASS: stop of %d at %s with counters %s; start of %d %.1f s later"
        % (old_pid, utc(b["wall_ns"] / 1e9), json.dumps(b.get("counters"), sort_keys=True),
           pid, gap / 1e9))


def mode_restart_rec():
    marks = load_marks()
    s_rec, k = mark_ns(marks, "start-rec"), mark_ns(marks, "kill-rec")
    old_pid = marks["kill-rec"]["rec_pid"]
    starts, ups, halts, torn = new_recorder_records(s_rec)
    for r in starts + ups:
        out("R %s" % json.dumps(r, sort_keys=True))
    assert len(starts) == 2, "G-RESTART-R: %d start records since start-rec" % len(starts)
    second = starts[1]
    assert second["recv_ns"] >= k, "G-RESTART-R: the second start precedes the mark"
    assert second.get("sha") == SHA_RECORDER, "G-RESTART-R: sha %r" % second.get("sha")
    assert len(ups) == 2, "G-RESTART-R: %d startup gaps since start-rec" % len(ups)
    up = ups[1]
    assert k - KILL_SLACK_NS <= up["start_recv_ns"] <= second["recv_ns"], \
        "G-RESTART-R: the gap starts at %d, mark %d, start %d" % (up["start_recv_ns"], k,
                                                                 second["recv_ns"])
    gap = up["end_recv_ns"] - up["start_recv_ns"]
    assert 0 <= gap <= RESTART_GAP_NS, "G-RESTART-R: the gap is %d ns" % gap
    assert not halts, "G-RESTART-R: halt records %r" % halts
    pid = check_unit(REC_UNIT, REC_ARGV, REC_CWD, 1, REC_MEMORY_MAX)
    assert pid != old_pid, "G-RESTART-R: the same pid %d" % pid
    out("G-RESTART-R PASS: pid %d replaced by %d; the gap %s to %s, %.1f s, recorded"
        % (old_pid, pid, utc(up["start_recv_ns"] / 1e9), utc(up["end_recv_ns"] / 1e9), gap / 1e9))


def mode_final():
    rec_pid, cb_pid = check_both(1)
    marks = load_marks()
    s_rec, s_cb = mark_ns(marks, "start-rec"), mark_ns(marks, "start-cb")
    recs, torn, newlines, _t = read_jsonl(REC_RUNTIME)
    kinds = {}
    for r in recs:
        if r.get("recv_ns", r.get("detected_recv_ns", 0)) >= s_rec:
            kinds[r.get("kind")] = kinds.get(r.get("kind"), 0) + 1
    starts = [r for r in recs if r.get("kind") == "start"]
    assert starts[-1].get("sha") == SHA_RECORDER, "FINAL: newest start sha %r" % starts[-1]
    cbr, cb_torn, _n2, _t2 = read_jsonl(CB_RUNTIME)
    events = [r.get("event") for r in cbr if isinstance(r.get("wall_ns"), int)
              and r["wall_ns"] >= s_cb]
    out("FINAL recorder runtime.jsonl: %d newlines, %d torn; since start-rec %s"
        % (newlines, torn, json.dumps(kinds, sort_keys=True)))
    out("FINAL chain book runtime.jsonl: %d records, %d torn; since start-cb %s"
        % (len(cbr), cb_torn, events))
    out("FINAL PASS: recorder pid %d, chain book pid %d, newest recorder start sha %s"
        % (rec_pid, cb_pid, SHA_RECORDER))


TOKEN = re.compile(r"(?<![0-9a-f])[0-9a-f]{16,64}(?![0-9a-f])")


def report_tokens():
    """Every run of 16 to 64 lowercase hex characters in a committed report."""
    tokens = set()
    for name in sorted(os.listdir(REPORTS)):
        if name.endswith(".md"):
            with open(os.path.join(REPORTS, name), encoding="utf-8") as fh:
                tokens.update(TOKEN.findall(fh.read()))
    return tokens


def by_name(tree, rel):
    """Files kept whatever the reports print: TZ-16a's label ledger, and this TZ's own record."""
    if tree == "/root/tz16a-work":
        return rel == "label-ledger.jsonl"
    if tree == "/root/tz20-work":
        return rel == "instants.json" or rel.startswith("logs/")
    return False


def mode_reclaim(trees):
    assert trees and all(t in RECLAIMABLE for t in trees), "reclaim: %r" % (trees,)
    tokens = report_tokens()
    lengths = sorted({len(t) for t in tokens})
    before = sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    out("reclaim: %d report tokens; forensic store holds %d files" % (len(tokens), before))
    considered = named = kept = copied = held = 0
    for tree in trees:
        if not os.path.isdir(tree):
            out("reclaim %s: absent" % tree)
            continue
        for dirpath, dirnames, filenames in os.walk(tree):
            dirnames.sort()
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
                with open(path, "rb") as fh:
                    data = fh.read()
                with open(dest, "xb") as fh:
                    fh.write(data)
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
        sys.exit("usage: tz20-capture-under-systemd.py MODE [ARG]")
    mode, rest = argv[0], argv[1:]
    table = {
        "state": mode_state, "path-recorder": mode_path_recorder,
        "path-chainbook": mode_path_chainbook, "start": mode_start, "cb": mode_cb,
        "rec": mode_rec, "restart-cb": mode_restart_cb, "restart-rec": mode_restart_rec,
        "final": mode_final,
    }
    if mode == "mark":
        assert len(rest) == 1, "mark NAME"
        mode_mark(rest[0])
    elif mode == "unit":
        assert len(rest) == 1, "unit N"
        mode_unit(rest[0])
    elif mode == "reclaim":
        mode_reclaim(rest)
    else:
        assert mode in table and not rest, "unknown mode %r" % (argv,)
        table[mode]()
    out("opens under the capture roots: %d" % len(OPENS))


if __name__ == "__main__":
    main(sys.argv[1:])
```
