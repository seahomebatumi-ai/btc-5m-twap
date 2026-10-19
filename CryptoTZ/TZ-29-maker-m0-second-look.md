# TZ-29 — M0's second look: do the makers earn, over both looks?

**Canonical filename:** `TZ-29-maker-m0-second-look.md`. The committed file takes this name and no other.

**Executor model: Opus.** Reads of the venue over the network, a gate's arithmetic over two looks, and the first
label read of a set no one has scored.

**Required System Map revision:** `2026-10-19-a`.

**Required anchors**, from map §0. A mismatch on any one is BLOCKED before any work:

| anchor | required |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `0f6c90451cbd` |
| `A6` — pricer | `729f0bcdbee3` |

**Host gate:** §0.3. This TZ runs on the capture host for its interpreter, its network and the forensic store, and
reads nothing of any capture.

**When:** §3.7 and everything after it **no earlier than 2026-10-20 00:15:00 UTC**, epoch `1792455300`: §3.7's first
command waits for that instant in its own text, and `fetch` asserts it. If every candidate qualifies, the set's last
member opens at 23:10 UTC on 2026-10-19, and TZ-23's walk stops before any market younger than `3,900` s (§1).
Everything before §3.7 may run earlier. About two hours of wall clock (§6), most of it the fetch held to the pair
book's idle stretch.

**What this TZ is.** The maker track's M0, read a second time, as TZ-23 fixed it. TZ-23's first look, 4,032 markets,
read UNDECIDABLE: the makers kept `0.211` c a share on their fills inside `[T0, T0 + 240)`, `0.224` c of it rebate.
This TZ extends TZ-23's sum over the next 4,032 qualifying markets after its last member and reads M0 once, on the
sum over both looks — `S`, `V` and `Sh` over 8,064 members, TZ-23's `α`, `λ` and `δ` — by TZ-23's own table:
**EARN**, **NO EARN** or **UNDECIDABLE**, each answer's false-reading probability at most `0.005` over both looks
together. Every sum, threshold and reading is TZ-23's own function, loaded byte for byte; this TZ's instrument,
`research/tz29-maker-m0-second-look.py` (Appendix A), adds the second set, the first look from the forensic store,
the sum of the two, and a fetch held to the pair book's idle stretch.

---

## 0. Gates

### 0.0 The work tree, first

After contract §1 steps 1 and 2, and before anything else:

```
mkdir /root/tz29-work /root/tz29-work/logs; echo "exit=$?"
```

`exit=0` proves neither existed; anything else is BLOCKED. **From here every command's output goes to
`/root/tz29-work/logs/`, one file per step, §0's included**, and nothing to the session's scratchpad. The one
exception is B-RECLAIM-OWN, §9.

### 0.1 The instrument, staged

Extract Appendix A from this TZ as the primary checkout carries it after contract §1's pull, with this script,
verbatim, its one argument the destination:

```
/root/tz04a-env/venv/bin/python -B - /root/tz29-work/stage <<'EOF'
import hashlib, os, sys
SRC = "/root/btc-5m-twap/CryptoTZ/TZ-29-maker-m0-second-look.md"
DEST = sys.argv[1]
WANT = {
    "research/tz29-maker-m0-second-look.py": "18defff93d08c13ea4638a518c88a3fec5541fcf53fb6827451e727f2204d905",
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
| `research/tz29-maker-m0-second-look.py` | 1,225 | 68,959 | `18defff93d08c13ea4638a518c88a3fec5541fcf53fb6827451e727f2204d905` |

Then the instrument's one dependency beside it, TZ-23's file as `main` carries it:

```
install -m 0644 /root/btc-5m-twap/research/tz23-maker-m0.py /root/tz29-work/stage/research/; echo "exit=$?"
sha256sum /root/tz29-work/stage/research/tz23-maker-m0.py
```

which must print `6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f` — map §0's row; the instrument
asserts it again each time it loads the file (Appendix A lines 58 to 72). A failed assert or another hash is
BLOCKED. The staged copy runs §0.2's `fingerprint` alone, written **`I0`**: `nice -n 19
/root/tz04a-env/venv/bin/python -B /root/tz29-work/stage/research/tz29-maker-m0-second-look.py`, run from
`/root/tz29-work` — every mode asserts that its current directory is the work tree (line 1205).

### 0.2 Fingerprint

`I0 fingerprint` performs contract §1 steps 3 and 4 inside the instrument and asserts them, against `SYSTEM-MAP.md`
and the files of its §0 table in the primary checkout `/root/btc-5m-twap`: revision `2026-10-19-a`; the six anchors;
`A2`, `A4`, `A5` and `A6` re-derived as the first 12 hex characters of those files' SHA-256; the table's **40** rows,
each printed in lines, bytes and SHA-256 — **37** `frozen` rows asserted equal to the map, **2** `tracked` and **1**
`reported`; and the map's own lines, bytes and SHA-256 (lines 492 to 519). It prints `FINGERPRINT PASS` or stops at
the first mismatch, which is BLOCKED.

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
cd /root/btc-forensics && stat -c '%s %n' tz23-work--set--set.json tz23-work--set--tz23-fills.jsonl.gz tz23-work--set--tz23-members.csv tz23-work--set--tz23-constants.json tz23-work--set--tz23-scored.csv tz23-work--set--tz23-reading.json && sha256sum tz23-work--set--set.json tz23-work--set--tz23-fills.jsonl.gz tz23-work--set--tz23-members.csv tz23-work--set--tz23-constants.json tz23-work--set--tz23-scored.csv tz23-work--set--tz23-reading.json; cd /root/btc-5m-twap
TZ=UTC systemctl show btc-recorder.service btc-pairbook.service btc-pairbook-archive.service btc-pairbook-archive.timer btc-chainbook.service -p Id -p MainPID -p NRestarts -p ActiveState -p SubState -p UnitFileState -p ActiveEnterTimestamp -p Result
TZ=UTC systemctl list-timers btc-pairbook-archive.timer --all --no-pager
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
systemctl is-active telemetry-watch.service; echo "exit=$?"
git -C /root/btc-recorder-svc rev-parse HEAD
cat /root/btc-pairbook-svc/commit.txt /root/btc-pairbook-archive-svc/commit.txt
for d in /root/tz28-work /root/tz18a-svc /root/btc-recorder-svc /root/btc-pairbook-svc /root/btc-pairbook-archive-svc /var/lib/btc-pairbook-archive; do test -e "$d"; echo "$d exit=$?"; done
find /root/btc-forensics -type f | wc -l
git worktree list
du -sb /var/lib/btc-pairbook /var/lib/btc-pairbook-archive /root/.claude /root/PROJECT_GAMING_PS5
echo "$S"; ls -la "$(dirname "$(dirname "$S")")"
```

- **H1** — `find` prints exactly one path.
- **H2** — `df` names source `/dev/vda2` and size `31612203008`; `grep -c` prints at least `1`. With H1 this is map
  §6's host identity.
- **H3** — the interpreter prints `3.12.`.
- **H4** — the first look in the forensic store: `stat` and `sha256sum` print, for the six files, the sizes and hashes
  of §1's table — TZ-23's, copied there by its §9 (its report §2.14).
- **Memory gate** — `MemAvailable` at least `177,135,616` bytes (§0.4).
- **Disk gate** — `avail` at least `4,800,000,000` bytes (§0.4).

Any of these six failing is BLOCKED. **The rest is printed and carries no threshold:** the boots, against which §3.4
reads the archive's two runs off its calendar, on 2026-10-15 06:18:30 and 2026-10-17 08:35:37 UTC (map §6); the five
units — this TZ needs none of them, G-STILL reads the recorder and the pair book (§4.5), and §1's hold reads the
archive's service; `telemetry-watch.service`'s two states, on which map §6's headroom is conditional; the three code
trees' commits, `e3975b5…`, `e8b46a8…` and `d8194fd…` by map §3; `/root/tz28-work` absent and the code and state
trees present, by map §3; the forensic store's count, map §3's `1,846`; the worktrees, map §3's two; `du` of the pair
book's store beside `df`, as map §2.5 asks, and of the archive's state; and the listing of the directory that holds
the session's own, whose UUID directories `I scratch` names live or earlier (§9).

### 0.4 Resource floors, in exact bytes

**Disk.** `/dev/vda2` free at least **`4,800,000,000`** bytes: the pair book's `STREAM_FLOOR`, `4,500,000,000`
(`research/tz26-nesting-b3-capture.py` line 132), below which no stream opens for a window, plus `300,000,000` for this
session — so nothing this TZ writes can stop B3's capture. The session's peak is its tree and §9's copies of it in the
forensic store together: `143,149,706` bytes in the Architect's dress rehearsal of 2026-10-19 on a stand-in second
look of the first look's size — the tree `94,181,997` at its largest, the copies `48,967,709` — and the allowance is
that twice over, rounded up, since the tree's fills and chunk cache grow with the second look's fills (map §6, disk).

**Memory.** `MemAvailable` at least **`177,135,616`** bytes: twice the largest peak of any mode in the Architect's runs
of Appendix A under Python 3.12.3 at the population's size (map §7 item 97's rule) — `constants`' `88,567,808`, the
larger of its two runs over a stand-in second look of 4,032 markets; `fetch` peaked at `77,385,728` over the first
look's 4,032 and `score` at `74,252,288` over 8,064 (map §6, memory). Every mode that reads the venue
or a set — `rehearse`, `replay`, `fetch`, `constants` and `score` — re-reads `MemAvailable` at its start and stops
BLOCKED below the floor, and asserts that glibc took TZ-23's mmap threshold and arena count (lines 233 to 238). Map §6
records the host: `1,002,127,360` bytes in all, one processor; TZ-28 read `259` to `305` MB available with its
session open. Every mode runs under `nice -n 19`.

### 0.5 Refs

`git ls-remote origin` before §3.1's push, every ref reported. Map §1 records, read on 2026-10-19 at 09:36 UTC, `main`
at `f6ab6e5a7eab2b577ac2b541e85d7f99ba7872f5`, PR #27's merge, six branches, thirteen tags — `tz-01a-dataset` and
`tz-27-pairbook-streams`, annotated, and eleven lightweight `pairbook-streams-*` — and **49** ref lines; every later run
of the archive adds one tag — 50 after 2026-10-20 03:00:20 UTC, one more each day. The upload that carries revision
`2026-10-19-a` and this TZ sits above `f6ab6e5`, in one commit or more; every commit on `main`'s first-parent line above
it is reported with the paths it changed. A difference is recorded, not BLOCKING, unless `main` does not carry revision
`2026-10-19-a` or `refs/heads/tz-29-maker-m0-second-look` already exists — either is BLOCKED.

---

## 1. Why this TZ exists

Line numbers here are Appendix A's unless a file is named; `tz23` is `research/tz23-maker-m0.py` at `f6ab6e5`.

**The question** — CANON PART II, the maker track's M0: do makers in `btc-updown-5m` earn, at settlement and with the
20% rebate, on the fills inside `[T0, T0 + 240)`? **TZ-23 read it once and decided nothing** (map §4, §5):
`S` = `272,424.113` USDC on 4,032 members, `0.211` c a share — `−0.013` c at settlement and `+0.224` c of rebate —
between NO EARN's `0.165` c and EARN's `0.335` c.

**What TZ-23 fixed for this look** (TZ-23 §1, "A second look costs no error"): Ville's bound holds at every `n`, so a
later TZ may **extend the same sum** over the next qualifying markets after the first set's last member, with TZ-23's
`α = 0.005`, `λ = 0.000021932` and `δ = 0.005`, and each answer's false-reading probability over every look together
stays at most `0.005`. So `S`, `V` and `Sh` here are sums over both looks' 8,064 members in `T0` order, and the
thresholds are TZ-23's on them: **`thr = L/λ + λ V / 8`**, `L = ln(1/α)`; **EARN** at `S >= thr`; **NO EARN** at
`S <= δ · Sh − thr`; **UNDECIDABLE** otherwise. The second set is never read against thresholds of its own: that would
be a second test, which TZ-23's text does not fix.

**The test**, TZ-23's (its §1, "The test"), over the longer sequence. Order the members by `T0` and let `G_m` be
everything public at `T0_m + 240`. `X_m`, `C_m` and `R_m` are known at `G_m`, and `up_m`, fixed by the reading at
`T0_m + 300`, at `G_(m+1)`; so `D_m = X_m (up_m − q_m)` are martingale differences, each in an interval of length
`|X_m|`, across both looks as within one, and `exp(λ M_n − λ² V_n / 8)` is a supermartingale whose probability of ever
reaching `1/α` is at most `α`. The first look's 4,032 terms are its own terms, unchanged; the sum continues from its
last. **The bound assumes no independence between outcomes, no calibration and no distribution.**

**The set.** The first **4,032** qualifying markets with **`T0 > 1791241800`**, M0's first look's last member (CANON
PART II), walked by TZ-23's `candidates` from **`1791242100`**, 2026-10-05 23:15 UTC, in steps of 300 (lines 297 to 312;
tz23 lines 449 to 472), past TZ-23's three excluded spans, all of which end below it. A candidate qualifies by TZ-23's
`qualify`, unchanged (tz23 lines 375 to 395): served closed, `outcomes` `["Up", "Down"]`, `outcomePrices` one of the two
resolved forms, `feeSchedule` `{exponent 1, rate 0.07, takerOnly true, rebateRate 0.2}` and `feeType` `crypto_fees_v2`,
`eventStartTime` its own `T0`, a condition id of 64 hex digits and two token ids. **If every candidate qualifies**, the
set runs from `1791242100` to `1792451400`, 2026-10-19 23:10 UTC — 576 members on each day of the week, 1,152 of them on
a weekend — in 202 document requests, and its member list's SHA-256 is
`971258b48251a8c7e89c52919bd1801ad73725d98796f3481292d66d27136e5c`, recorded and asserted by nothing. The walk requests
no document after the 4,032nd member, and stops BLOCKED before it requests a market younger than `3,900` s or once it
has considered 6,048 candidates — the 4,032 and TZ-23's slack of 2,016 (tz23 lines 461 and 455); **a walk stopped
because a market is too recent is walked again 300 s later, at most 24 times** (lines 301 to 311), so a 4,032nd
member pushed past 23:10 UTC by up to 24 non-members waits rather than blocks — the first look had none in 4,032 — and
every other stop is final.

**The first look, from the forensic store.** TZ-23's §9 copied its outputs into `/root/btc-forensics/` (its report
§2.14). This TZ reads six of them and writes none, each asserted by its size and SHA-256 in TZ-23's report (lines
122 to 139):

| file in `/root/btc-forensics/` | bytes | SHA-256 | what it holds |
|---|---|---|---|
| `tz23-work--set--set.json` | 2,314,799 | `a04226f0ec324400fa493f8101b24becf2e0609e614e60aa11d6adeacae76303` | the 4,032 members' documents |
| `tz23-work--set--tz23-fills.jsonl.gz` | 36,870,673 | `4f20400e20913dec4bff8cd715f03934dc1bde0933214258414afd55cdf55a64` | their taker fills |
| `tz23-work--set--tz23-members.csv` | 2,444,450 | `cf269016781bca698eb0d707e5aea3ce5dfefc15d8a068b4deb85a03ec229a61` | every member's sums by band |
| `tz23-work--set--tz23-constants.json` | 2,114 | `1b28df4382ed926ad92d514cb9bbfd6764e15a90b3e4c39618115db5e30217d5` | `V`, `Sh`, the thresholds |
| `tz23-work--set--tz23-scored.csv` | 464,610 | `12002203479ac5634c509c4f4306b42159e74d10cf987839fad6ec7022bdb988` | every member's label and result |
| `tz23-work--set--tz23-reading.json` | 1,915 | `fdad516faaa3abfa7cc70134d19caa2be562d636235b464506a971893aef4043` | `S`, its parts, the reading |

**G-REPLAY** comes first: TZ-23's `score`, run again by this instrument on the store's set, members and constants
files, must write TZ-23's scored and reading files byte for byte, its `S`, its 2,023 Up outcomes and its UNDECIDABLE —
the store, TZ-23's functions and the host's interpreter are what read the first look (lines 383 to 431). **Then the sum
over both looks is TZ-23's own** (lines 436 to 487): the cumulative members file is the first look's 4,032 rows of
TZ-23's members file, then the second look's 4,032 rows of TZ-23's `build_constants` over the second set, under the
one header both carry; `V` and `Sh` are the two constants files' sums added, exact at 60 digits; the thresholds and the
power are TZ-23's `gate_constants` on them; and the reading is TZ-23's `score` over the cumulative members file and
both looks' documents (tz23 lines 572 to 614, 410 to 423 and 642 to 699). **The self-test proves the cumulative
members file byte for byte, and `V`, `Sh` and every threshold digit for digit, equal to TZ-23's `build_constants` over
the union of two looks it builds, and the score over them equal to TZ-23's `score` over that union** (lines
1019 to 1093). No second implementation of any sum, threshold or reading exists in this instrument.

**The venue, re-read by the Architect on 2026-10-19** (map §7 item 87's rule; CANON §1.1). The changelog's newest entry
is of 2026-10-07: nothing since TZ-23's re-read of 2026-10-09 touches the fee, the maker rebate, the taker delay, Gamma
`/markets` or `/v2/trades`, and that entry changes `/v2/trades` only for requests that carry `user`, which no request
here does. The fee page gives the Crypto taker fee `C × 0.07 × p × (1 − p)`, makers none, a 20% maker rebate; the rebate
page gives 20% of a market's taker fees, fee-curve weighted, paid daily in pUSD, a 1 pUSD minimum; the taker delay is
the 150 ms of 2026-09-04 14:00 UTC. `/v1` trades retire on 2026-10-24; TZ-23 reads `/v2` alone. A fee change on the
venue would make the second set's documents fail `qualify` and stop the walk BLOCKED at its slack.

**The path, proved on the venue the same day.** The Architect ran TZ-23's own `rehearse` against the venue on
2026-10-19 under Python 3.12.3: its 10 figures equal TZ-23's `REF` and **its six files hash equal to TZ-23's**
(TZ-23's report §2.5 and §2.13). **Then TZ-23's own `fetch`, `constants` and `score` over the first look's 4,032
markets: all six of §1's files came back byte for byte**, so the venue's record of the first look has not moved since
TZ-23 read it; and this instrument's held fetch of the same markets an hour later wrote the same set and the same 202
chunk files again, every chunk inside the idle stretch. **G-REHEARSAL** repeats the rehearsal through this
instrument, held as the fetch is, and reads all sixteen (lines 663 to 690). **The whole run, rehearsed:** the
Architect ran §0.1 to §9 in a copy of the host's layout — the forensic store's six files from that re-fetch, a ledger
shaped as TZ-28's, stand-in units — on a stand-in second look built from the first look's own files, every `T0` moved
to the second look's and every row with it, so no member of the second set was read and the stand-in's reading is no
datum; every gate passed, and §0.4 and §6 are that run's measurements.

**Every request inside the pair book's idle stretch, and none near or during the archive's run.** TZ-23's fetch ran
1,565 s beside the chain book's REST reads. Since 2026-10-10 the pair book streams the four books of each nested pair
from `T+595` to `T+905` of every 900 s window, and B3's measurement reads every window's segments (map §2.5, §7 items
109 and 113); since 2026-10-11 the archive's run starts at 03:00:20 UTC and moves the streams over the same link
(map §6). So **every walk and every chunk of fills starts only at seconds 15 to 470 of a window** — a request budgeted
at `120` s, about twice the slowest chunk the Architect's fetch of 2026-10-19 took, ends by second 590 — **never from
02:57:20 to 03:01:20 UTC, and never while `btc-pairbook-archive.service` reads `active`, `activating`,
`deactivating`, `reloading` or `refreshing`** (lines 264 to 294). A hold longer than `7,200` s is BLOCKED. Each chunk's
start and end go to a timing file, and every chunk that ended after second 590 is listed, so B3's measurement can set
its windows beside them. The chunks are TZ-23's `fetch_chunk`'s, unchanged (tz23 lines 479 to 492); the loop that
holds them is this instrument's (lines 315 to 358), and its fail-fast projects the chunks' own fetching time — the
holds excluded — after the first 30, BLOCKED above `7,200` s, TZ-23's bound, and cancels every chunk not yet started.

**Power**, before any label and deciding nothing: TZ-23's normal approximation at the largest variance the outcomes
allow, `V/4`, `Φ((δ · Sh − thr) / (sqrt(V) / 2))`. At the first look's per-member rates over both looks — `V` and `Sh`
twice TZ-23's — `thr / Sh` is `0.2412` c a share and NO EARN's bound `0.2588` c, so **`2 thr / Sh` = `0.482` c is
under `δ`, and UNDECIDABLE cannot occur**; the power is `0.99983`. UNDECIDABLE needs the second look's `V` above
`1.119` times the first's at an equal `Sh` — the Architect's computation at 80 digits, independent of the instrument.
`constants` prints the power and whether UNDECIDABLE can occur before any label is read (lines 470 to 487).

**What this TZ decides.**

1. **The instrument**, `research/tz29-maker-m0-second-look.py`, on the branch `tz-29-maker-m0-second-look`; `main`
   carries it once the Boss merges after the verdict.
2. **The second set, formed and fetched; both looks' constants, label-free, on disk with their SHA-256 in
   `state.json`; the instrument's commit on `origin`** — and only then the labels, read once a run.
3. **M0's reading, over both looks.** EARN is CANON PART II's M0 PASS: M1 may be written. NO EARN closes the maker
   track for this window (TZ-23 §1 item 3). UNDECIDABLE leaves M0 open, and a later TZ may extend the same sum again at
   the same constants. Where both bounds hold the reading is EARN, and half a tick a share is rejected too (TZ-23 §4.3).
4. **The archive's record**, read from its own ledger and printed, for the map and for B3 (§3.4).
5. **Nothing on the host is touched** but this TZ's tree, the forensic store by exclusive create, and the directories
   earlier sessions left (§9).

**Data hygiene.** **No member of the second set has been read by anyone**: no TZ reads a five-minute market with
`T0 > 1791241800` before this one (CANON PART II); the pair book's store, whose five-minute legs are these markets, is
reserved on the host and in every Release made from it, and its streams have been hashed and moved, never
decompressed (map §2.5). The Architect's reads for this TZ, on 2026-10-19: TZ-23's rehearsal span and the first look's
4,032 markets, documents and fills, through TZ-23's own instrument and once more through this one's walk and held
fetch — both spans scored by TZ-23 already; the venue's changelog, fee and rebate pages; and one request to
`/v2/trades` with `limit=1` and no condition, written to `/dev/null` and never read. §2 bars any read of a member
outside the instrument.

---

## 2. Scope

**Repository paths this TZ may write, and no others:**

1. `research/tz29-maker-m0-second-look.py` — new, byte for byte Appendix A's, on branch `tz-29-maker-m0-second-look`,
   then a pull request. Not merged by the Executor.
2. `CryptoReports/TZ-29-maker-m0-second-look-report.md` — straight to `main`, in one commit. **The one path pushed to
   `main`, and the exemption to item 7 below.**

**Host paths this TZ may write:** `/root/tz29-work/**`; `/root/btc-forensics/`, by exclusive create only (§9); and in
the primary checkout `/root/btc-5m-twap`, its `.git` for the branch and the worktree, and its `CryptoReports/` for the
report. **Host paths it removes, under §9 and nothing else:** `/root/tz29-work/` with its worktree, and the directories
`I scratch` names earlier.

**Prohibited, each absolutely:**

1. No committed file is modified; every `frozen` row of map §0 is byte-identical at run end.
2. **Nothing under `/var/lib/btc-recorder/` or `/var/lib/btc-chainbook/` is opened, listed or written** — TZ-23's audit
   hook refuses every open there and this instrument's every open and listing (lines 184 to 215); only §0.3's `df`,
   `find` and `grep -c`, at both of its runs, and B-RECLAIM-OWN's `df` touch the recorder's root.
3. **Nothing under `/var/lib/btc-pairbook/` is opened, listed or written** — the hook refuses both; only `du -sb` at
   §0.3, at both of its runs, reads the store's size. **No price, size, side, book hash or outcome is extracted from a
   body stored there or from any Release asset made from it** (CANON PART II, B3's reserve; map §2.5).
4. **Under `/var/lib/btc-pairbook-archive/` nothing is written; `ledger.jsonl` is opened for reading by `I archive`
   alone — the named exemption — and nothing else there is opened or listed** but by `du -sb` at §0.3. The ledger's
   records carry events, counts, times, ids, tags and hashes and no price: TZ-28's run asserts each against TZ-27's
   forbidden keys before writing it (`research/tz28-pairbook-archive-timer.py` lines 212 to 220).
5. **No unit is signalled, started, stopped, enabled, disabled or changed.** `systemctl show`, `is-active`,
   `is-enabled`, `list-timers` and `journalctl --list-boots` are this TZ's only reads of a unit.
6. `/root/tz04a-env/`, `/root/tz01-env/`, `/root/tz18a-svc/`, `/root/btc-recorder-svc/`, `/root/btc-pairbook-svc/` and
   `/root/btc-pairbook-archive-svc/` are not modified; `/root/btc-forensics/` only by §9's exclusive create, and the
   first look's six files there are read and never written.
7. Nothing is pushed to `main` except the report of item 2.
8. **No label of the second set is read before §3.8's cumulative constants are on disk with their SHA-256 in
   `state.json` and the instrument's commit is on `origin`.** A label is the outcome a member's `outcomePrices` states.
   Four exemptions, each named because the body requires it: (a) `qualify`, which asks only whether `outcomePrices` is
   one of the two resolved forms, and `fetch` and `constants`, which carry each member's document in `set.json`,
   `outcomePrices` with it, and never interpret it — the self-test asserts the cumulative constants file byte-identical
   with every label of both looks flipped; (b) `rehearse`, which reads the labels of TZ-23's excluded rehearsal span;
   (c) `replay`, which reads the first look's labels, read by TZ-23 and held in its scored file; (d) `score`, which
   reads both looks' labels once a run, its determinism run included, each run a line in the ledger.
9. **Requests:** `gamma-api.polymarket.com/markets` and `data-api.polymarket.com/v2/trades`, through TZ-23's `http_json`
   and its two headers, `User-Agent: btc-5m-twap-m0/TZ-23` and `Accept: application/json` (tz23 lines 81, 82 and 233 to
   253), each walk and chunk held by §1's rule; `git` against `origin`, `I archive`'s `git ls-remote` among them; and
   `gh` for the pull request alone. No other request — no CLOB, no websocket, no GitHub API, no authenticated call —
   and **no read of any member's document or fills by any command but the instrument's modes**, `set.json` and the
   cache included.
10. **No single fill's, member's or market's price, size or outcome is printed or written outside `/root/tz29-work/`**:
    the instrument prints sums over a set, and the report quotes them. The one exemption is §9's byte-for-byte copies
    into `/root/btc-forensics/` of the files the report names by hash.
11. No Release is created, and no dataset, archive or binary enters git history.

---

## 3. The work, in this order

From §3.1 on, `nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz29-work/wt/research/tz29-maker-m0-second-look.py`
is written **`I`**; a mode is `I <mode>`, run from `/root/tz29-work`. Every command's output goes to `logs/`, one file
per step, and is quoted in the report. **§9's B-RECLAIM-SCRATCH runs after §3.3 and before §3.4; B-RECLAIM-OWN runs
last, after §3.11.** On a BLOCK before §3.1, B-RECLAIM-OWN runs with `I0` in place of `I` and without its `git worktree
remove` line; on a BLOCK or a FAIL after it, the run goes to §3.11 and §9, skipping every step that needs a PASS it
lacks.

**Where the session's permission classifier refuses a command of a block named B-…**, the Executor prints the block,
the Boss runs it verbatim in a root shell on the VPS, and the Executor verifies it through the reads this TZ names —
never from the Boss's account.

### 3.1 The branch and its file

```
git -C /root/btc-5m-twap fetch origin
git -C /root/btc-5m-twap worktree add -b tz-29-maker-m0-second-look /root/tz29-work/wt origin/main
```

Then §0.1's script again, verbatim but for its argument, `/root/tz29-work/wt`; it must print the same line as at §0.1.
`sha256sum /root/tz29-work/wt/research/tz23-maker-m0.py` must print `6b3ace2c…`: `main` carries TZ-23's file. Commit the
one file alone on the branch, push it with `git push -u origin tz-29-maker-m0-second-look` from the worktree, then
`date -u +%FT%T.%NZ; git ls-remote origin refs/heads/tz-29-maker-m0-second-look` — the instant the commit is on
`origin`, and its hash there — and open the pull request against `main`. A failed assert here is BLOCKED. **The push is
what lets §3.9 read a label:** `score` refuses a `HEAD` that `origin` does not carry (lines 751 to 753).

### 3.2 The self-test

`I selftest` must print `51 of 51 checks passed`. It reaches no network and runs on literals and on temporary
trees under `/root/tz29-work/selftest-tmp/`, which it removes (lines 864 to 1198). A red self-test stops the run here,
and it goes to §3.11 and §9.

### 3.3 The units, and the directories beside this session

`I still` records the recorder's and the pair book's `MainPID`, `NRestarts` and `ActiveState` in `state.json` and
prints their `MemoryCurrent` and `MemoryPeak` and the archive's two units' states. Then `I scratch "$(dirname "$S")"`
lists every UUID directory beside this session's own and names each **live** — born from 1 s before to 60 s after the
start of a running process whose `argv[0]` is `claude` or ends in `/claude.exe` — or **earlier**.

### 3.4 The archive's record

`I archive`: the archive's two units by `systemctl show`; `ledger.jsonl` read whole, its size and SHA-256, every
complete record printed with its UTC stamp; every run summarized — its start on the calendar or off it, its events, its
set, Release, removal, restart, resume and terminal record; the tags `origin` carries beside the ledger's sets; and
whether the archive is halted (lines 583 to 660). **Printed facts, no threshold:** its exit is recorded and gates
nothing. The report sets each run off the calendar beside §0.3's boots.

### 3.5 G-REHEARSAL

`I rehearse`: the whole path — the walk, the fetch held to the idle stretch, the constants and the score — over TZ-23's
144 excluded markets of 2026-10-03/04, against TZ-23's figures and files (§4.1). A FAIL stops the run here, and it goes
to §3.11 and §9.

### 3.6 G-REPLAY

`I replay`: the first look from the store, scored again (§4.2). A FAIL stops the run here, and it goes to §3.11 and §9.

### 3.7 The instant, then the set — G-SET

First, in its own text, the instant:

```
t=$(date -u +%s); while [ "$t" -lt 1792455300 ]; do sleep 30; t=$(date -u +%s); done; echo "instant reached: $t $(date -u)"
```

Run it in the background where the instant is more than five minutes away, and go on only once it prints. Then
`I fetch`, in the background, its output to `logs/`, read until it prints `G-SET PASS` or fails (§4.3). Its walk starts
inside the idle stretch; its chunks are held; after its first 30 fresh chunks it projects its own fetching time and
stops BLOCKED above `7,200` s. **A network failure is resumable:** the cache keeps every finished chunk, and `I fetch`
may be run again twice, 600 s apart; a third failure is BLOCKED.

### 3.8 The constants, twice

`I constants`, then `I constants` again. The second run must print `unchanged` for **five** files —
`tz29-fills.jsonl.gz`, `tz29-members.csv` and `tz29-constants.json`, the second look's, and `cumulative-members.csv` and
`cumulative-constants.json`, both looks' — contract §6's determinism. The cumulative constants file's SHA-256 is in
`state.json`.

### 3.9 The score, twice

`I score`, then `I score` again. The first reads the labels and prints the reading over both looks; the second must
print `unchanged` for `cumulative-scored.csv` and `cumulative-reading.json`. The ledger then holds two lines.

### 3.10 The units again — G-STILL

`I still`.

### 3.11 The closing reads

§0.3's block again, `I archive` again, then:

```
TZ=UTC systemctl show btc-recorder.service btc-pairbook.service btc-pairbook-archive.service -p MainPID -p NRestarts -p ActiveState -p MemoryCurrent -p MemoryPeak
free -b
du -sb /root/tz29-work /root/.claude
cat /root/tz29-work/state.json /root/tz29-work/label-ledger.jsonl
```

---

## 4. The gates — fixed here, before any of their data exists

| gate | population | PASS | false failure | power, against |
|---|---|---|---|---|
| **G-REHEARSAL** | TZ-23's 144 markets `1791050100` … `1791093000` | §4.1's 16 checks equal, exactly | `0` — one public record read again, equal to TZ-23's on 2026-10-19 | `1`, any change in the record, the fetch, a sign, the window, the rebate or a sum |
| **G-REPLAY** | the first look in the forensic store | §4.2's 6 files and 5 checks | `0` — the store against TZ-23's report | `1`, a byte changed in the store, a function or an interpreter that sums otherwise |
| **G-SET** | the walk from `1791242100` and the fetch of its members | 4,032 members, every chunk read back | `0` | — |
| **M0** | both looks' 8,064 members' fills inside the window | §4.4 | at most `0.005` for each answer, over both looks together | TZ-23's normal approximation, printed before any label; `0.99983` projected |
| **G-STILL** | the recorder and the pair book, §3.3 to §3.10 | `MainPID`, `NRestarts` and `ActiveState` unchanged | `0` — systemd read directly | `1`, a restart or a stop |

### 4.1 G-REHEARSAL

Over the 144 markets: the window's fills `n`, shares, `X`, `C`, `R`, `V`, `Σ X · up`, `S`, the members and the Up
outcomes equal TZ-23's `REF`, the Architect's independent figures (tz23 lines 88 to 93; TZ-23 §4.1), as values; and the
six files the rehearsal writes hash equal to TZ-23's own (lines 141 to 146): `set.json` `83a53bd3…`,
`rehearsal-fills.jsonl.gz` `3ce50a85…`, `rehearsal-members.csv` `2676af1d…`, `rehearsal-constants.json` `9f521a23…`,
`rehearsal-scored.csv` `d31eb18f…` and `rehearsal-reading.json` `4cdf1a11…`. `rehearse` prints `G-REHEARSAL PASS: 16 of
16`. **A FAIL means the venue's record of a span TZ-23 already scored has changed since TZ-23 read it**, and the two
looks would not be one sum.

### 4.2 G-REPLAY

`replay` verifies the store's six files by size and SHA-256, asserts the first look's 4,032 members, first and last
`T0`, member list `699cab9a…`, `V` and `Sh` against TZ-23's report, copies the members file into the work tree, runs
TZ-23's `score` on the store's set and constants, and checks five things: the scored file `12002203…` and the reading
file `fdad516f…`, byte for byte; `S` = `272424.11263025802271516797439628522`; 2,023 Up; UNDECIDABLE (lines
383 to 431). The three copies are then removed. It prints `G-REPLAY PASS: 6 of 6 stored files equal, 5 of 5 checks`.

### 4.3 G-SET

`fetch` prints `G-SET PASS` when the walk from `1791242100` has formed 4,032 members, all above `1791241800`; every
chunk's feed has ended with no cursor; every row has belonged to its chunk's markets and carried its market's token for
its outcome (TZ-23's `trades`, tz23 lines 269 to 299); and every chunk reads back to its members in order. Every
non-member is listed with its reason by `constants`.

### 4.4 M0's reading, over both looks

| condition, on `S`, `V` and `Sh` over both looks | reading |
|---|---|
| `S >= thr` | **EARN** — whatever the power |
| `S <= δ · Sh − thr` | **NO EARN** — whatever the power |
| otherwise | **UNDECIDABLE** |

TZ-23 §4.3's table, applied by TZ-23's `reading` inside its `score` (tz23 lines 426 to 433 and 671 to 673). Where both
hold the reading is EARN, and the report states that half a tick is also rejected. **No row reads a power.** The report
prints `S`, its settlement and rebate parts, each per share, both margins, and, barred from every reading, the first
look's `S` — TZ-23's — and the second look's by difference, each per share, and the makers' result per share in each
band of the interval.

**What a reading establishes, and what it does not** (TZ-23 §4.3). EARN says that on these 8,064 markets the makers'
fills inside the window were priced in their favour, given what was public at each window's end, beyond what the
outcomes' noise explains; it says nothing about a quote of ours — its queue position, its share of the fills, the
adverse selection it would meet and the 150 ms delay are M1's (CANON PART II). NO EARN says the makers kept less than
half a tick a share there, rebate included. Neither says which look carried it: the second look alone is a diagnostic.

### 4.5 G-STILL

From §3.3 to §3.10 both units keep their `MainPID`, `NRestarts` and `ActiveState`. **This TZ signals nothing**, so a
FAIL runs no block; where the archive's own daily run restarted the pair book between the two reads, §3.11's `I
archive` shows its `restart` record, and the report names it.

---

## 5. The instrument

`research/tz29-maker-m0-second-look.py`, Appendix A, fixed by the Architect as this TZ's Validation and written byte for
byte. **The standard library alone**, run under `/root/tz04a-env` — Python 3.12.3, the recorder's interpreter, which
nothing here modifies. It imports nothing from the repository: it **loads** `research/tz23-maker-m0.py` from its own
directory, asserts its SHA-256 `6b3ace2c…` and executes those very bytes (lines 58 to 72), so TZ-23's audit hook, its
60-digit context and its malloc settings are installed and TZ-23's functions are the ones every step calls. **Its own
code** is its audit hook (lines 184 to 215), the idle stretch and the archive's run (lines 264 to 294), the walk's retry
(lines 301 to 311), the held fetch (lines 315 to 358), the first look from the store and G-REPLAY (lines
383 to 431), the sum over both looks (lines 436 to 487), the archive's ledger (lines 583 to 660), the modes and the
self-test. One mode a run; each prints its findings with UTC stamps, its peak memory, whether glibc took its two
settings, and its opens refused by either hook. Every number of the venue is parsed as the `Decimal` of its own text,
every sum is done in the main thread at 60 digits, and the fetch's two worker threads only parse and format (map §7 item
99). Exit `0` is every assert held; exit `1` a failed assert, named, or a BLOCK whose message says so. Run with `-O` it
refuses to start (lines 49 to 51).

---

## 6. Cost

Measured in the Architect's runs on 2026-10-19 under Python 3.12.3 on two cores of an Intel Xeon — the host has one
(map §6) — and taken at the population's upper bound: the walk at most `6,048` candidates — 4,032 members and TZ-23's
slack of 2,016 — in at most `303` document requests, and at most 25 walks; the fetch at all 4,032 members at the first
look's busiest day's rate, `1,766` rows a market (2026-09-08; its mean `1,491`, TZ-23's weekday bound `1,707`),
`7,120,512` rows, at most `7,322` pages of 1,000 over 202 chunks. **The fetch waits on the venue, not the processor,
and the venue's latency more than halved within the hour:** TZ-23's own fetch of the first look's 4,032 markets —
`6,013,558` rows, at least `6,118` pages — ran at `0.832` s a page and a worker, its slowest chunk `63.0` s by its
cache files' times; this instrument's held fetch of the same markets an hour later ran at `0.363` s a page, its
slowest chunk `30.1` s; TZ-23's fetch on the host on 2026-10-09 ran at `0.512` s a page.

| check | population | measured | bound |
|---|---|---|---|
| `fetch`, the walk | at most 303 gamma requests a walk | 202 requests in `56.9` to `60.5` s here, `23.0` s on the host | `91` s a walk at `0.30` s a request, inside its `120` s budget; at most 25 walks, each after `300` s |
| `fetch`, fetching | 202 chunks, at most 7,322 pages | `0.832` s a page and a worker at the slowest, two workers | `3,046` s of fetching; **projected after the first 30 fresh chunks, BLOCKED above `7,200` s** |
| `fetch`, wall | the same chunks, each started at seconds 15 to 470 of a window | `2,353` s for the first look's 202 chunks at `0.363` s a page: its first hold `310` s, its walk `57` s, then `1,982` s from the first chunk's start to the last one's end for `1,111` s of fetching, every chunk inside the idle stretch | about `5,700` s at the bound: each worker fetches about 480 s of every 900 |
| `constants`, twice | the second look's rows parsed and summed, both looks' members files written | `72.3` and `72.4` s for 6,013,558 rows | `86` s a run at the bound; `258` s on a host three times slower |
| `score`, twice | 8,064 members | `0.45` to `0.50` s | `15` s a run |
| `rehearse` | 144 markets, fixed | `119` s, of it `80` s held and `34` s fetching | `120` s of work and one hold, at most `444` s |
| `replay` | the first look's 4,032 members | `0.66` s | `15` s |
| `selftest`, `fingerprint`, `still`, `scratch`, `archive`, each `reclaim` | — | `0.8` to `5.3` s each | `30` s a run |

**Wall clock at those bounds about `7,000` s** — the fetch `5,700`, its walk and the wait of a retry beside it, the
constants twice `172`, `rehearse` with its hold `564`, the rest under `300` — **of which the processor's at most about
`1,100` s on a host three times slower; every second at `nice 19`.** The fetch's fail-fast bound, `7,200` s of fetching,
is its own bound, `3,046` s, at a venue `2.36` times slower than at its slowest measured run; slower still, the session
would hold the host for over four hours, and it stops BLOCKED. **A hold longer than `7,200` s stops BLOCKED:** the
longest wait the idle stretch makes is `444` s, from second 471 to second 15 of the next window, the calendar guard adds
`66` s, and TZ-28's first run lasted `749` s from its `start` to its `complete` record (map §2.5) — a hold of `7,200` s
is that run more than seven times over beside both. **The walk's retries wait at most `7,200` s**, 24 of `300` s: they
carry the walk past up to 24 non-members before its 4,032nd member — the first look had none in 4,032 — and a walk still
too recent after them stops BLOCKED.

---

## 7. Validation

| # | check | count |
|---|---|---|
| **V1** | §0.2's fingerprint | `FINGERPRINT PASS`: revision `2026-10-19-a`; anchors 6 of 6, 4 re-derived; 40 rows, 37 of 37 `frozen` equal |
| **V2** | §0.3's host gate | H1 to H4, the memory and the disk gate; the rest printed |
| **V3** | §0.1's and §3.1's file | 1 of 1 hash asserted at each, lines and bytes; TZ-23's file `6b3ace2c…` at each; the branch's diff against `origin/main` names exactly one path, `A`, 1,225 lines |
| **V4** | the self-test | `51 of 51` |
| **V5** | the archive's record | the ledger's size, SHA-256 and records, every run's line, the tags; recorded, gating nothing |
| **V6** | G-REHEARSAL | `16 of 16` — 10 figures and 6 files |
| **V7** | G-REPLAY | 6 of 6 stored files; 5 of 5 checks |
| **V8** | G-SET | 4,032 members; the candidates considered; every non-member with its reason; the chunks inside and outside the idle stretch |
| **V9** | the constants, twice | 5 of 5 files `unchanged` at the second run |
| **V10** | the score, twice | the reading; 2 of 2 files `unchanged`; 2 ledger lines; the first look's 4,032 scored rows equal to TZ-23's; the instant §3.1's `ls-remote` printed the instrument's commit on `origin`, beside the first ledger line's `at`, the first label read of the second set (map §7 item 63) |
| **V11** | G-STILL | both units unchanged, or the change named |
| **V12** | the hooks | `opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0` at every mode |
| **V13** | memory | every mode's printed peak, against §0.4's floor; `malloc tuned: True` at every mode |
| **V14** | contract §4.2's self-check | run after the push and the pull request and before the report's commit |
| **V15** | §3.11's closing reads | every read printed |
| **V16** | §9's `reclaim` runs | files considered, named by a report, kept by name, copied and already held; the store's count after equal to before plus the copies |
| **V17** | §9's removals | `git worktree remove` without `--force` exit `0`; `test -e` exit `1` for `/root/tz29-work` and each directory removed; `git worktree list` naming `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else |

---

## 8. The report

`CryptoReports/TZ-29-maker-m0-second-look-report.md`, in contract §8's order. **In its first lines:** M0's reading over
both looks, with `S`, its two parts, both bounds and both margins, each per share; G-REHEARSAL, G-REPLAY and G-SET; the
second set — candidates considered, members, first and last, non-members; the instant of the first label read beside the
instant the instrument's commit reached `origin` and the constants' `state.json` record (map §7 item 63's rule); and
G-STILL. Beyond what V1 to V17 print: the set — **every non-member with its reason**, the members by weekday and
weekend, the member list's SHA-256 and the set file's; both looks' window fills, shares, `X`, `C`, `R` and `V`, and the
sum's; the thresholds, both per share, and the power; **the reading**; the first look's `S` and the second look's by
difference, and the band figures, barred; **the timing files' summary lines and every chunk that ended after second
590**, with the walk's start second and both timing files by SHA-256 — §9 keeps them in the forensic store, so that B3's
measurement can set the pair book's segments beside every chunk; the archive's record as `I archive` printed it, at both
reads, and each run off the calendar beside §0.3's boots; both units at both reads, memory included; both ledger lines;
every block the classifier refused, who ran it and when; every free-space and `MemAvailable` read with its instant and
bound; §9's counts and removals; and every file the run wrote, by SHA-256, but the two chunk caches — the set's 202
files and the rehearsal's 8 — which §9 lets go with the tree. **The report is drafted in the primary checkout
`/root/btc-5m-twap` before B-RECLAIM-OWN and committed after it**, so the removal of this TZ's tree is in it.

---

## 9. Reclaim — the host left clean (CANON hard rule 15)

**What a file is kept for:** a committed report prints its SHA-256, whole or as a prefix of 16 to 64 hex characters,
or it is kept by name: `state.json`, `label-ledger.jsonl` and every file under `logs/`. `reclaim` copies each into
`/root/btc-forensics/` as `<tree>--<path with / as -->`, by exclusive create, and verifies its hash; a name already
there with the same hash is counted as held, and with another hash is a failed assert (lines 782 to 859). The branch
worktree is not copied: `reclaim` asserts that `git status --porcelain --ignored` in it prints nothing and that its
`HEAD` is its upstream's, so `git worktree remove` needs no `--force`. The report draft in `CryptoReports/` counts as a
report. The chunk caches are not named — the fills files hold their rows — and go with the tree. `replay` removes its
three copies of store files itself, so none is copied back.

**B-RECLAIM-SCRATCH**, after §3.3 and before §3.4, for every directory `I scratch` named **earlier** — none it named
live, and never this session's own; map §3 names TZ-28's pair, `6b7bd886…` and `6de9e261…`, unless a reboot of the
host emptied `/tmp` (map §6, process supervision):

```
I reclaim <each earlier directory, by its full path>
rm -rf <one such directory>; echo "exit=$?"
test -e <that directory>; echo "exit=$?"
```

One `I reclaim` names every earlier directory; then one `rm -rf` and one `test -e` a directory. `reclaim` refuses a
directory born from 1 s before to 60 s after a running claude process started, and any path but `/root/tz29-work` that
is not a UUID directory under `/tmp/` whose parent's name carries `btc-5m-twap`; it prints `RECLAIM PASS` before any
removal. If `I scratch` names none earlier, the block is recorded as empty and skipped.

**B-RECLAIM-OWN**, last, after §3.11 and with the report drafted. **Its output is written to no file; the report quotes
it verbatim from the session**, every line of it:

```
I reclaim /root/tz29-work
git -C /root/btc-5m-twap worktree remove /root/tz29-work/wt; echo "exit=$?"
rm -rf /root/tz29-work; echo "exit=$?"
test -e /root/tz29-work; echo "exit=$?"
git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
find /root/btc-forensics -type f | wc -l
df -B1 --output=source,size,avail /var/lib/btc-recorder
```

The branch `tz-29-maker-m0-second-look` stays on `origin` and as a local ref; only its working tree goes. **Kept:**
`/root/btc-recorder-svc/`, `/root/btc-pairbook-svc/` and `/root/btc-pairbook-archive-svc/` are the running units' code,
`/root/tz18a-svc/` the disabled chain book's; the three capture roots, the archive's state and the forensic store are
data, never scratch. **A refused `rm -rf` is handed to the Boss** by §3's route, one tree per command, and verified by
`test -e`.

---

## 10. Pre-send checks

Performed by the Architect on 2026-10-19 against this file as sent, in a reading separate from its writing, with the
repository at `origin/main` `f6ab6e5a7eab2b577ac2b541e85d7f99ba7872f5` and map revision `2026-10-19-a` as it ships with
this TZ. `tz23` is `research/tz23-maker-m0.py` at that commit, `6b3ace2c…`; any other line number without a file is
Appendix A's, the extracted file's.

| # | check | result |
|---|---|---|
| **C1** | scope against body | **Repository paths the body names or cites — ten, one class, and the 40 files of the map's table:** `CryptoTZ/TZ-29-maker-m0-second-look.md`, read by §0.1's script; `SYSTEM-MAP.md` and its table's files, read by `I0 fingerprint`; `BTC-EXECUTOR-INSTRUCTIONS.md`, cited for §1, §4.2, §6 and §8; `research/tz29-maker-m0-second-look.py`, written on the branch and staged; `research/tz23-maker-m0.py`, installed beside the staged copy and loaded by its bytes in both places, never modified; `research/tz26-nesting-b3-capture.py` and `research/tz28-pairbook-archive-timer.py`, cited for their lines and read by no step; `CryptoTZ/TZ-23-maker-m0.md`, cited and read by no step; every `CryptoReports/*.md`, `CryptoReports/TZ-23-maker-m0-report.md` among them, read by `reclaim` for hashes (lines 782 to 859); `CryptoReports/TZ-29-maker-m0-second-look-report.md`, written to `main`. **Entry points:** Appendix A's eleven modes (lines 1201 to 1221); §0.1's script; `install`; `sha256sum`; `git` (`fetch`, `worktree add`, `remove`, `prune` and `list`, `add`, `commit`, `push`, `ls-remote`, `rev-parse`, `branch`, `status`, and contract §4.2's `rev-list`, `diff` and `ls-tree`); `gh` for the pull request; §0.3's block; §3.7's wait; §3.11's reads; §9's `rm -rf`, `test -e` and `df`. **Output files**, every one under `/root/tz29-work/`: `stage/research/`'s two files; `logs/*`; `state.json`; `label-ledger.jsonl`; `rehearsal/` — `set.json`, 8 chunk files, `rehearsal-timing.jsonl`, the fills, members, constants, scored and reading files; `replay/`'s three copies, removed by `replay` itself; `set/` — `set.json`, 202 chunk files, `fetch-timing.jsonl`, `tz29-fills.jsonl.gz`, `tz29-members.csv`, `tz29-constants.json`; `cumulative/` — the members, constants, scored and reading files; `selftest-tmp/`, removed by the self-test; `wt/`; and §9's copies in `/root/btc-forensics/`. **Intersected with §2, by path and by content class:** item 1 × the branch's file and the report — neither exists at `f6ab6e5` (C3); item 2 × §0.3's `df`, `find` and `grep -c` and B-RECLAIM-OWN's `df` — named there; item 3 × §0.3's `du -sb` — named there, and no output carries a body of the pair book's store; item 4 × `I archive`'s read of `ledger.jsonl` and §0.3's `du -sb` — named there, and the ledger's records carry no price (TZ-28's lines 212 to 220 assert it); item 5 × every unit read — `show`, `is-active`, the hold's among them (lines 264 to 294), `is-enabled`, `list-timers` and `journalctl --list-boots`, all named there; item 6 × `/root/btc-forensics/` — §9's exclusive create, named, and the six first-look files read alone; item 7 × the report — item 2's exemption; **item 8, the label class** × `set/set.json`, whose documents carry `outcomePrices` — exemption (a); × `rehearsal/`'s files — (b); × `replay/`'s copies and the store's scored and reading files — (c); × `cumulative-scored.csv` and `cumulative-reading.json` — (d); `tz29-constants.json`, `tz29-members.csv`, `tz29-fills.jsonl.gz`, `cumulative-members.csv` and `cumulative-constants.json` carry no outcome, and the self-test asserts the cumulative constants file byte-identical with every label flipped (lines 1019 to 1093); item 9 × every request — gamma `/markets` and `/v2/trades` through `http_json`, `git` against `origin`, `gh` — all named there; **item 10, the class of a single fill's, member's or market's price, size or outcome** × the chunk caches, the set, fills, members and scored files — all under `/root/tz29-work/`, and §9's copies the named exemption; the logs print sums over a set, a non-member's reason as one of `qualify`'s eight words (tz23 lines 375 to 395), each chunk's first `T0` and seconds, and the ledger's records; item 11 × nothing. No prohibition was removed. |
| **C2** | origin of every expectation | **§5's literals** are Appendix A's, fixed by the Architect and measured by nothing: exits `0` and `1`, `-O` refused (lines 49 to 51). **§7's, by kind.** Quoted from a committed artifact: V1's revision `2026-10-19-a`, `6` anchors, `4` re-derived, `40` rows and `37` `frozen`, map `2026-10-19-a` §0, which ships in this upload; V3's `6b3ace2c…`, map §0; V6's 10 figures, tz23 lines 88 to 93, TZ-23's independent figures (TZ-23 §4.1), and its 6 hashes, TZ-23's report §2.13; V7's six sizes and hashes, TZ-23's report §2.13, and the figures `replay` and `first_look` assert — `4,032`, `2,023`, `1788530400`, `1791241800`, `699cab9a…`, `V`, `Sh`, `S` and UNDECIDABLE — TZ-23's report §2.6, §2.7 and §2.9 (lines 122 to 139). Computed by an implementation independent of the one under test: `1791242100`, `1792455300` and the 4,032nd member `1792451400`, integer arithmetic on CANON's `1791241800` and TZ-23's `300`, `3,900` and `4,032`, and `date -u -d @…`, exact; the self-test's projection — `623,389.475150266978894322547225` within `1e-20`, the per-share intervals, the power between `0.9998` and `0.9999`, and the first look's EARN bound to its last printed digit — `mpmath` at 80 digits, `623389.4751502669788943225472253741101257…`, better than the tolerance by more than fifty decades; §1's `1.119`, the same run; V3's lines, bytes and SHA-256, `wc` and `sha256sum` over Appendix A's file against the extraction script's `hashlib`, exact. Fixed by Appendix A's and tz23's code, which this TZ measures nothing to set: V4's `51`, V6's `16`, V7's `6` and `5`, V9's `5`, V10's `2` and `2`, V12's `0`. **§0.4's floors:** `4,800,000,000` = `4,500,000,000`, `research/tz26-nesting-b3-capture.py` line 132, + `300,000,000`, which is `143,149,706` measured, twice over, rounded up; `177,135,616` = 2 × `88,567,808`, the Architect's measured peak — both made before this TZ was sent, not by it. **No expectation depends on a quantity this TZ measures.** |
| **C3** | shape of every diff | One path, new: `git cat-file -e f6ab6e5:research/tz29-maker-m0-second-look.py` exits `128`, so the change replaces **none** of its lines; V3 asserts `A`. The report's path is new too, exit `128`. PART VI's two words for an additive diff appear nowhere in this TZ — `grep -c` of them prints `0` — since none is needed. |
| **C4** | cost of every check | §6, at the population's upper bound: 6,048 candidates in 303 document requests a walk, 25 walks at most; all 4,032 members at the first look's busiest day's rate, `7,120,512` rows, at most `7,322` pages over 202 chunks. `fetch`: the walk `91` s at `0.30` s a request; fetching `3,046` s at the slowest measured `0.832` s a page and a worker; held, about `5,700` s of wall clock. `constants` `86` s a run, `258` on a host three times slower; `score` `15` s; `rehearse` `120` s and one hold of at most `444`; `replay` `15` s; the rest `30` s a run. Wall clock at most about `7,000` s; **single-session processor at most about `1,100` s on a host three times slower — the held fetch's `148` s of processor for 6,013,558 rows here, `175` at the bound, and the constants' `172`, each three times over, and the rest under `80` — under `3,600`, so nothing is sampled.** The fail-fast bounds, derived in §6 from the same figures: the fetch's `7,200` s is `3,046` s times `2.36`; a hold's `7,200` s is TZ-28's first run, `749` s, more than seven times over beside the longest idle wait, `444` s, and the calendar guard's `66` s; the walk's retries, 24 × `300` s = `7,200` s. |
| **C5** | every count | **The set, if every candidate qualifies**, re-derived by a dry run of tz23's own `candidates` with every candidate qualifying and its clock at `1792455300`: `4,032` members in `1791242100` … `1792451400`, `4,032` considered, `202` document requests and `4,032` documents, `576` on each day of the week, `1,152` on a weekend, every one in segment `3`, member list `971258b4…`; with its clock one second earlier the walk stops BLOCKED after 201 requests, too recent — so `1792455300` is the first instant at which it can finish. **Both looks:** `8,064` = 4,032 + 4,032. **The chunks:** `202` = ⌈4,032 / 20⌉ for the set, `8` = ⌈144 / 20⌉ for the rehearsal. V1's `40` rows = `37` + `2` + `1`, read from the map, and `4` re-derived anchors: `A2`, `A4`, `A5`, `A6`. V6's `16` = 10 figures + 6 files. V7's `6` files and `5` checks: the scored and reading files, `S`, the Up count, the reading. V9's `5`: the second look's fills, members and constants files and both looks' members and constants files. V10's `2` files, scored and reading, and `2` ledger lines, one a `score` run. The forensic store: `1,846` before §9 by map §3. |
| **C6** | every population | `S`, its settlement and rebate parts, `X`, `C`, `R`, `V`, `Sh`, `thr`, both margins and the power: both looks' 8,064 members' fills inside `[T0, T0 + 240)`. The first look's `S` and the second's by difference, each per share, and the band figures: the same members' fills, the bands' all of them — barred from every reading. The weekend count, the weekdays and the segments: the members. The non-members and their reasons: the candidates considered. G-REHEARSAL's ten: the 144 markets of 2026-10-03/04, their window fills. G-REPLAY's five: the first look's 4,032 members as the store holds them. The timing lines: the chunks fetched fresh, each by the window it started in. Each memory peak: one mode's process. `MemAvailable` and free space: the host at each read. G-STILL: the two capture units. The archive's record: its ledger's complete lines at each read, and the tags `origin` carries. |
| **C7** | every signature and every behaviour | **tz23 at `f6ab6e5`, every function the TZ names, as the file holds it:** `def http_json(url, tries=8):` (233) — one `urllib.request.Request(url, headers=HEADERS, method="GET")` a try (238), `HEADERS` the two of lines 81 and 82; `def trades(cids, taker_only, tokens=None, keep_tx=False):` (269) — `assert c in by, "a row of %s outside the request" % c` (288), `assert r["token_id"] == tokens[c][0 if row[2] == "U" else 1]` (291), `if not cursor:` … `break` (296 to 298); `def qualify(t0, doc):` (375) — its eight words at lines 379 to 393, `outcomePrices` read only as `not in (["1", "0"], ["0", "1"])` (382); `def gate_constants(V, sh, lam=LAMBDA, alpha=ALPHA, delta=DELTA):` (410) — `thr = L / lam + lam * V / 8` (414), `"earn_at": thr, "no_earn_at": delta * sh - thr` (415 and 416), the power `0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))` with `sd = float(V.sqrt()) / 2.0` (420 to 422); `def reading(S, c):` (426) — `earn` first, then `no_earn` (427 to 433); `def candidates(start, spans, need, docs_of):` (449) — `next_open(start, spans)` (453), `assert len(considered) < need + WALK_SLACK` (455), `min(CHUNK, need - len(members))` (458), `assert chunk[-1] <= time.time() - RESOLVED_AFTER_S` with "too recent to be resolved" (461 and 462), `break` at the need-th member (470 and 471); `def fetch_chunk(cache, group):` (479) — `trades(cids, "true", tokens)` (486), written once, atomically (491); `def form_set(base, start, spans, need):` (495) — returns the stored set where `set.json` exists (498 to 503), else walks and writes it (504 to 512); `def member_rows(cache, groups):` (541) — each chunk's members asserted in order and by condition (546 and 548); `def build_constants(base, s, cache, groups, label):` (572) — label-free, `V += win["X"] * win["X"]` (583), `c = gate_constants(V, tot["win"]["sh"])` (599), its fills file by its own determinism check and the other two by `write_once` (591 to 597 and 611 to 613); `def score(base, s, const, label):` (642) — `rows[0] == COLS` and one row a document (646 and 649), `up = label_of(docs[t0])` (656), `reading` at 671 to 673, both files by `write_once` (685 and 686); `def write_once(path, data):` (175) — `unchanged` printed on a second run (177 to 181). **Appendix A's own, each sentence against its lines:** the load by bytes, lines 58 to 72; the hook, lines 184 to 215; the idle stretch and the archive's run, lines 264 to 294 — `IDLE[0] <= p <= IDLE[1] - budget`, the calendar span `ARCHIVE_CALENDAR_S - budget - ARCHIVE_LEAD_S` to `+ ARCHIVE_LEAD_S`, `RUNNING`, `HOLD_MAX_S`; the walk's retry, lines 301 to 311 — on "too recent to be resolved" alone, `WALK_TRIES` 25; the held fetch, lines 315 to 358 — `proj = busy / fresh * len(groups) / tz23.FETCH_WORKERS` at the 30th fresh chunk, and `f.cancel()` for every future on any exception; G-REPLAY, lines 383 to 431; the sum over both looks, lines 436 to 487 — the two headers asserted equal to `tz23.COLS`, the two looks' `T0` in order, `V` and `Sh` added, `tz23.gate_constants(V, sh)`; `score`'s refusal of a `HEAD` `origin` does not carry, lines 751 to 753. **TZ-28's `Ledger.write`** at `f6ab6e5` (lines 212 to 220): `rec = dict(rec, wall_ns=env.time_ns())`, `assert LEDGER_KEYS <= frozenset(rec)`, `tz27.forbid(rec, "ledger.jsonl")`, appended as one line — so every record carries `event`, `run` and `wall_ns`, which `I archive` reads. **`research/tz26-nesting-b3-capture.py` line 132:** `STREAM_FLOOR = 4500000000`. Every sentence matched its lines; none was rewritten after this reading. |
| **C8** | every cross-reference | **This TZ's own:** §0.1 to §0.5, §1, §2's items 1 to 11 and exemptions (a) to (d), §3.1 to §3.11, §4.1 to §4.5, §5, §6, §7's V1 to V17, §8, §9's two blocks — each resolves to the text it names. **CANON:** PART II's maker track — M0's row, "the next 4,032 qualifying markets after `1791241800`", "no TZ reads a five-minute market with `T0 > 1791241800` before it" — and B3's row, its store reserved; §1.1; hard rules 13 and 15; PART VI. **Map `2026-10-19-a`:** §0's rows and anchors; §1's refs, 49 lines; §2.5's archive record and its two runs off the calendar; §3's forensic store at `1,846`, TZ-28's pair and the code trees; §4's TZ-23 and TZ-28 rows; §5's B3 and M0 rows; §6's disk, memory, process supervision, harness, taker delay, public fills and maker incentives rows; §7's items 63, 87, 97, 99, 109 and 113. **Contract:** §1 steps 1 to 4, §4.2, §6, §8. **TZ-23:** §1's "A second look costs no error", "The test" and item 3, §4.1, §4.3; its report §2.5, §2.6, §2.7, §2.9, §2.13 and §2.14. **TZ-28:** its lines 212 to 220. Each read in its file, not from memory, and each supports the sentence that cites it. |

**Converted to BLOCK conditions under CANON hard rule 13**, because the Architect's session cannot reach the host:
H1 to H4 — the host's identity and the first look in its forensic store, which the Architect proved by re-fetching
the six files from the venue byte for byte, not by reading the host; the memory and the disk gate; §0.5's two refs
conditions; and G-REPLAY, which reads the store through TZ-23's own `score`. **Printed and gating nothing:** the
archive's ledger, the units, the boots and the tags — the Architect could not read them, and no gate of this TZ needs
them.

---

## Appendix A — `research/tz29-maker-m0-second-look.py`, byte for byte

Extracted by §0.1's script; the block's content is the file.

```python file=research/tz29-maker-m0-second-look.py
#!/usr/bin/env python3
"""TZ-29 - M0's second look: do the makers of btc-updown-5m earn, at settlement and with the 20% rebate, on the
fills inside [T0, T0 + 240), over TZ-23's 4,032 markets and the next 4,032 that qualify after them?

    fingerprint       contract section 1 steps 3 and 4, asserted: the map's revision, anchors and rows
    selftest          every rule of this file, on literals and on temporary trees under the work tree
    still             the recorder's and the pair book's MainPID, NRestarts and ActiveState: the first run
                      records them, the second compares (G-STILL)
    scratch OWN       the UUID directories beside OWN, this session's, each named live or earlier
    archive           the pair book archive's ledger, read and printed, beside the tags origin carries
    rehearse          the whole path on TZ-23's rehearsal span, every request held to the idle stretch
                      (G-REHEARSAL)
    replay            the first look, from the forensic store, scored again by TZ-23's score (G-REPLAY)
    fetch             the second set - the first 4,032 qualifying markets with T0 > 1791241800 - and
                      their taker fills, every request held to the idle stretch (G-SET)
    constants         label-free: the second look's sums, by TZ-23's build_constants, and both looks'
                      V, Sh, thresholds and power, on disk
    score             the labels of both looks, read once, and M0's reading over both
    reclaim TREE...   section 9

It loads research/tz23-maker-m0.py from beside itself, executed from the bytes whose SHA-256 it asserts,
and calls TZ-23's functions for the walk, the documents, the fills of a chunk, every sum, the thresholds
and the score: it writes no second implementation of any of them. Its requests are TZ-23's, to
gamma-api.polymarket.com and data-api.polymarket.com through TZ-23's http_json and its two headers, each
walk and each chunk started only inside seconds 15 to 470 of a 900-second window and never near or
during the pair book archive's run; and git against origin. Under /var/lib/btc-recorder,
/var/lib/btc-chainbook and /var/lib/btc-pairbook it opens and lists nothing, and under
/var/lib/btc-pairbook-archive it opens ledger.jsonl alone, for reading, in mode archive: an audit hook
refuses everything else there. It writes under /root/tz29-work/ and, in `reclaim`, new files in
/root/btc-forensics/ by exclusive create. It prints sums over a set and no price, size or outcome of any
single fill or market. Exit 0: every assert of the mode held. Exit 1: an assert failed, and its message
names it. Run it with the recorder's interpreter, /root/tz04a-env.

Written for CryptoTZ/TZ-29-maker-m0-second-look.md. The TZ is the specification.
"""

import concurrent.futures
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
    sys.stderr.write("tz29: refuses to run with asserts disabled (-O); every check is an assert\n")
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

MAP_REVISION = "2026-10-19-a"
ANCHORS = {"A1": "229a944f2d51", "A2": "6c5089330629",
           "A3": "0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable",
           "A4": "437b45ea196b", "A5": "0f6c90451cbd", "A6": "729f0bcdbee3"}
ANCHOR_FILES = {"A2": "research/twap-divergence.py", "A4": "BTC-EXECUTOR-INSTRUCTIONS.md",
                "A5": "research/recorder/recorder.py", "A6": "research/pfair.py"}
MAP_ROWS = {"frozen": 37, "tracked": 2, "reported": 1}
ROW = re.compile(r"^\| `([^`]+)` \| ([0-9,]+|—) \| ([0-9,]+|—) \| (frozen|tracked|reported) \| "
                 r"`?([0-9a-f]{64}|self-reference[^|]*?)`? \|$", re.M)
ANCHOR_ROW = re.compile(r"^\| `(A[0-9])` — [^|]*\| `([^`]+)` \|$", re.M)

LAST_FIRST = 1791241800      # M0's first look's last member, 2026-10-05 23:10 UTC (TZ-23)
START2 = LAST_FIRST + 300    # the second look's walk starts at the next five-minute market
N_SET = 4032                 # TZ-23's N_SET: two whole weeks of five-minute markets
START_AT = START2 + (N_SET - 1) * 300 + 3900    # 2026-10-20 00:15:00 UTC: no mode reads the second set before
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
MEM_FLOOR = 177135616        # MemAvailable: twice the largest peak of any mode, constants' (TZ-29 section 0.4)

WORK = "/root/tz29-work"
WT = WORK + "/wt"
STATE = WORK + "/state.json"
LEDGER = WORK + "/label-ledger.jsonl"
PRIMARY = "/root/btc-5m-twap"
REPORTS = PRIMARY + "/CryptoReports"
FORENSICS = "/root/btc-forensics"
BRANCH = "tz-29-maker-m0-second-look"
UNITS = {"recorder": "btc-recorder.service", "pairbook": "btc-pairbook.service"}
CAPTURE_ROOTS = ("/var/lib/btc-recorder", "/var/lib/btc-chainbook", "/var/lib/btc-pairbook")
ARCHIVE_STATE = "/var/lib/btc-pairbook-archive"
ARCHIVE_LEDGER = ARCHIVE_STATE + "/ledger.jsonl"
SHOW_ENV = {"TZ": "UTC", "LC_ALL": "C", "SYSTEMD_COLORS": "0", "SYSTEMD_PAGER": ""}

# The first look in the forensic store, each file by its size and SHA-256 in TZ-23's report (its 2.13 and 2.14)
STORE = FORENSICS + "/tz23-work--set--"
FIRST = {"set": (STORE + "set.json", 2314799,
                 "a04226f0ec324400fa493f8101b24becf2e0609e614e60aa11d6adeacae76303"),
         "fills": (STORE + "tz23-fills.jsonl.gz", 36870673,
                   "4f20400e20913dec4bff8cd715f03934dc1bde0933214258414afd55cdf55a64"),
         "members": (STORE + "tz23-members.csv", 2444450,
                     "cf269016781bca698eb0d707e5aea3ce5dfefc15d8a068b4deb85a03ec229a61"),
         "constants": (STORE + "tz23-constants.json", 2114,
                       "1b28df4382ed926ad92d514cb9bbfd6764e15a90b3e4c39618115db5e30217d5"),
         "scored": (STORE + "tz23-scored.csv", 464610,
                    "12002203479ac5634c509c4f4306b42159e74d10cf987839fad6ec7022bdb988"),
         "reading": (STORE + "tz23-reading.json", 1915,
                     "fdad516faaa3abfa7cc70134d19caa2be562d636235b464506a971893aef4043")}
# and its figures, as TZ-23's report prints them (its 2.7 and 2.9)
FIRST_FIGURES = {"members": 4032, "ups": 2023, "first": 1788530400, "last": LAST_FIRST,
                 "member_list_sha": "699cab9aa3f540b6cdfe2ae8a295b1fa4bca96921238106dad4b243bc4ecce4f",
                 "V": D("69635266807.031814646570"), "sh": D("129225737.554660"),
                 "S": D("272424.11263025802271516797439628522"), "reading": "UNDECIDABLE"}
# TZ-23's rehearsal files, by its report (its 2.5 and 2.13): the venue's record of the 144 markets, byte for byte
REHEARSAL_FILES = {"set.json": "83a53bd3fb13829173282487833ef0398280d358377e0f09d0beb414c7829cbc",
                   "rehearsal-fills.jsonl.gz": "3ce50a85f84068a4cac15ece53d2ea1b16184b9080d69228b0baae8f887c8116",
                   "rehearsal-members.csv": "2676af1dee730001abf560555c1c0eb9b88901209a94598dcb966495e20131d1",
                   "rehearsal-constants.json": "9f521a23b3a5b48ac7569f68a9c42bf6da1bb8ef09f5a71c0c8e091fbf5098e3",
                   "rehearsal-scored.csv": "d31eb18fa58f8a26f12979f733fcead3b2482a480ba97a17c1145c1eef99bda2",
                   "rehearsal-reading.json": "4cdf1a1179c0d58f048d091e0a719951cb3af38c822d49a2e9343bea5f502d1f"}
UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
TOKEN = re.compile(r"[0-9a-f]{16,64}")
LIVE_S = 60                  # a directory born this soon after a claude process started is that process's

# ---- the audit hook: TZ-29 section 2's reads and writes ------------------------------------------------

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
    """None where TZ-29 section 2 allows the event in this mode; otherwise the reason it is refused."""
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
        return None if mode == "archive" and p == ARCHIVE_LEDGER and not w else "an open under the archive's state"
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


def groups_of(s):
    return [[(m["t0"], m["doc"]) for m in s["members"][i:i + tz23.CHUNK]]
            for i in range(0, len(s["members"]), tz23.CHUNK)]

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


def fetch_held(base, s, timing, budget_s=FETCH_BUDGET_S, fetcher=None, holdf=hold, clock=time.time):
    """TZ-23's fetch_fills with each chunk held: every chunk not already in the cache is fetched by TZ-23's
    fetch_chunk, started where holdf allows, and its start and end are written to `timing`."""
    fetcher = fetcher or tz23.fetch_chunk
    cache = os.path.join(base, "cache")
    os.makedirs(cache, exist_ok=True)
    groups = groups_of(s)

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

# ---- the first look, from the forensic store --------------------------------------------------------------


def verify_first(first=None):
    """The first look's six files in the forensic store, each its size and SHA-256 by TZ-23's report."""
    first = first or FIRST
    for key in sorted(first):
        path, nbytes, sha = first[key]
        got = (os.path.getsize(path), tz23.sha256_file(path))
        assert got == (nbytes, sha), "the first look's %s %s: %r, TZ-23's %r" % (key, path, got, (nbytes, sha))
        out("first look %-9s %s %d bytes sha256 %s equal" % (key, path, nbytes, sha))
    return len(first)


def first_look(first=None, figures=None):
    """The first look's set and constants, asserted on TZ-23's figures."""
    first, figures = first or FIRST, figures or FIRST_FIGURES
    s1, c1 = load_json(first["set"][0]), load_json(first["constants"][0])
    t1 = [m["t0"] for m in s1["members"]]
    assert len(t1) == figures["members"] and t1[0] == figures["first"] and t1[-1] == figures["last"], \
        "the first look's set: %d members, %r to %r" % (len(t1), t1[:1], t1[-1:])
    assert c1["member_list_sha"] == figures["member_list_sha"] == tz23.sha256_bytes(
        ("\n".join(map(str, t1)) + "\n").encode()), "the first look's member list"
    assert D(c1["gate"]["V"]) == figures["V"] and D(c1["gate"]["sh"]) == figures["sh"], "the first look's V and Sh"
    return s1, c1


def replay(base, first=None, figures=None):
    """G-REPLAY: TZ-23's score of the first look, run again on the forensic store's set, members and constants;
    its two outputs must be the store's, byte for byte, and its figures TZ-23's. The copies are removed after."""
    first, figures = first or FIRST, figures or FIRST_FIGURES
    s1, c1 = first_look(first, figures)
    os.makedirs(base, exist_ok=True)
    assert not os.listdir(base), "replay: %s is not empty" % base
    members = os.path.join(base, "tz23-members.csv")
    with open(first["members"][0], "rb") as src, open(members, "xb") as dst:
        shutil.copyfileobj(src, dst, 1 << 20)
    res = tz23.score(base, s1, c1, "tz23")
    checks = {}
    for key, name in (("scored", "tz23-scored.csv"), ("reading", "tz23-reading.json")):
        got = tz23.sha256_file(os.path.join(base, name))
        checks["%s equal to the store's" % name] = got == first[key][2]
        out("G-REPLAY %-18s sha256 %s, the store's %s" % (name, got, first[key][2]))
    checks["S equal to TZ-23's"] = res["S"] == figures["S"]
    checks["Up outcomes equal to TZ-23's"] = res["ups"] == figures["ups"]
    checks["reading equal to TZ-23's"] = res["reading"] == figures["reading"]
    for k, v in checks.items():
        out("G-REPLAY %-34s %s" % (k, v))
    for name in ("tz23-members.csv", "tz23-scored.csv", "tz23-reading.json"):
        os.remove(os.path.join(base, name))
    os.rmdir(base)
    return checks

# ---- the sum over both looks ------------------------------------------------------------------------------


def cumulative(cbase, c1, members1, s2, const2, members2):
    """Both looks as one sum: the members file is the first look's rows, then the second's, under the header both
    carry; V and Sh are the two looks' sums added; the thresholds and the power are TZ-23's gate_constants on them.
    Label-free: no outcome is read."""
    with open(members1, "rb") as fh:
        m1 = fh.read()
    with open(members2, "rb") as fh:
        m2 = fh.read()
    h1, rows1 = m1.split(b"\n", 1)
    h2, rows2 = m2.split(b"\n", 1)
    assert h1 == h2 == ",".join(tz23.COLS).encode("utf-8"), "the two members files' headers"
    t1 = [int(ln.split(b",", 1)[0]) for ln in rows1.split(b"\n") if ln]
    t2 = [int(ln.split(b",", 1)[0]) for ln in rows2.split(b"\n") if ln]
    assert t2 == [m["t0"] for m in s2["members"]] and t1 and t2 and t1[-1] < t2[0], "the two looks' order"
    body = h1 + b"\n" + rows1 + rows2
    assert body.count(b"\n") == 1 + len(t1) + len(t2), "the cumulative members file's lines"
    os.makedirs(cbase, exist_ok=True)
    msha = tz23.write_once(os.path.join(cbase, "cumulative-members.csv"), body)
    V = D(c1["gate"]["V"]) + D(const2["gate"]["V"])
    sh = D(c1["gate"]["sh"]) + D(const2["gate"]["sh"])
    t0s = t1 + t2
    look = lambda c, msh: {"members": c["members"], "first": c["first"], "last": c["last"],
                           "member_list_sha": c["member_list_sha"], "members_csv_sha": msh,
                           "fills_sha": c["fills_sha"], "considered": c["considered"],
                           "non_members": c["non_members"], "weekend_members": c["weekend_members"],
                           "V": D(c["gate"]["V"]), "sh": D(c["gate"]["sh"]), "window": c["totals"]["win"]}
    const = {"label": "cumulative", "members": len(t0s), "first": t0s[0], "last": t0s[-1],
             "member_list_sha": tz23.sha256_bytes(("\n".join(map(str, t0s)) + "\n").encode()),
             "looks": {"first": look(c1, tz23.sha256_bytes(m1)), "second": look(const2, tz23.sha256_bytes(m2))},
             "gate": tz23.gate_constants(V, sh), "members_csv_sha": msha}
    csha = tz23.write_once(os.path.join(cbase, "cumulative-constants.json"), dumps(const).encode("utf-8"))
    return const, msha, csha


def show_cumulative(const, msha, csha):
    g, f, s = const["gate"], const["looks"]["first"], const["looks"]["second"]
    for name, lk in (("first", f), ("second", s)):
        w = lk["window"]
        out("%s look: members %d, %d to %d, considered %d, non-members %d, weekend %d; window fills %d, shares %s, "
            "X %s, C %s, R %s; V %s" % (name, lk["members"], lk["first"], lk["last"], lk["considered"],
                                       len(lk["non_members"]), lk["weekend_members"], w["n"], fx(D(w["sh"])),
                                       fx(D(w["X"])), fx(D(w["C"])), fx(D(w["R"])), fx(lk["V"])))
    out("both looks: members %d, %d to %d, member list sha %s" % (const["members"], const["first"], const["last"],
                                                                   const["member_list_sha"]))
    out("both looks: V %s; Sh %s; lambda %s; L %s" % (fx(g["V"]), fx(g["sh"]), fx(g["lambda"]), fx(g["L"])))
    out("EARN at S >= %s (%s a share); NO EARN at S <= %s (%s a share)" % (
        fx(g["earn_at"]), fx(g["thr_per_share"]), fx(g["no_earn_at"]), fx(g["no_earn_per_share"])))
    out("power of either answer against the other's alternative, normal, variance V/4: %s" % fx(g["power"]))
    out("2 thr / Sh %s against delta %s: %s" % (fx(2 * g["thr_per_share"]), fx(g["delta"]),
                                                "UNDECIDABLE cannot occur" if 2 * g["thr_per_share"] <= g["delta"]
                                                else "UNDECIDABLE can occur"))
    out("wrote cumulative-members.csv sha256 %s and cumulative-constants.json sha256 %s" % (msha, csha))

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
    out("SYSTEM-MAP.md %d lines %d bytes sha256 %s" % (raw.count(b"\n"), len(raw), tz23.sha256_bytes(raw)))
    out("FINGERPRINT PASS: revision %s; anchors 6 of 6, 4 re-derived; rows %d: frozen %d of %d equal, tracked %d, "
        "reported %d" % (MAP_REVISION, len(rows), states["frozen"], MAP_ROWS["frozen"], states["tracked"],
                         states["reported"]))


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
        st["still"] = {"at": utc(time.time()), "units": now}
        save_state(st)
        out("still: recorded")
        return
    same = now == st["still"]["units"]
    out("G-STILL %s: %s since %s" % ("PASS" if same else "FAIL", "unchanged" if same else "changed",
                                     st["still"]["at"]))


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
            parts.append("Release %s: sent %s, held %s" % (r.get("release_id"), r.get("sent"), r.get("held")))
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


def mode_archive():
    """The archive's own record, read whole: its complete lines, each printed, and its runs summarized."""
    for unit in (ARCHIVE_TIMER, ARCHIVE_UNIT):
        out("%s %s" % (unit, show(unit, ["ActiveState", "SubState", "UnitFileState", "Result", "ExecMainStatus",
                                         "LastTriggerUSec", "NextElapseUSecRealtime"])))
    with open(ARCHIVE_LEDGER, "rb") as fh:
        raw = fh.read()
    lines = raw.split(b"\n")
    tail = lines.pop()
    recs = [json.loads(ln) for ln in lines if ln.strip()]
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


def mode_rehearse():
    floor_check()
    base = os.path.join(WORK, "rehearsal")
    s = walk(base, tz23.REHEARSAL[0], (), tz23.REHEARSAL[1])
    assert len(s["members"]) == tz23.REF["members"] and len(s["considered"]) == tz23.REF["members"], \
        "G-REHEARSAL: %d members of %d considered" % (len(s["members"]), len(s["considered"]))
    cache, groups = fetch_held(base, s, os.path.join(base, "rehearsal-timing.jsonl"), budget_s=10 ** 9)
    timing_summary(os.path.join(base, "rehearsal-timing.jsonl"))
    const, paths = tz23.build_constants(base, s, cache, groups, "rehearsal")
    tz23.show_constants(const, paths)
    res = tz23.score(base, s, const, "rehearsal")
    w = const["totals"]["win"]
    got = {"members": const["members"], "ups": res["ups"], "n": w["n"], "sh": w["sh"], "X": w["X"], "C": w["C"],
           "R": w["R"], "V": const["gate"]["V"], "XU": res["XU"], "S": res["S"]}
    checks = {}
    for k in tz23.REF:
        checks["figure " + k] = got[k] == tz23.REF[k]
        out("G-REHEARSAL %-7s instrument %s, the Architect's %s, %s" % (k, got[k], tz23.REF[k],
                                                                       "equal" if got[k] == tz23.REF[k] else
                                                                       "DIFFERENT"))
    for name, want in sorted(REHEARSAL_FILES.items()):
        h = tz23.sha256_file(os.path.join(base, name))
        checks["file " + name] = h == want
        out("G-REHEARSAL %-24s sha256 %s, TZ-23's %s, %s" % (name, h, want, "equal" if h == want else "DIFFERENT"))
    bad = sorted(k for k, v in checks.items() if not v)
    assert not bad, "G-REHEARSAL FAIL: %s" % bad
    out("G-REHEARSAL PASS: %d of %d - %d figures and %d files equal to TZ-23's" % (
        len(checks), len(checks), len(tz23.REF), len(REHEARSAL_FILES)))


def mode_replay():
    floor_check()
    verify_first()
    checks = replay(os.path.join(WORK, "replay"))
    bad = sorted(k for k, v in checks.items() if not v)
    assert not bad, "G-REPLAY FAIL: %s" % bad
    out("G-REPLAY PASS: 6 of 6 stored files equal, %d of %d checks" % (len(checks), len(checks)))


def second_set():
    base = os.path.join(WORK, "set")
    s = load_json(os.path.join(base, "set.json"))
    return base, s, os.path.join(base, "cache"), groups_of(s)


def mode_fetch():
    now = time.time()
    assert now >= START_AT, "BLOCKED: %s is before %s, TZ-29's instant" % (utc(now), utc(START_AT))
    floor_check()
    base = os.path.join(WORK, "set")
    os.makedirs(base, exist_ok=True)
    s = walk(base, START2, tz23.EXCLUDED, N_SET)
    t0s = [m["t0"] for m in s["members"]]
    assert s["start"] == START2 and s["need"] == N_SET and len(t0s) == N_SET, "G-SET: %d members" % len(t0s)
    assert s["considered"][0][0] == START2 and t0s[0] > LAST_FIRST, "G-SET: the walk did not start at %d" % START2
    cache, groups = fetch_held(base, s, os.path.join(base, "fetch-timing.jsonl"))
    n = sum(1 for _ in tz23.member_rows(cache, groups))
    assert n == N_SET, "G-SET: %d members read back" % n
    timing_summary(os.path.join(base, "fetch-timing.jsonl"))
    out("G-SET PASS: %d members, %d considered, %d to %d, %d chunks, every chunk read back" % (
        N_SET, len(s["considered"]), t0s[0], t0s[-1], len(groups)))


def mode_constants():
    floor_check()
    verify_first()
    s1, c1 = first_look()
    base, s2, cache, groups = second_set()
    assert len(s2["members"]) == N_SET and s2["start"] == START2, "the second set"
    const2, paths2 = tz23.build_constants(base, s2, cache, groups, "tz29")
    tz23.show_constants(const2, paths2)
    const, msha, csha = cumulative(os.path.join(WORK, "cumulative"), c1, FIRST["members"][0], s2, const2,
                                   paths2["members.csv"][0])
    show_cumulative(const, msha, csha)
    st = load_state()
    st["constants_sha"], st["constants_at"] = csha, utc(time.time())
    save_state(st)


def mode_score():
    floor_check()
    verify_first()
    s1, _c1 = first_look()
    _base, s2, _cache, _groups = second_set()
    cbase = os.path.join(WORK, "cumulative")
    cpath = os.path.join(cbase, "cumulative-constants.json")
    st = load_state()
    assert tz23.sha256_file(cpath) == st.get("constants_sha"), "score: not the constants recorded"
    head = git("rev-parse", "HEAD")
    assert "origin/" + BRANCH in git("branch", "-r", "--contains", head).split(), \
        "score: HEAD %s is not on origin" % head
    const = load_json(cpath)
    s = {"members": s1["members"] + s2["members"]}
    t0s = [m["t0"] for m in s["members"]]
    assert tz23.sha256_bytes(("\n".join(map(str, t0s)) + "\n").encode()) == const["member_list_sha"], \
        "score: the members are not the constants' members"
    with open(LEDGER, "a", encoding="utf-8") as fh:
        fh.write(dumps({"at": utc(time.time()), "head": head, "members": const["members"],
                        "member_list_sha": const["member_list_sha"]}))
    res = tz23.score(cbase, s, const, "cumulative")
    with open(os.path.join(cbase, "cumulative-scored.csv"), "rb") as fh:
        scored = fh.read().split(b"\n")
    with open(FIRST["scored"][0], "rb") as fh:
        first_scored = fh.read().split(b"\n")
    assert scored[:N_SET + 1] == first_scored[:N_SET + 1], "score: the first look's rows are not TZ-23's"
    out("the first look's %d rows of the scored file equal TZ-23's, byte for byte" % N_SET)
    r1 = load_json(FIRST["reading"][0])
    S1, P1, R1, U1 = D(r1["S"]), D(r1["P"]), D(r1["R"]), r1["ups"]
    sh2 = D(const["looks"]["second"]["sh"])
    S2, P2, R2 = res["S"] - S1, res["P"] - P1, res["R"] - R1
    out("the first look, TZ-23's: S %s = settlement %s + rebate %s, %d Up" % (fx(S1), fx(P1), fx(R1), U1))
    out("the second look, by difference, barred from every reading: S %s = settlement %s + rebate %s, %d Up; "
        "per share %s = %s + %s" % (fx(S2), fx(P2), fx(R2), res["ups"] - U1, fx(S2 / sh2), fx(P2 / sh2),
                                    fx(R2 / sh2)))
    if res["earn"] and res["no_earn"]:
        out("both bounds hold: the reading is EARN, and half a tick a share is rejected too (TZ-23 section 4.3)")
    out("M0 READING, OVER BOTH LOOKS: %s" % res["reading"])


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
    ok((tz23.N_SET, tz23.STEP, tz23.CHUNK, tz23.RESOLVED_AFTER_S, tz23.WALK_SLACK, tz23.FETCH_WORKERS) ==
       (N_SET, 300, 20, 3900, 2016, 2), "TZ-23's set size, step, chunk, resolution age, slack and workers")
    ok((tz23.ALPHA, tz23.DELTA, tz23.LAMBDA) == (D("0.005"), D("0.005"), D("0.000021932")),
       "TZ-23's alpha, delta and lambda, the second look's by TZ-23 section 1")
    ok(tz23.HEADERS == {"User-Agent": "btc-5m-twap-m0/TZ-23", "Accept": "application/json"},
       "every request carries TZ-23's two headers")
    # the second look's set, its walk and its instant
    ok(START2 == 1791242100 and utc(START2) == "2026-10-05T23:15:00Z", "the walk starts at 2026-10-05 23:15 UTC")
    ok(START_AT == 1792455300 and utc(START_AT) == "2026-10-20T00:15:00Z" and
       START_AT == START2 + (N_SET - 1) * tz23.STEP + tz23.RESOLVED_AFTER_S,
       "no set is read before 2026-10-20 00:15 UTC, the 4,032nd member's resolution age")
    ok(tz23.next_open(START2, tz23.EXCLUDED) == START2 and not tz23.excluded(START2, tz23.EXCLUDED),
       "no excluded span reaches the second look")
    good = {"slug": "", "outcomes": '["Up", "Down"]', "outcomePrices": '["1", "0"]', "closed": True,
            "feeType": tz23.FEE_TYPE, "feeSchedule": dict(tz23.FEE_SCHEDULE), "eventStartTime": "",
            "conditionId": "0x" + "cd" * 32, "clobTokenIds": '["11", "22"]'}

    def fake_docs(t0s, asked=None):
        if asked is not None:
            asked.extend(t0s)
        return {"btc-updown-5m-%d" % t: dict(good, slug="btc-updown-5m-%d" % t, eventStartTime=tz23.iso(t))
                for t in t0s}

    ok(START2 + (N_SET - 1) * tz23.STEP == 1792451400 and utc(1792451400) == "2026-10-19T23:10:00Z",
       "every candidate qualifying, the 4,032nd member is 1792451400, 2026-10-19 23:10 UTC")
    asked = []
    cons, mem = tz23.candidates(START2, tz23.EXCLUDED, 50, lambda ts: fake_docs(ts, asked))
    ok(len(mem) == 50 and mem[0][0] == START2 and mem[-1][0] == START2 + 49 * 300 and len(cons) == 50 and
       len(asked) == 50, "TZ-23's walk from 1791242100 takes 50 qualifying members in 50 documents")
    ok(asked == [t for t, _st in cons] and min(asked) > LAST_FIRST,
       "the walk requests no document at or below 1791241800 and none after the need-th member")
    ok(tz23.segments([t for t, _d in mem]) == {"3": 50}, "every second-look member reads segment 3")
    # the walk again, 300 s later, on a market too recent to be resolved; any other stop is final
    calls, slept = [], []

    def form_stops(times, msg):
        def form(base, start, spans, need):
            calls.append(start)
            if len(calls) <= times:
                raise AssertionError(msg)
            return {"start": start}
        return form

    r = walk("/nonexistent", START2, (), N_SET, form=form_stops(2, "BLOCKED: the walk reached x, too recent to "
                                                                   "be resolved"),
             holdf=lambda b: (0, 0), sleep=slept.append)
    ok(r == {"start": START2} and len(calls) == 3 and slept == [WALK_RETRY_S, WALK_RETRY_S],
       "a walk stopped twice on a market too recent is walked a third time, 300 s after each stop")
    calls.clear()
    try:
        walk("/nonexistent", START2, (), N_SET, form=form_stops(1, "BLOCKED: 6049 considered for 4031 members"),
             holdf=lambda b: (0, 0), sleep=slept.append)
        stopped = False
    except AssertionError:
        stopped = True
    ok(stopped and len(calls) == 1, "a walk stopped on its slack is not walked again")
    # the clock: the idle stretch, the archive's calendar run and its service
    W = 1792458000
    idle = lambda st="inactive": (lambda: st)
    ok(quiet(W + 14, CHUNK_BUDGET_S, idle()) is not None and quiet(W + 15, CHUNK_BUDGET_S, idle()) is None and
       quiet(W + 470, CHUNK_BUDGET_S, idle()) is None and quiet(W + 471, CHUNK_BUDGET_S, idle()) is not None,
       "a chunk starts from second 15 to 470 of a window and at no other second")
    ok(quiet(W + 600, CHUNK_BUDGET_S, idle()) is not None and quiet(W + 899, CHUNK_BUDGET_S, idle()) is not None,
       "nothing starts while the pair book streams, seconds 595 to 905")
    cal = W // 86400 * 86400 + ARCHIVE_CALENDAR_S
    ok(cal % WINDOW_S == 20, "the archive's calendar run is at second 20 of its window")
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
    # the fetch, held, on a fake chunk fetcher: each fresh chunk timed, a cached chunk fetched again by nothing
    tmp = os.path.join(WORK, "selftest-tmp")
    shutil.rmtree(tmp, ignore_errors=True)
    try:
        os.makedirs(tmp)
        s = {"members": [{"t0": START2 + 300 * i, "doc": dict(good, conditionId="0x%064x" % (i + 1))}
                         for i in range(45)]}
        fetched = []

        def fake_fetch(cache, group):
            fetched.append(group[0][0])
            path = tz23.chunk_path(cache, group[0][0])
            tz23.write_atomic(path, tz23.gz_bytes(dumps({"members": [
                {"t0": t, "condition": d["conditionId"], "rows": []} for t, d in group]})))
            return path, True

        timing = os.path.join(tmp, "timing.jsonl")
        clk = [float(W + 20)]
        cache, groups = fetch_held(tmp, s, timing, fetcher=fake_fetch, holdf=lambda b: (clk[0], 0.0),
                                   clock=lambda: clk[0])
        recs, outside = timing_summary(timing)
        ok(len(groups) == 3 and sorted(fetched) == [START2, START2 + 6000, START2 + 12000] and len(recs) == 3
           and not outside, "45 members are 3 chunks, each fetched once and timed inside the idle stretch")
        fetched.clear()
        fetch_held(tmp, s, timing, fetcher=fake_fetch, holdf=lambda b: (clk[0], 0.0), clock=lambda: clk[0])
        ok(fetched == [] and len(timing_summary(timing)[0]) == 3, "a cached chunk is fetched again by nothing")
        ok(sum(1 for _ in tz23.member_rows(cache, groups)) == 45, "every chunk reads back to its members")
        big = {"members": [{"t0": START2 + 300 * i, "doc": dict(good, conditionId="0x%064x" % (i + 1))}
                           for i in range(800)]}

        import threading
        gate = threading.Event()

        def slow_fetch(step, held_from=None):
            def f(cache, group):
                if held_from is not None and (group[0][0] - START2) // 6000 >= held_from:
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
                                                  "30th chunk: at most the two chunks running end, and the six "
                                                  "queued never start")
        fetched.clear()
        fetch_held(os.path.join(tmp, "fast"), big, os.path.join(tmp, "fast.jsonl"), fetcher=slow_fetch(10.0),
                   holdf=lambda b: (clk[0], 0.0), clock=lambda: clk[0])
        ok(len(fetched) == 40, "a fetch projected under it fetches all 40 chunks")
        # both looks as one sum: equal to TZ-23's build_constants over the union, the fills file aside
        rng = random.Random(29)

        def look(t0s, k):
            docs = [dict(good, slug="btc-updown-5m-%d" % t, eventStartTime=tz23.iso(t), conditionId="0x%064x" % (
                k * 1000 + i + 1), outcomePrices=('["1", "0"]' if rng.random() < 0.5 else '["0", "1"]'))
                    for i, t in enumerate(t0s)]
            rows = {t: sorted([[t + rng.randrange(-30, 330), rng.choice("BS"), rng.choice("UD"),
                                tz23.fx(D(rng.randrange(1, 500000)) / 100), tz23.fx(D(rng.randrange(1, 999)) / 1000)]
                               for _ in range(rng.randrange(0, 40))]) for t in t0s}
            return docs, rows

        def build(base, docs, rows, label):
            cache = os.path.join(base, "cache")
            os.makedirs(cache)
            st = {"start": docs[0]["eventStartTime"], "need": len(docs),
                  "considered": [[int(d["slug"].rsplit("-", 1)[1]), "member"] for d in docs],
                  "members": [{"t0": int(d["slug"].rsplit("-", 1)[1]), "doc": tz23.kept_doc(d)} for d in docs]}
            groups = groups_of(st)
            for g in groups:
                tz23.write_atomic(tz23.chunk_path(cache, g[0][0]), tz23.gz_bytes(dumps({"members": [
                    {"t0": t, "condition": d["conditionId"], "rows": rows[t]} for t, d in g]})))
            const, paths = tz23.build_constants(base, st, cache, groups, label)
            return st, const, paths

        ta = [1788530400 + 300 * i for i in range(23)]
        tb = [START2 + 300 * i for i in range(27)]
        da, ra = look(ta, 1)
        db, rb = look(tb, 2)
        sa, ca, pa = build(os.path.join(tmp, "a"), da, ra, "tz23")
        sb, cb, pb = build(os.path.join(tmp, "b"), db, rb, "tz29")
        su, cu, pu = build(os.path.join(tmp, "u"), da + db, {**ra, **rb}, "u")
        const, msha, csha = cumulative(os.path.join(tmp, "c"), ca, pa["members.csv"][0], sb, cb, pb["members.csv"][0])
        with open(pu["members.csv"][0], "rb") as fh:
            union_members = fh.read()
        ok(msha == tz23.sha256_bytes(union_members),
           "the cumulative members file is byte for byte TZ-23's build_constants over the union")
        ok(D(const["gate"]["V"]) == cu["gate"]["V"] and D(const["gate"]["sh"]) == cu["gate"]["sh"] and
           all(D(const["gate"][k]) == cu["gate"][k] for k in ("thr", "earn_at", "no_earn_at")),
           "both looks' V, Sh and thresholds equal TZ-23's build_constants over the union")
        ok(const["member_list_sha"] == cu["member_list_sha"] and const["members"] == cu["members"] == 50,
           "the cumulative member list is the union's")
        su_score = {"members": sa["members"] + sb["members"]}
        res_c = tz23.score(os.path.join(tmp, "c"), su_score, load_json(os.path.join(tmp, "c",
                                                                                    "cumulative-constants.json")),
                           "cumulative")
        res_u = tz23.score(os.path.join(tmp, "u"), su, cu, "u")
        with open(os.path.join(tmp, "c", "cumulative-scored.csv"), "rb") as fh:
            sc_c = fh.read()
        with open(os.path.join(tmp, "u", "u-scored.csv"), "rb") as fh:
            sc_u = fh.read()
        ok(sc_c == sc_u and all(res_c[k] == res_u[k] for k in ("S", "P", "R", "XU", "ups", "reading", "earn",
                                                                "no_earn")),
           "the score over both looks equals TZ-23's score over the union, file and figures")
        res_a = tz23.score(os.path.join(tmp, "a"), sa, ca, "tz23")
        with open(os.path.join(tmp, "a", "tz23-scored.csv"), "rb") as fh:
            sc_a = fh.read().split(b"\n")
        ok(sc_c.split(b"\n")[:len(ta) + 1] == sc_a[:len(ta) + 1],
           "the first look's rows of the scored file over both looks are its own scored rows")
        res_b = tz23.score(os.path.join(tmp, "b"), sb, cb, "tz29")
        ok(res_c["S"] == res_a["S"] + res_b["S"] and res_c["ups"] == res_a["ups"] + res_b["ups"],
           "S over both looks is the first look's S plus the second's, exactly")
        # label-free: the cumulative constants file with every label of both looks flipped
        flip = lambda docs: [dict(d, outcomePrices=('["0", "1"]' if d["outcomePrices"] == '["1", "0"]'
                                                    else '["1", "0"]')) for d in docs]
        sa2, ca2, pa2 = build(os.path.join(tmp, "a2"), flip(da), ra, "tz23")
        sb2, cb2, pb2 = build(os.path.join(tmp, "b2"), flip(db), rb, "tz29")
        const2, msha2, csha2 = cumulative(os.path.join(tmp, "c2"), ca2, pa2["members.csv"][0], sb2, cb2,
                                          pb2["members.csv"][0])
        ok(csha2 == csha and msha2 == msha, "the cumulative constants file is byte-identical with every label flipped")
        res_c2 = tz23.score(os.path.join(tmp, "c2"), {"members": sa2["members"] + sb2["members"]},
                            load_json(os.path.join(tmp, "c2", "cumulative-constants.json")), "cumulative")
        ok(res_c2["S"] != res_c["S"], "the score moves when the labels flip (negative control)")
        again = cumulative(os.path.join(tmp, "c"), ca, pa["members.csv"][0], sb, cb, pb["members.csv"][0])
        ok(again[1:] == (msha, csha), "a second cumulative run finds both files unchanged")
        # G-REPLAY on a store made here: a first look built and scored, then replayed from its files
        store = {"set": os.path.join(tmp, "a", "set.json"), "fills": pa["fills.jsonl.gz"][0],
                 "members": pa["members.csv"][0], "constants": pa["constants.json"][0],
                 "scored": os.path.join(tmp, "a", "tz23-scored.csv"), "reading": os.path.join(tmp, "a",
                                                                                          "tz23-reading.json")}
        with open(store["set"], "w", encoding="utf-8") as fh:
            fh.write(dumps(sa))
        first = {k: (p, os.path.getsize(p), tz23.sha256_file(p)) for k, p in store.items()}
        figures = {"members": len(ta), "ups": res_a["ups"], "first": ta[0], "last": ta[-1],
                   "member_list_sha": ca["member_list_sha"], "V": ca["gate"]["V"], "sh": ca["gate"]["sh"],
                   "S": res_a["S"], "reading": res_a["reading"]}
        ok(verify_first(first) == 6, "the store's six files verify by size and SHA-256")
        checks = replay(os.path.join(tmp, "replay"), first, figures)
        ok(all(checks.values()) and len(checks) == 5 and not os.path.exists(os.path.join(tmp, "replay")),
           "G-REPLAY passes 5 of 5 on a faithful store, and leaves no copy behind")
        with open(store["members"], "r+b") as fh:
            b0 = fh.read(1)
            fh.seek(0)
            fh.write(b"9" if b0 != b"9" else b"8")
        try:
            verify_first(first)
            caught = False
        except AssertionError:
            caught = True
        ok(caught, "a store file with one byte changed fails verify (negative control)")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    # the projection, both looks at the first look's rates, against the Architect's independent 80-digit figures
    g = tz23.gate_constants(2 * FIRST_FIGURES["V"], 2 * FIRST_FIGURES["sh"])
    ok(abs(g["thr"] - D("623389.475150266978894322547225")) < D("1e-20"),
       "at twice the first look's V the threshold is 623,389.475150, the Architect's figure")
    ok(D("0.0024120") < g["thr_per_share"] < D("0.0024121") and D("0.0025879") < g["no_earn_per_share"] <
       D("0.0025880") and 2 * g["thr_per_share"] < tz23.DELTA,
       "at the first look's rates EARN needs 0.2412 c a share and NO EARN 0.2588 c: UNDECIDABLE cannot occur")
    ok(D("0.9998") < g["power"] < D("0.9999"), "the projected power is 0.99983")
    g1 = tz23.gate_constants(FIRST_FIGURES["V"], FIRST_FIGURES["sh"])
    ok(g1["earn_at"] == D("432484.391198789259040750892225374110125738788601942422313849"),
       "the first look's own EARN bound is TZ-23's, to every printed digit")
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
            refused.append("tz29")
        except RuntimeError:
            refused.append("tz23")
        except OSError:
            refused.append("not refused")
    ok(refused == ["tz29", "tz29", "tz23"], "opens under the pair book's root and of the archive's ledger outside "
                                            "mode archive are refused by this hook, under the chain book's root by "
                                            "TZ-23's, each before it happens")
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
       policy("archive", "open", (ARCHIVE_LEDGER, "ab", os.O_WRONLY)) is not None and
       policy("archive", "open", (ARCHIVE_STATE + "/archive.log", "rb", 0)) is not None and
       policy("archive", "os.listdir", (ARCHIVE_STATE,)) is not None,
       "mode archive reads ledger.jsonl and nothing else of the archive's state, and writes nothing there")
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
        sys.exit("usage: tz29-maker-m0-second-look.py MODE [ARG...]")
    mode, rest = argv[0], argv[1:]
    assert os.getcwd() == WORK, "run from %s, not %s" % (WORK, os.getcwd())
    MODE[0] = mode
    table = {"fingerprint": mode_fingerprint, "selftest": mode_selftest, "still": mode_still,
             "archive": mode_archive, "rehearse": mode_rehearse, "replay": mode_replay, "fetch": mode_fetch,
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
