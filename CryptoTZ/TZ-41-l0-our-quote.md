# TZ-41 — L0, our quote on the venue's reward markets: does a two-sided quote of ours, alone one tick inside a wide touch, simulated on the reward book's streams, collect more in liquidity rewards and maker rebates than its fills lose?

**Canonical filename:** `TZ-41-l0-our-quote.md`. The committed file takes this name and no other.

**Executor model: Claude Opus 5.5.** A replay at venue time of stored streams, a reward formula's arithmetic, the first read of a reserved store, and a gate's reading.

**Required System Map revision:** `2026-11-01-b`.

**Map sections this TZ rests on**, copied from §10's C8 (map §7 item 141): §0, the fingerprint gate and its table; §1, the refs; §2.5, the pair book's idle stretch and its archive's calendar run and restarts; §2.6, the reward book — its store, its slot records, its archive's runs, sets and assets, `STREAM_FLOOR` and the reserve; §3, the forensic store, the worktrees, the directories TZ-40's session left and the code trees kept; §6, its rows host identity, language, git remote, egress, venue edge, disk, process supervision, memory, both sandbox limits and the harness; §7 items 115, 118 to 121, 123 to 125, 129, 131, 132, 136 to 141 and 143 to 146.

**Required anchors**, from map §0. A mismatch on any one is BLOCKED before any work:

| anchor | required |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `0f6c90451cbd` |
| `A6` — pricer | `729f0bcdbee3` |

**Host gate:** §0.3. This TZ runs on the capture host for its interpreter, its network, the reward book's store, both archives' ledgers and the forensic store; **it reads no stream stored on the host** — every stream it replays is a Release asset the reward book's archive made.

**Before `EXECUTE TZ-41`:** the Boss uploads this file alone, into `CryptoTZ/`. `main` already carries map revision `2026-11-01-b` (`a1c7ba1`) and PR #40's merge (`494f10f`); nothing else is needed, and no step of the Boss's is a precondition of the run (map §7 item 132).

**When: from 2026-11-08 07:30:00 UTC, epoch `1794123000`, on any day, at 07:30:00 to 21:00:00 UTC.** §0.0 reads the clock before anything else and, outside that band, begins nothing. The set's eighth candidate day, 2026-11-07, ends at 2026-11-08 00:00 UTC, and the reward book's archive moves it at its calendar run of 01:30:20 UTC (map §2.6). 07:30 is clear of the package manager's morning run (map §7 item 143), and a run begun by 21:00 ends before the next one, its bounds reached included (§6), so that no capture unit is restarted by it while G-STILL watches (map §7 item 120). Both archives' calendar runs, 01:30:20 and 03:00:20 UTC, are held by the instrument itself (§1). About 2 h 30 min of wall clock (§6).

**What this TZ is.** The L track's first step, L0 (CANON PART II). The W track closed on a quote at the touch whose fills were adversely selected and paid by nothing but the rebate (TZ-32). The venue pays makers on other markets a second way — a daily pool per market, shared by a score of the book each maker keeps near the midpoint (CANON §1.7) — and since 2026-10-28 the reward book has captured the books, trades and reward records of 150 such markets a day, chosen by TZ-33's rule before their data, ending 14 days or more after each day and with no live event near it, their streams moved to Releases every day since 2026-10-29 (map §2.6). **This TZ fixes one quoting rule** (§1): on each market, a bid one tick above the best bid and an ask one tick below the best ask wherever the touch is five ticks wide or more, each of the market's minimum size and inside its maximum spread, alone at its price, a position of at most one minimum size either way. It replays that rule, label-free, on **the first 8 qualifying days from 2026-10-31** — days no one has read — at venue time: every member's book rebuilt from every stored frame and checked against the venue's own book frames, every order arriving 50 ms after the host decides it, refused where it would cross, filled only by matches the venue printed or by orders that came to its price, its reward share computed by the venue's published formula against the competitors the book and the venue's own figure allow, its rebate by the venue's published schedule, and its position marked at each day's end. It reads L0 once, on each day's money as one block: **EARN** where the variant that makes every unmeasurable assumption against us reaches 10 USDC on every day, **NO EARN** where the variant that makes every one for us stays below it on every day, **UNDECIDABLE** otherwise, each answer's false-reading probability `2⁻⁸`, under `0.005`. The instrument, `research/tz41-l0-our-quote.py` (Appendix A), is the whole of that arithmetic — the standard library alone.

---

## 0. Gates

### 0.0 The instant, then the work tree

After contract §1 steps 1 and 2, and before anything else, in the session:

```
t=$(date -u +%s); s=$(( t % 86400 )); echo "now $t $(date -u -d @$t +%FT%TZ), second of the day $s"; [ "$t" -ge 1794123000 ] && [ "$s" -ge 27000 ] && [ "$s" -le 75600 ]; echo "inside=$?"
```

**`inside=0` begins the run. Anything else begins nothing:** no directory is made, nothing is written, committed or pushed and no report is written — this TZ has not executed (CANON hard rule 5) — and the Executor tells the Boss in one line, in Russian, the next instant the band opens — a 07:30 UTC no earlier than 2026-11-08 — and stops. This is not BLOCKED and owes no report: nothing has begun (contract §5), and a later `EXECUTE TZ-41` inside the band starts the TZ afresh. Then:

```
mkdir /root/tz41-work /root/tz41-work/logs; echo "exit=$?"
```

`exit=0` proves neither existed; anything else is BLOCKED. The clock line is run again into `logs/00-instant.log`. **From here every command's output goes to `/root/tz41-work/logs/`, one file per step, under the names §3's table fixes**, and nothing to the session's scratchpad. The one exception is B-RECLAIM-OWN, §9, which removes the directory the logs are in.

Three abbreviations: **`P`** is `nice -n 19 /root/tz04a-env/venv/bin/python -B`; **`I0`** is `P /root/tz41-work/stage/research/tz41-l0-our-quote.py`, the staged copy, for §0 alone; and **`I`**, from §3.1 on, is `P /root/tz41-work/wt/research/tz41-l0-our-quote.py`, the committed copy. Every mode runs from `/root/tz41-work` — each asserts that its current directory is the work tree (line 2528). **In every block that removes, both are written out in full**, because the Boss may be handed the block (map §6, sandbox limit — destructive actions).

### 0.1 The instrument, staged

Extract Appendix A from this TZ as the primary checkout carries it after contract §1's pull, with this script, verbatim, its one argument the destination, its output into `logs/01-stage.log`:

```
/root/tz04a-env/venv/bin/python -B - /root/tz41-work/stage <<'EOF2'
import hashlib, os, sys
SRC = "/root/btc-5m-twap/CryptoTZ/TZ-41-l0-our-quote.md"
DEST = sys.argv[1]
WANT = {
    "research/tz41-l0-our-quote.py": "e4867068a5d1620d5deab981f68c1ae60b97d364ab00f31895a8e402d479ce16",
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
EOF2
```

| path | lines | bytes | SHA-256 |
|---|---|---|---|
| `research/tz41-l0-our-quote.py` | 3,054 | 152,763 | `e4867068a5d1620d5deab981f68c1ae60b97d364ab00f31895a8e402d479ce16` |

A failed assert or another hash is BLOCKED. The staged copy runs §0.2's `fingerprint` and §0.5's `number` alone.

### 0.2 Fingerprint

`I0 fingerprint`, into `logs/02-fingerprint.log`, performs contract §1 steps 3 and 4 inside the instrument and asserts them, against `SYSTEM-MAP.md` and the files of its §0 table in the primary checkout `/root/btc-5m-twap`: revision `2026-11-01-b`; the six anchors; `A2`, `A4`, `A5` and `A6` re-derived as the first 12 hex characters of those files' SHA-256; the table's **60** rows, each printed in lines, bytes and SHA-256 — **57** `frozen` rows asserted equal to the map, **2** `tracked` and **1** `reported`; and the map's own lines, bytes and SHA-256 (lines 2253 to 2280). It prints `FINGERPRINT PASS` or stops at the first mismatch, which is BLOCKED.

### 0.3 Host gate

From `/root/btc-5m-twap`, with `S` first set to the scratchpad directory the session's system prompt names, output verbatim into `logs/03-host-gate.log`:

```
date -u; date -u +%s; uptime -s; journalctl --list-boots --no-pager | tail -n 3
nproc; grep -E '^(MemTotal|MemAvailable|SwapTotal|SwapFree):' /proc/meminfo
df -B1 --output=source,size,avail /var/lib/btc-recorder
find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
grep -c e3975b5da44c5328adf3bf3914634cd878842c73 /var/lib/btc-recorder/runtime.jsonl
/root/tz04a-env/venv/bin/python -c 'import sys; print(sys.version.split()[0])'
stat -c '%s %n' /var/lib/btc-rewardbook-archive/ledger.jsonl /var/lib/btc-rewardbook-archive/runs/1793263627/set.json /var/lib/btc-pairbook-archive/ledger.jsonl
TZ=UTC systemctl show btc-recorder.service btc-pairbook.service btc-rewardbook.service adv3-bot.service btc-pairbook-archive.service btc-pairbook-archive.timer btc-rewardbook-archive.service btc-rewardbook-archive.timer btc-chainbook.service -p Id -p MainPID -p NRestarts -p ActiveState -p SubState -p UnitFileState -p ActiveEnterTimestamp -p Result
TZ=UTC systemctl list-timers btc-pairbook-archive.timer btc-rewardbook-archive.timer apt-daily-upgrade.timer apt-daily.timer --all --no-pager
journalctl _PID=1 -o short-iso --since 2026-11-01 --no-pager | grep -E 'Reload|btc-|adv3' | tail -n 80
grep -E '^(Start-Date|Commandline|Upgrade|End-Date)' /var/log/apt/history.log | tail -n 40
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
systemctl is-active telemetry-watch.service; echo "exit=$?"
test -e /root/tz40-work; echo "/root/tz40-work exit=$?"
test -e /root/btc-recorder-svc; echo "/root/btc-recorder-svc exit=$?"
test -e /root/btc-pairbook-svc; echo "/root/btc-pairbook-svc exit=$?"
test -e /root/btc-pairbook-archive-svc; echo "/root/btc-pairbook-archive-svc exit=$?"
test -e /root/btc-rewardbook-svc; echo "/root/btc-rewardbook-svc exit=$?"
test -e /root/btc-rewardbook-archive-svc; echo "/root/btc-rewardbook-archive-svc exit=$?"
test -e /root/adv3-bot-svc; echo "/root/adv3-bot-svc exit=$?"
find /root/btc-forensics -type f | wc -l
git -C /root/btc-5m-twap worktree list
du -sb /var/lib/btc-rewardbook /var/lib/btc-pairbook /var/lib/btc-rewardbook-archive
echo "$S"; ls -la "$(dirname "$S")"
```

then the memory gate's own reads, appended to the same log:

```
for k in 1 2 3 4 5; do m=$(( $(awk '/^MemAvailable:/ {print $2}' /proc/meminfo) * 1024 )); echo "MemAvailable read $k $(date -u +%T): $m"; [ "$m" -ge 143592894 ] && break; [ "$k" -lt 5 ] && sleep 60; done
```

- **H1** — `find` prints exactly one path.
- **H2** — `df` names source `/dev/vda2` and size `31612203008`; `grep -c` prints at least `1`. With H1 this is map §6's host identity.
- **H3** — the interpreter prints `3.12.`.
- **H4** — `stat` prints all three files: the reward book's archive's ledger and its first run's `set.json`, which §3.4 and §3.5 read, and the pair book's archive's ledger, which G-STILL reads.
- **H5** — `btc-recorder.service`, `btc-pairbook.service`, `btc-rewardbook.service` and `adv3-bot.service` each read `ActiveState=active` and `UnitFileState=enabled`: G-STILL reads all four (§4.6).
- **Memory gate** — the last `MemAvailable read` at least `143,592,894` bytes: a read below it is read again 60 s later, five reads at most, the first at or above it passing (§0.4; map §7 item 137).
- **Disk gate** — `avail` at least `7,800,000,000` bytes (§0.4).

These are eleven checks — H2 two, H5 four — and any one failing is BLOCKED. **The rest is printed and carries no threshold:** the boots; the units and the timers, among them both archives' and the package manager's; systemd's reload records since 2026-11-01 and the package history, beside which §3.4 reads the reward book's archive's runs off its calendar (map §7 items 115 and 129); the consumer's two states, on which map §6's headroom is conditional; `/root/tz40-work` gone and the code trees present, by map §3; the forensic store's count, map §3's `2,370`; the worktrees, map §3's two; `du` of both stores beside `df`, as map §2.5 and §2.6 ask, and of the reward book's archive's state; and the listing of the directory that holds the session's own, whose UUID directories `I scratch` names live or earlier (§3.3).

### 0.4 Resource floors, in exact bytes

**Disk.** `/dev/vda2` free at least **`7,800,000,000`** bytes at the host gate and at the start of every mode that reads the store, a Release or the set: the reward book's `STREAM_FLOOR`, `7,300,000,000`, below which no stream of it opens for a slot (map §2.6; `research/tz33-reward-book-capture.py` line 190), plus `100,000,000`, one slot of its streams at the cut, which it may write while a unit of ours runs — `DISK_FLOOR`, `7,400,000,000` — plus `400,000,000` for this session. **Every unit re-reads free space before its download and stops BLOCKED where the download would leave less than `7,400,000,000`** (lines 1899 to 1933), so nothing this TZ writes can pause the reward book. The session's peak is about `160,000,000` bytes — the worktree's checkout, `12,898,775`; the fetch records and polls of eight days, `40,333,256` at the set's full size; the day files, the logs and the timing files, a few megabytes; and one unit's download at the reward book's cut, `100,000,000` — the rehearsal's four assets, `47,329,972`, come and go before `fetch`; the allowance is that peak twice over, rounded up (map §6, disk). Both archives move their streams off the host every day; TZ-40 read `10,239,823,872` bytes free after its §9 (map §6, disk).

**Memory.** `MemAvailable` at least **`143,592,894`** bytes: twice `71,796,447`, the host peak modelled for the largest peak of any mode in the Architect's runs of these bytes under Python 3.12.3 — `fetch` at the set's full size, `59,879,424` — at the ratio TZ-37 measured between the host's peak and the Architect's for one code, `58,953,728 / 49,168,384`: this code has never run on the host, so its host peak — the larger of map §7 item 131's two — is modelled, as TZ-40 modelled its floor (map §6, memory). **Every mode that holds the set was measured at the set's size** (map §7 item 123): `fetch` over eight member days of 150 markets with distinct condition ids — 1,200 markets, 48 document requests of real-size documents, each day's 96 slot records and 96 reward files of the Architect's captured polls — and `replay` over two days of the Architect's exploration in one process, each with a full day of 43,200 polls, the second day's peak equal to the first's: the replay holds one day at a time and reads a day's polls from its file one line at a time. The peaks, under Python 3.12.3, of the bytes sent: `selftest` `34,910,208`; `fingerprint` `33,955,840`; `archive` `32,768,000`; `rehearse` `45,907,968`; `fetch` `41,537,536` on the stand-in and `59,588,608` to `59,863,040` at the set's full size, five runs, and `59,879,424` the largest of ten earlier runs of the same code under other values of `MEM_FLOOR` and `WAIT_MAX_S`; `replay` `47,910,912` on the stand-in, `56,066,048` over a day of 82 slots with a full day of polls and `55,857,152` to `56,913,920` over two days in one process; `rescore` `46,211,072`; `score` `37,314,560` (§6). Every mode that reads the store, a Release or the set reads `MemAvailable` and free space at its start: a memory read below the floor is read again every 60 s, five reads at most, the first at or above it passing and five below it BLOCKING; free space below `7,800,000,000` BLOCKS; and glibc's mmap threshold and arena count are asserted taken (lines 63 to 69 and 393 to 414). Map §6 records the host: `1,002,127,360` bytes in all, one processor; TZ-40 read `MemAvailable` from `201,670,656` to `223,096,832` bytes across its session and TZ-37 from `136,404,992` (map §6, memory). Every mode runs under `nice -n 19`.

### 0.5 Refs and the number

`I0 number`, into `logs/05-number.log`, and `git -C /root/btc-5m-twap ls-remote origin`, into `logs/05-refs.log`, after §0.4, every ref reported; both again in §3.1 — `I0 number` after its fetch, `git ls-remote origin` before its push. Map §1's last record is TZ-40's audit, 106 ref lines. **The Architect read 113 on 2026-11-04 at 17:35 UTC:** `HEAD` and `refs/heads/main` at `494f10f`, PR #40's merge, above `a1c7ba1`, revision `2026-11-01-b` of `SYSTEM-MAP.md`; seventeen `tz-*` branches; thirty-nine pull heads; thirty-nine `pairbook-streams-*` and twelve `rewardbook-streams-*` tags; and the two annotated tags with their peeled lines. Every run of either archive that takes a new set adds one tag — the reward book's at 01:30:20 UTC and the pair book's at 03:00:20, and each possibly 1,800 s and 600 s after a reload of systemd (map §7 items 115 and 129); from 2026-11-05 to 2026-11-08 at least four of each. Every commit on `main`'s first-parent line above `494f10f` is reported with the paths it changed, the upload that carries this TZ among them. A difference is recorded, not BLOCKING, unless `main` does not carry revision `2026-11-01-b` or `refs/heads/tz-41-l0-our-quote` already exists — either is BLOCKED.

**NUMBER — CANON hard rule 2.** `I0 number` reads, in the primary checkout, `git ls-tree --name-only origin/main -- CryptoTZ/ CryptoReports/` and must print `NUMBER PASS - 2 of 2`: `CryptoTZ/` holds `TZ-41-l0-our-quote.md` and no other file whose name begins with `TZ-41-`, and `CryptoReports/` no report whose name does (lines 2283 to 2298). Anything else is BLOCKED, here and in §3.1 alike. The Boss's order of 2026-10-29 named this specification TZ-36; `main` gave that number to `TZ-36-advisor-trust-block.md` on 2026-10-31 and 37 to 40 to the advisor's next four, so it carries 41, the next free.

---

## 1. Why this TZ exists

Line numbers here are Appendix A's unless a file is named.

**The question** — CANON PART II, the L track's L0: on reward markets chosen by a rule fixed before their data, does a
resting two-sided quote of ours, simulated on the captured books and trades with queue position and the venue's terms,
earn its liquidity-reward share by the venue's formula and its maker rebate, net of its fills marked to the market? The
W track closed on a quote whose fills are adversely selected and paid by nothing but the rebate (TZ-32). The venue pays
makers on other markets a second way, a daily pool per market shared by a score of the book a maker keeps near the
midpoint (CANON §1.7), and the reward book has captured 150 such markets a day since 2026-10-28 (TZ-33, map §2.6) and
moved their streams to Releases every day since 2026-10-29 (TZ-34). L0 asks whether that pool, on markets where
information arrives slowly, pays a quote of ours more than its fills lose.

**The quoting rule, ours, fixed here before any stream of the set has been read** (`Day.decide`, lines 1224 to 1290). On each member
market of a day, on its first token's book — the token the selection lists first; the venue's book for it holds every
order on both tokens, a bid on the second token at `1 − p` an ask on the first at `p` — from the day's first instant to
its last:

1. **Where — alone, one tick inside a wide touch.** Where the book has a best bid `b` and a best ask `a` at least
   **five ticks** apart, a bid at `b + tick` and an ask at `a − tick`, each of the market's **minimum size** — the
   size below which the venue scores no order — at prices strictly between `0` and `1`. `tick` is the market's tick
   size, from its seed and its `tick_size_change` frames. Each quote is then at least a tick and a half from the
   touch's midpoint, the margin a fill buys against the price moving on; and **it rests alone at its price**, ahead of
   no one and behind no one but the orders that later join it, so no fill of it hangs on a queue place the stream
   cannot show — the condition CANON §1.6 names for any later quote of ours.
2. **When not:** no quote while either best is missing, while the touch is under five ticks wide, or while the two
   targets are not inside the market's maximum spread of their own midpoint — `a − b − 2·tick` below twice the maximum
   spread — so that a quote of ours always scores; none on a member whose minimum size or maximum spread is zero; **no
   bid while the position the host knows of is one minimum size long or more, no ask while it is one minimum size
   short or more** — the least a two-sided quote at minimum size can hold. A live quote whose target is gone is
   cancelled.
3. **Replace:** a live quote whose price is no longer the target is cancelled and a new one sent at the target, the
   same instant. A quote the host has learned is filled, cancelled or refused, or partly filled below the minimum size,
   is replaced at the next decision. A decision is made after every frame of the market the host receives, at each
   slot's first instant and after a seed.
4. **Post-only:** an order that would cross when it arrives is refused, as the venue refuses a post-only order that
   would match.
5. **A disconnect:** a close of the stream other than a slot's end cancels every live quote at the host's instant.

**The replay, at venue time** (lines 730 to 1598) — TZ-32's, on the reward book's streams: every frame one line with its
host receipt `recv_ns` and the venue's frame verbatim, read in the order stored (map §2.6). The host's clock is each
line's `recv_ns`; the venue's is each frame's `timestamp`, in milliseconds.

- **Latency:** a message the host sends at host instant `h` reaches the venue at `h + L`, **`L = 50` ms** one way, as
  TZ-30 and TZ-32 took it; the host learns of a fill, a refusal or a cancel `L` after the venue makes it. A message due
  at the venue at `τ` takes effect before every frame of its market stamped after `τ`, and before any line whose host
  instant is more than 1 s after `τ`.
- **No taker delay.** The selection keeps no market with one (TZ-33 §1: `seconds_delay` absent or `0`; map §2.6: "no delay"), so an order that would cross ours
  is a taker the instant it arrives, or a post-only order the venue refuses — which of the two, the stream cannot say.
- **The book:** seeded by each subscription's `book` frame of the first token and moved by every `price_change` entry
  of it, a size of zero removing the level; every later `book` frame of the token replaces it, after its touch and
  every level are compared with the book rebuilt to it (G-BOOK, §4.3). Prices are integers of thousandths and sizes of
  hundredths, read exactly from the venue's text.
- **A slot's files:** each slot's stream runs from `S − 5` to `S + 905`. Lines received before `S` build the next
  book; at `S` every member's book becomes the one its new file has built, our orders standing; lines at or after
  `S + 900` are the next slot's. A day's 96 slots are replayed in order as one run, and nothing carries from one day to
  the next.
- **A match:** the entries of the token that share one venue stamp form a block; a block that the token's own `book`
  frame with the same stamp closes is a match, any other is not (TZ-32 §1). In a match a side is hit where its best
  level at the block's start decreased, its consumption running from that level outward while every level before it
  was emptied. A resting order of ours on the hit side fills where the sweep reaches its price, for `min(its remaining
  size, max(0, T − Q))`, `T` the consumption at its price and beyond it and `Q` the size queued ahead of it; then `Q`
  falls by the consumption at its price.
- **The queue:** an order arriving at a level joins behind the size displayed there then — none, for a quote alone at
  its price — and where the level later shrinks with no trade, `Q` is held at most at the level's size.
- **A crossing order:** where the book's opposite side comes to a resting order's price with no match, the orders that
  did so would have met ours; a variant that counts them takers fills ours at once, at the block's stamp, for their
  size not yet counted.

**The reward, by the venue's published formula** (`Day.share_of` and `Day.parts_of`, lines 1009 to 1071). The venue samples each market's book once a
minute at a random offset, scores each maker's orders inside the market's maximum spread `v` of the size-cutoff-adjusted
midpoint by `((v − s)/v)²` a share, `s` an order's distance from it, takes a maker's sample score as the smaller of its
two sides' sums — or a third of the larger, where the midpoint lies in `[0.10, 0.90]` — divides it by every maker's,
and pays each maker the market's daily rate times its day's mean of those shares, at midnight UTC, `1` pUSD at least
(CANON §1.7; the venue's liquidity-rewards page, read 2026-10-29). The replay takes that mean as the time-average of our
share over the day — its expectation under the random sampling — and:

- **The midpoint:** of the best bid and the best ask among the displayed levels of at least the minimum size and our
  own orders; the venue does not publish its adjustment.
- **Our score:** our resting orders of at least the minimum size inside `v` of that midpoint, by the formula.
- **The competitors' score — bracketed.** The stream shows each level's size, not its makers. Over every split of the
  displayed levels of at least the minimum size inside `v` among makers, with `A` and `B` the two sides' scored sums,
  the competitors score **at most `(2·min(A, B) + max(A, B))/3`** and **at least `max((A + B)/4, max(A, B)/3)`** where the
  midpoint is in `[0.10, 0.90]`, and at most `min(A, B)` and at least `0` outside it (`envelope`, lines 931 to 937; the
  self-test checks both against every split of six pairs among three makers). **The venue's own figure:** each served
  reward poll carries `market_competitiveness`, which times the daily rate the Architect read as the makers' total
  score — on 192 comparisons of 2026-10-29 it fell inside the book's bracket at 167, its median `0.848` of the upper
  bound — read, not measured against the venue's payouts.
- **The rate:** the selection's daily rate from the day's first instant, then each served poll's; a served poll whose
  page holds no row stops the reward until the next that does.
- **The 1-pUSD minimum** — whether per market or per address, the venue does not say: `pess` and `central` pay a
  member's day only where it reaches `1`, `opt` the day's sum where it does.
- **The daily normalization** over all 1,440 samples: where a sample scores no maker at all the venue divides by fewer,
  and the replay's reward is a lower bound.

The share changes at every frame of its market the host receives, at every order event of ours at its venue instant,
at every poll and at each slot's instant; between those instants it holds, and each variant's clock moves forward
only (lines 958 to 1007).

**The rebate:** for a member whose gamma document, as the selection stored it, reads `feesEnabled` `true` and a
taker-only schedule of exponent `1`, its `rate` times its `rebateRate` times `C·p·(1 − p)` a fill — published, not
measured on these categories (CANON §1.7). `pess` counts none.

**The marks.** Each member's position at the day's end is valued at its outcome where its gamma document, read once
after the set's last day, states it resolved — closed, its prices exactly `0` and `1`; else at the day's last midpoint
of its two-sided book, **a proxy, named so wherever it is used**; else, where the market showed no two-sided book that
day, by liquidation into its book as it stands. A day's money for a variant is its reward paid, its rebate counted and
its marks: positions start at zero each day.

**The variants.** What the stream cannot show — where in a level's queue our order stands, whether an order that came
to ours was a taker, and the competitors' true score — is bracketed. Every variant replays the same rule on the same
frames (lines 104 to 108 and 788 to 798):

| variant | queue | crossing orders | competitors | 1-pUSD minimum | rebate | role |
|---|---|---|---|---|---|---|
| **`pess`** | behind the displayed size | takers | the larger of the book's most and the venue's figure | per member-day | none | **gated: EARN** — every assumption against us |
| **`opt`** | first at its level | refused, never takers | the smaller of the book's least and the venue's figure | per day | counted | **gated: NO EARN** — every assumption for us |
| `central` | behind | takers | the venue's figure | per member-day | counted | barred |

Before a member's first poll the venue's figure is absent, and `pess` and `central` take the book's most, `opt` its
least.

**The set** (lines 1600 to 1858). The candidates are the UTC days from **2026-10-31**, `1793404800`, in order — after every
read of the Architect's exploration (§1, exploration). A candidate is a **member** where the reward book's store holds
its selection — the first attempt whose record reads `ok`, its replies' SHA-256 the record's — of at least one market,
and each of its **96 slots** qualifies by TZ-30's stream rule as the reward book records it: the slot's `slot.json`
records consecutive from `k = 0`, each of that selection and its member count, no error, its stream opened and not cut,
its file named by the record; the first subscribed by `S` and not joined late; the last's last frame at or after
`S + 900`; no gap above 15 s within a file or between two; and every stream file among the assets of a complete run of
the reward book's archive, by its name. **The members are the first 8**; the walk stops BLOCKED past 6 non-members
before the eighth — at 2026-11-13 — and every candidate is disclosed in order with its reason. Each member's polls are
the served replies of its 96 slots' reward files, in the order received.

**The test — eight days, each a block.** For a variant, a day's money is its total over the day's members. **EARN**
where `pess`'s money reaches **`θ = 10` USDC on every one of the 8 days**; **NO EARN** where `opt`'s stays below `θ` on
every one; **UNDECIDABLE** otherwise, and where both hold. Under independent days, a variant whose day reaches `θ`
with probability at most `1/2` reads EARN with probability at most `2⁻⁸ = 0.00390625`, and one whose day reaches it with
probability at least `1/2` reads NO EARN with at most the same — each under `0.005`, the sign test of TZ-30's B3 on
day-blocks, exact. **Power**, printed before any money is read: EARN's is `q⁸` where each `pess` day reaches `θ` with
probability `q` — `0.430467` at `0.90`, `0.663420` at `0.95`, `0.922745` at `0.99`. A day is the venue's own unit: it
pays each day's pool on its own scores, so a day's money depends on no other day's replay. `θ` is TZ-30's.

**What a reading establishes, and what it does not.** EARN says that on 8 days no one had read, the rule's quotes —
behind every displayed queue, every crossing order a taker, the competitors at the most the book or the venue allows,
the reward unpaid on any member-day under 1 and no rebate — earned at least 10 USDC a day over the day's members, its
positions marked to each market's midpoint at the day's end. It says nothing of a quote placed live, whose fills and score move the book
this replay holds fixed, nor of the venue's payouts — L1's. NO EARN says that even first in every queue, never met by a
crossing order, the competitors at the least, the rule's quotes kept under 10 USDC a day. Neither speaks of another
rule, another size, another latency or other markets.

**Exploration, excluded from the set by time.** The Architect's snapshot and runs of TZ-33's instrument on 2026-10-27
(map §5) framed the track. **For this rule the Architect read, on 2026-10-30, the reward book archive's first three
Releases** — `rewardbook-streams-1793263627`, `-1793286490` and `-1793306720`, the 132 slots from 2026-10-28 11:30 to
2026-10-29 20:15 UTC, 133 files, `1,417,239,479` bytes, downloaded anonymously — with this instrument's replay, each
market's minimum size, maximum spread and daily rate from its own selection of 2026-10-29 and its snapshot of the
venue's reward listing that evening (149 of the first day's 150 markets, 135 of the second's), no fee, and no poll: the
polls stay on the host. Positions started at zero at each UTC day. **By the touch's width the rule needs:**

| touch at least | `pess` reward a day | `pess` marks a day | `pess` money a day | `opt` money a day | shares filled a day, `pess` |
|---|---|---|---|---|---|
| three ticks | `353` | `−435` | `−82` | `247` | `64,368` |
| four | `296` | `−230` | `65` | `315` | `48,709` |
| **five** | **`273`** | **`−158`** | **`115`** | **`361`** | **`40,396`** |
| seven | `224` | `−107` | `117` | `335` | `33,361` |

Without the margin a fill at the touch loses more than the reward pays (W1's finding, here on reward markets); from
five ticks the money no longer rises with the width while the reward keeps falling, and five is the rule. At five,
`pess`'s eight 4-hour blocks had a mean of `19.9` and a deviation of `26.3` USDC — about `64` a day were they
independent — so a day reached `θ` with probability about `0.95`, at which EARN's power is `0.66`: the alternative §4
names. At three ticks, a pause of 60 s after a fill made `pess` lose more, `−101` a day, and quoting only on members of
minimum size 50 shares or less made it lose less, `−25`; holding at most one minimum size rather than two lost less on
the Architect's own capture's first 90 minutes, and is the rule.
**The Architect's own capture from a second host**, TZ-33's code from 19:45 UTC on 2026-10-29 to 01:45 UTC on 2026-10-30, gave
the competitiveness bracket's 192 comparisons and the three slots, their 1,157 served polls of 1,350, on which the
instrument and the Architect's reference agreed. None of it is a member's, and every member day begins after it. **On 2026-11-04 the
Architect read the exploration's 133 files again**, for this instrument's memory and processor (§0.4, §6) and for
their frames' gaps: the largest `10.576` s — the reward book sends `PING` every 10 s and stores the venue's `PONG`
as a frame (`research/tz33-reward-book-capture.py` lines 179 and 1162 to 1171), so that a gap above 15 s is a stalled
connection, not a quiet book. The Release listings of later runs were not read.

**When.** The archive moves each day's streams at 01:30:20 UTC the next day (map §2.6). The eighth candidate ends at
2026-11-08 00:00 UTC; the run begins from **2026-11-08 07:30:00 UTC**, `1794123000`, inside a band of 07:30 to 21:00
UTC (§0.0), and `fetch` waits for the archive's assets to reach each candidate's last slot, re-reading its ledger every
60 s, and stops BLOCKED 6 h after its start — or at once where a non-member pushes the walk to a day not yet ended
(lines 1617 to 1634 and 1781 to 1841). Begun on 2026-11-08, the run absorbs no non-member; begun on a later day, one
for each day later.

---

## 2. Scope

**Repository paths this TZ may write, and no others:**

1. `research/tz41-l0-our-quote.py` — new, byte for byte Appendix A's, on branch `tz-41-l0-our-quote`, then a pull
   request. Not merged by the Executor.
2. `CryptoReports/TZ-41-l0-our-quote-report.md` — straight to `main`, in one commit. **The one path pushed to `main`,
   and the exemption to item 8 below.**

**Host paths this TZ may write:** `/root/tz41-work/**`; `/root/btc-forensics/`, by exclusive create only (§9); and in
the primary checkout `/root/btc-5m-twap`, its `.git` for the branch and the worktree, and its `CryptoReports/` for the
report. **Host paths it removes, under §3.3 and §9 and nothing else:** `/root/tz41-work/` with its worktree, and the directories
`I scratch` names earlier.

**Prohibited, each absolutely:**

1. No committed file is modified; every `frozen` row of map §0 is byte-identical at run end.
2. **Nothing under `/var/lib/btc-recorder/`, `/var/lib/btc-chainbook/`, `/var/lib/btc-pairbook/`, `/var/lib/adv3-bot/`
   or `/etc/adv3-bot/` is opened, listed or written** — the instrument's audit hook refuses every open and listing there
   (lines 190 to 295); only §0.3's `df`, `find` and `grep -c`, at both of its runs, touch the recorder's root, and its
   `du -sb` the pair book's and the reward book's sizes.
3. **Under `/var/lib/btc-rewardbook/` nothing is written, and nothing is opened or listed but by `I fetch`, for
   reading, and only a candidate day's directory `<D0>/`, `D0` from `1793404800` to `1794528000`: its listing, its
   `select.<a>.json` and `select.<a>.replies.jsonl.gz`, and its `<S>.<k>.slot.json` and `<S>.<k>.rewards.jsonl.gz`**
   — the named exemption, and the reserve's end (map §2.6): this TZ is L0's measurement. **No stream file stored
   there is opened by anything**, and no day before `1793404800` is opened or listed.
4. **Under `/var/lib/btc-rewardbook-archive/` nothing is written or listed; `ledger.jsonl` is opened for reading by
   `I archive`, `I fetch` and `I still`, and every complete run's `runs/<A>/set.json` by `I archive` and `I fetch`.
   Under `/var/lib/btc-pairbook-archive/` nothing is written or listed, and `ledger.jsonl` is opened by `I still`
   alone** — the named exemptions; nothing else in either is opened but by `du -sb` and `stat` at §0.3.
5. **No unit is signalled, started, stopped, enabled, disabled or changed.** `systemctl show`, `is-active`,
   `is-enabled`, `list-timers` and `journalctl` are this TZ's only reads of a unit and of systemd.
6. `/root/tz04a-env/`, `/root/tz01-env/`, `/root/btc-recorder-svc/`, `/root/btc-pairbook-svc/`,
   `/root/btc-pairbook-archive-svc/`, `/root/btc-rewardbook-svc/`, `/root/btc-rewardbook-archive-svc/` and
   `/root/adv3-bot-svc/` are not modified; `/root/btc-forensics/` only by §9's exclusive create.
7. **Requests:** `gamma-api.polymarket.com/markets`, with `User-Agent: btc-5m-twap-tz41` and `Accept:
   application/json`, in `I fetch` alone — the members' documents, once, each request held to the idle stretch (lines
   1717 to 1778); **the reward book archive's Release assets**, from `github.com` and the hosts it redirects a download to,
   `release-assets.githubusercontent.com` and `objects.githubusercontent.com`, anonymously, with `User-Agent:
   btc-5m-twap-tz41` and `Accept: application/octet-stream`, in `I rehearse`, `I replay` and `I rescore` alone, each
   held to the idle stretch (lines 1863 to 1933); `git` against `origin`; and `gh` for the pull request and for git's
   credential alone. **No other request** — no CLOB, no websocket, no Data API, no GitHub API, no authenticated call
   to the venue — and the hook refuses any other host in every mode.
8. Nothing is pushed to `main` except the report of item 2.
9. **No stream asset is downloaded but a member day's and the rehearsal's four**, and none is read but by the
   instrument's replay, in its unit, before its removal.
10. **No single member's, fill's or poll's price, size, rate, competitiveness or outcome is printed or written outside
    `/root/tz41-work/`**: the instrument prints sums over a day or a set, and the report quotes them. **This binds the
    Executor's own reads as strictly as the instrument** (map §7 item 118): no file under `/root/tz41-work/fetch/`,
    `/root/tz41-work/days/` or `/root/tz41-work/dl/`, nor `set.json`, `reading.json`, `rehearsal.txt` or
    `rescore.txt`, is printed, whole or in part, by any command but the instrument's modes and `sha256sum`, `stat`,
    `wc -l` and `du`, which print hashes, sizes and counts; the timing files carry slots, seconds and bytes and may be
    printed, and so may `state.json`, `read-ledger.jsonl` and every file under `logs/`. The one exemption is §9's
    byte-for-byte copies into `/root/btc-forensics/` of the files the report names by hash.
11. No Release is created, and no dataset, archive or binary enters git history.

---

## 3. The work, in this order

Every command's output goes to `logs/`, one file per step under the names below, and is quoted in the report; a step run again appends to its own log under a `date -u` line. **B-RECLAIM-SCRATCH runs inside §3.3 and holds back nothing after it — no later step reads what it removes (map §7 item 140); B-RECLAIM-OWN runs last, after §3.11 (§9).** On a BLOCK before §3.1, B-RECLAIM-OWN runs with `I0` in place of `I` and without its `git worktree remove` line; on a BLOCK or a FAIL after it, the run goes to §3.11 and §9, skipping every step that needs a PASS it lacks.

| step | logs |
|---|---|
| §0.0 to §0.5 | `00-instant.log`, `01-stage.log`, `02-fingerprint.log`, `03-host-gate.log`, `05-number.log`, `05-refs.log` |
| §3.1 | `10-number.log`, `11-worktree.log`, `12-fingerprint.log`, `13-push.log`, `14-pr.log` |
| §3.2 | `20-selftest.log` |
| §3.3 | `30-still.log`, `31-scratch.log`, `32-reclaim-scratch.log` |
| §3.4 | `40-archive.log` |
| §3.5 | `50-rehearse.log` |
| §3.6 | `60-fetch.log` |
| §3.7 | `70-replay.log`, `71-replay-again.log` |
| §3.8 | `80-rescore.log` |
| §3.9 | `90-score.log`, `91-score-again.log` |
| §3.10 | `95-still.log` |
| §3.11 | `96-host-gate-again.log`, `97-archive-again.log`, `98-closing.log` |

**Where the session's permission classifier refuses a command of a block named B-…**, the Executor tries the block once and hands the Boss its paste, unchanged, once, in plain words (CANON hard rule 14; map §7 items 124 and 138); the Boss runs it verbatim in a root shell on the VPS, every step chained to the one before it and appended to its log under a `date -u` line, and the Executor verifies it from that log and through the reads this TZ names — never from the Boss's account — and runs no step of the paste again (map §7 item 144).

### 3.1 The branch and its file

```
git -C /root/btc-5m-twap fetch origin
I0 number
git -C /root/btc-5m-twap worktree add -b tz-41-l0-our-quote /root/tz41-work/wt origin/main
```

Into `10-number.log` the fetch and `I0 number`, which must print `NUMBER PASS - 2 of 2` again (§0.5), or BLOCKED; into `11-worktree.log` the worktree and §0.1's script again, verbatim but for its argument, `/root/tz41-work/wt`; it must print the same lines, bytes and SHA-256 as at §0.1; into `12-fingerprint.log` `I fingerprint`, which must print `FINGERPRINT PASS` again, from the worktree's file. Into `13-push.log`: commit the one file alone on the branch; `git -C /root/btc-5m-twap ls-remote origin` (§0.5); push with `git -C /root/tz41-work/wt push -u origin tz-41-l0-our-quote` — through `credential.helper=!gh auth git-credential` where the URL's credential is refused (map §6, git remote) — then:

```
date -u +%FT%T.%NZ; git -C /root/tz41-work/wt ls-remote origin refs/heads/tz-41-l0-our-quote
git -C /root/tz41-work/wt rev-parse HEAD
```

— the instant the commit is on `origin`, and its hash there, which must be the worktree's `HEAD`; into `14-pr.log` the pull request against `main`, opened with `gh pr create`. A failed assert or a non-zero exit here is BLOCKED. **The commit on `origin` comes before any stream of the set is read:** every mode that reads the store, a Release or the set writes the worktree's `HEAD` and its own SHA-256 into `read-ledger.jsonl` (lines 2512 to 2521).

### 3.2 The self-test

`I selftest` must print `SELFTEST PASS: 42 checks`. It reaches no network but a listener of its own on `127.0.0.1`, and runs on literals, on a synthetic day of two slots and on temporary trees under `/root/tz41-work/selftest-tmp/`, which it removes (lines 2547 to 3050). A red self-test stops the run here, and it goes to §3.11 and §9.

### 3.3 The units, the directories beside this session, and B-RECLAIM-SCRATCH

`I still` records the recorder's, the pair book's, the reward book's and the advisor's `MainPID`, `NRestarts` and `ActiveState` in `state.json`, with the instant, and prints their `MemoryCurrent` and `MemoryPeak` and both archives' units' states (lines 2322 to 2347). Then `I scratch "$(dirname "$S")"` lists every UUID directory beside this session's own and names each **live** — born from 1 s before to 60 s after the start of a running process whose `argv[0]` is `claude` or ends in `/claude.exe` — or **earlier** (lines 2350 to 2388). Map §3 expects the two TZ-40's session left, `981b3989…` and `e19b6910-2c25-4765-98b9-49d2a819677e`, unless a reboot of the host emptied `/tmp`; `238335b9-cf23-414a-8e8f-ad4705c4d19e`, born with the remote-control processes, is live and no TZ's, and is never touched.

**B-RECLAIM-SCRATCH**, for every directory `I scratch` names **earlier** — none it named live, and never this session's own:

```
cd /root/tz41-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz41-work/wt/research/tz41-l0-our-quote.py reclaim <each earlier directory, by its full path>
rm -rf <one such directory>; echo "exit=$?"
test -e <that directory>; echo "exit=$?"
```

One `reclaim` names every earlier directory and must print `RECLAIM PASS` before any removal; then one `rm -rf` and one `test -e` a directory, the last reading `exit=1`. `reclaim` refuses a directory born from 1 s before to 60 s after a running claude process started, and any path but `/root/tz41-work` that is not a UUID directory under `/tmp/` whose parent's name carries `btc-5m-twap` (lines 2455 to 2509). If `I scratch` names none earlier, the block is recorded as empty and skipped. **Its paste**, where the classifier refuses it — the Executor writes in every earlier directory's full path, one `rm -rf` and one `test -e` a directory, all chained to the `reclaim`'s `exit=0`, which it reaches only after `RECLAIM PASS`:

```
{ date -u +%FT%T.%NZ; (cd /root/tz41-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz41-work/wt/research/tz41-l0-our-quote.py reclaim <D1> <D2>); echo "exit=$?"; } >> /root/tz41-work/logs/32-reclaim-scratch.log 2>&1 && tail -n 1 /root/tz41-work/logs/32-reclaim-scratch.log | grep -qx 'exit=0' && { date -u +%FT%T.%NZ; rm -rf <D1>; echo "exit=$?"; test -e <D1>; echo "exit=$?"; rm -rf <D2>; echo "exit=$?"; test -e <D2>; echo "exit=$?"; } >> /root/tz41-work/logs/32-reclaim-scratch.log 2>&1
```

**It holds back nothing of §3.4 to §3.11**, which read none of what it removes (map §7 item 140): the Executor goes on while the paste waits for the Boss.

### 3.4 The archive's record

`I archive`: the reward book archive's two units by `systemctl show`; its `ledger.jsonl` read whole, its size and SHA-256, every complete record printed with its UTC stamp; every run summarized — on the calendar or off it, its set, its deferrals and its terminal record; every complete run's `set.json` asserted by the SHA-256 its set record carries, with its files, bytes and slots; the slots the assets reach, at and after `1793404800`; the tags `origin` carries beside the sets; whether the archive is halted; and **the rehearsal's four assets in the set of `rewardbook-streams-1793263627` by name, bytes and SHA-256**, or BLOCKED (lines 2391 to 2429). The rest is printed facts and gates nothing: the report sets each run off the calendar beside §0.3's reads of systemd's reloads (map §7 items 115 and 129).

### 3.5 G-REHEARSAL

`I rehearse`: the four assets downloaded from `rewardbook-streams-1793263627` by the bytes and SHA-256 Appendix A fixes — TZ-34's report's, and §3.4's set's — each held to the idle stretch, replayed as one hour under fixed parameters, removed, and compared with the Architect's reference (§4.1). **A network failure is resumable:** `I rehearse` may be run again twice, 600 s apart; a third failure is BLOCKED. A FAIL stops the run here, and it goes to §3.11 and §9.

### 3.6 The set — G-SET

`I fetch`, in the background, its output to `logs/60-fetch.log`, read until it prints `G-SET PASS` or fails (§4.2). For each candidate in order it waits for the archive's assets to reach the day's last slot, then reads the day from the store held to the idle stretch; then the members' documents, each request held. `set.json`, each member's `fetch/<D0>.json` and its polls are written once. **A network failure is resumable:** `I fetch` may be run again twice, 600 s apart, and a third failure is BLOCKED; a run after `set.json` exists reads nothing and asserts the records unchanged.

### 3.7 The replay — G-BOOK

`I replay`, in the background, its output to `logs/70-replay.log`, read until it prints G-BOOK or fails: every member day, slot by slot, each slot a unit held to the idle stretch, its files downloaded, replayed and removed; after its first 24 units it projects its replays' processor time over the set's bytes and stops BLOCKED above `3,000` s; each day's `days/<D0>.slots.txt` and `days/<D0>.json` written once at its end; then G-BOOK (§4.3). **A network failure is resumable:** the days on disk are kept, a day cut short is replayed again from its first slot, and `I replay` may be run again twice, 600 s apart; a third failure is BLOCKED. Then `I replay` again, into `logs/71-replay-again.log`, which replays nothing and prints G-BOOK again.

### 3.8 The rescore — DETERMINISM

`I rescore`: the set's first day's first 24 slots downloaded again and replayed again; their lines must be byte for byte the replay's (§4.4).

### 3.9 The score, twice

`I score`, then `I score` again. The first prints the power, G-BOOK and every day's money by variant, and the reading; the second must print `unchanged` for `reading.json`.

### 3.10 The units again — G-STILL

`I still` (§4.6).

### 3.11 The closing reads

§0.3's block again, the memory gate's reads among it, into `logs/96-host-gate-again.log`; `I archive` again, into `logs/97-archive-again.log`; then, into `logs/98-closing.log`:

```
TZ=UTC systemctl show btc-recorder.service btc-pairbook.service btc-rewardbook.service adv3-bot.service btc-pairbook-archive.service btc-rewardbook-archive.service -p MainPID -p NRestarts -p ActiveState -p MemoryCurrent -p MemoryPeak
journalctl -u btc-recorder.service -u btc-pairbook.service -u btc-rewardbook.service -o short-iso --since -24h --no-pager | tail -n 60
free -b
du -sb /root/tz41-work
cat /root/tz41-work/state.json /root/tz41-work/read-ledger.jsonl
wc -l /root/tz41-work/timing-replay.jsonl /root/tz41-work/timing-rescore.jsonl /root/tz41-work/timing-rehearsal.jsonl
```

---

## 4. The gates — fixed here, before any of their data exists

| gate | population | PASS | false failure | power, against |
|---|---|---|---|---|
| **G-REHEARSAL** | the four assets of `rewardbook-streams-1793263627`, 2026-10-29 00:00 to 01:00 UTC, 150 markets | §4.1's lines byte for byte the Architect's | `0` — the same stored bytes replayed by the same rule, equal to the Architect's independent replay on 2026-10-30 | `1`, any change in an asset, a fill, a queue, a crossing, a share, a sum or the arithmetic |
| **G-SET** | the walk from `1793404800` | 8 members, at most 6 non-members before the eighth | `0` | — |
| **G-BOOK** | every `book` frame of the members' first tokens but a seed, over the 8 days | the rebuilt touch equal to the venue's own at no fewer than 99 in 100 | a count, not an estimate: equal at 15,461 of 15,462 frames over the Architect's exploration's 132 slots | `1`, a lost frame, a misread entry or a missed session |
| **DETERMINISM** | the first member day's first 24 slots | each slot's line byte for byte the replay's | `0` | `1`, any difference between two downloads or two replays |
| **L0** | `pess`'s and `opt`'s money on each of the 8 days | §4.5 | `2⁻⁸ = 0.00390625` for each answer, under independent days | EARN `0.430467`, `0.663420` and `0.922745` where each `pess` day reaches `θ` with probability `0.90`, `0.95` and `0.99` |
| **G-STILL** | the recorder, the pair book, the reward book and the advisor, §3.3 to §3.10 | unchanged, or the pair book moved by its archive's own restarts alone | `0` — systemd and the pair book archive's ledger read directly | `1`, a restart or a stop that is not that archive's |

### 4.1 G-REHEARSAL

The four assets — 2026-10-29 00:00 to 01:00 UTC, `47,329,972` bytes — are one stand-in hour: every market of the
first seed after the first subscribe, 150, each with its first `book` item's token as its first token, under fixed
parameters — minimum size `50` shares, maximum spread `4.5` cents, a rate of `100` a day, no fee and no poll — so that
nothing of the store is read for it (lines 2162 to 2248). Every variant replays it; `compare_lines` prints, per member and
variant, its reward, rebate and marks at twelve places and its position, cost, fills, shares, crossed shares, scored
nanoseconds, sends, cancels, refusals, crossings and mark, then the book's counts: **451 lines, SHA-256
`1ab40f4b2a9b4f263e92959dc78a67dc9583731889cce70b22edad59091944cd`**, the Architect's (line 160). **The Architect's lines come from its own replay**, written from §1
and sharing no code with this instrument — every price, size, score and share a `Fraction`, every share recomputed from
scratch at each point §1 names, no cache, no filter, no fast path — and equal to the instrument's byte for byte under
Python 3.12.3, as were its lines over three slots of the Architect's own capture with their own parameters and their 1,157
served polls, 451 of 451, through a queue in memory and through the polls file alike, and over the self-test's
synthetic day (§3.2). `rehearse` prints `G-REHEARSAL PASS`. **A FAIL means
the stored record differs from what the Architect replayed, or that the instrument replays otherwise**, and the reading
would not be what §1 describes.

### 4.2 G-SET

`fetch` prints `G-SET PASS` when the walk from `1793404800` has formed 8 members with at most 6 non-members before the
eighth; every member's stream files are among the archive's assets by their own names, and the bytes and SHA-256 the
replay downloads them by are the archive's; every member's document is found once, open or closed; and `set.json` is
written. Every candidate is listed in order, a non-member with its first failing reason.

### 4.3 G-BOOK

At every `book` frame of a member's first token but a subscription's seed, the touch the replay rebuilt — the best bid
and its size and the best ask and its size — equals the frame's at **no fewer than 99 in 100** over the set (lines
2055 to 2067). `replay` and `score` print the counts by day, and the count of frames equal at every level beside them,
barred. `score` reads no reading where G-BOOK fails: a FAIL means the replay's book is not the venue's, and its fills
are not ours.

### 4.4 DETERMINISM

`rescore` downloads the set's first day's first 24 slots again and replays them again from the day's start; each
slot's line — the stream's counts and each variant's fills, shares, position, cost and reward with a SHA-256 of every
member's state — must be byte for byte the replay's: 24 of 24 (lines 1956 to 1979).

### 4.5 L0's reading

| condition, on each day's money of `pess` and `opt` over the set's 8 days | reading |
|---|---|
| every `pess` day at or above `θ = 10` USDC, and some `opt` day at or above it | **EARN** |
| every `opt` day below `θ`, and some `pess` day below it | **NO EARN** |
| otherwise | **UNDECIDABLE** |

Pure arithmetic on the day files (`day_money` and `l0_reading`, lines 2091 to 2120); `score` prints both gated
variants' money on every day, each split into the reward paid, the reward before the 1-pUSD minimum, the rebate and
the marks, with the members paid, the fills, the shares, the crossed shares, the hours scored and the marks by kind; the
least `pess` day and the most `opt` day; and, barred from every reading, `central`'s and each variant's total and mean
day. **No row reads a power.** The marks are a proxy, named so (§1).

### 4.6 G-STILL

From §3.3 to §3.10 the recorder, the reward book and the advisor keep their `MainPID`, `NRestarts` and `ActiveState`,
and the pair book keeps them or is moved by its archive's own restarts alone — its ledger's `restart` records since
§3.3's read, a chain from the recorded `MainPID` to the current one, `NRestarts` one higher at each, the unit `active`
(lines 2301 to 2347). The reward book's archive restarts nothing (map §2.6). **This TZ signals nothing**, so a FAIL runs no
block, and the report names what changed beside §3.11's journal of the units — the package manager restarts capture
units (map §6, process supervision; §7 item 120).

---

## 5. The instrument

`research/tz41-l0-our-quote.py`, Appendix A, fixed by the Architect as this TZ's Validation and written byte for byte.
**The standard library alone**, run under `/root/tz04a-env` — Python 3.12.3, the capture units' interpreter, which
nothing here modifies. It imports nothing from the repository. **Its own code** is its audit hook (lines 190 to 295), the memory
and disk floors (lines 380 to 414), the idle stretch and both archives' runs (lines 436 to 471), the reward book archive's ledger, sets and asset map (lines
473 to 563), the store's selection, slot records, members and polls and the slot rule (lines 565 to 728), the replay —
the integers, the book, the blocks, the sweep, the queues, the crossings, the latency, the quoting rule, the reward and
the line reader (lines 730 to 1598) — the set, its documents and a day's polls read back one line at a time (lines 1600 to 1858), the downloads (lines 1860 to 1894), the units
held (lines 1896 to 1933), the day's money and L0's reading (lines 2088 to 2160), the rehearsal (lines 2162 to 2248), G-STILL and
NUMBER (lines 2283 to 2347), the modes, the synthetic day and the self-test. One mode a run; each prints its findings with
UTC stamps, its peak memory, whether glibc took its two settings, and its opens refused. A price is an integer of
thousandths and a size of hundredths from the venue's own text; a score is an integer, twelve times `((v − s)/v)²` a
share over `v²` in its units; a share is a pair of integers; the reward a `Decimal` sum of 50-digit quotients; every
position, cost, rebate and mark a `Fraction`; and every printed figure has twelve decimals, half-even. Exit `0` is every
assert held; exit `1` a failed assert, named, or a BLOCK whose message says so. Run with `-O` it refuses to start
(line 58).

---

## 6. Cost

Measured in the Architect's runs of 2026-11-04 under Python 3.12.3 on two cores of an Intel Xeon at 2.10 GHz — the host has one (map §6), and TZ-32's replay ran there at about the rate it ran on the Architect's stand-in: `0.2104` s a megabyte on the host against `0.2157` (TZ-32 report §2.1, TZ-32 §6) — of Appendix A's bytes: the self-test; the rehearsal from a loopback Release server; a stand-in host built from the Architect's exploration — its store's files, an archive record and that server — through `fetch`, `replay`, `rescore` and `score`; `fetch` at the set's full size (§0.4); and the replay of the exploration's 132 cached slots, two days in one process, each with a full day of 43,200 polls read from its file.

| check | population, at its upper bound | measured | at the bound |
|---|---|---|---|
| `selftest` | literals, a synthetic day of two slots, temporary trees | under `1` s of wall clock | fixed |
| `fetch` | 14 candidates: 8 members, each its selection, 96 slot records and 96 reward files of 450 polls; 6 non-members, each its slot records; at most 1,200 markets and ⌈1,200 / 50⌉ × 2 = 48 document requests | `16.0` to `16.8` s of processor at the set's full size, the requests answered by a stand-in | **`30` s**, every read held |
| `rehearse` | the four assets, `47,329,972` bytes, fixed | `5.3` to `5.7` s of replay | **`6` s**; BLOCKED above `120` s |
| `replay` | 768 units, 8 days of 96 slots, each as heavy as the heaviest the Architect measured, `15,989,893` bytes — `12,280,237,824` bytes | `0.1285` to `0.1358` s a megabyte over the exploration's 132 units in three runs; the slowest of its 128 units of 5 MB or more `0.1861`; its four units under 5 MB at most `0.07` s each | **`2,363` s** — the bytes at `0.1861` and `0.1` s a unit; **projected over the set's own bytes after its first 24 units, BLOCKED above `3,000` s** |
| `rescore` | 24 units of the first day at that slot, `383,757,432` bytes | the same rates | **`74` s**; projected after its first 6 units, BLOCKED above `300` s |
| `score` and the rest | 8 day files; `fingerprint`, `number`, `still` and `archive` twice; systemd, git, the ledgers | under `1` s each | about `60` s together |

**Processor at those bounds at most `1 + 30 + 6 + 2,363 + 74 + 60 = 2,534` s**, under `3,600`, so nothing is sampled; **with every fail-fast bound reached together** — the replay's `3,000`, the rescore's `300`, the rehearsal's `120` — and the rest's `91`, `3,511` s, under `3,600`. The replay's `3,000` s is `1.27` times its bound: a set heavier still than every slot at the heaviest and slowest measured still runs; the set's own bytes, about `1,006,278,726` a day (map §2.6), `8,050,229,808` over eight, project to about `1,071` s at `0.1330`.

**Wall clock** from §0.0, at the measured rates: §0 and §3.1 to §3.4 about 15 minutes; the rehearsal and `fetch` minutes each, once the idle stretch opens — at most 900 s apiece to wait for it; the replay's 768 units, each about 3 s of download and replay, held to the idle stretch — up to `575` s of every `900` — about 70 minutes; the rescore and the score minutes more; the report about 30 minutes: **about 2 h 30 min**. At its bounds — the replay at `3,000` s of processor, `fetch` waiting its `10,800` s for an archive that has not moved a day, every memory gate reading five times — about 7 h, so that a run begun by 21:00 UTC ends before the package manager's next morning run. A hold's `7,200` s is the idle stretch's longest wait, the calendar guard and either archive's longest run together twice over; inside the band neither calendar run is met unless the bounds are.

**Disk:** the session's tree at its peak about `160,000,000` bytes (§0.4). **Memory:** every mode's peak as §0.4 gives it, the largest `fetch`'s at the set's full size, `59,879,424`, on which the floor stands.

---

## 7. Validation

| # | check | count |
|---|---|---|
| **V1** | §0.2's fingerprint, at §0.2 and §3.1 | `FINGERPRINT PASS`: revision `2026-11-01-b`; anchors 6 of 6, 4 re-derived; 60 rows, 57 of 57 `frozen` equal, 2 `tracked`, 1 `reported` |
| **V2** | §0.3's host gate, at §0.3 and §3.11 | H1 to H5, the memory and the disk gate — 11 checks; every memory read with its instant; the rest printed |
| **V3** | §0.1's and §3.1's file | 1 of 1 hash asserted at each, lines and bytes; the branch's diff against `origin/main` names exactly one path, `A`, 3,054 lines |
| **V4** | the self-test | `SELFTEST PASS: 42 checks` |
| **V5** | the archive's record, at §3.4 and §3.11 | the ledger's size, SHA-256 and records, every run's line, every complete run's set, the slots the assets reach, the tags; the rehearsal's four assets in their set by name, bytes and SHA-256 |
| **V6** | G-REHEARSAL | `451` lines, SHA-256 `1ab40f4b2a9b4f263e92959dc78a67dc9583731889cce70b22edad59091944cd` |
| **V7** | G-SET | 8 members; every candidate considered with its verdict; each member's markets, slots, files, bytes and polls; the document requests and the members resolved |
| **V8** | the replay, twice | every unit inside the idle stretch or listed; the projection after 24 units against `3,000` s; every day's two files; G-BOOK; no day replayed at the second run |
| **V9** | DETERMINISM | `24 of 24` |
| **V10** | the score, twice | the reading; `reading.json` `unchanged` at the second; the read ledger's lines; the instant §3.1's `ls-remote` printed the instrument's commit on `origin`, before the read ledger's first `fetch` line |
| **V11** | G-STILL | PASS, or what changed named beside §3.11's reads of systemd and the units' journal |
| **V12** | the hook | `opens refused: 0` at every mode; `reward book opens` above `0` at `fetch` alone |
| **V13** | memory | every mode's printed peak against §0.4's floor and its modelled `71,796,447`; every `MemAvailable` read a mode printed; `malloc tuned: True` at every mode |
| **V14** | contract §4.2's self-check | run after the push and the pull request and before the report's commit |
| **V15** | §3.11's closing reads | every read printed |
| **V16** | §9's `reclaim` runs, B-RECLAIM-SCRATCH's and B-RECLAIM-OWN's | files considered, named by a report, kept by name, copied and already held; the store's count after equal to before plus the copies; every line of each `reclaim`'s output quoted unfiltered (map §7 item 119) |
| **V17** | the removals | `git worktree remove` without `--force` exit `0`; `test -e` exit `1` for `/root/tz41-work` and each directory removed; `git worktree list` naming `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else |
| **V18** | the classifier | every block it refused, with the paste handed over, the instant the Boss ran it and the log lines that verify it |

---

## 8. The report

`CryptoReports/TZ-41-l0-our-quote-report.md`, in contract §8's order. **In its first lines:** L0's reading, with every day's money of `pess` and `opt` and its four parts, the least `pess` day and the most `opt` day; G-REHEARSAL, G-SET, G-BOOK and DETERMINISM; the set — candidates considered, members, non-members with their reasons; the instant the instrument's commit reached `origin` beside the read ledger's first line; G-STILL; and every block the classifier refused and who ran it. Beyond what V1 to V18 print: §0.0's clock line; the set as `fetch` printed it — every candidate with its verdict, each member's markets, slots, files, bytes and polls, the document requests and the members resolved; every day's money by variant as `score` printed it, `central`'s barred; the G-BOOK counts by day; **the timing files' summary lines and every unit that ended after second 590**; the archive's record as `I archive` printed it, at both reads, each run off the calendar beside §0.3's reads of systemd; the four units at both reads, memory included; the read ledger's lines; every free-space and `MemAvailable` read with its instant and bound, and every mode's printed peak; §9's counts and removals; and every file the run wrote, by SHA-256. **It prints no single member's, fill's or poll's price, size, rate, competitiveness or outcome** (§2 item 10). **The report is drafted in the primary checkout `/root/btc-5m-twap` before B-RECLAIM-OWN and committed after it**, so the removal of this TZ's tree is in it.

---

## 9. Reclaim — the host left clean (CANON hard rule 15)

**What a file is kept for:** a committed report prints its SHA-256, whole or as a prefix of 16 to 64 hex characters, or it is kept by name: `state.json`, `read-ledger.jsonl` and every file under `logs/`. `reclaim` copies each into `/root/btc-forensics/` as `<tree>--<path with / as -->`, by exclusive create, and verifies its hash; a name already there with the same hash is counted as held, and with another hash is a failed assert (lines 2432 to 2509). The branch worktree is not copied: `reclaim` asserts that `git status --porcelain --ignored` in it prints nothing and that its `HEAD` is its upstream's, so `git worktree remove` needs no `--force`. The report draft in `CryptoReports/` counts as a report. The downloads are removed by each unit as it ends. **No `reclaim`'s output is filtered**: every line it prints is quoted (map §7 item 119). B-RECLAIM-SCRATCH is §3.3.

**B-RECLAIM-OWN**, last, after §3.11 and with the report drafted. **Its output is written to no file; the report quotes it verbatim from the session**, every line of it:

```
cd /root/tz41-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz41-work/wt/research/tz41-l0-our-quote.py reclaim /root/tz41-work
cd /root/btc-5m-twap && git -C /root/btc-5m-twap worktree remove /root/tz41-work/wt; echo "exit=$?"
rm -rf /root/tz41-work; echo "exit=$?"
test -e /root/tz41-work; echo "exit=$?"
git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
find /root/btc-forensics -type f | wc -l
df -B1 --output=source,size,avail /var/lib/btc-recorder
```

`reclaim` must print `RECLAIM PASS` before the removals. **Its paste**, where the classifier refuses any line of it — every step chained to the one before it, the `reclaim`'s `exit=0` reached only after `RECLAIM PASS`; its output goes to the Boss's terminal, the tree its log would be in being removed:

```
(cd /root/tz41-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz41-work/wt/research/tz41-l0-our-quote.py reclaim /root/tz41-work) && cd /root/btc-5m-twap && git -C /root/btc-5m-twap worktree remove /root/tz41-work/wt && rm -rf /root/tz41-work; test -e /root/tz41-work; echo "exit=$?"; git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list; find /root/btc-forensics -type f | wc -l
```

Where the Boss ran it, the Executor verifies it by its own reads — `test -e /root/tz41-work; echo "exit=$?"`, `git -C /root/btc-5m-twap worktree list`, `find /root/btc-forensics -type f | wc -l` and `sha256sum /root/btc-forensics/tz41-work--*`, each copy's hash against the report's — and the report quotes those reads; a refused first attempt is quoted too. The branch `tz-41-l0-our-quote` stays on `origin` and as a local ref; only its working tree goes. **Kept:** the running units' code trees, the capture roots, both archives' state and the forensic store — data and code, never scratch.

---

## 10. Pre-send checks

Performed by the Architect on 2026-11-04 against this file as sent, in a reading separate from its writing — the body was written, read start to end and corrected where it read wrongly (the corrections are named in C7), and this section written after — with the repository at `origin/main` `494f10f90468bc43aef48100d3f354092669eea6` (PR #40's merge over map revision `2026-11-01-b`, `a1c7ba1`; fetched again before sending: no `TZ-41-` file, no report of that number and no `tz-41` branch), the map at that commit (2,033 lines, 536,884 bytes, SHA-256 `1396fa805e9eb72cc36f449c60698822f8d4c2e5314fdd6856f030e07fc46472`) and CANON revision `2026-11-01-b`. Line numbers are those of the file §0.1 extracts for Appendix A, and those of `main` for committed code.

| # | check | result |
|---|---|---|
| **C1** | scope against body | **Repository paths the body names:** `CryptoTZ/TZ-41-l0-our-quote.md`, read by §0.1's script and named by `number`; `CryptoTZ/` and `CryptoReports/`, listed by `number`, every `CryptoReports/*.md` read by `reclaim` for hash tokens (`report_tokens`, line 2432); `SYSTEM-MAP.md` and the 60 rows of its table, read by `fingerprint`, among them `BTC-EXECUTOR-INSTRUCTIONS.md` (`A4`; cited for contract §1, §2, §4.2, §6 and §8), `research/twap-divergence.py`, `research/recorder/recorder.py` and `research/pfair.py` (hashed for `A2`, `A5` and `A6`), `research/tz33-reward-book-capture.py` (cited for lines 179, 190, 192, 767 to 773, 1020 to 1022, 1033 to 1048, 1162 to 1171, 1191 to 1194, 1250 to 1252, 1346 to 1348, 1461, 1562 to 1564 and 1576 to 1577), `research/tz34-rewardbook-archive-timer.py` (lines 302, 605, 607 and 744) and `research/tz28-pairbook-archive-timer.py` (lines 213 and 565 to 567), read by no command but `fingerprint`; `research/tz41-l0-our-quote.py`, written on the branch; `CryptoReports/TZ-41-l0-our-quote-report.md`, written to `main`; `CryptoTZ/TZ-32-our-quoting.md` (§6), `CryptoReports/TZ-32-our-quoting-report.md` (§2.1), `CryptoTZ/TZ-33-reward-book-capture.md` (§1, line 273) and `CryptoReports/TZ-34-rewardbook-archive-timer-report.md` (lines 1509 to 1512), cited and read by no command. **Host paths:** `/root/tz41-work/**` written — `logs/`, `stage/`, `wt/`, `state.json`, `read-ledger.jsonl`, `set.json`, `fetch/`, `days/`, `dl/`, `rehearsal-dl/`, `selftest-tmp/`, `reading.json`, `rehearsal.txt`, `rescore.txt` and the three timing files; `/root/btc-forensics/` written by `reclaim` by exclusive create and counted by `find`; the primary checkout's `.git` for the branch and the worktree and its `CryptoReports/` for the report; `/var/lib/btc-rewardbook/<D0>/` for `D0` from `1793404800` to `1794528000` listed and read by `fetch`; `/var/lib/btc-rewardbook-archive/ledger.jsonl` and `runs/<A>/set.json` read by `archive`, `fetch` and `still`, and `runs/1793263627/set.json` by §0.3's `stat`; `/var/lib/btc-pairbook-archive/ledger.jsonl` read by `still` and `stat`; `/var/lib/btc-recorder` read by `find`, `grep -c` and `df`; the three stores by `du`; `/var/log/apt/history.log` by `grep`; `/proc/meminfo` by the floors and §0.3, `/proc/stat` and each process's `cmdline` and `stat` by `scratch` and `reclaim`; the UUID directories beside the session's own listed, copied from and removed. **Entry points:** the instrument's modes `fingerprint`, `number`, `selftest`, `still`, `scratch`, `archive`, `rehearse`, `fetch`, `replay`, `rescore`, `score` and `reclaim`; §0.1's script; `git`, `gh`, `systemctl show`, `is-active`, `is-enabled` and `list-timers`, `journalctl`, `df`, `du`, `find`, `stat`, `test`, `free`, `cat`, `wc` and `rm -rf`. **Intersections with §2 and their exemptions, by path and by content class:** item 3, the reward book's store — `fetch` alone, its candidate days' files and never a stream file, the named exemption; item 4, both archives' state — `ledger.jsonl` and `set.json` by the modes named; item 2, the recorder's root — §0.3's three reads, named; item 7, requests — `gamma-api` in `fetch`, Release assets in `rehearse`, `replay` and `rescore`, `git` and `gh`, named; **item 10, the class "price, size, rate, competitiveness or outcome"** — `fetch/<D0>.json` (each member's rate, minimum size, maximum spread and rebate coefficient), `fetch/<D0>.polls.jsonl` (every poll's rate and competitiveness), `set.json` (the outcomes), `days/` (each member's figures), `reading.json`, `rehearsal.txt` and `rescore.txt` all carry it: each is written inside `/root/tz41-work/` and printed by nothing but the instrument's modes, which print sums, and hash, size and count commands; §9's byte-for-byte copies of the files the report names by hash are the one exemption, named in item 10; the timing files, `state.json`, `read-ledger.jsonl` and `logs/` carry slots, seconds, bytes, counts and sums and may be printed; item 9, stream assets — a member day's and the rehearsal's four, read by the replay alone; item 8 — the report, the one path pushed to `main`; item 6 — the forensic store by exclusive create alone. **§2's removals** — `/root/tz41-work` and the directories `I scratch` names earlier, under §3.3 and §9. No other intersection. |
| **C2** | origin of every expectation | **Quoted from a committed artifact, at `494f10f`:** revision `2026-11-01-b`, the six anchors, `60`, `57`, `2` and `1` — map §0 and its line 278, the table counted again by the Architect's own parse and every frozen row hashed at `494f10f`, `57 of 57` equal, then by `fingerprint` against the clone, `PASS`; `31612203008` and `e3975b5…` — map §6's host identity (line 1709); `2,370`, the two worktrees, TZ-40's two directories and the live `238335b9…` — map §3 (line 1341); `7,300,000,000` and `100,000,000` — `research/tz33-reward-book-capture.py` lines 190 and 192, `STREAM_FLOOR` and `SLOT_STREAM_MAX`; `58,953,728` and `49,168,384` — map §6, memory (line 1733); `10,239,823,872`, TZ-40's free bytes after its §9 — map §6, disk (line 1716); `201,670,656`, `223,096,832` and `136,404,992` — map §6, memory; `1,002,127,360` — map §7 item 137; the four rehearsal assets' names, bytes and SHA-256 — TZ-34's report lines 1509 to 1512, their sum `47,329,972`; `0.2104` — TZ-32's report §2.1, line 217; `0.2157` — TZ-32 §6, line 714; `1,006,278,726` bytes a day — map §2.6; `θ = 10` — TZ-30's B3 (CANON §1.5); `99 in 100` — TZ-32's G-BOOK rule (map §7 item 121); 01:30:20 and 03:00:20 UTC, the idle stretch's seconds 15 to 590 — map §2.5 (line 946) and §2.6; the 113 ref lines — `git ls-remote origin` on 2026-11-04 at 17:35 UTC, recorded, not gating. **Computed by an implementation independent of the one under test, exactly:** G-REHEARSAL's `451` lines and `1ab40f4b…` — the Architect's reference replay, every quantity a `Fraction`, sharing no code with Appendix A (§4.1); the self-test's synthetic day, `7` lines and `04e6917e…` (`SYN_REF`, line 2675) — the same reference; the powers `0.430467`, `0.663420` and `0.922745` and `2⁻⁸ = 0.00390625` — exact `Fraction` powers, re-derived by the Architect's own arithmetic; `143,592,894` = `2 × ⌈59,879,424 × 58,953,728 / 49,168,384⌉`, exact integer arithmetic on the measured peak and the map's two figures; `48` = `⌈1,200 / 50⌉ × 2`; `12,280,237,824` = `768 × 15,989,893`; `383,757,432` = `24 × 15,989,893`; `2,363` = `⌈12,280,237,824 × 0.1861 / 10⁶ + 76.8⌉`; `74` = `⌈383,757,432 × 0.1861 / 10⁶ + 2.4⌉`. **No expectation depends on a quantity this TZ measures**: the floors, bounds and gates are fixed constants; G-BOOK's `99 in 100` and L0's `θ` are thresholds on what the run measures, not values derived from it. |
| **C3** | shape of every diff | One path, read against `origin/main` `494f10f`: `git cat-file -e 494f10f:research/tz41-l0-our-quote.py` exits `128`, as do the report's path and this TZ's own — **the file is new and replaces no committed line**; `3,054 0` by `--numstat`. No sentence of this TZ calls a change to a committed file additive or speaks of insertions only. |
| **C4** | cost of every check | §6, at the population's upper bound, term by term. **Processor:** `selftest` `1` s against `0.74` s of wall clock measured; `fetch` `30` s at the bound — 14 candidates, 8 of them members of 96 reward files of 450 polls, 1,200 markets and 48 document requests — against `16.0` to `16.8` s measured at the set's full size with the requests answered by a stand-in, the 6 non-members' slot records under `1` s each; `rehearse` `6` s against `5.3` to `5.7` s; `replay` `2,363` s = `12,280,237,824` bytes at `0.1861` s a megabyte, the slowest of the exploration's 128 units of 5 MB or more, and `768 × 0.1` s for the units' fixed cost, the four units under 5 MB having taken at most `0.07` s each, the mean over all 132 `0.1285` to `0.1358` in three runs; `rescore` `74` s = `383,757,432` bytes at the same rate and `24 × 0.1` s; the rest `60` s — `score` twice, `fingerprint`, `number`, `still` and `archive` twice each, under `1` s each measured, and the `git`, `gh`, `systemctl`, `journalctl` and `du` commands: **`1 + 30 + 6 + 2,363 + 74 + 60 = 2,534` s, under `3,600`; nothing is sampled.** **The fail-fast bounds, each with its derivation:** the replay's `3,000` s (`REPLAY_CPU_MAX`, line 111), projected after 24 units over the set's own bytes (`Projection`, lines 2011 to 2027) — `1.27` times its bound of `2,363`; the rescore's `300` s (line 112), projected after 6 units — `4.05` times its `74`; the rehearsal's `120` s (line 113), measured at its end — `20` times its `6`; with the rest's `1 + 30 + 60 = 91`, **`3,000 + 300 + 120 + 91 = 3,511` s, under `3,600`.** The waits, which cost no processor: `fetch`'s `10,800` s for the archive (`WAIT_MAX_S`, line 97, asserted at line 1626); each hold's `7,200` s (`HOLD_MAX_S`, line 126, asserted at line 470); five memory reads `60` s apart at each of the seven starts of a mode that reads the store, a Release or the set, `240` s each at most (lines 400 to 414); six tries of each download and document request, `5 × 2^k` s apart up to `60` s (lines 1863 to 1894 and 1717 to 1736). **Wall clock:** about 2 h 30 min at the measured rates; about 7 h with `fetch`'s wait and the replay's processor bound reached (§6). **Disk** at the same bound: §0.4. |
| **C5** | every count | `60` rows = 57 `frozen` + 2 `tracked` + 1 `reported`, the map's line 278 and the Architect's parse; FINGERPRINT asserts them (`MAP_ROWS`, line 83; lines 2253 to 2280) — `PASS` on the clone at `494f10f`. `42` self-test checks = the `ok` calls of `mode_selftest` (lines 2678 to 3050), counted by a parse of its syntax tree, none inside a loop — `SELFTEST PASS: 42 checks` three times on the bytes sent. `11` host checks = H1 one, H2 two, H3 one, H4 one, H5 four, the memory gate and the disk gate. `8` members, at most `6` non-members, so at most `14` candidates, `1793404800` to `1794528000` (`NEED`, `NONMEMBER_MAX`, `LAST_D0`, lines 93 to 95). `96` slots a day and `768` units over the set; `24` rescored slots (`RESCORE_SLOTS`). `451` lines = 150 markets × 3 variants + 1 line of the book's counts. `48` document requests = `⌈1,200 / 50⌉ × 2`, 1,200 = 8 × 150 the set's markets at most. `113` ref lines = `HEAD` 1, `main` 1, `tz-*` branches 17, pull heads 39, `pairbook-streams-*` tags 39, `rewardbook-streams-*` tags 12, the two annotated tags and their two peeled lines. `2⁻⁸` over the 8 days. `2,370` files in the forensic store, map §3. |
| **C6** | every population | FINGERPRINT: the map's table of 60 rows against the files of the primary checkout. NUMBER: the paths under `CryptoTZ/` and `CryptoReports/` of `origin/main` at each of its two reads. HOST: the host at the instant of each read — its units, files, record, memory and disk; the memory gate the first read at or above the floor, or the fifth. SELFTEST: literals, the synthetic day of two slots, temporary trees and a loopback listener. G-STILL: the four units' `MainPID`, `NRestarts` and `ActiveState` at §3.3 and §3.10, and the pair book archive's ledger records between. ARCHIVE: the reward book archive's ledger and every complete run's `set.json` at each read. G-REHEARSAL: the four assets of `rewardbook-streams-1793263627`, 150 markets, under fixed parameters. G-SET: the candidate days from `1793404800`, in order, until 8 members. G-BOOK: every `book` frame of a member's first token but a subscription's seed, over the 8 member days. DETERMINISM: the first member day's first 24 slots. L0: each of the 8 member days' money, of `pess` and of `opt`, each the sum over that day's members; `central` and the totals barred. The memory floor: one mode's process, measured at the set's full size; `MemAvailable` and free space: the host at each read. RECLAIM: the UUID directories `scratch` names earlier, and the work tree's files the report names or §9 keeps by name. §1's exploration: the 132 slots of 2026-10-28 11:30 to 2026-10-29 20:15 UTC and the Architect's own capture of 2026-10-29 19:45 to 2026-10-30 01:45 UTC. No statistic of this TZ is a calibration claim, and none is read against a label but the markets' outcomes that `fetch` reads for the marks. |
| **C7** | every signature and every behaviour | **Committed code this TZ relies on, read at `494f10f`.** `research/tz33-reward-book-capture.py` — `PING_S = 10` (line 179), the client's `PING` every 10 s; `STREAM_FLOOR = 7300000000` (190) and `SLOT_STREAM_MAX = 100000000` (192); `def member_of(rank, cid, row, gdoc, cdoc):` (767), the member's `condition_id`, `token_ids`, `rate`, `min_size` and `max_spread` (769 to 772), as `members_of` reads them; the selection record `{"day": d0, "attempt": a, "ok": ok, …, "replies": {"file": …, "sha256": sha256_file(rpath), …}` (1020 to 1022) and `def load_selection(ddir):` (1033), the first attempt whose `ok` is `True`, its replies' SHA-256 asserted (1045, 1046) — the rule `selection_of` repeats; every received message a frame, `PONG` among them, `max_gap` the largest wall-clock gap between two (1162 to 1171), and the stream's summary `first_frame_wall_ns`, `last_frame_wall_ns`, `max_gap_ns`, `subscribed_wall_ns` and `cut` (`def summary(self):`, 1191 to 1194), its initial `opened` `False` and `cut` `False` (1250 to 1252); the poll record `condition_id`, `status`, `recv_wall_ns` and `raw` (1346 to 1348), as `polls_of` reads it; the selection's `sha256` the SHA-256 of `select.<a>.json` (1461) and `def selection_id_of(sel):` (1576), `{"day", "attempt", "sha256"}` (1577); the slot record `{"S": s, "day": d0, "index": k, …, "joined_late": joined_late, …, "selection": …, "markets": len(members), …, "stream": stats, "rewards": rew, …, "error": error}` (1562 to 1564) — every field `slot_problem` (lines 610 to 649) reads. `research/tz34-rewardbook-archive-timer.py` — each asset `{"T": d0, "S": s, "k": k, "file": n, "asset": "%d-%s" % (d0, n), "bytes": nbytes, "sha256": h}` (302), `set.json` written under the run's directory (605), the ledger's `set` record with `run`, `tag` and the `sha256` of `set.json`'s bytes (607) and its `complete` record (744) — what `archived_sets` and `asset_map` (lines 495 to 528) read. `research/tz28-pairbook-archive-timer.py` — every ledger record stamped `wall_ns` (213); the `restart` record's `pid`, `stopped` and `NRestarts` (565 to 567) — what `still_reading` (lines 2301 to 2319) chains. **Every behaviour this TZ attributes to Appendix A** is the body of one function, read against it: the rule `Day.decide` (1224 to 1290); the share `Day.share_of` and `Day.parts_of` (1009 to 1071) and `envelope` (931 to 937); the clock `Day.integrate`, `integrate_one`, `flush` and `refresh` (958 to 1007); the fills `Day.fill`, `sweep`, `close_block` and `cross` (1115 to 1221); the polls `Day.poll` (1320 to 1342) and `PollFile` (1671 to 1706); the slots `Day.feed_slot` and `Day.finish` (1504 to 1598); the set `wait_archive`, `day_verdict` and `mode_fetch` (1617 to 1663, 1781 to 1841); the documents `documents` (1753 to 1778), each document's outcome kept and the document dropped; the units `run_unit` (1899 to 1933); the replay `mode_replay` (2030 to 2052), one day held at a time; the reading `day_money` and `l0_reading` (2091 to 2120); the floors `memory_gate` and `floor_check` (393 to 414); the hook `policy` and `_audit` (234 to 295); `reclaim` (2463 to 2509). **Sentences rewritten in this reading:** the header's map items named 122 and 142, which this row does not cite — rewritten to the items it cites; §0.0 called the deferral "not BLOCKED (contract §2)", which contract §2 does not say — it owes no report because nothing has begun (contract §5); §0.4 called the modelled host peak "the larger of map §7 item 131's two" as if the host had a peak of this code — it has none, and the model stands in for it; §1 quoted TZ-33 §1 as "no delay", the map's phrase — TZ-33's text, line 273, is "`seconds_delay` absent or `0`", and both are cited; §1 and §4.1 counted the reference's three slots by their 1,350 polls — 1,157 of them served, the ones replayed; §1 put the 10-s heartbeat on the venue — the reward book sends `PING` and stores the venue's `PONG` (TZ-33, lines 179 and 1162 to 1171); §2 put the removals under §9 alone — §3.3 and §9; §3.1's commands had no logs — each is named; §3.11 read the advisor's unit's journal, which can carry a coin or a price — dropped, systemd's own lines on the unit read by §0.3's block instead; §6 cited TZ-32's host rate from its report's §2.7 — it is §2.1, line 217; §6 and C4 stood the replay's bound on the slowest unit's rate, `0.2047`, a 144,076-byte unit whose rate is its fixed cost and read `0.253` in a later run — rewritten on the slowest of the 128 units of 5 MB or more, `0.1861`, with `0.1` s a unit for the fixed cost: `2,514` s became `2,363` and the rescore's `79` became `74`; C4 put the hold's assert at line 469 — it is 470 — and counted six starts of the modes that read the floor — they are seven. **Appendix A rewritten in this preparation, each change measured and the outputs compared:** `documents` kept every member's document until its last request — it keeps each one's outcome; `mode_fetch` held one day's polls while it read the next — dropping them first took `fetch` at the set's full size from `78,913,536` bytes to `59,879,424`; `mode_replay` held one day's state while it replayed the next — it drops it; `polls_read` held a day's 43,200 polls in memory — `PollFile` reads them one line at a time, which took a day's replay from `66,207,744` bytes to `56,066,048` (map §7 item 123); the stand-in's day files, slot lines, rescore lines and reading are byte for byte the earlier code's, and the reference's 451 lines equal through both readers; `floor_check` read memory once — it reads five times, 60 s apart (map §7 item 137); `MEM_FLOOR` `117,293,056` became `143,592,894` on the set-size peak at TZ-37's ratio (item 131); `WAIT_MAX_S` `21,600` became `10,800`, the band starting six hours after the archive's run; and the number, the map revision and its rows. |
| **C8** | every cross-reference | Resolved by reading the text referenced. **Map `2026-11-01-b` at `494f10f`:** §0's anchors and its table of 60 rows, 57 / 2 / 1 (line 278: "A later TZ's `fingerprint` expects `60`, `57` and `2026-11-01-b`"); §1's record of refs, its last TZ-40's audit of 106 lines (a difference from it is recorded, not blocking, §0.5); §2.5 for the pair book's archive at `03:00:20` UTC and its idle stretch, seconds 15 to 590 of a window (lines 943 to 946); §2.6 for the reward book's store, its slot records, its archive's calendar run at `01:30:20` UTC and its sets and assets, `STREAM_FLOOR`, its rate `1,006,278,726` bytes a day and the reserve this TZ ends (lines 986 to 1054); §3's `2,370` files in the forensic store, the two worktrees, TZ-40's two directories and the live `238335b9…` (line 1341), and the code trees no TZ removes (lines 1342 to 1361); §6's rows host identity (1709), language — `/root/tz04a-env`, Python 3.12.3 (1710) — git remote — the push through `gh`'s credential helper (1713) — egress (1714), venue edge — the `User-Agent` (1715) — disk (1716), process supervision (1732), memory (1733), both sandbox limits (1736 and 1738) and the harness (1739); §7 items 115 and 129 (runs off the calendar after a reload), 118 (no file of the work tree printed but by a command the TZ names), 119 (no `reclaim` output filtered), 120 (the package manager restarts capture units; a G-STILL names the cause), 121 (G-BOOK on the touch at 99 in 100), 123 (a mode that holds the set measured at its size before its floor is fixed), 124 (a block handed to the Boss: one line, chained, appended under a `date -u` line), 125, 131 (the floor's peak, the larger of two), 132 (no step of the Boss's before `EXECUTE`), 136 (`NRestarts` a count since the unit's start), 137 (a memory floor read again before blocking), 138 (ONE paste, a refused block handed over unchanged), 139 and 141 (the header names the sections this row cites — copied there), 140 (a handed-over block holds back only the steps that read what it changes), 143 (bands from 07:30 UTC, clear of the package manager's run), 144 (no step of a paste run again), 145 (a mode timed for its host peak — this instrument prints its own) and 146. **CANON `2026-11-01-b`:** PART II's L track and L0's question, its rule that near-resolution and live-event markets are excluded, that a mark is not a label and that the Architect's snapshot is excluded by time; §1.5 for TZ-30's `10` USDC and TZ-32's W1; §1.6 for the condition a later quote must meet, "a quoting rule whose fills do not hang on a queue place the streams cannot show"; §1.7 for the reward formula and the rebate schedule, read and not measured; PART III's hard rules 2, 5, 11, 13, 14 and 15; PART VI's fourth rule — a set the Architect has read is an exploration, and §1 says which. **Contract `437b45ea`:** §1 steps 1 to 5, §2, §4.1, §4.2, §6 and §8. **Other TZs:** TZ-30's θ and stream rule; TZ-32 §1's match rule and §6's `0.2157`, its report §2.1's `0.2104`; TZ-33 §1, line 273, `seconds_delay` absent or `0`, the selection's "no delay" in map §2.6; TZ-34's report, lines 1509 to 1512, for the rehearsal's assets. No quotation of the Boss's words appears in this TZ. |

**Six checks could not be performed from this session**, and each is converted into a mechanical condition the Executor evaluates and BLOCKS on (CANON hard rule 13): the host's own state — free space, memory, units, interpreter, both archives' ledgers — §0.3; the set's days on the host, which only `fetch` may read, and the archive's assets of them — G-SET, with every candidate disclosed; the host's reach of `github.com` and `gamma-api.polymarket.com` under this TZ's headers — G-REHEARSAL downloads before any member is read, and every request is tried six times and BLOCKS after; the host's processor rate for this code — the projection after 24 units BLOCKS above `3,000` s; the host's memory peaks for this code — every mode prints its own peak beside the floor, and the floor is read at every mode's start; and the harness's permission classifier — each refused block handed over unchanged with its paste (§3.3, §9).

---

## Appendix A — the instrument, byte for byte

`research/tz41-l0-our-quote.py`, 3,054 lines, 152,763 bytes, SHA-256 `e4867068a5d1620d5deab981f68c1ae60b97d364ab00f31895a8e402d479ce16`. §0.1's script extracts it from the fence below and asserts its hash.

```python file=research/tz41-l0-our-quote.py
#!/usr/bin/env python3
"""TZ-41 - L0, our quote on the venue's reward markets: does a two-sided quote of ours, each side one tick inside the
touch and alone at its price, simulated on the reward book's streams, collect more in liquidity rewards and maker
rebates than its fills lose?

    fingerprint       contract section 1 steps 3 and 4, asserted: the map's revision, anchors and rows
    number            CANON hard rule 2: no other TZ-41 specification or report on origin/main
    selftest          every rule of this file, on literals, on synthetic streams and on temporary trees
    still             the five units' MainPID, NRestarts and ActiveState: the first run records them, the second
                      compares, the pair book archive's own restarts read from its ledger (G-STILL)
    scratch OWN       the UUID directories beside OWN, this session's, each named live or earlier
    archive           the reward book archive's ledger and the set.json of every complete run, read and printed
    rehearse          the replay over four of the archive's first assets under fixed parameters, every unit held,
                      against the Architect's independent replay (G-REHEARSAL)
    fetch             the candidate days from 2026-10-31, once the archive has moved them: each day's selection,
                      slot records, polls and fee schedules, the members' documents, and the set (G-SET)
    replay            every member day's slots downloaded, replayed and removed, every unit held; the days' money
                      on disk (G-BOOK)
    rescore           the set's first day replayed again, from a second download (DETERMINISM)
    score             L0's reading from the replay's day files
    reclaim TREE...   section 9

Its own code is the whole of L0's arithmetic - the replay of a day's streams, every member market's book rebuilt, our
quote placed, queued, filled and cancelled at venue time, its reward share by the venue's published formula, its
rebate and its fills marked to the market - and the reward book's record, the downloads held to the pair book's idle
stretch and G-STILL. Its requests: gamma-api.polymarket.com, the members' documents, in fetch alone; downloads of
Release assets from github.com; and git against origin. An audit hook refuses every open, listing, request and process
TZ-41 section 2 does not give the running mode. It writes under /root/tz41-work/ and, in reclaim, new files in
/root/btc-forensics/ by exclusive create. Exit 0: every assert of the mode held. Exit 1: an assert failed, and its
message names it. Run it with the recorder's interpreter, /root/tz04a-env.

Written for CryptoTZ/TZ-41-l0-our-quote.md. The TZ is the specification.
"""

import bisect
import collections
import ctypes
import datetime
import decimal
import gzip
import hashlib
import heapq
import http.client
import json
import os
import re
import resource
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from decimal import Decimal as D
from fractions import Fraction as Fr

if not __debug__:
    sys.stderr.write("tz41: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(2)


def _malloc_tune():
    """glibc's mmap threshold at 128 KiB and two arenas, as TZ-23's and TZ-33's instruments fix them."""
    try:
        libc = ctypes.CDLL("libc.so.6")
        return libc.mallopt(-3, 131072) == 1 and libc.mallopt(-8, 2) == 1
    except OSError:
        return False


MALLOC_TUNED = _malloc_tune()
HERE = os.path.dirname(os.path.abspath(__file__))

# ---- the TZ's constants: none of them is measured by this run -----------------------------------------------

MAP_REVISION = "2026-11-01-b"
ANCHORS = {"A1": "229a944f2d51", "A2": "6c5089330629",
           "A3": "0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable",
           "A4": "437b45ea196b", "A5": "0f6c90451cbd", "A6": "729f0bcdbee3"}
ANCHOR_FILES = {"A2": "research/twap-divergence.py", "A4": "BTC-EXECUTOR-INSTRUCTIONS.md",
                "A5": "research/recorder/recorder.py", "A6": "research/pfair.py"}
MAP_ROWS = {"frozen": 57, "tracked": 2, "reported": 1}
ROW = re.compile(r"^\| `([^`]+)` \| ([0-9,]+|—) \| ([0-9,]+|—) \| (frozen|tracked|reported) \| "
                 r"(?:`([0-9a-f]{64})`|[^|]*) \|$", re.M)
ANCHOR_ROW = re.compile(r"^\| `(A[0-9])` — [^|]*\| `([^`]+)` \|$", re.M)
NUMBER = "TZ-41-"

DAY = 86400
SLOT = 900
SLOTS_A_DAY = 96
FIRST_D0 = 1793404800        # 2026-10-31 00:00:00 UTC: the first candidate day, after every read of the exploration
NEED = 8                     # member days: the reading's eight blocks
NONMEMBER_MAX = 6            # the walk is BLOCKED past six non-member days before the eighth member
LAST_D0 = FIRST_D0 + (NEED + NONMEMBER_MAX - 1) * DAY    # 1794528000, 2026-11-13: the fourteenth candidate
GAP_MAX_NS = 15 * 10 ** 9    # no gap between received frames of a slot above 15 s
WAIT_MAX_S = 10800           # fetch waits at most three hours for the archive to reach a candidate day

# The quoting rule (TZ-41 section 1): one tick inside each side of the touch, where the touch is five ticks wide or
# more; the reward band; the position cap in minimum-size clips; the one-way latency.
LATENCY_MS = 50
CAP_CLIPS = 1
SPREAD_TICKS = 5
# (name, rule, first in its level's queue, a crossing order a taker, the competitors' score): the first two are
# gated - pess, every assumption against us, for EARN; opt, every assumption for us, for NO EARN - central barred.
VARIANTS = (("pess", "alone", False, True, "pess"), ("opt", "alone", True, False, "opt"),
            ("central", "alone", False, True, "venue"))
GATED = ("pess", "opt")
THETA = D("10")              # USDC a day: EARN where every pess day reaches it, NO EARN where no opt day does
BOOK_EQUAL_MIN = Fr(99, 100) # G-BOOK: the rebuilt touch equals the venue's own at 99 in 100 of its book frames
REPLAY_CPU_MAX = 3000        # processor seconds the set's replay may take, projected after its first 24 units
RESCORE_CPU_MAX = 300
REHEARSAL_CPU_MAX = 120
PROJECT_AFTER = 24
UNIT_BUDGET_S = 45           # a unit's budget beside its download: replay and deletion
DL_RATE = 2000000            # bytes a second a download is budgeted at, TZ-28's
DL_TRIES = 6
DOC_BUDGET_S = 120           # a document request's budget in the idle stretch
STORE_BUDGET_S = 60          # a candidate day's read of the store's files, its selection, slots and polls
DOC_CHUNK = 50               # condition ids a gamma request carries: TZ-33's batch
IDLE = (15, 590)             # the pair book's idle stretch: a unit starts at second 15 or later, ends by 590
CALENDAR = ((5420, "the reward book archive's calendar run at 01:30:20 UTC"),
            (10820, "the pair book archive's calendar run at 03:00:20 UTC"))
CALENDAR_LEAD_S = 60
RUNNING = ("active", "activating", "deactivating", "reloading", "refreshing")
HOLD_MAX_S = 7200
MEM_FLOOR = 143592894        # MemAvailable: twice the largest peak of any mode the Architect measured, modelled at
#                              the host's ratio TZ-37 measured, 58,953,728 / 49,168,384 (section 0.4)
MEM_RETRY_S = 60             # a MemAvailable read below the floor is read again this much later,
MEM_READS = 5                # five reads at most
DISK_FLOOR = 7400000000      # free bytes on /dev/vda2 once a unit's download lands: the reward book's STREAM_FLOOR,
#                              7,300,000,000, and one slot of its streams at the cut, 100,000,000 (section 0.4)
DISK_GATE = 7800000000       # free bytes at a mode's start: DISK_FLOOR and this session's tree twice over (section 0.4)

UA = "btc-5m-twap-tz41"
DL_HEADERS = {"User-Agent": UA, "Accept": "application/octet-stream"}
GAMMA_HEADERS = {"User-Agent": UA, "Accept": "application/json"}
REPO = "seahomebatumi-ai/btc-5m-twap"
DL_URL = "https://github.com/" + REPO + "/releases/download/%s/%s"
DL_HOSTS = ("github.com", "release-assets.githubusercontent.com", "objects.githubusercontent.com")
GAMMA_HOST = "gamma-api.polymarket.com"
GAMMA_URL = "https://gamma-api.polymarket.com/markets?%s"
ASSET_RE = re.compile(r"([0-9]{10})-(([0-9]{10})\.([0-9]+)\.stream\.jsonl\.gz)")
SLOT_FILE_RE = re.compile(r"([0-9]{10})\.([0-9]+)\.(stream\.jsonl\.gz|rewards\.jsonl\.gz|slot\.json)")
SELECT_FILE_RE = re.compile(r"select\.([0-9]+)\.(json|replies\.jsonl\.gz)")
CID_RE = re.compile(r"0x[0-9a-f]{64}")
TOKEN_RE = re.compile(r"[0-9]{1,100}")
SHA_RE = re.compile(r"[0-9a-f]{64}")

# G-REHEARSAL: four of the reward book archive's first Release's assets, their bytes and SHA-256 as TZ-34's report
# printed them, replayed as one stand-in hour under fixed parameters (TZ-41 section 4.1)
REHEARSAL_TAG = "rewardbook-streams-1793263627"
REHEARSAL_D0 = 1793232000
REHEARSAL_ASSETS = (
    ("1793232000-1793232000.0.stream.jsonl.gz", 11579610, "bafa2d5e0ed6293ab1a4a8466431db62100413766eac72c5c6a13d18a591271f"),
    ("1793232000-1793232900.0.stream.jsonl.gz", 10715152, "46076896c752257334186cf66c256d6c76685dccd274dbd7f6ab9d1b5917e370"),
    ("1793232000-1793233800.0.stream.jsonl.gz", 11443056, "2881148ced021d3c865fdc976183de94869fbe4876f9e70d3b6747394834a4a9"),
    ("1793232000-1793234700.0.stream.jsonl.gz", 13592154, "ca030bcb13717dd12c41d485f8abf83c1f8c4ac92fbef2625cbd6a6aecca9496"))
REHEARSAL_PARAMS = {"ms": 5000, "vu": 90, "rate": Fr(100), "fee": Fr(0)}   # 50 shares, 4.5 cents, 100 a day, no fee
REF = {"lines": 451, "digest": "1ab40f4b2a9b4f263e92959dc78a67dc9583731889cce70b22edad59091944cd"}

WORK = "/root/tz41-work"
WT = WORK + "/wt"
STATE = WORK + "/state.json"
LEDGER = WORK + "/read-ledger.jsonl"
PRIMARY = "/root/btc-5m-twap"
REPORTS = PRIMARY + "/CryptoReports"
FORENSICS = "/root/btc-forensics"
BRANCH = "tz-41-l0-our-quote"
RB_ROOT = "/var/lib/btc-rewardbook"
RB_ARCHIVE = "/var/lib/btc-rewardbook-archive"
RB_LEDGER = RB_ARCHIVE + "/ledger.jsonl"
PB_ARCHIVE = "/var/lib/btc-pairbook-archive"
PB_LEDGER = PB_ARCHIVE + "/ledger.jsonl"
RECORDER = "/var/lib/btc-recorder"
PAIRBOOK = "/var/lib/btc-pairbook"
CHAINBOOK = "/var/lib/btc-chainbook"
ADVISOR = "/var/lib/adv3-bot"
ADVISOR_ETC = "/etc/adv3-bot"
UNITS = {"recorder": "btc-recorder.service", "pairbook": "btc-pairbook.service", "rewardbook": "btc-rewardbook.service",
         "advisor": "adv3-bot.service"}
ARCHIVES = {"pairbook": ("btc-pairbook-archive.service", "btc-pairbook-archive.timer"),
            "rewardbook": ("btc-rewardbook-archive.service", "btc-rewardbook-archive.timer")}
SHOW_ENV = {"TZ": "UTC", "LC_ALL": "C", "SYSTEMD_COLORS": "0", "SYSTEMD_PAGER": ""}
UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
TOKEN = re.compile(r"[0-9a-f]{16,64}")
LIVE_S = 60
PYFILE = "tz41-l0-our-quote.py"

# ---- the audit hook: TZ-41 section 2's reads, writes, requests and processes -----------------------------

MODE = [None]
REFUSED = []
COUNTS = collections.Counter()
WRITE_FLAGS = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC
RB_SET = re.compile(re.escape(RB_ARCHIVE) + r"/runs/([0-9]{10})/set\.json")
RB_DAY = re.compile(re.escape(RB_ROOT) + r"/([0-9]{10})")
RB_FILE = re.compile(re.escape(RB_ROOT) + r"/([0-9]{10})/([0-9]{10}\.[0-9]+\.(?:slot\.json|rewards\.jsonl\.gz)|"
                     r"select\.[0-9]+\.(?:json|replies\.jsonl\.gz))")
PROCESSES = {"git", "systemctl", "stat"}
SELFTEST_HOSTS = ("127.0.0.1",)


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


def day_in_span(d0):
    return FIRST_D0 <= d0 <= LAST_D0 and (d0 - FIRST_D0) % DAY == 0


def policy(mode, event, args):
    """None where TZ-41 section 2 allows the event in this mode; otherwise the reason it is refused."""
    if event == "urllib.Request":
        host = urllib.parse.urlsplit(args[0]).hostname if args and isinstance(args[0], str) else None
        if mode in ("rehearse", "replay", "rescore") and host in DL_HOSTS:
            return None
        if mode == "fetch" and host == GAMMA_HOST:
            return None
        if mode == "selftest" and host in SELFTEST_HOSTS:
            return None
        return "a request to %s" % host
    if event == "subprocess.Popen":
        exe = args[0] if args and args[0] else (args[1][0] if len(args) > 1 and args[1] else "")
        exe = os.path.basename(os.fsdecode(exe) if isinstance(exe, bytes) else str(exe))
        return None if exe in PROCESSES else "a process %s" % exe
    p = _path(args[0]) if args else None
    if p is None:
        return None
    if event in ("os.listdir", "os.scandir"):
        if any(_under(p, r) for r in (RECORDER, CHAINBOOK, PAIRBOOK, PB_ARCHIVE, RB_ARCHIVE, ADVISOR, ADVISOR_ETC)):
            return "a listing under a capture root or an archive's state"
        if _under(p, RB_ROOT):
            m = RB_DAY.fullmatch(p)
            if mode == "fetch" and m is not None and day_in_span(int(m.group(1))):
                return None
            return "a listing under the reward book's root"
        return None
    wm, fl = (args[1] if len(args) > 1 else None), (args[2] if len(args) > 2 else None)
    w = _writing(wm, fl)
    if any(_under(p, r) for r in (RECORDER, CHAINBOOK, PAIRBOOK, ADVISOR, ADVISOR_ETC)):
        return "an open under a capture root or the advisor's"
    if _under(p, RB_ROOT):
        m = RB_FILE.fullmatch(p)
        if not w and mode == "fetch" and m is not None and day_in_span(int(m.group(1))):
            return None
        return "an open under the reward book's root"
    if _under(p, RB_ARCHIVE):
        if not w and mode in ("archive", "fetch", "still") and (p == RB_LEDGER or RB_SET.fullmatch(p)):
            return None
        return "an open under the reward book archive's state"
    if _under(p, PB_ARCHIVE):
        if not w and mode == "still" and p == PB_LEDGER:
            return None
        return "an open under the pair book archive's state"
    if _under(p, FORENSICS):
        if w:
            return None if mode == "reclaim" and _exclusive(wm, fl) else "a write into the forensic store"
        return None
    if w and not _under(p, WORK):
        return "a write outside the work tree"
    return None


def _audit(event, args):
    if event not in ("open", "os.listdir", "os.scandir", "urllib.Request", "subprocess.Popen"):
        return
    why = policy(MODE[0], event, args)
    if why is None and event == "open" and _under(_path(args[0]) or "", RB_ROOT):
        COUNTS["reward book opens"] += 1
    if why is not None:
        REFUSED.append((event, str(args[0]) if args else ""))
        raise GuardError("%s refused in mode %s, %s: %r" % (event, MODE[0], why, args[0] if args else None))


sys.addaudithook(_audit)

# ---- small helpers ----------------------------------------------------------------------------------------


def out(msg):
    sys.stdout.write("[%s] %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    sys.stdout.flush()


def utc(t):
    return datetime.datetime.fromtimestamp(float(t), datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


C50 = decimal.Context(prec=50)        # every reward term and sum at 50 significant digits
Q12 = D("0.000000000001")


def q12(x):
    """A figure for print, half-even to 12 places; every sum and comparison is made on the exact figure."""
    if isinstance(x, Fr):
        x = C50.divide(D(x.numerator), D(x.denominator))
    s = format(D(x).quantize(Q12, rounding=decimal.ROUND_HALF_EVEN), "f")
    return "0.000000000000" if s.lstrip("-") == "0.000000000000" else s


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def write_atomic(path, data):
    tmp = path + ".tmp"
    with open(tmp, "wb") as fh:
        fh.write(data)
    os.replace(tmp, path)


def write_once(path, data):
    """The first run writes; a later run must produce the same bytes (contract section 6)."""
    if os.path.exists(path):
        got = sha256_file(path)
        assert got == sha256_bytes(data), "determinism: %s differs from the first run" % path
        out("unchanged %s sha256 %s" % (path, got))
        return got
    write_atomic(path, data)
    out("wrote %s %d bytes sha256 %s" % (path, len(data), sha256_bytes(data)))
    return sha256_bytes(data)


def dumps(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), default=_dec) + "\n"


def _dec(o):
    if isinstance(o, D):
        return format(o, "f")
    if isinstance(o, Fr):
        return "%d/%d" % (o.numerator, o.denominator)
    raise TypeError(type(o))


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh, parse_float=D)


def load_state():
    return load_json(STATE) if os.path.exists(STATE) else {}


def save_state(st):
    write_atomic(STATE, (json.dumps(st, sort_keys=True, indent=1, default=_dec) + "\n").encode("utf-8"))


def mem_available():
    with open("/proc/meminfo", encoding="ascii") as fh:
        for ln in fh:
            if ln.startswith("MemAvailable:"):
                return int(ln.split()[1]) * 1024
    raise AssertionError("no MemAvailable in /proc/meminfo")


def free_bytes(path="/var/lib"):
    st = os.statvfs(path)
    return st.f_bavail * st.f_frsize


def memory_gate(reads):
    """MemAvailable at a mode's reads, in order: the first, and one every MEM_RETRY_S after it while every read before
    fell below MEM_FLOOR, MEM_READS at most (map section 7 item 137). The last decides: (passes, it). Pure."""
    assert 1 <= len(reads) <= MEM_READS and all(r < MEM_FLOOR for r in reads[:-1]), reads
    return reads[-1] >= MEM_FLOOR, reads[-1]


def floor_check(read=None, sleep=None, freef=None):
    """Before a mode that reads the venue, the archive's Releases or the set: glibc's two settings, the memory floor -
    a read below it read again every MEM_RETRY_S, MEM_READS reads at most, the last deciding - and the disk floor."""
    read, sleep, freef = read or mem_available, sleep or time.sleep, freef or free_bytes
    assert MALLOC_TUNED, "BLOCKED: glibc did not take the mmap threshold and the arena count"
    reads, free = [read()], freef()
    out("MemAvailable %d bytes, floor %d; free %d bytes, floor %d" % (reads[0], MEM_FLOOR, free, DISK_GATE))
    while reads[-1] < MEM_FLOOR and len(reads) < MEM_READS:
        sleep(MEM_RETRY_S)
        reads.append(read())
        out("MemAvailable read %d of %d at most, %d s after a read below the floor: %d bytes" % (
            len(reads), MEM_READS, MEM_RETRY_S, reads[-1]))
    passes, final = memory_gate(reads)
    assert passes, "BLOCKED: MemAvailable %d bytes at read %d, every read below %d" % (final, len(reads), MEM_FLOOR)
    assert free >= DISK_GATE, "BLOCKED: %d bytes free, below %d" % (free, DISK_GATE)


def show(unit, props):
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


def is_active(unit):
    cp = subprocess.run(["systemctl", "is-active", unit], capture_output=True, text=True)
    return cp.stdout.strip()

# ---- the clock: the pair book's idle stretch and both archives' runs -----------------------------------------


def archives_state():
    return {k: is_active(svc) for k, (svc, _timer) in sorted(ARCHIVES.items())}


def quiet(now, budget, state_of=None):
    """None where a unit of `budget` seconds may start at `now`; otherwise why not: it starts inside the pair book's
    idle stretch and ends by its second 590, never near or during either archive's run."""
    state_of = state_of or archives_state
    p = int(now) % SLOT
    if not IDLE[0] <= p <= IDLE[1] - budget:
        return "second %d of the window" % p
    d = int(now) % DAY
    for at, what in CALENDAR:
        if at - budget - CALENDAR_LEAD_S <= d <= at + CALENDAR_LEAD_S:
            return what
    for k, st in sorted(state_of().items()):
        if st in RUNNING:
            return "the %s archive's service is %s" % (k, st)
    return None


def hold(budget, clock=None, sleep=None, state_of=None):
    """Until a unit of `budget` seconds may start; returns that instant and the seconds waited."""
    clock, sleep = clock or time.time, sleep or time.sleep
    assert budget <= IDLE[1] - IDLE[0], "a unit of %d s fits no idle stretch" % budget
    t0 = clock()
    while True:
        now = clock()
        why = quiet(now, budget, state_of)
        if why is None:
            return now, now - t0
        assert now - t0 <= HOLD_MAX_S, "BLOCKED: held %.0f s, the last reason %s" % (now - t0, why)
        sleep(1.0)

# ---- the reward book archive's record: its ledger, every complete run's set.json, every stream file's asset -------


def ledger_records(path):
    with open(path, "rb") as fh:
        raw = fh.read()
    lines = raw.split(b"\n")
    tail = lines.pop()
    return raw, [json.loads(ln) for ln in lines if ln.strip()], tail


def runs_of(recs):
    runs, order = {}, []
    for r in recs:
        a = r.get("run")
        if a not in runs:
            runs[a] = []
            order.append(a)
        runs[a].append(r)
    return runs, order


def archived_sets(recs, state=None):
    """Every run whose ledger holds a complete record: its set.json, asserted by the SHA-256 its last set record
    carries, its tag, assets and counts against that record."""
    state = state or RB_ARCHIVE
    runs, order = runs_of(recs)
    found = []
    for a in order:
        if "complete" not in [r.get("event") for r in runs[a]]:
            continue
        sets = [r for r in runs[a] if r.get("event") == "set"]
        assert sets and isinstance(a, int), "run %r: complete without a set record" % a
        with open(os.path.join(state, "runs", str(a), "set.json"), "rb") as fh:
            raw = fh.read()
        sha = sha256_bytes(raw)
        assert sha == sets[-1]["sha256"], "run %d: set.json sha256 %s, its set record %s" % (a, sha, sets[-1]["sha256"])
        doc = json.loads(raw)
        assert doc["tag"] == sets[-1]["tag"] and doc["assets_n"] == sets[-1]["assets_n"] == len(doc["assets"]) \
            and doc["bytes_total"] == sets[-1]["bytes_total"], "run %d: set.json against its set record" % a
        found.append({"run": a, "tag": doc["tag"], "sha256": sha, "doc": doc})
    return found


def asset_map(sets):
    """(D0, file) -> {tag, asset, bytes, sha256}, every stream file once; a file in two sets is a failed assert."""
    m = {}
    for s in sets:
        for x in s["doc"]["assets"]:
            mt = ASSET_RE.fullmatch(x["asset"])
            assert mt and int(mt.group(1)) == x["T"] and mt.group(2) == x["file"] and int(mt.group(3)) == x["S"] \
                and int(mt.group(4)) == x["k"] and x["T"] == x["S"] // DAY * DAY, "an asset named %r" % x["asset"]
            key = (x["T"], x["file"])
            assert key not in m, "%s in two sets" % x["asset"]
            m[key] = {"tag": s["tag"], "asset": x["asset"], "bytes": x["bytes"], "sha256": x["sha256"]}
    return m


def archived_to(state=None):
    """The asset map of every complete run and the last slot its assets reach."""
    state = state or RB_ARCHIVE
    _raw, recs, _tail = ledger_records(os.path.join(state, "ledger.jsonl"))
    amap = asset_map(archived_sets(recs, state))
    last = max(int(ASSET_RE.fullmatch(v["asset"]).group(3)) for v in amap.values()) if amap else 0
    return amap, last


def ledger_summary(recs):
    """The archive's runs from its own records: each run's set and terminal record, and whether it began on the
    calendar; whether the archive is halted."""
    runs, order = runs_of(recs)
    lines = []
    for a in order:
        rs = runs[a]
        ev = [r.get("event") for r in rs]
        term = [e for e in ev if e in ("complete", "empty", "halt")]
        sec = a % DAY if isinstance(a, int) else None
        when = "calendar" if sec == CALENDAR[0][0] else ("off-calendar, second %s of the day" % sec)
        parts = ["run %s %s, %s: %d records; terminal %s" % (a, utc(a) if isinstance(a, int) else "-", when, len(rs),
                                                            term[-1] if term else "none")]
        for r in [r for r in rs if r.get("event") == "set"][-1:]:
            parts.append("set %s: %s files, %s bytes, slots %s to %s" % (
                r.get("tag"), r.get("assets_n"), r.get("bytes_total"), r.get("first_S"), r.get("last_S")))
        for r in rs:
            if r.get("event") in ("deferred", "halt", "refused", "timer-disabled"):
                parts.append("%s in %s: %s" % (r.get("event"), r.get("phase"), r.get("reason", r.get("exit"))))
        lines.append("; ".join(parts))
    flags = [r.get("event") for r in recs if r.get("event") in ("halt", "clear")]
    return {"runs": order, "lines": lines, "halted": bool(flags) and flags[-1] == "halt",
            "terminal": {a: [r.get("event") for r in runs[a] if r.get("event") in ("complete", "empty", "halt")]
                         for a in order}}

# ---- the reward book's store: a day's selection, slot records and polls (fetch alone reads them) -----------------


def day_dir(d0, root=None):
    return os.path.join(root or RB_ROOT, str(d0))


def selection_of(d0, root=None):
    """The day's first ok attempt and its replies' bytes, asserted against its record (TZ-33's load_selection rule),
    with the SHA-256 of its select.<a>.json; None where the day holds none."""
    ddir = day_dir(d0, root)
    if not os.path.isdir(ddir):
        return None
    a = 0
    while True:
        jp, rp = (os.path.join(ddir, "select.%d.json" % a), os.path.join(ddir, "select.%d.replies.jsonl.gz" % a))
        if not os.path.exists(jp):
            if os.path.exists(rp):
                a += 1
                continue
            return None
        with open(jp, "rb") as fh:
            jraw = fh.read()
        rec = json.loads(jraw)
        if rec.get("ok") is True:
            with open(rp, "rb") as fh:
                rraw = fh.read()
            assert sha256_bytes(rraw) == rec["replies"]["sha256"], "%s: replies differ from their record" % rp
            return {"attempt": a, "rec": rec, "sha256": sha256_bytes(jraw), "replies": rraw}
        a += 1


def slot_records(d0, root=None):
    """S -> [slot.json of k = 0, 1, ...] for every slot of the day the store holds a record of, by its listing."""
    by = {}
    for name in sorted(os.listdir(day_dir(d0, root))):
        m = SLOT_FILE_RE.fullmatch(name)
        if m is None or m.group(3) != "slot.json":
            continue
        s, k = int(m.group(1)), int(m.group(2))
        with open(os.path.join(day_dir(d0, root), name), "rb") as fh:
            by.setdefault(s, {})[k] = json.loads(fh.read())
    return {s: [v[k] for k in sorted(v)] for s, v in by.items()}


def slot_problem(s, recs, sel_sha, n_members, assets, d0):
    """The first rule slot s fails, or None: its records consecutive from k = 0, each of the day's selection and
    every member, its stream opened and not cut, the first subscribed by S, the last's last frame at or after S + 900,
    no gap above 15 s within a file or between two, and every stream file in the archive's assets."""
    if not recs:
        return "no slot record"
    files = []
    for k, sj in enumerate(recs):
        if sj.get("S") != s or sj.get("index") != k or sj.get("day") != d0:
            return "records: index %d" % k
        if (sj.get("selection") or {}).get("sha256") != sel_sha or sj.get("markets") != n_members:
            return "records: another selection"
        if sj.get("error") is not None:
            return "records: an error"
        st = sj.get("stream") or {}
        if st.get("opened") is not True or st.get("off_reason") is not None or st.get("file") is None:
            return "stream: not opened"
        if st.get("cut") is not False:
            return "stream: cut"
        if st.get("file") != "%d.%d.stream.jsonl.gz" % (s, k):
            return "stream: its file"
        g = st.get("max_gap_ns")
        if not (type(g) is int and g <= GAP_MAX_NS):
            return "stream: a gap above 15 s"
        a, b = st.get("first_frame_wall_ns"), st.get("last_frame_wall_ns")
        if not (type(a) is int and type(b) is int and a <= b):
            return "stream: no frame"
        files.append((a, b, st["file"]))
    sub = (recs[0].get("stream") or {}).get("subscribed_wall_ns")
    if recs[0].get("joined_late") is not False or not (type(sub) is int and sub <= s * 10 ** 9):
        return "stream: subscribed late"
    if files[-1][1] < (s + SLOT) * 10 ** 9:
        return "stream: ended early"
    for (_a0, b0, _f0), (a1, _b1, _f1) in zip(files, files[1:]):
        if a1 - b0 > GAP_MAX_NS:
            return "stream: a gap above 15 s between files"
    for _a, _b, f in files:
        if (d0, f) not in assets:
            return "stream: not archived"
    return None


def fee_of(doc):
    """A member's maker rebate coefficient, the fee rate times the rebate rate, from its gamma document as the
    selection stored it: 0 where fees are not enabled or the schedule is not the venue's taker-only form."""
    if not isinstance(doc, dict) or doc.get("feesEnabled") is not True:
        return Fr(0)
    fs = doc.get("feeSchedule")
    if not isinstance(fs, dict) or fs.get("takerOnly") is not True or str(fs.get("exponent")) != "1":
        return Fr(0)
    return Fr(str(fs.get("rate"))) * Fr(str(fs.get("rebateRate")))


def gamma_docs_of(replies):
    """conditionId -> [documents] of every served gamma reply an attempt stored, numbers as Decimals of their text."""
    by = {}
    with gzip.open(__import__("io").BytesIO(replies), "rt", encoding="utf-8") as fh:
        for ln in fh:
            if not ln.strip():
                continue
            r = json.loads(ln)
            if r.get("kind") != "gamma" or r.get("status") != 200:
                continue
            for d in json.loads(r["raw"], parse_float=D):
                if isinstance(d, dict) and isinstance(d.get("conditionId"), str):
                    by.setdefault(d["conditionId"], []).append(d)
    return by


def members_of(sel):
    """The day's members as the replay takes them: condition id, its first token, the minimum size in hundredths of
    a share, the maximum spread in half-thousandths, the selection's daily rate and the rebate coefficient."""
    docs = gamma_docs_of(sel["replies"])
    out_ = []
    for m in sel["rec"]["members"]:
        cid, toks = m["condition_id"], m["token_ids"]
        assert CID_RE.fullmatch(cid) and len(toks) == 2 and all(TOKEN_RE.fullmatch(t) for t in toks), cid
        ms, vu = Fr(m["min_size"]) * 100, Fr(m["max_spread"]) * 20
        assert ms.denominator == 1 and vu.denominator == 1 and ms >= 0 and vu >= 0, "%s: size or spread" % cid
        fees = {fee_of(x) for x in docs.get(cid, [])}
        assert len(fees) == 1, "%s: %d fee terms in the selection's documents" % (cid, len(fees))
        out_.append({"cid": cid, "tok": toks[0], "ms": int(ms), "vu": int(vu), "rate": Fr(m["rate"]),
                     "fee": fees.pop()})
    return out_


def polls_of(d0, recs_by_slot, root=None):
    """Every served poll of the day's slots, in the order received: (recv_ns, condition id, row), row None where the
    page held no row, else (the daily rate, the competitiveness), each the Fraction of its decimal text - the rate the
    sum over the row's reward configurations in force on the poll's UTC date, from start_date to end_date."""
    polls, counts = [], collections.Counter()
    for s in sorted(recs_by_slot):
        for sj in recs_by_slot[s]:
            f = (sj.get("rewards") or {}).get("file")
            if f is None:
                continue
            with gzip.open(os.path.join(day_dir(d0, root), f), "rt", encoding="utf-8") as fh:
                for ln in fh:
                    if not ln.strip():
                        continue
                    r = json.loads(ln)
                    counts["polls"] += 1
                    if r.get("status") != 200 or r.get("raw") is None:
                        counts["unserved"] += 1
                        continue
                    data = json.loads(r["raw"], parse_float=D).get("data")
                    row = None
                    if data:
                        d = data[0]
                        day = utc(r["recv_wall_ns"] // 10 ** 9)[:10]
                        rate = sum((Fr(str(c["rate_per_day"])) for c in d["rewards_config"]
                                    if (c.get("start_date") is None or str(c["start_date"])[:10] <= day) and
                                    (c.get("end_date") is None or day <= str(c["end_date"])[:10])), Fr(0))
                        row = (rate, Fr(str(d["market_competitiveness"])))
                    else:
                        counts["no row"] += 1
                    polls.append((r["recv_wall_ns"], sys.intern(r["condition_id"]), row))
    polls.sort(key=lambda p: (p[0], p[1]))
    return polls, counts

# ---- the replay: one UTC day of the reward book's streams, our quote on every member (TZ-41 section 1) -------------

MS_NS = 10 ** 6
S_NS = 10 ** 9
PRICE_UNIT = 1000            # a price as an integer of thousandths
SIZE_UNIT = 100              # a size as an integer of hundredths of a share
STALE_NS = S_NS              # a market's pending order events are resolved once any line's host instant passes them by 1 s
INSIDE = (200, 1800)         # the qualifying midpoint, in half-thousandths, inside [0.10, 0.90]: one side scores a third
SEND, CANCEL = 0, 1
ZERO = (0, 1)
NEVER = 1 << 62

_PRICE = re.compile(r"(0|[1-9][0-9]*)(?:\.([0-9]{1,3}))?")
_SIZE = re.compile(r"(0|[1-9][0-9]*)(?:\.([0-9]{1,2}))?")
_PRICES, _SIZES = {}, {}


def price_int(s):
    v = _PRICES.get(s)
    if v is None:
        m = _PRICE.fullmatch(s)
        assert m, "a price %r" % (s,)
        v = _PRICES[s] = int(m.group(1)) * PRICE_UNIT + int((m.group(2) or "").ljust(3, "0"))
    return v


def size_int(s):
    v = _SIZES.get(s)
    if v is None:
        m = _SIZE.fullmatch(s)
        assert m, "a size %r" % (s,)
        v = int(m.group(1)) * SIZE_UNIT + int((m.group(2) or "").ljust(2, "0"))
        if len(_SIZES) < 1 << 16:
            _SIZES[s] = v
    return v


# A price_change frame as the venue sends it and the reward book stores it, matched whole: two entries, each field a
# run of digits, hex or BUY/SELL, where no escape can occur (TZ-30's and TZ-32's PC_LINE).
_ENTRY = (r'\{\\"asset_id\\":\\"([0-9]+)\\", \\"price\\":\\"([0-9.]+)\\", \\"size\\":\\"([0-9.]+)\\", '
          r'\\"side\\":\\"(BUY|SELL)\\", \\"hash\\":\\"[0-9a-f]*\\", \\"best_bid\\":\\"[0-9.]+\\", '
          r'\\"best_ask\\":\\"[0-9.]+\\"\}')
PC_LINE = re.compile(r'\{"recv_ns":([0-9]+),"mono_ns":-?[0-9]+,"raw":"\{\\"market\\":\\"(0x[0-9a-f]{64})\\", '
                     r'\\"price_changes\\":\[' + _ENTRY + ', ' + _ENTRY + r'\], \\"timestamp\\":\\"([0-9]+)\\", '
                     r'\\"event_type\\":\\"price_change\\"\}"\}\n?')


class Order:
    __slots__ = ("side", "p", "s", "q", "state", "done_at", "xc", "fill_vt")

    def __init__(self, side, p, s):
        self.side, self.p, self.s, self.q = side, p, s, None
        self.state = "sent"        # sent, resting, filled, cancelled, refused
        self.done_at = None        # the venue instant it left the book or was refused
        self.xc = 0                # the crossing size already counted against it
        self.fill_vt = None        # the venue instant of its last fill


class Spec:
    """A variant (TZ-41 section 1): its rule, its queue place, the crossing orders, the competitors' score."""
    __slots__ = ("name", "rule", "front", "takers", "denom", "L")

    def __init__(self, name, rule, front, takers, denom):
        assert rule in ("alone", "touch") and denom in ("pess", "opt", "venue"), (rule, denom)
        self.name, self.rule, self.front, self.takers, self.denom = name, rule, front, takers, denom
        self.L = LATENCY_MS * MS_NS


SPECS = tuple(Spec(*v) for v in VARIANTS)


class MV:
    """One market in one variant: our orders, their events, our fills, the host's knowledge, the reward."""
    __slots__ = ("sp", "live", "resting", "pend", "fills", "unknown", "x_known", "x", "cost", "rew", "share", "t",
                 "acc", "n", "scored_ns", "touch")

    def __init__(self, sp):
        self.sp = sp
        self.live = {"b": None, "a": None}
        self.resting = []
        self.pend = []
        self.fills = []
        self.unknown = []
        self.x_known = 0
        self.x = 0                 # hundredths of a share of the market's first token, + long
        self.cost = 0              # thousandths x hundredths: a bid filled at p costs +p f, an ask -p f
        self.rew = D(0)
        self.share = ZERO
        self.t = None              # the last instant the variant's clock reached
        self.acc = 0               # nanoseconds at the share in force, not yet added to the reward
        self.n = {"sent": 0, "cancels": 0, "refused": 0, "crossings": 0, "fills": 0}
        self.scored_ns = 0
        self.touch = None          # the qualifying touch of its last share; None: any entry can move it


class Market:
    __slots__ = ("cid", "tok", "ms", "vu", "fee", "rate", "ven", "bids", "asks", "bp", "ap", "block", "bvt",
                 "touch0", "seeded", "mvs", "c", "shadow", "dirty", "dtouch", "wake", "tick", "lastmid")

    def __init__(self, m, specs):
        self.cid, self.tok, self.ms, self.vu, self.fee = m["cid"], m["tok"], m["ms"], m["vu"], m["fee"]
        self.rate = (m["rate"].numerator, m["rate"].denominator)
        self.ven = (None, 1)       # the venue's score of every maker, x 12 over vu^2 * 100: none before a poll
        self.bids, self.asks, self.bp, self.ap = {}, {}, [], []
        self.block, self.bvt, self.touch0 = [], None, (None, None)
        self.seeded = False
        self.mvs = [MV(sp) for sp in specs]
        self.c = {"snapshots": 0, "touch_equal": 0, "book_equal": 0, "matches": 0}
        self.shadow = None
        self.dirty = False
        self.dtouch = None         # the touch the quoting rule last decided on
        self.wake = 0              # the first host instant the host learns of a fill, a refusal or a cancel
        self.tick = 10             # thousandths: the seed's tick_size, 0.01 until one is read
        self.lastmid = None        # twice the last midpoint of a two-sided book, in thousandths: the day's mark

    # -- the book ---------------------------------------------------------------------------------------------
    def set_level(self, side, p, s):
        bk, pl = (self.bids, self.bp) if side == "b" else (self.asks, self.ap)
        old = bk.get(p, 0)
        if s:
            if not old:
                bisect.insort(pl, p)
            bk[p] = s
        elif old:
            del bk[p]
            del pl[bisect.bisect_left(pl, p)]
        return old

    def replace(self, bids, asks):
        self.bids, self.asks = bids, asks
        self.bp, self.ap = sorted(bids), sorted(asks)

    def best(self, side):
        if side == "b":
            return self.bp[-1] if self.bp else None
        return self.ap[0] if self.ap else None

    def qual_best(self, side, ours):
        """The best displayed level whose size reaches the minimum size, or our own qualifying order's price."""
        ms = self.ms
        if side == "b":
            for p in reversed(self.bp):
                if self.bids[p] >= ms:
                    return p if ours is None or p > ours else ours
            return ours
        for p in self.ap:
            if self.asks[p] >= ms:
                return p if ours is None or p < ours else ours
        return ours

    def others(self, mid_u):
        """A and B: the displayed levels of at least the minimum size inside the band around mid_u, each side's sum
        of d^2 times size, over vu^2 * 100."""
        vu, ms = self.vu, self.ms
        A = 0
        lo = mid_u - vu                          # a bid scores where 2p > mid_u - vu
        i = len(self.bp) - 1
        while i >= 0:
            p = self.bp[i]
            if 2 * p <= lo:
                break
            s = self.bids[p]
            if s >= ms:
                d = vu - (mid_u - 2 * p)
                A += d * d * s
            i -= 1
        B = 0
        hi = mid_u + vu
        for p in self.ap:
            if 2 * p >= hi:
                break
            s = self.asks[p]
            if s >= ms:
                d = vu - (2 * p - mid_u)
                B += d * d * s
        return A, B

    def liquidation(self, x):
        """Thousandths x hundredths: the proceeds of selling x > 0 into the bids, or minus the cost of buying -x from
        the asks, the remainder beyond the book at 0 or at 1."""
        if x == 0:
            return 0
        if x > 0:
            left, val = x, 0
            for p in reversed(self.bp):
                f = min(left, self.bids[p])
                val += f * p
                left -= f
                if not left:
                    break
            return val
        left, val = -x, 0
        for p in self.ap:
            f = min(left, self.asks[p])
            val -= f * p
            left -= f
            if not left:
                break
        return val - left * PRICE_UNIT


def envelope(A, B, inside):
    """The competitors' score, x 12 over vu^2 * 100, from the displayed sides' sums A and B: (hi, lo), the most and
    the least the levels can score, split among makers in any way (TZ-41 section 1, the reward)."""
    m, M = min(A, B), max(A, B)
    if inside:
        return 4 * (2 * m + M), max(3 * (A + B), 4 * M)
    return 12 * m, 0


class Day:
    """The replay of one day's streams and polls (TZ-41 section 1). Members: dicts with cid, tok (the market's first
    token), ms (minimum size, hundredths), vu (maximum spread, half-thousandths), fee (Fraction: the fee rate times the
    rebate rate) and rate (the selection's daily rate, Fraction)."""

    def __init__(self, d0, members, specs=SPECS):
        self.d0, self.specs = d0, specs
        self.mk = [Market(m, specs) for m in members]
        self.by_cid = {M.cid: M for M in self.mk}
        assert len(self.by_cid) == len(self.mk), "a member twice"
        self.idx = {M.cid: i for i, M in enumerate(self.mk)}
        self.stale = []            # (tau, seq, market index)
        self.seq = 0
        self.live = False          # decisions, fills and rewards run from the day's first slot instant
        self.c = {"lines": 0, "frames": 0, "fast": 0, "skipped": 0, "polls": 0, "switches": 0, "subscribes": 0,
                  "closes": 0}

    # -- rewards ------------------------------------------------------------------------------------------------
    def integrate(self, M, t):
        for mv in M.mvs:
            self.integrate_one(M, mv, t)

    def integrate_one(self, M, mv, t):
        """The variant's clock advanced to t where t is later: the time passes at the share and the rate in force."""
        if mv.t is None:
            mv.t = t
        elif t > mv.t:
            mv.acc += t - mv.t
            mv.t = t

    def flush(self, M, mv):
        """The time at the share and the rate in force added to the reward: rate * share * dt / 86,400 s, a Decimal
        quotient at 50 significant digits, summed in order - before either changes."""
        if mv.acc:
            num, den = mv.share
            if num:
                rn, rd = M.rate
                if rn:
                    mv.rew = C50.add(mv.rew, C50.divide(D(rn * num * mv.acc), D(rd * den * DAY * S_NS)))
                mv.scored_ns += mv.acc
            mv.acc = 0

    def set_share(self, M, mv, sh):
        if sh != mv.share:
            self.flush(M, mv)
            mv.share = sh

    def refresh(self, M, ents=None, t=None):
        """Every variant's clock advanced to host instant t, then its share recomputed - or, given a frame's entries,
        only the shares an entry can move: a variant's with resting orders whose entries reach its band or its
        qualifying touch."""
        cache = {}
        for mv in M.mvs:
            if t is not None:
                self.integrate_one(M, mv, t)
            if ents is not None:
                if not mv.resting:
                    continue
                tch = mv.touch
                if tch is not None:
                    qb, qa = tch
                    lo, hi = qb + qa - M.vu, qb + qa + M.vu
                    for side, p, _s in ents:
                        if (2 * p > lo or p >= qb) if side == "b" else (2 * p < hi or p <= qa):
                            break
                    else:
                        continue
            self.set_share(M, mv, self.share_of(M, mv, cache))

    def share_of(self, M, mv, cache):
        """Our share of the market's score at this instant, as (numerator, denominator); (0, 1) where we score
        nothing. `cache` keeps, for one book state, each set of our resting orders' parts."""
        if not M.seeded or not mv.resting:
            mv.touch = None
            return ZERO
        key = tuple((o.side, o.p, o.s) for o in mv.resting)
        parts = cache.get(key)
        if parts is None:
            parts = cache[key] = self.parts_of(M, mv.resting)
        if parts is None:
            mv.touch = None
            return ZERO
        touch, Q, hi, lo = parts
        mv.touch = touch
        if Q == 0:
            return ZERO
        vn, vd = M.ven
        den = mv.sp.denom
        if vn is None:
            O_n, O_d = (lo if den == "opt" else hi), 1
        elif den == "pess":
            O_n, O_d = (hi, 1) if hi * vd >= vn else (vn, vd)
        elif den == "opt":
            O_n, O_d = (lo, 1) if lo * vd <= vn else (vn, vd)
        else:
            O_n, O_d = vn, vd
        return (Q * O_d, Q * O_d + O_n)

    def parts_of(self, M, resting):
        """For one set of our resting orders on the book as it stands: the qualifying touch, our score Q and the
        competitors' hi and lo, all x 12 over vu^2 * 100; None where no qualifying touch exists."""
        ms, vu = M.ms, M.vu
        ob = oa = None
        for o in resting:
            if o.s >= ms:
                if o.side == "b":
                    ob = o.p if ob is None or o.p > ob else ob
                else:
                    oa = o.p if oa is None or o.p < oa else oa
        if ob is None and oa is None:
            return None
        qb, qa = M.qual_best("b", ob), M.qual_best("a", oa)
        if qb is None or qa is None or qb >= qa:
            return None
        mid_u = qb + qa
        q1 = q2 = 0
        for o in resting:
            if o.s < ms:
                continue
            su = (mid_u - 2 * o.p) if o.side == "b" else (2 * o.p - mid_u)
            if 0 <= su < vu:
                d = vu - su
                if o.side == "b":
                    q1 += d * d * o.s
                else:
                    q2 += d * d * o.s
        inside = INSIDE[0] <= mid_u <= INSIDE[1]
        Q = 4 * max(3 * min(q1, q2), max(q1, q2)) if inside else 12 * min(q1, q2)
        if Q == 0:
            return ((qb, qa), 0, 0, 0)
        hi, lo = envelope(*M.others(mid_u), inside)
        return ((qb, qa), Q, hi, lo)

    # -- our orders' events ---------------------------------------------------------------------------------------
    def push(self, mi, mv, tau, kind, o):
        self.seq += 1
        heapq.heappush(mv.pend, (tau, self.seq, kind, o))
        heapq.heappush(self.stale, (tau, self.seq, mi))

    def resolve(self, M, before):
        """Every variant's events of M due before `before`, in their order; the reward integrated to each."""
        for mv in M.mvs:
            P = mv.pend
            while P and P[0][0] < before:
                tau, _s, kind, o = heapq.heappop(P)
                self.integrate_one(M, mv, tau)
                if kind == SEND:
                    opp = M.best("a" if o.side == "b" else "b")
                    if opp is not None and (o.p >= opp if o.side == "b" else o.p <= opp):
                        o.state, o.done_at = "refused", tau
                        mv.n["refused"] += 1
                        if tau + mv.sp.L < M.wake:
                            M.wake = tau + mv.sp.L
                    else:
                        o.q = 0 if mv.sp.front else (M.bids if o.side == "b" else M.asks).get(o.p, 0)
                        o.state = "resting"
                        mv.resting.append(o)
                elif o.state in ("sent", "resting"):
                    o.state, o.done_at = "cancelled", tau
                    if tau + mv.sp.L < M.wake:
                        M.wake = tau + mv.sp.L
                    mv.resting = [x for x in mv.resting if x.state == "resting"]
                self.set_share(M, mv, self.share_of(M, mv, {}))

    def resolve_stale(self, h):
        S = self.stale
        lim = h - STALE_NS
        while S and S[0][0] < lim:
            tau, _s, mi = heapq.heappop(S)
            M = self.mk[mi]
            if M.block:
                self.close_block(M, False)
            self.resolve(M, tau + 1)

    # -- fills ----------------------------------------------------------------------------------------------------
    def fill(self, M, mv, o, vt, f, kind):
        M.dirty = True
        if vt + mv.sp.L < M.wake:
            M.wake = vt + mv.sp.L
        o.s -= f
        o.fill_vt = vt
        mv.fills.append((vt, o.side, o.p, f, kind))
        dx = f if o.side == "b" else -f
        mv.x += dx
        mv.cost += dx * o.p
        heapq.heappush(mv.unknown, (vt, dx))
        mv.n["fills"] += 1
        if o.s == 0:
            o.state, o.done_at = "filled", vt

    def known_x(self, mv, h):
        u = mv.unknown
        while u and u[0][0] + mv.sp.L <= h:
            mv.x_known += heapq.heappop(u)[1]
        return mv.x_known

    def sweep(self, M, side, t0):
        """A match's sweep of one side from its touch before the block: [(price, size taken)], best first, through
        the last level it reached."""
        cur = M.bids if side == "b" else M.asks
        first, dec = {}, {}
        for sd, p, old, new in M.block:
            if sd != side:
                continue
            if p not in first:
                first[p] = old
            dec[p] = first[p] - new
        if t0 is None or dec.get(t0, 0) <= 0:
            return []
        levels = sorted((p for p in set(first) | set(cur) if (p <= t0 if side == "b" else p >= t0)),
                        reverse=(side == "b"))
        sw = []
        for p in levels:
            pre = first[p] if p in first else cur.get(p, 0)
            if pre <= 0:
                continue
            c = dec.get(p, 0)
            if c <= 0:
                break
            sw.append((p, c))
            if c < pre:
                break
        return sw

    def close_block(self, M, match):
        """A block of entries with one venue stamp ends; where the venue's book frame of the same stamp followed it,
        a match: every resting order the sweep reached fills beyond its queue place."""
        if match and M.block:
            hit = 0
            for side, t0 in (("b", M.touch0[0]), ("a", M.touch0[1])):
                sw = self.sweep(M, side, t0)
                if not sw:
                    continue
                hit += 1
                last = sw[-1][0]
                at = dict(sw)
                for mv in M.mvs:
                    for o in mv.resting:
                        if o.side != side or o.state != "resting":
                            continue
                        f = 0
                        if (last <= o.p) if side == "b" else (last >= o.p):
                            tot = sum(c for p, c in sw if (p <= o.p if side == "b" else p >= o.p))
                            f = min(o.s, max(0, tot - o.q))
                        o.q = max(0, o.q - at.get(o.p, 0))
                        if f > 0:
                            self.fill(M, mv, o, M.bvt, f, "m")
                    mv.resting = [x for x in mv.resting if x.state == "resting"]
            if hit:
                M.c["matches"] += 1
        for mv in M.mvs:
            for o in mv.resting:
                lv = (M.bids if o.side == "b" else M.asks).get(o.p, 0)
                if lv < o.q:
                    o.q = lv
        t = M.bvt
        M.block, M.bvt = [], None
        self.cross(M, t)

    def cross(self, M, vt):
        """Where the opposite side reaches a resting order's price with no match, the orders there would have met
        ours: in a variant that counts them takers, our order fills at once for their size not yet counted."""
        bb, ba = M.best("b"), M.best("a")
        for mv in M.mvs:
            if not mv.sp.takers:
                continue
            gone = False
            for o in mv.resting:
                if o.state != "resting":
                    continue
                if o.side == "b":
                    c = sum(s for p, s in M.asks.items() if p <= o.p) if ba is not None and ba <= o.p else 0
                else:
                    c = sum(s for p, s in M.bids.items() if p >= o.p) if bb is not None and bb >= o.p else 0
                if c > o.xc:
                    f = min(o.s, c - o.xc)
                    mv.n["crossings"] += 1
                    self.fill(M, mv, o, vt, f, "x")
                    gone = gone or o.state != "resting"
                o.xc = c
            if gone:
                mv.resting = [x for x in mv.resting if x.state == "resting"]

    # -- the quoting rule -------------------------------------------------------------------------------------------
    def decide(self, M, h):
        """The quoting rule after a frame of the market reaches the host at h. Where the touch is the one it last
        decided on and the host has learned nothing since, it would decide the same, and returns."""
        if not (self.live and M.seeded):
            return
        bb, ba = M.best("b"), M.best("a")
        if (bb, ba) == M.dtouch and h < M.wake:
            return
        M.dtouch = (bb, ba)
        mi = self.idx[M.cid]
        for mv in M.mvs:
            cap = CAP_CLIPS * M.ms
            L = mv.sp.L
            x = None
            tb = ta = None
            if bb is not None and ba is not None:
                if mv.sp.rule == "alone":
                    if ba - bb >= SPREAD_TICKS * M.tick:
                        tb, ta = bb + M.tick, ba - M.tick
                else:
                    tb, ta = bb, ba
            band = tb is not None and ta - tb < M.vu and M.ms > 0
            for side in ("b", "a"):
                o = mv.live[side]
                if o is not None and o.done_at is not None and o.done_at + L <= h:
                    o = mv.live[side] = None
                tgt = None
                if band:
                    tgt = tb if side == "b" else ta
                    if not 0 < tgt < PRICE_UNIT:
                        tgt = None
                if tgt is not None:
                    if x is None:
                        x = self.known_x(mv, h)
                    if x >= cap if side == "b" else x <= -cap:
                        tgt = None
                stale = (o is not None and o.state == "resting" and o.fill_vt is not None and o.fill_vt + L <= h
                         and o.s < M.ms)
                if tgt is None:
                    if o is not None:
                        self.push(mi, mv, h + L, CANCEL, o)
                        mv.n["cancels"] += 1
                        mv.live[side] = None
                elif o is None:
                    n = Order(side, tgt, M.ms)
                    mv.live[side] = n
                    self.push(mi, mv, h + L, SEND, n)
                    mv.n["sent"] += 1
                elif o.p != tgt or stale:
                    self.push(mi, mv, h + L, CANCEL, o)
                    mv.n["cancels"] += 1
                    n = Order(side, tgt, M.ms)
                    mv.live[side] = n
                    self.push(mi, mv, h + L, SEND, n)
                    mv.n["sent"] += 1
        w = NEVER
        for mv in M.mvs:
            L = mv.sp.L
            for o in mv.live.values():
                if o is None:
                    continue
                for t in (o.done_at, o.fill_vt):
                    if t is not None and t + L < w:
                        w = t + L
            if mv.unknown and mv.unknown[0][0] + L < w:
                w = mv.unknown[0][0] + L
        M.wake = w

    # -- the stream ---------------------------------------------------------------------------------------------
    def session(self, ev, h, reason):
        """A session event of the live stream: every market's book cleared at a connect or subscribe; at a close
        other than the slot's end, every live order of ours cancelled."""
        if ev == "subscribe":
            self.c["subscribes"] += 1
        elif ev == "close" and reason != "end":
            self.c["closes"] += 1
        for M in self.mk:
            if M.block:
                self.close_block(M, False)
            self.resolve(M, h)
            self.integrate(M, h)
        if ev in ("connect", "subscribe"):
            for M in self.mk:
                M.replace({}, {})
                M.seeded = False
                self.refresh(M, None, h)
        elif ev == "close" and reason != "end":
            for mi, M in enumerate(self.mk):
                for mv in M.mvs:
                    for side in ("b", "a"):
                        o = mv.live[side]
                        if o is not None:
                            self.push(mi, mv, h + mv.sp.L, CANCEL, o)
                            mv.n["cancels"] += 1
                            mv.live[side] = None

    def poll(self, t, cid, row):
        """A served reward poll of a member: its daily rate and the venue's figure from then on; a page with no row
        stops the reward (rate 0)."""
        M = self.by_cid.get(cid)
        if M is None:
            return
        if self.live:
            if M.block:
                self.close_block(M, False)
            self.resolve(M, t)
            self.integrate(M, t)
            for mv in M.mvs:
                self.flush(M, mv)
        if row is None:
            M.rate, M.ven = (0, 1), (None, 1)
        else:
            rate, comp = row
            M.rate = (rate.numerator, rate.denominator)
            v = comp * rate * M.vu * M.vu * SIZE_UNIT * 12
            M.ven = (v.numerator, v.denominator)
        self.c["polls"] += 1
        if self.live:
            self.refresh(M, None, t)

    def frame_items(self, fr, h, shadow):
        seed = isinstance(fr, list)
        touched = []
        for it in (fr if seed else (fr,)):
            if not isinstance(it, dict):
                continue
            M = self.by_cid.get(it.get("market"))
            if M is None:
                continue
            et = it.get("event_type")
            if et == "book":
                if it.get("asset_id") != M.tok:
                    continue
                bids = {}
                for lv in it["bids"]:
                    bids[price_int(lv["price"])] = size_int(lv["size"])
                asks = {}
                for lv in it["asks"]:
                    asks[price_int(lv["price"])] = size_int(lv["size"])
                bids = {p: s for p, s in bids.items() if s}
                asks = {p: s for p, s in asks.items() if s}
                ts = it.get("tick_size")
                if seed and ts in ("0.1", "0.01", "0.001"):
                    M.tick = price_int(ts)
                if shadow:
                    M.shadow = [bids, asks, True]
                    continue
                vt = int(it["timestamp"]) * MS_NS
                if M.block and vt != M.bvt:
                    self.close_block(M, False)
                self.resolve(M, vt)
                if seed:
                    if M.block:
                        self.close_block(M, False)
                    M.seeded = True
                else:
                    M.c["snapshots"] += 1
                    if M.block:
                        self.close_block(M, vt == M.bvt)
                    bb, ba = M.best("b"), M.best("a")
                    nb = max(bids) if bids else None
                    na = min(asks) if asks else None
                    if (bb, M.bids.get(bb), ba, M.asks.get(ba)) == (nb, bids.get(nb), na, asks.get(na)):
                        M.c["touch_equal"] += 1
                    if M.bids == bids and M.asks == asks:
                        M.c["book_equal"] += 1
                M.replace(bids, asks)
                for mv in M.mvs:
                    for o in mv.resting:
                        lv = (M.bids if o.side == "b" else M.asks).get(o.p, 0)
                        if lv < o.q:
                            o.q = lv
                self.cross(M, vt)
                touched.append((M, None))
            elif et == "tick_size_change":
                ts = it.get("new_tick_size")
                if it.get("asset_id") == M.tok and ts in ("0.1", "0.01", "0.001"):
                    M.tick = price_int(ts)
                    M.dtouch = None
            elif et == "price_change":
                ents = [(("b" if pc["side"] == "BUY" else "a"), price_int(pc["price"]), size_int(pc["size"]))
                        for pc in it["price_changes"] if pc.get("asset_id") == M.tok]
                if not ents:
                    continue
                if shadow:
                    self.shadow_apply(M, ents)
                    continue
                touched.append(self.entries(M, int(it["timestamp"]) * MS_NS, ents))
        return touched

    def shadow_apply(self, M, ents):
        sh = M.shadow
        if sh is None or not sh[2]:
            return
        for side, p, s in ents:
            bk = sh[0] if side == "b" else sh[1]
            if s:
                bk[p] = s
            else:
                bk.pop(p, None)

    def entries(self, M, vt, ents):
        if M.block and vt != M.bvt:
            self.close_block(M, False)
        self.resolve(M, vt)
        if not M.block:
            M.bvt = vt
            M.touch0 = (M.best("b"), M.best("a"))
        for side, p, s in ents:
            old = M.set_level(side, p, s)
            M.block.append((side, p, old, s))
        return (M, ents)

    def pc_fast(self, g, shadow):
        """A price_change line matched whole by PC_LINE: the same as frame_items on its parsed frame."""
        M = self.by_cid.get(g[1])
        if M is None:
            return None
        ents = [("b" if g[j + 3] == "BUY" else "a", price_int(g[j + 1]), size_int(g[j + 2])) for j in (2, 6)
                if g[j] == M.tok]
        if not ents:
            return None
        if shadow:
            self.shadow_apply(M, ents)
            return None
        return self.entries(M, int(g[10]) * MS_NS, ents)

    def after(self, tm, h):
        """After a frame of a market: the quoting rule, then the shares it can have moved."""
        M, ents = tm
        if M.bp and M.ap:
            M.lastmid = M.bp[-1] + M.ap[0]
        self.decide(M, h)
        if M.dirty:
            M.dirty = False
            self.refresh(M, None, h)
        else:
            self.refresh(M, ents, h)

    def switch(self, S_ns):
        """The slot's instant: every market's book becomes the one the new slot's file has built to it."""
        self.c["switches"] += 1
        for M in self.mk:
            if M.block:
                self.close_block(M, False)
            self.resolve(M, S_ns)
            self.integrate(M, S_ns)
            sh = M.shadow
            M.shadow = None
            if sh is None:
                M.replace({}, {})
                M.seeded = False
            else:
                M.replace(sh[0], sh[1])
                M.seeded = sh[2]
            for mv in M.mvs:
                for o in mv.resting:
                    lv = (M.bids if o.side == "b" else M.asks).get(o.p, 0)
                    if lv < o.q:
                        o.q = lv
            if M.seeded:
                self.cross(M, S_ns)
        self.live = True
        for M in self.mk:
            if M.bp and M.ap:
                M.lastmid = M.bp[-1] + M.ap[0]
            M.dtouch = None
            self.decide(M, S_ns)
            self.refresh(M, None, S_ns)

    def at_host(self, h, shadow, switched, S_ns, polls):
        if not shadow and not switched:
            self.switch(S_ns)
        if not shadow:
            while polls and polls[0][0] <= h:
                t, cid, row = polls.popleft()
                self.poll(t, cid, row)
            self.resolve_stale(h)
        return switched or not shadow

    def feed_slot(self, S, paths, polls):
        """Every line of slot S's stream files, in the order stored: lines received before S build each market's
        next book; from S to S + 900 they run the day; later lines belong to the next slot's file. `polls`: a deque
        of the day's served polls (recv_ns, condition id, row) in order, consumed from the front."""
        S_ns, E_ns = S * S_NS, (S + SLOT) * S_NS
        switched = False
        for M in self.mk:
            M.shadow = None
        for path in paths:
            with gzip.open(path, "rt", encoding="utf-8") as fh:
                for line in fh:
                    self.c["lines"] += 1
                    mt = PC_LINE.fullmatch(line)
                    if mt is not None:
                        g = mt.groups()
                        h = int(g[0])
                        if h >= E_ns:
                            continue
                        shadow = h < S_ns
                        switched = self.at_host(h, shadow, switched, S_ns, polls)
                        self.c["frames"] += 1
                        self.c["fast"] += 1
                        tm = self.pc_fast(g, shadow)
                        if tm is not None:
                            self.after(tm, h)
                        continue
                    if not line.strip():
                        continue
                    o = json.loads(line)
                    h = o.get("recv_ns")
                    assert type(h) is int, "a line without its host receipt"
                    if h >= E_ns:
                        continue
                    shadow = h < S_ns
                    switched = self.at_host(h, shadow, switched, S_ns, polls)
                    if "event" in o:
                        ev = o["event"]
                        if ev in ("connect", "subscribe", "close"):
                            if shadow:
                                if ev != "close":
                                    for M in self.mk:
                                        M.shadow = [{}, {}, False]
                            else:
                                self.session(ev, h, o.get("reason"))
                        continue
                    raw = o.get("raw")
                    if raw is None or raw == "PONG":
                        self.c["skipped"] += 1
                        continue
                    try:
                        fr = json.loads(raw)
                    except ValueError:
                        self.c["skipped"] += 1
                        continue
                    self.c["frames"] += 1
                    touched = self.frame_items(fr, h, shadow)
                    if not shadow:
                        for tm in touched:
                            self.after(tm, h)
        if not switched:
            self.switch(S_ns)
        while polls and polls[0][0] < E_ns:
            t, cid, row = polls.popleft()
            self.poll(t, cid, row)

    def finish(self, end_ns, outcomes):
        """The day's end: every event and reward integrated to it, every position valued at the market's last
        midpoint of the day - or at its outcome, where `outcomes` holds one (thousandths a share of the first token)
        - or, where the market never showed a two-sided book, by liquidation into the book as it stands."""
        rows = []
        for M in self.mk:
            if M.block:
                self.close_block(M, False)
            self.resolve(M, end_ns)
            self.integrate(M, end_ns)
            for mv in M.mvs:
                self.flush(M, mv)
            mark = outcomes.get(M.cid)
            how = "outcome"
            if mark is None and M.lastmid is not None:
                mark, how = Fr(M.lastmid, 2), "mid"
            for mv in M.mvs:
                if mark is not None:
                    val = mv.x * Fr(mark)
                else:
                    val, how = Fr(M.liquidation(mv.x)), "book"
                reb = sum((M.fee * f * p * (PRICE_UNIT - p) for _vt, _sd, p, f, _k in mv.fills), Fr(0)) \
                    / (SIZE_UNIT * PRICE_UNIT * PRICE_UNIT)
                pnl = (val - mv.cost) / (SIZE_UNIT * PRICE_UNIT)
                rows.append({"cid": M.cid, "variant": mv.sp.name, "rew": mv.rew, "reb": reb, "pnl": pnl, "x": mv.x,
                             "cost": mv.cost, "mark": how, "fills": len(mv.fills),
                             "fill_hu": sum(f for _a, _b, _c, f, _d in mv.fills),
                             "crossed_hu": sum(f for _a, _b, _c, f, k in mv.fills if k == "x"),
                             "scored_ns": mv.scored_ns, "n": dict(mv.n)})
        return rows

# ---- the set: the candidate days in order, each a member or not by TZ-41 section 1's rules --------------------------

RESCORE_SLOTS = 24           # the rescore replays the set's first day's first 24 slots (TZ-41 section 4.4)
DAY_FILE_KEYS = ("cid", "variant", "rew", "reb", "pnl", "x", "cost", "mark", "fills", "fill_hu", "crossed_hu",
                 "scored_ns", "n")


def fr_text(x):
    x = Fr(x)
    return "%d/%d" % (x.numerator, x.denominator)


def fr_of(s):
    n, d = s.split("/")
    return Fr(int(n), int(d))


def wait_archive(d0, t_start, clock=None, sleep=None, read=None):
    """Until the reward book archive's assets reach the last slot of day d0: its ledger read again every 60 s,
    BLOCKED once WAIT_MAX_S have passed since `t_start`. Returns the asset map."""
    clock, sleep, read = clock or time.time, sleep or time.sleep, read or archived_to
    amap, last = read()
    said = None
    need = d0 + DAY - SLOT
    while last < need:
        now = clock()
        assert now - t_start <= WAIT_MAX_S, "BLOCKED: the archive's assets reach slot %d, below %d, at %s" % (
            last, need, utc(now))
        if said is None or now - said >= 1800:
            out("the archive's assets reach slot %d (%s); day %d needs %d; its ledger read again every 60 s" % (
                last, utc(last) if last else "-", d0, need))
            said = now
        sleep(60)
        amap, last = read()
    return amap


def day_verdict(d0, amap, root=None):
    """One candidate day: (None, its record, its polls) where it is a member, else (the first reason it is not,
    None, None) - no selection; a slot without its records or failing a rule, the first such slot named."""
    sel = selection_of(d0, root)
    if sel is None:
        return "no selection", None, None
    members = members_of(sel)
    if not members:
        return "a selection of no market", None, None
    recs = slot_records(d0, root)
    slots = []
    for S in range(d0, d0 + DAY, SLOT):
        why = slot_problem(S, recs.get(S, []), sel["sha256"], len(members), amap, d0)
        if why is not None:
            return "slot %d (%s): %s" % (S, utc(S), why), None, None
        files = []
        for sj in recs[S]:
            a = amap[(d0, sj["stream"]["file"])]
            files.append({"file": sj["stream"]["file"], "tag": a["tag"], "asset": a["asset"], "bytes": a["bytes"],
                          "sha256": a["sha256"]})
        slots.append({"S": S, "files": files})
    polls, counts = polls_of(d0, {S: recs[S] for S in range(d0, d0 + DAY, SLOT)}, root)
    rec = {"d0": d0, "selection": {"attempt": sel["attempt"], "sha256": sel["sha256"], "members": len(members)},
           "members": [dict(m, rate=fr_text(m["rate"]), fee=fr_text(m["fee"])) for m in members], "slots": slots,
           "polls": {"n": len(polls), "polls": counts["polls"], "unserved": counts["unserved"],
                     "no_row": counts["no row"]}}
    return None, rec, polls


def polls_text(polls):
    return "".join(json.dumps([t, cid, None if row is None else [fr_text(row[0]), fr_text(row[1])]],
                              separators=(",", ":")) + "\n" for t, cid, row in polls)


class PollFile:
    """A member day's polls file read in order, one line at a time: the front poll as `[0]`, `popleft()`, truth while
    a poll is left, and iteration over the rest - a deque's interface, so that a day's polls are never all held."""

    def __init__(self, path):
        self.fh = open(path, encoding="utf-8")
        self.head = None
        self._advance()

    def _advance(self):
        ln = self.fh.readline() if self.fh is not None else ""
        if not ln:
            self.head = None
            if self.fh is not None:
                self.fh.close()
                self.fh = None
            return
        t, cid, row = json.loads(ln)
        self.head = (t, sys.intern(cid), None if row is None else (fr_of(row[0]), fr_of(row[1])))

    def __bool__(self):
        return self.head is not None

    def __getitem__(self, i):
        assert i == 0 and self.head is not None, "PollFile: only the front poll"
        return self.head

    def popleft(self):
        assert self.head is not None, "PollFile: no poll left"
        h = self.head
        self._advance()
        return h

    def __iter__(self):
        while self.head is not None:
            yield self.popleft()


def polls_read(path):
    return PollFile(path)


def members_read(rec):
    return [dict(m, rate=fr_of(m["rate"]), fee=fr_of(m["fee"])) for m in rec["members"]]


def gamma_get(query, tries=DL_TRIES, sleep=None):
    sleep = sleep or time.sleep
    url = GAMMA_URL % query
    last = None
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers=GAMMA_HEADERS, method="GET")
            with urllib.request.urlopen(req, timeout=60) as r:
                body = r.read()
                assert r.status == 200, "HTTP %d" % r.status
            return json.loads(body, parse_float=D), len(body), sha256_bytes(body), k
        except urllib.error.HTTPError as e:
            last = "HTTP %d" % e.code
            if e.code not in (429, 500, 502, 503, 504):
                break
        except (urllib.error.URLError, http.client.HTTPException, TimeoutError, ConnectionError, OSError,
                ValueError) as e:
            last = "%s %s" % (type(e).__name__, e)
        sleep(min(60.0, 5.0 * 2 ** k))
    raise AssertionError("BLOCKED: gamma %s: %d attempts, the last %s" % (query[:80], tries, last))


def outcome_of(doc, tok):
    """The first token's outcome in thousandths, 1000 or 0, where the document reads the market closed with prices of
    exactly 0 and 1; otherwise None."""
    if doc.get("closed") is not True:
        return None
    try:
        prices, toks = json.loads(doc.get("outcomePrices")), json.loads(doc.get("clobTokenIds"))
    except (TypeError, ValueError):
        return None
    if sorted(map(str, prices)) != ["0", "1"] or len(toks) != 2 or tok not in toks:
        return None
    return PRICE_UNIT if str(prices[toks.index(tok)]) == "1" else 0


def documents(toks, holdf=None, get=None):
    """Every member's gamma document, read open and closed, DOC_CHUNK condition ids a request, each request held to
    the idle stretch; each member's document found exactly once, and only its outcome kept. Returns ({cid: outcome},
    requests)."""
    holdf, get = holdf or hold, get or gamma_get
    cids = sorted(toks)
    found, reqs = {}, []
    for i in range(0, len(cids), DOC_CHUNK):
        chunk = cids[i:i + DOC_CHUNK]
        for closed in (False, True):
            q = [("limit", 2 * DOC_CHUNK)] + [("condition_ids", c) for c in chunk] + (
                [("closed", "true")] if closed else [])
            holdf(DOC_BUDGET_S)
            docs, n, sha, k = get(urllib.parse.urlencode(q))
            assert isinstance(docs, list) and len(docs) <= len(chunk), "gamma: %d documents for %d ids" % (
                len(docs), len(chunk))
            reqs.append({"ids": len(chunk), "closed": closed, "bytes": n, "sha256": sha, "docs": len(docs),
                         "retries": k})
            for d in docs:
                cid = d.get("conditionId")
                assert cid in toks and cid not in found, "gamma: a document of %r" % cid
                found[cid] = outcome_of(d, toks[cid])
            del docs
    missing = sorted(set(cids) - set(found))
    assert not missing, "BLOCKED: no gamma document of %d members: %s" % (len(missing), missing[:3])
    return {c: found[c] for c in cids}, reqs


def mode_fetch():
    """The set (TZ-41 section 3.6): the candidate days in order from FIRST_D0, each read from the reward book's store
    and the archive's record once the archive has moved it, until NEED members; the members' documents; every
    candidate disclosed."""
    floor_check()
    os.makedirs(os.path.join(WORK, "fetch"), exist_ok=True)
    sp = os.path.join(WORK, "set.json")
    if os.path.exists(sp):
        s = load_json(sp)
        for d0 in s["members"]:
            got = sha256_file(os.path.join(WORK, "fetch", "%d.json" % d0))
            assert got == s["days"][str(d0)]["sha256"], "the set's day %d differs from its record" % d0
        out("the set is on disk: %s sha256 %s, %d members, every day's record unchanged" % (
            sp, sha256_file(sp), len(s["members"])))
        return
    assert time.time() >= FIRST_D0 + NEED * DAY, "BLOCKED: before the eighth candidate day has ended"
    t_start = time.time()
    considered, member_days, days = [], [], {}
    d0 = FIRST_D0
    while len(member_days) < NEED:
        assert d0 <= LAST_D0, "BLOCKED: %d non-member days before the eighth member, the bound %d" % (
            len(considered) - len(member_days), NONMEMBER_MAX)
        assert time.time() >= d0 + DAY, "BLOCKED: day %d (%s) has not ended; the set needs it" % (d0, utc(d0))
        amap = wait_archive(d0, t_start)
        hold(STORE_BUDGET_S)
        why, rec, polls = day_verdict(d0, amap)
        considered.append({"d0": d0, "member": why is None, "reason": why})
        if why is None:
            ptxt = polls_text(polls).encode("utf-8")
            rec["polls"]["sha256"] = write_once(os.path.join(WORK, "fetch", "%d.polls.jsonl" % d0), ptxt)
            body = dumps(rec).encode("utf-8")
            days[str(d0)] = {"sha256": write_once(os.path.join(WORK, "fetch", "%d.json" % d0), body),
                             "bytes": sum(f["bytes"] for s in rec["slots"] for f in s["files"]),
                             "files": sum(len(s["files"]) for s in rec["slots"]),
                             "members": len(rec["members"])}
            member_days.append(d0)
            out("candidate %d (%s): MEMBER %d of %d - %d markets, %d slots, %d stream files, %d bytes; polls %d "
                "served of %d, %d without a row" % (
                    d0, utc(d0), len(member_days), NEED, len(rec["members"]), len(rec["slots"]), days[str(d0)]["files"],
                    days[str(d0)]["bytes"], rec["polls"]["n"], rec["polls"]["polls"], rec["polls"]["no_row"]))
        else:
            out("candidate %d (%s): not a member - %s" % (d0, utc(d0), why))
        rec = polls = ptxt = body = None    # one day's polls held at a time
        d0 += DAY
    toks = {}
    for d in member_days:
        for m in load_json(os.path.join(WORK, "fetch", "%d.json" % d))["members"]:
            assert toks.get(m["cid"], m["tok"]) == m["tok"], "%s: two first tokens" % m["cid"]
            toks[m["cid"]] = m["tok"]
    outcomes, reqs = documents(toks)
    for r in reqs:
        out("gamma request: %d ids, closed %s, %d documents, %d bytes, sha256 %s, retries %d" % (
            r["ids"], r["closed"], r["docs"], r["bytes"], r["sha256"], r["retries"]))
    s = {"first_d0": FIRST_D0, "need": NEED, "considered": considered, "members": member_days, "days": days,
         "markets": len(toks), "outcomes": {c: v for c, v in sorted(outcomes.items()) if v is not None},
         "requests": reqs}
    sha = write_once(sp, dumps(s).encode("utf-8"))
    out("G-SET PASS: %d members of %d candidates considered, %d to %d; %d distinct markets, %d resolved by their "
        "documents; %d stream files, %d bytes; set.json sha256 %s" % (
            len(member_days), len(considered), member_days[0], member_days[-1], len(toks), len(s["outcomes"]),
            sum(v["files"] for v in days.values()), sum(v["bytes"] for v in days.values()), sha))


def day_inputs(d0):
    """A member day's record and its polls, the polls file asserted by the SHA-256 its record carries."""
    rec = load_json(os.path.join(WORK, "fetch", "%d.json" % d0))
    path = os.path.join(WORK, "fetch", "%d.polls.jsonl" % d0)
    assert sha256_file(path) == rec["polls"]["sha256"], "day %d: its polls differ from its record" % d0
    return rec, polls_read(path)


def the_set():
    s = load_json(os.path.join(WORK, "set.json"))
    assert len(s["members"]) == NEED, "the set holds %d members" % len(s["members"])
    for d0 in s["members"]:
        got = sha256_file(os.path.join(WORK, "fetch", "%d.json" % d0))
        assert got == s["days"][str(d0)]["sha256"], "the set's day %d differs from its record" % d0
    return s

# ---- downloads: one Release asset, by its tag and name, verified by its bytes and SHA-256 ----------------------


def download(tag, asset, nbytes, sha, dest, url_of=None, tries=DL_TRIES, sleep=None):
    sleep = sleep or time.sleep
    url = (url_of or (lambda t, a: DL_URL % (urllib.parse.quote(t), urllib.parse.quote(a))))(tag, asset)
    last = None
    for k in range(tries):
        t0 = time.time()
        try:
            req = urllib.request.Request(url, headers=DL_HEADERS, method="GET")
            h, n = hashlib.sha256(), 0
            with urllib.request.urlopen(req, timeout=120) as r, open(dest + ".part", "wb") as fh:
                assert r.status == 200, "HTTP %d" % r.status
                while True:
                    b = r.read(1 << 20)
                    if not b:
                        break
                    h.update(b)
                    fh.write(b)
                    n += len(b)
            if n == nbytes and h.hexdigest() == sha:
                os.replace(dest + ".part", dest)
                return n, time.time() - t0, k
            last = "%d bytes sha256 %s, the set's %d %s" % (n, h.hexdigest(), nbytes, sha)
        except urllib.error.HTTPError as e:
            last = "HTTP %d" % e.code
            if e.code not in (403, 404, 429, 500, 502, 503, 504):
                break
        except (urllib.error.URLError, http.client.HTTPException, TimeoutError, ConnectionError, OSError) as e:
            last = "%s %s" % (type(e).__name__, e)
        if os.path.exists(dest + ".part"):
            os.remove(dest + ".part")
        sleep(min(60.0, 5.0 * 2 ** k))
    raise AssertionError("BLOCKED: %s/%s: %d attempts, the last %s" % (tag, asset, tries, last))

# ---- units: one slot held to the idle stretch, its streams downloaded, replayed and removed -------------------------


def run_unit(S, files, dl_dir, feed, timing, holdf=None, dl=None):
    """One slot: started where `holdf` allows, its stream files downloaded in index order and verified by bytes and
    SHA-256, fed to the day by `feed(paths)`, and removed whatever the replay did; its record appended to `timing`."""
    holdf, dl = holdf or hold, dl or download
    nbytes = sum(f["bytes"] for f in files)
    budget = 5 + -(-nbytes // DL_RATE) + UNIT_BUDGET_S
    start, waited = holdf(budget)
    free = free_bytes()
    assert free - nbytes >= DISK_FLOOR, "BLOCKED: %d bytes free, %d to download, the floor %d" % (
        free, nbytes, DISK_FLOOR)
    os.makedirs(dl_dir, exist_ok=True)
    paths, retries = [], 0
    t0 = time.time()
    try:
        for f in sorted(files, key=lambda f: int(SLOT_FILE_RE.fullmatch(f["file"]).group(2))):
            dest = os.path.join(dl_dir, f["asset"])
            _n, _secs, k = dl(f["tag"], f["asset"], f["bytes"], f["sha256"], dest)
            retries += k
            paths.append(dest)
        t1, c1 = time.time(), time.process_time()
        feed(paths)
        cpu = time.process_time() - c1
    finally:
        for p in paths:
            if os.path.exists(p):
                os.remove(p)
    end = time.time()
    W = int(start) // SLOT * SLOT
    rec = {"S": S, "window": W, "start_second": round(start - W, 3), "end_second": round(end - W, 3),
           "waited_s": round(waited, 3), "download_s": round(t1 - t0, 3), "replay_s": round(end - t1, 3),
           "cpu_s": round(cpu, 3), "bytes": nbytes, "retries": retries, "budget_s": budget,
           "inside": end <= W + IDLE[1]}
    with open(timing, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, sort_keys=True) + "\n")
    return rec


def timing_summary(path):
    recs = []
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            recs = [json.loads(ln) for ln in fh if ln.strip()]
    outside = [r for r in recs if not r["inside"]]
    if recs:
        out("units %d: inside the idle stretch %d, ending after second %d %d; longest %.1f s, download %.1f s and "
            "replay %.1f s at most; %.0f s waited; processor %.1f s; %d bytes downloaded; retries %d; windows %s to "
            "%s" % (len(recs), len(recs) - len(outside), IDLE[1], len(outside),
                    max(r["end_second"] - r["start_second"] for r in recs), max(r["download_s"] for r in recs),
                    max(r["replay_s"] for r in recs), sum(r["waited_s"] for r in recs),
                    sum(r["cpu_s"] for r in recs), sum(r["bytes"] for r in recs), sum(r["retries"] for r in recs),
                    utc(min(r["window"] for r in recs)), utc(max(r["window"] for r in recs))))
    for r in outside:
        out("unit %d started at second %.1f of window %d and ended at second %.1f" % (
            r["S"], r["start_second"], r["window"], r["end_second"]))
    return recs, outside


def slot_line(day, S):
    """A slot's record once the day has run to its end: the stream's counts, and each variant's sums over the
    members with a SHA-256 of every member's state - its position, cost, fills and reward."""
    c = day.c
    parts = ["%d lines %d frames %d fast %d skipped %d polls %d subscribes %d closes %d" % (
        S, c["lines"], c["frames"], c["fast"], c["skipped"], c["polls"], c["subscribes"], c["closes"])]
    for M in day.mk:
        for mv in M.mvs:
            day.flush(M, mv)
    for vi, sp in enumerate(day.specs):
        h = hashlib.sha256()
        nf = fhu = x = cost = 0
        rew = D(0)
        for M in day.mk:
            mv = M.mvs[vi]
            h.update(("%s %d %d %d %s\n" % (M.cid, mv.x, mv.cost, len(mv.fills), format(mv.rew, "f"))).encode())
            nf += len(mv.fills)
            fhu += sum(f for _a, _b, _c, f, _d in mv.fills)
            x += mv.x
            cost += mv.cost
            rew = C50.add(rew, mv.rew)
        parts.append("%s fills %d hu %d x %d cost %d rew %s state %s" % (sp.name, nf, fhu, x, cost, format(rew, "f"),
                                                                        h.hexdigest()[:16]))
    return " | ".join(parts)


def book_counts(day):
    book = {k: sum(M.c[k] for M in day.mk) for k in ("snapshots", "touch_equal", "book_equal", "matches")}
    book.update(subscribes=day.c["subscribes"], closes=day.c["closes"])
    return book


def day_rows_text(d0, rows, day):
    book = book_counts(day)
    doc = {"d0": d0, "counts": dict(day.c), "book": book,
           "rows": [{k: (format(r[k], "f") if k == "rew" else fr_text(r[k]) if k in ("reb", "pnl") else r[k])
                     for k in DAY_FILE_KEYS} for r in rows]}
    return dumps(doc).encode("utf-8")


def replay_day(d0, rec, polls, outcomes, dl_dir, timing, slots=None, holdf=None, dl=None, on_unit=None):
    """One member day replayed slot by slot; returns its slot lines and, where every slot ran, its rows."""
    day = Day(d0, members_read(rec))
    lines = []
    for s in rec["slots"][:slots]:
        u = run_unit(s["S"], s["files"], dl_dir, lambda paths, S=s["S"]: day.feed_slot(S, paths, polls), timing,
                     holdf, dl)
        lines.append(slot_line(day, s["S"]))
        if on_unit is not None:
            on_unit(u)
    if slots is not None and slots < len(rec["slots"]):
        return lines, None, day
    return lines, day.finish((d0 + DAY) * S_NS, {c: v for c, v in outcomes.items()}), day


class Projection:
    """After the first `after` units of this run, the replays' processor time projected over `total` bytes,
    BLOCKED above `cpu_max`."""

    def __init__(self, total, cpu_max, after=PROJECT_AFTER):
        self.total, self.cpu_max, self.after = total, cpu_max, after
        self.n, self.cpu, self.nb = 0, 0.0, 0

    def __call__(self, u):
        self.n += 1
        self.cpu += u["cpu_s"]
        self.nb += u["bytes"]
        if self.n == self.after:
            proj = self.cpu / self.nb * self.total
            out("projected %.0f s of replay for %d bytes after %d units at %.4f s a megabyte" % (
                proj, self.total, self.n, self.cpu / self.nb * 1e6))
            assert proj <= self.cpu_max, "BLOCKED: replay projected at %.0f s, above %d" % (proj, self.cpu_max)


def mode_replay():
    """Every member day not yet on disk, slot by slot (TZ-41 section 3.7); then G-BOOK over the days on disk."""
    floor_check()
    s = the_set()
    ddir = os.path.join(WORK, "days")
    os.makedirs(ddir, exist_ok=True)
    timing = os.path.join(WORK, "timing-replay.jsonl")
    todo = [d0 for d0 in s["members"] if not os.path.exists(os.path.join(ddir, "%d.json" % d0))]
    total = sum(s["days"][str(d0)]["bytes"] for d0 in todo)
    out("days to replay %d of %d, %d bytes of streams" % (len(todo), NEED, total))
    proj = Projection(total, REPLAY_CPU_MAX)
    for d0 in todo:
        rec, polls = day_inputs(d0)
        t0 = time.time()
        lines, rows, day = replay_day(d0, rec, polls, s["outcomes"], os.path.join(WORK, "dl"), timing, on_unit=proj)
        assert all(t >= (d0 + DAY) * S_NS for t, _c, _r in polls), "day %d: a poll left before its end" % d0
        st = write_once(os.path.join(ddir, "%d.slots.txt" % d0), ("\n".join(lines) + "\n").encode("utf-8"))
        sd = write_once(os.path.join(ddir, "%d.json" % d0), day_rows_text(d0, rows, day))
        out("day %d (%s) replayed in %.0f s: %d slots, %d lines; slots sha256 %s, day sha256 %s" % (
            d0, utc(d0), time.time() - t0, len(lines), day.c["lines"], st, sd))
        rec = polls = lines = rows = day = None    # one day held at a time
    timing_summary(timing)
    g_book(s)


def g_book(s):
    tot = collections.Counter()
    for d0 in s["members"]:
        b = load_json(os.path.join(WORK, "days", "%d.json" % d0))["book"]
        tot.update(b)
        out("day %d: book frames %d, the rebuilt touch equal at %d, every level equal at %d; matches %d; "
            "subscribes %d, closes %d" % (d0, b["snapshots"], b["touch_equal"], b["book_equal"], b["matches"],
                                          b["subscribes"], b["closes"]))
    ok = tot["snapshots"] > 0 and Fr(tot["touch_equal"], tot["snapshots"]) >= BOOK_EQUAL_MIN
    out("G-BOOK %s: the rebuilt touch equal to the venue's book frame at %d of %d frames, at least %s required; "
        "barred: every level equal at %d" % ("PASS" if ok else "FAIL", tot["touch_equal"], tot["snapshots"],
                                            BOOK_EQUAL_MIN, tot["book_equal"]))
    return ok


def mode_rescore():
    """DETERMINISM (TZ-41 section 4.4): the set's first day's first RESCORE_SLOTS slots replayed again from a second
    download; their lines equal the replay's."""
    floor_check()
    s = the_set()
    d0 = s["members"][0]
    with open(os.path.join(WORK, "days", "%d.slots.txt" % d0), encoding="utf-8") as fh:
        first = fh.read().split("\n")[:RESCORE_SLOTS]
    rec, polls = day_inputs(d0)
    total = sum(f["bytes"] for sl in rec["slots"][:RESCORE_SLOTS] for f in sl["files"])
    proj = Projection(total, RESCORE_CPU_MAX, after=6)
    lines, _rows, _day = replay_day(d0, rec, polls, s["outcomes"], os.path.join(WORK, "dl"),
                                    os.path.join(WORK, "timing-rescore.jsonl"), slots=RESCORE_SLOTS, on_unit=proj)
    write_once(os.path.join(WORK, "rescore.txt"), ("\n".join(lines) + "\n").encode("utf-8"))
    same = sum(1 for a, b in zip(lines, first) if a == b)
    out("DETERMINISM %s: %d of %d slot lines of day %d equal to the replay's" % (
        "PASS" if same == RESCORE_SLOTS == len(lines) else "FAIL", same, RESCORE_SLOTS, d0))

# ---- the reading: each day's money by variant, and L0's reading (TZ-41 section 4.5) ---------------------------------


def day_money(rows, name):
    """A day's money for one variant: the reward with the venue's 1-pUSD minimum, the rebate and the marks.
    pess and central pay a member's reward only where it reaches 1 on the day, opt the day's sum where it reaches 1;
    pess counts no rebate."""
    rs = [r for r in rows if r["variant"] == name]
    rew = [D(r["rew"]) for r in rs]
    if name == "opt":
        tot = sum(rew, D(0))
        paid = tot if tot >= 1 else D(0)
    else:
        paid = sum((x for x in rew if x >= 1), D(0))
    reb = sum((fr_of(r["reb"]) for r in rs), Fr(0)) if name != "pess" else Fr(0)
    pnl = sum((fr_of(r["pnl"]) for r in rs), Fr(0))
    total = Fr(paid) + reb + pnl
    return {"reward": sum(rew, D(0)), "paid": paid, "rebate": reb, "marks": pnl, "total": total,
            "markets": len(rs), "paying": sum(1 for x in rew if x >= 1), "fills": sum(r["fills"] for r in rs),
            "shares": Fr(sum(r["fill_hu"] for r in rs), SIZE_UNIT),
            "crossed": Fr(sum(r["crossed_hu"] for r in rs), SIZE_UNIT),
            "scored_h": Fr(sum(r["scored_ns"] for r in rs), 3600 * S_NS),
            "marks_by": dict(collections.Counter(r["mark"] for r in rs))}


def l0_reading(pess_days, opt_days, theta=THETA):
    """EARN where every pess day reaches theta, NO EARN where no opt day does, UNDECIDABLE otherwise; each false
    reading at most 2^-8 over eight independent days (TZ-41 section 4.5). Pure."""
    assert len(pess_days) == len(opt_days) == NEED
    earn = all(t >= theta for t in pess_days)
    no_earn = all(t < theta for t in opt_days)
    word = "EARN" if earn and not no_earn else "NO EARN" if no_earn and not earn else "UNDECIDABLE"
    return word, earn, no_earn


def power(q, n=NEED):
    return Fr(q) ** n


def mode_score():
    floor_check()
    s = the_set()
    rows_by = {d0: load_json(os.path.join(WORK, "days", "%d.json" % d0))["rows"] for d0 in s["members"]}
    for name, q in (("0.90", Fr(9, 10)), ("0.95", Fr(19, 20)), ("0.99", Fr(99, 100))):
        out("power: every pess day at or above %s with probability %s each: %s" % (THETA, name, q12(power(q))))
    out("false reading: 2^-%d = %s for each answer, under independent days" % (NEED, q12(Fr(1, 2 ** NEED))))
    book = g_book(s)
    res = {"days": {}, "variants": {}}
    for d0 in s["members"]:
        res["days"][str(d0)] = {name: day_money(rows_by[d0], name) for name, *_r in VARIANTS}
        for name, *_r in VARIANTS:
            e = res["days"][str(d0)][name]
            out("day %d %-7s total %s = paid %s of reward %s on %d of %d markets + rebate %s + marks %s; fills %d, "
                "%s shares, %s against crossing orders; scored %s h; marks %s%s" % (
                    d0, name, q12(e["total"]), q12(e["paid"]), q12(e["reward"]), e["paying"], e["markets"],
                    q12(e["rebate"]), q12(e["marks"]), e["fills"], q12(e["shares"]), q12(e["crossed"]),
                    q12(e["scored_h"]), e["marks_by"], "" if name in GATED else ", barred"))
    pess = [res["days"][str(d0)]["pess"]["total"] for d0 in s["members"]]
    opt = [res["days"][str(d0)]["opt"]["total"] for d0 in s["members"]]
    word, earn, no_earn = l0_reading(pess, opt)
    out("pess days at or above %s: %d of %d, the least %s; opt days below it: %d of %d, the most %s" % (
        THETA, sum(1 for t in pess if t >= THETA), NEED, q12(min(pess)), sum(1 for t in opt if t < THETA), NEED,
        q12(max(opt))))
    for name, *_r in VARIANTS:
        tot = sum((res["days"][str(d0)][name]["total"] for d0 in s["members"]), Fr(0))
        res["variants"][name] = {"total": tot, "per_day": tot / NEED}
        out("%s: over the %d days %s, a day %s%s" % (name, NEED, q12(tot), q12(tot / NEED),
                                                     "" if name in GATED else ", barred"))
    res["reading"] = word if book else None
    res["g_book"] = "PASS" if book else "FAIL"
    sha = write_once(os.path.join(WORK, "reading.json"), dumps(res).encode("utf-8"))
    out("L0 %s: EARN %s, NO EARN %s; reading.json sha256 %s" % (word if book else "not read, G-BOOK FAIL", earn,
                                                               no_earn, sha))

# ---- G-REHEARSAL: four of the archive's first assets, replayed as one stand-in hour (TZ-41 section 4.1) ----------------


def rehearsal_members(path, params=REHEARSAL_PARAMS):
    """The markets of the first seed after the first subscribe of `path`, in order of first appearance, each with
    its first book item's token as its first token, under the rehearsal's fixed parameters."""
    seen, order = {}, []
    subscribed = False
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        for line in fh:
            o = json.loads(line)
            if o.get("event") == "subscribe":
                subscribed = True
                continue
            raw = o.get("raw")
            if not subscribed or raw is None or not raw.startswith("["):
                continue
            for it in json.loads(raw):
                if isinstance(it, dict) and it.get("event_type") == "book" and it.get("market") not in seen:
                    seen[it["market"]] = it["asset_id"]
                    order.append(it["market"])
            break
    assert order, "%s: no seed after a subscribe" % path
    return [{"cid": c, "tok": seen[c], "ms": params["ms"], "vu": params["vu"], "rate": params["rate"],
             "fee": params["fee"]} for c in order]


def compare_lines(rows, book):
    """The figures G-REHEARSAL and the self-test compare with the Architect's independent replay: per member and
    variant, in the members' order, every figure at twelve places or as an integer; then the book's counts."""
    lines = []
    for r in rows:
        n = r["n"]
        lines.append("%s %s rew %s reb %s pnl %s x %d cost %d fills %d hu %d crossed %d scored_ns %d sent %d "
                     "cancels %d refused %d crossings %d mark %s" % (
                         r["cid"], r["variant"], q12(r["rew"]), q12(r["reb"]), q12(r["pnl"]), r["x"], r["cost"],
                         r["fills"], r["fill_hu"], r["crossed_hu"], r["scored_ns"], n["sent"], n["cancels"],
                         n["refused"], n["crossings"], r["mark"]))
    lines.append("book snapshots %d touch_equal %d book_equal %d matches %d subscribes %d closes %d" % tuple(
        book[k] for k in ("snapshots", "touch_equal", "book_equal", "matches", "subscribes", "closes")))
    return lines


def replay_paths(d0, members, slot_paths, end_s, polls=None):
    """A stand-in day: every slot's local files, in order; its rows at end_s and the book's counts."""
    day = Day(d0, members)
    pq = collections.deque(polls or ())
    for S, paths in slot_paths:
        day.feed_slot(S, paths, pq)
    rows = day.finish(end_s * S_NS, {})
    return rows, book_counts(day), day


def mode_rehearse():
    floor_check()
    dl_dir = os.path.join(WORK, "rehearsal-dl")
    os.makedirs(dl_dir, exist_ok=True)
    timing = os.path.join(WORK, "timing-rehearsal.jsonl")
    paths, c0 = [], time.process_time()
    try:
        for name, nbytes, sha in REHEARSAL_ASSETS:
            dest = os.path.join(dl_dir, name)
            start, waited = hold(5 + -(-nbytes // DL_RATE) + 5)
            assert free_bytes() - nbytes >= DISK_FLOOR, "BLOCKED: the disk floor"
            n, secs, k = download(REHEARSAL_TAG, name, nbytes, sha, dest)
            out("downloaded %s: %d bytes in %.1f s, sha256 %s, retries %d, held %.0f s" % (name, n, secs, sha, k,
                                                                                          waited))
            paths.append(dest)
        members = rehearsal_members(paths[0])
        c1 = time.process_time()
        slots = [(int(ASSET_RE.fullmatch(p.rsplit("/", 1)[1]).group(3)), [p]) for p in paths]
        start, waited = hold(UNIT_BUDGET_S)
        rows, book, day = replay_paths(REHEARSAL_D0, members, slots, REHEARSAL_D0 + 4 * SLOT)
        cpu = time.process_time() - c1
        assert cpu <= REHEARSAL_CPU_MAX, "BLOCKED: the rehearsal's replay took %.0f s" % cpu
    finally:
        for p in paths:
            if os.path.exists(p):
                os.remove(p)
    lines = compare_lines(rows, book)
    body = ("\n".join(lines) + "\n").encode("utf-8")
    write_once(os.path.join(WORK, "rehearsal.txt"), body)
    out("rehearsal: %d markets, %d lines of stream, %.1f s of processor, held %.0f s; %d lines sha256 %s" % (
        len(members), day.c["lines"], cpu, waited, len(lines), sha256_bytes(body)))
    same = len(lines) == REF["lines"] and sha256_bytes(body) == REF["digest"]
    out("G-REHEARSAL %s: %d lines sha256 %s against the Architect's %d lines sha256 %s" % (
        "PASS" if same else "FAIL", len(lines), sha256_bytes(body), REF["lines"], REF["digest"]))

# ---- the session's modes ------------------------------------------------------------------------------------


def mode_fingerprint():
    with open(os.path.join(PRIMARY, "SYSTEM-MAP.md"), "rb") as fh:
        raw = fh.read()
    txt = raw.decode("utf-8")
    rev = re.findall(r"^\*\*Revision string:\*\* `([^`]+)`$", txt, re.M)
    assert rev == [MAP_REVISION], "map revision %r, required %s" % (rev, MAP_REVISION)
    found = dict(ANCHOR_ROW.findall(txt))
    assert found == ANCHORS, "anchors %r" % found
    for k, rel in sorted(ANCHOR_FILES.items()):
        h = sha256_file(os.path.join(PRIMARY, rel))[:12]
        assert h == ANCHORS[k], "re-derived %s %s, the map %s" % (k, h, ANCHORS[k])
        out("re-derived %s %s sha256[:12] %s equal" % (k, rel, h))
    rows = ROW.findall(txt)
    states = {k: sum(1 for r in rows if r[3] == k) for k in MAP_ROWS}
    assert states == MAP_ROWS and len(rows) == sum(MAP_ROWS.values()), "rows %r" % states
    for path, lines, nbytes, state, sha in rows:
        with open(os.path.join(PRIMARY, path), "rb") as fh:
            blob = fh.read()
        got = (blob.count(b"\n"), len(blob), sha256_bytes(blob))
        if state == "frozen":
            want = (int(lines.replace(",", "")), int(nbytes.replace(",", "")), sha)
            assert got == want, "frozen row %s: %r, the map %r" % (path, got, want)
        out("%-48s %6d lines %8d bytes %s %s%s" % (path, got[0], got[1], got[2], state,
                                                  " equal" if state == "frozen" else ""))
    out("SYSTEM-MAP.md %d lines %d bytes sha256 %s" % (raw.count(b"\n"), len(raw), sha256_bytes(raw)))
    out("FINGERPRINT PASS: revision %s; anchors 6 of 6, 4 re-derived; rows %d: frozen %d of %d equal, tracked %d, "
        "reported %d" % (MAP_REVISION, len(rows), states["frozen"], MAP_ROWS["frozen"], states["tracked"],
                         states["reported"]))


def number_reading(names, own):
    """NUMBER, CANON hard rule 2: CryptoTZ/ holds this TZ's file and no other of its number; CryptoReports/ no report
    of it. Pure."""
    tz = [n for n in names if n.startswith("CryptoTZ/" + NUMBER)]
    rp = [n for n in names if n.startswith("CryptoReports/" + NUMBER)]
    return tz == [own] and not rp, tz, rp


def mode_number():
    names = git("ls-tree", "--name-only", "origin/main", "--", "CryptoTZ/", "CryptoReports/", tree=PRIMARY).split("\n")
    head = git("rev-parse", "origin/main", tree=PRIMARY)
    ok, tz, rp = number_reading(names, "CryptoTZ/TZ-41-l0-our-quote.md")
    out("origin/main %s: %d paths under CryptoTZ/ and CryptoReports/; of the number %s: %s and %s" % (
        head, len(names), NUMBER, tz, rp))
    out("NUMBER %s" % ("PASS - 2 of 2" if ok else "FAIL"))
    assert ok, "BLOCKED: of the number %s, CryptoTZ/ holds %s and CryptoReports/ %s" % (NUMBER, tz, rp)


def still_reading(before, now, restarts):
    """G-STILL from two reads and the pair book archive's restart records between them, in order: PASS where every
    unit is unchanged, or where every unit but the pair book is unchanged and its change is that archive's own
    restarts alone - a chain from the recorded MainPID to the current one, NRestarts one higher at each, the unit
    active. Pure."""
    if now == before:
        return True, "unchanged"
    for k in sorted(now):
        if k != "pairbook" and now[k] != before.get(k):
            return False, "the %s changed" % k
    b, n = before["pairbook"], now["pairbook"]
    pid, count = b["MainPID"], int(b["NRestarts"])
    for r in restarts:
        if str(r.get("stopped")) != pid or str(r.get("NRestarts")) != str(count + 1):
            return False, "a restart record that does not follow %s at NRestarts %d: %r" % (pid, count, r)
        pid, count = str(r.get("pid")), count + 1
    if restarts and pid == n["MainPID"] and str(count) == n["NRestarts"] and n["ActiveState"] == "active":
        return True, "changed by the pair book archive's own restarts alone: %d" % len(restarts)
    return False, "the pair book changed, %d restart records of its archive since the first read" % len(restarts)


def mode_still():
    st = load_state()
    now = {}
    for key, unit in sorted(UNITS.items()):
        kv = show(unit, ["MainPID", "NRestarts", "ActiveState", "MemoryCurrent", "MemoryPeak"])
        now[key] = {k: kv[k] for k in ("MainPID", "NRestarts", "ActiveState")}
        out("%s %s, MemoryCurrent %s, MemoryPeak %s" % (unit, now[key], kv.get("MemoryCurrent"), kv.get("MemoryPeak")))
    for key, (svc, timer) in sorted(ARCHIVES.items()):
        for unit in (timer, svc):
            out("%s %s" % (unit, show(unit, ["ActiveState", "SubState", "UnitFileState", "Result"])))
    if "still" not in st:
        st["still"] = {"at": utc(time.time()), "at_ns": time.time_ns(), "units": now}
        save_state(st)
        out("still: recorded")
        return
    _raw, recs, _tail = ledger_records(PB_LEDGER)
    since = st["still"]["at_ns"]
    restarts = [r for r in recs if r.get("event") == "restart" and r.get("wall_ns", 0) >= since]
    for r in restarts:
        out("the pair book archive's restart record %s: run %s, window %s, pid %s after %s, NRestarts %s" % (
            utc(r["wall_ns"] / 1e9), r.get("run"), r.get("W"), r.get("pid"), r.get("stopped"), r.get("NRestarts")))
    _raw, rrecs, _tail = ledger_records(RB_LEDGER)
    runs = sorted({r.get("run") for r in rrecs if r.get("wall_ns", 0) >= since and isinstance(r.get("run"), int)})
    out("the reward book archive's runs with records since the first read: %s" % runs)
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
    """The reward book archive's own record, read whole: its complete lines, its runs summarized, every complete
    run's set.json asserted by its set record's SHA-256, and the slots its assets reach."""
    svc, timer = ARCHIVES["rewardbook"]
    for unit in (timer, svc):
        out("%s %s" % (unit, show(unit, ["ActiveState", "SubState", "UnitFileState", "Result", "ExecMainStatus",
                                         "LastTriggerUSec", "NextElapseUSecRealtime"])))
    raw, recs, tail = ledger_records(RB_LEDGER)
    out("ledger %s: %d bytes sha256 %s, %d complete records, %d bytes of a line still written" % (
        RB_LEDGER, len(raw), sha256_bytes(raw), len(recs), len(tail)))
    for r in recs:
        out("L %s %s" % (utc(r["wall_ns"] / 1e9) if isinstance(r.get("wall_ns"), int) else "-",
                         json.dumps(r, sort_keys=True)))
    summ = ledger_summary(recs)
    for ln in summ["lines"]:
        out(ln)
    sets = archived_sets(recs)
    amap = asset_map(sets)
    for s in sets:
        ss = sorted(x["S"] for x in s["doc"]["assets"])
        out("set %s run %d sha256 %s: %d files, %d bytes, slots %s to %s" % (
            s["tag"], s["run"], s["sha256"], s["doc"]["assets_n"], s["doc"]["bytes_total"], ss[0] if ss else "-",
            ss[-1] if ss else "-"))
    slots = sorted({int(ASSET_RE.fullmatch(v["asset"]).group(3)) for v in amap.values()})
    after = [s for s in slots if s >= FIRST_D0]
    out("the archive's assets: %d files of %d slots, to slot %s; at or after %d: %d slots, to %s" % (
        len(amap), len(slots), slots[-1] if slots else "-", FIRST_D0, len(after), after[-1] if after else "-"))
    tags = sorted(ln.split("\t")[1][len("refs/tags/"):] for ln in git(
        "ls-remote", "origin", "refs/tags/rewardbook-streams-*", tree=PRIMARY).split("\n") if "\t" in ln)
    stags = [s["tag"] for s in sets]
    out("tags on origin %d: %s" % (len(tags), tags))
    out("complete runs' sets %d; their tags not on origin %s; halted %s; runs without a terminal record %s" % (
        len(stags), sorted(set(stags) - set(tags)), summ["halted"],
        [a for a, t in summ["terminal"].items() if not t]))
    assert REHEARSAL_TAG in stags, "BLOCKED: the rehearsal's set %s is not a complete run's" % REHEARSAL_TAG
    held = {(x["asset"], x["bytes"], x["sha256"]) for s in sets if s["tag"] == REHEARSAL_TAG
            for x in s["doc"]["assets"]}
    assert all(a in held for a in REHEARSAL_ASSETS), "BLOCKED: the rehearsal's assets differ from its set"
    out("the rehearsal's four assets are in set %s, bytes and SHA-256 equal" % REHEARSAL_TAG)


def report_tokens():
    tokens = set()
    for name in sorted(os.listdir(REPORTS)):
        if name.endswith(".md"):
            with open(os.path.join(REPORTS, name), encoding="utf-8", errors="replace") as fh:
                tokens.update(TOKEN.findall(fh.read()))
    return tokens


def by_name(tree, rel):
    return tree == WORK and (rel in ("state.json", "read-ledger.jsonl") or rel.startswith("logs/"))


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
                h = sha256_file(path)
                is_named = any(h[:k] in tokens for k in lengths)
                is_kept = by_name(tree, rel)
                if not (is_named or is_kept):
                    continue
                named += 1 if is_named else 0
                kept += 1 if is_kept and not is_named else 0
                dest = os.path.join(FORENSICS, os.path.basename(tree) + "--" + rel.replace("/", "--"))
                if os.path.exists(dest):
                    got = sha256_file(dest)
                    assert got == h, "reclaim: %s exists with sha256 %s, source %s" % (dest, got, h)
                    held += 1
                    out("R held   %s %s" % (h, dest))
                    continue
                with open(path, "rb") as src, open(dest, "xb") as dst:
                    shutil.copyfileobj(src, dst, 1 << 20)
                assert sha256_file(dest) == h, "reclaim: %s did not copy whole" % dest
                copied += 1
                out("R copied %s %s" % (h, dest))
    after = sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    assert after == before + copied, "reclaim: store %d, expected %d" % (after, before + copied)
    out("RECLAIM PASS: %d files considered, %d named by a report, %d kept by name, %d copied, %d already held; "
        "forensic store %d -> %d files" % (considered, named, kept, copied, held, before, after))


def read_ledger(mode):
    """The read ledger: one line a mode that reads the store, the archive's Releases or the set, with this file's
    SHA-256 and the work tree's HEAD."""
    with open(os.path.join(HERE, PYFILE), "rb") as fh:
        mine = sha256_bytes(fh.read())
    head = git("rev-parse", "HEAD") if os.path.isdir(WT) else None
    rec = {"mode": mode, "at": utc(time.time()), "at_ns": time.time_ns(), "file_sha256": mine, "head": head}
    with open(LEDGER, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, sort_keys=True) + "\n")
    out("read ledger: %s" % json.dumps(rec, sort_keys=True))


def main(argv):
    if not argv:
        sys.exit("usage: %s MODE [ARG...]" % PYFILE)
    mode, rest = argv[0], argv[1:]
    assert os.getcwd() == WORK, "run from %s, not %s" % (WORK, os.getcwd())
    MODE[0] = mode
    table = {"fingerprint": mode_fingerprint, "number": mode_number, "selftest": mode_selftest,
             "still": mode_still, "archive": mode_archive, "rehearse": mode_rehearse, "fetch": mode_fetch,
             "replay": mode_replay, "rescore": mode_rescore, "score": mode_score}
    if mode in ("rehearse", "fetch", "replay", "rescore", "score"):
        read_ledger(mode)
    if mode == "reclaim":
        mode_reclaim(rest)
    elif mode == "scratch":
        assert len(rest) == 1, "scratch OWN"
        mode_scratch(rest[0])
    else:
        assert mode in table and not rest, "unknown mode %r" % (argv,)
        table[mode]()
    out("malloc tuned: %s" % MALLOC_TUNED)
    out("peak memory of this run: %d bytes" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024))
    out("opens refused: %d; reward book opens: %d" % (len(REFUSED), COUNTS["reward book opens"]))

# ---- the self-test: literals, a synthetic day and temporary trees under the work tree ------------------------------

SYN_D0 = 1792800000          # 2026-10-24 00:00:00 UTC: a synthetic day, two slots
SYN = {"A": {"cid": "0x" + "a1" * 32, "tok": "1001", "other": "1002", "ms": 2000, "vu": 90, "rate": Fr(100),
             "fee": Fr(1, 80)},
       "B": {"cid": "0x" + "b2" * 32, "tok": "2001", "other": "2002", "ms": 5000, "vu": 70, "rate": Fr(50),
             "fee": Fr(0)}}


def _side(levels):
    return [{"price": p, "size": s} for p, s in levels]


def _book(m, ts, bids, asks, tick="0.01", tok=None):
    return {"market": m["cid"], "asset_id": tok or m["tok"], "timestamp": str(ts), "hash": "ab" * 20,
            "bids": _side(bids), "asks": _side(asks), "tick_size": tick, "event_type": "book",
            "last_trade_price": "0.5"}


def _pc(m, ts, side, price, size):
    """A price_change frame of market m: the first token's entry and its mirror on the other token, in the venue's
    key order and separators."""
    mirror = format(D(1) - D(price), "f").rstrip("0").rstrip(".") if D(price) != 0 else "1"
    other = "SELL" if side == "BUY" else "BUY"
    return {"market": m["cid"], "price_changes": [
        {"asset_id": m["tok"], "price": price, "size": size, "side": side, "hash": "cd" * 20, "best_bid": "0.4",
         "best_ask": "0.46"},
        {"asset_id": m["other"], "price": mirror, "size": size, "side": other, "hash": "ef" * 20, "best_bid": "0.54",
         "best_ask": "0.6"}], "timestamp": str(ts), "event_type": "price_change"}


def _line(h, frame=None, event=None, **kw):
    if event is not None:
        return json.dumps(dict({"recv_ns": h, "mono_ns": h - 10 ** 9, "event": event}, **kw), separators=(",", ":"))
    raw = frame if isinstance(frame, str) else json.dumps(frame, separators=(", ", ":"))
    return json.dumps({"recv_ns": h, "mono_ns": h - 10 ** 9, "raw": raw}, separators=(",", ":"))


def synth_lines(S, first):
    """Slot S's synthetic stream (TZ-41 section 4.1): host instants in ms after S, venue stamps 20 ms before."""
    A, B = SYN["A"], SYN["B"]
    ms = lambda off: S * 1000 + off
    hn = lambda off: (S * 1000 + off) * MS_NS
    out_ = [_line(hn(-5000), event="connect", seg=0), _line(hn(-4900), event="open", seg=0),
            _line(hn(-4800), event="subscribe", seg=0, tokens=4)]
    if first:
        seed = [_book(A, ms(-4020), [("0.4", "100"), ("0.38", "500")], [("0.46", "100"), ("0.48", "300")]),
                _book(A, ms(-4020), [("0.52", "300")], [("0.6", "100")], tok=A["other"]),
                _book(B, ms(-4020), [("0.6", "200")], [("0.62", "200")]),
                _book(B, ms(-4020), [("0.38", "200")], [("0.4", "200")], tok=B["other"])]
        out_.append(_line(hn(-4000), seed))
        steps = [(1000, _pc(A, ms(1000), "BUY", "0.39", "50")),
                 (10000, _pc(A, ms(10000), "BUY", "0.4", "70")),
                 (10010, _book(A, ms(10000), [("0.4", "70"), ("0.39", "50"), ("0.38", "500")],
                               [("0.46", "100"), ("0.48", "300")])),
                 (10011, _book(A, ms(10000), [("0.52", "300")], [("0.6", "70")], tok=A["other"])),
                 (10020, {"market": A["cid"], "asset_id": A["tok"], "price": "0.4", "size": "30", "fee_rate_bps": "0",
                          "side": "SELL", "timestamp": str(ms(10000)), "event_type": "last_trade_price"}),
                 (20000, _pc(A, ms(20000), "SELL", "0.47", "10")),
                 (30000, _pc(A, ms(30000), "SELL", "0.41", "50")),
                 (40000, _pc(A, ms(40000), "SELL", "0.41", "0")),
                 (50000, _pc(A, ms(50000), "BUY", "0.45", "10")),
                 (60000, _pc(A, ms(60000), "BUY", "0.45", "0")),
                 (60050, _pc(A, ms(60050), "BUY", "0.45", "5")),
                 (60200, _pc(A, ms(60200), "BUY", "0.45", "0")),
                 (61000, _pc(B, ms(61000), "SELL", "0.62", "150")),
                 (62000, _pc(B, ms(62000), "SELL", "0.66", "100")),
                 (62100, _pc(B, ms(62100), "SELL", "0.62", "0"))]
        for off, fr in steps:
            out_.append(_line(hn(off + 20), fr))
        out_.append(_line(hn(70020), event="close", code=1006, reason="closed", seg=0))
        out_ += [_line(hn(71000), event="connect", seg=1), _line(hn(71100), event="open", seg=1),
                 _line(hn(71200), event="subscribe", seg=1, tokens=4)]
        out_.append(_line(hn(72000), [
            _book(A, ms(71980), [("0.4", "70"), ("0.39", "50"), ("0.38", "500")],
                  [("0.46", "100"), ("0.47", "10"), ("0.48", "300")]),
            _book(B, ms(71980), [("0.6", "200")], [("0.66", "100")])]))
        out_.append(_line(hn(80020), "PONG"))
        out_.append(_line(hn(100020), _pc(B, ms(100000), "SELL", "0.65", "30")))
        out_.append(_line(hn(110020), _pc(B, ms(110000), "SELL", "0.65", "0")))
        out_.append(_line(hn(110030), _book(B, ms(110000), [("0.6", "200")], [("0.66", "100")])))
        out_.append(_line(hn(900500), _pc(A, ms(900480), "BUY", "0.4", "999")))
        out_.append(_line(hn(905000), event="close", code=1000, reason="end", seg=1))
    else:
        out_.append(_line(hn(-4000), [
            _book(A, ms(-4020), [("0.4", "80"), ("0.39", "50"), ("0.38", "500")],
                  [("0.46", "100"), ("0.47", "10"), ("0.48", "300")]),
            _book(B, ms(-4020), [("0.6", "200")], [("0.66", "100")])]))
        out_.append(_line(hn(-2000), _pc(A, ms(-2020), "BUY", "0.4", "90")))
        steps = [(20, _pc(A, ms(20), "BUY", "0.4", "85")),
                 (300000, {"market": A["cid"], "asset_id": A["tok"], "old_tick_size": "0.01",
                           "new_tick_size": "0.001", "timestamp": str(ms(300000)), "event_type": "tick_size_change"}),
                 (300100, _pc(A, ms(300100), "BUY", "0.39", "60")),
                 (600000, _pc(B, ms(600000), "BUY", "0.59", "40")),
                 (700000, _pc(B, ms(700000), "BUY", "0.63", "20"))]
        for off, fr in steps:
            out_.append(_line(hn(off + 20), fr))
        out_.append(_line(hn(905000), event="close", code=1000, reason="end", seg=0))
    return out_


def synth_day(dirpath, d0=SYN_D0, slow=False):
    """The synthetic day's two stream files under `dirpath`; with `slow`, every line written with a space after
    each colon, out of PC_LINE's reach, so that only the JSON path reads it."""
    paths = []
    for k, S in enumerate((d0, d0 + SLOT)):
        lines = synth_lines(S, k == 0)
        if slow:
            lines = [json.dumps(json.loads(ln), separators=(", ", ": ")) for ln in lines]
        p = os.path.join(dirpath, "%d.0.stream.jsonl.gz" % S)
        with open(p, "wb") as raw, gzip.GzipFile(fileobj=raw, mode="wb", compresslevel=9, mtime=0) as fh:
            fh.write(("\n".join(lines) + "\n").encode("utf-8"))
        paths.append((S, [p]))
    return paths


def synth_polls(d0=SYN_D0):
    A, B = SYN["A"]["cid"], SYN["B"]["cid"]
    t = lambda s: (d0 + s) * S_NS
    return [(t(5), A, (Fr(100), Fr(2))), (t(35), B, (Fr(50), Fr(1, 2))), (t(65), A, None), (t(80), A, (Fr(120), Fr(3))),
            (t(930), A, (Fr(120), Fr(3))), (t(931), B, (Fr(50), Fr(1, 2)))]


def synth_members():
    return [{k: m[k] for k in ("cid", "tok", "ms", "vu", "rate", "fee")} for m in (SYN["A"], SYN["B"])]


# the Architect's reference over the synthetic day: its lines and their SHA-256 (TZ-41 section 4.1)
SYN_REF = {"lines": 7, "digest": "04e6917ef2efbe42590a82967ef4e590033adefef27d41b8a278021330bd157b"}


def mode_selftest():
    import http.server
    import threading
    n = [0]

    def ok(cond, what):
        assert cond, "selftest: " + what
        n[0] += 1
        out("  ok  " + what)

    def fails(fn, exc=AssertionError):
        try:
            fn()
        except exc:
            return True
        return False

    tmp = os.path.join(WORK, "selftest-tmp")
    shutil.rmtree(tmp, ignore_errors=True)
    os.makedirs(tmp)
    # the constants
    ok(MALLOC_TUNED, "glibc took the 128 KiB mmap threshold and the two arenas")
    ok(utc(FIRST_D0) == "2026-10-31T00:00:00Z" and utc(LAST_D0) == "2026-11-13T00:00:00Z" and NEED == 8 and
       NONMEMBER_MAX == 6 and (LAST_D0 - FIRST_D0) // DAY + 1 == NEED + NONMEMBER_MAX,
       "candidates from 2026-10-31, at most 14 days to 2026-11-13, for 8 members")
    ok([v[0] for v in VARIANTS] == ["pess", "opt", "central"] and GATED == ("pess", "opt") and
       [s.name for s in SPECS] == ["pess", "opt", "central"] and all(s.L == 50 * MS_NS for s in SPECS) and
       (SPECS[0].front, SPECS[0].takers, SPECS[0].denom) == (False, True, "pess") and
       (SPECS[1].front, SPECS[1].takers, SPECS[1].denom) == (True, False, "opt") and
       (SPECS[2].front, SPECS[2].takers, SPECS[2].denom) == (False, True, "venue"),
       "three variants of one rule: pess behind and met by crossing orders, opt first and never, central the venue's")
    ok(THETA == D("10") and power(Fr(9, 10)) == Fr(43046721, 100000000) and
       q12(power(Fr(19, 20))) == "0.663420431289" and q12(power(Fr(99, 100))) == "0.922744694428" and
       Fr(1, 2 ** NEED) == Fr(1, 256) and Fr(1, 256) < Fr(5, 1000),
       "power 0.430467, 0.663420 and 0.922745 at 0.90, 0.95 and 0.99; each false reading 1/256, under 0.005")
    ok(DL_HEADERS == {"User-Agent": "btc-5m-twap-tz41", "Accept": "application/octet-stream"} and
       GAMMA_HEADERS == {"User-Agent": "btc-5m-twap-tz41", "Accept": "application/json"},
       "every request carries the TZ's two headers")
    lo = MEM_FLOOR - 1
    ok(MEM_FLOOR == 143592894 and memory_gate([MEM_FLOOR]) == (True, MEM_FLOOR) and
       memory_gate([lo, lo, MEM_FLOOR]) == (True, MEM_FLOOR) and memory_gate([lo] * 5) == (False, lo) and
       fails(lambda: memory_gate([MEM_FLOOR, lo])) and fails(lambda: memory_gate([lo] * 6)),
       "the memory gate: a read at the floor or above passes; below it the next read decides, five reads at most")
    reads, slept = iter([lo, lo - 7, MEM_FLOOR + 3, lo]), []
    floor_check(read=lambda: next(reads), sleep=slept.append, freef=lambda: DISK_GATE)
    reads2, slept2 = iter([lo] * 5), []
    ok(slept == [MEM_RETRY_S] * 2 and (MEM_RETRY_S, MEM_READS) == (60, 5) and
       fails(lambda: floor_check(read=lambda: next(reads2), sleep=slept2.append, freef=lambda: DISK_GATE)) and
       slept2 == [MEM_RETRY_S] * 4 and
       fails(lambda: floor_check(read=lambda: MEM_FLOOR, sleep=slept2.append, freef=lambda: DISK_GATE - 1)),
       "floor_check reads MemAvailable again every 60 s while below its floor, passes at the first read at it or "
       "above, BLOCKS where five reads are below; it BLOCKS below the disk gate")
    # the venue's numbers as exact integers
    ok([price_int(x) for x in ("0.5", "0.505", "1", "0", "0.07")] == [500, 505, 1000, 0, 70] and
       [size_int(x) for x in ("12.34", "5", "0.1", "1000000")] == [1234, 500, 10, 100000000],
       "prices in thousandths and sizes in hundredths, exactly")
    ok(all(fails(lambda t=t: price_int(t)) for t in ("0.5051", "1e-3", "-0.5", ".5", "0.5 ")) and
       all(fails(lambda t=t: size_int(t)) for t in ("1.234", "1e2", "-1", "")),
       "any other text of a price or a size is a failed assert")
    # the competitors' bounds against every split of the displayed sides among two and three makers
    def f12(a, b, inside):
        return 4 * max(3 * min(a, b), max(a, b)) if inside else 12 * min(a, b)
    worst = []
    for A_, B_ in ((4, 4), (3, 9), (12, 4), (6, 1), (0, 5), (8, 8)):
        for inside in (True, False):
            sums = set()
            for a1 in range(A_ + 1):
                for b1 in range(B_ + 1):
                    for a2 in range(A_ - a1 + 1):
                        for b2 in range(B_ - b1 + 1):
                            sums.add(f12(a1, b1, inside) + f12(a2, b2, inside) +
                                     f12(A_ - a1 - a2, B_ - b1 - b2, inside))
            hi, lo = envelope(A_, B_, inside)
            worst.append((max(sums) == hi, min(sums) == lo))
    ok(all(a and b for a, b in worst), "the competitors' most and least, x 12, equal the extremes over every split "
                                       "of six pairs of sides among three makers, inside [0.10, 0.90] and outside")
    # one share by hand: market A's book, our bid at 0.41 and ask at 0.45, 20 shares each
    m = Market(dict(SYN["A"]), SPECS)
    m.replace({400: 10000, 380: 50000}, {460: 10000, 480: 30000})
    m.seeded = True
    o_b, o_a = Order("b", 410, 2000), Order("a", 450, 2000)
    for mv in m.mvs:
        mv.resting = [o_b, o_a]
    dd = Day(SYN_D0, [])
    # mid 0.43; our distances 0.02, v 0.045: S = (25/45)^2; the book's 0.40 and 0.46 at 0.03: S = (15/45)^2
    sh = [Fr(*dd.share_of(m, mv, {})) for mv in m.mvs]
    q_ours = Fr(25, 45) ** 2 * 20
    A1 = B1 = Fr(15, 45) ** 2 * 100
    ok(sh[0] == q_ours / (q_ours + (2 * A1 + B1) / 3) and sh[1] == q_ours / (q_ours + (A1 + B1) / 4) and
       sh[2] == sh[0], "a share by hand: ours 20 (5/9)^2; the book's sides 100 (1/3)^2 each; pess against "
                       "(2A + B)/3, opt against (A + B)/4, the venue's before its first poll pess's")
    m.ven = ((Fr(2) * Fr(100) * m.vu * m.vu * SIZE_UNIT * 12).numerator, 1)
    sh = [Fr(*dd.share_of(m, mv, {})) for mv in m.mvs]
    ok(sh[0] == q_ours / (q_ours + 200) and sh[1] == q_ours / (q_ours + (A1 + B1) / 4) and
       sh[2] == q_ours / (q_ours + 200), "after a poll of competitiveness 2 at rate 100, the venue's 200: pess and "
                                          "central against it, opt against the book's least")
    # the synthetic day, against the Architect's reference and against its own rules by hand
    paths = synth_day(tmp)
    rows, book, day = replay_paths(SYN_D0, synth_members(), paths, SYN_D0 + 2 * SLOT, polls=synth_polls())
    lines = compare_lines(rows, book)
    body = ("\n".join(lines) + "\n").encode("utf-8")
    ok(len(lines) == SYN_REF["lines"] and sha256_bytes(body) == SYN_REF["digest"],
       "the synthetic day, %d lines, byte for byte the Architect's independent replay" % SYN_REF["lines"])
    f = {(M.cid[2:4], mv.sp.name): [(t // MS_NS - SYN_D0 * 1000, s, p, q, k) for t, s, p, q, k in mv.fills]
         for M in day.mk for mv in M.mvs}
    ok(f[("a1", "pess")] == [(10000, "b", 410, 2000, "m"), (50000, "a", 450, 1000, "x")] and
       f[("a1", "opt")] == [(10000, "b", 410, 2000, "m")] and f[("a1", "central")] == f[("a1", "pess")],
       "A: a sale of 30 at 0.40 fills our bid of 20 at 0.41, first; one minimum size long, no bid follows, so the ask "
       "placed at 0.41 meets none; a bid placed at 0.45 fills pess's and central's ask as a crossing order, never opt's")
    ok(f[("b2", "pess")] == f[("b2", "opt")] == [(110000, "a", 640, 3000, "m")],
       "B: once a 0.65 ask narrows the touch to five ticks and moves our ask to 0.64, a purchase of the 30 at 0.65 "
       "fills ours, 30 of 50")
    r = {(x["cid"][2:4], x["variant"]): x for x in rows}
    ok(r[("a1", "pess")]["n"]["refused"] == 1 and r[("a1", "opt")]["n"]["refused"] == 1 and
       r[("a1", "pess")]["x"] == 1000 and r[("a1", "pess")]["cost"] == 370000 and
       r[("a1", "pess")]["pnl"] == Fr(3, 5) and r[("a1", "pess")]["reb"] == Fr(73130, 80 * 10000),
       "A: an ask arriving after a bid of 0.45 came up is refused; pess long 10 at a cost of 3.70, marked at the "
       "day's last mid 0.43 for 0.60, its rebate 7.313 / 80")
    ok(r[("b2", "pess")]["pnl"] == Fr(-3, 20) and r[("b2", "pess")]["mark"] == "mid" and
       r[("a1", "pess")]["scored_ns"] == 1777770000000 and r[("a1", "opt")]["scored_ns"] == 1777720000000,
       "B: short 30 at 0.64 marked at 0.645; A scored 1,777.77 s of the 1,800 under pess and 1,777.72 under opt, "
       "unseeded from the close to the seed")
    ok(book == {"snapshots": 2, "touch_equal": 2, "book_equal": 2, "matches": 2, "subscribes": 1, "closes": 1} and
       day.c["polls"] == 6 and day.c["switches"] == 2 and day.c["skipped"] == 1,
       "2 book frames, both equal to the rebuilt book, 2 matches; 1 subscribe and 1 close inside the day, the "
       "slots' own before their instants not counted; 6 polls; the PONG skipped")
    slow = os.path.join(tmp, "slow")
    os.makedirs(slow)
    rows2, book2, day2 = replay_paths(SYN_D0, synth_members(), synth_day(slow, slow=True), SYN_D0 + 2 * SLOT,
                                      polls=synth_polls())
    ok(compare_lines(rows2, book2) == lines and day2.c["fast"] == 0 and day.c["fast"] == 19,
       "the same lines through the JSON path alone: the fast path read 19 frames, the slow 0")
    rows3, book3, _d3 = replay_paths(SYN_D0, synth_members(), paths, SYN_D0 + 2 * SLOT, polls=synth_polls())
    ok(compare_lines(rows3, book3) == lines, "a second replay of the same files: the same lines")
    # the day's money and L0's reading
    lit = [{"variant": v, "rew": "%s" % rw, "reb": "1/10", "pnl": "-1/2", "fills": 1, "fill_hu": 500,
            "crossed_hu": 0, "scored_ns": 3600 * S_NS, "mark": "mid", "cid": c}
           for v in ("pess", "opt", "central") for c, rw in (("x", "0.6"), ("y", "1.5"), ("z", "0.9"))]
    mp, mo, mc = (day_money(lit, v) for v in ("pess", "opt", "central"))
    ok(mp["total"] == Fr(3, 2) - Fr(3, 2) and mo["total"] == Fr(3) + Fr(3, 10) - Fr(3, 2) and
       mc["total"] == Fr(3, 2) + Fr(3, 10) - Fr(3, 2) and mp["paying"] == 1,
       "the 1-pUSD minimum: pess and central pay only a member's day at 1 or more, opt the day's sum; pess counts "
       "no rebate")
    T = THETA
    ok(l0_reading([T] * 8, [T] * 8) == ("EARN", True, False) and
       l0_reading([T] * 7 + [T - D("0.000001")], [T + 1] * 8) == ("UNDECIDABLE", False, False) and
       l0_reading([T - 1] * 8, [T - D("0.000001")] * 8) == ("NO EARN", False, True) and
       l0_reading([T] * 8, [T - 1] * 8) == ("UNDECIDABLE", True, True),
       "EARN at every pess day at 10 or more; NO EARN at every opt day below; both or neither UNDECIDABLE")
    # the slot rules
    good = {"S": SYN_D0, "index": 0, "day": SYN_D0, "selection": {"sha256": "s"}, "markets": 2, "error": None,
            "joined_late": False, "stream": {"opened": True, "off_reason": None, "file": "%d.0.stream.jsonl.gz" % SYN_D0,
                                             "cut": False, "max_gap_ns": GAP_MAX_NS, "subscribed_wall_ns":
                                                 SYN_D0 * S_NS - 1, "first_frame_wall_ns": SYN_D0 * S_NS,
                                             "last_frame_wall_ns": (SYN_D0 + SLOT) * S_NS}}
    am = {(SYN_D0, "%d.0.stream.jsonl.gz" % SYN_D0): {}}
    sp_ = lambda **kw: slot_problem(SYN_D0, [dict(good, **kw)], "s", 2, am, SYN_D0)
    st_ = lambda **kw: sp_(stream=dict(good["stream"], **kw))
    ok(sp_() is None and sp_(index=1) == "records: index 0" and sp_(markets=3) == "records: another selection" and
       sp_(error="x") == "records: an error" and st_(cut=True) == "stream: cut" and
       st_(max_gap_ns=GAP_MAX_NS + 1) == "stream: a gap above 15 s" and
       st_(subscribed_wall_ns=SYN_D0 * S_NS + 1) == "stream: subscribed late" and
       st_(last_frame_wall_ns=(SYN_D0 + SLOT) * S_NS - 1) == "stream: ended early" and
       slot_problem(SYN_D0, [good], "s", 2, {}, SYN_D0) == "stream: not archived" and
       slot_problem(SYN_D0, [], "s", 2, am, SYN_D0) == "no slot record",
       "a slot qualifies with its records whole, subscribed by S, to S + 900, no gap above 15 s, archived")
    g2 = dict(good, index=1, stream=dict(good["stream"], file="%d.1.stream.jsonl.gz" % SYN_D0,
                                          first_frame_wall_ns=(SYN_D0 + 20) * S_NS))
    g1 = dict(good, stream=dict(good["stream"], last_frame_wall_ns=(SYN_D0 + 4) * S_NS))
    am2 = dict(am)
    am2[(SYN_D0, "%d.1.stream.jsonl.gz" % SYN_D0)] = {}
    ok(slot_problem(SYN_D0, [g1, g2], "s", 2, am2, SYN_D0) == "stream: a gap above 15 s between files" and
       slot_problem(SYN_D0, [g1, dict(g2, stream=dict(g2["stream"], first_frame_wall_ns=(SYN_D0 + 19) * S_NS))],
                    "s", 2, am2, SYN_D0) is None, "two files: a gap above 15 s between them fails, 15 s does not")
    # the archive's record on a temporary tree
    state = os.path.join(tmp, "archive")
    os.makedirs(os.path.join(state, "runs", "1793263627"))
    doc = {"tag": "rewardbook-streams-1793263627", "assets_n": 1, "bytes_total": 7, "assets": [
        {"T": 1793232000, "S": 1793232000, "k": 0, "file": "1793232000.0.stream.jsonl.gz",
         "asset": "1793232000-1793232000.0.stream.jsonl.gz", "bytes": 7, "sha256": "aa" * 32}]}
    raw = json.dumps(doc).encode()
    with open(os.path.join(state, "runs", "1793263627", "set.json"), "wb") as fh:
        fh.write(raw)
    recs = [{"run": 1793263627, "event": "set", "sha256": sha256_bytes(raw), "tag": doc["tag"], "assets_n": 1,
             "bytes_total": 7, "wall_ns": 1}, {"run": 1793263627, "event": "complete", "wall_ns": 2},
            {"run": 1793300000, "event": "set", "sha256": "bb" * 32, "tag": "x", "assets_n": 0, "bytes_total": 0,
             "wall_ns": 3}]
    sets = archived_sets(recs, state)
    ok(len(sets) == 1 and asset_map(sets) == {(1793232000, "1793232000.0.stream.jsonl.gz"): {
        "tag": doc["tag"], "asset": doc["assets"][0]["asset"], "bytes": 7, "sha256": "aa" * 32}},
       "a complete run's set.json, asserted by its set record's SHA-256, maps its file; a run with no complete "
       "record maps nothing")
    ok(fails(lambda: asset_map(sets + sets)) and
       fails(lambda: archived_sets([dict(recs[0], sha256="cc" * 32), recs[1]], state)),
       "a file in two sets, or a set.json other than its record's, is a failed assert")
    # the store's readers on a temporary day
    store = os.path.join(tmp, "store")
    dday = os.path.join(store, str(SYN_D0))
    os.makedirs(dday)
    A, B = SYN["A"], SYN["B"]
    gdocs = [{"conditionId": c["cid"], "feesEnabled": c is A,
              "feeSchedule": {"rate": 0.05, "rebateRate": 0.25, "takerOnly": True, "exponent": 1}} for c in (A, B)]
    rep = (json.dumps({"kind": "gamma", "status": 200, "raw": json.dumps(gdocs)}) + "\n").encode()
    rgz = os.path.join(dday, "select.0.replies.jsonl.gz")
    with open(rgz, "wb") as raw_, gzip.GzipFile(fileobj=raw_, mode="wb", mtime=0) as fh:
        fh.write(rep)
    selrec = {"ok": True, "replies": {"sha256": sha256_file(rgz)}, "members": [
        {"condition_id": c["cid"], "token_ids": [c["tok"], c["other"]], "min_size": str(Fr(c["ms"], 100)),
         "max_spread": str(D(c["vu"]) / 20), "rate": str(c["rate"])} for c in (A, B)]}
    with open(os.path.join(dday, "select.0.json"), "w") as fh:
        fh.write(json.dumps(selrec))
    sel = selection_of(SYN_D0, store)
    mem = members_of(sel)
    ok(sel["attempt"] == 0 and [(x["cid"], x["tok"], x["ms"], x["vu"], x["rate"], x["fee"]) for x in mem] == [
        (A["cid"], "1001", 2000, 90, Fr(100), Fr(1, 80)), (B["cid"], "2001", 5000, 70, Fr(50), Fr(0))],
       "the selection's members: first token, size and spread as integers, the rate, and the rebate coefficient "
       "0.05 x 0.25 where fees are enabled, 0 where not")
    os.remove(os.path.join(dday, "select.0.json"))
    with open(os.path.join(dday, "select.0.json"), "w") as fh:
        fh.write(json.dumps(dict(selrec, ok=False)))
    ok(selection_of(SYN_D0, store) is None, "a day whose only attempt is not ok has no selection")
    pz = os.path.join(dday, "%d.0.rewards.jsonl.gz" % SYN_D0)
    prow = lambda c, rate, comp, more=(): json.dumps({"data": [{"condition_id": c, "market_competitiveness": comp,
                                                              "rewards_config": [{"rate_per_day": rate}] +
                                                              list(more)}]})
    cfgs = ({"rate_per_day": 999, "start_date": "1970-01-02", "end_date": "2500-12-31"},
            {"rate_per_day": 0.5, "start_date": "1969-12-31", "end_date": "1970-01-01"})
    lines_p = [{"recv_wall_ns": 7, "condition_id": B["cid"], "status": 200, "raw": prow(B["cid"], 50, 0.5)},
               {"recv_wall_ns": 5, "condition_id": A["cid"], "status": 200, "raw": prow(A["cid"], 100, 2.25, cfgs)},
               {"recv_wall_ns": 6, "condition_id": A["cid"], "status": 503, "raw": None},
               {"recv_wall_ns": 8, "condition_id": A["cid"], "status": 200, "raw": json.dumps({"data": []})}]
    with open(pz, "wb") as raw_, gzip.GzipFile(fileobj=raw_, mode="wb", mtime=0) as fh:
        fh.write(("\n".join(json.dumps(x) for x in lines_p) + "\n").encode())
    pls, cnt = polls_of(SYN_D0, {SYN_D0: [{"rewards": {"file": os.path.basename(pz)}}]}, store)
    ok(pls == [(5, A["cid"], (Fr(201, 2), Fr(9, 4))), (7, B["cid"], (Fr(50), Fr(1, 2))), (8, A["cid"], None)] and
       cnt == {"polls": 4, "unserved": 1, "no row": 1},
       "the polls in order received: rate and competitiveness exact from their text, the rate summed over the "
       "configurations in force on the poll's date; an unserved poll dropped, a page with no row kept as the end of "
       "the reward")
    pf_path = os.path.join(tmp, "polls.jsonl")
    with open(pf_path, "w", encoding="utf-8") as fh:
        fh.write(polls_text(pls))
    pf = polls_read(pf_path)
    seen = [bool(pf), pf[0]]
    first = pf.popleft()
    ok(isinstance(pf, PollFile) and seen == [True, pls[0]] and first == pls[0] and pf[0] == pls[1] and
       list(pf) == pls[1:] and not pf and pf.fh is None and fails(lambda: pf.popleft()) and
       fails(lambda: polls_read(pf_path)[1]),
       "a day's polls read back from their file one line at a time, as a deque: the front, popleft, the rest in "
       "order, the file closed at its end")
    # the documents: an outcome only where a market reads closed with prices exactly 0 and 1
    dc = lambda closed, prices: {"closed": closed, "outcomePrices": json.dumps(prices),
                                 "clobTokenIds": json.dumps(["1001", "1002"])}
    ok(outcome_of(dc(True, ["1", "0"]), "1001") == 1000 and outcome_of(dc(True, ["1", "0"]), "1002") == 0 and
       outcome_of(dc(True, ["0.5", "0.5"]), "1001") is None and outcome_of(dc(False, ["1", "0"]), "1001") is None,
       "the first token's outcome, 1 or 0, from a closed document's prices; none otherwise")
    calls = []

    def fake_get(q):
        qs = urllib.parse.parse_qs(q)
        calls.append(qs)
        ids = qs["condition_ids"]
        closed = qs.get("closed") == ["true"]
        docs = [dict(dc(closed, ["0", "1"]), conditionId=i) for i in ids if i.endswith("1") == closed]
        return docs, 10, "dd" * 32, 0
    toks = {"0x" + "%063x1" % k if k % 2 else "0x" + "%063x2" % k: "1001" for k in range(60)}
    oc, reqs = documents(toks, holdf=lambda b: (0, 0), get=fake_get)
    ok(len(calls) == 4 and len(reqs) == 4 and all(len(c["condition_ids"]) <= DOC_CHUNK for c in calls) and
       sum(1 for v in oc.values() if v == 0) == 30 and sum(1 for v in oc.values() if v is None) == 30,
       "60 members in chunks of 50, each read open and closed: 30 closed at 0 for the first token, 30 open")
    ok(fails(lambda: documents(toks, holdf=lambda b: (0, 0), get=lambda q: ([], 2, "ee" * 32, 0))),
       "a member whose document neither request returns is a failed assert")
    # the clock
    st_idle = lambda: {"pairbook": "inactive", "rewardbook": "inactive"}
    ok(quiet(SYN_D0 + 900 * 10 + 15, 45, st_idle) is None and
       quiet(SYN_D0 + 900 * 10 + 14, 45, st_idle) == "second 14 of the window" and
       quiet(SYN_D0 + 900 * 10 + 546, 45, st_idle) == "second 546 of the window" and
       quiet(SYN_D0 + 900 * 4 + 20, 45, st_idle) is None and
       quiet(SYN_D0 + 5430, 20, st_idle) == CALENDAR[0][1] and
       quiet(SYN_D0 + 10820 + 10, 20, st_idle) == CALENDAR[1][1] and
       quiet(SYN_D0 + 900 * 10 + 15, 45, lambda: {"pairbook": "activating"}) is not None,
       "a unit starts from second 15 and ends by 590, clear of both archives' calendar runs and of their services")
    clk = [float(SYN_D0 + 900 * 10 + 580)]
    t_, w_ = hold(45, clock=lambda: clk[0], sleep=lambda s: clk.__setitem__(0, clk[0] + s), state_of=st_idle)
    ok(t_ == SYN_D0 + 900 * 11 + 15 and w_ == 335, "held from second 580 to the next window's second 15")
    # the reading's purity: G-STILL and NUMBER
    u = {"recorder": {"MainPID": "1", "NRestarts": "0", "ActiveState": "active"},
         "pairbook": {"MainPID": "2", "NRestarts": "3", "ActiveState": "active"},
         "rewardbook": {"MainPID": "4", "NRestarts": "1", "ActiveState": "active"},
         "advisor": {"MainPID": "5", "NRestarts": "0", "ActiveState": "active"}}
    u2 = json.loads(json.dumps(u))
    u2["pairbook"] = {"MainPID": "9", "NRestarts": "4", "ActiveState": "active"}
    u3 = json.loads(json.dumps(u2))
    u3["rewardbook"]["MainPID"] = "6"
    ok(still_reading(u, u, [])[0] and still_reading(u, u2, [{"stopped": "2", "NRestarts": "4", "pid": "9"}])[0] and
       not still_reading(u, u2, [])[0] and not still_reading(u, u3, [{"stopped": "2", "NRestarts": "4", "pid": "9"}])[0],
       "G-STILL: unchanged, or the pair book moved by its archive's restarts alone; any other change fails")
    names = ["CryptoTZ/TZ-40-strong-every-rank.md", "CryptoTZ/TZ-41-l0-our-quote.md", "CryptoReports/TZ-40-x-report.md"]
    ok(number_reading(names, "CryptoTZ/TZ-41-l0-our-quote.md")[0] and
       not number_reading(names + ["CryptoTZ/TZ-41-other.md"], "CryptoTZ/TZ-41-l0-our-quote.md")[0] and
       not number_reading(names + ["CryptoReports/TZ-41-l0-our-quote-report.md"],
                          "CryptoTZ/TZ-41-l0-our-quote.md")[0], "NUMBER: this file alone of its number, no report")
    # the hook
    ok(policy("fetch", "open", (RB_ROOT + "/%d/select.0.json" % FIRST_D0, "rb")) is None and
       policy("fetch", "open", (RB_ROOT + "/%d/select.0.json" % (FIRST_D0 - DAY), "rb")) is not None and
       policy("replay", "open", (RB_ROOT + "/%d/select.0.json" % FIRST_D0, "rb")) is not None and
       policy("fetch", "open", (RB_ROOT + "/%d/%d.0.stream.jsonl.gz" % (FIRST_D0, FIRST_D0), "rb")) is not None and
       policy("fetch", "os.listdir", (RB_ROOT + "/%d" % FIRST_D0,)) is None and
       policy("fetch", "os.listdir", (RB_ROOT,)) is not None and
       policy("archive", "open", (RB_LEDGER, "rb")) is None and policy("score", "open", (RB_LEDGER, "rb")) is not None
       and policy("still", "open", (PB_LEDGER, "rb")) is None and
       policy("replay", "urllib.Request", ("https://github.com/x",)) is None and
       policy("fetch", "urllib.Request", ("https://github.com/x",)) is not None and
       policy("fetch", "urllib.Request", ("https://gamma-api.polymarket.com/markets?x",)) is None and
       policy("replay", "urllib.Request", ("https://clob.polymarket.com/x",)) is not None and
       policy("replay", "open", (RECORDER + "/x", "rb")) is not None and
       policy("replay", "open", ("/root/elsewhere", "wb")) is not None and
       policy("reclaim", "open", (FORENSICS + "/x", "xb")) is None and
       policy("reclaim", "open", (FORENSICS + "/x", "wb")) is not None and
       policy("replay", "subprocess.Popen", ("curl", ["curl"])) is not None,
       "the hook: the store's day files to fetch alone and for the span's days, never a stream; each archive's "
       "record to its modes; Release downloads, gamma and nothing else; no write outside the work tree but the "
       "forensic store's exclusive creates; no process but git, systemctl and stat")
    # downloads on the loopback: a good asset, a corrupt reply retried, a 404 given up
    blob = b"stream bytes" * 1000
    hits = collections.Counter()

    class H(http.server.BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_GET(self):
            hits[self.path] += 1
            if self.path == "/t/bad" and hits[self.path] == 1:
                body = b"x" * len(blob)
            elif self.path in ("/t/good", "/t/bad"):
                body = blob
            else:
                self.send_response(404)
                self.end_headers()
                return
            self.send_response(200)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
    srv = http.server.HTTPServer(("127.0.0.1", 0), H)
    th = threading.Thread(target=srv.serve_forever, daemon=True)
    th.start()
    try:
        url_of = lambda t, a: "http://127.0.0.1:%d/%s/%s" % (srv.server_port, t, a)
        dest = os.path.join(tmp, "dl")
        n1 = download("t", "good", len(blob), sha256_bytes(blob), dest, url_of=url_of, sleep=lambda s: None)
        n2 = download("t", "bad", len(blob), sha256_bytes(blob), dest + "2", url_of=url_of, sleep=lambda s: None)
        ok(n1[0] == n2[0] == len(blob) and n1[2] == 0 and n2[2] == 1 and sha256_file(dest) == sha256_bytes(blob) and
           not os.path.exists(dest + "2.part"), "a download verified by bytes and SHA-256; a corrupt reply retried")
        ok(fails(lambda: download("t", "gone", 1, "ff" * 32, dest + "3", url_of=url_of, sleep=lambda s: None)) and
           hits["/t/gone"] == DL_TRIES, "a 404, as a repository not serving its Releases answers, is tried %d times, "
                                        "then BLOCKED" % DL_TRIES)
    finally:
        srv.shutdown()
        srv.server_close()
    # a unit removes its files whatever the replay does, and the projection blocks
    fake = lambda t, a, nb, sha, dst: (open(dst, "wb").close(), (0, 0.0, 0))[1]
    tim = os.path.join(tmp, "timing.jsonl")
    fl = [{"file": "%d.0.stream.jsonl.gz" % SYN_D0, "tag": "t", "asset": "a0", "bytes": 1, "sha256": "x"}]
    ok(fails(lambda: run_unit(SYN_D0, fl, os.path.join(tmp, "u"), lambda p: 1 / 0, tim, holdf=lambda b: (0.0, 0),
                              dl=fake), ZeroDivisionError) and not os.listdir(os.path.join(tmp, "u")),
       "a unit whose replay fails leaves no file behind")
    pj = Projection(10 ** 9, 100, after=2)
    pj({"cpu_s": 1.0, "bytes": 10 ** 6})
    ok(fails(lambda: pj({"cpu_s": 1.0, "bytes": 10 ** 6})), "a replay projected above its bound stops BLOCKED")
    shutil.rmtree(tmp)
    out("SELFTEST PASS: %d checks" % n[0])


if __name__ == "__main__":
    main(sys.argv[1:])
```
