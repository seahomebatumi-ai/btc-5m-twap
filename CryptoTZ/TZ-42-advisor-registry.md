# TZ-42 — The registry of STRONG signals: every STRONG signal the bot publishes kept append-only and hash-chained, walked on Binance's 1- and 5-minute candles to its fill, its targets and its end by the rule's own exit; the model's defaults — 200,000 USDT, 0.5 % a trade, 10 % in all, a stop within 14 % — STRONG at every rank, seven new a close, the risk shared by strength; the second check at 15:07 UTC; a reply keyboard

**Canonical filename:** `TZ-42-advisor-registry.md`. The committed file takes this name and no other.

**Executor model: Claude Opus 5.5.** It replaces the advisor's bot — its sizing, its schedule, its views and a new persistent registry whose every signal is walked on live candles — signals a long-lived unit on the capture host, writes one file of its record and, on a rollback after the signal, moves the registry's files out of it.

**Required System Map revision:** `2026-11-01-b`.

**Map sections this TZ rests on**, copied from §10's C8 (map §7 item 141): §0, the fingerprint gate and its table; §1, the refs; §2.5 and §2.6, the archives' calendar runs and the reward book's `STREAM_FLOOR`; §2.7, the advisor's record and TZ-39's and TZ-40's paragraphs; §3, the forensic store, the worktrees and the directories TZ-40's session left; §6, its rows host identity, language, git remote, egress, host is shared, process supervision, memory, disk, both sandbox limits and the harness; §7 items 118, 124, 125, 129, 131, 132 and 136 to 147.

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

**Before `EXECUTE TZ-42`:** the Boss uploads this file alone, into `CryptoTZ/`. `main` already carries map revision `2026-11-01-b` (`a1c7ba1`), PR #40's merge (`494f10f`) and TZ-41's specification (`0ec452e`); nothing else is needed, and no step of the Boss's is a precondition of the run (map §7 item 132). The bot's token and its pinned chat exist (map §2.7); this TZ's own commands read neither, and the bot's `--probe`, which reads the token to send `getMe` and `getMyCommands`, prints neither (§2 item 3).

**When: before 2026-11-08 07:00:00 UTC, epoch `1794121200`, or once TZ-41's report is on `main` — and never while `/root/tz41-work` exists.** TZ-41 runs on this host from 2026-11-08 07:30 UTC and reads the advisor's unit unchanged through its run (its H5 and G-STILL); the host gate (H8) and the `deploy` and `kill` marks refuse outside that window, so the last band before TZ-41 closes at 2026-11-07 23:50:00 UTC. Within it, while `/dev/vda2` holds at least `7,400,000,000` bytes free and `MemAvailable` at least `150,369,520` bytes (§0.4). **B-DEPLOY waits in its own text for 07:30:00 to 11:20:00, 12:20:00 to 14:20:00 or 15:20:00 to 23:20:00 UTC, and B-KILL for 07:30:00 to 11:50:00, 12:20:00 to 14:50:00 or 15:20:00 to 23:50:00 UTC**: clear of the package manager's morning run (map §7 item 143) and of both archives' calendar runs, the reward book's at 01:30:20 and the pair book's at 03:00:20 (map §2.5 and §2.6); clear of the running unit's two checks, 00:10 and 12:10 UTC, and of the new code's second, 15:07, so that the check the new process replays at its start (§1) meets none of them and ends before the next; and each band of B-DEPLOY ends 30 minutes before the band of B-KILL it opens with, so that B-KILL's is still open when COPY, G-RENDER and P-START have run, each at its bound (§6). This TZ reloads systemd **never**, so it sets off no run of either archive (map §7 items 125 and 129). About 50 minutes of wall clock (§6).

**What this TZ is.** The Boss's specification of 2026-11-05, «ADV-3 — Required System Changes», built where it strengthens the advisor and decided where it would weaken it (§1). **A registry of every STRONG signal the bot publishes** — `registry.jsonl` beside the journal, one event a line, each line carrying the SHA-256 of the line before it, so that an edit, an insertion or a removal is seen — **each signal walked forward on Binance's 1- and 5-minute candles** to its fill, its targets and its end: its stop, the rule's own exit at a daily close, or, for a limit not filled, its validity; its result in R and in USDT, its status the Boss's — ACTIVE, TARGET 1, 2 or 3 REACHED, PARTIAL TARGET COMPLETION, STOPPED OUT, INVALIDATED, EXPIRED, and PENDING for a limit not yet filled. **It starts from the bot's own past:** at the new code's first check every STRONG card with an entry the journal holds since TZ-35 is seeded as a signal, sized at the defaults and walked to the moment. **The model's defaults** are the Boss's — a calculation base of `200,000` USDT, `0.5` % a trade at its stop and `1` % at most, `10` % for every open signal together, a stop within `14` % of the entry — and a request's overrides narrow them for that request alone; **the risk is shared by strength**, the strongest trend the most; **the leverage is the rule's**, lowered only to keep the margin at `1,000` USDT (`0.5` % of the capital) or more, never raised; STRONG at every rank, at most seven new signals a close. **The second check moves from 12:10 to 15:07 UTC** (16:10 to 19:07 in Batumi), the first stays at 00:10; both walk every open signal before anything new, and sound only for a new signal or an end. «Сигнал», «Реестр», «Рейтинг», «Оценка» and «Помощь» are a keyboard under every reply, and the bot's command menu carries the same five. **It changes no rule, no parameter of the rule and no coin:** `adv3.py`, `selftest-adv3.py`, `RULE-ADV-3.txt` and the unit file stay what TZ-35 to TZ-40 deployed, byte for byte (G-RULE). It replaces `advisor/adv3-bot.py`, adds its checker `research/tz42-advisor-registry.py`, deploys by replacing the service copy's bot and signalling the unit once, and reads the new process's first check — the day's signal check, which the new process replays at its start because B-KILL's mark sets `check-done` to the slot before it, sent to the Boss's chat by the unit itself, the registry seeded at it — as the deployment's proof on the host (G-FIRST).

---

## 0. Gates

### 0.0 The work tree, first

After contract §1 steps 1 and 2, and before anything else:

```
mkdir /root/tz42-work /root/tz42-work/logs; echo "exit=$?"
```

`exit=0` proves neither existed; anything else is BLOCKED. **From here every command's output goes to `/root/tz42-work/logs/`, one file per step, `NN-<step>.log` in this TZ's order** — the steps of §3.4 to §3.6 and §4.4 under the names their blocks write and the pastes read, `20-b-deploy.log` to `26-first.log` and `30-b-rollback.log` to `35-b-aside.log` — and nothing to the session's scratchpad. The one exception is B-RECLAIM-OWN, §9, which removes the directory the logs are in.

Two abbreviations: **`P`** is `nice -n 19 /root/tz04a-env/venv/bin/python -B`, and **`I`** is `P /root/tz42-work/stage/research/tz42-advisor-registry.py`. **In every block that deploys, signals, restores, moves or removes, both are written out in full**, because the Boss may be handed the block (map §6, sandbox limit).

### 0.1 The files, staged

Extract Appendix A from this TZ as the primary checkout carries it after contract §1's pull, with this script, verbatim, its one argument the destination:

```
/root/tz04a-env/venv/bin/python -B - /root/tz42-work/stage <<'EOF'
import hashlib, os, sys
SRC = "/root/btc-5m-twap/CryptoTZ/TZ-42-advisor-registry.md"
DEST = sys.argv[1]
WANT = {
    "advisor/adv3-bot.py": "c3d9fff54f3585cfc4c33b5f7e1f93b390e62b03e0b4725fee2d6fdda6d04c11",
    "research/tz42-advisor-registry.py": "b6c45490b2f86f5c4678c645041ef1556b1199a6bc814470de904aedf7f5105f",
}
OLD = {  # the committed file an extraction over a worktree replaces, by hash: TZ-40's bot
    "advisor/adv3-bot.py": "9e622daf2e8a5ec3e93f15c7f56e7cf859547fbd3771daad75bc6532adb2b9d1",
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
    if os.path.exists(path):
        with open(path, "rb") as fh:
            assert name in OLD and hashlib.sha256(fh.read()).hexdigest() == OLD[name], ("not the committed file", name)
        mode = "wb"
    else:
        mode = "xb"
    with open(path, mode) as fh:
        fh.write(data)
    print(path, data.count(b"\n"), len(data), hashlib.sha256(data).hexdigest())
EOF
```

| path | lines | bytes | SHA-256 |
|---|---|---|---|
| `advisor/adv3-bot.py` | 2,548 | 157,438 | `c3d9fff54f3585cfc4c33b5f7e1f93b390e62b03e0b4725fee2d6fdda6d04c11` |
| `research/tz42-advisor-registry.py` | 2,088 | 134,077 | `b6c45490b2f86f5c4678c645041ef1556b1199a6bc814470de904aedf7f5105f` |

A failed assert is BLOCKED. Over an empty `stage/` the script creates both files (`xb`); over the branch's worktree, §3.1, it overwrites the committed bot, only after asserting it is TZ-40's by hash, and creates the checker. **The stage holds the new bot alone, without `adv3.py` beside it:** the bot's and the checker's self-tests run from the worktree, §3.2, and nothing imports the stage's bot.

### 0.2 Fingerprint

`I fingerprint` performs contract §1 steps 3 and 4 against `SYSTEM-MAP.md` and the files of its §0 table in the primary checkout `/root/btc-5m-twap`, and asserts them: revision `2026-11-01-b`; the six anchors, `A2`, `A4`, `A5` and `A6` re-derived as the first 12 hex characters of those files' SHA-256; the table's **60** rows, every one read (map §7 item 139) and printed in lines, bytes and SHA-256 — **57** `frozen` rows asserted equal to the map, **2** `tracked` and **1** `reported`, the map's own. It prints `READING FINGERPRINT: PASS - 69 of 69` — 1 revision, 6 anchors, 4 re-derived, 57 rows, 1 shape — or fails at the first mismatch, which is BLOCKED. The advisor rows are `frozen` at TZ-40's hashes and stay so until the verdict of this TZ.

### 0.3 Host gate

From `/root/btc-5m-twap`, with `S` first set to the scratchpad directory the session's system prompt names:

```
date -u; date -u +%s; uptime -s
nproc; grep -E '^(MemTotal|MemAvailable|SwapTotal|SwapFree):' /proc/meminfo
I host
TZ=UTC systemctl list-timers btc-pairbook-archive.timer btc-rewardbook-archive.timer apt-daily-upgrade.timer apt-daily.timer --all --no-pager
TZ=UTC systemctl show btc-pairbook-archive.service btc-rewardbook-archive.service -p Id -p ActiveState -p SubState -p Result
ls -la /root/adv3-bot-svc /var/lib/adv3-bot
du -sb /var/lib/btc-rewardbook /var/lib/btc-pairbook /var/lib/adv3-bot /root/.claude
find /root/btc-forensics -type f | wc -l
git worktree list
echo "$S"; ls -la "$(dirname "$(dirname "$S")")"
```

`I host` asserts these twenty-three, prints each check beside the units' readings, the check records' slots and delays, the journal's size and the span of its STRONG cards, and the memory and disk figures, and prints `READING HOST: PASS - 23 of 23`, or fails:

- **H1** — `find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit` prints one path.
- **H2** — `df` names source `/dev/vda2` and size `31612203008`; `grep -c e3975b5da44c5328adf3bf3914634cd878842c73 /var/lib/btc-recorder/runtime.jsonl` prints at least `1` — two checks. With H1 this is map §6's host identity.
- **H3** — `/root/tz04a-env/venv/bin/python` prints `3.12.`: the interpreter the bot runs under (map §6, language).
- **H4** — `btc-recorder.service`, `btc-pairbook.service` and `btc-rewardbook.service` each read `ActiveState=active` and `UnitFileState=enabled` — three checks: UNIT-NEW compares them, later, against the `kill` mark's snapshot.
- **H5** — `adv3-bot.service` reads `active`, `running`, `enabled`; its `MainPID` runs the unit's exact argv, alone; `/root/adv3-bot-svc` holds `adv3.py`, `adv3-bot.py` and `commit.txt` and nothing else; `adv3.py` and `adv3-bot.py` hash to TZ-40's (`81ef0112…` and `9e622daf…`); the installed unit file hashes to `main`'s (`82acd8e4…`); `commit.txt` is 40 hex characters and a newline — six checks.
- **H6** — `/var/lib/adv3-bot/journal.jsonl` ends in a newline, and `check-done` names a slot, `YYYY-MM-DD signal` or `YYYY-MM-DD fact`.
- **H7 — the clock fires**, map §2.7's open reading: the journal's `check` records from TZ-40's replay — the last record naming `2026-11-01 signal`; TZ-39's first named that slot too, and TZ-40's restart replayed it at 18:06 UTC — name strictly later slots, each once; every one after it — at least one — is stamped at or after its slot's instant under the running code's schedule, 00:10 or 12:10 UTC; and `check-done` names the last one's slot, or its day's `fact` where the last is a signal check stamped at or after 12:10 UTC (`done_after`) — three checks. A slot the unit was down for is a gap, printed and not blocking.
- **H8 — no registry yet, and TZ-41's window** — neither `registry.jsonl` nor `registry-state.json` exists under `/var/lib/adv3-bot/`; the instant is before 2026-11-08 07:00:00 UTC, or `git ls-tree --name-only origin/main -- CryptoReports/TZ-41-l0-our-quote-report.md` names that report; `/root/tz41-work` does not exist — three checks.
- **H9 — the seed's span** — the journal's STRONG cards with an entry that the new code's seed will read (`journal_cards`, the checker's own reading of the seed's rule, §4.2) span at most **120** coin-days to the instant: for each coin the days from its first such card, summed — the span G-RENDER's memory floor was measured at (§0.4).
- **Memory gate** — `MemAvailable` at least `150,369,520` bytes (§0.4); **where the first read is below it, `I host` reads again after 60 s and the second read decides** (map §7 item 137). **Disk gate** — `/dev/vda2` free at least `7,400,000,000` bytes (§0.4).

Any one failing is BLOCKED. **The rest is printed and carries no threshold:** the timers and the two archives' services; the listing of the service copy and the record; `du` of the capture roots and the Claude directory; the forensic store's count, map §3's `2,370`, more where TZ-41 ran first; the worktrees, map §3's two; and the listing of the directory that holds the session's own scratch, whose UUID directories §3.3 names live or earlier. Map §3 records the two TZ-40's session left, `981b3989…` and `e19b6910-2c25-4765-98b9-49d2a819677e`, and one live directory that is no TZ's, `238335b9-cf23-414a-8e8f-ad4705c4d19e`, the remote-control session of 2026-10-30 (TZ-38's report).

### 0.4 Resource floors, in exact bytes

**Disk.** `/dev/vda2` free at least **`7,400,000,000`** bytes: the reward book's `STREAM_FLOOR`, `7,300,000,000`, below which no stream of it opens (map §2.6; `research/tz33-reward-book-capture.py` line 190), plus `100,000,000` for this session at its upper bound — the worktree, about `13,600,000` bytes of tracked files with this file; the stage and the logs under `2,000,000`; the render's scratch — a copy of the bot's journal, under `1,000,000` today, and the registry it seeds, under `100,000` at H9's bound (§6); and the copies of the work tree's files under `5,000,000`. **This TZ never takes free space below the floor that pauses the reward book.** TZ-40 read `10,310,459,392` bytes free at its host gate.

**Memory.** `MemAvailable` at least **`150,369,520`** bytes: twice `75,184,760`. A floor is twice the largest peak among the modes the TZ runs (TZ-37 §0.4), and map §7 item 131 takes the larger of the Architect's measurement and the host's last measured peak of the same code. The largest mode here is `I render`, the service copy's bot answering seven commands — the first seeding a registry from a copy of the bot's journal — and running both checks in one process, the checker keeping every candle the bot read. The Architect measured it on 2026-11-05 on the bytes sent, with Binance stood in for by its own candles of the 42 coins, read record by record from binary files so that the stand-in holds nothing, under Python 3.12.3, the host's interpreter, and under 3.13.18: on a journal in the host's shape — 21 STRONG cards of 4 coins over 20.4 coin-days, as the host's stood on 2026-11-04 — eight runs each, at most `48,545,792` and `47,665,152` bytes; on a heavier one — 411 STRONG cards of 32 coins over **120.8** coin-days, 257 candle requests and 36,382 candles — eight runs each, at most `49,692,672` and `48,951,296`; and `49,762,304` in a run under 3.12.3 before the bot's last edit, which changed one loop's bound and nothing the render holds. **The same method on TZ-40's `I render`** — its bot and checker as `main` holds them, on the host-shaped journal at TZ-40's instant, 2026-11-01 18:05:53 UTC — read `43,302,912` to `44,449,792` bytes across both interpreters, eight runs each, where the host read `65,425,408` (map §7 item 146): **the largest of these figures, at the host's ratio to that method's smallest, gives `75,184,760`** [modelled: `49,762,304` × `65,425,408` / `43,302,912`, rounded up]. **H9 holds the journal within the span measured:** at 437.5 coin-days the same method read `58,740,736` under 3.12.3, so a journal beyond 120 coin-days BLOCKS and the next TZ measures it. **`I render` prints its own peak resident set and its time** (map §7 item 145): the mode is its own wrapper, inside a paste as outside it. The service runs under its unit's `MemoryMax=128M`, which this TZ does not change; the new code's own process, through seven commands and two checks, peaked at most at `46,673,920` bytes on either journal under Python 3.12.3, three runs each (§6). Every mode of this TZ runs under `nice -n 19`.

### 0.5 Refs and the number

```
git -C /root/btc-5m-twap fetch origin
git -C /root/btc-5m-twap ls-remote origin
git -C /root/btc-5m-twap ls-remote --heads origin tz-42-advisor-registry | wc -l
I number
git -C /root/btc-5m-twap log --first-parent --name-status --format='%h %cI %s' -n 5 origin/main
```

Every ref line is reported. **`wc -l` must print `0`:** the branch does not exist. **`I number`** reads `git ls-tree --name-only origin/main -- CryptoTZ/ CryptoReports/` and must print `READING NUMBER: PASS - 2 of 2`: `CryptoTZ/` holds `TZ-42-advisor-registry.md` and no other file whose name begins with `TZ-42-`, and `CryptoReports/` no report whose name does (CANON hard rule 2). Anything else is BLOCKED. A difference in the refs or the log from what map §1 records is recorded, not blocking, unless `main` does not carry revision `2026-11-01-b`.

---

## 1. Why this TZ exists

**The Boss's specification of 2026-11-05**, «ADV-3 — Required System Changes», seven sections, prefaced in his words: "THEREFORE, YOU ARE RESPONSIBLE, AND THE FINAL DECISION IS YOURS!" Its core, in his words: "Maintain a persistent internal registry of every recommendation classified as STRONG, independently of the user's actual exchange positions." "Move the existing reconciliation scheduled for 16:10 Batumi time to **19:07 Batumi time (15:07 UTC)**. Preserve the second daily reconciliation schedule." "Current confidence remains **1/5 until supported by validated evidence**." **He names `crypto-auto` as the place [решение принято мной]:** what his text describes — the `signal` trigger, STRONG candidates, the 16:10 Batumi reconciliation, the five-point confidence at 1/5 — is ADV-3's bot in `advisor/`, and this TZ changes it and nothing else; `crypto-auto` on the host is another project's service (map §6, host is shared), and no step of this TZ reads or touches it. Discarded: a TZ against `crypto-auto`, whose code no clause of his text describes.

**What the frozen rule says, and what moves.** RULE-ADV-3's signal, stop, targets, display rules and STRONG are untouched, `adv3.py` is `main`'s byte for byte, and the forward, PIT and market records are re-derived from Binance's archive by their own TZs (CANON PART VII), never from the bot's journal or registry: **the registry is a record of what the bot published and of what the rule's own exit and the card's stop and targets made of it on Binance's candles — a description, not a measurement; it moves no rung.** The frozen text's Sizing line — deposit 10,000 USDT, 0.5 % a trade, 1 % at most, all open signals together at most 5 % — is TZ-35's display default, and the capital and the risk are the Boss's to set (CANON PART III). **[решение принято мной]** The bot's model carries his new defaults; `RULE-ADV-3.txt` and `adv3.py`'s `DEPOSIT` and `RISK_ALL` stay as frozen, and no signal, stop, R or record moves; CANON PART VII's Size paragraph is revised at this TZ's verdict. Discarded: holding the frozen 5 % against his 10 % — sizing measures nothing, and his risk is his.

| the Boss's section | before this TZ | built as |
|---|---|---|
| 1 — defaults: 200,000 USDT, 0.5 %, 10 %, 14 %; overrides per request, through a menu or parameters | 10,000 USDT and 0.5 % by default; an allocation's budget and N only in «сигнал <budget> топ <N>»; 5 % in all; 14 % | `DEFAULTS`: `CAPITAL` `200000.0`, `adv3.RISK` `0.5`, `RISK_TOTAL` `10.0`, `STOP_MAX` `14.0`, `NEW_MAX` `7`; `params` reads «сигнал 50000 риск 0,75 лимит 8 стоп 12 топ 3», each override for that request alone, each only narrowing its limit; the reply keyboard and Telegram's command menu |
| 2 — STRONG at any rank, the strongest the most, margin 1,000–7,000 (8,000), margin apart from notional, per-trade and aggregate limits, no leverage or risk raised, exclusions with reasons, 200,000 a base | STRONG at every rank since TZ-40; TZ-37's `plan` — shares by `\|z\|`, 1 % and 5 %, the rule's leverage, a 5 USDT minimum | `candidates` over `strong_all`; `allocate`, the shares `min(\|z\|, 3)`; `position` — the notional the loss at the stop allows with both sides' costs, the rule's leverage lowered only to keep the margin at 0.5 % of the capital, the margin at most 4 % and above 3.5 % flagged, within 0.5 % of the coin's volume; margin, leverage, notional and coins, and the loss in USDT and percent, on the card; every coin not taken named with its reason; «Капитал 200 000 USDT — база расчёта, не ваш баланс» |
| 3 — a persistent registry: ID, timestamp, symbol, direction, entry, stop, targets, classification, allocation, leverage, validity, status changes, outcome; the statuses; persistence; no duplicates | none of its own: TZ-39's checks re-derived the trades the cards offered from the journal at every check, on daily candles and the forming one | `Registry`: `registry.jsonl`, append-only, every line flushed to the disk and chained by SHA-256, and `registry-state.json`, rebuilt from the log where lost; `register` and `seed`; `walk`; `status_of`; one signal a coin, side and close (below) |
| 4 — the second run at 15:07 UTC, the first kept; every open signal rechecked first; material changes notified | 00:10 and 12:10 UTC; the offered trades held on daily candles and the forming one | `SLOTS` 00:10 and 15:07 UTC; `check` walks every open signal (`ensure`, `reconcile`, `walk`) before the model's new ones; loud only for a new signal or an end; the weakening a note |
| 5 — the confidence 1/5 until validated; STRONG's performance evaluated, auditable, no threshold changed | rung 1; TZ-38's history in «оценка» | `RELIABILITY` `1` unchanged; `stats_lines` in «оценка» and «реестр»; the registry's chain the audit; no threshold moves |
| 6 — concise mobile reports: new STRONG with positions, material changes, progress and outcomes, risk and room, reasons; no wording of the Boss's real positions | TZ-39's and TZ-40's messages, the offered trades under «Сделки по карточкам бота — бот не видит ваш счёт» | `compose`, `signal_view`, `registry_view`, `ranking_view`, `assess_view`; «Модель бота при капитале 200 000 USDT … не ваш счёт» |
| 7 — reuse, verify, report | — | the journal, `check-done`, the schedule's functions, the unit and `adv3`'s rule functions reused; the bot's self-test 135 checks, the checker's 102, G-RENDER's 34 on live data; the report's limitations (§4.5) |

**Repeated recommendations [решение принято мной].** His §3 asks both "Track repeated recommendations independently when their entries or risk parameters differ" and "Prevent duplicate records during repeated analyses." On this bot the first, read literally, defeats the second: a card's market entry is the price of the moment, so every «сигнал» of a day differs from the last and would write the same trade again. **One signal a coin, a side and a close, and one open signal a coin:** a card repeated while its signal lives is that signal shown again — the card says «Сигнал #N с <instant>: <status>, вход <price>» — and a coin opens a new signal only once its last has ended, at a later close; a signal ended at its own close is not opened again that close. A request's own capital, risk or limits size its reply and write nothing: the registry holds the model's signal at the defaults. Discarded: a record per differing entry, which would count one outcome several times — inflating exactly the target and stop rates his §5 judges trust by ("Do not increase confidence based solely on signal volume") — and count one coin's risk twice against the 10 %.

**The margin [решение принято мной].** The loss at the stop is the risk; the margin is the collateral the exchange holds. At the rule's leverage — `⌊1 / (1.5·d + 0.01)⌋`, at most 20, so that liquidation lies beyond the stop — the margin is `1.55` to `2.27` times the loss at the stop for a stop from 2 % to 14 % of the entry [computed: `1 / (lev · (d + 0.002))` over that range in steps of 0.001 %]: `1,550` to `2,270` USDT at `0.5` % of `200,000`, up to `4,550` at `1` % — inside his 1,000–7,000. **The leverage is the rule's, lowered only to keep the margin at `0.5` % of the capital — `1,000` USDT — or more, never raised**; a notional under that floor is no position, its reason named — "Never increase leverage or risk artificially to meet the minimum position size." A margin above `3.5` % of the capital, `7,000` USDT, is flagged as the exception; above `4` %, `8,000`, the notional is cut to it. The bounds are percentages of the capital, so a request at another capital scales them. Discarded: lowering the leverage to spread the margins over his range — more of his money held as collateral, and no less lost at the stop.

**The risk shared by strength.** "Allocate more personal margin to the strongest, highest-conviction candidate and progressively less to lower-ranked candidates": among the k new signals of a close each takes the share `min(|z|, 3) / Σ min(|z|, 3)` of `k × 0.5 %`, at most the rule's `1 %`, in the rule's order, within the room every open signal leaves under `10 %`; a share the room cuts is marked so, one it empties named «лимит общего риска 10% исчерпан». Seven new signals a close at most, counting those the registry already holds of it; beyond them «сверх 7 новых сигналов за закрытие». The cap of `3` on `|z|` is TZ-37's `Z_CAP`.

**The 10 % [решение принято мной].** Every signal open or waiting counts against it at its own risk — the seeded ones (below) at `0.5 %` each — so the limit is the loss if every open signal stops at once. On a day of one direction it is one bet: on the archive's heaviest close, 2026-09-27, 35 of the 42 were STRONG at every rank, every one LONG (TZ-40 §1). The risk line splits the total by side. Discarded: counting only the model's new signals, which would leave the seeded ones outside the limit they share a market with.

**The seed [решение принято мной].** "Never discard previous signal history when issuing a new recommendation": at the registry's first check — the new process's replay (below) — every STRONG card with an entry, at market or as a limit, of the journal's `daily`, `request`, `alloc` and `check` records since TZ-35 — of an allocation only the trades it placed or sized as more — is a **legacy** signal issued at its record's instant, to the second, unless its coin, side and close already hold one or its coin still holds one open then, walked on its candles to that instant; each sized as one trade at `0.5 %` of `200,000`. Their events are the history's and are never announced as news; the first message says how many it took, open, ended and expired. Discarded: an empty registry from the restart, which would drop every STRONG card the Boss has had since 2026-10-29.

**The walk [решение принято мной].** "Determine outcomes from available chronological market data and existing strategy rules. Never assume actual order execution." A signal is walked on `fapi.binance.com`'s 5-minute candles of its coin from its issue, its first minutes — from the issue to the next 5-minute boundary — on 1-minute candles, because a 5-minute candle's range mixes the minutes before the issue with those after it. A market entry is filled at the card's price at the card's instant — the price the Boss was shown; a limit when a candle reaches it, at the open where the open is already past it. A filled signal's candle credits each target its open is already past, then ends the signal at a stop it reaches — at the open where the open is beyond the stop — and otherwise credits each target it reaches: **a candle that reaches both a target and the stop counts the stop alone**, because the order inside a candle is not known. Each daily close the walk passes ends a filled signal whose sum of four signs has left its side — the rule's own exit — at that close's price; a limit not filled by the close after its card's, 00:00 UTC two days after the close it is of, expires. The result: the move from the fill, both sides' costs (`0.1 %` a side) and the funding of every close held — the coin's own, `+0.01 %` per 8 h where none is published — in R of the planned risk `|entry − stop|` and in USDT at the signal's quantity. A candle not yet closed is read and not walked past. Discarded: crediting the target first in a candle that reaches both, which would write a better outcome than the data supports.

**The statuses**, the Boss's: PENDING — a limit not yet filled — ACTIVE and TARGET 1, 2 or 3 REACHED while a signal lives; at its end TARGET 3 REACHED, PARTIAL TARGET COMPLETION (a target and not the third), STOPPED OUT, INVALIDATED (the rule's exit before any target) and EXPIRED.

**The figures, and the confidence.** «Оценка» adds the registry's figures over its ended signals — the targets reached against TZ-38's history with their 95 % Wilson intervals, the stops before a target, the sum and mean of R with Student's 95 % interval, the result in USDT and in percent of the capital, by side, by the signal's age at its card and by BTC's signal — and the line that only the forward and PIT readings, after 2027-10-28 and 2027-10-31, move the rating: the registry describes and does not prove. Below 30 ended signals they carry «мало для выводов». `RELIABILITY` stays `1`, the evidence ladder's rung (CANON PART VII; map §7 item 142).

**The checks.** At 00:10 UTC (04:10 in Batumi) and, since this TZ, 15:07 UTC (19:07) each check walks every open signal to the moment before anything new, then writes the model's new signals at the defaults — after its message is sent, so that a signal exists once it has been published. The 00:10 message holds its events, the new STRONG with their positions, the signals open with where each stands in R, the notes — a signal whose coin is no longer STRONG, its rule signal kept: information, never an exit (CANON PART VII) — the model's risk and room, the coins not taken and why, and the registry's fingerprint; the 15:07 message its events, the new signals, the entry zones left and the risk. **Loud only for a new signal or an end — a stop, the rule's exit, a limit not filled**; fills and targets go quiet; a check with nothing to say is one quiet line. «Сигнал» answers at the defaults or at the request's overrides and writes the model's new signals it showed; «Реестр» lists the signals open, the last ten ended and the figures; «Рейтинг [N]» the rule's first N coins, 7 by default, ★ on every STRONG; «Оценка» the rung and the figures; «Помощь» the commands. The keyboard rides on every reply's last part, and the unit sets Telegram's command menu at its start.

**The first check after the restart.** As TZ-40's (map §2.7): B-KILL's mark asserts that `check-done` names the latest slot of the running code — 00:10 or 12:10 UTC — and writes it to the day before's `fact`; the old process holds its slot in memory and never reads the file again. **The new process reads that slot at its start and replays the day's signal check at once** — the close of the day before, in the new format — **seeding the registry at it**, so that the Boss's first message of the new code says what the registry took; a signal check that ends at or after 15:07 marks the day's fact check done too (`done_after`). G-FIRST reads that check, its record and the registry from the host (§4.3); nothing in this TZ sends or fakes a message to the Boss's chat. Where the run rolls back before the new process advanced `check-done`, the rollback mark writes the kill mark's value back; where it rolls back after the signal, B-ASIDE moves the registry's files out of the record into the work tree (§4.4). TZ-40's code reads a journal the new code wrote: the Architect ran TZ-40's bot on two such journals, five commands and both checks each, without a failure.

**What it costs after the session.** At 00:10 at most 177 requests to `fapi.binance.com` — 84 for the candles and funding, two for the marks and the funding intervals, at most 42 for the volumes of the STRONG coins, one for the 5-minute candles of each coin holding an open signal, at most 42, and one for each new signal's first minutes, at most 7; at 15:07 at most 93, the candles held; a «сигнал» at most 93 more. The journal grows by about `7,000` bytes a check record [measured: `6,778` to `7,066` on both of §0.4's journals] and the registry by about `400` bytes an event, at most `682` a line, a signal three to five events. The seed runs once (§6).

**What this TZ does not do.** No new rule, no parameter of the rule, no coin, no change to `adv3.py`, the rule text or the unit, no scan beyond the 42, no frozen record of the registry, no change to the confidence, no new unit and no reload of systemd. It reads nothing of the Boss's exchange: the registry is the bot's model at `200,000` USDT, and every view says so.

---

## 2. Scope

**Paths this TZ writes.** On the branch `tz-42-advisor-registry`: `advisor/adv3-bot.py`, modified, and `research/tz42-advisor-registry.py`, new. On the host: `/root/tz42-work/**`; `/root/adv3-bot-svc/adv3-bot.py` and `/root/adv3-bot-svc/commit.txt`; **`/var/lib/adv3-bot/check-done`**, by the checker's `kill` mark and, where §4.4 says, its `rollback` mark, each by one rename through `check-done.tz42`; **where §4.4 says, `registry.jsonl`, `registry-state.json` and `registry-state.json.tmp` moved out of `/var/lib/adv3-bot/` into the work tree by B-ASIDE**; `/root/btc-forensics/tz42-work--*`. On `main`: the report, `CryptoReports/TZ-42-advisor-registry-report.md`. **The unit itself, once restarted, writes `check-done`, its journal, its registry and its log** — its own writes, not this TZ's.

**Prohibited**, by path and by content class:

1. Any change to a repository file but the two above and the report — `advisor/adv3.py`, `advisor/selftest-adv3.py`, `advisor/RULE-ADV-3.txt`, `deploy/systemd/adv3-bot.service`, `SYSTEM-MAP.md` and `BTC-EXECUTOR-INSTRUCTIONS.md` among them.
2. Any change to a definition or a constant of `adv3-bot.py` but those §4.1 names: G-RULE reads it, and `adv3.py` byte for byte.
3. Any read, copy, print or hash of anything under `/etc/adv3-bot/`, and any request to Telegram or to Binance by this TZ's own commands, but two: G-RENDER runs the service copy's bot, whose `Data`, `live_report`, `volumes` and `klines` read Binance's public futures market, and P-START runs the bot's own `--probe`, whose function reads the token to send `getMe` and `getMyCommands` and prints the bot's username and the menu's count, never the token or a chat id. The unit makes its own requests.
4. Any `systemctl` verb but `show`, `list-timers`, `is-enabled`, `kill --signal=SIGTERM adv3-bot.service` (B-KILL, B-KILL2) and, on a FAIL of UNIT-OLD, `disable --now adv3-bot.service` (K-42). No `daemon-reload`, `enable`, `restart`, `start`, `stop` or `mask`.
5. Any change to a capture unit, its store, either archive's timer or ledger — `systemctl show` and `list-timers`, `du`, and under the recorder's root `find`, `grep -c` and `df` read them; any read or write under `/root/tz41-work`, but `test -e` of it by `I host` and the marks; and any read of `crypto-auto` or another service of the shared host.
6. Any write to the unit's record but `check-done` by the marks and B-ASIDE's move: `journal.jsonl`, `offset`, `daily-sent`, `service.log`, `registry.jsonl` and `registry-state.json` are the unit's.
7. A dataset or a binary in git history.
8. A coin, a price, a size or a card from the live replies, from the render's scratch journal or registry, or from the bot's own journal or registry printed in the report or the logs: G-RENDER, G-FIRST and the marks print counts and labels alone, and no file of the work tree is printed, whole or in part, but by a command this TZ names (map §7 item 118). The day's cards are the Boss's to read in his chat.
9. The report on `main` before the branch is pushed and its pull request opened (contract §4.1).

**Exemptions.** The requests of item 3, each by the service copy's own code, as TZ-40's P-START and G-RENDER made theirs; the scratch of item 8 — `render-state/journal.jsonl`, a copy of the bot's own taken by `I render`, and `render-state/registry.jsonl` and `registry-state.json`, the registry the render seeds from it — never printed and never kept, removed with the tree; item 6's `check-done`, a slot and nothing else, printed by the marks, `I host` and §3.7; and item 6's move by B-ASIDE, which takes the registry the new process wrote out of the record only after a rollback has restored and restarted TZ-40's code, which never reads it — the files kept in the forensic store by hash and never printed (§9).

---

## 3. The work, in this order

### 3.1 The branch and its files

```
git -C /root/btc-5m-twap fetch origin
I number
git -C /root/btc-5m-twap worktree add -b tz-42-advisor-registry /root/tz42-work/wt origin/main
```

`I number` must print `READING NUMBER: PASS - 2 of 2` again, or BLOCKED. Then §0.1's script again, verbatim but for its argument, `/root/tz42-work/wt`; it must print the same lines, bytes and SHA-256 as at §0.1. Then:

```
git -C /root/tz42-work/wt add advisor/adv3-bot.py research/tz42-advisor-registry.py
git -C /root/tz42-work/wt diff --cached --name-status
git -C /root/tz42-work/wt diff --cached --numstat
```

`--name-status` must print exactly two lines — `M` for `advisor/adv3-bot.py`, `A` for the checker — and `--numstat` exactly `1903	1224	advisor/adv3-bot.py` and `2088	0	research/tz42-advisor-registry.py`, or BLOCKED. Commit them alone; `git ls-remote origin` (§0.5); push with `git push -u origin tz-42-advisor-registry` — through `credential.helper=!gh auth git-credential` where the URL's credential is refused (map §6, git remote) — and open the pull request against `main`. A failed assert here is BLOCKED.

### 3.2 The self-tests and G-RULE

```
P /root/tz42-work/wt/advisor/selftest-adv3.py
P /root/tz42-work/wt/advisor/adv3-bot.py --selftest
P /root/tz42-work/wt/research/tz42-advisor-registry.py selftest
I rule
```

They must print `SELFTEST-ADV3 PASS: 57 of 57 checks passed`, `SELFTEST PASS: 135 of 135 checks passed`, `SELFTEST PASS: 102 of 102 checks passed` and `READING RULE: PASS - 8 of 8`. **The checker's self-test runs from the worktree**, whose copy is the stage's by §0.1's hashes, because it loads the bot from `../advisor/` beside itself, where the worktree holds `main`'s `adv3.py` and the new bot. The first three reach no network — the checker's runs the worktree's bot on a synthetic market with Binance and Telegram stood in for (§5); `I rule` reads `git show origin/main:` of `adv3.py`, `adv3-bot.py`, `selftest-adv3.py`, `RULE-ADV-3.txt` and the unit file, and the branch's files. A red check stops the run here, and it goes to §3.7 and §9.

### 3.3 The directories beside this session

```
P /root/btc-5m-twap/research/tz35-advisor-deploy.py scratch "$(dirname "$S")"
```

lists every UUID directory beside this session's own and names each **live** — born from 1 s before to 60 s after the start of a running process whose `argv[0]` is `claude` or ends in `/claude.exe` — or **earlier**. **B-RECLAIM-SCRATCH**, for every directory it names **earlier** — none it named live, and never this session's own:

```
P /root/btc-5m-twap/research/tz35-advisor-deploy.py reclaim <each earlier directory, by its full path>
rm -rf <one such directory>; echo "exit=$?"
test -e <that directory>; echo "exit=$?"
```

One `reclaim` names every earlier directory and must print `RECLAIM PASS` before any removal; then one `rm -rf` and one `test -e` a directory, the last reading `exit=1`. TZ-35's checker is `main`'s, frozen by the map's table, and its `reclaim` refuses a directory born with a running claude process and any path that is not a UUID directory under `/tmp/` whose parent's name carries `btc-5m-twap`. Map §3 expects TZ-40's two directories (§0.3) — or TZ-41's, where TZ-41 ran first — unless a reboot emptied `/tmp`; each holds the harness's copy of its session's background output (map §6, harness); the live session of 2026-10-30 is not touched. If `scratch` names none earlier, the block is recorded as empty and skipped. **Where the classifier refuses it, the Boss runs it as one line** (map §6, sandbox limit; §7 items 124 and 138), the Executor writing in every earlier directory's full path, one `rm -rf` and one `test -e` a directory, all chained to the `reclaim`'s `exit=0`, which it reaches only after `RECLAIM PASS`:

```
{ date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/btc-5m-twap/research/tz35-advisor-deploy.py reclaim <D1> <D2>; echo "exit=$?"; } >> /root/tz42-work/logs/12-reclaim-scratch.log 2>&1 && tail -n 1 /root/tz42-work/logs/12-reclaim-scratch.log | grep -qx 'exit=0' && { date -u +%FT%T.%NZ; rm -rf <D1>; echo "exit=$?"; test -e <D1>; echo "exit=$?"; rm -rf <D2>; echo "exit=$?"; test -e <D2>; echo "exit=$?"; } >> /root/tz42-work/logs/12-reclaim-scratch.log 2>&1
```

**It holds back nothing of §3.4 to §3.6**, which read none of what it removes (map §7 item 140).

### 3.4 B-DEPLOY, then COPY and G-RENDER

All of §3.1 and §3.2 PASS first. Then **B-DEPLOY**, which waits for its band and records its mark inside the block:

```
until s=$(( $(date +%s) % 86400 )); { [ $s -ge 27000 ] && [ $s -le 40800 ]; } || { [ $s -ge 44400 ] && [ $s -le 51600 ]; } || { [ $s -ge 55200 ] && [ $s -le 84000 ]; }; do sleep 5; done; { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz42-work/stage/research/tz42-advisor-registry.py mark deploy && cp -p /root/adv3-bot-svc/adv3-bot.py /root/tz42-work/bot.before && cp -p /root/adv3-bot-svc/commit.txt /root/tz42-work/commit.before && git -C /root/tz42-work/wt show origin/tz-42-advisor-registry:advisor/adv3-bot.py > /root/adv3-bot-svc/adv3-bot.py.new && mv /root/adv3-bot-svc/adv3-bot.py.new /root/adv3-bot-svc/adv3-bot.py && git -C /root/tz42-work/wt rev-parse origin/tz-42-advisor-registry > /root/adv3-bot-svc/commit.txt; echo "exit=$?"; } >> /root/tz42-work/logs/20-b-deploy.log 2>&1
```

07:30:00 to 11:20:00, 12:20:00 to 14:20:00 and 15:20:00 to 23:20:00 UTC are seconds `27,000` to `40,800`, `44,400` to `51,600` and `55,200` to `84,000` of the day. **`I mark deploy` refuses — and the block copies nothing — outside TZ-41's window or where a registry exists in the record** (H8); `bot.before` then does not exist, nothing was copied, and the run is BLOCKED. Otherwise `exit=0`, or B-ROLLBACK (§4.4). `adv3.py` is not copied: the service copy's is `main`'s, and COPY asserts it. The running process keeps the old code in memory until it is signalled. Then:

```
I copy >> /root/tz42-work/logs/21-copy.log 2>&1; echo "exit=$?" >> /root/tz42-work/logs/21-copy.log
timeout 900 I render >> /root/tz42-work/logs/22-render.log 2>&1; echo "exit=$?" >> /root/tz42-work/logs/22-render.log
```

`I copy` must print `READING COPY: PASS - 5 of 5`; `I render` imports the service copy's bot, points its `STATE` at `/root/tz42-work/render-state/` holding a copy of the bot's own `journal.jsonl` and no registry, replaces Telegram by a stand-in, answers seven commands — the first seeding the scratch registry from the copy — and runs both checks on `fapi.binance.com`'s live data, prints its peak resident set and its time, and must print `READING RENDER: PASS - 34 of 34`. A FAIL of either, or a `timeout`, is B-ROLLBACK (§4.4), and nothing is signalled.

### 3.5 P-START, B-KILL, then UNIT-NEW and G-FIRST

Only after COPY and G-RENDER PASS. **P-START**, CANON hard rule 14's proof of the request path, through the service copy's own functions:

```
P /root/adv3-bot-svc/adv3-bot.py --probe >> /root/tz42-work/logs/23-probe.log 2>&1; echo "exit=$?" >> /root/tz42-work/logs/23-probe.log
```

It must print `READING P-START: served - 6 of 6 endpoints, 8 requests` (§4.3). A FAIL is B-ROLLBACK (§4.4), and nothing is signalled. Then **B-KILL**, its mark inside the block:

```
until s=$(( $(date +%s) % 86400 )); { [ $s -ge 27000 ] && [ $s -le 42600 ]; } || { [ $s -ge 44400 ] && [ $s -le 53400 ]; } || { [ $s -ge 55200 ] && [ $s -le 85800 ]; }; do sleep 5; done; { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz42-work/stage/research/tz42-advisor-registry.py mark kill && systemctl kill --signal=SIGTERM adv3-bot.service; echo "exit=$?"; } >> /root/tz42-work/logs/24-b-kill.log 2>&1
```

07:30:00 to 11:50:00, 12:20:00 to 14:50:00 and 15:20:00 to 23:50:00 UTC are seconds `27,000` to `42,600`, `44,400` to `53,400` and `55,200` to `85,800`. **`I mark kill` refuses — and writes and signals nothing — where `check-done` does not name the latest slot of the running code**, 00:10 or 12:10 UTC of the day — the running process then owes a check — **outside TZ-41's window, or where a registry exists**, and the run goes to B-ROLLBACK (§4.4) with the unit not signalled; **otherwise it writes `check-done` to the day before's `fact`** by one rename, reads it back, and records both values in `state.json`, and the signal follows. At least 45 s later, then every 15 s while it prints `NOT YET` and exits `3`, and for at most 100 s after the mark: `I unit new` — **UNIT-NEW**, `READING UNIT-NEW: PASS - 9 of 9`. Then every 15 s while it prints `NOT YET` and exits `3`, for at most 900 s after the mark: `I first` — **G-FIRST**, `READING FIRST: PASS - 10 of 10`. Each run's output is appended to `25-unit-new.log` and `26-first.log`. A FAIL of either is B-ROLLBACK (§4.4).

### 3.6 The Boss's one paste — CANON hard rule 14

**The Executor tries each block once; a refused one is handed to the Boss unchanged, with the paste below** (map §7 item 138). Each step's output goes to the log the Executor's own step names, under a `date -u` line and appended, each step gated on the one before it by that log's last line, and the bands wait in the text (map §7 item 124). **P-BOSS-A** is handed over where B-DEPLOY is refused, and only while a band of B-DEPLOY is open — 07:30:00 to 11:20:00, 12:20:00 to 14:20:00 or 15:20:00 to 23:20:00 UTC — so that B-KILL's band is open too when the paste reaches it and its waits are seconds; the Executor waits for that band before handing it over. It runs B-DEPLOY, COPY, G-RENDER — which times itself — P-START, B-KILL, UNIT-NEW and G-FIRST:

```
until s=$(( $(date +%s) % 86400 )); { [ $s -ge 27000 ] && [ $s -le 40800 ]; } || { [ $s -ge 44400 ] && [ $s -le 51600 ]; } || { [ $s -ge 55200 ] && [ $s -le 84000 ]; }; do sleep 5; done; { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz42-work/stage/research/tz42-advisor-registry.py mark deploy && cp -p /root/adv3-bot-svc/adv3-bot.py /root/tz42-work/bot.before && cp -p /root/adv3-bot-svc/commit.txt /root/tz42-work/commit.before && git -C /root/tz42-work/wt show origin/tz-42-advisor-registry:advisor/adv3-bot.py > /root/adv3-bot-svc/adv3-bot.py.new && mv /root/adv3-bot-svc/adv3-bot.py.new /root/adv3-bot-svc/adv3-bot.py && git -C /root/tz42-work/wt rev-parse origin/tz-42-advisor-registry > /root/adv3-bot-svc/commit.txt; echo "exit=$?"; } >> /root/tz42-work/logs/20-b-deploy.log 2>&1; tail -n 1 /root/tz42-work/logs/20-b-deploy.log | grep -qx 'exit=0' && { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz42-work/stage/research/tz42-advisor-registry.py copy; echo "exit=$?"; } >> /root/tz42-work/logs/21-copy.log 2>&1 && tail -n 1 /root/tz42-work/logs/21-copy.log | grep -qx 'exit=0' && { date -u +%FT%T.%NZ; timeout 900 nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz42-work/stage/research/tz42-advisor-registry.py render; echo "exit=$?"; } >> /root/tz42-work/logs/22-render.log 2>&1 && tail -n 1 /root/tz42-work/logs/22-render.log | grep -qx 'exit=0' && { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/adv3-bot-svc/adv3-bot.py --probe; echo "exit=$?"; } >> /root/tz42-work/logs/23-probe.log 2>&1 && tail -n 1 /root/tz42-work/logs/23-probe.log | grep -qx 'exit=0' && { until s=$(( $(date +%s) % 86400 )); { [ $s -ge 27000 ] && [ $s -le 42600 ]; } || { [ $s -ge 44400 ] && [ $s -le 53400 ]; } || { [ $s -ge 55200 ] && [ $s -le 85800 ]; }; do sleep 5; done; } && { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz42-work/stage/research/tz42-advisor-registry.py mark kill && systemctl kill --signal=SIGTERM adv3-bot.service; echo "exit=$?"; } >> /root/tz42-work/logs/24-b-kill.log 2>&1 && tail -n 1 /root/tz42-work/logs/24-b-kill.log | grep -qx 'exit=0' && sleep 45 && for k in 1 2 3 4; do { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz42-work/stage/research/tz42-advisor-registry.py unit new; echo "exit=$?"; } >> /root/tz42-work/logs/25-unit-new.log 2>&1; tail -n 1 /root/tz42-work/logs/25-unit-new.log | grep -qx 'exit=3' || break; sleep 15; done; tail -n 1 /root/tz42-work/logs/25-unit-new.log 2>/dev/null | grep -qx 'exit=0' && for k in $(seq 1 60); do { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz42-work/stage/research/tz42-advisor-registry.py first; echo "exit=$?"; } >> /root/tz42-work/logs/26-first.log 2>&1; tail -n 1 /root/tz42-work/logs/26-first.log | grep -qx 'exit=3' || break; sleep 15; done; echo "P-BOSS-A ended"
```

**P-BOSS-B** is handed over where the Executor's B-DEPLOY, COPY, G-RENDER and P-START passed and B-KILL alone is refused, while B-KILL's band is open; it runs B-KILL, UNIT-NEW and G-FIRST:

```
tail -n 1 /root/tz42-work/logs/23-probe.log | grep -qx 'exit=0' && { until s=$(( $(date +%s) % 86400 )); { [ $s -ge 27000 ] && [ $s -le 42600 ]; } || { [ $s -ge 44400 ] && [ $s -le 53400 ]; } || { [ $s -ge 55200 ] && [ $s -le 85800 ]; }; do sleep 5; done; } && { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz42-work/stage/research/tz42-advisor-registry.py mark kill && systemctl kill --signal=SIGTERM adv3-bot.service; echo "exit=$?"; } >> /root/tz42-work/logs/24-b-kill.log 2>&1 && tail -n 1 /root/tz42-work/logs/24-b-kill.log | grep -qx 'exit=0' && sleep 45 && for k in 1 2 3 4; do { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz42-work/stage/research/tz42-advisor-registry.py unit new; echo "exit=$?"; } >> /root/tz42-work/logs/25-unit-new.log 2>&1; tail -n 1 /root/tz42-work/logs/25-unit-new.log | grep -qx 'exit=3' || break; sleep 15; done; tail -n 1 /root/tz42-work/logs/25-unit-new.log 2>/dev/null | grep -qx 'exit=0' && for k in $(seq 1 60); do { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz42-work/stage/research/tz42-advisor-registry.py first; echo "exit=$?"; } >> /root/tz42-work/logs/26-first.log 2>&1; tail -n 1 /root/tz42-work/logs/26-first.log | grep -qx 'exit=3' || break; sleep 15; done; echo "P-BOSS-B ended"
```

While a paste runs, the Executor runs nothing that reads the service copy, the unit or its record. **Once it ends, the Executor reads every log it wrote; the paste's own reads are the gates' reads, and no mode of the checker is run again** (map §7 item 144). Every outcome is verified from the logs, and from the closing reads of §3.7, never from the Boss's account. A FAIL inside a paste is B-ROLLBACK (§4.4), the Executor's, handed over unchanged if refused.

### 3.7 The closing reads

```
TZ=UTC systemctl show adv3-bot.service btc-recorder.service btc-pairbook.service btc-rewardbook.service btc-pairbook-archive.service btc-rewardbook-archive.service -p Id -p MainPID -p NRestarts -p ActiveState -p Result -p Nice -p MemoryCurrent -p MemoryPeak -p ActiveEnterTimestamp
TZ=UTC systemctl list-timers btc-pairbook-archive.timer btc-rewardbook-archive.timer --all --no-pager
systemctl is-enabled adv3-bot.service; echo "exit=$?"
journalctl -u adv3-bot.service --no-pager -o short-iso | tail -n 20
tail -n 30 /var/lib/adv3-bot/service.log
ls -la /var/lib/adv3-bot /root/adv3-bot-svc
cat /var/lib/adv3-bot/check-done
free -b; df -B1 --output=source,size,avail /var/lib/btc-recorder
du -sb /root/tz42-work /root/adv3-bot-svc /var/lib/adv3-bot /var/lib/btc-rewardbook /var/lib/btc-pairbook /root/.claude
cat /root/tz42-work/state.json
```

The journal holds systemd's own lines for the unit; `service.log` the service's own — a start with the `check-done` it read, the registry it loaded, the command menu set or refused, a refresh, a check sent or failed, a request answered — with no token, no chat id and no price, and a coin only where Binance failed to serve it. **The next scheduled check is the first the running unit's clock fires under this code** — the 15:07 UTC fact check of the same day where the restart came before 14:50, else the 00:10 UTC signal check of the next — the next TZ's host gate reads it (H7); nothing in this TZ waits for it.

---

## 4. The gates — fixed here, before any of their data exists

| gate | population | PASS | false failure | power, against |
|---|---|---|---|---|
| **G-RULE** | `origin/main`'s `adv3.py`, `adv3-bot.py`, `selftest-adv3.py`, `RULE-ADV-3.txt` and the unit file, and the branch's files | 8 of 8 (§4.1) | `0` — the files and their syntax trees read directly | `1`, `adv3.py`, its self-test, the unit or the rule text changed, or a definition of the bot changed beyond Appendix A |
| **SELFTESTS** | the three self-tests | 57 of 57, 135 of 135 and 102 of 102 | `0` | `1`, a changed expectation or a red check |
| **COPY** | the service copy | 5 of 5 (§4.3) | `0` | `1`, a file not `main`'s or Appendix A's, or not the branch head's |
| **G-RENDER** | the service copy's bot answering seven commands and running both checks on live data, over a copy of its own journal and the registry it seeds from it | 34 of 34 (§4.3) | `0` — the registry read against the checker's own chain, seed and walk, replayed on every candle the bot read in the order it read them; each position and allocation against the checker's own arithmetic; each reply against the view it was made from; the records against the checker's own order and STRONG; fixed labels and limits | `1`, a broken chain, a legacy signal not its card's, a fill, target or end the walk does not find or one it finds missing, a result in R or USDT not the walk's, a place not the replay's, two signals of a coin open at once, a margin, leverage, loss or risk beyond its arithmetic or its limits, a wanted risk not the shares', risk beyond the room or 10 %, more than seven new a close, a reply not its view, a loud check without a new signal or an end, a reply without its keyboard, another constant |
| **P-START** | six endpoints, eight requests, through the service copy's own functions | `READING P-START: served - 6 of 6 endpoints, 8 requests` | `0` — each read directly | `1`, a refused request — `451`, `403` — or a reply of another shape |
| **UNIT-NEW** | the unit after the signal | 9 of 9 (§4.3) | `0` | `1`, a process not new, not the new code's, not started from the replay slot, a traceback, a capture unit moved |
| **G-FIRST** | the new process's first check: its record, `check-done`, its log and the registry it seeded | 10 of 10 (§4.3) | `0` | `1`, no check at the start, another slot or close, no message sent, a record without its fields, a loud check without a new signal or an end, a failure in the log, a registry not whole or not seeded from the journal it read |

**Family-wise false failure `0`:** every gate reads its quantity directly and none samples. A FAIL before B-DEPLOY is BLOCKED and deploys nothing; a FAIL of COPY, G-RENDER, P-START, B-KILL's mark or signal, UNIT-NEW or G-FIRST is B-ROLLBACK (§4.4).

### 4.1 G-RULE

`I rule` asserts eight. **Three of the files** are `main`'s, byte for byte: `advisor/RULE-ADV-3.txt` (`ee206e7c…`, and the `RULE` constant of the branch's `adv3.py`); `deploy/systemd/adv3-bot.service` (`82acd8e4…`); and `advisor/adv3.py` and `advisor/selftest-adv3.py` (`81ef0112…` and `6f29b82f…`) — so the rule's fourteen functions, `report`, `card`, `trust`, `assessment` and the rest of `adv3.py` are TZ-40's. **Three of `adv3-bot.py`**, by `ast.dump` against `main`'s: the definitions that changed are exactly `Telegram`, `base_record`, `candidates`, `check`, `check_record`, `compose`, `done_after`, `due`, `event_lines`, `handle`, `hello`, `probe`, `route`, `selftest`, `serve` and `zone_lines` — sixteen; those added exactly fifty-seven — `Registry`, `advance`, `allocate`, `assess_view`, `base_fund`, `bat`, `by_side`, `card_lines`, `carded`, `ceil1`, `ceil5`, `chain_line`, `day_ms`, `ended_line`, `ensure`, `event_line`, `excluded_lines`, `first_window`, `footer`, `from_iso`, `iso`, `item_record`, `klines`, `last_check`, `legend`, `line_hash`, `live_line`, `mean_ci`, `model_plan`, `ms_at`, `new_signal`, `note_lines`, `notes_of`, `notional_of`, `open_risk`, `params`, `params_line`, `pct0`, `position`, `ranking_view`, `reconcile`, `register`, `registry_view`, `risk_line`, `second`, `seed`, `seed_line`, `sg`, `signal_view`, `signed_usdt`, `stats_lines`, `status_of`, `t975`, `view_plan`, `walk`, `wilson` and `zones_of`; those removed exactly twenty-three — `alerted`, `alerts_of`, `alloc_fields`, `candidate_lines`, `correlation`, `follow`, `followed_lines`, `forming_candles`, `item_lines`, `journal_scan`, `make`, `numbers`, `offers`, `plan`, `plan_parts`, `plan_strong`, `quiet_line`, `returns_of`, `strong_shares`, `top_n`, `weak_lines`, `weakened` and `zones_left`; **the 23 others are identical** — `Data`, `TooMany`, `append`, `chunks`, `find_chat`, `hhmm`, `journal_records`, `latest_slot`, `liquidity`, `live_report`, `log`, `main`, `malloc_tune`, `next_at`, `put`, `ranked`, `read`, `slot_at`, `slot_key`, `slot_parse`, `slot_text`, `strong_all` and `volumes` — **so the candles' fetch, the live report, the rule's order, STRONG at every rank, the volumes, the schedule's arithmetic and the modes are TZ-40's**; of the assignments `CARD_KEYS`, `HELP`, `SLOTS` and `TOPN` changed, twenty-one added — `(CAPITAL, RISK_TOTAL, STOP_MAX, NEW_MAX)`, `(K1_MS, K5_MS, K5_PAGE)`, `(LIQ_FRAC, Z_CAP, LIQ_DAYS)`, `(MARGIN_MIN, MARGIN_MAX, MARGIN_EXC)`, `(RANK_LIST, RANK_MAX)`, `(REG_FILE, REG_STATE, GENESIS)`, `COMMANDS`, `DAY_MS`, `DEFAULTS`, `HELPS`, `INTERVAL`, `KEYBOARD`, `KEYWORDS`, `LABEL`, `LEGACY_KEYS`, `LOUD`, `NUMBER`, `RANKING`, `REGISTRY`, `SHOWN` and `T975` — and `(STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, CROWD, Z_CAP, LIQ_DAYS)`, `FOOTER` and `LIST_MAX` removed. **One more:** `due` and `done_after` are `main`'s code, their docstrings alone changed — the schedule is TZ-39's, its second slot moved by `SLOTS`. **One more:** the branch's `adv3-bot.py` hashes to Appendix A's. TZ-37's `plan`, which TZ-40 kept, goes: the Boss's §2 replaces its sizing (§1).

### 4.2 What Appendix A answers

**The model.** `DEFAULTS` — capital `200,000` USDT, a trade's risk `adv3.RISK` `0.5` %, all open signals `10` %, the stop within `14` % of the entry, `7` new signals a close. `params` reads a request: «риск X», «лимит X» («всего X»), «стоп X» and «топ N» name theirs; of the other numbers the first of 100 or more is the capital and the first below 100 the risk, as TZ-37 read them; `15 000` reads 15000 and `10k`, `10к` and `10 тыс` 10000. An override narrows its limit and never widens it: the risk at most `adv3.RISK_MAX`, `1` %, the total at most `10` %, the stop at most `14` %, N at most `7`; the capital `100` to `10,000,000` USDT, the risk at least `0.05` %, the total `0.5` %, the stop `2` %, N `1`. The parameters a reply rests on, and those the request set, head it.

**The registry** (`Registry`), under `/var/lib/adv3-bot/`: `registry.jsonl`, one event a line — `seed`, `open`, `fill`, `target`, `stop`, `exit`, `expire` — each carrying `n`, its place, `at`, the instant it was written, and `prev`, the SHA-256 of the line before it, `0` × 64 for the first, written with its keys sorted and flushed to the disk before it takes effect; a line edited, inserted or removed breaks the chain at the line after it, and a torn last line — a write cut short — is cut at load and counted. `registry-state.json`, written in one rename: each open signal's place — the first minute not yet walked as closed, the last daily close its walk passed, its largest favourable excursion in R — and the number of events a message has announced; lost, it is rebuilt from the events, every place from its signal's issue. **A signal** is its `open` event — id (1, 2, … in the order of the opens), issue instant, coin, side, the close it is of, its source (`check:<slot>`, `request` or, seeded, `journal:<kind>`), entry mode, entry, stop, three targets, close, unit, `z`, the sum of signs, rank, the day its rule signal began, BTC's signal, how many coins were STRONG at every rank, its validity (00:00 UTC two days after its close), and its position at the defaults — capital, risk in percent, loss at the stop, notional, quantity, leverage, margin — and whether it is legacy; then its events. `status_of` gives the Boss's statuses (§1). At most one signal a coin is open at once.

**The seed** (`seed`), the registry's first event and the legacy signals (§1): its event names the journal by SHA-256, its records that parse and its STRONG cards with an entry; the cards are read one coin at a time, each coin's 5-minute candles fetched once from its first card and let go before the next coin's, and the signals and their events written in the order of the cards.

**The walk** (`walk`, `first_window`, `reconcile`), as §1 states it: each coin's 5-minute candles fetched once, from the earliest 5-minute boundary its signals' places reach, and a signal's first minutes on 1-minute candles where its place is still inside them, in one request; the events appended in time order and the places saved; a coin whose candles fail stays where it was, logged; a start after the moment — a signal issued this minute — asks Binance for nothing (`klines`).

**The plan.** `candidates`: the STRONG coins at every rank of the report's close, in the rule's order — those whose signal of this close the registry holds open, those that may be new (current prices, an entry, a stop within the limit, no signal of the coin open from an earlier close and none of this close ended), and the rest named with a code and a reason: `marks` — no current price, `near` — the price at the stop, no entry, `stop` — beyond the limit, `ended` — this close's signal already ended. `model_plan`: the new candidates at the defaults, the first seven a close counting those the registry holds of it, sized by `allocate` within the room every open signal leaves under `10` %; beyond seven `count`, or `room` where the room stopped one of the first. `view_plan`: a request's plan at its parameters — the registry's signals of this close and the model's new ones, carded at the request's capital and risk, the first N in the rule's order sized within the room the signals of earlier closes leave under the request's total, those beyond N named `top`; a coin the model did not take keeps the model's reason; the request writes no signal the model did not take. `allocate` and `position`, as §1 states them: `room` where the room cut a risk to nothing, `margin` where a notional is under the margin's floor — by liquidity where the volume capped it; each position with its wanted risk and whether the room cut it, and the flags «урезано лимитом риска», «ограничено ликвидностью» and «маржа выше 3,5% капитала — исключение».

| view | what it shows |
|---|---|
| «сигнал», the keyboard's «Сигнал», `/signal` | the close, the cards' validity (04:00 two days on, in Batumi), the parameters; the events not yet announced; **«STRONG закрытия dd.mm»** — the registry's signals of this close and the model's new ones, each its card: number, coin, side, `#id` or «🆕 #id», ★ its rank and «вне ТОП-3» beyond the TOP-3, `z`; entry at market with its zone, or a limit, or none; the signal's status since its issue; stop with its distance, three targets; **margin · leverage · notional and coins; the loss at the stop in USDT and in percent of the capital**, or why there is no position now; the signals open from earlier closes, each where it stands in R; the model's risk — earlier closes plus this one, of the limit, free in percent and in USDT, by side; **«Не берём»** — every coin not taken, grouped by reason; the targets' line with TZ-38's shares; `adv3.BEYOND` where a card is beyond the TOP-3; the confidence line |
| «реестр», `/registry` | the counts — signals since the first close, open, closed, expired; «Модель бота при капитале 200 000 USDT … не ваш счёт»; the open ones; the last ten ended, each how it ended, after which target, when, its R and USDT; the figures — targets reached, stops before a target, the sum and mean of R with its interval, USDT; the chain's fingerprint, or «цепочка нарушена на событии N» |
| «рейтинг [N]», `/ranking` | the rule's first N coins in its order (`ranked`), 7 by default, all 42 at most: side, `z`, the sum of signs, ★ on STRONG at every rank, `#id` of an open signal; the day's changes; the others counted |
| «оценка», `/rating` | `adv3.assessment`, unchanged — the rung, the next readings, the six ratings, the forward record, the history — then the registry's figures in full (§1) and that only the forward and PIT readings move the rating |
| «помощь», `/help`, `/start`, anything else | `HELP`: the commands, the defaults, the overrides and their ceilings, the checks at 04:10 and 19:07 in Batumi and what sounds |
| the 00:10 check | the events, loud for a stop, an exit or an expiry; the new STRONG with their positions, or «Новых STRONG нет»; the open signals; the notes; the risk; «Не берём»; the targets' line; the registry's fingerprint — or one quiet line «✓ … событий нет, новых STRONG нет …» where it found no event, no new signal, no note and the coins not taken for the codes of the check before; the first after the seed says what the seed took |
| the 15:07 check | the events; the new STRONG; the entry zones left — a limit at the zone's edge, or no entry near the stop; the risk — or one quiet line naming the next check |

**Telegram:** TZ-40's pace and `429` waits; the reply keyboard — «Сигнал», «Реестр» / «Рейтинг», «Оценка», «Помощь», persistent and resized — on the last part of every reply and of no check; the quiet flag on every part of a quiet check. At its start the unit calls `setMyCommands` once with `/signal`, `/registry`, `/ranking`, `/rating` and `/help`, and logs a refusal without failing.

**The records.** A `check` record: its slot, quiet and one-line flags, every coin's signal, sum, `z`, rank, unit, close and mark; STRONG at every rank; the new signals' cards with their ids and positions; the coins not taken with their reasons and codes; the registry events it announced, by `n`; the notes and zones; the registry's events, head, chain state, open ids, risk and the signals the seed opened where it seeded; the defaults; the six ratings. A `request` record: the parameters, the signals it opened, its cards and positions, the coins not taken; `registry`, `ranking` and `assess` records for those views; `HELP` writes none.

### 4.3 COPY, G-RENDER, P-START, UNIT-NEW and G-FIRST

**COPY** (`I copy`), five: the service copy holds `adv3.py`, `adv3-bot.py` and `commit.txt` and nothing else; `adv3.py` is `main`'s (`81ef0112…`); `adv3-bot.py` is Appendix A's; `commit.txt` is 40 hex characters and a newline equal to the worktree's `HEAD` and to `origin/tz-42-advisor-registry`; the branch's two files equal the service copy's byte for byte.

**G-RENDER** (`I render`), thirty-four, on the service copy's bot, its `klines`, `allocate`, `signal_view` and `live_report` wrapped so that the checker keeps what they read, returned and were given — each candle request with the function that made it and the registry's lines before it, kept compactly — Telegram a stand-in that records each part, its notification flag and whether it carries the keyboard, and `STATE` at `/root/tz42-work/render-state/`, a copy of the bot's journal and no registry. The seven commands are «сигнал», «сигнал 50000 риск 1 лимит 2 топ 3», «реестр», «рейтинг», «оценка», «помощь» and «привет», then the signal check and the fact check of the run's UTC day, each appended to the scratch journal. **The checker rebuilds the registry by its own reading** (`own_chain`, `own_signals`) — **its own seed from the same journal copy** (`journal_cards`, `own_seed`) — and **replays its own walk** (`own_walk`) of every signal on the very candles the bot read, in the order it read them (`replay`): the seed's on the seed's, each later read of a coin's 5-minute candles walking every signal of that coin the registry held before the read, from its place, with the 1-minute candles read next for that place. **It computes its own order and STRONG** (`own_order`, `own_strong`), **its own entry and stop** (`own_entry`), **its own leverage** (`own_lev`) and **its own position arithmetic** (`pos_ok`). (1) every command and both checks answered, no traceback and no failed request in the bot's log; (2) every part's markup balances; (3) the registry's chain is whole from the genesis, every line numbered by its place, the file ending in a newline; (4) its first event is the seed, the only one; (5) the signals are numbered 1, 2, … in the order of their opens; (6) the legacy signals are those the checker's seed opens from the same journal on the same candles — coin, side, close, issue instant, mode, entry, stop and the record's kind — first and in that order; (7) no coin holds two signals open at once; (8) every signal's fill, targets and end, with R and USDT, are those the checker's replay finds on the candles the bot read; (9) every signal open keeps the replay's place; (10) the seed names the journal the bot read, by SHA-256 and its records; (11) every signal opened at the default capital, its position whole by the checker's arithmetic at its entry and stop, a legacy one at most `0.5` %, a model one at most `1` %; (12) every signal valid to 00:00 UTC two days after its close; (13) a market entry filled at its entry at its issue, a limit never at its issue; (14) the model opens a signal only within `10` % of risk, the signals open then counted; (15) the model's signals of a close at most seven, less the legacy ones of that close; (16) to (20) every allocation by the checker's own arithmetic — each wanted risk `k × risk × min(|z|, 3) / Σ`, at most `1` %, never rising along the order; the risk taken within the room and within what each wanted; every position whole, its loss the notional times its stop's distance and both sides' costs, its margin within `0.5` and `4` % of the capital and covering it, its leverage 1 to the rule's, within `0.5` % of the volume; an item left without a position with the room's reason or the margin's; each entry and stop the checker's own, the stop within the limit; (21) each «сигнал» reply is the bot's own view sent in its parts, each position written as the plan holds it, at most N items; (22) «сигнал 50000 риск 1 лимит 2 топ 3» rests on `50,000` USDT, `1` %, `2` % and N `3`, the four names set, the defaults unchanged, and says so; (23) «реестр» its counts, the chain whole and its fingerprint, the figures; (24) «рейтинг» the rule's first seven by the checker's order, ★ exactly on STRONG at every rank; (25) «оценка» the rung `1` and the next readings, the six ratings, the registry's figures and that they move no rung; (26) «помощь» and an unknown text answer `HELP` and nothing else; (27) every reply carries the keyboard on its last part alone and a notification, and no check carries it; (28) and (29) each check's flags agree with what it announced, opened and found — loud exactly with a new signal or an end, one line exactly where it found nothing — every part with the record's flag; (30) both check records carry their slot, every coin's state ranked by the checker's order, STRONG at every rank by the checker's reading, the cards numbered as opened with their positions, the coins not taken with their codes, the registry's head at their events and its chain whole, the defaults and the six ratings; (31) the scratch journal holds, after the bot's own records, `request`, `request`, `registry`, `ranking`, `assess`, `check`, `check`; (32) the scratch registry's state counts every event announced and keeps a place for every signal open; (33) the bot's own `journal.jsonl`, `offset`, `daily-sent` and `check-done` hash as before the run, and no registry is written there; (34) the bot's constants are this TZ's — `CAPITAL` `200000.0`, `RISK` `0.5`, `RISK_MAX` `1.0`, `RISK_TOTAL` `10.0`, `STOP_MAX` `14.0`, `NEW_MAX` `7`, `MARGIN_MIN` `0.5`, `MARGIN_MAX` `3.5`, `MARGIN_EXC` `4.0`, `LIQ_FRAC` `0.005`, `Z_CAP` `3.0`, `COST` `0.001`, `SLOTS` 00:10 and 15:07 UTC, `RELIABILITY` `1`, `PACE` `1.1`, `STRONG_Z` `1.0`, `K1_MS` `60000`, `K5_MS` `300000`. **Only counts and labels are printed:** each reply's size in characters and parts; the bot's log lines; the candle requests, how many of 1-minute candles, and the candles; the allocations and views; the registry's events by type, its signals — legacy, open, ended by a stop, by an exit, expired — and the seed's records and cards; for each check its flags, parts, events announced, signals opened, STRONG at every rank, coins not taken by code, notes and zones; the events the replay walked and the signals whose events differ, by id; then `PEAK <bytes> bytes resident` and its wall and processor seconds. **A day with no STRONG coin to take reads 34 of 34 with no new signal**, and the new views then rest on live data where they are empty, on the legacy signals the seed opens, and on the self-test's synthetic market in full (§5); the report prints the counts.

**P-START** is `adv3-bot.py --probe`, every reply asserted served and parsed: **P-KLINES** — `/fapi/v1/klines?symbol=BTCUSDT&interval=1d&limit=1500` serves closed daily candles, the last at most two days old, each of four prices with its close positive; `/fapi/v1/klines?symbol=BTCUSDT&interval=5m&startTime=<the 5-minute boundary at or after 65 minutes ago>&limit=1000` serves 10 to 14 candles 5 minutes apart, `/fapi/v1/klines?symbol=BTCUSDT&interval=1m&startTime=<the minute at or after 4 minutes ago>&limit=4` 3 or 4 a minute apart, each its high at or above its open and close and its low positive and at or below them, every one but the last closed — the candles the registry walks on; **P-FUNDING** — `/fapi/v1/fundingRate?symbol=BTCUSDT&startTime=<2026-10-27 00:00 UTC>&limit=1000` serves settlements, each a number; **P-MARKS** — `/fapi/v1/premiumIndex` serves a positive mark price for every one of the 42 coins' perpetuals; **P-INTERVALS** — `/fapi/v1/fundingInfo` serves the adjusted funding intervals, each a positive number of hours; **P-TELEGRAM** — `getMe` answers `is_bot` true and a username, which it prints, and `getMyCommands` a list, whose length it prints. Eight requests to six endpoints. **Every header fixed:** to Binance `User-Agent: adv3-advisor/1`, beside `urllib`'s own `Accept-Encoding: identity`, `Host` and `Connection: close`; to Telegram `User-Agent: adv3-bot/1` and `Content-Type: application/json`, beside `urllib`'s `Content-Length`, `Accept-Encoding: identity`, `Host` and `Connection: close`. A refused request is never retried but for a network error, `418`, `429` or a `5xx`, three times after 1, 3 and 5 s (`adv3.get`); Telegram's `call` has one try, and `send` retries a part only on `429`. The unit's own requests at its checks go through the same functions and headers.

**UNIT-NEW** (`I unit new`), nine, read against the `kill` mark's snapshot: the unit `active`, `running`, `enabled`; a new `MainPID` and `NRestarts` one more — read against the mark's, never as a lifetime count (map §7 item 136); the process started after the mark and within 90 s of it; its argv the unit's exact one, alone; the service copy's `adv3.py` `main`'s and `adv3-bot.py` Appendix A's, and the process started after B-DEPLOY's mark; the unit file unchanged; **`service.log` showing the new process serving from the `check-done` the mark wrote** — its `serving the pinned chat: pid <pid> offset <n> check-done <slot>` line naming the day before's `fact`; no traceback since the mark; the three capture units active with their `MainPID` and `NRestarts` as at the mark.

**G-FIRST** (`I first`), ten, from the journal's records stamped since the `kill` mark, `check-done`, `service.log`'s lines since the mark and the registry: exactly one check record; it is the day's signal check, of the close of the day before, under rule `ee206e7c…`; it was sent, its Telegram message ids integers; it holds the 42 coins' state, the six ratings, STRONG at every rank, its cards numbered as it opened them with their positions, the coins not taken and their codes, the registry's head at its events and the seed it made, and is loud exactly with a new signal or an end among the events it announced; `check-done` reads the day's `signal` where the mark came before 15:07 UTC and its `fact` where after — a replay read within 900 s of a mark at or before 14:50 ends before 15:07, and one after a mark at or after 15:20 marks the fact slot done too (`done_after`); the log since the mark shows the new pid serving from the replay slot, the check sent and no check failed and no traceback; the journal ends in a newline and every line from that record on parses; **the registry is whole from the genesis and ends in a newline, its seed first, naming by SHA-256 and its records the journal as the seed read it — its bytes before that check's record**; every legacy signal is a STRONG card of that journal with an entry, issued at its record's instant; the registry's state counts every event announced and keeps a place for every signal open. **NOT YET** while no check record stands since the mark and 900 s have not passed. Printed beside it: the check's flags, its message count, events announced, signals opened, STRONG at every rank, coins not taken, `check-done`, the registry's events and signals — legacy and open — and the journal the seed read, in records, STRONG cards and the first 12 hex characters of its SHA-256 beside the kill mark's — never a coin or a price.

### 4.4 The stops — CANON hard rule 14

**The unit's restart policy is TZ-35's, unchanged** (map §6, process supervision) — `Restart=always`, `RestartSec=30`, `RestartPreventExitStatus=3 4` — and so is its stop, K-35, `systemctl disable --now adv3-bot.service`, which K-42 repeats. **B-ROLLBACK**, on a FAIL of COPY, G-RENDER, P-START, B-KILL's mark or signal, UNIT-NEW or G-FIRST, at once, the Executor's own: the bot and `commit.txt` return to what B-DEPLOY saved, and **`I mark rollback` writes the kill mark's `check-done` back where it still reads the replay slot** — where the new process never ran the replay, so that the old code does not replay the day's message at its start — and leaves it where the new process moved it.

```
{ date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz42-work/stage/research/tz42-advisor-registry.py mark rollback && cp -p /root/tz42-work/bot.before /root/adv3-bot-svc/adv3-bot.py.new && mv /root/adv3-bot-svc/adv3-bot.py.new /root/adv3-bot-svc/adv3-bot.py && cp -p /root/tz42-work/commit.before /root/adv3-bot-svc/commit.txt; echo "exit=$?"; } >> /root/tz42-work/logs/30-b-rollback.log 2>&1
sha256sum /root/adv3-bot-svc/adv3.py /root/adv3-bot-svc/adv3-bot.py; cmp /root/adv3-bot-svc/commit.txt /root/tz42-work/commit.before; echo "cmp exit=$?"; cat /var/lib/adv3-bot/check-done
```

The second line is the Executor's own read. `exit=0`, the `sha256sum` printing `81ef0112…` and `9e622daf…` and `cmp` exit `0`, or the run is BLOCKED with the files' state named. Where the unit was **not** signalled (a FAIL of COPY, G-RENDER, P-START, or B-KILL's mark or signal) that is all: the running process never loaded the new file, it never reads `check-done` again, and no registry exists. **B-KILL's signal counts as not delivered only where `systemctl show adv3-bot.service -p MainPID -p NRestarts` still reads the pid and the restart count its mark printed**; where either moved, the unit was signalled. Where it **was** (a FAIL of UNIT-NEW or G-FIRST), the signal follows, its mark inside the block, in the band of §3.5:

```
until s=$(( $(date +%s) % 86400 )); { [ $s -ge 27000 ] && [ $s -le 42600 ]; } || { [ $s -ge 44400 ] && [ $s -le 53400 ]; } || { [ $s -ge 55200 ] && [ $s -le 85800 ]; }; do sleep 5; done; { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz42-work/stage/research/tz42-advisor-registry.py mark kill2 && systemctl kill --signal=SIGTERM adv3-bot.service; echo "exit=$?"; } >> /root/tz42-work/logs/31-b-kill2.log 2>&1
```

and at least 45 s later `I unit old`, each run appended to `32-unit-old.log` (every 15 s while it prints `NOT YET`, at most 100 s after that mark) — **UNIT-OLD**, `READING UNIT-OLD: PASS - 10 of 10`: UNIT-NEW's nine read against the second mark with TZ-40's `adv3.py` and `adv3-bot.py` — the old process serving from the `check-done` the second mark read, a slot it may owe and run then — and `NRestarts` two more than at the first mark. The records the new process left in the journal stay, and the report counts them; TZ-40's code reads them (§1).

**K-42**, on a FAIL of UNIT-OLD only — the advisor is then stopped, and the Boss is told:

```
{ date -u +%FT%T.%NZ; systemctl disable --now adv3-bot.service; echo "exit=$?"; } >> /root/tz42-work/logs/33-k42.log 2>&1
```

by the classifier route where refused (the Boss runs the block unchanged), verified at least 30 s later by `I stopped`, appended to `34-stopped.log`, which must print `READING STOPPED: PASS - 2 of 2`.

**B-ASIDE**, after UNIT-OLD's PASS — or STOPPED's, where K-42 ran — and only where the unit was signalled: the registry the new process wrote leaves the record, so that TZ-40's code runs beside no file it does not know and the next deployment of a registry starts from none (H8):

```
{ date -u +%FT%T.%NZ; ls -la /var/lib/adv3-bot; ( [ ! -e /var/lib/adv3-bot/registry.jsonl ] || mv -n /var/lib/adv3-bot/registry.jsonl /root/tz42-work/registry.jsonl.rolled ) && ( [ ! -e /var/lib/adv3-bot/registry-state.json ] || mv -n /var/lib/adv3-bot/registry-state.json /root/tz42-work/registry-state.json.rolled ) && ( [ ! -e /var/lib/adv3-bot/registry-state.json.tmp ] || mv -n /var/lib/adv3-bot/registry-state.json.tmp /root/tz42-work/registry-state.json.tmp.rolled ) && test ! -e /var/lib/adv3-bot/registry.jsonl && test ! -e /var/lib/adv3-bot/registry-state.json && test ! -e /var/lib/adv3-bot/registry-state.json.tmp; echo "exit=$?"; } >> /root/tz42-work/logs/35-b-aside.log 2>&1
```

`exit=0`, or BLOCKED with the record's listing named. Each file it finds goes into the work tree under its name with `.rolled` added, and `keep` copies it into the forensic store by hash (§9); none is printed. **Under PASS none of B-ROLLBACK, B-KILL2, K-42 and B-ASIDE is run.**

### 4.5 What a PASS establishes, and what it does not

The service copy's `adv3-bot.py` is Appendix A's and the unit runs it beside `main`'s `adv3.py`; the rule, its functions, `report`, `card`, `trust` and the assessment, the rule text and the unit are what TZ-35 to TZ-40 deployed; the seven commands and both checks are answered on live data with the shapes §4.2 fixes; the registry the render seeded from a copy of the bot's journal is the one the checker's own seed and walk find on every candle the bot read, and every position and allocation is the checker's own arithmetic within the Boss's limits; the new process replayed the day's signal check at its start, seeded the unit's registry from its own journal, and sent it. **Not established:** that the 15:07 and 00:10 checks fire on their own clock under this code — the next TZ's host gate reads it (H7); that Binance's candles are the market — the checker replays the candles the bot read and takes them as served; **that a signal's outcome is what a trade of the Boss's would have made** — the model enters at the card's price at the card's instant, takes the stop first in a candle that reaches both, pays no slippage and the funding as published, and sizes at `200,000` USDT; that Telegram shows the keyboard and the command menu as the Architect expects — the unit logs a refused `setMyCommands`, and the report quotes the log; that a day with a new STRONG signal was among G-RENDER's — the self-test proves the views on a synthetic market, and the report prints the counts; that the sizes suit the Boss — the Architect's formula, unproven; **that STRONG earns** — the registry describes and measures nothing, and the forward record, read after 2027-10-28, measures the rule and the TOP-3's STRONG; and anything about the market to come.

---

## 5. The files

**`advisor/adv3-bot.py`** — replaced. The model: `DEFAULTS`, `params` and `route`, the keyboard and the command menu (`KEYBOARD`, `COMMANDS`), `HELP`. The registry: `Registry` with `load`, `apply`, `append`, `save_state`, `next_id`, `cursor_of` and `live`; `new_signal`, `advance`, `status_of`, `open_risk`, `line_hash`, `event_line`. The candles and the walk: `klines`, `first_window`, `walk`, `reconcile`, `seed`, `ensure`, `base_fund`, `ceil1`, `ceil5`, `second` and the instants' helpers. The plan: `notional_of`, `position`, `allocate`, `candidates`, `carded`, `model_plan`, `view_plan`, `register`. The messages: `card_lines`, `live_line`, `ended_line`, `event_lines`, `risk_line`, `excluded_lines`, `chain_line`, `seed_line`, `note_lines`, `zone_lines`, `notes_of`, `zones_of`, `compose`, `signal_view`, `registry_view`, `ranking_view`, `assess_view`, `stats_lines` with `wilson`, `t975` and `mean_ci`, `footer`, `legend`, `params_line`. The checks and requests: `check_record`, `check` and `handle`; `serve` with the registry loaded and the menu set at its start; `probe` with the 5- and 1-minute candles and `getMyCommands`; `Telegram.send` with the keyboard; `SLOTS` with 15:07. TZ-40's followed trades (`journal_scan`, `offers`, `follow`, `alerted`, `alerts_of`, `forming_candles`), TZ-37's `plan` with `plan_strong` and `plan_parts`, and their helpers go (§4.1). Every other line — `Data`, `live_report`, `ranked`, `strong_all`, `liquidity`, `volumes`, the schedule's arithmetic and `main` among them — is TZ-40's. **`selftest`, 135 checks offline:** 49 of `route`'s readings — the commands, their parameters and their ceilings; `HELP` and the keyboard, two; twelve of Telegram — the parts, the rename, HTML and its plain fallback, the quiet flag, the keyboard on the last part, the pace, three of the `429`, `call`'s refusals, the token kept out of the log; eight of the schedule with its 15:07 slot, three days minute by minute among them; nine of the registry's chain — written, read back, broken by an edit, a removal and a line that does not parse, a torn line cut, the state rebuilt; sixteen of the walk on hand-built candles — targets then the stop, a candle reaching both, an open beyond the stop and one past a target, a short, a limit at itself, at an open past it, filled and stopped, expired, the rule's exit at a close with its funding, a candle not yet closed, `until`, and four of the first minutes on 1-minute candles; two of the requests — `reconcile`'s, and none asked for a start after the moment; six of `position` by hand; four of `allocate` — three by hand and 300 random scenarios; six of the candidates and the plans; two of `register`; two of the seed; three of the statistics by hand; seven end to end with Binance and Telegram stood in for — two signal checks, two fact checks, Telegram down and the retry, the registry read back; three of `handle`; and four more — the markup, no wording of the Boss's account or positions, glibc, `time.sleep` restored. Every expectation is computed by hand or by a formula of its own, never by the code under test.

**`research/tz42-advisor-registry.py`** — this TZ's checker: `fingerprint`, `host`, `number`, `rule`, `selftest`, `mark` (`deploy`, `kill`, `rollback`, `kill2`), `copy`, `render`, `unit` (`new`, `old`), `first`, `keep` and `stopped`. Where a reading can be a pure function it is — `parse_map`, `top_level`, `tree_checks`, `strip_docs`, `html_balanced`, `own_order`, `own_strong`, `sign_sum`, `journal_lines`, `journal_objects`, `records_since`, `count_kind`, `prefix_before_check`, `own_chunks`, `own_chain`, `head_at`, `own_signals`, `start_of`, `own_walk`, `journal_cards`, `coin_days`, `own_seed`, `union_k5`, `replay`, `same_events`, `registry_checks`, `own_entry`, `own_stop_pct`, `own_lev`, `pos_ok`, `alloc_checks`, `opens_checks`, `model_checks`, `flags_checks`, `unit_checks`, `first_checks`, `slot_instant`, `latest_slot_text`, `replay_text`, `clock_checks`, `served_from`, `log_since`, `memory_gate`, `number_reading`, `window_reading`, `kept_files` — each its own reading of the rule and of the Boss's limits, never the bot's functions; `Candles` keeps the candles the render's bot read compactly. Its self-test, 102 checks: each pure reading on stand-ins, with a negative control for every one that can fail, 77; `render_run`, the render's own pipeline, **on the worktree's bot with a synthetic market of fourteen coins and Binance stood in for**, 34 of 34 — every event met: the seed's eight legacy signals, one stopped, one filled on a 1-minute candle and its targets on, one ended by the rule's exit, one expired, one filled and stopped, three a target and on; every reason met: `margin`, `count`, `near`, `stop`, `room` and `top`; a note, a zone, six model signals — four; and twenty-one negative controls on its output. `host`, `copy`, `mark`, `unit`, `first`, `keep` and `stopped` read the host and are exercised there; of the unit's record `mark kill` and `mark rollback` write `check-done` alone, and every mark writes `state.json`. It starts, stops and signals nothing; its `render` runs the service copy's bot. Standard library alone, under `/root/tz04a-env`.

---

## 6. Cost

Measured by the Architect on 2026-11-05 under Python 3.12.3 and 3.13.18 and taken at the population's upper bound.

| check | population | measured | bound |
|---|---|---|---|
| the three self-tests | 57, 135 and 102 checks, no network | `0.13` to `0.19` s, `0.55` to `0.62` s and `0.99` to `1.28` s of wall under 3.12.3, three runs each on the bytes sent; peaks at most `26,218,496`, `39,612,416` and `46,186,496` bytes | `30` s each |
| G-RULE and FINGERPRINT | `git show` of five paths, the bot's syntax trees and its docstring-stripped functions, the map's 60 rows | `0.48` to `0.55` s together, three runs, a worktree's creation and removal among them; peak at most `44,576,768` bytes | `5` s a run |
| G-RENDER | one process: 84 requests of `Data` over six threads, once; two for the marks and the funding intervals at each of seven reports; one for the volume of each coin STRONG at every rank, at most 42, at each of two «сигнал» and two checks, six at a time; the seed's 5-minute candles of each coin from its first card, at most 76 pages of 1,000 at H9's bound; at each of six `ensure` one request of 5-minute candles for each coin with an open signal, at most 42; and a request of 1-minute candles each time a signal is walked from a place inside its first minutes; seven replies and two checks, their parts `1.1` s apart | under 3.12.3 on the bytes sent, Binance stood in for from binary files, eight runs a case: `2.23` to `3.06` s of processor on the host-shaped journal — 23 candle requests, 8,795 candles, 10 registry events — and `2.04` to `2.73` s on the heavier — 257 requests, 36,382 candles, 84 events; peaks at most `48,545,792` and `49,692,672` bytes (§0.4); TZ-40's render on the host took `29.55` s of wall and `3.87` s of processor (map §7 item 146) | `900` s of wall, the `timeout`; `30` s of processor |
| P-START | eight requests to six endpoints, one after another | TZ-40's six requests answered within 3 s on the host (its report, §2.7 and §2.8) | `834` s of wall at worst — six Binance requests at `129` s and two Telegram calls at `30` s — without processor |
| UNIT-NEW and G-FIRST | `systemctl show`, `/proc`, the journal, the log and the registry | under `1` s a run | `30` s; at most 4 and 60 runs |

**Single-session processor at most `630` s at those bounds** — the self-tests `90`, G-RENDER and P-START `30`, at most `90` checker runs at `5` s, `450`, and the `reclaim`, `git` and `systemctl` commands `60` — **under `3,600`, so nothing is sampled.** **Wall clock about 50 minutes:** §0 to §3.3 about 15 minutes; §3.4 and §3.5 about 10, the restart's 30 s, the seed and the replay among them; §3.7 and §9 about 5; the report about 20. **`93` minutes with every `timeout` and every request at its bound** — `10 + 5 + 2 + 5 + 16 + 14 + 16 + 2 + 20 + 3` (§0 with the memory re-read; §3.1; §3.2; §3.3; B-DEPLOY, COPY and G-RENDER at 900 s; P-START at 834 s; the signal, UNIT-NEW and G-FIRST at 945 s; §3.7; the report; §9) — and up to 30 more where a paste waits for the Boss; plus a wait for a band of B-DEPLOY of at most 8 h 10 min, from 23:20:00 to 07:30:00 UTC. **The host pays, after the session:** two checks a day of the unit's own — at 00:10 at most 177 requests to `fapi.binance.com` and at 15:07 at most 93 (§1); a few seconds of processor each; messages of a few parts, each part `1.1` s after the one before; the journal about `14,000` bytes a day in check records and the registry about `400` bytes an event; the unit's process within its `MemoryMax=128M` — the new code's process peaked at most at `46,673,920` bytes through seven commands and two checks under 3.12.3 (§0.4).

---

## 7. Validation

| # | check | count |
|---|---|---|
| **V1** | §0.2's fingerprint | `READING FINGERPRINT: PASS - 69 of 69`: revision `2026-11-01-b`; 6 anchors, 4 re-derived; 60 rows, 57 of 57 `frozen` equal |
| **V2** | §0.3's host gate | `READING HOST: PASS - 23 of 23`; the check records' slots and delays; the journal's size and its STRONG cards' span; the memory figures of the first read and of the second, if one was made |
| **V3** | §0.5's NUMBER, at §0.5 and at §3.1 | `READING NUMBER: PASS - 2 of 2` each, the `TZ-42-` path printed; the branch count `0` |
| **V4** | §0.1's and §3.1's files | 2 of 2 hashes asserted at each, lines and bytes; the branch's diff naming exactly `M`, `A`, and `--numstat` exact |
| **V5** | the self-tests | `57 of 57`, `135 of 135`, `102 of 102` |
| **V6** | G-RULE | `READING RULE: PASS - 8 of 8` |
| **V7** | B-DEPLOY | `exit=0`; the mark printed |
| **V8** | COPY | `READING COPY: PASS - 5 of 5` |
| **V9** | G-RENDER | `READING RENDER: PASS - 34 of 34`; the printed counts; `PEAK` and the seconds |
| **V10** | P-START | `READING P-START: served - 6 of 6 endpoints, 8 requests`, each line printed |
| **V11** | B-KILL and UNIT-NEW | `exit=0`; the mark with `check-done` before and after; `READING UNIT-NEW: PASS - 9 of 9`, both pids, both instants |
| **V12** | G-FIRST | `READING FIRST: PASS - 10 of 10`; the printed counts |
| **V13** | contract §4.2's self-check | run after the push and the pull request and before the report's commit |
| **V14** | §3.7's closing reads | every read printed |
| **V15** | B-RECLAIM-SCRATCH and §9's `keep` | files considered, copied and held; the store's count after equal to before plus the copies |
| **V16** | §9's removals | `git worktree remove` without `--force` exit `0`; `test -e` exit `1` for `/root/tz42-work` and each directory removed; `git worktree list` naming `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else |
| **V17** | every block refused and every paste the Boss ran | its refusal's text, the paste, when he ran it and every log line it appended |
| **V18** | a rollback, where one ran | B-ROLLBACK's `exit=0` and its own read; where signalled, B-KILL2's `exit=0`, `READING UNIT-OLD: PASS - 10 of 10` — or K-42 and `READING STOPPED: PASS - 2 of 2` — and B-ASIDE's `exit=0` with the record's listing and the files set aside, by name and SHA-256 |

---

## 8. The report

`CryptoReports/TZ-42-advisor-registry-report.md`, in contract §8's order. **In its first ten lines:** NUMBER at both reads; G-RULE; the three self-tests; B-DEPLOY, COPY, G-RENDER — with the registry's events and signals, the candle requests, each check's flags, and the render's peak — and P-START; B-KILL with `check-done` before and after, UNIT-NEW and G-FIRST with the pids, the replayed check's flags and the registry the unit seeded, in events and signals; whether a rollback ran; whether the unit runs, and how that was verified; every block refused and who ran it. Beyond what V1 to V18 print: every mark's instant; the unit's journal lines and the `service.log` lines since the first mark; each memory and free-space read with its instant and bound; the commit and the pull request; §9's counts and removals; and every file the run wrote, by SHA-256, but the bot's own root and the render's scratch. **It never prints the token, the chat id, the content of any file under `/etc/adv3-bot/`, a line of the registry, or a coin, a price or a size from the live replies, a journal or a registry** (§2 item 8); `check-done`'s slot is printed. The report is drafted in the primary checkout `/root/btc-5m-twap` before B-RECLAIM-OWN and committed after it.

---

## 9. Reclaim — the host left clean (CANON hard rule 15)

**What a file is kept for:** `I keep` copies every file under `logs/`, `state.json`, `bot.before`, `commit.before` and every file B-ASIDE set aside, `*.rolled`, into `/root/btc-forensics/` as `tz42-work--<path with - for />`, by exclusive create, and verifies each hash; a name already there with the same hash is counted as held, and with another a failed assert. The branch worktree is not copied: `keep` asserts that `git status --porcelain --ignored` in it prints nothing and that its `HEAD` is its upstream's, so `git worktree remove` needs no `--force`. **No output of `keep` or `reclaim` is filtered**: every line it prints is quoted. B-RECLAIM-SCRATCH is §3.3. `render-state/` is scratch — a copy of the bot's journal and the registry the render seeded from it, coins and prices among them — never kept, and goes with the tree.

**B-RECLAIM-OWN**, last, after §3.7 and with the report drafted. **Its output is written to no file; the report quotes it verbatim from the session**, every line of it:

```
nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz42-work/stage/research/tz42-advisor-registry.py keep
git -C /root/btc-5m-twap worktree remove /root/tz42-work/wt; echo "exit=$?"
rm -rf /root/tz42-work; echo "exit=$?"
test -e /root/tz42-work; echo "exit=$?"
git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
find /root/btc-forensics -type f | wc -l
df -B1 --output=source,size,avail /var/lib/btc-recorder
```

The branch `tz-42-advisor-registry` stays on `origin` and as a local ref; only its working tree goes. **Kept:** `/root/adv3-bot-svc/` is the running unit's code, `/var/lib/adv3-bot/` its record — `check-done`, the journal and the registry among it — and `/etc/adv3-bot/` the Boss's token and the pinned chat; the capture roots, both archives' state and the forensic store are data, never scratch. **A refused `rm -rf` is handed to the Boss** by §3.3's route, one tree per command, and verified by `test -e`.

---

## 10. Pre-send checks

Performed by the Architect on 2026-11-05 against this file as sent, in a reading separate from its writing — the body was written, read start to end and corrected where it read wrongly (the corrections are named in C7), and this section written after — with the repository at `origin/main` `0ec452e407488548de2b2c8aff320f73bab42d91` (TZ-41's upload over PR #40's merge `494f10f` and map revision `2026-11-01-b`, `a1c7ba1`; fetched again before sending: no `TZ-42-` file, no report of that number and no `tz-42` branch), the map at that commit (2,033 lines, 536,884 bytes, SHA-256 `1396fa805e9eb72cc36f449c60698822f8d4c2e5314fdd6856f030e07fc46472`) and CANON revision `2026-11-01-b`. Line numbers are those of the files §0.1 extracts for Appendix A, and those of `main` for committed code.

| # | check | result |
|---|---|---|
| **C1** | scope against body | **Repository paths the body names:** `CryptoTZ/TZ-42-advisor-registry.md`, read by §0.1's script and named by `number`; `CryptoTZ/` and `CryptoReports/`, listed by `number`, every `CryptoReports/*.md` read by TZ-35's `reclaim` for hash tokens; `CryptoReports/TZ-41-l0-our-quote-report.md`, named by `git ls-tree` in `host` and the marks (`tz41_reported`); `SYSTEM-MAP.md` and the other 59 rows of its table, read by `fingerprint`, among them `BTC-EXECUTOR-INSTRUCTIONS.md` (cited for contract §1, §4.1, §4.2 and §8), `research/tz33-reward-book-capture.py` (cited for line 190), `research/tz35-advisor-deploy.py` (run for `scratch` and `reclaim`) and `research/twap-divergence.py`, `research/recorder/recorder.py` and `research/pfair.py` (hashed for the anchors); `advisor/adv3-bot.py`, written on the branch and copied to the service; `research/tz42-advisor-registry.py`, written on the branch; `advisor/adv3.py`, `advisor/selftest-adv3.py`, `advisor/RULE-ADV-3.txt` and `deploy/systemd/adv3-bot.service`, read and hashed by `rule`, the first two run from the worktree by §3.2, never written; `CryptoTZ/TZ-40-strong-every-rank.md`, `CryptoReports/TZ-40-strong-every-rank-report.md` and `CryptoTZ/TZ-41-l0-our-quote.md`, cited (§0.4, §1, §6, the When) and read by no command; `CryptoReports/TZ-42-advisor-registry-report.md`, written to `main`. **Host paths:** `/root/tz42-work/**` written (`render-state/` among it, scratch); `/root/adv3-bot-svc/adv3-bot.py` and `commit.txt` written, `adv3-bot.py.new` transient, `adv3.py` read and hashed; `/var/lib/adv3-bot/check-done` written by the `kill` and `rollback` marks through `check-done.tz42`, one rename each (`put_done`, line 1163); `/var/lib/adv3-bot/{registry.jsonl,registry-state.json,registry-state.json.tmp}` moved by B-ASIDE where §4.4 says, and the first two read by `first` and tested by `host` and the marks; `/var/lib/adv3-bot/{journal.jsonl,offset,daily-sent,service.log}` read and hashed, `journal.jsonl` copied into `render-state/`; `/etc/adv3-bot/token` read by the bot's own `--probe`, P-START's, and by nothing of this checker's; `/etc/systemd/system/adv3-bot.service` hashed; `/var/lib/btc-recorder` read by `find`, `grep -c` and `df`; the other capture stores by `du`; `/root/tz41-work` tested for existence by `host` and the marks; `/root/btc-forensics` written by `keep` and `reclaim`; `/proc/meminfo`, `/proc/stat` and the processes' `cmdline` and `stat` read by `host` and `unit`; the UUID directories of `/tmp` read, copied from and removed by TZ-35's checker. **Entry points:** this checker's modes `fingerprint`, `host`, `number`, `rule`, `selftest`, `mark` (`deploy`, `kill`, `rollback`, `kill2`), `copy`, `render`, `unit` (`new`, `old`), `first`, `keep` and `stopped`; TZ-35's `scratch` and `reclaim`; `selftest-adv3.py`; `adv3-bot.py --selftest` and `--probe`; `git` (`fetch`, `ls-remote`, `log`, `ls-tree`, `worktree`, `add`, `diff --cached`, `commit`, `push`, `show`, `rev-parse`, `status`), `gh`'s credential helper; `systemctl` (`show`, `list-timers`, `is-enabled`, `kill`, and `disable` at K-42 only); `journalctl` (the unit's lines, §3.7); `cp`, `mv`, `sha256sum`, `cmp`, `timeout`, `nice`, `rm -rf`, `test -e`, `mkdir`, `du`, `df`, `free`, `find`, `grep`, `wc`, `ls`, `cat`, `tail`, `date`, `uptime`, `nproc`, `sleep`, `seq`. **Outputs:** under `/root/tz42-work/` `logs/`, `stage/`, `wt/`, `render-state/`, `state.json`, `bot.before`, `commit.before` and, where B-ASIDE ran, `*.rolled`; the service copy's two files; `check-done`'s slot; the forensic store's copies; the branch, its pull request and the report. **Intersections with §2, by path and by content class, eleven, each named in §2:** the bot's `--probe` reads the token — item 3's exemption; G-RENDER's and P-START's requests — item 3; `systemctl list-timers`, `is-enabled`, `show`, `kill` and `disable` — item 4; `find`, `grep -c`, `df` and `du` on the capture stores and `systemctl show` of their units — item 5, reads; the test of `/root/tz41-work` — item 5's exemption, existence alone; the marks' write of `check-done` — item 6's exemption, a slot and nothing else; B-ASIDE's move — item 6's exemption, after a rollback restored TZ-40's code; `tail` of `service.log`, `journalctl` of the unit, `cat` of `state.json` and `check-done` and `ls` of the record — item 8's content class: they carry log lines, pids, instants, sizes, slots and counts, `service.log`'s lines a close, a slot, a kind of request, counts and the registry's head, and a coin only where Binance failed to serve it, never a price, a size or a card (§3.7), and none of them is a live reply, a journal or a registry; **`render-state/journal.jsonl`, `registry.jsonl` and `registry-state.json`** — item 8's content class, the coins and prices of cards and signals: scratch files of the work tree, never printed, never copied by `keep` (`kept_files`, lines 1536 to 1542, copies `state.json`, `bot.before`, `commit.before`, the work tree's `*.rolled` and `logs/` alone) and removed with the tree by §9; **`/var/lib/adv3-bot/journal.jsonl` and the unit's registry**, the same class — read by `host`, `mark`, `unit` and `first` and copied by `render`, each printing counts, slots, labels and the first 12 hex characters of a hash alone (`mode_host` 1082 to 1101, `mode_mark` 1203 to 1207, `render_print` 1332 to 1353, `mode_first` 1526 to 1533); **the `*.rolled` files**, the same class — kept in the forensic store by hash and never printed; the live replies — item 8: held in memory by the stand-in, never printed. **Classes checked and intersecting nothing:** labels and settled documents — this TZ reads none, and the registry's results are the model's walk on Binance's candles, which no gate scores against a label; `crypto-auto` and the host's other services — no command names them. |
| **C2** | origin of every expectation | **Quoted from a committed artifact, at `0ec452e`:** revision `2026-11-01-b`, the six anchors, `60`, `57`, `2` and `1` — map §0, its table counted independently of `fingerprint` by the Architect's own parse and each frozen row compared with its blob, then by `fingerprint` against the clone, `PASS - 69 of 69`; `2,370`, TZ-40's two directories and `238335b9…` — map §3, line 1341; the hashes `81ef0112…`, `9e622daf…`, `6f29b82f…`, `ee206e7c…` and `82acd8e4…` — map §0's table, lines 169 to 173, and `sha256sum` of the files at `0ec452e`; `65,425,408`, `29.55` s and `3.87` s — TZ-40's report, line 215, and map §7 item 146 (line 1759); TZ-40's `10,310,459,392` bytes free — its report, line 132; its P-START within 3 s — its report §2.7 and §2.8, `18:05:53.735` and `18:05:56.810`; `7,300,000,000` — `research/tz33-reward-book-capture.py` line 190, `STREAM_FLOOR = 7300000000`, and map §2.6; `31612203008` and `e3975b5…` — map §6's host identity (line 1709); `2026-11-01 signal`, TZ-39's first and TZ-40's replay at 18:06 — map §2.7, lines 1071 and 1072, and TZ-40's report, line 377; TZ-41's band from 2026-11-08 07:30:00 UTC, epoch `1794123000`, its H5 and G-STILL — `CryptoTZ/TZ-41-l0-our-quote.md`, its **When**, lines 138 and 519; `0.5`, `1.0` and `10,000` — `adv3.RISK`, `RISK_MAX` and `DEPOSIT`, line 26 of `main`'s `adv3.py`, `5.0` `RISK_ALL` there; `3` and `1.0` — `TOP_N` and `STRONG_Z`, line 23; `0.001` and `0.0001` — `COST` and `BASE_F`, line 22; the rung `1` — `RELIABILITY`, line 41; `00:10` and `12:10` — `SLOTS` of `main`'s bot, line 26; `3.0`, TZ-37's `Z_CAP` — line 33 of `main`'s bot; `30` s, `3 4` and `128M` — the unit, lines 15, 16 and 18; the old wording «Сделки по карточкам бота — бот не видит ваш счёт» — `main`'s bot line 861; 2026-09-27's 35 of 42 STRONG, every one LONG — TZ-40 §1; `04:10` — CANON PART VII; the Boss's `200,000` USDT, `0.5` %, `10` %, `14` %, 1,000–7,000 and 8,000 USDT, 16:10 and 19:07 in Batumi, 15:07 UTC and every sentence quoted — his file of 2026-11-05. **Computed by an implementation independent of the one under test:** `150,369,520` = 2 × `75,184,760`; `75,184,760` = ⌈`49,762,304` × `65,425,408` / `43,302,912`⌉ [modelled], in exact rationals; the render's peaks — `resource.getrusage` of a process running the checker's `render_run` and `render_checks` on the stage's bot, Binance stood in for by its candles read record by record from binary files, eight runs a case under Python 3.12.3 and eight under 3.13.18, two journals, on the bytes sent, and `49,762,304` in a run before the bot's last edit, and the same method on TZ-40's bot and checker as `main` holds them, eight runs under each; `58,740,736` at 437.5 coin-days, four runs; the bot process's `46,673,920` — a process running the bot alone through seven commands and two checks, three runs a journal; the spans `20.4`, `120.8` and `437.5` coin-days — `coin_days`, the very reading H9 applies, so the bound and the measurement are one quantity; the margin's `1.55` to `2.27` — `1 / (lev · (d + 0.002))` with the rule's leverage, scanned from 2 % to 14 % in steps of 0.001 %; the self-tests' and G-RULE's walls and peaks — a parent's `RUSAGE_CHILDREN`, three runs each; the numstats `1903 1224` and `2088 0` — `git diff --numstat` against `0ec452e` over the files §0.1's script writes into a worktree of the clone; §0.1's table — `wc` and `sha256sum` of the two files, equal to the script's own lines over an empty stage and over that worktree; `6,778` to `7,066` bytes a check record, about `400` bytes an event and `682` a line — the records and registries those runs wrote; TZ-40's bot on journals the new bot wrote — a process running TZ-40's `handle` for «сигнал», «сигнал топ 7», «сигнал 10000 топ 3», «оценка» and «помощь» and its `check` for both slots on each, every log line read for a failure; the request counts `177`, `93` and `76` — C4's arithmetic over the bot's request functions. **Fixed by Appendix A's code, which this TZ measures nothing to set:** `69`, `23`, `2`, `8`, `5`, `34`, `9`, `10`, `10` and `2` (FINGERPRINT, HOST, NUMBER, RULE, COPY, RENDER, UNIT-NEW, FIRST, UNIT-OLD, STOPPED), `57`, `135` and `102` (the self-tests), `6` endpoints and `8` requests, the `7` commands and `7` record kinds of the render, and G-RULE's `16` changed, `57` added, `23` removed and `23` identical definitions and `4` changed, `21` added and `3` removed assignments — each the count its function's dictionary or tuple holds, re-run by the Architect where it runs off the host (C5). **Fixed by this TZ and measured by nothing:** the bands, the 45 s wait, the 15 s polls, UNIT-NEW's 90 s and 100 s, G-FIRST's 900 s and the `timeout`'s, the 60 s memory re-read, the session's `100,000,000` bytes, the edge at 07:00:00 UTC — half an hour before TZ-41's band — and H9's `120` coin-days, the largest span measured below the next — the Architect's choices, named so. **The floors and the bands:** `7,400,000,000` = `7,300,000,000` + `100,000,000`; `27,000` = 7 × 3,600 + 30 × 60, `40,800` = 11 × 3,600 + 20 × 60, `42,600` = 11 × 3,600 + 50 × 60, `44,400` = 12 × 3,600 + 20 × 60, `51,600` = 14 × 3,600 + 20 × 60, `53,400` = 14 × 3,600 + 50 × 60, `55,200` = 15 × 3,600 + 20 × 60, `84,000` = 23 × 3,600 + 20 × 60, `85,800` = 23 × 3,600 + 50 × 60; `1794121200` = `1794123000` − 1,800; `834` = 6 × `129` + 2 × `30`, `129` = 4 × 30 + 1 + 3 + 5. **No expectation depends on a quantity this TZ measures but as an inequality or an equation that holds for every admissible value of it:** UNIT-NEW reads `NRestarts` as the `kill` mark's plus one and the capture units' as the mark's, whatever the mark read; the memory, disk and span gates are inequalities on a read; G-RENDER's limits are inequalities, and its equations are between the registry, positions, replies and records the bot made and the chain, seed, walk, arithmetic and order the checker recomputes from the same journal, reports, candles and volumes; G-FIRST reads `check-done` against the mark's instant — `signal` before 15:07 UTC, `fact` after — which holds for every mark the bands admit (§4.3), and the seed against the journal's own bytes before the check's record; H7 reads slots against their instants and `check-done` against the last; the numbers of signals, events, requests and coins are printed, never asserted. |
| **C3** | shape of every diff | Two paths, read from `git diff -U0 0ec452e` over the extraction. **`advisor/adv3-bot.py` replaces 1,224 committed lines in 75 hunks:** 3–8; 12; 23–26; 32–37; 40–52; 120; 123; 125; 130; 166–177; 181–185; 192–202; 285–325; 343–363; 365–394; 396–471; 474–484; 486–519; 555; 565; 584–587; 604–606; 608–609; 612; 620–654; 657–668; 671–709; 712–723; 726–728; 731–748; 751–766; 769–784; 787; 789–822; 826–849; 853–854; 856–858; 860–868; 871–872; 876; 879–883; 887–892; 895–898; 900–913; 915–924; 926–951; 953; 957–960; 964–982; 984; 998; 1009; 1020–1021; 1039; 1044; 1047–1069; 1074; 1080–1082; 1087–1089; 1101–1104; 1138; 1144–1147; 1155–1175; 1177–1181; 1216–1217; 1273; 1277–1278; 1280–1283; 1285–1290; 1296; 1301–1771; 1775; 1777–1781; 1783–1812; 1814–1839 — the header's comment, `SLOTS` and its comment, `TOPN`, TZ-40's constants, `HELP`, `Telegram`, `route`, the removed definitions of §4.1, `CARD_KEYS`, `base_record`, `candidates`, `event_lines`, `zone_lines`, `compose`, `check_record`, `check`, `serve`'s start, `handle`, `probe`, `hello` and `selftest`; `due`'s and `done_after`'s docstrings — `--numstat` `1903 1224`, the three lines beyond the replaced ones `klines`' bound and docstring and one self-test check. **`research/tz42-advisor-registry.py` is new:** `git cat-file -e 0ec452e:research/tz42-advisor-registry.py` exits `128`, as do the report's path and this TZ's own; `2088 0`. No sentence of this TZ calls a change additive or speaks of insertions only. |
| **C4** | cost of every check | §6, at the population's upper bound. **Processor, single session, term by term:** the three self-tests `3 × 30 = 90` s against `0.19`, `0.62` and `1.28` s measured at most; G-RENDER and P-START `30` s against `3.06` s at most measured for G-RENDER's seven replies and two checks; at most `90` checker runs at `5` s, `450` s — HOST 1, FINGERPRINT 1, NUMBER 2, RULE 1, the marks up to 4, COPY 1, UNIT-NEW up to 5, G-FIRST up to 61, UNIT-OLD up to 5, KEEP 1 and STOPPED up to 2, `84` at most, each under `1` s measured, RULE and FINGERPRINT `0.55` s together at most; and the `reclaim`, `git` and `systemctl` commands `60` s: **`90 + 30 + 450 + 60 = 630` s, under `3,600`; nothing is sampled.** **The fail-fast bounds, each with its derivation:** `adv3.get`'s four tries — four `30` s timeouts and the `1`, `3` and `5` s between them, `129` s, `adv3.py` lines 69 to 87 — make a render with Binance silent worst at `14 × 129 = 1,806` s for `Data`'s 84 requests over six threads (`Data.fresh`, line 269, `ThreadPoolExecutor(6)` at 285), `14 × 129 = 1,806` s for the marks and funding intervals of seven reports one after another (`live_report`, 301), `4 × 7 × 129 = 3,612` s for the volumes of at most 42 STRONG coins at two «сигнал» and two checks, six at a time (`volumes`, 352), `76 × 129 = 9,804` s for the seed's pages at H9's bound (`klines`, 557, one coin after another in `seed`, 709) and `6 × 42 × 129 = 32,508` s for six `ensure`'s 5-minute requests (`reconcile`, 678), so G-RENDER runs under `timeout 900`; its stand-in's pauses at most `9 × 9 × 1.1 = 89.1` s, nine messages of ten parts — the replies measured on the host-shaped journal were one part each; P-START's eight requests one after another, `6 × 129 + 2 × 30 = 834` s of wall (`Telegram.call`, line 139, has one try of `30` s), `probe`, lines 1736 to 1769; UNIT-NEW's `NOT YET` at most 100 s after the mark, every 15 s, at most 4 runs in a paste; G-FIRST's at most `900` s after the mark, every 15 s, at most 60. **Wall clock:** about 50 minutes; `93` with every bound reached — `10 + 5 + 2 + 5 + 16 + 14 + 16 + 2 + 20 + 3` — up to 30 more where a paste waits for the Boss, and a wait for a band of B-DEPLOY of at most 8 h 10 min; at the bounds B-DEPLOY at 11:20:00 UTC reaches B-KILL by 11:49, at 14:20:00 by 14:49 and at 23:20:00 by 23:49, each inside its band. Disk at the same bound: §0.4's `100,000,000`, the logs under `2,000,000` bytes. **After the session:** at 00:10 `84 + 2 + 42 + 42 + 7 = 177` requests at most and at 15:07 `2 + 42 + 42 + 7 = 93`, the candles held (`Data.fresh` refetches only for a newer close), each under the same `get`; a «сигнал» at most `93` more; a message of eight parts at least `7 × 1.1 = 7.7` s of pauses and, with every part refused twice at the longest wait, at most `7.7 + 8 × 2 × 61 = 983.7` s, the unit answering no command meanwhile. |
| **C5** | every count | `69` = 1 revision + 6 anchors + 4 re-derived + 57 frozen rows + 1 table shape, `parse_map` and `mode_fingerprint` (lines 171 and 1022), the table counted again by the Architect's parse — `60` rows, `57` frozen, `2` tracked, `1` reported — and `PASS - 69 of 69` on the clone. `23`, `mode_host` lines 1047 to 1102: H1 one, H2 two, H3 one, H4 three, H5 six, H6 one, H7 three (`clock_checks`, 937), H8 three — one and `window_reading`'s two (1008) — H9 one, the memory gate and the disk gate; **`23 of 23` on a stand-in host** — systemd, `/proc`, `df` and the host's files stood in for, a journal in the host's shape with TZ-40's replay among its check records — and `22 of 23`, the one named, after the edge, beside TZ-41's work tree, with a registry and with a slot twice. `2`, `number_reading` (1002): `PASS` on stand-ins with the one file, `FAIL` with a second `TZ-42-` file and with a report, and `FAIL - 1 of 2` on the clone at `0ec452e`, which holds no `TZ-42-` file. `2` files and `2` hashes, §0.1. `8` = `mode_rule` (1128 to 1147): three file checks, three of `tree_checks` (198), one of `strip_docs` (215) for `due` and `done_after`, one hash — `8 of 8` on a worktree of the clone holding the two files. `57`, `main`'s `selftest-adv3.py` unchanged; `135` = 49 + 2 + 12 + 8 + 9 + 16 + 2 + 6 + 4 + 6 + 2 + 2 + 3 + 7 + 3 + 4, the groups §5 names, each listed by its run; `102` = 77 + 4 + 21 — the pure readings with their negative controls, the synthetic market's four, the twenty-one negative controls on the render's output, each listed by its run; `57 of 57`, `135 of 135` and `102 of 102` on the files §0.1 extracts, under 3.12.3 and 3.13.18. `5`, `mode_copy` (1210). `34` = `render_checks` (1356 to 1441): 2, `registry_checks`' 7 (660), 1, `opens_checks`' 3 (780), `model_checks`' 2 (806), `alloc_checks`' 5 (747), and 14 — `34 of 34` on the stage's bot with the synthetic market and on Binance's candles with both journals, and each of twenty-one faults reading FAIL. `6` endpoints and `8` requests, `probe` (1736 to 1769). `9`, `unit_checks` (837), and `10` with `mode_unit`'s extra check (1488): `9 of 9` on stand-ins for a clean restart and for the rollback's, and eight faults reading FAIL; `10`, `first_checks` (859): `10 of 10` on stand-ins for a restart before 15:07 and one after it, and sixteen faults reading FAIL; `2`, `mode_stopped` (1575). **On the stand-in host the sequence ran end to end:** `host` 23 of 23; `mark deploy`; COPY 5 of 5; G-RENDER 34 of 34 on the host-shaped journal; `mark kill`, `check-done` `2026-11-04 signal` → `2026-11-03 fact`; UNIT-NEW and G-FIRST `NOT YET` before the restart, then the new bot's own replay of `2026-11-04 signal` in the stand-in record, UNIT-NEW 9 of 9 and G-FIRST 10 of 10; `mark rollback` leaving the slot the new process wrote; `mark kill2`; UNIT-OLD 10 of 10; B-ASIDE `exit=0`, two files set aside; `keep` seven files; STOPPED 2 of 2. `7` = `RENDER_CASES`, `7` = `RENDER_KINDS` (lines 79 and 80). G-RULE's lists — `16` changed, `57` added, `23` removed and `23` identical of `main`'s `62` definitions, `4` changed, `21` added and `3` removed of its `20` assignments — the Architect's own AST script, equal to `BOT_DEFS`, `BOT_SAME` and `BOT_ASG` and to §4.1's names. V1 to V18 are §7's eighteen rows. |
| **C6** | every population | NUMBER: the paths under `CryptoTZ/` and `CryptoReports/` of `origin/main` at each of its two reads. FINGERPRINT: the map's table of 60 rows against the files of the primary checkout. HOST: the host at the instant of the read — its units, files, record, memory and disk; H7 the journal's `check` records from the last naming `2026-11-01 signal`; H9 the journal's records at the instant; the memory figure the first read and, if it fell below the floor, the second. RULE: `adv3.py`, `adv3-bot.py`, `selftest-adv3.py`, `RULE-ADV-3.txt` and the unit file of `origin/main` against the branch's files. The self-tests: synthetic candles, markets, journals and stand-ins, no network. COPY: `/root/adv3-bot-svc` and the worktree. RENDER: the service copy's bot answering seven texts and running two checks on the latest close at the run's instant — the 42 coins' daily candles, at most 1,500 each, marks, funding intervals, the volumes of every coin STRONG at any rank, at most 42, at each «сигнал» and check, and every 5- and 1-minute candle the seed and the six `ensure` read — over a copy of the bot's journal; the registry the bot seeded there against the checker's own chain, seed and replay over the same journal and the same candles; each allocation against what it shared risk among and the report it rests on; the order, STRONG and entries the checker computes from the same rows. P-START: one request to each of six endpoints, the klines endpoint three times. UNIT-NEW and UNIT-OLD: the unit, the three capture units and `service.log`'s lines stamped at or after the mark less 1 s. G-FIRST: the journal's records stamped at or after the `kill` mark less 1 s, its bytes before the first check record since then, `check-done`, `service.log`'s lines since the mark, the unit's registry and its state. KEEP: the work tree's files §9 names. RECLAIM: the UUID directories `scratch` names earlier. §0.4's memory figures: one mode's process each; §1's margin ratio: stops from 2 % to 14 %; `MemAvailable` and free space: the host at each read. No statistic of this TZ is a calibration claim and none is read against a label: the registry's figures describe the model's walk and gate nothing. |
| **C7** | every signature and every behaviour | **Committed code this TZ relies on, read at `0ec452e`.** `adv3.py` — `def get(url, tries=4):` line 69, four tries of 30 s (73, 75) with `1 + 2 * k` s between them (86), the `129` s of §6; `def fapi(path, **params):` 160; `def fapi_candles(sym, now_ms):` 164, one request of 1,500 daily candles; `def fapi_funding(sym, first):` 173; `def fapi_intervals():` 188; `def fapi_marks():` 193; `def signal(days, closes, i):` 211, the rule's signal the walk's exit reads; `def strength(days, closes, i):` 220, which `notes_of` reads; `def ranking(day_states):` 312, `top = sorted(active, key=lambda cs: -abs(cs[1][1]))[:TOP_N]` (315) and `strong = [coin for coin, s in top if s[2] == 4 * s[0] and abs(s[1]) >= STRONG_Z]` (316); `def trust(rep):` 387; `def report(cs, funds, marks, deposit, risk, now_ms, missing=(), intervals=None):` 454, `risk = min(risk, RISK_MAX)` (457) and `'marks_ok': bool(marks), 'made_at_ms': now_ms` (495); `def card(coin, row, is_strong, deposit, risk):` 500 — `S = C - k * U` (503), the zone (505), the entry at market, a limit or none (507, 509), `leverage=min(20, math.floor(1 / (1.5 * dist / entry + 0.01)))` (519) — the stop, entry and leverage `position` and `register` take from the card; `def changes(rep):` 558; `def assessment(rep, facts):` 645; the constants lines 22, 23, 26 and 41. `adv3-bot.py` of `main` — `SLOTS` (26); `def put(path, text):` 70; `class Data:` 205, `ThreadPoolExecutor(6)` (229); `def live_report(data, deposit, risk):` 245; `def ranked(rep):` 262; `def strong_all(rep):` 277; `def liquidity(coin, now_ms):` 326; `def volumes(coins, now_ms):` 337; `def due(now, done):` 553 and `def done_after(slot, now):` 564 — from the day before's `fact` the day's signal check is due at any hour, and a signal check ending at or after the fact slot marks the day's fact done; `def journal_records():` 589; `def append(rec):` 615; `def serve():` 987 — `done = slot_parse(read(done_path)) …` (1001) once at its start, `log('serving the pinned chat: pid', …, 'check-done', …)` (1003), `slot = due(now, done)` (1006), `done = done_after(…)` (1014) and `put(done_path, …)` (1016), so the running process never reads `check-done` again; the wording of line 861; `def main():` 1849 — `Data`, `live_report`, `ranked`, `strong_all`, `liquidity`, `volumes`, `due`, `done_after` and `main` identical to Appendix A's by G-RULE. TZ-35's checker `research/tz35-advisor-deploy.py` — `UUID` (54) and `LIVE_S = 60` (56); `def claude_starts():` 157; `def live_or_earlier(birth, starts):` 274; `def reclaimable(tree):` 279; `def mode_scratch(own):` 419; `def mode_reclaim(trees):` 434, printing `RECLAIM PASS` at 486; `def main(argv):` 774. The unit — `WorkingDirectory` line 12, `ExecStart` 13, `Restart=always` 14, `RestartSec=30` 15, `RestartPreventExitStatus=3 4` 16, `MemoryMax=128M` 18, `ProtectSystem=strict` 21 and `ReadWritePaths=/var/lib/adv3-bot` 22, under which the bot writes its registry and the checker `check-done.tz42`. **Every behaviour this TZ attributes to Appendix A** is the body of one function: of the bot `Telegram.call` 139 — a `429` raising `TooMany` with its `retry_after`, `5` where none is named (150, 151) — `send` 155 — `time.sleep(PACE)` before every part but the first (163, 164), the keyboard on the last part (165), three tries with `min(e.retry_after, 60) + 1` between them (166 to 173) — `send_part` 176, `params` 204, `route` 238, `Registry` 416 — `load` 429, a torn tail cut (433 to 438), the chain checked line by line (445 to 448); `append` 472, `n`, `prev` and `at` added (475), the line flushed and synced (479, 480); `save_state` 486; `cursor_of` 493; `live` 502 — `new_signal` 507, `advance` 515, `status_of` 530, `open_risk` 547, `klines` 557 — no request for a start after the moment (562) — `first_window` 576, `walk` 584, `reconcile` 678, `seed` 709 — its event first (754) — `notional_of` 820, `position` 830, `allocate` 853, `candidates` 883, `carded` 912, `model_plan` 928, `view_plan` 948, `register` 976, `ensure` 1002, `compose` 1349, `signal_view` 1404, `stats_lines` 1469, `registry_view` 1517, `ranking_view` 1536, `assess_view` 1563, `check_record` 1571, `check` 1592 — the message sent (1606) before the new signals are written (1609) — `serve` 1617 — the registry loaded (1628), `check-done` read once (1631), the serving and registry lines (1633, 1634), `setMyCommands` with its refusal logged (1637 to 1639) — `handle` 1680 and `probe` 1736; and the checker's readings and modes at the lines C5 names — each sentence of §1 and §4.2 to §4.4 read against them. **Sentences rewritten in this reading:** §1 gave the margin as `1.63` to `2.27` times the loss at the stop, from a few stops by hand — scanned from 2 % to 14 %, `1.55` at a stop of 12.67 % and the rule's 5×; §1's table quoted the old message's wording from memory — read from `main`'s bot, line 861; §0.4's peaks were measured before the last edits — re-measured on the bytes sent, eight runs a case: `48,545,792` and `49,692,672` under 3.12.3, `47,665,152` and `48,951,296` under 3.13.18, the model keeping `49,762,304`, the largest of every run; the bot process's peak was named for one journal — it is either's, `46,673,920`; the self-tests' and G-RULE's times re-measured on the bytes sent; **a reconcile within five minutes of a signal's issue asked Binance for candles opening after the moment**, which it may refuse and the render's first check would then read as a failure — `klines` now asks nothing for a start after the moment, and the bot's self-test checks it; **H7 read the check records from TZ-39's first, and the host's journal repeats that slot at TZ-40's replay of 18:06 UTC** — H7 would have read FAIL on the host; `clock_checks` now reads from the last record naming `2026-11-01 signal`, its self-test with TZ-40's replay among the records; the checker's memory floor was derived before its last edits — re-measured on the bytes sent, `145,400,000` → `150,369,520`, the largest of the final runs, `49,762,304`, above every earlier one; `keep` copied no registry B-ASIDE sets aside, and named `adv3.before`, which B-DEPLOY no longer saves — `kept_files` now keeps every `*.rolled` and no `adv3.before`; §6's wall at the bounds summed to 92 with the report at 19 minutes where the estimate gave 20 — `93`; the views' «реестр» named the figures by a reference — named; G-RENDER's cost counted one 1-minute request a legacy signal — a request each time a signal is walked from inside its first minutes; the What-this-TZ-is omitted PENDING and called the menu the keyboard; the header named map §7 items 136, 139 and 142 and §6's language, process supervision and harness rows that the body did not cite — cited; two table cells carried an unescaped `\|z\|`. Every count and hash of this section is that of the bytes sent. |
| **C8** | every cross-reference | Resolved by reading the text referenced. **Map `2026-11-01-b` at `0ec452e`:** §0's anchors and its table of 60 rows, 57 / 2 / 1; §1's record of refs (a difference from it is recorded, not blocking, §0.5); §2.5 (line 837) and §2.6 (986) for the archives' calendar runs at `03:00:20` and `01:30:20` UTC, and §2.6 for `STREAM_FLOOR`; §2.7 (1055) — the record under `/var/lib/adv3-bot/`, the token and chat under `/etc/adv3-bot/`, K-35, TZ-39's paragraph (1071) and TZ-40's (1072), the replay of `2026-11-01 signal` at 18:06 UTC and the clock's first check under TZ-40's code; §3's `2,370` files, the two worktrees and TZ-40's two directories and the live `238335b9…` (1341); §6's rows host identity (1709), language (1710), git remote (1713), egress (1714) — `fapi.binance.com` answering `451` to the Architect's sessions — disk (1716), host is shared (1730) — `crypto-auto` among the unrelated services — process supervision (1732), memory (1733), both sandbox limits (1736, 1738) and the harness (1739); §7 items 118 (no file of the work tree printed but by a command the TZ names), 124 (a block handed to the Boss: once its band is open, one line, appended under a `date -u` line), 125 and 129 (a reload re-arming an archive's run), 131 (the floor rule), 132 (no step of the Boss's before `EXECUTE`), 136 (`NRestarts` not a lifetime count), 137 (a memory floor read twice), 138 (ONE paste, a refused block handed over unchanged), 139 and 141 (the fingerprint reads every row; the header names the sections this row cites — copied there), 140 (a handed-over block holds back only the steps that read what it changes), 142 (the ladder as `2026-10-31-c` corrected it, which `2026-11-01-b` carries), 143 (bands opening at 07:30 UTC), 144 (no mode run again after a paste), 145 (a mode timed for its host peak carries its own wrapper inside the paste), 146 (G-RENDER's host peak `65,425,408`) and 147 (Binance's archive's hole of 2026-10-28, which this TZ's reads of `fapi.binance.com` do not meet). **CANON `2026-11-01-b`:** PART III — the Boss decides objectives and capital; PART VII — the frozen rule and its STRONG of the TOP-3, the records re-derived from Binance's archive and never from the bot's journal, the evidence ladder at rung 1, the sizes the Boss's — 0.5 % a trade, 1 % at most, 5 % in all, which his specification now sets to 10 % for the bot's model — the 14 % stop, the checks at 04:10 Batumi, ADV-4 for any change of the rule's parameters and «Уверенность: N/5»; hard rules 2 (NUMBER), 12 and 13 (this section), 14 (P-START, every header, the unit, its restart policy and stop, the bands in the blocks' text, ONE paste) and 15 (§9). **Quotations, compared character for character with his file of 2026-11-05:** "THEREFORE, YOU ARE RESPONSIBLE, AND THE FINAL DECISION IS YOURS!", "Maintain a persistent internal registry …", "Move the existing reconciliation scheduled for 16:10 Batumi time to **19:07 Batumi time (15:07 UTC)**. Preserve the second daily reconciliation schedule.", "Current confidence remains **1/5 until supported by validated evidence**.", "Track repeated recommendations independently when their entries or risk parameters differ", "Prevent duplicate records during repeated analyses.", "Do not increase confidence based solely on signal volume", "Never increase leverage or risk artificially to meet the minimum position size.", "Allocate more personal margin to the strongest, highest-conviction candidate and progressively less to lower-ranked candidates", "Never discard previous signal history when issuing a new recommendation" and "Determine outcomes from available chronological market data and existing strategy rules. Never assume actual order execution." — each a substring of it, his bold markers kept; his title «ADV-3 — Required System Changes» and his `crypto-auto` likewise. **Contract:** §1 steps 1 to 4 (§0.0, `fingerprint`), §4.1 (the order of the branch and the report), §4.2 (V13) and §8 (the report's order). **Other artifacts:** `CryptoTZ/TZ-40-strong-every-rank.md`, whose §0.1 script, bands, marks, B-DEPLOY, B-KILL, gates and §0.4 floor rule this TZ adapts, and its §1 for 2026-09-27; its report (lines 132, 215 and 377, §2.7 and §2.8); `CryptoTZ/TZ-41-l0-our-quote.md` — its **When**, H5 and G-STILL; TZ-37 §0.4's floor rule; TZ-38's report for `238335b9…`; TZ-35's checker's `scratch` and `reclaim`. **This TZ:** §0.1 to §0.5, §1, §2's items, §3.1 to §3.7, §4.1 to §4.5, §5, §6 and §9, each supporting the sentence that cites it. **None unresolved.** |

**Eight checks could not be performed from this session**, and each is converted into a mechanical condition the Executor evaluates and BLOCKS on, or rolls back on (CANON hard rule 13): the host's own state — free space, memory, units, interpreter, the service copy's and the unit file's hashes, the record, the clock's firing under TZ-40's code and the journal's span — `I host`, §0.3, `23 of 23` on the stand-in host and the host's own read on the host; TZ-41's window on the host — H8 and the `deploy` and `kill` marks; the live reach of `fapi.binance.com` and `api.telegram.org` under the service's headers — `fapi.binance.com` answers `451` to this session's container (map §6, egress) — P-START and G-RENDER, before anything is signalled; a live day with a new STRONG signal to take, which depends on the market — G-RENDER reads the registry, the plans and the allocations against the checker's own whenever the day holds one, and a disagreement is B-ROLLBACK; when it holds none it reads 34 of 34 with the legacy signals alone, and the new views rest on the self-test's synthetic market and the Architect's render on Binance's own candles (C5); systemd's restart of the unit after a `SIGTERM`, the new process's replay of the day's signal check, its seed from the unit's own journal and its message to the Boss's chat — UNIT-NEW and G-FIRST; Telegram's acceptance of the command menu, which nothing here provokes but the unit's start — logged, and quoted by the report (§4.5); the harness's permission classifier — each refused block handed over unchanged with its paste (§3.6); and the 00:10 and 15:07 checks under this code on their own clock — the next TZ's host gate reads them (H7).

---

## Appendix A — the two files, byte for byte

Extracted by §0.1's script; each block's content is its file.

```text file=advisor/adv3-bot.py
#!/usr/bin/env python3
# adv3-bot.py - ADV-3's Telegram side (CANON PART VII): the Boss's commands; two checks a day by the unit's own scheduler, at
# 00:10 UTC (04:10 in Batumi) the close's signals and at 15:07 UTC (19:07) the facts of the moment, each loud only for an alert and
# one quiet line where it finds nothing; and, since TZ-42, the registry of every STRONG signal the bot published - registry.jsonl,
# append-only and hash-chained - each signal walked forward on Binance's 1- and 5-minute candles to its fill, its targets and its end
# by the rule's own exit; beside the journal of every check's state and every message sent. Standard library only; adv3.py beside it.
# TZ-42, the Boss's specification of 2026-11-05: the model's defaults - a calculation base of 200,000 USDT, never his balance; 0.5 %
# a trade at its stop, 1 % at most; 10 % for every open signal together; a stop within 14 % of the entry - a request's overrides
# narrowing them for that request alone; the risk shared by the strength of the trend, the strongest the most; the leverage the rule's
# ceiling, lowered only to keep the margin at 0.5 % of the capital or more, never raised; STRONG at every rank, at most 7 new signals
# a close; a reply keyboard. The frozen rule's STRONG, its strategy and its records stay the TOP-3's: the registry measures nothing.
# Modes: --serve (the unit's), --probe, --find-chat, --hello, --selftest.
# Exits: 0 or SIGTERM, restarted by systemd; 3 without a token or a chat id and 4 where glibc refuses its two
# settings, neither restarted; 1, an unexpected exception, restarted.
import argparse, ctypes, datetime as dt, hashlib, html, json, math, os, re, sys, time, traceback, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import adv3  # noqa: E402

TOKEN_FILE = '/etc/adv3-bot/token'
CHAT_FILE = '/etc/adv3-bot/chat-id'
STATE = '/var/lib/adv3-bot'
TG = 'https://api.telegram.org/bot{token}/{method}'
UA = 'adv3-bot/1'
# The two checks a day (TZ-39; the second at 15:07 UTC, 19:07 in Batumi, since TZ-42 - the Boss's of 2026-11-05). The rule changes
# state only at a daily close: the check of 00:10 UTC reads the close's signals, ten minutes after it - the margin kept for the day's
# last funding settlement; the check of 15:07 reads facts alone and never a signal of a half-formed candle.
SLOTS = (('signal', dt.time(0, 10)), ('fact', dt.time(15, 7)))
BATUMI = dt.timedelta(hours=4)
POLL, RETRY, LIMIT = 50, 300, 4000
OPEN = ('сигнал', 'сигналы', 'signal', 'signals', 'топ', 'top', 'стратегия', 'стратегию', 'strategy')
ASSESS = ('оценка', 'оценки', 'оценку', 'rating')
REGISTRY = ('реестр', 'registry')
RANKING = ('рейтинг', 'ranking')
HELPS = ('помощь', 'help', 'start', 'команды', 'меню', 'menu')
HEAD = re.compile(r'^\s*/?([^\W\d_]+)')
TOPN = re.compile(r'(?<![^\W\d_])(?:топ|top)[\s\-\u2013]*(\d{1,2})(?!\d)', re.I)   # «стоп 12» holds no «топ»
NUMBER = r'(\d+(?:[.,]\d+)?)'
KEYWORDS = (('risk', re.compile(r'(?<![^\W\d_])(?:риск|risk)\s*[:=]?\s*' + NUMBER, re.I)),
            ('total', re.compile(r'(?<![^\W\d_])(?:лимит|limit|всего|total)\s*[:=]?\s*' + NUMBER, re.I)),
            ('stop', re.compile(r'(?<![^\W\d_])(?:стоп|stop)\s*[:=]?\s*' + NUMBER, re.I)))
# The model's defaults, the Boss's of 2026-11-05 (CANON PART VII): the capital - a calculation base, never his balance or his margin;
# the risk of all open signals together, in percent of it; the stop's farthest distance from the entry, in percent; the new signals one
# close may hold. The risk of one trade is adv3.RISK, at most adv3.RISK_MAX. The margin's floor, its ceiling and its exceptional
# ceiling, in percent of the capital: 1,000, 7,000 and 8,000 USDT at 200,000.
CAPITAL, RISK_TOTAL, STOP_MAX, NEW_MAX = 200000.0, 10.0, 14.0, 7
MARGIN_MIN, MARGIN_MAX, MARGIN_EXC = 0.5, 3.5, 4.0
# The share of a coin's mean daily quote volume of LIQ_DAYS days a position may take - TZ-37's 0.1 %, 0.5 % since TZ-42 at the
# capital of 200,000 USDT - and the strength's cap in the risk shares.
LIQ_FRAC, Z_CAP, LIQ_DAYS = 0.005, 3.0, 7
RANK_LIST, RANK_MAX = 7, 42   # «рейтинг»: the rule's first 7 coins by default, all 42 at most
# The candles a signal is walked on, their length in ms: its first minutes - from its issue to the next 5-minute boundary - on 1-minute
# candles, then 5-minute ones; a page of fapi's klines.
K1_MS, K5_MS, K5_PAGE = 60_000, 300_000, 1000
INTERVAL = {K1_MS: '1m', K5_MS: '5m'}
DAY_MS = 86_400_000
PACE = 1.1     # seconds between the parts of one message: Telegram asks for at most one message a second in a chat (TZ-40)
REG_FILE, REG_STATE, GENESIS = 'registry.jsonl', 'registry-state.json', '0' * 64
SIDE, DOT = {1: 'LONG', -1: 'SHORT'}, {1: '🟢', -1: '🔴'}
# A legacy signal's open event: the fields the seed writes, in the shape register writes a model signal's.
LEGACY_KEYS = ('utc', 'coin', 'side', 'close_of', 'source', 'mode', 'entry', 'stop', 'targets', 'close', 'U', 'z', 'sum', 'rank', 'since',
               'btc', 'breadth', 'valid', 'capital', 'risk_pct', 'loss', 'notional', 'qty', 'leverage', 'margin', 'legacy')
# The Boss's statuses (his specification of 2026-11-05, §3) and their Russian labels; PENDING is a limit not yet filled.
LABEL = {'PENDING': 'ждёт входа', 'ACTIVE': 'активен', 'TARGET 1 REACHED': 'цель 1', 'TARGET 2 REACHED': 'цель 2',
         'TARGET 3 REACHED': 'цель 3', 'PARTIAL TARGET COMPLETION': 'цели частично', 'STOPPED OUT': 'стоп',
         'INVALIDATED': 'инвалидация', 'EXPIRED': 'истёк'}
CARD_KEYS = ('coin', 'side', 'strong', 'mode', 'entry', 'stop', 'targets', 'close', 'U', 'since', 'z', 'sum', 'mark')
KEYBOARD = {'keyboard': [[{'text': 'Сигнал'}, {'text': 'Реестр'}], [{'text': 'Рейтинг'}, {'text': 'Оценка'}, {'text': 'Помощь'}]],
            'resize_keyboard': True, 'is_persistent': True}
COMMANDS = [{'command': 'signal', 'description': 'STRONG-сигналы, позиции и риск модели'},
            {'command': 'registry', 'description': 'Реестр STRONG-сигналов и итоги'},
            {'command': 'ranking', 'description': 'Рейтинг правила по 42 монетам'},
            {'command': 'rating', 'description': 'Уверенность и статистика реестра'},
            {'command': 'help', 'description': 'Команды и параметры'}]
DEFAULTS = {'capital': CAPITAL, 'risk': adv3.RISK, 'total': RISK_TOTAL, 'stop': STOP_MAX, 'n': NEW_MAX, 'set': []}
HELP = ('<b>ADV-3 · STRONG-сигналы Binance Futures</b>\n'
        '«Сигнал» — STRONG этого закрытия с позициями, открытые сигналы, риск модели и почему монета не взята. Модель: капитал '
        '200 000 USDT — база расчёта, не ваш баланс; риск 0,5% на сделку, у сильнейшей больше, не больше 1%; все открытые сигналы '
        'вместе ≤ 10%; стоп ≤ 14% от входа; до 7 новых за закрытие.\n'
        'На один запрос: «сигнал 50000 риск 0,75 лимит 8 стоп 12 топ 3» — капитал, риск на сделку (≤ 1%), общий лимит (≤ 10%), '
        'предел стопа (≤ 14%), число сделок (≤ 7). Умолчания не меняются; ограничения можно только ужесточить.\n'
        '«Реестр» — все STRONG-сигналы бота: открытые, завершённые, итоги.\n'
        '«Рейтинг» — рейтинг правила по 42 монетам; «рейтинг 15».\n'
        '«Оценка» — уверенность и статистика реестра.\n'
        'Проверки — в 04:10 и 19:07 по Батуми. Со звуком — новый STRONG, стоп, выход по сигналу, неисполненный лимит; остальное '
        'приходит тихо, проверка без событий — одной строкой.')


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


class TooMany(RuntimeError):
    """Telegram's 429: too many requests, and the seconds it asks to wait (TZ-40)."""

    def __init__(self, text, retry_after):
        super().__init__(text)
        self.retry_after = retry_after


class Telegram:
    """The Bot API through one request function: every call is a JSON POST with UA as its User-Agent."""

    def __init__(self, token, chat=None):
        self.token, self.chat = token, chat

    def call(self, method, http_timeout=30, **params):
        """One call; a reply not ok raises - TooMany, with the retry_after Telegram names (5 s where it names none), for a 429."""
        req = urllib.request.Request(TG.format(token=self.token, method=method), data=json.dumps(params).encode(),
                                     headers={'User-Agent': UA, 'Content-Type': 'application/json'})
        try:
            with urllib.request.urlopen(req, timeout=http_timeout) as r:
                out = json.loads(r.read())
        except urllib.error.HTTPError as e:
            out = json.loads(e.read() or b'{}')
        if not out.get('ok'):
            text = f"telegram {method}: {out.get('error_code')} {out.get('description')}"
            if out.get('error_code') == 429:
                raise TooMany(text, int((out.get('parameters') or {}).get('retry_after') or 5))
            raise RuntimeError(text)
        return out['result']

    def send(self, text, quiet=False, keyboard=False):
        """The text as HTML, in parts of at most LIMIT characters, PACE seconds apart; a part Telegram cannot parse goes as plain
        text, and a part refused as too many requests waits the retry_after named, at most 60 s, and goes again, twice at most
        (TZ-40). quiet sends every part without a notification (the Bot API's disable_notification); keyboard attaches the reply
        keyboard, KEYBOARD, to the last part (TZ-42)."""
        ids, extra = [], ({'disable_notification': True} if quiet else {})
        parts = chunks(text)
        for k, part in enumerate(parts):
            if k:
                time.sleep(PACE)
            more = dict(extra, reply_markup=KEYBOARD) if keyboard and k == len(parts) - 1 else extra
            for attempt in range(3):
                try:
                    ids.append(self.send_part(part, more))
                    break
                except TooMany as e:
                    if attempt == 2:
                        raise
                    time.sleep(min(e.retry_after, 60) + 1)
        return ids

    def send_part(self, part, extra):
        """One part as HTML, or as plain text where Telegram cannot parse it; its message id."""
        try:
            return self.call('sendMessage', chat_id=self.chat, text=part, parse_mode='HTML', disable_web_page_preview=True,
                             **extra)['message_id']
        except TooMany:
            raise
        except RuntimeError as e:
            if 'parse entities' not in str(e):
                raise
        plain = html.unescape(re.sub(r'</?[bi]>', '', part))
        return self.call('sendMessage', chat_id=self.chat, text=plain, disable_web_page_preview=True, **extra)['message_id']


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


def params(text):
    """A request's parameters (TZ-42): {'capital', 'risk', 'total', 'stop', 'n', 'set' - the names the text gave}, each the model's
    default unless the text names it. «риск X», «лимит X» («всего X»), «стоп X» and «топ N» name theirs; of the other numbers the
    first of 100 or more is the capital and the first below 100 the risk, as TZ-37 read them; 15 000 reads 15000, and 10k, 10к and
    10 тыс read 10000. An override narrows a limit and never widens it: the risk at most the rule's 1 %, the total at most 10 %, the
    stop at most 14 %, N at most 7; the capital 100 to 10,000,000 USDT, the risk at least 0.05 %, the total 0.5 %, the stop 2 %, N 1."""
    s = re.sub(r'@\w+', ' ', text or '')
    s = re.sub(r'(?<=\d)[ \u00a0\u202f](?=\d{3}(?!\d))', '', s)
    s = re.sub(r'(\d+(?:[.,]\d+)?)[ \u00a0]?(?:тыс\.?|[кk])(?![^\W\d_])',
               lambda m: f"{float(m.group(1).replace(',', '.')) * 1000:.0f}", s, flags=re.I)
    got = {}
    m = TOPN.search(s)
    if m:
        got['n'] = int(m.group(1))
        s = s[:m.start()] + ' ' + s[m.end():]
    for name, rx in KEYWORDS:
        m = rx.search(s)
        if m:
            got[name] = float(m.group(1).replace(',', '.'))
            s = s[:m.start()] + ' ' + s[m.end():]
    nums = [float(x.replace(',', '.')) for x in re.findall(r'\d+(?:[.,]\d+)?', s)]
    big = next((x for x in nums if x >= 100), None)
    small = next((x for x in nums if x < 100), None)
    if big is not None:
        got['capital'] = big
    if small is not None and 'risk' not in got:
        got['risk'] = small
    return {'capital': min(max(got.get('capital', CAPITAL), 100.0), 10_000_000.0),
            'risk': min(max(got.get('risk', adv3.RISK), 0.05), adv3.RISK_MAX),
            'total': min(max(got.get('total', RISK_TOTAL), 0.5), RISK_TOTAL),
            'stop': min(max(got.get('stop', STOP_MAX), 2.0), STOP_MAX),
            'n': min(max(int(got.get('n', NEW_MAX)), 1), NEW_MAX), 'set': sorted(got)}


def route(text):
    """(kind, argument) of a text (TZ-42): ('signal', params(text)) for «сигнал …» and «топ N …»; ('registry', None) for «реестр»;
    ('ranking', n) for «рейтинг [N]», n 1 to RANK_MAX, default RANK_LIST; ('assess', None) for «оценка»; ('help', None) for «помощь»,
    /start and the like; None where the text is none of them."""
    text = text or ''
    m = HEAD.match(text)
    if not m:
        return None
    word = m.group(1).lower()
    if word in ASSESS:
        return ('assess', None)
    if word in REGISTRY:
        return ('registry', None)
    if word in HELPS:
        return ('help', None)
    if word in RANKING:
        nums = re.findall(r'\d+', text[m.end():])
        return ('ranking', min(max(int(nums[0]), 1), RANK_MAX) if nums else RANK_LIST)
    if word in OPEN:
        return ('signal', params(text))
    return None


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


def live_report(data, deposit, risk):
    """The report of the latest close at this moment: the closed candles and funding Data holds, the mark prices and funding
    intervals read now; marks that fail leave the cards on the close."""
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
    return adv3.report(cs, funds, marks, deposit, risk, int(time.time() * 1000), data.missing, intervals)


def ranked(rep):
    """Every LONG or SHORT coin of the report in the rule's order: adv3.ranking applied again to the coins it has not yet
    placed, so the first three are the report's TOP-3 and no order is written here."""
    rest = [(coin, (r['signal'], r.get('z'), r.get('sum'), r.get('U'), r.get('close'))) for coin in adv3.COINS
            for r in (rep['rows'][coin],) if r.get('signal') in (1, -1)]
    out = []
    while rest:
        top, _ = adv3.ranking(rest)
        if not top:
            break
        out += top
        rest = [x for x in rest if x[0] not in top]
    return out


def strong_all(rep):
    """STRONG at every rank (TZ-40): every coin of the rule's order whose four signs agree with its side and whose |z| is at least
    the rule's STRONG_Z - the frozen rule's condition without its TOP-3, so that its members among the TOP-3 are the report's
    STRONG. In the rule's order."""
    rows = rep['rows']
    return [coin for coin in ranked(rep) if rows[coin].get('sum') == 4 * rows[coin]['signal'] and abs(rows[coin]['z']) >= adv3.STRONG_Z]


def liquidity(coin, now_ms):
    """The mean quote volume in USDT of the coin's last LIQ_DAYS closed days, from fapi.binance.com, or None."""
    try:
        rows = adv3.fapi('/fapi/v1/klines', symbol=coin + 'USDT', interval='1d', limit=LIQ_DAYS + 1)
        vols = [float(r[7]) for r in rows if int(r[6]) < now_ms][-LIQ_DAYS:]
        return sum(vols) / len(vols) if vols else None
    except Exception as e:
        log('liquidity failed:', coin, repr(e)[:200])
        return None


def volumes(coins, now_ms):
    """{coin: liquidity(coin, now_ms)} for coins, six requests at a time (TZ-40: an allocation reads every STRONG coin's)."""
    with ThreadPoolExecutor(6) as pool:
        return dict(zip(coins, pool.map(lambda coin: liquidity(coin, now_ms), coins)))


# ---- time ----------------------------------------------------------------------------------------------------------

def ms_at(t):
    """A datetime as epoch milliseconds."""
    return int(t.timestamp() * 1000)


def iso(ms):
    """Epoch milliseconds as an ISO instant in UTC, to the second."""
    return dt.datetime.fromtimestamp(ms / 1000, dt.timezone.utc).isoformat(timespec='seconds')


def from_iso(text):
    """An ISO instant as epoch milliseconds."""
    return int(dt.datetime.fromisoformat(text).timestamp() * 1000)


def day_ms(day):
    """The epoch milliseconds of a UTC day's 00:00."""
    return int(dt.datetime.combine(day, dt.time(0), tzinfo=dt.timezone.utc).timestamp() * 1000)


def ceil5(ms):
    """The first 5-minute candle's open at or after ms."""
    return -(-int(ms) // K5_MS) * K5_MS


def ceil1(ms):
    """The first 1-minute candle's open at or after ms."""
    return -(-int(ms) // K1_MS) * K1_MS


def second(ms):
    """ms to its whole second, as an event's instant is written: a signal's issue, its place and its fill rest on the same instant."""
    return int(ms) - int(ms) % 1000


def bat(text):
    """An ISO instant as dd.mm HH:MM in Batumi."""
    return (dt.datetime.fromisoformat(text) + BATUMI).strftime('%d.%m %H:%M')


# ---- the registry of STRONG signals (TZ-42) -------------------------------------------------------------------------

def line_hash(line):
    return hashlib.sha256(line.encode('utf-8')).hexdigest()


def event_line(ev):
    """An event as its one line: compact JSON, keys sorted, Cyrillic as it is."""
    return json.dumps(ev, ensure_ascii=False, sort_keys=True, separators=(',', ':'))


def base_fund(_day):
    """The rule's funding where the source served none: +0.01 % per 8 h, three settlements a day (RULE-ADV-3)."""
    return 3 * adv3.BASE_F


class Registry:
    """The STRONG signals the bot published (TZ-42): registry.jsonl in its directory, one event a line - seed, open, fill, target,
    stop, exit, expire - each with its number n, the instant it was written (at) and the SHA-256 of the line before it (prev, GENESIS
    for the first), so that a line changed, inserted or removed breaks the chain at the line after it; and registry-state.json, each
    open signal's place on the 5-minute candles and the last event a message announced, written in one rename and rebuilt from the
    log where it is lost. A torn last line - a write cut short - is cut at load. The signals are derived from the events alone."""

    def __init__(self, folder):
        self.path, self.state_path = os.path.join(folder, REG_FILE), os.path.join(folder, REG_STATE)
        self.events, self.sig, self.cursor = [], {}, {}
        self.head, self.broken, self.torn, self.announced = GENESIS, None, 0, 0
        self.load()

    def load(self):
        if os.path.exists(self.path):
            with open(self.path, 'rb') as fh:
                data = fh.read()
            if data and not data.endswith(b'\n'):
                cut = data.rfind(b'\n') + 1
                self.torn = len(data) - cut
                with open(self.path, 'r+b') as fh:
                    fh.truncate(cut)
                data = data[:cut]
            prev = GENESIS
            for raw in data.decode('utf-8').splitlines():
                try:
                    ev = json.loads(raw)
                except ValueError:
                    ev = None
                if not isinstance(ev, dict):
                    self.broken = self.broken or len(self.events) + 1
                elif ev.get('prev') != prev or ev.get('n') != len(self.events) + 1:
                    self.broken = self.broken or len(self.events) + 1
                if isinstance(ev, dict):
                    self.events.append(ev)
                    self.apply(ev)
                prev = line_hash(raw)
            self.head = prev
        if os.path.exists(self.state_path):
            try:
                st = json.loads(read(self.state_path))
                self.cursor = {int(k): dict(v) for k, v in st['cursor'].items()}
                self.announced = int(st['announced'])
            except (KeyError, TypeError, ValueError, AttributeError):
                self.cursor, self.announced = {}, len(self.events)
        else:
            self.announced = len(self.events)

    def apply(self, ev):
        """One event's effect on the signals."""
        kind, i = ev.get('type'), ev.get('id')
        if kind == 'open':
            self.sig[i] = new_signal(ev)
        elif i in self.sig:
            advance(self.sig[i], ev)

    def append(self, ev, at):
        """One event written: its number, the instant it is written and the chain's prev added, the line flushed to the disk before
        it is applied. Returns the event as written."""
        ev = dict(ev, n=len(self.events) + 1, prev=self.head, at=at.isoformat(timespec='seconds'))
        line = event_line(ev)
        with open(self.path, 'a', encoding='utf-8') as fh:
            fh.write(line + '\n')
            fh.flush()
            os.fsync(fh.fileno())
        self.events.append(ev)
        self.apply(ev)
        self.head = line_hash(line)
        return ev

    def save_state(self):
        put(self.state_path, json.dumps({'cursor': {str(k): v for k, v in sorted(self.cursor.items())},
                                         'announced': self.announced}, sort_keys=True))

    def next_id(self):
        return 1 + max(self.sig, default=0)

    def cursor_of(self, s):
        """A signal's place on its candles: the first minute not yet walked as closed (t), the last daily close its walk passed (b) and
        its largest favourable excursion in R (mfe); from its issue where none is kept - the first 1-minute candle at or after it."""
        cur = self.cursor.get(s['id'])
        if cur is None:
            issued = from_iso(s['utc'])
            cur = {'t': ceil1(issued), 'b': issued, 'mfe': 0.0}
        return cur

    def live(self):
        """The signals open or waiting for their limit, by number."""
        return [s for _i, s in sorted(self.sig.items()) if s['status'] in ('pending', 'open')]


def new_signal(ev):
    """A signal from its open event: waiting for its entry, no target, no end."""
    s = dict(ev, status='pending', fill=None, fill_utc=None, hit=0, hits={}, exit=None, exit_utc=None, why=None, R=None, pnl=None)
    for k in ('type', 'n', 'at', 'prev'):
        s.pop(k, None)
    return s


def advance(s, ev):
    """One event's effect on its signal: a fill opens it, a target raises its hit, a stop or the rule's exit closes it, an expiry ends
    a limit not filled."""
    kind = ev.get('type')
    if kind == 'fill':
        s.update(status='open', fill=ev['price'], fill_utc=ev['utc'])
    elif kind == 'target':
        s['hit'] = max(s['hit'], ev['k'])
        s['hits'][str(ev['k'])] = ev['utc']
    elif kind in ('stop', 'exit'):
        s.update(status='closed', exit=ev['price'], exit_utc=ev['utc'], why='stop' if kind == 'stop' else 'signal', R=ev['R'], pnl=ev['pnl'])
    elif kind == 'expire':
        s.update(status='expired', exit_utc=ev['utc'], why='expire')


def status_of(s):
    """The Boss's status of a signal (his specification of 2026-11-05, §3): PENDING, ACTIVE or TARGET k REACHED while it lives; at
    its end TARGET 3 REACHED, PARTIAL TARGET COMPLETION (a target and not the third), STOPPED OUT or INVALIDATED (the rule's exit at a
    close, before a target), EXPIRED (a limit not filled by its validity)."""
    if s['status'] == 'pending':
        return 'PENDING'
    if s['status'] == 'expired':
        return 'EXPIRED'
    if s['status'] == 'open':
        return 'TARGET %d REACHED' % s['hit'] if s['hit'] else 'ACTIVE'
    if s['hit'] == 3:
        return 'TARGET 3 REACHED'
    if s['hit']:
        return 'PARTIAL TARGET COMPLETION'
    return 'STOPPED OUT' if s['why'] == 'stop' else 'INVALIDATED'


def open_risk(reg, skip_close=None):
    """The risk at their stops of the signals open or waiting, in percent of each one's capital, by side - those of skip_close left
    out where it is given: {1: the longs', -1: the shorts'}."""
    out = {1: 0.0, -1: 0.0}
    for s in reg.live():
        if s['close_of'] != skip_close:
            out[s['side']] += s['risk_pct']
    return out


def klines(coin, start_ms, now_ms, step=K5_MS, count=None):
    """The coin's candles of step ms - 5 minutes, or 1 - from fapi.binance.com from the one opening at start_ms on: count of them in
    one request where count is given, else page after page of K5_PAGE to now_ms. [(open ms, open, high, low, close, closed)], closed
    where the candle's close time is before now_ms; a start after now_ms asks nothing, no candle opening there yet."""
    out, t = [], int(start_ms)
    for _ in range(0 if t > now_ms else 1 if count else 400):
        n = count or K5_PAGE
        rows = adv3.fapi('/fapi/v1/klines', symbol=coin + 'USDT', interval=INTERVAL[step], startTime=t, limit=n)
        for r in rows:
            if int(r[0]) >= t:
                out.append((int(r[0]), float(r[1]), float(r[2]), float(r[3]), float(r[4]), int(r[6]) < now_ms))
        if len(rows) < n:
            break
        t = int(rows[-1][0]) + step
        if t > now_ms:
            break
    return out


def first_window(coin, cur, now_ms):
    """A signal's first minutes on 1-minute candles (TZ-42): where its place is not on a 5-minute boundary - it was issued inside a
    5-minute candle, whose range mixes the minutes before the issue with those after it - the 1-minute candles from its place to the
    next boundary, in one request; else none."""
    t = cur['t']
    return klines(coin, t, now_ms, K1_MS, (ceil5(t) - t) // K1_MS) if t % K5_MS else []


def walk(s, cur, c, fund, k5, until=None, k1=()):
    """One signal walked forward on its coin's candles (TZ-42), in time order: the events of its fill, its targets and its end, and
    its new place. s is the signal; cur its place; c the coin's closed daily candles; fund, day -> the day's funding sum; k1 the
    1-minute candles of its first minutes (first_window), then k5 the 5-minute ones, each [(open ms, o, h, l, c, closed)]; until, where
    given, the instant past which nothing is walked - no candle closing after it is read. Each daily close the walk passes
    ends a filled signal whose rule signal at that close is not its side, at that close's price (the rule's exit, adv3.signal); the
    validity's end - the close after the card's - ends a limit not yet filled, whether its daily candle is served or not. Each candle fills a waiting limit it reaches - at the limit,
    or at the open where the open is already past it - and then reads only the stop; a filled signal's candle credits each target its
    open is already past, then ends the signal at the stop it reaches - at the open where the open is already beyond the stop - a target
    touched later in that candle not credited; else it credits each target it reaches. A candle not yet closed is read and not walked
    past. The result of an end: the move from the fill, both sides' costs (adv3.COST) and the funding of every close held, per unit,
    in R of the planned risk |entry - stop| and in USDT at the signal's quantity."""
    side, E, S, T = s['side'], s['entry'], s['stop'], s['targets']
    days = sorted(c)
    closes = [c[d][3] for d in days]
    D = dt.date.fromisoformat(s['close_of'])
    valid = from_iso(s['valid'])
    t, b, mfe = cur['t'], cur['b'], cur.get('mfe', 0.0)
    status, hit, fp = s['status'], s['hit'], s['fill']
    fill_ms = from_iso(s['fill_utc']) if s['fill_utc'] else None
    risk = abs(E - S)
    bounds = [(day_ms(d) + DAY_MS, i) for i, d in enumerate(days) if d > D and day_ms(d) + DAY_MS > b]
    out = []

    def funding(end_ms):
        return sum(side * fund(d) * closes[i] for i, d in enumerate(days) if fill_ms < day_ms(d) + DAY_MS <= end_ms)

    def end(kind, at_ms, X):
        unit_ = side * (X - fp) - adv3.COST * (fp + X) - funding(at_ms)
        out.append({'type': kind, 'id': s['id'], 'utc': iso(at_ms), 'price': X, 'R': unit_ / risk, 'pnl': unit_ * s['qty']})

    def at_close(B, i):
        nonlocal status
        if status == 'open' and adv3.signal(days, closes, i) != side:
            end('exit', B, closes[i])
            status = 'closed'
        return status not in ('open', 'pending')

    def expire():
        nonlocal status
        out.append({'type': 'expire', 'id': s['id'], 'utc': iso(valid)})
        status = 'expired'

    def place():
        return {'t': t, 'b': b, 'mfe': mfe}

    bi = 0
    for width, (o_ms, o, h, lo, _cl, closed) in [(K1_MS, x) for x in k1] + [(K5_MS, x) for x in k5]:
        if o_ms < t:
            continue
        if until is not None and o_ms + width > until:
            break
        while bi < len(bounds) and bounds[bi][0] <= o_ms:
            B, i = bounds[bi]
            bi, b = bi + 1, B
            if at_close(B, i):
                return out, place()
        if status == 'pending' and o_ms >= valid:
            expire()
            return out, place()
        if status == 'pending':
            if (lo <= E) if side > 0 else (h >= E):
                fp = min(o, E) if side > 0 else max(o, E)
                fill_ms, status = o_ms, 'open'
                out.append({'type': 'fill', 'id': s['id'], 'utc': iso(o_ms), 'price': fp})
                if (lo <= S) if side > 0 else (h >= S):
                    end('stop', o_ms, o if ((o <= S) if side > 0 else (o >= S)) else S)
                    return out, place()
        else:
            for k in (1, 2, 3):
                if k > hit and ((o >= T[k - 1]) if side > 0 else (o <= T[k - 1])):
                    out.append({'type': 'target', 'id': s['id'], 'utc': iso(o_ms), 'k': k, 'price': T[k - 1]})
                    hit = k
            gap = (o <= S) if side > 0 else (o >= S)
            if gap or ((lo <= S) if side > 0 else (h >= S)):
                end('stop', o_ms, o if gap else S)
                return out, place()
            for k in (1, 2, 3):
                if k > hit and ((h >= T[k - 1]) if side > 0 else (lo <= T[k - 1])):
                    out.append({'type': 'target', 'id': s['id'], 'utc': iso(o_ms), 'k': k, 'price': T[k - 1]})
                    hit = k
            mfe = max(mfe, side * ((h if side > 0 else lo) - fp) / risk)
        if closed:
            t = o_ms + width
    while bi < len(bounds) and bounds[bi][0] <= t and (until is None or bounds[bi][0] <= until):
        B, i = bounds[bi]
        bi, b = bi + 1, B
        if at_close(B, i):
            return out, place()
    if status == 'pending' and t >= valid and (until is None or valid <= until):
        expire()
    return out, place()


def reconcile(reg, cs, funds, now_ms, at):
    """Every signal open or waiting walked to now (TZ-42): each coin's 5-minute candles fetched once from the earliest 5-minute
    boundary any of its signals' places reaches, and a signal's first minutes on their 1-minute candles where its place is still among
    them; the events appended in time order, the places saved. A coin or a signal whose candles fail stays where it was, logged.
    Returns the events appended."""
    groups = {}
    for s in reg.live():
        groups.setdefault(s['coin'], []).append(s)
    new = []
    for coin in sorted(groups, key=adv3.COINS.index):
        sigs = groups[coin]
        try:
            k5 = klines(coin, min(ceil5(reg.cursor_of(s)['t']) for s in sigs), now_ms)
        except Exception as e:
            log('5-minute candles failed:', coin, repr(e)[:200])
            continue
        for s in sigs:
            cur = reg.cursor_of(s)
            try:
                k1 = first_window(coin, cur, now_ms)
            except Exception as e:
                log('1-minute candles failed:', coin, repr(e)[:200])
                continue
            evs, reg.cursor[s['id']] = walk(s, cur, cs.get(coin) or {}, funds.get(coin) or base_fund, k5, k1=k1)
            new += evs
    new.sort(key=lambda e: (e['utc'], e['id']))
    written = [reg.append(e, at) for e in new]
    reg.save_state()
    return written


def seed(reg, cs, funds, now_ms, at):
    """The registry's first event, and the STRONG signals the journal's records published before it (TZ-42): every STRONG card with an
    entry, at market or as a limit, of a daily, request, allocation or check record - of an allocation only the coins it placed - in
    the order the records were written, each a signal issued at its record's instant, to the second, unless its coin holds a signal
    still open then, walked on its candles to that instant: a card repeated within one signal's life is that signal shown again. Each
    is sized as one trade at the default risk on the default capital and marked legacy. The cards are read one coin at a time - its
    candles fetched once and let go before the next coin's - and the signals and their events written in the order of the cards.
    Returns the signals opened."""
    path = os.path.join(STATE, 'journal.jsonl')
    sha = None
    if os.path.exists(path):
        h = hashlib.sha256()
        with open(path, 'rb') as fh:
            for block in iter(lambda: fh.read(1 << 20), b''):
                h.update(block)
        sha = h.hexdigest()
    records, cards = 0, []
    for rec in journal_records():
        records += 1
        kind = rec.get('kind')
        if kind not in ('daily', 'request', 'alloc', 'check'):
            continue
        try:
            t_ms, close_of = second(from_iso(rec['utc'])), str(dt.date.fromisoformat(rec['close_of']))
        except (KeyError, TypeError, ValueError):
            continue
        placed = None
        if kind == 'alloc' and isinstance(rec.get('alloc'), dict):
            placed = {x.get('coin') for x in (rec['alloc'].get('items') or []) + (rec['alloc'].get('more') or []) if isinstance(x, dict)}
        state = rec.get('state') if isinstance(rec.get('state'), dict) else {}
        btc = (rec.get('signals') or {}).get('BTC') if isinstance(rec.get('signals'), dict) else None
        for cd in rec.get('cards') or []:
            try:
                if (not cd.get('strong') or cd.get('mode') not in ('market', 'limit') or cd.get('entry') is None
                        or (placed is not None and cd['coin'] not in placed)):
                    continue
                coin, side = cd['coin'], int(cd['side'])
                E, S, C, U = float(cd['entry']), float(cd['stop']), float(cd['close']), float(cd['U'])
                T = [float(x) for x in cd['targets']]
                if coin not in adv3.COINS or side not in (1, -1) or len(T) != 3 or min(E, S, C, U) <= 0 or side * (E - S) <= 0:
                    continue
            except (AttributeError, KeyError, TypeError, ValueError):
                continue
            st = state.get(coin) if isinstance(state.get(coin), dict) else {}
            cards.append((t_ms, coin, side, close_of, cd, st, kind, btc))
    reg.append({'type': 'seed', 'utc': iso(now_ms), 'journal_sha': sha, 'records': records, 'cards': len(cards)}, at)
    cards.sort(key=lambda x: x[0])
    acts = []   # (the card's place, 0 an event of the walk to it - 1 the open it makes, the signal, the event)
    for coin in sorted({x[1] for x in cards}, key=adv3.COINS.index):
        mine = [(k, x) for k, x in enumerate(cards) if x[1] == coin]
        try:
            k5 = klines(coin, ceil5(mine[0][1][0]), now_ms)
        except Exception as e:
            log('5-minute candles failed:', coin, repr(e)[:200])
            k5 = None
        sigs = []
        for k, (t_ms, _coin, side, close_of, cd, st, kind, btc) in mine:
            if any(s['side'] == side and s['close_of'] == close_of for s in sigs):
                continue
            live = [s for s in sigs if s['status'] in ('pending', 'open')]
            if live and k5 is not None:
                for s in live:
                    try:
                        k1 = first_window(coin, s['place'], now_ms)
                    except Exception as e:
                        log('1-minute candles failed:', coin, repr(e)[:200])
                        continue
                    evs, s['place'] = walk(s, s['place'], cs.get(coin) or {}, funds.get(coin) or base_fund, k5, until=t_ms, k1=k1)
                    for e in evs:
                        advance(s, e)
                        acts.append((k, 0, s, e))
                live = [s for s in sigs if s['status'] in ('pending', 'open')]
            if live:
                continue
            E, S = float(cd['entry']), float(cd['stop'])
            d = abs(E - S) / E
            pos, _why = position({'stop_pct': 100 * d, 'leverage': min(20, math.floor(1 / (1.5 * d + 0.01))), 'entry': E},
                                 adv3.RISK, CAPITAL, None)
            if pos is None:
                continue
            D = dt.date.fromisoformat(close_of)
            s = new_signal({'type': 'open', 'id': None, 'utc': iso(t_ms), 'coin': coin, 'side': side, 'close_of': close_of,
                            'source': 'journal:' + kind, 'mode': cd['mode'], 'entry': E, 'stop': S, 'targets': [float(x) for x in cd['targets']],
                            'close': float(cd['close']), 'U': float(cd['U']), 'z': st.get('z'), 'sum': st.get('sum'), 'rank': cd.get('rank'),
                            'since': cd.get('since'), 'btc': btc, 'breadth': None, 'valid': iso(day_ms(D + 2 * adv3.DAY)), 'capital': CAPITAL,
                            'risk_pct': pos['risk_pct'], 'loss': pos['loss'], 'notional': pos['notional'], 'qty': pos['qty'],
                            'leverage': pos['leverage'], 'margin': pos['margin'], 'legacy': True})
            if cd['mode'] == 'market':
                advance(s, {'type': 'fill', 'price': E, 'utc': iso(t_ms)})
            s['place'] = {'t': ceil1(t_ms), 'b': t_ms, 'mfe': 0.0}
            sigs.append(s)
            acts.append((k, 1, s, None))
    acts.sort(key=lambda a: (a[0], a[1]))
    opened = []
    for _k, what, s, e in acts:
        if what == 1:
            s['id'] = reg.next_id()
            reg.append({k: s[k] for k in LEGACY_KEYS} | {'type': 'open', 'id': s['id']}, at)
            if s['mode'] == 'market':
                reg.append({'type': 'fill', 'id': s['id'], 'utc': s['utc'], 'price': s['entry']}, at)
            opened.append(s)
        else:
            reg.append(dict(e, id=s['id']), at)
    for s in opened:
        reg.cursor[s['id']] = s['place']
    reg.save_state()
    return len(opened)


# ---- the plan: the STRONG signals of a close, their positions within the limits (TZ-42) --------------------------------

def notional_of(cd, risk_pct, capital, volume):
    """The notional the loss at the stop allows at risk_pct percent of the capital (TZ-42), both sides' costs included, at most LIQ_FRAC
    of the coin's mean daily volume where known, in whole USDT rounded down: (notional, the loss per USDT of it, whether the volume
    capped it)."""
    rate = cd['stop_pct'] / 100 + 2 * adv3.COST
    raw = risk_pct / 100 * capital / rate
    capped = bool(volume) and raw > LIQ_FRAC * volume
    return math.floor(LIQ_FRAC * volume if capped else raw), rate, capped


def position(cd, risk_pct, capital, volume):
    """One position at risk_pct percent of the capital (TZ-42): notional_of's notional; the leverage the rule's ceiling - the card's -
    lowered only to keep the margin at MARGIN_MIN percent of the capital or more, never raised; a notional under that floor is no
    position, for the risk is never raised to meet it; the margin at most MARGIN_EXC percent of the capital in whole USDT, the notional
    cut where it would pass it. (position, None) or (None, the reason)."""
    notional, rate, capped = notional_of(cd, risk_pct, capital, volume)
    floor_m = MARGIN_MIN / 100 * capital
    if cd['leverage'] < 1:
        return None, 'плечо правила меньше 1×'
    if notional < floor_m:
        return None, 'позиция меньше минимальной маржи %s USDT' % adv3.usdt(floor_m) + (' — по ликвидности' if capped else '')
    lev = min(cd['leverage'], math.floor(notional / floor_m))
    margin = math.ceil(notional / lev)
    top = math.floor(MARGIN_EXC / 100 * capital)
    cut = margin > top
    if cut:
        notional, margin = top * lev, top
    loss = notional * rate
    return {'notional': notional, 'leverage': lev, 'lmax': cd['leverage'], 'margin': margin, 'loss': loss,
            'risk_pct': 100 * loss / capital, 'qty': notional / cd['entry'], 'capped': capped,
            'over': margin > MARGIN_MAX / 100 * capital, 'cut': cut}, None


def allocate(items, prm, room, liq):
    """The risk shared by strength (TZ-42): each item without a reason against it takes a share min(|z|, Z_CAP) over all of them -
    k times prm's risk times its share, at most the rule's RISK_MAX - then, in the rule's order, that risk or what the room still
    holds, sized by position(). An item gets a reason and a code where it has no position: 'room' where the room cut its risk, else
    'margin', its position under the margin's floor. Each item sized gets pos, with its wanted risk and whether the room cut it."""
    live = [it for it in items if not it.get('why')]
    if not live:
        return
    q = [min(abs(it['card']['z']), Z_CAP) for it in live]
    for it, qi in zip(live, q):
        want = min(adv3.RISK_MAX, len(live) * prm['risk'] * qi / sum(q))
        take = max(0.0, min(want, room))
        pos, why = position(it['card'], take, prm['capital'], liq.get(it['coin'])) if take > 1e-9 else (None, None)
        if pos is None:
            if take < want - 1e-9:
                it['code'], it['why'], it['detail'] = 'room', 'лимит общего риска %s%% исчерпан' % pct0(prm['total']), ''
            else:
                it['code'], it['why'], it['detail'] = 'margin', why, '%s USDT' % adv3.usdt(
                    notional_of(it['card'], take, prm['capital'], liq.get(it['coin']))[0])
            continue
        pos.update(want=want, short=take < want - 1e-9)
        it['pos'] = pos
        room -= pos['risk_pct']


def pct0(x):
    """A percent without a needless ',0': 10 -> '10', 12.5 -> '12,5'."""
    return adv3.pct(x, 1).replace(',0', '')


def candidates(rep, reg, prm):
    """The STRONG coins of the report's close at prm (TZ-42), in the rule's order: the signals of this close the registry holds open or
    waiting ('mine'), the coins that may be new - current prices, an entry, a stop within prm's limit, no signal of the coin open from
    an earlier close and none of this close already ended - and the rest named, (coin, side, code, reason). Each item {'coin', 'side',
    'rank', 'card' at prm's capital and risk, 'sig' - the registry's or None - 'code' and 'why' - None, or why it has no position now}.
    A coin open from an earlier close belongs to the open list, not to the candidates."""
    rows, close_of = rep['rows'], rep['close_of']
    rank = {coin: k for k, coin in enumerate(ranked(rep), 1)}
    live = {s['coin']: s for s in reg.live()}
    this = {(s['coin'], s['side']): s for s in reg.sig.values() if s['close_of'] == close_of}
    mine, new, excluded = [], [], []
    for coin in strong_all(rep):
        side = rows[coin]['signal']
        if coin in live and live[coin]['close_of'] != close_of:
            continue
        s = this.get((coin, side))
        if s is not None and s['status'] not in ('pending', 'open'):
            excluded.append((coin, side, 'ended', 'сигнал этого закрытия уже завершён', '#%d %s' % (s['id'], LABEL[status_of(s)])))
            continue
        it = carded(rep, coin, rank[coin], prm, s)
        if s is not None:
            mine.append(it)
        elif it['why']:
            excluded.append((coin, side, it['code'], it['why'], it['detail']))
        else:
            new.append(it)
    return mine, new, excluded


def carded(rep, coin, rank, prm, sig=None):
    """One STRONG coin's item at prm: its card at prm's capital and risk, and the reason, if any, it has no position now - no current
    price, no entry, a stop beyond prm's limit."""
    row = rep['rows'][coin]
    cd = dict(adv3.card(coin, row, True, prm['capital'], prm['risk']), sum=row.get('sum'))
    code = why = None
    detail = ''
    if not rep['marks_ok']:
        code, why = 'marks', 'нет текущей цены Binance'
    elif cd['mode'] == 'none':
        code, why = 'near', 'цена у стопа — входа нет'
    elif cd['stop_pct'] > prm['stop'] + 1e-9:
        code, why, detail = 'stop', 'стоп дальше %s%%' % pct0(prm['stop']), '%s%%' % adv3.pct(cd['stop_pct'])
    return {'coin': coin, 'side': row['signal'], 'rank': rank, 'card': cd, 'sig': sig, 'code': code, 'why': why, 'detail': detail}


def model_plan(rep, reg, liq):
    """The model's new signals at this moment (TZ-42): the new candidates at the defaults, the first NEW_MAX a close counting those the
    registry holds of this close, sized by allocate within the room every open signal leaves under RISK_TOTAL; with the signals of
    this close the registry holds open ('mine') and the coins not taken, each (coin, side, code, reason, detail) - those beyond the
    first NEW_MAX the room's where the room stopped one of the first, else the count's."""
    mine, new, excluded = candidates(rep, reg, DEFAULTS)
    allowed = max(0, NEW_MAX - sum(1 for s in reg.sig.values() if s['close_of'] == rep['close_of']))
    risk = open_risk(reg)
    head = new[:allowed]
    allocate(head, DEFAULTS, RISK_TOTAL - risk[1] - risk[-1], liq)
    excluded += [(it['coin'], it['side'], it['code'], it['why'], it['detail']) for it in head if it.get('why')]
    full = any(it.get('code') == 'room' for it in head)
    for it in new[allowed:]:
        if full:
            excluded.append((it['coin'], it['side'], 'room', 'лимит общего риска %s%% исчерпан' % pct0(RISK_TOTAL), ''))
        else:
            excluded.append((it['coin'], it['side'], 'count', 'сверх %d новых сигналов за закрытие' % NEW_MAX, ''))
    return {'new': [it for it in head if it.get('pos')], 'mine': mine, 'excluded': excluded, 'risk': risk}


def view_plan(rep, reg, liq, prm, model):
    """A request's plan (TZ-42): the signals of this close the registry holds open and the model's new ones, carded at prm, in the
    rule's order, those beyond prm's N named; a coin prm excludes - beyond its stop limit, without an entry - named with prm's reason,
    one the model did not take with the model's; the rest sized at prm, the risk shared by strength within the room the signals of
    earlier closes leave under prm's total. A signal of the registry stays in the plan without a position where it has none now, its
    card saying why; the request writes no signal the model did not take."""
    mine, new, excluded = candidates(rep, reg, prm)
    taken = {it['coin'] for it in model['new']}
    why = {c: (code, w, detail) for c, _s, code, w, detail in model['excluded']}
    for it in new:
        if it['coin'] not in taken:
            code, w, detail = why.get(it['coin'], ('model', 'модель не взяла', ''))
            excluded.append((it['coin'], it['side'], code, w, detail))
    items = sorted(mine + [it for it in new if it['coin'] in taken], key=lambda x: x['rank'])
    for it in items[prm['n']:]:
        excluded.append((it['coin'], it['side'], 'top', 'сверх топ %d запроса' % prm['n'], ''))
    keep = items[:prm['n']]
    older = open_risk(reg, rep['close_of'])
    allocate(keep, prm, prm['total'] - older[1] - older[-1], liq)
    out = []
    for it in keep:
        if it.get('pos') or it['sig'] is not None:
            out.append(it)
        else:
            excluded.append((it['coin'], it['side'], it['code'], it['why'], it['detail']))
    return {'items': out, 'excluded': excluded, 'older': older}


def register(reg, rep, items, at, source):
    """Each new item written as a signal (TZ-42), in the rule's order: 'open' with its card, its position at the defaults and what it
    rests on - the rule's strength and sum, its rank, the day its rule signal began, BTC's signal, how many coins were STRONG at every
    rank - and, an entry at market, 'fill' at that entry and that instant: a market entry is the price the card published. A limit
    waits for its price until the close after the card's. Returns the ids, which are reg.next_id() onwards."""
    rows, ids = rep['rows'], []
    issued = second(ms_at(at))
    D = dt.date.fromisoformat(rep['close_of'])
    breadth = len(strong_all(rep))
    for it in sorted(items, key=lambda x: x['rank']):
        cd, pos = it['card'], it['pos']
        i = reg.next_id()
        reg.append({'type': 'open', 'id': i, 'utc': iso(issued), 'coin': it['coin'], 'side': it['side'], 'close_of': rep['close_of'],
                    'source': source, 'mode': cd['mode'], 'entry': cd['entry'], 'stop': cd['stop'], 'targets': cd['targets'],
                    'close': cd['close'], 'U': cd['U'], 'z': cd['z'], 'sum': cd['sum'], 'rank': it['rank'], 'since': cd['since'],
                    'btc': (rows.get('BTC') or {}).get('signal'), 'breadth': breadth, 'valid': iso(day_ms(D + 2 * adv3.DAY)),
                    'capital': CAPITAL, 'risk_pct': pos['risk_pct'], 'loss': pos['loss'], 'notional': pos['notional'], 'qty': pos['qty'],
                    'leverage': pos['leverage'], 'margin': pos['margin'], 'legacy': False}, at)
        if cd['mode'] == 'market':
            reg.append({'type': 'fill', 'id': i, 'utc': iso(issued), 'price': cd['entry']}, at)
        reg.cursor[i] = {'t': ceil1(issued), 'b': issued, 'mfe': 0.0}
        ids.append(i)
    reg.save_state()
    return ids


def ensure(reg, data, now):
    """The registry brought to now: seeded from the journal where it holds no event yet - its events then counted announced, the
    history's, never news - and every signal open or waiting walked to now. Returns the signals the seed opened, or None."""
    cs, funds = data.fresh()
    now_ms = ms_at(now)
    opened = None
    if not reg.events:
        opened = seed(reg, cs, funds, now_ms, now)
    reconcile(reg, cs, funds, now_ms, now)
    if opened is not None:
        reg.announced = len(reg.events)
        reg.save_state()
    return opened


# ---- the schedule: two slots a day, each sent once ----------------------------------------------------------------

def slot_key(slot):
    return slot[0], [k for k, _ in SLOTS].index(slot[1])


def slot_at(slot):
    return dt.datetime.combine(slot[0], dict(SLOTS)[slot[1]], tzinfo=dt.timezone.utc)


def slot_text(slot):
    return f'{slot[0].isoformat()} {slot[1]}'


def slot_parse(text):
    """The slot a check-done file names, 'YYYY-MM-DD signal' or 'YYYY-MM-DD fact'; None for anything else."""
    try:
        day, kind = text.split()
        return (dt.date.fromisoformat(day), kind) if kind in dict(SLOTS) else None
    except ValueError:
        return None


def latest_slot(now):
    """The last slot whose instant is at or before now."""
    for kind, at in reversed(SLOTS):
        if now >= dt.datetime.combine(now.date(), at, tzinfo=dt.timezone.utc):
            return now.date(), kind
    return now.date() - adv3.DAY, SLOTS[-1][0]


def due(now, done):
    """The slot to run now, or None: the latest slot unless done holds it or a later one; where the latest is a day's fact
    check and that day's signal check is not done, the signal check - the fact slot repeats the signal slot where it failed."""
    last = latest_slot(now)
    if done is not None and slot_key(done) >= slot_key(last):
        return None
    if last[1] == 'fact' and (done is None or slot_key(done) < slot_key((last[0], 'signal'))):
        return last[0], 'signal'
    return last


def done_after(slot, now):
    """What a check marks done: itself, or - a signal check that ends at or after its day's fact slot - that day's fact check too."""
    if slot[1] == 'signal' and now >= slot_at((slot[0], 'fact')):
        return slot[0], 'fact'
    return slot


def next_at(now):
    """The first slot instant after now."""
    for day in (now.date(), now.date() + adv3.DAY):
        for kind, at in SLOTS:
            t = dt.datetime.combine(day, at, tzinfo=dt.timezone.utc)
            if t > now:
                return t


def hhmm(t):
    return (t + BATUMI).strftime('%H:%M')


# ---- the journal ---------------------------------------------------------------------------------------------------

def journal_records():
    """Every record of journal.jsonl that parses as an object, in order, one at a time - a year's journal is never held whole;
    a line that does not parse is left out."""
    path = os.path.join(STATE, 'journal.jsonl')
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            for line in f:
                try:
                    rec = json.loads(line)
                except ValueError:
                    continue
                if isinstance(rec, dict):
                    yield rec


def last_check():
    """The journal's last check record, or None, read in one pass that keeps it alone."""
    prev = None
    for rec in journal_records():
        if rec.get('kind') == 'check':
            prev = rec
    return prev


def append(rec):
    with open(os.path.join(STATE, 'journal.jsonl'), 'a', encoding='utf-8') as f:
        f.write(json.dumps(rec, ensure_ascii=False, default=str) + '\n')


def base_record(kind, rep, ids, at):
    """A journal record: its instant, kind, rule, close, the report's deposit and risk, TOP-3, STRONG, message ids and every coin's
    signal."""
    return {'utc': at.isoformat(timespec='seconds'), 'kind': kind, 'rule': rep['rule'], 'close_of': rep['close_of'],
            'deposit': rep['deposit'], 'risk_pct': rep['risk_pct'], 'top': rep['top'], 'strong': rep['strong'], 'message_ids': ids,
            'signals': {k: v.get('signal') for k, v in rep['rows'].items()}}


def item_record(it, i=None):
    """A plan item as a record holds it: its card's fields, its rank, its signal's number and its position."""
    pos = it.get('pos')
    return dict({k: it['card'].get(k) for k in CARD_KEYS}, rank=it['rank'], id=i if i is not None else (it['sig'] or {}).get('id'),
                position={k: pos[k] for k in ('notional', 'leverage', 'margin', 'loss', 'risk_pct')} if pos else None, why=it.get('why'))


# ---- what a message says ------------------------------------------------------------------------------------------

SHOWN = ('fill', 'target', 'stop', 'exit', 'expire')
LOUD = ('stop', 'exit', 'expire')


def signed_usdt(x):
    return ('+' if x >= 0 else '−') + adv3.usdt(abs(x))


def sg(x, places=2):
    """x signed to places decimals, Russian style; a value that rounds to zero is never signed negative."""
    x = round(x, places)
    return adv3.signed(0.0 if x == 0 else x, places)


def footer():
    r = adv3.RELIABILITY
    return f"<i>Уверенность {r}/5 — {adv3.LADDER[r][0]} · размеры — формула Архитектора, не доказана · не инвестиционный совет</i>"


def params_line(prm):
    """The model's parameters a message rests on, and the ones the request overrode."""
    names = {'capital': 'капитал', 'risk': 'риск', 'total': 'лимит', 'stop': 'стоп', 'n': 'топ'}
    pct = adv3.pct
    line = (f"Капитал {adv3.num(prm['capital'], 6)} USDT · риск {pct(prm['risk'])}% · лимит {pct0(prm['total'])}% · "
            f"стоп ≤ {pct0(prm['stop'])}%" + (f" · до {prm['n']} сделок" if 'n' in prm['set'] else ''))
    return line + (' · по запросу: ' + ', '.join(names[k] for k in prm['set']) if prm['set'] else '')


def legend():
    """The targets' line: what the three targets are and how often STRONG trades reached them in TZ-38's history, without survivorship."""
    m = adv3.PIT['strong' if adv3.FACTS['strong'].get('gate_S') == 'NOT DISQUALIFIED' else 'base']['mfe']
    return (f"<i>🎯 — цели +1, +2, +3 U от закрытия; в истории STRONG до них доходили {adv3.pct(100 * m[1], 0)}, "
            f"{adv3.pct(100 * m[2], 0)} и {adv3.pct(100 * m[3], 0)}% сделок</i>")


def card_lines(it, number, new_id=None, mark_new=False):
    """One STRONG item of a plan: its number, coin, side, signal number, rank and strength; entry; stop and targets; and its position
    - the margin, the rule's leverage or less, the notional and the coins, the loss at the stop in USDT and in percent of the capital -
    or why it has none now; a signal of the registry says since when and at what entry it runs."""
    cd, pos, s, side = it['card'], it.get('pos'), it['sig'], it['side']
    price, pct = adv3.price, adv3.pct
    ident = f" #{s['id']}" if s is not None else ((' 🆕' if mark_new else '') + (f" #{new_id}" if new_id else ''))
    lines = [f"{number}) {DOT[side]} <b>{it['coin']} {SIDE[side]}</b>{ident} · ★ ранг {it['rank']}"
             + (' вне ТОП-3' if it['rank'] > adv3.TOP_N else '') + f" · z {sg(cd['z'])}"]
    lo, hi = cd['zone']
    if cd['mode'] == 'market':
        lines.append(f"Вход: <b>по рынку ≈ {price(cd['entry'])}</b> · зона {price(lo)}–{price(hi)}")
    elif cd['mode'] == 'limit':
        lines.append(f"Вход: <b>лимит {price(cd['entry'])}</b> — цена {price(cd['mark'])} ушла от зоны, не догонять")
    else:
        lines.append(f"Вход сейчас: <b>нет</b> — цена {price(cd['mark'])} у стопа")
    if s is not None:
        lines.append(f"Сигнал #{s['id']} с {bat(s['utc'])}: {LABEL[status_of(s)]}" + (f", вход {price(s['fill'])}" if s['fill'] else ''))
    ref = cd['entry'] if cd['entry'] is not None else cd['close']
    lines.append(f"⛔ Стоп <b>{price(cd['stop'])}</b> ({'−' if side > 0 else '+'}{pct(100 * abs(ref - cd['stop']) / ref)}%) · 🎯 "
                 + ' · '.join(price(t) for t in cd['targets']))
    if pos:
        flags = ([' · урезано лимитом риска'] if pos['short'] else []) + ([' · ограничено ликвидностью'] if pos['capped'] else []) \
            + ([' · маржа выше 3,5% капитала — исключение'] if pos['over'] else [])
        lines += [f"Маржа <b>{adv3.usdt(pos['margin'])} USDT</b> · плечо {pos['leverage']}× изол. → позиция {adv3.usdt(pos['notional'])} "
                  f"USDT = {adv3.num(pos['qty'])} {it['coin']}",
                  f"Потеря на стопе <b>{adv3.usdt(pos['loss'])} USDT</b> = {pct(pos['risk_pct'], 2)}% капитала" + ''.join(flags)]
    elif it.get('why'):
        lines.append('Позиции сейчас нет: ' + it['why'])
    return lines


def live_line(s, rows):
    """One signal open or waiting: number, coin, side, the close it is of; its entry, stop, targets reached and where the price
    stands now in R of its planned risk - or the limit it waits for and until when."""
    side, price = s['side'], adv3.price
    head = f"#{s['id']} {DOT[side]} {s['coin']} {SIDE[side]} {adv3.ddmm(s['close_of'])}"
    if s['status'] == 'pending':
        return f"{head} · ждёт лимит {price(s['entry'])} до {bat(s['valid'])} · стоп {price(s['stop'])}"
    mark = (rows.get(s['coin']) or {}).get('mark')
    now = f" · сейчас {sg(side * (mark - s['fill']) / abs(s['entry'] - s['stop']), 1)} R" if mark else ''
    return (f"{head} · вход {price(s['fill'])} · стоп {price(s['stop'])}" + (f" · 🎯{s['hit']}" if s['hit'] else '') + now)


def ended_line(s):
    """One signal ended: number, coin, side, the close it is of; how it ended - the stop, the rule's exit at a close, after which
    target - when, its result in R and in USDT."""
    side, price = s['side'], adv3.price
    head = f"#{s['id']} {DOT[side]} {s['coin']} {SIDE[side]} {adv3.ddmm(s['close_of'])}"
    if s['status'] == 'expired':
        return f"{head} → ⌛ истёк {bat(s['exit_utc'])}: лимит {price(s['entry'])} не исполнен"
    how = '⛔ стоп' if s['why'] == 'stop' else ('🚪 выход по сигналу' if s['hit'] else '🚪 инвалидация — выход по сигналу')
    after = f" после цели {s['hit']}" if s['hit'] else ''
    return f"{head} → {how}{after} {bat(s['exit_utc'])} · {sg(s['R'])} R · {signed_usdt(s['pnl'])} USDT"


def event_lines(evs, reg):
    """The events a message announces, in time order, each with its signal, its price, its instant in Batumi and - an end - its
    result; a limit not filled says to take its order off where it was placed."""
    lines = ['🔔 <b>События</b> · время Батуми']
    price = adv3.price
    for e in evs:
        s = reg.sig.get(e['id'])
        if s is None:
            continue
        who = f"#{s['id']} {s['coin']} {SIDE[s['side']]}"
        if e['type'] == 'fill':
            lines.append(f"✅ {who} — лимит {price(e['price'])} исполнен {bat(e['utc'])}")
        elif e['type'] == 'target':
            lines.append(f"🎯 {who} — цель {e['k']} {price(e['price'])} достигнута {bat(e['utc'])}")
        elif e['type'] == 'stop':
            lines.append(f"⛔ {who} — стоп {price(e['price'])} {bat(e['utc'])} · {sg(e['R'])} R ({signed_usdt(e['pnl'])} USDT)"
                         + (f" · до этого цель {s['hit']}" if s['hit'] else ''))
        elif e['type'] == 'exit':
            day = (dt.datetime.fromisoformat(e['utc']) - dt.timedelta(days=1)).date()
            lines.append(f"🚪 {who} — сигнал закончился на закрытии {day:%d.%m}: выход {price(e['price'])} · {sg(e['R'])} R "
                         f"({signed_usdt(e['pnl'])} USDT)" + (f" · цели {s['hit']}" if s['hit'] else ''))
        elif e['type'] == 'expire':
            lines.append(f"⌛ {who} — лимит {price(s['entry'])} не исполнен до {bat(e['utc'])}: снять ордер, если выставлен")
    return lines


def risk_line(held, new, prm, labels=('открытые', 'новые')):
    """The model's risk at the stops: the signals held and the new ones, in percent of the capital, against the limit, what is left
    in percent and in USDT, and the split by side. held and new are {1: longs, -1: shorts}."""
    pct = adv3.pct
    h, n = held[1] + held[-1], new[1] + new[-1]
    total, free = h + n, max(0.0, prm['total'] - h - n)
    line = f"⚖️ Риск модели: {labels[0]} {pct(h)}%" + (f" + {labels[1]} {pct(n)}% = {pct(total)}%" if n else '')
    line += f" из {pct0(prm['total'])}% · свободно {pct(free)}% = {adv3.usdt(math.floor(free / 100 * prm['capital']))} USDT"
    longs, shorts = held[1] + new[1], held[-1] + new[-1]
    if longs and shorts:
        line += f" · ЛОНГ {pct(longs)}% · ШОРТ {pct(shorts)}%"
    elif total:
        line += ' · все в ' + ('ЛОНГ' if longs else 'ШОРТ')
    return line


def excluded_lines(excluded):
    """The coins not taken, grouped by their reason in the order the reasons first appear: one line a reason, each coin with its
    side's dot and its detail."""
    groups = {}
    for c, s, _code, why, detail in excluded:
        groups.setdefault(why, []).append(f"{DOT[s]}{c}" + (f" {detail}" if detail else ''))
    if not groups:
        return []
    return ['🚫 <b>Не берём</b>'] + [f"· {why} — {', '.join(coins)}" for why, coins in groups.items()]


def chain_line(reg):
    if reg.broken:
        return f"⚠️ Реестр: цепочка нарушена на событии {reg.broken} — записи с него не подтверждены"
    return f"🔐 Реестр: {len(reg.events)} {adv3.plural(len(reg.events), 'событие', 'события', 'событий')} · отпечаток {reg.head[:8]}"


def seed_line(reg, opened):
    """The first message after the registry's seed: what it took from the journal."""
    legacy = [s for s in reg.sig.values() if s.get('legacy')]
    live = sum(s['status'] in ('pending', 'open') for s in legacy)
    ended = sum(s['status'] == 'closed' for s in legacy)
    expired = sum(s['status'] == 'expired' for s in legacy)
    return (f"📒 Реестр создан: из журнала перенесено {opened} {adv3.plural(opened, 'STRONG-сигнал', 'STRONG-сигнала', 'STRONG-сигналов')}"
            f" — открыто {live}, завершено {ended}, истекло {expired}; подробности — «реестр»")


def note_lines(notes):
    return [f"ℹ️ #{i} {coin} {SIDE[side]} — больше не STRONG (сумма знаков {sg(ssum, 0)}, z {sg(z)}): по правилу "
            f"держать до стопа или смены сигнала" for i, coin, side, ssum, z in notes]


def zone_lines(zones):
    if not zones:
        return []
    price = adv3.price
    lines = ['<b>Зоны входа</b> — для тех, кто ещё не вошёл']
    for z in zones:
        lo, hi = z['zone']
        lines.append(f"#{z['id']} {z['coin']} {SIDE[z['side']]} — цена {price(z['mark'])} " + (
            f"ушла из зоны {price(lo)}–{price(hi)}: лимит {price(z['entry'])}, не догонять" if z['mode'] == 'limit'
            else f"у стопа {price(z['stop'])}: не входить"))
    return lines


def notes_of(rep, reg, cs):
    """The signals of earlier closes open or waiting whose coin was STRONG at the close before and is not at this one, its rule signal
    kept: information, never an exit (CANON PART VII). [(id, coin, side, sum, z)], by number."""
    last = dt.date.fromisoformat(rep['close_of'])
    out = []
    for s in reg.live():
        row = rep['rows'].get(s['coin']) or {}
        if s['close_of'] == rep['close_of'] or row.get('signal') != s['side'] or row.get('z') is None:
            continue
        if row.get('sum') == 4 * s['side'] and abs(row['z']) >= adv3.STRONG_Z:
            continue
        c = cs.get(s['coin']) or {}
        days = sorted(d for d in c if d <= last)
        if len(days) < 2 or days[-1] != last:
            continue
        st = adv3.strength(days, [c[d][3] for d in days], len(days) - 2)
        if st and st[1] == 4 * s['side'] and abs(st[0]) >= adv3.STRONG_Z:
            out.append((s['id'], s['coin'], s['side'], row['sum'], row['z']))
    return out


def zones_of(rep, reg):
    """This close's signals entered at market whose zone the price of the moment has left (TZ-39's zones): a limit at the zone's edge
    where it ran past it, no entry where it stands near the stop - for the Boss who has not entered yet."""
    out = []
    for s in reg.live():
        row = rep['rows'].get(s['coin']) or {}
        if s['close_of'] != rep['close_of'] or s['mode'] != 'market' or not rep['marks_ok'] or row.get('signal') != s['side']:
            continue
        cd = adv3.card(s['coin'], row, True, CAPITAL, adv3.RISK)
        if cd['mode'] != 'market':
            out.append({'id': s['id'], 'coin': s['coin'], 'side': s['side'], 'mode': cd['mode'], 'mark': cd['mark'],
                        'zone': list(cd['zone']), 'entry': cd['entry'], 'stop': cd['stop']})
    return out


def by_side(items):
    out = {1: 0.0, -1: 0.0}
    for it in items:
        if it.get('pos'):
            out[it['side']] += it['pos']['risk_pct']
    return out


def compose(slot, rep, reg, model, news, notes, zones, prev, now, new_ids, seeded=None):
    """(text, quiet, one line) of a check (TZ-42). It notifies only for a new signal or an end - a stop, an exit by the rule, a limit not
    filled. The signal check: the events, the new STRONG signals with their positions, the signals open with where each stands, the
    notes, the model's risk, the coins not taken and why, the registry's fingerprint - or one line where it finds no event, no new
    signal, no note and the coins not taken for the reasons of the check before. The fact check: the events, the new signals, the
    zones left and the risk - or one line where it finds none of them."""
    close = adv3.ddmm(rep['close_of'])
    new = sorted(model['new'], key=lambda x: x['rank'])
    loud = bool(new) or any(e['type'] in LOUD for e in news)
    held = model['risk']
    tail = f"активных {len(reg.live())} · риск {adv3.pct(held[1] + held[-1])}% из {pct0(RISK_TOTAL)}%"
    codes = sorted([c, s, code] for c, s, code, _why, _detail in model['excluded'])
    if slot[1] == 'signal':
        same = prev is not None and prev.get('excluded_codes') == codes
        if not news and not new and not notes and same and seeded is None:
            return (f"✓ {hhmm(now)} по Батуми · закрытие {close}: событий нет, новых STRONG нет · {tail} · 🔐 {len(reg.events)} · "
                    f"{reg.head[:8]}", True, True)
        lines = [f"🌅 <b>ADV-3 · проверка {hhmm(now)}</b> по Батуми · закрытие {close} (UTC)", params_line(DEFAULTS)]
    else:
        if not news and not new and not zones and seeded is None:
            return (f"✓ {hhmm(now)} по Батуми: событий нет · {tail} · следующая проверка {hhmm(next_at(now))}", True, True)
        lines = [f"🕖 <b>ADV-3 · проверка {hhmm(now)}</b> по Батуми · закрытие {close} (UTC)"]
    if not rep['marks_ok']:
        lines.append('⚠️ Текущие цены Binance недоступны: новых позиций нет')
    if seeded is not None:
        lines += ['', seed_line(reg, seeded)]
    if news:
        lines += [''] + event_lines(news, reg)
    if new:
        lines += ['', f"🆕 <b>Новые STRONG</b> — {len(new)} · риск по силе тренда, до 04:00 {dt.date.fromisoformat(rep['close_of']) + 2 * adv3.DAY:%d.%m}"]
        for k, it in enumerate(new, 1):
            lines += [''] + card_lines(it, k, new_ids.get(it['coin']))
    elif slot[1] == 'signal':
        lines += ['', '🆕 Новых STRONG нет']
    if slot[1] == 'signal':
        live = reg.live()
        if live:
            lines += ['', f"📂 <b>Открытые сигналы</b> — {len(live)}"] + [live_line(s, rep['rows']) for s in live]
        if notes:
            lines += note_lines(notes)
    if zones:
        lines += [''] + zone_lines(zones)
    lines += ['', risk_line(held, by_side(new), DEFAULTS)]
    if slot[1] == 'signal':
        lines += excluded_lines(model['excluded'])
    if new:
        lines.append(legend())
        if any(it['rank'] > adv3.TOP_N for it in new):
            lines.append(adv3.BEYOND)
    if slot[1] == 'signal':
        lines.append(chain_line(reg))
    lines += ['', footer()]
    return '\n'.join(lines), not loud, False


def signal_view(rep, reg, view, prm, now, new_ids, seeded=None):
    """The «сигнал» reply (TZ-42): the close, the parameters, the events not yet announced, the STRONG signals of this close - the
    registry's and the new - each with its position at the request's parameters, the signals open from earlier closes, the risk, the
    coins not taken and why."""
    close = adv3.ddmm(rep['close_of'])
    last = dt.date.fromisoformat(rep['close_of'])
    lines = [f"📊 <b>ADV-3 · STRONG</b> · {hhmm(now)} по Батуми", f"Закрытие {close} (UTC) · карточки до 04:00 {last + 2 * adv3.DAY:%d.%m}",
             params_line(prm)]
    if not rep['marks_ok']:
        lines.append('⚠️ Текущие цены Binance недоступны: позиции не рассчитаны')
    if seeded is not None:
        lines += ['', seed_line(reg, seeded)]
    news = [e for e in reg.events if e['n'] > reg.announced and e['type'] in SHOWN]
    if news:
        lines += [''] + event_lines(news, reg)
    items = view['items']
    if items:
        lines += ['', f"📌 <b>STRONG закрытия {close}</b> — {len(items)} · риск по силе тренда"]
        for k, it in enumerate(items, 1):
            lines += [''] + card_lines(it, k, new_ids.get(it['coin']), mark_new=True)
    else:
        lines += ['', f"📌 STRONG закрытия {close}: нет"]
    older = [s for s in reg.live() if s['close_of'] != rep['close_of']]
    if older:
        lines += ['', f"📂 <b>Открытые с прошлых закрытий</b> — {len(older)}"] + [live_line(s, rep['rows']) for s in older]
    lines += ['', risk_line(view['older'], by_side(items), prm, ('прошлые закрытия', 'это закрытие'))]
    lines += excluded_lines(view['excluded'])
    if items:
        lines.append(legend())
        if any(it['rank'] > adv3.TOP_N for it in items):
            lines.append(adv3.BEYOND)
    lines += ['', footer()]
    return '\n'.join(lines)


def wilson(k, n, z=1.96):
    """The 95 % Wilson interval of a share k of n, in percent: (low, high)."""
    p = k / n
    mid, half = p + z * z / (2 * n), z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return 100 * (mid - half) / (1 + z * z / n), 100 * (mid + half) / (1 + z * z / n)


T975 = (12.706, 4.303, 3.182, 2.776, 2.571, 2.447, 2.365, 2.306, 2.262, 2.228, 2.201, 2.179, 2.160, 2.145, 2.131, 2.120, 2.110,
        2.101, 2.093, 2.086, 2.080, 2.074, 2.069, 2.064, 2.060, 2.056, 2.052, 2.048, 2.045, 2.042)


def t975(df):
    """Student's t at 0.975 with df degrees of freedom: the table to 30, then the Cornish-Fisher expansion about the normal's 1.95996."""
    if df <= 30:
        return T975[df - 1]
    z = 1.959964
    return z + (z ** 3 + z) / (4 * df) + (5 * z ** 5 + 16 * z ** 3 + 3 * z) / (96 * df ** 2)


def mean_ci(xs):
    """(mean, low, high) of xs with Student's 95 % interval; the interval None below two values."""
    n = len(xs)
    m = sum(xs) / n
    if n < 2:
        return m, None, None
    sd = math.sqrt(sum((x - m) ** 2 for x in xs) / (n - 1))
    h = t975(n - 1) * sd / math.sqrt(n)
    return m, m - h, m + h


def stats_lines(reg, full=False):
    """The registry's figures over its ended signals (TZ-42): the targets reached, the stops before a target, the sum and mean of R
    with the mean's 95 % interval, the result in USDT and in percent of the default capital; full adds the targets against TZ-38's
    history with their Wilson intervals and the mean R by side, by the signal's age at its card and by BTC's signal. Descriptive: it
    moves no rung (CANON PART VII)."""
    closed = [s for _i, s in sorted(reg.sig.items()) if s['status'] == 'closed']
    n = len(closed)
    if not n:
        return ['Завершённых сделок пока нет — итогов нет.']
    pct, signed = adv3.pct, sg
    hits = {k: sum(s['hit'] >= k for s in closed) for k in (1, 2, 3)}
    stops = sum(s['why'] == 'stop' and not s['hit'] for s in closed)
    R = [s['R'] for s in closed]
    m, lo, hi = mean_ci(R)
    pnl = sum(s['pnl'] for s in closed)
    lines = [f"Закрыто {n}: 🎯1 {hits[1]} ({pct(100 * hits[1] / n, 0)}%) · 🎯2 {hits[2]} · 🎯3 {hits[3]} · стоп до цели {stops}",
             f"Сумма {signed(sum(R), 1)} R = {signed_usdt(pnl)} USDT ({signed(100 * pnl / CAPITAL)}% капитала) · средняя {signed(m)} R"
             + (f" (95%: {signed(lo)}…{signed(hi)})" if lo is not None else '')]
    if n < 30:
        lines.append(f"⚠️ {n} {adv3.plural(n, 'сделка', 'сделки', 'сделок')} — мало для выводов: интервал широк, уверенность не меняется")
    if not full:
        return lines
    mfe = adv3.PIT['strong']['mfe']
    lines.append('Цели против истории STRONG: ' + ' · '.join(
        f"🎯{k} {pct(100 * hits[k] / n, 0)}% (95%: {pct(wilson(hits[k], n)[0], 0)}–{pct(wilson(hits[k], n)[1], 0)}) — история "
        f"{pct(100 * mfe[k], 0)}%" for k in (1, 2, 3)))

    def group(title, key, names):
        parts = []
        for name, label in names:
            xs = [s['R'] for s in closed if key(s) == name]
            if xs:
                parts.append(f"{label} {len(xs)} · {signed(sum(xs) / len(xs))} R")
        return [f"{title}: " + '; '.join(parts)] if parts else []

    def age(s):
        try:
            days = (dt.date.fromisoformat(s['close_of']) - dt.date.fromisoformat(s['since'])).days
        except (TypeError, ValueError):
            return None
        return 'young' if days <= 3 else 'mid' if days <= 14 else 'old'

    lines += group('По стороне', lambda s: s['side'], ((1, 'ЛОНГ'), (-1, 'ШОРТ')))
    lines += group('По возрасту сигнала', age, (('young', '≤3 дн'), ('mid', '4–14 дн'), ('old', '>14 дн')))
    lines += group('По рынку (BTC)', lambda s: s.get('btc'), ((1, 'BTC в ЛОНГ'), (-1, 'BTC в ШОРТ'), (0, 'BTC вне рынка')))
    return lines


def registry_view(reg, rep, now):
    """The «реестр» reply (TZ-42): the counts, every signal open or waiting with where it stands, the last ten ended, the figures over
    the ended ones and the chain's state."""
    sigs = [s for _i, s in sorted(reg.sig.items())]
    live = reg.live()
    ended = sorted([s for s in sigs if s['status'] in ('closed', 'expired')], key=lambda s: s['exit_utc'], reverse=True)
    first = min((s['close_of'] for s in sigs), default=None)
    lines = [f"📒 <b>ADV-3 · реестр STRONG</b> · {hhmm(now)} по Батуми",
             f"Сигналов {len(sigs)}" + (f" с {adv3.ddmm(first)}" if first else '') + f" · открыто {len(live)} · закрыто "
             f"{sum(s['status'] == 'closed' for s in sigs)} · истекло {sum(s['status'] == 'expired' for s in sigs)}",
             '<i>Модель бота при капитале 200 000 USDT: рыночный вход — по цене карточки, лимит — когда цена его коснулась; не ваш счёт</i>']
    if live:
        lines += ['', '<b>Открытые</b>'] + [live_line(s, rep['rows']) for s in live]
    if ended:
        lines += ['', f"<b>Завершённые</b> — последние {min(10, len(ended))} из {len(ended)}"] + [ended_line(s) for s in ended[:10]]
    lines += ['', '<b>Итоги</b>'] + stats_lines(reg) + ['', chain_line(reg), '', footer()]
    return '\n'.join(lines)


def ranking_view(rep, reg, n):
    """The «рейтинг» reply (TZ-42): the rule's first n coins in its order, each with its side, strength, sum of signs, ★ where STRONG at
    any rank and its open signal's number; the day's changes; the others counted."""
    rows = rep['rows']
    order = ranked(rep)
    strong = set(strong_all(rep))
    live = {s['coin']: s['id'] for s in reg.live()}
    lines = [f"🏆 <b>ADV-3 · рейтинг правила</b> · закрытие {adv3.ddmm(rep['close_of'])} (UTC)", f"В рынке {len(order)} из {len(adv3.COINS)}", '']
    for k, coin in enumerate(order[:n], 1):
        r = rows[coin]
        lines.append(f"{k}. {DOT[r['signal']]} {coin} {SIDE[r['signal']]} · z {sg(r['z'])} · знаки {sg(r['sum'], 0)}"
                     + (' · ★' if coin in strong else '') + (f" · #{live[coin]}" if coin in live else ''))
    new, out_long, out_short, flips = adv3.changes(rep)
    word = {1: 'ЛОНГ', -1: 'ШОРТ'}
    parts = ([f"🆕 {', '.join(f'{c} {word[k]}' for c, k in new)}"] if new else []) \
        + ([f"🚪 {', '.join(out_long)} из лонга"] if out_long else []) + ([f"🚪 {', '.join(out_short)} из шорта"] if out_short else []) \
        + ([f"🔄 {', '.join(f'{c} в {word[k]}' for c, k in flips)}"] if flips else [])
    lines += ['', 'Изменения за день: ' + (' · '.join(parts) if parts else 'нет')]
    rest = [c for c in order[n:]]
    flat = sum(rows[c].get('signal') == 0 for c in adv3.COINS)
    young = sum(rows[c].get('signal') is None and not rows[c].get('missing') for c in adv3.COINS)
    lost = [c for c in adv3.COINS if rows[c].get('missing')]
    lines.append(f"Дальше в рынке {len(rest)} · вне рынка {flat} · мало истории {young}" + (f" · Binance не отдал: {', '.join(lost)}" if lost else ''))
    lines += ['<i>★ — STRONG: четыре знака совпадают и |z| ≥ 1; #N — открытый сигнал реестра; карточки и позиции — «сигнал»</i>', '', footer()]
    return '\n'.join(lines)


def assess_view(rep, reg):
    """The «оценка» reply: adv3's assessment - the rung, the next readings, the six ratings, the forward record, the history - and, since
    TZ-42, the registry's figures in full, which describe and move no rung."""
    return (adv3.assessment(rep, adv3.FACTS) + '\n\n<b>Реестр сигналов бота</b> — модель при капитале 200 000 USDT, не ваш счёт\n'
            + '\n'.join(stats_lines(reg, full=True)) + '\n<i>Рейтинг двигают только чтения форварда (после 28.10.2027) и PIT (после '
            '31.10.2027); реестр описывает, а не доказывает.</i>')


def check_record(slot, rep, reg, model, news, notes, zones, ids, quiet, one_line, opened, at, seeded=None):
    """The check's journal record (CANON PART VII's internal log; it measures and tunes nothing): every coin's signal, sum of signs,
    strength, rank, unit, close and mark; the coins STRONG at every rank; the new signals with their cards and positions; the coins
    not taken with their reasons and codes; the events announced; the notes and zones; the registry's open signals, risk, size,
    head and state; the six ratings."""
    rank = {coin: k for k, coin in enumerate(ranked(rep), 1)}
    new = sorted(model['new'], key=lambda x: x['rank'])
    rec = base_record('check', rep, ids, at)
    held = open_risk(reg)
    rec.update(slot=slot_text(slot), quiet=quiet, one_line=one_line,
               state={coin: {'signal': r.get('signal'), 'sum': r.get('sum'), 'z': r.get('z'), 'rank': rank.get(coin), 'U': r.get('U'),
                             'close': r.get('close'), 'mark': r.get('mark')} for coin, r in rep['rows'].items()},
               strong_all=strong_all(rep), cards=[item_record(it, i) for it, i in zip(new, opened or [None] * len(new))],
               excluded=[list(x) for x in model['excluded']], excluded_codes=sorted([c, s, code] for c, s, code, _w, _d in model['excluded']),
               events=[e['n'] for e in news], notes=[list(x) for x in notes], zones=zones, opened=opened,
               registry={'events': len(reg.events), 'head': reg.head, 'broken': reg.broken, 'open': [s['id'] for s in reg.live()],
                         'risk': held[1] + held[-1], 'seeded': seeded},
               params={k: DEFAULTS[k] for k in ('capital', 'risk', 'total', 'stop', 'n')}, trust=rep['trust'])
    return rec


def check(tg, data, reg, slot, now):
    """One scheduled check (TZ-42): the report at the model's defaults; the registry brought to now - seeded at its first check, every
    signal open or waiting walked on its candles; the model's new signals; the notes at the signal check and the zones left at
    the fact check; the message, sent quiet unless it holds a new signal or an end; then the new signals written - a signal exists once
    its message is sent - and the events counted announced; its record returned for the journal."""
    rep = live_report(data, CAPITAL, adv3.RISK)
    seeded = ensure(reg, data, now)
    model = model_plan(rep, reg, volumes(strong_all(rep), rep['made_at_ms']))
    news = [e for e in reg.events if e['n'] > reg.announced and e['type'] in SHOWN]
    notes = notes_of(rep, reg, data.cs) if slot[1] == 'signal' else []
    zones = zones_of(rep, reg) if slot[1] == 'fact' else []
    first = reg.next_id()
    new_ids = {it['coin']: first + k for k, it in enumerate(sorted(model['new'], key=lambda x: x['rank']))}
    text, quiet, one_line = compose(slot, rep, reg, model, news, notes, zones, last_check(), now, new_ids, seeded)
    ids = tg.send(text, quiet=quiet)
    opened = []
    try:
        opened = register(reg, rep, model['new'], now, 'check:' + slot_text(slot))
        reg.announced = len(reg.events)
        reg.save_state()
    except Exception:
        log('registry write failed\n' + traceback.format_exc())
    return check_record(slot, rep, reg, model, news, notes, zones, ids, quiet, one_line, opened, now, seeded)


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
    tg, data, reg = Telegram(token, chat), Data(), Registry(STATE)
    off_path, done_path = os.path.join(STATE, 'offset'), os.path.join(STATE, 'check-done')
    offset = int(read(off_path)) if os.path.exists(off_path) else 0
    done = slot_parse(read(done_path)) if os.path.exists(done_path) else None
    retry_at = 0.0
    log('serving the pinned chat: pid', os.getpid(), 'offset', offset, 'check-done', slot_text(done) if done else '-')
    log('registry:', len(reg.events), 'events,', len(reg.sig), 'signals,', len(reg.live()), 'open | head', reg.head[:12],
        '| torn', reg.torn, '| broken', reg.broken or '-')
    try:
        tg.call('setMyCommands', commands=COMMANDS)
    except Exception as e:
        log('setMyCommands refused:', repr(e)[:200])   # the menu is a convenience: the keyboard and the texts answer without it
    while True:
        now = dt.datetime.now(dt.timezone.utc)
        slot = due(now, done)
        if slot and time.time() >= retry_at:
            try:
                rec = check(tg, data, reg, slot, now)
            except Exception:
                retry_at = time.time() + RETRY
                log('check failed:', slot_text(slot), '- retry in', RETRY, 's\n' + traceback.format_exc())
            else:
                done = done_after(slot, dt.datetime.now(dt.timezone.utc))   # sent: never again, whatever its record does
                try:
                    put(done_path, slot_text(done))
                    append(rec)
                except Exception:
                    log('check record failed\n' + traceback.format_exc())
                log('check sent:', slot_text(slot), 'for the close of', rec['close_of'], '| events', len(rec['events']), '| new',
                    len(rec['opened']), '| quiet' if rec['quiet'] else '| loud', '| one line' if rec['one_line'] else '| full')
        now = dt.datetime.now(dt.timezone.utc)
        if due(now, done):
            wait = min(POLL, max(1, int(retry_at - time.time())))
        else:
            wait = min(POLL, max(1, int((next_at(now) - now).total_seconds())))
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
            handle(tg, data, reg, msg.get('text') or '')
        if updates:
            put(off_path, str(offset))


def handle(tg, data, reg, text):
    """One message of the Boss's (TZ-42): «сигнал» - the registry brought to now, the model's new signals, the request's plan sent,
    then the new ones it showed written; «реестр» and «оценка» - the registry brought to now and its view; «рейтинг» - the rule's
    order; anything else HELP. Every reply carries the keyboard and leaves one journal record."""
    cmd = route(text)
    try:
        if cmd is None or cmd[0] == 'help':
            tg.send(HELP, keyboard=True)
            log('help sent')
            return
        kind, arg = cmd
        now = dt.datetime.now(dt.timezone.utc)
        rep = live_report(data, CAPITAL, adv3.RISK)
        if kind == 'ranking':
            rec = base_record('ranking', rep, tg.send(ranking_view(rep, reg, arg), keyboard=True), now)
            rec['n'] = arg
        else:
            seeded = ensure(reg, data, now)
            if kind == 'signal':
                liq = volumes(strong_all(rep), rep['made_at_ms'])
                model = model_plan(rep, reg, liq)
                view = view_plan(rep, reg, liq, arg, model)
                shown = {it['coin'] for it in view['items'] if it['sig'] is None and it.get('pos')}
                new = sorted([it for it in model['new'] if it['coin'] in shown], key=lambda x: x['rank'])
                first = reg.next_id()
                new_ids = {it['coin']: first + k for k, it in enumerate(new)}
                ids = tg.send(signal_view(rep, reg, view, arg, now, new_ids, seeded), keyboard=True)
                opened = []
                try:
                    opened = register(reg, rep, new, now, 'request')
                    reg.announced = len(reg.events)
                    reg.save_state()
                except Exception:
                    log('registry write failed\n' + traceback.format_exc())
                rec = base_record('request', rep, ids, now)
                rec.update(params={k: arg[k] for k in ('capital', 'risk', 'total', 'stop', 'n', 'set')}, opened=opened,
                           cards=[item_record(it) for it in view['items']], excluded=[list(x) for x in view['excluded']])
            elif kind == 'registry':
                rec = base_record('registry', rep, tg.send(registry_view(reg, rep, now), keyboard=True), now)
            else:
                rec = base_record('assess', rep, tg.send(assess_view(rep, reg), keyboard=True), now)
                rec['trust'] = rep['trust']
            rec['seeded'] = seeded
        try:
            append(rec)
        except Exception:
            log('request record failed\n' + traceback.format_exc())
        log('request answered for the close of', rep['close_of'], '| kind', kind)
    except Exception:
        log('request failed\n' + traceback.format_exc())
        try:
            tg.send('Binance или Telegram не ответили — повторите через минуту.', keyboard=True)
        except Exception:
            log('apology failed\n' + traceback.format_exc())


def probe():
    """P-START: live requests through the process's own request functions, each asserted served and parsed - six endpoints, eight
    requests: the klines endpoint three times, for the closed daily candles and, since TZ-42, for the 5-minute candles of the last
    hour and the 1-minute ones of the last minutes, which the registry walks on; fundingRate, premiumIndex and fundingInfo once each;
    Telegram's getMe and, since TZ-42, getMyCommands. Prints counts, dates and the bot's name; never the token or a chat id."""
    now_ms = int(time.time() * 1000)
    today = dt.datetime.now(dt.timezone.utc).date()
    c = adv3.fapi_candles('BTCUSDT', now_ms)
    assert c and max(c) >= today - 2 * adv3.DAY and all(len(v) == 4 and v[3] > 0 for v in c.values()), 'klines'
    k5 = klines('BTC', ceil5(now_ms - 13 * K5_MS), now_ms)
    k1 = klines('BTC', ceil1(now_ms - 4 * K1_MS), now_ms, K1_MS, 4)
    for rows, step, lo in ((k5, K5_MS, 10), (k1, K1_MS, 3)):
        assert lo <= len(rows) <= (14 if step == K5_MS else 4) and all(
            len(x) == 6 and x[2] >= max(x[1], x[4]) and 0 < x[3] <= min(x[1], x[4]) for x in rows) \
            and all(a[0] + step == b[0] for a, b in zip(rows, rows[1:])) and all(x[5] for x in rows[:-1]), '%d-minute klines' % (step // K1_MS)
    print('P-KLINES served:', len(c), 'closed daily candles of BTCUSDT, the last', max(c), '-', len(k5), '5-minute candles of the last hour and',
          len(k1), '1-minute candles of the last minutes')
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
    tg = Telegram(read(TOKEN_FILE))
    me = tg.call('getMe')
    cmds = tg.call('getMyCommands')
    assert me.get('is_bot') is True and me.get('username') and isinstance(cmds, list), 'getMe, getMyCommands'
    print('P-TELEGRAM served: bot @' + me['username'] + ',', len(cmds), 'commands in its menu')
    print('READING P-START: served - 6 of 6 endpoints, 8 requests')


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
        'ADV-3 подключён к этому чату. Напишите «сигнал» — или ждите проверок в 04:10 и 19:07 по Батуми.', keyboard=True)
    assert ids and all(isinstance(x, int) for x in ids), ids
    print('G-HELLO sent: message ids', ids)


def selftest():
    """The bot's own checks, offline (TZ-42): the commands and their parameters, the keyboard, the schedule with its 15:07 slot, the
    registry's chain - written, read back, broken by an edit, a removal or a torn line - each signal's walk on 5-minute candles in
    hand-built cases, the position and the shares by hand, the candidates and the model's and a request's plans, the seed from a
    journal, the messages, and checks and requests end to end with Binance and Telegram stood in for; the stats by hand; the chunks,
    the files, the log, the HTML fallback and the quiet flag, the pace and the 429s, glibc. Every expectation is computed here by hand
    or by a formula of its own, never by the code under test."""
    import contextlib, io, random, shutil, tempfile
    done = []

    def chk(name, ok):
        done.append(name)
        assert ok, name

    # ---- the commands -----------------------------------------------------------------------------------------------
    def P(capital=200000.0, risk=0.5, total=10.0, stop=14.0, n=7, given=()):
        return {'capital': capital, 'risk': risk, 'total': total, 'stop': stop, 'n': n, 'set': sorted(given)}
    S_, A_, R_, H_ = 'signal', ('assess', None), ('registry', None), ('help', None)
    for text, want in (('сигнал', (S_, P())), ('Сигнал', (S_, P())), ('Сигнал 0,5%', (S_, P(risk=0.5, given=['risk']))),
                       ('signal 0.3', (S_, P(risk=0.3, given=['risk']))), ('сигналы', (S_, P())), ('сигнал топ 3', (S_, P(n=3, given=['n']))),
                       ('сигнал топ 10', (S_, P(n=7, given=['n']))), ('сигнал топ 0', (S_, P(n=1, given=['n']))), ('топ 5', (S_, P(n=5, given=['n']))),
                       ('сигнал 10000 топ 3', (S_, P(capital=10000.0, n=3, given=['capital', 'n']))),
                       ('Сигнал 15 000 топ 5 1', (S_, P(capital=15000.0, n=5, risk=1.0, given=['capital', 'n', 'risk']))),
                       ('сигнал 10к топ 3', (S_, P(capital=10000.0, n=3, given=['capital', 'n']))),
                       ('signal 15k top 5', (S_, P(capital=15000.0, n=5, given=['capital', 'n']))),
                       ('сигнал 1,5 тыс', (S_, P(capital=1500.0, given=['capital']))),
                       ('сигнал 150000 риск 0,75 лимит 8 стоп 12 топ 5',
                        (S_, P(capital=150000.0, risk=0.75, total=8.0, stop=12.0, n=5, given=['capital', 'n', 'risk', 'stop', 'total']))),
                       ('сигнал риск 2', (S_, P(risk=1.0, given=['risk']))), ('сигнал лимит 20', (S_, P(total=10.0, given=['total']))),
                       ('сигнал всего 6%', (S_, P(total=6.0, given=['total']))), ('сигнал стоп 20', (S_, P(stop=14.0, given=['stop']))),
                       ('сигнал стоп 1', (S_, P(stop=2.0, given=['stop']))), ('сигнал лимит 0,1', (S_, P(total=0.5, given=['total']))),
                       ('сигнал 50', (S_, P(risk=1.0, given=['risk']))), ('signal 200000000', (S_, P(capital=10_000_000.0, given=['capital']))),
                       ('сигнал 12000 0.01', (S_, P(capital=12000.0, risk=0.05, given=['capital', 'risk']))),
                       ('/signal@adv3_bot 5000 top 2', (S_, P(capital=5000.0, n=2, given=['capital', 'n']))),
                       ('топ 3 на 10000', (S_, P(capital=10000.0, n=3, given=['capital', 'n']))),
                       ('сигнал 100 топ 3', (S_, P(capital=100.0, n=3, given=['capital', 'n']))),
                       ('реестр', R_), ('Реестр', R_), ('/registry', R_), ('рейтинг', ('ranking', 7)), ('Рейтинг 15', ('ranking', 15)),
                       ('рейтинг 99', ('ranking', 42)), ('рейтинг 0', ('ranking', 1)), ('/ranking', ('ranking', 7)),
                       ('оценка', A_), ('Оценка', A_), ('/rating', A_), ('помощь', H_), ('Помощь', H_), ('/start', H_), ('help', H_), ('меню', H_),
                       ('привет', None), ('сигнализация', None), ('', None), ('12345', None), ('eth', None), ('оценочный', None)):
        chk(f'route {text!r}', route(text) == want)
    chk('HELP: the commands, the defaults, the overrides and their ceilings, the checks at 04:10 and 19:07 and the quiet rule, in one part',
        all(k in HELP for k in ('«Сигнал»', '«Реестр»', '«Рейтинг»', '«Оценка»', '200 000 USDT', 'не ваш баланс', '0,5%', '10%', '14%',
                                'до 7 новых', '«сигнал 50000 риск 0,75 лимит 8 стоп 12 топ 3»', 'только ужесточить', '04:10', '19:07',
                                'одной строкой')) and len(chunks(HELP)) == 1)
    chk('the keyboard: Сигнал and Реестр, then Рейтинг, Оценка and Помощь, each a command route reads; five menu commands',
        [[b['text'] for b in row] for row in KEYBOARD['keyboard']] == [['Сигнал', 'Реестр'], ['Рейтинг', 'Оценка', 'Помощь']]
        and [route(b['text'])[0] for row in KEYBOARD['keyboard'] for b in row] == ['signal', 'registry', 'ranking', 'assess', 'help']
        and [route('/' + c['command'])[0] for c in COMMANDS] == ['signal', 'registry', 'ranking', 'assess', 'help'])
    long_text = '\n'.join(f'line {i} ' + 'x' * 90 for i in range(200))
    parts = chunks(long_text)
    chk('chunks: 5 parts under the limit, joined back whole',
        len(parts) == 5 and all(len(p) <= LIMIT for p in parts) and '\n'.join(parts) == long_text)
    tmp = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'.selftest-{os.getpid()}')
    os.mkdir(tmp)
    try:
        f = os.path.join(tmp, 'offset')
        put(f, '41')
        put(f, '42')
        chk('put replaces in one rename', read(f) == '42' and sorted(os.listdir(tmp)) == ['offset'])
    finally:
        for name in os.listdir(tmp):
            os.remove(os.path.join(tmp, name))
        os.rmdir(tmp)

    # ---- Telegram -----------------------------------------------------------------------------------------------------
    slept, real_sleep = [], time.sleep
    time.sleep = slept.append       # the self-test never waits: each pause is recorded instead, and time.sleep restored at its end

    class Fake(Telegram):
        def __init__(self, busy=0, wait=7):
            super().__init__('123456:SECRET', 777)
            self.calls, self.busy, self.wait = [], busy, wait

        def call(self, method, http_timeout=30, **params):
            self.calls.append(params)
            if self.busy:
                self.busy -= 1
                raise TooMany(f'telegram sendMessage: 429 Too Many Requests: retry after {self.wait}', self.wait)
            if params.get('parse_mode') == 'HTML' and '<b>bad' in params.get('text', ''):
                raise RuntimeError("telegram sendMessage: 400 Bad Request: can't parse entities")
            return {'message_id': len(self.calls)}

    fk = Fake()
    chk('HTML sent as HTML, with a notification and no keyboard', fk.send('<b>ok</b>') == [1] and fk.calls[0]['parse_mode'] == 'HTML'
        and 'disable_notification' not in fk.calls[0] and 'reply_markup' not in fk.calls[0])
    chk('unparseable HTML resent as plain text', fk.send('<b>bad &amp; x</b>') == [3]
        and 'parse_mode' not in fk.calls[2] and fk.calls[2]['text'] == 'bad & x')
    n0 = len(fk.calls)
    fk.send('\n'.join(['q' * 3000, 'r' * 3000]), quiet=True)
    fk.send('<b>bad quiet</b>', quiet=True)
    chk('quiet: every part, the plain fallback among them, without a notification',
        len(fk.calls) == n0 + 4 and all(c.get('disable_notification') is True for c in fk.calls[n0:]))
    n0 = len(fk.calls)
    fk.send('\n'.join(['q' * 3000, 'r' * 3000, 's' * 3000]), keyboard=True)
    fk.send('<b>bad kb</b>', keyboard=True)
    chk('keyboard: on the last part alone, the plain fallback keeping it (TZ-42)',
        ['reply_markup' in c for c in fk.calls[n0:]] == [False, False, True, True, True] and fk.calls[-1]['reply_markup'] == KEYBOARD)
    del slept[:]
    fk.send('\n'.join(['q' * 3000, 'r' * 3000, 's' * 3000]))
    chk('pace: the parts of one message 1.1 s apart, none before the first (TZ-40)', slept == [1.1, 1.1] and PACE == 1.1)
    busy = Fake(busy=2)
    del slept[:]
    ids = busy.send('<b>one</b>', quiet=True)
    chk('429: a part refused as too many requests waits the retry_after named and a second more, and goes again, quiet still',
        ids == [3] and slept == [8, 8] and len(busy.calls) == 3 and all(c['text'] == '<b>one</b>' and c.get('disable_notification') is True
                                                                     for c in busy.calls))
    stuck, raised = Fake(busy=3), False
    try:
        stuck.send('x\n' + 'y' * 4000)
    except TooMany:
        raised = True
    chk('429: a part refused three times raises, and no later part is sent', raised and len(stuck.calls) == 3
        and all(c['text'] == 'x' for c in stuck.calls))
    del slept[:]
    Fake(busy=1, wait=600).send('z')
    chk('429: a retry_after above 60 s waits 61 s', slept == [61])
    real_open = urllib.request.urlopen

    def refuse(body):
        def opener(req, timeout=None):
            raise urllib.error.HTTPError(req.full_url, 429, 'x', {}, io.BytesIO(json.dumps(body).encode()))
        return opener
    got = []
    try:
        for body in ({'ok': False, 'error_code': 429, 'description': 'Too Many Requests: retry after 9', 'parameters': {'retry_after': 9}},
                     {'ok': False, 'error_code': 429, 'description': 'Too Many Requests'},
                     {'ok': False, 'error_code': 400, 'description': 'Bad Request'}):
            urllib.request.urlopen = refuse(body)
            try:
                Telegram('123456:SECRET', 777).call('sendMessage', text='x')
            except TooMany as e:
                got.append(('429', e.retry_after))
            except RuntimeError as e:
                got.append(('other', str(e)))
    finally:
        urllib.request.urlopen = real_open
    chk('call: a 429 raises TooMany with the retry_after named, 5 s where none is; another refusal a RuntimeError of its own',
        got == [('429', 9), ('429', 5), ('other', 'telegram sendMessage: 400 Bad Request')])
    SECRETS.append('123456:SECRET')
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        log('url https://api.telegram.org/bot123456:SECRET/getMe failed')
    SECRETS.remove('123456:SECRET')
    chk('the token never reaches the log', 'SECRET' not in buf.getvalue() and '<token>' in buf.getvalue())

    # ---- the schedule: 00:10 and 15:07 UTC --------------------------------------------------------------------------------
    X = dt.date(2026, 11, 5)
    at = lambda d, h, m, s=0: dt.datetime.combine(d, dt.time(h, m, s), tzinfo=dt.timezone.utc)
    sig, fac = (X, 'signal'), (X, 'fact')
    chk('the slots are 00:10 and 15:07 UTC, 04:10 and 19:07 in Batumi', SLOTS == (('signal', dt.time(0, 10)), ('fact', dt.time(15, 7)))
        and hhmm(at(X, 0, 10)) == '04:10' and hhmm(at(X, 15, 7)) == '19:07')
    chk('latest_slot: 00:09:59 is the day before\'s fact, 00:10 the signal, 15:06:59 still the signal, 15:07 the fact',
        [latest_slot(at(X, 0, 9, 59)), latest_slot(at(X, 0, 10)), latest_slot(at(X, 15, 6, 59)), latest_slot(at(X, 15, 7)),
         latest_slot(at(X, 23, 59, 59))] == [(X - adv3.DAY, 'fact'), sig, sig, fac, fac])
    chk('due: nothing done runs the day\'s signal, at 00:10 and at 16:00 alike (15:07 repeats 00:10)',
        due(at(X, 0, 10), None) == sig and due(at(X, 16, 0), None) == sig)
    chk('due: the signal done, nothing before 15:07, the fact at 15:07; the fact done, nothing until 00:10',
        due(at(X, 15, 6), sig) is None and due(at(X, 15, 7), sig) == fac and due(at(X, 23, 0), fac) is None
        and due(at(X + adv3.DAY, 0, 10), fac) == (X + adv3.DAY, 'signal'))
    chk('done_after: a signal ended before 15:07 is itself; at or after 15:07 it covers the fact; a fact is itself',
        done_after(sig, at(X, 0, 10, 30)) == sig and done_after(sig, at(X, 15, 7)) == fac and done_after(fac, at(X, 16, 0)) == fac)
    chk('next_at: 00:10, then 15:07, then 00:10 of the next day',
        [next_at(at(X, 0, 9)), next_at(at(X, 0, 10)), next_at(at(X, 15, 7)), next_at(at(X, 23, 0))]
        == [at(X, 0, 10), at(X, 15, 7), at(X + adv3.DAY, 0, 10), at(X + adv3.DAY, 0, 10)])
    chk('slot_text and slot_parse: a round trip, and nothing else parsed', slot_parse(slot_text(fac)) == fac
        and slot_parse('2026-11-05 daily') is None and slot_parse('garbage') is None and slot_parse('') is None)
    runs, d_, t = [], None, at(X, 13, 0)
    while t < at(X + 3 * adv3.DAY, 23, 59):
        s = due(t, d_)
        fail = s == (X + adv3.DAY, 'signal') and t < at(X + adv3.DAY, 15, 30)
        if s and not fail:
            runs.append((slot_text(s), t.strftime('%d %H:%M')))
            d_ = done_after(s, t)
        t += dt.timedelta(minutes=1)
    chk('three days minute by minute from a first start at 13:00: each slot once, a signal failing until 15:30 covering its fact',
        runs == [('2026-11-05 signal', '05 13:00'), ('2026-11-05 fact', '05 15:07'), ('2026-11-06 signal', '06 15:30'),
                 ('2026-11-07 signal', '07 00:10'), ('2026-11-07 fact', '07 15:07'), ('2026-11-08 signal', '08 00:10'),
                 ('2026-11-08 fact', '08 15:07')])

    # ---- the registry's chain ---------------------------------------------------------------------------------------------
    state = tempfile.mkdtemp(prefix='.selftest-', dir=os.path.dirname(os.path.abspath(__file__)))
    saved = (globals()['STATE'], adv3.fapi)
    try:
        when = at(X, 0, 10)
        rg = Registry(state)
        chk('an empty registry: no event, the genesis head, nothing announced', rg.events == [] and rg.head == '0' * 64 and rg.announced == 0
            and rg.next_id() == 1 and rg.live() == [])
        o1 = {'type': 'open', 'id': 1, 'utc': '2026-11-05T00:10:00+00:00', 'coin': 'ETH', 'side': 1, 'close_of': '2026-11-04', 'mode': 'limit',
              'entry': 100.0, 'stop': 90.0, 'targets': [110.0, 120.0, 130.0], 'valid': '2026-11-06T00:00:00+00:00', 'risk_pct': 0.5, 'qty': 10.0}
        rg.append({'type': 'seed', 'utc': '2026-11-05T00:10:00+00:00', 'cards': 0}, when)
        rg.append(o1, when)
        rg.append({'type': 'fill', 'id': 1, 'utc': '2026-11-05T01:00:00+00:00', 'price': 100.0}, when)
        raw = open(os.path.join(state, REG_FILE), 'rb').read().split(b'\n')
        hs = [hashlib.sha256(x).hexdigest() for x in raw[:3]]
        lines3 = [json.loads(x) for x in raw[:3]]
        chk('append: one line an event, numbered 1 to 3, each prev the SHA-256 of the line before, the first the genesis; the head the last\'s',
            raw[3] == b'' and [x['n'] for x in lines3] == [1, 2, 3] and [x['prev'] for x in lines3] == ['0' * 64, hs[0], hs[1]]
            and rg.head == hs[2] and all(x['at'] == '2026-11-05T00:10:00+00:00' for x in lines3)
            and raw[1] == json.dumps(lines3[1], ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode())
        chk('apply: the limit\'s signal waits, then its fill opens it', rg.sig[1]['status'] == 'open' and rg.sig[1]['fill'] == 100.0
            and status_of(rg.sig[1]) == 'ACTIVE' and [s['id'] for s in rg.live()] == [1] and rg.next_id() == 2)
        rg.cursor[1] = {'t': 5, 'b': 4, 'mfe': 0.5}
        rg.announced = 2
        rg.save_state()
        rb = Registry(state)
        chk('read back: the same events, signals, head, places and announced; no break, nothing torn',
            rb.events == rg.events and rb.sig == rg.sig and rb.head == rg.head and rb.cursor == {1: {'t': 5, 'b': 4, 'mfe': 0.5}}
            and rb.announced == 2 and rb.broken is None and rb.torn == 0)
        path = os.path.join(state, REG_FILE)
        good = open(path, 'rb').read()
        open(path, 'wb').write(good.replace(b'"entry":100.0', b'"entry":101.0', 1))
        chk('an edited line breaks the chain at the line after it', Registry(state).broken == 3)
        lines_ = good.split(b'\n')
        open(path, 'wb').write(b'\n'.join([lines_[0], lines_[2], b'']))
        chk('a removed line breaks the chain where it was', Registry(state).broken == 2)
        open(path, 'wb').write(b'\n'.join([lines_[0], b'not json', lines_[1], lines_[2], b'']))
        chk('a line that does not parse breaks the chain there', Registry(state).broken == 2)
        open(path, 'wb').write(good + b'{"type":"targ')
        rt = Registry(state)
        chk('a torn last line - a write cut short - is cut at load, its bytes counted, the chain whole',
            rt.torn == 13 and open(path, 'rb').read() == good and rt.broken is None and len(rt.events) == 3)
        os.remove(os.path.join(state, REG_STATE))
        chk('the state lost: the places rebuilt from each issue, every event counted announced', Registry(state).announced == 3
            and Registry(state).cursor_of(rg.sig[1]) == {'t': ceil1(from_iso('2026-11-05T00:10:00+00:00')), 'b': from_iso('2026-11-05T00:10:00+00:00'),
                                                          'mfe': 0.0})
        for name in os.listdir(state):
            os.remove(os.path.join(state, name))

        # ---- a signal's walk on 5-minute candles: cases by hand ------------------------------------------------------------
        d0 = dt.date(2026, 6, 1)
        rise = [100 * 1.01 ** i for i in range(150)]

        def daily(closes, start=d0):
            out, prev = {}, closes[0]
            for i, cl in enumerate(closes):
                out[start + i * adv3.DAY] = (prev, max(prev, cl) * 1.001, min(prev, cl) * 0.999, cl)
                prev = cl
            return out

        DD = d0 + 149 * adv3.DAY           # the card's close
        issue = day_ms(DD + adv3.DAY) + 600_000          # 00:10 of the day after it
        c_up = daily(rise + [rise[-1] * 1.01 ** k for k in range(1, 30)])

        def S(side=1, mode='market', E=100.0, stop=None, T=None, hit=0, status=None, fill=None, fill_utc=None, i=7, qty=10.0):
            stop = E - side * 10 if stop is None else stop
            T = [E + side * k * 10 for k in (1, 2, 3)] if T is None else T
            return {'id': i, 'coin': 'ETH', 'side': side, 'close_of': str(DD), 'utc': iso(issue), 'mode': mode, 'entry': E, 'stop': stop,
                    'targets': T, 'valid': iso(day_ms(DD + 2 * adv3.DAY)), 'qty': qty, 'hit': hit,
                    'status': status or ('open' if mode == 'market' else 'pending'), 'fill': fill if fill is not None else (E if mode == 'market' else None),
                    'fill_utc': fill_utc or (iso(issue) if mode == 'market' else None)}

        def K(*rows, start=None, closed=True):
            t0 = ceil5(issue) if start is None else start
            return [(t0 + k * K5_MS, *r, closed) for k, r in enumerate(rows)]

        cur0 = {'t': ceil5(issue), 'b': issue, 'mfe': 0.0}
        zero = lambda d: 0.0
        kinds = lambda evs: [(e['type'], e.get('k'), e.get('price')) for e in evs]
        k1 = K((100, 105, 98, 104), (104, 111, 103, 110), (110, 121, 108, 120), (120, 121, 89, 95))
        ev1, cur1 = walk(S(), cur0, c_up, zero, k1)
        chk('walk: a long reaches its first target, then its second, then its stop: two targets and a stop at 90, -1.019 R, -101.9 USDT',
            kinds(ev1) == [('target', 1, 110), ('target', 2, 120), ('stop', None, 90)] and [e['utc'] for e in ev1] == [iso(k1[i][0]) for i in (1, 2, 3)]
            and abs(ev1[2]['R'] - (-10 - 0.001 * 190) / 10) < 1e-12 and abs(ev1[2]['pnl'] - (-10.19 * 10)) < 1e-9)
        ev2, _c = walk(S(), cur0, c_up, zero, K((100, 111, 89, 95)))
        chk('walk: a candle reaching a target and the stop is the stop alone', kinds(ev2) == [('stop', None, 90)])
        ev3, _c = walk(S(), cur0, c_up, zero, K((85, 86, 80, 82)))
        chk('walk: a candle opening beyond the stop ends at its open: 85, -1.5185 R',
            kinds(ev3) == [('stop', None, 85)] and abs(ev3[0]['R'] - (-15 - 0.001 * 185) / 10) < 1e-12)
        ev4, _c = walk(S(), cur0, c_up, zero, K((112, 113, 89, 95)))
        chk('walk: a candle opening past a target credits it, then reaches the stop', kinds(ev4) == [('target', 1, 110), ('stop', None, 90)])
        ev5, _c = walk(S(side=-1), cur0, c_up, zero, K((100, 102, 95, 96), (96, 97, 89, 90), (90, 92, 79, 80), (80, 111, 79, 105)))
        chk('walk: a short mirrored - two targets, then its stop at 110', kinds(ev5) == [('target', 1, 90), ('target', 2, 80), ('stop', None, 110)])
        k6 = K((105, 106, 101, 102), (102, 103, 99, 100), (100, 109, 99, 108))
        ev6, cur6 = walk(S(mode='limit'), cur0, c_up, zero, k6)
        chk('walk: a waiting limit fills on the candle that reaches it, at the limit; the place after the last closed candle',
            kinds(ev6) == [('fill', None, 100.0)] and ev6[0]['utc'] == iso(k6[1][0]) and cur6['t'] == k6[2][0] + K5_MS)
        ev7, _c = walk(S(mode='limit'), cur0, c_up, zero, K((98, 99, 97, 98)))
        chk('walk: a candle opening past the limit fills it at its open, 98', kinds(ev7) == [('fill', None, 98)])
        ev8, _c = walk(S(mode='limit'), cur0, c_up, zero, K((101, 101, 89, 90)))
        chk('walk: the candle that fills a limit and reaches the stop ends it at the stop - R on the planned risk',
            kinds(ev8) == [('fill', None, 100.0), ('stop', None, 90)] and abs(ev8[1]['R'] - (-10 - 0.001 * 190) / 10) < 1e-12)
        flat = K(*[(105, 105.5, 104.5, 105)] * 300)
        ev9, cur9 = walk(S(mode='limit'), cur0, {}, zero, flat)
        chk('walk: a limit not reached by its validity, the close after the card\'s, expires there - daily candles or not',
            kinds(ev9) == [('expire', None, None)] and ev9[0]['utc'] == iso(day_ms(DD + 2 * adv3.DAY)))
        # the rule's exit at a close: the sum of signs of the daily closes, written here
        fall = rise + [rise[-1] * 0.98 ** k for k in range(1, 40)]
        c_fall = daily(fall)

        def sum_signs(closes, i):
            return sum((closes[i] > closes[i - L]) - (closes[i] < closes[i - L]) for L in (14, 28, 56, 112))
        x_i = next(i for i in range(150, len(fall)) if sum_signs(fall, i) < 2)
        E_ = fall[149]
        n_c = (x_i - 149 + 2) * 288
        kx = K(*[(E_, E_ * 1.0001, E_ * 0.9999, E_)] * n_c)
        sx = S(E=E_, stop=E_ * 0.5, T=[E_ * 2, E_ * 3, E_ * 4])
        evx, curx = walk(sx, cur0, c_fall, lambda d: 0.0003, kx)
        fund_ = sum(0.0003 * fall[i] for i in range(150, x_i + 1))
        Rx = ((fall[x_i] - E_) - 0.001 * (E_ + fall[x_i]) - fund_) / (E_ * 0.5)
        chk('walk: a long ends at the first close whose sum of signs is below +2, at that close, the funding of every close held paid',
            kinds(evx) == [('exit', None, fall[x_i])] and evx[0]['utc'] == iso(day_ms(d0 + x_i * adv3.DAY) + DAY_MS)
            and abs(evx[0]['R'] - Rx) < 1e-12 and curx['b'] == day_ms(d0 + x_i * adv3.DAY) + DAY_MS)
        k10 = K((100, 105, 98, 104)) + K((104, 111, 103, 110), start=ceil5(issue) + K5_MS, closed=False)
        ev10, cur10 = walk(S(), cur0, c_up, zero, k10)
        k10b = K((100, 105, 98, 104), (104, 112, 103, 111))
        ev10b, cur10b = walk(S(hit=1), cur10, c_up, zero, k10b)
        chk('walk: a candle not yet closed is read - its target credited - and not walked past; walked again closed, nothing twice',
            kinds(ev10) == [('target', 1, 110)] and cur10['t'] == k10[1][0] and ev10b == [] and cur10b['t'] == k10b[1][0] + K5_MS)
        ev11, cur11 = walk(S(mode='limit'), cur0, c_up, zero, k6, until=k6[1][0] + K5_MS - 1)
        chk('walk: until stops it before the candle that closes after it', ev11 == [] and cur11['t'] == k6[1][0])
        # the first minutes: a signal issued at 00:10:20 is walked on 1-minute candles from 00:11 to 00:15, then on 5-minute ones
        issue2 = issue + 20_000
        cur2 = {'t': ceil1(issue2), 'b': issue2, 'mfe': 0.0}
        M = lambda *rows, closed=True: [(ceil1(issue2) + k * K1_MS, *r, closed) for k, r in enumerate(rows)]
        S2 = lambda **kw: dict(S(**kw), utc=iso(issue2), fill_utc=iso(issue2) if kw.get('mode', 'market') == 'market' else None)
        k5b = K((100, 111, 99, 110), start=ceil5(issue2))
        ev12, cur12 = walk(S2(), cur2, c_up, zero, k5b, k1=M((100, 101, 99, 100), (100, 100, 89, 91)))
        chk('walk: the first minutes on 1-minute candles - the stop in the minute 00:12, the 5-minute candle of 00:15 never read',
            kinds(ev12) == [('stop', None, 90)] and ev12[0]['utc'] == iso(ceil1(issue2) + K1_MS) and ceil5(issue2) == issue + K5_MS)
        ev13, cur13 = walk(S2(), cur2, c_up, zero, k5b, k1=M(*[(100, 101, 99, 100)] * 4))
        chk('walk: four quiet minutes to the boundary, then the 5-minute candle of 00:15 reaching target 1; the place after it',
            kinds(ev13) == [('target', 1, 110)] and ev13[0]['utc'] == iso(ceil5(issue2)) and cur13['t'] == ceil5(issue2) + K5_MS)
        k14 = M((100, 100.5, 99.8, 100), (100, 100, 99.4, 99.6)) + [(ceil1(issue2) + 2 * K1_MS, 99.6, 100, 99.5, 99.9, False)]
        ev14, cur14 = walk(S2(mode='limit', E=99.5), cur2, c_up, zero, [], k1=k14)
        chk('walk: a limit filled in its first minutes, at the minute that reached it; the place at the minute not yet closed',
            kinds(ev14) == [('fill', None, 99.5)] and ev14[0]['utc'] == iso(ceil1(issue2) + K1_MS) and cur14['t'] == ceil1(issue2) + 2 * K1_MS)
        ev15, cur15 = walk(S2(), cur2, c_up, zero, k5b, until=ceil1(issue2) + 2 * K1_MS + 1, k1=M(*[(100, 101, 99, 100)] * 4))
        chk('walk: until inside the first minutes stops at the minute closing after it', ev15 == [] and cur15['t'] == ceil1(issue2) + 2 * K1_MS)
        rgw, asked = Registry(state), []

        def fake_r(path, **p_):
            step = K1_MS if p_['interval'] == '1m' else K5_MS
            asked.append((p_['symbol'][:-4], step, int(p_['startTime']), int(p_['limit'])))
            t_, out = int(p_['startTime']), []
            while len(out) < int(p_['limit']) and t_ <= issue + 30 * K1_MS:
                out.append([t_, '100', '100.1', '99.9', '100', '0', t_ + step - 1, '0'])
                t_ += step
            return out
        adv3.fapi = fake_r
        for i_, coin_, at_ in ((1, 'ETH', issue), (2, 'SOL', issue2)):
            rgw.append(dict(S(i=i_, qty=1.0), type='open', coin=coin_, utc=iso(at_)), dt.datetime.now(dt.timezone.utc))
            rgw.append({'type': 'fill', 'id': i_, 'utc': iso(at_), 'price': 100.0}, dt.datetime.now(dt.timezone.utc))
            rgw.cursor[i_] = {'t': ceil1(at_), 'b': at_, 'mfe': 0.0}
        reconcile(rgw, {}, {}, issue + 30 * K1_MS + 1, dt.datetime.now(dt.timezone.utc))
        first_asked = list(asked)
        reconcile(rgw, {}, {}, issue + 30 * K1_MS + 1, dt.datetime.now(dt.timezone.utc))
        chk('reconcile: the signal issued at 00:10:20 asks its four minutes, 00:11 to 00:15, once, beside its coin\'s 5-minute candles from '
            '00:15; the one issued at 00:10 asks none; coins in the rule\'s order; walked, both places at the candle not yet closed, 00:40',
            first_asked == [('SOL', K5_MS, ceil5(issue2), K5_PAGE), ('SOL', K1_MS, ceil1(issue2), 4), ('ETH', K5_MS, issue, K5_PAGE)]
            and asked[3:] == [('SOL', K5_MS, issue + 6 * K5_MS, K5_PAGE), ('ETH', K5_MS, issue + 6 * K5_MS, K5_PAGE)]
            and rgw.cursor[1]['t'] == rgw.cursor[2]['t'] == issue + 6 * K5_MS)
        asked.clear()
        none_ = klines('ETH', issue + 31 * K1_MS, issue + 30 * K1_MS + 1) + klines('ETH', issue + 31 * K1_MS, issue + 30 * K1_MS + 1, K1_MS, 4)
        chk('klines: a start after the moment asks nothing - a signal issued this minute waits for its first candle, no request made', none_ == [] and asked == [])
        for name in os.listdir(state):
            os.remove(os.path.join(state, name))

        # ---- the position, the shares, the plans -------------------------------------------------------------------------
        card8 = {'stop_pct': 8.0, 'leverage': 7, 'entry': 100.0}
        p8, _w = position(card8, 0.5, 200000.0, None)
        chk('position: 0.5 % at an 8 % stop is 12,195 USDT at the rule\'s 7x, margin 1,743, loss 999.99 with both sides\' costs',
            (p8['notional'], p8['leverage'], p8['margin']) == (12195, 7, 1743) and abs(p8['loss'] - 12195 * 0.082) < 1e-9
            and abs(p8['qty'] - 121.95) < 1e-12 and not p8['capped'] and not p8['over'] and not p8['cut'])
        p12, _w = position({'stop_pct': 12.0, 'leverage': 5, 'entry': 50.0}, 0.25, 200000.0, None)
        chk('position: 0.25 % at a 12 % stop is 4,098 USDT; the leverage lowered from 5x to 4x so the margin, 1,025, stays above 1,000',
            (p12['notional'], p12['leverage'], p12['lmax'], p12['margin']) == (4098, 4, 5, 1025))
        p05, w05 = position({'stop_pct': 12.0, 'leverage': 5, 'entry': 50.0}, 0.05, 200000.0, None)
        chk('position: 819 USDT is under the margin\'s floor and no position - the risk is never raised to meet it',
            p05 is None and w05 == 'позиция меньше минимальной маржи 1 000 USDT')
        pl, _w = position(card8, 0.5, 200000.0, 1_000_000.0)
        pv, wv = position(card8, 0.5, 200000.0, 100_000.0)
        chk('position: at most 0.5 % of the coin\'s daily volume - 5,000 USDT of 1,000,000 - at 5x for a margin of 1,000, and says so; '
            '500 USDT of 100,000 is under the margin\'s floor, by the liquidity',
            (pl['notional'], pl['leverage'], pl['margin'], pl['capped']) == (5000, 5, 1000, True) and abs(pl['loss'] - 410) < 1e-9
            and pv is None and wv == 'позиция меньше минимальной маржи 1 000 USDT — по ликвидности')
        pc, _w = position({'stop_pct': 5.0, 'leverage': 1, 'entry': 10.0}, 1.0, 200000.0, None)
        pc2, _w = position({'stop_pct': 5.0, 'leverage': 1, 'entry': 10.0}, 1.0, 12345.67, None)
        chk('position: a margin above 4 % of the capital is cut to 8,000 USDT, beyond the 3.5 % of 7,000 an exception; at 12,345.67 USDT '
            'to 493, the whole USDT within 4 %',
            (pc['notional'], pc['margin'], pc['cut'], pc['over']) == (8000, 8000, True, True)
            and (pc2['notional'], pc2['margin'], pc2['leverage'], pc2['cut']) == (493, 493, 1, True))
        chk('position: a rule leverage under 1x is no position', position({'stop_pct': 70.0, 'leverage': 0, 'entry': 1.0}, 0.5, 200000.0, None)[0] is None)

        def card_z(z, stop_pct=8.0, lev=7):
            return {'z': z, 'stop_pct': stop_pct, 'leverage': lev, 'entry': 100.0}
        its = [{'coin': c, 'side': 1, 'rank': k, 'card': card_z(z), 'sig': None, 'why': None} for k, (c, z) in enumerate((('ETH', 3.5), ('SOL', 2.0), ('XRP', 1.0)), 1)]
        allocate(its, DEFAULTS, 10.0, {})
        want = [3 * 0.5 * q / 6 for q in (3, 2, 1)]
        chk('allocate: shares min(|z|, 3) of 6 - a half, a third, a sixth - of three times 0.5 %: 0.75, 0.5 and 0.25 %, the strongest the most',
            [round(it['pos']['want'], 12) for it in its] == [round(x, 12) for x in want]
            and [it['pos']['notional'] for it in its] == [math.floor(w / 100 * 200000 / 0.082) for w in want])
        its2 = [{'coin': c, 'side': 1, 'rank': k, 'card': card_z(z), 'sig': None, 'why': None} for k, (c, z) in enumerate((('ETH', 3.5), ('SOL', 2.0), ('XRP', 1.0)), 1)]
        allocate(its2, DEFAULTS, 1.0, {})
        first_r = math.floor(0.75 / 100 * 200000 / 0.082) * 0.082 / 2000
        chk('allocate: a room of 1 % - the first its 0.75 %, the second the rest and marked short, the third the room\'s reason',
            abs(its2[0]['pos']['risk_pct'] - first_r) < 1e-12 and its2[1]['pos']['short'] is True
            and its2[1]['pos']['notional'] == math.floor((1.0 - first_r) / 100 * 200000 / 0.082)
            and its2[2].get('pos') is None and its2[2]['code'] == 'room' and its2[2]['why'] == 'лимит общего риска 10% исчерпан')
        its3 = [{'coin': adv3.COINS[k], 'side': 1, 'rank': k + 1, 'card': card_z(z), 'sig': None, 'why': None} for k, z in enumerate((3, 1, 1, 1, 1, 1, 1))]
        allocate(its3, DEFAULTS, 10.0, {})
        chk('allocate: seven trades, one of strength 3 and six of 1 - the first 7 x 0.5 % x 3/9, capped at the rule\'s 1 %, the others 0.39 %',
            its3[0]['pos']['want'] == 1.0 and all(abs(it['pos']['want'] - 7 * 0.5 / 9) < 1e-12 for it in its3[1:]))
        rnd, bad = random.Random(42), []
        for trial in range(300):
            k = rnd.randint(1, 9)
            zs = sorted((rnd.uniform(1.0, 5.0) for _ in range(k)), reverse=True)
            prm = dict(DEFAULTS, capital=rnd.choice((10000.0, 12345.67, 50000.0, 200000.0, 1e6)), risk=rnd.choice((0.05, 0.25, 0.5, 1.0)))
            room = rnd.choice((10.0, 3.0, 0.7, 0.01))
            vol = {adv3.COINS[i]: rnd.choice((None, 2e5, 5e6, 1e9)) for i in range(k)}
            items_ = []
            for i, z in enumerate(zs):
                sp = rnd.uniform(1.0, 14.0)
                items_.append({'coin': adv3.COINS[i], 'side': 1, 'rank': i + 1, 'sig': None, 'why': None,
                               'card': {'z': z, 'stop_pct': sp, 'leverage': min(20, math.floor(1 / (1.5 * sp / 100 + 0.01))), 'entry': 3.0}})
            allocate(items_, prm, room, vol)
            placed = [it for it in items_ if it.get('pos')]
            wants = [it['pos']['want'] for it in placed]
            cap_ = prm['capital']
            ok = (all(a >= b - 1e-12 for a, b in zip(wants, wants[1:])) and sum(it['pos']['risk_pct'] for it in placed) <= room + 1e-9
                  and all(it['pos']['risk_pct'] <= 1.0 + 1e-9 for it in placed)
                  and all(MARGIN_MIN / 100 * cap_ - 1e-9 <= it['pos']['margin'] <= MARGIN_EXC / 100 * cap_
                          and 1 <= it['pos']['leverage'] <= it['card']['leverage'] and it['pos']['margin'] * it['pos']['leverage'] >= it['pos']['notional']
                          and float(it['pos']['notional']).is_integer() for it in placed)
                  and all((not vol.get(it['coin'])) or it['pos']['notional'] <= LIQ_FRAC * vol[it['coin']] + 1e-9 for it in placed)
                  and all(abs(it['pos']['loss'] - it['pos']['notional'] * (it['card']['stop_pct'] / 100 + 0.002)) < 1e-6 for it in placed)
                  and all(it.get('code') in ('room', 'margin') for it in items_ if not it.get('pos')))
            if not ok:
                bad.append(trial)
        chk('allocate over 300 random scenarios: wanted risk never rising with rank, each within 1 %, all within the room; margin within 0.5 '
            'and 4 % of the capital and covering the position, leverage 1 to the rule\'s, whole USDT, the liquidity cap; a reason for each left out',
            not bad)

        # a report of synthetic rows: the plans
        CL = '2026-11-04'
        base_rows = {c: {'signal': None} for c in adv3.COINS}

        def row(side, z, ssum=None, U=8.0, mark=100.0):
            return {'signal': side, 'z': z * side, 'sum': (4 if ssum is None else ssum) * side, 'U': U, 'close': 100.0, 'prev': side,
                    'since': '2026-10-20', 'stop': 100.0 - side * U, 'mark': mark, 'funding': 0.0001, 'funding_h': 8}
        spec = {'ETH': row(1, 3.2), 'SOL': row(1, 2.6), 'XRP': row(-1, 2.4, U=16.0), 'ADA': row(1, 2.2, mark=92.5), 'BNB': row(1, 2.05, ssum=2),
                'AVAX': row(1, 1.9), 'LINK': row(1, 1.8), 'XMR': row(1, 1.7), 'NEAR': row(1, 1.6), 'HBAR': row(1, 1.5), 'ENA': row(1, 1.4),
                'UNI': row(1, 1.3), 'ARB': row(1, 1.25), 'ZEC': row(1, 1.2), 'HYPE': row(1, 1.1), 'SUI': row(1, 1.05), 'LTC': row(1, 0.8)}
        rep = {'rule': adv3.RULE, 'close_of': CL, 'deposit': CAPITAL, 'risk_pct': 0.5, 'marks_ok': True, 'made_at_ms': 0,
               'rows': dict(base_rows, **spec), 'top': ['ETH', 'SOL', 'XRP'], 'strong': ['ETH', 'SOL', 'XRP'], 'cards': [], 'trust': {}}
        order_hand = ['ETH', 'SOL', 'XRP', 'ADA', 'BNB', 'AVAX', 'LINK', 'XMR', 'NEAR', 'HBAR', 'ENA', 'UNI', 'ARB', 'ZEC', 'HYPE', 'SUI', 'LTC']
        chk('the synthetic report: the rule\'s order by |z|, STRONG at every rank all but BNB (sum 2) and LTC (|z| 0.8)',
            ranked(rep) == order_hand and strong_all(rep) == [c for c in order_hand if c not in ('BNB', 'LTC')])
        rg = Registry(state)
        mk = lambda i, coin, close_of, risk=0.5: {'type': 'open', 'id': i, 'utc': '2026-11-01T00:10:00+00:00', 'coin': coin, 'side': 1,
                                                 'close_of': close_of, 'mode': 'market', 'entry': 100.0, 'stop': 92.0, 'targets': [108.0, 116.0, 124.0],
                                                 'valid': '2026-11-06T00:00:00+00:00', 'risk_pct': risk, 'qty': 1.0}
        rg.append(mk(1, 'XMR', '2026-10-31'), when)
        rg.append({'type': 'fill', 'id': 1, 'utc': '2026-11-01T00:10:00+00:00', 'price': 100.0}, when)
        rg.append(mk(2, 'LINK', CL), when)
        rg.append({'type': 'fill', 'id': 2, 'utc': '2026-11-05T00:10:00+00:00', 'price': 100.0}, when)
        rg.append(mk(3, 'NEAR', CL), when)
        rg.append({'type': 'fill', 'id': 3, 'utc': '2026-11-05T00:10:00+00:00', 'price': 100.0}, when)
        rg.append({'type': 'stop', 'id': 3, 'utc': '2026-11-05T02:00:00+00:00', 'price': 92.0, 'R': -1.02, 'pnl': -8.16}, when)
        mine, new, excl = candidates(rep, rg, DEFAULTS)
        chk('candidates: this close\'s open LINK is the registry\'s; XMR, open from an earlier close, is the open list\'s; NEAR ended this close; '
            'XRP\'s stop 16 % and ADA at its stop are named; the rest new, in the rule\'s order',
            [it['coin'] for it in mine] == ['LINK'] and mine[0]['sig']['id'] == 2
            and [it['coin'] for it in new] == ['ETH', 'SOL', 'AVAX', 'HBAR', 'ENA', 'UNI', 'ARB', 'ZEC', 'HYPE', 'SUI']
            and [(c, code) for c, _s, code, _w, _d in excl] == [('XRP', 'stop'), ('ADA', 'near'), ('NEAR', 'ended')]
            and excl[0][3:] == ('стоп дальше 14%', '16,0%') and excl[2][4] == '#3 стоп')
        vols = {c: 1e12 for c in adv3.COINS}
        m = model_plan(rep, rg, vols)
        qs = [3.0, 2.6, 1.9, 1.5, 1.4]
        wants = [min(1.0, 5 * 0.5 * q / sum(qs)) for q in qs]
        chk('model_plan: two signals of this close leave five places of seven - ETH, SOL, AVAX, HBAR and ENA - their risk 5 x 0.5 % shared by '
            'min(|z|, 3); the other five named, beyond seven new a close',
            [it['coin'] for it in m['new']] == ['ETH', 'SOL', 'AVAX', 'HBAR', 'ENA']
            and all(abs(it['pos']['want'] - w) < 1e-12 for it, w in zip(m['new'], wants))
            and [(c, code) for c, _s, code, _w, _d in m['excluded'][3:]] == [(c, 'count') for c in ('UNI', 'ARB', 'ZEC', 'HYPE', 'SUI')]
            and m['risk'] == {1: 1.0, -1: 0.0})
        rg_full = Registry(state)
        rg_full.sig[1]['risk_pct'] = 9.5
        mf = model_plan(rep, rg_full, vols)
        chk('model_plan: the room spent - 9.5 % and 0.5 % open - every candidate named for the room, those beyond seven too',
            mf['new'] == [] and [code for _c, _s, code, _w, _d in mf['excluded'][3:]] == ['room'] * 10)
        v = view_plan(rep, rg, vols, dict(DEFAULTS, n=2, set=['n']), m)
        chk('view_plan: «топ 2» - ETH and SOL; LINK, this close\'s, and AVAX, HBAR and ENA named beyond the request\'s top',
            [it['coin'] for it in v['items']] == ['ETH', 'SOL'] and [c for c, _s, code, _w, _d in v['excluded'] if code == 'top'] == ['AVAX', 'LINK', 'HBAR', 'ENA'])
        rows_tight = dict(rep['rows'], SOL=row(1, 2.6, U=12.0))
        rep_t = dict(rep, rows=rows_tight)
        m_t = model_plan(rep_t, rg, vols)
        v2 = view_plan(rep_t, rg, vols, dict(DEFAULTS, stop=10.0, set=['stop']), m_t)
        chk('view_plan: «стоп 10» names SOL for its 12 % stop at 10 %; a coin the model left out keeps the model\'s reason; LINK, the '
            'registry\'s, stays sized', ('SOL', 'stop', 'стоп дальше 10%', '12,0%') in [(c, code, w, d) for c, _s, code, w, d in v2['excluded']]
            and ('UNI', 'count') in [(c, code) for c, _s, code, _w, _d in v2['excluded']]
            and 'LINK' in [it['coin'] for it in v2['items']] and all(it.get('pos') for it in v2['items']))
        ids_ = register(rg, rep, m['new'], when, 'check:test')
        reg_ev = [e for e in rg.events if e['type'] in ('open', 'fill') and e['id'] >= 4]
        chk('register: ids 4 to 8 in the rule\'s order, each open then filled at its market entry at the instant written; places from it',
            ids_ == [4, 5, 6, 7, 8] and [(e['type'], e['id']) for e in reg_ev] == [(t_, i) for i in range(4, 9) for t_ in ('open', 'fill')]
            and all(e['utc'] == when.isoformat(timespec='seconds') for e in reg_ev)
            and all(rg.sig[i]['valid'] == '2026-11-06T00:00:00+00:00' and rg.sig[i]['capital'] == CAPITAL and rg.sig[i]['btc'] is None
                    and rg.sig[i]['breadth'] == 15 for i in ids_)
            and rg.cursor[4] == {'t': ceil1(ms_at(when)), 'b': ms_at(when), 'mfe': 0.0})
        later = when + dt.timedelta(seconds=20, microseconds=500_000)
        ids_l = register(rg, rep, [dict(m['new'][0], rank=1)], later, 'request')
        sl = rg.sig[ids_l[0]]
        chk('register: an instant inside a minute - 00:10:20.5 - written to its second, the place from the next minute, 00:11',
            sl['utc'] == '2026-11-05T00:10:20+00:00' and sl['fill_utc'] == sl['utc']
            and rg.cursor[ids_l[0]] == {'t': ms_at(when) + K1_MS, 'b': ms_at(when) + 20_000, 'mfe': 0.0})
        for name in os.listdir(state):
            os.remove(os.path.join(state, name))

        # ---- the seed: a journal of the old records ------------------------------------------------------------------------
        globals()['STATE'] = state
        T0 = dt.datetime(2026, 10, 29, 14, 40, tzinfo=dt.timezone.utc)
        tz_ = lambda h: (T0 + dt.timedelta(hours=h)).isoformat(timespec='seconds')
        cardj = lambda coin, mode='market', E=100.0, strong=True, side=1: {'coin': coin, 'side': side, 'strong': strong, 'mode': mode, 'entry': E,
                                                                         'stop': 90.0, 'targets': [110.0, 120.0, 130.0], 'close': 100.0, 'U': 10.0,
                                                                         'since': '2026-10-20', 'rank': 1}
        recs = [{'utc': tz_(0), 'kind': 'daily', 'close_of': '2026-10-28', 'cards': [cardj('ETH'), cardj('BTC', strong=False), cardj('SOL', mode='none', E=None), {'coin': 'ETH'}],
                 'signals': {'BTC': 1}},
                {'utc': tz_(15), 'kind': 'alloc', 'close_of': '2026-10-29', 'alloc': {'items': [{'coin': 'SOL'}], 'more': []},
                 'cards': [cardj('SOL'), cardj('AVAX')]},
                {'utc': tz_(16), 'kind': 'request', 'close_of': '2026-10-29', 'cards': [cardj('ETH', E=101.0), cardj('SOL', mode='limit')]},
                {'utc': tz_(40), 'kind': 'check', 'close_of': '2026-10-30', 'cards': [cardj('ETH', E=95.0)], 'state': {'ETH': {'z': 2.5, 'sum': 4}}},
                {'utc': tz_(41), 'kind': 'assess', 'close_of': '2026-10-30', 'cards': [cardj('XRP')]}]
        with open(os.path.join(state, 'journal.jsonl'), 'w', encoding='utf-8') as fh:
            fh.write('\n'.join(json.dumps(r) for r in recs[:2]) + '\nnot json\n' + '\n'.join(json.dumps(r) for r in recs[2:]) + '\n')
        t_open = ms_at(T0)

        def fake5(path, **p_):
            coin, start = p_['symbol'][:-4], int(p_['startTime'])
            out = []
            t_ = max(start, ceil5(t_open))
            while len(out) < int(p_['limit']) and t_ <= t_open + 60 * 3600_000:
                px = 100.0 if not (coin == 'ETH' and t_open + 20 * 3600_000 <= t_ < t_open + 21 * 3600_000) else 89.0
                out.append([t_, str(px), str(px + 0.5), str(px - 0.5), str(px), '0', t_ + K5_MS - 1, '0'])
                t_ += K5_MS
            return out
        adv3.fapi = fake5
        rs = Registry(state)
        opened = seed(rs, {}, {}, t_open + 60 * 3600_000, when)
        sigs = [rs.sig[i] for i in sorted(rs.sig)]
        jsha = hashlib.sha256(open(os.path.join(state, 'journal.jsonl'), 'rb').read()).hexdigest()
        def legacy_pos(E, S):
            d_ = abs(E - S) / E
            rate = d_ + 0.002
            notional = math.floor(0.005 * CAPITAL / rate)
            lev = min(min(20, math.floor(1 / (1.5 * d_ + 0.01))), math.floor(notional / 1000))
            return notional, math.ceil(notional / lev)
        chk('seed: its first event names the journal by SHA-256, its 5 records that parse and the 5 STRONG cards with an entry of the kinds '
            'it reads; the signals ETH of 29.10, SOL of the allocation\'s placed coin and ETH again after its stop - a card repeated within a '
            'signal\'s life is that signal shown again',
            rs.events[0]['type'] == 'seed' and rs.events[0]['journal_sha'] == jsha and rs.events[0]['records'] == 5 and rs.events[0]['cards'] == 5
            and opened == 3 and [(s['coin'], s['close_of'], s['source']) for s in sigs]
            == [('ETH', '2026-10-28', 'journal:daily'), ('SOL', '2026-10-29', 'journal:alloc'), ('ETH', '2026-10-30', 'journal:check')]
            and sigs[0]['status'] == 'closed' and sigs[0]['why'] == 'stop' and sigs[2]['entry'] == 95.0 and sigs[2]['z'] == 2.5 and sigs[0]['btc'] == 1
            and all(s['legacy'] and (s['notional'], s['margin']) == legacy_pos(s['entry'], s['stop']) for s in sigs)
            and [legacy_pos(100.0, 90.0), legacy_pos(95.0, 90.0)] == [(9803, 1634), (18304, 1664)])
        chk('seed: ETH\'s stop walked to the instant of the next card - the candle opening at 89, beyond the stop at 90 - before ETH of '
            '30.10 is written', [e['type'] for e in rs.events] == ['seed', 'open', 'fill', 'open', 'fill', 'stop', 'open', 'fill']
            and rs.events[5]['utc'] == iso(t_open + 20 * 3600_000) and rs.events[5]['price'] == 89.0)
        for name in os.listdir(state):
            os.remove(os.path.join(state, name))

        # ---- the stats, by hand -------------------------------------------------------------------------------------------
        w1, w2 = wilson(5, 10), wilson(0, 1)
        chk('wilson: 5 of 10 is 23.66 to 76.34 %, 0 of 1 is 0 to 79.35 %', abs(w1[0] - 23.66) < 0.01 and abs(w1[1] - 76.34) < 0.01
            and abs(w2[0]) < 1e-9 and abs(w2[1] - 79.35) < 0.01)
        chk('t975: the table to 30 - 12.706 at 1, 2.042 at 30 - then the expansion: 2.0395 at 31, 2.0003 at 60, 1.9799 at 120',
            t975(1) == 12.706 and t975(30) == 2.042 and abs(t975(31) - 2.0395) < 2e-4 and abs(t975(60) - 2.0003) < 2e-4 and abs(t975(120) - 1.9799) < 2e-4)
        mc = mean_ci([1.0, 2.0, 3.0, 4.0])
        chk('mean_ci: 1, 2, 3, 4 - mean 2.5, 95 % from 0.446 to 4.554; one value, no interval',
            mc[0] == 2.5 and abs(mc[1] - (2.5 - 3.182 * math.sqrt(5 / 3) / 2)) < 1e-12 and mean_ci([1.0])[1:] == (None, None))

        # ---- checks and requests end to end: Binance and Telegram stood in for ------------------------------------------------
        class Cap(Telegram):
            def __init__(self, down=False):
                super().__init__('123456:SECRET', 777)
                self.sent, self.down = [], down

            def call(self, method, http_timeout=30, **params):
                if self.down:
                    raise RuntimeError('telegram sendMessage: 502 Bad Gateway')
                self.sent.append((params['text'], params.get('disable_notification', False), 'reply_markup' in params))
                return {'message_id': len(self.sent)}

        dm = dt.date(2026, 6, 1)
        cs, funds = {}, {}
        for n, coin in enumerate(adv3.COINS[:12]):
            c, x = {}, 100.0 + n
            slope = (0.004 + 0.0015 * n) * (1 if n % 2 == 0 else -1)
            for i in range(160):
                x *= (1 + slope) * (1 + 0.004 * ((i * 7 + n) % 5 - 2))
                c[dm + dt.timedelta(days=i)] = (x, x * 1.02, x * 0.98, x)
            cs[coin] = c
            funds[coin] = lambda d: 0.0
        last = max(cs['BTC'])
        T1 = at(last + adv3.DAY, 0, 10)
        clock = {'now': T1}
        path5, calls1 = {}, []

        def fake(path, **p_):
            now_ms = ms_at(clock['now'])
            if path == '/fapi/v1/premiumIndex':
                return [{'symbol': c + 'USDT', 'markPrice': str(cs[c][last][3]), 'lastFundingRate': '0.0001'} for c in cs]
            if path == '/fapi/v1/fundingInfo':
                return []
            coin = p_['symbol'][:-4]
            if p_['interval'] == '1d':
                return [[day_ms(last - k * adv3.DAY), '1', '1', '1', '1', '0', day_ms(last - k * adv3.DAY) + DAY_MS - 1, '1e12'] for k in range(8)]
            step = K1_MS if p_['interval'] == '1m' else K5_MS
            calls1.append(step == K1_MS)
            out, t_ = [], max(int(p_['startTime']), ms_at(T1) - 2 * K5_MS)
            base_ = cs[coin][last][3]
            while len(out) < int(p_['limit']) and t_ <= now_ms:
                px = path5.get(coin, {}).get(t_ - t_ % K5_MS, base_)
                out.append([t_, str(px), str(px * 1.0001), str(px * 0.9999), str(px), '0', t_ + step - 1, '0'])
                t_ += step
            return out

        class Stub:
            def __init__(self):
                self.cs, self.funds, self.missing = cs, funds, []

            def fresh(self):
                return self.cs, self.funds

        adv3.fapi = fake
        stub, cap, rg = Stub(), Cap(), Registry(state)

        def run(fn, *a):
            with contextlib.redirect_stdout(io.StringIO()):
                return fn(*a)
        rep0 = adv3.report(cs, funds, {c + 'USDT': (cs[c][last][3], 0.0001) for c in cs}, CAPITAL, 0.5, ms_at(T1))
        strong0 = strong_all(rep0)
        e1 = run(check, cap, stub, rg, (T1.date(), 'signal'), T1)
        append(e1)
        n_new = len(e1['opened'])
        chk('end to end, the first signal check: the registry seeded from an empty journal, the STRONG candidates written after the message '
            'went - seven at most - loud, one full message; its record the 42 coins, the cards with their numbers and positions, the registry',
            rg.events[0]['type'] == 'seed' and rg.events[0]['cards'] == 0 and 1 <= n_new <= NEW_MAX and e1['opened'] == list(range(1, n_new + 1))
            and e1['quiet'] is False and e1['one_line'] is False and len(cap.sent) == 1 and '🆕 <b>Новые STRONG</b>' in cap.sent[0][0]
            and len(e1['state']) == 42 and [c['id'] for c in e1['cards']] == e1['opened'] and all(c['position'] for c in e1['cards'])
            and e1['strong_all'] == strong0 and e1['registry']['seeded'] == 0 and rg.announced == len(rg.events)
            and all(f'#{i}' in cap.sent[0][0] for i in e1['opened']) and cap.sent[0][2] is False)
        e1b = run(check, cap, stub, rg, (T1.date(), 'signal'), T1 + dt.timedelta(minutes=1))
        append(e1b)
        chk('end to end, the same check again: nothing new, nothing ended, the coins not taken as before - one quiet line, no signal written twice',
            e1b['one_line'] is True and e1b['quiet'] is True and e1b['opened'] == [] and '\n' not in cap.sent[-1][0]
            and cap.sent[-1][0].startswith('✓ 04:11 по Батуми · закрытие') and len([s for s in rg.sig.values()]) == n_new)
        coin_a, coin_b = rg.sig[1]['coin'], rg.sig[min(2, n_new)]['coin']
        sa = rg.sig[1]
        Tt = ms_at(T1) + 10 * K5_MS
        path5[coin_a] = {Tt: sa['targets'][0] + sa['side'] * 0.0}
        clock['now'] = T1 + dt.timedelta(hours=15)
        Tf = at(T1.date(), 15, 7)
        e2 = run(check, cap, stub, rg, (T1.date(), 'fact'), Tf)
        append(e2)
        chk('end to end, the fact check: the first signal\'s target 1, walked on its 5-minute candles, a quiet event - no new signal, no end',
            [(rg.events[n - 1]['type'], rg.events[n - 1]['id']) for n in e2['events']] == [('target', 1)] and e2['quiet'] is True
            and e2['one_line'] is False and '🎯 #1' in cap.sent[-1][0] and rg.sig[1]['hit'] == 1)
        if n_new >= 2:
            sb = rg.sig[2]
            path5[coin_b] = {ceil5(ms_at(Tf)) + 6 * K5_MS: sb['stop'] - sb['side'] * sb['entry'] * 0.01}
        clock['now'] = T1 + dt.timedelta(hours=16)
        down = Cap(down=True)
        failed = False
        try:
            run(check, down, stub, rg, (T1.date(), 'fact'), T1 + dt.timedelta(hours=16))
        except RuntimeError:
            failed = True
        stopped = [e for e in rg.events if e['type'] == 'stop']
        chk('end to end, Telegram down: the check raises, the stop it found is written and stays unannounced',
            failed and (n_new < 2 or (len(stopped) == 1 and stopped[0]['n'] > rg.announced)))
        e3 = run(check, cap, stub, rg, (T1.date(), 'fact'), T1 + dt.timedelta(hours=16, minutes=5))
        append(e3)
        chk('end to end, the retry: the stop announced once, loud', n_new < 2 or (e3['quiet'] is False and '⛔ #2' in cap.sent[-1][0]
                                                                           and [rg.events[n - 1]['type'] for n in e3['events']] == ['stop']))
        e4 = run(check, cap, stub, rg, (T1.date(), 'fact'), T1 + dt.timedelta(hours=16, minutes=10))
        chk('end to end, the fact check again: one quiet line naming the next check', e4['one_line'] is True and e4['quiet'] is True
            and 'следующая проверка 04:10' in cap.sent[-1][0])
        rr = Registry(state)
        chk('the registry read back after the checks: the same signals, head and announced, the chain whole',
            rr.sig == rg.sig and rr.head == rg.head and rr.announced == rg.announced and rr.broken is None)
        cap2, per = Cap(), []
        for text in ('сигнал', 'сигнал 50000 риск 1 топ 2', 'реестр', 'рейтинг', 'оценка', 'помощь', 'привет'):
            n0 = len(cap2.sent)
            run(handle, cap2, stub, rg, text)
            per.append(cap2.sent[n0:])
        texts = ['\n'.join(t for t, _q, _k in p_) for p_ in per]
        chk('handle: «сигнал» the close\'s STRONG with their positions and the risk, «сигнал 50000…» at the request\'s parameters, «реестр» the '
            'signals and the chain, «рейтинг» the order, «оценка» the assessment and the registry\'s figures, «помощь» and an unknown text HELP; '
            'every reply its keyboard and a notification',
            texts[0].startswith('📊 <b>ADV-3 · STRONG</b>') and 'Риск модели' in texts[0] and 'Капитал 50 000 USDT · риск 1,0%' in texts[1]
            and 'по запросу: капитал, топ, риск' in texts[1] and texts[2].startswith('📒') and '🔐 Реестр:' in texts[2]
            and texts[3].startswith('🏆') and '1. ' in texts[3] and 'Оценка доверия' in texts[4] and 'Реестр сигналов бота' in texts[4]
            and texts[5] == HELP and texts[6] == HELP and all(p_[-1][2] for p_ in per) and all(not q for p_ in per for _t, q, _k in p_))
        kinds_ = [r['kind'] for r in journal_records()]
        chk('handle: the journal holds check, check, check, check, then request, request, registry, ranking, assess - HELP no record',
            kinds_ == ['check'] * 4 + ['request', 'request', 'registry', 'ranking', 'assess'])
        saved_lr = globals()['live_report']
        globals()['live_report'] = lambda *a_: (_ for _ in ()).throw(RuntimeError('fapi.binance.com served no candles'))
        try:
            run(handle, cap2, stub, rg, 'сигнал')
            run(handle, Cap(down=True), stub, rg, 'сигнал')
        finally:
            globals()['live_report'] = saved_lr
        chk('handle: Binance down gets the apology, Telegram down raises nothing', cap2.sent[-1][0].startswith('Binance или Telegram не ответили'))
        allt = [t for t, _q, _k in cap.sent + cap2.sent]
        chk('every part of every message balances its markup', all(t.count('<b>') == t.count('</b>') and t.count('<i>') == t.count('</i>')
                                                                   for t in allt))
        chk('no message calls the bot the Boss\'s account or asks to check his positions', not any(
            k in t for t in allt for k in ('ваши позиции', 'проверьте позиции', 'ваш аккаунт', 'видит ваш счёт')))
    finally:
        globals()['STATE'], adv3.fapi = saved
        shutil.rmtree(state)
    chk('glibc takes its two settings', malloc_tune())
    time.sleep = real_sleep
    chk('the self-test restored time.sleep and paused nowhere: every pause recorded', time.sleep is real_sleep and all(x in (1.1, 8, 61) for x in slept))
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

```text file=research/tz42-advisor-registry.py
#!/usr/bin/env python3
# tz42-advisor-registry.py - TZ-42's checker: the fingerprint, the host gate, the number, G-RULE, COPY, G-RENDER, the readings
# after the unit's restart - UNIT-NEW and G-FIRST - and the marks. Standard library only. It starts and stops no unit, signals no
# process and sends no request of its own (G-RENDER runs the service copy's bot, which reads Binance's public market), and it
# never reads or prints the bot's token or the pinned chat, a coin, a price or a size. It writes one file of the unit's record,
# /var/lib/adv3-bot/check-done: at the kill mark the slot before the day's signal check, so that the new process replays that
# check at its start, and at the rollback mark the kill mark's value again where the new process never moved it. It re-derives
# the registry the bot keeps - its chain, the signals the journal seeds and every signal's walk on the 1- and 5-minute candles the bot
# read, in the order it read them - and every position and allocation, by its own reading, never by the bot's functions.
# Exits: 0 every assert held; 1 a failed assert, named; 3 NOT YET.
import array, ast, bisect, calendar, contextlib, datetime as dt, hashlib, importlib.util, io, itertools, json, math, os, re, shutil, \
    subprocess, sys, time

WORK = '/root/tz42-work'
WT = WORK + '/wt'
STATE = WORK + '/state.json'
SCRATCH = WORK + '/render-state'
PRIMARY = '/root/btc-5m-twap'
FORENSICS = '/root/btc-forensics'
SVC = '/root/adv3-bot-svc'
BOTDIR = '/var/lib/adv3-bot'
PY = '/root/tz04a-env/venv/bin/python'
ARGV = [PY, '-B', '-u', SVC + '/adv3-bot.py', '--serve']
BOT = 'adv3-bot.service'
CAPTURES = ('btc-recorder.service', 'btc-pairbook.service', 'btc-rewardbook.service')
TZ_FILE = 'CryptoTZ/TZ-42-advisor-registry.md'
NUMBER = 'TZ-42-'
BRANCH = 'tz-42-advisor-registry'
MAP_REV = '2026-11-01-b'
ANCHORS = {'A1': '229a944f2d51', 'A2': '6c5089330629',
           'A3': '0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable',
           'A4': '437b45ea196b', 'A5': '0f6c90451cbd', 'A6': '729f0bcdbee3'}
DERIVED = {'A2': 'research/twap-divergence.py', 'A4': 'BTC-EXECUTOR-INSTRUCTIONS.md',
           'A5': 'research/recorder/recorder.py', 'A6': 'research/pfair.py'}
H = {'adv3': '81ef0112d3fe4b86566e51a51aab924d9776ff37a927e65982ecb0bb7c1f34e1',
     'bot_old': '9e622daf2e8a5ec3e93f15c7f56e7cf859547fbd3771daad75bc6532adb2b9d1',
     'bot_new': 'c3d9fff54f3585cfc4c33b5f7e1f93b390e62b03e0b4725fee2d6fdda6d04c11',
     'selftest': '6f29b82f2b2ca82cd2ff4bbb370e032354dbb4743497330530777429b3af7398',
     'rule': 'ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169',
     'unit': '82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66'}
# G-RULE's table for adv3-bot.py: (changed, added, removed) definitions and assignments against origin/main's; the definitions whose
# code is the same and only their docstring changed; and those that must stay identical, docstring and all.
BOT_DEFS = ({'Telegram', 'base_record', 'candidates', 'check', 'check_record', 'compose', 'done_after', 'due', 'event_lines', 'handle',
             'hello', 'probe', 'route', 'selftest', 'serve', 'zone_lines'},
            {'Registry', 'advance', 'allocate', 'assess_view', 'base_fund', 'bat', 'by_side', 'card_lines', 'carded', 'ceil1', 'ceil5', 'chain_line',
             'day_ms', 'ended_line', 'ensure', 'event_line', 'excluded_lines', 'first_window', 'footer', 'from_iso', 'iso', 'item_record',
             'klines', 'last_check', 'legend', 'line_hash', 'live_line', 'mean_ci', 'model_plan', 'ms_at', 'new_signal', 'note_lines', 'notes_of',
             'notional_of', 'open_risk', 'params', 'params_line', 'pct0', 'position', 'ranking_view', 'reconcile', 'register',
             'registry_view', 'risk_line', 'second', 'seed', 'seed_line', 'sg', 'signal_view', 'signed_usdt', 'stats_lines', 'status_of',
             't975', 'view_plan', 'walk', 'wilson', 'zones_of'},
            {'alerted', 'alerts_of', 'alloc_fields', 'candidate_lines', 'correlation', 'follow', 'followed_lines', 'forming_candles',
             'item_lines', 'journal_scan', 'make', 'numbers', 'offers', 'plan', 'plan_parts', 'plan_strong', 'quiet_line', 'returns_of',
             'strong_shares', 'top_n', 'weak_lines', 'weakened', 'zones_left'})
DOC_ONLY = ('due', 'done_after')
BOT_SAME = ('Data', 'TooMany', 'append', 'chunks', 'find_chat', 'hhmm', 'journal_records', 'latest_slot', 'liquidity', 'live_report', 'log',
            'main', 'malloc_tune', 'next_at', 'put', 'ranked', 'read', 'slot_at', 'slot_key', 'slot_parse', 'slot_text', 'strong_all',
            'volumes')
BOT_ASG = ({'CARD_KEYS', 'HELP', 'SLOTS', 'TOPN'},
           {'(CAPITAL, RISK_TOTAL, STOP_MAX, NEW_MAX)', '(K1_MS, K5_MS, K5_PAGE)', '(LIQ_FRAC, Z_CAP, LIQ_DAYS)',
            '(MARGIN_MIN, MARGIN_MAX, MARGIN_EXC)', '(RANK_LIST, RANK_MAX)', '(REG_FILE, REG_STATE, GENESIS)', 'COMMANDS', 'DAY_MS',
            'DEFAULTS', 'HELPS', 'INTERVAL', 'KEYBOARD', 'KEYWORDS', 'LABEL', 'LEGACY_KEYS', 'LOUD', 'NUMBER', 'RANKING', 'REGISTRY', 'SHOWN', 'T975'},
           {'(STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, CROWD, Z_CAP, LIQ_DAYS)', 'FOOTER', 'LIST_MAX'})
# this TZ's numbers: the model's defaults, the margin's bounds in percent of the capital, the liquidity share, the strength's cap, the
# new signals a close, the rung, the pause between parts, |z| 1 for STRONG; the old schedule the running process keeps and the new one
CAPITAL, RISK, RISK_MAX, RISK_TOTAL, STOP_MAX, NEW_MAX = 200000.0, 0.5, 1.0, 10.0, 14.0, 7
MARGIN_MIN, MARGIN_MAX, MARGIN_EXC, LIQ_FRAC, Z_CAP, COST, RUNG, PACE, STRONG_Z = 0.5, 3.5, 4.0, 0.005, 3.0, 0.001, 1, 1.1, 1.0
OLD_SLOTS = (('signal', dt.time(0, 10)), ('fact', dt.time(12, 10)))
SLOTS = (('signal', dt.time(0, 10)), ('fact', dt.time(15, 7)))
K1_MS, K5_MS, DAY_MS = 60_000, 300_000, 86_400_000
MEM_FLOOR, DISK_FLOOR, COIN_DAYS_MAX = 150_369_520, 7_400_000_000, 120
ROWS, FROZEN = 60, 57
FIRST_BOUND = 900
TZ40_REPLAY = '2026-11-01 signal'   # TZ-40's replay at its restart, 18:06 UTC (map §2.7): the last check record naming this slot
# TZ-41 (L0) runs on this host from 2026-11-08 07:30 UTC and reads the advisor's unit unchanged through its run (its G-STILL): this TZ
# deploys only before 07:00 that day, or once TZ-41's report is on main, and never while TZ-41's work tree exists.
TZ41_EDGE = 1794121200
TZ41_REPORT = 'CryptoReports/TZ-41-l0-our-quote-report.md'
TZ41_WORK = '/root/tz41-work'
RENDER_CASES = ('сигнал', 'сигнал 50000 риск 1 лимит 2 топ 3', 'реестр', 'рейтинг', 'оценка', 'помощь', 'привет')
RENDER_KINDS = ['request', 'request', 'registry', 'ranking', 'assess', 'check', 'check']
TRUST_KEYS = {'system', 'strong_justified', 'served', 'cards', 'quality', 'fresh', 'complete', 'expectancy_established'}
DAY = dt.timedelta(days=1)
GENESIS = '0' * 64


class Failed(Exception):
    pass


class NotYet(Exception):
    pass


def out(*parts):
    print(*parts, flush=True)


def sh(args, **kw):
    p = subprocess.run(args, capture_output=True, text=True, **kw)
    return p.returncode, p.stdout, p.stderr


def read(path, mode='r'):
    with open(path, mode, **({} if 'b' in mode else {'encoding': 'utf-8'})) as fh:
        return fh.read()


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(path):
    return sha256_bytes(read(path, 'rb'))


def maybe_sha(path):
    return sha256_file(path) if os.path.exists(path) else None


def load_state():
    return json.loads(read(STATE)) if os.path.exists(STATE) else {}


def save_state(state):
    tmp = STATE + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(state, indent=1, sort_keys=True) + '\n')
    os.replace(tmp, STATE)


def verdict(name, checks):
    n = sum(1 for v in checks.values() if v)
    for k, v in checks.items():
        out(('ok   ' if v else 'FAIL ') + k)
    out('READING %s: %s - %d of %d' % (name, 'PASS' if n == len(checks) else 'FAIL', n, len(checks)))
    if n != len(checks):
        raise Failed(name)


def show(unit, *props):
    args = ['systemctl', 'show', unit] + [a for p in props for a in ('-p', p)]
    rc, so, se = sh(args, env=dict(os.environ, TZ='UTC'))
    assert rc == 0, se
    return dict(line.split('=', 1) for line in so.splitlines() if '=' in line)


def proc_argv(pid):
    try:
        with open('/proc/%s/cmdline' % pid, 'rb') as fh:
            parts = fh.read().split(b'\0')
    except OSError:
        return None
    return [p.decode() for p in parts[:-1]] if parts and parts[-1] == b'' else [p.decode() for p in parts]


def procs(argv):
    return sorted(int(p) for p in os.listdir('/proc') if p.isdigit() and proc_argv(p) == argv)


def proc_start(pid):
    """The process's start as epoch seconds, from /proc/<pid>/stat (field 22) and the boot time."""
    stat_text = read('/proc/%s/stat' % pid)
    fields = stat_text[stat_text.rindex(')') + 2:].split()
    ticks = int(fields[19])
    btime = next(int(line.split()[1]) for line in read('/proc/stat').splitlines() if line.startswith('btime '))
    return btime + ticks / os.sysconf('SC_CLK_TCK')


# ---- pure readings: each takes what the modes read and returns its checks -----------------------------------------

def parse_map(text):
    """(revision, {anchor: value}, rows) of SYSTEM-MAP.md section 0; a row is (path, lines, bytes, state, sha)."""
    rev = re.search(r'\*\*Revision string:\*\* `([^`]+)`', text).group(1)
    anchors = dict(re.findall(r'^\| `(A\d)` — [^|]*\| `([^`]+)` \|$', text, re.M))
    rows = []
    for line in text[text.index('### Fingerprint table'):].split('\n')[1:]:
        if line.startswith('## ') or line.startswith('### '):
            break
        m = re.match(r'^\| `([^`]+)` \| ([^|]+) \| ([^|]+) \| (frozen|tracked|reported) \| ([^|]+) \|$', line)
        if m:
            num = lambda s: None if s.strip() == '—' else int(s.replace(',', ''))
            sha = re.search(r'`([0-9a-f]{64})`', m.group(5))
            rows.append((m.group(1), num(m.group(2)), num(m.group(3)), m.group(4), sha.group(1) if sha else None))
    return rev, anchors, rows


def top_level(src):
    """{name: ast.dump} of a module's functions and classes, and of its assignments keyed by their targets."""
    defs, asg = {}, {}
    for n in ast.parse(src).body:
        if isinstance(n, (ast.FunctionDef, ast.ClassDef)):
            defs[n.name] = ast.dump(n)
        elif isinstance(n, ast.Assign):
            asg[','.join(ast.unparse(t) for t in n.targets)] = ast.dump(n)
    return defs, asg


def tree_checks(label, old_src, new_src, defs, asg, rule=()):
    """Two of a file's syntax trees: the definitions that changed, were added and were removed are exactly defs'; every other
    definition - rule's among them, named - is identical; the assignments differ exactly as asg names."""
    (od, oa), (nd, na) = top_level(old_src), top_level(new_src)
    changed = {k for k in od if k in nd and od[k] != nd[k]}
    same = [k for k in od if k in nd and od[k] == nd[k]]
    return {
        '%s: the definitions changed are exactly %s, added %s, removed %s' % (label, sorted(defs[0]), sorted(defs[1]), sorted(defs[2])):
            (changed, set(nd) - set(od), set(od) - set(nd)) == defs,
        '%s: the %d others identical by AST%s' % (label, len(set(od) - defs[0] - defs[2]),
                                                  ', the %d this checker names among them' % len(rule) if rule else ''):
            set(same) == set(od) - defs[0] - defs[2] and all(k in same for k in rule),
        '%s: the assignments changed are exactly %s, added %s, removed %s' % (label, sorted(asg[0]), sorted(asg[1]), sorted(asg[2])):
            ({k for k in oa if k in na and oa[k] != na[k]}, set(na) - set(oa), set(oa) - set(na)) == asg,
    }


def strip_docs(src):
    """{name: ast.dump} of a module's functions with each docstring - its first statement where that is a string - removed."""
    out_ = {}
    for n in ast.parse(src).body:
        if isinstance(n, ast.FunctionDef):
            body = n.body[1:] if n.body and isinstance(n.body[0], ast.Expr) and isinstance(getattr(n.body[0], 'value', None), ast.Constant) \
                and isinstance(n.body[0].value.value, str) else n.body
            out_[n.name] = ast.dump(ast.Module(body=body, type_ignores=[]))
    return out_


def html_balanced(text):
    return all(text.count('<%s>' % t) == text.count('</%s>' % t) for t in ('b', 'i'))


def own_order(rows, coins):
    """The rule's order by this checker's own reading: every coin with a LONG or SHORT signal, a strength and a unit, by |z| from
    the largest, ties in the coins' order."""
    act = [c for c in coins if (rows.get(c) or {}).get('signal') in (1, -1) and rows[c].get('z') is not None and rows[c].get('U')]
    return sorted(act, key=lambda c: -abs(rows[c]['z']))


def own_strong(rows, order):
    """STRONG at every rank by this checker's own reading: four signs agreeing with the side and |z| at least 1."""
    return [c for c in order if rows[c].get('sum') == 4 * rows[c]['signal'] and abs(rows[c]['z']) >= STRONG_Z]


def sign_sum(days, closes, i):
    """The sum of the four signs at days[i], written here: the close against the last close at least 14, 28, 56 and 112 days
    before; None before the longest exists."""
    s = 0
    for L in (14, 28, 56, 112):
        j = bisect.bisect_right(days, days[i] - L * DAY) - 1
        if j < 0:
            return None
        s += (closes[i] > closes[j]) - (closes[i] < closes[j])
    return s


def ms_of(text):
    return int(dt.datetime.fromisoformat(text).timestamp() * 1000)


def iso_of(ms):
    return dt.datetime.fromtimestamp(ms / 1000, dt.timezone.utc).isoformat(timespec='seconds')


def midnight(day):
    return calendar.timegm(day.timetuple()) * 1000


def journal_lines(text):
    """A journal text's lines as the bot's journal_records reads them - a text file's universal newlines, '\\n', '\\r\\n' and '\\r' -
    without their ends, a last line without an end kept."""
    lines = text.replace('\r\n', '\n').replace('\r', '\n').split('\n')
    return lines[:-1] if lines and lines[-1] == '' else lines


def journal_objects(text):
    """Every line of a journal text that parses as a JSON object, in order: the records the bot's seed counts and reads."""
    out_ = []
    for line in journal_lines(text):
        try:
            r = json.loads(line)
        except ValueError:
            continue
        if isinstance(r, dict):
            out_.append(r)
    return out_


def records_since(text, t0):
    """The journal's objects from the first stamped at or after t0 less 1 s, and whether the text ends in a newline with every line
    from that record on parsing as an object."""
    recs, ok, on = [], text.endswith('\n') or text == '', False
    for line in journal_lines(text):
        try:
            r = json.loads(line)
            t = dt.datetime.fromisoformat(r['utc']).timestamp()
        except (ValueError, KeyError, TypeError, AttributeError):
            ok = ok and not on
            continue
        on = on or t >= t0 - 1
        if on:
            recs.append(r)
    return recs, ok


def count_kind(text, kind):
    """How many records of a kind a journal.jsonl text holds; a broken line left out."""
    return sum(r.get('kind') == kind for r in journal_objects(text))


def prefix_before_check(raw, t0):
    """The journal's bytes before its first check record stamped at or after t0 less 1 s - the journal as the new process's seed read
    it, its first record being that check - or the whole where there is none: (the bytes, whether such a record was found)."""
    pos = 0
    for line in raw.split(b'\n'):
        try:
            r = json.loads(line.decode('utf-8'))
            found = r.get('kind') == 'check' and dt.datetime.fromisoformat(r['utc']).timestamp() >= t0 - 1
        except (ValueError, KeyError, TypeError, AttributeError, UnicodeDecodeError):
            found = False
        if found:
            return raw[:pos], True
        pos += len(line) + 1
    return raw, False


def own_chunks(text, limit=4000):
    """The parts a message of the bot is sent in, by TZ-40's rule read here: split at line ends, never inside a line, each part at most
    limit characters but a line longer than it; a line that would begin a part and is empty is left out."""
    parts, cur = [], ''
    for line in text.split('\n'):
        if cur and len(cur) + 1 + len(line) > limit:
            parts.append(cur)
            cur = line
        else:
            cur = cur + '\n' + line if cur else line
    if cur:
        parts.append(cur)
    return parts


def own_chain(text):
    """The registry's chain by this checker's own reading: (events, the position of the first line whose prev is not the SHA-256 of
    the line before it - the genesis for the first - or whose n is not its position, or that does not parse, else None, the SHA-256 of
    the last line, whether the text ends in a newline)."""
    events, broken, prev = [], None, GENESIS
    lines = text.split('\n')
    whole = text.endswith('\n') or text == ''
    for k, raw in enumerate(lines[:-1] if whole else lines, 1):
        try:
            ev = json.loads(raw)
        except ValueError:
            ev = None
        if not isinstance(ev, dict) or ev.get('prev') != prev or ev.get('n') != k:
            broken = broken or k
        if isinstance(ev, dict):
            events.append(ev)
        prev = hashlib.sha256(raw.encode('utf-8')).hexdigest()
    return events, broken, prev, whole


def head_at(text, n):
    """The chain's head after its first n lines: the SHA-256 of line n, the genesis for n = 0."""
    if n == 0:
        return GENESIS
    lines = text.split('\n')
    return hashlib.sha256(lines[n - 1].encode('utf-8')).hexdigest() if 0 < n <= len(lines) else None


def own_signals(events):
    """{id: the signal} from the events by this checker's own reading: the open's fields, then 'fill', 'hit' (the highest target), 'end'
    ('stop', 'exit' or 'expire') and the end's R and pnl."""
    out_ = {}
    for e in events:
        t = e.get('type')
        if t == 'open':
            out_[e['id']] = dict(e, fill=None, hit=0, end=None, R=None, pnl=None)
        elif e.get('id') in out_:
            s = out_[e['id']]
            if t == 'fill':
                s['fill'] = e['price']
            elif t == 'target':
                s['hit'] = max(s['hit'], e['k'])
            elif t in ('stop', 'exit', 'expire'):
                s['end'], s['R'], s['pnl'] = t, e.get('R'), e.get('pnl')
    return out_


def start_of(o):
    """A signal's place at its issue by this checker's own reading: its first minute the one opening at or after the issue; filled at
    its entry and its instant where it enters at market."""
    issued = ms_of(o['utc'])
    market = o['mode'] == 'market'
    return {'filled': market, 'fp': o['entry'] if market else None, 'fill_ms': issued if market else None, 'hit': 0,
            't': -(-issued // K1_MS) * K1_MS, 'b': issued, 'end': None}


def own_walk(o, k5, daily, fund, until=None, start=None, k1=()):
    """One signal's events on its candles by this checker's own reading of TZ-42's rule. o: its open event's fields; start: its place
    ({'filled', 'fp', 'fill_ms', 'hit', 't', 'b', 'end'}), start_of(o) where None; k1 its first minutes' 1-minute candles, then k5 the
    5-minute ones, each [(open ms, o, h, l, c, closed)] in time order; daily: [(day, (o, h, l, c))] in day order; fund: day -> the
    funding sum. From the first candle at or after the place: a
    daily close - 00:00 UTC of the day after - at or before a candle's open ends a filled signal whose sum of four signs (sign_sum) has
    left its side, at that close; a candle opening at or after the validity's end ends a waiting limit; a waiting limit's candle that
    reaches the limit fills it - at the open where the open is past it - and ends it where it also reaches the stop; a filled signal's
    candle opening past targets credits them, then a stop reached in it ends the signal - at the open where the open is beyond the
    stop - else it credits each target reached. Closed candles advance the place, the last one open is read; with until, no candle
    closing after it is read. Returns (events [(type, k, utc ms, price, R, the result per unit)], the place at the end)."""
    side, E, S, T = o['side'], o['entry'], o['stop'], o['targets']
    valid = ms_of(o['valid'])
    D = dt.date.fromisoformat(o['close_of'])
    st = dict(start) if start else start_of(o)
    days = [d for d, _c in daily]
    closes = [c[3] for _d, c in daily]
    out_ = []

    def end(kind, at, X):
        held = sum(side * fund(days[i]) * closes[i] for i in range(len(days)) if st['fill_ms'] < midnight(days[i] + DAY) <= at)
        unit = side * (X - st['fp']) - COST * (st['fp'] + X) - held
        out_.append((kind, None, at, X, unit / abs(E - S), unit))
        st['end'] = kind

    bounds = [(midnight(d + DAY), i) for i, d in enumerate(days) if d > D and midnight(d + DAY) > st['b']]
    at = [0]

    def closes_upto(limit):
        while at[0] < len(bounds) and bounds[at[0]][0] <= limit:
            B, i = bounds[at[0]]
            at[0] += 1
            st['b'] = B
            if st['filled']:
                sgn = sign_sum(days, closes, i)
                rule = 1 if sgn is not None and sgn >= 2 else -1 if sgn is not None and sgn <= -2 else 0
                if rule != side:
                    end('exit', B, closes[i])
                    return True
        return False

    if st['end']:
        return out_, st
    for width, (t0, op, hi, lo, cl, closed) in itertools.chain(((K1_MS, x) for x in k1), ((K5_MS, x) for x in k5)):
        if t0 < st['t']:
            continue
        if until is not None and t0 + width > until:
            break
        if closes_upto(t0):
            return out_, st
        if not st['filled']:
            if t0 >= valid:
                out_.append(('expire', None, valid, None, None, None))
                st['end'] = 'expire'
                return out_, st
            if (lo <= E) if side > 0 else (hi >= E):
                fp = min(op, E) if side > 0 else max(op, E)
                st.update(filled=True, fp=fp, fill_ms=t0)
                out_.append(('fill', None, t0, fp, None, None))
                if (lo <= S) if side > 0 else (hi >= S):
                    end('stop', t0, op if ((op <= S) if side > 0 else (op >= S)) else S)
                    return out_, st
        else:
            for k in (1, 2, 3):
                if st['hit'] < k and ((op >= T[k - 1]) if side > 0 else (op <= T[k - 1])):
                    st['hit'] = k
                    out_.append(('target', k, t0, T[k - 1], None, None))
            beyond = (op <= S) if side > 0 else (op >= S)
            if beyond or ((lo <= S) if side > 0 else (hi >= S)):
                end('stop', t0, op if beyond else S)
                return out_, st
            for k in (1, 2, 3):
                if st['hit'] < k and ((hi >= T[k - 1]) if side > 0 else (lo <= T[k - 1])):
                    st['hit'] = k
                    out_.append(('target', k, t0, T[k - 1], None, None))
        if closed:
            st['t'] = t0 + width
    limit = st['t'] if until is None else min(st['t'], until)
    if not closes_upto(limit) and not st['filled'] and st['t'] >= valid and (until is None or valid <= until):
        out_.append(('expire', None, valid, None, None, None))
        st['end'] = 'expire'
    return out_, st


def own_coins():
    """The Boss's 42, in RULE-ADV-3's order, read here."""
    return ('BTC BCH SKY XLM XMR MORPHO LIT NEAR HBAR GRAM ENA UNI ARB ZEC HYPE SUI ADA RENDER TAO FET YFI XRP SOL ONDO LINK ALGO TRX BNB '
            'AAVE AVAX ETH INJ LTC XAU DASH PYTH WLD BTW QNT PUMP VVV EGLD').split()


def journal_cards(records):
    """The STRONG cards with an entry the journal's records published, by this checker's own reading of TZ-42's seed: of the daily,
    request, allocation and check records - of an allocation only the coins it placed - each card marked strong, at market or as a
    limit, with a coin of the 42, a side, an entry, a stop on the right side of it, three targets, a close and a unit, each positive;
    with its record's instant, to the second, and kind. In the records' order, then by instant: [(ms, coin, side, close_of, card,
    kind)]."""
    coins = set(own_coins())
    out_ = []
    for rec in records:
        kind = rec.get('kind')
        if kind not in ('daily', 'request', 'alloc', 'check'):
            continue
        try:
            t = ms_of(rec['utc'])
            close_of = str(dt.date.fromisoformat(rec['close_of']))
        except (KeyError, TypeError, ValueError):
            continue
        t -= t % 1000
        placed = None
        if kind == 'alloc' and isinstance(rec.get('alloc'), dict):
            placed = {x.get('coin') for x in (rec['alloc'].get('items') or []) + (rec['alloc'].get('more') or []) if isinstance(x, dict)}
        for cd in rec.get('cards') or []:
            try:
                if not (cd.get('strong') and cd.get('mode') in ('market', 'limit') and cd.get('entry') is not None
                        and (placed is None or cd['coin'] in placed)):
                    continue
                side, E, S = int(cd['side']), float(cd['entry']), float(cd['stop'])
                T = [float(x) for x in cd['targets']]
                ok_ = (cd['coin'] in coins and side in (1, -1) and len(T) == 3 and min(E, S, float(cd['close']), float(cd['U'])) > 0
                       and side * (E - S) > 0)
            except (AttributeError, KeyError, TypeError, ValueError):
                continue
            if ok_:
                out_.append((t, cd['coin'], side, close_of, cd, kind))
    return sorted(out_, key=lambda x: x[0])


def coin_days(records, t_ms):
    """How much history the seed will read, by journal_cards: for each coin the days from its first STRONG card with an entry to t_ms,
    summed - 288 5-minute candles a coin-day - and the coins: (coin-days, coins)."""
    first = {}
    for t, c, _s, _d, _cd, _k in journal_cards(records):
        first.setdefault(c, t)
    return sum((t_ms - t) / DAY_MS for t in first.values()), len(first)


def own_seed(records, k5, k1, daily, fund):
    """The signals TZ-42's seed opens from the journal's records, by this checker's own reading: each card of journal_cards, in time
    order, opens a signal issued at its record's instant unless one of its coin, side and close was opened already, or
    a signal of its coin is still open then - walked by own_walk to that instant on the coin's 5-minute candles k5 and, where its place
    is inside its first minutes, the 1-minute ones k1 holds for that place, unread without them - or the rule's leverage at its stop is
    under 1x. k1: {(coin, place): candles}; fund: coin -> (day -> the funding sum). [(coin, side, close_of, issued ms, mode, entry, stop,
    kind)] in the order of the ids, and for each its open's fields, its place and its events after the seed's walks: [(o, place,
    events)]."""
    opened, states, live = [], [], {}
    for t, coin, side, close_of, cd, kind in journal_cards(records):
        if any(x[0] == coin and x[1] == side and x[2] == close_of for x in opened):
            continue
        j = live.get(coin)
        if j is not None and k5.get(coin) is not None:
            o, st, evs = states[j]
            first = st['t'] % K5_MS != 0
            if not first or (coin, st['t']) in k1:
                got, st = own_walk(o, k5[coin], daily.get(coin) or [], fund(coin), until=t, start=st,
                                   k1=k1.get((coin, st['t']), []) if first else [])
                states[j] = (o, st, evs + got)
                if st['end']:
                    live.pop(coin)
                    j = None
        if j is not None:
            continue
        d_ = abs(float(cd['entry']) - float(cd['stop'])) / float(cd['entry'])
        if math.floor(1 / (1.5 * d_ + 0.01)) < 1:
            continue
        o = {'side': side, 'entry': float(cd['entry']), 'stop': float(cd['stop']), 'targets': [float(x) for x in cd['targets']],
             'utc': iso_of(t), 'valid': iso_of(midnight(dt.date.fromisoformat(close_of) + 2 * DAY)), 'close_of': close_of,
             'mode': cd['mode']}
        evs = [('fill', None, t, o['entry'], None, None)] if cd['mode'] == 'market' else []
        live[coin] = len(states)
        states.append((o, start_of(o), evs))
        opened.append((coin, side, close_of, t, cd['mode'], o['entry'], o['stop'], kind))
    return opened, states


class Candles:
    """A request's candles kept compact - the render holds every one the bot read - and read back as the bot's tuples, (open ms, o,
    h, l, c, closed): the same integers and floats."""
    __slots__ = ('t', 'o', 'h', 'l', 'c', 'x')

    def __init__(self, rows):
        rows = list(rows)
        self.t = array.array('q', (r[0] for r in rows))
        self.o, self.h, self.l, self.c = (array.array('d', (r[k] for r in rows)) for k in (1, 2, 3, 4))
        self.x = bytes(1 if r[5] else 0 for r in rows)

    def __iter__(self):
        return zip(self.t, self.o, self.h, self.l, self.c, (b == 1 for b in self.x))

    def __len__(self):
        return len(self.t)


def union_k5(calls):
    """Every 5-minute candle the calls read of each coin: a coin read once its candles as read, else the last version of each."""
    by = {}
    for c in calls:
        by.setdefault(c['coin'], []).append(c['rows'])
    out_ = {}
    for coin, reads in by.items():
        if len(reads) == 1:
            out_[coin] = reads[0]
            continue
        d = {}
        for rows in reads:
            for r in rows:
                d[r[0]] = r
        out_[coin] = [d[k] for k in sorted(d)]
    return out_


def replay(events, records, calls, daily, fund):
    """Every signal's events by this checker's own reading, replayed on the candles the bot read, in the order it read them: the
    legacy signals the seed opens from the journal's records on the seed's candles (own_seed), then, at each of the reconcile's reads
    of a coin's 5-minute candles, every signal of that coin whose open the registry held before the read and that has not ended, walked
    on that read's candles from its place (own_walk) - with the 1-minute candles read next for that place where it is inside its first
    minutes, and not walked without them. calls: [{'caller' - 'seed' or 'reconcile', 'coin', 'start', 'step', 'rows', 'n_before'}], in
    time order; daily: coin -> [(day, candle)]; fund: coin -> (day -> the funding sum). Returns (the legacy signals own_seed opens, {id:
    events}, {id: place}), the legacy signals numbered 1, 2, ... in their order and the model's by their open events."""
    seed5 = union_k5([c for c in calls if c['caller'] == 'seed' and c['step'] == K5_MS])
    seed1 = {(c['coin'], c['start']): c['rows'] for c in calls if c['caller'] == 'seed' and c['step'] == K1_MS}
    opened, states = own_seed(records, seed5, seed1, daily, fund)
    exp, place, op = {}, {}, {}
    for i, (o, st, evs) in enumerate(states, 1):
        exp[i], place[i], op[i] = list(evs), st, o
    n_open = {}
    for e in events:
        if e.get('type') == 'open':
            n_open[e['id']] = e['n']
            if not e.get('legacy'):
                o = {k: e[k] for k in ('side', 'entry', 'stop', 'targets', 'utc', 'valid', 'close_of', 'mode')}
                op[e['id']], place[e['id']] = o, start_of(o)
                exp[e['id']] = [('fill', None, ms_of(o['utc']), o['entry'], None, None)] if o['mode'] == 'market' else []
    coin_of = {e['id']: e['coin'] for e in events if e.get('type') == 'open'}
    rec = [c for c in calls if c['caller'] == 'reconcile']
    k = 0
    while k < len(rec):
        c = rec[k]
        k += 1
        if c['step'] != K5_MS:
            continue
        ones = {}
        while k < len(rec) and rec[k]['step'] == K1_MS and rec[k]['coin'] == c['coin']:
            ones[rec[k]['start']] = rec[k]['rows']
            k += 1
        for i in sorted(n_open):
            if coin_of[i] != c['coin'] or n_open[i] > c['n_before'] or i not in place or place[i]['end']:
                continue
            first = place[i]['t'] % K5_MS != 0
            if first and place[i]['t'] not in ones:
                continue
            got, place[i] = own_walk(op[i], c['rows'], daily.get(c['coin']) or [], fund(c['coin']), start=place[i],
                                     k1=ones[place[i]['t']] if first else [])
            exp[i] += got
    return opened, exp, place


def same_events(mine, theirs, qty):
    """Whether one signal's events as the bot wrote them, [(type, k, utc ms, price, R, pnl)], are this checker's, [(type, k, utc ms,
    price, R, the result per unit)], the pnl the unit's result times the signal's quantity."""
    close = lambda a, b, rel: (a is None and b is None) or (a is not None and b is not None and abs(a - b) <= rel * max(1.0, abs(a)))
    return len(mine) == len(theirs) and all(
        a[:3] == b[:3] and close(a[3], b[3], 1e-12) and close(a[4], b[4], 1e-9)
        and close(None if a[5] is None else a[5] * qty, b[5], 1e-9) for a, b in zip(mine, theirs))


def registry_checks(text, records, calls, daily, fund, state=None):
    """The registry a bot built, read against this checker's own chain, seed and walks: the chain whole from the genesis; a seed first
    and alone; ids 1, 2, ... in the order of their opens; the legacy signals those own_seed opens from the same journal on the same
    candles, issued at their cards' instants; at most one signal of a coin open at once; every signal's fill, targets and end, with R
    and USDT, those the replay finds on every candle the bot read, in the order it read them; and, given the bot's registry-state.json,
    every signal open there at the replay's place. (checks, the counts printed)."""
    events, broken, _head, whole = own_chain(text)
    sigs = own_signals(events)
    opened, exp, place = replay(events, records, calls, daily, fund)
    legacy = [s for _i, s in sorted(sigs.items()) if s.get('legacy')]
    got = [(s['coin'], s['side'], s['close_of'], ms_of(s['utc']), s['mode'], s['entry'], s['stop'], s['source'].split(':', 1)[-1])
           for s in legacy]
    mism = []
    for i, s in sorted(sigs.items()):
        theirs = [(e['type'], e.get('k'), ms_of(e['utc']), e.get('price'), e.get('R'), e.get('pnl')) for e in events
                  if e.get('id') == i and e.get('type') in ('fill', 'target', 'stop', 'exit', 'expire')]
        if not same_events(exp.get(i, []), theirs, s['qty']):
            mism.append(i)
    opens = [e for e in events if e.get('type') == 'open']
    live_ok, by_coin = True, {}
    for e in opens:
        if any(not _ended_before(events, j, ms_of(e['utc'])) for j in by_coin.get(e['coin'], [])):
            live_ok = False
        by_coin.setdefault(e['coin'], []).append(e['id'])
    checks = {
        'the registry\'s chain is whole from the genesis, every line numbered by its place, the file ending in a newline':
            broken is None and whole and bool(events),
        'its first event is the seed, the only one': bool(events) and events[0].get('type') == 'seed'
            and sum(e.get('type') == 'seed' for e in events) == 1,
        'the signals are numbered 1, 2, ... in the order of their opens': [e['id'] for e in opens] == list(range(1, len(opens) + 1)),
        'the legacy signals are those this checker\'s seed opens from the same journal on the same candles, first and in that order':
            got == opened and all(s['id'] == k for k, s in enumerate(legacy, 1)),
        'no coin holds two signals open at once': live_ok,
        'every signal\'s fill, targets and end, with R and USDT, are those this checker\'s replay finds on the candles the bot read':
            not mism,
    }
    if state is not None:
        cur = state.get('cursor') or {}
        checks['every signal open keeps the replay\'s place: its first candle not walked and its last close passed'] = all(
            str(i) in cur and (cur[str(i)].get('t'), cur[str(i)].get('b')) == (place[i]['t'], place[i]['b'])
            for i, s in sigs.items() if s['end'] is None and i in place)
    return checks, {'events': len(events), 'signals': len(sigs), 'legacy': len(legacy), 'walked': sum(len(v) for v in exp.values()),
                    'mismatches': mism}


def _ended_before(events, i, t):
    """Whether signal i ended at or before the instant t - its stop, exit or expiry stamped then - by the events."""
    return any(e.get('id') == i and e.get('type') in ('stop', 'exit', 'expire') and ms_of(e['utc']) <= t for e in events)


def own_entry(row):
    """The entry and the stop a card offers, by RULE-ADV-3's display rules read here: the stop C - k*U; LONG above the zone a limit at
    its top, else at market while more than 0.25*U above the stop, else no entry; SHORT mirrored; the mark, or the close without one.
    (entry, stop), the entry None where no entry is offered."""
    k, C, U = row['signal'], row['close'], row['U']
    S, P = C - k * U, row.get('mark') or C
    if k > 0:
        entry = C + 0.25 * U if P > C + 0.25 * U else P if P > S + 0.25 * U else None
    else:
        entry = C - 0.25 * U if P < C - 0.25 * U else P if P < S - 0.25 * U else None
    return entry, S


def own_stop_pct(row):
    """The stop's distance in percent of the entry a card offers (own_entry), None where it offers no entry."""
    entry, S = own_entry(row)
    return None if entry is None else 100 * abs(entry - S) / entry


def own_lev(entry, stop):
    """The rule's leverage at a stop, RULE-ADV-3's: at most 20, and so that liquidation lies beyond the stop."""
    d = abs(entry - stop) / entry
    return min(20, math.floor(1 / (1.5 * d + 0.01)))


def pos_ok(p, entry, stop, cap, lev_max, volume=None):
    """One position against this checker's own arithmetic (TZ-42): whole USDT; its loss the notional times its stop's distance and
    both sides' costs; its margin whole, within 0.5 and 4 % of the capital and covering the notional; its leverage 1 to the rule's; its
    quantity the notional over the entry; its risk the loss over the capital; within 0.5 % of the coin's volume where known."""
    rate = abs(entry - stop) / entry + 2 * COST
    return (float(p['notional']).is_integer() and float(p['margin']).is_integer() and abs(p['loss'] - p['notional'] * rate) <= 1e-9 * max(1.0, p['loss'])
            and MARGIN_MIN / 100 * cap - 1e-9 <= p['margin'] <= MARGIN_EXC / 100 * cap and p['margin'] * p['leverage'] >= p['notional']
            and p['margin'] == math.ceil(p['notional'] / p['leverage']) and 1 <= p['leverage'] <= lev_max
            and (not volume or p['notional'] <= LIQ_FRAC * volume + 1e-9) and abs(p['risk_pct'] - 100 * p['loss'] / cap) <= 1e-12 * max(1.0, p['risk_pct'])
            and ('qty' not in p or abs(p['qty'] - p['notional'] / entry) <= 1e-12 * max(1.0, p['qty'])))


def alloc_checks(calls):
    """Every allocation a bot made, read against this checker's own arithmetic (TZ-42): calls [{'prm', 'room', 'liq', 'live' - the
    coins it shared risk among, 'items' - after it, 'rows' - the report's}]. Each wanted risk k times prm's risk times min(|z|, 3) over
    the sum, at most 1 %, never rising along the order; the risk taken within the room - none where the room is spent or below
    nothing - each at most 1 %; each position by pos_ok at the
    card's entry and stop - which are this checker's own (own_entry), within prm's stop limit - the rule's leverage at them its ceiling;
    each item without a position the room's reason or the margin's."""
    wants_ok = room_ok = sized_ok = why_ok = stop_ok = True
    for c in calls:
        prm, items, live = c['prm'], c['items'], c['live']
        q = {it['coin']: min(abs(it['card']['z']), Z_CAP) for it in items if it['coin'] in live}
        w = {coin: min(RISK_MAX, len(live) * prm['risk'] * q[coin] / sum(q.values())) for coin in live}
        seq = [w[coin] for coin in live]
        wants_ok &= all(a >= b - 1e-12 for a, b in zip(seq, seq[1:]))
        sized = [it for it in items if it['coin'] in live and it.get('pos')]
        wants_ok &= all(abs(it['pos']['want'] - w[it['coin']]) < 1e-12 for it in sized)
        room_ok &= (sum(it['pos']['risk_pct'] for it in sized) <= max(0.0, c['room']) + 1e-9 and all(it['pos']['risk_pct'] <= RISK_MAX + 1e-9 for it in sized)
                    and all(it['pos']['risk_pct'] <= w[it['coin']] + 1e-9 for it in sized))
        for it in sized:
            entry, S = own_entry(c['rows'][it['coin']])
            cd = it['card']
            mine = entry is not None and abs(entry - cd['entry']) <= 1e-12 * entry and abs(S - cd['stop']) <= 1e-12 * abs(S)
            stop_ok &= mine and 100 * abs(entry - S) / entry <= prm['stop'] + 1e-9
            sized_ok &= mine and pos_ok(it['pos'], cd['entry'], cd['stop'], prm['capital'], own_lev(cd['entry'], cd['stop']), c['liq'].get(it['coin']))
        why_ok &= all(it.get('code') in ('room', 'margin') and it.get('why') for it in items if it['coin'] in live and not it.get('pos'))
    return {'allocate: each wanted risk k x the risk x min(|z|, 3) over their sum, at most 1 %, never rising along the order': wants_ok,
            'allocate: the risk taken within the room and within what each wanted, each at most 1 %': room_ok,
            'allocate: every position whole, its loss the notional times its stop and both sides\' costs, its margin within 0.5 and 4 % of '
            'the capital and covering it, its leverage 1 to the rule\'s, within 0.5 % of the volume': sized_ok,
            'allocate: an item left without a position has the room\'s reason or the margin\'s': why_ok,
            'allocate: each entry and stop this checker\'s own, the stop within the limit': stop_ok}


def opens_checks(events):
    """Every signal the registry opened, read against this checker's own arithmetic (TZ-42): at the default capital, its position by
    pos_ok at its entry and stop, its leverage at most the rule's there; a legacy signal at most the default risk, a model one at most 1 %;
    its validity the close after its card's, 00:00 UTC two days after the close it is of; a market entry filled at its entry and its
    issue, a limit not filled at its issue."""
    ok_pos = ok_valid = ok_fill = True
    fills = {}
    for e in events:
        if e.get('type') == 'fill' and e['id'] not in fills:
            fills[e['id']] = e
    for e in events:
        if e.get('type') != 'open':
            continue
        p = {k: e[k] for k in ('notional', 'leverage', 'margin', 'loss', 'risk_pct', 'qty')}
        ok_pos &= (e['capital'] == CAPITAL and pos_ok(p, e['entry'], e['stop'], CAPITAL, own_lev(e['entry'], e['stop']))
                   and e['risk_pct'] <= (RISK if e.get('legacy') else RISK_MAX) + 1e-9)
        ok_valid &= ms_of(e['valid']) == midnight(dt.date.fromisoformat(e['close_of']) + 2 * DAY)
        f = fills.get(e['id'])
        ok_fill &= ((f is not None and f['utc'] == e['utc'] and f['price'] == e['entry']) if e['mode'] == 'market'
                    else (f is None or ms_of(f['utc']) > ms_of(e['utc'])))
    return {'every signal opened at the default capital, its position whole by this checker\'s arithmetic at its entry and stop, a legacy '
            'one at most the default 0.5 %, a model one at most 1 %': ok_pos,
            'every signal valid to 00:00 UTC two days after the close it is of': ok_valid,
            'a market entry filled at its entry at its issue, a limit never at its issue': ok_fill}


def model_checks(events, sigs):
    """The registry's model limits (TZ-42), read from the events: at each signal the model opened - not a legacy one - the risk of the
    signals open then, its own included, within 10 %; the model's signals of a close at most 7, less the legacy ones of that close."""
    ok_risk = True
    for e in events:
        if e.get('type') == 'open' and not e.get('legacy'):
            t = ms_of(e['utc'])
            live = [s for i, s in sigs.items() if ms_of(s['utc']) <= t and not _ended_before(events, i, t)]
            ok_risk &= sum(s['risk_pct'] for s in live) <= RISK_TOTAL + 1e-9
    per = {}
    for s in sigs.values():
        per.setdefault(s['close_of'], [0, 0])[1 if s.get('legacy') else 0] += 1
    return {'the model opens a signal only within 10 % of risk, the signals open then counted': ok_risk,
            'the model\'s signals of a close at most 7, less the legacy ones of that close': all(m <= max(0, NEW_MAX - lg) for m, lg in per.values())}


def flags_checks(run, kind):
    """One check's flags against its own content (TZ-42): loud exactly when it announced an end - a stop, an exit, an expiry - or
    opened a signal; one line only where it announced no event and opened none and, at the signal check, held no note and the coins
    not taken for the reasons of the check before, at the fact check no zone left, and no seed; every part of its message with the
    record's flag; a line of one part beginning «✓ » where it is one line."""
    rec, sent, events = run['rec'], run['sent'], run['events']
    announced = [events[n - 1] for n in rec['events'] if 0 < n <= len(events)]
    loud = bool(rec['opened']) or any(e['type'] in ('stop', 'exit', 'expire') for e in announced)
    nothing = not announced and not rec['opened'] and (
        (kind == 'signal' and not rec['notes'] and run['prev_codes'] == rec['excluded_codes']) or (kind == 'fact' and not rec['zones']))
    return (len(announced) == len(rec['events']) and rec['quiet'] == (not loud) and bool(sent) and all(q == rec['quiet'] for _t, q, _k in sent)
            and rec['one_line'] == (nothing and rec['registry']['seeded'] is None)
            and (not rec['one_line'] or (len(sent) == 1 and '\n' not in sent[0][0] and sent[0][0].startswith('✓ '))))


def unit_checks(which, pre, now):
    """UNIT-NEW's and UNIT-OLD's nine readings after a restart: now is what the modes read; pre the snapshot of the kill mark, which
    names the check-done the new process must read at its start."""
    want = (H['adv3'], H['bot_new']) if which == 'new' else (H['adv3'], H['bot_old'])
    return {
        'the unit is active, running and enabled': (now['bot']['ActiveState'], now['bot']['SubState'],
                                                    now['bot']['UnitFileState']) == ('active', 'running', 'enabled'),
        'a new MainPID, one restart more': int(now['bot']['MainPID']) not in (0, int(pre['bot']['MainPID']))
        and int(now['bot']['NRestarts']) == int(pre['bot']['NRestarts']) + 1,
        'the process started after the mark and within 90 s of it': pre['t'] <= now['start'] <= pre['t'] + 90,
        'the process runs the unit\'s exact argv, alone': now['argv'] == ARGV and now['procs'] == [int(now['bot']['MainPID'])],
        'the service copy\'s adv3.py is main\'s and adv3-bot.py the %s one, and the process started after the copy' % which:
            (now['sha_adv3'], now['sha_bot']) == want and now['start'] > now['copy_t'],
        'the unit file is unchanged': now['sha_unit'] == H['unit'],
        'the log shows the new process serving from check-done %s' % pre['read_done']: now['serving'] and now['read'] == pre['read_done'],
        'no traceback in the log since the mark': not now['traceback'],
        'the three capture units unchanged, each active': all(
            now['caps'][u]['ActiveState'] == 'active' and now['caps'][u]['MainPID'] == pre['caps'][u]['MainPID']
            and now['caps'][u]['NRestarts'] == pre['caps'][u]['NRestarts'] for u in CAPTURES),
    }


def first_checks(pre, recs, done_text, log, pid, tail_ok, reg_text, reg_state, seen):
    """G-FIRST's ten readings: the new process's first check - the day's signal check, replayed at its start because the kill mark set
    check-done to the slot before it - from the journal's records stamped since the kill mark, the check-done file and service.log's
    lines since the mark; and the registry it seeded at that check, against seen - the journal as its seed read it, its bytes before
    that check's record: {'sha', 'records', 'cards' - the set of (coin, side, close, ms) of journal_cards over it}."""
    t0 = dt.datetime.fromtimestamp(pre['t'], dt.timezone.utc)
    day = t0.date()
    checks_ = [r for r in recs if r.get('kind') == 'check']
    r = checks_[0] if checks_ else {}
    want_done = '%s %s' % (day, 'fact' if t0.time() >= SLOTS[1][1] else 'signal')
    events, broken, _head, whole = own_chain(reg_text or '')
    sigs = own_signals(events)
    legacy = [s for s in sigs.values() if s.get('legacy')]
    seed = events[0] if events else {}
    reg = r.get('registry') or {}
    ends = ('stop', 'exit', 'expire')
    return {
        'exactly one check record since the mark': len(checks_) == 1,
        'it is the day\'s signal check, of the close of the day before, under rule ee206e7c': (
            r.get('slot') == '%s signal' % day and r.get('close_of') == str(day - DAY) and r.get('rule') == H['rule']),
        'it was sent: its Telegram message ids': bool(r.get('message_ids')) and all(isinstance(x, int) for x in r.get('message_ids') or ['x']),
        'it holds the 42 coins\' state, the six ratings, STRONG at every rank, its cards numbered as it opened them with their positions, '
        'the coins not taken and their codes, the registry\'s head at its events and the seed it made; loud exactly with a new signal or '
        'an end': (
            len(r.get('state') or {}) == 42 and TRUST_KEYS <= set(r.get('trust') or {}) and isinstance(r.get('strong_all'), list)
            and [c.get('id') for c in r.get('cards') or []] == (r.get('opened') or []) and all(c.get('position') for c in r.get('cards') or [])
            and isinstance(r.get('excluded_codes'), list) and isinstance(reg.get('events'), int)
            and reg.get('head') == head_at(reg_text or '', reg['events']) and isinstance(reg.get('seeded'), int)
            and r.get('quiet') == (not r.get('opened') and not any(
                events[n - 1].get('type') in ends for n in r.get('events') or [] if 0 < n <= len(events)))),
        'check-done names the slot it covers: %s' % want_done: done_text == want_done,
        'the log since the mark: the new process serving from check-done %s, the check sent, no check failed and no traceback' % pre['read_done']: (
            ('serving the pinned chat: pid %d ' % pid in log and 'check-done %s' % pre['read_done'] in log) and 'check sent: %s signal' % day in log
            and 'check failed' not in log and 'Traceback' not in log),
        'the journal ends in a newline and every line since the mark parses': tail_ok,
        'the registry is whole from the genesis and ends in a newline; its seed first, naming by SHA-256 and its records the journal as the '
        'seed read it - its lines before that check\'s record': (
            broken is None and whole and seed.get('type') == 'seed' and seed.get('journal_sha') == seen['sha']
            and seed.get('records') == seen['records']),
        'every legacy signal is a STRONG card of that journal with an entry, issued at its record\'s instant': all(
            (s['coin'], s['side'], s['close_of'], ms_of(s['utc'])) in seen['cards'] for s in legacy),
        'the registry\'s state counts every event announced and keeps a place for every signal open': (
            isinstance(reg_state, dict) and reg_state.get('announced') == len(events)
            and all(str(i) in (reg_state.get('cursor') or {}) for i, s in sigs.items() if s['end'] is None)),
    }


def slot_instant(text, slots=SLOTS):
    """The instant of a slot 'YYYY-MM-DD signal|fact' as epoch seconds under slots, or None."""
    try:
        day, kind = text.split()
        at = dict(slots)[kind]
        return calendar.timegm(dt.datetime.combine(dt.date.fromisoformat(day), at).timetuple())
    except (ValueError, KeyError, AttributeError):
        return None


def slot_order(text):
    day, kind = text.split()
    return day, [k for k, _ in SLOTS].index(kind)


def latest_slot_text(t, slots=OLD_SLOTS):
    """The last slot whose instant is at or before the epoch second t, under slots: the running process's, 00:10 and 12:10 UTC, unless
    named."""
    d = dt.datetime.fromtimestamp(t, dt.timezone.utc)
    for kind, at in reversed(slots):
        if d.time() >= at:
            return '%s %s' % (d.date(), kind)
    return '%s %s' % (d.date() - DAY, slots[-1][0])


def replay_text(t):
    """The slot the kill mark writes to check-done: the one before the UTC day's signal check, the day before's fact - so that
    the new process's schedule owes, and runs at its start, the day's signal check."""
    return '%s %s' % (dt.datetime.fromtimestamp(t, dt.timezone.utc).date() - DAY, SLOTS[-1][0])


def clock_checks(recs, done_text):
    """H7, that the clock fires (map §2.7): the journal's check records from the last one naming 2026-11-01 signal - TZ-40's replay at
    its restart; TZ-39's first named that slot too - name strictly later slots, each once; every one after it - at least one - stamped
    at or after its slot's instant under the running code's schedule, 00:10 and 12:10 UTC; and check-done names the last one's slot,
    or that day's fact where the last is a signal check stamped at or after 12:10 UTC. (checks, the delays in seconds)."""
    every = [r for r in recs if r.get('kind') == 'check']
    starts = [k for k, r in enumerate(every) if r.get('slot') == TZ40_REPLAY]
    checks_ = every[starts[-1]:] if starts else []
    slots = [r.get('slot') for r in checks_]
    delays = []
    for r in checks_[1:]:
        at = slot_instant(r.get('slot') or '', OLD_SLOTS)
        try:
            delays.append(dt.datetime.fromisoformat(r['utc']).timestamp() - at)
        except (KeyError, TypeError, ValueError):
            delays.append(None)
    last = checks_[-1] if checks_ else {}
    covered = None
    if (last.get('slot') or '').endswith(' signal'):
        day = last['slot'].split()[0]
        try:
            covered = '%s fact' % day if dt.datetime.fromisoformat(last['utc']).timestamp() >= slot_instant('%s fact' % day, OLD_SLOTS) else None
        except (KeyError, TypeError, ValueError):
            covered = None
    ok_slots = all(slot_instant(x or '', OLD_SLOTS) is not None for x in slots)
    return {
        'H7 the check records from TZ-40\'s replay, the last naming %s, name strictly later slots, each once' % TZ40_REPLAY: (
            bool(slots) and ok_slots and all(slot_order(a) < slot_order(b) for a, b in zip(slots, slots[1:]))),
        'H7 every check after TZ-40\'s replay - at least one - stamped at or after its slot\'s instant': (
            len(checks_) > 1 and all(x is not None and x >= 0 for x in delays)),
        'H7 check-done names the last check\'s slot, or the fact slot its signal check covered': (
            done_text is not None and done_text in (last.get('slot'), covered)),
    }, delays


def served_from(text, pid):
    """The check-done a process logged at its start - 'serving the pinned chat: pid <pid> offset <n> check-done <slot>' - or None."""
    m = None
    for m in re.finditer(r'serving the pinned chat: pid %d offset \d+ check-done (\d{4}-\d{2}-\d{2} (?:signal|fact)|-)$' % pid, text, re.M):
        pass
    return m.group(1) if m else None


def log_since(text, t0, pid):
    """service.log's lines stamped at or after t0 less 1 s, a traceback's lines with them, and whether the process pid logged
    'serving' among them: (serving, the text, a traceback)."""
    keep, tb, serving, on = [], False, False, False
    for line in text.splitlines():
        m = re.match(r'^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})Z (.*)$', line)
        if m:
            on = calendar.timegm(time.strptime(m.group(1), '%Y-%m-%dT%H:%M:%S')) >= t0 - 1
            serving = serving or (on and m.group(2).startswith('serving the pinned chat: pid %d ' % pid))
        if on:
            keep.append(line)
            tb = tb or 'Traceback' in line
    return serving, '\n'.join(keep), tb


def memory_gate(first, second):
    """The memory gate: MemAvailable at the first read, and at the second, 60 s later, taken only where the first fell
    below MEM_FLOOR; the second decides. Returns (passes, the read that decided)."""
    final = first if first >= MEM_FLOOR or second is None else second
    return final >= MEM_FLOOR, final


def number_reading(names):
    return {'CryptoTZ/ holds %s and no other file of that number' % TZ_FILE:
            [n for n in names if n.startswith('CryptoTZ/' + NUMBER)] == [TZ_FILE],
            'CryptoReports/ holds no report of that number': not [n for n in names if n.startswith('CryptoReports/' + NUMBER)]}


def window_reading(t, tz41_report, tz41_work):
    """TZ-41's window: this TZ deploys only before 2026-11-08 07:00:00 UTC, half an hour before TZ-41's band opens, or once TZ-41's
    report is on main; and never while TZ-41's work tree exists."""
    return {'before 2026-11-08 07:00 UTC, or TZ-41\'s report on main': t < TZ41_EDGE or tz41_report,
            'TZ-41\'s work tree absent': not tz41_work}


def tz41_reported():
    rc, so, _ = sh(['git', '-C', PRIMARY, 'ls-tree', '--name-only', 'origin/main', '--', TZ41_REPORT])
    return rc == 0 and so.strip() == TZ41_REPORT


# ---- the modes ----------------------------------------------------------------------------------------------------

def mode_fingerprint():
    text = read(PRIMARY + '/SYSTEM-MAP.md')
    rev, anchors, rows = parse_map(text)
    checks = {'revision ' + MAP_REV: rev == MAP_REV}
    for a, want in ANCHORS.items():
        checks['anchor ' + a] = anchors.get(a) == want
    for a, path in DERIVED.items():
        checks['%s re-derived from %s' % (a, path)] = sha256_file(PRIMARY + '/' + path)[:12] == anchors.get(a)
    states = {}
    for path, lines, nbytes, state, sha in rows:
        states[state] = states.get(state, 0) + 1
        b = read(PRIMARY + '/' + path, 'rb')
        got = (b.count(b'\n'), len(b), sha256_bytes(b))
        out('%-8s %d lines %d bytes %s %s' % (state, got[0], got[1], got[2], path))
        if state == 'frozen':
            checks['frozen ' + path] = got == (lines, nbytes, sha)
    checks['the table holds %d rows, %d frozen, 2 tracked, 1 reported' % (ROWS, FROZEN)] = (
        len(rows) == ROWS and states == {'frozen': FROZEN, 'tracked': 2, 'reported': 1})
    verdict('FINGERPRINT', checks)


def meminfo():
    return {k: int(v.split()[0]) * 1024 for k, v in (l.split(':', 1) for l in read('/proc/meminfo').splitlines())}


def mode_host():
    checks = {}
    rc, so, _ = sh(['find', '/var/lib/btc-recorder', '-mindepth', '1', '-maxdepth', '3', '-name', 'manifest.json', '-print', '-quit'])
    checks['H1 the recorder\'s manifest.json is found'] = rc == 0 and len(so.split()) == 1
    rc, so, _ = sh(['df', '-B1', '--output=source,size,avail', '/var/lib/btc-recorder'])
    src, size, avail = so.splitlines()[1].split()
    checks['H2 /dev/vda2 of 31612203008 bytes'] = (src, size) == ('/dev/vda2', '31612203008')
    rc, so, _ = sh(['grep', '-c', 'e3975b5da44c5328adf3bf3914634cd878842c73', '/var/lib/btc-recorder/runtime.jsonl'])
    checks['H2 the recorder\'s runtime record names e3975b5'] = rc == 0 and int(so) >= 1
    rc, so, _ = sh([PY, '-c', 'import sys; print(sys.version.split()[0])'])
    checks['H3 the venv interpreter is Python 3.12'] = rc == 0 and so.startswith('3.12.')
    units = {u: show(u, 'MainPID', 'NRestarts', 'ActiveState', 'SubState', 'UnitFileState') for u in CAPTURES + (BOT,)}
    for u in CAPTURES:
        checks['H4 %s active and enabled' % u] = (units[u]['ActiveState'], units[u]['UnitFileState']) == ('active', 'enabled')
    b = units[BOT]
    checks['H5 the bot is active, running and enabled'] = (b['ActiveState'], b['SubState'], b['UnitFileState']) == ('active', 'running', 'enabled')
    checks['H5 the bot\'s MainPID runs the unit\'s argv, alone'] = (
        int(b['MainPID']) > 0 and proc_argv(b['MainPID']) == ARGV and procs(ARGV) == [int(b['MainPID'])])
    checks['H5 the service copy holds adv3.py, adv3-bot.py and commit.txt only'] = sorted(os.listdir(SVC)) == ['adv3-bot.py', 'adv3.py', 'commit.txt']
    checks['H5 adv3.py and adv3-bot.py are TZ-40\'s'] = (
        sha256_file(SVC + '/adv3.py') == H['adv3'] and sha256_file(SVC + '/adv3-bot.py') == H['bot_old'])
    checks['H5 the installed unit file is TZ-35\'s'] = sha256_file('/etc/systemd/system/adv3-bot.service') == H['unit']
    checks['H5 commit.txt is 40 hex characters and a newline'] = re.fullmatch(r'[0-9a-f]{40}\n', read(SVC + '/commit.txt')) is not None
    jtext = read(BOTDIR + '/journal.jsonl')
    done_text = read(BOTDIR + '/check-done').strip() if os.path.exists(BOTDIR + '/check-done') else None
    checks['H6 the record holds a journal of whole lines and a check-done naming a slot'] = (
        jtext.endswith('\n') and done_text is not None and slot_instant(done_text, OLD_SLOTS) is not None)
    recs, _ok = records_since(jtext, 0)
    clock, delays = clock_checks(recs, done_text)
    checks.update(clock)
    checks['H8 no registry yet: neither registry.jsonl nor registry-state.json in the record'] = not any(
        os.path.exists(BOTDIR + '/' + f) for f in ('registry.jsonl', 'registry-state.json'))
    for k, v in window_reading(time.time(), tz41_reported(), os.path.exists(TZ41_WORK)).items():
        checks['H8 ' + k] = v
    slots = [r['slot'] for r in recs if r.get('kind') == 'check' and isinstance(r.get('slot'), str)]
    out('check records: %d; slots %s; delays after their instants, seconds: %s; check-done %s' % (
        len(slots), ' '.join(x.replace(' signal', ' s').replace(' fact', ' f') for x in slots),
        ' '.join('-' if x is None else '%.0f' % x for x in delays), done_text or '-'))
    objs = journal_objects(jtext)
    cdays, ncoins = coin_days(objs, time.time() * 1000)
    checks['H9 the journal\'s STRONG cards span at most %d coin-days, the span G-RENDER\'s memory floor was measured at' % COIN_DAYS_MAX] = (
        cdays <= COIN_DAYS_MAX)
    out('journal: %d bytes, %d records, %d STRONG cards with an entry the seed would read, of %d coins over %.1f coin-days' % (
        len(jtext.encode('utf-8')), len(objs), len(journal_cards(objs)), ncoins, cdays))
    first = meminfo()['MemAvailable']
    second = None
    if first < MEM_FLOOR:
        out('MemAvailable %d bytes, below %d: read again after 60 s' % (first, MEM_FLOOR))
        time.sleep(60)
        second = meminfo()['MemAvailable']
    passes, final = memory_gate(first, second)
    checks['memory gate: MemAvailable at least %d bytes, a first read below it read again after 60 s' % MEM_FLOOR] = passes
    checks['disk gate: /dev/vda2 free at least %d bytes' % DISK_FLOOR] = int(avail) >= DISK_FLOOR
    out('units:', json.dumps(units, sort_keys=True))
    out('MemAvailable first %d bytes, second %s, deciding %d; /dev/vda2 free %s bytes' % (first, 'not read' if second is None else second, final, avail))
    verdict('HOST', checks)


def mode_number():
    rc, so, se = sh(['git', '-C', PRIMARY, 'ls-tree', '--name-only', 'origin/main', '--', 'CryptoTZ/', 'CryptoReports/'])
    assert rc == 0, se
    names = so.split('\n')
    for n in names:
        if n.startswith('CryptoTZ/' + NUMBER) or n.startswith('CryptoReports/' + NUMBER):
            out(n)
    verdict('NUMBER', number_reading(names))


def git_show(path):
    rc, so, se = sh(['git', '-C', PRIMARY, 'show', 'origin/main:' + path])
    assert rc == 0, se
    return so


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def mode_rule():
    rule_txt = read(WT + '/advisor/RULE-ADV-3.txt', 'rb')
    unit = read(WT + '/deploy/systemd/adv3-bot.service', 'rb')
    old_bot, new_bot = git_show('advisor/adv3-bot.py'), read(WT + '/advisor/adv3-bot.py')
    od, nd = strip_docs(old_bot), strip_docs(new_bot)
    checks = {
        'RULE-ADV-3.txt is main\'s, byte for byte, hashes to the RULE constant, and is adv3.py\'s':
            rule_txt == git_show('advisor/RULE-ADV-3.txt').encode() and sha256_bytes(rule_txt) == H['rule']
            and ("RULE = '%s'" % H['rule']) in read(WT + '/advisor/adv3.py'),
        'the unit file is main\'s, byte for byte, and hashes to TZ-35\'s': unit == git_show('deploy/systemd/adv3-bot.service').encode()
            and sha256_bytes(unit) == H['unit'],
        'adv3.py and selftest-adv3.py are main\'s, byte for byte - the rule, the report, the card and the ratings untouched': (
            read(WT + '/advisor/adv3.py', 'rb') == git_show('advisor/adv3.py').encode() and sha256_file(WT + '/advisor/adv3.py') == H['adv3']
            and read(WT + '/advisor/selftest-adv3.py', 'rb') == git_show('advisor/selftest-adv3.py').encode()
            and sha256_file(WT + '/advisor/selftest-adv3.py') == H['selftest']),
    }
    checks.update(tree_checks('adv3-bot.py', old_bot, new_bot, BOT_DEFS, BOT_ASG, BOT_SAME))
    checks['adv3-bot.py: %s the same code, their docstrings alone changed' % ' and '.join(DOC_ONLY)] = all(od[k] == nd[k] for k in DOC_ONLY)
    checks['the branch\'s adv3-bot.py is Appendix A\'s'] = sha256_file(WT + '/advisor/adv3-bot.py') == H['bot_new']
    verdict('RULE', checks)


def snapshot():
    """What a mark records: the instant, the bot's and the captures' units, the journal's check records, lines and SHA-256, whether a
    registry exists, and check-done."""
    raw = read(BOTDIR + '/journal.jsonl', 'rb')
    text = raw.decode('utf-8')
    return {'t': time.time(), 'bot': show(BOT, 'MainPID', 'NRestarts', 'ActiveState'),
            'caps': {u: show(u, 'MainPID', 'NRestarts', 'ActiveState') for u in CAPTURES},
            'checks': count_kind(text, 'check'), 'lines': len(journal_lines(text)), 'journal_sha': sha256_bytes(raw),
            'records': len(journal_objects(text)),
            'registry': [f for f in ('registry.jsonl', 'registry-state.json') if os.path.exists(BOTDIR + '/' + f)],
            'check_done': read(BOTDIR + '/check-done').strip() if os.path.exists(BOTDIR + '/check-done') else None}


def put_done(text):
    """check-done replaced in one rename, as the bot's own put writes it."""
    tmp = BOTDIR + '/check-done.tz42'
    with open(tmp, 'w', encoding='utf-8') as fh:
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, BOTDIR + '/check-done')


def mode_mark(name):
    """A mark: the snapshot, kept in state.json. deploy and kill refuse outside TZ-41's window (window_reading), and where a registry
    exists in the record. kill refuses unless check-done names the latest slot of the running code's schedule - the process owes no
    check - and then writes check-done to the slot before the UTC day's signal check, so that the new process replays that check at its
    start (G-FIRST); the old process holds its slot in memory and never reads the file again. rollback writes the kill mark's
    check-done back where the new process never moved it from the replay slot. kill2 writes nothing and records the check-done the old
    code will read at its start."""
    assert name in ('deploy', 'kill', 'rollback', 'kill2'), name
    st = load_state()
    snap = snapshot()
    if name in ('deploy', 'kill'):
        w = window_reading(snap['t'], tz41_reported(), os.path.exists(TZ41_WORK))
        assert all(w.values()), 'outside TZ-41\'s window: %s' % [k for k, v in w.items() if not v]
        assert not snap['registry'], 'a registry exists already: %s' % snap['registry']
    if name == 'kill':
        latest = latest_slot_text(snap['t'])
        assert snap['check_done'] == latest, 'a check is owed: check-done %s, the latest slot %s' % (snap['check_done'], latest)
        snap['read_done'] = replay_text(snap['t'])
        put_done(snap['read_done'])
        assert read(BOTDIR + '/check-done').strip() == snap['read_done'], 'check-done not written'
    if name == 'kill2':
        snap['read_done'] = snap['check_done']
    if name == 'rollback' and 'kill' in st.get('marks', {}):
        kill = st['marks']['kill']
        snap['restored'] = snap['check_done'] == kill['read_done']
        if snap['restored']:
            put_done(kill['check_done'])
            assert read(BOTDIR + '/check-done').strip() == kill['check_done'], 'check-done not restored'
    st.setdefault('marks', {})[name] = snap
    save_state(st)
    out('mark %s at %s: bot pid %s NRestarts %s, %d check records, journal %d lines %s…, registry %s, check-done %s%s' % (
        name, time.strftime('%FT%TZ', time.gmtime(snap['t'])), snap['bot']['MainPID'], snap['bot']['NRestarts'], snap['checks'],
        snap['lines'], snap['journal_sha'][:12], ','.join(snap['registry']) or 'none', snap['check_done'] or '-',
        (' -> %s, replayed by the new process at its start' % snap['read_done']) if name == 'kill'
        else (' -> restored to %s' % st['marks']['kill']['check_done']) if snap.get('restored') else ''))


def mode_copy():
    rc, head, _ = sh(['git', '-C', WT, 'rev-parse', 'HEAD'])
    rc2, up, _ = sh(['git', '-C', WT, 'rev-parse', 'origin/' + BRANCH])
    commit = read(SVC + '/commit.txt')
    verdict('COPY', {
        'the service copy holds adv3.py, adv3-bot.py and commit.txt only': sorted(os.listdir(SVC)) == ['adv3-bot.py', 'adv3.py', 'commit.txt'],
        'adv3.py is main\'s, unchanged': sha256_file(SVC + '/adv3.py') == H['adv3'],
        'adv3-bot.py is Appendix A\'s': sha256_file(SVC + '/adv3-bot.py') == H['bot_new'],
        'commit.txt is the branch head and the worktree\'s HEAD': (
            re.fullmatch(r'[0-9a-f]{40}\n', commit) is not None and rc == 0 and rc2 == 0 and commit.strip() == head.strip() == up.strip()),
        'the branch\'s two files equal the service copy\'s': all(read(WT + '/advisor/' + f, 'rb') == read(SVC + '/' + f, 'rb')
                                                               for f in ('adv3.py', 'adv3-bot.py')),
    })


def own_files():
    return tuple(maybe_sha(BOTDIR + '/' + f) for f in ('journal.jsonl', 'offset', 'daily-sent', 'check-done', 'registry.jsonl',
                                                        'registry-state.json'))


def line_count(path):
    """The lines of a file, read one at a time: a year's journal is never held whole."""
    with open(path, encoding='utf-8') as fh:
        return sum(1 for _line in fh)


def lines_after(path, k):
    """The records of a journal's lines after its first k, each parsed, read one at a time."""
    with open(path, encoding='utf-8') as fh:
        return [json.loads(line) for n, line in enumerate(fh) if n >= k]


def render_run(mod, data):
    """G-RENDER's pipeline on a loaded bot and a Data, its STATE a directory holding a copy of a journal and no registry: the commands
    answered through the bot's handle - the first seeding the registry from the copy - then the signal check and the fact check through
    its check, each at the moment it runs, each record appended to the journal; Telegram a stand-in; every candle request the bot made -
    which function made it and the registry's events before it - every allocation with what it shared risk among and the report it rests
    on, every «сигнал» view and every report captured. Returns what render_checks reads."""
    jpath, rpath = mod.STATE + '/journal.jsonl', mod.STATE + '/' + mod.REG_FILE
    raw = read(jpath, 'rb')
    base_lines = line_count(jpath)
    records0 = journal_objects(raw.decode('utf-8'))

    class Cap(mod.Telegram):
        def __init__(self):
            super().__init__('123456:SECRET', 777)
            self.sent = []

        def call(self, method, http_timeout=30, **params):
            if method == 'sendMessage':
                self.sent.append((params['text'], params.get('disable_notification', False), 'reply_markup' in params))
                return {'message_id': len(self.sent)}
            return True

    cap, texts, runs = Cap(), {}, {}
    calls, allocs, views, reps = [], [], [], []
    real = {k: getattr(mod, k) for k in ('klines', 'allocate', 'signal_view', 'live_report')}

    def k_spy(coin, start_ms, now_ms, step=mod.K5_MS, count=None):
        caller = sys._getframe(1).f_code.co_name
        via = sys._getframe(2).f_code.co_name if caller == 'first_window' else caller
        n_before = line_count(rpath) if os.path.exists(rpath) else 0
        rows = real['klines'](coin, start_ms, now_ms, step, count)
        calls.append({'caller': via, 'coin': coin, 'start': start_ms, 'now': now_ms, 'step': step, 'count': count, 'rows': Candles(rows),
                      'n_before': n_before})
        return rows

    def alloc_spy(items, prm, room, liq):
        live = [it['coin'] for it in items if not it.get('why')]
        real['allocate'](items, prm, room, liq)
        allocs.append({'prm': dict(prm), 'room': room, 'liq': dict(liq), 'live': live, 'items': [dict(it) for it in items],
                       'rows': reps[-1]['rows'] if reps else {}})

    def view_spy(rep, reg, view, prm, now_, new_ids, seeded=None):
        text = real['signal_view'](rep, reg, view, prm, now_, new_ids, seeded)
        views.append((rep, view, dict(prm), dict(new_ids), text))
        return text

    def report_spy(d, deposit, risk):
        r = real['live_report'](d, deposit, risk)
        reps.append(r)
        return r

    mod.klines, mod.allocate, mod.signal_view, mod.live_report = k_spy, alloc_spy, view_spy, report_spy
    buf = io.StringIO()
    case_reps = {}
    try:
        with contextlib.redirect_stdout(buf):
            reg = mod.Registry(mod.STATE)
            for case in RENDER_CASES:
                n0, m0 = len(cap.sent), len(reps)
                mod.handle(cap, data, reg, case)
                texts[case] = cap.sent[n0:]
                case_reps[case] = reps[m0:]
            for kind in ('signal', 'fact'):
                prev = mod.last_check()
                n0, m0 = len(cap.sent), len(reps)
                now = dt.datetime.now(dt.timezone.utc)
                rec = mod.check(cap, data, reg, (now.date(), kind), now)
                mod.append(rec)
                runs[kind] = {'rec': rec, 'sent': cap.sent[n0:], 'rep': reps[m0], 'prev_codes': (prev or {}).get('excluded_codes')}
    finally:
        mod.klines, mod.allocate, mod.signal_view, mod.live_report = real['klines'], real['allocate'], real['signal_view'], real['live_report']
    records = lines_after(jpath, base_lines)
    reg_text = read(rpath) if os.path.exists(rpath) else ''
    sp = mod.STATE + '/' + mod.REG_STATE
    reg_state = json.loads(read(sp)) if os.path.exists(sp) else None
    events = own_chain(reg_text)[0]
    for x in runs.values():
        x['events'] = events
    m, a = mod, mod.adv3
    expect = {'help': m.HELP,
              'consts': (m.CAPITAL, a.RISK, a.RISK_MAX, m.RISK_TOTAL, m.STOP_MAX, m.NEW_MAX, m.MARGIN_MIN, m.MARGIN_MAX, m.MARGIN_EXC,
                         m.LIQ_FRAC, m.Z_CAP, a.COST, m.SLOTS, a.RELIABILITY, m.PACE, a.STRONG_Z, m.K1_MS, m.K5_MS),
              'defaults': dict(m.DEFAULTS), 'usdt': a.usdt}
    daily = {c: sorted(v.items()) for c, v in data.cs.items() if v}
    funds = data.funds or {}
    return {'texts': texts, 'runs': runs, 'records': records, 'log': buf.getvalue(), 'expect': expect, 'calls': calls, 'allocs': allocs,
            'views': views, 'case_reps': case_reps, 'records0': records0, 'jsha': sha256_bytes(raw), 'reg_text': reg_text,
            'reg_state': reg_state, 'daily': daily, 'fund': lambda coin: funds.get(coin) or (lambda d: 3 * a.BASE_F)}


def render_print(r):
    """What G-RENDER prints: sizes, counts and labels, never a coin, a price or a size."""
    events = own_chain(r['reg_text'])[0]
    sigs = own_signals(events)
    one = [c for c in r['calls'] if c['step'] == K1_MS]
    out('replies: %s; the bot\'s log: %d lines; candle requests %d - %d of 1-minute candles - and candles %d; allocations %d; views %d' % (
        ', '.join('%d chars in %d parts' % (sum(len(t) for t, _q, _k in r['texts'][k]), len(r['texts'][k])) for k in RENDER_CASES),
        r['log'].count('\n'), len(r['calls']), len(one), sum(len(c['rows']) for c in r['calls']), len(r['allocs']), len(r['views'])))
    kinds = {}
    for e in events:
        kinds[e.get('type')] = kinds.get(e.get('type'), 0) + 1
    out('registry: %d events %s; %d signals - %d legacy, %d open, %d ended by a stop, %d by an exit, %d expired; the seed of %d records '
        'and %d cards' % (len(events), json.dumps(kinds, sort_keys=True), len(sigs), sum(bool(s.get('legacy')) for s in sigs.values()),
                          sum(s['end'] is None for s in sigs.values()), sum(s['end'] == 'stop' for s in sigs.values()),
                          sum(s['end'] == 'exit' for s in sigs.values()), sum(s['end'] == 'expire' for s in sigs.values()),
                          (events[0] if events else {}).get('records', -1), (events[0] if events else {}).get('cards', -1)))
    for kind, run in r['runs'].items():
        rec = run['rec']
        out('%s check: %s, %s, %d parts; events announced %d; signals opened %d; STRONG at every rank %d; not taken %d, by code %s; notes %d; '
            'zones %d' % (kind, 'quiet' if rec['quiet'] else 'loud', 'one line' if rec['one_line'] else 'full', len(run['sent']),
                          len(rec['events']), len(rec['opened']), len(rec['strong_all']), len(rec['excluded']),
                          json.dumps(sorted({c for _c, _s, c in rec['excluded_codes']})), len(rec['notes']), len(rec['zones'])))


def render_checks(r, same):
    """G-RENDER: what the service copy's bot sent for each command and each check, read against its own registry rebuilt by this
    checker, its allocations against this checker's arithmetic, its views against the plans they were made from, its records and its
    constants; counts and labels only."""
    texts, runs, expect = r['texts'], r['runs'], r['expect']
    usdt = expect['usdt']
    events, _b, head, _w = own_chain(r['reg_text'])
    sigs = own_signals(events)
    checks = {
        'every command and both checks answered, no traceback and no failed request in the bot\'s log':
            all(texts.get(k) for k in RENDER_CASES) and set(runs) == {'signal', 'fact'} and 'Traceback' not in r['log']
            and 'failed' not in r['log'],
        'the markup is balanced in every part of every message (b, i)': all(
            html_balanced(t) for ps in list(texts.values()) + [x['sent'] for x in runs.values()] for t, _q, _k in ps),
    }
    reg_c, counts = registry_checks(r['reg_text'], r['records0'], r['calls'], r['daily'], r['fund'], r['reg_state'])
    checks.update(reg_c)
    checks['the seed names the journal the bot read, by SHA-256 and its records'] = bool(events) and events[0].get('journal_sha') == r['jsha'] \
        and events[0].get('records') == len(r['records0'])
    checks.update(opens_checks(events))
    checks.update(model_checks(events, sigs))
    checks.update(alloc_checks(r['allocs']))
    views_ok = len(r['views']) == 2
    for k, (rep, view, prm, new_ids, text) in enumerate(r['views']):
        views_ok &= [t for t, _q, _k in texts.get(RENDER_CASES[k], [])] == own_chunks(text) and len(view['items']) <= prm['n']
        for it in view['items']:
            p = it.get('pos')
            if p:
                views_ok &= ('Маржа <b>%s USDT</b> · плечо %d× изол. → позиция %s USDT' % (usdt(p['margin']), p['leverage'], usdt(p['notional']))
                             in text and 'Потеря на стопе <b>%s USDT</b>' % usdt(p['loss']) in text)
    checks['each «сигнал» reply is the bot\'s own view sent in its parts, each position written as the plan holds it, at most N items'] = views_ok
    p1 = r['views'][1][2] if len(r['views']) == 2 else {}
    sent1 = '\n'.join(t for t, _q, _k in texts.get(RENDER_CASES[1], []))
    checks['«%s» rests on its parameters - 50,000 USDT, 1 %%, a limit of 2 %%, at most 3 - the defaults unchanged' % RENDER_CASES[1]] = (
        {k: p1.get(k) for k in ('capital', 'risk', 'total', 'stop', 'n', 'set')} == {
            'capital': 50000.0, 'risk': 1.0, 'total': 2.0, 'stop': 14.0, 'n': 3, 'set': ['capital', 'n', 'risk', 'total']}
        and expect['defaults'] == {'capital': CAPITAL, 'risk': RISK, 'total': RISK_TOTAL, 'stop': STOP_MAX, 'n': NEW_MAX, 'set': []}
        and 'Капитал 50 000 USDT · риск 1,0% · лимит 2% · стоп ≤ 14% · до 3 сделок · по запросу: капитал, топ, риск, лимит' in sent1)
    reg_t = '\n'.join(t for t, _q, _k in texts.get(RENDER_CASES[2], []))
    checks['«реестр»: its counts, the chain whole and its fingerprint, the figures'] = (
        reg_t.startswith('📒 <b>ADV-3 · реестр STRONG</b>') and ('Сигналов %d' % len(sigs)) in reg_t and '🔐 Реестр:' in reg_t
        and 'цепочка нарушена' not in reg_t and '<b>Итоги</b>' in reg_t)
    rk = '\n'.join(t for t, _q, _k in texts.get(RENDER_CASES[3], []))
    rep_k = (r['case_reps'].get(RENDER_CASES[3]) or [None])[0]
    rows_k = rep_k['rows'] if rep_k else {}
    order_k = own_order(rows_k, own_coins()) if rep_k else []
    listed = re.findall(r'^\d+\. [🟢🔴] (\S+) (?:LONG|SHORT) · z [^·\n]+· знаки [^·\n]+(· ★)?', rk, re.M)
    checks['«рейтинг»: the rule\'s first seven by this checker\'s own order, ★ exactly on STRONG at every rank'] = (
        bool(rep_k) and [c for c, _s in listed] == order_k[:7] and all((st == '· ★') == (c in own_strong(rows_k, order_k)) for c, st in listed))
    asst = '\n'.join(t for t, _q, _k in texts.get(RENDER_CASES[4], []))
    checks['«оценка»: the rung and the next readings, the six ratings, the registry\'s figures and that they move no rung'] = all(
        k in asst for k in ('рубеж %d из 5' % RUNG, 'после закрытия 28.10.2027', 'Оценка доверия', 'Реестр сигналов бота',
                            'описывает, а не доказывает'))
    checks['«помощь» and an unknown text answer HELP and nothing else'] = (
        [t for t, _q, _k in texts.get(RENDER_CASES[5], [])] == [expect['help']] == [t for t, _q, _k in texts.get(RENDER_CASES[6], [])])
    checks['every reply carries the keyboard on its last part alone and a notification; no check carries it'] = (
        all(ps and ps[-1][2] and not any(k for _t, _q, k in ps[:-1]) and not any(q for _t, q, _k in ps) for ps in texts.values())
        and not any(k for x in runs.values() for _t, _q, k in x['sent']))
    checks['the signal check\'s flags agree with what it announced, opened and found'] = 'signal' in runs and flags_checks(runs['signal'], 'signal')
    checks['the fact check\'s flags agree with what it announced, opened and found'] = 'fact' in runs and flags_checks(runs['fact'], 'fact')

    def record_ok(run, kind):
        rec, rows = run['rec'], run['rep']['rows']
        order = own_order(rows, own_coins())
        reg = rec['registry']
        return (rec['kind'] == 'check' and rec['slot'].endswith(' ' + kind) and len(rec['state']) == 42 and TRUST_KEYS <= set(rec['trust'])
                and rec['rule'] == H['rule'] and rec['close_of'] == run['rep']['close_of'] and rec['strong_all'] == own_strong(rows, order)
                and all(rec['state'][c]['rank'] == k for k, c in enumerate(order, 1)) and [c['id'] for c in rec['cards']] == rec['opened']
                and all(c['position'] for c in rec['cards']) and rec['excluded_codes'] == sorted([c, s, code] for c, s, code, _w, _d in rec['excluded'])
                and reg['head'] == head_at(r['reg_text'], reg['events']) and reg['broken'] is None
                and rec['params'] == {k: expect['defaults'][k] for k in ('capital', 'risk', 'total', 'stop', 'n')})
    checks['the check records: their slots, every coin\'s state ranked by this checker\'s order, STRONG at every rank, the cards numbered as '
           'opened with their positions, the coins not taken with their codes, the registry\'s head at their events, the defaults and the '
           'six ratings'] = set(runs) == {'signal', 'fact'} and record_ok(runs['signal'], 'signal') and record_ok(runs['fact'], 'fact')
    checks['the scratch journal holds, after the bot\'s own records, request, request, registry, ranking, assess, check, check'] = (
        [x.get('kind') for x in r['records']] == RENDER_KINDS)
    checks['the registry\'s state counts every event announced by the last check and keeps a place for every signal open'] = (
        isinstance(r['reg_state'], dict) and r['reg_state'].get('announced') == len(events)
        and all(str(i) in (r['reg_state'].get('cursor') or {}) for i, s in sigs.items() if s['end'] is None))
    checks['the bot\'s own journal, offset, daily-sent and check-done are as before the run, and no registry is written there'] = same is True
    checks['the bot\'s constants are this TZ\'s: 200,000 USDT, 0.5 % and 1 % a trade, 10 % in all, a stop within 14 %, 7 new a close, a '
           'margin of 0.5 to 4 % of the capital and 3.5 % its exception, 0.5 % of the volume, |z| capped at 3, 0.1 % a side, checks at '
           '00:10 and 15:07 UTC, the rung 1, 1.1 s between parts, |z| 1 for STRONG, candles of 1 and 5 minutes'] = expect['consts'] == (
        CAPITAL, RISK, RISK_MAX, RISK_TOTAL, STOP_MAX, NEW_MAX, MARGIN_MIN, MARGIN_MAX, MARGIN_EXC, LIQ_FRAC, Z_CAP, COST, SLOTS, RUNG,
        PACE, STRONG_Z, K1_MS, K5_MS)
    return checks, counts


def mode_render():
    """G-RENDER: the service copy's bot answers the commands and runs both checks on live data, its Telegram a stand-in, its STATE a
    scratch directory holding a copy of the bot's own journal - so the registry it seeds is the one the unit will seed from the same
    records. Its process's peak resident set and its time are printed (map §7 item 145): the mode is its own wrapper."""
    t0, c0 = time.time(), time.process_time()
    os.makedirs(SCRATCH, exist_ok=False)
    shutil.copyfile(BOTDIR + '/journal.jsonl', SCRATCH + '/journal.jsonl')
    own = own_files()
    saved = list(sys.path)
    sys.path.insert(0, SVC)
    try:
        mod = load_module('advbot', SVC + '/adv3-bot.py')
    finally:
        sys.path[:] = saved
    mod.STATE = SCRATCH
    r = render_run(mod, mod.Data())
    same = own == own_files()
    render_print(r)
    checks, counts = render_checks(r, same)
    import resource
    out('replayed: %d events walked; signals whose events differ: %s' % (counts['walked'], counts['mismatches'] or 'none'))
    out('PEAK %d bytes resident; %.2f s of wall, %.2f s of processor' % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024,
                                                                       time.time() - t0, time.process_time() - c0))
    verdict('RENDER', checks)


def mode_unit(which):
    assert which in ('new', 'old'), which
    st = load_state()
    pre = st['marks']['kill' if which == 'new' else 'kill2']
    copy_t = st['marks']['deploy' if which == 'new' else 'rollback']['t']
    bot = show(BOT, 'MainPID', 'NRestarts', 'ActiveState', 'SubState', 'UnitFileState')
    pid = int(bot['MainPID'])
    if pid in (0, int(pre['bot']['MainPID'])) or bot['ActiveState'] != 'active':
        if time.time() - pre['t'] < 100:
            raise NotYet()
    caps = {u: show(u, 'MainPID', 'NRestarts', 'ActiveState') for u in CAPTURES}
    start = proc_start(pid) if pid else 0.0
    serving, text, tb = log_since(read(BOTDIR + '/service.log'), pre['t'], pid)
    now = {'bot': bot, 'caps': caps, 'start': start, 'copy_t': copy_t, 'argv': proc_argv(pid) if pid else None, 'procs': procs(ARGV),
           'sha_adv3': sha256_file(SVC + '/adv3.py'), 'sha_bot': sha256_file(SVC + '/adv3-bot.py'),
           'sha_unit': sha256_file('/etc/systemd/system/adv3-bot.service'), 'serving': serving, 'read': served_from(text, pid),
           'traceback': tb}
    checks = unit_checks(which, pre, now)
    if which == 'old':
        checks['two restarts more than before the first kill'] = int(bot['NRestarts']) == int(st['marks']['kill']['bot']['NRestarts']) + 2
    out('bot: pid %d NRestarts %s started %s; captures: %s' % (pid, bot['NRestarts'], time.strftime('%FT%TZ', time.gmtime(start)),
        json.dumps({u: [c['MainPID'], c['NRestarts']] for u, c in caps.items()}, sort_keys=True)))
    verdict('UNIT-' + which.upper(), checks)


def seen_journal(raw, t0):
    """The journal as the new process's seed read it - its bytes before the first check record stamped since the kill mark at t0 - by
    SHA-256, its records that parse and its STRONG cards with an entry: {'sha', 'records', 'cards'}."""
    pre_bytes, _found = prefix_before_check(raw, t0)
    objs = journal_objects(pre_bytes.decode('utf-8'))
    return {'sha': sha256_bytes(pre_bytes), 'records': len(objs),
            'cards': {(c, s, d, t) for t, c, s, d, _cd, _k in journal_cards(objs)}}


def mode_first():
    st = load_state()
    pre = st['marks']['kill']
    pid = int(show(BOT, 'MainPID')['MainPID'])
    raw = read(BOTDIR + '/journal.jsonl', 'rb')
    jtext = raw.decode('utf-8')
    recs, tail_ok = records_since(jtext, pre['t'])
    if not [r for r in recs if r.get('kind') == 'check']:
        if time.time() - pre['t'] < FIRST_BOUND:
            raise NotYet()
    done_text = read(BOTDIR + '/check-done').strip() if os.path.exists(BOTDIR + '/check-done') else None
    _serving, text, _tb = log_since(read(BOTDIR + '/service.log'), pre['t'], pid)
    reg_text = read(BOTDIR + '/registry.jsonl') if os.path.exists(BOTDIR + '/registry.jsonl') else ''
    try:
        reg_state = json.loads(read(BOTDIR + '/registry-state.json'))
    except (OSError, ValueError):
        reg_state = None
    seen = seen_journal(raw, pre['t'])
    events = own_chain(reg_text)[0]
    sigs = own_signals(events)
    checks_ = [r for r in recs if r.get('kind') == 'check']
    r = checks_[0] if checks_ else {}
    out('first check: %s, %s, %d messages; events announced %d; signals opened %d; STRONG at every rank %d; not taken %d; check-done %s; '
        'registry %d events, %d signals - %d legacy, %d open; the journal the seed read: %d records, %d STRONG cards, %s… (the kill '
        'mark\'s %s…)' % ('quiet' if r.get('quiet') else 'loud', 'one line' if r.get('one_line') else 'full', len(r.get('message_ids') or []),
                         len(r.get('events') or []), len(r.get('opened') or []), len(r.get('strong_all') or []), len(r.get('excluded') or []),
                         done_text or '-', len(events), len(sigs), sum(bool(s.get('legacy')) for s in sigs.values()),
                         sum(s['end'] is None for s in sigs.values()), seen['records'], len(seen['cards']), seen['sha'][:12],
                         pre['journal_sha'][:12]))
    verdict('FIRST', first_checks(pre, recs, done_text, text, pid, tail_ok, reg_text, reg_state, seen))


def kept_files():
    """The work tree's files a report keeps by name: state.json, the two files B-DEPLOY saves, the registry's files B-ASIDE set aside -
    each named with .rolled - where a rollback came after the signal, and every file under logs/; relative to WORK, sorted."""
    names = ['state.json', 'bot.before', 'commit.before'] + [f for f in os.listdir(WORK) if f.endswith('.rolled')]
    for d, _s, fs in os.walk(WORK + '/logs'):
        names += [os.path.relpath(os.path.join(d, f), WORK) for f in fs]
    return sorted(n for n in names if os.path.isfile(os.path.join(WORK, n)))


def mode_keep():
    """B-RECLAIM-OWN's copy: every kept file into the forensic store as tz42-work--<path with - for />, by exclusive create and
    verified whole; the branch worktree must hold nothing but its pushed HEAD."""
    rc, so, _ = sh(['git', '-C', WT, 'status', '--porcelain', '--ignored'])
    assert rc == 0 and so == '', 'keep: %s holds %r' % (WT, so[:400])
    head = sh(['git', '-C', WT, 'rev-parse', 'HEAD'])[1].strip()
    up = sh(['git', '-C', WT, 'rev-parse', '@{u}'])[1].strip()
    assert head and up == head, 'keep: %s at %s, upstream %r' % (WT, head, up)
    count = lambda: sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    before, copied, held = count(), 0, 0
    for rel in kept_files():
        path = WORK + '/' + rel
        h = sha256_file(path)
        dest = FORENSICS + '/tz42-work--' + rel.replace('/', '--')
        if os.path.exists(dest):
            assert sha256_file(dest) == h, 'keep: %s exists with another hash' % dest
            held += 1
            out('K held   %s %s' % (h, dest))
            continue
        with open(path, 'rb') as src, open(dest, 'xb') as dst:
            shutil.copyfileobj(src, dst, 1 << 20)
        assert sha256_file(dest) == h, 'keep: %s did not copy whole' % dest
        copied += 1
        out('K copied %s %s' % (h, dest))
    after = count()
    assert after == before + copied, 'keep: store %d, expected %d' % (after, before + copied)
    out('KEEP PASS: %d files kept, %d copied, %d already held; forensic store %d -> %d files; worktree at %s, its upstream\'s'
        % (copied + held, copied, held, before, after, head))


def mode_stopped():
    bot = show(BOT, 'ActiveState', 'UnitFileState')
    verdict('STOPPED', {'the unit is inactive or failed, and disabled': bot['ActiveState'] in ('inactive', 'failed') and bot['UnitFileState'] == 'disabled',
                        'no process runs under the unit\'s argv': procs(ARGV) == []})


# ---- the self-test ------------------------------------------------------------------------------------------------

def synthetic(bot):
    """A synthetic market of fourteen coins for the stage's bot, Binance stood in for, its last close yesterday (UTC) and its 1- and
    5-minute candles a path to the present moment; and a journal of the cards TZ-35 to TZ-40 published in the four days before, built so
    that the seed opens eight signals - one stopped, one filled in its first minutes on 1-minute candles, one ended by the rule's exit,
    one expired, one filled and stopped, three that run - and skips a card repeated, a card of a coin still open, one not STRONG, one
    without an entry, one broken, one an allocation did not place and one of a record it does not read; and the present close holds a
    coin no longer STRONG with its signal open, one near its stop, one with a stop beyond 14 %, one too thin to trade and one that runs out
    of its zone at the fact check. Returns the Data stand-in."""
    a = bot.adv3
    utc = dt.timezone.utc
    last = dt.datetime.now(utc).date() - DAY
    coins = a.COINS[:14]
    cs, funds, slope = {}, {}, {}
    for n, coin in enumerate(coins):
        c, x = {}, 100.0 + n
        slope[coin] = (0.004 + 0.0015 * n) * (1 if n % 2 == 0 else -1)
        wide = 0.09 if coin == 'UNI' else 0.02
        for i in range(160):
            d = last - (159 - i) * DAY
            prev = x
            x *= (1 + slope[coin]) * (1 + 0.004 * ((i * 7 + n) % 5 - 2))
            if coin == 'BTC' and d == last:
                x = prev * 0.93
            c[d] = (prev, max(prev, x) * (1 + wide), min(prev, x) * (1 - wide), x)
        cs[coin] = c
        funds[coin] = (lambda d: 0.0003) if n % 2 == 0 else (lambda d: 0.0)

    def close_on(coin, d):
        if d <= last:
            return cs[coin][d][3]
        return cs[coin][last][3] * (1 + slope[coin]) ** (d - last).days

    def path(coin, t):
        d = dt.datetime.fromtimestamp(t / 1000, utc).date()
        f = (t - midnight(d)) / DAY_MS
        lo, hi = close_on(coin, d - DAY), close_on(coin, d)
        return lo * (hi / lo) ** f * (1 + 0.002 * math.sin(2 * math.pi * t / 3_600_000))

    def unit_of(coin):
        days = sorted(cs[coin])
        return a.unit(cs[coin], days, len(days) - 1)

    D = last - 4 * DAY
    at = lambda d, h, m=0, s=0: int(dt.datetime.combine(d, dt.time(h, m, s), tzinfo=utc).timestamp() * 1000)
    iso_ = lambda ms: dt.datetime.fromtimestamp(ms / 1000, utc).isoformat(timespec='seconds')

    def card(coin, side, mode, t, close_of, k_e=1.0, k_s=None, k_t=(1.001, 1.5, 2.0), strong=True):
        P = path(coin, t)
        E = P * k_e
        C = close_on(coin, close_of)
        return {'coin': coin, 'side': side, 'strong': strong, 'mode': mode, 'entry': E, 'stop': E * (k_s or (0.5 if side > 0 else 1.5)),
                'targets': [E * k for k in k_t], 'close': C, 'U': C * 0.05, 'since': str(close_of - 10 * DAY), 'rank': 1}
    t1, t2, t3, t4, t5 = at(D + DAY, 0, 10, 30), at(D + DAY, 9), at(D + 2 * DAY, 0, 10), at(D + 2 * DAY, 9), at(D + 3 * DAY, 6)
    A = card('BTC', -1, 'market', t1, D, k_s=1.003, k_t=(0.99, 0.98, 0.97))
    recs = [{'utc': iso_(t1), 'kind': 'check', 'close_of': str(D), 'signals': {'BTC': 1},
             'cards': [A, card('XMR', 1, 'limit', t1, D, k_e=0.9998, k_s=0.9, k_t=(1.001, 1.003, 1.5))],
             'state': {'XMR': {'z': 2.0, 'sum': 4}}},
            {'utc': iso_(t2), 'kind': 'request', 'close_of': str(D),
             'cards': [dict(A, entry=A['entry'] * 1.001), card('BCH', 1, 'market', t2, D, k_t=(2.0, 3.0, 4.0)),
                       card('SKY', 1, 'limit', t2, D, k_e=0.95, k_s=0.9), card('LIT', 1, 'limit', t2, D, k_e=0.9985, k_s=0.99985),
                       card('NEAR', -1, 'market', t2, D, strong=False), dict(card('GRAM', -1, 'market', t2, D), mode='none', entry=None),
                       {'coin': 'ETH'}]},
            {'utc': iso_(t3), 'kind': 'check', 'close_of': str(D + DAY),
             'cards': [card('XMR', 1, 'market', t3, D + DAY), card('BTC', 1, 'market', t3, D + DAY)]},
            {'utc': iso_(t4), 'kind': 'alloc', 'close_of': str(D + DAY), 'alloc': {'items': [{'coin': 'HBAR'}], 'more': []},
             'cards': [card('HBAR', 1, 'market', t4, D + DAY), card('GRAM', -1, 'market', t4, D + DAY)]},
            {'utc': iso_(t4 + 3_600_000), 'kind': 'assess', 'close_of': str(D + DAY), 'cards': [card('XLM', -1, 'market', t4, D + DAY)]},
            {'utc': iso_(t5), 'kind': 'daily', 'close_of': str(D + 2 * DAY),
             'cards': [card('ZEC', -1, 'market', t5, D + 2 * DAY, k_t=(0.999, 0.5, 0.3))]}]
    with open(bot.STATE + '/journal.jsonl', 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(recs[0]) + '\nnot json\n' + ''.join(json.dumps(r) + '\n' for r in recs[1:]))
    seen = {'premium': 0}
    U_ena = unit_of('ENA')

    def mark(coin):
        C = cs[coin][last][3]
        if coin == 'ENA':
            return C - 1.9 * U_ena
        if coin == 'SKY' and seen['premium'] >= 7:
            return C * 1.05
        return C

    def fake_fapi(path_, **p):
        if path_ == '/fapi/v1/premiumIndex':
            seen['premium'] += 1
            return [{'symbol': c + 'USDT', 'markPrice': str(mark(c)), 'lastFundingRate': '0.0001'} for c in coins]
        if path_ == '/fapi/v1/fundingInfo':
            return []
        assert path_ == '/fapi/v1/klines', path_
        coin = p['symbol'][:-4]
        if p['interval'] == '1d':
            vol = {'MORPHO': '1e5', 'LIT': '1e6'}.get(coin, '1e12')
            return [[midnight(last - k * DAY), '1', '1', '1', '1', '0', midnight(last - k * DAY + DAY) - 1, vol] for k in range(8)][::-1]
        step = {'1m': K1_MS, '5m': K5_MS}[p['interval']]
        now_ms = int(time.time() * 1000)
        t, out_ = -(-int(p['startTime']) // step) * step, []
        while t <= now_ms and len(out_) < int(p['limit']):
            o_, c_ = path(coin, t), path(coin, min(t + step, now_ms))
            out_.append([t, repr(o_), repr(max(o_, c_) * 1.0005), repr(min(o_, c_) * 0.9995), repr(c_), '0', t + step - 1, '0'])
            t += step
        return out_

    class Stub:
        def __init__(self):
            self.cs, self.funds, self.missing = cs, funds, []

        def fresh(self):
            return self.cs, self.funds

    a.fapi = fake_fapi
    return Stub()


def rechain(events):
    """A registry's text from its events, each line's n and prev rewritten so that the chain is whole - for the negative controls,
    which must fail on what they change and not on the chain."""
    lines, prev = [], GENESIS
    for k, e in enumerate(events, 1):
        e = dict(e, n=k, prev=prev)
        line = json.dumps(e, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        lines.append(line)
        prev = hashlib.sha256(line.encode('utf-8')).hexdigest()
    return ''.join(x + '\n' for x in lines)


def mode_selftest():
    import copy
    import tempfile
    done = []

    def ok(cond, name):
        done.append(name)
        assert cond, name

    # ---- the pure readings, each with its negative controls -------------------------------------------------------------
    mp = ('**Revision string:** `%s`\n\n| anchor | value |\n|---|---|\n| `A1` — observation set | `229a944f2d51` |\n'
          '| `A3` — phase | `x / y` |\n\n### Fingerprint table\n\n| path | lines | bytes | state | SHA-256 |\n|---|---|---|---|---|\n'
          '| `SYSTEM-MAP.md` | — | — | reported | self-reference |\n| `a/b.py` | 1,135 | 50,928 | frozen | `%s` |\n'
          '| `c.py` | 7 | 8 | tracked | `%s` |\n\n---\n\n## 1. Repository\n| `z.py` | 1 | 1 | frozen | `%s` |\n') % (MAP_REV, 'a' * 64, 'b' * 64, 'c' * 64)
    rev, anchors, rows = parse_map(mp)
    ok(rev == MAP_REV and anchors == {'A1': '229a944f2d51', 'A3': 'x / y'}, 'parse_map: the revision and the anchors')
    ok(rows == [('SYSTEM-MAP.md', None, None, 'reported', None), ('a/b.py', 1135, 50928, 'frozen', 'a' * 64), ('c.py', 7, 8, 'tracked', 'b' * 64)],
       'parse_map: the table\'s rows, thousands separators read, the next section left out')
    old = 'X = 1\nA, B = 1, 2\ndef a():\n    return 1\ndef b():\n    return 2\nclass K:\n    def m(self):\n        return 1\nCMD = 5\ndef gone():\n    pass\n'
    new = 'X = 1\nA, B = 1, 3\ndef a():\n    return 1\ndef b():\n    return 3\nclass K:\n    def m(self):\n        return 1\nNEWC = 0\ndef c():\n    return 0\n'
    T = (({'b'}, {'c'}, {'gone'}), ({'(A, B)'}, {'NEWC'}, {'CMD'}), ('a',))
    good = tree_checks('f', old, new, *T)
    ok(all(good.values()) and len(good) == 3, 'tree_checks: exactly the named definitions and assignments differ - a tuple target named as '
                                              'ast.unparse writes it - the rule\'s among the same, 3 of 3')
    for label, src in (('a definition that should be the same changed', new.replace('def a():\n    return 1', 'def a():\n    return 9')),
                       ('a definition named changed that did not', new.replace('def b():\n    return 3', 'def b():\n    return 2')),
                       ('an extra definition', new + 'def d():\n    return 0\n'),
                       ('an assignment changed and not named', new.replace('X = 1', 'X = 2'))):
        ok(not all(tree_checks('f', old, src, *T).values()), 'tree_checks: %s reads FAIL' % label)
    sd_a = strip_docs('def f():\n    """one"""\n    return 1\ndef g():\n    return 2\n')
    sd_b = strip_docs('def f():\n    """two"""\n    return 1\ndef g():\n    """new"""\n    return 3\n')
    ok(sd_a['f'] == sd_b['f'] and sd_a['g'] != sd_b['g'], 'strip_docs: a docstring alone is the same code; a changed body is not')
    ok(journal_lines('a\nb\r\nc\rd\n') == ['a', 'b', 'c', 'd'] and journal_lines('a\nb') == ['a', 'b']
       and journal_objects('{"k": 1}\n[1]\nx\n{"k": 2}\r\n') == [{'k': 1}, {'k': 2}],
       'journal_lines and journal_objects: universal newlines, as the bot\'s text file reads them; an object a record, a list or a broken line not')
    t_m = calendar.timegm(time.strptime('2026-11-03T09:00:00', '%Y-%m-%dT%H:%M:%S'))
    jl = ('{"utc": "2026-11-03T06:00:00+00:00", "kind": "daily"}\n{"utc": "2026-11-03T09:00:30+00:00", "kind": "request"}\n'
          '{"utc": "2026-11-03T09:00:40+00:00", "kind": "check"}\n{"utc": "2026-11-03T15:07:00+00:00", "kind": "check"}\n')
    rs, okj = records_since(jl, t_m)
    ok([r['kind'] for r in rs] == ['request', 'check', 'check'] and okj and not records_since(jl + 'broken\n', t_m)[1]
       and not records_since(jl.rstrip('\n'), t_m)[1] and records_since('broken\n' + jl, t_m)[1],
       'records_since: the records since the mark; a broken line after it or no final newline reads FAIL, one before it does not')
    ok(count_kind(jl + 'x\n{"kind": "check"}\n', 'check') == 3 and count_kind('', 'check') == 0, 'count_kind: the kind counted, a broken line left out')
    pb, found = prefix_before_check(jl.encode(), t_m)
    ok(found and pb == jl.encode()[:jl.index('{"utc": "2026-11-03T09:00:40')] and prefix_before_check(jl.encode(), t_m + 86400)
       == (jl.encode(), False), 'prefix_before_check: the bytes before the first check record since the mark - a request before it kept')
    ok(own_chunks('a\nb', 3) == ['a\nb'] and own_chunks('aa\nbb\ncc', 5) == ['aa\nbb', 'cc'] and own_chunks('a\n\nb', 1) == ['a', 'b']
       and own_chunks('x' * 9, 4) == ['x' * 9], 'own_chunks: parts at line ends, an empty line beginning a part left out, a long line whole')
    evs0 = [{'type': 'seed', 'utc': 'x'}, {'type': 'open', 'id': 1}, {'type': 'fill', 'id': 1, 'price': 1.0}]
    txt = rechain(evs0)
    e_, br, hd, wh = own_chain(txt)
    ok(br is None and wh and len(e_) == 3 and hd == head_at(txt, 3) and head_at(txt, 0) == GENESIS
       and hd == hashlib.sha256(txt.split('\n')[2].encode()).hexdigest(), 'own_chain and head_at: a whole chain, its head the last line\'s SHA-256')
    lines_ = txt.split('\n')
    ok(own_chain(txt.replace('"price":1.0', '"price":2.0'))[1] is None and own_chain('\n'.join([lines_[0], lines_[2], '']))[1] == 2
       and own_chain(lines_[0] + '\n' + lines_[1].replace('"id":1', '"id":2') + '\n' + lines_[2] + '\n')[1] == 3
       and own_chain(txt + '{"type"')[3] is False, 'own_chain: a removed line breaks it there, an edited one at the line after it; a torn end is not whole')
    d0 = dt.date(2026, 1, 1)
    closes = [100 * 1.01 ** i for i in range(150)] + [100 * 1.01 ** 149 * 0.98 ** k for k in range(1, 40)]
    days = [d0 + i * DAY for i in range(len(closes))]
    daily = [(d, (cl, cl * 1.002, cl * 0.998, cl)) for d, cl in zip(days, closes)]
    ok(sign_sum(days, closes, 120) == 4 and sign_sum(days, closes, 100) is None, 'sign_sum: four agreeing signs on a rising line, none before 112 days')
    DD = days[149]
    iss = midnight(DD + DAY) + 600_000
    o = {'side': 1, 'entry': 100.0, 'stop': 90.0, 'targets': [110.0, 120.0, 130.0], 'utc': iso_of(iss), 'valid': iso_of(midnight(DD + 2 * DAY)),
         'close_of': str(DD), 'mode': 'market'}
    K = lambda *rows, start=iss, w=K5_MS, closed=True: [(start + k * w, *r, closed) for k, r in enumerate(rows)]
    zero = lambda d: 0.0
    kind_of = lambda evs: [(e[0], e[1], e[3]) for e in evs]
    ev1, _s = own_walk(o, K((100, 105, 98, 104), (104, 111, 103, 110), (110, 121, 108, 120), (120, 121, 89, 95)), daily, zero)
    ok(kind_of(ev1) == [('target', 1, 110), ('target', 2, 120), ('stop', None, 90)] and abs(ev1[2][4] - (-10 - 0.001 * 190) / 10) < 1e-12
       and abs(ev1[2][5] - (-10.19)) < 1e-12, 'own_walk: two targets then the stop at 90, -1.019 R, -10.19 a unit')
    ok(kind_of(own_walk(o, K((100, 111, 89, 95)), daily, zero)[0]) == [('stop', None, 90)]
       and kind_of(own_walk(o, K((85, 86, 80, 82)), daily, zero)[0]) == [('stop', None, 85)]
       and kind_of(own_walk(o, K((112, 113, 89, 95)), daily, zero)[0]) == [('target', 1, 110), ('stop', None, 90)],
       'own_walk: a target and the stop in one candle the stop alone; an open beyond the stop ends there; an open past a target credits it first')
    ol = dict(o, mode='limit')
    ok(kind_of(own_walk(ol, K((105, 106, 101, 102), (102, 103, 99, 100)), daily, zero)[0]) == [('fill', None, 100.0)]
       and kind_of(own_walk(ol, K((98, 99, 97, 98)), daily, zero)[0]) == [('fill', None, 98)]
       and kind_of(own_walk(ol, K((101, 101, 89, 90)), daily, zero)[0]) == [('fill', None, 100.0), ('stop', None, 90)],
       'own_walk: a limit filled at itself, at an open past it, and filled and stopped in one candle')
    ev9, _s = own_walk(ol, K(*[(105, 105.5, 104.5, 105)] * 300), [], zero)
    ok(kind_of(ev9) == [('expire', None, None)] and ev9[0][2] == midnight(DD + 2 * DAY), 'own_walk: a limit not reached expires at its validity')
    x_i = next(i for i in range(150, len(closes)) if sign_sum(days, closes, i) < 2)
    E_ = closes[149]
    ox = dict(o, entry=E_, stop=E_ * 0.5, targets=[E_ * 2, E_ * 3, E_ * 4])
    evx, _s = own_walk(ox, K(*[(E_, E_ * 1.0001, E_ * 0.9999, E_)] * ((x_i - 149 + 2) * 288)), daily, lambda d: 0.0003)
    fund_ = sum(0.0003 * closes[i] for i in range(150, x_i + 1))
    ok(kind_of(evx) == [('exit', None, closes[x_i])] and evx[0][2] == midnight(days[x_i] + DAY)
       and abs(evx[0][4] - ((closes[x_i] - E_) - 0.001 * (E_ + closes[x_i]) - fund_) / (E_ * 0.5)) < 1e-12,
       'own_walk: a long ends at the first close whose sum of signs leaves +2, at that close, the funding of every close held paid')
    o2 = dict(o, utc=iso_of(iss + 20_000))
    st2 = start_of(o2)
    M = lambda *rows: K(*rows, start=st2['t'], w=K1_MS)
    ev12, _s = own_walk(o2, K((100, 111, 99, 110), start=iss + K5_MS), daily, zero, k1=M((100, 101, 99, 100), (100, 100, 89, 91)))
    ev13, s13 = own_walk(o2, K((100, 111, 99, 110), start=iss + K5_MS), daily, zero, k1=M(*[(100, 101, 99, 100)] * 4))
    ok(st2['t'] == iss + K1_MS and kind_of(ev12) == [('stop', None, 90)] and ev12[0][2] == iss + 2 * K1_MS
       and kind_of(ev13) == [('target', 1, 110)] and ev13[0][2] == iss + K5_MS and s13['t'] == iss + 2 * K5_MS,
       'own_walk and start_of: an issue at 00:10:20 starts at 00:11, its first minutes on 1-minute candles, then 5-minute ones')
    ev15, s15 = own_walk(o2, K((100, 111, 99, 110), start=iss + K5_MS), daily, zero, until=iss + 3 * K1_MS + 1,
                         k1=M(*[(100, 101, 99, 100)] * 4))
    ok(ev15 == [] and s15['t'] == iss + 3 * K1_MS, 'own_walk: until stops at the candle closing after it')
    rec_j = [{'utc': '2026-11-01T00:10:30+00:00', 'kind': 'check', 'close_of': '2026-10-31',
              'cards': [{'coin': 'BTC', 'side': 1, 'strong': True, 'mode': 'market', 'entry': 100.0, 'stop': 90.0, 'targets': [110, 120, 130],
                         'close': 100.0, 'U': 5.0},
                        {'coin': 'BTC', 'side': 1, 'strong': False, 'mode': 'market', 'entry': 100.0, 'stop': 90.0, 'targets': [1, 2, 3],
                         'close': 1, 'U': 1},
                        {'coin': 'ETH', 'side': 1, 'strong': True, 'mode': 'none', 'entry': None},
                        {'coin': 'DOGE', 'side': 1, 'strong': True, 'mode': 'market', 'entry': 1.0, 'stop': 0.9, 'targets': [1, 2, 3], 'close': 1, 'U': 1},
                        {'coin': 'ETH', 'side': 1, 'strong': True, 'mode': 'limit', 'entry': 1.0, 'stop': 1.1, 'targets': [1, 2, 3], 'close': 1, 'U': 1}]},
             {'utc': '2026-11-01T09:00:00.700+00:00', 'kind': 'alloc', 'close_of': '2026-10-31', 'alloc': {'items': [{'coin': 'SOL'}], 'more': []},
              'cards': [{'coin': c, 'side': 1, 'strong': True, 'mode': 'market', 'entry': 1.0, 'stop': 0.9, 'targets': [1, 2, 3], 'close': 1, 'U': 1}
                        for c in ('SOL', 'XRP')]},
             {'utc': '2026-11-01T10:00:00+00:00', 'kind': 'assess', 'close_of': '2026-10-31', 'cards': rec_j_cards()}]
    jc = journal_cards(rec_j)
    ok([(c, k) for _t, c, _s, _d, _cd, k in jc] == [('BTC', 'check'), ('SOL', 'alloc')] and jc[1][0] % 1000 == 0,
       'journal_cards: a STRONG card with an entry of the 42, its stop on its side, of a record the seed reads - of an allocation the coin '
       'placed - at its record\'s second; not STRONG, no entry, not of the 42, a stop on the wrong side, not placed, an assess record left out')
    cdj, ncj = coin_days(rec_j, ms_of('2026-11-03T09:00:00+00:00'))
    ok(ncj == 2 and abs(cdj - ((ms_of('2026-11-03T09:00:00+00:00') - ms_of('2026-11-01T00:10:30+00:00'))
                               + (ms_of('2026-11-03T09:00:00+00:00') - ms_of('2026-11-01T09:00:00+00:00'))) / DAY_MS) < 1e-9,
       'coin_days: each coin\'s days from its first card, summed')
    calls_s = [{'caller': 'seed', 'coin': 'BTC', 'start': 0, 'step': K5_MS, 'rows': K((100, 101, 99, 100)), 'n_before': 1}]
    rec_s = [{'utc': iso_of(iss), 'kind': 'daily', 'close_of': str(DD), 'cards': [dict(jc[0][4], entry=100.0)]},
             {'utc': iso_of(iss + 60_000), 'kind': 'request', 'close_of': str(DD), 'cards': [dict(jc[0][4], entry=101.0)]},
             {'utc': iso_of(iss + 120_000), 'kind': 'request', 'close_of': str(DD + DAY), 'cards': [dict(jc[0][4], entry=102.0)]},
             {'utc': iso_of(iss + 30 * K5_MS), 'kind': 'check', 'close_of': str(DD + DAY), 'cards': [dict(jc[0][4], entry=103.0, stop=102.9)]}]
    opened, states = own_seed(rec_s, union_k5(calls_s), {}, {'BTC': daily}, lambda c: zero)
    ok([x[2] for x in opened] == [str(DD)] and len(states) == 1,
       'own_seed: one signal of a coin, side and close; a card of another close while it is open is not a new signal')
    rows_o = {'A': {'signal': 1, 'z': 2.0, 'sum': 4, 'U': 1.0}, 'B': {'signal': -1, 'z': -3.0, 'sum': -4, 'U': 1.0},
              'C': {'signal': 1, 'z': 2.0, 'sum': 2, 'U': 1.0}, 'D': {'signal': 0, 'z': 9.0, 'sum': 0, 'U': 1.0},
              'E': {'signal': 1, 'z': 0.9, 'sum': 4, 'U': 1.0}, 'F': {'signal': -1, 'z': None, 'sum': None, 'U': 1.0}, 'G': {'signal': None}}
    ord_o = own_order(rows_o, list(rows_o))
    ok(ord_o == ['B', 'A', 'C', 'E'] and own_strong(rows_o, ord_o) == ['B', 'A'],
       'own_order and own_strong: by |z|, ties in the coins\' order; STRONG four agreeing signs and |z| at least 1')
    r_l = {'signal': 1, 'close': 100.0, 'U': 8.0}
    ok(own_entry(dict(r_l, mark=101.0)) == (101.0, 92.0) and own_entry(dict(r_l, mark=103.0)) == (102.0, 92.0)
       and own_entry(dict(r_l, mark=93.5))[0] is None and own_entry(dict(r_l, mark=None)) == (100.0, 92.0)
       and own_entry(dict(r_l, signal=-1, mark=97.0)) == (98.0, 108.0) and abs(own_stop_pct(dict(r_l, mark=101.0)) - 100 * 9 / 101) < 1e-12
       and own_lev(100.0, 92.0) == 7 and own_lev(100.0, 1.0) == 0,
       'own_entry, own_stop_pct and own_lev: at market in the zone, a limit at its edge past it, none near the stop, the close without a mark, '
       'a short mirrored; the rule\'s leverage')
    pz = {'notional': 12195, 'leverage': 7, 'margin': 1743, 'loss': 12195 * 0.082, 'risk_pct': 100 * 12195 * 0.082 / CAPITAL, 'qty': 121.95}
    ok(pos_ok(pz, 100.0, 92.0, CAPITAL, 7), 'pos_ok: 12,195 USDT at 7x, a margin of 1,743, the loss with both sides\' costs')
    for label, bad_p in (('a margin under 0.5 %', dict(pz, leverage=13, margin=939)), ('a margin above 4 %', dict(pz, notional=63000, margin=9000)),
                         ('a leverage above the rule\'s', dict(pz, leverage=8, margin=1525)), ('a loss not the arithmetic\'s', dict(pz, loss=900.0)),
                         ('a fractional notional', dict(pz, notional=12195.5)), ('a quantity not the notional\'s', dict(pz, qty=120.0))):
        ok(not pos_ok(bad_p, 100.0, 92.0, CAPITAL, 7), 'pos_ok: %s reads FAIL' % label)
    t_k = calendar.timegm(time.strptime('2026-11-03T09:00:00', '%Y-%m-%dT%H:%M:%S'))
    ok([latest_slot_text(t_k), latest_slot_text(t_k + 4 * 3600), latest_slot_text(t_k - 9 * 3600 + 1), latest_slot_text(t_k + 7 * 3600, SLOTS),
        replay_text(t_k), replay_text(t_k + 7 * 3600)]
       == ['2026-11-03 signal', '2026-11-03 fact', '2026-11-02 fact', '2026-11-03 fact', '2026-11-02 fact', '2026-11-02 fact'],
       'latest_slot_text and replay_text: the running code\'s 00:10 and 12:10, the new 15:07; the replay the day before\'s fact')
    ok(slot_instant('2026-11-03 fact') - slot_instant('2026-11-03 fact', OLD_SLOTS) == 2 * 3600 + 57 * 60 and slot_instant('x') is None,
       'slot_instant: the fact slot at 15:07 under the new schedule, 12:10 under the old; a text not a slot None')
    srv = ('2026-11-03T09:01:00Z serving the pinned chat: pid 11 offset 9 check-done 2026-11-02 fact\n'
           '2026-11-03T09:01:01Z serving the pinned chat: pid 12 offset 9 check-done -')
    ok(served_from(srv, 11) == '2026-11-02 fact' and served_from(srv, 12) == '-' and served_from(srv, 13) is None,
       'served_from: the check-done a process logged at its start, \'-\' for none, None for a pid that did not serve')
    mk = lambda slot, u: {'kind': 'check', 'slot': slot, 'utc': u}
    good_c = [{'kind': 'daily', 'utc': '2026-11-01T06:00:00+00:00'}, mk('2026-11-01 signal', '2026-11-01T06:51:46+00:00'),
              mk('2026-11-01 fact', '2026-11-01T12:10:09+00:00'), mk('2026-11-01 signal', '2026-11-01T18:06:27+00:00'),
              mk('2026-11-02 signal', '2026-11-02T00:10:12+00:00'), {'kind': 'request', 'utc': '2026-11-02T08:00:00+00:00'},
              mk('2026-11-02 fact', '2026-11-02T12:15:30+00:00')]
    ck_, dl_ = clock_checks(good_c, '2026-11-02 fact')
    ok(all(ck_.values()) and len(ck_) == 3 and [round(x) for x in dl_] == [12, 330],
       'clock_checks: from TZ-40\'s replay - TZ-39\'s first and its fact before it not read - slots each once, each after its instant: 3 of 3')
    for label, recs_, done_ in (('a slot twice', good_c + [mk('2026-11-02 fact', '2026-11-02T12:20:00+00:00')], '2026-11-02 fact'),
                                ('a check before its slot', good_c[:4] + [mk('2026-11-02 signal', '2026-11-02T00:09:00+00:00')], '2026-11-02 signal'),
                                ('no check after TZ-40\'s replay', good_c[:4], '2026-11-01 fact'), ('no replay', good_c[4:], '2026-11-02 fact'),
                                ('a check-done not the last', good_c, '2026-11-02 signal'), ('no check-done', good_c, None)):
        ok(not all(clock_checks(recs_, done_)[0].values()), 'clock_checks: %s reads FAIL' % label)
    ok(all(window_reading(TZ41_EDGE - 1, False, False).values()) and all(window_reading(TZ41_EDGE + 1, True, False).values())
       and not all(window_reading(TZ41_EDGE, False, False).values()) and not all(window_reading(0, True, True).values()),
       'window_reading: before 2026-11-08 07:00 UTC or after TZ-41\'s report, never beside its work tree')
    pre = {'t': 1000.0, 'bot': {'MainPID': '10', 'NRestarts': '2'}, 'read_done': '2026-11-02 fact',
           'caps': {u: {'MainPID': str(i), 'NRestarts': '0', 'ActiveState': 'active'} for i, u in enumerate(CAPTURES, 20)}}
    now = {'bot': {'MainPID': '11', 'NRestarts': '3', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'enabled'},
           'caps': dict(pre['caps']), 'start': 1035.0, 'copy_t': 990.0, 'argv': ARGV, 'procs': [11], 'sha_adv3': H['adv3'],
           'sha_bot': H['bot_new'], 'sha_unit': H['unit'], 'serving': True, 'read': '2026-11-02 fact', 'traceback': False}
    ok(all(unit_checks('new', pre, now).values()) and len(unit_checks('new', pre, now)) == 9, 'unit_checks: a clean restart reads 9 of 9')
    for key, val, label in (('read', '2026-11-03 signal', 'a process that read another check-done'), ('start', 1200.0, 'a start 200 s after the mark'),
                            ('sha_bot', H['bot_old'], 'the old bot'), ('traceback', True, 'a traceback'), ('procs', [11, 12], 'a second process'),
                            ('serving', False, 'no serving line'), ('sha_unit', 'x', 'another unit file')):
        ok(not all(unit_checks('new', pre, dict(now, **{key: val})).values()), 'unit_checks: %s reads FAIL' % label)
    ok(not all(unit_checks('new', pre, dict(now, caps={u: dict(c, NRestarts='1') for u, c in pre['caps'].items()})).values())
       and all(unit_checks('old', pre, dict(now, sha_bot=H['bot_old'])).values()), 'unit_checks: a capture restarted reads FAIL; the rollback the old bot')
    t0 = calendar.timegm(time.strptime('2026-11-02T14:00:00', '%Y-%m-%dT%H:%M:%S'))
    pre_f = dict(pre, t=float(t0), read_done='2026-11-01 fact', journal_sha='j')
    ev_f = [{'type': 'seed', 'utc': '2026-11-02T14:00:40+00:00', 'journal_sha': 'j' * 64, 'records': 3, 'cards': 1},
            {'type': 'open', 'id': 1, 'utc': '2026-11-01T00:10:30+00:00', 'coin': 'BTC', 'side': 1, 'close_of': '2026-10-31', 'legacy': True},
            {'type': 'fill', 'id': 1, 'utc': '2026-11-01T00:10:30+00:00', 'price': 1.0},
            {'type': 'open', 'id': 2, 'utc': '2026-11-02T14:00:45+00:00', 'coin': 'ETH', 'side': 1, 'close_of': '2026-11-01', 'legacy': False}]
    rt = rechain(ev_f)
    seen = {'sha': 'j' * 64, 'records': 3, 'cards': {('BTC', 1, '2026-10-31', ms_of('2026-11-01T00:10:30+00:00'))}}
    rec = {'utc': '2026-11-02T14:00:50+00:00', 'kind': 'check', 'slot': '2026-11-02 signal', 'close_of': '2026-11-01', 'rule': H['rule'],
           'message_ids': [5, 6], 'state': {str(k): {} for k in range(42)}, 'trust': {k: 0 for k in TRUST_KEYS}, 'strong_all': [],
           'cards': [{'id': 2, 'position': {'notional': 1}}], 'opened': [2], 'excluded_codes': [], 'events': [],
           'registry': {'events': 4, 'head': head_at(rt, 4), 'seeded': 1}, 'quiet': False}
    log_f = ('2026-11-02T14:00:35Z serving the pinned chat: pid 11 offset 9 check-done 2026-11-01 fact\n'
             '2026-11-02T14:00:50Z check sent: 2026-11-02 signal for the close of 2026-11-01 | events 0 | new 1 | loud | full')
    rstate = {'announced': 4, 'cursor': {'1': {}, '2': {}}}
    fargs = ([rec], '2026-11-02 signal', log_f, 11, True, rt, rstate, seen)
    good = first_checks(pre_f, *fargs)
    ok(all(good.values()) and len(good) == 10, 'first_checks: the replayed signal check after a 14:00 restart, the registry it seeded, 10 of 10')
    ok(all(first_checks(dict(pre_f, t=float(t0 + 2 * 3600)), [rec], '2026-11-02 fact', log_f.replace('14:00:35', '16:00:35'), 11, True,
                        rt, rstate, seen).values()), 'first_checks: a 16:00 restart, after 15:07, wants check-done at the fact slot')
    for label, k, v in (('no check record', 0, []), ('two check records', 0, [rec, rec]), ('another slot', 0, [dict(rec, slot='2026-11-02 fact')]),
                        ('no message ids', 0, [dict(rec, message_ids=[])]), ('a quiet check that opened a signal', 0, [dict(rec, quiet=True)]),
                        ('cards not as opened', 0, [dict(rec, opened=[3])]), ('a head not the registry\'s', 0,
                                                                              [dict(rec, registry=dict(rec['registry'], head='x'))]),
                        ('check-done at the fact before 15:07', 1, '2026-11-02 fact'), ('a failed check in the log', 2, log_f + '\ncheck failed: x'),
                        ('another pid serving', 3, 12), ('a broken journal', 4, False), ('a broken registry', 5, rt.replace('"price":1.0', '"price":2.0', 1)),
                        ('a seed naming another journal', 7, dict(seen, sha='k' * 64)), ('a legacy signal not of the journal', 7, dict(seen, cards=set())),
                        ('a state that does not count the events', 6, {'announced': 3, 'cursor': {'1': {}, '2': {}}}),
                        ('no place for a signal open', 6, {'announced': 4, 'cursor': {'1': {}}})):
        a_ = list(fargs)
        a_[k] = v
        ok(not all(first_checks(pre_f, *a_).values()), 'first_checks: %s reads FAIL' % label)
    log = ('2026-10-31T06:00:01Z daily sent\n2026-10-31T09:00:00Z serving the pinned chat: pid 11 offset 5 check-done -\n'
           'Traceback (most recent call last):\n  File x\n2026-10-31T09:00:30Z check sent: 2026-10-31 signal')
    t_l = calendar.timegm(time.strptime('2026-10-31T08:59:59', '%Y-%m-%dT%H:%M:%S'))
    s_, text_, tb_ = log_since(log, t_l, 11)
    ok(s_ and tb_ and 'daily sent' not in text_ and '  File x' in text_ and not log_since(log, t_l, 12)[0],
       'log_since: the lines since the mark, a traceback\'s with them, the serving pid found')
    ok(memory_gate(MEM_FLOOR, None) == (True, MEM_FLOOR) and memory_gate(MEM_FLOOR - 1, MEM_FLOOR) == (True, MEM_FLOOR)
       and memory_gate(MEM_FLOOR - 1, MEM_FLOOR - 2) == (False, MEM_FLOOR - 2), 'memory_gate: a first read below the floor is decided by the second')
    ok(all(number_reading([TZ_FILE, 'CryptoTZ/TZ-41-x.md']).values()) and not all(number_reading([TZ_FILE, 'CryptoTZ/TZ-42-other.md']).values())
       and not all(number_reading([TZ_FILE, 'CryptoReports/TZ-42-x-report.md']).values()), 'number: one file of the number PASS; two, or a report, FAIL')
    with tempfile.TemporaryDirectory() as tmp:
        os.makedirs(tmp + '/logs/sub')
        os.makedirs(tmp + '/render-state')
        for rel in ('state.json', 'bot.before', 'adv3.before', 'commit.before', 'registry.jsonl.rolled', 'registry-state.json.tmp.rolled',
                    'logs/01-a.log', 'logs/sub/02-b.log', 'x.txt', 'render-state/journal.jsonl'):
            with open(tmp + '/' + rel, 'w') as fh:
                fh.write(rel)
        saved_work = WORK
        globals().update(WORK=tmp)
        try:
            kept = kept_files()
        finally:
            globals().update(WORK=saved_work)
    ok(kept == ['bot.before', 'commit.before', 'logs/01-a.log', 'logs/sub/02-b.log', 'registry-state.json.tmp.rolled', 'registry.jsonl.rolled',
               'state.json'],
       'kept_files: the named files, a registry set aside, and the logs; nothing else - not adv3.before, which B-DEPLOY no longer saves, '
       'nor the render\'s scratch journal')

    # ---- G-RENDER on the stage's own bot and a synthetic market ---------------------------------------------------------
    here = os.path.dirname(os.path.abspath(__file__))
    stage = os.path.join(os.path.dirname(here), 'advisor')
    real_sleep = time.sleep
    with tempfile.TemporaryDirectory() as tmp:
        saved = list(sys.path)
        sys.path.insert(0, stage)
        try:
            bot = load_module('advbot_selftest', stage + '/adv3-bot.py')
        finally:
            sys.path[:] = saved
        bot.STATE = tmp
        real_fapi = bot.adv3.fapi
        time.sleep = lambda x: None
        try:
            data = synthetic(bot)
            r = render_run(bot, data)
        finally:
            bot.adv3.fapi = real_fapi
            time.sleep = real_sleep
    checks, counts = render_checks(r, True)
    ok(all(checks.values()) and len(checks) == 34, 'render_checks: the stage\'s bot on a synthetic market reads 34 of 34 - %s'
       % [k for k, v in checks.items() if not v])
    events = own_chain(r['reg_text'])[0]
    sigs = own_signals(events)
    ok({e['type'] for e in events} == {'seed', 'open', 'fill', 'target', 'stop', 'exit', 'expire'} and not counts['mismatches']
       and [s['coin'] for _i, s in sorted(sigs.items()) if s.get('legacy')] == ['BTC', 'XMR', 'BCH', 'SKY', 'LIT', 'BTC', 'HBAR', 'ZEC']
       and [(s['end'], s['hit'] > 0) for _i, s in sorted(sigs.items()) if s.get('legacy')]
       == [('stop', False), (None, True), ('exit', False), ('expire', False), ('stop', False), (None, True), (None, True), (None, True)],
       'the synthetic registry meets every event: the seed\'s eight legacy signals - stopped, filled and two targets on, ended by the rule\'s '
       'exit, expired, filled and stopped, three a target and on - and the cards it skips')
    xmr = next(s for s in sigs.values() if s['coin'] == 'XMR' and s.get('legacy'))
    fill = next(e for e in events if e.get('id') == xmr['id'] and e['type'] == 'fill')
    ok(ms_of(fill['utc']) % K5_MS != 0 and ms_of(fill['utc']) < ceil_to(ms_of(xmr['utc']), K5_MS)
       and any(c['step'] == K1_MS and c['caller'] == 'seed' for c in r['calls']),
       'the first minutes: a limit filled on a 1-minute candle before the first 5-minute boundary after its issue, read by the seed')
    codes = {code for x in (r['runs']['signal']['rec'], r['runs']['fact']['rec']) for _c, _s, code in x['excluded_codes']}
    v_codes = {code for _rep, v, _p, _n, _t in r['views'] for _c, _s, code, _w, _d in v['excluded']} | {
        it.get('code') for _rep, v, _p, _n, _t in r['views'] for it in v['items'] if it.get('code')}
    ok({'margin', 'count', 'near', 'stop'} <= codes and {'room', 'top'} <= v_codes and r['runs']['signal']['rec']['notes']
       and r['runs']['fact']['rec']['zones'] and len([s for s in sigs.values() if not s.get('legacy')]) == 6,
       'the synthetic market meets every reason: the model\'s margin, count, near and stop; the request\'s room - a signal of the close '
       'kept without a position - and top; a note and a zone; six model signals')

    def bad(fn):
        r2 = copy.deepcopy({k: v for k, v in r.items() if k != 'fund'})
        r2['fund'] = r['fund']
        fn(r2)
        return not all(render_checks(r2, True)[0].values())

    def ev_edit(fn):
        def go(r2):
            evs = own_chain(r2['reg_text'])[0]
            fn(evs)
            r2['reg_text'] = rechain(evs)
        return go
    stop_ev = next(i for i, e in enumerate(events) if e['type'] == 'stop')
    tgt_ev = next(i for i, e in enumerate(events) if e['type'] == 'target')
    leg_ev = next(i for i, e in enumerate(events) if e['type'] == 'open' and e.get('legacy'))
    mod_ev = next(i for i, e in enumerate(events) if e['type'] == 'open' and not e.get('legacy'))
    ok(bad(ev_edit(lambda evs: evs[stop_ev].update(price=evs[stop_ev]['price'] * 1.01))), 'render_checks: a stop at another price reads FAIL')
    ok(bad(ev_edit(lambda evs: evs[stop_ev].update(R=evs[stop_ev]['R'] + 0.01))), 'render_checks: a result in R not the walk\'s reads FAIL')
    ok(bad(ev_edit(lambda evs: evs.pop(tgt_ev))), 'render_checks: a target the walk finds and the registry lacks reads FAIL')
    ok(bad(ev_edit(lambda evs: evs[leg_ev].update(entry=evs[leg_ev]['entry'] * 1.001))), 'render_checks: a legacy signal not its card\'s reads FAIL')
    ok(bad(ev_edit(lambda evs: evs[mod_ev].update(margin=evs[mod_ev]['margin'] + 1))), 'render_checks: a signal\'s margin not its arithmetic\'s reads FAIL')
    ok(bad(ev_edit(lambda evs: evs[mod_ev].update(valid=iso_of(ms_of(evs[mod_ev]['valid']) + DAY_MS)))),
       'render_checks: a validity a day late reads FAIL')
    ok(bad(lambda r2: r2.update(reg_text=r2['reg_text'].replace('"type":"fill"', '"type":"fill","x":1', 1))),
       'render_checks: a registry line edited after it was written reads FAIL')
    oid = str(min(i for i, s_ in sigs.items() if s_['end'] is None))
    ok(bad(lambda r2: r2['reg_state']['cursor'][oid].update(t=r2['reg_state']['cursor'][oid]['t'] - K5_MS)),
       'render_checks: the place of a signal open not the replay\'s reads FAIL')
    a0 = next(k for k, c in enumerate(r['allocs']) if any(it.get('pos') for it in c['items']))
    i0 = next(k for k, it in enumerate(r['allocs'][a0]['items']) if it.get('pos'))
    ok(bad(lambda r2: r2['allocs'][a0]['items'][i0]['pos'].update(leverage=r2['allocs'][a0]['items'][i0]['pos']['leverage'] + 1)),
       'render_checks: an allocation\'s leverage above the rule\'s reads FAIL')
    ok(bad(lambda r2: r2['allocs'][a0]['items'][i0]['pos'].update(want=r2['allocs'][a0]['items'][i0]['pos']['want'] * 1.1)),
       'render_checks: a wanted risk not the shares\' reads FAIL')
    ok(bad(lambda r2: r2['allocs'][a0].update(room=0.0)), 'render_checks: risk taken beyond the room reads FAIL')
    sig0 = r['texts'][RENDER_CASES[0]]
    ok(bad(lambda r2: r2['texts'].update({RENDER_CASES[0]: [(sig0[0][0].replace('Маржа <b>', 'Маржа <b>1', 1),) + sig0[0][1:]] + sig0[1:]})),
       'render_checks: a «сигнал» reply not its view\'s reads FAIL')
    ok(bad(lambda r2: r2['runs']['signal']['rec'].update(quiet=not r2['runs']['signal']['rec']['quiet'])),
       'render_checks: a check whose quiet flag disagrees with what it announced reads FAIL')
    ok(bad(lambda r2: r2['runs']['fact']['rec'].update(one_line=True)), 'render_checks: one line beside a zone left reads FAIL')
    ok(bad(lambda r2: r2['runs']['signal']['rec'].update(strong_all=r2['runs']['signal']['rec']['strong_all'][:-1])),
       'render_checks: a record whose STRONG at every rank is not the checker\'s reads FAIL')
    ok(bad(lambda r2: r2.update(records=r2['records'][:-1])), 'render_checks: a journal lacking a record reads FAIL')
    ok(bad(lambda r2: r2['expect'].update(consts=(150000.0,) + r2['expect']['consts'][1:])), 'render_checks: another capital reads FAIL')
    ok(bad(lambda r2: r2['texts'].update({RENDER_CASES[5]: [('x', False, True)]})), 'render_checks: «помощь» not HELP reads FAIL')
    rk = r['texts'][RENDER_CASES[3]]
    ok(bad(lambda r2: r2['texts'].update({RENDER_CASES[3]: [(rk[0][0].replace(' · ★', '', 1),) + rk[0][1:]] + rk[1:]})),
       'render_checks: a STRONG coin of the ranking without its ★ reads FAIL')
    ok(bad(lambda r2: r2['texts'].update({RENDER_CASES[2]: [t[:2] + (False,) for t in r2['texts'][RENDER_CASES[2]]]})),
       'render_checks: a reply without its keyboard reads FAIL')
    ok(not all(render_checks(r, False)[0].values()), 'render_checks: the bot\'s own record changed reads FAIL')
    out('SELFTEST PASS: %d of %d checks passed' % (len(done), len(done)))


def rec_j_cards():
    return [{'coin': 'XRP', 'side': 1, 'strong': True, 'mode': 'market', 'entry': 1.0, 'stop': 0.9, 'targets': [1, 2, 3], 'close': 1, 'U': 1}]


def ceil_to(ms, step):
    return -(-ms // step) * step


def main(argv):
    if not argv:
        sys.exit('usage: tz42-advisor-registry.py MODE [ARG]')
    mode, rest = argv[0], argv[1:]
    table = {'fingerprint': mode_fingerprint, 'host': mode_host, 'number': mode_number, 'rule': mode_rule, 'copy': mode_copy,
             'render': mode_render, 'first': mode_first, 'keep': mode_keep, 'stopped': mode_stopped, 'selftest': mode_selftest}
    try:
        if mode == 'mark':
            assert len(rest) == 1, 'mark deploy|kill|rollback|kill2'
            mode_mark(rest[0])
        elif mode == 'unit':
            assert len(rest) == 1, 'unit new|old'
            mode_unit(rest[0])
        else:
            assert mode in table and not rest, 'unknown mode %r' % (argv,)
            table[mode]()
    except NotYet:
        out('NOT YET')
        return 3
    except Failed:
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
```
