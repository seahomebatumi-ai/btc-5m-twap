# TZ-54 — the liquidation guard: the Boss's Binance Futures positions read every five seconds by a key that can read and nothing else, Telegram and Pushover's emergency alarm as they near liquidation, a systemd unit on the capture host, its request paths, what it sees and its alarm proved by its own code before it starts

**Canonical filename:** `TZ-54-liq-guard.md`. The committed file takes this name and no other.

**Executor model: Claude Opus 5.5.** Credentials the Boss types on the host, an authenticated exchange read, an alarm on his phone, a unit that outlives the run.

**Required System Map revision:** `2026-11-21-d` — on `main` since the merge of pull request #51, `aeaca24`. **This TZ ships with no map revision:** it moves, replaces and adds no row (CANON hard rule 17); its merge adds three — `guard/liq-guard.py`, `deploy/systemd/liq-guard.service` and `research/tz54-liq-guard.py` — and the verdict's revision carries them.

**Map sections this TZ rests on**, copied from §10's C8 (map §7 item 174): §0, the fingerprint gate and its table; §1, the repository; §3, the units and the trees on the host; §6, its rows host, host identity for TZ host gates, language, git remote, egress, disk, disk floors and caps, memory, process supervision, sandbox limit — destructive actions, and harness — background output; §7 items 86, 91, 95, 115, 118, 137, 138, 144, 167, 174 and 176.

**Required anchors**, from map §0. A mismatch on any one is BLOCKED before any work:

| anchor | required |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` |
| `A4` — executor contract | `6ac6e10aeabc` |
| `A5` — recorder | `0f6c90451cbd` |
| `A6` — pricer | `729f0bcdbee3` |

**Written authorization (contract §10).** From the capture host, every connection IPv4 (`V4HTTPS.connect`, Appendix A lines 217 to 221), by `guard/liq-guard.py`'s modes and nothing else: **Binance, with the Boss's key, GET reads alone** — `fapi.binance.com`'s `/fapi/v1/time`, unsigned; its `/fapi/v3/positionRisk` — `/fapi/v2/positionRisk` where v3 answers `404` — and `/fapi/v1/leverageBracket`, signed; and `api.binance.com`'s `/sapi/v1/account/apiRestrictions`, signed. **No order, no transfer, no change of margin, leverage or any setting — no request to Binance but these four GETs** — and **with a key that can read and nothing else**, its permissions read by the guard itself and every other key refused (§1.2). **Pushover**, `api.pushover.net`: `/1/users/validate.json`, `/1/messages.json`, `/1/receipts/<receipt>.json` and its `cancel.json`. **Telegram**, `api.telegram.org`, the guard's own bot: `getMe`, `getUpdates`, `sendMessage`. **`hc-ping.com`**, the dead-man's ping, where the Boss sets one. Headers: `User-Agent: btc-5m-twap-liq-guard` on every request (`Net._call`, line 243); `Accept: application/json` and, signed, `X-MBX-APIKEY` at Binance (`Binance._get`, lines 289 to 296); `Content-Type: application/x-www-form-urlencoded` on Pushover's POSTs and `application/json` on Telegram's. **No other venue, exchange or key is called by this TZ, and the live host is not reached.**

**CANON `2026-11-21-b` ships with this TZ** — the Boss's instruction of 2026-11-21 and the guard's decision (CANON PART VII); it is the Architect's project instructions and no file of this repository.

**Before EXECUTE.** The Boss has Pushover on his iPhone, signed in, its **Critical Alerts on for high and emergency priority** and their volume set — the evening's quick setup did it, and §3 step 9's block repeats it. **He is at his phone for the run's middle hour:** he makes a Binance key that can read alone, bound to the Warsaw server's IPv4 address, a Pushover application token and a Telegram bot, and types them on the host (§3 step 9); he answers «да» or «нет» to the list the guard shows him, and acknowledges its test alarm (§3 step 11).

**When: begun at any hour.** The unit runs from then on.

---

## 0. The readiness, the files and the host

### 0.0 The readiness, then the work tree

After contract §1 steps 1 and 2, and before anything else, in the session — verbatim, read-only:

```
/root/tz04a-env/venv/bin/python -B - <<'EOF2'
import os, time
now = int(time.time())
v = os.statvfs("/var/lib"); free = v.f_bavail * v.f_frsize
with open("/proc/meminfo", encoding="utf-8") as fh:
    mem = [int(ln.split()[1]) * 1024 for ln in fh if ln.startswith("MemAvailable:")][0]
ready = free >= 7450000000 and mem >= 100663296
print("ready=%d: %d bytes free on /var/lib, 7450000000 needed; MemAvailable %d, 100663296 needed; at %d %s" % (ready, free, mem, now, time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now))))
EOF2
```

**The two floors, each derived from map §6:** `7,450,000,000` free bytes — the reclaim's floor at §9, `7,400,000,000`, the reward book's `STREAM_FLOOR` `7,300,000,000` and `100,000,000` (map §6, disk floors and caps; the checker's `RECLAIM_FLOOR`, its line 295), and this session's writes, at most `50,000,000`; `100,663,296` bytes of `MemAvailable` — the unit's `MemoryMax`, `96` MiB, the most it may hold, against the host's `MemAvailable` of `136,404,992` to `562,360,320` across the TZs' reads (map §6, memory).

**`ready=1` begins the run. `ready=0`, or a read without its `ready=` line, begins nothing:** no directory is made and no report is written — this TZ has not executed (CANON hard rule 5) — and the Executor gives the Boss the line as printed and, in one line in Russian, that `EXECUTE TZ-54` is sent again an hour later. This is not BLOCKED and owes no report (contract §5). Then `mkdir /root/tz54-work /root/tz54-work/logs; echo "exit=$?"` — `exit=0` proves neither existed; anything else is BLOCKED — and the readiness read again into `logs/00-ready.log`. **From here every command's output goes to a log under `/root/tz54-work/logs/`, one file per step, under the names §3 fixes; nothing to the session's scratchpad** but §9's last block (map §7 item 118).

Four abbreviations, written out in full in every block handed to the Boss:

- **`P`** — `nice -n 19 /root/tz04a-env/venv/bin/python -B`.
- **`C M NN`** — the checker's mode `M`: `cd /root/tz54-work && { date -u +%FT%T.%NZ; P /root/tz54-work/stage/research/tz54-liq-guard.py M; echo "exit=$?"; } >> /root/tz54-work/logs/NN.log 2>&1; tail -n 60 /root/tz54-work/logs/NN.log`. The checker asserts it runs from `/root/tz54-work`.
- **`G M NN`** — the guard's mode `M` from the stage: the same with `/root/tz04a-env/venv/bin/python -B /root/tz54-work/stage/guard/liq-guard.py M`, without `nice`.
- **`S`** — the scratchpad directory the session's system prompt names.

### 0.1 The files, staged

**The checker is TZ-53's, renamed:** `research/tz53-l1-account.py` read from `main`, at its map §0 hash, changed by the edits below, each asserted to occur the number of times it names — so that its capture-host modes, `fingerprint`, `number`, `refs`, `scratch` and `reclaim`, run under this TZ's number, paths and map revision; it reaches no host but GitHub's through `git`. **The guard, its unit file and B-DEPLOY are this file's Appendices A, B and C**, each extracted by its fence and the next line that is a fence alone. **This script, verbatim**, its first argument the destination and its second `stage` — four files — or `branch` — the branch's three — its output into `logs/01-stage.log`:

```
/root/tz04a-env/venv/bin/python -B - /root/tz54-work/stage stage <<'EOF3'
import hashlib, os, subprocess, sys
REPO = "/root/btc-5m-twap"
TZ = REPO + "/CryptoTZ/TZ-54-liq-guard.md"
DEST, WHAT = sys.argv[1], sys.argv[2]
assert WHAT in ("stage", "branch"), WHAT
WANT = {
    "research/tz54-liq-guard.py": "fd8f8c21d3dc5c36655a6948ce593a03d06ca8f783955ea7d18df5a57ea0e4bf",
    "guard/liq-guard.py": "782efaa88e268bd6ace42e23dc192e279ae130bb7bdc23d2f4de4d628c4da66f",
    "deploy/systemd/liq-guard.service": "26f609134730e4b9080bcdddbf2365ba35b1f69ddc1633d538a250bd46bce920",
    "b-deploy.sh": "8f59acce92292bf2afda632636e8cd80ca154dfc3d9a48315acb0de19dfba4ad"}
FILES = {"branch": ("research/tz54-liq-guard.py", "guard/liq-guard.py", "deploy/systemd/liq-guard.service"),
         "stage": ("research/tz54-liq-guard.py", "guard/liq-guard.py", "deploy/systemd/liq-guard.service", "b-deploy.sh")}


def fenced(fence):
    lines = open(TZ, encoding="utf-8").read().split("\n")
    i = lines.index(fence)
    j = lines.index("```", i + 1)
    return ("\n".join(lines[i + 1:j]) + "\n").encode("utf-8")


def checker():
    b = subprocess.run(["git", "-C", REPO, "show", "origin/main:research/tz53-l1-account.py"], capture_output=True,
                       check=True).stdout
    assert hashlib.sha256(b).hexdigest() == "e4b72d0e285f1d8736a056012d3c9056f7f103e8e899742e10e488932c910c94", "base"
    t = b.decode("utf-8")
    EDITS = [
        ('"""TZ-53 - L1\'s unit deployed: this file is TZ-52\'s instrument renamed, its deployment checks on both hosts -\n'
         "the fingerprint, the number, the refs, the capture's room, the scratch, the reclaim, the live host's gate and its\n"
         "facts, the geoblock, sshd and the client's environment. The unit itself and every check of its own - its account,\n"
         "its order path, its stop, its state under systemd - are engine/l1-bot.py's modes (TZ-53 section 5). Its modes\n"
         "that ask the Boss anything, its approvals and its round trip are TZ-51's and TZ-52's, kept and tested; TZ-53 runs\n"
         "none of them.\n",
         '"""TZ-54 - the liquidation guard deployed on the capture host: this file is TZ-53\'s checker renamed, of which\n'
         "TZ-54 runs the capture host's modes alone - the fingerprint, the number, the refs, the scratch and the reclaim -\n"
         "and the self-test. The guard itself and every check of its own - its credentials, its request paths, its key's\n"
         "permissions, its alarm, its state under systemd - are guard/liq-guard.py's modes (TZ-54 section 5). Every other\n"
         "mode of this file is TZ-51's, TZ-52's and TZ-53's, kept and tested; TZ-54 runs none of them.\n", 1),
        ("TZ-53-l1-unit", "TZ-54-liq-guard", 3),
        ("tz-53-l1-unit", "tz-54-liq-guard", 1),
        ("tz53", "tz54", 21),
        ("TZ-53", "TZ-54", 9),
        ("ТЗ-53", "ТЗ-54", 3),
        ('MAP_REVISION = "2026-11-21-c"', 'MAP_REVISION = "2026-11-21-d"', 1),
        ('MAP_ROWS = {"frozen": 64, "tracked": 2, "reported": 1}', 'MAP_ROWS = {"frozen": 67, "tracked": 2, "reported": 1}', 1),
    ]
    for old, new, n in EDITS:
        assert t.count(old) == n, (old[:60], t.count(old), n)
        t = t.replace(old, new)
    return t.encode("utf-8")


data = {"research/tz54-liq-guard.py": checker(),
        "guard/liq-guard.py": fenced("```python file=guard/liq-guard.py"),
        "deploy/systemd/liq-guard.service": fenced("```ini file=deploy/systemd/liq-guard.service"),
        "b-deploy.sh": fenced("```bash file=b-deploy.sh")}
for rel in FILES[WHAT]:
    b = data[rel]
    assert hashlib.sha256(b).hexdigest() == WANT[rel], rel
    path = os.path.join(DEST, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path):
        with open(path, "rb") as fh:
            assert fh.read() == b, path + " exists with other bytes"
        state = "equal, kept"
    else:
        with open(path, "xb") as fh:
            fh.write(b)
        state = "created"
    print(path, b.count(b"\n"), len(b), WANT[rel], state)
EOF3
```

| file | lines | bytes | SHA-256 |
|---|---|---|---|
| base: `research/tz53-l1-account.py` on `main`, map §0 | 3,324 | 188,378 | `e4b72d0e285f1d8736a056012d3c9056f7f103e8e899742e10e488932c910c94` |
| `research/tz54-liq-guard.py` — the checker | 3,323 | 188,349 | `fd8f8c21d3dc5c36655a6948ce593a03d06ca8f783955ea7d18df5a57ea0e4bf` |
| `guard/liq-guard.py` — Appendix A, the guard | 1,850 | 93,840 | `782efaa88e268bd6ace42e23dc192e279ae130bb7bdc23d2f4de4d628c4da66f` |
| `deploy/systemd/liq-guard.service` — Appendix B | 29 | 1,055 | `26f609134730e4b9080bcdddbf2365ba35b1f69ddc1633d538a250bd46bce920` |
| `b-deploy.sh` — Appendix C | 117 | 6,554 | `8f59acce92292bf2afda632636e8cd80ca154dfc3d9a48315acb0de19dfba4ad` |

A failed assert or another hash is BLOCKED; here every line reads `created`. **`b-deploy.sh` is staged and never committed:** the report quotes it by this hash, and §9 keeps it in the forensic store.

### 0.2 Fingerprint

`C fingerprint 02-fingerprint` performs contract §1 steps 3 and 4 inside the checker against `SYSTEM-MAP.md` and the files of its §0 table in the primary checkout, and must print `FINGERPRINT PASS: revision 2026-11-21-d; anchors 6 of 6, 4 re-derived; rows 70: frozen 67 of 67 equal, tracked 2, reported 1; the signing page on main equal to TZ-50's Appendix B` (`mode_fingerprint`, the checker's lines 1087 to 1122). Anything else is BLOCKED.

### 0.3 Host gate

On the capture host, where the Executor runs (map §6, host), from `/root/btc-5m-twap`, output verbatim into `logs/03-host-gate.log`:

```
date -u; uptime -s
nproc; grep -E '^(MemTotal|MemAvailable|SwapTotal|SwapFree):' /proc/meminfo
df -B1 --output=source,size,avail /var/lib/btc-recorder
find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
grep -c e3975b5da44c5328adf3bf3914634cd878842c73 /var/lib/btc-recorder/runtime.jsonl
/root/tz04a-env/venv/bin/python -c 'import sys; print(sys.version.split()[0])'
TZ=UTC systemctl show btc-recorder.service btc-rewardbook.service btc-rewardbook-archive.timer adv3-bot.service liq-guard.service -p Id -p LoadState -p ActiveState -p SubState -p UnitFileState -p NRestarts -p MainPID
for p in /root/liq-guard-svc /var/lib/liq-guard /etc/liq-guard /etc/systemd/system/liq-guard.service; do test -e $p; echo "$p exit=$?"; done
echo "global IPv4 addresses: $(ip -4 -o addr show scope global | wc -l)"; command -v ip df systemd-run install cmp sha256sum
```

- **H1** — `find` prints exactly one path. **H2** — `df` names source `/dev/vda2` and size `31612203008`, and `grep -c` prints at least `1`: with H1, map §6's host identity, in the form TZ-46's host gate read it.
- **H3** — the interpreter prints `3.12.` (map §6, language).
- **H4** — `liq-guard.service` reads `LoadState=not-found`, and the four paths each `exit=1`: the guard is new here. The other units' lines are recorded, not judged (map §7 item 86).
- **H5** — at least one global IPv4 address, **counted and never printed**, and the six commands found.

Any of H1 to H5 failing is BLOCKED.

### 0.4 The number and the refs

Into `04-number.log`: `git -C /root/btc-5m-twap fetch origin`, then `C number 04-number`, which must print `NUMBER PASS - 2 of 2` — of the number `TZ-54`, this file alone under `CryptoTZ/` and no report (CANON hard rule 2) — and `C refs 04-number`, which must find no `refs/heads/tz-54-liq-guard` on `origin`. Either failing is BLOCKED.

---

## 1. What this TZ decides

### 1.1 The guard — the Boss's request of 2026-11-21, decided in CANON `2026-11-21-b`, PART VII

Binance's own alerts no longer ring him at night, and Binance does not guarantee their delivery. **One unit, `liq-guard.service`, on the capture host,** runs `guard/liq-guard.py serve` (Appendix A, standard library alone, Python 3.12): every `5` s (`POLL_S`, line 49) it reads his USDⓈ-M positions through `/fapi/v3/positionRisk` (`Binance.positions`, lines 312 to 323) and, for each, the distance from its mark price to its liquidation price as a percent of the mark, on the side that loses (`distance_pct`, lines 439 to 445). **Three thresholds, his, `5`, `3` and `1.5` by default** (`DEFAULT_THRESHOLDS`, line 59): under the first, a message in his Telegram; under the second, **Pushover's emergency priority — repeated every `30` s until he acknowledges, at most `50` times, about `25` minutes, as Pushover caps it, and, with iOS's Critical Alerts on, sounding through silent mode and Focus** (`ALARM_RETRY_S`, `ALARM_EXPIRE_S`, line 62; `Guard.announce`, lines 784 to 789); under the third, a second emergency alarm. **Each level rings once a descent** and re-arms once the distance is a point above its threshold; a read that crosses several at once rings the highest (`step`, lines 456 to 465). **Every alarm says how much margin moves the liquidation price back to `8`% from the mark** (`margin_hint`, lines 480 to 489): for an isolated position the liquidation price is linear in its margin, `dLP/dM = 1/(Q(1+mmr))` short and `−1/(Q(1−mmr))` long, `mmr` the maintenance rate of the position's leverage bracket (`bracket_for`, lines 468 to 477) — exact; for a cross position, an estimate, said so in the message. **After he adds margin the guard reads the new liquidation price itself**; nothing is set again by hand.

### 1.2 The key — it can read and nothing else, proved by the guard at every start

The key is a Binance key the Boss makes with **«Enable Reading» alone, bound to the capture host's IPv4 address**, typed by him on the host. **The guard reads its permissions from Binance** (`/sapi/v1/account/apiRestrictions`) at every start and every `6` h, and refuses — exit `2`, which its unit does not restart, after a Pushover alarm at high priority and a Telegram message — any key whose `ipRestrict` is not `true`, whose `enableReading` is not `true`, or for which any other field named `enable…` or `permits…` reads `true` but `enableFixReadOnly`; a key missing one of the five core fields is refused too (`key_reading`, lines 492 to 503; `Guard.check_key`, lines 732 to 744; `refuse`, lines 1311 to 1322). **Every connection is IPv4** (`V4HTTPS.connect`), because the key is bound to the host's IPv4 address and an IPv6 connection would be refused. **Read-only is a design choice, not a measurement:** Binance's documentation and its developers' forum disagree on whether every futures read is served to a reading-only key; §1.5's G-SEE settles it for this account before the unit starts.

### 1.3 Blindness, the dead-man and the watchdog

**No successful read for `120` s** (`BLIND_S`, line 52) **is an alarm of its own**: Pushover at high priority — with Critical Alerts on, one loud alert — and Telegram, naming Binance's own error, repeated every `30` minutes while it lasts (`Guard.check_blind`, lines 791 to 801). A `429` or `418` from Binance holds the guard's reads back `60` or `300` s (`BACKOFF_S`, line 58). **A host that fails at the network is not tried again for `15` s** (`Net.call`, lines 232 to 239), so one pass waits at most one timeout a host. **Every step of a pass runs on its own:** a fault in one is journaled and stops no other — the blind check among them (`Guard.cycle`, lines 956 to 972); **the alarm is queued before the levels are committed and before anything is written**, so a fault or a full disk after it rings it again or not at all, never loses it (`Guard.poll`, lines 746 to 782; `Guard.journal`, lines 657 to 671). **systemd's watchdog** restarts a pass that hangs for `300` s (`WatchdogSec`, Appendix B; `sd_notify`, lines 395 to 405). **The dead-man**, where the Boss sets one: a ping to `hc-ping.com` every `60` s while the guard sees Binance, so that healthchecks.io's own Pushover alarm wakes him if the host, its network or the guard dies (`Guard.ping`, lines 935 to 939).

### 1.4 Telegram — a bot of its own, his pinned chat alone

Its own bot, because one token serves one poller (CANON PART IV). `find-chat` pins the one private chat that sent `/start` (`mode_find_chat`, lines 1039 to 1078). **Commands from that chat alone** — every other chat is journaled and never answered: «Статус» — every position's distance, prices and margin hint; «Тест» — a test alarm, and «Тест пройден» once he acknowledges it in Pushover; «Пороги» and «Пороги 5 3 1,5» — his thresholds, each a number, decreasing, at most `30`, kept across restarts; a change rings nothing at once (`Guard.command`, lines 840 to 868). A quiet heartbeat at `19:00` UTC, `23:00` in Batumi: positions counted, the nearest to liquidation named (`Guard.heartbeat`, lines 909 to 923). **Telegram never trades, and neither does anything else of the guard.**

### 1.5 The prove — CANON hard rule 14, and what the guard sees confirmed by the Boss

`prove` runs, through the guard's own functions and before the unit starts, every request path the unit uses, asserted served and parsed (`mode_prove`, lines 1105 to 1207), each a gate of its record `prove.json`, which carries the code's SHA-256: **G-CRED** — the credentials, each of its form, `0600`, root's; **G-TIME** — Binance's clock less the host's under `2,000` ms; **G-KEY** — §1.2's permissions, every boolean printed; **G-POS** — the positions served and parsed, counted; **G-BRACKET** — one held symbol's leverage brackets, or `BTCUSDT`'s where none is held; **G-PUSH** — the user key and token validated; **G-TG** — `getMe` and one message to the pinned chat; **G-SEE — the guard sends the Boss, in his chat, every position it sees, with its distance and prices, or that it sees none, and asks «Совпадает с твоими позициями в Binance? Ответь «да» или «нет»»; it passes on «да» within `900` s** (`see_text`, lines 1081 to 1088; `answer_of`, lines 1091 to 1102) — **a reading-only key that Binance serves an empty list would otherwise guard nothing in silence;** **G-ALARM** — a test alarm at emergency priority, acknowledged on his phone within `900` s; and **G-HC** — the dead-man's ping answered `OK`, or not set — **last, after the Boss's two answers, so that no wait of the prove reads as the host's death at healthchecks.io: the unit's own pings follow within a minute.** **PASS is the ten gates in this order, each PASS** (`PROVE_GATES`, line 71).

### 1.6 The record, and what is never printed

`/var/lib/liq-guard/`, `0700`, root's: `state.json` every `30` s — counts, states and instants, no position; `journal/<day>.jsonl`, `0600` — each event: a level reached with its distance and prices, an alarm sent, an error once a minute at most, a command's name, a tick every `10` minutes; files older than `90` days removed at the tick (`Guard.tick`, lines 941 to 954); `prove.json`; and systemd's `service.log`. **A credential, the chat id and this host's address are never written:** every text the guard journals, and every error text it prints or sends, is scrubbed of each credential and of every IPv4 address first (`Scrub`, lines 199 to 209; `Guard.journal` and `Guard.err`, lines 657 to 678; `mode_prove`'s `tried`), and the guard's own texts carry none. **No mode the Executor runs prints a symbol, price, size or margin of the Boss's positions:** `prove` and `status` print counts (`mode_status`, lines 1210 to 1230). **G-PRINT** (§4): the guard's `scan` reads every log and the report for every credential, the chat id and the host's own IPv4 addresses, and prints counts alone (`mode_scan`, lines 1253 to 1271).

### 1.7 The unit

`deploy/systemd/liq-guard.service`, Appendix B: `Type=notify`, `NotifyAccess=main`, `WatchdogSec=300`, `TimeoutStartSec=120`; `Restart=always`, `RestartSec=15`, **`RestartPreventExitStatus=2`** — a refused key or credential stays down — and **`StartLimitIntervalSec=0`**, so that no burst of restarts leaves the guard down; `MemoryMax=96M`; `NoNewPrivileges`, `PrivateTmp`, `ProtectSystem=strict` with `ReadWritePaths=/var/lib/liq-guard`; under `/root/tz04a-env/venv/bin/python` — a system unit, enabled for boot, as every long-lived process of this project (map §6, process supervision; CANON hard rule 14). **Its stop is `systemctl disable --now liq-guard.service`.** A `daemon-reload` re-arms only a timer's `OnActiveSec` (map §7 item 115): the reward book's archive's timer has none since TZ-46, and the pair book's is disabled. A restart by needrestart (map §7 item 176) costs the guard about `15` s and no alarm.

### 1.8 What a PASS establishes, and what it does not

A PASS establishes that the unit runs, reads the Boss's positions as he confirmed them, and that its alarm reached his phone and was acknowledged. **It does not establish that every later alarm will wake him:** that rests on his phone's settings — Critical Alerts on, volume, Pushover not removed — which «Тест» checks at any hour; and on the host, which the dead-man watches where he sets it. **It measures no edge and moves no rung of PART VII's ladder:** the guard is a tool for his own trading, judged against his trading without it (CANON PART V).

---

## 2. Scope

1. **Repository, written:** `guard/liq-guard.py`, `deploy/systemd/liq-guard.service` and `research/tz54-liq-guard.py` on the branch `tz-54-liq-guard`, and its pull request; `CryptoReports/TZ-54-liq-guard-report.md` on `main`. **Read:** this file by §0.1's script; `research/tz53-l1-account.py` by `git show`; `SYSTEM-MAP.md` and the files of its §0 table by `fingerprint`; `CryptoTZ/` and `CryptoReports/` by `number`; `origin`'s refs by `refs`.
2. **Capture host, written:** `/root/tz54-work/**` — the logs, the stage, the worktree `wt`, B-DEPLOY's `inst`, the checker's `selftest-tmp` — and the primary checkout's record of the worktree, removed by §9; the guard's self-test's temporary tree under `/tmp`, removed by the self-test; **kept, the guard's:** `/root/liq-guard-svc/` with `liq-guard.py` and `liq-guard.service`, `0700`; `/var/lib/liq-guard/`, `0700`, as §1.6; `/etc/liq-guard/`, `0700`, its files `0600` and root's — `binance-key`, `binance-secret`, `pushover-user`, `pushover-token`, `tg-token` and, where given, `hc-url` by the Boss's `secrets`, and `tg-chat` by `find-chat`, each by exclusive create — **but by B-RESET** (§3 step 11), which removes the credential files of a gate that refused them, before anything has used them, so that the Boss types them again; and `/etc/systemd/system/liq-guard.service`, enabled. The transient unit `tz54-deploy`, collected when it ends. `/root/btc-forensics/tz54-work--*` by `reclaim`; earlier session directories by B-RECLAIM-SCRATCH (§3 step 8).
3. **Capture host, read:** `/proc`; `df`; the recorder's store by `find` and `grep -c` alone; `systemctl show` of the units §0.3 names; `ip -4`, counted, and by `scan` in memory; the primary checkout; `/root/liq-guard-svc/` and the unit file by `sha256sum`, `cmp` and `ls`. **A file under `/etc/liq-guard/` is read by the guard's modes alone; `/var/lib/liq-guard/` by the guard's modes, B-DEPLOY's `state` reads of four fields — `key_ok`, `blind`, `polls_ok`, `disk_faults` — and §3 step 12's reads, which print `prove.json` whole, the last lines of `service.log` and the files' names and modes; never the journal.**
4. **Network:** the written authorization's, from the capture host; GitHub by `git` and `gh`. **`api.binance.com`, `api.pushover.net` and `hc-ping.com` are in no row of map §6's egress:** G-KEY, G-PUSH and G-HC are this host's first reads of them, and a refusal of any is a FAIL of its gate.
5. **Not changed, and read by nothing but §0.3's `systemctl show`, `find` and `grep -c` — a named exemption, the host gate's identity and state:** every other unit and store of this project or another. **Not touched:** the advisor's credentials and record; the live host — no `ssh` in this TZ.
6. **Never printed — in a log, the report, a pull request or the chat:** a credential, the chat id, an address of this host, or a symbol, price, size or margin of the Boss's positions. The guard's messages to his own chat carry his positions: they are the product, and no log holds them.

---

## 3. The work, in this order

| step | logs |
|---|---|
| 1 to 5 | `00-ready.log`, `01-stage.log`, `02-fingerprint.log`, `03-host-gate.log`, `04-number.log` |
| 6 | `10-worktree.log`, `11-push.log`, `12-pr.log` |
| 7 | `20-checker-selftest.log`, `21-guard-selftest.log` |
| 8 | `22-scratch.log`, `23-reclaim-scratch.log` |
| 9 | `30-secrets.log` |
| 10 | `31-find-chat.log` |
| 11 | `59-deploy-start.log`, `60-deploy.log`, `58-reset.log` where B-RESET runs |
| 12 | `61-unit-after.log` |
| 13 | `62-print.log` |
| 14 | none: the session, §9 |

1. **§0.0**, the readiness and the work tree.
2. **§0.1**, `stage`, into `01-stage.log`: four lines `created`.
3. **§0.2**, `fingerprint`.
4. **§0.3**, the host gate.
5. **§0.4**, the number and the refs.
6. **The branch.** Into `10-worktree.log`: `git -C /root/btc-5m-twap worktree add -b tz-54-liq-guard /root/tz54-work/wt origin/main`, then §0.1's script verbatim but for its arguments, `/root/tz54-work/wt branch` — three lines `created`. Into `11-push.log`: commit the three files on the branch; push with `git -C /root/tz54-work/wt push -u origin tz-54-liq-guard` — through `credential.helper=!gh auth git-credential` where the URL's credential is refused (map §6, git remote) — then `git -C /root/tz54-work/wt ls-remote origin refs/heads/tz-54-liq-guard`, `git -C /root/tz54-work/wt rev-parse HEAD` and `git -C /root/tz54-work/wt diff --numstat origin/main HEAD`: the hash on `origin` the worktree's `HEAD`, and exactly `29 0 deploy/systemd/liq-guard.service`, `1850 0 guard/liq-guard.py` and `3323 0 research/tz54-liq-guard.py`. Into `12-pr.log`: the pull request against `main`, opened with `gh pr create`. A failed assert or a non-zero exit is BLOCKED.
7. **The self-tests.** `C selftest 20-checker-selftest` must print `SELFTEST PASS: 141 checks, 141 passed; refused by the hook: 5, each a check's own` — TZ-53's checker, every one of its checks, under this TZ's names. `G selftest 21-guard-selftest` must print `SELFTEST PASS: 83 checks` (§7): it reaches no network — Binance, Pushover, Telegram and healthchecks.io are stand-ins in the process (`FakeNet`, lines 1327 to 1410) — and runs `secrets` at a real pseudo-terminal of its own (`on_terminal`, lines 1419 to 1485), on a temporary tree under `/tmp` that it removes. Anything else is BLOCKED.
8. **The directories beside this session, and B-RECLAIM-SCRATCH.** `cd /root/tz54-work && P /root/tz54-work/stage/research/tz54-liq-guard.py scratch "$(dirname "$S")"`, into `22-scratch.log`, names every UUID directory beside this session's own **live** — born from 1 s before to 60 s after the start of a running `claude` process — or **earlier** (map §7 items 91 and 95); with a directory goes the harness's copy of its background output (map §6, harness — background output). For each named earlier, into `23-reclaim-scratch.log`: `cd /root/tz54-work && P /root/tz54-work/stage/research/tz54-liq-guard.py reclaim <its full path>`, `rm -rf <it>; echo "exit=$?"`, `test -e <it>; echo "exit=$?"` — `RECLAIM PASS`, `exit=0`, `exit=1`. **Its paste**, where the classifier refuses it, the same three lines for each, chained with `&&` up to the `test`.
9. **The Boss's credentials.** The Executor hands the Boss, **verbatim, in one message**, the block below, and waits for his «готово». Then it reads `30-secrets.log`: `SECRETS binance-key`, `binance-secret`, `pushover-user`, `pushover-token` and `tg-token` each `written, N bytes` — or `kept`, for any a dropped connection had already written — `hc-url` written, kept or `skipped`, and `exit=0`; and, into the same log, `ls -la /etc/liq-guard`: the directory `0700`, every file `0600`, root's. Where a line reads `not given in 3 tries` or the exit is not `0`, the Executor tells the Boss once, in one line, to paste the same line again; a second failure is BLOCKED.

> **Сторож · ТЗ-54 — ключи. Сначала соберите всё (шаги 1–4), потом вставляйте (шаг 5).**
>
> **1. Binance.** Профиль → **Управление API** (API Management) → **Создать API** → **Сгенерированный системой** (System generated). Название — `guard`. Разрешения: **только «Включить чтение» (Enable Reading)** — больше ничего не отмечать. **«Ограничить доступ только доверенными IP»** — IP сервера в Варшаве, тот же адрес, по которому к нему подключается Termius. Сохранить; подтверждение кодом или письмом — как обычно. Скопировать **API Key** и **Secret Key** (Secret показывается один раз).
>
> **2. Pushover.** На **pushover.net**: **Create an Application/API Token**, имя «Сторож» → скопировать его **API Token**. Ваш **User Key** — вверху главной страницы pushover.net. В приложении Pushover на iPhone: Настройки → **Critical Alerts** включены для High и Emergency, громкость высокая.
>
> **3. Telegram.** В **@BotFather**: `/newbot`, имя «Сторож», любое свободное имя пользователя на `bot` → скопировать **токен**.
>
> **4. По желанию — страховка от падения сервера.** На **healthchecks.io**: новая проверка, **Period 1 minute, Grace 5 minutes**; Integrations → **Pushover**, приоритет **Emergency** для «down»; скопировать адрес пинга `https://hc-ping.com/…`.
>
> **5. В терминале сервера в Варшаве, под root,** вставьте строку:
> `cd /root/tz54-work && { /root/tz04a-env/venv/bin/python -B /root/tz54-work/stage/guard/liq-guard.py secrets; echo "exit=$?"; } | tee -a /root/tz54-work/logs/30-secrets.log`
> Она спросит по очереди: API Key и Secret Key Binance, User Key и API Token Pushover, токен бота, адрес пинга (или просто Enter — без него). Ввод скрыт. Если связь прервётся — подключитесь снова и вставьте ту же строку: введённое раньше сохранится.
>
> **6.** Откройте нового бота «Сторож» в Telegram и нажмите **Start**. Напишите мне «готово».

10. **The chat.** `G find-chat 31-find-chat`, in the background — it waits up to `1,800` s for the `/start` — its log read every `570` s at most until its `exit=` line: `FIND-CHAT updates N, private chats that sent /start: 1, pinned`, `exit=0`; the bot writes in his chat «Сторож на связи…». Where it ends without one, the Executor tells the Boss once, in one line, to press Start in his bot, and runs it once more; a second failure is BLOCKED.
11. **B-DEPLOY — Appendix C, the Executor's first.** The Executor tells the Boss once, in Russian: «Запускаю сторожа. В Telegram придёт список позиций, которые он видит, — ответьте «да», если он совпадает с Binance, иначе «нет». Потом зазвонит Pushover — нажмите «Подтвердить». На каждое — 15 минут.» Then, into `59-deploy-start.log`:

```
systemd-run --unit=tz54-deploy --collect -p RuntimeMaxSec=7200 /bin/bash /root/tz54-work/stage/b-deploy.sh; echo "exit=$?"
```

`exit=0`, the transient unit started. **Its paste**, where the classifier refuses it (map §6, sandbox limit — destructive actions): the same line, by the Boss, as root, in a terminal on the capture host — **one paste for the whole sequence**, its copy, its start and its timed reads in order, each gated on the one before it (map §7 item 138), **and its reads are the gate's reads**: the Executor reads the log and runs none of it again (map §7 item 144). Either way the Executor reads `tail -n 60 /root/tz54-work/logs/60-deploy.log` at most every `570` s until its `B-DEPLOY END` line. **B-DEPLOY's steps, each gated on the one before it** (§4): the host; `MemAvailable` at or above `100,663,296` at one of five reads a minute apart (map §7 item 137); the guard and its unit file installed and read at §0.1's SHA-256, the unit file equal to the code's copy by `cmp`, `daemon-reload`, `LoadState` `loaded` and `UnitFileState` `disabled`; **G-PROVE**, once for this code; `systemctl enable --now`, **G-UNIT** at `60` s; **G-LIVE** `900` s after the start. **`B-DEPLOY END exit=0` is G-DEPLOY PASS.** `END exit=1` is a FAIL at the step its `FAIL at` line names — after G-UNIT's start, B-DEPLOY itself stopped the unit, `systemctl disable --now`, and printed its state. Then `systemctl is-active tz54-deploy.service; echo "exit=$?"` must not read `active`. A log that stops without its `END` line for `2,400` s — G-PROVE's two waits of `900` s and a read's `570` beside them — is read again once, then BLOCKED, and the Executor runs `systemctl stop tz54-deploy.service; systemctl disable --now liq-guard.service; echo "exit=$?"` — its paste the same line.

**One more B-DEPLOY, at most, and only for these.** Where G-PROVE's FAIL is **G-KEY, G-POS or G-BRACKET** with Binance's refusal, **G-PUSH**, **G-TG** or **G-HC** — the credentials, not the design — the Executor tells the Boss once, in one line in Russian, the gate and its printed cause, and runs **B-RESET** into `58-reset.log`: `rm` of the files of that gate — `binance-key` and `binance-secret`; `pushover-user` and `pushover-token`; `tg-token` and `tg-chat`; `hc-url` — then `test -e` of each, `exit=1`; its paste the same lines. The Boss deletes a refused Binance key in Binance's API Management, makes the credential again and pastes step 9's line; G-TG's reset runs step 10 again; then B-DEPLOY once more. **Where G-ALARM's FAIL is no acknowledgement in `900` s,** the Executor tells the Boss once to check Pushover's Critical Alerts and its volume, and runs B-DEPLOY once more, nothing reset. **G-SEE answered «нет», G-CRED, G-TIME, the memory, the install, G-UNIT or G-LIVE is BLOCKED** at its first FAIL: a view of his positions the Boss does not recognise is a design question — a reading-only key Binance serves no futures data, or another account — for the next TZ, not a retry. A second B-DEPLOY that fails is BLOCKED.
12. **The unit after**, into `61-unit-after.log`, from `/root/tz54-work`: `systemctl show liq-guard.service -p ActiveState -p SubState -p NRestarts -p MainPID -p UnitFileState -p ActiveEnterTimestamp -p WatchdogUSec -p MemoryCurrent -p MemoryPeak`; `sha256sum /root/liq-guard-svc/* /etc/systemd/system/liq-guard.service`; `ls -la /root/liq-guard-svc /var/lib/liq-guard /etc/liq-guard`; `tail -n 20 /var/lib/liq-guard/service.log`; `/root/tz04a-env/venv/bin/python -B /root/liq-guard-svc/liq-guard.py status`; `cat /var/lib/liq-guard/prove.json`. The unit `active`, `NRestarts` `0`, its files at §0.1's SHA-256, the prove's record `"pass": true`.
13. **G-PRINT on the logs**, into `62-print.log`: `/root/tz04a-env/venv/bin/python -B /root/liq-guard-svc/liq-guard.py scan /root/tz54-work/logs/*.log` must print `G-PRINT PASS`. A FAIL names the file and the kind found, never the value, and is BLOCKED: the file is copied by §9 to the forensic store alone, and the report names it.
14. **The report, the reclaim and the last scan, in this order:** the report drafted at its path (§8); **§9's B-RECLAIM-OWN**, its lines quoted in the draft's §3; then **G-PRINT on the report**, from the session: `/root/tz04a-env/venv/bin/python -B /root/liq-guard-svc/liq-guard.py scan /root/btc-5m-twap/CryptoReports/TZ-54-liq-guard-report.md` must print `G-PRINT PASS` — the Executor gives its two lines to the Boss in the chat, since the report cannot quote a scan of itself — and only then the report committed and pushed to `main`. A FAIL: the report is written again without what was found, and scanned again.

---

## 4. Gates — fixed here, before any of their data exists

| gate | step | PASS |
|---|---|---|
| READY | §0.0 | `ready=1` |
| STAGE | §0.1 | four lines `created`, each at its SHA-256 |
| FINGERPRINT | §0.2 | the line §0.2 quotes |
| HOST | §0.3 | H1 to H5 |
| NUMBER and REFS | §0.4 | `NUMBER PASS - 2 of 2`; no branch of this TZ on `origin` |
| BRANCH | §3 step 6 | three files `created`; the push on `origin` at `HEAD`; the numstat's three lines exactly |
| C-SELF | §3 step 7 | `141` of `141`, the hook's refusals `5` |
| G-SELF | §3 step 7 | `SELFTEST PASS: 83 checks` |
| SCRATCH | §3 step 8 | every directory named earlier reclaimed and gone; none named live touched |
| SECRETS | §3 step 9 | five required credentials written or kept, the sixth written, kept or skipped; `exit=0`; `/etc/liq-guard` `0700`, its files `0600`, root's |
| CHAT | §3 step 10 | `FIND-CHAT … 1, pinned` or `pinned already, kept`; `exit=0` |
| G-MEM | B-DEPLOY 2 | `MemAvailable` at or above `100,663,296` at one of five reads |
| G-INSTALL | B-DEPLOY 3 | both files at §0.1's SHA-256 in `/root/liq-guard-svc/`, the unit file equal by `cmp`, `loaded`, `disabled` |
| G-PROVE | B-DEPLOY 4 | `PROVE PASS: 10 gates of 10 passed`, its record `"pass": true` with this code's SHA-256 — G-CRED, G-TIME, G-KEY, G-POS, G-BRACKET, G-PUSH, G-TG, G-SEE, G-ALARM, G-HC, in this order, each `PASS` (§1.5) |
| G-UNIT | B-DEPLOY 5 | `60` s after `enable --now`: `active`, `running`, `NRestarts` `0`, `enabled`, `WatchdogUSec` `5min`; the guard's state `key_ok` `True`, `blind` `False`, `polls_ok` at least `1`; its line `SERVE start: key True, positions read N` |
| G-LIVE | B-DEPLOY 6 | `900` s after the start: `active`, `NRestarts` `0`, the same `MainPID`; `key_ok` `True`, `blind` `False`, `polls_ok` at least `150` — `180` passes of `5` s, a sixth of them spare — and `disk_faults` `0` |
| G-DEPLOY | §3 step 11 | `B-DEPLOY END exit=0` |
| G-AFTER | §3 step 12 | the unit `active`, `NRestarts` `0`; its files at §0.1's SHA-256; `prove.json` `"pass": true` |
| G-PRINT | §3 steps 13 and 14 | `G-PRINT PASS` on every log, and on the report before it is committed |

**Every gate is asserted where it is read** — in the checker, the guard or B-DEPLOY, which exit non-zero — or read by the Executor against the literal above; **a gate read by eye is named so in the report**. A FAIL is BLOCKED but where §3 step 11 allows one more B-DEPLOY.

---

## 5. The files

**Appendix A — `guard/liq-guard.py`**, fixed by the Architect and written byte for byte; standard library alone. Its sections: the constants (lines 44 to 99); files and credentials (lines 118 to 209); the network, IPv4 alone, and its clients — Binance, Pushover, Telegram, healthchecks.io and systemd's notify socket (lines 214 to 405); the readings, pure functions (lines 410 to 593); the guard's pass, `Guard` (lines 607 to 972); the modes — `secrets`, `find-chat`, `prove`, `status`, `scan`, `serve` — and `refuse` (lines 981 to 1322); the self-test's stand-ins, `binance_lp` and `on_terminal` (lines 1327 to 1485); the self-test (lines 1488 to 1832); `main` (lines 1835 to 1846). **Exits:** `0` done; `1` a failed assert or a BLOCK; `2` refused — a key that can do more than read, or a credential missing or malformed — which its unit does not restart; `4` a reading's FAIL. **Appendix B — `deploy/systemd/liq-guard.service`**, installed byte for byte (§1.7). **Appendix C — `b-deploy.sh`**, staged and never committed (§3 step 11). **`research/tz54-liq-guard.py`** — §0.1's checker.

---

## 6. Cost

At the populations' upper bounds (§10 C4): `selftest` under `1` s — `0.15` s at the Architect's runs, its peak `27,080` KiB with its pseudo-terminal children; the checker's `selftest` about `1` s, its peak `35,901,440` bytes at the Architect's run; `fingerprint` under `1` s over 70 rows; `number`, `refs`, `scratch` about `1` s each; `reclaim` under `2` s over at most `50,000,000` bytes; `find-chat` at most `1,800` s, in the background; `scan` under `1` s over the logs. **B-DEPLOY:** the memory's reads at most `300` s; G-PROVE's requests under `30` s beside its two waits of at most `900` s each — the Boss's answer and his acknowledgement; G-UNIT `60` s; G-LIVE `900` s from the start — **at most about `3,100` s**, under its unit's `RuntimeMaxSec`, `7,200`. **Waits, not compute:** the Boss's credentials, his `/start`, his answer and his acknowledgement. **No check reaches `3,600` s of compute.** **The unit:** `MemoryMax` `96` MiB against the guard's peak under `30` MB; on disk its journal at most about `1,600` lines a day — a tick every `10` minutes, a repeating error once a minute at most, a few events — about `400,000` bytes a day at the worst and `90` days kept, so under `40,000,000` bytes, against map §6's disk margin of `2,797,417,277` at TZ-50's read; at Binance, `60` request weight a minute of its `2,400`; at Telegram, one `getUpdates` a pass; at Pushover, at most `20` alarms an hour (`PUSH_PER_HOUR`, line 64), its free account's `10,000` messages a month. Fail-fast bounds, each derived: `TIMEOUT_S` `10` — a reply from any of the five hosts in under a second, ten times over, and at most one wait of it a host a pass by the cooldown, five hosts, under `60` s — well under the watchdog's `300` s; `COOLDOWN_S` `15` — three passes; `BLIND_S` `120` — two failed minutes, not one slow reply; `SEE_WAIT_S` and `TEST_WAIT_S` `900` — the Boss reads a message and answers, with room; `FIND_CHAT_S` `1,800` — his Start, after the message that asks for it.

---

## 7. Validation

**The guard's self-test, `83` checks, fixed by the Architect as this TZ's Validation** (`mode_selftest`, lines 1488 to 1832), each an `assert` that ends the run: **the margin hint against Binance's own liquidation formula** — three positions, short and long, two maintenance rates and a maintenance amount, each margin added moving the liquidation price to exactly `8`% within `1e-9` — and no hint beyond it; both sides' distances; **the levels over a descent of thirteen reads** — announced `[0, 1, 0, 2, 0, 3, 0, 0, 3, 0, 3, 0, 1]` — and the one-point re-arm; the positions of v3 and v2 replies, hedge and one-way; the brackets; **the key's permissions — read-only and bound accepted, and five widenings, an unbound key and a missing field each refused**; the commands and thresholds; the notation; the scrub; **every connection resolved in IPv4 alone**; the cooldown; **`secrets` at a real pseudo-terminal**, a malformed answer refused and asked again, no value echoed or logged, the files `0600`, a second run keeping them; `find-chat`; **`prove` — its ten gates, a key that can trade refused, an answer «нет» failing it before any alarm**, v2 where v3 is not served; **the guard's pass** — a descent alarming once a level, the second alarm's text, re-arming after margin, a new descent alarming again, the commands from the pinned chat alone with a stranger's thresholds ignored, new thresholds ringing nothing at once, a `429` holding the reads back, the test alarm acknowledged, **blindness alarmed once and reminded, with one step failing beside it**, seen again, **a full disk stopping no alarm**, Pushover down and the alarm sent once it is up, Telegram down with its queue bounded and sent five a pass, the heartbeat once a day and quiet, a key widened at a later check refused, no credential or chat id in any file of the record, every file `0600`, the watchdog notified, no host but the five; and **`scan`** — a clean file passing and a token, the chat id and an address found. **The Architect's runs on these bytes:** `SELFTEST PASS: 83 checks` under Python 3.12 and 3.13; and the self-test **fails** on each of eight mutations of the code — the hint's sign, the IPv4 family, `ipRestrict` ignored, the re-arm removed, a foreign chat accepted, the blind interval tenfold, an answer read as «да» whatever it says, and the outbox unbounded. **B-DEPLOY** was run by the Architect against stand-ins of systemd and the guard: its PASS path to `END exit=0`, a G-PROVE FAIL that started nothing, and a G-UNIT FAIL that stopped the unit with `disable --now`. **Appendix B** passed `systemd-analyze verify` under systemd 255, the host's version. **The checker's** `fingerprint` printed §0.2's line against `main` at `aeaca24`, and its self-test `141` of `141`.

---

## 8. The report

`CryptoReports/TZ-54-liq-guard-report.md`, contract §8's sections in their order. **§2 Measurements:** the readiness and host gate's lines but the counted address; every log's gate lines as printed; the B-DEPLOY log whole; `prove.json` whole; the unit's state after; `status`'s lines; `MemAvailable` at each read; the instants of the Boss's «готово», his `/start`, his answer and his acknowledgement as the logs carry them. **§3:** the branch, its commit, the pull request, the numstat, contract §4.2's self-check, and `b-deploy.sh`'s SHA-256 with its forensic copy. **§4:** every gate of §4, `PASS` or `FAIL`, asserted or read by eye. **§6:** every departure, every refusal by the classifier with its block, its words and who ran it, every block the Boss ran with its instant, and B-RESET and the second B-DEPLOY where they ran. **The report prints no credential, chat id, address of this host, or symbol, price, size or margin of the Boss's positions** — G-PRINT reads it before it is committed.

---

## 9. Reclaim — the host left clean (CANON hard rule 15)

**B-RECLAIM-OWN**, with the report drafted and before G-PRINT reads it (§3 step 14). **Its output is written to no file; the report's §3 quotes it verbatim from the session**, every line of it:

```
(cd /root/tz54-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz54-work/wt/research/tz54-liq-guard.py reclaim /root/tz54-work); echo "reclaim exit=$?"
cd /root/btc-5m-twap && git -C /root/btc-5m-twap worktree remove /root/tz54-work/wt; echo "exit=$?"
rm -rf /root/tz54-work; echo "exit=$?"
test -e /root/tz54-work; echo "exit=$?"
git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
find /root/btc-forensics -type f | wc -l
df -B1 --output=source,size,avail /var/lib/btc-recorder
```

`reclaim` must print `RECLAIM PASS` before the removals: it copies every regular file of `/root/tz54-work` but the worktree's and the checker's temporary tree's — the logs, the stage's four files and B-DEPLOY's `inst` copies — into `/root/btc-forensics/` as `tz54-work--<path with / as -->`, by exclusive create, its hash verified, free space at or above `7,400,000,000` after each copy. **No file of this run is held by a Release** (map §7 item 167). The last `test -e` must print `exit=1`. **Its paste**, where the classifier refuses any line: the same lines chained with `&&`, the removals reached only after `RECLAIM PASS`. **Kept on the host — the guard's:** `/root/liq-guard-svc/`, `/var/lib/liq-guard/`, `/etc/liq-guard/` and the enabled unit.

---

## 10. Pre-send checks

Performed on this file as sent, in a reading separate from its writing; every count below re-derived for it.

| # | check | result |
|---|---|---|
| **C1** | scope against body | **Named by the body, each inside §2.** *Repository, written:* the three files of the branch and its pull request, the report on `main` — §2 item 1. *Read:* this file by §0.1's script, `research/tz53-l1-account.py` by `git show`, `SYSTEM-MAP.md` and its §0 table's 70 rows' files — `docs/l1-sign.html` among them — by `fingerprint`, `CryptoTZ/` and `CryptoReports/` by `number`, the refs by `refs` — §2 item 1. *Capture host, written:* `/root/tz54-work/**` with `wt`, `inst`, `selftest-tmp` and the worktree's record; the guard's self-test's tree under `/tmp`; `/root/liq-guard-svc/`, `/var/lib/liq-guard/`, `/etc/liq-guard/` and its seven files' names, the unit file, the transient unit, the forensic store's `tz54-work--*`, earlier session directories — §2 item 2, B-RESET's removal its named exemption. *Read:* `/proc`, `df`, the recorder's store by `find` and `grep -c`, five units' `systemctl show`, `ip -4` counted, the guard's files by its modes, four fields of `state.json` by B-DEPLOY, `prove.json` and `service.log`'s tail by §3 step 12 — §2 item 3. *Network:* the written authorization's and GitHub's — §2 item 4. **Intersections found and resolved:** the host gate's reads of other units' state and of the recorder's store against §2 item 5's "not touched" — written into §2 item 5 as a named exemption; the guard's self-test's `/tmp` tree and the worktree's record, absent from §2 item 2 in the first draft — added. **By content class:** an output carrying a credential, the chat id, the host's address or a position's figure — the guard's messages to the Boss's own chat carry positions and are named in §2 item 6 as the product; `prove.json`, `status`, `find-chat`, `secrets`, `scan` and B-DEPLOY print counts, names, booleans and states alone (§1.6), and G-PRINT reads every log and the report for every credential, the chat id and the host's addresses. **No other intersection.** |
| **C2** | origin of every expectation | **Computed by an implementation independent of the one under test:** the four staged files' and the base's lines, bytes and SHA-256 — `wc` and `sha256sum` over the bytes, and §0.1's script run by the Architect against this file, four lines `created` and three on `branch`, a second run `equal, kept`; the numstat's `29`, `1850`, `3323` — `wc -l`; **`83` checks — counted by a profiler outside the self-test's own counter, `83` `check` calls**; the levels `[0, 1, 0, 2, 0, 3, 0, 0, 3, 0, 3, 0, 1]` — derived by hand from `5`, `3`, `1.5` and the one-point re-arm, read by read; the hint's `8`% — the selftest's `binance_lp`, Binance's closed formula, against `margin_hint`'s derivative. **Quoted from a committed artifact:** the fingerprint line's revision and its `70`, `67`, `2`, `1` — map §0's own count; `141` of `141` and `refused by the hook: 5` — TZ-53's report, its lines 992 and 993; `7,400,000,000` — the checker's `RECLAIM_FLOOR`, its line 295, and map §6; `100,663,296` — Appendix B's `MemoryMax=96M`; the map's `MemAvailable` range and disk margin — map §6. **Inequalities, holding for every admissible value:** `polls_ok` at least `150` in `900` s at `5` s a pass; `MemAvailable` at or above its floor. **The Boss's credentials' lengths are no literal of this TZ:** §3 step 9 reads `written, N bytes`. **No expectation depends on a quantity this TZ measures.** |
| **C3** | shape of every diff | `git ls-tree -r --name-only origin/main` at `aeaca24` holds none of `guard/`, `deploy/systemd/liq-guard.service` or `research/tz54-liq-guard.py`: **three new files, no line replaced**; the numstat asserts `N 0` for each. |
| **C4** | cost of every check | §6, at the populations' upper bounds: the self-tests under `1` s and about `1` s, the checker's modes about `1` s over `70` rows, `reclaim` under `2` s over at most `50,000,000` bytes, `scan` under `1` s over the logs; B-DEPLOY at most about `3,100` s, almost all of it waits for the Boss and G-LIVE's `900` s; `find-chat` at most `1,800` s, a wait. **No check reaches `3,600` s of compute.** Each fail-fast bound derived beside it in §6. |
| **C5** | every count | `four` staged files and `three` on the branch — §0.1's `FILES`; `five` required credentials and a `sixth` — Appendix A's `CREDENTIALS`, six rows, five `True`; `ten` gates — `PROVE_GATES`, line 71; `H1` to `H5` — §0.3's five bullets; `five` reads of memory — B-DEPLOY's loop `1 2 3 4 5`; `three` positions, `five` widenings, `thirteen` reads and `eight` mutations in §7 — the self-test's tuples, its five refused keys, its thirteen-value list and the eight `sed` edits the Architect ran; `70` rows of map §0. Each re-derived from the set it counts. |
| **C6** | every population | `polls_ok` — the passes of the unit since its start, read at `60` s and `900` s; `disk_faults` — the unit's writes since its start; `MemAvailable` — five reads a minute apart at B-DEPLOY's step 2; `scan` — every `.log` under `/root/tz54-work/logs/`, then the report; `fingerprint` — map §0's `70` rows; `reclaim` — every regular file of `/root/tz54-work` but `wt` and `selftest-tmp`; `scratch` — the UUID directories beside this session's own; G-POS and G-SEE — every position `positionRisk` serves at the prove's instant. |
| **C7** | every signature and every behaviour | **Committed, read at `aeaca24`, `research/tz53-l1-account.py`, each at its renamed line in the checker:** `def mode_fingerprint():` — prints `FINGERPRINT PASS: revision %s; anchors 6 of 6, 4 re-derived; rows %d: frozen %d of %d equal, tracked %d, reported %d; the signing page on main equal to TZ-50's Appendix B` and asserts `states == MAP_ROWS`; `def mode_number():` — `NUMBER %s` `PASS - 2 of 2`; `def mode_refs():` — `assert not branch, "BLOCKED: refs/heads/%s exists on origin already"`; `def mode_scratch(own):` — `live, process %s` or `earlier` by a start from `t - 1` to `t + LIVE_S`; `def mode_reclaim(trees):` — `open(dest, "xb")`, the copy's SHA-256 checked, `avail - size >= RECLAIM_FLOOR`, `RECLAIM PASS`; `main` — `assert os.getcwd() == WORK`. **Appendix A's own, each sentence against the lines it cites:** 38 references of the form `name`, lines a to b, and `NAME`, line n, checked mechanically against the definitions' spans in Appendix A's syntax tree — 36 equal to one definition's span or one constant's line, and 2 joint: `Guard.journal` and `Guard.err`, lines 657 to 678, two adjacent definitions with nothing between, and `ALARM_RETRY_S`, `ALARM_EXPIRE_S`, line 62, two names on one line; §5's nine section ranges read by their first and last lines. **The standard library, Python 3.12:** `http.client.HTTPSConnection.__init__` sets `self._context = context` (its line 1494), which `V4HTTPS.connect` wraps the IPv4 socket with; `getpass`'s flush of what was typed before a hidden question, TZ-51 §10 C7's reading, unchanged. **systemd's, read on its manual pages:** `StartLimitIntervalSec=` "may be set to 0 to disable any kind of rate limiting"; a missed watchdog fails the service and `Restart=always` restarts it; `RestartPreventExitStatus=` prevents a restart "regardless of the restart setting"; `Type=notify` waits for `READY=1`; `NotifyAccess=main` accepts the main process's messages alone. **Binance's behaviours the body attributes are named as read, not measured** — §1.2 says so of the reading-only key, and G-SEE and G-KEY are the measurements. |
| **C8** | every cross-reference | **This file:** §0.0 to §0.4, §1.1 to §1.8, §2 items 1 to 6, §3 steps 1 to 14, §4, §5, §6, §7, §8, §9 and §10 — each reference resolved to the text it names. **CANON `2026-11-21-b`:** hard rules 2, 5, 9, 14, 15 and 17; PART IV's "one token serves one poller"; PART V's tool "judged against his trading without it"; PART VII's guard paragraph and its decision that the guard never adds margin — each read in the file and supporting its sentence. **The map, revision `2026-11-21-d`:** §0 and its table, §1, §3's units and trees, §6's eleven rows the header names — `git remote` added in this reading, cited by §3 step 6 and missing from the header's first draft — and §7 items 86, 91, 95, 115, 118, 137, 138, 144, 167, 174 and 176, each read in full; **item 166, in the first draft's header, cited by no sentence, removed.** **The contract:** §1 steps 1 to 4, §4.2, §5, §8 and §10. **No quotation of the Boss's own words.** |

---

## Appendix A — the guard, byte for byte

### `guard/liq-guard.py`

```python file=guard/liq-guard.py
#!/usr/bin/env python3
"""liq-guard.py - the liquidation guard (TZ-54, CANON PART VII): the Boss's Binance USD-M futures positions read
every five seconds through a key that can read and nothing else, each position's distance from its mark price to its
liquidation price held against three thresholds of his - a Telegram message, then Pushover's emergency alarm, then a
second one - and the guard's own loss of Binance alarmed the same way. It never trades and holds no key that can.
Standard library only; every connection IPv4, because the key is bound to the host's IPv4 address.

Modes:
    secrets     the Boss, at his terminal: the Binance key and secret, the Pushover user key and token, the Telegram
                token, the dead-man's ping address or none - each hidden, each written once, 0600, root's
    find-chat   the one private chat that sent /start to the guard's bot, pinned
    prove       every request path proved through this file's own functions, the key's permissions read, and a test
                alarm acknowledged on the Boss's phone (CANON hard rule 14); its record prove.json
    serve       the unit's loop, under systemd, Type=notify with a watchdog
    status      the guard's own state from its files - no symbol, price, size or margin is printed
    scan FILE.. G-PRINT: in each file, the occurrences of every credential, the chat id and this host's own IPv4
                addresses - counts alone; exit 4 where any is found
    selftest    every pure function and every flow against stand-ins, and `secrets` at a real pseudo-terminal
Exits: 0 done; 1 a failed assert or a BLOCK; 2 refused - a key that can do more than read, or a credential missing or
malformed - which the unit does not restart; 4 a reading's FAIL. Never printed by any mode: a key, secret, token,
user key, ping address, chat id, address of this host, or any figure of a position."""
import datetime as dt
import getpass
import hashlib
import hmac
import http.client
import json
import os
import re
import signal
import socket
import ssl
import sys
import threading
import time
import urllib.parse

if not __debug__:
    sys.stderr.write("liq-guard: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(2)

# ---- constants: none is measured by this file -------------------------------------------------------------------

ETC = "/etc/liq-guard"
VAR = "/var/lib/liq-guard"
UA = "btc-5m-twap-liq-guard"
FAPI, SAPI, PUSHOVER, TG, HC = "fapi.binance.com", "api.binance.com", "api.pushover.net", "api.telegram.org", "hc-ping.com"
POSITION_PATHS = ("/fapi/v3/positionRisk", "/fapi/v2/positionRisk")
POLL_S = 5                    # one read of the positions; its weight 5 is 60 a minute of Binance's 2,400
TIMEOUT_S = 10                # a request's socket timeout: two reads and a send fit a watchdog interval
RECV_WINDOW = 10000           # ms; the clock is read from Binance every hour besides
BLIND_S = 120                 # no read for this long: the guard is blind and says so
BLIND_REPEAT_S = 1800
TIME_SYNC_S, BRACKETS_S, PERM_S, PERM_RETRY_S = 3600, 3600, 6 * 3600, 60
HC_S, TICK_S, STATE_S = 60, 600, 30
ERR_EVERY_S = 60             # one journal line a minute for a repeating error
KEEP_DAYS = 90               # journal files older than this are removed at the tick
BACKOFF_S = {429: 60, 418: 300}   # Binance's rate refusals: no request to it until this has passed
DEFAULT_THRESHOLDS = (5.0, 3.0, 1.5)   # percent of the mark price: Telegram, the alarm, the second alarm
REARM_PP = 1.0                # a level re-arms once the distance is this many points above its threshold
TARGET_PCT = 8.0              # the distance the margin hint aims the liquidation price at
ALARM_RETRY_S, ALARM_EXPIRE_S = 30, 3600       # Pushover's emergency priority: its minimum retry, an hour
TEST_EXPIRE_S, TEST_WAIT_S, RECEIPT_EVERY_S = 900, 900, 10
PUSH_PER_HOUR = 20
OUTBOX_TRIES = 10
OUTBOX_MAX = 100             # Telegram messages beyond this, oldest first, are dropped; alarms never
TG_PER_PASS = 5              # Telegram messages sent in one pass; the rest wait for the next
COOLDOWN_S = 15              # a host that failed at the network is not tried again for this long
HEARTBEAT_UTC = (19, 0)       # 23:00 in Batumi
FIND_CHAT_S = 1800
PROVE_GATES = ("G-CRED", "G-TIME", "G-KEY", "G-POS", "G-BRACKET", "G-PUSH", "G-TG", "G-SEE", "G-ALARM", "G-HC")
SEE_WAIT_S = 900             # the Boss's answer to what the guard sees, at prove
LONG_POLL_S = 25             # Telegram's long poll in find-chat and prove; their sockets wait 40 s
YES, NO = ("да", "yes", "совпадает"), ("нет", "no", "не совпадает")
READ_PERMS = ("enableReading", "enableFixReadOnly")
CORE_PERMS = ("enableReading", "ipRestrict", "enableWithdrawals", "enableFutures", "enableSpotAndMarginTrading")
LABEL = {"binance-key": "ключ Binance", "binance-secret": "секрет Binance", "pushover-user": "User Key Pushover",
         "pushover-token": "токен Pushover", "tg-token": "токен бота", "hc-url": "адрес пинга"}
LEVEL_NAME = {1: "предупреждение", 2: "тревога", 3: "последний звонок"}
SIDE_RU = {"LONG": "лонг", "SHORT": "шорт"}
KEYBOARD = {"keyboard": [[{"text": "Статус"}, {"text": "Тест"}], [{"text": "Пороги"}, {"text": "Помощь"}]],
            "resize_keyboard": True, "is_persistent": True}
IPV4 = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")
CREDENTIALS = (   # name, form, required, the Boss's prompt
    ("binance-key", r"[A-Za-z0-9]{32,128}", True,
     "Binance — API Key ключа «только чтение» (ввод скрыт): "),
    ("binance-secret", r"[A-Za-z0-9]{32,128}", True,
     "Binance — Secret Key того же ключа (ввод скрыт): "),
    ("pushover-user", r"[A-Za-z0-9]{30}", True,
     "Pushover — ваш User Key, вверху страницы pushover.net (ввод скрыт): "),
    ("pushover-token", r"[A-Za-z0-9]{30}", True,
     "Pushover — API Token приложения «Сторож» (ввод скрыт): "),
    ("tg-token", r"[0-9]{5,12}:[A-Za-z0-9_-]{30,64}", True,
     "Telegram — токен бота «Сторож» от BotFather (ввод скрыт): "),
    ("hc-url", r"https://hc-ping\.com/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", False,
     "healthchecks.io — адрес пинга (https://hc-ping.com/…), или просто Enter — без него (ввод скрыт): "),
)
FORM = {n: re.compile(f) for n, f, _r, _p in CREDENTIALS}
FORM["tg-chat"] = re.compile(r"-?[0-9]{1,20}")


def out(*parts):
    sys.stdout.write(" ".join(str(p) for p in parts) + "\n")
    sys.stdout.flush()


def utc(t):
    return dt.datetime.fromtimestamp(t, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_file(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


# ---- files -------------------------------------------------------------------------------------------------------

def file_state(path):
    """A path's kind, mode, owner and size - never its content: all that is printed of a credential."""
    try:
        st = os.lstat(path)
    except FileNotFoundError:
        return "absent"
    kind = "dir" if os.path.isdir(path) and not os.path.islink(path) else (
        "file" if os.path.isfile(path) and not os.path.islink(path) else "other")
    return "%s mode %04o uid %d bytes %d" % (kind, st.st_mode & 0o7777, st.st_uid, st.st_size)


def private_file_ok(path, mode=0o600, uid=0):
    """A regular file, not a link, of `uid`, of `mode`, not empty."""
    try:
        st = os.lstat(path)
    except FileNotFoundError:
        return False
    return (os.path.isfile(path) and not os.path.islink(path) and st.st_uid == uid
            and st.st_mode & 0o7777 == mode and st.st_size > 0)


def private_dir(path, uid=0):
    """`path` made 0700 where absent; asserted a directory of `uid`, 0700, not a link."""
    if not os.path.isdir(path):
        os.mkdir(path, 0o700)
    st = os.lstat(path)
    assert not os.path.islink(path) and st.st_uid == uid and st.st_mode & 0o7777 == 0o700, \
        "%s: %s" % (path, file_state(path))


def write_private(path, data, uid=0):
    """`data` to `path` by exclusive create, 0600 from its first byte. Returns the bytes written."""
    private_dir(os.path.dirname(path), uid)
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        os.write(fd, data)
        os.fsync(fd)
    finally:
        os.close(fd)
    assert private_file_ok(path, uid=uid), "%s: %s" % (path, file_state(path))
    return len(data)


def replace_private(path, data, uid=0):
    """`data` to `path` through a 0600 file beside it and a rename: no reader sees half a file."""
    private_dir(os.path.dirname(path), uid)
    tmp = path + ".tmp"
    if os.path.exists(tmp):
        os.unlink(tmp)
    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        os.write(fd, data)
        os.fsync(fd)
    finally:
        os.close(fd)
    os.replace(tmp, path)


def read_credentials(etc=ETC, uid=0):
    """{name: value} of every credential present; refused (exit 2) where a required one is absent, malformed, or
    not a 0600 file of `uid`. The dead-man's address may be absent."""
    creds, problems = {}, []
    for name in [c[0] for c in CREDENTIALS] + ["tg-chat"]:
        path = os.path.join(etc, name)
        required = name == "tg-chat" or dict((c[0], c[2]) for c in CREDENTIALS)[name]
        if not os.path.lexists(path):
            if required:
                problems.append("%s absent" % name)
            continue
        if not private_file_ok(path, uid=uid):
            problems.append("%s: %s" % (name, file_state(path)))
            continue
        with open(path, encoding="utf-8") as fh:
            v = fh.read().strip()
        if not FORM[name].fullmatch(v):
            problems.append("%s malformed, %d bytes" % (name, len(v)))
            continue
        creds[name] = v
    return creds, problems


class Scrub:
    """Every loaded secret and every IPv4 address out of a text before it is printed, journaled or sent."""

    def __init__(self, creds=None):
        self.values = sorted((v for k, v in (creds or {}).items() if k != "tg-chat" and v), key=len, reverse=True)

    def __call__(self, text):
        t = str(text)
        for v in self.values:
            t = t.replace(v, "***")
        return IPV4.sub("x.x.x.x", t)


# ---- the network: IPv4 alone, one kept connection a host ----------------------------------------------------------

class V4HTTPS(http.client.HTTPSConnection):
    """An HTTPS connection whose every (re)connect resolves the host to IPv4 alone."""

    def connect(self):
        infos = socket.getaddrinfo(self.host, self.port, socket.AF_INET, socket.SOCK_STREAM)
        assert infos, "no IPv4 address for %s" % self.host
        sock = socket.create_connection(infos[0][4], self.timeout)
        self.sock = self._context.wrap_socket(sock, server_hostname=self.host)


class Net:
    """call(host, method, path, body, headers) -> (status, bytes). A kept connection is reopened once where the
    server closed it while idle; a host that failed at the network is not tried again for COOLDOWN_S, so that one
    pass of the loop waits at most one timeout a host."""

    def __init__(self, timeout=TIMEOUT_S, clock=time.monotonic):
        self.timeout, self.clock, self.conns, self.count, self.down_until = timeout, clock, {}, {}, {}

    def call(self, host, method, path, body=None, headers=()):
        if self.clock() < self.down_until.get(host, 0.0):
            raise ConnectionError("%s not tried: it failed less than %d s ago" % (host, COOLDOWN_S))
        try:
            return self._call(host, method, path, body, headers)
        except (OSError, http.client.HTTPException):
            self.down_until[host] = self.clock() + COOLDOWN_S
            raise

    def _call(self, host, method, path, body, headers):
        hdrs = dict(headers)
        hdrs.setdefault("User-Agent", UA)
        self.count[host] = self.count.get(host, 0) + 1
        for attempt in (1, 2):
            c = self.conns.get(host)
            reused = c is not None and c.sock is not None
            if c is None:
                c = self.conns[host] = V4HTTPS(host, 443, timeout=self.timeout,
                                               context=ssl.create_default_context())
            try:
                c.request(method, path, body=body, headers=hdrs)
                r = c.getresponse()
                data = r.read()
                if r.will_close:
                    c.close()
                return r.status, data
            except (http.client.RemoteDisconnected, BrokenPipeError, ConnectionResetError):
                c.close()
                self.conns.pop(host, None)
                if attempt == 2 or not reused:
                    raise
            except Exception:
                c.close()
                self.conns.pop(host, None)
                raise


def json_of(data):
    try:
        return json.loads(data.decode("utf-8"))
    except (ValueError, UnicodeDecodeError, AttributeError):
        return None


class Refused(Exception):
    """A request the far end answered and refused: its status and its own words."""

    def __init__(self, host, status, words):
        Exception.__init__(self, "%s answered %s: %s" % (host, status, words))
        self.status, self.words = status, words


class Binance:
    def __init__(self, net, key, secret, now=time.time):
        self.net, self.key, self.secret, self.now, self.offset_ms = net, key, secret, now, 0
        self.position_path = None

    def _get(self, host, path, signed=False):
        headers = [("Accept", "application/json")] + ([("X-MBX-APIKEY", self.key)] if signed else [])
        status, data = self.net.call(host, "GET", path, None, headers)
        doc = json_of(data)
        if status != 200 or doc is None:
            words = ("%s %s" % (doc.get("code"), doc.get("msg"))) if isinstance(doc, dict) else "%d bytes" % len(data)
            raise Refused(host, status, words)
        return doc

    def signed(self, host, path, params=()):
        ts = int(self.now() * 1000) + self.offset_ms
        q = urllib.parse.urlencode(list(params) + [("recvWindow", RECV_WINDOW), ("timestamp", ts)])
        sig = hmac.new(self.secret.encode(), q.encode(), hashlib.sha256).hexdigest()
        return self._get(host, "%s?%s&signature=%s" % (path, q, sig), signed=True)

    def sync_time(self):
        t0 = self.now()
        doc = self._get(FAPI, "/fapi/v1/time")
        t1 = self.now()
        assert isinstance(doc, dict) and isinstance(doc.get("serverTime"), int), "time: %r" % (doc,)
        self.offset_ms = doc["serverTime"] - int((t0 + t1) * 500)
        return self.offset_ms

    def positions(self):
        paths = (self.position_path,) if self.position_path else POSITION_PATHS
        for k, path in enumerate(paths):
            try:
                doc = self.signed(FAPI, path)
            except Refused as e:
                if e.status == 404 and k + 1 < len(paths):
                    continue
                raise
            self.position_path = path
            return doc
        raise AssertionError("unreachable")

    def brackets(self, symbol):
        return self.signed(FAPI, "/fapi/v1/leverageBracket", [("symbol", symbol)])

    def restrictions(self):
        return self.signed(SAPI, "/sapi/v1/account/apiRestrictions")


class Pushover:
    def __init__(self, net, token, user):
        self.net, self.token, self.user = net, token, user

    def _post(self, path, fields):
        body = urllib.parse.urlencode(fields).encode()
        status, data = self.net.call(PUSHOVER, "POST", path, body,
                                     [("Content-Type", "application/x-www-form-urlencoded")])
        doc = json_of(data)
        if status != 200 or not isinstance(doc, dict) or doc.get("status") != 1:
            words = "; ".join(doc.get("errors") or []) if isinstance(doc, dict) else "%d bytes" % len(data)
            raise Refused(PUSHOVER, status, words)
        return doc

    def validate(self):
        return self._post("/1/users/validate.json", {"token": self.token, "user": self.user})

    def send(self, title, message, priority, expire=ALARM_EXPIRE_S):
        fields = {"token": self.token, "user": self.user, "title": title[:250], "message": message[:1024],
                  "priority": priority}
        if priority == 2:
            fields.update(retry=ALARM_RETRY_S, expire=expire, tags="liq-guard")
        return self._post("/1/messages.json", fields).get("receipt")

    def receipt(self, receipt):
        assert re.fullmatch(r"[A-Za-z0-9]{20,40}", receipt or ""), "receipt: malformed"
        status, data = self.net.call(PUSHOVER, "GET", "/1/receipts/%s.json?token=%s" % (receipt, self.token))
        doc = json_of(data)
        if status != 200 or not isinstance(doc, dict) or doc.get("status") != 1:
            raise Refused(PUSHOVER, status, "receipt")
        return doc

    def cancel(self, receipt):
        assert re.fullmatch(r"[A-Za-z0-9]{20,40}", receipt or ""), "receipt: malformed"
        return self._post("/1/receipts/%s/cancel.json" % receipt, {"token": self.token})


class Telegram:
    def __init__(self, net, token):
        self.net, self.token = net, token

    def call(self, method, **params):
        status, data = self.net.call(TG, "POST", "/bot%s/%s" % (self.token, method),
                                     json.dumps(params).encode(), [("Content-Type", "application/json")])
        doc = json_of(data)
        if not isinstance(doc, dict) or doc.get("ok") is not True:
            raise Refused(TG, status, doc.get("description") if isinstance(doc, dict) else "%d bytes" % len(data))
        return doc["result"]

    def send(self, chat, text, quiet=False):
        return self.call("sendMessage", chat_id=int(chat), text=text[:4000], disable_notification=bool(quiet),
                         reply_markup=KEYBOARD)


def hc_ping(net, url):
    u = urllib.parse.urlsplit(url)
    assert u.scheme == "https" and u.hostname == HC, "the dead-man's address is not hc-ping.com"
    status, data = net.call(HC, "GET", u.path)
    if status != 200 or data.strip() != b"OK":
        raise Refused(HC, status, "%d bytes" % len(data))
    return True


def sd_notify(msg):
    """systemd's notify socket, where the unit gives one: READY=1 once, WATCHDOG=1 every cycle."""
    addr = os.environ.get("NOTIFY_SOCKET")
    if not addr:
        return False
    if addr.startswith("@"):
        addr = "\0" + addr[1:]
    with socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM) as s:
        s.connect(addr)
        s.sendall(msg.encode())
    return True


# ---- the readings: pure functions ---------------------------------------------------------------------------------

def num(x):
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    return v if v == v and v not in (float("inf"), float("-inf")) else None


def parse_positions(doc):
    """The open positions of positionRisk's reply, v3 or v2: symbol, side, quantity, mark, liquidation price,
    notional, isolated or not. Pure."""
    assert isinstance(doc, list), "positionRisk: not a list"
    found = []
    for e in doc:
        assert isinstance(e, dict) and isinstance(e.get("symbol"), str), "positionRisk: an entry %r" % (type(e),)
        amt = num(e.get("positionAmt"))
        if not amt:
            continue
        ps = e.get("positionSide")
        side = ps if ps in ("LONG", "SHORT") else ("LONG" if amt > 0 else "SHORT")
        mark = num(e.get("markPrice"))
        notional = num(e.get("notional"))
        found.append({"symbol": e["symbol"], "side": side, "key": "%s:%s" % (e["symbol"], side), "qty": abs(amt),
                      "mark": mark, "liq": num(e.get("liquidationPrice")),
                      "notional": abs(notional) if notional is not None else abs(amt) * (mark or 0.0),
                      "isolated": (num(e.get("isolatedWallet")) or 0.0) > 0 or e.get("marginType") == "isolated"})
    return found


def distance_pct(p):
    """Percent of the mark price between it and the liquidation price, on the side that loses; None where there is
    no liquidation price. At or under 0 the mark is at or past it. Pure."""
    mark, liq = p.get("mark"), p.get("liq")
    if not mark or mark <= 0 or liq is None or liq <= 0:
        return None
    return 100.0 * ((mark - liq) / mark if p["side"] == "LONG" else (liq - mark) / mark)


def crossed(d, th):
    """The highest level whose threshold `d` is at or under: 3, 2, 1, or 0. Pure."""
    for lvl, t in ((3, th[2]), (2, th[1]), (1, th[0])):
        if d <= t:
            return lvl
    return 0


def step(fired, d, th, rearm=REARM_PP):
    """(the level to announce now, or 0; the levels announced in this descent after this read). A level re-arms once
    `d` is above its threshold by `rearm` points; a read that crosses several levels at once announces the highest
    alone and counts the lower ones announced; no liquidation price re-arms every level. Pure."""
    if d is None:
        return 0, frozenset()
    left = {lvl for lvl in fired if not d > th[lvl - 1] + rearm}
    top = crossed(d, th)
    new = top if top and top not in left else 0
    return new, frozenset(left | set(range(1, top + 1)))


def bracket_for(doc, notional):
    """(maintMarginRatio, cum) of the leverage bracket holding `notional`, or None. `doc` is leverageBracket's
    reply for one symbol - an object, or a list of one. Pure."""
    if isinstance(doc, list):
        doc = doc[0] if len(doc) == 1 else {}
    for b in sorted((doc or {}).get("brackets") or [], key=lambda b: num(b.get("notionalFloor")) or 0.0):
        lo, hi, r = num(b.get("notionalFloor")), num(b.get("notionalCap")), num(b.get("maintMarginRatio"))
        if lo is not None and hi is not None and r is not None and lo <= notional < hi:
            return r, num(b.get("cum")) or 0.0
    return None


def margin_hint(p, mmr, target=TARGET_PCT):
    """USDT of margin that moves the liquidation price to `target` percent from the mark price; 0 where it is there
    already. For an isolated position the liquidation price is linear in its margin M: dLP/dM = 1/(Q(1+mmr)) for a
    short and -1/(Q(1-mmr)) for a long, so this is exact; for a cross position, an estimate. Pure."""
    t = target / 100.0
    if p["side"] == "SHORT":
        need = (p["mark"] * (1 + t) - p["liq"]) * p["qty"] * (1 + mmr)
    else:
        need = (p["liq"] - p["mark"] * (1 - t)) * p["qty"] * (1 - mmr)
    return max(0.0, need)


def key_reading(doc):
    """(read-only and bound to an address, the problems): the key's permissions as Binance reads them. Pure."""
    if not isinstance(doc, dict):
        return False, ["no permissions object"]
    problems = ["%s absent" % k for k in CORE_PERMS if not isinstance(doc.get(k), bool)]
    if doc.get("enableReading") is not True:
        problems.append("enableReading not true")
    if doc.get("ipRestrict") is not True:
        problems.append("ipRestrict not true")
    problems += ["%s true" % k for k, v in sorted(doc.items())
                 if (k.startswith("enable") or k.startswith("permits")) and k not in READ_PERMS and v is True]
    return not problems, problems


def perms_line(doc):
    """Every permission's name and value - booleans alone. Pure."""
    return ", ".join("%s %s" % (k, v) for k, v in sorted(doc.items()) if isinstance(v, bool))


def parse_command(text):
    """(command, arguments) of a chat message: status, test, thresholds, help, or None. Pure."""
    words = (text or "").strip().lower().replace("ё", "е").split()
    if not words:
        return None, []
    w = words[0].lstrip("/").split("@")[0]
    names = {"статус": "status", "status": "status", "тест": "test", "test": "test", "пороги": "thresholds",
             "thresholds": "thresholds", "помощь": "help", "help": "help", "start": "help"}
    return names.get(w), words[1:]


def thresholds_of(args):
    """Three thresholds from a message's words, `5 3 1,5`, or None: each a number, 0 < third < second < first <= 30.
    Pure."""
    if len(args) != 3:
        return None
    try:
        w, a, c = (float(x.replace(",", ".")) for x in args)
    except ValueError:
        return None
    if not (0 < c < a < w <= 30):
        return None
    return (round(w, 2), round(a, 2), round(c, 2))


def ru(x, d):
    s = "{:,.{}f}".format(x, d)
    return s.replace(",", " ").replace(".", ",")


def price(x):
    """A price in Russian notation, to about six significant digits. Pure."""
    if x is None:
        return "—"
    a = abs(x)
    d = 1 if a >= 1000 else 2 if a >= 100 else 3 if a >= 1 else min(8, max(4, 3 - int(f"{a:e}".split("e")[1])))
    return ru(x, d)


def pct(x):
    return "—" if x is None else ru(x, 1) + "%"


def usdt(x):
    return ru(x, 0) + " USDT"


def position_line(p, d, mmr, target=TARGET_PCT):
    """One position for the Boss: its distance, prices and the margin hint. Pure."""
    line = "%s %s: до ликвидации %s (цена %s → ликвидация %s)" % (
        p["symbol"], SIDE_RU[p["side"]], pct(d), price(p["mark"]), price(p["liq"]))
    if d is None:
        return line
    need = margin_hint(p, mmr or 0.0, target)
    if need > 0:
        line += "; долить %s%s, чтобы ликвидация ушла на %s%s" % (
            "≈ " if mmr is None or not p["isolated"] else "", usdt(need), ru(target, 0) + "%",
            "" if p["isolated"] else " (кросс-маржа — оценка)")
    return line


def alarm_text(items, mmrs, target=TARGET_PCT):
    """(title, message) of one alarm: items are (level, position, distance), the highest level first. Pure."""
    items = sorted(items, key=lambda i: (-i[0], i[2] if i[2] is not None else -1e9))
    lvl, p, d = items[0]
    title = "Сторож: %s — %s %s, до ликвидации %s" % (
        LEVEL_NAME[lvl].upper() if lvl == 3 else LEVEL_NAME[lvl], p["symbol"], SIDE_RU[p["side"]], pct(d))
    body = "\n".join(position_line(q, e, mmrs.get(q["symbol"]), target) for _l, q, e in items)
    return title, body


def private_starts(updates):
    """The private chats that sent /start among Telegram updates, sorted. Pure."""
    chats = set()
    for u in updates:
        m = u.get("message") if isinstance(u, dict) else None
        if not isinstance(m, dict):
            continue
        chat = m.get("chat") or {}
        if (m.get("text") or "").startswith("/start") and chat.get("type") == "private" \
                and isinstance(chat.get("id"), int):
            chats.add(chat["id"])
    return sorted(chats)


HELP = ("Сторож следит за твоими фьючерсными позициями Binance каждые 5 секунд — по ключу «только чтение».\n"
        "• Ближе первого порога до ликвидации — сообщение здесь; ближе второго — тревога Pushover (звучит сквозь "
        "беззвучный режим и «Сон», повторяется каждые 30 с, пока не нажмёшь «Подтвердить»); ближе третьего — "
        "второй звонок. В каждой тревоге — сколько долить, чтобы ликвидация ушла на 8% от цены.\n"
        "• Потеряет Binance дольше 2 минут — тоже разбудит.\n"
        "Команды: «Статус», «Тест» (проверить звонок перед сном), «Пороги», «Пороги 5 3 1,5» — задать свои, "
        "в процентах от цены. Сторож никогда не торгует и не доливает маржу сам.")


# ---- the guard: one cycle at a time, every effect through its stand-ins in the self-test ---------------------------

class Guard:
    def __init__(self, creds, net=None, now=time.time, var=VAR, uid=0, notify=sd_notify):
        self.creds, self.now, self.var, self.uid, self.notify = creds, now, var, uid, notify
        self.net = net or Net()
        self.scrub = Scrub(creds)
        self.bn = Binance(self.net, creds["binance-key"], creds["binance-secret"], now)
        self.po = Pushover(self.net, creds["pushover-token"], creds["pushover-user"])
        self.tg = Telegram(self.net, creds["tg-token"])
        self.chat, self.hc = int(creds["tg-chat"]), creds.get("hc-url")
        t = now()
        st = self.load_state()
        th = st.get("thresholds")
        self.th = tuple(th) if isinstance(th, list) and thresholds_of([str(x) for x in th]) else DEFAULT_THRESHOLDS
        self.tg_offset = st.get("tg_offset") if isinstance(st.get("tg_offset"), int) else 0
        self.hb_day = st.get("hb_day")
        self.fired, self.positions, self.mmr, self.outbox, self.pushes = {}, [], {}, [], []
        self.started, self.last_ok, self.polls_ok, self.polls_err, self.last_error = t, t, 0, 0, None
        self.blind, self.blind_next, self.key_ok, self.key_checked = False, 0.0, None, None
        self.next_time = self.next_key = self.next_hc = 0.0
        self.next_tick, self.next_state = t + TICK_S, 0.0
        self.test = None
        self.min_seen = None
        self.bn_error, self.bn_backoff, self.err_last = None, 0.0, (None, 0.0)
        self.disk_faults = 0

    # -- record ------------------------------------------------------------------------------------------------------
    def load_state(self):
        try:
            with open(os.path.join(self.var, "state.json"), encoding="utf-8") as fh:
                doc = json.load(fh)
            return doc if isinstance(doc, dict) else {}
        except (OSError, ValueError):
            return {}

    def save_state(self):
        t = self.now()
        doc = {"at": utc(t), "started": utc(self.started), "thresholds": list(self.th), "tg_offset": self.tg_offset,
               "hb_day": self.hb_day, "last_ok": utc(self.last_ok), "polls_ok": self.polls_ok,
               "polls_err": self.polls_err, "positions": len(self.positions),
               "with_liquidation": sum(1 for p in self.positions if distance_pct(p) is not None),
               "blind": self.blind, "last_error": self.last_error, "key_ok": self.key_ok,
               "key_checked": utc(self.key_checked) if self.key_checked else None, "dead_man": bool(self.hc),
               "outbox": len(self.outbox), "disk_faults": self.disk_faults, "pid": os.getpid()}
        self.next_state = t + STATE_S
        try:
            replace_private(os.path.join(self.var, "state.json"), (json.dumps(doc, sort_keys=True) + "\n").encode(),
                            self.uid)
        except OSError:
            self.disk_faults += 1

    def journal(self, ev, **fields):
        t = self.now()
        rec = {"t": utc(t), "ev": ev}
        rec.update({k: (self.scrub(v) if isinstance(v, str) else v) for k, v in fields.items()})
        d = os.path.join(self.var, "journal")
        try:
            private_dir(self.var, self.uid)
            private_dir(d, self.uid)
            fd = os.open(os.path.join(d, utc(t)[:10] + ".jsonl"), os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o600)
            try:
                os.write(fd, (json.dumps(rec, sort_keys=True, ensure_ascii=False) + "\n").encode())
            finally:
                os.close(fd)
        except OSError:
            self.disk_faults += 1

    def err(self, where, e):
        t = self.now()
        self.last_error = self.scrub("%s: %s" % (where, e))[:300]
        if self.err_last[0] != self.last_error or t - self.err_last[1] >= ERR_EVERY_S:
            self.err_last = (self.last_error, t)
            self.journal("error", where=where, error=self.last_error)

    # -- sending -----------------------------------------------------------------------------------------------------
    def say(self, text, quiet=False):
        self.outbox.append({"to": "tg", "text": text, "quiet": quiet, "tries": 0})

    def push(self, title, message, priority, expire=ALARM_EXPIRE_S):
        t = self.now()
        self.pushes = [x for x in self.pushes if x > t - 3600]
        if len(self.pushes) >= PUSH_PER_HOUR:
            self.journal("push_capped", title=title)
            self.say("Pushover: предел %d тревог в час достигнут — эта только здесь:\n%s\n%s" % (
                PUSH_PER_HOUR, title, message))
            return None
        self.pushes.append(t)
        m = {"to": "push", "title": title, "text": message, "priority": priority, "expire": expire, "tries": 0}
        self.outbox.append(m)
        return m

    def flush(self):
        """Every waiting message tried once, in order; a channel that fails is not tried again in this pass."""
        pending, self.outbox, failed, tg_sent = self.outbox, [], set(), 0
        for m in pending:
            if m["to"] in failed or (m["to"] == "tg" and tg_sent >= TG_PER_PASS):
                self.outbox.append(m)
                continue
            try:
                if m["to"] == "tg":
                    tg_sent += 1
                    self.tg.send(self.chat, m["text"], m["quiet"])
                else:
                    r = self.po.send(m["title"], m["text"], m["priority"], m["expire"])
                    self.journal("pushed", priority=m["priority"], title=m["title"], receipt=bool(r))
                    if m.get("test") and r:
                        self.test = {"receipt": r, "sent": self.now(), "next": self.now() + RECEIPT_EVERY_S,
                                     "deadline": self.now() + TEST_WAIT_S}
            except Exception as e:
                failed.add(m["to"])
                m["tries"] += 1
                self.err("send %s" % m["to"], e)
                if m["tries"] < OUTBOX_TRIES:
                    self.outbox.append(m)
                else:
                    self.journal("dropped", to=m["to"], tries=m["tries"])
                    if m["to"] == "push":
                        self.say("Pushover не принял тревогу за %d попыток: %s\n%s" % (
                            OUTBOX_TRIES, m["title"], m["text"]))
        tg = [m for m in self.outbox if m["to"] == "tg"]
        if len(tg) > OUTBOX_MAX:
            drop = {id(m) for m in tg[:len(tg) - OUTBOX_MAX]}
            self.outbox = [m for m in self.outbox if id(m) not in drop]
            self.journal("dropped", to="tg", count=len(drop))

    # -- the cycle ---------------------------------------------------------------------------------------------------
    def check_key(self):
        t = self.now()
        try:
            doc = self.bn.restrictions()
        except Exception as e:
            self.err("key", e)
            self.next_key = t + PERM_RETRY_S
            return
        ok, problems = key_reading(doc)
        self.key_checked, self.key_ok, self.next_key = t, ok, t + PERM_S
        self.journal("key", ok=ok, perms=perms_line(doc), problems=problems)
        if not ok:
            raise KeyRefused(problems)

    def poll(self):
        t = self.now()
        if t < self.bn_backoff:
            return False
        try:
            pos = parse_positions(self.bn.positions())
        except Exception as e:
            self.polls_err += 1
            self.err("positions", e)
            self.bn_error = self.last_error
            if isinstance(e, Refused):
                self.bn_backoff = t + BACKOFF_S.get(e.status, 0)
                if "-1021" in str(e.words):
                    self.next_time = 0.0
            return False
        alarms, fired = [], {}
        for p in pos:
            d = distance_pct(p)
            lvl, fired[p["key"]] = step(self.fired.get(p["key"], frozenset()), d, self.th)
            if lvl:
                alarms.append((lvl, p, d))
        self.positions = pos
        if alarms:
            self.refresh_brackets([p["symbol"] for _l, p, _d in alarms])
            self.announce(alarms)
        self.fired = fired          # committed once the alarms are queued: a fault before this rings them again
        for lvl, p, d in alarms:
            self.journal("level", key=p["key"], level=lvl, distance=d, mark=p["mark"], liq=p["liq"])
        self.polls_ok += 1
        if self.blind:
            self.blind = False
            self.say("Сторож снова видит Binance: слеп был %d мин." % round((t - self.last_ok) / 60))
            self.journal("seen_again", blind_s=round(t - self.last_ok))
        self.last_ok = t
        ds = [d for d in (distance_pct(p) for p in pos) if d is not None]
        self.min_seen = min(ds) if ds else None
        return True

    def announce(self, alarms):
        top = max(lvl for lvl, _p, _d in alarms)
        title, body = alarm_text(alarms, self.mmr)
        if top >= 2:
            self.push(title, body + "\nПодтверди в Pushover, чтобы звонок затих.", 2)
        self.say(("🔴 " if top >= 2 else "⚠️ ") + title + "\n" + body, quiet=False)

    def check_blind(self):
        t = self.now()
        if t - self.last_ok >= BLIND_S and (not self.blind or t >= self.blind_next):
            first = not self.blind
            self.blind, self.blind_next = True, t + BLIND_REPEAT_S
            why = self.bn_error or "нет ответа"
            text = "Сторож не видит Binance %d мин: %s. Твои позиции сейчас без присмотра." % (
                round((t - self.last_ok) / 60), why)
            self.push("Сторож ослеп" if first else "Сторож всё ещё слеп", text, 1)
            self.say("🔴 " + text)
            self.journal("blind", since=utc(self.last_ok), error=why)

    def refresh_brackets(self, first=()):
        t = self.now()
        done = 0
        order = [p for s in first for p in self.positions if p["symbol"] == s]
        for p in order + [p for p in self.positions if p not in order]:
            s = p["symbol"]
            got = self.mmr.get(s)
            if got is not None and self.mmr.get(s + "@t", 0) > t - BRACKETS_S:
                continue
            if done >= 2:
                break
            done += 1
            try:
                b = bracket_for(self.bn.brackets(s), p["notional"])
            except Exception as e:
                self.err("brackets %s" % s, e)
                b = None
            self.mmr[s] = b[0] if b else None
            self.mmr[s + "@t"] = t

    def telegram(self):
        try:
            ups = self.tg.call("getUpdates", offset=self.tg_offset, timeout=0, allowed_updates=["message"])
        except Exception as e:
            self.err("telegram", e)
            return
        for u in ups:
            if isinstance(u.get("update_id"), int):
                self.tg_offset = max(self.tg_offset, u["update_id"] + 1)
            m = u.get("message") or {}
            if (m.get("chat") or {}).get("id") != self.chat:
                self.journal("foreign_chat")
                continue
            cmd, args = parse_command(m.get("text"))
            self.journal("command", cmd=cmd or "none")
            self.command(cmd, args)

    def command(self, cmd, args):
        if cmd == "status":
            self.say(self.status_text())
        elif cmd == "test":
            if self.test:
                self.say("Тест уже идёт — подтверди тревогу в Pushover.")
                return
            m = self.push("Сторож: проверка тревоги",
                          "Это тест. Нажми «Подтвердить» — и сторож напишет, что звонок дошёл.", 2, TEST_EXPIRE_S)
            if m is not None:
                m["test"] = True
                self.say("Тестовая тревога отправлена в Pushover. Подтверди её на телефоне.")
        elif cmd == "thresholds":
            if not args:
                self.say("Пороги: %s / %s / %s до ликвидации (сообщение / тревога / последний звонок). "
                         "Задать свои: «Пороги 5 3 1,5»." % tuple(pct(x) for x in self.th))
                return
            th = thresholds_of(args)
            if th is None:
                self.say("Не понял. Нужно три числа по убыванию, не больше 30: «Пороги 5 3 1,5».")
                return
            self.th = th
            self.fired = {p["key"]: frozenset(range(1, crossed(distance_pct(p), th) + 1))
                          for p in self.positions if distance_pct(p) is not None}
            self.journal("thresholds", th=list(th))
            self.save_state()
            self.say("Пороги заданы: %s / %s / %s." % tuple(pct(x) for x in th))
        else:
            self.say(HELP)

    def status_text(self):
        t = self.now()
        lines = ["Сторож: %s; последнее чтение Binance %d с назад; ключ %s; пороги %s / %s / %s; "
                 "страховка от падения сервера: %s." % (
                     "слеп" if self.blind else "на месте", round(t - self.last_ok),
                     "только чтение ✓" if self.key_ok else "не проверен" if self.key_ok is None else "НЕ только чтение",
                     pct(self.th[0]), pct(self.th[1]), pct(self.th[2]), "есть" if self.hc else "нет")]
        if not self.positions:
            lines.append("Открытых позиций нет.")
        for p in sorted(self.positions, key=lambda q: (distance_pct(q) is None, distance_pct(q) or 0)):
            lines.append("• " + position_line(p, distance_pct(p), self.mmr.get(p["symbol"])))
        return "\n".join(lines)

    def check_test(self):
        t = self.now()
        if not self.test or t < self.test["next"]:
            return
        self.test["next"] = t + RECEIPT_EVERY_S
        try:
            doc = self.po.receipt(self.test["receipt"])
        except Exception as e:
            self.err("receipt", e)
            doc = {}
        if doc.get("acknowledged") == 1:
            at = doc.get("acknowledged_at")
            self.say("Тест пройден: тревогу подтвердили%s. Звонок до тебя доходит." % (
                " в %s UTC" % utc(at)[11:19] if isinstance(at, int) else ""))
            self.journal("test", acknowledged=True, after_s=round(t - self.test["sent"]))
            self.test = None
        elif t >= self.test["deadline"]:
            try:
                self.po.cancel(self.test["receipt"])
            except Exception as e:
                self.err("cancel", e)
            self.say("Тест не подтверждён за %d мин. Проверь в Pushover: Настройки → Critical Alerts включены, "
                     "громкость не на нуле." % (TEST_WAIT_S // 60))
            self.journal("test", acknowledged=False)
            self.test = None

    def heartbeat(self):
        t = self.now()
        day = utc(t)[:10]
        h, m = HEARTBEAT_UTC
        now = dt.datetime.fromtimestamp(t, dt.timezone.utc)
        if self.hb_day != day and (now.hour, now.minute) >= (h, m):
            self.hb_day = day
            near = min(((distance_pct(p), p) for p in self.positions if distance_pct(p) is not None),
                       default=None, key=lambda x: x[0])
            self.say("Сторож на месте: позиций %d%s; ключ %s; пороги %s / %s / %s." % (
                len(self.positions),
                ", ближе всех к ликвидации %s — %s" % (near[1]["symbol"], pct(near[0])) if near else "",
                "только чтение ✓" if self.key_ok else "не проверен", pct(self.th[0]), pct(self.th[1]),
                pct(self.th[2])), quiet=True)
            self.journal("heartbeat")

    def sync(self):
        t = self.now()
        if t >= self.next_time:
            try:
                self.bn.sync_time()
                self.next_time = t + TIME_SYNC_S
            except Exception as e:
                self.err("time", e)
                self.next_time = t + PERM_RETRY_S

    def ping(self):
        t = self.now()
        if self.hc and t >= self.next_hc and t - self.last_ok < 2 * HC_S:
            self.next_hc = t + HC_S
            hc_ping(self.net, self.hc)

    def tick(self):
        t = self.now()
        if t >= self.next_tick:
            self.next_tick = t + TICK_S
            self.journal("tick", polls_ok=self.polls_ok, polls_err=self.polls_err, positions=len(self.positions),
                         min_distance=self.min_seen, blind=self.blind, outbox=len(self.outbox))
            d = os.path.join(self.var, "journal")
            cut = utc(t - KEEP_DAYS * 86400)[:10]
            for f in sorted(os.listdir(d)):
                if re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}\.jsonl", f) and f[:10] < cut:
                    os.unlink(os.path.join(d, f))
                    self.journal("pruned", file=f)
        if t >= self.next_state:
            self.save_state()

    def cycle(self):
        """One pass: the clock, the key's permissions, the positions, blindness, brackets, the chat, the test, the
        heartbeat, the outbox, the dead-man, the record, the watchdog. A step's fault is journaled and stops no
        other step; a key that can do more than read stops the guard."""
        if self.now() >= self.next_key:
            self.check_key()
        for name, f in (("sync", self.sync), ("poll", self.poll), ("blind", self.check_blind),
                        ("brackets", self.refresh_brackets), ("telegram", self.telegram), ("test", self.check_test),
                        ("heartbeat", self.heartbeat), ("flush", self.flush), ("dead-man", self.ping),
                        ("tick", self.tick)):
            try:
                f()
            except KeyRefused:
                raise
            except Exception as e:
                self.err(name, e)
        self.notify("WATCHDOG=1")


class KeyRefused(Exception):
    pass


# ---- the modes ----------------------------------------------------------------------------------------------------

class Tty:
    """The Boss's terminal, as TZ-51 corrected it: two streams, never "r+" (map section 7 item 189); a hidden answer
    read by getpass, which discards what was typed before it; a visible one discards it too."""

    def __init__(self, path="/dev/tty"):
        self.rh = open(path, "r", encoding="utf-8", errors="replace")
        self.fh = open(path, "w", encoding="utf-8", errors="replace")

    def say(self, text):
        self.fh.write(text + "\n")
        self.fh.flush()

    def ask(self, prompt, hidden=False):
        if hidden:
            return getpass.getpass(prompt, stream=self.fh)
        import termios
        termios.tcflush(self.rh.fileno(), termios.TCIFLUSH)
        self.fh.write(prompt)
        self.fh.flush()
        line = self.rh.readline()
        if line == "":
            raise EOFError("the terminal closed")
        return line.rstrip("\r\n")


def mode_secrets(tty=None, etc=ETC, uid=0):
    """The Boss's credentials onto the host, typed by him: each hidden, refused and asked again where it is not of
    its form, three times at most, written once by exclusive create, 0600; one already in place and of its form is
    kept. Printed: written, kept or skipped, and the bytes - never a value."""
    tty = tty or Tty()
    tty.say("Сторож · ТЗ-54: учётные данные. Ввод скрыт; ничего из введённого не попадает ни в журнал, ни в отчёт.")
    rc = 0
    for name, _form, required, prompt in CREDENTIALS:
        path = os.path.join(etc, name)
        if os.path.lexists(path):
            with open(path, encoding="utf-8") as fh:
                ok = FORM[name].fullmatch(fh.read().strip()) is not None
            assert ok and private_file_ok(path, uid=uid), "BLOCKED: %s: %s" % (path, file_state(path))
            out("SECRETS %s: kept" % name)
            continue
        v = None
        for _k in range(3):
            a = tty.ask(prompt, hidden=True).strip()
            if not a and not required:
                break
            if FORM[name].fullmatch(a):
                v = a
                break
            tty.say("Не похоже на %s. Ещё раз." % LABEL[name])
        if v is None:
            out("SECRETS %s: %s" % (name, "skipped" if not required else "not given in 3 tries"))
            rc = rc or (4 if required else 0)
            continue
        out("SECRETS %s: written, %d bytes" % (name, write_private(path, (v + "\n").encode(), uid)))
    tty.say("Готово." if rc == 0 else "Не всё введено — запустите ту же строку ещё раз.")
    return rc


def mode_find_chat(tg=None, etc=ETC, wait_s=FIND_CHAT_S, uid=0, now=time.time, sleep=time.sleep):
    """The one private chat that sent /start to the guard's bot, pinned to tg-chat by exclusive create; one already
    pinned is kept. Waits up to wait_s. Prints counts only, never a chat id."""
    path = os.path.join(etc, "tg-chat")
    if os.path.lexists(path):
        with open(path, encoding="utf-8") as fh:
            ok = FORM["tg-chat"].fullmatch(fh.read().strip()) is not None
        assert ok and private_file_ok(path, uid=uid), "BLOCKED: %s: %s" % (path, file_state(path))
        out("FIND-CHAT pinned already, kept")
        return 0
    if tg is None:
        creds, problems = read_credentials(etc, uid)
        assert "tg-token" in creds, "BLOCKED: tg-token: %s" % problems
        tg = Telegram(Net(timeout=LONG_POLL_S + 15), creds["tg-token"])
    deadline, offset, said = now() + wait_s, 0, False
    while True:
        try:
            ups = tg.call("getUpdates", offset=offset, timeout=min(LONG_POLL_S, max(0, int(deadline - now()))),
                          allowed_updates=["message"])
        except Exception as e:
            out("FIND-CHAT a poll failed: %s" % type(e).__name__)
            if now() >= deadline:
                return 4
            sleep(5)
            continue
        found = private_starts(ups)
        if len(found) == 1:
            break
        if len(found) > 1 or now() >= deadline:
            out("FIND-CHAT updates %d, private chats that sent /start: %d - FAIL" % (len(ups), len(found)))
            return 4
        if ups:
            offset = ups[-1]["update_id"] + 1
        if not said:
            out("FIND-CHAT no /start among %d updates; waiting up to %d s" % (len(ups), wait_s))
            said = True
    write_private(path, ("%d\n" % found[0]).encode(), uid)
    tg.send(found[0], "Сторож на связи. Чат закреплён — сюда будут приходить предупреждения.", quiet=False)
    out("FIND-CHAT updates %d, private chats that sent /start: 1, pinned" % len(ups))
    return 0


def see_text(pos):
    """What the guard sees, for the Boss to hold against his Binance app. Pure."""
    if not pos:
        return "Сторож не видит ни одной открытой позиции на фьючерсах USDⓈ-M."
    lines = ["Сторож видит открытых позиций: %d" % len(pos)]
    for p in sorted(pos, key=lambda q: (q["symbol"], q["side"])):
        lines.append("• " + position_line(p, distance_pct(p), None))
    return "\n".join(lines)


def answer_of(updates, chat):
    """The first yes or no from `chat` among Telegram updates: True, False or None. Pure."""
    for u in updates:
        m = u.get("message") if isinstance(u, dict) else None
        if not isinstance(m, dict) or (m.get("chat") or {}).get("id") != chat:
            continue
        t = (m.get("text") or "").strip().lower().strip(".!")
        if t in YES:
            return True
        if t in NO:
            return False
    return None


def mode_prove(net=None, etc=ETC, var=VAR, uid=0, now=time.time, sleep=time.sleep, code=None):
    """CANON hard rule 14: every request path the unit uses, through this file's own functions, served and parsed;
    the key read able to read and nothing else, and bound to an address; what it sees confirmed by the Boss in his
    chat as every open position he has; a test alarm sent at Pushover's emergency priority and acknowledged on his
    phone. Its record, prove.json, carries this code's SHA-256."""
    creds, problems = read_credentials(etc, uid)
    gates = []

    def gate(name, ok, detail):
        gates.append({"gate": name, "pass": bool(ok), "detail": detail})
        out("%s %s - %s" % (name, "PASS" if ok else "FAIL", detail))
        return ok
    if not gate("G-CRED", not problems, "%d credentials of their form, 0600, root's; the dead-man %s%s" % (
            len(creds), "set" if "hc-url" in creds else "not set", "; " + "; ".join(problems) if problems else "")):
        return 4
    scrub = Scrub(creds)
    net = net or Net(timeout=LONG_POLL_S + 15)
    bn = Binance(net, creds["binance-key"], creds["binance-secret"], now)
    po = Pushover(net, creds["pushover-token"], creds["pushover-user"])
    tg = Telegram(net, creds["tg-token"])

    def tried(name, f):
        try:
            return f(), None
        except Exception as e:
            return None, scrub("%s: %s" % (type(e).__name__, e))[:300]
    off, e = tried("time", bn.sync_time)
    gate("G-TIME", e is None and abs(off) < 2000, "Binance's clock less this host's: %s ms" % (off if e is None else e))
    doc, e = tried("key", bn.restrictions)
    ok, why = key_reading(doc) if e is None else (False, [e])
    gate("G-KEY", ok, (perms_line(doc) if e is None else "") + ("; refused: " + "; ".join(why) if why else ""))
    raw, e = tried("positions", bn.positions)
    pos = None
    if e is None:
        try:
            pos = parse_positions(raw)
        except AssertionError as x:
            e = scrub(x)
    gate("G-POS", e is None, ("%s served; open positions %d, with a liquidation price %d" % (
        bn.position_path, len(pos), sum(1 for p in pos if distance_pct(p) is not None))) if e is None else e)
    sym = pos[0]["symbol"] if pos else "BTCUSDT"
    br, e = tried("brackets", lambda: bn.brackets(sym))
    n = len((br[0] if isinstance(br, list) and br else br or {}).get("brackets") or []) if e is None else 0
    gate("G-BRACKET", e is None and n > 0, ("leverage brackets of one held symbol: %d" % n) if e is None else e)
    _v, e = tried("pushover", po.validate)
    gate("G-PUSH", e is None, "the user key and token validated" if e is None else e)
    me, e = tried("telegram", lambda: tg.call("getMe"))
    if e is None:
        _s, e = tried("telegram", lambda: tg.send(creds["tg-chat"], "Сторож · проверка связи (ТЗ-54)."))
    gate("G-TG", e is None, "getMe and one message to the pinned chat" if e is None else e)
    if all(g["pass"] for g in gates):
        chat = int(creds["tg-chat"])
        last, e = tried("telegram", lambda: tg.call("getUpdates", offset=-1, timeout=0, allowed_updates=["message"]))
        offset = (last[-1]["update_id"] + 1) if e is None and last else 0
        if e is None:
            _s, e = tried("telegram", lambda: tg.send(chat, see_text(pos) + "\n\nСовпадает с твоими позициями в "
                                                                       "Binance? Ответь «да» или «нет»."))
        said, t0 = None, now()
        while e is None and said is None and now() - t0 < SEE_WAIT_S:
            ups, e2 = tried("telegram", lambda: tg.call("getUpdates", offset=offset, timeout=LONG_POLL_S,
                                                        allowed_updates=["message"]))
            if e2 is not None:
                sleep(5)
                continue
            if ups:
                offset = ups[-1]["update_id"] + 1
            said = answer_of(ups, chat)
        gate("G-SEE", said is True, e or ("the Boss answered yes to the list of %d positions after %d s" % (
            len(pos), round(now() - t0)) if said is True else "the Boss answered no" if said is False
            else "no answer in %d s" % SEE_WAIT_S))
    if all(g["pass"] for g in gates):
        r, e = tried("alarm", lambda: po.send("Сторож: проверка тревоги (ТЗ-54)",
                                               "Нажми «Подтвердить» — так проверяется, что тревога будит тебя.", 2,
                                               TEST_EXPIRE_S))
        acked, waited = False, 0
        if e is None:
            tried("telegram", lambda: tg.send(creds["tg-chat"], "Сейчас зазвонит Pushover — нажми «Подтвердить»."))
            t0 = now()
            while now() - t0 < TEST_WAIT_S:
                sleep(RECEIPT_EVERY_S)
                d, e2 = tried("receipt", lambda: po.receipt(r))
                if e2 is None and d.get("acknowledged") == 1:
                    acked = True
                    break
            waited = round(now() - t0)
            if not acked:
                tried("cancel", lambda: po.cancel(r))
        gate("G-ALARM", acked, ("acknowledged after %d s" % waited) if acked else (e or "not acknowledged in %d s" % TEST_WAIT_S))
    if all(g["pass"] for g in gates):
        if "hc-url" in creds:
            _h, e = tried("dead-man", lambda: hc_ping(net, creds["hc-url"]))
            gate("G-HC", e is None, "the dead-man's ping answered OK" if e is None else e)
        else:
            gate("G-HC", True, "not set - no ping")
    passed = all(g["pass"] for g in gates) and [g["gate"] for g in gates] == list(PROVE_GATES)
    code = code or sha256_file(os.path.abspath(__file__))
    rec = {"at": utc(now()), "code_sha256": code, "pass": passed, "gates": gates,
           "requests": {h: c for h, c in sorted(net.count.items())} if hasattr(net, "count") else {}}
    replace_private(os.path.join(var, "prove.json"), (json.dumps(rec, sort_keys=True, ensure_ascii=False) + "\n").encode(),
                    uid)
    out("PROVE %s: %d gates of %d passed; requests %s" % ("PASS" if passed else "FAIL",
                                                          sum(g["pass"] for g in gates), len(gates), rec["requests"]))
    return 0 if passed else 4


def mode_status(var=VAR):
    """The guard's own state from its files: counts, states and instants - no symbol, price, size or margin."""
    path = os.path.join(var, "state.json")
    if not os.path.exists(path):
        out("STATUS no state.json")
        return 4
    with open(path, encoding="utf-8") as fh:
        st = json.load(fh)
    keys = ("at", "started", "last_ok", "polls_ok", "polls_err", "positions", "with_liquidation", "blind", "key_ok",
            "key_checked", "dead_man", "outbox", "disk_faults", "thresholds", "pid")
    out("STATUS " + "; ".join("%s %s" % (k, st.get(k)) for k in keys))
    jd = os.path.join(var, "journal")
    files = sorted(os.listdir(jd)) if os.path.isdir(jd) else []
    evs = {}
    for f in files[-2:]:
        with open(os.path.join(jd, f), encoding="utf-8") as fh:
            for ln in fh:
                e = json.loads(ln).get("ev")
                evs[e] = evs.get(e, 0) + 1
    out("STATUS journal files %d; events in the last two: %s" % (len(files), dict(sorted(evs.items()))))
    return 0


def host_addresses():
    """This host's global IPv4 addresses, as `ip -4 -o addr show scope global` lists them."""
    import subprocess
    r = subprocess.run(["ip", "-4", "-o", "addr", "show", "scope", "global"], capture_output=True, text=True,
                       timeout=20)
    assert r.returncode == 0, "ip: exit %d" % r.returncode
    return sorted(set(re.findall(r"inet ((?:[0-9]{1,3}\.){3}[0-9]{1,3})/", r.stdout)))


def scan_counts(blob, needles):
    """{label: occurrences} of each needle in blob, a number matched whole. Pure."""
    found = {}
    for label, v in needles:
        pat = re.escape(v.encode())
        if v.isdigit() or IPV4.fullmatch(v):
            pat = rb"(?<![0-9.])" + pat + rb"(?![0-9])"
        found[label] = len(re.findall(pat, blob))
    return found


def mode_scan(paths, etc=ETC, uid=0, addresses=None):
    """G-PRINT: every given file read whole for every credential, the chat id and this host's own IPv4 addresses.
    Prints counts per file - never a value; exit 4 where any count is above zero."""
    creds, problems = read_credentials(etc, uid)
    needles = [(k, v) for k, v in sorted(creds.items())]
    addrs = host_addresses() if addresses is None else addresses
    needles += [("host-ipv4-%d" % i, a) for i, a in enumerate(addrs, 1)]
    assert paths, "scan takes files"
    total = 0
    for path in paths:
        with open(path, "rb") as fh:
            found = scan_counts(fh.read(), needles)
        n = sum(found.values())
        total += n
        out("SCAN %s: %d bytes, %s" % (path, os.path.getsize(path), "nothing found" if n == 0 else
                                       ", ".join("%s %d" % (k, c) for k, c in sorted(found.items()) if c)))
    out("G-PRINT %s: %d files, %d values sought - credentials %d, the host's IPv4 addresses %d; found %d" % (
        "PASS" if total == 0 else "FAIL", len(paths), len(needles), len(creds), len(addrs), total))
    return 0 if total == 0 else 4


def mode_serve(etc=ETC, var=VAR):
    creds, problems = read_credentials(etc)
    if problems:
        out("SERVE refused: %s" % "; ".join(problems))
        return 2
    g = Guard(creds, var=var)
    stop = []
    signal.signal(signal.SIGTERM, lambda *_a: stop.append(1))
    g.journal("start", code=sha256_file(os.path.abspath(__file__)), thresholds=list(g.th), dead_man=bool(g.hc))
    try:
        g.check_key()
    except KeyRefused as e:
        return refuse(g, e)
    g.poll()
    g.say("Сторож запущен: позиций %d; пороги %s / %s / %s; ключ %s." % (
        len(g.positions), pct(g.th[0]), pct(g.th[1]), pct(g.th[2]),
        "только чтение ✓" if g.key_ok else "ещё не проверен"), quiet=True)
    g.flush()
    g.save_state()
    g.notify("READY=1")
    out("SERVE start: key %s, positions read %s" % (g.key_ok, g.polls_ok))
    while not stop:
        t0 = time.monotonic()
        try:
            g.cycle()
        except KeyRefused as e:
            return refuse(g, e)
        except Exception as e:
            g.err("cycle", e)
        while not stop and time.monotonic() - t0 < POLL_S:
            time.sleep(min(1.0, max(0.0, POLL_S - (time.monotonic() - t0))))
    g.journal("stop", polls_ok=g.polls_ok, polls_err=g.polls_err)
    g.save_state()
    out("SERVE stop on SIGTERM")
    return 0


def refuse(g, e):
    text = "Сторож остановлен: ключ Binance может больше, чем читать (%s). Создай ключ только с «Enable Reading» и " \
           "привязкой к IP сервера." % "; ".join(e.args[0])
    for f in (lambda: g.po.send("Сторож остановлен", text, 1), lambda: g.tg.send(g.chat, "🔴 " + text)):
        try:
            f()
        except Exception as x:
            g.err("refuse", x)
    g.journal("refused", problems=e.args[0])
    g.save_state()
    out("SERVE refused: the key can do more than read: %s" % "; ".join(e.args[0]))
    return 2


# ---- the self-test: stand-ins for Binance, Pushover, Telegram and healthchecks ----------------------------------

class FakeNet:
    """Binance, Pushover, Telegram and healthchecks.io as dictionaries; every request recorded."""

    def __init__(self, key, secret, positions=(), perms=None):
        self.key, self.secret, self.log, self.count = key, secret, [], {}
        self.positions, self.down = list(positions), set()
        self.perms = perms if perms is not None else {"ipRestrict": True, "enableReading": True,
                                                     "enableWithdrawals": False, "enableInternalTransfer": False,
                                                     "enableMargin": False, "enableFutures": False,
                                                     "permitsUniversalTransfer": False, "enableVanillaOptions": False,
                                                     "enableFixApiTrade": False, "enableFixReadOnly": True,
                                                     "enableSpotAndMarginTrading": False,
                                                     "enablePortfolioMarginTrading": False, "createTime": 1}
        self.pushes, self.receipts, self.tg_sent, self.updates, self.v3 = [], {}, [], [], True
        self.answer = "Да"
        self.now = time.time

    def call(self, host, method, path, body=None, headers=()):
        h = dict(headers)
        self.log.append((host, method, path.split("?")[0]))
        self.count[host] = self.count.get(host, 0) + 1
        if host in self.down:
            raise ConnectionResetError("down")
        u = urllib.parse.urlsplit(path)
        q = urllib.parse.parse_qs(u.query)
        if host in (FAPI, SAPI):
            if u.path == "/fapi/v1/time":
                return 200, json.dumps({"serverTime": int(self.now() * 1000)}).encode()
            assert h.get("X-MBX-APIKEY") == self.key, "a signed request without the key"
            raw, sig = u.query.rsplit("&signature=", 1)
            want = hmac.new(self.secret.encode(), raw.encode(), hashlib.sha256).hexdigest()
            if sig != want:
                return 400, b'{"code":-1022,"msg":"Signature for this request is not valid."}'
            if host == SAPI and u.path == "/sapi/v1/account/apiRestrictions":
                return 200, json.dumps(self.perms).encode()
            if host == FAPI and u.path in POSITION_PATHS:
                if u.path.startswith("/fapi/v3") and not self.v3:
                    return 404, b"<html>404</html>"
                return 200, json.dumps(self.positions).encode()
            if host == FAPI and u.path == "/fapi/v1/leverageBracket":
                return 200, json.dumps({"symbol": q["symbol"][0], "brackets": [
                    {"bracket": 1, "notionalFloor": 0, "notionalCap": 50000, "maintMarginRatio": 0.01, "cum": 0},
                    {"bracket": 2, "notionalFloor": 50000, "notionalCap": 250000, "maintMarginRatio": 0.02,
                     "cum": 500}]}).encode()
            return 404, b"{}"
        if host == PUSHOVER:
            if method == "POST":
                f = urllib.parse.parse_qs(body.decode())
                if u.path == "/1/users/validate.json":
                    return 200, b'{"status":1,"devices":["iphone"]}'
                if u.path == "/1/messages.json":
                    r = "r%029d" % len(self.pushes) if f["priority"][0] == "2" else None
                    self.pushes.append({k: v[0] for k, v in f.items()})
                    if r:
                        self.receipts[r] = {"status": 1, "acknowledged": 0}
                    return 200, json.dumps({"status": 1, "request": "x", **({"receipt": r} if r else {})}).encode()
                m = re.fullmatch(r"/1/receipts/(\w+)/cancel\.json", u.path)
                if m:
                    self.receipts[m.group(1)]["cancelled"] = True
                    return 200, b'{"status":1}'
            m = re.fullmatch(r"/1/receipts/(\w+)\.json", u.path)
            if m and m.group(1) in self.receipts:
                return 200, json.dumps(self.receipts[m.group(1)]).encode()
            return 400, b'{"status":0,"errors":["bad"]}'
        if host == TG:
            meth = u.path.rsplit("/", 1)[1]
            p = json.loads(body.decode())
            if meth == "getMe":
                return 200, b'{"ok":true,"result":{"id":1,"is_bot":true}}'
            if meth == "sendMessage":
                self.tg_sent.append(p)
                if "Совпадает" in p["text"] and self.answer is not None:
                    n = max([x["update_id"] for x in self.updates] or [0]) + 1
                    self.updates.append({"update_id": n, "message": {"text": self.answer,
                                                                    "chat": {"id": p["chat_id"], "type": "private"}}})
                return 200, b'{"ok":true,"result":{"message_id":1}}'
            if meth == "getUpdates":
                off = p.get("offset", 0)          # as Telegram: an offset confirms, and forgets, what is before it
                self.updates = self.updates[off:] if off < 0 else [x for x in self.updates if x["update_id"] >= off]
                return 200, json.dumps({"ok": True, "result": self.updates}).encode()
            return 404, b'{"ok":false,"description":"Not Found"}'
        if host == HC:
            return 200, b"OK"
        raise AssertionError("an unknown host %s" % host)


def binance_lp(side, qty, entry, wallet, mmr, cum):
    """Binance's liquidation price of a one-way isolated position, for the self-test's arithmetic."""
    s = 1 if side == "LONG" else -1
    return (wallet + cum - s * qty * entry) / (qty * mmr - s * qty)


def on_terminal(child, script, timeout=60):
    """child() in a child process whose controlling terminal is a new pseudo-terminal, as sshd gives `ssh -t`, and
    whose standard output and error are a pipe. `script`: (what the screen shows, what is typed), each typed once the
    screen shows its text after the last line typed. Returns (exit status, screen, log, lines left untyped)."""
    import codecs
    import fcntl
    import select
    import termios
    assert threading.active_count() == 1
    sys.stdout.flush()
    sys.stderr.flush()
    master, slave = os.openpty()
    rlog, wlog = os.pipe()
    pid = os.fork()
    if pid == 0:
        rc = 70
        try:
            os.close(master)
            os.close(rlog)
            os.setsid()
            fcntl.ioctl(slave, termios.TIOCSCTTY, 0)
            os.dup2(slave, 0)
            os.dup2(wlog, 1)
            os.dup2(wlog, 2)
            os.close(slave)
            os.close(wlog)
            rc = child()
        except BaseException:
            import traceback
            traceback.print_exc()
            rc = 71
        finally:
            try:
                sys.stdout.flush()
                sys.stderr.flush()
            finally:
                os._exit(rc if isinstance(rc, int) else 72)
    os.close(slave)
    os.close(wlog)
    dec = codecs.getincrementaldecoder("utf-8")("replace")
    screen, log, pending, mark = "", b"", list(script), 0
    fds, deadline = [master, rlog], time.monotonic() + timeout
    try:
        while fds:
            if time.monotonic() > deadline:
                os.kill(pid, signal.SIGKILL)
                break
            ready, _w, _x = select.select(fds, [], [], 0.2)
            for fd in ready:
                try:
                    data = os.read(fd, 65536)
                except OSError:
                    data = b""
                if not data:
                    fds.remove(fd)
                elif fd == master:
                    screen += dec.decode(data)
                else:
                    log += data
            if pending and pending[0][0] in screen[mark:]:
                mark = screen.index(pending[0][0], mark) + len(pending[0][0])
                os.write(master, (pending.pop(0)[1] + "\n").encode())
    finally:
        os.close(master)
        os.close(rlog)
        status = os.waitpid(pid, 0)[1]
    return os.waitstatus_to_exitcode(status), screen, log.decode("utf-8", "replace"), pending


def mode_selftest():
    import shutil
    import tempfile
    n = [0]

    def check(cond, what):
        n[0] += 1
        assert cond, "SELFTEST FAIL: " + what

    root = tempfile.mkdtemp(prefix="liq-guard-selftest-")
    uid = os.getuid()
    try:
        # -- arithmetic: the margin hint against Binance's own liquidation formula --------------------------------
        for side, qty, entry, wallet, mmr, cum, mark in (("SHORT", 25.0, 1787.0, 4100.0, 0.01, 0.0, 1900.0),
                                                        ("LONG", 0.5, 97000.0, 3000.0, 0.004, 0.0, 92000.0),
                                                        ("SHORT", 1200.0, 2.31, 180.0, 0.025, 12.5, 2.40)):
            lp = binance_lp(side, qty, entry, wallet, mmr, cum)
            p = {"side": side, "qty": qty, "mark": mark, "liq": lp, "isolated": True}
            need = margin_hint(p, mmr, 8.0)
            lp2 = binance_lp(side, qty, entry, wallet + need, mmr, cum)
            d2 = distance_pct({"side": side, "mark": mark, "liq": lp2})
            check(need > 0 and abs(d2 - 8.0) < 1e-9, "the margin hint moves %s's liquidation to 8%%: %r" % (side, d2))
            check(margin_hint(dict(p, liq=binance_lp(side, qty, entry, wallet + need + 100, mmr, cum)), mmr) == 0.0,
                  "no hint where the liquidation is beyond the target")
        check(abs(distance_pct({"side": "SHORT", "mark": 100.0, "liq": 103.0}) - 3.0) < 1e-12, "a short's distance")
        check(abs(distance_pct({"side": "LONG", "mark": 100.0, "liq": 97.0}) - 3.0) < 1e-12, "a long's distance")
        check(distance_pct({"side": "LONG", "mark": 100.0, "liq": 0.0}) is None, "no liquidation price, no distance")
        # -- levels: announce once a descent, the highest of a jump, re-arm above threshold + 1 -------------------
        th, f, seq = (5.0, 3.0, 1.5), frozenset(), []
        for d in (6.0, 4.9, 4.5, 2.9, 2.8, 1.4, 1.0, 2.6, 1.4, 8.0, 0.9, None, 4.0):
            lvl, f = step(f, d, th)
            seq.append(lvl)
        check(seq == [0, 1, 0, 2, 0, 3, 0, 0, 3, 0, 3, 0, 1], "the levels announced: %r" % seq)
        check(step(frozenset({1}), 5.5, th)[1] == frozenset({1}) and step(frozenset({1}), 6.01, th)[1] == frozenset(),
              "hysteresis of one point")
        # -- positions, brackets, the key's permissions, commands ----------------------------------------------------
        raw = [{"symbol": "YFIUSDT", "positionSide": "BOTH", "positionAmt": "-25.000", "markPrice": "1596.20",
                "liquidationPrice": "1700.00", "notional": "-39905.0", "isolatedWallet": "4100.0"},
               {"symbol": "BTCUSDT", "positionSide": "LONG", "positionAmt": "0.500", "markPrice": "92000",
                "liquidationPrice": "0", "notional": "46000", "isolatedWallet": "0"},
               {"symbol": "ETHUSDT", "positionSide": "BOTH", "positionAmt": "0.000", "markPrice": "3000",
                "liquidationPrice": "0"}]
        ps = parse_positions(raw)
        check([(p["symbol"], p["side"], p["isolated"]) for p in ps] == [("YFIUSDT", "SHORT", True),
                                                                        ("BTCUSDT", "LONG", False)], "positions: %r" % ps)
        br = {"brackets": [{"notionalFloor": 50000, "notionalCap": 250000, "maintMarginRatio": 0.02, "cum": 500},
                           {"notionalFloor": 0, "notionalCap": 50000, "maintMarginRatio": 0.01, "cum": 0}]}
        check(bracket_for(br, 39905.0) == (0.01, 0.0) and bracket_for([br], 60000) == (0.02, 500.0)
              and bracket_for(br, 9e9) is None, "brackets")
        good = FakeNet("k" * 64, "s" * 64).perms
        check(key_reading(good) == (True, []), "a read-only, bound key")
        for k in ("enableFutures", "enableWithdrawals", "enableSpotAndMarginTrading", "permitsUniversalTransfer",
                  "enableSomethingNew"):
            check(key_reading(dict(good, **{k: True}))[0] is False, "refused: %s" % k)
        check(key_reading(dict(good, ipRestrict=False))[0] is False, "refused: no address")
        check(key_reading({k: v for k, v in good.items() if k != "enableFutures"})[0] is False, "refused: absent field")
        check(parse_command("/status@SomeBot") == ("status", []) and parse_command("Пороги 5 3 1,5")
              == ("thresholds", ["5", "3", "1,5"]) and parse_command("  ТЕСТ ") == ("test", []), "commands")
        check(thresholds_of(["5", "3", "1,5"]) == (5.0, 3.0, 1.5) and thresholds_of(["3", "5", "1"]) is None
              and thresholds_of(["40", "3", "1"]) is None and thresholds_of(["5", "3"]) is None, "thresholds")
        check(price(1596.2) == "1 596,2" and price(0.00012346) == "0,0001235" and pct(2.94) == "2,9%",
              "notation: %r %r" % (price(1596.2), price(0.00012346)))
        sc = Scrub({"binance-key": "A" * 64, "tg-chat": "123"})
        check(sc("key %s from 203.0.113.9" % ("A" * 64)) == "key *** from x.x.x.x", "scrub")
        # -- IPv4 alone ----------------------------------------------------------------------------------------------
        seen = []

        def fake_gai(host, port, family=0, type=0, *a):
            seen.append(family)
            raise OSError("stop")
        real_gai, socket.getaddrinfo = socket.getaddrinfo, fake_gai
        try:
            try:
                V4HTTPS("example.invalid", 443, timeout=1, context=ssl.create_default_context()).connect()
            except OSError:
                pass
        finally:
            socket.getaddrinfo = real_gai
        check(seen == [socket.AF_INET], "every connect resolves IPv4 alone: %r" % seen)
        tick = [100.0]
        net = Net(timeout=1, clock=lambda: tick[0])
        calls = []

        def timing_out(*a, **k):
            calls.append(1)
            raise TimeoutError("timed out")
        net._call = timing_out
        for _k in range(3):
            try:
                net.call(FAPI, "GET", "/x")
            except OSError:
                pass
        tick[0] += COOLDOWN_S
        try:
            net.call(FAPI, "GET", "/x")
        except OSError:
            pass
        check(len(calls) == 2, "a failed host waits out its cooldown: %d tries" % len(calls))
        # -- secrets at a real terminal ------------------------------------------------------------------------------
        etc = os.path.join(root, "etc")
        vals = {"binance-key": "K" * 64, "binance-secret": "S" * 64, "pushover-user": "u" * 30,
                "pushover-token": "a" * 30, "tg-token": "123456789:" + "T" * 35}
        script = [("API Key", "not-a-key"), ("API Key", vals["binance-key"]), ("Secret Key", vals["binance-secret"]),
                  ("User Key", vals["pushover-user"]), ("API Token", vals["pushover-token"]),
                  ("BotFather", vals["tg-token"]), ("hc-ping.com", "")]
        rc, screen, log, left = on_terminal(lambda: mode_secrets(etc=etc, uid=uid), script)
        check(rc == 0 and not left, "secrets at a real terminal: rc %s, left %d, log %r" % (rc, len(left), log[-300:]))
        check(all(v not in screen + log for v in vals.values()), "no value echoed or logged")
        check(sorted(os.listdir(etc)) == sorted(vals) and all(private_file_ok(os.path.join(etc, k), uid=uid)
                                                              for k in vals), "five files, 0600")
        check("hc-url: skipped" in log and "written, 65 bytes" in log, "the log: written and skipped")
        rc2, _s, log2, _l = on_terminal(lambda: mode_secrets(etc=etc, uid=uid), [("hc-ping.com", "")])
        check(rc2 == 0 and log2.count(": kept") == 5 and "hc-url: skipped" in log2,
              "a second run keeps them and asks for the optional one again: %r" % log2[-200:])
        # -- find-chat -----------------------------------------------------------------------------------------------
        fn = FakeNet(vals["binance-key"], vals["binance-secret"])
        fn.updates = [{"update_id": 7, "message": {"text": "/start", "chat": {"id": 4242, "type": "private"}}}]
        check(mode_find_chat(Telegram(fn, vals["tg-token"]), etc, 5, uid) == 0, "find-chat pins one chat")
        creds, problems = read_credentials(etc, uid)
        check(problems == [] and creds["tg-chat"] == "4242", "credentials read: %r" % problems)
        # -- prove ---------------------------------------------------------------------------------------------------
        clock = [1.8e9]
        var = os.path.join(root, "var")

        def ack_later(_s):
            clock[0] += _s
            for r in fn.receipts.values():
                r["acknowledged"], r["acknowledged_at"] = 1, int(clock[0])
        fn.positions, fn.now = raw, (lambda: clock[0])
        check(mode_prove(fn, etc, var, uid, lambda: clock[0], ack_later, code="c" * 64) == 0, "prove passes")
        rec = json.load(open(os.path.join(var, "prove.json")))
        check(rec["pass"] is True and [g["gate"] for g in rec["gates"]] == list(PROVE_GATES), "prove's ten gates")
        write_private(os.path.join(etc, "hc-url"), b"https://hc-ping.com/0f0e0d0c-0b0a-4908-8706-050403020100\n", uid)
        n_hc = fn.count.get(HC, 0)
        check(mode_prove(fn, etc, var, uid, lambda: clock[0], ack_later, code="c" * 64) == 0
              and json.load(open(os.path.join(var, "prove.json")))["gates"][-1]["detail"] == "the dead-man's ping answered OK"
              and fn.count.get(HC, 0) == n_hc + 1, "the dead-man pinged once, last, after the Boss's answers")
        check(any("YFIUSDT шорт" in m["text"] and "Совпадает" in m["text"] for m in fn.tg_sent), "the list shown")
        fn.answer = "нет"
        check(mode_prove(fn, etc, var, uid, lambda: clock[0], ack_later, code="c" * 64) == 4,
              "prove fails where the Boss answers no")
        check(json.load(open(os.path.join(var, "prove.json")))["gates"][-1]["gate"] == "G-SEE", "no alarm after a no")
        fn.answer = "да"
        check(fn.pushes[-1]["priority"] == "2" and fn.pushes[-1]["expire"] == str(TEST_EXPIRE_S), "a test alarm")
        fn.perms = dict(fn.perms, enableFutures=True)
        check(mode_prove(fn, etc, var, uid, lambda: clock[0], ack_later, code="c" * 64) == 4,
              "prove refuses a key that can trade")
        fn.perms["enableFutures"] = False
        fn.v3 = False
        bn = Binance(fn, vals["binance-key"], vals["binance-secret"], lambda: clock[0])
        check(bn.positions() == raw and bn.position_path == "/fapi/v2/positionRisk", "v2 where v3 is not served")
        fn.v3 = True
        # -- the guard's cycle -----------------------------------------------------------------------------------------
        notes = []
        g = Guard(creds, net=fn, now=lambda: clock[0], var=var, uid=uid, notify=notes.append)
        fn.positions = [dict(raw[0], liquidationPrice="1700.00")]
        n_push, n_tg = len(fn.pushes), len(fn.tg_sent)
        g.cycle()
        check(g.key_ok is True and g.polls_ok == 1 and len(fn.pushes) == n_push and len(fn.tg_sent) == n_tg + 1
              and HELP[:20] in fn.tg_sent[-1]["text"], "first cycle: 6.5%% from liquidation, nothing rings; the "
              "pending /start answered with the help")
        base_push = len(fn.pushes)
        for liq, want_push in (("1670.0", 0), ("1640.0", 1), ("1630.0", 0), ("1615.0", 1)):
            clock[0] += 5
            fn.positions = [dict(raw[0], liquidationPrice=liq)]
            g.cycle()
            check(len(fn.pushes) - base_push == want_push, "liq %s: pushes %d" % (liq, len(fn.pushes) - base_push))
            base_push = len(fn.pushes)
        alarm = fn.pushes[-1]
        check(alarm["priority"] == "2" and alarm["retry"] == "30" and "ПОСЛЕДНИЙ ЗВОНОК" in alarm["title"]
              and "долить" in alarm["message"] and "4242" not in alarm["message"], "the second alarm: %r" % alarm)
        check(any("до ликвидации" in m["text"] for m in fn.tg_sent), "Telegram carries the warning")
        # margin added: re-armed, then a new descent alarms again
        clock[0] += 5
        fn.positions = [dict(raw[0], liquidationPrice="1800.0")]
        g.cycle()
        check(g.fired.get("YFIUSDT:SHORT") == frozenset(), "re-armed after margin")
        clock[0] += 5
        fn.positions = [dict(raw[0], liquidationPrice="1640.0")]
        n0 = len(fn.pushes)
        g.cycle()
        check(len(fn.pushes) == n0 + 1, "a new descent alarms again")
        # commands: status, thresholds, test acknowledged; a foreign chat ignored
        sent0 = len(fn.tg_sent)
        fn.updates = [{"update_id": 20, "message": {"text": "Статус", "chat": {"id": 4242, "type": "private"}}},
                      {"update_id": 21, "message": {"text": "Пороги 6 4 2", "chat": {"id": 4242, "type": "private"}}},
                      {"update_id": 22, "message": {"text": "Пороги 9 8 7", "chat": {"id": 9999, "type": "private"}}},
                      {"update_id": 23, "message": {"text": "Тест", "chat": {"id": 4242, "type": "private"}}}]
        clock[0] += 5
        g.cycle()
        texts = [m["text"] for m in fn.tg_sent[sent0:]]
        check(g.th == (6.0, 4.0, 2.0) and g.tg_offset == 24 and all(m["chat_id"] == 4242 for m in fn.tg_sent),
              "commands from the pinned chat alone: %r" % (g.th,))
        check(any(t.startswith("Сторож: на месте") for t in texts) and any("Пороги заданы" in t for t in texts),
              "status and thresholds answered: %r" % texts)
        check(g.test is not None and fn.pushes[-1]["expire"] == str(TEST_EXPIRE_S), "the test alarm sent")
        rid = g.test["receipt"]
        n2 = sum(1 for x in fn.pushes if x["priority"] == "2")
        fn.receipts[rid].update(acknowledged=1, acknowledged_at=int(clock[0]))
        fn.updates = []
        clock[0] += RECEIPT_EVERY_S
        g.cycle()
        check(g.test is None and any("Тест пройден" in m["text"] for m in fn.tg_sent), "the test acknowledged")
        check(json.load(open(os.path.join(var, "state.json")))["thresholds"] == [6.0, 4.0, 2.0], "thresholds kept")
        check(sum(1 for x in fn.pushes if x["priority"] == "2") == n2
              and g.fired.get("YFIUSDT:SHORT") == frozenset({1, 2}), "new thresholds ring nothing at once")
        # Binance's rate refusal: no request until its back-off has passed
        real_call = fn.call

        def limited(host, *a, **k):
            if host == FAPI and a[1].startswith("/fapi/v3/positionRisk"):
                return 429, b'{"code":-1003,"msg":"Too many requests"}'
            return real_call(host, *a, **k)
        fn.call = limited
        clock[0] += 5
        g.cycle()
        n_req = sum(1 for h, _m, pth in fn.log if pth.startswith("/fapi/v3/positionRisk"))
        clock[0] += 5
        g.cycle()
        check(sum(1 for h, _m, pth in fn.log if pth.startswith("/fapi/v3/positionRisk")) == n_req
              and g.bn_backoff > clock[0], "a 429 holds the reads back")
        fn.call = real_call
        clock[0] += 60
        g.cycle()
        check(g.polls_ok > 0 and g.bn_backoff <= clock[0], "reads resume after the back-off")
        # blindness: two minutes without a read alarm once, then a reminder after 30 minutes, then seen again
        fn.down.add(FAPI)
        n0 = len(fn.pushes)
        g.heartbeat = lambda: 1 / 0
        for _k in range(30):
            clock[0] += 5
            g.cycle()
        check(g.blind and len(fn.pushes) == n0 + 1 and fn.pushes[-1]["priority"] == "1", "blind once")
        check("Сторож не видит Binance" in fn.pushes[-1]["message"] and "positions" in fn.pushes[-1]["message"],
              "the blind alarm names Binance's own error")
        del g.heartbeat
        check(any(json.loads(ln).get("where") == "heartbeat" for f in os.listdir(os.path.join(var, "journal"))
                  for ln in open(os.path.join(var, "journal", f), encoding="utf-8")), "the failing step journaled")
        clock[0] += BLIND_REPEAT_S
        g.cycle()
        check(len(fn.pushes) == n0 + 2, "blind, reminded")
        fn.down.discard(FAPI)
        clock[0] += 5
        g.cycle()
        check(not g.blind and any("снова видит" in m["text"] for m in fn.tg_sent), "seen again")
        # a disk that refuses every write: the alarm still goes, the fault is counted
        real_open, faults0 = os.open, g.disk_faults

        def no_room(path, *a, **k):
            if str(path).startswith(var):
                raise OSError(28, "No space left on device")
            return real_open(path, *a, **k)
        os.open = no_room
        try:
            fn.positions = [dict(raw[0], liquidationPrice="1800.0")]
            clock[0] += 5
            g.cycle()
            n0 = len(fn.pushes)
            fn.positions = [dict(raw[0], liquidationPrice="1625.0")]
            clock[0] += STATE_S
            g.cycle()
        finally:
            os.open = real_open
        check(len(fn.pushes) == n0 + 1 and g.disk_faults > faults0, "a full disk stops no alarm")
        # Pushover down: the alarm waits in the outbox, then goes
        fn.down.add(PUSHOVER)
        fn.positions = [dict(raw[0], liquidationPrice="1800.0")]
        clock[0] += 5
        g.cycle()
        fn.positions = [dict(raw[0], liquidationPrice="1620.0")]
        clock[0] += 5
        g.cycle()
        check(any(m["to"] == "push" for m in g.outbox), "an alarm kept while Pushover is down")
        fn.down.discard(PUSHOVER)
        n0 = len(fn.pushes)
        clock[0] += 5
        g.cycle()
        check(len(fn.pushes) == n0 + 1 and not any(m["to"] == "push" for m in g.outbox), "sent once it is up")
        # Telegram down: one try a pass, the alarm channel still served, the queue bounded
        fn.down.add(TG)
        tries0 = sum(1 for h, _m, _p in fn.log if h == TG)
        for k in range(OUTBOX_MAX + 5):
            g.say("m%d" % k)
        clock[0] += 5
        g.cycle()
        check(sum(1 for h, _m, _p in fn.log if h == TG) - tries0 == 2, "Telegram tried once for the outbox and once "
              "for its updates")
        check(len([m for m in g.outbox if m["to"] == "tg"]) == OUTBOX_MAX, "the queue bounded")
        fn.down.discard(TG)
        sent0 = len(fn.tg_sent)
        clock[0] += 5
        g.cycle()
        check(len(fn.tg_sent) - sent0 == TG_PER_PASS, "at most %d Telegram messages a pass" % TG_PER_PASS)
        for _k in range(30):
            clock[0] += 5
            g.cycle()
        check(not g.outbox, "the queue sent, five a pass, once Telegram is up")
        # the heartbeat at 19:00 UTC, once a day, quiet
        day0 = dt.datetime(2027, 1, 5, 18, 59, 0, tzinfo=dt.timezone.utc).timestamp()
        clock[0] = day0
        g.last_ok = clock[0]
        g.cycle()
        clock[0] = day0 + 120
        g.cycle()
        clock[0] = day0 + 600
        g.cycle()
        old = os.path.join(var, "journal", "2026-09-01.jsonl")
        open(old, "w").close()
        os.chmod(old, 0o600)
        g.next_tick = 0
        g.cycle()
        check(not os.path.exists(old), "a journal file older than %d days removed" % KEEP_DAYS)
        hb = [m for m in fn.tg_sent if m["text"].startswith("Сторож на месте")]
        check(len(hb) == 1 and hb[0]["disable_notification"] is True, "one quiet heartbeat: %d" % len(hb))
        # a key widened at a later check: refused
        fn.perms = dict(fn.perms, enableSpotAndMarginTrading=True)
        g.next_key = 0
        try:
            g.cycle()
            refused = False
        except KeyRefused:
            refused = True
        check(refused, "a key widened later is refused")
        # the record: 0600 files, no secret in any of them, no chat id
        jd = os.path.join(var, "journal")
        blob = b"".join(open(os.path.join(jd, f), "rb").read() for f in os.listdir(jd))
        blob += open(os.path.join(var, "state.json"), "rb").read() + open(os.path.join(var, "prove.json"), "rb").read()
        check(all(v.encode() not in blob for v in vals.values()) and b"4242" not in blob, "no secret in the record")
        check(all(private_file_ok(os.path.join(jd, f), uid=uid) for f in os.listdir(jd)), "journal files 0600")
        check("WATCHDOG=1" in notes, "the watchdog notified")
        check(all(h in (FAPI, SAPI, PUSHOVER, TG, HC) for h, _m, _p in fn.log), "no other host")
        clean = os.path.join(root, "clean.log")
        open(clean, "w").write("G-KEY PASS - enableReading True\nat 1795000000 from 10.0.0.2\n")
        dirty = os.path.join(root, "dirty.log")
        open(dirty, "w").write("x %s y 4242 z 203.0.113.7 w 203.0.113.70\n" % vals["pushover-token"])
        check(mode_scan([clean], etc, uid, ["203.0.113.7"]) == 0, "scan: a clean file")
        check(scan_counts(open(dirty, "rb").read(), [("t", vals["pushover-token"]), ("c", "4242"),
                                                     ("a", "203.0.113.7")]) == {"t": 1, "c": 1, "a": 1},
              "scan: a token, the chat id and an address found, a longer address not")
        check(mode_scan([clean, dirty], etc, uid, ["203.0.113.7"]) == 4, "scan: a dirty file fails G-PRINT")
    finally:
        shutil.rmtree(root, ignore_errors=True)
    check(not os.path.exists(root), "the self-test's tree removed")
    out("SELFTEST PASS: %d checks" % n[0])
    return 0


def main(argv):
    modes = {"secrets": mode_secrets, "find-chat": mode_find_chat, "prove": mode_prove, "serve": mode_serve,
             "status": mode_status, "selftest": mode_selftest}
    if len(argv) >= 3 and argv[1] == "scan":
        assert os.geteuid() == 0, "BLOCKED: scan runs as root"
        return mode_scan(argv[2:])
    if len(argv) != 2 or argv[1] not in modes:
        out("usage: liq-guard.py " + "|".join(modes) + "|scan FILE...")
        return 1
    if argv[1] != "selftest":
        assert os.geteuid() == 0, "BLOCKED: %s runs as root" % argv[1]
    return modes[argv[1]]()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

## Appendix B — the unit file, byte for byte

### `deploy/systemd/liq-guard.service`

```ini file=deploy/systemd/liq-guard.service
# btc-5m-twap: the liquidation guard - the Boss's Binance Futures positions read every five seconds by a key that can
# read and nothing else, Telegram and Pushover's emergency alarm as they near liquidation (TZ-54, CANON PART VII).
# Installed byte for byte as /etc/systemd/system/liq-guard.service; its stop is systemctl disable --now. It never trades.
[Unit]
Description=Liquidation guard, the Boss's Binance Futures positions watched for liquidation
Wants=network-online.target
After=network-online.target time-sync.target
StartLimitIntervalSec=0

[Service]
Type=notify
NotifyAccess=main
WorkingDirectory=/root/liq-guard-svc
ExecStart=/root/tz04a-env/venv/bin/python -B -u /root/liq-guard-svc/liq-guard.py serve
Restart=always
RestartSec=15
RestartPreventExitStatus=2
TimeoutStartSec=120
WatchdogSec=300
MemoryMax=96M
NoNewPrivileges=yes
PrivateTmp=yes
ProtectSystem=strict
ReadWritePaths=/var/lib/liq-guard
StandardOutput=append:/var/lib/liq-guard/service.log
StandardError=append:/var/lib/liq-guard/service.log

[Install]
WantedBy=multi-user.target
```

## Appendix C — B-DEPLOY, byte for byte

### `b-deploy.sh`

```bash file=b-deploy.sh
#!/bin/bash
# TZ-54 B-DEPLOY - the liquidation guard on the capture host, one sequence, each step gated on the one before it: the
# host and its memory read, the code and the unit file installed byte for byte, G-PROVE (the Boss acknowledges the
# test alarm in Pushover), G-UNIT and, 15 minutes on, G-LIVE. Started by the Executor or by the Boss with the same line,
# under systemd-run, so that no dropped connection ends it (TZ-54 section 3, step 8). Its log is
# /root/tz54-work/logs/60-deploy.log. A FAIL after the unit was started stops it, systemctl disable --now.
exec >>/root/tz54-work/logs/60-deploy.log 2>&1
export LC_ALL=C TZ=UTC
set -u
W=/root/tz54-work
SVC=/root/liq-guard-svc
VAR=/var/lib/liq-guard
PY=/root/tz04a-env/venv/bin/python
UNIT=liq-guard.service
SUMS="782efaa88e268bd6ace42e23dc192e279ae130bb7bdc23d2f4de4d628c4da66f  liq-guard.py
26f609134730e4b9080bcdddbf2365ba35b1f69ddc1633d538a250bd46bce920  liq-guard.service"
MEM_FLOOR=100663296        # the unit's MemoryMax, 96 MiB: the most it may hold (TZ-54 section 6)
STARTED=0

say() { printf '%s B-DEPLOY %s\n' "$(date -u +%FT%T.%3NZ)" "$*"; }
prop() { systemctl show "$UNIT" -p "$1" --value; }
props() { systemctl show "$UNIT" -p ActiveState -p SubState -p Result -p ExecMainStatus -p NRestarts -p MainPID \
          -p UnitFileState -p WatchdogUSec -p MemoryCurrent -p MemoryPeak | tr '\n' ' '; echo; }
grd() { "$PY" -B "$SVC/liq-guard.py" "$@"; }
state() { /usr/bin/python3 -I -B -c 'import json, sys; print(json.load(open(sys.argv[1])).get(sys.argv[2]))' \
          "$VAR/state.json" "$1"; }
fail() {
    say "FAIL at $1"
    if [ "$STARTED" = 1 ]; then
        systemctl disable --now "$UNIT"
        say "the unit stopped, disable --now exit=$?: $(props)"
        grd status
    fi
    say "END exit=1"
    exit 1
}

say "BEGIN pid $$"
H1=$(find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit)
H2=$(df -B1 --output=source,size /var/lib/btc-recorder | tail -n 1 | tr -s ' ')
H3=$(grep -c e3975b5da44c5328adf3bf3914634cd878842c73 /var/lib/btc-recorder/runtime.jsonl)
say "host: a manifest ${H1:+found}; $H2; runtime.jsonl names e3975b5 $H3 times"
[ -n "$H1" ] && [ "$H2" = "/dev/vda2 31612203008" ] && [ "${H3:-0}" -ge 1 ] || fail "the host: not the capture host"

# -- 1. the unit already running: nothing installed, proved or started again -------------------------------------------
if [ "$(prop ActiveState)" = active ]; then
    say "the unit is active already: $(props)"
    STARTED=1
else
    # -- 2. memory, read up to five times a minute apart (map section 7 item 137) ---------------------------------------
    for i in 1 2 3 4 5; do
        avail=$(awk '/^MemAvailable:/ {print $2 * 1024}' /proc/meminfo)
        say "MemAvailable read $i: $avail bytes, the floor $MEM_FLOOR"
        [ "$avail" -ge "$MEM_FLOOR" ] && break
        [ "$i" = 5 ] && fail "memory: under the floor at five reads"
        sleep 60
    done

    # -- 3. the code and the unit file, byte for byte -------------------------------------------------------------------
    install -d -m 0700 -o root -g root "$W/inst" || fail "install: the staged copies"
    install -m 0600 "$W/stage/guard/liq-guard.py" "$W/inst/liq-guard.py" || fail "install: the staged guard"
    install -m 0600 "$W/stage/deploy/systemd/liq-guard.service" "$W/inst/liq-guard.service" || fail "install: staged unit"
    (cd "$W/inst" && printf '%s\n' "$SUMS" | sha256sum -c -) || fail "install: the staged bytes"
    install -d -m 0700 -o root -g root "$SVC" "$VAR" || fail "install: $SVC and $VAR"
    install -m 0600 -o root -g root "$W/inst/liq-guard.py" "$SVC/liq-guard.py" || fail "install: the guard"
    install -m 0600 -o root -g root "$W/inst/liq-guard.service" "$SVC/liq-guard.service" || fail "install: its copy"
    install -m 0644 -o root -g root "$W/inst/liq-guard.service" "/etc/systemd/system/$UNIT" || fail "install: the unit"
    systemctl daemon-reload || fail "install: daemon-reload"
    (cd "$SVC" && printf '%s\n' "$SUMS" | sha256sum -c -) || fail "install: the installed bytes"
    cmp "$SVC/liq-guard.service" "/etc/systemd/system/$UNIT" || fail "install: the unit file"
    ls -la "$SVC" "/etc/systemd/system/$UNIT"
    say "installed: $(props)"
    [ "$(prop LoadState)" = loaded ] && [ "$(prop UnitFileState)" = disabled ] || fail "install: the unit's state"

    # -- 4. G-PROVE, once for this code: the Boss acknowledges the test alarm within 15 minutes ---------------------------
    if /usr/bin/python3 -I -B - "$SVC/liq-guard.py" "$VAR/prove.json" <<'EOF'
import hashlib, json, os, sys
code = hashlib.sha256(open(sys.argv[1], "rb").read()).hexdigest()
rec = json.load(open(sys.argv[2])) if os.path.exists(sys.argv[2]) else {}
sys.exit(0 if rec.get("code_sha256") == code and rec.get("pass") is True else 1)
EOF
    then
        say "G-PROVE read PASS for this code already: not run again"
    else
        say "G-PROVE: the Boss's phone rings - Pushover's test alarm, acknowledged within 15 minutes"
        grd prove || fail "G-PROVE"
    fi

    # -- 5. G-UNIT ------------------------------------------------------------------------------------------------------
    STARTED=1
    systemctl enable --now "$UNIT" || fail "G-UNIT: enable --now"
    say "enabled and started; read in 60 s"
    sleep 60
    say "G-UNIT read: $(props)"
    grd status
    [ "$(prop ActiveState)" = active ] && [ "$(prop SubState)" = running ] && [ "$(prop NRestarts)" = 0 ] &&
        [ "$(prop UnitFileState)" = enabled ] && [ "$(prop WatchdogUSec)" = 5min ] || fail "G-UNIT: systemd's reads"
    [ "$(state key_ok)" = True ] && [ "$(state blind)" = False ] && [ "$(state polls_ok)" -ge 1 ] ||
        fail "G-UNIT: the guard's own state"
    tail -n 5 "$VAR/service.log" | grep -q '^SERVE start: key True, positions read ' || fail "G-UNIT: the start line"
    say "G-UNIT PASS"
fi

# -- 6. G-LIVE, 15 minutes after the start ------------------------------------------------------------------------------
PID=$(prop MainPID)
T0=$(date -d "$(prop ActiveEnterTimestamp)" +%s)
WAIT=$(( T0 + 900 - $(date +%s) ))
[ "$WAIT" -gt 0 ] && { say "G-LIVE read in $WAIT s"; sleep "$WAIT"; }
say "G-LIVE read: $(props)"
grd status
[ "$(prop ActiveState)" = active ] && [ "$(prop NRestarts)" = 0 ] && [ "$(prop MainPID)" = "$PID" ] ||
    fail "G-LIVE: systemd's reads"
[ "$(state key_ok)" = True ] && [ "$(state blind)" = False ] && [ "$(state polls_ok)" -ge 150 ] &&
    [ "$(state disk_faults)" = 0 ] || fail "G-LIVE: the guard's own state"
say "G-LIVE PASS"
say "END exit=0"
exit 0
```
