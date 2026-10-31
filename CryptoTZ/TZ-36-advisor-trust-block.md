# TZ-36 — the advisor's card says what it rests on: the forward book in parts, each card's basis and invalidation, and the Boss's six ratings

**Canonical filename:** `TZ-36-advisor-trust-block.md`. The committed file takes this name and no other.

**Executor model: Claude Opus 5.5.** It changes ADV-3's only implementation — `history`, `report`, `card` and `message`
in `advisor/adv3.py` — and G-HISTORY's arithmetic, and signals a long-lived unit on the capture host.

**Required System Map revision:** `2026-10-29-b`.

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

**Before `EXECUTE TZ-36`:** nothing is the Boss's. The bot's token and its pinned chat exist (map §2.7); this TZ reads
neither and prints neither.

**When:** any time after the upload that carries this TZ, while `/dev/vda2` holds at least `7,400,000,000` bytes free
(§0.4). **§3.5 waits for 06:35:00 to 23:45:00 UTC before the service copy is replaced, and §3.6 for 06:35:00 to 23:50:00
before the unit is signalled**, clear of the package manager's morning runs and of both archives' calendar runs, the
reward book's at 01:30:20 and the pair book's at 03:00:20 (map §6; §7 item 129). This TZ reloads systemd **never**, so it sets
off no run of either archive (map §7 items 125 and 129). About 45 minutes of wall clock (§6).

**What this TZ is.** On 2026-10-31 the Boss asked how each signal is generated, validated and rated, and ordered six
ratings appended to every signal report, each with a factual reason and none given by impression. The Architect's
answer found one defect in what the advisor's message shows (§1) and no way to give the ratings without the message
carrying them. **This TZ changes what the message shows and nothing the rule does:** (1) the forward record in its
parts — entries, the closed trades and the R they closed on, the open positions and the R they hold, and the total
over the market; (2) on each card, the basis of its direction — the sum of the four signs, the strength `z`, the rank —
and the level at which it is invalidated; (3) the six ratings, each a function of recorded facts (§4.4), with two more
facts, the one-sided `p` of each class's daily portfolio R and the share of each class's R that its five best trades
hold, re-derived by G-HISTORY like the rest. It replaces `adv3.py` and `selftest-adv3.py` and adds this TZ's checker
`research/tz36-advisor-trust.py`; **it leaves `RULE-ADV-3.txt`, `adv3-bot.py` and the unit untouched**, and it proves
the fourteen functions of the rule byte-identical by their syntax trees (G-RULE). It deploys by replacing the service
copy's `adv3.py` and signalling the unit once. It measures nothing about the market to come.

---

## 0. Gates

### 0.0 The work tree, first

After contract §1 steps 1 and 2, and before anything else:

```
mkdir /root/tz36-work /root/tz36-work/logs; echo "exit=$?"
```

`exit=0` proves neither existed; anything else is BLOCKED. **From here every command's output goes to
`/root/tz36-work/logs/`, one file per step, `NN-<step>.log` in this TZ's order**, and nothing to the session's
scratchpad. The one exception is B-RECLAIM-OWN, §9, which removes the directory the logs are in.

Two abbreviations: **`P`** is `nice -n 19 /root/tz04a-env/venv/bin/python -B`, and **`I`** is `P
/root/tz36-work/stage/research/tz36-advisor-trust.py`. **In every block that signals the unit, restores a file or removes a tree, `I` is
written out in full**, because the Boss may be handed the block (map §6, sandbox limit).

### 0.1 The files, staged

Extract Appendix A from this TZ as the primary checkout carries it after contract §1's pull, with this script,
verbatim, its one argument the destination:

```
/root/tz04a-env/venv/bin/python -B - /root/tz36-work/stage <<'EOF'
import hashlib, os, sys
SRC = "/root/btc-5m-twap/CryptoTZ/TZ-36-advisor-trust-block.md"
DEST = sys.argv[1]
WANT = {
    "advisor/adv3.py": "d73a657ef31decad276b858c4ec9672dce1c1c5cec36f0bb1c5b3378838224a8",
    "advisor/selftest-adv3.py": "ef4ffc44e6f8bcdd5685fc1db9090957890c6e2ab762cdad8ae9826b18cf1395",
    "research/tz36-advisor-trust.py": "a0fb9d53afe435d37354862eb8fd299256bf551fdbdb25a5c828d2cc7376d4f5",
}
OLD = {  # the committed files an extraction over a worktree replaces: TZ-35's, by hash
    "advisor/adv3.py": "7f2863a5b433ed7008c8f44af4f9c59d724d0c016c2c317f451158899c4f9adb",
    "advisor/selftest-adv3.py": "76bad371727e0d4bf13c1d009f1b8f9412133a33788c456ecd53d1f83df6f0e6",
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
            assert name in OLD and hashlib.sha256(fh.read()).hexdigest() == OLD[name], ("not TZ-35's", name)
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
| `advisor/adv3.py` | 817 | 43,274 | `d73a657ef31decad276b858c4ec9672dce1c1c5cec36f0bb1c5b3378838224a8` |
| `advisor/selftest-adv3.py` | 201 | 12,600 | `ef4ffc44e6f8bcdd5685fc1db9090957890c6e2ab762cdad8ae9826b18cf1395` |
| `research/tz36-advisor-trust.py` | 582 | 32,925 | `a0fb9d53afe435d37354862eb8fd299256bf551fdbdb25a5c828d2cc7376d4f5` |

A failed assert is BLOCKED. Over an empty `stage/` the script creates three files (`xb`); over the branch's worktree,
§3.1, it overwrites the two committed files and only after asserting each is TZ-35's by hash, and creates the third.

### 0.2 Fingerprint

`I fingerprint` performs contract §1 steps 3 and 4 against `SYSTEM-MAP.md` and the files of its §0 table in the primary
checkout `/root/btc-5m-twap`, and asserts them: revision `2026-10-29-b`; the six anchors, `A2`, `A4`, `A5` and `A6`
re-derived as the first 12 hex characters of those files' SHA-256; the table's **55** rows, each printed in lines,
bytes and SHA-256 — **52** `frozen` rows asserted equal to the map, **2** `tracked` and **1** `reported`, the map's
own. It prints `READING FINGERPRINT: PASS - 64 of 64` — 1 revision, 6 anchors, 4 re-derived, 52 rows, 1 shape — or
fails at the first mismatch, which is BLOCKED. The five advisor rows are `frozen` at TZ-35's hashes and stay so until
the verdict of this TZ.

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
- **H2** — `df` names source `/dev/vda2` and size `31612203008`; `grep -c e3975b5da44c5328adf3bf3914634cd878842c73
  /var/lib/btc-recorder/runtime.jsonl` prints at least `1` — two checks. With H1 this is map §6's host identity.
- **H3** — `/root/tz04a-env/venv/bin/python` prints `3.12.`: the interpreter the bot runs under.
- **H4** — `btc-recorder.service`, `btc-pairbook.service` and `btc-rewardbook.service` each read `ActiveState=active` and
  `UnitFileState=enabled` — three checks: UNIT-NEW compares them, later, against the `kill` mark's snapshot.
- **H5** — `adv3-bot.service` reads `active`, `running`, `enabled`; its `MainPID` runs the unit's exact argv, alone;
  `/root/adv3-bot-svc` holds `adv3.py`, `adv3-bot.py` and `commit.txt` and nothing else; `adv3.py` and `adv3-bot.py`
  hash to TZ-35's (`7f2863a5…` and `e65de91c…`); the installed unit file hashes to `main`'s (`82acd8e4…`); `commit.txt`
  is 40 hex characters and a newline — six checks.
- **H6** — `/var/lib/adv3-bot/daily-sent` holds a date, and `journal.jsonl` ends in a newline.
- **Memory gate** — `MemAvailable` at least `170,344,448` bytes (§0.4). **Disk gate** — `/dev/vda2` free at least
  `7,400,000,000` bytes (§0.4).

Any one failing is BLOCKED. **The rest is printed and carries no threshold:** the timers and the two archives' services;
the listing of the service copy and the record; `du` of the capture roots and the Claude directory; the forensic
store's count, map §3's `2,205`; the worktrees, map §3's two; and the listing of the directory that holds the
session's own scratch, whose UUID directories §3.3 names live or earlier. Map §3 records TZ-35's two left behind,
`95f1d37e-8b62-5abb-93a1-839ff07d8cf8` and `670d0460-3b29-4949-95f8-46f94b680ab9`.

### 0.4 Resource floors, in exact bytes

**Disk.** `/dev/vda2` free at least **`7,400,000,000`** bytes: the reward book's `STREAM_FLOOR`, `7,300,000,000`, below
which no stream of it opens (map §2.6; `research/tz33-reward-book-capture.py` line 190), plus `100,000,000` for this
session at its upper bound — the worktree, about `10,300,000` bytes of tracked files, the logs under `2,000,000`,
`history.json` `19,434`, the copies of the work tree's files under `5,000,000`. **This TZ never takes free space
below the floor that pauses the reward book.** TZ-35 read `10,355,449,856` bytes free at its closing read (map §6).

**Memory.** `MemAvailable` at least **`170,344,448`** bytes: twice `85,172,224`. Map §7 item 131's rule is that a floor derived from a
peak takes the larger of the Architect's measurement and the host's last measured peak of the same code. The largest mode is `adv3.py
--history`: the Architect measured `85,172,224` bytes on TZ-35's bytes and the host `72,032,256` (item 131); the Architect's run of the
changed function on 2026-10-31 under Python 3.13.18 peaked at `79,220,736` — it adds one sort of at most 5,265 floats, about `42,000`
bytes [modelled]. The larger, `85,172,224`, stands. The service runs under its unit's `MemoryMax=128M`, which this TZ does not change;
the new message adds three short lists to a report the service already builds. Every mode of this TZ runs under `nice -n 19`.

### 0.5 Refs and the number

```
git -C /root/btc-5m-twap fetch origin
git -C /root/btc-5m-twap ls-remote origin
git -C /root/btc-5m-twap ls-remote --heads origin tz-36-advisor-trust-block | wc -l
I number
git -C /root/btc-5m-twap log --first-parent --name-status --format='%h %cI %s' -n 5 origin/main
```

Every ref line is reported. **`wc -l` must print `0`:** the branch does not exist. **`I number`** reads `git ls-tree
--name-only origin/main -- CryptoTZ/ CryptoReports/` and must print `READING NUMBER: PASS - 2 of 2`: `CryptoTZ/` holds
`TZ-36-advisor-trust-block.md` and no other file whose name begins with `TZ-36-`, and `CryptoReports/` no report whose
name does (CANON hard rule 2). Anything else is BLOCKED. A difference in the refs or the log from what map §1 records
is recorded, not blocking, unless `main` does not carry revision `2026-10-29-b`.

---

## 1. Why this TZ exists

**The order.** The Boss asked, on 2026-10-31, for the rules, the confirmation, the levels, the statistics, the forward
record and the sizing behind each signal, and for six ratings appended to every signal report — signal confidence,
system reliability, whether STRONG is justified, the key invalidation condition, evidence quality and expected net
expectancy — each with a brief factual reason, none given by impression or by a backtest alone, and "unverified"
where the evidence is short. The Architect answered the first part in chat, from `advisor/` at `main` and from a
re-derivation of the history on Binance's archive. **The second part is the bot's, not the chat's** (CANON, the
signal trigger): this TZ makes the message carry it.

**The defect, named plainly.** The message's forward line printed `fb['total_R']` and `fs['total_R']` from
`rep['forward']`, which is `stats(trades, daily)['total_R']` — the sum of the R of the **closed** trades alone
(`adv3.py` lines 322 and 429); the positions still open are the third value `simulate` returns, and `report` threw it
away (line 422, `tf, df, _ = simulate(...)`). It printed neither the number of trades nor the open positions' R, so
"−8.49 R overall" read as a result, and "0 R" for STRONG — `num(0)` is `'0'` (lines 459 and 460) — read as break-even
when it meant that no STRONG trade had closed. Trades that lose close quickly, by a stop or a flipped signal, and trades that win stay open, so a closed-only sum is biased
low in the first days [modelled]. The Architect's re-derivation on 2026-10-31, approximate because Binance's archive holds no
daily file for 2026-10-28 for any of the 42 coins and the stand-in was spot candles for 39 of them: at the close of
2026-10-30 about 34 entries, about 11 closed (4 stops, 7 signal exits) on about −7.5 R, about 23 open on about +1.0 R,
about −6.5 R over the market; STRONG 3 open, 0 closed, about −0.1 R. That re-derivation gates nothing here.

**The class repaired.** A figure on the card whose population is not named. This TZ's rule, which G-RENDER reads: every
R in the forward lines is one of three named populations — closed, open, total — and the total is their sum.

**The ratings** are the Boss's six. Each is a function of facts the message already holds or of a constant that only a
reading of the forward record moves (§4.4). They are not new knowledge: while the rule is unproven they say so, six
ways, and they cannot say otherwise until CANON PART VII's single reading, after 2027-10-28.

**What this TZ does not do.** It adds no market factor — volume, open interest, funding as a signal, liquidations, strength
against BTC, catalysts — to any card as confirmation: the rule does not read them and no step has measured their
relation to its outcomes (CANON §1.2, last sentence, and §1.6). The card keeps funding as a cost, as before. A factor enters only after a
measurement on the history, under a rule frozen before its data: a TZ of its own.

**A finding the next map revision records.** Binance's public archive held on 2026-10-31, between 07:18 and 07:30 UTC, no daily kline
file for 2026-10-28 for any of the 42 perpetuals (HTTP 404; for BTCUSDT also at 1h, 4h, 15m, 5m and 1m), while the
files of 2026-10-27 and 2026-10-29 were served. The forward record's reading, which CANON PART VII has an Executor
re-derive from the archive, must take that day from `fapi.binance.com`. This TZ touches none of it.

---

## 2. Scope

**Paths this TZ writes.** On the branch `tz-36-advisor-trust-block`: `advisor/adv3.py` and `advisor/selftest-adv3.py`,
each modified, and `research/tz36-advisor-trust.py`, new. On the host: `/root/tz36-work/**`; `/root/adv3-bot-svc/adv3.py`
and `/root/adv3-bot-svc/commit.txt`; `/root/btc-forensics/tz36-work--*`. On `main`: the report,
`CryptoReports/TZ-36-advisor-trust-block-report.md`.

**Prohibited**, by path and by content class:

1. Any change to a repository file but the three above and the report — `advisor/RULE-ADV-3.txt`, `advisor/adv3-bot.py`,
   `deploy/systemd/adv3-bot.service`, `SYSTEM-MAP.md` and `BTC-EXECUTOR-INSTRUCTIONS.md` among them.
2. Any change to a rule function of `adv3.py` — `signs`, `signal`, `strength`, `true_range`, `unit`, `open_at`, `hold`,
   `close_at`, `simulate`, `states`, `ranking`, `simulate_strong`, `stats`, `funding_of` — or to a constant but `FACTS`
   and the two added after it. G-RULE reads it.
3. Any read, copy, print or hash of anything under `/etc/adv3-bot/`, and any request to Telegram or to Binance by this
   TZ's own commands, but two: G-RENDER runs the service copy's `adv3.py`, which reads Binance's public futures market, and
   P-START (§3.6) runs the bot's own `--probe`, whose function reads the token to send one `getMe` and prints the bot's
   username and neither the token nor a chat id. The unit makes its own requests.
4. Any `systemctl` verb but `show`, `list-timers`, `is-enabled`, `kill --signal=SIGTERM adv3-bot.service` (B-KILL, B-ROLLBACK) and, on
   a FAIL of UNIT-OLD, `disable --now adv3-bot.service` (K-36). No `daemon-reload`, `enable`, `restart`, `start`,
   `stop` or `mask`.
5. Any change to a capture unit, its store, either archive's timer or ledger: `systemctl show` and `list-timers`, `du`, and under
   the recorder's root `find`, `grep -c` and `df` read them, nothing writes.
6. A dataset or a binary in git history: `history.json` is `19,434` bytes and stays in the work tree and the forensic store.
7. A price, a coin, a size or a card from the live message printed in the report: G-RENDER prints counts and labels
   alone. Binance's prices are public market data and none is a capture's, but the day's cards are the Boss's to read in his
   chat, not the repository's.
8. The report on `main` before the branch is pushed and its pull request opened (contract §4.1).

**Exemptions.** The two requests of item 3, each by the service copy's own code, as TZ-35's P-START and G-SAME made theirs.

---

## 3. The work, in this order

### 3.1 The branch and its files

```
git -C /root/btc-5m-twap fetch origin
I number
git -C /root/btc-5m-twap worktree add -b tz-36-advisor-trust-block /root/tz36-work/wt origin/main
```

`I number` must print `READING NUMBER: PASS - 2 of 2` again, or BLOCKED. Then §0.1's script again, verbatim but for its
argument, `/root/tz36-work/wt`; it must print the same lines, bytes and SHA-256 as at §0.1. Then:

```
git -C /root/tz36-work/wt add advisor/adv3.py advisor/selftest-adv3.py research/tz36-advisor-trust.py
git -C /root/tz36-work/wt diff --cached --name-status
git -C /root/tz36-work/wt diff --cached --numstat
```

`--name-status` must print exactly three lines — `M` for the two advisor files, `A` for the checker — and `--numstat`
exactly `115	16	advisor/adv3.py`, `48	2	advisor/selftest-adv3.py` and `582	0	research/tz36-advisor-trust.py`, or BLOCKED.
Commit them alone; `git ls-remote origin` (§0.5); push with `git push -u origin tz-36-advisor-trust-block` — through
`credential.helper=!gh auth git-credential` where the URL's credential is refused (map §6, git remote) — and open the
pull request against `main`. A failed assert here is BLOCKED.

### 3.2 The self-tests and G-RULE

```
P /root/tz36-work/wt/advisor/selftest-adv3.py
P /root/tz36-work/wt/advisor/adv3-bot.py --selftest
I selftest
I rule
```

They must print `SELFTEST-ADV3 PASS: 44 of 44 checks passed`, `SELFTEST PASS: 19 of 19 checks passed`, `SELFTEST PASS: 26 of 26
checks passed` and `READING RULE: PASS - 7 of 7`. The first, second and third reach no network; `I rule` reads `git show
origin/main:advisor/adv3.py` and the branch's files. A red check stops the run here, and it goes to §3.7 and §9.

### 3.3 The directories beside this session

```
P /root/btc-5m-twap/research/tz35-advisor-deploy.py scratch "$(dirname "$S")"
```

lists every UUID directory beside this session's own and names each **live** — born from 1 s before to 60 s after the start
of a running process whose `argv[0]` is `claude` or ends in `/claude.exe` — or **earlier**. **B-RECLAIM-SCRATCH**, for
every directory it names **earlier** — none it named live, and never this session's own:

```
P /root/btc-5m-twap/research/tz35-advisor-deploy.py reclaim <each earlier directory, by its full path>
rm -rf <one such directory>; echo "exit=$?"
test -e <that directory>; echo "exit=$?"
```

One `reclaim` names every earlier directory and must print `RECLAIM PASS` before any removal; then one `rm -rf` and one
`test -e` a directory, the last reading `exit=1`. TZ-35's checker is `main`'s, frozen by the map's table, and its `reclaim`
refuses a directory born with a running claude process and any path that is not a UUID directory under `/tmp/` whose parent's
name carries `btc-5m-twap`. Map §3 expects TZ-35's two directories, named in §0.3, unless a reboot emptied `/tmp`. If `scratch`
names none earlier, the block is recorded as empty and skipped. **A refused `rm -rf` is handed to the Boss** as one exact
command a tree, and verified by `test -e` (map §6, sandbox limit).

### 3.4 G-HISTORY

```
timeout 1800 P /root/tz36-work/wt/advisor/adv3.py --history /root/tz36-work/history.json
sha256sum /root/tz36-work/history.json; wc -c /root/tz36-work/history.json
```

It must print `READING G-HISTORY: PASS - 20 of 20 equal`, and the file must be `19,434` bytes with SHA-256
`99e6a47d6aa4ac96eff0a84ca31fc720bdaf734c0f2084d3c7f9350c406b668c` — **DETERMINISM**, the bytes the Architect's runs of 2026-10-31 wrote on two separate fetches of the
archive (§4.2). Anything else, a timeout included, is BLOCKED, and nothing is deployed.

### 3.5 B-DEPLOY, then COPY and G-RENDER

All of §3.1 to §3.4 PASS first. Then **B-DEPLOY**, which waits for its band and records its mark inside the block:

```
until s=$(( $(date +%s) % 86400 )); [ $s -ge 23700 ] && [ $s -le 85500 ]; do sleep 5; done; { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz36-work/stage/research/tz36-advisor-trust.py mark deploy && cp -p /root/adv3-bot-svc/adv3.py /root/tz36-work/adv3.before && cp -p /root/adv3-bot-svc/commit.txt /root/tz36-work/commit.before && git -C /root/tz36-work/wt show origin/tz-36-advisor-trust-block:advisor/adv3.py > /root/adv3-bot-svc/adv3.py.new && mv /root/adv3-bot-svc/adv3.py.new /root/adv3-bot-svc/adv3.py && git -C /root/tz36-work/wt rev-parse origin/tz-36-advisor-trust-block > /root/adv3-bot-svc/commit.txt; echo "exit=$?"; } >> /root/tz36-work/logs/NN-b-deploy.log 2>&1
```

06:35:00 to 23:45:00 UTC is seconds `23,700` to `85,500` of the day. `exit=0`, or B-ROLLBACK (§4.5). The
running process keeps the old code in memory until it is signalled. Then:

```
I copy
I render
```

`I copy` must print `READING COPY: PASS - 5 of 5`; `I render` runs the service copy's `adv3.py` twice against `fapi.binance.com` — the message
and its `--json` report — and must print `READING RENDER: PASS - 10 of 10`. A FAIL of either is B-ROLLBACK (§4.5), and nothing
is signalled.

### 3.6 P-START, B-KILL, then UNIT-NEW

Only after COPY and G-RENDER PASS. **P-START**, CANON hard rule 14's proof of the request path, through the service copy's own functions:

```
P /root/adv3-bot-svc/adv3-bot.py --probe
```

It must print `READING P-START: served - 5 of 5 endpoints` (§4.3): one request to each of `fapi.binance.com`'s klines, funding rate, premium index
and funding info, and Telegram's `getMe`. A FAIL is B-ROLLBACK (§4.5), and nothing is signalled. Then **B-KILL**, its mark inside the block:

```
until s=$(( $(date +%s) % 86400 )); [ $s -ge 23700 ] && [ $s -le 85800 ]; do sleep 5; done; { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz36-work/stage/research/tz36-advisor-trust.py mark kill && systemctl kill --signal=SIGTERM adv3-bot.service; echo "exit=$?"; } >> /root/tz36-work/logs/NN-b-kill.log 2>&1
```

06:35:00 to 23:50:00 UTC keeps the restart inside the UTC day of the message it must not send again. `I mark kill` fails —
and nothing is signalled — where `daily-sent` is not today's UTC date. At least 45 s later, then every 15 s while it
prints `NOT YET` and exits `3`, and for at most 100 s after the mark: `I unit new` — **UNIT-NEW**, `READING UNIT-NEW: PASS - 9 of 9`.
`RestartSec=30` and the start put the new process 35 s after the signal in TZ-35's run. A FAIL is B-ROLLBACK (§4.5).

### 3.7 The closing reads

```
TZ=UTC systemctl show adv3-bot.service btc-recorder.service btc-pairbook.service btc-rewardbook.service btc-pairbook-archive.service btc-rewardbook-archive.service -p Id -p MainPID -p NRestarts -p ActiveState -p Result -p Nice -p MemoryCurrent -p MemoryPeak -p ActiveEnterTimestamp
TZ=UTC systemctl list-timers btc-pairbook-archive.timer btc-rewardbook-archive.timer --all --no-pager
systemctl is-enabled adv3-bot.service; echo "exit=$?"
journalctl -u adv3-bot.service --no-pager -o short-iso | tail -n 20
tail -n 30 /var/lib/adv3-bot/service.log
ls -la /var/lib/adv3-bot /root/adv3-bot-svc
free -b; df -B1 --output=source,size,avail /var/lib/btc-recorder
du -sb /root/tz36-work /root/adv3-bot-svc /var/lib/adv3-bot /var/lib/btc-rewardbook /var/lib/btc-pairbook /root/.claude
cat /root/tz36-work/state.json
```

The journal holds systemd's own lines for the unit; `service.log` the service's own, one line a start, a refresh, a message and a
failure, with no token and no chat id. The Boss's next «сигнал», or the 06:00 UTC message of the next day, is the first message the
running unit builds with the new code; nothing in this TZ sends or fakes one.

---

## 4. The gates — fixed here, before any of their data exists

| gate | population | PASS | false failure | power, against |
|---|---|---|---|---|
| **G-RULE** | `origin/main`'s `adv3.py` and the branch's; their `adv3-bot.py` and `RULE-ADV-3.txt` | 7 of 7 (§4.1) | `0` — the syntax trees read directly | `1`, a rule function, a constant, the bot or the rule text changed beyond Appendix A |
| **SELFTESTS** | the three self-tests | 44 of 44, 19 of 19 and 26 of 26 | `0` | `1`, a changed expectation or a red check |
| **G-HISTORY** | the rule and the STRONG strategy on the 42 coins' archive history to the close of 2026-10-27 | 20 of 20 facts equal to `FACTS`, and the file's bytes the Architect's | `0` — one function on the archive's files; a republished candle is itself a finding | `1`, a fact mistyped into `FACTS`, or a history not the Architect's |
| **COPY** | the service copy | 5 of 5 (§4.3) | `0` | `1`, a file not Appendix A's or not the branch head's |
| **G-RENDER** | the service copy's two live runs, message and report | 10 of 10 (§4.3) | `0` — the report's figures compared with each other and with fixed labels | `1`, a message without its blocks, a card without its basis, a book whose total is not its parts' sum |
| **P-START** | five endpoints, one request each, through the service copy's own functions | `READING P-START: served - 5 of 5 endpoints` | `0` — each read directly | `1`, a refused request — `451`, `403` — or a reply of another shape |
| **UNIT-NEW** | the unit after the signal | 9 of 9 (§4.3) | `0` | `1`, a process not new, not the new code's, a daily sent again, a capture unit moved |

**Family-wise false failure `0`:** every gate reads its quantity directly and none samples. A FAIL before B-DEPLOY is BLOCKED and
deploys nothing; a FAIL of COPY, G-RENDER, P-START or UNIT-NEW is B-ROLLBACK (§4.5).

### 4.1 G-RULE

`I rule` asserts seven: the functions that changed are exactly `card`, `card_lines`, `facts_checks`, `history`, `message` and
`report`; the functions added are exactly `book_line`, `forward_book`, `signed`, `trust` and `trust_lines`; no function is
removed; the fourteen rule functions of §2 are identical by `ast.dump`; of the module's assignments only `FACTS` changed and
`RELIABILITY, STRONG_JUSTIFIED` was added; `adv3-bot.py` is `main`'s, byte for byte; `RULE-ADV-3.txt` is `main`'s, hashes to
`ee206e7c…` and that hash is the `RULE` constant of the branch's `adv3.py`.

### 4.2 G-HISTORY and DETERMINISM

`adv3.py --history PATH`: the history re-derived from the archive — the 42 coins' monthly kline files from 2019-09, the
daily files of months without one, the monthly funding files through 2026-09 and `+0.01%` per 8 h where none — written to
`PATH` as JSON, then each of the **20** facts read against `FACTS`, at its four decimals: for the rule and for STRONG,
the trades, the profitable trades, the mean R, the median days held, the one-sided `p` of the daily portfolio R, the
share of the class's R that its five best trades hold, and the three shares; and the two gates' verdicts — 9 + 9 + 2.
**PASS** at 20 of 20 with the file's bytes `19,434` long and SHA-256 `99e6a47d6aa4ac96eff0a84ca31fc720bdaf734c0f2084d3c7f9350c406b668c`. TZ-35 fixed `19,362`
bytes and `bcee5309…` for the unchanged function, which the Architect's run of 2026-10-31 under Python 3.13.18 wrote
again to the byte; the changed function adds one key to each class's record and writes the bytes fixed here, which that
Python wrote on 2026-10-31 on two separate fetches of the archive. The two additions, from that run: the one-sided `p`,
`0.022629…` for the rule and `0.054523…` for STRONG; the top-5 share, `0.30418…` and `1.00933…`. A run after the archive
publishes October's monthly files reads October's candles from them in place of the daily files; candles to the close of
2026-10-27 alone enter, so the bytes stay the same unless the archive republished a candle — itself a finding, and BLOCKED.

### 4.3 COPY, G-RENDER and UNIT-NEW

**COPY** (`I copy`), five: the service copy holds `adv3.py`, `adv3-bot.py` and `commit.txt` and nothing else; `adv3.py` hashes to
Appendix A's; `adv3-bot.py` is unchanged; `commit.txt` is 40 hex characters and a newline equal to the worktree's `HEAD` and to
`origin/tz-36-advisor-trust-block`; the branch's `adv3.py` equals the service copy's byte for byte.

**G-RENDER** (`I render`), ten: the message run exits `0` with no traceback; the message holds the forward book, the six ratings
and their lines, by label; every card holds its basis and its invalidation, and there are at most three; the message is under
12,000 characters, three Telegram parts; the report run exits `0` with no traceback; the report is the frozen rule's and has 42
coins; the ratings read system `1`, STRONG not justified, the data fresh, a trade `0` or `1` for each card; each book's entries
are its closed plus its open and its total is the two parts' sum to `1e-9`; each book's days are the closes from 2026-10-28
to the report's; each card carries a rank 1 to 3 and a sum of signs of size 2 to 4. **Only counts and labels are printed.**

**P-START** is `adv3-bot.py --probe`, unchanged from TZ-35's: it asserts each of its five replies served and parsed — closed daily candles of BTCUSDT, the last at most two days old; funding settlements; a mark price for every one of the 42 coins; the funding intervals; and `getMe` answering `is_bot`.

**UNIT-NEW** (`I unit new`), nine, read against the `kill` mark's snapshot: the unit `active`, `running`, `enabled`; a new
`MainPID` and `NRestarts` one more; the process started after the mark and within 90 s of it; its argv the unit's exact one, alone;
the service copy's `adv3.py` Appendix A's and the process started after B-DEPLOY's copy; `adv3-bot.py` and the unit file unchanged;
`daily-sent` and the journal's count of `daily` records as at the mark — the Boss's own requests add records of another kind; `service.log` showing the new process serving, no daily sent and no
traceback since the mark; the three capture units active with their `MainPID` and `NRestarts` as at the mark.

### 4.4 The six ratings — what Appendix A computes

Each is a function of recorded facts. **System reliability** is the constant `RELIABILITY`: `0` where the forward record read
DISPROVEN, `1` until it is read — and after a reading that is UNDECIDABLE — `4` where it read PROVEN; `2`, `3` and `5` are not
used, because CANON PART VII reads the forward record once and running figures decide nothing. **Signal confidence** of a trade is
`RELIABILITY`, and `0` where its card offers no entry or the mark prices failed: the rule gives no probability of a trade, so a
trade cannot be better evidenced than the system. **STRONG classification justified** is the constant `STRONG_JUSTIFIED`, true only
where the STRONG strategy's own forward record read PROVEN; its reason carries the history's `p`, the top-5 share and the rest of
the class's mean R, computed from `FACTS`, and the forward's closed trades of its entries. **Evidence quality** is low while
`RELIABILITY` is 1 or less, whatever the data; otherwise high where the close is the day before the report's, every coin was served and
the mark prices came, else medium. **Expected net expectancy** is "not established" while `RELIABILITY` is below 4, with the history's
means named as in-sample and not a forecast. **Key invalidation condition** is the card's: the price at its stop, or the close of a day
that takes the sum of signs below 2 for a long, above −2 for a short. Only a TZ that reads the forward record changes `RELIABILITY` or
`STRONG_JUSTIFIED`; that TZ changes them and nothing else.

### 4.5 The stops — CANON hard rule 14

**The unit's restart policy is TZ-35's, unchanged** — `Restart=always`, `RestartSec=30`, `RestartPreventExitStatus=3 4` — and so is its stop, K-35, `systemctl disable --now
adv3-bot.service`, which K-36 repeats. **B-ROLLBACK**, on a FAIL of COPY, G-RENDER, P-START or UNIT-NEW, at once, the Executor's own: the file and `commit.txt` return to what
B-DEPLOY saved.

```
{ date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz36-work/stage/research/tz36-advisor-trust.py mark rollback && cp -p /root/tz36-work/adv3.before /root/adv3-bot-svc/adv3.py.new && mv /root/adv3-bot-svc/adv3.py.new /root/adv3-bot-svc/adv3.py && cp -p /root/tz36-work/commit.before /root/adv3-bot-svc/commit.txt; echo "exit=$?"; } >> /root/tz36-work/logs/NN-b-rollback.log 2>&1
sha256sum /root/adv3-bot-svc/adv3.py; cmp /root/adv3-bot-svc/commit.txt /root/tz36-work/commit.before; echo "cmp exit=$?"
```

`exit=0`, the `sha256sum` printing `7f2863a5…` and `cmp` exit `0`, or the run is BLOCKED with the file's state named. Where the unit was **not** signalled (a FAIL of COPY,
G-RENDER or P-START) that is all: the running process never loaded the new file. Where it **was** (a FAIL of UNIT-NEW), the signal follows, its mark inside the
block, in the band of §3.6:

```
until s=$(( $(date +%s) % 86400 )); [ $s -ge 23700 ] && [ $s -le 85800 ]; do sleep 5; done; { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz36-work/stage/research/tz36-advisor-trust.py mark kill2 && systemctl kill --signal=SIGTERM adv3-bot.service; echo "exit=$?"; } >> /root/tz36-work/logs/NN-b-kill2.log 2>&1
```

and at least 45 s later `I unit old` (every 15 s while it prints `NOT YET`, at most 100 s after that mark) — **UNIT-OLD**, `READING UNIT-OLD: PASS - 10 of 10`: UNIT-NEW's nine read against the second mark with the old `adv3.py`,
and `NRestarts` two more than at the first mark.

**K-36**, on a FAIL of UNIT-OLD only — the advisor is then stopped, and the Boss is told:

```
{ date -u +%FT%T.%NZ; systemctl disable --now adv3-bot.service; echo "exit=$?"; } >> /root/tz36-work/logs/k36.log 2>&1
```

by the classifier route where refused (map §6, sandbox limit: the Boss runs the block), verified at least 30 s later by
`I stopped`, which must print `READING STOPPED: PASS - 2 of 2`. **UNDECIDABLE closes nothing and stops nothing; under PASS K-36 is not run.**

### 4.6 What a PASS establishes, and what it does not

The service copy's `adv3.py` is Appendix A's and the unit runs it; the rule's fourteen functions, the rule text, the bot and the unit
are byte-for-byte or tree-for-tree what TZ-35 deployed; the facts the message quotes — now twenty — re-derive from Binance's archive
to the last digit; the live message and report carry the forward book in parts, a basis and an invalidation on every card, and the six
ratings, their figures consistent with each other; and the three capture units are as they were. **Not established:** that the Boss's
Telegram shows the message — Telegram's rendering of the added lines is the Boss's next «сигнал»; the ratings' truth, which is the
forward record's, read after 2027-10-28; and anything about the market to come.

---

## 5. The files

**`advisor/adv3.py`** — replaced: `FACTS` gains `p_up` and `top5_share`; `RELIABILITY` and `STRONG_JUSTIFIED` are added; `history`
computes each class's top-5 share; `facts_checks` reads twenty facts; `report` keeps the base rule's open positions, builds `book`
with `forward_book`, ranks the cards and adds `trust`; `card` carries the sum of signs; `message` replaces the forward line by the
book and appends `trust_lines`; `card_lines` adds the basis and the invalidation; `forward_book`, `trust`, `signed`, `book_line` and
`trust_lines` are new. Every other line is TZ-35's. **`advisor/selftest-adv3.py`** — replaced: twelve more checks (32 to 44) and the
twenty-fact comparison of check 7. **`research/tz36-advisor-trust.py`** — this TZ's checker: `fingerprint`, `host`, `number`, `rule`,
`selftest`, `mark`, `copy`, `render`, `unit`, `keep` and `stopped`. Where a reading can be a pure function it is — `parse_map`, `rule_checks`,
`number_reading`, `render_checks`, `unit_checks`, `log_since`, `daily_records` and `kept_files` — and its self-test runs each on stand-ins, with a
negative control for every one that can fail; `host`, `copy`, `mark`, `keep` and `stopped` read the host and are exercised there. It starts, stops and
signals nothing; its `render` runs the service copy's `adv3.py`. Standard library alone, under `/root/tz04a-env`.

---

## 6. Cost

Measured by the Architect on 2026-10-31 under Python 3.13.18 and taken at the population's upper bound.

| check | population | measured | bound |
|---|---|---|---|
| the three self-tests | 44, 19 and 26 checks, no network | under `1` s each | `30` s each |
| G-RULE, fingerprint, NUMBER, COPY, the marks | `git show`, two parses, 55 files, systemd, small files | fingerprint and G-RULE together `0.09` s, the rest under `1` s | `5` s a run |
| G-HISTORY | the 42 coins' archive from 2019-09: about 8,400 requests, most `404` before a listing | `220.7` s elapsed and `23.0` s of processor (`20.8` user, `2.2` system) at 16 workers, peak `79,220,736` bytes, 2026-10-31 | `1,800` s, the `timeout`; `120` s of processor |
| G-RENDER | two live runs of the service copy: 42 coins' 1,500 candles and funding, marks, intervals | TZ-35 measured `1.2` to `1.4` s of processor a run, a message `0.7` to `1.3` s | `600` s of wall each, the checker's `timeout` |
| P-START | five requests, one after another | TZ-35: `0.1` to `0.2` s | `546` s of wall at worst — four requests at `129` s and one at `30` s — without processor |
| UNIT-NEW | `systemctl show`, `/proc`, the log | under `1` s a run | at most 8 runs |

**Single-session processor at most `500` s at those bounds** — the self-tests `90`, G-HISTORY `120`, G-RENDER and P-START `30`, at most 40 checker
runs at `5` s, `200`, and the `reclaim`, `git` and `systemctl` commands `60` — **under `3,600`, so nothing is sampled.** **Wall clock about 45 minutes:** §0 to §3.3 about 10
minutes; §3.4 4 to 10; §3.5's wait, none inside the band, and about 3 minutes; §3.6 about 3; §3.7 and §9 about 10; **about 1 h 15 min with every `timeout` and every request at its bound, plus a wait for a band that is at most 6 h 50 min**, from 23:45:00 to 06:35:00 UTC. **The host pays,
after the session:** nothing it did not pay before; the message is one more screen of lines.

---

## 7. Validation

| # | check | count |
|---|---|---|
| **V1** | §0.2's fingerprint | `READING FINGERPRINT: PASS - 64 of 64`: revision `2026-10-29-b`; 6 anchors, 4 re-derived; 55 rows, 52 of 52 `frozen` equal |
| **V2** | §0.3's host gate | `READING HOST: PASS - 16 of 16` |
| **V3** | §0.5's NUMBER, at §0.5 and at §3.1 | `READING NUMBER: PASS - 2 of 2` each, the `TZ-36-` path printed; the branch count `0` |
| **V4** | §0.1's and §3.1's files | 3 of 3 hashes asserted at each, lines and bytes; the branch's diff naming exactly `M`, `M`, `A`, and `--numstat` exact |
| **V5** | the self-tests | `44 of 44`, `19 of 19`, `26 of 26` |
| **V6** | G-RULE | `READING RULE: PASS - 7 of 7` |
| **V7** | G-HISTORY and DETERMINISM | `20 of 20 equal`; the file `19,434` bytes, SHA-256 `99e6a47d…` |
| **V8** | B-DEPLOY | `exit=0`; the mark printed |
| **V9** | COPY | `READING COPY: PASS - 5 of 5` |
| **V10** | G-RENDER | `READING RENDER: PASS - 10 of 10`, the message's and the report's sizes printed |
| **V11** | P-START | `READING P-START: served - 5 of 5 endpoints`, each line printed |
| **V12** | B-KILL and UNIT-NEW | `exit=0`; `READING UNIT-NEW: PASS - 9 of 9`, both pids, both instants |
| **V13** | contract §4.2's self-check | run after the push and the pull request and before the report's commit |
| **V14** | §3.7's closing reads | every read printed |
| **V15** | B-RECLAIM-SCRATCH and §9's `keep` | files considered, copied and held; the store's count after equal to before plus the copies |
| **V16** | §9's removals | `git worktree remove` without `--force` exit `0`; `test -e` exit `1` for `/root/tz36-work` and each directory removed; `git worktree list` naming `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else |

---

## 8. The report

`CryptoReports/TZ-36-advisor-trust-block-report.md`, in contract §8's order. **In its first ten lines:** NUMBER at both reads; G-RULE;
the three self-tests; G-HISTORY and its bytes; B-DEPLOY, COPY, G-RENDER and P-START; B-KILL and UNIT-NEW with the pids; whether a rollback ran; whether the unit
runs, and how that was verified. Beyond what V1 to V16 print: every mark's instant; every block the classifier refused, who ran it and when; the unit's
journal lines; each memory and free-space read with its instant and bound; the commit and the pull request; §9's counts and removals; and every file the
run wrote, by SHA-256, but the bot's own root. **It never prints the token, the chat id, the content of any file under `/etc/adv3-bot/`, or a coin, a
price or a size from the live message** (§2 item 7). The report is drafted in the primary checkout `/root/btc-5m-twap` before B-RECLAIM-OWN and committed
after it.

---

## 9. Reclaim — the host left clean (CANON hard rule 15)

**What a file is kept for:** `I keep` copies every file under `logs/`, `state.json`, `history.json`, `adv3.before` and `commit.before` into
`/root/btc-forensics/` as `tz36-work--<path with - for />`, by exclusive create, and verifies each hash; a name already there with the same hash
is counted as held, and with another a failed assert. The branch worktree is not copied: `keep` asserts that `git status --porcelain --ignored` in
it prints nothing and that its `HEAD` is its upstream's, so `git worktree remove` needs no `--force`. **No output of `keep` or `reclaim` is
filtered**: every line it prints is quoted. B-RECLAIM-SCRATCH is §3.3.

**B-RECLAIM-OWN**, last, after §3.7 and with the report drafted. **Its output is written to no file; the report quotes it verbatim from the
session**, every line of it:

```
nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz36-work/stage/research/tz36-advisor-trust.py keep
git -C /root/btc-5m-twap worktree remove /root/tz36-work/wt; echo "exit=$?"
rm -rf /root/tz36-work; echo "exit=$?"
test -e /root/tz36-work; echo "exit=$?"
git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
find /root/btc-forensics -type f | wc -l
df -B1 --output=source,size,avail /var/lib/btc-recorder
```

The branch `tz-36-advisor-trust-block` stays on `origin` and as a local ref; only its working tree goes. **Kept:** `/root/adv3-bot-svc/` is the running
unit's code, `/var/lib/adv3-bot/` its record, `/etc/adv3-bot/` the Boss's token and the pinned chat; the capture roots, both archives' state and the
forensic store are data, never scratch. **A refused `rm -rf` is handed to the Boss** by §3.3's route, one tree per command, and verified by `test -e`.

---

## 10. Pre-send checks

Performed by the Architect on 2026-10-31 against this file as sent, in a reading separate from its writing — the body was written, read
start to end and corrected where it read wrongly, and this section written after — with the repository at `origin/main`
`d97dd19d9c48717a6dad73142c011be85e827ea5` and map revision `2026-10-29-b` as `main` carries it. Line numbers are those of the files
§0.1 extracts for Appendix A, and those of `main` for committed code.

| # | check | result |
|---|---|---|
| **C1** | scope against body | **Repository paths the body names:** `CryptoTZ/TZ-36-advisor-trust-block.md`, read by §0.1's script and named by `number`; `CryptoTZ/` and `CryptoReports/`, listed by `number`, every `CryptoReports/*.md` read by TZ-35's `reclaim` for hash tokens; `SYSTEM-MAP.md` and the 54 other rows of its table, read by `fingerprint`, among them `BTC-EXECUTOR-INSTRUCTIONS.md` (cited for contract §1, §4.1, §4.2 and §8), `deploy/systemd/adv3-bot.service`, `research/tz33-reward-book-capture.py` (cited for line 190) and `research/tz35-advisor-deploy.py` (run for `scratch` and `reclaim`); the three files of Appendix A, written on the branch, `adv3.py` also copied to the service; `advisor/adv3-bot.py` and `advisor/RULE-ADV-3.txt`, read by `rule`, run or hashed, never written; `CryptoReports/TZ-36-advisor-trust-block-report.md`, written to `main`. **Host paths:** `/root/tz36-work/**` written; `/root/adv3-bot-svc/adv3.py` and `commit.txt` written, `adv3.py.new` transient; `/var/lib/adv3-bot/{daily-sent,journal.jsonl,service.log}` read; `/etc/adv3-bot/token` read by the bot's own `--probe` and nowhere else; `/etc/systemd/system/adv3-bot.service` hashed; `/var/lib/btc-recorder` read by `find`, `grep -c` and `df`; the capture stores by `du`; `/root/btc-forensics` written by `keep` and `reclaim`; `/proc` read; the UUID directories of `/tmp` read, copied from and removed by TZ-35's checker. **Entry points:** this checker's modes `fingerprint`, `host`, `number`, `rule`, `selftest`, `mark` (four marks), `copy`, `render`, `unit` (`new`, `old`), `keep` and `stopped`; TZ-35's `scratch` and `reclaim`; `selftest-adv3.py`; `adv3-bot.py --selftest` and `--probe`; `adv3.py --history`, and its default and `--json` modes under `render`; `git` (`fetch`, `ls-remote`, `log`, `worktree`, `add`, `diff --cached`, `commit`, `push`, `show`, `rev-parse`, `status`), `gh`'s credential helper; `systemctl` (`show`, `list-timers`, `is-enabled`, `kill`, and `disable` at K-36 only); `journalctl`, `cp`, `mv`, `sha256sum`, `cmp`, `timeout`, `nice`, `rm -rf`, `test -e`, `du`, `df`, `free`, `find`, `grep`, `wc`, `ls`, `cat`, `tail`. **Outputs:** under `/root/tz36-work/` `logs/`, `stage/`, `wt/`, `state.json`, `history.json`, `adv3.before`, `commit.before`; the service copy's two files; the forensic store's copies; the branch, its pull request and the report. **Intersections with §2, by path and by content class, seven, each named in §2:** the bot's `--probe` reads the token — item 3's exemption; G-RENDER's requests — item 3; `systemctl is-enabled` and `list-timers` — item 4, **where `is-enabled` was missing and is added in this reading**; `find`, `grep -c` and `df` under the recorder's root — item 5, **where only `show`, `list-timers` and `du` were named and the three are added in this reading**; `tail` of `service.log`, `journalctl` of the unit, `cat state.json` and `ls` of the record — item 7: they carry log lines, pids, instants and sizes, and `service.log`'s refresh line names a coin the source did not serve, never a price; `history.json` — item 6: counts, R and shares, no price, kept in the work tree and the store; the live message and report — item 7: never printed, `render` prints sizes and `READING` lines. **Classes checked and intersecting nothing:** labels, outcomes and settled documents — this TZ reads none; Binance's candles pass through the service copy and the live runs and are stored nowhere but inside `history.json`'s derived figures, which hold none. |
| **C2** | origin of every expectation | **Quoted from a committed artifact:** `55`, `52`, `2`, `1`, the six anchors and `2,205` — map `2026-10-29-b` §0 and §3, counted independently of the checker by a parse of the table (55 rows, 52 frozen) and then by `fingerprint` against the repository at `d97dd19`, `PASS - 64 of 64`; the TZ-35 hashes `7f2863a5…`, `76bad371…`, `e65de91c…`, `ee206e7c…`, `82acd8e4…` — map §0's table rows, and `sha256sum` of the files at `d97dd19`; `85,172,224` and `72,032,256` — map §7 item 131; `7,300,000,000` — `research/tz33-reward-book-capture.py` line 190, `STREAM_FLOOR = 7300000000`; `31612203008` and `e3975b5…` — map §6's host identity. **Computed by an implementation independent of the one under test, to the digit:** the new `FACTS` literals — the top-5 shares `0.3042` and `1.0093` by a sort of the trades' R in a script of the Architect's (`252.4` and `139.77` over `829.73` and `138.48`), the one-sided `p` `0.0226` and `0.0545` by `mean / sd · sqrt(n)` and `0.5 · erfc(t / sqrt(2))` over the daily R of the same 2,492 days (`t` `2.0022` and `1.6025`), both equal to `adv3.stats`'s and `history`'s; `19,434` bytes and `99e6a47d…` — the bytes `adv3.py --history` wrote on two runs of 2026-10-31 under Python 3.13.18, each on a separate fetch of the archive, the second on this TZ's final bytes, after the unchanged function had written TZ-35's `19,362` bytes and `bcee5309…` again to the byte on the same fetch method — a reproduction target fixed before any run of this TZ; `115 16`, `48 2` and `582 0` — `git diff --cached --numstat` over the extraction of Appendix A into a copy of the repository at `d97dd19`, exact; the hashes, lines and bytes of §0.1 — `sha256sum` and `wc` over the three files, and §0.1's script run against this file, equal. **Fixed by Appendix A's code, which this TZ measures nothing to set:** `16`, `2`, `7`, `5`, `10`, `9`, `10` and `2` (HOST, NUMBER, RULE, COPY, RENDER, UNIT-NEW, UNIT-OLD, STOPPED), `5` endpoints, `44`, `19` and `26`, `20` (G-HISTORY) — each the count its function's dictionary holds, re-run by the Architect where it runs off the host (C5). **Fixed by §4 and measured by nothing:** the 90 s and 100 s windows, the 45 s wait, the 12,000 characters. **§0.4's floors and §3's bands:** `170,344,448` = 2 × `85,172,224`; `7,400,000,000` = `7,300,000,000` + `100,000,000`; `23,700` = 6 × 3,600 + 35 × 60, `85,500` = 23 × 3,600 + 45 × 60, `85,800` = 23 × 3,600 + 50 × 60. **No expectation depends on a quantity this TZ measures but as an inequality or an equation that holds for every admissible value of it:** UNIT-NEW reads `NRestarts` as the `kill` mark's plus one, the capture units' as the mark's, and the journal's daily records as the mark's — whatever the mark read. |
| **C3** | shape of every diff | Three paths. **`advisor/adv3.py` replaces 16 committed lines**, read from `git diff --no-index -U0` against the file at `d97dd19`: lines `27` (the facts' comment), `29` and `31` (the two `mfe` lines of `FACTS`), `418` (`b_trades, b_daily = [], {}`), `422` (`tf, df, _ = simulate(…)`), `427` to `430` (the four lines of `report`'s `return`), `443` (`card`'s first `out = {` line), `559` to `562` (the forward line of `message`) and `626` to `627` (`facts_checks`' docstring) — `--numstat` `115 16`: 115 lines added, 16 removed. **`advisor/selftest-adv3.py` replaces 2**: lines `116` and `117` (the dictionary of check 7 and its `20`-fact assertion line, whose old text read `16`) — `48 2`. **`research/tz36-advisor-trust.py` is new**: `git cat-file -e origin/main:research/tz36-advisor-trust.py` exits `128`, so the change replaces none of its lines; the report's path exits `128` as well. The words "insertions only" appear in this TZ in this cell alone. |
| **C4** | cost of every check | §6, at the population's upper bound. **Processor, single session, term by term:** the three self-tests `3 × 30 = 90` s; G-HISTORY `120` s against `23.0` s measured; G-RENDER's two runs and P-START `30` s against `1.2` to `1.4` s a run measured by TZ-35; at most 40 checker runs `40 × 5 = 200` s — fingerprint and rule together measured `0.09` s, selftest `0.08`; and `reclaim`, `git` and `systemctl` commands `60` s: **`90 + 120 + 30 + 200 + 60 = 500` s, under `3,600`; nothing is sampled.** **The fail-fast bounds, each with its derivation:** G-HISTORY's `timeout 1800`; `adv3.get`'s four tries — four `30` s timeouts and the `1`, `3` and `5` s between them, `129` s, `adv3.py` lines 36 to 54, unchanged by this TZ; P-START's five requests one after another, `4 × 129 + 30 = 546` s of wall, `adv3-bot.py` lines 271 to 293; each G-RENDER run under the checker's `timeout=600` s; UNIT-NEW's `NOT YET` at most 100 s after the mark, every 15 s, at most 8 runs. **Wall clock:** about 45 minutes, about 1 h 15 min with every bound reached — `10 + 30 + 20 + 9 + 2 + 4 = 75` minutes — plus a wait for a band of at most 6 h 50 min. Disk at the same bound: §0.4's `100,000,000`; the history file is `19,434` bytes. |
| **C5** | every count | `64` = 1 revision + 6 anchors + 4 re-derived + 52 frozen rows + 1 table shape, the map's table read by `parse_map` and counted again by the Architect's script — `55` rows, `52` frozen, `2` tracked, `1` reported. `16`, `mode_host` lines 268 to 302: H1 one, H2 two, H3 one, H4 three, H5 six, H6 one, the memory gate and the disk gate; re-run on stand-ins, `16 of 16`. `2`, `number_reading`, lines 305 to 308. `3` files and `3` hashes, §0.1. `7` = 5 of `rule_checks` (lines 153 to 166) + the bot and the rule text, `mode_rule` lines 327 to 334; run on the repository at `d97dd19` against the extracted files, `7 of 7`. `44` = 32 + 12: the twelve are the three of check 6 (each card's basis and invalidation, the message's blocks, the book's identity), the one of check 7 (a top-5 share not derived reads DIFFERENT), the three of the new check 9 (the forward book by hand) and the five of check 10 (`trust`) — counted by `grep -c "check("` less its definition, `45 - 1`; run on the finished bytes and on the files extracted by §0.1's script, `44 of 44`. `19`: `adv3-bot.py --selftest`, unchanged, `19 of 19` with the new `adv3.py`. `26`: the checker's `selftest`, `26 of 26`. `20` = 2 classes × 9 + 2 verdicts, `facts_checks` lines 721 to 739, printed `20 of 20 equal` on two runs. `5`, `mode_copy` lines 371 to 382, `5 of 5` on a stand-in. `10` = 5 + 5, `render_checks` lines 169 to 197, `10 of 10` on a real message and report built by the new code and on a stand-in service copy. `5` endpoints, `probe`, `adv3-bot.py` lines 271 to 293, unchanged. `9`, `unit_checks` lines 200 to 220, and `10` with its extra; `9 of 9` on stand-ins, with four negative controls and the `NOT YET`. `2`, `mode_stopped`. V1 to V16 are the sixteen rows of §7. The checker's `--numstat` is `582 0`: 582 lines added, none removed. |
| **C6** | every population | NUMBER: the paths under `CryptoTZ/` and `CryptoReports/` of `origin/main` at each of its two reads. FINGERPRINT: the map's table of 55 rows against the files of the primary checkout. HOST: the host at the instant of the read — its units, files, memory and disk. RULE: `adv3.py`, `adv3-bot.py` and `RULE-ADV-3.txt` of `origin/main` against the branch's. The self-tests: synthetic candles and stand-ins, no network. G-HISTORY: the 42 coins' archive history to the close of 2026-10-27, the rule's trades and the STRONG strategy's. COPY: `/root/adv3-bot-svc` and the worktree. RENDER: the service copy's two live runs — the message and the report of the latest close at the instant of the run, the 42 coins' 1,500 candles each. P-START: five requests, one to each endpoint. UNIT-NEW and UNIT-OLD: the unit, the three capture units, `daily-sent`, the `daily` records of `journal.jsonl` and `service.log`'s lines stamped at or after the mark less 1 s. KEEP: the files of the work tree named in §9. RECLAIM: the UUID directories `scratch` names earlier. Each memory figure: one mode's process; `MemAvailable` and free space: the host at each read. |
| **C7** | every signature and every behaviour | **Committed code this TZ relies on, read at `d97dd19`:** `adv3.py` — `def get(url, tries=4):` line 36, its docstring "A network error, 418, 429 or 5xx is tried again after 1, 3 and 5 s", lines 37 to 54, unchanged; `def simulate(c, fund, first_entry, last_day):` line 237, `return trades, daily, pos` line 261 — the open position is its third value; `def simulate_strong(cs, st, funds, first_entry, last_day):` line 287, `return trades, daily, open_` line 317; `def stats(trades, daily):` line 320, `out = {'trades': len(R), 'wins': sum(x > 0 for x in R), 'total_R': sum(R),` line 322 — the sum of the R of the trades it is given, which `report` gives it closed ones; `def history():` line 351, `base, strong = stats(base_trades, base_daily), stats(s_trades, s_daily)` line 385 — the line after which the loop of the top-5 share is inserted; `def report(cs, funds, marks, deposit, risk, now_ms, missing=(), intervals=None):` line 394, `tf, df, _ = simulate(c, funds.get(coin, lambda d: 3 * BASE_F), FORWARD_FROM, last)` line 422, `'forward': {'base': stats(b_trades, b_daily), 'strong': stats(s_trades, s_daily)},` line 429; `def card(coin, row, is_strong, deposit, risk):` line 433, the modes `'limit'`, `'market'` and `'none'` at lines 440 to 442, `row.get('funding_h')` read at line 446 — the new `row.get('sum')` is the same shape and gives `None` for a row without it; `def num(x, sig=3):` line 457, `if x == 0:` `return '0'` lines 459 and 460; `def message(rep, facts):` line 490; `def card_lines(cd, facts):` line 571; `def facts_checks(h):` line 625. `adv3-bot.py` — `log`, lines 30 to 34, the stamp `%Y-%m-%dT%H:%M:%SZ` then the line; `serve`, line 207 `log('serving the pinned chat: pid', os.getpid(), …)` and line 225 `log('daily sent for the close of', rep['close_of'])` — the two lines `log_since` reads; `make`, lines 163 to 177, `rep = adv3.report(cs, funds, marks, deposit, risk, int(time.time() * 1000), data.missing, intervals)` and `return rep, adv3.message(rep, adv3.FACTS)`; `journal`, lines 180 to 188, reads of `rep` only `rule`, `close_of`, `deposit`, `risk_pct`, `top`, `strong`, `rows` and `cards` with the card keys `coin`, `side`, `strong`, `mode`, `entry`, `stop`, `targets`, `close` and `U` — none removed or renamed by this TZ, so the journal's record is unchanged; `probe`, lines 271 to 293, prints `READING P-START: served - 5 of 5 endpoints`; `selftest`, line 397, `len(chunks(msg)) == 1` — the new message of three synthetic cards passes it, `19 of 19`. The unit — `WorkingDirectory` line 12, `ExecStart` line 13, `Restart=always` 14, `RestartSec=30` 15, `RestartPreventExitStatus=3 4` 16. TZ-35's checker `research/tz35-advisor-deploy.py` — `reclaimable`, lines 279 to 285: a UUID directory under `/tmp/` whose parent's name carries `btc-5m-twap`; `mode_scratch(own)`, lines 419 to 431, lists the siblings of `own`; `mode_reclaim(trees)`, lines 434 to 488, copies the files a report names by hash and asserts the store's count; `main`, lines 774 to 799: `scratch` takes exactly one argument, `reclaim` any number. **Every behaviour this TZ attributes to Appendix A:** `forward_book`, lines 350 to 357 of `adv3.py`; `trust`, 360 to 372; `history`'s loop, 417 to 418; `report`'s book, ranks and `trust`, 427 to 470; `card`'s `'sum'`, line 483; `message`, 531 to 611; `signed`, 614 to 615, `book_line`, 618 to 622, and `trust_lines`, 625 to 660; `card_lines`, 663 to 700, whose two added lines print the basis only where the card carries a sum and a rank; `facts_checks`' two checks, 721 to 739. The checker — `parse_map` 126, `top_level` 142, `rule_checks` 153, `render_checks` 169, `unit_checks` 200, `log_since` 223, `mode_fingerprint` 243, `mode_host` 268, `number_reading` 305, `mode_number` 311, `mode_rule` 327, `daily_records` 337, `snapshot` 349, `mode_mark` 357 — `kill` and `kill2` assert `daily-sent` is today's UTC date —, `mode_copy` 371, `mode_render` 385, `mode_unit` 400 — `NotYet` while the old process runs within 100 s of the mark —, `kept_files` 427, `mode_keep` 436 and `mode_stopped` 466. **Sentences rewritten in this reading:** §0.0 named two exceptions to the logs rule, where only B-RECLAIM-OWN is one; §0.3 said H4's readings were compared "below", where UNIT-NEW compares them; §0.4 took the memory floor from a figure without the rule of map §7 item 131; §1 stated that a closed-only sum is biased low as a fact, where it is modelled; §2 item 4 omitted `is-enabled` and item 5 the recorder-root reads (C1); §3.6 lacked P-START, which CANON hard rule 14 asks of a process's request path; the blocks that signal or restore carried `I` where the Boss may be handed the block, and now carry its full text; and the restart reading counted every journal line, where the Boss's own requests add lines of another kind (now counted by kind). |
| **C8** | every cross-reference | Resolved by reading the text referenced. **Map `2026-10-29-b`:** §0's anchors and its table of 55 rows, 52 / 2 / 1; §1's record of refs; §2.6's `STREAM_FLOOR` `7,300,000,000`; §2.7's record under `/var/lib/adv3-bot/` and the token under `/etc/adv3-bot/`; §3's `2,205` files in the forensic store and TZ-35's two directories left behind; §6's host identity, `/root/tz04a-env` on Python 3.12, the push through `gh`'s credential helper, and the sandbox limit on destructive actions — `systemctl kill` run by the Executor at TZ-20, TZ-21, TZ-27, TZ-33 and TZ-35, `enable --now` refused, a single-tree `rm -rf` sometimes refused and then the Boss's; §7 items 125 and 129, a reload re-arming an archive's run and the rule that a TZ states it, 131, the floor rule applied in §0.4. **CANON `2026-10-29-b`:** PART VII, the advisor, its forward record read once after 2027-10-28 and running figures deciding nothing; hard rules 2 (NUMBER), 5, 10, 12, 13, 14 (P-START, the stop K-36, the restart policy) and 15 (§9); §1.2's last sentence and §1.6; the signal trigger. **Contract:** §1 steps 1 to 4 (`fingerprint`), §4.1 (the order of the branch and the report), §4.2 (V13) and §8 (the report's order). **Other artifacts:** `CryptoTZ/TZ-35-advisor-bot.md`, whose §0.1 script, bands, B-KILL, K-35 and gates this TZ adapts — `diff` shows the changes named; its checker's `scratch` and `reclaim`. **This TZ:** §0.1 to §0.5, §1, §2's items, §3.1 to §3.7, §4.1 to §4.6, §5, §6 and §9, each supporting the sentence that cites it. **None unresolved.** |

**Six checks could not be performed from this session**, and each is a BLOCK condition of this TZ under CANON hard rule 13: the host's
own state — free space, memory, units, interpreter, the service copy's hashes and the Boss's token — `I host`, §0.3; the live
reach of `fapi.binance.com` and `api.telegram.org` under the service's headers — `fapi.binance.com` answers `451` to this session's
container — P-START and G-RENDER, before anything is signalled; systemd's restart of the unit after a `SIGTERM` and its journal —
UNIT-NEW; NUMBER on `main` with this file uploaded — `I number` on the clone at `d97dd19`, which holds no `TZ-36-` file, reads `FAIL - 1
of 2` by design, and the stand-ins read `PASS - 2 of 2` and `FAIL` with a second file and with a report; TZ-35's `scratch` and `reclaim`
against the host's real `/tmp`; and Telegram's rendering of the added lines, which is the Boss's next «сигнал». **Everything else above
was performed here** under Python 3.13.18: the three self-tests, `44`, `19` and `26` of their own; G-HISTORY twice against the archive
itself, the file's bytes equal and the unchanged function's equal to TZ-35's; §0.1's script run against this file — three files, the
stage and a copy of the repository, its numstat exact, and its refusal over a worktree that is not TZ-35's; the checker's `fingerprint`
and `rule` against the repository, `64 of 64` and `7 of 7`; its `host`, `mark`, `unit`, `stopped`, `keep`, `copy`, `render` and `number`
against stand-ins for systemd, `/proc` and the host's files, thirty-three assertions, a negative control for each reading that can fail;
`render_checks` on a real message and report built by the new code from the archive's candles and spot stand-ins for two days; and a
lint of the three files, clean under `-W error`.

---

## Appendix A — the three files, byte for byte

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
# The ratings' two inputs (TZ-36). RELIABILITY, 0 to 5: 1 = the history only, in sample and not disqualified; 0 = the
# forward record read DISPROVEN; 4 = read PROVEN. STRONG_JUSTIFIED: True only where the STRONG strategy's own forward
# record read PROVEN. Only a TZ that reads CANON PART VII's forward record, after 2027-10-28, moves either.
RELIABILITY, STRONG_JUSTIFIED = 1, False


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
    bb, bs = rep['book']['base'], rep['book']['strong']
    if bb['days']:
        lines += ['', f"<b>Форвард с 28.10</b> — день {bb['days']} из 365, бумажный портфель правила, не ваш счёт",
                  book_line('Все сигналы', bb), book_line('STRONG', bs),
                  'Доказанность проверяется после 28.10.2027; текущие R ничего не решают.']
    else:
        lines.append('Форвард начинается с закрытия 28.10; доказанность проверяется после 28.10.2027.')
    lines += [''] + trust_lines(rep, facts)
    lines += ['', '<i>«Дошли» — доля прошлых сделок того же класса (★ STRONG или обычных), цена которых дошла до '
              'цели до выхода. R — результат в единицах риска сделки: −1 R — сработал стоп. Не инвестиционный '
              'совет: правило показывает состояние рынка; решение и риск — ваши.</i>']
    return '\n'.join(lines)


def signed(x, places=2):
    return f'{x:+.{places}f}'.replace('.', ',').replace('-', '−')


def book_line(name, b):
    """One strategy's forward line: the entries, the closed part and the open part apart, and the total over the market."""
    r = lambda x: ('+' if x > 0 else '') + num(x, 3)
    return (f"{name}: входов {b['opened']} · закрыто {b['closed']} ({r(b['closed_R'])} R) · "
            f"в позиции {b['open']} ({r(b['open_R'])} R) · итого {r(b['total_R'])} R")


def trust_lines(rep, facts):
    """The Boss's six ratings with their reasons (TZ-36). Every figure is a frozen fact, a count of this report or a
    figure computed from them; nothing here is a judgement of this moment."""
    tr, bb, bs = rep['trust'], rep['book']['base'], rep['book']['strong']
    b, s = (facts or {}).get('base'), (facts or {}).get('strong')
    status = {0: 'опровергнута форвардом', 1: 'не проверена', 4: 'доказана форвардом'}.get(tr['system'], '')
    why = ''
    if tr['system'] <= 1 and b and s:
        why = (f": история в выборке, p {pct(b['p_up'], 4)} у всех сигналов и {pct(s['p_up'], 4)} у STRONG при пороге "
               f"форварда 0,005; форвард {bb['days']} из 365 дн.")
    out = ['<b>Оценка доверия</b>', f"Надёжность системы: <b>{tr['system']}/5</b> — {status}{why}"]
    if tr['cards']:
        out.append('Уверенность в сделках: ' + ' · '.join(f'{c} {v}/5' for c, v in tr['cards'].items())
                   + ' — не выше надёжности системы; 0 — входа нет; правило не даёт вероятности на сделку')
    else:
        out.append('Уверенность в сделках: сделок нет')
    evidence = ''
    if s:
        rest = s['mean_R'] * s['trades'] * (1 - s['top5_share']) / (s['trades'] - 5)
        evidence = (f" — история в выборке: p {pct(s['p_up'], 4)}, пять лучших сделок = {pct(100 * s['top5_share'], 0)}% "
                    f"её прибыли, остальные {num(rest, 2)} R на сделку; форвард: закрыто {bs['closed']} из {bs['opened']}")
    out.append(f"STRONG обоснован: <b>{'да' if tr['strong_justified'] else 'нет'}</b>{evidence}")
    issues = (([] if tr['fresh'] else ['закрытие не вчерашнее']) + ([f"нет данных по {len(rep['missing'])} монетам"]
              if rep['missing'] else []) + ([] if rep['marks_ok'] else ['нет текущих цен Binance']))
    data = ('данные свежие и полные' if not issues else 'данные: ' + ', '.join(issues)) +         f" (закрытие {ddmm(rep['close_of'])}, {tr['served']} из {len(COINS)} монет)"
    quality = {'low': 'низкое', 'medium': 'среднее', 'high': 'высокое'}[tr['quality']]
    out.append(f"Качество данных: <b>{quality}</b> — {data}{'' if tr['system'] > 1 else '; правило не проверено'}")
    if tr['expectancy_established']:
        out.append('Ожидаемая R на сделку: берётся из прочитанного форварда')
    elif b and s:
        out.append(f"Ожидаемая R на сделку: <b>не установлена</b> — история в выборке: {signed(b['mean_R'])} R у всех "
                   f"сигналов и {signed(s['mean_R'])} R у STRONG, это не прогноз")
    else:
        out.append('Ожидаемая R на сделку: <b>не установлена</b>')
    out.append('Инвалидация: у каждой карточки — стоп и смена сигнала')
    return out


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
    if cd.get('sum') is not None and cd.get('rank'):
        out.append(f"Основание: сумма знаков {signed(cd['sum'], 0)} из ±4 · z {signed(cd['z'])} · ранг {cd['rank']} из {TOP_N}")
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

```text file=advisor/selftest-adv3.py
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
check('each card holds its basis and its invalidation, ranks 1 to 3', msg.count('Основание: сумма знаков') == 3
      and msg.count('Инвалидация: цена') == 3 and [cd['rank'] for cd in rep['cards']] == [1, 2, 3])
check('the message holds the forward book and the six ratings', all(k in msg for k in (
    'Форвард с 28.10', 'Оценка доверия', 'Надёжность системы: <b>1/5</b>', 'Уверенность в сделках:',
    'STRONG обоснован: <b>нет</b>', 'Качество данных: <b>низкое</b>', 'Ожидаемая R на сделку: <b>не установлена</b>',
    'Инвалидация: у каждой карточки')))
bk = rep['book']['base']
check('the book: opened is closed plus open, and the total is the sum of its two parts',
      bk['opened'] == bk['closed'] + bk['open'] and abs(bk['total_R'] - (bk['closed_R'] + bk['open_R'])) < 1e-9)
strong_card = dict(rep['cards'][0], strong=True)
plain_card = dict(rep['cards'][0], strong=False)
check('a STRONG card shows the STRONG shares 48 / 28 / 18%',
      [l.rsplit('дошли ', 1)[1] for l in a.card_lines(strong_card, a.FACTS) if 'дошли' in l] == ['48%', '28%', '18%'])
check('another card shows the rule\'s shares 23 / 13 / 8%',
      [l.rsplit('дошли ', 1)[1] for l in a.card_lines(plain_card, a.FACTS) if 'дошли' in l] == ['23%', '13%', '8%'])

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

```text file=research/tz36-advisor-trust.py
#!/usr/bin/env python3
# tz36-advisor-trust.py - TZ-36's checker: the fingerprint, the host gate, the number, G-RULE, COPY, G-RENDER, the
# readings after the unit's restart, and the marks. Standard library only. It starts and stops no unit, signals no
# process and sends no request of its own (G-RENDER runs the service copy's adv3.py, which reads Binance's public
# market), and it never reads or prints the bot's token or the pinned chat. Exits: 0 every assert held; 1 a failed
# assert, named; 3 NOT YET.
import ast, calendar, datetime as dt, hashlib, json, os, re, shutil, subprocess, sys, time

WORK = '/root/tz36-work'
WT = WORK + '/wt'
STATE = WORK + '/state.json'
PRIMARY = '/root/btc-5m-twap'
FORENSICS = '/root/btc-forensics'
SVC = '/root/adv3-bot-svc'
BOTDIR = '/var/lib/adv3-bot'
PY = '/root/tz04a-env/venv/bin/python'
ARGV = [PY, '-B', '-u', SVC + '/adv3-bot.py', '--serve']
BOT = 'adv3-bot.service'
CAPTURES = ('btc-recorder.service', 'btc-pairbook.service', 'btc-rewardbook.service')
TZ_FILE = 'CryptoTZ/TZ-36-advisor-trust-block.md'
NUMBER = 'TZ-36-'
MAP_REV = '2026-10-29-b'
ANCHORS = {'A1': '229a944f2d51', 'A2': '6c5089330629',
           'A3': '0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable',
           'A4': '437b45ea196b', 'A5': '0f6c90451cbd', 'A6': '729f0bcdbee3'}
DERIVED = {'A2': 'research/twap-divergence.py', 'A4': 'BTC-EXECUTOR-INSTRUCTIONS.md',
           'A5': 'research/recorder/recorder.py', 'A6': 'research/pfair.py'}
H = {'adv3_old': '7f2863a5b433ed7008c8f44af4f9c59d724d0c016c2c317f451158899c4f9adb',
     'adv3_new': 'd73a657ef31decad276b858c4ec9672dce1c1c5cec36f0bb1c5b3378838224a8',
     'bot': 'e65de91c7b49c6f932db91e568a5956c005e63119c1cf6fb8724ffb0438d1dcb',
     'rule': 'ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169',
     'unit': '82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66'}
RULE_FUNCS = ('signs', 'signal', 'strength', 'true_range', 'unit', 'open_at', 'hold', 'close_at', 'simulate', 'states',
              'ranking', 'simulate_strong', 'stats', 'funding_of')
CHANGED = {'card', 'card_lines', 'facts_checks', 'history', 'message', 'report'}
ADDED = {'book_line', 'forward_book', 'signed', 'trust', 'trust_lines'}
MEM_FLOOR, DISK_FLOOR = 170_344_448, 7_400_000_000
ROWS, FROZEN = 55, 52
MARKERS = ('Оценка доверия', 'Надёжность системы: <b>1/5</b>', 'Уверенность в сделках:', 'STRONG обоснован: <b>нет</b>',
           'Качество данных: <b>низкое</b>', 'Ожидаемая R на сделку: <b>не установлена</b>',
           'Инвалидация: у каждой карточки', 'Форвард с 28.10', 'Все сигналы: входов', 'STRONG: входов')
CARD = re.compile(r'^[🟢🔴] <b>[A-Z0-9]+ · (LONG|SHORT)</b>', re.M)


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
    stat = read('/proc/%s/stat' % pid)
    fields = stat[stat.rindex(')') + 2:].split()
    ticks = int(fields[19])
    btime = next(int(line.split()[1]) for line in read('/proc/stat').splitlines() if line.startswith('btime '))
    return btime + ticks / os.sysconf('SC_CLK_TCK')


# ---- pure readings: each takes what the modes read and returns its checks -----------------------------------

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
    """{name: ast.dump} of a module's functions, and of its assignments keyed by their targets."""
    fns, asg = {}, {}
    for n in ast.parse(src).body:
        if isinstance(n, ast.FunctionDef):
            fns[n.name] = ast.dump(n)
        elif isinstance(n, ast.Assign):
            asg[','.join(ast.unparse(t) for t in n.targets)] = ast.dump(n)
    return fns, asg


def rule_checks(old_src, new_src):
    """G-RULE's first five checks: the two adv3.py files differ in exactly the functions and constants TZ-36 names."""
    (of, oa), (nf, na) = top_level(old_src), top_level(new_src)
    return {
        'the functions that changed are exactly %s' % sorted(CHANGED):
            {k for k in of if k in nf and of[k] != nf[k]} == CHANGED,
        'the functions added are exactly %s' % sorted(ADDED): set(nf) - set(of) == ADDED,
        'no function removed': set(of) - set(nf) == set(),
        'the %d rule functions are identical by AST' % len(RULE_FUNCS):
            all(k in of and k in nf and of[k] == nf[k] for k in RULE_FUNCS),
        'the constants: FACTS changed, RELIABILITY and STRONG_JUSTIFIED added, nothing else':
            {k for k in oa if k in na and oa[k] != na[k]} == {'FACTS'} and set(oa) - set(na) == set()
            and set(na) - set(oa) == {'(RELIABILITY, STRONG_JUSTIFIED)'},
    }


def render_checks(msg, rc, err, rep, rc_json, err_json, close_day):
    """G-RENDER: the live message and the live report of the service copy; counts and labels only."""
    n = len(CARD.findall(msg))
    checks = {
        'the message run exits 0 with no traceback': rc == 0 and 'Traceback' not in err and msg.strip() != '',
        'the message holds the forward book, the six ratings and their lines': all(k in msg for k in MARKERS),
        'every card (%d) holds its basis and its invalidation' % n:
            msg.count('Основание: сумма знаков') == n and msg.count('Инвалидация: цена') == n and n <= 3,
        'the message fits three Telegram parts': len(msg) < 12000,
        'the report run exits 0 with no traceback': rc_json == 0 and 'Traceback' not in err_json and rep is not None,
    }
    if rep is None:
        return checks
    book, tr = rep.get('book', {}), rep.get('trust', {})
    checks.update({
        'the report is the frozen rule\'s, of 42 coins': rep.get('rule') == H['rule'] and len(rep.get('rows', {})) == 42,
        'the ratings: system 1, STRONG not justified, the data fresh, a trade 0 or 1, one for each card':
            tr.get('system') == 1 and tr.get('strong_justified') is False and tr.get('fresh') is True
            and set(tr.get('cards', {})) == set(rep['top'])
            and set(tr.get('cards', {}).values()) <= {0, 1},
        'the books: opened is closed plus open, the total is the two parts\' sum': all(
            b['opened'] == b['closed'] + b['open'] and abs(b['total_R'] - (b['closed_R'] + b['open_R'])) < 1e-9
            for b in book.values()) and set(book) == {'base', 'strong'},
        'the forward days are the closes from 2026-10-28 to the report\'s': all(
            b['days'] == close_day for b in book.values()),
        'each card carries a rank 1 to 3 and a sum of signs of 2 to 4 in size': all(
            cd.get('rank') in (1, 2, 3) and cd.get('sum') is not None and 2 <= abs(cd['sum']) <= 4 for cd in rep['cards']),
    })
    return checks


def unit_checks(which, pre, now):
    """The readings after a restart: now is what the modes read; pre is the snapshot of the mark before the kill."""
    want_sha = H['adv3_new'] if which == 'new' else H['adv3_old']
    return {
        'the unit is active, running and enabled': (now['bot']['ActiveState'], now['bot']['SubState'],
                                                    now['bot']['UnitFileState']) == ('active', 'running', 'enabled'),
        'a new MainPID, one restart more': int(now['bot']['MainPID']) not in (0, int(pre['bot']['MainPID']))
        and int(now['bot']['NRestarts']) == int(pre['bot']['NRestarts']) + 1,
        'the process started after the kill mark and within 90 s of it': pre['t'] <= now['start'] <= pre['t'] + 90,
        'the process runs the unit\'s exact argv, alone': now['argv'] == ARGV and now['procs'] == [int(now['bot']['MainPID'])],
        'the service copy is %s\'s adv3.py, the process started after the copy' % which:
            now['sha_adv3'] == want_sha and now['start'] > now['copy_t'],
        'the service copy\'s bot and the unit file are unchanged': now['sha_bot'] == H['bot'] and now['sha_unit'] == H['unit'],
        'the day\'s message was not sent again: daily-sent and the journal\'s daily records as before': (
            now['daily'] == pre['daily'] and now['journal'] == pre['journal']),
        'the log shows the new process serving and no daily sent, no traceback, since the mark': (
            now['serving'] and not now['daily_line'] and not now['traceback']),
        'the three capture units unchanged, each active': all(
            now['caps'][u]['ActiveState'] == 'active' and now['caps'][u]['MainPID'] == pre['caps'][u]['MainPID']
            and now['caps'][u]['NRestarts'] == pre['caps'][u]['NRestarts'] for u in CAPTURES),
    }


def log_since(text, t0, pid):
    """From service.log: whether the process pid logged 'serving', whether a daily was sent, whether a traceback
    appeared, in the lines stamped at or after t0 (epoch seconds)."""
    serving = daily = tb = since_ok = False
    for line in text.splitlines():
        m = re.match(r'^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})Z (.*)$', line)
        if not m:
            tb = tb or ('Traceback' in line and since_ok)
            continue
        stamp = calendar.timegm(time.strptime(m.group(1), '%Y-%m-%dT%H:%M:%S'))
        since_ok = stamp >= t0 - 1
        if since_ok:
            serving = serving or m.group(2).startswith('serving the pinned chat: pid %d ' % pid)
            daily = daily or m.group(2).startswith('daily sent')
            tb = tb or 'Traceback' in m.group(2)
    return serving, daily, tb


# ---- the modes -------------------------------------------------------------------------------------------------

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
        if path == 'SYSTEM-MAP.md':
            b = read(PRIMARY + '/' + path, 'rb')
            out('reported %d lines %d bytes %s %s' % (b.count(b'\n'), len(b), sha256_bytes(b), path))
            continue
        b = read(PRIMARY + '/' + path, 'rb')
        got = (b.count(b'\n'), len(b), sha256_bytes(b))
        out('%-8s %d lines %d bytes %s %s' % (state, got[0], got[1], got[2], path))
        if state == 'frozen':
            checks['frozen ' + path] = got == (lines, nbytes, sha)
    checks['the table holds %d rows, %d frozen, 2 tracked, 1 reported' % (ROWS, FROZEN)] = (
        len(rows) == ROWS and states == {'frozen': FROZEN, 'tracked': 2, 'reported': 1})
    verdict('FINGERPRINT', checks)


def mode_host():
    checks = {}
    rc, so, _ = sh(['find', '/var/lib/btc-recorder', '-mindepth', '1', '-maxdepth', '3', '-name', 'manifest.json',
                    '-print', '-quit'])
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
    checks['H5 the bot is active, running and enabled'] = (b['ActiveState'], b['SubState'], b['UnitFileState']) == (
        'active', 'running', 'enabled')
    checks['H5 the bot\'s MainPID runs the unit\'s argv, alone'] = (
        int(b['MainPID']) > 0 and proc_argv(b['MainPID']) == ARGV and procs(ARGV) == [int(b['MainPID'])])
    checks['H5 the service copy holds adv3.py, adv3-bot.py and commit.txt only'] = (
        sorted(os.listdir(SVC)) == ['adv3-bot.py', 'adv3.py', 'commit.txt'])
    checks['H5 adv3.py is TZ-35\'s and adv3-bot.py is TZ-35\'s'] = (
        sha256_file(SVC + '/adv3.py') == H['adv3_old'] and sha256_file(SVC + '/adv3-bot.py') == H['bot'])
    checks['H5 the installed unit file is TZ-35\'s'] = sha256_file('/etc/systemd/system/adv3-bot.service') == H['unit']
    checks['H5 commit.txt is 40 hex characters and a newline'] = re.fullmatch(r'[0-9a-f]{40}\n', read(SVC + '/commit.txt')) is not None
    checks['H6 the record holds daily-sent and a journal of whole lines'] = (
        re.fullmatch(r'\d{4}-\d{2}-\d{2}\n?', read(BOTDIR + '/daily-sent')) is not None
        and read(BOTDIR + '/journal.jsonl', 'rb').endswith(b'\n'))
    mem = {k: int(v.split()[0]) for k, v in (l.split(':', 1) for l in read('/proc/meminfo').splitlines())}
    checks['memory gate: MemAvailable at least %d bytes' % MEM_FLOOR] = mem['MemAvailable'] * 1024 >= MEM_FLOOR
    checks['disk gate: /dev/vda2 free at least %d bytes' % DISK_FLOOR] = int(avail) >= DISK_FLOOR
    out('units:', json.dumps(units, sort_keys=True))
    out('MemAvailable %d bytes, /dev/vda2 free %s bytes' % (mem['MemAvailable'] * 1024, avail))
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


def git_show(path):
    rc, so, se = sh(['git', '-C', PRIMARY, 'show', 'origin/main:' + path])
    assert rc == 0, se
    return so


def mode_rule():
    checks = rule_checks(git_show('advisor/adv3.py'), read(WT + '/advisor/adv3.py'))
    checks['adv3-bot.py is main\'s, byte for byte'] = read(WT + '/advisor/adv3-bot.py', 'rb') == git_show('advisor/adv3-bot.py').encode()
    rule_txt = read(WT + '/advisor/RULE-ADV-3.txt', 'rb')
    checks['RULE-ADV-3.txt is main\'s and hashes to the RULE constant'] = (
        rule_txt == git_show('advisor/RULE-ADV-3.txt').encode() and sha256_bytes(rule_txt) == H['rule']
        and ("RULE = '%s'" % H['rule']) in read(WT + '/advisor/adv3.py'))
    verdict('RULE', checks)


def daily_records(text):
    """How many records of kind 'daily' a journal.jsonl text holds: the Boss's own requests add records of another
    kind, and a restart must add none of the first."""
    n = 0
    for line in text.splitlines():
        try:
            n += json.loads(line).get('kind') == 'daily'
        except ValueError:
            pass
    return n


def snapshot():
    """What a mark records: the instant, the bot's and the captures' units, the record's two figures."""
    st = {'t': time.time(), 'bot': show(BOT, 'MainPID', 'NRestarts', 'ActiveState'),
          'caps': {u: show(u, 'MainPID', 'NRestarts', 'ActiveState') for u in CAPTURES},
          'daily': read(BOTDIR + '/daily-sent').strip(), 'journal': daily_records(read(BOTDIR + '/journal.jsonl'))}
    return st


def mode_mark(name):
    assert name in ('deploy', 'kill', 'rollback', 'kill2'), name
    st = load_state()
    snap = snapshot()
    if name in ('kill', 'kill2'):
        today = time.strftime('%Y-%m-%d', time.gmtime())
        assert snap['daily'] == today, 'the day\'s message is not sent: daily-sent %s, today %s' % (snap['daily'], today)
    st.setdefault('marks', {})[name] = snap
    save_state(st)
    out('mark %s at %s: bot pid %s NRestarts %s, daily-sent %s, %d daily records' % (
        name, time.strftime('%FT%TZ', time.gmtime(snap['t'])), snap['bot']['MainPID'], snap['bot']['NRestarts'],
        snap['daily'], snap['journal']))


def mode_copy():
    rc, head, _ = sh(['git', '-C', WT, 'rev-parse', 'HEAD'])
    rc2, up, _ = sh(['git', '-C', WT, 'rev-parse', 'origin/tz-36-advisor-trust-block'])
    commit = read(SVC + '/commit.txt')
    verdict('COPY', {
        'the service copy holds adv3.py, adv3-bot.py and commit.txt only': sorted(os.listdir(SVC)) == ['adv3-bot.py', 'adv3.py', 'commit.txt'],
        'adv3.py is Appendix A\'s': sha256_file(SVC + '/adv3.py') == H['adv3_new'],
        'adv3-bot.py is unchanged': sha256_file(SVC + '/adv3-bot.py') == H['bot'],
        'commit.txt is the branch head and the worktree\'s HEAD': (
            re.fullmatch(r'[0-9a-f]{40}\n', commit) is not None and rc == 0 and rc2 == 0 and commit.strip() == head.strip() == up.strip()),
        'the branch\'s adv3.py equals the service copy\'s': read(WT + '/advisor/adv3.py', 'rb') == read(SVC + '/adv3.py', 'rb'),
    })


def mode_render():
    cmd = ['nice', '-n', '19', PY, '-B', SVC + '/adv3.py']
    p1 = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    p2 = subprocess.run(cmd + ['--json'], capture_output=True, text=True, timeout=600)
    try:
        rep = json.loads(p2.stdout)
    except ValueError:
        rep = None
    close_day = None
    if rep is not None:
        close_day = (dt.date.fromisoformat(rep['close_of']) - dt.date(2026, 10, 28)).days + 1
    out('message: %d characters, %d lines; report: %d bytes' % (len(p1.stdout), p1.stdout.count('\n'), len(p2.stdout)))
    verdict('RENDER', render_checks(p1.stdout, p1.returncode, p1.stderr, rep, p2.returncode, p2.stderr, close_day))


def mode_unit(which):
    assert which in ('new', 'old'), which
    st = load_state()
    mark = 'kill' if which == 'new' else 'kill2'
    pre = st['marks'][mark]
    copy_t = st['marks']['deploy' if which == 'new' else 'rollback']['t']
    bot = show(BOT, 'MainPID', 'NRestarts', 'ActiveState', 'SubState', 'UnitFileState')
    pid = int(bot['MainPID'])
    if pid in (0, int(pre['bot']['MainPID'])) or bot['ActiveState'] != 'active':
        if time.time() - pre['t'] < 100:
            raise NotYet()
    caps = {u: show(u, 'MainPID', 'NRestarts', 'ActiveState') for u in CAPTURES}
    start = proc_start(pid) if pid else 0.0
    serving, daily_line, tb = log_since(read(BOTDIR + '/service.log'), pre['t'], pid)
    now = {'bot': bot, 'caps': caps, 'start': start, 'copy_t': copy_t, 'argv': proc_argv(pid) if pid else None,
           'procs': procs(ARGV), 'sha_adv3': sha256_file(SVC + '/adv3.py'), 'sha_bot': sha256_file(SVC + '/adv3-bot.py'),
           'sha_unit': sha256_file('/etc/systemd/system/adv3-bot.service'),
           'daily': read(BOTDIR + '/daily-sent').strip(), 'journal': daily_records(read(BOTDIR + '/journal.jsonl')),
           'serving': serving, 'daily_line': daily_line, 'traceback': tb}
    checks = unit_checks(which, pre, now)
    if which == 'old':
        checks['two restarts more than before the first kill'] = int(bot['NRestarts']) == int(st['marks']['kill']['bot']['NRestarts']) + 2
    out('bot: pid %d NRestarts %s started %s; captures: %s' % (pid, bot['NRestarts'], time.strftime('%FT%TZ', time.gmtime(start)),
        json.dumps({u: [c['MainPID'], c['NRestarts']] for u, c in caps.items()}, sort_keys=True)))
    verdict('UNIT-' + which.upper(), checks)


def kept_files():
    """The work tree's files a report keeps by name: state.json, history.json, the two files B-DEPLOY saves, and every
    file under logs/; relative to WORK, sorted."""
    names = ['state.json', 'history.json', 'adv3.before', 'commit.before']
    for d, _s, fs in os.walk(WORK + '/logs'):
        names += [os.path.relpath(os.path.join(d, f), WORK) for f in fs]
    return sorted(n for n in names if os.path.isfile(os.path.join(WORK, n)))


def mode_keep():
    """B-RECLAIM-OWN's copy: every kept file into the forensic store as tz36-work--<path with - for />, by exclusive
    create and verified whole; the branch worktree must hold nothing but its pushed HEAD."""
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
        dest = FORENSICS + '/tz36-work--' + rel.replace('/', '--')
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
    verdict('STOPPED', {'the unit is inactive or failed, and disabled': bot['ActiveState'] in ('inactive', 'failed')
                        and bot['UnitFileState'] == 'disabled', 'no process runs under the unit\'s argv': procs(ARGV) == []})


# ---- the self-test: the pure readings on stand-ins, each with a negative control -----------------------------

def mode_selftest():
    done = []

    def ok(cond, name):
        done.append(name)
        assert cond, name

    mp = ('**Revision string:** `%s`\n\n| anchor | value |\n|---|---|\n| `A1` — observation set | `229a944f2d51` |\n'
          '| `A3` — phase | `x / y` |\n\n### Fingerprint table\n\n| path | lines | bytes | state | SHA-256 |\n|---|---|---|---|---|\n'
          '| `SYSTEM-MAP.md` | — | — | reported | self-reference |\n| `a/b.py` | 1,135 | 50,928 | frozen | `%s` |\n'
          '| `c.py` | 7 | 8 | tracked | `%s` |\n\n---\n\n## 1. Repository\n| `z.py` | 1 | 1 | frozen | `%s` |\n') % (
        MAP_REV, 'a' * 64, 'b' * 64, 'c' * 64)
    rev, anchors, rows = parse_map(mp)
    ok(rev == MAP_REV and anchors == {'A1': '229a944f2d51', 'A3': 'x / y'}, 'parse_map: the revision and the anchors')
    ok(rows == [('SYSTEM-MAP.md', None, None, 'reported', None), ('a/b.py', 1135, 50928, 'frozen', 'a' * 64),
                ('c.py', 7, 8, 'tracked', 'b' * 64)], 'parse_map: the table\'s rows, thousands separators read, the next section left out')
    old = 'RULE = 1\nFACTS = {1: 2}\ndef a():\n    return 1\ndef b():\n    return 2\n'
    new_ok = old.replace('{1: 2}', '{1: 2, 3: 4}').replace('return 2', 'return 3') + 'def c():\n    return 0\n'
    saved = (RULE_FUNCS, CHANGED, ADDED)
    globals().update(RULE_FUNCS=('a',), CHANGED={'b'}, ADDED={'c'})
    try:
        good = rule_checks(old, new_ok.replace('RULE = 1', 'RULE = 1\nRELIABILITY, STRONG_JUSTIFIED = 1, False'))
        ok(all(good.values()), 'rule_checks: exactly the named functions and constants differ')
        bad = rule_checks(old, new_ok.replace('return 1', 'return 9').replace('RULE = 1', 'RULE = 1\nRELIABILITY, STRONG_JUSTIFIED = 1, False'))
        ok(not all(bad.values()) and not bad[[k for k in bad if 'identical by AST' in k][0]], 'rule_checks: a changed rule function reads FAIL')
        bad2 = rule_checks(old, new_ok)
        ok(not all(bad2.values()), 'rule_checks: constants not added read FAIL')
    finally:
        globals().update(RULE_FUNCS=saved[0], CHANGED=saved[1], ADDED=saved[2])
    msg = '\n'.join(MARKERS + ('🟢 <b>XMR · LONG</b>', 'Основание: сумма знаков +4', 'Инвалидация: цена ≤ 1'))
    book = {'opened': 5, 'closed': 2, 'open': 3, 'closed_R': -1.5, 'open_R': 0.5, 'total_R': -1.0, 'days': 4}
    rep = {'rule': H['rule'], 'rows': {str(i): 0 for i in range(42)}, 'top': ['XMR'],
           'trust': {'system': 1, 'strong_justified': False, 'fresh': True, 'cards': {'XMR': 1}},
           'book': {'base': dict(book), 'strong': dict(book)}, 'cards': [{'rank': 1, 'sum': 4}]}
    ok(all(render_checks(msg, 0, '', rep, 0, '', 4).values()), 'render_checks: a whole message and report read PASS')
    ok(not render_checks(msg.replace('Оценка доверия', ''), 0, '', rep, 0, '', 4)['the message holds the forward book, the six ratings and their lines'],
       'render_checks: a missing rating block reads FAIL')
    ok(not all(render_checks(msg + '\n🔴 <b>BTC · SHORT</b>', 0, '', rep, 0, '', 4).values()), 'render_checks: a card without its basis reads FAIL')
    broken = dict(rep, book={'base': dict(book, total_R=-2.0), 'strong': dict(book)})
    ok(not all(render_checks(msg, 0, '', broken, 0, '', 4).values()), 'render_checks: a book whose total is not its parts\' sum reads FAIL')
    ok(not all(render_checks(msg, 0, '', rep, 0, '', 5).values()), 'render_checks: forward days not equal to the closes since 2026-10-28 read FAIL')
    pre = {'t': 1000.0, 'bot': {'MainPID': '10', 'NRestarts': '1'}, 'daily': '2026-10-31', 'journal': 7,
           'caps': {u: {'MainPID': str(i), 'NRestarts': '0', 'ActiveState': 'active'} for i, u in enumerate(CAPTURES, 20)}}
    now = {'bot': {'MainPID': '11', 'NRestarts': '2', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'enabled'},
           'caps': dict(pre['caps']), 'start': 1035.0, 'copy_t': 990.0, 'argv': ARGV, 'procs': [11], 'sha_adv3': H['adv3_new'],
           'sha_bot': H['bot'], 'sha_unit': H['unit'], 'daily': '2026-10-31', 'journal': 7, 'serving': True, 'daily_line': False,
           'traceback': False}
    ok(all(unit_checks('new', pre, now).values()) and len(unit_checks('new', pre, now)) == 9, 'unit_checks: a clean restart reads 9 of 9')
    for key, val, label in (('daily', '2026-11-01', 'a daily-sent changed'), ('journal', 8, 'a message sent again'),
                            ('start', 1200.0, 'a process started 200 s after the kill'), ('sha_adv3', H['adv3_old'], 'the old adv3.py'),
                            ('daily_line', True, 'a daily line since the mark'), ('procs', [11, 12], 'a second process under the argv')):
        ok(not all(unit_checks('new', pre, dict(now, **{key: val})).values()), 'unit_checks: %s reads FAIL' % label)
    moved = {u: dict(c, NRestarts='1') for u, c in pre['caps'].items()}
    ok(not all(unit_checks('new', pre, dict(now, caps=moved)).values()), 'unit_checks: a capture unit restarted reads FAIL')
    ok(all(unit_checks('old', pre, dict(now, sha_adv3=H['adv3_old'])).values()), 'unit_checks: the rollback reads the old adv3.py')
    log = ('2026-10-31T06:00:01Z daily sent for the close of 2026-10-30\n2026-10-31T09:00:00Z serving the pinned chat: pid 11 offset 5 daily-sent 2026-10-31\n'
           'Traceback (most recent call last):\n')
    t = calendar.timegm(time.strptime('2026-10-31T08:59:59', '%Y-%m-%dT%H:%M:%S'))
    jl = '{"kind": "daily", "x": 1}\n{"kind": "request"}\nnot json\n{"kind": "daily"}\n'
    ok(daily_records(jl) == 2 and daily_records('') == 0, 'daily_records: the daily kind counted, requests and a broken line left out')
    ok(log_since(log, t, 11) == (True, False, True), 'log_since: serving found, the earlier daily left out, a later traceback found')
    ok(log_since(log, t, 12) == (False, False, True), 'log_since: another pid does not serve')
    ok(all(number_reading(['CryptoTZ/' + 'TZ-36-advisor-trust-block.md', 'CryptoTZ/TZ-35-x.md']).values()), 'number: the one file reads PASS')
    ok(not all(number_reading(['CryptoTZ/TZ-36-advisor-trust-block.md', 'CryptoTZ/TZ-36-other.md']).values()), 'number: two files of the number read FAIL')
    ok(not all(number_reading(['CryptoTZ/TZ-36-advisor-trust-block.md', 'CryptoReports/TZ-36-x-report.md']).values()), 'number: a report of the number reads FAIL')
    import tempfile
    saved_work = WORK
    with tempfile.TemporaryDirectory() as tmp:
        os.makedirs(tmp + '/logs/sub')
        for rel in ('state.json', 'history.json', 'adv3.before', 'logs/01-a.log', 'logs/sub/02-b.log', 'wt-not-kept.txt', 'stage-not-kept.txt'):
            with open(tmp + '/' + rel, 'w') as fh:
                fh.write(rel)
        globals().update(WORK=tmp)
        try:
            kept = kept_files()
        finally:
            globals().update(WORK=saved_work)
    ok(kept == ['adv3.before', 'history.json', 'logs/01-a.log', 'logs/sub/02-b.log', 'state.json'],
       'kept_files: the named files and the logs, nothing else, commit.before absent where not written')
    out('SELFTEST PASS: %d of %d checks passed' % (len(done), len(done)))


def main(argv):
    if not argv:
        sys.exit('usage: tz36-advisor-trust.py MODE [ARG]')
    mode, rest = argv[0], argv[1:]
    table = {'fingerprint': mode_fingerprint, 'host': mode_host, 'number': mode_number, 'rule': mode_rule,
             'copy': mode_copy, 'render': mode_render, 'keep': mode_keep, 'stopped': mode_stopped,
             'selftest': mode_selftest}
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

