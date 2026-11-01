# TZ-40 — STRONG at every rank: the list's TOP-N and every STRONG beyond it, the allocation's first N and every other STRONG that passes its limits, each sized alone, the checks' candidates — and Telegram's pace for the longer messages

**Canonical filename:** `TZ-40-strong-every-rank.md`. The committed file takes this name and no other.

**Executor model: Claude Opus 5.5.** It replaces three files of the advisor — the selection of STRONG in every view, the allocation's sizing of the trades beyond the requested N, the checks' candidates and the bot's sending of a long message — signals a long-lived unit on the capture host and writes one file of its record.

**Required System Map revision:** `2026-11-01-a`.

**Map sections this TZ rests on**, copied from §10's C8 (map §7 item 141): §0, the fingerprint gate and its table; §1, the refs; §2.5 and §2.6, the archives' calendar runs and the reward book's `STREAM_FLOOR`; §2.7, the advisor's record and TZ-39's paragraph; §3, the forensic store, the worktrees and the directories TZ-39's session left; §6, its rows host identity, language, git remote, egress, process supervision, memory, disk, both sandbox limits and the harness; §7 items 118, 124, 125, 129, 131, 132 and 136 to 145.

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

**Before `EXECUTE TZ-40`:** the Boss uploads this file alone, into `CryptoTZ/`. `main` already carries map revision `2026-11-01-a` (`f2a3ed6`) and PR #39's merge (`f212cd4`); nothing else is needed, and no step of the Boss's is a precondition of the run (map §7 item 132). The bot's token and its pinned chat exist (map §2.7); this TZ's own commands read neither, and the bot's `--probe`, which reads the token to send `getMe`, prints neither (§2 item 3).

**When:** any time after the upload, while `/dev/vda2` holds at least `7,400,000,000` bytes free and `MemAvailable` at least `140,037,206` bytes (§0.4). **B-DEPLOY waits in its own text for 07:30:00 to 11:20:00 or 12:20:00 to 23:20:00 UTC, and B-KILL for 07:30:00 to 11:50:00 or 12:20:00 to 23:50:00 UTC**: clear of the package manager's morning run (map §7 item 143) and of both archives' calendar runs, the reward book's at 01:30:20 and the pair book's at 03:00:20 (map §2.5 and §2.6); clear of the unit's two checks, 00:10 and 12:10 UTC, so that the check the new process replays at its start (§1) meets neither and ends before the next; and B-DEPLOY's band ends 30 minutes before B-KILL's, so that B-KILL's is still open when COPY, G-RENDER and P-START have run, each at its bound (§6). This TZ reloads systemd **never**, so it sets off no run of either archive (map §7 items 125 and 129). About 45 minutes of wall clock (§6).

**What this TZ is.** The Boss's specification of 2026-11-01, «Change STRONG Candidate Selection and Reporting Logic», built with the stronger of the two readings it allows (§1): **STRONG at every rank in every view** — a coin whose four signs agree with its side and whose `|z|` is at least `1`, wherever it ranks — the rule's first N coins as the list and **every STRONG coin beyond them under «Дополнительные STRONG-кандидаты»**, with the same card; the allocation's first N STRONG trades that pass its limits, placed by TZ-37's arithmetic, and **every other STRONG trade that passes them below, each sized by the same arithmetic as a trade of its own**, with the loss of all of them together read against the 5 % limit; the checks' candidates at every rank; and **every STRONG card beyond the TOP-3 marked «· вне ТОП-3»**, because the frozen rule's STRONG — and the strategy its forward record measures — is the TOP-3's. Because the messages grow, **the bot paces the parts of one message 1.1 s apart and waits out Telegram's «too many requests»**. **It changes no rule, no parameter of the rule and no coin:** the fourteen rule functions of `adv3.py` with `report`, `card` and `trust`, `RULE-ADV-3.txt`, the unit file and **TZ-37's `plan`** stay what TZ-35 to TZ-39 deployed, by file and by syntax tree (G-RULE). It replaces `advisor/adv3.py`, `advisor/adv3-bot.py` and `advisor/selftest-adv3.py`, adds its checker `research/tz40-advisor-strong.py`, deploys by replacing the service copy's two files and signalling the unit once, and reads the new process's first check — the day's signal check, which the new process replays at its start because B-KILL's mark sets `check-done` to the slot before it, sent to the Boss's chat by the unit itself — as the deployment's proof on the host (G-FIRST).

---

## 0. Gates

### 0.0 The work tree, first

After contract §1 steps 1 and 2, and before anything else:

```
mkdir /root/tz40-work /root/tz40-work/logs; echo "exit=$?"
```

`exit=0` proves neither existed; anything else is BLOCKED. **From here every command's output goes to `/root/tz40-work/logs/`, one file per step, `NN-<step>.log` in this TZ's order** — the steps of §3.4 to §3.6 and §4.4 under the names their blocks write and the pastes read, `20-b-deploy.log` to `26-first.log` and `30-b-rollback.log` to `34-stopped.log` — and nothing to the session's scratchpad. The one exception is B-RECLAIM-OWN, §9, which removes the directory the logs are in.

Two abbreviations: **`P`** is `nice -n 19 /root/tz04a-env/venv/bin/python -B`, and **`I`** is `P /root/tz40-work/stage/research/tz40-advisor-strong.py`. **In every block that deploys, signals, restores or removes, both are written out in full**, because the Boss may be handed the block (map §6, sandbox limit).

### 0.1 The files, staged

Extract Appendix A from this TZ as the primary checkout carries it after contract §1's pull, with this script, verbatim, its one argument the destination:

```
/root/tz04a-env/venv/bin/python -B - /root/tz40-work/stage <<'EOF'
import hashlib, os, sys
SRC = "/root/btc-5m-twap/CryptoTZ/TZ-40-strong-every-rank.md"
DEST = sys.argv[1]
WANT = {
    "advisor/adv3.py": "81ef0112d3fe4b86566e51a51aab924d9776ff37a927e65982ecb0bb7c1f34e1",
    "advisor/adv3-bot.py": "9e622daf2e8a5ec3e93f15c7f56e7cf859547fbd3771daad75bc6532adb2b9d1",
    "advisor/selftest-adv3.py": "6f29b82f2b2ca82cd2ff4bbb370e032354dbb4743497330530777429b3af7398",
    "research/tz40-advisor-strong.py": "4403b27185f7e9aaa090dedfca457af6c4f70b6b020f0d2fcd9f9fbb96b6054b",
}
OLD = {  # the committed files an extraction over a worktree replaces, by hash: TZ-39's three advisor files
    "advisor/adv3.py": "c19572dccf30a505342ca334e42c7ec347a5d29db4db20887229d2a8c7b48e31",
    "advisor/adv3-bot.py": "ca989b6fe487d41181b32312418d6acda1e9c64fbf5cfbb3f041d54826dd108f",
    "advisor/selftest-adv3.py": "09d2ba9a8361ec5ebc7f5934ebb818d1a685bb16fb3f32b7da94409d9516cc0e",
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
| `advisor/adv3-bot.py` | 1,869 | 126,909 | `9e622daf2e8a5ec3e93f15c7f56e7cf859547fbd3771daad75bc6532adb2b9d1` |
| `advisor/adv3.py` | 895 | 51,834 | `81ef0112d3fe4b86566e51a51aab924d9776ff37a927e65982ecb0bb7c1f34e1` |
| `advisor/selftest-adv3.py` | 256 | 19,111 | `6f29b82f2b2ca82cd2ff4bbb370e032354dbb4743497330530777429b3af7398` |
| `research/tz40-advisor-strong.py` | 1,436 | 95,474 | `4403b27185f7e9aaa090dedfca457af6c4f70b6b020f0d2fcd9f9fbb96b6054b` |

A failed assert is BLOCKED. Over an empty `stage/` the script creates four files (`xb`); over the branch's worktree, §3.1, it overwrites the three committed advisor files, each only after asserting it is the committed one by hash, and creates the checker.

### 0.2 Fingerprint

`I fingerprint` performs contract §1 steps 3 and 4 against `SYSTEM-MAP.md` and the files of its §0 table in the primary checkout `/root/btc-5m-twap`, and asserts them: revision `2026-11-01-a`; the six anchors, `A2`, `A4`, `A5` and `A6` re-derived as the first 12 hex characters of those files' SHA-256; the table's **59** rows, each printed in lines, bytes and SHA-256 — **56** `frozen` rows asserted equal to the map, **2** `tracked` and **1** `reported`, the map's own. It prints `READING FINGERPRINT: PASS - 68 of 68` — 1 revision, 6 anchors, 4 re-derived, 56 rows, 1 shape — or fails at the first mismatch, which is BLOCKED. The advisor rows are `frozen` at TZ-39's hashes and stay so until the verdict of this TZ.

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

`I host` asserts these nineteen, prints each check beside the units' readings, the check records' slots and delays, and the memory and disk figures, and prints `READING HOST: PASS - 19 of 19`, or fails:

- **H1** — `find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit` prints one path.
- **H2** — `df` names source `/dev/vda2` and size `31612203008`; `grep -c e3975b5da44c5328adf3bf3914634cd878842c73 /var/lib/btc-recorder/runtime.jsonl` prints at least `1` — two checks. With H1 this is map §6's host identity.
- **H3** — `/root/tz04a-env/venv/bin/python` prints `3.12.`: the interpreter the bot runs under.
- **H4** — `btc-recorder.service`, `btc-pairbook.service` and `btc-rewardbook.service` each read `ActiveState=active` and `UnitFileState=enabled` — three checks: UNIT-NEW compares them, later, against the `kill` mark's snapshot.
- **H5** — `adv3-bot.service` reads `active`, `running`, `enabled`; its `MainPID` runs the unit's exact argv, alone; `/root/adv3-bot-svc` holds `adv3.py`, `adv3-bot.py` and `commit.txt` and nothing else; `adv3.py` and `adv3-bot.py` hash to TZ-39's (`c19572dc…` and `ca989b6f…`); the installed unit file hashes to `main`'s (`82acd8e4…`); `commit.txt` is 40 hex characters and a newline — six checks.
- **H6** — `/var/lib/adv3-bot/journal.jsonl` ends in a newline, and `check-done` names a slot, `YYYY-MM-DD signal` or `YYYY-MM-DD fact`.
- **H7 — the clock fires**, map §2.7's open reading: the journal's `check` records, from TZ-39's first, `2026-11-01 signal`, name strictly later slots, each once; every one after it — at least one — is stamped at or after its slot's instant, 00:10 or 12:10 UTC; and `check-done` names the last one's slot, or its day's `fact` where the last is a signal check stamped at or after 12:10 UTC (`done_after`) — three checks. A slot the unit was down for is a gap, printed and not blocking.
- **Memory gate** — `MemAvailable` at least `140,037,206` bytes (§0.4); **where the first read is below it, `I host` reads again after 60 s and the second read decides** (map §7 item 137). **Disk gate** — `/dev/vda2` free at least `7,400,000,000` bytes (§0.4).

Any one failing is BLOCKED. **The rest is printed and carries no threshold:** the timers and the two archives' services; the listing of the service copy and the record; `du` of the capture roots and the Claude directory; the forensic store's count, map §3's `2,344`; the worktrees, map §3's two; and the listing of the directory that holds the session's own scratch, whose UUID directories §3.3 names live or earlier. Map §3 records the two TZ-39's session left, `a2827336-da6d-511b-b699-35cb76f477de` and `0f8f6761-2295-466b-9178-9b8a0261193e`, and one live directory that is no TZ's, `238335b9-cf23-414a-8e8f-ad4705c4d19e`, the remote-control session of 2026-10-30 (TZ-38's report).

### 0.4 Resource floors, in exact bytes

**Disk.** `/dev/vda2` free at least **`7,400,000,000`** bytes: the reward book's `STREAM_FLOOR`, `7,300,000,000`, below which no stream of it opens (map §2.6; `research/tz33-reward-book-capture.py` line 190), plus `100,000,000` for this session at its upper bound — the worktree, about `12,700,000` bytes of tracked files, the stage and the logs under `2,000,000`, the render's scratch journal, a copy of the bot's own, under `1,000,000` today and about `36,000,000` at a year of the heaviest checks the Architect simulated (§6), and the copies of the work tree's files under `5,000,000`. **This TZ never takes free space below the floor that pauses the reward book.** TZ-39 read `11,410,116,608` bytes free at its host gate.

**Memory.** `MemAvailable` at least **`140,037,206`** bytes: twice `70,018,603`. A floor is twice the largest peak among the modes the TZ runs (TZ-37 §0.4), and map §7 item 131 takes the larger of the Architect's measurement and the host's last measured peak of the same code. The largest mode here is `I render`, the service copy's bot answering seven commands and running both checks in one process. The Architect measured it on 2026-11-01 on Binance's archive candles of the 42 coins, a stand-in for `fapi.binance.com`, five runs a case under Python 3.12.3, the host's interpreter, and five under 3.13.18: to the close of 2026-10-30 with a journal of 13 offers in the host's shape, at most `58,220,544` and `58,085,376` bytes; with the journal of the Architect's ninety-day simulation (§6), `8,917,445` bytes and 930 offers, `58,667,008` and `58,396,672`; on the archive's heaviest STRONG close, 2026-09-27 — 35 coins of 42 STRONG — with that journal, `58,134,528` and `58,060,800`. The journal is streamed and the candles dominate, so neither moves the peak by more than a megabyte. This code has no host peak yet. TZ-37's own `I render` peaked on the host at `1.199` times the Architect's Python 3.13.18 measurement of it (map §6, memory: `58,953,728` against `49,168,384`); at that ratio this TZ's largest 3.13.18 figure gives `70,018,603` [modelled: `58,396,672` × `58,953,728` / `49,168,384`, rounded up], above every 3.12.3 figure and above TZ-36's `I render` process tree, `65,490,944`, which stood in at TZ-37 and TZ-39 (map §6, memory). The larger stands. **`I render` prints its own peak resident set and its time** (map §7 item 145): the mode is its own wrapper, inside a paste as outside it. The service runs under its unit's `MemoryMax=128M`, which this TZ does not change; the new code's own process, holding the archive's candles and the ninety-day journal, peaked at `55,922,688` bytes through two checks and four commands under Python 3.12.3 (§6). Every mode of this TZ runs under `nice -n 19`.

### 0.5 Refs and the number

```
git -C /root/btc-5m-twap fetch origin
git -C /root/btc-5m-twap ls-remote origin
git -C /root/btc-5m-twap ls-remote --heads origin tz-40-strong-every-rank | wc -l
I number
git -C /root/btc-5m-twap log --first-parent --name-status --format='%h %cI %s' -n 5 origin/main
```

Every ref line is reported. **`wc -l` must print `0`:** the branch does not exist. **`I number`** reads `git ls-tree --name-only origin/main -- CryptoTZ/ CryptoReports/` and must print `READING NUMBER: PASS - 2 of 2`: `CryptoTZ/` holds `TZ-40-strong-every-rank.md` and no other file whose name begins with `TZ-40-`, and `CryptoReports/` no report whose name does (CANON hard rule 2). Anything else is BLOCKED. A difference in the refs or the log from what map §1 records is recorded, not blocking, unless `main` does not carry revision `2026-11-01-a`.

---

## 1. Why this TZ exists

**The Boss's specification of 2026-11-01**, in his words: "Remove the hard limit that allows STRONG trades only within the TOP-3. Do not suppress or exclude any qualifying STRONG candidate because of its ranking." "If more than 7 candidates qualify as STRONG, output the TOP-7 in the main section and list all remaining qualifying STRONG candidates in a separate **Additional STRONG Candidates** section below, using exactly the same fields, calculations, and risk checks." "The requested TOP-N determines the size of the main list, not the maximum number of qualifying STRONG opportunities the system may identify and report." His example was an allocation of `210,000` USDT for seven trades that placed two.

**What the frozen rule says, and what moves.** RULE-ADV-3 defines STRONG as "a TOP-3 coin whose four signs all agree with its side and whose |z| >= 1", and the STRONG strategy holds at most three; its forward record and the market record are re-derived from Binance's archive by that definition (CANON PART VII) and never from the bot's journal, so **what the bot shows moves no record and no rung.** This TZ adds a class of the bot's own — **STRONG at every rank**: the frozen condition without its TOP-3 (`strong_all`), whose members among the TOP-3 are the report's STRONG exactly — and shows it everywhere the Boss asked. The rule's `ranking`, `simulate_strong`, `report`, `card` and `trust` are untouched.

**Where the instruction is weak, and the stronger thing [решение принято мной].** Rank carries information the instruction would erase. In TZ-38's history (E6, in sample, the 609 contracts of *P*) STRONG with seven places made `+0.51` R a trade against `+0.80` with three; by the place a trade entered at, ranks 4 to 5 made `+0.07` R a trade over 131 trades and 6 to 7 `+1.33` over 35; beyond seven places nothing is measured. The Architect's exploration of the 42's archive since 2023 — in sample, on coins picked in 2026, the funding at the rule's default, an exploration that gates nothing (CANON PART VI) — reads STRONG at every rank, every place taken, at `+0.57` R a trade over 154 trades entered at ranks 1 to 3, `+0.54` over 161 at 4 to 7 and `+0.20` over 384 at 8 and beyond. And the class is large: on the 42 since 2025 the median close holds 4 coins STRONG at every rank and 1 of them with a stop within 14 % of the close; the heaviest, 2026-09-27, holds 35 of 42, every one LONG — one bet on the market's direction — 22 of them within 14 %. **So the change is built as asked — nothing omitted, the same card, the same sizes, the same limits — and each STRONG card beyond the TOP-3 carries «· вне ТОП-3»**, one line saying that this is not the strategy the forward record measures, **each trade beyond the requested N its correlation with the placed ones, and the allocation the loss of all of them together against the 5 % limit.** Discarded: labelling them as the measured STRONG, which would let the Boss read a TOP-3 strategy's history into a class nobody measured.

| the Boss's specification | built as |
|---|---|
| no STRONG candidate excluded because of its ranking | `strong_all`: four signs agreeing and `|z|` at least `STRONG_Z`, at every rank of the rule's order (`ranked`) |
| the main section the first N, the rest under «Additional STRONG Candidates», the same fields, calculations and risk checks | the list: `top_n`, the rule's first N cards and then every STRONG beyond them marked `extra`, `adv3.message`'s «Дополнительные STRONG-кандидаты»; the allocation: `plan_strong`, `plan_parts`, `item_lines` |
| any requested TOP-N | N from 1 to 7 in the list and the allocation (`LIST_MAX`), the extra section beyond it at any N |
| never downgrade, omit or suppress | ★ STRONG on every STRONG card, at every rank; the checks' candidates at every rank (`candidates`, `alerts_of`, `candidate_lines`, `event_lines`); every extra card offered and followed (`compose`, `offers`) |

**The list [решение принято мной].** «сигнал» and «сигнал топ N» keep the rule's first N coins as their main section — the Boss's specification of 2026-10-31, CANON PART VII — each STRONG among them marked ★ at whatever rank; **every STRONG coin ranked beyond N follows under «Дополнительные STRONG-кандидаты»**, each with its full card at the same deposit and risk, its basis reading «ранг k — за ТОП-N». Discarded: a list of STRONG coins only, which would drop the strongest trends that are not STRONG — the ranking the list was asked to show.

**The allocation.** The main section is the first N STRONG trades at any rank that pass the limits — current prices, an entry, a stop within 14 % of it — **placed by TZ-37's `plan`, unchanged by its syntax tree**, called over STRONG at every rank in the rule's order: the same strength shares, crowding discount, 1 % and 5 % caps, liquidity cap, minimum and leverage. **Every other STRONG trade that passes the limits follows under «Дополнительные STRONG-кандидаты», each sized by the same `plan` alone** — a one-trade allocation, so its loss at the stop is the average risk, `0.5 %` of the budget by default, under the same caps — with its mean same-way correlation with the placed trades, read from the same `plan` over them and it; **none of them counts in «Итог»**, and one line gives the loss at the stops of all of them and the placed ones together, adding, where it exceeds 5 % of the budget, «больше лимита 5%: брать вместо основных, а не вдобавок». The rejected keep their reasons; «Без STRONG среди первых N по силе — не берутся: …» replaces TZ-37's «В ТОП-3 без STRONG», and «STRONG бывает только в ТОП-3» is gone. Discarded: one allocation over every STRONG trade, which would shrink the N trades the Boss asked for whenever more pass, and move their sizes with trades he did not ask for.

**N stays at most 7 [решение принято мной]** — the Boss's limit of 2026-10-31 for the list, and the allocation's since TZ-37: a request above 7 reads 7, and with the extra section nothing beyond it is hidden.

**The checks.** At 00:10 and 12:10 UTC the allocation at the default budget, `10,000` USDT and `0.5 %`, runs over STRONG at every rank, N = 3; **a STRONG coin that passes the limits — placed or among the more — that did not at the check before is an alert**, pushed with its plan; the 00:10 message carries the TOP-3, every STRONG beyond it in its own section, and among «STRONG-кандидаты» every STRONG coin at every rank with its capital, leverage, margin and loss, or its reason. **The quiet line asks one thing more**: the coins STRONG at every rank as at the check before (`strong_all` in the record), which no record of TZ-39's holds — so the new code's first signal check, the replay at its start (below), sends the full message. Every extra card a message publishes with an entry is offered, and followed by the rule's own functions like every other (CANON PART VII); an allocation offers its placed trades and its more.

**The reach shares.** Every ★ STRONG card quotes one set, TZ-38's STRONG shares without survivorship, `47 / 29 / 19 %` (E4, three places); E6's seven places read `49 / 30 / 20 %`, not below them; beyond seven places nothing is measured, and the Architect's exploration on the 42 reads `51 / 26 / 16 %` for ranks 8 and beyond. No new figure reaches a card.

**«оценка»** gains one line: STRONG beyond the TOP-3 is the same condition and the same calculation, not the measured strategy; on every Binance contract STRONG with seven places made `+0,51` R a trade against `+0,80` with three; beyond the seventh place nothing is measured (`adv3.PIT`'s `mean_R_P7` and `mean_R_P3`, read by G-RULE from TZ-38's report cell for cell).

**Telegram's pace.** The messages grow: on the archive's heaviest close «сигнал» is 17,724 characters in five parts and the 00:10 check 24,416 in seven [measured by the Architect: the archive's candles to the close of 2026-09-27, the marks at the close, an empty journal]. The Bot API asks for at most one message a second in a chat and answers a burst with `429` and a `retry_after`; under TZ-39's `send` a refused part fails the check, and the retry 300 s later sends every part again. **So `Telegram.send` sends the parts of one message `1.1` s apart and, where a part is refused as too many requests, waits the `retry_after` named, at most 60 s, plus one, and sends that part again, twice at most**; `call` raises `TooMany` for a `429` and a `RuntimeError` of its own for every other refusal, as before.

**The first check after the restart.** B-KILL's mark asserts that `check-done` names the latest slot — the running process owes no check — and then writes it to the slot before the UTC day's signal check, the day before's `fact`; the old process holds its slot in memory and never reads the file again. **The new process reads that slot at its start and replays the day's signal check at once** — the close of the day before, in the new format, with every STRONG beyond the TOP-3 — **a second message of that close**, as TZ-39's first check was; a signal check that ends at or after 12:10 marks the day's fact check done too (`done_after`), whose 12:10 run the old code has made. Its stops and signal exits already alerted are not alerted again (`alerted`); **each STRONG coin beyond the TOP-3 that passes the limits is a new candidate against the check before, TZ-39's, and sounds once**. G-FIRST reads that check from its record and its log (§4.3); nothing in this TZ sends or fakes a message to the Boss's chat. Where the run rolls back before the new process advanced `check-done`, the rollback mark writes the kill mark's value back (§4.4).

**What it costs after the session.** Longer messages, and more trades followed: the Architect's simulation of the new code's two checks a day over the archive's 90 closes from 2026-08-01 to 2026-10-29, the journal accumulating — the heaviest trend of the archive's last two years among them — wrote `99,083` bytes of journal a day against TZ-39's modelled `21,000`, at most `141,145` bytes a record, at most 8 Telegram parts a message (mean 2.14), at most 593 followed trades, at most `1.66` s of processor a check under Python 3.12.3 [modelled: the archive's candles, marks at the close, every card offered at market] (§6).

**What this TZ does not do.** No new rule, no parameter, no coin, no frozen record of the new class, no scan beyond the 42, no change to the allocation's arithmetic, the schedule, the monitor's rules, the stop limit, the confidence or the unit, no new unit and no reload of systemd. It does not touch Telegram's command menu, a bound on `service.log` or the journal's record of the followed trades, which stay where TZ-39 left them.

---

## 2. Scope

**Paths this TZ writes.** On the branch `tz-40-strong-every-rank`: `advisor/adv3.py`, `advisor/adv3-bot.py` and `advisor/selftest-adv3.py`, modified, and `research/tz40-advisor-strong.py`, new. On the host: `/root/tz40-work/**`; `/root/adv3-bot-svc/adv3.py`, `/root/adv3-bot-svc/adv3-bot.py` and `/root/adv3-bot-svc/commit.txt`; **`/var/lib/adv3-bot/check-done`**, by the checker's `kill` mark and, where §4.4 says, its `rollback` mark, each by one rename through `check-done.tz40`; `/root/btc-forensics/tz40-work--*`. On `main`: the report, `CryptoReports/TZ-40-strong-every-rank-report.md`. **The unit itself, once restarted, writes `check-done` and its own records** — its own writes, not this TZ's.

**Prohibited**, by path and by content class:

1. Any change to a repository file but the four above and the report — `advisor/RULE-ADV-3.txt`, `deploy/systemd/adv3-bot.service`, `SYSTEM-MAP.md` and `BTC-EXECUTOR-INSTRUCTIONS.md` among them.
2. Any change to a definition or a constant of `adv3.py` or `adv3-bot.py` but those §4.1 names: G-RULE reads both.
3. Any read, copy, print or hash of anything under `/etc/adv3-bot/`, and any request to Telegram or to Binance by this TZ's own commands, but two: G-RENDER runs the service copy's bot, whose `Data`, `live_report`, `liquidity` and `forming_candles` read Binance's public futures market, and P-START runs the bot's own `--probe`, whose function reads the token to send `getMe` and prints the bot's username and neither the token nor a chat id. The unit makes its own requests.
4. Any `systemctl` verb but `show`, `list-timers`, `is-enabled`, `kill --signal=SIGTERM adv3-bot.service` (B-KILL, B-KILL2) and, on a FAIL of UNIT-OLD, `disable --now adv3-bot.service` (K-40). No `daemon-reload`, `enable`, `restart`, `start`, `stop` or `mask`.
5. Any change to a capture unit, its store, either archive's timer or ledger: `systemctl show` and `list-timers`, `du`, and under the recorder's root `find`, `grep -c` and `df` read them.
6. Any write to the unit's record but `check-done` by the marks above: `journal.jsonl`, `offset`, `daily-sent` and `service.log` are the unit's.
7. A dataset or a binary in git history.
8. A coin, a price, a size or a card from the live replies, from the render's scratch journal or from the bot's own journal printed in the report or the logs: G-RENDER, G-FIRST and the marks print counts and labels alone, and no file of the work tree is printed, whole or in part, but by a command this TZ names (map §7 item 118). The day's cards are the Boss's to read in his chat.
9. The report on `main` before the branch is pushed and its pull request opened (contract §4.1).

**Exemptions.** The requests of item 3, each by the service copy's own code, as TZ-39's P-START and G-RENDER made theirs; the scratch journal of item 8, `render-state/journal.jsonl`, a copy of the bot's own taken by `I render` and removed with the tree, never printed and never kept; and item 6's `check-done`, a slot and nothing else, printed by the marks, `I host` and §3.7.

---

## 3. The work, in this order

### 3.1 The branch and its files

```
git -C /root/btc-5m-twap fetch origin
I number
git -C /root/btc-5m-twap worktree add -b tz-40-strong-every-rank /root/tz40-work/wt origin/main
```

`I number` must print `READING NUMBER: PASS - 2 of 2` again, or BLOCKED. Then §0.1's script again, verbatim but for its argument, `/root/tz40-work/wt`; it must print the same lines, bytes and SHA-256 as at §0.1. Then:

```
git -C /root/tz40-work/wt add advisor/adv3.py advisor/adv3-bot.py advisor/selftest-adv3.py research/tz40-advisor-strong.py
git -C /root/tz40-work/wt diff --cached --name-status
git -C /root/tz40-work/wt diff --cached --numstat
```

`--name-status` must print exactly four lines — `M` for the three advisor files, `A` for the checker — and `--numstat` exactly `439	128	advisor/adv3-bot.py`, `35	11	advisor/adv3.py`, `21	0	advisor/selftest-adv3.py` and `1436	0	research/tz40-advisor-strong.py`, or BLOCKED. Commit them alone; `git ls-remote origin` (§0.5); push with `git push -u origin tz-40-strong-every-rank` — through `credential.helper=!gh auth git-credential` where the URL's credential is refused (map §6, git remote) — and open the pull request against `main`. A failed assert here is BLOCKED.

### 3.2 The self-tests and G-RULE

```
P /root/tz40-work/wt/advisor/selftest-adv3.py
P /root/tz40-work/wt/advisor/adv3-bot.py --selftest
I selftest
I rule
```

They must print `SELFTEST-ADV3 PASS: 57 of 57 checks passed`, `SELFTEST PASS: 128 of 128 checks passed`, `SELFTEST PASS: 86 of 86 checks passed` and `READING RULE: PASS - 10 of 10`. The first three reach no network — `I selftest` runs the stage's own bot on a synthetic market with Binance stood in for (§5); `I rule` reads `git show origin/main:` of `adv3.py`, `adv3-bot.py`, `RULE-ADV-3.txt`, the unit file and TZ-38's report, and the branch's files. A red check stops the run here, and it goes to §3.7 and §9.

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

One `reclaim` names every earlier directory and must print `RECLAIM PASS` before any removal; then one `rm -rf` and one `test -e` a directory, the last reading `exit=1`. TZ-35's checker is `main`'s, frozen by the map's table, and its `reclaim` refuses a directory born with a running claude process and any path that is not a UUID directory under `/tmp/` whose parent's name carries `btc-5m-twap`. Map §3 expects TZ-39's two directories (§0.3) unless a reboot emptied `/tmp`; the live session of 2026-10-30 is not touched. If `scratch` names none earlier, the block is recorded as empty and skipped. **Where the classifier refuses it, the Boss runs it as one line** (map §6, sandbox limit; §7 items 124 and 138), the Executor writing in every earlier directory's full path, one `rm -rf` and one `test -e` a directory, all chained to the `reclaim`'s `exit=0`, which it reaches only after `RECLAIM PASS`:

```
{ date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/btc-5m-twap/research/tz35-advisor-deploy.py reclaim <D1> <D2>; echo "exit=$?"; } >> /root/tz40-work/logs/12-reclaim-scratch.log 2>&1 && tail -n 1 /root/tz40-work/logs/12-reclaim-scratch.log | grep -qx 'exit=0' && { date -u +%FT%T.%NZ; rm -rf <D1>; echo "exit=$?"; test -e <D1>; echo "exit=$?"; rm -rf <D2>; echo "exit=$?"; test -e <D2>; echo "exit=$?"; } >> /root/tz40-work/logs/12-reclaim-scratch.log 2>&1
```

**It holds back nothing of §3.4 to §3.6**, which read none of what it removes (map §7 item 140).

### 3.4 B-DEPLOY, then COPY and G-RENDER

All of §3.1 and §3.2 PASS first. Then **B-DEPLOY**, which waits for its band and records its mark inside the block:

```
until s=$(( $(date +%s) % 86400 )); { [ $s -ge 27000 ] && [ $s -le 40800 ]; } || { [ $s -ge 44400 ] && [ $s -le 84000 ]; }; do sleep 5; done; { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz40-work/stage/research/tz40-advisor-strong.py mark deploy && cp -p /root/adv3-bot-svc/adv3.py /root/tz40-work/adv3.before && cp -p /root/adv3-bot-svc/adv3-bot.py /root/tz40-work/bot.before && cp -p /root/adv3-bot-svc/commit.txt /root/tz40-work/commit.before && git -C /root/tz40-work/wt show origin/tz-40-strong-every-rank:advisor/adv3.py > /root/adv3-bot-svc/adv3.py.new && git -C /root/tz40-work/wt show origin/tz-40-strong-every-rank:advisor/adv3-bot.py > /root/adv3-bot-svc/adv3-bot.py.new && mv /root/adv3-bot-svc/adv3.py.new /root/adv3-bot-svc/adv3.py && mv /root/adv3-bot-svc/adv3-bot.py.new /root/adv3-bot-svc/adv3-bot.py && git -C /root/tz40-work/wt rev-parse origin/tz-40-strong-every-rank > /root/adv3-bot-svc/commit.txt; echo "exit=$?"; } >> /root/tz40-work/logs/20-b-deploy.log 2>&1
```

07:30:00 to 11:20:00 and 12:20:00 to 23:20:00 UTC are seconds `27,000` to `40,800` and `44,400` to `84,000` of the day. `exit=0`, or B-ROLLBACK (§4.4). The running process keeps the old code in memory until it is signalled. Then:

```
I copy >> /root/tz40-work/logs/21-copy.log 2>&1; echo "exit=$?" >> /root/tz40-work/logs/21-copy.log
timeout 900 I render >> /root/tz40-work/logs/22-render.log 2>&1; echo "exit=$?" >> /root/tz40-work/logs/22-render.log
```

`I copy` must print `READING COPY: PASS - 5 of 5`; `I render` imports the service copy's bot, points its `STATE` at `/root/tz40-work/render-state/` holding a copy of the bot's own `journal.jsonl`, replaces Telegram by a stand-in, answers seven commands and runs both checks on `fapi.binance.com`'s live data, prints its peak resident set and its time, and must print `READING RENDER: PASS - 22 of 22`. A FAIL of either, or a `timeout`, is B-ROLLBACK (§4.4), and nothing is signalled.

### 3.5 P-START, B-KILL, then UNIT-NEW and G-FIRST

Only after COPY and G-RENDER PASS. **P-START**, CANON hard rule 14's proof of the request path, through the service copy's own functions:

```
P /root/adv3-bot-svc/adv3-bot.py --probe >> /root/tz40-work/logs/23-probe.log 2>&1; echo "exit=$?" >> /root/tz40-work/logs/23-probe.log
```

It must print `READING P-START: served - 5 of 5 endpoints` (§4.3). A FAIL is B-ROLLBACK (§4.4), and nothing is signalled. Then **B-KILL**, its mark inside the block:

```
until s=$(( $(date +%s) % 86400 )); { [ $s -ge 27000 ] && [ $s -le 42600 ]; } || { [ $s -ge 44400 ] && [ $s -le 85800 ]; }; do sleep 5; done; { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz40-work/stage/research/tz40-advisor-strong.py mark kill && systemctl kill --signal=SIGTERM adv3-bot.service; echo "exit=$?"; } >> /root/tz40-work/logs/24-b-kill.log 2>&1
```

07:30:00 to 11:50:00 and 12:20:00 to 23:50:00 UTC are seconds `27,000` to `42,600` and `44,400` to `85,800`. **`I mark kill` refuses — and writes and signals nothing — where `check-done` does not name the latest slot**, 00:10 or 12:10 UTC of the day: the running process then owes a check, and the run goes to B-ROLLBACK (§4.4) with the unit not signalled; **otherwise it writes `check-done` to the day before's `fact`** by one rename, reads it back, and records both values in `state.json`, and the signal follows. At least 45 s later, then every 15 s while it prints `NOT YET` and exits `3`, and for at most 100 s after the mark: `I unit new` — **UNIT-NEW**, `READING UNIT-NEW: PASS - 9 of 9`. Then every 15 s while it prints `NOT YET` and exits `3`, for at most 900 s after the mark: `I first` — **G-FIRST**, `READING FIRST: PASS - 7 of 7`. Each run's output is appended to `25-unit-new.log` and `26-first.log`. A FAIL of either is B-ROLLBACK (§4.4).

### 3.6 The Boss's one paste — CANON hard rule 14

**The Executor tries each block once; a refused one is handed to the Boss unchanged, with the paste below** (map §7 item 138). Each step's output goes to the log the Executor's own step names, under a `date -u` line and appended, each step gated on the one before it by that log's last line, and the bands wait in the text (map §7 item 124). **P-BOSS-A** is handed over where B-DEPLOY is refused, and only while B-DEPLOY's band is open — 07:30:00 to 11:20:00 or 12:20:00 to 23:20:00 UTC — so that B-KILL's band is open too when the paste reaches it and its waits are seconds; the Executor waits for that band before handing it over. It runs B-DEPLOY, COPY, G-RENDER — which times itself — P-START, B-KILL, UNIT-NEW and G-FIRST:

```
until s=$(( $(date +%s) % 86400 )); { [ $s -ge 27000 ] && [ $s -le 40800 ]; } || { [ $s -ge 44400 ] && [ $s -le 84000 ]; }; do sleep 5; done; { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz40-work/stage/research/tz40-advisor-strong.py mark deploy && cp -p /root/adv3-bot-svc/adv3.py /root/tz40-work/adv3.before && cp -p /root/adv3-bot-svc/adv3-bot.py /root/tz40-work/bot.before && cp -p /root/adv3-bot-svc/commit.txt /root/tz40-work/commit.before && git -C /root/tz40-work/wt show origin/tz-40-strong-every-rank:advisor/adv3.py > /root/adv3-bot-svc/adv3.py.new && git -C /root/tz40-work/wt show origin/tz-40-strong-every-rank:advisor/adv3-bot.py > /root/adv3-bot-svc/adv3-bot.py.new && mv /root/adv3-bot-svc/adv3.py.new /root/adv3-bot-svc/adv3.py && mv /root/adv3-bot-svc/adv3-bot.py.new /root/adv3-bot-svc/adv3-bot.py && git -C /root/tz40-work/wt rev-parse origin/tz-40-strong-every-rank > /root/adv3-bot-svc/commit.txt; echo "exit=$?"; } >> /root/tz40-work/logs/20-b-deploy.log 2>&1; tail -n 1 /root/tz40-work/logs/20-b-deploy.log | grep -qx 'exit=0' && { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz40-work/stage/research/tz40-advisor-strong.py copy; echo "exit=$?"; } >> /root/tz40-work/logs/21-copy.log 2>&1 && tail -n 1 /root/tz40-work/logs/21-copy.log | grep -qx 'exit=0' && { date -u +%FT%T.%NZ; timeout 900 nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz40-work/stage/research/tz40-advisor-strong.py render; echo "exit=$?"; } >> /root/tz40-work/logs/22-render.log 2>&1 && tail -n 1 /root/tz40-work/logs/22-render.log | grep -qx 'exit=0' && { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/adv3-bot-svc/adv3-bot.py --probe; echo "exit=$?"; } >> /root/tz40-work/logs/23-probe.log 2>&1 && tail -n 1 /root/tz40-work/logs/23-probe.log | grep -qx 'exit=0' && { until s=$(( $(date +%s) % 86400 )); { [ $s -ge 27000 ] && [ $s -le 42600 ]; } || { [ $s -ge 44400 ] && [ $s -le 85800 ]; }; do sleep 5; done; } && { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz40-work/stage/research/tz40-advisor-strong.py mark kill && systemctl kill --signal=SIGTERM adv3-bot.service; echo "exit=$?"; } >> /root/tz40-work/logs/24-b-kill.log 2>&1 && tail -n 1 /root/tz40-work/logs/24-b-kill.log | grep -qx 'exit=0' && sleep 45 && for k in 1 2 3 4; do { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz40-work/stage/research/tz40-advisor-strong.py unit new; echo "exit=$?"; } >> /root/tz40-work/logs/25-unit-new.log 2>&1; tail -n 1 /root/tz40-work/logs/25-unit-new.log | grep -qx 'exit=3' || break; sleep 15; done; tail -n 1 /root/tz40-work/logs/25-unit-new.log 2>/dev/null | grep -qx 'exit=0' && for k in $(seq 1 60); do { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz40-work/stage/research/tz40-advisor-strong.py first; echo "exit=$?"; } >> /root/tz40-work/logs/26-first.log 2>&1; tail -n 1 /root/tz40-work/logs/26-first.log | grep -qx 'exit=3' || break; sleep 15; done; echo "P-BOSS-A ended"
```

**P-BOSS-B** is handed over where the Executor's B-DEPLOY, COPY, G-RENDER and P-START passed and B-KILL alone is refused, while B-KILL's band is open; it runs B-KILL, UNIT-NEW and G-FIRST:

```
tail -n 1 /root/tz40-work/logs/23-probe.log | grep -qx 'exit=0' && { until s=$(( $(date +%s) % 86400 )); { [ $s -ge 27000 ] && [ $s -le 42600 ]; } || { [ $s -ge 44400 ] && [ $s -le 85800 ]; }; do sleep 5; done; } && { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz40-work/stage/research/tz40-advisor-strong.py mark kill && systemctl kill --signal=SIGTERM adv3-bot.service; echo "exit=$?"; } >> /root/tz40-work/logs/24-b-kill.log 2>&1 && tail -n 1 /root/tz40-work/logs/24-b-kill.log | grep -qx 'exit=0' && sleep 45 && for k in 1 2 3 4; do { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz40-work/stage/research/tz40-advisor-strong.py unit new; echo "exit=$?"; } >> /root/tz40-work/logs/25-unit-new.log 2>&1; tail -n 1 /root/tz40-work/logs/25-unit-new.log | grep -qx 'exit=3' || break; sleep 15; done; tail -n 1 /root/tz40-work/logs/25-unit-new.log 2>/dev/null | grep -qx 'exit=0' && for k in $(seq 1 60); do { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz40-work/stage/research/tz40-advisor-strong.py first; echo "exit=$?"; } >> /root/tz40-work/logs/26-first.log 2>&1; tail -n 1 /root/tz40-work/logs/26-first.log | grep -qx 'exit=3' || break; sleep 15; done; echo "P-BOSS-B ended"
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
du -sb /root/tz40-work /root/adv3-bot-svc /var/lib/adv3-bot /var/lib/btc-rewardbook /var/lib/btc-pairbook /root/.claude
cat /root/tz40-work/state.json
```

The journal holds systemd's own lines for the unit; `service.log` the service's own — a start with the `check-done` it read, a refresh, a check sent or failed, a request answered — with no token, no chat id and no price, and a coin only where Binance failed to serve it. The next scheduled check — the 12:10 UTC fact check of the same day where the restart came before 11:50, else the 00:10 UTC signal check of the next — is the first the running unit's clock fires under this code; the next TZ's host gate reads it (H7); nothing in this TZ waits for it.

---

## 4. The gates — fixed here, before any of their data exists

| gate | population | PASS | false failure | power, against |
|---|---|---|---|---|
| **G-RULE** | `origin/main`'s `adv3.py`, `adv3-bot.py`, `RULE-ADV-3.txt` and the unit file, TZ-38's report, and the branch's files | 10 of 10 (§4.1) | `0` — the files, their syntax trees and the report's cells read directly | `1`, a rule function, `plan`, a constant, the unit or the rule text changed, a definition changed beyond Appendix A, or a quoted figure not TZ-38's |
| **SELFTESTS** | the three self-tests | 57 of 57, 128 of 128 and 86 of 86 | `0` | `1`, a changed expectation or a red check |
| **COPY** | the service copy | 5 of 5 (§4.3) | `0` | `1`, a file not Appendix A's or not the branch head's |
| **G-RENDER** | the service copy's bot answering seven commands and running both checks on live data, on a copy of its own journal | 22 of 22 (§4.3) | `0` — the replies, records and alerts read against plans, orders, stops and walks the checker makes itself from the same reports, candles and offers, and against fixed labels and limits | `1`, a STRONG coin omitted or not marked, a tag where it does not belong, a trade beyond N placed or one within N moved below, a loss beyond 1 % or 5 % or beyond the average risk, a stop beyond 14 %, methodology in a pushed message, an exit not alerted or alerted twice, a loud check without an alert, no pause between parts |
| **P-START** | five endpoints, six requests, through the service copy's own functions | `READING P-START: served - 5 of 5 endpoints` | `0` — each read directly | `1`, a refused request — `451`, `403` — or a reply of another shape |
| **UNIT-NEW** | the unit after the signal | 9 of 9 (§4.3) | `0` | `1`, a process not new, not the new code's, not started from the replay slot, a traceback, a capture unit moved |
| **G-FIRST** | the new process's first check: its record, `check-done` and its log | 7 of 7 (§4.3) | `0` | `1`, no check at the start, another slot or close, no message sent, a record without the STRONG at every rank, a loud check without an alert, a failure in the log |

**Family-wise false failure `0`:** every gate reads its quantity directly and none samples. A FAIL before B-DEPLOY is BLOCKED and deploys nothing; a FAIL of COPY, G-RENDER, P-START, B-KILL's mark or signal, UNIT-NEW or G-FIRST is B-ROLLBACK (§4.4).

### 4.1 G-RULE

`I rule` asserts ten. **Two files** are `main`'s, byte for byte: `advisor/RULE-ADV-3.txt` (`ee206e7c…`, and the `RULE` constant of the branch's `adv3.py`) and `deploy/systemd/adv3-bot.service` (`82acd8e4…`). **Three of `adv3.py`**, by `ast.dump` against `main`'s: the definitions that changed are exactly `assessment`, `card_lines` and `message`, none added, none removed; **the 46 others are identical** — the fourteen rule functions, `signs`, `signal`, `strength`, `true_range`, `unit`, `open_at`, `hold`, `close_at`, `simulate`, `states`, `ranking`, `simulate_strong`, `stats` and `funding_of`, with `report`, `card` and `trust` named among them — and of the assignments `PIT` changed, `BEYOND` and `BEYOND_TAG` added, none removed. **One of `PIT`:** it equals the figures of `CryptoReports/TZ-38-adv3-pit-validation-report.md` as committed (`f4a0ac3f…`), read from its §2.7 cell for cell — E4's reach shares and STRONG's top-5 share, E1's rule on *G*, E2's `p`, E5's median and its share of lists in profit, the size of *G*, and **E6's mean R a trade of STRONG with three places and with seven**, `0.7962` and `0.5084`. **Three of `adv3-bot.py`**: the definitions that changed are exactly `Telegram`, `alerts_of`, `candidate_lines`, `candidates`, `check`, `check_record`, `compose`, `event_lines`, `handle`, `item_lines`, `offers`, `plan_parts`, `selftest` and `top_n`, those added exactly `TooMany`, `alloc_fields`, `plan_strong`, `strong_all` and `volumes`, none removed; **the 43 others are identical** — `plan`, `ranked`, `route`, `Data`, `liquidity`, `follow`, `journal_scan`, `due`, `done_after`, `serve` and `main` named among them — **so the allocation's arithmetic, the schedule, the monitor and the candles' fetch are TZ-37's and TZ-39's**; of the assignments `CARD_KEYS` and `HELP` changed, `PACE` added, none removed. **One more:** the branch's three advisor files hash to Appendix A's.

### 4.2 The views — what Appendix A answers

**STRONG at every rank** (`strong_all`): every coin of the rule's order (`ranked`, the frozen `ranking` applied again to the coins it has not placed) whose sum of signs is `4` times its side and whose `|z|` is at least `adv3.STRONG_Z`, `1.0`. Its members among the TOP-3 are the report's STRONG. **A STRONG card beyond the TOP-3** carries «· вне ТОП-3» on its header (`adv3.BEYOND_TAG`), and a message showing one carries once «★ STRONG вне ТОП-3 — четыре знака совпадают и |z| ≥ 1, но это не измеряемая стратегия: форвард STRONG ведётся только по ТОП-3» (`adv3.BEYOND`).

| view | main section | then |
|---|---|---|
| «сигнал», «сигнал топ N» (N 1 to 7, default 3) | the rule's first N coins, each its card at `10,000` USDT and the risk given, ranked k of N, ★ STRONG wherever STRONG at every rank | **«Дополнительные STRONG-кандидаты»** — every STRONG coin ranked beyond N, the same card, its basis «ранг k — за ТОП-N»; then the other signals, without the coins shown |
| «сигнал <budget> топ <N>» (N 1 to 7, default 3) | TZ-37's `plan`, unchanged, over STRONG at every rank in the rule's order: the first N that pass — current prices, an entry, a stop within 14 % — placed with its shares, caps, liquidity, minimum and leverage, «Итог» theirs alone | **«Дополнительные STRONG-кандидаты»** — every other STRONG that passes, each `plan`'s one-trade allocation (the average risk, the same caps), «вне распределения — одна сделка», its correlation with the placed; the loss of all together against 5 %; then the rejected with their reasons and «Без STRONG среди первых N по силе — не берутся: …» |
| the 00:10 check | the close's message — events, the day's changes, the TOP-3 | the STRONG beyond the TOP-3, extra; «STRONG-кандидаты» — every STRONG coin at every rank at the default allocation: placed, «проходит, сверх 3 (одна сделка)» or its reason; the trades the cards offered; the weakened |
| the 12:10 check | its events — a stop touched, a new candidate with its plan, placed or «сверх 3 — как одна сделка» — and the zones left | — |

**The checks' rules otherwise are TZ-39's:** the slots and `check-done`, the trades the cards offered held by the rule's own functions, each alert sent once, the weakening as information, quiet unless an alert, one line where nothing is found — now also requiring the coins STRONG at every rank as at the check before. **A candidate alert** fires for a STRONG coin that passes the default allocation's limits — placed or among the more — and did not at the check before (`passing` in the record, now both). **The journal's records** gain: each card its `extra`; a check record its `strong_all` and its allocation's `more`, in the placed trades' shape, its `passing` both; an allocation record its `more`, its cards the placed and the more.

**Telegram:** the parts of one message `PACE`, `1.1` s, apart; a part refused with `429` waits `min(retry_after, 60) + 1` s and is sent again, twice at most, and a third refusal raises, as any other refusal did; the quiet flag on every part and every retry.

### 4.3 COPY, G-RENDER, P-START, UNIT-NEW and G-FIRST

**COPY** (`I copy`), five: the service copy holds `adv3.py`, `adv3-bot.py` and `commit.txt` and nothing else; `adv3.py` and `adv3-bot.py` hash to Appendix A's, two checks; `commit.txt` is 40 hex characters and a newline equal to the worktree's `HEAD` and to `origin/tz-40-strong-every-rank`; the branch's two files equal the service copy's byte for byte.

**G-RENDER** (`I render`), twenty-two, on the service copy's bot, its `Data`, `live_report`, `liquidity` and `forming_candles` reading `fapi.binance.com` — the last three wrapped so that the checker keeps what they returned — Telegram a stand-in that records each part and its notification flag, and `STATE` at `/root/tz40-work/render-state/`, a copy of the bot's own journal. The seven commands are «сигнал», «сигнал топ 7», «сигнал 10000 топ 3», «сигнал 15000 топ 5», «оценка», «помощь» and «привет», then the signal check and the fact check of the run's UTC day, each appended to the scratch journal. **The checker computes its own order** — every coin with a signal, a strength and a unit by `|z|` from the largest, ties in the coins' order — **its own STRONG** — four signs agreeing and `|z|` at least 1 — **and its own stop** for a card, by RULE-ADV-3's display rules (`own_order`, `own_strong`, `own_stop_pct`). (1) every command and both checks answered, no traceback and no failure in the bot's log; (2) every part's markup balances; (3) «сигнал»: the rule's first three ranked k of 3, then every STRONG beyond them, extra, ranked «за ТОП-3»; ★ STRONG exactly where the coin is STRONG at every rank and «вне ТОП-3» exactly where such a card ranks beyond 3; each card its basis, its invalidation and one confidence line reading the rung `1` or `0`; the footnote once where a tag shows; none of the methodology's labels; (4) «сигнал топ 7» the same at 7; (5) «оценка»: the rung and both next readings, the six ratings, the forward record, `+0,22 R` and `+0,04 R`, no `0,55`, and the line on STRONG beyond the TOP-3 with `+0,51 R` against `+0,80`; (6) the bot's constants are this TZ's — `STOP_MAX` `14.0`, `MIN_NOTIONAL` `5`, `LIQ_FRAC` `0.001`, `RISK_MAX` `1`, `RISK_ALL` `5`, `TOP_N` `3`, `COST` `0.001`, `LIST_MAX` `7`, `SLOTS` 00:10 and 12:10 UTC, `RELIABILITY` `1`, `PACE` `1.1`, `STRONG_Z` `1.0`; (7) each allocation reply is the bot's own `plan_parts` of the `plan_strong` the checker recomputes from the very report and volumes it was made from; (8) to (13) its six limits: the placed are the first N STRONG at any rank that pass the checker's own limits and the more the rest, both in rank order; every STRONG coin placed, more or named with a reason, once; every trade an entry and a stop within 14 %, the checker's own; each placed loss within 1 % and all within 5 %, each more within the average risk; whole positions of at least 5 USDT, the placed within the budget, free the budget less them; the rule's leverage, the margin covering it, the liquidity cap; (14) the Boss's fields in each allocation reply — the more under their heading with the loss of all together, and «больше лимита 5%» exactly where it exceeds — and no six ratings; (15) «сигнал 15000 топ 5» places at most five and says nothing of three; (16) «помощь» and «привет» answer `HELP` and nothing else; (17) the signal check is quiet exactly when it holds no alert, every part sent with that flag, one line exactly where it finds nothing, else the TOP-3 and the STRONG beyond it by (3)'s reading, its candidates and its followed trades with no methodology, its events heading it exactly when it has alerts and its weakening line exactly when it has one; (18) the fact check is quiet exactly when it holds no alert, one line exactly where it finds neither an alert nor a zone left, and offers no card but a new candidate's; (19) **every alert of both checks is the first exit of an offered trade by the checker's own walk** — a candle reaching the stop, else a close whose sum of signs, counted by the checker over the closes at least 14, 28, 56 and 112 days before, leaves the side — or the forming candle through its stop, **every such exit not alerted before is alerted, none twice across the checks**, and the candidates are exactly the STRONG coins the plan places or holds as more that the check before did not pass; (20) both records carry their slot, the 42 coins' state ranked by the checker's order, the six ratings, the coins that pass, the STRONG at every rank by the checker's reading, the more, and each card its `extra`; (21) the scratch journal holds, after the bot's own records, `request`, `request`, `alloc`, `alloc`, `assess`, `check`, `check`; (22) the bot's own `journal.jsonl`, `offset`, `daily-sent` and `check-done` hash as before the run. **Only counts and labels are printed:** each reply's size in characters and parts, the STRONG at every rank, the trades placed and more per allocation, and for each check its flags, its parts, its alerts by kind, the offers read, the followed trades, its cards and how many extra, the coins that pass, the zones left and the forming candles read; then `PEAK <bytes> bytes resident` and its wall and processor seconds. **A day with no STRONG beyond the TOP-3 reads 22 of 22 with no extra card**, and then proves the new views on live data only where they are empty and on the self-tests' synthetic market — twelve STRONG of twelve, nine beyond the TOP-3 — in full; the report prints the counts.

**P-START** is `adv3-bot.py --probe`, every reply asserted served and parsed, TZ-39's: **P-KLINES** — `/fapi/v1/klines?symbol=BTCUSDT&interval=1d&limit=1500` serves closed daily candles, the last at most two days old, each of four prices with its close positive, and `/fapi/v1/klines?symbol=BTCUSDT&interval=1d&limit=2` the candle forming since 00:00 UTC, its high at or above its open and last and its low positive and at or below them; **P-FUNDING** — `/fapi/v1/fundingRate?symbol=BTCUSDT&startTime=<2026-10-27 00:00 UTC>&limit=1000` serves settlements, each a number; **P-MARKS** — `/fapi/v1/premiumIndex` serves a positive mark price for every one of the 42 coins' perpetuals; **P-INTERVALS** — `/fapi/v1/fundingInfo` serves the adjusted funding intervals, each a positive number of hours; **P-TELEGRAM** — `getMe` answers `is_bot` true and a username, which it prints. Six requests to five endpoints. **Every header fixed:** to Binance `User-Agent: adv3-advisor/1`, beside `urllib`'s own `Accept-Encoding: identity`, `Host` and `Connection: close`; to Telegram `User-Agent: adv3-bot/1` and `Content-Type: application/json`, beside `urllib`'s `Content-Length`, `Accept-Encoding: identity`, `Host` and `Connection: close`. A refused request is never retried but for a network error, `418`, `429` or a `5xx`, three times after 1, 3 and 5 s (`adv3.get`); Telegram's `call` has one try, and `send` retries a part only on `429`. The unit's own requests at its checks go through the same functions and headers.

**UNIT-NEW** (`I unit new`), nine, read against the `kill` mark's snapshot: the unit `active`, `running`, `enabled`; a new `MainPID` and `NRestarts` one more; the process started after the mark and within 90 s of it; its argv the unit's exact one, alone; the service copy's `adv3.py` and `adv3-bot.py` Appendix A's and the process started after B-DEPLOY's mark; the unit file unchanged; **`service.log` showing the new process serving from the `check-done` the mark wrote** — its `serving the pinned chat: pid <pid> offset <n> check-done <slot>` line naming the day before's `fact`; no traceback since the mark; the three capture units active with their `MainPID` and `NRestarts` as at the mark.

**G-FIRST** (`I first`), seven, from the journal's records stamped since the `kill` mark, `check-done` and `service.log`'s lines since the mark: exactly one check record; it is the day's signal check, of the close of the day before, under rule `ee206e7c…`; it was sent, its Telegram message ids integers; it holds the 42 coins' state, the six ratings, its alerts, the coins that pass, the STRONG at every rank and the allocation's more, each card its `extra`, and is quiet exactly when it holds no alert; `check-done` reads the day's `signal` where the mark came before 12:10 UTC and its `fact` where after — a replay read within 900 s of a mark at or before 11:50 ended before 12:10, and one after a mark at or after 12:20 marks the fact slot done too (`done_after`); the log since the mark shows the new pid serving from the replay slot, the check sent and no check failed and no traceback; the journal ends in a newline and every line from that record on parses. **NOT YET** while no check record stands since the mark and 900 s have not passed. Printed beside it: the check's flags, its message count, its alerts by kind, its followed trades, its cards and how many extra, the coins that pass, the STRONG at every rank and `check-done` — never a coin or a price.

### 4.4 The stops — CANON hard rule 14

**The unit's restart policy is TZ-35's, unchanged** — `Restart=always`, `RestartSec=30`, `RestartPreventExitStatus=3 4` — and so is its stop, K-35, `systemctl disable --now adv3-bot.service`, which K-40 repeats. **B-ROLLBACK**, on a FAIL of COPY, G-RENDER, P-START, B-KILL's mark or signal, UNIT-NEW or G-FIRST, at once, the Executor's own: the two files and `commit.txt` return to what B-DEPLOY saved, and **`I mark rollback` writes the kill mark's `check-done` back where it still reads the replay slot** — where the new process never ran the replay, so that the old code does not replay the day's message at its start — and leaves it where the new process moved it.

```
{ date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz40-work/stage/research/tz40-advisor-strong.py mark rollback && cp -p /root/tz40-work/adv3.before /root/adv3-bot-svc/adv3.py.new && cp -p /root/tz40-work/bot.before /root/adv3-bot-svc/adv3-bot.py.new && mv /root/adv3-bot-svc/adv3.py.new /root/adv3-bot-svc/adv3.py && mv /root/adv3-bot-svc/adv3-bot.py.new /root/adv3-bot-svc/adv3-bot.py && cp -p /root/tz40-work/commit.before /root/adv3-bot-svc/commit.txt; echo "exit=$?"; } >> /root/tz40-work/logs/30-b-rollback.log 2>&1
sha256sum /root/adv3-bot-svc/adv3.py /root/adv3-bot-svc/adv3-bot.py; cmp /root/adv3-bot-svc/commit.txt /root/tz40-work/commit.before; echo "cmp exit=$?"; cat /var/lib/adv3-bot/check-done
```

The second line is the Executor's own read. `exit=0`, the `sha256sum` printing `c19572dc…` and `ca989b6f…` and `cmp` exit `0`, or the run is BLOCKED with the files' state named. Where the unit was **not** signalled (a FAIL of COPY, G-RENDER, P-START, or B-KILL's mark or signal) that is all: the running process never loaded the new files, and it never reads `check-done` again. **B-KILL's signal counts as not delivered only where `systemctl show adv3-bot.service -p MainPID -p NRestarts` still reads the pid and the restart count its mark printed**; where either moved, the unit was signalled. Where it **was** (a FAIL of UNIT-NEW or G-FIRST), the signal follows, its mark inside the block, in the band of §3.5:

```
until s=$(( $(date +%s) % 86400 )); { [ $s -ge 27000 ] && [ $s -le 42600 ]; } || { [ $s -ge 44400 ] && [ $s -le 85800 ]; }; do sleep 5; done; { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz40-work/stage/research/tz40-advisor-strong.py mark kill2 && systemctl kill --signal=SIGTERM adv3-bot.service; echo "exit=$?"; } >> /root/tz40-work/logs/31-b-kill2.log 2>&1
```

and at least 45 s later `I unit old`, each run appended to `32-unit-old.log` (every 15 s while it prints `NOT YET`, at most 100 s after that mark) — **UNIT-OLD**, `READING UNIT-OLD: PASS - 10 of 10`: UNIT-NEW's nine read against the second mark with TZ-39's `adv3.py` and `adv3-bot.py` — the old process serving from the `check-done` the second mark read, a slot it may owe and run then — and `NRestarts` two more than at the first mark. The `check` records the new process left stay, and the report names them.

**K-40**, on a FAIL of UNIT-OLD only — the advisor is then stopped, and the Boss is told:

```
{ date -u +%FT%T.%NZ; systemctl disable --now adv3-bot.service; echo "exit=$?"; } >> /root/tz40-work/logs/33-k40.log 2>&1
```

by the classifier route where refused (the Boss runs the block unchanged), verified at least 30 s later by `I stopped`, appended to `34-stopped.log`, which must print `READING STOPPED: PASS - 2 of 2`. **Under PASS neither B-ROLLBACK nor K-40 is run.**

### 4.5 What a PASS establishes, and what it does not

The service copy's `adv3.py` and `adv3-bot.py` are Appendix A's and the unit runs them; the rule, its fourteen functions with `report`, `card` and `trust`, the rule text, the unit, TZ-37's `plan`, the schedule and the monitor are what TZ-35 to TZ-39 deployed; the seven commands and both checks are answered on live data with the shapes §4.2 fixes, every STRONG coin at every rank shown, marked where it belongs and sized by the allocation's own arithmetic; the new process replayed the day's signal check at its start and sent it, its parts paced. **Not established:** that a day with STRONG beyond the TOP-3 was among G-RENDER's — the self-tests prove the views on a synthetic market of twelve STRONG, and the report prints the counts; that Telegram's `429` was met — the self-tests prove the wait and the retry on stand-ins; that the 00:10 and 12:10 checks fire on their own clock under this code — H7 read it of TZ-39's, and the next TZ's host gate reads it of this; that the Boss's Telegram shows the messages as the Architect expects; that the followed trades are the Boss's; **that STRONG beyond the TOP-3 earns** — no record measures it, in sample it made less a trade than the TOP-3's, and the forward record, read after 2027-10-28, measures the rule and the TOP-3's STRONG and none of the sizes; and anything about the market to come.

---

## 5. The files

**`advisor/adv3.py`** — replaced: `card_lines` marks a STRONG card beyond the TOP-3 with `BEYOND_TAG` and gives a card marked `extra` its rank beyond the list; `message` puts the cards marked `extra` under «Дополнительные STRONG-кандидаты» after the TOP-N and adds `BEYOND` once where a tag shows; `assessment` adds the line on STRONG beyond the TOP-3 and E6's figures; `PIT` gains `mean_R_P3` and `mean_R_P7`; `BEYOND_TAG` and `BEYOND` added. Every other line, the rule's fourteen functions among them, is TZ-39's. **`advisor/adv3-bot.py`** — replaced: `strong_all`; `top_n` with ★ at every rank and the extra cards; `volumes`; `plan_strong` over TZ-37's `plan`; `item_lines` with the tag and the more's fields; `plan_parts` with «Дополнительные STRONG-кандидаты» and the loss of all together; `candidates`, `alerts_of`, `event_lines`, `candidate_lines` and `compose` over the placed and the more; `alloc_fields`, `check_record`, `check`, `handle` and `offers` for the record's new fields; `TooMany` and `Telegram.call`, `send` and `send_part` for the pace and the `429`; `CARD_KEYS` with `extra`; `PACE`; `HELP`; and `selftest`, 128 checks offline — 96 of TZ-39's 106 by name, two of them, `plan_parts`' fields and confidence lines, now on `plan_strong`'s golden scenario; the other ten rewritten for the new views — `HELP`, `top_n`, the TOP-7 message, the synthetic market's allocation, `plan_parts`' markup, two of `compose`'s, the end-to-end signal check and two of `handle`'s; and twenty-two more: the pace and three of the `429` on stand-ins, `call`'s refusals, an allocation's more offered, `strong_all` on the synthetic market and with `top_n` on a mixed one, the TOP-1 message, no extra where none is STRONG beyond the TOP-3, `plan_strong`'s two golden cases by hand — the placed pair `731` and `487` USDT, the more `490` USDT at the average risk with its correlation `0.5` — seven requested and one, the 5 % warning, 400 random scenarios, `plan_parts`' extra section and its warning, three of `compose`'s — the quiet condition, the signal check's sections and the fact check's more — the record's new fields and `time.sleep` restored. **`advisor/selftest-adv3.py`** — replaced: TZ-39's 53 checks and four more — the tag, the extra card's basis, the message's extra section and footnote, the assessment's line with E6's figures — 57. **`research/tz40-advisor-strong.py`** — this TZ's checker: `fingerprint`, `host`, `number`, `rule`, `selftest`, `mark`, `copy`, `render`, `unit`, `first`, `keep` and `stopped`. Where a reading can be a pure function it is — `parse_map`, `tree_checks`, `report_sections`, `pit_from_report`, `own_order`, `own_strong`, `own_stop_pct`, `plan_invariants`, `sign_sum`, `walk`, `alert_checks`, `card_blocks`, `list_ok`, `render_checks`, `unit_checks`, `first_checks`, `slot_instant`, `latest_slot_text`, `replay_text`, `clock_checks`, `served_from`, `log_since`, `records_since`, `memory_gate`, `count_kind`, `number_reading`, `kept_files` — and its self-test runs each on stand-ins with a negative control for every one that can fail, and `render_run`, the render's own pipeline, **on the stage's bot with a synthetic market and Binance stood in for**: 22 of 22, every alert kind met, twelve STRONG, nine extra, three placed and nine more, and twenty-four negative controls on its output. `host`, `copy`, `mark`, `unit`, `first`, `keep` and `stopped` read the host and are exercised there; of the unit's record `mark kill` and `mark rollback` write `check-done` alone, and every mark writes `state.json`. It starts, stops and signals nothing; its `render` runs the service copy's bot. Standard library alone, under `/root/tz04a-env`.

---

## 6. Cost

Measured by the Architect on 2026-11-01 under Python 3.12.3 and 3.13.18 and taken at the population's upper bound.

| check | population | measured | bound |
|---|---|---|---|
| the three self-tests | 57, 128 and 86 checks, no network | `0.13` to `0.24` s, `0.83` to `1.16` s and `0.49` to `0.60` s of wall under 3.12.3, three runs each on the bytes sent; peaks at most `26,140,672`, `37,486,592` and `40,071,168` bytes | `30` s each |
| G-RULE and FINGERPRINT | `git show` of five paths, four syntax trees, TZ-38's report, the map's 59 rows | `0.38` to `0.68` s together, three runs; peak at most `42,287,104` bytes | `5` s a run |
| G-RENDER | one process: 84 requests of `Data` over six threads, once; two for the marks and the funding intervals at each of seven reports; one for the volume of each coin STRONG at every rank, at most 42, at each of two allocations and two checks, six at a time; one forming candle for each coin of an offered trade at the fact check, at most 42; seven replies and two checks, their parts `1.1` s apart | under Python 3.12.3, five runs a case: `4.2` to `5.1` s of processor on the archive's candles of the 42 coins to the close of 2026-10-30 — 13 offers, 3 STRONG at every rank, none beyond the TOP-3 — and `58,220,544` bytes at its peak (§0.4); `4.6` to `5.9` s with the ninety-day journal; on the archive's heaviest close, 2026-09-27, with that journal — 35 STRONG, 32 extra cards in «сигнал» and in the signal check — `5.1` to `6.1` s of processor and `23.9` to `27.0` s of wall, the paces of up to six parts a message among them, and `58,134,528` bytes; TZ-39's live render on the host took about 17 s of wall (its report, §2.5) | `900` s of wall, the `timeout`; `30` s of processor |
| P-START | six requests to five endpoints, one after another | TZ-39's six, every reply within the second at 06:51:08 UTC (its report, §2.6) | `675` s of wall at worst — five requests at `129` s and one at `30` s — without processor |
| UNIT-NEW and G-FIRST | `systemctl show`, `/proc`, the journal and the log | under `1` s a run | `30` s; at most 4 and 60 runs |

**Single-session processor at most `630` s at those bounds** — the self-tests `90`, G-RENDER and P-START `30`, at most `90` checker runs at `5` s, `450`, and the `reclaim`, `git` and `systemctl` commands `60` — **under `3,600`, so nothing is sampled.** **Wall clock about 45 minutes:** §0 to §3.3 about 15 minutes; §3.4 and §3.5 about 8, the restart's 30 s and the replay's minute among them; §3.7 and §9 about 5; the report about 17. **`88` minutes with every `timeout` and every request at its bound** — `10 + 5 + 2 + 5 + 16 + 12 + 16 + 2 + 17 + 3` (§0 with the memory re-read; §3.1; §3.2; §3.3; B-DEPLOY, COPY and G-RENDER at 900 s; P-START at 675 s; the signal, UNIT-NEW and G-FIRST at 945 s; §3.7; the report; §9) — and up to 30 more where a paste waits for the Boss; plus a wait for B-DEPLOY's band of at most 8 h 10 min, from 23:20:00 to 07:30:00 UTC. **The host pays, after the session:** two checks a day of the unit's own — at 00:10 at most 128 requests to `fapi.binance.com`, 84 for the candles and funding, two for the marks and the funding intervals and at most 42 for the volumes; at 12:10, for a process that ran the 00:10 check, at most 86, the two, the 42 and one forming candle for each coin of an offered trade; a few seconds of processor each, `1.66` s at most under Python 3.12.3 in the simulation below; messages of up to eight parts on a heavy day, each part `1.1` s after the one before; and a journal growing about `99,000` bytes a day in a trend — **the Architect's simulation of the new code's two checks a day over the archive's 90 closes from 2026-08-01 to 2026-10-29, the journal accumulating: `8,917,445` bytes, at most `141,145` a record and `49,490` on average, at most 593 followed trades** [modelled: the archive's candles, marks at the close, every card offered at market] — about `36,000,000` bytes a year at that rate, against TZ-39's `21,000` a day; the unit's process with that journal held `55,922,688` bytes at its peak through two checks and four commands — «сигнал», «сигнал топ 7», «сигнал 210000 топ 7» and «оценка» — under Python 3.12.3, under its `MemoryMax=128M`.

---

## 7. Validation

| # | check | count |
|---|---|---|
| **V1** | §0.2's fingerprint | `READING FINGERPRINT: PASS - 68 of 68`: revision `2026-11-01-a`; 6 anchors, 4 re-derived; 59 rows, 56 of 56 `frozen` equal |
| **V2** | §0.3's host gate | `READING HOST: PASS - 19 of 19`; the check records' slots and delays; the memory figures of the first read and of the second, if one was made |
| **V3** | §0.5's NUMBER, at §0.5 and at §3.1 | `READING NUMBER: PASS - 2 of 2` each, the `TZ-40-` path printed; the branch count `0` |
| **V4** | §0.1's and §3.1's files | 4 of 4 hashes asserted at each, lines and bytes; the branch's diff naming exactly `M`, `M`, `M`, `A`, and `--numstat` exact |
| **V5** | the self-tests | `57 of 57`, `128 of 128`, `86 of 86` |
| **V6** | G-RULE | `READING RULE: PASS - 10 of 10` |
| **V7** | B-DEPLOY | `exit=0`; the mark printed |
| **V8** | COPY | `READING COPY: PASS - 5 of 5` |
| **V9** | G-RENDER | `READING RENDER: PASS - 22 of 22`; the printed counts; `PEAK` and the seconds |
| **V10** | P-START | `READING P-START: served - 5 of 5 endpoints`, each line printed |
| **V11** | B-KILL and UNIT-NEW | `exit=0`; the mark with `check-done` before and after; `READING UNIT-NEW: PASS - 9 of 9`, both pids, both instants |
| **V12** | G-FIRST | `READING FIRST: PASS - 7 of 7`; the printed counts |
| **V13** | contract §4.2's self-check | run after the push and the pull request and before the report's commit |
| **V14** | §3.7's closing reads | every read printed |
| **V15** | B-RECLAIM-SCRATCH and §9's `keep` | files considered, copied and held; the store's count after equal to before plus the copies |
| **V16** | §9's removals | `git worktree remove` without `--force` exit `0`; `test -e` exit `1` for `/root/tz40-work` and each directory removed; `git worktree list` naming `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else |
| **V17** | every block refused and every paste the Boss ran | its refusal's text, the paste, when he ran it and every log line it appended |

---

## 8. The report

`CryptoReports/TZ-40-strong-every-rank-report.md`, in contract §8's order. **In its first ten lines:** NUMBER at both reads; G-RULE; the three self-tests; B-DEPLOY, COPY, G-RENDER — with the STRONG at every rank, the trades placed and more per allocation, each check's alerts by kind and extra cards, and the render's peak — and P-START; B-KILL with `check-done` before and after, UNIT-NEW and G-FIRST with the pids and the replayed check's flags; whether a rollback ran; whether the unit runs, and how that was verified; every block refused and who ran it. Beyond what V1 to V17 print: every mark's instant; the unit's journal lines; each memory and free-space read with its instant and bound; the commit and the pull request; §9's counts and removals; and every file the run wrote, by SHA-256, but the bot's own root and the render's scratch journal. **It never prints the token, the chat id, the content of any file under `/etc/adv3-bot/` but `check-done`'s slot, or a coin, a price or a size from the live replies or a journal** (§2 item 8). The report is drafted in the primary checkout `/root/btc-5m-twap` before B-RECLAIM-OWN and committed after it.

---

## 9. Reclaim — the host left clean (CANON hard rule 15)

**What a file is kept for:** `I keep` copies every file under `logs/`, `state.json`, `adv3.before`, `bot.before` and `commit.before` into `/root/btc-forensics/` as `tz40-work--<path with - for />`, by exclusive create, and verifies each hash; a name already there with the same hash is counted as held, and with another a failed assert. The branch worktree is not copied: `keep` asserts that `git status --porcelain --ignored` in it prints nothing and that its `HEAD` is its upstream's, so `git worktree remove` needs no `--force`. **No output of `keep` or `reclaim` is filtered**: every line it prints is quoted. B-RECLAIM-SCRATCH is §3.3. `render-state/` is scratch — a copy of the bot's journal, prices and coins among it — never kept, and goes with the tree.

**B-RECLAIM-OWN**, last, after §3.7 and with the report drafted. **Its output is written to no file; the report quotes it verbatim from the session**, every line of it:

```
nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz40-work/stage/research/tz40-advisor-strong.py keep
git -C /root/btc-5m-twap worktree remove /root/tz40-work/wt; echo "exit=$?"
rm -rf /root/tz40-work; echo "exit=$?"
test -e /root/tz40-work; echo "exit=$?"
git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
find /root/btc-forensics -type f | wc -l
df -B1 --output=source,size,avail /var/lib/btc-recorder
```

The branch `tz-40-strong-every-rank` stays on `origin` and as a local ref; only its working tree goes. **Kept:** `/root/adv3-bot-svc/` is the running unit's code, `/var/lib/adv3-bot/` its record — `check-done` and the `check` records among it — and `/etc/adv3-bot/` the Boss's token and the pinned chat; the capture roots, both archives' state and the forensic store are data, never scratch. **A refused `rm -rf` is handed to the Boss** by §3.3's route, one tree per command, and verified by `test -e`.

---

## 10. Pre-send checks

Performed by the Architect on 2026-11-01 against this file as sent, in a reading separate from its writing — the body was written, read start to end and corrected where it read wrongly (the corrections are named in C7), and this section written after — with the repository at `origin/main` `f2a3ed6211b75dfc927a0d20a62458f0af273c35` (map revision `2026-11-01-a` over PR #39's merge `f212cd4`; fetched again before sending: no `TZ-40-` file, no report of that number and no `tz-40` branch), the map at that commit (2,018 lines, 520,651 bytes, SHA-256 `2b113897e3221073c073c95b64e9141a98d1227a9559912e382652772d062763`) and CANON revision `2026-11-01-a`. Line numbers are those of the files §0.1 extracts for Appendix A, and those of `main` for committed code.

| # | check | result |
|---|---|---|
| **C1** | scope against body | **Repository paths the body names:** `CryptoTZ/TZ-40-strong-every-rank.md`, read by §0.1's script and named by `number`; `CryptoTZ/` and `CryptoReports/`, listed by `number`, every `CryptoReports/*.md` read by TZ-35's `reclaim` for hash tokens; `SYSTEM-MAP.md` and the other 58 rows of its table, read by `fingerprint`, among them `BTC-EXECUTOR-INSTRUCTIONS.md` (cited for contract §1, §4.1, §4.2 and §8), `research/tz33-reward-book-capture.py` (cited for line 190), `research/tz35-advisor-deploy.py` (run for `scratch` and `reclaim`) and `research/twap-divergence.py`, `research/recorder/recorder.py` and `research/pfair.py` (hashed for the anchors); `advisor/adv3.py`, `advisor/adv3-bot.py` and `advisor/selftest-adv3.py`, written on the branch, the first two copied to the service; `research/tz40-advisor-strong.py`, written on the branch; `advisor/RULE-ADV-3.txt`, `deploy/systemd/adv3-bot.service` and `CryptoReports/TZ-38-adv3-pit-validation-report.md`, read and hashed by `rule`, never written; `CryptoTZ/TZ-39-advisor-checks.md` and `CryptoReports/TZ-39-advisor-checks-report.md`, cited (§0.4, §1, §6) and read by no command; `CryptoReports/TZ-40-strong-every-rank-report.md`, written to `main`. **Host paths:** `/root/tz40-work/**` written (`render-state/` among it, scratch); `/root/adv3-bot-svc/adv3.py`, `adv3-bot.py` and `commit.txt` written, `adv3.py.new` and `adv3-bot.py.new` transient; `/var/lib/adv3-bot/check-done` written by the `kill` and `rollback` marks through `check-done.tz40`, one rename each (`put_done`, line 814); `/var/lib/adv3-bot/{journal.jsonl,offset,daily-sent,service.log}` read and hashed, `journal.jsonl` copied into `render-state/`; `/etc/adv3-bot/token` read by the bot's own `--probe`, P-START's, and by nothing of this checker's; `/etc/systemd/system/adv3-bot.service` hashed; `/var/lib/btc-recorder` read by `find`, `grep -c` and `df`; the other capture stores by `du`; `/root/btc-forensics` written by `keep` and `reclaim`; `/proc/meminfo`, `/proc/stat` and the processes' `cmdline` and `stat` read by `host` and `unit`; the UUID directories of `/tmp` read, copied from and removed by TZ-35's checker. **Entry points:** this checker's modes `fingerprint`, `host`, `number`, `rule`, `selftest`, `mark` (`deploy`, `kill`, `rollback`, `kill2`), `copy`, `render`, `unit` (`new`, `old`), `first`, `keep` and `stopped`; TZ-35's `scratch` and `reclaim`; `selftest-adv3.py`; `adv3-bot.py --selftest` and `--probe`; `git` (`fetch`, `ls-remote`, `log`, `ls-tree`, `worktree`, `add`, `diff --cached`, `commit`, `push`, `show`, `rev-parse`, `status`), `gh`'s credential helper; `systemctl` (`show`, `list-timers`, `is-enabled`, `kill`, and `disable` at K-40 only); `journalctl` (the unit's lines, §3.7), `cp`, `mv`, `sha256sum`, `cmp`, `timeout`, `nice`, `rm -rf`, `test -e`, `mkdir`, `du`, `df`, `free`, `find`, `grep`, `wc`, `ls`, `cat`, `tail`, `date`, `uptime`, `nproc`. **Outputs:** under `/root/tz40-work/` `logs/`, `stage/`, `wt/`, `render-state/`, `state.json`, `adv3.before`, `bot.before`, `commit.before`; the service copy's three files; `check-done`'s slot; the forensic store's copies; the branch, its pull request and the report. **Intersections with §2, by path and by content class, nine, each named in §2:** the bot's `--probe` reads the token — item 3's exemption; G-RENDER's and P-START's requests — item 3; `systemctl list-timers`, `is-enabled`, `show`, `kill` and `disable` — item 4; `find`, `grep -c`, `df` and `du` on the capture stores and `systemctl show` of their units — item 5, reads; the marks' write of `check-done` — item 6's exemption, a slot and nothing else; `tail` of `service.log`, `journalctl` of the unit, `cat` of `state.json` and `check-done` and `ls` of the record — item 8's content class: they carry log lines, pids, instants, sizes and slots, and `service.log`'s lines name a close, a slot, a kind of request and counts, and a coin only where Binance failed to serve it, never a price, a size or a card (§3.7), and none of them is a live reply or a journal; **`render-state/journal.jsonl`** — item 8's content class, the coins and prices of cards and of allocations: a scratch file of the work tree, never printed, never copied by `keep` (`kept_files`, lines 1055 to 1062, copies `state.json`, the three `.before` files and `logs/` alone) and removed with the tree by §9; **`/var/lib/adv3-bot/journal.jsonl`**, the same class — read by `host`, `mark`, `unit` and `first` and copied by `render`, each printing counts, slots and labels alone (`mode_host` 742 to 756, `mode_mark` 849 to 853, `render_print` 966 to 984, `mode_first` 1046 to 1050); the live replies — item 8: held in memory by the stand-in, never printed. **Classes checked and intersecting nothing:** labels, outcomes and settled documents — this TZ reads none; Binance's candles, marks and volumes pass through the service copy's `Data`, `live_report`, `liquidity` and `forming_candles` in the live render and are stored nowhere but in that scratch journal. |
| **C2** | origin of every expectation | **Quoted from a committed artifact, at `f2a3ed6`:** revision `2026-11-01-a`, the six anchors, `59`, `56`, `2` and `1` — map §0, its table counted independently of the checker by the Architect's own parse (59 rows: 56 `frozen`, 2 `tracked`, 1 `reported`) and each frozen row's lines, bytes and SHA-256 compared with its blob at `f2a3ed6`, `56 of 56` equal, then by `fingerprint` against the clone, `PASS - 68 of 68`; `2,344`, TZ-39's two directories and `238335b9…` — map §3, line 1331, and TZ-38's report; the hashes `c19572dc…`, `ca989b6f…`, `09d2ba9a…`, `ee206e7c…` and `82acd8e4…` — map §0's table and `sha256sum` of the files at `f2a3ed6`; `f4a0ac3f…` — `sha256sum` of TZ-38's report at `f2a3ed6`, 1,641 lines, 103,678 bytes; `PIT`'s figures — TZ-38's report §2.7: E1 `p_t_up` `0.0735` (line 898), `trades` `19,002` (902) and `mean_R` `0.0403` (923), E2 `p_t_up` `0.1100` (963), E4's `mfe` rows (1022 to 1024) and STRONG's `top5_share` `0.9875` (1036), E5's median `0.2195` (1055), `lists` `500` (1061) and `share_mean_R_positive` `0.8600` (1065), `G` `570` (1192), and **E6's `mean_R` `0.7962` and `0.5084` (1102)** — read again by `pit_from_report` and equal; §1's `+0.51` and `+0.80` — E6 line 1102; `+0.07` over `131` and `+1.33` over `35` — E6's places, lines 1133 and 1134; `49 / 30 / 20 %` — E6's `top7` reach, lines 1105 to 1107; `47 / 29 / 19 %` — E4, lines 1022 to 1024; `65,490,944`, `58,953,728` and `49,168,384` — map §6, memory (line 1722); TZ-39's `11,410,116,608` bytes free — its report, line 359; its render's 17 s — line 796; its P-START at 06:51:08 UTC — line 822; its modelled `21,000` bytes a day — its TZ, line 433; `7,300,000,000` — `research/tz33-reward-book-capture.py` line 190, `STREAM_FLOOR = 7300000000`, and map §2.6; `31612203008` and `e3975b5…` — map §6's host identity (line 1698); `2026-11-01 signal`, H7's first slot — map §2.7, TZ-39's paragraph (line 1064); `0.5`, `1`, `5` and `10,000` — `adv3.RISK`, `RISK_MAX`, `RISK_ALL` and `DEPOSIT`, line 24 of `main`'s `adv3.py`; `3` and `1.0` — `TOP_N` and `STRONG_Z`, line 21; `0.001` — `COST`, line 20; the rung `1` — `RELIABILITY`, line 39; `14.0`, `5`, `0.001` and `7` — `STOP_MAX`, `MIN_NOTIONAL`, `LIQ_FRAC` and `LIST_MAX`, lines 33 and 34 of `main`'s bot; `00:10` and `12:10` — `SLOTS`, line 23; `300` s — `RETRY`, line 25; `30` s, `3 4` and `128M` — the unit, lines 15, 16 and 18; `04:10` and `16:10` — CANON PART VII; the Boss's `210,000` USDT, seven requested and two placed — his file of 2026-11-01. **Computed by an implementation independent of the one under test:** `140,037,206` = 2 × `70,018,603`; `70,018,603` = ⌈`58,396,672` × `58,953,728` / `49,168,384`⌉ [modelled], in exact rationals; the render's peaks — `resource.getrusage` of the process that ran `render_run` on the archive's candles, five runs a case under Python 3.12.3 and five under 3.13.18, three cases (§0.4) — and the bot process's `55,922,688` — the same, through two checks and four commands, two runs each; the self-tests' and G-RULE's walls and peaks — a parent's `RUSAGE_CHILDREN`, three runs each; the numstats `439 128`, `35 11`, `21 0` and `1436 0` — `git diff --numstat` against `f2a3ed6` over the files §0.1's script writes into a worktree of the clone; §0.1's table — `wc` and `sha256sum` of the four files, equal to the script's own lines over an empty stage and over that worktree; the golden allocation — exact arithmetic of TZ-37's formula, `⌊60 / 0.082⌋ = 731`, `⌊40 / 0.082⌋ = 487`, `⌊50 / 0.102⌋ = 490`, `⌊1 / 0.13⌋ = 7`, `⌊1 / 0.16⌋ = 6`, `⌈731 / 7⌉ = 105`, `⌈487 / 7⌉ = 70`, `⌈490 / 6⌉ = 82`, shares `3 / 5` and `2 / 5`, the more's correlation `(1 + 0) / 2 = 0.5`, and at 1 % `⌊100 / 0.082⌋ = 1,219` six times, `600` USDT, beyond `500` — each equal to the bot's golden checks; the simulation's `99,083`, `141,145`, `49,490`, `8`, `2.14`, `593` and `1.66` s — its own counts over its journal, re-run under 3.12.3 with the journal equal byte for byte to the first run's; `930` offers — the bot's own `journal_scan` over that journal; §1's exploration — `adv3.simulate_strong` with its places widened, and the closes' STRONG counts by `adv3.states`, on the 42's archive candles; the demo's `17,724` characters in five parts and `24,416` in seven — `len` of the parts the bot's `chunks` made, re-run on the bytes sent and equal; `12,144,254` — the sum of `git ls-tree -r -l` at `f2a3ed6`, `12,271,776` with the branch's files and about `12,700,000` with this file. **Fixed by Appendix A's code, which this TZ measures nothing to set:** `68`, `19`, `2`, `10`, `5`, `22`, `9`, `7`, `10` and `2` (FINGERPRINT, HOST, NUMBER, RULE, COPY, RENDER, UNIT-NEW, FIRST, UNIT-OLD, STOPPED), `57`, `128` and `86` (the self-tests), `5` endpoints and `6` requests, the `7` commands and `7` record kinds of the render, the synthetic market's twelve STRONG, nine extra, three placed and nine more, and G-RULE's `46` and `43` identical, `3` and `14` changed, `0` and `5` added and `0` removed definitions — each the count its function's dictionary or tuple holds, re-run by the Architect where it runs off the host (C5). **Fixed by this TZ and measured by nothing:** the bands, the 45 s wait, the 15 s polls, UNIT-NEW's 90 s and 100 s, G-FIRST's 900 s and the `timeout`'s, the 60 s memory re-read, the session's `100,000,000` bytes, `PACE` `1.1` s — above the one message a second the Bot API asks of a chat — and the `429`'s wait, `min(retry_after, 60) + 1` s, twice at most — the Architect's choices, named so. **The floors and the bands:** `7,400,000,000` = `7,300,000,000` + `100,000,000`; `27,000` = 7 × 3,600 + 30 × 60, `40,800` = 11 × 3,600 + 20 × 60, `42,600` = 11 × 3,600 + 50 × 60, `44,400` = 12 × 3,600 + 20 × 60, `84,000` = 23 × 3,600 + 20 × 60, `85,800` = 23 × 3,600 + 50 × 60; `675` = 5 × `129` + `30`, `129` = 4 × 30 + 1 + 3 + 5. **No expectation depends on a quantity this TZ measures but as an inequality or an equation that holds for every admissible value of it:** UNIT-NEW reads `NRestarts` as the `kill` mark's plus one and the capture units' as the mark's, whatever the mark read; the memory and disk gates are inequalities on a read; G-RENDER's limits are inequalities, and its equations are between the replies, records and alerts and the orders, STRONG, plans and walks the checker recomputes from the same reports, candles, volumes and offers; G-FIRST reads `check-done` against the mark's instant — `signal` before 12:10 UTC, `fact` after — which holds for every mark either band admits (§4.3); H7 reads slots against their instants and `check-done` against the last; the numbers of STRONG at every rank, extra cards, alerts and trades placed and more are printed, never asserted. |
| **C3** | shape of every diff | Four paths, read from `git diff -U0 f2a3ed6` over the extraction. **`advisor/adv3.py` replaces 11 committed lines:** 44; 48; 571; 600–601; 603; 630; 713; 716; 738–739 — the measurements' comment, `PIT`'s STRONG row, `message`, `assessment` and `card_lines` — `--numstat` `35 11`. **`advisor/selftest-adv3.py` replaces none:** `21 0`. **`advisor/adv3-bot.py` replaces 128:** 34; 39; 41–42; 99; 103–104; 106–115; 245–246; 248–250; 362–364; 370–372; 387–388; 392; 411–413; 483; 532; 538; 624–625; 630–631; 639; 709; 714; 721–723; 727–728; 733–736; 738; 799; 804; 819; 826–827; 836–840; 846–848; 857; 935; 937–941; 1060–1062; 1080; 1082; 1239–1242; 1245–1248; 1334–1337; 1341–1343; 1345–1351; 1367; 1369; 1395–1396; 1403; 1405–1407; 1422–1423; 1433; 1491–1496; 1499; 1501–1502; 1510; 1524–1529 — `LIST_MAX`'s comment (its value unchanged, its syntax tree equal), `HELP`, `Telegram`, `top_n`, `item_lines`, `plan_parts`, `CARD_KEYS`, `offers`, `candidates`, `alerts_of`, `event_lines`, `candidate_lines`, `compose`, `check_record`, `check`, `handle` and lines of `selftest` — `439 128`. **`research/tz40-advisor-strong.py` is new:** `git cat-file -e f2a3ed6:research/tz40-advisor-strong.py` exits `128`, as do the report's path and this TZ's own; `1436 0`. No sentence of this TZ calls a change additive or speaks of insertions only. |
| **C4** | cost of every check | §6, at the population's upper bound. **Processor, single session, term by term:** the three self-tests `3 × 30 = 90` s against `0.24`, `1.16` and `0.60` s measured at most; G-RENDER and P-START `30` s against `6.1` s at most measured for G-RENDER's seven reports, replies and two checks, on the archive's heaviest STRONG close with the ninety-day journal; at most `90` checker runs at `5` s, `450` s — HOST 1, FINGERPRINT 1, NUMBER 2, RULE 1, the marks up to 4, COPY 1, UNIT-NEW up to 5, G-FIRST up to 61, UNIT-OLD up to 5, KEEP 1 and STOPPED up to 2, `84` at most, each under `1` s measured but RULE and FINGERPRINT, `0.68` s together at most; and the `reclaim`, `git` and `systemctl` commands `60` s: **`90 + 30 + 450 + 60 = 630` s, under `3,600`; nothing is sampled.** **The fail-fast bounds, each with its derivation:** `adv3.get`'s four tries — four `30` s timeouts and the `1`, `3` and `5` s between them, `129` s, `adv3.py` lines 69 to 87, unchanged from `main`'s 62 to 80 — make a render with Binance silent worst at `14 × 129 = 1,806` s for `Data`'s 84 requests over six threads (`Data.fresh`, line 213), `14 × 129 = 1,806` s for the marks and funding intervals of seven reports one after another (`live_report`, 245), `28 × 129 = 3,612` s for the volumes of at most 42 STRONG coins at two allocations and two checks, six at a time (`volumes`, 337), and `42 × 129 = 5,418` s for the fact check's forming candles one after another (`forming_candles`, 712), `12,642` s in all, so G-RENDER runs under `timeout 900`; its stand-in's pauses at most `9 × 9 × 1.1 = 89.1` s, nine messages of ten parts; P-START's six requests one after another, `5 × 129 + 30 = 675` s of wall (`Telegram.call`, line 104, has one try of `30` s), `probe`, lines 1079 to 1104; UNIT-NEW's `NOT YET` at most 100 s after the mark, every 15 s, at most 4 runs in a paste; G-FIRST's at most `900` s after the mark, every 15 s, at most 60. **Wall clock:** about 45 minutes; `88` with every bound reached — `10 + 5 + 2 + 5 + 16 + 12 + 16 + 2 + 17 + 3` — up to 30 more where a paste waits for the Boss, and a wait for B-DEPLOY's band of at most 8 h 10 min; at the bounds B-DEPLOY at 11:20:00 UTC reaches B-KILL by 11:48, inside its band. Disk at the same bound: §0.4's `100,000,000`, the logs under `2,000,000` bytes. **After the session:** at most 128 requests at 00:10 and 86 at 12:10 a day, §6, each under the same `get`; a message of eight parts at least `7 × 1.1 = 7.7` s of pauses and, with every part refused twice at the longest wait, at most `7.7 + 8 × 2 × 61 = 983.7` s, the unit answering no command meanwhile. |
| **C5** | every count | `68` = 1 revision + 6 anchors + 4 re-derived + 56 frozen rows + 1 table shape, `parse_map` and `mode_fingerprint` (lines 157 and 687), the table counted again by the Architect's parse — `59` rows, `56` frozen, `2` tracked, `1` reported. `19`, `mode_host` lines 712 to 757: H1 one, H2 two, H3 one, H4 three, H5 six, H6 one, H7 three (`clock_checks`, 590), the memory gate and the disk gate; `19 of 19` on stand-ins for systemd, `/proc`, `df` and the host's files, and `memory_gate` deciding a low first read by the second. `2`, `number_reading` (679): `PASS` on stand-ins with the one file, `FAIL` with a second `TZ-40-` file and with a report, and `FAIL - 1 of 2` on the clone at `f2a3ed6`, which holds no `TZ-40-` file. `4` files and `4` hashes, §0.1. `10` = `mode_rule` (783 to 802): two file checks, three of `tree_checks` (184) for `adv3.py`, `PIT` against `pit_from_report` (214), three of `tree_checks` for the bot and the three hashes — `10 of 10` on the clone and on the extracted worktree. `57` = 53 + 4, the four `check` calls §5 names; `128` = 96 + 10 + 22, by name against `main`'s `selftest` — the ten names that no longer stand rewritten, the twenty-two new each one check; `86` = 56 single assertions of `mode_selftest` (1154) and its four loops of negative controls, 5 of `tree_checks`, 6 of `clock_checks`, 7 of `unit_checks` and 12 of `first_checks` — each listed by its run, `57 of 57`, `128 of 128` and `86 of 86` on the files §0.1 extracts. `5`, `mode_copy` (855), `5 of 5` on a stand-in origin, worktree and service copy. `22` = `render_checks` (385 to 507), `22 of 22` on the stage's bot with the synthetic market and on the archive's candles to the close of 2026-10-30 with both journals; on the archive's heaviest close, 2026-09-27, `21 of 22`, the one short (5), «оценка»'s forward record, which a close before 2026-10-28 does not carry (`assessment`, lines 660 and 666); and each of twenty-four faults reading FAIL. `5` endpoints and `6` requests, `probe` (1079 to 1104). `9`, `unit_checks` (510), and `10` with `mode_unit`'s extra check (1028): `9 of 9` and `10 of 10` on stand-ins for a deploy, a kill, a restart, a rollback — `check-done` restored — and a second kill, and eight faults reading FAIL. `7`, `first_checks` (532), `7 of 7` on stand-ins, and twelve faults reading FAIL. `2`, `mode_stopped` (1094). `7` = `RENDER_CASES`, `7` = `RENDER_KINDS` (lines 59 and 60). G-RULE's lists — for `adv3.py` `3` changed, `0` added, `0` removed and `46` identical of `main`'s `49` definitions, `PIT` changed and `BEYOND` and `BEYOND_TAG` added among its assignments; for the bot `14` changed, `5` added, `0` removed and `43` identical of `57`, `CARD_KEYS` and `HELP` changed and `PACE` added — the Architect's own AST script, equal to `ADV3_DEFS`, `ADV3_ASG`, `BOT_DEFS` and `BOT_ASG` and to §4.1's names. V1 to V17 are §7's seventeen rows. |
| **C6** | every population | NUMBER: the paths under `CryptoTZ/` and `CryptoReports/` of `origin/main` at each of its two reads. FINGERPRINT: the map's table of 59 rows against the files of the primary checkout. HOST: the host at the instant of the read — its units, files, record, memory and disk; H7 the journal's `check` records from TZ-39's first, `2026-11-01 signal`; the memory figure the first read and, if it fell below the floor, the second. RULE: `adv3.py`, `adv3-bot.py`, `RULE-ADV-3.txt`, the unit file and TZ-38's report of `origin/main` against the branch's files. The self-tests: synthetic candles, markets and stand-ins, no network. COPY: `/root/adv3-bot-svc` and the worktree. RENDER: the service copy's bot answering seven texts and running two checks on the latest close at the run's instant — the 42 coins' candles, at most 1,500 each, marks, funding intervals, the volumes of every coin STRONG at any rank, at most 42, at each allocation and check, and the forming candles of the offered coins at the fact check — over a copy of the bot's journal; for each allocation the `plan_strong` recomputed from the report and volumes that reply was made from; the order, STRONG and stops the checker computes from the same rows; for each check the checker's walk of every offer the journal held before it. P-START: one request to each of five endpoints, the klines endpoint twice. UNIT-NEW and UNIT-OLD: the unit, the three capture units and `service.log`'s lines stamped at or after the mark less 1 s. G-FIRST: the journal's records stamped at or after the `kill` mark less 1 s, `check-done` and `service.log`'s lines since the mark. KEEP: the work tree's files §9 names. RECLAIM: the UUID directories `scratch` names earlier. §1's history figures: TZ-38's E6 on *P*, the 609 contracts of *L*, in sample; the exploration on the 42's archive candles, 2023-01-01 to 2026-10-27 for the trades by rank, 2025-01-01 and 2024-11-01 to the close of 2026-10-30 for the closes' STRONG counts. §6's journal growth: the simulation's 180 checks over the closes 2026-08-01 to 2026-10-29. Each memory figure: one mode's process; `MemAvailable` and free space: the host at each read. No statistic of this TZ is a calibration claim and none is read against a label. |
| **C7** | every signature and every behaviour | **Committed code this TZ relies on, read at `f2a3ed6`.** `adv3.py` — `def get(url, tries=4):` line 62, four tries of 30 s with 1, 3 and 5 s between them (62 to 80), the `129` s of §6; `def fapi(path, **params):` 153; `def fapi_candles(sym, now_ms):` 157; `def fapi_funding(sym, first):` 166; `def fapi_intervals():` 181; `def fapi_marks():` 186; `def ranking(day_states):` 305, `top = sorted(active, key=lambda cs: -abs(cs[1][1]))[:TOP_N]` (308) and `strong = [coin for coin, s in top if s[2] == 4 * s[0] and abs(s[1]) >= STRONG_Z]` (309) — the condition `strong_all` keeps without its `[:TOP_N]`, so that its members among the TOP-3 are the report's STRONG; `def simulate_strong(cs, st, funds, first_entry, last_day):` 313; `def trust(rep):` 380; `def report(cs, funds, marks, deposit, risk, now_ms, missing=(), intervals=None):` 447, `top, strong = ranking(today)` (454); `def card(coin, row, is_strong, deposit, risk):` 493; the constants lines 20, 21, 24 and 39. `adv3-bot.py` of `main` — `SLOTS` (23), `POLL, RETRY, LIMIT = 50, 300, 4000` (25), `STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, CROWD, Z_CAP, LIQ_DAYS = 14.0, 5.0, 0.001, 0.5, 3.0, 7` (33), `LIST_MAX = 7` (34); `def put(path, text):` 64; `class Telegram:` 84 with `def call(self, method, http_timeout=30, **params):` 90 and `def send(self, text, quiet=False):` 102, a refused part re-raised unless Telegram could not parse it (111, 112), so that the check fails and `serve` tries it again after `RETRY` (891) — §1's "every part again"; `def route(text):` 147, `n = min(max(int(top.group(1)), 1), LIST_MAX)` (166); `class Data:` 172, `def fresh(self):` 180, its 84 requests over `ThreadPoolExecutor(6)` (196); `def ranked(rep):` 229, `adv3.ranking` applied again to the coins it has not placed; `def liquidity(coin, now_ms):` 280; `def plan(rep, cs, budget, n, risk, liq):` 291 — its candidates `[c for c in rep['top'] if c in rep['strong']]` (301), its rejections in that order (304 to 311), `f'сверх запрошенных {n}'` (311), the reason `plan_strong` reads to find the trades beyond n, and `crowd`, each trade's mean same-way correlation with the others (323), which `plan_strong` reads for a trade of the more from `plan` over the placed and it; `def due(now, done):` 450 and `def done_after(slot, now):` 461 — from the day before's `fact` the day's signal check is due at any hour, and a signal check ending at or after 12:10 marks the day's fact done; `def journal_scan():` 501, `prev` the last `check` record of either kind (507, 508) — so the quiet condition reads the check before, and TZ-39's records hold no `strong_all`; `def alerted(records):` 554; `def follow(offs, cs, funds, last, forming=None, done=frozenset()):` 568; `def forming_candles(coins, day):` 609, one coin after another; `def serve():` 867 — `done = slot_parse(read(done_path)) …` (881) once at its start, `log('serving the pinned chat: pid', …, 'check-done', …)` (883), `slot = due(now, done)` (886), `done = done_after(…)` (894) and `put(done_path, …)` (896), so the running process never reads `check-done` again; `def probe():` 962; `def main():` 1538 — `plan`, `ranked`, `route`, `Data`, `liquidity`, `follow`, `journal_scan`, `due`, `done_after`, `serve` and `main` identical to Appendix A's by G-RULE. TZ-35's checker `research/tz35-advisor-deploy.py` — `UUID` (54) and `LIVE_S = 60` (56); `def claude_starts():` 157, `argv[0] == 'claude' or argv[0].endswith('/claude.exe')` (167); `def live_or_earlier(birth, starts):` 274, `s - 1 <= birth <= s + LIVE_S` (276); `def reclaimable(tree):` 279; `def mode_scratch(own):` 419; `def mode_reclaim(trees):` 434, printing `RECLAIM PASS` at 486; `def main(argv):` 774. The unit — `WorkingDirectory` line 12, `ExecStart` 13, `Restart=always` 14, `RestartSec=30` 15, `RestartPreventExitStatus=3 4` 16, `MemoryMax=128M` 18, `ProtectSystem=strict` 21 and `ReadWritePaths=/var/lib/adv3-bot` 22, under which the bot writes `check-done` and the checker `check-done.tz40`. **Every behaviour this TZ attributes to Appendix A** is the body of one function: of the bot `TooMany` 90, `Telegram.call` 104 — a `429` raising `TooMany` with its `retry_after`, `5` where none is named (115, 116) — `send` 120 — `time.sleep(PACE)` before every part but the first (126, 127), three tries, `min(e.retry_after, 60) + 1` between them (128 to 135) — and `send_part` 138, `route` 180, `live_report` 245, `ranked` 262, `strong_all` 277, `top_n` 285, `make` 301, `volumes` 337, `plan_strong` 409, `item_lines` 443, `plan_parts` 474, the schedule 524 to 580, `journal_scan` 604, `base_record` 620, `offers` 631, `alerted` 657, `follow` 671, `forming_candles` 712, `candidates` 726, `alerts_of` 731, `event_lines` 789, `candidate_lines` 826, `quiet_line` 895, `compose` 906, `alloc_fields` 936, `check_record` 946, `check` 964, `serve` 987, `handle` 1044 and `probe` 1079; of `adv3.py` `changes` 558, `message` 574, `assessment` 645 and `card_lines` 731; and the checker's readings and modes at the lines C5 names — each sentence of §1 and §4.2 to §4.4 read against them. **Sentences rewritten in this reading:** §1 said the first 00:10 check of the new code sends the full message, where the first signal check is the replay at the restart and the next 00:10 reads that replay's record — rewritten; §1's exploration named no funding — it is the rule's default; §1 cited §6 for the heavy close's characters and parts, which §6 does not hold — named the Architect's measurement, with its inputs; §1 and §6 gave `1.37` s of processor a check, measured under 3.13.18 and not named so — re-run under 3.12.3, the journal equal byte for byte, `1.66` s; **§0.4's peaks were measured before the bot's last edit:** re-measured on the bytes sent, five runs a case under both interpreters, the heaviest close and the ninety-day journal among the cases — the largest 3.13.18 figure rose from `56,688,640` to `58,396,672` and the floor from `135,941,286` to `140,037,206`, the checker's `MEM_FLOOR` with it; "937 offers" read `930` by the bot's own `journal_scan`; the bot process's `48,721,920` re-measured, `55,922,688`; §0.4's tracked files were `11,700,000` bytes where `git ls-tree` sums `12,144,254`; §4 and §4.4 gave a failed signal of B-KILL no outcome — it is B-ROLLBACK with the unit not signalled, and the signal counts as delivered wherever the unit's pid or restart count moved from the mark's; §5 said the `kill` and `rollback` marks write `check-done` and nothing else, where every mark writes `state.json`; §5's "three of `compose`'s on the quiet condition, …" read as three on one condition — punctuated; §6 said G-RULE runs `git show` of six paths, where it runs five; §6's wall clock summed its parts to 42 minutes and called them 50, and left the report's time out of its bound — about 45, and `88` at the bounds; the self-tests' and G-RULE's times re-measured on the bytes sent. Every count and hash of this section is that of the bytes sent. |
| **C8** | every cross-reference | Resolved by reading the text referenced. **Map `2026-11-01-a` at `f2a3ed6`:** §0's anchors and its table of 59 rows, 56 / 2 / 1; §1's record of refs (a difference from it is recorded, not blocking, §0.5); §2.5 and §2.6 for the archives' calendar runs at `03:00:20` and `01:30:20` UTC, and §2.6 for `STREAM_FLOOR` `7,300,000,000`; §2.7's record under `/var/lib/adv3-bot/`, the token and chat under `/etc/adv3-bot/`, K-35, and TZ-39's paragraph (line 1064) — the two checks, `check-done`, the trades the cards offered and the first check `2026-11-01 signal`; §3's `2,344` files in the forensic store, the two worktrees and the two directories TZ-39's session left (line 1331) and the live `238335b9…`; §6's rows host identity (line 1698), language — `/root/tz04a-env` on Python 3.12 (1699) — git remote — the push through `gh`'s credential helper (1702) — egress — `fapi.binance.com` answering `451` to the Architect's sessions (1703) — disk (1705), process supervision — system units and their restart policy (1721) — memory — `65,490,944`, TZ-37's `58,953,728` against `49,168,384` and TZ-39's host reads (1722) — both sandbox limits (1725, 1727) and the harness (1728); §7 items 118 (no file of the work tree printed but by a command the TZ names), 124 (a block handed to the Boss: once its band is open, one line, appended under a `date -u` line), 125 and 129 (a reload re-arming an archive's run), 131 (the floor rule), 132 (no step of the Boss's before `EXECUTE`), 136 (`NRestarts` not a lifetime count — UNIT-NEW reads it against the mark's), 137 (a memory floor read twice), 138 (ONE paste, a refused block handed over unchanged), 139 and 141 (the header names the sections this row cites — copied there), 140 (a handed-over block holds back only the steps that read what it changes), 142 (CANON `2026-10-31-c`'s ladder, which `2026-11-01-a` carries), 143 (bands opening at 07:30 UTC, clear of the package manager's run), 144 (no mode run again after a paste) and 145 (a mode timed for its host peak carries its own wrapper inside the paste). **CANON `2026-11-01-a`:** PART VII — the frozen rule and its STRONG of the TOP-3, the STRONG strategy's three places, the forward, PIT and market records re-derived from Binance's archive and never from the bot's journal, the evidence ladder at rung 1, the sizes (0.5 % a trade, 1 % at most, 5 % in all), the 14 % stop, «сигнал топ <N>» to 7 with STRONG within the TOP-3 — the decision this TZ changes for the bot's display and not for the rule — the random lists' `+0.22` R, ADV-4 for any change of parameter and «Уверенность: N/5»; PART VI's fourth rule (an exploration gates nothing); hard rules 2 (NUMBER), 12 and 13 (this section), 14 (P-START, every header, the unit, its restart policy and stop, the bands in the blocks' text, ONE paste) and 15 (§9). **Quotations, compared character for character:** the Boss's three sentences of §1 and his title «Change STRONG Candidate Selection and Reporting Logic» with his file of 2026-11-01 — each a substring of it, his «Additional STRONG Candidates» among his words; RULE-ADV-3's "a TOP-3 coin whose four signs all agree with its side and whose \|z\| >= 1" with `advisor/RULE-ADV-3.txt` lines 11 and 12, its line break and indentation read as one space. **Contract:** §1 steps 1 to 4 (§0.0, `fingerprint`), §4.1 (the order of the branch and the report), §4.2 (V13) and §8 (the report's order). **Other artifacts:** `CryptoTZ/TZ-39-advisor-checks.md`, whose §0.1 script, bands, marks, B-DEPLOY, B-KILL, gates and §0.4 floor rule this TZ adapts, line 433, and its report (lines 359, 796 and 822); `CryptoTZ/TZ-35-advisor-bot.md` §4.1, whose fixed headers §4.3 repeats; TZ-38's report §2.7 (E1, E2, E4, E5 and E6); TZ-35's checker's `scratch` and `reclaim`. **This TZ:** §0.1 to §0.5, §1, §2's items, §3.1 to §3.7, §4.1 to §4.5, §5, §6 and §9, each supporting the sentence that cites it. **None unresolved.** |

**Seven checks could not be performed from this session**, and each is converted into a mechanical condition the Executor evaluates and BLOCKS on, or rolls back on (CANON hard rule 13): the host's own state — free space, memory, units, interpreter, the service copy's and the unit file's hashes, the record and the clock's firing under TZ-39's code — `I host`, §0.3; the live reach of `fapi.binance.com` and `api.telegram.org` under the service's headers — `fapi.binance.com` answers `451` to this session's container (map §6, egress) — P-START and G-RENDER, before anything is signalled; a live day with STRONG beyond the TOP-3, which depends on the market — at the close of 2026-10-30 the 42 held three STRONG at every rank, all within the TOP-3 — G-RENDER computes its own order and STRONG and reads every extra card, tag and allocation against them whenever the day holds one, and a disagreement is B-ROLLBACK; when it holds none it reads 22 of 22 with no extra card, and the new views rest on the self-tests' synthetic market of twelve STRONG and the Architect's render on the archive's heaviest close (35 STRONG, 32 extra, every check of the new views passing, C5); systemd's restart of the unit after a `SIGTERM`, the new process's replay of the day's signal check and its message to the Boss's chat, now paced — UNIT-NEW and G-FIRST; Telegram's `429` on the live API, which nothing here provokes — the self-tests prove the wait and the retry on stand-ins, and §4.5 says it is not established; the harness's permission classifier — each refused block handed over unchanged with its paste (§3.6); and the 00:10 and 12:10 checks under this code on their own clock — the next TZ's host gate reads them (H7).

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
# Since TZ-40 a message may carry, after its TOP-N, the cards the bot marks extra - every coin STRONG at any rank beyond the
# list (adv3-bot.py's strong_all) - and a STRONG card beyond the TOP-3 says so: the frozen rule's STRONG is the TOP-3's.
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
# lists of 42 (E5) - never what a STRONG trade made on the 42 (CANON PART VII). Since TZ-40 the assessment quotes E6 too:
# the STRONG strategy on the same 609 contracts with three places and with seven, mean R a trade (mean_R_P3, mean_R_P7).
PIT = {'base': {'mfe': {1: 0.2318, 2: 0.1257, 3: 0.0759}, 'mean_R_G': 0.0403, 'trades_G': 19002, 'p_G': 0.0735,
                 'contracts_G': 570},
       'strong': {'mfe': {1: 0.4717, 2: 0.2906, 3: 0.1887}, 'p_G': 0.1100, 'mean_R_lists': 0.2195, 'lists': 500,
                  'lists_positive': 0.8600, 'top5_share': 0.9875, 'mean_R_P3': 0.7962, 'mean_R_P7': 0.5084}}
# CANON PART VII's evidence ladder: for each rung, the card's line and the ratings' sentence.
LADDER = {0: ('направление не публикуется', 'история или форвард дисквалифицировали правило: направление не публикуется'),
          1: ('правило не доказано', 'история на ваших 42 монетах — в выборке, на монетах, выбранных в 2026, — не '
                                     'дисквалифицировала правило; это не подтверждение'),
          2: ('подтверждено вне вашего списка', 'PIT-запись подтвердила: правило зарабатывает на контрактах, которые вы не '
                                                'выбирали, на данных, которых никто не читал'),
          3: ('подтверждено и не опровергнуто', 'PIT-запись подтвердила правило, и год на ваших монетах этого не опроверг'),
          4: ('доказано на ваших монетах', 'форвард доказал правило на монетах, которыми вы торгуете'),
          5: ('доказано и держится', 'форвард доказал правило, и следующий год это подтвердил')}
# TZ-40: the label of a STRONG card beyond the TOP-3, and the one line a message carries wherever it shows such a card.
BEYOND_TAG = ' · вне ТОП-3'
BEYOND = ('<i>★ STRONG вне ТОП-3 — четыре знака совпадают и |z| ≥ 1, но это не измеряемая стратегия: форвард STRONG ведётся '
          'только по ТОП-3</i>')


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
    trades its cards offered). The methodology, the forward record and the six ratings are the assessment's, «оценка» (TZ-39).
    The cards marked extra follow the TOP-N under their own heading, and one line says what a STRONG card beyond the TOP-3 is
    wherever the message shows one (TZ-40)."""
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
    main = [cd for cd in rep['cards'] if not cd.get('extra')]
    extra = [cd for cd in rep['cards'] if cd.get('extra')]
    conf = (rep.get('trust') or {}).get('cards') or {}
    if main:
        lines.append(f"<b>ТОП-{rep.get('n', TOP_N)} по силе тренда</b>")
        for cd in main:
            lines += [''] + card_lines(cd, facts, conf.get(cd['coin']))
    else:
        lines.append('<b>Открытых сигналов нет</b> — все монеты вне рынка.')
    if extra:
        lines += ['', f"<b>Дополнительные STRONG-кандидаты</b> — за ТОП-{rep.get('n', TOP_N)}: те же условия STRONG и тот же расчёт"]
        for cd in extra:
            lines += [''] + card_lines(cd, facts, conf.get(cd['coin']))
    if any(cd.get('strong') and (cd.get('rank') or 0) > TOP_N for cd in rep['cards']):
        lines += ['', BEYOND]
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
    its parts and what the history says in figures without survivorship - the methodology the pushed messages no longer carry -
    and, since TZ-40, what a STRONG card beyond the TOP-3 is and what TZ-38's E6 measured of STRONG with seven places."""
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
              f"★ STRONG вне ТОП-3 — те же условия и тот же расчёт, но не измеряемая стратегия: форвард STRONG ведётся по ТОП-3. "
              f"На всех контрактах Binance STRONG на семи местах дал {signed(s['mean_R_P7'])} R на сделку против "
              f"{signed(s['mean_R_P3'])} на трёх; дальше седьмого места не измерено.",
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
    confidence: the rung of the evidence ladder, or 0 where the card offers no entry or no current price came. A STRONG card
    whose rank is beyond the TOP-3 carries BEYOND_TAG, and a card marked extra gives its rank beyond the list (TZ-40)."""
    side = 'LONG' if cd['side'] > 0 else 'SHORT'
    dot = '🟢' if cd['side'] > 0 else '🔴'
    tag = (' · ★ STRONG' + (BEYOND_TAG if (cd.get('rank') or 0) > TOP_N else '')) if cd['strong'] else ''
    out = [f"{dot} <b>{cd['coin']} · {side}</b>" + tag]
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
        where = (f"ранг {cd['rank']} — за ТОП-{cd.get('of', TOP_N)}" if cd.get('extra')
                 else f"ранг {cd['rank']} из {cd.get('of', TOP_N)}")
        out.append(f"Основание: сумма знаков {signed(cd['sum'], 0)} из ±4 · z {signed(cd['z'])} · {where}")
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
# TZ-40: STRONG at every rank - four signs agreeing with the side and |z| at least the rule's STRONG_Z, whatever the rank - in
# every view: the list's TOP-N, then every such coin beyond it; the allocation's first N that pass the limits, then every other
# that passes them, each sized alone; the checks' candidates. The frozen rule's STRONG, its strategy and records stay the TOP-3's.
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
LIST_MAX = 7   # the longest list «сигнал топ N» shows and the most trades an allocation places; STRONG beyond it is listed
PACE = 1.1     # seconds between the parts of one message: Telegram asks for at most one message a second in a chat (TZ-40)
SIDE, DOT = {1: 'LONG', -1: 'SHORT'}, {1: '🟢', -1: '🔴'}
FOOTER = '<i>Не инвестиционный совет · «оценка» — на чём держится уверенность</i>'
HELP = ('<b>ADV-3 · сигналы Binance Futures</b>\n'
        '«сигнал» — ТОП-3 правила сейчас: вход, стоп, цели и размер при депозите 10 000 USDT и риске 0,5% на сделку.\n'
        '«сигнал топ 7» — то же для семи сильнейших, от 1 до 7. ★ STRONG — на любом месте рейтинга (четыре знака совпадают и '
        '|z| ≥ 1); STRONG за пределами списка — ниже, в «Дополнительные STRONG-кандидаты», с той же карточкой.\n'
        '«сигнал 10000 топ 3» — распределить 10 000 USDT между сделками STRONG со стопом не дальше 14% входа; подошло меньше — '
        'покажу меньше, ни одной — скажу, больше — остальные ниже, каждая посчитана как одна сделка. Риск — 0,5% бюджета на '
        'сделку, не больше 1%: «сигнал 10000 топ 3 1». Чего нельзя разместить без превышения риска, остаётся свободным. '
        '★ STRONG вне ТОП-3 — не измеряемая стратегия: форвард STRONG ведётся по ТОП-3.\n'
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

    def send(self, text, quiet=False):
        """The text as HTML, in parts of at most LIMIT characters, PACE seconds apart; a part Telegram cannot parse goes as plain
        text, and a part refused as too many requests waits the retry_after named, at most 60 s, and goes again, twice at most
        (TZ-40). quiet sends every part without a notification (the Bot API's disable_notification)."""
        ids, extra = [], ({'disable_notification': True} if quiet else {})
        for k, part in enumerate(chunks(text)):
            if k:
                time.sleep(PACE)
            for attempt in range(3):
                try:
                    ids.append(self.send_part(part, extra))
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


def strong_all(rep):
    """STRONG at every rank (TZ-40): every coin of the rule's order whose four signs agree with its side and whose |z| is at least
    the rule's STRONG_Z - the frozen rule's condition without its TOP-3, so that its members among the TOP-3 are the report's
    STRONG. In the rule's order."""
    rows = rep['rows']
    return [coin for coin in ranked(rep) if rows[coin].get('sum') == 4 * rows[coin]['signal'] and abs(rows[coin]['z']) >= adv3.STRONG_Z]


def top_n(rep, n):
    """The report with the cards of the rule's first n coins - the TOP-3's own cards, then adv3.card for the rest at the report's
    deposit and risk, ★ STRONG wherever strong_all names the coin - each its rank k of n; then, marked extra, the card of every
    coin strong_all names beyond the first n, its rank in the rule's order (TZ-40); the ratings recomputed over them all."""
    have = {cd['coin']: cd for cd in rep['cards']}
    order, strong = ranked(rep), set(strong_all(rep))

    def card_of(coin):
        return have.get(coin) or adv3.card(coin, rep['rows'][coin], coin in strong, rep['deposit'], rep['risk_pct'])
    cards = [dict(card_of(coin), rank=k, of=n, extra=False) for k, coin in enumerate(order[:n], 1)]
    cards += [dict(card_of(coin), rank=k, of=n, extra=True) for k, coin in enumerate(order, 1) if k > n and coin in strong]
    out = dict(rep, cards=cards, n=n)
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


def volumes(coins, now_ms):
    """{coin: liquidity(coin, now_ms)} for coins, six requests at a time (TZ-40: an allocation reads every STRONG coin's)."""
    with ThreadPoolExecutor(6) as pool:
        return dict(zip(coins, pool.map(lambda coin: liquidity(coin, now_ms), coins)))


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


def plan_strong(rep, cs, budget, n, risk, liq):
    """TZ-40's allocation: TZ-37's plan, unchanged, over every coin STRONG at any rank (strong_all) in the rule's order - the first n
    that pass its limits placed, every other that passes them 'more', each sized by the same plan alone, as a trade of its own at
    the average risk, and its mean same-way correlation with the placed trades read from the same plan over them and it; the
    rejected with their reasons; 'plain' the rule's first n coins that are not STRONG. Each card carries its rank in the rule's
    order, each 'more' item its number after the placed ones. The placed trades and the totals are plan's, the 'more' outside them."""
    order, quals = ranked(rep), strong_all(rep)
    rank = {coin: k for k, coin in enumerate(order, 1)}
    over = f'сверх запрошенных {n}'
    p = plan(dict(rep, top=quals, strong=quals), cs, budget, n, risk, liq)
    placed = [it['card']['coin'] for it in p['items']]
    more, rejected = [], [x for x in p['rejected'] if x[2] != over]
    for coin in [c for c, _s, why in p['rejected'] if why == over]:
        one = plan(dict(rep, top=[coin], strong=[coin]), cs, budget, 1, risk, liq)
        rejected += one['rejected']
        for it in one['items']:
            crowd = None
            if placed:
                both = plan(dict(rep, top=placed + [coin], strong=placed + [coin]), cs, budget, len(placed) + 1, risk, liq)
                crowd = next((x['crowd'] for x in both['items'] if x['card']['coin'] == coin), None)
            more.append(dict(it, crowd=crowd))
    for it in p['items'] + more:
        it['card']['rank'] = rank[it['card']['coin']]
    for number, it in enumerate(more, len(p['items']) + 1):
        it['rank'] = number
    return dict(p, more=more, rejected=rejected, plain=[c for c in order[:n] if c not in quals], strong_all=quals,
                more_loss=sum(it['loss'] for it in more), more_loss_exact=sum(it['loss_exact'] for it in more))


def strong_shares():
    """The reach shares a STRONG trade's targets carry: TZ-38's STRONG shares where Gate S stands, else the rule's (adv3.PIT)."""
    return adv3.PIT['strong' if adv3.FACTS['strong'].get('gate_S') == 'NOT DISQUALIFIED' else 'base']['mfe']


def item_lines(it, k, number=None, more=False):
    """One trade of an allocation: direction and quality, entry, stop, targets with their shares, capital, leverage, margin, loss
    at the stop, invalidation, and its confidence with the note that the sizes are the Architect's formula, unproven. A trade
    beyond the TOP-3 carries adv3.BEYOND_TAG; one of 'more' (TZ-40) is outside the allocation, a trade of its own, with its mean
    same-way correlation with the placed trades where there are any."""
    usdt, pct, price = adv3.usdt, adv3.pct, adv3.price
    cd, mfe = it['card'], strong_shares()
    lo, hi = cd['zone']
    ref = cd['entry']
    conf = adv3.RELIABILITY if cd['mode'] != 'none' else 0
    if more:
        share = 'вне распределения — одна сделка' + (f" · корреляция с основными {adv3.signed(it['crowd'])}"
                                                     if it.get('crowd') is not None else '')
    else:
        share = f"доля {pct(100 * it['share'], 0)}%" + (f" · корреляция с остальными {adv3.signed(it['crowd'])}" if k > 1 else '')
    lines = [f"{f'{number}) ' if number else ''}{DOT[cd['side']]} <b>{cd['coin']} · {SIDE[cd['side']]}</b> · ★ STRONG"
             + (adv3.BEYOND_TAG if (cd.get('rank') or 0) > adv3.TOP_N else ''),
             f"Качество: z {adv3.signed(cd['z'])} · сумма знаков {adv3.signed(cd['sum'], 0)} из ±4 · {share}",
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
    """The allocation view as one message: the budget and the limits in money, the result, each placed trade, then - TZ-40 - every
    other STRONG trade that passes the limits under «Дополнительные STRONG-кандидаты», each sized alone, with the loss of all of
    them and the placed ones together against the 5 % limit; the rejected and the weaker named, and the note that the sizes are
    unproven. The six ratings are the assessment's, «оценка» (TZ-39)."""
    last = dt.date.fromisoformat(rep['close_of'])
    usdt, pct, num = adv3.usdt, adv3.pct, adv3.num
    lines = ['💼 <b>ADV-3 · распределение капитала</b>', f"Закрытие дня {adv3.ddmm(rep['close_of'])} (UTC) · действует до 04:00 {last + 2 * adv3.DAY:%d.%m} по Батуми",
             f"Бюджет {num(p['budget'], 6)} USDT · до {p['n']} {adv3.plural(p['n'], 'сделки', 'сделок', 'сделок')} · STRONG на любом месте рейтинга, стоп не дальше {pct(STOP_MAX)}% входа",
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
    more = p.get('more') or []
    if more:
        lines.append(f"Ещё {len(more)} STRONG {adv3.plural(len(more), 'проходит', 'проходят', 'проходят')} лимиты — ниже, в "
                     f"«Дополнительные STRONG-кандидаты»")
    for it in p['items']:
        lines += [''] + item_lines(it, p['k'], it['rank'])
    if more:
        total, exact = p['loss'] + p['more_loss'], p['loss_exact'] + p['more_loss_exact']
        lines += ['', f"<b>Дополнительные STRONG-кандидаты</b> — сверх запрошенных {p['n']}, в «Итог» не входят: каждая посчитана как "
                      f"одна сделка с риском {pct(p['risk'])}% бюджета ({usdt(p['avg_trade'])} USDT)",
                  f"Вместе с основными потеря на стопах — {usdt(total)} USDT = {pct(100 * total / p['budget'], 2)}% бюджета"
                  + (f"; больше лимита {pct(adv3.RISK_ALL, 0)}%: брать вместо основных, а не вдобавок"
                     if exact > p['budget'] * adv3.RISK_ALL / 100 + 1e-9 else '')]
        for it in more:
            lines += [''] + item_lines(it, p['k'], it['rank'], more=True)
    if p['rejected']:
        lines += ['', 'Отклонены: ' + '; '.join(f'{c} {s} — {why}' for c, s, why in p['rejected'])]
    if p['plain']:
        lines.append(f"Без STRONG среди первых {p['n']} по силе — не берутся: " + ', '.join(p['plain']))
    if any((it['card'].get('rank') or 0) > adv3.TOP_N for it in p['items'] + more):
        lines += ['', adv3.BEYOND]
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

CARD_KEYS = ('coin', 'side', 'strong', 'mode', 'entry', 'stop', 'targets', 'close', 'U', 'since', 'rank', 'of', 'extra')


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
    added to out where it is given. Since TZ-40 an allocation's offered trades are its placed ones and its 'more'."""
    out = {} if out is None else out
    for rec in records:
        close_of = rec.get('close_of')
        placed = None
        if rec.get('kind') == 'alloc' and isinstance(rec.get('alloc'), dict):
            placed = {i.get('coin') for i in (rec['alloc'].get('items') or []) + (rec['alloc'].get('more') or []) if isinstance(i, dict)}
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
    """The STRONG coins that pass an allocation's limits, as (coin, side): the placed ones, then - TZ-40 - its 'more'."""
    return [(it['card']['coin'], it['card']['side']) for it in p['items'] + (p.get('more') or [])]


def alerts_of(fol, passing, prev_passing, done, rep, p):
    """The check's alerts, each with the price it fired at against the close it rests on: a followed trade stopped - by a closed
    candle or the forming one - or ended by its signal at a close, each once; and every STRONG candidate that passes the
    allocation's limits now - placed or, since TZ-40, among its 'more' - that did not at the check before."""
    out = []
    for f in fol:
        kind = {'stop': 'stop', 'touch': 'stop', 'signal': 'signal'}.get(f['state'])
        if kind and (f['coin'], f['side'], f['close_of'], kind) not in done:
            out.append({'kind': kind, 'coin': f['coin'], 'side': f['side'], 'close_of': f['close_of'], 'close': f['close'],
                        'level': f['stop'] if kind == 'stop' else f['price'], 'price': f['price'], 'day': f['day'],
                        'touch': f['state'] == 'touch', 'mark': (rep['rows'].get(f['coin']) or {}).get('mark')})
    placed = {(it['card']['coin'], it['card']['side']): it['card'] for it in p['items'] + (p.get('more') or [])}
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
    placed = {(it['card']['coin'], it['card']['side']): (it, False) for it in p['items']}
    placed.update({(it['card']['coin'], it['card']['side']): (it, True) for it in p.get('more') or []})
    for a in al:
        if a['kind'] == 'candidate':
            if fact:
                it, more = placed[a['coin'], a['side']]
                lines += [f"🆕 STRONG {a['coin']} {SIDE[a['side']]} теперь проходит лимиты распределения ({adv3.num(p['budget'], 6)} "
                          f"USDT, риск {adv3.pct(p['risk'])}%" + (f"; сверх {p['n']} — как одна сделка" if more else '') + '):'] \
                    + item_lines(it, p['k'], more=more)
            else:
                lines.append(f"🆕 STRONG: {a['coin']} {SIDE[a['side']]} проходит лимиты распределения — план ниже")
    return lines


def candidate_lines(rep, p, new):
    """The close's STRONG candidates at the default budget - since TZ-40 every coin STRONG at any rank, in the rule's order, each
    beyond the TOP-3 marked: each placed one with its capital, leverage, margin and loss at the stop, each of 'more' the same as a
    trade of its own, each other named with its reason; 🆕 marks a candidate that did not pass the limits at the check before."""
    strong = strong_all(rep)
    if not strong:
        return ['<b>STRONG-кандидатов нет</b>']
    usdt = adv3.usdt
    lines = [f"<b>STRONG-кандидаты</b> — на любом месте рейтинга; распределение {adv3.num(p['budget'], 6)} USDT, риск "
             f"{adv3.pct(p['risk'])}%, стоп не дальше {adv3.pct(STOP_MAX, 0)}%"]
    placed = {it['card']['coin']: it for it in p['items']}
    more = {it['card']['coin']: it for it in p.get('more') or []}
    why = {c: r for c, _s, r in p['rejected']}
    rank = {coin: k for k, coin in enumerate(ranked(rep), 1)}
    for coin in strong:
        side = rep['rows'][coin]['signal']
        head = f"{'🆕 ' if (coin, side) in new else ''}{coin} {SIDE[side]}{adv3.BEYOND_TAG if rank[coin] > adv3.TOP_N else ''}"
        it = placed.get(coin) or more.get(coin)
        if it:
            beyond = f", сверх {p['n']} (одна сделка)" if coin in more else ''
            lines.append(f"{head} — проходит{beyond}: капитал {usdt(it['notional'])} USDT · плечо {it['leverage']}× изол. · маржа "
                         f"{usdt(it['margin'])} USDT · потеря на стопе {usdt(it['loss'])} USDT")
        else:
            lines.append(f"{head} — не проходит: {why.get(coin, 'вне распределения')}")
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
    check before, and - TZ-40 - the coins STRONG at any rank as at the check before, which a record of TZ-39's does not hold. The
    fact check is its events and the zones left, or one line where it finds neither."""
    loud = bool(al)
    new = {(a['coin'], a['side']) for a in al if a['kind'] == 'candidate'}
    if slot[1] == 'signal':
        same = (prev is not None and prev.get('top') == rep['top'] and prev.get('strong') == rep['strong']
                and all((prev.get('signals') or {}).get(c) == rep['rows'][c].get('signal') for c in rep['top'])
                and isinstance(prev.get('strong_all'), list) and sorted(prev['strong_all']) == sorted(strong_all(rep)))
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
    offered = [it['card'] for it in p['items'] + (p.get('more') or []) if (it['card']['coin'], it['card']['side']) in new]
    return '\n'.join(lines), not loud, False, offered


def alloc_fields(p):
    """An allocation's part of a record: its budget, N, risk, totals, placed trades, since TZ-40 its 'more' in the same shape, and
    the rejected - the fields TZ-37's and TZ-39's records hold."""
    def trade(it):
        return {'coin': it['card']['coin'], 'side': it['card']['side'], 'notional': it['notional'], 'leverage': it['leverage'],
                'margin': it['margin'], 'loss': it['loss']}
    return {'budget': p['budget'], 'n': p['n'], 'risk': p['risk'], 'allocated': p['allocated'], 'free': p['free'], 'loss': p['loss'],
            'items': [trade(it) for it in p['items']], 'more': [trade(it) for it in p.get('more') or []], 'rejected': p['rejected']}


def check_record(slot, rep, fol, al, p, zones, ids, quiet, one_line, offered, at, weak=()):
    """The check's journal record (CANON PART VII's internal log; it measures and tunes nothing): every coin's signal, sum of
    signs, strength, rank, unit, close and mark; the trades the cards offered that this check read, with their state; the
    alerts with the price each fired at against the close it rests on; the trades weakened; the STRONG coins that pass the
    allocation's limits at the default budget, placed and - TZ-40 - 'more'; the coins STRONG at any rank; the zones left; the six
    ratings; and the cards the message offered."""
    rank = {coin: k for k, coin in enumerate(ranked(rep), 1)}
    rec = base_record('check', rep, ids, offered, at)
    rec.update(slot=slot_text(slot), quiet=quiet, one_line=one_line,
               state={coin: {'signal': r.get('signal'), 'sum': r.get('sum'), 'z': r.get('z'), 'rank': rank.get(coin), 'U': r.get('U'),
                             'close': r.get('close'), 'mark': r.get('mark')} for coin, r in rep['rows'].items()},
               followed=[{k: f.get(k) for k in ('coin', 'side', 'close_of', 'close', 'U', 'stop', 'state', 'day', 'price', 'R')}
                         for f in fol if f['state'] != 'closed'],
               alerts=al, weakened=[[c, s] for c, s in weak], passing=[[c, s] for c, s in candidates(p)], zones_left=zones,
               strong_all=strong_all(rep), trust=rep['trust'], alloc=alloc_fields(p))
    return rec


def check(tg, data, slot, now):
    """One scheduled check (TZ-39): the report at the default deposit and risk, the trades the cards offered held by the rule, the
    candle forming since the close at the fact check, the allocation at the default budget over STRONG at every rank (TZ-40), the
    alerts, the weakened trades at the signal check, the message - sent quiet unless it holds an alert - and its record, returned
    for the journal once the message is sent."""
    rep = top_n(live_report(data, adv3.DEPOSIT, adv3.RISK), adv3.TOP_N)
    last = dt.date.fromisoformat(rep['close_of'])
    offs, done, prev = journal_scan()
    forming = {}
    if slot[1] == 'fact':
        held = sorted({k[0] for k in offs if (*k, 'stop') not in done and (*k, 'signal') not in done})
        forming = forming_candles(held, last + adv3.DAY)
    fol = follow(offs, data.cs, data.funds, last, forming, done)
    p = plan_strong(rep, data.cs, adv3.DEPOSIT, adv3.TOP_N, adv3.RISK, volumes(strong_all(rep), rep['made_at_ms']))
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
                p = plan_strong(rep, data.cs, budget, n, risk, volumes(strong_all(rep), rep['made_at_ms']))
                ids = [i for part in plan_parts(rep, p) for i in tg.send(part)]
                rec = base_record('alloc', rep, ids, [it['card'] for it in p['items'] + p['more']])
                rec['alloc'] = alloc_fields(p)
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
    chk('HELP names the commands, the list to 7, STRONG at every rank and its extra section, the 14 % filter, the checks at 04:10 and '
        '16:10 and the quiet rule, in one part', all(k in HELP for k in (
            '«сигнал»', '«сигнал топ 7»', '«сигнал 10000 топ 3»', '«оценка»', '14%', 'на любом месте рейтинга', '«Дополнительные STRONG-кандидаты»',
            'каждая посчитана как одна сделка', 'вне ТОП-3 — не измеряемая стратегия', 'не больше 1%', '04:10', '16:10', 'одной строкой'))
        and len(chunks(HELP)) == 1)
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
    chk('HTML sent as HTML, with a notification', fk.send('<b>ok</b>') == [1] and fk.calls[0]['parse_mode'] == 'HTML'
        and 'disable_notification' not in fk.calls[0])
    chk('unparseable HTML resent as plain text', fk.send('<b>bad &amp; x</b>') == [3]
        and 'parse_mode' not in fk.calls[2] and fk.calls[2]['text'] == 'bad & x')
    n0 = len(fk.calls)
    fk.send('\n'.join(['q' * 3000, 'r' * 3000]), quiet=True)
    fk.send('<b>bad quiet</b>', quiet=True)
    chk('quiet: every part, the plain fallback among them, without a notification',
        len(fk.calls) == n0 + 4 and all(c.get('disable_notification') is True for c in fk.calls[n0:]))
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
    more_rec = {'kind': 'alloc', 'close_of': '2026-10-31', 'alloc': {'items': [{'coin': 'XRP'}], 'more': [{'coin': 'ADA'}]}, 'cards': [
        {'coin': 'XRP', 'side': 1, 'mode': 'market', 'close': 2.0, 'U': 0.2}, {'coin': 'ADA', 'side': 1, 'mode': 'market', 'close': 0.5, 'U': 0.05},
        {'coin': 'SOL', 'side': 1, 'mode': 'market', 'close': 9.0, 'U': 0.5}]}
    chk('offers: an allocation offers its placed trades and, since TZ-40, its more - nothing else of its cards',
        list(offers([more_rec])) == [('XRP', 1, '2026-10-31'), ('ADA', 1, '2026-10-31')])

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
    rows0 = rep0['rows']
    strong_hand = [c for c in order if rows0[c]['sum'] == 4 * rows0[c]['signal'] and abs(rows0[c]['z']) >= 1.0]
    chk('strong_all: every coin whose four signs agree with its side and whose |z| is at least 1, at every rank, in the rule\'s order - '
        'here all twelve; its members among the TOP-3 are the report\'s STRONG (TZ-40)',
        strong_all(rep0) == strong_hand == order and [c for c in strong_all(rep0) if c in rep0['top']] == rep0['strong'])
    c5, c9 = order[4], order[8]
    rows_mix = dict(rows0, **{c5: dict(rows0[c5], sum=2 * rows0[c5]['signal']), c9: dict(rows0[c9], z=0.9 * rows0[c9]['signal'])})
    mix = dict(rep0, rows=rows_mix)
    want_mix = [c for c in order if c not in (c5, c9)]
    m_mix = top_n(mix, 3)
    chk('strong_all and top_n on a mixed market: a coin whose signs do not all agree and one whose |z| is below 1 - which moves to '
        'the end of the order - are neither STRONG nor extra; the STRONG beyond the first three are extra, in order',
        strong_all(mix) == want_mix and ranked(mix)[-1] == c9 and [cd['coin'] for cd in m_mix['cards'] if not cd['extra']] == order[:3]
        and [cd['coin'] for cd in m_mix['cards'] if cd['extra']] == want_mix[3:]
        and not any(cd['coin'] in (c5, c9) for cd in m_mix['cards']))
    r7 = top_n(rep0, 7)
    main7, extra7 = r7['cards'][:7], r7['cards'][7:]
    chk('top_n: seven cards ranked 1 to 7 of 7, the TOP-3\'s own cards first, ★ STRONG wherever four signs agree and |z| >= 1, then '
        'the five STRONG beyond seven marked extra, ranks 8 to 12; the ratings over all twelve; applied twice, the same (TZ-40)',
        [cd['coin'] for cd in main7] == order[:7] and [(cd['rank'], cd['of'], cd['extra']) for cd in main7] == [(k, 7, False) for k in range(1, 8)]
        and all(dict(cd, rank=None, of=None, extra=None) == dict(c0, rank=None, of=None, extra=None) for cd, c0 in zip(main7, rep0['cards']))
        and [cd['coin'] for cd in extra7] == order[7:] and [(cd['rank'], cd['of'], cd['extra']) for cd in extra7] == [(k, 7, True) for k in range(8, 13)]
        and all(cd['strong'] for cd in r7['cards']) and len(r7['trust']['cards']) == 12 and r7['n'] == 7
        and top_n(top_n(rep0, 3), 7)['cards'] == r7['cards'])
    r1 = top_n(rep0, 1)
    m7, m1 = adv3.message(r7, adv3.FACTS), adv3.message(r1, adv3.FACTS)
    others7 = m7.split('Остальные сигналы')[1]
    chk('the TOP-7 message: seven cards under ТОП-7, then five under «Дополнительные STRONG-кандидаты», each with its confidence; '
        'ranks 4 to 12 marked beyond the TOP-3, the extra by their rank beyond the list; the footnote once; no coin left among the other signals',
        m7.count('Основание: сумма знаков') == 12 and m7.count('Уверенность: <b>1/5</b>') == 12
        and m7.index('ТОП-7 по силе тренда') < m7.index('<b>Дополнительные STRONG-кандидаты</b> — за ТОП-7') < m7.index('Остальные сигналы')
        and m7.count('ранг 7 из 7') == 1 and m7.count('ранг 8 — за ТОП-7') == 1 and m7.count('ранг 12 — за ТОП-7') == 1
        and m7.count('· ★ STRONG · вне ТОП-3') == 9 and m7.count(adv3.BEYOND) == 1 and '🟢 ЛОНГ:' not in others7 and '🔴 ШОРТ:' not in others7)
    chk('TOP-1: one card ranked 1 of 1 and the eleven STRONG beyond it, extra', len(r1['cards']) == 12 and m1.count('ранг 1 из 1') == 1
        and len(re.findall(r'ранг \d+ — за ТОП-1', m1)) == 11 and 'ТОП-1 по силе тренда' in m1)
    flat = dict(rep0, rows={c: (dict(r, sum=2 * r['signal']) if c in order[3:] else r) for c, r in rows0.items()})
    m3 = adv3.message(top_n(flat, 3), adv3.FACTS)
    chk('no STRONG beyond the TOP-3: no extra section, no tag, no footnote, the others among the other signals',
        'Дополнительные STRONG' not in m3 and 'вне ТОП-3' not in m3 and m3.count('Основание: сумма знаков') == 3
        and all(c in m3.split('Остальные сигналы')[1] for c in order[3:]))

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

    # ---- TZ-40: STRONG at every rank - plan_strong over TZ-37's plan, golden cases by hand and the limits at random --------------
    def scen2(spec, marks_ok=True):
        """A report of spec's coins alone - (coin, side, |z|, stop %, |sum of signs|) each - every other coin without a signal; its
        TOP-3 and STRONG by the frozen rule's own ranking, its closes and marks 100."""
        rows = {c: {'signal': None} for c in adv3.COINS}
        for coin, side, z, stop, ssum in spec:
            rows[coin] = {'signal': side, 'z': z * side, 'sum': ssum * side, 'U': stop, 'close': 100.0, 'prev': side, 'since': str(last),
                          'stop': 100.0 - side * stop, 'mark': 100.0, 'funding': 0.0001, 'funding_h': 8}
        top, strong = adv3.ranking([(c, (r['signal'], r.get('z'), r.get('sum'), r.get('U'), r.get('close'))) for c, r in rows.items()
                                    if r['signal'] is not None])
        return dict(base, rows=rows, top=top, strong=strong, marks_ok=marks_ok, cards=[])

    ga = [('ETH', 1, 3.0, 8.0, 4), ('SOL', 1, 2.5, 8.0, 2), ('XRP', -1, 2.2, 15.0, 4), ('ADA', 1, 2.0, 8.0, 4), ('BNB', 1, 1.5, 10.0, 4),
          ('LTC', 1, 0.8, 8.0, 4)]
    ra = scen2(ga)
    csa = {'ETH': series(A), 'SOL': series(Cs), 'XRP': series(Cs), 'ADA': series(Bs), 'BNB': series(A), 'LTC': series(Ds)}
    pa = plan_strong(ra, csa, 10000.0, 2, 0.5, {})
    ia, ma = pa['items'], pa['more']
    chk('plan_strong golden: n 2 places the first two STRONG that pass - ETH at rank 1 and ADA at rank 4 - XRP rejected for its 15 % '
        'stop, BNB at rank 5 beyond n in more; SOL without four agreeing signs and LTC with |z| 0.8 not STRONG; SOL the weaker named',
        ra['top'] == ['ETH', 'SOL', 'XRP'] and ra['strong'] == ['ETH', 'XRP'] and strong_all(ra) == ['ETH', 'XRP', 'ADA', 'BNB']
        and [x['card']['coin'] for x in ia] == ['ETH', 'ADA'] and [x['card']['coin'] for x in ma] == ['BNB']
        and pa['rejected'] == [('XRP', 'SHORT', 'стоп 15,0% дальше 14,0%')] and pa['plain'] == ['SOL']
        and [x['card']['rank'] for x in ia + ma] == [1, 4, 5] and [x['rank'] for x in ia + ma] == [1, 2, 3])
    chk('plan_strong golden: the placed pair by TZ-37\'s arithmetic - strengths 3 and 2 uncorrelated, shares 0.6 and 0.4, 731 and 487 USDT, '
        'leverage 7, margin 105 and 70, loss 60 and 40 - and BNB alone at the average risk: 490 USDT, leverage 6, margin 82, loss 50, its '
        'correlation with the placed ones 0.5 (one series with ETH\'s, none with ADA\'s)',
        [(x['notional'], x['leverage'], x['margin'], x['loss']) for x in ia] == [(731, 7, 105, 60), (487, 7, 70, 40)]
        and [round(x['share'], 6) for x in ia] == [0.6, 0.4] and (ma[0]['notional'], ma[0]['leverage'], ma[0]['margin'], ma[0]['loss']) == (490, 6, 82, 50)
        and abs(ma[0]['crowd'] - 0.5) < 1e-9 and pa['allocated'] == 1218 and pa['free'] == 8782 and pa['loss'] == 100 and pa['more_loss'] == 50)
    pb = plan_strong(ra, csa, 10000.0, 7, 0.5, {})
    chk('plan_strong: seven requested, three pass - all three placed, nothing more; one requested - one placed, two more',
        [x['card']['coin'] for x in pb['items']] == ['ETH', 'ADA', 'BNB'] and pb['more'] == [] and pb['plain'] == ['SOL', 'LTC']
        and [x['card']['coin'] for x in plan_strong(ra, csa, 10000.0, 1, 0.5, {})['more']] == ['ADA', 'BNB'])
    gw = [(c, 1, 3.0 - 0.1 * k, 8.0, 4) for k, c in enumerate(('ETH', 'SOL', 'XRP', 'ADA', 'BNB', 'LTC'))]
    rw = scen2(gw)
    csw = {c: series([r * (1 + 0.1 * k) if j % (k + 2) == 0 else 0.0 for j, r in enumerate(A)]) for k, (c, *_x) in enumerate(gw)}
    pw = plan_strong(rw, csw, 10000.0, 1, 1.0, {})
    chk('plan_strong at 1 % and n 1: one placed at 1 %, five more at 1 % each - 1,219 USDT each at an 8 % stop, losses 100 - together '
        'beyond 5 % of the budget', len(pw['items']) == 1 and len(pw['more']) == 5 and all(x['notional'] == 1219 and x['loss'] == 100 for x in pw['items'] + pw['more'])
        and pw['loss_exact'] + pw['more_loss_exact'] > 500)
    rnd2, bad2 = random.Random(40), []
    for trial in range(400):
        coins_ = rnd2.sample(adv3.COINS, rnd2.randint(1, 9))
        spec = [(c, rnd2.choice((1, -1)), rnd2.uniform(0.5, 6.0), rnd2.uniform(0.3, 18.0), rnd2.choice((4, 4, 4, 3, 2))) for c in coins_]
        r = scen2(spec)
        cs2 = {c: series([rnd2.gauss(0, 0.03) if rnd2.random() < 0.8 else x for x in A]) for c in coins_}
        budget, risk, n = rnd2.choice((100.0, 777.0, 10000.0, 250000.0, 3e6)), rnd2.choice((0.05, 0.3, 0.5, 1.0)), rnd2.randint(1, 7)
        liq = {c: rnd2.choice((None, 5e4, 1e6, 1e9)) for c in coins_}
        pp = plan_strong(r, cs2, budget, n, risk, liq)
        order_ = ranked(r)
        rows_ = r['rows']
        quals = [c for c in order_ if rows_[c]['sum'] == 4 * rows_[c]['signal'] and abs(rows_[c]['z']) >= 1.0]
        passing = [c for c in quals if rows_[c]['U'] <= 14.0]
        main_, more_ = [x['card']['coin'] for x in pp['items']], [x['card']['coin'] for x in pp['more']]
        named = [x[0] for x in pp['rejected']]
        trades = pp['items'] + pp['more']
        ok = (set(main_) <= set(passing[:n]) and set(more_) <= set(passing[n:]) and main_ + more_ == [c for c in passing if c in main_ + more_]
              and sorted(main_ + more_ + named) == sorted(quals) and pp['plain'] == [c for c in order_[:n] if c not in quals]
              and all(x['card']['rank'] == order_.index(x['card']['coin']) + 1 for x in trades)
              and all(float(x['notional']).is_integer() and 5 <= x['notional'] <= budget for x in trades)
              and all(x['loss_exact'] <= budget * RM / 100 + 1e-9 for x in pp['items']) and pp['loss_exact'] <= budget * adv3.RISK_ALL / 100 + 1e-9
              and all(x['loss_exact'] <= budget * risk / 100 + 1e-9 and x['share'] == 1 for x in pp['more'])
              and pp['allocated'] == sum(x['notional'] for x in pp['items']) <= budget and pp['free'] == budget - pp['allocated']
              and all(x['margin'] * x['leverage'] >= x['notional'] and 1 <= x['leverage'] <= 20 and x['card']['stop_pct'] <= 14.0 for x in trades)
              and all((not liq.get(x['card']['coin'])) or x['notional'] <= LIQ_FRAC * liq[x['card']['coin']] + 1 for x in trades))
        text_ = plan_parts(r, pp)[0]
        ok = ok and all(text_.count('<%s>' % t) == text_.count('</%s>' % t) for t in ('b', 'i')) and text_.count('Капитал:') == len(trades)
        if not ok:
            bad2.append(trial)
    chk('plan_strong over 400 random scenarios: the placed among the first n that pass, the more among the rest, both in rank order, '
        'every STRONG coin placed, more or named; each more a trade of its own at the average risk; the placed within 1 % and 5 %, whole '
        'positions, the leverage and margin, the liquidity cap; the view balanced, one Капитал a trade', not bad2)
    view = plan_parts(ra, pa)
    first = view[0]
    chk('plan_parts: one message with the Boss\'s fields - budget, count and ranking, quality, entry, stop, targets with TZ-38\'s '
        'shares, capital, leverage, margin, loss, invalidation, unallocated', len(view) == 1 and all(k in first for k in (
            'Бюджет 10 000 USDT', 'STRONG на любом месте рейтинга, стоп не дальше 14,0% входа', 'Подходящих сделок: 2 из 2 запрошенных',
            '1) 🟢 <b>ETH · LONG</b> · ★ STRONG\n', '2) 🟢 <b>ADA · LONG</b> · ★ STRONG · вне ТОП-3', 'Качество: z', 'Вход:', '⛔ Стоп:',
            '· дошли 47%', 'Капитал:', 'плечо', 'маржа', 'Потеря на стопе:', 'Свободно', 'Размещено', 'Инвалидация:')))
    chk('plan_parts: each trade its confidence with the note that the sizes are unproven; no six ratings; the rejected and the weaker named',
        first.count('Уверенность: <b>1/5</b> — правило не доказано · размеры — формула Архитектора, не доказана') == 3
        and 'Оценка доверия' not in first and 'Отклонены: XRP SHORT — стоп 15,0% дальше 14,0%' in first
        and 'Без STRONG среди первых 2 по силе — не берутся: SOL' in first and 'не доказанная' in first and 'больше 3 сделок не будет' not in first)
    chk('plan_parts: the more under «Дополнительные STRONG-кандидаты» after the placed, each a trade of its own at the average risk with '
        'its correlation with the placed ones, the loss of all together against the 5 % limit, the footnote on STRONG beyond the TOP-3 (TZ-40)',
        'Ещё 1 STRONG проходит лимиты — ниже, в «Дополнительные STRONG-кандидаты»' in first
        and first.index('2) 🟢 <b>ADA') < first.index('<b>Дополнительные STRONG-кандидаты</b> — сверх запрошенных 2, в «Итог» не входят: '
                                                     'каждая посчитана как одна сделка с риском 0,5% бюджета (50 USDT)') < first.index('3) 🟢 <b>BNB · LONG</b> · ★ STRONG · вне ТОП-3')
        and 'Вместе с основными потеря на стопах — 150 USDT = 1,50% бюджета\n' in first and 'больше лимита' not in first
        and 'вне распределения — одна сделка · корреляция с основными +0,50' in first and 'Капитал: <b>490 USDT</b>' in first
        and first.count(adv3.BEYOND) == 1)
    vw = plan_parts(rw, pw)[0]
    chk('plan_parts: more beyond 5 % of the budget says to take them instead of the placed ones, not on top; all within the TOP-3 no footnote',
        'больше лимита 5%: брать вместо основных, а не вдобавок' in vw and 'Ещё 5 STRONG проходят лимиты' in vw
        and adv3.BEYOND in vw and adv3.BEYOND not in plan_parts(scen2(ga[:1]), plan_strong(scen2(ga[:1]), csa, 10000.0, 3, 0.5, {}))[0])
    chk('plan_parts: balanced markup; none qualifying says so',
        all(first.count('<%s>' % t) == first.count('</%s>' % t) for t in ('b', 'i'))
        and 'Подходящих сделок нет' in plan_parts(scen2([('SOL', -1, 2.5, 15.0, 4)]), plan_strong(scen2([('SOL', -1, 2.5, 15.0, 4)]),
                                                                                                    {'SOL': series(A)}, 10000.0, 3, 0.5, {}))[0])

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
    p_ = plan_strong(rep0, cs, D2, 3, 0.5, {})
    placed = candidates(p_)
    chk('the synthetic market: the default allocation places the TOP-3\'s three STRONG and the nine beyond them pass as more; the '
        'candidates are the twelve, placed first', [x['card']['coin'] for x in p_['items']] == rep0['strong'] == order[:3]
        and [x['card']['coin'] for x in p_['more']] == order[3:] and [c for c, _ in placed] == strong_all(rep0))
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
    prev_same = {'top': rep0['top'], 'strong': rep0['strong'], 'signals': {c: rep0['rows'][c].get('signal') for c in adv3.COINS},
                 'strong_all': list(reversed(strong_all(rep0)))}
    still = top_n(dict(rep0, rows={c: dict(r, prev=r.get('signal')) for c, r in rep0['rows'].items()}), 3)
    t1, q1, o1, cards1 = compose((last + adv3.DAY, 'signal'), still, [], [], p_, [], prev_same, now0)
    t1w, q1w, o1w, _c = compose((last + adv3.DAY, 'signal'), still, [], [], p_, [], prev_same, now0, [(order[0], 1)])
    chk('compose: a signal check that finds nothing is one quiet line naming the TOP-3, offering no card; a weakening makes it full and quiet',
        q1 and o1 and cards1 == [] and '\n' not in t1 and t1.startswith('✓ 04:10 по Батуми') and ', '.join(rep0['top']) in t1
        and q1w and not o1w and 'ℹ️ Ослабление' in t1w)
    t1a = compose((last + adv3.DAY, 'signal'), still, [], [], p_, [], dict(prev_same, strong_all=order[:-1]), now0)
    t1b = compose((last + adv3.DAY, 'signal'), still, [], [], p_, [], {k: v for k, v in prev_same.items() if k != 'strong_all'}, now0)
    chk('compose: the STRONG at every rank not as at the check before - one gained - or a check before that does not record them (TZ-39\'s) '
        'make the signal check full and quiet; their order alone does not (TZ-40)', not t1a[2] and t1a[1] and not t1b[2] and t1b[1])
    flip = order[-1]
    moved = top_n(dict(still, rows=dict(still['rows'], **{flip: dict(still['rows'][flip], prev=-still['rows'][flip]['signal'])})), 3)
    t2, q2, o2, cards2 = compose((last + adv3.DAY, 'signal'), moved, fol0, [], p_, [], prev_same, now0)
    chk('compose: a signal check with the day\'s changes is the full message, quiet without an alert, its cards offered - the TOP-3\'s and '
        'the nine STRONG beyond them - no methodology', q2 and not o2 and cards2 == moved['cards'] and len(cards2) == 12
        and [cd['extra'] for cd in cards2] == [False] * 3 + [True] * 9 and 'STRONG-кандидаты' in t2 and 'Сделки по карточкам бота' in t2
        and '🔄 Разворот' in t2 and 'XRP LONG — карточка' in t2 and 'Оценка доверия' not in t2 and 'Форвард с' not in t2 and '🔔' not in t2)
    chk('compose: the signal check\'s message carries the TOP-3, the nine STRONG beyond it in their own section, and among the candidates '
        'the three placed and the nine more, each beyond the TOP-3 marked (TZ-40)', t2.count('Основание: сумма знаков') == 12
        and '<b>Дополнительные STRONG-кандидаты</b> — за ТОП-3' in t2 and t2.count('— проходит, сверх 3 (одна сделка): капитал') == 9
        and t2.count('— проходит: капитал') == 3 and t2.count(adv3.BEYOND_TAG + ' — проходит') == 9 and t2.count(adv3.BEYOND) == 1)
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
    chk('compose: a new candidate beyond the placed ones is announced as a trade of its own, outside the allocation (TZ-40)',
        t6.count('; сверх 3 — как одна сделка):') == 9 and t6.count('вне распределения — одна сделка') == 9
        and t6.count('из ±4 · доля ') == 3)
    chk('compose: every part of every message balances its markup; the quiet lines are one part each', all(
        all(x.count('<b>') == x.count('</b>') and x.count('<i>') == x.count('</i>') for x in chunks(t)) for t in (t1, t2, t3, t4, t5, t6))
        and len(chunks(t1)) == len(chunks(t4)) == 1)
    recq = check_record((last + adv3.DAY, 'signal'), rep0, fol0 + [dict(fol0[0], state='closed')], al, p_, [], [7, 8], False, False, cards2, now0,
                        [('XRP', 1)])
    chk('check_record: kind, slot, flags, every coin\'s state with the ranks, the followed trades but the closed, the alerts with their '
        'prices, the placed coins, the six ratings, the cards with their confidence', recq['kind'] == 'check' and recq['slot'] == slot_text((last + adv3.DAY, 'signal'))
        and recq['quiet'] is False and recq['one_line'] is False and len(recq['state']) == len(adv3.COINS)
        and [c for c in adv3.COINS if recq['state'][c]['rank']] == [c for c in adv3.COINS if c in order]
        and all(recq['state'][c]['rank'] == order.index(c) + 1 for c in order) and len(recq['followed']) == 4
        and recq['alerts'] == al and recq['passing'] == [list(x) for x in placed] and recq['message_ids'] == [7, 8] and recq['weakened'] == [['XRP', 1]]
        and set(recq['trust']) >= {'system', 'strong_justified', 'cards', 'quality', 'expectancy_established'}
        and [c['confidence'] for c in recq['cards']] == [moved['trust']['cards'][cd['coin']] for cd in cards2]
        and json.loads(json.dumps(recq, default=str))['utc'] == now0.isoformat(timespec='seconds'))
    chk('check_record: the STRONG at every rank in the rule\'s order, the allocation\'s more in the placed trades\' shape, each card '
        'whether it was extra (TZ-40)', recq['strong_all'] == order and [x['coin'] for x in recq['alloc']['more']] == order[3:]
        and set(recq['alloc']['more'][0]) == set(recq['alloc']['items'][0]) == {'coin', 'side', 'notional', 'leverage', 'margin', 'loss'}
        and [c['extra'] for c in recq['cards']] == [False] * 3 + [True] * 9)

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
        n_sent, k1, k2 = len(cap.sent), len(e1['message_ids']), len(e2['message_ids'])
        chk('end to end: the signal check sends the full message in parts, quiet with no alert, records 42 states, its twelve cards and the '
            'twelve coins that pass', e1['kind'] == 'check' and e1['slot'] == slot_text((last + adv3.DAY, 'signal')) and not e1['one_line']
            and k1 >= 2 and all(q == e1['quiet'] for _t, q in cap.sent[:k1]) and e1['quiet'] == (not e1['alerts']) and len(e1['state']) == 42
            and len(e1['cards']) == 12 and e1['passing'] == [list(x) for x in placed] and all(a['kind'] == 'candidate' for a in e1['alerts'])
            and len(e1['alerts']) == len(placed) and e1['strong_all'] == order)
        chk('end to end: the fact check reads the forming candle through the stop of the offer the old daily record made - one loud alert',
            [(a['kind'], a['coin'], a['touch']) for a in e2['alerts']] == [('stop', top0, True)] and e2['quiet'] is False
            and cap.sent[k1][1] is False and 'задет сегодня' in cap.sent[k1][0] and e2['one_line'] is False)
        chk('end to end: the same fact check again sends no second alert - the offer is closed - and finds the candidates placed before',
            e3['alerts'] == [] and e3['quiet'] is True and n_sent == k1 + k2 + 1 and len(e3['message_ids']) == 1
            and not [f for f in e3['followed'] if f['coin'] == top0 and f['close_of'] == str(last) and f['U'] == r0['U'] * 0.25])
        recs2 = list(journal_records())
        chk('end to end: the journal parses past its broken line, holds the old record and the two checks, in order',
            [r['kind'] for r in recs2] == ['daily', 'check', 'check'] and recs2[1]['utc'] == now0.isoformat(timespec='seconds'))

        def fake_make_fail(*a_, **k_):
            raise RuntimeError('fapi.binance.com served no candles')

        cap2, per = Cap(), []
        with contextlib.redirect_stdout(io.StringIO()):
            for text in ('сигнал', 'сигнал топ 7', 'оценка', 'сигнал 10000 топ 3', 'привет'):
                n0 = len(cap2.sent)
                handle(cap2, stub, text)
                per.append('\n'.join(t for t, _q in cap2.sent[n0:]))
            n5 = len(cap2.sent)
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
        chk('handle: «сигнал» the TOP-3 and the nine STRONG beyond it, «сигнал топ 7» the seven and five, «оценка» the assessment, the '
            'allocation its three and nine more, an unknown text HELP; every part with a notification',
            per[0].count('Основание:') == 12 and len(re.findall(r'ранг \d+ — за ТОП-3', per[0])) == 9 and per[1].count('Основание:') == 12
            and len(re.findall(r'ранг \d+ — за ТОП-7', per[1])) == 5 and per[2].startswith('🧭') and 'Оценка доверия' in per[2] and 'на семи местах дал +0,51 R' in per[2]
            and per[3].startswith('💼') and per[3].count('Капитал:') == 12 and per[4] == HELP and all(q is False for _t, q in cap2.sent[:n5]))
        chk('handle: the journal holds request, request, assess, alloc, each with its cards; an unknown text no record; the allocation\'s '
            'cards its twelve trades and its record their nine more', kinds == ['request', 'request', 'assess', 'alloc'] and recs3[3]['n'] == 3
            and recs3[4]['n'] == 7 and recs3[5]['cards'] == [] and 'trust' in recs3[5] and len(recs3[6]['cards']) == len(placed)
            and len(recs3[6]['alloc']['more']) == 9 and len(recs3[3]['cards']) == 12)
        chk('handle: Binance down gets the apology, Telegram down raises nothing', texts[-1].startswith('Binance или Telegram не ответили'))
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

```text file=advisor/selftest-adv3.py
#!/usr/bin/env python3
# selftest-adv3.py - the Architect's checks of adv3.py's mechanics on synthetic candles; no network.
# Every expectation is computed here by hand or by an independent formula, never by adv3.py itself.
# TZ-39: the message without its methodology, each card's confidence, the reach shares without survivorship, the assessment.
# TZ-40: a STRONG card beyond the TOP-3 says so, the cards marked extra under their own heading, the assessment on STRONG with seven places.
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
head = lambda cd: a.card_lines(cd, a.FACTS)[0]
check('a STRONG card ranked beyond the TOP-3 carries «· вне ТОП-3»; one ranked within it, or not STRONG, or with no rank, does not (TZ-40)',
      head(dict(strong_card, rank=4)).endswith(' · ★ STRONG · вне ТОП-3') and head(dict(strong_card, rank=3)).endswith(' · ★ STRONG')
      and head(dict(plain_card, rank=5)).endswith('</b>') and head(dict(strong_card, rank=None)).endswith(' · ★ STRONG'))
check('a card marked extra gives its rank beyond the list; a card of the list its rank of N (TZ-40)',
      any(l.endswith('ранг 5 — за ТОП-3') for l in a.card_lines(dict(strong_card, rank=5, of=3, extra=True), a.FACTS))
      and any(l.endswith('ранг 2 из 7') for l in a.card_lines(dict(strong_card, rank=2, of=7, extra=False), a.FACTS)))
order6 = sorted([c for c in a.COINS if rows.get(c, {}).get('signal') in (1, -1)], key=lambda c: -abs(rows[c]['z']))
extras = [dict(a.card(c, rows[c], True, 10000.0, 0.5), rank=k, of=3, extra=True) for k, c in enumerate(order6[3:5], 4)]
with_extra = dict(rep, cards=rep['cards'] + extras)
mx = a.message(with_extra, a.FACTS)
check('the message: the cards marked extra under «Дополнительные STRONG-кандидаты» after the TOP-3 and before the other signals, '
      'each with its basis; the line on STRONG beyond the TOP-3 once; neither in a message without them (TZ-40)',
      mx.index('ТОП-3 по силе тренда') < mx.index('<b>Дополнительные STRONG-кандидаты</b> — за ТОП-3') < mx.index('Остальные сигналы')
      and mx.count('Основание: сумма знаков') == 5 and mx.count(a.BEYOND) == 1 and mx.count(' · ★ STRONG · вне ТОП-3') == 2
      and 'Дополнительные STRONG' not in msg and a.BEYOND not in msg and all(c not in mx.split('Остальные сигналы')[1] for c in order6[:5]))
check('the assessment: STRONG beyond the TOP-3 is not the measured strategy, with E6\'s mean R a trade at seven places and at three',
      '★ STRONG вне ТОП-3 — те же условия и тот же расчёт, но не измеряемая стратегия' in ass
      and 'STRONG на семи местах дал +0,51 R на сделку против +0,80 на трёх; дальше седьмого места не измерено' in ass
      and (a.PIT['strong']['mean_R_P7'], a.PIT['strong']['mean_R_P3']) == (0.5084, 0.7962))

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

```text file=research/tz40-advisor-strong.py
#!/usr/bin/env python3
# tz40-advisor-strong.py - TZ-40's checker: the fingerprint, the host gate, the number, G-RULE, COPY, G-RENDER, the readings
# after the unit's restart - UNIT-NEW and G-FIRST - and the marks. Standard library only. It starts and stops no unit, signals no
# process and sends no request of its own (G-RENDER runs the service copy's bot, which reads Binance's public market), and it
# never reads or prints the bot's token or the pinned chat, a coin, a price or a size. It writes one file of the unit's record,
# /var/lib/adv3-bot/check-done: at the kill mark the slot before the day's signal check, so that the new process replays that
# check at its start, and at the rollback mark the kill mark's value again where the new process never moved it.
# Exits: 0 every assert held; 1 a failed assert, named; 3 NOT YET.
import ast, bisect, calendar, contextlib, datetime as dt, hashlib, importlib.util, io, json, math, os, re, shutil, subprocess, \
    sys, time

WORK = '/root/tz40-work'
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
TZ_FILE = 'CryptoTZ/TZ-40-strong-every-rank.md'
NUMBER = 'TZ-40-'
BRANCH = 'tz-40-strong-every-rank'
MAP_REV = '2026-11-01-a'
ANCHORS = {'A1': '229a944f2d51', 'A2': '6c5089330629',
           'A3': '0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable',
           'A4': '437b45ea196b', 'A5': '0f6c90451cbd', 'A6': '729f0bcdbee3'}
DERIVED = {'A2': 'research/twap-divergence.py', 'A4': 'BTC-EXECUTOR-INSTRUCTIONS.md',
           'A5': 'research/recorder/recorder.py', 'A6': 'research/pfair.py'}
H = {'adv3_old': 'c19572dccf30a505342ca334e42c7ec347a5d29db4db20887229d2a8c7b48e31',
     'adv3_new': '81ef0112d3fe4b86566e51a51aab924d9776ff37a927e65982ecb0bb7c1f34e1',
     'bot_old': 'ca989b6fe487d41181b32312418d6acda1e9c64fbf5cfbb3f041d54826dd108f',
     'bot_new': '9e622daf2e8a5ec3e93f15c7f56e7cf859547fbd3771daad75bc6532adb2b9d1',
     'selftest_old': '09d2ba9a8361ec5ebc7f5934ebb818d1a685bb16fb3f32b7da94409d9516cc0e',
     'selftest_new': '6f29b82f2b2ca82cd2ff4bbb370e032354dbb4743497330530777429b3af7398',
     'rule': 'ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169',
     'unit': '82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66'}
TZ38 = ('CryptoReports/TZ-38-adv3-pit-validation-report.md', 'f4a0ac3f643ac99dd08f20c8c8c43bf1e98e51b2954592d1456a59ae98030528')
# G-RULE's tables: (changed, added, removed) definitions and assignments of each file against origin/main's
ADV3_DEFS = ({'assessment', 'card_lines', 'message'}, set(), set())
ADV3_RULE = ('signs', 'signal', 'strength', 'true_range', 'unit', 'open_at', 'hold', 'close_at', 'simulate', 'states', 'ranking',
             'simulate_strong', 'stats', 'funding_of', 'report', 'card', 'trust')
ADV3_ASG = ({'PIT'}, {'BEYOND', 'BEYOND_TAG'}, set())
BOT_DEFS = ({'Telegram', 'alerts_of', 'candidate_lines', 'candidates', 'check', 'check_record', 'compose', 'event_lines', 'handle',
             'item_lines', 'offers', 'plan_parts', 'selftest', 'top_n'},
            {'TooMany', 'alloc_fields', 'plan_strong', 'strong_all', 'volumes'}, set())
BOT_SAME = ('plan', 'ranked', 'route', 'Data', 'liquidity', 'follow', 'journal_scan', 'due', 'done_after', 'serve', 'main')
BOT_ASG = ({'CARD_KEYS', 'HELP'}, {'PACE'}, set())
# this TZ's numbers: the allocation's limits, the list's length, the two checks' instants, the rung, the pause between parts
STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, RISK_MAX, RISK_ALL, LIST_MAX, RUNG, PACE, STRONG_Z = 14.0, 5.0, 0.001, 1.0, 5.0, 7, 1, 1.1, 1.0
SLOTS = (('signal', dt.time(0, 10)), ('fact', dt.time(12, 10)))
MEM_FLOOR, DISK_FLOOR = 140_037_206, 7_400_000_000
ROWS, FROZEN = 59, 56
FIRST_BOUND = 900
TZ39_FIRST = '2026-11-01 signal'
RENDER_CASES = ('сигнал', 'сигнал топ 7', 'сигнал 10000 топ 3', 'сигнал 15000 топ 5', 'оценка', 'помощь', 'привет')
RENDER_KINDS = ['request', 'request', 'alloc', 'alloc', 'assess', 'check', 'check']
TRUST = ('Оценка доверия', 'Надёжность системы: <b>1/5</b>', 'Уверенность в сделках:', 'STRONG обоснован: <b>нет</b>',
         'Качество данных: <b>низкое</b>', 'Ожидаемая R на сделку: <b>не установлена</b>', 'Инвалидация: у каждой карточки')
METHOD = ('Оценка доверия', 'Надёжность системы', 'Форвард с 28.10', 'история 2020–2026', 'Открытые STRONG-сделки')
TRUST_KEYS = {'system', 'strong_justified', 'served', 'cards', 'quality', 'fresh', 'complete', 'expectancy_established'}
CARD = re.compile(r'^[🟢🔴] <b>([A-Z0-9]+) · (LONG|SHORT)</b>', re.M)
CONF = re.compile(r'^Уверенность: <b>([0-5])/5</b> — ', re.M)
EXTRA_HEAD = '<b>Дополнительные STRONG-кандидаты</b>'
TAG = ' · вне ТОП-3'
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
                                                  ', the %d this checker names among them' % len(rule) if rule else ''):
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
    median and its share of lists in profit, the size of G, and - TZ-40 - E6's mean R a trade of STRONG with three places and with
    seven; each cell read as a number."""
    sec = report_sections(text)
    pick = lambda prefix: next(v for k, v in sec.items() if k.startswith(prefix))
    e1, e2, e4, e5, e6, sets = pick('E1 '), pick('E2 '), pick('E4 '), pick('E5 '), pick('E6 '), pick('The sets ')
    f = lambda s: float(s.replace(',', ''))
    return {'base': {'mfe': {n: f(e4['mfe +%dR' % n][0]) for n in (1, 2, 3)}, 'mean_R_G': f(e1['mean_R'][0]),
                     'trades_G': int(f(e1['trades'][0])), 'p_G': f(e1['p_t_up'][0]), 'contracts_G': int(f(sets['G'][0]))},
            'strong': {'mfe': {n: f(e4['mfe +%dR' % n][1]) for n in (1, 2, 3)}, 'p_G': f(e2['p_t_up'][0]),
                       'mean_R_lists': f(e5['0.5'][1]), 'lists': int(f(e5['lists'][0])),
                       'lists_positive': f(e5['share_mean_R_positive'][0]), 'top5_share': f(e4['top5_share'][1]),
                       'mean_R_P3': f(e6['mean_R'][0]), 'mean_R_P7': f(e6['mean_R'][2])}}


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


def own_stop_pct(row):
    """The stop's distance in percent of the entry a card offers, by RULE-ADV-3's display rules read here: the stop C - k*U; LONG
    above the zone a limit at its top, else at market while more than 0.25*U above the stop, else no entry; SHORT mirrored.
    None where no entry is offered."""
    k, C, U = row['signal'], row['close'], row['U']
    S, P = C - k * U, row.get('mark') or C
    if k > 0:
        entry = C + 0.25 * U if P > C + 0.25 * U else P if P > S + 0.25 * U else None
    else:
        entry = C - 0.25 * U if P < C - 0.25 * U else P if P < S - 0.25 * U else None
    return None if entry is None else 100 * abs(entry - S) / entry


def plan_invariants(p, rep, liq, budget, n, risk):
    """The allocation's limits (TZ-40), read from a plan (the bot's own plan_strong) and the report and liquidity it was made from,
    against this checker's own order, STRONG and stops. The limits are this TZ's: stop 14 %, minimum 5 USDT, liquidity 0.1 %, risk
    1 % a trade and 5 % in all for the placed, the average risk for each of the more."""
    rows = rep['rows']
    order = own_order(rows, list(rows))
    strong = own_strong(rows, order)
    passing = [c for c in strong if rep['marks_ok'] and own_stop_pct(rows[c]) is not None and own_stop_pct(rows[c]) <= STOP_MAX]
    items, more = p['items'], p.get('more') or []
    placed, extra = [it['card']['coin'] for it in items], [it['card']['coin'] for it in more]
    named = [r[0] for r in p['rejected']]
    small = {r[0] for r in p['rejected'] if r[2] == 'позиция меньше 5 USDT'}
    trades = items + more
    return {
        'the placed are the first n STRONG coins at any rank that pass the limits, the more the rest that pass, both in rank order':
            placed == [c for c in passing[:n] if c not in small] and extra == [c for c in passing[n:] if c not in small],
        'every STRONG coin is placed, among the more or named with a reason, once': sorted(placed + extra + named) == sorted(strong),
        'every trade has an entry and a stop within 14 % of it, on current prices': (
            all(it['card']['entry'] is not None and it['card']['stop_pct'] <= STOP_MAX
                and abs(it['card']['stop_pct'] - own_stop_pct(rows[it['card']['coin']])) < 1e-9 for it in trades) and (rep['marks_ok'] or not trades)),
        'each placed loss at its stop within 1 % of the budget and all within 5 %; each of the more within the average risk': (
            all(it['loss_exact'] <= budget * RISK_MAX / 100 + 1e-9 for it in items)
            and sum(it['loss_exact'] for it in items) <= budget * RISK_ALL / 100 + 1e-9
            and all(it['loss_exact'] <= budget * risk / 100 + 1e-9 for it in more)),
        'whole positions of at least 5 USDT, the placed together within the budget, free the budget less them': (
            all(float(it['notional']).is_integer() and MIN_NOTIONAL <= it['notional'] <= budget for it in trades)
            and p['allocated'] == sum(it['notional'] for it in items) <= budget and p['free'] == budget - p['allocated']),
        'leverage the rule\'s formula and at most 20, the margin covering the position, a position within its liquidity cap': all(
            it['leverage'] == min(20, math.floor(1 / (1.5 * it['card']['stop_pct'] / 100 + 0.01)))
            and it['margin'] * it['leverage'] >= it['notional']
            and ((not liq.get(it['card']['coin'])) or it['notional'] <= LIQ_FRAC * liq[it['card']['coin']]) for it in trades),
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
    before is alerted, and each candidate is a STRONG coin that passes the plan's limits - placed or among the more - that did not
    pass them at the check before."""
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
    placed = [(it['card']['coin'], it['card']['side']) for it in run['plan']['items'] + (run['plan'].get('more') or [])]
    cand = [(a['coin'], a['side']) for a in rec['alerts'] if a['kind'] == 'candidate']
    return sorted(got) == sorted(want) and cand == [x for x in placed if x not in prev_passing]


def card_blocks(text):
    """The card blocks of a message - each from its header line to the blank line after it - as (coin, header line, block text)."""
    out_ = []
    for block in text.split('\n\n'):
        m = CARD.match(block)
        if m:
            out_.append((m.group(1), block.split('\n')[0], block))
    return out_


def list_ok(text, rep, n_of):
    """A list message («сигнал», «сигнал топ N», the signal check) against this checker's own order and STRONG: the rule's first
    n_of coins ranked k of n_of, then every STRONG coin beyond them under the extra heading ranked by its place beyond the list;
    ★ STRONG on a card exactly where the coin is STRONG at any rank, «вне ТОП-3» exactly where such a card's rank is beyond 3;
    every card its basis, its invalidation and one confidence line reading the rung 1 or 0; the footnote once where a tag shows."""
    rows = rep['rows']
    order = own_order(rows, list(rows))
    strong = own_strong(rows, order)
    rank = {c: k for k, c in enumerate(order, 1)}
    want = order[:n_of] + [c for c in order[n_of:] if c in strong]
    blocks = card_blocks(text)
    coins = [c for c, _h, _b in blocks]
    tags = [c for c, h, _b in blocks if h.endswith(TAG)]
    head_ok = all(('★ STRONG' in h) == (c in strong) and h.endswith(TAG) == (c in strong and rank[c] > 3) for c, h, _b in blocks)
    basis_ok = all(('ранг %d из %d' % (rank[c], n_of) if rank[c] <= n_of else 'ранг %d — за ТОП-%d' % (rank[c], n_of)) in b
                   for c, _h, b in blocks)
    each = all(b.count('Основание: сумма знаков') == 1 and b.count('Инвалидация: цена') == 1 and len(CONF.findall(b)) == 1
               and int(CONF.findall(b)[0]) in (0, RUNG) for _c, _h, b in blocks)
    extra_ok = ((EXTRA_HEAD in text) == bool(want[n_of:])) and (not want[n_of:] or text.index(EXTRA_HEAD) < text.index(
        '%s <b>%s · ' % ({1: '🟢', -1: '🔴'}[rows[want[n_of]]['signal']], want[n_of])))
    return coins == want and head_ok and basis_ok and each and extra_ok and (text.count(BEYOND_LINE) == (1 if tags else 0))


BEYOND_LINE = '★ STRONG вне ТОП-3 — четыре знака совпадают и |z| ≥ 1'


def render_checks(texts, calc, runs, kinds, records, log, same, expect):
    """G-RENDER: what the service copy's bot sent for each command (texts, by command, each a list of parts), the reports the list
    commands were made from (calc['lists']), the plan the checker recomputed from the report and liquidity each allocation reply
    was made from (calc), the two checks run on live data (runs), the scratch journal's kinds and records, the bot's log, whether the
    bot's own record is as before, and the bot module's constants (expect); counts and labels only."""
    whole = lambda parts: '\n'.join(parts)
    sig, top7, ass = whole(texts[RENDER_CASES[0]]), whole(texts[RENDER_CASES[1]]), whole(texts[RENDER_CASES[4]])
    allocs = [c for c in RENDER_CASES if c in calc]
    lists = calc.get('lists') or {}
    usdt, num = expect['usdt'], expect['num']
    inv = {c: plan_invariants(calc[c]['plan'], calc[c]['rep'], calc[c]['liq'], calc[c]['budget'], calc[c]['n'], calc[c]['risk'])
           for c in allocs}

    def fields(c):
        p, t = calc[c]['plan'], whole(texts[c])
        more = p.get('more') or []
        head = ('не доказанная' in t and 'Бюджет %s USDT' % num(p['budget'], 6) in t and 'Размещено %s USDT' % usdt(p['allocated']) in t
                and ('Свободно %s USDT' % usdt(p['free']) in t or 'свободно %s USDT' % usdt(p['free']) in t) and 'Оценка доверия' not in t
                and 'STRONG на любом месте рейтинга' in t and 'больше 3 сделок не будет' not in t)
        if not p['items']:
            return head and 'Подходящих сделок нет' in t and not more
        k, m = len(p['items']), len(more)
        total = p['loss'] + sum(it['loss'] for it in more)
        exact = p['loss_exact'] + sum(it['loss_exact'] for it in more)
        more_ok = (EXTRA_HEAD in t) == bool(more) and (not more or (
            'сверх запрошенных %d, в «Итог» не входят' % p['n'] in t and t.count('вне распределения — одна сделка') == m
            and 'Вместе с основными потеря на стопах — %s USDT' % usdt(total) in t
            and ('больше лимита 5%' in t) == (exact > p['budget'] * RISK_ALL / 100 + 1e-9)))
        return (head and more_ok and 'Подходящих сделок: %d из %d запрошенных' % (k, p['n']) in t
                and all(t.count(x) == k + m for x in ('Капитал:', 'Потеря на стопе:', '⛔ Стоп:', 'Инвалидация: цена', 'Качество: z'))
                and t.count('🎯') == 3 * (k + m) and t.count('размеры — формула Архитектора, не доказана') == k + m
                and 'Потеря на стопах %s USDT' % usdt(p['loss']) in t and 'маржа %s USDT' % usdt(p['margin']) in t)

    sg, fa = runs.get('signal'), runs.get('fact')

    def run_shape(r, kind):
        rec, sent = r['rec'], r['sent']
        alerts = rec['alerts']
        loud = bool(alerts)
        flags = all(q == rec['quiet'] for _t, q in sent) and rec['quiet'] == (not loud) and len(sent) >= 1
        text = whole(t for t, _q in sent)
        rows = r['rep']['rows']
        order = own_order(rows, list(rows))
        strong = own_strong(rows, order)
        if rec['one_line']:
            shape = (not loud and len(sent) == 1 and '\n' not in text and text.startswith('✓ ') and rec['cards'] == []
                     and (kind == 'fact' and not rec['zones_left'] or kind == 'signal' and not r['changes'] and r['same'] and not rec['weakened']))
        elif kind == 'signal':
            want = order[:3] + [c for c in order[3:] if c in strong]
            shape = ('STRONG-канд' in text and 'Сделки по карточкам бота' in text and not any(m in text for m in METHOD)
                     and [c['coin'] for c in rec['cards']] == want and list_ok(text, r['rep'], 3)
                     and (loud or r['changes'] or not r['same'] or bool(rec['weakened'])) and (('🔔 <b>События</b>' in text) == loud)
                     and (('ℹ️ Ослабление' in text) == bool(rec['weakened'])))
        else:
            shape = (('🔔 <b>События</b>' in text) == loud and (loud or bool(rec['zones_left'])) and CARD.findall(text) == []
                     and [(c['coin'], c['side']) for c in rec['cards']] == [(a['coin'], a['side']) for a in alerts if a['kind'] == 'candidate'])
        return flags and shape and all(html_balanced(t) for t, _q in sent)

    def record_ok(r, kind):
        rec, p = r['rec'], r['plan']
        rows = r['rep']['rows']
        order = own_order(rows, list(rows))
        return (rec['kind'] == 'check' and rec['slot'].endswith(' ' + kind) and len(rec['state']) == 42 and TRUST_KEYS <= set(rec['trust'])
                and rec['rule'] == H['rule'] and rec['close_of'] == r['rep']['close_of']
                and rec['passing'] == [[it['card']['coin'], it['card']['side']] for it in p['items'] + (p.get('more') or [])]
                and rec['strong_all'] == own_strong(rows, order) and isinstance(rec['alloc'].get('more'), list)
                and len(rec['alloc']['more']) == len(p.get('more') or []) and all('extra' in c for c in rec['cards'])
                and all(rec['state'][c]['rank'] == k for k, c in enumerate(order, 1)))

    ok_inv = lambda key: all(v[key] for v in inv.values())
    c5 = RENDER_CASES[3]
    return {
        'every command and both checks answered, no traceback and no failed request in the bot\'s log':
            all(texts[k] for k in RENDER_CASES) and sg is not None and fa is not None and 'Traceback' not in log and 'failed' not in log,
        'the markup is balanced in every part of every message (b, i)': all(html_balanced(t) for ps in texts.values() for t in ps),
        '«сигнал»: the TOP-3 ranked k of 3, then every STRONG coin beyond them, extra; ★ STRONG and «вне ТОП-3» exactly where they '
        'belong; each card its basis, invalidation and confidence, the rung 1 or 0; no methodology':
            RENDER_CASES[0] in lists and list_ok(sig, lists[RENDER_CASES[0]], 3) and not any(m in sig for m in METHOD)
            and 'на чём держится уверенность' in sig,
        '«сигнал топ 7»: the first seven ranked k of 7, then every STRONG coin beyond them, extra, with the same labels and lines':
            RENDER_CASES[1] in lists and list_ok(top7, lists[RENDER_CASES[1]], 7) and 'ТОП-7 по силе тренда' in top7,
        '«оценка»: the rung and the next readings, the six ratings, the forward record; STRONG at the lists\' median, never the 42\'s; '
        'STRONG beyond the TOP-3 not the measured strategy, E6\'s +0,51 R against +0,80':
            all(k in ass for k in TRUST + ('рубеж 1 из 5', 'после закрытия 28.10.2027', 'после закрытия 31.10.2027', 'Форвард с 28.10',
                                           '★ STRONG вне ТОП-3 — те же условия', 'дал +0,51 R на сделку против +0,80 на трёх'))
            and '+0,22 R' in ass and '+0,04 R' in ass and '0,55' not in ass,
        'the bot\'s constants are this TZ\'s: 14 % a stop, 5 USDT, 0.1 % of the volume, 1 % and 5 % of risk, three places, 0.1 % a side, '
        'a list of 7, checks at 00:10 and 12:10 UTC, the rung 1, 1.1 s between parts, |z| 1 for STRONG':
            expect['consts'] == (STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, RISK_MAX, RISK_ALL, 3, 0.001, LIST_MAX, SLOTS, RUNG, PACE, STRONG_Z),
        'each allocation reply is the bot\'s own plan_parts of plan_strong over the report and liquidity it was made from':
            len(allocs) == 2 and all(whole(texts[c]) == whole(calc[c]['parts']) for c in allocs),
        'plan: the placed are the first n STRONG coins at any rank that pass the limits, the more the rest that pass, in rank order':
            ok_inv('the placed are the first n STRONG coins at any rank that pass the limits, the more the rest that pass, both in rank order'),
        'plan: every STRONG coin is placed, among the more or named with a reason, once':
            ok_inv('every STRONG coin is placed, among the more or named with a reason, once'),
        'plan: every trade has an entry and a stop within 14 % of it, on current prices':
            ok_inv('every trade has an entry and a stop within 14 % of it, on current prices'),
        'plan: each placed loss within 1 % of the budget and all within 5 %, each of the more within the average risk':
            ok_inv('each placed loss at its stop within 1 % of the budget and all within 5 %; each of the more within the average risk'),
        'plan: whole positions of at least 5 USDT, the placed together within the budget, free the budget less them':
            ok_inv('whole positions of at least 5 USDT, the placed together within the budget, free the budget less them'),
        'plan: leverage the rule\'s formula and at most 20, the margin covering the position, a position within its liquidity cap':
            ok_inv('leverage the rule\'s formula and at most 20, the margin covering the position, a position within its liquidity cap'),
        'the Boss\'s fields in each allocation reply - budget, count, allocated, free, for each trade capital, leverage, margin, loss, stop, '
        'targets, invalidation and its confidence with the note that the sizes are unproven, the more under their own heading with the '
        'loss of all together against 5 % - and no six ratings': len(allocs) == 2 and all(fields(c) for c in allocs),
        '«сигнал 15000 топ 5» places at most five, the other STRONG that pass among the more, and says nothing of three':
            c5 in calc and len(calc[c5]['plan']['items']) <= 5 and 'больше 3 сделок не будет' not in whole(texts[c5]),
        '«помощь» and an unknown text answer HELP and nothing else': texts[RENDER_CASES[5]] == [expect['help']] == texts[RENDER_CASES[6]],
        'the signal check: quiet exactly when it holds no alert, one line only where it finds nothing, else the close\'s TOP-3 and the '
        'STRONG beyond it, the candidates and the offered trades': sg is not None and run_shape(sg, 'signal'),
        'the fact check: quiet exactly when it holds no alert, one line where it finds neither an alert nor a zone left, no card but '
        'a new candidate\'s': fa is not None and run_shape(fa, 'fact'),
        'the alerts of both checks are the exits of the offered trades by this checker\'s own walk, each once, and the new candidates':
            sg is not None and fa is not None and alert_checks(sg, sg['cs'], sg['prev_passing']) and alert_checks(fa, fa['cs'], fa['prev_passing'])
            and not ({(a['kind'], a['coin'], a['side'], a['close_of']) for a in sg['rec']['alerts'] if a['kind'] != 'candidate'}
                     & {(a['kind'], a['coin'], a['side'], a['close_of']) for a in fa['rec']['alerts'] if a['kind'] != 'candidate'}),
        'the check records: their slots, every coin\'s state ranked, the six ratings, the coins that pass, the STRONG at every rank, the '
        'more, each card\'s extra': sg is not None and fa is not None and record_ok(sg, 'signal') and record_ok(fa, 'fact'),
        'the scratch journal holds, after the bot\'s own records, request, request, alloc, alloc, assess, check, check':
            kinds == RENDER_KINDS and all(r.get('cards') is not None for r in records),
        'the bot\'s own journal, offset, daily-sent and check-done are as before the run': same is True,
    }


def unit_checks(which, pre, now):
    """UNIT-NEW and UNIT-OLD's nine readings after a restart: now is what the modes read; pre is the snapshot of the kill mark, which
    names the check-done the new process must read at its start."""
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
        'the log shows the new process serving from check-done %s' % pre['read_done']: now['serving'] and now['read'] == pre['read_done'],
        'no traceback in the log since the mark': not now['traceback'],
        'the three capture units unchanged, each active': all(
            now['caps'][u]['ActiveState'] == 'active' and now['caps'][u]['MainPID'] == pre['caps'][u]['MainPID']
            and now['caps'][u]['NRestarts'] == pre['caps'][u]['NRestarts'] for u in CAPTURES),
    }


def first_checks(pre, recs, done_text, log, pid, tail_ok):
    """G-FIRST: the new process's first check - the day's signal check, replayed at its start because the kill mark set check-done
    to the slot before it - from the journal's records stamped after the kill mark, the check-done file and service.log's lines
    since the mark."""
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
        'it holds the 42 coins\' state, the six ratings, its alerts, the coins that pass, the STRONG at every rank and the more, each card '
        'its extra; quiet exactly without an alert': (
            len(r.get('state') or {}) == 42 and TRUST_KEYS <= set(r.get('trust') or {}) and isinstance(r.get('alerts'), list)
            and isinstance(r.get('passing'), list) and isinstance(r.get('strong_all'), list)
            and isinstance((r.get('alloc') or {}).get('more'), list) and all('extra' in c for c in r.get('cards') or [])
            and r.get('quiet') == (not r.get('alerts'))),
        'check-done names the slot it covers: %s' % want_done: done_text == want_done,
        'the log since the mark: the new process serving from check-done %s, the check sent, no check failed and no traceback' % pre['read_done']: (
            ('serving the pinned chat: pid %d ' % pid in log and 'check-done %s' % pre['read_done'] in log) and 'check sent: %s signal' % day in log
            and 'check failed' not in log and 'Traceback' not in log),
        'the journal ends in a newline and every line since the mark parses': tail_ok,
    }


def slot_instant(text):
    """The instant of a slot 'YYYY-MM-DD signal|fact' as epoch seconds, or None."""
    try:
        day, kind = text.split()
        at = dict(SLOTS)[kind]
        return calendar.timegm(dt.datetime.combine(dt.date.fromisoformat(day), at).timetuple())
    except (ValueError, KeyError, AttributeError):
        return None


def slot_order(text):
    day, kind = text.split()
    return day, [k for k, _ in SLOTS].index(kind)


def latest_slot_text(t):
    """The last slot whose instant is at or before the epoch second t, read here: 00:10 and 12:10 UTC."""
    d = dt.datetime.fromtimestamp(t, dt.timezone.utc)
    for kind, at in reversed(SLOTS):
        if d.time() >= at:
            return '%s %s' % (d.date(), kind)
    return '%s %s' % (d.date() - DAY, SLOTS[-1][0])


def replay_text(t):
    """The slot the kill mark writes to check-done: the one before the UTC day's signal check, the day before's fact - so that
    the new process's schedule owes, and runs at its start, the day's signal check."""
    return '%s %s' % (dt.datetime.fromtimestamp(t, dt.timezone.utc).date() - DAY, SLOTS[-1][0])


def clock_checks(recs, done_text):
    """H7, that the clock fires (map §2.7): the journal's check records from TZ-39's first name strictly later slots, each once;
    every one after TZ-39's first - at least one - stamped at or after its slot's instant; and check-done names the last one's slot,
    or that day's fact where the last is a signal check stamped at or after 12:10 UTC. (checks, the delays in seconds)."""
    checks_ = [r for r in recs if r.get('kind') == 'check']
    slots = [r.get('slot') for r in checks_]
    later = checks_[1:]
    delays = []
    for r in later:
        at = slot_instant(r.get('slot') or '')
        try:
            delays.append(dt.datetime.fromisoformat(r['utc']).timestamp() - at)
        except (KeyError, TypeError, ValueError):
            delays.append(None)
    last = checks_[-1] if checks_ else {}
    covered = None
    if last.get('slot', '').endswith(' signal'):
        day = last['slot'].split()[0]
        covered = '%s fact' % day if dt.datetime.fromisoformat(last['utc']).timestamp() >= slot_instant('%s fact' % day) else None
    ok_slots = all(slot_instant(x or '') is not None for x in slots)
    return {
        'H7 the check records from TZ-39\'s first, %s, name strictly later slots, each once' % TZ39_FIRST: (
            bool(slots) and slots[0] == TZ39_FIRST and ok_slots
            and all(slot_order(a) < slot_order(b) for a, b in zip(slots, slots[1:]))),
        'H7 every check after TZ-39\'s first - at least one - stamped at or after its slot\'s instant': (
            bool(later) and all(x is not None and x >= 0 for x in delays)),
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
    checks['H5 adv3.py and adv3-bot.py are TZ-39\'s'] = (
        sha256_file(SVC + '/adv3.py') == H['adv3_old'] and sha256_file(SVC + '/adv3-bot.py') == H['bot_old'])
    checks['H5 the installed unit file is TZ-35\'s'] = sha256_file('/etc/systemd/system/adv3-bot.service') == H['unit']
    checks['H5 commit.txt is 40 hex characters and a newline'] = re.fullmatch(r'[0-9a-f]{40}\n', read(SVC + '/commit.txt')) is not None
    jtext = read(BOTDIR + '/journal.jsonl')
    done_text = read(BOTDIR + '/check-done').strip() if os.path.exists(BOTDIR + '/check-done') else None
    checks['H6 the record holds a journal of whole lines and a check-done naming a slot'] = (
        jtext.endswith('\n') and done_text is not None and slot_instant(done_text) is not None)
    recs, _ok = records_since(jtext, 0)
    clock, delays = clock_checks(recs, done_text)
    checks.update(clock)
    out('check records: %d; slots %s; delays after their instants, seconds: %s; check-done %s' % (
        sum(r.get('kind') == 'check' for r in recs), ' '.join(r['slot'].replace(' signal', ' s').replace(' fact', ' f') for r in recs
                                                         if r.get('kind') == 'check' and isinstance(r.get('slot'), str)),
        ' '.join('-' if x is None else '%.0f' % x for x in delays), done_text or '-'))
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
    checks.update(tree_checks('adv3-bot.py', git_show('advisor/adv3-bot.py'), read(WT + '/advisor/adv3-bot.py'), BOT_DEFS, BOT_ASG, BOT_SAME))
    checks['the branch\'s adv3.py, adv3-bot.py and selftest-adv3.py are Appendix A\'s'] = (
        sha256_file(WT + '/advisor/adv3.py'), sha256_file(WT + '/advisor/adv3-bot.py'), sha256_file(WT + '/advisor/selftest-adv3.py')) == (
        H['adv3_new'], H['bot_new'], H['selftest_new'])
    verdict('RULE', checks)


def snapshot():
    """What a mark records: the instant, the bot's and the captures' units, the record's check count and lines, and check-done."""
    text = read(BOTDIR + '/journal.jsonl')
    return {'t': time.time(), 'bot': show(BOT, 'MainPID', 'NRestarts', 'ActiveState'),
            'caps': {u: show(u, 'MainPID', 'NRestarts', 'ActiveState') for u in CAPTURES},
            'checks': count_kind(text, 'check'), 'lines': text.count('\n'),
            'check_done': read(BOTDIR + '/check-done').strip() if os.path.exists(BOTDIR + '/check-done') else None}


def put_done(text):
    """check-done replaced in one rename, as the bot's own put writes it."""
    tmp = BOTDIR + '/check-done.tz40'
    with open(tmp, 'w', encoding='utf-8') as fh:
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, BOTDIR + '/check-done')


def mode_mark(name):
    """A mark: the snapshot, kept in state.json. kill refuses unless check-done names the latest slot - the running process owes no
    check - and then writes check-done to the slot before the UTC day's signal check, so that the new process replays that check
    at its start (G-FIRST); the old process holds its slot in memory and never reads the file again. rollback writes the kill mark's
    check-done back where the new process never moved it from the replay slot. kill2 writes nothing and records the check-done the
    old code will read at its start, a slot it may owe and run then."""
    assert name in ('deploy', 'kill', 'rollback', 'kill2'), name
    st = load_state()
    snap = snapshot()
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
    out('mark %s at %s: bot pid %s NRestarts %s, %d check records, check-done %s%s' % (
        name, time.strftime('%FT%TZ', time.gmtime(snap['t'])), snap['bot']['MainPID'], snap['bot']['NRestarts'], snap['checks'],
        snap['check_done'] or '-', (' -> %s, replayed by the new process at its start' % snap['read_done']) if name == 'kill'
        else (' -> restored to %s' % st['marks']['kill']['check_done']) if snap.get('restored') else ''))


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


def line_count(path):
    """The lines of a file, read one at a time: a year's journal is never held whole."""
    with open(path, encoding='utf-8') as fh:
        return sum(1 for _line in fh)


def lines_after(path, k):
    """The records of a journal's lines after its first k, each parsed, read one at a time."""
    with open(path, encoding='utf-8') as fh:
        return [json.loads(line) for n, line in enumerate(fh) if n >= k]


def render_run(mod, data, now):
    """G-RENDER's pipeline on a loaded bot and a Data: the commands answered through the bot's handle, then the signal check and
    the fact check through its check, each appended to its STATE's journal; Telegram a stand-in, the reports, volumes and forming
    candles the bot read captured - the list commands' reports kept in calc['lists'] - and each allocation's plan recomputed by the
    bot's plan_strong from the very report and volumes its reply was made from. (texts, calc, runs, records, log, expect)."""
    base_lines = line_count(mod.STATE + '/journal.jsonl')

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
                if cmd and cmd[0] == 'signal' and len(seen) == m0 + 1:
                    calc.setdefault('lists', {})[case] = seen[-1]
                if cmd and cmd[0] == 'alloc' and len(seen) == m0 + 1:
                    _k, budget, n, risk = cmd
                    rep = mod.top_n(seen[-1], mod.adv3.TOP_N)
                    p = mod.plan_strong(rep, data.cs, budget, n, risk, dict(liqs))
                    calc[case] = {'rep': rep, 'liq': dict(liqs), 'plan': p, 'budget': budget, 'n': n, 'risk': risk,
                                  'parts': mod.plan_parts(rep, p)}
            for kind in ('signal', 'fact'):
                scan = mod.journal_scan()
                n0, m0 = len(cap.sent), len(seen)
                liqs.clear()
                formed.clear()
                rec = mod.check(cap, data, (now.date(), kind), now)
                mod.append(rec)
                rep = mod.top_n(seen[m0], mod.adv3.TOP_N)
                p = mod.plan_strong(rep, data.cs, mod.adv3.DEPOSIT, mod.adv3.TOP_N, mod.adv3.RISK, dict(liqs))
                prev, rows = scan[2], rep['rows']
                runs[kind] = {'rec': rec, 'sent': cap.sent[n0:], 'scan': scan, 'rep': rep, 'plan': p, 'forming': dict(formed),
                              'last': dt.date.fromisoformat(rep['close_of']), 'cs': data.cs,
                              'prev_passing': {(c, s) for c, s in (prev or {}).get('passing') or []},
                              'changes': any(rows[c].get('signal') != rows[c].get('prev')
                                             and (rows[c].get('signal') in (1, -1) or rows[c].get('prev') in (1, -1)) for c in mod.adv3.COINS),
                              'same': prev is not None and prev.get('top') == rep['top'] and prev.get('strong') == rep['strong']
                              and all((prev.get('signals') or {}).get(c) == rows[c].get('signal') for c in rep['top'])
                              and isinstance(prev.get('strong_all'), list)
                              and sorted(prev['strong_all']) == sorted(own_strong(rows, own_order(rows, list(rows))))}
    finally:
        mod.live_report, mod.liquidity, mod.forming_candles = real_lr, real_liq, real_form
    records = lines_after(mod.STATE + '/journal.jsonl', base_lines)
    m = mod.adv3
    expect = {'help': mod.HELP, 'usdt': m.usdt, 'num': m.num,
              'consts': (mod.STOP_MAX, mod.MIN_NOTIONAL, mod.LIQ_FRAC, m.RISK_MAX, m.RISK_ALL, m.TOP_N, m.COST, mod.LIST_MAX, mod.SLOTS,
                         m.RELIABILITY, mod.PACE, m.STRONG_Z)}
    return texts, calc, runs, records, buf.getvalue(), expect


def render_print(texts, calc, runs, log):
    """What G-RENDER prints: sizes, counts and labels, never a coin, a price or a size."""
    lists = calc.get('lists') or {}
    strong = {c: len(own_strong(r['rows'], own_order(r['rows'], list(r['rows'])))) for c, r in lists.items()}
    allocs = [c for c in RENDER_CASES if c in calc]
    out('replies: %s; the bot\'s log: %d lines; STRONG at every rank: %s; per allocation, placed and more: %s' % (
        ', '.join('%d chars in %d parts' % (sum(map(len, texts[k])), len(texts[k])) for k in RENDER_CASES), log.count('\n'),
        ', '.join(str(v) for v in strong.values()) or '-',
        ', '.join('%d and %d' % (len(calc[c]['plan']['items']), len(calc[c]['plan'].get('more') or [])) for c in allocs)))
    for kind, r in runs.items():
        rec = r['rec']
        out('%s check: %s, %s, %d parts; alerts %s; offers read %d, followed %d; cards %d, of them extra %d; passing %d; STRONG at every '
            'rank %d; zones left %d; forming candles read %d' % (
                kind, 'quiet' if rec['quiet'] else 'loud', 'one line' if rec['one_line'] else 'full', len(r['sent']),
                json.dumps({k: sum(a['kind'] == k for a in rec['alerts']) for k in ('stop', 'signal', 'candidate')}, sort_keys=True),
                len(r['scan'][0]), len(rec['followed']), len(rec['cards']), sum(bool(c.get('extra')) for c in rec['cards']),
                len(rec['passing']), len(rec.get('strong_all') or []), len(rec['zones_left']), len(r['forming'])))


def mode_render():
    """G-RENDER: the service copy's bot answers the commands and runs both checks on live data, its Telegram a stand-in, its
    STATE a scratch directory holding a copy of the bot's own journal, so the trades its cards offered are the real ones. Its
    process's peak resident set and its time are printed (map §7 item 145): the mode is its own wrapper."""
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
    texts, calc, runs, records, log, expect = render_run(mod, mod.Data(), dt.datetime.now(dt.timezone.utc))
    same = own == own_files()
    render_print(texts, calc, runs, log)
    import resource
    out('PEAK %d bytes resident; %.2f s of wall, %.2f s of processor' % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024,
                                                                       time.time() - t0, time.process_time() - c0))
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
    out('first check: %s, %s, %d messages; alerts %s; followed %d; cards %d, of them extra %d; passing %d; STRONG at every rank %d; '
        'check-done %s' % (
            'quiet' if r.get('quiet') else 'loud', 'one line' if r.get('one_line') else 'full', len(r.get('message_ids') or []),
            json.dumps({k: sum(a.get('kind') == k for a in r.get('alerts') or []) for k in ('stop', 'signal', 'candidate')}, sort_keys=True),
            len(r.get('followed') or []), len(r.get('cards') or []), sum(bool(c.get('extra')) for c in r.get('cards') or []),
            len(r.get('passing') or []), len(r.get('strong_all') or []), done_text or '-'))
    verdict('FIRST', first_checks(pre, recs, done_text, text, pid, tail_ok))


def kept_files():
    """The work tree's files a report keeps by name: state.json, the three files B-DEPLOY saves, and every file under logs/;
    relative to WORK, sorted."""
    names = ['state.json', 'adv3.before', 'bot.before', 'commit.before']
    for d, _s, fs in os.walk(WORK + '/logs'):
        names += [os.path.relpath(os.path.join(d, f), WORK) for f in fs]
    return sorted(n for n in names if os.path.isfile(os.path.join(WORK, n)))


def mode_keep():
    """B-RECLAIM-OWN's copy: every kept file into the forensic store as tz40-work--<path with - for />, by exclusive create and
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
        dest = FORENSICS + '/tz40-work--' + rel.replace('/', '--')
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
           '#### E6 — STRONG with 3, 5 and 7 places\n\n| field | top3 | top5 | top7 |\n|---|---|---|---|\n| `trades` | 265 | 449 | 620 |\n'
           '| `mean_R` | 0.7962 | 0.5491 | 0.5084 |\n\n| variant | bucket | trades |\n|---|---|---|\n| top3 | `1-3` | 265 |\n\n'
           '#### The sets and the frozen FACTS\n\n| `G` | 570 |\n')
    want = {'base': {'mfe': {1: 0.2318, 2: 0.1257, 3: 0.0759}, 'mean_R_G': 0.0403, 'trades_G': 19002, 'p_G': 0.0735, 'contracts_G': 570},
            'strong': {'mfe': {1: 0.4717, 2: 0.2906, 3: 0.1887}, 'p_G': 0.11, 'mean_R_lists': 0.2195, 'lists': 500, 'lists_positive': 0.86,
                       'top5_share': 0.9875, 'mean_R_P3': 0.7962, 'mean_R_P7': 0.5084}}
    ok(pit_from_report(rpt) == want, 'pit_from_report: every figure read from its section and row, E6\'s three places and seven among them')
    ok(pit_from_report(rpt.replace('| 0.5 | 37.7116 | 0.2195 |', '| 0.5 | 37.7116 | 0.2196 |')) != want
       and pit_from_report(rpt.replace('| 0.7962 | 0.5491 | 0.5084 |', '| 0.7962 | 0.5491 | 0.5085 |')) != want,
       'pit_from_report: a changed cell, E5\'s or E6\'s, reads another PIT')
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
    rows_o = {'A': {'signal': 1, 'z': 2.0, 'sum': 4, 'U': 1.0}, 'B': {'signal': -1, 'z': -3.0, 'sum': -4, 'U': 1.0},
              'C': {'signal': 1, 'z': 2.0, 'sum': 2, 'U': 1.0}, 'D': {'signal': 0, 'z': 9.0, 'sum': 0, 'U': 1.0},
              'E': {'signal': 1, 'z': 0.9, 'sum': 4, 'U': 1.0}, 'F': {'signal': -1, 'z': None, 'sum': None, 'U': 1.0}, 'G': {'signal': None}}
    ord_o = own_order(rows_o, list(rows_o))
    ok(ord_o == ['B', 'A', 'C', 'E'] and own_strong(rows_o, ord_o) == ['B', 'A'],
       'own_order and own_strong: by |z| with ties in the coins\' order, out of the market and without a strength left out; STRONG four '
       'agreeing signs and |z| at least 1')
    r_l = {'signal': 1, 'close': 100.0, 'U': 8.0}
    ok(abs(own_stop_pct(dict(r_l, mark=101.0)) - 100 * 9 / 101) < 1e-12 and abs(own_stop_pct(dict(r_l, mark=103.0)) - 100 * 10 / 102) < 1e-12
       and own_stop_pct(dict(r_l, mark=93.5)) is None and abs(own_stop_pct(dict(r_l, mark=97.0)) - 100 * 5 / 97) < 1e-12
       and abs(own_stop_pct(dict(r_l, signal=-1, mark=97.0)) - 100 * 10 / 98) < 1e-12 and abs(own_stop_pct(dict(r_l, mark=None)) - 8.0) < 1e-12,
       'own_stop_pct: at market inside the zone, a limit at its top above it, none near the stop, at market below the zone clear of it; '
       'a short mirrored; no mark, the close')
    t_k = calendar.timegm(time.strptime('2026-11-03T09:00:00', '%Y-%m-%dT%H:%M:%S'))
    ok([latest_slot_text(t_k), latest_slot_text(t_k + 4 * 3600), latest_slot_text(t_k - 9 * 3600 + 1), replay_text(t_k), replay_text(t_k + 6 * 3600)]
       == ['2026-11-03 signal', '2026-11-03 fact', '2026-11-02 fact', '2026-11-02 fact', '2026-11-02 fact'],
       'latest_slot_text and replay_text: 09:00 the day\'s signal, 13:00 its fact, 00:00:01 the day before\'s fact; the replay the day before\'s fact')
    srv = ('2026-11-03T09:01:00Z serving the pinned chat: pid 11 offset 9 check-done 2026-11-02 fact\n'
           '2026-11-03T09:01:01Z serving the pinned chat: pid 12 offset 9 check-done -')
    ok(served_from(srv, 11) == '2026-11-02 fact' and served_from(srv, 12) == '-' and served_from(srv, 13) is None,
       'served_from: the check-done a process logged at its start, \'-\' for none, None for a pid that did not serve')
    mk = lambda slot, utc: {'kind': 'check', 'slot': slot, 'utc': utc}
    good_c = [{'kind': 'daily', 'utc': '2026-11-01T06:00:00+00:00'}, mk('2026-11-01 signal', '2026-11-01T06:51:46+00:00'),
              mk('2026-11-01 fact', '2026-11-01T12:10:09+00:00'), mk('2026-11-02 signal', '2026-11-02T00:10:12+00:00'),
              {'kind': 'request', 'utc': '2026-11-02T08:00:00+00:00'}, mk('2026-11-02 fact', '2026-11-02T12:15:30+00:00')]
    ck_, dl_ = clock_checks(good_c, '2026-11-02 fact')
    ok(all(ck_.values()) and len(ck_) == 3 and [round(x) for x in dl_] == [9, 12, 330],
       'clock_checks: TZ-39\'s first, then slots each once, each stamped after its instant - a retry\'s 330 s among them - and check-done '
       'the last: 3 of 3')
    covered = good_c[:4] + [mk('2026-11-03 signal', '2026-11-03T12:20:00+00:00')]
    ok(all(clock_checks(covered, '2026-11-03 fact')[0].values()) and all(clock_checks(covered, '2026-11-03 signal')[0].values()),
       'clock_checks: a signal check that ended after 12:10 covers its day\'s fact in check-done')
    for label, recs_, done_ in (('a slot twice', good_c + [mk('2026-11-02 fact', '2026-11-02T12:20:00+00:00')], '2026-11-02 fact'),
                                ('a check stamped before its slot', good_c[:3] + [mk('2026-11-02 signal', '2026-11-02T00:09:00+00:00')], '2026-11-02 signal'),
                                ('no check after TZ-39\'s first', good_c[:2], '2026-11-01 signal'),
                                ('another first', good_c[2:], '2026-11-02 fact'),
                                ('a check-done not the last', good_c, '2026-11-02 signal'),
                                ('no check-done', good_c, None)):
        ok(not all(clock_checks(recs_, done_)[0].values()), 'clock_checks: %s reads FAIL' % label)
    pre = {'t': 1000.0, 'bot': {'MainPID': '10', 'NRestarts': '2'}, 'read_done': '2026-11-02 fact',
           'caps': {u: {'MainPID': str(i), 'NRestarts': '0', 'ActiveState': 'active'} for i, u in enumerate(CAPTURES, 20)}}
    now = {'bot': {'MainPID': '11', 'NRestarts': '3', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'enabled'},
           'caps': dict(pre['caps']), 'start': 1035.0, 'copy_t': 990.0, 'argv': ARGV, 'procs': [11], 'sha_adv3': H['adv3_new'],
           'sha_bot': H['bot_new'], 'sha_unit': H['unit'], 'serving': True, 'read': '2026-11-02 fact', 'traceback': False}
    ok(all(unit_checks('new', pre, now).values()) and len(unit_checks('new', pre, now)) == 9, 'unit_checks: a clean restart reads 9 of 9')
    for key, val, label in (('read', '2026-11-03 signal', 'a process that read another check-done'), ('start', 1200.0, 'a process started 200 s after the kill'),
                            ('sha_bot', H['bot_old'], 'the old bot'), ('sha_adv3', H['adv3_old'], 'the old adv3.py'),
                            ('traceback', True, 'a traceback since the mark'), ('procs', [11, 12], 'a second process under the argv'),
                            ('serving', False, 'no serving line of the new pid')):
        ok(not all(unit_checks('new', pre, dict(now, **{key: val})).values()), 'unit_checks: %s reads FAIL' % label)
    moved = {u: dict(cc, NRestarts='1') for u, cc in pre['caps'].items()}
    ok(not all(unit_checks('new', pre, dict(now, caps=moved)).values()), 'unit_checks: a capture unit restarted reads FAIL')
    ok(all(unit_checks('old', pre, dict(now, sha_bot=H['bot_old'], sha_adv3=H['adv3_old'])).values()), 'unit_checks: the rollback reads the old files')
    t0 = calendar.timegm(time.strptime('2026-11-02T14:00:00', '%Y-%m-%dT%H:%M:%S'))
    pre_f = dict(pre, t=float(t0), read_done='2026-11-01 fact')
    rec = {'utc': '2026-11-02T14:00:50+00:00', 'kind': 'check', 'slot': '2026-11-02 signal', 'close_of': '2026-11-01', 'rule': H['rule'],
           'message_ids': [5, 6], 'state': {str(k): {} for k in range(42)}, 'trust': {k: 0 for k in TRUST_KEYS}, 'alerts': [], 'passing': [],
           'strong_all': [], 'alloc': {'more': []}, 'cards': [{'coin': 'BTC', 'extra': False}], 'quiet': True}
    log_f = ('2026-11-02T14:00:35Z serving the pinned chat: pid 11 offset 9 check-done 2026-11-01 fact\n'
             '2026-11-02T14:00:50Z check sent: 2026-11-02 signal for the close of 2026-11-01 | alerts 0 | quiet | full')
    good = first_checks(pre_f, [rec], '2026-11-02 fact', log_f, 11, True)
    ok(all(good.values()) and len(good) == 7, 'first_checks: the replayed signal check after a 14:00 restart reads 7 of 7, check-done covering 12:10')
    ok(all(first_checks(dict(pre_f, t=float(t0 - 4 * 3600)), [rec], '2026-11-02 signal', log_f.replace('14:00:35', '10:00:35'), 11, True).values()),
       'first_checks: a 10:00 restart wants check-done at the signal slot')
    for label, args in (('no check record', ([], '2026-11-02 fact', log_f, 11, True)),
                        ('two check records', ([rec, rec], '2026-11-02 fact', log_f, 11, True)),
                        ('another slot', ([dict(rec, slot='2026-11-02 fact')], '2026-11-02 fact', log_f, 11, True)),
                        ('no message ids', ([dict(rec, message_ids=[])], '2026-11-02 fact', log_f, 11, True)),
                        ('a loud check without an alert', ([dict(rec, quiet=False)], '2026-11-02 fact', log_f, 11, True)),
                        ('a record without the STRONG at every rank', ([{k: v for k, v in rec.items() if k != 'strong_all'}], '2026-11-02 fact', log_f, 11, True)),
                        ('a card without its extra', ([dict(rec, cards=[{'coin': 'BTC'}])], '2026-11-02 fact', log_f, 11, True)),
                        ('check-done at the signal after 12:10', ([rec], '2026-11-02 signal', log_f, 11, True)),
                        ('a failed check in the log', ([rec], '2026-11-02 fact', log_f + '\ncheck failed: x', 11, True)),
                        ('a start from another check-done', ([rec], '2026-11-02 fact', log_f.replace('check-done 2026-11-01 fact', 'check-done -'), 11, True)),
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
    ok(all(number_reading([TZ_FILE, 'CryptoTZ/TZ-39-x.md']).values()), 'number: the one file reads PASS')
    ok(not all(number_reading([TZ_FILE, 'CryptoTZ/TZ-40-other.md']).values()) and not all(number_reading([TZ_FILE, 'CryptoReports/TZ-40-x-report.md']).values()),
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
            time.sleep = real_sleep
    kinds = [r['kind'] for r in records]
    args = dict(texts=texts, calc=calc, runs=runs, kinds=kinds, records=records, log=blog, same=True, expect=expect)
    good = render_checks(**args)
    al = {k: [(x['kind'], x['touch']) for x in runs[k]['rec']['alerts']] for k in runs}
    ok(all(good.values()) and len(good) == 22, 'render_checks: the stage\'s bot on a synthetic market reads 22 of 22 - %s' % [k for k, v in good.items() if not v])
    ok(('stop', False) in al['signal'] and ('signal', False) in al['signal'] and ('candidate', False) in al['signal'] and al['fact'] == [('stop', True)],
       'the synthetic market meets every alert: a stop on a closed candle, an exit by signal and new candidates at the signal check, a forming candle '
       'through a stop at the fact check')
    c3 = RENDER_CASES[2]
    ok(len(calc[c3]['plan']['items']) == 3 and len(calc[c3]['plan']['more']) == 9 and EXTRA_HEAD in '\n'.join(texts[RENDER_CASES[0]])
       and len(runs['signal']['rec']['cards']) == 12 and sum(c['extra'] for c in runs['signal']['rec']['cards']) == 9,
       'the synthetic market shows STRONG at every rank: twelve STRONG, the default allocation three placed and nine more, «сигнал» '
       'and the signal check nine extra cards')

    def bad(**kw):
        a_ = dict(args)
        a_.update(kw)
        return not all(render_checks(**a_).values())

    sig, top7 = texts[RENDER_CASES[0]], texts[RENDER_CASES[1]]
    sig_t = '\n'.join(sig)
    ok(bad(log='Traceback (most recent call last):') and bad(log='check failed: x'), 'render_checks: a traceback or a failure in the bot\'s log reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[0]: []})), 'render_checks: a command with no answer reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[5]: ['<b>HELP']})), 'render_checks: unbalanced markup reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[0]: [sig_t + '\nОценка доверия']})), 'render_checks: a «сигнал» carrying the six ratings reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[0]: [re.sub(CONF, 'X: ', sig_t, count=1)]})), 'render_checks: a card without its confidence reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[0]: [sig_t.replace('Уверенность: <b>1/5</b>', 'Уверенность: <b>3/5</b>', 1)]})),
       'render_checks: a confidence that is not the rung reads FAIL')
    cut = sig_t[:sig_t.index(EXTRA_HEAD)] + sig_t[sig_t.index('<b>Остальные сигналы</b>'):]
    ok(bad(texts=dict(texts, **{RENDER_CASES[0]: [cut]})), 'render_checks: a «сигнал» without its STRONG beyond the TOP-3 reads FAIL')
    untag = sig_t.replace(TAG + '\n', '\n', 1)
    ok(untag != sig_t and bad(texts=dict(texts, **{RENDER_CASES[0]: [untag]})), 'render_checks: a STRONG card beyond the TOP-3 without its tag reads FAIL')
    unstar = re.sub(r'(?m)^([🟢🔴] <b>[A-Z0-9]+ · (?:LONG|SHORT)</b>) · ★ STRONG$', r'\1', '\n'.join(top7), count=1)
    ok(unstar != '\n'.join(top7) and bad(texts=dict(texts, **{RENDER_CASES[1]: [unstar]})), 'render_checks: a STRONG card of the list without its ★ reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[4]: [texts[RENDER_CASES[4]][0].replace('+0,22 R', '+0,55 R')]}))
       and bad(texts=dict(texts, **{RENDER_CASES[4]: [texts[RENDER_CASES[4]][0].replace('дал +0,51 R', 'дал +0,61 R')]})),
       'render_checks: an assessment quoting the 42\'s STRONG figure, or another E6 figure, reads FAIL')
    ok(bad(expect=dict(expect, consts=(11.1,) + expect['consts'][1:])) and bad(expect=dict(expect, consts=expect['consts'][:7] + (10,) + expect['consts'][8:]))
       and bad(expect=dict(expect, consts=expect['consts'][:10] + (0.0,) + expect['consts'][11:])),
       'render_checks: another stop limit, another list length or no pause between parts reads FAIL')
    ok(bad(texts=dict(texts, **{c3: [calc[c3]['parts'][0] + ' ']})), 'render_checks: an allocation reply that is not the plan\'s own reads FAIL')
    p = calc[c3]['plan']
    worse = dict(p, items=[dict(p['items'][0], card=dict(p['items'][0]['card'], stop_pct=14.5))] + p['items'][1:])
    ok(bad(calc=dict(calc, **{c3: dict(calc[c3], plan=worse)})), 'render_checks: a stop beyond 14 % in a plan reads FAIL')
    heavy = dict(p, items=[dict(p['items'][0], loss_exact=p['budget'] * 0.0101)] + p['items'][1:])
    ok(bad(calc=dict(calc, **{c3: dict(calc[c3], plan=heavy)})), 'render_checks: a loss at a stop beyond 1 % of the budget reads FAIL')
    fat = dict(p, more=[dict(p['more'][0], loss_exact=p['budget'] * p['risk'] / 100 * 1.01)] + p['more'][1:])
    ok(bad(calc=dict(calc, **{c3: dict(calc[c3], plan=fat)})), 'render_checks: one of the more beyond the average risk reads FAIL')
    lost = dict(p, more=p['more'][1:])
    ok(bad(calc=dict(calc, **{c3: dict(calc[c3], plan=lost)})), 'render_checks: a STRONG coin that passes and is neither placed nor among the more reads FAIL')
    swapped = dict(p, items=p['items'][:2] + p['more'][:1], more=p['items'][2:] + p['more'][1:])
    ok(bad(calc=dict(calc, **{c3: dict(calc[c3], plan=swapped)})), 'render_checks: a coin beyond the first n placed before one within them reads FAIL')
    sg = runs['signal']
    flipped = dict(sg, rec=dict(sg['rec'], quiet=not sg['rec']['quiet']))
    ok(bad(runs=dict(runs, signal=flipped)), 'render_checks: a check whose quiet flag disagrees with its alerts reads FAIL')
    dropped = dict(sg, rec=dict(sg['rec'], alerts=[a for a in sg['rec']['alerts'] if a['kind'] != 'signal']))
    ok(bad(runs=dict(runs, signal=dropped)), 'render_checks: an exit the walk finds and the check does not alert reads FAIL')
    fa = runs['fact']
    again = dict(fa, rec=dict(fa['rec'], alerts=fa['rec']['alerts'] + [a for a in sg['rec']['alerts'] if a['kind'] == 'stop']))
    ok(bad(runs=dict(runs, fact=again)), 'render_checks: an alert sent twice across the checks reads FAIL')
    ok(bad(runs=dict(runs, fact=dict(fa, rec=dict(fa['rec'], cards=list(sg['rec']['cards']))))), 'render_checks: a fact check offering the close\'s cards reads FAIL')
    ok(bad(runs=dict(runs, signal=dict(sg, rec=dict(sg['rec'], strong_all=sg['rec']['strong_all'][:-1])))),
       'render_checks: a check record whose STRONG at every rank is not the checker\'s reads FAIL')
    ok(bad(kinds=kinds[:-1]) and bad(kinds=['check'] + kinds[1:]), 'render_checks: a journal that lacks a record or has another kind reads FAIL')
    ok(bad(same=False), 'render_checks: the bot\'s own record changed reads FAIL')
    out('SELFTEST PASS: %d of %d checks passed' % (len(done), len(done)))


def main(argv):
    if not argv:
        sys.exit('usage: tz40-advisor-strong.py MODE [ARG]')
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
