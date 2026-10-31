# TZ-38 — the rule on contracts the Boss did not pick: ADV-3 run unchanged on every Binance USDⓈ-M USDT perpetual that traded, an entry allowed only where the contract was liquid before the day

**Canonical filename:** `TZ-38-adv3-pit-validation.md`. The committed file takes this name and no other.

**Executor model: Claude Opus 5.5.** It fetches about 66,700 files from a public archive and runs the advisor's frozen functions over 612 contracts, with gate arithmetic and a bootstrap among the readings.

**Required System Map revision:** `2026-10-31-b`.

**Required anchors**, from map §0. A mismatch on any one is BLOCKED before any work:

| anchor | required |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `0f6c90451cbd` |
| `A6` — pricer | `729f0bcdbee3` |

**Host gate:** §0.3. This TZ runs on the capture host because the Executor does. It touches no capture, no unit and no file of the advisor, and it reads the public archive alone.

**Before `EXECUTE TZ-38`:** the Boss uploads this file alone, into `CryptoTZ/`. `main` already carries map `2026-10-31-b` (`133d57f`) and PR #37 is merged; nothing else is needed.

**When:** any time after the upload, while `/dev/vda2` holds at least `7,700,000,000` bytes free and `MemAvailable` at least `122,462,208` (§0.4). **§3.5 to §3.7, the fetch and the two runs, wait for 06:35:00 to 20:30:00 UTC** (§3.5 gives the wait), clear of the package manager's morning runs and of both archives' calendar runs, the reward book's at 01:30:20 and the pair book's at 03:00:20 (map §2.5 and §2.6). This TZ reloads systemd **never**, so it sets off no run of either archive (map §7 items 125 and 129). About 2 hours of wall clock (§6).

**What this TZ is.** On 2026-10-31 the Boss asked for the advisor's signals to be as accurate as they can be made and for its confidence to rise above 1 of 5 by evidence only. Every number behind that 1 of 5 comes from his 42 coins, a list he made in 2026. This TZ runs the frozen rule, unchanged, on every contract the archive holds — 895 USDⓈ-M USDT perpetuals, 31 of them delisted — letting a contract open a trade only on a day when the median quote volume of its 28 candles before the day was 10,000,000 USDT or more, and measures what his list cannot: how the rule does outside the list, and how much of STRONG's displayed edge is the list. It adds no rule, changes no parameter, deploys nothing and publishes nothing. It writes one file, `research/tz38-adv3-pit-validation.py`, and runs it.

**It moves no rung, and the reason is the Architect's defect.** CANON PART II fixes a gate before any score exists. The Architect ran this instrument over the full store, in rehearsal, on 2026-10-31, before this TZ was written, and printed the reading of the rule on the contracts outside the Boss's 42. That reading is the Architect's exploration, in sample and barred (CANON PART VI), whatever this run prints; the same rehearsal printed the other tables. The run is still worth making, and §4 says what it buys: the numbers become the host's, from the archive's own bytes and a manifest of every file, and the Architect's verdict compares them with the rehearsal's to the last digit — a difference is a finding. What can move a rung is the PIT record (CANON PART VII), which starts at the close of 2026-10-28 and is read after 2027-10-28, on data nobody had read. The SHA-256 of every file the rehearsal wrote are in §4.6, committed here before the Executor's run.

---

## 0. Gates

### 0.0 The work tree, first

After contract §1 steps 1 and 2, and before anything else:

```
mkdir /root/tz38-work /root/tz38-work/logs; echo "exit=$?"
```

`exit=0` proves neither existed; anything else is BLOCKED. **From here every command's output goes to `/root/tz38-work/logs/`, one file per step, `NN-<step>.log` in this TZ's order**, and nothing to the session's scratchpad. The one exception is B-RECLAIM-OWN, §9, which removes the directory the logs are in.

Two abbreviations: **`P`** is `nice -n 19 /root/tz04a-env/venv/bin/python -B`, and **`I`** is `P /root/tz38-work/stage/research/tz38-adv3-pit-validation.py`. **In every block that removes a tree, `I` is written out in full**, because the Boss may be handed the block (map §6, sandbox limit).

### 0.1 The file, staged

Extract Appendix A from this TZ as the primary checkout carries it after contract §1's pull, with this script, verbatim, its one argument the destination:

```
/root/tz04a-env/venv/bin/python -B - /root/tz38-work/stage <<'EOF'
import hashlib, os, sys
SRC = "/root/btc-5m-twap/CryptoTZ/TZ-38-adv3-pit-validation.md"
DEST = sys.argv[1]
WANT = {
    "research/tz38-adv3-pit-validation.py": "579474b65329662f7bed735994381241a928a2c65a726cec3f933dc7afd4427b",
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
| `research/tz38-adv3-pit-validation.py` | 1782 | 90,181 | `579474b65329662f7bed735994381241a928a2c65a726cec3f933dc7afd4427b` |

A failed assert is BLOCKED. The script creates the file by exclusive create (`xb`); over a non-empty destination it fails.

### 0.2 Fingerprint

`I fingerprint` performs contract §1 steps 3 and 4 against `SYSTEM-MAP.md` and the files of its §0 table in the primary checkout `/root/btc-5m-twap`, and asserts them: revision `2026-10-31-b`; the six anchors, `A2`, `A4`, `A5` and `A6` re-derived as the first 12 hex characters of those files' SHA-256; the table's **57** rows, each printed in lines, bytes and SHA-256 — **54** `frozen` rows asserted equal to the map, **2** `tracked` and **1** `reported`; and that `advisor/adv3.py` hashes to the SHA-256 the instrument loads it by. It prints `READING FINGERPRINT: PASS - 67 of 67` — 1 revision, 6 anchors, 4 re-derived, 54 rows, 1 shape, 1 loader — or fails at the first mismatch, which is BLOCKED.

### 0.3 Host gate

From `/root/btc-5m-twap`, with `S` first set to the scratchpad directory the session's system prompt names:

```
date -u; date -u +%s; uptime -s
nproc; grep -E '^(MemTotal|MemAvailable|SwapTotal|SwapFree):' /proc/meminfo
I host
TZ=UTC systemctl list-timers btc-pairbook-archive.timer btc-rewardbook-archive.timer apt-daily-upgrade.timer apt-daily.timer --all --no-pager
du -sb /var/lib/btc-rewardbook /var/lib/btc-pairbook /var/lib/adv3-bot /root/.claude
find /root/btc-forensics -type f | wc -l
git worktree list
echo "$S"; ls -la "$(dirname "$(dirname "$S")")"
```

`I host` asserts these eleven, prints each check beside the units' readings and the memory and disk figures, and prints `READING HOST: PASS - 11 of 11`, or fails:

- **H1** — `find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit` prints one path.
- **H2** — `df` names source `/dev/vda2` and size `31612203008`; `grep -c e3975b5da44c5328adf3bf3914634cd878842c73 /var/lib/btc-recorder/runtime.jsonl` prints at least `1` — two checks. With H1 this is map §6's host identity.
- **H3** — `/root/tz04a-env/venv/bin/python` prints `3.12.`: the interpreter this TZ runs under.
- **H4** — `btc-recorder.service`, `btc-pairbook.service` and `btc-rewardbook.service` each read `ActiveState=active` and `UnitFileState=enabled` — three checks: STILL compares them, later, against the mark.
- **H5** — `adv3-bot.service` reads `active`, `running`, `enabled`.
- **H6** — `/root/tz38-work` holds nothing but `logs/` and `stage/`.
- **Memory gate** — `MemAvailable` at least `122,462,208` bytes (§0.4); **where the first read is below it, `I host` reads again after 60 s and the second read decides**. **Disk gate** — `/dev/vda2` free at least `7,700,000,000` bytes (§0.4).

Any one failing is BLOCKED. **The rest is printed and carries no threshold:** the timers; `du` of the capture roots and the Claude directory; the forensic store's count, map §3's `2,267`; the worktrees, map §3's two; and the listing of the directory that holds the session's own scratch, whose UUID directories §3.3 names live or earlier. Map §3 records the two TZ-37's session left, `f13dd443-b053-5e1f-ab49-f3593ec7b06b` and `50f7dcda-5a03-4e54-8f23-a03fd054d0b0`, and one live `claude` session of 2026-10-30 that is no TZ's, `238335b9-cf23-414a-8e8f-ad4705c4d19e`.

### 0.4 Resource floors, in exact bytes

**Disk.** `/dev/vda2` free at least **`7,700,000,000`** bytes: the reward book's `STREAM_FLOOR`, `7,300,000,000`, below which no stream of it opens (map §2.6; `research/tz33-reward-book-capture.py` line 190), plus `400,000,000` for this session at its upper bound. The Architect measured the store on 2026-10-31: 66,677 files of 67,600,876 bytes, `291,500,032` bytes on disk at 4 KiB blocks; add the arena, `41,000,000` bytes while it is written and none once the file is unlinked, the plan and the manifest, `14,300,000`, the two output directories, `5,000,000`, the logs and the forensic copies, `20,000,000` — `371,800,032`, under the `400,000,000`. **This TZ never takes free space below the floor that pauses the reward book.**

**Memory.** `MemAvailable` at least **`122,462,208`** bytes: twice `61,231,104`. Map §7 item 131's rule is that a floor is twice the largest peak among the modes the TZ runs. The peak the instrument reads is its **anonymous set** — `RssAnon` of `/proc/self/status`, sampled every 0.05 s by a thread of its own — because the prices of every contract live in one file the process maps read-only, pages the system can take back; the resident set the run reaches holds `54,206,464` bytes of them at its high-water mark. The Architect measured `run` five times on 2026-10-31: `61,231,104` (Python 3.13.18, the code before it dropped the plan's keys), `54,951,936` and `55,914,496` (3.12.3, the code before its last edit) and, on the bytes of §0.1's table under Python 3.12.3, `57,004,032` and `53,878,784`; the high-water mark of the resident set, `111,620,096` bytes at most, holds `54,206,464` of mapped file pages. The other modes, by `ru_maxrss` of the process: `fetch` `50,270,208`, `plan` `59,748,352`, `selftest` `39,448,576` — none above the first. The largest stands. Every mode runs under `nice -n 19`.

### 0.5 Refs and the number

```
git -C /root/btc-5m-twap fetch origin
git -C /root/btc-5m-twap ls-remote origin
git -C /root/btc-5m-twap ls-remote --heads origin tz-38-adv3-pit-validation | wc -l
I number
git -C /root/btc-5m-twap log --first-parent --name-status --format='%h %cI %s' -n 5 origin/main
```

Every ref line is reported. **`wc -l` must print `0`:** the branch does not exist. **`I number`** reads `git ls-tree --name-only origin/main -- CryptoTZ/ CryptoReports/` and must print `READING NUMBER: PASS - 2 of 2`: `CryptoTZ/` holds `TZ-38-adv3-pit-validation.md` and no other file whose name begins with `TZ-38-`, and `CryptoReports/` no report whose name does (CANON hard rule 2). Anything else is BLOCKED. A difference in the refs or the log from what map §1 records is recorded, not blocking, unless `main` does not carry revision `2026-10-31-b`.

---

## 1. Why this TZ exists

**What the advisor's numbers rest on.** CANON PART VII: the rule's history is 5,265 trades, `+0.158` R a trade, and STRONG's 253 trades `+0.547` R, of which longs `+167` R and shorts `−29` R, and five trades are `101%` of the total. The coins are the Boss's of 2026 — the ones that are still listed, still liquid and wanted. A list made in 2026 from what exists in 2026 is a selection on the future: it holds the coins that rose into view, and it holds none of the ones that were delisted. The history is therefore no evidence of an edge to come (PART VII says so) and, worse, the size of the edge it shows is overstated by an amount nobody has measured. Two questions follow, and they are this TZ's: **does the rule earn on contracts the Boss did not pick, and how much of STRONG's displayed edge is his list?**

**What the archive holds** [measured, the Architect's listing of `data.binance.vision`, 2026-10-31; structure alone, no price]. Under `data/futures/um/monthly/klines/` there are 1,056 symbols, of which 895 are plain `BASEUSDT` perpetuals (the rest are delivery futures, BUSD and USDC pairs and settled contracts). 864 of the 895 have a monthly file for 2026-09 and daily files for 2026-10; 31 stop earlier — the delisted. 623 had their first candle on or before 2025-11-30; 272 came after, among them the TradFi wave — XAUUSDT from 2025-12, equity, ETF and commodity perpetuals from 2026-01 — a different kind of contract with at most eleven months of history. The Boss's 42 are all among the 895; three of them (XAU, BTW, GRAM) are listed after 2025-11-30.

**The universe, and why these rules.** *L* is every one of the 895 whose first candle is on or before 2025-11-30 and whose base is not USDC (a contract pegged to the dollar has no trend to follow), taking part in a run only on the days it is **admissible**: the median quote volume (field 7 of the kline row) of the 28 candles before the day — all within 42 days of it — is `V_MIN = 10,000,000` USDT. A contract opens a trade only on an admissible day, and a position already open is held to its ordinary exit whatever the volume does; a contract whose data ends, delisted, is flat on its last day, which closes a position there at the close with one exit cost. **The floor is the bot's own sizing rule read backwards:** a position takes at most 0.1% of a coin's mean daily volume (`adv3-bot.py` `LIQ_FRAC`), so 10,000,000 USDT of daily volume is what a 10,000 USDT position needs. **The date is the TradFi wave's edge**, not a choice among results. **Everything is a function of what the contract had traded before the day** (`admissible` reads `qv[i-28:i]` and the days; §7 V7 proves it by perturbation). *G* is *L* less the Boss's 42, the contracts nobody picked; *P* is *L* with them.

**The instrument calls the advisor's functions and writes none of them.** `advisor/adv3.py`, loaded by its SHA-256, is ADV-3's only implementation (CANON PART VII). The instrument reads the candles into arrays, hands adv3 views of them that behave as its dictionaries do, and calls `adv3.states`, `adv3.simulate`, `adv3.simulate_strong`, `adv3.ranking` and `adv3.stats` as the bot's own history does. Three things are done *around* them and are tested one by one (§7): the admissibility lifts `adv3.unit` to `None` on a day it does not admit, so that no entry opens and no ranking admits the contract (`adv3.simulate` calls `unit` by its module name at line 261 and `adv3.states` at line 281); the universe is passed to `simulate_strong` through the module's `COINS` (it reads it at call time, line 306); and a contract that ends is made flat on its last day — `simulate_strong` leaves a position of a contract whose candles stop in `open_` for ever, holding one of the three places (lines 300–306 and 315), which the 42 coins, all alive, never showed. **G-EQUAL proves the glue:** over the Boss's 42, with no admissibility, the pipeline must equal the frozen FACTS (`adv3.facts_checks`, 20 checks) — 5,265 and 253 trades and the rest — and in the Architect's rehearsal it equals `adv3.history()` block for block as well.

**What it measures** — each a table in `result.json`, none with a threshold of this TZ's:

| reading | what | key |
|---|---|---|
| E1 | the rule on *G*: the monthly series, its t-test and block bootstrap, by year, long and short, concentration | `pit_rule` |
| E2 | STRONG on *G*, the same | `pit_strong` |
| E3 | E1 at `V` = 30,000,000 | `sensitivity` |
| E4 | what the card shows, measured on *P*: the share of trades whose price reached +1, +2, +3 R, the days held, the share winning, the mean R — for the rule and for STRONG | `P_rule`, `P_strong.top3` |
| E5 | STRONG on 500 lists of 42 contracts drawn from *L* at random: the quantiles of its total R and of its mean R a trade, and the place of the Boss's 42 among them | `random_lists`, `A_admissible` |
| E6 | STRONG with 5 and 7 places beside 3, by the place a trade entered at; STRONG's trades by the stop's distance, up to 11.1%, 11.1 to 14%, beyond | `P_strong.top5`, `top7` |
| E7 | of the STRONG trades entered with all four signs agreeing, those whose sum fell to ±2 with the signal kept: what they made after it against what leaving at it would have made | `P_strong.top3.weakening` |
| E8 | concentration: the five best trades' share and the mean R without the best 1% | in each block |

**What the status of E1 is, and what E1 to E8 are for.** E1 and E2 carry a word — REPLICATED, CONTRADICTED, UNDECIDABLE — because their procedure is the one the PIT record is read by (§4.5); in this run the word is a reading of an exploration and moves nothing. E3 to E8 are descriptive and were never meant to move anything: they set what the bot may *say* — E4 and E5 the figures its cards and ratings quote in place of the Boss's 42, E6 the answer to the Boss's top-N and 14% stop limits, E7 the answer to his invalidation alert — and what TZ-39 may build. No tuning follows from them: a parameter is changed only as a new frozen rule on records written after its freeze (CANON PART VII).

**What this TZ does not do.** It does not touch the bot, the unit, the daily message, the rule, the Boss's coin list or any rating. It runs no queue, no model of direction and no search over thresholds. The Boss's schedule, monitor, scanner, layout and stop-limit requests (his specification of 2026-10-31) are decided in CANON PART VII and built by a TZ of their own, TZ-39, which takes its numbers from this one's verdict.

---

## 2. Scope

**Paths this TZ writes.** On the branch `tz-38-adv3-pit-validation`: `research/tz38-adv3-pit-validation.py`, new. On the host: `/root/tz38-work/**`; `/root/btc-forensics/tz38-work--*`. On `main`: the report, `CryptoReports/TZ-38-adv3-pit-validation-report.md`.

**Prohibited**, by path and by content class:

1. Any change to a repository file but the one above and the report — `advisor/**`, `deploy/**`, `SYSTEM-MAP.md` and `BTC-EXECUTOR-INSTRUCTIONS.md` among them.
2. Any `systemctl` verb but `show` and `list-timers`; any signal to a process; any change to a capture unit, its store, either archive's timer or ledger, or the advisor's unit or record.
3. Any request but these: `https://s3-ap-northeast-1.amazonaws.com/data.binance.vision` (listings of one public bucket) and `https://data.binance.vision/` (its files), each under the `User-Agent` `btc-5m-twap-tz38`, and git's to GitHub. No request to `fapi.binance.com`, `api.telegram.org`, a venue or any other host.
4. Any read, copy, print or hash of anything under `/etc/adv3-bot/`.
5. A dataset or a binary in git history; a file of the store in the report. The store, the arena and the outputs are the host's and go with `/root/tz38-work`.
6. Any credential beyond the repository's, and any call that trades, signs or asks an exchange about an account.
7. Any change to a declaration of the instrument — `V_MIN`, `V_SENS`, `WINDOW`, `SPAN`, `MIN_COINS`, `MIN_MONTHS`, `ALPHA`, `BOOT_B`, `BOOT_L`, `SEED`, `RANDOM_LISTS`, `LIST_SIZE`, `LISTED_TO`, `EXCLUDED_BASES`: a different value is a new TZ, and `inputs.json` prints them all.
8. The report on `main` before the branch is pushed and its pull request opened (contract §4.1).

**Exemptions.** The requests of item 3, by the instrument's own `request`, which names its `User-Agent` on every one.

---

## 3. The work, in this order

### 3.1 The branch and its file

```
git -C /root/btc-5m-twap fetch origin
I number
git -C /root/btc-5m-twap worktree add -b tz-38-adv3-pit-validation /root/tz38-work/wt origin/main
```

`I number` must print `READING NUMBER: PASS - 2 of 2` again, or BLOCKED. Then §0.1's script again, verbatim but for its argument, `/root/tz38-work/wt`; it must print the same line, bytes and SHA-256 as at §0.1. Then:

```
git -C /root/tz38-work/wt add research/tz38-adv3-pit-validation.py
git -C /root/tz38-work/wt diff --cached --name-status
git -C /root/tz38-work/wt diff --cached --numstat
```

`--name-status` must print exactly one line — `A` for the instrument — and `--numstat` exactly `1782	0	research/tz38-adv3-pit-validation.py`, or BLOCKED. Commit it alone; `git ls-remote origin` (§0.5); push with `git push -u origin tz-38-adv3-pit-validation` — through `credential.helper=!gh auth git-credential` where the URL's credential is refused (map §6, git remote) — and open the pull request against `main`. A failed assert here is BLOCKED.

### 3.2 The self-test

```
I selftest
```

It must print `SELFTEST PASS: 58 of 58 checks passed`. It reaches no network, reads `advisor/adv3.py` of the primary checkout by its hash, builds synthetic contracts and synthetic stores in a temporary directory, and removes them. A red check stops the run here, and it goes to §9.

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

One `reclaim` names every earlier directory and must print `RECLAIM PASS` before any removal; then one `rm -rf` and one `test -e` a directory, the last reading `exit=1`. TZ-35's checker is `main`'s, frozen by the map's table, and its `reclaim` refuses a directory born with a running claude process and any path that is not a UUID directory under `/tmp/` whose parent's name carries `btc-5m-twap`. Map §3 expects the two directories named in §0.3 unless a reboot emptied `/tmp`; the live session of 2026-10-30 is not touched. If `scratch` names none earlier, the block is recorded as empty and skipped. **A refused `rm -rf` is handed to the Boss** as one exact command a tree, and verified by `test -e` (map §6, sandbox limit).

### 3.4 The mark and P-START

```
I mark
I probe
```

`mark` snapshots `MainPID`, `NRestarts`, `ActiveState` and `UnitFileState` of the three capture units and of `adv3-bot.service` into `state.json` by exclusive create; §3.7's `still` reads them against it. `probe` makes one request to each of the four endpoints the run uses, through the instrument's own `request` function: a listing of `data/futures/um/monthly/klines/BTCUSDT/1d/`, and a monthly kline file, a daily kline file and a monthly funding file of BTCUSDT; each is asserted served and parsed. It prints `READING P-START: served - 4 of 4 endpoints`, each line beside it. **A non-default `User-Agent` is fixed in the instrument and sent on every request; the archive served the project's other agent, `adv3-advisor/1`, to the Architect's session and to the advisor's host (map §6), and `btc-5m-twap-tz38` is this TZ's.** A failure is BLOCKED.

### 3.5 The plan and the fetch

Both wait for the band (06:35:00 to 20:30:00 UTC); the block waits in its own text, so whoever runs it cannot run it outside:

```
bash -c 'while :; do h=$(date -u +%H%M%S); [[ $h > 063459 && $h < 203000 ]] && break; sleep 30; done; date -u'
timeout 1800 I plan
timeout 5400 I fetch
```

`plan` lists the archive and writes `plan.json`: every plain `BASEUSDT` symbol of the klines listing, and for each its monthly kline files, the daily kline files of every month up to 2026-10 that has no monthly file, and its monthly funding files to 2026-09. The Architect's listing of 2026-10-31 gave `895` symbols, `66,677` keys and `3,771` listing calls, and a `plan.json` of `4,932,756` bytes, SHA-256 `83eb4f03ee3c2639894d2019a67539c5156dad97a33df2149512709dea5bb098` — **read, not expected**: Binance publishes a month's files in the first days of the next, so the plan of a later day lists 2026-10's monthly files in place of its daily ones, and the report prints the Executor's own figures. `fetch` takes each key by exclusive create into `/root/tz38-work/archive/`, verbatim, sixteen requests at a time, and writes `manifest.tsv`, one line `key`, `bytes`, `sha256` a file in key order. It prints `FETCH PASS: <files> files, <bytes> bytes in <s> s; manifest.tsv <bytes> bytes SHA-256 <hex>` or fails — **a planned key the archive does not serve is a failed assert**. A request is tried four times (`1`, `3` and `5` s between) before it fails.

### 3.6 The runs

```
timeout 3600 I run A
timeout 3600 I run B
I same
```

`run` is offline. It reads the store through `adv3`'s own readers, runs G-DATA and G-EQUAL, then every reading of §4, and writes `/root/tz38-work/out-<A|B>/`: `result.json`, `inputs.json` (the plan's and the manifest's SHA-256, `adv3.py`'s, the cut and every declaration), `monthly-G.csv`, `monthly-A.csv`, `trades-P-rule.csv`, `trades-P-strong-3.csv`, `-5.csv`, `-7.csv` and `random-lists.csv` — nine files, each by exclusive create. It prints, in order, `READING G-DATA`, `READING G-EQUAL`, one line a phase with the resident set, its anonymous part and its high-water mark, the readings, then one `OUT <file> <bytes> <sha256>` a file and `RUN PASS` with the largest anonymous set sampled. **`same` compares the two directories file by file by SHA-256** and prints `READING DETERMINISM: PASS - 10 of 10` — the same nine names, and each equal. A run that fails is not repeated into the same directory.

### 3.7 The closing reads

```
I still
df -B1 --output=source,size,avail /var/lib/btc-recorder
grep -E '^(MemAvailable|SwapFree):' /proc/meminfo
ls -la /root/tz38-work /root/tz38-work/out-A
```

`still` must print `READING STILL: PASS - 4 of 4`: the three capture units and the advisor's unit read as the mark has them. The report then holds the closing figures.

### 3.8 The report and the reclaim

The report is drafted in the primary checkout `/root/btc-5m-twap` and committed after §9's B-RECLAIM-OWN, to `main` (contract §4.1).

---

## 4. The gates — fixed here, and what each is

### 4.1 The procedural gates

| gate | reading | passes when |
|---|---|---|
| FINGERPRINT | §0.2 | `67 of 67` |
| HOST | §0.3 | `11 of 11` |
| NUMBER | §0.5, §3.1 | `2 of 2` at each |
| G-FILE | §0.1, §3.1 | the extracted file's lines, bytes and SHA-256 as the table has them; the diff exactly as §3.1 |
| SELFTEST | §3.2 | `58 of 58` |
| P-START | §3.4 | `4 of 4` |
| G-FETCH | §3.5 | `FETCH PASS`, no planned key absent |
| G-DATA | §3.6 | `42 of 42`: for each of the Boss's 42, the store's candles read by the instrument and by `adv3.archive_candles` are equal day for day |
| G-EQUAL | §3.6 | `20 of 20`: the pipeline over the Boss's 42, no admissibility, against `adv3.FACTS` through `adv3.facts_checks` — counts and verdicts exact, the means, shares and p-values at FACTS' four decimals |
| DETERMINISM | §3.6 | `10 of 10` |
| STILL | §3.7 | `4 of 4` |

Any one failing is BLOCKED with the evidence; none is repeated into the same state.

### 4.2 E1, E2 and E3 — the rule on the contracts outside the Boss's 42

**The series.** On each day *d* the instrument counts *N_d*, the contracts of *G* that are admissible on *d* and have a signal, and sums *S_d*, the rule's daily R over all the positions of those contracts — a position opened on an admissible day held to its ordinary exit, the exit cost of a position closed at the end of a contract's data added on that day. *x_m* is the sum over the days of calendar month *m* of *S_d / N_d*, a day with *N_d* = 0 adding nothing: the R the rule earned in the month for each admissible coin. A month counts where its last day is 2026-10-27 or before and its mean *N_d* is at least `MIN_COINS = 10`; with fewer than `MIN_MONTHS = 24` months the word is UNDECIDABLE and no test is made. For STRONG the series is the month sums of its daily R over the same months.

**The reading.** *n*, the mean, the standard deviation, *t = mean / (sd / √n)*; *p_t*, the Student upper tail at *t* with *n − 1* degrees of freedom (a continued fraction of the incomplete beta function, equal to `scipy.stats.t.sf` to `1e-11` at five points the self-test holds); *p_boot*, the circular block bootstrap of the centred series — blocks of `BOOT_L = 3` months, `BOOT_B = 100,000` resamples, each block's start ⌊*r · n* / 2⁶⁴⌋ for *r* the next output of SplitMix64 from the seed `0x3A38`, the last block cut to *n* values, *p* up = (1 + #{resampled mean ≥ the observed}) / (*B* + 1), *p* down alike with ≤. **The word:** REPLICATED where *p_t* and *p_boot* up are both at most `ALPHA = 0.05`; CONTRADICTED where both down are; UNDECIDABLE otherwise. The false-reading probability of each tail is at most `0.05` as the tests' own assumptions give it; **the instrument does not measure it, and any reading made by this procedure carries that sentence.** The alternative named: the Boss's 42 coins' own monthly Sharpe ratio under the same series, measured by the instrument; `result.json` prints the power at it, at half of it and at the set's own, by the normal approximation `φ(Sharpe · √n − z₀.₉₅)`. The power decides nothing.

**E3** is E1 on the contracts admissible at `V` = 30,000,000. **The status of all three is §1's: the Architect's exploration, re-derived. They move no rung.**

### 4.3 E4 to E8 — the descriptive readings

All on *P* (*L* with the Boss's contracts), `V_MIN` = 10,000,000, the rule's and STRONG's trades by `adv3.stats`, the definitions the cards already quote.

- **E4.** The rule and STRONG (three places): trades, wins, mean R, total R, the median days held, the share of trades whose favourable excursion reached +1, +2 and +3 R before the exit (`adv3.stats`' `mfe`), the Sharpe and the p of the daily portfolio R as FACTS carries them, by year of exit, long and short apart.
- **E5.** 500 draws of 42 contracts without replacement from *L* — a partial Fisher–Yates over the sorted list, SplitMix64 from `2 · 0x3A38 + 1` — STRONG on each, admissibility on: the quantiles `0.05`, `0.25`, `0.5`, `0.75`, `0.95` of its total R and of its mean R a trade, the share of draws with a positive total, the median number of trades, and, for the Boss's 42 under the same admissibility, its total R and the share of draws it exceeds.
- **E6.** STRONG with `TOP_N` = `STRONG_MAX` = 3, 5 and 7 (the module's two constants, set for the pass): trades, mean R, total R, long and short, and each trade by the place it entered at — 1 to 3, 4 to 5, 6 to 7, by `|z|` among the active, admissible contracts that day — and each trade of each variant by its stop's distance, `100 · U / entry close` percent, up to 11.1, to 14, beyond.
- **E7.** Of the STRONG trades (three places) entered with the sum of signs at ±4: those whose sum fell to ±2 on a close with the signal kept, and for them `delta = R at the end − (R at that close − the exit cost in R)` — what holding made against leaving at that close — its mean, median and the share above zero; and the mean R of those that never fell.
- **E8.** In every block: the five best trades' share of the total R, and the mean R without the best 1% of the trades.

### 4.4 What the readings inform

Nothing is decided by a threshold of this TZ. The verdict states, from the Executor's figures: what STRONG's card may quote for its expectancy (E5's median of the mean R a trade, in place of the 42's `+0.547`) and its reach shares (E4); whether a 14% stop limit and a top-N beyond 3 have any evidence against them (E6); and whether a falling sum of signs is an exit (E7). TZ-39 builds what CANON PART VII has already decided and what the verdict adds.

### 4.5 The PIT record

CANON PART VII defines it and its reading; this TZ writes the instrument that reads it. `admissible`, `rule_pass`, `monthly`, `read_series` and `power` are, once this TZ is accepted, the only implementations of that reading, frozen by the map's table, which the reading's TZ imports by hash and never writes again. The contracts, the floor, the date and the statistics are §1's and §4.2's.

### 4.6 Committed before the Executor's run

The Architect's rehearsal on 2026-10-31, under Python 3.12.3 on the instrument of §0.1's table, two runs A and B, `same` reading `PASS - 10 of 10`. **The SHA-256 of what they wrote** — a file the Executor's run writes differently is a finding of the verdict, not a failure of the run; the figures depend on the archive alone and on nothing the Executor chooses, so a difference means the archive changed between the two days or a host differs. **`inputs.json` is the exception:** it holds the SHA-256 of the Executor's own plan and manifest, which differ wherever the listing of its day does (October's monthly files may have appeared); the eight other files carry the candles' consequences alone:

| file | bytes | SHA-256 |
|---|---|---|
| `inputs.json` | 605 | `b3705da9c9e57fe771540ad01871f95b149658b45e9b88618f40d32bc5ed17ec` |
| `monthly-A.csv` | 2,732 | `f9efa9c0d195a10701d05f94e81df67cdb9a76ce68e2353c2df0ad9dd43407a6` |
| `monthly-G.csv` | 4,561 | `6a581f6cd548566d40cd5976e74aa82786e85b58f5fd80f8650da2f772886208` |
| `random-lists.csv` | 33,985 | `029e236ad51a04d6e645b097c228b9d2002115b35d664f1329d7c37bea7ba441` |
| `result.json` | 14,392 | `4873b6e77e927c5aa0ca59c5f8593a42cd9a05c80c54010efd5e42e2b7471608` |
| `trades-P-rule.csv` | 2,329,047 | `aa62838d70efaf50ee819c9e6d90b5e289e6730eab34ecade67ba24fbbd769da` |
| `trades-P-strong-3.csv` | 25,987 | `b31d6e0910a2bf3516abe14c264e679fa8077b7ce3b80e2dfc0113c5dc3e123d` |
| `trades-P-strong-5.csv` | 43,964 | `c19fcdac3e44e81bad26744d37ae4c65b52b9f9a60afd0ffc05e82b29c5c4929` |
| `trades-P-strong-7.csv` | 60,681 | `a2b36e1e5fa26a5c57a54467ba6c2b5c3a63f06d99f2f8a240c830958c082729` |

The largest anonymous set sampled: A `57,004,032`, B `53,878,784` bytes; the run took `329` s and `338` s on the Architect's machine.

### 4.7 What a PASS establishes, and what it does not

It establishes that the instrument runs on the host and that the archive's own bytes, fetched by the Executor and listed in a manifest, give the Architect the numbers he holds — or it names where they differ. It establishes the measurements the bot's figures will rest on. It does not establish that the rule earns, on any contract, in any year to come; it moves no rung; and it says nothing about direction.

---

## 5. The file

**`research/tz38-adv3-pit-validation.py`** — new, 1782 lines, standard library alone, under `/root/tz04a-env`. Modes: `fingerprint`, `host`, `number`, `probe`, `plan`, `fetch`, `mark`, `still`, `run A|B`, `same`, `keep`, `selftest`, and `equal`, which the Architect runs in his audit (the pipeline over the 42 against `adv3.history()` block for block, in a process of its own: `adv3.history()` alone peaks near 83 MB). **Pure functions** — `admissible`, `monthly`, `monthly_sum`, `t_sf`, `boot_p`, `read_series`, `power`, `bucket_table`, `rank_at`, `weakening`, `plan_symbol`, `request`, `parse_map`, `number_reading`, `memory_gate`, `still_reading`, `kept_files` — each run by the self-test on stand-ins with a negative control; **the pipeline** — `Series`, `Candles`, `States`, `Arena`, `candle_rows`, `fill_states`, `funding_for`, `rule_pass`, `strong_pass`, `run_prepare`, `run_measure` — run by the self-test on synthetic stores against `adv3`'s own functions on dictionaries and against `adv3.history()`, and on the real store by G-DATA and G-EQUAL. It starts, stops and signals nothing and sends no request but §2's.

---

## 6. Cost

Measured by the Architect on 2026-10-31 under Python 3.12.3, one core, and taken at the population's upper bound — the store of §0.4, 612 contracts loaded, 609 in *L*.

| check | population | measured | bound |
|---|---|---|---|
| `selftest` | 58 checks, synthetic contracts of 420 days, no network | `19` s | `120` s |
| `probe` | four requests | under `5` s | `129 · 4 = 516` s at worst |
| `plan` | 895 symbols, 3,771 listing calls, twelve at a time | `209` s | `timeout 1800` |
| `fetch` | 66,677 files, sixteen at a time | `527` s for 23,399 downloaded and the rest hashed, on a machine with 8 GB and a proxy | `timeout 5400` |
| `run` | 612 contracts, about 700,000 contract-days: reading and states `150` s, the rule and STRONG on *G* `20` s, the sensitivity `7` s, the rule on *P* `7` s, the three STRONG passes `15` s, the 42 under admissibility `3` s, 500 random lists `30` s | `329` s and `338` s | `timeout 3600` each |
| `same`, `still`, `host`, `fingerprint`, `number`, `keep` | files, `systemctl show`, `git` | under `5` s each | `30` s |

**Single-session processor, term by term at the measured rate and a host assumed three times slower** — the Architect has not measured the host's core against his own: `selftest` `30`; `plan` and `fetch`, measured on 1,500 files at `3.6` ms of processor a file and four symbols' listings at `15` ms a symbol, so `66,677 × 3.6 + 895 × 15` ms `= 253` s and `3 × 253 = 760`; the two runs `2 × 3 × 340 = 2,040`; the rest, `100` — **`2,930` s, under `3,600`; nothing is sampled.** The two runs and the fetch are the only terms that grow with the store, and the store is the archive's own upper bound at the listing of the run. **The fail-fast bounds, each with its derivation:** `request` has four tries of 30 s with `1`, `3` and `5` s between, `129` s a request, and the first request that fails ends the mode; a mode that stalls is ended by its `timeout`, `1,800` s for `plan` (`8.6 ×` its measure), `5,400` s for `fetch` (`10 ×`), `3,600` s for a run (`14 ×`). **Wall clock about 2 hours:** §0 to §3.4 about 20 minutes; the plan about 5, the fetch about 15 to 40, each run about 5 to 20; §3.7, the report and §9 about 20 — plus a wait for a band that is at most 8 h 5 min, from 20:30:00 to 06:35:00 UTC. **The host pays, after the session:** nothing it did not pay before; §9 returns `/root/tz38-work`.

---

## 7. Validation

| # | check | count |
|---|---|---|
| **V1** | §0.2's fingerprint | `READING FINGERPRINT: PASS - 67 of 67`: revision `2026-10-31-b`; 6 anchors, 4 re-derived; 57 rows, 54 of 54 `frozen` equal; the loader's hash |
| **V2** | §0.3's host gate | `READING HOST: PASS - 11 of 11`; the memory figures of the first read and of the second, if one was made |
| **V3** | §0.5's NUMBER, at §0.5 and at §3.1 | `READING NUMBER: PASS - 2 of 2` each, the `TZ-38-` path printed; the branch count `0` |
| **V4** | §0.1's and §3.1's file | 1 of 1 hash asserted at each, lines and bytes; the branch's diff naming exactly `A`, and `--numstat` exact |
| **V5** | the self-test | `58 of 58`, among them the causality by perturbation of `admissible` — the volumes from index 60 on multiplied by 1,000 leave the flags up to index 60 bit-identical — and its negative control, the flags after it changing |
| **V6** | P-START | `READING P-START: served - 4 of 4 endpoints`, each line printed |
| **V7** | PLAN and G-FETCH | the plan's counts, the fetch's files and bytes, the manifest's SHA-256; no planned key absent |
| **V8** | G-DATA | `READING G-DATA: PASS - 42 of 42`, in each run |
| **V9** | G-EQUAL | `READING G-EQUAL: PASS - 20 of 20 (FACTS alone)`, in each run |
| **V10** | E1 to E8 | every table of `result.json` named in §1 present and printed in the report; the largest anonymous set of each run; the OUT lines |
| **V11** | DETERMINISM | `READING DETERMINISM: PASS - 10 of 10`; the nine files' SHA-256 of A and of B, equal |
| **V12** | STILL | `READING STILL: PASS - 4 of 4` |
| **V13** | contract §4.2's self-check | run after the push and the pull request and before the report's commit |
| **V14** | §3.7's closing reads | every read printed |
| **V15** | B-RECLAIM-SCRATCH and §9's `keep` | files considered, copied and held; the store's count after equal to before plus the copies |
| **V16** | §9's removals | `git worktree remove` without `--force` exit `0`; `test -e` exit `1` for `/root/tz38-work` and each directory removed; `git worktree list` naming `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else |

---

## 8. The report

`CryptoReports/TZ-38-adv3-pit-validation-report.md`, in contract §8's order. **In its first ten lines:** NUMBER at both reads; FINGERPRINT and HOST; the self-test; P-START; the plan's and the fetch's counts; G-DATA and G-EQUAL; DETERMINISM; STILL. **Then the tables E1 to E8**, as `result.json` holds them, rounded to four places, with the word of E1 and E2 stated as §1 states its status — an exploration, re-derived, that moves no rung. Beyond what V1 to V16 print: the largest anonymous set of each run and each mode's `ru_maxrss`; every memory and free-space read with its instant; the commit and the pull request; §9's counts and removals; and every file the run wrote, by SHA-256. **It never prints a file of the store, a credential, the content of any file under `/etc/adv3-bot/`, or a price of a live market.** The report is drafted in the primary checkout `/root/btc-5m-twap` before B-RECLAIM-OWN and committed after it.

---

## 9. Reclaim — the host left clean (CANON hard rule 15)

**What a file is kept for:** `I keep` copies `state.json`, `plan.json`, `manifest.tsv`, every file under `logs/`, `out-A/` and `out-B/` into `/root/btc-forensics/` as `tz38-work--<path with - for />`, by exclusive create, and verifies each hash; a name already there with the same hash is counted as held, and with another a failed assert. The store, the arena (already unlinked) and the branch worktree are not copied: `keep` asserts that `git status --porcelain --ignored` in the worktree prints nothing and that its `HEAD` is its upstream's, so `git worktree remove` needs no `--force`. **No output of `keep` or `reclaim` is filtered**: every line it prints is quoted. B-RECLAIM-SCRATCH is §3.3.

**B-RECLAIM-OWN**, last, after §3.7 and with the report drafted. **Its output is written to no file; the report quotes it verbatim from the session**, every line of it:

```
nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz38-work/stage/research/tz38-adv3-pit-validation.py keep
git -C /root/btc-5m-twap worktree remove /root/tz38-work/wt; echo "exit=$?"
rm -rf /root/tz38-work; echo "exit=$?"
test -e /root/tz38-work; echo "exit=$?"
git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
find /root/btc-forensics -type f | wc -l
df -B1 --output=source,size,avail /var/lib/btc-recorder
```

The branch `tz-38-adv3-pit-validation` stays on `origin` and as a local ref; only its working tree goes. **Kept:** the capture roots, both archives' state, the advisor's service copy and record and the forensic store are data, never scratch. **A refused `rm -rf` is handed to the Boss** by §3.3's route, one tree per command, and verified by `test -e`. The tree is about `330,000,000` bytes on disk, almost all of it the store.

---

## 10. Pre-send checks

Performed by the Architect on 2026-10-31 against this file as sent, in a reading separate from its writing — the body was written, read start to end and corrected where it read wrongly, and this section written after — with the repository at `origin/main` `133d57f55b37a483c2675c3354f2cecf5c520d77` (after the merge of PR #37 and the upload of map revision `2026-10-31-b`, 1,985 lines, SHA-256 `8d33d8d21d11f16871299246474f6144f3d6d94c0ae6c80c5acbee2a7efa280c`; fetched again before sending, `main` unchanged, no `TZ-38-` file, no report and no `tz-38` branch). Line numbers are those of the instrument §0.1 extracts for Appendix A, and those of `main` for committed code.

| # | check | result |
|---|---|---|
| **C1** | scope against body | **Repository paths the body names:** `CryptoTZ/TZ-38-adv3-pit-validation.md`, read by §0.1's script and named by `number`; `CryptoTZ/` and `CryptoReports/`, listed by `number`; `SYSTEM-MAP.md` and the other 56 rows of its table, read by `fingerprint`, among them `BTC-EXECUTOR-INSTRUCTIONS.md` (cited for contract §1, §4.1, §4.2 and §8), `research/tz33-reward-book-capture.py` (cited for line 190, `STREAM_FLOOR = 7300000000`), `research/tz35-advisor-deploy.py` (run for `scratch` and `reclaim`), `research/twap-divergence.py`, `research/recorder/recorder.py` and `research/pfair.py` (hashed for the anchors), `advisor/adv3-bot.py` (cited for `LIQ_FRAC`, line 25) and `advisor/selftest-adv3.py` and `advisor/RULE-ADV-3.txt` (rows of the table, hashed); `advisor/adv3.py`, **loaded and executed by hash and written never**; `research/tz38-adv3-pit-validation.py`, written on the branch; `CryptoReports/TZ-38-adv3-pit-validation-report.md`, written to `main`. **Host paths:** `/root/tz38-work/**` written (`archive/`, `arena.bin` for the seconds before it is unlinked, `out-A/`, `out-B/`, `logs/`, `stage/`, `wt/`, `plan.json`, `manifest.tsv`, `state.json`); `/root/btc-forensics/tz38-work--*` written; `/var/lib/btc-recorder` read by `find`, `grep -c` and `df`; `/var/lib/btc-rewardbook`, `/var/lib/btc-pairbook`, `/var/lib/adv3-bot` and `/root/.claude` read by `du -sb`; `/proc/meminfo` and `/proc/self/status` read; systemd read by `show` and `list-timers` and written never. **Network:** the bucket's listing and its CDN, through `request` alone — `grep -n 'urlopen'` over the instrument finds one call, line 109, and no line that opens `/etc/adv3-bot`, `fapi`, Telegram or a venue; `adv3.get` is replaced by a reader of the store before any `adv3` function runs (`run_prepare`, `mode_equal`), so none of `adv3`'s own requests can be made. **Output files:** the nine of §3.6, the plan, the manifest, the state and the store. **Intersections with §2:** none of the nine carries a price — they hold dates, R, a stop's distance as a percent, counts and ratios — against item 5's «a file of the store in the report»; the store holds Binance's public daily candles and is not copied, committed or quoted; `inputs.json` holds the declarations of item 7, printed and not changed; item 3 is held by the single `urlopen`. No exemption is added beyond §2's. |
| **C2** | origin of every expectation | **Quoted from a committed artifact:** `57`, `54`, `2`, `1` and the six anchors — map `2026-10-31-b` §0, counted by an independent parse of the table and by `fingerprint` against the clone at `133d57f`, `PASS - 67 of 67`; `42` — `len(adv3.COINS)`; `20` — the entries `adv3.facts_checks` returns (2 blocks × 9 facts + 2 gates), counted by a call; `7,300,000,000` — `research/tz33-reward-book-capture.py` line 190; `31,612,203,008` and `e3975b5…` — map §6 host identity; `d73a657e…` — map §0 row `advisor/adv3.py`; `122,462,208` — twice `61,231,104`, arithmetic. **Computed by an implementation independent of the one under test:** the five values of `t_sf` — `scipy.stats.t.sf` 1.18.1 at 16 digits, held by the self-test to `1e-11` relative, so the literal's precision is five decades better than the tolerance and no more, a double's limit, which this TZ states and does not claim to be ten; `0.8065153063880648` (the power) — `scipy.stats.norm`; `(0.63968015992004, 0.36081959020489757)` — the bootstrap, from an independent implementation that builds each resample explicitly, in counts over `B + 1`, exact; the three SplitMix64 outputs for state 0 — the algorithm's published test vector, equal to the instrument's and to the independent implementation's; `58`, `11`, `4`, `10`, `2` — counted from the instrument by name (C5). **Measured by the Architect and read, not expected:** `61,231,104`, `54,951,936`, `55,914,496` and the rest of §0.4; `291,500,032`; the plan's `895`, `66,677`, `3,771`; the listing's `1,056`, `864`, `31`, `623`, `272` — a count of the bucket's listing of 2026-10-31. **No gate of this TZ expects a value that this TZ measures:** the readings E1 to E8 carry no expectation, and §4.6's hashes are the Architect's rehearsal, compared by the verdict and read by no check. |
| **C3** | shape of every diff | One path. **`research/tz38-adv3-pit-validation.py` is new**: `git cat-file -e origin/main:research/tz38-adv3-pit-validation.py` exits `128`, so the change replaces none of its lines; the report's path and this TZ's own path exit `128` as well. The list of replaced lines is none, and no sentence of this TZ calls the change additive. |
| **C4** | cost of every check | §6, at the population's upper bound: the store as the listing of 2026-10-31 gives it, 66,677 files, 895 symbols, 612 contracts loaded, 609 in *L*. **Processor, single session, term by term:** `30 + 760 + 2,040 + 100 = 2,930` s, under `3,600`; nothing is sampled — the selftest `30` against `19` measured; `plan` and `fetch` `3 × (66,677 × 0.0036 + 895 × 0.015) = 760` against `3.6` ms a file measured on 1,500 and `0.015` s a symbol on four; the two runs `2 × 3 × 340 = 2,040` against `329` and `338` s of wall measured with other work on the machine, `232` s alone; the rest `100`. **The fail-fast bounds, each with its derivation:** `request` four tries of 30 s with `1 + 3 + 5` s between, `129` s, the first failure ending the mode; `timeout 1800` on `plan` is `8.6 ×` its `209` s, `5400` on `fetch` is `10 ×` its `527` s, `3600` on a run `10.6 ×` its `338` s; `probe` four requests at `129` s, `516` s at worst; the band's wait at most `8 h 5 min` (20:30:00 to 06:35:00). **Wall clock** about 2 hours, §6. |
| **C5** | every count | `67` = 1 revision + 6 anchors + 4 re-derived + 54 frozen rows + 1 table shape + 1 loader (`mode_fingerprint`), re-run on the clone at `133d57f`: `PASS - 67 of 67`. `11` = H1 one, H2 two, H3 one, H4 three, H5 one, H6 one, memory one, disk one (`mode_host`); run on stand-ins: `11 of 11`, a first memory read below the floor decided by the second, and six negative controls reading FAIL. `2`, `number_reading`. `58` = statistics 8 (`t_sf` 2, SplitMix64 1, `probit` and `phi` 1, `power` 1, `boot_p` 1, `read_series` 1, `mean_sd` 1), months 4, `admissible` 7 (five readings, the perturbation and its negative control), the views over adv3 5, the gate 3, a contract that ends 2, `rule_pass` 3, tables 3, `weakening` 2, `candle_rows` 1, G-EQUAL on a synthetic store 2, the arena 2, `request` 1, `plan_symbol` 1, the host 8 (two passing and six negative controls), `kept_files` and `mode_same` 2, and the checker's `parse_map`, `number_reading`, `memory_gate` and `still_reading` 4 — `58 of 58`, under Python 3.12.3 and 3.13.18. `42` and `20`, C2. `4` = the endpoints of `probe`. `10` = the nine names of §3.6 and the equality of each. `4` = the units of `still`. *L* `609`, *G* `570`, loaded `612`, delisted in *L* `28`: counted by `run_prepare` on the store of 2026-10-31 in each of the Architect's four runs — read, not expected. |
| **C6** | every population | NUMBER: the paths under `CryptoTZ/` and `CryptoReports/` of `origin/main` at its two reads. FINGERPRINT: the map's table of 57 rows against the files of the primary checkout. HOST: the host at the instant of the read. SELFTEST: synthetic contracts of 420 days and synthetic stores, no network. P-START: one request to each of four endpoints. PLAN: the bucket's listing of the run's instant. FETCH: the keys of the plan. G-DATA: the Boss's 42 contracts, every day of each to 2026-10-27. G-EQUAL: the same 42, the rule and STRONG, no admissibility. E1 and E2: *G*, the admissible contract-days of 570 contracts, months with at least ten admissible coins on average. E3: *G* at `V` = 30,000,000. E4, E6, E7 and E8: *P*, the admissible contract-days of the 609 contracts of *L*. E5: 500 lists of 42 contracts drawn from *L*, and the Boss's 42 under the same admissibility. DETERMINISM: the nine files of two runs. STILL: the four units. |
| **C7** | every signature and every behaviour | **Committed code this TZ relies on, read at `133d57f`.** `advisor/adv3.py`: `def get(url, tries=4):` 42; `def months(a, b):` 63; `def zip_rows(body):` 70; `def ms_day(ms):` 76; `def holding_day(ms):` 82; `def archive_candles(sym, last_day, pool, first=ARCHIVE_FROM):` 89; `def _valid(ym, k):` 111; `def archive_funding(sym, first, last, pool):` 119; `def unit(c, days, i):` 211; `def open_at(side, close, U, day):` 218; `def hold(pos, candle, pc, fund_d, day):` 222; `def close_at(pos, close, day):` 237; `def simulate(c, fund, first_entry, last_day):` 243; `def states(c, last_day, since=None):` 270; `def ranking(day_states):` 285; `def simulate_strong(cs, st, funds, first_entry, last_day):` 293; `def stats(trades, daily):` 326; `def funding_of(per_day, covered_days):` 375; `def history():` 382; `def facts_checks(h):` 721. **The sentences that rest on their bodies.** *Entries are gated through `unit`:* `U = unit(c, days, i) if pos is None and sig in (1, -1) and d >= first_entry else None` (261) opens a trade only `if U:` and `out[d] = (signal(...), ..., unit(c, days, i), closes[i])` (281) carries the same `U` to the ranking, whose `active = [... if s[0] in (1, -1) and s[1] is not None and s[3]]` (287) drops a contract with `U` of `None`; both call `unit` as a module name, so the instrument's replacement reaches them, and a position open already is held by `hold` (251, 302) which never calls `unit`. *The universe is `COINS`:* `today = [(coin, st[coin][d]) for coin in COINS if coin in cs and d in st[coin]]` (306), read at call time; `TOP_N` at 288 and `STRONG_MAX` at 315 likewise. *A contract whose candles stop leaves a position open for ever:* `if d in cs[coin] and coin in prev:` (301) skips the hold and nothing else removes `open_[coin]` but the stop (302–305) and the signal flip at 307–310, which needs a state on the day — the reason the instrument makes the last day flat. *`stats`' held days* `[(t['exit'] - t['entry']).days for t in trades if 'exit' in t]` (330) leaves out a trade that has no `exit`, as `history()` leaves out the positions it closes at the cut (404, 413–415: `dict(ph, R=ph['R'] - COST * c[days[-1]][3] / ph['U'], why='open at the history cut')`), which is why the instrument's end trades carry `end` and not `exit`. *`history()`'s order and gates* (402–422) are those `facts_shape` repeats: `top5_share` over `sorted(R, reverse=True)[:5]`, `gate_H` and `gate_S`. *`funding_of`'s closure* (375–377) reads `per_day.get(d, 0.0)` and nothing else of `per_day`, so a two-array object with `.get` serves. *`facts_checks`* compares 18 facts and 2 verdicts against `FACTS` (721–739). Nothing of this TZ rests on a sentence the bodies do not bear out; three statements of an earlier draft did not — the line numbers of `unit`'s two call sites, the line of `COINS`, and the count of the October daily files in §1 — and were rewritten. |
| **C8** | every cross-reference | Resolved by reading the text referenced. **CANON `2026-10-31-b`:** PART II — «a gate is a threshold plus a sampling rule, and both are fixed before any score exists» (the ground of §1's status paragraph); PART VI — the fourth rule, a set the Architect has read is an exploration (§1, §4.2); PART VII — the evidence ladder, the PIT record, the decisions on the specification (§1, §4.4, §4.5); hard rules 2 (§0.5), 5, 9 (§0.4), 12, 13 (§10), 14 (the band, P-START), 15 (§9). **Map `2026-10-31-b`:** §0's anchors and table of 57 rows, 54 / 2 / 1; §1's record of refs; §2.5 and §2.6 for the archives' calendar runs at 03:00:20 and 01:30:20; §3's `2,267` files in the forensic store, the two directories TZ-37's session left, `f13dd443…` and `50f7dcda…`, and the live session `238335b9…`; §6's host identity, `/root/tz04a-env` on Python 3.12, the push through `gh`'s credential helper, the sandbox limit on destructive actions, and its memory row; §7 items 125 and 129 (a reload re-arms an archive's run — this TZ reloads never), 131 (a floor is twice the largest peak) and 137 (the floor's asserted read, a first read below it read again after 60 s). **Contract:** §1 steps 1 to 4, §4.1, §4.2, §5, §8. **TZ-37:** its §3.3 and §9 are the pattern of §3.3 and §9. **The Boss's words:** this TZ quotes none of his file; §1 paraphrases his standing objective of 2026-10-31 as CANON states it. |

**Seven checks could not be performed from this session**, and each is converted into a mechanical condition the Executor evaluates and BLOCKS on (CANON hard rule 13): the host's own state — free space, memory, units, interpreter — `I host`, §0.3; the live reach and the speed of `data.binance.vision` from the host under this TZ's `User-Agent`, which this session reached under `adv3-advisor/1` and `btc-5m-twap-tz38` alike — `I probe` (P-START) and `I fetch` (G-FETCH), before any run; the instrument under the host's `/root/tz04a-env` interpreter, which this session ran under `/usr/bin/python3.12`, Python 3.12.3, the same patch version, and under 3.13.18 — `I selftest`, G-DATA and G-EQUAL on the host; the run's memory on the host, which item 131 says runs above the Architect's measure — the floor is twice the largest anonymous set, `MemAvailable` is asserted on `I host`'s read, and the report quotes the host's own peak; NUMBER on `main` with this file uploaded — `I number` on the clone, which holds no `TZ-38-` file, reads `FAIL - 1 of 2` by design, and the stand-ins read `PASS - 2 of 2` and `FAIL` with a second file and with a report; TZ-35's `scratch` and `reclaim` against the host's real `/tmp`; and the archive's publication of October's monthly files after this listing, which makes the plan's keys differ and the candles equal — the report prints the Executor's own plan and the verdict compares the candles by the rehearsal's hashes (§4.6). **Everything else above was performed here:** the self-test, 58 checks, under both interpreters; `fingerprint` against the clone, `67 of 67`; §0.1's script run against this file, one file, hash equal, and its refusal over a non-empty destination; the plan, the fetch and four full runs of the instrument over the real store, the last two, A and B, under Python 3.12.3 on the instrument of §0.1's table, `READING DETERMINISM: PASS - 10 of 10`, and six of their nine files byte-identical to those of an earlier run under Python 3.13.18 (the other three changed with the fields the code added since); `equal` — the pipeline against `adv3.history()` block for block on the real store, `22 of 22`; the t-test against `scipy`, the bootstrap against an explicit-resample implementation, SplitMix64 against its test vector; a lint of the instrument, clean under `pyflakes`; and the memory of every mode.

---

## Appendix A — the file, byte for byte

```python file=research/tz38-adv3-pit-validation.py
#!/usr/bin/env python3
# tz38-adv3-pit-validation.py - TZ-38's instrument: ADV-3's frozen rule run, unchanged, on every Binance USD-M USDT perpetual
# that traded - the Boss's 42 coins, the delisted ones and the rest - with an entry allowed only where the contract was liquid
# before the day. Standard library only. It fetches Binance's public archive (data.binance.vision) into a store, builds each
# contract's point-in-time admissibility, runs the advisor's own functions (advisor/adv3.py, loaded by its hash, never copied
# and never written), and writes the tables. The reading of the rule on the contracts outside the Boss's 42 is an exploration
# that moves no rung (CANON PART VII). It starts no unit, signals no process, reads nothing under /etc/adv3-bot and nothing of
# the Boss's account. Exits: 0 every assert held; 1 a failed assert, named; 3 NOT YET.
import bisect, contextlib, datetime as dt, hashlib, http.client, importlib.util, io, json, math, os, re, resource, shutil, \
    statistics, subprocess, sys, threading, time, urllib.error, urllib.parse, urllib.request, xml.etree.ElementTree as ET
from array import array
from concurrent.futures import ThreadPoolExecutor

WORK = os.environ.get('TZ38_WORK', '/root/tz38-work')
PRIMARY = os.environ.get('TZ38_PRIMARY', '/root/btc-5m-twap')
FORENSICS = '/root/btc-forensics'
STORE = WORK + '/archive'
OUT = WORK + '/out'
NUMBER = 'TZ-38-'
TZ_FILE = 'CryptoTZ/TZ-38-adv3-pit-validation.md'
MAP_REV = '2026-10-31-b'
ANCHORS = {'A1': '229a944f2d51', 'A2': '6c5089330629',
           'A3': '0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable',
           'A4': '437b45ea196b', 'A5': '0f6c90451cbd', 'A6': '729f0bcdbee3'}
DERIVED = {'A2': 'research/twap-divergence.py', 'A4': 'BTC-EXECUTOR-INSTRUCTIONS.md',
           'A5': 'research/recorder/recorder.py', 'A6': 'research/pfair.py'}
ROWS, FROZEN = 57, 54
ADV3_SHA = 'd73a657ef31decad276b858c4ec9672dce1c1c5cec36f0bb1c5b3378838224a8'
RULE_SHA = 'ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169'
MEM_FLOOR, DISK_FLOOR = 122_462_208, 7_700_000_000   # TZ section 0.4: twice the largest anonymous set of any mode, and the reward book's floor plus this TZ's bytes

S3 = 'https://s3-ap-northeast-1.amazonaws.com/data.binance.vision'
CDN = 'https://data.binance.vision/'
UA = 'btc-5m-twap-tz38'
KL = 'data/futures/um/monthly/klines/'
FU = 'data/futures/um/monthly/fundingRate/'
KD = 'data/futures/um/daily/klines/'

# ---- the declarations of the gate, fixed before any contract outside the Boss's 42 was read ----------------------------
V_MIN = 10_000_000.0       # admissibility: the median daily quote volume of the 28 candles before the day, in USDT
V_SENS = (30_000_000.0,)
WINDOW, SPAN = 28, 42      # candles in the median; the days they must lie within
MIN_COINS = 10             # a month counts where its mean number of admissible coins is at least this
ALPHA = 0.05               # G-PIT's one-sided level for each tail, for the t-test and for the bootstrap alike
BOOT_B, BOOT_L, SEED = 100_000, 3, 0x3A38
RANDOM_LISTS, LIST_SIZE = 500, 42
M64 = (1 << 64) - 1


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


def verdict(name, checks):
    n = sum(1 for v in checks.values() if v)
    for k, v in checks.items():
        out(('ok   ' if v else 'FAIL ') + k)
    out('READING %s: %s - %d of %d' % (name, 'PASS' if n == len(checks) else 'FAIL', n, len(checks)))
    if n != len(checks):
        raise Failed(name)


# ---- the advisor, loaded by hash ---------------------------------------------------------------------------------------

def load_adv3():
    path = PRIMARY + '/advisor/adv3.py'
    assert sha256_file(path) == ADV3_SHA, 'advisor/adv3.py is not the frozen file'
    spec = importlib.util.spec_from_file_location('adv3', path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules['adv3'] = mod
    spec.loader.exec_module(mod)
    return mod


# ---- the archive: listing, plan, fetch, manifest -------------------------------------------------------------------------

def request(url, tries=4):
    """The body of url, or None where the server answers 404; a network error, 418, 429 or 5xx is tried again after 1, 3 and
    5 s; any other answer raises at once. Every request names UA."""
    err = None
    for k in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=30) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code not in (418, 429) and e.code < 500:
                raise RuntimeError('FETCH REFUSED %s: HTTP %d' % (url, e.code)) from None
            err = e
        except (OSError, http.client.HTTPException) as e:
            err = e
        if k + 1 < tries:
            time.sleep(1 + 2 * k)
    raise RuntimeError('FETCH FAILED %s: %r' % (url, err))


def s3_list(prefix, delimiter='/'):
    """([common prefixes], [keys]) under prefix, page after page of 1,000."""
    prefixes, keys, marker = [], [], ''
    while True:
        q = {'prefix': prefix, 'max-keys': '1000'}
        if delimiter:
            q['delimiter'] = delimiter
        if marker:
            q['marker'] = marker
        body = request(S3 + '?' + urllib.parse.urlencode(q))
        assert body is not None, 'listing %s' % prefix
        root = ET.fromstring(body)
        ns = {'s': root.tag.split('}')[0][1:]}
        prefixes += [e.find('s:Prefix', ns).text for e in root.findall('s:CommonPrefixes', ns)]
        keys += [e.find('s:Key', ns).text for e in root.findall('s:Contents', ns)]
        if root.find('s:IsTruncated', ns).text != 'true':
            return prefixes, keys
        nxt = root.find('s:NextMarker', ns)
        marker = nxt.text if nxt is not None else (prefixes[-1] if delimiter and prefixes else keys[-1])


def month_of(key):
    m = re.search(r'-(\d{4})-(\d{2})\.zip$', key)
    return (int(m.group(1)), int(m.group(2))) if m else None


def plan_symbol(sym, hist_to, funding_to):
    """The keys one contract needs, by the listing: every monthly kline file, the daily files of each month up to hist_to's that
    has no monthly file, and every monthly funding file up to funding_to. Returns (keys, listing calls made)."""
    _, k1 = s3_list(KL + '%s/1d/' % sym)
    monthly = sorted(k for k in k1 if k.endswith('.zip'))
    have = {month_of(k) for k in monthly}
    _, f1 = s3_list(FU + '%s/' % sym)
    funding = sorted(k for k in f1 if k.endswith('.zip') and month_of(k) <= funding_to)
    first = min(have) if have else None
    daily, calls = [], 2
    todo = []
    y, m = (first if first else (2019, 9))
    while (y, m) <= (hist_to.year, hist_to.month):
        if (y, m) not in have:
            todo.append((y, m))
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)
    for ym in todo:
        _, kd = s3_list(KD + '%s/1d/%s-1d-%04d-%02d' % (sym, sym, ym[0], ym[1]), delimiter='')
        calls += 1
        daily += [k for k in kd if k.endswith('.zip')
                  and dt.date.fromisoformat(k[-14:-4]) <= hist_to]
    return monthly + sorted(daily) + funding, calls


def fetch_one(key):
    """key into STORE, verbatim, by one rename; (key, size, sha256) or (key, None, None) where the server has no such file."""
    path = os.path.join(STORE, key)
    if os.path.exists(path):
        b = read(path, 'rb')
        return key, len(b), sha256_bytes(b)
    b = request(CDN + key)
    if b is None:
        return key, None, None
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + '.tmp'
    with open(tmp, 'wb') as f:
        f.write(b)
    os.replace(tmp, path)
    return key, len(b), sha256_bytes(b)


def universe_symbols():
    """Every plain USDT perpetual of the archive's klines listing, sorted: BASEUSDT with no delivery suffix."""
    prefixes, _ = s3_list(KL)
    return sorted(s for s in (p.split('/')[-2] for p in prefixes) if re.fullmatch(r'[A-Z0-9]+USDT', s))


# ---- the local store through adv3's own readers; the series in arrays -----------------------------------------------------

class SerialPool:
    """The one method of a pool adv3.archive_funding calls, run in order."""

    @staticmethod
    def map(fn, it):
        return [fn(x) for x in it]


def local_get_for(adv3):
    def local_get(url, tries=4):
        assert url.startswith(adv3.ARCH), url
        path = STORE + '/data/futures/um/' + url[len(adv3.ARCH):]
        return read(path, 'rb') if os.path.exists(path) else None
    return local_get


def candle_rows(adv3, sym, last_day):
    """{day: (open, high, low, close, quote volume)} of one perpetual from the store, the files selected as
    adv3.archive_candles selects them - every monthly file, then the daily files of the months with no monthly file from the
    first month with data on - the quote volume (field 7) read beside the four prices."""
    ms = list(adv3.months(adv3.ARCHIVE_FROM, last_day))
    url_m = lambda ym: '%smonthly/klines/%s/1d/%s-1d-%04d-%02d.zip' % (adv3.ARCH, sym, sym, ym[0], ym[1])
    got = {ym: adv3.get(url_m(ym)) for ym in ms}
    out_ = {}
    for ym, body in got.items():
        if body is not None:
            for p in adv3.zip_rows(body):
                out_[adv3.ms_day(p[0])] = (float(p[1]), float(p[2]), float(p[3]), float(p[4]), float(p[7]))
    first_seen = min(out_) if out_ else None
    missing = [ym for ym, body in got.items() if body is None and (first_seen is None or ym >= (first_seen.year, first_seen.month))]
    days = [d for ym in missing for d in (dt.date(ym[0], ym[1], k) for k in range(1, 32) if adv3._valid(ym, k)) if d <= last_day]
    for d in days:
        body = adv3.get('%sdaily/klines/%s/1d/%s-1d-%s.zip' % (adv3.ARCH, sym, sym, d.isoformat()))
        if body is not None:
            for p in adv3.zip_rows(body):
                out_[adv3.ms_day(p[0])] = (float(p[1]), float(p[2]), float(p[3]), float(p[4]), float(p[7]))
    return {d: v for d, v in out_.items() if d <= last_day}


NONE_I, NONE_F = 9, float('nan')


class Series:
    """One contract: ordinals and prices in arrays, then the states adv3.states derives from them."""
    __slots__ = ('sym', 'ords', 'o', 'h', 'l', 'c', 'qv', 'sig', 'z', 'sm', 'U', 'ended')

    def __init__(self, sym, rows):
        days = sorted(rows)
        self.sym = sym
        self.ords = array('i', [d.toordinal() for d in days])
        self.o, self.h, self.l, self.c, self.qv = (array('d', [rows[d][k] for d in days]) for k in range(5))
        self.sig = self.sm = self.z = self.U = None
        self.ended = False

    def index(self, d):
        o = d.toordinal()
        i = bisect.bisect_left(self.ords, o)
        return i if i < len(self.ords) and self.ords[i] == o else -1


class Candles:
    """The mapping adv3.simulate, adv3.states and adv3.unit read: {day: (open, high, low, close)}."""

    def __init__(self, s):
        self.s = s

    def __iter__(self):
        return (dt.date.fromordinal(x) for x in self.s.ords)

    def __len__(self):
        return len(self.s.ords)

    def __contains__(self, d):
        return self.s.index(d) >= 0

    def __getitem__(self, d):
        i = self.s.index(d)
        if i < 0:
            raise KeyError(d)
        s = self.s
        return (s.o[i], s.h[i], s.l[i], s.c[i])


class States:
    """{day: (signal, z, sum of signs, U, close)} as adv3.states returns it, over arrays; mask, where given, lifts U to None
    on the days the contract is not admissible, which no ranking admits; a contract whose data ends before the cut is flat
    on its last day, which closes a position there."""

    def __init__(self, s, mask=None):
        self.s, self.mask = s, mask

    def __iter__(self):
        return (dt.date.fromordinal(x) for x in self.s.ords)

    def __contains__(self, d):
        return self.s.index(d) >= 0

    def __getitem__(self, d):
        s = self.s
        i = s.index(d)
        if i < 0:
            raise KeyError(d)
        u = s.U[i]
        if u != u or (self.mask is not None and not self.mask[i]):
            u = None
        z = s.z[i]
        sg = 0 if (s.ended and i == len(s.ords) - 1) else s.sig[i]
        return (None if sg == NONE_I else sg, None if z != z else z, None if s.sm[i] == NONE_I else s.sm[i], u, s.c[i])


def fill_states(adv3, s, last_day):
    """The states of s, from adv3.states over the series' own candles, into arrays."""
    st = adv3.states(Candles(s), last_day)
    n = len(s.ords)
    s.sig, s.sm = array('b', [NONE_I] * n), array('b', [NONE_I] * n)
    s.z, s.U = array('d', [NONE_F] * n), array('d', [NONE_F] * n)
    for i, o in enumerate(s.ords):
        sg, z, sm, u, _ = st[dt.date.fromordinal(o)]
        if sg is not None:
            s.sig[i] = sg
        if z is not None:
            s.z[i] = z
        if sm is not None:
            s.sm[i] = sm
        if u is not None:
            s.U[i] = u


class FundingDays:
    """The {day: sum of the day's settlements} that adv3.funding_of reads through .get, in two arrays."""

    def __init__(self, per_day):
        days = sorted(per_day)
        self.ords = array('i', [d.toordinal() for d in days])
        self.vals = array('d', [per_day[d] for d in days])

    def get(self, d, default=0.0):
        o = d.toordinal()
        i = bisect.bisect_left(self.ords, o)
        return self.vals[i] if i < len(self.ords) and self.ords[i] == o else default


def funding_for(adv3, sym, s, hist_to):
    """The rule's funding of one contract, built as adv3.history() builds it, over the store: (the function, its FundingDays)."""
    first = dt.date.fromordinal(s.ords[0])
    per_day, covered = adv3.archive_funding(sym, first, hist_to, SerialPool)
    covered = {ym for ym in covered if ym <= adv3.FUNDING_TO}
    per_day = {d: x for d, x in per_day.items() if (d.year, d.month) in covered}
    first_settle = min(per_day) if per_day else None
    fd = FundingDays(per_day)
    return adv3.funding_of(fd, lambda d, fs=first_settle, cv=covered: fs is not None and d >= fs and (d.year, d.month) in cv), fd


class Arena:
    """One file holding the arrays of every contract, written as the contracts are built and mapped read-only once it is
    sealed: the arrays are then views into the map, pages the system can take back, and the process's own memory holds the
    objects and not the prices."""
    SIZE = {'d': 8, 'i': 4, 'b': 1}

    def __init__(self, path):
        self.path, self.index, self.pos, self.view, self.mm = path, {}, 0, None, None
        self.f = open(path, 'xb')

    def add(self, key, arr):
        pad = (-self.pos) % 8
        self.f.write(b'\0' * pad)
        self.pos += pad
        self.index[key] = (self.pos, len(arr), arr.typecode)
        b = arr.tobytes()
        self.f.write(b)
        self.pos += len(b)

    def seal(self):
        import mmap
        self.f.close()
        fd = os.open(self.path, os.O_RDONLY)
        self.mm = mmap.mmap(fd, 0, access=mmap.ACCESS_READ)
        os.close(fd)
        os.unlink(self.path)               # the map keeps the file's pages; nothing is left on disk
        self.view = memoryview(self.mm)

    def get(self, key):
        off, n, tc = self.index[key]
        return self.view[off:off + n * self.SIZE[tc]].cast(tc)


# ---- the admissibility, a pure function of what the contract had traded before the day -------------------------------------

def admissible(ords, qv, v_min, window=WINDOW, span=SPAN):
    """flags[i]: True where the median quote volume of the `window` candles before ords[i] is at least v_min and the
    earliest of those lies within `span` days of ords[i]. It reads qv[i - window : i] and ords[i - window : i + 1] alone; a
    v_min of 0 admits every day."""
    n = len(ords)
    flags = array('b', bytes(n))
    if v_min <= 0:
        return array('b', [1] * n)
    for i in range(window, n):
        if ords[i] - ords[i - window] <= span and statistics.median(qv[i - window:i]) >= v_min:
            flags[i] = 1
    return flags


# ---- the statistics: pure functions ---------------------------------------------------------------------------------------

def betacf(a, b, x):
    """The continued fraction of the regularized incomplete beta function, by the modified Lentz method."""
    tiny = 1e-300
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    d = 1.0 / (d if abs(d) > tiny else tiny)
    h = d
    for m in range(1, 1000):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        d = 1.0 / (d if abs(d) > tiny else tiny)
        c = 1.0 + aa / c
        c = c if abs(c) > tiny else tiny
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        d = 1.0 / (d if abs(d) > tiny else tiny)
        c = 1.0 + aa / c
        c = c if abs(c) > tiny else tiny
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < 1e-16:
            return h
    raise ArithmeticError('betacf did not converge')


def betai(a, b, x):
    """The regularized incomplete beta function I_x(a, b)."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    lbeta = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log1p(-x)
    if x < (a + 1.0) / (a + b + 2.0):
        return math.exp(lbeta) * betacf(a, b, x) / a
    return 1.0 - math.exp(lbeta) * betacf(b, a, 1.0 - x) / b


def t_sf(t, df):
    """P(T >= t) for Student's t with df degrees of freedom."""
    p = 0.5 * betai(df / 2.0, 0.5, df / (df + t * t))
    return p if t >= 0 else 1.0 - p


def splitmix64(state):
    """(next state, output) of SplitMix64."""
    state = (state + 0x9E3779B97F4A7C15) & M64
    z = state
    z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & M64
    z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & M64
    return state, z ^ (z >> 31)


def boot_p(x, B=BOOT_B, L=BOOT_L, seed=SEED):
    """(p up, p down) of the circular block bootstrap of the mean of x: the series is centred, B resamples of ceil(n / L)
    blocks of L consecutive values (wrapping round), each block's start u = floor(r * n / 2^64) for r the next SplitMix64 output,
    the last block cut to the n values; p up = (1 + #{resampled mean >= the observed mean}) / (B + 1), p down alike with <=."""
    n = len(x)
    mean = sum(x) / n
    pre = [0.0]
    for v in [v - mean for v in x] * 2:
        pre.append(pre[-1] + v)
    nb = -(-n // L)
    last = n - L * (nb - 1)
    state, up, down = seed & M64, 0, 0
    for _ in range(B):
        tot = 0.0
        for j in range(nb):
            state, r = splitmix64(state)
            u = (r * n) >> 64
            tot += pre[u + (L if j < nb - 1 else last)] - pre[u]
        m = tot / n
        up += m >= mean
        down += m <= mean
    return (1 + up) / (B + 1), (1 + down) / (B + 1)


def mean_sd(x):
    n = len(x)
    m = sum(x) / n
    return m, math.sqrt(sum((v - m) ** 2 for v in x) / (n - 1))


def phi(z):
    return 0.5 * math.erfc(-z / math.sqrt(2.0))


def probit(p):
    """The z with phi(z) = p, by bisection to 1e-15."""
    lo, hi = -40.0, 40.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if phi(mid) < p else (lo, mid)
    return 0.5 * (lo + hi)


def read_series(x):
    """G-PIT's statistic on a monthly series: n, mean, sd, t, the Student p up and down, the bootstrap's, the word."""
    n = len(x)
    m, sd = mean_sd(x)
    if not sd > 0:
        return {'n': n, 'mean': m, 'sd': sd, 'word': 'UNDECIDABLE', 'why': 'a series with no spread'}
    t = m / (sd / math.sqrt(n))
    pu, pd = t_sf(t, n - 1), 1.0 - t_sf(t, n - 1)
    bu, bd = boot_p(x)
    word = ('REPLICATED' if pu <= ALPHA and bu <= ALPHA else 'CONTRADICTED' if pd <= ALPHA and bd <= ALPHA
            else 'UNDECIDABLE')
    return {'n': n, 'mean': m, 'sd': sd, 'sharpe_month': m / sd, 't': t, 'p_t_up': pu, 'p_t_down': pd,
            'p_boot_up': bu, 'p_boot_down': bd, 'word': word}


def power(sharpe, n, alpha=ALPHA):
    """The normal approximation of the power of the one-sided test of a mean at the level alpha, n months of Sharpe ratio
    `sharpe` a month: phi(sharpe * sqrt(n) - z(1 - alpha))."""
    return phi(sharpe * math.sqrt(n) - probit(1.0 - alpha))


def monthly(S, N, hist_to, min_coins=MIN_COINS):
    """[(year, month, x, mean N)] of the calendar months whose last day is hist_to or before and whose mean number of admissible
    coins a day is min_coins or more; x is the month's sum of S[day] / N[day] over the days with N[day] > 0. S and N are
    keyed by ordinal."""
    import calendar
    rows = []
    if not N:
        return rows
    first = dt.date.fromordinal(min(N))
    y, m = first.year, first.month
    while (y, m) <= (hist_to.year, hist_to.month):
        nd = calendar.monthrange(y, m)[1]
        d0 = dt.date(y, m, 1).toordinal()
        if dt.date(y, m, nd) <= hist_to:
            days = range(d0, d0 + nd)
            mean_n = sum(N.get(o, 0) for o in days) / nd
            if mean_n >= min_coins:
                rows.append((y, m, sum(S.get(o, 0.0) / N[o] for o in days if N.get(o, 0) > 0), mean_n))
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)
    return rows


def monthly_sum(R, rows):
    """The month sums of R (keyed by ordinal) over the months of rows, in rows' order."""
    import calendar
    return [sum(R.get(o, 0.0) for o in range(dt.date(y, m, 1).toordinal(), dt.date(y, m, 1).toordinal() + calendar.monthrange(y, m)[1]))
            for y, m, _x, _n in rows]


# ---- the advisor's functions over the series -------------------------------------------------------------------------------

@contextlib.contextmanager
def patched(mod, **attrs):
    """Module attributes replaced for the block and restored after it, whatever happens."""
    old = {k: getattr(mod, k) for k in attrs}
    for k, v in attrs.items():
        setattr(mod, k, v)
    try:
        yield
    finally:
        for k, v in old.items():
            setattr(mod, k, v)


@contextlib.contextmanager
def gated(adv3, s, mask):
    """adv3.unit lifted to None on the days of s that mask does not admit: no entry opens there and no ranking admits the
    contract. adv3.states and adv3.simulate call unit by its module name, so the block reaches both. A mask of None changes
    nothing."""
    if mask is None:
        yield
        return
    orig = adv3.unit

    def unit(c, days, i):
        j = s.index(days[i])
        return orig(c, days, i) if j >= 0 and mask[j] else None
    with patched(adv3, unit=unit):
        yield


@contextlib.contextmanager
def recording(adv3):
    """adv3.hold wrapped so that each position keeps, in an array, the pairs (ordinal, R after the day) of its days held."""
    orig = adv3.hold

    def hold(pos, candle, pc, fund_d, day):
        r, stopped = orig(pos, candle, pc, fund_d, day)
        path = pos.get('path')
        if path is None:
            path = pos['path'] = array('d')
        path.extend((float(day.toordinal()), pos['R']))
        return r, stopped
    with patched(adv3, hold=hold):
        yield


def end_trade(adv3, s, pos, why):
    """A position open at the end of a contract's data, closed at its last close with one exit cost, as adv3.history() closes
    one at the cut; the trade and the cost in R."""
    cost = adv3.COST * s.c[-1] / pos['U']
    return dict(pos, R=pos['R'] - cost, why=why, end=dt.date.fromordinal(s.ords[-1])), cost


def rule_pass(adv3, series, funds, masks, hist_to, order=None, record=False):
    """The rule on each series of `order`, sorted by default. Returns trades (each with its coin), the daily R summed over the contracts
    as adv3.history() sums it ('facts'), the same with the exit cost of each position closed at the end of data on its last
    day ('gate'), and N, the number of contracts a day that are admissible and have a signal."""
    trades, facts, gate, N = [], {}, {}, {}
    for sym in (sorted(series) if order is None else order):
        s = series[sym]
        mask = masks.get(sym)
        with gated(adv3, s, mask), (recording(adv3) if record else contextlib.nullcontext()):
            th, dh, ph = adv3.simulate(Candles(s), funds[sym], dt.date.fromordinal(s.ords[0]), hist_to)
        why = 'delisted' if s.ended else 'open at the history cut'
        extra = None
        if ph:
            t, cost = end_trade(adv3, s, ph, why)
            th = th + [t]
            extra = (s.ords[-1], cost)
        for t in th:
            t['coin'] = sym
        trades += th
        for d, x in dh.items():
            o = d.toordinal()
            facts[o] = facts.get(o, 0.0) + x
            gate[o] = gate.get(o, 0.0) + x
        if extra:
            gate[extra[0]] = gate.get(extra[0], 0.0) - extra[1]
        for i, o in enumerate(s.ords):
            if s.sig[i] != NONE_I and (mask is None or mask[i]):
                N[o] = N.get(o, 0) + 1
    return {'trades': trades, 'facts': facts, 'gate': gate, 'N': N}


def strong_pass(adv3, series, funds, masks, syms, hist_to, top_n=3, strong_max=3, record=False):
    """The STRONG strategy over syms (their order is the ranking's tie order): trades, daily R, and the positions the data
    ends on, closed as adv3.history() closes them at the cut. A contract whose data ends before the cut is flat on its last day,
    which closes a position there."""
    cs = {k: Candles(series[k]) for k in syms}
    st = {k: States(series[k], masks.get(k)) for k in syms}
    first = dt.date.fromordinal(min(series[k].ords[0] for k in syms))
    with patched(adv3, COINS=tuple(syms), TOP_N=top_n, STRONG_MAX=strong_max), \
            (recording(adv3) if record else contextlib.nullcontext()):
        trades, daily, open_ = adv3.simulate_strong(cs, st, funds, first, hist_to)
    for coin, t in open_.items():
        tr, _cost = end_trade(adv3, series[coin], t, 'open at the history cut')
        trades.append(tr)
    return {'trades': trades, 'daily': {d.toordinal(): x for d, x in daily.items()}}


# ---- the tables: pure readings of trades and series ----------------------------------------------------------------------------

def stat_block(adv3, trades, daily):
    """adv3.stats of one strategy, with the history's own additions: the share of the five best trades in the total, the
    mean R without the best 1 % of the trades, the long and short parts, the stops hit."""
    x = adv3.stats(trades, daily)
    R = sorted((t['R'] for t in trades), reverse=True)
    x['top5_share'] = sum(R[:5]) / x['total_R'] if x['total_R'] > 0 else None
    cut = max(1, math.ceil(0.01 * len(R))) if R else 0
    x['mean_R_ex_top1pct'] = sum(R[cut:]) / (len(R) - cut) if len(R) > cut else None
    for name, side in (('long', 1), ('short', -1)):
        part = [t['R'] for t in trades if t['d'] == side]
        x[name] = {'trades': len(part), 'total_R': sum(part), 'mean_R': sum(part) / len(part) if part else None}
    x['stops'] = sum(t.get('why') == 'stop' for t in trades)
    return x


def exit_of(t):
    """The day a trade ended: its exit, or the last day of the data for a position closed there."""
    return t['exit'] if 'exit' in t else t['end']


def by_year(trades):
    out_ = {}
    for t in trades:
        y = exit_of(t).year
        a = out_.setdefault(y, [0, 0.0])
        a[0] += 1
        a[1] += t['R']
    return {str(y): {'trades': n, 'total_R': r} for y, (n, r) in sorted(out_.items())}


def bucket_table(trades, key, edges, labels):
    """Trades grouped by key(trade) into the buckets edges cut: [(label, n, mean R, total R, share in profit)]."""
    rows = [[lab, 0, 0.0, 0] for lab in labels]
    for t in trades:
        k = bisect.bisect_left(edges, key(t))
        rows[k][1] += 1
        rows[k][2] += t['R']
        rows[k][3] += t['R'] > 0
    return [{'bucket': lab, 'trades': n, 'total_R': r, 'mean_R': r / n if n else None, 'wins': w}
            for lab, n, r, w in rows]


def stop_pct(t):
    return 100.0 * t['U'] / t['E']


def rank_at(series, syms, masks, day, coin):
    """The coin's place in the day's ranking by |z| among the contracts that are active, admissible and have a signal, ties by
    syms' order, as adv3.ranking orders them."""
    act = []
    for k in syms:
        s = series[k]
        i = s.index(day)
        if i < 0:
            continue
        z, u = s.z[i], s.U[i]
        if s.sig[i] in (1, -1) and z == z and u == u and (masks.get(k) is None or masks[k][i]):
            act.append((-abs(z), k))
    act.sort(key=lambda a: a[0])
    return [k for _z, k in act].index(coin) + 1


def weakening(adv3, trades, series):
    """Of the trades entered with all four signs agreeing, those whose sum of signs fell to +/-2 while the signal held: the R
    they made after that close, against the R of leaving at it. delta = R_final - (R at the close - the exit cost in R)."""
    n4, rows, never = 0, [], []
    for t in trades:
        path = t.get('path')
        if path is None:
            continue
        s = series[t['coin']]
        j0 = s.index(t['entry'])
        if j0 < 0 or s.sm[j0] == NONE_I or abs(s.sm[j0]) != 4:
            continue
        n4 += 1
        stop_day = t['exit'].toordinal() if t.get('why') == 'stop' else None
        hit = None
        for k in range(0, len(path), 2):
            o = int(path[k])
            j = s.index(dt.date.fromordinal(o))
            if o == stop_day:
                break
            if j >= 0 and s.sig[j] == t['d'] and s.sm[j] != NONE_I and abs(s.sm[j]) == 2:
                hit = (path[k + 1], s.c[j])
                break
        if hit is None:
            never.append(t['R'])
            continue
        r_at, close = hit
        rows.append((t['R'] - (r_at - adv3.COST * close / t['U']), t['R'] - r_at))
    d = sorted(x for x, _ in rows)
    return {'entered_with_four_signs': n4, 'weakened': len(rows), 'never_weakened': len(never),
            'mean_R_never_weakened': sum(never) / len(never) if never else None,
            'mean_R_after': sum(a for _, a in rows) / len(rows) if rows else None,
            'mean_hold_minus_exit': sum(d) / len(d) if d else None,
            'median_hold_minus_exit': d[len(d) // 2] if d else None,
            'share_hold_better': sum(x > 0 for x in d) / len(d) if d else None}


def trade_csv(trades, rank=None):
    """The trades as CSV text, sorted by entry then coin: forensic reconstruction of any row without re-running."""
    head = 'coin,side,entry,exit,why,R,mfe_R,stop_pct' + (',rank' if rank else '') + '\n'
    rows = []
    for t in sorted(trades, key=lambda t: (t['entry'], t['coin'])):
        rows.append('%s,%d,%s,%s,%s,%r,%r,%r%s\n' % (t['coin'], t['d'], t['entry'], exit_of(t), t.get('why', ''), t['R'],
                                                    t['mfe'], stop_pct(t), (',%d' % rank[(t['coin'], t['entry'])]) if rank else ''))
    return head + ''.join(rows)


def series_csv(rows, extra=None):
    head = 'year,month,x,mean_coins' + (',strong_R' if extra else '') + '\n'
    return head + ''.join('%d,%d,%r,%r%s\n' % (y, m, x, n, (',%r' % extra[i]) if extra else '') for i, (y, m, x, n) in enumerate(rows))


# ---- the plan, the fetch and the probe -------------------------------------------------------------------------------------

def mode_probe():
    """G-PATH: one request to each endpoint through request(), each asserted served and parsed, before the bulk begins."""
    import zipfile
    _, keys = s3_list(KL + 'BTCUSDT/1d/')
    assert len([k for k in keys if k.endswith('.zip')]) >= 80, 'klines listing'
    out('P-LIST served: %d keys under %sBTCUSDT/1d/' % (len(keys), KL))
    for name, key in (('P-MONTHLY', KL + 'BTCUSDT/1d/BTCUSDT-1d-2024-01.zip'), ('P-DAILY', KD + 'BTCUSDT/1d/BTCUSDT-1d-2024-01-15.zip'),
                      ('P-FUNDING', FU + 'BTCUSDT/BTCUSDT-fundingRate-2024-01.zip')):
        body = request(CDN + key)
        assert body is not None, name
        z = zipfile.ZipFile(io.BytesIO(body))
        rows = [l.split(',') for l in z.read(z.namelist()[0]).decode().splitlines() if l[:1].isdigit()]
        assert rows, name
        out('%s served: %s, %d bytes, %d rows' % (name, key, len(body), len(rows)))
    out('READING P-START: served - 4 of 4 endpoints')


def mode_plan(hist_to):
    os.makedirs(WORK, exist_ok=True)
    syms = universe_symbols()
    with ThreadPoolExecutor(12) as pool:
        res = list(pool.map(lambda s: plan_symbol(s, hist_to, (2026, 9)), syms))
    plan = {'hist_to': str(hist_to), 'symbols': syms, 'keys': {s: r[0] for s, r in zip(syms, res)},
            'listing_calls': sum(r[1] for r in res)}
    text = json.dumps(plan, sort_keys=True, indent=0) + '\n'
    with open(WORK + '/plan.json', 'x', encoding='utf-8') as f:
        f.write(text)
    out('PLAN: %d symbols, %d keys, %d listing calls; plan.json %d bytes SHA-256 %s' % (
        len(syms), sum(len(v) for v in plan['keys'].values()), plan['listing_calls'], len(text.encode()), sha256_bytes(text.encode())))


def mode_fetch():
    plan = json.loads(read(WORK + '/plan.json'))
    keys = sorted({k for v in plan['keys'].values() for k in v})
    del plan
    t0, done, absent, total = time.time(), 0, [], 0
    h = hashlib.sha256()
    with ThreadPoolExecutor(16) as pool, open(WORK + '/manifest.tsv', 'x', encoding='utf-8') as mf:
        for text in ('key\tbytes\tsha256\n',):
            mf.write(text)
            h.update(text.encode())
        for lo in range(0, len(keys), 2000):
            lines = []
            for key, size, sha in pool.map(fetch_one, keys[lo:lo + 2000]):
                done += 1
                if size is None:
                    absent.append(key)
                else:
                    lines.append('%s\t%d\t%s\n' % (key, size, sha))
                    total += size
            text = ''.join(lines)
            mf.write(text)
            h.update(text.encode())
            if done % 10000 == 0:
                out('fetched %d of %d in %.0f s' % (done, len(keys), time.time() - t0))
    assert not absent, 'planned keys the server does not serve: %r' % absent[:5]
    out('FETCH PASS: %d files, %d bytes in %.0f s; manifest.tsv %d bytes SHA-256 %s' % (
        done, total, time.time() - t0, os.path.getsize(WORK + '/manifest.tsv'), h.hexdigest()))


# ---- the run ------------------------------------------------------------------------------------------------------------------

LISTED_TO = dt.date(2025, 11, 30)    # the universe L: contracts whose first candle is on or before this day
EXCLUDED_BASES = ('USDC',)            # a contract pegged to the dollar has no trend to follow
MIN_MONTHS = 24


def load_all(adv3, plan, hist_to, arena=None):
    """{symbol: Series}, {symbol: funding}, {V: {symbol: flags}} of every contract of the plan that has candles, was listed by
    LISTED_TO and is admissible on some day at the lowest V of the run - or is the Boss's. The quote volumes are dropped once
    the flags are made; with an arena the arrays go to its file and come back as views once it is sealed."""
    vs = (V_MIN,) + V_SENS
    lowest = min(vs)
    boss = {c + 'USDT' for c in adv3.COINS}
    series, funds, masks, fds = {}, {}, {v: {} for v in vs}, {}
    names = ('ords', 'o', 'h', 'l', 'c', 'sig', 'z', 'sm', 'U')
    for sym in plan['symbols']:
        rows = candle_rows(adv3, sym, hist_to)
        if not rows:
            continue
        s = Series(sym, rows)
        del rows
        s.ended = dt.date.fromordinal(s.ords[-1]) < hist_to
        if not (sym in boss or (sym[:-4] not in EXCLUDED_BASES and dt.date.fromordinal(s.ords[0]) <= LISTED_TO
                                and any(admissible(s.ords, s.qv, lowest)))):
            continue
        fill_states(adv3, s, hist_to)
        for v in vs:
            masks[v][sym] = admissible(s.ords, s.qv, v)
        s.qv = None
        funds[sym], fds[sym] = funding_for(adv3, sym, s, hist_to)
        series[sym] = s
        if arena is not None:
            for nm in names:
                arena.add((sym, nm), getattr(s, nm))
                setattr(s, nm, None)
            for v in vs:
                arena.add((sym, 'mask', v), masks[v][sym])
                masks[v][sym] = None
            arena.add((sym, 'f_ords'), fds[sym].ords)
            arena.add((sym, 'f_vals'), fds[sym].vals)
            fds[sym].ords = fds[sym].vals = None
    if arena is not None:
        arena.seal()
        for sym, s in series.items():
            for nm in names:
                setattr(s, nm, arena.get((sym, nm)))
            for v in vs:
                masks[v][sym] = arena.get((sym, 'mask', v))
            fds[sym].ords, fds[sym].vals = arena.get((sym, 'f_ords')), arena.get((sym, 'f_vals'))
    return series, funds, masks


def facts_shape(adv3, rule, strong):
    """adv3.history()'s h, from the passes of the Boss's 42 with no admissibility."""
    to_date = lambda d: {dt.date.fromordinal(o): x for o, x in d.items()}
    base, st = adv3.stats(rule['trades'], to_date(rule['facts'])), adv3.stats(strong['trades'], to_date(strong['daily']))
    for x, tr in ((base, rule['trades']), (st, strong['trades'])):
        x['top5_share'] = sum(sorted((t['R'] for t in tr), reverse=True)[:5]) / x['total_R'] if x['total_R'] > 0 else None
    base['gate_H'] = 'NOT DISQUALIFIED' if base['total_R'] > 0 else 'DISQUALIFIED'
    st['gate_S'] = 'NOT DISQUALIFIED' if st['total_R'] > 0 and st['mean_R'] > base['mean_R'] else 'DISQUALIFIED'
    return {'base': base, 'strong': st}


PEAK_ANON = [0]


def proc_mem():
    """The process's memory now, from /proc/self/status: resident, of it anonymous (its own heap) and file-backed (the map's
    pages, which the system can take back), and the high-water mark of the resident set; the largest anonymous figure read so far
    is kept in PEAK_ANON."""
    d = {}
    for line in read('/proc/self/status').splitlines():
        if line.split(':')[0] in ('VmRSS', 'RssAnon', 'RssFile', 'VmHWM'):
            d[line.split(':')[0]] = int(line.split()[1]) * 1024
    PEAK_ANON[0] = max(PEAK_ANON[0], d.get('RssAnon', 0))
    return 'resident %(VmRSS)d (anon %(RssAnon)d, file %(RssFile)d), high-water %(VmHWM)d' % d


def start_sampler(interval=0.05):
    """A thread that reads proc_mem() every `interval` s, so that PEAK_ANON is the largest anonymous set of the whole run and not of
    the instants the phases happen to log. Returns the event that stops it."""
    stop = threading.Event()

    def loop():
        while not stop.is_set():
            try:
                proc_mem()
            except (OSError, KeyError, ValueError):
                pass
            stop.wait(interval)
    threading.Thread(target=loop, daemon=True).start()
    return stop


def malloc_tune():
    """glibc's mmap threshold at 128 KiB and its arenas at two, as the project's long-lived units fix them; True if glibc took both."""
    try:
        import ctypes
        libc = ctypes.CDLL('libc.so.6')
        return libc.mallopt(-3, 131072) == 1 and libc.mallopt(-8, 2) == 1
    except OSError:
        return False


def g_data(adv3, boss, hist_to, log):
    """G-DATA: the store's candles, read by candle_rows and read by adv3.archive_candles, equal day for day for the Boss's 42."""
    same = 0
    for sym in boss:
        mine = candle_rows(adv3, sym, hist_to)
        theirs = adv3.archive_candles(sym, hist_to, SerialPool)
        same += bool(mine) and {d: v[:4] for d, v in mine.items()} == theirs
    log('READING G-DATA: %s - %d of %d' % ('PASS' if same == len(boss) else 'FAIL', same, len(boss)))
    assert same == len(boss), 'G-DATA'


def g_equal(adv3, series, funds, boss, hist_to, log, exact):
    """G-EQUAL: the pipeline over the Boss's 42, no admissibility, read against the frozen FACTS (20 checks) and, where `exact`,
    against adv3.history() on the same store, block for block (2 checks). Returns (the passes, h)."""
    rule_a = rule_pass(adv3, series, funds, {}, hist_to, order=boss)
    strong_a = strong_pass(adv3, series, funds, {}, boss, hist_to)
    mine = facts_shape(adv3, rule_a, strong_a)
    checks = adv3.facts_checks(mine)
    if exact:
        ref = adv3.history()
        checks['base block equals history()'] = mine['base'] == ref['base']
        checks['strong block equals history()'] = mine['strong'] == ref['strong']
    n_ok = sum(1 for v in checks.values() if (v[0] if isinstance(v, tuple) else v))
    log('READING G-EQUAL: %s - %d of %d%s' % ('PASS' if n_ok == len(checks) else 'FAIL', n_ok, len(checks),
                                              '' if exact else ' (FACTS alone)'))
    assert n_ok == len(checks), 'G-EQUAL'
    return rule_a, mine


def run_prepare(adv3, plan, hist_to, log=out):
    t0 = time.time()
    stamp = lambda: '%.0f s, %s' % (time.time() - t0, proc_mem())
    adv3.get = local_get_for(adv3)
    boss = [c + 'USDT' for c in adv3.COINS]
    g_data(adv3, boss, hist_to, log)
    series, funds, masks = load_all(adv3, plan, hist_to, Arena(WORK + '/arena.bin'))
    trim()
    log('loaded %d contracts: %s' % (len(series), stamp()))
    assert all(boss_sym in series and not series[boss_sym].ended for boss_sym in boss), 'a contract of the Boss\'s 42 is absent or ended'
    listed = [k for k, s in series.items() if k[:-4] not in EXCLUDED_BASES and dt.date.fromordinal(s.ords[0]) <= LISTED_TO]
    L = sorted(k for k in listed if any(masks[V_MIN][k]))
    G = [k for k in L if k not in set(boss)]
    log('sets: Boss %d, universe L %d, gate set G %d: %s' % (len(boss), len(L), len(G), stamp()))
    res = {'sets': {'boss': len(boss), 'L': len(L), 'G': len(G), 'ended_in_L': sum(series[k].ended for k in L), 'loaded': len(series)}}
    rule_a, mine = g_equal(adv3, series, funds, boss, hist_to, log, exact=False)
    res['facts_42'] = {k: dict(v) for k, v in mine.items()}
    return {'res': res, 'series': series, 'funds': funds, 'masks': masks, 'boss': boss, 'L': L, 'G': G, 'listed': listed,
            'rule_a': rule_a, 'stamp': stamp, 'hist_to': hist_to, 'log': log}


def mode_equal():
    """G-EQUAL's exact reading, in a process of its own: the Boss's 42 alone, the pipeline against FACTS and against history()."""
    adv3 = load_adv3()
    plan = json.loads(read(WORK + '/plan.json'))
    hist_to = dt.date.fromisoformat(plan['hist_to'])
    adv3.get = local_get_for(adv3)
    boss = [c + 'USDT' for c in adv3.COINS]
    g_data(adv3, boss, hist_to, out)
    series, funds = {}, {}
    for sym in boss:
        series[sym] = Series(sym, candle_rows(adv3, sym, hist_to))
        fill_states(adv3, series[sym], hist_to)
        funds[sym] = funding_for(adv3, sym, series[sym], hist_to)[0]
    g_equal(adv3, series, funds, boss, hist_to, out, exact=True)
    out('EQUAL PASS: peak resident %d bytes' % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024))


def trim():
    """Free pages glibc holds back: the memory a finished phase released goes to the system before the next one starts."""
    import ctypes, gc
    gc.collect()
    try:
        ctypes.CDLL('libc.so.6').malloc_trim(0)
    except OSError:
        pass


def word_or_short(x):
    if len(x) < MIN_MONTHS:
        return {'n': len(x), 'word': 'UNDECIDABLE', 'why': 'fewer than %d months' % MIN_MONTHS}
    return read_series(x)


def run_measure(adv3, ctx):
    """The readings over the prepared series. Returns the result dictionary and the files to write. Nothing here is a gate of
    this TZ: the reading of the rule on G is the Architect's exploration, re-derived (TZ section 4.2), and moves no rung."""
    res, series, funds, masks, boss, L, G = (ctx[k] for k in ('res', 'series', 'funds', 'masks', 'boss', 'L', 'G'))
    hist_to, log, stamp, listed = ctx['hist_to'], ctx['log'], ctx['stamp'], ctx['listed']
    Mv = masks[V_MIN]
    to_date = lambda d: {dt.date.fromordinal(o): x for o, x in d.items()}
    files = {}
    bset = set(boss)
    # -- the rule, then STRONG, on G: the contracts outside the Boss's 42
    rule_g = rule_pass(adv3, series, funds, Mv, hist_to, order=G)
    rows_g = monthly(rule_g['gate'], rule_g['N'], hist_to)
    gp = word_or_short([r[2] for r in rows_g])
    gp['trades'] = len(rule_g['trades'])
    gp['by_year'] = by_year(rule_g['trades'])
    gp['block'] = stat_block(adv3, rule_g['trades'], to_date(rule_g['facts']))
    del rule_g
    trim()
    strong_g = strong_pass(adv3, series, funds, Mv, G, hist_to)
    gs = word_or_short(monthly_sum(strong_g['daily'], rows_g))
    gs['trades'] = len(strong_g['trades'])
    gs['block'] = stat_block(adv3, strong_g['trades'], to_date(strong_g['daily']))
    xs_g = monthly_sum(strong_g['daily'], rows_g)
    del strong_g
    trim()
    log('phase G done: %s' % stamp())
    rows_a = monthly(ctx['rule_a']['gate'], ctx['rule_a']['N'], hist_to)
    xa = [r[2] for r in rows_a]
    ma, sa = mean_sd(xa)
    gp['alternative'] = {'boss_42_months': len(xa), 'boss_42_mean': ma, 'boss_42_sharpe_month': ma / sa,
                         'power_at_boss_42_sharpe': power(ma / sa, len(rows_g)), 'power_at_half': power(ma / sa / 2, len(rows_g)),
                         'power_at_own_sharpe': power(gp['sharpe_month'], len(rows_g)) if 'sharpe_month' in gp else None}
    gp['months'] = '%d-%02d to %d-%02d' % (rows_g[0][:2] + rows_g[-1][:2]) if rows_g else None
    gp['mean_coins'] = [min(r[3] for r in rows_g), max(r[3] for r in rows_g)] if rows_g else None
    res['pit_rule'], res['pit_strong'] = gp, gs
    log('PIT rule on G (exploratory, moves no rung): the procedure reads %s - %d months, mean %.6f R a coin-month, t %.3f, p(t) up %.5f, '
        'p(boot) up %.5f; %d trades on %d contracts: %s' % (gp['word'], gp['n'], gp.get('mean', float('nan')), gp.get('t', float('nan')),
                                                          gp.get('p_t_up', float('nan')), gp.get('p_boot_up', float('nan')), gp['trades'], len(G), stamp()))
    log('PIT STRONG on G (exploratory): the procedure reads %s - %d months, mean %.4f R a month, t %.3f, p(t) up %.5f, p(boot) up %.5f; %d trades'
        % (gs['word'], gs['n'], gs.get('mean', float('nan')), gs.get('t', float('nan')), gs.get('p_t_up', float('nan')),
           gs.get('p_boot_up', float('nan')), gs['trades']))
    files['monthly-G.csv'] = series_csv(rows_g, xs_g)
    files['monthly-A.csv'] = series_csv(rows_a)
    # -- sensitivity of the rule's reading to V
    sens = []
    for v in V_SENS:
        Gv = sorted(k for k in listed if k not in bset and any(masks[v][k]))
        rv = rule_pass(adv3, series, funds, masks[v], hist_to, order=Gv)
        rr = monthly(rv['gate'], rv['N'], hist_to)
        sens.append(dict(word_or_short([r[2] for r in rr]), V=v, contracts=len(Gv), trades=len(rv['trades'])))
        del rv
    res['sensitivity'] = sens
    for s_ in sens:
        log('sensitivity V %.0f: %s - %d contracts, %d trades, n %d, mean %s, p(t) up %s' % (
            s_['V'], s_['word'], s_['contracts'], s_['trades'], s_['n'], s_.get('mean'), s_.get('p_t_up')))
    log('phase sensitivity done: %s' % stamp())
    # -- P: every admissible contract of L, the Boss's included
    rule_p = rule_pass(adv3, series, funds, Mv, hist_to, order=L)
    res['P_rule'] = stat_block(adv3, rule_p['trades'], to_date(rule_p['facts']))
    res['P_rule']['by_year'] = by_year(rule_p['trades'])
    files['trades-P-rule.csv'] = trade_csv(rule_p['trades'])
    del rule_p
    trim()
    log('phase P rule done: %s' % stamp())
    variants = {}
    for n in (3, 5, 7):
        sp = strong_pass(adv3, series, funds, Mv, L, hist_to, top_n=n, strong_max=n, record=(n == 3))
        blk = stat_block(adv3, sp['trades'], to_date(sp['daily']))
        blk['by_year'] = by_year(sp['trades'])
        blk['stop_buckets'] = bucket_table(sp['trades'], stop_pct, [11.1, 14.0], ['<=11.1%', '11.1-14%', '>14%'])
        ranks = {(t['coin'], t['entry']): rank_at(series, L, Mv, t['entry'], t['coin']) for t in sp['trades']}
        blk['rank_buckets'] = bucket_table(sp['trades'], lambda t, r=ranks: r[(t['coin'], t['entry'])], [3, 5], ['1-3', '4-5', '6-7'])
        if n == 3:
            blk['weakening'] = weakening(adv3, sp['trades'], series)
        variants['top%d' % n] = blk
        files['trades-P-strong-%d.csv' % n] = trade_csv(sp['trades'], ranks)
        del sp, ranks
        trim()
    res['P_strong'] = variants
    log('phase P strong done: %s' % stamp())
    # -- the Boss's 42 with the same admissibility, and the random lists
    rule_a2 = rule_pass(adv3, series, funds, Mv, hist_to, order=boss)
    strong_a2 = strong_pass(adv3, series, funds, Mv, boss, hist_to)
    res['A_admissible'] = {'rule': stat_block(adv3, rule_a2['trades'], to_date(rule_a2['facts'])),
                           'strong': stat_block(adv3, strong_a2['trades'], to_date(strong_a2['daily']))}
    del rule_a2, strong_a2
    state, draws = (SEED * 2 + 1) & M64, []
    for k in range(RANDOM_LISTS):
        idx = list(range(len(L)))
        for i in range(LIST_SIZE):
            state, r = splitmix64(state)
            j = i + ((r * (len(idx) - i)) >> 64)
            idx[i], idx[j] = idx[j], idx[i]
        syms = sorted(L[t] for t in idx[:LIST_SIZE])
        sp = strong_pass(adv3, series, funds, Mv, syms, hist_to)
        R = [t['R'] for t in sp['trades']]
        longs = [t['R'] for t in sp['trades'] if t['d'] > 0]
        draws.append((k, len(R), sum(R), sum(R) / len(R) if R else 0.0, len(longs), sum(longs)))
        del sp
        if k % 50 == 0:
            stamp()
    tot = sorted(d[2] for d in draws)
    ref_total = res['A_admissible']['strong']['total_R']
    q = lambda p: tot[min(len(tot) - 1, int(p * len(tot)))]
    res['random_lists'] = {'lists': RANDOM_LISTS, 'size': LIST_SIZE, 'pool': len(L),
                           'total_R_quantiles': {str(p): q(p) for p in (0.05, 0.25, 0.5, 0.75, 0.95)},
                           'share_total_positive': sum(x > 0 for x in tot) / len(tot),
                           'boss_42_total_R': ref_total,
                           'share_of_lists_below_boss_42': sum(x < ref_total for x in tot) / len(tot),
                           'mean_R_trade_quantiles': {str(p): sorted(d[3] for d in draws)[min(len(draws) - 1, int(p * len(draws)))]
                                                      for p in (0.05, 0.25, 0.5, 0.75, 0.95)},
                           'share_mean_R_positive': sum(d[3] > 0 for d in draws) / len(draws),
                           'trades_median': sorted(d[1] for d in draws)[len(draws) // 2]}
    files['random-lists.csv'] = 'list,trades,total_R,mean_R,long_trades,long_total_R\n' + ''.join('%d,%d,%r,%r,%d,%r\n' % d for d in draws)
    log('random lists: %s' % json.dumps(res['random_lists'], sort_keys=True))
    log('finished: %s' % stamp())
    return res, files


# ---- the checker: the map, the host, the number, the marks and the keep ------------------------------------------------------------

CAPTURES = ('btc-recorder.service', 'btc-pairbook.service', 'btc-rewardbook.service')
BOT = 'adv3-bot.service'
PY = '/root/tz04a-env/venv/bin/python'
STATE = WORK + '/state.json'


def show(unit, *props):
    rc, so, se = sh(['systemctl', 'show', unit] + [a for p in props for a in ('-p', p)], env=dict(os.environ, TZ='UTC'))
    assert rc == 0, se
    return dict(line.split('=', 1) for line in so.splitlines() if '=' in line)


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
    checks['advisor/adv3.py hashes to the SHA-256 the instrument loads it by, ' + ADV3_SHA[:8]] = sha256_file(PRIMARY + '/advisor/adv3.py') == ADV3_SHA
    verdict('FINGERPRINT', checks)


def meminfo():
    return {k: int(v.split()[0]) * 1024 for k, v in (l.split(':', 1) for l in read('/proc/meminfo').splitlines())}


def memory_gate(first, second):
    final = first if first >= MEM_FLOOR or second is None else second
    return final >= MEM_FLOOR, final


def mode_host():
    checks = {}
    rc, so, _ = sh(['find', '/var/lib/btc-recorder', '-mindepth', '1', '-maxdepth', '3', '-name', 'manifest.json', '-print', '-quit'])
    checks["H1 the recorder's manifest.json is found"] = rc == 0 and len(so.split()) == 1
    rc, so, _ = sh(['df', '-B1', '--output=source,size,avail', '/var/lib/btc-recorder'])
    src, size, avail = so.splitlines()[1].split()
    checks['H2 /dev/vda2 of 31612203008 bytes'] = (src, size) == ('/dev/vda2', '31612203008')
    rc, so, _ = sh(['grep', '-c', 'e3975b5da44c5328adf3bf3914634cd878842c73', '/var/lib/btc-recorder/runtime.jsonl'])
    checks["H2 the recorder's runtime record names e3975b5"] = rc == 0 and int(so) >= 1
    rc, so, _ = sh([PY, '-c', 'import sys; print(sys.version.split()[0])'])
    checks['H3 the venv interpreter is Python 3.12'] = rc == 0 and so.startswith('3.12.')
    units = {u: show(u, 'MainPID', 'NRestarts', 'ActiveState', 'SubState', 'UnitFileState') for u in CAPTURES + (BOT,)}
    for u in CAPTURES:
        checks['H4 %s active and enabled' % u] = (units[u]['ActiveState'], units[u]['UnitFileState']) == ('active', 'enabled')
    checks['H5 adv3-bot.service active, running and enabled'] = (
        (units[BOT]['ActiveState'], units[BOT]['SubState'], units[BOT]['UnitFileState']) == ('active', 'running', 'enabled'))
    checks['H6 the work tree holds nothing but logs/ and stage/'] = not os.path.exists(WORK) or set(os.listdir(WORK)) <= {'logs', 'stage'}
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
    out('MemAvailable first %d bytes, second %s, deciding %d; /dev/vda2 free %s bytes' % (
        first, 'not read' if second is None else second, final, avail))
    verdict('HOST', checks)


def number_reading(names):
    return {'CryptoTZ/ holds %s and no other file of that number' % TZ_FILE:
            [n for n in names if n.startswith('CryptoTZ/' + NUMBER)] == [TZ_FILE],
            'CryptoReports/ holds no report of that number': not [n for n in names if n.startswith('CryptoReports/' + NUMBER)]}


def mode_number():
    rc, so, se = sh(['git', '-C', PRIMARY, 'ls-tree', '--name-only', 'origin/main', '--', 'CryptoTZ/', 'CryptoReports/'])
    assert rc == 0, se
    names = so.split('\n')
    for n in names:
        if n.startswith('CryptoTZ/' + NUMBER) or n.startswith('CryptoReports/' + NUMBER):
            out(n)
    verdict('NUMBER', number_reading(names))


def snapshot():
    return {u: show(u, 'MainPID', 'NRestarts', 'ActiveState', 'UnitFileState') for u in CAPTURES + (BOT,)}


def mode_mark():
    os.makedirs(WORK, exist_ok=True)
    snap = snapshot()
    with open(STATE, 'x', encoding='utf-8') as f:
        f.write(json.dumps({'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'units': snap}, indent=1, sort_keys=True) + '\n')
    out('MARK', json.dumps(snap, sort_keys=True))


def still_reading(before, now):
    checks = {}
    for u in CAPTURES + (BOT,):
        checks['%s unchanged: MainPID, NRestarts, ActiveState, UnitFileState' % u] = before.get(u) == now.get(u) and now[u]['ActiveState'] == 'active'
    return checks


def mode_still():
    verdict('STILL', still_reading(json.loads(read(STATE))['units'], snapshot()))


def mode_same(a, b):
    """DETERMINISM: every file of two output directories equal by SHA-256, the same names in both."""
    fa, fb = sorted(os.listdir(a)), sorted(os.listdir(b))
    checks = {'the same %d file names' % len(fa): fa == fb}
    for f in fa:
        ha, hb = sha256_file(a + '/' + f), sha256_file(b + '/' + f) if f in fb else None
        out('%s %s %s' % (ha, hb, f))
        checks['equal ' + f] = ha == hb
    verdict('DETERMINISM', checks)


def kept_files():
    names = ['state.json', 'plan.json', 'manifest.tsv']
    for sub in ('logs', 'out-A', 'out-B'):
        for d, _s, fs in os.walk(WORK + '/' + sub):
            names += [os.path.relpath(os.path.join(d, f), WORK) for f in fs]
    return sorted(n for n in names if os.path.isfile(os.path.join(WORK, n)))


def mode_keep():
    """B-RECLAIM-OWN's copy: every kept file into the forensic store as tz38-work--<path with - for />, by exclusive create and
    verified whole; the branch worktree must hold nothing but its pushed HEAD."""
    wt = WORK + '/wt'
    rc, so, _ = sh(['git', '-C', wt, 'status', '--porcelain', '--ignored'])
    assert rc == 0 and so == '', 'keep: %s holds %r' % (wt, so[:400])
    head = sh(['git', '-C', wt, 'rev-parse', 'HEAD'])[1].strip()
    up = sh(['git', '-C', wt, 'rev-parse', '@{u}'])[1].strip()
    assert head and up == head, 'keep: %s at %s, upstream %r' % (wt, head, up)
    count = lambda: sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    before, copied, held = count(), 0, 0
    for rel in kept_files():
        path = WORK + '/' + rel
        h = sha256_file(path)
        dest = FORENSICS + '/tz38-work--' + rel.replace('/', '--')
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


def mode_run(name):
    """The measurement, offline: the store -> out-<name>/ . Peak memory and wall time are printed."""
    assert malloc_tune(), 'glibc refused its two settings'
    stop = start_sampler()
    adv3 = load_adv3()
    plan = json.loads(read(WORK + '/plan.json'))
    plan = {'hist_to': plan['hist_to'], 'symbols': plan['symbols']}      # the keys are the fetch's, not the run's
    hist_to = dt.date.fromisoformat(plan['hist_to'])
    assert hist_to == adv3.HISTORY_TO, 'the plan was made for another cut'
    ctx = run_prepare(adv3, plan, hist_to)
    res, files = run_measure(adv3, ctx)
    files['result.json'] = json.dumps(res, sort_keys=True, indent=1, default=str) + '\n'
    files['inputs.json'] = json.dumps({'plan_sha256': sha256_file(WORK + '/plan.json'), 'manifest_sha256': sha256_file(WORK + '/manifest.tsv'),
                                       'adv3_sha256': ADV3_SHA, 'cut': plan['hist_to'], 'declarations': {
                                           'V_MIN': V_MIN, 'V_SENS': V_SENS, 'WINDOW': WINDOW, 'SPAN': SPAN, 'MIN_COINS': MIN_COINS,
                                           'MIN_MONTHS': MIN_MONTHS, 'ALPHA': ALPHA, 'BOOT_B': BOOT_B, 'BOOT_L': BOOT_L, 'SEED': SEED,
                                           'RANDOM_LISTS': RANDOM_LISTS, 'LIST_SIZE': LIST_SIZE, 'LISTED_TO': str(LISTED_TO),
                                           'EXCLUDED_BASES': EXCLUDED_BASES}}, sort_keys=True, indent=1) + '\n'
    odir = WORK + '/out-' + name
    os.makedirs(odir)
    for fname, text in sorted(files.items()):
        with open(odir + '/' + fname, 'x', encoding='utf-8') as f:
            f.write(text)
        b = text.encode()
        out('OUT %s %d bytes %s' % (fname, len(b), sha256_bytes(b)))
    stop.set()
    out('RUN PASS: %s; the largest anonymous set sampled every 0.05 s: %d bytes' % (proc_mem(), PEAK_ANON[0]))


# ---- the self-test: the pure readings and the pipeline on synthetic contracts, each with a negative control ------------------------

def synth_rows(seed, n, start, drift=0.0, vol=0.03, volume=2.0e7):
    """n daily candles from start, a random walk of the given drift and volatility, prices to four decimals, a quote volume
    within a factor of three of `volume`; {day: (open, high, low, close, quote volume)}."""
    import random
    r = random.Random(seed)
    x, rows = 100.0, {}
    for i in range(n):
        o = x
        x *= math.exp(drift + vol * r.gauss(0, 1))
        h = max(o, x) * (1 + abs(r.gauss(0, 0.01)))
        l = min(o, x) * (1 - abs(r.gauss(0, 0.01)))
        rows[start + dt.timedelta(days=i)] = (round(o, 4), round(h, 4), round(l, 4), round(x, 4), volume * (0.5 + 2.5 * r.random()))
    return rows


def write_store(root, sym, rows, rate=0.0001, missing_months=(), funding_months=None):
    """sym's candles as the archive holds them under root: a monthly zip for each month but missing_months, whose days are
    written as daily zips instead, and a monthly funding file for each month with three settlements a day."""
    import zipfile
    base = root + '/data/futures/um/'
    head = 'open_time,open,high,low,close,volume,close_time,quote_volume,count,taker_buy_volume,taker_buy_quote_volume,ignore\n'
    line = lambda d, v: '%d,%s,%s,%s,%s,1.0,%d,%r,1,1.0,1.0,0\n' % (
        int(dt.datetime(d.year, d.month, d.day, tzinfo=dt.timezone.utc).timestamp() * 1000), v[0], v[1], v[2], v[3],
        int(dt.datetime(d.year, d.month, d.day, tzinfo=dt.timezone.utc).timestamp() * 1000) + 86399999, v[4])
    bymonth = {}
    for d, v in rows.items():
        bymonth.setdefault((d.year, d.month), []).append((d, v))

    def put(path, name, text):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with zipfile.ZipFile(path, 'w') as z:
            z.writestr(name, text)
    for (y, m), items in bymonth.items():
        if (y, m) in missing_months:
            for d, v in items:
                n = '%s-1d-%s' % (sym, d.isoformat())
                put('%sdaily/klines/%s/1d/%s.zip' % (base, sym, n), n + '.csv', head + line(d, v))
        else:
            n = '%s-1d-%04d-%02d' % (sym, y, m)
            put('%smonthly/klines/%s/1d/%s.zip' % (base, sym, n), n + '.csv', head + ''.join(line(d, v) for d, v in items))
        if funding_months is None or (y, m) in funding_months:
            n = '%s-fundingRate-%04d-%02d' % (sym, y, m)
            fl = ''.join('%d,8,%r\n' % (int(dt.datetime(d.year, d.month, d.day, h, tzinfo=dt.timezone.utc).timestamp() * 1000), rate)
                         for d, _v in items for h in (0, 8, 16))
            put('%smonthly/fundingRate/%s/%s.zip' % (base, sym, n), n + '.csv', 'calc_time,funding_interval_hours,last_funding_rate\n' + fl)


def mode_selftest():
    import random, tempfile, unittest.mock as mock
    adv3 = load_adv3()
    done = []

    def ok(cond, name):
        done.append(name)
        assert cond, name

    # -- the statistics, against values computed by scipy 1.18.1 at 16 digits
    gold = [(1.7, 60, 0.04715490953428684), (-2.3, 64, 0.9876402584275776), (0.0, 30, 0.5), (3.1, 12, 0.004594998189195668),
            (2.0, 400, 0.023087972586784064)]
    ok(all(abs(t_sf(t, df) - p) <= 1e-11 * max(p, 1e-3) for t, df, p in gold), 't_sf equals scipy.stats.t.sf at five points to 1e-11')
    ok(abs(t_sf(2.2, 50) + t_sf(-2.2, 50) - 1.0) < 1e-14 and t_sf(1.0, 20) > t_sf(1.5, 20) > t_sf(3.0, 20), 't_sf is symmetric and decreasing')
    st = 0
    vec = []
    for _ in range(3):
        st, o = splitmix64(st)
        vec.append(o)
    ok(vec == [0xE220A8397B1DCDAF, 0x6E789E6AA1B965F4, 0x06C45D188009454F], "splitmix64 from state 0 gives the published outputs")
    ok(abs(probit(0.95) - 1.6448536269514722) < 1e-12 and abs(phi(1.0) - 0.8413447460685429) < 1e-14, 'probit and phi')
    ok(abs(power(0.3, 70) - 0.8065153063880648) < 1e-9 and abs(power(0.0, 70) - ALPHA) < 1e-12, 'power: the normal approximation, and alpha at no edge')
    rnd = random.Random(7)
    base = [rnd.gauss(0.0, 1.0) for _ in range(60)]
    b1, b2 = boot_p(base, B=2000), boot_p(base, B=2000)
    ok(b1 == b2 and b1 == (0.63968015992004, 0.36081959020489757), 'boot_p: deterministic, equal to an independent numpy implementation of its specification')
    pos = [x + 1.2 for x in base]
    neg = [x - 1.2 for x in base]
    rp, rn, rz = read_series(pos), read_series(neg), read_series([x - sum(base) / 60 for x in base])
    ok((rp['word'], rn['word'], rz['word']) == ('REPLICATED', 'CONTRADICTED', 'UNDECIDABLE'),
       'read_series: a clearly positive series REPLICATED, a negative CONTRADICTED, a centred one UNDECIDABLE')
    m, sd = mean_sd([1.0, 2.0, 4.0])
    ok(abs(m - 7 / 3) < 1e-15 and abs(sd - math.sqrt(7 / 3)) < 1e-12, 'mean_sd')
    # -- the months
    d0 = dt.date(2024, 1, 1).toordinal()
    S = {d0 + i: 1.0 for i in range(0, 91)}
    N = {d0 + i: 20 for i in range(0, 91)}
    rows = monthly(S, N, dt.date(2024, 3, 31))
    ok([(r[0], r[1]) for r in rows] == [(2024, 1), (2024, 2), (2024, 3)] and abs(rows[0][2] - 31 * 0.05) < 1e-12 and rows[1][3] == 20,
       'monthly: three complete months, x the sum of S / N')
    ok(len(monthly(S, N, dt.date(2024, 3, 30))) == 2, 'monthly: a month whose last day is after the cut is not counted (negative control)')
    ok(len(monthly(S, {o: 9 for o in N}, dt.date(2024, 3, 31))) == 0, 'monthly: a month with fewer than 10 coins a day on average is not counted')
    ok(monthly_sum({d0: 2.0, d0 + 40: 3.0}, rows) == [2.0, 3.0, 0.0], 'monthly_sum')
    # -- the admissibility
    ords = array('i', range(1000, 1100))
    qv = array('d', [20e6] * 100)
    f = admissible(ords, qv, 10e6)
    ok(list(f[:28]) == [0] * 28 and all(f[28:]), 'admissible: nothing before 28 candles exist, everything after at 20M against 10M')
    qv2 = array('d', qv)
    qv2[40] = 1.0
    ok(all(admissible(ords, qv2, 10e6)[28:]), 'admissible: one bad day among 28 does not move the median')
    for i in range(30, 50):
        qv2[i] = 1.0
    ok(not admissible(ords, qv2, 10e6)[55] and admissible(ords, qv2, 10e6)[85], 'admissible: a median below the floor excludes the day and recovers once the window has passed')
    ords2 = array('i', list(range(1000, 1050)) + list(range(1100, 1150)))
    ok(admissible(ords2, array('d', [20e6] * 100), 10e6)[50] == 0 and admissible(ords2, array('d', [20e6] * 100), 10e6)[80] == 1,
       'admissible: a gap in the days leaves the window too wide, so the day is not admitted')
    ok(all(admissible(ords, qv2, 0.0)), 'admissible: a v_min of 0 admits every day')
    big = array('d', [20e6 + 1000.0 * i for i in range(100)])
    base_f = admissible(ords, big, 20.5e6)
    pert = array('d', big)
    for i in range(60, 100):
        pert[i] *= 1000.0
    pf = admissible(ords, pert, 20.5e6)
    ok(list(pf[:61]) == list(base_f[:61]), 'CAUSALITY: multiplying every volume from index 60 on leaves the flags up to index 60 bit-identical')
    ok(any(pf[i] != base_f[i] for i in range(61, 100)), 'CAUSALITY negative control: the flags after index 60 do change')
    # -- the series over adv3: states, simulate and the strategy equal adv3's own on dicts
    start = dt.date(2024, 1, 1)
    syms = ['AAAUSDT', 'BBBUSDT', 'CCCUSDT', 'DDDUSDT', 'EEEUSDT', 'FFFUSDT']
    data = {s: synth_rows(11 + k, 420, start, drift=(0.004 if k % 2 == 0 else -0.004), vol=0.025) for k, s in enumerate(syms)}
    cut = start + dt.timedelta(days=419)
    series = {}
    for s_, rows_ in data.items():
        series[s_] = Series(s_, rows_)
        fill_states(adv3, series[s_], cut)
    ok(all(adv3.states({d: v[:4] for d, v in data[k].items()}, cut)[d] == States(series[k])[d] for k in syms for d in list(data[k])[::17]),
       'States over arrays equal adv3.states over a dict, on every 17th day of 6 contracts')
    ok(all(adv3.simulate({d: v[:4] for d, v in data[k].items()}, lambda d: 0.0001, start, cut)[:2] ==
           adv3.simulate(Candles(series[k]), lambda d: 0.0001, start, cut)[:2] for k in syms), 'simulate over Candles equals simulate over a dict (trades and daily R), 6 contracts')
    funds = {s_: (lambda d: 0.0001) for s_ in syms}
    cs_dict = {s_: {d: v[:4] for d, v in data[s_].items()} for s_ in syms}
    st_dict = {s_: adv3.states(cs_dict[s_], cut) for s_ in syms}
    with patched(adv3, COINS=tuple(syms)):
        ref_t, ref_d, ref_o = adv3.simulate_strong(cs_dict, st_dict, funds, start, cut)
    mine = strong_pass(adv3, series, funds, {}, syms, cut)
    ok(len(ref_t) + len(ref_o) == len(mine['trades']) and ref_d == {dt.date.fromordinal(o): x for o, x in mine['daily'].items()} and len(ref_t) > 0,
       'strong_pass equals simulate_strong over dicts: the same trades and the same daily R (%d trades)' % len(mine['trades']))
    ok(adv3.COINS == tuple(c for c in adv3.COINS) and len(adv3.COINS) == 42 and adv3.TOP_N == 3 and adv3.STRONG_MAX == 3, 'adv3 is restored after the passes: 42 coins, TOP_N 3, STRONG_MAX 3')
    try:
        with patched(adv3, TOP_N=9):
            raise RuntimeError('x')
    except RuntimeError:
        pass
    ok(adv3.TOP_N == 3, 'patched restores an attribute when the block raises')
    # -- the gate: no entry on a day the contract is not admissible, a position held across such days
    s0 = series['AAAUSDT']
    th_free, _dh, _ph = adv3.simulate(Candles(s0), funds['AAAUSDT'], start, cut)
    first = th_free[0]['entry']
    j = s0.index(first)
    closed = array('b', [1] * len(s0.ords))
    closed[j] = 0
    with gated(adv3, s0, closed):
        th_g, _dh, _ph = adv3.simulate(Candles(s0), funds['AAAUSDT'], start, cut)
    ok(all(t['entry'] != first for t in th_g) and len(th_g) >= 1, 'gated: the entry of the first trade is not made on the day the mask closes, later ones are')
    ok(th_free[0]['entry'] == first, 'gated negative control: with no mask the entry is made on that day')
    gap = array('b', [1] * len(s0.ords))
    for i in range(j + 1, min(j + 6, len(gap))):
        gap[i] = 0
    with gated(adv3, s0, gap):
        th_h, _d2, _p2 = adv3.simulate(Candles(s0), funds['AAAUSDT'], start, cut)
    ok(th_h[0]['entry'] == first and th_h[0]['R'] == th_free[0]['R'], 'gated: a position open when the mask closes is held to its ordinary exit, with the same R')
    # -- a contract whose data ends: flat on its last day, which closes the position and frees the slot
    lone = Series('TTTUSDT', synth_rows(21, 200, start, drift=0.012, vol=0.01))
    cut_t = dt.date.fromordinal(lone.ords[-1])
    fill_states(adv3, lone, cut_t)
    f_t = {'TTTUSDT': lambda d: 0.0}
    lone.ended = True
    ended_run = strong_pass(adv3, {'TTTUSDT': lone}, f_t, {}, ['TTTUSDT'], cut_t + dt.timedelta(days=30))
    lone.ended = False
    open_run = strong_pass(adv3, {'TTTUSDT': lone}, f_t, {}, ['TTTUSDT'], cut_t + dt.timedelta(days=30))
    ok(len(ended_run['trades']) >= 1 and ended_run['trades'][-1]['why'] == 'signal' and ended_run['trades'][-1]['exit'] == cut_t,
       'ended: a contract whose data ends closes its position on its last day, at the close, as a signal exit')
    ok(len(open_run['trades']) >= 1 and open_run['trades'][-1]['why'] == 'open at the history cut' and 'exit' not in open_run['trades'][-1]
       and open_run['trades'][-1]['end'] == cut_t, 'ended negative control: without the flag the position is carried to the end of the data and closed there as at the cut')
    # -- the rule pass and its day counts
    rp_ = rule_pass(adv3, series, funds, {}, cut)
    ok(rp_['N'][series['AAAUSDT'].ords[200]] == 6 and rp_['N'].get(series['AAAUSDT'].ords[50], 0) == 0, 'rule_pass: N counts the contracts that have a signal that day (6 late, 0 before the lookback)')
    mk = {s_: admissible(series[s_].ords, series[s_].qv, 1e12) for s_ in syms}
    ok(not rule_pass(adv3, series, funds, mk, cut)['trades'] and not any(rule_pass(adv3, series, funds, mk, cut)['N'].values()),
       'rule_pass with nothing admissible opens no trade and counts no coin')
    ends = [t for t in rp_['trades'] if t['why'] == 'open at the history cut']
    ok(abs(sum(rp_['facts'].values()) - sum(rp_['gate'].values()) - sum(adv3.COST * series[t['coin']].c[-1] / t['U'] for t in ends)) < 1e-9 and len(ends) >= 1,
       'rule_pass: the gate series is the facts series less the exit cost of each position closed at the end of data (%d of them)' % len(ends))
    # -- tables
    tr = [{'R': -1.0, 'U': 1.0, 'E': 20.0, 'd': 1, 'coin': 'X'}, {'R': 2.0, 'U': 2.4, 'E': 20.0, 'd': -1, 'coin': 'Y'},
          {'R': 5.0, 'U': 3.0, 'E': 20.0, 'd': 1, 'coin': 'Z'}]
    bt = bucket_table(tr, stop_pct, [11.1, 14.0], ['<=11.1%', '11.1-14%', '>14%'])
    ok([b['trades'] for b in bt] == [1, 1, 1] and bt[0]['total_R'] == -1.0 and bt[2]['mean_R'] == 5.0, 'bucket_table: stop distances 5 %, 12 %, 15 % land in three buckets')
    ok(bucket_table(tr, lambda t: 11.1, [11.1, 14.0], ['a', 'b', 'c'])[0]['trades'] == 3, 'bucket_table: an edge belongs to the lower bucket')
    day300 = dt.date.fromordinal(series['AAAUSDT'].ords[300])
    ranks = sorted(rank_at(series, syms, {}, day300, k) for k in syms if series[k].sig[300] in (1, -1) and series[k].U[300] == series[k].U[300])
    ok(ranks == list(range(1, len(ranks) + 1)) and len(ranks) >= 2, 'rank_at: the active contracts of a day take the places 1..n once each (%d active)' % len(ranks))
    # -- weakening on a constructed trade
    fake = Series('QQQUSDT', synth_rows(5, 40, start))
    n = len(fake.ords)
    fake.sig, fake.sm = array('b', [1] * n), array('b', [4] * 10 + [2] * 30)
    fake.z, fake.U = array('d', [1.5] * n), array('d', [1.0] * n)
    entry = dt.date.fromordinal(fake.ords[5])
    path = array('d')
    for k in range(6, 20):
        path.extend((float(fake.ords[k]), 0.1 * (k - 5)))
    t_ = {'coin': 'QQQUSDT', 'd': 1, 'entry': entry, 'exit': dt.date.fromordinal(fake.ords[19]), 'why': 'signal', 'R': 2.0, 'U': 1.0, 'path': path}
    w = weakening(adv3, [t_], {'QQQUSDT': fake})
    r_at = path[2 * 4 + 1]
    want = 2.0 - (r_at - adv3.COST * fake.c[10] / 1.0)
    ok(w['entered_with_four_signs'] == 1 and w['weakened'] == 1 and abs(w['mean_hold_minus_exit'] - want) < 1e-12 and w['share_hold_better'] == 1.0,
       'weakening: the first close with the sum at +/-2 is day 10; the R after it is read against the R of leaving there')
    t_['entry'] = dt.date.fromordinal(fake.ords[15])
    ok(weakening(adv3, [t_], {'QQQUSDT': fake})['entered_with_four_signs'] == 0, 'weakening negative control: a trade entered with two signs is not read')
    # -- the store: candle_rows equals adv3.archive_candles, a gap month read from daily files
    with tempfile.TemporaryDirectory() as tmp:
        rows_ = synth_rows(3, 150, dt.date(2024, 1, 1))
        write_store(tmp, 'ZZZUSDT', rows_, missing_months=((2024, 3),))
        old_store, old_get = globals()['STORE'], adv3.get
        globals()['STORE'] = tmp
        adv3.get = local_get_for(adv3)
        try:
            mine_c = candle_rows(adv3, 'ZZZUSDT', dt.date(2024, 5, 20))
            theirs_c = adv3.archive_candles('ZZZUSDT', dt.date(2024, 5, 20), SerialPool)
        finally:
            globals()['STORE'], adv3.get = old_store, old_get
        ok(len(mine_c) == 141 and {d: v[:4] for d, v in mine_c.items()} == theirs_c and all(mine_c[d][4] == rows_[d][4] for d in mine_c),
           'candle_rows equals adv3.archive_candles day for day over a store with a gap month read from daily files, and carries the quote volume')
    # -- G-EQUAL on a synthetic store: the pipeline over six contracts equals adv3.history()
    with tempfile.TemporaryDirectory() as tmp:
        for s_, rows_ in data.items():
            write_store(tmp, s_, rows_, funding_months={(2024, m) for m in range(1, 13)})
        old_store, old_get = globals()['STORE'], adv3.get
        globals()['STORE'] = tmp
        adv3.get = local_get_for(adv3)
        try:
            with patched(adv3, COINS=tuple(s_[:-4] for s_ in syms), HISTORY_TO=cut, ARCHIVE_FROM=start, FUNDING_TO=(2024, 9)):
                ref = adv3.history()
                ser2, fun2 = {}, {}
                for s_ in syms:
                    ser2[s_] = Series(s_, candle_rows(adv3, s_, cut))
                    fill_states(adv3, ser2[s_], cut)
                    fun2[s_] = funding_for(adv3, s_, ser2[s_], cut)[0]
                ra = rule_pass(adv3, ser2, fun2, {}, cut, order=syms)
                sa = strong_pass(adv3, ser2, fun2, {}, syms, cut)
                got = facts_shape(adv3, ra, sa)
        finally:
            globals()['STORE'], adv3.get = old_store, old_get
        ok(got['base'] == ref['base'] and got['strong'] == ref['strong'] and got['base']['trades'] > 0 and got['strong']['trades'] > 0,
           'G-EQUAL on a synthetic store: both blocks of the pipeline equal adv3.history() exactly (%d and %d trades)' % (got['base']['trades'], got['strong']['trades']))
        ok(got['base']['total_R'] != 0 and ref['base'] != {}, 'G-EQUAL negative control: a different cut gives a different block')
    # -- the arena: arrays written to one file and read back as views give the same trades, the file left no trace
    with tempfile.TemporaryDirectory() as tmp:
        for s_, rows_ in data.items():
            write_store(tmp, s_, rows_, funding_months={(2024, m) for m in range(1, 13)})
        old_store, old_get = globals()['STORE'], adv3.get
        globals()['STORE'] = tmp
        adv3.get = local_get_for(adv3)
        plan_ = {'symbols': syms}
        try:
            with patched(adv3, COINS=tuple(s_[:-4] for s_ in syms), HISTORY_TO=cut, ARCHIVE_FROM=start, FUNDING_TO=(2024, 9)):
                ser_a, fun_a, msk_a = load_all(adv3, plan_, cut, Arena(tmp + '/arena.bin'))
                ser_b, fun_b, msk_b = load_all(adv3, plan_, cut)
                ra, rb = rule_pass(adv3, ser_a, fun_a, msk_a[V_MIN], cut), rule_pass(adv3, ser_b, fun_b, msk_b[V_MIN], cut)
                sa_, sb_ = strong_pass(adv3, ser_a, fun_a, msk_a[V_MIN], syms, cut), strong_pass(adv3, ser_b, fun_b, msk_b[V_MIN], syms, cut)
                gone = not os.path.exists(tmp + '/arena.bin')
        finally:
            globals()['STORE'], adv3.get = old_store, old_get
        ok(isinstance(ser_a['AAAUSDT'].c, memoryview) and isinstance(ser_b['AAAUSDT'].c, array) and gone,
           'arena: the arrays are views into the map after the seal, the file is gone from the disk, the plain load keeps arrays')
        ok(ra['trades'] == rb['trades'] and ra['facts'] == rb['facts'] and ra['N'] == rb['N'] and sa_['trades'] == sb_['trades'] and sa_['daily'] == sb_['daily']
           and len(ra['trades']) > 0 and all(list(msk_a[V_MIN][k]) == list(msk_b[V_MIN][k]) for k in syms),
           'arena: the rule and the strategy over the views equal those over the arrays - trades, daily R, day counts and flags (%d and %d trades)' % (len(ra['trades']), len(sa_['trades'])))
    # -- the request function: the User-Agent, 404, a retried 429, a refusal
    class Resp:
        def __init__(self, body):
            self.body = body

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

        def read(self):
            return self.body
    seen = []

    def fake_open(req, timeout=0):
        seen.append(req.get_header('User-agent'))
        step = len(seen)
        if 'gone' in req.full_url:
            raise urllib.error.HTTPError(req.full_url, 404, 'nf', {}, None)
        if 'busy' in req.full_url and step < 3:
            raise urllib.error.HTTPError(req.full_url, 429, 'busy', {}, None)
        if 'denied' in req.full_url:
            raise urllib.error.HTTPError(req.full_url, 403, 'no', {}, None)
        return Resp(b'body')
    with mock.patch('urllib.request.urlopen', fake_open), mock.patch('time.sleep', lambda s: None):
        r1, r2 = request('https://x/ok'), request('https://x/gone')
        seen.clear()
        r3 = request('https://x/busy')
        try:
            request('https://x/denied')
            refused = False
        except RuntimeError:
            refused = True
    ok(r1 == b'body' and r2 is None and r3 == b'body' and refused and set(seen) == {UA}, 'request: served, 404 as None, a 429 retried, a 403 raised, and every request names its User-Agent')
    # -- the plan: gap months get a daily listing, the funding of the cut month is left out
    calls = []

    def fake_list(prefix, delimiter='/'):
        calls.append(prefix)
        if prefix.startswith(KL):
            return [], [KL + 'XXXUSDT/1d/XXXUSDT-1d-2026-%02d.zip' % m for m in (5, 6, 8, 9)] + [KL + 'XXXUSDT/1d/XXXUSDT-1d-2026-05.zip.CHECKSUM']
        if prefix.startswith(FU):
            return [], [FU + 'XXXUSDT/XXXUSDT-fundingRate-2026-%02d.zip' % m for m in (5, 6, 8, 9, 10)]
        if prefix.endswith('2026-07'):
            return [], [KD + 'XXXUSDT/1d/XXXUSDT-1d-2026-07-%02d.zip' % d for d in (30, 31)]
        return [], [KD + 'XXXUSDT/1d/XXXUSDT-1d-2026-10-%02d.zip' % d for d in (1, 27, 28, 30)]
    old_list = globals()['s3_list']
    globals()['s3_list'] = fake_list
    try:
        keys_, n_calls = plan_symbol('XXXUSDT', dt.date(2026, 10, 27), (2026, 9))
    finally:
        globals()['s3_list'] = old_list
    ok(sum('/monthly/klines/' in k for k in keys_) == 4 and sum('/daily/klines/' in k for k in keys_) == 4 and sum('/fundingRate/' in k for k in keys_) == 4
       and not any(k.endswith('10-28.zip') or k.endswith('10-30.zip') for k in keys_) and n_calls == 4,
       'plan_symbol: 4 monthly files, the daily files of the July gap and of October up to the cut (28 and 30 left out), funding to September only, 4 listing calls')
    # -- the host gate against stand-ins for the machine, each reading with a negative control
    def host_run(mem=(200_000_000, None), avail=8_000_000_000, active='active', manifest=True, size='31612203008', tree=False):
        reads = iter(mem)

        def f_sh(args, **kw):
            if args[0] == 'find':
                return 0, ('/var/lib/btc-recorder/2026/manifest.json\n' if manifest else ''), ''
            if args[0] == 'df':
                return 0, 'Filesystem Size Avail\n/dev/vda2 %s %d\n' % (size, avail), ''
            if args[0] == 'grep':
                return 0, '2\n', ''
            return 0, '3.12.3\n', ''
        f_show = lambda unit, *p: {'MainPID': '5', 'NRestarts': '0', 'ActiveState': active, 'SubState': 'running', 'UnitFileState': 'enabled'}
        old = {k: globals()[k] for k in ('sh', 'show', 'meminfo', 'out')}
        old_exists, old_listdir, old_sleep = os.path.exists, os.listdir, time.sleep
        globals().update(sh=f_sh, show=f_show, meminfo=lambda: {'MemAvailable': next(reads)}, out=lambda *a: None)
        os.path.exists = lambda p: True if p == WORK else old_exists(p)
        os.listdir = lambda p: ['x'] if (p == WORK and tree) else ['logs', 'stage'] if p == WORK else old_listdir(p)
        time.sleep = lambda s: None
        try:
            mode_host()
            return True
        except Failed:
            return False
        finally:
            globals().update(old)
            os.path.exists, os.listdir, time.sleep = old_exists, old_listdir, old_sleep
    ok(host_run(), 'host: every reading passes on a stand-in that is the capture host with 200 MB available and 8 GB free')
    ok(host_run(mem=(100_000_000, 200_000_000)), 'host: a first memory read below the floor is read again and the second decides (pass)')
    ok(not host_run(mem=(100_000_000, 110_000_000)), 'host negative control: both memory reads below the floor fail')
    ok(not host_run(avail=7_000_000_000), 'host negative control: free space below the floor fails')
    ok(not host_run(active='failed'), 'host negative control: a capture unit that is not active fails')
    ok(not host_run(manifest=False), 'host negative control: no recorder manifest, so not the capture host, fails')
    ok(not host_run(size='1'), 'host negative control: another filesystem fails')
    ok(not host_run(tree=True), 'host negative control: a tree of an earlier run beside logs/ and stage/ fails')
    # -- the kept files and the determinism reading, on a temporary work tree
    with tempfile.TemporaryDirectory() as tmp:
        old_work = globals()['WORK']
        globals()['WORK'] = tmp
        try:
            for sub in ('logs', 'out-A', 'out-B'):
                os.makedirs(tmp + '/' + sub)
            for rel in ('state.json', 'plan.json', 'manifest.tsv', 'logs/01-selftest.log', 'out-A/result.json', 'out-B/result.json', 'arena.bin'):
                with open(tmp + '/' + rel, 'w') as f:
                    f.write('same bytes')
            kept = kept_files()
            same_ok, same_bad = True, False
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    mode_same(tmp + '/out-A', tmp + '/out-B')
            except Failed:
                same_ok = False
            with open(tmp + '/out-B/result.json', 'w') as f:
                f.write('changed')
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    mode_same(tmp + '/out-A', tmp + '/out-B')
            except Failed:
                same_bad = True
        finally:
            globals()['WORK'] = old_work
        ok(kept == ['logs/01-selftest.log', 'manifest.tsv', 'out-A/result.json', 'out-B/result.json', 'plan.json', 'state.json'],
           'kept_files: the logs, the state, the plan, the manifest and both outputs, and not the arena')
        ok(same_ok and same_bad, 'mode_same: equal directories pass, a changed file fails (negative control)')
    # -- the checker's pure readings
    mp = ('**Revision string:** `%s`\n| `A1` — x | `229a944f2d51` |\n### Fingerprint table\n| path | a |\n| `a.py` | 3 | 1,234 | frozen | `%s` |\n'
          '| `b.md` | — | — | reported | self |\n\n## 1. next\n') % (MAP_REV, 'ab' * 32)
    rv, an, rw = parse_map(mp)
    ok(rv == MAP_REV and an == {'A1': '229a944f2d51'} and rw == [('a.py', 3, 1234, 'frozen', 'ab' * 32), ('b.md', None, None, 'reported', None)], 'parse_map reads the revision, the anchors and the rows')
    ok(all(number_reading(['CryptoTZ/' + TZ_FILE.split('/')[1], 'CryptoTZ/TZ-37-x.md']).values()) and
       not all(number_reading(['CryptoTZ/' + TZ_FILE.split('/')[1], 'CryptoTZ/TZ-38-other.md']).values()) and
       not all(number_reading([TZ_FILE, 'CryptoReports/TZ-38-adv3-pit-validation-report.md']).values()), 'number_reading: one file passes, a second file or a report fails')
    global MEM_FLOOR
    old_floor, MEM_FLOOR = MEM_FLOOR, 100
    ok(memory_gate(150, None) == (True, 150) and memory_gate(50, 120) == (True, 120) and memory_gate(50, 60) == (False, 60) and memory_gate(50, None) == (False, 50),
       'memory_gate: the second read decides where the first was below the floor')
    MEM_FLOOR = old_floor
    snap = {u: {'MainPID': '1', 'NRestarts': '0', 'ActiveState': 'active', 'UnitFileState': 'enabled'} for u in CAPTURES + (BOT,)}
    moved = {u: dict(v) for u, v in snap.items()}
    moved[BOT]['MainPID'] = '2'
    ok(all(still_reading(snap, snap).values()) and not all(still_reading(snap, moved).values()), 'still_reading: equal passes, a moved MainPID fails')
    print('SELFTEST PASS: %d of %d checks passed' % (len(done), len(done)))


def main(argv):
    if not argv:
        sys.exit('usage: tz38-adv3-pit-validation.py MODE [ARG]')
    mode, rest = argv[0], argv[1:]
    table = {'fingerprint': mode_fingerprint, 'host': mode_host, 'number': mode_number, 'probe': mode_probe, 'fetch': mode_fetch,
             'mark': mode_mark, 'still': mode_still, 'keep': mode_keep, 'selftest': mode_selftest, 'equal': mode_equal}
    try:
        if mode == 'plan':
            mode_plan(load_adv3().HISTORY_TO)
        elif mode == 'run':
            assert len(rest) == 1 and re.fullmatch(r'[AB]', rest[0]), 'run A|B'
            mode_run(rest[0])
        elif mode == 'same':
            assert not rest
            mode_same(WORK + '/out-A', WORK + '/out-B')
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
