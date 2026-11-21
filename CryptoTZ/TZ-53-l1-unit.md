# TZ-53 — L1's unit: rule W live at the minimum size from the live host in Sofia, a systemd unit with a loss limit and «Стоп» in Telegram, its order path proved by its own code before it starts

**Canonical filename:** `TZ-53-l1-unit.md`. The committed file takes this name and no other.

**Executor model: Claude Opus 5.5.** Two hosts, a live order path with money in the wallet, a unit deployed that outlives the run.

**Required System Map revision:** `2026-11-21-c` — **it ships with this TZ:** the Boss uploads `SYSTEM-MAP.md` and this file in one upload onto `main` at `dc0b34e`, which carries revision `2026-11-21-b`. The revision moves no row and no anchor, adds none and replaces none (CANON hard rule 17): it records this TZ's decisions — map §7 items 184, 186, 187, 190 and 192 — and CANON `2026-11-21-a`'s PART IV; this TZ's merge adds `engine/l1-bot.py`, `deploy/systemd/l1-bot.service` and `research/tz53-l1-account.py`, which the map revision attached to its verdict carries.

**Map sections this TZ rests on**, copied from §10's C8 (map §7 item 174): §0, the fingerprint gate, its table and the signing page; §1, the repository, its TZs and pull request #50; §2.6, the reward book — its selection, its store's bounds and its reserve; §3, the units, the trees on the host and the session directories; §5, L1's row and the reward book's days; §6, its rows host identity, for TZ host gates; live host; live host identity, for TZ host gates; live host — the venue's geoblock, measured 2026-11-19, TZ-48 and TZ-49, and 2026-11-20, TZ-50; live host — the venue's CLOB from Sofia; language; git remote; egress; venue edge — the `User-Agent`; venue constants; maker incentives; disk; disk floors and caps; process supervision; memory; clock; sandbox limit — destructive actions; and harness — background output; §7 items 86, 89, 91, 95, 98, 119, 124, 127, 132, 137, 138, 140, 143, 144, 150, 156, 163, 164, 169, 171, 172, 174, 175, 176, 177, 180, 181, 183, 184, 185, 186, 187, 189, 190, 191 and 192; §8. **And TZ-52**, `CryptoTZ/TZ-52-l1-round-trip.md`, with TZ-51's file it rests on, `CryptoTZ/TZ-51-l1-account-round-trip-rerun.md` — every section this file names (§0.0 below); **TZ-52's report**, `CryptoReports/TZ-52-l1-round-trip-report.md`, its §1 and §2.4, whose state this TZ starts from; and **TZ-45**, `CryptoTZ/TZ-45-l0-rule-w.md`, its §1 — rule W, which the unit runs.

**Required anchors**, from map §0. A mismatch on any one is BLOCKED before any work:

| anchor | required |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` |
| `A4` — executor contract | `6ac6e10aeabc` |
| `A5` — recorder | `0f6c90451cbd` |
| `A6` — pricer | `729f0bcdbee3` |

**Written authorization (contract §10).** From the live host, IPv4 alone, by the checker's modes §1.9 names and by `engine/l1-bot.py`'s `ready`, `prove`, `clear-stop` and `serve`, and nothing else: `polymarket.com`'s geoblock; the anonymous reads of `gamma-api.polymarket.com` and the CLOB that TZ-33's selection makes, and each candidate's reward document; the CLOB's market channel; `polygon.drpc.org`'s `eth_call` reads of the wallet's pUSD, its allowances and its position approvals; **by the session key** — the CLOB's derivation of its API credentials, its reads of the wallet's open orders, trades, balances and allowances, closed-only state, earnings and rebates, **orders, each post-only — the prove's, at most `5`, each a buy of its market's minimum order size at the lowest price its tick allows, and the unit's by rule W, each of its market's minimum scoring size** — their cancellation by id and `cancel_all`, and order heartbeats; the client's reads of the wallet through the relayer; Telegram's Bot API by the bot's token — `getMe`, `getUpdates` and `sendMessage` to the pinned chat. **Nothing is submitted to the relayer, and no owner's signature is asked.** From the capture host: `git` and `gh` as TZ-52 §2 item 1, pull request #50 in place of #49.

**Before EXECUTE.** The Boss tops up the bot's wallet on polymarket.com, signed in with the bot's MetaMask account, so that it holds from `80` to `150` pUSD — it held `11.10` at TZ-52 (§1.2). During the run, once the bot writes in his Telegram «проверка кнопки «Стоп»», he presses «Стоп» within 30 minutes (§3 step 10).

**When: begun at any hour.** The unit runs from then on.

---

## 0. TZ-52's text, renamed, and what this file replaces

### 0.0 The rule

**TZ-52's file is this TZ's text wherever this file says nothing** — and through it TZ-51's, as TZ-52 §0.0 reads it — **read with the renaming R′ after TZ-52's R:** `TZ-52-l1-round-trip` reads `TZ-53-l1-unit`; `tz-52-l1-round-trip`, `tz-53-l1-unit`; `tz52`, `tz53`; `TZ-52`, `TZ-53`; `ТЗ-52`, `ТЗ-53`; `2026-11-21-a`, `2026-11-21-c`. So the work tree is `/root/tz53-work` on both hosts, the checker `research/tz53-l1-account.py`, the branch `tz-53-l1-unit`, the report `CryptoReports/TZ-53-l1-unit-report.md`, the agent `btc-5m-twap-tz53`. **R′ does not touch** TZ-51's and TZ-52's own files, Appendices, reports and pull requests, their copies under `/var/lib/l1-bot/`, or B-REVOKE (TZ-51 §4.11), which stays TZ-51's word for word with TZ-51's copy. **Where this file and TZ-52 or TZ-51 differ, this file holds. A step either has and this file neither keeps nor names is not run.**

Two abbreviations beside TZ-51 §0.0's seven, written out in full in every block handed to the Boss:

- **`LE M NN`** — the engine's mode `M` on the live host, from the stage's copy: `R 'cd /root/tz53-work/engine && { date -u +%FT%T.%NZ; /root/l1-env/bin/python -B /root/tz53-work/engine/l1-bot.py M; echo "exit=$?"; } >> /root/tz53-work/logs/NN.log 2>&1; tail -n 60 /root/tz53-work/logs/NN.log'`.
- **`LU M NN`** — the same from the unit's installed copy: `R 'cd /root/l1-bot-svc && { date -u +%FT%T.%NZ; /root/l1-env/bin/python -B /root/l1-bot-svc/l1-bot.py M; echo "exit=$?"; } >> /root/tz53-work/logs/NN.log 2>&1; tail -n 60 /root/tz53-work/logs/NN.log'`.

### 0.1 The files, staged — replaces TZ-52 §0.1

TZ-52's own §0.1 script, read from TZ-52's file on `main` and run as it stands into a scratch directory that this script removes, its result — TZ-52's instrument, `a425e67c…`, asserted there — changed by the edits below, each asserted to occur the number of times it names; this file's Appendices A, B and C, each extracted by its fence and the next line that is a fence alone; and the two frozen files the unit takes its rules from, from `main`. **This script, verbatim**, its first argument the destination and its second `stage` — six files — or `branch` — the branch's three — its output into `logs/01-stage.log`:

```
/root/tz04a-env/venv/bin/python -B - /root/tz53-work/stage stage <<'EOF3'
import hashlib, os, shutil, subprocess, sys
REPO = "/root/btc-5m-twap"
TZ = REPO + "/CryptoTZ/TZ-53-l1-unit.md"
DEST, WHAT = sys.argv[1], sys.argv[2]
assert WHAT in ("stage", "branch"), WHAT
WANT = {
    "research/tz53-l1-account.py": "e4b72d0e285f1d8736a056012d3c9056f7f103e8e899742e10e488932c910c94",
    "engine/l1-bot.py": "98851b3c0df447ed7c846edfbf18b9ea1611d12228a4d9a3c1fda3b4f22da214",
    "deploy/systemd/l1-bot.service": "a6305d0e7a220ea88f5a4d2be612cac35f3dbe527d7c3b7ed12fd7c47f956266",
    "engine/l1-bot.service": "a6305d0e7a220ea88f5a4d2be612cac35f3dbe527d7c3b7ed12fd7c47f956266",
    "engine/tz33-reward-book-capture.py": "a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670",
    "engine/tz45-l0-rule-w.py": "4720e78573e54b1325dd24af7c30e0de59bfb4c1879d309a23fa6bab6b32d2d4",
    "b-deploy.sh": "373df4093b4ba4ad4fd093a173ad4c5396a52e2231b789814aef99ca23acf069"}
FILES = {"branch": ("research/tz53-l1-account.py", "engine/l1-bot.py", "deploy/systemd/l1-bot.service"),
         "stage": ("research/tz53-l1-account.py", "engine/l1-bot.py", "engine/l1-bot.service",
                   "engine/tz33-reward-book-capture.py", "engine/tz45-l0-rule-w.py", "b-deploy.sh")}


def fenced(fence):
    lines = open(TZ, encoding="utf-8").read().split("\n")
    i = lines.index(fence)
    j = lines.index("```", i + 1)
    return ("\n".join(lines[i + 1:j]) + "\n").encode("utf-8")


def checker():
    lines = open(REPO + "/CryptoTZ/TZ-52-l1-round-trip.md", encoding="utf-8").read().split("\n")
    i = lines.index("/root/tz04a-env/venv/bin/python -B - /root/tz52-work/stage <<'EOF2'")
    j = lines.index("EOF2", i + 1)
    tmp = os.path.join(DEST, ".tz52")
    os.makedirs(tmp)
    try:
        subprocess.run([sys.executable, "-B", "-", tmp], input="\n".join(lines[i + 1:j]) + "\n", text=True,
                       check=True)
        t = open(os.path.join(tmp, "research/tz52-l1-account.py"), encoding="utf-8").read()
    finally:
        shutil.rmtree(tmp)
    EDITS = [
        ("TZ-52-l1-round-trip", "TZ-53-l1-unit", 3),
        ("tz-52-l1-round-trip", "tz-53-l1-unit", 1),
        ("tz52", "tz53", 21),
        ("TZ-52", "TZ-53", 9),
        ("ТЗ-52", "ТЗ-53", 3),
        ('MAP_REVISION = "2026-11-21-a"', 'MAP_REVISION = "2026-11-21-c"', 1),
        ('"""TZ-53 - L1\'s round trip at the minimum size, from the live host in Sofia, on the account TZ-51 left: its session\n'
         "key authorized by the Boss's signature, the wallet's pUSD allowances to the venue's two exchanges at the maximum.\n"
         "TZ-51 BLOCKED at G-APPROVE: the venue's relayer approves an exchange at MaxUint256 alone, so the allowance stays at\n"
         "the maximum the venue set, and what a stolen session key could spend is the wallet's balance (map section 7 item\n"
         "190). This file proves one order's round trip with the key through the venue's official client, polymarket-client,\n"
         "installed at pinned versions and hashes into /root/l1-env, pins the bot's Telegram chat and reports there. Every\n"
         "refusal of the venue is printed in the venue's own words, its hexadecimal strings masked (map section 7 item 191).\n"
         "Its modes that ask the Boss anything are TZ-51's, kept and tested; TZ-53 runs none of them.\n",
         '"""TZ-53 - L1\'s unit deployed: this file is TZ-52\'s instrument renamed, its deployment checks on both hosts -\n'
         "the fingerprint, the number, the refs, the capture's room, the scratch, the reclaim, the live host's gate and its\n"
         "facts, the geoblock, sshd and the client's environment. The unit itself and every check of its own - its account,\n"
         "its order path, its stop, its state under systemd - are engine/l1-bot.py's modes (TZ-53 section 5). Its modes\n"
         "that ask the Boss anything, its approvals and its round trip are TZ-51's and TZ-52's, kept and tested; TZ-53 runs\n"
         "none of them.\n", 1),
    ]
    for old, new, n in EDITS:
        assert t.count(old) == n, (old[:60], t.count(old), n)
        t = t.replace(old, new)
    return t.encode("utf-8")


data = {"research/tz53-l1-account.py": checker(),
        "engine/l1-bot.py": fenced("```python file=engine/l1-bot.py"),
        "deploy/systemd/l1-bot.service": fenced("```ini file=deploy/systemd/l1-bot.service"),
        "b-deploy.sh": fenced("```bash file=b-deploy.sh")}
data["engine/l1-bot.service"] = data["deploy/systemd/l1-bot.service"]
for rel in ("tz33-reward-book-capture.py", "tz45-l0-rule-w.py"):
    with open(os.path.join(REPO, "research", rel), "rb") as fh:
        data["engine/" + rel] = fh.read()
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
| base: TZ-52's instrument, `research/tz52-l1-account.py`, by TZ-52's §0.1 | 3,326 | 188,720 | `a425e67cce7178e425b04f899ad245cf31a38848bd2553dfacdbbbcdf3a73366` |
| `research/tz53-l1-account.py` — the checker | 3,324 | 188,378 | `e4b72d0e285f1d8736a056012d3c9056f7f103e8e899742e10e488932c910c94` |
| `engine/l1-bot.py` — Appendix A, the unit | 3,656 | 188,968 | `98851b3c0df447ed7c846edfbf18b9ea1611d12228a4d9a3c1fda3b4f22da214` |
| `deploy/systemd/l1-bot.service` and `engine/l1-bot.service` — Appendix B | 29 | 1,014 | `a6305d0e7a220ea88f5a4d2be612cac35f3dbe527d7c3b7ed12fd7c47f956266` |
| `b-deploy.sh` — Appendix C | 135 | 6,789 | `373df4093b4ba4ad4fd093a173ad4c5396a52e2231b789814aef99ca23acf069` |
| `engine/tz33-reward-book-capture.py`, from `research/` on `main` | 3,542 | 175,160 | `a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670` |
| `engine/tz45-l0-rule-w.py`, from `research/` on `main` | 4,299 | 233,655 | `4720e78573e54b1325dd24af7c30e0de59bfb4c1879d309a23fa6bab6b32d2d4` |

TZ-52's script prints its own line first, `… research/tz52-l1-account.py 3326 188720 a425e67c… created`, into the scratch directory. A failed assert or another hash is BLOCKED; here every line reads `created`. **`b-deploy.sh` is staged and never committed:** the report quotes it by this hash.

### 0.2 to 0.6 — TZ-52's, under R′, with these differences

- **§0.2:** `FINGERPRINT PASS: revision 2026-11-21-c; anchors 6 of 6, 4 re-derived; rows 67: frozen 64 of 64 equal, tracked 2, reported 1; the signing page on main equal to TZ-50's Appendix B`.
- **§0.4:** the checker's floors are TZ-51's, unchanged — `MEM_FLOOR` `86,426,834` and `MEM_FLOOR_SDK` `274,917,678`, `CAPTURE_FLOOR` `7,795,535,636`, `LIVE_FLOOR` `2,447,483,648`; the Architect's runs of the checker on these bytes peaked at `35,536,896` to `36,192,256` for `selftest` and `115,064,832` to `115,523,584` for `sdk-selftest`, each under the host peak those floors model, `43,213,417` and `137,458,839`. **The engine's floors are the checker's for the client:** `MEM_FLOOR` `274,917,678` and `DISK_FLOOR` `2,447,483,648` on `/`, read at the start of `ready`, `prove` and `serve` (`floors`); its runs peaked at `69,378,048` to `69,644,288` for `selftest` and `112,115,712` to `113,111,040` for `sdk-selftest`, under `137,458,839`. A `serve` below a floor exits `1` and systemd starts it again in `30` s.
- **§0.5:** `NUMBER PASS - 2 of 2`; the refs against map §1's read of 2026-11-21, 202 lines, each kind that differs named and none BLOCKING; the branch `tz-53-l1-unit` absent.
- **§0.6, the copy** — `07-copy.log` — carries beside the checker the stage's other five files: `R 'mkdir /root/tz53-work /root/tz53-work/logs /root/tz53-work/engine; echo "exit=$?"'`, one `scp` for the checker as TZ-51 §0.6, then `scp -q -o BatchMode=yes -o LogLevel=QUIET /root/tz53-work/stage/engine/* live-host:/root/tz53-work/engine/; echo "scp exit=$?"` and `scp -q -o BatchMode=yes -o LogLevel=QUIET /root/tz53-work/stage/b-deploy.sh live-host:/root/tz53-work/b-deploy.sh; echo "scp exit=$?"`, then `R 'cd /root/tz53-work && sha256sum tz53-l1-account.py b-deploy.sh engine/*'`: `exit=0`, every `scp exit=0` and the six SHA-256 of §0.1 — anything else is BLOCKED.
- **§0.6, the condition LS replaced:** at `host before`, root's keys the Executor's alone, and the `PATH` lines exactly these, as TZ-52's report §2.4 quotes `79-host-after.log`, the last line under R′:

```
PATH /etc/l1-bot: dir mode 0700 uid 0 bytes 4096
PATH /etc/l1-bot/session-key: file mode 0600 uid 0 bytes 67
PATH /etc/l1-bot/relayer-key: file mode 0600 uid 0 bytes 105
PATH /etc/l1-bot/telegram-token: file mode 0600 uid 0 bytes 47
PATH /etc/l1-bot/chat-id: file mode 0600 uid 0 bytes 10
PATH /var/lib/l1-bot: dir mode 0700 uid 0 bytes 4096
PATH /var/lib/l1-bot/account.json: file mode 0600 uid 0 bytes 310
PATH /root/l1-env: dir mode 0755 uid 0 bytes 4096
PATH /root/tz53-work/wheels: absent
```

  and, into `43-l1-before.log`, `R 'ls -A /var/lib/l1-bot; test -e /root/l1-bot-svc; echo "svc exit=$?"; test -e /etc/systemd/system/l1-bot.service; echo "unit exit=$?"; systemctl is-active l1-bot.service tz53-deploy.service; echo "active exit=$?"'`: exactly `account.json`, `tz51-l1-account.py` and `tz52-l1-account.py`; `svc exit=1`; `unit exit=1`; both `inactive`. Anything else is BLOCKED before any mode but `host` runs there: the account is not the one TZ-52 left.

---

## 1. What TZ-52 left, and what this TZ decides

### 1.0 The state

TZ-52 BLOCKED at §3.9 (its report §1): **the session key's post-only buy for the bot's wallet read `live` in `127` ms**, the CLOB answered its read by id `null`, which its flow did not handle, and `cancel_all` cancelled it — `canceled` `1`. Before it: G-READY 7 of 7, `11.10` pUSD, both allowances at the venue's maximum; the bot's Telegram chat pinned. Pull request #50 open. **The order path's decisive part is measured — a placement live and a cancellation served** (map §7 item 192); its read-back is this TZ's to prove, by the unit's own code before it starts.

### 1.1 The unit — decided: rule W as TZ-45 fixed it, live, at each market's minimum size

`engine/l1-bot.py`, Appendix A: one process, Python 3.12 and `asyncio`, the venue's client `polymarket-client` `0.20.0` from `/root/l1-env`, IPv4 alone by its audit hook (map §7 item 181). **Its rules are not written again:** the day's selection is TZ-33's `run_rule` and its helpers, rule W's targets TZ-45's `w_targets` and its constants, each taken by name from its frozen file beside the code, by that file's SHA-256 — nothing else of either file runs (`load_frozen`; CANON PART III, one implementation of every formula). Each UTC day:

- **The markets.** From 00:00 UTC less `900` s the unit reads the next day's selection by TZ-33's rule through its own requests, as the reward book's capture does, and keeps the replies under `/var/lib/l1-bot/select/`. Its candidates are the day's members of a proved kind whose minimum size is `20` shares or less, in the selection's rank by daily rate; each candidate's reward document is read every `300` s and kept under `polls/`. **A candidate is quoted while its last served poll carries the selection's terms and a competitiveness of at most `1`** (TZ-45 §1; map §5): a market whose terms move is left for the day, its orders cancelled. **At most `4` markets are quoted at a time**, the highest ranked first; **no new market is quoted while `8` hold a position.**
- **The quote.** A bid and an ask of the market's minimum size, `0.9` of twice the maximum spread apart, centred in a touch that leaves a tick each side, neither more than `0.10` inside it — `w_targets` on the touch with the unit's own orders taken out; post-only, good till cancelled, at the market's tick; replaced when its target moves, an order living `3` s at least; **a position of one minimum size at most**, the side that would pass it withdrawn. The ask is a sell of the first token where the wallet holds it, and otherwise a buy of the second at one less the ask — the same order in the venue's book. A market's books come from the CLOB's market channel.
- **The orders** are known by the wallet's open orders read by the session key every `3` s, the fills by its trades and its balances (§1.4); **order heartbeats every `5` s where the prove read them accepted**, so that a process that dies leaves no order on the book past the venue's `10` s.
- **The equity** — the wallet's pUSD on chain and each position marked at the touch, the first token at its best bid, the second at one less the best ask, a complete set at `1` — is read every `30` s.

A market's kind decides its exchange and signing domain — a CTF market's standard or negative-risk exchange, a Protocol V2 market's V2 exchange (map §7 item 186) — **and the unit quotes a market only where its prove's round trip on that kind read PASS** (§1.5).

### 1.2 The money — decided: the risk is the wallet's balance, and the unit stops itself inside it

**The allowances stay at the venue's maximum**, the one amount its relayer approves (map §7 item 190): what the session key could spend, by an order of this unit or of a thief, is the wallet's balance. **So the balance is the bound, and G-READY reads it:** from `80` to `150` pUSD at the unit's first start — four markets' quotes, under `20` pUSD each at a minimum size of `20` shares, and not more than the Boss entrusts to L1. **The loss limit:** the unit stops where its equity falls `25` pUSD below its start equity — the equity it read at its first start — read so twice, `30` s apart; its buys leave `1` pUSD unreserved. A stop cancels every open order of the key; the positions stay in the wallet, the Boss's to sell or hold. **The whole loss this step can take is the wallet's balance, `150` pUSD at most at its first start, and the unit's own stop holds it at `25` below its start, marked at the touch.** What a replay could not see — the taker our own quote calls out (CANON §1.5) — is what L1 measures, inside that limit. The prove's orders: at most `5`, each a buy at the lowest price its tick allows — at most `1` pUSD reserved, and nothing spent unless a seller takes it there. **CANON PART IV is revised by `2026-11-21-a` to say so** (§1.8).

### 1.3 Telegram — decided: map §7 item 184, built

The unit's own bot, its token and chat as TZ-51 and TZ-52 wrote them, answering the pinned chat alone, a reply keyboard of two buttons. **«Стоп»:** every open order of the key cancelled and read gone, a stop record written that holds across restarts and boots, exit `3`, which the unit file does not restart. **The same stop, each with its reason:** the loss limit; a geoblock read of `blocked`, every `900` s; the disk under its floor, read every `3,600` s; an equity unread for `900` s; the account in closed-only mode; the session key's authorization due within a day; orders that will not cancel. **«Статус»** reads and changes nothing. **Reports:** each start and stop with its reason, every fill, the position, and at 01:15 UTC the day's report — the rewards and rebates the venue paid our address for the day before, beside the unit's counts. **No message places, sizes, prices or moves an order, or starts the unit:** after a stop, `clear-stop` on the host — the record moved into its history, the chat's pending commands consumed — then a start by `systemctl` on the host. **The replay beside the venue's payouts is the measurement's, not the unit's:** it needs the capture's day whole (map §7 item 184, corrected by revision `2026-11-21-c`).

### 1.4 What the venue answers — decided: map §7 item 192

The unit knows its orders by the wallet's open orders read by its key and its fills by its trades and its balances — **never by a read by id**, which the venue answered `null`: an order placed is expected in the open orders within `10` reads `1` s apart, and one cancelled gone within as many. Every refusal prints the venue's own words, masked (`said`); the prove's record is written on every exit, an error's trace masked beside it; the self-tests' stand-in answers `null` to a read by id and asserts that none is made. **What the run does where the venue refuses** (map §7 item 191): a placement refused for any reason but crossing the book ends the prove with G-RT FAIL, its record holding the venue's words, and B-DEPLOY ends there — BLOCKED, no order left open, nothing started; no other attempt is made.

### 1.5 The prove — decided: CANON hard rule 14, the request path proved by the unit's own code before it starts

`prove`, once for a code by its SHA-256, from the unit's installed copy; its record `/var/lib/l1-bot/prove-N.json`, `N` at most `3`. **`serve` refuses, exit `2`, where no record of its own code read PASS.** Its gates, each one live request per endpoint through the unit's own functions. **Every request's headers are fixed:** the unit's own, Telegram's among them, `User-Agent: btc-5m-twap-l1` and `Accept: application/json`; the client's, its own headers with `httpx`'s agent set to the same; the market channel's handshake, the same agent (`Net`, `client` and `stream_session`).

- **G-GEO** — the geoblock over IPv4: served, `blocked` `False`.
- **G-READY** — six checks: a Deposit Wallet signed for by the session key; not in closed-only mode; the standard exchange's pUSD allowance at the maximum; the key authorized `7` days ahead at least; no open order of the key; its pUSD on chain from `80` to `150`.
- **G-TG** — `getMe` reads a bot; the prove's message sent to the pinned chat.
- **G-SELECT** — the day's selection by TZ-33's rule through the unit's requests; at least one candidate.
- **G-POLL** — one candidate's reward document served.
- **G-WS** — one session of the market channel: every subscribed book seeded.
- **G-RT** — **on each kind the day's candidates use, the Boss's round trip:** one post-only buy of the market's minimum order size at the lowest price its tick allows, **placed, seen in the wallet's open orders, cancelled by its id, seen gone, no fill, the balance unchanged** — three placements at most on the first kind where one would cross.
- **G-HB** — recorded, not gated: a heartbeat accepted, then none, and the venue's own cancellation of the order read within `40` s; the unit sends heartbeats only where it read so.
- **G-STOP** — the stop's round trip at the minimum size (map §7 item 184): an order resting and seen; the bot asks in the pinned chat; **the Boss's «Стоп» within `1,800` s**; every order cancelled and read gone; the stop record written, reason `drill`.

**G-PROVE PASS: the eight but G-HB, each PASS.** The kinds whose G-RT read PASS are the unit's kinds.

### 1.6 Protocol V2 — decided: map §7 item 186 re-scoped

Item 186 asked that, before L1's unit TZ and its measurement TZ were written, a TZ read on a day after 2026-12-01 whether the reward book records V2 markets' books whole and whether rule W's selection and replay read them. **The unit reads neither the capture nor a replay:** its books come from the venue's market channel, its orders sign each market's own version, and a kind is quoted only once its round trip has read PASS (§1.5). **That read therefore binds L1's measurement TZ alone**, whose replay rests on the capture; revision `2026-11-21-c` re-scopes the item so, and this section discharges the unit's half (CANON PART VI, the fifth rule). A V2 market among a day's candidates before a prove has proved that kind is left: proving it is new code's prove, in a TZ of its own, once the venue has moved rule W's markets (from 2026-11-24 and 2026-12-01). **Rejected:** holding L1 to 2026-12-01 for a fact the unit does not use.

### 1.7 Fees — map §7 item 187

L1's volume earns no rebate under the venue's tiers; the day's report shows what the venue paid — rewards and rebates — and no rebate is counted that the venue did not pay.

### 1.8 CANON `2026-11-21-a`, delivered with this TZ

PART IV's keys: the allowances at the venue's maximum, the risk the wallet's balance — from `80` to `150` pUSD at the unit's first start — and the unit's loss limit, `25` pUSD below its start equity. PART IV's deployment: **the live host's journal is JSON lines, a file a UTC day, `0600`** — the live host's environment holds the venue's client alone, pinned by hash; the TZ that reads the journal writes it as Parquet. PART IV's control: the replay beside the payouts is the measurement's. PART II's L1 row and PART III's locations carry the unit. The CANON is not in the repository; the Executor never reads it.

### 1.9 What runs

**On the capture host, the checker's** `fingerprint`, `number`, `refs`, `room`, `methods`, `scratch` and `reclaim`. **On the live host, the checker's** `host`, `geoblock`, `sshd`, `selftest`, `env`, `sdk-selftest` and `key`; **the engine's** `selftest` and `sdk-selftest` from the stage's copy; and **B-DEPLOY**, which runs the engine's `ready`, `prove`, `unit`, `clear-stop` and `status` from the installed copy and starts the unit. **Not run:** the checker's `page`, `wheels`, `secrets`, `bosskey`, `authorize`, `approve`, `revoke`, `ready`, `tg-probe`, `find-chat`, `roundtrip` and `tg-report` — the Boss's modes among them, which its self-tests still run at a real terminal (map §7 item 189).

### 1.10 What a PASS establishes, and what it does not

**PASS:** the unit's order path and its stop proved at the minimum size by its own code; its stop record holding a start under systemd; the unit enabled and running `900` s with no restart. **It establishes no income:** what the venue pays our address against the replay of the same days is L1's measurement, a TZ of its own fixed before its days, after the capture keeps them whole (map §7 items 175, 176 and 178).

---

## 2. Scope

TZ-52's §2 under R′ — and through it TZ-51's §2 — with these differences, each named against the item it changes, and nothing else allowed:

1. **The repository — TZ-51 §2 item 1.** The branch `tz-53-l1-unit` carries three files, each new: `engine/l1-bot.py`, `deploy/systemd/l1-bot.service` and `research/tz53-l1-account.py`. **Pull request #50 closed unmerged** by `gh api`, its branch kept. GitHub Pages is not read or touched. The staging script reads TZ-51's, TZ-52's and this file and `research/tz33-reward-book-capture.py` and `research/tz45-l0-rule-w.py` on `main`.
2. **The live host — TZ-51 §2 items 3 and 7.** *Written and kept — L1's unit:* `/root/l1-bot-svc/`, `0700`, and its four files, `0600`, and `/etc/systemd/system/l1-bot.service`, `0644`, by B-DEPLOY; under `/var/lib/l1-bot/`, by the engine's modes and the unit: `prove-N.json`, `unit-state.json`, `stop.json` and `stops/`, `journal/`, `select/`, `polls/`, and the unit's `service.log`. **Units — in place of TZ-51's "none":** `l1-bot.service` installed, started with the drill's stop record standing, then enabled and started, by B-DEPLOY — and stopped by it, `disable --now`, on a FAIL after its start; the transient `tz53-deploy.service`, B-DEPLOY's, which systemd collects at its end. **Removed:** `/var/lib/l1-bot/tz52-l1-account.py`, TZ-52's copy, which no stop runs, at its SHA-256 first (§3 step 12). **Nothing of `/etc/l1-bot/` is written**; `account.json` and TZ-51's copy for B-REVOKE are kept. *Written and removed:* `/root/tz53-work/**` by §9, and the engine's self-tests' `/tmp/l1-bot-selftest/` by themselves.
3. **The network — TZ-51 §2 item 4:** the requests of the header's authorization, in place of TZ-51's list. The checker's carry `User-Agent: btc-5m-twap-tz53`; **the engine's carry `btc-5m-twap-l1`**, its own, through its own requests and the client's.
4. **Prints and records — TZ-51 §2 item 5.** No address of either host; no key, token, relayer key, signature, address of the owner, wallet or session key, transaction hash, order id or chat id in any log or record of this run (G-PRINT; the prove's record, `SDK SELFTEST` check 12). **In place of TZ-51's "no price, size, side, book hash, rate, competitiveness or outcome of any book or market is read":** the unit reads the books, the reward documents and the selection to quote — the robot's work, which the reserve on the reward book's days does not bind (map §5) — and keeps them in its journal and stores on the host, `0600`; **no mode of this run and no report prints a price, size, rate, competitiveness or outcome of another participant on a reserved day:** the logs carry the unit's own orders and the wallet's own balances, a market by its slug and the day's selection by its counts. L1's measurement TZ fixes its gate before any of them is read.
5. **Money and keys — TZ-51 §2 item 6.** In place of TZ-51's one order: **the prove's orders, at most `5`, and the unit's orders by rule W, inside the wallet's balance and the unit's loss limit** (§1.2), each signed by the session key alone. No withdrawal, transfer, deposit, approval, authorization or revocation is made by any code of this run; the Boss's deposit is his own, on polymarket.com.
6. **No tmux server** is started or touched by this run (TZ-51 §2 item 2's `btc-l1` among them).

---

## 3. The work, in this order

Every step is TZ-52's under R′ — and through it TZ-51's — unless it says otherwise; its logs keep their names under R′. The new steps' logs:

| step | the capture host's logs | the live host's logs |
|---|---|---|
| §0.6 | — | `43-l1-before.log` |
| 9 | — | `57-engine-selftest.log`, `58-engine-sdk-selftest.log` |
| 10 | `59-deploy-start.log` | `60-deploy.log`, `61-ready-N.log` |
| 11 | — | `62-unit-after.log` |
| 12 | — | `81-keep.log` |

1. TZ-51 §0.0, the readiness and the work tree.
2. **§0.1 here**, `stage`, into `logs/01-stage.log`: six lines `created`.
3. TZ-51 §0.2 to §0.6, with TZ-52's and this file's differences: `fingerprint`, the host gate and `room`, the floors, `number` and `refs`, the access, the copy, `host before` with LS and `43-l1-before.log`, G-GEO, G-SSH and `methods`.
4. TZ-51 §3.1: the worktree's files written by **§0.1's script with the worktree and `branch` as its arguments** — three lines `created` — and `--numstat` exactly `29 0 deploy/systemd/l1-bot.service`, `3656 0 engine/l1-bot.py` and `3324 0 research/tz53-l1-account.py`; **pull request #50 in place of #48:** read first, `open`, `merged` `false`, head `1719ff46d22444aa7a4f05e7a735cfc4856240ab`, then closed by `gh api -X PATCH repos/seahomebatumi-ai/btc-5m-twap/pulls/50 -f state=closed`, read `closed`; found already closed, recorded and nothing closed; found merged, BLOCKED; where `gh` may not close it, TZ-51's B-PR48, for #50. The pull request of this TZ's branch is created.
5. TZ-51 §3.2: the checker's `SELFTEST PASS: 141 checks, 141 passed`, `refused by the hook: 5`, on both hosts.
6. TZ-51 §3.3, the scratch directories.
7. TZ-51 §3.4, **without its wheels and B-ENV:** `env`, `G-ENV installed PASS`, and the checker's `sdk-selftest`, `SDK SELFTEST PASS: 32 checks, 32 passed`, `refused by the hook: 2`.
8. TZ-51 §3.6: `G-KEY` reads the key present and kept. **TZ-51 §3.5, §3.7, §3.8 and §3.9 are not run.**
9. **E-SELF — the engine's self-tests**, on the live host, from the stage's copy: `LE selftest 57-engine-selftest` must print `SELFTEST PASS: 38 checks, 38 passed; refused by the hook: 0` and `LE sdk-selftest 58-engine-sdk-selftest` `SDK SELFTEST PASS: 29 checks, 29 passed; refused by the hook: 2`, each a check's own. Both reach no network but listeners of their own on `127.0.0.1`, write under `/tmp/l1-bot-selftest/` alone and remove it. Anything else is BLOCKED.
10. **B-DEPLOY — Appendix C, the Executor's first.** The Executor tells the Boss once, in one line in Russian: «Запускаю бота. Когда он напишет в Telegram «проверка кнопки «Стоп»», нажмите «Стоп» — у вас 30 минут». Then, into `59-deploy-start.log`:

```
R 'systemd-run --unit=tz53-deploy --collect -p RuntimeMaxSec=12600 /bin/bash /root/tz53-work/b-deploy.sh; echo "exit=$?"'
```

`exit=0`, the transient unit started. **Its paste**, where the classifier refuses it — one line on the capture host, as root: `ssh -T live-host 'export LC_ALL=C; systemd-run --unit=tz53-deploy --collect -p RuntimeMaxSec=12600 /bin/bash /root/tz53-work/b-deploy.sh; echo "exit=$?"'`. Either way the Executor reads `R 'tail -n 60 /root/tz53-work/logs/60-deploy.log'` at most every 570 s until its `B-DEPLOY END` line; **where a `61-ready-N.log` prints its capital check alone `FAIL`**, it tells the Boss once, in one line in Russian — «Пополните кошелёк бота: на нём должно быть от 80 до 150 pUSD, сейчас X» — X the pUSD on chain as that log prints it, and B-DEPLOY reads again every 600 s, 13 reads at most. **B-DEPLOY's steps, each gated on the one before it** (§4): the four files and the unit file installed and read at their SHA-256, `daemon-reload`; G-READY; G-PROVE, once for this code; G-HOLD — the unit started with the drill's stop record standing; `clear-stop`; `systemctl enable --now`, G-UNIT at `60` s; G-LIVE `900` s after the start. **`B-DEPLOY END exit=0` is G-DEPLOY PASS; `END exit=1` is BLOCKED** at the step its `FAIL at` line names — after G-UNIT's start, B-DEPLOY itself stopped the unit, `systemctl disable --now`, and printed its state. Then `R 'systemctl is-active tz53-deploy.service; echo "exit=$?"'` must not read `active`. A log that stops without its `END` line for `2,400` s — the drill's `1,800` and a read's `570` beside it — is read again once and then BLOCKED, and the Executor runs `R 'systemctl stop tz53-deploy.service; systemctl disable --now l1-bot.service; echo "exit=$?"'` — its paste the quoted part alone.
11. **The unit after**, into `62-unit-after.log`: `LU status 62-unit-after`, `LU 'unit after' 62-unit-after`, and `R 'cd /root/tz53-work && { date -u +%FT%T.%NZ; systemctl show l1-bot.service -p ActiveState -p SubState -p NRestarts -p MainPID -p UnitFileState -p ActiveEnterTimestamp; sha256sum /root/l1-bot-svc/* /etc/systemd/system/l1-bot.service; ls -la /root/l1-bot-svc /var/lib/l1-bot; tail -n 20 /var/lib/l1-bot/service.log; cat /var/lib/l1-bot/prove-*.json; } >> /root/tz53-work/logs/62-unit-after.log 2>&1; tail -n 60 /root/tz53-work/logs/62-unit-after.log'`: the unit `active`, `NRestarts` `0`, its files at §0.1's SHA-256, and the prove's record whole.
12. TZ-51 §3.10, **without its tmux step, and its item 3 replaced:** into `81-keep.log`, `R 'cd /root/tz53-work && { date -u +%FT%T.%NZ; sha256sum /var/lib/l1-bot/tz52-l1-account.py && rm /var/lib/l1-bot/tz52-l1-account.py; test -e /var/lib/l1-bot/tz52-l1-account.py; echo "exit=$?"; ls -la /etc/l1-bot /var/lib/l1-bot; } >> /root/tz53-work/logs/81-keep.log 2>&1; tail -n 30 /root/tz53-work/logs/81-keep.log'` — `a425e67cce7178e425b04f899ad245cf31a38848bd2553dfacdbbbcdf3a73366` and `exit=1`; its paste the quoted part alone. TZ-51's copy stays for B-REVOKE.
13. TZ-51 §9, then the report, §8.

---

## 4. Gates — fixed here, before any of their data exists

TZ-52's §4 under R′, with these differences:

- **Not read by this run:** G-PAGE, G-AUTH, G-APPROVE, G-ENV's wheels half, and TZ-51's G-READY, G-RT and G-TG (its §4.7, §4.8 and §4.10) — the engine's gates below read the account, the order path and the chat.
- **E-SELF** — §3 step 9: `38` of `38` and `29` of `29`, the refusals `0` and `2`.
- **G-INSTALL** — B-DEPLOY's step 2: the four files under `/root/l1-bot-svc/` and `/etc/systemd/system/l1-bot.service` at §0.1's SHA-256, the unit file equal to the code's copy by `cmp`; `LoadState` `loaded`, `UnitFileState` `disabled`.
- **G-READY** — §1.5's six checks, PASS, and G-GEO PASS: `G-READY PASS: 6 of 6, G-GEO PASS`.
- **G-PROVE** — §1.5: `G-PROVE PASS`, its eight gates each `PASS`, its record written; G-HB recorded.
- **G-HOLD** — the unit started with the drill's stop record standing, read `45` s on — past its `RestartSec`, `30` — `ExecMainStatus` `3`, `NRestarts` `0`, not `active` and not `activating`; the unit's own last lines `SERVE the stop record stands` and `… lookups 0, requests 0`: **the stop record holds a start, and the start made no request.**
- **G-CLEAR** — `clear-stop` exit `0`: the record moved into `stops/`, none standing.
- **G-UNIT** — `60` s after `enable --now`: `ActiveState` `active`, `NRestarts` `0`, `UnitFileState` `enabled`, and the unit's line `SERVE start: geoblock PASS`.
- **G-LIVE** — `900` s after the start: `active`, `NRestarts` `0`, the same `MainPID`, no stop record.
- **G-DEPLOY** — `B-DEPLOY END exit=0`: G-INSTALL to G-LIVE, each PASS.
- **G-PRINT** — TZ-51 §4.9, over every log of both hosts.
- **The stops — CANON hard rule 14.** This TZ deploys a unit that outlives it. **Its restart policy:** `Restart=on-failure`, `RestartSec=30`, **`RestartPreventExitStatus=2 3`** — a refusal and a stop are never started again; an error is, five times in an hour at most (`StartLimitBurst=5`). **Its stops, by who reaches them:** «Стоп» in the pinned chat, the Boss's; **`systemctl disable --now l1-bot.service`** on the live host — SIGTERM: every open order cancelled, exit `0`, no restart, no stop record — **authorized on every FAIL of G-UNIT and G-LIVE and performed by B-DEPLOY itself**, its state printed after it; before G-UNIT the unit never ran. **And the last stop of every order path, the Boss's and not run by this TZ:** **B-REVOKE**, TZ-51 §4.11's line word for word with TZ-51's copy, and **withdraw** on polymarket.com, which needs no host. Each stop is verified from the unit's own record and `systemctl show`.

---

## 5. The files

- **`engine/l1-bot.py`**, Appendix A — 3,656 lines, 188,968 bytes, `98851b3c0df447ed7c846edfbf18b9ea1611d12228a4d9a3c1fda3b4f22da214`. Its modes: `serve`, `ready`, `prove`, `clear-stop`, `status`, `unit LABEL`, `selftest`, `sdk-selftest`; it refuses `-O`. **Measured by the Architect on these bytes under Python 3.12.3 against his build of `/root/l1-env` by TZ-50's command:** `SELFTEST PASS: 38 checks, 38 passed; refused by the hook: 0` in `0.5` s; `SDK SELFTEST PASS: 29 checks, 29 passed; refused by the hook: 2` in `18.8` to `19.0` s, three runs of each; **and on two copies with a defect put in, `sdk-selftest` FAILS** — with the position cap's `<` made `<=`, at `the bid filled: the cap holds the bid back, the ask sells the 20 shares held at 0.40`; with the touch read without taking the unit's own orders out, at `the unit live to the Boss's «Стоп»: exit 3, the record written, no order left`.
- **`deploy/systemd/l1-bot.service`**, Appendix B — 29 lines, 1,014 bytes, `a6305d0e7a220ea88f5a4d2be612cac35f3dbe527d7c3b7ed12fd7c47f956266`: `Type=simple`; `ExecStart=/root/l1-env/bin/python -B -u /root/l1-bot-svc/l1-bot.py serve` in `/root/l1-bot-svc`; `Restart=on-failure`, `RestartSec=30`, `RestartPreventExitStatus=2 3`, `StartLimitIntervalSec=3600`, `StartLimitBurst=5`; `MemoryMax=384M`; `NoNewPrivileges=yes`, `PrivateTmp=yes`, `ProtectSystem=strict` with `ReadWritePaths=/var/lib/l1-bot`; output appended to `/var/lib/l1-bot/service.log`. `systemd-analyze verify` reads it clean but for the interpreter absent from the Architect's host.
- **`b-deploy.sh`**, Appendix C — 135 lines, 6,789 bytes, `373df4093b4ba4ad4fd093a173ad4c5396a52e2231b789814aef99ca23acf069`; `bash -n` and `shellcheck` clean; **rehearsed by the Architect on a stand-in host** — `systemctl`, the engine and `sleep` stand-ins over a temporary tree — in seven cases: a clean run `END exit=0`; the capital outside its bounds for two reads, `END exit=0` at the third; for thirteen, `FAIL at G-READY, read 13`; the prove failing, `FAIL at G-PROVE`; the unit restarted after a stop, `FAIL at G-HOLD`; no start line, `FAIL at G-UNIT: the unit's start line` and the unit disabled; a second run while the unit runs, nothing installed and G-LIVE read.
- **`research/tz53-l1-account.py`**, the checker — TZ-52's instrument changed by §0.1's edits alone: its names under R′, `MAP_REVISION`, its docstring. Every line number TZ-51 cites is TZ-51's Appendix A's; this TZ cites none of the new file's. Measured on these bytes: `SELFTEST PASS: 141 checks, 141 passed; refused by the hook: 5` and `SDK SELFTEST PASS: 32 checks, 32 passed; refused by the hook: 2`.

## 6. Cost

**Compute:** the checker's modes as TZ-52 §6; the engine's `selftest` `0.5` s and `sdk-selftest` under `20` s; §0.1's script under `1` s over TZ-52's and this file. No check reaches `3,600` s of compute. **Waits:** G-READY `7,200` s at most; G-PROVE about `120` s and the Boss's «Стоп» `1,800` s at most; G-HOLD `45` s; G-UNIT `60` s; G-LIVE to `900` s after the start — under the transient unit's `RuntimeMaxSec`, `12,600` s. **The unit:** its memory capped at `384M`, the engine's largest self-test peak `113,111,040` bytes; its disk about the reward book's other files', `14.6` MB a day for 150 members (map §2.6), for its candidates' polls and its selection [modelled] — it stops itself at `2,447,483,648` bytes available on `/`, read every `3,600` s, `16,913,440,768` at TZ-52's read; its requests about one a second — open orders every `3` s, heartbeats every `5` s, a candidate's reward document every `300` s each.

## 7. Validation

- **V1** — `FINGERPRINT PASS` at §0.2 and TZ-51 §3.1, as §0.2 here. Asserted.
- **V2** — `NUMBER PASS - 2 of 2`; refs by kind; the branch absent before the push. Asserted.
- **V3** — §0.1's script: six lines `created` into the stage, three into the worktree, every SHA-256 its table's; the live host's copies the same. Asserted.
- **V4** — the branch: three paths, `--numstat` `29 0`, `3656 0` and `3324 0`; pull request #50 read and closed unmerged, or found closed. Asserted.
- **V5** — the capture host gate, seven checks; the room and its margin printed. Asserted.
- **V6** — the access, as TZ-51's V6. Asserted.
- **V7** — the live host gate, five checks, at `host before` and `host after`; LS and `43-l1-before.log` as §0.6 here. Asserted.
- **V8** — `G-GEO PASS` at §0.6, and in G-READY and G-PROVE. Asserted.
- **V9** — `G-SSH` K1 to K6 at §0.6 and TZ-51 §3.10. Asserted at §0.6.
- **V10** — the checker's `SELFTEST PASS: 141 checks, 141 passed`, `refused by the hook: 5`, on both hosts; `SDK SELFTEST PASS: 32 checks, 32 passed`, `refused by the hook: 2`. Asserted.
- **V11** — the scratch directories, and `RECLAIM PASS` where any was reclaimed. Asserted where it runs.
- **V12** — `G-ENV installed PASS`, its files line. Asserted.
- **V13** — `G-KEY`: present and kept. Asserted.
- **V14** — E-SELF: `38` of `38`, refused `0`; `29` of `29`, refused `2`. Asserted.
- **V15** — G-INSTALL and G-READY: every line of `60-deploy.log` to them and every `61-ready-N.log`, the balance and the allowances as printed. Asserted.
- **V16** — G-PROVE: every `PROVE` line — G-RT's placements, reads, cancellation and balances by kind, G-HB, G-STOP's press after its seconds — and the record's path and bytes. Asserted.
- **V17** — G-HOLD, G-CLEAR, G-UNIT and G-LIVE: each read of the unit with its instant, its own lines, and `B-DEPLOY END exit=0`. Asserted.
- **V18** — §3 step 11: the unit `active`, `NRestarts` `0`, its files at §0.1's SHA-256; `status`'s lines. Asserted.
- **V19** — G-PRINT: `0` and `0`. Asserted.
- **V20** — TZ-51 §3.10 without its tmux step: `81-keep.log`'s SHA-256 and `exit=1`; `scp exit=0` and `diff exit=0`; the capture host's units as at §0.3; contract §4.2's self-check. Asserted.
- **V21** — every mode's printed peak — the checker's standard-library modes each under `43,213,417`, its client modes and the engine's each under `137,458,839`. Recorded.
- **V22** — TZ-51 §9 under R′. Asserted.

## 8. The report

`CryptoReports/TZ-53-l1-unit-report.md`, as TZ-51 §8 and contract §8. **Its §2 quotes `60-deploy.log` whole, every `61-ready-N.log`, and the prove's record whole** (CANON hard rule 16) — it carries no address, key or order id (`SDK SELFTEST` check 12) — and every refusal's line. **It names the unit's state at its end and its stops**, as §4 fixes them. **A departure from this file is named in its own item** — and no request to a venue outside the modes of §1.9 is one this TZ allows.

## 9. Reclaim

TZ-51 §9 under R′ — **with the live host's unit kept:** `/root/l1-bot-svc/`, `/etc/systemd/system/l1-bot.service` and `/var/lib/l1-bot/` are L1's deployment, not this run's scratch; `B-RECLAIM-LIVE` removes `/root/tz53-work` alone.

---

## 10. Pre-send checks

Performed by the Architect on 2026-11-21 against this file, start to end, in a reading separate from its writing. Every committed file was read at `origin/main` `dc0b34e`; the staged files at §0.1's SHA-256, produced by §0.1's script — run as the Executor runs it, from this file in a copy of `main` with this revision — into a stage and a worktree; the venue's client at TZ-51's set's SHA-256, `polymarket_client-0.20.0-py3-none-any.whl`.

| # | check | result |
|---|---|---|
| **C1** | scope against body | **Named by the body, each inside §2 or TZ-51's §2 under R and R′.** *Repository, written:* the branch's three files, the report on `main`, pull request #50 closed unmerged and this TZ's own opened — §2 item 1. *Repository, read:* TZ-51's, TZ-52's and this file, `research/tz33-reward-book-capture.py` and `research/tz45-l0-rule-w.py` by §0.1's script — §2 item 1; `SYSTEM-MAP.md`, its 67 rows' files and `docs/l1-sign.html` by `fingerprint`; `CryptoTZ/` and `CryptoReports/` by `number`; `origin`'s refs by `refs` and TZ-51 §3.1's `ls-remote`; pull request #50 by `gh api`. *Capture host, written:* `/root/tz53-work/**`, the forensic store's copies by `reclaim`, earlier session directories by B-RECLAIM-SCRATCH — TZ-51 §2 items 2 and 7; no tmux server — §2 item 6. *Live host, written:* `/root/tz53-work/**`, removed by §9; `/root/l1-bot-svc/`, `/etc/systemd/system/l1-bot.service`, `/var/lib/l1-bot/`'s records and the units `l1-bot.service` and `tz53-deploy.service` — §2 item 2; `/var/lib/l1-bot/tz52-l1-account.py` removed — §2 item 2; `/tmp/l1-bot-selftest/` — §2 item 2. *Live host, read:* `/etc/l1-bot/`'s `session-key`, `telegram-token` and `chat-id` and `account.json` by the engine's modes, never printed — TZ-51 §2 item 3 under R and R′. *Network:* the header's authorization — §2 item 3. **By content class, and each intersection exempted by name:** TZ-51 §2 item 3's "*Units:* none started, stopped, enabled or edited" against B-DEPLOY's units — §2 item 2; its `/var/lib/l1-bot/` list against the unit's records — §2 item 2; TZ-52 §2 item 2's "nothing of L1's is removed" against TZ-52's copy removed — §2 item 2; TZ-51 §2 item 4's list and agent against the engine's requests and `btc-5m-twap-l1` — §2 item 3; TZ-51 §2 item 5's "no price, size, side, book hash, rate, competitiveness or outcome of any book or market is read or printed" against the unit, which reads them to quote — §2 item 4, which keeps every print to the unit's own orders and balances, slugs and counts; TZ-51 §2 item 6's one order against the prove's and the unit's — §2 item 5. **The outputs that carry a class:** the prove's record and `PROVE` lines carry the prove's own orders, at the lowest price their tick allows, the wallet's balances and allowances, slugs and counts; `status` prints counts and the start equity; `serve` prints its start and end lines and an error's trace masked — no fill, touch or rate. |
| **C2** | origin of every expectation | **Every fixed literal of §0, §1, §3, §4, §5 and §7, of two kinds and no third.** *Quoted from a committed artifact, named:* revision `2026-11-21-c`, the anchors and rows `67` = `64` + `2` + `1` (map §0, its table unchanged from `2026-11-21-b`'s); the nine `PATH` lines (TZ-52's report §2.4, `79-host-after.log`, line for line, the last under R′); `43-l1-before.log`'s three names (TZ-52's report §2.4, `81-keep.log`'s listing) and the unit absent (map §6, live host: "no unit"); PR #50's head `1719ff46d22444aa7a4f05e7a735cfc4856240ab` (`git ls-remote` on 2026-11-21: `refs/pull/50/head` and the branch, `refs/pull/50/merge` present, the pull request open); the base's lines, bytes and SHA-256 (TZ-52 §0.1's table); the frozen files' (map §0's rows); the floors and their modelled host peaks (TZ-51 §0.4; the checker's lines 291 to 298); `202` refs (map §1); `16,913,440,768` (TZ-52's report §2.4); `14.6` MB a day (map §7 item 175); `RestartSec` `30` and `RestartPreventExitStatus` `2 3` (Appendix B). *Computed by an implementation independent of the one under test:* every file's lines, bytes and SHA-256 by `wc` and `sha256sum`, and `--numstat`'s by `wc -l`. *Counted on the Architect's runs, which run on literals and stand-ins of their own:* `38` and `0`, `29` and `2` — the engine's self-tests' `ok` calls and the hook's refusals — and `141` and `5`, `32` and `2`, the checker's, TZ-52's; the two mutations' FAILs; B-DEPLOY's seven rehearsed outcomes. *Measured by the kernel:* the peaks of §0.4 here. **No expectation depends on a quantity this TZ measures:** the capital's bounds, the loss limit and G-HOLD's exit `3` are this TZ's constants, read as inequalities and equalities against them. |
| **C3** | shape of every diff | **Three files, each new:** `engine/l1-bot.py`, `deploy/systemd/l1-bot.service` and `research/tz53-l1-account.py` are absent from `origin/main` (`git cat-file -e` exit `128`, each): `3656`, `29` and `3324` lines added and `0` removed. `SYSTEM-MAP.md` is replaced by its revision in the Boss's upload — `23` lines of `2026-11-21-b` replaced by `28`, no row of its table among them — with this file, absent from `origin/main` too (exit `128`). The report is new. |
| **C4** | cost of every check | **Compute, measured on these bytes:** the engine's `selftest` `0.5` s and `sdk-selftest` `18.8` to `19.0` s; the checker's `selftest` `0.66` s and `sdk-selftest` under `20` s, as TZ-52 §10 C4; §0.1's script `0.05` s over TZ-51's `322,047`-byte and TZ-52's and this file. **No check reaches `3,600` s of compute.** **Waits, at their upper bounds:** G-READY's `13` reads, `12` waits of `600` s — `7,200` s; G-PROVE about `120` s beside the drill's `1,800`; G-HOLD `45`; G-UNIT `60`; G-LIVE `900` from the start — `10,125` s and the reads' own, under the transient unit's `RuntimeMaxSec`, `12,600`. **Fail-fast bounds:** the Executor's read of `60-deploy.log` every `570` s, under the session's `600` s; a log silent `2,400` s — the drill's `1,800` and a read's `570`, with `30` to spare — read once more, then BLOCKED. The prove's orders at their bound, `5`; G-RT's kinds at theirs, `3`. |
| **C5** | every count | V1: `67 = 64 + 2 + 1` over map §0's table of `2026-11-21-c`, counted by the Architect's own parse of its state column — `64` `frozen`, `2` `tracked`, `1` `reported` — and by the checker's `fingerprint` on his copy of `main`: `FINGERPRINT PASS: revision 2026-11-21-c; anchors 6 of 6, 4 re-derived; rows 67: frozen 64 of 64 equal, tracked 2, reported 1; …`. V2: `2 of 2`, by `number` on the same copy. V3: `6` over §0.1's `FILES["stage"]`, `3` over `FILES["branch"]`. V4: `3` paths. V5: `7`, TZ-51's. V7: `5` over `live_gate`'s keys; LS's `9` lines over `host`'s list; `3` names. V9: `6`. V10: `141` and `32`. V14: `38` and `29`, the `ok` calls the engine's self-tests executed at each of the Architect's three runs. G-READY: `6` — `ready_checks`' five and, at a first start, the capital's. G-PROVE: `8` over `prove_flow`'s `rec["pass"]` tuple. §0.1: `7` edits on TZ-52's `24`. B-DEPLOY: `7` rehearsed cases. §5: `2` mutations. §7: `22` items. |
| **C6** | every population | G-READY: the account's reads at each of B-DEPLOY's reads, `13` at most. G-SELECT: the day's members at the prove's instant. G-RT: each kind among the day's candidates at that instant, `3` at most. G-WS: one first token of a picked candidate per kind. G-HOLD: the one start with the drill's record standing. G-UNIT and G-LIVE: the unit's first `60` and `900` s. The peaks: the Architect's runs under Python 3.12.3 against his build of `/root/l1-env` by TZ-50's command — the engine's `selftest` and `sdk-selftest` three each, the checker's `selftest` three and `sdk-selftest` two. The mutations: one run of `sdk-selftest` each. The rehearsal: B-DEPLOY under stand-ins, seven runs. |
| **C7** | every signature and every behaviour | **Committed, read at `dc0b34e`:** `research/tz45-l0-rule-w.py` line 953, `def w_targets(bb, ba, tick, vu):`, its returns `return None, None` (lines 960 and 964) and `return tb, ta` (line 965), and lines 121 to 125, `CAP_CLIPS = 1`, `W_MS_MAX = 2000`, `W_COMP_MAX = Fr(1)`, `W_BAND = (9, 10)`, `W_INSIDE_MAX = 100`; `research/tz33-reward-book-capture.py` line 929, `def run_rule(fetch, d0, k=SET_SIZE, walk_max=WALK_MAX):`, with `END_MIN_S = 15 * DAY` (line 148) and `SELECT_LEAD_S = 900` (line 163); TZ-52 §0.1's script — `path = os.path.join(DEST, "research/tz52-l1-account.py")` and `assert hashlib.sha256(data).hexdigest() == WANT, "the patched instrument"` — so its scratch output is TZ-52's instrument, asserted. **The checker:** `mode_fingerprint` — `assert is_capture_host(), "BLOCKED: fingerprint runs on the capture host"`, `is_capture_host` — `return os.path.isdir(CAPTURE_MARK)`; `PYFILE` used by the usage line alone. **This file's code, every behaviour §1 and §4 attribute to it, read in Appendix A:** `mode_serve` — `if st is not None:` … `return STOP_EXIT` before any request, then `prove = proved(paths, SELF_SHA)`, `if prove is None:` … `return REFUSE_EXIT`; `ready_checks` — five checks and `if first:` the capital's, `CAPITAL_MIN <= f["cash"] <= CAPITAL_MAX`; `Unit.candidates` — `m.member and m.kind in self.kinds and m.ms <= self.W.W_MS_MAX and (m.min_order is None or m.ms >= m.min_order)`; `equity_of` — `sets * 1000 * 10 + (m.yes - sets) * (bb or 0) * 10 + (m.no - sets) * ((1000 - ba) if ba is not None else 0) * 10`; `prove_flow` — `rec["pass"] = all(g.get(n) is True for n in ("G-GEO", "G-READY", "G-TG", "G-SELECT", "G-POLL", "G-WS", "G-RT", "G-STOP"))`, and its record written in `finally` on every exit; `mode_prove` — `assert len(earlier) < 3` and `assert proved(paths, SELF_SHA) is None`; `Unit.run` — `code = {"term": TERM_EXIT, "error": ERROR_EXIT}.get(self.reason, STOP_EXIT)`; `mode_unit` — the installed file against `os.path.join(os.path.dirname(os.path.abspath(__file__)), UNIT)`, so B-DEPLOY installs the unit file beside the code as well; `clear_stop` — `stop-<at>.json`, a second stop of the same second `stop-<at>-2.json`. **The venue's client `0.20.0`,** as the engine calls it and its stand-in answers it: `list_wallet_open_orders(signer_addresses=…)`, `cancel_order(order_id=…)`, `cancel_orders(order_ids=…)`, `cancel_all()`, `send_order_heartbeat(heartbeat_id=…)`, `get_balance_allowance(asset_type=…, asset_id=…)`, `get_closed_only_mode()`, `get_total_earnings_for_user_for_day(date=…)`, `get_current_rebates(date=…, maker_address=…)`. |
| **C8** | every cross-reference | **Map, revision `2026-11-21-c` — the sections, rows and items this run rests on, which the header copies from here (map §7 item 174):** §0, the fingerprint gate, its table and the signing page; §1, the repository, its TZs and pull request #50; §2.6, the reward book — its selection, its store's bounds and its reserve; §3, the units, the trees on the host and the session directories; §5, L1's row and the reward book's days; §6, its rows host identity, for TZ host gates; live host; live host identity, for TZ host gates; live host — the venue's geoblock, measured 2026-11-19, TZ-48 and TZ-49, and 2026-11-20, TZ-50; live host — the venue's CLOB from Sofia; language; git remote; egress; venue edge — the `User-Agent`; venue constants; maker incentives; disk; disk floors and caps; process supervision; memory; clock; sandbox limit — destructive actions; and harness — background output; §7 items 86, 89, 91, 95, 98, 119, 124, 127, 132, 137, 138, 140, 143, 144, 150, 156, 163, 164, 169, 171, 172, 174, 175, 176, 177, 180, 181, 183, 184, 185, 186, 187, 189, 190, 191 and 192; §8. Each read in full, an item's disposition column included, each §6 row found by its first cell. **The duties items leave to the Architect "before" a step** (CANON PART VI, the fifth rule): item 186 — the read before L1's unit TZ, re-scoped to the measurement's and discharged for the unit, §1.6; item 190 — the loss limit fixed and CANON PART IV revised, §1.2 and §1.8; item 192 — the unit's read-back, §1.4 and §1.5; item 184 — the stop's round trip before rule W quotes, G-STOP; item 187 — no rebate counted unpaid, §1.7; item 191 — the refusal's path named, §1.4; item 185 — `LC_ALL=C` in `R`, B-DEPLOY and the unit's `Environment`; item 189 — the Boss's modes not run, §1.9; items 175, 176 and 178 — before L1's measurement days, §1.10; item 172 — TZ-33's rule, unchanged, leaves a market by its end date and tags; item 171 — the unit's money in integers of `10⁻⁶` pUSD, exact; item 163 — `assert_live` refuses the capture host. **TZ-52's file:** §0.0, §0.1's delimiter lines, §0.2 to §0.6, §2 items 1 and 2, §3 steps 1 to 14, §4 and §6 — resolved to their headings and lines. **TZ-51's file:** §0.0, §0.2 to §0.6, §2 items 1 to 7, §3.1 to §3.6, §3.10, §4.7 to §4.11, §8 and §9 — resolved to their headings; its B-PR48 in §3.1. **TZ-52's report:** §1 and §2.4. **TZ-45:** §1. **The Executor contract**, `A4` `6ac6e10aeabc`: §1, §4.2, §5, §8 and §10. **CANON** PART II, L1's row; PART III, hard rules 2, 4 to 6, 8, 10 and 13 to 17; PART IV; PART VI, the fifth rule. **This file's own sections**, each `§` resolved to its heading. **The Boss's words:** none quoted. |

**Not performable in the session that wrote this TZ, and converted into conditions the run evaluates** (CANON hard rule 13): **(1)** that the live host stands as TZ-52 left it — the Architect cannot read that host: LS and `43-l1-before.log` BLOCK otherwise (§0.6); **(2)** that the venue takes and serves the unit's order path, its heartbeat and its market channel from the live host — G-PROVE reads them, and §1.4 fixes the run's path on a refusal; **(3)** the Boss's deposit — G-READY's capital check, read `13` times at most; **(4)** the Boss's «Стоп» — G-STOP, `1,800` s, else G-PROVE FAIL and B-DEPLOY ends; **(5)** that systemd on the live host keeps the unit down on exit `3` and runs the transient unit — G-HOLD and B-DEPLOY's own reads; the Architect's `systemd-analyze verify` ran on a host without the interpreter, and B-DEPLOY was rehearsed under stand-ins alone; **(6)** that `gh` may close pull request #50 — TZ-51's B-PR48, for #50; **(7)** the engine's self-tests on the live host — E-SELF.

---

## Appendix A — the unit, byte for byte

### `engine/l1-bot.py`

```python file=engine/l1-bot.py
#!/usr/bin/env python3
"""L1's unit - rule W live at the minimum size, from the live host in Sofia (CANON PART II, L1; TZ-53).

The bot's Deposit Wallet is the Boss's, its owner key in his MetaMask. The live host holds the session key TZ-50 made
and TZ-51 had the owner authorize: scope CLOB, it signs orders for the wallet and cannot withdraw. The wallet's
allowances to the venue's exchanges are the venue's maximum, the one amount its relayer approves (map section 7 item
190), so what the key could spend is the wallet's balance: the Boss keeps on it what he entrusts to L1, and this unit
stops itself LOSS_LIMIT below its start equity, marked at the touch.

    serve          the unit, as systemd runs it: on each UTC day's selection - TZ-33's rule - rule W on at most
                   N_QUOTE markets at a time, each quote of the market's minimum scoring size; its books from the
                   CLOB's market channel, its terms from the market's reward document every POLL_S; its orders
                   known by the wallet's open orders read by its key, its fills by its trades and its balances,
                   never by a read by id alone (map section 7 item 192); order heartbeats every HB_S where the
                   prove read them accepted; reports and the one command that acts, «Стоп», in the Boss's
                   pinned Telegram chat. It stops - every open order of its key cancelled, a stop record that holds
                   across restarts and boots, exit 3 - on «Стоп», on the loss limit, on a geoblock read of blocked,
                   on the disk floor and on an equity it cannot read for EQUITY_UNREAD_S.
    ready          G-READY: the account read through the session key; exit 4 on FAIL
    prove          G-PROVE: the unit's own request path, one live request per endpoint, before the unit starts -
                   the geoblock, Telegram, the day's selection, a reward poll, a stream session; on each kind of
                   exchange the day's markets use, one order placed, seen in the wallet's open orders, cancelled
                   by its id, seen gone, the balance unchanged; the order heartbeat's own cancellation; and the
                   stop's round trip - an order resting, the Boss's «Стоп», every order cancelled, the stop record
                   written. Its record is prove-N.json; exit 4 on FAIL
    clear-stop     the stop record moved into the stop history, the chat's pending commands consumed: the one way
                   the unit starts again after a stop
    status         the unit's own records, counts and instants alone
    unit LABEL     the unit as systemd holds it: its file, its state, its exits
    selftest       every rule of this file that needs no venue client, on literals and temporary trees
    sdk-selftest   the unit's flows through the venue's client against loopback stand-ins of the venue and Telegram

Rule W is TZ-45's: its targets are tz45-l0-rule-w.py's own w_targets and its constants, its selection TZ-33's own
run_rule and its helpers, each taken by name from its frozen file beside this one, by that file's SHA-256 - nothing
else of either file runs (load_frozen). IPv4 alone (map section 7 item 181): every lookup asks AF_INET, every network
socket is AF_INET, the audit hook refusing any other. No mode prints a key, a token, an address, an order's id, a
transaction hash or a chat's id; serve's journal under /var/lib/l1-bot, 0600, holds its own orders and the touches it
decided on, and no TZ's mode prints them before L1's measurement fixes its gate.

Written for CryptoTZ/TZ-53-l1-unit.md. The TZ is the specification.
"""

import ast
import asyncio
import builtins
import collections
import datetime
import decimal
import fractions
import gzip
import hashlib
import json
import os
import re
import resource
import signal
import socket
import subprocess
import sys
import time
import traceback
import types
import urllib.parse

if not __debug__:
    sys.stderr.write("l1-bot: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(2)

D = decimal.Decimal
Fr = fractions.Fraction
PYFILE = "l1-bot.py"

# ---- where it lives ---------------------------------------------------------------------------------------------

SVC = "/root/l1-bot-svc"                 # this file and the two frozen files it takes rules from
L1_ETC = "/etc/l1-bot"                   # the session key, the bot's token and the pinned chat: read, never written
L1_VAR = "/var/lib/l1-bot"               # the account record, the prove records, the unit's state, journal and stop
L1_ENV = "/root/l1-env"                  # polymarket-client 0.20.0 at its pins (TZ-50, TZ-51)
UNIT = "l1-bot.service"
UNIT_FILE = "/etc/systemd/system/" + UNIT
CAPTURE_MARK = "/var/lib/btc-recorder"   # the capture host's identity (map section 6): never this unit's host
LIVE_HOSTNAME = "vs-2348"                # the live host's name, its first label (map section 7 item 180)
LIVE_HOST_KEY = ("ssh-ed25519", "SHA256:Y14Iy6okVrEz76M/JsR9hLre/54PtMAGXd6ZKDe4ZJw")
HOST_KEY_DIR = "/etc/ssh"
PROTECTED = ("/var/lib/btc-recorder", "/var/lib/btc-chainbook", "/var/lib/btc-pairbook", "/var/lib/btc-rewardbook",
             "/var/lib/btc-rewardbook-archive", "/var/lib/btc-pairbook-archive", "/var/lib/adv3-bot", "/etc/adv3-bot")

FROZEN = {"tz33": ("tz33-reward-book-capture.py",
                   "a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670"),
          "tz45": ("tz45-l0-rule-w.py",
                   "4720e78573e54b1325dd24af7c30e0de59bfb4c1879d309a23fa6bab6b32d2d4")}


class Paths:
    """Every path the unit reads or writes; the self-tests build one over a temporary tree."""

    def __init__(self, etc=L1_ETC, var=L1_VAR, svc=SVC):
        self.etc, self.var, self.svc = etc, var, svc
        self.key, self.token, self.chat = etc + "/session-key", etc + "/telegram-token", etc + "/chat-id"
        self.account = var + "/account.json"
        self.state = var + "/unit-state.json"
        self.stop = var + "/stop.json"
        self.stops = var + "/stops"
        self.journal = var + "/journal"
        self.select = var + "/select"
        self.polls = var + "/polls"


P = Paths()

# ---- the venue ---------------------------------------------------------------------------------------------------

UA = "btc-5m-twap-l1"
GEO_HOST, GEO_PATH = "polymarket.com", "/api/geoblock"
CLOB_HOST = "clob.polymarket.com"
GAMMA_HOST = "gamma-api.polymarket.com"
WS_HOST = "ws-subscriptions-clob.polymarket.com"
RELAYER_HOST = "relayer-v2.polymarket.com"
RPC_HOST = "polygon.drpc.org"
TG_HOST = "api.telegram.org"
ORIGINS = {"geo": "https://" + GEO_HOST, "clob": "https://" + CLOB_HOST, "gamma": "https://" + GAMMA_HOST,
           "ws": "wss://" + WS_HOST, "rpc": "https://" + RPC_HOST, "tg": "https://" + TG_HOST}
TIMEOUT_S = 15
SDK_DIST, SDK_VERSION = "polymarket-client", "0.20.0"
CHAIN_ID = 137
PUSD = "0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB"              # the client's collateral_token
CTF = "0x4D97DCd97eC945f40cF65F87097ACe5EA0476045"               # conditional_tokens: a CTF market's positions
POSITIONS = "0x006F54F7f9A22e0000CC2AB60031000000ae9fEF"         # position_manager: a Protocol V2 market's
EXCHANGES = {"c": "0xE111180000d2663C0091e4f400237545B87B996B",  # standard_exchange
             "n": "0xe2222d279d744050d28e00520010520000310F59",  # neg_risk_exchange
             "v": "0xe3333700cA9d93003F00f0F71f8515005F6c00Aa"}  # exchange_v3
KIND_NAMES = {"c": "CTF", "n": "CTF negative-risk", "v": "Protocol V2"}
POSITION_TOKEN = {"c": CTF, "n": CTF, "v": POSITIONS}
V2_RESERVED = ((1 << 64) - 1) << 40     # the client's _V2_RESERVED_BITS_MASK: all zero in a V2 position ID
SEL = {"balanceOf": "70a08231", "allowance": "dd62ed3e", "isApprovedForAll": "e985e9c5"}
MAX_READ = 1 << 255                     # an allowance at or above it reads max: the venue's MaxUint256
UNITS = 1000000                         # pUSD and positions in six-decimal units

# ---- L1's terms: TZ-53 section 1 ---------------------------------------------------------------------------------

N_QUOTE = 4                    # markets quoted at once
N_HOLD = 8                     # markets holding a position at once: no new market is quoted beyond it
LOSS_LIMIT = 25000000          # 25 pUSD: the unit stops where its equity falls this far below its start equity
CAPITAL_MIN = 80000000         # G-READY: the wallet's pUSD on chain at least 80 pUSD ...
CAPITAL_MAX = 150000000        # ... and at most 150: the most a stolen session key could spend (CANON PART IV)
CASH_KEEP = 1000000            # 1 pUSD the unit's buys leave unreserved
KEY_DAYS_MIN = 7               # the session key's authorization valid this long at least at a start
PROVE_ORDERS_MAX = 5           # the prove's orders: three on the first kind, one on each other
PROVE_PRICE_TICKS = 1          # each at the lowest price its market's tick allows
PROVE_RECORD = re.compile(r"prove-([123])\.json")


class Cfg:
    """The unit's clock, in seconds; the self-tests shorten it."""
    hb_s = 5.0                  # an order heartbeat every 5 s (the venue: cancel-all 10 s after the last accepted)
    hb_late_s = 12.0            # no accepted heartbeat for this long: the unit reads its orders gone
    reconcile_s = 3.0           # the wallet's open orders read
    quote_s = 0.25              # a market whose book moved is decided again
    full_s = 5.0                # every market decided again
    poll_s = 300.0              # each candidate's reward document, as the reward book polls it
    guard_s = 30.0              # the equity read
    geo_s = 900.0               # the geoblock read
    disk_s = 3600.0             # the disk read
    dwell_s = 3.0               # an order lives this long before a moved target replaces it
    ghost_s = 2.0               # an order of ours that left the book stays taken out of its level this long
    gone_after_s = 5.0          # an order of ours absent from two reads this long after its placement is gone
    pause_s = 15.0              # a market after a fill: its other orders cancelled, its balances read again
    blind_s = 5.0               # the stream down this long: every order cancelled until its books are seeded again
    silence_s = 60.0            # no frame this long: the stream reconnected
    ping_s = 10.0               # the market channel's text PING
    backoff_s = (1, 2, 4, 8)
    tg_poll_s = 25              # Telegram's long poll
    tg_gap_s = 1.0              # between two messages sent
    select_lead_s = 900         # the next day's selection from D0 - 900 s, as the reward book's (TZ-33)
    select_retry_s = 60
    report_at_s = 4500          # the day's report at 01:15 UTC, after the venue's payouts
    equity_unread_s = 900       # no equity read this long: stop
    loss_confirm_s = 30.0       # the loss limit read breached this long, two guard reads apart, before it stops
    seen_reads, seen_gap_s = 10, 1.0
    hb_wait_s = 40.0            # the prove waits this long for the heartbeat's own cancellation
    tg_wait_s = 1800.0          # the prove waits this long for the Boss's «Стоп»
    stop_reads = 10


C = Cfg()

# ---- the audit hook: TZ-53 section 2 as a pure function ------------------------------------------------------------

MODE = [None]
REFUSED = []
RESOLVED = set()
COUNTS = {"lookups": 0, "requests": 0}
NET = {"serve": (GEO_HOST, CLOB_HOST, GAMMA_HOST, WS_HOST, RELAYER_HOST, RPC_HOST, TG_HOST),
       "prove": (GEO_HOST, CLOB_HOST, GAMMA_HOST, WS_HOST, RELAYER_HOST, RPC_HOST, TG_HOST),
       "ready": (GEO_HOST, CLOB_HOST, RELAYER_HOST, RPC_HOST),
       "clear-stop": (TG_HOST,), "status": (), "unit": (),
       "selftest": ("127.0.0.1",), "sdk-selftest": ("127.0.0.1",)}
EXECS = {"serve": ("file", "timedatectl"), "prove": ("file", "timedatectl"), "ready": ("file", "timedatectl"),
         "clear-stop": (), "status": (), "unit": ("systemctl",), "selftest": (), "sdk-selftest": ("file",)}
SECRET_MODES = ("serve", "prove", "ready", "clear-stop", "sdk-selftest")
TEST_ROOT = "/tmp/l1-bot-selftest"       # the self-tests' trees: written in their modes alone, removed by them
TEST_MODES = ("selftest", "sdk-selftest")
WRITE_FLAGS = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC
IPV4 = re.compile(r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}")
CHANGE_EVENTS = ("os.remove", "os.rename", "os.rmdir", "os.mkdir", "os.truncate", "os.chmod", "os.chown",
                 "os.utime", "os.link", "os.symlink", "shutil.rmtree", "shutil.copyfile")
HOOKED = ("open", "socket.__new__", "socket.getaddrinfo", "socket.connect", "subprocess.Popen") + CHANGE_EVENTS


class GuardError(RuntimeError):
    pass


def _under(p, root):
    return p == root or p.startswith(root + "/")


def _path(p):
    if isinstance(p, bytes):
        p = os.fsdecode(p)
    return os.path.abspath(p) if isinstance(p, str) else None


def _writing(wmode, flags):
    if isinstance(wmode, str):
        return bool(set(wmode) & set("wax+"))
    return isinstance(flags, int) and bool(flags & WRITE_FLAGS)


def policy(mode, event, args, paths=None):
    """None where TZ-53 section 2 allows the event in this mode; otherwise why it is refused. Pure but for the
    addresses this process resolved from an allowed name. IPv4 alone: a network socket of any family but AF_INET, a
    lookup in any family but AF_INET and a connection to anything but an IPv4 address are refused in every mode; an
    AF_UNIX socket is let through - asyncio's self-pipe - and never connects. Writes and changes under the unit's
    record alone; its credentials read in the modes that use them; the captures' stores never opened."""
    pp = paths or P
    tests = mode in TEST_MODES
    if event == "socket.__new__":
        fam = args[1] if len(args) > 1 else None
        return None if fam in (socket.AF_INET, socket.AF_UNIX) else "a socket of family %r: IPv4 alone" % (fam,)
    if event == "socket.getaddrinfo":
        host = args[0] if args else None
        if isinstance(host, bytes):
            host = host.decode("ascii", "replace")
        fam = args[2] if len(args) > 2 else None
        if fam != socket.AF_INET:
            return "a lookup of %r in family %r: IPv4 alone" % (host, fam)
        return None if host in RESOLVED or host in NET.get(mode, ()) else "a lookup of %r" % (host,)
    if event == "socket.connect":
        addr = args[1] if len(args) > 1 else None
        ok = isinstance(addr, tuple) and len(addr) == 2 and isinstance(addr[0], str) \
            and IPV4.fullmatch(addr[0]) is not None and (addr[0] in RESOLVED or addr[0] in NET.get(mode, ()))
        return None if ok else "a connection to %r" % (addr,)
    if event == "subprocess.Popen":
        exe = args[0] if args and args[0] else (args[1][0] if len(args) > 1 and args[1] else None)
        name = os.path.basename(os.fsdecode(exe)) if exe is not None else None
        return None if name in EXECS.get(mode, ()) else "running %r" % (name,)
    p = _path(args[0]) if args else None
    if p is None:
        return None
    if event == "open":
        wm, fl = (args[1] if len(args) > 1 else None), (args[2] if len(args) > 2 else None)
        if any(_under(p, r) for r in PROTECTED):
            return "an open under a capture's store or the advisor's credentials"
        if p == "/dev/tty":
            return "the terminal"
        if p == "/dev/null" or (tests and _under(p, TEST_ROOT)):
            return None
        if _under(p, pp.etc):
            if _writing(wm, fl):
                return "a write under %s" % pp.etc
            return None if mode in SECRET_MODES else "a read of %s in mode %s" % (p, mode)
        if _writing(wm, fl) and not _under(p, pp.var) and not (tests and _under(p, TEST_ROOT)):
            return "a write outside %s" % pp.var
        return None
    for i in ((0, 1) if event in ("os.rename", "os.link", "os.symlink", "shutil.copyfile") else (0,)):
        q = _path(args[i]) if len(args) > i else None
        if q is not None and not _under(q, pp.var) and not (tests and _under(q, TEST_ROOT)):
            return "a change outside %s" % pp.var
    return None


def _audit(event, args):
    if event not in HOOKED:
        return
    why = policy(MODE[0], event, args)
    if why is not None:
        REFUSED.append((event, MODE[0]))
        raise GuardError("%s refused in mode %s: %s" % (event, MODE[0], why))


sys.addaudithook(_audit)
_GAI = socket.getaddrinfo


def gai4(host, port, family=0, type=0, proto=0, flags=0):
    """socket.getaddrinfo with AF_INET asked of every lookup that names no family and any other refused: httpx,
    asyncio and websockets open IPv4 sockets alone (map section 7 item 181)."""
    if family in (0, socket.AF_UNSPEC):
        family = socket.AF_INET
    if family != socket.AF_INET:
        raise GuardError("a lookup of %r in family %r: IPv4 alone" % (host, family))
    infos = _GAI(host, port, family, type, proto, flags)
    RESOLVED.update(ai[4][0] for ai in infos if ai[0] == socket.AF_INET)
    COUNTS["lookups"] += 1
    return infos


socket.getaddrinfo = gai4

# ---- small helpers -------------------------------------------------------------------------------------------------


def out(msg):
    sys.stdout.write("[%s] %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    sys.stdout.flush()


def utc(t):
    return datetime.datetime.fromtimestamp(float(t), datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def day_of(t):
    """The UTC day of instant t: its D0, epoch seconds. Pure."""
    return int(t) // 86400 * 86400


def date_of(d0):
    return utc(d0)[:10]


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(path):
    with open(path, "rb") as fh:
        return sha256_bytes(fh.read())


def read_text(path, default=None):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except OSError:
        return default


def json_of(blob):
    try:
        return json.loads(blob.decode("utf-8") if isinstance(blob, (bytes, bytearray)) else blob)
    except (ValueError, UnicodeDecodeError, TypeError):
        return None


def scrub(text):
    """Text with every secret shape masked: a hexadecimal string of six digits or more after 0x - an address, a
    hash, a signature, an order's id - a bare 64-digit key, a UUID, a Telegram bot token. Pure."""
    s = re.sub(r"0x[0-9a-fA-F]{6,}", "0x…", str(text))
    s = re.sub(r"\b[0-9a-fA-F]{64}\b", "<hex>", s)
    s = re.sub(r"[0-9]{5,12}:[A-Za-z0-9_-]{30,64}", "<token>", s)
    return re.sub(r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}", "<uuid>", s)


def said(exc):
    """The venue's own words in a refusal, every secret shape masked (scrub), on one line of at most 300
    characters. Pure (map section 7 item 191)."""
    return scrub(" ".join(str(exc).split()))[:300]


def units(v):
    """Six-decimal units as pUSD, signed. Pure."""
    if not isinstance(v, int):
        return "—"
    s, a = ("-" if v < 0 else ""), abs(v)
    return "%s%d.%06d" % ((s,) + divmod(a, UNITS))


def usd2(v):
    """Six-decimal units as pUSD to the cent, for the Boss's messages. Pure."""
    if not isinstance(v, int):
        return "—"
    return "%s%d.%02d" % ((("-" if v < 0 else ""),) + divmod((abs(v) + 5000) // 10000, 100))


def file_state(path):
    """A path's kind, mode, owner and size - never its content."""
    try:
        st = os.lstat(path)
    except FileNotFoundError:
        return "absent"
    kind = "dir" if os.path.isdir(path) and not os.path.islink(path) else (
        "file" if os.path.isfile(path) and not os.path.islink(path) else "other")
    return "%s mode %04o uid %d bytes %d" % (kind, st.st_mode & 0o7777, st.st_uid, st.st_size)


def private_file_ok(path, mode=0o600, uid=0):
    try:
        st = os.lstat(path)
    except FileNotFoundError:
        return False
    return (os.path.isfile(path) and not os.path.islink(path) and st.st_uid == uid
            and st.st_mode & 0o7777 == mode and st.st_size > 0)


def ensure_dir(d, mode=0o700):
    if not os.path.isdir(d):
        os.mkdir(d, mode)


def write_private(path, data):
    """`data` to `path` by exclusive create, 0600 from its first byte. Returns the bytes written."""
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        os.write(fd, data)
        os.fsync(fd)
    finally:
        os.close(fd)
    return len(data)


def write_json_atomic(path, obj):
    """`obj` as JSON to `path` through `path`.tmp and a rename, 0600."""
    tmp = path + ".tmp"
    data = (json.dumps(obj, sort_keys=True, indent=1) + "\n").encode()
    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    try:
        os.write(fd, data)
        os.fsync(fd)
    finally:
        os.close(fd)
    os.rename(tmp, path)
    return len(data)


def load_json(path):
    return json_of((read_text(path) or "").encode())


def meminfo(text):
    found = {}
    for line in text.split("\n"):
        f = line.split()
        if len(f) >= 2 and f[0].endswith(":") and f[1].isdigit():
            found[f[0][:-1]] = int(f[1]) * (1024 if len(f) > 2 and f[2] == "kB" else 1)
    return found


def mem_available():
    return meminfo(read_text("/proc/meminfo", ""))["MemAvailable"]


def disk_available(path="/"):
    st = os.statvfs(path)
    return st.f_bavail * st.f_frsize


def peak():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024


def run(argv, timeout=20):
    """A command under TZ=UTC and the C locale (map section 7 item 185): (exit, stdout, stderr)."""
    cp = subprocess.run(argv, capture_output=True, text=True, timeout=timeout,
                        env=dict(os.environ, TZ="UTC", LC_ALL="C", SYSTEMD_COLORS="0", SYSTEMD_PAGER=""))
    return cp.returncode, cp.stdout, cp.stderr


def ntp_synchronized():
    rc, so, _se = run(["timedatectl", "show", "-p", "NTPSynchronized", "--value"])
    return rc == 0 and so.strip() == "yes"


def key_fingerprints(text):
    import base64
    found = []
    for ln in text.split("\n"):
        f = ln.split()
        for i, w in enumerate(f[:-1]):
            if w.startswith("ssh-") or w.startswith("ecdsa-") or w.startswith("sk-"):
                try:
                    blob = base64.b64decode(f[i + 1], validate=True)
                except ValueError:
                    break
                found.append((w, "SHA256:" + base64.b64encode(hashlib.sha256(blob).digest()).decode().rstrip("=")))
                break
    return found


def is_live_host():
    """The live host by its fixed facts (map section 6, live host identity): its name's first label, its pinned
    host key among its own, and no capture's store."""
    keys = []
    if os.path.isdir(HOST_KEY_DIR):
        for n in sorted(os.listdir(HOST_KEY_DIR)):
            if n.startswith("ssh_host_") and n.endswith("_key.pub"):
                keys += key_fingerprints(read_text(os.path.join(HOST_KEY_DIR, n), "") or "")
    return (socket.gethostname().split(".", 1)[0] == LIVE_HOSTNAME and LIVE_HOST_KEY in keys
            and not os.path.exists(CAPTURE_MARK))


def assert_live():
    assert is_live_host(), "BLOCKED: this mode runs on the live host %s and nowhere else" % LIVE_HOSTNAME

# ---- the frozen rules: taken by name from their files, by their SHA-256 ------------------------------------------

TZ33_NAMES = ("DAY", "SET_SIZE", "WALK_MAX", "GAMMA_BATCH", "GAMMA_LIMIT", "END_MIN_S", "EVENT_BAND_S", "EXCLUDED_TAGS",
              "LISTING_FIRST", "LISTING_END", "LISTING_PAGES_MAX", "REQUEST_TRIES", "RETRY_S", "REQUEST_GAP_S",
              "SELECT_LEAD_S", "CID_RE", "TOKEN_ID_RE", "MEMBER_KEYS", "CLOB_LISTING_URL", "GAMMA_MARKETS_URL",
              "CLOB_MARKET_URL", "CLOB_REWARDS_URL", "CLOB_WS_URL", "SelectionError", "sha256_bytes", "loads_exact",
              "canonical", "number", "compact_row", "listing_rows", "listing_verdict", "ranking", "iso_seconds",
              "gamma_verdict", "clob_verdict", "member_of", "walk", "gamma_query", "docs_by_condition", "run_rule")
TZ45_NAMES = ("CAP_CLIPS", "W_MS_MAX", "W_COMP_MAX", "W_BAND", "W_INSIDE_MAX", "PRICE_UNIT", "SIZE_UNIT", "_PRICE",
              "_SIZE", "_PRICES", "_SIZES", "price_int", "size_int", "_TERM", "terms_of", "w_targets")


def _bound_names(tree):
    names = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Name) and isinstance(n.ctx, (ast.Store, ast.Del)):
            names.add(n.id)
        elif isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            names.add(n.name)
        elif isinstance(n, ast.arg):
            names.add(n.arg)
        elif isinstance(n, ast.ExceptHandler) and n.name:
            names.add(n.name)
        elif isinstance(n, (ast.Import, ast.ImportFrom)):
            names.update((a.asname or a.name).split(".")[0] for a in n.names)
    return names


def free_names(tree):
    """The names a module's code reads and never binds, builtins aside. Pure."""
    used = {n.id for n in ast.walk(tree) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load)}
    return used - _bound_names(tree) - set(dir(builtins))


def load_frozen(path, sha, names, env):
    """The named top-level functions, classes and constants of a frozen file, compiled alone from its source - its
    own lines, under its own name - after its bytes are asserted at `sha`; every name they read is one of them or of
    `env`. Nothing else of the file runs."""
    with open(path, "rb") as fh:
        data = fh.read()
    assert sha256_bytes(data) == sha, "BLOCKED: %s is not the frozen file %s" % (path, sha[:12])
    tree = ast.parse(data, filename=path)
    keep, found = [], []
    for node in tree.body:
        name = None
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            name = node.name
        elif isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            name = node.targets[0].id
        elif isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Tuple):
            tn = [e.id for e in node.targets[0].elts if isinstance(e, ast.Name)]
            if tn and set(tn) <= set(names):
                keep.append(node)
                found += tn
            continue
        if name in names:
            keep.append(node)
            found.append(name)
    assert sorted(found) == sorted(names), "BLOCKED: %s lacks %s" % (path, sorted(set(names) - set(found)))
    mod = ast.Module(body=keep, type_ignores=[])
    free = free_names(mod) - set(env)
    assert not free, "BLOCKED: %s's rules read %s" % (path, sorted(free))
    ns = dict(env)
    exec(compile(mod, path, "exec"), ns)
    return types.SimpleNamespace(**{n: ns[n] for n in names})


RULES = {}


def rules(svc=None):
    """tz33's selection and tz45's rule W, loaded once from the files beside this one."""
    if not RULES:
        here = svc or os.path.dirname(os.path.abspath(__file__))
        RULES["tz33"] = load_frozen(os.path.join(here, FROZEN["tz33"][0]), FROZEN["tz33"][1], TZ33_NAMES,
                                    {"json": json, "re": re, "hashlib": hashlib, "datetime": datetime,
                                     "urllib": urllib, "Counter": collections.Counter, "Decimal": D})
        RULES["tz45"] = load_frozen(os.path.join(here, FROZEN["tz45"][0]), FROZEN["tz45"][1], TZ45_NAMES,
                                    {"Fr": Fr, "D": D, "re": re})
    return RULES["tz33"], RULES["tz45"]

# ---- rule W in the unit: TZ-45's Day.decide, lines 1412 to 1442, around tz45's own w_targets ----------------------


def quote_targets(W, m, bb, ba):
    """Rule W's bid and ask, thousandths of the market's first token, on the displayed touch bb, ba - ours taken
    out - each None where that side quotes nothing: the market's minimum size at most W_MS_MAX, its terms unmoved,
    its last served poll's competitiveness at most W_COMP_MAX; w_targets; the band narrower than twice the maximum
    spread; each target inside (0, 1). Pure."""
    if bb is None or ba is None:
        return None, None
    if not (m.ms <= W.W_MS_MAX and not m.moved and m.comp is not None and m.comp <= W.W_COMP_MAX):
        return None, None
    tb, ta = W.w_targets(bb, ba, m.tick, m.vu)
    if tb is None or not (ta - tb < m.vu and m.ms > 0):
        return None, None
    return (tb if 0 < tb < W.PRICE_UNIT else None), (ta if 0 < ta < W.PRICE_UNIT else None)


def capped(W, tb, ta, x, ms):
    """Rule W's position cap of CAP_CLIPS sizes: no bid at a position of a cap or more, no ask at minus a cap or
    less; x in hundredths of the first token, + long. Pure."""
    cap = W.CAP_CLIPS * ms
    return (tb if x < cap else None), (ta if x > -cap else None)


def order_of(side, tgt, yes, no, ms, sell_ok):
    """The order that stands for rule W's side at the first token's price tgt, thousandths: (op, outcome index, the
    order's own price). A bid sells the second token where the wallet holds a size of it and may sell it, else buys
    the first; an ask sells the first where it holds a size of it, else buys the second at the complement. Pure."""
    if side == "b":
        return ("SELL", 1, 1000 - tgt) if sell_ok and no >= ms else ("BUY", 0, tgt)
    return ("SELL", 0, tgt) if sell_ok and yes >= ms else ("BUY", 1, 1000 - tgt)


def reserve_of(op, px, size):
    """The pUSD a resting order reserves, six-decimal units: a buy its price times its size, a sell none. Pure."""
    return px * size * 10 if op == "BUY" else 0


def price_text(px, tick):
    """A price in thousandths as the order's text on its tick's grid. Pure."""
    places = {100: 1, 10: 2, 1: 3}[tick]
    assert px % tick == 0 and 0 < px < 1000, "a price %d off the grid of tick %d" % (px, tick)
    return format((D(px) / 1000).quantize(D(1).scaleb(-places)), "f")


def px_text(px):
    """A price in thousandths as the Boss reads it: 0.45, 0.455. Pure."""
    d = (D(px) / 1000).normalize()
    return format(d, "f")


def size_text(size):
    """A size in hundredths of a share as the order's text. Pure."""
    return format((D(size) / 100).quantize(D("0.01")), "f")


def kind_of(member):
    """A member's exchange: v where its tokens are Protocol V2 position IDs, n where it is negative-risk, else c."""
    toks = member["token_ids"]
    if all(int(t) & V2_RESERVED == 0 for t in toks):
        return "v"
    return "n" if member.get("neg_risk") is True else "c"


def poll_row(doc, day):
    """A served reward poll as TZ-45's polls_of reads it (research/tz45-l0-rule-w.py lines 863 to 876): None where
    the page holds no row; else (the daily rate - the sum over the row's reward configurations in force on the
    poll's UTC date - the competitiveness, the row's minimum size in hundredths, its maximum spread in
    half-thousandths), terms_of giving the last two. `doc` parsed with every non-integer number a Decimal."""
    _R, W = rules()
    data = doc.get("data") if isinstance(doc, dict) else None
    if not data:
        return None
    d = data[0]
    rate = sum((Fr(str(c["rate_per_day"])) for c in d["rewards_config"]
                if (c.get("start_date") is None or str(c["start_date"])[:10] <= day) and
                (c.get("end_date") is None or day <= str(c["end_date"])[:10])), Fr(0))
    return (rate, Fr(str(d["market_competitiveness"]))) + W.terms_of(d)

# ---- the book of a market's first token, from the market channel ------------------------------------------------


class Book:
    """One token's displayed levels: thousandths to hundredths of a share."""
    __slots__ = ("bids", "asks", "tick", "seeded", "frames")

    def __init__(self):
        self.bids, self.asks, self.tick, self.seeded, self.frames = {}, {}, 10, False, 0

    def seed(self, bids, asks, tick=None):
        self.bids = {p: s for p, s in bids.items() if s}
        self.asks = {p: s for p, s in asks.items() if s}
        if tick is not None:
            self.tick = tick
        self.seeded = True

    def change(self, side, p, s):
        bk = self.bids if side == "b" else self.asks
        if s:
            bk[p] = s
        else:
            bk.pop(p, None)

    def clear(self):
        self.bids, self.asks, self.seeded = {}, {}, False

    def touch(self, ours=None):
        """The best bid and ask with our own resting sizes taken out of their levels: rule W reads the book as the
        replay held it, without our quote. Pure."""
        ours = ours or {}
        bb = next((p for p in sorted(self.bids, reverse=True) if self.bids[p] - ours.get(("b", p), 0) > 0), None)
        ba = next((p for p in sorted(self.asks) if self.asks[p] - ours.get(("a", p), 0) > 0), None)
        return bb, ba


def frame_items(raw):
    """A market channel's text frame as its items: a list frame's dicts, a dict frame alone; PONG and anything
    else none. Pure."""
    if raw == "PONG" or not isinstance(raw, str):
        return []
    obj = json_of(raw)
    if isinstance(obj, list):
        return [x for x in obj if isinstance(x, dict)]
    return [obj] if isinstance(obj, dict) else []

# ---- the unit's records ----------------------------------------------------------------------------------------


class Journal:
    """The unit's journal: one JSON line an event, a file a UTC day under paths.journal, 0600, appended and flushed;
    the events that move money or stop the unit synced to the disk."""
    SYNC = ("placed", "refused", "canceled", "fill", "gone", "stop", "term", "error", "start", "drill")

    def __init__(self, paths, clock=time.time):
        self.paths, self.clock, self.fh, self.day, self.lines = paths, clock, None, None, 0

    def write(self, kind, **fields):
        t = self.clock()
        d = date_of(day_of(t))
        if d != self.day:
            self.close()
            ensure_dir(self.paths.journal)
            path = os.path.join(self.paths.journal, d + ".jsonl")
            fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o600)
            self.fh, self.day = os.fdopen(fd, "a", encoding="utf-8"), d
        rec = {"t": round(t, 3), "k": kind}
        rec.update(fields)
        self.fh.write(json.dumps(rec, sort_keys=True, separators=(",", ":"), default=str) + "\n")
        self.fh.flush()
        self.lines += 1
        if kind in self.SYNC:
            os.fsync(self.fh.fileno())

    def close(self):
        if self.fh is not None:
            self.fh.flush()
            os.fsync(self.fh.fileno())
            self.fh.close()
            self.fh = None


def stop_record(paths):
    """The stop record, or None."""
    return load_json(paths.stop) if os.path.exists(paths.stop) else None


def write_stop(paths, rec):
    """The stop record by exclusive create; one that stands is kept. True where this call wrote it."""
    try:
        write_private(paths.stop, (json.dumps(rec, sort_keys=True, indent=1) + "\n").encode())
        return True
    except FileExistsError:
        return False


def prove_paths(paths):
    if not os.path.isdir(paths.var):
        return []
    found = sorted((int(m.group(1)), n) for n in os.listdir(paths.var) for m in [PROVE_RECORD.fullmatch(n)] if m)
    return [os.path.join(paths.var, n) for _i, n in found]


def proved(paths, code_sha):
    """The last prove record of this code that read PASS: the kinds it proved and whether its heartbeat was
    accepted; None where there is none."""
    for p in reversed(prove_paths(paths)):
        rec = load_json(p) or {}
        if rec.get("code_sha256") == code_sha and rec.get("pass") is True:
            return rec
    return None

# ---- the unit's own public requests: httpx, IPv4 alone, this unit's agent, no proxy -------------------------------


class Net:
    """Every public request of the unit - the geoblock, the CLOB's public documents, gamma, Telegram, the chain's
    reads - through one httpx client: its agent UA, IPv4 alone through gai4, no proxy read from the environment."""

    def __init__(self, origins=None):
        import httpx
        self.httpx = httpx
        self.o = dict(ORIGINS, **(origins or {}))
        self.h = httpx.AsyncClient(headers={"User-Agent": UA, "Accept": "application/json"}, timeout=TIMEOUT_S,
                                   trust_env=False)

    async def call(self, method, kind, path, body=None, timeout=TIMEOUT_S):
        """(status, body bytes, reason): status None where no reply came."""
        COUNTS["requests"] += 1
        try:
            r = await self.h.request(method, self.o[kind] + path, json=body, timeout=timeout)
            return r.status_code, r.content, None
        except self.httpx.HTTPError as exc:
            return None, b"", type(exc).__name__

    async def close(self):
        await self.h.aclose()


def sync_get(origins=None):
    """A blocking GET with the unit's agent, for the selection's thread: url -> the reply's record."""
    import httpx
    h = httpx.Client(headers={"User-Agent": UA, "Accept": "application/json"}, timeout=10.0, trust_env=False)

    def get(url):
        COUNTS["requests"] += 1
        status, body, reason = None, b"", None
        try:
            r = h.get(url)
            status, body = r.status_code, r.content
        except httpx.HTTPError as exc:
            reason = type(exc).__name__
        try:
            raw = body.decode("utf-8")
        except UnicodeDecodeError:
            raw = body.decode("latin-1")
        return {"url": url, "status": status, "recv_wall_ns": time.time_ns(), "bytes": len(body),
                "sha256": sha256_bytes(body), "raw": raw, "reason": reason}
    get.close = h.close
    return get


def geo_reading(status, doc):
    """G-GEO from one geoblock read: PASS where served and not blocked, BLOCKED where blocked, else UNREAD; the
    country beside. The reply's address is never kept. Pure."""
    if status != 200 or not isinstance(doc, dict) or not isinstance(doc.get("blocked"), bool):
        return "UNREAD", None
    return ("BLOCKED" if doc["blocked"] else "PASS"), doc.get("country")


async def geo_read(net):
    status, body, reason = await net.call("GET", "geo", GEO_PATH)
    reading, country = geo_reading(status, json_of(body) if status == 200 else None)
    return reading, country, status if status is not None else reason

# ---- Telegram: the Boss's pinned chat, the reports and the one command that acts -----------------------------------

KEYBOARD = {"keyboard": [[{"text": "Стоп"}, {"text": "Статус"}]], "resize_keyboard": True, "is_persistent": True}


def tg_command(text):
    """A message's command: stop, status, start, or other. Pure."""
    t = " ".join((text or "").split()).casefold()
    if t in ("стоп", "/stop", "stop"):
        return "stop"
    if t in ("статус", "/status", "status"):
        return "status"
    if t.startswith("/start"):
        return "start"
    return "other"


def chat_commands(updates, chat):
    """The pinned chat's commands among Telegram updates, in order: (update_id, command); every other chat's
    message is ignored. Pure."""
    found = []
    for u in updates:
        m = u.get("message") if isinstance(u, dict) else None
        if not isinstance(m, dict) or not isinstance(u.get("update_id"), int):
            continue
        if (m.get("chat") or {}).get("id") != chat:
            continue
        found.append((u["update_id"], tg_command(m.get("text"))))
    return found


class TgError(RuntimeError):
    pass


class Tg:
    """The bot's own Telegram: its token in the request path alone, never printed; its one chat."""

    def __init__(self, net, token, chat):
        self.net, self.token, self.chat = net, token, chat
        self.sent = 0

    async def call(self, method, http_timeout=TIMEOUT_S, **params):
        status, body, reason = await self.net.call("POST", "tg", "/bot%s/%s" % (self.token, method), body=params,
                                                   timeout=http_timeout)
        doc = json_of(body)
        if not (isinstance(doc, dict) and doc.get("ok") is True):
            raise TgError("telegram %s: %s %s" % (method, doc.get("error_code") if isinstance(doc, dict) else
                                                  status or reason, doc.get("description") if isinstance(doc, dict)
                                                  else ""))
        return doc["result"]

    async def send(self, text):
        msg = await self.call("sendMessage", chat_id=self.chat, text=text[:4000], reply_markup=KEYBOARD,
                              disable_web_page_preview=True)
        self.sent += 1
        return msg.get("message_id") if isinstance(msg, dict) else None

    async def updates(self, offset, wait):
        params = {"timeout": int(wait), "allowed_updates": ["message"]}
        if offset is not None:
            params["offset"] = offset
        return await self.call("getUpdates", http_timeout=wait + 15, **params)


def read_token(paths):
    assert private_file_ok(paths.token), "BLOCKED: %s: %s" % (paths.token, file_state(paths.token))
    t = (read_text(paths.token) or "").strip()
    assert re.fullmatch(r"[0-9]{5,12}:[A-Za-z0-9_-]{30,64}", t), "BLOCKED: %s holds no bot token" % paths.token
    return t


def read_chat(paths):
    assert private_file_ok(paths.chat), "BLOCKED: %s: %s" % (paths.chat, file_state(paths.chat))
    c = (read_text(paths.chat) or "").strip()
    assert re.fullmatch(r"-?[0-9]+", c), "BLOCKED: %s holds no chat" % paths.chat
    return int(c)

# ---- the day's selection: TZ-33's run_rule through the unit's own requests -------------------------------------------


class Fetch:
    """TZ-33's LiveFetch through this unit's own GET: every try one reply record handed to `sink`; a request tried
    at most REQUEST_TRIES times on a network error, a 429 or a 5xx, RETRY_S apart; REQUEST_GAP_S between two
    requests; a final reply that is not 200 - or 404 for a CLOB document - fails the attempt (SelectionError)."""

    def __init__(self, R, get, sink, origins=None, sleep=time.sleep):
        self.R, self.get, self.sink, self.sleep = R, get, sink, sleep
        o = dict(ORIGINS, **(origins or {}))
        self.urls = {k: getattr(R, n).replace(ORIGINS["clob"], o["clob"]).replace(ORIGINS["gamma"], o["gamma"])
                     for k, n in (("listing", "CLOB_LISTING_URL"), ("gamma", "GAMMA_MARKETS_URL"),
                                  ("clob", "CLOB_MARKET_URL"))}
        self.requests = 0

    def _one(self, kind, key, url):
        R = self.R
        for t in range(R.REQUEST_TRIES):
            if self.requests:
                self.sleep(R.REQUEST_GAP_S)
            self.requests += 1
            res = self.get(url)
            self.sink(dict(res, kind=kind, key=key, attempt=t))
            st = res["status"]
            if st is not None and st != 429 and st < 500:
                return res
            if t + 1 < R.REQUEST_TRIES:
                self.sleep(R.RETRY_S[min(t, len(R.RETRY_S) - 1)])
        return res

    def listing(self, cursor):
        res = self._one("listing", cursor, self.urls["listing"].format(cursor=cursor))
        if res["status"] != 200:
            raise self.R.SelectionError("listing page %s: status %s" % (cursor, res["status"]))
        return res["raw"]

    def gamma(self, cids):
        res = self._one("gamma", list(cids), self.urls["gamma"].format(query=self.R.gamma_query(cids)))
        if res["status"] != 200:
            raise self.R.SelectionError("gamma request: status %s" % res["status"])
        return res["raw"]

    def clob(self, cid):
        res = self._one("clob", cid, self.urls["clob"].format(condition_id=cid))
        if res["status"] == 404:
            return None
        if res["status"] != 200:
            raise self.R.SelectionError("CLOB document %s: status %s" % (cid, res["status"]))
        return res["raw"]


def select_path(paths, d0):
    return os.path.join(paths.select, "%d.json" % d0)


def select_day(d0, paths, get, origins=None, sleep=time.sleep):
    """The day's selection by TZ-33's rule, its every reply stored gzipped beside its result: the result, with each
    member's CLOB document's minimum order size, tick and negative-risk flag."""
    R, _W = rules()
    replies = []
    fetch = Fetch(R, get, replies.append, origins=origins, sleep=sleep)
    t0 = time.time()
    res = R.run_rule(fetch, d0)
    docs = {}
    for r in replies:
        if r["kind"] == "clob" and r["status"] == 200:
            d = json_of(r["raw"])
            if isinstance(d, dict):
                docs[r["key"]] = {"minimum_order_size": str(d.get("minimum_order_size")),
                                  "minimum_tick_size": str(d.get("minimum_tick_size")),
                                  "neg_risk": d.get("neg_risk")}
    rec = {"d0": d0, "made_at": int(time.time()), "seconds": round(time.time() - t0, 1), "requests": fetch.requests,
           "listing": res["listing"], "walked": res["walked"], "covered": res["covered"], "reasons": res["reasons"],
           "members": res["members"], "clob": {m["condition_id"]: docs.get(m["condition_id"]) for m in res["members"]}}
    ensure_dir(paths.select)
    gz = os.path.join(paths.select, "%d.replies.jsonl.gz" % d0)
    with gzip.open(gz + ".tmp", "wt", encoding="utf-8", compresslevel=6) as fh:
        for r in replies:
            fh.write(json.dumps(r, sort_keys=True, separators=(",", ":")) + "\n")
    os.rename(gz + ".tmp", gz)
    write_json_atomic(select_path(paths, d0), rec)
    return rec


def load_selection(paths, d0):
    rec = load_json(select_path(paths, d0))
    return rec if isinstance(rec, dict) and rec.get("d0") == d0 and isinstance(rec.get("members"), list) else None

# ---- a member of the day's selection, as the unit quotes it ---------------------------------------------------


class Market:
    """One member: its terms as the selection and the polls read them, its book, our orders and holdings."""

    def __init__(self, m, doc, d0):
        self.cid, self.toks, self.slug, self.rank = m["condition_id"], list(m["token_ids"]), m.get("slug"), m["rank"]
        self.outcomes = list(m.get("outcomes") or ["", ""])
        self.kind = kind_of(m)
        ms, vu = Fr(m["min_size"]) * 100, Fr(m["max_spread"]) * 20
        assert ms.denominator == 1 and vu.denominator == 1 and ms > 0 and vu > 0, "%s: size or spread" % self.cid
        self.ms, self.vu, self.rate = int(ms), int(vu), Fr(m["rate"])
        self.min_order = None
        try:
            self.min_order = int(D((doc or {}).get("minimum_order_size")) * 100)
        except (TypeError, ValueError, decimal.InvalidOperation):
            pass
        self.d0 = d0
        self.book = Book()
        tick = str((doc or {}).get("minimum_tick_size"))
        if tick in ("0.1", "0.01", "0.001"):
            self.book.tick = {"0.1": 100, "0.01": 10, "0.001": 1}[tick]
        self.mark = 0                           # six-decimal units: the holdings at the last seeded book
        self.comp, self.moved, self.polled_at, self.polls = None, False, 0.0, 0
        self.orders = {"b": None, "a": None}
        self.yes = self.no = 0                  # hundredths of a share held of each outcome
        self.paused_until, self.dirty, self.decided = 0.0, True, None
        self.member = True                      # of today's selection: rule W may quote it
        self.member_doc = m
        self.refusals, self.cool_until = 0, 0.0
        self.ghosts = []                        # (side, price, size, until): orders of ours the book may still show
        self.expect, self.verify_at, self.expect_since = None, 0.0, 0.0   # the ledger's holdings, unverified
        self.lock = asyncio.Lock()              # one decision, cancel or fill reading of the market at a time

    @property
    def x(self):
        return self.yes - self.no

    @property
    def tick(self):
        return self.book.tick

    def ours(self, now=None):
        """Our resting sizes by the first token's side and price, to take out of its book - and, for GHOST_S after
        they leave it, the orders a frame behind the venue may still show."""
        found = {}
        for side, o in self.orders.items():
            if o is not None and o["state"] in ("live", "sent"):
                key = (side, o["ypx"])
                found[key] = found.get(key, 0) + o["size"] - o["matched"]
        t = time.time() if now is None else now
        self.ghosts = [g for g in self.ghosts if g[3] > t]
        for side, p, size, _u in self.ghosts:
            found[(side, p)] = found.get((side, p), 0) + size
        return found

    def leave(self, side, now, ghost_s):
        """Our order on `side` off the book: its level remembered as a ghost for ghost_s."""
        o = self.orders[side]
        if o is not None and o["state"] == "live":
            self.ghosts.append((side, o["ypx"], o["size"] - o["matched"], now + ghost_s))
        self.orders[side] = None

    def holds(self):
        return self.yes > 0 or self.no > 0

    def quoting(self):
        return any(o is not None for o in self.orders.values())

# ---- the venue's client, /root/l1-env, polymarket-client 0.20.0 -------------------------------------------------


def client():
    """The venue's client in this process: every request with this unit's agent, every lookup through gai4; its
    pinned version and the terms this file relies on asserted."""
    import dataclasses
    import importlib.metadata as md
    import httpx
    import httpx._client
    httpx._client.USER_AGENT = UA
    from eth_account import Account
    from polymarket import AsyncSecureClient
    from polymarket.environments import PRODUCTION, _create_environment
    from polymarket import errors as E
    from polymarket._internal.actions import account as A
    from polymarket._internal.wallet import signature_type_for
    assert md.version(SDK_DIST) == SDK_VERSION, "the client is %s, not %s" % (md.version(SDK_DIST), SDK_VERSION)
    cfg = PRODUCTION._config
    assert (cfg.chain_id, cfg.collateral_token, cfg.conditional_tokens, cfg.position_manager) == (
        CHAIN_ID, PUSD, CTF, POSITIONS), "the client's collateral and positions"
    assert (cfg.standard_exchange, cfg.neg_risk_exchange, cfg.exchange_v3) == (
        EXCHANGES["c"], EXCHANGES["n"], EXCHANGES["v"]), "the client's exchanges"
    assert (cfg.clob_url, cfg.relayer_url, cfg.gamma_url, cfg.rpc_url) == (
        ORIGINS["clob"], "https://" + RELAYER_HOST, ORIGINS["gamma"], ORIGINS["rpc"]), "the client's hosts"
    return types.SimpleNamespace(dataclasses=dataclasses, Account=Account, AsyncSecureClient=AsyncSecureClient,
                                 PRODUCTION=PRODUCTION, _create_environment=_create_environment, E=E, A=A,
                                 signature_type_for=signature_type_for)


def load_session_key(paths):
    assert private_file_ok(paths.key), "BLOCKED: %s: %s" % (paths.key, file_state(paths.key))
    v = (read_text(paths.key) or "").strip()
    assert re.fullmatch(r"0x[0-9a-f]{64}", v), "BLOCKED: %s holds no key" % paths.key
    return v


def load_account(paths):
    doc = load_json(paths.account)
    assert isinstance(doc, dict) and doc.get("wallet") and doc.get("session_key") and doc.get("authorized_at"), \
        "BLOCKED: %s names no authorized session key" % paths.account
    return doc


def _word(address):
    return address.lower().removeprefix("0x").rjust(64, "0")


class Chain:
    """The wallet's reads on chain through the client's own Polygon RPC, eth_call alone."""

    def __init__(self, net, wallet):
        self.net, self.wallet = net, wallet

    async def call(self, to, data):
        body = {"jsonrpc": "2.0", "id": 1, "method": "eth_call", "params": [{"to": to, "data": data}, "latest"]}
        status, blob, _r = await self.net.call("POST", "rpc", "", body=body)
        doc = json_of(blob) if status == 200 else None
        res = doc.get("result") if isinstance(doc, dict) else None
        return int(res, 16) if isinstance(res, str) and re.fullmatch(r"0x[0-9a-fA-F]{1,64}", res) else None

    async def cash(self):
        return await self.call(PUSD, "0x" + SEL["balanceOf"] + _word(self.wallet))

    async def allowance(self, spender):
        return await self.call(PUSD, "0x" + SEL["allowance"] + _word(self.wallet) + _word(spender))

    async def approved(self, token, operator):
        v = await self.call(token, "0x" + SEL["isApprovedForAll"] + _word(self.wallet) + _word(operator))
        return None if v is None else v == 1


class Venue:
    """The session key's client for the wallet: every authenticated request the unit makes."""

    def __init__(self, k, c, session, wallet):
        self.k, self.c, self.session, self.wallet = k, c, session, wallet
        self.hb_id, self.hb_ok, self.hb_fail, self.hb_last = "", 0, 0, 0.0

    @classmethod
    async def open(cls, k, env, key_hex, acct):
        c = await k.AsyncSecureClient.create(private_key=key_hex, wallet=acct["wallet"], environment=env)
        return cls(k, c, k.Account.from_key(key_hex).address, acct["wallet"])

    def is_session(self):
        return self.c.wallet_type == "DEPOSIT_WALLET" and self.c._ctx.signer_type == "SESSION_KEY"

    async def close(self):
        await self.c.close()

    async def place(self, tok, op, px, size, tick, perf=time.perf_counter_ns):
        """One post-only GTC order: {result, oid, ms, words}; result live, crosses, or refused."""
        t0 = perf()
        oid, words = None, None
        try:
            signed = await self.c.create_limit_order(asset_id=tok, price=price_text(px, tick), size=size_text(size),
                                                     side=op, post_only=True)
            resp = await self.c.post_order(signed)
            if resp.ok:
                result, oid = ("live" if resp.status == "live" else "accepted %s" % resp.status), resp.order_id
            else:
                result = "crosses" if resp.code == "post_only_would_cross" else "refused"
                words = "%s: %s" % (resp.code, said(resp.message))
        except self.k.E.RequestRejectedError as exc:
            result = "crosses" if "crosses book" in str(exc) else "refused"
            words = "status %s: %s" % (exc.status, said(exc))
        except (self.k.E.PolymarketError, ValueError) as exc:
            result, words = "refused", "%s: %s" % (type(exc).__name__, said(exc))
        return {"result": result, "oid": oid, "ms": int((perf() - t0) // 1000000), "words": words}

    async def cancel(self, oids):
        """(the ids canceled, the ids not canceled with the venue's words)."""
        oids = list(oids)
        if len(oids) == 1:
            r = await self.c.cancel_order(order_id=oids[0])
        else:
            r = await self.c.cancel_orders(order_ids=oids)
        return set(r.canceled), {k: said(v) for k, v in r.not_canceled.items()}

    async def cancel_all(self):
        r = await self.c.cancel_all()
        return len(r.canceled), len(r.not_canceled)

    async def open_orders(self, pages=20):
        """The wallet's live orders placed by this key: [{id, asset, side, price, size, matched}], prices in
        thousandths, sizes in hundredths."""
        found, n = [], 0
        async for o in self.c.list_wallet_open_orders(signer_addresses=[self.session]).iter_items():
            found.append({"id": o.id, "asset": str(o.asset_id), "side": o.side, "price": int(o.price * 1000),
                          "size": int(o.original_size * 100), "matched": int(o.size_matched * 100),
                          "status": o.status})
            n += 1
            assert n <= pages * 500, "the wallet's open orders beyond %d" % (pages * 500)
        return found

    async def fills_of(self, cid, after_s, oids):
        """The matched sizes, hundredths, of our orders `oids` in the market's trades since after_s, by order id."""
        got = {}
        async for t in self.c.list_account_trades(market=cid, after=str(int(after_s))).iter_items():
            for mo in t.maker_orders:
                if mo.order_id in oids:
                    got[mo.order_id] = got.get(mo.order_id, 0) + int(mo.matched_amount * 100)
            if t.taker_order_id in oids and t.trader_side == "TAKER":
                got[t.taker_order_id] = got.get(t.taker_order_id, 0) + int(t.size * 100)
        return got

    async def balance_of(self, kind, tok):
        """The CLOB's view of the wallet's balance of a position, hundredths of a share, refreshed first."""
        at = "CONDITIONAL-V2" if kind == "v" else "CONDITIONAL"
        st = self.k.signature_type_for(self.c._ctx.wallet_type)
        path, params = self.k.A.build_update_balance_allowance_request(asset_type=at, asset_id=tok, signature_type=st)
        await self.c._ctx.secure_clob.get_bytes(path, params=params)
        ba = await self.c.get_balance_allowance(asset_type=at, asset_id=tok)
        return ba.balance // 10000

    async def clob_cash(self):
        st = self.k.signature_type_for(self.c._ctx.wallet_type)
        path, params = self.k.A.build_update_balance_allowance_request(asset_type="COLLATERAL", signature_type=st)
        await self.c._ctx.secure_clob.get_bytes(path, params=params)
        return (await self.c.get_balance_allowance(asset_type="COLLATERAL")).balance

    async def heartbeat(self, clock=time.time):
        """One order heartbeat with the id the venue last gave; a stale id retried once with the venue's."""
        for _t in range(2):
            try:
                r = await self.c.send_order_heartbeat(heartbeat_id=self.hb_id)
                self.hb_id, self.hb_ok, self.hb_last = r.heartbeat_id, self.hb_ok + 1, clock()
                return True
            except self.k.E.OrderHeartbeatMismatchError as exc:
                self.hb_id = exc.heartbeat_id
            except (self.k.E.PolymarketError, ValueError):
                break
        self.hb_fail += 1
        return False

    async def closed_only(self):
        return await self.c.get_closed_only_mode()

    async def earnings(self, date):
        rows = await self.c.get_total_earnings_for_user_for_day(date=date)
        return int(sum((r.earnings for r in rows), D(0)) * UNITS)

    async def rebates(self, date):
        rows = await self.c.get_current_rebates(date=date, maker_address=self.wallet)
        return int(sum((r.rebated_fees_usdc for r in rows), D(0)) * UNITS)

# ---- the account: G-READY's checks, read through the session key -----------------------------------------------


async def account_reads(venue, chain):
    """Every fact G-READY and the unit's start read of the account: the wallet's kind, closed-only mode, its pUSD
    on chain and in the CLOB's view, each exchange's allowance and position approval, the key's open orders."""
    f = {"session": venue.is_session(), "closed_only": await venue.closed_only(), "cash": await chain.cash(),
         "clob_cash": await venue.clob_cash(), "allowance": {}, "approved": {},
         "open": len(await venue.open_orders())}
    for x, ex in EXCHANGES.items():
        f["allowance"][x] = await chain.allowance(ex)
        f["approved"][x] = await chain.approved(POSITION_TOKEN[x], ex)
    return f


def kinds_usable(f):
    """The exchanges whose pUSD allowance reads the maximum: the kinds of market the unit may buy on. Pure."""
    return sorted(x for x, v in f["allowance"].items() if isinstance(v, int) and v >= MAX_READ)


def ready_checks(f, acct, now, first=True):
    """G-READY's gating checks from the account's reads. Pure. At a first start the wallet's pUSD on chain is
    between CAPITAL_MIN and CAPITAL_MAX; the standard exchange's allowance is the maximum; the key acts for a
    Deposit Wallet, outside closed-only mode, with no open order, authorized KEY_DAYS_MIN days ahead at least."""
    until = acct.get("valid_until")
    checks = {
        "a Deposit Wallet signed for by the session key": f["session"] is True,
        "not in closed-only mode": f["closed_only"] is False,
        "the standard exchange's pUSD allowance the maximum": isinstance(f["allowance"].get("c"), int)
        and f["allowance"]["c"] >= MAX_READ,
        "the key authorized %d days ahead at least" % KEY_DAYS_MIN: isinstance(until, int)
        and until >= now + KEY_DAYS_MIN * 86400,
        "no open order of the wallet by the key": f["open"] == 0}
    if first:
        checks["its pUSD on chain from %s to %s" % (usd2(CAPITAL_MIN), usd2(CAPITAL_MAX))] = (
            isinstance(f["cash"], int) and CAPITAL_MIN <= f["cash"] <= CAPITAL_MAX)
    return checks


def ready_lines(f):
    """The account's facts as printed: amounts, max where at the maximum; no address. Pure."""
    def al(v):
        return "max" if isinstance(v, int) and v >= MAX_READ else units(v)
    return ("pUSD on chain %s, the CLOB's view %s; allowances %s; position approvals %s; open orders of the key %d" % (
        units(f["cash"]), units(f["clob_cash"]), {x: al(v) for x, v in sorted(f["allowance"].items())},
        dict(sorted(f["approved"].items())), f["open"]))

# ---- the unit -------------------------------------------------------------------------------------------------

STOP_EXIT, TERM_EXIT, ERROR_EXIT, REFUSE_EXIT = 3, 0, 1, 2
DISK_FLOOR = 2447483648        # bytes available on /: TZ-52's LIVE_FLOOR, the journal's SystemKeepFree and room
MEM_FLOOR = 274917678          # MemAvailable at a start: TZ-52's client floor
STOP_WORDS = {"stop": "«Стоп» из Telegram", "drill": "«Стоп» из Telegram, проверка",
              "loss": "лимит убытка", "geo": "геоблок: адрес хоста заблокирован",
              "disk": "мало места на диске", "equity": "капитал не читается",
              "account": "счёт в режиме только закрытия позиций", "key": "срок сессионного ключа на исходе",
              "capital": "баланс кошелька вне границ ТЗ", "stuck": "заявки не снимаются",
              "term": "сигнал systemd", "error": "ошибка"}


def equity_of(cash, markets):
    """The wallet's equity, six-decimal units: its pUSD and each position marked at the touch, ours taken out - a
    complete set at 1, the first token at its best bid, the second at one less the best ask, an empty side at 0 -
    a market whose book is not seeded at its last mark; None where the cash is unread."""
    if not isinstance(cash, int):
        return None
    v = cash
    for m in markets:
        if not (m.yes or m.no):
            m.mark = 0
            continue
        if m.book.seeded:
            sets = min(m.yes, m.no)
            bb, ba = m.book.touch(m.ours())
            m.mark = (sets * 1000 * 10 + (m.yes - sets) * (bb or 0) * 10 +
                      (m.no - sets) * ((1000 - ba) if ba is not None else 0) * 10)
        v += m.mark
    return v


class Unit:
    """Rule W live: the day's markets, their books and terms, our orders and holdings, the guards, Telegram."""

    def __init__(self, paths, cfg, k, venue, chain, net, tg, journal, prove_rec=None, sell_ok=None, usable=None,
                 origins=None, get=None, clock=time.time):
        self.p, self.c, self.k = paths, cfg, k
        self.R, self.W = rules()
        self.v, self.chain, self.net, self.tg, self.j = venue, chain, net, tg, journal
        self.clock = clock
        self.origins, self.get = origins, get
        self.kinds = set((prove_rec or {}).get("kinds") or []) & set(usable or [])
        self.hb_on = bool((prove_rec or {}).get("heartbeat_accepted"))
        self.sell_ok = dict(sell_ok or {})
        self.state = load_json(paths.state) or {}
        self.markets, self.by_tok = {}, {}
        self.d0 = None
        self.sel_next, self.sel_task, self.sel_retry_at, self.sel_for, self.built_d0 = None, None, 0.0, None, None
        self.reason, self.reason_words, self.err = None, None, None
        self.done = asyncio.Event()
        self.cash, self.cash_at = None, 0.0
        self.equity, self.equity_at = None, clock()
        self.stream_up, self.down_since, self.last_frame, self.tokens_version = False, clock(), 0.0, 0
        self.venue_ok_at = clock()
        self.counts = collections.Counter()
        self.outbox = asyncio.Queue()
        self.geo_at, self.geo_last, self.disk_at = 0.0, None, 0.0
        self.kick = False
        self.reported = set(self.state.get("reported") or [])
        self.polls_fh, self.polls_day, self.polls_sync = None, None, 0.0
        self.absent = collections.Counter()
        self.loss_since = None
        self.read_oids = set()          # the orders whose end after_fill read: each read once
        import httpx
        self.transient = (OSError, asyncio.TimeoutError, httpx.HTTPError) + ((k.E.PolymarketError,) if k else ())

    # -- the records ------------------------------------------------------------------------------------------
    def save(self):
        self.state["held"] = {m.cid: m.member_doc for m in self.markets.values() if m.holds()}
        self.state["reported"] = sorted(self.reported)[-10:]
        write_json_atomic(self.p.state, self.state)

    def say(self, text):
        self.outbox.put_nowait(text)

    # -- the markets ------------------------------------------------------------------------------------------
    def build(self, sel, d0):
        """Today's members as markets; a market held from an earlier day kept, a member no longer."""
        keep = {cid: m for cid, m in self.markets.items() if m.holds() or m.quoting()}
        for m in keep.values():
            m.member = False
        new = {}
        for mem in sel["members"]:
            m = keep.pop(mem["condition_id"], None) or Market(mem, (sel.get("clob") or {}).get(mem["condition_id"]), d0)
            m.member, m.d0, m.member_doc = True, d0, mem
            m.moved, m.comp, m.polled_at, m.refusals = False, None, 0.0, 0
            new[m.cid] = m
        new.update(keep)
        self.markets = new
        self.by_tok = {m.toks[0]: m for m in new.values()}
        self.tokens_version += 1
        self.built_d0 = d0

    def candidates(self):
        """The markets rule W may quote today, in the selection's rank: members of a proved kind whose minimum
        size is at most W_MS_MAX and at least the venue's minimum order size."""
        return sorted((m for m in self.markets.values() if m.member and m.kind in self.kinds
                       and m.ms <= self.W.W_MS_MAX and (m.min_order is None or m.ms >= m.min_order)),
                      key=lambda m: m.rank)

    def stream_tokens(self):
        toks = [m.toks[0] for m in self.candidates()]
        toks += [m.toks[0] for m in self.markets.values() if m.holds() and m.toks[0] not in toks]
        return toks

    def blind(self, now):
        return not self.stream_up and now - self.down_since >= self.c.blind_s

    def wants(self, m, now):
        """The orders rule W wants on m now: {side: (op, outcome index, price, first token's price) or None}."""
        none = {"b": None, "a": None}
        if (self.reason or not m.member or m.kind not in self.kinds or not m.book.seeded or now < m.paused_until
                or m.expect is not None or self.blind(now) or now - self.venue_ok_at > 120 or m.refusals >= 3):
            return none
        bb, ba = m.book.touch(m.ours(now))
        tb, ta = quote_targets(self.W, m, bb, ba)
        tb, ta = capped(self.W, tb, ta, m.x, m.ms)
        m.decided = (bb, ba, tb, ta)
        want = {}
        for side, tgt in (("b", tb), ("a", ta)):
            if tgt is None:
                want[side] = None
            else:
                op, oi, px = order_of(side, tgt, m.yes, m.no, m.ms, self.sell_ok.get(m.kind) is True)
                want[side] = (op, oi, px, tgt)
        return want

    def free_cash(self):
        if not isinstance(self.cash, int):
            return None
        held = sum(reserve_of(o["op"], o["px"], o["size"] - o["matched"]) for m in self.markets.values()
                   for o in m.orders.values() if o is not None)
        return self.cash - held - CASH_KEEP

    def may_open(self, m, w):
        if not m.quoting() and sum(1 for x in self.markets.values() if x.quoting()) >= N_QUOTE:
            return False
        if not m.holds() and sum(1 for x in self.markets.values() if x.holds()) >= N_HOLD:
            return False
        if self.clock() < m.cool_until:
            return False
        if w[0] == "BUY":
            free = self.free_cash()
            return free is not None and reserve_of("BUY", w[2], m.ms) <= free
        return True

    # -- orders -----------------------------------------------------------------------------------------------
    async def place(self, m, side, w):
        op, oi, px, ypx = w
        o = {"oid": None, "op": op, "oi": oi, "tok": m.toks[oi], "px": px, "ypx": ypx, "size": m.ms, "matched": 0,
             "placed": self.clock(), "state": "sent"}
        m.orders[side] = o
        self.j.write("place", cid=m.cid, side=side, op=op, oi=oi, px=px, ypx=ypx, size=m.ms, tick=m.book.tick,
                     decided=m.decided)
        r = await self.v.place(o["tok"], op, px, m.ms, m.book.tick)
        self.venue_ok_at = self.clock()
        self.counts["place " + r["result"].split(" ")[0]] += 1
        if r["oid"] is not None:
            o.update(oid=r["oid"], state="live", placed=self.clock())
            self.j.write("placed", cid=m.cid, side=side, oid=r["oid"], ms=r["ms"], result=r["result"])
            return True
        m.orders[side] = None
        self.j.write("refused", cid=m.cid, side=side, result=r["result"], words=r["words"], ms=r["ms"])
        if r["result"] == "crosses":
            m.dirty = True
        else:
            m.refusals += 1
            m.cool_until = self.clock() + 60
            if m.refusals == 3:
                self.say("L1 · рынок «%s» оставлен до конца дня: биржа трижды отклонила заявку (%s)" % (
                    m.slug, r["words"]))
        return False

    async def cancel_quiet(self, m, side):
        """One order of ours cancelled by its id: True where the venue lists it canceled. An order still being
        placed is left to its placement's answer and the next decision."""
        o = m.orders[side]
        if o is None:
            return True
        if o["oid"] is None:
            return False
        canceled, nc = await self.v.cancel([o["oid"]])
        self.venue_ok_at = self.clock()
        if o["oid"] in canceled:
            m.leave(side, self.clock(), self.c.ghost_s)
            self.j.write("canceled", cid=m.cid, side=side, oid=o["oid"])
            return True
        self.j.write("cancel-refused", cid=m.cid, side=side, oid=o["oid"], words=nc.get(o["oid"]))
        return False

    async def cancel(self, m, side):
        """An order of ours cancelled; one the venue does not cancel is read as a fill (after_fill)."""
        o = m.orders[side]
        if await self.cancel_quiet(m, side):
            return True
        if o is not None and o["oid"] is not None:
            await self.after_fill(m, [o])
        return False

    async def act(self, m, now):
        async with m.lock:
            await self._act(m, now)

    async def _act(self, m, now):
        want = self.wants(m, now)
        for side in ("b", "a"):
            o, w = m.orders[side], want[side]
            if o is not None and o["state"] != "live":
                continue
            if w is None:
                if o is not None:
                    await self.cancel(m, side)
                continue
            if o is not None:
                if (o["op"], o["oi"], o["px"]) == w[:3] and o["size"] - o["matched"] >= m.ms:
                    continue
                if now - o["placed"] < self.c.dwell_s:
                    continue
                if not await self.cancel(m, side):
                    continue
            if self.may_open(m, w):
                await self.place(m, side, w)

    async def cancel_market(self, m):
        async with m.lock:
            for side in ("b", "a"):
                if m.orders[side] is not None:
                    await self.cancel(m, side)

    # -- fills ------------------------------------------------------------------------------------------------
    async def reconcile(self):
        """The wallet's open orders by this key against ours: a matched size grown is a fill; an order of ours
        absent at two reads, five seconds after its placement, is gone - its trades say whether it filled; an
        order not ours is cancelled."""
        oo = await self.v.open_orders()
        self.venue_ok_at = now = self.clock()
        by_id = {o["id"]: o for o in oo}
        ours = {}
        for m in self.markets.values():
            for side, o in m.orders.items():
                if o is not None and o["oid"] is not None:
                    ours[o["oid"]] = (m, side, o)
        foreign = [i for i in by_id if i not in ours]
        sending = any(o is not None and o["oid"] is None for m in self.markets.values() for o in m.orders.values())
        if foreign and not sending:
            canceled, _nc = await self.v.cancel(foreign)
            self.j.write("foreign", n=len(foreign), canceled=len(canceled))
        hit = collections.defaultdict(list)
        for oid, (m, side, o) in ours.items():
            w = by_id.get(oid)
            if w is not None:
                self.absent.pop(oid, None)
                if w["matched"] > o["matched"]:
                    hit[m.cid].append(o)
            elif now - o["placed"] >= self.c.gone_after_s:
                self.absent[oid] += 1
                if self.absent[oid] >= 2:
                    hit[m.cid].append(o)
        for cid, os_ in hit.items():
            m = self.markets[cid]
            async with m.lock:
                await self.after_fill(m, os_)
        for m in list(self.markets.values()):
            if m.expect is not None and now >= m.verify_at:
                async with m.lock:
                    await self.verify(m, now)

    async def after_fill(self, m, orders):
        """A market whose order filled or left the book unasked, its lock held: every order of it cancelled - one
        the venue no longer holds read with the rest, each order's end read once - the market paused until its
        balances show the fills its trades read, the holdings meanwhile the ledger's, the cash again; a message for
        each fill."""
        now = self.clock()
        m.paused_until = now + self.c.pause_s
        orders = [o for o in orders if o is not None and o["oid"] is not None and o["oid"] not in self.read_oids]
        for side in ("b", "a"):
            o = m.orders[side]
            if o is None or o["oid"] is None:
                continue
            if not await self.cancel_quiet(m, side):
                m.leave(side, self.clock(), self.c.ghost_s)
                if o not in orders:
                    orders.append(o)
        oids = {o["oid"] for o in orders}
        self.read_oids |= oids
        fills = await self.v.fills_of(m.cid, min(o["placed"] for o in orders) - 60, oids) if oids else {}
        yes0, no0 = m.yes, m.no
        for o in orders:
            f = fills.get(o["oid"], 0)
            sign = 1 if o["op"] == "BUY" else -1
            if o["oi"] == 0:
                m.yes += sign * f
            else:
                m.no += sign * f
        if (m.yes, m.no) != (yes0, no0):
            m.expect, m.verify_at, m.expect_since = (m.yes, m.no), now + self.c.pause_s, now
        self.cash = await self.chain.cash()
        self.cash_at = self.clock()
        for o in orders:
            self.absent.pop(o["oid"], None)
            f = fills.get(o["oid"], 0)
            self.j.write("fill" if f else "gone", cid=m.cid, oid=o["oid"], op=o["op"], oi=o["oi"], px=o["px"],
                         size=o["size"], matched=f, yes=m.yes, no=m.no, cash=self.cash)
            if f:
                self.counts["fills"] += 1
                eq = equity_of(self.cash, self.markets.values())
                self.say("L1 · исполнение · %s: %s %s «%s» по %s · позиция «%s» %s, «%s» %s · капитал %s (старт %s)"
                         % (m.slug, "куплено" if o["op"] == "BUY" else "продано", size_text(f),
                            m.outcomes[o["oi"]], px_text(o["px"]), m.outcomes[0], size_text(m.yes),
                            m.outcomes[1], size_text(m.no), usd2(eq), usd2(self.state.get("e0"))))
            else:
                self.counts["gone"] += 1
        if (m.yes, m.no) != (yes0, no0) or m.holds():
            self.save()
        m.dirty = True

    async def verify(self, m, now):
        """The ledger's holdings against the venue's balances, read again: equal, or five minutes past the fill,
        the market quotes again on the balances; else it waits PAUSE_S more."""
        yes = await self.v.balance_of(m.kind, m.toks[0])
        no = await self.v.balance_of(m.kind, m.toks[1])
        if (yes, no) == m.expect or now - m.expect_since >= 300:
            if (yes, no) != m.expect:
                self.j.write("balance-differs", cid=m.cid, ledger=list(m.expect), venue=[yes, no])
            m.yes, m.no, m.expect = yes, no, None
            self.save()
            m.dirty = True
        else:
            m.verify_at = now + self.c.pause_s
    # -- the stop ---------------------------------------------------------------------------------------------
    def end(self, reason, words=None):
        if self.reason is None:
            self.reason, self.reason_words = reason, words
            self.done.set()

    async def clear_orders(self):
        """Every open order of the key cancelled and read gone: (canceled, open after or None)."""
        n = 0
        for _t in range(3):
            try:
                c, _nc = await self.v.cancel_all()
                n += c
                break
            except Exception as exc:     # the stop goes on: the reads below decide
                self.j.write("cancel-all-error", words=said(exc))
                await asyncio.sleep(1)
        left = None
        for _i in range(self.c.stop_reads):
            try:
                oo = await self.v.open_orders()
                left = len(oo)
                if not oo:
                    break
                await self.v.cancel([o["id"] for o in oo])
            except Exception as exc:
                self.j.write("open-read-error", words=said(exc))
            await asyncio.sleep(1)
        for m in self.markets.values():
            m.orders = {"b": None, "a": None}
        return n, left

    async def halt(self, reason, record, words=None):
        """The stop: every open order cancelled and read gone; where `record`, the stop record written; the
        Boss told. Returns the record."""
        n, left = await self.clear_orders()
        eq = equity_of(self.cash, self.markets.values())
        rec = {"at": int(self.clock()), "reason": reason, "words": words or STOP_WORDS.get(reason, reason),
               "canceled": n, "open_after": left, "equity": eq, "e0": self.state.get("e0")}
        wrote = write_stop(self.p, rec) if record else False
        self.j.write("stop", record=wrote, **rec)
        text = "L1 остановлен: %s. Отменено заявок: %d; открытых после: %s; капитал %s (старт %s).%s" % (
            rec["words"], n, "—" if left is None else left, usd2(eq), usd2(self.state.get("e0")),
            " Повторный запуск — только после снятия стопа на хосте." if wrote else "")
        try:
            await asyncio.wait_for(self.tg.send(text), timeout=20)
        except Exception as exc:
            self.j.write("tg-error", words=said(exc))
        return dict(rec, written=wrote)

    # -- the tasks ----------------------------------------------------------------------------------------------
    async def t_heartbeat(self):
        while True:
            ok = await self.v.heartbeat(clock=self.clock)
            if ok:
                self.venue_ok_at = self.clock()
            elif self.clock() - self.v.hb_last > self.c.hb_late_s:
                self.kick = True
            await asyncio.sleep(self.c.hb_s)

    async def t_quote(self):
        last_full = 0.0
        while True:
            now = self.clock()
            full = now - last_full >= self.c.full_s
            if full:
                last_full = now
            if self.blind(now) and any(m.quoting() for m in self.markets.values()):
                for m in list(self.markets.values()):
                    await self.cancel_market(m)
                self.j.write("blind", since=round(self.down_since, 3))
            for m in sorted(self.markets.values(), key=lambda x: (not x.member, x.rank)):
                if self.reason:
                    return
                if m.dirty or full:
                    m.dirty = False
                    try:
                        await self.act(m, self.clock())
                    except self.transient as exc:     # the venue or the path to it: the market decided again later
                        self.j.write("venue-error", where="act", cid=m.cid, words=said(exc))
                        m.dirty = True
                        await asyncio.sleep(1)
            await asyncio.sleep(self.c.quote_s)

    async def t_reconcile(self):
        while True:
            try:
                await self.reconcile()
            except self.transient as exc:             # read again at the next turn
                self.j.write("venue-error", where="reconcile", words=said(exc))
            for _i in range(int(self.c.reconcile_s / 0.25) or 1):
                if self.kick:
                    break
                await asyncio.sleep(0.25)
            self.kick = False

    async def poll(self, m):
        path = self.R.CLOB_REWARDS_URL[len(ORIGINS["clob"]):].format(condition_id=m.cid)
        status, body, reason = await self.net.call("GET", "clob", path, timeout=5)
        now = self.clock()
        m.polled_at = now if status == 200 else now - self.c.poll_s + 30
        self.store_poll(now, m.cid, status, body)
        if status != 200:
            self.j.write("poll", cid=m.cid, status=status or reason)
            return None
        row = poll_row(json.loads(body, parse_float=D), date_of(day_of(now)))
        m.polls += 1
        if row is None:
            m.comp = None
        else:
            if not m.moved and tuple(row[2:]) != (m.ms, m.vu):
                m.moved = True
                self.j.write("moved", cid=m.cid, ms=str(row[2]), vu=str(row[3]))
            m.comp = row[1]
        self.j.write("poll", cid=m.cid, status=200, rate=str(row[0]) if row else None,
                     comp=str(row[1]) if row else None, terms=[str(x) for x in row[2:]] if row else None,
                     sha256=sha256_bytes(body))
        m.dirty = True
        return row

    def store_poll(self, now, cid, status, body):
        day = date_of(day_of(now))
        if day != self.polls_day:
            self.close_polls()
            ensure_dir(self.p.polls)
            self.polls_fh = gzip.open(os.path.join(self.p.polls, day + ".jsonl.gz"), "ab", compresslevel=6)
            self.polls_day = day
        line = {"recv_ns": time.time_ns(), "cid": cid, "status": status,
                "raw": body.decode("utf-8", "replace") if status == 200 else None}
        self.polls_fh.write((json.dumps(line, separators=(",", ":")) + "\n").encode())
        if now - self.polls_sync >= 60:
            import zlib
            self.polls_fh.flush(zlib.Z_SYNC_FLUSH)
            self.polls_sync = now

    def close_polls(self):
        if self.polls_fh is not None:
            self.polls_fh.close()
            self.polls_fh = None

    async def t_polls(self):
        while True:
            now = self.clock()
            due = [m for m in self.candidates() if now - m.polled_at >= self.c.poll_s]
            if not due:
                await asyncio.sleep(1)
                continue
            await self.poll(min(due, key=lambda m: (m.polled_at, m.rank)))
            await asyncio.sleep(0.2)

    def on_frame(self, raw):
        for it in frame_items(raw):
            et = it.get("event_type")
            if et == "price_change":
                m = self.markets.get(it.get("market"))
                if m is None or not m.book.seeded:
                    continue
                for pc in it.get("price_changes") or []:
                    if pc.get("asset_id") == m.toks[0]:
                        try:
                            m.book.change("b" if pc["side"] == "BUY" else "a", self.W.price_int(pc["price"]),
                                          self.W.size_int(pc["size"]))
                        except (AssertionError, KeyError, TypeError):
                            self.counts["bad entries"] += 1
                m.book.frames += 1
                m.dirty = True
                continue
            m = self.by_tok.get(it.get("asset_id"))
            if m is None:
                continue
            if et == "book":
                try:
                    bids = {self.W.price_int(x["price"]): self.W.size_int(x["size"]) for x in it["bids"]}
                    asks = {self.W.price_int(x["price"]): self.W.size_int(x["size"]) for x in it["asks"]}
                except (AssertionError, KeyError, TypeError):
                    self.counts["bad books"] += 1
                    continue
                ts = it.get("tick_size")
                m.book.seed(bids, asks, self.W.price_int(ts) if ts in ("0.1", "0.01", "0.001") else None)
                m.book.frames += 1
                m.dirty = True
            elif et == "tick_size_change" and it.get("new_tick_size") in ("0.1", "0.01", "0.001"):
                m.book.tick = self.W.price_int(it["new_tick_size"])
                m.dirty = True
            elif et == "last_trade_price":
                try:
                    p = self.W.price_int(it.get("price"))
                except (AssertionError, TypeError):
                    continue
                if any(o is not None and o["ypx"] == p for o in m.orders.values()):
                    self.kick = True

    def stream_down(self):
        if self.stream_up:
            self.down_since = self.clock()
        self.stream_up = False
        for m in self.markets.values():
            m.book.clear()

    async def stream_session(self, url, toks, once=None):
        """One session of the market channel: the subscribe frame, the frames into the books, the text PING every
        PING_S; it ends on silence, on a new set of tokens, on the unit's end, or - where `once` - when every
        token in it is seeded or `once` seconds pass."""
        from websockets.asyncio.client import connect
        version = self.tokens_version
        t0 = self.clock()
        async with connect(url, open_timeout=10, close_timeout=2, ping_interval=None, max_size=16777216,
                           max_queue=16, compression=None, user_agent_header=UA, proxy=None,
                           family=socket.AF_INET) as ws:
            await ws.send(json.dumps({"assets_ids": list(toks), "type": "market"}, separators=(",", ":")))
            self.stream_up, self.last_frame = True, self.clock()
            self.j.write("stream", tokens=len(toks))

            async def pinger():
                while True:
                    await asyncio.sleep(self.c.ping_s)
                    await ws.send("PING")

            async def watch():
                while True:
                    await asyncio.sleep(0.5)
                    now = self.clock()
                    seeded = once is not None and all(self.by_tok[t].book.seeded for t in toks if t in self.by_tok)
                    if (now - self.last_frame > self.c.silence_s or version != self.tokens_version or self.reason
                            or seeded or (once is not None and now - t0 > once)):
                        await ws.close()
                        return
            tasks = [asyncio.create_task(pinger()), asyncio.create_task(watch())]
            try:
                async for raw in ws:
                    self.last_frame = self.clock()
                    self.on_frame(raw)
            finally:
                for t in tasks:
                    t.cancel()
                await asyncio.gather(*tasks, return_exceptions=True)

    async def t_stream(self, url):
        import websockets
        attempt = 0
        while True:
            toks = self.stream_tokens()
            if not toks:
                await asyncio.sleep(1)
                continue
            try:
                await self.stream_session(url, toks)
                attempt = 0
            except (OSError, asyncio.TimeoutError, websockets.exceptions.WebSocketException) as exc:
                self.j.write("stream-error", words=said(exc))
                attempt += 1
            self.stream_down()
            await asyncio.sleep(self.c.backoff_s[min(attempt, len(self.c.backoff_s) - 1)])

    async def t_guard(self):
        while True:
            try:
                await self.guard()
            except self.transient as exc:             # the guard reads again at its next turn
                self.j.write("venue-error", where="guard", words=said(exc))
            await asyncio.sleep(self.c.guard_s)

    async def guard(self):
        now = self.clock()
        cash = await self.chain.cash()
        if isinstance(cash, int):
            self.cash, self.cash_at = cash, now
        eq = equity_of(cash, self.markets.values()) if isinstance(cash, int) else None
        if eq is not None:
            self.equity, self.equity_at = eq, now
            e0 = self.state.get("e0")
            if isinstance(e0, int) and e0 - eq >= LOSS_LIMIT:
                if self.loss_since is None:
                    self.loss_since = now
                    self.j.write("loss-read", equity=eq, e0=e0)
                elif now - self.loss_since >= self.c.loss_confirm_s:
                    self.j.write("loss", equity=eq, e0=e0, since=round(self.loss_since, 3))
                    return self.end("loss")
            else:
                self.loss_since = None
        elif now - self.equity_at >= self.c.equity_unread_s:
            return self.end("equity")
        if now - self.geo_at >= self.c.geo_s:
            self.geo_at = now
            reading, country, st = await geo_read(self.net)
            self.j.write("geo", reading=reading, country=country, status=st)
            if reading == "BLOCKED":
                return self.end("geo")
            if reading != "PASS" and self.geo_last == "PASS":
                self.say("L1 · геоблок не прочитан (%s); заявки работают, следующая проверка через %d мин" % (
                    st, self.c.geo_s // 60))
            self.geo_last = reading
        if now - self.disk_at >= self.c.disk_s:
            self.disk_at = now
            if disk_available("/") < DISK_FLOOR:
                return self.end("disk")
        await self.days(now)

    async def days(self, now):
        """Today's selection where it is not built yet, retried every SELECT_RETRY_S; the next day's from its
        D0 - SELECT_LEAD_S; the switch at its D0, today's members quoted only once its selection is built; the day's
        report after the venue's payouts."""
        want = self.d0 if self.built_d0 != self.d0 else (
            self.d0 + 86400 if now >= self.d0 + 86400 - self.c.select_lead_s else None)
        if want is not None and not (self.sel_next is not None and self.sel_next.get("d0") == want):
            if self.sel_task is None and now >= self.sel_retry_at:
                self.sel_for = want
                self.sel_task = asyncio.create_task(self.selection(want), name="selection")
            elif self.sel_task is not None and self.sel_task.done():
                res, self.sel_task = self.sel_task.result(), None
                if res is None:
                    self.sel_retry_at = now + self.c.select_retry_s
                else:
                    self.sel_next = res
        if now >= self.d0 + 86400:
            self.d0 += 86400
            for m in self.markets.values():
                m.member = False
            self.j.write("day", d0=self.d0)
        if self.built_d0 != self.d0 and self.sel_next is not None and self.sel_next.get("d0") == self.d0:
            self.build(self.sel_next, self.d0)
            self.j.write("built", d0=self.d0, members=len(self.sel_next["members"]),
                         candidates=len(self.candidates()))
        prev = self.d0 - 86400
        if now >= self.d0 + self.c.report_at_s and date_of(prev) not in self.reported:
            await self.report(prev)

    async def selection(self, d0):
        sel = load_selection(self.p, d0)
        if sel is not None:
            return sel
        try:
            sel = await asyncio.to_thread(select_day, d0, self.p, self.get or sync_get(self.origins), self.origins)
            self.j.write("select", d0=d0, members=len(sel["members"]), requests=sel["requests"],
                         seconds=sel["seconds"])
            return sel
        except Exception as exc:     # a failed attempt is tried again SELECT_RETRY_S later, as the reward book does
            self.j.write("select-error", d0=d0, words=said(exc))
            return None

    async def report(self, d0):
        date = date_of(d0)
        try:
            paid = await self.v.earnings(date)
        except Exception as exc:
            paid = None
            self.j.write("earnings-error", date=date, words=said(exc))
        try:
            reb = await self.v.rebates(date)
        except Exception as exc:
            reb = None
            self.j.write("rebates-error", date=date, words=said(exc))
        self.reported.add(date)
        self.save()
        n = self.day_counts(date)
        self.j.write("report", date=date, paid=paid, rebates=reb, **n)
        self.say("L1 · итоги %s UTC: выплачено наград %s pUSD, ребейтов %s; заявок выставлено %d, исполнений %d; "
                 "капитал %s (старт %s, стоп при %s)" % (
                     date, usd2(paid), usd2(reb), n["placed"], n["fills"], usd2(self.equity),
                     usd2(self.state.get("e0")), usd2(self.state["e0"] - LOSS_LIMIT)
                     if isinstance(self.state.get("e0"), int) else "—"))

    def day_counts(self, date):
        n = collections.Counter()
        path = os.path.join(self.p.journal, date + ".jsonl")
        if os.path.exists(path):
            with open(path, encoding="utf-8") as fh:
                for ln in fh:
                    k = (json_of(ln) or {}).get("k")
                    if k in ("placed", "fill"):
                        n[k + ("s" if k == "fill" else "")] += 1
        return {"placed": n["placed"], "fills": n["fills"]}

    async def t_telegram(self):
        offset = self.state.get("tg_offset")
        while True:
            try:
                ups = await self.tg.updates(offset, self.c.tg_poll_s)
            except Exception as exc:
                self.j.write("tg-error", words=said(exc))
                await asyncio.sleep(5)
                continue
            if ups:
                offset = max(u["update_id"] for u in ups if isinstance(u, dict)) + 1
                self.state["tg_offset"] = offset
                self.save()
            for _uid, cmd in chat_commands(ups, self.tg.chat):
                self.j.write("command", cmd=cmd)
                if cmd == "stop":
                    return self.end("stop")
                if cmd == "status":
                    self.say(self.status_text())
                elif cmd in ("start", "other"):
                    self.say("L1 работает. Кнопки: «Стоп» — отменить все заявки и остановить бота; «Статус».")

    async def t_outbox(self):
        while True:
            text = await self.outbox.get()
            try:
                await self.tg.send(text)
                self.j.write("sent", head=text[:40])
            except Exception as exc:
                self.j.write("tg-error", words=said(exc))
            await asyncio.sleep(self.c.tg_gap_s)

    def status_text(self):
        q = sum(1 for m in self.markets.values() if m.quoting())
        h = sum(1 for m in self.markets.values() if m.holds())
        live = sum(1 for m in self.markets.values() for o in m.orders.values() if o is not None)
        e0 = self.state.get("e0")
        return ("L1 · статус: работает с %s UTC; котируется рынков %d из %d (кандидатов %d, в отборе %d); с позицией "
                "%d; заявок %d; капитал %s (старт %s, стоп при %s); heartbeat %s; геоблок %s" % (
                    utc(self.state.get("started_at", 0))[:16].replace("T", " "), q, N_QUOTE, len(self.candidates()),
                    sum(1 for m in self.markets.values() if m.member), h, live, usd2(self.equity), usd2(e0),
                    usd2(e0 - LOSS_LIMIT) if isinstance(e0, int) else "—",
                    ("принят %d, отказ %d" % (self.v.hb_ok, self.v.hb_fail)) if self.hb_on else "выключен",
                    self.geo_last or "—"))

    # -- the run ----------------------------------------------------------------------------------------------
    async def start(self, ws_url):
        """The start: every order of the key cancelled and read gone; today's selection; the held markets'
        balances; the start equity at the first start; the Boss told."""
        n, left = await self.clear_orders()
        if left != 0:
            self.end("stuck")
            return
        now = self.clock()
        self.d0 = day_of(now)
        self.geo_at, self.geo_last = now, "PASS"
        for cid, mem in (self.state.get("held") or {}).items():
            m = Market(mem, None, self.d0)
            m.member, m.member_doc = False, mem
            self.markets[cid] = m
        sel = await self.selection(self.d0)
        if sel is not None:
            self.build(sel, self.d0)
        for m in self.markets.values():
            if not m.member:
                m.yes = await self.v.balance_of(m.kind, m.toks[0])
                m.no = await self.v.balance_of(m.kind, m.toks[1])
        self.by_tok = {m.toks[0]: m for m in self.markets.values()}
        self.cash = await self.chain.cash()
        self.cash_at = self.clock()
        eq = equity_of(self.cash, self.markets.values())
        if "e0" not in self.state:
            if not (isinstance(self.cash, int) and CAPITAL_MIN <= self.cash <= CAPITAL_MAX):
                self.end("capital")
                return
            self.state.update(e0=eq, e0_at=int(now))
        self.equity, self.equity_at = eq, self.clock()
        self.state["started_at"] = int(now)
        self.save()
        self.j.write("start", canceled=n, d0=self.d0, members=sum(1 for m in self.markets.values() if m.member),
                     candidates=len(self.candidates()), held=sum(1 for m in self.markets.values() if m.holds()),
                     kinds=sorted(self.kinds), sell=self.sell_ok, hb=self.hb_on, equity=eq, e0=self.state["e0"])
        self.say("L1 запущен: рынков в отборе %d, кандидатов правила W %d, котирую не больше %d одновременно; "
                 "капитал %s, старт %s, стоп при %s. Кнопки: «Стоп», «Статус»." % (
                     sum(1 for m in self.markets.values() if m.member), len(self.candidates()), N_QUOTE, usd2(eq),
                     usd2(self.state["e0"]), usd2(self.state["e0"] - LOSS_LIMIT)))

    async def run(self, ws_url):
        """The unit to its end: (exit status, the stop's record or None)."""
        loop = asyncio.get_running_loop()
        for sig in (signal.SIGTERM, signal.SIGINT):
            try:
                loop.add_signal_handler(sig, self.end, "term")
            except (NotImplementedError, RuntimeError):
                pass
        tasks = [asyncio.create_task(self.t_outbox(), name="outbox")]
        try:
            await self.start(ws_url)
            if not self.reason:
                coros = {"telegram": self.t_telegram(), "stream": self.t_stream(ws_url), "polls": self.t_polls(),
                         "quote": self.t_quote(), "reconcile": self.t_reconcile(), "guard": self.t_guard()}
                if self.hb_on:
                    coros["heartbeat"] = self.t_heartbeat()
                tasks += [asyncio.create_task(c, name=n) for n, c in coros.items()]
                waiter = asyncio.create_task(self.done.wait(), name="done")
                done, _p = await asyncio.wait(tasks + [waiter], return_when=asyncio.FIRST_COMPLETED)
                for t in done:
                    if t is waiter or self.reason:
                        continue
                    exc = t.exception()
                    self.err = exc or RuntimeError("the task %s ended" % t.get_name())
                    self.end("error", "%s in %s" % (type(self.err).__name__, t.get_name()))
                waiter.cancel()
        except Exception as exc:     # an error of the start: the unit's end decides its exit
            self.err = exc
            self.end("error", "%s at the start" % type(exc).__name__)
        for t in tasks:
            if t.get_name() != "outbox":
                t.cancel()
        await asyncio.gather(*[t for t in tasks if t.get_name() != "outbox"], return_exceptions=True)
        if self.err is not None:
            trace = scrub("".join(traceback.format_exception(self.err)))[-3000:]
            self.j.write("error", words=said(self.err), trace=trace)
            out("SERVE error, its trace masked:\n" + trace)
        record = self.reason not in ("term", "error")
        rec = await self.halt(self.reason, record, self.reason_words)
        if self.reason == "error":
            try:
                await asyncio.wait_for(self.tg.send("L1: ошибка (%s) — заявки сняты, systemd перезапустит бота "
                                                    "через 30 с" % self.reason_words), timeout=20)
            except Exception:
                pass
        t_end = self.clock() + 5
        while not self.outbox.empty() and self.clock() < t_end:
            await asyncio.sleep(0.1)         # the messages queued before the stop go out first
        tasks[0].cancel()
        await asyncio.gather(tasks[0], return_exceptions=True)
        if self.sel_task is not None:
            self.sel_task.cancel()
        self.close_polls()
        self.save()
        code = {"term": TERM_EXIT, "error": ERROR_EXIT}.get(self.reason, STOP_EXIT)
        return code, rec

# ---- G-PROVE: the unit's own request path before it starts (CANON hard rule 14) ---------------------------------

SELF_SHA = sha256_file(os.path.abspath(__file__))


async def wait_seen(unit, oid, present, reads=None, gap=None):
    """The wallet's open orders read until order `oid` is in them (present) or not: (as wanted, its row, reads)."""
    reads, gap = reads or unit.c.seen_reads, gap if gap is not None else unit.c.seen_gap_s
    for i in range(1, reads + 1):
        row = next((o for o in await unit.v.open_orders() if o["id"] == oid), None)
        if (row is not None) == present:
            return True, row, i
        await asyncio.sleep(gap)
    return False, None, reads


async def prove_order(unit, m):
    """One order of the prove on m: a post-only buy of its minimum order size at the lowest price of its tick, on
    its first token, on its second where the first would cross the book."""
    size = m.min_order if isinstance(m.min_order, int) and 100 <= m.min_order <= 2000 else 500
    tick = m.book.tick
    rec = {"placements": [], "px": tick, "size": size, "tick": tick}
    for oi in (0, 1):
        r = await unit.v.place(m.toks[oi], "BUY", tick, size, tick)
        rec["placements"].append({"outcome": oi, "result": r["result"], "ms": r["ms"], "words": r["words"]})
        if r["oid"] is not None:
            rec.update(oid=r["oid"], oi=oi, placed=unit.clock())
            break
        if r["result"] != "crosses":
            break
    unit.counts["prove orders"] += 1 if "oid" in rec else 0
    return rec


def seen_reading(row, o, m):
    return {"price": row["price"] == o["px"], "size": row["size"] == o["size"], "side BUY": row["side"] == "BUY",
            "the token": row["asset"] == m.toks[o["oi"]], "nothing matched": row["matched"] == 0}


async def round_trip(unit, m):
    """The Boss's round trip on m: one order placed, seen in the wallet's open orders, cancelled by its id, seen gone,
    no fill in its trades, the wallet's pUSD on chain unchanged."""
    rt = {"market": m.slug, "kind": m.kind}
    bal0 = await unit.chain.cash()
    o = await prove_order(unit, m)
    rt["placements"] = o["placements"]
    checks = {"placed live": "oid" in o}
    if "oid" in o:
        seen, row, n = await wait_seen(unit, o["oid"], True)
        rt["seen_reads"] = n
        sr = seen_reading(row, o, m) if seen else {}
        checks["seen in the wallet's open orders"] = seen and all(sr.values())
        rt["seen"] = sr
        canceled, nc = await unit.v.cancel([o["oid"]])
        rt["cancel"] = {"canceled": o["oid"] in canceled, "not_canceled": len(nc), "words": sorted(nc.values())[:1]}
        checks["cancelled by its id"] = rt["cancel"]["canceled"] and not nc
        gone, _r, n2 = await wait_seen(unit, o["oid"], False)
        rt["gone_reads"] = n2
        checks["seen gone from them"] = gone
        fills = await unit.v.fills_of(m.cid, o["placed"] - 60, {o["oid"]})
        rt["matched"] = fills.get(o["oid"], 0)
        checks["no fill in its trades"] = rt["matched"] == 0
    bal1 = await unit.chain.cash()
    rt["balance"] = {"before": bal0, "after": bal1}
    checks["the wallet's pUSD on chain unchanged"] = isinstance(bal0, int) and bal0 == bal1
    rt["checks"] = checks
    rt["pass"] = all(checks.values())
    return rt


async def heartbeat_test(unit, m):
    """The order heartbeat's own cancellation: a heartbeat accepted, an order placed and seen while they go on every
    HB_S, then none sent; the order read gone within HB_WAIT_S of the last accepted, no fill, the balance unchanged."""
    hb = {"accepted": await unit.v.heartbeat(clock=unit.clock)}
    if not hb["accepted"]:
        hb.update(pass_=False, why="the venue did not accept the heartbeat")
        return hb

    async def beats():
        while True:
            await asyncio.sleep(unit.c.hb_s)
            await unit.v.heartbeat(clock=unit.clock)
    beat = asyncio.create_task(beats())
    bal0 = await unit.chain.cash()
    try:
        o = await prove_order(unit, m)
        hb["placements"] = o["placements"]
        seen = False
        if "oid" in o:
            seen, row, _n = await wait_seen(unit, o["oid"], True)
            seen = seen and all(seen_reading(row, o, m).values())
    finally:
        beat.cancel()
        await asyncio.gather(beat, return_exceptions=True)
    hb["sends"], hb["refused"] = unit.v.hb_ok, unit.v.hb_fail
    gone = False
    if "oid" in o:
        t_last = unit.v.hb_last
        while unit.clock() - t_last < unit.c.hb_wait_s:
            if not any(x["id"] == o["oid"] for x in await unit.v.open_orders()):
                gone = True
                hb["gone_after_s"] = round(unit.clock() - t_last, 1)
                break
            await asyncio.sleep(2)
        if not gone:
            canceled, _nc = await unit.v.cancel([o["oid"]])
            hb["cancelled_by_id_after_the_wait"] = o["oid"] in canceled
        fills = await unit.v.fills_of(m.cid, o["placed"] - 60, {o["oid"]})
        hb["matched"] = fills.get(o["oid"], 0)
    bal1 = await unit.chain.cash()
    hb["checks"] = {"a heartbeat accepted": True, "placed live and seen": "oid" in o and seen,
                    "gone by the venue within %d s of the last heartbeat" % unit.c.hb_wait_s: gone,
                    "no fill": hb.get("matched") == 0,
                    "the balance unchanged": isinstance(bal0, int) and bal0 == bal1}
    hb["pass_"] = all(hb["checks"].values())
    return hb


async def stop_drill(unit, m, offset):
    """The stop's round trip at the minimum size: an order resting and seen; the Boss's «Стоп» in the pinned chat
    within TG_WAIT_S; the unit's own stop - every order cancelled and read gone, the stop record written; no fill,
    the balance unchanged."""
    dr = {}
    bal0 = await unit.chain.cash()
    o = await prove_order(unit, m)
    dr["placements"] = o["placements"]
    seen = False
    if "oid" in o:
        seen, row, _n = await wait_seen(unit, o["oid"], True)
        seen = seen and all(seen_reading(row, o, m).values())
    pressed = None
    if seen:
        await unit.tg.send("L1 · проверка кнопки «Стоп»: выставлена заявка-проверка — покупка %s по %s, ниже рынка. "
                           "Нажмите «Стоп»: бот снимет все заявки и запишет стоп." % (
                               size_text(o["size"]), px_text(o["px"])))
        t0 = unit.clock()
        while pressed is None and unit.clock() - t0 < unit.c.tg_wait_s:
            ups = await unit.tg.updates(offset, min(unit.c.tg_poll_s, max(1, int(unit.c.tg_wait_s -
                                                                                 (unit.clock() - t0)))))
            if ups:
                offset = max(u["update_id"] for u in ups if isinstance(u, dict)) + 1
            if any(cmd == "stop" for _u, cmd in chat_commands(ups, unit.tg.chat)):
                pressed = round(unit.clock() - t0, 1)
    dr["pressed_after_s"], dr["offset"] = pressed, offset
    if pressed is not None:
        unit.state["tg_offset"] = offset
        rec = await unit.halt("drill", True)
        dr["stop"] = {"canceled": rec["canceled"], "open_after": rec["open_after"], "written": rec["written"]}
    else:
        n, left = await unit.clear_orders()
        dr["cleared"] = {"canceled": n, "open_after": left}
    matched = (await unit.v.fills_of(m.cid, o["placed"] - 60, {o["oid"]})).get(o["oid"], 0) if "oid" in o else None
    bal1 = await unit.chain.cash()
    dr["matched"] = matched
    dr["checks"] = {"placed live and seen": "oid" in o and seen, "«Стоп» pressed": pressed is not None,
                    "every order cancelled and read gone": (dr.get("stop") or {}).get("open_after") == 0
                    and (dr.get("stop") or {}).get("canceled", 0) >= 1,
                    "the stop record written": (dr.get("stop") or {}).get("written") is True,
                    "no fill": matched == 0, "the balance unchanged": isinstance(bal0, int) and bal0 == bal1}
    dr["pass_"] = all(dr["checks"].values())
    return dr


async def prove_flow(paths, cfg, k, env, key_hex, acct, origins=None, get=None, ws_url=None, clock=time.time):
    """G-PROVE's record: every gate's reading and the kinds the unit may quote."""
    net = Net(origins)
    tg = Tg(net, read_token(paths), read_chat(paths))
    j = Journal(paths, clock)
    rec = {"code_sha256": SELF_SHA, "at": int(clock()), "gates": {}}
    g = rec["gates"]
    venue = unit = None
    try:
        reading, country, st = await geo_read(net)
        rec["geo"] = {"reading": reading, "country": country, "status": st}
        g["G-GEO"] = reading == "PASS"
        venue = await Venue.open(k, env, key_hex, acct)
        chain = Chain(net, acct["wallet"])
        f = await account_reads(venue, chain)
        checks = ready_checks(f, acct, clock())
        rec["ready"] = {"facts": ready_lines(f), "checks": checks}
        g["G-READY"] = all(checks.values())
        usable = kinds_usable(f)
        sell = {x: f["approved"][x] is True for x in EXCHANGES}
        rec.update(usable=usable, sell_ok=sell)
        if not (g["G-GEO"] and g["G-READY"]):
            return rec
        me = await tg.call("getMe")
        ups = await tg.updates(None, 0)
        offset = (max(u["update_id"] for u in ups) + 1) if ups else None
        await tg.send("L1 · проверка пути заявки перед запуском: заявки по самой низкой цене, ниже рынка; все будут "
                      "сняты.")
        g["G-TG"] = isinstance(me, dict) and me.get("is_bot") is True
        unit = Unit(paths, cfg, k, venue, chain, net, tg, j, prove_rec={"kinds": usable}, sell_ok=sell,
                    usable=usable, origins=origins, get=get, clock=clock)
        d0 = day_of(clock())
        sel = await unit.selection(d0)
        picks = {}
        if sel is not None:
            unit.build(sel, d0)
            for m in unit.candidates():
                picks.setdefault(m.kind, m)
        rec["select"] = None if sel is None else {
            "members": len(sel["members"]), "candidates": len(unit.candidates()), "requests": sel["requests"],
            "kinds": dict(collections.Counter(m.kind for m in unit.candidates())), "picked": sorted(picks)}
        g["G-SELECT"] = bool(picks)
        if not picks:
            return rec
        first = picks[sorted(picks)[0]]
        row = await unit.poll(first)
        rec["poll"] = {"served": first.polls == 1, "row": row is not None}
        g["G-POLL"] = first.polls == 1
        unit.by_tok = {m.toks[0]: m for m in unit.markets.values()}
        toks = [m.toks[0] for m in picks.values()]
        try:
            await unit.stream_session(ws_url or ORIGINS["ws"] + "/ws/market", toks, once=30)
        except Exception as exc:      # the gate reads the books
            rec["ws_error"] = said(exc)
        rec["ws"] = {"tokens": len(toks), "seeded": sum(1 for m in picks.values() if m.book.seeded),
                     "frames": sum(m.book.frames for m in picks.values())}
        g["G-WS"] = rec["ws"]["seeded"] == len(toks)
        rec["rt"] = {}
        for x in sorted(picks):
            rec["rt"][x] = await round_trip(unit, picks[x])
        g["G-RT"] = all(r["pass"] for r in rec["rt"].values())
        rec["hb"] = await heartbeat_test(unit, first)
        rec["drill"] = await stop_drill(unit, first, offset)
        g["G-STOP"] = rec["drill"]["pass_"]
        unit.save()
        return rec
    except Exception as exc:     # the record is written on every exit (map section 7 item 192)
        rec["error"] = {"words": said(exc), "trace": scrub("".join(traceback.format_exception(exc)))[-3000:]}
        return rec
    finally:
        rec["kinds"] = sorted(x for x, r in (rec.get("rt") or {}).items() if r["pass"])
        rec["heartbeat_accepted"] = bool((rec.get("hb") or {}).get("accepted"))
        rec["pass"] = all(g.get(n) is True for n in ("G-GEO", "G-READY", "G-TG", "G-SELECT", "G-POLL", "G-WS",
                                                     "G-RT", "G-STOP"))
        rec["orders"] = sum(1 for part in [*(rec.get("rt") or {}).values(), rec.get("hb") or {}, rec.get("drill") or {}]
                            for p in part.get("placements", []) if p["result"] in ("live",) or
                            p["result"].startswith("accepted"))
        if venue is not None:
            try:
                if not (rec.get("drill") or {}).get("stop"):
                    n, _nc = await venue.cancel_all()
                    rec["last_cancel_all"] = n
            except Exception as exc:
                rec["last_cancel_all"] = "error %s" % said(exc)
            await venue.close()
        if unit is not None:
            unit.close_polls()
        await net.close()
        j.close()

# ---- the modes ---------------------------------------------------------------------------------------------------


def floors(mem_floor=MEM_FLOOR, disk_floor=DISK_FLOOR):
    m, d = mem_available(), disk_available("/")
    out("MemAvailable %d bytes, floor %d; available on / %d bytes, floor %d" % (m, mem_floor, d, disk_floor))
    return m >= mem_floor and d >= disk_floor


def mode_ready(paths=P):
    assert_live()
    assert floors(), "BLOCKED: below a floor"
    k = client()

    async def flow():
        net = Net()
        venue = await Venue.open(k, k.PRODUCTION, load_session_key(paths), load_account(paths))
        try:
            reading, country, st = await geo_read(net)
            out("G-GEO over IPv4: %s, country %r, status %s" % (reading, country, st))
            f = await account_reads(venue, Chain(net, venue.wallet))
            return reading, f
        finally:
            await venue.close()
            await net.close()
    reading, f = asyncio.run(flow())
    checks = ready_checks(f, load_account(paths), time.time())
    out("READY %s" % ready_lines(f))
    out("READY kinds the unit may buy on: %s; may sell on: %s" % (
        kinds_usable(f), sorted(x for x, v in f["approved"].items() if v is True)))
    for name, v in checks.items():
        out("G-READY %s: %s" % (name, "PASS" if v else "FAIL"))
    ok = all(checks.values()) and reading == "PASS"
    out("G-READY %s: %d of %d, G-GEO %s" % ("PASS" if ok else "FAIL", sum(checks.values()), len(checks), reading))
    return 0 if ok else 4


def mode_prove(paths=P, cfg=C):
    assert_live()
    assert floors(), "BLOCKED: below a floor"
    assert stop_record(paths) is None, "BLOCKED: a stop record stands; the prove runs before the unit's stop"
    earlier = prove_paths(paths)
    assert len(earlier) < 3, "BLOCKED: three prove records stand"
    assert proved(paths, SELF_SHA) is None, "BLOCKED: this code's prove read PASS already"
    synced = ntp_synchronized()
    out("PROVE clock NTP-synchronized: %s" % synced)
    assert synced, "BLOCKED: the clock is not NTP-synchronized"
    k = client()
    rec = asyncio.run(prove_flow(paths, cfg, k, k.PRODUCTION, load_session_key(paths), load_account(paths)))
    return prove_report(paths, rec, len(earlier) + 1)


def prove_report(paths, rec, n):
    path = os.path.join(paths.var, "prove-%d.json" % n)
    nb = write_private(path, (json.dumps(rec, sort_keys=True, indent=1, default=str) + "\n").encode())
    out("PROVE record %s: %d bytes, 0600" % (path, nb))
    if rec.get("error"):
        out("PROVE error, its trace masked:\n%s" % rec["error"]["trace"])
    out("PROVE G-GEO %s; %s" % (rec.get("geo"), (rec.get("ready") or {}).get("facts")))
    for name, v in ((rec.get("ready") or {}).get("checks") or {}).items():
        out("PROVE G-READY %s: %s" % (name, "PASS" if v else "FAIL"))
    out("PROVE select %s; poll %s; ws %s" % (rec.get("select"), rec.get("poll"), rec.get("ws")))
    for x, r in sorted((rec.get("rt") or {}).items()):
        out("PROVE G-RT %s (%s): placements %s; seen in %s reads %s; cancel %s; gone in %s reads; matched %s; "
            "balance %s -> %s" % (KIND_NAMES[x], r["market"], [(p["outcome"], p["result"], p["ms"], p["words"])
                                                                for p in r["placements"]], r.get("seen_reads"),
                                  r.get("seen"), r.get("cancel"), r.get("gone_reads"), r.get("matched"),
                                  units(r["balance"]["before"]), units(r["balance"]["after"])))
        for name, v in r["checks"].items():
            out("PROVE G-RT %s %s: %s" % (x, name, "PASS" if v else "FAIL"))
    hb = rec.get("hb") or {}
    out("PROVE G-HB accepted %s; sends %s, refused %s; gone after %s s; %s" % (
        hb.get("accepted"), hb.get("sends"), hb.get("refused"), hb.get("gone_after_s"),
        {n_: ("PASS" if v else "FAIL") for n_, v in (hb.get("checks") or {}).items()}))
    dr = rec.get("drill") or {}
    out("PROVE G-STOP pressed after %s s; stop %s; matched %s; %s" % (
        dr.get("pressed_after_s"), dr.get("stop"), dr.get("matched"),
        {n_: ("PASS" if v else "FAIL") for n_, v in (dr.get("checks") or {}).items()}))
    for name in ("G-GEO", "G-READY", "G-TG", "G-SELECT", "G-POLL", "G-WS", "G-RT", "G-STOP"):
        out("PROVE %s: %s" % (name, "PASS" if rec["gates"].get(name) is True else "FAIL or not read"))
    out("G-PROVE %s; kinds proved %s; heartbeat accepted %s; orders placed %d; last cancel_all %s" % (
        "PASS" if rec["pass"] else "FAIL", rec["kinds"], rec["heartbeat_accepted"], rec["orders"],
        rec.get("last_cancel_all", "not needed: the stop cancelled")))
    return 0 if rec["pass"] else 4


def mode_serve(paths=P, cfg=C, origins=None, get=None, ws_url=None, k=None, env=None):
    """The unit. Exit 3 - a stop - with no request to the venue where the stop record stands."""
    if k is None:
        assert_live()
    st = stop_record(paths)
    if st is not None:
        out("SERVE the stop record stands (%s at %s): no request, exit 3" % (st.get("reason"), utc(st.get("at", 0))))
        return STOP_EXIT
    prove = proved(paths, SELF_SHA)
    if prove is None:
        out("SERVE no prove of this code read PASS: refused, exit 2")
        return REFUSE_EXIT
    if k is None:
        if not floors():
            out("SERVE below a floor: exit 1, systemd starts it again in 30 s")
            return ERROR_EXIT
        if not ntp_synchronized():
            out("SERVE the clock is not NTP-synchronized: exit 1")
            return ERROR_EXIT
        k = client()
        env = k.PRODUCTION

    async def main():
        net = Net(origins)
        j = Journal(paths)
        venue = None
        try:
            for i in range(20):
                reading, country, stt = await geo_read(net)
                j.write("geo", reading=reading, country=country, status=stt)
                if reading != "UNREAD":
                    break
                await asyncio.sleep(30 if k is not None and origins is None else 0.1)
            acct = load_account(paths)
            venue = await Venue.open(k, env, load_session_key(paths), acct)
            chain = Chain(net, acct["wallet"])
            tg = Tg(net, read_token(paths), read_chat(paths))
            f = await account_reads(venue, chain)
            usable = kinds_usable(f)
            unit = Unit(paths, cfg, k, venue, chain, net, tg, j, prove_rec=prove, usable=usable,
                        sell_ok={x: f["approved"][x] is True for x in EXCHANGES}, origins=origins, get=get)
            why = None
            if reading == "BLOCKED":
                why = "geo"
            elif reading == "UNREAD":
                out("SERVE the geoblock unread at 20 reads: exit 1")
                return ERROR_EXIT
            elif f["closed_only"] is not False or not f["session"]:
                why = "account"
            elif not (isinstance(acct.get("valid_until"), int) and acct["valid_until"] >= time.time() + 86400):
                why = "key"
            if why is not None:
                await unit.halt(why, True)
                return STOP_EXIT
            out("SERVE start: geoblock %s %s; kinds proved %s, usable %s; heartbeat %s" % (
                reading, country, prove.get("kinds"), usable, "on" if unit.hb_on else "off"))
            code, rec = await unit.run(ws_url or ORIGINS["ws"] + "/ws/market")
            out("SERVE end: %s (%s), exit %d; canceled %s, open after %s" % (
                unit.reason, unit.reason_words or STOP_WORDS.get(unit.reason, ""), code, rec.get("canceled"),
                rec.get("open_after")))
            return code
        finally:
            if venue is not None:
                await venue.close()
            await net.close()
            j.close()
    return asyncio.run(main())


def mode_clear_stop(paths=P, origins=None):
    assert_live()
    return clear_stop(paths, origins)


def clear_stop(paths, origins=None):
    """The stop record moved into the stop history, the pinned chat's pending commands consumed, the Boss told."""
    st = stop_record(paths)
    assert st is not None, "BLOCKED: no stop record stands"
    ensure_dir(paths.stops)
    base, k = "stop-%d" % int(st.get("at", time.time())), 1
    dest = os.path.join(paths.stops, base + ".json")
    while os.path.exists(dest):          # two stops inside one second keep two records
        k += 1
        dest = os.path.join(paths.stops, "%s-%d.json" % (base, k))
    os.rename(paths.stop, dest)
    out("CLEAR the stop record (%s at %s) moved to %s" % (st.get("reason"), utc(st.get("at", 0)), dest))
    j = Journal(paths)
    j.write("clear", stop_at=st.get("at"), reason=st.get("reason"))

    async def flow():
        net = Net(origins)
        try:
            tg = Tg(net, read_token(paths), read_chat(paths))
            ups = await tg.updates(None, 0)
            state = load_json(paths.state) or {}
            if ups:
                state["tg_offset"] = max(u["update_id"] for u in ups) + 1
                write_json_atomic(paths.state, state)
                await tg.updates(state["tg_offset"], 0)
            await tg.send("L1 · стоп снят на хосте. Бот запускается только на хосте; о запуске придёт сообщение.")
            return len(ups)
        finally:
            await net.close()
    n = asyncio.run(flow())
    j.close()
    out("CLEAR the chat's pending updates consumed: %d" % n)
    return 0


def mode_status(paths=P):
    """The unit's own records, counts and instants alone."""
    st = stop_record(paths)
    out("STATUS stop record: %s" % ("none" if st is None else "%s at %s" % (st.get("reason"), utc(st.get("at", 0)))))
    for p in prove_paths(paths):
        rec = load_json(p) or {}
        out("STATUS %s: code %s, pass %s, kinds %s, heartbeat accepted %s, orders %s" % (
            os.path.basename(p), (rec.get("code_sha256") or "")[:12], rec.get("pass"), rec.get("kinds"),
            rec.get("heartbeat_accepted"), rec.get("orders")))
    s = load_json(paths.state) or {}
    out("STATUS state: start equity %s at %s; started %s; held %d; reports %s" % (
        units(s.get("e0")), utc(s["e0_at"]) if s.get("e0_at") else "—",
        utc(s["started_at"]) if s.get("started_at") else "—", len(s.get("held") or {}), s.get("reported")))
    if os.path.isdir(paths.journal):
        for name in sorted(os.listdir(paths.journal))[-2:]:
            n, last = collections.Counter(), None
            with open(os.path.join(paths.journal, name), encoding="utf-8") as fh:
                for ln in fh:
                    r = json_of(ln) or {}
                    n[r.get("k")] += 1
                    last = r.get("t", last)
            out("STATUS journal %s: %d lines, last %s; %s" % (name, sum(n.values()), utc(last) if last else "—",
                                                              dict(sorted(n.items()))))
    return 0


def mode_unit(label):
    """The unit as systemd holds it: its file against this file's copy beside the code, its state and exits."""
    props = ("LoadState", "UnitFileState", "ActiveState", "SubState", "Result", "ExecMainStatus", "ExecMainCode",
             "NRestarts", "MainPID", "ActiveEnterTimestamp", "InactiveEnterTimestamp", "MemoryCurrent", "MemoryPeak",
             "Restart", "NeedDaemonReload")
    rc, so, se = run(["systemctl", "show", UNIT] + ["-p" + p for p in props])
    assert rc == 0, "systemctl show: %s" % se.strip()
    kv = dict(ln.split("=", 1) for ln in so.strip().split("\n") if "=" in ln)
    mine = os.path.join(os.path.dirname(os.path.abspath(__file__)), UNIT)
    same = os.path.exists(UNIT_FILE) and os.path.exists(mine) and sha256_file(UNIT_FILE) == sha256_file(mine)
    out("UNIT %s: file installed byte for byte: %s; %s" % (label, same, "; ".join(
        "%s=%s" % (p, kv.get(p, "")) for p in props)))
    return 0


def main(argv):
    if not argv:
        sys.stderr.write(__doc__)
        return 2
    mode, rest = argv[0], argv[1:]
    table = {"serve": (mode_serve, 0), "ready": (mode_ready, 0), "prove": (mode_prove, 0),
             "clear-stop": (mode_clear_stop, 0), "status": (mode_status, 0), "unit": (lambda: mode_unit(rest[0]), 1),
             "selftest": (lambda: mode_selftest(), 0), "sdk-selftest": (lambda: mode_sdk_selftest(), 0)}
    if mode not in table or len(rest) != table[mode][1]:
        sys.stderr.write("l1-bot: refused command line %r\n" % (argv,))
        return 2
    MODE[0] = mode
    try:
        rc = table[mode][0]()
    finally:
        out("peak memory of this run: %d bytes; refused by the hook: %d; lookups %d, requests %d" % (
            peak(), len(REFUSED), COUNTS["lookups"], COUNTS["requests"]))
    return rc

# ---- the self-tests -------------------------------------------------------------------------------------------

SYN_D0 = 1795219200                      # 2026-11-21 00:00 UTC: the synthetic day
SYN_TOKS = {x: (str(int(a * 32, 16)), str(int(b * 32, 16)))     # CTF position IDs: their reserved bits set
            for x, a, b in (("c", "a1", "a2"), ("n", "b1", "b2"), ("w", "c1", "c2"))}


def syn_cid(x):
    return "0x" + {"c": "c1", "n": "d2", "w": "e3"}[x] * 32


def syn_venue(d0=SYN_D0):
    """A synthetic day of the venue's public documents: three reward markets - a CTF one, a negative-risk one,
    and one whose minimum size is above rule W's - each passing TZ-33's rule."""
    end = utc(d0 + 40 * 86400)
    rows, gamma, clob = [], [], {}
    for i, (x, ms, rate) in enumerate((("c", 20, 120), ("n", 10, 90), ("w", 50, 200))):
        cid = syn_cid(x)
        rows.append({"condition_id": cid, "total_daily_rate": rate, "rewards_min_size": ms,
                     "rewards_max_spread": 4.5, "question": "q%d" % i})
        gamma.append({"conditionId": cid, "endDate": end, "events": [{"startTime": utc(d0 - 30 * 86400)}]})
        clob[cid] = {"condition_id": cid, "active": True, "closed": False, "archived": False,
                     "accepting_orders": True, "enable_order_book": True, "seconds_delay": 0,
                     "tokens": [{"token_id": SYN_TOKS[x][0], "outcome": "Yes"},
                                {"token_id": SYN_TOKS[x][1], "outcome": "No"}],
                     "tags": ["Politics"], "neg_risk": x == "n", "market_slug": "syn-%s" % x,
                     "minimum_order_size": 5, "minimum_tick_size": "0.01"}
    return {"rows": rows, "gamma": gamma, "clob": clob}


def syn_get(venue, base="https://clob.polymarket.com", gbase="https://gamma-api.polymarket.com"):
    """A stand-in of the unit's GET over the synthetic documents."""
    def get(url):
        if url.startswith(base + "/rewards/markets/current"):
            raw = json.dumps({"data": venue["rows"], "next_cursor": "LTE=", "limit": 500, "count": len(venue["rows"])})
        elif url.startswith(gbase + "/markets?"):
            q = urllib.parse.parse_qs(urllib.parse.urlsplit(url).query)
            raw = json.dumps([d for d in venue["gamma"] if d["conditionId"] in q.get("condition_ids", [])])
        elif url.startswith(base + "/markets/"):
            d = venue["clob"].get(url.rsplit("/", 1)[1])
            if d is None:
                return {"url": url, "status": 404, "recv_wall_ns": 0, "bytes": 0, "sha256": "", "raw": "",
                        "reason": None}
            raw = json.dumps(d)
        else:
            return {"url": url, "status": 404, "recv_wall_ns": 0, "bytes": 0, "sha256": "", "raw": "", "reason": None}
        return {"url": url, "status": 200, "recv_wall_ns": time.time_ns(), "bytes": len(raw),
                "sha256": sha256_bytes(raw.encode()), "raw": raw, "reason": None}
    return get


def syn_reward_doc(cid, comp=0.5, ms=20, spread=4.5, rate=120, day="2026-11-21", rows=True):
    """A reward document as the venue serves it, its numbers JSON numbers."""
    if not rows:
        return {"data": [], "next_cursor": "LTE="}
    return {"data": [{"condition_id": cid, "market_competitiveness": comp, "rewards_min_size": ms,
                      "rewards_max_spread": spread,
                      "rewards_config": [{"rate_per_day": rate, "start_date": "2026-11-01", "end_date": "2026-12-31"},
                                         {"rate_per_day": 7, "start_date": day, "end_date": day},
                                         {"rate_per_day": 1000, "start_date": "2026-12-01", "end_date": None}]}],
            "next_cursor": "LTE="}


def remove_tree(root):
    """A self-test's tree removed, every path absolute, deepest first."""
    for d, dirs, files in os.walk(root, topdown=False):
        for n in files:
            os.remove(os.path.join(d, n))
        for n in dirs:
            os.rmdir(os.path.join(d, n))
    os.rmdir(root)


def mode_selftest():
    """Every rule of this file that needs no venue client."""
    import tempfile
    count = [0]

    def ok(cond, what):
        count[0] += 1
        assert cond, "SELFTEST FAIL: %s" % what
        out("SELFTEST %d %s" % (count[0], what))

    def fails(fn, exc=AssertionError):
        try:
            fn()
        except exc:
            return True
        return False
    here = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(TEST_ROOT, mode=0o700, exist_ok=True)
    tmp = tempfile.mkdtemp(prefix="selftest-", dir=TEST_ROOT)
    tp = Paths(etc=tmp + "/etc", var=tmp + "/var", svc=here)
    for d in (tp.etc, tp.var):
        os.mkdir(d, 0o700)
    global P
    saved_p = P
    P = tp
    try:
        # -- the audit hook, pure
        pol = lambda mode, ev, *a: policy(mode, ev, a, tp)
        ok(pol("serve", "socket.__new__", None, socket.AF_INET6) and pol("serve", "socket.__new__", None, socket.AF_INET)
           is None and pol("status", "socket.__new__", None, socket.AF_UNIX) is None,
           "an AF_INET6 socket refused, AF_INET and asyncio's AF_UNIX let through")
        ok(pol("serve", "socket.getaddrinfo", CLOB_HOST, 443, socket.AF_INET) is None and
           pol("serve", "socket.getaddrinfo", CLOB_HOST, 443, 0) and
           pol("serve", "socket.getaddrinfo", CLOB_HOST, 443, socket.AF_INET6) and
           pol("serve", "socket.getaddrinfo", "example.com", 443, socket.AF_INET) and
           pol("status", "socket.getaddrinfo", CLOB_HOST, 443, socket.AF_INET) and
           pol("clear-stop", "socket.getaddrinfo", TG_HOST, 443, socket.AF_INET) is None and
           pol("clear-stop", "socket.getaddrinfo", CLOB_HOST, 443, socket.AF_INET),
           "a lookup in AF_INET alone, of a host its mode names alone")
        ok(pol("serve", "socket.connect", None, ("::1", 443, 0, 0)) and pol("serve", "socket.connect", None, "/run/x")
           and pol("serve", "socket.connect", None, ("10.9.8.7", 443)) and
           pol("selftest", "socket.connect", None, ("127.0.0.1", 9)) is None,
           "a connection to an IPv4 address this process resolved alone; an IPv6 or a path refused")
        ok(pol("serve", "subprocess.Popen", "timedatectl", None) is None and pol("serve", "subprocess.Popen", "sh", None)
           and pol("unit", "subprocess.Popen", "systemctl", None) is None and
           pol("status", "subprocess.Popen", "systemctl", None), "a process its mode names alone")
        ok(pol("serve", "open", tp.var + "/journal/x", "a", None) is None and
           pol("serve", "open", tmp + "/elsewhere", "w", None) and pol("serve", "open", tp.key, "r", None) is None and
           pol("status", "open", tp.key, "r", None) and pol("serve", "open", tp.key, "w", None) and
           pol("serve", "open", "/dev/tty", "r", None) and pol("serve", "open", "/var/lib/btc-rewardbook/x", "r", None)
           and pol("serve", "open", tp.var + "/x", None, os.O_WRONLY | os.O_CREAT) is None,
           "writes under the unit's record alone; its credentials read in their modes; no terminal; no capture's store")
        ok(pol("serve", "os.rename", tp.var + "/a", tp.var + "/b") is None and
           pol("serve", "os.rename", tp.var + "/a", tmp + "/b") and pol("serve", "os.remove", tmp + "/x"),
           "a change under the unit's record alone")
        ok(fails(lambda: gai4("127.0.0.1", 80, socket.AF_INET6), GuardError) and
           all(ai[0] == socket.AF_INET for ai in gai4("127.0.0.1", 80)) and "127.0.0.1" in RESOLVED,
           "gai4 asks AF_INET of a lookup that names no family, and refuses any other")
        # -- the frozen rules
        R, W = rules(here)
        cases = {(300, 420, 10, 90): (320, 400), (300, 400, 10, 90): (310, 390), (300, 399, 10, 90): (None, None),
                 (300, 430, 10, 90): (320, 400), (305, 420, 1, 90): (322, 403), (300, 420, 10, 70): (330, 390),
                 (300, 420, 10, 40): (340, 370), (140, 420, 10, 90): (240, 320), (150, 420, 10, 90): (240, 320),
                 (130, 420, 10, 90): (None, None), (150, 440, 10, 90): (None, None), (300, 420, 100, 90): (None, None),
                 (300, 420, 10, 9): (None, None)}
        ok(all(W.w_targets(*a) == b for a, b in cases.items()) and (W.W_MS_MAX, W.W_COMP_MAX, W.CAP_CLIPS) ==
           (2000, 1, 1), "tz45's own w_targets at its own self-test's 13 cases (its lines 3932 to 3940); its "
                         "W_MS_MAX 20 shares, W_COMP_MAX 1, CAP_CLIPS 1")
        ok((R.SET_SIZE, R.WALK_MAX, R.END_MIN_S, R.SELECT_LEAD_S, len(R.EXCLUDED_TAGS)) == (150, 1500, 15 * 86400, 900,
                                                                                            31) and
           R.CLOB_REWARDS_URL == "https://clob.polymarket.com/rewards/markets/{condition_id}",
           "tz33's rule: 150 members, 1,500 walked at most, an end 15 days on, 31 tags, its endpoints")
        bad = os.path.join(tmp, FROZEN["tz45"][0])
        with open(os.path.join(here, FROZEN["tz45"][0]), "rb") as fh:
            data = bytearray(fh.read())
        data[-2] ^= 1
        with open(bad, "wb") as fh:
            fh.write(data)
        ok(fails(lambda: load_frozen(bad, FROZEN["tz45"][1], ("w_targets",), {})) and
           fails(lambda: load_frozen(os.path.join(here, FROZEN["tz45"][0]), FROZEN["tz45"][1], ("no_such",), {})) and
           fails(lambda: load_frozen(os.path.join(here, FROZEN["tz45"][0]), FROZEN["tz45"][1],
                                     ("W_COMP_MAX",), {})),
           "a frozen file of other bytes refused; a name it lacks refused; a name its rules read and nothing gives "
           "refused (W_COMP_MAX reads Fr)")
        # -- rule W in the unit
        m = types.SimpleNamespace(ms=2000, vu=90, tick=10, moved=False, comp=Fr(1, 2))
        ok(quote_targets(W, m, 300, 420) == (320, 400) and quote_targets(W, m, 300, 399) == (None, None) and
           quote_targets(W, m, None, 420) == (None, None),
           "rule W's targets on the touch, ours out: w_targets, nothing on a narrow or one-sided touch")
        ok(quote_targets(W, types.SimpleNamespace(**dict(vars(m), comp=None)), 300, 420) == (None, None) and
           quote_targets(W, types.SimpleNamespace(**dict(vars(m), comp=Fr(101, 100))), 300, 420) == (None, None) and
           quote_targets(W, types.SimpleNamespace(**dict(vars(m), comp=Fr(1))), 300, 420) == (320, 400) and
           quote_targets(W, types.SimpleNamespace(**dict(vars(m), moved=True)), 300, 420) == (None, None) and
           quote_targets(W, types.SimpleNamespace(**dict(vars(m), ms=2001)), 300, 420) == (None, None),
           "nothing before a served poll, above competitiveness 1, after the terms moved, above 20 shares")
        W0 = types.SimpleNamespace(W_MS_MAX=2000, W_COMP_MAX=1, PRICE_UNIT=1000, w_targets=lambda *a: (0, 81))
        W1 = types.SimpleNamespace(W_MS_MAX=2000, W_COMP_MAX=1, PRICE_UNIT=1000, w_targets=lambda *a: (919, 1000))
        ok(quote_targets(W, types.SimpleNamespace(**dict(vars(m), tick=1)), 1, 120) == (20, 101) and
           quote_targets(W0, m, 1, 120) == (None, 81) and quote_targets(W1, m, 1, 120) == (919, None),
           "a target outside (0, 1) quotes nothing on its side, as Day.decide's guard")
        ok(capped(W, 320, 400, 0, 2000) == (320, 400) and capped(W, 320, 400, 2000, 2000) == (None, 400) and
           capped(W, 320, 400, 1999, 2000) == (320, 400) and capped(W, 320, 400, -2000, 2000) == (320, None),
           "the cap: no bid at a position of one size, no ask at minus one size")
        ok(order_of("b", 320, 0, 0, 2000, True) == ("BUY", 0, 320) and order_of("a", 400, 0, 0, 2000, True) ==
           ("BUY", 1, 600) and order_of("a", 400, 2000, 0, 2000, True) == ("SELL", 0, 400) and
           order_of("b", 320, 0, 2000, 2000, True) == ("SELL", 1, 680) and
           order_of("a", 400, 2000, 0, 2000, False) == ("BUY", 1, 600) and
           order_of("a", 400, 1999, 0, 2000, True) == ("BUY", 1, 600),
           "a side's order: a sell of a size held where selling is approved, else a buy - the second token's at the "
           "complement")
        ok(reserve_of("BUY", 320, 2000) == 6400000 and reserve_of("SELL", 400, 2000) == 0 and
           price_text(320, 10) == "0.32" and price_text(322, 1) == "0.322" and price_text(300, 100) == "0.3" and
           fails(lambda: price_text(325, 10)) and fails(lambda: price_text(0, 10)) and size_text(2000) == "20.00" and
           px_text(320) == "0.32" and px_text(322) == "0.322",
           "a buy reserves its price times its size; prices on their tick's grid; sizes to the hundredth")
        ok(kind_of({"token_ids": list(SYN_TOKS["c"]), "neg_risk": False}) == "c" and
           kind_of({"token_ids": list(SYN_TOKS["c"]), "neg_risk": True}) == "n" and
           kind_of({"token_ids": [str(1 << 100), str((1 << 100) + 5)], "neg_risk": False}) == "c" and
           kind_of({"token_ids": [str((7 << 200) | 3), str(5 << 200)], "neg_risk": False}) == "v",
           "a member's exchange by its tokens' reserved bits and its negative-risk flag")
        # -- the book and the frames
        b = Book()
        b.seed({400: 1000, 380: 5000}, {460: 1000, 480: 3000}, 10)
        ok(b.touch() == (400, 460) and b.touch({("b", 400): 1000}) == (380, 460) and
           b.touch({("b", 400): 500}) == (400, 460) and b.touch({("a", 460): 1000, ("a", 480): 3000}) == (400, None),
           "the touch with our own resting sizes taken out of their levels")
        b.change("b", 400, 0)
        b.change("a", 450, 200)
        ok(b.touch() == (380, 450) and frame_items("PONG") == [] and frame_items("[1, {\"a\": 1}]") == [{"a": 1}]
           and frame_items("{\"a\": 2}") == [{"a": 2}] and frame_items("not json") == [],
           "a level emptied and one added; a frame as its items, PONG none")
        mk = Market({"condition_id": syn_cid("c"), "token_ids": list(SYN_TOKS["c"]), "rank": 0, "min_size": "20",
                     "max_spread": "4.5", "rate": "120", "slug": "syn-c", "outcomes": ["Yes", "No"],
                     "neg_risk": False}, {"minimum_order_size": "5"}, SYN_D0)
        ok((mk.ms, mk.vu, mk.kind, mk.min_order, mk.x) == (2000, 90, "c", 500, 0) and
           fails(lambda: Market(dict(mk.member_doc, min_size="20.005"), None, SYN_D0)),
           "a member's minimum size in hundredths, its spread in half-thousandths; a fraction of either refused")
        u = Unit(tp, Cfg(), None, None, None, None, None, Journal(tp), prove_rec={"kinds": ["c"]}, usable=["c"])
        u.markets, u.by_tok = {mk.cid: mk}, {mk.toks[0]: mk}
        u.on_frame(json.dumps([{"event_type": "book", "asset_id": mk.toks[0], "market": mk.cid,
                                "bids": [{"price": "0.30", "size": "100"}], "asks": [{"price": "0.42", "size": "50"}],
                                "tick_size": "0.001"},
                               {"event_type": "book", "asset_id": mk.toks[1], "market": mk.cid,
                                "bids": [{"price": "0.58", "size": "50"}], "asks": []}]))
        ok(mk.book.seeded and mk.book.touch() == (300, 420) and mk.book.tick == 1,
           "a list frame seeds the first token's book and its tick; the second token's book is not read")
        u.on_frame(json.dumps({"event_type": "price_change", "market": mk.cid, "price_changes": [
            {"asset_id": mk.toks[0], "price": "0.31", "size": "10", "side": "BUY"},
            {"asset_id": mk.toks[1], "price": "0.69", "size": "10", "side": "SELL"}]}))
        u.on_frame(json.dumps({"event_type": "tick_size_change", "asset_id": mk.toks[0], "new_tick_size": "0.01"}))
        ok(mk.book.touch() == (310, 420) and mk.book.tick == 10 and u.kick is False,
           "a price_change applied to the first token alone; a tick change read")
        mk.orders["b"] = {"oid": "o1", "op": "BUY", "oi": 0, "tok": mk.toks[0], "px": 330, "ypx": 330, "size": 2000,
                          "matched": 0, "placed": 0.0, "state": "live"}
        u.on_frame(json.dumps({"event_type": "last_trade_price", "asset_id": mk.toks[0], "price": "0.33"}))
        ok(u.kick is True and mk.ours() == {("b", 330): 2000},
           "a trade printed at our own price asks for the open orders at once")
        mk.orders["b"] = None
        # -- the reward poll, against TZ-45's own polls_of on the same stored reply
        ok(poll_row(json.loads(json.dumps(syn_reward_doc(mk.cid)), parse_float=D), "2026-11-21") ==
           (Fr(127), Fr(1, 2), Fr(2000), Fr(90)) and
           poll_row(json.loads(json.dumps(syn_reward_doc(mk.cid, rows=False)), parse_float=D), "2026-11-21") is None,
           "a poll's row: the rate in force that day, the competitiveness, the terms; a page of no row none")
        T45 = load_frozen(os.path.join(here, FROZEN["tz45"][0]), FROZEN["tz45"][1],
                          ("RB_ROOT", "SIZE_UNIT", "_TERM", "terms_of", "utc", "day_dir", "polls_of"),
                          {"Fr": Fr, "D": D, "re": re, "os": os, "gzip": gzip, "json": json, "sys": sys,
                           "collections": collections, "datetime": datetime})
        ddir = os.path.join(tmp, "rb", str(SYN_D0))
        os.makedirs(ddir)
        docs = [syn_reward_doc(mk.cid, comp=0.25), syn_reward_doc(mk.cid, ms=50), syn_reward_doc(mk.cid, rows=False),
                syn_reward_doc(mk.cid, spread=3, rate=5.5)]
        with gzip.open(os.path.join(ddir, "x.rewards.jsonl.gz"), "wt") as fh:
            for i, d in enumerate(docs):
                fh.write(json.dumps({"recv_wall_ns": (SYN_D0 + 60 + i) * 10 ** 9, "condition_id": mk.cid,
                                     "status": 200, "raw": json.dumps(d)}) + "\n")
        theirs, _c = T45.polls_of(SYN_D0, {SYN_D0: [{"rewards": {"file": "x.rewards.jsonl.gz"}}]},
                                  root=os.path.join(tmp, "rb"))
        mine = [poll_row(json.loads(json.dumps(d), parse_float=D), "2026-11-21") for d in docs]
        ok([r for _t, _c2, r in theirs] == mine,
           "poll_row equals TZ-45's own polls_of, row by row, on the same four stored replies")
        # -- the equity, the account, the geoblock, Telegram
        mk.book.seed({300: 1000}, {420: 1000}, 10)
        mk.yes, mk.no = 2000, 0
        ok(equity_of(100000000, [mk]) == 100000000 + 2000 * 300 * 10 and equity_of(None, [mk]) is None,
           "the equity: the cash and the first token held marked at its best bid")
        mk.yes, mk.no = 2000, 500
        e = equity_of(100000000, [mk])
        mk.orders["b"] = {"oid": "o1", "op": "BUY", "oi": 0, "tok": mk.toks[0], "px": 300, "ypx": 300, "size": 1000,
                          "matched": 0, "placed": 0.0, "state": "live"}
        ok(e == 100000000 + 500 * 1000 * 10 + 1500 * 300 * 10 and equity_of(100000000, [mk]) == 100000000 + 500 * 10000,
           "a complete set at 1; a bid level that is ours alone marks nothing")
        mark = mk.mark
        mk.book.clear()
        ok(equity_of(100000000, [mk]) == 100000000 + mark,
           "a book not seeded - the stream down - marks the holdings at their last mark, never at 0")
        mk.orders["b"], mk.yes, mk.no = None, 0, 0
        acct = {"valid_until": int(time.time()) + 100 * 86400}
        f = {"session": True, "closed_only": False, "cash": 100000000, "clob_cash": 100000000,
             "allowance": {"c": 2 ** 256 - 1, "n": 2 ** 256 - 1, "v": 0}, "approved": {"c": True, "n": True, "v": None},
             "open": 0}
        ck = ready_checks(f, acct, time.time())
        ok(all(ck.values()) and len(ck) == 6 and kinds_usable(f) == ["c", "n"] and "0x" not in ready_lines(f),
           "G-READY's six checks on a ready account; the kinds with the maximum allowance; no address printed")
        ok(not ready_checks(dict(f, cash=79999999), acct, time.time())["its pUSD on chain from 80.00 to 150.00"] and
           not ready_checks(dict(f, cash=150000001), acct, time.time())["its pUSD on chain from 80.00 to 150.00"] and
           not all(ready_checks(dict(f, allowance=dict(f["allowance"], c=10 ** 12)), acct, time.time()).values()) and
           not all(ready_checks(dict(f, open=1), acct, time.time()).values()) and
           not all(ready_checks(f, {"valid_until": int(time.time()) + 6 * 86400}, time.time()).values()) and
           not all(ready_checks(dict(f, closed_only=True), acct, time.time()).values()) and
           len(ready_checks(f, acct, time.time(), first=False)) == 5,
           "G-READY fails outside the capital's bounds, below the maximum allowance, on an open order, a key due in "
           "six days, closed-only; a later start reads no capital bound")
        ok(geo_reading(200, {"blocked": False, "country": "BG", "ip": "x"}) == ("PASS", "BG") and
           geo_reading(200, {"blocked": True, "country": "PL"}) == ("BLOCKED", "PL") and
           geo_reading(500, None) == ("UNREAD", None) and geo_reading(200, {"blocked": "no"}) == ("UNREAD", None),
           "G-GEO: PASS, BLOCKED or UNREAD; the address never kept")
        ups = [{"update_id": 5, "message": {"chat": {"id": 42, "type": "private"}, "text": "Стоп"}},
               {"update_id": 6, "message": {"chat": {"id": 43, "type": "private"}, "text": "Стоп"}},
               {"update_id": 7, "message": {"chat": {"id": 42}, "text": " статус "}},
               {"update_id": 8, "message": {"chat": {"id": 42}, "text": "/start"}},
               {"update_id": 9, "message": {"chat": {"id": 42}, "text": "hello"}}, {"update_id": 10}]
        ok(chat_commands(ups, 42) == [(5, "stop"), (7, "status"), (8, "start"), (9, "other")] and
           tg_command("/stop") == "stop" and tg_command("СТОП") == "stop",
           "the pinned chat's commands alone; another chat's «Стоп» ignored")
        # -- the records
        j = Journal(tp)
        j.write("start", n=1)
        j.write("poll", cid="x")
        j.close()
        lines = open(os.path.join(tp.journal, date_of(day_of(time.time())) + ".jsonl")).read().split("\n")
        ok(len(lines) == 3 and json_of(lines[0])["k"] == "start" and
           os.stat(os.path.join(tp.journal, date_of(day_of(time.time())) + ".jsonl")).st_mode & 0o777 == 0o600,
           "the journal: a line an event, 0600")
        ok(write_stop(tp, {"at": 1, "reason": "stop"}) is True and write_stop(tp, {"at": 2, "reason": "loss"}) is False
           and stop_record(tp)["reason"] == "stop", "the stop record by exclusive create: the first stands")
        os.remove(tp.stop)
        write_private(os.path.join(tp.var, "prove-1.json"), json.dumps({"code_sha256": "a", "pass": False}).encode())
        write_private(os.path.join(tp.var, "prove-2.json"), json.dumps({"code_sha256": SELF_SHA, "pass": True,
                                                                        "kinds": ["c"]}).encode())
        ok(proved(tp, SELF_SHA)["kinds"] == ["c"] and proved(tp, "b") is None and len(prove_paths(tp)) == 2,
           "a prove of this code that read PASS, and none of another")
        # -- the selection, through the unit's own fetch, against TZ-33's own StoredFetch on its stored replies
        sel = select_day(SYN_D0, tp, syn_get(syn_venue()), sleep=lambda s: None)
        R33 = load_frozen(os.path.join(here, FROZEN["tz33"][0]), FROZEN["tz33"][1],
                          TZ33_NAMES + ("StoredFetch",), {"json": json, "re": re, "hashlib": hashlib,
                                                          "datetime": datetime, "urllib": urllib, "gzip": gzip,
                                                          "Counter": collections.Counter, "Decimal": D})
        replay = R33.run_rule(R33.StoredFetch(os.path.join(tp.select, "%d.replies.jsonl.gz" % SYN_D0)), SYN_D0)
        ok([x["condition_id"] for x in sel["members"]] == [syn_cid("w"), syn_cid("c"), syn_cid("n")] and
           replay["members"] == json.loads(json.dumps(sel["members"])) and sel["clob"][syn_cid("c")] ==
           {"minimum_order_size": "5", "minimum_tick_size": "0.01", "neg_risk": False} and
           load_selection(tp, SYN_D0)["d0"] == SYN_D0,
           "the day's selection by tz33's run_rule through the unit's fetch; TZ-33's own StoredFetch on the stored "
           "replies gives the same members")
        u2 = Unit(tp, Cfg(), None, None, None, None, None, Journal(tp), prove_rec={"kinds": ["c", "n"]},
                  usable=["c", "n", "v"])
        u2.build(sel, SYN_D0)
        ok([m.kind for m in u2.candidates()] == ["c", "n"] and len(u2.stream_tokens()) == 2,
           "the candidates: members of a proved kind at most 20 shares, in rank; their first tokens streamed")
        ok(said(RuntimeError("approve to exchange 0x" + "Ab" * 20 + " must be  MaxUint256")) ==
           "approve to exchange 0x… must be MaxUint256" and len(said("x" * 999)) == 300,
           "a refusal in the venue's words, addresses masked, one line")
        out("SELFTEST PASS: %d checks, %d passed; refused by the hook: %d" % (count[0], count[0], len(REFUSED)))
        return 0
    finally:
        P = saved_p
        remove_tree(tmp)

class FakeVenue:
    """The self-tests' loopback stand-in of the venue's CLOB, gamma, relayer, Polygon RPC and geoblock, and of
    Telegram, under one port, each by its path's first segment; and of the CLOB's market channel on a second. Its
    book is one book a market, its orders shown in it as the venue shows them; it answers what the venue was
    measured answering - a post-only order that would cross refused, an order heartbeat's id rotated and its lapse
    a cancel-all of the key's orders - and records every request's agent."""

    def __init__(self, k, wallet, session, venue, chat, token, hb_timeout_s=2.0):
        import threading
        self.k, self.wallet, self.session, self.chat, self.token = k, wallet, session.lower(), chat, token
        self.lock = threading.RLock()
        self.seen, self.orders, self.trades, self.sent, self.updates, self.paths = [], {}, [], [], [], []
        self.creds, self.cash, self.cond = {}, 100000000, collections.Counter()
        self.allow = {x.lower(): 2 ** 256 - 1 for x in EXCHANGES.values()}
        self.approved = {(t.lower(), x.lower()): True for x, t in (
            (EXCHANGES["c"], CTF), (EXCHANGES["n"], CTF), (EXCHANGES["v"], POSITIONS))}
        self.blocked, self.closed_only, self.next_update, self.hb, self.hb_timeout = False, False, 1, {}, hb_timeout_s
        self.venue, self.rewards, self.books, self.meta, self.version = venue, {}, {}, {}, 0
        self.on_send, self.posted, self.hb_lapses = [], [], 0
        for x in ("c", "n", "w"):
            cid = syn_cid(x)
            for t in SYN_TOKS[x]:
                self.meta[t] = {"cid": cid, "nr": x == "n", "toks": SYN_TOKS[x], "yes": SYN_TOKS[x][0]}
            self.books[cid] = {"bids": {}, "asks": {}}
            self.rewards[cid] = syn_reward_doc(cid, ms={"c": 20, "n": 10, "w": 50}[x])
        self.closed = False

    # -- the book: others' levels and our orders, in the first token's terms
    def book_of(self, cid):
        bids, asks = dict(self.books[cid]["bids"]), dict(self.books[cid]["asks"])
        for o in self.orders.values():
            if o["cid"] != cid or o["status"] != "LIVE":
                continue
            left = o["size"] - o["matched"]
            yes = self.meta[o["tok"]]["yes"] == o["tok"]
            if (o["side"] == "BUY") == yes:
                p = o["px"] if yes else 1000 - o["px"]
                bids[p] = bids.get(p, 0) + left
            else:
                p = o["px"] if yes else 1000 - o["px"]
                asks[p] = asks.get(p, 0) + left
        return bids, asks

    def set_book(self, cid, bids, asks):
        with self.lock:
            self.books[cid] = {"bids": dict(bids), "asks": dict(asks)}
            self.version += 1

    def book_frame(self, cid, seed=False):
        tok = next(t for t, m in self.meta.items() if m["cid"] == cid and m["yes"] == t)
        bids, asks = self.book_of(cid)
        fr = {"event_type": "book", "asset_id": tok, "market": cid, "timestamp": str(int(time.time() * 1000)),
              "hash": "h", "bids": [{"price": px_text(p), "size": size_text(s)} for p, s in sorted(bids.items())],
              "asks": [{"price": px_text(p), "size": size_text(s)} for p, s in sorted(asks.items(), reverse=True)]}
        if seed:
            fr["tick_size"] = "0.01"
        return fr

    # -- HTTP
    def handle(self, method, path, q, body, h):
        seg, rest = (path.split("/", 2)[1:] + [""])[:2]
        with self.lock:
            self.seen.append((method, seg, h.get("User-Agent")))
            self.paths.append(path)
            self.lapse()
            return getattr(self, "h_" + seg, self.h_none)(method, "/" + rest, q, body, h)

    def h_none(self, method, path, q, body, h):
        return 404, {"error": "no such path"}

    def h_geo(self, method, path, q, body, h):
        return 200, {"blocked": self.blocked, "country": "PL" if self.blocked else "BG", "ip": "203.0.113.9",
                     "region": "22"}

    def h_gamma(self, method, path, q, body, h):
        if path == "/markets":
            ids = q.get("condition_ids", [])
            return 200, [d for d in self.venue["gamma"] if d["conditionId"] in ids]
        return 404, {"error": "not found"}

    def h_relayer(self, method, path, q, body, h):
        if method == "GET" and path == "/deployed":
            return 200, {"deployed": (q.get("address") or [""])[0].lower() == self.wallet.lower()}
        return 404, {"error": "no such path %s %s" % (method, path)}

    def h_rpc(self, method, path, q, body, h):
        call = body["params"][0]
        d, to = call["data"], call["to"].lower()
        if d.startswith("0x" + SEL["balanceOf"]):
            v = self.cash
        elif d.startswith("0x" + SEL["allowance"]):
            v = self.allow.get("0x" + d[98:138], 0)
        elif d.startswith("0x" + SEL["isApprovedForAll"]):
            v = 1 if self.approved.get((to, "0x" + d[98:138])) else 0
        else:
            return 200, {"jsonrpc": "2.0", "id": body["id"], "error": {"code": -32000, "message": "no"}}
        return 200, {"jsonrpc": "2.0", "id": body["id"], "result": "0x%064x" % v}

    def h_tg(self, method, path, q, body, h):
        tok, meth = path.split("/", 2)[1][3:], path.split("/", 2)[2]
        if tok != self.token:
            return 401, {"ok": False, "error_code": 401, "description": "Unauthorized"}
        if meth == "getMe":
            return 200, {"ok": True, "result": {"id": 7, "is_bot": True, "username": "l1_test_bot"}}
        if meth == "sendMessage":
            assert body["chat_id"] == self.chat and body["reply_markup"] == KEYBOARD, body
            self.sent.append(body["text"])
            for rule in list(self.on_send):
                if rule[0] in body["text"]:
                    self.on_send.remove(rule)
                    self.push_update(rule[1], rule[2] if len(rule) > 2 else self.chat)
            return 200, {"ok": True, "result": {"message_id": len(self.sent)}}
        if meth == "getUpdates":
            off = body.get("offset") or 0
            t_end = time.time() + min(int(body.get("timeout") or 0), 2)
            while True:
                ups = [u for u in self.updates if u["update_id"] >= off]
                if ups or time.time() >= t_end:
                    return 200, {"ok": True, "result": ups}
                self.lock.release()
                try:
                    time.sleep(0.05)
                finally:
                    self.lock.acquire()
        return 404, {"ok": False, "error_code": 404, "description": "Not Found"}

    def push_update(self, text, chat=None):
        with self.lock:
            self.updates.append({"update_id": self.next_update, "message": {
                "message_id": self.next_update, "chat": {"id": chat or self.chat, "type": "private"}, "text": text}})
            self.next_update += 1

    def _auth(self, h):
        addr = (h.get("POLY_ADDRESS") or "").lower()
        cred = self.creds.get(addr)
        if not (cred and h.get("POLY_API_KEY") == cred["apiKey"] and h.get("POLY_SIGNATURE")):
            return None
        return cred if addr == self.session else None

    def wire(self, o):
        return {"id": o["id"], "market": o["cid"], "asset_id": o["tok"], "owner": o["owner"],
                "maker_address": self.wallet, "signer_address": self.session, "side": o["side"],
                "price": px_text(o["px"]), "original_size": size_text(o["size"]),
                "size_matched": size_text(o["matched"]), "outcome": "Yes" if self.meta[o["tok"]]["yes"] == o["tok"]
                else "No", "order_type": "GTC", "status": o["status"], "associate_trades": [],
                "created_at": int(o["at"]), "expiration": "0"}

    def h_clob(self, method, path, q, body, h):
        g = {a: b[0] for a, b in q.items()}
        if path in ("/auth/api-key", "/auth/derive-api-key"):
            addr = (h.get("POLY_ADDRESS") or "").lower()
            if method == "POST" and addr in self.creds:
                return 400, {"error": "Could not create api key"}
            self.creds.setdefault(addr, {"apiKey": "k-%d" % len(self.creds), "secret":
                                         __import__("base64").urlsafe_b64encode(os.urandom(32)).decode(),
                                         "passphrase": "pp"})
            return 200, self.creds[addr]
        if path.startswith("/markets-by-token/"):
            return 200, {"condition_id": self.meta[path.rsplit("/", 1)[1]]["cid"]}
        if path.startswith("/clob-markets/"):
            cid = path.rsplit("/", 1)[1]
            mt = next(m for m in self.meta.values() if m["cid"] == cid)
            return 200, {"nr": mt["nr"], "mts": "0.01", "fd": {"r": 0, "e": 1}, "t": [{"t": t} for t in mt["toks"]]}
        if path == "/rewards/markets/current":
            return 200, {"data": self.venue["rows"], "next_cursor": "LTE=", "limit": 500,
                         "count": len(self.venue["rows"])}
        if path.startswith("/rewards/markets/"):
            return 200, self.rewards.get(path.rsplit("/", 1)[1], {"data": [], "next_cursor": "LTE="})
        if path.startswith("/markets/"):
            d = self.venue["clob"].get(path.rsplit("/", 1)[1])
            return (200, d) if d else (404, {"error": "not found"})
        if path == "/rebates/current":
            return 200, []
        if path.startswith("/data/order/"):
            return 200, None             # the venue's answer to a read by id, measured (map section 7 item 192)
        cred = self._auth(h)
        if cred is None:
            return 401, {"error": "Unauthorized/Invalid api key"}
        if path == "/auth/api-keys":
            return 200, {"apiKeys": [cred["apiKey"]]}
        if path == "/auth/ban-status/closed-only":
            return 200, {"closed_only": self.closed_only}
        if path == "/balance-allowance/update":
            return 200, {}
        if path == "/balance-allowance":
            if g.get("asset_type") == "COLLATERAL":
                return 200, {"balance": str(self.cash), "allowances": {EXCHANGES["c"]: str(2 ** 256 - 1)}}
            return 200, {"balance": str(self.cond[g.get("token_id")]), "allowances": {}}
        if path == "/v1/heartbeats":
            reg = self.hb.get(cred["apiKey"])
            want = reg["id"] if reg else ""
            if body.get("heartbeat_id") != want:
                return 400, {"error_msg": "Invalid Heartbeat ID", "heartbeat_id": want}
            new = "hb-%d" % (int(reg["id"][3:]) + 1 if reg else 1)
            self.hb[cred["apiKey"]] = {"id": new, "last": time.time()}
            return 200, {"heartbeat_id": new}
        if path == "/order" and method == "POST":
            o = body["order"]
            assert body.get("postOnly") is True and body.get("orderType") == "GTC" and body["owner"] == cred["apiKey"]
            assert o["maker"] == self.wallet and o["signatureType"] == 3, o
            ma, ta = int(o["makerAmount"]), int(o["takerAmount"])
            size, px = (ta, ma * 1000 // ta) if o["side"] == "BUY" else (ma, ta * 1000 // ma)
            tok = o["tokenId"]
            cid, yes = self.meta[tok]["cid"], self.meta[tok]["yes"] == tok
            bids, asks = self.book_of(cid)
            yp = px if yes else 1000 - px
            crosses = (yp >= min(asks) if asks else False) if (o["side"] == "BUY") == yes else \
                (yp <= max(bids) if bids else False)
            self.posted.append((tok, o["side"], px, size // 10000))
            if crosses:
                return 400, {"error": "invalid post-only order: order crosses book"}
            if o["side"] == "BUY" and ma > self.cash - sum(
                    x["px"] * (x["size"] - x["matched"]) * 10 for x in self.orders.values()
                    if x["status"] == "LIVE" and x["side"] == "BUY"):
                return 400, {"error": "not enough balance / allowance"}
            oid = "0x%064x" % (len(self.orders) + 1)
            self.orders[oid] = {"id": oid, "tok": tok, "cid": cid, "side": o["side"], "px": px, "size": size // 10000,
                                "matched": 0, "status": "LIVE", "owner": cred["apiKey"], "at": time.time()}
            self.version += 1
            return 200, {"success": True, "errorMsg": "", "orderID": oid, "status": "live", "makingAmount": "",
                         "takingAmount": "", "tradeIDs": [], "transactionsHashes": []}
        if path in ("/order", "/orders") and method == "DELETE":
            ids = [body["orderID"]] if path == "/order" else list(body)
            done, nc = [], {}
            for i in ids:
                o = self.orders.get(i)
                if o and o["status"] == "LIVE" and o["owner"] == cred["apiKey"]:
                    o["status"] = "CANCELED"
                    done.append(i)
                else:
                    nc[i] = "order not found" if o is None else "order already matched"
            self.version += 1
            return 200, {"canceled": done, "not_canceled": nc}
        if path == "/cancel-all" and method == "DELETE":
            done = self.cancel_key(cred["apiKey"])
            return 200, {"canceled": done, "not_canceled": {}}
        if path == "/data/wallet-open-orders":
            return 200, {"data": [self.wire(o) for o in self.orders.values() if o["status"] == "LIVE"],
                         "next_cursor": ""}
        if path == "/data/trades":
            after = int(g.get("after") or 0)
            return 200, {"data": [t for t in self.trades if t["market"] == g.get("market") and
                                  t["match_time"] >= after], "next_cursor": "LTE="}
        if path == "/rewards/user/total":
            return 200, [{"asset_address": PUSD, "asset_rate": "1", "date": SYN_D0 * 1000, "earnings": "3.25",
                          "maker_address": self.wallet}]
        return 404, {"error": "no such path %s %s" % (method, path)}

    def cancel_key(self, key):
        done = [o["id"] for o in self.orders.values() if o["status"] == "LIVE" and o["owner"] == key]
        for i in done:
            self.orders[i]["status"] = "CANCELED"
        self.version += 1
        return done

    def lapse(self):
        """An order heartbeat's lapse: a key registered and silent for hb_timeout loses every open order."""
        for key, reg in list(self.hb.items()):
            if time.time() - reg["last"] > self.hb_timeout:
                self.cancel_key(key)
                del self.hb[key]
                self.hb_lapses += 1

    def fill(self, oid, amount):
        """A taker crossing our order for `amount` hundredths: the order, the balances and a trade."""
        with self.lock:
            o = self.orders[oid]
            o["matched"] += amount
            if o["matched"] >= o["size"]:
                o["status"] = "MATCHED"
            sign = 1 if o["side"] == "BUY" else -1
            self.cond[o["tok"]] += sign * amount * 10000
            self.cash -= sign * o["px"] * amount * 10
            t = int(time.time())
            self.trades.append({"id": "t%d" % len(self.trades), "market": o["cid"], "asset_id": o["tok"],
                                "owner": "taker", "maker_address": "0x" + "9" * 40, "taker_order_id": "0x" + "8" * 64,
                                "side": "SELL" if o["side"] == "BUY" else "BUY", "trader_side": "TAKER",
                                "price": px_text(o["px"]), "size": size_text(amount), "outcome": "Yes",
                                "status": "MATCHED", "fee_rate_bps": "0", "bucket_index": 0,
                                "transaction_hash": "0x" + "7" * 64,
                                "maker_orders": [{"order_id": oid, "asset_id": o["tok"], "maker_address": self.wallet,
                                                  "owner": o["owner"], "side": o["side"], "price": px_text(o["px"]),
                                                  "matched_amount": size_text(amount), "outcome": "Yes",
                                                  "fee_rate_bps": "0"}], "match_time": t, "last_update": t})
            self.version += 1

    def live(self, cid=None):
        with self.lock:
            return [dict(o) for o in self.orders.values() if o["status"] == "LIVE" and cid in (None, o["cid"])]

    def serve_http(self):
        import http.server
        import threading
        fv = self

        class H(http.server.BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.1"

            def log_message(self, *_a):
                pass

            def _route(self, method):
                u = urllib.parse.urlsplit(self.path)
                n = int(self.headers.get("Content-Length") or 0)
                raw = self.rfile.read(n) if n else b""
                body = json.loads(raw) if raw else None
                try:
                    code, obj = fv.handle(method, u.path, urllib.parse.parse_qs(u.query), body, self.headers)
                except Exception as exc:    # a stand-in's own fault is a 500 the test sees
                    code, obj = 500, {"error": "%s: %s" % (type(exc).__name__, exc)}
                data = json.dumps(obj).encode()
                try:
                    self.send_response(code)
                    self.send_header("Content-Type", "application/json")
                    self.send_header("Content-Length", str(len(data)))
                    self.end_headers()
                    self.wfile.write(data)
                except (BrokenPipeError, ConnectionResetError):
                    pass                     # the unit closed a long poll at its stop

            def do_GET(self):
                self._route("GET")

            def do_POST(self):
                self._route("POST")

            def do_DELETE(self):
                self._route("DELETE")
        class Srv(http.server.ThreadingHTTPServer):
            daemon_threads = True

            def handle_error(self, request, client_address):
                pass                         # a connection the unit closed at its stop
        srv = Srv(("127.0.0.1", 0), H)
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        self.http = srv
        return "http://127.0.0.1:%d" % srv.server_address[1]

    def serve_ws(self):
        """The market channel: the subscribe frame answered by one list frame of every token's book, then the
        book of a market whose orders or levels moved, and PONG to PING."""
        import threading
        import websockets
        from websockets.asyncio.server import serve
        fv, ready = self, threading.Event()

        async def handler(ws):
            sub = json.loads(await ws.recv())
            toks = sub["assets_ids"]
            cids = [fv.meta[t]["cid"] for t in toks if t in fv.meta]
            with fv.lock:
                await ws.send(json.dumps([fv.book_frame(c, seed=True) for c in cids]))
                seen = fv.version

            async def reader():
                async for msg in ws:
                    if msg == "PING":
                        await ws.send("PONG")
            rt = asyncio.create_task(reader())
            try:
                while not fv.closed:
                    await asyncio.sleep(0.05)
                    with fv.lock:
                        v = fv.version
                        frames = [fv.book_frame(c) for c in cids] if v != seen else []
                    seen = v
                    for fr in frames:
                        await ws.send(json.dumps(fr))
            except websockets.exceptions.ConnectionClosed:
                pass                         # the unit's session ended
            finally:
                rt.cancel()

        def run():
            async def main():
                async with serve(handler, "127.0.0.1", 0, compression=None) as srv:
                    self.ws_port = srv.sockets[0].getsockname()[1]
                    ready.set()
                    while not fv.closed:
                        await asyncio.sleep(0.1)
            asyncio.run(main())
        threading.Thread(target=run, daemon=True).start()
        ready.wait(10)
        return "ws://127.0.0.1:%d/ws/market" % self.ws_port


def test_cfg():
    c = Cfg()
    for k_, v in dict(hb_s=0.5, hb_late_s=3.0, reconcile_s=0.5, quote_s=0.05, full_s=0.5, poll_s=5.0, guard_s=0.5,
                      geo_s=60.0, dwell_s=0.3, ghost_s=1.0, gone_after_s=0.5, pause_s=1.0, blind_s=2.0,
                      silence_s=10.0, ping_s=1.0, backoff_s=(0.2, 0.5), tg_poll_s=1, tg_gap_s=0.05, select_retry_s=1,
                      equity_unread_s=30, seen_reads=20, seen_gap_s=0.2, hb_wait_s=8.0, tg_wait_s=20.0,
                      loss_confirm_s=1.0).items():
        setattr(c, k_, v)
    return c


def mode_sdk_selftest():
    """The unit's flows through the venue's client against the stand-in: G-READY; G-PROVE whole - the round trip on
    both kinds, the heartbeat's lapse, the stop's round trip; the stop record holding a start; its clearing; the unit
    live - quotes as rule W places them, its own orders in the book not chased, a fill read and the cap kept, the
    position sold at the ask, «Стоп»; the loss limit; the geoblock; a signal; every request with this unit's agent."""
    import tempfile
    import threading
    from polymarket._internal import wallet as Wl
    global P
    count = [0]

    def ok(cond, what):
        count[0] += 1
        assert cond, "SDK SELFTEST FAIL: %s" % what
        out("SDK SELFTEST %d %s" % (count[0], what))
    k = client()
    here = os.path.dirname(os.path.abspath(__file__))
    rules(here)
    ok(k.E is not None and socket.getaddrinfo is gai4 and __import__("httpx")._client.USER_AGENT == UA,
       "the client loaded at its pin, its agent this unit's, its lookups through gai4")
    for fam, bad in ((socket.AF_INET6, True), (socket.AF_UNIX, False)):
        try:
            socket.socket(fam, socket.SOCK_STREAM).close()
            refused = False
        except GuardError:
            refused = True
        ok(refused == bad, "the hook live: a socket of family %s %s" % (fam.name, "refused" if bad else "let through"))
    for args in (("localhost", 80, socket.AF_INET6), ("example.com", 443)):
        try:
            socket.getaddrinfo(*args)
            refused = False
        except GuardError:
            refused = True
        ok(refused, "the hook live: a lookup %r refused" % (args,))
    os.makedirs(TEST_ROOT, mode=0o700, exist_ok=True)
    tmp = tempfile.mkdtemp(prefix="sdk-", dir=TEST_ROOT)
    tp = Paths(etc=tmp + "/etc", var=tmp + "/var", svc=here)
    for d in (tp.etc, tp.var):
        os.mkdir(d, 0o700)
    saved_p = P
    P = tp
    fv = None
    try:
        owner = k.Account.create()
        key = "0x" + os.urandom(32).hex()
        session = k.Account.from_key(key).address
        wallet = Wl.derive_beacon_deposit_wallet_address(owner.address, k.PRODUCTION._config.wallet_derivation)
        token, chat = "123456789:" + "A" * 35, 4242
        write_private(tp.key, (key + "\n").encode())
        write_private(tp.token, (token + "\n").encode())
        write_private(tp.chat, b"4242\n")
        now = int(time.time())
        acct = {"owner": owner.address.lower(), "wallet": wallet.lower(), "session_key": session.lower(),
                "scopes": ["CLOB"], "authorized_at": now - 3600, "valid_until": now + 170 * 86400}
        write_json_atomic(tp.account, acct)
        venue_docs = syn_venue(day_of(now))
        fv = FakeVenue(k, wallet, session, venue_docs, chat, token)
        base = fv.serve_http()
        ws_url = fv.serve_ws()
        cid_c, cid_n = syn_cid("c"), syn_cid("n")
        fv.set_book(cid_c, {300: 10000, 290: 5000}, {420: 10000, 430: 8000})
        fv.set_book(cid_n, {400: 10000}, {430: 10000})
        origins = {"geo": base + "/geo", "clob": base + "/clob", "gamma": base + "/gamma", "rpc": base + "/rpc",
                   "tg": base + "/tg"}
        cfg0 = k.PRODUCTION._config
        env = k._create_environment(name="l1-selftest", config=k.dataclasses.replace(
            cfg0, clob_url=base + "/clob", relayer_url=base + "/relayer", gamma_url=base + "/gamma",
            rpc_url=base + "/rpc", relayer_poll_frequency_ms=50, relayer_max_polls=40))
        cfg = test_cfg()

        async def ready_flow():
            net = Net(origins)
            v = await Venue.open(k, env, key, acct)
            try:
                return await account_reads(v, Chain(net, wallet))
            finally:
                await v.close()
                await net.close()
        f = asyncio.run(ready_flow())
        ck = ready_checks(f, acct, time.time())
        ok(all(ck.values()) and f["session"] and kinds_usable(f) == ["c", "n", "v"] and
           all(f["approved"].values()) and f["cash"] == 100000000,
           "G-READY against the stand-in: 6 of 6, a Deposit Wallet signed for by the session key, three kinds usable")
        fv.allow[EXCHANGES["n"].lower()] = 10 ** 9
        f2 = asyncio.run(ready_flow())
        fv.allow[EXCHANGES["n"].lower()] = 2 ** 256 - 1
        ok(kinds_usable(f2) == ["c", "v"], "an exchange's allowance below the maximum: its kind not usable")
        # -- G-PROVE whole
        fv.on_send.append(("Нажмите «Стоп»", "Стоп"))
        fv.push_update("старое сообщение")
        rec = asyncio.run(prove_flow(tp, cfg, k, env, key, acct, origins=origins, ws_url=ws_url))
        rc = prove_report(tp, rec, 1)
        ok(rc == 0 and rec["pass"] and rec["kinds"] == ["c", "n"] and rec["heartbeat_accepted"] and
           rec["hb"]["pass_"] and rec["orders"] == 4 and fv.live() == [] and stop_record(tp)["reason"] == "drill",
           "G-PROVE PASS: geoblock, account, Telegram, selection, poll, stream, the round trip on CTF and "
           "negative-risk, the heartbeat's lapse cancelling the order, the stop's round trip; 4 orders; none left")
        ok(all(r["checks"]["seen in the wallet's open orders"] and r["checks"]["cancelled by its id"] and
               r["checks"]["seen gone from them"] for r in rec["rt"].values()) and
           [p[1:] for p in fv.posted[:2]] == [("BUY", 10, 500), ("BUY", 10, 500)],
           "the Boss's round trip: placed at the lowest price and the minimum order size, seen, cancelled by its id, "
           "seen gone, the balance unchanged")
        ok(fv.hb_lapses == 1 and 0 < rec["hb"]["gone_after_s"] <= 8,
           "the heartbeat: accepted every HB_S, then silent; the venue's lapse cancels the order")
        ok(any("Нажмите «Стоп»" in t for t in fv.sent) and any(t.startswith("L1 остановлен") for t in fv.sent) and
           rec["drill"]["stop"]["canceled"] == 1 and rec["drill"]["stop"]["open_after"] == 0,
           "the stop's round trip: the Boss's «Стоп», the order cancelled and read gone, the record written")
        out_text = json.dumps(rec)
        ok(wallet.lower() not in out_text.lower() and session.lower() not in out_text.lower() and
           "0x" + "0" * 63 not in out_text and key[2:] not in out_text,
           "the prove's record holds no address, no key and no order id")
        # -- the stop record holds a start: no request
        n0 = len(fv.seen)
        rc = mode_serve(tp, cfg, origins=origins, ws_url=ws_url, k=k, env=env)
        ok(rc == STOP_EXIT and len(fv.seen) == n0, "a start with the stop record standing: exit 3, no request at all")
        rc = clear_stop(tp, origins)
        ok(rc == 0 and stop_record(tp) is None and len(os.listdir(tp.stops)) == 1,
           "clear-stop: the record moved into the history, the chat's pending commands consumed")

        # -- the unit live
        def drive(script, timeout=60):
            """mode_serve in this thread; `script` in another, against the stand-in; (exit, script's error)."""
            err = []

            def run():
                try:
                    script()
                except BaseException as exc:      # the test fails below with the script's own error
                    err.append(exc)
                    fv.push_update("Стоп")
            th = threading.Thread(target=run, daemon=True)
            th.start()
            rc_ = mode_serve(tp, cfg, origins=origins, ws_url=ws_url, k=k, env=env)
            th.join(timeout)
            return rc_, err

        def wait_for(cond, what, t=20.0):
            t_end = time.time() + t
            while time.time() < t_end:
                if cond():
                    return
                time.sleep(0.05)
            raise AssertionError("timed out waiting for " + what)
        steps = {}

        def script_live():
            wait_for(lambda: len(fv.live(cid_c)) == 2, "two quotes on the CTF market")
            q = sorted((o["tok"], o["side"], o["px"], o["size"]) for o in fv.live(cid_c))
            steps["quotes"] = q
            time.sleep(1.0)
            steps["churn"] = len([p for p in fv.posted[n_posted:] if fv.meta[p[0]]["cid"] == cid_c])
            bid = next(o for o in fv.live(cid_c) if o["tok"] == SYN_TOKS["c"][0])
            fv.fill(bid["id"], bid["size"])
            wait_for(lambda: any(o["side"] == "SELL" for o in fv.live(cid_c)), "the ask as a sell of the shares held")
            steps["after"] = sorted((o["tok"], o["side"], o["px"], o["size"]) for o in fv.live(cid_c))
            steps["n"] = len(fv.live(cid_n))
            fv.push_update("Статус")
            wait_for(lambda: any(t.startswith("L1 · статус") for t in fv.sent), "the status")
            fv.push_update("Стоп")
        n_sent, n_posted = len(fv.sent), len(fv.posted)
        rc, err = drive(script_live)
        ok(not err and rc == STOP_EXIT and stop_record(tp)["reason"] == "stop" and fv.live() == [],
           "the unit live to the Boss's «Стоп»: exit 3, the record written, no order left")
        ok(steps["quotes"] == sorted([(SYN_TOKS["c"][0], "BUY", 320, 2000), (SYN_TOKS["c"][1], "BUY", 600, 2000)]),
           "rule W's quotes on the touch 0.30-0.42, spread 4.5 c: a buy of 20 at 0.32 and a buy of the second token "
           "at 0.60 for the ask at 0.40")
        ok(steps["churn"] == 2, "its own quotes in the book, shown back by the channel, are not chased: two placed")
        ok(steps["after"] == [(SYN_TOKS["c"][0], "SELL", 400, 2000)],
           "the bid filled: the cap holds the bid back, the ask sells the 20 shares held at 0.40")
        ok(steps["n"] == 0, "a market whose touch is narrower than rule W's width quotes nothing")
        msgs = fv.sent[n_sent:]
        ok(msgs[0].startswith("L1 запущен") and any(t.startswith("L1 · исполнение · syn-c: куплено 20.00 «Yes» по 0.32")
                                                    for t in msgs) and
           any(t.startswith("L1 · статус") for t in msgs) and msgs[-1].startswith("L1 остановлен: «Стоп» из Telegram"),
           "the Boss's chat: the start, the fill, the status, the stop")
        st_ = load_json(tp.state)
        ok(st_["e0"] == 100000000 and cid_c in st_["held"],
           "the start equity recorded at the first start; the market held kept in the unit's state")
        jl = [json_of(x) for x in open(os.path.join(tp.journal, date_of(day_of(time.time())) + ".jsonl"))]
        kinds_ = collections.Counter(r["k"] for r in jl)
        ok(all(kinds_[x] for x in ("start", "place", "placed", "canceled", "fill", "poll", "stream", "command", "stop"))
           and kinds_["refused"] == 0, "the journal: every order, cancel, fill, poll, command and the stop")
        clear_stop(tp, origins)
        # -- the loss limit
        def script_loss():
            wait_for(lambda: len(fv.live(cid_c)) >= 1, "a quote")
            with fv.lock:
                fv.cash -= 30000000
        rc, err = drive(script_loss)
        ok(not err and rc == STOP_EXIT and stop_record(tp)["reason"] == "loss" and fv.live() == [],
           "the loss limit: equity 25 pUSD below the start equity stops the unit, every order cancelled")
        with fv.lock:
            fv.cash += 30000000
        clear_stop(tp, origins)
        # -- the geoblock at the start
        fv.blocked = True
        n0 = len(fv.posted)
        rc = mode_serve(tp, cfg, origins=origins, ws_url=ws_url, k=k, env=env)
        ok(rc == STOP_EXIT and stop_record(tp)["reason"] == "geo" and len(fv.posted) == n0,
           "the geoblock read blocked at the start: the stop record, no order placed")
        fv.blocked = False
        clear_stop(tp, origins)
        # -- a signal: SIGTERM from systemd
        def script_term():
            wait_for(lambda: len(fv.live(cid_c)) >= 1, "a quote")
            os.kill(os.getpid(), signal.SIGTERM)
        rc, err = drive(script_term)
        ok(not err and rc == TERM_EXIT and stop_record(tp) is None and fv.live() == [],
           "SIGTERM: every order cancelled, exit 0, no stop record - systemd's own stop")
        # -- the day's report and the day's switch, on a unit built over the stand-in
        async def day_flow():
            net = Net(origins)
            v = await Venue.open(k, env, key, acct)
            try:
                c2 = test_cfg()
                c2.report_at_s = 86399
                u = Unit(tp, c2, k, v, Chain(net, wallet), net, Tg(net, token, chat), Journal(tp),
                         prove_rec={"kinds": ["c", "n"]}, usable=["c", "n"], origins=origins)
                d0 = day_of(time.time())
                u.d0 = d0 - 86400
                u.build({"members": [], "d0": d0 - 86400}, d0 - 86400)
                await u.days(time.time())
                missing = (u.d0, u.built_d0, len(u.candidates()))
                await asyncio.wait_for(u.sel_task, 10)
                await u.days(time.time())
                switched = (missing, u.d0, u.built_d0, len(u.candidates()))
                await u.report(d0 - 86400)
                return switched, u.outbox.get_nowait()
            finally:
                await v.close()
                await net.close()
        switched, text = asyncio.run(day_flow())
        d0_ = day_of(time.time())
        ok(switched == ((d0_, d0_ - 86400, 0), d0_, d0_, 2),
           "the day's switch: no member quoted before the day's selection is read; once read, its markets built")
        ok(text.startswith("L1 · итоги %s UTC: выплачено наград 3.25 pUSD, ребейтов 0.00" % date_of(
            day_of(time.time()) - 86400)), "the day's report: the venue's paid rewards and rebates, read for the day")
        ok(not any(x.startswith("/clob/data/order/") for x in fv.paths),
           "no order of ours read by its id: the venue answered such a read null (map section 7 item 192)")
        agents = collections.Counter(a for _m, _s, a in fv.seen)
        ok(set(agents) == {UA}, "every request to the stand-in carried this unit's agent: %d" % sum(agents.values()))
        out("SDK SELFTEST PASS: %d checks, %d passed; refused by the hook: %d" % (count[0], count[0], len(REFUSED)))
        return 0
    finally:
        if fv is not None:
            fv.closed = True
            fv.http.shutdown()
        P = saved_p
        remove_tree(tmp)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
```

## Appendix B — the unit file, byte for byte

### `deploy/systemd/l1-bot.service`

```ini file=deploy/systemd/l1-bot.service
# btc-5m-twap: L1's unit, rule W live at the minimum size from the live host in Sofia (TZ-53, CANON PART II).
# Installed byte for byte as /etc/systemd/system/l1-bot.service on the live host alone. Its stop is
# systemctl disable --now; the Boss's is «Стоп» in its Telegram chat; the last, the session key's revocation.
[Unit]
Description=L1 - rule W live at the minimum size, the bot's orders from the live host
Wants=network-online.target
After=network-online.target time-sync.target
StartLimitIntervalSec=3600
StartLimitBurst=5

[Service]
Type=simple
WorkingDirectory=/root/l1-bot-svc
ExecStart=/root/l1-env/bin/python -B -u /root/l1-bot-svc/l1-bot.py serve
Environment=LC_ALL=C TZ=UTC
Restart=on-failure
RestartSec=30
RestartPreventExitStatus=2 3
TimeoutStopSec=60
MemoryMax=384M
NoNewPrivileges=yes
PrivateTmp=yes
ProtectSystem=strict
ReadWritePaths=/var/lib/l1-bot
StandardOutput=append:/var/lib/l1-bot/service.log
StandardError=append:/var/lib/l1-bot/service.log

[Install]
WantedBy=multi-user.target
```

## Appendix C — B-DEPLOY, byte for byte

### `b-deploy.sh`

```bash file=b-deploy.sh
#!/bin/bash
# TZ-53 B-DEPLOY - L1's unit on the live host, one sequence, each step gated on the one before it: the code and the
# unit file installed byte for byte, G-READY, G-PROVE (the Boss presses «Стоп» in Telegram when the bot asks),
# G-HOLD, the stop cleared, G-UNIT and, 15 minutes on, G-LIVE. Started by the Executor or by the Boss with the same
# line, under systemd-run, so that no dropped connection ends it (TZ-53 section 3, step 9). Its log is
# /root/tz53-work/logs/60-deploy.log. A FAIL after the unit was started stops it, systemctl disable --now.
exec >>/root/tz53-work/logs/60-deploy.log 2>&1
export LC_ALL=C TZ=UTC
set -u
W=/root/tz53-work
SVC=/root/l1-bot-svc
VAR=/var/lib/l1-bot
PY=/root/l1-env/bin/python
UNIT=l1-bot.service
SUMS="98851b3c0df447ed7c846edfbf18b9ea1611d12228a4d9a3c1fda3b4f22da214  l1-bot.py
a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670  tz33-reward-book-capture.py
4720e78573e54b1325dd24af7c30e0de59bfb4c1879d309a23fa6bab6b32d2d4  tz45-l0-rule-w.py
a6305d0e7a220ea88f5a4d2be612cac35f3dbe527d7c3b7ed12fd7c47f956266  l1-bot.service"
STARTED=0

say() { printf '%s B-DEPLOY %s\n' "$(date -u +%FT%T.%3NZ)" "$*"; }
prop() { systemctl show "$UNIT" -p "$1" --value; }
props() { systemctl show "$UNIT" -p ActiveState -p SubState -p Result -p ExecMainStatus -p NRestarts -p MainPID \
          -p UnitFileState | tr '\n' ' '; echo; }
eng() { "$PY" -B "$SVC/l1-bot.py" "$@"; }
fail() {
    say "FAIL at $1"
    if [ "$STARTED" = 1 ]; then
        systemctl disable --now "$UNIT"
        say "the unit stopped, disable --now exit=$?: $(props)"
        eng status
    fi
    say "END exit=1"
    exit 1
}

say "BEGIN pid $$ on $(hostname -s)"
[ "$(hostname -s)" = vs-2348 ] || fail "the host: not the live host"

# -- 1. the unit already running: nothing installed, proved or started again ---------------------------------------
if [ "$(prop ActiveState)" = active ]; then
    say "the unit is active already: $(props)"
    STARTED=1
else
    # -- 2. the code and the unit file, byte for byte ---------------------------------------------------------------
    (cd "$W/engine" && printf '%s\n' "$SUMS" | sha256sum -c -) || fail "install: the staged bytes"
    install -d -m 0700 -o root -g root "$SVC" || fail "install: $SVC"
    for f in l1-bot.py tz33-reward-book-capture.py tz45-l0-rule-w.py l1-bot.service; do
        install -m 0600 -o root -g root "$W/engine/$f" "$SVC/$f" || fail "install: $f"
    done
    install -m 0644 -o root -g root "$W/engine/l1-bot.service" "/etc/systemd/system/$UNIT" || fail "install: the unit"
    systemctl daemon-reload || fail "install: daemon-reload"
    (cd "$SVC" && printf '%s\n' "$SUMS" | sha256sum -c -) || fail "install: the installed bytes"
    cmp "$SVC/l1-bot.service" "/etc/systemd/system/$UNIT" || fail "install: the unit file"
    ls -la "$SVC" "/etc/systemd/system/$UNIT"
    say "installed: $(props)"
    [ "$(prop LoadState)" = loaded ] && [ "$(prop UnitFileState)" = disabled ] || fail "install: the unit's state"

    # -- 3. G-READY, waiting up to two hours where the wallet's balance alone is outside its bounds -----------------
    for i in $(seq 1 13); do
        eng ready > "$W/logs/61-ready-$i.log" 2>&1
        rc=$?
        cat "$W/logs/61-ready-$i.log"
        [ "$rc" = 0 ] && break
        n=$(grep -c ': FAIL$' "$W/logs/61-ready-$i.log")
        c=$(grep -c 'its pUSD on chain from .*: FAIL$' "$W/logs/61-ready-$i.log")
        if [ "$n" = 1 ] && [ "$c" = 1 ] && grep -q 'G-GEO PASS$' "$W/logs/61-ready-$i.log" && [ "$i" -lt 13 ]; then
            say "G-READY read $i: the wallet's pUSD outside 80 to 150 alone; read again in 600 s"
            sleep 600
        else
            fail "G-READY, read $i, exit $rc"
        fi
    done

    # -- 4. G-PROVE, once for this code ------------------------------------------------------------------------------
    if /usr/bin/python3 -I -B - "$SVC/l1-bot.py" "$VAR" <<'EOF'
import glob, hashlib, json, sys
code = hashlib.sha256(open(sys.argv[1], "rb").read()).hexdigest()
recs = [json.load(open(p)) for p in sorted(glob.glob(sys.argv[2] + "/prove-[123].json"))]
sys.exit(0 if any(r.get("code_sha256") == code and r.get("pass") is True for r in recs) else 1)
EOF
    then
        say "G-PROVE read PASS for this code already: not run again"
    else
        say "G-PROVE: the bot asks the Boss in Telegram to press «Стоп» once its drill's order rests"
        eng prove || fail "G-PROVE"
    fi

    # -- 5. G-HOLD: the drill's stop record keeps the unit down, then the stop is cleared ---------------------------
    if [ -f "$VAR/stop.json" ]; then
        /usr/bin/python3 -I -B -c 'import json, sys; sys.exit(0 if json.load(open(sys.argv[1])).get("reason") == "drill" else 1)' \
            "$VAR/stop.json" || fail "G-HOLD: a stop record of another reason stands"
        systemctl start "$UNIT"
        say "started with the stop record standing, exit=$?; read in 45 s"
        sleep 45
        say "G-HOLD read: $(props)"
        eng unit hold
        tail -n 3 "$VAR/service.log"
        [ "$(prop ExecMainStatus)" = 3 ] && [ "$(prop NRestarts)" = 0 ] && [ "$(prop ActiveState)" != active ] &&
            [ "$(prop ActiveState)" != activating ] || fail "G-HOLD"
        tail -n 3 "$VAR/service.log" | grep -q 'SERVE the stop record stands' || fail "G-HOLD: the unit's own line"
        tail -n 3 "$VAR/service.log" | grep -q 'lookups 0, requests 0$' || fail "G-HOLD: a request was made"
        systemctl reset-failed "$UNIT"
        say "G-HOLD PASS"
        eng clear-stop || fail "the stop cleared"
    fi
    [ ! -e "$VAR/stop.json" ] || fail "a stop record stands"

    # -- 6. G-UNIT ---------------------------------------------------------------------------------------------------
    STARTED=1
    systemctl enable --now "$UNIT" || fail "G-UNIT: enable --now"
    say "enabled and started; read in 60 s"
    sleep 60
    say "G-UNIT read: $(props)"
    eng unit start
    eng status
    tail -n 20 "$VAR/service.log" | grep -q 'SERVE start: geoblock PASS' || fail "G-UNIT: the unit's start line"
    [ "$(prop ActiveState)" = active ] && [ "$(prop NRestarts)" = 0 ] && [ "$(prop UnitFileState)" = enabled ] ||
        fail "G-UNIT"
    say "G-UNIT PASS"
fi

# -- 7. G-LIVE, 15 minutes after the start ----------------------------------------------------------------------------
PID=$(prop MainPID)
T0=$(date -d "$(prop ActiveEnterTimestamp)" +%s)
WAIT=$(( T0 + 900 - $(date +%s) ))
[ "$WAIT" -gt 0 ] && { say "G-LIVE read in $WAIT s"; sleep "$WAIT"; }
say "G-LIVE read: $(props)"
eng unit live
eng status
[ "$(prop ActiveState)" = active ] && [ "$(prop NRestarts)" = 0 ] && [ "$(prop MainPID)" = "$PID" ] &&
    [ ! -e "$VAR/stop.json" ] || fail "G-LIVE"
say "G-LIVE PASS"
say "END exit=0"
exit 0
```
