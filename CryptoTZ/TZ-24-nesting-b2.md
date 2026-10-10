# TZ-24 — B2: does the nesting break on executable quotes?

**Canonical filename:** `TZ-24-nesting-b2.md`. The committed file takes this name and no other.

**Executor model: Opus.** The first read of a capture no one has opened, reads of the venue over the network, and a
gate's arithmetic.

**Required System Map revision:** `2026-10-10-a`.

**Required anchors**, from map §0. A mismatch on any one is BLOCKED before any work:

| anchor | required |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `0f6c90451cbd` |
| `A6` — pricer | `729f0bcdbee3` |

**Host gate:** §0.3. This TZ runs on the capture host: it reads the chain book's stored windows, read only, and
nothing of the recorder's capture.

**When:** any time after the upload that carries this TZ and revision `2026-10-10-a`. Every window it reads closed
by 2026-10-05 23:15 UTC.

**What this TZ is.** The backup track's B2 (CANON PART II). Over every window the chain book stored from
`1790184600`, 2026-09-23 17:30 UTC, to `1791241200`, 2026-10-05 23:00 UTC, it asks whether the executable asks of
`btc-updown-15m-{T}` and `btc-updown-5m-{T+600}` ever priced a dominated pair below what the pair pays at
settlement, after both legs' taker fees. Three answers: **VIOLATION** — a member holds a firm violation;
**NONE** — no member holds a violation of any class, among at least 528 whose every checkpoint read valid, read
from an exact test at `0.005`; **UNDECIDABLE** — neither. No pricer, no `sigma`, no direction: the containment is
CANON §1.1's measured nesting, re-measured on every member from the venue's own settled documents. One instrument,
`research/tz24-nesting-b2.py`, Appendix A.

---

## 0. Gates

### 0.0 The work tree, first

After contract §1 steps 1 and 2, and before anything else:

```
mkdir /root/tz24-work /root/tz24-work/logs; echo "exit=$?"
```

`exit=0` proves neither existed; anything else is BLOCKED. **From here every command's output goes to
`/root/tz24-work/logs/`, one file per step, §0's included**, and nothing to the session's scratchpad. The one
exception is B-RECLAIM-OWN, §9.

### 0.1 The instrument, staged

Extract Appendix A from this TZ as the primary checkout carries it after contract §1's pull, with this script,
verbatim, its one argument the destination:

```
/root/tz01-env/venv/bin/python -B - /root/tz24-work/stage <<'EOF'
import hashlib, os, sys
SRC = "/root/btc-5m-twap/CryptoTZ/TZ-24-nesting-b2.md"
DEST = sys.argv[1]
WANT = {
    "research/tz24-nesting-b2.py": "4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b",
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
| `research/tz24-nesting-b2.py` | 1,535 | 76,142 | `4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b` |

A failed assert is BLOCKED. The staged copy runs one mode only, §0.2's `fingerprint`, and is written **`I0`**:
`nice -n 19 /root/tz01-env/venv/bin/python -B /root/tz24-work/stage/research/tz24-nesting-b2.py`.

### 0.2 Fingerprint

`I0 fingerprint` performs contract §1 steps 3 and 4 inside the instrument and asserts them (map §7 item 98's
rule), against `SYSTEM-MAP.md` and the files of its §0 table in the primary checkout `/root/btc-5m-twap`: revision
`2026-10-10-a`; the six anchors; `A2`, `A4`, `A5` and `A6` re-derived as the first 12 hex characters of those files'
SHA-256; the table's **33** rows, each printed in lines, bytes and SHA-256 — **30** `frozen` rows asserted equal to
the map, **2** `tracked` and **1** `reported`. It prints `FINGERPRINT PASS` or stops at the first mismatch, which is
BLOCKED.

### 0.3 Host gate

From `/root/btc-5m-twap`, with `S` first set to the scratchpad directory the session's system prompt names (map §7
item 98's rule), output verbatim into `logs/03-host-gate.log`:

```
date -u; date -u +%s
nproc; grep -E '^(MemTotal|MemAvailable|SwapTotal|SwapFree):' /proc/meminfo
df -B1 --output=source,size,avail /var/lib/btc-recorder
find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
grep -c e3975b5da44c5328adf3bf3914634cd878842c73 /var/lib/btc-recorder/runtime.jsonl
test -d /var/lib/btc-chainbook/1790184600; echo "chainbook exit=$?"
systemctl is-active btc-recorder.service btc-chainbook.service; echo "exit=$?"
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
systemctl is-active telemetry-watch.service; echo "exit=$?"
git -C /root/btc-recorder-svc rev-parse HEAD
for d in /root/tz23-work /root/tz18a-svc /root/btc-recorder-svc; do test -e "$d"; echo "$d exit=$?"; done
find /root/btc-forensics -type f | wc -l
/root/tz01-env/venv/bin/python -c 'import sys, numpy; print(sys.version.split()[0], numpy.__version__)'
git worktree list
du -sb /root/.claude /root/PROJECT_GAMING_PS5
echo "$S"; ls -la "$(dirname "$(dirname "$S")")"
```

- **H1** — `find` prints exactly one path.
- **H2** — `df` names source `/dev/vda2` and size `31612203008`; `grep -c` prints at least `1`, the recorder's own
  record of TZ-21's restart. With H1 this is map §6's host identity.
- **H3** — the interpreter prints `3.12.` and a numpy version.
- **H4** — `chainbook exit=0`: the chain book's first window directory, written on 2026-09-23 by TZ-18a's service
  (map §2.5).
- **Memory gate** — `MemAvailable` at least `141,189,120` bytes (§0.4).
- **Disk gate** — `avail` at least `2,400,000,000` bytes (§0.4).

Any of these six failing is BLOCKED. **The rest is printed and carries no threshold:** both units' state, which
G-STILL reads (§4.4); `telemetry-watch.service`'s two states, on which map §6's headroom is conditional; the
recorder's tree, which map §6 puts at `e3975b5…`; the three trees, `/root/tz23-work` absent by map §3; the forensic
store's count, map §3's `1,561`; the worktrees; `du`; and the listing of `S`'s parent, whose UUID directories
`I scratch` names live or earlier (§9).

### 0.4 Resource floors, in exact bytes

**Disk.** `/dev/vda2` free at least **`2,400,000,000`** bytes: the chain book's own floor, `RESOURCE_FLOOR` =
`2,200,000,000` (`research/tz18a-chainbook-capture.py` line 79), plus `200,000,000` for this session. The session
writes far less, in the Architect's runs: the worktree, `5,014,911` bytes of tracked files at `d4857c3` before this
upload; the set's document cache, at most 118 responses at the rehearsal's `9,407` bytes each, about `1,110,000`;
`set.json` at the rehearsal's `706` bytes a member, about `830,000`; the units file at most `1,424,593` bytes, written
for 1,175 synthetic members; the rehearsal `329,261`; the logs under `2,000,000`: under `15,000,000` in all, of which
§9 keeps under `6,000,000` in the forensic store.

**Memory.** `MemAvailable` at least **`141,189,120`** bytes: twice the largest peak any mode reached in the
Architect's runs under Python 3.12.3 — `score` over 1,175 synthetic members, every considered window a member,
`70,594,560` bytes. That run's books held `13,189` bytes a reply, `74,923` stored a window against the chain book's
own `28,467` (map §2.5): the peak is taken at the population's upper bound and above the stored size (map §7 item
97's rule). The other modes peaked at `43,495,424` (`selftest`), `36,098,048` (`fetch`, on the synthetic book),
`32,575,488` (`constants`) and `29,147,136` (`rehearse`). **`rehearse`, `fetch`, `constants` and `score` assert at
their start that glibc took its two settings, re-read `MemAvailable`, and stop BLOCKED on either.** Map §6 records
the host's memory: `1,002,127,360` bytes in all, one processor; TZ-23 read `255,062,016` to `327,110,656` available
with its session open. Every mode runs under `nice -n 19`.

### 0.5 Refs

`git ls-remote origin` before §3.1's push, every ref reported. Map §1 records `main` at
`d4857c3a95097d7b500a0b86c09b6283599663bc`, PR #23's merge, `tz-23-maker-m0` at `7f5ae3f`, and **28** ref lines. The
upload that carries revision `2026-10-10-a` and this TZ sits above `d4857c3`, in one commit or more; every commit on
`main`'s first-parent line above it is reported with the paths it changed. A difference is recorded, not BLOCKING,
unless `main` does not carry revision `2026-10-10-a` or `refs/heads/tz-24-nesting-b2` already exists — either is
BLOCKED.

---

## 1. Why this TZ exists

**The question** — CANON PART II, the backup track. B0 measured that `btc-updown-15m-{T}` and
`btc-updown-5m-{T+600}` settle on one published reading at `T+900` (TZ-17; TZ-18 G-CHAIN, 1,000 of 1,000 by
literal); B1, that the chain book reads both books at one instant (TZ-18a). B2 asks whether the books ever priced
that nesting wrong by more than two taker fees. It uses no pricer and no direction.

**The containment.** For a window `T`, `R0` is the fifteen-minute market's `priceToBeat`, `R600` the five-minute
market's, and `R900` the reading both settle on, each one's `finalPrice`. The fifteen-minute market resolves Up iff
`R900 >= R0`, the five-minute iff `R900 >= R600`. With `D = R600 − R0`:

- **pair A**, where `D >= 0`: one share of fifteen-minute Up and one of five-minute Down. It pays 2 where
  `R0 <= R900 < R600` and 1 in every other state;
- **pair B**, where `D <= 0`: one share of five-minute Up and one of fifteen-minute Down, symmetrically.

At `D = 0` both pairs pay exactly 1. **A pair is violated at a checkpoint** when its two shares cost less than 1
after both taker fees: a payment of at least 1 bought for less. `R0` and `R600` are readings at `T` and `T+600`, both
past at every checkpoint, so the dominated pair is fixed before the first read; B2 takes `D` from the venue's own
literals after settlement. A live reader would reconstruct it from the feed, wrong about one time in a hundred
(CANON §1.1) — a question of capture, not of existence.

**Every member re-measures the nesting** from its own two settled documents: **E1** — the two `finalPrice`
literals are one text; **E2** and **E3** — each market's outcome is Up iff its `finalPrice` is at or above its
`priceToBeat`. A window failing one is not a member, and its reason is printed.

**The cost.** Each leg is bought at its **executable ask**: the lowest ask carrying at least the venue's minimum
size, `tz14.touch_of` on the reply's own `min_order_size` and `tick_size`, as TZ-15 and TZ-16a bought — the only
implementation of the executable touch (map §0). Each leg pays CANON §1.1's taker fee, `tz14.fee_pp(a)`, `0.07 · a ·
(1 − a)` a share, the only implementation of the fee. **How the venue collects the fee — in USDC beside the price, or
in shares out of what is bought — no TZ has read**, so both are computed: `k_top = Σ (a + fee(a))`, the fee beside
the price; and `k_shares = Σ a / (1 − fee(a) / a)`, the cost of one share net of a fee taken in shares, never below
`k_top`.

**Coexistence.** The chain book releases the four reads of a checkpoint together (`research/tz18a-chainbook-capture.py`
lines 652 to 663); TZ-18a's proof received them `1.19` to `28.43` ms apart. A violation needs both asks at one
instant, so a firm one asks it twice: the two replies **received at most `150,000,000` ns apart** by the host's
monotonic clock, and **the two books' own `timestamp`s at most `150` ms apart** — the venue's instant, compared
directly (CANON PART III). `150` ms is the crypto taker delay (CANON §1.1): two asks farther apart than one delay
cannot be shown to have stood together for a taker. The chain book's own completeness bound, one second (line 90),
is not used: it admits pairs no taker could have filled together.

**Classes**, per checkpoint and dominated pair:

| class | condition |
|---|---|
| **firm** | `k_shares < 1`, the two replies received at most 150 ms apart, the two books' timestamps at most 150 ms apart |
| **loose** | `k_top < 1` and not firm; its reason printed — `convention` where `k_shares >= 1`, `apart` where a gap exceeds 150 ms, `no time` where a time is missing |
| **none** | `k_top >= 1` |
| **unquoted** | a leg has no ask at the minimum size |

**The chain book's record** (map §2.5; `research/tz18a-chainbook-capture.py`). Each window `T` has a directory
`/var/lib/btc-chainbook/{T}/` with `documents.jsonl`; `books.jsonl.gz`, one line per read, 28 a window, each with
exactly the fifteen keys of `BOOK_KEYS` (line 675) and the reply verbatim in `raw` beside its status, byte count and
SHA-256 (lines 454 to 465 and 751); and `window.json` (line 781), with `documents_ok`, `checkpoints_complete`,
`missed`, and for each market its slug, `clobTokenIds`, `outcomes` and `conditionId`. Seven checkpoints, `T+655` to
`T+885`: `tau'`, the seconds left to the shared close, is `245`, `185`, `125`, `95`, `65`, `35` and `15`. A checkpoint
is complete when its four replies are `200`, non-empty, JSON, and received within one second (lines 296 to 314).

**The set.** Every window `T` from **`1790184600`**, 2026-09-23 17:30 UTC — the first TZ-18a's service fetched
documents for, its start falling at `T+590` — to **`1791241200`**, 2026-10-05 23:00 UTC, in steps of 900:
**1,175 windows considered**. A window is a **member** when:

1. its `window.json` reads `documents_ok` true, `checkpoints_complete` `7`, `missed` `0`, both slugs its own, and
   for each market `["Up", "Down"]` with two token ids and a condition id — and its `books.jsonl.gz` exists;
2. both settled documents are served closed and resolved, with `outcomes` `["Up", "Down"]`, `feeSchedule`
   `{exponent 1, rate 0.07, takerOnly true, rebateRate 0.2}` and `feeType` `crypto_fees_v2`, their own start
   instant, both readings, and the chain book's tokens and condition id;
3. E1, E2 and E3 hold.

`window.json` decides membership without opening a book: it carries counts, times and token ids, map §2.5's
exception. **The 90 windows `1791018000` … `1791098100` were never stored** (map §2.5), and `1791017100`, which the
chain book's stop of 2026-10-03 08:56:15 UTC cut at `T+675`, after its first checkpoint, cannot read `7`. If every
other window qualifies, the members are **1,084** — 791 on a weekday and 293 on a weekend, 925 before the gap and
159 after it — recorded, and asserted by nothing.

**Why it ends at `1791241200`.** Its five-minute market, `1791241800`, is M0's last member, and no TZ reads a
five-minute market with `T0 > 1791241800` before M0's second look (CANON PART II). The last fifteen-minute
document's `finalPrice` is the reading at `1791242100`, the close of `1791241800`, already in the documents TZ-23
fetched.

**The reserve.** Map §2.5 kept every body under the chain book's root for the TZ that scores it, B2; with §2.3's
reserve released (CANON §1.5), this TZ is that TZ.

**Data hygiene.** The Architect has opened nothing of the chain book, and no fifteen-minute document or price of the
span. Its audit of TZ-23 fetched the settled documents and taker fills of the five-minute markets M0 scored, among
them the five-minute legs of most of B2's windows: no fifteen-minute price and no book is among them, and no B2
figure can be formed from them. The rehearsal's span, TZ-17's 200 windows, ends `1,006,200` s below the set.

**The test.** `N` is the members; `N_clean` those whose seven checkpoints all read valid, both legs of every pair;
`V_firm` the members with a firm violation at some checkpoint; `V_any` those with a firm or a loose one.

- **VIOLATION** — `V_firm >= 1`. A firm row is an observation of the stored quotes, not an inference: under the
  containment, the fee and the touch, its false-reading probability is `0`. The self-test and the rehearsal guard
  the arithmetic, and the report prints every firm row for the Architect to re-derive.
- **NONE** — `V_any = 0` and `N_clean >= 528`. If the windows violate independently, each with probability at least
  `θ1 = 1 − 0.005^(1/N_clean)`, it reads with probability at most `(1 − θ1)^N_clean = 0.005`. It is also a census:
  no stored checkpoint of a clean member violates, in either class.
- **UNDECIDABLE** — neither.

**`528` is the fewest members at which `θ1 <= 0.01`**: NONE must reject violations in one window of a hundred. At
1,084 clean members `θ1` is `0.004876`. **Power**, before any book and deciding nothing: VIOLATION reads with
probability `1 − (1 − θ)^N` against windows violating independently at `θ` — at 1,084, `0.662` at `θ = 0.001`,
`0.9956` at `0.005` and `0.99998` at `0.01`; `constants` prints it at the measured `N`. Where violations cluster,
NONE's bound does not hold, and only its census does.

**What a reading establishes, and what it does not.** VIOLATION says the stored books offered both legs of a
dominated pair below 1 after both fees, at the venue's minimum size, inside one taker delay: **a violation measured
is not an edge captured** (CANON PART II) — depth, the 150 ms delay, both legs filled together, and `D` known live
are the next step's. NONE says the nesting held at every stored checkpoint of the clean members, and that
violations, if they occur at the chain book's seven instants, are rarer than `θ1` a window; between checkpoints it
says nothing. UNDECIDABLE closes nothing.

**What this TZ decides.**

1. **The instrument**, `research/tz24-nesting-b2.py`, on the branch `tz-24-nesting-b2`; `main` carries it once the
   Boss merges after the verdict.
2. **The set formed, its constants on disk with their SHA-256 in `state.json`, the instrument's commit on
   `origin`** — and only then the books, read once a run.
3. **The reading is B2's.** VIOLATION opens B3, whether a violation can be captured (CANON PART II). NONE closes B2,
   and the taker's nested pair joins CANON §1.6's closed list. UNDECIDABLE leaves B2 open for a later reading over
   windows after M0's second look.
4. **Nothing on the host is touched** but this TZ's tree, the forensic store by exclusive create, and the
   directories earlier sessions left (§9).

---

## 2. Scope

**Repository paths this TZ may write, and no others:**

1. `research/tz24-nesting-b2.py` — new, byte for byte Appendix A's, on branch `tz-24-nesting-b2`, then a pull
   request. Not merged by the Executor.
2. `CryptoReports/TZ-24-nesting-b2-report.md` — straight to `main`, in one commit. **The one path pushed to `main`,
   and the exemption to item 6 below.**

**Host paths this TZ may write:** `/root/tz24-work/**`; `/root/btc-forensics/`, by exclusive create only (§9); and in
the primary checkout `/root/btc-5m-twap`, its `.git` for the branch and the worktree, and its `CryptoReports/` for
the report.
**Host paths it removes, under §9 and nothing else:** `/root/tz24-work/` with its worktree, and the directories
`I scratch` names earlier.

**Prohibited, each absolutely:**

1. No committed file is modified; every `frozen` row of map §0 is byte-identical at run end.
2. **Nothing under `/var/lib/btc-recorder/` is opened or listed** — by the instrument, whose audit hook refuses any
   open there, or by any command of this TZ but §0.3's `df`, `find` and `grep -c`, at both of its runs, and
   B-RECLAIM-OWN's `df`.
3. **Under `/var/lib/btc-chainbook/` nothing is written or listed, and nothing opened but two files of a considered
   window, read only:** its `window.json`, by `fetch`; and its `books.jsonl.gz`, by `score` alone, after its
   preconditions (item 7). The instrument's audit hook refuses every other open there and every open for writing,
   and counts each it allows. `runtime.jsonl`, `service.pid`, `service.log` and every `documents.jsonl` are never
   opened. The one command outside the instrument that touches the root is §0.3's `test -d`, at both of its runs.
   The self-test's three deliberate opens under the two roots are refused by the hook before any open happens, which
   is what they test.
4. No unit is signalled, started, stopped, enabled, disabled or changed. `systemctl show` and `is-active` are this
   TZ's only reads of either.
5. `/root/tz04a-env/`, `/root/tz01-env/`, `/root/tz18a-svc/` and `/root/btc-recorder-svc/` are not modified, and
   `/root/btc-forensics/` only by §9's exclusive create.
6. Nothing is pushed to `main` except the report of item 2.
7. **No book is opened before §3.6's constants are on disk with their SHA-256 in `state.json` and the instrument's
   commit is on `origin`.** A book is a member's `books.jsonl.gz`. The self-test reads only the synthetic chain book
   it builds under `/root/tz24-work/`, and the rehearsal reads no chain book.
8. **Requests:** `gamma-api.polymarket.com/markets`, through the instrument's `http_json` and its two headers; `git`
   against `origin`; and `gh` for the pull request alone. No other request — no CLOB, no websocket, no
   authenticated call — and no read of a member's document or book by any command but the instrument's modes.
9. **Single books and markets:** the instrument prints sums over the set and, row by row, every firm and every
   loose checkpoint up to 40 a class, and the closest checkpoint a `tau'` and pair — asks, costs, times, the size at
   each ask, and the window's two strikes, which is what a re-derivation of the reading needs (map §7 item 70). It
   prints nothing else of a single book or market, and nothing of either leaves `/root/tz24-work/` but those prints
   and §9's byte-for-byte copies into `/root/btc-forensics/`.
10. No Release is created, and no dataset, archive or binary enters git history.

---

## 3. The work, in this order

From §3.1 on, `nice -n 19 /root/tz01-env/venv/bin/python -B /root/tz24-work/wt/research/tz24-nesting-b2.py` is
written **`I`**; a mode is `I <mode>`, run from `/root/tz24-work`. Every command's output goes to `logs/`, one file
per step, and is quoted in the report. **§9's B-RECLAIM-SCRATCH runs after §3.3 and before §3.4; B-RECLAIM-OWN runs
last, after §3.9.** On a BLOCK before §3.1, B-RECLAIM-OWN runs with `I0` in place of `I` and without its
`git worktree remove` line.

**Where the session's permission classifier refuses a command of a block named B-…**, the Executor prints the
block, the Boss runs it verbatim in a root shell on the VPS, and the Executor verifies it through the reads this TZ
names — never from the Boss's account.

### 3.1 The branch and its file

```
git -C /root/btc-5m-twap fetch origin
git -C /root/btc-5m-twap worktree add -b tz-24-nesting-b2 /root/tz24-work/wt origin/main
```

Then §0.1's script again, verbatim but for its argument, `/root/tz24-work/wt`; it must print the same lines, bytes
and SHA-256 as at §0.1. Commit that file alone on the branch, push it with
`git push -u origin tz-24-nesting-b2`, and open the pull request against `main`. A failed assert here is BLOCKED.
**The push is what lets §3.7 read a book:** `score` refuses a `HEAD` that `origin` does not carry.

### 3.2 The self-test

`I selftest` must print `122 of 122 checks passed`. A red self-test stops the run here, and it goes to §3.9 and §9.

### 3.3 The units, and the directories beside this session

`I still` records both units' `MainPID`, `NRestarts` and `ActiveState` in `state.json` and prints their
`MemoryCurrent` and `MemoryPeak`. Then `I scratch "$(dirname "$S")"` lists every UUID directory beside this
session's own and names each **live** — born from 1 s before to 60 s after the start of a running process whose
`argv[0]` is `claude` or ends in `/claude.exe` — or **earlier**.

### 3.4 The rehearsal — G-REHEARSAL

`I rehearse`: the document path — the request, the readings, the literals, E1 to E3, `D` and the outcomes — over
TZ-17's 200 windows, `1788998400` … `1789177500`, against the Architect's independent figures (§4.1). A FAIL stops the
run here, and it goes to §3.9 and §9.

### 3.5 The set — G-SET

`I fetch`: the 1,175 windows' `window.json`, and the two settled documents of every window whose `window.json`
qualifies, ten windows a request, until it prints `G-SET PASS` or fails. After its first 20 requests it projects its
own time and stops BLOCKED above `900` s. **A network failure is resumable:** the cache keeps every finished
request, and `I fetch` may be run again twice, 600 s apart; a third failure is BLOCKED.

### 3.6 The constants, twice

`I constants`, then `I constants` again. The second run must print `unchanged` for the constants file — contract
§6's determinism. Its SHA-256 is in `state.json`.

### 3.7 The score, twice

`I score`, then `I score` again. The first reads the books and prints the reading; the second must print
`unchanged` for the units and reading files. The ledger then holds two lines.

### 3.8 The units again — G-STILL

`I still`.

### 3.9 The closing reads

§0.3's block again, then:

```
systemctl show btc-recorder.service btc-chainbook.service -p MainPID -p NRestarts -p MemoryCurrent -p MemoryPeak
free -b
du -sb /root/tz24-work /root/.claude
cat /root/tz24-work/state.json /root/tz24-work/book-ledger.jsonl
```

---

## 4. The gates — fixed here, before any of their data exists

| gate | population | PASS, or the reading | false failure | power, against |
|---|---|---|---|---|
| **G-REHEARSAL** | TZ-17's 200 windows, `1788998400` … `1789177500` | §4.1's 10 figures equal, exactly | `0` — two independent computations of one public record | `1`, any difference in the request, a literal, an outcome, a sign or a sum |
| **G-SET** | the 1,175 windows `1790184600` … `1791241200` | every window a status; the members in order; `set.json`'s SHA-256 in `state.json` | `0` | — |
| **B2** | the members' books | §4.3 | VIOLATION `0`; NONE at most `0.005` against `θ1`, independent windows | VIOLATION `1 − (1 − θ)^N`, printed before any book |
| **G-STILL** | the two capture units, §3.3 to §3.8 | `MainPID`, `NRestarts` and `ActiveState` unchanged | `0` — systemd read directly | `1`, a restart or a stop |

### 4.1 G-REHEARSAL

Over TZ-17's 200 windows, the windows considered, the members, the counts of `D > 0`, `D < 0` and `D = 0`, the
fifteen-minute and five-minute Up outcomes, `Σ D`, `Σ |D|` and the digest must equal the Architect's figures. They
were computed from TZ-17's committed CSV — its columns `T`, `K15`, `K5c`, `K5d`, `O15` and `O5c` — and again from the
venue's documents fetched one a request by the per-slug route, by a script that shares no code with the
instrument, and the two agree:

| figure | value |
|---|---|
| windows considered | `200` |
| members | `200` |
| `D > 0` | `102` |
| `D < 0` | `98` |
| `D = 0` | `0` |
| fifteen-minute Up | `98` |
| five-minute Up | `102` |
| `Σ D` | `-2198.32154130825` |
| `Σ \|D\|` | `19953.70645914237` |
| digest | `a9b57a6ea03fa6d57d964afcf1aa17da463547a5bf216069430d25d99cf1b3ee` |

The digest is the SHA-256 of one line a window, in order, `T,R0,R600,R900,O15,O5`, each ending in a newline. They
are the instrument's `REF`. The Architect's run of this file printed the same ten, and `set.json` SHA-256
`4635cb07fce5f998da23cca5bc376160f704df2e1772e542ba8d52883dd6320a`, recorded and judged by nothing.

### 4.2 G-SET

`fetch` prints `G-SET PASS` once each of the 1,175 windows has a status, the members are exactly the windows whose
status is `member`, in order, and `set.json`'s SHA-256 is in `state.json`. `constants` prints every non-member with
its reason.

### 4.3 B2's reading

| condition | reading |
|---|---|
| `V_firm >= 1` | **VIOLATION** — whatever `N` |
| `V_any = 0` and `N_clean >= 528` | **NONE** |
| otherwise | **UNDECIDABLE** |

**No row reads a power.** The report prints `V_firm`, `V_any`, `N`, `N_clean`, `θ1` at `N_clean`, the rows by class,
by `tau'` and by pair, the invalid checkpoints by reason, and every firm and loose row the instrument prints; and,
barred from every reading, the closest row at each `tau'` and pair, the rows whose asks sum below 1 before any fee,
the firm rows' margins, receive gaps, book-time gaps, ages and sizes at the ask, their profit at the touch, and the
members by `|D|`.

### 4.4 G-STILL

From §3.3 to §3.8 both units keep their `MainPID`, `NRestarts` and `ActiveState`. **This TZ signals nothing**, so a
FAIL runs no block: the report carries it, with both units' memory at both reads, for TZ-22.

---

## 5. The instrument

`research/tz24-nesting-b2.py`, Appendix A, fixed by the Architect as this TZ's Validation and written byte for byte.
The standard library and one committed file: `research/tz14-quote-inventory.py`, loaded once by `tz14()` for
`book_of`, `touch_of` and `fee_pp`, none of which it writes again. Loading it writes three thread-count variables,
loads `tz12` and every module below it, and installs `tz14`'s own audit hook (that file's lines 37 to 39, 71 and
213); the instrument prints that hook's count and the self-test asserts it `0`. Run under `/root/tz01-env`, whose
numpy that load needs. One mode a run; each prints its findings with UTC stamps, its peak memory, whether glibc
took its two settings, the opens refused under either capture root, and the chain book opens it allowed, by file.
Every number of the venue is the `Decimal` of its own text, and every sum is exact at 60 digits in the main thread,
which the self-test asserts (map §7 item 99). **After its first book is opened nothing the books can hold raises:**
an unreadable file, line, reply or level is an invalid checkpoint with its reason (map §7 item 83's rule). It writes
under `/root/tz24-work/` and, in `reclaim`, new files in `/root/btc-forensics/` by exclusive create. Exit `0` is every
assert held; exit `1` a failed assert, named, or a BLOCK whose message says so. Run with `-O` it refuses to start.

---

## 6. Cost

Measured in the Architect's runs under Python 3.12.3 on one core of an Intel Xeon at 2.10 GHz — the host has one
processor (map §6) — and taken at the population's upper bound: every considered window a member, 1,175, each with
7 checkpoints of four replies, `32,900` replies of `13,189` bytes each, `8,225` checkpoints.

| check | population | measured | bound |
|---|---|---|---|
| `fetch` | 1,175 `window.json`; at most 118 requests of 20 slugs | 20 requests in `6.5` s from the Architect's session on 2026-10-10; the host served TZ-23's 202 in `23.0` s | `600` s; **projected after its first 20 requests, BLOCKED above `900` s** |
| `score`, each run | 1,175 members, 32,900 replies | `23.3` to `26.4` s over four runs | `300` s on a host three times slower with books twice as large |
| `rehearse` | 200 windows, 20 requests | `6.5` and `6.8` s | `120` s |
| `constants` | the set file | under 1 s | `30` s a run |
| `selftest`, `fingerprint`, `still`, `scratch`, each `reclaim` | — | under 1 s each | `30` s a run |

**Wall clock at those bounds at most about `1,650` s, of which the processor's at most about `700`; every second at
`nice 19`.** The fetch's fail-fast bound, `900` s, is 118 requests at `7.63` s each, 23.5 times the `0.325` s a
request the rehearsal measured.

---

## 7. Validation

| # | check | count |
|---|---|---|
| **V1** | §0.2's fingerprint | `FINGERPRINT PASS`: revision `2026-10-10-a`; anchors 6 of 6, 4 re-derived; 33 rows, 30 of 30 `frozen` equal |
| **V2** | §0.3's host gate | H1 to H4, the memory and the disk gate; the rest printed |
| **V3** | §0.1's and §3.1's file | 1 of 1 hash asserted at each, lines and bytes; the branch's diff against `origin/main` names exactly one path, `A`, 1,535 lines |
| **V4** | the self-test | `122 of 122` |
| **V5** | G-REHEARSAL | 10 of 10 figures equal |
| **V6** | G-SET | 1,175 considered; every non-member with its reason; the members by span, weekend and pair |
| **V7** | the constants, twice | 1 of 1 file `unchanged` at the second run |
| **V8** | the score, twice | the reading; 2 of 2 files `unchanged`; 2 ledger lines |
| **V9** | G-STILL | both units unchanged, or the change named |
| **V10** | opens under the capture roots | refused `0` at every mode; `fetch`'s `window.json` opens equal to the considered windows whose status is none of `no directory`, `no window.json` and `no books`, and its `books.jsonl.gz` opens `0`; each `score`'s `books.jsonl.gz` opens equal to `N`, and its `window.json` opens `0`; every other mode `0` and `0` |
| **V11** | memory | every mode's printed peak, against §0.4's floor; `malloc tuned: True` at every mode |
| **V12** | contract §4.2's self-check | run after the push and the pull request and before the report's commit |
| **V13** | §3.9's closing reads | every read printed |
| **V14** | §9's `reclaim` runs | files considered, named by a report, kept by name, copied and already held; the store's count after equal to before plus the copies |
| **V15** | §9's removals | `git worktree remove` without `--force` exit `0`; `test -e` exit `1` for `/root/tz24-work` and each directory removed; `git worktree list` naming `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else |

---

## 8. The report

`CryptoReports/TZ-24-nesting-b2-report.md`, in contract §8's order. Beyond what V1 to V15 print: the set — windows
considered, members, the first and last member, the members by span, weekend and pair, **every non-member with its
reason**, the member list's SHA-256 and the set file's; `N`, `N_clean`, `θ1` at both, and the powers; **the
reading**, with `V_firm` and `V_any`; the rows by class, `tau'` and pair, and the invalid checkpoints by reason;
**every firm and loose row the instrument printed**, verbatim; the barred figures; both ledger lines; both units at
both reads, memory included; every block the classifier refused, who ran it and when; §9's counts and removals; every
free-space and `MemAvailable` read with its instant and bound; and every file the run wrote, by SHA-256, but the two
document caches — the set's at most 118 files and the rehearsal's 20 — which §9 keeps by name, and whose file counts
and bytes the report prints instead. **The report is drafted in the primary checkout `/root/btc-5m-twap` before
B-RECLAIM-OWN and committed after it**, so the removal of this TZ's tree is in it.

---

## 9. Reclaim — the host left clean (CANON hard rule 15)

**What a file is kept for:** a committed report prints its SHA-256, whole or as a prefix of 16 to 64 hex
characters, or it is kept by name: `state.json`, `book-ledger.jsonl`, every file under `logs/`, and every file under
`set/docs/` and `rehearsal/docs/` — the venue's settled documents as they were served, which the venue no longer
serves byte for byte (map §7 item 100). `reclaim` copies each into `/root/btc-forensics/` as
`<tree>--<path with / as -->`, by exclusive create, and verifies its hash; a name already there with the same hash is
counted as held, and with another hash is a failed assert. The branch worktree is not copied: `reclaim` asserts that
`git status --porcelain --ignored` in it prints nothing and that its `HEAD` is its upstream's, so `git worktree
remove` needs no `--force`.

**B-RECLAIM-SCRATCH**, after §3.3 and before §3.4, for every directory `I scratch` named **earlier** — none it named
live, and never this session's own:

```
I reclaim <each earlier directory, by its full path>
rm -rf <one such directory>; echo "exit=$?"
test -e <that directory>; echo "exit=$?"
```

`reclaim` refuses a directory born from 1 s before to 60 s after a running claude process started, and any path but
`/root/tz24-work` that is not a UUID directory under `/tmp/` whose parent's name carries `btc-5m-twap`; it prints
`RECLAIM PASS` before any removal. If `I scratch` names none earlier, the block is recorded as empty and skipped.

**B-RECLAIM-OWN**, last, after §3.9 and with the report drafted. **Its output is written to no file**, and the
Executor quotes it from the session:

```
I reclaim /root/tz24-work
git -C /root/btc-5m-twap worktree remove /root/tz24-work/wt; echo "exit=$?"
rm -rf /root/tz24-work; echo "exit=$?"
test -e /root/tz24-work; echo "exit=$?"
git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
find /root/btc-forensics -type f | wc -l
df -B1 --output=source,size,avail /var/lib/btc-recorder
```

The branch `tz-24-nesting-b2` stays on `origin` and as a local ref; only its working tree goes.
`/root/btc-recorder-svc` and `/root/tz18a-svc` are the two units' code, and the captures and the forensic store are
data, never scratch. **A refused `rm -rf` is handed to the Boss** by §3's route, one tree per command, and verified
by `test -e`.

---

## 10. Pre-send checks

Performed by the Architect on 2026-10-10 against this file as sent, in a reading separate from its writing, with
the repository at `origin/main` `d4857c3a95097d7b500a0b86c09b6283599663bc` and map revision `2026-10-10-a` as it
ships with this TZ.

| # | check | result |
|---|---|---|
| **C1** | scope against body | **Repository paths the body names, 8:** `CryptoTZ/TZ-24-nesting-b2.md`, read by §0.1's script; `SYSTEM-MAP.md` and the 33 files of its §0 table, read by `I0 fingerprint`; `research/tz14-quote-inventory.py`, loaded, with `tz12` and the modules below it; `research/tz18a-chainbook-capture.py`, cited for the chain book's format and floor and hashed by the fingerprint, never imported; `CryptoReports/TZ-17-settlement-chain-report.md`, the source of `REF`, never opened by the instrument; every `CryptoReports/*.md`, read by `reclaim` for hashes; `research/tz24-nesting-b2.py`, written on the branch; `CryptoReports/TZ-24-nesting-b2-report.md`, written to `main`. **Entry points:** Appendix A's nine modes — `fingerprint`, `selftest`, `still`, `scratch`, `rehearse`, `fetch`, `constants`, `score`, `reclaim` — §0.1's script, `git`, `gh`, and §0.3's and §3.9's shell reads. **Outputs:** `logs/`, `state.json`, `book-ledger.jsonl`, `stage/research/tz24-nesting-b2.py`, `rehearsal/set.json` and `rehearsal/docs/`, `set/set.json`, `set/docs/`, `set/tz24-constants.json`, `set/tz24-units.csv`, `set/tz24-reading.json`, the self-test's transient tree, the forensic store's copies, the report, the branch and the pull request. **Intersections with §2, by path and by content class, 6, each named in §2:** the report on `main` — item 6's exemption, item 2 of the paths; `fetch`'s `window.json` and `score`'s `books.jsonl.gz` under the chain book — item 3 names both, and item 7 orders the second; §0.3's `test -d`, `df`, `find` and `grep -c` and B-RECLAIM-OWN's `df` under the capture roots, and the self-test's three refused opens there — items 2 and 3 name them; single books' prices in the units file, the reading file and the printed rows — item 9's exemption; §9's copies of these into `/root/btc-forensics/` — items 5 and 9; the pull request — item 8 names `gh`. **One class checked and intersecting nothing:** the settled documents and outcomes in `set/docs/` and `set.json` — no prohibition of this TZ names labels, outcomes or settled documents; its held-back class is the book. Host writes in the primary checkout — §2's host paths. |
| **C2** | origin of every expectation | **§5 holds no numeric expectation; its line numbers are citations. §7's, by kind:** quoted from a committed artifact — V1's revision, 6, 4, 33 and 30, and V15's two worktrees, from map revision `2026-10-10-a` §0 and §3, which ships in this upload; V2's `/dev/vda2` and `31612203008` from map §6; `2,400,000,000` from `research/tz18a-chainbook-capture.py` line 79 plus `200,000,000`, derived in §0.4; V4's `122` and V5's 10 from Appendix A, fixed by its code and by nothing this TZ measures; V6's `1,175` = `(1791241200 − 1790184600) / 900 + 1`. `141,189,120` is twice the Architect's measured `70,594,560`, made before this TZ was sent — not a quantity the run measures. Computed by an implementation independent of the one under test — V3's SHA-256, lines and bytes, by `sha256sum` and `wc` over Appendix A, exact; V5's ten figures, `REF`, by the Architect's reference script, which shares no code with the instrument, from TZ-17's committed CSV and again from the venue's per-slug documents, exact `Decimal`, the two agreeing; **the self-test's literals** — `0.996013`, `1157525/1161919` = `0.99621832502954164619…`, `0.99995625`, `1.00127013455235589192…`, `0.993409`, `0.99948825`, `0.99950403631641686324…`, `1.035`, `θ1(528)` = `0.00998451244616880761…`, `1 − 0.99^1000` = `0.99995682875258934174…` — by exact rational arithmetic and an 80-digit `Decimal` computation outside the instrument, against tolerances of `1e-50` or exact equality, 29 decades and more; `fee_pp`'s three points from CANON §1.1's formula, exact. V7's 1, V8's 2 and 2, V10's counts and 0s are counts of §3's own runs and files. **No expectation depends on a quantity this TZ measures:** `θ1` and the reading are functions of `N_clean`, `V_firm` and `V_any`, and judge nothing but them; the self-test's synthetic counts are fixed by the book it builds. |
| **C3** | shape of every diff | One path: `research/tz24-nesting-b2.py`, new. `git cat-file -e d4857c3:research/tz24-nesting-b2.py` exits `128`: the path does not exist on `origin/main`, so the change replaces **none** of its lines. The words "insertions only" appear nowhere in this TZ. |
| **C4** | cost of every check | §6, at the population's upper bound: every considered window a member, 1,175, `32,900` replies, `8,225` checkpoints. `fetch` `600` s — 1,175 `window.json` and at most 118 requests; `score` `300` s a run, measured at `23.3` to `26.4` s; `rehearse` `120` s; `constants`, `selftest`, `fingerprint`, `still`, `scratch` and each `reclaim` `30` s a run. Wall clock at most about `1,650` s; **single-session processor at most about `700` s, under `3,600`, so nothing is sampled**. The one fail-fast bound, `900` s, is 118 requests at `7.63` s each, `23.5` times the rehearsal's measured `0.325` s a request, derived in §6. |
| **C5** | every count | Over the grid `T = 1790184600 + 900k`: `1,175` considered = `(1791241200 − 1790184600) / 900 + 1`; `926` from `1790184600` to `1791017100`, `90` from `1791018000` to `1791098100`, `159` from `1791099000` to `1791241200`, summing to `1,175`; at most `1,084` members = `1,175 − 90 − 1`, the one being `1791017100`, `925` and `159` by span; `791` weekday and `293` weekend by a walk of the same grid; `384` weekend windows considered, `90` of them in the gap. Requests: at most `118` = ⌈1,175 / 10⌉ for the set, `20` = 200 / 10 for the rehearsal. `28` lines a window = 7 offsets (`research/tz18a-chainbook-capture.py` line 86) × 4 reads; `32,900` = 1,175 × 28; `8,225` = 1,175 × 7. `528` = the least `n` with `θ1(n) <= 0.01`: `θ1(527)` = `0.0100034` and `θ1(528)` = `0.0099845`. V1's `33` = 30 + 2 + 1, read from the map's table; its `4` re-derived anchors `A2`, `A4`, `A5`, `A6`. V7's `1`: the constants file; V8's `2`: the units and reading files, and `2` ledger lines, one a `score` run. §0.3's six BLOCKING conditions: H1 to H4, memory, disk. `1,006,200` = `1790184600 − (1789177500 + 900)`. V4's `122`: the count Appendix A's self-test prints, re-run by the Architect. |
| **C6** | every population | `V_firm`, `V_any`, `N`, the weekend, span and pair counts: the members. `N_clean`: the members whose every row is valid. `θ1`: at `N_clean` in `score`, at `N` in `constants`. The powers: `N`. The rows by class, `tau'` and pair: the members' valid rows. The invalid checkpoints by reason: the members' invalid rows. The printed firm and loose rows: those classes, first 40 each in member order. The closest rows: the valid rows with both asks, per `tau'` and pair. The pre-fee inversions: the valid rows with both asks. The firm figures and the profit: the firm rows, the profit's best row a window. The loose margins: the loose rows. The members by `\|D\|`: the members. G-REHEARSAL's ten: TZ-17's 200 windows. G-SET and the non-members: the 1,175 considered windows. Each memory peak: one mode's process. `MemAvailable` and free space: the host at each read. G-STILL: the two capture units. |
| **C7** | every signature and every behaviour | **Committed functions called, read at `d4857c3` in `research/tz14-quote-inventory.py`:** `def book_of(raw):` (line 531) — line 538 `body = json.loads(raw)`, which raises on a body that does not parse, and Appendix A catches it (line 707); line 549 `levels.append((D(str(lv["price"])), D(str(lv["size"]))))`, and line 551 `out["bad_levels"] += 1` for a level that does not parse; lines 555 and 556 set `out[field]` and `out[field + "_present"]` for `BODY_FIELDS` (line 160: `tick_size`, `min_order_size`, `timestamp`, `hash`, `market`, `asset_id`) — the fields Appendix A reads. `def touch_of(book, min_size, tick):` (line 583) — line 591 `ask5 = min((p for p, s in book["asks"] if s >= min_size), default=None)`, the lowest ask with at least the minimum size; lines 602 and 603, `cum["ask"][k]` the size priced from `ask5` to `ask5 + k * tick`, so `k = 0` (`KS`, line 115) is the size at the ask; line 605 returns `{"bid5": bid5, "ask5": ask5, "band": band, "cum": cum}`. `def fee_pp(p):` (line 610) — line 616 `return FEE_RATE * p * (D(1) - p)`, `FEE_RATE = D("0.07")` at line 123. The load's side effects: lines 37 to 39, the thread variables; line 71, `tz12`; line 177, `CAPTURE_OPENS = []`, appended at line 210 by the hook installed at line 213. **`research/tz18a-chainbook-capture.py`, never called, read for the format:** `BOOK_KEYS` (line 675) and line 751 `lines.append(json_line({k: e.get(k) for k in BOOK_KEYS}))`; `json_line` (lines 235 and 236, `ensure_ascii=False`); `http_get`'s `raw` from `body.decode("utf-8")` (line 454, `latin-1` at 456), `"bytes": len(body)` and `"sha256": sha256_hex(body)` (lines 463 and 464); `labels = outs[:2]` (line 498) and `"outcome_label": … labels[i]` (line 641); `WINDOW_JSON_KEYS` and `WINDOW_MARKET_KEYS` (lines 123 and 127), written at line 781; completeness at lines 296 to 314; `SKEW_BOUND_NS` line 90; `CHECKPOINT_OFFSETS` line 86; `RESOURCE_FLOOR` line 79; the four threads released together at lines 652 to 663; and the stop path — `if not sleep_until(instant): break` (lines 741 and 742), `if lines:` (757), `sleep_until(sched["close_instant"])` unchecked (761), `window.json` written (781) — which leaves `1791017100` a `window.json` reading at most one complete checkpoint. **Every behaviour this TZ attributes to Appendix A, by the extracted file's line numbers:** `-O` refused, lines 49 to 51; precision 60, line 53, asserted at lines 1260 and 1264; `tz14` loaded once, lines 123 to 135, its hook's count asserted `0` at line 1506; the audit hook, lines 160 to 200 — books refused before `score`'s preconditions at line 174, both roots' refusals at lines 190 and 196; the four floor checks at lines 960, 990, 1014 and 1026, each asserting at lines 297 and 300; the fetch's projection after 20 requests, lines 581 to 584; G-SET at lines 994 to 996 and 1003, `set.json`'s hash into `state.json` at line 998; `constants` refusing another set at line 1017 and recording its hash at line 1020; determinism's `unchanged`, line 253; `score`'s preconditions at lines 1030, 1033 and 1036, and `BOOKS_OPEN` set at line 1040, after them; `score` tied to its constants before the first book at line 806; the clean count at line 822; the reading table, lines 532 to 539; `θ1`, lines 542 to 545; the costs, lines 502 to 506; the classes, lines 509 to 529, firm at 521 and 522; totality after the first book — `read_books` at lines 662 to 670, `line_check` at 696 and 707, `rows_of` at 766, 775 and 779; the printed rows, 40 a class, lines 891 and 892; the rehearsal's ten figures, line 82 on, judged at lines 980 and 981; the fingerprint's asserts, lines 935 to 954; `still`, lines 1057 and 1062; `scratch`'s live rule, line 1104, and `reclaim`'s, line 1149, its paths at line 1138, its kept names at line 1117, its pristine worktree at lines 1126 and 1130, its store count at line 1188; every mode's last three prints, lines 1525 to 1531. Two sentences were rewritten before sending: §3.1 had the second extraction print "the same line", and its path differs; §0.1 had the staged copy run "§0's gates", and it runs the fingerprint alone. |
| **C8** | every cross-reference | Resolved by reading the text referenced. **Map `2026-10-10-a`:** §0's anchors and 33 rows, 30 / 2 / 1; §1's `d4857c3`, `tz-23-maker-m0` at `7f5ae3f` and 28 ref lines; §2.3's released reserve; §2.5's chain book — its start at 17:39:50 UTC on 2026-09-23, `T+590` of `1790184600`, its stop at 2026-10-03 08:56:15 UTC, the 90 lost windows `1791018000` … `1791098100`, `28,467` bytes a window, TZ-18a's `1.19` to `28.43` ms, and the reserve kept for B2; §3's store at `1,561` and the two worktrees; §6's host identity, the recorder's tree at `e3975b5`, `/root/tz01-env` with numpy, `1,002,127,360` bytes and one processor, TZ-23's `255,062,016` to `327,110,656`, and the headroom's condition; §7 items 70, 83, 97, 98, 99 and 100. **Contract:** §1 steps 1 to 4, §4.2's self-check, §6's determinism, §8's order. **CANON `2026-10-10-a`:** §1.1's fee, taker delay and strike reconstruction; §1.5's released reserve; §1.6; PART II's backup track, B2 and B3, "a violation measured is not an edge captured", and M0's second-look rule on `T0 > 1791241800`; PART III's published-quantity rule; hard rule 15. **This TZ:** §0.1 to §0.5, §1, §2 items 1 to 10, §3.1 to §3.9, §4.1 to §4.4, §5, §6, §9 and Appendix A, each supporting the sentence that cites it. **None unresolved.** |

**No check was unperformable in this session**, so none is converted into a BLOCK condition under CANON hard rule 13.
The host's state is read by §0's gates on the host itself. **One venue fact was not re-read here:** how the venue
collects the taker fee; the classes are defined so that a firm violation holds under either collection (§1).

---

## Appendix A — `research/tz24-nesting-b2.py`, byte for byte

Extracted by §0.1's script; the block's content is the file.

```python file=research/tz24-nesting-b2.py
#!/usr/bin/env python3
"""TZ-24 - the backup track's B2: does the nesting of btc-updown-5m-{T+600} inside btc-updown-15m-{T}
break on executable quotes, after both legs' taker fees?

    fingerprint       map section 0 against the primary checkout: the revision, the six anchors, four of
                      them re-derived, and every row of the table, each frozen row asserted equal
    selftest          every rule of this file, on literals and on a synthetic chain book
    still             both capture units: the first run records MainPID, NRestarts and ActiveState, the
                      second compares (G-STILL)
    scratch OWN       the UUID directories beside OWN, this session's directory: live or earlier
    rehearse          the document path over TZ-17's 200 windows, against the Architect's figures
                      (G-REHEARSAL)
    fetch             the set: every window T = 1790184600 ... 1791241200, its window.json and its two
                      settled documents (G-SET)
    constants         book-free: the members, N, NONE's alternative and the powers, on disk
    score             the members' books, read once a run, and the reading
    reclaim TREE...   section 9

It requests gamma-api.polymarket.com/markets and nothing else, every request with the two headers HEADERS
fixes. Under /var/lib/btc-recorder it opens nothing. Under /var/lib/btc-chainbook it opens, read only, a
considered window's window.json and - in `score` alone, after its two preconditions - its books.jsonl.gz:
an audit hook refuses every other open under either root. It writes under /root/tz24-work/ and, in
`reclaim`, new files in /root/btc-forensics/ by exclusive create. Exit 0: every assert of the mode held.
Exit 1: an assert failed, and its message names it. Run it with the research interpreter, /root/tz01-env,
which research/tz14-quote-inventory.py needs.

Written for CryptoTZ/TZ-24-nesting-b2.md. The TZ is the specification.
"""

import datetime
import gzip
import hashlib
import importlib.util
import io
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
import zlib
from decimal import Decimal as D, getcontext

if not __debug__:
    sys.stderr.write("tz24: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(2)

getcontext().prec = 60

# ---- the TZ's constants ------------------------------------------------------------------------

FIRST_T = 1790184600         # 2026-09-23 17:30 UTC: the first window TZ-18a's service fetched documents for
LAST_T = 1791241200          # 2026-10-05 23:00 UTC: its five-minute market, 1791241800, is M0's last member
WINDOW = 900
CONSIDERED = (LAST_T - FIRST_T) // WINDOW + 1
OFFSETS = (655, 715, 775, 805, 835, 865, 885)   # the chain book's seven checkpoints after T
TAUS = tuple(WINDOW - o for o in OFFSETS)       # seconds left to T + 900: 245, 185, 125, 95, 65, 35, 15
SECOND_SPAN = 1791099000     # the first window after the chain book's restart under its unit
CHUNK = 20                   # slugs a gamma request: ten windows
ALPHA = D("0.005")           # NONE's false-reading probability
N_MIN = 528                  # the fewest members at which NONE's alternative is at most 1 window in 100
THETAS = (D("0.001"), D("0.005"), D("0.01"))
SKEW_BOUND_NS = 150000000    # the two legs received at most 150 ms apart: CANON section 1.1's taker delay
TS_BOUND_MS = 150            # and the two books' own timestamps at most 150 ms apart
ROWS_SHOWN = 40              # firm and loose units printed in full, each class, in member order
FEE_TYPE = "crypto_fees_v2"
FEE_SCHEDULE = {"exponent": 1, "rate": D("0.07"), "takerOnly": True, "rebateRate": D("0.2")}
MEM_FLOOR = 141189120        # MemAvailable below which a mode that reads the venue or the capture stops
FETCH_BUDGET_S = 900         # a fetch projected past this after its first 20 requests is BLOCKED
UA = "btc-5m-twap-b2/TZ-24"
HEADERS = {"User-Agent": UA, "Accept": "application/json"}
GAMMA = "https://gamma-api.polymarket.com/markets"
REHEARSAL = (1788998400, 200)    # TZ-17's 200 windows, 1788998400 ... 1789177500

# The Architect's independent figures for the rehearsal: TZ-17's committed CSV, and the venue's documents
# re-fetched one a request by a script that shares no code with this file (TZ-24 section 4.1).
REF = {
    "windows": 200, "members": 200, "d_pos": 102, "d_neg": 98, "d_zero": 0, "up15": 98, "up5": 102,
    "sum_d": D("-2198.32154130825"), "sum_abs_d": D("19953.70645914237"),
    "digest": "a9b57a6ea03fa6d57d964afcf1aa17da463547a5bf216069430d25d99cf1b3ee",
}

MAP_REVISION = "2026-10-10-a"
ANCHORS = {"A1": "229a944f2d51", "A2": "6c5089330629",
           "A3": "0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable",
           "A4": "437b45ea196b", "A5": "0f6c90451cbd", "A6": "729f0bcdbee3"}
ANCHOR_FILES = {"A2": "research/twap-divergence.py", "A4": "BTC-EXECUTOR-INSTRUCTIONS.md",
                "A5": "research/recorder/recorder.py", "A6": "research/pfair.py"}
MAP_ROWS = {"frozen": 30, "tracked": 2, "reported": 1}

UNITS = {"recorder": "btc-recorder.service", "chainbook": "btc-chainbook.service"}
WORK = "/root/tz24-work"
WT = WORK + "/wt"
STATE = WORK + "/state.json"
LEDGER = WORK + "/book-ledger.jsonl"
BRANCH = "tz-24-nesting-b2"
PRIMARY = "/root/btc-5m-twap"
REPORTS = PRIMARY + "/CryptoReports"
FORENSICS = "/root/btc-forensics"
CHAINBOOK = "/var/lib/btc-chainbook"
RECORDER = "/var/lib/btc-recorder"
UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
TOKEN = re.compile(r"[0-9a-f]{16,64}")
CONDITION = re.compile(r"0x[0-9a-f]{64}")
LIVE_S = 60                  # a directory born this soon after a claude process started is that process's

# The chain book's book line, research/tz18a-chainbook-capture.py BOOK_KEYS, and the two legs of each pair.
BOOK_KEYS = frozenset(("T", "tau_prime", "market", "slug", "token_id", "outcome_label", "url", "status",
                       "send_mono_ns", "recv_mono_ns", "recv_wall_ns", "bytes", "sha256", "raw",
                       "reason"))
LEGS = {"A": (("m15", "Up"), ("m5", "Down")),     # D > 0: Up of the 5m implies Up of the 15m
        "B": (("m5", "Up"), ("m15", "Down"))}     # D < 0: Up of the 15m implies Up of the 5m

HERE = os.path.dirname(os.path.abspath(__file__))
_TZ14 = []


def tz14():
    """research/tz14-quote-inventory.py, loaded once, on first use: the only implementation of the taker fee,
    `fee_pp`, and of the executable touch, `touch_of`, with `book_of`, which parses a reply for it. Loading it
    writes three thread-count variables, loads tz12 and everything below it, and installs an audit hook that
    records opens under /var/lib/btc-recorder; this file reads that record only to print its length."""
    if not _TZ14:
        if HERE not in sys.path:
            sys.path.insert(0, HERE)
        spec = importlib.util.spec_from_file_location(
            "tz14quoteinventory", os.path.join(HERE, "tz14-quote-inventory.py"))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        _TZ14.append(mod)
    return _TZ14[0]


def _malloc_tune():
    """glibc's mmap threshold fixed at 128 KiB and two arenas, as TZ-23 fixed them. True where both took."""
    try:
        import ctypes
        libc = ctypes.CDLL("libc.so.6")
        return libc.mallopt(-3, 131072) == 1 and libc.mallopt(-8, 2) == 1
    except (OSError, AttributeError):
        return False


MALLOC_TUNED = _malloc_tune()

# ---- the audit hook ------------------------------------------------------------------------------

REFUSED = []
CB_OPENS = {"window.json": 0, "books.jsonl.gz": 0}
BOOKS_OPEN = [False]         # set by `score` alone, after its two preconditions
CB_PATH = re.compile(r"/var/lib/btc-chainbook/([0-9]{10})/(window\.json|books\.jsonl\.gz)")
WRITE_FLAGS = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC


def cb_decision(path, mode, flags, books_open):
    """TZ-24 section 2, item 3, as a pure function of one open under the chain book: 'allow' or the
    reason it is refused."""
    m = CB_PATH.fullmatch(path)
    if m is None:
        return "not a window's window.json or books.jsonl.gz"
    if isinstance(mode, str):
        if set(mode) & set("wax+"):
            return "not read-only"
    elif not (isinstance(flags, int) and flags & WRITE_FLAGS == 0):
        return "not read-only"
    t = int(m.group(1))
    if not (FIRST_T <= t <= LAST_T and (t - FIRST_T) % WINDOW == 0):
        return "not a considered window"
    if m.group(2) == "books.jsonl.gz" and not books_open:
        return "a book before score's preconditions"
    return "allow"


def _audit(event, args):
    if event != "open" or not args:
        return
    p = args[0]
    if isinstance(p, bytes):
        p = os.fsdecode(p)
    if not isinstance(p, str):
        return
    path = os.path.abspath(p)
    if path == RECORDER or path.startswith(RECORDER + "/"):
        REFUSED.append(path)
        raise RuntimeError("open refused under the recorder's root: %s" % path)
    if path == CHAINBOOK or path.startswith(CHAINBOOK + "/"):
        why = cb_decision(path, args[1] if len(args) > 1 else None,
                          args[2] if len(args) > 2 else None, BOOKS_OPEN[0])
        if why != "allow":
            REFUSED.append(path)
            raise RuntimeError("open refused under the chain book's root, %s: %s" % (why, path))
        CB_OPENS[os.path.basename(path)] += 1


sys.addaudithook(_audit)

# ---- small helpers -------------------------------------------------------------------------------


def out(msg):
    sys.stdout.write("[%s] %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    sys.stdout.flush()


def utc(t):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(t))


def iso(t):
    return datetime.datetime.fromtimestamp(t, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def fx(x):
    """A Decimal as fixed-point text, never in exponent form."""
    return format(x, "f")


def lit(x):
    """A venue number as the text of its literal: a Decimal of its own text, or an int."""
    assert isinstance(x, (D, int)) and not isinstance(x, bool), type(x)
    return str(x)


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
    """The first run writes; a later run must produce the same bytes (determinism, contract section 6)."""
    if os.path.exists(path):
        got = sha256_file(path)
        assert got == sha256_bytes(data), "determinism: %s differs from the first run" % path
        out("unchanged %s sha256 %s" % (path, got))
        return got
    write_atomic(path, data)
    return sha256_bytes(data)


def gz_bytes(data):
    """Deterministic gzip: no name, no time."""
    buf = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=buf, mtime=0) as g:
        g.write(data)
    return buf.getvalue()


def _dec(o):
    if isinstance(o, D):
        return fx(o)
    raise TypeError(type(o))


def dumps(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), default=_dec) + "\n"


def loads_maybe(v):
    """A field the venue sends as JSON text inside JSON, parsed; anything else as it is."""
    if isinstance(v, str):
        try:
            return json.loads(v)
        except ValueError:
            return None
    return v


def mem_available():
    with open("/proc/meminfo", encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("MemAvailable:"):
                return int(line.split()[1]) * 1024
    raise AssertionError("no MemAvailable")


def floor_check():
    """Before a mode that reads the venue or the capture: glibc's two settings, and the memory floor."""
    assert MALLOC_TUNED, "BLOCKED: glibc did not take the mmap threshold and the arena count"
    avail = mem_available()
    out("MemAvailable %d bytes, floor %d" % (avail, MEM_FLOOR))
    assert avail >= MEM_FLOOR, "BLOCKED: MemAvailable %d bytes, below %d" % (avail, MEM_FLOOR)


def load_state():
    if not os.path.exists(STATE):
        return {}
    with open(STATE, encoding="utf-8") as fh:
        return json.load(fh)


def save_state(state):
    write_atomic(STATE, (json.dumps(state, sort_keys=True, indent=1) + "\n").encode("utf-8"))


def slug15(t):
    return "btc-updown-15m-%d" % t


def slug5(t):
    return "btc-updown-5m-%d" % t


def quantiles(values):
    """min, the nearest-rank median and max of a list, or None where it is empty."""
    if not values:
        return None
    v = sorted(values)
    return {"n": len(v), "min": v[0], "median": v[(len(v) - 1) // 2], "max": v[-1]}

# ---- the venue -----------------------------------------------------------------------------------


def http_json(url, tries=8):
    """One GET with HEADERS: the body's bytes and its JSON, every number a Decimal of its own text. 429,
    5xx and transport errors are retried, honouring Retry-After up to 60 s; anything else is fatal."""
    last = None
    for k in range(tries):
        req = urllib.request.Request(url, headers=HEADERS, method="GET")
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                body = r.read()
                assert r.status == 200, "HTTP %d %s" % (r.status, url)
                return body, json.loads(body, parse_float=D)
        except urllib.error.HTTPError as e:
            last = "HTTP %d" % e.code
            if e.code not in (429, 500, 502, 503, 504):
                raise AssertionError("%s on %s: %r" % (last, url, e.read()[:200]))
            wait = e.headers.get("Retry-After")
            time.sleep(min(60.0, float(wait)) if wait else min(60.0, 2.0 ** k))
        except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as e:
            last = "%s %s" % (type(e).__name__, e)
            time.sleep(min(60.0, 2.0 ** k))
    raise AssertionError("BLOCKED: %d attempts failed on %s, the last %s" % (tries, url, last))


def by_slug(docs, slugs):
    assert isinstance(docs, list), "gamma: not a list"
    by = {}
    for d in docs:
        s = d.get("slug")
        assert s in slugs, "gamma: %r was not requested" % s
        assert s not in by, "gamma: %s twice" % s
        by[s] = d
    return by


def gamma_cached(docs_dir, slugs):
    """The settled documents of up to CHUNK slugs, one request, its body stored once, gzip, verbatim."""
    assert 1 <= len(slugs) <= CHUNK and len(set(slugs)) == len(slugs)
    path = os.path.join(docs_dir, "%s.json.gz" % slugs[0])
    if os.path.exists(path):
        with gzip.open(path, "rb") as fh:
            docs = json.loads(fh.read(), parse_float=D)
    else:
        q = [("slug", s) for s in slugs] + [("closed", "true"), ("limit", str(len(slugs) + 5))]
        body, docs = http_json(GAMMA + "?" + urllib.parse.urlencode(q))
        write_atomic(path, gz_bytes(body))
    return by_slug(docs, slugs)

# ---- the rules: the chain book's window, the settled documents, the identities ----------------


def window_problem(w, t):
    """The first condition a window.json fails, or None, with the chain book's token map."""
    if not isinstance(w, dict) or w.get("T") != t:
        return "window T", None
    if w.get("documents_ok") is not True:
        return "documents", None
    if w.get("checkpoints_complete") != len(OFFSETS) or w.get("missed") != 0:
        return "incomplete", None
    mk = w.get("markets")
    if not (isinstance(mk, dict) and set(mk) == {"m15", "m5"}
            and all(isinstance(v, dict) for v in mk.values())):
        return "markets", None
    if mk["m15"].get("slug") != slug15(t) or mk["m5"].get("slug") != slug5(t + 600):
        return "slugs", None
    mapping = {}
    for m in ("m15", "m5"):
        outs = loads_maybe(mk[m].get("outcomes"))
        toks = loads_maybe(mk[m].get("clobTokenIds"))
        cond = mk[m].get("conditionId")
        if outs != ["Up", "Down"] or not two_tokens(toks) or not CONDITION.fullmatch(cond or ""):
            return "tokens", None
        mapping[m] = {"Up": toks[0], "Down": toks[1], "condition": cond}
    return None, mapping


def two_tokens(toks):
    return (isinstance(toks, list) and len(toks) == 2 and toks[0] != toks[1]
            and all(isinstance(x, str) and x.isdigit() for x in toks))


def chainbook_window(root, t):
    """A considered window as the chain book stored it: the reason it is not a member, or its token map.
    window.json carries counts, times and token ids (map section 2.5's exception); nothing else is opened."""
    d = os.path.join(root, str(t))
    if not os.path.isdir(d):
        return "no directory", None
    if not os.path.isfile(os.path.join(d, "window.json")):
        return "no window.json", None
    if not os.path.isfile(os.path.join(d, "books.jsonl.gz")):
        return "no books", None
    with open(os.path.join(d, "window.json"), "rb") as fh:
        raw = fh.read()
    try:
        w = json.loads(raw)
    except ValueError:
        return "window.json", None
    return window_problem(w, t)


def readings_of(doc):
    """priceToBeat and finalPrice from events[0].eventMetadata, as the venue printed them, or None, None."""
    ev = doc.get("events")
    if not (isinstance(ev, list) and ev and isinstance(ev[0], dict)):
        return None, None
    em = ev[0].get("eventMetadata")
    if not isinstance(em, dict):
        return None, None
    vals = []
    for k in ("priceToBeat", "finalPrice"):
        v = em.get(k)
        if isinstance(v, bool) or not isinstance(v, (D, int)) or not v > 0:
            return None, None
        vals.append(D(v) if isinstance(v, int) else v)
    return vals[0], vals[1]


def outcome_of(doc):
    return {("1", "0"): "Up", ("0", "1"): "Down"}[tuple(loads_maybe(doc["outcomePrices"]))]


def doc_problem(doc, start, cb):
    """The first condition a settled document fails, or None. `cb` is the chain book's map for that market,
    or None in the rehearsal, which has no chain book."""
    if doc is None:
        return "absent"
    if doc.get("closed") is not True:
        return "open"
    if loads_maybe(doc.get("outcomes")) != ["Up", "Down"]:
        return "outcomes"
    if loads_maybe(doc.get("outcomePrices")) not in (["1", "0"], ["0", "1"]):
        return "unresolved"
    if doc.get("feeType") != FEE_TYPE or doc.get("feeSchedule") != FEE_SCHEDULE:
        return "fee"
    if doc.get("eventStartTime") != iso(start):
        return "start"
    if not CONDITION.fullmatch(doc.get("conditionId") or ""):
        return "condition"
    toks = loads_maybe(doc.get("clobTokenIds"))
    if not two_tokens(toks):
        return "tokens"
    if cb is not None and (toks != [cb["Up"], cb["Down"]] or doc["conditionId"] != cb["condition"]):
        return "not the chain book's tokens"
    ptb, fin = readings_of(doc)
    if ptb is None:
        return "readings"
    return None


def identities(d15, d5):
    """E1: one reading settles both, the same literal. E2 and E3: each outcome is Up iff its finalPrice is
    at or above its priceToBeat."""
    p15, f15 = readings_of(d15)
    p5, f5 = readings_of(d5)
    return (lit(f15) == lit(f5), (outcome_of(d15) == "Up") == (f15 >= p15),
            (outcome_of(d5) == "Up") == (f5 >= p5))


def pairs_of(dv):
    """The dominated pairs of a window: A where the 5m strike is above the 15m's, B below, both at equal."""
    return ["A"] if dv > 0 else (["B"] if dv < 0 else ["A", "B"])


def payoff(pair, r0, r600, r900):
    """What the pair pays at settlement, per share of each leg: the containment, by its own outcomes."""
    up15, up5 = 1 if r900 >= r0 else 0, 1 if r900 >= r600 else 0
    return (up15 + 1 - up5) if pair == "A" else (up5 + 1 - up15)

# ---- the costs -----------------------------------------------------------------------------------


def costs(a):
    """One share bought at a, its fee tz14.fee_pp(a), two ways the venue could collect it: on top of the
    price, a + fee; or in shares, a / (1 - fee / a), the cost of one share net of the fee."""
    f = tz14().fee_pp(a)
    return a + f, a / (1 - f / a)


def classify(ax, ay, skew_ns, dt_ms):
    """The pair's cost a share of each leg after both taker fees, and its class. firm: below 1 with the fee
    collected either way, the two replies received at most SKEW_BOUND_NS apart and the two books' own
    timestamps at most TS_BOUND_MS apart. loose: below 1 with the fee on top, but not firm. none: at or above
    1 with the fee on top. unquoted: a leg has no ask at the venue's minimum size."""
    r = {"k_top": None, "k_shares": None, "cls": "unquoted", "sub": ""}
    if ax is None or ay is None:
        return r
    tx, sx = costs(ax)
    ty, sy = costs(ay)
    r["k_top"], r["k_shares"] = tx + ty, sx + sy
    timed = skew_ns is not None and dt_ms is not None
    together = timed and skew_ns <= SKEW_BOUND_NS and dt_ms <= TS_BOUND_MS
    if r["k_shares"] < 1 and together:
        r["cls"] = "firm"
    elif r["k_top"] < 1:
        r["cls"] = "loose"
        r["sub"] = "convention" if r["k_shares"] >= 1 else ("no time" if not timed else "apart")
    else:
        r["cls"] = "none"
    return r


def reading_of(n_clean, v_firm, v_any):
    """Section 4.3: VIOLATION on one firm window; NONE on no window firm or loose among at least N_MIN
    members whose every unit read valid; UNDECIDABLE otherwise."""
    if v_firm >= 1:
        return "VIOLATION"
    if v_any == 0 and n_clean >= N_MIN:
        return "NONE"
    return "UNDECIDABLE"


def theta1(n):
    """NONE's alternative: the per-window violation probability at which no violation in n windows has
    probability exactly ALPHA."""
    return 1 - (ALPHA.ln() / n).exp()


def power(n, theta):
    return 1 - (1 - theta) ** n

# ---- the set -------------------------------------------------------------------------------------


def form_set(base, root, ts, docs_fn, chainbook=True, budget_s=None):
    """Every considered window, in order, with its status; and the members with what the score needs."""
    os.makedirs(base, exist_ok=True)
    setp = os.path.join(base, "set.json")
    if os.path.exists(setp):
        with open(setp, encoding="utf-8") as fh:
            s = json.load(fh)
        out("the set from %s sha256 %s: %d considered, %d members" % (
            setp, sha256_file(setp), len(s["considered"]), len(s["members"])))
        return s
    t0 = time.time()
    status, pending = {}, []
    for t in ts:
        why, mapping = chainbook_window(root, t) if chainbook else (None, None)
        status[t] = why
        if why is None:
            pending.append((t, mapping))
    docs_dir = os.path.join(base, "docs")
    os.makedirs(docs_dir, exist_ok=True)
    members, requests = [], 0
    total = -(-len(pending) // (CHUNK // 2))
    t_req = time.time()
    for i in range(0, len(pending), CHUNK // 2):
        grp = pending[i:i + CHUNK // 2]
        slugs = [s for t, _m in grp for s in (slug15(t), slug5(t + 600))]
        by = docs_fn(docs_dir, slugs)
        requests += 1
        if budget_s is not None and requests == 20:
            proj = (time.time() - t_req) / 20 * total
            out("projected %.0f s for %d document requests after 20" % (proj, total))
            assert proj <= budget_s, "BLOCKED: the fetch projected at %.0f s, above %d" % (proj, budget_s)
        for t, mapping in grp:
            d15, d5 = by.get(slug15(t)), by.get(slug5(t + 600))
            why = doc_problem(d15, t, mapping and mapping["m15"])
            if why:
                status[t] = "15m document: " + why
                continue
            why = doc_problem(d5, t + 600, mapping and mapping["m5"])
            if why:
                status[t] = "5m document: " + why
                continue
            e1, e2, e3 = identities(d15, d5)
            if not (e1 and e2 and e3):
                status[t] = "E1" if not e1 else ("E2" if not e2 else "E3")
                continue
            p15, f15 = readings_of(d15)
            p5, _f5 = readings_of(d5)
            dv = p5 - p15
            t15, t5 = loads_maybe(d15["clobTokenIds"]), loads_maybe(d5["clobTokenIds"])
            members.append({
                "T": t, "R0": lit(p15), "R600": lit(p5), "R900": lit(f15), "D": fx(dv),
                "O15": outcome_of(d15), "O5": outcome_of(d5), "pairs": pairs_of(dv),
                "map": {"m15": {"Up": t15[0], "Down": t15[1], "condition": d15["conditionId"]},
                        "m5": {"Up": t5[0], "Down": t5[1], "condition": d5["conditionId"]}}})
            status[t] = "member"
    s = {"first": ts[0], "last": ts[-1], "considered": [[t, status[t]] for t in ts],
         "members": members, "requests": requests}
    write_atomic(setp, dumps(s).encode("utf-8"))
    out("the set formed in %.1f s: %d considered, %d members, %d document requests, %s sha256 %s" % (
        time.time() - t0, len(ts), len(members), requests, setp, sha256_file(setp)))
    with open(setp, encoding="utf-8") as fh:
        return json.load(fh)


def weekend(t):
    return 1 if datetime.datetime.fromtimestamp(t, datetime.timezone.utc).weekday() >= 5 else 0


def build_constants(base, s, label):
    """Book-free: the members, N, NONE's alternative and VIOLATION's power. A second run must write the
    same bytes."""
    ms = s["members"]
    n = len(ms)
    ts = [m["T"] for m in ms]
    th = theta1(n) if n else None
    c = {"label": label, "considered": len(s["considered"]), "members": n,
         "first": ts[0] if ts else None, "last": ts[-1] if ts else None,
         "member_list_sha": sha256_bytes(("\n".join(map(str, ts)) + "\n").encode()),
         "set_sha": sha256_file(os.path.join(base, "set.json")),
         "non_members": [[t, st] for t, st in s["considered"] if st != "member"],
         "pairs": {k: sum(1 for m in ms if m["pairs"] == v) for k, v in
                   (("A", ["A"]), ("B", ["B"]), ("AB", ["A", "B"]))},
         "weekend": sum(weekend(t) for t in ts),
         "spans": {"1": sum(1 for t in ts if t < SECOND_SPAN), "2": sum(1 for t in ts if t >= SECOND_SPAN)},
         "alpha": ALPHA, "n_min": N_MIN, "none_possible": n >= N_MIN, "theta1": th,
         "powers": {fx(th_): power(n, th_) for th_ in THETAS},
         "skew_bound_ns": SKEW_BOUND_NS, "ts_bound_ms": TS_BOUND_MS, "taus": list(TAUS)}
    path = os.path.join(base, "%s-constants.json" % label)
    return c, path, write_once(path, dumps(c).encode("utf-8"))


def show_constants(c, path, sha):
    out("considered %d, members %d, first %s %s, last %s %s, weekend members %d, by span %s" % (
        c["considered"], c["members"], c["first"], utc(c["first"]) if c["first"] else "-", c["last"],
        utc(c["last"]) if c["last"] else "-", c["weekend"], c["spans"]))
    out("member list sha %s; set sha %s" % (c["member_list_sha"], c["set_sha"]))
    out("members by pair: %s" % c["pairs"])
    for t, st in c["non_members"]:
        out("non-member %d %s: %s" % (t, utc(t), st))
    out("NONE possible: %s (N %d, N_MIN %d); its alternative theta1 = %s a window" % (
        c["none_possible"], c["members"], N_MIN, fx(c["theta1"]) if c["theta1"] is not None else "-"))
    for k, v in sorted(c["powers"].items()):
        out("power of VIOLATION against a firm-violation probability of %s a window: %s" % (k, fx(v)))
    out("wrote %s sha256 %s" % (path, sha))

# ---- the books -----------------------------------------------------------------------------------


def read_books(root, t):
    """A member's stored lines, parsed, or the reason they cannot be. Total: data never raises here."""
    path = os.path.join(root, str(t), "books.jsonl.gz")
    try:
        with gzip.open(path, "rb") as fh:
            text = fh.read().decode("utf-8")
        return [json.loads(ln) for ln in text.split("\n") if ln], None
    except (OSError, EOFError, ValueError, zlib.error) as e:
        return None, "books unreadable: %s" % type(e).__name__


def venue_ms(book):
    """The reply's own timestamp in milliseconds, or None where it is not a run of ASCII digits."""
    v = book.get("timestamp")
    s = str(v) if v is not None else ""
    return int(s) if s.isascii() and s.isdigit() else None


def line_check(ln, t, member):
    """One stored reply: its problem, or None with what the pair needs from it."""
    if not isinstance(ln, dict) or frozenset(ln) != BOOK_KEYS:
        return "keys", None
    m = ln["market"]
    if ln["T"] != t or m not in ("m15", "m5") or ln["tau_prime"] not in TAUS:
        return "place", None
    if ln["slug"] != (slug15(t) if m == "m15" else slug5(t + 600)):
        return "slug", None
    if ln["status"] != 200:
        return "status", None
    raw = ln["raw"]
    if not isinstance(raw, str):
        return "raw", None
    try:
        b = raw.encode("utf-8")
    except UnicodeEncodeError:
        return "raw", None
    if ln["bytes"] != len(b) or ln["sha256"] != sha256_bytes(b):
        return "hash", None
    mp = member["map"][m]
    outcome = {mp["Up"]: "Up", mp["Down"]: "Down"}.get(ln["token_id"]) if isinstance(
        ln["token_id"], str) else None
    if outcome is None or ln["outcome_label"] != outcome:
        return "token", None
    try:
        book = tz14().book_of(raw)
    except Exception:            # the reply is data: a body that cannot be parsed is a finding, never a stop
        return "body", None
    if not book["ok"] or book["bad_levels"]:
        return "body", None
    if not (book["min_order_size_present"] and book["tick_size_present"]):
        return "size or tick", None
    try:
        size, tick = D(str(book["min_order_size"])), D(str(book["tick_size"]))
        if not (size > 0 and tick > 0):
            return "size or tick", None
    except ArithmeticError:
        return "size or tick", None
    if str(book["asset_id"]) != ln["token_id"]:
        return "asset", None
    return None, {"outcome": outcome, "book": book, "size": size, "tick": tick, "ts": venue_ms(book),
                  "recv": ln["recv_mono_ns"] if type(ln["recv_mono_ns"]) is int else None,
                  "wall": ln["recv_wall_ns"] if type(ln["recv_wall_ns"]) is int else None}


def units_of(member, lines):
    """Per tau': (tau, problem, legs) - legs maps (market, outcome) to what line_check returned."""
    t = member["T"]
    by_tau = {tau: [] for tau in TAUS}
    for ln in lines:
        k = ln.get("tau_prime") if isinstance(ln, dict) else None
        if type(k) is int and k in by_tau:
            by_tau[k].append(ln)
    res = []
    for tau in TAUS:
        lns, legs, why = by_tau[tau], {}, None
        if len(lns) != 4:
            why = "lines %d" % len(lns)
        for ln in lns if why is None else ():
            why, info = line_check(ln, t, member)
            if why:
                break
            key = (ln["market"], info["outcome"])
            if key in legs:
                why = "duplicate"
                break
            legs[key] = info
        res.append((tau, why, legs if why is None else None))
    return res


COLS = ["T", "tau", "pair", "valid", "why", "ask_x", "ask_y", "k_top", "k_shares", "cls", "sub", "skew_ns",
        "ts_x", "ts_y", "dt_ms", "lag_x_ms", "lag_y_ms", "q_x", "q_y"]


def lag_ms(leg):
    """Milliseconds from the reply's own timestamp to its receipt, on the host's wall clock."""
    return None if leg["ts"] is None or leg["wall"] is None else leg["wall"] // 1000000 - leg["ts"]


def rows_of(member, units):
    """One row a unit and pair; an invalid unit is one row with its problem."""
    rows = []
    for tau, why, legs in units:
        if why is not None:
            rows.append({"T": member["T"], "tau": tau, "pair": "-", "valid": 0, "why": why})
            continue
        for pair in member["pairs"]:
            x, y = (legs[k] for k in LEGS[pair])
            skew = None if x["recv"] is None or y["recv"] is None else abs(x["recv"] - y["recv"])
            try:
                tx = tz14().touch_of(x["book"], x["size"], x["tick"])
                ty = tz14().touch_of(y["book"], y["size"], y["tick"])
                if any(a is not None and a <= 0 for a in (tx["ask5"], ty["ask5"])):
                    rows.append({"T": member["T"], "tau": tau, "pair": pair, "valid": 0, "why": "price"})
                    continue
                dt = None if x["ts"] is None or y["ts"] is None else abs(x["ts"] - y["ts"])
                r = classify(tx["ask5"], ty["ask5"], skew, dt)
            except ArithmeticError:
                rows.append({"T": member["T"], "tau": tau, "pair": pair, "valid": 0, "why": "levels"})
                continue
            r.update({"T": member["T"], "tau": tau, "pair": pair, "valid": 1, "why": "",
                      "ask_x": tx["ask5"], "ask_y": ty["ask5"], "skew_ns": skew,
                      "ts_x": x["ts"], "ts_y": y["ts"], "dt_ms": dt,
                      "lag_x_ms": lag_ms(x), "lag_y_ms": lag_ms(y),
                      "q_x": tx["cum"]["ask"][0], "q_y": ty["cum"]["ask"][0]})
            rows.append(r)
    return rows


def cell(v):
    if v is None:
        return ""
    return fx(v) if isinstance(v, D) else str(v)


def band_of(dv):
    a = abs(dv)
    return "<1" if a < 1 else ("1-10" if a < 10 else ("10-100" if a < 100 else ">=100"))


def score(base, root, s, c, label):
    """The members' books, read once, and the reading. Everything after the first book is total."""
    ms = s["members"]
    n = len(ms)
    assert c["members"] == n and c["member_list_sha"] == sha256_bytes(
        ("\n".join(str(m["T"]) for m in ms) + "\n").encode()), "score: the constants are not this set's"
    lines_csv = [",".join(COLS)]
    allrows, flags = [], []
    invalid, clean = {}, 0
    for m in ms:
        lines, why = read_books(root, m["T"])
        units = ([(tau, why, None) for tau in TAUS] if lines is None else units_of(m, lines))
        rows = rows_of(m, units)
        for r in rows:
            if not r["valid"]:
                invalid[r["why"]] = invalid.get(r["why"], 0) + 1
            lines_csv.append(",".join(cell(r.get(k)) for k in COLS))
        allrows += [(m, r) for r in rows]
        flags.append((m, any(r.get("cls") == "firm" for r in rows),
                      any(r.get("cls") in ("firm", "loose") for r in rows)))
        clean += 1 if all(r["valid"] for r in rows) else 0
    v_firm = sum(1 for _m, f, _a in flags if f)
    v_any = sum(1 for _m, _f, a in flags if a)
    word = reading_of(clean, v_firm, v_any)
    valid = [(m, r) for m, r in allrows if r["valid"]]
    cls_n = {k: sum(1 for _m, r in valid if r["cls"] == k) for k in ("firm", "loose", "none", "unquoted")}
    sub_n = {k: sum(1 for _m, r in valid if r["cls"] == "loose" and r["sub"] == k)
             for k in ("convention", "apart", "no time")}
    by_tau = {str(tau): {k: sum(1 for _m, r in valid if r["tau"] == tau and r["cls"] == k)
                         for k in ("firm", "loose", "none", "unquoted")} for tau in TAUS}
    by_pair = {p: {k: sum(1 for _m, r in valid if r["pair"] == p and r["cls"] == k)
                   for k in ("firm", "loose", "none", "unquoted")} for p in ("A", "B")}
    closest = {}
    for tau in TAUS:
        for p in ("A", "B"):
            q = [(r["k_top"], m["T"], r) for m, r in valid if r["tau"] == tau and r["pair"] == p and
                 r["k_top"] is not None]
            if q:
                k, t, r = min(q, key=lambda z: (z[0], z[1]))
                closest["%d %s" % (tau, p)] = {"T": t, "ask_x": r["ask_x"], "ask_y": r["ask_y"],
                                               "k_top": k, "k_shares": r["k_shares"],
                                               "skew_ns": r["skew_ns"]}
    firm = [(m, r) for m, r in valid if r["cls"] == "firm"]
    loose = [(m, r) for m, r in valid if r["cls"] == "loose"]
    best = {}
    for m, r in firm:
        p = (1 - r["k_shares"]) * min(r["q_x"], r["q_y"])
        best[m["T"]] = max(best.get(m["T"], D(0)), p)
    profit = sum(best.values(), D(0))
    bands = {}
    for m, f, a in flags:
        b = bands.setdefault(band_of(D(m["D"])), {"members": 0, "firm": 0, "any": 0})
        b["members"] += 1
        b["firm"] += f
        b["any"] += a
    res = {
        "label": label, "members": n, "units": n * len(TAUS), "rows": len(allrows),
        "invalid": invalid, "classes": cls_n, "loose_by": sub_n, "by_tau": by_tau, "by_pair": by_pair,
        "v_firm": v_firm, "v_any": v_any, "reading": word, "n_clean": clean,
        "none_possible": clean >= N_MIN, "theta1_clean": theta1(clean) if clean else None,
        "pre_fee_inversions": sum(1 for _m, r in valid if r["ask_x"] is not None and
                                  r["ask_y"] is not None and r["ask_x"] + r["ask_y"] < 1),
        "closest": closest,
        "firm_margin_shares": quantiles([1 - r["k_shares"] for _m, r in firm]),
        "firm_skew_ns": quantiles([r["skew_ns"] for _m, r in firm]),
        "firm_dt_ms": quantiles([r["dt_ms"] for _m, r in firm if r["dt_ms"] is not None]),
        "firm_lag_ms": quantiles([v for _m, r in firm for v in (r["lag_x_ms"], r["lag_y_ms"])
                                  if v is not None]),
        "firm_q": quantiles([min(r["q_x"], r["q_y"]) for _m, r in firm]),
        "firm_profit_at_touch": profit,
        "firm_profit_per_day": (profit * 96 / n) if n else None,
        "loose_margin_top": quantiles([1 - r["k_top"] for _m, r in loose]),
        "d_bands": bands,
    }
    units_csv = ("\n".join(lines_csv) + "\n").encode("utf-8")
    body = dumps(res).encode("utf-8")
    hu = write_once(os.path.join(base, "%s-units.csv" % label), units_csv)
    hr = write_once(os.path.join(base, "%s-reading.json" % label), body)
    out("books: %d members, %d units, %d rows, invalid %s" % (n, n * len(TAUS), len(allrows), invalid))
    out("rows by class: %s; loose by reason: %s" % (cls_n, sub_n))
    for tau in TAUS:
        out("tau' %3d: %s" % (tau, by_tau[str(tau)]))
    out("by pair: %s" % by_pair)
    out("windows with a firm violation V_firm %d of %d; with any V_any %d of %d; clean members %d" % (
        v_firm, n, v_any, n, clean))
    out("NONE possible: %s; its alternative at the clean members, theta1 = %s a window" % (
        res["none_possible"], cell(res["theta1_clean"])))
    out("ROW columns: class,reason,T,tau',pair,ask_x,ask_y,k_top,k_shares,skew_ns,ts_x,ts_y,dt_ms,q_x,q_y,"
        "R0,R600")
    for name, group in (("firm", firm), ("loose", loose)):
        for m, r in group[:ROWS_SHOWN]:
            out("ROW %s,%s,%d,%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (
                r["cls"], r["sub"], r["T"], r["tau"], r["pair"], cell(r["ask_x"]), cell(r["ask_y"]),
                cell(r["k_top"]), cell(r["k_shares"]), cell(r["skew_ns"]), cell(r["ts_x"]),
                cell(r["ts_y"]), cell(r["dt_ms"]), cell(r["q_x"]), cell(r["q_y"]), m["R0"], m["R600"]))
        if len(group) > ROWS_SHOWN:
            out("%d more %s rows, in %s-units.csv" % (len(group) - ROWS_SHOWN, name, label))
    for k, v in sorted(closest.items(), key=lambda kv: (-int(kv[0].split()[0]), kv[0])):
        out("closest tau' %s: T %d ask_x %s ask_y %s k_top %s k_shares %s skew_ns %s - barred" % (
            k, v["T"], cell(v["ask_x"]), cell(v["ask_y"]), cell(v["k_top"]), cell(v["k_shares"]),
            cell(v["skew_ns"])))
    out("pre-fee inversions, ask_x + ask_y < 1: %d rows - barred" % res["pre_fee_inversions"])
    for k in ("firm_margin_shares", "firm_skew_ns", "firm_dt_ms", "firm_lag_ms", "firm_q",
              "loose_margin_top"):
        q = res[k]
        out("%s: %s - barred" % (k, "none" if q is None else
                                 ", ".join("%s %s" % (kk, cell(vv)) for kk, vv in q.items())))
    out("firm profit at the touch, the best unit a window: %s USDC, %s a day of members - barred" % (
        fx(profit), cell(res["firm_profit_per_day"])))
    out("members by |D| in USD: %s - barred" % bands)
    out("wrote %s-units.csv sha256 %s and %s-reading.json sha256 %s" % (label, hu, label, hr))
    return res

# ---- modes ---------------------------------------------------------------------------------------


def git(*args):
    cp = subprocess.run(["git", "-C", WT] + list(args), capture_output=True, text=True)
    assert cp.returncode == 0, "git %s: %s" % (" ".join(args), cp.stderr.strip())
    return cp.stdout.strip()


ROW = re.compile(r"^\| `([^`]+)` \| ([0-9,]+|—) \| ([0-9,]+|—) \| (frozen|tracked|reported) \| "
                 r"`?([0-9a-f]{64}|self-reference[^|]*?)`? \|$", re.M)
ANCHOR_ROW = re.compile(r"^\| `(A[0-9])` — [^|]*\| `([^`]+)` \|$", re.M)


def mode_fingerprint():
    """Contract section 1 steps 3 and 4, asserted: map section 0 against the primary checkout."""
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
        tail = " equal" if state == "frozen" else ""
        out("%-44s %6d lines %8d bytes %s %s%s" % (path, got[0], got[1], got[2], state, tail))
    out("FINGERPRINT PASS: revision %s; anchors 6 of 6, 4 re-derived; rows %d: frozen %d of %d equal, "
        "tracked %d, reported %d" % (MAP_REVISION, len(rows), states["frozen"], MAP_ROWS["frozen"],
                                     states["tracked"], states["reported"]))


def mode_rehearse():
    floor_check()
    base = os.path.join(WORK, "rehearsal")
    ts = [REHEARSAL[0] + WINDOW * k for k in range(REHEARSAL[1])]
    s = form_set(base, None, ts, gamma_cached, chainbook=False)
    ms = s["members"]
    dvs = [D(m["D"]) for m in ms]
    lines = ["%d,%s,%s,%s,%s,%s" % (m["T"], m["R0"], m["R600"], m["R900"], m["O15"], m["O5"]) for m in ms]
    got = {"windows": len(s["considered"]), "members": len(ms),
           "d_pos": sum(1 for d in dvs if d > 0), "d_neg": sum(1 for d in dvs if d < 0),
           "d_zero": sum(1 for d in dvs if d == 0),
           "up15": sum(1 for m in ms if m["O15"] == "Up"), "up5": sum(1 for m in ms if m["O5"] == "Up"),
           "sum_d": sum(dvs, D(0)), "sum_abs_d": sum((abs(d) for d in dvs), D(0)),
           "digest": sha256_bytes(("\n".join(lines) + "\n").encode())}
    for t, st in s["considered"]:
        if st != "member":
            out("rehearsal non-member %d: %s" % (t, st))
    bad = [k for k in REF if got[k] != REF[k]]
    for k in REF:
        out("G-REHEARSAL %-9s instrument %s, the Architect's %s, %s" % (
            k, cell(got[k]), cell(REF[k]), "equal" if got[k] == REF[k] else "DIFFERENT"))
    assert not bad, "G-REHEARSAL FAIL: %s" % bad
    out("G-REHEARSAL PASS: %d of %d figures equal; %d document requests" % (
        len(REF), len(REF), s["requests"]))


def considered_windows():
    return [FIRST_T + WINDOW * k for k in range(CONSIDERED)]


def mode_fetch():
    floor_check()
    os.makedirs(WORK, exist_ok=True)
    base = os.path.join(WORK, "set")
    s = form_set(base, CHAINBOOK, considered_windows(), gamma_cached, budget_s=FETCH_BUDGET_S)
    assert [t for t, _st in s["considered"]] == considered_windows(), "G-SET: the considered windows"
    assert all(st for _t, st in s["considered"]), "G-SET: a window without a status"
    assert [m["T"] for m in s["members"]] == [t for t, st in s["considered"] if st == "member"]
    st = load_state()
    st["set_sha"] = sha256_file(os.path.join(base, "set.json"))
    save_state(st)
    reasons = {}
    for _t, w in s["considered"]:
        reasons[w] = reasons.get(w, 0) + 1
    out("G-SET PASS: %d considered, %d members; statuses %s; set.json sha256 %s" % (
        len(s["considered"]), len(s["members"]), dict(sorted(reasons.items())), st["set_sha"]))


def the_set():
    base = os.path.join(WORK, "set")
    with open(os.path.join(base, "set.json"), encoding="utf-8") as fh:
        return base, json.load(fh)


def mode_constants():
    floor_check()
    base, s = the_set()
    st = load_state()
    assert sha256_file(os.path.join(base, "set.json")) == st.get("set_sha"), "constants: not G-SET's set"
    c, path, sha = build_constants(base, s, "tz24")
    show_constants(c, path, sha)
    st["constants_sha"] = sha
    st["constants_at"] = utc(time.time())
    save_state(st)


def mode_score():
    floor_check()
    base, s = the_set()
    st = load_state()
    cpath = os.path.join(base, "tz24-constants.json")
    assert sha256_file(cpath) == st.get("constants_sha"), "score: not the constants recorded"
    with open(cpath, encoding="utf-8") as fh:
        c = json.load(fh, parse_float=D)
    assert c["set_sha"] == sha256_file(os.path.join(base, "set.json")), "score: not the constants' set"
    head = git("rev-parse", "HEAD")
    branches = git("branch", "-r", "--contains", head).split()
    assert "origin/" + BRANCH in branches, "score: HEAD %s is not on origin" % head
    with open(LEDGER, "a", encoding="utf-8") as fh:
        fh.write(dumps({"at": utc(time.time()), "head": head, "members": c["members"],
                        "member_list_sha": c["member_list_sha"], "constants_sha": st["constants_sha"]}))
    BOOKS_OPEN[0] = True
    res = score(base, CHAINBOOK, s, c, "tz24")
    out("B2 READING: %s" % res["reading"])


def mode_still():
    st = load_state()
    now = {}
    for key, unit in UNITS.items():
        cp = subprocess.run(["systemctl", "show", unit, "-p", "MainPID", "-p", "NRestarts",
                             "-p", "ActiveState", "-p", "MemoryCurrent", "-p", "MemoryPeak"],
                            capture_output=True, text=True)
        assert cp.returncode == 0, cp.stderr
        kv = dict(line.split("=", 1) for line in cp.stdout.split("\n") if "=" in line)
        now[key] = {k: kv[k] for k in ("MainPID", "NRestarts", "ActiveState")}
        out("%s %s, MemoryCurrent %s, MemoryPeak %s" % (unit, now[key], kv.get("MemoryCurrent"),
                                                        kv.get("MemoryPeak")))
    if "still" not in st:
        st["still"] = {"at": utc(time.time()), "units": now}
        save_state(st)
        out("still: recorded")
        return
    same = now == st["still"]["units"]
    out("G-STILL %s: %s since %s" % ("PASS" if same else "FAIL", "unchanged" if same else
                                     "changed", st["still"]["at"]))


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


def report_tokens():
    tokens = set()
    for name in sorted(os.listdir(REPORTS)):
        if name.endswith(".md"):
            with open(os.path.join(REPORTS, name), encoding="utf-8", errors="replace") as fh:
                tokens.update(TOKEN.findall(fh.read()))
    return tokens


def by_name(tree, rel):
    """Kept whatever a report prints: the state, the ledger, the logs, and the venue's documents as served."""
    return tree == WORK and (rel == "state.json" or rel == "book-ledger.jsonl" or rel.startswith("logs/")
                             or rel.startswith("set/docs/") or rel.startswith("rehearsal/docs/"))


def pristine(tree):
    cp = subprocess.run(["git", "-C", tree, "status", "--porcelain", "--ignored"],
                        capture_output=True, text=True)
    assert cp.returncode == 0 and cp.stdout == "", "reclaim: %s holds %r" % (tree, cp.stdout[:400])
    head = subprocess.run(["git", "-C", tree, "rev-parse", "HEAD"], capture_output=True,
                          text=True).stdout.strip()
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
            assert not [p for p, s, _a in procs if s - 1 <= b <= s + LIVE_S], \
                "reclaim: %s belongs to a running process" % t
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
                dest = os.path.join(FORENSICS, os.path.basename(tree) + "--"
                                    + rel.replace("/", "--"))
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
    out("RECLAIM PASS: %d files considered, %d named by a report, %d kept by name, %d copied, "
        "%d already held; forensic store %d -> %d files" % (
            considered, named, kept, copied, held, before, after))

# ---- the self-test -------------------------------------------------------------------------------


def synth_reply(token, cond, bids, asks, ts, tick="0.01"):
    """A /book reply as the venue sends it: bids ascending and asks descending, the worst price first."""
    return json.dumps({
        "market": cond, "asset_id": token, "timestamp": str(ts), "hash": sha256_bytes(token.encode())[:40],
        "bids": [{"price": p, "size": q} for p, q in sorted(bids, key=lambda z: D(z[0]))],
        "asks": [{"price": p, "size": q} for p, q in sorted(asks, key=lambda z: -D(z[0]))],
        "min_order_size": "5", "tick_size": tick, "neg_risk": False, "last_trade_price": "0.5"},
        separators=(",", ":"))


def synth_window(root, t, mp, books, complete=7):
    """window.json and books.jsonl.gz in the chain book's own format. books[(tau, market, outcome)] is
    (bids, asks, tick, receive delay ms, book time shift ms); a missing key is a coherent book around 0.5.
    The reply's own timestamp is 20 ms after the checkpoint plus the shift, its receipt 45 ms after plus the
    delay."""
    d = os.path.join(root, str(t))
    os.makedirs(d, exist_ok=True)
    lines = []
    for off, tau in zip(OFFSETS, TAUS):
        for m in ("m15", "m5"):
            for o in ("Up", "Down"):
                tok = mp[m][o]
                bids, asks, tick, late, shift = books.get((tau, m, o), (
                    [("0.48", "100"), ("0.47", "300")], [("0.52", "100"), ("0.53", "300")], "0.01", 0, 0))
                raw = synth_reply(tok, mp[m]["condition"], bids, asks, (t + off) * 1000 + 20 + shift, tick)
                b = raw.encode()
                lines.append(json.dumps({
                    "T": t, "tau_prime": tau, "market": m,
                    "slug": slug15(t) if m == "m15" else slug5(t + 600),
                    "token_id": tok, "outcome_label": o, "url": "u", "status": 200,
                    "send_mono_ns": 10 ** 12 + off * 10 ** 9,
                    "recv_mono_ns": 10 ** 12 + off * 10 ** 9 + (40 + late) * 10 ** 6,
                    "recv_wall_ns": ((t + off) * 1000 + 45 + late) * 10 ** 6, "bytes": len(b),
                    "sha256": sha256_bytes(b),
                    "raw": raw, "reason": None}, sort_keys=True, separators=(",", ":")))
    with open(os.path.join(d, "books.jsonl.gz"), "wb") as fh:
        fh.write(gz_bytes(("\n".join(lines) + "\n").encode()))
    wj = {"T": t, "document_instant": t + 625, "closed_wall_ns": (t + 905) * 10 ** 9, "documents_ok": True,
          "checkpoints_complete": complete, "status_counts": {"200": 28}, "skews_ns": [1] * 7, "missed": 0,
          "markets": {m: {"slug": slug15(t) if m == "m15" else slug5(t + 600),
                          "clobTokenIds": json.dumps([mp[m]["Up"], mp[m]["Down"]]),
                          "outcomes": '["Up", "Down"]', "conditionId": mp[m]["condition"]}
                      for m in ("m15", "m5")}}
    with open(os.path.join(d, "window.json"), "wb") as fh:
        fh.write(dumps(wj).encode())


def synth_doc(slug, start, mp, ptb, fin, up, fee=None):
    return {"slug": slug, "closed": True, "outcomes": '["Up", "Down"]',
            "outcomePrices": '["1", "0"]' if up else '["0", "1"]', "feeType": FEE_TYPE,
            "feeSchedule": fee or dict(FEE_SCHEDULE), "eventStartTime": iso(start),
            "conditionId": mp["condition"], "clobTokenIds": json.dumps([mp["Up"], mp["Down"]]),
            "events": [{"eventMetadata": {"priceToBeat": D(ptb), "finalPrice": D(fin)}}]}


def mode_selftest():
    n = [0]

    def ok(cond, what):
        assert cond, "selftest: " + what
        n[0] += 1
        out("  ok  " + what)

    ok(MALLOC_TUNED, "glibc took the 128 KiB mmap threshold and the two arenas")
    ok(getcontext().prec == 60, "Decimal arithmetic at 60 digits in the thread that does every sum")
    t14 = tz14()
    ok(t14.fee_pp(D("0.50")) == D("0.0175") and t14.fee_pp(D("0.85")) == D("0.008925")
       and t14.fee_pp(D("0.90")) == D("0.0063"), "tz14.fee_pp at CANON section 1.1's three points")
    ok(getcontext().prec == 60, "loading tz14 leaves the precision at 60 digits")
    # the costs, against exact rationals computed outside this file (TZ-24 section 10, C2)
    r = classify(D("0.95"), D("0.04"), 0, 0)
    ok(r["k_top"] == D("0.996013") and r["cls"] == "firm", "0.95 + 0.04 after both fees on top: 0.996013, firm")
    ok(abs(r["k_shares"] - D("0.99621832502954164619048315760392936168528098774527312144822")) < D("1e-50"),
       "0.95 + 0.04 with the fee in shares: 1157525/1161919")
    r = classify(D("0.480"), D("0.485"), 7000000, 0)
    ok(r["k_top"] == D("0.99995625") and r["cls"] == "loose" and r["sub"] == "convention",
       "0.480 + 0.485: 0.99995625 on top, below 1; in shares above 1: loose, convention")
    ok(abs(r["k_shares"] - D("1.00127013455235589192119365130384999402817782813903228834089")) < D("1e-50"),
       "0.480 + 0.485 with the fee in shares: 1.0012701345...")
    r = classify(D("0.97"), D("0.02"), 400000000, 0)
    ok(r["k_top"] == D("0.993409") and r["cls"] == "loose" and r["sub"] == "apart",
       "0.97 + 0.02 received 400 ms apart: loose, apart")
    ok(classify(D("0.97"), D("0.02"), 150000000, 150)["cls"] == "firm",
       "received 150 ms apart, books 150 ms apart: firm")
    ok(classify(D("0.97"), D("0.02"), 150000001, 0)["cls"] == "loose", "received 150 ms and 1 ns apart: loose")
    ok(classify(D("0.97"), D("0.02"), 0, 151)["sub"] == "apart", "books 151 ms apart by their own clocks: loose")
    ok(classify(D("0.97"), D("0.02"), None, 0)["sub"] == "no time", "a leg without a receive time is not firm")
    ok(classify(D("0.97"), D("0.02"), 0, None)["sub"] == "no time", "a book without its own time is not firm")
    r = classify(D("0.996"), D("0.003"), 0, 0)
    ok(r["k_top"] == D("0.99948825") and r["cls"] == "firm" and
       abs(r["k_shares"] - D("0.99950403631641686324217092909083527810659239239162280689988")) < D("1e-50"),
       "a one-tick inversion at the 0.001 tick: 0.99948825, firm")
    r = classify(D("0.50"), D("0.50"), 0, 0)
    ok(r["k_top"] == D("1.035") and r["cls"] == "none", "0.50 + 0.50 costs 1.035: none")
    ok(classify(None, D("0.5"), 0, 0)["cls"] == "unquoted", "a leg without an ask is unquoted")
    for a in (D("0.001"), D("0.01"), D("0.3333"), D("0.5"), D("0.99"), D("0.999")):
        top, shares = costs(a)
        ok(shares >= top > a, "the fee in shares costs at least the fee on top, at %s" % a)
    # the pairs and the containment, by enumeration of the reading at T + 900
    ok(pairs_of(D("0.01")) == ["A"] and pairs_of(D("-3.5")) == ["B"] and pairs_of(D("0")) == ["A", "B"],
       "the pairs by the sign of D")
    ok(LEGS["A"] == (("m15", "Up"), ("m5", "Down")) and LEGS["B"] == (("m5", "Up"), ("m15", "Down")),
       "A buys 15m Up and 5m Down; B buys 5m Up and 15m Down")
    r0 = D("78000.5")
    for r600 in (D("78010.25"), D("77990.75"), r0):
        for r900 in (D("77980"), D("77990.75"), D("77995"), r0, D("78005"), D("78010.25"), D("78020")):
            for p in pairs_of(r600 - r0):
                ok(payoff(p, r0, r600, r900) >= 1,
                   "pair %s pays at least 1: R0 %s, R600 %s, R900 %s" % (p, r0, r600, r900))
    ok(payoff("A", r0, D("78010.25"), D("78005")) == 2, "between the strikes pair A pays 2")
    ok(payoff("A", r0, D("77990.75"), D("77995")) == 0, "pair A is not dominated where D < 0")
    # NONE's alternative and VIOLATION's power, against values computed outside this file
    ok(theta1(N_MIN) <= D("0.01") < theta1(N_MIN - 1), "N_MIN = 528 is the fewest members with theta1 <= 1%")
    ok(abs(theta1(528) - D("0.0099845124461688076149542661933792988781358095260817")) < D("1e-50"),
       "theta1(528) = 0.009984512446...")
    for k in (528, 1000, 1084, 1175):
        ok(abs((1 - theta1(k)) ** k - ALPHA) < D("1e-50"), "(1 - theta1(%d))^%d = alpha" % (k, k))
    ok(abs(power(1000, D("0.01")) - D("0.99995682875258934174901136717136474026078912309378513559")) <
       D("1e-50"), "power(1000, 0.01) = 1 - 0.99^1000")
    ok([reading_of(*a) for a in ((1084, 0, 0), (527, 0, 0), (528, 0, 0), (1084, 1, 1), (0, 2, 9),
                                 (1084, 0, 3))] ==
       ["NONE", "UNDECIDABLE", "NONE", "VIOLATION", "VIOLATION", "UNDECIDABLE"],
       "the reading table, by clean members, firm windows and any windows")
    ok(CONSIDERED == 1175 and TAUS == (245, 185, 125, 95, 65, 35, 15), "1,175 windows of seven checkpoints")
    ok(iso(FIRST_T) == "2026-09-23T17:30:00Z" and iso(LAST_T + 600) == "2026-10-05T23:10:00Z",
       "the span: 2026-09-23 17:30 to the window whose five-minute market opens 2026-10-05 23:10")
    # the audit rule, as a pure function, and the hook itself
    cb = CHAINBOOK + "/%d/%s"
    ok(cb_decision(cb % (FIRST_T, "window.json"), "rb", None, False) == "allow", "window.json read: allowed")
    ok(cb_decision(cb % (LAST_T, "books.jsonl.gz"), "rb", None, True) == "allow", "books in score: allowed")
    ok(cb_decision(cb % (LAST_T, "books.jsonl.gz"), "rb", None, False) != "allow", "books before score: refused")
    ok(cb_decision(cb % (LAST_T + WINDOW, "window.json"), "rb", None, False) != "allow",
       "a window after the span: refused")
    ok(cb_decision(cb % (FIRST_T - WINDOW, "window.json"), "rb", None, False) != "allow",
       "a window before the span: refused")
    ok(cb_decision(cb % (FIRST_T + 300, "window.json"), "rb", None, False) != "allow", "off the grid: refused")
    ok(cb_decision(cb % (FIRST_T, "window.json"), "r+b", None, False) != "allow", "a write mode: refused")
    ok(cb_decision(cb % (FIRST_T, "window.json"), None, os.O_RDWR, False) != "allow", "os.open RDWR: refused")
    ok(cb_decision(cb % (FIRST_T, "window.json"), None, os.O_RDONLY, False) == "allow", "os.open RDONLY: allowed")
    ok(cb_decision(CHAINBOOK + "/runtime.jsonl", "rb", None, False) != "allow", "runtime.jsonl: refused")
    ok(cb_decision(cb % (FIRST_T, "documents.jsonl"), "rb", None, False) != "allow", "documents.jsonl: refused")
    for p in (RECORDER + "/runtime.jsonl", CHAINBOOK + "/runtime.jsonl",
              CHAINBOOK + "/%d/books.jsonl.gz" % FIRST_T):
        try:
            open(p, "rb")
            refused = False
        except RuntimeError:
            refused = True
        except OSError:
            refused = False
        ok(refused and REFUSED[-1] == p, "the hook refuses %s before it is opened" % p)
    REFUSED.clear()
    # windows and documents
    mp = {"m15": {"Up": "111", "Down": "222", "condition": "0x" + "1" * 64},
          "m5": {"Up": "333", "Down": "444", "condition": "0x" + "2" * 64}}
    t = FIRST_T
    good = {"T": t, "documents_ok": True, "checkpoints_complete": 7, "missed": 0,
            "markets": {"m15": {"slug": slug15(t), "clobTokenIds": '["111", "222"]', "outcomes": '["Up", "Down"]',
                                "conditionId": mp["m15"]["condition"]},
                        "m5": {"slug": slug5(t + 600), "clobTokenIds": '["333", "444"]',
                               "outcomes": '["Up", "Down"]', "conditionId": mp["m5"]["condition"]}}}
    ok(window_problem(good, t) == (None, mp), "a complete window.json yields the chain book's token map")
    for change, why in ((("checkpoints_complete", 6), "incomplete"), (("missed", 1), "incomplete"),
                        (("documents_ok", False), "documents"), (("T", t + 900), "window T")):
        bad = dict(good)
        bad[change[0]] = change[1]
        ok(window_problem(bad, t)[0] == why, "%s=%r reads %s" % (change[0], change[1], why))
    d15 = synth_doc(slug15(t), t, mp["m15"], "78000.5", "78020.25", True)
    d5 = synth_doc(slug5(t + 600), t + 600, mp["m5"], "78030", "78020.25", False)
    ok(doc_problem(d15, t, mp["m15"]) is None and doc_problem(d5, t + 600, mp["m5"]) is None,
       "two settled documents that conform")
    ok(identities(d15, d5) == (True, True, True), "E1, E2 and E3 hold")
    ok(doc_problem(d15, t + 900, mp["m15"]) == "start", "a document of another window reads start")
    ok(doc_problem(dict(d15, closed=False), t, mp["m15"]) == "open", "an open document")
    ok(doc_problem(dict(d15, outcomePrices='["0.5", "0.5"]'), t, mp["m15"]) == "unresolved", "unresolved")
    ok(doc_problem(dict(d15, feeSchedule=dict(FEE_SCHEDULE, rebateRate=D("0.25"))), t, mp["m15"]) == "fee",
       "another rebate rate reads fee")
    ok(doc_problem(dict(d15, clobTokenIds='["222", "111"]'), t, mp["m15"]) == "not the chain book's tokens",
       "tokens swapped against the chain book's read so")
    ok(doc_problem(dict(d15, events=[{"eventMetadata": {"priceToBeat": D("1")}}]), t, mp["m15"]) == "readings",
       "a document without finalPrice reads readings")
    ok(doc_problem(None, t, mp["m15"]) == "absent", "no document reads absent")
    tie = synth_doc(slug15(t), t, mp["m15"], "78020.25", "78020.25", True)
    ok(identities(tie, d5)[1], "E2 at equality: Up")
    ok(not identities(synth_doc(slug15(t), t, mp["m15"], "78000.5", "78020.250", True), d5)[0],
       "E1 compares literals: 78020.250 is not 78020.25")
    ok(not identities(dict(d15, outcomePrices='["0", "1"]'), d5)[1], "E2 fails on the wrong outcome")
    # line_check is total on what a stored line can hold
    good_raw = synth_reply("111", mp["m15"]["condition"], [("0.48", "10")], [("0.52", "10")], t * 1000)
    line = {"T": t, "tau_prime": 245, "market": "m15", "slug": slug15(t), "token_id": "111",
            "outcome_label": "Up", "url": "u", "status": 200, "send_mono_ns": 1, "recv_mono_ns": 2,
            "recv_wall_ns": 3, "bytes": len(good_raw.encode()), "sha256": sha256_bytes(good_raw.encode()),
            "raw": good_raw, "reason": None}
    member = {"T": t, "map": mp}
    ok(line_check(line, t, member)[0] is None, "a stored line as the chain book writes it reads valid")
    ok(line_check(dict(line, raw="\ud800"), t, member)[0] == "raw", "a body that is not UTF-8 text reads raw")
    ok(line_check(dict(line, raw="{", bytes=1, sha256=sha256_bytes(b"{")), t, member)[0] == "body",
       "a body that does not parse reads body")
    ok(line_check(dict(line, token_id=["111"]), t, member)[0] == "token", "a token that is not text reads token")
    ok(line_check(dict(line, outcome_label="Down"), t, member)[0] == "token", "a label against the map reads token")
    ok(line_check(dict(line, status=403), t, member)[0] == "status", "a refused read reads status")
    ok(line_check({"T": t}, t, member)[0] == "keys", "a line without the chain book's keys reads keys")
    ok(venue_ms({"timestamp": "\u00b2"}) is None and venue_ms({"timestamp": "1790184600123"}) == 1790184600123,
       "a book time is a run of ASCII digits or nothing")
    # a synthetic chain book end to end: the set, the constants, the score, twice
    tmp = os.path.join(WORK, "selftest-tmp")
    shutil.rmtree(tmp, ignore_errors=True)
    try:
        root = os.path.join(tmp, "chainbook")
        ts = [FIRST_T + WINDOW * k for k in range(10)]
        maps, docs = {}, {}
        plan = {  # T index: (R0, R600, R900, books)
            0: ("78000.5", "78010.25", "78005",
                {(35, "m15", "Up"): ([("0.94", "50")], [("0.95", "50")], "0.01", 0, 0),
                 (35, "m5", "Down"): ([("0.03", "20")], [("0.04", "20")], "0.01", 0, 0)}),
            1: ("78000.5", "77990.75", "77995", {}),
            2: ("78000.5", "78010.25", "78020",
                {(65, "m15", "Up"): ([("0.470", "9")], [("0.480", "9")], "0.001", 0, 0),
                 (65, "m5", "Down"): ([("0.484", "9")], [("0.485", "9")], "0.001", 0, 0)}),
            3: ("78000.5", "77990.75", "78001",
                {(15, "m5", "Up"): ([("0.96", "7")], [("0.97", "7")], "0.01", 0, 0),
                 (15, "m15", "Down"): ([("0.01", "8")], [("0.02", "8")], "0.01", 400, 0)}),
            4: ("78000.5", "78010.25", "77999",
                {(245, "m15", "Up"): ([("0.48", "100")], [("0.52", "4")], "0.01", 0, 0)}),
            5: ("78000.5", "78000.5", "78001",
                {(95, "m15", "Up"): ([("0.94", "50")], [("0.95", "50")], "0.01", 0, 0),
                 (95, "m5", "Down"): ([("0.03", "20")], [("0.04", "20")], "0.01", 0, 300)}),
            6: ("78000.5", "78010.25", "78005", {}),
            8: ("78000.5", "78010.25", "78005", {}),
            9: ("78000.5", "78010.25", "78005", {}),
        }
        for k, t in enumerate(ts):
            maps[t] = {"m15": {"Up": str(1000 + 4 * k), "Down": str(1001 + 4 * k),
                               "condition": "0x%064x" % (2 * k + 1)},
                       "m5": {"Up": str(1002 + 4 * k), "Down": str(1003 + 4 * k),
                              "condition": "0x%064x" % (2 * k + 2)}}
            if k == 7:
                continue                      # no directory
            r0, r600, r900, books = plan[k]
            synth_window(root, t, maps[t], books, complete=6 if k == 6 else 7)
            up15, up5 = D(r900) >= D(r0), D(r900) >= D(r600)
            docs[slug15(t)] = synth_doc(slug15(t), t, maps[t]["m15"], r0, r900, up15,
                                        fee=dict(FEE_SCHEDULE, rate=D("0.08")) if k == 9 else None)
            docs[slug5(t + 600)] = synth_doc(slug5(t + 600), t + 600, maps[t]["m5"], r600,
                                             "78005.5" if k == 8 else r900, up5)
        # window 4: one stored line whose hash is not its body's
        p = os.path.join(root, str(ts[4]), "books.jsonl.gz")
        with gzip.open(p, "rb") as fh:
            lines = fh.read().decode().split("\n")
        hit = [i for i, ln in enumerate(lines) if '"tau_prime":125' in ln and '"market":"m5"' in ln][0]
        rec = json.loads(lines[hit])
        rec["sha256"] = "0" * 64
        lines[hit] = json.dumps(rec, sort_keys=True, separators=(",", ":"))
        with open(p, "wb") as fh:
            fh.write(gz_bytes("\n".join(lines).encode()))
        asked = []

        def fake_docs(_dir, slugs):
            asked.append(list(slugs))
            return {s: docs[s] for s in slugs if s in docs}
        base = os.path.join(tmp, "set")
        s = form_set(base, root, ts, fake_docs)
        st = dict(s["considered"])
        ok([st[t] for t in ts] == ["member"] * 6 + ["incomplete", "no directory", "E1", "15m document: fee"],
           "ten windows: six members, and four non-members with their reasons")
        ok([len(a) for a in asked] == [16], "eight windows' documents in one request of sixteen slugs")
        c, cpath, csha = build_constants(base, s, "t")
        ok(c["members"] == 6 and c["pairs"] == {"A": 3, "B": 2, "AB": 1} and not c["none_possible"],
           "constants: six members, pairs A 3, B 2, AB 1; NONE impossible below 528")
        BOOKS_OPEN[0] = True
        res = score(base, root, s, c, "t")
        ok(res["v_firm"] == 1 and res["v_any"] == 4 and res["reading"] == "VIOLATION",
           "V_firm 1 and V_any 4: VIOLATION")
        ok(res["n_clean"] == 5 and not res["none_possible"], "five clean members: the sixth has an invalid unit")
        ok(res["rows"] == 49 and res["invalid"] == {"hash": 1}, "49 rows, one invalid unit, by its hash")
        ok(res["classes"] == {"firm": 1, "loose": 3, "none": 43, "unquoted": 1},
           "classes: firm 1, loose 3, none 43, unquoted 1")
        ok(res["loose_by"] == {"convention": 1, "apart": 2, "no time": 0},
           "loose: convention 1, apart 2 - received 400 ms apart, and books 300 ms apart by their own clocks")
        ok(abs(res["firm_profit_at_touch"] -
               (1 - D("0.99621832502954164619048315760392936168528098774527312144822")) * 20) < D("1e-48"),
           "the firm unit's profit at the touch: its margin, 0.0037816749..., times 20 shares")
        ok(res["pre_fee_inversions"] == 4, "four rows whose asks sum below 1 before any fee")
        with open(cpath, "rb") as fh:
            const0 = fh.read()
        res2 = score(base, root, s, c, "t")
        ok(res2 == res, "a second score writes and returns the same")
        # the constants ignore every book; the score does not (negative control)
        p0 = os.path.join(root, str(ts[0]), "books.jsonl.gz")
        synth_window(root, ts[0], maps[ts[0]],
                     {(35, "m15", "Up"): ([("0.94", "50")], [("0.96", "50")], "0.01", 0, 0),
                      (35, "m5", "Down"): ([("0.03", "20")], [("0.04", "20")], "0.01", 0, 0)})
        base2 = os.path.join(tmp, "set2")
        os.makedirs(base2)
        shutil.copy(os.path.join(base, "set.json"), os.path.join(base2, "set.json"))
        c2, cpath2, _h = build_constants(base2, s, "t")
        with open(cpath2, "rb") as fh:
            ok(fh.read() == const0, "the constants file is byte-identical with a book changed")
        res3 = score(base2, root, s, c2, "t")
        ok(res3["v_firm"] == 0 and res3["v_any"] == 3 and res3["reading"] == "UNDECIDABLE",
           "the score moves when the book moves: 0.96 + 0.04 is no violation")
        ok(os.path.exists(p0), "the synthetic book stands")
        BOOKS_OPEN[0] = False
    finally:
        BOOKS_OPEN[0] = False
        shutil.rmtree(tmp, ignore_errors=True)
    # deterministic gzip and JSON
    ok(gz_bytes(b"abc\n") == gz_bytes(b"abc\n"), "gzip is deterministic")
    ok(dumps({"b": D("0.10"), "a": 1}) == '{"a":1,"b":"0.10"}\n', "JSON is sorted with Decimals as text")
    ok(fx(D("1E-7")) == "0.0000001", "no exponent form")
    ok(len(t14.CAPTURE_OPENS) == 0, "tz14's own hook recorded no open under the recorder's root")
    out("%d of %d checks passed" % (n[0], n[0]))


def main(argv):
    if not argv:
        sys.exit("usage: tz24-nesting-b2.py MODE [ARG...]")
    mode, rest = argv[0], argv[1:]
    table = {"fingerprint": mode_fingerprint, "selftest": mode_selftest, "still": mode_still,
             "rehearse": mode_rehearse, "fetch": mode_fetch, "constants": mode_constants,
             "score": mode_score}
    if mode == "reclaim":
        mode_reclaim(rest)
    elif mode == "scratch":
        assert len(rest) == 1, "scratch OWN"
        mode_scratch(rest[0])
    else:
        assert mode in table and not rest, "unknown mode %r" % (argv,)
        table[mode]()
    out("malloc tuned: %s" % MALLOC_TUNED)
    out("peak memory of this run: %d bytes" % (
        resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024))
    out("opens refused under the capture roots: %d; chain book opens: window.json %d, books.jsonl.gz %d; "
        "tz14's record of opens under the recorder's root: %s" % (
            len(REFUSED), CB_OPENS["window.json"], CB_OPENS["books.jsonl.gz"],
            len(_TZ14[0].CAPTURE_OPENS) if _TZ14 else "not loaded"))


if __name__ == "__main__":
    main(sys.argv[1:])
```
