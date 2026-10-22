# TZ-31 — W0, who earns: do the makers who earned most keep earning on markets whose fills no one has read?

**Canonical filename:** `TZ-31-who-earns.md`. The committed file takes this name and no other.

**Executor model: Opus.** Reads of the venue over the network, a gate's arithmetic, and the first label read of a set no
one has scored.

**Required System Map revision:** `2026-10-22-a`.

**Required anchors**, from map §0. A mismatch on any one is BLOCKED before any work:

| anchor | required |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `0f6c90451cbd` |
| `A6` — pricer | `729f0bcdbee3` |

**Host gate:** §0.3. This TZ runs on the capture host for its interpreter, its network and the forensic store, and reads
nothing of any capture.

**When:** §3.6 and everything after it **no earlier than 2026-10-23 12:15:00 UTC**, epoch `1792757700`: §3.6's first
command waits for that instant in its own text, and `fetch` asserts it. If every candidate qualifies, the set's last
member opens at 11:10 UTC on 2026-10-23, and TZ-23's walk stops before any market younger than `3,900` s (§1).
Everything before §3.6 may run earlier. At most about `7,600` s of wall clock from §3.6 on at §6's bounds, most of it
the fetch held to the pair book's idle stretch; under one hour at the venue's pace of 2026-10-22 on the Architect's
stand-in.

**What this TZ is.** The W track's first step, W0 (CANON PART II). M0 summed every maker's side of every taker fill as
one pool and read NO EARN over both looks (TZ-29); a pool cannot say how its result divides between makers. The
Architect named two groups of ten wallets on M0's last 864 markets, every one already read — the makers with the largest
`S / sqrt(V)` and the takers with the largest `S` — and fixed them in Appendix A. This TZ sums each group's own fills
over each market's life, every fill before `T0 + 300`, on **the first 1,008 qualifying markets after `1792451400`**,
M0's last member — markets whose fills no one has read — and reads W0 on the makers once, by TZ-23's own thresholds and
table: **W-EARN**, **W-NO-EARN** or **UNDECIDABLE**, each answer's false-reading probability at most `0.005`. The
takers' sum is printed beside it and barred from every reading. Every walk, request for fills, position, rebate,
threshold and reading is TZ-23's own function, loaded byte for byte; this TZ's instrument, `research/tz31-who-earns.py`
(Appendix A), adds the makers' rows of a market — its full feed less its takers' rows — each wallet's own position from
its own rows, the two groups' sums, and TZ-29's fetch held to the pair book's idle stretch.

---

## 0. Gates

### 0.0 The work tree, first

After contract §1 steps 1 and 2, and before anything else:

```
mkdir /root/tz31-work /root/tz31-work/logs; echo "exit=$?"
```

`exit=0` proves neither existed; anything else is BLOCKED. **From here every command's output goes to
`/root/tz31-work/logs/`, one file per step, §0's included**, and nothing to the session's scratchpad. The one exception
is B-RECLAIM-OWN, §9.

### 0.1 The instrument, staged

Extract Appendix A from this TZ as the primary checkout carries it after contract §1's pull, with this script, verbatim,
its one argument the destination:

```
/root/tz04a-env/venv/bin/python -B - /root/tz31-work/stage <<'EOF'
import hashlib, os, sys
SRC = "/root/btc-5m-twap/CryptoTZ/TZ-31-who-earns.md"
DEST = sys.argv[1]
WANT = {
    "research/tz31-who-earns.py": "7073188c8fbaa19568e8c6e4d6379e40ea57cf2a1341ebde0ea6a08f2c544765",
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
| `research/tz31-who-earns.py` | 1,523 | 84,775 | `7073188c8fbaa19568e8c6e4d6379e40ea57cf2a1341ebde0ea6a08f2c544765` |

Then the instrument's one dependency beside it, TZ-23's file as `main` carries it:

```
install -m 0644 /root/btc-5m-twap/research/tz23-maker-m0.py /root/tz31-work/stage/research/; echo "exit=$?"
sha256sum /root/tz31-work/stage/research/tz23-maker-m0.py
```

which must print `6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f` — map §0's row; the instrument
asserts it again each time it loads the file (Appendix A lines 59 to 70). A failed assert or another hash is BLOCKED.
The staged copy runs §0.2's `fingerprint` alone, written **`I0`**:
`nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz31-work/stage/research/tz31-who-earns.py`, run from
`/root/tz31-work` — every mode asserts that its current directory is the work tree (line 1503).

### 0.2 Fingerprint

`I0 fingerprint` performs contract §1 steps 3 and 4 inside the instrument and asserts them, against `SYSTEM-MAP.md` and
the files of its §0 table in the primary checkout `/root/btc-5m-twap`: revision `2026-10-22-a`; the six anchors; `A2`,
`A4`, `A5` and `A6` re-derived as the first 12 hex characters of those files' SHA-256; the table's **42** rows, each
printed in lines, bytes and SHA-256 — **39** `frozen` rows asserted equal to the map, **2** `tracked` and **1**
`reported`; and the map's own lines, bytes and SHA-256 (lines 768 to 799). It prints `FINGERPRINT PASS` or stops at the
first mismatch, which is BLOCKED.

### 0.3 Host gate

From `/root/btc-5m-twap`, with `S` first set to the scratchpad directory the session's system prompt names, output
verbatim into `logs/03-host-gate.log`:

```
date -u; date -u +%s
nproc; grep -E '^(MemTotal|MemAvailable|SwapTotal|SwapFree):' /proc/meminfo
uptime -s; journalctl --list-boots --no-pager
df -B1 --output=source,size,avail /var/lib/btc-recorder
find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
grep -c e3975b5da44c5328adf3bf3914634cd878842c73 /var/lib/btc-recorder/runtime.jsonl
/root/tz04a-env/venv/bin/python -c 'import sys; print(sys.version.split()[0])'
stat -c '%s %n' /root/btc-forensics/tz27-work--archive--set.json; sha256sum /root/btc-forensics/tz27-work--archive--set.json
TZ=UTC systemctl show btc-recorder.service btc-pairbook.service btc-pairbook-archive.service btc-pairbook-archive.timer btc-chainbook.service -p Id -p MainPID -p NRestarts -p ActiveState -p SubState -p UnitFileState -p ActiveEnterTimestamp -p Result
TZ=UTC systemctl list-timers btc-pairbook-archive.timer --all --no-pager
journalctl -u btc-pairbook-archive.timer -o short-iso --since 2026-10-14 --no-pager
journalctl _PID=1 -o short-iso --since 2026-10-14 --no-pager | grep -E 'Reload|btc-pairbook-archive' | tail -n 80
grep -E '^(Start-Date|Commandline|Upgrade|End-Date)' /var/log/apt/history.log | tail -n 40
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
systemctl is-active telemetry-watch.service; echo "exit=$?"
git -C /root/btc-recorder-svc rev-parse HEAD
cat /root/btc-pairbook-svc/commit.txt /root/btc-pairbook-archive-svc/commit.txt
for d in /root/tz30-work /root/tz18a-svc /root/btc-recorder-svc /root/btc-pairbook-svc /root/btc-pairbook-archive-svc /var/lib/btc-pairbook-archive; do test -e "$d"; echo "$d exit=$?"; done
find /root/btc-forensics -type f | wc -l
git worktree list
du -sb /var/lib/btc-pairbook /var/lib/btc-pairbook-archive /root/.claude /root/PROJECT_GAMING_PS5
echo "$S"; ls -la "$(dirname "$(dirname "$S")")"
```

- **H1** — `find` prints exactly one path.
- **H2** — `df` names source `/dev/vda2` and size `31612203008`; `grep -c` prints at least `1`. With H1 this is map §6's
  host identity.
- **H3** — the interpreter prints `3.12.`.
- **H4** — the forensic store this TZ writes into is the host's: `stat` and `sha256sum` print `16570` bytes and
  `ec71b1a7ce7db37ff29a49156006541dd5729c1df2c829c481eb64181228e4dd` — TZ-27's `set.json`, copied there by TZ-27's §9
  and asserted by TZ-30's host gate (TZ-30 report §0.3).
- **Memory gate** — `MemAvailable` at least `172,064,768` bytes (§0.4).
- **Disk gate** — `avail` at least `5,250,000,000` bytes (§0.4).

Any of these six failing is BLOCKED. **The rest is printed and carries no threshold:** the boots, the timer's journal,
systemd's own reload records and the package manager's history, beside which §3.4 reads the archive's runs off its
calendar — six with no boot, five by its ledger and one by its tag, to 2026-10-22 06:24:08 UTC (map §2.5, §7 item 115);
the five units — this TZ needs none of them, G-STILL reads the recorder and the pair book (§4.4), and §1's hold reads
the archive's service; `telemetry-watch.service`'s two states, on which map §6's headroom is conditional; the three code
trees' commits, `e3975b5…`, `e8b46a8…` and `d8194fd…` by map §3; `/root/tz30-work` absent and the code and state trees
present, by map §3; the forensic store's count, map §3's `1,938`; the worktrees, map §3's two; `du` of the pair book's
store beside `df`, as map §2.5 asks, and of the archive's state; and the listing of the directory that holds the
session's own, whose UUID directories `I scratch` names live or earlier (§9).

### 0.4 Resource floors, in exact bytes

**Disk.** `/dev/vda2` free at least **`5,250,000,000`** bytes: the pair book's `STREAM_FLOOR`, `4,500,000,000`
(`research/tz26-nesting-b3-capture.py` line 132), below which no stream opens for a window, plus `750,000,000` for this
session — so nothing this TZ writes can stop the pair book's capture. The session's peak is its tree and §9's copies of
it in the forensic store together, `372,007,447` bytes at the bound: the set's tree, `204,383,308` bytes in the
Architect's run of 2026-10-22 over a stand-in of 1,008 markets — `187,169,879` of it the chunk cache — scaled from that
stand-in's `4,217,005` full rows over its 1,008 markets to the bound's `6,218` a market (§6), so `303,775,370`; the
rehearsal's tree, `30,369,874`; the worktree's `7,658,893`, the stage's `139,660` and `1,000,000` allowed for the logs;
and §9's copies, `29,063,650` — the set's tree but its chunk cache, `17,213,429` bytes scaled the same way to
`25,584,358`, the rehearsal's but its cache, `2,339,632`, the stage and the logs. The allowance is that peak twice over,
`744,014,894`, rounded up (map §6, disk).

**Memory.** `MemAvailable` at least **`172,064,768`** bytes: twice the largest peak of any mode in the Architect's runs
of Appendix A under Python 3.12.3 at the population's size (map §7 item 97's rule) — `fetch`'s `86,032,384` over the
stand-in's 1,008 markets, two chunks of three markets in flight, the busiest holding `27,884` rows of both feeds;
`rehearse` peaked at `69,636,096`, `constants` at `62,832,640`, `score` at `42,106,880` and `selftest` at `31,539,200`
(map §6, memory). The fetch's peak grows with the chunks in flight, not with the set: at five markets a chunk it reached
`118,718,464` over the formation's 864, which is why a chunk is three. Every mode that reads the venue or a set —
`rehearse`, `fetch`, `constants` and `score` — re-reads `MemAvailable` at its start and stops BLOCKED below the floor,
and asserts that glibc took TZ-23's mmap threshold and arena count (lines 252 to 257). Map §6 records the host:
`1,002,127,360` bytes in all, one processor; TZ-30 read `235,171,840` to `311,447,552` bytes available with its session
open. Every mode runs under `nice -n 19`.

### 0.5 Refs

`git ls-remote origin` before §3.1's push, every ref reported. Map §1 records, read on 2026-10-22 at 10:07 UTC, `main`
at `d973ff12e1692b80c128154a233cdc355c638616`, PR #29's merge, eight branches, twenty tags — `tz-01a-dataset` and
`tz-27-pairbook-streams`, annotated, and eighteen lightweight `pairbook-streams-*` — and **60** ref lines; every later
run of the archive adds one tag — 61 after 2026-10-23 03:00:20 UTC, and one more for each run off the calendar. The
upload that carries revision `2026-10-22-a` and this TZ sits above `d973ff1`, in one commit or more; every commit on
`main`'s first-parent line above it is reported with the paths it changed. A difference is recorded, not BLOCKING,
unless `main` does not carry revision `2026-10-22-a` or `refs/heads/tz-31-who-earns` already exists — either is BLOCKED.

---

## 1. Why this TZ exists

Line numbers here are Appendix A's unless a file is named; `tz23` is `research/tz23-maker-m0.py` at `d973ff1`.

**The question** — CANON PART II, the W track's W0: do the makers who earned most on markets already read keep earning,
at settlement and with the 20% rebate, on markets whose fills no one has read? **M0 could not answer it** (map §4, §5):
TZ-23 and TZ-29 summed the makers' side of every taker fill inside `[T0, T0 + 240)` as one pool — `0.231` c a share over
8,064 markets, `0.219` c of it rebate — and a pool averages every maker together, those who move a stale quote inside
the 150 ms taker delay and those whose stale quotes are taken alike. B3 found the stale side of the book gone before a
taker's order could match: on 768 windows of the pair book's streams the violations it saw were on the book and gone, on
one leg at least, by the time its orders matched, and buying them lost in every block (TZ-30; map §4).

**The fills, by maker.** Data API v2's `/v2/trades` with `taker_only=false` serves every fill's maker rows beside its
taker's row, each with its own wallet, side, outcome, size and price, and with `taker_only=true` the taker's alone (map
§6, public fills). **A market's maker rows are its full feed less its takers' rows, as multisets of whole rows** (lines
337 to 346), and `split_feeds` asserts that every takers' row is in the full feed. These are the rows the venue's rebate
payouts were measured against — four wallet-days, `0.19975` to `0.20003` of the fee over a wallet's maker rows so formed
(map §4). In a transaction the makers' sizes sum to the taker's but where the venue prints a maker's size at two
decimals and the taker's at six — 71 of 1,151,005 transactions on the formation's 864 markets — and `constants` counts
them and `score` prints the count over the set (lines 349 to 358).

**A wallet's own position.** TZ-23's `aggregate` turns a taker's row into the makers' side of it by `maker_terms` (tz23
lines 316 to 323 and 342 to 360). A wallet's own row with its side flipped is a taker's row whose makers' side is the
wallet's own (lines 459 to 462): BUY Up `+s` at `p`, SELL Up `−s` at `p`, BUY Down `−s` at `1 − p`, SELL Down `+s` at
`1 − p`, in Up shares. So `X`, `C` and `R` of a wallet's rows in a market are TZ-23's, `R` the rebate
`0.014 · s · p · (1 − p)` at the row's own price (tz23 lines 326 to 328); a maker's money at settlement is
`X · up − C + R`, and a taker's `X · up − C − R / 0.2`, the fee `0.07 · s · p · (1 − p)` taken off (lines 478 to 481).
**The self-test proves both against row-by-row arithmetic written apart from TZ-23's** — `s (won − p)` for a buy and
`s (p − won)` for a sell — at either outcome, and over a synthetic set built, scored and summed end to end (lines 1103
to 1113; lines 1116 to 1496).

**A market's life is every fill before `T0 + 300`**: TZ-23's bands `pre` — before `T0` — `w0` to `w3`, and `last`,
`[T0 + 240, T0 + 300)` (lines 465 to 471); `post`, from `T0 + 300`, is after the reading the market settles on and is
printed beside the bands, barred. M0's window was `[T0, T0 + 240)`; W0's quantity is a maker's whole book in a market as
it carries it to settlement. **A named maker's own taker fills, if it has any, are not in its sums:** W0 reads resting
quotes, filled and held — what W1 would place.

**The groups, named by the Architect before this TZ, on the formation** — M0's last 864 markets, `1792192500` …
`1792451400`, 2026-10-16 23:15 to 2026-10-19 23:10 UTC, 435 of them Up, every one read by TZ-29 — through an independent
client and an independent implementation in exact arithmetic:

- **The makers, gated:** among the 128 wallets with a maker fill in at least 648 of the 864 markets — three in four —
  the ten with the largest `S / sqrt(V)`, `S` the wallet's money at settlement with the rebate over its maker fills
  before `T0 + 300` and `V` the sum over markets of its `X²`: the ten with the most signal for their noise. Together, on
  the formation, `211,127` fills: `S` = `13,822.225` USDC on `2,085,206.453` shares, `0.663` c a share — `9,067.234` at
  settlement and `4,754.991` of rebate — and `V` = `18,528,280.704`.
- **The takers, barred:** among the 159 wallets with a taker fill in at least 432 — one in two — the ten with the
  largest `S` after the fee: `60,454` fills, `S` = `16,080.836` USDC on `2,567,699.904` shares — `46,493.310` at
  settlement less `30,412.475` of fee — and `V` = `366,723,215.043`. Named to show who pays the makers; their reading's
  power is `0.023` (below), so no reading of theirs is read.

Both groups and their wallets are Appendix A's `GROUPS` (line 122 onward). The formation is in-sample for both: the
groups were picked on it, and its figures are what selection makes of edge and noise together. **What carries over is
the test, not the figure.** The 864 are excluded from the set by `T0`.

**The set.** The first **1,008** qualifying markets with **`T0 > 1792451400`**, walked by TZ-23's `candidates` from
**`1792451700`**, 2026-10-19 23:15 UTC, in steps of 300 (lines 317 to 332; tz23 lines 449 to 472), past TZ-23's three
excluded spans, all of which end below it. A candidate qualifies by TZ-23's `qualify`, unchanged (tz23 lines 375 to
395): served closed, `outcomes` `["Up", "Down"]`, `outcomePrices` one of the two resolved forms, `feeSchedule`
`{exponent 1, rate 0.07, takerOnly true, rebateRate 0.2}` and `feeType` `crypto_fees_v2`, `eventStartTime` its own `T0`,
a condition id of 64 hex digits and two token ids. **If every candidate qualifies**, the set runs from `1792451700` to
`1792753800`, 2026-10-23 11:10 UTC — 9 members on Monday, 288 on each of Tuesday, Wednesday and Thursday, 135 on Friday,
none on a weekend — in 51 document requests, and its member list's SHA-256 is
`e3d77b0a36847b1ef628f79ec78ed6b7d597bdc39a16d6ecf87786e91ed3f658`, recorded and asserted by nothing. The walk requests
no document after the 1,008th member, and stops BLOCKED before it requests a market younger than `3,900` s or, before a
request, once it has considered 3,024 candidates — the 1,008 and TZ-23's slack of 2,016 (tz23 lines 455 and 461); **a
walk stopped because a market is too recent is walked again 300 s later, at most 24 times** (lines 317 to 332), and
every other stop is final. 1,008 markets are three and a half days: the power below, and a set whose last member is
resolved by 2026-10-23 12:15 UTC.

**The test**, TZ-23's (its §1, "The test"), on each group's own sum. Order the members by `T0` and let `G_m` be
everything public before `T0_m + 300`. A group's `X_m`, `C_m` and `R_m`, over its fills before `T0_m + 300`, are known
at `G_m`, and `up_m`, fixed by the reading at `T0_m + 300`, is known at `G_(m+1)`; so `D_m = X_m (up_m − q_m)`, `q_m`
the probability of Up given `G_m`, are martingale differences, each in an interval of length `|X_m|`, and
`exp(λ M_n − λ² V_n / 8)` is a supermartingale whose probability of ever reaching `1/α` is at most `α` (Ville). With
`S = Σ (X_m up_m − C_m + R_m)` — for the takers, the fee `R_m / 0.2` taken off in place of the rebate — and `Sh` the
group's shares: **W-EARN** rejects that the group's expected money given what was public is at most nothing, and
**W-NO-EARN** that it is at least half a tick a share — **`thr = L/λ + λ V / 8`**, `L = ln(1/α)`; **W-EARN** at
`S >= thr`; **W-NO-EARN** at `S <= δ · Sh − thr`; **UNDECIDABLE** otherwise; W-EARN first where both hold (tz23 lines
410 to 433). `α = 0.005` for each answer and `δ = 0.005`, half a tick a share, are TZ-23's. **The bound assumes no
independence between outcomes, no calibration and no distribution**, and holds at any look: a later TZ may extend the
same sum over the next qualifying markets at the same constants, as TZ-29 extended TZ-23's.

**`λ`, fixed before any member is read:** `sqrt(8 L / V)` at the formation's per-member `V` over 2,016 members — twice
the set, so that a second look at the same constants keeps its power — `0.00099017` for the makers and `0.00022256` for
the takers (lines 123 and 129).

**Power**, before any label and deciding nothing: TZ-23's normal approximation at the largest variance the outcomes
allow, `V/4`, `Φ((δ · Sh − thr) / (sqrt(V) / 2))` (tz23 lines 420 to 422). **At the formation's per-member `V` and `Sh`,
both scaled to 1,008 members** — `21,616,327.488` and `2,432,740.862` for the makers — `thr` is `8,026.397` USDC,
`0.330` c a share: W-EARN asks at least `0.330` c a share and W-NO-EARN at most `0.170` c, and **the power is `0.962`**
— of W-EARN against half a tick a share, and of W-NO-EARN against nothing. `2 thr / Sh` is `0.660` c, above `δ`, so
UNDECIDABLE can occur, most often where the true edge lies between the two bounds, about `0.17` and `0.33` c a share.
**The projection rests on two quantities, the set's `V` and `Sh` per member**, and the set is all weekday where the
formation held a weekend: `constants` prints both, `thr` and the power at them before any label is read (lines 577 to
598). The takers' power at their projection is `0.023`, and they are barred. Every figure in this paragraph is the
Architect's computation at 80 digits, independent of the instrument; the self-test asserts the instrument's `thr` within
`1e-20` of it and its power between `0.9624` and `0.9625` at the same `V` and `Sh` (line 1286 onward). On the stand-in's
1,008 markets below — the formation and the 144 before it — the makers' own `V` and `Sh` gave the instrument's `thr`
`0.341` c a share and power `0.947`: the projection moves with the two quantities it rests on.

**The venue, re-read by the Architect on 2026-10-22** (map §7 item 87's rule; CANON §1.1). The changelog's newest
entries are of 2026-10-21 and add equity prices; nothing since TZ-29's re-read of 2026-10-19 touches the fee, the maker
rebate, the taker delay, Gamma `/markets` or `/v2/trades`, and its entry of 2026-10-07 changes `/v2/trades` only for
requests that carry `user`, which no request here does. The maker-rebate page gives 20% for Crypto, fee-curve weighted —
`C × 0.07 × p × (1 − p)` a filled maker order, totals per market — paid daily in pUSD, a 1 pUSD minimum. `/v1` trades
retire on 2026-10-24; TZ-23 reads `/v2` alone. A fee change on the venue would make the set's documents fail `qualify`
and stop the walk BLOCKED at its slack.

**The path, proved on the venue the same day.** The Architect ran Appendix A's `rehearse` against the venue on
2026-10-22 under Python 3.12.3, every request held to the idle stretch: the walk over the formation's last 144 markets,
both feeds of their fills, both groups' sums, the gate and the labels — **its 18 figures equal to the Architect's
independent figures to every digit** (§4.1). **Then the whole path at the set's size:** `fetch`, `constants` twice and
`score` twice on a stand-in set of 1,008 markets, `1792149300` … `1792451400`, every one read by TZ-29 — `START` moved
and the instant to none, every other rule the instrument's — whose last 864 members, the formation, came back member by
member equal to the independent implementation's sums for both groups, 864 of 864 and 864 of 864, and in total equal to
the figures above to every digit; the stand-in's reading is in-sample and no datum. §0.4 and §6 are those runs'
measurements.

**Every request inside the pair book's idle stretch, and none near or during the archive's run** — TZ-29's rule and code
(lines 289 to 301 and lines 304 to 314): every walk and every chunk of fills starts only at seconds 15 to 470 of a
900-second window — a request budgeted at `120` s ends by second 590 — never from 02:57:20 to 03:01:20 UTC, and never
while `btc-pairbook-archive.service` reads `active`, `activating`, `deactivating`, `reloading` or `refreshing`; a hold
longer than `7,200` s is BLOCKED. A chunk is three markets and both of their feeds — TZ-23's `trades` twice,
`taker_only` `false` and `true`, every row asserted on its market and its token (lines 361 to 377; tz23 lines 269 to
299) — its start and end written to a timing file, and every chunk that ended after second 590 listed. The fail-fast
projects the chunks' own fetching time, the holds excluded, after the first 30 fresh chunks, BLOCKED above `7,200` s,
and cancels every chunk not yet started (lines 391 to 434).

**What this TZ decides.**

1. **The instrument**, `research/tz31-who-earns.py`, on the branch `tz-31-who-earns`; `main` carries it once the Boss
   merges after the verdict.
2. **The set, formed and fetched; both groups' constants, label-free, on disk with the constants file's SHA-256 in
   `state.json`; the instrument's commit on `origin`** — and only then the labels, read once a run.
3. **W0's reading, the makers.** W-EARN opens W1, our quoting simulated on the pair book's streams (CANON PART II).
   W-NO-EARN closes the maker side on these terms: the makers who earned most keep under half a tick a share on markets
   whose fills no one has read. UNDECIDABLE leaves W0 open, and a later TZ may extend the same sum at the same
   constants. Where both bounds hold the reading is W-EARN, and half a tick a share is rejected too.
4. **The archive's record**, read from its own ledger and printed (§3.4).
5. **Nothing on the host is touched** but this TZ's tree, the forensic store by exclusive create, and the directories
   earlier sessions left (§9).

**Data hygiene.** **No fill of any market of the set has been read by anyone.** M0's sets end at `1792451400`; the pair
book's streams and stored books after window `1792403100`, whose five-minute legs include the set's, are unread (map
§2.5); and of the set's documents only TZ-30's set rule has read any — the settled documents of the five-minute legs of
B3's 936 candidate windows, to `1792548600`, 108 of this set's candidates among them, outcomes included, for the
nesting's identities and nothing else (TZ-30 report §1). Nothing of this TZ was chosen on them: the groups, `λ`, `α`,
`δ` and the set rule were fixed on the formation and on TZ-23 alone. The Architect's reads for this TZ stop at
`1792451400`: the formation's 864 markets' documents and both feeds of their fills, the rehearsal's 144 among them,
through its own client and through the instrument; one request of `1792451400`'s maker rows, to read their fields; the
venue's changelog and rebate page. The set's member list above comes from a dry run of TZ-23's walk that sent no
request. §2 bars any read of a member outside the instrument.

---

## 2. Scope

**Repository paths this TZ may write, and no others:**

1. `research/tz31-who-earns.py` — new, byte for byte Appendix A's, on branch `tz-31-who-earns`, then a pull request. Not
   merged by the Executor.
2. `CryptoReports/TZ-31-who-earns-report.md` — straight to `main`, in one commit. **The one path pushed to `main`, and
   the exemption to item 7 below.**

**Host paths this TZ may write:** `/root/tz31-work/**`; `/root/btc-forensics/`, by exclusive create only (§9); and in
the primary checkout `/root/btc-5m-twap`, its `.git` for the branch and the worktree, and its `CryptoReports/` for the
report. **Host paths it removes, under §9 and nothing else:** `/root/tz31-work/` with its worktree, and the directories
`I scratch` names earlier.

**Prohibited, each absolutely:**

1. No committed file is modified; every `frozen` row of map §0 is byte-identical at run end.
2. **Nothing under `/var/lib/btc-recorder/` or `/var/lib/btc-chainbook/` is opened, listed or written** — TZ-23's audit
   hook refuses every open there and this instrument's every open and listing (lines 202 to 222); only §0.3's `df`,
   `find` and `grep -c`, at both of its runs, and B-RECLAIM-OWN's `df` touch the recorder's root.
3. **Nothing under `/var/lib/btc-pairbook/` is opened, listed or written** — the hook refuses both; only `du -sb` at
   §0.3, at both of its runs, reads the store's size. **No price, size, side, book hash or outcome is extracted from a
   body stored there or from any Release asset made from it** (map §2.5).
4. **Under `/var/lib/btc-pairbook-archive/` nothing is written; `ledger.jsonl` is opened for reading by `I archive` and
   `I still` alone — the named exemption — and nothing else there is opened or listed** but by `du -sb` at §0.3. The
   ledger's records carry events, counts, times, ids, tags and hashes and no price: TZ-28's run asserts each against
   TZ-27's forbidden keys before writing it (`research/tz28-pairbook-archive-timer.py` lines 212 to 220).
5. **No unit is signalled, started, stopped, enabled, disabled or changed.** `systemctl show`, `is-active`,
   `is-enabled`, `list-timers` and `journalctl` are this TZ's only reads of a unit and of systemd.
6. `/root/tz04a-env/`, `/root/tz01-env/`, `/root/tz18a-svc/`, `/root/btc-recorder-svc/`, `/root/btc-pairbook-svc/` and
   `/root/btc-pairbook-archive-svc/` are not modified; `/root/btc-forensics/` only by §9's exclusive create, and the one
   file of it §0.3 reads is read and never written.
7. Nothing is pushed to `main` except the report of item 2.
8. **No label of the set is read before §3.7's constants are on disk with their SHA-256 in `state.json` and the
   instrument's commit is on `origin`.** A label is the outcome a member's `outcomePrices` states. Three exemptions,
   each named because the body requires it: (a) `qualify`, which asks only whether `outcomePrices` is one of the two
   resolved forms, and `fetch` and `constants`, which carry each member's document in `set.json`, `outcomePrices` with
   it, and never interpret it — the self-test asserts every constants file byte-identical with every label flipped; (b)
   `rehearse`, which reads the labels of the formation's last 144 markets, every one read by TZ-29; (c) `score`, which
   reads the set's labels once a run, its determinism run included, each run a line in the ledger.
9. **Requests:** `gamma-api.polymarket.com/markets` and `data-api.polymarket.com/v2/trades`, through TZ-23's `http_json`
   and its two headers, `User-Agent: btc-5m-twap-m0/TZ-23` and `Accept: application/json` (tz23 lines 81, 82 and 233 to
   253), each walk and chunk held by §1's rule; `git` against `origin`, `I archive`'s `git ls-remote` among them; and
   `gh` for the pull request and for git's credential alone. No other request — no CLOB, no websocket, no GitHub API, no
   authenticated call — and **no read of any member's document or fills by any command but the instrument's modes**,
   `set.json` and the cache included.
10. **No single fill's, member's or market's price, size or outcome, and no wallet's figure in one market, is printed or
    written outside `/root/tz31-work/`**: the instrument prints sums over a set — a group's, a wallet's, a band's — and
    the report quotes them. **This binds the Executor's own reads as strictly as the instrument** (map §7 item 118): no
    file under `/root/tz31-work/rehearsal/` or `/root/tz31-work/set/` is printed, whole or in part, by any command but
    the instrument's modes and `sha256sum`, `stat`, `wc -l` and `du`, which print hashes, sizes and counts; the timing
    files carry chunks' first `T0` and seconds and may be printed, and so may `state.json`, the label ledger and every
    file under `logs/`. The one exemption is §9's byte-for-byte copies into `/root/btc-forensics/` of the files the
    report names by hash.
11. No Release is created, and no dataset, archive or binary enters git history.

---

## 3. The work, in this order

From §3.1 on, `nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz31-work/wt/research/tz31-who-earns.py` is written
**`I`**; a mode is `I <mode>`, run from `/root/tz31-work`. Every command's output goes to `logs/`, one file per step,
and is quoted in the report. **§9's B-RECLAIM-SCRATCH runs after §3.3 and before §3.4; B-RECLAIM-OWN runs last, after
§3.10.** On a BLOCK before §3.1, B-RECLAIM-OWN runs with `I0` in place of `I` and without its `git worktree remove`
line; on a BLOCK or a FAIL after it, the run goes to §3.10 and §9, skipping every step that needs a PASS it lacks.

**Where the session's permission classifier refuses a command of a block named B-…**, the Executor prints the block, the
Boss runs it verbatim in a root shell on the VPS, and the Executor verifies it through the reads this TZ names — never
from the Boss's account.

### 3.1 The branch and its file

```
git -C /root/btc-5m-twap fetch origin
git -C /root/btc-5m-twap worktree add -b tz-31-who-earns /root/tz31-work/wt origin/main
```

Then §0.1's script again, verbatim but for its argument, `/root/tz31-work/wt`; it must print the same lines, bytes and
SHA-256 as at §0.1. `sha256sum /root/tz31-work/wt/research/tz23-maker-m0.py` must print `6b3ace2c…`: `main` carries
TZ-23's file. `I fingerprint` must print `FINGERPRINT PASS` again, from the worktree. Commit the one file alone on the
branch, then push it and set its upstream **through `gh`'s stored login, as TZ-29 and TZ-30 did** (map §7 item 114):

```
git -C /root/tz31-work/wt -c credential.helper= -c 'credential.helper=!gh auth git-credential' push https://github.com/seahomebatumi-ai/btc-5m-twap.git tz-31-who-earns:refs/heads/tz-31-who-earns; echo "exit=$?"
git -C /root/tz31-work/wt fetch origin +refs/heads/tz-31-who-earns:refs/remotes/origin/tz-31-who-earns; echo "exit=$?"
git -C /root/tz31-work/wt branch --set-upstream-to=origin/tz-31-who-earns; echo "exit=$?"
date -u +%FT%T.%NZ; git -C /root/tz31-work/wt ls-remote origin refs/heads/tz-31-who-earns
git -C /root/tz31-work/wt rev-parse HEAD
```

— the instant the commit is on `origin`, and its hash there, which must be the worktree's `HEAD` — and open the pull
request against `main` with `gh pr create`. A failed assert or a non-zero exit here is BLOCKED. **The push is what lets
§3.8 read a label:** `score` refuses a `HEAD` that `origin` does not carry (lines 998 to 1018). The token in `origin`'s
URL is not touched.

### 3.2 The self-test

`I selftest` must print `58 of 58 checks passed`. It reaches no network and runs on literals and on temporary trees
under `/root/tz31-work/selftest-tmp/`, which it removes (lines 1116 to 1496). A red self-test stops the run here, and it
goes to §3.10 and §9.

### 3.3 The units, and the directories beside this session

`I still` records the recorder's and the pair book's `MainPID`, `NRestarts` and `ActiveState` in `state.json`, with the
instant, and prints their `MemoryCurrent` and `MemoryPeak` and the archive's two units' states. Then
`I scratch "$(dirname "$S")"` lists every UUID directory beside this session's own and names each **live** — born from 1
s before to 60 s after the start of a running process whose `argv[0]` is `claude` or ends in `/claude.exe` — or
**earlier**.

### 3.4 The archive's record

`I archive`: the archive's two units by `systemctl show`; `ledger.jsonl` read whole, its size and SHA-256, every
complete record printed with its UTC stamp; every run summarized — its start on the calendar or off it, its events, its
set, Release, removal, restart, resume and terminal record; the tags `origin` carries beside the ledger's sets; and
whether the archive is halted (lines 712 to 763 and lines 897 to 917). **Printed facts, no threshold:** its exit is
recorded and gates nothing. The report sets each run off the calendar beside §0.3's boots, the timer's journal,
systemd's reload records and the package history (map §7 item 115).

### 3.5 G-REHEARSAL

`I rehearse`: the whole path — the walk, the fetch held to the idle stretch, both groups' constants and the score — over
the formation's last 144 markets, against the Architect's independent figures (§4.1). A FAIL stops the run here, and it
goes to §3.10 and §9.

### 3.6 The instant, then the set — G-SET

First, in its own text, the instant:

```
t=$(date -u +%s); while [ "$t" -lt 1792757700 ]; do sleep 30; t=$(date -u +%s); done; echo "instant reached: $t $(date -u)"
```

Run it in the background where the instant is more than five minutes away, and go on only once it prints. Then
`I fetch`, in the background, its output to `logs/`, read until it prints `G-SET PASS` or fails (§4.2). Its walk starts
inside the idle stretch; its chunks are held; after its first 30 fresh chunks it projects its own fetching time and
stops BLOCKED above `7,200` s. **A network failure is resumable:** the cache keeps every finished chunk, and `I fetch`
may be run again twice, 600 s apart; a third failure is BLOCKED.

### 3.7 The constants, twice

`I constants`, then `I constants` again. The second run must print `unchanged` for **eight** files —
`tz31-makers-fills.jsonl.gz`, `tz31-makers-members.csv`, `tz31-makers-wallets.csv`, `tz31-takers-fills.jsonl.gz`,
`tz31-takers-members.csv`, `tz31-takers-wallets.csv`, `tz31-pool.csv` and `tz31-constants.json` — contract §6's
determinism. The constants file's SHA-256 is in `state.json`.

### 3.8 The score, twice

`I score`, then `I score` again. The first reads the labels and prints the reading; the second must print `unchanged`
for `tz31-makers-scored.csv`, `tz31-takers-scored.csv` and `tz31-reading.json`. The ledger then holds two lines.

### 3.9 The units again — G-STILL

`I still` (§4.4).

### 3.10 The closing reads

§0.3's block again, `I archive` again, then:

```
TZ=UTC systemctl show btc-recorder.service btc-pairbook.service btc-pairbook-archive.service -p MainPID -p NRestarts -p ActiveState -p MemoryCurrent -p MemoryPeak
free -b
du -sb /root/tz31-work /root/.claude
cat /root/tz31-work/state.json /root/tz31-work/label-ledger.jsonl
```

---

## 4. The gates — fixed here, before any of their data exists

| gate | population | PASS | false failure | power, against |
|---|---|---|---|---|
| **G-REHEARSAL** | the formation's last 144 markets, `1792408500` … `1792451400` | §4.1's 18 figures equal, exactly | `0` — one public record read again, equal to the Architect's independent read of it on 2026-10-22 | `1`, any change in the record, the fetch, the feeds' split, a sign, a band, the rebate, the fee or a sum |
| **G-SET** | the walk from `1792451700` and the fetch of its members | 1,008 members, every chunk read back | `0` | — |
| **W0** | the makers' fills before `T0 + 300` over the set's 1,008 members | §4.3 | at most `0.005` for each answer | TZ-23's normal approximation, printed before any label; `0.962` projected at the formation's per-member `V` and `Sh` |
| **G-STILL** | the recorder and the pair book, §3.3 to §3.9 | unchanged, or the pair book moved by the archive's own restarts alone | `0` — systemd and the archive's ledger read directly | `1`, a restart or a stop that is not the archive's |

### 4.1 G-REHEARSAL

Over the 144 markets: the members and the Up outcomes, and for each group its fills `n`, shares, `X`, `C`, `R`, `V`,
settlement `Σ (X · up − C)` and `S`, equal the Architect's figures in Appendix A's `REF` (line 143 onward), as values —
18 figures (lines 930 to 937). The Architect's figures come from its own client's fetch of both feeds and its own
position arithmetic at 60 digits, which shares no code with this instrument or TZ-23's. `rehearse` prints
`G-REHEARSAL PASS: 18 of 18`. **A FAIL means the venue's record of markets TZ-29 already read has changed since the
Architect read it, or that the instrument sums otherwise**, and the reading would not be what §1 describes.

### 4.2 G-SET

`fetch` prints `G-SET PASS` when the walk from `1792451700` has formed 1,008 members, all above `1792451400`; every
chunk's two feeds have ended with no cursor; every row has belonged to its chunk's markets and carried its market's
token for its outcome (TZ-23's `trades`, tz23 lines 269 to 299); every takers' row has been found in its market's full
feed (lines 337 to 346); and every chunk reads back to its members in order (lines 380 to 388). Every non-member is
listed with its reason by `constants`.

### 4.3 W0's reading, the makers

| condition, on the makers' `S`, `V` and `Sh` over the set | reading |
|---|---|
| `S >= thr` | **W-EARN** — whatever the power |
| `S <= δ · Sh − thr` | **W-NO-EARN** — whatever the power |
| otherwise | **UNDECIDABLE** |

TZ-23 §4.3's table, applied by TZ-23's `reading` to this TZ's thresholds (tz23 lines 426 to 433; lines 616 to 707).
Where both hold the reading is W-EARN, and the report states that half a tick is also rejected. **No row reads a
power.** The report prints `S`, its settlement and rebate parts, each per share, both margins, and, barred from every
reading, each named maker's `S`, shares and `S` a share; the makers' result in each band; the takers' `S`, its
settlement and fee parts and their per-wallet and per-band figures; and the pools of every maker and every taker of the
set.

**What a reading establishes, and what it does not.** W-EARN says that on these 1,008 markets the named makers' fills
before each market's reading were priced in their favour, given what was public, beyond what the outcomes' noise
explains — rebate included; it says nothing of a quote of ours — its queue position, its share of the fills, the adverse
selection it would meet and the 150 ms delay are W1's. W-NO-EARN says the makers who earned most on the formation kept
less than half a tick a share on markets whose fills no one had read, rebate included. Neither names a maker that earns
alone: the per-wallet figures are barred, and a group of ten picked on 864 markets is one test, not ten.

### 4.4 G-STILL

From §3.3 to §3.9 the recorder keeps its `MainPID`, `NRestarts` and `ActiveState`, and the pair book keeps them or is
moved by the archive's own restarts alone — its ledger's `restart` records since §3.3's read, a chain from the recorded
`MainPID` to the current one, `NRestarts` one higher at each, the unit `active` (lines 802 to 819). **This TZ signals
nothing**, so a FAIL runs no block, and the report names what changed.

---

## 5. The instrument

`research/tz31-who-earns.py`, Appendix A, fixed by the Architect as this TZ's Validation and written byte for byte.
**The standard library alone**, run under `/root/tz04a-env` — Python 3.12.3, the recorder's interpreter, which nothing
here modifies. It imports nothing from the repository: it **loads** `research/tz23-maker-m0.py` from its own directory,
asserts its SHA-256 `6b3ace2c…` and executes those very bytes (lines 59 to 70), so TZ-23's audit hook, its 60-digit
context and its malloc settings are installed and TZ-23's functions are the ones every step calls: `form_set` and
`candidates` for the walk, `trades` for both feeds, `aggregate` — and through it `maker_terms` and `rebate` — for every
position, cost and rebate, `gate_constants` for the thresholds and the power, `reading` for the table and `label_of` for
the labels. **Its own code** is its audit hook (lines 202 to 222), the idle stretch and the archive's run (lines 289 to
301, lines 304 to 314), the walk's retry (lines 317 to 332), the makers' rows of a market (lines 337 to 346), a chunk of
both feeds (lines 361 to 377), the held fetch (lines 391 to 434), a wallet's own rows (lines 459 to 462), each group's
sums and the pool (lines 495 to 574), the score (lines 616 to 707), G-STILL (lines 802 to 819), the archive's ledger
(lines 712 to 763), the modes and the self-test. One mode a run; each prints its findings with UTC stamps, its peak
memory, whether glibc took its two settings, and its opens refused by either hook. Every number of the venue is parsed
as the `Decimal` of its own text, every sum is done in the main thread at 60 digits, and the fetch's two worker threads
only parse, format and split the feeds as multisets, with no `Decimal` arithmetic (map §7 item 99): the count of
transactions whose sides' sizes differ is `constants`' (lines 349 to 358). Exit `0` is every assert held; exit `1` a
failed assert, named, or a BLOCK whose message says so. Run with `-O` it refuses to start (line 50).

---

## 6. Cost

Measured in the Architect's runs of 2026-10-22 under Python 3.12.3 on two cores of an Intel Xeon — the host has one (map
§6) — of Appendix A's bytes but for `MEM_FLOOR`, which they measured, and taken at the population's upper bound: the
walk at most `3,042` candidates — TZ-23's slack stops it before any request once 3,024 are considered — in at most `51`
document requests and one more for each non-member, `2,067` at that slack, and at most 25 walks; the fetch at all 1,008
members at the busiest rate M0 or the formation has shown — `1,766` taker rows a market, the first look's busiest day
(2026-09-08), and `3.520` full rows a taker row, the formation's largest by chunk of three markets, `10,945` of `3,109`
— so `6,218` full and `1,766` taker rows a market, at most `25` pages a chunk of three markets, and `8,400` pages over
the set's 336 chunks. **The fetch waits on the venue, not the processor, and the venue's latency moves within the
hour:** the Architect's held fetches of 2026-10-22 ran at `0.338` to `0.625` s a page and a worker by chunk, `0.511`
over the stand-in's 1,008 markets; the Architect's run of TZ-23's own fetch on 2026-10-19 ran at `0.832`, the slowest
measured, and TZ-23's on the host, on 2026-10-09, at `0.512`.

| check | population | measured | bound |
|---|---|---|---|
| `fetch`, the walk | at most `51` gamma requests a walk and one more for each non-member, and no market younger than `3,900` s — so at most 289 non-members for a walk started before 2026-10-24 12:15 UTC, one of them while it runs | 51 requests in `15.9` s for the stand-in's 1,008 | `112` s a walk at 340 requests and `0.33` s a request, inside its `120` s budget up to 312 non-members; past them, `682` s at 2,067 requests, where TZ-23's slack stops it BLOCKED; at most 25 walks, each after `300` s |
| `fetch`, fetching | 336 chunks, at most 8,400 pages | `1,284` s projected after the first 30 of 336 chunks; `1,517.7` s of fetching, `5,936` pages at `0.511` s a page and a worker, the longest chunk `14.7` s; processor `163.4` s | `3,494` s of fetching at `0.832` s a page and a worker, two workers; **projected after the first 30 fresh chunks, BLOCKED above `7,200` s** |
| `fetch`, wall | the same chunks, each started at seconds 15 to 470 of a window | `3,240` s for the stand-in's 1,008: its first hold `370` s, its walk `16` s, then `2,846` s from the first chunk's start to the last one's end, every chunk inside the idle stretch, the last ending at second `480` | `6,620` s at the bound, `3,494` × 900 / 475: each worker fetches about 475 s of every 900 |
| `constants`, twice | the set's rows parsed and summed, both groups' files and the pool's written | `25.2` and `25.8` s for `4,217,005` full rows, processor `24.9` and `25.5` s | `38` s a run at the bound's `6,267,744` rows; `115` s on a host three times slower |
| `score`, twice | 1,008 members | `0.1` s a run | `15` s a run |
| `rehearse` | 144 markets, fixed | `611.8` s of wall clock for 48 chunks, about `445` of them held, `169` s of fetching projected; processor `27.1` s | `499` s of fetching at the bound and two holds of at most `444` s: about `1,400` s |
| `selftest`, `fingerprint`, `still`, `scratch`, `archive`, each `reclaim` | — | `selftest` `5.6` s; `fingerprint` 0.14 s on a stand-in checkout; `still`, `scratch`, `archive` and `reclaim` are TZ-29's and TZ-30's, under `2` s each by TZ-30's own stamps | `30` s a run |

**Wall clock at those bounds about 9,200 s** — the fetch's first hold at most `510`, its walk `112` and its chunks
`6,620`; the constants twice `230`, at `115` s a run on a host three times slower, and `score` twice `30`, at its bound;
`rehearse` with its holds `1,400`; the rest under `300` — and `300` more for each retry of the walk. **Of it the
processor's at most about `1,070` s on a host three times slower** — the fetch's `729`, the constants' `227`,
`rehearse`'s `81`, the rest under `35`; every second at `nice 19`. The fetch's fail-fast bound, `7,200` s of fetching,
is its own bound, `3,494` s, at a venue `2.06` times slower than at its slowest measured run; slower still, the fetch
alone would hold the host for about four hours, and it stops BLOCKED. **A hold longer than `7,200` s stops BLOCKED:**
the longest wait the idle stretch makes is `444` s, from second 471 to second 15 of the next window, the calendar guard
adds `66` s, and the archive's longest run, `1792446859`, lasted `2,181` s from its `start` to its `complete` record by
its ledger as TZ-30 printed it — a hold of `7,200` s is that run three times over beside both. **The walk's retries wait
at most `7,200` s**, 24 of `300` s: they carry the walk past up to 24 non-members before its 1,008th member — M0's 8,064
had none — and a walk still too recent after them stops BLOCKED.

---

## 7. Validation

| # | check | count |
|---|---|---|
| **V1** | §0.2's fingerprint, at §0.2 and §3.1 | `FINGERPRINT PASS`: revision `2026-10-22-a`; anchors 6 of 6, 4 re-derived; 42 rows, 39 of 39 `frozen` equal |
| **V2** | §0.3's host gate | H1 to H4, the memory and the disk gate; the rest printed |
| **V3** | §0.1's and §3.1's file | 1 of 1 hash asserted at each, lines and bytes; TZ-23's file `6b3ace2c…` at each; the branch's diff against `origin/main` names exactly one path, `A`, 1,523 lines |
| **V4** | the self-test | `58 of 58` |
| **V5** | the archive's record | the ledger's size, SHA-256 and records, every run's line, the tags; recorded, gating nothing |
| **V6** | G-REHEARSAL | `18 of 18` figures |
| **V7** | G-SET | 1,008 members; the candidates considered; every non-member with its reason; the chunks inside and outside the idle stretch |
| **V8** | the constants, twice | 8 of 8 files `unchanged` at the second run |
| **V9** | the score, twice | the reading; 3 of 3 files `unchanged`; 2 ledger lines; the instant §3.1's `ls-remote` printed the instrument's commit on `origin`, beside the first ledger line's `at`, the first label read of the set (map §7 item 63) |
| **V10** | G-STILL | PASS, or what changed named |
| **V11** | the hooks | `opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0` at every mode |
| **V12** | memory | every mode's printed peak, against §0.4's floor; `malloc tuned: True` at every mode |
| **V13** | contract §4.2's self-check | run after the push and the pull request and before the report's commit |
| **V14** | §3.10's closing reads | every read printed |
| **V15** | §9's `reclaim` runs | files considered, named by a report, kept by name, copied and already held; the store's count after equal to before plus the copies |
| **V16** | §9's removals | `git worktree remove` without `--force` exit `0`; `test -e` exit `1` for `/root/tz31-work` and each directory removed; `git worktree list` naming `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else |

---

## 8. The report

`CryptoReports/TZ-31-who-earns-report.md`, in contract §8's order. **In its first lines:** W0's reading, with the
makers' `S`, its two parts, both bounds and both margins, each per share; G-REHEARSAL and G-SET; the set — candidates
considered, members, first and last, non-members; the instant of the first label read beside the instant the
instrument's commit reached `origin` and the constants' `state.json` record (map §7 item 63's rule); and G-STILL. Beyond
what V1 to V16 print: the set — **every non-member with its reason**, the members by weekday, the member list's SHA-256
and the set file's; each group's fills, shares, `X`, `C`, `R`, `V` and the members and wallets with a fill; the
thresholds, both per share, and the power at the set's own `V` and `Sh`; **the reading**; and, barred, each named
maker's and taker's `S`, shares and `S` a share, each group's bands, the pools of every maker and every taker, and the
feeds' counts of transactions, of those whose sides' sizes differ and of those with one side only; **the timing files'
summary lines and every chunk that ended after second 590**, with the walk's start second, its duration as TZ-23's
`the set formed in` line prints it, whether it ended after second 590, and both timing files by SHA-256; the archive's
record as `I archive` printed it, at both reads, and each run off the calendar beside §0.3's boots, the timer's journal,
systemd's reload records and the package history; both units at both reads, memory included; both ledger lines; every
block the classifier refused, who ran it and when; every free-space and `MemAvailable` read with its instant and bound;
§9's counts and removals; and every file the run wrote, by SHA-256, but the two chunk caches — the set's 336 files and
the rehearsal's 48 — which §9 lets go with the tree. **The report is drafted in the primary checkout `/root/btc-5m-twap`
before B-RECLAIM-OWN and committed after it**, so the removal of this TZ's tree is in it.

---

## 9. Reclaim — the host left clean (CANON hard rule 15)

**What a file is kept for:** a committed report prints its SHA-256, whole or as a prefix of 16 to 64 hex characters, or
it is kept by name: `state.json`, `label-ledger.jsonl` and every file under `logs/`. `reclaim` copies each into
`/root/btc-forensics/` as `<tree>--<path with / as -->`, by exclusive create, and verifies its hash; a name already
there with the same hash is counted as held, and with another hash is a failed assert (lines 1052 to 1098). The branch
worktree is not copied: `reclaim` asserts that `git status --porcelain --ignored` in it prints nothing and that its
`HEAD` is its upstream's, so `git worktree remove` needs no `--force`. The report draft in `CryptoReports/` counts as a
report. The chunk caches are not named — the groups' fills files hold their rows, and the pool file every market's sums
— and go with the tree.

**B-RECLAIM-SCRATCH**, after §3.3 and before §3.4, for every directory `I scratch` named **earlier** — none it named
live, and never this session's own; map §3 names TZ-30's pair, `2f1eadf7…` and `c498ebed…`, unless a reboot of the host
emptied `/tmp` (map §6, process supervision):

```
I reclaim <each earlier directory, by its full path>
rm -rf <one such directory>; echo "exit=$?"
test -e <that directory>; echo "exit=$?"
```

One `I reclaim` names every earlier directory; then one `rm -rf` and one `test -e` a directory. `reclaim` refuses a
directory born from 1 s before to 60 s after a running claude process started, and any path but `/root/tz31-work` that
is not a UUID directory under `/tmp/` whose parent's name carries `btc-5m-twap`; it prints `RECLAIM PASS` before any
removal. If `I scratch` names none earlier, the block is recorded as empty and skipped.

**B-RECLAIM-OWN**, last, after §3.10 and with the report drafted. **Its output is written to no file; the report quotes
it verbatim from the session**, every line of it:

```
I reclaim /root/tz31-work
git -C /root/btc-5m-twap worktree remove /root/tz31-work/wt; echo "exit=$?"
rm -rf /root/tz31-work; echo "exit=$?"
test -e /root/tz31-work; echo "exit=$?"
git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
find /root/btc-forensics -type f | wc -l
df -B1 --output=source,size,avail /var/lib/btc-recorder
```

The branch `tz-31-who-earns` stays on `origin` and as a local ref; only its working tree goes. **Kept:**
`/root/btc-recorder-svc/`, `/root/btc-pairbook-svc/` and `/root/btc-pairbook-archive-svc/` are the running units' code,
`/root/tz18a-svc/` the disabled chain book's; the three capture roots, the archive's state and the forensic store are
data, never scratch. **A refused `rm -rf` is handed to the Boss** by §3's route, one tree per command, and verified by
`test -e`.

---

## 10. Pre-send checks

Performed by the Architect on 2026-10-22 against this file as sent, in a reading separate from its writing, with the
repository at `origin/main` `d973ff12e1692b80c128154a233cdc355c638616` and map revision `2026-10-22-a` as it ships with
this TZ. `tz23` is `research/tz23-maker-m0.py` at that commit, `6b3ace2c…`; any other line number without a file is
Appendix A's, the extracted file's.

| # | check | result |
|---|---|---|
| **C1** | scope against body | **Repository paths the body names or cites — eleven, one class, and the files of the map's table:** `CryptoTZ/TZ-31-who-earns.md`, read by §0.1's script; `SYSTEM-MAP.md` and the files of its table's 42 rows, read by `fingerprint` — `BTC-EXECUTOR-INSTRUCTIONS.md`, `research/twap-divergence.py`, `research/recorder/recorder.py` and `research/pfair.py` among them, the four anchors it re-derives; `BTC-EXECUTOR-INSTRUCTIONS.md`, cited for §1, §4.2, §6 and §8; `research/tz31-who-earns.py`, staged and written on the branch; `research/tz23-maker-m0.py`, installed beside the staged copy and loaded by its bytes in both places, never modified; `research/tz26-nesting-b3-capture.py` and `research/tz28-pairbook-archive-timer.py`, cited for their lines and read by no step; `CryptoTZ/TZ-23-maker-m0.md`, cited for its §1 and §4.3, and `CryptoTZ/TZ-27-pairbook-archive.md`, cited for its §9, both read by no step; `CryptoReports/TZ-30-nesting-b3-measure-report.md`, cited for its §0.3 and §1; every `CryptoReports/*.md`, read by `reclaim` for hashes (lines 1021 to 1027); `CryptoReports/TZ-31-who-earns-report.md`, written to `main`. **Entry points:** Appendix A's ten modes (lines 1499 to 1519); §0.1's script; `install`; `sha256sum`; `git` — `fetch`, `worktree add`, `remove`, `prune` and `list`, `add`, `commit`, `push`, `ls-remote`, `rev-parse`, `branch`, `status`, and contract §4.2's `rev-list`, `diff` and `ls-tree`; `gh pr create` and `gh auth git-credential`; `systemctl show`, `is-active`, `is-enabled` and `list-timers`; `journalctl`; `df`, `du`, `find`, `grep`, `stat`, `ls`, `free`, `cat`, `date`, `uptime`, `nproc`, `mkdir`, `rm -rf` and `test -e`. **Outputs:** under `/root/tz31-work/` — `logs/`, `state.json`, `label-ledger.jsonl`, `stage/research/`'s two files, the worktree `wt/`, `selftest-tmp/` (removed by the self-test), and in `rehearsal/` and `set/` each: `set.json`, the chunk cache, a timing file, both groups' fills, members, wallets and scored files, the pool file, the constants file and the reading file; copies of them in `/root/btc-forensics/` by §9; the report. **By content class:** `set.json`, both trees, carries every member's document with its `outcomePrices` — §2 item 8's exemptions (a) and (b), and the self-test's flip check holds the constants label-free; the scored files carry each member's label and money — item 8 (c), after the constants and the push; the chunk caches carry every fill's price and size, the fills, members, wallets and pool files a member's or a wallet's figure in one market — item 10, inside the work tree, and the forensic copies of the files the report names by hash, item 10's one exemption; the constants and reading files and every log carry sums over a set, non-members' `T0` and status, chunks' first `T0` and seconds, and the archive's ledger records, which carry no price (item 4). **No intersection is left unnamed.** |
| **C2** | origin of every expectation | **§5's literals** are Appendix A's, fixed by the Architect and measured by nothing: exits `0` and `1`, `-O` refused (lines 50 to 52); `6b3ace2c…` is map §0's row. **§7's, by kind.** Quoted from a committed artifact: V1's revision `2026-10-22-a`, `6` anchors, `4` re-derived, `42` rows and `39` `frozen`, map `2026-10-22-a` §0, which ships in this upload; V3's `6b3ace2c…`, map §0; V12's floor, `172,064,768`, map §6's memory row in the same revision; V16's two worktrees, map §3. Computed by an implementation independent of the one under test: V3's `7073188c…`, `1,523` lines and `84,775` bytes, by `hashlib` over the extracted bytes; V4's `58`, a static count of the self-test's checks over its syntax tree, each loop multiplied — `58`, and the Architect's run of those bytes under Python 3.12.3 printed `58 of 58`; V6's `18` = 2 + 8 × 2 from `compare_ref`'s structure, and the 18 values of `REF` from the Architect's own client and position arithmetic, exact; the self-test's projection — `thr` `8,026.396753092002830475931710145973…` and `35,708.855810187921298631769127247…` within `1e-20`, each recomputed at 80 digits by `mpmath`, `6e-36` and `5e-35` from the literals, and the powers `0.962441` and `0.022510` inside `(0.9624, 0.9625)` and `(0.0225, 0.0226)`; `START_AT` `1792757700`, integer arithmetic on `1792451400`, `300`, `1,008` and tz23's `3,900`, and `SET_INSTANT` by `date -u -d @1792757700`. Fixed by this TZ and measured by nothing: V7's `1,008`, V8's `8` files, V9's `3` files and `2` ledger lines, V11's `0` and `0`, V16's exits `0` and `1`. **No expectation depends on a quantity this TZ measures:** V15's count is an identity, after = before + copied, true at every admissible value. |
| **C3** | shape of every diff | Three paths, each new: `git cat-file -e d973ff1:<path>` exits `128` for `research/tz31-who-earns.py`, `CryptoReports/TZ-31-who-earns-report.md` and `CryptoTZ/TZ-31-who-earns.md`, so no change replaces any committed line; V3 asserts `A`. PART VI's two words for an additive diff appear nowhere in this TZ — `grep -c` prints `0`. |
| **C4** | cost of every check | §6, at the population's upper bound: the walk at most `3,042` candidates — the slack's assert passes up to 3,023 considered, and a request takes at most 20 candidates, 3,040 from 3,020, or at most 19 once fewer than 20 members remain, 3,042 from 3,023 — and at most `2,067` requests, `51` and one for each non-member, re-derived by dry runs of tz23's `candidates` with non-members placed after each of the last 48 members and at random: the maximum `51 + N` at every `N` tried to 312, and `2,067` where every candidate after the 1,007th member fails, 2,017 of them before the slack stops it; at most 25 walks; all 1,008 members at the busiest rate shown, `1,766` taker rows a market and `3.520` full rows a taker row, the formation's largest by chunk of three, `10,945` of `3,109` at chunk `1792285200` — so `6,218` and `6,267,744` full rows, `25` pages a chunk and `8,400` pages over 336 chunks. `fetch`: the walk `112` s at 340 requests, `682` s at 2,067; fetching `3,494` s at the slowest measured `0.832` s a page and a worker, `6,620` s of wall clock held; `constants` `38` s a run, `115` on a host three times slower; `score` `15` s; `rehearse` `499` s of fetching and two holds, about `1,400`; the rest `30` s a run. Wall clock about `9,200` s; **single-session processor at most about `1,070` s on a host three times slower — the fetch's `163.4` s of processor here scaled by `6,218` over the stand-in's `4,183.5` full rows a market and tripled, `729`, the constants' `25.5` s the same way twice, `227`, `rehearse`'s `27.1` tripled, `81`, and the rest under `35` — under `3,600`, so nothing is sampled.** The fail-fast bounds, derived in §6 from the same figures: the fetch's `7,200` s is `3,494` s times `2.06`; a hold's `7,200` s is the archive's longest run, `2,181` s, three times over beside the longest idle wait, `444` s, and the calendar guard's `66`; the walk's retries, 24 × `300` s = `7,200` s. Disk, by the same bound: the tree `342,943,797` and §9's copies `29,063,650`, `372,007,447` together, twice `744,014,894`, so `750,000,000` (§0.4). |
| **C5** | every count | **The set, if every candidate qualifies**, re-derived by a dry run of tz23's own `candidates` with every candidate qualifying and its clock at `1792757700`: `1,008` members in `1792451700` … `1792753800`, `1,008` considered, `51` document requests, `9` on Monday, `288` on each of Tuesday, Wednesday and Thursday and `135` on Friday, member list `e3d77b0a…`; with its clock one second earlier the walk stops BLOCKED after 50 requests, too recent — so `1792757700` is the first instant at which it can finish. **The chunks:** `336` = ⌈1,008 / 3⌉ for the set, `48` = ⌈144 / 3⌉ for the rehearsal. **The spans:** the formation `864` = (`1792451400` − `1792192500`) / 300 + 1; the rehearsal's first `1792408500` = `1792451400` − 143 × 300; the stand-in's first `1792149300` = `1792192500` − 144 × 300, `1,008` = 144 + 864; TZ-30's legs among the set's candidates `108` = (`1792548000` − `1792451700`) / 900 + 1. V1's `42` rows = `39` + `2` + `1`, read from the map, and `4` re-derived anchors: `A2`, `A4`, `A5`, `A6`. V4's `58`, counted over the syntax tree. V6's `18` = 2 + 8 × 2. V8's `8` = 2 groups × 3 files + the pool file + the constants file. V9's `3` = 2 scored files + the reading file, and `2` ledger lines, one a `score` run. The forensic store: `1,938` before §9 by map §3. The refs: `60` lines by map §1, `61` after the calendar run of 2026-10-23. |
| **C6** | every population | W0's `S`, its settlement and rebate parts, `X`, `C`, `R`, `V`, `Sh`, `thr`, both margins and the power: the named makers' fills before `T0 + 300` over the set's 1,008 members. The takers' figures: the named takers' fills over the same members, barred. Each wallet's `S` and shares: that wallet's fills over the set, barred; each band's: the group's fills in that band over the set, barred; the pools: every maker's and every taker's rows of the set's members over each market's life, barred. The feeds' three counts: every transaction of the set's members. G-REHEARSAL's 18: the formation's last 144 markets. The projection, `thr` `0.330` c and the power `0.962`: the formation's per-member `V` and `Sh` scaled to 1,008; the stand-in's `0.341` c and `0.947`: its 1,008 markets. The non-members and their reasons: the candidates considered. The timing lines: the chunks fetched fresh, each by the window it started in. Each memory peak: one mode's process. `MemAvailable` and free space: the host at each read. G-STILL: the two capture units between §3.3 and §3.9. The archive's record: its ledger's complete lines at each read, and the tags `origin` carries. `reclaim`'s counts: every file of the trees it walks. |
| **C7** | every signature and every behaviour | **tz23 at `d973ff1`, every function the TZ names, as the file holds it:** `def http_json(url, tries=8):` (233) — one `urllib.request.Request(url, headers=HEADERS, method="GET")` a try (238), `HEADERS` the two of lines 81 and 82, the last line of the function its BLOCKED assert (253); `def trades(cids, taker_only, tokens=None, keep_tx=False):` (269) — `assert c in by, "a row of %s outside the request" % c` (288), `assert r["token_id"] == tokens[c][0 if row[2] == "U" else 1], "token of %s" % c` (291), `row += [r["token_id"], r["transaction_hash"], r["proxy_wallet"]]` (293), so a row's transaction is `r[6]` and its wallet `r[7]` where `feed_check` and the groups read them, and `if not cursor:` … `break` (296 to 298); `def maker_terms(side, outcome, s, p):` (316) — `return (-s, p) if side == "B" else (s, p)` (321) and `return (s, 1 - p) if side == "B" else (-s, 1 - p)` (323), which on a flipped side give §1's four own positions; `def rebate(s, p):` (326) — `return REBATE_COEF * s * p * (1 - p)` (328), `REBATE_COEF = D("0.014")` (70); `def aggregate(t0, rows):` (342) — `x, pi = maker_terms(side, outcome, s, p)` (349), the band `band_of(ts - t0)` (350) of `BANDS` (61 and 62), `b["X"] += x`, `b["C"] += x * pi`, `b["R"] += rebate(s, p)` (353 to 355); `def qualify(t0, doc):` (375) — its eight words at lines 379 to 394, `outcomePrices` read only as `not in (["1", "0"], ["0", "1"])` (382), `feeSchedule` against `FEE_SCHEDULE` (386; 69), `CONDITION` `0x[0-9a-f]{64}` (390; 106), two digit tokens (393); `def label_of(doc):` (403) — `return {("1", "0"): 1, ("0", "1"): 0}[...]` (405); `def gate_constants(V, sh, lam=LAMBDA, alpha=ALPHA, delta=DELTA):` (410) — `thr = L / lam + lam * V / 8` (414), `"earn_at": thr, "no_earn_at": delta * sh - thr` (416), the power `0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))` with `sd = float(V.sqrt()) / 2.0` (420 to 422) — called with this TZ's `lam`, `alpha` and `delta` (line 559), not its defaults; `def reading(S, c):` (426) — `earn` first, then `no_earn` (427 to 433); `def candidates(start, spans, need, docs_of):` (449) — `next_open(start, spans)` (453), `assert len(considered) < need + WALK_SLACK` before each request (455), `min(CHUNK, need - len(members))` (458), `assert chunk[-1] <= time.time() - RESOLVED_AFTER_S` before `docs_of` (461 to 463), `break` at the need (470 and 471); `def form_set(base, start, spans, need):` (495) — an existing `set.json` returned unread by the walk (498 to 503), `candidates(start, spans, need, gamma_docs)` (505), `the set formed in %.1f s` (509); `def _malloc_tune():` (112) — `mallopt(-3, 131072)` and `mallopt(-8, 2)` (120); `def _audit(event, args):` (128) — every `open` under `CAPTURE_ROOTS`, the recorder's and the chain book's (103), refused (130 to 136); `getcontext().prec = 60` (52); `RESOLVED_AFTER_S = 3900` (78), `WALK_SLACK = 2016` (79), `FETCH_WORKERS = 2` (75), the three `EXCLUDED` spans, each ending below `1792451700` (64 to 66). **`research/tz26-nesting-b3-capture.py` at `d973ff1`:** `STREAM_FLOOR = 4500000000` (132) and `def stream_off_reason(docs_ok, free, total):` (809) — `if free < STREAM_FLOOR: return "floor"` (813 and 814). **`research/tz28-pairbook-archive-timer.py` at `d973ff1`:** `def write(self, env, rec):` (212) — `tz27.forbid(rec, "ledger.jsonl")` (215) before the append (216 and 217). Every sentence that attributes an output, a condition or a precondition to these is supported by the lines quoted; none was rewritten after this reading. |
| **C8** | every cross-reference | **This TZ's own:** §0.0 to §0.5, §1, §2's items 1 to 11 and exemptions (a) to (c), §3 to §3.10, §4 to §4.4, §5, §6, §7's V1 to V16, §8, §9's two blocks — 82 references to 22 sections before this one, each resolved to the text it names. **CANON `2026-10-22-b`:** PART II's W track — W0's row, "over every maker fill before `T0 + 300`", "on the first 1,008 qualifying markets after `1792451400`", W1 behind W-EARN — §1.1, hard rule 15. **Map `2026-10-22-a`:** §0's rows and anchors; §1's refs, 60 lines; §2.5's store, read by `du` beside `df`, and its windows after `1792403100` unread; §3's forensic store at `1,938`, TZ-30's pair, the two worktrees and the code trees' `e3975b5`, `e8b46a8` and `d8194fd`; §4's M0, rebate and B3 rows; §5's W track; §6's host identity, disk, memory, public fills and process supervision rows; §7's items 63, 87, 97, 99, 114, 115 and 118. **Contract:** §1 steps 1 to 4, §4.2, §6's determinism, §8's order. **TZ-23:** §1's "The test" and §4.3's table. **TZ-27:** its §9's copy of `set.json`, which TZ-30's host gate asserted. **TZ-30's report:** §0.3's H4, `16570` bytes and `ec71b1a7…`; §1's documents, 94 requests for 936 candidates `1791706500` … `1792548000`. Each read in its file, not from memory, and each supports the sentence that cites it. |

**Converted to BLOCK conditions under CANON hard rule 13**, because the Architect's session cannot reach the host: H1 to
H4 — the host's identity, its interpreter and its forensic store; the memory and the disk gate, and `floor_check` at
every mode that reads the venue or a set; §0.2's fingerprint against the primary checkout as it will be; §0.5's two refs
conditions; the instant, which `fetch` asserts; the set's 1,008 members, which G-SET asserts at the walk's own reading
of the venue; and G-REHEARSAL, which reads again a record the Architect read on 2026-10-22 and stops on any change in
it. **Printed and gating nothing:** the archive's ledger, the units, the boots, the timer's journal, systemd's reload
records, the package history and the tags — the Architect could not read them, and no gate of this TZ needs them but
G-STILL, which reads them itself.

---

## Appendix A — `research/tz31-who-earns.py`, byte for byte

Extracted by §0.1's script; the block's content is the file.

```python file=research/tz31-who-earns.py
#!/usr/bin/env python3
"""TZ-31 - W0, who earns: do the makers and the takers who earned most on btc-updown-5m markets M0 has read,
named before this TZ by the Architect, earn at least half a tick a share at settlement - the makers with the 20%
rebate, the takers after the fee - on the first qualifying markets no TZ has read?

    fingerprint       contract section 1 steps 3 and 4, asserted: the map's revision, anchors and rows
    selftest          every rule of this file, on literals and on temporary trees under the work tree
    still             the recorder's and the pair book's MainPID, NRestarts and ActiveState: the first run
                      records them, the second compares, the archive's own restarts read from its ledger
                      (G-STILL)
    scratch OWN       the UUID directories beside OWN, this session's, each named live or earlier
    archive           the pair book archive's ledger, read and printed, beside the tags origin carries
    rehearse          the whole path on the Architect's rehearsal span, every request held to the idle
                      stretch, against the Architect's independent figures (G-REHEARSAL)
    fetch             the set and both feeds of its fills, every request held to the idle stretch (G-SET)
    constants         label-free: each group's sums by member, V, Sh, thresholds and power, on disk
    score             the labels, read once, and each group's reading
    reclaim TREE...   section 9

It loads research/tz23-maker-m0.py from beside itself, executed from the bytes whose SHA-256 it asserts,
and calls TZ-23's functions for the walk, the documents, every request for fills, every position, cost and
rebate, the thresholds, the power and the reading: it writes no second implementation of any of them. Its
requests are TZ-23's, to gamma-api.polymarket.com and data-api.polymarket.com through TZ-23's http_json and
its two headers, each walk and each chunk started only inside seconds 15 to 470 of a 900-second window and
never near or during the pair book archive's run; and git against origin. Under /var/lib/btc-recorder,
/var/lib/btc-chainbook and /var/lib/btc-pairbook it opens and lists nothing, and under
/var/lib/btc-pairbook-archive it opens ledger.jsonl alone, for reading, in modes archive and still: an audit
hook refuses everything else there. It writes under /root/tz31-work/ and, in `reclaim`, new files in
/root/btc-forensics/ by exclusive create. It prints sums over a set - a group's, a wallet's, a band's - and no
price, size or outcome of any single fill or market. Exit 0: every assert of the mode held. Exit 1: an
assert failed, and its message names it. Run it with the recorder's interpreter, /root/tz04a-env.

Written for CryptoTZ/TZ-31-who-earns.md. The TZ is the specification.
"""

import collections
import concurrent.futures
import gzip
import hashlib
import json
import os
import re
import resource
import shutil
import subprocess
import sys
import time
import types

if not __debug__:
    sys.stderr.write("tz31: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(2)

HERE = os.path.dirname(os.path.abspath(__file__))
TZ23_NAME = "tz23-maker-m0.py"
TZ23_SHA256 = "6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f"


def load_tz23(path):
    """TZ-23's instrument, executed from the very bytes whose SHA-256 is asserted. It installs its audit hook,
    sets the main thread's decimal precision to 60 digits and tunes glibc's malloc."""
    with open(path, "rb") as fh:
        raw = fh.read()
    got = hashlib.sha256(raw).hexdigest()
    assert got == TZ23_SHA256, "%s sha256 %s, required %s" % (path, got, TZ23_SHA256)
    mod = types.ModuleType("tz23")
    mod.__file__ = path
    sys.modules["tz23"] = mod
    exec(compile(raw, path, "exec"), mod.__dict__)
    return mod


tz23 = load_tz23(os.path.join(HERE, TZ23_NAME))
D = tz23.D
out, utc, fx, dumps = tz23.out, tz23.utc, tz23.fx, tz23.dumps

# ---- the TZ's constants: none of them is measured by this run -----------------------------------------

MAP_REVISION = "2026-10-22-a"
ANCHORS = {"A1": "229a944f2d51", "A2": "6c5089330629",
           "A3": "0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable",
           "A4": "437b45ea196b", "A5": "0f6c90451cbd", "A6": "729f0bcdbee3"}
ANCHOR_FILES = {"A2": "research/twap-divergence.py", "A4": "BTC-EXECUTOR-INSTRUCTIONS.md",
                "A5": "research/recorder/recorder.py", "A6": "research/pfair.py"}
MAP_ROWS = {"frozen": 39, "tracked": 2, "reported": 1}
ROW = re.compile(r"^\| `([^`]+)` \| ([0-9,]+|—) \| ([0-9,]+|—) \| (frozen|tracked|reported) \| "
                 r"`?([0-9a-f]{64}|self-reference[^|]*?)`? \|$", re.M)
ANCHOR_ROW = re.compile(r"^\| `(A[0-9])` — [^|]*\| `([^`]+)` \|$", re.M)

M0_LAST = 1792451400         # M0's last member, 2026-10-19 23:10 UTC (TZ-29): no TZ has read a later one
START = M0_LAST + 300        # 1792451700, 2026-10-19 23:15 UTC: the set's walk starts here
N_SET = 1008                 # three and a half days of five-minute markets
START_AT = START + (N_SET - 1) * 300 + 3900    # no mode reads the set before the last member's resolution age
SET_INSTANT = "2026-10-23T12:15:00Z"          # START_AT, as the self-test asserts
FORMATION = (1792192500, 1792451400)    # the 864 markets the Architect named the groups on, all read by M0
REHEARSAL = (1792408500, 144)           # the formation's last 144 markets: G-REHEARSAL's span
FILL_CHUNK = 3               # members a chunk of fills: both feeds of three markets in memory at once
WALK_TRIES = 25              # a walk stopped on a market too recent to be resolved is walked again,
WALK_RETRY_S = 300           # 300 s later, at most 24 times more
FETCH_BUDGET_S = 7200        # a fetch projected past this after its first 30 chunks is BLOCKED
WINDOW_S = 900               # the pair book's window: its stream from T+595 to T+905, window.json at T+910
IDLE = (15, 590)             # its idle stretch: a request starts at second 15 or later and ends by 590
CHUNK_BUDGET_S = 120         # a chunk or a walk starts no later than second 470
ARCHIVE_UNIT = "btc-pairbook-archive.service"
ARCHIVE_TIMER = "btc-pairbook-archive.timer"
ARCHIVE_CALENDAR_S = 10820   # the archive's calendar run, 03:00:20 UTC
ARCHIVE_LEAD_S = 60          # nothing starts from budget + 60 s before it to 60 s after it
RUNNING = ("active", "activating", "deactivating", "reloading", "refreshing")
HOLD_MAX_S = 7200            # one window and an archive's run fit in it many times over
MEM_FLOOR = 172064768        # MemAvailable: twice the largest peak of any mode (TZ-31 section 0.4)

ALPHA = D("0.005")           # each answer's false-reading probability, for each group
DELTA = tz23.DELTA           # half a tick a share, TZ-23's and M0's bar
LIFE_BANDS = ("pre", "w0", "w1", "w2", "w3", "last")    # every fill before T0 + 300; "post" is after the reading
FLIP = {"B": "S", "S": "B"}
REBATE_RATE = tz23.FEE_SCHEDULE["rebateRate"]
GROUP_ORDER = ("makers", "takers")
GROUP_SIZE = 10
# The two groups, named by the Architect on FORMATION (TZ-31 section 1): the makers by the largest S / sqrt(V) among the
# wallets with a maker fill in at least 648 of its 864 markets, gated; the takers by the largest S among those with a
# taker fill in at least 432, barred from every reading. Each wallet as the venue's proxy_wallet prints it.
GROUPS = {
    "makers": {"role": "maker", "gated": True, "lambda": D("0.00099017"), "wallets": (
        "0x32c4922da31d9f90232ea40748846e5ccc48b175", "0xf548517cbefe7636bef51ee31a1817f021e7c20e",
        "0xbfa0ed0c199c00aec969d822818f789ca35acd6d", "0x373b2d17d78c27bbdbcb034dae71d26b8094c855",
        "0x1dd2a69e73ba444ecd5d87f0073d51a670ad51c2", "0x809f275254e21f720a4e6c50c28c669c721f2ef0",
        "0x18c18e0c8c3154360b4f730ec8b9d8013ceb2183", "0x764fd57b0b885cbeada5a119cdf0a113ee4ec347",
        "0xf79dccd12edb1e599dc3f9bff979b95987609fe9", "0xd8f1fbe130e2b33f32633bf568a08b85058e74a9")},
    "takers": {"role": "taker", "gated": False, "lambda": D("0.00022256"), "wallets": (
        "0xd84403efd50b49a1d8a7181627e00307e6ea5908", "0x129246beaac356e104c397f0985c11b7469be5a6",
        "0x41e2e1ccf1e4940029af02259a31c6b89b9fa354", "0xeebde7a0e019a63e6b476eb425505b7b3e6eba30",
        "0x5a06acbaee263540a16a0109d584f6672101ffa2", "0x20d2309cd92b797ae7ca175ed828ed8a27fbe29d",
        "0x3c58ef422754ff22c7e806336feba0064d8b776b", "0x14ea1c239393f7c1ad68c72e34e250e0679583b5",
        "0x19b3823092892c026517fd0ff58df4889abe0b9b", "0x5e2b9261b0c4f697b55bf921ff2bc227183d9101")},
}
# The projection: each group's V and Sh at the set's size, at the formation's rates, and the Architect's independent
# threshold and power at them (TZ-31 section 1)
PROJ = {"makers": (D("18528280.704135900604"), D("2085206.453030"),
                   {"thr": D("8026.39675309200283047593171014597323349"), "power": (D("0.9624"), D("0.9625"))}),
        "takers": (D("366723215.042597362222"), D("2567699.904176"),
                   {"thr": D("35708.8558101879212986317691272476559876"), "power": (D("0.0225"), D("0.0226"))})}
# The Architect's independent figures for the rehearsal span (TZ-31 section 4.1)
REF = {"members": 144, "ups": 71, "groups": {
    "makers": {"n": 32911, "sh": D("414244.819465"), "X": D("-6778.530163"), "C": D("-6531.4184270423230341"),
               "R": D("957.39614134740118920440492969386"), "V": D("4897801.198403732397"),
               "P": D("2407.4304690423230341"), "S": D("3364.82661038972422330440492969386")},
    "takers": {"n": 8326, "sh": D("412423.876637"), "X": D("-831.786637"), "C": D("14859.1622011511058812"),
               "R": D("984.45142398558404651653052080920"), "V": D("60301555.497845147905"),
               "P": D("8245.6376908488941188"), "S": D("3323.3805709209738862173473959540")}}}

WORK = "/root/tz31-work"
WT = WORK + "/wt"
STATE = WORK + "/state.json"
LEDGER = WORK + "/label-ledger.jsonl"
PRIMARY = "/root/btc-5m-twap"
REPORTS = PRIMARY + "/CryptoReports"
FORENSICS = "/root/btc-forensics"
BRANCH = "tz-31-who-earns"
UNITS = {"recorder": "btc-recorder.service", "pairbook": "btc-pairbook.service"}
CAPTURE_ROOTS = ("/var/lib/btc-recorder", "/var/lib/btc-chainbook", "/var/lib/btc-pairbook")
ARCHIVE_STATE = "/var/lib/btc-pairbook-archive"
ARCHIVE_LEDGER = ARCHIVE_STATE + "/ledger.jsonl"
SHOW_ENV = {"TZ": "UTC", "LC_ALL": "C", "SYSTEMD_COLORS": "0", "SYSTEMD_PAGER": ""}
UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
TOKEN = re.compile(r"[0-9a-f]{16,64}")
WALLET = re.compile(r"0x[0-9a-f]{40}")
LIVE_S = 60                  # a directory born this soon after a claude process started is that process's

# ---- the audit hook: TZ-31 section 2's reads and writes ------------------------------------------------

MODE = [None]
REFUSED = []
WRITE_FLAGS = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC


class GuardError(RuntimeError):
    pass


def _under(p, root):
    return p == root or p.startswith(root + "/")


def _writing(wmode, flags):
    if isinstance(wmode, str):
        return bool(set(wmode) & set("wax+"))
    return isinstance(flags, int) and bool(flags & WRITE_FLAGS)


def _exclusive(wmode, flags):
    if isinstance(wmode, str):
        return "x" in wmode
    return isinstance(flags, int) and bool(flags & os.O_EXCL)


def _path(p):
    if isinstance(p, bytes):
        p = os.fsdecode(p)
    return os.path.abspath(p) if isinstance(p, str) else None


def policy(mode, event, args):
    """None where TZ-31 section 2 allows the event in this mode; otherwise the reason it is refused."""
    p = _path(args[0]) if args else None
    if p is None:
        return None
    if event in ("os.listdir", "os.scandir"):
        if any(_under(p, r) for r in CAPTURE_ROOTS + (ARCHIVE_STATE,)):
            return "a listing under a capture root or the archive's state"
        return None
    w = _writing(args[1] if len(args) > 1 else None, args[2] if len(args) > 2 else None)
    if any(_under(p, r) for r in CAPTURE_ROOTS):
        return "an open under a capture root"
    if _under(p, ARCHIVE_STATE):
        return None if mode in ("archive", "still") and p == ARCHIVE_LEDGER and not w else \
            "an open under the archive's state"
    if _under(p, FORENSICS) and w:
        ex = _exclusive(args[1] if len(args) > 1 else None, args[2] if len(args) > 2 else None)
        return None if mode == "reclaim" and ex else "a write into the forensic store"
    if w and not _under(p, WORK):
        return "a write outside the work tree"
    return None


def _audit(event, args):
    if event not in ("open", "os.listdir", "os.scandir"):
        return
    why = policy(MODE[0], event, args)
    if why is not None:
        REFUSED.append((event, str(args[0]) if args else ""))
        raise GuardError("%s refused in mode %s, %s: %r" % (event, MODE[0], why, args[0] if args else None))


sys.addaudithook(_audit)

# ---- small helpers ----------------------------------------------------------------------------------------


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh, parse_float=D)


def load_state():
    return load_json(STATE) if os.path.exists(STATE) else {}


def save_state(st):
    tz23.write_atomic(STATE, (json.dumps(st, sort_keys=True, indent=1, default=tz23._dec) + "\n").encode("utf-8"))


def floor_check():
    """Before a mode that reads the venue or a set: glibc's two settings, and the memory floor."""
    assert tz23.MALLOC_TUNED, "BLOCKED: glibc did not take the mmap threshold and the arena count"
    avail = tz23.mem_available()
    out("MemAvailable %d bytes, floor %d" % (avail, MEM_FLOOR))
    assert avail >= MEM_FLOOR, "BLOCKED: MemAvailable %d bytes, below %d" % (avail, MEM_FLOOR)


def show(unit, props):
    """systemctl show, every stamp printed in UTC and the C locale."""
    args = ["systemctl", "show", unit]
    for prop in props:
        args += ["-p", prop]
    cp = subprocess.run(args, capture_output=True, text=True, env=dict(os.environ, **SHOW_ENV))
    assert cp.returncode == 0, "systemctl show %s: %s" % (unit, cp.stderr.strip())
    return dict(line.split("=", 1) for line in cp.stdout.split("\n") if "=" in line)


def git(*args, tree=WT):
    cp = subprocess.run(["git", "-C", tree] + list(args), capture_output=True, text=True)
    assert cp.returncode == 0, "git %s: %s" % (" ".join(args), cp.stderr.strip())
    return cp.stdout.strip()


def fill_groups_of(s):
    """The set's members in chunks of FILL_CHUNK, in T0 order: one chunk of fills each."""
    return [[(m["t0"], m["doc"]) for m in s["members"][i:i + FILL_CHUNK]]
            for i in range(0, len(s["members"]), FILL_CHUNK)]

# ---- the clock: the pair book's idle stretch and the archive's run -------------------------------------------


def archive_state():
    cp = subprocess.run(["systemctl", "is-active", ARCHIVE_UNIT], capture_output=True, text=True)
    return cp.stdout.strip()


def quiet(now, budget, state_of=archive_state):
    """None where a request of `budget` seconds may start at `now`; otherwise why it may not: it must start inside
    the pair book's idle stretch and end by its second 590, and never near or during the archive's run."""
    p = int(now) % WINDOW_S
    if not IDLE[0] <= p <= IDLE[1] - budget:
        return "second %d of the window" % p
    d = int(now) % 86400
    if ARCHIVE_CALENDAR_S - budget - ARCHIVE_LEAD_S <= d <= ARCHIVE_CALENDAR_S + ARCHIVE_LEAD_S:
        return "the archive's calendar run at 03:00:20 UTC"
    st = state_of()
    if st in RUNNING:
        return "the archive's service is %s" % st
    return None


def hold(budget, clock=time.time, sleep=time.sleep, state_of=archive_state):
    """Until a request of `budget` seconds may start; returns that instant and the seconds waited. A hold longer
    than HOLD_MAX_S - an archive's run that does not end - is BLOCKED."""
    t0 = clock()
    while True:
        now = clock()
        why = quiet(now, budget, state_of)
        if why is None:
            return now, now - t0
        assert now - t0 <= HOLD_MAX_S, "BLOCKED: held %.0f s, the last reason %s" % (now - t0, why)
        sleep(5.0)


def walk(base, start, spans, need, form=None, holdf=hold, sleep=time.sleep):
    """TZ-23's form_set, started inside the idle stretch; a walk stopped on a market too recent to be resolved is
    walked again WALK_RETRY_S later, and any other stop is final."""
    form = form or tz23.form_set
    for k in range(WALK_TRIES):
        if not os.path.exists(os.path.join(base, "set.json")):
            t, _w = holdf(CHUNK_BUDGET_S)
            out("the walk starts at second %d of window %d" % (int(t) % WINDOW_S, int(t) // WINDOW_S * WINDOW_S))
        try:
            return form(base, start, spans, need)
        except AssertionError as e:
            if "too recent to be resolved" not in str(e) or k == WALK_TRIES - 1:
                raise
            out("the walk stopped (%s); walked again in %d s, %d of %d" % (e, WALK_RETRY_S, k + 1, WALK_TRIES - 1))
            sleep(WALK_RETRY_S)
    raise AssertionError("unreachable")

# ---- the fills: both feeds of a chunk, and the makers' rows between them ------------------------------------


def split_feeds(full, taker):
    """The makers' rows of one market: its full feed less its takers' rows, as multisets of whole rows - every
    takers' row must be in the full feed. No Decimal arithmetic: it runs in the fetch's worker threads (map section 7
    item 99)."""
    left = collections.Counter(tuple(r) for r in full)
    for r in taker:
        k = tuple(r)
        assert left[k] > 0, "a takers' row not in the full feed: %r" % (r,)
        left[k] -= 1
    return sorted(list(k) for k, n in left.items() for _ in range(n))


def feed_check(taker, maker):
    """One market's transactions, those whose makers' and takers' sizes differ - the venue prints a maker's size at
    two decimals where a taker's carries six - and those with one side's rows alone. Summed in the main thread."""
    size = collections.defaultdict(lambda: [D(0), D(0)])
    for i, rows in ((0, taker), (1, maker)):
        for r in rows:
            size[r[6]][i] += D(r[3])
    differ = sum(1 for t, (a, b) in size.items() if a > 0 and b > 0 and a != b)
    one_side = sum(1 for t, (a, b) in size.items() if (a > 0) != (b > 0))
    return {"transactions": len(size), "sizes_differ": differ, "one_side_only": one_side}


def fetch_chunk2(cache, group):
    """Both feeds of up to FILL_CHUNK members by TZ-23's trades - the full feed (taker_only false) and the takers'
    (taker_only true), each row with its token, transaction and wallet - written once, atomically: a member's
    takers' rows and its makers', the full feed less the takers'."""
    path = tz23.chunk_path(cache, group[0][0])
    if os.path.exists(path):
        return path, False
    cids = [d["conditionId"] for _t, d in group]
    tokens = {d["conditionId"]: json.loads(d["clobTokenIds"]) for _t, d in group}
    full = tz23.trades(cids, "false", tokens, keep_tx=True)
    taker = tz23.trades(cids, "true", tokens, keep_tx=True)
    members = []
    for t, d in group:
        c = d["conditionId"]
        members.append({"t0": t, "condition": c, "taker": sorted(taker[c]), "maker": split_feeds(full[c], taker[c])})
    tz23.write_atomic(path, tz23.gz_bytes(dumps({"members": members})))
    return path, True


def member_rows2(cache, groups):
    """Every member's two sides, in T0 order, read back from the cache."""
    for g in groups:
        with gzip.open(tz23.chunk_path(cache, g[0][0]), "rt", encoding="utf-8") as fh:
            doc = json.load(fh)
        assert [m["t0"] for m in doc["members"]] == [t for t, _d in g], "chunk %d: its members" % g[0][0]
        for m, (t, d) in zip(doc["members"], g):
            assert m["condition"] == d["conditionId"], "chunk %d: member %d's condition" % (g[0][0], t)
            yield t, d, m


def fetch_held(base, s, timing, budget_s=FETCH_BUDGET_S, fetcher=None, holdf=hold, clock=time.time):
    """Every chunk not already in the cache fetched by `fetcher`, fetch_chunk2 by default, on TZ-23's two worker
    threads, each started where holdf allows, its start and end written to `timing`."""
    fetcher = fetcher or fetch_chunk2
    cache = os.path.join(base, "cache")
    os.makedirs(cache, exist_ok=True)
    groups = fill_groups_of(s)

    def one(group):
        if os.path.exists(tz23.chunk_path(cache, group[0][0])):
            return tz23.chunk_path(cache, group[0][0]), False, None
        start, waited = holdf(CHUNK_BUDGET_S)
        path, new = fetcher(cache, group)
        return path, new, {"first": group[0][0], "start_ns": int(start * 1e9), "end_ns": int(clock() * 1e9),
                           "waited_s": round(waited, 3)}

    t, done, fresh, busy = clock(), 0, 0, 0.0
    with concurrent.futures.ThreadPoolExecutor(max_workers=tz23.FETCH_WORKERS) as pool:
        futs = [pool.submit(one, g) for g in groups]
        try:
            for fut in futs:
                _path, new, rec = fut.result()
                done += 1
                if new:
                    fresh += 1
                    busy += (rec["end_ns"] - rec["start_ns"]) / 1e9
                    w = rec["start_ns"] // 10 ** 9 // WINDOW_S * WINDOW_S
                    rec.update({"window": w, "start_second": rec["start_ns"] / 1e9 - w,
                                "end_second": rec["end_ns"] / 1e9 - w,
                                "inside": rec["end_ns"] <= (w + IDLE[1]) * 10 ** 9})
                    with open(timing, "a", encoding="utf-8") as fh:
                        fh.write(json.dumps(rec, sort_keys=True) + "\n")
                    if fresh == 30:
                        proj = busy / fresh * len(groups) / tz23.FETCH_WORKERS
                        out("projected %.0f s of fetching for %d chunks after %d fetched; %.0f s of wall clock so "
                            "far" % (proj, len(groups), fresh, clock() - t))
                        assert proj <= budget_s, "BLOCKED: fetching projected at %.0f s, above %d" % (proj, budget_s)
                if done % 25 == 0 or done == len(groups):
                    out("chunks %d of %d, %.0f s" % (done, len(groups), clock() - t))
        except BaseException:
            for f in futs:
                f.cancel()
            raise
    return cache, groups


def timing_summary(path):
    """Every chunk fetched fresh: its start and end against the idle stretch of the window it started in."""
    recs = []
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            recs = [json.loads(ln) for ln in fh if ln.strip()]
    outside = [r for r in recs if not r["inside"]]
    if recs:
        out("chunks fetched fresh %d: inside the idle stretch %d, ending after second %d %d; longest %.1f s; "
            "waited %.0f s; windows %d, from %s to %s" % (
                len(recs), len(recs) - len(outside), IDLE[1], len(outside),
                max((r["end_ns"] - r["start_ns"]) / 1e9 for r in recs), sum(r["waited_s"] for r in recs),
                len({r["window"] for r in recs}), utc(min(r["window"] for r in recs)),
                utc(max(r["window"] for r in recs))))
    for r in outside:
        out("chunk %d started at second %.1f of window %d and ended at second %.1f" % (
            r["first"], r["start_second"], r["window"], r["end_second"]))
    return recs, outside

# ---- a group's sums: TZ-23's aggregate on a wallet's own rows ------------------------------------------------


def own_rows(rows):
    """A wallet's own rows as TZ-23's aggregate reads a taker's: the side flipped, so that its maker_terms give the
    wallet's own position - BUY Up +s at p, SELL Up -s at p, BUY Down -s at 1 - p, SELL Down +s at 1 - p."""
    return [[r[0], FLIP[r[1]], r[2], r[3], r[4]] for r in rows]


def life_of(bands):
    """The sums over every fill before T0 + 300: TZ-23's bands pre, w0 to w3 and last."""
    z = tz23.zero()
    for name in LIFE_BANDS:
        for k in z:
            z[k] += bands[name][k]
    return z


def side_rows(m, role):
    return m["maker"] if role == "maker" else m["taker"]


def extra_of(role, R):
    """A group's own money beyond settlement: a maker's rebate, R itself; a taker's fee, R over the rebate rate,
    so 0.07 s p (1 - p), taken off."""
    return R if role == "maker" else -(R / REBATE_RATE)


BAND_NAMES = [n for n, _l, _h in tz23.BANDS]
COLS2 = ["t0"] + ["%s_%s" % (k, b) for b in ["life"] + BAND_NAMES for k in ("n", "sh", "X", "C", "R")]
WCOLS = ["t0", "wallet", "n", "sh", "X", "C", "R"]
PCOLS = ["t0"] + ["%s_%s" % (k, r) for r in ("maker", "taker") for k in ("n", "sh", "X", "C", "R")] + [
    "transactions", "sizes_differ", "one_side_only"]


def cells(agg):
    return [str(agg[k]) if k == "n" else fx(agg[k]) for k in ("n", "sh", "X", "C", "R")]


def build_constants2(base, s, cache, groups, label):
    """Label-free: for each group its members file - every member's sums over its life and by band - its wallets
    file, its fills file and its gate; the pool of all makers and all takers beside them. A second run must write
    the same bytes."""
    t0s = [m["t0"] for m in s["members"]]
    sel = {g: frozenset(GROUPS[g]["wallets"]) for g in GROUP_ORDER}
    lines = {g: [",".join(COLS2)] for g in GROUP_ORDER}
    wlines = {g: [",".join(WCOLS)] for g in GROUP_ORDER}
    plines = [",".join(PCOLS)]
    tot = {g: {"V": D(0), "life": tz23.zero(), "members_with_fills": 0, "wallets_seen": set()} for g in GROUP_ORDER}
    fills = {g: os.path.join(base, "%s-%s-fills.jsonl.gz" % (label, g)) for g in GROUP_ORDER}
    raws = {g: open(fills[g] + ".build", "wb") for g in GROUP_ORDER}
    gzs = {g: gzip.GzipFile(filename="", mode="wb", fileobj=raws[g], mtime=0) for g in GROUP_ORDER}
    try:
        for t0, d, m in member_rows2(cache, groups):
            pool = []
            for role in ("maker", "taker"):
                b, _w = tz23.aggregate(t0, own_rows(side_rows(m, role)))
                pool += cells(life_of(b))
            chk = feed_check(m["taker"], m["maker"])
            plines.append(",".join([str(t0)] + pool + [str(chk[k]) for k in (
                "transactions", "sizes_differ", "one_side_only")]))
            for g in GROUP_ORDER:
                role = GROUPS[g]["role"]
                rows = [r for r in side_rows(m, role) if r[7] in sel[g]]
                bands, _win = tz23.aggregate(t0, own_rows(rows))
                life = life_of(bands)
                tt = tot[g]
                tt["V"] += life["X"] * life["X"]
                for k in life:
                    tt["life"][k] += life[k]
                tt["members_with_fills"] += 1 if life["n"] else 0
                row = [str(t0)] + cells(life)
                for name in BAND_NAMES:
                    row += cells(bands[name])
                lines[g].append(",".join(row))
                byw = collections.defaultdict(list)
                for r in rows:
                    byw[r[7]].append(r)
                for w in sorted(byw):
                    wb, _ww = tz23.aggregate(t0, own_rows(byw[w]))
                    wlines[g].append(",".join([str(t0), w] + cells(life_of(wb))))
                    tt["wallets_seen"].add(w)
                gzs[g].write(dumps({"t0": t0, "rows": sorted(rows)}).encode("utf-8"))
    finally:
        for g in GROUP_ORDER:
            gzs[g].close()
            raws[g].close()
    paths = {}
    gate = {}
    for g in GROUP_ORDER:
        tmp = fills[g] + ".build"
        fsha = tz23.sha256_file(tmp)
        if os.path.exists(fills[g]):
            assert tz23.sha256_file(fills[g]) == fsha, "determinism: %s differs" % fills[g]
            os.remove(tmp)
            out("unchanged %s sha256 %s" % (fills[g], fsha))
        else:
            os.replace(tmp, fills[g])
        paths["%s-fills.jsonl.gz" % g] = (fills[g], fsha)
        for name, body in (("members.csv", lines[g]), ("wallets.csv", wlines[g])):
            pth = os.path.join(base, "%s-%s-%s" % (label, g, name))
            paths["%s-%s" % (g, name)] = (pth, tz23.write_once(pth, ("\n".join(body) + "\n").encode("utf-8")))
        tt, gc = tot[g], GROUPS[g]
        c = tz23.gate_constants(tt["V"], tt["life"]["sh"], lam=gc["lambda"], alpha=ALPHA, delta=DELTA)
        gate[g] = {"role": gc["role"], "gated": gc["gated"], "wallets": list(gc["wallets"]),
                   "wallets_with_fills": len(tt["wallets_seen"]),
                   "members_with_fills": tt["members_with_fills"], "life": tt["life"], "gate": c,
                   "members_csv_sha": paths["%s-members.csv" % g][1], "wallets_csv_sha": paths["%s-wallets.csv" % g][1],
                   "fills_sha": fsha}
    ppath = os.path.join(base, "%s-pool.csv" % label)
    paths["pool.csv"] = (ppath, tz23.write_once(ppath, ("\n".join(plines) + "\n").encode("utf-8")))
    nonm = [[t, st] for t, st in s["considered"] if st != "member"]
    const = {"label": label, "members": len(t0s), "first": t0s[0], "last": t0s[-1],
             "member_list_sha": tz23.sha256_bytes(("\n".join(map(str, t0s)) + "\n").encode()),
             "considered": len(s["considered"]), "non_members": nonm, "groups": gate,
             "pool_csv_sha": paths["pool.csv"][1]}
    cpath = os.path.join(base, "%s-constants.json" % label)
    paths["constants.json"] = (cpath, tz23.write_once(cpath, dumps(const).encode("utf-8")))
    return const, paths


def show_constants2(const, paths):
    out("members %d, considered %d, first %d %s, last %d %s; member list sha %s" % (
        const["members"], const["considered"], const["first"], utc(const["first"]), const["last"],
        utc(const["last"]), const["member_list_sha"]))
    for t, st in const["non_members"]:
        out("non-member %d %s: %s" % (t, utc(t), st))
    for g in GROUP_ORDER:
        gg, c, lf = const["groups"][g], const["groups"][g]["gate"], const["groups"][g]["life"]
        out("%s (%s rows of %d wallets, %d of them with a fill): members with a fill %d; fills %d, shares %s, "
            "X %s, C %s, R %s" % (g, gg["role"], len(gg["wallets"]), gg["wallets_with_fills"],
                                  gg["members_with_fills"], lf["n"], fx(lf["sh"]), fx(lf["X"]), fx(lf["C"]),
                                  fx(lf["R"])))
        out("%s: V %s; Sh %s; lambda %s; L %s; thr %s (%s a share)" % (
            g, fx(c["V"]), fx(c["sh"]), fx(c["lambda"]), q12(c["L"]), q12(c["thr"]),
            q12(c["thr_per_share"]) if "thr_per_share" in c else "-"))
        out("%s%s: W-EARN at S >= %s (%s a share); W-NO-EARN at S <= %s (%s a share); power of either answer "
            "against the other's alternative %s" % (
                g, "" if gg["gated"] else ", barred from every reading", q12(c["earn_at"]),
                q12(c["thr_per_share"]) if "thr_per_share" in c else "-", q12(c["no_earn_at"]),
                q12(c["no_earn_per_share"]) if "no_earn_per_share" in c else "-", fx(c["power"])))
    for name, (p, h) in sorted(paths.items()):
        out("wrote %s sha256 %s" % (p, h))


def q12(x):
    """A figure for print, half-even to 12 places; every sum and comparison is made on the exact figure."""
    return fx(x.quantize(D("0.000000000001")))


def read_csv(path, cols):
    with open(path, encoding="utf-8") as fh:
        rows = [ln.split(",") for ln in fh.read().splitlines()]
    assert rows[0] == cols, "%s: its header" % path
    return rows[1:]


WORDS = {"EARN": "W-EARN", "NO EARN": "W-NO-EARN", "UNDECIDABLE": "UNDECIDABLE"}


def score2(base, s, const, label):
    """The labels, read once from the set's own documents, and each group's reading by TZ-23's reading on this TZ's
    thresholds; beside them, barred from every reading, each wallet's, each band's and the pool's result."""
    docs = {m["t0"]: m["doc"] for m in s["members"]}
    ups = {t: tz23.label_of(d) for t, d in docs.items()}
    res = {"label": label, "members": len(docs), "ups": sum(ups.values()), "groups": {}}
    scored = {}
    for g in GROUP_ORDER:
        gg = const["groups"][g]
        role, c = gg["role"], gg["gate"]
        rows = read_csv(os.path.join(base, "%s-%s-members.csv" % (label, g)), COLS2)
        assert [int(r[0]) for r in rows] == [m["t0"] for m in s["members"]], "%s: members" % g
        ix = {k: i for i, k in enumerate(COLS2)}
        S = P = E = D(0)
        bands = {b: [D(0), D(0)] for b in BAND_NAMES}
        out_rows = ["t0,up,X,C,R,pnl"]
        for r in rows:
            t0 = int(r[0])
            up = ups[t0]
            X, C, R = D(r[ix["X_life"]]), D(r[ix["C_life"]]), D(r[ix["R_life"]])
            settle, extra = X * up - C, extra_of(role, R)
            S += settle + extra
            P += settle
            E += extra
            out_rows.append("%d,%d,%s,%s,%s,%s" % (t0, up, fx(X), fx(C), fx(R), fx(settle + extra)))
            for b in BAND_NAMES:
                bands[b][0] += D(r[ix["X_" + b]]) * up - D(r[ix["C_" + b]]) + extra_of(role, D(r[ix["R_" + b]]))
                bands[b][1] += D(r[ix["sh_" + b]])
        word, earn, no_earn = tz23.reading(S, {"earn_at": D(c["earn_at"]), "no_earn_at": D(c["no_earn_at"])})
        sh = D(c["sh"])
        wl = read_csv(os.path.join(base, "%s-%s-wallets.csv" % (label, g)), WCOLS)
        per_w = collections.defaultdict(lambda: [D(0), D(0), 0])
        for t0, w, n, shw, X, C, R in wl:
            up = ups[int(t0)]
            per_w[w][0] += D(X) * up - D(C) + extra_of(role, D(R))
            per_w[w][1] += D(shw)
            per_w[w][2] += 1
        res["groups"][g] = {
            "role": role, "gated": gg["gated"], "S": S, "settlement": P, "extra": E, "sh": sh,
            "reading": WORDS[word] if gg["gated"] else None, "w_earn": earn, "w_no_earn": no_earn,
            "per_share": S / sh if sh else None, "settlement_per_share": P / sh if sh else None,
            "extra_per_share": E / sh if sh else None, "margin_w_earn": S - D(c["earn_at"]),
            "margin_w_no_earn": D(c["no_earn_at"]) - S,
            "barred_wallets": {w: {"S": v[0], "sh": v[1], "members": v[2], "per_share": v[0] / v[1] if v[1] else None}
                               for w, v in sorted(per_w.items())},
            "barred_bands": {b: {"S": v[0], "sh": v[1], "per_share": v[0] / v[1] if v[1] else None}
                             for b, v in bands.items()}}
        scored[g] = ("\n".join(out_rows) + "\n").encode("utf-8")
    prow = read_csv(os.path.join(base, "%s-pool.csv" % label), PCOLS)
    pi = {k: i for i, k in enumerate(PCOLS)}
    pool = {}
    for role in ("maker", "taker"):
        S = sh = D(0)
        for r in prow:
            up = ups[int(r[0])]
            S += D(r[pi["X_" + role]]) * up - D(r[pi["C_" + role]]) + extra_of(role, D(r[pi["R_" + role]]))
            sh += D(r[pi["sh_" + role]])
        pool[role] = {"S": S, "sh": sh, "per_share": S / sh if sh else None}
    res["barred_pool"] = pool
    res["checks"] = {k: sum(int(r[pi[k]]) for r in prow) for k in ("transactions", "sizes_differ", "one_side_only")}
    paths = {}
    for g in GROUP_ORDER:
        p = os.path.join(base, "%s-%s-scored.csv" % (label, g))
        paths[g] = tz23.write_once(p, scored[g])
    rp = os.path.join(base, "%s-reading.json" % label)
    paths["reading"] = tz23.write_once(rp, dumps(res).encode("utf-8"))
    out("labels: %d members, %d Up" % (len(docs), res["ups"]))
    for g in GROUP_ORDER:
        r = res["groups"][g]
        out("%s: S %s = settlement %s + %s %s; per share %s = %s + %s" % (
            g, fx(r["S"]), fx(r["settlement"]), "rebate" if r["role"] == "maker" else "fee", fx(r["extra"]),
            q12(r["per_share"]), q12(r["settlement_per_share"]), q12(r["extra_per_share"])))
        out("%s%s: W-EARN %s (margin %s); W-NO-EARN %s (margin %s)" % (
            g, "" if r["gated"] else ", barred from every reading", r["w_earn"], q12(r["margin_w_earn"]),
            r["w_no_earn"], q12(r["margin_w_no_earn"])))
        for w, v in r["barred_wallets"].items():
            out("%s barred: wallet %s, %d members, shares %s, S %s, per share %s" % (
                g, w, v["members"], fx(v["sh"]), q12(v["S"]), q12(v["per_share"]) if v["per_share"] is not None
                else "-"))
        for b, v in r["barred_bands"].items():
            if v["sh"]:
                out("%s barred: band %-4s shares %s, S %s, per share %s" % (g, b, fx(v["sh"]), q12(v["S"]),
                                                                           q12(v["per_share"])))
    for role, v in pool.items():
        out("barred: every %s together: S %s on %s shares, %s a share" % (
            role, q12(v["S"]), fx(v["sh"]), q12(v["per_share"]) if v["per_share"] is not None else "-"))
    out("the feeds: %d transactions, makers' and takers' sizes differ at %d, one side only at %d" % (
        res["checks"]["transactions"], res["checks"]["sizes_differ"], res["checks"]["one_side_only"]))
    for g in GROUP_ORDER:
        out("wrote %s-%s-scored.csv sha256 %s" % (label, g, paths[g]))
    out("wrote %s-reading.json sha256 %s" % (label, paths["reading"]))
    return res

# ---- the archive's record --------------------------------------------------------------------------------


def ledger_summary(recs):
    """The archive's runs, from its own records: each run's events, its set, its terminal record and whether it
    began on the calendar; whether the archive is halted. Pure: it reads nothing but `recs`."""
    runs, order = {}, []
    for r in recs:
        a = r.get("run")
        if a not in runs:
            runs[a] = []
            order.append(a)
        runs[a].append(r)
    lines = []
    for a in order:
        rs = runs[a]
        ev = [r.get("event") for r in rs]
        term = [e for e in ev if e in ("complete", "empty", "halt")]
        last = lambda name: [r for r in rs if r.get("event") == name][-1:]
        sec = a % 86400 if isinstance(a, int) else None
        when = "calendar" if sec == ARCHIVE_CALENDAR_S else ("off-calendar, second %s of the day" % sec)
        parts = ["run %s %s, %s: %d records %s; terminal %s" % (a, utc(a) if isinstance(a, int) else "-", when,
                                                                len(rs), ev, term[-1] if term else "none")]
        for r in last("set"):
            parts.append("set %s: %s files, %s bytes, windows %s to %s of %s considered" % (
                r.get("tag"), r.get("assets_n"), r.get("bytes_total"), r.get("first_T"), r.get("last_T"),
                r.get("windows_considered")))
        for r in last("upload"):
            parts.append("Release %s: sent %s, held %s, credential %s" % (r.get("release_id"), r.get("sent"),
                                                                         r.get("held"), r.get("credential")))
        for r in last("delete"):
            parts.append("removed %s, freed %s bytes, free after %s" % (r.get("removed"), r.get("freed"),
                                                                       r.get("free_after")))
        for r in last("restart"):
            parts.append("restart: window %s, pid %s after %s, NRestarts %s" % (r.get("W"), r.get("pid"),
                                                                              r.get("stopped"), r.get("NRestarts")))
        for r in last("resume"):
            parts.append("resume %s at window %s" % (r.get("reading"), r.get("T")))
        for r in last("complete"):
            parts.append("complete: requests %s, started outside %s, ended outside %s, store %s bytes, free %s, "
                         "rate %s a day" % (r.get("requests"), r.get("started_outside"), r.get("ended_outside"),
                                            r.get("store_stream_bytes"), r.get("free_bytes"), r.get("rate_per_day")))
        for r in rs:
            if r.get("event") in ("deferred", "halt", "refused", "timer-disabled"):
                parts.append("%s in %s: %s" % (r.get("event"), r.get("phase"), r.get("reason", r.get("exit"))))
        lines.append("; ".join(parts))
    flags = [r.get("event") for r in recs if r.get("event") in ("halt", "clear")]
    sets = [r for r in recs if r.get("event") == "set"]
    gaps = [[p.get("last_T"), q.get("first_T")] for p, q in zip(sets, sets[1:])
            if isinstance(p.get("last_T"), int) and q.get("first_T") != p["last_T"] + 900]
    return {"runs": order, "lines": lines, "halted": bool(flags) and flags[-1] == "halt",
            "terminal": {a: [r.get("event") for r in runs[a] if r.get("event") in ("complete", "empty", "halt")]
                         for a in order},
            "tags": [r.get("tag") for r in sets], "assets": sum(r.get("assets_n") or 0 for r in sets),
            "bytes": sum(r.get("bytes_total") or 0 for r in sets), "gaps": gaps}

# ---- modes -----------------------------------------------------------------------------------------------------


def mode_fingerprint():
    with open(os.path.join(PRIMARY, "SYSTEM-MAP.md"), "rb") as fh:
        raw = fh.read()
    txt = raw.decode("utf-8")
    rev = re.findall(r"^\*\*Revision string:\*\* `([^`]+)`$", txt, re.M)
    assert rev == [MAP_REVISION], "map revision %r, required %s" % (rev, MAP_REVISION)
    found = dict(ANCHOR_ROW.findall(txt))
    assert found == ANCHORS, "anchors %r" % found
    for k, rel in sorted(ANCHOR_FILES.items()):
        h = tz23.sha256_file(os.path.join(PRIMARY, rel))[:12]
        assert h == ANCHORS[k], "re-derived %s %s, the map %s" % (k, h, ANCHORS[k])
        out("re-derived %s %s sha256[:12] %s equal" % (k, rel, h))
    rows = ROW.findall(txt)
    states = {k: sum(1 for r in rows if r[3] == k) for k in MAP_ROWS}
    assert states == MAP_ROWS and len(rows) == sum(MAP_ROWS.values()), "rows %r" % states
    for path, lines, nbytes, state, sha in rows:
        with open(os.path.join(PRIMARY, path), "rb") as fh:
            blob = fh.read()
        got = (blob.count(b"\n"), len(blob), tz23.sha256_bytes(blob))
        if state == "frozen":
            want = (int(lines.replace(",", "")), int(nbytes.replace(",", "")), sha)
            assert got == want, "frozen row %s: %r, the map %r" % (path, got, want)
        out("%-44s %6d lines %8d bytes %s %s%s" % (path, got[0], got[1], got[2], state,
                                                  " equal" if state == "frozen" else ""))
    with open(os.path.join(PRIMARY, "research", TZ23_NAME), "rb") as fh:
        t23 = tz23.sha256_bytes(fh.read())
    assert t23 == TZ23_SHA256, "the primary checkout's %s sha256 %s" % (TZ23_NAME, t23)
    out("SYSTEM-MAP.md %d lines %d bytes sha256 %s" % (raw.count(b"\n"), len(raw), tz23.sha256_bytes(raw)))
    out("FINGERPRINT PASS: revision %s; anchors 6 of 6, 4 re-derived; rows %d: frozen %d of %d equal, tracked %d, "
        "reported %d; %s is the file this instrument loads" % (
            MAP_REVISION, len(rows), states["frozen"], MAP_ROWS["frozen"], states["tracked"], states["reported"],
            TZ23_NAME))


def still_reading(before, now, restarts):
    """G-STILL from the two reads and the archive's restart records between them, in order: PASS where both units
    are unchanged, or where the recorder is unchanged and the pair book's change is the archive's own restarts alone -
    a chain of records from the recorded MainPID to the current one, NRestarts one higher at each, the unit active.
    Pure: it reads nothing but its arguments."""
    if now == before:
        return True, "unchanged"
    if now["recorder"] != before["recorder"]:
        return False, "the recorder changed"
    b, n = before["pairbook"], now["pairbook"]
    pid, count = b["MainPID"], int(b["NRestarts"])
    for r in restarts:
        if str(r.get("stopped")) != pid or str(r.get("NRestarts")) != str(count + 1):
            return False, "a restart record that does not follow %s at NRestarts %d: %r" % (pid, count, r)
        pid, count = str(r.get("pid")), count + 1
    if restarts and pid == n["MainPID"] and str(count) == n["NRestarts"] and n["ActiveState"] == "active":
        return True, "changed by the archive's own restarts alone: %d" % len(restarts)
    return False, "the pair book changed, %d restart records of the archive since the first read" % len(restarts)


def ledger_records():
    """The archive's ledger, its complete lines; opened in modes archive and still alone (section 2 item 4)."""
    with open(ARCHIVE_LEDGER, "rb") as fh:
        raw = fh.read()
    lines = raw.split(b"\n")
    tail = lines.pop()
    return raw, [json.loads(ln) for ln in lines if ln.strip()], tail


def mode_still():
    st = load_state()
    now = {}
    for key, unit in sorted(UNITS.items()):
        kv = show(unit, ["MainPID", "NRestarts", "ActiveState", "MemoryCurrent", "MemoryPeak"])
        now[key] = {k: kv[k] for k in ("MainPID", "NRestarts", "ActiveState")}
        out("%s %s, MemoryCurrent %s, MemoryPeak %s" % (unit, now[key], kv.get("MemoryCurrent"), kv.get("MemoryPeak")))
    for unit in (ARCHIVE_TIMER, ARCHIVE_UNIT):
        kv = show(unit, ["ActiveState", "SubState", "UnitFileState", "Result"])
        out("%s %s" % (unit, kv))
    if "still" not in st:
        st["still"] = {"at": utc(time.time()), "at_ns": time.time_ns(), "units": now}
        save_state(st)
        out("still: recorded")
        return
    _raw, recs, _tail = ledger_records()
    since = st["still"]["at_ns"]
    restarts = [r for r in recs if r.get("event") == "restart" and r.get("wall_ns", 0) >= since]
    for r in restarts:
        out("the archive's restart record %s: run %s, window %s, pid %s after %s, NRestarts %s" % (
            utc(r["wall_ns"] / 1e9), r.get("run"), r.get("W"), r.get("pid"), r.get("stopped"), r.get("NRestarts")))
    ok, why = still_reading(st["still"]["units"], now, restarts)
    out("G-STILL %s: %s since %s" % ("PASS" if ok else "FAIL", why, st["still"]["at"]))


def proc_start_times():
    """The start instant of every running process whose argv[0] is `claude` or ends in `/claude.exe`."""
    with open("/proc/stat", encoding="utf-8") as fh:
        btime = int([ln for ln in fh.read().split("\n") if ln.startswith("btime ")][0].split()[1])
    hz = os.sysconf("SC_CLK_TCK")
    found = []
    for pid in sorted((p for p in os.listdir("/proc") if p.isdigit()), key=int):
        try:
            with open("/proc/%s/cmdline" % pid, "rb") as fh:
                argv = fh.read().split(b"\0")
            with open("/proc/%s/stat" % pid, encoding="utf-8") as fh:
                fields = fh.read().rsplit(")", 1)[1].split()
        except OSError:
            continue
        a0 = argv[0].decode("utf-8", "replace") if argv else ""
        if a0 == "claude" or a0.endswith("/claude.exe"):
            found.append((int(pid), btime + int(fields[19]) / hz, a0))
    return found


def birth(path):
    cp = subprocess.run(["stat", "-c", "%W", path], capture_output=True, text=True)
    assert cp.returncode == 0, cp.stderr
    return int(cp.stdout.strip())


def mode_scratch(own):
    """Lists the UUID directories beside `own`, this session's, and names each live or earlier."""
    parent = os.path.dirname(own)
    procs = proc_start_times()
    for pid, t, a0 in procs:
        out("running %d started %s %s" % (pid, utc(t), a0))
    for name in sorted(os.listdir(parent)):
        path = os.path.join(parent, name)
        if path == own or not UUID.fullmatch(name) or not os.path.isdir(path):
            continue
        b = birth(path)
        owner = [pid for pid, t, _a in procs if t - 1 <= b <= t + LIVE_S]
        out("%s born %s: %s" % (name, utc(b), ("live, process %s" % owner) if owner else "earlier"))


def mode_archive():
    """The archive's own record, read whole: its complete lines, each printed, and its runs summarized."""
    for unit in (ARCHIVE_TIMER, ARCHIVE_UNIT):
        out("%s %s" % (unit, show(unit, ["ActiveState", "SubState", "UnitFileState", "Result", "ExecMainStatus",
                                         "LastTriggerUSec", "NextElapseUSecRealtime"])))
    raw, recs, tail = ledger_records()
    out("ledger %s: %d bytes sha256 %s, %d complete records, %d bytes of a line still written" % (
        ARCHIVE_LEDGER, len(raw), tz23.sha256_bytes(raw), len(recs), len(tail)))
    for r in recs:
        out("L %s %s" % (utc(r["wall_ns"] / 1e9), json.dumps(r, sort_keys=True)))
    summ = ledger_summary(recs)
    for ln in summ["lines"]:
        out(ln)
    tags = sorted(ln.split("\t")[1][len("refs/tags/"):] for ln in git(
        "ls-remote", "origin", "refs/tags/pairbook-streams-*", tree=PRIMARY).split("\n") if "\t" in ln)
    out("tags on origin %d: %s" % (len(tags), tags))
    out("the ledger's sets %d, %d files, %d bytes; their tags not on origin %s; tags on origin without a set %s" % (
        len(summ["tags"]), summ["assets"], summ["bytes"], sorted(set(summ["tags"]) - set(tags)),
        sorted(set(tags) - set(summ["tags"]))))
    out("runs %d; without a terminal record %s; windows skipped between consecutive sets %s; halted %s" % (
        len(summ["runs"]), [a for a, t in summ["terminal"].items() if not t], summ["gaps"], summ["halted"]))


def figures(const, res):
    """The figures G-REHEARSAL compares: the members, the Up count, and each group's sums over the span."""
    got = {"members": const["members"], "ups": res["ups"], "groups": {}}
    for g in GROUP_ORDER:
        lf, c, r = const["groups"][g]["life"], const["groups"][g]["gate"], res["groups"][g]
        got["groups"][g] = {"n": lf["n"], "sh": lf["sh"], "X": lf["X"], "C": lf["C"], "R": lf["R"], "V": c["V"],
                            "P": r["settlement"], "S": r["S"]}
    return got


def compare_ref(got, ref=None):
    """Every figure against the Architect's, exactly: a list of (name, equal)."""
    ref = ref or REF
    checks = [("members", got["members"] == ref["members"]), ("ups", got["ups"] == ref["ups"])]
    for g in GROUP_ORDER:
        for k in ("n", "sh", "X", "C", "R", "V", "P", "S"):
            checks.append(("%s %s" % (g, k), got["groups"][g][k] == ref["groups"][g][k]))
    return checks


def mode_rehearse():
    floor_check()
    base = os.path.join(WORK, "rehearsal")
    s = walk(base, REHEARSAL[0], (), REHEARSAL[1])
    assert len(s["members"]) == REF["members"] and len(s["considered"]) == REF["members"], \
        "G-REHEARSAL: %d members of %d considered" % (len(s["members"]), len(s["considered"]))
    cache, groups = fetch_held(base, s, os.path.join(base, "rehearsal-timing.jsonl"), budget_s=10 ** 9)
    timing_summary(os.path.join(base, "rehearsal-timing.jsonl"))
    const, paths = build_constants2(base, s, cache, groups, "rehearsal")
    show_constants2(const, paths)
    res = score2(base, s, const, "rehearsal")
    got = figures(const, res)
    checks = compare_ref(got)
    for name, eq in checks:
        g, _sp, k = name.partition(" ")
        a = got["groups"][g][k] if k else got[name]
        b = REF["groups"][g][k] if k else REF[name]
        out("G-REHEARSAL %-12s instrument %s, the Architect's %s, %s" % (name, a, b, "equal" if eq else "DIFFERENT"))
    bad = [n for n, eq in checks if not eq]
    assert not bad, "G-REHEARSAL FAIL: %s" % bad
    out("G-REHEARSAL PASS: %d of %d figures equal to the Architect's" % (len(checks), len(checks)))


def the_set():
    base = os.path.join(WORK, "set")
    s = load_json(os.path.join(base, "set.json"))
    return base, s, os.path.join(base, "cache"), fill_groups_of(s)


def mode_fetch():
    now = time.time()
    assert now >= START_AT, "BLOCKED: %s is before %s, TZ-31's instant" % (utc(now), utc(START_AT))
    floor_check()
    base = os.path.join(WORK, "set")
    os.makedirs(base, exist_ok=True)
    s = walk(base, START, tz23.EXCLUDED, N_SET)
    t0s = [m["t0"] for m in s["members"]]
    assert s["start"] == START and s["need"] == N_SET and len(t0s) == N_SET, "G-SET: %d members" % len(t0s)
    assert s["considered"][0][0] == START and t0s[0] > M0_LAST, "G-SET: the walk did not start at %d" % START
    cache, groups = fetch_held(base, s, os.path.join(base, "fetch-timing.jsonl"))
    n = sum(1 for _ in member_rows2(cache, groups))
    assert n == N_SET, "G-SET: %d members read back" % n
    timing_summary(os.path.join(base, "fetch-timing.jsonl"))
    out("G-SET PASS: %d members, %d considered, %d to %d, %d chunks, every chunk read back" % (
        N_SET, len(s["considered"]), t0s[0], t0s[-1], len(groups)))


def mode_constants():
    floor_check()
    base, s, cache, groups = the_set()
    assert len(s["members"]) == N_SET and s["start"] == START, "the set"
    const, paths = build_constants2(base, s, cache, groups, "tz31")
    show_constants2(const, paths)
    st = load_state()
    st["constants_sha"], st["constants_at"] = paths["constants.json"][1], utc(time.time())
    save_state(st)


def mode_score():
    floor_check()
    base, s, _cache, _groups = the_set()
    cpath = os.path.join(base, "tz31-constants.json")
    st = load_state()
    assert tz23.sha256_file(cpath) == st.get("constants_sha"), "score: not the constants recorded"
    head = git("rev-parse", "HEAD")
    assert "origin/" + BRANCH in git("branch", "-r", "--contains", head).split(), \
        "score: HEAD %s is not on origin" % head
    const = load_json(cpath)
    t0s = [m["t0"] for m in s["members"]]
    assert tz23.sha256_bytes(("\n".join(map(str, t0s)) + "\n").encode()) == const["member_list_sha"], \
        "score: the members are not the constants' members"
    with open(LEDGER, "a", encoding="utf-8") as fh:
        fh.write(dumps({"at": utc(time.time()), "head": head, "members": const["members"],
                        "member_list_sha": const["member_list_sha"]}))
    res = score2(base, s, const, "tz31")
    r = res["groups"]["makers"]
    if r["w_earn"] and r["w_no_earn"]:
        out("both bounds hold: the reading is W-EARN, and half a tick a share is rejected too (TZ-23 section 4.3)")
    out("W0 READING, THE MAKERS: %s" % r["reading"])


def report_tokens():
    tokens = set()
    for name in sorted(os.listdir(REPORTS)):
        if name.endswith(".md"):
            with open(os.path.join(REPORTS, name), encoding="utf-8", errors="replace") as fh:
                tokens.update(TOKEN.findall(fh.read()))
    return tokens


def by_name(tree, rel):
    return tree == WORK and (rel in ("state.json", "label-ledger.jsonl") or rel.startswith("logs/"))


def pristine(tree):
    cp = subprocess.run(["git", "-C", tree, "status", "--porcelain", "--ignored"], capture_output=True, text=True)
    assert cp.returncode == 0 and cp.stdout == "", "reclaim: %s holds %r" % (tree, cp.stdout[:400])
    head = subprocess.run(["git", "-C", tree, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    up = subprocess.run(["git", "-C", tree, "rev-parse", "@{u}"], capture_output=True, text=True)
    assert up.returncode == 0 and up.stdout.strip() == head, \
        "reclaim: %s is at %s, its upstream at %r" % (tree, head, up.stdout.strip())
    out("reclaim: %s skipped: no file but its HEAD's, and HEAD %s is its upstream's" % (tree, head))


def reclaimable(tree):
    if tree == WORK:
        return True
    return (tree.startswith("/tmp/") and os.path.isdir(tree) and not os.path.islink(tree)
            and UUID.fullmatch(os.path.basename(tree)) is not None
            and "btc-5m-twap" in os.path.basename(os.path.dirname(tree)))


def mode_reclaim(trees):
    assert trees and all(reclaimable(t) for t in trees), "reclaim: %r" % (trees,)
    procs = proc_start_times()
    for t in trees:
        if t != WORK:
            b = birth(t)
            owner = [p for p, s, _a in procs if s - 1 <= b <= s + LIVE_S]
            assert not owner, "reclaim: %s belongs to the running process %s" % (t, owner)
    tokens = report_tokens()
    lengths = sorted({len(t) for t in tokens})
    before = sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    out("reclaim: %d report tokens; forensic store holds %d files" % (len(tokens), before))
    considered = named = kept = copied = held = 0
    for tree in trees:
        if tree == WORK and os.path.isdir(WT):
            pristine(WT)
        for dirpath, dirnames, filenames in os.walk(tree):
            dirnames[:] = sorted(d for d in dirnames if os.path.join(dirpath, d) != WT)
            for name in sorted(filenames):
                path = os.path.join(dirpath, name)
                if os.path.islink(path) or not os.path.isfile(path):
                    continue
                considered += 1
                rel = os.path.relpath(path, tree)
                h = tz23.sha256_file(path)
                is_named = any(h[:k] in tokens for k in lengths)
                is_kept = by_name(tree, rel)
                if not (is_named or is_kept):
                    continue
                named += 1 if is_named else 0
                kept += 1 if is_kept and not is_named else 0
                dest = os.path.join(FORENSICS, os.path.basename(tree) + "--" + rel.replace("/", "--"))
                if os.path.exists(dest):
                    got = tz23.sha256_file(dest)
                    assert got == h, "reclaim: %s exists with sha256 %s, source %s" % (dest, got, h)
                    held += 1
                    out("R held   %s %s" % (h, dest))
                    continue
                with open(path, "rb") as src, open(dest, "xb") as dst:
                    shutil.copyfileobj(src, dst, 1 << 20)
                assert tz23.sha256_file(dest) == h, "reclaim: %s did not copy whole" % dest
                copied += 1
                out("R copied %s %s" % (h, dest))
    after = sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    assert after == before + copied, "reclaim: store %d, expected %d" % (after, before + copied)
    out("RECLAIM PASS: %d files considered, %d named by a report, %d kept by name, %d copied, %d already held; "
        "forensic store %d -> %d files" % (considered, named, kept, copied, held, before, after))

# ---- the self-test: literals and temporary trees under the work tree -----------------------------------------


def pnl_by_row(role, rows, won_up):
    """The self-test's own arithmetic, written apart from TZ-23's: one row's money at settlement, its rebate or its
    fee taken at the row - BUY a token at p pays s (won - p), SELL pays s (p - won) - summed."""
    tot = D(0)
    for r in rows:
        side, outcome, s, p = r[1], r[2], D(r[3]), D(r[4])
        won = won_up if outcome == "U" else 1 - won_up
        money = s * (won - p) if side == "B" else s * (p - won)
        fee = D("0.07") * s * p * (1 - p)
        tot += money + (fee * D("0.2") if role == "maker" else -fee)
    return tot


def mode_selftest():
    import random
    n = [0]

    def ok(cond, what):
        assert cond, "selftest: " + what
        n[0] += 1
        out("  ok  " + what)

    # TZ-23's file, as loaded, and the constants this file takes from it
    ok(tz23.__file__ == os.path.join(HERE, TZ23_NAME) and sys.modules["tz23"] is tz23,
       "TZ-23's instrument loaded from beside this file, from its asserted bytes")
    ok(tz23.MALLOC_TUNED, "glibc took the 128 KiB mmap threshold and the two arenas")
    ok(tz23.getcontext().prec == 60, "the main thread sums at 60 digits")
    ok((tz23.STEP, tz23.CHUNK, tz23.RESOLVED_AFTER_S, tz23.WALK_SLACK, tz23.FETCH_WORKERS) == (300, 20, 3900, 2016, 2),
       "TZ-23's step, document chunk, resolution age, slack and workers")
    ok(DELTA == D("0.005") and REBATE_RATE == D("0.2") and tz23.REBATE_COEF == D("0.014") and
       tz23.FEE_SCHEDULE == {"exponent": 1, "rate": D("0.07"), "takerOnly": True, "rebateRate": D("0.2")},
       "half a tick a share; the fee 0.07 s p (1 - p), the rebate a fifth of it, as the documents must state")
    ok(tz23.HEADERS == {"User-Agent": "btc-5m-twap-m0/TZ-23", "Accept": "application/json"},
       "every request carries TZ-23's two headers")
    ok(tz23.BANDS[0] == ("pre", None, 0) and tz23.BANDS[-2] == ("last", 240, 300) and
       tz23.BANDS[-1] == ("post", 300, None) and LIFE_BANDS == tuple(b for b in BAND_NAMES if b != "post"),
       "a market's life is every fill before T0 + 300: TZ-23's bands but post")
    # the set: its start, its instant and its walk
    ok(START == 1792451700 and utc(START) == "2026-10-19T23:15:00Z" and START == M0_LAST + 300,
       "the walk starts at 2026-10-19 23:15 UTC, the market after M0's last")
    ok(START_AT == START + (N_SET - 1) * tz23.STEP + tz23.RESOLVED_AFTER_S and utc(START_AT) == SET_INSTANT,
       "no set is read before %s, the last member's resolution age if every candidate qualifies" % SET_INSTANT)
    ok(tz23.next_open(START, tz23.EXCLUDED) == START and not tz23.excluded(START, tz23.EXCLUDED),
       "no excluded span reaches the set")
    ok(FORMATION[1] == M0_LAST and (FORMATION[1] - FORMATION[0]) // 300 + 1 == 864 and
       REHEARSAL[0] + (REHEARSAL[1] - 1) * 300 == M0_LAST,
       "the formation is M0's last 864 markets and the rehearsal its last 144")
    good = {"slug": "", "outcomes": '["Up", "Down"]', "outcomePrices": '["1", "0"]', "closed": True,
            "feeType": tz23.FEE_TYPE, "feeSchedule": dict(tz23.FEE_SCHEDULE), "eventStartTime": "",
            "conditionId": "0x" + "cd" * 32, "clobTokenIds": '["11", "22"]'}

    def fake_docs(t0s, asked=None):
        if asked is not None:
            asked.extend(t0s)
        return {"btc-updown-5m-%d" % t: dict(good, slug="btc-updown-5m-%d" % t, eventStartTime=tz23.iso(t))
                for t in t0s}

    asked = []
    cons, mem = tz23.candidates(START, tz23.EXCLUDED, 50, lambda ts: fake_docs(ts, asked))
    ok(len(mem) == 50 and mem[0][0] == START and mem[-1][0] == START + 49 * 300 and len(cons) == 50 and
       asked == [t for t, _st in cons] and min(asked) > M0_LAST,
       "TZ-23's walk from 1792451700 takes 50 members in 50 documents and requests none at or below M0's last")
    ok(len(fill_groups_of({"members": [{"t0": START + 300 * i, "doc": good} for i in range(N_SET)]})) ==
       -(-N_SET // FILL_CHUNK), "the set's members are %d chunks of fills" % -(-N_SET // FILL_CHUNK))
    # the groups, as named
    ok(all(WALLET.fullmatch(w) for g in GROUP_ORDER for w in GROUPS[g]["wallets"]) and
       all(len(set(GROUPS[g]["wallets"])) == len(GROUPS[g]["wallets"]) == GROUP_SIZE for g in GROUP_ORDER) and
       [(GROUPS[g]["role"], GROUPS[g]["gated"]) for g in GROUP_ORDER] == [("maker", True), ("taker", False)],
       "each group names %d distinct wallets: the makers' rows, gated; the takers', barred" % GROUP_SIZE)
    # the feeds: the makers' rows are the full feed less the takers'
    T = 1792500000
    tk = [[T + 10, "B", "U", "10", "0.6", "11", "0xaa", "0x" + "1" * 40]]
    mk = [[T + 10, "S", "U", "4", "0.6", "11", "0xaa", "0x" + "2" * 40],
          [T + 10, "B", "D", "6", "0.4", "22", "0xaa", "0x" + "3" * 40]]
    maker = split_feeds(mk + tk + [list(mk[0])], tk)
    diag = feed_check(tk, maker)
    ok(sorted(maker) == sorted(mk + [list(mk[0])]) and diag == {"transactions": 1, "sizes_differ": 1,
                                                               "one_side_only": 0},
       "the makers' rows are the full feed less the takers', as multisets; a transaction whose sizes differ counted")
    maker = split_feeds(mk + tk, tk)
    ok(sorted(maker) == sorted(mk) and feed_check(tk, maker)["sizes_differ"] == 0 and
       feed_check(tk, [])["one_side_only"] == 1, "sizes 4 + 6 against 10 are equal; a transaction with the takers' "
                                                  "rows alone is counted")
    try:
        split_feeds(mk, tk)
        caught = False
    except AssertionError:
        caught = True
    ok(caught, "a takers' row absent from the full feed is a failed assert")
    # a wallet's own position: TZ-23's maker_terms on the flipped side, against this file's own row arithmetic
    rows = [[T, "B", "U", "10", "0.6"], [T, "S", "U", "3", "0.7"], [T, "B", "D", "5", "0.25"],
            [T, "S", "D", "2", "0.9"]]
    b, _w = tz23.aggregate(T - 60, own_rows(rows))
    lf = life_of(b)
    ok(lf["X"] == D(10) - 3 - 5 + 2 and lf["C"] == D("6") - D("2.1") - D("3.75") + D("0.2") and
       lf["sh"] == D(20) and lf["n"] == 4, "own rows: BUY Up +s at p, SELL Up -s at p, BUY Down -s at 1 - p, SELL "
                                          "Down +s at 1 - p")
    for up in (0, 1):
        for role in ("maker", "taker"):
            ok(lf["X"] * up - lf["C"] + extra_of(role, lf["R"]) == pnl_by_row(role, rows, up),
               "%s, Up %d: X up - C plus the rebate or less the fee equals the row-by-row money" % (role, up))
    late = rows + [[T - 60 + 300, "B", "U", "100", "0.99"]]
    b2, _w = tz23.aggregate(T - 60, own_rows(late))
    ok(life_of(b2) == lf and b2["post"]["n"] == 1, "a fill at T0 + 300 is post: outside every life sum")
    # a synthetic set, built, scored, against the row-by-row arithmetic; label-free; deterministic
    tmp = os.path.join(WORK, "selftest-tmp")
    shutil.rmtree(tmp, ignore_errors=True)
    saved = {g: dict(GROUPS[g]) for g in GROUP_ORDER}
    try:
        os.makedirs(tmp)
        rng = random.Random(31)
        wallets = ["0x%040x" % (i + 1) for i in range(8)]
        GROUPS["makers"] = dict(saved["makers"], wallets=tuple(wallets[:3]))
        GROUPS["takers"] = dict(saved["takers"], wallets=tuple(wallets[2:5]))
        t0s = [START + 300 * i for i in range(23)]
        docs = [dict(good, slug="btc-updown-5m-%d" % t, eventStartTime=tz23.iso(t),
                     conditionId="0x%064x" % (i + 1), outcomePrices=('["1", "0"]' if rng.random() < 0.5 else
                                                                     '["0", "1"]')) for i, t in enumerate(t0s)]

        def synth_rows(t):
            def one():
                return [t + rng.randrange(-60, 330), rng.choice("BS"), rng.choice("UD"),
                        tz23.fx(D(rng.randrange(1, 50000)) / 100), tz23.fx(D(rng.randrange(1, 999)) / 1000),
                        rng.choice(["11", "22"]), "0x%064x" % rng.randrange(1, 10 ** 6), rng.choice(wallets)]
            return sorted(one() for _ in range(rng.randrange(0, 30))), sorted(one() for _ in range(rng.randrange(0, 30)))

        synth = {t: synth_rows(t) for t in t0s}

        def build(base, dd, label):
            cache = os.path.join(base, "cache")
            os.makedirs(cache)
            st = {"start": START, "need": len(dd), "considered": [[int(d["slug"].rsplit("-", 1)[1]), "member"]
                                                                  for d in dd],
                  "members": [{"t0": int(d["slug"].rsplit("-", 1)[1]), "doc": tz23.kept_doc(d)} for d in dd]}
            groups = fill_groups_of(st)
            for g in groups:
                tz23.write_atomic(tz23.chunk_path(cache, g[0][0]), tz23.gz_bytes(dumps({"members": [
                    {"t0": t, "condition": d["conditionId"], "taker": synth[t][0], "maker": synth[t][1]}
                    for t, d in g]})))
            const, paths = build_constants2(base, st, cache, groups, label)
            return st, const, paths

        sa, ca, pa = build(os.path.join(tmp, "a"), docs, "x")
        ra = score2(os.path.join(tmp, "a"), sa, ca, "x")
        for g, role, side in (("makers", "maker", 1), ("takers", "taker", 0)):
            want = post = D(0)
            for t, d in zip(t0s, docs):
                up = tz23.label_of(d)
                mine = [r for r in synth[t][side] if r[7] in GROUPS[g]["wallets"]]
                want += pnl_by_row(role, [r for r in mine if r[0] < t + 300], up)
                post += pnl_by_row(role, [r for r in mine if r[0] >= t + 300], up)
            ok(ra["groups"][g]["S"] == want and want != 0,
               "%s: S over the synthetic set equals the row-by-row money of every fill before T0 + 300" % g)
            wsum = sum((v["S"] for v in ra["groups"][g]["barred_wallets"].values()), D(0))
            ok(wsum == want and post != 0 and
               sum((v["S"] for v in ra["groups"][g]["barred_bands"].values()), D(0)) == want + post,
               "%s: the wallets' sums add to S, and the bands' to S with post beside it" % g)
        flip = [dict(d, outcomePrices=('["0", "1"]' if d["outcomePrices"] == '["1", "0"]' else '["1", "0"]'))
                for d in docs]
        sb, cb, pb = build(os.path.join(tmp, "b"), flip, "x")
        ok(pb["constants.json"][1] == pa["constants.json"][1] and all(
            pb[k][1] == pa[k][1] for k in pa), "every constants file is byte-identical with every label flipped")
        rb = score2(os.path.join(tmp, "b"), sb, cb, "x")
        ok(rb["groups"]["makers"]["S"] != ra["groups"]["makers"]["S"], "the score moves when the labels flip "
                                                                       "(negative control)")
        again = build_constants2(os.path.join(tmp, "a"), sa, os.path.join(tmp, "a", "cache"), fill_groups_of(sa), "x")
        ok(again[1] == pa, "a second constants run finds every file unchanged")
        # the readings: TZ-23's table, TZ-23's reading, on this TZ's lambda
        c = tz23.gate_constants(D(10 ** 10), D(10 ** 9), lam=GROUPS["makers"]["lambda"], alpha=ALPHA, delta=DELTA)
        th = {"earn_at": c["earn_at"], "no_earn_at": c["no_earn_at"]}
        ok(c["earn_at"] == c["thr"] and c["no_earn_at"] == DELTA * D(10 ** 9) - c["thr"] and c["thr"] < c["no_earn_at"]
           and [WORDS[tz23.reading(x, th)[0]] for x in (c["thr"] - 1, c["thr"], c["no_earn_at"] + 1)] ==
           ["W-NO-EARN", "W-EARN", "W-EARN"] and tz23.reading(c["thr"], th)[1:] == (True, True),
           "W-EARN at S >= thr, W-NO-EARN at S <= delta Sh - thr, W-EARN first where both hold")
        c2 = tz23.gate_constants(D(10 ** 14), D(10 ** 8), lam=GROUPS["makers"]["lambda"], alpha=ALPHA, delta=DELTA)
        th2 = {"earn_at": c2["earn_at"], "no_earn_at": c2["no_earn_at"]}
        ok(c2["no_earn_at"] < c2["thr"] and [WORDS[tz23.reading(x, th2)[0]] for x in (
            c2["no_earn_at"], c2["no_earn_at"] + 1, c2["thr"] - 1, c2["thr"])] ==
           ["W-NO-EARN", "UNDECIDABLE", "UNDECIDABLE", "W-EARN"], "UNDECIDABLE between the bounds where they part")
    finally:
        for g in GROUP_ORDER:
            GROUPS[g] = saved[g]
        shutil.rmtree(tmp, ignore_errors=True)
    # the projection: each group's V and Sh at the set's size, at the formation's rates, against the Architect's
    # independent figures
    for g in GROUP_ORDER:
        vf, sf, want = PROJ[g]
        c = tz23.gate_constants(vf * N_SET / 864, sf * N_SET / 864, lam=GROUPS[g]["lambda"], alpha=ALPHA, delta=DELTA)
        ok(abs(c["thr"] - want["thr"]) < D("1e-20") and want["power"][0] < c["power"] < want["power"][1],
           "%s: at the projected V and Sh the threshold is %s and the power between %s and %s, the Architect's" % (
               g, fx(want["thr"]), want["power"][0], want["power"][1]))
    # G-REHEARSAL's comparison
    got = {"members": REF["members"], "ups": REF["ups"],
           "groups": {g: dict(REF["groups"][g]) for g in GROUP_ORDER}}
    ok(all(eq for _n, eq in compare_ref(got)) and len(compare_ref(got)) == 2 + 8 * len(GROUP_ORDER),
       "the rehearsal's %d figures compare equal to themselves" % (2 + 8 * len(GROUP_ORDER)))
    got["groups"]["takers"]["S"] += D("1e-30")
    ok([nm for nm, eq in compare_ref(got) if not eq] == ["takers S"], "one figure off by 1e-30 fails alone")
    # the clock: the idle stretch, the archive's calendar run and its service
    W = 1792458000
    idle = lambda st="inactive": (lambda: st)
    ok(quiet(W + 14, CHUNK_BUDGET_S, idle()) is not None and quiet(W + 15, CHUNK_BUDGET_S, idle()) is None and
       quiet(W + 470, CHUNK_BUDGET_S, idle()) is None and quiet(W + 471, CHUNK_BUDGET_S, idle()) is not None,
       "a chunk starts from second 15 to 470 of a window and at no other second")
    ok(quiet(W + 600, CHUNK_BUDGET_S, idle()) is not None and quiet(W + 899, CHUNK_BUDGET_S, idle()) is not None,
       "nothing starts while the pair book streams, seconds 595 to 905")
    cal = W // 86400 * 86400 + ARCHIVE_CALENDAR_S
    ok(quiet(cal - 5, CHUNK_BUDGET_S, idle()) is not None and quiet(cal + 40, CHUNK_BUDGET_S, idle()) is not None
       and quiet(cal + 61, CHUNK_BUDGET_S, idle()) is None,
       "nothing starts from 03:00:15 to 03:01:20 UTC; at 03:01:21 a chunk may start")
    ok(all(quiet(W + 100, CHUNK_BUDGET_S, idle(st)) is not None for st in RUNNING) and
       quiet(W + 100, CHUNK_BUDGET_S, idle("failed")) is None,
       "nothing starts while the archive's service runs; a failed one does not hold")
    clock = [W + 600.25]
    t, waited = hold(CHUNK_BUDGET_S, clock=lambda: clock[0], sleep=lambda s: clock.__setitem__(0, clock[0] + s),
                     state_of=idle())
    ok(int(t) % WINDOW_S == 15 and int(t) == W + 900 + 15 and 314 <= waited <= 320,
       "held from second 600, a chunk starts at second 15 of the next window")
    clock = [W + 100.0]
    try:
        hold(CHUNK_BUDGET_S, clock=lambda: clock[0], sleep=lambda s: clock.__setitem__(0, clock[0] + s),
             state_of=idle("activating"))
        stuck = False
    except AssertionError as e:
        stuck = "BLOCKED: held" in str(e) and clock[0] - (W + 100) <= HOLD_MAX_S + 5
    ok(stuck, "an archive's run that never ends holds a chunk 7,200 s and then stops it BLOCKED")
    # the walk again, 300 s later, on a market too recent to be resolved; any other stop is final
    calls, slept = [], []

    def form_stops(times, msg):
        def form(base, start, spans, need):
            calls.append(start)
            if len(calls) <= times:
                raise AssertionError(msg)
            return {"start": start}
        return form

    r = walk("/nonexistent", START, (), N_SET, form=form_stops(2, "BLOCKED: the walk reached x, too recent to be "
                                                                   "resolved"),
             holdf=lambda b: (0, 0), sleep=slept.append)
    ok(r == {"start": START} and len(calls) == 3 and slept == [WALK_RETRY_S, WALK_RETRY_S],
       "a walk stopped twice on a market too recent is walked a third time, 300 s after each stop")
    calls.clear()
    try:
        walk("/nonexistent", START, (), N_SET, form=form_stops(1, "BLOCKED: 3025 considered for 1007 members"),
             holdf=lambda b: (0, 0), sleep=slept.append)
        stopped = False
    except AssertionError:
        stopped = True
    ok(stopped and len(calls) == 1, "a walk stopped on its slack is not walked again")
    # the fetch, held, on a fake chunk fetcher: each fresh chunk timed, a cached chunk fetched again by nothing
    tmp = os.path.join(WORK, "selftest-tmp")
    shutil.rmtree(tmp, ignore_errors=True)
    try:
        os.makedirs(tmp)
        s = {"members": [{"t0": START + 300 * i, "doc": dict(good, conditionId="0x%064x" % (i + 1))}
                         for i in range(14)]}
        fetched = []

        def fake_fetch(cache, group):
            fetched.append(group[0][0])
            path = tz23.chunk_path(cache, group[0][0])
            tz23.write_atomic(path, tz23.gz_bytes(dumps({"members": [
                {"t0": t, "condition": d["conditionId"], "taker": [], "maker": []} for t, d in group]})))
            return path, True

        timing = os.path.join(tmp, "timing.jsonl")
        clk = [float(W + 20)]
        cache, groups = fetch_held(tmp, s, timing, fetcher=fake_fetch, holdf=lambda b: (clk[0], 0.0),
                                   clock=lambda: clk[0])
        recs, outside = timing_summary(timing)
        span, n14 = FILL_CHUNK * 300, -(-14 // FILL_CHUNK)
        ok(len(groups) == n14 and sorted(fetched) == [START + span * k for k in range(n14)] and len(recs) == n14
           and [len(g) for g in groups] == [FILL_CHUNK] * (n14 - 1) + [14 - FILL_CHUNK * (n14 - 1)] and not outside,
           "14 members are %d chunks of at most %d, each fetched once and timed inside the idle stretch" % (
               n14, FILL_CHUNK))
        fetched.clear()
        fetch_held(tmp, s, timing, fetcher=fake_fetch, holdf=lambda b: (clk[0], 0.0), clock=lambda: clk[0])
        ok(fetched == [] and len(timing_summary(timing)[0]) == n14, "a cached chunk is fetched again by nothing")
        ok(sum(1 for _ in member_rows2(cache, groups)) == 14, "every chunk reads back to its members")
        big = {"members": [{"t0": START + 300 * i, "doc": dict(good, conditionId="0x%064x" % (i + 1))}
                           for i in range(200)]}
        nbig = -(-200 // FILL_CHUNK)

        import threading
        gate = threading.Event()

        def slow_fetch(step, held_from=None):
            def f(cache, group):
                if held_from is not None and (group[0][0] - START) // span >= held_from:
                    gate.wait(30)
                clk[0] += step
                return fake_fetch(cache, group)
            return f

        fetched.clear()
        threading.Timer(5.0, gate.set).start()
        try:
            fetch_held(os.path.join(tmp, "slow"), big, os.path.join(tmp, "slow.jsonl"),
                       fetcher=slow_fetch(1000.0, held_from=32), holdf=lambda b: (clk[0], 0.0), clock=lambda: clk[0])
            blocked = False
        except AssertionError as e:
            blocked = "BLOCKED: fetching projected" in str(e)
        ok(blocked and 32 <= len(fetched) <= 34, "a fetch projected above 7,200 s of fetching stops BLOCKED at its "
                                                  "30th chunk: at most the two chunks running end, and the %d "
                                                  "queued never start" % (nbig - 34))
        fetched.clear()
        fetch_held(os.path.join(tmp, "fast"), big, os.path.join(tmp, "fast.jsonl"), fetcher=slow_fetch(10.0),
                   holdf=lambda b: (clk[0], 0.0), clock=lambda: clk[0])
        ok(len(fetched) == nbig, "a fetch projected under it fetches all %d chunks" % nbig)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    # the archive's ledger, summarized from literal records
    recs = [{"event": "start", "run": 1792378820, "wall_ns": 1}, {"event": "set", "run": 1792378820, "wall_ns": 2,
            "tag": "pairbook-streams-1792378820", "assets_n": 96, "bytes_total": 10, "first_T": 1792291500,
            "last_T": 1792377000, "windows_considered": 96}, {"event": "complete", "run": 1792378820, "wall_ns": 3,
            "requests": 1, "started_outside": 0, "ended_outside": 0, "store_stream_bytes": 0, "free_bytes": 1,
            "rate_per_day": 1}, {"event": "start", "run": 1792045110, "wall_ns": 4},
            {"event": "set", "run": 1792045110, "wall_ns": 5, "tag": "pairbook-streams-1792045110", "assets_n": 1,
             "bytes_total": 1, "first_T": 1792378800, "last_T": 1792378800, "windows_considered": 1},
            {"event": "halt", "run": 1792045110, "wall_ns": 6, "phase": "restart", "reason": "x"}]
    summ = ledger_summary(recs)
    ok(summ["runs"] == [1792378820, 1792045110] and "calendar" in summ["lines"][0] and
       "off-calendar, second 22710" in summ["lines"][1] and summ["halted"] and
       summ["terminal"] == {1792378820: ["complete"], 1792045110: ["halt"]} and summ["assets"] == 97 and
       summ["gaps"] == [[1792377000, 1792378800]], "the ledger's runs, terminals, calendar, halt and gaps")
    ok(not ledger_summary(recs + [{"event": "clear", "run": None, "wall_ns": 7}])["halted"],
       "a clear after a halt reads not halted")
    # G-STILL: unchanged, or the pair book's change the archive's own restarts alone
    u0 = {"recorder": {"MainPID": "4148534", "NRestarts": "2", "ActiveState": "active"},
          "pairbook": {"MainPID": "2221487", "NRestarts": "19", "ActiveState": "active"}}
    u2 = {"recorder": dict(u0["recorder"]), "pairbook": {"MainPID": "30", "NRestarts": "21", "ActiveState": "active"}}
    chain = [{"event": "restart", "stopped": 2221487, "pid": 20, "NRestarts": "20"},
             {"event": "restart", "stopped": 20, "pid": 30, "NRestarts": "21"}]
    ok(still_reading(u0, json.loads(json.dumps(u0)), []) == (True, "unchanged") and
       still_reading(u0, u2, chain)[0] and not still_reading(u0, u2, chain[:1])[0] and
       not still_reading(u0, u2, chain[::-1])[0] and not still_reading(u0, u2, [])[0] and
       not still_reading(u0, dict(u2, recorder=dict(u0["recorder"], MainPID="1")), chain)[0],
       "G-STILL: unchanged, or the pair book moved by a chain of the archive's restart records, each one NRestarts "
       "higher; a broken, reversed or missing chain or a changed recorder fails")
    # the fingerprint's rows, on literal lines
    lines = ("| `research/tz23-maker-m0.py` | 1,184 | 54,885 | frozen | `%s` |\n"
             "| `SYSTEM-MAP.md` | — | — | reported | self-reference; report the value you compute |\n"
             "| `A6` — pricer | `729f0bcdbee3` |\n" % TZ23_SHA256)
    ok(ROW.findall(lines) == [("research/tz23-maker-m0.py", "1,184", "54,885", "frozen", TZ23_SHA256),
                              ("SYSTEM-MAP.md", "—", "—", "reported",
                               "self-reference; report the value you compute")] and
       dict(ANCHOR_ROW.findall(lines)) == {"A6": "729f0bcdbee3"}, "the map's rows and anchors parse")
    # reclaim's paths
    ok(reclaimable(WORK) and not reclaimable(FORENSICS) and not reclaimable("/tmp/x/" + "0" * 8 + "-0000-0000-0000-"
                                                                           + "0" * 12),
       "reclaim takes the work tree and refuses the forensic store and a directory outside a session's")
    # the audit hook: section 2's refusals happen before the open
    MODE[0] = "selftest"
    refused = []
    for p in ("/var/lib/btc-pairbook/runtime.jsonl", ARCHIVE_LEDGER, "/var/lib/btc-chainbook/runtime.jsonl"):
        try:
            open(p, "rb")
            refused.append("opened")
        except GuardError:
            refused.append("tz31")
        except RuntimeError:
            refused.append("tz23")
        except OSError:
            refused.append("not refused")
    ok(refused == ["tz31", "tz31", "tz23"], "opens under the pair book's root and of the archive's ledger outside "
                                            "modes archive and still are refused by this hook, under the chain "
                                            "book's root by TZ-23's, each before it happens")
    try:
        open("/var/lib/btc-recorder/runtime.jsonl", "rb")
        rec_refused = False
    except RuntimeError:
        rec_refused = True
    except OSError:
        rec_refused = False
    ok(rec_refused and tz23.OPENS[-1] == "/var/lib/btc-recorder/runtime.jsonl",
       "TZ-23's own hook still refuses the recorder's root")
    tz23.OPENS.clear()
    ok(policy("archive", "open", (ARCHIVE_LEDGER, "rb", 0)) is None and
       policy("still", "open", (ARCHIVE_LEDGER, "rb", 0)) is None and
       policy("score", "open", (ARCHIVE_LEDGER, "rb", 0)) is not None and
       policy("archive", "open", (ARCHIVE_LEDGER, "ab", os.O_WRONLY)) is not None and
       policy("archive", "open", (ARCHIVE_STATE + "/archive.log", "rb", 0)) is not None and
       policy("archive", "os.listdir", (ARCHIVE_STATE,)) is not None,
       "modes archive and still read ledger.jsonl and nothing else of the archive's state, and write nothing there; "
       "no other mode reads it")
    ok(policy("reclaim", "open", (FORENSICS + "/x", "xb", 0)) is None and
       policy("reclaim", "open", (FORENSICS + "/x", "wb", 0)) is not None and
       policy("score", "open", (FORENSICS + "/x", "xb", 0)) is not None and
       policy("score", "open", ("/root/elsewhere", "wb", 0)) is not None and
       policy("score", "open", (FORENSICS + "/x", "rb", 0)) is None,
       "the forensic store is written by reclaim's exclusive create alone, and nothing outside the work tree")
    del REFUSED[:]
    out("%d of %d checks passed" % (n[0], n[0]))


def main(argv):
    if not argv:
        sys.exit("usage: tz31-who-earns.py MODE [ARG...]")
    mode, rest = argv[0], argv[1:]
    assert os.getcwd() == WORK, "run from %s, not %s" % (WORK, os.getcwd())
    MODE[0] = mode
    table = {"fingerprint": mode_fingerprint, "selftest": mode_selftest, "still": mode_still,
             "archive": mode_archive, "rehearse": mode_rehearse, "fetch": mode_fetch,
             "constants": mode_constants, "score": mode_score}
    if mode == "reclaim":
        mode_reclaim(rest)
    elif mode == "scratch":
        assert len(rest) == 1, "scratch OWN"
        mode_scratch(rest[0])
    else:
        assert mode in table and not rest, "unknown mode %r" % (argv,)
        table[mode]()
    out("malloc tuned: %s" % tz23.MALLOC_TUNED)
    out("peak memory of this run: %d bytes" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024))
    out("opens refused: %d; under the recorder's and the chain book's roots by TZ-23's hook: %d" % (
        len(REFUSED), len(tz23.OPENS)))


if __name__ == "__main__":
    main(sys.argv[1:])
```
