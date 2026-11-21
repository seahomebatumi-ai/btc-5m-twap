# TZ-55 — the liquidation guard, its second version: a position's gains told from 7% beyond its entry, every message opening with its side's colour — green for a long, red for a short; three stages of calls with the margin to 5%; an acknowledged call means the Boss is at work, and nothing rings while he works; the cards redesigned — the first version replaced on the capture host, and the second's request paths, what it sees and how it looks proved by its own code before it starts

**Canonical filename:** `TZ-55-liq-guard-v2.md`. The committed file takes this name and no other.

**Executor model: Claude Opus 5.5.** A running guard of the Boss's money replaced, credentials he types, an alarm on his phone, a unit that outlives the run.

**Required System Map revision:** `2026-11-21-e` — on `main` with the merge of pull request #52, TZ-54's verdict. **This TZ ships with no map revision:** its merge replaces two `frozen` rows — `guard/liq-guard.py` and `deploy/systemd/liq-guard.service` — and adds one, `research/tz55-liq-guard-v2.py`, and the verdict's revision carries them; no other uploaded TZ waits to run (CANON hard rule 17).

**Map sections this TZ rests on**, copied from §10's C8 (map §7 item 174): §0, the fingerprint gate and its table; §1, the repository; §3, the units and the trees on the host; §6, its rows host, host identity for TZ host gates, language, git remote, egress, disk, disk floors and caps, memory, process supervision, sandbox limit — destructive actions, and harness — background output; §7 items 86, 91, 95, 115, 118, 137, 138, 144, 167, 174, 176, 195, 196 and 197.

**Required anchors**, from map §0. A mismatch on any one is BLOCKED before any work:

| anchor | required |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` |
| `A4` — executor contract | `6ac6e10aeabc` |
| `A5` — recorder | `0f6c90451cbd` |
| `A6` — pricer | `729f0bcdbee3` |

**Written authorization (contract §10).** From the capture host, every connection IPv4 (`V4HTTPS.connect`, Appendix A lines 246 to 250), by `guard/liq-guard.py`'s modes and nothing else: **Binance, with the Boss's key, GET reads alone** — `fapi.binance.com`'s `/fapi/v1/time`, unsigned; its `/fapi/v3/positionRisk` — `/fapi/v2/positionRisk` where v3 answers `404` — and `/fapi/v1/leverageBracket`, signed; and `api.binance.com`'s `/sapi/v1/account/apiRestrictions`, signed. **No order, no transfer, no change of margin, leverage or any setting — no request to Binance but these four GETs** — and **with a key that can read and nothing else**, its permissions read by the guard itself and every other key refused, as TZ-54 proved them. **Pushover**, `api.pushover.net`: `/1/users/validate.json`, `/1/messages.json` — its fields `title`, `message`, `priority`, `html`, `sound`, `url`, `url_title`, and `retry`, `expire` and `tags` at emergency priority (`Pushover.send`, lines 378 to 389) — `/1/receipts/<receipt>.json` and its `cancel.json`, each with the token of the application that sent it. **Telegram**, `api.telegram.org`, the guard's own bot: `getMe`, `getUpdates`, `sendMessage`, `editMessageText` and `answerCallbackQuery` (`Telegram`, lines 404 to 436). **`hc-ping.com`**, the dead-man's ping. Headers: `User-Agent: btc-5m-twap-liq-guard` on every request (`Net._call`, lines 270 to 295); `Accept: application/json` and, signed, `X-MBX-APIKEY` at Binance (`Binance._get`, lines 318 to 325); `Content-Type: application/x-www-form-urlencoded` on Pushover's POSTs and `application/json` on Telegram's. **No other venue, exchange or key is called by this TZ, and the live host is not reached.**

**Before EXECUTE.** The Boss has, where he chooses to: on **pushover.net**, two more applications, **«Сторож LONG»** and **«Сторож SHORT»**, each with its icon from the Architect's message — the green and the red — so that a long's notice and a short's come through their own applications and their icons colour his lock screen; and on **healthchecks.io**, his check's Pushover integration set to **Emergency** for «down» (map §7 item 195). Either may be skipped: §3 step 9 asks for each token, and Enter skips it. **He is at his phone for the run's middle half hour:** he types the two tokens or skips them; he answers «да» or «нет» twice — to what the guard sees and to how its two examples look — and acknowledges its test alarm (§3 step 10). **His positions are unwatched from the first version's stop to the second's start, while he answers** (§1.9).

**When: at any hour he is awake.** The second version runs from then on.

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

**`ready=1` begins the run. `ready=0`, or a read without its `ready=` line, begins nothing:** no directory is made and no report is written — this TZ has not executed (CANON hard rule 5) — and the Executor gives the Boss the line as printed and, in one line in Russian, that `EXECUTE TZ-55` is sent again an hour later. This is not BLOCKED and owes no report (contract §5). Then `mkdir /root/tz55-work /root/tz55-work/logs; echo "exit=$?"` — `exit=0` proves neither existed; anything else is BLOCKED — and the readiness read again into `logs/00-ready.log`. **From here every command's output goes to a log under `/root/tz55-work/logs/`, one file per step, under the names §3 fixes; nothing to the session's scratchpad** but §9's last block (map §7 item 118).

Four abbreviations, written out in full in every block handed to the Boss:

- **`P`** — `nice -n 19 /root/tz04a-env/venv/bin/python -B`.
- **`C M NN`** — the checker's mode `M`: `cd /root/tz55-work && { date -u +%FT%T.%NZ; P /root/tz55-work/stage/research/tz55-liq-guard-v2.py M; echo "exit=$?"; } >> /root/tz55-work/logs/NN.log 2>&1; tail -n 60 /root/tz55-work/logs/NN.log`. The checker asserts it runs from `/root/tz55-work`.
- **`G M NN`** — the second version's mode `M` from the stage: the same with `/root/tz04a-env/venv/bin/python -B /root/tz55-work/stage/guard/liq-guard.py M`, without `nice`.
- **`S`** — the scratchpad directory the session's system prompt names.

### 0.1 The files, staged

**The checker is TZ-54's, renamed:** `research/tz54-liq-guard.py` read from `main`, at its map §0 hash, changed by the edits below, each asserted to occur the number of times it names — so that its capture-host modes, `fingerprint`, `number`, `refs`, `scratch` and `reclaim`, run under this TZ's number, paths and map revision; it reaches no host but GitHub's through `git`. **The guard, its unit file and B-DEPLOY are this file's Appendices A, B and C**, each extracted by its fence and the next line that is a fence alone. **On the branch, the guard and its unit file replace the first version's**, each read first at TZ-54's hash. **This script, verbatim**, its first argument the destination and its second `stage` — four files — or `branch` — the branch's three — its output into `logs/01-stage.log`:

```
/root/tz04a-env/venv/bin/python -B - /root/tz55-work/stage stage <<'EOF3'
import hashlib, os, subprocess, sys
REPO = "/root/btc-5m-twap"
TZ = REPO + "/CryptoTZ/TZ-55-liq-guard-v2.md"
DEST, WHAT = sys.argv[1], sys.argv[2]
assert WHAT in ("stage", "branch"), WHAT
WANT = {
    "research/tz55-liq-guard-v2.py": "1f7e9e8393ec3efda564a2ee0ff8356228f1ab2e435acad5f6f4729a9870bf35",
    "guard/liq-guard.py": "6b851f3f93578dadcb683d33969b4d235daf2c852dbdce74c66e978946ec840a",
    "deploy/systemd/liq-guard.service": "11bff792d802cbf1abe9ee4f496c24517cce0e63a0dbf6aa49f277b7cdc55157",
    "b-deploy.sh": "d4968301541d9c49148081d127be5951741999bf55ceb795b54513602665e814"}
FIRST = {"guard/liq-guard.py": "782efaa88e268bd6ace42e23dc192e279ae130bb7bdc23d2f4de4d628c4da66f",
         "deploy/systemd/liq-guard.service": "26f609134730e4b9080bcdddbf2365ba35b1f69ddc1633d538a250bd46bce920"}
FILES = {"branch": ("research/tz55-liq-guard-v2.py", "guard/liq-guard.py", "deploy/systemd/liq-guard.service"),
         "stage": ("research/tz55-liq-guard-v2.py", "guard/liq-guard.py", "deploy/systemd/liq-guard.service",
                   "b-deploy.sh")}


def fenced(fence):
    lines = open(TZ, encoding="utf-8").read().split("\n")
    i = lines.index(fence)
    j = lines.index("```", i + 1)
    return ("\n".join(lines[i + 1:j]) + "\n").encode("utf-8")


def checker():
    b = subprocess.run(["git", "-C", REPO, "show", "origin/main:research/tz54-liq-guard.py"], capture_output=True,
                       check=True).stdout
    assert hashlib.sha256(b).hexdigest() == "fd8f8c21d3dc5c36655a6948ce593a03d06ca8f783955ea7d18df5a57ea0e4bf", "base"
    t = b.decode("utf-8")
    EDITS = [
        ('"""TZ-54 - the liquidation guard deployed on the capture host: this file is TZ-54\'s checker renamed, of which\n'
         "TZ-54 runs the capture host's modes alone - the fingerprint, the number, the refs, the scratch and the reclaim -\n"
         "and the self-test. The guard itself and every check of its own - its credentials, its request paths, its key's\n"
         "permissions, its alarm, its state under systemd - are guard/liq-guard.py's modes (TZ-54 section 5). Every other\n"
         "mode of this file is TZ-51's, TZ-52's and TZ-54's, kept and tested; TZ-54 runs none of them.\n",
         '"""TZ-55 - the liquidation guard\'s second version deployed on the capture host: this file is the first version\'s\n'
         "checker renamed, of which TZ-55 runs the capture host's modes alone - the fingerprint, the number, the refs, the\n"
         "scratch and the reclaim - and the self-test. The guard itself and every check of its own - its credentials, its\n"
         "request paths, its key's permissions, its alerts, its state under systemd - are guard/liq-guard.py's modes (TZ-55\n"
         "section 5). Every other mode of this file is TZ-51's, TZ-52's and TZ-53's, kept and tested; TZ-55 runs none.\n", 1),
        ("TZ-54-liq-guard", "TZ-55-liq-guard-v2", 3),
        ("tz-54-liq-guard", "tz-55-liq-guard-v2", 1),
        ("tz54", "tz55", 21),
        ("TZ-54", "TZ-55", 7),
        ("ТЗ-54", "ТЗ-55", 3),
        ('MAP_REVISION = "2026-11-21-d"', 'MAP_REVISION = "2026-11-21-e"', 1),
        ('MAP_ROWS = {"frozen": 67, "tracked": 2, "reported": 1}', 'MAP_ROWS = {"frozen": 70, "tracked": 2, "reported": 1}', 1),
    ]
    for old, new, n in EDITS:
        assert t.count(old) == n, (old[:60], t.count(old), n)
        t = t.replace(old, new)
    return t.encode("utf-8")


data = {"research/tz55-liq-guard-v2.py": checker(),
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
            old = fh.read()
        if old == b:
            state = "equal, kept"
        else:
            assert WHAT == "branch" and hashlib.sha256(old).hexdigest() == FIRST.get(rel), path + " exists with other bytes"
            with open(path, "wb") as fh:
                fh.write(b)
            state = "replaced the first version"
    else:
        with open(path, "xb") as fh:
            fh.write(b)
        state = "created"
    print(path, b.count(b"\n"), len(b), WANT[rel], state)
EOF3
```

| file | lines | bytes | SHA-256 |
|---|---|---|---|
| base: `research/tz54-liq-guard.py` on `main`, map §0 | 3,323 | 188,349 | `fd8f8c21d3dc5c36655a6948ce593a03d06ca8f783955ea7d18df5a57ea0e4bf` |
| `research/tz55-liq-guard-v2.py` — the checker | 3,323 | 188,383 | `1f7e9e8393ec3efda564a2ee0ff8356228f1ab2e435acad5f6f4729a9870bf35` |
| `guard/liq-guard.py` — Appendix A, the guard's second version | 2,772 | 148,628 | `6b851f3f93578dadcb683d33969b4d235daf2c852dbdce74c66e978946ec840a` |
| `deploy/systemd/liq-guard.service` — Appendix B | 30 | 1,086 | `11bff792d802cbf1abe9ee4f496c24517cce0e63a0dbf6aa49f277b7cdc55157` |
| `b-deploy.sh` — Appendix C | 147 | 8,633 | `d4968301541d9c49148081d127be5951741999bf55ceb795b54513602665e814` |
| the first version on `main`: `guard/liq-guard.py` and `deploy/systemd/liq-guard.service`, map §0 | 1,850 and 29 | 93,840 and 1,055 | `782efaa8…` and `26f60913…` |

A failed assert or another hash is BLOCKED; on `stage` every line reads `created`. **`b-deploy.sh` is staged and never committed:** the report quotes it by this hash, and §9 keeps it in the forensic store.

### 0.2 Fingerprint

`C fingerprint 02-fingerprint` performs contract §1 steps 3 and 4 inside the checker against `SYSTEM-MAP.md` and the files of its §0 table in the primary checkout, and must print `FINGERPRINT PASS: revision 2026-11-21-e; anchors 6 of 6, 4 re-derived; rows 73: frozen 70 of 70 equal, tracked 2, reported 1; the signing page on main equal to TZ-50's Appendix B` (`mode_fingerprint`, the checker's lines 1087 to 1122). Anything else is BLOCKED — **a `main` without pull request #52's merge among them:** its `guard/liq-guard.py` row is not there.

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
sha256sum /root/liq-guard-svc/liq-guard.py /root/liq-guard-svc/liq-guard.service /etc/systemd/system/liq-guard.service
ls -la /etc/liq-guard /var/lib/liq-guard
/root/tz04a-env/venv/bin/python -B /root/liq-guard-svc/liq-guard.py status
echo "global IPv4 addresses: $(ip -4 -o addr show scope global | wc -l)"; command -v ip df systemd-run install cmp sha256sum stat
```

- **H1** — `find` prints exactly one path. **H2** — `df` names source `/dev/vda2` and size `31612203008`, and `grep -c` prints at least `1`: with H1, map §6's host identity, in the form TZ-46's host gate read it.
- **H3** — the interpreter prints `3.12.` (map §6, language).
- **H4** — **the first version is what runs:** `liq-guard.service` reads `LoadState=loaded`, `UnitFileState=enabled`, `ActiveState=active`; `sha256sum` prints `782efaa88e268bd6ace42e23dc192e279ae130bb7bdc23d2f4de4d628c4da66f` for the guard and `26f609134730e4b9080bcdddbf2365ba35b1f69ddc1633d538a250bd46bce920` for both unit files; `/etc/liq-guard` holds `binance-key`, `binance-secret`, `pushover-user`, `pushover-token`, `tg-token` and `tg-chat`, each `0600`, root's. The other units' lines, `hc-url`'s presence and `status`'s `dead_man` are recorded, not judged (map §7 items 86 and 195).
- **H5** — at least one global IPv4 address, **counted and never printed**, and the seven commands found.

Any of H1 to H5 failing is BLOCKED.

### 0.4 The number and the refs

Into `04-number.log`: `git -C /root/btc-5m-twap fetch origin`, then `C number 04-number`, which must print `NUMBER PASS - 2 of 2` — of the number `TZ-55`, this file alone under `CryptoTZ/` and no report (CANON hard rule 2) — and `C refs 04-number`, which must find no `refs/heads/tz-55-liq-guard-v2` on `origin`. Either failing is BLOCKED.

---

## 1. What this TZ decides

### 1.1 The Boss's specification of 2026-11-21, decided (map §7 item 196)

His points, in his words: a profit alert "If the price rises above the entry point by 7%", "naturally green for LONG and red for SHORT, so that I do not miss the moment of maximum profit!"; "Adding margin to move liquidation 5% away from the price!" and "Three-stage alerts."; and "when I acknowledge an alert (press it), it means I have engaged in the process, and at that moment, no on-screen calls should distract me". **The decisions:** a position's gain is read **beyond its entry on its own side** — above it for a long, below it for a short — so that a short's profit is told as a long's is (§1.5); the margin hint aims at `5`% (§1.3); the three stages each call, the last two critically (§1.3); an acknowledged call, or the card's button, silences every call about that position while he works — **with one exception, the last line, because an alarm acknowledged half asleep and slept through is the night's worst case** (§1.4); and every message is redesigned after his own bot's: a coloured first line, sections, aligned figures, a quoted bottom line, arrows of the last five minutes (§1.6). **No alert can know the top:** the gain alerts mark the position's records and the price's retreat from them, and claim nothing of what comes next. **The guard still never trades, adds margin or holds a key that can** (CANON PART VII).

### 1.2 Each side its colour, and its own Pushover application

Every message about a position opens with its side's colour, **🟢 for a long and 🔴 for a short** (`DOT`, line 101; `head`, lines 764 to 767), then its coin, its side and leverage, then what happened. **On the lock screen, iOS shows a Pushover message beside its application's icon** — the Boss's own screenshot shows the first version's default — so each side's messages go through an application of its own where he made one: `pushover-long` and `pushover-short`, two optional credentials of the form of `pushover-token` (`CREDENTIALS`, line 109), each with the icon the Architect sends him; **without one, that side's messages go through «Сторож» and keep their coloured first character.** Messages about no position — the test, blindness, a refused key — go through «Сторож» (`Guard.__init__`, lines 991 to 1017; `Guard.flush`, lines 1104 to 1150). **Each receipt is read and cancelled with the token of the application that sent it** (`Guard.check_alarms`, lines 1402 to 1422).

### 1.3 Liquidation — three stages, each a call, each with the margin to his target

The distance and the stages are the first version's: the distance from the mark price to the liquidation price as a percent of the mark on the side that loses (`distance_pct`, lines 498 to 504); three thresholds, the Boss's — kept from the first version's `state.json`, `4`, `2.5` and `1.5` at his last setting, `5`, `3` and `1.5` by default (`DEFAULT_THRESHOLDS`, line 68; `settings_of`, lines 689 to 698); a stage announced once a descent, re-armed a point above its threshold, the highest of a jump alone (`step`, lines 515 to 524). **What changes:** each position is announced on its own, through its side's application (`Guard.announce`, lines 1230 to 1247): **stage 1 at Pushover's high priority**, sound `spacealarm` — it bypasses Pushover's quiet hours and, with Critical Alerts on for high priority on his iPhone, his silent mode; **stages 2 and 3 at emergency priority**, sounds `siren` and `persistent`, repeated every `30` s until acknowledged (`SOUND`, line 98). **Every call and card says how much margin moves the liquidation price to `5`% from the price** (`TARGET_PCT`, line 70; `margin_hint`, lines 539 to 548, the first version's arithmetic, exact for an isolated position and an estimate for a cross one; `hint`, lines 780 to 788, rounds it up), **«Цель N» setting it, `1` to `30`**. **Each call carries a link that opens the position in Binance** (`BINANCE_URL`, line 100), and **its Telegram card is live**: edited in place at most every `10` s while the danger lasts — no notification — its distance, prices, arrow and hint current (`LIVE_EDIT_S`, line 79; `Guard.edit_card`, lines 1285 to 1309; `liq_card`, lines 800 to 837). **Where the distance climbs past the second stage's threshold and a point, its open calls are cancelled; past the first's and a point, the card's last edit says the danger is over** (`Guard.tend`, lines 1342 to 1383; `Guard.finish`, lines 1385 to 1391). **Margin added is seen** — the liquidation price moved `0.2`% of itself away from the worst it read (`TOPUP_REL`, line 78; `topup_seen`, lines 607 to 611) — and confirmed by a quiet message.

### 1.4 He is at work: nothing rings about that position

**An emergency call he acknowledges in Pushover, read from its receipt every `10` s, or the card's button «✋ Я в деле», pressed from his chat alone, puts him at work on that position for `10` minutes** (`ENGAGE_S`, line 75; `Guard.engage`, lines 1264 to 1283; `Guard.callback`, lines 1479 to 1494). **While he works:** that position's open calls are cancelled at once and no new one is sent — a deeper stage changes its live card alone; every gain alert of any position is held, and told quietly once no work remains (`Guard.tell`, lines 1249 to 1262; `Guard.end_engaged`, lines 1311 to 1340); a call queued before he engaged is dropped unsent (`Guard.flush`). **Margin seen added extends his work by `10` minutes from then; his work ends** with margin added and the distance past the first threshold — a ✅ and the card's last edit — or the danger over by itself, or the position closed, or the `10` minutes out: **then, with the distance still at or under the second threshold, a fresh emergency call** — "10 мин после «Подтвердить» — маржа не добавлена" — and under the first, a high-priority one (`liq_push`, lines 840 to 860). **The last line:** while he works, a distance at or under `1`% — the third threshold where that is lower — with no margin seen added for `3` minutes sends **one** emergency call (`LAST_LINE_PCT`, `LAST_QUIET_S`, line 76 and line 77; `last_line`, lines 614 to 616). A call he acknowledges again puts him at work again.

### 1.5 Gains — records and retreats

The gain is `100 × (mark / entry − 1)` for a long and `100 × (1 − mark / entry)` for a short (`gain_pct`, lines 556 to 558), with the ROE over the initial margin at the entry, as Binance's app shows it (`roe_pct`, lines 561 to 567). **A record is told once the gain reaches `7`%** (`PROFIT_FROM`, line 71) **and then at each new record `3` points above the last told, or a quarter above it, the larger** (`next_record`, lines 570 to 572) — `7`, `10`, `13`, `16.25`, `20.3`… **A retreat is told twice a record at most:** once the gain is a third of the peak below it, and at least `2` points — "откат от пика" — and once at half the peak — "ушла половина прибыли", or "прибыль ушла" at zero or below (`profit_step`, lines 575 to 604; `PULLBACK_MIN_PP`, line 73). **Each at Pushover's high priority**, sounds `cashregister` and `falling`, through the side's application, with its card (`record_card`, lines 863 to 877; `pullback_card`, lines 891 to 903). **The memory** — side, entry, best price and when, the last record told and the retreats since — is kept in `memory.json` across restarts; an entry moved `0.1`% — margin averaged in — or a side changed starts it again (`ENTRY_MOVE`, line 74; `Guard.load_memory`, lines 1028 to 1036). **At the second version's first start no memory exists: a position already `7`% or more beyond its entry is told once, as its first record.** **«Прибыль N» sets the start, `3` to `100`; «Прибыль 0» or «Прибыль выкл» turns gains off** — before sleep, where he wants no profit call at night (`profit_of`, lines 701 to 706).

### 1.6 Telegram — the cards, the buttons, the commands

**Every message is Telegram's HTML** (`Telegram.send`, lines 416 to 420): a coloured first line, the alert in bold, figures aligned in a monospace block, the bottom line quoted, an arrow and the value five minutes before (`then_of`, `arrow`, lines 619 to 626 and lines 629 to 631). **A card's buttons:** «📲 Открыть … в Binance» and, while a call is out, «✋ Я в деле — тише 10 мин». **The keyboard:** «Статус», «Тест», «Настройки», «Помощь». **«Статус»** — one line a position, nearest the liquidation first: its colour, coin, side, leverage, gain and arrow, and distance, with the hint inside the first threshold; **the guard's own health folded into a quote he opens** — the Boss struck it out of the first version's status as clutter (`status_card`, lines 933 to 948). **«Настройки»** — the thresholds, the target and the gains' start, and how to change each (`settings_card`, lines 951 to 955); **«Пороги a b c»**, **«Цель N»**, **«Прибыль N»** — kept across restarts. **«Тест»** — an emergency call through «Сторож», and «✅ Звонок дошёл» once acknowledged. A word that is no command answers with the keyboard's names. A quiet heartbeat at `19:00` UTC lists the positions. Commands and buttons from his pinned chat alone; every other chat is journaled and never answered (`Guard.telegram`, lines 1457 to 1477; `Guard.command`, lines 1496 to 1535).

### 1.7 The prove — CANON hard rule 14, and how it looks confirmed by the Boss

`prove` runs every request path the unit uses through the guard's own functions before the unit starts (`mode_prove`, lines 1772 to 1927), each a gate of `prove.json`, which carries the code's SHA-256: **G-CRED** — the credentials of their form, `0600`, root's, the side applications counted; **G-TIME**; **G-KEY** — the key's permissions, every boolean printed; **G-POS** — the positions served and parsed, counted with their liquidation and entry prices; **G-BRACKET**; **G-PUSH** — the user key and every application's token validated; **G-TG** — `getMe` and one message; **G-SEE** — his status card, with his own settings, and «Совпадает с твоими позициями в Binance? Ответь «да» или «нет»», «да» within `900` s; **G-LOOK — two examples, a long's record through its application and a short's call through its own, each at normal priority, and their cards, and «Цвета видны, всё читается? Ответь «да» или «нет»», «да» within `900` s** (`samples`, lines 1748 to 1755); **G-ALARM** — a test call at emergency priority acknowledged within `900` s; and **G-HC** — the dead-man pinged, last. **Through every wait the prove pings the dead-man once a minute**, so that the first version's stop does not read at healthchecks.io as the host's death; **and it confirms his answers to Telegram**, so that the unit never reads «да» as a command. **PASS is the eleven gates in this order, each PASS** (`PROVE_GATES`, line 91).

### 1.8 The record, and what is never printed

`/var/lib/liq-guard/`, `0700`, root's: `state.json` every `30` s — counts, states, instants and the settings, no position; **`memory.json`, `0600` — the gains' memory, a position's prices among them**; `journal/<day>.jsonl`, `0600` — each event: a stage reached, a record or a retreat with the gain and the price, a call sent with its kind and application, a receipt acknowledged, his work begun and ended, margin seen added, an error once a minute at most, a command's name; files older than `90` days removed; `prove.json`; and `service.log`, **`0600` from this TZ** (§1.9). **A credential, the chat id and this host's address are never written:** every text journaled or printed is scrubbed of each credential and every IPv4 address first (`Scrub`, lines 228 to 238). **No mode the Executor runs prints a symbol, price, size or margin:** `prove`, `status`, `secrets` and `scan` print counts, names, booleans and states (`mode_status`, lines 1930 to 1951). **G-PRINT** (§4) reads every log and the report.

### 1.9 The replacement, and the unit

**One poller of the bot at a time** — two `getUpdates` callers conflict, and the first version would read the Boss's «да» as a command — **so the prove runs with the first version stopped**: B-DEPLOY (Appendix C) keeps the first version's two files beside the stage, stops it, proves the second from its staged copy and, **on PASS**, installs the second's files byte for byte and restarts the unit; **on any FAIL from the stop on, it puts the first version back — its files where it had replaced them — and restarts it: the guard is never left stopped.** **His positions are unwatched from the stop to the restart** — the prove's minutes, while he answers it at his phone — and the dead-man is kept quiet by the prove (§1.7). **Appendix B is the first version's unit file with `UMask=0077`**, so that `service.log` and every file the unit makes is `0600` (map §7 item 197); B-DEPLOY sets the existing `service.log` `0600`. The rest is the first version's: a system unit, enabled for boot (map §6, process supervision; CANON hard rule 14); `Type=notify`, `WatchdogSec=300`, `Restart=always`, `RestartPreventExitStatus=2`, `StartLimitIntervalSec=0`; `MemoryMax=96M` — the first version's `MemoryPeak` `21,970,944` bytes at TZ-54's close (map §6, memory), the second holding a few kilobytes more a position, its gains' memory and fifteen minutes of history; and its stop, `systemctl disable --now liq-guard.service`. B-DEPLOY's `daemon-reload` re-arms only a timer's `OnActiveSec` (map §7 item 115): the reward book's archive's timer has none since TZ-46, and the pair book's is disabled. A restart by needrestart (map §7 item 176) costs the guard about `15` s and no alarm, and the gains' memory survives it.

### 1.10 What a PASS establishes, and what it does not

A PASS establishes that the second version runs, reads the Boss's positions as he confirmed them, that its examples looked right to him, and that its call reached his phone and was acknowledged. **It does not establish that a later call wakes him** — his phone's settings decide it, and «Тест» checks them at any hour — **nor that a gain alert comes at the top:** none can. **It measures no edge and moves no rung of PART VII's ladder:** the guard is a tool for his own trading, judged against his trading without it (CANON PART V).

---

## 2. Scope

1. **Repository, written:** `guard/liq-guard.py` and `deploy/systemd/liq-guard.service`, replaced, and `research/tz55-liq-guard-v2.py`, new, on the branch `tz-55-liq-guard-v2`, and its pull request; `CryptoReports/TZ-55-liq-guard-v2-report.md` on `main`. **Read:** this file by §0.1's script; `research/tz54-liq-guard.py` by `git show`; `SYSTEM-MAP.md` and the files of its §0 table by `fingerprint`; `CryptoTZ/` and `CryptoReports/` by `number`; `origin`'s refs by `refs`.
2. **Capture host, written:** `/root/tz55-work/**` — the logs, the stage, the worktree `wt`, B-DEPLOY's `inst` and `first`, the checker's `selftest-tmp` — and the primary checkout's record of the worktree, removed by §9; the guard's self-test's temporary tree under `/tmp`, removed by the self-test; **the guard's, kept:** `/root/liq-guard-svc/liq-guard.py` and `liq-guard.service`, replaced by the second version's — or put back to the first's by B-DEPLOY on a FAIL; `/etc/systemd/system/liq-guard.service`, likewise, enabled; `/var/lib/liq-guard/` — `prove.json` replaced, `memory.json` new, `state.json`, `journal/` and `service.log`, its mode `0600`; `/etc/liq-guard/pushover-long` and `pushover-short`, where the Boss gives them, by `secrets`'s exclusive create — **and by B-RESET** (§3 step 10), which removes them where G-PUSH refused them, before anything else has used them. The transient unit `tz55-deploy`, collected when it ends. `/root/btc-forensics/tz55-work--*` by `reclaim`; earlier session directories by B-RECLAIM-SCRATCH (§3 step 8).
3. **Capture host, read:** `/proc`; `df`; the recorder's store by `find` and `grep -c` alone; `systemctl show` of the units §0.3 names; `ip -4`, counted, and by `scan` in memory; the primary checkout; `/root/liq-guard-svc/` and the unit file by `sha256sum`, `cmp` and `ls`; `/etc/liq-guard/` by `ls` — names and modes — and by the guard's modes. **`/var/lib/liq-guard/` is read by the guard's modes, by B-DEPLOY's reads of four fields of `state.json` — `key_ok`, `blind`, `polls_ok`, `disk_faults` — and of `prove.json`'s `code_sha256` and `pass`, by `ls` and `stat`, and by §3 step 11's reads, which print `prove.json` whole and `service.log`'s last lines; `memory.json` and the journal by the guard's modes alone, which print neither.**
4. **Network:** the written authorization's, from the capture host — every host in map §6's egress row since revision `2026-11-21-e`; GitHub by `git` and `gh`.
5. **Not changed, and read by nothing but §0.3's `systemctl show`, `find` and `grep -c` — a named exemption, the host gate's identity and state:** every other unit and store of this project or another. **Not touched:** the guard's other credentials — read by its modes alone, never written; the advisor's credentials and record; the live host — no `ssh` in this TZ.
6. **Never printed — in a log, the report, a pull request or the chat:** a credential, the chat id, an address of this host, or a symbol, price, size or margin of the Boss's positions. The guard's messages to his own chat and his phone carry his positions: they are the product, and no log holds them.

---

## 3. The work, in this order

| step | logs |
|---|---|
| 1 to 5 | `00-ready.log`, `01-stage.log`, `02-fingerprint.log`, `03-host-gate.log`, `04-number.log` |
| 6 | `10-worktree.log`, `11-push.log`, `12-pr.log` |
| 7 | `20-checker-selftest.log`, `21-guard-selftest.log` |
| 8 | `22-scratch.log`, `23-reclaim-scratch.log` |
| 9 | `30-secrets.log` |
| 10 | `59-deploy-start.log`, `60-deploy.log`, `58-reset.log` where B-RESET runs |
| 11 | `61-unit-after.log` |
| 12 | `62-print.log` |
| 13 | none: the session, §9 |

1. **§0.0**, the readiness and the work tree.
2. **§0.1**, `stage`, into `01-stage.log`: four lines `created`.
3. **§0.2**, `fingerprint`.
4. **§0.3**, the host gate.
5. **§0.4**, the number and the refs.
6. **The branch.** Into `10-worktree.log`: `git -C /root/btc-5m-twap worktree add -b tz-55-liq-guard-v2 /root/tz55-work/wt origin/main`, then §0.1's script verbatim but for its arguments, `/root/tz55-work/wt branch` — `research/tz55-liq-guard-v2.py` `created`, the other two `replaced the first version`. Into `11-push.log`: commit the three files on the branch; push with `git -C /root/tz55-work/wt push -u origin tz-55-liq-guard-v2` — through `credential.helper=!gh auth git-credential` where the URL's credential is refused (map §6, git remote) — then `git -C /root/tz55-work/wt ls-remote origin refs/heads/tz-55-liq-guard-v2`, `git -C /root/tz55-work/wt rev-parse HEAD` and `git -C /root/tz55-work/wt diff --numstat --diff-algorithm=myers origin/main HEAD`: the hash on `origin` the worktree's `HEAD`, and exactly `3 2 deploy/systemd/liq-guard.service`, `1201 279 guard/liq-guard.py` and `3323 0 research/tz55-liq-guard-v2.py`. Into `12-pr.log`: the pull request against `main`, opened with `gh pr create`. A failed assert or a non-zero exit is BLOCKED.
7. **The self-tests.** `C selftest 20-checker-selftest` must print `SELFTEST PASS: 141 checks, 141 passed; refused by the hook: 5, each a check's own` — TZ-54's checker, every one of its checks, under this TZ's names. `G selftest 21-guard-selftest` must print `SELFTEST PASS: 127 checks` (§7): it reaches no network — Binance, Pushover, Telegram and healthchecks.io are stand-ins in the process (`FakeNet`, lines 2050 to 2143) — and runs `secrets` at a real pseudo-terminal of its own (`on_terminal`, lines 2152 to 2218), on a temporary tree under `/tmp` that it removes. Anything else is BLOCKED.
8. **The directories beside this session, and B-RECLAIM-SCRATCH.** `cd /root/tz55-work && P /root/tz55-work/stage/research/tz55-liq-guard-v2.py scratch "$(dirname "$S")"`, into `22-scratch.log`, names every UUID directory beside this session's own **live** — born from 1 s before to 60 s after the start of a running `claude` process — or **earlier** (map §7 items 91 and 95); with a directory goes the harness's copy of its background output (map §6, harness — background output). For each named earlier, into `23-reclaim-scratch.log`: `cd /root/tz55-work && P /root/tz55-work/stage/research/tz55-liq-guard-v2.py reclaim <its full path>`, `rm -rf <it>; echo "exit=$?"`, `test -e <it>; echo "exit=$?"` — `RECLAIM PASS`, `exit=0`, `exit=1`. **Its paste**, where the classifier refuses it, the same three lines for each, chained with `&&` up to the `test`.
9. **The Boss's two tokens.** The Executor hands the Boss, **verbatim, in one message**, the block below, and waits for his «готово». Then it reads `30-secrets.log`: `SECRETS binance-key`, `binance-secret`, `pushover-user`, `pushover-token` and `tg-token` each `kept`; `hc-url` `kept`, `written` or `skipped`; `pushover-long` and `pushover-short` each `written, 31 bytes` or `skipped`; and `exit=0`; and, into the same log, `ls -la /etc/liq-guard`: the directory `0700`, every file `0600`, root's. Where a line reads `not given in 3 tries` or the exit is not `0`, the Executor tells the Boss once, in one line, to paste the same line again; a second failure is BLOCKED.

> **Сторож v2 — два токена Pushover (если хотите цветные иконки на экране блокировки).**
>
> **1.** На **pushover.net** → **Create an Application/API Token**: имя **«Сторож LONG»**, иконка — **зелёная** из моего сообщения → скопируйте его **API Token**. Затем так же **«Сторож SHORT»** с **красной** иконкой. Не хотите — пропустите этот шаг: цвет всё равно будет в первом символе сообщения.
>
> **2. В терминале сервера в Варшаве, под root,** вставьте строку:
> `cd /root/tz55-work && { /root/tz04a-env/venv/bin/python -B /root/tz55-work/stage/guard/liq-guard.py secrets; echo "exit=$?"; } | tee -a /root/tz55-work/logs/30-secrets.log`
> Всё прежнее она оставит как есть и спросит только токены «Сторож LONG» и «Сторож SHORT» — вставьте каждый или просто нажмите Enter. Ввод скрыт.
>
> **3.** Напишите мне «готово».

10. **B-DEPLOY — Appendix C, the Executor's first.** The Executor tells the Boss once, in Russian: «Обновляю сторожа. На несколько минут он остановится — пока вы отвечаете. В Telegram придёт карточка с вашими позициями — ответьте «да», если она совпадает с Binance. Потом придут два примера сигналов, 🟢 и 🔴, в Telegram и на экран блокировки — ответьте «да», если цвета видны и всё читается. Потом зазвонит Pushover — нажмите «Подтвердить». На каждое — 15 минут.» Then, into `59-deploy-start.log`:

```
systemd-run --unit=tz55-deploy --collect -p RuntimeMaxSec=7200 /bin/bash /root/tz55-work/stage/b-deploy.sh; echo "exit=$?"
```

`exit=0`, the transient unit started. **Its paste**, where the classifier refuses it (map §6, sandbox limit — destructive actions): the same line, by the Boss, as root, in a terminal on the capture host — **one paste for the whole sequence**, its copies, its stop, its prove, its install, its restart and its timed reads in order, each gated on the one before it (map §7 item 138), **and its reads are the gate's reads**: the Executor reads the log and runs none of it again (map §7 item 144). Either way the Executor reads `tail -n 60 /root/tz55-work/logs/60-deploy.log` at most every `570` s until its `B-DEPLOY END` line. **B-DEPLOY's steps, each gated on the one before it** (§4): the host; the first version installed at TZ-54's bytes — or the second already, installed and active, when only G-LIVE is read again; `MemAvailable` at or above `100,663,296` at one of five reads a minute apart (map §7 item 137); the second staged at §0.1's SHA-256 and the first's two files kept beside it, both read by `sha256sum -c`; **the first stopped and G-PROVE run from the stage**, once for this code; the second installed, `daemon-reload`, its files read at §0.1's SHA-256, the unit file equal to the code's copy by `cmp`, `loaded` and `enabled`, `service.log` `0600`; `systemctl restart`, **G-UNIT** at `60` s; **G-LIVE** `900` s after the start. **`B-DEPLOY END exit=0` is G-DEPLOY PASS.** `END exit=1` is a FAIL at the step its `FAIL at` line names, and B-DEPLOY has put the first version back and restarted it — its lines `the first version installed again` where the second had been installed, and `the first version restarted` with the unit's state — **but at the host, an installed guard of neither version or the memory, where it changed nothing.** Then `systemctl is-active tz55-deploy.service; echo "exit=$?"` must not read `active`. A log that stops without its `END` line for `3,300` s — G-PROVE's three waits of `900` s and a read's `570` beside them — is read again once, then BLOCKED, and the Executor runs `systemctl stop tz55-deploy.service; systemctl restart liq-guard.service; echo "exit=$?"` — its paste the same line — and reports which version `sha256sum /root/liq-guard-svc/liq-guard.py` reads.

**One more B-DEPLOY, at most, and only for these.** Where G-PROVE's FAIL is **G-PUSH** with a side application's token refused, the Executor tells the Boss once, in one line in Russian, the gate and its printed cause, and runs **B-RESET** into `58-reset.log`: `rm` of `/etc/liq-guard/pushover-long` and `/etc/liq-guard/pushover-short`, then `test -e` of each, `exit=1`; its paste the same lines; the Boss pastes step 9's line again — or presses Enter twice — and B-DEPLOY runs once more. **Where G-ALARM's FAIL is no acknowledgement in `900` s,** the Executor tells the Boss once to check Pushover's Critical Alerts and its volume, and runs B-DEPLOY once more, nothing reset. **G-SEE or G-LOOK answered «нет», any other gate of G-PROVE, the install, G-UNIT or G-LIVE is BLOCKED** at its first FAIL: a view or a look the Boss does not accept is a design question for the next TZ, not a retry. A second B-DEPLOY that fails is BLOCKED.
11. **The unit after**, into `61-unit-after.log`, from `/root/tz55-work`: `systemctl show liq-guard.service -p ActiveState -p SubState -p NRestarts -p MainPID -p UnitFileState -p ActiveEnterTimestamp -p WatchdogUSec -p MemoryCurrent -p MemoryPeak`; `sha256sum /root/liq-guard-svc/* /etc/systemd/system/liq-guard.service`; `ls -la /root/liq-guard-svc /var/lib/liq-guard /etc/liq-guard`; `tail -n 20 /var/lib/liq-guard/service.log`; `/root/tz04a-env/venv/bin/python -B /root/liq-guard-svc/liq-guard.py status`; `cat /var/lib/liq-guard/prove.json`. The unit `active`, `NRestarts` `0`, its files at §0.1's SHA-256, `service.log` `0600`, the prove's record `"pass": true`.
12. **G-PRINT on the logs**, into `62-print.log`: `/root/tz04a-env/venv/bin/python -B /root/liq-guard-svc/liq-guard.py scan /root/tz55-work/logs/*.log` must print `G-PRINT PASS`. A FAIL names the file and the kind found, never the value, and is BLOCKED: the file is copied by §9 to the forensic store alone, and the report names it.
13. **The report, the reclaim and the last scan, in this order:** the report drafted at its path (§8); **§9's B-RECLAIM-OWN**, its lines quoted in the draft's §3; then **G-PRINT on the report**, from the session: `/root/tz04a-env/venv/bin/python -B /root/liq-guard-svc/liq-guard.py scan /root/btc-5m-twap/CryptoReports/TZ-55-liq-guard-v2-report.md` must print `G-PRINT PASS` — the Executor gives its two lines to the Boss in the chat, since the report cannot quote a scan of itself — and only then the report committed and pushed to `main`. A FAIL: the report is written again without what was found, and scanned again.

---

## 4. Gates — fixed here, before any of their data exists

| gate | step | PASS |
|---|---|---|
| READY | §0.0 | `ready=1` |
| STAGE | §0.1 | four lines `created`, each at its SHA-256 |
| FINGERPRINT | §0.2 | the line §0.2 quotes |
| HOST | §0.3 | H1 to H5 |
| NUMBER and REFS | §0.4 | `NUMBER PASS - 2 of 2`; no branch of this TZ on `origin` |
| BRANCH | §3 step 6 | one file `created` and two `replaced the first version`, each at its SHA-256; the push on `origin` at `HEAD`; the numstat's three lines exactly |
| C-SELF | §3 step 7 | `141` of `141`, the hook's refusals `5` |
| G-SELF | §3 step 7 | `SELFTEST PASS: 127 checks` |
| SCRATCH | §3 step 8 | every directory named earlier reclaimed and gone; none named live touched |
| SECRETS | §3 step 9 | five required credentials `kept`; `hc-url` kept, written or skipped; each side token written or skipped; `exit=0`; `/etc/liq-guard` `0700`, its files `0600`, root's |
| G-FIRST | B-DEPLOY 1 | the first version installed at TZ-54's two hashes, or the second installed and active |
| G-MEM | B-DEPLOY 2 | `MemAvailable` at or above `100,663,296` at one of five reads |
| G-STAGE | B-DEPLOY 3 | the second's two files at §0.1's SHA-256 in `inst`, the first's two at TZ-54's in `first` |
| G-PROVE | B-DEPLOY 4 | `PROVE PASS: 11 gates of 11 passed`, its record `"pass": true` with this code's SHA-256 — G-CRED, G-TIME, G-KEY, G-POS, G-BRACKET, G-PUSH, G-TG, G-SEE, G-LOOK, G-ALARM, G-HC, in this order, each `PASS` (§1.7) |
| G-INSTALL | B-DEPLOY 5 | both files at §0.1's SHA-256 in `/root/liq-guard-svc/`, the unit file equal by `cmp`, `loaded`, `enabled` |
| G-UNIT | B-DEPLOY 6 | `60` s after `restart`: `active`, `running`, `NRestarts` `0`, `enabled`, `WatchdogUSec` `5min`; `key_ok` `True`, `blind` `False`, `polls_ok` at least `1`; its line `SERVE start: key True, positions read N`; `service.log` `600` |
| G-LIVE | B-DEPLOY 7 | `900` s after the start: `active`, `NRestarts` `0`, the same `MainPID`; `key_ok` `True`, `blind` `False`, `polls_ok` at least `150` — `180` passes of `5` s, a sixth of them spare — and `disk_faults` `0` |
| G-DEPLOY | §3 step 10 | `B-DEPLOY END exit=0` |
| G-AFTER | §3 step 11 | the unit `active`, `NRestarts` `0`; its files at §0.1's SHA-256; `service.log` `0600`; `prove.json` `"pass": true` |
| G-PRINT | §3 steps 12 and 13 | `G-PRINT PASS` on every log, and on the report before it is committed |

**Every gate is asserted where it is read** — in the checker, the guard or B-DEPLOY, which exit non-zero — or read by the Executor against the literal above; **a gate read by eye is named so in the report**. A FAIL is BLOCKED but where §3 step 10 allows one more B-DEPLOY.

---

## 5. The files

**Appendix A — `guard/liq-guard.py`**, the second version, fixed by the Architect and written byte for byte; standard library alone. Its sections: the constants (lines 53 to 128); files and credentials (lines 147 to 238); the network, IPv4 alone, and its clients — Binance, Pushover, Telegram, healthchecks.io and systemd's notify socket (lines 243 to 458); the readings, pure functions (lines 463 to 706); the texts, pure functions, HTML for Telegram and Pushover (lines 711 to 985); the guard's pass, `Guard` (lines 990 to 1627); the modes — `secrets`, `find-chat`, `prove`, `status`, `scan`, `serve` — and `refuse` (lines 1636 to 2045); the self-test's stand-ins, `binance_lp` and `on_terminal` (lines 2050 to 2218); the self-test (lines 2221 to 2754); `main` (lines 2757 to 2768). **Exits:** `0` done; `1` a failed assert or a BLOCK; `2` refused — a key that can do more than read, or a credential missing or malformed — which its unit does not restart; `4` a reading's FAIL. **Appendix B — `deploy/systemd/liq-guard.service`**, installed byte for byte (§1.9). **Appendix C — `b-deploy.sh`**, staged and never committed (§3 step 10). **`research/tz55-liq-guard-v2.py`** — §0.1's checker. **Read by the Architect for this TZ:** the first version, Appendix A of TZ-54, from which `parse_positions`, `distance_pct`, `crossed`, `step`, `bracket_for`, `margin_hint`, `key_reading`, `Scrub`, `Net`, `Binance`, the file helpers and `secrets`, `find-chat` and `scan` are kept, `parse_positions` reading four more fields — `entryPrice`, `unRealizedProfit`, `leverage` and `positionInitialMargin`.

---

## 6. Cost

At the populations' upper bounds (§10 C4): the guard's `selftest` under `1` s — `0.23` to `0.35` s at the Architect's runs, its peak `31,624` to `32,556` KiB with its pseudo-terminal children; the checker's `selftest` about `1` s — `0.71` s — its peak `35,160` KiB at the Architect's run under Python 3.12; `fingerprint` under `1` s over 73 rows; `number`, `refs`, `scratch` about `1` s each; `reclaim` under `2` s over at most `50,000,000` bytes; `scan` under `1` s over the logs. **B-DEPLOY:** the memory's reads at most `300` s; the copies and the first's stop under `30` s; G-PROVE's requests under `30` s beside its three waits of at most `900` s each — the Boss's two answers and his acknowledgement; G-UNIT `60` s; G-LIVE `900` s from the start — **at most about `4,100` s**, under its unit's `RuntimeMaxSec`, `7,200`; **the positions unwatched for G-PROVE's span alone, at most `2,730` s and in practice the minutes he takes to answer.** **No check reaches `3,600` s of compute.** **The unit:** `MemoryMax` `96` MiB against the guard's peak under `40` MB; on disk its journal at most about `2,000` lines a day — a tick every `10` minutes, a repeating error once a minute at most, the stages, records, retreats, calls and commands — about `500,000` bytes a day at the worst and `90` days kept, so under `50,000,000` bytes, and `memory.json` a few hundred bytes a position, against map §6's disk margin of `2,797,417,277` at TZ-50's read; at Binance, `60` request weight a minute of its `2,400`; at Telegram, one `getUpdates` a pass and at most one edit a watched position every `10` s; at Pushover, at most `20` messages an hour (`PUSH_PER_HOUR`, line 83) and one receipt read every `10` s an open call. Fail-fast bounds, each the first version's and unchanged: `TIMEOUT_S` `10`, `COOLDOWN_S` `15`, `BLIND_S` `120`, `SEE_WAIT_S` and `TEST_WAIT_S` `900`; and this version's: `ENGAGE_S` `600` — a top-up's minutes, transfers included, with room; `LAST_QUIET_S` `180` — no margin seen for three minutes at the last line is a sleeper, not a slow hand; `LIVE_EDIT_S` `10` — two passes, Telegram's limit for edits a chat far above it.

---

## 7. Validation

**The guard's self-test, `127` checks, fixed by the Architect as this TZ's Validation** (`mode_selftest`, lines 2227 to 2754), each an `assert` that ends the run. **Kept from the first version:** the margin hint against Binance's own liquidation formula — now at `8`% and at `5`%, with the target's liquidation price — and no hint beyond it; both sides' distances; **the stages over a descent of thirteen reads** — `[0, 1, 0, 2, 0, 3, 0, 0, 3, 0, 3, 0, 1]` — and the one-point re-arm; the positions of v3 and v2 replies, now with their entry and leverage, and the ROE; the brackets; **the key's permissions — read-only and bound accepted, five widenings, an unbound key and a missing field each refused**; the commands, the thresholds, the target, the gains' start and the settings kept or defaulted; the notation; the scrub; **every connection IPv4 alone**; the cooldown; **`secrets` at a real pseudo-terminal**, now with a side token written and the other skipped; `find-chat`; **`prove`'s eleven gates**, the examples through their applications, **the dead-man kept quiet through the waits and pinged last**, an answer «нет» failing G-SEE before any example, **a «нет» to the examples failing G-LOOK**, a key that can trade refused, v2 where v3 is not served; **the cycle** — a descent calling once a stage, stage 1 at high priority and 2 and 3 at emergency, **the last stage's call through «Сторож» where no short application is**, its live card and its button; **acknowledged: at work, the other call cancelled, the card edited; silent under the last line within three minutes, then one call; margin added — the card's last edit, a quiet ✅, the work over**; «Я в деле» from his chat alone, a stranger's button ignored; **ten minutes on with the danger still there, called again**; **a long's records and retreats, titles and sounds exact, through its own application; the memory written and a restart telling nothing again; a record held while he works and told quietly after**; the commands from the pinned chat alone, a stranger's thresholds ignored; the test call acknowledged; the settings kept; gains off; a `429` holding reads back; **blindness alarmed once and reminded, one step failing beside it**, seen again; **a full disk stopping no alarm**; Pushover down and the call sent once it is up; Telegram down with its queue bounded and sent five a pass; the heartbeat once a day and quiet; a key widened later refused; **no credential or chat id in any file of the record**, every file `0600`; the watchdog notified; no host but the five; **every message sent and every edit well-formed HTML**; and `scan`. **The texts** — every card and call checked for its colour first, its HTML balanced, and its length within Telegram's `4,000` and Pushover's `250` and `1,024`. **The Architect's runs on these bytes:** `SELFTEST PASS: 127 checks` under Python 3.12 — the host's — and 3.13; and the self-test **fails** on each of ten mutations of the code — the sides' colours swapped, a retreat at a quarter of the peak, margin added unseen on a short, the last line rung at once, a stranger's button accepted, every side through «Сторож», no call at the timeout, gains not held while he works, a card's bold left open, and an acknowledged call ignored. **B-DEPLOY** was read line by line against its gates; `bash -n` passes. **The mockup the Boss was sent is drawn from these functions' own output** — `liq_card`, `liq_push`, `record_card`, `record_push`, `pullback_card`, `pullback_push`, `status_card` and `settings_card` on example positions — so what he approved is what the code sends. **The checker's** `fingerprint` printed §0.2's line on a copy of `main` with pull request #52's merge and this map revision, and its self-test `141` of `141`.

---

## 8. The report

`CryptoReports/TZ-55-liq-guard-v2-report.md`, contract §8's sections in their order. **§2 Measurements:** the readiness and host gate's lines but the counted address; every log's gate lines as printed; the B-DEPLOY log whole; `prove.json` whole; the unit's state after; `status`'s lines; `MemAvailable` at each read; **the instants of the first version's stop and the second's start, and the span between them**; the instants of the Boss's «готово», his two answers and his acknowledgement as the logs carry them. **§3:** the branch, its commit, the pull request, the numstat, contract §4.2's self-check, and `b-deploy.sh`'s SHA-256 with its forensic copy. **§4:** every gate of §4, `PASS` or `FAIL`, asserted or read by eye. **§6:** every departure, every refusal by the classifier with its block, its words and who ran it, every block the Boss ran with its instant, and B-RESET and the second B-DEPLOY where they ran. **The report prints no credential, chat id, address of this host, or symbol, price, size or margin of the Boss's positions** — G-PRINT reads it before it is committed.

---

## 9. Reclaim — the host left clean (CANON hard rule 15)

**B-RECLAIM-OWN**, with the report drafted and before G-PRINT reads it (§3 step 13). **Its output is written to no file; the report's §3 quotes it verbatim from the session**, every line of it:

```
(cd /root/tz55-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz55-work/wt/research/tz55-liq-guard-v2.py reclaim /root/tz55-work); echo "reclaim exit=$?"
cd /root/btc-5m-twap && git -C /root/btc-5m-twap worktree remove /root/tz55-work/wt; echo "exit=$?"
rm -rf /root/tz55-work; echo "exit=$?"
test -e /root/tz55-work; echo "exit=$?"
git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
find /root/btc-forensics -type f | wc -l
df -B1 --output=source,size,avail /var/lib/btc-recorder
```

`reclaim` must print `RECLAIM PASS` before the removals: it copies every regular file of `/root/tz55-work` but the worktree's and the checker's temporary tree's — the logs, the stage's four files, B-DEPLOY's `inst` and `first` copies — into `/root/btc-forensics/` as `tz55-work--<path with / as -->`, by exclusive create, its hash verified, free space at or above `7,400,000,000` after each copy. **No file of this run is held by a Release** (map §7 item 167). The last `test -e` must print `exit=1`. **Its paste**, where the classifier refuses any line: the same lines chained with `&&`, the removals reached only after `RECLAIM PASS`. **Kept on the host — the guard's:** `/root/liq-guard-svc/`, `/var/lib/liq-guard/`, `/etc/liq-guard/` and the enabled unit.

---

## 10. Pre-send checks

Performed on this file as sent, in a reading separate from its writing; every count below re-derived for it.

| # | check | result |
|---|---|---|
| **C1** | scope against body | **Named by the body, each inside §2.** *Repository, written:* the branch's three files — two replaced, one new — and its pull request, the report on `main` — §2 item 1. *Read:* this file by §0.1's script, `research/tz54-liq-guard.py` by `git show`, `SYSTEM-MAP.md` and its §0 table's 73 rows' files — `docs/l1-sign.html` among them — by `fingerprint`, `CryptoTZ/` and `CryptoReports/` by `number`, the refs by `refs` — §2 item 1. *Capture host, written:* `/root/tz55-work/**` with `wt`, `inst`, `first`, `selftest-tmp` and the worktree's record; the guard's self-test's tree under `/tmp`; `/root/liq-guard-svc/`'s two files and the unit file, replaced or put back; `/var/lib/liq-guard/`'s `prove.json`, `memory.json`, `state.json`, `journal/` and `service.log`'s mode; the two side tokens by `secrets`; the transient unit; the forensic store's `tz55-work--*`; earlier session directories — §2 item 2, B-RESET's removal its named exemption. *Read:* `/proc`, `df`, the recorder's store by `find` and `grep -c`, five units' `systemctl show`, `ip -4` counted, the installed files by `sha256sum`, `cmp`, `ls` and `stat`, `/etc/liq-guard` by `ls` and the guard's modes, four fields of `state.json` and two of `prove.json` by B-DEPLOY, `prove.json` and `service.log`'s tail by §3 step 11 — §2 item 3. *Network:* the written authorization's and GitHub's — §2 item 4. **Intersections found and resolved:** the host gate's reads of other units and of the recorder's store against §2 item 5's "not changed" — §2 item 5's named exemption; **the first version's `status` in §0.3 and B-DEPLOY's `status` read the journal to count its events, against the first draft's "never the journal" in §2 item 3 — rewritten: the journal and `memory.json` by the guard's modes alone, which print neither.** **By content class:** an output carrying a credential, the chat id, the host's address or a position's figure — the guard's messages to the Boss's chat and phone carry positions and are named in §2 item 6 as the product; `memory.json` and the journal carry them and are read by the guard's modes alone; `prove`, `status`, `secrets`, `scan`, `ls` and B-DEPLOY print counts, names, sizes, booleans, settings and states alone (§1.8); G-PRINT reads every log and the report. **No other intersection.** |
| **C2** | origin of every expectation | **Computed by an implementation independent of the one under test:** the four files' and the base's lines, bytes and SHA-256 — `wc` and `sha256sum` over the bytes, and §0.1's script run by the Architect against this file: on `stage`, four lines `created`, again `equal, kept`; on `branch` over TZ-54's two files, one `created` and two `replaced the first version`; the numstat's `3 2`, `1201 279` and `3323 0` — `git diff --numstat --diff-algorithm=myers` in a scratch repository between TZ-54's files and these, histogram's `1202 280` beside it the reason the algorithm is named; **`127` checks — counted by a profiler outside the self-test's own counter, `127` calls of `check`**; the stages `[0, 1, 0, 2, 0, 3, 0, 0, 3, 0, 3, 0, 1]` and the gains' `["-", "record", "-", "record", "-", "-", "pullback1", "-", "pullback2", "-", "record"]` — derived by hand, read by read, from `5`, `3`, `1.5` and the one-point re-arm, and from `7`, `next_record` and a third and a half of the peak; the hint's `8`% and `5`% — the self-test's `binance_lp`, Binance's closed formula, against `margin_hint`; `31 bytes` — a side token's form, thirty characters, and `secrets`'s newline. **Quoted from a committed artifact:** the fingerprint line's revision and its `73`, `70`, `2`, `1` — map §0 of revision `2026-11-21-e`, which the checker's `fingerprint` printed on a copy of `main` with pull request #52's merge; `141` of `141` and `refused by the hook: 5` — TZ-54's report, its lines 16 and 343; the first version's two hashes, lines and bytes — map §0's rows; `7,400,000,000` — the checker's `RECLAIM_FLOOR`, its line 295, and map §6; `100,663,296` — Appendix B's `MemoryMax=96M`; `21,970,944` — map §6, memory; the map's `MemAvailable` range and disk margin — map §6. **Inequalities, holding for every admissible value:** `polls_ok` at least `150` in `900` s at `5` s a pass; `MemAvailable` at or above its floor. **No expectation depends on a quantity this TZ measures.** |
| **C3** | shape of every diff | **Not additive:** `guard/liq-guard.py` and `deploy/systemd/liq-guard.service` are on `main` since pull request #52's merge, and this TZ replaces them whole — by myers' diff `279` and `2` of the first version's lines go, `1201` and `3` come; the header's comment and `Description=` lines, and `UMask=0077` inserted, are the unit file's. `research/tz55-liq-guard-v2.py` is new: none replaced. **The words "insertions only" appear nowhere in this file.** |
| **C4** | cost of every check | §6, at the populations' upper bounds: the self-tests under `1` s, the checker's modes about `1` s over `73` rows, `reclaim` under `2` s over at most `50,000,000` bytes, `scan` under `1` s over the logs; B-DEPLOY at most about `4,100` s, almost all of it waits for the Boss — three of at most `900` s — and G-LIVE's `900` s; the positions unwatched at most `2,730` s, G-PROVE's span. **No check reaches `3,600` s of compute.** Each fail-fast bound derived beside it in §6; §3 step 10's `3,300` s is G-PROVE's three waits and a read's `570`. |
| **C5** | every count | `four` staged files and `three` on the branch — §0.1's `FILES`; `five` required credentials `kept` and `three` optional — Appendix A's `CREDENTIALS`, eight rows, five `True`; `eleven` gates — `PROVE_GATES`; `H1` to `H5` — §0.3's five bullets; `seven` commands in H5 — `ip`, `df`, `systemd-run`, `install`, `cmp`, `sha256sum`, `stat`; `five` reads of memory — B-DEPLOY's loop `1 2 3 4 5`; `three` waits of `900` s — G-SEE, G-LOOK and G-ALARM; `ten` mutations — §7's list; `73` rows of map §0; `127` and `141` checks. Each re-derived from the set it counts. |
| **C6** | every population | `polls_ok` — the second version's passes since its start, read at `60` s and `900` s; `disk_faults` — its writes since its start; `MemAvailable` — five reads a minute apart at B-DEPLOY's step 2; `scan` — every `.log` under `/root/tz55-work/logs/`, then the report; `fingerprint` — map §0's `73` rows; `reclaim` — every regular file of `/root/tz55-work` but `wt` and `selftest-tmp`; `scratch` — the UUID directories beside this session's own; G-POS and G-SEE — every position `positionRisk` serves at the prove's instant; G-LOOK — the two examples; the live card's edits — the watched positions, each at most every `10` s. |
| **C7** | every signature and every behaviour | **The checker, read in its staged bytes — TZ-54's at `fd8f8c21…` with §0.1's edits, which change no line's number:** `def mode_fingerprint():`, lines 1087 to 1122, printing `FINGERPRINT PASS: revision %s; anchors 6 of 6, 4 re-derived; rows %d: frozen %d of %d equal, tracked %d, reported %d; …` at line 1119; `def mode_number():`, lines 1125 to 1133, `NUMBER %s` `PASS - 2 of 2` at line 1131; `def mode_refs():`, lines 1136 to 1147, `assert not branch, "BLOCKED: refs/heads/%s exists on origin already"` at line 1146; `def mode_scratch(own):`, lines 1231 to 1245; `def mode_reclaim(trees):`, lines 1264 to 1311, `RECLAIM PASS` at line 1309; `RECLAIM_FLOOR = STREAM_FLOOR + 100000000`, line 295; `MAP_REVISION = "2026-11-21-e"`, line 88; `MAP_ROWS = {"frozen": 70, "tracked": 2, "reported": 1}`, line 94; `WORK = "/root/tz55-work"`, line 103. **Appendix A's own:** 66 references of the form `name`, lines a to b, or `NAME`, line n, **each filled from Appendix A's syntax tree** — a definition's span or an assignment's line — so none can name lines its definition does not hold. **Each behaviour §1 attributes to the guard is pinned by a self-test check §7 names** and run on these bytes: the colours and the side's application (§1.2), the stages' priorities and sounds, the hint, the link and the live card (§1.3), the work, its exits and the last line (§1.4), the records, the retreats, the memory and gains off (§1.5), the cards, buttons and commands (§1.6), the prove's eleven gates and the dead-man through its waits (§1.7), and the record's privacy (§1.8). **Pushover's behaviours** — high priority bypassing quiet hours, emergency's `retry` of at least `30` and `expire` of at most `10,800`, the `html`, `sound`, `url` and `url_title` fields, the tags stripped from the lock screen's banner and the application's icon shown with each message — **are read from Pushover's API page and support pages by the Architect on 2026-11-21, not measured;** G-LOOK is the measurement on the Boss's phone. **Telegram's** `editMessageText`, `answerCallbackQuery`, `parse_mode` `HTML`, `blockquote expandable` and `link_preview_options` are the Bot API's, read, not measured; G-TG, G-SEE and G-LOOK send them. |
| **C8** | every cross-reference | **This file:** §0.0 to §0.4, §1.1 to §1.10, §2 items 1 to 6, §3 steps 1 to 13, §4, §5, §6, §7, §8, §9 and §10 — each reference resolved to the text it names. **CANON `2026-11-21-b`:** hard rules 2, 5, 14, 15 and 17; PART V's tool "judged against his trading without it"; PART VII's guard paragraph — "It never adds margin, opens or closes" — each read in the file and supporting its sentence. **The map, revision `2026-11-21-e`:** §0 and its table, §1, §3's units and trees, §6's eleven rows the header names — each cited by a sentence of the body, `process supervision` and `egress` in §1.9 and §2 item 4 — and §7 items 86, 91, 95, 115, 118, 137, 138, 144, 167, 174, 176, 195, 196 and 197, each read in full; **items 115 and 176, in the header from TZ-54's list and cited by no sentence in the first draft, now cited by §1.9.** **The contract:** §1 steps 1 to 4, §4.2, §5, §8 and §10. **The Boss's own words, compared with his message's file character by character:** "If the price rises above the entry point by 7%", "naturally green for LONG and red for SHORT, so that I do not miss the moment of maximum profit!", "Adding margin to move liquidation 5% away from the price!", "Three-stage alerts." and "when I acknowledge an alert (press it), it means I have engaged in the process, and at that moment, no on-screen calls should distract me" — each a substring of it; **the first draft's "…the price! Three-stage alerts." joined two of his lines with a space, and is quoted as two.** |

---

## Appendix A — the guard, byte for byte

### `guard/liq-guard.py`

```python file=guard/liq-guard.py
#!/usr/bin/env python3
"""liq-guard.py - the liquidation guard, its second version (TZ-55, CANON PART VII): the Boss's Binance USD-M futures
positions read every five seconds through a key that can read and nothing else. For each position, two things:
its distance from the mark price to the liquidation price, held against his three stages - a loud notice, Pushover's
emergency alarm, a last alarm - each with the margin that moves the liquidation price to his target; and its gain from
the entry price - told from his threshold on, at each new record, and when the price gives back a third and a half of
the record. An alarm he acknowledges, or the card's «Я в деле», silences every call about that position while he
works, and its card in Telegram updates itself; margin he adds is seen and confirmed. Every message about a position
opens with its side's colour - green for a long, red for a short - and goes through that side's own Pushover
application where he made one. The guard's own loss of Binance is alarmed too. It never trades and holds no key that
can. Standard library only; every connection IPv4, because the key is bound to the host's IPv4 address.

Modes:
    secrets     the Boss, at his terminal: each credential not yet on the host - the Binance key and secret, the
                Pushover user key and the three application tokens, the Telegram token, the dead-man's ping address -
                each hidden, each written once, 0600, root's; the optional ones may be skipped
    find-chat   the one private chat that sent /start to the guard's bot, pinned
    prove       every request path proved through this file's own functions, the key's permissions read, what the
                guard sees and how its alerts look confirmed by the Boss, and a test alarm acknowledged on his phone
                (CANON hard rule 14); its record prove.json
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
import html
import http.client
import json
import math
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
DEFAULT_THRESHOLDS = (5.0, 3.0, 1.5)   # percent of the mark price: the three stages; the Boss's own are kept
REARM_PP = 1.0                # a stage re-arms once the distance is this many points above its threshold
TARGET_PCT = 5.0              # the distance the margin hint aims the liquidation price at - the Boss's; «Цель N»
PROFIT_FROM = 7.0             # the gain from the entry, percent of the price, from which records are told; «Прибыль N»
RECORD_STEP_PP, RECORD_STEP_X = 3.0, 1.25   # the next record: 3 points above the last told, or a quarter, the larger
PULLBACK_MIN_PP = 2.0         # a retreat is told once a third of the peak gain is given back, and at least this
ENTRY_MOVE = 0.001            # an entry price moved by this share - margin averaged in - is a new position's gains
ENGAGE_S = 600                # an acknowledged alarm or «Я в деле»: no call about that position for this long
LAST_LINE_PCT = 1.0           # while he works: one alarm at this distance, or the third stage where it is lower ...
LAST_QUIET_S = 180            # ... where no margin has been seen added for this long
TOPUP_REL = 0.002             # a liquidation price moved away by this share of itself is margin added
LIVE_EDIT_S = 10              # a live card is edited at most this often
TREND_S, HIST_S = 300, 900    # the trend shown is over five minutes; fifteen are kept
ALARM_RETRY_S, ALARM_EXPIRE_S = 30, 3600       # Pushover's emergency priority: its minimum retry, an hour
TEST_EXPIRE_S, TEST_WAIT_S, RECEIPT_EVERY_S = 900, 900, 10
PUSH_PER_HOUR = 20
OUTBOX_TRIES = 10
OUTBOX_MAX = 100             # Telegram messages beyond this, oldest first, are dropped; alarms never
TG_PER_PASS = 5              # Telegram messages sent in one pass; the rest wait for the next
COOLDOWN_S = 15              # a host that failed at the network is not tried again for this long
HEARTBEAT_UTC = (19, 0)       # 23:00 in Batumi
LOCAL = dt.timezone(dt.timedelta(hours=4))     # Batumi: UTC+4, no daylight saving
FIND_CHAT_S = 1800
PROVE_GATES = ("G-CRED", "G-TIME", "G-KEY", "G-POS", "G-BRACKET", "G-PUSH", "G-TG", "G-SEE", "G-LOOK", "G-ALARM",
               "G-HC")
SEE_WAIT_S = 900             # each of the Boss's answers at prove
LONG_POLL_S = 25             # Telegram's long poll in find-chat and prove; their sockets wait 40 s
YES, NO = ("да", "yes", "совпадает"), ("нет", "no", "не совпадает")
READ_PERMS = ("enableReading", "enableFixReadOnly")
CORE_PERMS = ("enableReading", "ipRestrict", "enableWithdrawals", "enableFutures", "enableSpotAndMarginTrading")
SOUND = {"liq1": "spacealarm", "liq2": "siren", "liq3": "persistent", "record": "cashregister", "pullback": "falling",
         "blind": "mechanical", "test": "siren", "sample": "pushover"}
BINANCE_URL = "https://www.binance.com/ru/futures/%s"
DOT = {"LONG": "🟢", "SHORT": "🔴"}
STAGE = {1: ("⚠️", "Ликвидация близко"), 2: ("🚨", "Тревога"), 3: ("🆘", "Последний рубеж")}
LABEL = {"binance-key": "ключ Binance", "binance-secret": "секрет Binance", "pushover-user": "User Key Pushover",
         "pushover-token": "токен Pushover", "tg-token": "токен бота", "hc-url": "адрес пинга",
         "pushover-long": "токен «Сторож LONG»", "pushover-short": "токен «Сторож SHORT»"}
KEYBOARD = {"keyboard": [[{"text": "Статус"}, {"text": "Тест"}], [{"text": "Настройки"}, {"text": "Помощь"}]],
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
    ("pushover-long", r"[A-Za-z0-9]{30}", False,
     "Pushover — API Token приложения «Сторож LONG» (зелёная иконка), или Enter — без него (ввод скрыт): "),
    ("pushover-short", r"[A-Za-z0-9]{30}", False,
     "Pushover — API Token приложения «Сторож SHORT» (красная иконка), или Enter — без него (ввод скрыт): "),
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

    def send(self, title, message, priority, expire=ALARM_EXPIRE_S, sound=None, url=None, url_title=None, html=True):
        fields = {"token": self.token, "user": self.user, "title": title[:250], "message": message[:1024],
                  "priority": priority}
        if html:
            fields["html"] = 1
        if sound:
            fields["sound"] = sound
        if url:
            fields.update(url=url[:512], url_title=(url_title or url)[:100])
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

    def send(self, chat, text, quiet=False, buttons=None):
        """A message in HTML; with `buttons`, an inline keyboard of them, else the chat's own keyboard."""
        return self.call("sendMessage", chat_id=int(chat), text=text[:4000], parse_mode="HTML",
                         disable_notification=bool(quiet), link_preview_options={"is_disabled": True},
                         reply_markup={"inline_keyboard": buttons} if buttons else KEYBOARD)

    def edit(self, chat, message_id, text, buttons=None):
        """A message of the bot's edited in place - no notification; a text unchanged is no fault."""
        params = dict(chat_id=int(chat), message_id=int(message_id), text=text[:4000], parse_mode="HTML",
                      link_preview_options={"is_disabled": True})
        if buttons:
            params["reply_markup"] = {"inline_keyboard": buttons}
        try:
            return self.call("editMessageText", **params)
        except Refused as e:
            if "not modified" in str(e.words):
                return None
            raise

    def answer(self, callback_id, text):
        return self.call("answerCallbackQuery", callback_query_id=str(callback_id), text=text[:200])


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
    notional, isolated or not; the entry price, the unrealized profit and the leverage - v2's own field, or v3's
    notional over its position's initial margin. Pure."""
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
        notional = abs(notional) if notional is not None else abs(amt) * (mark or 0.0)
        entry, lev, pim = num(e.get("entryPrice")), num(e.get("leverage")), num(e.get("positionInitialMargin"))
        if not lev and pim and pim > 0 and notional > 0:
            lev = notional / pim
        found.append({"symbol": e["symbol"], "side": side, "key": "%s:%s" % (e["symbol"], side), "qty": abs(amt),
                      "mark": mark, "liq": num(e.get("liquidationPrice")), "notional": notional,
                      "isolated": (num(e.get("isolatedWallet")) or 0.0) > 0 or e.get("marginType") == "isolated",
                      "entry": entry if entry and entry > 0 else None, "upnl": num(e.get("unRealizedProfit")),
                      "lev": max(1, int(round(lev))) if lev and lev > 0 else None})
    return found


def distance_pct(p):
    """Percent of the mark price between it and the liquidation price, on the side that loses; None where there is
    no liquidation price. At or under 0 the mark is at or past it. Pure."""
    mark, liq = p.get("mark"), p.get("liq")
    if not mark or mark <= 0 or liq is None or liq <= 0:
        return None
    return 100.0 * ((mark - liq) / mark if p["side"] == "LONG" else (liq - mark) / mark)


def crossed(d, th):
    """The highest stage whose threshold `d` is at or under: 3, 2, 1, or 0. Pure."""
    for lvl, t in ((3, th[2]), (2, th[1]), (1, th[0])):
        if d <= t:
            return lvl
    return 0


def step(fired, d, th, rearm=REARM_PP):
    """(the stage to announce now, or 0; the stages announced in this descent after this read). A stage re-arms once
    `d` is above its threshold by `rearm` points; a read that crosses several stages at once announces the highest
    alone and counts the lower ones announced; no liquidation price re-arms every stage. Pure."""
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


def target_price(p, target):
    """The liquidation price `target` percent from the mark, on the side that loses. Pure."""
    return p["mark"] * (1 + target / 100.0) if p["side"] == "SHORT" else p["mark"] * (1 - target / 100.0)


def gain_pct(side, entry, price_):
    """The gain from the entry price at `price_`, percent of the entry, on the position's side. Pure."""
    return 100.0 * (price_ / entry - 1.0) if side == "LONG" else 100.0 * (1.0 - price_ / entry)


def roe_pct(p):
    """The unrealized profit over the position's initial margin at its entry, as Binance's app shows ROI; None where
    a figure is missing. Pure."""
    if p.get("upnl") is None or not p.get("entry") or not p.get("lev"):
        return None
    im = p["qty"] * p["entry"] / p["lev"]
    return 100.0 * p["upnl"] / im if im > 0 else None


def next_record(rec):
    """The gain the next record is told at, after one told at `rec`. Pure."""
    return max(rec + RECORD_STEP_PP, rec * RECORD_STEP_X)


def profit_step(m, p, t, start):
    """(the position's profit memory after this read, its events). The memory holds its side, the entry it was
    counted from, its best price since and when, the last record told and the retreats told since. A record is told
    once the gain reaches `start`, then each next_record above the last told; a retreat once the gain falls a third of
    the peak, at least PULLBACK_MIN_PP, below it - stage 1 - and once to half the peak - stage 2 - each once a record,
    the highest of a jump alone. An entry moved by ENTRY_MOVE, or a side changed, starts the memory again. `start` 0
    tells nothing. Pure."""
    e, mark = p.get("entry"), p.get("mark")
    if not e or e <= 0 or not mark or mark <= 0:
        return m, []
    if m is None or m.get("side") != p["side"] or abs(m.get("entry", 0.0) - e) > ENTRY_MOVE * e:
        m = {"side": p["side"], "entry": e, "best": mark, "best_t": t, "rec": None, "pb": 0}
    else:
        m = dict(m)
    if (mark > m["best"]) if p["side"] == "LONG" else (mark < m["best"]):
        m["best"], m["best_t"] = mark, t
    if not start:
        return m, []
    g, gp = gain_pct(p["side"], e, mark), gain_pct(p["side"], e, m["best"])
    if g >= (start if m["rec"] is None else next_record(m["rec"])) - 1e-9:
        m["rec"], m["pb"] = g, 0
        return m, [{"kind": "record", "gain": g, "next": next_record(g)}]
    if m["rec"] is None or gp <= 0:
        return m, []
    first = gp - max(PULLBACK_MIN_PP, gp / 3.0)
    stage = 2 if g <= min(gp / 2.0, first) else 1 if g <= first else 0
    if stage > m["pb"]:
        m["pb"] = stage
        return m, [{"kind": "pullback", "stage": stage, "gain": g, "peak": gp, "given": 100.0 * (gp - g) / gp}]
    return m, []


def topup_seen(side, liq0, liq):
    """True where the liquidation price moved away from where it was by TOPUP_REL of itself - margin added. Pure."""
    if not liq0 or not liq or liq0 <= 0 or liq <= 0:
        return False
    return liq >= liq0 * (1 + TOPUP_REL) if side == "SHORT" else liq <= liq0 * (1 - TOPUP_REL)


def last_line(th):
    """The distance under which a call goes even while the Boss works. Pure."""
    return min(LAST_LINE_PCT, th[2])


def then_of(hist, t, i):
    """(the value at index `i` about TREND_S before `t`, its age in whole minutes) from a position's history of
    (instant, distance, gain), among samples at least 60 s old; None where there is none. Pure."""
    old = [h for h in hist if t - h[0] >= 60 and h[i] is not None]
    if not old:
        return None
    h = min(old, key=lambda h: abs(t - h[0] - TREND_S))
    return h[i], max(1, int(round((t - h[0]) / 60.0)))


def arrow(now, then, eps=0.05):
    """The direction from `then` to `now`. Pure."""
    return "↗" if now - then > eps else "↘" if now - then < -eps else "→"


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
    """(command, arguments) of a chat message, or (None, words). Pure."""
    words = (text or "").strip().lower().replace("ё", "е").split()
    if not words:
        return None, []
    w = words[0].lstrip("/").split("@")[0]
    names = {"статус": "status", "status": "status", "тест": "test", "test": "test", "пороги": "thresholds",
             "thresholds": "thresholds", "помощь": "help", "help": "help", "start": "help", "настройки": "settings",
             "settings": "settings", "цель": "target", "target": "target", "прибыль": "profit", "profit": "profit"}
    return names.get(w), words[1:]


def number_of(word):
    try:
        return float(word.replace(",", "."))
    except ValueError:
        return None


def thresholds_of(args):
    """Three thresholds from a message's words, `5 3 1,5`, or None: each a number, 0 < third < second < first <= 30.
    Pure."""
    if len(args) != 3:
        return None
    w, a, c = (number_of(x) for x in args)
    if None in (w, a, c) or not (0 < c < a < w <= 30):
        return None
    return (round(w, 2), round(a, 2), round(c, 2))


def target_of(args):
    """The margin hint's target from `5`, or None: one number, 1 to 30. Pure."""
    v = number_of(args[0]) if len(args) == 1 else None
    return round(v, 2) if v is not None and 1 <= v <= 30 else None


def settings_of(st):
    """(thresholds, target, profit start) from a state.json's document, each its default where absent or not of its
    form. Pure."""
    th, tg, pf = st.get("thresholds"), st.get("target"), st.get("profit_from")
    th = tuple(th) if isinstance(th, list) and thresholds_of([str(x) for x in th]) else DEFAULT_THRESHOLDS
    tg = tg if isinstance(tg, (int, float)) and not isinstance(tg, bool) and target_of([str(tg)]) is not None \
        else TARGET_PCT
    pf = pf if isinstance(pf, (int, float)) and not isinstance(pf, bool) and profit_of([str(pf)]) is not None \
        else PROFIT_FROM
    return th, tg, pf


def profit_of(args):
    """The records' start from `7`, `0` or `выкл`, or None: 0 is off, else 3 to 100. Pure."""
    if len(args) == 1 and args[0] in ("выкл", "off"):
        return 0.0
    v = number_of(args[0]) if len(args) == 1 else None
    return round(v, 2) if v is not None and (v == 0 or 3 <= v <= 100) else None


# ---- the texts: pure functions, HTML for Telegram and Pushover -----------------------------------------------------

def esc(x):
    return html.escape(str(x), quote=False)


def ru(x, d):
    s = "{:,.{}f}".format(x, d)
    return s.replace(",", " ").replace(".", ",").replace("-", "−")


def price(x):
    """A price in Russian notation, to about six significant digits. Pure."""
    if x is None:
        return "—"
    a = abs(x)
    d = 1 if a >= 1000 else 2 if a >= 100 else 3 if a >= 1 else min(8, max(4, 3 - int(f"{a:e}".split("e")[1])))
    return ru(x, d)


def pct(x):
    return "—" if x is None else ru(x, 1) + "%"


def spct(x):
    """A signed percent: +7,3% or −2,1%. Pure."""
    return "—" if x is None else ("+" if x >= 0.05 else "") + ru(x, 1) + "%"


def pct0(x):
    """A setting's percent: 5% or 2,5%. Pure."""
    return (ru(x, 0) if abs(x - round(x)) < 1e-9 else ru(x, 1)) + "%"


def usdt(x):
    return ru(x, 0) + " USDT"


def money(x):
    """A signed sum: +1 240 USDT or −162 USDT. Pure."""
    return ("+" if x >= 0.5 else "") + ru(x, 0) + " USDT"


def coin(symbol):
    for q in ("USDT", "USDC", "BUSD"):
        if symbol.endswith(q) and len(symbol) > len(q):
            return symbol[:-len(q)]
    return symbol


def hm(t):
    """An instant as Batumi's clock reads it. Pure."""
    return dt.datetime.fromtimestamp(t, LOCAL).strftime("%H:%M")


def head(p):
    """A card's first line: the side's colour, the coin, the side and the leverage. Pure."""
    return "%s <b>%s · %s%s</b>" % (DOT[p["side"]], esc(coin(p["symbol"])), p["side"],
                                    " ×%d" % p["lev"] if p.get("lev") else "")


def pre(rows):
    """Aligned label-value rows in a monospace block. Pure."""
    w = max(len(k) for k, _v in rows) + 2
    return "<pre>" + "\n".join(esc(k.ljust(w) + v) for k, v in rows) + "</pre>"


def link_row(p):
    return [{"text": "📲 Открыть %s в Binance" % coin(p["symbol"]), "url": BINANCE_URL % p["symbol"]}]


def hint(p, mmr, target):
    """(USDT to add, rounded up, approximate or not), or None where the liquidation price is at the target or beyond
    it. Pure."""
    if distance_pct(p) is None:
        return None
    need = margin_hint(p, mmr or 0.0, target)
    if need <= 0:
        return None
    return float(math.ceil(need)), mmr is None or not p["isolated"]


def hint_html(p, mmr, target):
    h = hint(p, mmr, target)
    if h is None:
        return None
    s = "➕ Добавь <b>%s%s</b> маржи → ликвидация уйдёт на <b>%s</b> от цены (%s)" % (
        "≈ " if h[1] else "", usdt(h[0]), pct0(target), price(target_price(p, target)))
    return s + (" · кросс-маржа — оценка" if not p["isolated"] else "")


def liq_card(p, mmr, target, th, lvl, state, trend=None, until=None):
    """(text, buttons) of a position's liquidation card. `state`: "ring" - its stage's call is out; "engaged" - he is at
    work, its calls silent until `until`; "added" - margin added and the danger over; "eased" - the danger over by
    itself; "closed" - the position closed. `trend` is (distance then, minutes ago) or None. Pure."""
    d = distance_pct(p)
    em, name = STAGE[lvl]
    lines = [head(p), "%s <b>%s — ступень %d из 3</b>" % (em, name, lvl), ""]
    tr = ""
    if trend is not None and d is not None:
        tr = " %s <i>%d мин назад %s</i>" % (arrow(d, trend[0]), trend[1], pct(trend[0]))
    lines.append("До ликвидации <b>%s</b>%s" % (pct(d), tr))
    rows = [("Цена", price(p["mark"])), ("Ликвидация", price(p["liq"]))]
    if p.get("entry"):
        rows.append(("Вход", price(p["entry"])))
    if p.get("upnl") is not None:
        rows.append(("PnL", money(p["upnl"])))
    lines.append(pre(rows))
    h = hint_html(p, mmr, target) if state in ("ring", "engaged") else None
    if h:
        lines.append("<blockquote>%s</blockquote>" % h)
    c = esc(coin(p["symbol"]))
    if state == "ring" and lvl == 1:
        lines.append("🔔 Следующая ступень — %s до ликвидации: звонок, пока не подтвердишь." % pct0(th[1]))
    elif state == "ring":
        lines.append("🔔 Звонит Pushover. «Подтвердить» или «✋ Я в деле» — и звонки по %s затихнут на %d мин." % (
            c, ENGAGE_S // 60))
    elif state == "engaged":
        lines.append("🔕 <b>Ты в деле</b> — звонки по %s молчат до %s. Карточка обновляется сама." % (c, hm(until)))
    elif state == "added":
        lines.append("✅ <b>Маржа добавлена</b> — до ликвидации %s." % pct(d))
    elif state == "eased":
        lines.append("✅ Опасность миновала — до ликвидации %s." % pct(d))
    else:
        lines.append("Позиция закрыта.")
    buttons = None if state == "closed" else [link_row(p)]
    if state == "ring":
        buttons.append([{"text": "✋ Я в деле — тише %d мин" % (ENGAGE_S // 60), "callback_data": "eng:" + p["key"]}])
    return "\n".join(lines), buttons


def liq_push(p, mmr, target, lvl, kind="stage"):
    """(title, message) of a position's liquidation call: `kind` "stage", "timeout" or "last". Pure."""
    d = distance_pct(p)
    em = STAGE[lvl][0]
    c = coin(p["symbol"])
    if kind == "timeout":
        title = "%s %s %s · ⏰ до ликвидации всё ещё %s" % (DOT[p["side"]], c, p["side"], pct(d))
        first = "%d мин после «Подтвердить» — маржа не добавлена" % (ENGAGE_S // 60)
    elif kind == "last":
        title = "%s %s %s · 🆘 до ликвидации %s" % (DOT[p["side"]], c, p["side"], pct(d))
        first = "Маржа не добавлена %d мин — ликвидация совсем близко" % (LAST_QUIET_S // 60)
    else:
        title = "%s %s %s · %s до ликвидации %s" % (DOT[p["side"]], c, p["side"], em, pct(d))
        first = "Ступень %d из 3 · цена %s → ликвидация %s" % (lvl, price(p["mark"]), price(p["liq"]))
    lines = [first]
    h = hint(p, mmr, target)
    if h:
        lines.append("Добавь <b>%s%s</b> → ликвидация на %s" % ("≈ " if h[1] else "", usdt(h[0]), pct0(target)))
    if kind != "stage" or lvl >= 2:
        lines.append("«Подтвердить» — звонки по %s затихнут на %d мин" % (c, ENGAGE_S // 60))
    return title, "\n".join(lines)


def record_card(p, ev, trend=None):
    """(text, buttons) of a record: the gain from the entry, its PnL and ROE, and the next record. Pure."""
    lines = [head(p), "💰 <b>Прибыль %s от входа — новый рекорд</b>" % spct(ev["gain"]), ""]
    rows = [("Вход", price(p["entry"])), ("Цена", price(p["mark"]))]
    if p.get("upnl") is not None:
        rows.append(("PnL", money(p["upnl"])))
    roe = roe_pct(p)
    if roe is not None:
        rows.append(("ROE", spct(roe)))
    lines.append(pre(rows))
    if trend is not None:
        lines.append("Прибыль %s <i>%d мин назад %s</i>" % (arrow(ev["gain"], trend[0]), trend[1], spct(trend[0])))
    lines.append("<blockquote>🎯 Следующий рекорд — на <b>%s</b>. Отдаст цена треть прибыли от пика — сообщу."
                 "</blockquote>" % spct(ev["next"]))
    return "\n".join(lines), [link_row(p)]


def record_push(p, ev):
    title = "%s %s %s · 💰 %s от входа" % (DOT[p["side"]], coin(p["symbol"]), p["side"], spct(ev["gain"]))
    parts = ["Новый рекорд"]
    if p.get("upnl") is not None:
        parts.append("PnL <b>%s</b>" % money(p["upnl"]))
    roe = roe_pct(p)
    if roe is not None:
        parts.append("ROE %s" % spct(roe))
    return title, " · ".join(parts) + "\nСледующий — на %s · откат от пика тоже сообщу" % spct(ev["next"])


def pullback_card(p, ev, m):
    """(text, buttons) of a retreat from the record. Pure."""
    if ev["stage"] == 1:
        title = "↩️ <b>Откат от пика — отдано %d%% прибыли</b>" % round(ev["given"])
        note = "Цена развернулась от рекорда. Уйдёт половина прибыли — сообщу ещё раз."
    else:
        title = "↩️ <b>%s</b>" % ("Прибыль ушла" if ev["gain"] <= 0 else "Ушла половина прибыли")
        note = "По этому витку больше не напоминаю — до нового рекорда на %s." % spct(next_record(m["rec"]))
    rows = [("Пик", "%s  %s" % (spct(ev["peak"]), hm(m["best_t"]))), ("Сейчас", spct(ev["gain"])),
            ("Цена", price(p["mark"]))]
    if p.get("upnl") is not None:
        rows.append(("PnL", money(p["upnl"])))
    return "\n".join([head(p), title, "", pre(rows), "<blockquote>%s</blockquote>" % note]), [link_row(p)]


def pullback_push(p, ev, m):
    c = "%s %s %s" % (DOT[p["side"]], coin(p["symbol"]), p["side"])
    if ev["stage"] == 1:
        title = "%s · ↩️ откат: отдано %d%%" % (c, round(ev["given"]))
    else:
        title = "%s · ↩️ %s" % (c, "прибыль ушла" if ev["gain"] <= 0 else "ушла половина прибыли")
    text = "Пик %s в %s → сейчас <b>%s</b> от входа" % (spct(ev["peak"]), hm(m["best_t"]), spct(ev["gain"]))
    if p.get("upnl") is not None:
        text += "\nPnL %s" % money(p["upnl"])
    return title, text


def position_row(p, mmr, th, target, gain_then=None):
    """One position's line in the status and the heartbeat. Pure."""
    d = distance_pct(p)
    g = gain_pct(p["side"], p["entry"], p["mark"]) if p.get("entry") and p.get("mark") else None
    s = "%s <b>%s</b> %s%s" % (DOT[p["side"]], esc(coin(p["symbol"])), p["side"], " ×%d" % p["lev"] if p.get("lev") else "")
    if g is not None:
        s += " · <b>%s</b>%s" % (spct(g), " " + arrow(g, gain_then) if gain_then is not None else "")
    s += " · ликв. <b>%s</b>" % pct(d)
    if d is not None and d <= th[0]:
        h = hint(p, mmr, target)
        s += " ⚠️" + ("\n      ➕ добавь %s%s → ликв. на %s" % ("≈ " if h[1] else "", usdt(h[0]), pct0(target))
                      if h else "")
    return s


def status_card(positions, mmrs, th, target, profit_from, now, last_ok, blind, key_ok, dead_man, thens=None):
    """The status: one line a position, nearest the liquidation first; the settings and the guard's health folded
    away. Pure."""
    thens = thens or {}
    state = "⚪ не видит Binance %d мин" % round((now - last_ok) / 60) if blind else "✅ на посту"
    lines = ["🛡 <b>Сторож</b> · %s · %s" % (hm(now), state)]
    if not positions:
        lines.append("Открытых позиций нет.")
    for p in sorted(positions, key=lambda q: (distance_pct(q) is None, distance_pct(q) or 0.0)):
        lines.append(position_row(p, mmrs.get(p["symbol"]), th, target, thens.get(p["key"])))
    lines.append("<blockquote expandable>⚙️ Ступени %s · %s · %s до ликвидации · цель маржи %s · прибыль от %s\n"
                 "📡 Binance %d с назад · ключ только чтение %s · пульс %s</blockquote>" % (
                     ru(th[0], 1), ru(th[1], 1), pct0(th[2]), pct0(target),
                     ("+" + pct0(profit_from)) if profit_from else "выкл", max(0, round(now - last_ok)),
                     "✓" if key_ok else "—", "✓" if dead_man else "нет"))
    return "\n".join(lines)


def settings_card(th, target, profit_from):
    return ("⚙️ <b>Настройки сторожа</b>\n" + pre([
        ("Ступени ликвидации", "%s · %s · %s" % (ru(th[0], 1), ru(th[1], 1), pct0(th[2]))),
        ("Цель маржи", pct0(target)), ("Прибыль от", ("+" + pct0(profit_from)) if profit_from else "выкл")]) +
        "\nИзменить: «Пороги 4 2,5 1,5» · «Цель 5» · «Прибыль 7» (0 — выключить)")


def help_card(th, target, profit_from):
    return ("🛡 <b>Сторож</b> смотрит твои фьючерсы Binance каждые 5 с — ключом «только чтение». Сам не торгует и "
            "маржу не доливает.\n\n"
            "🔻 <b>Ликвидация — три ступени</b>, расстояние до неё в %% от цены:\n"
            "1️⃣ %s — громкое уведомление\n2️⃣ %s — звонок сквозь беззвучный режим, повторяется до «Подтвердить»\n"
            "3️⃣ %s — последний звонок\nВ каждой — сколько маржи добавить, чтобы ликвидация ушла на %s.\n\n"
            "🔕 <b>Нажал «Подтвердить» или «✋ Я в деле»</b> — по этой позиции %d мин никаких звонков, а карточка в "
            "Telegram обновляется сама. Добавишь маржу — сторож увидит и напишет ✅. Одно исключение: до ликвидации "
            "меньше %s и маржа не добавлена %d мин — один звонок.\n\n"
            "💰 <b>Прибыль</b> — от %s от входа: каждый новый рекорд (+3 пункта, дальше +25%%), откат от пика на треть "
            "и на половину прибыли.\n\n"
            "🟢 лонг · 🔴 шорт — цвет в начале каждого сигнала.\nКнопки внизу: Статус · Тест · Настройки · Помощь." % (
                pct0(th[0]), pct0(th[1]), pct0(th[2]), pct0(target), ENGAGE_S // 60, pct0(last_line(th)),
                LAST_QUIET_S // 60, ("+" + pct0(profit_from)) if profit_from else "— выключено"))


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


# ---- the guard: one cycle at a time, every effect through its stand-ins in the self-test ---------------------------

class Guard:
    def __init__(self, creds, net=None, now=time.time, var=VAR, uid=0, notify=sd_notify):
        self.creds, self.now, self.var, self.uid, self.notify = creds, now, var, uid, notify
        self.net = net or Net()
        self.scrub = Scrub(creds)
        self.bn = Binance(self.net, creds["binance-key"], creds["binance-secret"], now)
        self.po = Pushover(self.net, creds["pushover-token"], creds["pushover-user"])
        self.apps = {"main": self.po}
        for side, name in (("LONG", "pushover-long"), ("SHORT", "pushover-short")):
            self.apps[side] = Pushover(self.net, creds[name], creds["pushover-user"]) if creds.get(name) else self.po
        self.tg = Telegram(self.net, creds["tg-token"])
        self.chat, self.hc = int(creds["tg-chat"]), creds.get("hc-url")
        t = now()
        st = self.load_state()
        self.th, self.target, self.profit_from = settings_of(st)
        self.mem = self.load_memory()
        self.tg_offset = st.get("tg_offset") if isinstance(st.get("tg_offset"), int) else 0
        self.hb_day = st.get("hb_day")
        self.fired, self.positions, self.mmr, self.outbox, self.pushes = {}, [], {}, [], []
        self.watch, self.alarms, self.hist, self.held = {}, {}, {}, {}
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

    def load_memory(self):
        try:
            with open(os.path.join(self.var, "memory.json"), encoding="utf-8") as fh:
                doc = json.load(fh)
        except (OSError, ValueError):
            return {}
        keep = ("side", "entry", "best", "best_t", "rec", "pb")
        return {k: v for k, v in doc.items() if isinstance(v, dict) and all(f in v for f in keep)} \
            if isinstance(doc, dict) else {}

    def save_state(self):
        t = self.now()
        doc = {"at": utc(t), "started": utc(self.started), "thresholds": list(self.th), "target": self.target,
               "profit_from": self.profit_from, "tg_offset": self.tg_offset, "hb_day": self.hb_day,
               "last_ok": utc(self.last_ok), "polls_ok": self.polls_ok, "polls_err": self.polls_err,
               "positions": len(self.positions),
               "with_liquidation": sum(1 for p in self.positions if distance_pct(p) is not None),
               "watched": len(self.watch), "engaged": sum(1 for w in self.watch.values() if w.get("until")),
               "alarms_open": len(self.alarms), "side_apps": sum(1 for s in ("LONG", "SHORT")
                                                                 if self.apps[s] is not self.po),
               "blind": self.blind, "last_error": self.last_error, "key_ok": self.key_ok,
               "key_checked": utc(self.key_checked) if self.key_checked else None, "dead_man": bool(self.hc),
               "outbox": len(self.outbox), "disk_faults": self.disk_faults, "pid": os.getpid()}
        self.next_state = t + STATE_S
        for name, body in (("state.json", doc), ("memory.json", self.mem)):
            try:
                replace_private(os.path.join(self.var, name), (json.dumps(body, sort_keys=True) + "\n").encode(),
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
    def say(self, text, quiet=False, buttons=None, card=None):
        """A Telegram message queued; `card` = (key, stage) makes it that position's live card once sent."""
        m = {"to": "tg", "text": text, "quiet": quiet, "buttons": buttons, "card": card, "tries": 0}
        self.outbox.append(m)
        return m

    def push(self, title, message, priority, expire=ALARM_EXPIRE_S, app="main", sound=None, url=None, key=None,
             kind=None):
        t = self.now()
        self.pushes = [x for x in self.pushes if x > t - 3600]
        if len(self.pushes) >= PUSH_PER_HOUR:
            self.journal("push_capped", title=title)
            self.say("⚠️ Pushover: предел %d сообщений в час — это только здесь:\n<b>%s</b>\n%s" % (
                PUSH_PER_HOUR, title, message))
            return None
        self.pushes.append(t)
        m = {"to": "push", "title": title, "text": message, "priority": priority, "expire": expire, "app": app,
             "sound": sound, "url": url, "key": key, "kind": kind, "tries": 0}
        self.outbox.append(m)
        return m

    def flush(self):
        """Every waiting message tried once, in order; a channel that fails is not tried again in this pass. A call
        about a position he is working on, queued before he engaged, is dropped - but the last line's and the
        timeout's."""
        pending, self.outbox, failed, tg_sent = self.outbox, [], set(), 0
        for m in pending:
            if m["to"] == "push" and m.get("key") and self.engaged(m["key"]) and m.get("kind") not in ("last", "timeout"):
                self.journal("push_held", key=m["key"], kind=m.get("kind"))
                continue
            if m["to"] in failed or (m["to"] == "tg" and tg_sent >= TG_PER_PASS):
                self.outbox.append(m)
                continue
            try:
                if m["to"] == "tg":
                    tg_sent += 1
                    r = self.tg.send(self.chat, m["text"], m["quiet"], m["buttons"])
                    if m.get("card") and isinstance(r, dict) and m["card"][0] in self.watch:
                        w = self.watch[m["card"][0]]
                        w["card"], w["lvl"], w["t_edit"] = r.get("message_id"), m["card"][1], self.now()
                else:
                    t = self.now()
                    r = self.apps[m["app"]].send(m["title"], m["text"], m["priority"], m["expire"], m["sound"],
                                                 m["url"], ("Открыть %s в Binance" % coin(m["key"].split(":")[0]))
                                                 if m.get("key") else None)
                    self.journal("pushed", priority=m["priority"], kind=m.get("kind"), key=m.get("key"),
                                 app=m["app"], receipt=bool(r))
                    if m.get("test") and r:
                        self.test = {"receipt": r, "sent": t, "next": t + RECEIPT_EVERY_S, "deadline": t + TEST_WAIT_S}
                    elif r and m.get("key"):
                        self.alarms[r] = {"key": m["key"], "app": m["app"], "sent": t, "next": t + RECEIPT_EVERY_S,
                                          "until": t + m["expire"]}
            except Exception as e:
                failed.add(m["to"])
                m["tries"] += 1
                self.err("send %s" % m["to"], e)
                if m["tries"] < OUTBOX_TRIES:
                    self.outbox.append(m)
                else:
                    self.journal("dropped", to=m["to"], tries=m["tries"])
                    if m["to"] == "push":
                        self.say("⚠️ Pushover не принял сообщение за %d попыток:\n<b>%s</b>\n%s" % (
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

    def engaged(self, key):
        w = self.watch.get(key)
        return bool(w and w.get("until"))

    def any_engaged(self):
        return any(w.get("until") for w in self.watch.values())

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
        stages, fired, gains, mem = [], {}, [], {}
        for p in pos:
            d = distance_pct(p)
            lvl, fired[p["key"]] = step(self.fired.get(p["key"], frozenset()), d, self.th)
            if lvl:
                stages.append((lvl, p, d))
            m, evs = profit_step(self.mem.get(p["key"]), p, t, self.profit_from)
            if m is not None:
                mem[p["key"]] = m
            gains += [(ev, p, m) for ev in evs]
            g = gain_pct(p["side"], p["entry"], p["mark"]) if p["entry"] and p["mark"] else None
            self.hist[p["key"]] = [h for h in self.hist.get(p["key"], []) if t - h[0] <= HIST_S] + [(t, d, g)]
        self.positions = pos
        if stages:
            self.refresh_brackets([p["symbol"] for _l, p, _d in stages])
            for lvl, p, d in stages:
                self.announce(lvl, p)
        for ev, p, m in gains:
            self.tell(ev, p, m)
        self.fired, self.mem = fired, mem       # committed once the calls are queued: a fault before rings them again
        self.hist = {k: v for k, v in self.hist.items() if k in fired}
        for lvl, p, d in stages:
            self.journal("level", key=p["key"], level=lvl, distance=d, mark=p["mark"], liq=p["liq"],
                         engaged=self.engaged(p["key"]))
        for ev, p, _m in gains:
            self.journal(ev["kind"], key=p["key"], gain=ev["gain"], stage=ev.get("stage"), mark=p["mark"])
        self.polls_ok += 1
        if self.blind:
            self.blind = False
            self.say("✅ Сторож снова видит Binance — слеп был %d мин." % round((t - self.last_ok) / 60), quiet=True)
            self.journal("seen_again", blind_s=round(t - self.last_ok))
        self.last_ok = t
        ds = [d for d in (distance_pct(p) for p in pos) if d is not None]
        self.min_seen = min(ds) if ds else None
        if gains:
            self.next_state = 0.0
        return True

    def trend(self, key, i):
        return then_of(self.hist.get(key, []), self.now(), i)

    def announce(self, lvl, p):
        """A stage reached: the live card, and the call - unless he is working on this position, when the card alone
        changes."""
        t = self.now()
        w = self.watch.get(p["key"])
        if w is None:
            w = self.watch[p["key"]] = {"card": None, "lvl": lvl, "t_edit": t, "liq0": p["liq"], "added": 0,
                                        "added_t": None, "since": None, "until": None, "last": False}
        if w["until"]:
            w["lvl"] = max(w["lvl"], lvl)
            self.edit_card(p["key"], force=True)
            return
        mmr = self.mmr.get(p["symbol"])
        title, text = liq_push(p, mmr, self.target, lvl)
        self.push(title, text, 2 if lvl >= 2 else 1, app=p["side"], sound=SOUND["liq%d" % lvl],
                  url=BINANCE_URL % p["symbol"], key=p["key"], kind="liq%d" % lvl)
        body, buttons = liq_card(p, mmr, self.target, self.th, lvl, "ring", self.trend(p["key"], 1))
        self.say(body, buttons=buttons, card=(p["key"], lvl))

    def tell(self, ev, p, m):
        """A record or a retreat: held while he works on any position, else its card and its notice."""
        if self.any_engaged():
            self.held[p["key"]] = ev["kind"]
            return
        if ev["kind"] == "record":
            body, buttons = record_card(p, ev, self.trend(p["key"], 2))
            title, text = record_push(p, ev)
        else:
            body, buttons = pullback_card(p, ev, m)
            title, text = pullback_push(p, ev, m)
        self.push(title, text, 1, app=p["side"], sound=SOUND[ev["kind"]], url=BINANCE_URL % p["symbol"],
                  key=p["key"], kind=ev["kind"])
        self.say(body, buttons=buttons)

    def engage(self, key, via):
        """He is at work on `key`: no call about it for ENGAGE_S, its other calls stopped, its card says so."""
        t = self.now()
        w = self.watch.get(key)
        if w is None or not any(p["key"] == key for p in self.positions):
            return False
        first = not w["until"]
        w["until"] = t + ENGAGE_S
        if first:
            w["since"], w["last"] = t, False
        for r, a in list(self.alarms.items()):
            if a["key"] == key:
                try:
                    self.apps[a["app"]].cancel(r)
                except Exception as e:
                    self.err("cancel", e)
                del self.alarms[r]
        self.journal("engaged", key=key, via=via, first=first)
        self.edit_card(key, force=True)
        return True

    def edit_card(self, key, state=None, force=False):
        """The position's live card edited to the present, at most every LIVE_EDIT_S unless forced; an edit Telegram
        refuses is tried at the next."""
        t = self.now()
        w = self.watch.get(key)
        p = next((q for q in self.positions if q["key"] == key), None)
        if w is None or w["card"] is None or (not force and t - w["t_edit"] < LIVE_EDIT_S):
            return
        if p is None:
            state = "closed"
            p = {"symbol": key.split(":")[0], "side": key.split(":")[1], "key": key, "mark": None, "liq": None}
        d = distance_pct(p) if state != "closed" else None
        lvl = max(w["lvl"], crossed(d, self.th)) if d is not None else w["lvl"]
        state = state or ("engaged" if w["until"] else "ring")
        try:
            if state == "closed":
                self.tg.edit(self.chat, w["card"], "\n".join([
                    "%s <b>%s · %s</b>" % (DOT[p["side"]], esc(coin(p["symbol"])), p["side"]), "Позиция закрыта."]))
            else:
                body, buttons = liq_card(p, self.mmr.get(p["symbol"]), self.target, self.th, lvl, state,
                                         self.trend(key, 1), w["until"])
                self.tg.edit(self.chat, w["card"], body, buttons)
            w["t_edit"] = t
        except Exception as e:
            self.err("edit", e)

    def end_engaged(self, key, why, p=None):
        """His work on `key` over: `why` "added", "eased", "closed" or "timeout". A timeout with the danger still
        there calls him again; what was held while he worked is told, quietly."""
        w = self.watch[key]
        w["until"], w["since"] = None, None
        self.journal("engaged_end", key=key, why=why)
        if why == "timeout" and p is not None:
            d = distance_pct(p)
            mmr = self.mmr.get(p["symbol"])
            if d is not None and d <= self.th[1]:
                title, text = liq_push(p, mmr, self.target, max(2, crossed(d, self.th)), "timeout")
                self.push(title, text, 2, app=p["side"], sound=SOUND["liq2"], url=BINANCE_URL % p["symbol"],
                          key=key, kind="timeout")
            elif d is not None and d <= self.th[0]:
                title, text = liq_push(p, mmr, self.target, 1, "timeout")
                self.push(title, text, 1, app=p["side"], sound=SOUND["liq1"], url=BINANCE_URL % p["symbol"],
                          key=key, kind="timeout")
            self.edit_card(key, force=True)
        if not self.any_engaged() and self.held:
            held, self.held = self.held, {}
            for k, kind in sorted(held.items()):
                q = next((x for x in self.positions if x["key"] == k), None)
                m = self.mem.get(k)
                if q is None or m is None or not q["entry"]:
                    continue
                g = gain_pct(q["side"], q["entry"], q["mark"])
                self.say("%s\n📊 Пока ты был в деле: %s. Сейчас <b>%s</b> от входа, пик %s в %s." % (
                    head(q), "новый рекорд" if kind == "record" else "откат от пика", spct(g),
                    spct(gain_pct(q["side"], q["entry"], m["best"])), hm(m["best_t"])), quiet=True,
                    buttons=[link_row(q)])

    def tend(self):
        """Every watched position, each pass: margin added seen, his work's end or its last line, the danger's end,
        the card kept live."""
        t = self.now()
        here = {p["key"]: p for p in self.positions}
        for key, w in list(self.watch.items()):
            p = here.get(key)
            if p is None:
                self.edit_card(key, "closed", force=True)
                self.cancel_alarms(key)
                if w["until"]:
                    self.end_engaged(key, "closed")
                del self.watch[key]
                continue
            d = distance_pct(p)
            if w["liq0"] and p["liq"] and p["liq"] > 0 and not topup_seen(p["side"], w["liq0"], p["liq"]):
                w["liq0"] = min(w["liq0"], p["liq"]) if p["side"] == "SHORT" else max(w["liq0"], p["liq"])
            if topup_seen(p["side"], w["liq0"], p["liq"]):
                w["liq0"], w["added"], w["added_t"] = p["liq"], w["added"] + 1, t
                self.journal("margin_added", key=key, distance=d)
                if w["until"]:
                    w["until"] = t + ENGAGE_S
            if w["until"]:
                if d is None or (w["added"] and d > self.th[0]) or d > self.th[0] + REARM_PP:
                    why = "added" if w["added"] else "eased"
                    self.end_engaged(key, why)
                    self.finish(key, w, p, d, why)
                    continue
                if d <= last_line(self.th) and not w["last"] and t - (w["added_t"] or w["since"]) >= LAST_QUIET_S:
                    w["last"] = True
                    title, text = liq_push(p, self.mmr.get(p["symbol"]), self.target, 3, "last")
                    self.push(title, text, 2, app=p["side"], sound=SOUND["liq3"], url=BINANCE_URL % p["symbol"],
                              key=key, kind="last")
                if t >= w["until"]:
                    self.end_engaged(key, "timeout", p)
                    continue
            elif d is None or d > self.th[0] + REARM_PP:
                self.finish(key, w, p, d, "added" if w["added"] else "eased")
                continue
            elif d > self.th[1] + REARM_PP:
                self.cancel_alarms(key)
            self.edit_card(key)

    def finish(self, key, w, p, d, why):
        """The danger over: the card's last edit, its calls stopped, and a quiet word where margin was added."""
        self.edit_card(key, why, force=True)
        self.cancel_alarms(key)
        if why == "added" and d is not None:
            self.say("✅ %s · ликвидация отодвинута: до неё <b>%s</b>." % (head(p), pct(d)), quiet=True)
        del self.watch[key]

    def cancel_alarms(self, key):
        for r, a in list(self.alarms.items()):
            if a["key"] == key:
                try:
                    self.apps[a["app"]].cancel(r)
                except Exception as e:
                    self.err("cancel", e)
                del self.alarms[r]

    def check_alarms(self):
        """Each open call's receipt read every RECEIPT_EVERY_S: acknowledged - he is at work on its position."""
        t = self.now()
        for r, a in list(self.alarms.items()):
            if t < a["next"]:
                continue
            if t > a["until"]:
                del self.alarms[r]
                continue
            a["next"] = t + RECEIPT_EVERY_S
            try:
                doc = self.apps[a["app"]].receipt(r)
            except Exception as e:
                self.err("receipt", e)
                continue
            if doc.get("acknowledged") == 1:
                del self.alarms[r]
                self.journal("acknowledged", key=a["key"], after_s=round(t - a["sent"]))
                self.engage(a["key"], "pushover")
            elif doc.get("expired") == 1:
                del self.alarms[r]

    def check_blind(self):
        t = self.now()
        if t - self.last_ok >= BLIND_S and (not self.blind or t >= self.blind_next):
            first = not self.blind
            self.blind, self.blind_next = True, t + BLIND_REPEAT_S
            why = self.bn_error or "нет ответа"
            mins = round((t - self.last_ok) / 60)
            self.push("⚪ Сторож не видит Binance · %d мин" % mins, "Позиции без присмотра. %s" % esc(why), 1,
                      sound=SOUND["blind"])
            self.say("⚪ <b>Сторож не видит Binance %d мин</b>\nПозиции без присмотра. Причина: <code>%s</code>\n"
                     "%s" % (mins, esc(why), "Напомню через 30 мин, если не пройдёт." if first else "Всё ещё слеп."))
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
            ups = self.tg.call("getUpdates", offset=self.tg_offset, timeout=0,
                               allowed_updates=["message", "callback_query"])
        except Exception as e:
            self.err("telegram", e)
            return
        for u in ups:
            if isinstance(u.get("update_id"), int):
                self.tg_offset = max(self.tg_offset, u["update_id"] + 1)
            cq = u.get("callback_query")
            if isinstance(cq, dict):
                self.callback(cq)
                continue
            m = u.get("message") or {}
            if (m.get("chat") or {}).get("id") != self.chat:
                self.journal("foreign_chat")
                continue
            cmd, args = parse_command(m.get("text"))
            self.journal("command", cmd=cmd or "none")
            self.command(cmd, args)

    def callback(self, cq):
        """A button of a card pressed: «Я в деле» from his chat alone."""
        data = cq.get("data") or ""
        mine = (cq.get("from") or {}).get("id") == self.chat and \
            ((cq.get("message") or {}).get("chat") or {}).get("id") == self.chat
        if not mine:
            self.journal("foreign_chat")
            return
        ok = data.startswith("eng:") and self.engage(data[4:], "telegram")
        self.journal("command", cmd="engage" if ok else "button")
        try:
            self.tg.answer(cq.get("id"), ("🔕 Звонки по %s молчат %d мин" % (coin(data[4:].split(":")[0]),
                                                                          ENGAGE_S // 60)) if ok
                           else "Эта позиция уже вне опасности")
        except Exception as e:
            self.err("answer", e)

    def command(self, cmd, args):
        if cmd == "status":
            thens = {p["key"]: (self.trend(p["key"], 2) or (None,))[0] for p in self.positions}
            self.say(status_card(self.positions, self.mmr, self.th, self.target, self.profit_from, self.now(),
                                 self.last_ok, self.blind, self.key_ok, bool(self.hc), thens))
        elif cmd == "test":
            if self.test:
                self.say("🔔 Тест уже идёт — подтверди звонок в Pushover.")
                return
            m = self.push("🛡 Сторож · проверка звонка", "Это тест. Нажми «Подтвердить» — в Telegram придёт ✅.", 2,
                          TEST_EXPIRE_S, sound=SOUND["test"])
            if m is not None:
                m["test"] = True
                self.say("🔔 Тестовый звонок отправлен — подтверди его в Pushover.")
        elif cmd in ("thresholds", "settings", "target", "profit") and not args:
            self.say(settings_card(self.th, self.target, self.profit_from))
        elif cmd in ("thresholds", "target", "profit"):
            v = {"thresholds": thresholds_of, "target": target_of, "profit": profit_of}[cmd](args)
            if v is None:
                self.say({"thresholds": "Не понял. Нужно три числа по убыванию, не больше 30: «Пороги 4 2,5 1,5».",
                          "target": "Не понял. Нужно одно число от 1 до 30: «Цель 5».",
                          "profit": "Не понял. Нужно одно число от 3 до 100, или 0 — выключить: «Прибыль 7»."}[cmd])
                return
            if cmd == "thresholds":
                self.th = v
                self.fired = {p["key"]: frozenset(range(1, crossed(distance_pct(p), v) + 1))
                              for p in self.positions if distance_pct(p) is not None}
            elif cmd == "target":
                self.target = v
            else:
                self.profit_from = v
            self.journal(cmd, value=list(v) if cmd == "thresholds" else v)
            self.save_state()
            self.say("✅ Задано.\n" + settings_card(self.th, self.target, self.profit_from))
        elif cmd == "settings":
            self.say(settings_card(self.th, self.target, self.profit_from))
        elif cmd == "help":
            self.say(help_card(self.th, self.target, self.profit_from))
        else:
            self.say("Команды — на кнопках внизу: Статус · Тест · Настройки · Помощь.")

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
            self.say("✅ <b>Звонок дошёл</b> — подтверждён%s." % (
                " через %d с" % max(0, at - round(self.test["sent"])) if isinstance(at, int) else ""))
            self.journal("test", acknowledged=True, after_s=round(t - self.test["sent"]))
            self.test = None
        elif t >= self.test["deadline"]:
            try:
                self.po.cancel(self.test["receipt"])
            except Exception as e:
                self.err("cancel", e)
            self.say("⚠️ Тест не подтверждён за %d мин. Проверь в Pushover: Настройки → Critical Alerts включены, "
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
            lines = ["🌙 <b>Сторож на посту</b> · позиций %d" % len(self.positions)]
            for p in sorted(self.positions, key=lambda q: (distance_pct(q) is None, distance_pct(q) or 0.0)):
                lines.append(position_row(p, self.mmr.get(p["symbol"]), self.th, self.target))
            lines.append("<i>Ступени %s · %s · %s · цель %s · прибыль от %s</i>" % (
                ru(self.th[0], 1), ru(self.th[1], 1), pct0(self.th[2]), pct0(self.target),
                ("+" + pct0(self.profit_from)) if self.profit_from else "выкл"))
            self.say("\n".join(lines), quiet=True)
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
                         min_distance=self.min_seen, blind=self.blind, outbox=len(self.outbox),
                         watched=len(self.watch), alarms_open=len(self.alarms))
            d = os.path.join(self.var, "journal")
            cut = utc(t - KEEP_DAYS * 86400)[:10]
            for f in sorted(os.listdir(d)):
                if re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}\.jsonl", f) and f[:10] < cut:
                    os.unlink(os.path.join(d, f))
                    self.journal("pruned", file=f)
        if t >= self.next_state:
            self.save_state()

    def cycle(self):
        """One pass: the clock, the key's permissions, the positions, blindness, brackets, the calls' receipts, the
        watched positions, the chat, the test, the heartbeat, the outbox, the dead-man, the record, the watchdog. A
        step's fault is journaled and stops no other step; a key that can do more than read stops the guard."""
        if self.now() >= self.next_key:
            self.check_key()
        for name, f in (("sync", self.sync), ("poll", self.poll), ("blind", self.check_blind),
                        ("brackets", self.refresh_brackets), ("alarms", self.check_alarms), ("tend", self.tend),
                        ("telegram", self.telegram), ("test", self.check_test), ("heartbeat", self.heartbeat),
                        ("flush", self.flush), ("dead-man", self.ping), ("tick", self.tick)):
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
    tty.say("Сторож · ТЗ-55: учётные данные. Ввод скрыт; ничего из введённого не попадает ни в журнал, ни в отчёт.")
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


def see_text(pos, mmrs, th, target, profit_from, now, dead_man):
    """What the guard sees, for the Boss to hold against his Binance app: its status card. Pure."""
    return status_card(pos, mmrs, th, target, profit_from, now, now, False, True, dead_man) + \
        "\n\nСовпадает с твоими позициями в Binance? Ответь «да» или «нет»."


SAMPLE_LONG = {"symbol": "SOLUSDT", "side": "LONG", "key": "SOLUSDT:LONG", "qty": 31.0, "mark": 200.01, "liq": 152.6,
               "notional": 6200.31, "isolated": True, "entry": 186.40, "upnl": 421.91, "lev": 5}
SAMPLE_SHORT = {"symbol": "YFIUSDT", "side": "SHORT", "key": "YFIUSDT:SHORT", "qty": 2.0, "mark": 1808.1,
                "liq": 1851.5, "notional": 3616.2, "isolated": True, "entry": 1646.5, "upnl": -323.2, "lev": 10}


def samples():
    """The two examples G-LOOK shows: a long's record and a short's alarm - (side, title, message, card, buttons). Pure."""
    ev = {"kind": "record", "gain": gain_pct("LONG", SAMPLE_LONG["entry"], SAMPLE_LONG["mark"]), "next": 10.3}
    t1, m1 = record_push(SAMPLE_LONG, ev)
    c1, b1 = record_card(SAMPLE_LONG, ev, (5.1, 5))
    t2, m2 = liq_push(SAMPLE_SHORT, 0.005, TARGET_PCT, 2)
    c2, b2 = liq_card(SAMPLE_SHORT, 0.005, TARGET_PCT, DEFAULT_THRESHOLDS, 2, "ring", (3.3, 5))
    return [("LONG", t1 + " (пример)", m1, c1, b1), ("SHORT", t2 + " (пример)", m2, c2, b2)]


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
    chat as every open position he has; the two examples of its alerts - a long's through its application, a short's
    through its own - confirmed by him as he sees them; a test alarm sent at Pushover's emergency priority and
    acknowledged on his phone; the dead-man pinged, and kept quiet through the waits. Its record, prove.json, carries
    this code's SHA-256."""
    creds, problems = read_credentials(etc, uid)
    gates = []

    def gate(name, ok, detail):
        gates.append({"gate": name, "pass": bool(ok), "detail": detail})
        out("%s %s - %s" % (name, "PASS" if ok else "FAIL", detail))
        return ok
    sides = [s for s in ("LONG", "SHORT") if "pushover-" + s.lower() in creds]
    if not gate("G-CRED", not problems, "%d credentials of their form, 0600, root's; the dead-man %s; side "
                                        "applications %d%s" % (len(creds), "set" if "hc-url" in creds else "not set",
                                                               len(sides), "; " + "; ".join(problems) if problems else "")):
        return 4
    scrub = Scrub(creds)
    net = net or Net(timeout=LONG_POLL_S + 15)
    bn = Binance(net, creds["binance-key"], creds["binance-secret"], now)
    po = Pushover(net, creds["pushover-token"], creds["pushover-user"])
    apps = {s: Pushover(net, creds["pushover-" + s.lower()], creds["pushover-user"]) if s in sides else po
            for s in ("LONG", "SHORT")}
    tg = Telegram(net, creds["tg-token"])
    beat = [0.0]

    def tried(name, f):
        try:
            return f(), None
        except Exception as e:
            return None, scrub("%s: %s" % (type(e).__name__, e))[:300]

    def keep_alive():
        """The dead-man pinged at most once a minute while the prove waits on the Boss, so that no wait reads at
        healthchecks.io as the host's death."""
        if "hc-url" in creds and now() - beat[0] >= HC_S:
            beat[0] = now()
            tried("dead-man", lambda: hc_ping(net, creds["hc-url"]))
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
    gate("G-POS", e is None, ("%s served; open positions %d, with a liquidation price %d, with an entry price %d" % (
        bn.position_path, len(pos), sum(1 for p in pos if distance_pct(p) is not None),
        sum(1 for p in pos if p["entry"]))) if e is None else e)
    sym = pos[0]["symbol"] if pos else "BTCUSDT"
    br, e = tried("brackets", lambda: bn.brackets(sym))
    n = len((br[0] if isinstance(br, list) and br else br or {}).get("brackets") or []) if e is None else 0
    gate("G-BRACKET", e is None and n > 0, ("leverage brackets of one held symbol: %d" % n) if e is None else e)
    errs = []
    for name, app in [("main", po)] + [(s, apps[s]) for s in sides]:
        _v, e = tried("pushover", app.validate)
        if e is not None:
            errs.append("%s: %s" % (name, e))
    gate("G-PUSH", not errs, ("the user key and %d application tokens validated" % (1 + len(sides))) if not errs
         else "; ".join(errs))
    me, e = tried("telegram", lambda: tg.call("getMe"))
    if e is None:
        _s, e = tried("telegram", lambda: tg.send(creds["tg-chat"], "🛡 Сторож · проверка связи (ТЗ-55)."))
    gate("G-TG", e is None, "getMe and one message to the pinned chat" if e is None else e)
    chat = int(creds["tg-chat"])
    offset = [0]

    def ask(text, wait=SEE_WAIT_S):
        """(the Boss's yes or no or None, the seconds he took, an error): `text` sent, his answer read."""
        _s, e = tried("telegram", lambda: tg.send(chat, text))
        said, t0 = None, now()
        while e is None and said is None and now() - t0 < wait:
            keep_alive()
            ups, e2 = tried("telegram", lambda: tg.call("getUpdates", offset=offset[0], timeout=LONG_POLL_S,
                                                        allowed_updates=["message", "callback_query"]))
            if e2 is not None:
                sleep(5)
                continue
            if ups:
                offset[0] = ups[-1]["update_id"] + 1
            said = answer_of(ups, chat)
        return said, round(now() - t0), e
    if all(g["pass"] for g in gates):
        last, e = tried("telegram", lambda: tg.call("getUpdates", offset=-1, timeout=0,
                                                    allowed_updates=["message", "callback_query"]))
        offset[0] = (last[-1]["update_id"] + 1) if e is None and last else 0
        try:
            with open(os.path.join(var, "state.json"), encoding="utf-8") as fh:
                st = json.load(fh)
        except (OSError, ValueError):
            st = {}
        th, target, profit_from = settings_of(st if isinstance(st, dict) else {})
        said, took, e = ask(see_text(pos, {}, th, target, profit_from, now(), "hc-url" in creds)) if e is None \
            else (None, 0, e)
        gate("G-SEE", said is True, e or ("the Boss answered yes to the list of %d positions after %d s" % (
            len(pos), took) if said is True else "the Boss answered no" if said is False
            else "no answer in %d s" % SEE_WAIT_S))
    if all(g["pass"] for g in gates):
        errs = []
        for side, title, text, card, buttons in samples():
            _r, e = tried("sample", lambda: apps[side].send(title, text, 0, sound=SOUND["sample"],
                                                            url=BINANCE_URL % ("SOLUSDT" if side == "LONG" else
                                                                               "YFIUSDT"),
                                                            url_title="Открыть в Binance"))
            if e is None:
                _s, e = tried("telegram", lambda: tg.send(chat, card, False, buttons))
            if e is not None:
                errs.append(e)
        said, took, e = ask("☝️ Два примера сигналов — 🟢 лонг и 🔴 шорт: здесь и на экране блокировки (Pushover). "
                            "Цвета видны, всё читается? Ответь «да» или «нет».") if not errs else (None, 0, errs[0])
        gate("G-LOOK", said is True, e or ("two examples through %d side applications; the Boss answered yes after "
                                           "%d s" % (len(sides), took) if said is True else "the Boss answered no"
                                           if said is False else "no answer in %d s" % SEE_WAIT_S))
    if all(g["pass"] for g in gates):
        tried("telegram", lambda: tg.call("getUpdates", offset=offset[0], timeout=0,
                                          allowed_updates=["message", "callback_query"]))
        r, e = tried("alarm", lambda: po.send("🛡 Сторож · проверка звонка (ТЗ-55)",
                                               "Нажми «Подтвердить» — так проверяется, что звонок будит тебя.", 2,
                                               TEST_EXPIRE_S, SOUND["test"]))
        acked, waited = False, 0
        if e is None:
            tried("telegram", lambda: tg.send(creds["tg-chat"], "🔔 Сейчас зазвонит Pushover — нажми «Подтвердить»."))
            t0 = now()
            while now() - t0 < TEST_WAIT_S:
                sleep(RECEIPT_EVERY_S)
                keep_alive()
                d, e2 = tried("receipt", lambda: po.receipt(r))
                if e2 is None and d.get("acknowledged") == 1:
                    acked = True
                    break
            waited = round(now() - t0)
            if not acked:
                tried("cancel", lambda: po.cancel(r))
        gate("G-ALARM", acked, ("acknowledged after %d s" % waited) if acked else (e or "not acknowledged in %d s" %
                                                                                    TEST_WAIT_S))
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
    keys = ("at", "started", "last_ok", "polls_ok", "polls_err", "positions", "with_liquidation", "watched", "engaged",
            "alarms_open", "side_apps", "blind", "key_ok", "key_checked", "dead_man", "outbox", "disk_faults",
            "thresholds", "target", "profit_from", "pid")
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
    g.journal("start", code=sha256_file(os.path.abspath(__file__)), thresholds=list(g.th), target=g.target,
              profit_from=g.profit_from, dead_man=bool(g.hc), side_apps=[s for s in ("LONG", "SHORT")
                                                                          if g.apps[s] is not g.po])
    try:
        g.check_key()
    except KeyRefused as e:
        return refuse(g, e)
    g.poll()
    g.say("🛡 <b>Сторож запущен</b> · версия 2 · позиций %d · ключ %s" % (
        len(g.positions), "только чтение ✓" if g.key_ok else "ещё не проверен"), quiet=True)
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
    text = "Ключ Binance может больше, чем читать (%s). Создай ключ только с «Enable Reading» и привязкой к IP " \
           "сервера." % esc("; ".join(e.args[0]))
    for f in (lambda: g.po.send("⛔ Сторож остановлен", text, 1), lambda: g.tg.send(g.chat, "⛔ <b>Сторож "
                                                                                     "остановлен</b>\n" + text)):
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
    """Binance, Pushover, Telegram and healthchecks.io as dictionaries; every request recorded. A question that asks
    for «да» or «нет» is answered from `answer`, the examples' from `look`."""

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
        self.tg_edits, self.tg_answers, self.next_id = [], [], 100
        self.answer, self.look = "Да", "да"
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
                said = self.look if "Цвета видны" in p["text"] else self.answer
                if "Ответь «да» или «нет»" in p["text"] and said is not None:
                    n = max([x["update_id"] for x in self.updates] or [0]) + 1
                    self.updates.append({"update_id": n, "message": {"text": said,
                                                                    "chat": {"id": p["chat_id"], "type": "private"}}})
                self.next_id += 1
                return 200, json.dumps({"ok": True, "result": {"message_id": self.next_id}}).encode()
            if meth == "editMessageText":
                self.tg_edits.append(p)
                return 200, b'{"ok":true,"result":true}'
            if meth == "answerCallbackQuery":
                self.tg_answers.append(p)
                return 200, b'{"ok":true,"result":true}'
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


def wellformed(text):
    """Every tag this file sends to Telegram opened and closed as often - b, i, pre, code, blockquote. Pure."""
    return all(text.count("<%s>" % t) + text.count("<%s " % t) == text.count("</%s>" % t)
               for t in ("b", "i", "pre", "code", "blockquote"))


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
            for target in (8.0, TARGET_PCT):
                need = margin_hint(p, mmr, target)
                lp2 = binance_lp(side, qty, entry, wallet + need, mmr, cum)
                d2 = distance_pct({"side": side, "mark": mark, "liq": lp2})
                check(need > 0 and abs(d2 - target) < 1e-9, "the margin hint moves %s's liquidation to %s%%: %r" % (
                    side, target, d2))
                check(abs(target_price(p, target) - lp2) < 1e-6 * lp2, "the target's liquidation price")
            check(margin_hint(dict(p, liq=binance_lp(side, qty, entry, wallet + need + 100, mmr, cum)), mmr) == 0.0,
                  "no hint where the liquidation is beyond the target")
        check(abs(distance_pct({"side": "SHORT", "mark": 100.0, "liq": 103.0}) - 3.0) < 1e-12, "a short's distance")
        check(abs(distance_pct({"side": "LONG", "mark": 100.0, "liq": 97.0}) - 3.0) < 1e-12, "a long's distance")
        check(distance_pct({"side": "LONG", "mark": 100.0, "liq": 0.0}) is None, "no liquidation price, no distance")
        # -- stages: announce once a descent, the highest of a jump, re-arm above threshold + 1 -------------------
        th, f, seq = (5.0, 3.0, 1.5), frozenset(), []
        for d in (6.0, 4.9, 4.5, 2.9, 2.8, 1.4, 1.0, 2.6, 1.4, 8.0, 0.9, None, 4.0):
            lvl, f = step(f, d, th)
            seq.append(lvl)
        check(seq == [0, 1, 0, 2, 0, 3, 0, 0, 3, 0, 3, 0, 1], "the stages announced: %r" % seq)
        check(step(frozenset({1}), 5.5, th)[1] == frozenset({1}) and step(frozenset({1}), 6.01, th)[1] == frozenset(),
              "hysteresis of one point")
        # -- gains: records, retreats, an entry moved, a short, off ---------------------------------------------------
        m, kinds = None, []
        for k, mk in enumerate((105, 107.2, 108, 110.3, 109, 107.5, 106.8, 105.5, 105.1, 104, 113.4)):
            m, evs = profit_step(m, {"side": "LONG", "entry": 100.0, "mark": float(mk)}, 1000.0 + k, PROFIT_FROM)
            kinds.append(evs[0]["kind"] + str(evs[0].get("stage", "")) if evs else "-")
        check(kinds == ["-", "record", "-", "record", "-", "-", "pullback1", "-", "pullback2", "-", "record"],
              "records and retreats - a third given back, not a quarter; half: %r" % kinds)
        check(m["best"] == 113.4 and m["best_t"] == 1010.0 and m["pb"] == 0 and abs(m["rec"] - 13.4) < 1e-9,
              "the memory after: %r" % m)
        m2, evs = profit_step(m, {"side": "LONG", "entry": 101.0, "mark": 113.4}, 2000.0, PROFIT_FROM)
        check(m2["entry"] == 101.0 and m2["best"] == 113.4 and [e["kind"] for e in evs] == ["record"],
              "an entry moved starts the gains again")
        _m, evs = profit_step(None, {"side": "SHORT", "entry": 100.0, "mark": 93.0}, 1.0, PROFIT_FROM)
        check([e["kind"] for e in evs] == ["record"] and abs(evs[0]["gain"] - 7.0) < 1e-9, "a short's record at 7%")
        check(profit_step(None, {"side": "SHORT", "entry": 100.0, "mark": 80.0}, 1.0, 0.0)[1] == [], "off at 0")
        check(profit_step(None, {"side": "LONG", "entry": None, "mark": 80.0}, 1.0, 7.0) == (None, []), "no entry")
        check(next_record(7.2) == 10.2 and abs(next_record(20.0) - 25.0) < 1e-12, "the next record")
        # -- margin added, the last line, the trend --------------------------------------------------------------------
        check(topup_seen("SHORT", 1610.0, 1700.0) and not topup_seen("SHORT", 1610.0, 1612.0)
              and topup_seen("LONG", 50000.0, 49800.0) and not topup_seen("LONG", 50000.0, 49950.0)
              and not topup_seen("LONG", None, 49000.0), "margin added seen")
        check(last_line((4.0, 2.5, 1.5)) == 1.0 and last_line((3.0, 1.0, 0.5)) == 0.5, "the last line")
        hist = [(0.0, 3.3, None), (200.0, 3.0, None), (290.0, 2.8, None)]
        check(then_of(hist, 300.0, 1) == (3.3, 5) and then_of(hist[2:], 300.0, 1) is None
              and arrow(2.4, 3.3) == "↘" and arrow(3.3, 2.4) == "↗" and arrow(3.0, 3.01) == "→", "the trend")
        # -- positions, brackets, the key's permissions, commands ----------------------------------------------------
        raw = [{"symbol": "YFIUSDT", "positionSide": "BOTH", "positionAmt": "-25.000", "markPrice": "1596.20",
                "liquidationPrice": "1700.00", "notional": "-39905.0", "isolatedWallet": "4100.0",
                "entryPrice": "1646.5", "unRealizedProfit": "1257.5", "positionInitialMargin": "3990.5"},
               {"symbol": "BTCUSDT", "positionSide": "LONG", "positionAmt": "0.500", "markPrice": "92000",
                "liquidationPrice": "0", "notional": "46000", "isolatedWallet": "0", "entryPrice": "90000",
                "unRealizedProfit": "1000", "leverage": "20"},
               {"symbol": "ETHUSDT", "positionSide": "BOTH", "positionAmt": "0.000", "markPrice": "3000",
                "liquidationPrice": "0"}]
        ps = parse_positions(raw)
        check([(p["symbol"], p["side"], p["isolated"], p["entry"], p["lev"]) for p in ps] ==
              [("YFIUSDT", "SHORT", True, 1646.5, 10), ("BTCUSDT", "LONG", False, 90000.0, 20)], "positions: %r" % ps)
        check(abs(roe_pct(ps[0]) - 100 * 1257.5 / (25 * 1646.5 / 10)) < 1e-9 and roe_pct(dict(ps[0], lev=None)) is None,
              "ROE over the initial margin at the entry")
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
              == ("thresholds", ["5", "3", "1,5"]) and parse_command("  ТЕСТ ") == ("test", [])
              and parse_command("Цель 5") == ("target", ["5"]) and parse_command("Прибыль выкл") == ("profit", ["выкл"])
              and parse_command("Настройки") == ("settings", []), "commands")
        check(thresholds_of(["5", "3", "1,5"]) == (5.0, 3.0, 1.5) and thresholds_of(["3", "5", "1"]) is None
              and thresholds_of(["40", "3", "1"]) is None and thresholds_of(["5", "3"]) is None
              and thresholds_of(["5", "x", "1"]) is None, "thresholds")
        check(target_of(["5"]) == 5.0 and target_of(["7,5"]) == 7.5 and target_of(["0,5"]) is None
              and target_of(["31"]) is None and profit_of(["7"]) == 7.0 and profit_of(["0"]) == 0.0
              and profit_of(["выкл"]) == 0.0 and profit_of(["2"]) is None and profit_of([]) is None, "target, profit")
        check(settings_of({"thresholds": [4.0, 2.5, 1.5], "target": 6, "profit_from": 0.0}) == ((4.0, 2.5, 1.5), 6, 0.0)
              and settings_of({"thresholds": [1, 2, 3], "target": True}) == (DEFAULT_THRESHOLDS, TARGET_PCT, PROFIT_FROM),
              "settings kept, and defaults where a value is not of its form")
        check(price(1596.2) == "1 596,2" and price(0.00012346) == "0,0001235" and pct(2.94) == "2,9%"
              and spct(7.31) == "+7,3%" and spct(-2.06) == "−2,1%" and money(1240.4) == "+1 240 USDT"
              and money(-162.2) == "−162 USDT" and pct0(5.0) == "5%" and pct0(2.5) == "2,5%"
              and coin("YFIUSDT") == "YFI" and coin("USDT") == "USDT", "notation")
        sc = Scrub({"binance-key": "A" * 64, "tg-chat": "123"})
        check(sc("key %s from 203.0.113.9" % ("A" * 64)) == "key *** from x.x.x.x", "scrub")
        # -- the texts: each colour first, HTML well formed, within the channels' limits ------------------------------
        y = ps[0]
        lc, lb = liq_card(dict(y, liq=1615.0), 0.01, 5.0, (4.0, 2.5, 1.5), 3, "ring", (3.3, 5))
        check(lc.startswith("🔴 <b>YFI · SHORT ×10</b>") and "Последний рубеж — ступень 3 из 3" in lc and "Добавь" in lc
              and "↘ <i>5 мин назад 3,3%</i>" in lc and lb[0][0]["url"] == BINANCE_URL % "YFIUSDT"
              and lb[1][0]["callback_data"] == "eng:YFIUSDT:SHORT", "a short's liquidation card: %r" % lc)
        ec, eb = liq_card(dict(y, liq=1615.0), 0.01, 5.0, (4.0, 2.5, 1.5), 3, "engaged", None, 1.8e9)
        check("Ты в деле" in ec and len(eb) == 1, "the engaged card keeps the link alone")
        tt, tm = liq_push(dict(y, liq=1640.0), 0.01, 5.0, 2)
        check(tt == "🔴 YFI SHORT · 🚨 до ликвидации 2,7%" and "Подтвердить" in tm and "Добавь <b>" in tm, "a push: %r" % tt)
        b = dict(ps[1], liq=None, mark=96400.0)
        rt, rm = record_push(b, {"gain": gain_pct("LONG", 90000.0, 96400.0), "next": 10.1})
        check(rt == "🟢 BTC LONG · 💰 +7,1% от входа" and "Новый рекорд" in rm, "a record's push: %r" % rt)
        texts = [lc, ec, rm, tm, record_card(b, {"gain": 7.1, "next": 10.1}, (5.1, 5))[0],
                 pullback_card(b, {"stage": 1, "gain": 6.7, "peak": 10.3, "given": 35.0},
                               {"best_t": 1.8e9, "rec": 10.3})[0],
                 pullback_card(b, {"stage": 2, "gain": -0.5, "peak": 10.3, "given": 104.9},
                               {"best_t": 1.8e9, "rec": 10.3})[0],
                 status_card(ps, {}, (4.0, 2.5, 1.5), 5.0, 7.0, 1.8e9, 1.8e9 - 3, False, True, True),
                 status_card([], {}, DEFAULT_THRESHOLDS, 5.0, 0.0, 1.8e9, 1.8e9 - 300, True, None, False),
                 settings_card((4.0, 2.5, 1.5), 5.0, 7.0), help_card((4.0, 2.5, 1.5), 5.0, 7.0)]
        texts += [s[3] for s in samples()] + [s[2] for s in samples()]
        check(all(wellformed(t) and len(t) <= 4000 for t in texts), "every text's HTML well formed")
        check(all(len(s[1]) <= 250 and len(s[2]) <= 1024 and s[1][0] in "🟢🔴" for s in samples()),
              "the examples within Pushover's limits, each colour first")
        check("Прибыль ушла" in texts[6] and "⚠️" not in texts[7].split("\n")[1], "a gain gone; no warning far off")
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
                "pushover-token": "a" * 30, "tg-token": "123456789:" + "T" * 35, "pushover-long": "L" * 30}
        script = [("API Key", "not-a-key"), ("API Key", vals["binance-key"]), ("Secret Key", vals["binance-secret"]),
                  ("User Key", vals["pushover-user"]), ("API Token", vals["pushover-token"]),
                  ("BotFather", vals["tg-token"]), ("hc-ping.com", ""), ("Сторож LONG", vals["pushover-long"]),
                  ("Сторож SHORT", "")]
        rc, screen, log, left = on_terminal(lambda: mode_secrets(etc=etc, uid=uid), script)
        check(rc == 0 and not left, "secrets at a real terminal: rc %s, left %d, log %r" % (rc, len(left), log[-300:]))
        check(all(v not in screen + log for v in vals.values()), "no value echoed or logged")
        check(sorted(os.listdir(etc)) == sorted(vals) and all(private_file_ok(os.path.join(etc, k), uid=uid)
                                                              for k in vals), "six files, 0600")
        check("hc-url: skipped" in log and "pushover-short: skipped" in log and "written, 65 bytes" in log,
              "the log: written and skipped")
        rc2, _s, log2, _l = on_terminal(lambda: mode_secrets(etc=etc, uid=uid), [("hc-ping.com", ""),
                                                                                 ("Сторож SHORT", "")])
        check(rc2 == 0 and log2.count(": kept") == 6 and "hc-url: skipped" in log2 and "pushover-short: skipped" in log2,
              "a second run keeps them and asks for the optional ones again: %r" % log2[-200:])
        # -- find-chat -----------------------------------------------------------------------------------------------
        fn = FakeNet(vals["binance-key"], vals["binance-secret"])
        fn.updates = [{"update_id": 7, "message": {"text": "/start", "chat": {"id": 4242, "type": "private"}}}]
        check(mode_find_chat(Telegram(fn, vals["tg-token"]), etc, 5, uid) == 0, "find-chat pins one chat")
        creds, problems = read_credentials(etc, uid)
        check(problems == [] and creds["tg-chat"] == "4242" and "pushover-short" not in creds,
              "credentials read: %r" % problems)
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
        check(rec["pass"] is True and [g["gate"] for g in rec["gates"]] == list(PROVE_GATES), "prove's eleven gates")
        ex = [x for x in fn.pushes if x["title"].endswith("(пример)")]
        check([(x["title"][0], x["token"], x["priority"]) for x in ex] == [("🟢", vals["pushover-long"], "0"),
                                                                          ("🔴", vals["pushover-token"], "0")]
              and "url" in ex[0] and ex[0]["html"] == "1", "the examples: the long's through its own application")
        write_private(os.path.join(etc, "hc-url"), b"https://hc-ping.com/0f0e0d0c-0b0a-4908-8706-050403020100\n", uid)
        n_hc = fn.count.get(HC, 0)
        check(mode_prove(fn, etc, var, uid, lambda: clock[0], ack_later, code="c" * 64) == 0
              and json.load(open(os.path.join(var, "prove.json")))["gates"][-1]["detail"] == "the dead-man's ping answered OK"
              and fn.count.get(HC, 0) >= n_hc + 2, "the dead-man kept quiet through the waits and pinged last")
        check(any("YFI" in m["text"] and "Совпадает" in m["text"] for m in fn.tg_sent), "the list shown")
        fn.answer = "нет"
        check(mode_prove(fn, etc, var, uid, lambda: clock[0], ack_later, code="c" * 64) == 4,
              "prove fails where the Boss answers no")
        check(json.load(open(os.path.join(var, "prove.json")))["gates"][-1]["gate"] == "G-SEE", "no alarm after a no")
        fn.answer, fn.look = "да", "нет"
        check(mode_prove(fn, etc, var, uid, lambda: clock[0], ack_later, code="c" * 64) == 4
              and json.load(open(os.path.join(var, "prove.json")))["gates"][-1]["gate"] == "G-LOOK",
              "prove fails where the Boss rejects the examples")
        fn.look = "да"
        check(mode_prove(fn, etc, var, uid, lambda: clock[0], ack_later, code="c" * 64) == 0, "prove passes again")
        check(fn.pushes[-1]["priority"] == "2" and fn.pushes[-1]["expire"] == str(TEST_EXPIRE_S)
              and fn.pushes[-1]["sound"] == SOUND["test"], "a test alarm")
        fn.perms = dict(fn.perms, enableFutures=True)
        check(mode_prove(fn, etc, var, uid, lambda: clock[0], ack_later, code="c" * 64) == 4,
              "prove refuses a key that can trade")
        fn.perms["enableFutures"] = False
        fn.v3 = False
        bn = Binance(fn, vals["binance-key"], vals["binance-secret"], lambda: clock[0])
        check(bn.positions() == raw and bn.position_path == "/fapi/v2/positionRisk", "v2 where v3 is not served")
        fn.v3 = True
        # -- the guard's cycle: three stages, a short's ------------------------------------------------------------------
        creds, _p = read_credentials(etc, uid)
        notes = []
        g = Guard(creds, net=fn, now=lambda: clock[0], var=var, uid=uid, notify=notes.append)
        key = "YFIUSDT:SHORT"

        def at(*liqs, btc=None):
            fn.positions = [dict(raw[0], liquidationPrice=str(liqs[0]))] + (
                [dict(raw[1], markPrice=str(btc))] if btc else [])
        at(1700.0)
        n_push, n_tg = len(fn.pushes), len(fn.tg_sent)
        g.cycle()
        check(g.key_ok is True and g.polls_ok == 1 and len(fn.pushes) == n_push and len(fn.tg_sent) == n_tg,
              "first cycle: 6.5%% from liquidation, nothing sent; the prove's answers confirmed, not read as commands")
        base = len(fn.pushes)
        for liq, want, prio in ((1670.0, 1, "1"), (1640.0, 1, "2"), (1630.0, 0, None), (1615.0, 1, "2")):
            clock[0] += 5
            at(liq)
            g.cycle()
            check(len(fn.pushes) - base == want and (prio is None or fn.pushes[-1]["priority"] == prio),
                  "liq %s: pushes %d" % (liq, len(fn.pushes) - base))
            base = len(fn.pushes)
        alarm = fn.pushes[-1]
        check(alarm["retry"] == "30" and alarm["title"].startswith("🔴 YFI SHORT · 🆘") and "Добавь" in alarm["message"]
              and alarm["sound"] == SOUND["liq3"] and alarm["url"] == BINANCE_URL % "YFIUSDT"
              and alarm["token"] == vals["pushover-token"] and "4242" not in alarm["message"],
              "the last stage's call, through the main application where no short one is: %r" % alarm["title"])
        card = fn.tg_sent[-1]
        check(card["parse_mode"] == "HTML" and card["reply_markup"]["inline_keyboard"][1][0]["callback_data"] ==
              "eng:" + key and g.watch[key]["card"] == fn.next_id and len(g.alarms) == 2, "the live card and two calls")
        # -- acknowledged: he is at work; silence but the last line; margin added ------------------------------------
        r2, r3 = list(g.alarms)
        fn.receipts[r3].update(acknowledged=1, acknowledged_at=int(clock[0]))
        e0 = len(fn.tg_edits)
        clock[0] += RECEIPT_EVERY_S
        g.cycle()
        check(g.engaged(key) and fn.receipts[r2].get("cancelled") and not g.alarms
              and "Ты в деле" in fn.tg_edits[-1]["text"] and len(fn.tg_edits) > e0, "acknowledged: engaged, quiet")
        base = len(fn.pushes)
        clock[0] += 5
        at(1610.0)
        g.cycle()
        check(len(fn.pushes) == base, "under the last line, within three minutes of his work: silent")
        clock[0] += LAST_QUIET_S
        g.cycle()
        clock[0] += 5
        g.cycle()
        check(len(fn.pushes) == base + 1 and "🆘" in fn.pushes[-1]["title"] and fn.pushes[-1]["priority"] == "2",
              "the last line rings once")
        sent0 = len(fn.tg_sent)
        clock[0] += 5
        at(1700.0)
        g.cycle()
        check(not g.watch and not g.alarms and "Маржа добавлена" in fn.tg_edits[-1]["text"]
              and any("ликвидация отодвинута" in m["text"] and m["disable_notification"] for m in fn.tg_sent[sent0:]),
              "margin added: the card closed, a quiet word, his work over")
        # -- «Я в деле» in Telegram, a stranger's button ignored, the timeout calls again ----------------------------------
        clock[0] += 5
        at(1640.0)
        g.cycle()
        rid = list(g.alarms)[0]
        fn.updates = [{"update_id": 30, "callback_query": {"id": "c1", "from": {"id": 4242}, "data": "eng:" + key,
                                                           "message": {"chat": {"id": 4242}}}},
                      {"update_id": 31, "callback_query": {"id": "c2", "from": {"id": 9999}, "data": "eng:" + key,
                                                           "message": {"chat": {"id": 9999}}}}]
        clock[0] += 5
        g.cycle()
        check(g.engaged(key) and fn.receipts[rid].get("cancelled") and len(fn.tg_answers) == 1
              and "молчат" in fn.tg_answers[0]["text"] and g.tg_offset == 32, "«Я в деле» from his chat alone")
        base = len(fn.pushes)
        clock[0] += ENGAGE_S
        g.cycle()
        check(len(fn.pushes) == base + 1 and "⏰" in fn.pushes[-1]["title"] and fn.pushes[-1]["priority"] == "2"
              and not g.engaged(key), "ten minutes on, the danger still there: called again")
        clock[0] += 5
        at(1800.0)
        g.cycle()
        check(not g.watch and not g.alarms, "the danger over: no watch, no open call")
        # -- gains: a long's records and retreats through its own application; kept across a restart -----------------
        base = len(fn.pushes)
        for mk in (95000, 96400, 99300, 96000, 94500):
            clock[0] += 5
            at(1800.0, btc=mk)
            g.cycle()
        gp = fn.pushes[base:]
        check([x["title"] for x in gp] == ["🟢 BTC LONG · 💰 +7,1% от входа", "🟢 BTC LONG · 💰 +10,3% от входа",
                                           "🟢 BTC LONG · ↩️ откат: отдано 35%", "🟢 BTC LONG · ↩️ ушла половина прибыли"]
              and all(x["token"] == vals["pushover-long"] and x["priority"] == "1" for x in gp)
              and gp[0]["sound"] == SOUND["record"] and gp[2]["sound"] == SOUND["pullback"], "gains: %r" % [
                  x["title"] for x in gp])
        g.save_state()
        mem = json.load(open(os.path.join(var, "memory.json")))
        check(abs(mem["BTCUSDT:LONG"]["rec"] - 100 * (99300 / 90000 - 1)) < 1e-9 and mem["BTCUSDT:LONG"]["pb"] == 2,
              "the gains' memory written")
        g2 = Guard(creds, net=fn, now=lambda: clock[0], var=var, uid=uid, notify=notes.append)
        g2.cycle()
        check(len(fn.pushes) == base + 4 and g2.mem["BTCUSDT:LONG"]["pb"] == 2, "a restart tells nothing again")
        # -- a gain while he works: held, then told quietly ----------------------------------------------------------------
        clock[0] += 5
        at(1640.0, btc=94500)
        g.cycle()
        fn.updates = [{"update_id": 40, "callback_query": {"id": "c3", "from": {"id": 4242}, "data": "eng:" + key,
                                                           "message": {"chat": {"id": 4242}}}}]
        clock[0] += 5
        g.cycle()
        base = len(fn.pushes)
        clock[0] += 5
        at(1640.0, btc=103400)
        g.cycle()
        check(g.engaged(key) and len(fn.pushes) == base and g.held == {"BTCUSDT:LONG": "record"}, "a record held")
        sent0 = len(fn.tg_sent)
        clock[0] += 5
        at(1800.0, btc=103400)
        g.cycle()
        check(not g.held and any("Пока ты был в деле" in m["text"] and m["disable_notification"]
                                 for m in fn.tg_sent[sent0:]), "told quietly once his work is over")
        # -- commands: status, thresholds, target, profit, settings, a stranger, the test, a word not a command -----------
        sent0 = len(fn.tg_sent)
        words = ["Статус", "Пороги 6 4 2", "Цель 7", "Прибыль 0", "Настройки", "Тест", "абв"]
        fn.updates = [{"update_id": 50 + k, "message": {"text": w, "chat": {"id": 4242, "type": "private"}}}
                      for k, w in enumerate(words)]
        fn.updates.insert(2, {"update_id": 49, "message": {"text": "Пороги 9 8 7", "chat": {"id": 9999,
                                                                                         "type": "private"}}})
        clock[0] += 5
        g.cycle()
        clock[0] += 5
        g.cycle()
        texts = [m["text"] for m in fn.tg_sent[sent0:]]
        check(g.th == (6.0, 4.0, 2.0) and g.target == 7.0 and g.profit_from == 0.0 and g.tg_offset == 57
              and all(m["chat_id"] == 4242 for m in fn.tg_sent), "commands from the pinned chat alone: %r" % (g.th,))
        check(any(t.startswith("🛡 <b>Сторож</b>") and "✅ на посту" in t for t in texts)
              and sum("Настройки сторожа" in t for t in texts) >= 4 and any("на кнопках" in t for t in texts),
              "status, settings and a hint answered: %r" % [t[:30] for t in texts])
        check(g.test is not None and fn.pushes[-1]["expire"] == str(TEST_EXPIRE_S), "the test alarm sent")
        fn.receipts[g.test["receipt"]].update(acknowledged=1, acknowledged_at=int(clock[0]))
        clock[0] += RECEIPT_EVERY_S
        g.cycle()
        check(g.test is None and any("Звонок дошёл" in m["text"] for m in fn.tg_sent), "the test acknowledged")
        st = json.load(open(os.path.join(var, "state.json")))
        check(st["thresholds"] == [6.0, 4.0, 2.0] and st["target"] == 7.0 and st["profit_from"] == 0.0,
              "settings kept")
        base = len(fn.pushes)
        clock[0] += 5
        at(1800.0, btc=120000)
        g.cycle()
        check(len(fn.pushes) == base, "gains off: a record told nowhere")
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
        check(g.blind and len(fn.pushes) == n0 + 1 and fn.pushes[-1]["priority"] == "1"
              and fn.pushes[-1]["title"].startswith("⚪ Сторож не видит Binance"), "blind once")
        check("positions" in fn.pushes[-1]["message"], "the blind alarm names Binance's own error")
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
            at(1800.0)
            clock[0] += 5
            g.cycle()
            n0 = len(fn.pushes)
            at(1625.0)
            clock[0] += STATE_S
            g.cycle()
        finally:
            os.open = real_open
        check(len(fn.pushes) == n0 + 1 and g.disk_faults > faults0, "a full disk stops no alarm")
        # Pushover down: the alarm waits in the outbox, then goes
        fn.down.add(PUSHOVER)
        at(1800.0)
        clock[0] += 5
        g.cycle()
        at(1620.0)
        clock[0] += 5
        g.cycle()
        check(any(m["to"] == "push" for m in g.outbox), "an alarm kept while Pushover is down")
        fn.down.discard(PUSHOVER)
        n0 = len(fn.pushes)
        clock[0] += 5
        g.cycle()
        check(len(fn.pushes) == n0 + 1 and not any(m["to"] == "push" for m in g.outbox), "sent once it is up")
        at(1800.0)
        clock[0] += 5
        g.cycle()
        check(not g.watch, "the danger over")
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
        hb = [m for m in fn.tg_sent if m["text"].startswith("🌙 <b>Сторож на посту</b>")]
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
        blob += b"".join(open(os.path.join(var, f), "rb").read() for f in ("state.json", "prove.json", "memory.json"))
        check(all(v.encode() not in blob for v in vals.values()) and b"4242" not in blob, "no secret in the record")
        check(all(private_file_ok(os.path.join(jd, f), uid=uid) for f in os.listdir(jd))
              and all(private_file_ok(os.path.join(var, f), uid=uid) for f in ("state.json", "memory.json")),
              "journal, state and memory files 0600")
        check("WATCHDOG=1" in notes, "the watchdog notified")
        check(all(h in (FAPI, SAPI, PUSHOVER, TG, HC) for h, _m, _p in fn.log), "no other host")
        check(all(wellformed(m["text"]) for m in fn.tg_sent) and all(wellformed(m["text"]) for m in fn.tg_edits),
              "every message sent and every edit well formed")
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
# read and nothing else: three stages of calls as they near liquidation, their gains told (TZ-55, CANON PART VII).
# Installed byte for byte as /etc/systemd/system/liq-guard.service; its stop is systemctl disable --now. It never trades.
[Unit]
Description=Liquidation guard, the Boss's Binance Futures positions watched for liquidation and for their gains
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
UMask=0077
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
# TZ-55 B-DEPLOY - the liquidation guard's second version on the capture host, one sequence, each step gated on the
# one before it: the host and its memory; the first version installed at TZ-54's bytes; the second staged byte for
# byte and the first's bytes kept beside it; the first stopped - the Boss's positions unwatched from here until the
# second starts, while he answers the prove - and G-PROVE of the second from its staged copy; on a FAIL there, the first
# started again as it was. On PASS the second installed and restarted, G-UNIT and, 15 minutes on, G-LIVE; on a FAIL
# after the install, the first installed again and restarted. Started by the Executor or by the Boss with the same
# line, under systemd-run, so that no dropped connection ends it (TZ-55 section 3, step 10). Its log is
# /root/tz55-work/logs/60-deploy.log. The guard is never left stopped by this script.
exec >>/root/tz55-work/logs/60-deploy.log 2>&1
export LC_ALL=C TZ=UTC
set -u
W=/root/tz55-work
SVC=/root/liq-guard-svc
VAR=/var/lib/liq-guard
PY=/root/tz04a-env/venv/bin/python
UNIT=liq-guard.service
OLD="782efaa88e268bd6ace42e23dc192e279ae130bb7bdc23d2f4de4d628c4da66f  liq-guard.py
26f609134730e4b9080bcdddbf2365ba35b1f69ddc1633d538a250bd46bce920  liq-guard.service"
NEW="6b851f3f93578dadcb683d33969b4d235daf2c852dbdce74c66e978946ec840a  liq-guard.py
11bff792d802cbf1abe9ee4f496c24517cce0e63a0dbf6aa49f277b7cdc55157  liq-guard.service"
MEM_FLOOR=100663296        # the unit's MemoryMax, 96 MiB: the most it may hold (TZ-55 section 6)
PHASE=first                # first: the first version installed; second: the second installed

say() { printf '%s B-DEPLOY %s\n' "$(date -u +%FT%T.%3NZ)" "$*"; }
prop() { systemctl show "$UNIT" -p "$1" --value; }
props() { systemctl show "$UNIT" -p ActiveState -p SubState -p Result -p ExecMainStatus -p NRestarts -p MainPID \
          -p UnitFileState -p WatchdogUSec -p MemoryCurrent -p MemoryPeak | tr '\n' ' '; echo; }
grd() { "$PY" -B "$SVC/liq-guard.py" "$@"; }
state() { /usr/bin/python3 -I -B -c 'import json, sys; print(json.load(open(sys.argv[1])).get(sys.argv[2]))' \
          "$VAR/state.json" "$1"; }
sums() { (cd "$1" && printf '%s\n' "$2" | sha256sum -c -); }
first_back() {
    if [ "$PHASE" = second ]; then
        install -m 0600 -o root -g root "$W/first/liq-guard.py" "$SVC/liq-guard.py" &&
        install -m 0600 -o root -g root "$W/first/liq-guard.service" "$SVC/liq-guard.service" &&
        install -m 0644 -o root -g root "$W/first/liq-guard.service" "/etc/systemd/system/$UNIT" &&
        systemctl daemon-reload && sums "$SVC" "$OLD"
        say "the first version installed again, exit=$?"
    fi
    systemctl restart "$UNIT"
    say "the first version restarted, exit=$?; read in 30 s"
    sleep 30
    say "the first version: $(props)"
}
fail() {
    say "FAIL at $1"
    first_back
    say "END exit=1"
    exit 1
}

say "BEGIN pid $$"
H1=$(find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit)
H2=$(df -B1 --output=source,size /var/lib/btc-recorder | tail -n 1 | tr -s ' ')
H3=$(grep -c e3975b5da44c5328adf3bf3914634cd878842c73 /var/lib/btc-recorder/runtime.jsonl)
say "host: a manifest ${H1:+found}; $H2; runtime.jsonl names e3975b5 $H3 times"
if ! { [ -n "$H1" ] && [ "$H2" = "/dev/vda2 31612203008" ] && [ "${H3:-0}" -ge 1 ]; }; then
    say "FAIL at the host: not the capture host"; say "END exit=1"; exit 1
fi

# -- 1. what is installed: the second already - G-LIVE alone; the first - the whole sequence; anything else - nothing --
if sums "$SVC" "$NEW" >/dev/null 2>&1 && [ "$(prop ActiveState)" = active ]; then
    say "the second version is installed and active already: $(props)"
    PHASE=second
else
    if ! sums "$SVC" "$OLD"; then
        say "FAIL at the install: the installed guard is neither version - nothing changed"; say "END exit=1"; exit 1
    fi
    say "the first version installed: $(props)"

    # -- 2. memory, read up to five times a minute apart (map section 7 item 137) ---------------------------------------
    for i in 1 2 3 4 5; do
        avail=$(awk '/^MemAvailable:/ {print $2 * 1024}' /proc/meminfo)
        say "MemAvailable read $i: $avail bytes, the floor $MEM_FLOOR"
        [ "$avail" -ge "$MEM_FLOOR" ] && break
        [ "$i" = 5 ] && { say "FAIL at memory: under the floor at five reads - nothing changed"; say "END exit=1"; exit 1; }
        sleep 60
    done

    # -- 3. the second staged byte for byte; the first's bytes kept beside it ---------------------------------------------
    install -d -m 0700 -o root -g root "$W/inst" "$W/first" || fail "install: the staged copies"
    install -m 0600 "$W/stage/guard/liq-guard.py" "$W/inst/liq-guard.py" || fail "install: the staged guard"
    install -m 0600 "$W/stage/deploy/systemd/liq-guard.service" "$W/inst/liq-guard.service" || fail "install: staged unit"
    sums "$W/inst" "$NEW" || fail "install: the staged bytes"
    install -m 0600 "$SVC/liq-guard.py" "$W/first/liq-guard.py" || fail "install: the first's guard kept"
    install -m 0600 "$SVC/liq-guard.service" "$W/first/liq-guard.service" || fail "install: the first's unit kept"
    sums "$W/first" "$OLD" || fail "install: the first's bytes kept"

    # -- 4. G-PROVE, once for this code, the first stopped while it runs: one poller of the bot at a time -------------------
    if /usr/bin/python3 -I -B - "$W/inst/liq-guard.py" "$VAR/prove.json" <<'EOF'
import hashlib, json, os, sys
code = hashlib.sha256(open(sys.argv[1], "rb").read()).hexdigest()
rec = json.load(open(sys.argv[2])) if os.path.exists(sys.argv[2]) else {}
sys.exit(0 if rec.get("code_sha256") == code and rec.get("pass") is True else 1)
EOF
    then
        say "G-PROVE read PASS for this code already: not run again"
    else
        systemctl stop "$UNIT"
        say "the first version stopped, exit=$?: the positions unwatched until the second starts: $(props)"
        say "G-PROVE: the Boss answers twice in Telegram and acknowledges the test alarm, each within 15 minutes"
        "$PY" -B "$W/inst/liq-guard.py" prove || fail "G-PROVE"
    fi

    # -- 5. the second installed --------------------------------------------------------------------------------------
    PHASE=second
    install -m 0600 -o root -g root "$W/inst/liq-guard.py" "$SVC/liq-guard.py" || fail "install: the guard"
    install -m 0600 -o root -g root "$W/inst/liq-guard.service" "$SVC/liq-guard.service" || fail "install: its copy"
    install -m 0644 -o root -g root "$W/inst/liq-guard.service" "/etc/systemd/system/$UNIT" || fail "install: the unit"
    systemctl daemon-reload || fail "install: daemon-reload"
    sums "$SVC" "$NEW" || fail "install: the installed bytes"
    cmp "$SVC/liq-guard.service" "/etc/systemd/system/$UNIT" || fail "install: the unit file"
    [ -e "$VAR/service.log" ] && chmod 0600 "$VAR/service.log"
    ls -la "$SVC" "/etc/systemd/system/$UNIT" "$VAR/service.log"
    say "installed: $(props)"
    [ "$(prop LoadState)" = loaded ] && [ "$(prop UnitFileState)" = enabled ] || fail "install: the unit's state"

    # -- 6. G-UNIT ------------------------------------------------------------------------------------------------------
    systemctl restart "$UNIT" || fail "G-UNIT: restart"
    say "restarted; read in 60 s"
    sleep 60
    say "G-UNIT read: $(props)"
    grd status
    [ "$(prop ActiveState)" = active ] && [ "$(prop SubState)" = running ] && [ "$(prop NRestarts)" = 0 ] &&
        [ "$(prop UnitFileState)" = enabled ] && [ "$(prop WatchdogUSec)" = 5min ] || fail "G-UNIT: systemd's reads"
    [ "$(state key_ok)" = True ] && [ "$(state blind)" = False ] && [ "$(state polls_ok)" -ge 1 ] ||
        fail "G-UNIT: the guard's own state"
    tail -n 5 "$VAR/service.log" | grep -q '^SERVE start: key True, positions read ' || fail "G-UNIT: the start line"
    [ "$(stat -c %a "$VAR/service.log")" = 600 ] || fail "G-UNIT: service.log not 0600"
    say "G-UNIT PASS"
fi

# -- 7. G-LIVE, 15 minutes after the start ------------------------------------------------------------------------------
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
