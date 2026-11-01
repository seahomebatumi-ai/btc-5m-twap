# TZ-39 — the advisor's two checks a day: a monitor of the trades its cards offered, a scanner of the 42, the 14 % stop, the list to seven, «Уверенность: N/5» on every card, and a journal of every check

**Canonical filename:** `TZ-39-advisor-checks.md`. The committed file takes this name and no other.

**Executor model: Claude Opus 5.5.** It replaces three files of the advisor — the bot's scheduler and its monitor, which holds trades by the rule's own functions, and the message with its ratings — and signals a long-lived unit on the capture host.

**Required System Map revision:** `2026-10-31-c`.

**Map sections this TZ rests on**, copied from §10's C8 (map §7 item 141): §0, the fingerprint gate and its table; §1, the refs; §2.5 and §2.6, the archives' calendar runs and the reward book's `STREAM_FLOOR`; §2.7, the advisor's record; §3, the forensic store, the worktrees and the directories TZ-38's session left; §6, its rows host identity, language, git remote, egress, process supervision, memory, disk, both sandbox limits and the harness; §7 items 118, 124, 125, 129, 131, 132 and 136 to 142.

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

**Before `EXECUTE TZ-39`:** the Boss uploads this file alone, into `CryptoTZ/`. `main` already carries map revision `2026-10-31-c` (`30a577e`) and PR #38's merge (`17dc258`); nothing else is needed, and no step of the Boss's is a precondition of the run (map §7 item 132). The bot's token and its pinned chat exist (map §2.7); this TZ's own commands read neither, and the bot's `--probe`, which reads the token to send `getMe`, prints neither (§2 item 3).

**When:** any time after the upload, while `/dev/vda2` holds at least `7,400,000,000` bytes free and `MemAvailable` at least `130,981,888` bytes (§0.4). **B-DEPLOY waits in its own text for 06:35:00 to 11:20:00 or 12:20:00 to 23:20:00 UTC, and B-KILL for 06:35:00 to 11:50:00 or 12:20:00 to 23:50:00 UTC**: clear of the package manager's morning runs and of both archives' calendar runs, the reward book's at 01:30:20 and the pair book's at 03:00:20 (map §2.5 and §2.6); after the old code's message of the UTC day, which the `kill` mark asserts sent; away from 12:10 UTC, so that the check the new code runs at its start (§1) and the 12:10 slot never meet; and B-DEPLOY's band ends 30 minutes before B-KILL's, so that B-KILL's is still open when COPY, G-RENDER and P-START have run, each at its bound (§6). This TZ reloads systemd **never**, so it sets off no run of either archive (map §7 items 125 and 129). About 50 minutes of wall clock (§6).

**What this TZ is.** CANON PART VII's decisions on the Boss's specification of 2026-10-31, built, each where §1 says: **two checks a day** by the unit's own scheduler, 00:10 UTC for the close's signals and 12:10 UTC for the facts of the moment, the first replacing the 06:00 UTC message; **a monitor of the trades the cards offered**, held by the rule's own functions, with an alert when a stop is touched or a signal ends at a close and a line of information when a sum of signs falls from ±4 to ±2; **a quiet line** for a check that finds nothing; **a scanner of the 42** that pushes a new STRONG candidate passing the allocation's limits at the default budget, with its entry plan; **the allocation's stop limit at 14 %** (it was 11.1 %); **«сигнал топ N» to seven**, STRONG a label of the TOP-3 still; **one line «Уверенность: N/5» on every card**, the rung of PART VII's evidence ladder, the methodology out of the pushed messages and the six ratings behind «оценка»; each card's reach shares TZ-38's, without survivorship; and **a journal record of every check's state**. **It changes no rule, no parameter of the rule and no coin:** the fourteen rule functions of `adv3.py`, `RULE-ADV-3.txt`, the unit file and the allocation's arithmetic stay what TZ-35 to TZ-37 deployed, by file and by syntax tree (G-RULE). It replaces `advisor/adv3.py`, `advisor/adv3-bot.py` and `advisor/selftest-adv3.py`, adds its checker `research/tz39-advisor-checks.py`, deploys by replacing the service copy's two files and signalling the unit once, and reads the new process's first check — run at its start, sent to the Boss's chat by the unit itself — as the deployment's proof on the host (G-FIRST).

---

## 0. Gates

### 0.0 The work tree, first

After contract §1 steps 1 and 2, and before anything else:

```
mkdir /root/tz39-work /root/tz39-work/logs; echo "exit=$?"
```

`exit=0` proves neither existed; anything else is BLOCKED. **From here every command's output goes to `/root/tz39-work/logs/`, one file per step, `NN-<step>.log` in this TZ's order** — the steps of §3.4 to §3.6 and §4.4 under the names their blocks write and the pastes read, `20-b-deploy.log` to `26-first.log` and `30-b-rollback.log` to `34-stopped.log` — and nothing to the session's scratchpad. The one exception is B-RECLAIM-OWN, §9, which removes the directory the logs are in.

Two abbreviations: **`P`** is `nice -n 19 /root/tz04a-env/venv/bin/python -B`, and **`I`** is `P /root/tz39-work/stage/research/tz39-advisor-checks.py`. **In every block that deploys, signals, restores or removes, both are written out in full**, because the Boss may be handed the block (map §6, sandbox limit).

### 0.1 The files, staged

Extract Appendix A from this TZ as the primary checkout carries it after contract §1's pull, with this script, verbatim, its one argument the destination:

```
/root/tz04a-env/venv/bin/python -B - /root/tz39-work/stage <<'EOF'
import hashlib, os, sys
SRC = "/root/btc-5m-twap/CryptoTZ/TZ-39-advisor-checks.md"
DEST = sys.argv[1]
WANT = {
    "advisor/adv3.py": "c19572dccf30a505342ca334e42c7ec347a5d29db4db20887229d2a8c7b48e31",
    "advisor/adv3-bot.py": "ca989b6fe487d41181b32312418d6acda1e9c64fbf5cfbb3f041d54826dd108f",
    "advisor/selftest-adv3.py": "09d2ba9a8361ec5ebc7f5934ebb818d1a685bb16fb3f32b7da94409d9516cc0e",
    "research/tz39-advisor-checks.py": "18294b0916d77b226083a18f9521f06e2fddb423bbc947a2e1100fd42b2980f3",
}
OLD = {  # the committed files an extraction over a worktree replaces, by hash: TZ-36's adv3.py and self-test, TZ-37's bot
    "advisor/adv3.py": "d73a657ef31decad276b858c4ec9672dce1c1c5cec36f0bb1c5b3378838224a8",
    "advisor/adv3-bot.py": "3a044d50f51b16563b99bf1514ef92f35a9795b1fcc377aea6be4c23a31f7af2",
    "advisor/selftest-adv3.py": "ef4ffc44e6f8bcdd5685fc1db9090957890c6e2ab762cdad8ae9826b18cf1395",
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
| `advisor/adv3-bot.py` | 1,558 | 99,958 | `ca989b6fe487d41181b32312418d6acda1e9c64fbf5cfbb3f041d54826dd108f` |
| `advisor/adv3.py` | 871 | 49,378 | `c19572dccf30a505342ca334e42c7ec347a5d29db4db20887229d2a8c7b48e31` |
| `advisor/selftest-adv3.py` | 235 | 16,470 | `09d2ba9a8361ec5ebc7f5934ebb818d1a685bb16fb3f32b7da94409d9516cc0e` |
| `research/tz39-advisor-checks.py` | 1,139 | 73,892 | `18294b0916d77b226083a18f9521f06e2fddb423bbc947a2e1100fd42b2980f3` |

A failed assert is BLOCKED. Over an empty `stage/` the script creates four files (`xb`); over the branch's worktree, §3.1, it overwrites the three committed advisor files, each only after asserting it is the committed one by hash, and creates the checker.

### 0.2 Fingerprint

`I fingerprint` performs contract §1 steps 3 and 4 against `SYSTEM-MAP.md` and the files of its §0 table in the primary checkout `/root/btc-5m-twap`, and asserts them: revision `2026-10-31-c`; the six anchors, `A2`, `A4`, `A5` and `A6` re-derived as the first 12 hex characters of those files' SHA-256; the table's **58** rows, each printed in lines, bytes and SHA-256 — **55** `frozen` rows asserted equal to the map, **2** `tracked` and **1** `reported`, the map's own. It prints `READING FINGERPRINT: PASS - 67 of 67` — 1 revision, 6 anchors, 4 re-derived, 55 rows, 1 shape — or fails at the first mismatch, which is BLOCKED. The advisor rows are `frozen` at TZ-36's and TZ-37's hashes and stay so until the verdict of this TZ.

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

`I host` asserts these sixteen, prints each check beside the units' readings and the memory and disk figures, and prints `READING HOST: PASS - 16 of 16`, or fails:

- **H1** — `find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit` prints one path.
- **H2** — `df` names source `/dev/vda2` and size `31612203008`; `grep -c e3975b5da44c5328adf3bf3914634cd878842c73 /var/lib/btc-recorder/runtime.jsonl` prints at least `1` — two checks. With H1 this is map §6's host identity.
- **H3** — `/root/tz04a-env/venv/bin/python` prints `3.12.`: the interpreter the bot runs under.
- **H4** — `btc-recorder.service`, `btc-pairbook.service` and `btc-rewardbook.service` each read `ActiveState=active` and `UnitFileState=enabled` — three checks: UNIT-NEW compares them, later, against the `kill` mark's snapshot.
- **H5** — `adv3-bot.service` reads `active`, `running`, `enabled`; its `MainPID` runs the unit's exact argv, alone; `/root/adv3-bot-svc` holds `adv3.py`, `adv3-bot.py` and `commit.txt` and nothing else; `adv3.py` and `adv3-bot.py` hash to TZ-36's and TZ-37's (`d73a657e…` and `3a044d50…`); the installed unit file hashes to `main`'s (`82acd8e4…`); `commit.txt` is 40 hex characters and a newline — six checks.
- **H6** — `/var/lib/adv3-bot/journal.jsonl` ends in a newline, and no `/var/lib/adv3-bot/check-done` exists: the new code's state file is not yet written.
- **Memory gate** — `MemAvailable` at least `130,981,888` bytes (§0.4); **where the first read is below it, `I host` reads again after 60 s and the second read decides** (map §7 item 137). **Disk gate** — `/dev/vda2` free at least `7,400,000,000` bytes (§0.4).

Any one failing is BLOCKED. **The rest is printed and carries no threshold:** the timers and the two archives' services; the listing of the service copy and the record; `du` of the capture roots and the Claude directory; the forensic store's count, map §3's `2,312`; the worktrees, map §3's two; and the listing of the directory that holds the session's own scratch, whose UUID directories §3.3 names live or earlier. Map §3 records the two TZ-38's session left, `716c29e7-4743-5553-ac5d-886f724de131` and `f00a192e-0435-4a82-9ad0-d54ae254a648`, and one live directory that is no TZ's, `238335b9-cf23-414a-8e8f-ad4705c4d19e`, the remote-control session of 2026-10-30 (TZ-38's report).

### 0.4 Resource floors, in exact bytes

**Disk.** `/dev/vda2` free at least **`7,400,000,000`** bytes: the reward book's `STREAM_FLOOR`, `7,300,000,000`, below which no stream of it opens (map §2.6; `research/tz33-reward-book-capture.py` line 190), plus `100,000,000` for this session at its upper bound — the worktree, about `11,500,000` bytes of tracked files, the stage and the logs under `2,000,000`, the render's scratch journal, a copy of the bot's own, under `1,000,000` today and under `10,000,000` at a year of checks, and the copies of the work tree's files under `5,000,000`. **This TZ never takes free space below the floor that pauses the reward book.** TZ-38 read `10,089,811,968` bytes free at its host gate.

**Memory.** `MemAvailable` at least **`130,981,888`** bytes: twice `65,490,944`. A floor is twice the largest peak among the modes the TZ runs (TZ-37 §0.4), and map §7 item 131 takes the larger of the Architect's measurement and the host's last measured peak of the same code. The largest mode here is `I render`, the service copy's bot answering seven commands and running both checks in one process. The Architect measured it on 2026-11-01 on Binance's archive candles of the 42 coins to the close of 2026-10-30, a stand-in for `fapi.binance.com` and a journal of 13 offers in the host's shape: under Python 3.12.3, the host's interpreter, at most `55,754,752` bytes over fifteen runs; under Python 3.13.18, `54,599,680`. This code has no host peak yet, so the nearest stands in, as at TZ-37: TZ-36's `I render` process tree, `65,490,944` (map §6, memory). TZ-37's own `I render` peaked on the host at `1.199` times the Architect's Python 3.13.18 measurement of it (map §6, memory: `58,953,728` against `49,168,384`); at that ratio this TZ's 3.13.18 figure gives `65,465,944` [modelled], below it. The larger stands. The service runs under its unit's `MemoryMax=128M`, which this TZ does not change. Every mode of this TZ runs under `nice -n 19`.

### 0.5 Refs and the number

```
git -C /root/btc-5m-twap fetch origin
git -C /root/btc-5m-twap ls-remote origin
git -C /root/btc-5m-twap ls-remote --heads origin tz-39-advisor-checks | wc -l
I number
git -C /root/btc-5m-twap log --first-parent --name-status --format='%h %cI %s' -n 5 origin/main
```

Every ref line is reported. **`wc -l` must print `0`:** the branch does not exist. **`I number`** reads `git ls-tree --name-only origin/main -- CryptoTZ/ CryptoReports/` and must print `READING NUMBER: PASS - 2 of 2`: `CryptoTZ/` holds `TZ-39-advisor-checks.md` and no other file whose name begins with `TZ-39-`, and `CryptoReports/` no report whose name does (CANON hard rule 2). Anything else is BLOCKED. A difference in the refs or the log from what map §1 records is recorded, not blocking, unless `main` does not carry revision `2026-10-31-c`.

---

## 1. Why this TZ exists

**The decisions this TZ builds** are CANON PART VII's, «Decisions on the Boss's specification of 2026-10-31 — TZ-39 builds them; TZ-38's verdict of 2026-10-31 settled the measured ones», each weighed against the frozen rule and what a history can support. What each becomes in Appendix A:

| CANON PART VII | built as |
|---|---|
| Schedule — checks at 00:10 and 12:10 UTC by the unit's own scheduler; 00:10 reads signals and replaces the 06:00 UTC message; 12:10 reads facts and no signal, and repeats 00:10 where it failed | `SLOTS`, `latest_slot`, `due`, `done_after`, `next_at` and `serve`'s loop; `check`; the file `check-done` |
| Followed trades — the trades the cards offered, the journal saying which | `offers`, `journal_scan`, `follow` |
| Invalidation — a push for a stop touched or a signal ended at a close; a fall from ±4 to ±2 with the signal kept shown as information | `alerts_of`, `forming_candles`, `event_lines`; `weakened`, `weak_lines` |
| Silent mode — one line without a notification where a check finds nothing | `compose`, `quiet_line`; `Telegram.send(…, quiet)` |
| Scanner — the 42 at every check; a new STRONG candidate passing the allocation's limits at the default budget pushed with its entry plan | `check`'s `plan` at `DEPOSIT`, `candidates`, `alerts_of`, `candidate_lines`, `item_lines` |
| Stop limit 14 % | `STOP_MAX = 14.0` |
| Top-N to 7 for the list; STRONG within the top 3 | `route`, `LIST_MAX`, `ranked`, `top_n`; the allocation still takes at most three |
| Layout and rating — no methodology in the pushed messages, «Уверенность: N/5» on every card, the allocation's sizes unproven, STRONG's history at the random lists' median, the six ratings behind «оценка» | `adv3.message`, `card_lines`, `assessment`, `trust_lines`, `PIT`, `LADDER`; `item_lines`, `plan_parts`; `route`'s `assess` |
| Internal log — every check's state | `check_record` |

**The schedule.** The rule changes state only at a daily close. **The check of 00:10 UTC** (04:10 in Batumi) reads the close of the day before — entries, exits, the STRONG candidates — ten minutes after it, the margin `Data.fresh` already keeps for the day's last funding settlement, and replaces the 06:00 UTC message: the code's `DAILY` is removed. **The check of 12:10 UTC** (16:10) reads no signal — a sum of signs on a half-formed candle is not the rule — but the candle forming since the close (`forming_candles`, the klines endpoint's row of the day), for the stops of the trades the cards offered, and the mark prices, for the entry zones and the STRONG candidates. Slots are kept in `/var/lib/adv3-bot/check-done` (`YYYY-MM-DD signal` or `YYYY-MM-DD fact`) by `put`'s one rename; `due` runs the latest slot not done, and **where the latest is a day's 12:10 and its 00:10 is not done, 12:10 runs the signal check** — CANON's «a repeat of 00:10 where it failed»; a signal check that ends at or after 12:10 marks that day's fact check done too, so no day sends two messages for one slot; a check that fails is tried again 300 s later (`RETRY`, as the daily was). The scheduler is the unit's own loop, never a cron job or a timer (CANON hard rule 14), and the unit file does not change.

**The trades the cards offered, and the stop they are held to [решение принято мной].** The bot holds no account. CANON PART VII says the Boss's «open positions» are "the trades the rule holds on coins whose card offered an entry; the journal says which were offered". **A card is an entry at its close** — `adv3.card` puts its stop at `C − k·U` of that close (line 476 of `main`'s `adv3.py`), and the Boss's stop is the card's. The rule's base position on the same coin may be older, with its stop set at its own entry; where a coin is offered again on a later day — a strong trend stays in the TOP-3 — that stop is not the one the card showed. **So a followed trade here is the trade each card offered**, keyed by coin, side and the close it was made from, **held by the rule's own functions from that close**: `adv3.open_at` at the card's close and unit, `adv3.hold` for the stop inside a day, `adv3.signal` and `adv3.close_at` for the end at a close (`follow`). Discarded: the rule's base position's stop, which for a card offered after the rule's entry day alerts at a level the Boss never set, or not at all. The offers are read from every journal record that carries cards — the daily, request, allocation and check records, since the unit's first of 2026-10-29 — each card whose entry was offered (`market` or `limit`), the first record of a key kept; an allocation record only for the coins its plan placed. **CANON PART VII's sentence is refined, not reversed, and its revision follows this TZ's verdict.**

**The alerts, the information and the quiet line.** An **alert** is sent once and is the only thing that sounds: a followed trade's stop touched — at 00:10 by a closed candle, at 12:10 by the forming one — its signal ended at a close, or a new STRONG candidate (below); each carries the price it fired at against the close it rests on, and none is sent twice (`alerted`, from the check records). **A fall of a followed trade's sum of signs from ±4 at the close before to ±2 at this close, the signal kept, is a line of information in the 00:10 message, never an exit**: in TZ-38's history 184 of 265 STRONG trades saw it, and holding them to the rule's exit made `+0.998` R a trade more than leaving there, the median `−0.238` R, holding better in `38.6 %` (CryptoReports/TZ-38-adv3-pit-validation-report.md, E7). **Every check sends one text — in parts where it is longer than Telegram takes — without a notification unless it holds an alert** (the Bot API's `disable_notification`). **A check that finds nothing sends one line:** the 12:10 check where no alert and no entry zone left; the 00:10 check where no alert, no weakening, no change of signal among the 42, and the TOP-3 with its sides and STRONG as at the check before. Otherwise the 00:10 check sends the close's message in full — the alerts first, the day's changes, the TOP-3 cards, the STRONG candidates, the trades the cards offered, the weakened ones — quiet without an alert; and the 12:10 check its alerts, each new candidate's entry plan and the entries whose zone the price has left, with the limit or the «не входить» the card would now show.

**The scanner.** Every check scans the 42 and runs the allocation of TZ-37 at the default budget, `10,000` USDT and `0.5 %` (`plan`, unchanged); **a STRONG coin it places that it did not place at the check before is an alert, pushed with its entry plan** — at 00:10 its TOP-3 card and its line among the STRONG candidates, at 12:10 the plan in full (`item_lines`) — and a STRONG coin it does not place is named with its reason. The wider market waits for the market record (CANON PART VII); this TZ scans the 42 alone.

**The 14 % stop and the list to seven.** `STOP_MAX` is `14.0`, the Boss's limit. The loss at the stop is the risk, 1 % a trade and 5 % in all, so a wider stop shrinks the position and the leverage: at 14 % the rule's `⌊1 ÷ (1.5 × 0.14 + 0.01)⌋` is `4`×, and a trade at `0.5 %` of `10,000` is `⌊50 ÷ 0.142⌋ = 352` USDT, margin `88`, loss at the stop `50` — the bot's fifth golden case. In TZ-38's history, of STRONG's 265 trades 28 had their stop within 11.1 % of the entry close, 25 between 11.1 and 14 % at `+0.36` R a trade and 212 beyond 14 % at `+0.48` (E6): the limit passes about one STRONG trade in five, against one in ten, and is a choice of risk, not of edge. **«сигнал топ N» shows the rule's first N coins, N from 1 to 7** (`LIST_MAX`): `ranked` applies `adv3.ranking` again to the coins it has not yet placed — no second order is written — and `top_n` gives the TOP-3 their own cards and the rest `adv3.card`'s, ★ STRONG only among the first three. The allocation takes N up to 7 and places at most three: STRONG of five or seven places made `+0.55` and `+0.51` R a trade against `+0.80` in TZ-38's history (E6).

**The card, the confidence and «оценка».** Every card ends with one line, «Уверенность: <b>N/5</b> — …», N the rung of PART VII's evidence ladder, `adv3.RELIABILITY`, `1` — «правило не доказано» — or `0` where the card offers no entry or no current price came (`adv3.trust`, unchanged). Each card's targets carry the shares of past trades of its class that reached them, **TZ-38's without survivorship**: STRONG's `47 / 29 / 19 %` in place of its `48 / 28 / 18 %` on the 42, and the rule's `23 / 13 / 8 %`, the same as on the 42 at whole percents (E4; `adv3.PIT`, which G-RULE reads against TZ-38's committed report cell for cell). **The pushed messages carry no methodology**: the history block, the forward book, the rule's open STRONG positions and the six ratings leave them for **«оценка»**, a new command — the rung and the next readings, the six ratings, the forward record in its parts and the history in figures without survivorship: the rule `+0.04` R a trade on the 570 contracts the Boss did not pick (E1) and STRONG's median `+0.22` R on 500 random lists of 42 (E5), **never STRONG's `+0.547` on the 42**. The allocation is one text now, each trade's confidence line adding that its sizes are the Architect's formula, unproven.

**The journal.** Each check writes one record of kind `check`: its slot, every coin's signal, sum of signs, strength, rank, unit, close and mark; the followed trades it read and their state; its alerts with the price each fired at against the close it rests on; the weakened trades; the STRONG coins it placed and the allocation's figures; the zones left; the six ratings; and the cards its message offered. It measures and tunes nothing: a parameter changes only as a new frozen rule (CANON PART VII). The journal is read in one pass that keeps only the offers, the alerts and the last check (`journal_scan`), so a year of records is never held whole. The request and allocation records keep TZ-35's and TZ-37's fields, each card adding its `since`, `rank`, `of` and `confidence`, a request its `n`, and an allocation's cards now the trades it placed; «оценка» writes a record of kind `assess`, with no cards and the six ratings.

**The first check after the restart.** The new process finds no `check-done` and runs the day's signal check at once — the 06:00 UTC message of the day is the old code's, and B-KILL waits for it — so **the Boss receives the new format within about a minute of the restart**, a second message of the same close that day. It reads every offer the journal holds since 2026-10-29: stops touched and signals ended since, and every STRONG candidate it places — no check came before it — are its alerts, so it is likely to sound. **G-FIRST reads that check from its record and its log** (§4.3); nothing in this TZ sends or fakes a message to the Boss's chat.

**What this TZ does not do.** No new rule, no parameter, no coin, no scan beyond the 42, no exit on a weakening, no signal on a half-formed candle, no new unit and no reload of systemd. It does not touch Telegram's command menu, a bound on `service.log` or a census of the host's memory and disk, which stay where TZ-37 left them.

---

## 2. Scope

**Paths this TZ writes.** On the branch `tz-39-advisor-checks`: `advisor/adv3.py`, `advisor/adv3-bot.py` and `advisor/selftest-adv3.py`, modified, and `research/tz39-advisor-checks.py`, new. On the host: `/root/tz39-work/**`; `/root/adv3-bot-svc/adv3.py`, `/root/adv3-bot-svc/adv3-bot.py` and `/root/adv3-bot-svc/commit.txt`; `/root/btc-forensics/tz39-work--*`. On `main`: the report, `CryptoReports/TZ-39-advisor-checks-report.md`. **The unit itself, once restarted, writes `/var/lib/adv3-bot/check-done` and its own records** — its own writes, not this TZ's.

**Prohibited**, by path and by content class:

1. Any change to a repository file but the four above and the report — `advisor/RULE-ADV-3.txt`, `deploy/systemd/adv3-bot.service`, `SYSTEM-MAP.md` and `BTC-EXECUTOR-INSTRUCTIONS.md` among them.
2. Any change to a definition or a constant of `adv3.py` or `adv3-bot.py` but those §4.1 names: G-RULE reads both.
3. Any read, copy, print or hash of anything under `/etc/adv3-bot/`, and any request to Telegram or to Binance by this TZ's own commands, but two: G-RENDER runs the service copy's bot, whose `Data`, `live_report`, `liquidity` and `forming_candles` read Binance's public futures market, and P-START runs the bot's own `--probe`, whose function reads the token to send `getMe` and prints the bot's username and neither the token nor a chat id. The unit makes its own requests.
4. Any `systemctl` verb but `show`, `list-timers`, `is-enabled`, `kill --signal=SIGTERM adv3-bot.service` (B-KILL, B-KILL2) and, on a FAIL of UNIT-OLD, `disable --now adv3-bot.service` (K-39). No `daemon-reload`, `enable`, `restart`, `start`, `stop` or `mask`.
5. Any change to a capture unit, its store, either archive's timer or ledger: `systemctl show` and `list-timers`, `du`, and under the recorder's root `find`, `grep -c` and `df` read them.
6. A dataset or a binary in git history.
7. A coin, a price, a size or a card from the live replies, from the render's scratch journal or from the bot's own journal printed in the report or the logs: G-RENDER, G-FIRST and the marks print counts and labels alone, and no file of the work tree is printed, whole or in part, but by a command this TZ names (map §7 item 118). The day's cards are the Boss's to read in his chat.
8. The report on `main` before the branch is pushed and its pull request opened (contract §4.1).

**Exemptions.** The requests of item 3, each by the service copy's own code, as TZ-37's P-START and G-RENDER made theirs; the scratch journal of item 7, `render-state/journal.jsonl`, a copy of the bot's own taken by `I render` and removed with the tree, never printed and never kept.

---

## 3. The work, in this order

### 3.1 The branch and its files

```
git -C /root/btc-5m-twap fetch origin
I number
git -C /root/btc-5m-twap worktree add -b tz-39-advisor-checks /root/tz39-work/wt origin/main
```

`I number` must print `READING NUMBER: PASS - 2 of 2` again, or BLOCKED. Then §0.1's script again, verbatim but for its argument, `/root/tz39-work/wt`; it must print the same lines, bytes and SHA-256 as at §0.1. Then:

```
git -C /root/tz39-work/wt add advisor/adv3.py advisor/adv3-bot.py advisor/selftest-adv3.py research/tz39-advisor-checks.py
git -C /root/tz39-work/wt diff --cached --name-status
git -C /root/tz39-work/wt diff --cached --numstat
```

`--name-status` must print exactly four lines — `M` for the three advisor files, `A` for the checker — and `--numstat` exactly `1005	245	advisor/adv3-bot.py`, `118	64	advisor/adv3.py`, `42	8	advisor/selftest-adv3.py` and `1139	0	research/tz39-advisor-checks.py`, or BLOCKED. Commit them alone; `git ls-remote origin` (§0.5); push with `git push -u origin tz-39-advisor-checks` — through `credential.helper=!gh auth git-credential` where the URL's credential is refused (map §6, git remote) — and open the pull request against `main`. A failed assert here is BLOCKED.

### 3.2 The self-tests and G-RULE

```
P /root/tz39-work/wt/advisor/selftest-adv3.py
P /root/tz39-work/wt/advisor/adv3-bot.py --selftest
I selftest
I rule
```

They must print `SELFTEST-ADV3 PASS: 53 of 53 checks passed`, `SELFTEST PASS: 106 of 106 checks passed`, `SELFTEST PASS: 64 of 64 checks passed` and `READING RULE: PASS - 10 of 10`. The first three reach no network — `I selftest` runs the stage's own bot on a synthetic market with Binance stood in for (§5); `I rule` reads `git show origin/main:` of `adv3.py`, `adv3-bot.py`, `RULE-ADV-3.txt`, the unit file and TZ-38's report, and the branch's files. A red check stops the run here, and it goes to §3.7 and §9.

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

One `reclaim` names every earlier directory and must print `RECLAIM PASS` before any removal; then one `rm -rf` and one `test -e` a directory, the last reading `exit=1`. TZ-35's checker is `main`'s, frozen by the map's table, and its `reclaim` refuses a directory born with a running claude process and any path that is not a UUID directory under `/tmp/` whose parent's name carries `btc-5m-twap`. Map §3 expects TZ-38's two directories (§0.3) unless a reboot emptied `/tmp`; the live session of 2026-10-30 is not touched. If `scratch` names none earlier, the block is recorded as empty and skipped. **Where the classifier refuses it, the Boss runs it as one line** (map §6, sandbox limit; §7 items 124 and 138), the Executor writing in every earlier directory's full path, one `rm -rf` and one `test -e` a directory, all chained to the `reclaim`'s `exit=0`, which it reaches only after `RECLAIM PASS`:

```
{ date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/btc-5m-twap/research/tz35-advisor-deploy.py reclaim <D1> <D2>; echo "exit=$?"; } >> /root/tz39-work/logs/12-reclaim-scratch.log 2>&1 && tail -n 1 /root/tz39-work/logs/12-reclaim-scratch.log | grep -qx 'exit=0' && { date -u +%FT%T.%NZ; rm -rf <D1>; echo "exit=$?"; test -e <D1>; echo "exit=$?"; rm -rf <D2>; echo "exit=$?"; test -e <D2>; echo "exit=$?"; } >> /root/tz39-work/logs/12-reclaim-scratch.log 2>&1
```

**It holds back nothing of §3.4 to §3.6**, which read none of what it removes (map §7 item 140).

### 3.4 B-DEPLOY, then COPY and G-RENDER

All of §3.1 and §3.2 PASS first. Then **B-DEPLOY**, which waits for its band and records its mark inside the block:

```
until s=$(( $(date +%s) % 86400 )); { [ $s -ge 23700 ] && [ $s -le 40800 ]; } || { [ $s -ge 44400 ] && [ $s -le 84000 ]; }; do sleep 5; done; { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz39-work/stage/research/tz39-advisor-checks.py mark deploy && cp -p /root/adv3-bot-svc/adv3.py /root/tz39-work/adv3.before && cp -p /root/adv3-bot-svc/adv3-bot.py /root/tz39-work/bot.before && cp -p /root/adv3-bot-svc/commit.txt /root/tz39-work/commit.before && git -C /root/tz39-work/wt show origin/tz-39-advisor-checks:advisor/adv3.py > /root/adv3-bot-svc/adv3.py.new && git -C /root/tz39-work/wt show origin/tz-39-advisor-checks:advisor/adv3-bot.py > /root/adv3-bot-svc/adv3-bot.py.new && mv /root/adv3-bot-svc/adv3.py.new /root/adv3-bot-svc/adv3.py && mv /root/adv3-bot-svc/adv3-bot.py.new /root/adv3-bot-svc/adv3-bot.py && git -C /root/tz39-work/wt rev-parse origin/tz-39-advisor-checks > /root/adv3-bot-svc/commit.txt; echo "exit=$?"; } >> /root/tz39-work/logs/20-b-deploy.log 2>&1
```

06:35:00 to 11:20:00 and 12:20:00 to 23:20:00 UTC are seconds `23,700` to `40,800` and `44,400` to `84,000` of the day. `exit=0`, or B-ROLLBACK (§4.4). The running process keeps the old code in memory until it is signalled. Then:

```
I copy >> /root/tz39-work/logs/21-copy.log 2>&1; echo "exit=$?" >> /root/tz39-work/logs/21-copy.log
timeout 900 I render >> /root/tz39-work/logs/22-render.log 2>&1; echo "exit=$?" >> /root/tz39-work/logs/22-render.log
```

`I copy` must print `READING COPY: PASS - 5 of 5`; `I render` imports the service copy's bot, points its `STATE` at `/root/tz39-work/render-state/` holding a copy of the bot's own `journal.jsonl`, replaces Telegram by a stand-in, answers seven commands and runs both checks on `fapi.binance.com`'s live data, and must print `READING RENDER: PASS - 22 of 22`. A FAIL of either, or a `timeout`, is B-ROLLBACK (§4.4), and nothing is signalled.

### 3.5 P-START, B-KILL, then UNIT-NEW and G-FIRST

Only after COPY and G-RENDER PASS. **P-START**, CANON hard rule 14's proof of the request path, through the service copy's own functions:

```
P /root/adv3-bot-svc/adv3-bot.py --probe >> /root/tz39-work/logs/23-probe.log 2>&1; echo "exit=$?" >> /root/tz39-work/logs/23-probe.log
```

It must print `READING P-START: served - 5 of 5 endpoints` (§4.3). A FAIL is B-ROLLBACK (§4.4), and nothing is signalled. Then **B-KILL**, its mark inside the block:

```
until s=$(( $(date +%s) % 86400 )); { [ $s -ge 23700 ] && [ $s -le 42600 ]; } || { [ $s -ge 44400 ] && [ $s -le 85800 ]; }; do sleep 5; done; { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz39-work/stage/research/tz39-advisor-checks.py mark kill && systemctl kill --signal=SIGTERM adv3-bot.service; echo "exit=$?"; } >> /root/tz39-work/logs/24-b-kill.log 2>&1
```

06:35:00 to 11:50:00 and 12:20:00 to 23:50:00 UTC are seconds `23,700` to `42,600` and `44,400` to `85,800`. `I mark kill` fails — and nothing is signalled — where `daily-sent` is not today's UTC date: the old code's message of the day is then not sent, and the run goes to B-ROLLBACK (§4.4) with the unit not signalled. At least 45 s later, then every 15 s while it prints `NOT YET` and exits `3`, and for at most 100 s after the mark: `I unit new` — **UNIT-NEW**, `READING UNIT-NEW: PASS - 9 of 9`. Then every 15 s while it prints `NOT YET` and exits `3`, for at most 900 s after the mark: `I first` — **G-FIRST**, `READING FIRST: PASS - 7 of 7`. Each run's output is appended to `25-unit-new.log` and `26-first.log`. A FAIL of either is B-ROLLBACK (§4.4).

### 3.6 The Boss's one paste — CANON hard rule 14

**The Executor tries each block once; a refused one is handed to the Boss unchanged, with the paste below** (map §7 item 138). Each step's output goes to the log the Executor's own step names, under a `date -u` line and appended, each step gated on the one before it by that log's last line, and the bands wait in the text (map §7 item 124). **P-BOSS-A** is handed over where B-DEPLOY is refused, and only while B-DEPLOY's band is open — 06:35:00 to 11:20:00 or 12:20:00 to 23:20:00 UTC — so that B-KILL's band is open too when the paste reaches it and its waits are seconds; the Executor waits for that band before handing it over. It runs B-DEPLOY, COPY, G-RENDER, P-START, B-KILL, UNIT-NEW and G-FIRST:

```
until s=$(( $(date +%s) % 86400 )); { [ $s -ge 23700 ] && [ $s -le 40800 ]; } || { [ $s -ge 44400 ] && [ $s -le 84000 ]; }; do sleep 5; done; { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz39-work/stage/research/tz39-advisor-checks.py mark deploy && cp -p /root/adv3-bot-svc/adv3.py /root/tz39-work/adv3.before && cp -p /root/adv3-bot-svc/adv3-bot.py /root/tz39-work/bot.before && cp -p /root/adv3-bot-svc/commit.txt /root/tz39-work/commit.before && git -C /root/tz39-work/wt show origin/tz-39-advisor-checks:advisor/adv3.py > /root/adv3-bot-svc/adv3.py.new && git -C /root/tz39-work/wt show origin/tz-39-advisor-checks:advisor/adv3-bot.py > /root/adv3-bot-svc/adv3-bot.py.new && mv /root/adv3-bot-svc/adv3.py.new /root/adv3-bot-svc/adv3.py && mv /root/adv3-bot-svc/adv3-bot.py.new /root/adv3-bot-svc/adv3-bot.py && git -C /root/tz39-work/wt rev-parse origin/tz-39-advisor-checks > /root/adv3-bot-svc/commit.txt; echo "exit=$?"; } >> /root/tz39-work/logs/20-b-deploy.log 2>&1; tail -n 1 /root/tz39-work/logs/20-b-deploy.log | grep -qx 'exit=0' && { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz39-work/stage/research/tz39-advisor-checks.py copy; echo "exit=$?"; } >> /root/tz39-work/logs/21-copy.log 2>&1 && tail -n 1 /root/tz39-work/logs/21-copy.log | grep -qx 'exit=0' && { date -u +%FT%T.%NZ; timeout 900 nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz39-work/stage/research/tz39-advisor-checks.py render; echo "exit=$?"; } >> /root/tz39-work/logs/22-render.log 2>&1 && tail -n 1 /root/tz39-work/logs/22-render.log | grep -qx 'exit=0' && { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/adv3-bot-svc/adv3-bot.py --probe; echo "exit=$?"; } >> /root/tz39-work/logs/23-probe.log 2>&1 && tail -n 1 /root/tz39-work/logs/23-probe.log | grep -qx 'exit=0' && { until s=$(( $(date +%s) % 86400 )); { [ $s -ge 23700 ] && [ $s -le 42600 ]; } || { [ $s -ge 44400 ] && [ $s -le 85800 ]; }; do sleep 5; done; } && { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz39-work/stage/research/tz39-advisor-checks.py mark kill && systemctl kill --signal=SIGTERM adv3-bot.service; echo "exit=$?"; } >> /root/tz39-work/logs/24-b-kill.log 2>&1 && tail -n 1 /root/tz39-work/logs/24-b-kill.log | grep -qx 'exit=0' && sleep 45 && for k in 1 2 3 4; do { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz39-work/stage/research/tz39-advisor-checks.py unit new; echo "exit=$?"; } >> /root/tz39-work/logs/25-unit-new.log 2>&1; tail -n 1 /root/tz39-work/logs/25-unit-new.log | grep -qx 'exit=3' || break; sleep 15; done; tail -n 1 /root/tz39-work/logs/25-unit-new.log 2>/dev/null | grep -qx 'exit=0' && for k in $(seq 1 60); do { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz39-work/stage/research/tz39-advisor-checks.py first; echo "exit=$?"; } >> /root/tz39-work/logs/26-first.log 2>&1; tail -n 1 /root/tz39-work/logs/26-first.log | grep -qx 'exit=3' || break; sleep 15; done; echo "P-BOSS-A ended"
```

**P-BOSS-B** is handed over where the Executor's B-DEPLOY, COPY, G-RENDER and P-START passed and B-KILL alone is refused, while B-KILL's band is open; it runs B-KILL, UNIT-NEW and G-FIRST:

```
tail -n 1 /root/tz39-work/logs/23-probe.log | grep -qx 'exit=0' && { until s=$(( $(date +%s) % 86400 )); { [ $s -ge 23700 ] && [ $s -le 42600 ]; } || { [ $s -ge 44400 ] && [ $s -le 85800 ]; }; do sleep 5; done; } && { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz39-work/stage/research/tz39-advisor-checks.py mark kill && systemctl kill --signal=SIGTERM adv3-bot.service; echo "exit=$?"; } >> /root/tz39-work/logs/24-b-kill.log 2>&1 && tail -n 1 /root/tz39-work/logs/24-b-kill.log | grep -qx 'exit=0' && sleep 45 && for k in 1 2 3 4; do { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz39-work/stage/research/tz39-advisor-checks.py unit new; echo "exit=$?"; } >> /root/tz39-work/logs/25-unit-new.log 2>&1; tail -n 1 /root/tz39-work/logs/25-unit-new.log | grep -qx 'exit=3' || break; sleep 15; done; tail -n 1 /root/tz39-work/logs/25-unit-new.log 2>/dev/null | grep -qx 'exit=0' && for k in $(seq 1 60); do { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz39-work/stage/research/tz39-advisor-checks.py first; echo "exit=$?"; } >> /root/tz39-work/logs/26-first.log 2>&1; tail -n 1 /root/tz39-work/logs/26-first.log | grep -qx 'exit=3' || break; sleep 15; done; echo "P-BOSS-B ended"
```

While a paste runs, the Executor runs nothing that reads the service copy or the unit; once it ends, the Executor reads every log it wrote and runs `I copy`, `I unit new` and `I first` again itself, each a read. Every outcome is verified from the logs, `sha256sum`, `systemctl show` and the checker's own modes, never from the Boss's account. A FAIL inside a paste is B-ROLLBACK (§4.4), the Executor's, handed over unchanged if refused.

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
du -sb /root/tz39-work /root/adv3-bot-svc /var/lib/adv3-bot /var/lib/btc-rewardbook /var/lib/btc-pairbook /root/.claude
cat /root/tz39-work/state.json
```

The journal holds systemd's own lines for the unit; `service.log` the service's own — a start, a refresh, a check sent or failed, a request answered — with no token, no chat id and no price, and a coin only where Binance failed to serve it. The 00:10 UTC check of the next day, or the 12:10 UTC check of the same day where the restart came before 11:50, is the first scheduled check the running unit sends after G-FIRST's; nothing in this TZ waits for it.

---

## 4. The gates — fixed here, before any of their data exists

| gate | population | PASS | false failure | power, against |
|---|---|---|---|---|
| **G-RULE** | `origin/main`'s `adv3.py`, `adv3-bot.py`, `RULE-ADV-3.txt` and the unit file, TZ-38's report, and the branch's files | 10 of 10 (§4.1) | `0` — the files, their syntax trees and the report's cells read directly | `1`, a rule function, a constant, the unit or the rule text changed, a definition changed beyond Appendix A, or a quoted figure not TZ-38's |
| **SELFTESTS** | the three self-tests | 53 of 53, 106 of 106 and 64 of 64 | `0` | `1`, a changed expectation or a red check |
| **COPY** | the service copy | 5 of 5 (§4.3) | `0` | `1`, a file not Appendix A's or not the branch head's |
| **G-RENDER** | the service copy's bot answering seven commands and running both checks on live data, on a copy of its own journal | 22 of 22 (§4.3) | `0` — the replies, records and alerts read against plans and walks the checker makes itself from the same reports, candles and offers, and against fixed labels and limits | `1`, a command that does not answer, methodology in a pushed message, a card without its confidence, a stop beyond 14 %, a loss beyond 1 % or 5 %, STRONG beyond the TOP-3, an exit not alerted or alerted twice, a loud check without an alert |
| **P-START** | five endpoints, six requests, through the service copy's own functions | `READING P-START: served - 5 of 5 endpoints` | `0` — each read directly | `1`, a refused request — `451`, `403` — or a reply of another shape |
| **UNIT-NEW** | the unit after the signal | 9 of 9 (§4.3) | `0` | `1`, a process not new, not the new code's, a daily record written, a capture unit moved |
| **G-FIRST** | the new process's first check: its record, `check-done` and its log | 7 of 7 (§4.3) | `0` | `1`, no check at the start, another slot or close, no message sent, a loud check without an alert, a failure in the log |

**Family-wise false failure `0`:** every gate reads its quantity directly and none samples. A FAIL before B-DEPLOY is BLOCKED and deploys nothing; a FAIL of COPY, G-RENDER, P-START, B-KILL's mark, UNIT-NEW or G-FIRST is B-ROLLBACK (§4.4).

### 4.1 G-RULE

`I rule` asserts ten. **Two files** are `main`'s, byte for byte: `advisor/RULE-ADV-3.txt` (`ee206e7c…`, and the `RULE` constant of the branch's `adv3.py`) and `deploy/systemd/adv3-bot.service` (`82acd8e4…`). **Three of `adv3.py`**, by `ast.dump` against `main`'s: the definitions that changed are exactly `card_lines`, `message` and `trust_lines`, those added exactly `assessment` and `changes`, none removed; **the 44 others are identical, the fourteen rule functions among them** — `signs`, `signal`, `strength`, `true_range`, `unit`, `open_at`, `hold`, `close_at`, `simulate`, `states`, `ranking`, `simulate_strong`, `stats`, `funding_of` — with `report`, `card`, `trust`, `history`, `facts_checks` and every fetcher; of the assignments none changed, `PIT` and `LADDER` added, none removed. **One of `PIT`:** it equals the figures of `CryptoReports/TZ-38-adv3-pit-validation-report.md` as committed (`f4a0ac3f…`), read from its §2.7 cell for cell — E4's reach shares and STRONG's top-5 share, E1's rule on *G*, E2's `p`, E5's median and its share of lists in profit, and the size of *G*. **Three of `adv3-bot.py`**: the definitions that changed are exactly `Telegram`, `handle`, `hello`, `make`, `plan_parts`, `probe`, `route`, `selftest` and `serve`, those added exactly the thirty-five functions §5 names, and the one removed is `journal`; **the 13 others are identical** — `Data`, `chunks`, `correlation`, `find_chat`, `liquidity`, `log`, `main`, `malloc_tune`, `numbers`, `plan`, `put`, `read` and `returns_of` — **so the allocation's arithmetic, the candles' fetch and the modes are TZ-37's**; of the assignments `(STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, CROWD, Z_CAP, LIQ_DAYS)` and `HELP` changed, `(SIDE, DOT)`, `ASSESS`, `BATUMI`, `CARD_KEYS`, `FOOTER`, `LIST_MAX` and `SLOTS` were added and `DAILY` removed. **One more:** the branch's three advisor files hash to Appendix A's.

### 4.2 The checks and the commands — what Appendix A answers

**The two checks.** At 00:10 and 12:10 UTC, by `serve`'s loop, each once (`due`, `done_after`, `check-done`), each tried again 300 s after a failure; 12:10 runs the signal check where the day's 00:10 failed. Each reads the report at the default deposit and risk (`live_report`, `top_n`), the offers and the alerts already sent (`journal_scan`), the followed trades (`follow`), at 12:10 the candle forming since the close of every followed coin (`forming_candles`), and the allocation at `10,000` USDT and `0.5 %` (`plan`); then its alerts (`alerts_of`), at 00:10 the weakened trades (`weakened`) and at 12:10 the zones left (`zones_left`); then its message (`compose`), sent by `Telegram.send` with `disable_notification` unless it holds an alert; then its record (`check_record`), appended once the message is sent.

| check | finds | sends |
|---|---|---|
| 00:10 | nothing: no alert, no weakening, no change of signal among the 42, the TOP-3 with its sides and STRONG as at the check before | one line, quiet: «✓ 04:10 по Батуми · закрытие …: без изменений — ТОП-3 тот же (…) …» |
| 00:10 | anything else | the close's message, loud only with an alert: «🔔 События» first where there are alerts, the day's changes, the TOP-3 cards, «STRONG-кандидаты» with each candidate's capital, leverage, margin and loss at the default budget or its reason, «Сделки по карточкам бота», «ℹ️ Ослабление» where a trade weakened, the other signals |
| 12:10 | neither an alert nor an entry zone left | one line, quiet: «✓ 16:10 по Батуми · закрытие …: событий нет — …» |
| 12:10 | an alert or a zone left | its events — a stop touched today with the day's extreme, a new candidate with its entry plan — and the zones left with what the card would now show; loud only with an alert |

**The commands.** `route` reads «сигнал», «сигналы», «топ», «стратегия», `signal`, `top`, `strategy` and the rest of TZ-37's words, with «топ N» or `top N` read first, N from 1 to 7: no number of 100 or more is **the TOP-N message** of the rule's first N coins, default 3, at `10,000` USDT and the risk given; a number of 100 or more is **the allocation** of TZ-37 at that budget, N up to 7, STRONG at most three, now in one text; «оценка», «оценки», «оценку», `rating` is **the assessment**; any other text is `HELP`. While Binance or Telegram does not answer, the apology of TZ-35, and no record.

**The allocation** is TZ-37's to the letter (`plan` identical by its syntax tree) with `STOP_MAX` at `14.0`: STRONG coins of the report only, in rank order, at most N and at most three; a stop beyond 14 % of the entry, an entry near the stop or no current price rejected and named; the loss at each stop at most `1 %` of the budget, all together at most `5 %`; the position that loss over the stop's distance and both sides' costs, at most `0.1 %` of the coin's mean daily quote volume and at least `5` USDT; leverage the rule's, at most 20. **Its reply** holds TZ-37's fields, each trade ending «Уверенность: <b>1/5</b> — правило не доказано · размеры — формула Архитектора, не доказана», and no six ratings.

**The card.** TZ-36's lines; the targets' shares from `adv3.PIT` by class — STRONG's where Gate S stands; the basis «ранг k из N»; and the last line «Уверенность: <b>N/5</b> — …»: `RELIABILITY` where the card offers an entry and a current price came, else `0` with «входа нет» or «нет текущей цены Binance».

**The assessment** («оценка»): the rung and the next readings — the forward record after the close of 2027-10-28 and the PIT record after the close of 2027-10-31, the chance that they lift the rating at most about one in seven [modelled, CANON PART VII] — the six ratings (`trust_lines`, its figures TZ-38's), the forward record in its parts with the rule's open STRONG positions, the history without survivorship and the footnote on «дошли» and R.

**The journal's record of a check:** `utc`, `kind` `check`, `slot`, `rule`, `close_of`, `deposit`, `risk_pct`, `top`, `strong`, `message_ids`, `quiet`, `one_line`, `signals`, `state` — for each of the 42 its `signal`, `sum`, `z`, `rank`, `U`, `close`, `mark` — `followed` — each followed trade read, its `coin`, `side`, `close_of`, `close`, `U`, `stop`, `state`, `day`, `price`, `R` — `alerts` — each with its `kind`, `coin`, `side`, `close_of`, `close`, `level`, `price`, `day`, `touch` and `mark` — `weakened`, `passing`, `zones_left`, `alloc`, `trust` and `cards`.

### 4.3 COPY, G-RENDER, P-START, UNIT-NEW and G-FIRST

**COPY** (`I copy`), five: the service copy holds `adv3.py`, `adv3-bot.py` and `commit.txt` and nothing else; `adv3.py` and `adv3-bot.py` hash to Appendix A's, two checks; `commit.txt` is 40 hex characters and a newline equal to the worktree's `HEAD` and to `origin/tz-39-advisor-checks`; the branch's two files equal the service copy's byte for byte.

**G-RENDER** (`I render`), twenty-two, on the service copy's bot, its `Data`, `live_report`, `liquidity` and `forming_candles` reading `fapi.binance.com` — the last three wrapped so that the checker keeps what they returned — Telegram a stand-in that records each message and its notification flag, and `STATE` at `/root/tz39-work/render-state/`, a copy of the bot's own journal. The seven commands are «сигнал», «сигнал топ 7», «сигнал 10000 топ 3», «сигнал 15000 топ 5», «оценка», «помощь» and «привет», then the signal check and the fact check of the run's UTC day, each appended to the scratch journal. (1) every command and both checks answered, no traceback and no failure in the bot's log; (2) every message's markup balances; (3) «сигнал»: at most three cards, each with its basis, its invalidation and one confidence line reading the rung `1` or `0`, and none of the methodology's labels; (4) «сигнал топ 7»: at most seven cards ranked of 7, each with its confidence, ★ STRONG only among the first three; (5) «оценка»: the rung and both next readings, the six ratings, the forward record, `+0,22 R` and `+0,04 R`, and no `0,55`; (6) the bot's constants are this TZ's — `STOP_MAX` `14.0`, `MIN_NOTIONAL` `5`, `LIQ_FRAC` `0.001`, `RISK_MAX` `1`, `RISK_ALL` `5`, `TOP_N` `3`, `COST` `0.001`, `LIST_MAX` `7`, `SLOTS` 00:10 and 12:10 UTC, `RELIABILITY` `1`; (7) each allocation reply is the bot's own `plan_parts` of the plan the checker recomputes from the very report and volumes it was made from; (8) to (13) TZ-37's six limits of each plan, at 14 %; (14) the Boss's fields in each allocation reply, each trade's confidence with the note that its sizes are unproven, and no six ratings; (15) «сигнал 15000 топ 5» says that STRONG is at most three; (16) «помощь» and «привет» answer `HELP` and nothing else; (17) the signal check is quiet exactly when it holds no alert, every part sent with that flag, one line exactly where it finds nothing, else the close's TOP-3 cards, its candidates and its followed trades with no methodology, its events heading it exactly when it has alerts and its weakening line exactly when it has one; (18) the fact check is quiet exactly when it holds no alert, one line exactly where it finds neither an alert nor a zone left, and offers no card but a new candidate's; (19) **every alert of both checks is the first exit of an offered trade by the checker's own walk** — a candle reaching the stop, else a close whose sum of signs, counted by the checker over the closes at least 14, 28, 56 and 112 days before, leaves the side — or the forming candle through its stop, **every such exit not alerted before is alerted, none twice across the checks**, and the candidates are exactly the STRONG coins the plan places that the check before did not; (20) both records carry their slot, the 42 coins' state with the TOP-3 ranked, the six ratings and the placed coins; (21) the scratch journal holds, after the bot's own records, `request`, `request`, `alloc`, `alloc`, `assess`, `check`, `check`; (22) the bot's own `journal.jsonl`, `offset` and `daily-sent` hash as before the run, and no `check-done` was written. **Only counts and labels are printed:** each reply's size in characters and parts, the number of STRONG coins, the trades placed per allocation, and for each check its flags, its parts, its alerts by kind, the offers read, the followed trades, the coins placed, the zones left and the forming candles read. **A day with no exit and no candidate reads 22 of 22 with zero alerts**, and then proves the routing, the shapes and the record on live data and the alert logic on the self-tests' synthetic market alone; the report prints the counts.

**P-START** is `adv3-bot.py --probe`, every reply asserted served and parsed: **P-KLINES** — `/fapi/v1/klines?symbol=BTCUSDT&interval=1d&limit=1500` serves closed daily candles, the last at most two days old, each of four prices with its close positive, and `/fapi/v1/klines?symbol=BTCUSDT&interval=1d&limit=2` the candle forming since 00:00 UTC, its high at or above its open and last and its low positive and at or below them; **P-FUNDING** — `/fapi/v1/fundingRate?symbol=BTCUSDT&startTime=<2026-10-27 00:00 UTC>&limit=1000` serves settlements, each a number; **P-MARKS** — `/fapi/v1/premiumIndex` serves a positive mark price for every one of the 42 coins' perpetuals; **P-INTERVALS** — `/fapi/v1/fundingInfo` serves the adjusted funding intervals, each a positive number of hours; **P-TELEGRAM** — `getMe` answers `is_bot` true and a username, which it prints. Six requests to five endpoints. **Every header fixed:** to Binance `User-Agent: adv3-advisor/1`, beside `urllib`'s own `Accept-Encoding: identity`, `Host` and `Connection: close`; to Telegram `User-Agent: adv3-bot/1` and `Content-Type: application/json`, beside `urllib`'s `Content-Length`, `Accept-Encoding: identity`, `Host` and `Connection: close`. A refused request is never retried but for a network error, `418`, `429` or a `5xx`, three times after 1, 3 and 5 s (`adv3.get`); Telegram's `call` has one try. The unit's own requests at its checks go through the same functions and headers.

**UNIT-NEW** (`I unit new`), nine, read against the `kill` mark's snapshot: the unit `active`, `running`, `enabled`; a new `MainPID` and `NRestarts` one more; the process started after the mark and within 90 s of it; its argv the unit's exact one, alone; the service copy's `adv3.py` and `adv3-bot.py` Appendix A's and the process started after B-DEPLOY's mark; the unit file unchanged; no `daily` record added since the mark; `service.log` showing the new process serving and no traceback since the mark; the three capture units active with their `MainPID` and `NRestarts` as at the mark.

**G-FIRST** (`I first`), seven, from the journal's records stamped since the `kill` mark, `check-done` and `service.log`'s lines since the mark: exactly one check record; it is the day's signal check, of the close of the day before, under rule `ee206e7c…`; it was sent, its Telegram message ids integers; it holds the 42 coins' state, the six ratings, its alerts and its placed coins, and is quiet exactly when it holds no alert; `check-done` reads the day's `signal` where the mark came before 12:10 UTC and its `fact` where after — a first check read within 900 s of a mark at or before 11:50 ended before 12:10, and one after a mark at or after 12:20 marks the fact slot done too (`done_after`); the log since the mark shows the new pid serving from no `check-done`, the check sent and no check failed and no traceback; the journal ends in a newline and every line from that record on parses. **NOT YET** while no check record stands since the mark and 900 s have not passed. Printed beside it: the check's flags, its message count, its alerts by kind, its followed trades and placed coins, and `check-done` — never a coin or a price.

### 4.4 The stops — CANON hard rule 14

**The unit's restart policy is TZ-35's, unchanged** — `Restart=always`, `RestartSec=30`, `RestartPreventExitStatus=3 4` — and so is its stop, K-35, `systemctl disable --now adv3-bot.service`, which K-39 repeats. **B-ROLLBACK**, on a FAIL of COPY, G-RENDER, P-START, B-KILL's mark, UNIT-NEW or G-FIRST, at once, the Executor's own: the two files and `commit.txt` return to what B-DEPLOY saved.

```
{ date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz39-work/stage/research/tz39-advisor-checks.py mark rollback && cp -p /root/tz39-work/adv3.before /root/adv3-bot-svc/adv3.py.new && cp -p /root/tz39-work/bot.before /root/adv3-bot-svc/adv3-bot.py.new && mv /root/adv3-bot-svc/adv3.py.new /root/adv3-bot-svc/adv3.py && mv /root/adv3-bot-svc/adv3-bot.py.new /root/adv3-bot-svc/adv3-bot.py && cp -p /root/tz39-work/commit.before /root/adv3-bot-svc/commit.txt; echo "exit=$?"; } >> /root/tz39-work/logs/30-b-rollback.log 2>&1
sha256sum /root/adv3-bot-svc/adv3.py /root/adv3-bot-svc/adv3-bot.py; cmp /root/adv3-bot-svc/commit.txt /root/tz39-work/commit.before; echo "cmp exit=$?"
```

The second line is the Executor's own read. `exit=0`, the `sha256sum` printing `d73a657e…` and `3a044d50…` and `cmp` exit `0`, or the run is BLOCKED with the files' state named. Where the unit was **not** signalled (a FAIL of COPY, G-RENDER, P-START or B-KILL's mark) that is all: the running process never loaded the new files. Where it **was** (a FAIL of UNIT-NEW or G-FIRST), the signal follows, its mark inside the block, in the band of §3.5:

```
until s=$(( $(date +%s) % 86400 )); { [ $s -ge 23700 ] && [ $s -le 42600 ]; } || { [ $s -ge 44400 ] && [ $s -le 85800 ]; }; do sleep 5; done; { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz39-work/stage/research/tz39-advisor-checks.py mark kill2 && systemctl kill --signal=SIGTERM adv3-bot.service; echo "exit=$?"; } >> /root/tz39-work/logs/31-b-kill2.log 2>&1
```

and at least 45 s later `I unit old`, each run appended to `32-unit-old.log` (every 15 s while it prints `NOT YET`, at most 100 s after that mark) — **UNIT-OLD**, `READING UNIT-OLD: PASS - 10 of 10`: UNIT-NEW's nine read against the second mark with TZ-36's `adv3.py` and TZ-37's `adv3-bot.py`, and `NRestarts` two more than at the first mark. The old code reads `daily-sent`, today's at both marks, and ignores `check-done` and the `check` records the new process left; both stay, and the report names them.

**K-39**, on a FAIL of UNIT-OLD only — the advisor is then stopped, and the Boss is told:

```
{ date -u +%FT%T.%NZ; systemctl disable --now adv3-bot.service; echo "exit=$?"; } >> /root/tz39-work/logs/33-k39.log 2>&1
```

by the classifier route where refused (the Boss runs the block unchanged), verified at least 30 s later by `I stopped`, appended to `34-stopped.log`, which must print `READING STOPPED: PASS - 2 of 2`. **Under PASS neither B-ROLLBACK nor K-39 is run.**

### 4.5 What a PASS establishes, and what it does not

The service copy's `adv3.py` and `adv3-bot.py` are Appendix A's and the unit runs them; the rule, its fourteen functions, the rule text, the unit and the allocation's arithmetic are what TZ-35 to TZ-37 deployed; the seven commands and both checks are answered on live data with the shapes §4.2 fixes, and on that data the allocation keeps its limits and every exit of a trade the cards offered is alerted once; the new process ran its first check at its start and sent it. **Not established:** that the 00:10 and 12:10 checks fire on their own clock — the self-tests prove the schedule over three simulated days minute by minute, and the next TZ's host gate reads the `check` records the unit wrote since; that a day with an exit or a candidate was among G-RENDER's (the report prints the counts); that the Boss's Telegram shows the messages as the Architect expects, and that a quiet message stays quiet on his phone; that the followed trades are the Boss's — the bot holds no account; that the sizes or the alerts are good ones — the forward record, read after 2027-10-28, measures the rule and none of them; and anything about the market to come.

---

## 5. The files

**`advisor/adv3.py`** — replaced: `changes` and `assessment` added; `message` loses the methodology, the forward book, the rule's open STRONG positions and the six ratings, takes `head` and `tail` lines and the report's N, and gives each card its confidence; `card_lines` takes the shares from `PIT` and ends with the confidence line; `trust_lines` quotes the ladder and TZ-38's figures; `PIT` and `LADDER` added. Every other line, the rule's fourteen functions among them, is TZ-36's. **`advisor/adv3-bot.py`** — replaced: the schedule (`SLOTS`, `slot_key`, `slot_at`, `slot_text`, `slot_parse`, `latest_slot`, `due`, `done_after`, `next_at`, `hhmm`); the report and the list (`live_report`, `ranked`, `top_n`; `make` takes N); the journal (`CARD_KEYS`, `journal_records`, `journal_scan`, `append`, `base_record`, which replace `journal`); the monitor (`offers`, `alerted`, `follow`, `forming_candles`, `candidates`, `alerts_of`, `weakened`, `zones_left`); the messages (`event_lines`, `candidate_lines`, `followed_lines`, `zone_lines`, `weak_lines`, `quiet_line`, `compose`, `strong_shares`, `item_lines`; `plan_parts` one text); `check_record` and `check`; `serve`'s loop on the slots; `handle` with «оценка» and N; `Telegram.send` with its quiet flag; `probe` with the forming candle; `hello`'s text; `route`; `HELP`; and `selftest`, 106 checks offline — the commands, the schedule over three days minute by minute, the monitor on synthetic candles, the alerts, the zones, every message's shape, the record, three checks end to end on a scratch journal, the TOP-N list, TZ-37's golden cases and a fifth at 14 %, the limits over 400 random scenarios, the replies, the quiet flag. **`advisor/selftest-adv3.py`** — replaced: TZ-36's 44 checks, the one that read the forward book and the six ratings in the message now reading that it carries no methodology and the two of the reach shares reading TZ-38's, and nine more — each card's confidence without current prices, with them and with no entry, the assessment's contents, its quotations and its markup, `changes` twice, and the head and tail — 53. **`research/tz39-advisor-checks.py`** — this TZ's checker: `fingerprint`, `host`, `number`, `rule`, `selftest`, `mark`, `copy`, `render`, `unit`, `first`, `keep` and `stopped`. Where a reading can be a pure function it is — `parse_map`, `tree_checks`, `report_sections`, `pit_from_report`, `plan_invariants`, `sign_sum`, `walk`, `alert_checks`, `render_checks`, `unit_checks`, `first_checks`, `log_since`, `records_since`, `memory_gate`, `count_kind`, `number_reading`, `kept_files` — and its self-test runs each on stand-ins with a negative control for every one that can fail, and `render_run`, the render's own pipeline, **on the stage's bot with a synthetic market and Binance stood in for**: 22 of 22, every alert kind met, and eighteen negative controls on its output. `host`, `copy`, `mark`, `unit`, `first`, `keep` and `stopped` read the host and are exercised there. It starts, stops and signals nothing; its `render` runs the service copy's bot. Standard library alone, under `/root/tz04a-env`.

---

## 6. Cost

Measured by the Architect on 2026-11-01 under Python 3.12.3 and 3.13.18 and taken at the population's upper bound.

| check | population | measured | bound |
|---|---|---|---|
| the three self-tests | 53, 106 and 64 checks, no network | `0.13` to `0.20` s, `0.53` to `0.57` s and `0.38` to `0.42` s of wall under 3.12.3, three runs each; peaks at most `25,903,104`, `34,955,264` and `36,470,784` bytes | `30` s each |
| G-RULE and FINGERPRINT | `git show` of six paths, four syntax trees, TZ-38's report, the map's 58 rows | `0.27` to `0.41` s together, peak at most `38,129,664` bytes | `5` s a run |
| G-RENDER | one process: 84 requests of `Data` over six threads, once; two for the marks and the funding intervals at each of seven reports; at most three for the volumes at each of two allocations and two checks; one forming candle for each coin of an offered trade at the fact check, at most 42; seven replies and two checks | `3.7` to `5.1` s of processor under 3.12.3 over fifteen runs on the archive's candles of the 42 coins to the close of 2026-10-30 — 13 offers read, an exit and two or three candidates at the signal check, seven forming candles at the fact check — and `55,754,752` bytes at its peak (§0.4); TZ-37 measured `13.70` s of wall live on the host for its render (map §2.7) | `900` s of wall, the `timeout`; `30` s of processor |
| P-START | six requests to five endpoints, one after another | TZ-37's five, from 13:56:10 to 13:56:13 UTC (its report) | `675` s of wall at worst — five requests at `129` s and one at `30` s — without processor |
| UNIT-NEW and G-FIRST | `systemctl show`, `/proc`, the journal and the log | under `1` s a run | `30` s; at most 4 and 60 runs |

**Single-session processor at most `630` s at those bounds** — the self-tests `90`, G-RENDER and P-START `30`, at most `90` checker runs at `5` s, `450`, and the `reclaim`, `git` and `systemctl` commands `60` — **under `3,600`, so nothing is sampled.** **Wall clock about 50 minutes:** §0 to §3.3 about 15 minutes; §3.4 and §3.5 about 6, the restart's 35 s and the first check's minute among them; §3.7, the report and §9 about 20. **`81` minutes with every `timeout` and every request at its bound** — `10 + 5 + 2 + 5 + 16 + 12 + 16 + 2 + 10 + 3` (§0 with the memory re-read; §3.1; §3.2; §3.3; B-DEPLOY, COPY and G-RENDER at 900 s; P-START at 675 s; the signal, UNIT-NEW and G-FIRST at 945 s; §3.7; the report; §9) — and up to 30 more where a paste waits for the Boss; plus a wait for B-DEPLOY's band of at most 7 h 15 min, from 23:20:00 to 06:35:00 UTC. **The host pays, after the session:** two checks a day of the unit's own — at 00:10 at most 89 requests to `fapi.binance.com`, 84 for the candles and funding, two for the marks and the funding intervals and at most three for the volumes; at 12:10, for a process that ran the 00:10 check, at most 47, the two, the three and one forming candle for each coin of an offered trade, about a dozen on the render's 13 offers — a few seconds of processor each; and a journal growing about `21,000` bytes a day [modelled: the render's two check records, `11,187` and `9,604` bytes, at 13 offers on the archive's candles].

---

## 7. Validation

| # | check | count |
|---|---|---|
| **V1** | §0.2's fingerprint | `READING FINGERPRINT: PASS - 67 of 67`: revision `2026-10-31-c`; 6 anchors, 4 re-derived; 58 rows, 55 of 55 `frozen` equal |
| **V2** | §0.3's host gate | `READING HOST: PASS - 16 of 16`; the memory figures of the first read and of the second, if one was made |
| **V3** | §0.5's NUMBER, at §0.5 and at §3.1 | `READING NUMBER: PASS - 2 of 2` each, the `TZ-39-` path printed; the branch count `0` |
| **V4** | §0.1's and §3.1's files | 4 of 4 hashes asserted at each, lines and bytes; the branch's diff naming exactly `M`, `M`, `M`, `A`, and `--numstat` exact |
| **V5** | the self-tests | `53 of 53`, `106 of 106`, `64 of 64` |
| **V6** | G-RULE | `READING RULE: PASS - 10 of 10` |
| **V7** | B-DEPLOY | `exit=0`; the mark printed |
| **V8** | COPY | `READING COPY: PASS - 5 of 5` |
| **V9** | G-RENDER | `READING RENDER: PASS - 22 of 22`; the printed counts |
| **V10** | P-START | `READING P-START: served - 5 of 5 endpoints`, each line printed |
| **V11** | B-KILL and UNIT-NEW | `exit=0`; `READING UNIT-NEW: PASS - 9 of 9`, both pids, both instants |
| **V12** | G-FIRST | `READING FIRST: PASS - 7 of 7`; the printed counts |
| **V13** | contract §4.2's self-check | run after the push and the pull request and before the report's commit |
| **V14** | §3.7's closing reads | every read printed |
| **V15** | B-RECLAIM-SCRATCH and §9's `keep` | files considered, copied and held; the store's count after equal to before plus the copies |
| **V16** | §9's removals | `git worktree remove` without `--force` exit `0`; `test -e` exit `1` for `/root/tz39-work` and each directory removed; `git worktree list` naming `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else |
| **V17** | every block refused and every paste the Boss ran | its refusal's text, the paste, when he ran it and every log line it appended, and the Executor's own reads after it |

---

## 8. The report

`CryptoReports/TZ-39-advisor-checks-report.md`, in contract §8's order. **In its first ten lines:** NUMBER at both reads; G-RULE; the three self-tests; B-DEPLOY, COPY, G-RENDER — with the number of STRONG coins, the trades placed per allocation and each check's alerts by kind — and P-START; B-KILL, UNIT-NEW and G-FIRST with the pids and the first check's flags; whether a rollback ran; whether the unit runs, and how that was verified; every block refused and who ran it. Beyond what V1 to V17 print: every mark's instant; the unit's journal lines; each memory and free-space read with its instant and bound; the commit and the pull request; §9's counts and removals; and every file the run wrote, by SHA-256, but the bot's own root and the render's scratch journal. **It never prints the token, the chat id, the content of any file under `/etc/adv3-bot/`, or a coin, a price or a size from the live replies or a journal** (§2 item 7). The report is drafted in the primary checkout `/root/btc-5m-twap` before B-RECLAIM-OWN and committed after it.

---

## 9. Reclaim — the host left clean (CANON hard rule 15)

**What a file is kept for:** `I keep` copies every file under `logs/`, `state.json`, `adv3.before`, `bot.before` and `commit.before` into `/root/btc-forensics/` as `tz39-work--<path with - for />`, by exclusive create, and verifies each hash; a name already there with the same hash is counted as held, and with another a failed assert. The branch worktree is not copied: `keep` asserts that `git status --porcelain --ignored` in it prints nothing and that its `HEAD` is its upstream's, so `git worktree remove` needs no `--force`. **No output of `keep` or `reclaim` is filtered**: every line it prints is quoted. B-RECLAIM-SCRATCH is §3.3. `render-state/` is scratch — a copy of the bot's journal, prices and coins among it — never kept, and goes with the tree.

**B-RECLAIM-OWN**, last, after §3.7 and with the report drafted. **Its output is written to no file; the report quotes it verbatim from the session**, every line of it:

```
nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz39-work/stage/research/tz39-advisor-checks.py keep
git -C /root/btc-5m-twap worktree remove /root/tz39-work/wt; echo "exit=$?"
rm -rf /root/tz39-work; echo "exit=$?"
test -e /root/tz39-work; echo "exit=$?"
git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
find /root/btc-forensics -type f | wc -l
df -B1 --output=source,size,avail /var/lib/btc-recorder
```

The branch `tz-39-advisor-checks` stays on `origin` and as a local ref; only its working tree goes. **Kept:** `/root/adv3-bot-svc/` is the running unit's code, `/var/lib/adv3-bot/` its record — `check-done` and the `check` records among it — and `/etc/adv3-bot/` the Boss's token and the pinned chat; the capture roots, both archives' state and the forensic store are data, never scratch. **A refused `rm -rf` is handed to the Boss** by §3.3's route, one tree per command, and verified by `test -e`.

---

## 10. Pre-send checks

Performed by the Architect on 2026-11-01 against this file as sent, in a reading separate from its writing — the body was written, read start to end and corrected where it read wrongly (the corrections are named in C7), and this section written after — with the repository at `origin/main` `17dc258c4ee56a609b2dbd12c73b8cc197bc80d9` (the merge of PR #38; fetched again before sending, `main` still carrying map revision `2026-10-31-c`, no `TZ-39-` file, no report of that number and no `tz-39` branch), the map at that commit (2,003 lines, SHA-256 `c2a318619bfaaa215a06870f90a8e906ae077dc5ab2b90f4d7dee6646e195a31`) and CANON revision `2026-10-31-c`. Line numbers are those of the files §0.1 extracts for Appendix A, and those of `main` for committed code.

| # | check | result |
|---|---|---|
| **C1** | scope against body | **Repository paths the body names:** `CryptoTZ/TZ-39-advisor-checks.md`, read by §0.1's script and named by `number`; `CryptoTZ/` and `CryptoReports/`, listed by `number`, every `CryptoReports/*.md` read by TZ-35's `reclaim` for hash tokens; `SYSTEM-MAP.md` and the other 57 rows of its table, read by `fingerprint`, among them `BTC-EXECUTOR-INSTRUCTIONS.md` (cited for contract §1, §4.1, §4.2 and §8), `research/tz33-reward-book-capture.py` (cited for line 190), `research/tz35-advisor-deploy.py` (run for `scratch` and `reclaim`) and `research/twap-divergence.py`, `research/recorder/recorder.py` and `research/pfair.py` (hashed for the anchors); `advisor/adv3.py`, `advisor/adv3-bot.py` and `advisor/selftest-adv3.py`, written on the branch, the first two copied to the service; `research/tz39-advisor-checks.py`, written on the branch; `advisor/RULE-ADV-3.txt`, `deploy/systemd/adv3-bot.service` and `CryptoReports/TZ-38-adv3-pit-validation-report.md`, read and hashed by `rule`, never written; `CryptoReports/TZ-39-advisor-checks-report.md`, written to `main`. **Host paths:** `/root/tz39-work/**` written (`render-state/` among it, scratch); `/root/adv3-bot-svc/adv3.py`, `adv3-bot.py` and `commit.txt` written, `adv3.py.new` and `adv3-bot.py.new` transient; `/var/lib/adv3-bot/{journal.jsonl,offset,daily-sent,check-done,service.log}` read and hashed, `journal.jsonl` copied into `render-state/`; `/etc/adv3-bot/token` read by the bot's own `--probe` and nowhere else; `/etc/systemd/system/adv3-bot.service` hashed; `/var/lib/btc-recorder` read by `find`, `grep -c` and `df`; the other capture stores by `du`; `/root/btc-forensics` written by `keep` and `reclaim`; `/proc/meminfo`, `/proc/stat` and the processes' `cmdline` and `stat` read by `host` and `unit`; the UUID directories of `/tmp` read, copied from and removed by TZ-35's checker. **Entry points:** this checker's modes `fingerprint`, `host`, `number`, `rule`, `selftest`, `mark` (`deploy`, `kill`, `rollback`, `kill2`), `copy`, `render`, `unit` (`new`, `old`), `first`, `keep` and `stopped`; TZ-35's `scratch` and `reclaim`; `selftest-adv3.py`; `adv3-bot.py --selftest` and `--probe`; `git` (`fetch`, `ls-remote`, `log`, `ls-tree`, `worktree`, `add`, `diff --cached`, `commit`, `push`, `show`, `rev-parse`, `status`), `gh`'s credential helper; `systemctl` (`show`, `list-timers`, `is-enabled`, `kill`, and `disable` at K-39 only); `journalctl` (the unit's lines, §3.7), `cp`, `mv`, `sha256sum`, `cmp`, `timeout`, `nice`, `rm -rf`, `test -e`, `mkdir`, `du`, `df`, `free`, `find`, `grep`, `wc`, `ls`, `cat`, `tail`, `date`, `uptime`, `nproc`. **Outputs:** under `/root/tz39-work/` `logs/`, `stage/`, `wt/`, `render-state/`, `state.json`, `adv3.before`, `bot.before`, `commit.before`; the service copy's three files; the forensic store's copies; the branch, its pull request and the report. **Intersections with §2, by path and by content class, eight, each named in §2:** the bot's `--probe` reads the token — item 3's exemption; G-RENDER's and P-START's requests — item 3; `systemctl list-timers`, `is-enabled`, `show`, `kill` and `disable` — item 4; `find`, `grep -c`, `df` and `du` on the capture stores and `systemctl show` of their units — item 5, reads; `tail` of `service.log`, `journalctl` of the unit, `cat` of `state.json` and `check-done` and `ls` of the record — item 7: they carry log lines, pids, instants, sizes and a slot, and `service.log`'s lines name a close, a slot, a kind of request and counts, and a coin only where Binance failed to serve it, never a price or a card (§3.7); **`render-state/journal.jsonl`** — item 7's content class, the coins and prices of cards and of the allocation: a scratch file of the work tree, never printed, never copied by `keep` (`kept_files`, lines 825 to 831, copies `state.json`, the three `.before` files and `logs/` alone) and removed with the tree by §9; **`/var/lib/adv3-bot/journal.jsonl`**, the same class — read by `mark`, `unit` and `first` and copied by `render`, each printing counts and labels alone (`mode_mark` 650, `render_print` 749 to 759, `mode_first` 818 to 821); the live replies — item 7: held in memory by the stand-in, never printed. **Classes checked and intersecting nothing:** labels, outcomes and settled documents — this TZ reads none; Binance's candles, marks and volumes pass through the service copy's `Data`, `live_report`, `liquidity` and `forming_candles` in the live render and are stored nowhere but in that scratch journal. |
| **C2** | origin of every expectation | **Quoted from a committed artifact, at `17dc258`:** revision `2026-10-31-c`, the six anchors, `58`, `55`, `2` and `1` — map §0, its table counted independently of the checker by the Architect's parse (58 rows: 55 `frozen`, 2 `tracked`, 1 `reported`) and each frozen row's lines, bytes and SHA-256 compared with its blob at `17dc258`, `55 of 55` equal, then by `fingerprint` against the clone, `PASS - 67 of 67`; `2,312`, TZ-38's two directories and `238335b9…` — map §3, line 1320, and TZ-38's report; the hashes `d73a657e…`, `3a044d50…`, `ef4ffc44…`, `ee206e7c…` and `82acd8e4…` — map §0's table, lines 167 to 171, and `sha256sum` of the files at `17dc258`; `f4a0ac3f…` — `sha256sum` of TZ-38's report at `17dc258`, 1,641 lines, 103,678 bytes; `PIT`'s figures — TZ-38's report §2.7: E1 `p_t_up` `0.0735` (line 898), `trades` `19,002` (902) and `mean_R` `0.0403` (923), E2 `p_t_up` `0.1100` (963), E4's `mfe` rows (1022 to 1024) and STRONG's `top5_share` `0.9875` (1036), E5's median `0.2195` (1055), `lists` `500` (1061) and `share_mean_R_positive` `0.8600` (1065), and `G` `570` (1192), read again by `pit_from_report` and equal; §1's `265`, `28`, `25`, `212`, `+0.36`, `+0.48`, `+0.55`, `+0.51` and `+0.80` — E6, lines 1102 and 1140 to 1142; `184`, `+0.998`, `−0.238` and `38.6 %` — E7, lines 1164 to 1171; `10,089,811,968` — TZ-38's report, line 322; `65,490,944`, `58,953,728` and `49,168,384` — map §6, memory (line 1710); `13.70` s — map §2.7 (line 1056); TZ-37's P-START from `13:56:10` to `13:56:13` — its report, line 495; `7,300,000,000` — `research/tz33-reward-book-capture.py` line 190, `STREAM_FLOOR = 7300000000`, and map §2.6; `31612203008` and `e3975b5…` — map §6's host identity (line 1686); `0.5`, `1`, `5` and `10,000` — `adv3.RISK`, `RISK_MAX`, `RISK_ALL` and `DEPOSIT`, line 22 of `main`'s `adv3.py`; `3` — `TOP_N`, line 19; `0.001` — `COST`, line 18; the rung `1` — `RELIABILITY`, line 37; `300` s — `RETRY`, line 19 of `main`'s bot; `30` s, `3 4` and `128M` — the unit, lines 15, 16 and 18; `14`, `7`, `00:10`, `12:10`, `04:10`, `16:10` and `11.1` — CANON PART VII. **Computed by an implementation independent of the one under test:** `130,981,888` = 2 × `65,490,944`; `65,465,944` = `54,599,680` × `58,953,728` / `49,168,384` [modelled]; the render's peaks — at most `55,754,752` over fifteen runs under Python 3.12.3 and `54,599,680` under 3.13.18 — `resource.getrusage` of the process that ran `render_run` on the archive's candles; the self-tests' and G-RULE's walls and peaks — a parent's `RUSAGE_CHILDREN`, three runs each; the numstats `1005 245`, `118 64`, `42 8` and `1139 0` — `git diff --cached --numstat` over §0.1's script run into a worktree of the clone at `17dc258`; §0.1's table — `wc` and `sha256sum` of the four files, equal to the script's own lines over an empty stage and over that worktree; `352`, `4`, `88` and `50` at 14 % — exact arithmetic, `⌊50 / 0.142⌋`, `⌊1 / 0.22⌋`, `⌈352 / 4⌉` and `⌈352 × 0.142⌉`, equal to the bot's fifth golden check; the record sizes `11,187` and `9,604` — the archive render's scratch journal, by line; `11,540,664` — `du -cb` of the tracked files at `17dc258`. **Fixed by Appendix A's code, which this TZ measures nothing to set:** `67`, `16`, `2`, `10`, `5`, `22`, `9`, `7`, `10` and `2` (FINGERPRINT, HOST, NUMBER, RULE, COPY, RENDER, UNIT-NEW, FIRST, UNIT-OLD, STOPPED), `53`, `106` and `64` (the self-tests), `5` endpoints and `6` requests, the `7` commands and `7` record kinds of the render, and G-RULE's `44` and `13` identical, `3` and `9` changed, `2` and `35` added and `1` removed definitions — each the count its function's dictionary or tuple holds, re-run by the Architect where it runs off the host (C5). **Fixed by this TZ and measured by nothing:** the bands, the 45 s wait, the 15 s polls, UNIT-NEW's 90 s and 100 s, G-FIRST's 900 s and the `timeout`'s, the 60 s memory re-read and the session's `100,000,000` bytes — the Architect's choices, named so. **The floors and the bands:** `7,400,000,000` = `7,300,000,000` + `100,000,000`; `23,700` = 6 × 3,600 + 35 × 60, `40,800` = 11 × 3,600 + 20 × 60, `42,600` = 11 × 3,600 + 50 × 60, `44,400` = 12 × 3,600 + 20 × 60, `84,000` = 23 × 3,600 + 20 × 60, `85,800` = 23 × 3,600 + 50 × 60; `675` = 5 × `129` + `30`, `129` = 4 × 30 + 1 + 3 + 5. **No expectation depends on a quantity this TZ measures but as an inequality or an equation that holds for every admissible value of it:** UNIT-NEW reads `NRestarts` as the `kill` mark's plus one, the capture units' as the mark's and the `daily` records as the mark's, whatever the mark read; the memory and disk gates are inequalities on a read; G-RENDER's limits are inequalities, and its equations are between the replies, records and alerts and the plans and walks recomputed from the same reports, candles and offers; G-FIRST reads `check-done` against the mark's instant — `signal` for a mark in the morning band, `fact` in the afternoon one — which holds for every mark either band admits (§4.3); the numbers of alerts, candidates and trades placed are printed, never asserted. |
| **C3** | shape of every diff | Four paths, read from `git diff -U0` over the extraction at `17dc258`. **`advisor/adv3.py` replaces 64 committed lines:** 34–36; 531–533; 546–554; 557; 563; 568; 570; 573–577; 591–599; 603–604; 606–610; 626–627; 629–635; 641–645; 649; 654–656; 658; 663–664; 678; 681; 689 — the ratings' comment, `message`'s signature, docstring and its changes, card, forward-book and methodology blocks, `trust_lines`'s body and `card_lines`'s shares and basis — `--numstat` `118 64`. **`advisor/selftest-adv3.py` replaces 8:** 4 (the imports, `sys` dropped); 109–112 (the check that read the forward book and the six ratings in the message); 118–120 (the two shares checks) — `42 8`. **`advisor/adv3-bot.py` replaces 245:** 2–3; 18; 23–25; 27–33; 89–91; 95; 101; 134–137; 140; 147–149; 192–193; 205; 306; 308; 325–341; 348–365; 382; 384; 386; 389–390; 392–393; 396; 398; 400–401; 403–409; 433–435; 437–442; 444; 461; 466; 515; 521–522; 526; 530–533; 539; 543; 545–549; 552–553; 560; 578–580; 586–587; 589; 592–593; 596–600; 615–617; 621–622; 634–635; 637–641; 643–684; 687; 689; 692; 694–696; 698–701; 704–706; 709–722; 726; 731–732; 735–744; 747–748; 750; 752–770; 772; 774 — the header, `DAILY`, `STOP_MAX`'s line and `HELP`, `Telegram.send`, `route`, `make`, `plan_parts`, `journal`, `serve`, `handle`, `probe`, `hello` and lines of `selftest` — `1005 245`. **`research/tz39-advisor-checks.py` is new**: `git cat-file -e 17dc258:research/tz39-advisor-checks.py` exits `128`, as do the report's path and this TZ's own; `1139 0`. No sentence of this TZ calls a change additive or speaks of insertions only. |
| **C4** | cost of every check | §6, at the population's upper bound. **Processor, single session, term by term:** the three self-tests `3 × 30 = 90` s against `0.20`, `0.57` and `0.42` s measured at most; G-RENDER and P-START `30` s against `5.1` s at most measured for G-RENDER's seven reports, replies and two checks; at most `90` checker runs at `5` s, `450` s — HOST up to 2, FINGERPRINT 1, NUMBER 2, RULE 1, the marks up to 4, COPY up to 2, UNIT-NEW up to 5, G-FIRST up to 61, UNIT-OLD up to 5, KEEP 1 and STOPPED up to 2, `86` at most, each under `1` s measured but RULE and FINGERPRINT, `0.41` s together; and the `reclaim`, `git` and `systemctl` commands `60` s: **`90 + 30 + 450 + 60 = 630` s, under `3,600`; nothing is sampled.** **The fail-fast bounds, each with its derivation:** `adv3.get`'s four tries — four `30` s timeouts and the `1`, `3` and `5` s between them, `129` s, `adv3.py` lines 42 to 60, unchanged — make a render with Binance silent worst at `14 × 129 = 1,806` s for `Data`'s 84 requests over six threads, `14 × 129 = 1,806` s for the marks and funding intervals of seven reports, `12 × 129 = 1,548` s for the volumes of at most three STRONG coins at two allocations and two checks and `42 × 129 = 5,418` s for the fact check's forming candles, `10,578` s in all, so G-RENDER runs under `timeout 900`; P-START's six requests one after another, `5 × 129 + 30 = 675` s of wall (`Telegram.call` has one try of `30` s), `adv3-bot.py` lines 962 to 987; UNIT-NEW's `NOT YET` at most 100 s after the mark, every 15 s, at most 4 runs in a paste; G-FIRST's at most `900` s after the mark, every 15 s, at most 60. **Wall clock:** about 50 minutes; `81` with every bound reached — `10 + 5 + 2 + 5 + 16 + 12 + 16 + 2 + 10 + 3` — up to 30 more where a paste waits for the Boss, and a wait for B-DEPLOY's band of at most 7 h 15 min. Disk at the same bound: §0.4's `100,000,000`, the logs under `2,000,000` bytes. **After the session:** at most 89 requests at 00:10 and 47 at 12:10 a day, §6, each under the same `get`. |
| **C5** | every count | `67` = 1 revision + 6 anchors + 4 re-derived + 55 frozen rows + 1 table shape, `parse_map` and `mode_fingerprint` (lines 155 and 521), the table counted again by the Architect's parse — `58` rows, `55` frozen, `2` tracked, `1` reported. `16`, `mode_host` lines 546 to 582: H1 one, H2 two, H3 one, H4 three, H5 six, H6 one, the memory gate and the disk gate; `16 of 16` on stand-ins for systemd, `/proc`, `df` and the host's files, and `memory_gate` deciding a low first read by the second. `2`, `number_reading` (513): `PASS` on stand-ins with the one file, `FAIL` with a second `TZ-39-` file and with a report, and `FAIL - 1 of 2` on the clone at `17dc258`, which holds no `TZ-39-` file. `4` files and `4` hashes, §0.1. `10` = `mode_rule` (608 to 627): two file checks, three of `tree_checks` (182) for `adv3.py`, `PIT` against `pit_from_report` (212), three of `tree_checks` for the bot and the three hashes — `10 of 10` on the clone and on the extracted worktree. `53` = 44 + 9, `106` and `64` = 44 + 2 + 18 — each listed by its run, `53 of 53`, `106 of 106` and `64 of 64` on the files §0.1 extracts. `5`, `mode_copy` (655), `5 of 5` on a stand-in origin, worktree and service copy. `22` = `render_checks` (311 to 415), `22 of 22` on the stage's bot with the synthetic market and on the archive's candles, and each of eighteen faults reading FAIL. `5` endpoints and `6` requests, `probe` (962 to 987). `9`, `unit_checks` (418), and `10` with `mode_unit`'s extra check (800): `9 of 9` and `10 of 10` on stand-ins for a deploy, a kill, a restart, a rollback and a second kill, and eight faults reading FAIL. `7`, `first_checks` (439), `7 of 7` on stand-ins, and nine faults reading FAIL. `2`, `mode_stopped` (864). `7` = `RENDER_CASES`, `7` = `RENDER_KINDS`. G-RULE's lists — for `adv3.py` `3` changed, `2` added, `0` removed and `44` identical of `main`'s `47` definitions, for the bot `9` changed, `35` added, `1` removed and `13` identical of `23` — the Architect's own AST script, equal to `ADV3_DEFS` and `BOT_DEFS` and to §4.1's names. V1 to V17 are §7's seventeen rows. |
| **C6** | every population | NUMBER: the paths under `CryptoTZ/` and `CryptoReports/` of `origin/main` at each of its two reads. FINGERPRINT: the map's table of 58 rows against the files of the primary checkout. HOST: the host at the instant of the read — its units, files, memory and disk; the memory figure the first read and, if it fell below the floor, the second. RULE: `adv3.py`, `adv3-bot.py`, `RULE-ADV-3.txt`, the unit file and TZ-38's report of `origin/main` against the branch's files. The self-tests: synthetic candles and stand-ins, no network. COPY: `/root/adv3-bot-svc` and the worktree. RENDER: the service copy's bot answering seven texts and running two checks on the latest close at the run's instant — the 42 coins' candles, at most 1,500 each, marks, funding intervals, the volumes of at most three STRONG coins at each allocation and check, and the forming candles of the offered coins at the fact check — over a copy of the bot's journal; for each allocation the plan recomputed from the report and volumes that reply was made from; for each check the checker's walk of every offer the journal held before it. P-START: one request to each of five endpoints, the klines endpoint twice. UNIT-NEW and UNIT-OLD: the unit, the three capture units, the journal's `daily` records and `service.log`'s lines stamped at or after the mark less 1 s. G-FIRST: the journal's records stamped at or after the `kill` mark less 1 s, `check-done` and `service.log`'s lines since the mark. KEEP: the work tree's files §9 names. RECLAIM: the UUID directories `scratch` names earlier. §1's history figures: TZ-38's E6 and E7, STRONG's 265 trades on *P*, in sample. §6's journal growth: the archive render's two check records. Each memory figure: one mode's process; `MemAvailable` and free space: the host at each read. No statistic of this TZ is a calibration claim and none is read against a label. |
| **C7** | every signature and every behaviour | **Committed code this TZ relies on, read at `17dc258`.** `adv3.py` — `def get(url, tries=4):` line 42, four tries of 30 s with 1, 3 and 5 s between them (42 to 60), the `129` s of §6; `def fapi(path, **params):` 133; `def fapi_candles(sym, now_ms):` 137, `limit=1500` and `if int(r[6]) < now_ms:` (140, 141), the closed candles; `def fapi_funding(sym, first):` 146, pages of 1,000 (150 to 157); `def fapi_intervals():` 161; `def fapi_marks():` 166; `def ms_day(ms):` 76; `def signs(days, closes, i):` 173, `j = bisect.bisect_right(days, days[i] - L * DAY) - 1` (177) — the last close at least L days before, as the checker's `sign_sum` reads it; `def signal(days, closes, i):` 184; `def strength(days, closes, i):` 193, returning `z, sum(x for x, _, _ in s)` (203), which `weakened` reads at the close before; `def open_at(side, close, U, day):` 218, `'S': close - side * U` (219); `def hold(pos, candle, pc, fund_d, day):` 222, `X = o if ((o <= S) if k > 0 else (o >= S)) else S` (227) — the stop inside a day, at the open where the open is beyond it; `def close_at(pos, close, day):` 237; `def simulate(c, fund, first_entry, last_day):` 243, holding then reading the signal, `if pos and sig != pos['d']: … close_at` (250 to 258), the order `follow` keeps; `def ranking(day_states):` 285, `top = sorted(active, key=lambda cs: -abs(cs[1][1]))[:TOP_N]` (288) and STRONG among it (289), which `ranked` applies again; `def trust(rep):` 360, `'cards': {cd['coin']: RELIABILITY if cd['mode'] != 'none' and rep['marks_ok'] else 0 …}` (370) — the card's confidence; `def report(cs, funds, marks, deposit, risk, now_ms, missing=(), intervals=None):` 427, each row's `'prev'` (442), which `changes` reads; `def card(coin, row, is_strong, deposit, risk):` 473, `S = C - k * U` (476), its modes (480, 482) and `stop_pct` and `leverage` (491, 492); the constants lines 14, 18, 19, 22 and 37. `adv3-bot.py` of `main` — `POLL, RETRY, LIMIT = 50, 300, 4000` (19); `def put(path, text):` 51, one rename (51 to 58); `class Telegram:` 71 with `def call(self, method, http_timeout=30, **params):` 77, one try; `class Data:` 152 with `def fresh(self):` 160, refetched for a newer close and once more after a fetch in the first ten minutes past midnight (160 to 189), 84 requests over `ThreadPoolExecutor(6)`; `def liquidity(coin, now_ms):` 228, `limit=LIQ_DAYS + 1`; `def plan(rep, cs, budget, n, risk, liq):` 239, its rejections and limits (239 to 302); `def serve():` 370 with `log('serving the pinned chat: pid', os.getpid(), …)` (386), the line UNIT-OLD's `log_since` reads; `def probe():` 459; `def main():` 778 — `plan`, `Data`, `liquidity`, `put` and `main` identical to Appendix A's by G-RULE. TZ-35's checker `research/tz35-advisor-deploy.py` — `UUID` (54) and `LIVE_S = 60` (56); `def claude_starts():` 157, `argv[0] == 'claude' or argv[0].endswith('/claude.exe')` (167); `def live_or_earlier(birth, starts):` 274, `s - 1 <= birth <= s + LIVE_S` (276); `def reclaimable(tree):` 279 to 284; `def mode_scratch(own):` 419, the siblings of `own`; `def mode_reclaim(trees):` 434, asserting at 435 and printing `RECLAIM PASS` at 486; `def main(argv):` 774, `scratch` one argument, `reclaim` any, `0` on success and an uncaught `AssertionError`'s `1` otherwise. The unit — `WorkingDirectory` line 12, `ExecStart` 13, `Restart=always` 14, `RestartSec=30` 15, `RestartPreventExitStatus=3 4` 16, `MemoryMax=128M` 18, `ProtectSystem=strict` 21 and `ReadWritePaths=/var/lib/adv3-bot` 22, under which `check-done` and its `.tmp` are written. **Every behaviour this TZ attributes to Appendix A** is the body of one function: `route` 147, `live_report` 212, `ranked` 229, `top_n` 244, `make` 255, `strong_shares` 357, `item_lines` 362, `plan_parts` 386, the schedule 421 to 477, `journal_records` 486, `journal_scan` 501, `append` 512, `base_record` 517, `offers` 528, `alerted` 554, `follow` 568, `forming_candles` 609, `candidates` 623, `alerts_of` 628, `weakened` 648, `zones_left` 666, the message's lines 686 to 792, `compose` 795, `check_record` 823, `check` 844, `serve` 867, `handle` 924 and `probe` 962 of the bot; `changes` 551, `message` 567, `assessment` 628, `trust_lines` 676 and `card_lines` 710 of `adv3.py`; and the checker's readings and modes at the lines C5 names — each sentence of §1 and §4.2 to §4.4 read against them. **Sentences rewritten in this reading:** the "When" and §3.4 gave B-DEPLOY the band 06:35 to 23:40 UTC, so that a deploy at its end met B-KILL's closed band and a paste waited hours — B-DEPLOY's band is now 06:35 to 11:20 and 12:20 to 23:20 UTC, P-BOSS-A's hand-over window; B-KILL's `mark` failing on `daily-sent` had no named outcome — it is now B-ROLLBACK, the unit not signalled (§3.5, §4, §4.4); §0.4 cited map §7 item 131 as "the same or the nearest code", where it says the same code — rewritten, the nearest standing in as at TZ-37, the render re-measured on the bytes sent (fifteen runs) and its host peak modelled at TZ-37's ratio; §1 said 28 STRONG trades "stopped within 11.1 %", where E6's bucket is the stop's distance; §1's sentence on the reach shares read as if the 42's `48 / 28 / 18 %` were the rule's; §1 said the request and allocation records "keep their shape", and a new kind cannot; §1 said every check sends "exactly one message", and a long text goes in parts; §1, §4.2 and §5 called the allocation "one message" — one text; §1's quotation of CANON PART VII was re-set to its guillemets, character for character; §0.0 named two logs no step writes — the rule is now `NN-<step>.log`, with the names the pastes read; §3.3 described the Boss's hand-over of B-RECLAIM-SCRATCH instead of giving it — the one line is written (map §7 item 124); §3.7 said `service.log` names no coin, where its failure lines name the symbol Binance failed to serve; §3.2 listed `RULE-ADV-3.txt` twice among G-RULE's reads; §4.3 named no request path and no header for P-START, which CANON hard rule 14 asks fixed — written, as TZ-35 wrote them; §4.3's G-FIRST now says why its `check-done` reading is exact inside the bands; §4.4's second line is marked the Executor's own read, and UNIT-OLD's and STOPPED's logs are named; §5 counted nineteen negative controls on the render, where there are eighteen, and ten new checks in `selftest-adv3.py`, where there are nine and two changed; §6 quoted TZ-35's `0.1` to `0.2` s as TZ-37's P-START, read `1 h 50 min` against its own `81` minutes, and gave the requests at 12:10 no bound; §0.4's tracked files were `10,700,000` bytes where `du` reads `11,540,664`; §1's "the host's census" now says what TZ-37 named, a census of the host's memory and disk. Every count and hash of this section is that of the bytes sent. |
| **C8** | every cross-reference | Resolved by reading the text referenced. **Map `2026-10-31-c` at `17dc258`:** §0's anchors and its table of 58 rows, 55 / 2 / 1; §1's record of refs (a difference from it is recorded, not blocking, §0.5); §2.5 and §2.6 for the archives' calendar runs at `03:00:20` and `01:30:20` UTC, and §2.6 for `STREAM_FLOOR` `7,300,000,000`; §2.7's record under `/var/lib/adv3-bot/`, the token and chat under `/etc/adv3-bot/`, K-35 and TZ-37's G-RENDER, `13.70` s and `58,953,728` bytes (line 1056); §3's `2,312` files in the forensic store, the two worktrees, the two directories TZ-38 left and the live `238335b9…` (line 1320); §6's rows host identity (line 1686), language — `/root/tz04a-env` on Python 3.12 (1687) — git remote — the push through `gh`'s credential helper (1690) — egress — `fapi.binance.com` answering `451` to the Architect's sessions (1691) — process supervision — system units, the restart policy, a package upgrade restarting the capture units (1709) — memory — `65,490,944` and TZ-37's `58,953,728` against `49,168,384` (1710) — disk (1693), both sandbox limits (1713, 1715) and the harness (1716); §7 items 118 (no file of the work tree printed but by a command the TZ names), 124 (a block handed to the Boss: once its band is open, one line, appended under a `date -u` line), 125 and 129 (a reload re-arming an archive's run), 131 (the floor rule), 132 (no step of the Boss's before `EXECUTE`), 136 (`NRestarts` not a lifetime count — H5 reads hashes), 137 (a memory floor read twice), 138 (ONE paste, a refused block handed over unchanged), 139 and 141 (the header names the sections this row cites — copied there), 140 (a handed-over block holds back only the steps that read what it changes) and 142 (CANON `2026-10-31-c`). **CANON `2026-10-31-c`:** PART VII — the decisions on the Boss's specification of 2026-10-31, quoted in §1 character for character («Decisions on the Boss's specification of 2026-10-31 — TZ-39 builds them; TZ-38's verdict of 2026-10-31 settled the measured ones», «a repeat of 00:10 where it failed», the Boss's «open positions» are "the trades the rule holds on coins whose card offered an entry; the journal says which were offered"), the evidence ladder and its chance of about one in seven, the sizes (0.5 % a trade, 1 % at most, 5 % in all), the market record before any scan beyond the 42, ADV-4 for any change of parameter, and «Уверенность: N/5»; hard rules 2 (NUMBER), 12 and 13 (this section), 14 (P-START, every header, the unit, its restart policy and stop, the bands in the blocks' text, ONE paste) and 15 (§9). The Boss's own text of 2026-10-31 is not quoted: every quotation is CANON's. **Contract:** §1 steps 1 to 4 (§0.0, `fingerprint`), §4.1 (the order of the branch and the report), §4.2 (V13) and §8 (the report's order). **Other artifacts:** `CryptoTZ/TZ-37-capital-allocation.md`, whose §0.1 script, bands, B-DEPLOY, B-KILL, K-37, gates and §0.4 floor rule this TZ adapts, and its report (line 495); `CryptoTZ/TZ-35-advisor-bot.md` §4.1, whose fixed headers §4.3 repeats; TZ-38's report §2.7 and line 322; TZ-35's checker's `scratch` and `reclaim`. **This TZ:** §0.1 to §0.5, §1, §2's items, §3.1 to §3.7, §4.1 to §4.5, §5, §6 and §9, each supporting the sentence that cites it. **None unresolved.** |

**Seven checks could not be performed from this session**, and each is converted into a mechanical condition the Executor evaluates and BLOCKS on, or rolls back on (CANON hard rule 13): the host's own state — free space, memory, units, interpreter, the service copy's and the unit file's hashes, the record — `I host`, §0.3; the live reach of `fapi.binance.com` and `api.telegram.org` under the service's headers — `fapi.binance.com` answers `451` to this session's container, `data.binance.vision` `200` — P-START and G-RENDER, before anything is signalled; the checks on a live day with an exit, a weakening or a STRONG candidate, which depend on the market and on the journal of the day — whenever the live data holds one, G-RENDER walks every offer itself and reads the alerts against its walk, and a disagreement is B-ROLLBACK; when it holds none, G-RENDER reads 22 of 22 with zero alerts, and the alert logic rests on the self-tests' synthetic market and the Architect's render on the archive's candles of the 42 coins (13 offers, an exit by signal and two or three candidates at the signal check, seven forming candles at the fact check, 22 of 22 at each of eight runs); systemd's restart of the unit after a `SIGTERM`, the new process's first check and its message to the Boss's chat — the `sendMessage` path TZ-35 proved, now with `disable_notification` — UNIT-NEW and G-FIRST, a failure B-ROLLBACK; NUMBER on `main` with this file uploaded — `I number` on the clone at `17dc258` reads `FAIL - 1 of 2` by design, and the stand-ins read `PASS - 2 of 2` and `FAIL` with a second file and with a report; TZ-35's `scratch` and `reclaim` against the host's real `/tmp`; and the scheduler firing at 00:10 and 12:10 on the host's own clock — not read by this TZ (§4.5): the self-tests run the schedule over three days minute by minute, and the next TZ's host gate reads the `check` records. **One thing is read and not measured, and nothing blocks on it:** Telegram's rendering of the messages and whether a quiet one stays quiet on the Boss's phone. **Everything else above was performed here** under Python 3.12.3, the host's interpreter: the three self-tests, `53`, `106` and `64` of their own; §0.1's script run against this file — four files, over an empty stage and over a worktree of the clone at `17dc258`, its numstat exact and its refusal over a tree whose files are not the committed ones; the checker's `fingerprint`, `rule` and `number` against the repository, `67 of 67`, `10 of 10` and the designed `FAIL - 1 of 2`; its `host`, `mark`, `copy`, `unit`, `first`, `keep` and `stopped` against stand-ins for systemd, `/proc`, `df`, git and the host's files, through a deploy, a kill, a restart, a rollback, a second kill and a stop; `render` on the archive's candles and on the synthetic market; the table of the map, the constants, the arithmetic and TZ-38's figures independently of the checker; and `pyflakes` over the four files, clean.

---

## Appendix A — the four files, byte for byte

Extracted by §0.1's script; each block's content is its file.

```text file=advisor/adv3.py
#!/usr/bin/env python3
# adv3.py - ADV-3, the Boss's advisor for Binance Futures (CANON PART VII). Standard library only.
# Rule text RULE-ADV-3, SHA-256 ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169, frozen
# 2026-10-28 16:14 UTC before any of its results was computed: ADV-1's rule on the Boss's perpetuals' own
# candles, with a strength ranking (TOP-3, STRONG) whose claim has its own gate. Candles and funding come from
# Binance's archive (data.binance.vision) or live from fapi.binance.com; both give the same closed candles.
# Modes: the message of the latest close (--source fapi, the default, or archive; --json for the report);
# --history PATH, Gate H, Gate S and the display facts re-derived from the archive and read against FACTS (G-HISTORY);
# --compare, the archive's last 14 daily candles against fapi.binance.com's (G-SAME). The bot imports this file.
# Since TZ-39 the message carries no methodology: each card its confidence, the rung of CANON PART VII's evidence ladder,
# and its reach shares without survivorship (PIT); the six ratings and what they rest on are the assessment, «оценка».
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
# Gate H, Gate S and the display facts, read once on the history to the close of 2026-10-27 (RULE-ADV-3); p_up (the
# one-sided p of the daily portfolio R) and top5_share (the five best trades' R over the class's total R) are TZ-36's
# two additions, re-derived by G-HISTORY like the rest
FACTS = {'base': {'trades': 5265, 'wins': 1708, 'mean_R': 0.1576, 'median_days': 3, 'gate_H': 'NOT DISQUALIFIED',
                  'mfe': {1: 0.2325, 2: 0.1297, 3: 0.0819}, 'p_up': 0.0226, 'top5_share': 0.3042},
         'strong': {'trades': 253, 'wins': 83, 'mean_R': 0.5473, 'median_days': 19, 'gate_S': 'NOT DISQUALIFIED',
                    'mfe': {1: 0.4783, 2: 0.2846, 3: 0.1779}, 'p_up': 0.0545, 'top5_share': 1.0093}}
# The ratings' two inputs (TZ-36). RELIABILITY is the rung of CANON PART VII's evidence ladder, 0 to 5 - LADDER below says
# what each holds; 1 = the history on the Boss's 42, in sample and not disqualified. STRONG_JUSTIFIED: True only where the
# STRONG strategy's own forward record read PROVEN. Only a TZ that reads one of PART VII's records moves either.
RELIABILITY, STRONG_JUSTIFIED = 1, False
# TZ-38's figures, measured on Binance's whole USDⓈ-M archive to the close of 2026-10-27 (CryptoReports/TZ-38-adv3-pit-
# validation-report.md, §2.7), in sample, an exploration that moves no rung. The cards quote the reach shares without
# survivorship (E4: the 609 contracts of L, the Boss's 42 among them, an entry only on a day of 10,000,000 USDT median quote
# volume); the ratings quote the rule on the 570 contracts the Boss did not pick (E1, E2) and STRONG's median on 500 random
# lists of 42 (E5) - never what a STRONG trade made on the 42 (CANON PART VII).
PIT = {'base': {'mfe': {1: 0.2318, 2: 0.1257, 3: 0.0759}, 'mean_R_G': 0.0403, 'trades_G': 19002, 'p_G': 0.0735,
                 'contracts_G': 570},
       'strong': {'mfe': {1: 0.4717, 2: 0.2906, 3: 0.1887}, 'p_G': 0.1100, 'mean_R_lists': 0.2195, 'lists': 500,
                  'lists_positive': 0.8600, 'top5_share': 0.9875}}
# CANON PART VII's evidence ladder: for each rung, the card's line and the ratings' sentence.
LADDER = {0: ('направление не публикуется', 'история или форвард дисквалифицировали правило: направление не публикуется'),
          1: ('правило не доказано', 'история на ваших 42 монетах — в выборке, на монетах, выбранных в 2026, — не '
                                     'дисквалифицировала правило; это не подтверждение'),
          2: ('подтверждено вне вашего списка', 'PIT-запись подтвердила: правило зарабатывает на контрактах, которые вы не '
                                                'выбирали, на данных, которых никто не читал'),
          3: ('подтверждено и не опровергнуто', 'PIT-запись подтвердила правило, и год на ваших монетах этого не опроверг'),
          4: ('доказано на ваших монетах', 'форвард доказал правило на монетах, которыми вы торгуете'),
          5: ('доказано и держится', 'форвард доказал правило, и следующий год это подтвердил')}


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


def forward_book(trades, daily, open_pos):
    """One strategy's forward record with its parts apart (TZ-36): the trades opened, the closed ones with the R they
    closed on and the stops among them, the positions still open with the R they hold so far, entry cost included,
    and the total over the days, which is the two parts' sum."""
    return {'days': len(daily), 'opened': len(trades) + len(open_pos), 'closed': len(trades),
            'stops': sum(t['why'] == 'stop' for t in trades), 'open': len(open_pos),
            'closed_R': sum(t['R'] for t in trades), 'open_R': sum(p['R'] for p in open_pos),
            'total_R': sum(daily.values())}


def trust(rep):
    """The Boss's six ratings of 2026-10-31, each a function of recorded facts alone (TZ-36): the system's is
    RELIABILITY; a trade's is the system's, and 0 where its card offers no entry or the mark prices failed; STRONG's
    is STRONG_JUSTIFIED; the data's quality is low while the rule is unproven (RELIABILITY 1 or less), else high where
    the close is the day before the report's, every coin was served and the mark prices came, else medium; the
    expectancy is established only where the rule is proven (RELIABILITY 4 or more)."""
    made = dt.datetime.fromtimestamp(rep['made_at_ms'] / 1000, dt.timezone.utc).date() if rep['made_at_ms'] else None
    fresh = made is not None and rep['close_of'] == str(made - DAY)
    complete = not rep['missing'] and rep['marks_ok']
    return {'system': RELIABILITY, 'strong_justified': STRONG_JUSTIFIED, 'served': len(COINS) - len(rep['missing']),
            'cards': {cd['coin']: RELIABILITY if cd['mode'] != 'none' and rep['marks_ok'] else 0 for cd in rep['cards']},
            'quality': 'low' if RELIABILITY <= 1 else 'high' if fresh and complete else 'medium',
            'fresh': fresh, 'complete': complete, 'expectancy_established': RELIABILITY >= 4}


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
    for x, tr in ((base, base_trades), (strong, s_trades)):
        x['top5_share'] = sum(sorted((t['R'] for t in tr), reverse=True)[:5]) / x['total_R'] if x['total_R'] > 0 else None
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
    b_trades, b_daily, b_open = [], {}, []
    for coin, c in cs.items():
        if not c:
            continue
        tf, df, pf = simulate(c, funds.get(coin, lambda d: 3 * BASE_F), FORWARD_FROM, last)
        b_trades += tf
        b_open += [pf] if pf else []
        for d, x in df.items():
            b_daily[d] = b_daily.get(d, 0.0) + x
    cards = [card(coin, rows[coin], coin in strong, deposit, risk) for coin in top]
    for n, cd in enumerate(cards, 1):
        cd['rank'] = n
    rep = {'rule': RULE, 'close_of': str(last), 'deposit': deposit, 'risk_pct': risk, 'top': top, 'strong': strong,
           'cards': cards, 'rows': rows, 'strong_open': {k: str(v['entry']) for k, v in s_open.items()},
           'forward': {'base': stats(b_trades, b_daily), 'strong': stats(s_trades, s_daily)},
           'book': {'base': forward_book(b_trades, b_daily, b_open),
                    'strong': forward_book(s_trades, s_daily, list(s_open.values()))},
           'missing': [c for c in COINS if c in missing], 'marks_ok': bool(marks), 'made_at_ms': now_ms}
    rep['trust'] = trust(rep)
    return rep


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
    out = {'coin': coin, 'side': k, 'strong': is_strong, 'z': row['z'], 'sum': row.get('sum'), 'close': C, 'U': U,
           'stop': S, 'mark': P,
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


def changes(rep):
    """The day's changes among the coins, each coin's signal at the close against the close before it: ([(coin, side)] new,
    [coin] out of a long, [coin] out of a short, [(coin, side)] reversed)."""
    rows, sides = rep['rows'], (1, -1)
    new, out_long, out_short, flips = [], [], [], []
    for coin in COINS:
        now, before = rows[coin].get('signal'), rows[coin].get('prev')
        if now in sides and before not in sides:
            new.append((coin, now))
        elif now not in sides and before in sides:
            (out_long if before > 0 else out_short).append(coin)
        elif now in sides and before in sides and now != before:
            flips.append((coin, now))
    return new, out_long, out_short, flips


def message(rep, facts, head=(), tail=()):
    """The Boss's message in Russian, as Telegram HTML, from the report and the frozen facts: the close, the day's changes,
    the cards - each with its confidence, the rung of the evidence ladder or 0 where it offers no entry - and the other
    signals; head's lines follow the header and tail's precede the other signals (the bot's events, candidates and the
    trades its cards offered). The methodology, the forward record and the six ratings are the assessment's, «оценка» (TZ-39)."""
    last = dt.date.fromisoformat(rep['close_of'])
    until = last + 2 * DAY
    lines = ['📊 <b>ADV-3 · сигналы Binance Futures</b>',
             f"Закрытие дня {ddmm(rep['close_of'])} (UTC)",
             f"⏱ Действует до 04:00 {until:%d.%m} по Батуми — до следующего закрытия",
             f"Депозит {num(rep['deposit'], 6)} USDT · риск {pct(rep['risk_pct'])}% = "
             f"{num(rep['deposit'] * rep['risk_pct'] / 100, 4)} USDT на сделку · все сделки вместе ≤ {pct(RISK_ALL, 0)}%"]
    if not rep.get('marks_ok', True):
        lines.append('⚠️ Текущие цены Binance недоступны: вход посчитан от цены закрытия')
    if head:
        lines += [''] + list(head)
    lines.append('')
    rows = rep['rows']
    word = {1: 'ЛОНГ', -1: 'ШОРТ'}
    new, out_long, out_short, flips = changes(rep)
    lines.append('<b>Изменения за день</b>')
    if new:
        lines.append('🆕 Новые: ' + ', '.join(f'{coin} {word[k]}' for coin, k in new))
    if out_long or out_short:
        parts = ([', '.join(out_long) + ' из лонга'] if out_long else []) + ([', '.join(out_short) + ' из шорта']
                                                                           if out_short else [])
        lines.append('🚪 Выход: ' + ' · '.join(parts))
    if flips:
        lines.append('🔄 Разворот: ' + ', '.join(f'{coin} в {word[k]}' for coin, k in flips))
    if not (new or out_long or out_short or flips):
        lines.append('Изменений нет.')
    lines.append('')
    shown = [cd['coin'] for cd in rep['cards']]
    if rep['cards']:
        conf = (rep.get('trust') or {}).get('cards') or {}
        lines.append(f"<b>ТОП-{rep.get('n', TOP_N)} по силе тренда</b>")
        for cd in rep['cards']:
            lines += [''] + card_lines(cd, facts, conf.get(cd['coin']))
    else:
        lines.append('<b>Открытых сигналов нет</b> — все монеты вне рынка.')
    if tail:
        lines += [''] + list(tail)
    longs = [c for c in COINS if rows[c].get('signal') == 1 and c not in shown]
    shorts = [c for c in COINS if rows[c].get('signal') == -1 and c not in shown]
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
    lines += ['', '<i>Не инвестиционный совет · «оценка» — на чём держится уверенность</i>']
    return '\n'.join(lines)


def assessment(rep, facts):
    """The «оценка» reply (TZ-39): the rung of the evidence ladder and the next readings, the six ratings, the forward record in
    its parts and what the history says in figures without survivorship - the methodology the pushed messages no longer carry."""
    rung = rep['trust']['system']
    b, s = PIT['base'], PIT['strong']
    lines = ['🧭 <b>ADV-3 · оценка: на чём держится уверенность</b>', f"Закрытие дня {ddmm(rep['close_of'])} (UTC)", '',
             f"Уверенность: <b>{rung}/5</b> — рубеж {rung} из 5 лестницы доказательств: {LADDER[rung][0]}."]
    if rung < 4:
        lines.append('Следующие чтения: форвард правила — после закрытия 28.10.2027; PIT-запись на контрактах, которые вы не '
                     'выбирали, — после закрытия 31.10.2027. Шанс, что они поднимут рейтинг, — не больше примерно 1 из 7 '
                     '[модель]; рейтинг двигает только измерение.')
    lines += [''] + trust_lines(rep, facts)
    bb, bs = rep['book']['base'], rep['book']['strong']
    if bb['days']:
        lines += ['', f"<b>Форвард с 28.10</b> — день {bb['days']} из 365, бумажный портфель правила, не ваш счёт",
                  book_line('Все сигналы', bb), book_line('STRONG', bs)]
        if rep['strong_open']:
            lines.append('Открытые STRONG-сделки правила: ' + html.escape(', '.join(f'{k} с {ddmm(v)}' for k, v in rep['strong_open'].items())))
        lines.append('Доказанность проверяется после 28.10.2027; текущие R ничего не решают.')
    else:
        lines += ['', 'Форвард начинается с закрытия 28.10; доказанность проверяется после 28.10.2027.']
    gates = ''
    if facts:
        ok = facts['base'].get('gate_H') == 'NOT DISQUALIFIED' and facts['strong'].get('gate_S') == 'NOT DISQUALIFIED'
        gates = (' Проверки истории на ваших 42 (Gate H, Gate S): ' + ('не дисквалифицировано — это ничего не подтверждает.'
                                                                       if ok else 'дисквалифицировано.'))
    lines += ['', '<b>История</b> — 2020–2026, в выборке, не доказательство',
              f"Вне вашего списка ({b['contracts_G']} контрактов): правило {signed(b['mean_R_G'])} R на сделку — не решено; STRONG "
              f"на {s['lists']} случайных списках из 42 — медиана {signed(s['mean_R_lists'])} R на сделку. На ваших 42 цифры "
              f"выше: список составлен в 2026, и отбор их завышает.{gates}",
              'Прибыль дают редкие длинные тренды; большинство сделок закрывается небольшим убытком.',
              '', '<i>«Дошли» — доля прошлых сделок того же класса (★ STRONG или обычных) на всех контрактах Binance, без отбора '
                  'выживших, цена которых дошла до цели до выхода. R — результат в единицах риска сделки: −1 R — сработал стоп. '
                  'Не инвестиционный совет: правило показывает состояние рынка; решение и риск — ваши.</i>']
    return '\n'.join(lines)


def signed(x, places=2):
    return f'{x:+.{places}f}'.replace('.', ',').replace('-', '−')


def book_line(name, b):
    """One strategy's forward line: the entries, the closed part and the open part apart, and the total over the market."""
    r = lambda x: ('+' if x > 0 else '') + num(x, 3)
    return (f"{name}: входов {b['opened']} · закрыто {b['closed']} ({r(b['closed_R'])} R) · "
            f"в позиции {b['open']} ({r(b['open_R'])} R) · итого {r(b['total_R'])} R")


def trust_lines(rep, facts):
    """The Boss's six ratings with their reasons (TZ-36; since TZ-39 behind «оценка»). Every figure is a frozen fact, a count of
    this report, a figure of TZ-38's exploration (PIT) or one computed from them; none is what a STRONG trade made on the
    Boss's 42, and nothing here is a judgement of this moment."""
    tr, bb, bs = rep['trust'], rep['book']['base'], rep['book']['strong']
    b, s = PIT['base'], PIT['strong']
    why = (f"; вне вашего списка правило не решено (p {pct(b['p_G'], 2)} на {b['contracts_G']} контрактах); форвард "
           f"{bb['days']} из 365 дн." if tr['system'] <= 1 else f"; форвард {bb['days']} из 365 дн.")
    out = ['<b>Оценка доверия</b>', f"Надёжность системы: <b>{tr['system']}/5</b> — {LADDER[tr['system']][1]}{why}"]
    if tr['cards']:
        out.append('Уверенность в сделках: ' + ' · '.join(f'{c} {v}/5' for c, v in tr['cards'].items())
                   + ' — не выше надёжности системы; 0 — входа нет; правило не даёт вероятности на сделку')
    else:
        out.append('Уверенность в сделках: сделок нет')
    evidence = (f" — вне вашего списка STRONG не решён (p {pct(s['p_G'], 2)}); на {s['lists']} случайных списках из 42 медиана "
                f"{signed(s['mean_R_lists'])} R на сделку, в плюсе {pct(100 * s['lists_positive'], 0)}% списков; пять лучших "
                f"сделок — {pct(100 * s['top5_share'], 0)}% прибыли; форвард: закрыто {bs['closed']} из {bs['opened']}")
    out.append(f"STRONG обоснован: <b>{'да' if tr['strong_justified'] else 'нет'}</b>{evidence}")
    issues = (([] if tr['fresh'] else ['закрытие не вчерашнее']) + ([f"нет данных по {len(rep['missing'])} монетам"]
              if rep['missing'] else []) + ([] if rep['marks_ok'] else ['нет текущих цен Binance']))
    data = ('данные свежие и полные' if not issues else 'данные: ' + ', '.join(issues)) + \
        f" (закрытие {ddmm(rep['close_of'])}, {tr['served']} из {len(COINS)} монет)"
    quality = {'low': 'низкое', 'medium': 'среднее', 'high': 'высокое'}[tr['quality']]
    out.append(f"Качество данных: <b>{quality}</b> — {data}{'' if tr['system'] > 1 else '; правило не проверено'}")
    if tr['expectancy_established']:
        out.append('Ожидаемая R на сделку: берётся из прочитанного форварда')
    else:
        out.append(f"Ожидаемая R на сделку: <b>не установлена</b> — вне вашего списка: правило {signed(b['mean_R_G'])} R на "
                   f"сделку ({b['contracts_G']} контрактов, в выборке); STRONG — медиана {signed(s['mean_R_lists'])} R на "
                   f"{s['lists']} случайных списках из 42; это не прогноз")
    out.append('Инвалидация: у каждой карточки — стоп и смена сигнала')
    return out


def card_lines(cd, facts, confidence=None):
    """One card: a line each for entry, stop, the three targets with the shares of past trades of its class that reached
    them (TZ-38's, without survivorship: PIT), size, basis and invalidation, and - where confidence is given - its
    confidence: the rung of the evidence ladder, or 0 where the card offers no entry or no current price came."""
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
    shares = None
    if facts:
        use_strong = cd['strong'] and facts['strong'].get('gate_S') == 'NOT DISQUALIFIED'
        shares = PIT['strong' if use_strong else 'base']['mfe']
    for n, t in zip((1, 2, 3), cd['targets']):
        move = 100 * (t - ref) / ref
        share = f' · дошли {pct(100 * shares[n], 0)}%' if shares else ''
        out.append(f"🎯 {price(t)} ({'+' if move > 0 else ''}{pct(move)}%){share}")
    if cd['entry'] is not None:
        out.append(f"Объём: {num(cd['qty'])} {cd['coin']} ≈ {usdt(cd['notional'])} USDT · плечо ≤ {cd['leverage']}× изол.")
    if cd.get('sum') is not None and cd.get('rank'):
        out.append(f"Основание: сумма знаков {signed(cd['sum'], 0)} из ±4 · z {signed(cd['z'])} · ранг {cd['rank']} из "
                   f"{cd.get('of', TOP_N)}")
    out.append(f"Инвалидация: {'цена ≤' if cd['side'] > 0 else 'цена ≥'} {price(cd['stop'])} или закрытие дня с суммой "
               f"знаков {'ниже +2' if cd['side'] > 0 else 'выше −2'}")
    extra = []
    if cd['since']:
        extra.append(f"Сигнал с {ddmm(cd['since'])}")
    if cd['funding'] is not None:
        period = f"/{cd['funding_h']} ч" if cd.get('funding_h') else ' за период'
        extra.append(f"фандинг {'+' if cd['funding'] >= 0 else ''}{pct(100 * cd['funding'], 3)}%{period}")
    if extra:
        out.append(' · '.join(extra))
    if confidence is not None:
        why = ('входа нет' if cd['mode'] == 'none' else LADDER[RELIABILITY][0] if confidence or not RELIABILITY
               else 'нет текущей цены Binance')
        out.append(f"Уверенность: <b>{confidence}/5</b> — {why}")
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
    """G-HISTORY: each frozen fact against the history just derived - counts and verdicts exact, shares, mean R, p and
    the top-5 share at FACTS' four decimals. {name: (equal, derived, FACTS)}."""
    out = {}
    for k in ('base', 'strong'):
        f, x = FACTS[k], h[k]
        out[f'{k} trades'] = (x['trades'] == f['trades'], x['trades'], f['trades'])
        out[f'{k} wins'] = (x['wins'] == f['wins'], x['wins'], f['wins'])
        out[f'{k} mean R'] = (round(x['mean_R'], 4) == f['mean_R'], x['mean_R'], f['mean_R'])
        out[f'{k} median days'] = (x['median_days'] == f['median_days'], x['median_days'], f['median_days'])
        out[f'{k} p'] = (round(x['p_up'], 4) == f['p_up'], x['p_up'], f['p_up'])
        t5 = x['top5_share']
        out[f'{k} top-5 share'] = (t5 is not None and round(t5, 4) == f['top5_share'], t5, f['top5_share'])
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

```text file=advisor/adv3-bot.py
#!/usr/bin/env python3
# adv3-bot.py - ADV-3's Telegram side (CANON PART VII): the Boss's commands; two checks a day by the unit's own scheduler, at
# 00:10 UTC (04:10 in Batumi) the close's signals and at 12:10 UTC (16:10) the facts of the moment - the stops of the trades the
# cards offered, the entry zones, the STRONG candidates - each loud only for an alert and one quiet line where it finds nothing;
# and a journal of every check's state and every message sent. Standard library only; adv3.py lies beside it.
# Modes: --serve (the unit's), --probe, --find-chat, --hello, --selftest.
# Exits: 0 or SIGTERM, restarted by systemd; 3 without a token or a chat id and 4 where glibc refuses its two
# settings, neither restarted; 1, an unexpected exception, restarted.
import argparse, ctypes, datetime as dt, html, json, math, os, re, sys, time, traceback, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import adv3  # noqa: E402

TOKEN_FILE = '/etc/adv3-bot/token'
CHAT_FILE = '/etc/adv3-bot/chat-id'
STATE = '/var/lib/adv3-bot'
TG = 'https://api.telegram.org/bot{token}/{method}'
UA = 'adv3-bot/1'
# TZ-39's two checks a day (CANON PART VII). The rule changes state only at a daily close: the check of 00:10 UTC reads the close's
# signals, ten minutes after it - the margin kept for the day's last funding settlement; the check of 12:10 reads facts alone and
# never a signal of a half-formed candle.
SLOTS = (('signal', dt.time(0, 10)), ('fact', dt.time(12, 10)))
BATUMI = dt.timedelta(hours=4)
POLL, RETRY, LIMIT = 50, 300, 4000
OPEN = ('сигнал', 'сигналы', 'signal', 'signals', 'топ', 'top', 'стратегия', 'стратегию', 'strategy')
ASSESS = ('оценка', 'оценки', 'оценку', 'rating')
HEAD = re.compile(r'^\s*/?([^\W\d_]+)')
TOPN = re.compile(r'(?:топ|top)[\s\-\u2013]*(\d{1,2})(?!\d)', re.I)
# The allocation view (TZ-37): the stop's limit in percent of the entry - the Boss's 14 % since TZ-39 - the smallest position, the
# share of a coin's mean daily quote volume a position may take, the discount for same-way correlation, the strength's cap, the
# days of volume.
STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, CROWD, Z_CAP, LIQ_DAYS = 14.0, 5.0, 0.001, 0.5, 3.0, 7
LIST_MAX = 7   # the longest list «сигнал топ N» shows; STRONG stays a label of the TOP-3
SIDE, DOT = {1: 'LONG', -1: 'SHORT'}, {1: '🟢', -1: '🔴'}
FOOTER = '<i>Не инвестиционный совет · «оценка» — на чём держится уверенность</i>'
HELP = ('<b>ADV-3 · сигналы Binance Futures</b>\n'
        '«сигнал» — ТОП-3 правила сейчас: вход, стоп, цели и размер при депозите 10 000 USDT и риске 0,5% на сделку.\n'
        '«сигнал топ 7» — то же для семи сильнейших, от 1 до 7; ★ STRONG бывает только в ТОП-3.\n'
        '«сигнал 10000 топ 3» — распределить 10 000 USDT между сделками STRONG со стопом не дальше 14% входа; подошло меньше — '
        'покажу меньше, ни одной — скажу. Риск — 0,5% бюджета на сделку, не больше 1%: «сигнал 10000 топ 3 1». Чего нельзя '
        'разместить без превышения риска, остаётся свободным.\n'
        '«оценка» — шесть оценок доверия и на чём они держатся.\n'
        'Проверки — в 04:10 и 16:10 по Батуми: в 04:10 сигналы закрытия дня, в 16:10 стопы и зоны входа. Со звуком — только '
        'когда задет стоп сделки, которую предлагала карточка, её сигнал закончился или появился новый STRONG, проходящий '
        'лимиты; остальное приходит тихо, а проверка без событий — одной строкой.')


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

    def send(self, text, quiet=False):
        """The text as HTML, in parts of at most LIMIT characters; a part Telegram cannot parse goes as plain text. quiet sends
        every part without a notification (the Bot API's disable_notification)."""
        ids, extra = [], ({'disable_notification': True} if quiet else {})
        for part in chunks(text):
            try:
                ids.append(self.call('sendMessage', chat_id=self.chat, text=part, parse_mode='HTML',
                                     disable_web_page_preview=True, **extra)['message_id'])
            except RuntimeError as e:
                if 'parse entities' not in str(e):
                    raise
                plain = html.unescape(re.sub(r'</?[bi]>', '', part))
                ids.append(self.call('sendMessage', chat_id=self.chat, text=plain,
                                     disable_web_page_preview=True, **extra)['message_id'])
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


def numbers(text):
    """(budget, risk) from the numbers in text: the first of 100 or more is the budget, None where there is none, the
    first below 100 the risk in percent, at least 0.05 and at most the rule's 1; 15 000 reads 15000, and 10k, 10к and 10 тыс
    read 10000."""
    text = re.sub(r'(?<=\d)[ \u00a0\u202f](?=\d{3}(?!\d))', '', text)
    text = re.sub(r'(\d+(?:[.,]\d+)?)[ \u00a0]?(?:тыс\.?|[кk])(?![^\W\d_])',
                  lambda m: f"{float(m.group(1).replace(',', '.')) * 1000:.0f}", text, flags=re.I)
    nums = [float(x.replace(',', '.')) for x in re.findall(r'\d+(?:[.,]\d+)?', text)]
    budget = next((x for x in nums if x >= 100), None)
    small = [x for x in nums if x < 100]
    risk = small[0] if small else adv3.RISK
    return (None if budget is None else min(budget, 10_000_000.0)), min(max(risk, 0.05), adv3.RISK_MAX)


def route(text):
    """('signal', None, n, risk) for «сигнал [топ N] [risk]», the rule's first n coins - n read after «топ» or «top», 1 to
    LIST_MAX, default TOP_N; ('alloc', budget, n, risk) where a budget of 100 or more is given - «сигнал 10000 топ 3», «сигнал
    15000 топ 5», «сигнал 10000», «топ 3 на 10000» - the allocation view, n likewise; ('assess', None, None, None) for «оценка»;
    None where the text is none of them. risk is the percent of the deposit or budget a trade may lose at its stop (default
    0.5, at most 1)."""
    text = text or ''
    m = HEAD.match(text)
    if not m:
        return None
    word = m.group(1).lower()
    if word in ASSESS:
        return ('assess', None, None, None)
    if word not in OPEN:
        return None
    s = re.sub(r'@\w+', ' ', text)
    top = TOPN.search(s)
    n = adv3.TOP_N
    if top:
        n = min(max(int(top.group(1)), 1), LIST_MAX)
        s = s[:top.start()] + ' ' + s[top.end():]
    budget, risk = numbers(s)
    return ('signal', None, n, risk) if budget is None else ('alloc', budget, n, risk)


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


def top_n(rep, n):
    """The report with the cards of the rule's first n coins: the TOP-3's own cards, then adv3.card for the rest at the report's
    deposit and risk, STRONG only within the TOP-3; each card its rank of n; the ratings recomputed over them."""
    have = {cd['coin']: cd for cd in rep['cards']}
    cards = [have.get(coin) or adv3.card(coin, rep['rows'][coin], False, rep['deposit'], rep['risk_pct'])
             for coin in ranked(rep)[:n]]
    out = dict(rep, cards=[dict(cd, rank=k, of=n) for k, cd in enumerate(cards, 1)], n=n)
    out['trust'] = adv3.trust(out)
    return out


def make(data, deposit, risk, n=adv3.TOP_N):
    """The report of the rule's first n coins and its message at this moment."""
    rep = top_n(live_report(data, deposit, risk), n)
    return rep, adv3.message(rep, adv3.FACTS)


def returns_of(c, last, days=adv3.VOL_DAYS):
    """{day: log return} of one coin's last `days` closed days up to last."""
    ds = sorted(d for d in c if d <= last)[-(days + 1):]
    return {ds[k]: math.log(c[ds[k]][3] / c[ds[k - 1]][3]) for k in range(1, len(ds))}


def correlation(a, b):
    """Pearson correlation of two {day: return} series on their common days; None below 30 days or for a flat series."""
    days = sorted(set(a) & set(b))
    if len(days) < 30:
        return None
    x, y = [a[d] for d in days], [b[d] for d in days]
    mx, my = sum(x) / len(x), sum(y) / len(y)
    sxx, syy = sum((u - mx) ** 2 for u in x), sum((v - my) ** 2 for v in y)
    if sxx <= 0 or syy <= 0:
        return None
    return sum((u - mx) * (v - my) for u, v in zip(x, y)) / math.sqrt(sxx * syy)


def liquidity(coin, now_ms):
    """The mean quote volume in USDT of the coin's last LIQ_DAYS closed days, from fapi.binance.com, or None."""
    try:
        rows = adv3.fapi('/fapi/v1/klines', symbol=coin + 'USDT', interval='1d', limit=LIQ_DAYS + 1)
        vols = [float(r[7]) for r in rows if int(r[6]) < now_ms][-LIQ_DAYS:]
        return sum(vols) / len(vols) if vols else None
    except Exception as e:
        log('liquidity failed:', coin, repr(e)[:200])
        return None


def plan(rep, cs, budget, n, risk, liq):
    """TZ-37's allocation of one report. Qualifying: a STRONG coin of the report, current prices served, an entry, a stop no
    farther than STOP_MAX percent of the entry, among the first n by rank; a weaker setup never fills a place. Each qualifying
    trade's share is its strength (at most Z_CAP) discounted by CROWD times its mean same-way correlation with the others
    (an unknown correlation counts as 1); its loss at the stop, costs of both sides included, is k * risk percent of the
    budget times the share, at most the rule's RISK_MAX, and all together at most RISK_ALL; its position is that loss over
    (stop + 2 * COST), at most LIQ_FRAC of the coin's mean daily volume where known, the whole at most the budget, in whole
    USDT rounded down; below MIN_NOTIONAL it is dropped. Leverage is the rule's; margin and loss round up."""
    last = dt.date.fromisoformat(rep['close_of'])
    cards, rejected = [], []
    for coin in [c for c in rep['top'] if c in rep['strong']]:
        cd = adv3.card(coin, rep['rows'][coin], True, budget, risk)
        side = 'LONG' if cd['side'] > 0 else 'SHORT'
        if not rep['marks_ok']:
            rejected.append((coin, side, 'нет текущей цены Binance'))
        elif cd['mode'] == 'none':
            rejected.append((coin, side, 'цена у стопа, входа нет'))
        elif cd['stop_pct'] > STOP_MAX:
            rejected.append((coin, side, f"стоп {adv3.pct(cd['stop_pct'])}% дальше {adv3.pct(STOP_MAX)}%"))
        elif len(cards) >= n:
            rejected.append((coin, side, f'сверх запрошенных {n}'))
        else:
            cards.append(cd)
    k = len(cards)
    rate = [cd['stop_pct'] / 100 + 2 * adv3.COST for cd in cards]
    items, rho = [], {}
    if k:
        ret = {cd['coin']: returns_of(cs[cd['coin']], last) for cd in cards}
        for a in range(k):
            for b in range(a + 1, k):
                rho[a, b] = rho[b, a] = correlation(ret[cards[a]['coin']], ret[cards[b]['coin']])
        kap = [[(1.0 if rho.get((a, b)) is None else rho[a, b]) * cards[a]['side'] * cards[b]['side'] for b in range(k)] for a in range(k)]
        crowd = [max(0.0, sum(kap[a][b] for b in range(k) if b != a) / (k - 1)) if k > 1 else 0.0 for a in range(k)]
        q = [min(abs(cd['z']), Z_CAP) for cd in cards]
        w = [q[a] / sum(q) * (1 - CROWD * crowd[a]) for a in range(k)]
        share = [x / sum(w) for x in w]
        pct_ = [min(adv3.RISK_MAX, k * risk * share[a]) for a in range(k)]
        if sum(pct_) > adv3.RISK_ALL:
            pct_ = [x * adv3.RISK_ALL / sum(pct_) for x in pct_]
        raw, capped = [], []
        for a, cd in enumerate(cards):
            r = pct_[a] / 100 * budget / rate[a]
            v = liq.get(cd['coin'])
            capped.append(bool(v) and r > LIQ_FRAC * v)
            raw.append(min(r, LIQ_FRAC * v) if v else r)
        scaled = sum(raw) > budget
        if scaled:
            raw = [x * budget / sum(raw) for x in raw]
        for a, cd in enumerate(cards):
            notional = math.floor(raw[a])
            if notional < MIN_NOTIONAL:
                rejected.append((cd['coin'], 'LONG' if cd['side'] > 0 else 'SHORT', f'позиция меньше {adv3.num(MIN_NOTIONAL, 2)} USDT'))
                continue
            items.append({'card': cd, 'notional': notional, 'leverage': cd['leverage'], 'margin': math.ceil(notional / cd['leverage']),
                          'loss': math.ceil(notional * rate[a] - 1e-9), 'loss_exact': notional * rate[a], 'risk_pct': pct_[a],
                          'share': share[a], 'crowd': crowd[a], 'capped': capped[a], 'rank': 0})
        for number, it in enumerate(items, 1):
            it['rank'] = number
    allocated = sum(it['notional'] for it in items)
    return {'budget': budget, 'n': n, 'risk': risk, 'items': items, 'rejected': rejected, 'k': k,
            'plain': [c for c in rep['top'] if c not in rep['strong']], 'allocated': allocated, 'free': budget - allocated,
            'margin': sum(it['margin'] for it in items), 'loss': sum(it['loss'] for it in items),
            'loss_exact': sum(it['loss_exact'] for it in items), 'avg_trade': budget * risk / 100, 'cap_trade': budget * adv3.RISK_MAX / 100,
            'cap_all': budget * adv3.RISK_ALL / 100}


def strong_shares():
    """The reach shares a STRONG trade's targets carry: TZ-38's STRONG shares where Gate S stands, else the rule's (adv3.PIT)."""
    return adv3.PIT['strong' if adv3.FACTS['strong'].get('gate_S') == 'NOT DISQUALIFIED' else 'base']['mfe']


def item_lines(it, k, number=None):
    """One placed trade of an allocation: direction and quality, entry, stop, targets with their shares, capital, leverage, margin,
    loss at the stop, invalidation, and its confidence with the note that the sizes are the Architect's formula, unproven."""
    usdt, pct, price = adv3.usdt, adv3.pct, adv3.price
    cd, mfe = it['card'], strong_shares()
    lo, hi = cd['zone']
    ref = cd['entry']
    conf = adv3.RELIABILITY if cd['mode'] != 'none' else 0
    lines = [f"{f'{number}) ' if number else ''}{DOT[cd['side']]} <b>{cd['coin']} · {SIDE[cd['side']]}</b> · ★ STRONG",
             f"Качество: z {adv3.signed(cd['z'])} · сумма знаков {adv3.signed(cd['sum'], 0)} из ±4 · доля {pct(100 * it['share'], 0)}%"
             + (f" · корреляция с остальными {adv3.signed(it['crowd'])}" if k > 1 else ''),
             (f"Вход: <b>по рынку</b> ≈ {price(ref)}, зона {price(lo)}–{price(hi)}" if cd['mode'] == 'market'
              else f"Вход: <b>лимит {price(ref)}</b> — ждать отката, цена {price(cd['mark'])} ушла от зоны"),
             f"⛔ Стоп: <b>{price(cd['stop'])}</b> ({'−' if cd['side'] > 0 else '+'}{pct(cd['stop_pct'])}%)"]
    for n, t in zip((1, 2, 3), cd['targets']):
        lines.append(f"🎯 {price(t)} ({'+' if (t - ref) > 0 else ''}{pct(100 * (t - ref) / ref)}%) · дошли {pct(100 * mfe[n], 0)}%")
    lines += [f"Капитал: <b>{usdt(it['notional'])} USDT</b>{' (ограничен ликвидностью)' if it['capped'] else ''} · плечо {it['leverage']}× изол. · маржа {usdt(it['margin'])} USDT",
              f"Потеря на стопе: {usdt(it['loss'])} USDT с комиссиями",
              f"Инвалидация: {'цена ≤' if cd['side'] > 0 else 'цена ≥'} {price(cd['stop'])} или закрытие дня с суммой знаков "
              f"{'ниже +2' if cd['side'] > 0 else 'выше −2'}",
              f"Уверенность: <b>{conf}/5</b> — {adv3.LADDER[adv3.RELIABILITY][0]} · размеры — формула Архитектора, не доказана"]
    return lines


def plan_parts(rep, p):
    """The allocation view as one message: the budget and the limits in money, the result, each placed trade, the rejected and the
    weaker named, and the note that the sizes are unproven. The six ratings are the assessment's, «оценка» (TZ-39)."""
    last = dt.date.fromisoformat(rep['close_of'])
    usdt, pct, num = adv3.usdt, adv3.pct, adv3.num
    lines = ['💼 <b>ADV-3 · распределение капитала</b>', f"Закрытие дня {adv3.ddmm(rep['close_of'])} (UTC) · действует до 04:00 {last + 2 * adv3.DAY:%d.%m} по Батуми",
             f"Бюджет {num(p['budget'], 6)} USDT · до {p['n']} {adv3.plural(p['n'], 'сделки', 'сделок', 'сделок')} · только STRONG, стоп не дальше {pct(STOP_MAX)}% входа",
             f"Риск на стопе: в среднем {pct(p['risk'])}% бюджета на сделку ({usdt(p['avg_trade'])} USDT), у сильнейшей не больше {pct(adv3.RISK_MAX, 0)}% "
             f"({usdt(p['cap_trade'])} USDT), на все не больше {pct(adv3.RISK_ALL, 0)}% ({usdt(p['cap_all'])} USDT)"]
    if not rep['marks_ok']:
        lines.append('⚠️ Текущие цены Binance недоступны: вход и размер не определены, ничего не распределяю')
    lines += ['', '<b>Итог</b>']
    if p['items']:
        lines += [f"Подходящих сделок: {len(p['items'])} из {p['n']} запрошенных",
                  f"Размещено {usdt(p['allocated'])} USDT · маржа {usdt(p['margin'])} USDT",
                  f"Потеря на стопах {usdt(p['loss'])} USDT = {pct(100 * p['loss'] / p['budget'], 2)}% бюджета",
                  f"Свободно {usdt(p['free'])} USDT — больше без превышения лимитов риска не разместить: размер сделки = допустимая потеря "
                  f"на её стопе / расстояние до стопа"]
    else:
        lines += ['Подходящих сделок нет — ничего не размещаю', f"Размещено 0 USDT · свободно {usdt(p['budget'])} USDT"]
    for it in p['items']:
        lines += [''] + item_lines(it, p['k'], it['rank'])
    if p['rejected']:
        lines += ['', 'Отклонены: ' + '; '.join(f'{c} {s} — {why}' for c, s, why in p['rejected'])]
    if p['plain']:
        lines.append('В ТОП-3 без STRONG — не берутся: ' + ', '.join(p['plain']))
    if p['n'] > adv3.TOP_N:
        lines.append(f'STRONG бывает только в ТОП-3: больше {adv3.TOP_N} сделок не будет')
    lines += ['', 'Размеры — формула Архитектора (сила тренда, поправка на корреляцию, ликвидность, лимиты риска), не доказанная: '
                  'форвард-запись проверяет правило, а не этот отбор и не эти размеры.', FOOTER]
    return ['\n'.join(lines)]


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
    check and that day's signal check is not done, the signal check - 12:10 repeats 00:10 where it failed."""
    last = latest_slot(now)
    if done is not None and slot_key(done) >= slot_key(last):
        return None
    if last[1] == 'fact' and (done is None or slot_key(done) < slot_key((last[0], 'signal'))):
        return last[0], 'signal'
    return last


def done_after(slot, now):
    """What a check marks done: itself, or - a signal check that ends at or after its day's 12:10 - that day's fact check too."""
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


# ---- the journal and the trades the cards offered -----------------------------------------------------------------

CARD_KEYS = ('coin', 'side', 'strong', 'mode', 'entry', 'stop', 'targets', 'close', 'U', 'since', 'rank', 'of')


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


def journal_scan():
    """(offers, alerted, the last check record) of the journal, in one pass that keeps those three alone."""
    offs, done, prev = {}, set(), None
    for rec in journal_records():
        offers((rec,), offs)
        done |= alerted((rec,))
        if rec.get('kind') == 'check':
            prev = rec
    return offs, done, prev


def append(rec):
    with open(os.path.join(STATE, 'journal.jsonl'), 'a', encoding='utf-8') as f:
        f.write(json.dumps(rec, ensure_ascii=False, default=str) + '\n')


def base_record(kind, rep, ids, cards=None, at=None):
    """A journal record: its instant, kind, rule, close, deposit, risk, TOP-3, STRONG, message ids, every coin's signal, and the
    cards the message offered (the report's, unless cards names others), each with its confidence."""
    cards = rep['cards'] if cards is None else cards
    conf = adv3.trust(dict(rep, cards=cards))['cards']
    return {'utc': (at or dt.datetime.now(dt.timezone.utc)).isoformat(timespec='seconds'), 'kind': kind, 'rule': rep['rule'],
            'close_of': rep['close_of'], 'deposit': rep['deposit'], 'risk_pct': rep['risk_pct'], 'top': rep['top'],
            'strong': rep['strong'], 'message_ids': ids, 'signals': {k: v.get('signal') for k, v in rep['rows'].items()},
            'cards': [dict({k: cd.get(k) for k in CARD_KEYS}, confidence=conf.get(cd['coin'])) for cd in cards]}


def offers(records, out=None):
    """The trades the bot's cards offered (TZ-39): every card a journal record carries whose entry was offered - at market or
    as a limit - keyed by its coin, side and the close it was made from, the first record's kept; of an allocation record only
    the coins its plan placed (TZ-37's records carry the report's cards beside the plan). {key: offer}, in the records' order,
    added to out where it is given."""
    out = {} if out is None else out
    for rec in records:
        close_of = rec.get('close_of')
        placed = None
        if rec.get('kind') == 'alloc' and isinstance(rec.get('alloc'), dict):
            placed = {i.get('coin') for i in rec['alloc'].get('items') or [] if isinstance(i, dict)}
        for cd in rec.get('cards') or []:
            try:
                if cd.get('mode') not in ('market', 'limit') or (placed is not None and cd['coin'] not in placed):
                    continue
                side, C, U = int(cd['side']), float(cd['close']), float(cd['U'])
                dt.date.fromisoformat(close_of)
                key = (cd['coin'], side, close_of)
                if cd['coin'] in adv3.COINS and side in (1, -1) and U > 0 and key not in out:
                    out[key] = {'coin': cd['coin'], 'side': side, 'close_of': close_of, 'close': C, 'U': U, 'stop': C - side * U,
                                'mode': cd['mode'], 'first': rec.get('utc')}
            except (AttributeError, KeyError, TypeError, ValueError):
                continue
    return out


def alerted(records):
    """{(coin, side, close_of, kind)} of every alert a check record holds: each alert is sent once."""
    out = set()
    for rec in records:
        if rec.get('kind') != 'check':
            continue
        for a in rec.get('alerts') or []:
            try:
                out.add((a['coin'], int(a['side']), a.get('close_of'), a['kind']))
            except (KeyError, TypeError, ValueError):
                pass
    return out


def follow(offs, cs, funds, last, forming=None, done=frozenset()):
    """Each offered trade held by the rule's own functions from the day after its close to the close of last - adv3.open_at at the
    card's close and unit, adv3.hold for its stop inside a day, adv3.signal for its end at a close and adv3.close_at for that exit -
    then, where forming holds the coin's candle of the day after last, whether that candle has reached the stop. An offer whose
    stop or signal alert was sent is closed and not held again. [{key, coin, side, close_of, close, U, stop, state, day, price, R}],
    state 'open', 'stop', 'signal', 'touch' (the forming candle), 'closed' or 'unknown' (no candle of its close)."""
    out = []
    for key, off in offs.items():
        coin, side, close_of = key
        f = dict(off, key=key, state='open', day=None, price=None, R=None)
        if (coin, side, close_of, 'stop') in done or (coin, side, close_of, 'signal') in done:
            out.append(dict(f, state='closed'))
            continue
        c = cs.get(coin) or {}
        D = dt.date.fromisoformat(close_of)
        if D not in c or D > last:
            out.append(dict(f, state='unknown'))
            continue
        days = sorted(d for d in c if d <= last)
        closes = [c[d][3] for d in days]
        pos = adv3.open_at(side, off['close'], off['U'], D)
        fund = funds.get(coin) or (lambda d: 3 * adv3.BASE_F)
        for i in range(days.index(D) + 1, len(days)):
            d = days[i]
            _, stopped = adv3.hold(pos, c[d], closes[i - 1], fund(d), d)
            if stopped:
                f.update(state='stop', day=str(d), price=pos['X'])
                break
            if adv3.signal(days, closes, i) != side:
                adv3.close_at(pos, closes[i], d)
                f.update(state='signal', day=str(d), price=closes[i])
                break
        f['R'] = pos['R']
        if f['state'] == 'open' and forming and forming.get(coin):
            _o, h, l, _c = forming[coin]
            if (l <= pos['S']) if side > 0 else (h >= pos['S']):
                f.update(state='touch', day=str(last + adv3.DAY), price=l if side > 0 else h)
        out.append(f)
    return out


def forming_candles(coins, day):
    """{coin: (open, high, low, last)} of each coin's daily candle that opened at day's 00:00 UTC, from fapi.binance.com - the
    candle the fact check reads the stops in, never a signal; a coin whose candle fails or is not served is left out."""
    out = {}
    for coin in coins:
        try:
            for r in adv3.fapi('/fapi/v1/klines', symbol=coin + 'USDT', interval='1d', limit=2):
                if adv3.ms_day(r[0]) == day:
                    out[coin] = (float(r[1]), float(r[2]), float(r[3]), float(r[4]))
        except Exception as e:
            log('forming candle failed:', coin, repr(e)[:200])
    return out


def candidates(p):
    """The STRONG coins an allocation places, as (coin, side): those that pass its limits."""
    return [(it['card']['coin'], it['card']['side']) for it in p['items']]


def alerts_of(fol, passing, prev_passing, done, rep, p):
    """The check's alerts, each with the price it fired at against the close it rests on: a followed trade stopped - by a closed
    candle or the forming one - or ended by its signal at a close, each once; and every STRONG candidate the allocation places
    now that it did not place at the check before."""
    out = []
    for f in fol:
        kind = {'stop': 'stop', 'touch': 'stop', 'signal': 'signal'}.get(f['state'])
        if kind and (f['coin'], f['side'], f['close_of'], kind) not in done:
            out.append({'kind': kind, 'coin': f['coin'], 'side': f['side'], 'close_of': f['close_of'], 'close': f['close'],
                        'level': f['stop'] if kind == 'stop' else f['price'], 'price': f['price'], 'day': f['day'],
                        'touch': f['state'] == 'touch', 'mark': (rep['rows'].get(f['coin']) or {}).get('mark')})
    placed = {(it['card']['coin'], it['card']['side']): it['card'] for it in p['items']}
    for coin, side in passing:
        if (coin, side) not in prev_passing:
            cd = placed[coin, side]
            out.append({'kind': 'candidate', 'coin': coin, 'side': side, 'close_of': rep['close_of'], 'close': cd['close'],
                        'level': cd['stop'], 'price': cd['entry'], 'day': None, 'touch': False, 'mark': cd['mark']})
    return out


def weakened(fol, rep, cs):
    """The trades the cards offered, open by the rule, whose coin's sum of signs fell from ±4 at the close before to ±2 at this
    close with the signal kept - shown as information and never as an exit (CANON PART VII): [(coin, side)], the coins' order.
    The close before's sum is adv3.strength's."""
    last = dt.date.fromisoformat(rep['close_of'])
    out = []
    for coin, side in sorted({(f['coin'], f['side']) for f in fol if f['state'] == 'open'}, key=lambda x: (adv3.COINS.index(x[0]), -x[1])):
        row = rep['rows'].get(coin) or {}
        c = cs.get(coin) or {}
        days = sorted(d for d in c if d <= last)
        if row.get('signal') != side or row.get('sum') != 2 * side or len(days) < 2 or days[-1] != last:
            continue
        st = adv3.strength(days, [c[d][3] for d in days], len(days) - 2)
        if st and st[1] == 4 * side:
            out.append((coin, side))
    return out


def zones_left(rep, offs, fol):
    """The entries this close's cards offered at market that the price of the moment has left - each card made again from the
    report's row at the current mark: a limit where the price ran past the zone, none where it stands near the stop. Only
    trades still open by the rule are read."""
    open_ = {f['key'] for f in fol if f['state'] == 'open'}
    out = []
    for key, off in offs.items():
        row = rep['rows'].get(off['coin']) or {}
        if (off['close_of'] != rep['close_of'] or off['mode'] != 'market' or key not in open_ or not rep['marks_ok']
                or row.get('signal') != off['side']):
            continue
        cd = adv3.card(off['coin'], row, False, rep['deposit'], rep['risk_pct'])
        if cd['mode'] != 'market':
            out.append({'coin': off['coin'], 'side': off['side'], 'mode': cd['mode'], 'mark': cd['mark'], 'zone': list(cd['zone']),
                        'entry': cd['entry'], 'stop': cd['stop']})
    return out


# ---- a check's message --------------------------------------------------------------------------------------------

def event_lines(al, p, fact=False):
    """The alerts as lines: stops, then signal exits by coin, side and close, then STRONG candidates - at the fact check each
    with its entry plan, at the signal check pointing to the candidates below."""
    if not al:
        return []
    price, ddmm = adv3.price, adv3.ddmm
    lines = ['🔔 <b>События</b>']
    for a in al:
        if a['kind'] == 'stop':
            when = (f"сегодня ({'минимум' if a['side'] > 0 else 'максимум'} дня {price(a['price'])})" if a['touch']
                    else ddmm(a['day']))
            lines.append(f"⛔ {a['coin']} {SIDE[a['side']]}, карточка {ddmm(a['close_of'])}: стоп {price(a['level'])} задет "
                         f"{when} — по правилу сделка закрыта по стопу")
    exits = {}
    for a in al:
        if a['kind'] == 'signal':
            exits.setdefault((a['coin'], a['side'], a['day']), []).append(a)
    for (coin, side, day), group in exits.items():
        cards = ', '.join(ddmm(a['close_of']) for a in group)
        mark = group[0]['mark']
        lines.append(f"🚪 {coin} {SIDE[side]}, {'карточка' if len(group) == 1 else 'карточки'} {cards}: сигнал закончился на "
                     f"закрытии {ddmm(day)} — по правилу выход по закрытию {price(group[0]['level'])}"
                     + (f"; сейчас {price(mark)}" if mark else ''))
    placed = {(it['card']['coin'], it['card']['side']): it for it in p['items']}
    for a in al:
        if a['kind'] == 'candidate':
            if fact:
                lines += [f"🆕 STRONG {a['coin']} {SIDE[a['side']]} теперь проходит лимиты распределения ({adv3.num(p['budget'], 6)} "
                          f"USDT, риск {adv3.pct(p['risk'])}%):"] + item_lines(placed[a['coin'], a['side']], p['k'])
            else:
                lines.append(f"🆕 STRONG: {a['coin']} {SIDE[a['side']]} проходит лимиты распределения — план ниже")
    return lines


def candidate_lines(rep, p, new):
    """The close's STRONG candidates at the default budget: each placed one with its capital, leverage, margin and loss at the
    stop, each other named with its reason; 🆕 marks a candidate the check before did not place."""
    strong = [c for c in rep['top'] if c in rep['strong']]
    if not strong:
        return ['<b>STRONG-кандидатов нет</b>']
    usdt = adv3.usdt
    lines = [f"<b>STRONG-кандидаты</b> — распределение {adv3.num(p['budget'], 6)} USDT, риск {adv3.pct(p['risk'])}%, стоп не "
             f"дальше {adv3.pct(STOP_MAX, 0)}%"]
    placed = {it['card']['coin']: it for it in p['items']}
    why = {c: r for c, _s, r in p['rejected']}
    for coin in strong:
        side = rep['rows'][coin]['signal']
        if coin in placed:
            it = placed[coin]
            lines.append(f"{'🆕 ' if (coin, side) in new else ''}{coin} {SIDE[side]} — проходит: капитал {usdt(it['notional'])} USDT · "
                         f"плечо {it['leverage']}× изол. · маржа {usdt(it['margin'])} USDT · потеря на стопе {usdt(it['loss'])} USDT")
        else:
            lines.append(f"{coin} {SIDE[side]} — не проходит: {why.get(coin, 'вне распределения')}")
    return lines


def followed_lines(fol):
    """The trades the cards offered that are open by the rule, by coin and side: the cards' closes and their stops."""
    groups = {}
    for f in fol:
        if f['state'] == 'open':
            groups.setdefault((f['coin'], f['side']), []).append(f)
    if not groups:
        return ['<b>Сделки по карточкам бота:</b> открытых по правилу нет']
    lines = ['<b>Сделки по карточкам бота</b> — бот не видит ваш счёт; открыты по правилу:']
    for (coin, side), fs in sorted(groups.items(), key=lambda kv: (adv3.COINS.index(kv[0][0]), -kv[0][1])):
        fs = sorted(fs, key=lambda f: f['close_of'])
        one = len(fs) == 1
        lines.append(f"{DOT[side]} {coin} {SIDE[side]} — {'карточка' if one else 'карточки'} "
                     f"{', '.join(adv3.ddmm(f['close_of']) for f in fs)} · {'стоп' if one else 'стопы'} "
                     f"{' · '.join(adv3.price(f['stop']) for f in fs)}")
    return lines


def zone_lines(zones, rep):
    """The entries whose zone the price has left, each with what to do instead."""
    if not zones:
        return []
    price = adv3.price
    lines = [f"<b>Зоны входа карточек закрытия {adv3.ddmm(rep['close_of'])}</b>"]
    for z in zones:
        lo, hi = z['zone']
        if z['mode'] == 'limit':
            lines.append(f"{z['coin']} {SIDE[z['side']]} — цена {price(z['mark'])} ушла из зоны {price(lo)}–{price(hi)}: "
                         f"лимит {price(z['entry'])}, не догонять")
        else:
            lines.append(f"{z['coin']} {SIDE[z['side']]} — цена {price(z['mark'])} у стопа {price(z['stop'])}: не входить")
    return lines


def weak_lines(weak):
    """The weakened trades, one line: information, not an exit."""
    if not weak:
        return []
    return ['ℹ️ Ослабление: ' + ', '.join(f'{coin} {SIDE[side]}' for coin, side in weak) + ' — сумма знаков упала с ±4 до ±2, '
            'сигнал держится; по правилу это не выход']


def quiet_line(slot, rep, fol, now):
    """The one line of a check that finds nothing, sent without a notification so that silence is never read as the bot down."""
    n = sum(f['state'] == 'open' for f in fol)
    head = f"✓ {hhmm(now)} по Батуми · закрытие {adv3.ddmm(rep['close_of'])}"
    if slot[1] == 'signal':
        return (f"{head}: без изменений — ТОП-3 тот же ({', '.join(rep['top']) or 'пуст'}), сигналы не менялись; сделок по "
                f"карточкам открыто {n}, стопы не задеты; новых STRONG нет · карточки дня — «сигнал»")
    return (f"{head}: событий нет — стопы {n} {adv3.plural(n, 'сделки', 'сделок', 'сделок')} по карточкам не задеты, зоны входа "
            f"на месте, новых STRONG нет · следующая проверка {hhmm(next_at(now))}")


def compose(slot, rep, fol, al, p, zones, prev, now, weak=()):
    """(text, quiet, one line, cards offered) of a check. It notifies only for an alert. The signal check is the close's
    message - events, changes, cards, STRONG candidates, the trades the cards offered and those weakened - or one line where it
    finds nothing: no alert, no weakening, no change of signal among the coins, the TOP-3 with its sides and STRONG as at the
    check before. The fact check is its events and the zones left, or one line where it finds neither."""
    loud = bool(al)
    new = {(a['coin'], a['side']) for a in al if a['kind'] == 'candidate'}
    if slot[1] == 'signal':
        same = (prev is not None and prev.get('top') == rep['top'] and prev.get('strong') == rep['strong']
                and all((prev.get('signals') or {}).get(c) == rep['rows'][c].get('signal') for c in rep['top']))
        if not loud and not weak and same and not any(adv3.changes(rep)):
            return quiet_line(slot, rep, fol, now), True, True, []
        tail = candidate_lines(rep, p, new) + [''] + followed_lines(fol) + weak_lines(weak)
        return adv3.message(rep, adv3.FACTS, head=event_lines(al, p), tail=tail), not loud, False, rep['cards']
    if not loud and not zones:
        return quiet_line(slot, rep, fol, now), True, True, []
    lines = [f"🕓 <b>ADV-3 · проверка {hhmm(now)} по Батуми</b> · закрытие {adv3.ddmm(rep['close_of'])} (UTC)"]
    if not rep['marks_ok']:
        lines.append('⚠️ Текущие цены Binance недоступны: зоны входа не проверены')
    for block in (event_lines(al, p, fact=True), zone_lines(zones, rep)):
        if block:
            lines += [''] + block
    n = sum(f['state'] == 'open' for f in fol)
    lines += ['', f"Сделок по карточкам открыто: {n} · следующая проверка {hhmm(next_at(now))} по Батуми", FOOTER]
    offered = [it['card'] for it in p['items'] if (it['card']['coin'], it['card']['side']) in new]
    return '\n'.join(lines), not loud, False, offered


def check_record(slot, rep, fol, al, p, zones, ids, quiet, one_line, offered, at, weak=()):
    """The check's journal record (CANON PART VII's internal log; it measures and tunes nothing): every coin's signal, sum of
    signs, strength, rank, unit, close and mark; the trades the cards offered that this check read, with their state; the
    alerts with the price each fired at against the close it rests on; the trades weakened; the STRONG coins the allocation
    placed at the default budget; the zones left; the six ratings; and the cards the message offered."""
    rank = {coin: k for k, coin in enumerate(ranked(rep), 1)}
    rec = base_record('check', rep, ids, offered, at)
    rec.update(slot=slot_text(slot), quiet=quiet, one_line=one_line,
               state={coin: {'signal': r.get('signal'), 'sum': r.get('sum'), 'z': r.get('z'), 'rank': rank.get(coin), 'U': r.get('U'),
                             'close': r.get('close'), 'mark': r.get('mark')} for coin, r in rep['rows'].items()},
               followed=[{k: f.get(k) for k in ('coin', 'side', 'close_of', 'close', 'U', 'stop', 'state', 'day', 'price', 'R')}
                         for f in fol if f['state'] != 'closed'],
               alerts=al, weakened=[[c, s] for c, s in weak], passing=[[c, s] for c, s in candidates(p)], zones_left=zones,
               trust=rep['trust'],
               alloc={'budget': p['budget'], 'n': p['n'], 'risk': p['risk'], 'allocated': p['allocated'], 'free': p['free'],
                      'loss': p['loss'], 'items': [{'coin': it['card']['coin'], 'side': it['card']['side'], 'notional': it['notional'],
                                                    'leverage': it['leverage'], 'margin': it['margin'], 'loss': it['loss']} for it in p['items']],
                      'rejected': p['rejected']})
    return rec


def check(tg, data, slot, now):
    """One scheduled check (TZ-39): the report at the default deposit and risk, the trades the cards offered held by the rule, the
    candle forming since the close at the fact check, the allocation at the default budget, the alerts, the weakened trades at
    the signal check, the message - sent quiet unless it holds an alert - and its record, returned for the journal once the
    message is sent."""
    rep = top_n(live_report(data, adv3.DEPOSIT, adv3.RISK), adv3.TOP_N)
    last = dt.date.fromisoformat(rep['close_of'])
    offs, done, prev = journal_scan()
    forming = {}
    if slot[1] == 'fact':
        held = sorted({k[0] for k in offs if (*k, 'stop') not in done and (*k, 'signal') not in done})
        forming = forming_candles(held, last + adv3.DAY)
    fol = follow(offs, data.cs, data.funds, last, forming, done)
    p = plan(rep, data.cs, adv3.DEPOSIT, adv3.TOP_N, adv3.RISK, {c: liquidity(c, rep['made_at_ms']) for c in rep['strong']})
    prev_passing = {(c, s) for c, s in (prev or {}).get('passing') or []}
    al = alerts_of(fol, candidates(p), prev_passing, done, rep, p)
    zones = zones_left(rep, offs, fol) if slot[1] == 'fact' else []
    weak = weakened(fol, rep, data.cs) if slot[1] == 'signal' else []
    text, quiet, one_line, offered = compose(slot, rep, fol, al, p, zones, prev, now, weak)
    ids = tg.send(text, quiet=quiet)
    return check_record(slot, rep, fol, al, p, zones, ids, quiet, one_line, offered, now, weak)


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
    off_path, done_path = os.path.join(STATE, 'offset'), os.path.join(STATE, 'check-done')
    offset = int(read(off_path)) if os.path.exists(off_path) else 0
    done = slot_parse(read(done_path)) if os.path.exists(done_path) else None
    retry_at = 0.0
    log('serving the pinned chat: pid', os.getpid(), 'offset', offset, 'check-done', slot_text(done) if done else '-')
    while True:
        now = dt.datetime.now(dt.timezone.utc)
        slot = due(now, done)
        if slot and time.time() >= retry_at:
            try:
                rec = check(tg, data, slot, now)
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
                log('check sent:', slot_text(slot), 'for the close of', rec['close_of'], '| alerts', len(rec['alerts']),
                    '| quiet' if rec['quiet'] else '| loud', '| one line' if rec['one_line'] else '| full')
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
            handle(tg, data, msg.get('text') or '')
        if updates:
            put(off_path, str(offset))


def handle(tg, data, text):
    cmd = route(text)
    try:
        if cmd:
            kind, budget, n, risk = cmd
            if kind == 'assess':
                rep = top_n(live_report(data, adv3.DEPOSIT, adv3.RISK), adv3.TOP_N)
                rec = base_record('assess', rep, tg.send(adv3.assessment(rep, adv3.FACTS)), [])
                rec['trust'] = rep['trust']
            elif kind == 'alloc':
                rep = top_n(live_report(data, budget, risk), adv3.TOP_N)
                p = plan(rep, data.cs, budget, n, risk, {c: liquidity(c, rep['made_at_ms']) for c in rep['strong']})
                ids = [i for part in plan_parts(rep, p) for i in tg.send(part)]
                rec = base_record('alloc', rep, ids, [it['card'] for it in p['items']])
                rec['alloc'] = {'budget': budget, 'n': n, 'risk': risk, 'allocated': p['allocated'], 'free': p['free'], 'loss': p['loss'],
                                'items': [{'coin': it['card']['coin'], 'side': it['card']['side'], 'notional': it['notional'],
                                           'leverage': it['leverage'], 'margin': it['margin'], 'loss': it['loss']} for it in p['items']],
                                'rejected': p['rejected']}
            else:
                rep, msg = make(data, adv3.DEPOSIT, risk, n)
                rec = base_record('request', rep, tg.send(msg))
                rec['n'] = n
            try:
                append(rec)
            except Exception:
                log('request record failed\n' + traceback.format_exc())
            log('request answered for the close of', rep['close_of'], '| kind', kind)
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
    and parsed - the klines endpoint read for the closed candles and for the candle forming since 00:00 UTC. Prints counts,
    dates and the bot's name; never the token or a chat id."""
    now_ms = int(time.time() * 1000)
    today = dt.datetime.now(dt.timezone.utc).date()
    c = adv3.fapi_candles('BTCUSDT', now_ms)
    assert c and max(c) >= today - 2 * adv3.DAY and all(len(v) == 4 and v[3] > 0 for v in c.values()), 'klines'
    f = forming_candles(['BTC'], today).get('BTC')
    assert f and len(f) == 4 and f[1] >= max(f[0], f[3]) and 0 < f[2] <= min(f[0], f[3]), 'the forming candle'
    print('P-KLINES served:', len(c), 'closed daily candles of BTCUSDT, the last', max(c), '- and the candle forming since', today)
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
        'ADV-3 подключён к этому чату. Напишите «сигнал» — или ждите проверок в 04:10 и 16:10 по Батуми.')
    assert ids and all(isinstance(x, int) for x in ids), ids
    print('G-HELLO sent: message ids', ids)


def selftest():
    """The bot's own checks, offline: the commands, the schedule, the trades the cards offered held by the rule, the alerts,
    the scanner, a check's message and record and three checks end to end, the TOP-N list, the allocation (golden cases computed
    by hand, the limits over random scenarios), the replies, the chunks, the files, the log, the HTML fallback and the quiet
    flag, glibc. Every expectation is computed here by hand or by a formula of its own, never by the code under test."""
    import contextlib, io, random, shutil, tempfile
    done = []

    def chk(name, ok):
        done.append(name)
        assert ok, name

    R, RM, T3 = adv3.RISK, adv3.RISK_MAX, adv3.TOP_N
    A_ = ('assess', None, None, None)
    for text, want in (('сигнал', ('signal', None, T3, R)), ('Сигнал 0,5%', ('signal', None, T3, 0.5)),
                       ('signal 0.3', ('signal', None, T3, 0.3)), ('сигналы', ('signal', None, T3, R)),
                       ('сигнал топ 3', ('signal', None, 3, R)), ('сигнал топ 5', ('signal', None, 5, R)),
                       ('сигнал топ 7', ('signal', None, 7, R)), ('топ 7', ('signal', None, 7, R)), ('сигнал топ 10', ('signal', None, 7, R)),
                       ('сигнал топ 0', ('signal', None, 1, R)), ('сигнал топ-5 1', ('signal', None, 5, 1.0)), ('сигнал 99', ('signal', None, T3, RM)),
                       ('сигнал 10000 топ 3', ('alloc', 10000.0, 3, R)), ('сигнал 15000 топ 5', ('alloc', 15000.0, 5, R)),
                       ('сигнал 10000', ('alloc', 10000.0, 3, R)), ('Сигнал 15 000 топ 5 1', ('alloc', 15000.0, 5, 1.0)),
                       ('/signal@adv3_bot 5000 top 2', ('alloc', 5000.0, 2, R)), ('signal 5000 top2', ('alloc', 5000.0, 2, R)),
                       ('топ 3 на 10000', ('alloc', 10000.0, 3, R)), ('топ3 10000', ('alloc', 10000.0, 3, R)),
                       ('сигнал 10к топ 3', ('alloc', 10000.0, 3, R)), ('signal 15k top 5', ('alloc', 15000.0, 5, R)),
                       ('сигнал 1,5 тыс', ('alloc', 1500.0, 3, R)), ('сигнал 10 коинов', ('signal', None, T3, RM)),
                       ('сигнал 10000 топ-3', ('alloc', 10000.0, 3, R)), ('сигнал 10000 топ 3 0,3', ('alloc', 10000.0, 3, 0.3)),
                       ('стратегия 7000 топ 2', ('alloc', 7000.0, 2, R)), ('сигнал 20000 топ 3 3', ('alloc', 20000.0, 3, RM)),
                       ('сигнал 12000 0.01', ('alloc', 12000.0, 3, 0.05)), ('сигнал 10000 usdt топ 1', ('alloc', 10000.0, 1, R)),
                       ('сигнал 10000 топ 0', ('alloc', 10000.0, 1, R)), ('сигнал 10000 топ 50', ('alloc', 10000.0, 7, R)),
                       ('signal 200000000', ('alloc', 10_000_000.0, 3, R)), ('сигнал 100 топ 3', ('alloc', 100.0, 3, R)),
                       ('оценка', A_), ('Оценка', A_), ('/оценка', A_), ('оценки доверия', A_), ('rating', A_),
                       ('привет', None), ('сигнализация', None), ('', None), ('12345', None), ('все', None), ('eth', None),
                       ('оценочный', None)):
        chk(f'route {text!r}', route(text) == want)
    chk('HELP names the commands, the list to 7, the 14 % filter, the checks at 04:10 and 16:10 and the quiet rule, in one part',
        all(k in HELP for k in ('«сигнал»', '«сигнал топ 7»', '«сигнал 10000 топ 3»', '«оценка»', '14%', 'STRONG', 'не больше 1%',
                                '04:10', '16:10', 'одной строкой')) and len(chunks(HELP)) == 1)
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

    class Fake(Telegram):
        def __init__(self):
            super().__init__('123456:SECRET', 777)
            self.calls = []

        def call(self, method, http_timeout=30, **params):
            self.calls.append(params)
            if params.get('parse_mode') == 'HTML' and '<b>bad' in params.get('text', ''):
                raise RuntimeError("telegram sendMessage: 400 Bad Request: can't parse entities")
            return {'message_id': len(self.calls)}

    fk = Fake()
    chk('HTML sent as HTML, with a notification', fk.send('<b>ok</b>') == [1] and fk.calls[0]['parse_mode'] == 'HTML'
        and 'disable_notification' not in fk.calls[0])
    chk('unparseable HTML resent as plain text', fk.send('<b>bad &amp; x</b>') == [3]
        and 'parse_mode' not in fk.calls[2] and fk.calls[2]['text'] == 'bad & x')
    n0 = len(fk.calls)
    fk.send('\n'.join(['q' * 3000, 'r' * 3000]), quiet=True)
    fk.send('<b>bad quiet</b>', quiet=True)
    chk('quiet: every part, the plain fallback among them, without a notification',
        len(fk.calls) == n0 + 4 and all(c.get('disable_notification') is True for c in fk.calls[n0:]))
    SECRETS.append('123456:SECRET')
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        log('url https://api.telegram.org/bot123456:SECRET/getMe failed')
    SECRETS.remove('123456:SECRET')
    chk('the token never reaches the log', 'SECRET' not in buf.getvalue() and '<token>' in buf.getvalue())

    # ---- the schedule ---------------------------------------------------------------------------------------------
    X = dt.date(2026, 11, 5)
    at = lambda d, h, m, s=0: dt.datetime.combine(d, dt.time(h, m, s), tzinfo=dt.timezone.utc)
    sig, fac = (X, 'signal'), (X, 'fact')
    chk('latest_slot: 00:09:59 is the day before\'s fact, 00:10 the signal, 12:09:59 still the signal, 12:10 the fact',
        [latest_slot(at(X, 0, 9, 59)), latest_slot(at(X, 0, 10)), latest_slot(at(X, 12, 9, 59)), latest_slot(at(X, 12, 10)),
         latest_slot(at(X, 23, 59, 59))] == [(X - adv3.DAY, 'fact'), sig, sig, fac, fac])
    chk('due: nothing done runs the day\'s signal, at 00:10 and at 14:00 alike (12:10 repeats 00:10)',
        due(at(X, 0, 10), None) == sig and due(at(X, 14, 0), None) == sig)
    chk('due: the signal done, nothing before 12:10, the fact at 12:10; the fact done, nothing until 00:10',
        due(at(X, 11, 0), sig) is None and due(at(X, 12, 10), sig) == fac and due(at(X, 23, 0), fac) is None
        and due(at(X + adv3.DAY, 0, 10), fac) == (X + adv3.DAY, 'signal'))
    chk('due: the day\'s signal failed until 12:10 - the 12:10 slot runs the signal', due(at(X, 12, 10), (X - adv3.DAY, 'fact')) == sig)
    chk('done_after: a signal ended before 12:10 is itself; at or after 12:10 it covers the fact; a fact is itself',
        done_after(sig, at(X, 0, 10, 30)) == sig and done_after(sig, at(X, 12, 10)) == fac and done_after(fac, at(X, 13, 0)) == fac)
    chk('next_at: 00:10, then 12:10, then 00:10 of the next day',
        [next_at(at(X, 0, 9)), next_at(at(X, 0, 10)), next_at(at(X, 12, 10)), next_at(at(X, 23, 0))]
        == [at(X, 0, 10), at(X, 12, 10), at(X + adv3.DAY, 0, 10), at(X + adv3.DAY, 0, 10)])
    chk('slot_text and slot_parse: a round trip, and nothing else parsed', slot_parse(slot_text(fac)) == fac
        and slot_parse('2026-11-05 daily') is None and slot_parse('garbage') is None and slot_parse('') is None)
    runs, d_, t = [], None, at(X, 13, 0)
    while t < at(X + 3 * adv3.DAY, 23, 59):
        s = due(t, d_)
        fail = s == (X + adv3.DAY, 'signal') and t < at(X + adv3.DAY, 12, 30)
        if s and not fail:
            runs.append((slot_text(s), t.strftime('%d %H:%M')))
            d_ = done_after(s, t)
        t += dt.timedelta(minutes=1)
    chk('three days minute by minute from a first start at 13:00: each slot once, a signal failing until 12:30 covering its fact',
        runs == [('2026-11-05 signal', '05 13:00'), ('2026-11-06 signal', '06 12:30'), ('2026-11-07 signal', '07 00:10'),
                 ('2026-11-07 fact', '07 12:10'), ('2026-11-08 signal', '08 00:10'), ('2026-11-08 fact', '08 12:10')])

    # ---- the trades the cards offered, held by the rule ---------------------------------------------------------------
    d0 = dt.date(2026, 1, 1)

    def candles(closes, width=0.01, start=d0, opens=None):
        """Candles from closes: high and low width around each close, the open the close before unless opens names it."""
        out, prev = {}, closes[0]
        for i, cl in enumerate(closes):
            o = (opens or {}).get(i, prev)
            out[start + i * adv3.DAY] = (o, max(o, cl) * (1 + width), min(o, cl) * (1 - width), cl)
            prev = cl
        return out

    def sum_signs(closes, i):
        """The sum of the four signs, written here: the close against those 14, 28, 56 and 112 days before."""
        return sum((closes[i] > closes[i - L]) - (closes[i] < closes[i - L]) for L in (14, 28, 56, 112))

    rise = [100 * 1.01 ** i for i in range(150)]
    fall = rise + [rise[-1] * 0.998 ** k for k in range(1, 40)]
    c_fall = candles(fall, 0.002)
    D = d0 + 145 * adv3.DAY
    expect_exit = next(i for i in range(146, len(fall)) if sum_signs(fall, i) < 2)
    off_sig = {('BTC', 1, str(D)): {'coin': 'BTC', 'side': 1, 'close_of': str(D), 'close': fall[145], 'U': 60.0,
                                    'stop': fall[145] - 60.0, 'mode': 'market', 'first': None}}
    f1 = follow(off_sig, {'BTC': c_fall}, {}, d0 + (len(fall) - 1) * adv3.DAY)[0]
    chk('follow: a long whose sum of signs falls below +2 ends at that close, its price the close',
        f1['state'] == 'signal' and f1['day'] == str(d0 + expect_exit * adv3.DAY) and f1['price'] == fall[expect_exit])
    gap = candles(rise, 0.002, opens={148: rise[147] * 0.95})
    off_stop = {('ETH', 1, str(D)): {'coin': 'ETH', 'side': 1, 'close_of': str(D), 'close': rise[145], 'U': rise[145] * 0.02,
                                     'stop': rise[145] * 0.98, 'mode': 'market', 'first': None}}
    f2 = follow(off_stop, {'ETH': gap}, {}, d0 + 149 * adv3.DAY)[0]
    chk('follow: a gap through the stop exits at the open, on the gap\'s day', f2['state'] == 'stop' and f2['day'] == str(d0 + 148 * adv3.DAY)
        and f2['price'] == rise[147] * 0.95)
    wick = candles(rise, 0.002)
    S = rise[145] * 0.995
    wick[d0 + 147 * adv3.DAY] = (rise[146], rise[147] * 1.002, S * 0.999, rise[147])
    f3 = follow({('ETH', 1, str(D)): dict(off_stop[('ETH', 1, str(D))], U=rise[145] - S, stop=S)}, {'ETH': wick}, {},
                d0 + 149 * adv3.DAY)[0]
    chk('follow: a wick through the stop exits at the stop', f3['state'] == 'stop' and f3['day'] == str(d0 + 147 * adv3.DAY)
        and abs(f3['price'] - S) < 1e-9)
    c_open = candles(rise, 0.002)
    last_o = d0 + 149 * adv3.DAY
    k_open = ('SOL', -1, str(D))
    off_short = {k_open: {'coin': 'SOL', 'side': -1, 'close_of': str(D), 'close': rise[145], 'U': 1000.0, 'stop': rise[145] + 1000.0,
                          'mode': 'limit', 'first': None}}
    f4 = follow(off_short, {'SOL': c_open}, {}, last_o)[0]
    chk('follow: a short on a rising series ends at the first close whose sum of signs is above -2', f4['state'] == 'signal'
        and f4['day'] == str(D + adv3.DAY))
    off_long = {('BTC', 1, str(last_o - adv3.DAY)): {'coin': 'BTC', 'side': 1, 'close_of': str(last_o - adv3.DAY), 'close': rise[148],
                                                     'U': 5.0, 'stop': rise[148] - 5.0, 'mode': 'market', 'first': None}}
    S4 = rise[148] - 5.0
    f5 = follow(off_long, {'BTC': c_open}, {}, last_o)[0]
    f6 = follow(off_long, {'BTC': c_open}, {}, last_o, {'BTC': (rise[149], rise[149], S4 - 0.01, S4 + 1)})[0]
    f7 = follow(off_long, {'BTC': c_open}, {}, last_o, {'BTC': (rise[149], rise[149] + 1, S4 + 0.01, S4 + 1)})[0]
    chk('follow: an open long; the candle forming after the close reaching its stop is a touch, its low the price; one above it is not',
        f5['state'] == 'open' and f6['state'] == 'touch' and f6['day'] == str(last_o + adv3.DAY) and f6['price'] == S4 - 0.01
        and f7['state'] == 'open')
    k_long = next(iter(off_long))
    chk('follow: an alerted offer is closed and not held; an offer of a close with no candle is unknown',
        follow(off_long, {'BTC': c_open}, {}, last_o, None, {k_long + ('stop',)})[0]['state'] == 'closed'
        and follow({('BTC', 1, '2025-01-01'): dict(off_long[k_long], close_of='2025-01-01')}, {'BTC': c_open}, {}, last_o)[0]['state'] == 'unknown')
    recs = [{'kind': 'daily', 'close_of': '2026-10-29', 'cards': [
                {'coin': 'BTC', 'side': 1, 'mode': 'market', 'close': 100.0, 'U': 8.0, 'stop': 92.0},
                {'coin': 'ETH', 'side': -1, 'mode': 'none', 'close': 50.0, 'U': 4.0, 'stop': 54.0},
                {'coin': 'NOPE', 'side': 1, 'mode': 'market', 'close': 1.0, 'U': 0.1},
                {'coin': 'SOL'}]},
            {'kind': 'alloc', 'close_of': '2026-10-30', 'alloc': {'items': [{'coin': 'XRP'}]}, 'cards': [
                {'coin': 'XRP', 'side': 1, 'mode': 'limit', 'close': 2.0, 'U': 0.2}, {'coin': 'ADA', 'side': 1, 'mode': 'market', 'close': 0.5, 'U': 0.05}]},
            {'kind': 'request', 'close_of': '2026-10-29', 'cards': [{'coin': 'BTC', 'side': 1, 'mode': 'limit', 'close': 101.0, 'U': 9.0}]},
            {'kind': 'check', 'close_of': '2026-10-30', 'cards': [{'coin': 'BTC', 'side': 1, 'mode': 'market', 'close': 104.0, 'U': 8.5}],
             'alerts': [{'kind': 'stop', 'coin': 'XRP', 'side': 1, 'close_of': '2026-10-30'}, {'kind': 'candidate', 'coin': 'BTC', 'side': 1,
                                                                                            'close_of': '2026-10-30'}, {'bad': 1}]},
            {'kind': 'check', 'close_of': 'x', 'cards': [{'coin': 'BTC', 'side': 1, 'mode': 'market', 'close': 1.0, 'U': 1.0}]}]
    offs = offers(recs)
    chk('offers: entries offered at market or as a limit, by coin, side and close, the first kept; no entry, an unknown coin, a '
        'broken card, an allocation\'s unplaced coin and a bad close left out', list(offs) == [('BTC', 1, '2026-10-29'), ('XRP', 1, '2026-10-30'),
                                                                                            ('BTC', 1, '2026-10-30')]
        and offs[('BTC', 1, '2026-10-29')]['stop'] == 92.0 and offs[('BTC', 1, '2026-10-29')]['mode'] == 'market')
    chk('alerted: the alerts of check records alone, a broken one left out',
        alerted(recs) == {('XRP', 1, '2026-10-30', 'stop'), ('BTC', 1, '2026-10-30', 'candidate')})

    # ---- a synthetic market: twelve coins, trends of several strengths -----------------------------------------------
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
    marks = {c + 'USDT': (cs[c][last][3], 0.0001) for c in cs}
    rep0 = adv3.report(cs, funds, marks, 10000.0, 0.5, int(at(last + adv3.DAY, 0, 10).timestamp() * 1000))
    order = ranked(rep0)
    active = [c for c in adv3.COINS if rep0['rows'][c].get('signal') in (1, -1) and rep0['rows'][c].get('z') is not None]
    by_hand = sorted(active, key=lambda c: (-abs(rep0['rows'][c]['z']), adv3.COINS.index(c)))
    chk('ranked: every active coin by |z|, ties in the coins\' order, its first three the report\'s TOP-3',
        order == by_hand and order[:3] == rep0['top'] and len(order) == 12)
    r7 = top_n(rep0, 7)
    chk('top_n: seven cards ranked 1 to 7 of 7, the TOP-3\'s own cards first, STRONG only among them, the ratings over all seven',
        [cd['coin'] for cd in r7['cards']] == order[:7] and [(cd['rank'], cd['of']) for cd in r7['cards']] == [(k, 7) for k in range(1, 8)]
        and all(dict(cd, rank=None, of=None) == dict(c0, rank=None, of=None) for cd, c0 in zip(r7['cards'], rep0['cards']))
        and not any(cd['strong'] for cd in r7['cards'][3:]) and len(r7['trust']['cards']) == 7 and r7['n'] == 7)
    r1 = top_n(rep0, 1)
    m7, m1 = adv3.message(r7, adv3.FACTS), adv3.message(r1, adv3.FACTS)
    chk('the TOP-7 message: seven cards, each its confidence, the label ТОП-7, the other signals without the seven; TOP-1 one card',
        m7.count('Основание: сумма знаков') == 7 and m7.count('Уверенность: <b>1/5</b>') == 7 and 'ТОП-7 по силе тренда' in m7
        and m7.count('ранг 7 из 7') == 1 and m1.count('Основание: сумма знаков') == 1 and len(r1['cards']) == 1
        and not any(f'{c},' in m7.split('Остальные сигналы')[1] or m7.split('Остальные сигналы')[1].rstrip().endswith(c) for c in order[:7]))

    # ---- the allocation: golden cases by hand, the selection with the 14 % limit, the limits at random ------------------
    D2 = adv3.DEPOSIT
    base = adv3.report(cs, funds, marks, 10000.0, 0.5, 1_793_000_000_000)

    def series(rets):
        """Candles whose daily log returns are rets, the last of them on `last`; closes from 100."""
        out, x = {}, 100.0
        ds = [last - dt.timedelta(days=len(rets) - k) for k in range(len(rets) + 1)]
        out[ds[0]] = (x, x, x, x)
        for d, r in zip(ds[1:], rets):
            x *= math.exp(r)
            out[d] = (x, x, x, x)
        return out

    A = [0.01 * (-1) ** k for k in range(60)]
    Bs = [0.01 * (1, 1, -1, -1)[k % 4] for k in range(60)]
    Cs = [0.01 * (1, -1, -1, 1)[k % 4] for k in range(60)]
    Ds = [-x for x in A]

    def scenario(spec, marks_ok=True, rets=None):
        rows = dict(base['rows'])
        for coin, side, z, stop, strong in spec:
            rows[coin] = {'signal': side, 'z': z, 'sum': 4 * side, 'U': stop, 'close': 100.0, 'prev': side, 'since': str(last),
                          'stop': 100.0 - side * stop, 'mark': 100.0, 'funding': 0.0001, 'funding_h': 8}
        r = dict(base, rows=rows, top=[c for c, *_ in spec], strong=[c for c, *_, st in spec if st], marks_ok=marks_ok, cards=[])
        return r, {c: series((rets or {}).get(c, A)) for c, *_ in spec}

    def pl(spec, budget=10000.0, n=3, risk=0.5, liq=None, rets=None, marks_ok=True):
        r, c = scenario(spec, marks_ok, rets)
        return r, plan(r, c, budget, n, risk, liq or {})

    r1_, p1 = pl([('ETH', 1, 2.0, 8.0, True)])
    it = p1['items'][0]
    chk('golden 1: one trade at an 8 % stop and 0,5 % risk is 609 USDT, leverage 7, margin 87, loss 50',
        (it['notional'], it['leverage'], it['margin'], it['loss']) == (609, 7, 87, 50) and p1['allocated'] == 609 and p1['free'] == 9391)
    r2_, p2 = pl([('ETH', 1, 2.0, 8.0, True), ('SOL', 1, 1.0, 10.0, True)], rets={'ETH': A, 'SOL': Bs})
    a, b = p2['items']
    chk('golden 2: two uncorrelated trades of strength 2 and 1 take two thirds and one third of the risk: 813 and 326 USDT',
        (a['notional'], b['notional']) == (813, 326) and (a['leverage'], b['leverage']) == (7, 6) and (a['margin'], b['margin']) == (117, 55)
        and (a['loss'], b['loss']) == (67, 34) and p2['allocated'] == 1139 and p2['loss'] == 101)
    r3_, p3 = pl([('ETH', 1, 2.0, 8.0, True), ('SOL', 1, 2.0, 8.0, True), ('XRP', 1, 2.0, 8.0, True)], rets={'ETH': A, 'SOL': A, 'XRP': Bs})
    chk('golden 3: a correlated pair is discounted and the independent trade takes more: shares 0.3, 0.3, 0.4; 548, 548 and 731 USDT',
        [round(x['share'], 6) for x in p3['items']] == [0.3, 0.3, 0.4] and [x['notional'] for x in p3['items']] == [548, 548, 731])
    r4_, p4 = pl([('ETH', 1, 2.0, 8.0, True), ('SOL', -1, 2.0, 8.0, True)], rets={'ETH': A, 'SOL': A})
    chk('golden 4: opposite sides on one series are no crowding: equal shares, 0.5 % each', [x['crowd'] for x in p4['items']] == [0.0, 0.0]
        and [x['notional'] for x in p4['items']] == [609, 609])
    r5_, p5 = pl([('ETH', 1, 2.0, 14.0, True)])
    it5 = p5['items'][0]
    chk('golden 5: a stop at the limit, 14 %: 352 USDT, leverage 4, margin 88, loss 50 - a wider stop, a smaller position, the same loss',
        (it5['notional'], it5['leverage'], it5['margin'], it5['loss']) == (352, 4, 88, 50))
    sel = [('ETH', 1, 3.0, 8.0, True), ('SOL', -1, 2.5, 15.0, True), ('XRP', 1, 2.0, 13.9, True), ('BTC', 1, 1.5, 6.0, False)]
    r6_, p6 = pl(sel, rets={'ETH': A, 'SOL': Bs, 'XRP': Cs, 'BTC': Ds})
    chk('selection: STRONG only; 13.9 % placed, 15 % rejected with its reason against 14 %; a weaker setup never fills a place',
        [x['card']['coin'] for x in p6['items']] == ['ETH', 'XRP'] and p6['rejected'] == [('SOL', 'SHORT', 'стоп 15,0% дальше 14,0%')]
        and p6['plain'] == ['BTC'])
    r7_, p7 = pl(sel[:3], n=1, rets={'ETH': A, 'SOL': Bs, 'XRP': Cs})
    chk('selection: only n are taken, the rest named', [x['card']['coin'] for x in p7['items']] == ['ETH']
        and ('XRP', 'LONG', 'сверх запрошенных 1') in p7['rejected'])
    r9_, p9 = pl([('ETH', 1, 2.0, 8.0, True)], marks_ok=False)
    chk('selection: without current prices nothing is placed', p9['items'] == [] and p9['rejected'] == [('ETH', 'LONG', 'нет текущей цены Binance')])
    r10_, p10 = pl([('ETH', 1, 2.0, 8.0, True)], liq={'ETH': 200_000.0})
    chk('liquidity: a position takes at most 0.1 % of the coin\'s mean daily volume, and says so',
        p10['items'][0]['notional'] == 200 and p10['items'][0]['capped'] is True and p1['items'][0]['capped'] is False)
    r12_, p12 = pl([('ETH', 1, 2.0, 8.0, True)], budget=50.0)
    chk('minimum: a position under 5 USDT is dropped with its reason', p12['items'] == [] and p12['rejected'] == [('ETH', 'LONG', 'позиция меньше 5 USDT')])
    rnd, bad = random.Random(39), []
    for trial in range(400):
        k = rnd.randint(1, 3)
        spec = [(adv3.COINS[m + 12], rnd.choice((1, -1)), rnd.uniform(1.0, 6.0), rnd.uniform(0.3, 18.0), rnd.random() < 0.85) for m in range(k)]
        rets = {c: [rnd.gauss(0, 0.03) if rnd.random() < 0.8 else x for x in A] for c, *_ in spec}
        budget, risk, n = rnd.choice((100.0, 777.0, 10000.0, 250000.0, 3e6)), rnd.choice((0.05, 0.3, 0.5, 1.0)), rnd.randint(1, 7)
        liq = {c: rnd.choice((None, 5e4, 1e6, 1e9)) for c, *_ in spec}
        r, pp = pl(spec, budget, n, risk, liq, rets)
        elig = [c for c, side, z, stop, st in spec if st and stop <= 14.0]
        got = [x['card']['coin'] for x in pp['items']]
        ok = (len(got) <= min(n, len(elig)) and set(got) <= set(elig) and all(float(x['notional']).is_integer() and 5 <= x['notional'] <= budget for x in pp['items'])
              and all(x['loss_exact'] <= budget * RM / 100 + 1e-9 for x in pp['items']) and pp['loss_exact'] <= budget * adv3.RISK_ALL / 100 + 1e-9
              and pp['allocated'] <= budget and pp['free'] == budget - pp['allocated']
              and all(x['margin'] * x['leverage'] >= x['notional'] and 1 <= x['leverage'] <= 20 for x in pp['items'])
              and all(x['card']['stop_pct'] <= 14.0 and x['card']['entry'] is not None for x in pp['items']))
        if not ok:
            bad.append(trial)
    chk('limits over 400 random scenarios: STRONG only and within n, stops within 14 %, each loss at the stop within 1 % of the budget, '
        'all within 5 %, positions whole and within the budget, margin covers the leverage', not bad)
    fr, stage = scenario([('ETH', 1, 3.0, 8.0, True), ('XRP', 1, 2.0, 10.0, True), ('SOL', -1, 2.5, 15.0, True), ('BTC', 1, 1.5, 6.0, False)],
                         rets={'ETH': A, 'XRP': Cs, 'SOL': Bs, 'BTC': Ds})
    pf = plan(fr, stage, 10000.0, 3, 0.5, {})
    view = plan_parts(fr, pf)
    first = view[0]
    chk('plan_parts: one message with the Boss\'s fields - budget, count and ranking, quality, entry, stop, targets with TZ-38\'s '
        'shares, capital, leverage, margin, loss, invalidation, unallocated', len(view) == 1 and all(k in first for k in (
            'Бюджет 10 000 USDT', 'стоп не дальше 14,0% входа', 'Подходящих сделок: 2 из 3 запрошенных', '1) 🟢 <b>ETH · LONG</b> · ★ STRONG',
            '2) 🟢 <b>XRP · LONG</b>', 'Качество: z', 'Вход:', '⛔ Стоп:', '· дошли 47%', 'Капитал:', 'плечо', 'маржа', 'Потеря на стопе:',
            'Свободно', 'Размещено', 'Инвалидация:')))
    chk('plan_parts: each trade its confidence with the note that the sizes are unproven; no six ratings; the rejected and the weaker named',
        first.count('Уверенность: <b>1/5</b> — правило не доказано · размеры — формула Архитектора, не доказана') == 2
        and 'Оценка доверия' not in first and 'Отклонены: SOL SHORT — стоп 15,0% дальше 14,0%' in first
        and 'В ТОП-3 без STRONG — не берутся: BTC' in first and 'не доказанная' in first)
    chk('plan_parts: one Telegram part, balanced markup; five requested says STRONG is at most three; none qualifying says so',
        len(chunks(first)) == 1 and all(first.count('<%s>' % t) == first.count('</%s>' % t) for t in ('b', 'i'))
        and 'больше 3 сделок не будет' in plan_parts(fr, plan(fr, stage, 15000.0, 5, 0.5, {}))[0]
        and 'Подходящих сделок нет' in plan_parts(*pl([('SOL', -1, 2.5, 15.0, True)], rets={'SOL': A}))[0])

    wk = [100 * 1.01 ** i for i in range(150)]
    wk.append(wk[-1] * 0.86)
    c_wk = candles(wk, 0.002)
    lw = d0 + 150 * adv3.DAY
    by_hand = [sum_signs(wk, 149), sum_signs(wk, 150)]
    rep_wk = {'close_of': str(lw), 'rows': {'BTC': {'signal': 1, 'sum': by_hand[1]}, 'ETH': {'signal': 1, 'sum': 2}}}
    fol_wk = [{'coin': 'BTC', 'side': 1, 'state': 'open'}, {'coin': 'BTC', 'side': 1, 'state': 'open'},
              {'coin': 'ETH', 'side': 1, 'state': 'open'}, {'coin': 'SOL', 'side': 1, 'state': 'stop'}]
    chk('weakened: a sum of signs from +4 at the close before to +2 at this one, the signal kept, is a weakening, once a coin; a sum '
        'that was not +4 before is not', by_hand == [4, 2] and weakened(fol_wk, rep_wk, {'BTC': c_wk, 'ETH': candles([100.0] * 151)}) == [('BTC', 1)]
        and weakened(fol_wk, dict(rep_wk, rows={'BTC': {'signal': 1, 'sum': 4}}), {'BTC': c_wk}) == []
        and weak_lines([('BTC', 1)]) == ['ℹ️ Ослабление: BTC LONG — сумма знаков упала с ±4 до ±2, сигнал держится; по правилу это не выход'])

    # ---- alerts, zones and the check's message ------------------------------------------------------------------------
    p_ = plan(rep0, cs, D2, 3, 0.5, {})
    placed = candidates(p_)
    chk('the synthetic market has STRONG coins the allocation places', len(placed) >= 1 and set(c for c, _ in placed) <= set(rep0['strong']))
    c0 = placed[0]
    fol0 = [dict(f5, key=k_long, state='stop', day=str(last), price=90.0, close=100.0, stop=91.0),
            dict(f5, key=('ETH', 1, '2026-11-01'), coin='ETH', close_of='2026-11-01', state='touch', day=str(last + adv3.DAY), price=1.0, stop=2.0),
            dict(f5, key=('SOL', -1, '2026-11-01'), coin='SOL', side=-1, close_of='2026-11-01', state='signal', day=str(last), price=5.0),
            dict(f5, key=('XRP', 1, '2026-11-02'), coin='XRP', close_of='2026-11-02', state='open')]
    al = alerts_of(fol0, placed, set(), {(k_long[0], 1, k_long[2], 'stop')}, rep0, p_)
    chk('alerts_of: a stop once, a touch as a stop, a signal exit, each candidate the check before did not place; prices against closes',
        [(x['kind'], x['coin']) for x in al] == [('stop', 'ETH'), ('signal', 'SOL')] + [('candidate', c) for c, _ in placed]
        and al[0]['touch'] is True and al[0]['level'] == 2.0 and al[1]['level'] == 5.0 and al[2]['level'] == p_['items'][0]['card']['stop'])
    chk('alerts_of: a candidate placed at the check before is not new', [x['kind'] for x in alerts_of([], placed, set(placed), set(), rep0, p_)] == [])
    coin_z = rep0['top'][0]
    row = rep0['rows'][coin_z]
    k_z = (coin_z, row['signal'], rep0['close_of'])
    off_z = {k_z: {'coin': coin_z, 'side': row['signal'], 'close_of': rep0['close_of'], 'close': row['close'], 'U': row['U'],
                   'stop': row['close'] - row['signal'] * row['U'], 'mode': 'market', 'first': None}}
    fol_z = [{'key': k_z, 'state': 'open'}]
    zone_hi = row['close'] + row['signal'] * 0.3 * row['U']
    run = dict(rep0, rows=dict(rep0['rows'], **{coin_z: dict(row, mark=zone_hi)}))
    near = dict(rep0, rows=dict(rep0['rows'], **{coin_z: dict(row, mark=row['close'] - row['signal'] * 0.8 * row['U'])}))
    zl, zn = zones_left(run, off_z, fol_z), zones_left(near, off_z, fol_z)
    chk('zones_left: past the zone a limit at its edge, near the stop no entry, inside it nothing, another close nothing',
        [z['mode'] for z in zl] == ['limit'] and abs(zl[0]['entry'] - (row['close'] + row['signal'] * 0.25 * row['U'])) < 1e-9
        and [z['mode'] for z in zn] == ['none'] and zones_left(rep0, off_z, fol_z) == []
        and zones_left(run, {k_z: dict(off_z[k_z], close_of='2026-01-01')}, fol_z) == [])
    now0 = at(last + adv3.DAY, 0, 10)
    prev_same = {'top': rep0['top'], 'strong': rep0['strong'], 'signals': {c: rep0['rows'][c].get('signal') for c in adv3.COINS}}
    still = dict(rep0, rows={c: dict(r, prev=r.get('signal')) for c, r in rep0['rows'].items()})
    t1, q1, o1, cards1 = compose((last + adv3.DAY, 'signal'), still, [], [], p_, [], prev_same, now0)
    t1w, q1w, o1w, _c = compose((last + adv3.DAY, 'signal'), still, [], [], p_, [], prev_same, now0, [(order[0], 1)])
    chk('compose: a signal check that finds nothing is one quiet line naming the TOP-3, offering no card; a weakening makes it full and quiet',
        q1 and o1 and cards1 == [] and '\n' not in t1 and t1.startswith('✓ 04:10 по Батуми') and ', '.join(rep0['top']) in t1
        and q1w and not o1w and 'ℹ️ Ослабление' in t1w)
    flip = order[-1]
    moved = dict(still, rows=dict(still['rows'], **{flip: dict(still['rows'][flip], prev=-still['rows'][flip]['signal'])}))
    t2, q2, o2, cards2 = compose((last + adv3.DAY, 'signal'), moved, fol0, [], p_, [], prev_same, now0)
    chk('compose: a signal check with the day\'s changes is the full message, quiet without an alert, its cards offered, no methodology',
        q2 and not o2 and cards2 == rep0['cards'] and 'STRONG-кандидаты' in t2 and 'Сделки по карточкам бота' in t2 and '🔄 Разворот' in t2
        and 'XRP LONG — карточка' in t2 and 'Оценка доверия' not in t2 and 'Форвард с' not in t2 and '🔔' not in t2)
    t3, q3, o3, _ = compose((last + adv3.DAY, 'signal'), still, fol0, al, p_, [], prev_same, now0)
    chk('compose: an alert makes the signal check loud and full, the events right after the header, a new candidate marked',
        not q3 and not o3 and t3.index('🔔 <b>События</b>') < t3.index('Изменения за день') and '⛔ ETH LONG' in t3
        and '🚪 SOL SHORT' in t3 and f'🆕 {c0[0]} {SIDE[c0[1]]} — проходит' in t3)
    nowf = at(last + adv3.DAY, 12, 10)
    t4, q4, o4, cards4 = compose((last + adv3.DAY, 'fact'), rep0, fol0[3:], [], p_, [], prev_same, nowf)
    t5, q5, o5, cards5 = compose((last + adv3.DAY, 'fact'), rep0, fol0[3:], [], p_, zl, prev_same, nowf)
    t6, q6, o6, cards6 = compose((last + adv3.DAY, 'fact'), rep0, fol0, al, p_, [], prev_same, nowf)
    chk('compose: a fact check that finds nothing is one quiet line naming the next check; zones alone are quiet and several lines',
        q4 and o4 and cards4 == [] and t4.startswith('✓ 16:10 по Батуми') and 'следующая проверка 04:10' in t4 and '\n' not in t4
        and q5 and not o5 and 'Зоны входа карточек закрытия' in t5 and 'не догонять' in t5 and cards5 == [])
    chk('compose: a fact check with alerts is loud, carries each new candidate\'s plan and offers its card, no other card',
        not q6 and not o6 and '🔔 <b>События</b>' in t6 and 'теперь проходит лимиты' in t6 and t6.count('Капитал:') == len(placed)
        and [cd['coin'] for cd in cards6] == [c for c, _ in placed] and 'сегодня (минимум дня' in t6)
    chk('compose: every message balances its markup and fits one Telegram part', all(
        len(chunks(t)) == 1 and t.count('<b>') == t.count('</b>') and t.count('<i>') == t.count('</i>') for t in (t1, t2, t3, t4, t5, t6)))
    recq = check_record((last + adv3.DAY, 'signal'), rep0, fol0 + [dict(fol0[0], state='closed')], al, p_, [], [7, 8], False, False, cards2, now0,
                        [('XRP', 1)])
    chk('check_record: kind, slot, flags, every coin\'s state with the ranks, the followed trades but the closed, the alerts with their '
        'prices, the placed coins, the six ratings, the cards with their confidence', recq['kind'] == 'check' and recq['slot'] == slot_text((last + adv3.DAY, 'signal'))
        and recq['quiet'] is False and recq['one_line'] is False and len(recq['state']) == len(adv3.COINS)
        and [c for c in adv3.COINS if recq['state'][c]['rank']] == [c for c in adv3.COINS if c in order]
        and all(recq['state'][c]['rank'] == order.index(c) + 1 for c in order) and len(recq['followed']) == 4
        and recq['alerts'] == al and recq['passing'] == [list(x) for x in placed] and recq['message_ids'] == [7, 8] and recq['weakened'] == [['XRP', 1]]
        and set(recq['trust']) >= {'system', 'strong_justified', 'cards', 'quality', 'expectancy_established'}
        and [c['confidence'] for c in recq['cards']] == [rep0['trust']['cards'][cd['coin']] for cd in cards2]
        and json.loads(json.dumps(recq, default=str))['utc'] == now0.isoformat(timespec='seconds'))

    # ---- three checks end to end: Binance and Telegram stood in for, the journal in a scratch directory ------------------
    class Cap(Telegram):
        def __init__(self, down=False):
            super().__init__('123456:SECRET', 777)
            self.sent, self.down = [], down

        def call(self, method, http_timeout=30, **params):
            if self.down:
                raise RuntimeError('telegram sendMessage: 502 Bad Gateway')
            self.sent.append((params['text'], params.get('disable_notification', False)))
            return {'message_id': len(self.sent)}

    class Stub:
        def __init__(self, cs, funds):
            self.cs, self.funds, self.missing = cs, funds, []

        def fresh(self):
            return self.cs, self.funds

    ms = lambda d: int(dt.datetime.combine(d, dt.time(0), tzinfo=dt.timezone.utc).timestamp() * 1000)
    forming = {}

    def fake_fapi(path, **params):
        if path == '/fapi/v1/premiumIndex':
            return [{'symbol': c + 'USDT', 'markPrice': str(m[0]), 'lastFundingRate': '0.0001'} for c, m in ((k[:-4], v) for k, v in marks.items())]
        if path == '/fapi/v1/fundingInfo':
            return []
        coin = params['symbol'][:-4]
        if params.get('limit') == 2:
            o, h, l, c_ = forming.get(coin) or (cs[coin][last][3],) * 4
            return [[ms(last), '1', '1', '1', '1', '0', ms(last + adv3.DAY) - 1, '0'],
                    [ms(last + adv3.DAY), str(o), str(h), str(l), str(c_), '0', ms(last + 2 * adv3.DAY) - 1, '0']]
        return [[ms(last - k * adv3.DAY), '1', '1', '1', '1', '0', ms(last - k * adv3.DAY + adv3.DAY) - 1, '1e12'] for k in range(8)]

    state = tempfile.mkdtemp(prefix='.selftest-', dir=os.path.dirname(os.path.abspath(__file__)))
    saved = (globals()['STATE'], adv3.fapi)
    globals()['STATE'], adv3.fapi = state, fake_fapi
    try:
        top0 = rep0['top'][0]
        r0 = rep0['rows'][top0]
        old = {'utc': '2026-10-29T06:00:00+00:00', 'kind': 'daily', 'close_of': str(last), 'cards': [
            {'coin': top0, 'side': r0['signal'], 'mode': 'market', 'close': r0['close'], 'U': r0['U'] * 0.25,
             'stop': r0['close'] - r0['signal'] * r0['U'] * 0.25}]}
        with open(os.path.join(state, 'journal.jsonl'), 'w', encoding='utf-8') as fh:
            fh.write(json.dumps(old) + '\nnot json\n')
        stub, cap = Stub(cs, funds), Cap()
        with contextlib.redirect_stdout(io.StringIO()):
            e1 = check(cap, stub, (last + adv3.DAY, 'signal'), now0)
            append(e1)
            S_ = r0['close'] - r0['signal'] * r0['U'] * 0.25
            touch = S_ * (0.999 if r0['signal'] > 0 else 1.001)
            forming[top0] = (r0['close'], max(r0['close'], touch), min(r0['close'], touch), r0['close'])
            e2 = check(cap, stub, (last + adv3.DAY, 'fact'), nowf)
            append(e2)
            e3 = check(cap, stub, (last + adv3.DAY, 'fact'), nowf)
        n_sent = len(cap.sent)
        chk('end to end: the signal check sends the full message, quiet with no alert, records 42 states, its cards and the placed coins',
            e1['kind'] == 'check' and e1['slot'] == slot_text((last + adv3.DAY, 'signal')) and not e1['one_line']
            and e1['quiet'] == (not e1['alerts']) == cap.sent[0][1] and len(e1['state']) == 42 and e1['cards']
            and e1['passing'] == [list(x) for x in placed] and all(a['kind'] == 'candidate' for a in e1['alerts'])
            and len(e1['alerts']) == len(placed))
        chk('end to end: the fact check reads the forming candle through the stop of the offer the old daily record made - one loud alert',
            [(a['kind'], a['coin'], a['touch']) for a in e2['alerts']] == [('stop', top0, True)] and e2['quiet'] is False
            and cap.sent[1][1] is False and 'задет сегодня' in cap.sent[1][0] and e2['one_line'] is False)
        chk('end to end: the same fact check again sends no second alert - the offer is closed - and finds the candidates placed before',
            e3['alerts'] == [] and e3['quiet'] is True and n_sent == 3 and not [f for f in e3['followed'] if f['coin'] == top0 and f['close_of'] == str(last)
                                                                                and f['U'] == r0['U'] * 0.25])
        recs2 = list(journal_records())
        chk('end to end: the journal parses past its broken line, holds the old record and the two checks, in order',
            [r['kind'] for r in recs2] == ['daily', 'check', 'check'] and recs2[1]['utc'] == now0.isoformat(timespec='seconds'))

        def fake_make_fail(*a_, **k_):
            raise RuntimeError('fapi.binance.com served no candles')

        cap2 = Cap()
        with contextlib.redirect_stdout(io.StringIO()):
            for text in ('сигнал', 'сигнал топ 7', 'оценка', 'сигнал 10000 топ 3', 'привет'):
                handle(cap2, stub, text)
            kinds = [r['kind'] for r in list(journal_records())[3:]]
            saved_lr = globals()['live_report']
            globals()['live_report'] = fake_make_fail
            try:
                handle(cap2, stub, 'сигнал')
                handle(Cap(down=True), stub, 'сигнал')
            finally:
                globals()['live_report'] = saved_lr
        texts = [t for t, _q in cap2.sent]
        recs3 = list(journal_records())
        chk('handle: «сигнал» three cards, «сигнал топ 7» seven, «оценка» the assessment, the allocation one message, an unknown text HELP',
            texts[0].count('Основание:') == 3 and texts[1].count('Основание:') == 7 and texts[2].startswith('🧭') and 'Оценка доверия' in texts[2]
            and texts[3].startswith('💼') and texts[4] == HELP and all(q is False for _t, q in cap2.sent[:5]))
        chk('handle: the journal holds request, request, assess, alloc, each with its cards; an unknown text no record',
            kinds == ['request', 'request', 'assess', 'alloc'] and recs3[3]['n'] == 3 and recs3[4]['n'] == 7
            and recs3[5]['cards'] == [] and 'trust' in recs3[5] and len(recs3[6]['cards']) == len(placed))
        chk('handle: Binance down gets the apology, Telegram down raises nothing', texts[-1].startswith('Binance или Telegram не ответили'))
    finally:
        globals()['STATE'], adv3.fapi = saved
        shutil.rmtree(state)
    chk('glibc takes its two settings', malloc_tune())
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

```text file=advisor/selftest-adv3.py
#!/usr/bin/env python3
# selftest-adv3.py - the Architect's checks of adv3.py's mechanics on synthetic candles; no network.
# Every expectation is computed here by hand or by an independent formula, never by adv3.py itself.
# TZ-39: the message without its methodology, each card's confidence, the reach shares without survivorship, the assessment.
import datetime as dt, importlib.util, math, os, random

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
check('each card holds its basis and its invalidation, ranks 1 to 3', msg.count('Основание: сумма знаков') == 3
      and msg.count('Инвалидация: цена') == 3 and [cd['rank'] for cd in rep['cards']] == [1, 2, 3])
check('the message carries no methodology: no forward book, no six ratings, no history block, one footer line',
      not any(k in msg for k in ('Форвард с 28.10', 'Оценка доверия', 'Надёжность системы', 'история 2020–2026',
                                 'Прибыль дают редкие', 'Открытые STRONG-сделки')) and msg.rstrip().endswith('на чём держится уверенность</i>'))
check('without current prices each card reads its confidence 0/5, «нет текущей цены»',
      msg.count('Уверенность: <b>0/5</b> — нет текущей цены Binance') == len(rep['cards']) == 3)
ass = a.assessment(rep, a.FACTS)
check('the assessment holds the rung, the next readings, the six ratings, the forward book and the history', all(k in ass for k in (
    'Уверенность: <b>1/5</b> — рубеж 1 из 5', 'после закрытия 28.10.2027', 'после закрытия 31.10.2027', 'Оценка доверия',
    'Надёжность системы: <b>1/5</b>', 'Уверенность в сделках:', 'STRONG обоснован: <b>нет</b>', 'Качество данных: <b>низкое</b>',
    'Ожидаемая R на сделку: <b>не установлена</b>', 'Инвалидация: у каждой карточки', 'Форвард с 28.10', 'Gate H, Gate S'))
      and bool(rep['strong_open']) and 'Открытые STRONG-сделки правила: ' in ass)
check('the assessment quotes STRONG at the random lists\' median and the rule outside the 42, never the 42\'s STRONG mean',
      '+0,22 R' in ass and '+0,04 R' in ass and '0,55' not in ass and '0,5473' not in ass and '+0,16' not in ass)
check('its markup balances and it fits one Telegram message', all(ass.count('<%s>' % t) == ass.count('</%s>' % t) for t in ('b', 'i'))
      and len(ass) <= 4000)
word = {1: 'ЛОНГ', -1: 'ШОРТ'}
rows = rep['rows']
by_hand = ([(c, rows[c]['signal']) for c in a.COINS if rows[c].get('signal') in (1, -1) and rows[c].get('prev') not in (1, -1)],
           [c for c in a.COINS if rows[c].get('signal') not in (1, -1) and rows[c].get('prev') == 1],
           [c for c in a.COINS if rows[c].get('signal') not in (1, -1) and rows[c].get('prev') == -1],
           [(c, rows[c]['signal']) for c in a.COINS if rows[c].get('signal') in (1, -1) and rows[c].get('prev') in (1, -1)
            and rows[c]['signal'] != rows[c]['prev']])
check('changes: the day\'s new, exits and reversals as the rows say', a.changes(rep) == by_hand)
moved = dict(rep, rows=dict(rows, **{a.COINS[0]: dict(rows[a.COINS[0]], prev=-rows[a.COINS[0]]['signal'])}))
check('changes: a reversed coin is a reversal, and the message names it', a.changes(moved)[3] == [(a.COINS[0], rows[a.COINS[0]]['signal'])]
      and f"{a.COINS[0]} в {word[rows[a.COINS[0]]['signal']]}" in a.message(moved, a.FACTS))
framed = a.message(dict(rep, n=7), a.FACTS, head=['HEAD-LINE'], tail=['TAIL-LINE'])
check('head follows the header, tail precedes the other signals, the TOP-N label is the report\'s n',
      framed.index('HEAD-LINE') < framed.index('Изменения за день') < framed.index('ТОП-7 по силе тренда')
      < framed.index('TAIL-LINE') < framed.index('Остальные сигналы'))
bk = rep['book']['base']
check('the book: opened is closed plus open, and the total is the sum of its two parts',
      bk['opened'] == bk['closed'] + bk['open'] and abs(bk['total_R'] - (bk['closed_R'] + bk['open_R'])) < 1e-9)
strong_card = dict(rep['cards'][0], strong=True)
plain_card = dict(rep['cards'][0], strong=False)
check('a STRONG card shows TZ-38\'s STRONG shares without survivorship, 47 / 29 / 19%',
      [l.rsplit('дошли ', 1)[1] for l in a.card_lines(strong_card, a.FACTS) if 'дошли' in l] == ['47%', '29%', '19%'])
check('another card shows the rule\'s shares without survivorship, 23 / 13 / 8%',
      [l.rsplit('дошли ', 1)[1] for l in a.card_lines(plain_card, a.FACTS) if 'дошли' in l] == ['23%', '13%', '8%'])
none_card = dict(rep['cards'][0], mode='none', entry=None)
check('a card with no entry reads 0/5, «входа нет»; without current prices 0/5 «нет текущей цены»; no confidence, no line',
      a.card_lines(none_card, a.FACTS, 0)[-1] == 'Уверенность: <b>0/5</b> — входа нет'
      and a.card_lines(plain_card, a.FACTS, 0)[-1] == 'Уверенность: <b>0/5</b> — нет текущей цены Binance'
      and not any('Уверенность' in l for l in a.card_lines(plain_card, a.FACTS)))

# 7. G-HISTORY's comparison: equal facts read equal, one changed fact reads DIFFERENT
h = {k: {'trades': f['trades'], 'wins': f['wins'], 'mean_R': f['mean_R'] + 1e-6, 'median_days': f['median_days'],
         'mfe': dict(f['mfe']), 'gate_H': f.get('gate_H'), 'gate_S': f.get('gate_S'), 'p_up': f['p_up'] + 1e-6,
         'top5_share': f['top5_share'] - 1e-6} for k, f in a.FACTS.items()}
check('G-HISTORY: 20 facts, all equal', len(a.facts_checks(h)) == 20 and all(ok for ok, _, _ in a.facts_checks(h).values()))
h['strong']['wins'] += 1
check('G-HISTORY: a changed fact reads DIFFERENT', [k for k, (ok, _, _) in a.facts_checks(h).items() if not ok]
      == ['strong wins'])
h['strong']['wins'] -= 1
h['strong']['top5_share'] = None
check('G-HISTORY: a top-5 share not derived reads DIFFERENT, never an error', [k for k, (ok, _, _) in a.facts_checks(h).items()
                                                                              if not ok] == ['strong top-5 share'])

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
check('with current prices each card offering an entry reads the rung, 1/5 «правило не доказано»',
      a.message(rep2, a.FACTS).count('Уверенность: <b>1/5</b> — правило не доказано') == sum(cd['mode'] != 'none' for cd in rep2['cards']) == 3)
check('a card carries its funding interval: 4 h adjusted, 8 h otherwise',
      all(h == (4 if c == a.COINS[0] else 8) for c, h in hours.items()) and rep2['marks_ok'])

# 9. the forward book of check 1's series by hand: one closed stop, one open short that only collects funding
fb = a.forward_book(trades, daily, [pos])
open_R = (-0.001 * 145.0 + 49 * 0.0003 * 145.0) / 16.6   # entry cost at 145; 49 flat days a short is paid 0.03% a day
check('the book of one stop and one open short', fb['opened'] == 2 and fb['closed'] == 1 and fb['stops'] == 1
      and fb['open'] == 1 and fb['days'] == 200)
check('the book: the closed R is the trade\'s by hand, the open R is the short\'s by hand',
      abs(fb['closed_R'] - (-62 - 0.001 * 362 - fund) / 6) < 1e-9 and abs(fb['open_R'] - open_R) < 1e-9)
check('the book: the total over the days is the two parts\' sum', abs(fb['total_R'] - (fb['closed_R'] + fb['open_R'])) < 1e-9)

# 10. the ratings: a function of recorded facts alone
base = {'cards': [{'coin': 'A', 'mode': 'market'}, {'coin': 'B', 'mode': 'none'}, {'coin': 'C', 'mode': 'limit'}],
        'missing': [], 'marks_ok': True, 'close_of': '2026-10-30',
        'made_at_ms': int(dt.datetime(2026, 10, 31, 7, 0, tzinfo=dt.timezone.utc).timestamp() * 1000)}
tr = a.trust(base)
check('trust: the system 1, a trade the system\'s or 0 where no entry is offered, STRONG not justified',
      tr['system'] == 1 and tr['cards'] == {'A': 1, 'B': 0, 'C': 1} and tr['strong_justified'] is False)
check('trust: quality low while unproven, the expectancy not established, the close of the day before fresh',
      tr['quality'] == 'low' and not tr['expectancy_established'] and tr['served'] == len(a.COINS) and tr['fresh'])
check('trust: a close two days old, or a report with no instant, is not fresh',
      not a.trust(dict(base, close_of='2026-10-29'))['fresh'] and not a.trust(dict(base, made_at_ms=0))['fresh'])
check('trust: no mark prices, no trade confidence', set(a.trust(dict(base, marks_ok=False))['cards'].values()) == {0})
a.RELIABILITY = 4
try:
    t4 = a.trust(base)
    t4m = a.trust(dict(base, missing=['XMR']))
    t4s = a.trust(dict(base, close_of='2026-10-29'))
finally:
    a.RELIABILITY = 1
check('trust at reliability 4: quality high where fresh and complete, medium where a coin is missing or the close is old, '
      'the expectancy established', t4['quality'] == 'high' and t4m['quality'] == 'medium' and t4s['quality'] == 'medium'
      and t4['expectancy_established'] and t4m['served'] == 41)

print(f'SELFTEST-ADV3 PASS: {len(CHECKS)} of {len(CHECKS)} checks passed')
```

```text file=research/tz39-advisor-checks.py
#!/usr/bin/env python3
# tz39-advisor-checks.py - TZ-39's checker: the fingerprint, the host gate, the number, G-RULE, COPY, G-RENDER, the readings
# after the unit's restart - UNIT-NEW and G-FIRST - and the marks. Standard library only. It starts and stops no unit, signals no
# process and sends no request of its own (G-RENDER runs the service copy's bot, which reads Binance's public market), and it
# never reads or prints the bot's token or the pinned chat, a coin, a price or a size. Exits: 0 every assert held; 1 a failed
# assert, named; 3 NOT YET.
import ast, bisect, calendar, contextlib, datetime as dt, hashlib, importlib.util, io, json, math, os, re, shutil, subprocess, \
    sys, time

WORK = '/root/tz39-work'
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
TZ_FILE = 'CryptoTZ/TZ-39-advisor-checks.md'
NUMBER = 'TZ-39-'
BRANCH = 'tz-39-advisor-checks'
MAP_REV = '2026-10-31-c'
ANCHORS = {'A1': '229a944f2d51', 'A2': '6c5089330629',
           'A3': '0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable',
           'A4': '437b45ea196b', 'A5': '0f6c90451cbd', 'A6': '729f0bcdbee3'}
DERIVED = {'A2': 'research/twap-divergence.py', 'A4': 'BTC-EXECUTOR-INSTRUCTIONS.md',
           'A5': 'research/recorder/recorder.py', 'A6': 'research/pfair.py'}
H = {'adv3_old': 'd73a657ef31decad276b858c4ec9672dce1c1c5cec36f0bb1c5b3378838224a8',
     'adv3_new': 'c19572dccf30a505342ca334e42c7ec347a5d29db4db20887229d2a8c7b48e31',
     'bot_old': '3a044d50f51b16563b99bf1514ef92f35a9795b1fcc377aea6be4c23a31f7af2',
     'bot_new': 'ca989b6fe487d41181b32312418d6acda1e9c64fbf5cfbb3f041d54826dd108f',
     'selftest_old': 'ef4ffc44e6f8bcdd5685fc1db9090957890c6e2ab762cdad8ae9826b18cf1395',
     'selftest_new': '09d2ba9a8361ec5ebc7f5934ebb818d1a685bb16fb3f32b7da94409d9516cc0e',
     'rule': 'ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169',
     'unit': '82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66'}
TZ38 = ('CryptoReports/TZ-38-adv3-pit-validation-report.md', 'f4a0ac3f643ac99dd08f20c8c8c43bf1e98e51b2954592d1456a59ae98030528')
# G-RULE's tables: (changed, added, removed) definitions and assignments of each file against origin/main's
ADV3_DEFS = ({'card_lines', 'message', 'trust_lines'}, {'assessment', 'changes'}, set())
ADV3_RULE = ('signs', 'signal', 'strength', 'true_range', 'unit', 'open_at', 'hold', 'close_at', 'simulate', 'states', 'ranking',
             'simulate_strong', 'stats', 'funding_of')
ADV3_ASG = (set(), {'PIT', 'LADDER'}, set())
BOT_DEFS = ({'Telegram', 'handle', 'hello', 'make', 'plan_parts', 'probe', 'route', 'selftest', 'serve'},
            {'alerted', 'alerts_of', 'append', 'base_record', 'candidate_lines', 'candidates', 'check', 'check_record', 'compose',
             'done_after', 'due', 'event_lines', 'follow', 'followed_lines', 'forming_candles', 'hhmm', 'item_lines',
             'journal_records', 'journal_scan', 'latest_slot', 'live_report', 'next_at', 'offers', 'quiet_line', 'ranked', 'slot_at',
             'slot_key', 'slot_parse', 'slot_text', 'strong_shares', 'top_n', 'weak_lines', 'weakened', 'zone_lines', 'zones_left'},
            {'journal'})
BOT_ASG = ({'(STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, CROWD, Z_CAP, LIQ_DAYS)', 'HELP'},
           {'(SIDE, DOT)', 'ASSESS', 'BATUMI', 'CARD_KEYS', 'FOOTER', 'LIST_MAX', 'SLOTS'}, {'DAILY'})
# this TZ's numbers: the allocation's limits, the list's length, the two checks' instants, the rung
STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, RISK_MAX, RISK_ALL, LIST_MAX, RUNG = 14.0, 5.0, 0.001, 1.0, 5.0, 7, 1
SLOTS = (('signal', dt.time(0, 10)), ('fact', dt.time(12, 10)))
MEM_FLOOR, DISK_FLOOR = 130_981_888, 7_400_000_000
ROWS, FROZEN = 58, 55
FIRST_BOUND = 900
RENDER_CASES = ('сигнал', 'сигнал топ 7', 'сигнал 10000 топ 3', 'сигнал 15000 топ 5', 'оценка', 'помощь', 'привет')
RENDER_KINDS = ['request', 'request', 'alloc', 'alloc', 'assess', 'check', 'check']
TRUST = ('Оценка доверия', 'Надёжность системы: <b>1/5</b>', 'Уверенность в сделках:', 'STRONG обоснован: <b>нет</b>',
         'Качество данных: <b>низкое</b>', 'Ожидаемая R на сделку: <b>не установлена</b>', 'Инвалидация: у каждой карточки')
METHOD = ('Оценка доверия', 'Надёжность системы', 'Форвард с 28.10', 'история 2020–2026', 'Открытые STRONG-сделки')
TRUST_KEYS = {'system', 'strong_justified', 'served', 'cards', 'quality', 'fresh', 'complete', 'expectancy_established'}
CARD = re.compile(r'^[🟢🔴] <b>[A-Z0-9]+ · (LONG|SHORT)</b>', re.M)
CONF = re.compile(r'^Уверенность: <b>([0-5])/5</b> — ', re.M)
DAY = dt.timedelta(days=1)


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
                                                  ', the %d rule functions among them' % len(rule) if rule else ''):
            set(same) == set(od) - defs[0] - defs[2] and all(k in same for k in rule),
        '%s: the assignments changed are exactly %s, added %s, removed %s' % (label, sorted(asg[0]), sorted(asg[1]), sorted(asg[2])):
            ({k for k in oa if k in na and oa[k] != na[k]}, set(na) - set(oa), set(oa) - set(na)) == asg,
    }


def report_sections(text):
    """{heading: {first cell: [the other cells]}} of every '#### ' section's table rows, a cell's backticks stripped."""
    out_, name = {}, None
    for line in text.split('\n'):
        if line.startswith('#### '):
            name = line[5:].strip()
            out_[name] = {}
        elif name and line.startswith('| ') and not line.startswith('|---'):
            cells = [c.strip().strip('`') for c in line.strip().strip('|').split('|')]
            out_[name].setdefault(cells[0], cells[1:])
    return out_


def pit_from_report(text):
    """adv3.PIT as TZ-38's report prints it (§2.7): E4's reach shares and STRONG's top-5 share, E1's rule on G, E2's p, E5's
    median and its share of lists in profit, the size of G - each cell read as a number."""
    sec = report_sections(text)
    pick = lambda prefix: next(v for k, v in sec.items() if k.startswith(prefix))
    e1, e2, e4, e5, sets = pick('E1 '), pick('E2 '), pick('E4 '), pick('E5 '), pick('The sets ')
    f = lambda s: float(s.replace(',', ''))
    return {'base': {'mfe': {n: f(e4['mfe +%dR' % n][0]) for n in (1, 2, 3)}, 'mean_R_G': f(e1['mean_R'][0]),
                     'trades_G': int(f(e1['trades'][0])), 'p_G': f(e1['p_t_up'][0]), 'contracts_G': int(f(sets['G'][0]))},
            'strong': {'mfe': {n: f(e4['mfe +%dR' % n][1]) for n in (1, 2, 3)}, 'p_G': f(e2['p_t_up'][0]),
                       'mean_R_lists': f(e5['0.5'][1]), 'lists': int(f(e5['lists'][0])),
                       'lists_positive': f(e5['share_mean_R_positive'][0]), 'top5_share': f(e4['top5_share'][1])}}


def html_balanced(text):
    return all(text.count('<%s>' % t) == text.count('</%s>' % t) for t in ('b', 'i'))


def plan_invariants(p, rep, liq, budget, n):
    """The allocation's limits, read from a plan (the bot's own) and the report and liquidity it was made from. The limits are
    this checker's, the TZ's: stop 14 %, minimum 5 USDT, liquidity 0.1 %, risk 1 % a trade and 5 % in all, three places."""
    items = p['items']
    coins = [it['card']['coin'] for it in items]
    strong = [c for c in rep['top'] if c in rep['strong']]
    named = [r[0] for r in p['rejected']]
    return {
        'only STRONG coins of the report, in rank order, at most n and at most three, none added to fill': (
            set(coins) <= set(strong) and coins == [c for c in strong if c in coins] and len(coins) <= min(n, 3)),
        'every STRONG coin is in the plan or named with a reason, once': sorted(coins + named) == sorted(strong),
        'every position has an entry and a stop within 14 % of it, on current prices': (
            all(it['card']['entry'] is not None and it['card']['stop_pct'] <= STOP_MAX for it in items) and (rep['marks_ok'] or not items)),
        'each loss at its stop within 1 % of the budget, all together within 5 %': (
            all(it['loss_exact'] <= budget * RISK_MAX / 100 + 1e-9 for it in items)
            and sum(it['loss_exact'] for it in items) <= budget * RISK_ALL / 100 + 1e-9),
        'whole positions of at least 5 USDT, together within the budget, free the budget less them': (
            all(float(it['notional']).is_integer() and it['notional'] >= MIN_NOTIONAL for it in items)
            and p['allocated'] == sum(it['notional'] for it in items) <= budget and p['free'] == budget - p['allocated']),
        'leverage the rule\'s formula and at most 20, the margin covering the position, a position within its liquidity cap': all(
            it['leverage'] == min(20, math.floor(1 / (1.5 * it['card']['stop_pct'] / 100 + 0.01)))
            and it['margin'] * it['leverage'] >= it['notional']
            and ((not liq.get(it['card']['coin'])) or it['notional'] <= LIQ_FRAC * liq[it['card']['coin']]) for it in items),
    }


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


def walk(c, side, close_of, stop, last):
    """An offer's fate by this checker's own reading of the rule: from the day after its close, a candle reaching the stop ends
    it there; else a close whose sum of signs leaves the side - below +2 for a long, above -2 for a short - ends it at that close.
    ('stop' | 'signal' | 'open' | 'unknown', day)."""
    D = dt.date.fromisoformat(close_of)
    days = sorted(d for d in c if d <= last)
    if D not in c:
        return 'unknown', None
    closes = [c[d][3] for d in days]
    for i in range(days.index(D) + 1, len(days)):
        _o, h, l, _c = c[days[i]]
        if (l <= stop) if side > 0 else (h >= stop):
            return 'stop', str(days[i])
        s = sign_sum(days, closes, i)
        if s is None or (s < 2 if side > 0 else s > -2):
            return 'signal', str(days[i])
    return 'open', None


def alert_checks(run, cs, prev_passing):
    """One check's alerts read against this checker's own walk of every offer the journal held before it: each stop, touch and
    signal alert is an offer's first exit by the walk (or the forming candle through its stop), each such exit not alerted
    before is alerted, and each candidate is a STRONG coin the plan places that the check before did not."""
    offs, done, _prev = run['scan']
    rec, last, forming = run['rec'], run['last'], run['forming']
    want = []
    for key, off in offs.items():
        coin, side, close_of = key
        if (coin, side, close_of, 'stop') in done or (coin, side, close_of, 'signal') in done:
            continue
        state, day = walk(cs.get(coin) or {}, side, close_of, off['stop'], last)
        if state == 'open' and forming.get(coin):
            _o, h, l, _c = forming[coin]
            if (l <= off['stop']) if side > 0 else (h >= off['stop']):
                state, day = 'touch', str(last + DAY)
        if state in ('stop', 'touch', 'signal'):
            want.append(('stop' if state == 'touch' else state, coin, side, close_of, day, state == 'touch'))
    got = [(a['kind'], a['coin'], a['side'], a['close_of'], a['day'], a['touch']) for a in rec['alerts'] if a['kind'] != 'candidate']
    placed = [(it['card']['coin'], it['card']['side']) for it in run['plan']['items']]
    cand = [(a['coin'], a['side']) for a in rec['alerts'] if a['kind'] == 'candidate']
    return sorted(got) == sorted(want) and cand == [x for x in placed if x not in prev_passing]


def render_checks(texts, calc, runs, kinds, records, log, same, expect):
    """G-RENDER: what the service copy's bot sent for each command (texts, by command), the plan the checker recomputed from the
    report and liquidity each allocation reply was made from (calc), the two checks run on live data (runs), the scratch
    journal's kinds and records, the bot's log, whether the bot's own record is as before, and the bot module's constants
    (expect); counts and labels only."""
    whole = lambda parts: '\n'.join(parts)
    sig, top7, ass = whole(texts[RENDER_CASES[0]]), whole(texts[RENDER_CASES[1]]), whole(texts[RENDER_CASES[4]])
    allocs = [c for c in RENDER_CASES if c in calc]
    usdt = expect['usdt']
    inv = {c: plan_invariants(calc[c]['plan'], calc[c]['rep'], calc[c]['liq'], calc[c]['budget'], calc[c]['n']) for c in allocs}

    def fields(c):
        p, t = calc[c]['plan'], whole(texts[c])
        head = ('не доказанная' in t and 'Бюджет %s USDT' % expect['num'](p['budget'], 6) in t and 'Размещено %s USDT' % usdt(p['allocated']) in t
                and ('Свободно %s USDT' % usdt(p['free']) in t or 'свободно %s USDT' % usdt(p['free']) in t) and 'Оценка доверия' not in t)
        if not p['items']:
            return head and 'Подходящих сделок нет' in t
        k = len(p['items'])
        return (head and 'Подходящих сделок: %d из %d запрошенных' % (k, p['n']) in t
                and all(t.count(m) == k for m in ('Капитал:', 'Потеря на стопе:', '⛔ Стоп:', 'Инвалидация: цена', 'Качество: z'))
                and t.count('🎯') == 3 * k and t.count('размеры — формула Архитектора, не доказана') == k
                and 'Потеря на стопах %s USDT' % usdt(p['loss']) in t and 'маржа %s USDT' % usdt(p['margin']) in t)

    def cards_ok(text, most, n_of):
        heads = CARD.findall(text)
        conf = CONF.findall(text)
        return (len(heads) <= most and text.count('Основание: сумма знаков') == len(heads) == text.count('Инвалидация: цена')
                == len(conf) and all(int(v) in (0, RUNG) for v in conf) and all(('ранг %d из %d' % (k, n_of)) in text for k in range(1, len(heads) + 1)))

    strong7 = [block.split('\n')[0] for block in top7.split('\n\n') if CARD.match(block)]
    sg, fa = runs.get('signal'), runs.get('fact')

    def run_shape(r, kind):
        rec, sent = r['rec'], r['sent']
        alerts = rec['alerts']
        loud = bool(alerts)
        flags = all(q == rec['quiet'] for _t, q in sent) and rec['quiet'] == (not loud) and len(sent) >= 1
        text = whole(t for t, _q in sent)
        if rec['one_line']:
            shape = (not loud and len(sent) == 1 and '\n' not in text and text.startswith('✓ ') and rec['cards'] == []
                     and (kind == 'fact' and not rec['zones_left'] or kind == 'signal' and not r['changes'] and r['same'] and not rec['weakened']))
        elif kind == 'signal':
            shape = ('STRONG-канд' in text and 'Сделки по карточкам бота' in text and not any(m in text for m in METHOD)
                     and [c['coin'] for c in rec['cards']] == r['rep']['top'] and cards_ok(text, 3, 3)
                     and (loud or r['changes'] or not r['same'] or bool(rec['weakened'])) and (('🔔 <b>События</b>' in text) == loud)
                     and (('ℹ️ Ослабление' in text) == bool(rec['weakened'])))
        else:
            shape = (('🔔 <b>События</b>' in text) == loud and (loud or bool(rec['zones_left'])) and CARD.findall(text) == []
                     and [(c['coin'], c['side']) for c in rec['cards']] == [(a['coin'], a['side']) for a in alerts if a['kind'] == 'candidate'])
        return flags and shape and html_balanced(text)

    def record_ok(r, kind):
        rec = r['rec']
        return (rec['kind'] == 'check' and rec['slot'].endswith(' ' + kind) and len(rec['state']) == 42 and TRUST_KEYS <= set(rec['trust'])
                and rec['rule'] == H['rule'] and rec['close_of'] == r['rep']['close_of'] and rec['passing'] == [list(x) for x in
                [(it['card']['coin'], it['card']['side']) for it in r['plan']['items']]]
                and all(rec['state'][c]['rank'] is not None for c in r['rep']['top']))

    return {
        'every command and both checks answered, no traceback and no failed request in the bot\'s log':
            all(texts[k] for k in RENDER_CASES) and sg is not None and fa is not None and 'Traceback' not in log and 'failed' not in log,
        'the markup is balanced in every message (b, i)': all(html_balanced(t) for ps in texts.values() for t in ps),
        '«сигнал»: at most three cards, each with its basis, invalidation and confidence - the rung 1 or 0 - and no methodology':
            cards_ok(sig, 3, 3) and not any(m in sig for m in METHOD) and 'на чём держится уверенность' in sig,
        '«сигнал топ 7»: at most seven cards ranked of 7, each with its confidence, STRONG only among the first three':
            cards_ok(top7, 7, 7) and 'ТОП-7 по силе тренда' in top7 and not any('★ STRONG' in h for h in strong7[3:]),
        '«оценка»: the rung and the next readings, the six ratings, the forward record; STRONG at the lists\' median, never the 42\'s':
            all(k in ass for k in TRUST + ('рубеж 1 из 5', 'после закрытия 28.10.2027', 'после закрытия 31.10.2027', 'Форвард с 28.10'))
            and '+0,22 R' in ass and '+0,04 R' in ass and '0,55' not in ass,
        'the bot\'s constants are this TZ\'s: 14 % a stop, 5 USDT, 0.1 % of the volume, 1 % and 5 % of risk, three places, 0.1 % a side, '
        'a list of 7, checks at 00:10 and 12:10 UTC, the rung 1': expect['consts'] == (STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, RISK_MAX, RISK_ALL, 3,
                                                                                     0.001, LIST_MAX, SLOTS, RUNG),
        'each allocation reply is the bot\'s own plan_parts of the report and liquidity it was made from':
            len(allocs) == 2 and all(texts[c] == calc[c]['parts'] for c in allocs),
        'plan: only STRONG coins of the report, in rank order, at most n and at most three, none added to fill':
            all(v['only STRONG coins of the report, in rank order, at most n and at most three, none added to fill'] for v in inv.values()),
        'plan: every STRONG coin is in the plan or named with a reason, once':
            all(v['every STRONG coin is in the plan or named with a reason, once'] for v in inv.values()),
        'plan: every position has an entry and a stop within 14 % of it, on current prices':
            all(v['every position has an entry and a stop within 14 % of it, on current prices'] for v in inv.values()),
        'plan: each loss at its stop within 1 % of the budget, all together within 5 %':
            all(v['each loss at its stop within 1 % of the budget, all together within 5 %'] for v in inv.values()),
        'plan: whole positions of at least 5 USDT, together within the budget, free the budget less them':
            all(v['whole positions of at least 5 USDT, together within the budget, free the budget less them'] for v in inv.values()),
        'plan: leverage the rule\'s formula and at most 20, the margin covering the position, a position within its liquidity cap':
            all(v['leverage the rule\'s formula and at most 20, the margin covering the position, a position within its liquidity cap'] for v in inv.values()),
        'the Boss\'s fields in each allocation reply - budget, count, allocated, free, and for each trade capital, leverage, margin, loss, '
        'stop, targets, invalidation and its confidence with the note that the sizes are unproven - and no six ratings':
            len(allocs) == 2 and all(fields(c) for c in allocs),
        '«сигнал 15000 топ 5» says that STRONG is at most three': 'больше 3 сделок не будет' in whole(texts[RENDER_CASES[3]]),
        '«помощь» and an unknown text answer HELP and nothing else': texts[RENDER_CASES[5]] == [expect['help']] == texts[RENDER_CASES[6]],
        'the signal check: quiet exactly when it holds no alert, one line only where it finds nothing, else the close\'s cards, '
        'candidates and offered trades': sg is not None and run_shape(sg, 'signal'),
        'the fact check: quiet exactly when it holds no alert, one line where it finds neither an alert nor a zone left, no card but '
        'a new candidate\'s': fa is not None and run_shape(fa, 'fact'),
        'the alerts of both checks are the exits of the offered trades by this checker\'s own walk, each once, and the new candidates':
            sg is not None and fa is not None and alert_checks(sg, sg['cs'], sg['prev_passing']) and alert_checks(fa, fa['cs'], fa['prev_passing'])
            and not ({(a['kind'], a['coin'], a['side'], a['close_of']) for a in sg['rec']['alerts'] if a['kind'] != 'candidate'}
                     & {(a['kind'], a['coin'], a['side'], a['close_of']) for a in fa['rec']['alerts'] if a['kind'] != 'candidate'}),
        'the check records: their slots, every coin\'s state with the TOP-3 ranked, the six ratings, the placed coins':
            sg is not None and fa is not None and record_ok(sg, 'signal') and record_ok(fa, 'fact'),
        'the scratch journal holds, after the bot\'s own records, request, request, alloc, alloc, assess, check, check':
            kinds == RENDER_KINDS and all(r.get('cards') is not None for r in records),
        'the bot\'s own journal, offset and daily-sent are as before the run, and no check-done file was written': same is True,
    }


def unit_checks(which, pre, now):
    """UNIT-NEW and UNIT-OLD's nine readings after a restart: now is what the modes read; pre is the snapshot of the kill mark."""
    want = (H['adv3_new'], H['bot_new']) if which == 'new' else (H['adv3_old'], H['bot_old'])
    return {
        'the unit is active, running and enabled': (now['bot']['ActiveState'], now['bot']['SubState'],
                                                    now['bot']['UnitFileState']) == ('active', 'running', 'enabled'),
        'a new MainPID, one restart more': int(now['bot']['MainPID']) not in (0, int(pre['bot']['MainPID']))
        and int(now['bot']['NRestarts']) == int(pre['bot']['NRestarts']) + 1,
        'the process started after the kill mark and within 90 s of it': pre['t'] <= now['start'] <= pre['t'] + 90,
        'the process runs the unit\'s exact argv, alone': now['argv'] == ARGV and now['procs'] == [int(now['bot']['MainPID'])],
        'the service copy\'s adv3.py and adv3-bot.py are the %s ones, and the process started after the copy' % which:
            (now['sha_adv3'], now['sha_bot']) == want and now['start'] > now['copy_t'],
        'the unit file is unchanged': now['sha_unit'] == H['unit'],
        'no daily record since the mark': now['daily'] == pre['daily'],
        'the log shows the new process serving and no traceback since the mark': now['serving'] and not now['traceback'],
        'the three capture units unchanged, each active': all(
            now['caps'][u]['ActiveState'] == 'active' and now['caps'][u]['MainPID'] == pre['caps'][u]['MainPID']
            and now['caps'][u]['NRestarts'] == pre['caps'][u]['NRestarts'] for u in CAPTURES),
    }


def first_checks(pre, recs, done_text, log, pid, tail_ok):
    """G-FIRST: the new process's first check, from the journal's records stamped after the kill mark, the check-done file and
    service.log's lines since the mark."""
    t0 = dt.datetime.fromtimestamp(pre['t'], dt.timezone.utc)
    day = t0.date()
    checks_ = [r for r in recs if r.get('kind') == 'check']
    r = checks_[0] if checks_ else {}
    want_done = '%s %s' % (day, 'fact' if t0.time() >= SLOTS[1][1] else 'signal')
    return {
        'exactly one check record since the mark': len(checks_) == 1,
        'it is the day\'s signal check, of the close of the day before, under rule ee206e7c': (
            r.get('slot') == '%s signal' % day and r.get('close_of') == str(day - DAY) and r.get('rule') == H['rule']),
        'it was sent: its Telegram message ids': bool(r.get('message_ids')) and all(isinstance(x, int) for x in r.get('message_ids') or ['x']),
        'it holds the 42 coins\' state, the six ratings, its alerts and its placed coins, quiet exactly without an alert': (
            len(r.get('state') or {}) == 42 and TRUST_KEYS <= set(r.get('trust') or {}) and isinstance(r.get('alerts'), list)
            and isinstance(r.get('passing'), list) and r.get('quiet') == (not r.get('alerts'))),
        'check-done names the slot it covers: %s' % want_done: done_text == want_done,
        'the log since the mark: the new process serving from no check-done, the check sent, no check failed and no traceback': (
            ('serving the pinned chat: pid %d ' % pid in log and 'check-done -' in log) and 'check sent: %s signal' % day in log
            and 'check failed' not in log and 'Traceback' not in log),
        'the journal ends in a newline and every line since the mark parses': tail_ok,
    }


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


def records_since(text, t0):
    """The journal's records from the first stamped at or after t0 less 1 s, and whether the text ends in a newline with every
    line from that record on parsing."""
    recs, ok, on = [], text.endswith('\n') or text == '', False
    for line in text.splitlines():
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


def memory_gate(first, second):
    """The memory gate: MemAvailable at the first read, and at the second, 60 s later, taken only where the first fell
    below MEM_FLOOR; the second decides. Returns (passes, the read that decided)."""
    final = first if first >= MEM_FLOOR or second is None else second
    return final >= MEM_FLOOR, final


def count_kind(text, kind):
    """How many records of a kind a journal.jsonl text holds; a broken line left out."""
    n = 0
    for line in text.splitlines():
        try:
            n += json.loads(line).get('kind') == kind
        except (ValueError, AttributeError):
            pass
    return n


def number_reading(names):
    return {'CryptoTZ/ holds %s and no other file of that number' % TZ_FILE:
            [n for n in names if n.startswith('CryptoTZ/' + NUMBER)] == [TZ_FILE],
            'CryptoReports/ holds no report of that number': not [n for n in names if n.startswith('CryptoReports/' + NUMBER)]}


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
    checks['H5 adv3.py is TZ-36\'s and adv3-bot.py is TZ-37\'s'] = (
        sha256_file(SVC + '/adv3.py') == H['adv3_old'] and sha256_file(SVC + '/adv3-bot.py') == H['bot_old'])
    checks['H5 the installed unit file is TZ-35\'s'] = sha256_file('/etc/systemd/system/adv3-bot.service') == H['unit']
    checks['H5 commit.txt is 40 hex characters and a newline'] = re.fullmatch(r'[0-9a-f]{40}\n', read(SVC + '/commit.txt')) is not None
    checks['H6 the record holds a journal of whole lines and no check-done file'] = (
        read(BOTDIR + '/journal.jsonl', 'rb').endswith(b'\n') and not os.path.exists(BOTDIR + '/check-done'))
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
    report = git_show(TZ38[0]).encode()
    pit = load_module('adv3_branch', WT + '/advisor/adv3.py').PIT
    checks = {
        'RULE-ADV-3.txt is main\'s, byte for byte, hashes to the RULE constant, and is the branch\'s adv3.py\'s':
            rule_txt == git_show('advisor/RULE-ADV-3.txt').encode() and sha256_bytes(rule_txt) == H['rule']
            and ("RULE = '%s'" % H['rule']) in read(WT + '/advisor/adv3.py'),
        'the unit file is main\'s, byte for byte, and hashes to TZ-35\'s': unit == git_show('deploy/systemd/adv3-bot.service').encode()
            and sha256_bytes(unit) == H['unit'],
    }
    checks.update(tree_checks('adv3.py', git_show('advisor/adv3.py'), read(WT + '/advisor/adv3.py'), ADV3_DEFS, ADV3_ASG, ADV3_RULE))
    checks['adv3.py\'s PIT is TZ-38\'s report as committed (%s…), cell for cell' % TZ38[1][:8]] = (
        sha256_bytes(report) == TZ38[1] and pit == pit_from_report(report.decode('utf-8')))
    checks.update(tree_checks('adv3-bot.py', git_show('advisor/adv3-bot.py'), read(WT + '/advisor/adv3-bot.py'), BOT_DEFS, BOT_ASG))
    checks['the branch\'s adv3.py, adv3-bot.py and selftest-adv3.py are Appendix A\'s'] = (
        sha256_file(WT + '/advisor/adv3.py'), sha256_file(WT + '/advisor/adv3-bot.py'), sha256_file(WT + '/advisor/selftest-adv3.py')) == (
        H['adv3_new'], H['bot_new'], H['selftest_new'])
    verdict('RULE', checks)


def snapshot():
    """What a mark records: the instant, the bot's and the captures' units, the record's daily and check counts and its files."""
    text = read(BOTDIR + '/journal.jsonl')
    return {'t': time.time(), 'bot': show(BOT, 'MainPID', 'NRestarts', 'ActiveState'),
            'caps': {u: show(u, 'MainPID', 'NRestarts', 'ActiveState') for u in CAPTURES},
            'daily': count_kind(text, 'daily'), 'checks': count_kind(text, 'check'), 'lines': text.count('\n'),
            'check_done': read(BOTDIR + '/check-done').strip() if os.path.exists(BOTDIR + '/check-done') else None}


def mode_mark(name):
    """A mark: the snapshot, kept in state.json. kill and kill2 refuse where the old code's message of the UTC day was not sent -
    daily-sent not today - so that a rollback's restart of the old code finds that message sent, as UNIT-OLD reads it."""
    assert name in ('deploy', 'kill', 'rollback', 'kill2'), name
    st = load_state()
    snap = snapshot()
    if name in ('kill', 'kill2'):
        today, sent = time.strftime('%Y-%m-%d', time.gmtime()), read(BOTDIR + '/daily-sent').strip()
        assert sent == today, 'the old code\'s message of the day is not sent: daily-sent %s, today %s' % (sent, today)
    st.setdefault('marks', {})[name] = snap
    save_state(st)
    out('mark %s at %s: bot pid %s NRestarts %s, %d daily and %d check records, check-done %s' % (
        name, time.strftime('%FT%TZ', time.gmtime(snap['t'])), snap['bot']['MainPID'], snap['bot']['NRestarts'], snap['daily'],
        snap['checks'], snap['check_done'] or '-'))


def mode_copy():
    rc, head, _ = sh(['git', '-C', WT, 'rev-parse', 'HEAD'])
    rc2, up, _ = sh(['git', '-C', WT, 'rev-parse', 'origin/' + BRANCH])
    commit = read(SVC + '/commit.txt')
    verdict('COPY', {
        'the service copy holds adv3.py, adv3-bot.py and commit.txt only': sorted(os.listdir(SVC)) == ['adv3-bot.py', 'adv3.py', 'commit.txt'],
        'adv3.py is Appendix A\'s': sha256_file(SVC + '/adv3.py') == H['adv3_new'],
        'adv3-bot.py is Appendix A\'s': sha256_file(SVC + '/adv3-bot.py') == H['bot_new'],
        'commit.txt is the branch head and the worktree\'s HEAD': (
            re.fullmatch(r'[0-9a-f]{40}\n', commit) is not None and rc == 0 and rc2 == 0 and commit.strip() == head.strip() == up.strip()),
        'the branch\'s two files equal the service copy\'s': all(read(WT + '/advisor/' + f, 'rb') == read(SVC + '/' + f, 'rb')
                                                               for f in ('adv3.py', 'adv3-bot.py')),
    })


def own_files():
    return tuple(maybe_sha(BOTDIR + '/' + f) for f in ('journal.jsonl', 'offset', 'daily-sent', 'check-done'))


def render_run(mod, data, now):
    """G-RENDER's pipeline on a loaded bot and a Data: the commands answered through the bot's handle, then the signal check and
    the fact check through its check, each appended to its STATE's journal; Telegram a stand-in, the reports, volumes and forming
    candles the bot read captured, and each allocation's plan recomputed by the bot's plan from the very report and volumes its
    reply was made from. (texts, calc, runs, records, log, expect)."""
    base_lines = read(mod.STATE + '/journal.jsonl').count('\n')

    class Cap(mod.Telegram):
        def __init__(self):
            super().__init__('123456:SECRET', 777)
            self.sent = []

        def call(self, method, http_timeout=30, **params):
            self.sent.append((params['text'], params.get('disable_notification', False)))
            return {'message_id': len(self.sent)}

    cap, texts, calc, seen, liqs, formed, runs = Cap(), {}, {}, [], {}, {}, {}
    real_lr, real_liq, real_form = mod.live_report, mod.liquidity, mod.forming_candles

    def lr_seen(d, deposit, risk):
        r = real_lr(d, deposit, risk)
        seen.append(r)
        return r

    def liq_seen(coin, now_ms):
        liqs[coin] = real_liq(coin, now_ms)
        return liqs[coin]

    def form_seen(coins, day):
        got = real_form(coins, day)
        formed.update(got)
        return got

    mod.live_report, mod.liquidity, mod.forming_candles = lr_seen, liq_seen, form_seen
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            for case in RENDER_CASES:
                n0, m0 = len(cap.sent), len(seen)
                liqs.clear()
                mod.handle(cap, data, case)
                texts[case] = [t for t, _q in cap.sent[n0:]]
                cmd = mod.route(case)
                if cmd and cmd[0] == 'alloc' and len(seen) == m0 + 1:
                    _k, budget, n, risk = cmd
                    rep = mod.top_n(seen[-1], mod.adv3.TOP_N)
                    p = mod.plan(rep, data.cs, budget, n, risk, dict(liqs))
                    calc[case] = {'rep': rep, 'liq': dict(liqs), 'plan': p, 'budget': budget, 'n': n, 'parts': mod.plan_parts(rep, p)}
            for kind in ('signal', 'fact'):
                scan = mod.journal_scan()
                n0, m0 = len(cap.sent), len(seen)
                liqs.clear()
                formed.clear()
                rec = mod.check(cap, data, (now.date(), kind), now)
                mod.append(rec)
                rep = mod.top_n(seen[m0], mod.adv3.TOP_N)
                p = mod.plan(rep, data.cs, mod.adv3.DEPOSIT, mod.adv3.TOP_N, mod.adv3.RISK, dict(liqs))
                prev, rows = scan[2], rep['rows']
                runs[kind] = {'rec': rec, 'sent': cap.sent[n0:], 'scan': scan, 'rep': rep, 'plan': p, 'forming': dict(formed),
                              'last': dt.date.fromisoformat(rep['close_of']), 'cs': data.cs,
                              'prev_passing': {(c, s) for c, s in (prev or {}).get('passing') or []},
                              'changes': any(rows[c].get('signal') != rows[c].get('prev')
                                             and (rows[c].get('signal') in (1, -1) or rows[c].get('prev') in (1, -1)) for c in mod.adv3.COINS),
                              'same': prev is not None and prev.get('top') == rep['top'] and prev.get('strong') == rep['strong']
                              and all((prev.get('signals') or {}).get(c) == rows[c].get('signal') for c in rep['top'])}
    finally:
        mod.live_report, mod.liquidity, mod.forming_candles = real_lr, real_liq, real_form
    records = [json.loads(line) for line in read(mod.STATE + '/journal.jsonl').splitlines()[base_lines:]]
    m = mod.adv3
    expect = {'help': mod.HELP, 'usdt': m.usdt, 'num': m.num,
              'consts': (mod.STOP_MAX, mod.MIN_NOTIONAL, mod.LIQ_FRAC, m.RISK_MAX, m.RISK_ALL, m.TOP_N, m.COST, mod.LIST_MAX, mod.SLOTS,
                         m.RELIABILITY)}
    return texts, calc, runs, records, buf.getvalue(), expect


def render_print(texts, calc, runs, seen_strong, log):
    """What G-RENDER prints: sizes, counts and labels, never a coin, a price or a size."""
    out('replies: %s; the bot\'s log: %d lines; STRONG coins: %d; trades placed per allocation: %s' % (
        ', '.join('%d chars in %d parts' % (sum(map(len, texts[k])), len(texts[k])) for k in RENDER_CASES), log.count('\n'),
        seen_strong, ', '.join(str(len(calc[c]['plan']['items'])) for c in calc)))
    for kind, r in runs.items():
        rec = r['rec']
        out('%s check: %s, %s, %d parts; alerts %s; offers read %d, followed %d; placed %d; zones left %d; forming candles read %d' % (
            kind, 'quiet' if rec['quiet'] else 'loud', 'one line' if rec['one_line'] else 'full', len(r['sent']),
            json.dumps({k: sum(a['kind'] == k for a in rec['alerts']) for k in ('stop', 'signal', 'candidate')}, sort_keys=True),
            len(r['scan'][0]), len(rec['followed']), len(rec['passing']), len(rec['zones_left']), len(r['forming'])))


def mode_render():
    """G-RENDER: the service copy's bot answers the commands and runs both checks on live data, its Telegram a stand-in, its
    STATE a scratch directory holding a copy of the bot's own journal, so the trades its cards offered are the real ones."""
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
    texts, calc, runs, records, log, expect = render_run(mod, mod.Data(), dt.datetime.now(dt.timezone.utc))
    same = own == own_files() and own[3] is None
    render_print(texts, calc, runs, len(runs['signal']['rep']['strong']) if 'signal' in runs else -1, log)
    verdict('RENDER', render_checks(texts, calc, runs, [r['kind'] for r in records], records, log, same, expect))


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
    serving, _text, tb = log_since(read(BOTDIR + '/service.log'), pre['t'], pid)
    now = {'bot': bot, 'caps': caps, 'start': start, 'copy_t': copy_t, 'argv': proc_argv(pid) if pid else None, 'procs': procs(ARGV),
           'sha_adv3': sha256_file(SVC + '/adv3.py'), 'sha_bot': sha256_file(SVC + '/adv3-bot.py'),
           'sha_unit': sha256_file('/etc/systemd/system/adv3-bot.service'), 'daily': count_kind(read(BOTDIR + '/journal.jsonl'), 'daily'),
           'serving': serving, 'traceback': tb}
    checks = unit_checks(which, pre, now)
    if which == 'old':
        checks['two restarts more than before the first kill'] = int(bot['NRestarts']) == int(st['marks']['kill']['bot']['NRestarts']) + 2
    out('bot: pid %d NRestarts %s started %s; captures: %s' % (pid, bot['NRestarts'], time.strftime('%FT%TZ', time.gmtime(start)),
        json.dumps({u: [c['MainPID'], c['NRestarts']] for u, c in caps.items()}, sort_keys=True)))
    verdict('UNIT-' + which.upper(), checks)


def mode_first():
    st = load_state()
    pre = st['marks']['kill']
    pid = int(show(BOT, 'MainPID')['MainPID'])
    recs, tail_ok = records_since(read(BOTDIR + '/journal.jsonl'), pre['t'])
    if not [r for r in recs if r.get('kind') == 'check']:
        if time.time() - pre['t'] < FIRST_BOUND:
            raise NotYet()
    done_text = read(BOTDIR + '/check-done').strip() if os.path.exists(BOTDIR + '/check-done') else None
    _serving, text, _tb = log_since(read(BOTDIR + '/service.log'), pre['t'], pid)
    checks_ = [r for r in recs if r.get('kind') == 'check']
    r = checks_[0] if checks_ else {}
    out('first check: %s, %s, %d messages; alerts %s; followed %d; placed %d; check-done %s' % (
        'quiet' if r.get('quiet') else 'loud', 'one line' if r.get('one_line') else 'full', len(r.get('message_ids') or []),
        json.dumps({k: sum(a.get('kind') == k for a in r.get('alerts') or []) for k in ('stop', 'signal', 'candidate')}, sort_keys=True),
        len(r.get('followed') or []), len(r.get('passing') or []), done_text or '-'))
    verdict('FIRST', first_checks(pre, recs, done_text, text, pid, tail_ok))


def kept_files():
    """The work tree's files a report keeps by name: state.json, the three files B-DEPLOY saves, and every file under logs/;
    relative to WORK, sorted."""
    names = ['state.json', 'adv3.before', 'bot.before', 'commit.before']
    for d, _s, fs in os.walk(WORK + '/logs'):
        names += [os.path.relpath(os.path.join(d, f), WORK) for f in fs]
    return sorted(n for n in names if os.path.isfile(os.path.join(WORK, n)))


def mode_keep():
    """B-RECLAIM-OWN's copy: every kept file into the forensic store as tz39-work--<path with - for />, by exclusive create and
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
        dest = FORENSICS + '/tz39-work--' + rel.replace('/', '--')
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


# ---- the self-test: the pure readings on stand-ins and the render on the real bot with a synthetic market, each with its
# negative controls ----------------------------------------------------------------------------------------------------

def synthetic(bot):
    """A synthetic market of twelve coins for the stage's bot, Binance stood in for, and a journal of offers from earlier closes
    built so that a check meets a stop on a closed candle, an exit by signal and - at the fact check - a forming candle through the
    stop of the first card the signal check offers. (data, forming, now)."""
    a = bot.adv3
    dm = dt.date(2026, 6, 1)
    cs, funds = {}, {}
    for n, coin in enumerate(a.COINS[:12]):
        c, x = {}, 100.0 + n
        slope = (0.004 + 0.0015 * n) * (1 if n % 2 == 0 else -1)
        for i in range(160):
            x *= (1 + slope) * (1 + 0.004 * ((i * 7 + n) % 5 - 2))
            c[dm + dt.timedelta(days=i)] = (x, x * 1.02, x * 0.98, x)
        cs[coin] = c
        funds[coin] = lambda d: 0.0
    last = max(cs[a.COINS[0]])
    up, down = a.COINS[0], a.COINS[1]
    d5 = last - 5 * DAY
    old = [{'utc': '%sT06:00:00+00:00' % (d5 + DAY), 'kind': 'daily', 'close_of': str(d5), 'cards': [
        {'coin': up, 'side': 1, 'mode': 'market', 'close': cs[up][d5][3], 'U': cs[up][d5][3] * 0.001},
        {'coin': down, 'side': 1, 'mode': 'market', 'close': cs[down][d5][3], 'U': cs[down][d5][3] * 0.9}]}]
    with open(bot.STATE + '/journal.jsonl', 'w', encoding='utf-8') as fh:
        fh.write(''.join(json.dumps(r) + '\n' for r in old))
    marks = {c + 'USDT': (cs[c][last][3], 0.0001) for c in cs}
    forming = {}
    ms = lambda d: int(dt.datetime.combine(d, dt.time(0), tzinfo=dt.timezone.utc).timestamp() * 1000)

    def fake_fapi(path, **params):
        if path == '/fapi/v1/premiumIndex':
            return [{'symbol': k, 'markPrice': str(v[0]), 'lastFundingRate': '0.0001'} for k, v in marks.items()]
        if path == '/fapi/v1/fundingInfo':
            return []
        coin = params['symbol'][:-4]
        if params.get('limit') == 2:
            cl = cs[coin][last][3]
            o, h, l, c_ = forming.get(coin) or (cl, cl * 1.001, cl * 0.999, cl)
            return [[ms(last), '1', '1', '1', '1', '0', ms(last + DAY) - 1, '0'],
                    [ms(last + DAY), str(o), str(h), str(l), str(c_), '0', ms(last + 2 * DAY) - 1, '0']]
        return [[ms(last - k * DAY), '1', '1', '1', '1', '0', ms(last - k * DAY + DAY) - 1, '1e12'] for k in range(8)]

    class Stub:
        def __init__(self):
            self.cs, self.funds, self.missing = cs, funds, []

        def fresh(self):
            return self.cs, self.funds

    a.fapi = fake_fapi
    return Stub(), forming, dt.datetime.combine(last + DAY, dt.time(14, 0), tzinfo=dt.timezone.utc)


def mode_selftest():
    import tempfile
    done = []

    def ok(cond, name):
        done.append(name)
        assert cond, name

    mp = ('**Revision string:** `%s`\n\n| anchor | value |\n|---|---|\n| `A1` — observation set | `229a944f2d51` |\n'
          '| `A3` — phase | `x / y` |\n\n### Fingerprint table\n\n| path | lines | bytes | state | SHA-256 |\n|---|---|---|---|---|\n'
          '| `SYSTEM-MAP.md` | — | — | reported | self-reference |\n| `a/b.py` | 1,135 | 50,928 | frozen | `%s` |\n'
          '| `c.py` | 7 | 8 | tracked | `%s` |\n\n---\n\n## 1. Repository\n| `z.py` | 1 | 1 | frozen | `%s` |\n') % (MAP_REV, 'a' * 64, 'b' * 64, 'c' * 64)
    rev, anchors, rows = parse_map(mp)
    ok(rev == MAP_REV and anchors == {'A1': '229a944f2d51', 'A3': 'x / y'}, 'parse_map: the revision and the anchors')
    ok(rows == [('SYSTEM-MAP.md', None, None, 'reported', None), ('a/b.py', 1135, 50928, 'frozen', 'a' * 64), ('c.py', 7, 8, 'tracked', 'b' * 64)],
       'parse_map: the table\'s rows, thousands separators read, the next section left out')
    old = 'X = 1\nHELP = 1\ndef a():\n    return 1\ndef b():\n    return 2\nclass K:\n    def m(self):\n        return 1\nCMD = 5\ndef gone():\n    pass\n'
    new = 'X = 1\nHELP = 2\ndef a():\n    return 1\ndef b():\n    return 3\nclass K:\n    def m(self):\n        return 1\nNEWC = 0\ndef c():\n    return 0\n'
    good = tree_checks('f', old, new, ({'b'}, {'c'}, {'gone'}), ({'HELP'}, {'NEWC'}, {'CMD'}), ('a',))
    ok(all(good.values()) and len(good) == 3, 'tree_checks: exactly the named definitions and assignments differ, the rule\'s among the same, 3 of 3')
    for label, src, defs, asg, rule in (
            ('a definition that should be the same changed', new.replace('def a():\n    return 1', 'def a():\n    return 9'),
             ({'b'}, {'c'}, {'gone'}), ({'HELP'}, {'NEWC'}, {'CMD'}), ('a',)),
            ('a definition named changed that did not', new.replace('def b():\n    return 3', 'def b():\n    return 2'),
             ({'b'}, {'c'}, {'gone'}), ({'HELP'}, {'NEWC'}, {'CMD'}), ('a',)),
            ('an extra definition', new + 'def d():\n    return 0\n', ({'b'}, {'c'}, {'gone'}), ({'HELP'}, {'NEWC'}, {'CMD'}), ('a',)),
            ('an assignment changed and not named', new.replace('X = 1', 'X = 2'), ({'b'}, {'c'}, {'gone'}), ({'HELP'}, {'NEWC'}, {'CMD'}), ('a',)),
            ('a rule function that changed', new, ({'b'}, {'c'}, {'gone'}), ({'HELP'}, {'NEWC'}, {'CMD'}), ('b',))):
        ok(not all(tree_checks('f', old, src, defs, asg, rule).values()), 'tree_checks: %s reads FAIL' % label)
    rpt = ('#### E1 — x\n\n| field | value |\n|---|---|\n| `p_t_up` | 0.0735 |\n| `trades` | 19,002 |\n\n| field | pit_rule.block |\n|---|---|\n'
           '| `trades` | 19,002 |\n| `mean_R` | 0.0403 |\n\n#### E2 — y\n\n| `p_t_up` | 0.1100 |\n\n#### E4 — z\n\n| field | P_rule | P_strong.top3 |\n'
           '|---|---|---|\n| `mfe +1R` | 0.2318 | 0.4717 |\n| `mfe +2R` | 0.1257 | 0.2906 |\n| `mfe +3R` | 0.0759 | 0.1887 |\n| `top5_share` | 0.2401 | 0.9875 |\n\n'
           '#### E5 — w\n\n| quantile | total R | mean R a trade |\n|---|---|---|\n| 0.5 | 37.7116 | 0.2195 |\n\n| `lists` | 500 |\n| `share_mean_R_positive` | 0.8600 |\n\n'
           '#### The sets and the frozen FACTS\n\n| `G` | 570 |\n')
    want = {'base': {'mfe': {1: 0.2318, 2: 0.1257, 3: 0.0759}, 'mean_R_G': 0.0403, 'trades_G': 19002, 'p_G': 0.0735, 'contracts_G': 570},
            'strong': {'mfe': {1: 0.4717, 2: 0.2906, 3: 0.1887}, 'p_G': 0.11, 'mean_R_lists': 0.2195, 'lists': 500, 'lists_positive': 0.86,
                       'top5_share': 0.9875}}
    ok(pit_from_report(rpt) == want, 'pit_from_report: every figure read from its section and row, the thousands separator read')
    ok(pit_from_report(rpt.replace('| 0.5 | 37.7116 | 0.2195 |', '| 0.5 | 37.7116 | 0.2196 |')) != want, 'pit_from_report: a changed cell reads another PIT')
    d0 = dt.date(2026, 1, 1)
    closes = [100 * 1.01 ** i for i in range(150)] + [100 * 1.01 ** 149 * 0.998 ** k for k in range(1, 40)]
    c = {d0 + i * DAY: (cl, cl * 1.002, cl * 0.998, cl) for i, cl in enumerate(closes)}
    days = sorted(c)
    ok(sign_sum(days, closes, 120) == 4 and sign_sum(days, closes, 100) is None, 'sign_sum: four agreeing signs on a rising line, none before 112 days')
    exit_i = next(i for i in range(146, len(closes)) if sum((closes[i] > closes[i - L]) - (closes[i] < closes[i - L]) for L in (14, 28, 56, 112)) < 2)
    ok(walk(c, 1, str(d0 + 145 * DAY), 1.0, days[-1]) == ('signal', str(d0 + exit_i * DAY)), 'walk: a long ends at the close whose signs fall below +2')
    S0 = closes[145] * 0.999
    c2 = dict(c)
    c2[d0 + 147 * DAY] = (closes[146], closes[147] * 1.002, S0 * 0.99, closes[147])
    ok(walk(c2, 1, str(d0 + 145 * DAY), S0, days[-1]) == ('stop', str(d0 + 147 * DAY)) and walk(c, 1, str(d0 + 145 * DAY), S0, d0 + 149 * DAY)
       == ('open', None), 'walk: a candle reaching the stop ends it there; a series above it stays open')
    ok(walk(c, 1, str(days[-1]), 1.0, days[-1]) == ('open', None) and walk(c, 1, '2025-01-01', 1.0, days[-1]) == ('unknown', None),
       'walk: an offer of the last close is open; one with no candle of its close unknown')
    pre = {'t': 1000.0, 'bot': {'MainPID': '10', 'NRestarts': '2'}, 'daily': 7,
           'caps': {u: {'MainPID': str(i), 'NRestarts': '0', 'ActiveState': 'active'} for i, u in enumerate(CAPTURES, 20)}}
    now = {'bot': {'MainPID': '11', 'NRestarts': '3', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'enabled'},
           'caps': dict(pre['caps']), 'start': 1035.0, 'copy_t': 990.0, 'argv': ARGV, 'procs': [11], 'sha_adv3': H['adv3_new'],
           'sha_bot': H['bot_new'], 'sha_unit': H['unit'], 'daily': 7, 'serving': True, 'traceback': False}
    ok(all(unit_checks('new', pre, now).values()) and len(unit_checks('new', pre, now)) == 9, 'unit_checks: a clean restart reads 9 of 9')
    for key, val, label in (('daily', 8, 'a daily record since the mark'), ('start', 1200.0, 'a process started 200 s after the kill'),
                            ('sha_bot', H['bot_old'], 'the old bot'), ('sha_adv3', H['adv3_old'], 'the old adv3.py'),
                            ('traceback', True, 'a traceback since the mark'), ('procs', [11, 12], 'a second process under the argv'),
                            ('serving', False, 'no serving line of the new pid')):
        ok(not all(unit_checks('new', pre, dict(now, **{key: val})).values()), 'unit_checks: %s reads FAIL' % label)
    moved = {u: dict(cc, NRestarts='1') for u, cc in pre['caps'].items()}
    ok(not all(unit_checks('new', pre, dict(now, caps=moved)).values()), 'unit_checks: a capture unit restarted reads FAIL')
    ok(all(unit_checks('old', pre, dict(now, sha_bot=H['bot_old'], sha_adv3=H['adv3_old'])).values()), 'unit_checks: the rollback reads the old files')
    t0 = calendar.timegm(time.strptime('2026-11-02T14:00:00', '%Y-%m-%dT%H:%M:%S'))
    pre_f = dict(pre, t=float(t0))
    rec = {'utc': '2026-11-02T14:00:20+00:00', 'kind': 'check', 'slot': '2026-11-02 signal', 'close_of': '2026-11-01', 'rule': H['rule'],
           'message_ids': [5, 6], 'state': {str(k): {} for k in range(42)}, 'trust': {k: 0 for k in TRUST_KEYS}, 'alerts': [], 'passing': [],
           'quiet': True}
    log_f = ('2026-11-02T14:00:05Z serving the pinned chat: pid 11 offset 9 check-done -\n'
             '2026-11-02T14:00:20Z check sent: 2026-11-02 signal for the close of 2026-11-01 | alerts 0 | quiet | full')
    good = first_checks(pre_f, [rec], '2026-11-02 fact', log_f, 11, True)
    ok(all(good.values()) and len(good) == 7, 'first_checks: the first check after a 14:00 restart reads 7 of 7, check-done covering 12:10')
    ok(all(first_checks(dict(pre, t=float(t0 - 4 * 3600)), [rec], '2026-11-02 signal', log_f.replace('14:00:05', '10:00:05'), 11, True).values()),
       'first_checks: a 10:00 restart wants check-done at the signal slot')
    for label, args in (('no check record', ([], '2026-11-02 fact', log_f, 11, True)),
                        ('two check records', ([rec, rec], '2026-11-02 fact', log_f, 11, True)),
                        ('another slot', ([dict(rec, slot='2026-11-02 fact')], '2026-11-02 fact', log_f, 11, True)),
                        ('no message ids', ([dict(rec, message_ids=[])], '2026-11-02 fact', log_f, 11, True)),
                        ('a loud check without an alert', ([dict(rec, quiet=False)], '2026-11-02 fact', log_f, 11, True)),
                        ('check-done at the signal after 12:10', ([rec], '2026-11-02 signal', log_f, 11, True)),
                        ('a failed check in the log', ([rec], '2026-11-02 fact', log_f + '\ncheck failed: x', 11, True)),
                        ('another pid serving', ([rec], '2026-11-02 fact', log_f, 12, True)),
                        ('a broken journal', ([rec], '2026-11-02 fact', log_f, 11, False))):
        ok(not all(first_checks(pre_f, *args).values()), 'first_checks: %s reads FAIL' % label)
    log = ('2026-10-31T06:00:01Z daily sent for the close of 2026-10-30\n2026-10-31T09:00:00Z serving the pinned chat: pid 11 offset 5 check-done -\n'
           'Traceback (most recent call last):\n  File x\n2026-10-31T09:00:30Z check sent: 2026-10-31 signal')
    t = calendar.timegm(time.strptime('2026-10-31T08:59:59', '%Y-%m-%dT%H:%M:%S'))
    s_, text_, tb_ = log_since(log, t, 11)
    ok(s_ and tb_ and 'daily sent' not in text_ and 'check sent' in text_ and '  File x' in text_, 'log_since: the lines since t, a traceback\'s with them, serving found')
    ok(not log_since(log, t, 12)[0] and not log_since(log, t + 3600, 11)[2], 'log_since: another pid does not serve; a later start sees no traceback')
    jl = ('{"utc": "2026-10-31T06:00:00+00:00", "kind": "daily"}\n{"utc": "2026-10-31T09:00:30+00:00", "kind": "check"}\n')
    rs, okj = records_since(jl, calendar.timegm(time.strptime('2026-10-31T09:00:00', '%Y-%m-%dT%H:%M:%S')))
    ok([r['kind'] for r in rs] == ['check'] and okj, 'records_since: the records since t, the earlier left out, a whole journal')
    ok(not records_since(jl + 'broken\n', t)[1] and not records_since(jl.rstrip('\n'), t)[1] and records_since('broken\n' + jl, t + 30)[1],
       'records_since: a broken line after the mark or no final newline reads FAIL; one before the mark does not')
    ok(count_kind(jl + 'x\n{"kind": "daily"}\n', 'daily') == 2 and count_kind('', 'check') == 0, 'count_kind: the kind counted, a broken line left out')
    ok(memory_gate(MEM_FLOOR, None) == (True, MEM_FLOOR) and memory_gate(MEM_FLOOR - 1, MEM_FLOOR) == (True, MEM_FLOOR)
       and memory_gate(MEM_FLOOR - 1, MEM_FLOOR - 2) == (False, MEM_FLOOR - 2), 'memory_gate: a first read below the floor is decided by the second')
    ok(all(number_reading([TZ_FILE, 'CryptoTZ/TZ-38-x.md']).values()), 'number: the one file reads PASS')
    ok(not all(number_reading([TZ_FILE, 'CryptoTZ/TZ-39-other.md']).values()) and not all(number_reading([TZ_FILE, 'CryptoReports/TZ-39-x-report.md']).values()),
       'number: two files of the number, or a report of it, read FAIL')
    with tempfile.TemporaryDirectory() as tmp:
        os.makedirs(tmp + '/logs/sub')
        for rel in ('state.json', 'bot.before', 'adv3.before', 'logs/01-a.log', 'logs/sub/02-b.log', 'render-state/journal.jsonl'.replace('/', '-'), 'x.txt'):
            with open(tmp + '/' + rel, 'w') as fh:
                fh.write(rel)
        saved_work = WORK
        globals().update(WORK=tmp)
        try:
            kept = kept_files()
        finally:
            globals().update(WORK=saved_work)
    ok(kept == ['adv3.before', 'bot.before', 'logs/01-a.log', 'logs/sub/02-b.log', 'state.json'], 'kept_files: the named files and the logs, nothing else')
    # ---- G-RENDER on the stage's own bot and a synthetic market ----------------------------------------------------
    here = os.path.dirname(os.path.abspath(__file__))
    stage = os.path.join(os.path.dirname(here), 'advisor')
    with tempfile.TemporaryDirectory() as tmp:
        saved = list(sys.path)
        sys.path.insert(0, stage)
        try:
            bot = load_module('advbot_selftest', stage + '/adv3-bot.py')
        finally:
            sys.path[:] = saved
        bot.STATE = tmp
        real_fapi = bot.adv3.fapi
        try:
            data, forming, now0 = synthetic(bot)
            rep0 = bot.top_n(bot.adv3.report(data.cs, data.funds, {c + 'USDT': (data.cs[c][max(data.cs[c])][3], 0.0001) for c in data.cs},
                                             10000.0, 0.5, int(now0.timestamp() * 1000)), 3)
            first = rep0['cards'][0]
            S = first['close'] - first['side'] * first['U']
            cl = first['close']
            forming[first['coin']] = (cl, max(cl, S * 1.01), min(cl, S * 0.99), cl)
            texts, calc, runs, records, blog, expect = render_run(bot, data, now0)
        finally:
            bot.adv3.fapi = real_fapi
    kinds = [r['kind'] for r in records]
    args = dict(texts=texts, calc=calc, runs=runs, kinds=kinds, records=records, log=blog, same=True, expect=expect)
    good = render_checks(**args)
    al = {k: [(x['kind'], x['touch']) for x in runs[k]['rec']['alerts']] for k in runs}
    ok(all(good.values()) and len(good) == 22, 'render_checks: the stage\'s bot on a synthetic market reads 22 of 22 - %s' % [k for k, v in good.items() if not v])
    ok(('stop', False) in al['signal'] and ('signal', False) in al['signal'] and ('candidate', False) in al['signal'] and al['fact'] == [('stop', True)],
       'the synthetic market meets every alert: a stop on a closed candle, an exit by signal and new candidates at the signal check, a forming candle '
       'through a stop at the fact check')

    def bad(**kw):
        a_ = dict(args)
        a_.update(kw)
        return not all(render_checks(**a_).values())

    sig, top7 = texts[RENDER_CASES[0]], texts[RENDER_CASES[1]]
    ok(bad(log='Traceback (most recent call last):') and bad(log='check failed: x'), 'render_checks: a traceback or a failure in the bot\'s log reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[0]: []})), 'render_checks: a command with no answer reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[5]: ['<b>HELP']})), 'render_checks: unbalanced markup reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[0]: [sig[0] + '\nОценка доверия']})), 'render_checks: a «сигнал» carrying the six ratings reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[0]: [re.sub(CONF, 'X: ', sig[0], count=1)]})), 'render_checks: a card without its confidence reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[0]: [sig[0].replace('Уверенность: <b>1/5</b>', 'Уверенность: <b>3/5</b>', 1)]})),
       'render_checks: a confidence that is not the rung reads FAIL')
    four = re.sub(r'(?m)^([🟢🔴] <b>[A-Z0-9]+ · (?:LONG|SHORT)</b>)$', r'\1 · ★ STRONG', top7[0])
    ok(four != top7[0] and bad(texts=dict(texts, **{RENDER_CASES[1]: [four]})), 'render_checks: STRONG beyond the first three of the list reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[4]: [texts[RENDER_CASES[4]][0].replace('+0,22 R', '+0,55 R')]})),
       'render_checks: an assessment quoting the 42\'s STRONG figure reads FAIL')
    ok(bad(expect=dict(expect, consts=(11.1,) + expect['consts'][1:])) and bad(expect=dict(expect, consts=expect['consts'][:7] + (10,) + expect['consts'][8:])),
       'render_checks: another stop limit or another list length reads FAIL')
    c1 = RENDER_CASES[2]
    ok(bad(texts=dict(texts, **{c1: [calc[c1]['parts'][0] + ' ']})), 'render_checks: an allocation reply that is not the plan\'s own reads FAIL')
    p = calc[c1]['plan']
    if p['items']:
        worse = dict(p, items=[dict(p['items'][0], card=dict(p['items'][0]['card'], stop_pct=14.5))] + p['items'][1:])
        ok(bad(calc=dict(calc, **{c1: dict(calc[c1], plan=worse)})), 'render_checks: a stop beyond 14 % in a plan reads FAIL')
        heavy = dict(p, items=[dict(p['items'][0], loss_exact=p['budget'] * 0.0101)] + p['items'][1:])
        ok(bad(calc=dict(calc, **{c1: dict(calc[c1], plan=heavy)})), 'render_checks: a loss at a stop beyond 1 % of the budget reads FAIL')
    sg = runs['signal']
    flipped = dict(sg, rec=dict(sg['rec'], quiet=not sg['rec']['quiet']))
    ok(bad(runs=dict(runs, signal=flipped)), 'render_checks: a check whose quiet flag disagrees with its alerts reads FAIL')
    dropped = dict(sg, rec=dict(sg['rec'], alerts=[a for a in sg['rec']['alerts'] if a['kind'] != 'signal']))
    ok(bad(runs=dict(runs, signal=dropped)), 'render_checks: an exit the walk finds and the check does not alert reads FAIL')
    fa = runs['fact']
    again = dict(fa, rec=dict(fa['rec'], alerts=fa['rec']['alerts'] + [a for a in sg['rec']['alerts'] if a['kind'] == 'stop']))
    ok(bad(runs=dict(runs, fact=again)), 'render_checks: an alert sent twice across the checks reads FAIL')
    ok(bad(runs=dict(runs, fact=dict(fa, rec=dict(fa['rec'], cards=list(sg['rec']['cards']))))), 'render_checks: a fact check offering the close\'s cards reads FAIL')
    ok(bad(kinds=kinds[:-1]) and bad(kinds=['check'] + kinds[1:]), 'render_checks: a journal that lacks a record or has another kind reads FAIL')
    ok(bad(same=False), 'render_checks: the bot\'s own record changed reads FAIL')
    out('SELFTEST PASS: %d of %d checks passed' % (len(done), len(done)))


def main(argv):
    if not argv:
        sys.exit('usage: tz39-advisor-checks.py MODE [ARG]')
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
