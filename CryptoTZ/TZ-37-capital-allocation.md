# TZ-37 — trigger commands and capital allocation: «сигнал 10000 топ 3» divides a budget among the STRONG trades that qualify, within the risk limits

**Canonical filename:** `TZ-37-capital-allocation.md`. The committed file takes this name and no other.

**Executor model: Claude Opus 5.5.** It changes the bot's routing, a new allocation view and its reply in `advisor/adv3-bot.py`, and signals a
long-lived unit on the capture host.

**Required System Map revision:** `2026-10-31-a`.

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

**Before `EXECUTE TZ-37`:** the Boss uploads, in the one upload that carries this TZ, `SYSTEM-MAP.md` at revision `2026-10-31-a`, which
`main` does not yet hold (it holds `2026-10-29-b`; PR #36 is merged). The bot's token and its pinned chat exist (map §2.7); this TZ's own commands read
neither, and the bot's `--probe`, which reads the token to send `getMe`, prints neither (§2, item 3).

**When:** any time after the upload that carries this TZ, while `/dev/vda2` holds at least `7,400,000,000` bytes free (§0.4). **§3.4 waits
for 06:35:00 to 23:45:00 UTC before the service copy is replaced, and §3.5 for 06:35:00 to 23:50:00 before the unit is signalled**, clear of the
package manager's morning runs and of both archives' calendar runs, the reward book's at 01:30:20 and the pair book's at 03:00:20 (map §2.5 and §2.6; §7
item 129). This TZ reloads systemd **never**, so it sets off no run of either archive (map §7 items 125 and 129). About 40 minutes of wall
clock (§6).

**What this TZ is.** On 2026-10-31 the Boss wrote this TZ's requirement himself, as «TЗ-37 — Trigger Commands and Intelligent Capital Allocation»: the bot is to
understand «сигнал» (the strongest valid setups, no budget), «сигнал 10000 топ 3» (a budget of 10,000 USDT across up to the 3 strongest qualifying trades)
and «сигнал 15000 топ 5», and equivalent forms; to select only trades that meet the STRONG criteria and return fewer when fewer qualify, never padding; to divide the
budget by trade quality, confidence, risk/reward, liquidity, volatility and correlation, "The specified budget represents the total capital intended for deployment across selected trades, not merely the
account balance used to calculate a fixed percentage risk"; to reject any setup whose stop lies farther than **11.1 %** of the entry; to compute size, leverage, margin
and the loss at the stop for every trade, **never letting the allocation override the risk limits**; and to show the budget and what is allocated, the count and ranking, coin,
direction and quality, entry, stop and targets, the capital, leverage, margin and loss for each trade, and the balance left unallocated. His instruction: "Implement this within the existing architecture
without unnecessary redesign or unrelated work." **This TZ does that and nothing else:** `route` reads the budget and the number of trades; `plan` selects, weighs and sizes (§4.2);
`plan_parts` writes the reply (§4.2); `handle` answers and journals. It replaces `advisor/adv3-bot.py` and adds this TZ's checker `research/tz37-capital-allocation.py`;
**it leaves `adv3.py`, `selftest-adv3.py`, `RULE-ADV-3.txt`, the unit, the daily message and plain «сигнал» untouched**, and proves it by file and by syntax tree (G-RULE). It deploys
by replacing the service copy's `adv3-bot.py` and signalling the unit once. **What the Boss's earlier messages of the day asked beyond this — a table of all 42 coins, the card of any one
coin, Telegram's command menu, a bound on `service.log`, a census of the host's memory and disk — is a TZ of its own, after this one.**

---

## 0. Gates

### 0.0 The work tree, first

After contract §1 steps 1 and 2, and before anything else:

```
mkdir /root/tz37-work /root/tz37-work/logs; echo "exit=$?"
```

`exit=0` proves neither existed; anything else is BLOCKED. **From here every command's output goes to
`/root/tz37-work/logs/`, one file per step, `NN-<step>.log` in this TZ's order**, and nothing to the session's
scratchpad. The one exception is B-RECLAIM-OWN, §9, which removes the directory the logs are in.

Two abbreviations: **`P`** is `nice -n 19 /root/tz04a-env/venv/bin/python -B`, and **`I`** is `P
/root/tz37-work/stage/research/tz37-capital-allocation.py`. **In every block that signals the unit, restores a file or removes a tree, `I` is
written out in full**, because the Boss may be handed the block (map §6, sandbox limit).

### 0.1 The files, staged

Extract Appendix A from this TZ as the primary checkout carries it after contract §1's pull, with this script,
verbatim, its one argument the destination:

```
/root/tz04a-env/venv/bin/python -B - /root/tz37-work/stage <<'EOF'
import hashlib, os, sys
SRC = "/root/btc-5m-twap/CryptoTZ/TZ-37-capital-allocation.md"
DEST = sys.argv[1]
WANT = {
    "advisor/adv3-bot.py": "3a044d50f51b16563b99bf1514ef92f35a9795b1fcc377aea6be4c23a31f7af2",
    "research/tz37-capital-allocation.py": "eec1f30b971ed1d6db31e27eb0c321276c1b107a1654e013996d023b1a6a04eb",
}
OLD = {  # the committed file an extraction over a worktree replaces: TZ-35's bot, by hash
    "advisor/adv3-bot.py": "e65de91c7b49c6f932db91e568a5956c005e63119c1cf6fb8724ffb0438d1dcb",
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
| `advisor/adv3-bot.py` | 798 | 49,783 | `3a044d50f51b16563b99bf1514ef92f35a9795b1fcc377aea6be4c23a31f7af2` |
| `research/tz37-capital-allocation.py` | 808 | 51,269 | `eec1f30b971ed1d6db31e27eb0c321276c1b107a1654e013996d023b1a6a04eb` |

A failed assert is BLOCKED. Over an empty `stage/` the script creates two files (`xb`); over the branch's worktree,
§3.1, it overwrites the committed bot and only after asserting it is TZ-35's by hash, and creates the checker.

### 0.2 Fingerprint

`I fingerprint` performs contract §1 steps 3 and 4 against `SYSTEM-MAP.md` and the files of its §0 table in the primary
checkout `/root/btc-5m-twap`, and asserts them: revision `2026-10-31-a`; the six anchors, `A2`, `A4`, `A5` and `A6`
re-derived as the first 12 hex characters of those files' SHA-256; the table's **56** rows, each printed in lines,
bytes and SHA-256 — **53** `frozen` rows asserted equal to the map, **2** `tracked` and **1** `reported`, the map's
own. It prints `READING FINGERPRINT: PASS - 65 of 65` — 1 revision, 6 anchors, 4 re-derived, 53 rows, 1 shape — or
fails at the first mismatch, which is BLOCKED. The advisor rows are `frozen` at TZ-36's and TZ-35's hashes and stay so until
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
  hash to TZ-36's and TZ-35's (`d73a657e…` and `e65de91c…`); the installed unit file hashes to `main`'s (`82acd8e4…`); `commit.txt`
  is 40 hex characters and a newline — six checks.
- **H6** — `/var/lib/adv3-bot/daily-sent` holds a date, and `journal.jsonl` ends in a newline.
- **Memory gate** — `MemAvailable` at least `130,981,888` bytes (§0.4); **where the first read is below it, `I host` reads again after 60 s and
  the second read decides**. **Disk gate** — `/dev/vda2` free at least `7,400,000,000` bytes (§0.4).

Any one failing is BLOCKED. **The rest is printed and carries no threshold:** the timers and the two archives' services;
the listing of the service copy and the record; `du` of the capture roots and the Claude directory; the forensic
store's count, map §3's `2,232`; the worktrees, map §3's two; and the listing of the directory that holds the
session's own scratch, whose UUID directories §3.3 names live or earlier. Map §3 records the two the previous session left,
`0bf93b31-e4ab-4a54-9db3-a06f592b7731` and `84903452-8bf4-53c5-8169-67946f6e03f0`, and one live `claude` session of 2026-10-30 that is no
TZ's, `238335b9-cf23-414a-8e8f-ad4705c4d19e`.

### 0.4 Resource floors, in exact bytes

**Disk.** `/dev/vda2` free at least **`7,400,000,000`** bytes: the reward book's `STREAM_FLOOR`, `7,300,000,000`, below
which no stream of it opens (map §2.6; `research/tz33-reward-book-capture.py` line 190), plus `100,000,000` for this
session at its upper bound — the worktree, about `10,300,000` bytes of tracked files, the logs under `2,000,000`,
the copies of the work tree's files under `5,000,000`. **This TZ never takes free space
below the floor that pauses the reward book.** TZ-36 read `11,058,540,544` bytes free at its host gate (map §6).

**Memory.** `MemAvailable` at least **`130,981,888`** bytes: twice `65,490,944`. Map §7 item 131's rule is that a floor derived from a
peak takes the larger of the Architect's measurement and the host's last measured peak of the same code. This TZ runs no `--history`: its largest
mode is `I render`, the bot's replies on live data in one process. The Architect measured it on 2026-10-31 under Python 3.13.18 on synthetic candles
of production size — 42 coins of 1,500 days — through four reports and the replies to five commands, the three allocations among them: `49,168,384` bytes, the largest of three runs; the host's last measurement of the nearest code,
TZ-36's `I render`, two live runs of `adv3.py` and its process tree, is `65,490,944` (map §6). The larger stands. **TZ-36's floor, `170,344,448`, was twice a peak of
`adv3.py --history`, a mode this TZ does not run; the host read `158,494,720` bytes at TZ-36's first printed read and `189,366,272` at the gate the
TZ asserted (map §7 item 137).** The decision, the Architect's: **a floor is twice the largest peak among the modes the TZ runs, and
it is asserted on `I host`'s read, a first read below it read again after 60 s** (§0.3). The service runs under its unit's `MemoryMax=128M`, which this TZ does not change.
Every mode of this TZ runs under `nice -n 19`.

### 0.5 Refs and the number

```
git -C /root/btc-5m-twap fetch origin
git -C /root/btc-5m-twap ls-remote origin
git -C /root/btc-5m-twap ls-remote --heads origin tz-37-capital-allocation | wc -l
I number
git -C /root/btc-5m-twap log --first-parent --name-status --format='%h %cI %s' -n 5 origin/main
```

Every ref line is reported. **`wc -l` must print `0`:** the branch does not exist. **`I number`** reads `git ls-tree
--name-only origin/main -- CryptoTZ/ CryptoReports/` and must print `READING NUMBER: PASS - 2 of 2`: `CryptoTZ/` holds
`TZ-37-capital-allocation.md` and no other file whose name begins with `TZ-37-`, and `CryptoReports/` no report whose
name does (CANON hard rule 2). Anything else is BLOCKED. A difference in the refs or the log from what map §1 records
is recorded, not blocking, unless `main` does not carry revision `2026-10-31-a`.

---

## 1. Why this TZ exists

**What the bot understood** (`advisor/adv3-bot.py` at `a5c66a1`): `CMD`, line 20, matched «сигнал» and `signal` and nothing else; `parse`, lines 110 to 120, read from the rest of
that text a deposit (the first number of 100 or more, default `10 000`) and a risk (the first below 100, default `0,5`, at least `0,05`, at most `1`); `handle`, lines 249 to 268, answered any other text with `HELP`.
**The measured consequence** — the Architect called `parse` of that file on the Boss's own examples, 2026-10-31: «сигнал 10000 топ 3» reads `(10000.0, 1.0)`, the `3` of «топ 3» taken for a risk of 3 % and capped to
the rule's 1 %; «сигнал 15000 топ 5» reads `(15000.0, 1.0)`; «сигнал топ 3» reads `(10000.0, 1.0)`; «топ 3 на 10000» reads `None`, which is the help. **So the bot that runs now answers the Boss's example with the day's three cards sized at
twice their default risk, 100 USDT a stop-out, and does not say that it misread «топ 3»** [measured]. `route` reads «топ N» out of the text before it reads the numbers (§4.2).

**A budget is not a deposit, and the limits do not move.** The Boss's text: the budget is "the total capital intended for deployment across selected trades, not merely the account balance used to calculate a fixed percentage risk"; and, in the same
text, "Capital allocation must never override risk limits or portfolio-level risk controls". The sizes are CANON PART VII's and `adv3.py`'s (`RISK`, `RISK_MAX`, `RISK_ALL` = `0,5`, `1` and `5` % — 0.5 % of the deposit a trade by default, 1 % at most, all open trades together at most 5 %): a trade's
size is what it may lose at its stop divided by the distance to that stop. At the median stop of the history's trades that pass the 11.1 % limit, 8.9 % of the entry, 0.5 % of 10 000 USDT is a position of about 550 USDT, 5.5 % of the budget; three of them about 1,650; at the cap of 1 % a trade about 1,100 each
and 3,300 of the 10 000 at most [modelled, arithmetic on `0.089 + 2 × 0.001`]. The Boss's own illustration of 4 000, 3 500 and 2 500 USDT would lose about 910 USDT at those stops, 9.1 % of the budget, against the 5 % in all.
**The two sentences cannot both hold for a full deployment, and the Architect decides [решение принято мной]: the limits win** — they are the Boss's, written in PART VII and again in his own sentence — so the allocation is the position the limits allow, and **what they do not allow is shown as the balance left free,
with the reason in the reply**, which is the Boss's own line "Any unallocated balance if the full budget cannot be deployed safely". Discarded: dividing the whole budget by weight, which risks about 9 % of it at the stops of the passers. Raising the limits is a change of PART VII and of `adv3.py`, the Boss's decision
about his own risk and a TZ of its own; this TZ touches neither. The reply states the limits in money for the budget given, so that what the Boss sees is what he can change.

**The selection.** "Select only trades meeting the STRONG quality criteria", "Return fewer trades if fewer qualify", "Never add weaker setups just to fill the requested number". STRONG is the rule's: a TOP-3 coin whose four signs agree and whose strength `|z|` is at least `1`
(`adv3.TOP_N`, `STRONG_Z`; `RULE-ADV-3.txt`). **At most three coins are STRONG on any day, so «топ 5» returns three at most, and the reply says so.** The 11.1 % limit is the card's own `stop_pct`, the distance from the entry the card computes to its stop, `U = 2N` from the close
(`adv3.card`, line 473); a STRONG coin beyond it is rejected and named with its distance, **the stop is never moved to fit** (the Boss: "reject the setup rather than forcing an unsuitable stop"), and a coin whose price stands within a quarter of `U` of its stop, or beyond it, has no entry (`NEAR_STOP`, `adv3.card`) and is named. The limit is read at the moment of the request, on the mark price.

**What the history says about the limit** [measured, in sample, not evidence — the Architect's re-derivation of Gate S, 2026-10-31, not committed]. The 253 STRONG trades had a median stop of 14.4 % of the entry, quartiles 10.3 % and 18.3 %; **74 of them, 29 %, lie within 11.1 %**, at a median of 8.9 %. Their mean was `+1.28` R against `+0.25` R for
the other 179 — but five trades make 108 % of the 74's total of `+94` R, the other 69 average `−0.11` R, and 27 of the 74 won. That is a selection made on a history, and no sign that the limit picks better trades. Of the rule's 5,265 trades 37 % pass, the median stop 12.6 %. **Expect most days to answer «подходящих сделок нет»**; a day that does not is
one to three trades and, at the limits above, a minority of the budget. The reply says why the balance is free, and the Boss is told what to expect.

**The weights.** The Boss lists trade quality, confidence, risk/reward, liquidity, volatility and correlation, with 4 000/3 500/2 500 as an illustration and "not fixed rules". What the rule gives: *quality* — `|z|` and the sum of signs; *confidence* — one reliability rating of the whole system, `adv3.RELIABILITY = 1` of 5, the same for every trade;
*risk/reward* — the stop at `1U` and the targets at `1U`, `2U` and `3U` from the close for every trade, with one set of measured shares reaching each, so the same for every trade to the entry's offset inside its zone; *volatility* — `U` itself, which enters through the stop's distance, a wider stop taking a smaller position for the same loss; *liquidity*
and *correlation* — read from Binance's public candles. **The two that do not differ between trades are not made weights**: a differentiator that no step has measured would show an unmeasured number as information, and CANON's first question is whether the number is real; they are shown as the rule's, in the six ratings. The weights are `min(|z|, 3)`, discounted for the mean same-way correlation with the others
(the last 56 daily log returns, at least 30 common days, an unknown correlation counted as 1); liquidity is a cap, 0.1 % of the coin's mean daily quote volume of its last 7 closed days; the rest is §4.2's arithmetic. **The formula is the Architect's, unproven, and the reply says so in a sentence the bot's self-test and G-RENDER read**: the forward record (PART VII) measures the rule, not this selection and not these sizes.
CANON PART V: a tool the Boss asks for, for trading he does anyway, is judged against his trading without it.

**What is unchanged.** «сигнал» with no number of 100 or more — the TOP-3 message of TZ-36, its cards at `10 000` USDT and `0,5 %`; the daily message at 06:00 UTC; the rule, `adv3.py`, the six ratings and the forward book. Binance's incident of 2026-10-29 (withdrawals suspended; the Architect verified it by search, 2026-10-31) is not a dependency: the bot reads
`fapi.binance.com` from the host, `daily-sent` read `2026-10-31` at TZ-36's marks, and a request that finds Binance silent is answered with the bot's apology, as before. This session's container is refused by `fapi.binance.com` with HTTP `451`; the host is not, and P-START and G-RENDER prove that, before anything is signalled.

**What this TZ does not do.** The Boss's earlier messages of the day asked for a table of all 42 coins, the card of any one coin, Telegram's command menu, a bound on `service.log` and a clean-up of what the architecture leaves on the host. They are not this requirement and not here: "without unnecessary redesign or unrelated work". The clean-up in particular
is a deletion rule, and a rule written before its numbers are read is the order CANON's mission forbids; it is a TZ of its own, built from a census of the host. This TZ leaves the host clean (§9) and deletes nothing but its own tree and the earlier session directories TZ-35's `reclaim` already handles. It adds no direction forecast, no market factor and no queue that waits for Binance.

---

## 2. Scope

**Paths this TZ writes.** On the branch `tz-37-capital-allocation`: `advisor/adv3-bot.py`, modified, and `research/tz37-capital-allocation.py`, new. On the host:
`/root/tz37-work/**`; `/root/adv3-bot-svc/adv3-bot.py` and `/root/adv3-bot-svc/commit.txt`; `/root/btc-forensics/tz37-work--*`. On `main`: the report,
`CryptoReports/TZ-37-capital-allocation-report.md`.

**Prohibited**, by path and by content class:

1. Any change to a repository file but the two above and the report — `advisor/adv3.py`, `advisor/selftest-adv3.py`, `advisor/RULE-ADV-3.txt`,
   `deploy/systemd/adv3-bot.service`, `SYSTEM-MAP.md` and `BTC-EXECUTOR-INSTRUCTIONS.md` among them.
2. Any change to a definition or a constant of `adv3-bot.py` but those §4.1 names, and any change to `adv3.py`: G-RULE reads both.
3. Any read, copy, print or hash of anything under `/etc/adv3-bot/`, and any request to Telegram or to Binance by this TZ's own commands, but two: G-RENDER runs the service copy's
   bot, whose `Data` and `liquidity` read Binance's public futures market, and P-START (§3.5) runs the bot's own `--probe`, whose function reads the token to send `getMe`. It prints the bot's username and neither the token nor a chat id.
   The unit makes its own requests.
4. Any `systemctl` verb but `show`, `list-timers`, `is-enabled`, `kill --signal=SIGTERM adv3-bot.service` (B-KILL, B-ROLLBACK) and, on
   a FAIL of UNIT-OLD, `disable --now adv3-bot.service` (K-37). No `daemon-reload`, `enable`, `restart`, `start`, `stop` or `mask`.
5. Any change to a capture unit, its store, either archive's timer or ledger: `systemctl show` and `list-timers`, `du`, and under the recorder's root `find`, `grep -c` and `df` read them.
6. A dataset or a binary in git history.
7. A price, a coin, a size or a card from the live replies printed in the report: G-RENDER prints counts and labels alone. Binance's prices are public market data and none is a capture's, but the
   day's cards are the Boss's to read in his chat, not the repository's.
8. The report on `main` before the branch is pushed and its pull request opened (contract §4.1).

**Exemptions.** The requests of item 3, each by the service copy's own code, as TZ-35's P-START and TZ-36's G-RENDER made theirs.

---

## 3. The work, in this order

### 3.1 The branch and its files

```
git -C /root/btc-5m-twap fetch origin
I number
git -C /root/btc-5m-twap worktree add -b tz-37-capital-allocation /root/tz37-work/wt origin/main
```

`I number` must print `READING NUMBER: PASS - 2 of 2` again, or BLOCKED. Then §0.1's script again, verbatim but for its
argument, `/root/tz37-work/wt`; it must print the same lines, bytes and SHA-256 as at §0.1. Then:

```
git -C /root/tz37-work/wt add advisor/adv3-bot.py research/tz37-capital-allocation.py
git -C /root/tz37-work/wt diff --cached --name-status
git -C /root/tz37-work/wt diff --cached --numstat
```

`--name-status` must print exactly two lines — `M` for the bot, `A` for the checker — and `--numstat`
exactly `405	29	advisor/adv3-bot.py` and `808	0	research/tz37-capital-allocation.py`, or BLOCKED.
Commit them alone; `git ls-remote origin` (§0.5); push with `git push -u origin tz-37-capital-allocation` — through
`credential.helper=!gh auth git-credential` where the URL's credential is refused (map §6, git remote) — and open the
pull request against `main`. A failed assert here is BLOCKED.

### 3.2 The self-tests and G-RULE

```
P /root/tz37-work/wt/advisor/selftest-adv3.py
P /root/tz37-work/wt/advisor/adv3-bot.py --selftest
I selftest
I rule
```

They must print `SELFTEST-ADV3 PASS: 44 of 44 checks passed`, `SELFTEST PASS: 67 of 67 checks passed`, `SELFTEST PASS: 50 of 50
checks passed` and `READING RULE: PASS - 7 of 7`. The first, second and third reach no network; `I rule` reads `git show
origin/main:advisor/adv3-bot.py` and the branch's files. A red check stops the run here, and it goes to §3.6 and §9.

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
name carries `btc-5m-twap`. Map §3 expects the two directories named in §0.3 unless a reboot emptied `/tmp`; the live session of 2026-10-30 is not touched. If `scratch`
names none earlier, the block is recorded as empty and skipped. **A refused `rm -rf` is handed to the Boss** as one exact
command a tree, and verified by `test -e` (map §6, sandbox limit).

### 3.4 B-DEPLOY, then COPY and G-RENDER

All of §3.1 to §3.3 PASS first. Then **B-DEPLOY**, which waits for its band and records its mark inside the block:

```
until s=$(( $(date +%s) % 86400 )); [ $s -ge 23700 ] && [ $s -le 85500 ]; do sleep 5; done; { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz37-work/stage/research/tz37-capital-allocation.py mark deploy && cp -p /root/adv3-bot-svc/adv3-bot.py /root/tz37-work/bot.before && cp -p /root/adv3-bot-svc/commit.txt /root/tz37-work/commit.before && git -C /root/tz37-work/wt show origin/tz-37-capital-allocation:advisor/adv3-bot.py > /root/adv3-bot-svc/adv3-bot.py.new && mv /root/adv3-bot-svc/adv3-bot.py.new /root/adv3-bot-svc/adv3-bot.py && git -C /root/tz37-work/wt rev-parse origin/tz-37-capital-allocation > /root/adv3-bot-svc/commit.txt; echo "exit=$?"; } >> /root/tz37-work/logs/NN-b-deploy.log 2>&1
```

06:35:00 to 23:45:00 UTC is seconds `23,700` to `85,500` of the day. `exit=0`, or B-ROLLBACK (§4.4). The
running process keeps the old code in memory until it is signalled. Then:

```
I copy
timeout 900 I render
```

`I copy` must print `READING COPY: PASS - 5 of 5`; `I render` imports the service copy's bot and runs its `handle` on six texts against `fapi.binance.com` — with a stand-in for Telegram, a scratch journal under
`/root/tz37-work/render-state/` and the bot's own record untouched — and must print `READING RENDER: PASS - 16 of 16`. A FAIL of either, or a `timeout`, is B-ROLLBACK (§4.4), and nothing
is signalled.

### 3.5 P-START, B-KILL, then UNIT-NEW

Only after COPY and G-RENDER PASS. **P-START**, CANON hard rule 14's proof of the request path, through the service copy's own functions:

```
P /root/adv3-bot-svc/adv3-bot.py --probe
```

It must print `READING P-START: served - 5 of 5 endpoints` (§4.3): one request to each of `fapi.binance.com`'s klines, funding rate, premium index
and funding info, and Telegram's `getMe`. A FAIL is B-ROLLBACK (§4.4), and nothing is signalled. Then **B-KILL**, its mark inside the block:

```
until s=$(( $(date +%s) % 86400 )); [ $s -ge 23700 ] && [ $s -le 85800 ]; do sleep 5; done; { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz37-work/stage/research/tz37-capital-allocation.py mark kill && systemctl kill --signal=SIGTERM adv3-bot.service; echo "exit=$?"; } >> /root/tz37-work/logs/NN-b-kill.log 2>&1
```

06:35:00 to 23:50:00 UTC keeps the restart inside the UTC day of the message it must not send again. `I mark kill` fails —
and nothing is signalled — where `daily-sent` is not today's UTC date. At least 45 s later, then every 15 s while it
prints `NOT YET` and exits `3`, and for at most 100 s after the mark: `I unit new` — **UNIT-NEW**, `READING UNIT-NEW: PASS - 9 of 9`.
`RestartSec=30` and the start put the new process 35 s after the signal in TZ-35's and TZ-36's runs. A FAIL is B-ROLLBACK (§4.4).

### 3.6 The closing reads

```
TZ=UTC systemctl show adv3-bot.service btc-recorder.service btc-pairbook.service btc-rewardbook.service btc-pairbook-archive.service btc-rewardbook-archive.service -p Id -p MainPID -p NRestarts -p ActiveState -p Result -p Nice -p MemoryCurrent -p MemoryPeak -p ActiveEnterTimestamp
TZ=UTC systemctl list-timers btc-pairbook-archive.timer btc-rewardbook-archive.timer --all --no-pager
systemctl is-enabled adv3-bot.service; echo "exit=$?"
journalctl -u adv3-bot.service --no-pager -o short-iso | tail -n 20
tail -n 30 /var/lib/adv3-bot/service.log
ls -la /var/lib/adv3-bot /root/adv3-bot-svc
free -b; df -B1 --output=source,size,avail /var/lib/btc-recorder
du -sb /root/tz37-work /root/adv3-bot-svc /var/lib/adv3-bot /var/lib/btc-rewardbook /var/lib/btc-pairbook /root/.claude
cat /root/tz37-work/state.json
```

The journal holds systemd's own lines for the unit; `service.log` the service's own, one line a start, a refresh, a message and a
failure, with no token and no chat id. The Boss's next «сигнал 10000 топ 3», or the 06:00 UTC message of the next day, is the first the running unit
answers with the new code; nothing in this TZ sends or fakes one to the Boss's chat.

---

## 4. The gates — fixed here, before any of their data exists

| gate | population | PASS | false failure | power, against |
|---|---|---|---|---|
| **G-RULE** | `origin/main`'s `adv3-bot.py` and the branch's; their `adv3.py`, `selftest-adv3.py`, `RULE-ADV-3.txt` and the unit file | 7 of 7 (§4.1) | `0` — the files and syntax trees read directly | `1`, a rule function, a constant, the unit or the rule text changed, or a bot definition changed beyond Appendix A |
| **SELFTESTS** | the three self-tests | 44 of 44, 67 of 67 and 50 of 50 | `0` | `1`, a changed expectation or a red check |
| **COPY** | the service copy | 5 of 5 (§4.3) | `0` | `1`, a file not Appendix A's or not the branch head's |
| **G-RENDER** | the service copy's bot answering six texts on live data | 16 of 16 (§4.3) | `0` — the replies compared with the plan the checker recomputes from the same report and with fixed labels and limits | `1`, a command that does not answer, a trade beyond 11.1 %, a loss beyond 1 % or 5 % of the budget, a coin added to fill a place, a reply that is not the bot's own plan |
| **P-START** | five endpoints, one request each, through the service copy's own functions | `READING P-START: served - 5 of 5 endpoints` | `0` — each read directly | `1`, a refused request — `451`, `403` — or a reply of another shape |
| **UNIT-NEW** | the unit after the signal | 9 of 9 (§4.3) | `0` | `1`, a process not new, not the new code's, a daily sent again, a capture unit moved |

**Family-wise false failure `0`:** every gate reads its quantity directly and none samples. A FAIL before B-DEPLOY is BLOCKED and
deploys nothing; a FAIL of COPY, G-RENDER, P-START or UNIT-NEW is B-ROLLBACK (§4.4).

### 4.1 G-RULE

`I rule` asserts seven. **Four files** are `main`'s, byte for byte, and hash to the values the map holds: `advisor/adv3.py` (`d73a657e…`), `advisor/selftest-adv3.py`
(`ef4ffc44…`), `advisor/RULE-ADV-3.txt` (`ee206e7c…`, and the `RULE` constant of `adv3.py`) and `deploy/systemd/adv3-bot.service` (`82acd8e4…`) — four checks, the rule's text and `adv3.py`'s `RULE` line
counted as one. **Three of `adv3-bot.py`**, by `ast.dump` against `main`'s: the definitions that changed are exactly `handle`, `journal` and `selftest`;
the definitions added are exactly `correlation`, `liquidity`, `numbers`, `plan`, `plan_parts`, `returns_of` and `route`, and the one removed is `parse`; and the thirteen others
— `Data`, `Telegram`, `chunks`, `find_chat`, `hello`, `log`, `main`, `make`, `malloc_tune`, `probe`, `put`, `read` and `serve` — are identical, **so the daily path, the probe and the modes are TZ-35's**, while of the module's assignments only `HELP` changed, `HEAD`, `OPEN`, `TOPN` and the tuple
`(STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, CROWD, Z_CAP, LIQ_DAYS)` were added and `CMD` was removed.

### 4.2 The commands and the allocation — what Appendix A answers

**What the Boss sends.** `route` takes the text's first word, with an optional leading `/` and `@botname`, and reads «топ N» or `top N` (N of one or two digits, with a space, a hyphen or none) out of it before it reads the numbers, and reads a number followed by `к`, `k` or `тыс` as thousands (not where a letter follows: «10 коинов» is a risk of 10 %, capped to 1 %).

| the Boss sends | the bot answers |
|---|---|
| «сигнал», «сигналы», «топ», «стратегия», «стратегию»; `signal`, `signals`, `top`, `strategy`; `/signal`, `/signal@bot` — with no number of 100 or more, «топ N» ignored | the TOP-3 message of TZ-36, unchanged, at `10 000` USDT and the risk given (default `0,5 %`, at least `0,05 %`, at most `1 %`) |
| the same, with a number of 100 or more — «сигнал 10000 топ 3», «сигнал 15000 топ 5», «сигнал 15 000 топ 5 1», «топ 3 на 10000», `signal 5000 top 2`, «сигнал 10000», «сигнал 10к топ 3», `signal 15k top 5` | the allocation view, two messages (below), for that **budget**, up to N trades (N from `1` to `10`, default `3`; STRONG never exceeds three), the average risk a trade may lose at its stop being the number below 100 that is not N's (default `0,5` % of the budget, at least `0,05`, at most `1`) |
| «помощь», `/start`, and any other text | `HELP`, which names the commands above, the filter, the cap of three and the defaults |
| any of them, while Binance or Telegram does not answer | the apology of TZ-35, «Binance или Telegram не ответили — повторите «сигнал» через минуту.»; nothing is journaled |

**Selection** (`plan`, from one report, the one the TOP-3 message of the moment is made from). The candidates are the coins of the report's `top` that are in its `strong`, in rank order. A candidate is **rejected, and named with its reason**, when current prices were not served (`marks_ok` false), when its card has no entry
(the price within a quarter of `U` of the stop, or beyond it), when its stop's distance from the entry exceeds `11.1` % — the reason prints the distance — or when `n` trades have already qualified. Every other candidate qualifies. A coin of the TOP-3 that is not STRONG is named as not taken and fills nothing.

**Arithmetic** (`plan`; `k` the number of qualifying trades; `B` the budget; `r` the requested average risk in percent; `d` a trade's stop distance as a fraction of its entry, the card's `stop_pct ÷ 100`; `COST = 0.001` a side, `adv3.COST`).

1. Strength `q = min(|z|, 3)`. Correlation `ρ` of two coins: Pearson on the common days of the last 56 daily log returns up to the close, at least 30 common days and neither series flat, else unknown and counted as `1`. `crowd` of a trade: the mean, over the other trades, of `ρ × side × side` — opposite sides cancel — floored at `0`; `0` for `k = 1`.
2. Weight `w = q / Σq × (1 − 0.5 × crowd)`; share `= w / Σw`.
3. Loss at the stop, as a percent of the budget: `min(1, k × r × share)`; where the sum exceeds `5`, every one is scaled down to make it `5`. The trades average `r`, none loses more than `1 %` of the budget, all together no more than `5 %` — PART VII's sizes, on the budget.
4. Position (notional, USDT) `= loss % ÷ 100 × B ÷ (d + 2 × COST)`; capped at `0.001` of the coin's mean daily quote volume over its last 7 closed days where Binance served it (the reply says «ограничен ликвидностью»); the whole scaled down in proportion where it exceeds `B`; rounded down to a whole USDT; **below `5` USDT the trade is dropped, with its reason**.
5. Leverage is the card's, `min(20, ⌊1 ÷ (1.5 × d + 0.01)⌋)`, isolated, so that liquidation lies beyond the stop. Margin `= ⌈position ÷ leverage⌉`. Loss at the stop `= ⌈position × (d + 2 × COST)⌉` — both sides' costs in. Free `= B − Σ positions`.

A worked case, the bot's first golden check: one STRONG trade, a stop `8 %` of the entry, `B = 10 000`, `r = 0,5`: loss `50`; position `⌊50 ÷ 0.082⌋ = 609`; leverage `⌊1 ÷ 0.13⌋ = 7`; margin `⌈609 ÷ 7⌉ = 87`; loss at the stop `⌈609 × 0.082⌉ = 50`; free `9 391`. The bot's self-test holds five such cases computed by hand, the selection's cases, and the limits over `400` random scenarios.

**The reply**: two messages, each one Telegram part with balanced markup. The first: the budget, the number asked for, the filter and the risk in money; **Итог** — «Подходящих сделок: k из n запрошенных» (or «Подходящих сделок нет»), allocated and margin, the loss at the stops in USDT and as a percent of the budget, and the **free balance with the reason it is free**; then each trade by rank; then the rejected, each with its reason, the coins of the TOP-3 that are not STRONG, and, where `n` exceeds three, the sentence that STRONG is never more than three. The second: the six ratings, the sentence that **the sizes are the Architect's formula, unproven, and that the forward record measures the rule and not this selection**, and the disclaimer. With no current prices, or none qualifying, the reply says so and the whole budget is free.

| the Boss's line | where in the reply |
|---|---|
| total requested budget, total allocated capital | «Бюджет … USDT» in the header; «Размещено … USDT · маржа … USDT» in the Итог |
| number of qualifying trades and their ranking | «Подходящих сделок: k из n»; the trades numbered `1)`, `2)`, `3)` in rank order |
| coin, LONG/SHORT, trade quality | «N) 🟢 coin · LONG · ★ STRONG»; «Качество: z …, сумма знаков … из ±4, доля …%» |
| entry, stop/invalidation, targets | «Вход:» (market, or a limit when the price has run past the zone), «⛔ Стоп:», three «🎯» with the measured shares that reached them, «Инвалидация:» |
| capital allocation per trade | «Капитал: … USDT» |
| recommended leverage and required margin | «плечо …× изол. · маржа … USDT» |
| estimated loss at the stop | «Потеря на стопе: … USDT с комиссиями»; «Потеря на стопах … USDT = …% бюджета» |
| any unallocated balance | «Свободно … USDT — …» |

**The journal**: each allocation answered writes one record of kind `alloc` — the usual fields and `alloc` with the budget, `n`, the risk, allocated, free, the loss at the stops, each trade's coin, side, position, leverage, margin and loss, and the rejected; the plain message writes `request`, as before; the `daily` records are the 06:00 UTC message's alone, and UNIT-NEW and the marks count those.

### 4.3 COPY, G-RENDER, P-START and UNIT-NEW

**COPY** (`I copy`), five: the service copy holds `adv3.py`, `adv3-bot.py` and `commit.txt` and nothing else; `adv3.py` is unchanged, hashing to `d73a657e…`; `adv3-bot.py` hashes to Appendix A's; `commit.txt` is 40 hex characters and
a newline equal to the worktree's `HEAD` and to `origin/tz-37-capital-allocation`; the branch's `adv3-bot.py` equals the service copy's byte for byte.

**G-RENDER** (`I render`), sixteen, on the service copy's bot with `Data` and `liquidity` reading `fapi.binance.com`, Telegram replaced by a stand-in that records each message, and `STATE` pointed at `/root/tz37-work/render-state/`. The six texts are «сигнал», «сигнал 10000 топ 3», «сигнал 15000 топ 5», «сигнал 10000», «помощь» and «привет». The checker recomputes each allocation's plan with the bot's own `plan` from the very report and liquidity that reply was made from, and states the limits itself, from this TZ's numbers, not from the bot's.
(1) every text is answered, with no traceback and no `request failed` in the bot's log; (2) every message's markup balances; (3) «сигнал» holds the six ratings and the forward book by label, at most three cards, each with its basis and its invalidation, in at most three parts; (4) the bot's constants are this TZ's — `STOP_MAX` `11.1`, `MIN_NOTIONAL` `5`, `LIQ_FRAC` `0.001`, `RISK_MAX` `1`, `RISK_ALL` `5`, `TOP_N` `3` and `COST` `0.001`;
(5) each allocation reply is the bot's own `plan_parts` of that plan; (6) **only STRONG coins of the report, in rank order, at most `n` and at most three, none added to fill a place**; (7) every STRONG coin of the report is placed or named with a reason, once; (8) **every position has an entry and a stop within `11.1` % of it, on current prices**; (9) **each loss at its stop within `1` % of the budget, all together within `5` %**; (10) whole positions of at least `5` USDT, together within the budget, the free balance the budget less them; (11) leverage the rule's formula and at most `20`, the margin covering the position, a position within its liquidity cap;
(12) the Boss's fields are in every allocation reply — the budget, the qualifying count, allocated and free, and for each trade the capital, leverage, margin, loss at the stop, stop, three targets and invalidation — and the sentence that the sizes are unproven; (13) «сигнал 10000» is the three-trade view and «сигнал 15000 топ 5» says that STRONG is never more than three; (14) «помощь» and «привет» answer `HELP` and nothing else; (15) the scratch journal holds, in order, `request`, `alloc`, `alloc`, `alloc`, each allocation record with its plan's allocated, free and coins; (16) the bot's own `journal.jsonl` and `daily-sent` hash as before the run.
**Only counts and labels are printed**, among them the number of STRONG coins in the report and the number of trades placed per allocation. **A day with no qualifying trade reads 16 of 16 with zero placed, and then proves the routing, the empty reply and the journal on live data and nothing about sizes on it** — the sizes are proven by the self-test's cases on the very bytes COPY compares, and by the checker's stand-in run; the report prints the count.

**P-START** is `adv3-bot.py --probe`, which this TZ does not change: it asserts each of its five replies served and parsed — closed daily candles of BTCUSDT, the last at most two days old; funding settlements; a mark price for every one of the 42 coins; the funding intervals; and `getMe` answering `is_bot`. `liquidity`, which `handle` calls to give `plan` the volumes, reads the same `fapi.binance.com` klines endpoint P-START proves.

**UNIT-NEW** (`I unit new`), nine, read against the `kill` mark's snapshot: the unit `active`, `running`, `enabled`; a new `MainPID` and `NRestarts` one more; the process started after the mark and within 90 s of it; its argv the unit's exact one, alone;
the service copy's `adv3-bot.py` Appendix A's and the process started after B-DEPLOY's copy; `adv3.py` and the unit file unchanged; `daily-sent` and the journal's count of `daily` records as at the mark — the Boss's own requests add records of
other kinds; `service.log` showing the new process serving and no daily sent and no traceback since the mark; the three capture units active with their `MainPID` and `NRestarts` as at the mark.

### 4.4 The stops — CANON hard rule 14

**The unit's restart policy is TZ-35's, unchanged** — `Restart=always`, `RestartSec=30`, `RestartPreventExitStatus=3 4` — and so is its stop, K-35, `systemctl disable --now
adv3-bot.service`, which K-37 repeats. **B-ROLLBACK**, on a FAIL of COPY, G-RENDER, P-START or UNIT-NEW, at once, the Executor's own: the file and `commit.txt` return to what
B-DEPLOY saved.

```
{ date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz37-work/stage/research/tz37-capital-allocation.py mark rollback && cp -p /root/tz37-work/bot.before /root/adv3-bot-svc/adv3-bot.py.new && mv /root/adv3-bot-svc/adv3-bot.py.new /root/adv3-bot-svc/adv3-bot.py && cp -p /root/tz37-work/commit.before /root/adv3-bot-svc/commit.txt; echo "exit=$?"; } >> /root/tz37-work/logs/NN-b-rollback.log 2>&1
sha256sum /root/adv3-bot-svc/adv3-bot.py; cmp /root/adv3-bot-svc/commit.txt /root/tz37-work/commit.before; echo "cmp exit=$?"
```

`exit=0`, the `sha256sum` printing `e65de91c…` and `cmp` exit `0`, or the run is BLOCKED with the file's state named. Where the unit was **not** signalled (a FAIL of COPY,
G-RENDER or P-START) that is all: the running process never loaded the new file. Where it **was** (a FAIL of UNIT-NEW), the signal follows, its mark inside the
block, in the band of §3.5:

```
until s=$(( $(date +%s) % 86400 )); [ $s -ge 23700 ] && [ $s -le 85800 ]; do sleep 5; done; { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz37-work/stage/research/tz37-capital-allocation.py mark kill2 && systemctl kill --signal=SIGTERM adv3-bot.service; echo "exit=$?"; } >> /root/tz37-work/logs/NN-b-kill2.log 2>&1
```

and at least 45 s later `I unit old` (every 15 s while it prints `NOT YET`, at most 100 s after that mark) — **UNIT-OLD**, `READING UNIT-OLD: PASS - 10 of 10`: UNIT-NEW's nine read against the second mark with the old `adv3-bot.py`
and `NRestarts` two more than at the first mark.

**K-37**, on a FAIL of UNIT-OLD only — the advisor is then stopped, and the Boss is told:

```
{ date -u +%FT%T.%NZ; systemctl disable --now adv3-bot.service; echo "exit=$?"; } >> /root/tz37-work/logs/k37.log 2>&1
```

by the classifier route where refused (map §6, sandbox limit: the Boss runs the block), verified at least 30 s later by
`I stopped`, which must print `READING STOPPED: PASS - 2 of 2`. **UNDECIDABLE closes nothing and stops nothing; under PASS K-37 is not run.**

### 4.5 What a PASS establishes, and what it does not

The service copy's `adv3-bot.py` is Appendix A's and the unit runs it; the rule, its message, the bot's unit and the other advisor files are byte-for-byte what TZ-36 and TZ-35 deployed, and the bot's other
definitions — the daily path, the probe and the modes among them — are tree-for-tree theirs; the six texts of G-RENDER are answered on live data with the shapes §4.2 fixes and, on that data, the allocation keeps the limits §4.2 states. **Not established:**
that the allocation is a good one — the weights are the Architect's, unproven (§1), and the forward record, read after 2027-10-28, measures the rule and not them; that a day with qualifying trades was among the six texts' (the report prints how many trades were placed); that the Boss's Telegram shows the reply as the Architect expects, which is his next
«сигнал 10000 топ 3»; and anything about the market to come.

---

## 5. The files

**`advisor/adv3-bot.py`** — replaced: `route` and `numbers` replace `parse` and `CMD`; `OPEN`, `HEAD`, `TOPN`, the tuple `(STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, CROWD, Z_CAP, LIQ_DAYS)` and `HELP` are the module's new or changed constants; `returns_of`, `correlation` and `liquidity` read the candles and the volumes,
`plan` selects, weighs and sizes, and `plan_parts` writes the reply; `handle` routes and answers and `journal` takes the allocation's record; `selftest` checks 67 things offline. Every other line is TZ-35's. **`research/tz37-capital-allocation.py`** — this TZ's checker: `fingerprint`, `host`, `number`,
`rule`, `selftest`, `mark`, `copy`, `render`, `unit`, `keep` and `stopped`. Where a reading can be a pure function it is — `parse_map`, `bot_checks`, `plan_invariants`, `render_checks`, `unit_checks`, `log_since`, `memory_gate`, `number_reading`, `daily_records`, `kept_files` — and its self-test runs each on stand-ins, with a negative control for every one that can fail; `host`, `copy`, `mark`, `keep` and `stopped` read the host and are exercised there, and `render` on the real bot with
synthetic market data and a stand-in service copy. It starts, stops and signals nothing; its `render` runs the service copy's bot. Standard library alone, under `/root/tz04a-env`.

---

## 6. Cost

Measured by the Architect on 2026-10-31 under Python 3.13.18 and taken at the population's upper bound.

| check | population | measured | bound |
|---|---|---|---|
| the three self-tests | 44, 67 and 50 checks, no network | `0.10` s, `0.18` s and `0.06` s of wall | `30` s each |
| G-RULE, fingerprint, NUMBER, COPY, the marks, G-RENDER and the rest of the checker's modes against stand-ins | `git show`, two parses, 56 files, systemd, small files, and the real bot on synthetic data | `4.8` s together, 36 assertions, most of it the real bot's synthetic run | `5` s a run |
| G-RENDER | one process: 84 requests of `Data` over six threads once, 2 requests a reply for the marks and the funding intervals, at most 3 a reply for the volumes; four reports and their replies | `1.8` to `1.9` s of processor on 1,500-candle synthetic coins for the four reports and the replies — `0.0005` s of it the plan — and `49,168,384` bytes at its peak, the largest of three runs; TZ-35 measured `1.2` to `1.4` s of processor for a live run of `adv3.py` | `900` s of wall, the `timeout`; `30` s of processor |
| P-START | five requests, one after another | TZ-35: `0.1` to `0.2` s | `546` s of wall at worst — four requests at `129` s and one at `30` s — without processor |
| UNIT-NEW | `systemctl show`, `/proc`, the log | under `1` s a run | `30` s; at most 8 runs |

**Single-session processor at most `380` s at those bounds** — the self-tests `90`, G-RENDER and P-START `30`, at most 40 checker runs at `5` s, `200`, and the `reclaim`, `git` and `systemctl` commands `60` — **under `3,600`, so nothing is sampled.**
**Wall clock about 40 minutes:** §0 to §3.3 about 12 minutes; §3.4's wait, none inside the band, and about 4 minutes; §3.5 about 4; §3.6, the report and §9 about 20; **about 1 h 5 min with every `timeout` and every request at its bound** —
`8 + 5 + 2 + 5 + 16 + 13 + 2 + 10 + 3 = 64` minutes (§0 with the memory re-read; §3.1; §3.2; §3.3; B-DEPLOY, COPY and G-RENDER at 900 s; P-START at 546 s, the signal and the wait of 145 s; §3.6; the report; §9) — plus a wait for a band that is at most 6 h 50 min, from 23:45:00 to 06:35:00 UTC. **The host pays, after the session:** nothing it did not pay before.

---

## 7. Validation

| # | check | count |
|---|---|---|
| **V1** | §0.2's fingerprint | `READING FINGERPRINT: PASS - 65 of 65`: revision `2026-10-31-a`; 6 anchors, 4 re-derived; 56 rows, 53 of 53 `frozen` equal |
| **V2** | §0.3's host gate | `READING HOST: PASS - 16 of 16`; the memory figures of the first read and of the second, if one was made |
| **V3** | §0.5's NUMBER, at §0.5 and at §3.1 | `READING NUMBER: PASS - 2 of 2` each, the `TZ-37-` path printed; the branch count `0` |
| **V4** | §0.1's and §3.1's files | 2 of 2 hashes asserted at each, lines and bytes; the branch's diff naming exactly `M`, `A`, and `--numstat` exact |
| **V5** | the self-tests | `44 of 44`, `67 of 67`, `50 of 50` |
| **V6** | G-RULE | `READING RULE: PASS - 7 of 7` |
| **V7** | B-DEPLOY | `exit=0`; the mark printed |
| **V8** | COPY | `READING COPY: PASS - 5 of 5` |
| **V9** | G-RENDER | `READING RENDER: PASS - 16 of 16`; the replies' sizes, the number of STRONG coins and the number of trades placed per allocation printed |
| **V10** | P-START | `READING P-START: served - 5 of 5 endpoints`, each line printed |
| **V11** | B-KILL and UNIT-NEW | `exit=0`; `READING UNIT-NEW: PASS - 9 of 9`, both pids, both instants |
| **V12** | contract §4.2's self-check | run after the push and the pull request and before the report's commit |
| **V13** | §3.6's closing reads | every read printed |
| **V14** | B-RECLAIM-SCRATCH and §9's `keep` | files considered, copied and held; the store's count after equal to before plus the copies |
| **V15** | §9's removals | `git worktree remove` without `--force` exit `0`; `test -e` exit `1` for `/root/tz37-work` and each directory removed; `git worktree list` naming `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else |

---

## 8. The report

`CryptoReports/TZ-37-capital-allocation-report.md`, in contract §8's order. **In its first ten lines:** NUMBER at both reads; G-RULE;
the three self-tests; B-DEPLOY, COPY, G-RENDER — with the number of STRONG coins the report held and the trades placed per allocation — and P-START; B-KILL and UNIT-NEW with the pids; whether a rollback ran; whether the unit
runs, and how that was verified. Beyond what V1 to V15 print: every mark's instant; every block the classifier refused, who ran it and when; the unit's
journal lines; each memory and free-space read with its instant and bound; the commit and the pull request; §9's counts and removals; and every file the
run wrote, by SHA-256, but the bot's own root. **It never prints the token, the chat id, the content of any file under `/etc/adv3-bot/`, or a coin, a
price or a size from the live replies** (§2 item 7). The report is drafted in the primary checkout `/root/btc-5m-twap` before B-RECLAIM-OWN and committed
after it.

---

## 9. Reclaim — the host left clean (CANON hard rule 15)

**What a file is kept for:** `I keep` copies every file under `logs/`, `state.json`, `bot.before` and `commit.before` into
`/root/btc-forensics/` as `tz37-work--<path with - for />`, by exclusive create, and verifies each hash; a name already there with the same hash
is counted as held, and with another a failed assert. The branch worktree is not copied: `keep` asserts that `git status --porcelain --ignored` in
it prints nothing and that its `HEAD` is its upstream's, so `git worktree remove` needs no `--force`. **No output of `keep` or `reclaim` is
filtered**: every line it prints is quoted. B-RECLAIM-SCRATCH is §3.3. `render-state/` is scratch and goes with the tree.

**B-RECLAIM-OWN**, last, after §3.6 and with the report drafted. **Its output is written to no file; the report quotes it verbatim from the
session**, every line of it:

```
nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz37-work/stage/research/tz37-capital-allocation.py keep
git -C /root/btc-5m-twap worktree remove /root/tz37-work/wt; echo "exit=$?"
rm -rf /root/tz37-work; echo "exit=$?"
test -e /root/tz37-work; echo "exit=$?"
git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
find /root/btc-forensics -type f | wc -l
df -B1 --output=source,size,avail /var/lib/btc-recorder
```

The branch `tz-37-capital-allocation` stays on `origin` and as a local ref; only its working tree goes. **Kept:** `/root/adv3-bot-svc/` is the running
unit's code, `/var/lib/adv3-bot/` its record, `/etc/adv3-bot/` the Boss's token and the pinned chat; the capture roots, both archives' state and the
forensic store are data, never scratch. **A refused `rm -rf` is handed to the Boss** by §3.3's route, one tree per command, and verified by `test -e`.

---

## 10. Pre-send checks

Performed by the Architect on 2026-10-31 against this file as sent, in a reading separate from its writing — the body was written, read
start to end and corrected where it read wrongly (the corrections are named in C7), and this section written after — with the repository at `origin/main`
`a5c66a17f0d05ca19dc68eccaf948df58698289d` (the merge of PR #36; fetched again before sending, `main` still carrying map revision `2026-10-29-b`, no `TZ-37-` file, no report and no `tz-37` branch) and map revision `2026-10-31-a`, the file the Architect delivered with TZ-36's verdict
(1,971 lines, SHA-256 `a164eb530a1d8188312e864e8256cc9405346c68e21e98b7f9cd077ebb7046ef`), which `main` does not yet hold and the upload that carries this TZ puts there. Line numbers
are those of the files §0.1 extracts for Appendix A, and those of `main` for committed code.

| # | check | result |
|---|---|---|
| **C1** | scope against body | **Repository paths the body names:** `CryptoTZ/TZ-37-capital-allocation.md`, read by §0.1's script and named by `number`; `CryptoTZ/` and `CryptoReports/`, listed by `number`, every `CryptoReports/*.md` read by TZ-35's `reclaim` for hash tokens; `SYSTEM-MAP.md` and the other 55 rows of its table, read by `fingerprint`, among them `BTC-EXECUTOR-INSTRUCTIONS.md` (cited for contract §1, §4.1, §4.2 and §8), `research/tz33-reward-book-capture.py` (cited for line 190), `research/tz35-advisor-deploy.py` (run for `scratch` and `reclaim`), and `research/twap-divergence.py`, `research/recorder/recorder.py` and `research/pfair.py` (hashed for the anchors); `advisor/adv3-bot.py`, written on the branch and copied to the service; `research/tz37-capital-allocation.py`, written on the branch; `advisor/adv3.py`, `advisor/selftest-adv3.py`, `advisor/RULE-ADV-3.txt` and `deploy/systemd/adv3-bot.service`, read by `rule`, run or hashed, never written; `CryptoReports/TZ-37-capital-allocation-report.md`, written to `main`. **Host paths:** `/root/tz37-work/**` written (`render-state/` among it, scratch); `/root/adv3-bot-svc/adv3-bot.py` and `commit.txt` written, `adv3-bot.py.new` transient, `adv3.py` hashed; `/var/lib/adv3-bot/{daily-sent,journal.jsonl,service.log}` read and hashed; `/etc/adv3-bot/token` read by the bot's own `--probe` and nowhere else; `/etc/systemd/system/adv3-bot.service` hashed; `/var/lib/btc-recorder` read by `find`, `grep -c` and `df`; the other capture stores by `du`; `/root/btc-forensics` written by `keep` and `reclaim`; `/proc/meminfo` and the processes' `cmdline` and `stat` read by `host` and `unit`; the UUID directories of `/tmp` read, copied from and removed by TZ-35's checker. **Entry points:** this checker's modes `fingerprint`, `host`, `number`, `rule`, `selftest`, `mark` (four marks), `copy`, `render`, `unit` (`new`, `old`), `keep` and `stopped`; TZ-35's `scratch` and `reclaim`; `selftest-adv3.py`; `adv3-bot.py --selftest` and `--probe`; `git` (`fetch`, `ls-remote`, `log`, `worktree`, `add`, `diff --cached`, `commit`, `push`, `show`, `rev-parse`, `status`), `gh`'s credential helper; `systemctl` (`show`, `list-timers`, `is-enabled`, `kill`, and `disable` at K-37 only); `journalctl` (the unit's lines, §3.6), `cp`, `mv`, `sha256sum`, `cmp`, `timeout`, `nice`, `rm -rf`, `test -e`, `du`, `df`, `free`, `find`, `grep`, `wc`, `ls`, `cat`, `tail`. **Outputs:** under `/root/tz37-work/` `logs/`, `stage/`, `wt/`, `render-state/`, `state.json`, `bot.before`, `commit.before`; the service copy's two files; the forensic store's copies; the branch, its pull request and the report. **Intersections with §2, by path and by content class, seven, each named in §2:** the bot's `--probe` reads the token — item 3's exemption; G-RENDER's and P-START's requests — item 3; `systemctl list-timers`, `is-enabled` and `show` — item 4; `find`, `grep -c`, `df` and `du` on the capture stores — item 5; `tail` of `service.log`, `journalctl` of the unit, `cat state.json` and `ls` of the record — item 7: they carry log lines, pids, instants and sizes, and `service.log`'s lines name a close and a kind of request, never a coin or a price; **`render-state/journal.jsonl`** — item 7's content class, prices and coins of cards and the allocation's figures, public market data: it is a scratch file of the work tree, never printed, never copied by `keep` (which copies `state.json`, `bot.before`, `commit.before` and `logs/` alone) and removed with the tree by §9; the live replies — item 7: held in memory by the stand-in, never printed, `render` prints counts and `READING` lines. **Classes checked and intersecting nothing:** labels, outcomes and settled documents — this TZ reads none; Binance's candles, marks and volumes pass through the service copy's `Data`, `make` and `liquidity` and the live render and are stored nowhere but in that scratch journal's cards. |
| **C2** | origin of every expectation | **Quoted from a committed artifact:** `56`, `53`, `2`, `1`, the six anchors and `2,232` — map `2026-10-31-a` §0 and §3 (§3 at its line 1298), counted independently of the checker by a parse of the table (56 rows: 53 `frozen`, 2 `tracked`, 1 `reported`) and each of the 55 hashed against its blob at `a5c66a1`, `55 of 55` equal, then by `fingerprint` against an export of that tree with the map in place, `PASS - 65 of 65`; the hashes `e65de91c…`, `d73a657e…`, `ef4ffc44…`, `ee206e7c…`, `82acd8e4…` — map §0's table rows, and `sha256sum` of the files at `a5c66a1`; `65,490,944` — map `2026-10-31-a` §6, memory row (line 1683), `I render`'s process tree; `7,300,000,000` — `research/tz33-reward-book-capture.py` line 190, `STREAM_FLOOR = 7300000000`, and map §2.6; `31,612,203,008` and `e3975b5…` — map §6's host identity (line 1659); `44` — `selftest-adv3.py`, run; `11.1` — the Boss's text; `1`, `5`, `0.5` — `adv3.RISK_MAX`, `RISK_ALL`, `RISK`, line 22; `3` and `1.0` — `adv3.TOP_N`, `STRONG_Z`, line 19; `0.001` — `adv3.COST`, line 18; `1` of 5 — `adv3.RELIABILITY`, line 37; `5,265` and `253` — CANON PART VII and `adv3.FACTS`. **Computed by an implementation independent of the one under test:** `130,981,888` = 2 × `65,490,944`, arithmetic; `49,168,384` — `resource.getrusage` peak of a process that built four reports and answered five commands on synthetic candles of production size (42 coins × 1,500 days), Python 3.13.18, the largest of three runs (`49,086,464`, `49,168,384`, `48,979,968`); `405 29` and `808 0` — `git diff --cached --numstat` over the extraction of Appendix A into a clone at `a5c66a1`, exact; the lines, bytes and hashes of §0.1 — `sha256sum` and `wc` over the two files, and §0.1's script run against this file over an empty stage and over a worktree, equal; the worked case of §4.2 (`609`, `7`, `87`, `50`, `9 391`) — exact rational arithmetic in a script of the Architect's, equal to the bot's first golden check; §1's `550`, `1,650`, `1,100`, `3,300`, `910` and `9.1 %` — the same, at `d = 0.089`; §1's history figures — a script over the Architect's re-derivation of the history (5,265 trades, 253 STRONG, in sample, not committed): median stops `12.63 %` and `14.44 %`, quartiles `10.3` and `18.3`, `74` within `11.1 %` at a median of `8.90 %`, means `+1.276` and `+0.246` R, `27` winners, five trades `108 %` of `+94.4` R, the other 69 at `−0.110` R, `37.1 %` of the base trades. **Fixed by Appendix A's code, which this TZ measures nothing to set:** `16`, `2`, `7`, `5`, `16`, `9`, `10` and `2` (HOST, NUMBER, RULE, COPY, RENDER, UNIT-NEW, UNIT-OLD, STOPPED), `5` endpoints, `6` texts and `4` journal records of the render, `67` and `50` — each the count its function's dictionary or tuple holds, re-run by the Architect where it runs off the host (C5). **Fixed by this TZ and measured by nothing:** `5` USDT, `0.001` of the volume, `7` days of it, `0.5` for the crowding, the cap `3` on strength, the 90 s and 100 s windows, the 45 s wait, the 60 s memory re-read, the `600`, `900` s `timeouts` — the Architect's choices, named so. **§0.4's floors and §3's bands:** `130,981,888` = 2 × `65,490,944`; `7,400,000,000` = `7,300,000,000` + `100,000,000`; `23,700` = 6 × 3,600 + 35 × 60, `85,500` = 23 × 3,600 + 45 × 60, `85,800` = 23 × 3,600 + 50 × 60; `546` = 4 × `129` + `30`, `129` = 4 × 30 + 1 + 3 + 5. **No expectation depends on a quantity this TZ measures but as an inequality or an equation that holds for every admissible value of it:** UNIT-NEW reads `NRestarts` as the `kill` mark's plus one, the capture units' as the mark's, and the journal's daily records as the mark's — whatever the mark read; the memory gate is an inequality on a read; G-RENDER's limits are inequalities (a stop within `11.1 %`, a loss within `1 %` and `5 %` of the budget, a position within its cap) and its equations are between the replies and a plan recomputed from the same report; the number of trades placed is printed, never asserted. |
| **C3** | shape of every diff | Two paths. **`advisor/adv3-bot.py` replaces 29 committed lines**, read from `git diff --cached -U0` at `a5c66a1` and printed by line: `7` (the imports, which gain `math`), `20` (`CMD`), `22` and `23` (`HELP`'s two command lines), `110` to `113` and `115` to `120` (`parse`'s head and its body after `return None`, replaced by `numbers` and `route`), `180` (`journal`'s signature), `250`, `253`, `254`, `256` and `259` (`handle`'s `parse` call, its `make` and `send` lines, the journal call and the log line), `333` (`selftest`'s docstring), `340` to `345` (its `parse` cases), `369` (the stand-in's `params['text']` test) and `378` (its local imports) — `--numstat` `405 29`: 405 lines added, 29 removed. **`research/tz37-capital-allocation.py` is new**: `git cat-file -e origin/main:research/tz37-capital-allocation.py` exits `128`, so the change replaces none of its lines; the report's path and this TZ's own path exit `128` as well. No sentence of this TZ calls the bot's change additive. |
| **C4** | cost of every check | §6, at the population's upper bound. **Processor, single session, term by term:** the three self-tests `3 × 30 = 90` s against `0.10`, `0.18` and `0.06` s measured; G-RENDER and P-START `30` s against `1.9` s at most measured for G-RENDER's four reports and replies — `63,000` candle-days a report, `252,000` for the four, `7.7` µs a candle-day — and `0.1` to `0.2` s measured by TZ-35 for P-START; at most 40 checker runs `40 × 5 = 200` s — the checker's every mode against stand-ins together `4.8` s, its self-test `0.05` s; and `reclaim`, `git` and `systemctl` commands `60` s: **`90 + 30 + 200 + 60 = 380` s, under `3,600`; nothing is sampled.** **The fail-fast bounds, each with its derivation:** `adv3.get`'s four tries — four `30` s timeouts and the `1`, `3` and `5` s between them, `129` s, `adv3.py` lines 42 to 60, unchanged by this TZ — make a render with Binance silent worst at `14 × 129 = 1,806` s for `Data`'s 84 requests over six threads, `8 × 129 = 1,032` s for the marks and funding intervals of four replies and `9 × 129 = 1,161` s for the volumes of at most three STRONG coins in three allocations, `3,999` s in all, so G-RENDER runs under `timeout 900`; P-START's five requests one after another, `4 × 129 + 30 = 546` s of wall (Telegram's `call` has one try of `30` s), `adv3-bot.py` lines 459 to 481; UNIT-NEW's `NOT YET` at most 100 s after the mark, every 15 s, at most 8 runs. **Wall clock:** about 40 minutes, about 1 h 5 min with every bound reached — `8 + 5 + 2 + 5 + 16 + 13 + 2 + 10 + 3 = 64` minutes — plus a wait for a band of at most 6 h 50 min. Disk at the same bound: §0.4's `100,000,000`; the logs are under `2,000,000` bytes. |
| **C5** | every count | `65` = 1 revision + 6 anchors + 4 re-derived + 53 frozen rows + 1 table shape, the map's table read by `parse_map` (lines 140 to 153) and counted again by the Architect's script — `56` rows, `53` frozen, `2` tracked, `1` reported. `16`, `mode_host` lines 351 to 392: H1 one, H2 two, H3 one, H4 three, H5 six, H6 one, the memory gate and the disk gate; re-run on stand-ins, `16 of 16`, and with a first memory read below the floor decided by the second. `2`, `number_reading`, lines 395 to 398. `2` files and `2` hashes, §0.1. `7` = 4 file checks of `mode_rule` (lines 417 to 433: `adv3.py`, `selftest-adv3.py`, the rule text with the `RULE` line, the unit file) + 3 of `bot_checks` (lines 167 to 178); run on the repository at `a5c66a1` against the extracted files, `7 of 7`, and with five negative controls reading FAIL. `67` = 34 `route` cases + 33: `HELP` one, `chunks` one, `put` one, the stand-in's sends three, the synthetic report two, the golden cases five, selection five, liquidity one, budget one, minimum one, the limits over 400 random scenarios one, `plan_parts` five, `handle` five, glibc one — listed by name from an instrumented run, `67 of 67`, on the finished bytes and on the files extracted by §0.1's script. `50` = `parse_map` 2, `bot_checks` 5, `render_checks` 25 (the positive case and 24 negative controls), `unit_checks` 10, `daily_records` 1, `log_since` 2, `memory_gate` 1, `number` 3, `kept_files` 1 — `50 of 50`. `44`: `selftest-adv3.py`, unchanged, `44 of 44` with `adv3.py` at `a5c66a1`. `16` = the entries of `render_checks`, lines 212 to 269, asserted equal to 16 by the self-test; `16 of 16` on the real bot with synthetic market data, and a bot that does not reject a stop beyond `11.1 %` reads FAIL. `5`, `mode_copy` lines 470 to 481, `5 of 5` on a stand-in. `5` endpoints, `probe`, `adv3-bot.py` lines 459 to 481 — unchanged: klines, funding, marks, intervals, `getMe`. `9`, `unit_checks` lines 272 to 292, and `10` with its extra check in `mode_unit`; `9 of 9` on stand-ins, with eight single-fault negative controls and a moved capture unit. `2`, `mode_stopped`. `6` = `RENDER_CASES`, `4` = `RENDER_KINDS`. `7` and `13`: G-RULE's three bot checks name 3 changed, 7 added, 1 removed and 13 identical definitions — `handle`, `journal`, `selftest`; `correlation`, `liquidity`, `numbers`, `plan`, `plan_parts`, `returns_of`, `route`; `parse`; `Data`, `Telegram`, `chunks`, `find_chat`, `hello`, `log`, `main`, `make`, `malloc_tune`, `probe`, `put`, `read`, `serve` — against the 17 top-level definitions of `main`'s bot, the AST lists saved from the run. V1 to V15 are the fifteen rows of §7. The checker's `--numstat` is `808 0`. |
| **C6** | every population | NUMBER: the paths under `CryptoTZ/` and `CryptoReports/` of `origin/main` at each of its two reads. FINGERPRINT: the map's table of 56 rows against the files of the primary checkout. HOST: the host at the instant of the read — its units, files, memory and disk; the memory figure, the first read and, if it fell below the floor, the second. RULE: `adv3.py`, `selftest-adv3.py`, `RULE-ADV-3.txt`, the unit file and `adv3-bot.py` of `origin/main` against the branch's. The self-tests: synthetic candles and stand-ins, no network. COPY: `/root/adv3-bot-svc` and the worktree. RENDER: the service copy's bot answering six texts on the latest close at the instant of the run — the 42 coins' 1,500 candles each, marks, funding intervals and the volumes of at most three STRONG coins — and, for each of three allocations, the plan recomputed from the report and the volumes that reply was made from. P-START: one request to each of five endpoints. UNIT-NEW and UNIT-OLD: the unit, the three capture units, `daily-sent`, the `daily` records of `journal.jsonl` and `service.log`'s lines stamped at or after the mark less 1 s. KEEP: the files of the work tree named in §9. RECLAIM: the UUID directories `scratch` names earlier. §1's history figures: the 5,265 trades of the rule and the 253 STRONG trades of the Architect's re-derivation, in sample, the stop distance as a share of the entry, and the 74 within `11.1 %` against the 179 beyond. No statistic of this TZ is a calibration claim and none is read against a label. Each memory figure: one mode's process; `MemAvailable` and free space: the host at each read. |
| **C7** | every signature and every behaviour | **Committed code this TZ relies on, read at `a5c66a1`.** `adv3.py` — `def get(url, tries=4):` line 42, four tries of 30 s with 1, 3 and 5 s between them (lines 42 to 60), the `129` s of §6; `def fapi(path, **params):` 133, which `liquidity` calls with the klines path and `limit=8`; `def ranking(day_states):` 285, with `top = sorted(active, key=lambda cs: -abs(cs[1][1]))[:TOP_N]` 288 and `strong = [coin for coin, s in top if s[2] == 4 * s[0] and abs(s[1]) >= STRONG_Z]` 289 — STRONG as §1 states it, at most three; `def report(cs, funds, marks, deposit, risk, now_ms, missing=(), intervals=None):` 427, whose `rep` holds `top`, `strong`, `cards`, `rows`, `missing`, `marks_ok`, `made_at_ms` and `close_of` (lines 462 to 468), `rows` holding all 42 coins and `{'signal': None, 'missing': …}` for those without candles, so `plan`, which reads `rep['rows'][coin]` for coins of `top` alone, reads a coin with a signal; `'marks_ok': bool(marks)` 468 — `marks_ok` is false only where no mark came at all, and a coin whose mark is missing falls back to the close in `card` (`P = row['mark'] if row['mark'] else C`, 477), as the daily message's cards do; `def card(coin, row, is_strong, deposit, risk):` 473 — `S = C - k * U` 476, `mode, entry = … ('none', None)` 480 and 482, so a price within `NEAR_STOP × U` of the stop, or beyond it, has no entry, and `stop_pct=100 * dist / entry` with `leverage=min(20, math.floor(1 / (1.5 * dist / entry + 0.01)))` 491 and 492 — §1's 11.1 % and §4.2's item 5; `def trust(rep):` 360, reading `rep['made_at_ms']`, `rep['close_of']`, `rep['missing']`, `rep['marks_ok']` and each card's `coin` and `mode` (366 to 369), which is why `plan_parts` may hand it a report whose `cards` are the allocation's; `def trust_lines(rep, facts):` 625; the constants `TOP_N, STRONG_Z, STRONG_MAX, ZONE, NEAR_STOP = 3, 1.0, 3, 0.25, 0.25` 19, `DEPOSIT, RISK, RISK_MAX, RISK_ALL = 10000.0, 0.5, 1.0, 5.0` 22, `RELIABILITY, STRONG_JUSTIFIED = 1, False` 37, `COST` `0.001` and `VOL_DAYS` `56` 18. `adv3-bot.py` of `main` — `CMD` 20; `parse`, lines 110 to 120, with `deposit = next((x for x in nums if x >= 100), adv3.DEPOSIT)` 117, `risk = rest[0] if rest else adv3.RISK` 119 and `return min(deposit, 10_000_000.0), min(max(risk, 0.05), adv3.RISK_MAX)` 120 — §1's sentence, and the measured misreading follows from them: «топ 3» leaves the `3` among the numbers below 100; `handle`, lines 249 to 268, with `tg.send(HELP)` 261 and the apology 266; `Telegram.call(self, method, http_timeout=30, **params)` 68, one try; `make(data, deposit, risk)` 163 returning `rep, adv3.message(rep, adv3.FACTS)` 177; `journal(kind, rep, ids)` 180; `Data.fresh` 131, which raises `fapi.binance.com served no candles` (153) only where every coin failed; `serve`, lines 191 to 246, with 207 `log('serving the pinned chat: pid', …)` and 225 `log('daily sent for the close of', …)` — the two lines `log_since` reads — and `probe` 271 to 293, both identical to Appendix A's by G-RULE. TZ-35's checker `research/tz35-advisor-deploy.py` — `reclaimable`, lines 279 to 284: a UUID directory under `/tmp/` whose parent's name carries `btc-5m-twap`; `mode_scratch(own)`, 419 to 431, lists the siblings of `own`; `mode_reclaim(trees)`, 434 to 487, asserting at 435 and printing `RECLAIM PASS` at 486; `main`, 774 to 798: `scratch` takes exactly one argument (783), `reclaim` any number (786). The unit — `WorkingDirectory` line 12, `ExecStart` 13, `Restart=always` 14, `RestartSec=30` 15, `RestartPreventExitStatus=3 4` 16, `MemoryMax=128M` 18, `ReadWritePaths=/var/lib/adv3-bot` 22. **Every behaviour this TZ attributes to Appendix A:** `numbers` 119 to 130; `route` 133 to 149; `returns_of` 209 to 212; `correlation` 215 to 225; `liquidity` 228 to 236; `plan` 239 to 302; `plan_parts` 305 to 355; `journal` 358 to 367; `handle` 428 to 456 — each sentence of §4.2 is the body of one of them, and the bot's self-test holds a check on each. The checker — `parse_map` 140, `top_level` 156, `bot_checks` 167, `plan_invariants` 185, `render_checks` 212, `unit_checks` 272, `log_since` 295, `memory_gate` 313, `mode_fingerprint` 322, `mode_host` 351, `number_reading` 395, `mode_rule` 417, `daily_records` 436, `snapshot` 448, `mode_mark` 456 — `kill` and `kill2` assert `daily-sent` is today's UTC date —, `mode_copy` 470, `mode_render` 484, `mode_unit` 548 — `NotYet` while the old process runs within 100 s of the mark —, `kept_files` 575, `mode_keep` 584 and `mode_stopped` 614. **Sentences rewritten in this reading:** the header cited map §6 for the archives' calendar runs (`01:30:20` and `03:00:20`), where map §2.6 and §2.5 hold them; §1 gave the weights CANON §1.2's last sentence and §1.6, which close direction models and not a differentiator between trades — rewritten to CANON's first question, whether the number is real; §1 quoted the Boss as "do not force a stop", which is not his sentence — it now carries his own, "reject the setup rather than forcing an unsuitable stop", and every quotation of his text was set to his capitals; §1's sentence on the passers' median stop read ambiguously and was rewritten; §4.2 used "stop distance" for a price difference and for a share of the entry — `d` now names the share; §4.3 said `plan` calls `liquidity`, where `handle` does; §2 allowed `systemctl list-units`, which no block runs; §0 called the shelved clean-up and table "built and tested", which no committed file can show — struck; §0.4 gave the peak of one run, `48,664,576`, where the largest of three is `49,168,384`; the checker's G-RENDER did not read the sentence that the sizes are unproven — it does now, and its self-test has a negative control for it; and a reading of `numbers` found that «сигнал 10к топ 3» would be read as a risk of 10 %, capped to 1 %, and answered with the plain message — the silent misreading §1 measures in `parse` — so `numbers` now reads `10к`, `10k` and `10 тыс` as thousands, with four more `route` cases, and every count and hash of this section is that of the bytes sent. |
| **C8** | every cross-reference | Resolved by reading the text referenced. **Map `2026-10-31-a`:** §0's anchors and its table of 56 rows, 53 / 2 / 1; §1's record of refs (a difference from it is recorded, not blocking, §0.5); §2.5 and §2.6 for the archives' calendar runs, §2.6 for `STREAM_FLOOR` `7,300,000,000`; §2.7's record under `/var/lib/adv3-bot/` and the token under `/etc/adv3-bot/`; §3's `2,232` files in the forensic store, the two directories TZ-36 left and the live session `238335b9…` (its line 1298); §6's host identity (line 1659), `/root/tz04a-env` on Python 3.12, the push through `gh`'s credential helper ("git remote"), the sandbox limit on destructive actions — `kill` refused by the permission classifier, a single-tree `rm -rf` sometimes refused and then the Boss's — and its memory row with `65,490,944` (line 1683); §7 items 125 and 129, a reload re-arming an archive's run and the rule that a TZ states it, 131, the floor rule applied in §0.4, and 137, the memory floor below a first read. **CANON `2026-10-29-b`:** PART VII, the advisor, its sizes (0.5 % a trade by default, 1 % at most, 5 % in all), its forward record read once after 2027-10-28; PART V, "a tool the Boss asks for … is judged against his trading without it"; the mission, "measure, then build"; the first priority, "is the number real"; hard rules 2 (NUMBER), 5, 10, 12, 13, 14 (P-START, the stop K-37, the restart policy) and 15 (§9). **Contract:** §1 steps 1 to 4 (`fingerprint`), §4.1 (the order of the branch and the report), §4.2 (V12) and §8 (the report's order). **Other artifacts:** `CryptoTZ/TZ-36-advisor-trust-block.md`, whose §0.1 script, bands, B-KILL, K-36 and gates this TZ adapts — the changes are the file names, the bot's hash `e65de91c…` as the file replaced, the two files instead of three, six texts of G-RENDER instead of ten, and no history run — and its report; `CryptoTZ/TZ-35-advisor-bot.md`; TZ-35's checker's `scratch` and `reclaim`. **The Boss's text** (`TЗ-37 — Trigger Commands and Intelligent Capital Allocation`, 2026-10-31): each quotation in §0 and §1 was compared with it, character for character. **This TZ:** §0.1 to §0.5, §1, §2's items, §3.1 to §3.6, §4.1 to §4.5, §5, §6 and §9, each supporting the sentence that cites it. **None unresolved.** |

**Six checks could not be performed from this session**, and each is converted into a mechanical condition the Executor evaluates and BLOCKS on (CANON hard rule 13): the host's
own state — free space, memory, units, interpreter, the service copy's hashes and the Boss's token — `I host`, §0.3; the live
reach of `fapi.binance.com` and `api.telegram.org` under the service's headers — `fapi.binance.com` and `api.binance.com` answer `451` to this session's
container, `data-api.binance.vision` `200` — P-START and G-RENDER, before anything is signalled; the allocation on a live day with qualifying STRONG trades, which this session could not run for the same reason and which depends on the market of the day
— whenever the live report holds one, G-RENDER recomputes its plan and reads the limits on it, and a violation is B-ROLLBACK; when it holds none, G-RENDER prints zero placed and reads 16 of 16 on the routing, the empty reply and the journal, and the sizes rest on the self-test's cases and the stand-in render, run on the very bytes COPY compares;
systemd's restart of the unit after a `SIGTERM` and its journal — UNIT-NEW; NUMBER on `main` with this file uploaded — `I number` on the clone at `a5c66a1`, which holds no `TZ-37-` file, reads `FAIL - 1
of 2` by design, and the stand-ins read `PASS - 2 of 2` and `FAIL` with a second file and with a report; and TZ-35's `scratch` and `reclaim`
against the host's real `/tmp`. **Two things are read and not measured, and nothing blocks on them:** the quote-volume field, index 7 of Binance's kline row (the documented layout, shared with the archive's daily files),
which `liquidity` reads — a wrong field would move a cap that only ever lowers a position, and no risk limit rests on it; and Telegram's rendering of the two messages, which is the Boss's next «сигнал 10000 топ 3». **Everything else above
was performed here** under Python 3.13.18: the three self-tests, `44`, `67` and `50` of their own; §0.1's script run against this file — two files, over an empty stage and over a worktree of the clone at `a5c66a1`, its numstat exact and its refusal over a stage or a worktree whose bot is not TZ-35's by hash; the checker's `fingerprint` and `rule` against the repository, `65 of 65` with the map in place and `7 of 7`; its `host`, `mark`, `unit`, `copy`, `keep`, `stopped`, `number` and `render` against stand-ins for systemd, `/proc` and
the host's files and against the real bot on synthetic market data, thirty-six assertions, a negative control for each reading that can fail; the table of the map, the constants, the arithmetic and the history figures independently of the checker; and a lint of the two files, clean under `-W error`, no unused import.

---

## Appendix A — the two files, byte for byte

Extracted by §0.1's script; each block's content is its file.

```text file=advisor/adv3-bot.py
#!/usr/bin/env python3
# adv3-bot.py - ADV-3's Telegram side (CANON PART VII): the Boss's commands, the daily message at 06:00 UTC
# (10:00 in Batumi), and a journal of every message sent. Standard library only; adv3.py lies beside it.
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
DAILY = dt.time(6, 0)
POLL, RETRY, LIMIT = 50, 300, 4000
OPEN = ('сигнал', 'сигналы', 'signal', 'signals', 'топ', 'top', 'стратегия', 'стратегию', 'strategy')
HEAD = re.compile(r'^\s*/?([^\W\d_]+)')
TOPN = re.compile(r'(?:топ|top)[\s\-\u2013]*(\d{1,2})(?!\d)', re.I)
# TZ-37's allocation view: the stop's limit in percent of the entry, the smallest position, the share of a coin's mean
# daily quote volume a position may take, the discount for same-way correlation, the strength's cap, the days of volume.
STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, CROWD, Z_CAP, LIQ_DAYS = 11.1, 5.0, 0.001, 0.5, 3.0, 7
HELP = ('<b>ADV-3 · сигналы Binance Futures</b>\n'
        '«сигнал» — сигналы сейчас: ТОП-3 правила, депозит 10 000 USDT и риск 0,5% на сделку — пример размера.\n'
        '«сигнал 10000 топ 3» — распределить 10 000 USDT между сильнейшими сделками: только STRONG, стоп не дальше 11,1% '
        'цены входа; подошло две — покажу две, ни одной — скажу, что нет. STRONG бывает только в ТОП-3, больше трёх не будет.\n'
        '«сигнал 15000 топ 5» — то же на 15 000 USDT; «сигнал 10000» — то же, до трёх сделок.\n'
        'Риск на сделку — 0,5% бюджета, не больше 1%: «сигнал 10000 топ 3 1». Чего нельзя разместить без превышения риска, '
        'остаётся свободным — ответ скажет, сколько.\n'
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
    """('signal', None, None, risk) for «сигнал [risk]», the TOP-3 message; ('alloc', budget, n, risk) where a budget of
    100 or more is given - «сигнал 10000 топ 3», «сигнал 15000 топ 5», «сигнал 10000» (n = 3), «топ 3 на 10000» - the
    allocation view; None where the text is neither. n is read after «топ» or «top» (1 to 10); risk is the percent of
    the budget a trade may lose at its stop (default 0.5, at most 1)."""
    text = text or ''
    m = HEAD.match(text)
    if not m or m.group(1).lower() not in OPEN:
        return None
    s = re.sub(r'@\w+', ' ', text)
    top = TOPN.search(s)
    if top:
        s = s[:top.start()] + ' ' + s[top.end():]
    budget, risk = numbers(s)
    if budget is None:
        return ('signal', None, None, risk)
    return ('alloc', budget, min(max(int(top.group(1)), 1), 10) if top else adv3.TOP_N, risk)


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


def plan_parts(rep, p):
    """The allocation view as two messages: the trades with their figures, then the six ratings."""
    last = dt.date.fromisoformat(rep['close_of'])
    usdt, pct, num, price = adv3.usdt, adv3.pct, adv3.num, adv3.price
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
        cd = it['card']
        side, dot = ('LONG', '🟢') if cd['side'] > 0 else ('SHORT', '🔴')
        lo, hi = cd['zone']
        ref = cd['entry']
        mfe = adv3.FACTS['strong'].get('mfe') if adv3.FACTS['strong'].get('gate_S') == 'NOT DISQUALIFIED' else adv3.FACTS['base'].get('mfe')
        lines += ['', f"{it['rank']}) {dot} <b>{cd['coin']} · {side}</b> · ★ STRONG",
                  f"Качество: z {adv3.signed(cd['z'])} · сумма знаков {adv3.signed(cd['sum'], 0)} из ±4 · доля {pct(100 * it['share'], 0)}%"
                  + (f" · корреляция с остальными {adv3.signed(it['crowd'])}" if p['k'] > 1 else ''),
                  (f"Вход: <b>по рынку</b> ≈ {price(ref)}, зона {price(lo)}–{price(hi)}" if cd['mode'] == 'market'
                   else f"Вход: <b>лимит {price(ref)}</b> — ждать отката, цена {price(cd['mark'])} ушла от зоны"),
                  f"⛔ Стоп: <b>{price(cd['stop'])}</b> ({'−' if cd['side'] > 0 else '+'}{pct(cd['stop_pct'])}%)"]
        for number, t in zip((1, 2, 3), cd['targets']):
            lines.append(f"🎯 {price(t)} ({'+' if (t - ref) > 0 else ''}{pct(100 * (t - ref) / ref)}%)" + (f" · дошли {pct(100 * mfe[number], 0)}%" if mfe else ''))
        lines += [f"Капитал: <b>{usdt(it['notional'])} USDT</b>{' (ограничен ликвидностью)' if it['capped'] else ''} · плечо {it['leverage']}× изол. · маржа {usdt(it['margin'])} USDT",
                  f"Потеря на стопе: {usdt(it['loss'])} USDT с комиссиями",
                  f"Инвалидация: {'цена ≤' if cd['side'] > 0 else 'цена ≥'} {price(cd['stop'])} или закрытие дня с суммой знаков "
                  f"{'ниже +2' if cd['side'] > 0 else 'выше −2'}"]
    if p['rejected']:
        lines += ['', 'Отклонены: ' + '; '.join(f'{c} {s} — {why}' for c, s, why in p['rejected'])]
    if p['plain']:
        lines.append('В ТОП-3 без STRONG — не берутся: ' + ', '.join(p['plain']))
    if p['n'] > adv3.TOP_N:
        lines.append(f'STRONG бывает только в ТОП-3: больше {adv3.TOP_N} сделок не будет')
    own = dict(rep, cards=[it['card'] for it in p['items']])
    for it in p['items']:
        it['card']['rank'] = it['rank']
    own['trust'] = adv3.trust(own)
    second = adv3.trust_lines(own, adv3.FACTS) + ['', 'Размеры — формула ТЗ-37 (сила тренда, поправка на корреляцию, ликвидность, лимиты риска), не доказанная: форвард-запись '
                                                  'проверяет правило, а не этот отбор и не эти размеры.',
              '<i>Не инвестиционный совет: правило показывает состояние рынка; решение и риск — ваши.</i>']
    return ['\n'.join(lines), '\n'.join(second)]


def journal(kind, rep, ids, extra=None):
    rec = {'utc': dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds'), 'kind': kind, 'rule': rep['rule'],
           'close_of': rep['close_of'], 'deposit': rep['deposit'], 'risk_pct': rep['risk_pct'], 'top': rep['top'],
           'strong': rep['strong'], 'message_ids': ids,
           'signals': {k: v.get('signal') for k, v in rep['rows'].items()},
           'cards': [{k: cd[k] for k in ('coin', 'side', 'strong', 'mode', 'entry', 'stop', 'targets', 'close', 'U')}
                     for cd in rep['cards']]}
    rec.update(extra or {})
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
    cmd = route(text)
    try:
        if cmd:
            kind, budget, n, risk = cmd
            rep, msg = make(data, budget or adv3.DEPOSIT, risk)
            extra, parts = None, [msg]
            if kind == 'alloc':
                p = plan(rep, data.cs, budget, n, risk, {c: liquidity(c, rep['made_at_ms']) for c in rep['strong']})
                parts = plan_parts(rep, p)
                extra = {'alloc': {'budget': budget, 'n': n, 'risk': risk, 'allocated': p['allocated'], 'free': p['free'], 'loss': p['loss'],
                                   'items': [{'coin': it['card']['coin'], 'side': it['card']['side'], 'notional': it['notional'],
                                              'leverage': it['leverage'], 'margin': it['margin'], 'loss': it['loss']} for it in p['items']],
                                   'rejected': p['rejected']}}
            ids = [i for part in parts for i in tg.send(part)]
            try:
                journal(kind if kind == 'alloc' else 'request', rep, ids, extra)
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
    """The bot's own checks, offline: the commands, the allocation (golden cases computed by hand, the limits over random
    scenarios), the replies, the chunks, the files, the log, the HTML fallback, glibc."""
    import contextlib, io, random, shutil, tempfile
    done = []

    def check(name, ok):
        done.append(name)
        assert ok, name

    D, R, RM = adv3.DEPOSIT, adv3.RISK, adv3.RISK_MAX
    for text, want in (('сигнал', ('signal', None, None, R)), ('Сигнал 0,5%', ('signal', None, None, 0.5)),
                       ('signal 0.3', ('signal', None, None, 0.3)), ('сигналы', ('signal', None, None, R)),
                       ('сигнал топ 3', ('signal', None, None, R)), ('сигнал 99', ('signal', None, None, RM)),
                       ('сигнал 10000 топ 3', ('alloc', 10000.0, 3, R)), ('сигнал 15000 топ 5', ('alloc', 15000.0, 5, R)),
                       ('сигнал 10000', ('alloc', 10000.0, 3, R)), ('Сигнал 15 000 топ 5 1', ('alloc', 15000.0, 5, 1.0)),
                       ('/signal@adv3_bot 5000 top 2', ('alloc', 5000.0, 2, R)), ('signal 5000 top2', ('alloc', 5000.0, 2, R)),
                       ('топ 3 на 10000', ('alloc', 10000.0, 3, R)), ('топ3 10000', ('alloc', 10000.0, 3, R)),
                       ('сигнал 10к топ 3', ('alloc', 10000.0, 3, R)), ('signal 15k top 5', ('alloc', 15000.0, 5, R)),
                       ('сигнал 1,5 тыс', ('alloc', 1500.0, 3, R)), ('сигнал 10 коинов', ('signal', None, None, RM)),
                       ('сигнал 10000 топ-3', ('alloc', 10000.0, 3, R)), ('сигнал 10000 топ 3 0,3', ('alloc', 10000.0, 3, 0.3)),
                       ('стратегия 7000 топ 2', ('alloc', 7000.0, 2, R)), ('сигнал 20000 топ 3 3', ('alloc', 20000.0, 3, RM)),
                       ('сигнал 12000 0.01', ('alloc', 12000.0, 3, 0.05)), ('сигнал 10000 usdt топ 1', ('alloc', 10000.0, 1, R)),
                       ('сигнал 10000 топ 0', ('alloc', 10000.0, 1, R)), ('сигнал 10000 топ 50', ('alloc', 10000.0, 10, R)),
                       ('signal 200000000', ('alloc', 10_000_000.0, 3, R)), ('сигнал 100 топ 3', ('alloc', 100.0, 3, R)),
                       ('привет', None), ('сигнализация', None), ('', None), ('12345', None), ('все', None), ('eth', None)):
        check(f'route {text!r}', route(text) == want)
    check('HELP names the commands, the filter, the cap of three and the defaults, in one Telegram part',
          all(k in HELP for k in ('«сигнал»', '«сигнал 10000 топ 3»', '«сигнал 15000 топ 5»', '«сигнал 10000»', '11,1%', 'STRONG',
                                  'не больше 1%', '10:00')) and len(chunks(HELP)) == 1)
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
            if params.get('parse_mode') == 'HTML' and '<b>bad' in params.get('text', ''):
                raise RuntimeError("telegram sendMessage: 400 Bad Request: can't parse entities")
            return {'message_id': len(self.calls)}

    fk = Fake()
    check('HTML sent as HTML', fk.send('<b>ok</b>') == [1] and fk.calls[0]['parse_mode'] == 'HTML')
    check('unparseable HTML resent as plain text', fk.send('<b>bad &amp; x</b>') == [3]
          and 'parse_mode' not in fk.calls[2] and fk.calls[2]['text'] == 'bad & x')
    SECRETS.append('123456:SECRET')
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
    last = max(cs['BTC'])
    marks = {c + 'USDT': (cs[c][last][3], 0.0001) for c in cs}
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

    A = [0.01 * (-1) ** k for k in range(60)]                       # alternating
    Bs = [0.01 * (1, 1, -1, -1)[k % 4] for k in range(60)]          # orthogonal to A over 56 days, both of mean zero
    Cs = [0.01 * (1, -1, -1, 1)[k % 4] for k in range(60)]          # orthogonal to A and to Bs
    Ds = [-x for x in A]

    def scenario(spec, marks_ok=True, rets=None):
        """A report whose rows are spec = [(coin, side, z, stop percent, strong)] in rank order, entry = close = 100, so the stop is at
        stop percent of the entry; and candles for the coins from rets."""
        rows = dict(base['rows'])
        for coin, side, z, stop, strong in spec:
            rows[coin] = {'signal': side, 'z': z, 'sum': 4 * side, 'U': stop, 'close': 100.0, 'prev': side, 'since': str(last),
                          'stop': 100.0 - side * stop, 'mark': 100.0, 'funding': 0.0001, 'funding_h': 8}
        r = dict(base, rows=rows, top=[c for c, *_ in spec], strong=[c for c, *_, st in spec if st], marks_ok=marks_ok, cards=[])
        return r, {c: series((rets or {}).get(c, A)) for c, *_ in spec}

    def pl(spec, budget=10000.0, n=3, risk=0.5, liq=None, rets=None, marks_ok=True):
        r, c = scenario(spec, marks_ok, rets)
        return r, plan(r, c, budget, n, risk, liq or {})

    # G1: one STRONG trade, stop 8 %, 10,000 USDT, 0,5 %: 50 USDT of loss over 0.082 -> 609 USDT; leverage 7; margin 87; loss 50
    r1, p1 = pl([('ETH', 1, 2.0, 8.0, True)])
    it = p1['items'][0]
    check('golden 1: one trade at an 8 % stop and 0,5 % risk is 609 USDT, leverage 7, margin 87, loss 50',
          (it['notional'], it['leverage'], it['margin'], it['loss']) == (609, 7, 87, 50) and p1['allocated'] == 609 and p1['free'] == 9391
          and p1['margin'] == 87 and p1['loss'] == 50 and p1['k'] == 1)
    # G2: two uncorrelated trades, z 2 and 1, stops 8 % and 10 %: losses 66.67 and 33.33 -> 813 and 326
    r2, p2 = pl([('ETH', 1, 2.0, 8.0, True), ('SOL', 1, 1.0, 10.0, True)], rets={'ETH': A, 'SOL': Bs})
    a, b = p2['items']
    check('golden 2: two uncorrelated trades of strength 2 and 1 take two thirds and one third of the risk: 813 and 326 USDT',
          (a['notional'], b['notional']) == (813, 326) and (a['leverage'], b['leverage']) == (7, 6) and (a['margin'], b['margin']) == (117, 55)
          and (a['loss'], b['loss']) == (67, 34) and p2['allocated'] == 1139 and p2['loss'] == 101 and a['rank'] == 1 and b['rank'] == 2)
    # G3: A and B the same series, C orthogonal: the pair is discounted, C takes 0.4 of the risk -> 45, 45, 60 USDT of loss
    r3, p3 = pl([('ETH', 1, 2.0, 8.0, True), ('SOL', 1, 2.0, 8.0, True), ('XRP', 1, 2.0, 8.0, True)], rets={'ETH': A, 'SOL': A, 'XRP': Bs})
    check('golden 3: a correlated pair is discounted and the independent trade takes more: shares 0.3, 0.3, 0.4; 548, 548 and 731 USDT',
          [round(x['share'], 6) for x in p3['items']] == [0.3, 0.3, 0.4] and [x['notional'] for x in p3['items']] == [548, 548, 731]
          and [round(x['risk_pct'], 6) for x in p3['items']] == [0.45, 0.45, 0.6])
    # G4: a LONG and a SHORT on the same series hedge each other: no discount
    r4, p4 = pl([('ETH', 1, 2.0, 8.0, True), ('SOL', -1, 2.0, 8.0, True)], rets={'ETH': A, 'SOL': A})
    check('golden 4: opposite sides on one series are no crowding: equal shares, 0.5 % each', [x['crowd'] for x in p4['items']] == [0.0, 0.0]
          and [round(x['share'], 6) for x in p4['items']] == [0.5, 0.5] and [x['notional'] for x in p4['items']] == [609, 609])
    r5, p5 = pl([('ETH', 1, 2.0, 8.0, True), ('SOL', 1, 2.0, 8.0, True)], rets={'ETH': A, 'SOL': A})
    check('golden 5: two longs on one series are discounted alike, so their shares stay equal', [round(x['crowd'], 6) for x in p5['items']] == [1.0, 1.0]
          and [round(x['share'], 6) for x in p5['items']] == [0.5, 0.5])
    # selection
    sel = [('ETH', 1, 3.0, 8.0, True), ('SOL', -1, 2.5, 13.0, True), ('XRP', 1, 2.0, 10.0, True), ('BTC', 1, 1.5, 6.0, False)]
    r6, p6 = pl(sel[:3] + [('BTC', 1, 1.5, 6.0, False)], rets={'ETH': A, 'SOL': Bs, 'XRP': Cs, 'BTC': Ds})
    check('selection: STRONG only, a stop beyond 11.1 % rejected with its reason, a weaker setup never fills a place',
          [x['card']['coin'] for x in p6['items']] == ['ETH', 'XRP'] and p6['rejected'] == [('SOL', 'SHORT', 'стоп 13,0% дальше 11,1%')]
          and p6['plain'] == ['BTC'] and p6['k'] == 2)
    r7, p7 = pl(sel[:3], n=1, rets={'ETH': A, 'SOL': Bs, 'XRP': Cs})
    check('selection: only n are taken, the rest named', [x['card']['coin'] for x in p7['items']] == ['ETH']
          and ('XRP', 'LONG', 'сверх запрошенных 1') in p7['rejected'])
    r8, p8 = pl([('SOL', -1, 2.5, 13.0, True)], rets={'SOL': A})
    check('selection: no qualifying trade is no allocation, the whole budget free', p8['items'] == [] and p8['free'] == 10000.0 and p8['allocated'] == 0 and p8['loss'] == 0)
    r9, p9 = pl([('ETH', 1, 2.0, 8.0, True)], marks_ok=False)
    check('selection: without current prices nothing is placed', p9['items'] == [] and p9['rejected'] == [('ETH', 'LONG', 'нет текущей цены Binance')])
    rA, cA = scenario([('ETH', 1, 2.0, 8.0, True)])
    rA['rows']['ETH'] = dict(rA['rows']['ETH'], mark=100.0 - 8.0 + 1.0)
    pA = plan(rA, cA, 10000.0, 3, 0.5, {})
    check('selection: a price at the stop gives no entry and no position', pA['items'] == [] and pA['rejected'][0][2] == 'цена у стопа, входа нет')
    r10, p10 = pl([('ETH', 1, 2.0, 8.0, True)], liq={'ETH': 200_000.0})
    check('liquidity: a position takes at most 0.1 % of the coin\'s mean daily volume, and says so',
          p10['items'][0]['notional'] == 200 and p10['items'][0]['capped'] is True and p1['items'][0]['capped'] is False)
    r11, p11 = pl([('ETH', 1, 2.0, 0.5, True), ('SOL', 1, 2.0, 0.5, True), ('XRP', 1, 2.0, 0.5, True)], budget=1000.0, rets={'ETH': A, 'SOL': Bs, 'XRP': Cs})
    check('budget: positions that would exceed the budget are scaled to it, risk only falling', sum(x['notional'] for x in p11['items']) <= 1000
          and all(x['loss_exact'] <= 1000 * 0.01 for x in p11['items']))
    r12, p12 = pl([('ETH', 1, 2.0, 8.0, True)], budget=50.0)
    check('minimum: a position under 5 USDT is dropped with its reason', p12['items'] == [] and p12['rejected'] == [('ETH', 'LONG', 'позиция меньше 5 USDT')])
    # the limits over random scenarios
    rnd, bad = random.Random(37), []
    for trial in range(400):
        k = rnd.randint(1, 3)
        spec = [(adv3.COINS[m + 6], rnd.choice((1, -1)), rnd.uniform(1.0, 6.0), rnd.uniform(0.3, 14.0), rnd.random() < 0.85) for m in range(k)]
        rets = {c: [rnd.gauss(0, 0.03) if rnd.random() < 0.8 else x for x in A] for c, *_ in spec}
        budget, risk, n = rnd.choice((100.0, 777.0, 10000.0, 250000.0, 3e6)), rnd.choice((0.05, 0.3, 0.5, 1.0)), rnd.randint(1, 6)
        liq = {c: rnd.choice((None, 5e4, 1e6, 1e9)) for c, *_ in spec}
        r, pp = pl(spec, budget, n, risk, liq, rets)
        elig = [c for c, side, z, stop, st in spec if st and stop <= STOP_MAX]
        got = [x['card']['coin'] for x in pp['items']]
        ok = (len(got) <= min(n, len(elig)) and set(got) <= set(elig) and all(float(x['notional']).is_integer() and MIN_NOTIONAL <= x['notional'] <= budget for x in pp['items'])
              and all(x['loss_exact'] <= budget * adv3.RISK_MAX / 100 + 1e-9 for x in pp['items'])
              and pp['loss_exact'] <= budget * adv3.RISK_ALL / 100 + 1e-9 and pp['allocated'] <= budget and pp['free'] == budget - pp['allocated']
              and all(x['margin'] * x['leverage'] >= x['notional'] and 1 <= x['leverage'] <= 20 for x in pp['items'])
              and all(x['loss'] >= x['loss_exact'] - 1e-9 for x in pp['items'])
              and all((not x['capped']) or x['notional'] <= LIQ_FRAC * liq[x['card']['coin']] for x in pp['items'])
              and all(x['card']['stop_pct'] <= STOP_MAX and x['card']['entry'] is not None for x in pp['items'])
              and pp['allocated'] == sum(x['notional'] for x in pp['items']) and pp['loss'] == sum(x['loss'] for x in pp['items']))
        if not ok:
            bad.append(trial)
    check('limits over 400 random scenarios: STRONG only and within n, each loss at the stop within 1 % of the budget, all within 5 %, '
          'positions whole and within the budget, margin covers the leverage, the liquidity cap held', not bad)
    fr, stage = scenario([('ETH', 1, 3.0, 8.0, True), ('XRP', 1, 2.0, 10.0, True), ('SOL', -1, 2.5, 13.0, True), ('BTC', 1, 1.5, 6.0, False)],
                         rets={'ETH': A, 'XRP': Cs, 'SOL': Bs, 'BTC': Ds})
    pf = plan(fr, stage, 10000.0, 3, 0.5, {})
    first, second = plan_parts(fr, pf)
    check('plan_parts: the Boss\'s fields - budget, qualifying count and ranking, direction, quality, entry, stop, targets, capital, leverage, margin, loss, unallocated',
          all(k in first for k in ('Бюджет 10 000 USDT', 'Подходящих сделок: 2 из 3 запрошенных', '1) 🟢 <b>ETH · LONG</b> · ★ STRONG', '2) 🟢 <b>XRP · LONG</b>', 'Качество: z', 'Вход:',
                                   '⛔ Стоп:', '🎯', 'Капитал:', 'плечо', 'маржа', 'Потеря на стопе:', 'Свободно', 'Размещено', 'Инвалидация:')))
    check('plan_parts: the rejected and the weaker named, the ratings, the note that the sizes are unproven and the disclaimer in the second message',
          'Отклонены: SOL SHORT — стоп 13,0% дальше 11,1%' in first and 'В ТОП-3 без STRONG — не берутся: BTC' in first
          and 'Оценка доверия' in second and 'ETH 1/5 · XRP 1/5' in second and 'не доказанная' in second and second.rstrip().endswith('решение и риск — ваши.</i>'))
    check('plan_parts: each message is one Telegram part and the markup balances', len(chunks(first)) == 1 and len(chunks(second)) == 1
          and all(t.count('<b>') == t.count('</b>') and t.count('<i>') == t.count('</i>') for t in (first, second)))
    empty = plan_parts(r8, p8)
    check('plan_parts: no qualifying trade says so, with the whole budget free and the ratings', 'Подходящих сделок нет' in empty[0] and 'Размещено 0 USDT · свободно 10 000 USDT' in empty[0]
          and 'сделок нет' in empty[1])
    check('plan_parts: five requested says that STRONG is at most three', 'больше 3 сделок не будет' in plan_parts(*(lambda r, c: (r, plan(r, c, 15000.0, 5, 0.5, {})))(*scenario([('ETH', 1, 3.0, 8.0, True)])))[0])

    class Cap(Telegram):
        def __init__(self, down=False):
            super().__init__('123456:SECRET', 777)
            self.texts, self.down = [], down

        def call(self, method, http_timeout=30, **params):
            if self.down:
                raise RuntimeError('telegram sendMessage: 502 Bad Gateway')
            self.texts.append(params['text'])
            return {'message_id': len(self.texts)}

    class Stub:
        pass

    stub = Stub()
    stub.cs = stage

    def fake_make(data, deposit, risk):
        return fr, 'PLAIN MESSAGE'

    def no_binance(data, deposit, risk):
        raise RuntimeError('fapi.binance.com served no candles')

    state = tempfile.mkdtemp(prefix='.selftest-', dir=os.path.dirname(os.path.abspath(__file__)))
    saved = (globals()['make'], globals()['STATE'], globals()['liquidity'])
    globals()['make'], globals()['STATE'], globals()['liquidity'] = fake_make, state, lambda coin, now_ms: 1e9
    try:
        cap = Cap()
        with contextlib.redirect_stdout(io.StringIO()):
            handle(cap, stub, 'сигнал 10000 топ 3')
            n1 = len(cap.texts)
            handle(cap, stub, 'сигнал')
            n2 = len(cap.texts)
            handle(cap, stub, 'сигнал 10000')
            n3 = len(cap.texts)
            handle(cap, stub, 'привет')
            records = [json.loads(line) for line in open(os.path.join(state, 'journal.jsonl'), encoding='utf-8')]
            globals()['make'] = no_binance
            handle(cap, stub, 'сигнал 10000 топ 3')
            handle(Cap(down=True), stub, 'сигнал')
        check('handle: «сигнал 10000 топ 3» answers with the allocation in two messages', n1 == 2 and 'распределение капитала' in cap.texts[0] and 'Оценка доверия' in cap.texts[1])
        check('handle: «сигнал» answers with the plain message and «сигнал 10000» as «сигнал 10000 топ 3»', cap.texts[n1] == 'PLAIN MESSAGE'
              and n3 - n2 == 2 and cap.texts[n2] == cap.texts[0])
        check('handle: an unknown text gets HELP and no record', cap.texts[n3] == HELP and len(records) == 3)
        check('handle: the journal holds an allocation record with its figures and a plain request record, each of its kind',
              [r['kind'] for r in records] == ['alloc', 'request', 'alloc'] and records[0]['alloc']['allocated'] == pf['allocated']
              and records[0]['alloc']['items'][0]['coin'] == 'ETH' and records[0]['alloc']['budget'] == 10000.0 and 'alloc' not in records[1])
        check('handle: Binance down gets the apology, Telegram down raises nothing', cap.texts[-1].startswith('Binance или Telegram не ответили'))
    finally:
        globals()['make'], globals()['STATE'], globals()['liquidity'] = saved
        shutil.rmtree(state)
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

```text file=research/tz37-capital-allocation.py
#!/usr/bin/env python3
# tz37-capital-allocation.py - TZ-37's checker: the fingerprint, the host gate, the number, G-RULE, COPY, G-RENDER, the
# readings after the unit's restart, and the marks. Standard library only. It starts and stops no
# unit, signals no process and sends no request of its own (G-RENDER runs the service copy's bot, which reads
# Binance's public market), and it never reads or prints the bot's token or the pinned chat. Exits: 0 every assert
# held; 1 a failed assert, named; 3 NOT YET.
import ast, calendar, contextlib, hashlib, importlib.util, io, json, math, os, re, shutil, subprocess, sys, time

WORK = '/root/tz37-work'
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
TZ_FILE = 'CryptoTZ/TZ-37-capital-allocation.md'
NUMBER = 'TZ-37-'
BRANCH = 'tz-37-capital-allocation'
MAP_REV = '2026-10-31-a'
ANCHORS = {'A1': '229a944f2d51', 'A2': '6c5089330629',
           'A3': '0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable',
           'A4': '437b45ea196b', 'A5': '0f6c90451cbd', 'A6': '729f0bcdbee3'}
DERIVED = {'A2': 'research/twap-divergence.py', 'A4': 'BTC-EXECUTOR-INSTRUCTIONS.md',
           'A5': 'research/recorder/recorder.py', 'A6': 'research/pfair.py'}
H = {'adv3': 'd73a657ef31decad276b858c4ec9672dce1c1c5cec36f0bb1c5b3378838224a8',
     'selftest': 'ef4ffc44e6f8bcdd5685fc1db9090957890c6e2ab762cdad8ae9826b18cf1395',
     'bot_old': 'e65de91c7b49c6f932db91e568a5956c005e63119c1cf6fb8724ffb0438d1dcb',
     'bot_new': '3a044d50f51b16563b99bf1514ef92f35a9795b1fcc377aea6be4c23a31f7af2',
     'rule': 'ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169',
     'unit': '82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66'}
BOT_CHANGED = {'selftest', 'handle', 'journal'}
BOT_ADDED = {'plan_parts', 'correlation', 'numbers', 'returns_of', 'liquidity', 'plan', 'route'}
BOT_REMOVED = {'parse'}
BOT_SAME = ('Data', 'Telegram', 'chunks', 'find_chat', 'hello', 'log', 'main', 'make', 'malloc_tune', 'probe', 'put', 'read', 'serve')
BOT_CONST = ({'HELP'}, {'HEAD', '(STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, CROWD, Z_CAP, LIQ_DAYS)', 'TOPN', 'OPEN'}, {'CMD'})
STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, RISK_MAX, RISK_ALL = 11.1, 5.0, 0.001, 1.0, 5.0
MEM_FLOOR, DISK_FLOOR = 130_981_888, 7_400_000_000
ROWS, FROZEN = 56, 53
RENDER_CASES = ('сигнал', 'сигнал 10000 топ 3', 'сигнал 15000 топ 5', 'сигнал 10000', 'помощь', 'привет')
RENDER_KINDS = ['request', 'alloc', 'alloc', 'alloc']
TRUST = ('Оценка доверия', 'Надёжность системы: <b>1/5</b>', 'Уверенность в сделках:', 'STRONG обоснован: <b>нет</b>',
         'Качество данных: <b>низкое</b>', 'Ожидаемая R на сделку: <b>не установлена</b>', 'Инвалидация: у каждой карточки')
BOOK = ('Форвард с 28.10', 'Все сигналы: входов', 'STRONG: входов')
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


def sh_try(args, **kw):
    """sh, where a command the host lacks is a reading of its own and not a crash: (127, '', why)."""
    try:
        return sh(args, **kw)
    except OSError as e:
        return 127, '', repr(e)


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
    stat_text = read('/proc/%s/stat' % pid)
    fields = stat_text[stat_text.rindex(')') + 2:].split()
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
    """{name: ast.dump} of a module's functions and classes, and of its assignments keyed by their targets."""
    defs, asg = {}, {}
    for n in ast.parse(src).body:
        if isinstance(n, (ast.FunctionDef, ast.ClassDef)):
            defs[n.name] = ast.dump(n)
        elif isinstance(n, ast.Assign):
            asg[','.join(ast.unparse(t) for t in n.targets)] = ast.dump(n)
    return defs, asg


def bot_checks(old_src, new_src):
    """G-RULE's last three checks: the two adv3-bot.py files differ in exactly the definitions and constants TZ-37 names."""
    (od, oa), (nd, na) = top_level(old_src), top_level(new_src)
    changed = {k for k in od if k in nd and od[k] != nd[k]}
    return {
        'the functions and classes that changed are exactly %s' % sorted(BOT_CHANGED): changed == BOT_CHANGED,
        'the added are exactly %s and the removed are %s' % (sorted(BOT_ADDED), sorted(BOT_REMOVED)):
            set(nd) - set(od) == BOT_ADDED and set(od) - set(nd) == BOT_REMOVED,
        'the %d others are identical by AST and the constants differ as named' % len(BOT_SAME):
            all(k in od and k in nd and od[k] == nd[k] for k in BOT_SAME)
            and ({k for k in oa if k in na and oa[k] != na[k]}, set(na) - set(oa), set(oa) - set(na)) == BOT_CONST,
    }


def html_balanced(text):
    return all(text.count('<%s>' % t) == text.count('</%s>' % t) for t in ('b', 'i'))


def plan_invariants(p, rep, liq, budget, n):
    """The allocation's limits, read from a plan (the bot's own) and the report and liquidity it was made from. The limits
    are this checker's, the TZ's: stop 11.1 %, minimum 5 USDT, liquidity 0.1 %, risk 1 % a trade and 5 % in all, three places."""
    items = p['items']
    coins = [it['card']['coin'] for it in items]
    strong = [c for c in rep['top'] if c in rep['strong']]
    named = [r[0] for r in p['rejected']]
    return {
        'only STRONG coins of the report, in rank order, at most n and at most three, none added to fill': (
            set(coins) <= set(strong) and coins == [c for c in strong if c in coins] and len(coins) <= min(n, 3)),
        'every STRONG coin is in the plan or named with a reason, once': sorted(coins + named) == sorted(strong),
        'every position has an entry and a stop within 11.1 % of it, on current prices': (
            all(it['card']['entry'] is not None and it['card']['stop_pct'] <= STOP_MAX for it in items)
            and (rep['marks_ok'] or not items)),
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


def render_checks(texts, calc, plain, kinds, records, log, same, expect):
    """G-RENDER: what the service copy's bot sent for each command (texts, by command), the plan the checker recomputed from
    the report and liquidity each allocation reply was made from (calc, by command), the plain report, the scratch journal's kinds and
    records, the bot's log, whether the bot's own record is as before, and what the bot module holds (expect); counts and labels only."""
    sig, hlp, hi = texts[RENDER_CASES[0]], texts[RENDER_CASES[4]], texts[RENDER_CASES[5]]
    whole = lambda parts: '\n'.join(parts)
    allocs = [c for c in RENDER_CASES if c in calc]
    usdt = expect['usdt']
    inv = {c: plan_invariants(calc[c]['plan'], calc[c]['rep'], calc[c]['liq'], calc[c]['budget'], calc[c]['n']) for c in allocs}

    def fields(c):
        p, t = calc[c]['plan'], whole(texts[c])
        head = ('не доказанная' in t and 'Бюджет %s USDT' % expect['num'](p['budget'], 6) in t and 'Размещено %s USDT' % usdt(p['allocated']) in t
                and ('Свободно %s USDT' % usdt(p['free']) in t or 'свободно %s USDT' % usdt(p['free']) in t))
        if not p['items']:
            return head and 'Подходящих сделок нет' in t
        k = len(p['items'])
        return (head and 'Подходящих сделок: %d из %d запрошенных' % (k, p['n']) in t
                and all(t.count(m) == k for m in ('Капитал:', 'плечо', 'Потеря на стопе:', '⛔ Стоп:', 'Инвалидация: цена', 'Качество: z')) and t.count('маржа') == k + 1
                and t.count('🎯') == 3 * k and 'Потеря на стопах %s USDT' % usdt(p['loss']) in t and 'маржа %s USDT' % usdt(p['margin']) in t)

    n = len(CARD.findall(whole(sig)))
    sixth = RENDER_CASES[3]
    return {
        'every command answered, no traceback and no failed request in the bot\'s log':
            all(texts[k] for k in RENDER_CASES) and 'Traceback' not in log and 'request failed' not in log,
        'the markup is balanced in every message (b, i)': all(html_balanced(t) for ps in texts.values() for t in ps),
        '«сигнал»: the six ratings and the forward book, at most three cards, each with its basis and invalidation, in at most three parts':
            all(k in whole(sig) for k in TRUST + BOOK) and n <= 3 and whole(sig).count('Основание: сумма знаков') == n
            and whole(sig).count('Инвалидация: цена') == n and len(sig) <= 3,
        'the allocation\'s constants are the TZ\'s: 11.1 % a stop, 5 USDT, 0.1 % of the volume, 1 % and 5 % of risk, three places, 0.1 % a side':
            expect['consts'] == (STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, RISK_MAX, RISK_ALL, 3, 0.001),
        'each allocation reply is the bot\'s own plan_parts of the report and liquidity it was made from':
            len(allocs) == 3 and all(texts[c] == calc[c]['parts'] for c in allocs),
        'plan: only STRONG coins of the report, in rank order, at most n and at most three, none added to fill':
            all(v['only STRONG coins of the report, in rank order, at most n and at most three, none added to fill'] for v in inv.values()),
        'plan: every STRONG coin is in the plan or named with a reason, once':
            all(v['every STRONG coin is in the plan or named with a reason, once'] for v in inv.values()),
        'plan: every position has an entry and a stop within 11.1 % of it, on current prices':
            all(v['every position has an entry and a stop within 11.1 % of it, on current prices'] for v in inv.values()),
        'plan: each loss at its stop within 1 % of the budget, all together within 5 %':
            all(v['each loss at its stop within 1 % of the budget, all together within 5 %'] for v in inv.values()),
        'plan: whole positions of at least 5 USDT, together within the budget, free the budget less them':
            all(v['whole positions of at least 5 USDT, together within the budget, free the budget less them'] for v in inv.values()),
        'plan: leverage the rule\'s formula and at most 20, the margin covering the position, a position within its liquidity cap':
            all(v['leverage the rule\'s formula and at most 20, the margin covering the position, a position within its liquidity cap'] for v in inv.values()),
        'the Boss\'s fields are in every allocation reply: budget, qualifying count, allocated, free, and for each trade capital, leverage, margin, loss at the stop, stop, targets, invalidation, and the note that the sizes are unproven':
            len(allocs) == 3 and all(fields(c) for c in allocs),
        '«сигнал 10000» is the three-trade view and «сигнал 15000 топ 5» says that STRONG is at most three':
            len(allocs) == 3 and 'до 3 сделок' in whole(texts[sixth]) and calc[sixth]['n'] == 3 and calc[sixth]['budget'] == 10000.0
            and 'больше 3 сделок не будет' in whole(texts[RENDER_CASES[2]]) and 'Бюджет 15 000 USDT' in whole(texts[RENDER_CASES[2]]),
        '«помощь» and an unknown text answer HELP and nothing else': hlp == [expect['help']] and hi == [expect['help']],
        'the scratch journal holds, in order, request, alloc, alloc, alloc, each allocation record with its plan\'s figures': kinds == RENDER_KINDS and len(allocs) == 3 and all(
            r['alloc']['allocated'] == calc[c]['plan']['allocated'] and r['alloc']['free'] == calc[c]['plan']['free']
            and [i['coin'] for i in r['alloc']['items']] == [it['card']['coin'] for it in calc[c]['plan']['items']]
            for r, c in zip(records[1:], allocs)),
        'the bot\'s own journal and daily-sent are as before the run': same is True,
    }


def unit_checks(which, pre, now):
    """The readings after a restart: now is what the modes read; pre is the snapshot of the mark before the kill."""
    want_bot = H['bot_new'] if which == 'new' else H['bot_old']
    return {
        'the unit is active, running and enabled': (now['bot']['ActiveState'], now['bot']['SubState'],
                                                    now['bot']['UnitFileState']) == ('active', 'running', 'enabled'),
        'a new MainPID, one restart more': int(now['bot']['MainPID']) not in (0, int(pre['bot']['MainPID']))
        and int(now['bot']['NRestarts']) == int(pre['bot']['NRestarts']) + 1,
        'the process started after the kill mark and within 90 s of it': pre['t'] <= now['start'] <= pre['t'] + 90,
        'the process runs the unit\'s exact argv, alone': now['argv'] == ARGV and now['procs'] == [int(now['bot']['MainPID'])],
        'the service copy\'s adv3-bot.py is the %s one, and the process started after the copy' % which:
            now['sha_bot'] == want_bot and now['start'] > now['copy_t'],
        'the service copy\'s adv3.py and the unit file are unchanged': now['sha_adv3'] == H['adv3'] and now['sha_unit'] == H['unit'],
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


def memory_gate(first, second):
    """The memory gate: MemAvailable at the first read, and at the second, 60 s later, taken only where the first fell
    below MEM_FLOOR; the second decides. Returns (passes, the read that decided)."""
    final = first if first >= MEM_FLOOR or second is None else second
    return final >= MEM_FLOOR, final


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


def meminfo():
    return {k: int(v.split()[0]) * 1024 for k, v in (l.split(':', 1) for l in read('/proc/meminfo').splitlines())}


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
    checks['H5 adv3.py is TZ-36\'s and adv3-bot.py is TZ-35\'s'] = (
        sha256_file(SVC + '/adv3.py') == H['adv3'] and sha256_file(SVC + '/adv3-bot.py') == H['bot_old'])
    checks['H5 the installed unit file is TZ-35\'s'] = sha256_file('/etc/systemd/system/adv3-bot.service') == H['unit']
    checks['H5 commit.txt is 40 hex characters and a newline'] = re.fullmatch(r'[0-9a-f]{40}\n', read(SVC + '/commit.txt')) is not None
    checks['H6 the record holds daily-sent and a journal of whole lines'] = (
        re.fullmatch(r'\d{4}-\d{2}-\d{2}\n?', read(BOTDIR + '/daily-sent')) is not None
        and read(BOTDIR + '/journal.jsonl', 'rb').endswith(b'\n'))
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


def git_show(path):
    rc, so, se = sh(['git', '-C', PRIMARY, 'show', 'origin/main:' + path])
    assert rc == 0, se
    return so


def mode_rule():
    same = {}
    for key, path in (('adv3', 'advisor/adv3.py'), ('selftest', 'advisor/selftest-adv3.py'),
                      ('unit', 'deploy/systemd/adv3-bot.service')):
        b = read(WT + '/' + path, 'rb')
        same[key] = b == git_show(path).encode() and sha256_bytes(b) == H[key]
    rule_txt = read(WT + '/advisor/RULE-ADV-3.txt', 'rb')
    checks = {
        'adv3.py is main\'s, byte for byte, and hashes to TZ-36\'s': same['adv3'],
        'selftest-adv3.py is main\'s, byte for byte, and hashes to TZ-36\'s': same['selftest'],
        'RULE-ADV-3.txt is main\'s, hashes to the RULE constant and is adv3.py\'s':
            rule_txt == git_show('advisor/RULE-ADV-3.txt').encode() and sha256_bytes(rule_txt) == H['rule']
            and ("RULE = '%s'" % H['rule']) in read(WT + '/advisor/adv3.py'),
        'the unit file is main\'s, byte for byte, and hashes to TZ-35\'s': same['unit'],
    }
    checks.update(bot_checks(git_show('advisor/adv3-bot.py'), read(WT + '/advisor/adv3-bot.py')))
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
    rc2, up, _ = sh(['git', '-C', WT, 'rev-parse', 'origin/' + BRANCH])
    commit = read(SVC + '/commit.txt')
    verdict('COPY', {
        'the service copy holds adv3.py, adv3-bot.py and commit.txt only': sorted(os.listdir(SVC)) == ['adv3-bot.py', 'adv3.py', 'commit.txt'],
        'adv3.py is unchanged, TZ-36\'s': sha256_file(SVC + '/adv3.py') == H['adv3'],
        'adv3-bot.py is Appendix A\'s': sha256_file(SVC + '/adv3-bot.py') == H['bot_new'],
        'commit.txt is the branch head and the worktree\'s HEAD': (
            re.fullmatch(r'[0-9a-f]{40}\n', commit) is not None and rc == 0 and rc2 == 0 and commit.strip() == head.strip() == up.strip()),
        'the branch\'s adv3-bot.py equals the service copy\'s': read(WT + '/advisor/adv3-bot.py', 'rb') == read(SVC + '/adv3-bot.py', 'rb'),
    })


def mode_render():
    saved = list(sys.path)
    sys.path.insert(0, SVC)
    try:
        spec = importlib.util.spec_from_file_location('advbot', SVC + '/adv3-bot.py')
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    scratch = WORK + '/render-state'
    os.makedirs(scratch, exist_ok=True)
    mod.STATE = scratch
    own = (sha256_file(BOTDIR + '/journal.jsonl'), sha256_file(BOTDIR + '/daily-sent'))

    class Cap(mod.Telegram):
        def __init__(self):
            super().__init__('123456:SECRET', 777)
            self.texts = []

        def call(self, method, http_timeout=30, **params):
            self.texts.append(params['text'])
            return {'message_id': len(self.texts)}

    cap, data, texts, calc, seen, liqs = Cap(), mod.Data(), {}, {}, [], {}
    real_make, real_liq = mod.make, mod.liquidity

    def make_seen(d, deposit, risk):
        out_ = real_make(d, deposit, risk)
        seen.append(out_[0])
        return out_

    def liq_seen(coin, now_ms):
        liqs[coin] = real_liq(coin, now_ms)
        return liqs[coin]

    mod.make, mod.liquidity = make_seen, liq_seen
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            for case in RENDER_CASES:
                n0, m0 = len(cap.texts), len(seen)
                liqs.clear()
                mod.handle(cap, data, case)
                texts[case] = cap.texts[n0:]
                cmd = mod.route(case)
                if cmd and cmd[0] == 'alloc' and len(seen) == m0 + 1:
                    _kind, budget, n, risk = cmd
                    p = mod.plan(seen[-1], data.cs, budget, n, risk, dict(liqs))
                    calc[case] = {'rep': seen[-1], 'liq': dict(liqs), 'plan': p, 'budget': budget, 'n': n, 'risk': risk,
                                  'parts': mod.plan_parts(seen[-1], p)}
    finally:
        mod.make, mod.liquidity = real_make, real_liq
    records = []
    if os.path.exists(scratch + '/journal.jsonl'):
        records = [json.loads(line) for line in read(scratch + '/journal.jsonl').splitlines()]
    same = own == (sha256_file(BOTDIR + '/journal.jsonl'), sha256_file(BOTDIR + '/daily-sent'))
    out('replies: %s; the bot\'s log: %d lines; STRONG coins of the report: %d; trades placed: %s' % (
        ', '.join('%d chars in %d parts' % (sum(map(len, texts[k])), len(texts[k])) for k in RENDER_CASES), buf.getvalue().count('\n'),
        len(seen[0]['strong']) if seen else -1, ', '.join(str(len(calc[c]['plan']['items'])) for c in calc)))
    expect = {'help': mod.HELP, 'usdt': mod.adv3.usdt, 'num': mod.adv3.num,
              'consts': (mod.STOP_MAX, mod.MIN_NOTIONAL, mod.LIQ_FRAC, mod.adv3.RISK_MAX, mod.adv3.RISK_ALL, mod.adv3.TOP_N, mod.adv3.COST)}
    verdict('RENDER', render_checks(texts, calc, seen[0] if seen else None, [r['kind'] for r in records], records, buf.getvalue(), same, expect))


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
    """The work tree's files a report keeps by name: state.json, the two files B-DEPLOY saves, and every file under
    logs/; relative to WORK, sorted."""
    names = ['state.json', 'bot.before', 'commit.before']
    for d, _s, fs in os.walk(WORK + '/logs'):
        names += [os.path.relpath(os.path.join(d, f), WORK) for f in fs]
    return sorted(n for n in names if os.path.isfile(os.path.join(WORK, n)))


def mode_keep():
    """B-RECLAIM-OWN's copy: every kept file into the forensic store as tz37-work--<path with - for />, by exclusive
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
        dest = FORENSICS + '/tz37-work--' + rel.replace('/', '--')
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
    old = ('X = 1\nHELP = 1\ndef a():\n    return 1\ndef b():\n    return 2\nclass K:\n    def m(self):\n        return 1\n'
           'class T:\n    x = 1\nCMD = 5\n')
    new_ok = ('X = 1\nHELP = 2\ndef a():\n    return 1\ndef b():\n    return 3\nclass K:\n    def m(self):\n        return 1\n'
              'class T:\n    x = 2\nnewfn = 0\ndef c():\n    return 0\n')
    saved = (BOT_CHANGED, BOT_ADDED, BOT_REMOVED, BOT_SAME, BOT_CONST)
    globals().update(BOT_CHANGED={'b', 'T'}, BOT_ADDED={'c'}, BOT_REMOVED=set(), BOT_SAME=('a', 'K'),
                     BOT_CONST=({'HELP'}, {'newfn'}, {'CMD'}))
    try:
        good = bot_checks(old, new_ok)
        ok(all(good.values()) and len(good) == 3, 'bot_checks: exactly the named definitions and constants differ, 3 of 3')
        ok(not all(bot_checks(old, new_ok.replace('def a():\n    return 1', 'def a():\n    return 9')).values()),
           'bot_checks: a changed function that should be the same reads FAIL')
        ok(not all(bot_checks(old, new_ok.replace('class T:\n    x = 2', 'class T:\n    x = 1')).values()),
           'bot_checks: a function that should have changed and did not reads FAIL')
        ok(not all(bot_checks(old, new_ok + 'def d():\n    return 0\n').values()), 'bot_checks: an extra function reads FAIL')
        ok(not all(bot_checks(old, new_ok.replace('X = 1', 'X = 2')).values()), 'bot_checks: a changed constant not named reads FAIL')
    finally:
        globals().update(BOT_CHANGED=saved[0], BOT_ADDED=saved[1], BOT_REMOVED=saved[2], BOT_SAME=saved[3], BOT_CONST=saved[4])
    # ---- G-RENDER on stand-ins: a plan, the replies made from it, and the reports around them
    usdt = lambda x: f'{round(x):,}'.replace(',', ' ')
    num = lambda x, sig=3: f'{x:,.0f}'.replace(',', ' ')
    expect = {'help': 'HELP', 'usdt': usdt, 'num': num, 'consts': (STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, RISK_MAX, RISK_ALL, 3, 0.001)}

    def item(coin, side, stop, notional, margin, loss, exact, capped=False):
        return {'card': {'coin': coin, 'side': side, 'entry': 100.0, 'stop_pct': stop}, 'notional': notional,
                'leverage': min(20, math.floor(1 / (1.5 * stop / 100 + 0.01))), 'margin': margin, 'loss': loss, 'loss_exact': exact, 'capped': capped}

    def make_plan(budget, n, items, rejected):
        alloc = sum(i['notional'] for i in items)
        return {'budget': budget, 'n': n, 'items': items, 'rejected': rejected, 'allocated': alloc, 'free': budget - alloc,
                'margin': sum(i['margin'] for i in items), 'loss': sum(i['loss'] for i in items), 'loss_exact': sum(i['loss_exact'] for i in items)}

    def render(p, extra=''):
        first = ['Бюджет %s USDT · до %d сделок' % (num(p['budget']), p['n']), 'Подходящих сделок: %d из %d запрошенных' % (len(p['items']), p['n'])
                 if p['items'] else 'Подходящих сделок нет',
                 'Размещено %s USDT · маржа %s USDT' % (usdt(p['allocated']), usdt(p['margin'])),
                 'Потеря на стопах %s USDT' % usdt(p['loss']), 'Свободно %s USDT' % usdt(p['free']), extra]
        for it in p['items']:
            first += ['Качество: z +2', '⛔ Стоп: 1', '🎯 1', '🎯 2', '🎯 3', 'Капитал: %s USDT · плечо %d× изол. · маржа %s USDT' % (usdt(it['notional']), it['leverage'], usdt(it['margin'])),
                      'Потеря на стопе: %s USDT' % usdt(it['loss']), 'Инвалидация: цена ≤ 1']
        return ['\n'.join(first), '\n'.join(TRUST + ('Размеры — формула, не доказанная',))]

    rep = {'top': ['ETH', 'SOL', 'XRP', 'BTC'], 'strong': ['ETH', 'SOL', 'XRP'], 'marks_ok': True}
    p1 = make_plan(10000.0, 3, [item('ETH', 1, 8.0, 609, 87, 50, 49.938), item('XRP', 1, 10.0, 300, 50, 31, 30.6)], [('SOL', 'SHORT', 'стоп 13,0% дальше 11,1%')])
    p2 = make_plan(15000.0, 5, [item('ETH', 1, 8.0, 900, 129, 74, 73.8)], [('SOL', 'SHORT', 'стоп 13,0% дальше 11,1%'), ('XRP', 'LONG', 'стоп 12,0% дальше 11,1%')])
    p3 = make_plan(10000.0, 3, [], [('ETH', 'LONG', 'стоп 12,0% дальше 11,1%'), ('SOL', 'SHORT', 'стоп 13,0% дальше 11,1%'), ('XRP', 'LONG', 'стоп 14,0% дальше 11,1%')])
    c1, c2, c3 = RENDER_CASES[1], RENDER_CASES[2], RENDER_CASES[3]
    calc = {c1: {'rep': rep, 'liq': {}, 'plan': p1, 'budget': 10000.0, 'n': 3, 'parts': render(p1)},
            c2: {'rep': rep, 'liq': {}, 'plan': p2, 'budget': 15000.0, 'n': 5, 'parts': render(p2, 'STRONG бывает только в ТОП-3: больше 3 сделок не будет')},
            c3: {'rep': rep, 'liq': {}, 'plan': p3, 'budget': 10000.0, 'n': 3, 'parts': render(p3)}}
    plain = ['\n'.join(list(TRUST + BOOK) + ['🟢 <b>BTC · LONG</b>', 'Основание: сумма знаков +4', 'Инвалидация: цена ≤ 1'])]
    texts = {RENDER_CASES[0]: plain, c1: calc[c1]['parts'], c2: calc[c2]['parts'], c3: calc[c3]['parts'], RENDER_CASES[4]: ['HELP'], RENDER_CASES[5]: ['HELP']}
    records = [{'kind': 'request'}] + [{'kind': 'alloc', 'alloc': {'allocated': calc[c]['plan']['allocated'], 'free': calc[c]['plan']['free'],
                                                                'items': [{'coin': it['card']['coin']} for it in calc[c]['plan']['items']]}} for c in (c1, c2, c3)]
    good = render_checks(texts, calc, rep, RENDER_KINDS, records, '', True, expect)
    ok(all(good.values()) and len(good) == 16, 'render_checks: whole replies and plans read 16 of 16')

    def bad(**kw):
        a = dict(texts=texts, calc=calc, plain=rep, kinds=RENDER_KINDS, records=records, log='', same=True, expect=expect)
        a.update(kw)
        return not all(render_checks(a['texts'], a['calc'], a['plain'], a['kinds'], a['records'], a['log'], a['same'], a['expect']).values())

    def with_item(case, **changes):
        p = calc[case]['plan']
        its = [dict(p['items'][0], **changes)] + p['items'][1:]
        q = make_plan(p['budget'], p['n'], its, p['rejected'])
        return dict(calc, **{case: dict(calc[case], plan=q, parts=render(q), )}), dict(texts, **{case: render(q)})

    ok(bad(log='Traceback (most recent call last):') and bad(log='request failed'), 'render_checks: a traceback or a failed request in the bot\'s log reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[0]: []})), 'render_checks: a command with no answer reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[4]: ['<b>HELP']})), 'render_checks: unbalanced markup reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[0]: [plain[0].replace('Оценка доверия', '')]})), 'render_checks: a «сигнал» without its rating block reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[0]: [plain[0] + '\n🔴 <b>SOL · SHORT</b>']})), 'render_checks: a card without its basis reads FAIL')
    ok(bad(expect=dict(expect, consts=(12.0,) + expect['consts'][1:])), 'render_checks: another stop limit than 11.1 % reads FAIL')
    ok(bad(texts=dict(texts, **{c1: [calc[c1]['parts'][0] + ' ', calc[c1]['parts'][1]]})), 'render_checks: a reply that is not the plan\'s own reads FAIL')
    ok(bad(texts=dict(texts, **{c1: [calc[c1]['parts'][0].replace('Капитал:', 'Объём:', 1), calc[c1]['parts'][1]]}), calc=dict(calc, **{c1: dict(calc[c1], parts=[calc[c1]['parts'][0].replace('Капитал:', 'Объём:', 1), calc[c1]['parts'][1]])})),
       'render_checks: a trade without its capital line reads FAIL')
    for label, case, changes in (('a coin that is not STRONG in the plan', c1, {'card': {'coin': 'BTC', 'side': 1, 'entry': 100.0, 'stop_pct': 8.0}}),
                                 ('a stop beyond 11.1 %', c1, {'card': {'coin': 'ETH', 'side': 1, 'entry': 100.0, 'stop_pct': 11.2}}),
                                 ('a position without an entry', c1, {'card': {'coin': 'ETH', 'side': 1, 'entry': None, 'stop_pct': 8.0}}),
                                 ('a loss at the stop beyond 1 % of the budget', c1, {'loss_exact': 100.5}),
                                 ('a position under 5 USDT', c1, {'notional': 4}),
                                 ('a position that is not whole', c1, {'notional': 609.5}),
                                 ('a leverage that is not the rule\'s', c1, {'leverage': 12}),
                                 ('a margin that does not cover the leverage', c1, {'margin': 80}),
                                 ('a position beyond its liquidity cap', c1, {'notional': 609})):
        cc, tt = with_item(case, **changes)
        if 'liquidity' in label:
            cc = dict(cc, **{case: dict(cc[case], liq={'ETH': 100_000.0})})
        ok(bad(calc=cc, texts=tt), 'render_checks: %s reads FAIL' % label)
    q = make_plan(10000.0, 3, [item('ETH', 1, 8.0, 609, 87, 50, 49.938), item('XRP', 1, 10.0, 300, 50, 31, 90.0), item('SOL', 1, 8.0, 609, 87, 50, 95.0)], [])
    ok(bad(calc=dict(calc, **{c1: dict(calc[c1], plan=q, parts=render(q))}), texts=dict(texts, **{c1: render(q)})), 'render_checks: all losses together beyond 5 % of the budget read FAIL')
    q = make_plan(10000.0, 3, [item('ETH', 1, 8.0, 609, 87, 50, 49.938)], [])
    ok(bad(calc=dict(calc, **{c1: dict(calc[c1], plan=q, parts=render(q))}), texts=dict(texts, **{c1: render(q)})), 'render_checks: a STRONG coin neither placed nor named reads FAIL')
    unproven = lambda case: [calc[case]['parts'][0], calc[case]['parts'][1].replace('не доказанная', 'доказанная')]
    ok(bad(calc=dict(calc, **{c1: dict(calc[c1], parts=unproven(c1))}), texts=dict(texts, **{c1: unproven(c1)})), 'render_checks: a reply without the note that the sizes are unproven reads FAIL')
    ok(bad(calc=dict(calc, **{c3: dict(calc[c3], n=5)})), 'render_checks: «сигнал 10000» that is not the three-trade view reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[4]: ['HELP', 'more']})), 'render_checks: an unknown text answered by more than HELP reads FAIL')
    ok(bad(kinds=RENDER_KINDS[:-1]) and bad(kinds=['alloc'] + RENDER_KINDS[1:]), 'render_checks: a journal that lacks a record or has another kind reads FAIL')
    ok(bad(same=False), 'render_checks: the bot\'s own journal changed reads FAIL')
    pre = {'t': 1000.0, 'bot': {'MainPID': '10', 'NRestarts': '1'}, 'daily': '2026-10-31', 'journal': 7,
           'caps': {u: {'MainPID': str(i), 'NRestarts': '0', 'ActiveState': 'active'} for i, u in enumerate(CAPTURES, 20)}}
    now = {'bot': {'MainPID': '11', 'NRestarts': '2', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'enabled'},
           'caps': dict(pre['caps']), 'start': 1035.0, 'copy_t': 990.0, 'argv': ARGV, 'procs': [11], 'sha_adv3': H['adv3'],
           'sha_bot': H['bot_new'], 'sha_unit': H['unit'], 'daily': '2026-10-31', 'journal': 7, 'serving': True,
           'daily_line': False, 'traceback': False}
    ok(all(unit_checks('new', pre, now).values()) and len(unit_checks('new', pre, now)) == 9, 'unit_checks: a clean restart reads 9 of 9')
    for key, val, label in (('daily', '2026-11-01', 'a daily-sent changed'), ('journal', 8, 'a message sent again'),
                            ('start', 1200.0, 'a process started 200 s after the kill'), ('sha_bot', H['bot_old'], 'the old bot'),
                            ('sha_adv3', 'x', 'another adv3.py'), ('daily_line', True, 'a daily line since the mark'),
                            ('procs', [11, 12], 'a second process under the argv')):
        ok(not all(unit_checks('new', pre, dict(now, **{key: val})).values()), 'unit_checks: %s reads FAIL' % label)
    moved = {u: dict(c, NRestarts='1') for u, c in pre['caps'].items()}
    ok(not all(unit_checks('new', pre, dict(now, caps=moved)).values()), 'unit_checks: a capture unit restarted reads FAIL')
    ok(all(unit_checks('old', pre, dict(now, sha_bot=H['bot_old'])).values()), 'unit_checks: the rollback reads the old bot')
    log = ('2026-10-31T06:00:01Z daily sent for the close of 2026-10-30\n2026-10-31T09:00:00Z serving the pinned chat: pid 11 offset 5 daily-sent 2026-10-31\n'
           'Traceback (most recent call last):\n')
    t = calendar.timegm(time.strptime('2026-10-31T08:59:59', '%Y-%m-%dT%H:%M:%S'))
    jl = '{"kind": "daily", "x": 1}\n{"kind": "request"}\nnot json\n{"kind": "daily"}\n'
    ok(daily_records(jl) == 2 and daily_records('') == 0, 'daily_records: the daily kind counted, requests and a broken line left out')
    ok(log_since(log, t, 11) == (True, False, True), 'log_since: serving found, the earlier daily left out, a later traceback found')
    ok(log_since(log, t, 12) == (False, False, True), 'log_since: another pid does not serve')
    ok(memory_gate(MEM_FLOOR, None) == (True, MEM_FLOOR) and memory_gate(MEM_FLOOR - 1, MEM_FLOOR) == (True, MEM_FLOOR)
       and memory_gate(MEM_FLOOR - 1, MEM_FLOOR - 2) == (False, MEM_FLOOR - 2) and memory_gate(MEM_FLOOR - 1, None) == (False, MEM_FLOOR - 1),
       'memory_gate: a first read at the floor passes, a first read below it is decided by the second')
    ok(all(number_reading(['CryptoTZ/' + 'TZ-37-capital-allocation.md', 'CryptoTZ/TZ-36-x.md']).values()), 'number: the one file reads PASS')
    ok(not all(number_reading(['CryptoTZ/TZ-37-capital-allocation.md', 'CryptoTZ/TZ-37-other.md']).values()), 'number: two files of the number read FAIL')
    ok(not all(number_reading(['CryptoTZ/TZ-37-capital-allocation.md', 'CryptoReports/TZ-37-x-report.md']).values()), 'number: a report of the number reads FAIL')
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        os.makedirs(tmp + '/logs/sub')
        for rel in ('state.json', 'bot.before', 'logs/01-a.log', 'logs/sub/02-b.log', 'wt-not-kept.txt', 'history.json'):
            with open(tmp + '/' + rel, 'w') as fh:
                fh.write(rel)
        saved_work = WORK
        globals().update(WORK=tmp)
        try:
            kept = kept_files()
        finally:
            globals().update(WORK=saved_work)
    ok(kept == ['bot.before', 'logs/01-a.log', 'logs/sub/02-b.log', 'state.json'],
       'kept_files: the named files and the logs, nothing else, commit.before absent where not written')
    out('SELFTEST PASS: %d of %d checks passed' % (len(done), len(done)))


def main(argv):
    if not argv:
        sys.exit('usage: tz37-capital-allocation.py MODE [ARG]')
    mode, rest = argv[0], argv[1:]
    table = {'fingerprint': mode_fingerprint, 'host': mode_host, 'number': mode_number, 'rule': mode_rule,
             'copy': mode_copy, 'render': mode_render, 'keep': mode_keep, 'stopped': mode_stopped, 'selftest': mode_selftest}
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

