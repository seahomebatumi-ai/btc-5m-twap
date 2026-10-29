# TZ-35 — the advisor's Telegram bot: ADV-3 on the Boss's Binance Futures coins, deployed as a system unit

**Canonical filename:** `TZ-35-advisor-bot.md`. The committed file takes this name and no other.

**Executor model: Claude Opus 5.5.** A long-lived process deployed as a system unit beside three capture units and two
archive timers, requests to two outside services, six new files and two removed.

**Required System Map revision:** `2026-10-29-a`.

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

**It re-issues the advisor bot's specification**, uploaded at `0968707` as `CryptoTZ/TZ-34-advisor-bot.md` against
revision `2026-10-28-a` and never executed: its number had gone seven minutes earlier to the reward book's archive's
TZ-34, which executed, and the Boss removed it from `main` at `ec5e2b3` (map §7 item 127). The rule, the engine, the bot
and the bot's self-test are that file's byte for byte; the unit differs from it in its first line alone, a comment that
now names this TZ; the checker is this TZ's own; and every gate, floor and band is read against revision
`2026-10-29-a` and the host it records. **§0.5 BLOCKs where `CryptoTZ/` on `main` holds another file of this number, or
`CryptoReports/` a report of it** — item 127's repair of the class.

**Before `EXECUTE TZ-35` — the Boss's three steps, §0.6:** the bot created with Telegram's `@BotFather` and its token
written by the Boss himself to `/etc/adv3-bot/token` on the host, by §0.6's command, never into a chat, a file of the
repository or a report — both once, and skipped where that file holds the bot's token already; and `/start` sent to the
bot from his own Telegram within the 24 h before the run. H6 reads the token's shape and never its value; §3.7 waits up
to 1,800 s for the `/start` where none is pending.

**When:** any time after the upload that carries this TZ, while `/dev/vda2` holds at least `7,400,000,000` bytes free
(§0.4). **§3.8 waits for 06:35:00 to 22:30:00 UTC before anything is installed**, clear of the package manager's morning
runs and of both archives' calendar runs, the reward book's at 01:30:20 and the pair book's at 03:00:20 (map §3, §6, §7
items 115 and 120). About 1 h 30 min of wall clock (§6), most of it §3.11's wait for a run of the pair book's archive
that this TZ's own reloads of systemd may set off.

**What this TZ is.** The Boss trades Binance Futures by hand and asked on 2026-10-28 for an assistant that tells him
LONG or SHORT, on his own coins, in Telegram, on his command and every morning, without trading for him (CANON PART
VII). ADV-3 is that assistant's rule, frozen before any of its results was computed. **This TZ deploys it as one unit,
`adv3-bot.service`**: a Telegram bot that answers the Boss's «сигнал» and «сигнал 15000 0.5» in his one chat and sends
the day's signals at 06:00 UTC, 10:00 in Batumi — the three strongest trends first, STRONG where the rule's strength
test says so, each with its entry, stop, three targets and the share of past trades that reached each, its size for
the deposit and risk asked and its isolated leverage. It reads Binance's USDⓈ-M perpetuals' own daily candles, funding
and mark prices from `fapi.binance.com`, and nothing of the Boss's account. **It retires ADV-2 in the same pull
request**, so that the merge which lands ADV-3's code stops ADV-2's daily comment. Before anything is installed it
reproduces two things on the host: the facts its message quotes, from Binance's archive (G-HISTORY), and the equality
of its live source and that archive on 588 closed candles (G-SAME). It measures nothing about the market to come.

---

## 0. Gates

### 0.0 The work tree, first

After contract §1 steps 1 and 2, and before anything else:

```
mkdir /root/tz35-work /root/tz35-work/logs; echo "exit=$?"
```

`exit=0` proves neither existed; anything else is BLOCKED. **From here every command's output goes to
`/root/tz35-work/logs/`, one file per step, `NN-<step>.log` in this TZ's order**, and nothing to the session's
scratchpad. The one exception is B-RECLAIM-OWN, §9.

### 0.1 The files, staged

Extract Appendix A from this TZ as the primary checkout carries it after contract §1's pull, with this script,
verbatim, its one argument the destination:

```
/root/tz04a-env/venv/bin/python -B - /root/tz35-work/stage <<'EOF'
import hashlib, os, sys
SRC = "/root/btc-5m-twap/CryptoTZ/TZ-35-advisor-bot.md"
DEST = sys.argv[1]
WANT = {
    "advisor/RULE-ADV-3.txt": "ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169",
    "advisor/adv3.py": "7f2863a5b433ed7008c8f44af4f9c59d724d0c016c2c317f451158899c4f9adb",
    "advisor/adv3-bot.py": "e65de91c7b49c6f932db91e568a5956c005e63119c1cf6fb8724ffb0438d1dcb",
    "advisor/selftest-adv3.py": "76bad371727e0d4bf13c1d009f1b8f9412133a33788c456ecd53d1f83df6f0e6",
    "deploy/systemd/adv3-bot.service": "82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66",
    "research/tz35-advisor-deploy.py": "d50787db5113c3f748806a60a3e71211b665cb5235296e43d0e9a747a529e6f5",
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
| `advisor/RULE-ADV-3.txt` | 33 | 3,203 | `ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169` |
| `advisor/adv3.py` | 718 | 35,479 | `7f2863a5b433ed7008c8f44af4f9c59d724d0c016c2c317f451158899c4f9adb` |
| `advisor/adv3-bot.py` | 422 | 19,365 | `e65de91c7b49c6f932db91e568a5956c005e63119c1cf6fb8724ffb0438d1dcb` |
| `advisor/selftest-adv3.py` | 155 | 8,909 | `76bad371727e0d4bf13c1d009f1b8f9412133a33788c456ecd53d1f83df6f0e6` |
| `deploy/systemd/adv3-bot.service` | 27 | 863 | `82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66` |
| `research/tz35-advisor-deploy.py` | 802 | 42,049 | `d50787db5113c3f748806a60a3e71211b665cb5235296e43d0e9a747a529e6f5` |

A failed assert is BLOCKED. The staged checker runs §0.2's, §0.3's and §0.5's modes — §0.5's again in §3.1 — and, on a
BLOCK before §3.1's worktree exists, B-RECLAIM-OWN's `reclaim` (§3); it is written **`I0`**:
`nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz35-work/stage/research/tz35-advisor-deploy.py`.

### 0.2 Fingerprint

`I0 fingerprint` performs contract §1 steps 3 and 4 and asserts them, against `SYSTEM-MAP.md` and the files of its §0
table in the primary checkout `/root/btc-5m-twap`: revision `2026-10-29-a`; the six anchors; `A2`, `A4`, `A5` and `A6`
re-derived as the first 12 hex characters of those files' SHA-256; the table's **49** rows, each printed in lines,
bytes and SHA-256 — **46** `frozen` rows asserted equal to the map, **2** `tracked` and **1** `reported`. The map's own
row is the `reported` one, printed: `1,879` lines, `444,652` bytes and SHA-256
`e14b15d36a6119cbfc49dc2acf8e42463134c75395ac9031baeee9bd35ea042f` as `main` carries it since `6ae312c`. It prints
`FINGERPRINT PASS` or stops at the first mismatch, which is BLOCKED.

### 0.3 Host gate

From `/root/btc-5m-twap`, with `S` first set to the scratchpad directory the session's system prompt names:

```
I0 host
date -u; date -u +%s; uptime -s; journalctl --list-boots --no-pager | tail -n 3
nproc; grep -E '^(MemTotal|MemAvailable|SwapTotal|SwapFree):' /proc/meminfo
TZ=UTC systemctl show btc-recorder.service btc-pairbook.service btc-pairbook-archive.service btc-pairbook-archive.timer btc-rewardbook.service btc-rewardbook-archive.service btc-rewardbook-archive.timer btc-chainbook.service crypto-deploy.service crypto-announce.service -p Id -p MainPID -p NRestarts -p ActiveState -p SubState -p UnitFileState -p ActiveEnterTimestamp -p Result
TZ=UTC systemctl list-timers btc-pairbook-archive.timer btc-rewardbook-archive.timer apt-daily-upgrade.timer apt-daily.timer --all --no-pager
for u in btc-recorder.service btc-pairbook.service btc-pairbook-archive.service btc-pairbook-archive.timer btc-rewardbook.service btc-rewardbook-archive.service btc-rewardbook-archive.timer; do cmp deploy/systemd/$u /etc/systemd/system/$u; echo "$u cmp exit=$?"; done
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
systemctl is-active telemetry-watch.service; echo "exit=$?"
for d in /root/tz34-work /root/adv3-bot-svc /var/lib/adv3-bot /etc/adv3-bot; do test -e "$d"; echo "$d exit=$?"; done
ls -la /etc/adv3-bot
du -sb /var/lib/btc-rewardbook /var/lib/btc-pairbook /root/.claude
find /root/btc-forensics -type f | wc -l
git worktree list
echo "$S"; ls -la "$(dirname "$(dirname "$S")")"
```

`I0 host` asserts these, prints each with its value, writes the capture units' `MainPID`, `NRestarts` and states and
the pair book's archive's ledger's count of `restart` records into `/root/tz35-work/state.json`, and prints `READING
HOST: PASS` or fails:

- **H1** — `find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit` prints one path.
- **H2** — `df` names source `/dev/vda2` and size `31612203008`; `grep -c e3975b5da44c5328adf3bf3914634cd878842c73
  /var/lib/btc-recorder/runtime.jsonl` prints at least `1`. With H1 this is map §6's host identity.
- **H3** — `/root/tz04a-env/venv/bin/python` prints `3.12.`: the capture units' interpreter, which the bot runs under
  and which nothing in this TZ modifies.
- **H4** — `btc-recorder.service`, `btc-pairbook.service` and `btc-rewardbook.service` each read `ActiveState=active`
  and `UnitFileState=enabled`: G-STILL reads all three (§4.7), so this TZ needs them running.
- **H5** — `systemctl cat adv3-bot.service` exits non-zero, `/etc/systemd/system/adv3-bot.service`,
  `/root/adv3-bot-svc` and `/var/lib/adv3-bot` do not exist, and no process runs under the service's argv: nothing of
  the bot exists yet.
- **H6** — `/etc/adv3-bot` is a directory of mode `700` owned by root, and `/etc/adv3-bot/token` a regular file of mode
  `600` owned by root, at most 200 bytes, one line ending in a newline whose text is a Telegram bot token's shape —
  digits, a colon, 30 to 64 of `A–Z a–z 0–9 _ -`. **Its value is read by this test and by the bot alone, and printed by
  nothing.**
- **Memory gate** — `MemAvailable` at least `170,344,448` bytes (§0.4).
- **Disk gate** — `/dev/vda2` free at least `7,400,000,000` bytes (§0.4).

These are twelve checks — H2 two, H4 three, H5 two — and any one failing is BLOCKED. **The rest is printed and
carries no threshold:** the boots; the units and the timers, among them both archives' and the package manager's;
`cmp` of the seven installed project units against `main`'s; the consumer's two states, on which map §6's headroom is
conditional; `/root/tz34-work` gone and the bot's trees absent; the listing of `/etc/adv3-bot`, names, sizes and modes
alone; `du` of the reward book's and the pair book's stores beside `df`, as map §2.6 asks; the forensic store's count,
map §3's `2,151`; the worktrees, map §3's two; the records of the pair book's archive's deferred set `1793260762` in its
ledger — event names, deferral counts and times alone — which map §7 item 128 asks the next TZ to read; and the listing
of the directory that holds the session's own, whose UUID directories `I scratch` names live or earlier (§9). Map §3
records TZ-34's two left behind, `540c6c83…` and `57feec2d…`.

### 0.4 Resource floors, in exact bytes

**Disk.** `/dev/vda2` free at least **`7,400,000,000`** bytes: the reward book's `STREAM_FLOOR`, `7,300,000,000`, below
which no stream of it opens (map §2.6; `research/tz33-reward-book-capture.py` line 190), plus `100,000,000` for this
session at its upper bound — the worktree, about `10,300,000` bytes of tracked files, the logs under `2,000,000`,
`history.json` `19,362`, the service's copy `54,885`, the bot's root under `1,000,000` over the session, the forensic
store's copies under `5,000,000`. **This TZ never takes free space below the floor that pauses the reward book.** Since
2026-10-29 the reward book's archive moves its streams off the host every day and holds its store near one day's
streams, about `1.0` GB; TZ-34 read `11,126,394,880` bytes free at its closing read (map §2.6, §6). Where the disk gate
fails, the run is BLOCKED, and the archives' records are the next TZ's to read.

**Memory.** `MemAvailable` at least **`170,344,448`** bytes: twice the largest peak of any mode this TZ runs, in the
Architect's runs under Python 3.12.3 — `adv3.py --history`, `85,172,224` on 2026-10-29 and `83,587,072` and `83,005,440`
on 2026-10-28, on the frozen file, holding 42 coins' candles from 2019-09 and their funding. None of these bytes has run
on the host, so the Architect's measurement is the larger of map §7 item 131's two. The others: the service
`61,464,576` (`VmHWM` 60,024 kB) over twelve forced refetches of every coin, flat from the seventh, `adv3.py --compare`
`28,925,952`, `adv3-bot.py --probe` `26,624,000`, `--find-chat` `25,919,488` and `--hello` `25,935,872`, against
stand-ins for both services on 2026-10-28 on these bytes; `adv3-bot.py --selftest` `27,959,296` and `selftest-adv3.py`
`24,887,296` on 2026-10-29; and the checker's `reclaim` `23,863,296` over a stand-in tree and the 44 reports' hashes,
`fingerprint` `21,815,296`, `selftest` `19,496,960`, `mark` `19,308,544` and `number` `19,292,160` on 2026-10-29 — its
other modes read systemd, `/proc` and a few small files and load the standard library alone [modelled under the
`reclaim` figure]. **The service runs under its unit's `MemoryMax=128M`, `134,217,728` bytes, `2.18` times its measured
peak**, glibc's mmap threshold fixed at 128 KiB and its arenas at two, as the reward book's are (map §6). Map §6 records
the host: `1,002,127,360` bytes, one processor; TZ-34 read `MemAvailable` from `263,163,904` to `363,487,232` across its
session. Every mode of this TZ runs under `nice -n 19`, the service under systemd at `Nice=10`, below the recorder's and
the pair book's `0` and beside the reward book's `10`.

### 0.5 Refs and the number

`I0 number` and `git ls-remote origin` after §0.4, every ref reported; both again in §3.1 — `I0 number` after its
fetch, `git ls-remote origin` before its push. Map §1 records **84** ref lines read on 2026-10-29 at 09:53 UTC, PR #34's
merge ref among them; PR #34's merge, `6785590`, removed that ref, and `main` stood at
`ec5e2b35d1e0bf79b6756d61690e17b3e09e49e1` with **83** ref lines when the Architect read it, 2026-10-29 at 10:38 UTC —
`HEAD`, twelve branches with `main`, the two annotated tags and their peeled lines, thirty-two `pairbook-streams-*` tags,
one `rewardbook-streams-*` tag and thirty-three pull heads. Every run of either archive that takes a new set adds one
tag — the reward book's at 01:30:20 UTC and the pair book's at 03:00:20, and each possibly 1,800 s and 600 s after a
reload of systemd, respectively (map §7 items 115 and 129) — and a run that resumes a set adds none. Every commit on
`main`'s first-parent line above `6785590` is reported with the paths it changed — two at the Architect's read:
`6ae312c`, revision `2026-10-29-a` of `SYSTEM-MAP.md`, and `ec5e2b3`, which removes `CryptoTZ/TZ-34-advisor-bot.md` —
and the upload that carries this TZ above them. A difference is recorded, not BLOCKING, unless `main` does not carry revision
`2026-10-29-a`, does not carry `ADVISOR-SKILL.md` and `.github/workflows/adv2-signal.yml`, or
`refs/heads/tz-35-advisor-bot` already exists — each is BLOCKED.

**NUMBER — map §7 item 127's repair, and CANON hard rule 2's.** `I0 number` reads, in the primary checkout,
`git ls-tree --name-only origin/main -- CryptoTZ/ CryptoReports/` and must print `READING NUMBER: PASS - 2 of 2`:
`CryptoTZ/` holds `TZ-35-advisor-bot.md` and no other file whose name begins with `TZ-35-`, and `CryptoReports/` no
report whose name does. Anything else is BLOCKED, here and in §3.1 alike, so that two specifications carrying one
number stop before either does any work.

### 0.6 The Boss's three steps — before `EXECUTE TZ-35`

They are the Boss's because the token is a credential no session holds (the CANON's owner section). Steps 1 and 2 are
done once, and skipped where `/etc/adv3-bot/token` already holds the bot's token; step 3 within the 24 h before the run:

1. **The bot.** In Telegram, `@BotFather` → `/newbot` → any name, a username ending in `bot`. BotFather answers with the
   token.
2. **The token on the host**, in a root shell on the VPS — one line, which reads it without echo and writes it nowhere
   else:

   ```
   install -d -m 0700 /etc/adv3-bot && read -rsp 'Bot token: ' T && echo && (umask 077; printf '%s\n' "$(printf '%s' "$T" | tr -d '[:space:]')" > /etc/adv3-bot/token) && unset T && chmod 0600 /etc/adv3-bot/token && echo OK
   ```

3. **`/start`** — the bot opened in the Boss's own Telegram and its Start button pressed, within the 24 h before the run:
   Telegram keeps an unanswered update for 24 h, and §3.7 pins the one private chat that sent it.

**The token never enters a chat, the repository, a log or a report.** H6 checks step 2 by shape; §3.7's `--find-chat`
waits up to 1,800 s for step 3 where no `/start` is pending, and the Executor then tells the Boss once, in plain words,
to press Start in the bot P-START named.

---

## 1. Why this TZ exists

**The objective.** The Boss's own trading on Binance Futures, by hand: an advisor that says LONG, SHORT or out on
each of his 42 coins, puts the three strongest first and marks STRONG where it has reason to, gives an entry — at the
market or on a pullback — a stop and targets, sizes the trade for a deposit of 10,000 to 20,000 USDT at 0.5% of risk,
says how long the signal holds and how confident the history makes it, reads Binance's futures market and not its spot
market, and speaks in Telegram, on his «сигнал 5000 0.5» and every morning. CANON PART VII holds the advisor; it is not
a track and claims no edge.

**The rule, ADV-3, frozen 2026-10-28 16:14 UTC before any of its results was computed by anyone** — Appendix A's
`advisor/RULE-ADV-3.txt`, SHA-256 `ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169`, carried as `RULE`
in `adv3.py`. It is ADV-1's trend rule on the Boss's coins' own perpetuals: at each daily close the signs of the close
against the closes 14, 28, 56 and 112 days before are summed, `+2` or more LONG, `−2` or less SHORT, else out; a trade
opens at the close with its stop `U = 2N` away, `N` the mean true range of 20 days, and closes at the stop inside a day
or at the close where the signal changes; costs `0.10%` a side, the perpetual's own funding. Beside it a strength `z` —
the mean over the four lookbacks of the log return scaled by 56 days of daily volatility; TOP-3, the three largest
`|z|`; and STRONG, a TOP-3 coin whose four signs agree with its side and whose `|z|` is at least 1, with a strategy of
its own, at most three open.

**What the history says, read by the Architect on Binance's archive to the close of 2026-10-27 — Gate H and Gate S NOT
DISQUALIFIED, which confirms nothing:** the rule `5,265` trades, `1,708` profitable, mean `+0.1576` R a trade; the
STRONG strategy `253` trades, `83` profitable, mean `+0.5473` R, held a median of `19` days; the share of trades whose
price reached `+1`, `+2` and `+3` R before their exit `0.2325`, `0.1297` and `0.0819` for the rule and `0.4783`,
`0.2846` and `0.1779` for STRONG. These are `FACTS` in `adv3.py`, the figures the message quotes, fixed on 2026-10-28 and
read again to the same bytes on 2026-10-29, and G-HISTORY derives every one of them again on the host. **The forward
record begins at the close of 2026-10-28** and is read once, after 365 days, by a TZ of its own; nothing here reads it.

**Why the host.** `fapi.binance.com` answers `451` to a host in the United States — the Architect's sessions and
GitHub's runners alike — and the host is in Warsaw; its reach is unread, and P-START reads it before anything is
installed. Binance's archive, `data.binance.vision`, serves a day's file hours after the day closes, too late for a
message at 10:00 in Batumi; `fapi.binance.com` serves the closed candle at the close. **Why a unit:** CANON hard rule 14.
**What it costs the host:** a process of about `60` MB resident that waits on Telegram's long poll, about `1.4` s of
processor at its start and `0.7` to `1.3` s a message (§6).

**What it retires.** ADV-2 — `.github/workflows/adv2-signal.yml`, which comments ADV-2's signals on issue #33 every
day at 05:52 UTC from GitHub's servers, and `ADVISOR-SKILL.md`, the skill file that ran it in a Claude session — is
removed on this TZ's branch, so the merge that lands ADV-3's code also stops ADV-2's comment. ADV-2's forward record
was to begin at the same close as ADV-3's and never began. The skill saved in the Boss's accounts is the Architect's to
replace, at this TZ's verdict.

**Why a new number.** The advisor bot's specification reached `main` at `0968707`, seven minutes after the reward
book's archive's at `ca85b08`: two sessions of the Architect had taken the next free number from one `main`. That TZ-34
executed — its report is on `main` at `cfa0bf5` — so by CANON hard rule 5 the number is spent, and the advisor's
specification, never executed, is re-issued here (map §7 item 127). What moved between the two map revisions, and what
this TZ does about it: the reward book's archive's two units, installed and enabled, which §0.3 reads and §2 forbids to
touch; that archive's calendar run at 01:30:20 UTC and its elapse 1,800 s after a start of its timer, which §3.8's band
avoids and §3.8 and §3.9 name; the map's 49 rows (§0.2); TZ-34's two session directories, which §9 reclaims; a reload of
systemd possibly, not certainly, setting off the pair book's archive's run (map §7 item 129), which §3.8 and §4.7 say;
the memory floor taken from the larger of the Architect's and the host's peaks (item 131, §0.4); the pair book's
archive's deferred set, whose ledger records §0.3 and §3.11 print (item 128); and the number's own BLOCK (§0.5).

---

## 2. Scope

**Repository paths this TZ may write, and no others:**

1. On branch `tz-35-advisor-bot`, then a pull request, not merged by the Executor: **added**, byte for byte Appendix
   A's — `advisor/RULE-ADV-3.txt`, `advisor/adv3.py`, `advisor/adv3-bot.py`, `advisor/selftest-adv3.py`,
   `deploy/systemd/adv3-bot.service` and `research/tz35-advisor-deploy.py`; **removed** — `ADVISOR-SKILL.md` and
   `.github/workflows/adv2-signal.yml`, the two exemptions to item 1 of the prohibitions below.
2. `CryptoReports/TZ-35-advisor-bot-report.md` — straight to `main`, in one commit. **The one path pushed to `main`.**

**Host paths this TZ may write:** `/root/tz35-work/**`; `/root/adv3-bot-svc/`, the service's copy and its
`commit.txt`; `/etc/systemd/system/adv3-bot.service`, byte-identical to the branch's unit, with the link `systemctl
enable` makes; `/var/lib/adv3-bot/`, created empty by B-INSTALL and from then written by the unit alone;
`/etc/adv3-bot/chat-id`, written by `--find-chat` alone, mode `600`; `/root/btc-forensics/`, by exclusive create only
(§9); and in the primary checkout `/root/btc-5m-twap`, its `.git` for the branch and the worktree, and its
`CryptoReports/` for the report. **Host paths it removes, under §9 and B-UNINSTALL and nothing else:**
`/root/tz35-work/` with its worktree; the directories `I scratch` names earlier; and, on a BLOCK after §3.5 and before
B-ENABLE, the service's copy, the unit file and the empty root. K-35 removes the unit's enable link and nothing else.

**Prohibited, each absolutely:**

1. No committed file is modified but the two removals of item 1 above; every `frozen` row of map §0 is
   byte-identical at run end.
2. **Under `/var/lib/btc-recorder/` nothing is opened or listed but by `I0 host`'s `find`, `grep -c` and `df`**, map
   §6's host identity; under `/var/lib/btc-pairbook/` and `/var/lib/btc-rewardbook/` nothing but §0.3's and §3.12's
   `du`; under `/var/lib/btc-pairbook-archive/` nothing but `ledger.jsonl`, read only, by `host` and `still`; under
   `/var/lib/btc-rewardbook-archive/` and `/var/lib/btc-chainbook/` nothing. No price, size, side, book or outcome of
   any capture is read.
3. **No unit is created, started, stopped, enabled, disabled, signalled or changed but `adv3-bot.service`, by B-INSTALL,
   B-ENABLE, B-KILL and, on a FAIL, K-35, or on a BLOCK B-UNINSTALL.** `systemctl show`, `cat`, `is-active`,
   `is-enabled` and `list-timers`, `systemd-analyze verify`, `journalctl`, and §0.3's and B-INSTALL's `cmp` of unit
   files are this TZ's only other reads of a unit. The recorder, the pair book, the reward book and both archives are
   never signalled.
4. `/root/tz04a-env/`, `/root/tz01-env/`, `/root/tz18a-svc/`, `/root/btc-recorder-svc/`, `/root/btc-pairbook-svc/`,
   `/root/btc-pairbook-archive-svc/`, `/root/btc-rewardbook-svc/` and `/root/btc-rewardbook-archive-svc/` are not
   modified, and `/root/btc-forensics/` only by §9's exclusive create.
5. **The token and the chat id.** `/etc/adv3-bot/token` is never modified, copied, printed, logged or passed on a command
   line; it is read by `I0 host` for its shape and by the bot's own code. `/etc/adv3-bot/chat-id` is written by
   `--find-chat` and printed by nothing. No command prints the content of a file under `/etc/adv3-bot/`; §0.3's and
   §3.12's `ls -la` and §3.7's `stat` print names, sizes, modes and owners alone.
6. **Requests:** P-START's five, through the bot's own functions — `fapi.binance.com` `/fapi/v1/klines`,
   `/fapi/v1/fundingRate`, `/fapi/v1/premiumIndex` and `/fapi/v1/fundingInfo`, and Telegram `getMe`; `--find-chat`'s
   `getUpdates` and `--hello`'s `sendMessage`; G-SAME's — `/fapi/v1/klines` for the 42 coins and 588 daily kline files
   of `data.binance.vision`; G-HISTORY's — the 42 coins' monthly and daily kline files and monthly funding files there;
   the unit's own, to `fapi.binance.com` and Telegram; `git` against `origin`; and `gh` for the pull request. **Binance
   is read through its public market-data endpoints alone: no order, no account endpoint, no key** — contract §10's
   "never call a trading venue" is lifted for these reads and nothing else.
7. **Prints.** Nothing under `/var/lib/adv3-bot/` is printed but by the checker's modes and §3.12's `tail -n 30
   service.log`, which holds dates, counts, pids, coin names and errors, and no token and no chat id. The checker prints
   of the daily record its TOP-3, STRONG and each card's coin, side and mode, and of the pair book's archive's ledger
   the deferred set's event names, deferral counts and times. These prohibitions bind the Executor's own reads (map §7
   item 118).
8. Nothing is pushed to `main` except the report of item 2. No Release is created, and no dataset, archive or binary
   enters git history.

---

## 3. The work, in this order

From §3.1 on, `nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz35-work/wt/research/tz35-advisor-deploy.py` is
written **`I`**, a mode `I <mode>`, and `nice -n 19 /root/tz04a-env/venv/bin/python -B` is written **`P`**; every
command runs from `/root/tz35-work`, its output to `logs/`, one file per step, quoted in the report. **§9's
B-RECLAIM-SCRATCH runs after §3.3 and before §3.4; B-RECLAIM-OWN runs last.** On a BLOCK before §3.1's worktree exists,
B-RECLAIM-OWN runs with `I0` in place of `I` and without its `git worktree remove` line; on a BLOCK after §3.5 and before
B-ENABLE, B-UNINSTALL runs first (§4.8).

**Where the session's permission classifier refuses a command of a block named B-… or K-…**, the Executor prints the
block, the Boss runs it verbatim in a root shell on the VPS, and the Executor verifies it through the reads this TZ
names — never from the Boss's account. Map §7 item 124's rule holds: **a block is handed over only once its band is
open, so its own wait is seconds; it is one command line, every step after the first chained by `&&` to the one it
depends on; and it appends its output to its log under a `date -u` line.** Every `mark` is the Executor's, taken
immediately before its block is run or handed over. Map §6 records `systemctl enable --now` refused at TZ-20, TZ-26,
TZ-28 and TZ-33 — TZ-34 handed its own to the Boss by its text — and `systemctl kill` never.

### 3.1 The branch and its files

```
git -C /root/btc-5m-twap fetch origin
I0 number
git -C /root/btc-5m-twap worktree add -b tz-35-advisor-bot /root/tz35-work/wt origin/main
```

`I0 number` must print `READING NUMBER: PASS - 2 of 2` again (§0.5), or BLOCKED. Then §0.1's script again, verbatim
but for its argument, `/root/tz35-work/wt`; it must print the same lines, bytes and SHA-256 as at §0.1. Then:

```
git -C /root/tz35-work/wt rm -q ADVISOR-SKILL.md .github/workflows/adv2-signal.yml
git -C /root/tz35-work/wt add advisor deploy/systemd/adv3-bot.service research/tz35-advisor-deploy.py
git -C /root/tz35-work/wt diff --cached --name-status
```

The last must print exactly eight lines — `D` for `.github/workflows/adv2-signal.yml` and `ADVISOR-SKILL.md`, `A` for
the six files of Appendix A — or BLOCKED. Commit them alone; `git ls-remote origin` (§0.5); push with `git push -u
origin tz-35-advisor-bot` — through `credential.helper=!gh auth git-credential` where the URL's credential is refused
(map §6, git remote) — and open the pull request against `main`. A failed assert here is BLOCKED.

### 3.2 The self-tests

```
P wt/advisor/selftest-adv3.py
P wt/advisor/adv3-bot.py --selftest
I selftest
```

They must print `SELFTEST-ADV3 PASS: 32 of 32 checks passed`, `SELFTEST PASS: 19 of 19 checks passed` and `SELFTEST
PASS: 24 of 24 checks passed`. They reach no network. A red self-test stops the run here, and it goes to §3.12 and §9.

### 3.3 The directories beside this session

`I scratch "$(dirname "$S")"` lists every UUID directory beside this session's own and names each **live** — born from
1 s before to 60 s after the start of a running process whose `argv[0]` is `claude` or ends in `/claude.exe` — or
**earlier**. Then B-RECLAIM-SCRATCH, §9.

### 3.4 The two reproductions — G-SAME and G-HISTORY

```
timeout 900 P wt/advisor/adv3.py --compare
timeout 1800 P wt/advisor/adv3.py --history /root/tz35-work/history.json
sha256sum /root/tz35-work/history.json; wc -c /root/tz35-work/history.json
```

**G-SAME** must print `READING G-SAME: PASS`; **G-HISTORY** must print `READING G-HISTORY: PASS - 16 of 16 equal`, and
the history file must be `19,362` bytes with SHA-256 `bcee53097f9f1a5820b551c90054a3f046c027f53cff868b857be3118c74faa1`
— **DETERMINISM**, the bytes the Architect's three runs wrote (§4.2). Anything else, a timeout included, is BLOCKED, and
nothing is installed.

### 3.5 The service's copy

```
mkdir /root/adv3-bot-svc; echo "exit=$?"
git -C /root/tz35-work/wt show origin/tz-35-advisor-bot:advisor/adv3.py > /root/adv3-bot-svc/adv3.py
git -C /root/tz35-work/wt show origin/tz-35-advisor-bot:advisor/adv3-bot.py > /root/adv3-bot-svc/adv3-bot.py
git -C /root/tz35-work/wt rev-parse origin/tz-35-advisor-bot > /root/adv3-bot-svc/commit.txt
I copy
```

`mkdir` exits `0` and `I copy` prints `READING COPY: PASS - 4 of 4`, or BLOCKED.

### 3.6 The request path — P-START

```
P /root/adv3-bot-svc/adv3-bot.py --probe
```

It must print `READING P-START: served - 5 of 5 endpoints` (§4.1). **A failed assert is BLOCKED, and nothing is
installed or started.**

### 3.7 The chat — G-CHAT and G-HELLO

```
P /root/adv3-bot-svc/adv3-bot.py --find-chat
P /root/adv3-bot-svc/adv3-bot.py --hello
stat -c '%a %U %s %n' /etc/adv3-bot/chat-id
```

`--find-chat` must print `private chats that sent /start: 1 | chat pinned to /etc/adv3-bot/chat-id` — where it first
prints that it is waiting, the Executor tells the Boss once to press Start in the bot P-TELEGRAM named — and exit `0`;
`--hello` must print `G-HELLO sent: message ids` and a list of one integer; `stat` must print mode `600`, owner `root`.
Anything else is BLOCKED.

### 3.8 Install — B-INSTALL

First wait for the band, then `I mark install`, then the block:

```
until s=$(( $(date +%s) % 86400 )); [ $s -ge 23700 ] && [ $s -le 81000 ]; do sleep 5; done; date -u +%FT%T.%NZ
```

**B-INSTALL:**

```
until s=$(( $(date +%s) % 86400 )); [ $s -ge 23700 ] && [ $s -le 81000 ]; do sleep 5; done; { date -u +%FT%T.%NZ; install -m 0644 /root/tz35-work/wt/deploy/systemd/adv3-bot.service /etc/systemd/system/adv3-bot.service && cmp /root/tz35-work/wt/deploy/systemd/adv3-bot.service /etc/systemd/system/adv3-bot.service && install -d -m 0700 /var/lib/adv3-bot && systemctl daemon-reload; echo "exit=$?"; systemd-analyze verify /etc/systemd/system/adv3-bot.service; echo "verify exit=$?"; } >> /root/tz35-work/logs/08-b-install.log 2>&1
```

06:35:00 to 22:30:00 UTC is seconds `23,700` to `81,000` of the day. `exit=0` or BLOCKED and nothing is started;
`systemd-analyze verify` is recorded — its findings may name other units on this host, and G-UNIT decides. Then
`I props` — **PROPS**, the installed unit's settings as systemd reads them before its first start — must print
`READING PROPS: PASS - 11 of 11`, or BLOCKED, B-UNINSTALL, and nothing is started. **The root is created here, before
the first start**, because systemd opens the unit's `append:` log under it before the process runs. **The reload may set
off a run of the pair book's archive 600 s later**, which restarts the pair book inside its band and which G-STILL
counts from that archive's ledger (§4.7), **and a run of the reward book's archive 1,800 s later**, which restarts
nothing (map §2.6, §7 items 115, 125 and 129): possible, not certain. If more than 3,600 s pass after P-START's exit
before B-ENABLE, §3.6 runs again once, into its own log, first.

### 3.9 The start — B-ENABLE, then G-UNIT, G-DAILY, G-REPLY and G-LOAD

`I mark start`, then **B-ENABLE:**

```
until s=$(( $(date +%s) % 86400 )); [ $s -ge 23700 ] && [ $s -le 81000 ]; do sleep 5; done; { date -u +%FT%T.%NZ; systemctl enable --now adv3-bot.service; echo "exit=$?"; } >> /root/tz35-work/logs/09-b-enable.log 2>&1
```

The service starts after 06:00 UTC on a day whose daily message is not yet sent, so **it sends the day's message at
once**: it is the Boss's first ADV-3 message, and G-DAILY reads it. The enable reloads systemd and may set off either
archive's run again, 600 s and 1,800 s later. At least 60 s after the block: `I unit 0` — **G-UNIT** at no restart —
and `I daily` — **G-DAILY** and **G-REPLY**, again every 30 s while it prints `NOT YET` and exits `3`. At least 300 s
after the block: `I load` — **G-LOAD**, over the first process from its start.

### 3.10 The restart — B-KILL, then G-RESTART, G-ONCE and G-UNIT at one restart

Only after every reading of §3.9 is PASS. `I mark kill`, then **B-KILL:**

```
until s=$(( $(date +%s) % 86400 )); [ $s -ge 23700 ] && [ $s -le 85800 ]; do sleep 5; done; { date -u +%FT%T.%NZ; systemctl kill --signal=SIGTERM adv3-bot.service; echo "exit=$?"; } >> /root/tz35-work/logs/10-b-kill.log 2>&1
```

Its band, 06:35:00 to 23:50:00 UTC, keeps the restart inside the UTC day of the message it must not send again. At
least 45 s later — `RestartSec=30` and the start: `I restart` — **G-RESTART** and **G-ONCE** — then `I unit 1`.

### 3.11 G-STILL

`I still`, again every 120 s while it prints `NOT YET` and exits `3`: it waits until the pair book's archive's run set
off by the last reload of systemd has started and ended, or 1,200 s have passed after that reload with none started,
and at most 4,200 s; then reads **G-STILL** (§4.7), and prints the deferred set's ledger records again.

### 3.12 The closing reads

```
TZ=UTC systemctl show adv3-bot.service btc-recorder.service btc-pairbook.service btc-rewardbook.service btc-pairbook-archive.service btc-rewardbook-archive.service -p Id -p MainPID -p NRestarts -p ActiveState -p Result -p Nice -p MemoryCurrent -p MemoryPeak -p ActiveEnterTimestamp
TZ=UTC systemctl list-timers btc-pairbook-archive.timer btc-rewardbook-archive.timer --all --no-pager
systemctl is-enabled adv3-bot.service; echo "exit=$?"
journalctl -u adv3-bot.service --no-pager -o short-iso | tail -n 20
tail -n 30 /var/lib/adv3-bot/service.log
ls -la /var/lib/adv3-bot /root/adv3-bot-svc /etc/adv3-bot
free -b; df -B1 --output=source,size,avail /var/lib/btc-recorder
du -sb /root/tz35-work /root/adv3-bot-svc /var/lib/adv3-bot /var/lib/btc-rewardbook /var/lib/btc-pairbook /root/.claude
cat /root/tz35-work/state.json
```

The journal holds systemd's own lines for the unit; `service.log` the service's own, one line a start, a refresh, a
message and a failure, with no token and no chat id.

---

## 4. The gates — fixed here, before any of their data exists

| gate | population | PASS | false failure | power, against |
|---|---|---|---|---|
| **G-SAME** | the 42 coins × the 14 closed days before the run: each day's archive file and `fapi.binance.com`'s candle | no candle compared differs, and at least 12 compared for every coin (§4.2) | `0` — the venue's two publications compared field by field | `1`, any differing open, high, low or close among those compared |
| **G-HISTORY** | the rule and the STRONG strategy on the 42 coins' archive history to the close of 2026-10-27 | 16 of 16 facts equal to `FACTS`, and the file's bytes the Architect's | `0` — one function on the archive's files; a republished candle is itself a finding | `1`, a fact mistyped into `FACTS`, or a history not the Architect's |
| **COPY** | the service's copy | 4 of 4 (§4.3) | `0` | `1`, a file not Appendix A's or not the branch head's |
| **PROPS** | the installed unit, before its first start | 11 of 11 (§4.3) | `0` — systemd's own reading | `1`, a setting systemd reads otherwise than the unit file means |
| **P-START** | five endpoints, one request each | served and parsed (§4.1) | `0` — each read directly | `1`, a refused request — `451`, `403` — or a reply of another shape |
| **G-CHAT**, **G-HELLO** | the bot's pending updates, up to 1,800 s; one message | one private chat sent `/start`; a message id | `0` | `1`, no chat or two, or a refused message |
| **G-UNIT** | the unit at `0` and at `1` restart | 18 of 18 each (§4.3) | `0` | `1`, a process outside its unit, unhardened, at another priority, beside a second instance, or not Appendix A's |
| **G-DAILY**, **G-REPLY** | the first process's log and journal from the `start` mark | 8 of 8 and 1 of 1 (§4.4) | `0` | `1`, a daily not sent, sent twice, of another close or with a coin not served; the Boss's `/start` unanswered |
| **G-LOAD** | the first process, from its start, at least 300 s | its processor time at most `0.05` of the wall time | `0` — `/proc` read directly | `1`, a process above it |
| **G-RESTART**, **G-ONCE** | the unit and its records after the `kill` mark | 5 of 5 and 2 of 2 (§4.5) | `0` | `1`, a `SIGTERM` not restarted within 60 s, or a second daily after it |
| **G-STILL** | the three capture units from §0.3 to §3.11 | 3 of 3 (§4.7) | `0` outside the package manager's runs, which the band avoids | `1`, a restart or a stop not the pair book's archive's |

**Family-wise false failure `0`:** every gate reads its quantity directly and none samples. A FAIL of G-SAME,
G-HISTORY, COPY, P-START, G-CHAT or G-HELLO comes before anything is installed, and one of PROPS before anything is
started — each is BLOCKED; a FAIL after B-ENABLE stops the unit (§4.8).

### 4.1 P-START

CANON hard rule 14's proof, through the bot's own request functions in the service's copy: `adv3.get`, one GET a
request, and `Telegram.call`, one JSON POST a call. **P-KLINES** — `/fapi/v1/klines?symbol=BTCUSDT&interval=1d&limit=1500`
serves closed daily candles, the last at most two days old, each four positive prices; **P-FUNDING** —
`/fapi/v1/fundingRate?symbol=BTCUSDT&startTime=<2026-10-27 00:00 UTC>&limit=1000` serves settlements, each a number;
**P-MARKS** — `/fapi/v1/premiumIndex` serves a positive mark price for every one of the 42 coins' perpetuals;
**P-INTERVALS** — `/fapi/v1/fundingInfo` serves the perpetuals whose funding interval Binance has adjusted, each a
positive number of hours; **P-TELEGRAM** — `getMe` answers `is_bot` true and a username, which it prints. **Every
header fixed:** to Binance `User-Agent: adv3-advisor/1`, beside `urllib`'s own `Accept-Encoding: identity`, `Host` and
`Connection: close`; to Telegram `User-Agent: adv3-bot/1` and `Content-Type: application/json`, beside `urllib`'s
`Content-Length`, `Accept-Encoding: identity`, `Host` and `Connection: close`. A refused request is never retried but
for a network error, `418`, `429` or a `5xx`, three times after 1, 3 and 5 s (`adv3.get`).

### 4.2 G-SAME and G-HISTORY

**G-SAME** (`adv3.py --compare`): for each coin, its perpetual's candles from `fapi.binance.com` and the archive's
daily kline file of each of the 14 days before the run's UTC day; every candle both hold compared as four numbers, and
each file of the archive absent counted. **PASS** where none differs and every coin has at least 12 compared — the
archive's file of the day before may be unpublished in the morning; **FAIL** at one difference; **UNDECIDABLE**
otherwise, which is BLOCKED here. Printed: per coin the candles compared and the files absent.

**G-HISTORY** (`adv3.py --history PATH`): the history re-derived from the archive — the 42 coins' monthly kline files
from 2019-09, the daily files of months without one, the monthly funding files through 2026-09, as the archive held them
at the freeze, and `+0.01%` per 8 h where none — written to `PATH` as JSON, then each of the 16 facts read against
`FACTS`: the trades, the profitable trades, the mean R, the median days held and the three shares, for the rule and for
STRONG, at `FACTS`' four decimals, and the two gates' verdicts. **PASS** at 16 of 16 with the file's bytes `19,362` long
and SHA-256 `bcee5309…` — the same bytes the Architect's three runs wrote, under Python 3.12.3 and 3.13.18 on 2026-10-28
and under 3.12.3 on 2026-10-29, on three separate fetches of the archive. A run after the archive publishes October's
monthly kline files reads October's candles from them in place of the daily files; candles to the close of 2026-10-27
alone enter, and no funding file after 2026-09 does, so the bytes stay the same unless the archive republished a
candle — itself a finding, and BLOCKED here. Printed beside it, gating nothing: each class's total R, Sharpe ratio, t,
p and worst drawdown.

### 4.3 COPY and G-UNIT

**COPY:** `/root/adv3-bot-svc` holds `adv3.py`, `adv3-bot.py` and `commit.txt` and nothing else; both files hash to
Appendix A's; `commit.txt` is 40 hex characters and a newline equal to the worktree's `HEAD` and to
`origin/tz-35-advisor-bot`.

**PROPS**, after B-INSTALL and before B-ENABLE: `LoadState` `loaded`, `ActiveState` `inactive`, `UnitFileState`
`disabled`, `FragmentPath` `/etc/systemd/system/adv3-bot.service`, `MemoryMax` `134217728`, `Nice` `10`,
`ProtectSystem` `strict`, `NoNewPrivileges` `yes`, `PrivateTmp` `yes`, `Restart` `always` and `ReadWritePaths`
`/var/lib/adv3-bot` — 11 checks, so that a setting systemd reads in another form than G-UNIT expects stops the run
before the unit starts, and not after. Printed beside them: `RestartPreventExitStatus` and `RestartUSec`.

**G-UNIT**, at `N` restarts: `ActiveState` `active`, `SubState` `running`, `UnitFileState` `enabled`, `FragmentPath`
`/etc/systemd/system/adv3-bot.service`, `ControlGroup` `/system.slice/adv3-bot.service`, `MemoryMax` `134217728`,
`Nice` `10`, `NRestarts` `N`, `ProtectSystem` `strict`, `NoNewPrivileges` `yes`, `Restart` `always`, `ReadWritePaths`
`/var/lib/adv3-bot`; `/proc/<MainPID>/cmdline` equal field for field to `/root/tz04a-env/venv/bin/python -B -u
/root/adv3-bot-svc/adv3-bot.py --serve`; its `cwd` `/root/adv3-bot-svc`; its `cgroup` naming
`/system.slice/adv3-bot.service` and no path under `/user.slice`; its `NoNewPrivs` `1`; the `MainPID` the only process
under that argv; and the installed unit file hashing to Appendix A's — 18 checks. Printed beside them:
`RestartPreventExitStatus` and `RestartUSec`.

### 4.4 G-DAILY and G-REPLY

From `service.log`'s lines stamped at or after the `start` mark less 1 s, and every record of `journal.jsonl`: the
service logged its start once under the unit's `MainPID`; its candles refreshed to the close of the day before the
run's UTC day with no coin missing; its daily logged as sent once, for that close; **exactly one** `daily` record, made
that day, of that close, of rule `ee206e7c…`, at `10,000` USDT and `0.5%`, with its Telegram message ids, 42 signals, at
most three cards and its STRONG coins among its TOP-3 — 8 checks. **NOT YET:** before 420 s after the mark — a first
attempt, its one retry 300 s later and the fetch — `daily` exits `3` while no daily line exists. **G-REPLY:** a line
after the mark reads `help sent` or `request answered…`, the unit's own reply to the Boss's `/start`, which
`--find-chat` left unconfirmed — the path the Boss's «сигнал» takes.
Printed beside them: the record's TOP-3, STRONG and each card's coin, side and mode, and every line that names a
failure.

### 4.5 G-RESTART and G-ONCE

**G-RESTART:** after the `kill` mark, a `MainPID` other than the marked one, its process started after the mark and at
most 60 s later, `NRestarts` `1`, the unit `active` and `running`, and a start line of the new pid reading the daily as
sent that day — 5 checks; then G-UNIT at `1` restart. **G-ONCE:** still exactly one `daily` record of the day, and no
daily line after the mark — 2 checks: a restart does not send the day's message again.

### 4.6 G-LOAD

`load` reads `/proc/<MainPID>/stat`: the first process's user and system time since its start, over the wall time
since, **at most `0.05`** of the host's one core, at least 300 s after its start. The Architect's runs took `1.2` to
`1.4` s of processor for the start-up fetch, report and message, and `0.7` to `1.3` s for each request after; a process
waiting on the long poll takes next to none. Printed beside it: the unit's `MemoryCurrent`, `MemoryPeak` and
`MemorySwapCurrent`, and the process's `VmRSS`, `VmHWM`, `VmSwap` and threads.

### 4.7 G-STILL

From §0.3 to §3.11, `btc-recorder.service` and `btc-rewardbook.service` each keep their `MainPID` and `NRestarts` and
read `active`; `btc-pairbook.service` reads `active`, and its `NRestarts` rises by exactly the number of `restart`
records the pair book's archive's ledger gains, its `MainPID` unchanged where that number is `0` — that archive's own
restarts, each of this TZ's reloads possibly setting one off (map §7 item 129), counted from its ledger and never from
the reloads. The reward book's archive restarts nothing (map §2.6), so its runs move none of the three. **It reads once
the pair book's archive's run set off by the last reload has started and ended** — that archive's
`ExecMainStartTimestampMonotonic` later than that reload's mark and the service inactive — or 1,200 s after that reload
with no run started, and at most 4,200 s after it, where a run still in progress reads **UNDECIDABLE**. **A FAIL names
its cause from the three units' journal**, which `still` prints on a FAIL (map §7 item 120).

### 4.8 The stops — CANON hard rule 14

**On a FAIL of G-UNIT, G-DAILY, G-REPLY, G-LOAD, G-RESTART, G-ONCE or G-STILL, after B-ENABLE, the bot's stop is
authorized and run at once**, by the classifier route of §3 where refused — after `I mark stop`, one block:

**K-35:**

```
{ date -u +%FT%T.%NZ; systemctl disable --now adv3-bot.service; echo "exit=$?"; } >> /root/tz35-work/logs/k35.log 2>&1
```

**Verification is the Executor's**, at least 30 s after the block: `I stopped` must print `READING STOPPED: PASS` — the
unit `inactive` or `failed` and `disabled`, no process under its argv. The disable reloads systemd; `I still` then
reads from the `stop` mark. The run goes to §3.11, §3.12 and §9, skipping every step that needs a PASS it lacks. **Under
PASS K-35 is not run**, and the bot runs on after the session. **UNDECIDABLE closes nothing and stops nothing.**

**B-UNINSTALL**, on a BLOCK after §3.5 and before B-ENABLE, so that nothing of the bot stays but the Boss's token and
the pinned chat:

```
{ date -u +%FT%T.%NZ; rm -f /etc/systemd/system/adv3-bot.service && systemctl daemon-reload; echo "exit=$?"; rmdir /var/lib/adv3-bot; echo "rmdir exit=$?"; rm -rf /root/adv3-bot-svc; echo "rm exit=$?"; for p in /etc/systemd/system/adv3-bot.service /var/lib/adv3-bot /root/adv3-bot-svc; do test -e "$p"; echo "$p exit=$?"; done; } >> /root/tz35-work/logs/b-uninstall.log 2>&1
```

The three `test -e` read `exit=1`; a `rmdir` of a root not yet created is recorded and harmless.

### 4.9 What a PASS establishes, and what it does not

The bot runs as a system unit outside every session, hardened — the filesystem read-only to it but for its own root —
under its memory ceiling and below the captures' priority; reads the Boss's 42 perpetuals from `fapi.binance.com`,
which serves the same closed candles as the archive the history was read on; quotes facts that the archive re-derives
to the last digit; sends the day's message once a day and not again after a restart; answers the Boss's chat and no
other; and leaves the three capture units as it found them. **Not established:** anything about the market to come —
the forward record's question, read after 2027-10-28; a request with a deposit and a risk, live — the self-tests parse
it, and G-REPLY reads the same path; a logout, a reboot and a day boundary — the unit's control group,
`WantedBy=multi-user.target` and the `daily-sent` file carry them.

---

## 5. The files

**`advisor/RULE-ADV-3.txt`** — the frozen rule text, its SHA-256 the `RULE` constant of `adv3.py`. **`advisor/adv3.py`**
— ADV-3's only implementation: the archive's and `fapi.binance.com`'s readers; the rule, `simulate`, the strength,
`ranking`, the STRONG strategy, `stats`; `history`, Gate H, Gate S and the display facts; `report`, `card` and `message`,
the Boss's message in Russian as Telegram HTML; `--history PATH` with G-HISTORY's reading against `FACTS`, and
`--compare`, G-SAME. **`advisor/adv3-bot.py`** — the Telegram side, importing `adv3.py` from beside itself: `serve`, the
unit's mode; `--probe`, P-START; `--find-chat`, `--hello` and `--selftest`. **Its exits:** `0` or a `SIGTERM`, which
systemd restarts unless it ordered the stop; `3` without a token or a chat id and `4` where glibc refuses its two
settings, neither restarted; `1`, an unexpected exception, restarted. Inside the loop an error is logged and retried —
a daily in 300 s, a poll in 15 s — and a coin whose candles fail is named in the message while the rest go out.
**`advisor/selftest-adv3.py`** — the Architect's checks of the rule's mechanics on synthetic candles, each expectation
computed by hand or by an independent formula. These four are `CryptoTZ/TZ-34-advisor-bot.md`'s Appendix A at `0968707`
byte for byte. **`deploy/systemd/adv3-bot.service`** — the reward book's unit with 10 of its 23 lines changed and 4
added: the two comments, the description, the working directory and the command line; `RestartSec=30` for `5`;
`RestartPreventExitStatus=3 4` for `1 2 3`; `MemoryMax=128M` for `192M`; the two log lines under `/var/lib/adv3-bot/`;
and `NoNewPrivileges=yes`, `PrivateTmp=yes`, `ProtectSystem=strict` and `ReadWritePaths=/var/lib/adv3-bot` added. The
rest is equal: `Type=simple`, `Restart=always`, `Nice=10`, `StartLimitIntervalSec=3600`, `StartLimitBurst=5`,
`WantedBy=multi-user.target`. It is the earlier specification's unit but for its first line, which names this TZ.
**`research/tz35-advisor-deploy.py`** — this TZ's checker: `fingerprint`, `host`, `number`, `selftest`, `scratch`,
`reclaim`, `mark`, `copy`, `props`, `unit`, `daily`, `load`, `restart`, `still` and `stopped`, each reading through pure
functions its self-test exercises; it starts, stops and signals nothing and sends no request. It is the earlier
specification's checker with its paths, branch, revision, row counts, unit hash and memory floor this TZ's, `number`
and the deferred set's print added, and two self-test checks for them. Standard library alone, every file, under
`/root/tz04a-env`; none imports anything from the repository but `adv3-bot.py`'s `adv3.py` beside it.

**What the Boss's message holds**, in this order: the close it is of and that it holds to the next close, 04:00 in
Batumi; the deposit and the risk; the day's changes — new signals, exits, reversals; TOP-3, each card its side, STRONG
where it is, the entry — at market inside the zone `C ± 0.25U`, a limit at the zone's edge where the price ran past it,
none near the stop — the stop and its distance, three targets with their move and the share of past trades of that
class that reached each, the size and the isolated leverage at most `⌊1 / (1.5·d/P + 0.01)⌋`, the signal's start and
the funding with its own interval; the other signals; the history's confidence, which confirms nothing; and the forward
record's state.

---

## 6. Cost

Measured in the Architect's runs under Python 3.12.3 and taken at the population's upper bound.

| check | population | measured | bound |
|---|---|---|---|
| the three self-tests | 32, 19 and 24 checks, no network | `0.08` to `0.20` s each on 2026-10-29 | `30` s each |
| G-SAME | 42 requests to `fapi.binance.com` and 588 archive files | `42.9` s, `2.6` s of processor, 588 compared at 8 workers against a stand-in for `fapi.binance.com`, 2026-10-28 | `900` s, the `timeout`; a request is tried at most 4 times, `129` s at worst |
| G-HISTORY | the 42 coins' archive from 2019-09: about 8,400 requests, most `404` for months before a listing | `198.4` to `222.2` s, `35.7` to `39.7` s of processor, at 16 workers, three runs | `1,800` s, the `timeout`; `120` s of processor |
| NUMBER, COPY, the marks, every checker mode | `git ls-tree`, systemd, `/proc` and small files | under 1 s each; `reclaim` `0.24` s over the 44 reports | `5` s a run, at most 70 runs |
| P-START, `--find-chat`, `--hello` | five requests; the pending updates; one message | `0.1` to `0.2` s each against stand-ins | `30` s each, and `--find-chat`'s wait of at most `1,800` s without processor |
| **the service** | 42 coins' 1,500 candles and funding, refetched once a close; a message | start-up `1.2` to `1.4` s of processor, a message `0.7` to `1.3` s; resident `47` to `60` MB | G-LOAD, `0.05` of the core |

**Single-session processor at most `680` s at those bounds** — the self-tests `90`, G-SAME `30` against its measured
`2.6`, G-HISTORY `120` against its measured `39.7`, P-START, `--find-chat` and `--hello` `90`, and at most 70 checker
runs, NOT YET's repeats included, at `5` s each, `350` — **under `3,600`, so nothing is sampled.** **Wall clock about 1 h
30 min:** §0 to §3.3 about 10 minutes; §3.4 4 to 10; §3.5 to §3.7 a minute, or up to 30 waiting for the Boss's
`/start`; §3.8's wait, none inside the band; §3.9 about 6 minutes; §3.10 about 2; §3.11 up to 70, a run of the pair
book's archive 600 s after B-ENABLE's reload, where one is set off, and its own length, which TZ-32 §6 and §10 C4 put at
`2,181` s at its longest; the rest about 10. **The host pays, after the session:** one process at about `60` MB
resident, about 3 s of processor a day and a few per request, and one long-poll connection to Telegram.

---

## 7. Validation

| # | check | count |
|---|---|---|
| **V1** | §0.2's fingerprint | `FINGERPRINT PASS`: revision `2026-10-29-a`; anchors 6 of 6, 4 re-derived; 49 rows, 46 of 46 `frozen` equal |
| **V2** | §0.3's host gate | `READING HOST: PASS - 12 of 12`: H1 to H6, the memory and the disk gate; the rest printed |
| **V3** | §0.5's NUMBER, at §0.5 and at §3.1 | `READING NUMBER: PASS - 2 of 2` each, the `TZ-35-` paths printed |
| **V4** | §0.1's and §3.1's files | 6 of 6 hashes asserted at each, lines and bytes; the branch's diff naming exactly the 6 `A` and 2 `D` paths |
| **V5** | the self-tests | `32 of 32`, `19 of 19`, `24 of 24` |
| **V6** | G-SAME | `READING G-SAME: PASS`, 42 coins, the candles compared per coin, the least, the files absent, 0 mismatches |
| **V7** | G-HISTORY and DETERMINISM | `16 of 16 equal`; the file `19,362` bytes, SHA-256 `bcee5309…` |
| **V8** | COPY | 4 of 4 |
| **V9** | P-START | `served - 5 of 5 endpoints`, each line printed |
| **V10** | G-CHAT, G-HELLO | one private chat pinned; one message id; the file `600 root` |
| **V11** | B-INSTALL and PROPS | `exit=0`; `verify` recorded; `11 of 11` |
| **V12** | G-UNIT at `0` and at `1` | 18 of 18 each |
| **V13** | G-DAILY, G-REPLY | 8 of 8, 1 of 1, the record's TOP-3, STRONG and cards printed |
| **V14** | G-LOAD | the fraction, against `0.05`; the memory reads |
| **V15** | G-RESTART, G-ONCE | 5 of 5, 2 of 2, both pids |
| **V16** | G-STILL | 3 of 3, each unit before and after, the ledger's restart records before and after, the deferred set's records at §0.3 and §3.11 |
| **V17** | contract §4.2's self-check | run after the push and the pull request and before the report's commit |
| **V18** | §3.12's closing reads | every read printed |
| **V19** | §9's `reclaim` runs | files considered, named by a report, kept by name, copied and already held; the store's count after equal to before plus the copies |
| **V20** | §9's removals | `git worktree remove` without `--force` exit `0`; `test -e` exit `1` for `/root/tz35-work` and each directory removed; `git worktree list` naming `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else |

---

## 8. The report

`CryptoReports/TZ-35-advisor-bot-report.md`, in contract §8's order. **In its first ten lines:** NUMBER at both reads;
G-SAME and G-HISTORY; COPY and P-START; G-CHAT and G-HELLO; B-ENABLE, G-UNIT, G-DAILY, G-REPLY and G-LOAD with their
counts; G-RESTART, G-ONCE and G-STILL; whether the bot runs, and how that was verified. Beyond what V1 to V20 print:
every mark's instant; every block the classifier refused, who ran it and when; the unit's journal lines; each memory and
free-space read with its instant and bound; the deferred set's ledger records at both reads; the commit and the pull
request; §9's counts and removals; and every file the run wrote, by SHA-256, but the bot's own root. **It never prints
the token, the chat id, or the content of any file under `/etc/adv3-bot/`.** The report is drafted in the primary
checkout `/root/btc-5m-twap` before B-RECLAIM-OWN and committed after it, so the removal of this TZ's tree is in it.

---

## 9. Reclaim — the host left clean (CANON hard rule 15)

**What a file is kept for:** a committed report prints its SHA-256, whole or as a prefix of 16 to 64 hex characters, or
it is kept by name: `state.json`, every file under `logs/`, and `history.json`. `reclaim` copies each into
`/root/btc-forensics/` as `<tree>--<path with / as -->`, by exclusive create, and verifies its hash; a name already
there with the same hash is counted as held, and with another hash is a failed assert. The branch worktree is not
copied: `reclaim` asserts that `git status --porcelain --ignored` in it prints nothing and that its `HEAD` is its
upstream's, so `git worktree remove` needs no `--force`. **No `reclaim`'s output is filtered**: every line it prints is
quoted (map §7 item 119).

**B-RECLAIM-SCRATCH**, after §3.3 and before §3.4, for every directory `I scratch` named **earlier** — none it named
live, and never this session's own:

```
I reclaim <each earlier directory, by its full path>
rm -rf <one such directory>; echo "exit=$?"
test -e <that directory>; echo "exit=$?"
```

One `I reclaim` names every earlier directory and must print `RECLAIM PASS` before any removal; then one `rm -rf` and
one `test -e` a directory, the last reading `exit=1`. `reclaim` refuses a directory born from 1 s before to 60 s after a
running claude process started, and any path but `/root/tz35-work` that is not a UUID directory under `/tmp/` whose
parent's name carries `btc-5m-twap`. If `I scratch` names none earlier, the block is recorded as empty and skipped. Map
§3 expects TZ-34's two, `540c6c83-4413-5ceb-86a4-2d45c7f8989a` and `57feec2d-2369-4cb0-9cad-8ac28cb7e578`, unless a
reboot of the host emptied `/tmp`.

**B-RECLAIM-OWN**, last, after §3.12 and with the report drafted. **Its output is written to no file; the report quotes
it verbatim from the session**, every line of it:

```
I reclaim /root/tz35-work
git -C /root/btc-5m-twap worktree remove /root/tz35-work/wt; echo "exit=$?"
rm -rf /root/tz35-work; echo "exit=$?"
test -e /root/tz35-work; echo "exit=$?"
git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
find /root/btc-forensics -type f | wc -l
df -B1 --output=source,size,avail /var/lib/btc-recorder
```

The branch `tz-35-advisor-bot` stays on `origin` and as a local ref; only its working tree goes. **Kept:**
`/root/adv3-bot-svc/` is the running unit's code, `/var/lib/adv3-bot/` its record, `/etc/adv3-bot/` the Boss's token
and the pinned chat; the capture roots, both archives' state and the forensic store are data, never scratch. **A refused
`rm -rf` is handed to the Boss** by §3's route, one tree per command, and verified by `test -e`.

---

## 10. Pre-send checks

Performed by the Architect on 2026-10-29 against this file as sent, in a reading separate from its writing, with the
repository at `origin/main` `ec5e2b35d1e0bf79b6756d61690e17b3e09e49e1` and map revision `2026-10-29-a` as `main`
carries it since `6ae312c`. Line numbers are those of the files §0.1 extracts.

| # | check | result |
|---|---|---|
| **C1** | scope against body | **Repository paths the body names, 26, and the 48 files of the map's table:** `CryptoTZ/TZ-35-advisor-bot.md`, read by §0.1's script and named by `number`; `CryptoTZ/` and `CryptoReports/`, listed by `number`; `CryptoTZ/TZ-34-advisor-bot.md`, named as the specification re-issued and read by no step; `SYSTEM-MAP.md` and its table's files, read by `I0 fingerprint`; `BTC-EXECUTOR-INSTRUCTIONS.md`, cited for contract §1, §4.2, §8 and §10; the six files of Appendix A, written on the branch — `adv3.py` and `adv3-bot.py` also copied to `/root/adv3-bot-svc/`, the unit to `/etc/systemd/system/`; `ADVISOR-SKILL.md` and `.github/workflows/adv2-signal.yml`, removed on the branch; `deploy/systemd/btc-recorder.service`, `btc-pairbook.service`, `btc-pairbook-archive.service`, `btc-pairbook-archive.timer`, `btc-rewardbook.service`, `btc-rewardbook-archive.service` and `btc-rewardbook-archive.timer`, read by §0.3's `cmp`, `btc-rewardbook.service` also cited by §5 as the new unit's template and never edited; every `CryptoReports/*.md`, read by `reclaim` for hashes; `CryptoReports/TZ-35-advisor-bot-report.md`, written to `main`; `research/tz33-reward-book-capture.py`, cited by §0.4, `research/tz28-pairbook-archive-timer.py`, cited by C7, and `CryptoTZ/TZ-32-our-quoting.md`, cited by §6, none read by a step but the first two as rows of `fingerprint`. **Entry points:** §0.1's script; the checker's fifteen modes — `fingerprint`, `host`, `number`, `selftest`, `scratch`, `reclaim`, `mark`, `copy`, `props`, `unit`, `daily`, `load`, `restart`, `still`, `stopped`; `adv3.py --compare` and `--history PATH`; `adv3-bot.py --selftest`, `--probe`, `--find-chat`, `--hello` and, under the unit, `--serve`; `selftest-adv3.py`; `git`, `gh`, `systemctl` (`show`, `cat`, `is-enabled`, `is-active`, `list-timers`, `daemon-reload`, `enable --now`, `kill`, `disable --now`), `systemd-analyze verify`, `journalctl`, `cmp`, `timeout`, `nice`, and the shell reads and writes of §0.0, §0.3, §3.1, §3.4, §3.5, §3.7, §3.8, §3.12, §4.8 and §9. **Outputs:** under `/root/tz35-work/` `logs/`, `state.json`, `stage/`, `wt/`, `history.json` and the bot self-test's transient `wt/advisor/.selftest-<pid>/`; `/root/adv3-bot-svc/` with `commit.txt`; the installed unit and its enable link; under `/var/lib/adv3-bot/`, by the unit, `service.log` and `journal.jsonl`, appended, and `offset` and `daily-sent`, each with a transient `.tmp`; `/etc/adv3-bot/chat-id` and its transient `.tmp`; the forensic store's copies; the branch, the pull request and the report. **Intersections with §2, by path and by content class, 11, each named in §2:** the two removals — paths item 1 and prohibited item 1's exemption; the report on `main` — paths item 2 and prohibited item 8; `I0 host`'s `find`, `grep -c` and `df` under the recorder's root — item 2; §0.3's and §3.12's `du` of the capture roots — item 2; `ledger.jsonl` read by `host` and `still`, its restart count and the deferred set's records — items 2 and 7; the token read by `host` and the bot — item 5; `/etc/adv3-bot/chat-id` written by `--find-chat` — host paths and item 5; `ls -la` and `stat` under `/etc/adv3-bot` — item 5; `systemctl show` and `list-timers` of the capture units and both archives, and `still`'s `journalctl` on a FAIL — item 3's reads; §0.3's and B-INSTALL's `cmp` of unit files — item 3's reads, **added to item 3 in this reading**, where they were missing; `tail` of `service.log` and the checker's prints of the journal — item 7. **Classes checked and intersecting nothing:** prices — G-SAME prints both candles of a mismatch, the journal and the Boss's messages carry entries, stops and targets, all of them Binance's public market data and none a capture's, which is item 2's class; `history.json` carries counts, R and shares and no price; the ledger's printed records carry event names, deferral counts and times; no settled document, book or outcome is fetched or read. |
| **C2** | origin of every expectation | **§7's literals, by kind.** Quoted from a committed artifact: V1's revision, `6`, `4`, `49` and `46`, map `2026-10-29-a` §0; V20's two worktrees, map §3; V7's sixteen facts, `FACTS`, Appendix A's `adv3.py` lines 28 to 31, fixed by the Architect's history run of 2026-10-28, and its `19,362` bytes and `bcee5309…`, the bytes the Architect's three runs of the frozen function wrote on three separate fetches of the archive under two interpreters — the third on 2026-10-29 for this TZ, `READING G-HISTORY: PASS - 16 of 16 equal` — a reproduction target fixed before any run of this TZ, so that no expectation is derived from the host's own run. Computed by an implementation independent of the one under test: V4's SHA-256, lines and bytes, by `sha256sum` and `wc` over the six files, exact, and §0.1's script run against this file, equal; the map's `1,879`, `444,652` and `e14b15d3…` the same way. Fixed by Appendix A's code, which this TZ measures nothing to set: V2's `12`, V3's `2`, V5's `32`, `19` and `24`, V8's `4`, V9's `5`, V11's `11`, V12's `18`, V13's `8` and `1`, V15's `5` and `2`, V16's `3` — each the count its function's dictionary holds, re-run by the Architect on the frozen files where it runs off the host; V10's mode `600`, `put` under `os.umask(0o077)`, `adv3-bot.py` lines 317 to 321. Fixed by §4 and measured by nothing: V6's `12` a coin and V14's `0.05`. **§5's literals:** "10 of its 23 lines changed and 4 added" is `diff` of Appendix A's unit against `deploy/systemd/btc-rewardbook.service` at `ec5e2b3`, exact — lines 1, 2, 4, 12, 13, 15, 16, 18, 23 and 24 changed, 19 to 22 added; "two self-test checks" is `diff` of the checker against `TZ-34-advisor-bot.md`'s, 22 checks to 24; the exits `0`, `3`, `4` and `1`, the retries of 300 and 15 s, the zone `C ± 0.25U` and the leverage bound are Appendix A's code and rule text. **§0.4's floors:** `170,344,448` = 2 × `85,172,224`; `7,400,000,000` = `7,300,000,000` (`research/tz33-reward-book-capture.py` line 190, `STREAM_FLOOR = 7300000000`) + `100,000,000`; `2.18` = `134,217,728` / `61,464,576`; `54,885` = `35,479` + `19,365` + `41`. **§3.8 to §3.10's bands:** `23,700` = 6 × 3,600 + 35 × 60, `81,000` = 22.5 × 3,600, `85,800` = 23 × 3,600 + 50 × 60. **No expectation depends on a quantity this TZ measures:** every gate compares what it reads with a threshold or a value fixed here or before. |
| **C3** | shape of every diff | Eight paths. The six added are new: `git cat-file -e ec5e2b3:<path>` exits `128` for each, so the change replaces **none** of their lines. The two removed replace all of theirs — `ADVISOR-SKILL.md`, 376 lines and `19,328` bytes, and `.github/workflows/adv2-signal.yml`, 45 lines and `1,665` bytes at `ec5e2b3`; §3.1 asserts the eight lines of `git diff --cached --name-status`. The report's path is new, exit `128`. The words "insertions only" appear in this TZ in this cell alone. |
| **C4** | cost of every check | §6, at the population's upper bound: the self-tests `30` s each; G-SAME's 630 requests under its `timeout 900`, `2.6` s of processor measured; G-HISTORY's about 8,400 requests under its `timeout 1800`, `35.7` to `39.7` s of processor measured over three runs, bounded at `120`; P-START, `--find-chat` and `--hello` `30` s each, `--find-chat`'s wait at most `1,800` s without processor; at most 70 checker runs at `5` s each — `fingerprint`, `host`, two `number`, `selftest`, `scratch`, two `reclaim`, `copy`, `props`, four `mark`, two `unit`, at most 14 `daily` within `DAILY_WAIT_S` = 420 s every 30 s, `load`, `restart`, at most 36 `still` within `STILL_DEADLINE_S` = 4,200 s every 120 s, `stopped` — 69. **Single-session processor at most `680` s; nothing is sampled.** The fail-fast bounds: the two `timeout`s; `adv3.get`'s four tries, `129` s at worst — four of its `30` s timeouts and the `1`, `3` and `5` s between — `adv3.py` lines 36 to 54; `--find-chat`'s `1,800` s, `adv3-bot.py` line 296; `daily`'s `420` s and `still`'s `4,200` s, the checker's lines 50 and 52. Wall clock about 1 h 30 min, derived in §6, about 2 h 20 min with every wait at its bound, and about 2 h 55 min with both `timeout`s reached as well. Disk at the same bound: §0.4's `100,000,000`. |
| **C5** | every count | V1's `49` = 46 + 2 + 1, read from map `2026-10-29-a` §0 by the checker's own `fingerprint` against the repository at `ec5e2b3`: 46 of 46 `frozen` rows equal, `FINGERPRINT PASS`. V2's `12`: H1, H2 two, H3, H4 three — the three capture units — H5 two, H6, the memory gate and the disk gate, `mode_host`, lines 344 to 393. V3's `2`, `number_reading`, lines 292 to 297. V4's `6` files and `8` diff lines = 6 `A` + 2 `D`. V5's `32`, `19` and `24`: the counts the three frozen self-tests print, re-run by the Architect on 2026-10-29. V6's `588` = 42 coins × 14 days, `12` a coin the least that passes. V7's `16` = 2 classes × 7 facts + 2 verdicts, `facts_checks`, `adv3.py` lines 625 to 640. V8's `4`, `mode_copy` lines 502 to 515; V11's `11`, `mode_props` lines 518 to 536; V12's `18`, `mode_unit` lines 539 to 573; V13's `8` and `1`, `daily_checks` lines 215 to 237; V15's `5` and `2`, `restart_checks` lines 240 to 257; V16's `3`, `still_checks` lines 260 to 271. V9's `5` endpoints, `probe`, `adv3-bot.py` lines 271 to 293. The 69 checker runs, as C4. |
| **C6** | every population | NUMBER: the paths under `CryptoTZ/` and `CryptoReports/` of `origin/main` at each of its two reads. G-SAME: the 42 coins' perpetuals, the 14 closed days before the run's UTC day, the archive's daily file and `fapi.binance.com`'s candle of each. G-HISTORY: the 42 coins' archive history to the close of 2026-10-27, the rule's trades and the STRONG strategy's. COPY: `/root/adv3-bot-svc`. P-START: one request to each of five endpoints. G-CHAT: the bot's pending updates for up to 1,800 s; G-HELLO: one message. PROPS: the installed unit before its first start. G-UNIT: the unit at `0` and at `1` restart. G-DAILY and G-REPLY: `service.log`'s lines from the `start` mark less 1 s, and every `journal.jsonl` record. G-LOAD: the first process from its start, at least 300 s. G-RESTART and G-ONCE: the unit, `service.log` and the journal after the `kill` mark. G-STILL: the three capture units from §0.3 to §3.11 and the pair book's archive's ledger's `restart` records between. The deferred set's print: that ledger's records of run `1793260762` at each read. Each memory figure: one mode's process; `MemAvailable` and free space: the host at each read. |
| **C7** | every signature and every behaviour | **Committed code this TZ relies on, read at `ec5e2b3`:** `research/tz28-pairbook-archive-timer.py`, `46a019d6…`, `def write(self, env, rec):`, lines 212 to 220, writes `(json.dumps(rec, sort_keys=True) + "\n")` with its default separators; its restart record, line 565, `led.write(env, {"event": "restart", "run": a, …})`; its start record, line 625, `{"event": "start", "run": a, "resumed": resumed, …}`; its deferral, line 666, `{"event": "deferred", "run": a, "phase": phase, "reason": reason[:400], "count": n}` — so a restart record's line holds `"event": "restart"`, the string `ledger_restarts` counts, checker lines 396 to 398, and every record is one JSON object a line carrying `event`, `run` and `wall_ns` (`LEDGER_KEYS`, line 124), the deferrals `count`, which `ledger_events` reads, lines 300 to 314. `research/tz33-reward-book-capture.py` line 190, `STREAM_FLOOR = 7300000000`. **Every behaviour this TZ attributes to Appendix A:** `adv3.get` — one GET with `User-Agent: adv3-advisor/1` (line 23), `404` as `None`, another `4xx` raised at once, a network error, `418`, `429` or `5xx` tried again after 1, 3 and 5 s, lines 36 to 54; `fapi_candles` closed candles only, `limit=1500`, lines 131 to 137; `fapi_funding` paged by 1,000, lines 140 to 152; `fapi_intervals`, lines 155 to 157; `fapi_marks`, lines 160 to 162; the rule — `signs`, `signal`, `strength`, `unit`, `hold`, `simulate`, `states`, `ranking`, `simulate_strong`, `stats` — lines 167 to 341; the funding months pinned through 2026-09, lines 21 and 361 to 362; `history`, lines 351 to 389; `report` with the coins not served and the funding intervals, lines 394 to 430; `card`'s entry modes, stop, targets, size and leverage, lines 433 to 452; `message` and `card_lines`, lines 490 to 604; `facts_checks`, lines 625 to 640; `compare`, lines 643 to 667; `--history PATH` written by exclusive create, its SHA-256 printed and G-HISTORY's reading, lines 681 to 697; G-SAME's reading, lines 698 to 708. `adv3-bot.py`: the token kept out of the log, lines 27 to 34; `put`, one rename, lines 42 to 49; `malloc_tune`, lines 52 to 59; `Telegram.call`, a JSON POST with `User-Agent: adv3-bot/1` (line 17) and `Content-Type: application/json`, lines 68 to 78; `send`, parts of at most 4,000 characters and plain text where HTML is refused, lines 80 to 93; `parse`, lines 110 to 120; `Data.fresh`, a coin not served named and the rest kept, lines 131 to 160; `make`, mark prices and intervals that fail tolerated, lines 163 to 177; `serve` — exit `3` at line 196, `4` at line 200, the daily due at 06:00 UTC (line 18), sent once and never again that day whatever its record does, lines 209 to 225, a failed daily retried in 300 s (lines 19 and 216), a failed poll in 15 s (line 237), the offset saved by rename (line 246); `handle`, lines 249 to 268; `probe`, P-START's five, lines 271 to 293; `find_chat`, the wait, the confirmation of updates that are not a `/start` and the file at mode `600`, lines 296 to 322; `hello`, lines 325 to 329. The unit: `ExecStart` line 13, `Restart` 14, `RestartSec` 15, `RestartPreventExitStatus` 16, `Nice` 17, `MemoryMax` 18, the four hardening lines 19 to 22, the logs 23 and 24. The checker: `show` lines 89 to 92, `procs` 129 to 130, `parse_map` 174 to 186, `number_reading` 292 to 297 and `mode_number` 409 to 416 — `git ls-tree --name-only origin/main -- CryptoTZ/ CryptoReports/`, exactly one `CryptoTZ/TZ-35-` path and it `TZ_FILE`, no `CryptoReports/TZ-35-` path — `deferred_run` 401 to 406, `still_wait` 633 to 640, `mode_still` 643 to 669, `mode_stopped` 672 to 677, `reclaim`'s rules 274 to 289 and 434 to 487. **Three sentences were rewritten in this reading:** §2 item 3 named no `cmp` among a unit's reads; §0.1 had `I0` run three modes only, where §3.1 runs `number` again and B-RECLAIM-OWN, on an early BLOCK, `reclaim`; and §4.2 had funding after 2026-09 never read, where `archive_funding` fetches such a month's file and `history` discards it, `adv3.py` lines 361 to 362. |
| **C8** | every cross-reference | Resolved by reading the text referenced. **Map `2026-10-29-a`:** §0's anchors and 49 rows, 46 / 2 / 1; §1's 84 ref lines read at 09:53 UTC and PR #34's merge ref that goes; §2.6's `STREAM_FLOOR` `7,300,000,000`, the reward book's archive at 01:30:20 UTC and 1,800 s after a start of its timer, restarting nothing, its store near one day's streams, about `1.0` GB, `du` beside `df`, `11,126,394,880` free at TZ-34's close; §3's two worktrees, TZ-34's two directories, the store's `2,151` files, both archives' code and state kept; §6's host identity, `/root/tz04a-env` on Python 3.12.3, `1,002,127,360` bytes and one processor, TZ-34's `MemAvailable` from `263,163,904` to `363,487,232`, the push through the URL's credential with `gh`'s as fallback, `enable --now` refused at TZ-20, TZ-26, TZ-28 and TZ-33, TZ-34's B-ENABLE the Boss's by its text, `systemctl kill` never refused; §7 items 115 and 125, a reload re-arming the pair book's archive's run 600 s later and the timeline that states it, 118, prints binding the Executor's reads, 119, no `reclaim` output filtered, 120, the package manager's restarts, 124, the hand-over rule, 127, the number used twice, its re-issue and its BLOCK, 128, the deferred set the next TZ reads from the ledger, 129, a run after a reload possible and not certain, counted from the ledger, and 131, the larger of the two peaks. **CANON `2026-10-29-b`**, delivered with this TZ: the owner section's credential the Architect cannot hold; PART VII, the advisor, deployed by TZ-35; hard rule 2's BLOCK on a number used twice, and hard rules 5, 13, 14 and 15. **Contract:** §1 steps 1 to 4, §4.2's self-check, §8's order, §10's venue rule. **Other artifacts:** TZ-32's archive run of `2,181` s, its §6 and §10 C4; `CryptoTZ/TZ-34-advisor-bot.md` at `0968707`, whose Appendix A's four advisor files §5 calls this TZ's byte for byte — extracted by its own §0.1 script and hashed equal, and `diff` of its unit and checker against this TZ's shows the changes §5 names. **This TZ:** §0.1 to §0.6, §1, §2's items, §3.1 to §3.12, §4.1 to §4.9, §5, §6 and §9, each supporting the sentence that cites it. **None unresolved.** |

**Five checks could not be performed from this session**, and each is a BLOCK condition of this TZ under CANON hard
rule 13: the host's reach of `fapi.binance.com` and `api.telegram.org` under this file's headers — `fapi.binance.com`
answers `451` to the Architect's session — P-START, §3.6, before anything is installed; G-SAME's comparison against the
live source, run on 2026-10-28 against a stand-in for `fapi.binance.com` and the real archive — §3.4; systemd's reading
of the unit's settings, which this session has no running systemd to give — PROPS, §3.8, before anything is started;
NUMBER on `main` with this file uploaded — `I0 number` printed `READING NUMBER: FAIL - 1 of 2` on `ec5e2b3`, which holds
no `TZ-35-` file yet, and `PASS - 2 of 2` and `FAIL` on a scratch clone holding a file of this name alone and with a
`TZ-35-` report beside it — §0.5; and the host's own state, its free space, memory, units, interpreter, ledger and the Boss's token —
§0.3. Everything else above was performed here under Python 3.12.3: the three self-tests, `32`, `19` and `24` of their
own; G-HISTORY against the archive itself, the file's bytes equal; §0.1's script against this file, 6 of 6; the
checker's `fingerprint` against `main`, 46 of 46, and its `mark`, `reclaim` and deferred-set print on stand-ins;
`systemd-analyze verify` of the unit under systemd 255, exit `0`; and a lint of the checker, clean. On 2026-10-28, on the
same bytes of `adv3.py` and `adv3-bot.py`: the bot end to end against stand-ins for both services, and the earlier
checker's readings on the bot's real log and journal — `log_lines`, `journal_records`, `daily_checks` and
`restart_checks`, which this checker carries unchanged.

---

## Appendix A — the six files, byte for byte

Extracted by §0.1's script; each block's content is its file.

```text file=advisor/RULE-ADV-3.txt
ADV-3 - frozen 2026-10-28, before any of its results was computed by anyone. ADV-1's rule on the Boss's
Binance Futures coins and their perpetuals' own candles, with a strength ranking whose claim has its own gate.
Instruments: BTC BCH SKY XLM XMR MORPHO LIT NEAR HBAR GRAM ENA UNI ARB ZEC HYPE SUI ADA RENDER TAO FET YFI XRP
  SOL ONDO LINK ALGO TRX BNB AAVE AVAX ETH INJ LTC XAU DASH PYTH WLD BTW QNT PUMP VVV EGLD, each its Binance
  USD-M USDT perpetual. Data: the perpetual's daily candles (UTC), from Binance's archive (data.binance.vision)
  for history and audits and from fapi.binance.com live; funding the perpetual's own, +0.01% per 8 h, longs
  paying, where none is published. A coin has no signal before its 112-day lookback exists.
Signal, stop, costs, funding and trade result: ADV-1's, word for word, on these candles.
Strength z at close t: sigma_t = sample standard deviation of the last 56 daily log returns;
  z = mean over L in {14, 28, 56, 112} of ln(C_t / C_(t-L)) / (sigma_t * sqrt(L)).
TOP-3: the three LONG or SHORT coins with the largest |z|, ties by the order above. STRONG: a TOP-3 coin whose
  four signs all agree with its side and whose |z| >= 1.
STRONG strategy: at each close, in rank order, every STRONG coin without an open STRONG trade opens one at C_t
  (U = 2*N_t, stop C_t -/+ U) while fewer than three STRONG trades are open; a STRONG trade closes exactly as
  ADV-1's position does - at its stop inside a day, or at the close where the signal changes.
Gate H, history to the close of 2026-10-27, all coins: the rule's total R <= 0 -> DISQUALIFIED (no direction
  is published); otherwise not disqualified, which confirms nothing.
Gate S, the same history: the STRONG strategy's total R <= 0, or its mean R a trade <= the rule's mean R a
  trade -> DISQUALIFIED (TOP-3 is shown without the STRONG label); otherwise not disqualified, which confirms
  nothing.
Display facts, measured once on the same history and gating nothing: the share of trades whose favourable
  excursion reaches +1R, +2R and +3R before their exit, and their median holding days - STRONG trades', or the
  rule's where Gate S disqualifies. The excursion runs from the day after entry to the exit day, the exit day's
  favourable extreme left out where the exit is a stop.
Display rules: entry zone C_t +/- 0.25*U. LONG: a mark price above the zone -> a limit at its top; inside it ->
  at market; below it and more than 0.25*U above the stop -> at market; nearer the stop -> no entry. SHORT
  mirrored. Stop: the rule's own level. Size = risk * deposit / |entry - stop|. Isolated leverage at most
  floor(1 / (1.5*|entry - stop|/entry + 0.01)), never above 20. Targets C_t +/- k*U, k = 1, 2, 3, each with its
  measured share. Valid until the next close, 00:00 UTC, 04:00 in Batumi.
Forward records, the rule's and the STRONG strategy's, from the close of 2026-10-28; each read once at 365
  days by an Executor TZ: one-sided t-test on the daily portfolio R, PROVEN at p <= 0.005, DISPROVEN at
  p <= 0.005 the other way, otherwise UNDECIDABLE. Running figures decide nothing.
Sizing: deposit 10,000 USDT and risk 0.5% a trade by default, 1% at most; all open signals together at most 5%.
```

```python file=advisor/adv3.py
#!/usr/bin/env python3
# adv3.py - ADV-3, the Boss's advisor for Binance Futures (CANON PART VII). Standard library only.
# Rule text RULE-ADV-3, SHA-256 ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169, frozen
# 2026-10-28 16:14 UTC before any of its results was computed: ADV-1's rule on the Boss's perpetuals' own
# candles, with a strength ranking (TOP-3, STRONG) whose claim has its own gate. Candles and funding come from
# Binance's archive (data.binance.vision) or live from fapi.binance.com; both give the same closed candles.
# Modes: the message of the latest close (--source fapi, the default, or archive; --json for the report);
# --history PATH, Gate H, Gate S and the display facts re-derived from the archive and read against FACTS (G-HISTORY);
# --compare, the archive's last 14 daily candles against fapi.binance.com's (G-SAME). The bot imports this file.
import argparse, bisect, datetime as dt, hashlib, html, io, json, math, statistics, sys, time, urllib.error, \
    urllib.parse, urllib.request, zipfile
from concurrent.futures import ThreadPoolExecutor

RULE = 'ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169'
COINS = ('BTC', 'BCH', 'SKY', 'XLM', 'XMR', 'MORPHO', 'LIT', 'NEAR', 'HBAR', 'GRAM', 'ENA', 'UNI', 'ARB', 'ZEC',
         'HYPE', 'SUI', 'ADA', 'RENDER', 'TAO', 'FET', 'YFI', 'XRP', 'SOL', 'ONDO', 'LINK', 'ALGO', 'TRX', 'BNB',
         'AAVE', 'AVAX', 'ETH', 'INJ', 'LTC', 'XAU', 'DASH', 'PYTH', 'WLD', 'BTW', 'QNT', 'PUMP', 'VVV', 'EGLD')
LOOKBACKS, ATR_DAYS, STOP_N, COST, BASE_F, VOL_DAYS = (14, 28, 56, 112), 20, 2.0, 0.001, 0.0001, 56
TOP_N, STRONG_Z, STRONG_MAX, ZONE, NEAR_STOP = 3, 1.0, 3, 0.25, 0.25
HISTORY_TO, FORWARD_FROM, ARCHIVE_FROM = dt.date(2026, 10, 27), dt.date(2026, 10, 28), dt.date(2019, 9, 1)
FUNDING_TO = (2026, 9)   # the archive's monthly funding files as published at the freeze, 2026-10-28
DEPOSIT, RISK, RISK_MAX, RISK_ALL = 10000.0, 0.5, 1.0, 5.0
UA = {'User-Agent': 'adv3-advisor/1'}
ARCH = 'https://data.binance.vision/data/futures/um/'
FAPI = 'https://fapi.binance.com'
DAY = dt.timedelta(days=1)
# Gate H, Gate S and the display facts, read once on the history to the close of 2026-10-27 (RULE-ADV-3)
FACTS = {'base': {'trades': 5265, 'wins': 1708, 'mean_R': 0.1576, 'median_days': 3, 'gate_H': 'NOT DISQUALIFIED',
                  'mfe': {1: 0.2325, 2: 0.1297, 3: 0.0819}},
         'strong': {'trades': 253, 'wins': 83, 'mean_R': 0.5473, 'median_days': 19, 'gate_S': 'NOT DISQUALIFIED',
                    'mfe': {1: 0.4783, 2: 0.2846, 3: 0.1779}}}


# ---- fetching ----------------------------------------------------------------------------------------------

def get(url, tries=4):
    """The body of url, or None where the server answers 404. A network error, 418, 429 or 5xx is tried again
    after 1, 3 and 5 s; any other answer raises at once."""
    err = None
    for k in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code not in (418, 429) and e.code < 500:
                raise RuntimeError(f'FETCH REFUSED {url}: HTTP {e.code}') from None
            err = e
        except OSError as e:
            err = e
        if k + 1 < tries:
            time.sleep(1 + 2 * k)
    raise RuntimeError(f'FETCH FAILED {url}: {err!r}')


def months(a, b):
    y, m = a.year, a.month
    while (y, m) <= (b.year, b.month):
        yield y, m
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)


def zip_rows(body):
    z = zipfile.ZipFile(io.BytesIO(body))
    rows = [line.split(',') for line in z.read(z.namelist()[0]).decode().splitlines()]
    return [p for p in rows if p[0].strip().isdigit()]


def ms_day(ms):
    ms = int(ms)
    ms = ms // 1000 if ms > 10 ** 14 else ms
    return dt.datetime.fromtimestamp(ms / 1000, dt.timezone.utc).date()


def holding_day(ms):
    """The day whose (open, close] holds a settlement at ms."""
    ms = int(ms)
    ms = ms // 1000 if ms > 10 ** 14 else ms
    return (dt.datetime.fromtimestamp(ms / 1000, dt.timezone.utc) - dt.timedelta(milliseconds=1)).date()


def archive_candles(sym, last_day, pool, first=ARCHIVE_FROM):
    """The perpetual's closed daily candles from first's month to last_day from the archive: monthly files, then
    daily files for the months whose monthly file is not out yet."""
    ms = list(months(first, last_day))
    url_m = lambda ym: f'{ARCH}monthly/klines/{sym}/1d/{sym}-1d-{ym[0]:04d}-{ym[1]:02d}.zip'
    got = dict(zip(ms, pool.map(lambda ym: get(url_m(ym)), ms)))
    out = {}
    for ym, body in got.items():
        if body is not None:
            for p in zip_rows(body):
                out[ms_day(p[0])] = (float(p[1]), float(p[2]), float(p[3]), float(p[4]))
    first_seen = min(out) if out else None
    missing = [ym for ym, body in got.items() if body is None and (first_seen is None or ym >= (first_seen.year, first_seen.month))]
    days = [d for ym in missing for d in (dt.date(ym[0], ym[1], k) for k in range(1, 32) if _valid(ym, k)) if d <= last_day]
    url_d = lambda d: f'{ARCH}daily/klines/{sym}/1d/{sym}-1d-{d.isoformat()}.zip'
    for d, body in zip(days, pool.map(lambda d: get(url_d(d)), days)):
        if body is not None:
            for p in zip_rows(body):
                out[ms_day(p[0])] = (float(p[1]), float(p[2]), float(p[3]), float(p[4]))
    return {d: v for d, v in out.items() if d <= last_day}


def _valid(ym, k):
    try:
        dt.date(ym[0], ym[1], k)
        return True
    except ValueError:
        return False


def archive_funding(sym, first, last, pool):
    """{holding day: sum of the perpetual's settlements} from the archive's monthly files, and the covered months."""
    ms = list(months(max(first, ARCHIVE_FROM), last))
    url = lambda ym: f'{ARCH}monthly/fundingRate/{sym}/{sym}-fundingRate-{ym[0]:04d}-{ym[1]:02d}.zip'
    per_day, covered = {}, set()
    for ym, body in zip(ms, pool.map(lambda ym: get(url(ym)), ms)):
        if body is not None:
            covered.add(ym)
            for p in zip_rows(body):
                d = holding_day(p[0])
                per_day[d] = per_day.get(d, 0.0) + float(p[2])
    return per_day, covered


def fapi(path, **params):
    return json.loads(get(f'{FAPI}{path}?{urllib.parse.urlencode(params)}' if params else f'{FAPI}{path}'))


def fapi_candles(sym, now_ms):
    """The perpetual's closed daily candles from fapi.binance.com, the last 1,500 days."""
    out = {}
    for r in fapi('/fapi/v1/klines', symbol=sym, interval='1d', limit=1500):
        if int(r[6]) < now_ms:
            out[ms_day(r[0])] = (float(r[1]), float(r[2]), float(r[3]), float(r[4]))
    return out


def fapi_funding(sym, first):
    """{holding day: sum of settlements} from fapi.binance.com since first, page after page of 1,000."""
    start = int(dt.datetime(first.year, first.month, first.day, tzinfo=dt.timezone.utc).timestamp() * 1000)
    per_day = {}
    for _ in range(100):
        rows = fapi('/fapi/v1/fundingRate', symbol=sym, startTime=start, limit=1000)
        for r in rows:
            d = holding_day(r['fundingTime'])
            per_day[d] = per_day.get(d, 0.0) + float(r['fundingRate'])
        if len(rows) < 1000:
            break
        start = int(rows[-1]['fundingTime']) + 1
    return per_day


def fapi_intervals():
    """{symbol: funding interval in hours} for the perpetuals whose interval Binance has adjusted; 8 h elsewhere."""
    return {r['symbol']: int(r['fundingIntervalHours']) for r in fapi('/fapi/v1/fundingInfo')}


def fapi_marks():
    """{symbol: (mark price, last funding rate)} for every perpetual, from fapi.binance.com."""
    return {r['symbol']: (float(r['markPrice']), float(r['lastFundingRate'])) for r in fapi('/fapi/v1/premiumIndex')}


# ---- the rule ----------------------------------------------------------------------------------------------

def signs(days, closes, i):
    """The four signs of the close against the closes 14, 28, 56 and 112 days before; None before they exist."""
    out = []
    for L in LOOKBACKS:
        j = bisect.bisect_right(days, days[i] - L * DAY) - 1
        if j < 0:
            return None
        out.append(((closes[i] > closes[j]) - (closes[i] < closes[j]), j, L))
    return out


def signal(days, closes, i):
    """+1 LONG, -1 SHORT, 0 FLAT at the close of days[i]; None before the longest lookback exists."""
    s = signs(days, closes, i)
    if s is None:
        return None
    t = sum(x for x, _, _ in s)
    return 1 if t >= 2 else -1 if t <= -2 else 0


def strength(days, closes, i):
    """(z, sum of the four signs) at the close of days[i]; None before both exist."""
    s = signs(days, closes, i)
    if s is None or i < VOL_DAYS:
        return None
    rets = [math.log(closes[k] / closes[k - 1]) for k in range(i - VOL_DAYS + 1, i + 1)]
    sd = statistics.stdev(rets)
    if sd <= 0:
        return None
    z = sum(math.log(closes[i] / closes[j]) / (sd * math.sqrt(L)) for _, j, L in s) / len(s)
    return z, sum(x for x, _, _ in s)


def true_range(c, days, i):
    h, l, pc = c[days[i]][1], c[days[i]][2], c[days[i - 1]][3]
    return max(h, pc) - min(l, pc)


def unit(c, days, i):
    """U = 2 N at the close of days[i]: twice the mean true range of the last 20 days; None before them."""
    if i < ATR_DAYS:
        return None
    return STOP_N * sum(true_range(c, days, j) for j in range(i - ATR_DAYS + 1, i + 1)) / ATR_DAYS


def open_at(side, close, U, day):
    return {'d': side, 'E': close, 'U': U, 'S': close - side * U, 'entry': day, 'R': -COST * close / U, 'mfe': 0.0}


def hold(pos, candle, pc, fund_d, day):
    """One day of an open position: its R for the day, and whether its stop closed it."""
    o, h, l, cl = candle
    k, U, S = pos['d'], pos['U'], pos['S']
    if (l <= S) if k > 0 else (h >= S):
        X = o if ((o <= S) if k > 0 else (o >= S)) else S
        r = (k * (X - pc) - COST * X) / U
        pos.update(R=pos['R'] + r, X=X, exit=day, why='stop')
        return r, True
    r = (k * (cl - pc) - k * fund_d * cl) / U
    pos['R'] += r
    pos['mfe'] = max(pos['mfe'], k * ((h if k > 0 else l) - pos['E']) / U)
    return r, False


def close_at(pos, close, day):
    x = -COST * close / pos['U']
    pos.update(R=pos['R'] + x, X=close, exit=day, why='signal')
    return x


def simulate(c, fund, first_entry, last_day):
    """The rule on one pair. Returns (closed trades, {day: R}, open position or None)."""
    days = sorted(d for d in c if d <= last_day)
    closes = [c[d][3] for d in days]
    trades, daily, pos = [], {}, None
    for i, d in enumerate(days):
        r = 0.0
        if i and pos:
            dr, stopped = hold(pos, c[d], closes[i - 1], fund(d), d)
            r += dr
            if stopped:
                trades.append(pos)
                pos = None
        sig = signal(days, closes, i)
        if pos and sig != pos['d']:
            r += close_at(pos, closes[i], d)
            trades.append(pos)
            pos = None
        U = unit(c, days, i) if pos is None and sig in (1, -1) and d >= first_entry else None
        if U:
            pos = open_at(sig, closes[i], U, d)
            r += pos['R']
        if d >= first_entry:
            daily[d] = r
    return trades, daily, pos


def states(c, last_day, since=None):
    """{day: (signal, z, sum of signs, U, close)} for every closed day of one pair to last_day; before since, the
    close alone, (None, None, None, None, close), which no ranking admits."""
    days = sorted(d for d in c if d <= last_day)
    closes = [c[d][3] for d in days]
    out = {}
    for i, d in enumerate(days):
        if since is not None and d < since:
            out[d] = (None, None, None, None, closes[i])
            continue
        st = strength(days, closes, i)
        out[d] = (signal(days, closes, i), st[0] if st else None, st[1] if st else None, unit(c, days, i), closes[i])
    return out


def ranking(day_states):
    """TOP-3 and STRONG for one close: day_states is [(coin, (signal, z, sum, U, close))] in universe order."""
    active = [(coin, s) for coin, s in day_states if s[0] in (1, -1) and s[1] is not None and s[3]]
    top = sorted(active, key=lambda cs: -abs(cs[1][1]))[:TOP_N]
    strong = [coin for coin, s in top if s[2] == 4 * s[0] and abs(s[1]) >= STRONG_Z]
    return [coin for coin, _ in top], strong


def simulate_strong(cs, st, funds, first_entry, last_day):
    """The STRONG strategy over all pairs: returns (closed trades, {day: R}, open trades)."""
    all_days = sorted({d for coin in cs for d in cs[coin] if d <= last_day})
    prev = {}
    trades, daily, open_ = [], {}, {}
    for d in all_days:
        r = 0.0
        for coin in list(open_):
            if d in cs[coin] and coin in prev:
                dr, stopped = hold(open_[coin], cs[coin][d], prev[coin], funds[coin](d), d)
                r += dr
                if stopped:
                    trades.append(open_.pop(coin))
        today = [(coin, st[coin][d]) for coin in COINS if coin in cs and d in st[coin]]
        for coin, s in today:
            if coin in open_ and s[0] != open_[coin]['d']:
                r += close_at(open_[coin], s[4], d)
                trades.append(open_.pop(coin))
        if d >= first_entry:
            _, strong = ranking(today)
            sd = dict(today)
            for coin in strong:
                if coin not in open_ and len(open_) < STRONG_MAX:
                    s = sd[coin]
                    open_[coin] = open_at(s[0], s[4], s[3], d)
                    open_[coin]['coin'] = coin
                    r += open_[coin]['R']
            daily[d] = r
        for coin, s in today:
            prev[coin] = s[4]
    return trades, daily, open_


def stats(trades, daily):
    R = [t['R'] for t in trades]
    out = {'trades': len(R), 'wins': sum(x > 0 for x in R), 'total_R': sum(R),
           'mean_R': sum(R) / len(R) if R else 0.0, 'days': len(daily)}
    held = [(t['exit'] - t['entry']).days for t in trades if 'exit' in t]
    if held:
        out['median_days'] = statistics.median(held)
    if R:
        out['mfe'] = {k: sum(t['mfe'] >= k for t in trades) / len(trades) for k in (1, 2, 3)}
    xs = [daily[d] for d in sorted(daily)]
    if len(xs) > 1:
        m = sum(xs) / len(xs)
        sd = math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))
        run = peak = dd = 0.0
        for x in xs:
            run += x
            peak = max(peak, run)
            dd = min(dd, run - peak)
        t = m / sd * math.sqrt(len(xs)) if sd > 0 else 0.0
        out.update(sharpe=m / sd * math.sqrt(365) if sd > 0 else 0.0, t=t,
                   p_up=0.5 * math.erfc(t / math.sqrt(2)), max_dd_R=dd)
    return out


def funding_of(per_day, covered_days):
    """The rule's funding by day: the published sum where the source covers the day, else the base rate."""
    return lambda d: per_day.get(d, 0.0) if covered_days(d) else 3 * BASE_F


# ---- the history and the gates -----------------------------------------------------------------------------

def history():
    """Gate H, Gate S and the display facts on the archive's history to the close of HISTORY_TO."""
    with ThreadPoolExecutor(16) as pool:
        cs = {coin: archive_candles(coin + 'USDT', HISTORY_TO, pool) for coin in COINS}
        funds = {}
        for coin in COINS:
            if not cs[coin]:
                continue
            first = min(cs[coin])
            per_day, covered = archive_funding(coin + 'USDT', first, HISTORY_TO, pool)
            covered = {ym for ym in covered if ym <= FUNDING_TO}
            per_day = {d: x for d, x in per_day.items() if (d.year, d.month) in covered}
            settled = [d for d in per_day]
            first_settle = min(settled) if settled else None
            funds[coin] = funding_of(per_day, lambda d, fs=first_settle, cv=covered:
                                     fs is not None and d >= fs and (d.year, d.month) in cv)
    cs = {k: v for k, v in cs.items() if v}
    base_trades, base_daily, per_coin = [], {}, {}
    for coin, c in cs.items():
        days = sorted(c)
        th, dh, ph = simulate(c, funds[coin], days[0], HISTORY_TO)
        if ph:
            th = th + [dict(ph, R=ph['R'] - COST * c[days[-1]][3] / ph['U'], why='open at the history cut')]
        for t in th:
            t['coin'] = coin
        base_trades += th
        for d, x in dh.items():
            base_daily[d] = base_daily.get(d, 0.0) + x
        per_coin[coin] = stats(th, dh) | {'from': str(days[0]), 'days_of_candles': len(days)}
    st = {coin: states(c, HISTORY_TO) for coin, c in cs.items()}
    s_trades, s_daily, s_open = simulate_strong(cs, st, funds, min(min(c) for c in cs.values()), HISTORY_TO)
    for coin, t in s_open.items():
        last = max(d for d in cs[coin] if d <= HISTORY_TO)
        s_trades.append(dict(t, R=t['R'] - COST * cs[coin][last][3] / t['U'], why='open at the history cut'))
    base, strong = stats(base_trades, base_daily), stats(s_trades, s_daily)
    base['gate_H'] = 'NOT DISQUALIFIED' if base['total_R'] > 0 else 'DISQUALIFIED'
    strong['gate_S'] = ('NOT DISQUALIFIED' if strong['total_R'] > 0 and strong['mean_R'] > base['mean_R']
                        else 'DISQUALIFIED')
    return {'rule': RULE, 'to_close_of': str(HISTORY_TO), 'base': base, 'strong': strong, 'per_coin': per_coin}


# ---- live: the signals of the latest close -----------------------------------------------------------------

def report(cs, funds, marks, deposit, risk, now_ms, missing=(), intervals=None):
    """Everything the Boss's message needs, from closed candles, funding and mark prices; missing names the coins
    whose candles the source did not serve, and intervals the funding periods (None where unread)."""
    risk = min(risk, RISK_MAX)
    last = max(max(c) for c in cs.values() if c)
    st = {coin: states(c, last, min(FORWARD_FROM, last) - DAY) for coin, c in cs.items() if c}
    today = [(coin, st[coin][last]) for coin in COINS if coin in st and last in st[coin]]
    top, strong = ranking(today)
    rows = {}
    for coin, s in today:
        c = cs[coin]
        days = sorted(c)
        _, _, pos = simulate(c, funds.get(coin, lambda d: 3 * BASE_F), days[0], last)
        prev = st[coin].get(days[-2]) if len(days) > 1 else None
        rows[coin] = {'signal': s[0], 'z': s[1], 'sum': s[2], 'U': s[3], 'close': s[4],
                      'prev': prev[0] if prev else None,
                      'since': str(pos['entry']) if pos else None, 'stop': pos['S'] if pos else None,
                      'mark': marks.get(coin + 'USDT', (None, None))[0],
                      'funding': marks.get(coin + 'USDT', (None, None))[1],
                      'funding_h': None if intervals is None else intervals.get(coin + 'USDT', 8)}
    for coin in COINS:
        if coin not in rows:
            rows[coin] = {'signal': None, 'missing': coin in missing}
    s_trades, s_daily, s_open = simulate_strong({k: v for k, v in cs.items() if v}, st, funds, FORWARD_FROM, last)
    b_trades, b_daily = [], {}
    for coin, c in cs.items():
        if not c:
            continue
        tf, df, _ = simulate(c, funds.get(coin, lambda d: 3 * BASE_F), FORWARD_FROM, last)
        b_trades += tf
        for d, x in df.items():
            b_daily[d] = b_daily.get(d, 0.0) + x
    cards = [card(coin, rows[coin], coin in strong, deposit, risk) for coin in top]
    return {'rule': RULE, 'close_of': str(last), 'deposit': deposit, 'risk_pct': risk, 'top': top, 'strong': strong,
            'cards': cards, 'rows': rows, 'strong_open': {k: str(v['entry']) for k, v in s_open.items()},
            'forward': {'base': stats(b_trades, b_daily), 'strong': stats(s_trades, s_daily)},
            'missing': [c for c in COINS if c in missing], 'marks_ok': bool(marks), 'made_at_ms': now_ms}


def card(coin, row, is_strong, deposit, risk):
    """One TOP-3 trade entered at this close: entry, stop, targets, size and leverage by RULE-ADV-3's display rules."""
    k, C, U = row['signal'], row['close'], row['U']
    S = C - k * U
    P = row['mark'] if row['mark'] else C
    lo, hi = C - ZONE * U, C + ZONE * U
    if k > 0:
        mode, entry = (('limit', hi) if P > hi else ('market', P) if P > S + NEAR_STOP * U else ('none', None))
    else:
        mode, entry = (('limit', lo) if P < lo else ('market', P) if P < S - NEAR_STOP * U else ('none', None))
    out = {'coin': coin, 'side': k, 'strong': is_strong, 'z': row['z'], 'close': C, 'U': U, 'stop': S, 'mark': P,
           'zone': (lo, hi), 'mode': mode, 'entry': entry, 'since': row['since'], 'funding': row['funding'],
           'funding_h': row.get('funding_h'),
           'targets': [C + k * n * U for n in (1, 2, 3)]}
    if entry is not None:
        dist = abs(entry - S)
        qty = risk / 100 * deposit / dist
        out.update(qty=qty, notional=qty * entry, stop_pct=100 * dist / entry,
                   leverage=min(20, math.floor(1 / (1.5 * dist / entry + 0.01))))
    return out


# ---- the message -------------------------------------------------------------------------------------------

def num(x, sig=3):
    """x to sig significant digits, Russian style: thin-free spaces between thousands, a decimal comma."""
    if x == 0:
        return '0'
    digits = max(0, sig - 1 - math.floor(math.log10(abs(x))))
    s = f'{x:,.{digits}f}'
    if digits:
        s = s.rstrip('0').rstrip('.')
    return s.replace(',', ' ').replace('.', ',').replace('-', '−')


def price(x):
    return num(x, 5)


def usdt(x):
    return f'{round(x):,}'.replace(',', ' ') if x >= 100 else num(x, 3)


def plural(n, one, few, many):
    if n % 10 == 1 and n % 100 != 11:
        return one
    return few if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14 else many


def pct(x, places=1):
    return f'{x:.{places}f}'.replace('.', ',').replace('-', '−')


def ddmm(day):
    return f'{day[8:10]}.{day[5:7]}'


def message(rep, facts):
    """The Boss's message in Russian, as Telegram HTML, from the report and the frozen history facts."""
    e = html.escape
    last = dt.date.fromisoformat(rep['close_of'])
    until = last + 2 * DAY
    lines = ['📊 <b>ADV-3 · сигналы Binance Futures</b>',
             f"Закрытие дня {ddmm(rep['close_of'])} (UTC)",
             f"⏱ Действует до 04:00 {until:%d.%m} по Батуми — до следующего закрытия",
             f"Депозит {num(rep['deposit'], 6)} USDT · риск {pct(rep['risk_pct'])}% = "
             f"{num(rep['deposit'] * rep['risk_pct'] / 100, 4)} USDT на сделку · все сделки вместе ≤ {pct(RISK_ALL, 0)}%"]
    if not rep.get('marks_ok', True):
        lines.append('⚠️ Текущие цены Binance недоступны: вход посчитан от цены закрытия')
    lines.append('')
    rows = rep['rows']
    word = {1: 'ЛОНГ', -1: 'ШОРТ'}
    new, out_long, out_short, flips = [], [], [], []
    for coin in COINS:
        now, before = rows[coin].get('signal'), rows[coin].get('prev')
        if now in word and before not in word:
            new.append(f'{coin} {word[now]}')
        elif now not in word and before in word:
            (out_long if before > 0 else out_short).append(coin)
        elif now in word and before in word and now != before:
            flips.append(f'{coin} в {word[now]}')
    lines.append('<b>Изменения за день</b>')
    if new:
        lines.append('🆕 Новые: ' + ', '.join(new))
    if out_long or out_short:
        parts = ([', '.join(out_long) + ' из лонга'] if out_long else []) + ([', '.join(out_short) + ' из шорта']
                                                                           if out_short else [])
        lines.append('🚪 Выход: ' + ' · '.join(parts))
    if flips:
        lines.append('🔄 Разворот: ' + ', '.join(flips))
    if not (new or out_long or out_short or flips):
        lines.append('Изменений нет.')
    lines.append('')
    if rep['cards']:
        lines.append('<b>ТОП-3 по силе тренда</b>')
        for cd in rep['cards']:
            lines += [''] + card_lines(cd, facts)
    else:
        lines.append('<b>Открытых сигналов нет</b> — все монеты вне рынка.')
    if rep['strong_open']:
        held = ', '.join(f'{k} с {ddmm(v)}' for k, v in rep['strong_open'].items())
        lines += ['', f'<b>Открытые STRONG-сделки правила:</b> {e(held)}']
    longs = [c for c in COINS if rows[c].get('signal') == 1 and c not in rep['top']]
    shorts = [c for c in COINS if rows[c].get('signal') == -1 and c not in rep['top']]
    flat = [c for c in COINS if rows[c].get('signal') == 0]
    young = [c for c in COINS if rows[c].get('signal') is None and not rows[c].get('missing')]
    lost = [c for c in COINS if rows[c].get('missing')]
    lines += ['', '<b>Остальные сигналы</b>']
    if longs:
        lines.append('🟢 ЛОНГ: ' + ', '.join(longs))
    if shorts:
        lines.append('🔴 ШОРТ: ' + ', '.join(shorts))
    lines.append(f'⚪ Вне рынка: {len(flat)} {plural(len(flat), "монета", "монеты", "монет")}')
    if young:
        lines.append('⏳ Мало истории для сигнала: ' + ', '.join(young))
    if lost:
        lines.append('⚠️ Binance не отдал данные: ' + ', '.join(lost))
    lines += ['', '<b>Уверенность</b> — история 2020–2026, не доказательство']
    if facts:
        s, b = facts['strong'], facts['base']
        if s.get('gate_S') == 'NOT DISQUALIFIED':
            lines.append(f"STRONG: {pct(100 * s['wins'] / s['trades'], 0)}% сделок в плюс, в среднем "
                         f"{'+' if s['mean_R'] > 0 else ''}{pct(s['mean_R'], 2)} R, держатся ~{s['median_days']:.0f} дн.")
        lines.append(f"Все сигналы: {pct(100 * b['wins'] / b['trades'], 0)}% в плюс, в среднем "
                     f"{'+' if b['mean_R'] > 0 else ''}{pct(b['mean_R'], 2)} R, держатся ~{b['median_days']:.0f} дн.")
        lines.append('Прибыль дают редкие длинные тренды; большинство сделок закрывается небольшим убытком.')
    fb, fs = rep['forward']['base'], rep['forward']['strong']
    if fb['days']:
        lines.append(f"Форвард с 28.10: {fb['days']} дн. · все сигналы {num(fb['total_R'], 3)} R · STRONG "
                     f"{num(fs['total_R'], 3)} R. Доказанность проверяется после 28.10.2027.")
    else:
        lines.append('Форвард начинается с закрытия 28.10; доказанность проверяется после 28.10.2027.')
    lines += ['', '<i>«Дошли» — доля прошлых сделок того же класса (★ STRONG или обычных), цена которых дошла до '
              'цели до выхода. R — результат в единицах риска сделки: −1 R — сработал стоп. Не инвестиционный '
              'совет: правило показывает состояние рынка; решение и риск — ваши.</i>']
    return '\n'.join(lines)


def card_lines(cd, facts):
    """One TOP-3 card: a line each for entry, stop, the three targets with their measured shares, and size."""
    side = 'LONG' if cd['side'] > 0 else 'SHORT'
    dot = '🟢' if cd['side'] > 0 else '🔴'
    out = [f"{dot} <b>{cd['coin']} · {side}</b>" + (' · ★ STRONG' if cd['strong'] else '')]
    lo, hi = cd['zone']
    if cd['mode'] == 'market':
        out += [f"Вход: <b>по рынку</b> ≈ {price(cd['entry'])}", f"   зона входа {price(lo)}–{price(hi)}"]
    elif cd['mode'] == 'limit':
        out += [f"Вход: <b>лимит {price(cd['entry'])}</b> — ждать отката", f"   цена {price(cd['mark'])} ушла от зоны, не догонять"]
    else:
        out += ['Вход: <b>не входить</b> — цена у стопа', f"   цена {price(cd['mark'])}"]
    ref = cd['entry'] if cd['entry'] is not None else cd['close']
    stop_pct = 100 * abs(ref - cd['stop']) / ref
    out.append(f"⛔ Стоп: <b>{price(cd['stop'])}</b> ({'−' if cd['side'] > 0 else '+'}{pct(stop_pct)}%)")
    shares, whose = None, ''
    if facts:
        use_strong = cd['strong'] and facts['strong'].get('gate_S') == 'NOT DISQUALIFIED'
        shares = (facts['strong'] if use_strong else facts['base']).get('mfe')
    for n, t in zip((1, 2, 3), cd['targets']):
        move = 100 * (t - ref) / ref
        share = f' · дошли {pct(100 * shares[n], 0)}%' if shares else ''
        out.append(f"🎯 {price(t)} ({'+' if move > 0 else ''}{pct(move)}%){share}")
    if cd['entry'] is not None:
        out.append(f"Объём: {num(cd['qty'])} {cd['coin']} ≈ {usdt(cd['notional'])} USDT · плечо ≤ {cd['leverage']}× изол.")
    extra = []
    if cd['since']:
        extra.append(f"Сигнал с {ddmm(cd['since'])}")
    if cd['funding'] is not None:
        period = f"/{cd['funding_h']} ч" if cd.get('funding_h') else ' за период'
        extra.append(f"фандинг {'+' if cd['funding'] >= 0 else ''}{pct(100 * cd['funding'], 3)}%{period}")
    if extra:
        out.append(' · '.join(extra))
    return out


# ---- command line ------------------------------------------------------------------------------------------

def live(source, deposit, risk):
    """The report of the latest close, from the archive or fapi.binance.com."""
    now_ms = int(time.time() * 1000)
    with ThreadPoolExecutor(16) as pool:
        if source == 'fapi':
            cs = dict(zip(COINS, pool.map(lambda k: fapi_candles(k + 'USDT', now_ms), COINS)))
            fs = dict(zip(COINS, pool.map(lambda k: fapi_funding(k + 'USDT', FORWARD_FROM - DAY), COINS)))
            funds = {k: funding_of(v, lambda d: d >= FORWARD_FROM) for k, v in fs.items()}
            marks, intervals = fapi_marks(), fapi_intervals()
        else:
            today = dt.datetime.now(dt.timezone.utc).date()
            cs = {k: archive_candles(k + 'USDT', today - DAY, pool) for k in COINS}
            funds, marks, intervals = {}, {}, None
    return report(cs, funds, marks, deposit, risk, now_ms, (), intervals)


def facts_checks(h):
    """G-HISTORY: each frozen fact against the history just derived - counts and verdicts exact, shares and mean R
    at FACTS' four decimals. {name: (equal, derived, FACTS)}."""
    out = {}
    for k in ('base', 'strong'):
        f, x = FACTS[k], h[k]
        out[f'{k} trades'] = (x['trades'] == f['trades'], x['trades'], f['trades'])
        out[f'{k} wins'] = (x['wins'] == f['wins'], x['wins'], f['wins'])
        out[f'{k} mean R'] = (round(x['mean_R'], 4) == f['mean_R'], x['mean_R'], f['mean_R'])
        out[f'{k} median days'] = (x['median_days'] == f['median_days'], x['median_days'], f['median_days'])
        for n in (1, 2, 3):
            out[f'{k} share +{n}R'] = (round(x['mfe'][n], 4) == f['mfe'][n], x['mfe'][n], f['mfe'][n])
    out['gate H'] = (h['base']['gate_H'] == FACTS['base']['gate_H'], h['base']['gate_H'], FACTS['base']['gate_H'])
    out['gate S'] = (h['strong']['gate_S'] == FACTS['strong']['gate_S'], h['strong']['gate_S'],
                     FACTS['strong']['gate_S'])
    return out


def compare(days_back=14):
    """G-SAME: for every coin, the archive's daily file and fapi.binance.com's candle of each of the last days_back
    closed days, compared field by field where both exist. Returns ([(coin, compared, archive files absent)],
    [mismatching (coin, day, archive, fapi)])."""
    now_ms = int(time.time() * 1000)
    today = dt.datetime.now(dt.timezone.utc).date()
    days = [today - k * DAY for k in range(days_back, 0, -1)]
    url = lambda sym, d: f'{ARCH}daily/klines/{sym}/1d/{sym}-1d-{d.isoformat()}.zip'
    rows, bad = [], []
    with ThreadPoolExecutor(8) as pool:
        for coin in COINS:
            sym = coin + 'USDT'
            live_c = fapi_candles(sym, now_ms)
            n = absent = 0
            for d, body in zip(days, pool.map(lambda d: get(url(sym, d)), days)):
                if body is None:
                    absent += 1
                    continue
                for p in zip_rows(body):
                    day, arch = ms_day(p[0]), (float(p[1]), float(p[2]), float(p[3]), float(p[4]))
                    n += 1
                    if day != d or live_c.get(day) != arch:
                        bad.append((coin, str(day), arch, live_c.get(day)))
            rows.append((coin, n, absent))
    return rows, bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--history', metavar='PATH', help='Gate H, Gate S and the display facts as JSON to PATH, '
                    'then G-HISTORY: each fact read against FACTS')
    ap.add_argument('--compare', action='store_true', help='G-SAME: the archive against fapi.binance.com')
    ap.add_argument('--source', choices=('fapi', 'archive'), default='fapi')
    ap.add_argument('--json', action='store_true', help='print the report instead of the message')
    ap.add_argument('--deposit', type=float, default=DEPOSIT)
    ap.add_argument('--risk', type=float, default=RISK)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    if a.history:
        h = history()
        text = json.dumps(h, indent=1, default=str) + '\n'
        with open(a.history, 'x', encoding='utf-8') as f:
            f.write(text)
        print('history written:', a.history, len(text.encode()), 'bytes, SHA-256',
              hashlib.sha256(text.encode()).hexdigest())
        checks = facts_checks(h)
        for k, (ok, got, want) in checks.items():
            print(f'G-HISTORY {k:<20} {got!s:<22} FACTS {want!s:<10} {"equal" if ok else "DIFFERENT"}')
        for k in ('base', 'strong'):
            x = h[k]
            print(f"printed, gating nothing: {k} total {x['total_R']:.4f} R, Sharpe {x['sharpe']:.4f}, t {x['t']:.4f}, "
                  f"p {x['p_up']:.6f}, worst drawdown {x['max_dd_R']:.4f} R")
        n = sum(ok for ok, _, _ in checks.values())
        print(f"READING G-HISTORY: {'PASS' if n == len(checks) else 'FAIL'} - {n} of {len(checks)} equal")
        sys.exit(0 if n == len(checks) else 1)
    if a.compare:
        rows, bad = compare()
        print('G-SAME per coin, candles compared / archive files absent:',
              ' '.join(f'{coin} {k}/{m}' for coin, k, m in rows))
        for b in bad:
            print('MISMATCH', *b)
        least = min(k for _, k, _ in rows)
        verdict = 'FAIL' if bad else 'PASS' if least >= 12 else 'UNDECIDABLE'
        print(f'READING G-SAME: {verdict} - {len(rows)} coins, {sum(k for _, k, _ in rows)} candles compared, '
              f'the least {least} for one coin, {len(bad)} mismatches')
        sys.exit(0 if verdict == 'PASS' else 1)
    rep = live(a.source, a.deposit, a.risk)
    if a.json:
        json.dump(rep, sys.stdout, indent=1, default=str)
        print()
    else:
        print(message(rep, FACTS))


if __name__ == '__main__':
    main()
```

```python file=advisor/adv3-bot.py
#!/usr/bin/env python3
# adv3-bot.py - ADV-3's Telegram side (CANON PART VII): the Boss's commands, the daily message at 06:00 UTC
# (10:00 in Batumi), and a journal of every message sent. Standard library only; adv3.py lies beside it.
# Modes: --serve (the unit's), --probe, --find-chat, --hello, --selftest.
# Exits: 0 or SIGTERM, restarted by systemd; 3 without a token or a chat id and 4 where glibc refuses its two
# settings, neither restarted; 1, an unexpected exception, restarted.
import argparse, ctypes, datetime as dt, html, json, os, re, sys, time, traceback, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import adv3  # noqa: E402

TOKEN_FILE = '/etc/adv3-bot/token'
CHAT_FILE = '/etc/adv3-bot/chat-id'
STATE = '/var/lib/adv3-bot'
TG = 'https://api.telegram.org/bot{token}/{method}'
UA = 'adv3-bot/1'
DAILY = dt.time(6, 0)
POLL, RETRY, LIMIT = 50, 300, 4000
CMD = re.compile(r'^\s*/?(сигнал|signal)(?:@\w+)?\b(.*)$', re.I | re.S)
HELP = ('<b>ADV-3 · сигналы Binance Futures</b>\n'
        '«сигнал» — сигналы сейчас: депозит 10 000 USDT, риск 0,5% на сделку.\n'
        '«сигнал 15000 0.5» — со своим депозитом и риском (риск не больше 1%).\n'
        'Каждый день в 10:00 по Батуми сигналы приходят сами.')


SECRETS = []   # the token, never written to the log


def log(*parts):
    line = ' '.join(str(p) for p in parts)
    for secret in SECRETS:
        line = line.replace(secret, '<token>')
    print(dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), line, flush=True)


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read().strip()


def put(path, text):
    """Replace path's content in one rename, so a kill mid-write leaves the old content or the new."""
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def malloc_tune():
    """glibc's mmap threshold at 128 KiB and its arenas at two, as the project's long-lived units fix them; True if
    glibc took both."""
    try:
        libc = ctypes.CDLL('libc.so.6')
        return libc.mallopt(-3, 131072) == 1 and libc.mallopt(-8, 2) == 1
    except OSError:
        return False


class Telegram:
    """The Bot API through one request function: every call is a JSON POST with UA as its User-Agent."""

    def __init__(self, token, chat=None):
        self.token, self.chat = token, chat

    def call(self, method, http_timeout=30, **params):
        req = urllib.request.Request(TG.format(token=self.token, method=method), data=json.dumps(params).encode(),
                                     headers={'User-Agent': UA, 'Content-Type': 'application/json'})
        try:
            with urllib.request.urlopen(req, timeout=http_timeout) as r:
                out = json.loads(r.read())
        except urllib.error.HTTPError as e:
            out = json.loads(e.read() or b'{}')
        if not out.get('ok'):
            raise RuntimeError(f"telegram {method}: {out.get('error_code')} {out.get('description')}")
        return out['result']

    def send(self, text):
        """The text as HTML, in parts of at most LIMIT characters; a part Telegram cannot parse goes as plain text."""
        ids = []
        for part in chunks(text):
            try:
                ids.append(self.call('sendMessage', chat_id=self.chat, text=part, parse_mode='HTML',
                                     disable_web_page_preview=True)['message_id'])
            except RuntimeError as e:
                if 'parse entities' not in str(e):
                    raise
                plain = html.unescape(re.sub(r'</?[bi]>', '', part))
                ids.append(self.call('sendMessage', chat_id=self.chat, text=plain,
                                     disable_web_page_preview=True)['message_id'])
        return ids


def chunks(text, limit=LIMIT):
    """Telegram takes at most 4,096 characters a message: split at line ends, never inside a line."""
    out, cur = [], ''
    for line in text.split('\n'):
        if cur and len(cur) + 1 + len(line) > limit:
            out.append(cur)
            cur = line
        else:
            cur = f'{cur}\n{line}' if cur else line
    if cur:
        out.append(cur)
    return out


def parse(text):
    """(deposit, risk) from «сигнал [deposit] [risk]», or None where the text is not that command."""
    m = CMD.match(text or '')
    if not m:
        return None
    rest_text = re.sub(r'(?<=\d)[ \u00a0\u202f](?=\d{3}(?!\d))', '', m.group(2))   # 15 000 -> 15000
    nums = [float(x.replace(',', '.')) for x in re.findall(r'\d+(?:[.,]\d+)?', rest_text)]
    deposit = next((x for x in nums if x >= 100), adv3.DEPOSIT)
    rest = [x for x in nums if x < 100]
    risk = rest[0] if rest else adv3.RISK
    return min(deposit, 10_000_000.0), min(max(risk, 0.05), adv3.RISK_MAX)


class Data:
    """The closed candles and funding of every coin, fetched from fapi.binance.com once per close. A coin whose
    candles fail is reported missing and the rest go on; where every coin fails, the fetch raises."""

    def __init__(self):
        self.cs = self.funds = self.close = self.at = None
        self.missing = []

    def fresh(self):
        """Refetched when a newer close exists, and once more where the last fetch fell in the first ten minutes
        after midnight UTC, before the day's last funding settlement was surely published."""
        now = dt.datetime.now(dt.timezone.utc)
        midnight = dt.datetime.combine(now.date(), dt.time(0, 0), tzinfo=dt.timezone.utc)
        early = self.at is not None and midnight <= self.at < midnight + dt.timedelta(minutes=10) <= now
        if self.close is None or self.close < (now - dt.timedelta(days=1)).date() or early:
            now_ms = int(now.timestamp() * 1000)

            def safe(fn, *args):
                try:
                    return fn(*args)
                except Exception as e:
                    log('fetch failed:', args[0], repr(e)[:300])
                    return None

            with ThreadPoolExecutor(6) as pool:
                got = list(pool.map(lambda k: safe(adv3.fapi_candles, k + 'USDT', now_ms), adv3.COINS))
                fs = list(pool.map(lambda k: safe(adv3.fapi_funding, k + 'USDT', adv3.FORWARD_FROM - adv3.DAY),
                                   adv3.COINS))
            cs = {k: v or {} for k, v in zip(adv3.COINS, got)}
            if not any(cs.values()):
                raise RuntimeError('fapi.binance.com served no candles')
            self.cs, self.missing = cs, [k for k, v in zip(adv3.COINS, got) if not v]
            self.funds = {k: adv3.funding_of(v, lambda d: d >= adv3.FORWARD_FROM) for k, v in zip(adv3.COINS, fs)
                          if v is not None}
            self.close = max(max(c) for c in cs.values() if c)
            self.at = now
            log('candles refreshed to the close of', self.close, '| missing', ','.join(self.missing) or '-')
        return self.cs, self.funds


def make(data, deposit, risk):
    """The report and the message at this moment; mark prices that fail leave the cards on the close."""
    cs, funds = data.fresh()
    try:
        marks = adv3.fapi_marks()
    except Exception as e:
        log('marks failed:', repr(e)[:300])
        marks = {}
    try:
        intervals = adv3.fapi_intervals()
    except Exception as e:
        log('funding intervals failed:', repr(e)[:300])
        intervals = None
    rep = adv3.report(cs, funds, marks, deposit, risk, int(time.time() * 1000), data.missing, intervals)
    return rep, adv3.message(rep, adv3.FACTS)


def journal(kind, rep, ids):
    rec = {'utc': dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds'), 'kind': kind, 'rule': rep['rule'],
           'close_of': rep['close_of'], 'deposit': rep['deposit'], 'risk_pct': rep['risk_pct'], 'top': rep['top'],
           'strong': rep['strong'], 'message_ids': ids,
           'signals': {k: v.get('signal') for k, v in rep['rows'].items()},
           'cards': [{k: cd[k] for k in ('coin', 'side', 'strong', 'mode', 'entry', 'stop', 'targets', 'close', 'U')}
                     for cd in rep['cards']]}
    with open(os.path.join(STATE, 'journal.jsonl'), 'a', encoding='utf-8') as f:
        f.write(json.dumps(rec, ensure_ascii=False, default=str) + '\n')


def serve():
    try:
        token, chat = read(TOKEN_FILE), int(read(CHAT_FILE))
    except (OSError, ValueError) as e:
        log('no token or chat id:', repr(e))
        sys.exit(3)
    SECRETS.append(token)
    if not malloc_tune():
        log('glibc refused its two settings')
        sys.exit(4)
    os.makedirs(STATE, exist_ok=True)
    tg, data = Telegram(token, chat), Data()
    off_path, day_path = os.path.join(STATE, 'offset'), os.path.join(STATE, 'daily-sent')
    offset = int(read(off_path)) if os.path.exists(off_path) else 0
    sent = read(day_path) if os.path.exists(day_path) else ''
    retry_at = 0.0
    log('serving the pinned chat: pid', os.getpid(), 'offset', offset, 'daily-sent', sent or '-')
    while True:
        now = dt.datetime.now(dt.timezone.utc)
        due = dt.datetime.combine(now.date(), DAILY, tzinfo=dt.timezone.utc)
        if now >= due and sent != now.date().isoformat() and time.time() >= retry_at:
            try:
                rep, msg = make(data, adv3.DEPOSIT, adv3.RISK)
                ids = tg.send(msg)
            except Exception:
                retry_at = time.time() + RETRY
                log('daily failed, retry in', RETRY, 's\n' + traceback.format_exc())
            else:
                sent = now.date().isoformat()      # sent: never again today, whatever its record does
                try:
                    put(day_path, sent)
                    journal('daily', rep, ids)
                except Exception:
                    log('daily record failed\n' + traceback.format_exc())
                log('daily sent for the close of', rep['close_of'])
        if sent == now.date().isoformat():
            wait = POLL
        elif now < due:
            wait = min(POLL, max(1, int((due - now).total_seconds())))
        else:
            wait = min(POLL, max(1, int(retry_at - time.time())))
        try:
            updates = tg.call('getUpdates', http_timeout=wait + 20, offset=offset, timeout=wait,
                              allowed_updates=['message'])
        except Exception:
            log('getUpdates failed\n' + traceback.format_exc())
            time.sleep(15)
            continue
        for u in updates:
            offset = u['update_id'] + 1
            msg = u.get('message') or {}
            if (msg.get('chat') or {}).get('id') != chat:
                continue
            handle(tg, data, msg.get('text') or '')
        if updates:
            put(off_path, str(offset))


def handle(tg, data, text):
    cmd = parse(text)
    try:
        if cmd:
            rep, msg = make(data, *cmd)
            ids = tg.send(msg)
            try:
                journal('request', rep, ids)
            except Exception:
                log('request record failed\n' + traceback.format_exc())
            log('request answered for the close of', rep['close_of'])
        else:
            tg.send(HELP)
            log('help sent')
    except Exception:
        log('request failed\n' + traceback.format_exc())
        try:
            tg.send('Binance или Telegram не ответили — повторите «сигнал» через минуту.')
        except Exception:
            log('apology failed\n' + traceback.format_exc())


def probe():
    """P-START: one live request per endpoint through the process's own request functions, each asserted served
    and parsed. Prints counts, dates and the bot's name; never the token or a chat id."""
    now_ms = int(time.time() * 1000)
    today = dt.datetime.now(dt.timezone.utc).date()
    c = adv3.fapi_candles('BTCUSDT', now_ms)
    assert c and max(c) >= today - 2 * adv3.DAY and all(len(v) == 4 and v[3] > 0 for v in c.values()), 'klines'
    print('P-KLINES served:', len(c), 'closed daily candles of BTCUSDT, the last', max(c))
    f = adv3.fapi_funding('BTCUSDT', adv3.FORWARD_FROM - adv3.DAY)
    assert f and all(isinstance(x, float) for x in f.values()), 'fundingRate'
    print('P-FUNDING served:', len(f), 'settlement days of BTCUSDT since', adv3.FORWARD_FROM - adv3.DAY)
    marks = adv3.fapi_marks()
    missing = [k for k in adv3.COINS if not (marks.get(k + 'USDT') or (0,))[0] > 0]
    assert not missing, f'premiumIndex lacks {missing}'
    print('P-MARKS served:', len(marks), 'perpetuals, all', len(adv3.COINS), 'coins among them with a mark price')
    iv = adv3.fapi_intervals()
    assert all(isinstance(h, int) and h > 0 for h in iv.values()), 'fundingInfo'
    print('P-INTERVALS served:', len(iv), 'perpetuals with an adjusted funding interval,',
          sum(k + 'USDT' in iv for k in adv3.COINS), 'of the coins among them')
    me = Telegram(read(TOKEN_FILE)).call('getMe')
    assert me.get('is_bot') is True and me.get('username'), 'getMe'
    print('P-TELEGRAM served: bot @' + me['username'])
    print('READING P-START: served - 5 of 5 endpoints')


def find_chat(wait_s=1800):
    """The one private chat that sent /start to the bot, pinned to CHAT_FILE. Waits up to wait_s for a /start;
    exit 1 where two chats sent one, or none did in time. Prints counts only, never a chat id."""
    tg = Telegram(read(TOKEN_FILE))
    deadline, said, offset = time.time() + wait_s, False, {}
    while True:
        ups = tg.call('getUpdates', http_timeout=80, timeout=50, allowed_updates=['message'], **offset)
        chats = {(u['message']['chat']['id'], u['message']['chat'].get('type'))
                 for u in ups if 'message' in u and (u['message'].get('text') or '').startswith('/start')}
        private = sorted(cid for cid, t in chats if t == 'private')
        if len(private) == 1:
            break                       # the /start stays unconfirmed: the service's first poll answers it
        if len(private) > 1 or time.time() >= deadline:
            print('updates', len(ups), '| private chats that sent /start:', len(private))
            sys.exit(1)
        if ups:                         # none a /start: confirmed, so the next poll waits for a new update
            offset = {'offset': ups[-1]['update_id'] + 1}
        if not said:
            print('no /start among', len(ups), 'pending updates; waiting up to', wait_s, 's for the Boss\'s /start',
                  flush=True)
            said = True
    old = os.umask(0o077)
    try:
        put(CHAT_FILE, f'{private[0]}\n')
    finally:
        os.umask(old)
    print('updates', len(ups), '| private chats that sent /start: 1 | chat pinned to', CHAT_FILE)


def hello():
    ids = Telegram(read(TOKEN_FILE), int(read(CHAT_FILE))).send(
        'ADV-3 подключён к этому чату. Напишите «сигнал» — или ждите сигналов в 10:00 по Батуми.')
    assert ids and all(isinstance(x, int) for x in ids), ids
    print('G-HELLO sent: message ids', ids)


def selftest():
    """The bot's own checks, offline: the command, the chunks, the files, the log, the HTML fallback, glibc."""
    done = []

    def check(name, ok):
        done.append(name)
        assert ok, name

    for text, want in (('сигнал', (adv3.DEPOSIT, adv3.RISK)), ('Сигнал 15000 0,5%', (15000.0, 0.5)),
                       ('/signal@adv3_bot 5000 0.8', (5000.0, 0.8)), ('signal 0.3', (adv3.DEPOSIT, 0.3)),
                       ('сигнал 20000 3', (20000.0, adv3.RISK_MAX)), ('сигнал 20 000 0,5', (20000.0, 0.5)),
                       ('signal 5000 0.5%', (5000.0, 0.5)), ('сигнал 12000 0.01', (12000.0, 0.05)),
                       ('привет', None), ('сигналы', None), ('', None)):
        check(f'parse {text!r}', parse(text) == want)
    long_text = '\n'.join(f'line {i} ' + 'x' * 90 for i in range(200))
    parts = chunks(long_text)
    check('chunks: 5 parts under the limit, joined back whole',
          len(parts) == 5 and all(len(p) <= LIMIT for p in parts) and '\n'.join(parts) == long_text)
    tmp = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'.selftest-{os.getpid()}')
    os.mkdir(tmp)
    try:
        f = os.path.join(tmp, 'offset')
        put(f, '41')
        put(f, '42')
        check('put replaces in one rename', read(f) == '42' and sorted(os.listdir(tmp)) == ['offset'])
    finally:
        for name in os.listdir(tmp):
            os.remove(os.path.join(tmp, name))
        os.rmdir(tmp)

    class Fake(Telegram):
        def __init__(self):
            super().__init__('123456:SECRET', 777)
            self.calls = []

        def call(self, method, http_timeout=30, **params):
            self.calls.append(params)
            if params.get('parse_mode') == 'HTML' and '<b>bad' in params['text']:
                raise RuntimeError("telegram sendMessage: 400 Bad Request: can't parse entities")
            return {'message_id': len(self.calls)}

    fk = Fake()
    check('HTML sent as HTML', fk.send('<b>ok</b>') == [1] and fk.calls[0]['parse_mode'] == 'HTML')
    check('unparseable HTML resent as plain text', fk.send('<b>bad &amp; x</b>') == [3]
          and 'parse_mode' not in fk.calls[2] and fk.calls[2]['text'] == 'bad & x')
    SECRETS.append('123456:SECRET')
    import contextlib, io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        log('url https://api.telegram.org/bot123456:SECRET/getMe failed')
    SECRETS.remove('123456:SECRET')
    check('the token never reaches the log', 'SECRET' not in buf.getvalue() and '<token>' in buf.getvalue())
    d0 = dt.date(2026, 6, 1)
    cs, funds = {}, {}
    for n, coin in enumerate(adv3.COINS[:6]):
        c, x = {}, 100.0 + n
        for i in range(160):
            x *= (1.012 if n % 2 == 0 else 0.988) * (1 + 0.004 * ((i * 7 + n) % 5 - 2))
            c[d0 + dt.timedelta(days=i)] = (x, x * 1.02, x * 0.98, x)
        cs[coin] = c
        funds[coin] = lambda d: 0.0
    rep = adv3.report(cs, funds, {}, 15000.0, 0.5, 0)
    msg = adv3.message(rep, adv3.FACTS)
    check('a synthetic report: 3 cards at 75 USDT of risk each', len(rep['cards']) == 3 and all(
        cd['mode'] == 'market' and abs(cd['qty'] * abs(cd['entry'] - cd['stop']) - 75) < 1e-9 for cd in rep['cards']))
    check('its message fits one Telegram message', len(chunks(msg)) == 1 and 'Депозит 15 000 USDT' in msg)
    check('glibc takes its two settings', malloc_tune())
    print(f'SELFTEST PASS: {len(done)} of {len(done)} checks passed')


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group()
    for m in ('serve', 'probe', 'find-chat', 'hello', 'selftest'):
        g.add_argument('--' + m, action='store_true')
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    if a.probe:
        probe()
    elif a.find_chat:
        find_chat()
    elif a.hello:
        hello()
    elif a.selftest:
        selftest()
    else:
        serve()


if __name__ == '__main__':
    main()
```

```python file=advisor/selftest-adv3.py
#!/usr/bin/env python3
# selftest-adv3.py - the Architect's checks of adv3.py's mechanics on synthetic candles; no network.
# Every expectation is computed here by hand or by an independent formula, never by adv3.py itself.
import datetime as dt, importlib.util, math, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('adv3', os.path.join(HERE, 'adv3.py'))
a = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)
CHECKS = []


def check(name, ok):
    CHECKS.append(name)
    assert ok, name


D0 = dt.date(2020, 1, 1)
DAY = dt.timedelta(days=1)

# 1. a rising line, stopped by a gap down at day 150, then flat: the trade, its R, the day's R and the excursion
c = {}
for i in range(200):
    cl = 100.0 + i
    c[D0 + i * DAY] = (cl - 1, cl + 1, cl - 2, cl)
c[D0 + 150 * DAY] = (150.0, 151.0, 140.0, 145.0)
for i in range(151, 200):
    c[D0 + i * DAY] = (145.0, 145.0, 145.0, 145.0)
trades, daily, pos = a.simulate(c, lambda d: 0.0003, D0, D0 + 199 * DAY)
t0 = trades[0]
check('entry at the first close with a 112-day lookback', t0['entry'] == D0 + 112 * DAY and t0['E'] == 212.0)
check('U = 2 x the mean true range of 20 days', abs(t0['U'] - 6.0) < 1e-12)
check('a gap through the stop exits at the open', t0['why'] == 'stop' and t0['X'] == 150.0
      and t0['exit'] == D0 + 150 * DAY)
# R: price move 150 - 212, costs 0.1% a side at 212 and 150, funding 0.03% a day on the closes held, in units of U
fund = 0.0003 * sum(212.0 + k for k in range(1, 38))
check('the trade R with costs and funding', abs(t0['R'] - (-62 - 0.001 * 362 - fund) / 6) < 1e-9)
check('the first held day R', abs(daily[D0 + 113 * DAY] - (1 - 0.0003 * 213) / 6) < 1e-12)
check('the excursion leaves out the stop day', abs(t0['mfe'] - (250 - 212) / 6) < 1e-12)
check('re-entry short on the stop day', pos['d'] == -1 and pos['entry'] == D0 + 150 * DAY and abs(pos['U'] - 16.6) < 1e-9)

# 2. the strength against an independent formula on a noisy rising series
random.seed(7)
c2, x = {}, 100.0
for i in range(300):
    x *= math.exp(0.004 + random.gauss(0, 0.02))
    c2[D0 + i * DAY] = (x, x * 1.01, x * 0.99, x)
days = sorted(c2)
closes = [c2[d][3] for d in days]
z, ssum = a.strength(days, closes, 299)
rets = [math.log(closes[k] / closes[k - 1]) for k in range(244, 300)]
m = sum(rets) / 56
sd = math.sqrt(sum((r - m) ** 2 for r in rets) / 55)
zz = sum(math.log(closes[299] / closes[299 - L]) / (sd * math.sqrt(L)) for L in (14, 28, 56, 112)) / 4
check('z equals the independent formula', abs(z - zz) < 1e-12)
check('the sum of signs is the four signs', ssum == sum((closes[299] > closes[299 - L]) - (closes[299] < closes[299 - L])
                                                      for L in (14, 28, 56, 112)))
check('no strength before 56 returns', a.strength(days, closes, 120) is not None and a.strength(days, closes, 55) is None)

# 3. the ranking: the three largest |z| among LONG and SHORT; STRONG needs four agreeing signs and |z| >= 1
st = [('A', (1, 2.0, 4, 1.0, 10.0)), ('B', (-1, -0.5, -4, 1.0, 10.0)), ('C', (1, 1.5, 2, 1.0, 10.0)),
      ('D', (0, 3.0, 0, 1.0, 10.0)), ('E', (-1, -1.2, -4, 1.0, 10.0))]
top, strong = a.ranking(st)
check('TOP-3 by |z|, FLAT left out', top == ['A', 'C', 'E'])
check('STRONG: four signs and |z| >= 1', strong == ['A', 'E'])

# 4. the card: zone C +/- 0.25U, the entry modes, the stop C -/+ U, size = 0.5% x 10,000 / |entry - stop|
row = {'signal': 1, 'close': 100.0, 'U': 8.0, 'stop': None, 'mark': 101.0, 'z': 2.0, 'since': '2026-10-20',
       'funding': 0.0001}
cd = a.card('A', row, True, 10000, 0.5)
check('LONG inside the zone: at market', cd['mode'] == 'market' and cd['stop'] == 92.0 and abs(cd['qty'] - 50 / 9.0) < 1e-12)
check('leverage floor(1 / (1.5 x 9/101 + 0.01)) = 6', cd['leverage'] == 6)
cd = a.card('A', dict(row, mark=103.0), True, 10000, 0.5)
check('LONG above the zone: a limit at its top', cd['mode'] == 'limit' and cd['entry'] == 102.0
      and abs(cd['qty'] - 50 / 10.0) < 1e-12)
cd = a.card('A', dict(row, mark=93.5), True, 10000, 0.5)
check('LONG within 0.25U of the stop: no entry', cd['mode'] == 'none' and cd['entry'] is None)
cd = a.card('A', dict(row, mark=97.0), True, 10000, 0.5)
check('LONG below the zone, clear of the stop: at market', cd['mode'] == 'market' and cd['entry'] == 97.0)
cd = a.card('A', dict(row, signal=-1, mark=99.0), False, 10000, 0.5)
check('SHORT mirrored: stop and targets', cd['mode'] == 'market' and cd['stop'] == 108.0
      and cd['targets'] == [92.0, 84.0, 76.0])
cd = a.card('A', dict(row, signal=-1, mark=97.0), False, 10000, 0.5)
check('SHORT below the zone: a limit at its bottom', cd['mode'] == 'limit' and cd['entry'] == 98.0)

# 5. the message's numbers, Russian style
check('num: spaces between thousands, a decimal comma', a.num(15000, 6) == '15 000' and a.num(0.5) == '0,5')
check('usdt: whole above 100', a.usdt(663.7) == '664' and a.usdt(86.43) == '86,4')
check('plural of монета', [a.plural(n, '1', '2', '5') for n in (1, 2, 5, 11, 12, 21, 22, 25, 111)]
      == ['1', '2', '5', '5', '5', '1', '2', '5', '5'])

# 6. a report and its message on six synthetic coins: three cards, every section present
cs, funds = {}, {}
for n, coin in enumerate(a.COINS[:6]):
    cc, x = {}, 100.0 + n
    for i in range(160):
        x *= (1.012 if n % 2 == 0 else 0.988) * (1 + 0.004 * ((i * 7 + n) % 5 - 2))
        cc[dt.date(2026, 6, 1) + i * DAY] = (x, x * 1.02, x * 0.98, x)
    cs[coin] = cc
    funds[coin] = lambda d: 0.0
rep = a.report(cs, funds, {}, 10000.0, 0.5, 0)
msg = a.message(rep, a.FACTS)
check('three cards, each with size 50 USDT of risk', len(rep['cards']) == 3
      and all(abs(cd['qty'] * abs(cd['entry'] - cd['stop']) - 50) < 1e-9 for cd in rep['cards']))
check('the message holds its sections', all(k in msg for k in ('ТОП-3', '⛔ Стоп', '🎯', 'Действует до 04:00',
                                                               'Уверенность', 'Остальные сигналы')))
strong_card = dict(rep['cards'][0], strong=True)
plain_card = dict(rep['cards'][0], strong=False)
check('a STRONG card shows the STRONG shares 48 / 28 / 18%',
      [l.rsplit('дошли ', 1)[1] for l in a.card_lines(strong_card, a.FACTS) if 'дошли' in l] == ['48%', '28%', '18%'])
check('another card shows the rule\'s shares 23 / 13 / 8%',
      [l.rsplit('дошли ', 1)[1] for l in a.card_lines(plain_card, a.FACTS) if 'дошли' in l] == ['23%', '13%', '8%'])

# 7. G-HISTORY's comparison: equal facts read equal, one changed fact reads DIFFERENT
h = {k: {'trades': f['trades'], 'wins': f['wins'], 'mean_R': f['mean_R'] + 1e-6, 'median_days': f['median_days'],
         'mfe': dict(f['mfe']), 'gate_H': f.get('gate_H'), 'gate_S': f.get('gate_S')} for k, f in a.FACTS.items()}
check('G-HISTORY: 16 facts, all equal', len(a.facts_checks(h)) == 16 and all(ok for ok, _, _ in a.facts_checks(h).values()))
h['strong']['wins'] += 1
check('G-HISTORY: a changed fact reads DIFFERENT', [k for k, (ok, _, _) in a.facts_checks(h).items() if not ok]
      == ['strong wins'])

# 8. the live readers on stand-in replies: funding paged by 1,000, intervals 8 h unless adjusted, marks and the card
calls = []
t_first = int(dt.datetime(2026, 10, 27, tzinfo=dt.timezone.utc).timestamp() * 1000)


def fake_fapi(path, **params):
    calls.append((path, params))
    if path == '/fapi/v1/fundingRate':
        s0 = params['startTime']
        n = 1000 if s0 == t_first else 5
        return [{'fundingTime': s0 + 3_600_000 * (k + 1), 'fundingRate': '0.0001'} for k in range(n)]
    if path == '/fapi/v1/fundingInfo':
        return [{'symbol': 'BTWUSDT', 'fundingIntervalHours': 4}]
    return [{'symbol': 'XMRUSDT', 'markPrice': '610.5', 'lastFundingRate': '0.00010000'}]


real_fapi, a.fapi = a.fapi, fake_fapi
try:
    per_day = a.fapi_funding('BTWUSDT', dt.date(2026, 10, 27))
    intervals, marks = a.fapi_intervals(), a.fapi_marks()
finally:
    a.fapi = real_fapi
check('funding: a second page from the last settlement + 1 ms', [p['startTime'] for _, p in calls[:2]]
      == [t_first, t_first + 3_600_000 * 1000 + 1])
check('funding: 1,005 hourly settlements summed by holding day, 24 in (27.10 00:00, 28.10 00:00]', abs(sum(per_day.values()) - 1005 * 0.0001) < 1e-12
      and abs(per_day[dt.date(2026, 10, 27)] - 24 * 0.0001) < 1e-12)
check('intervals and marks parsed', intervals == {'BTWUSDT': 4} and marks == {'XMRUSDT': (610.5, 0.0001)})
rep2 = a.report(cs, funds, {k + 'USDT': (cs[k][max(cs[k])][3], 0.0001) for k in cs}, 10000.0, 0.5, 0, (),
                {a.COINS[0] + 'USDT': 4})
hours = {cd['coin']: cd['funding_h'] for cd in rep2['cards']}
check('a card carries its funding interval: 4 h adjusted, 8 h otherwise',
      all(h == (4 if c == a.COINS[0] else 8) for c, h in hours.items()) and rep2['marks_ok'])

print(f'SELFTEST-ADV3 PASS: {len(CHECKS)} of {len(CHECKS)} checks passed')
```

```ini file=deploy/systemd/adv3-bot.service
# btc-5m-twap: ADV-3, the Boss's Binance Futures advisor, as a Telegram bot (TZ-35, CANON PART VII).
# Installed byte for byte as /etc/systemd/system/adv3-bot.service; its stop is systemctl disable --now.
[Unit]
Description=ADV-3 advisor, the Boss's Binance Futures signals over Telegram
Wants=network-online.target
After=network-online.target time-sync.target
StartLimitIntervalSec=3600
StartLimitBurst=5

[Service]
Type=simple
WorkingDirectory=/root/adv3-bot-svc
ExecStart=/root/tz04a-env/venv/bin/python -B -u /root/adv3-bot-svc/adv3-bot.py --serve
Restart=always
RestartSec=30
RestartPreventExitStatus=3 4
Nice=10
MemoryMax=128M
NoNewPrivileges=yes
PrivateTmp=yes
ProtectSystem=strict
ReadWritePaths=/var/lib/adv3-bot
StandardOutput=append:/var/lib/adv3-bot/service.log
StandardError=append:/var/lib/adv3-bot/service.log

[Install]
WantedBy=multi-user.target
```

```python file=research/tz35-advisor-deploy.py
#!/usr/bin/env python3
# tz35-advisor-deploy.py - TZ-35's checker: the fingerprint, the host gate, the number, the scratch and reclaim of
# earlier trees, and every reading of the deployment proof of adv3-bot.service (TZ-35 section 4). Standard library
# only. It starts, stops and signals no unit and no process, sends no request, and never prints the bot's token or a
# chat id. Exits: 0 every assert held; 1 a failed assert, named; 3 NOT YET.
import datetime as dt, hashlib, json, os, re, shutil, stat, subprocess, sys, time

PRIMARY = '/root/btc-5m-twap'
WORK = '/root/tz35-work'
WT = WORK + '/wt'
STATE = WORK + '/state.json'
REPORTS = PRIMARY + '/CryptoReports'
FORENSICS = '/root/btc-forensics'
SVC = '/root/adv3-bot-svc'
ROOT = '/var/lib/adv3-bot'
UNIT = 'adv3-bot.service'
UNIT_FILE = '/etc/systemd/system/adv3-bot.service'
ETC = '/etc/adv3-bot'
TOKEN_FILE = ETC + '/token'
CHAT_FILE = ETC + '/chat-id'
PY = '/root/tz04a-env/venv/bin/python'
ARGV = [PY, '-B', '-u', SVC + '/adv3-bot.py', '--serve']
BRANCH = 'tz-35-advisor-bot'
NUMBER = 'TZ-35-'
TZ_FILE = 'CryptoTZ/TZ-35-advisor-bot.md'
CAPTURE = ('btc-recorder.service', 'btc-pairbook.service', 'btc-rewardbook.service')
ARCHIVE = 'btc-pairbook-archive.service'
LEDGER = '/var/lib/btc-pairbook-archive/ledger.jsonl'
DEFERRED_RUN = 1793260762      # the pair book's archive's set deferred on 2026-10-29 (map section 7 item 128)
RECORDER = '/var/lib/btc-recorder'
REVISION = '2026-10-29-a'
ANCHORS = {'A1': '229a944f2d51', 'A2': '6c5089330629',
           'A3': '0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable',
           'A4': '437b45ea196b', 'A5': '0f6c90451cbd', 'A6': '729f0bcdbee3'}
DERIVED = {'A2': 'research/twap-divergence.py', 'A4': 'BTC-EXECUTOR-INSTRUCTIONS.md',
           'A5': 'research/recorder/recorder.py', 'A6': 'research/pfair.py'}
ROWS, FROZEN, TRACKED, REPORTED = 49, 46, 2, 1
# TZ-35 Appendix A: the files the service copy and the installed unit must equal
SHA = {'advisor/adv3.py': '7f2863a5b433ed7008c8f44af4f9c59d724d0c016c2c317f451158899c4f9adb',
       'advisor/adv3-bot.py': 'e65de91c7b49c6f932db91e568a5956c005e63119c1cf6fb8724ffb0438d1dcb',
       'deploy/systemd/adv3-bot.service': '82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66'}
RULE = 'ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169'
HOST_SHA = 'e3975b5da44c5328adf3bf3914634cd878842c73'
VDA_SIZE = 31612203008
MEM_FLOOR = 170344448          # twice the largest peak of any mode this TZ runs, adv3.py --history's 85,172,224
DISK_FLOOR = 7400000000        # the reward book's STREAM_FLOOR, 7,300,000,000, and this TZ's 100,000,000
LOAD_MAX = 0.05
LOAD_MIN_S = 300
RESTART_MAX_S = 60
DAILY_WAIT_S = 420              # a first attempt, its one retry 300 s later, and the fetch
RUN_WAIT_S = 1200              # the archive timer's OnActiveSec=600 after a reload, and 600 s for a hand-over
STILL_DEADLINE_S = 4200
TOKEN_RE = re.compile(r'[0-9]{5,16}:[A-Za-z0-9_-]{30,64}')
UUID = re.compile(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}')
HASHTOKEN = re.compile(r'[0-9a-f]{16,64}')
LIVE_S = 60
LOG_RE = re.compile(r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})Z (.*)')


class NotYet(Exception):
    pass


def out(*parts):
    print(*parts, flush=True)


def sh(args):
    cp = subprocess.run(args, capture_output=True, text=True)
    return cp.returncode, cp.stdout, cp.stderr


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        for block in iter(lambda: fh.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def utc(t):
    return dt.datetime.fromtimestamp(t, dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%fZ')


def show(unit, *props):
    rc, so, se = sh(['systemctl', 'show', unit] + [x for p in props for x in ('-p', p)])
    assert rc == 0, f'systemctl show {unit}: {se.strip()}'
    return dict(line.split('=', 1) for line in so.splitlines() if '=' in line)


def load_state():
    if not os.path.exists(STATE):
        return {}
    with open(STATE, encoding='utf-8') as fh:
        return json.load(fh)


def save_state(state):
    tmp = STATE + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as fh:
        json.dump(state, fh, indent=1, sort_keys=True)
        fh.write('\n')
    os.replace(tmp, STATE)


def verdict(name, checks):
    for k, v in checks.items():
        out(f'{name} {k:<64} {"PASS" if v else "FAIL"}')
    bad = [k for k, v in checks.items() if not v]
    out(f'READING {name}: {"PASS" if not bad else "FAIL"} - {len(checks) - len(bad)} of {len(checks)}')
    assert not bad, f'{name} FAIL: {bad}'


# ---- /proc ---------------------------------------------------------------------------------------------------

def proc_argv(pid):
    try:
        with open(f'/proc/{pid}/cmdline', 'rb') as fh:
            parts = fh.read().split(b'\0')
    except OSError:
        return None
    return [p.decode('utf-8', 'replace') for p in parts[:-1]] if parts and parts[-1] == b'' else None


def procs(argv):
    return sorted(int(p) for p in os.listdir('/proc') if p.isdigit() and proc_argv(p) == argv)


def _btime():
    with open('/proc/stat', encoding='utf-8') as fh:
        return int([ln for ln in fh.read().split('\n') if ln.startswith('btime ')][0].split()[1])


def _stat_fields(pid):
    with open(f'/proc/{pid}/stat', encoding='utf-8') as fh:
        return fh.read().rsplit(')', 1)[1].split()


def proc_start(pid):
    return _btime() + int(_stat_fields(pid)[19]) / os.sysconf('SC_CLK_TCK')


def proc_cpu(pid):
    f = _stat_fields(pid)
    return (int(f[11]) + int(f[12])) / os.sysconf('SC_CLK_TCK')


def proc_status(pid):
    with open(f'/proc/{pid}/status', encoding='utf-8') as fh:
        return dict(line.split(':', 1) for line in fh.read().splitlines() if ':' in line)


def claude_starts():
    found = []
    for pid in sorted((p for p in os.listdir('/proc') if p.isdigit()), key=int):
        argv = proc_argv(pid)
        if not argv:
            continue
        try:
            start = proc_start(pid)
        except OSError:
            continue
        if argv[0] == 'claude' or argv[0].endswith('/claude.exe'):
            found.append((int(pid), start, argv[0]))
    return found


# ---- pure readings: each takes what the modes read and returns its checks ----------------------------------------

def parse_map(text):
    """(revision, anchors, rows) from SYSTEM-MAP.md's section 0; a row is (path, lines, bytes, state, sha256)."""
    head = text[:text.index('### Fingerprint table')]
    m = re.search(r'\*\*Revision string:\*\* `([^`]+)`', head)
    anchors = dict(re.findall(r'^\| `(A\d)` — [^|\n]+\| `([^`\n]+)` \|$', head, re.M))
    sec = text[text.index('### Fingerprint table'):]
    sec = sec[:sec.index('\n\nHashes are of the file')]
    rows = []
    for path, lines, size, state, sha in re.findall(
            r'^\| `([^`]+)` \| ([^|\n]+) \| ([^|\n]+) \| (frozen|tracked|reported) \| ([^|\n]+) \|$', sec, re.M):
        num = lambda x: int(x.strip().replace(',', '')) if x.strip().replace(',', '').isdigit() else None
        rows.append((path, num(lines), num(size), state, sha.strip().strip('`')))
    return (m.group(1) if m else None), anchors, rows


def log_lines(text):
    """[(UTC second as an epoch, message)] of service.log's own lines; traceback lines belong to the line above."""
    got = []
    for line in text.splitlines():
        m = LOG_RE.fullmatch(line)
        if m:
            t = dt.datetime.strptime(m.group(1), '%Y-%m-%dT%H:%M:%S').replace(tzinfo=dt.timezone.utc).timestamp()
            got.append((int(t), m.group(2)))
    return got


def journal_records(text):
    """Every journal line parsed; a torn last line - a kill mid-write - is counted and left out."""
    lines = text.split('\n')
    recs, torn = [], 0
    for k, line in enumerate(lines):
        if not line:
            continue
        try:
            recs.append(json.loads(line))
        except ValueError:
            assert k == len(lines) - 1, f'journal line {k + 1} does not parse'
            torn += 1
    return recs, torn


def daily_checks(log, recs, pid, t0, today):
    """G-DAILY and G-REPLY: the first process's start, its daily for the close of the day before, and its answer."""
    d1 = str(today - dt.timedelta(days=1))
    after = [x for t, x in log if t >= int(t0) - 1]
    dailies = [r for r in recs if r.get('kind') == 'daily']
    r = dailies[0] if len(dailies) == 1 else {}
    g = {
        'the service logged its start under the unit MainPID': sum(
            x.startswith(f'serving the pinned chat: pid {pid} ') for x in after) == 1,
        'its candles refreshed to the close of the day before, 42 of 42 served': (
            f'candles refreshed to the close of {d1} | missing -' in after),
        'its daily sent once, for the close of the day before': after.count(f'daily sent for the close of {d1}') == 1,
        'exactly one daily record, made today': len(dailies) == 1 and str(r.get('utc', ''))[:10] == str(today),
        'the record: the close of the day before, rule ADV-3': r.get('close_of') == d1 and r.get('rule') == RULE,
        'the record: 10,000 USDT, 0.5% a trade': r.get('deposit') == 10000.0 and r.get('risk_pct') == 0.5,
        'the record: Telegram message ids': bool(r.get('message_ids')) and all(
            isinstance(x, int) for x in r.get('message_ids', [])),
        'the record: 42 signals, at most 3 cards, STRONG among TOP-3': len(r.get('signals', {})) == 42 and len(
            r.get('cards', [])) == len(r.get('top', [])) <= 3 and set(r.get('strong', [])) <= set(r.get('top', [])),
    }
    reply = {'the service answered the pinned chat': any(
        x == 'help sent' or x.startswith('request answered for the close of') for x in after)}
    return g, reply


def restart_checks(log, recs, old_pid, new_pid, new_start, t_kill, nrestarts, active, today):
    """G-RESTART and G-ONCE: a new process, started by systemd after the kill, that sends no second daily."""
    after = [x for t, x in log if t >= int(t_kill)]
    g = {
        'a new MainPID': new_pid > 0 and new_pid != old_pid,
        'started after the kill and at most 60 s later': t_kill < new_start <= t_kill + RESTART_MAX_S,
        'NRestarts 1': nrestarts == '1',
        'active and running': active,
        'the new process logged its start, the daily read as sent today': any(
            x.startswith(f'serving the pinned chat: pid {new_pid} ') and x.endswith(f'daily-sent {today}')
            for x in after),
    }
    once = {
        'still exactly one daily record for today': sum(
            1 for r in recs if r.get('kind') == 'daily' and str(r.get('utc', ''))[:10] == str(today)) == 1,
        'no daily sent after the kill': not any(x.startswith('daily sent') for x in after),
    }
    return g, once


def still_checks(before, after, ledger_before, ledger_after):
    """G-STILL: the recorder and the reward book untouched; the pair book moved by the archive's own restarts alone."""
    g = {}
    for u in ('btc-recorder.service', 'btc-rewardbook.service'):
        b, a = before[u], after[u]
        g[f'{u} kept MainPID, NRestarts and active'] = (a['MainPID'] == b['MainPID'] and a['NRestarts'] == b['NRestarts']
                                                        and a['ActiveState'] == 'active')
    b, a = before['btc-pairbook.service'], after['btc-pairbook.service']
    dn, dl = int(a['NRestarts']) - int(b['NRestarts']), ledger_after - ledger_before
    g['btc-pairbook.service active, restarted only by the archive'] = (
        a['ActiveState'] == 'active' and dn == dl >= 0 and (dn > 0 or a['MainPID'] == b['MainPID']))
    return g


def live_or_earlier(birth, starts):
    """The running claude processes whose start lies within 1 s before to 60 s after a directory's birth."""
    return [pid for pid, s, _a in starts if s - 1 <= birth <= s + LIVE_S]


def reclaimable(tree):
    if tree == WORK:
        return True
    return (tree.startswith('/tmp/') and os.path.isdir(tree) and not os.path.islink(tree)
            and UUID.fullmatch(os.path.basename(tree)) is not None
            and 'btc-5m-twap' in os.path.basename(os.path.dirname(tree)))


def by_name(tree, rel):
    """Kept whatever a report prints: the state, the logs and the history."""
    return tree == WORK and (rel == 'state.json' or rel.startswith('logs/') or rel == 'history.json')


def number_reading(names):
    """NUMBER, map section 7 item 127's repair: CryptoTZ/ holds this TZ's file and no other file of its number, and
    CryptoReports/ no report of that number, so a number used twice stops both specifications before any work."""
    return {'CryptoTZ/ holds TZ-35-advisor-bot.md and no other TZ-35- file': [
                n for n in names if n.startswith('CryptoTZ/' + NUMBER)] == [TZ_FILE],
            'CryptoReports/ holds no TZ-35- report': not any(n.startswith('CryptoReports/' + NUMBER) for n in names)}


def ledger_events(text, run):
    """One run's records in the pair book's archive's ledger text, as (event, deferral count, UTC), and the count of
    lines that do not parse - a run may be writing its last one."""
    got, bad = [], 0
    for line in text.splitlines():
        if not line.strip():
            continue
        try:
            r = json.loads(line)
        except ValueError:
            bad += 1
            continue
        if r.get('run') == run:
            got.append((r.get('event'), r.get('count'), utc(int(r.get('wall_ns') or 0) / 1e9)))
    return got, bad


# ---- the modes -------------------------------------------------------------------------------------------------

def mode_fingerprint():
    with open(PRIMARY + '/SYSTEM-MAP.md', 'rb') as fh:
        raw = fh.read()
    rev, anchors, rows = parse_map(raw.decode('utf-8'))
    out('map', raw.count(b'\n'), 'lines', len(raw), 'bytes, SHA-256', sha256_bytes(raw), '- revision', rev)
    assert rev == REVISION, f'revision {rev!r}'
    assert anchors == ANCHORS, f'anchors {anchors!r}'
    for k, rel in DERIVED.items():
        got = sha256_file(os.path.join(PRIMARY, rel))[:12]
        out(f'anchor {k} {rel} {got}')
        assert got == ANCHORS[k], f'anchor {k}'
    counts = {'frozen': 0, 'tracked': 0, 'reported': 0}
    for path, lines, size, state, sha in rows:
        with open(os.path.join(PRIMARY, path), 'rb') as fh:
            data = fh.read()
        got = (data.count(b'\n'), len(data), sha256_bytes(data))
        counts[state] += 1
        if state == 'frozen':
            assert got == (lines, size, sha), f'frozen {path}: {got} against {(lines, size, sha)}'
        out(f'{state:<8} {path:<46} {got[0]:>6} {got[1]:>8} {got[2]}{"  equal" if state == "frozen" else ""}')
    assert len(rows) == ROWS and counts == {'frozen': FROZEN, 'tracked': TRACKED, 'reported': REPORTED}, counts
    out(f'FINGERPRINT PASS: revision {REVISION}; anchors 6 of 6, 4 re-derived; {len(rows)} rows, {FROZEN} of '
        f'{FROZEN} frozen equal, {TRACKED} tracked, {REPORTED} reported')


def mode_host():
    checks = {}
    rc, so, _ = sh(['find', RECORDER, '-mindepth', '1', '-maxdepth', '3', '-name', 'manifest.json', '-print', '-quit'])
    checks['H1 a recorder manifest exists'] = rc == 0 and len(so.split()) == 1
    rc, so, _ = sh(['df', '-B1', '--output=source,size,avail', RECORDER])
    f = so.splitlines()[1].split() if rc == 0 and len(so.splitlines()) > 1 else ['', '0', '0']
    avail = int(f[2])
    checks['H2 the filesystem is /dev/vda2 of 31,612,203,008 bytes'] = f[0] == '/dev/vda2' and int(f[1]) == VDA_SIZE
    rc, so, _ = sh(['grep', '-c', HOST_SHA, RECORDER + '/runtime.jsonl'])
    checks['H2 the recorder runtime names e3975b5'] = so.strip().isdigit() and int(so) >= 1
    rc, so, _ = sh([PY, '-c', 'import sys; print(sys.version.split()[0])'])
    checks['H3 /root/tz04a-env runs Python 3.12'] = rc == 0 and so.startswith('3.12.')
    units = {}
    for u in CAPTURE:
        units[u] = show(u, 'MainPID', 'NRestarts', 'ActiveState', 'UnitFileState')
        checks[f'H4 {u} active and enabled'] = (units[u]['ActiveState'] == 'active'
                                                 and units[u]['UnitFileState'] == 'enabled')
    rc, _, _ = sh(['systemctl', 'cat', UNIT])
    checks['H5 no adv3-bot unit, file, copy or root'] = rc != 0 and not any(
        os.path.lexists(p) for p in (UNIT_FILE, SVC, ROOT))
    checks['H5 no process under the service argv'] = procs(ARGV) == []
    ok = False
    try:
        se, st = os.lstat(ETC), os.lstat(TOKEN_FILE)
        if (stat.S_ISDIR(se.st_mode) and stat.S_IMODE(se.st_mode) == 0o700 and se.st_uid == 0 and stat.S_ISREG(st.st_mode)
                and stat.S_IMODE(st.st_mode) == 0o600 and st.st_uid == 0 and 0 < st.st_size <= 200):
            with open(TOKEN_FILE, encoding='ascii', errors='replace') as fh:
                body = fh.read()
            ok = body.endswith('\n') and body.count('\n') == 1 and TOKEN_RE.fullmatch(body[:-1]) is not None
    except OSError:
        ok = False
    checks['H6 /etc/adv3-bot 700 and its token 600, one line of a bot token'] = ok
    with open('/proc/meminfo', encoding='utf-8') as fh:
        mem = {k: int(v.split()[0]) * 1024 for k, v in (ln.split(':', 1) for ln in fh.read().splitlines())}
    checks['the memory gate: MemAvailable at least 170,344,448 bytes'] = mem['MemAvailable'] >= MEM_FLOOR
    checks['the disk gate: /dev/vda2 free at least 7,400,000,000 bytes'] = avail >= DISK_FLOOR
    ledger = ledger_restarts()
    out('printed: MemAvailable', mem['MemAvailable'], 'MemTotal', mem['MemTotal'], 'SwapFree', mem['SwapFree'],
        '| free bytes', avail, '| archive ledger restart records', ledger, '| chat-id present',
        os.path.exists(CHAT_FILE))
    for u in CAPTURE:
        out('printed:', u, ' '.join(f'{k}={v}' for k, v in sorted(units[u].items())))
    a = show(ARCHIVE, 'ActiveState', 'Result')
    out('printed:', ARCHIVE, ' '.join(f'{k}={v}' for k, v in sorted(a.items())))
    deferred_run()
    state = load_state()
    state['host'] = {'ns': time.time_ns(), 'units': units, 'ledger_restarts': ledger, 'free_bytes': avail,
                     'mem_available': mem['MemAvailable']}
    save_state(state)
    verdict('HOST', checks)


def ledger_restarts():
    with open(LEDGER, encoding='utf-8') as fh:
        return sum(1 for line in fh if '"event": "restart"' in line)


def deferred_run():
    """Printed, gating nothing: the deferred set's records in the pair book's archive's ledger (map section 7 item
    128) - event names, deferral counts and times alone."""
    with open(LEDGER, encoding='utf-8') as fh:
        held, torn = ledger_events(fh.read(), DEFERRED_RUN)
    out('printed: the archive ledger, run', DEFERRED_RUN, 'records', held, '| lines that do not parse', torn)


def mode_number():
    rc, so, se = sh(['git', '-C', PRIMARY, 'ls-tree', '--name-only', 'origin/main', '--', 'CryptoTZ/', 'CryptoReports/'])
    assert rc == 0, f'git ls-tree: {se.strip()}'
    names = so.splitlines()
    head = sh(['git', '-C', PRIMARY, 'rev-parse', 'origin/main'])[1].strip()
    out('printed: origin/main', head, '|', len(names), 'paths under CryptoTZ/ and CryptoReports/ | of the number',
        NUMBER, [n for n in names if n.split('/', 1)[-1].startswith(NUMBER)])
    verdict('NUMBER', number_reading(names))


def mode_scratch(own):
    parent = os.path.dirname(own)
    starts = claude_starts()
    for pid, t, a0 in starts:
        out('running %d started %s %s' % (pid, utc(t), a0))
    for name in sorted(os.listdir(parent)):
        path = os.path.join(parent, name)
        if path == own or not UUID.fullmatch(name) or not os.path.isdir(path):
            continue
        rc, so, se = sh(['stat', '-c', '%W', path])
        assert rc == 0, se
        owner = live_or_earlier(int(so.strip()), starts)
        out('%s born %s: %s' % (name, utc(int(so.strip())), ('live, process %s' % owner) if owner else 'earlier'))


def mode_reclaim(trees):
    assert trees and all(reclaimable(t) for t in trees), 'reclaim: %r' % (trees,)
    starts = claude_starts()
    for t in trees:
        if t != WORK:
            rc, so, se = sh(['stat', '-c', '%W', t])
            assert rc == 0 and not live_or_earlier(int(so.strip()), starts), 'reclaim: %s belongs to a running process' % t
    tokens = set()
    for name in sorted(os.listdir(REPORTS)):
        if name.endswith('.md'):
            with open(os.path.join(REPORTS, name), encoding='utf-8', errors='replace') as fh:
                tokens.update(HASHTOKEN.findall(fh.read()))
    lengths = sorted({len(t) for t in tokens})
    before = sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    out('reclaim: %d report tokens; forensic store holds %d files' % (len(tokens), before))
    considered = named = kept = copied = held = 0
    for tree in trees:
        if tree == WORK and os.path.isdir(WT):
            rc, so, _ = sh(['git', '-C', WT, 'status', '--porcelain', '--ignored'])
            assert rc == 0 and so == '', 'reclaim: %s holds %r' % (WT, so[:400])
            head = sh(['git', '-C', WT, 'rev-parse', 'HEAD'])[1].strip()
            up = sh(['git', '-C', WT, 'rev-parse', '@{u}'])[1].strip()
            assert head and up == head, 'reclaim: %s at %s, upstream %r' % (WT, head, up)
            out('reclaim: %s skipped: no file but its HEAD\'s, and HEAD %s is its upstream\'s' % (WT, head))
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
                dest = os.path.join(FORENSICS, os.path.basename(tree) + '--' + rel.replace('/', '--'))
                if os.path.exists(dest):
                    assert sha256_file(dest) == h, 'reclaim: %s exists with another hash' % dest
                    held += 1
                    out('R held   %s %s' % (h, dest))
                    continue
                with open(path, 'rb') as src, open(dest, 'xb') as dst:
                    shutil.copyfileobj(src, dst, 1 << 20)
                assert sha256_file(dest) == h, 'reclaim: %s did not copy whole' % dest
                copied += 1
                out('R copied %s %s' % (h, dest))
    after = sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    assert after == before + copied, 'reclaim: store %d, expected %d' % (after, before + copied)
    out('RECLAIM PASS: %d files considered, %d named by a report, %d kept by name, %d copied, %d already held; '
        'forensic store %d -> %d files' % (considered, named, kept, copied, held, before, after))


def mode_mark(name):
    state = load_state()
    rec = {'ns': time.time_ns(), 'mono_ns': time.monotonic_ns()}
    if sh(['systemctl', 'cat', UNIT])[0] == 0:
        rec['unit'] = show(UNIT, 'MainPID', 'NRestarts', 'ActiveState')
    state.setdefault('marks', {})
    assert name not in state['marks'], f'mark {name} taken already'
    state['marks'][name] = rec
    save_state(state)
    out('mark', name, utc(rec['ns'] / 1e9), json.dumps(rec.get('unit', {}), sort_keys=True))


def mode_copy():
    names = sorted(os.listdir(SVC))
    head = sh(['git', '-C', WT, 'rev-parse', 'HEAD'])[1].strip()
    branch = sh(['git', '-C', WT, 'rev-parse', 'origin/' + BRANCH])[1].strip()
    with open(SVC + '/commit.txt', encoding='ascii') as fh:
        commit = fh.read()
    checks = {
        'the copy holds adv3.py, adv3-bot.py and commit.txt alone': names == ['adv3-bot.py', 'adv3.py', 'commit.txt'],
        'adv3.py equal to Appendix A': sha256_file(SVC + '/adv3.py') == SHA['advisor/adv3.py'],
        'adv3-bot.py equal to Appendix A': sha256_file(SVC + '/adv3-bot.py') == SHA['advisor/adv3-bot.py'],
        'commit.txt the branch head, 40 hex and a newline': re.fullmatch(r'[0-9a-f]{40}\n', commit) is not None
                                                           and commit[:-1] == head == branch,
    }
    verdict('COPY', checks)


def mode_props():
    """PROPS: the installed unit's own settings as systemd reads them, before it is started."""
    p = show(UNIT, 'LoadState', 'ActiveState', 'UnitFileState', 'FragmentPath', 'MemoryMax', 'Nice', 'ProtectSystem',
             'NoNewPrivileges', 'PrivateTmp', 'Restart', 'ReadWritePaths', 'RestartPreventExitStatus', 'RestartUSec')
    out('printed:', ' '.join(f'{k}={v}' for k, v in sorted(p.items())))
    checks = {
        'LoadState loaded': p.get('LoadState') == 'loaded',
        'ActiveState inactive': p.get('ActiveState') == 'inactive',
        'UnitFileState disabled': p.get('UnitFileState') == 'disabled',
        'FragmentPath /etc/systemd/system/adv3-bot.service': p.get('FragmentPath') == UNIT_FILE,
        'MemoryMax 134217728': p.get('MemoryMax') == '134217728',
        'Nice 10': p.get('Nice') == '10',
        'ProtectSystem strict': p.get('ProtectSystem') == 'strict',
        'NoNewPrivileges yes': p.get('NoNewPrivileges') == 'yes',
        'PrivateTmp yes': p.get('PrivateTmp') == 'yes',
        'Restart always': p.get('Restart') == 'always',
        'ReadWritePaths /var/lib/adv3-bot': p.get('ReadWritePaths') == ROOT,
    }
    verdict('PROPS', checks)


def mode_unit(n):
    p = show(UNIT, 'Id', 'ActiveState', 'SubState', 'UnitFileState', 'FragmentPath', 'ControlGroup', 'MemoryMax',
             'Nice', 'NRestarts', 'MainPID', 'ProtectSystem', 'NoNewPrivileges', 'Restart', 'ReadWritePaths',
             'RestartPreventExitStatus', 'RestartUSec')
    out('printed:', ' '.join(f'{k}={v}' for k, v in sorted(p.items())))
    pid = int(p.get('MainPID') or 0)
    argv = proc_argv(pid) if pid else None
    try:
        cwd = os.readlink(f'/proc/{pid}/cwd')
        with open(f'/proc/{pid}/cgroup', encoding='utf-8') as fh:
            cg = fh.read()
        nnp = proc_status(pid).get('NoNewPrivs', '').strip()
    except OSError:
        cwd, cg, nnp = None, '', ''
    checks = {
        'ActiveState active': p.get('ActiveState') == 'active',
        'SubState running': p.get('SubState') == 'running',
        'UnitFileState enabled': p.get('UnitFileState') == 'enabled',
        'FragmentPath /etc/systemd/system/adv3-bot.service': p.get('FragmentPath') == UNIT_FILE,
        'ControlGroup /system.slice/adv3-bot.service': p.get('ControlGroup') == '/system.slice/adv3-bot.service',
        'MemoryMax 134217728': p.get('MemoryMax') == '134217728',
        'Nice 10': p.get('Nice') == '10',
        f'NRestarts {n}': p.get('NRestarts') == str(n),
        'ProtectSystem strict': p.get('ProtectSystem') == 'strict',
        'NoNewPrivileges yes': p.get('NoNewPrivileges') == 'yes',
        'Restart always': p.get('Restart') == 'always',
        'ReadWritePaths /var/lib/adv3-bot': p.get('ReadWritePaths') == ROOT,
        'the MainPID runs the exact argv': argv == ARGV,
        'its cwd /root/adv3-bot-svc': cwd == SVC,
        'its cgroup the unit, outside every user slice': '/system.slice/adv3-bot.service' in cg and '/user.slice' not in cg,
        'its NoNewPrivs 1': nnp == '1',
        'the MainPID the only process under the argv': procs(ARGV) == [pid],
        'the installed unit equal to Appendix A': sha256_file(UNIT_FILE) == SHA['deploy/systemd/adv3-bot.service'],
    }
    verdict(f'G-UNIT-{n}', checks)


def mode_daily():
    state = load_state()
    t0 = state['marks']['start']['ns'] / 1e9
    pid = int(show(UNIT, 'MainPID')['MainPID'])
    with open(ROOT + '/service.log', encoding='utf-8', errors='replace') as fh:
        log = log_lines(fh.read())
    path = ROOT + '/journal.jsonl'
    text = open(path, encoding='utf-8').read() if os.path.exists(path) else ''
    recs, torn = journal_records(text)
    today = dt.datetime.now(dt.timezone.utc).date()
    after = [x for t, x in log if t >= int(t0) - 1]
    if not any(x.startswith('daily sent') for x in after) and time.time() < t0 + DAILY_WAIT_S:
        out('NOT YET: no daily line yet, %.0f s after the start' % (time.time() - t0))
        raise NotYet()
    for x in after:
        if 'failed' in x:
            out('printed, a failure the service logged:', x)
    out('printed: journal records', len(recs), 'torn', torn, '| log lines since the start', len(after))
    g, reply = daily_checks(log, recs, pid, t0, today)
    d = [r for r in recs if r.get('kind') == 'daily']
    if d:
        out('printed: the daily record - top', d[0].get('top'), 'strong', d[0].get('strong'), 'cards',
            [(c.get('coin'), c.get('side'), c.get('mode')) for c in d[0].get('cards', [])])
    verdict('G-DAILY', g)
    verdict('G-REPLY', reply)


def mode_load():
    pid = int(show(UNIT, 'MainPID')['MainPID'])
    cpu, wall = proc_cpu(pid), time.time() - proc_start(pid)
    m = show(UNIT, 'MemoryCurrent', 'MemoryPeak', 'MemorySwapCurrent')
    s = proc_status(pid)
    out('printed:', ' '.join(f'{k}={v}' for k, v in sorted(m.items())), '|',
        ' '.join(f'{k}={s.get(k, "").strip()}' for k in ('VmRSS', 'VmHWM', 'VmSwap', 'Threads')))
    out(f'printed: processor {cpu:.2f} s over {wall:.1f} s of wall time since the process started')
    verdict('G-LOAD', {f'at least {LOAD_MIN_S} s since the start': wall >= LOAD_MIN_S,
                       f'processor at most {LOAD_MAX} of the core': cpu / wall <= LOAD_MAX})


def mode_restart():
    state = load_state()
    k = state['marks']['kill']
    p = show(UNIT, 'MainPID', 'NRestarts', 'ActiveState', 'SubState')
    new = int(p['MainPID'] or 0)
    with open(ROOT + '/service.log', encoding='utf-8', errors='replace') as fh:
        log = log_lines(fh.read())
    with open(ROOT + '/journal.jsonl', encoding='utf-8') as fh:
        recs, torn = journal_records(fh.read())
    today = dt.datetime.now(dt.timezone.utc).date()
    g, once = restart_checks(log, recs, int(k['unit']['MainPID']), new, proc_start(new) if new else 0,
                             k['ns'] / 1e9, p['NRestarts'], p['ActiveState'] == 'active' and p['SubState'] == 'running',
                             today)
    out('printed: old MainPID', k['unit']['MainPID'], 'new', new, 'started', utc(proc_start(new)) if new else '-')
    verdict('G-RESTART', g)
    verdict('G-ONCE', once)


def still_wait(last, arch, started_us, now_ns, mono_ns):
    """NOT YET while the archive runs, or while no run of it has started since the last reload of systemd and fewer
    than RUN_WAIT_S have passed - its timer may elapse 600 s after a reload (map section 7 items 115 and 129); past
    STILL_DEADLINE_S it decides on what exists. (wait, a run started after the reload, seconds since the reload)."""
    elapsed = (now_ns - last['ns']) / 1e9
    ran = started_us * 1000 > last['mono_ns']
    busy = arch in ('active', 'activating', 'reloading', 'deactivating')
    return (busy or not ran and elapsed < RUN_WAIT_S) and elapsed < STILL_DEADLINE_S, ran, elapsed


def mode_still():
    state = load_state()
    last = max((state['marks'][m] for m in ('install', 'start', 'stop') if m in state['marks']), key=lambda r: r['ns'])
    a = show(ARCHIVE, 'ActiveState', 'ExecMainStartTimestampMonotonic')
    arch, started_us = a.get('ActiveState', ''), int(a.get('ExecMainStartTimestampMonotonic') or 0)
    wait, ran, elapsed = still_wait(last, arch, started_us, time.time_ns(), time.monotonic_ns())
    if wait:
        out('NOT YET: archive %s, a run since the last reload %s, %.0f s after it' % (arch, ran, elapsed))
        raise NotYet()
    after = {u: show(u, 'MainPID', 'NRestarts', 'ActiveState', 'UnitFileState') for u in CAPTURE}
    before = state['host']['units']
    ledger = ledger_restarts()
    for u in CAPTURE:
        out('printed:', u, 'before', json.dumps(before[u], sort_keys=True), 'after', json.dumps(after[u], sort_keys=True))
    out('printed: the archive ledger restart records', state['host']['ledger_restarts'], '->', ledger, '| archive', arch,
        '| a run since the last reload', ran, '| %.0f s after it' % elapsed)
    deferred_run()
    g = still_checks(before, after, state['host']['ledger_restarts'], ledger)
    if arch in ('active', 'activating', 'reloading', 'deactivating'):
        out('READING G-STILL: UNDECIDABLE - the archive still runs at the deadline')
        return
    if not all(g.values()):
        since = int(state['host']['ns'] / 1e9) - 5
        rc, so, _ = sh(['journalctl', '-u', CAPTURE[0], '-u', CAPTURE[1], '-u', CAPTURE[2], '--since', f'@{since}',
                        '--no-pager', '-o', 'short-iso'])
        out('printed, the capture units\' journal since the host gate:\n' + so)
    verdict('G-STILL', g)


def mode_stopped():
    p = show(UNIT, 'ActiveState', 'UnitFileState')
    checks = {'the unit inactive or failed': p.get('ActiveState') in ('inactive', 'failed'),
              'the unit disabled': p.get('UnitFileState') == 'disabled',
              'no process under the service argv': procs(ARGV) == []}
    verdict('STOPPED', checks)


def mode_selftest():
    n = []

    def ok(cond, name):
        n.append(name)
        assert cond, name

    sample = ('**Revision string:** `2026-10-28-a`\n\n| `A1` — observation set | `229a944f2d51` |\n'
              '| `A3` — phase | `0-complete / 1-x` |\n\n### Fingerprint table\n\n| path | lines | bytes | state | SHA-256 |\n'
              '|---|---|---|---|---|\n| `SYSTEM-MAP.md` | — | — | reported | self-reference; report the value you compute |\n'
              '| `a.py` | 1,135 | 50,928 | frozen | `' + 'a' * 64 + '` |\n| `.gitignore` | 5 | 252 | tracked | `' + 'b' * 64
              + '` |\n\nHashes are of the file as committed')
    rev, an, rows = parse_map(sample)
    ok(rev == '2026-10-28-a' and an == {'A1': '229a944f2d51', 'A3': '0-complete / 1-x'}, 'parse_map: revision, anchors')
    ok(rows == [('SYSTEM-MAP.md', None, None, 'reported', 'self-reference; report the value you compute'),
                ('a.py', 1135, 50928, 'frozen', 'a' * 64), ('.gitignore', 5, 252, 'tracked', 'b' * 64)],
       'parse_map: three rows, commas read')
    log = log_lines('2026-10-29T07:00:01Z serving the pinned chat: pid 42 offset 0 daily-sent -\nTraceback (most\n'
                    '2026-10-29T07:00:03Z candles refreshed to the close of 2026-10-28 | missing -\n'
                    '2026-10-29T07:00:04Z daily sent for the close of 2026-10-28\n2026-10-29T07:00:05Z help sent\n')
    ok([x for _, x in log][1:] == ['candles refreshed to the close of 2026-10-28 | missing -',
                                   'daily sent for the close of 2026-10-28', 'help sent'] and len(log) == 4,
       'log_lines: four own lines, the traceback dropped')
    t0 = dt.datetime(2026, 10, 29, 7, 0, 0, tzinfo=dt.timezone.utc).timestamp()
    rec = {'utc': '2026-10-29T07:00:04+00:00', 'kind': 'daily', 'rule': RULE, 'close_of': '2026-10-28',
           'deposit': 10000.0, 'risk_pct': 0.5, 'top': ['A', 'B', 'C'], 'strong': ['A'], 'message_ids': [5],
           'signals': {str(i): 1 for i in range(42)}, 'cards': [{}, {}, {}]}
    recs, torn = journal_records(json.dumps(rec) + '\n{"utc": "2026-10-29T07:0')
    ok(len(recs) == 1 and torn == 1, 'journal_records: a torn last line counted and left out')
    try:
        journal_records('{"a": 1\n{"b": 2}\n')
        ok(False, 'journal_records: a torn inner line refused')
    except AssertionError:
        ok(True, 'journal_records: a torn inner line refused')
    g, reply = daily_checks(log, recs, 42, t0, dt.date(2026, 10, 29))
    ok(all(g.values()) and len(g) == 8 and all(reply.values()), 'daily_checks: 8 of 8 and the reply on a good day')
    g, _ = daily_checks(log, recs + [dict(rec)], 42, t0, dt.date(2026, 10, 29))
    ok(not g['exactly one daily record, made today'], 'daily_checks: a second daily record fails')
    g, _ = daily_checks(log, recs, 43, t0, dt.date(2026, 10, 29))
    ok(not g['the service logged its start under the unit MainPID'], 'daily_checks: another pid fails')
    short = [(t, x.replace('missing -', 'missing EGLD')) for t, x in log]
    g, _ = daily_checks(short, recs, 42, t0, dt.date(2026, 10, 29))
    ok(not g['its candles refreshed to the close of the day before, 42 of 42 served'],
       'daily_checks: a coin not served fails')
    log2 = log + [(int(t0) + 100, 'serving the pinned chat: pid 50 offset 3 daily-sent 2026-10-29')]
    g, once = restart_checks(log2, recs, 42, 50, t0 + 95, t0 + 60, '1', True, dt.date(2026, 10, 29))
    ok(all(g.values()) and all(once.values()), 'restart_checks: a clean restart passes')
    g, once = restart_checks(log2 + [(int(t0) + 101, 'daily sent for the close of 2026-10-28')], recs, 42, 50,
                             t0 + 95, t0 + 60, '1', True, dt.date(2026, 10, 29))
    ok(not once['no daily sent after the kill'], 'restart_checks: a second daily after the kill fails')
    g, _ = restart_checks(log2, recs, 42, 50, t0 + 125, t0 + 60, '1', True, dt.date(2026, 10, 29))
    ok(not g['started after the kill and at most 60 s later'], 'restart_checks: a restart 65 s late fails')
    u = lambda pid, n: {'MainPID': str(pid), 'NRestarts': str(n), 'ActiveState': 'active'}
    before = {'btc-recorder.service': u(1, 0), 'btc-pairbook.service': u(2, 9), 'btc-rewardbook.service': u(3, 1)}
    ok(all(still_checks(before, before, 5, 5).values()), 'still_checks: nothing moved passes')
    moved = dict(before, **{'btc-pairbook.service': u(7, 10)})
    ok(all(still_checks(before, moved, 5, 6).values()), 'still_checks: one archive restart passes')
    ok(not all(still_checks(before, moved, 5, 5).values()), 'still_checks: a pair book restart without a record fails')
    ok(not all(still_checks(before, dict(before, **{'btc-recorder.service': u(9, 0)}), 5, 5).values()),
       'still_checks: a recorder restart fails')
    ok(TOKEN_RE.fullmatch('123456789:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw') is not None
       and TOKEN_RE.fullmatch('123456789:short') is None and TOKEN_RE.fullmatch('abc:' + 'A' * 35) is None,
       'the token shape: a bot token and two others')
    starts = [(10, 1000.0, 'claude'), (11, 5000.0, '/x/claude.exe')]
    ok(live_or_earlier(5030, starts) == [11] and live_or_earlier(4998, starts) == [] and live_or_earlier(999, starts) == [10],
       'live_or_earlier: born 1 s before to 60 s after a start')
    ok(by_name(WORK, 'logs/03-host.log') and by_name(WORK, 'history.json') and not by_name(WORK, 'stage/x')
       and not by_name('/tmp/x', 'state.json'), 'by_name: the state, the logs and the history of the work tree')
    ok(not reclaimable('/root/other') and reclaimable(WORK), 'reclaimable: the work tree and nothing else outside /tmp')
    last = {'ns': 10 ** 18, 'mono_ns': 5 * 10 ** 12}
    s_ = 10 ** 9
    ok(still_wait(last, 'inactive', 0, last['ns'] + 700 * s_, 0)[0]
       and still_wait(last, 'active', 5 * 10 ** 9 + 1, last['ns'] + 2000 * s_, 0)[0]
       and not still_wait(last, 'inactive', 5 * 10 ** 9 + 1, last['ns'] + 700 * s_, 0)[0]
       and not still_wait(last, 'inactive', 0, last['ns'] + 1300 * s_, 0)[0]
       and not still_wait(last, 'active', 0, last['ns'] + 4300 * s_, 0)[0],
       'still_wait: waits for the run a reload sets off, and no longer than its bounds')
    ok(ARGV == ['/root/tz04a-env/venv/bin/python', '-B', '-u', '/root/adv3-bot-svc/adv3-bot.py', '--serve'],
       'the service argv is the unit\'s ExecStart')
    names = ['CryptoReports/TZ-34-rewardbook-archive-timer-report.md', 'CryptoTZ/TZ-34-rewardbook-archive-timer.md',
             'CryptoTZ/TZ-35-advisor-bot.md', 'CryptoTZ/TZ-35a-other.md']
    ok(all(number_reading(names).values()) and not all(number_reading(names + ['CryptoTZ/TZ-35-other.md']).values())
       and not all(number_reading(names + ['CryptoReports/TZ-35-advisor-bot-report.md']).values())
       and not all(number_reading(names[:2]).values()),
       'number_reading: its one file passes; a second TZ-35- file, a TZ-35- report or none fails')
    text = ('{"event": "start", "run": 1793260762, "wall_ns": 1793260762000000000}\n'
            '{"event": "deferred", "run": 1793260762, "count": 1, "wall_ns": 1793260977000000000}\n\n'
            '{"event": "start", "run": 1793242820, "wall_ns": 1793242820000000000}\n{"event": "comp')
    held, torn = ledger_events(text, DEFERRED_RUN)
    ok([e for e, _c, _t in held] == ['start', 'deferred'] and held[1][1] == 1 and torn == 1
       and held[0][2] == '2026-10-29T07:59:22.000000Z', 'ledger_events: one run\'s records, a torn line counted')
    out(f'SELFTEST PASS: {len(n)} of {len(n)} checks passed')


def main(argv):
    if not argv:
        sys.exit('usage: tz35-advisor-deploy.py MODE [ARG...]')
    mode, rest = argv[0], argv[1:]
    table = {'fingerprint': mode_fingerprint, 'host': mode_host, 'copy': mode_copy, 'props': mode_props, 'daily': mode_daily,
             'load': mode_load, 'restart': mode_restart, 'still': mode_still, 'stopped': mode_stopped,
             'selftest': mode_selftest, 'number': mode_number}
    try:
        if mode == 'scratch':
            assert len(rest) == 1, 'scratch OWN'
            mode_scratch(rest[0])
        elif mode == 'reclaim':
            mode_reclaim(rest)
        elif mode == 'mark':
            assert len(rest) == 1 and rest[0] in ('install', 'start', 'kill', 'stop'), 'mark install|start|kill|stop'
            mode_mark(rest[0])
        elif mode == 'unit':
            assert len(rest) == 1 and rest[0] in ('0', '1'), 'unit 0|1'
            mode_unit(int(rest[0]))
        else:
            assert mode in table and not rest, 'unknown mode %r' % (argv,)
            table[mode]()
    except NotYet:
        return 3
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
```
