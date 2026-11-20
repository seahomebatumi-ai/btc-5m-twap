# TZ-52 — L1, the round trip on the account TZ-51 left: the venue's maximum allowances kept, one order placed and cancelled, the bot's chat pinned

**Canonical filename:** `TZ-52-l1-round-trip.md`. The committed file takes this name and no other.

**Executor model: Claude Opus 5.5.** Two hosts, an authenticated order path proved with money in the wallet.

**Required System Map revision:** `2026-11-21-a` — **it ships with this TZ:** the Boss uploads `SYSTEM-MAP.md` and this file in one upload onto `main` at `b941123`, TZ-51's report, which carries revision `2026-11-20-b`. The revision moves no row and no anchor, adds none and replaces none (CANON hard rule 17): it records TZ-51's BLOCK and the state it left, rewrites §7 item 190 and adds item 191.

**Map sections this TZ rests on**, copied from §10's C8 (map §7 item 174): §0, the fingerprint gate, its table and the signing page; §1, the repository, its TZs and pull requests #48 and #49; §2.6, the reward book — its store's bounds and its reserve; §3, the units, the trees on the host and the session directories; §5, L1's row and the reward book's days; §6, its rows host identity, for TZ host gates; live host; live host identity, for TZ host gates; live host — the venue's geoblock, measured 2026-11-19, TZ-48 and TZ-49, and 2026-11-20, TZ-50; live host — the venue's CLOB from Sofia; language; git remote; egress; venue edge — the `User-Agent`; venue constants; maker incentives; RTDS session limit; disk; disk floors and caps; process supervision; memory; clock; sandbox limit — destructive actions; and harness — background output; §7 items 86, 89, 91, 95, 98, 119, 124, 127, 132, 137, 138, 140, 143, 144, 150, 156, 163, 169, 174, 175, 176, 177, 180, 181, 183, 184, 185, 186, 187, 188, 189, 190 and 191; §8. **And TZ-51 itself**, `CryptoTZ/TZ-51-l1-account-round-trip-rerun.md` on `main`, every section this file does not replace (§0.0 below), and its Appendix A, the base of this TZ's instrument; **and TZ-51's report**, `CryptoReports/TZ-51-l1-account-round-trip-rerun-report.md`, its §1, §2.3 and §3, whose state this TZ starts from.

**Required anchors**, from map §0. A mismatch on any one is BLOCKED before any work:

| anchor | required |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` |
| `A4` — executor contract | `6ac6e10aeabc` |
| `A5` — recorder | `0f6c90451cbd` |
| `A6` — pricer | `729f0bcdbee3` |

**Written authorization (contract §10).** From the live host, IPv4 alone, by this TZ's instrument alone: the anonymous reads TZ-51 §2 item 4 names but the wheels and the signing page; **authenticated** — the CLOB's derivation of the session key's API credentials and its reads by them, `/balance-allowance/update`, **the one order of TZ-51 §1.5**, at most two placements, its cancellation by id and `cancel_all`; Telegram's Bot API by the bot's token — `getMe`, `getMyCommands`, `getUpdates`, one `sendMessage` to the pinned chat. **Nothing is submitted to the relayer:** no owner's signature, no approval, no authorization and no revocation is asked or sent by this run. **No request to any venue outside these modes** — no probe: a refusal is printed by the instrument in the venue's own words (§1.2), and the run does what §1.2 says. From the capture host: `git` and `gh` as TZ-51 §2 item 4, pull request #49 in place of #48.

**Before EXECUTE.** The Boss sends `/start` to his bot in Telegram, from the chat he will read it in — `find-chat` reads the last 24 hours of the bot's messages. Nothing else of his is needed; the run asks again only where `find-chat` finds none (§3 step 11).

**When: begun at any hour**, as TZ-51.

---

## 0. TZ-51's text, renamed, and what this file replaces

### 0.0 The rule

**TZ-51's file is this TZ's text wherever this file says nothing** — its §0 to §9, its blocks, gates, checks and logs — **read with the renaming R:** `TZ-51-l1-account-round-trip-rerun` reads `TZ-52-l1-round-trip`; `tz-51-l1-account-round-trip-rerun`, `tz-52-l1-round-trip`; `tz51`, `tz52`; `TZ-51`, `TZ-52`; `ТЗ-51`, `ТЗ-52`; `2026-11-20-b`, `2026-11-21-a`. So the work tree is `/root/tz52-work` on both hosts, the instrument `research/tz52-l1-account.py`, the branch `tz-52-l1-round-trip`, the report `CryptoReports/TZ-52-l1-round-trip-report.md`, the agent `btc-5m-twap-tz52`. **R does not touch** TZ-51's own file, its Appendix A, its report, its pull request #49, its kept copy `/var/lib/l1-bot/tz51-l1-account.py`, and B-REVOKE (TZ-51 §4.11), which stays TZ-51's, word for word, with that copy. **Where this file and TZ-51 differ, this file holds.** A step TZ-51 has and this file neither keeps nor names is not run.

### 0.1 The instrument, staged — replaces TZ-51 §0.1

TZ-51's Appendix A, extracted from TZ-51's file as the primary checkout carries it after contract §1's pull, with its SHA-256 asserted, then changed by the edits below, each asserted to occur the number of times it names, the result asserted at its SHA-256 — this script, verbatim, its argument the destination, its output into `logs/01-stage.log`:

```
/root/tz04a-env/venv/bin/python -B - /root/tz52-work/stage <<'EOF2'
import hashlib, os, sys
SRC = "/root/btc-5m-twap/CryptoTZ/TZ-51-l1-account-round-trip-rerun.md"
BASE = "73fd0f6160eb1627a15589a081437f54ee5d826b987586c0f218541c7083dca0"
WANT = "a425e67cce7178e425b04f899ad245cf31a38848bd2553dfacdbbbcdf3a73366"
DEST = sys.argv[1]
lines = open(SRC, encoding="utf-8").read().split("\n")
i = lines.index("```python file=research/tz51-l1-account.py")
j = lines.index("```", i + 1)
t = "\n".join(lines[i + 1:j]) + "\n"
assert hashlib.sha256(t.encode("utf-8")).hexdigest() == BASE, "not TZ-51's Appendix A"
EDITS = [
    # -- the names: this TZ's number, file, branch, work tree, agent and records
    ("TZ-51-l1-account-round-trip-rerun", "TZ-52-l1-round-trip", 3),
    ("tz-51-l1-account-round-trip-rerun", "tz-52-l1-round-trip", 1),
    ("tz51", "tz52", 21),
    ("TZ-51", "TZ-52", 8),
    ("ТЗ-51", "ТЗ-52", 3),
    ('MAP_REVISION = "2026-11-20-b"', 'MAP_REVISION = "2026-11-21-a"', 1),
    # -- what this file is
    ('"""TZ-52 - L1\'s account, its session key and one order\'s round trip at the minimum size, from the live host in Sofia.\n'
     "The bot's Deposit Wallet is the Boss's; its owner key stays in his MetaMask. This file makes a session key on the live\n"
     "host, which can trade and cannot withdraw, has the Boss authorize it by his own signature through the signing page,\n"
     "docs/l1-sign.html, has him approve the wallet's pUSD to the venue's two exchanges at 1 pUSD each where it is short,\n"
     "and proves one order's round trip with the key through the venue's official client, polymarket-client, installed at\n"
     "pinned versions and hashes into /root/l1-env. It pins the bot's Telegram chat and reports there.\n",
     '"""TZ-52 - L1\'s round trip at the minimum size, from the live host in Sofia, on the account TZ-51 left: its session\n'
     "key authorized by the Boss's signature, the wallet's pUSD allowances to the venue's two exchanges at the maximum.\n"
     "TZ-51 BLOCKED at G-APPROVE: the venue's relayer approves an exchange at MaxUint256 alone, so the allowance stays at\n"
     "the maximum the venue set, and what a stolen session key could spend is the wallet's balance (map section 7 item\n"
     "190). This file proves one order's round trip with the key through the venue's official client, polymarket-client,\n"
     "installed at pinned versions and hashes into /root/l1-env, pins the bot's Telegram chat and reports there. Every\n"
     "refusal of the venue is printed in the venue's own words, its hexadecimal strings masked (map section 7 item 191).\n"
     "Its modes that ask the Boss anything are TZ-51's, kept and tested; TZ-52 runs none of them.\n", 1),
    # -- the allowance: the venue's maximum, the only amount its relayer approves
    ("APPROVE_UNITS = 1000000        # 1 pUSD to each exchange whose allowance is short, never the maximum: what a key can\n"
     "                               # spend through that exchange until another TZ approves more\n",
     "APPROVE_UNITS = 2 ** 256 - 1   # MaxUint256: the venue's relayer approves an exchange at this amount alone (TZ-51);\n"
     "                               # what a stolen session key could spend is then the wallet's balance\n", 1),
    ('    """An allowance G-APPROVE keeps: at least one order\'s cost and at most APPROVE_UNITS. Pure."""',
     '    """An allowance G-APPROVE and G-READY keep: at least one order\'s cost, up to APPROVE_UNITS, the maximum the\n'
     '    venue sets. Pure."""', 1),
    ("between one order's cost and 1 pUSD", "at least one order's cost", 5),
    ("\"its allowance on chain to the CTF exchange between one order's cost \"\n"
     "                                                  \"and 1 pUSD\"]",
     "\"its allowance on chain to the CTF exchange at least one order's cost\"]", 1),
    ("    APPROVE_UNITS - the maximum polymarket.com may have set among it - the owner's signature of one Deposit Wallet\n"
     "    batch of approve(exchange, APPROVE_UNITS) on pUSD for each such exchange, which sets its allowance to 1 pUSD,\n"
     "    never more: what a stolen session key could spend through it (CANON PART IV). Made in MetaMask from the signing\n",
     "    APPROVE_UNITS, the owner's signature of one Deposit Wallet batch of approve(exchange, APPROVE_UNITS) on pUSD for\n"
     "    each such exchange: MaxUint256, the one amount the venue's relayer approves (TZ-51; map section 7 item 190).\n"
     "    Made in MetaMask from the signing\n", 1),
    ('            tty.say("Разрешение %s Polymarket списывать pUSD кошелька бота для исполнения его ордеров — %s %s pUSD. "\n'
     '                    "Владелец: %s" % ("двум биржам" if len(short) == 2 else "бирже", "каждой не больше" if len(short) == 2\n'
     '                                      else "не больше", units(APPROVE_UNITS).rstrip("0").rstrip("."), owner_cs))\n',
     '            tty.say("Разрешение %s Polymarket списывать pUSD кошелька бота для исполнения его ордеров — без "\n'
     '                    "ограничения: другой суммы релеер Polymarket не принимает. Владелец: %s" % (\n'
     '                        "двум биржам" if len(short) == 2 else "бирже", owner_cs))\n', 1),
    # -- every refusal of the venue in its own words (map section 7 item 191)
    ("def json_of(blob):\n",
     "def said(exc):\n"
     "    \"\"\"The venue's own words in a refusal, each hexadecimal string of six digits or more after 0x and each UUID\n"
     "    masked - an address, a hash, a signature, an id or a key - on one line of at most 300 characters. Pure (map\n"
     "    section 7 item 191).\"\"\"\n"
     "    s = re.sub(r\"0x[0-9a-fA-F]{6,}\", \"0x…\", \" \".join(str(exc).split()))\n"
     "    return re.sub(r\"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\", \"<uuid>\", s)[:300]\n"
     "\n\n"
     "def json_of(blob):\n", 1),
    ('            out("KEY read %d: refused, status %s" % (i, exc.status))',
     '            out("KEY read %d: refused, status %s: %s" % (i, exc.status, said(exc)))', 1),
    ('                out("OWNER approve link %d: the relayer refused the batch, status %s" % (link, exc.status))',
     '                out("OWNER approve link %d: the relayer refused the batch, status %s: %s" % (link, exc.status,\n'
     '                                                                                           said(exc)))', 1),
    ('                    result = resp.code if resp.code == "post_only_would_cross" else "refused: %s" % resp.code',
     '                    result = (resp.code if resp.code == "post_only_would_cross" else\n'
     '                              "refused: %s: %s" % (resp.code, said(resp.message)))', 1),
    ('                result = "post_only_would_cross" if "crosses book" in str(exc) else "refused: status %s" % exc.status',
     '                result = ("post_only_would_cross" if "crosses book" in str(exc) else\n'
     '                          "refused: status %s: %s" % (exc.status, said(exc)))', 1),
    ('            rt["read_after"] = {"status": "not served, status %s" % exc.status, "matched": None}',
     '            rt["read_after"] = {"status": "not served, status %s: %s" % (exc.status, said(exc)), "matched": None}', 1),
    # -- the relayer's stand-in refuses what the venue refuses: an approval to an exchange below MaxUint256
    ('            spenders = ["0x" + c["data"][34:74] for c in dw["calls"]]\n',
     '            spenders = ["0x" + c["data"][34:74] for c in dw["calls"]]\n'
     '            if any(int(c["data"][74:138], 16) != 2 ** 256 - 1 for c in dw["calls"]):\n'
     '                return 400, {"error": "call blocked: call[0] blocked: approve to exchange %s must be MaxUint256"\n'
     '                             % k.to_checksum_address(spenders[0])}\n', 1),
    # -- the self-tests: the maximum kept, a short exchange set to it
    ('    ok(got[2] == {"c": APPROVE_UNITS, "v": APPROVE_UNITS} and st["batches"] == [[ctf_x, v2_x]] and len(link) == 1 and\n'
     '       "&x=cv&" in link[0] and st["nonce"] == 9 and withheld(printed) and\n'
     '       sum(1 for x in tty.said if "без ограничения" in x) == 1,\n'
     '       "approve, the CTF exchange at the maximum and the V2 exchange short: one link of x=cv, each set to 1 pUSD")\n',
     '    ok(got[2] == {"c": APPROVE_UNITS, "v": APPROVE_UNITS} and st["batches"] == [[v2_x]] and len(link) == 1 and\n'
     '       "&x=v&" in link[0] and st["nonce"] == 9 and withheld(printed) and\n'
     '       sum(1 for x in tty.said if "без ограничения" in x) == 1,\n'
     '       "approve, the CTF exchange at the maximum kept and the V2 exchange short: one link of x=v, set to the maximum")\n', 1),
    ('       "approve, the V2 exchange short alone: an empty answer gives a second link, one call of 1 pUSD, the CTF "\n'
     '       "exchange\'s 1 pUSD kept")\n',
     '       "approve, the V2 exchange short alone: an empty answer gives a second link, one call at the maximum, the CTF "\n'
     '       "exchange\'s maximum kept")\n', 1),
    ('       "approve, both at 1 pUSD: kept, nothing asked, nothing sent")',
     '       "approve, both at the maximum: kept, nothing asked, nothing sent")', 1),
    ('    ok(bounded(RT_COST_UNITS) and bounded(APPROVE_UNITS) and not bounded(RT_COST_UNITS - 1) and\n'
     '       not bounded(APPROVE_UNITS + 1) and not bounded(2 ** 256 - 1) and not bounded(None),\n'
     '       "an allowance in bounds: from one order\'s cost to 1 pUSD, the maximum out")\n',
     '    ok(bounded(RT_COST_UNITS) and bounded(2 ** 256 - 1) and not bounded(RT_COST_UNITS - 1) and not bounded(0) and\n'
     '       not bounded(2 ** 256) and not bounded(None),\n'
     '       "an allowance kept: at least one order\'s cost, the maximum the venue sets in, nothing above it")\n'
     '    ok(said(Exception("call blocked: call[0] blocked: approve to exchange 0x" + "Ab" * 20 + " must be  MaxUint256"))\n'
     '       == "call blocked: call[0] blocked: approve to exchange 0x… must be MaxUint256" and\n'
     '       said("key 019a2b3c-4d5e-6f70-8192-a3b4c5d6e7f8 order 0x" + "cd" * 32) == "key <uuid> order 0x…" and\n'
     '       len(said("x" * 999)) == 300, "a refusal in the venue\'s words: addresses, ids and keys masked, one line")\n', 1),
]
for old, new, n in EDITS:
    assert t.count(old) == n, (old[:60], t.count(old), n)
    t = t.replace(old, new)
data = t.encode("utf-8")
assert hashlib.sha256(data).hexdigest() == WANT, "the patched instrument"
path = os.path.join(DEST, "research/tz52-l1-account.py")
os.makedirs(os.path.dirname(path), exist_ok=True)
if os.path.exists(path):
    with open(path, "rb") as fh:
        assert fh.read() == data, path + " exists with other bytes"
    print(path, data.count(b"\n"), len(data), WANT, "equal, kept")
else:
    with open(path, "xb") as fh:
        fh.write(data)
    print(path, data.count(b"\n"), len(data), WANT, "created")
EOF2
```

| file | lines | bytes | SHA-256 |
|---|---|---|---|
| base: TZ-51's Appendix A, `research/tz51-l1-account.py` | 3,306 | 187,351 | `73fd0f6160eb1627a15589a081437f54ee5d826b987586c0f218541c7083dca0` |
| `research/tz52-l1-account.py` | 3,326 | 188,720 | `a425e67cce7178e425b04f899ad245cf31a38848bd2553dfacdbbbcdf3a73366` |

A failed assert or another hash is BLOCKED; here the line reads `created`. The staged instrument is the one every mode of this run runs, on both hosts; TZ-51 §3.1 writes the branch's file with the same script, its argument the worktree. **There is no Appendix and no B-OWNER script.**

### 0.2 to 0.6 — TZ-51's, under R, with these differences

- **§0.2:** `FINGERPRINT PASS: revision 2026-11-21-a; anchors 6 of 6, 4 re-derived; rows 67: frozen 64 of 64 equal, tracked 2, reported 1; the signing page on main equal to TZ-50's Appendix B`.
- **§0.4:** the floors are TZ-51's, unchanged — `MEM_FLOOR` `86,426,834` and `MEM_FLOOR_SDK` `274,917,678`, `CAPTURE_FLOOR` `7,795,535,636`, `LIVE_FLOOR` `2,447,483,648` — the Architect's runs of this instrument, two of each, peaking at `35,610,624` to `36,016,128` for `selftest` and `112,173,056` to `112,754,688` for `sdk-selftest`, under TZ-51's bases, `36,040,704` and `114,642,944`.
- **§0.5:** `NUMBER PASS - 2 of 2`; the refs against map §1's read of 2026-11-21, 199 lines, each kind that differs named and none BLOCKING; the branch `tz-52-l1-round-trip` absent.
- **§0.6, the condition LS replaced:** at `host before`, root's keys the Executor's alone, and the `PATH` lines exactly these, as TZ-51's report §2.3 quotes `79-host-after.log`, the last line under R:

```
PATH /etc/l1-bot: dir mode 0700 uid 0 bytes 4096
PATH /etc/l1-bot/session-key: file mode 0600 uid 0 bytes 67
PATH /etc/l1-bot/relayer-key: file mode 0600 uid 0 bytes 105
PATH /etc/l1-bot/telegram-token: file mode 0600 uid 0 bytes 47
PATH /etc/l1-bot/chat-id: absent
PATH /var/lib/l1-bot: dir mode 0700 uid 0 bytes 4096
PATH /var/lib/l1-bot/account.json: file mode 0600 uid 0 bytes 310
PATH /root/l1-env: dir mode 0755 uid 0 bytes 4096
PATH /root/tz52-work/wheels: absent
```

  Anything else is BLOCKED before any mode but `host` runs there: the account is not the one TZ-51 left.

---

## 1. What TZ-51 left, and what this TZ decides

### 1.0 The state

TZ-51 BLOCKED at §3.7, G-APPROVE (its report §1). **Before it:** the owner's Relayer API key and the bot's Telegram token written; **the session key authorized for the bot's wallet by the owner's signature, G-AUTH PASS at 18:35:20 UTC on 2026-11-20**; every gate before them PASS. **At it:** the relayer refused each of four owner-signed batches of `approve(exchange, 1,000,000)` with `400`, `call blocked: call[0] blocked: approve to exchange 0x… must be MaxUint256` — read by a probe outside that TZ (its report §2.2 and §3 item 1). **Both allowances already stand at the maximum** polymarket.com set when it enabled trading. No order was placed; G-READY, G-TG and G-RT were not read; `chat-id` is absent. Pull request #48 was closed unmerged by the repository's owner; #49, TZ-51's, is open.

### 1.1 The allowances — decided: the venue's maximum, kept

**The venue's relayer approves an exchange at MaxUint256 alone** (map §7 item 190): the bound of `1` pUSD an exchange cannot be set through the venue's route, whoever signs. This run signs nothing and approves nothing: **both allowances stay at the maximum, and G-READY's checks (4) and (5) read each allowance at least one order's cost**, `50,000` units. **What a stolen session key could spend is then the wallet's balance**, which G-READY prints: the Boss keeps on the bot's wallet what he entrusts to L1, and L1's unit TZ fixes its loss limit and revises CANON PART IV, whose bound binds an allowance the owner signs. The instrument's `approve`, never run here, asks for MaxUint256 where an allowance is short. **Rejected:** an approval below the maximum sent from the owner's account outside the relayer — it needs gas, and a route the venue does not document.

### 1.2 The venue's refusals, in its own words — and what the run does on one

Every refusal the instrument meets prints the venue's own words, each hexadecimal string after `0x` and each UUID masked, one line of at most 300 characters (`said`; map §7 item 191). **This run rests on one venue behaviour no TZ has measured: an order of the session key for the bot's wallet. Where the CLOB refuses it for any reason but `post_only_would_cross`, the round trip stops, its record holds the venue's words, G-RT reads FAIL and the run goes to TZ-51 §3.10 and §9 — BLOCKED, with no other request to the venue and no other attempt** (`mode_roundtrip` refuses a second run after a record with a placement). The words decide the next TZ.

### 1.3 What runs

**On the capture host:** `fingerprint`, `number`, `refs`, `room`, `methods`, `scratch`, `reclaim`. **On the live host:** `host`, `geoblock`, `sshd`, `selftest`, `env`, `sdk-selftest`, `key`, `ready`, `tg-probe`, `find-chat`, `roundtrip`, `tg-report`. **Not run:** `page`, `wheels`, `secrets`, `bosskey`, `authorize`, `approve`, `revoke` — the Boss's modes among them, which the self-tests still run at a real terminal (map §7 item 189).

### 1.4 The instrument's changes, all of them §0.1's edits

The names under R and `MAP_REVISION`; the module's docstring; `APPROVE_UNITS`, MaxUint256; `bounded`'s docstring and every label "between one order's cost and 1 pUSD", which reads "at least one order's cost" — G-READY's checks (4) and (5), G-APPROVE's line, `approve`'s; `approve_flow`'s docstring and its terminal's text; `said`, new, before `json_of`; the venue's words added to the four refusal prints — the key's reads, `approve`'s links, a placement refused by status or by code, and a read-back not served; **the relayer's stand-in refuses an approval to an exchange of any amount but MaxUint256 with the venue's words**; and the self-tests' expectations — `approve` with the CTF exchange at the maximum and the V2 exchange short sets the V2 exchange alone, at the maximum; the bound's literal check; a check of `said`. **Measured by the Architect on these bytes:** `SELFTEST PASS: 141 checks, 141 passed; refused by the hook: 5`; `SDK SELFTEST PASS: 32 checks, 32 passed; refused by the hook: 2`; `G-ENV installed PASS` against the Architect's build of `/root/l1-env` by TZ-50's command; and **with `APPROVE_UNITS` put back to `1000000` on a copy, `sdk-selftest` FAILS** at "authorize and approve at a real terminal", its log carrying `the relayer refused the batch, status 400: call blocked: call[0] blocked: approve to exchange 0x… must be MaxUint256`.

---

## 2. Scope

TZ-51's §2 under R, with these differences, and nothing else allowed:

1. **The repository.** The branch `tz-52-l1-round-trip` carries one file, `research/tz52-l1-account.py`, new. Pull request #49 closed unmerged by `gh api`, its branch kept; **GitHub Pages is not read or touched.** The staging script reads TZ-51's file on `main`.
2. **The live host, written, and kept — L1's:** `/etc/l1-bot/chat-id` by `find-chat`, exclusive create; `/var/lib/l1-bot/tz52-roundtrip-N.json`, `N` at most `3`, by `roundtrip`; `/var/lib/l1-bot/tz52-l1-account.py` by TZ-51 §3.10's `install`. **Nothing of L1's is removed or rewritten by this run** — no B-ENV, no B-RESET, no `secrets`, no `bosskey`. *Written and removed by §9:* `/root/tz52-work/**`.
3. **Money and keys.** This run moves money only by the one order, whose loss is at most `0.10` pUSD, and signs nothing but its two placements at most, through the session key. No withdrawal, transfer, deposit, approval, authorization or revocation is made by any code of this run.
4. **No tmux server** is started or touched by this run.

---

## 3. The work, in this order

Every step is TZ-51's under R unless it says otherwise; its logs keep TZ-51's names under R.

1. TZ-51 §0.0, the readiness and the work tree.
2. **§0.1 here**, into `logs/01-stage.log`.
3. TZ-51 §0.2 to §0.6, with §0.2 to §0.6 here: `fingerprint`, the host gate and `room`, the floors, `number` and `refs`, the live host's access, `host before` with LS, G-GEO, G-SSH and `methods`.
4. TZ-51 §3.1: the worktree's file written by **§0.1's script with the worktree as its argument** — `created`, at §0.1's SHA-256 — one path, `--numstat` `3326 0`; **pull request #49 in place of #48:** read first, `open`, `merged` `false`, head `bfbb1041529f60045172dd95167d8096f6153fba`, then closed by `gh api -X PATCH repos/seahomebatumi-ai/btc-5m-twap/pulls/49 -f state=closed`, read `closed`; found already closed, recorded and nothing closed; found merged, BLOCKED; where `gh` may not close it, TZ-51's B-PR48, for #49. The pull request of this TZ's branch is created.
5. TZ-51 §3.2: `SELFTEST PASS: 141 checks, 141 passed`, `refused by the hook: 5`, on both hosts.
6. TZ-51 §3.3, the scratch directories.
7. TZ-51 §3.4, **without its wheels and B-ENV:** `env`, `G-ENV installed PASS`, and `sdk-selftest`, `SDK SELFTEST PASS: 32 checks, 32 passed`, `refused by the hook: 2`.
8. **TZ-51 §3.5 is not run.**
9. TZ-51 §3.6: `G-KEY` reads the key present and kept.
10. **TZ-51 §3.7 is not run:** no B-ACCOUNT, no B-OWNER, no B-RESET, no tmux.
11. TZ-51 §3.8, **without its first paragraph**, which read B-OWNER's log: `ready` — **G-READY 7 of 7**, its checks (4) and (5) "at least one order's cost", read again as TZ-51 says on a FAIL — then `tg-probe`, then `find-chat` in the background; **where `find-chat` ends with no chat**, the Executor tells the Boss once, in one line in Russian — «Отправьте /start вашему боту в Telegram» — and runs it once more.
12. TZ-51 §3.9, the round trip, **with §1.2 here:** a placement refused for any reason but crossing the book is recorded in the venue's words and BLOCKS; nothing else is sent to the venue.
13. TZ-51 §3.10, **without its tmux step**; its `install` keeps `/var/lib/l1-bot/tz52-l1-account.py` beside TZ-51's copy.
14. TZ-51 §9, then the report, §8.

---

## 4. Gates

TZ-51's §4 under R, with these differences:

- **Not read by this run:** G-PAGE, G-AUTH and G-APPROVE, and G-ENV's wheels half.
- **G-READY** — its seven checks, (4) and (5) reading `its allowance on chain to the CTF exchange at least one order's cost` and `its allowance on chain to the V2 exchange at least one order's cost`. PASS: 7 of 7.
- **G-RT** — TZ-51 §4.8's nine checks, unchanged; a refusal's line carries the venue's words.
- **The stops — TZ-51 §4.11, with its reason corrected:** this TZ deploys no unit and starts no process that outlives it; the round trip's last act is `cancel_all` of the key, whatever happened. After it, in the Boss's hands: **withdraw** on polymarket.com, which needs no host, and **B-REVOKE**, TZ-51 §4.11's line word for word, with TZ-51's kept copy. **It is not run by this TZ, and no FAIL of it calls for it** — but its reason is no longer TZ-51's: the allowances are the maximum, so what the key could spend through orders is the wallet's balance (§1.1).

---

## 5. The instrument

`research/tz52-l1-account.py`, 3,326 lines, 188,720 bytes, `a425e67cce7178e425b04f899ad245cf31a38848bd2553dfacdbbbcdf3a73366`: TZ-51's Appendix A changed by §0.1's edits alone (§1.4). Every line number TZ-51 cites is TZ-51's Appendix A's; this TZ cites none of the new file's.

## 6. Cost

TZ-51's §6 for the modes §1.3 runs; `sdk-selftest` under 20 s; §0.1's script under 1 s. No check reaches `3,600` s of compute. **Waits:** G-READY 120 minutes at most; `find-chat` `1,800` s twice at most; the archive 30 minutes.

## 7. Validation

- **V1** — `FINGERPRINT PASS` at §0.2 and TZ-51 §3.1, as §0.2 here. Asserted.
- **V2** — `NUMBER PASS - 2 of 2`; refs by kind; the branch absent before the push. Asserted.
- **V3** — §0.1's script: `created` at `a425e67cce7178e425b04f899ad245cf31a38848bd2553dfacdbbbcdf3a73366` into the stage, then into the worktree; the live host's copy the same SHA-256. Asserted.
- **V4** — the branch: one path, `--numstat` `3326 0`; pull request #49 read and closed unmerged, or found closed. Asserted.
- **V5** — the capture host gate, seven checks; the room and its margin printed. Asserted.
- **V6** — the access, as TZ-51's V6. Asserted.
- **V7** — the live host gate, five checks, at `host before` and `host after`; **LS as §0.6 here** at `host before`. Asserted.
- **V8** — `G-GEO PASS` at §0.6 and TZ-51 §3.9. Asserted.
- **V9** — `G-SSH` K1 to K6 at §0.6 and TZ-51 §3.10. Asserted at §0.6.
- **V10** — `SELFTEST PASS: 141 checks, 141 passed`, `refused by the hook: 5`, on both hosts; `SDK SELFTEST PASS: 32 checks, 32 passed`, `refused by the hook: 2`. Asserted.
- **V11** — the scratch directories, and `RECLAIM PASS` where any was reclaimed. Asserted where it runs.
- **V12** — `G-ENV installed PASS`, its files line. Asserted.
- **V13** — `G-KEY`: present and kept. Asserted.
- **V14** — `G-READY PASS: 7 of 7`, every read with its instant, the balance and both allowances as printed. Asserted.
- **V15** — G-TG: `getMe` PASS, the chat pinned, the report's message sent with its text. Recorded.
- **V16** — `G-RT PASS: 9 of 9`, every placement's line, the read-backs, the cancellation, the balances before and after, and the record whole; a refusal in the venue's words. Asserted.
- **V17** — G-PRINT: `0` and `0`. Asserted.
- **V18** — TZ-51 §3.10 without its tmux step: the kept copy at §0.1's SHA-256; `scp exit=0` and `diff exit=0`; the capture host's units as at §0.3; contract §4.2's self-check. Asserted.
- **V19** — every mode's printed peak — the standard library's each under `43,213,417`, the client's each under `137,458,839`. Recorded.
- **V20** — TZ-51 §9 under R. Asserted.

## 8. The report

`CryptoReports/TZ-52-l1-round-trip-report.md`, as TZ-51 §8 and contract §8. **Its §2 quotes the round trip's record whole** (CANON hard rule 16) and every refusal's line. **A departure from this file is named in its own item** — and no request to a venue outside the modes of §1.3 is one this TZ allows.

## 9. Reclaim

TZ-51 §9 under R.

---

## 10. Pre-send checks

Performed by the Architect on 2026-11-21 against this file, start to end, in a reading separate from its writing. Every committed file was read at `origin/main` `b941123`; the instrument at §0.1's SHA-256, `a425e67cce7178e425b04f899ad245cf31a38848bd2553dfacdbbbcdf3a73366`, produced by §0.1's script from TZ-51's file; the venue's client at `polymarket_client-0.20.0-py3-none-any.whl`, TZ-51's set's SHA-256.

| # | check | result |
|---|---|---|
| **C1** | scope against body | **Named by the body, each inside §2 or TZ-51's §2 under R.** *Repository, written:* `research/tz52-l1-account.py` on the branch, the report on `main`, pull request #49 closed unmerged and this TZ's own opened — §2 item 1, TZ-51 §2 item 1. *Repository, read:* TZ-51's file by §0.1's script — §2 item 1; `SYSTEM-MAP.md`, its 67 rows' files and `docs/l1-sign.html` by `fingerprint`; `CryptoTZ/` and `CryptoReports/` by `number`; `origin`'s refs by `refs` and TZ-51 §3.1's `ls-remote`; pull request #49 by `gh api`. *Capture host, written:* `/root/tz52-work/**`, the forensic store's copies by `reclaim`, earlier session directories by B-RECLAIM-SCRATCH — TZ-51 §2 items 2 and 7; no tmux server — §2 item 4. *Live host, written:* `/root/tz52-work/**`, removed by §9; `chat-id`, `tz52-roundtrip-N.json` and `tz52-l1-account.py`, kept — §2 item 2; nothing of L1's removed or rewritten. *Live host, read:* TZ-51 §2 item 3 under R. *Network:* the header's authorization and TZ-51 §2 item 4 less the wheels, the page and every relayer submission. **By content class:** no price, size, side, book hash, rate, competitiveness or outcome of a market is printed — the order's own state and the wallet's own balance and allowances are this run's; a refusal's words pass through `said`, which masks every hexadecimal string after `0x` and every UUID; G-PRINT reads every log. **No intersection:** TZ-51's B-RESET exemption does not arise, B-RESET not being run. |
| **C2** | origin of every expectation | **Every fixed literal of §0, §1, §3, §4 and §7, of two kinds and no third.** *Quoted from a committed artifact, named:* revision `2026-11-21-a`, the anchors and rows `67` = `64` + `2` + `1` (map §0, its table unchanged from `2026-11-20-b`'s, which TZ-51's `fingerprint` read PASS twice); the nine `PATH` lines (TZ-51's report §2.3, `79-host-after.log`, quoted line for line, the last under R); PR #49's head `bfbb1041529f60045172dd95167d8096f6153fba` (`git ls-remote` on 2026-11-21: `refs/pull/49/head` and the branch, and `refs/pull/49/merge` present, the pull request open); the base's lines, bytes and SHA-256 (TZ-51 §0.1's table); the floors and their bases (TZ-51 §0.4); `199` refs (map §1); `0.10` pUSD and the nine checks of G-RT (TZ-51 §2 item 6 and §4.8). *Computed by an implementation independent of the one under test:* the result's lines, bytes and SHA-256 by `wc` and `sha256sum` of the script's output; MaxUint256 = 2²⁵⁶ − 1; `50,000` = 5 · 0.01 · 10⁶. *Counted on the Architect's runs of the self-tests on these bytes, which run on literals, stand-ins and pseudo-terminals of their own:* `141` and `5` — TZ-51's `140` and the check of `said` — and `32` and `2` — TZ-51's `32`, three of its checks of `approve` rewritten and none added. *Measured by the kernel:* the peaks of §0.2 to §0.6 here. **No expectation depends on a quantity this TZ measures.** |
| **C3** | shape of every diff | **One file, new:** `research/tz52-l1-account.py` is absent from `origin/main` (`git cat-file -e` exit `128`): `3326` lines added and `0` removed. `SYSTEM-MAP.md` is replaced by its revision in the Boss's upload, with this file, absent from `origin/main` too (exit `128`). The report is new. |
| **C4** | cost of every check | TZ-51's §10 C4 for the modes §1.3 runs, at the same bounds — the instrument's modes are TZ-51's code but for §0.1's edits, none of which touches a loop; measured on these bytes: `selftest` under 1 s, `sdk-selftest` `18.9` s and under 20 s, `env` `1.2` s; §0.1's script under 1 s over TZ-51's `322,047`-byte file. **Waits, not compute:** G-READY 120 minutes, `find-chat` `1,800` s twice, the archive 30 minutes. **No check reaches `3,600` s of compute.** Fail-fast bounds: TZ-51's, unchanged, each derived there. |
| **C5** | every count | V1: `67 = 64 + 2 + 1` over map §0's table of `2026-11-21-a` by an independent parse. V2: `2 of 2`. V3: one file, written twice — the stage and the worktree. V4: one path; `3326` the script's output's line count. V5: `7`, TZ-51's. V7: `5` over `live_gate`'s keys; LS's `9` lines over `host`'s list — `(L1_ETC,) + SECRETS + (L1_VAR, ACCOUNT_FILE) + tuple(rt_paths()) + (L1_ENV, WHEELS)`, four files of `SECRETS` and no record — and `1` key. V9: `6`. V10: `141` and `32`, the `ok` calls the two self-tests executed at each of the Architect's runs on these bytes, two of each; `5` and `2` their live refusals. V14: `7` over `ready_flow`'s keys. V16: `9` over `rt_reading`'s keys. §0.1: `24` edits, each with its count asserted. |
| **C6** | every population | Each gate's population is TZ-51 §4's. The peaks: the Architect's runs of this instrument under Python 3.12.3, two of each self-test. `env`'s and the self-tests' counts: the Architect's runs against his build of `/root/l1-env` by TZ-50's command. The mutation's FAIL: one run of `sdk-selftest` on a copy with `APPROVE_UNITS` `1000000`. |
| **C7** | every signature and every behaviour | **Committed, read at `b941123`:** TZ-51's Appendix A, `73fd0f61…`, extracted by the fence `` ```python file=research/tz51-l1-account.py `` and the next line that is a fence alone, as TZ-51's own §0.1 extracts it. **This TZ calls no committed function; every behaviour it attributes was read in the patched file:** `mode_roundtrip` — `assert not prior.get("placements"), "BLOCKED: %s placed an order already; a round trip runs once" % p` — so a placement refused once is not tried again; the placement's refusal now `"refused: %s: %s" % (resp.code, said(resp.message))` and `"refused: status %s: %s" % (exc.status, said(exc))`, and `roundtrip_flow`'s `if result != "post_only_would_cross": break`; `bounded` — `return enough(v) and v <= APPROVE_UNITS`, `APPROVE_UNITS = 2 ** 256 - 1`; `ready_flow`'s checks (4) and (5), `bounded(allow["c"])` and `bounded(allow["v"])` under their new labels; `mode_host`'s `PATH` list as C5 quotes it. **The venue's client:** `RejectedOrder` carries `message: str`, from the venue's `errorMsg` (`models/clob/order_response.py`); a `RequestRejectedError`'s text carries the venue's words — `said` printed them through the client from the relayer's stand-in in the mutation's log. |
| **C8** | every cross-reference | **Map, revision `2026-11-21-a` — the sections, rows and items this run rests on, which the header copies from here (map §7 item 174):** §0, the fingerprint gate, its table and the signing page; §1, the repository, its TZs and pull requests #48 and #49; §2.6, the reward book — its store's bounds and its reserve; §3, the units, the trees on the host and the session directories; §5, L1's row and the reward book's days; §6, its rows host identity, for TZ host gates; live host; live host identity, for TZ host gates; live host — the venue's geoblock, measured 2026-11-19, TZ-48 and TZ-49, and 2026-11-20, TZ-50; live host — the venue's CLOB from Sofia; language; git remote; egress; venue edge — the `User-Agent`; venue constants; maker incentives; RTDS session limit; disk; disk floors and caps; process supervision; memory; clock; sandbox limit — destructive actions; and harness — background output; §7 items 86, 89, 91, 95, 98, 119, 124, 127, 132, 137, 138, 140, 143, 144, 150, 156, 163, 169, 174, 175, 176, 177, 180, 181, 183, 184, 185, 186, 187, 188, 189, 190 and 191; §8. Each read in full, an item's disposition column included, each §6 row found by its first cell. **The duties items leave to the Architect "before" a step** (CANON PART VI, the fifth rule): item 190 — the allowance decided, §1.1; item 191 — the refusal's fallback named before the run, §1.2; item 189 — the Boss's modes still run at a real terminal by the self-tests, §1.3; items 132, 175, 184 to 186 — as TZ-51 §10 C8 discharged them, unchanged. **TZ-51's file**, every section this TZ names — §0.0 to §0.6, §1.5, §2 items 1 to 7, §3.1 to §3.10, §4, §4.1, §4.7, §4.8, §4.10, §4.11, §6, §8 and §9 — resolved to its heading; its B-PR48 in §3.1. **TZ-51's report**, §1, §2.2, §2.3 and §3 item 1. **The Executor contract**, `A4` `6ac6e10aeabc`: §1, §4.2, §5, §8 and §10. **CANON** PART III, hard rules 2, 4, 5, 10, 13 to 17; PART IV, keys. **This file's own sections**, each `§` resolved to its heading. **The Boss's words:** none quoted. |

**Not performable in the session that wrote this TZ, and converted into conditions the run evaluates** (CANON hard rule 13): **(1)** that the live host stands as TZ-51 left it — the Architect cannot read that host: LS BLOCKS otherwise (§0.6); **(2)** that the venue takes an order of the session key for the bot's wallet — G-RT reads it, and §1.2 fixes what the run does on a refusal; **(3)** that the Boss's `/start` is in the bot's last 24 hours of updates — `find-chat`, and §3 step 11's one line; **(4)** that `gh` may close pull request #49 — TZ-51's B-PR48, for #49.

