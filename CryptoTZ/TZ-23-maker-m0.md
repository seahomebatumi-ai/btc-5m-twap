# TZ-23 — M0: do the makers earn?

**Canonical filename:** `TZ-23-maker-m0.md`. The committed file takes this name and no other.

**Executor model: Opus.** Reads of the venue over the network, a gate's arithmetic, and the first label read
of a set no one has scored.

**Required System Map revision:** `2026-10-05-a`.

**Required anchors**, from map §0. A mismatch on any one is BLOCKED before any work:

| anchor | required |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `0f6c90451cbd` |
| `A6` — pricer | `729f0bcdbee3` |

**Host gate:** §0.2. This TZ runs on the capture host for its interpreter and its network, and reads
nothing of either capture.

**When:** no earlier than **2026-10-06 01:00 UTC**. If every candidate qualifies, the set's last member opens
at 23:10 UTC on 2026-10-05; the walk itself stops BLOCKED before any market younger than `3,900` s (§1).

**What this TZ is.** The maker track's first step, CANON PART II's M0. Over the first 4,032 qualifying
five-minute markets that no TZ has scored, it asks whether the makers — whoever sold to or bought from the
takers — earned, at settlement and with the 20% rebate, on the fills inside `[T0, T0 + 240)`. One statistic,
`S`, the makers' summed result; two answers, **EARN** and **NO EARN**, each read from its own bound at a
false-reading probability of `0.005` fixed here; **UNDECIDABLE** between them. The bound is Ville's inequality
on the martingale the outcomes make of `S`: it holds whatever the outcomes' probabilities and their dependence,
and at any later look that extends the same sum. No pricer, no `sigma`, no capture — the venue's public
documents and fills, read through one instrument, `research/tz23-maker-m0.py`, Appendix A.

---

## 0. Gates

### 0.0 The work tree, first

After contract §1 steps 1 and 2, and before anything else:

```
mkdir /root/tz23-work /root/tz23-work/logs; echo "exit=$?"
```

`exit=0` proves neither existed; anything else is BLOCKED. **From here every command's output goes to
`/root/tz23-work/logs/`, one file per step, §0's included**, and nothing to the session's scratchpad. The one
exception is B-RECLAIM-OWN, §9.

### 0.1 Fingerprint

Contract §1 steps 3 and 4, against `SYSTEM-MAP.md` at `main` after contract §1's pull: revision string
`2026-10-05-a`; the six anchors above, `A2`, `A4`, `A5` and `A6` re-derived as the first 12 hex characters of
those files' SHA-256; the §0 table's **32** rows hashed in lines, bytes and SHA-256 — **29** `frozen` rows equal
to the map, **2** `tracked` and **1** `reported` row printed. Any mismatch is BLOCKED.

### 0.2 Host gate

From `/root/btc-5m-twap`, with `S` first set to this session's scratchpad directory as the session's own
environment names it, output verbatim into `logs/01-host-gate.log`:

```
date -u; date -u +%s
nproc; grep -E '^(MemTotal|MemAvailable|SwapTotal|SwapFree):' /proc/meminfo
df -B1 --output=source,size,avail /var/lib/btc-recorder
find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
grep -c e3975b5da44c5328adf3bf3914634cd878842c73 /var/lib/btc-recorder/runtime.jsonl
systemctl is-active btc-recorder.service btc-chainbook.service; echo "exit=$?"
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
systemctl is-active telemetry-watch.service; echo "exit=$?"
git -C /root/btc-recorder-svc rev-parse HEAD
for d in /root/tz21-work /root/tz18a-svc /root/btc-recorder-svc; do test -e "$d"; echo "$d exit=$?"; done
find /root/btc-forensics -type f | wc -l
/root/tz04a-env/venv/bin/python -c 'import sys; print(sys.version.split()[0])'
git worktree list
du -sb /root/.claude /root/PROJECT_GAMING_PS5
echo "$S"; ls -la "$(dirname "$(dirname "$S")")"
```

- **H1** — `find` prints exactly one path.
- **H2** — `df` names source `/dev/vda2` and size `31612203008`; `grep -c` prints at least `1`, the recorder's
  own record of TZ-21's restart. With H1 this is map §6's host identity.
- **H3** — the interpreter prints `3.12.`.
- **Memory gate** — `MemAvailable` at least `147,152,896` bytes (§0.3).
- **Disk gate** — `avail` at least `2,400,000,000` bytes (§0.3).

Any of these five failing is BLOCKED. **The rest is printed and carries no threshold:** this TZ needs neither
capture unit, and G-STILL reads both (§4.4); `telemetry-watch.service`'s two states, on which map §6's headroom
is conditional; the recorder's tree, which map §6 puts at `e3975b5…`; the three trees; the forensic store's
count, map §3's `1,519`; the worktrees; `du`; and the listing of `S`'s parent, whose UUID directories `I scratch`
names live or earlier (§9).

### 0.3 Resource floors, in exact bytes

**Disk.** `/dev/vda2` free at least **`2,400,000,000`** bytes: the chain book's own floor, `RESOURCE_FLOOR` =
`2,200,000,000` (`research/tz18a-chainbook-capture.py` line 79), plus `200,000,000` for this session. A copy of
this instrument pointed at the 576 weekday markets of 2026-09-02/04 wrote `12,646,213` bytes — the chunk cache
`6,017,400`, the fills file `5,966,081`, the members file `331,990`, the set file `330,742` — so about
`88,530,000` at 4,032 at weekday volume; the rehearsal about `2,300,000`; the branch worktree about `4,600,000`;
the logs under `2,000,000`: the tree at most about `97,500,000`. §9 then copies into the forensic store, where they
stay, the files the report names by hash — the fills file, about `41,800,000` bytes, the set, members, constants,
scored and reading files, the rehearsal's, and the logs: about `49,000,000` bytes, so the session's peak is about
`146,500,000`.

**Memory.** `MemAvailable` at least **`147,152,896`** bytes: twice the largest peak any mode reached in the
Architect's runs under Python 3.12.3 — `rebate` over 64 weekday markets, `73,576,448` bytes. `fetch`, `constants`
and `score` together reached `64,159,744` over 576 weekday markets at two workers, in a copy of this instrument
pointed at that span; Appendix A's own `rehearse` reached `54,509,568` on 2026-10-09, and its `selftest`
`25,825,280`. The instrument fixes glibc's mmap threshold at 128 KiB and its arenas
at two (`_malloc_tune`): without it the same fetch at two workers held `92.7` MiB after 140 weekday markets and
`111.3` MiB after 288, and grew with every chunk; with it, `56.2` MiB after 288 — each as `ru_maxrss` printed it,
to a tenth of a MiB. **`rehearse`, `fetch`, `constants` and `rebate` assert at their start that glibc took both
settings, re-read `MemAvailable`, and stop BLOCKED on either.** Map §6 records the host's memory: `1,002,127,360`
bytes in all, one processor; TZ-21 read `265,342,976` to `370,880,512` available with its session open. Every
mode runs under `nice -n 19`.

### 0.4 Refs

`git ls-remote origin` before the branch of §3.1 exists, every ref reported. Map §1 records `main` at
`e1095b44d3d1391f9f352ad11f1356e7b1678d1d`, PR #22's merge, `main` the only branch, and **26** ref lines. The
upload that carries revision `2026-10-05-a` and this TZ sits above it, in one commit or more; every commit on
`main`'s first-parent line above `e1095b4` is reported with the paths it changed. A difference is recorded, not
BLOCKING, unless `main` does not carry revision `2026-10-05-a` or `refs/heads/tz-23-maker-m0` already exists —
either is BLOCKED.

---

## 1. Why this TZ exists

**The question** — CANON PART II, the maker track. Taking a quote and paying the fee lost at four horizons of
five (CANON §1.5). A resting quote pays no fee, collects a fifth of the taker's fee as rebate, and is filled
only when a taker crosses it. Whether that side of the book earns is a property of the market, measurable on
the venue's public record of fills, with no pricer and nothing of the capture.

**The record — read by the Architect on 2026-10-05 and 2026-10-09 from markets this TZ never scores (data
hygiene, below):**

1. `GET https://data-api.polymarket.com/v2/trades` serves a market's fills. With `taker_only=true` each fill is
   served once, on its taker side: one row per taker order and transaction, `size` its shares and `price` the
   size-weighted mean of the prices it filled at. On the excluded market `1791050100`: 1,082 taker rows over
   1,082 transactions, and with `taker_only=false` the maker rows of each transaction sum to its taker row's
   size at 1,082 of 1,082.
2. **The cursor carries no filter.** `next_cursor` encodes a page size and a `(block timestamp, sequence)`
   anchor and nothing else; sent alone it continues the venue-wide feed — 270 markets on the second page. Every
   request therefore re-sends `condition` and `taker_only` beside the cursor, and every row is asserted to
   belong to the requested markets and to carry its market's token for its outcome. Sent so, 20 excluded
   markets' rows equal the v1 `/trades` rows by offset paging: 23,588 of 23,588 taker rows and 71,908 of 71,908
   with maker rows.
3. At most 20 condition ids a request and 1,000 rows a page; `/v2/trades` takes 300 requests in 10 s and gamma
   `/markets` 300 (the venue's rate-limit page). v1 is retired on 2026-10-24 and its offset stops at 10,000 rows,
   so this TZ reads v2 alone. Rows under 0.01 share are never served (`filter_amount`).
4. Gamma `/markets?slug=…&closed=true` returns up to twenty five-minute documents in one request; `closed`
   defaults to `false` since 2026-04-09. The edge refuses Python's default agent (CANON §1.1): every request
   carries `User-Agent: btc-5m-twap-m0/TZ-23` and `Accept: application/json`, and nothing else.

**The venue's terms, re-read 2026-10-09** (map §7 item 87's rule): taker fee `C × 0.07 × p × (1 − p)`, makers none;
the maker rebate is 20% of each market's taker fees, paid daily and fee-curve weighted — each filled maker order
earns the pool in proportion to `C × 0.07 × p × (1 − p)` at its own price. A member's document must carry
`feeSchedule` `{exponent 1, rate 0.07, takerOnly true, rebateRate 0.2}` and `feeType` `crypto_fees_v2`. The taker
delay has been 150 ms since **2026-09-04 14:00 UTC**, the changelog's own instant; the changelog records no fee,
rebate or delay change after it, and its one later entry that touches `/v2/trades`, of 2026-10-07, changes requests
that carry `user`, which this TZ never sends. Liquidity rewards, a separate programme with no rate in the documents
(map §6), are not counted.

**The makers' result.** For a taker fill of `s` shares at `p`, the makers' side in Up shares is `(x, π)`: a taker
buying Up leaves makers short `s` Up at `p`; selling Up, long `s` at `p`; buying Down at `p`, long `s` Up at
`1 − p`, whether the makers sold Down or bought Up; selling Down, short `s` Up at `1 − p` (`maker_terms`). On a
member `m` the makers' net position over the window is `X_m = Σ x`, its cost `C_m = Σ x π`, the rebate
`R_m = Σ 0.014 s p (1 − p)`, and the result at settlement `X_m · up_m − C_m + R_m`, `up_m` the venue's resolved
outcome, 1 Up and 0 Down. Before the rebate it is exactly minus the takers' result on the same fills before the
taker's fee. **Two approximations, both measured** on 64 excluded weekday markets by this instrument's `rebate`
mode: a row's price is its fills' mean and `p (1 − p)` is concave, so the rebate counted can only exceed the
venue's — by `0.014%` of it there; and a taker row's size and the sum of the maker rows served for it differ at 6
of 90,509 transactions there, by `0.050340` shares in all. §3.7 measures both on 64 members.

**The window, `[T0, T0 + 240)`**, by block time. The Student pricer's domain ends at `tau = 60` (CANON §1.2),
and the final minute is the settlement average, where a quote meets takers who watch the reading form. Fills
before `T0`, in the final minute and after the close are counted by band and judged by nothing.

**The set.** The first **4,032** qualifying markets — fourteen days of 288 — walking `T0` from **`1788530400`**,
2026-09-04 14:00:00 UTC, the instant the taker delay became 150 ms, in steps of 300, past three spans no one
may test on:

- **`1788998400` … `1790452200`**, 2026-09-10 00:00 to 09-26 19:50 UTC: every market whose outcome a TZ has
  read — TZ-17's 601 settled five-minute documents from `1788998400` to `1789178400` (map §2.5), whose report
  prints every boundary's price to beat, and TZ-04b to TZ-16a from `1789033800` (map §2.3); test 3 and TZ-16a's
  set are never a test set again;
- **`1791050100` … `1791097800`**: the 144 markets of 2026-10-03/04 that framed M0 (CANON PART II), read
  again by the Architect on 2026-10-05 and 2026-10-09 for the rehearsal, and the 16 documents after them that an
  earlier rehearsal request carried;
- **`1788350400` … `1788524100`**: the 580 slots of 2026-09-02 12:00 to 09-04 13:55 UTC, before the 150 ms
  delay, whose documents the Architect requested and whose 576 members' fills he read to project the variance and
  measure time and memory.

A candidate qualifies when its document is served closed, with `outcomes` `["Up", "Down"]`, `outcomePrices` one of
the two resolved forms, the fee schedule above, `eventStartTime` its own `T0`, and two token ids (`qualify`,
label-free: which resolved form it is is not read). **If every candidate qualifies**, the set is 1,560 markets from
`1788530400` to `1788998100`, 1,992 from `1790452500` to `1791049800` and 480 from `1791098100` to `1791241800`,
2026-10-05 23:10 UTC — 1,329 of them on a weekend — and its member list's SHA-256 is
`699cab9aa3f540b6cdfe2ae8a295b1fa4bca96921238106dad4b243bc4ecce4f`, recorded and asserted by nothing. `constants`
prints the members by the number of excluded spans ending below each, so the three segments read `1`, `2` and `3`:
`1: 1560, 2: 1992, 3: 480` if every candidate qualifies. The walk requests no document after the 4,032nd member, and
stops BLOCKED before a market younger than `3,900` s or after 2,016 non-members.

**The test.** Order the members by `T0` and let `G_m` be everything public at `T0_m + 240`. `X_m`, `C_m` and
`R_m` are known at `G_m`; `up_m` is fixed by the reading at `T0_m + 300` and known at `G_(m+1)`. Given `G_m`,
member `m`'s result takes one of two values `|X_m|` apart. So with `q_m = P(up_m = 1 | G_m)` the terms
`D_m = X_m (up_m − q_m)` are martingale differences, each confined to an interval of length `|X_m|`, and
`S = M + A` with `M = Σ D_m` and `A = Σ (X_m q_m − C_m + R_m)`, the makers' result expected at each window's end.
Hoeffding's lemma makes `exp(λ M_n − λ² V_n / 8)`, `V_n = Σ X_m²`, a supermartingale for any fixed `λ`, and Ville's
inequality bounds by `α` the probability that it ever reaches `1/α`. With `L = ln(1/α)` and
**`thr = L/λ + λ V/8`**:

- **EARN** — `S >= thr`. If `A <= 0` — the makers did not earn, given what was public at each window's end — this
  has probability at most `α`.
- **NO EARN** — `S <= δ · Sh − thr`, `Sh` the window's shares. If `A >= δ · Sh`, this has probability at most `α`.
- **UNDECIDABLE** — neither.

**`α = 0.005`** for each answer. **`δ = 0.005`** USDC a share: half the venue's 0.01 tick (map §6), what a maker at
the touch takes from a taker who crosses a one-tick book, before adverse selection. **`λ = 0.000021932`**, fixed now
as `sqrt(8 L / V̂)` with `V̂ = 88,119,062,784.574`, the `V` projected for 4,032 members in the set's own weekend
share, `(1,329 × 2,140,569,358.582178867947 + 2,703 × 3,642,000,874.370305971585) / 144`: the first figure from the
144 weekend markets of 2026-10-03/04, the second from the first 144 of 2026-09-02, 12:00 to 23:55 UTC, a Wednesday.
At `V = V̂` the threshold is Hoeffding's `sqrt(V L / 2)`; at `2 V̂` or `V̂ / 2` it is 6.1% above it. All 576 weekday
markets of the third span give a `V̂` 14% lower, `75,762,364,118.653`, where this `λ`'s threshold is 0.29% above
Hoeffding's. **The bound assumes no independence between outcomes, no calibration and no distribution** — only that
each member's outcome is fixed before the next member's window closes, and is one of two values.

**Power**, before any label and deciding nothing: under a normal approximation at the largest variance the
outcomes allow, `V/4`, each answer is read with probability `Φ((δ · Sh − thr) / (sqrt(V) / 2))` against the other's
alternative. At the projection `thr / Sh` is `0.307` c a share and the power `0.979`; from all 576 weekday markets
`0.307` c and `0.980`; on weekend volume alone it would be `0.76`.

**A second look costs no error.** Ville's bound holds at every `n`, so a later TZ may extend the same sum over
the next qualifying markets after this set's last member, with this `α`, `λ` and `δ`, and each answer's
false-reading probability over every look together stays at most `0.005`.

**What this TZ decides.**

1. **The instrument**, `research/tz23-maker-m0.py`, on the branch `tz-23-maker-m0`; `main` carries it once the
   Boss merges after the verdict.
2. **The set, formed and fetched; its constants, label-free, on disk with their SHA-256 in `state.json`; the
   instrument's commit on `origin`** — and only then the labels, read once.
3. **The reading is M0's.** EARN is CANON PART II's M0 PASS: M1 may be written. NO EARN closes the maker track
   for this window. UNDECIDABLE opens the second look.
4. **Nothing on the host is touched** but this TZ's tree, the forensic store by exclusive create, and the
   directories earlier sessions left (§9).

**Data hygiene.** The Architect read the 144 markets of 2026-10-03/04 — fills by both feeds of v1 and v2, and
outcomes — on 2026-10-05 and again on 2026-10-09, and 16 documents after them; the documents of the 580 slots of
2026-09-02/04 and their 576 members' fills; and, measuring the cursor, pages of the venue-wide feed near 2026-10-03
17:55–19:30 UTC, printed as counts of rows and markets and never kept. **No member of the set was read.** The
rehearsal reads the 2026-10-03/04 span alone, and §2 bars any read of a member outside the instrument.

---

## 2. Scope

**Repository paths this TZ may write, and no others:**

1. `research/tz23-maker-m0.py` — new, byte for byte Appendix A's, on branch `tz-23-maker-m0`, then a pull
   request. Not merged by the Executor.
2. `CryptoReports/TZ-23-maker-m0-report.md` — straight to `main`, in one commit. **The one path pushed to
   `main`, and the exemption to item 5 below.**

**Host paths this TZ may write:** `/root/tz23-work/**`; `/root/btc-forensics/`, by exclusive create only (§9); and
in the primary checkout `/root/btc-5m-twap`, its `.git` for the branch and the worktree, and its `CryptoReports/`
for the report.
**Host paths it removes, under §9 and nothing else:** `/root/tz23-work/` with its worktree, and the directories
`I scratch` names earlier.

**Prohibited, each absolutely:**

1. No committed file is modified; every `frozen` row of map §0 is byte-identical at run end.
2. **Nothing under `/var/lib/btc-recorder/` or `/var/lib/btc-chainbook/` is opened or listed** — by the instrument,
   whose audit hook refuses any open there, or by any command of this TZ but §0.2's `df`, `find` and `grep -c`, the
   host's identity, at both of its runs, and B-RECLAIM-OWN's `df`.
3. No unit is signalled, started, stopped, enabled, disabled or changed. `systemctl show` and `is-active` are
   this TZ's only reads of either.
4. `/root/tz04a-env/`, `/root/tz01-env/`, `/root/tz18a-svc/` and `/root/btc-recorder-svc/` are not modified, and
   `/root/btc-forensics/` only by §9's exclusive create.
5. Nothing is pushed to `main` except the report of item 2.
6. **No label is read before §3.6's constants are on disk with their SHA-256 in `state.json` and the instrument's
   commit is on `origin`.** A label is the outcome a member's `outcomePrices` states. Three exemptions, each named
   because the body requires it: (a) `qualify`, which asks only whether `outcomePrices` is one of the two resolved
   forms, and `fetch`, `constants` and `rebate`, which carry each member's document in `set.json`, `outcomePrices`
   with it, and never interpret it — the self-test asserts the constants file byte-identical with every label
   flipped; (b) `rehearse`, which reads the labels of the excluded 2026-10-03/04 span; (c) `score`, which reads the
   members' labels once a run, its determinism run included, each run a line in the ledger.
7. **Requests:** `gamma-api.polymarket.com/markets` and `data-api.polymarket.com/v2/trades`, through the
   instrument's `http_json` and its two headers; `git` against `origin`; and `gh` for the pull request alone. No
   other request — no CLOB, no websocket, no authenticated call — and **no read of any member's document or fills
   by any command but the instrument's modes**, `set.json` and the cache included.
8. **No single fill's, member's or market's price, size or outcome is printed or written outside
   `/root/tz23-work/`**: the instrument prints sums over a set, and the report quotes them. The one exemption is
   §9's byte-for-byte copies into `/root/btc-forensics/` of the files the report names by hash.
9. No Release is created, and no dataset, archive or binary enters git history.

---

## 3. The work, in this order

`nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz23-work/wt/research/tz23-maker-m0.py` is written `I`; a
mode is `I <mode>`, run from `/root/tz23-work`. Every command's output goes to `logs/`, one file per step, and is
quoted in the report. **§9's B-RECLAIM-SCRATCH runs after §3.3 and before §3.4; B-RECLAIM-OWN runs last, after
§3.10.**

**Where the session's permission classifier refuses a command of a block named B-…**, the Executor prints the
block, the Boss runs it verbatim in a root shell on the VPS, and the Executor verifies it through the reads this
TZ names — never from the Boss's account.

### 3.1 The branch and its file

```
git -C /root/btc-5m-twap fetch origin
git -C /root/btc-5m-twap worktree add -b tz-23-maker-m0 /root/tz23-work/wt origin/main
```

Then extract Appendix A from this TZ as `main` carries it, with this script, verbatim:

```
/root/tz04a-env/venv/bin/python -B - <<'EOF'
import hashlib, os
SRC = "/root/tz23-work/wt/CryptoTZ/TZ-23-maker-m0.md"
WANT = {
    "research/tz23-maker-m0.py": "6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f",
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
    with open(os.path.join("/root/tz23-work/wt", name), "xb") as fh:
        fh.write(data)
    print(name, data.count(b"\n"), len(data), hashlib.sha256(data).hexdigest())
EOF
```

| path | lines | bytes | SHA-256 |
|---|---|---|---|
| `research/tz23-maker-m0.py` | 1,184 | 54,885 | `6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f` |

Commit the file alone on the branch, push it with `git push -u origin tz-23-maker-m0`, and open the pull request
against `main`. A failed assert here is BLOCKED. **The push is what lets §3.8 read a label:** `score` refuses a
`HEAD` that `origin` does not carry.

### 3.2 The self-test

`I selftest` must print `59 of 59 checks passed`. A red self-test stops the run here, and it goes
to §3.10 and §9.

### 3.3 The units, and the directories beside this session

`I still` records both units' `MainPID`, `NRestarts` and `ActiveState` in `state.json` and prints their
`MemoryCurrent` and `MemoryPeak`. Then `I scratch "$(dirname "$S")"` lists every UUID directory beside this
session's own and names each **live** — born from 1 s before to 60 s after the start of a running process whose
`argv[0]` is `claude` or ends in `/claude.exe` — or **earlier**.

### 3.4 The rehearsal — G-REHEARSAL

`I rehearse`: the whole path — the walk, the fetch, the constants and the score — over the 144 markets of
2026-10-03/04, against the Architect's independent figures (§4.1). A FAIL stops the run here, and it goes to §3.10
and §9.

### 3.5 The set — G-SET

`I fetch`, in the background, its output to `logs/`, read until it prints `G-SET PASS` or fails. After its first
30 chunks it projects its own time and stops BLOCKED above `7,200` s. **A network failure is resumable:** the
cache keeps every finished chunk, and `I fetch` may be run again twice, 600 s apart; a third failure is BLOCKED.

### 3.6 The constants, twice

`I constants`, then `I constants` again. The second run must print `unchanged` for the fills, members and
constants files — contract §6's determinism. The constants file's SHA-256 is in `state.json`.

### 3.7 The rebate check

`I rebate`: every 63rd member, 64 in all, read again through both feeds. **Asserted:** each sampled member's taker
rows equal the cache's. **Recorded, not asserted:** the window's transactions, those filled at several prices,
those whose taker size differs from its makers' sum, and the rebate the reported prices give against each
maker's own.

### 3.8 The score, twice

`I score`, then `I score` again. The first reads the labels and prints the reading; the second must print
`unchanged` for the scored and reading files. The ledger then holds two lines.

### 3.9 The units again — G-STILL

`I still`.

### 3.10 The closing reads

§0.2's block again, then:

```
systemctl show btc-recorder.service btc-chainbook.service -p MainPID -p NRestarts -p MemoryCurrent -p MemoryPeak
free -b
du -sb /root/tz23-work /root/.claude
cat /root/tz23-work/state.json /root/tz23-work/label-ledger.jsonl
```

---

## 4. The gates — fixed here, before any of their data exists

| gate | population | PASS | false failure | power, against |
|---|---|---|---|---|
| **G-REHEARSAL** | the 144 markets `1791050100` … `1791093000` | §4.1's 10 figures equal, exactly | `0` — two independent computations of one public record | `1`, any difference in the fetch, a sign, the window, the rebate or a sum |
| **G-SET** | the walk from `1788530400` and the fetch of its members | 4,032 members; every chunk fetched, every row on its market and its token, every chunk read back | `0` | — |
| **M0** | the 4,032 members' fills inside the window | §4.3 | at most `0.005` for each answer, at any look | §1's normal approximation, printed before any label; `0.979` projected |
| **G-STILL** | the two capture units, §3.3 to §3.9 | `MainPID`, `NRestarts` and `ActiveState` unchanged | `0` — systemd read directly | `1`, a restart or a stop |

### 4.1 G-REHEARSAL

Over the 144 markets, the window's fills `n`, shares, `X`, `C`, `R`, `V`, `Σ X · up`, `S`, the members and the Up
outcomes must equal, as values, the Architect's figures, computed from the v1 feed by offset paging with a script
that shares no code with the instrument:

| figure | value |
|---|---|
| members | `144` |
| Up outcomes | `75` |
| `n` | `128,031` |
| shares | `3509409.854401` |
| `X` | `-44336.003951` |
| `C` | `-108894.2181475504884399` |
| `R` | `8015.91427290719561009665372913342` |
| `V` | `2140569358.582178867947` |
| `Σ X · up` | `-88853.166114` |
| `S` | `28056.96630645768404999665372913342` |

They are the instrument's `REF`. The Architect's run of this file printed the same ten, and these hashes — recorded
beside the gate and judged by none: `set.json` `83a53bd3fb13…`, the fills file `3ce50a85f840…`, the members file
`2676af1dee73…`, the scored file `d31eb18fa58f…`.

### 4.2 G-SET

`fetch` prints `G-SET PASS` when the walk has formed 4,032 members, every chunk's feed has ended with no cursor,
every row has belonged to its chunk's markets and carried its market's token for its outcome, and every chunk
reads back to its members in order. Every non-member is listed with its reason by `constants`.

### 4.3 M0's reading

| condition | reading |
|---|---|
| `S >= thr` | **EARN** — whatever the power |
| `S <= δ · Sh − thr` | **NO EARN** — whatever the power |
| otherwise | **UNDECIDABLE** |

Where both hold the reading is EARN, and the report states that half a tick is also rejected; at the projection
they cannot both hold, because `2 thr / Sh` is `0.61` c, above `δ`. **No row reads a power.** The report prints
`S`, its settlement and rebate parts, each per share, both margins, and, barred from every reading, the makers'
result per share in each band of the interval.

**What a reading establishes, and what it does not.** EARN says that on these markets the makers' fills inside the
window were priced in their favour, given what was public at each window's end, beyond what the outcomes' noise
explains. It says nothing about a quote of ours: its queue position, its share of the fills, the adverse selection
it would meet and the 150 ms delay are M1's (CANON PART II). NO EARN says the makers kept less than half a tick a
share there, rebate included.

### 4.4 G-STILL

From §3.3 to §3.9 both units keep their `MainPID`, `NRestarts` and `ActiveState`. **This TZ signals nothing**, so a
FAIL runs no block: the report carries it, with both units' memory at both reads, for TZ-22.

---

## 5. The instrument

`research/tz23-maker-m0.py`, Appendix A, fixed by the Architect as this TZ's Validation and written byte for byte.
Standard library only, run under the recorder's interpreter. One mode a run; each prints its findings with UTC
stamps, its peak memory, whether glibc took its two settings, and its count of opens under the capture roots, which
its audit hook refuses. The four that read the venue or the cache stop BLOCKED at their start if glibc did not take
both settings or `MemAvailable` is below §0.3's floor. It writes under `/root/tz23-work/` and, in `reclaim`, new
files in `/root/btc-forensics/` by exclusive create. Every number of the venue is parsed as the `Decimal` of its own
text, and every sum is exact at 60 digits. Exit `0` is every assert held; exit `1` a failed assert, named, or a
BLOCK whose message says so. Run with `-O` it refuses to start.

---

## 6. Cost

Measured in the Architect's runs under Python 3.12.3 on two cores of an Intel Xeon at 2.80 GHz — the host has one
(TZ-21's `nproc`) — and taken at the population's upper bound: all 4,032 members at the weekday markets' `1,707`
rows a market, `6,882,267` rows, at most `7,084` pages of 1,000 over 202 chunks. The fetch waits on the venue, not
the processor, and the venue's latency moved threefold between runs: the 144 weekend markets' `165,315` rows, at
least 170 pages, took 21 s on 2026-10-05 and 61, 25, 24 and 37 s on 2026-10-09; the 576 weekday markets' `983,181`
rows took 184 s on 2026-10-05.

| check | population | measured | bound |
|---|---|---|---|
| `fetch`, wall | 202 gamma requests and at most 7,084 pages | at most `0.359` s a page and `0.363` s a gamma request, two workers | `2,620` s; **projected after its first 30 chunks, BLOCKED above `7,200` s** |
| `fetch`, `constants` twice and `score`, processor | 6,882,267 rows, parsed once and summed three times | `8.3` s for the rehearsal's 165,315 rows, the whole path once | `700` s; `2,100` on a host three times slower |
| `rebate` | 64 members, both feeds | `297.4` s for 64 weekday members on 2026-10-05 | `900` s; about `580` at the slowest latency |
| `rehearse` | 144 markets, fixed | `25` to `66` s over five runs | `120` s |
| `score` | the members file, 4,032 lines | under 1 s | `15` s a run |
| `selftest`, `still`, `scratch`, each `reclaim` | — | under 1 s each | `30` s a run |

**Wall clock at those bounds at most about `6,000` s, of which the processor's at most about `2,250` on a host
three times slower; every second at `nice 19`.** The fetch's fail-fast bound, `7,200` s, is its own bound, `2,620`,
at a venue `2.75` times slower than at its slowest measured run; slower still, the session would hold the host for
over two hours, and it stops BLOCKED.

---

## 7. Validation

| # | check | count |
|---|---|---|
| **V1** | §0.1's fingerprint | 6 anchors, 4 re-derived, 29 of 29 `frozen` equal |
| **V2** | §0.2's host gate | H1 to H3, the memory and the disk gate; the rest printed |
| **V3** | §3.1's file | 1 of 1 hash asserted, lines and bytes; the branch's diff against `origin/main` names exactly one path, `A`, 1,184 lines |
| **V4** | the self-test | `59 of 59` |
| **V5** | G-REHEARSAL | 10 of 10 figures equal |
| **V6** | G-SET | 4,032 members; the candidates considered; every non-member with its reason; the members by segment |
| **V7** | the constants, twice | 3 of 3 files `unchanged` at the second run |
| **V8** | the rebate check | 64 of 64 sampled members' taker rows equal to the cache; the four recorded figures |
| **V9** | the score, twice | the reading; 2 of 2 files `unchanged`; 2 ledger lines |
| **V10** | G-STILL | both units unchanged, or the change named |
| **V11** | opens under the capture roots | `0` printed by every mode |
| **V12** | memory | every mode's printed peak, against §0.3's floor; `malloc tuned: True` at every mode |
| **V13** | contract §4.2's self-check | run after the push and the pull request and before the report's commit |
| **V14** | §3.10's closing reads | every read printed |
| **V15** | §9's `reclaim` runs | files considered, named by a report, kept by name, copied and already held; the store's count after equal to before plus the copies |
| **V16** | §9's removals | `git worktree remove` without `--force` exit `0`; `test -e` exit `1` for `/root/tz23-work` and each directory removed; `git worktree list` naming `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else |

---

## 8. The report

`CryptoReports/TZ-23-maker-m0-report.md`, in contract §8's order. Beyond what V1 to V16 print: the set — candidates
considered, members, the first and last member, the members by segment and by weekend, **every non-member with its
reason**, the member list's SHA-256 and the set file's; the window's fills, shares, `X`, `C`, `R`, `V`; the
threshold, both per share, and the power; **the reading** with `S`, its two parts and both margins; the band
figures, barred; the rebate check; both ledger lines; both units at both reads, memory included; every block the
classifier refused, who ran it and when; §9's counts and removals; every free-space and `MemAvailable` read with its
instant and bound; and every file the run wrote, by SHA-256, but the two chunk caches — the set's 202 files and the
rehearsal's 8 — which §9 lets go with the tree. **The report is drafted in the primary checkout `/root/btc-5m-twap`
before B-RECLAIM-OWN and committed after it**, so the removal of this TZ's tree is in it.

---

## 9. Reclaim — the host left clean (CANON hard rule 15)

**What a file is kept for:** a committed report prints its SHA-256, whole or as a prefix of 16 to 64 hex
characters, or it is kept by name: `state.json`, `label-ledger.jsonl` and every file under `logs/`. `reclaim`
copies each into `/root/btc-forensics/` as `<tree>--<path with / as -->`, by exclusive create, and verifies its
hash; a name already there with the same hash is counted as held, and with another hash is a failed assert. The
branch worktree is not copied: `reclaim` asserts that `git status --porcelain --ignored` in it prints nothing and
that its `HEAD` is its upstream's, so `git worktree remove` needs no `--force`. The chunk cache is not named — the
fills file holds its rows — and goes with the tree.

**B-RECLAIM-SCRATCH**, after §3.3 and before §3.4, for every directory `I scratch` named **earlier** — none it
named live, and never this session's own:

```
I reclaim <each earlier directory, by its full path>
rm -rf <one such directory>; echo "exit=$?"
test -e <that directory>; echo "exit=$?"
```

`reclaim` refuses a directory born from 1 s before to 60 s after a running claude process started, and any path
but `/root/tz23-work` that is not a UUID directory under `/tmp/` whose parent's name carries `btc-5m-twap`; it prints
`RECLAIM PASS` before any removal. If `I scratch` names none earlier, the block is recorded as
empty and skipped.

**B-RECLAIM-OWN**, last, after §3.10 and with the report drafted. **Its output is written to no file**, and the
Executor quotes it from the session:

```
I reclaim /root/tz23-work
git -C /root/btc-5m-twap worktree remove /root/tz23-work/wt; echo "exit=$?"
rm -rf /root/tz23-work; echo "exit=$?"
test -e /root/tz23-work; echo "exit=$?"
git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
find /root/btc-forensics -type f | wc -l
df -B1 --output=source,size,avail /var/lib/btc-recorder
```

The branch `tz-23-maker-m0` stays on `origin` and as a local ref; only its working tree goes.
`/root/btc-recorder-svc` and `/root/tz18a-svc` are the two units' code, and the capture and the forensic store are
data, never scratch. **A refused `rm -rf` is handed to the Boss** by §3's route, one tree per command, and verified
by `test -e`.

---

## 10. Pre-send checks

Performed by the Architect on 2026-10-09 against this file as sent, in a reading separate from its writing, with
the repository at `origin/main` `e1095b44d3d1391f9f352ad11f1356e7b1678d1d` and map revision `2026-10-05-a` as it
ships with this TZ.

| # | check | result |
|---|---|---|
| **C1** | scope against body | **Repository paths the body names, 5:** `CryptoTZ/TZ-23-maker-m0.md` and `SYSTEM-MAP.md`, read; `research/tz18a-chainbook-capture.py`, cited and not opened; `research/tz23-maker-m0.py`, written on the branch; `CryptoReports/TZ-23-maker-m0-report.md`, written to `main`. **By reference, read and never written:** the files of the four re-derived anchors and the map's 32 rows. **Entry points:** Appendix A's nine modes, §3.1's extraction script, `git` and `gh`. **Outputs:** `logs/`, `state.json`, `label-ledger.jsonl`, the rehearsal's and the set's `set.json`, chunk cache, fills, members, constants, scored and reading files, the self-test's transient tree, the forensic store's copies, the report, the branch and the pull request. **Intersections with §2, by path and by content class, 6, each now named in §2:** the report on `main`, item 5's exemption; `set.json` carries every member's settled document, `outcomePrices` with it, before any label may be read — item 6 (a), with the self-test's proof that the constants ignore it; the scored and reading files carry labels — item 6 (c); §9's copies put single members' prices, sizes and outcomes in `/root/btc-forensics/` — item 8's exemption; the pull request is a request to GitHub — item 7 names `gh`; §0.2's and B-RECLAIM-OWN's `df` and §0.2's `find` and `grep -c` touch a capture root — item 2 names all four. The primary checkout's `.git` and `CryptoReports/` are written — §2's host paths name both. |
| **C2** | origin of every expectation | **§5 holds no numeric expectation. §7's, by kind:** quoted from a committed artifact — V1's 6, 4, 29, 2 and 1 from map §0 and V16's two worktrees from map §3, revision `2026-10-05-a`; V2's `/dev/vda2`, `31612203008` and `147,152,896` from map §6, and `2,400,000,000` from `research/tz18a-chainbook-capture.py` line 79 plus the session's footprint, derived in §0.3 from the instrument's measured writes that map §6's disk row records; V4's `59` and V6's `4,032` from Appendix A, fixed by its code and by nothing this TZ measures. Computed by an implementation independent of the one under test — V3's SHA-256, `1,184` lines and `54,885` bytes, by `sha256sum` and `wc` over Appendix A, exact; V5's ten figures by the Architect's v1 reference script, which shares no code with the instrument, in exact `Decimal`; the self-test's projection checks, by the Architect's 60-digit computation: `thr / Sh` `0.0030727…` against the band `0.0030` to `0.0031`, power `0.97941…` against `0.97` to `0.99`, the threshold within `1.7e-12` relative of Hoeffding's against `1e-6`. V7's 3, V8's 64, V9's 2 and 2 and V11's 0 are counts of §3's own runs and files. **No expectation depends on a quantity this TZ measures:** M0's thresholds are computed by the instrument from the measured `V` and `Sh`, and judged against `S` alone. |
| **C3** | shape of every diff | One path: `research/tz23-maker-m0.py`, new. `git cat-file -e origin/main:research/tz23-maker-m0.py` at `e1095b4` exits `128`: the path does not exist, so the change replaces **none** of `origin/main`'s lines. The words "insertions only" appear nowhere in this TZ. |
| **C4** | cost of every check | §6, at the population's upper bound: every member at the weekday rate, `6,882,267` rows, at most `7,084` pages. `fetch` wall `2,620` s at the slowest measured `0.359` s a page and `0.363` s a gamma request; the whole path's processor `700` s, `2,100` on a host three times slower; `rebate` `900` s; `rehearse` `120` s; `score` `15` s a run; the rest `30` s a run. Wall clock at most about `6,000` s; **single-session processor at most about `2,250` s, under `3,600`, so nothing is sampled**. The one fail-fast bound, `7,200` s, is `2,620` s times `2.75`, derived in §6 from the same figures. |
| **C5** | every count | The set, over the walk from `1788530400` past §1's three spans, re-derived by a dry run of Appendix A's own `candidates` with every candidate qualifying: `1,560` members in `1788530400` … `1788998100`, `1,992` in `1790452500` … `1791049800`, `480` in `1791098100` … `1791241800`, `4,032` in all, `1,329` on a weekend, `202` document requests and `4,032` documents, member list `699cab9a…`. The chunks: `202` = ⌈4,032 / 20⌉ for the set, `8` = ⌈144 / 20⌉ for the rehearsal. V8's `64`: indices `62`, `125`, … `4,031` of the 4,032 members, `(4,031 − 62) / 63 + 1`. V7's `3`: fills, members, constants; V9's `2` files, scored and reading, and `2` ledger lines, one a `score` run. V1's `4` re-derived anchors: `A2`, `A4`, `A5`, `A6`; `32` rows = `29` + `2` + `1`, read from the map. §1's spans: `580` slots in `1788350400` … `1788524100`, `16` documents in `1791093300` … `1791097800`, `144` markets in `1791050100` … `1791093000`. |
| **C6** | every population | `S`, its settlement and rebate parts, `X`, `C`, `R`, `V`, `Sh`, `thr`, both margins and the power: the members' fills inside `[T0, T0 + 240)`. The band figures: the members' fills by band, all of them. The weekend count and the segments: the members. The non-members and their reasons: the candidates considered. The rebate check's four figures: the 64 sampled members' window transactions with exactly one taker row. G-REHEARSAL's ten: the 144 markets of 2026-10-03/04, their window fills. `V̂` and `Ŝh`: 144 weekend markets of 2026-10-03/04 and 144 weekday markets of 2026-09-02, in the set's weekend share; the alternative projection, all 576 weekday markets of 2026-09-02/04 with the same 144 weekend. Each memory peak: one mode's process. `MemAvailable` and free space: the host at each read. G-STILL: the two capture units. |
| **C7** | every signature and every behaviour | **No committed function is called.** The one committed value cited, at `e1095b4`: `research/tz18a-chainbook-capture.py` line 79, `RESOURCE_FLOOR = 2200000000          # section 0.2, 2.0e9 map floor + 2.0e8 write cap`. **Every behaviour this TZ attributes to Appendix A, read against its body, by the extracted file's line numbers:** `score` refuses an unpushed `HEAD` — line 834, `assert "origin/tz-23-maker-m0" in branches`; the four reading modes' preconditions — `floor_check()` at lines 711, 733, 754 and 769, and lines 214 and 217, `assert MALLOC_TUNED` and `assert avail >= MEM_FLOOR`; no document after the need-th member — line 458, `while len(chunk) < min(CHUNK, need - len(members))`, and the walk's two BLOCKs at lines 455 and 461; the projection after 30 fresh chunks — lines 531 and 534; G-SET — line 741, after `trades`' row and token asserts and `member_rows`' order asserts; the rebate check's one assert — line 790; its recorded gap — line 819, "differs from its makers' sum", the wording §1 and §3.7 now use; the constants file label-free — the self-test at line 1136; `still`'s memory print — line 854; `scratch`'s and `reclaim`'s live rule — line 903, `t - 1 <= b <= t + LIVE_S`, and line 947, `s - 1 <= b <= s + LIVE_S`; `reclaim`'s refusal of other paths — lines 933 to 938, the wording §9 now uses; `-O` refused — lines 48 to 50; every mode's last three prints — lines 1177 to 1180. Two sentences were rewritten before sending: §9's refusal, which said "beside this session's", and §1's and §3.7's size gap, which said "exceeds". |
| **C8** | every cross-reference | Resolved by reading the text referenced. **Map `2026-10-05-a`:** §0's anchors and 32 rows, 29 / 2 / 1; §1's `e1095b4` and 26 ref lines; §2.3's reads from `1789033800` and §2.5's TZ-17 documents from `1788998400`; §3's forensic store at `1,519` files and the two worktrees at TZ-21's end; §6's host identity with the `e3975b5` start record, the recorder's tree at `e3975b5`, one processor, `1,002,127,360` bytes and TZ-21's `265,342,976` to `370,880,512`, the headroom's condition on `telemetry-watch.service`, the `0.01` tick, and liquidity rewards without a rate; §7 item 87's re-read rule. **Contract:** §1 steps 1 to 4, §4.2's self-check, §6's determinism, §8's order. **CANON:** §1.1's agent refusal, §1.2's domain to `tau = 60`, §1.5's four closed horizons, PART II's M0 and its exploration rule, hard rule 15. **This TZ:** §0.2 to §0.4, §1, §2 items 2 to 8, §3.1 to §3.10, §4.1 to §4.4, §6, §9 and Appendix A, each supporting the sentence that cites it. **None unresolved.** |

**No check was unperformable in this session**, so none is converted into a BLOCK condition under CANON hard rule 13.
The host's state is read by §0's gates on the host itself.

---

## Appendix A — `research/tz23-maker-m0.py`, byte for byte

Extracted by §3.1's script; the block's content is the file.

```python file=research/tz23-maker-m0.py
#!/usr/bin/env python3
"""TZ-23 - the maker track's first step, M0: do the makers of btc-updown-5m earn, at settlement and
with the 20% rebate, on the fills inside [T0, T0 + 240)?

    selftest          every rule of this file, on literals
    still             both capture units' MainPID and NRestarts: the first run records them, the
                      second compares
    rehearse          the whole path on the Architect's excluded span of 2026-10-03/04, against the
                      Architect's independent figures (G-REHEARSAL)
    fetch             the set - the first 4,032 qualifying markets from 1788530400 - and their
                      taker fills
    constants         label-free: every member's sums, V, the thresholds and the power, on disk
    rebate            label-free: the exact maker rebate of every 63rd member, from both feeds
    score             the labels, read once, and the reading
    scratch           the UUID directories beside this session's own, and which of them a running
                      claude process made
    reclaim TREE...   section 9

It requests gamma-api.polymarket.com and data-api.polymarket.com and nothing else, every request with
the two headers HEADERS fixes. Under /var/lib/btc-recorder and /var/lib/btc-chainbook it opens nothing:
an audit hook refuses any open there. It writes under /root/tz23-work/ and, in `reclaim`, new files in
/root/btc-forensics/ by exclusive create. It prints no price, size or outcome of any single fill or
market; it prints sums over a set. Exit 0: every assert of the mode held. Exit 1: an assert failed, and
its message names it. Run it with the recorder's interpreter, /root/tz04a-env.

Written for CryptoTZ/TZ-23-maker-m0.md. The TZ is the specification.
"""

import concurrent.futures
import datetime
import gzip
import hashlib
import io
import json
import math
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
from decimal import Decimal as D, getcontext

if not __debug__:
    sys.stderr.write("tz23: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(2)

getcontext().prec = 60

# ---- the TZ's constants ------------------------------------------------------------------------

START = 1788530400           # 2026-09-04 14:00:00 UTC: the crypto taker delay is 150 ms from here on
N_SET = 4032                 # two whole weeks of five-minute markets
STEP = 300
CHUNK = 20                   # the most condition ids /v2/trades takes in one request
WINDOW = (0, 240)            # [T0, T0 + 240): the pricer's domain ends at tau = 60
BANDS = (("pre", None, 0), ("w0", 0, 60), ("w1", 60, 120), ("w2", 120, 180), ("w3", 180, 240),
         ("last", 240, 300), ("post", 300, None))
WINDOW_BANDS = ("w0", "w1", "w2", "w3")
EXCLUDED = ((1788998400, 1790452200, "labels read, TZ-04b to TZ-17"),
            (1791050100, 1791097800, "explored 2026-10-03/04"),
            (1788350400, 1788524100, "explored 2026-09-02/04"))
REHEARSAL = (1791050100, 144)
FEE_TYPE = "crypto_fees_v2"
FEE_SCHEDULE = {"exponent": 1, "rate": D("0.07"), "takerOnly": True, "rebateRate": D("0.2")}
REBATE_COEF = D("0.014")     # rebateRate 0.2 times the crypto fee rate 0.07
ALPHA = D("0.005")           # each answer's false-reading probability
DELTA = D("0.005")           # half a tick per share: NO EARN's alternative
LAMBDA = D("0.000021932")    # fixed before any member is read: sqrt(8 ln 200 / V projected)
SAMPLE_EVERY = 63            # the rebate check reads members 62, 125, ... : 64 of 4,032
FETCH_WORKERS = 2
FETCH_BUDGET_S = 7200        # a fetch projected past this after its first 30 chunks is BLOCKED
MEM_FLOOR = 147152896        # MemAvailable below which a mode that reads the venue or the cache stops
RESOLVED_AFTER_S = 3900      # a market younger than this may be unresolved; the walk stops before it
WALK_SLACK = 2016            # the walk considers at most one week of non-members beyond its need
MAX_PAGES = 5000             # a chunk's feed longer than this is BLOCKED
UA = "btc-5m-twap-m0/TZ-23"
HEADERS = {"User-Agent": UA, "Accept": "application/json"}
GAMMA = "https://gamma-api.polymarket.com/markets"
TRADES = "https://data-api.polymarket.com/v2/trades"

# The Architect's independent figures for the rehearsal span: v1 /trades, offset paging, raw pages
# parsed to Decimal by a script that shares no code with this file (TZ-23 section 10, C2).
REF = {
    "members": 144, "ups": 75, "n": 128031,
    "sh": D("3509409.854401"), "X": D("-44336.003951"), "C": D("-108894.2181475504884399"),
    "R": D("8015.91427290719561009665372913342"), "V": D("2140569358.582178867947"),
    "XU": D("-88853.166114"), "S": D("28056.96630645768404999665372913342"),
}

UNITS = {"recorder": "btc-recorder.service", "chainbook": "btc-chainbook.service"}
WORK = "/root/tz23-work"
WT = WORK + "/wt"
STATE = WORK + "/state.json"
LEDGER = WORK + "/label-ledger.jsonl"
PRIMARY = "/root/btc-5m-twap"
REPORTS = PRIMARY + "/CryptoReports"
FORENSICS = "/root/btc-forensics"
CAPTURE_ROOTS = ("/var/lib/btc-recorder", "/var/lib/btc-chainbook")
UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
TOKEN = re.compile(r"[0-9a-f]{16,64}")
CONDITION = re.compile(r"0x[0-9a-f]{64}")
LIVE_S = 60                  # a directory born this soon after a claude process started is that process's

OPENS = []


def _malloc_tune():
    """glibc raises its mmap threshold each time it frees a large block, so the 0.8 MB pages this TZ
    parses would be served from the heap and never returned; fixed at 128 KiB, with two arenas, the
    run's resident peak stays flat (TZ-23 section 0.3). True where both settings took."""
    try:
        import ctypes
        libc = ctypes.CDLL("libc.so.6")
        # mallopt(M_MMAP_THRESHOLD = -3, 128 KiB) and mallopt(M_ARENA_MAX = -8, 2)
        return libc.mallopt(-3, 131072) == 1 and libc.mallopt(-8, 2) == 1
    except (OSError, AttributeError):
        return False


MALLOC_TUNED = _malloc_tune()


def _audit(event, args):
    """No open at all under either capture root."""
    if event != "open" or not args or not isinstance(args[0], str):
        return
    path = os.path.abspath(args[0])
    for root in CAPTURE_ROOTS:
        if path == root or path.startswith(root + "/"):
            OPENS.append(path)
            raise RuntimeError("open refused under a capture root: %s" % path)


sys.addaudithook(_audit)


def out(msg):
    sys.stdout.write("[%s] %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    sys.stdout.flush()


def utc(t):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(t))


def fx(x):
    """A Decimal as fixed-point text, never in exponent form."""
    return format(x, "f")


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
    """The first run writes; a later run must produce the same bytes (determinism, contract §6)."""
    if os.path.exists(path):
        got = sha256_file(path)
        assert got == sha256_bytes(data), "determinism: %s differs from the first run" % path
        out("unchanged %s sha256 %s" % (path, got))
        return got
    write_atomic(path, data)
    return sha256_bytes(data)


def gz_bytes(text):
    """Deterministic gzip: no name, no time."""
    buf = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=buf, mtime=0) as g:
        g.write(text.encode("utf-8"))
    return buf.getvalue()


def dumps(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), default=_dec) + "\n"


def _dec(o):
    if isinstance(o, D):
        return fx(o)
    raise TypeError(type(o))


def mem_available():
    with open("/proc/meminfo", encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("MemAvailable:"):
                return int(line.split()[1]) * 1024
    raise AssertionError("no MemAvailable")


def floor_check():
    """Before a mode that reads the venue or the cache: glibc's two settings, and the memory floor."""
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


# ---- the venue -----------------------------------------------------------------------------------

def http_json(url, tries=8):
    """One GET with HEADERS, parsed with every JSON number as a Decimal of its own text. 429 and 5xx
    and transport errors are retried, honouring Retry-After up to 60 s; anything else is fatal."""
    last = None
    for k in range(tries):
        req = urllib.request.Request(url, headers=HEADERS, method="GET")
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                body = r.read()
                assert r.status == 200, "HTTP %d %s" % (r.status, url)
                return json.loads(body, parse_float=D)
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


def gamma_docs(t0s):
    """The closed market documents of the given five-minute slugs, one request, keyed by slug."""
    q = [("slug", "btc-updown-5m-%d" % t) for t in t0s]
    q += [("closed", "true"), ("limit", str(len(t0s) + 5))]
    docs = http_json(GAMMA + "?" + urllib.parse.urlencode(q))
    assert isinstance(docs, list), "gamma: not a list"
    by = {}
    for d in docs:
        assert d["slug"] not in by, "gamma: slug %s twice" % d["slug"]
        by[d["slug"]] = d
    return by


def trades(cids, taker_only, tokens=None, keep_tx=False):
    """Every row /v2/trades serves for these conditions. The cursor carries no filter, so every
    request re-sends `condition` and `taker_only` beside it (TZ-23 section 1); every row is asserted
    to belong to the requested conditions and, where `tokens` is given, to carry its market's token
    for its outcome. Returns {condition: [row, ...]}; a row is [ts, side, outcome, size, price], or
    with `keep_tx` [ts, side, outcome, size, price, token, transaction, wallet]."""
    assert 1 <= len(cids) <= CHUNK and len(set(cids)) == len(cids)
    by = {c: [] for c in cids}
    cursor, pages = None, 0
    while True:
        q = {"condition": ",".join(cids), "limit": "1000", "taker_only": taker_only}
        if cursor:
            q["cursor"] = cursor
        doc = http_json(TRADES + "?" + urllib.parse.urlencode(q))
        pages += 1
        assert pages <= MAX_PAGES, "BLOCKED: more than %d pages for %s" % (MAX_PAGES, cids[0])
        assert isinstance(doc.get("data"), list) and isinstance(doc.get("pagination"), dict)
        for r in doc["data"]:
            c = r["condition_id"]
            assert c in by, "a row of %s outside the request" % c
            row = compact(r)
            if tokens is not None:
                assert r["token_id"] == tokens[c][0 if row[2] == "U" else 1], "token of %s" % c
            if keep_tx:
                row += [r["token_id"], r["transaction_hash"], r["proxy_wallet"]]
            by[c].append(row)
        cursor = doc["pagination"].get("next_cursor")
        if not cursor:
            assert doc["pagination"].get("has_more") in (False, None), "no cursor, has_more"
            break
    return by


def compact(r):
    """[block time, side, outcome, size, price], sizes and prices as the text of their Decimals."""
    side, outcome = r["side"], r["outcome"]
    assert side in ("BUY", "SELL"), side
    assert (outcome, r["outcome_index"]) in (("Up", 0), ("Down", 1)), (outcome, r["outcome_index"])
    s, p = r["size"], r["price"]
    assert isinstance(s, D) and isinstance(p, D) and s > 0 and 0 < p < 1, (s, p)
    t = r["timestamp"]
    assert isinstance(t, int) and not isinstance(t, bool)
    return [t, side[0], outcome[0], fx(s), fx(p)]


# ---- the rules -----------------------------------------------------------------------------------

def maker_terms(side, outcome, s, p):
    """The makers' side of one taker fill in Up shares: (x, pi). x > 0 is makers long Up, pi the Up
    price of the fill. A taker who buys Up sells it from makers; a taker who buys Down at p takes it
    from makers who are then long Up at 1 - p, whether they sold Down or bought Up."""
    if outcome == "U":
        return (-s, p) if side == "B" else (s, p)
    assert outcome == "D"
    return (s, 1 - p) if side == "B" else (-s, 1 - p)


def rebate(s, p):
    """The 20% maker rebate of the venue's fee, 0.07 * s * p * (1 - p), at the price reported."""
    return REBATE_COEF * s * p * (1 - p)


def band_of(dt):
    for name, lo, hi in BANDS:
        if (lo is None or dt >= lo) and (hi is None or dt < hi):
            return name
    raise AssertionError(dt)


def zero():
    return {"n": 0, "sh": D(0), "X": D(0), "C": D(0), "R": D(0)}


def aggregate(t0, rows):
    """Per band: fills, shares, the makers' net Up position X, its cost C = sum x * pi, and the
    rebate R. The window's sums are the sums over WINDOW_BANDS."""
    bands = {name: zero() for name, _lo, _hi in BANDS}
    for row in rows:
        ts, side, outcome, s, p = row[:5]
        s, p = D(s), D(p)
        x, pi = maker_terms(side, outcome, s, p)
        b = bands[band_of(ts - t0)]
        b["n"] += 1
        b["sh"] += s
        b["X"] += x
        b["C"] += x * pi
        b["R"] += rebate(s, p)
    win = zero()
    for name in WINDOW_BANDS:
        for k in win:
            win[k] += bands[name][k]
    return bands, win


def iso(t0):
    return datetime.datetime.fromtimestamp(t0, datetime.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ")


def excluded(t0, spans):
    for lo, hi, why in spans:
        if lo <= t0 <= hi:
            return why
    return None


def qualify(t0, doc):
    """Label-free: the first condition a candidate fails, or None. outcomePrices is checked for being
    one of the two resolved forms and nothing else is read from it (TZ-23 section 2, item 6 (a))."""
    if doc is None:
        return "absent"
    if json.loads(doc["outcomes"]) != ["Up", "Down"]:
        return "outcomes"
    if json.loads(doc["outcomePrices"]) not in (["1", "0"], ["0", "1"]):
        return "unresolved"
    if doc.get("closed") is not True:
        return "open"
    if doc.get("feeType") != FEE_TYPE or doc.get("feeSchedule") != FEE_SCHEDULE:
        return "fee"
    if doc.get("eventStartTime") != iso(t0):
        return "start"
    if not CONDITION.fullmatch(doc.get("conditionId") or ""):
        return "condition"
    tok = json.loads(doc["clobTokenIds"])
    if not (isinstance(tok, list) and len(tok) == 2 and all(t.isdigit() for t in tok)):
        return "tokens"
    return None


def kept_doc(doc):
    return {k: doc[k] for k in ("slug", "conditionId", "outcomes", "outcomePrices", "closed",
                                "feeType", "feeSchedule", "eventStartTime", "clobTokenIds")}


def label_of(doc):
    """The venue's resolved outcome: 1 Up, 0 Down. Called by `score` alone."""
    return {("1", "0"): 1, ("0", "1"): 0}[tuple(json.loads(doc["outcomePrices"]))]


# ---- the gate ------------------------------------------------------------------------------------

def gate_constants(V, sh, lam=LAMBDA, alpha=ALPHA, delta=DELTA):
    """Ville's inequality on exp(lam * M - lam^2 * V / 8), M the martingale part of the makers'
    settlement result: a false reading of either answer has probability at most alpha, at any look."""
    L = (1 / alpha).ln()
    thr = L / lam + lam * V / 8
    c = {"L": L, "lambda": lam, "alpha": alpha, "delta": delta, "V": V, "sh": sh, "thr": thr,
         "earn_at": thr, "no_earn_at": delta * sh - thr}
    if sh > 0:
        c["thr_per_share"] = thr / sh
        c["no_earn_per_share"] = delta - thr / sh
    sd = float(V.sqrt()) / 2.0 if V > 0 else 0.0
    z = (float(delta * sh - thr) / sd) if sd > 0 else float("-inf")
    c["power"] = D(repr(0.5 * (1.0 + math.erf(z / math.sqrt(2.0))))) if sd > 0 else D(0)
    return c


def reading(S, c):
    earn = S >= c["earn_at"]
    no_earn = S <= c["no_earn_at"]
    if earn:
        return "EARN", earn, no_earn
    if no_earn:
        return "NO EARN", earn, no_earn
    return "UNDECIDABLE", earn, no_earn


# ---- the set -------------------------------------------------------------------------------------

def next_open(t, spans):
    """The first T0 at or after t outside every excluded span."""
    moved = True
    while moved:
        moved = False
        for lo, hi, _why in spans:
            if lo <= t <= hi:
                t, moved = hi + STEP, True
    return t


def candidates(start, spans, need, docs_of):
    """Walk T0 = start, start + 300, ... past every excluded span, in chunks of at most CHUNK and
    never more than the members still needed, so no document after the need-th member is requested;
    return every candidate considered with its status."""
    considered, members, t = [], [], next_open(start, spans)
    while len(members) < need:
        assert len(considered) < need + WALK_SLACK, "BLOCKED: %d considered for %d members" % (
            len(considered), len(members))
        chunk = []
        while len(chunk) < min(CHUNK, need - len(members)):
            chunk.append(t)
            t = next_open(t + STEP, spans)
        assert chunk[-1] <= time.time() - RESOLVED_AFTER_S, \
            "BLOCKED: the walk reached %s, too recent to be resolved" % utc(chunk[-1])
        docs = docs_of(chunk)
        for c in chunk:
            doc = docs.get("btc-updown-5m-%d" % c)
            status = qualify(c, doc) or "member"
            considered.append((c, status))
            if status == "member":
                members.append((c, kept_doc(doc)))
                if len(members) == need:
                    break
    return considered, members


def chunk_path(cache, first):
    return os.path.join(cache, "%d.json.gz" % first)


def fetch_chunk(cache, group):
    """The taker fills of up to CHUNK members, written once, atomically."""
    path = chunk_path(cache, group[0][0])
    if os.path.exists(path):
        return path, False
    cids = [d["conditionId"] for _t, d in group]
    tokens = {d["conditionId"]: json.loads(d["clobTokenIds"]) for _t, d in group}
    by = trades(cids, "true", tokens)
    for rs in by.values():
        rs.sort()
    body = dumps({"members": [{"t0": t, "condition": d["conditionId"],
                               "rows": by[d["conditionId"]]} for t, d in group]})
    write_atomic(path, gz_bytes(body))
    return path, True


def form_set(base, start, spans, need):
    os.makedirs(base, exist_ok=True)
    setp = os.path.join(base, "set.json")
    if os.path.exists(setp):
        with open(setp, encoding="utf-8") as fh:
            s = json.load(fh, parse_float=D)
        out("the set from %s sha256 %s: %d considered, %d members" % (
            setp, sha256_file(setp), len(s["considered"]), len(s["members"])))
        return s
    t = time.time()
    considered, members = candidates(start, spans, need, gamma_docs)
    s = {"start": start, "need": need, "considered": considered,
         "members": [{"t0": t0, "doc": d} for t0, d in members]}
    write_atomic(setp, dumps(s).encode("utf-8"))
    out("the set formed in %.1f s: %d considered, %d members, %s sha256 %s" % (
        time.time() - t, len(considered), len(members), setp, sha256_file(setp)))
    with open(setp, encoding="utf-8") as fh:
        return json.load(fh, parse_float=D)


def fetch_fills(base, s, budget_s=FETCH_BUDGET_S):
    cache = os.path.join(base, "cache")
    os.makedirs(cache, exist_ok=True)
    groups, cur = [], []
    for m in s["members"]:
        cur.append((m["t0"], m["doc"]))
        if len(cur) == CHUNK:
            groups.append(cur)
            cur = []
    if cur:
        groups.append(cur)
    t, done, fresh = time.time(), 0, 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=FETCH_WORKERS) as pool:
        for path, new in pool.map(lambda g: fetch_chunk(cache, g), groups):
            done += 1
            fresh += 1 if new else 0
            if fresh == 30:
                proj = (time.time() - t) / fresh * (len(groups) - done + fresh)
                out("projected %.0f s for %d chunks after %d fetched" % (proj, len(groups), fresh))
                assert proj <= budget_s, "BLOCKED: fetch projected at %.0f s, above %d" % (proj,
                                                                                          budget_s)
            if done % 25 == 0 or done == len(groups):
                out("chunks %d of %d, %.0f s" % (done, len(groups), time.time() - t))
    return cache, groups


def member_rows(cache, groups):
    """Every member's rows, in T0 order, read back from the cache."""
    for g in groups:
        with gzip.open(chunk_path(cache, g[0][0]), "rt", encoding="utf-8") as fh:
            doc = json.load(fh)
        assert [m["t0"] for m in doc["members"]] == [t for t, _d in g]
        for m, (t, d) in zip(doc["members"], g):
            assert m["condition"] == d["conditionId"]
            yield t, d, m["rows"]


# ---- constants and score -------------------------------------------------------------------------

COLS = ["t0", "weekend"] + ["%s_%s" % (k, b) for b in ["win"] + [n for n, _l, _h in BANDS]
                            for k in ("n", "sh", "X", "C", "R")]


def segments(t0s):
    """Members counted by how many excluded spans end below them."""
    ends = sorted(hi for _lo, hi, _why in EXCLUDED)
    seg = {}
    for t in t0s:
        k = str(sum(1 for e in ends if e < t))
        seg[k] = seg.get(k, 0) + 1
    return seg


def weekend(t0):
    return 1 if datetime.datetime.fromtimestamp(t0, datetime.timezone.utc).weekday() >= 5 else 0


def build_constants(base, s, cache, groups, label):
    """Label-free: the members file, the fills file and the constants file. A second run must write
    the same bytes."""
    lines = [",".join(COLS)]
    tot = {"win": zero(), **{n: zero() for n, _l, _h in BANDS}}
    V = D(0)
    fills_path = os.path.join(base, "%s-fills.jsonl.gz" % label)
    tmp = fills_path + ".build"
    with open(tmp, "wb") as raw, gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as g:
        for t0, d, rows in member_rows(cache, groups):
            bands, win = aggregate(t0, rows)
            V += win["X"] * win["X"]
            cells = [str(t0), str(weekend(t0))]
            for name, agg in [("win", win)] + [(n, bands[n]) for n, _l, _h in BANDS]:
                for k in ("n", "sh", "X", "C", "R"):
                    tot[name][k] += agg[k]
                    cells.append(str(agg[k]) if k == "n" else fx(agg[k]))
            lines.append(",".join(cells))
            g.write(dumps({"t0": t0, "rows": rows}).encode("utf-8"))
    fills_sha = sha256_file(tmp)
    if os.path.exists(fills_path):
        assert sha256_file(fills_path) == fills_sha, "determinism: %s differs" % fills_path
        os.remove(tmp)
        out("unchanged %s sha256 %s" % (fills_path, fills_sha))
    else:
        os.replace(tmp, fills_path)
    members_csv = ("\n".join(lines) + "\n").encode("utf-8")
    c = gate_constants(V, tot["win"]["sh"])
    t0s = [m["t0"] for m in s["members"]]
    nonm = [[t, st] for t, st in s["considered"] if st != "member"]
    const = {"label": label, "members": len(t0s), "first": t0s[0], "last": t0s[-1],
             "member_list_sha": sha256_bytes(("\n".join(map(str, t0s)) + "\n").encode()),
             "considered": len(s["considered"]), "non_members": nonm,
             "weekend_members": sum(weekend(t) for t in t0s),
             "segments": segments(t0s),
             "totals": tot, "gate": c, "members_csv_sha": sha256_bytes(members_csv),
             "fills_sha": fills_sha}
    body = dumps(const).encode("utf-8")
    paths = {"fills.jsonl.gz": (fills_path, fills_sha)}
    for name, data in (("members.csv", members_csv), ("constants.json", body)):
        pth = os.path.join(base, "%s-%s" % (label, name))
        paths[name] = (pth, write_once(pth, data))
    return const, paths


def show_constants(const, paths):
    g, w = const["gate"], const["totals"]["win"]
    out("members %d, considered %d, first %d %s, last %d %s, weekend members %d" % (
        const["members"], const["considered"], const["first"], utc(const["first"]), const["last"],
        utc(const["last"]), const["weekend_members"]))
    out("member list sha %s" % const["member_list_sha"])
    out("members by the number of excluded spans ending below them: %s" % (
        ", ".join("%s: %d" % kv for kv in sorted(const["segments"].items()))))
    for t, st in const["non_members"]:
        out("non-member %d %s: %s" % (t, utc(t), st))
    out("window fills %d, shares %s, X %s, C %s, R %s" % (w["n"], fx(w["sh"]), fx(w["X"]),
                                                       fx(w["C"]), fx(w["R"])))
    for name, _l, _h in BANDS:
        b = const["totals"][name]
        out("band %-4s fills %d, shares %s" % (name, b["n"], fx(b["sh"])))
    out("V %s; lambda %s; L %s" % (fx(g["V"]), fx(g["lambda"]), fx(g["L"])))
    out("EARN at S >= %s (%s a share); NO EARN at S <= %s (%s a share)" % (
        fx(g["earn_at"]), fx(g["thr_per_share"]), fx(g["no_earn_at"]),
        fx(g["no_earn_per_share"])))
    out("power of either answer against the other's alternative, normal, variance V/4: %s"
        % fx(g["power"]))
    for name, (p, h) in sorted(paths.items()):
        out("wrote %s sha256 %s" % (p, h))


def score(base, s, const, label):
    """The labels, read once from the set's own documents, and the reading."""
    with open(os.path.join(base, "%s-members.csv" % label), encoding="utf-8") as fh:
        rows = [ln.split(",") for ln in fh.read().splitlines()]
    assert rows[0] == COLS
    ix = {k: i for i, k in enumerate(COLS)}
    docs = {m["t0"]: m["doc"] for m in s["members"]}
    assert len(rows) - 1 == len(docs)
    S = P = R = XU = D(0)
    ups = 0
    bands = {n: {"XU": D(0), "C": D(0), "R": D(0), "sh": D(0)} for n, _l, _h in BANDS}
    scored = ["t0,up,X,C,R,pnl"]
    for r in rows[1:]:
        t0 = int(r[ix["t0"]])
        up = label_of(docs[t0])
        ups += up
        X, C, Rm = D(r[ix["X_win"]]), D(r[ix["C_win"]]), D(r[ix["R_win"]])
        pnl = X * up - C + Rm
        S += pnl
        P += X * up - C
        R += Rm
        XU += X * up
        scored.append("%d,%d,%s,%s,%s,%s" % (t0, up, fx(X), fx(C), fx(Rm), fx(pnl)))
        for n, _l, _h in BANDS:
            b = bands[n]
            b["XU"] += D(r[ix["X_" + n]]) * up
            b["C"] += D(r[ix["C_" + n]])
            b["R"] += D(r[ix["R_" + n]])
            b["sh"] += D(r[ix["sh_" + n]])
    g = const["gate"]
    word, earn, no_earn = reading(S, {"earn_at": D(g["earn_at"]),
                                      "no_earn_at": D(g["no_earn_at"])})
    sh = D(g["sh"])
    res = {"label": label, "members": len(docs), "ups": ups, "S": S, "P": P, "R": R, "XU": XU,
           "sh": sh, "S_per_share": S / sh, "P_per_share": P / sh, "R_per_share": R / sh,
           "earn": earn, "no_earn": no_earn, "reading": word,
           "margin_earn": S - D(g["earn_at"]), "margin_no_earn": D(g["no_earn_at"]) - S,
           "bands": {n: {"pnl_per_share": ((b["XU"] - b["C"] + b["R"]) / b["sh"]) if b["sh"]
                         else None,
                         "rebate_per_share": (b["R"] / b["sh"]) if b["sh"] else None}
                     for n, b in bands.items()}}
    body = dumps(res).encode("utf-8")
    scored_csv = ("\n".join(scored) + "\n").encode("utf-8")
    for name, data in (("scored.csv", scored_csv), ("reading.json", body)):
        write_once(os.path.join(base, "%s-%s" % (label, name)), data)
    out("labels: %d members, %d Up" % (len(docs), ups))
    out("S %s = settlement %s + rebate %s; per share %s = %s + %s" % (
        fx(S), fx(P), fx(R), fx(res["S_per_share"]), fx(res["P_per_share"]),
        fx(res["R_per_share"])))
    out("EARN %s (margin %s); NO EARN %s (margin %s)" % (earn, fx(res["margin_earn"]), no_earn,
                                                       fx(res["margin_no_earn"])))
    for n, b in res["bands"].items():
        if b["pnl_per_share"] is not None:
            out("band %-4s makers per share %s, of it rebate %s - barred from every reading" % (
                n, fx(b["pnl_per_share"]), fx(b["rebate_per_share"])))
    out("wrote %s-scored.csv sha256 %s and %s-reading.json sha256 %s" % (
        label, sha256_bytes(scored_csv), label, sha256_bytes(body)))
    return res


# ---- modes ---------------------------------------------------------------------------------------

def git(*args):
    cp = subprocess.run(["git", "-C", WT] + list(args), capture_output=True, text=True)
    assert cp.returncode == 0, "git %s: %s" % (" ".join(args), cp.stderr.strip())
    return cp.stdout.strip()


def mode_rehearse():
    floor_check()
    base = os.path.join(WORK, "rehearsal")
    s = form_set(base, REHEARSAL[0], (), REHEARSAL[1])
    assert len(s["members"]) == REF["members"] and len(s["considered"]) == REF["members"], \
        "G-REHEARSAL: %d members of %d considered" % (len(s["members"]), len(s["considered"]))
    cache, groups = fetch_fills(base, s, budget_s=10 ** 9)
    const, paths = build_constants(base, s, cache, groups, "rehearsal")
    show_constants(const, paths)
    res = score(base, s, const, "rehearsal")
    w = const["totals"]["win"]
    got = {"members": const["members"], "ups": res["ups"], "n": w["n"], "sh": w["sh"],
           "X": w["X"], "C": w["C"], "R": w["R"], "V": const["gate"]["V"], "XU": res["XU"],
           "S": res["S"]}
    bad = [k for k in REF if got[k] != REF[k]]
    for k in REF:
        out("G-REHEARSAL %-7s instrument %s, the Architect's %s, %s" % (
            k, got[k], REF[k], "equal" if got[k] == REF[k] else "DIFFERENT"))
    assert not bad, "G-REHEARSAL FAIL: %s" % bad
    out("G-REHEARSAL PASS: %d of %d figures equal" % (len(REF), len(REF)))


def mode_fetch():
    floor_check()
    os.makedirs(WORK, exist_ok=True)
    base = os.path.join(WORK, "set")
    s = form_set(base, START, EXCLUDED, N_SET)
    assert len(s["members"]) == N_SET, "G-SET: %d members" % len(s["members"])
    cache, groups = fetch_fills(base, s)
    n = sum(1 for _ in member_rows(cache, groups))
    assert n == N_SET, "G-SET: %d members read back" % n
    out("G-SET PASS: %d members, %d chunks, every chunk read back" % (N_SET, len(groups)))


def set_and_groups():
    base = os.path.join(WORK, "set")
    with open(os.path.join(base, "set.json"), encoding="utf-8") as fh:
        s = json.load(fh, parse_float=D)
    groups = [[(m["t0"], m["doc"]) for m in s["members"][i:i + CHUNK]]
              for i in range(0, len(s["members"]), CHUNK)]
    return base, s, os.path.join(base, "cache"), groups


def mode_constants():
    floor_check()
    base, s, cache, groups = set_and_groups()
    assert len(s["members"]) == N_SET
    const, paths = build_constants(base, s, cache, groups, "tz23")
    show_constants(const, paths)
    st = load_state()
    st["constants_sha"] = paths["constants.json"][1]
    st["constants_at"] = utc(time.time())
    save_state(st)


def mode_rebate():
    """Label-free. For every SAMPLE_EVERY-th member: both feeds again, with transaction and wallet;
    the maker rows of each transaction are its rows less its one taker row; the exact rebate is the
    fee formula at each maker's own price. The taker feed must equal the cached rows."""
    floor_check()
    base, s, cache, groups = set_and_groups()
    sample = [(m["t0"], m["doc"]) for i, m in enumerate(s["members"]) if i % SAMPLE_EVERY ==
              SAMPLE_EVERY - 1]
    want = {t for t, _d in sample}
    cached = {}
    for g in groups:
        if want.intersection(t for t, _d in g):
            for t, _d, rows in member_rows(cache, [g]):
                if t in want:
                    cached[t] = rows
    assert set(cached) == want, "rebate: %d of %d sampled members in the cache" % (len(cached),
                                                                                   len(want))
    exact = reported = D(0)
    sh = D(0)
    n_tx = n_multi = n_skip = n_gap = 0
    gap_sh = D(0)
    for t0, d in sample:
        cid = d["conditionId"]
        tokens = {cid: json.loads(d["clobTokenIds"])}
        taker = trades([cid], "true", tokens, keep_tx=True)[cid]
        assert sorted(r[:5] for r in taker) == cached[t0], "rebate: the taker feed of %d changed" % t0
        pool, takers = {}, {}
        for r in trades([cid], "false", tokens, keep_tx=True)[cid]:
            pool.setdefault(r[6], []).append(r)
        for r in taker:
            takers.setdefault(r[6], []).append(r)
        for tx, trs in sorted(takers.items()):
            if len(trs) != 1:
                n_skip += 1
                continue
            r = trs[0]
            if not (WINDOW[0] <= r[0] - t0 < WINDOW[1]):
                continue
            makers = pool.get(tx, [])
            assert r in makers, "rebate: the taker row of %s is not among its rows" % tx
            makers.remove(r)
            gap = D(r[3]) - sum((D(m[3]) for m in makers), D(0))
            if gap != 0:
                n_gap += 1
                gap_sh += abs(gap)
            p = D(r[4])
            reported += D(r[3]) * p * (1 - p)
            exact += sum((D(m[3]) * D(m[4]) * (1 - D(m[4])) for m in makers), D(0))
            sh += D(r[3])
            n_tx += 1
            prices = {D(m[4]) if m[2] == r[2] else 1 - D(m[4]) for m in makers}
            n_multi += 1 if len(prices) > 1 else 0
    out("rebate check: %d members, %d window transactions, %d at several prices, %d transactions "
        "with other than one taker row skipped" % (len(sample), n_tx, n_multi, n_skip))
    out("transactions whose taker size differs from its makers' sum: %d, %s shares in all" % (
        n_gap, fx(gap_sh)))
    out("fee-equivalent at the reported price %s, at each maker's own price %s, ratio %s" % (
        fx(reported), fx(exact), fx(exact / reported) if reported else "undefined"))
    out("the rebate counted above the venue's, per share of the sample's window: %s" % (
        fx(REBATE_COEF * (reported - exact) / sh) if sh else "undefined"))


def mode_score():
    base, s, cache, groups = set_and_groups()
    st = load_state()
    cpath = os.path.join(base, "tz23-constants.json")
    assert sha256_file(cpath) == st.get("constants_sha"), "score: not the constants recorded"
    head = git("rev-parse", "HEAD")
    branches = git("branch", "-r", "--contains", head).split()
    assert "origin/tz-23-maker-m0" in branches, "score: HEAD %s is not on origin" % head
    with open(cpath, encoding="utf-8") as fh:
        const = json.load(fh, parse_float=D)
    with open(LEDGER, "a", encoding="utf-8") as fh:
        fh.write(dumps({"at": utc(time.time()), "head": head, "members": const["members"],
                        "member_list_sha": const["member_list_sha"]}))
    res = score(base, s, const, "tz23")
    out("M0 READING: %s" % res["reading"])


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
    return tree == WORK and (rel == "state.json" or rel == "label-ledger.jsonl"
                             or rel.startswith("logs/"))


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
        "%d already held; forensic store %d -> %d files" % (considered, named, kept, copied, held,
                                                           before, after))


# ---- the self-test -------------------------------------------------------------------------------

def mode_selftest():
    n = [0]

    def ok(cond, what):
        assert cond, "selftest: " + what
        n[0] += 1
        out("  ok  " + what)

    ok(MALLOC_TUNED, "glibc took the 128 KiB mmap threshold and the two arenas")
    # the sign convention, at live magnitudes: a taker's result and the makers' are opposite
    for side, outcome, s, p in (("B", "U", D("364.58"), D("0.999")), ("S", "U", D("30"), D("0.99")),
                                ("B", "D", D("100"), D("0.01")), ("S", "D", D("1250.5"), D("0.47"))):
        x, pi = maker_terms(side, outcome, s, p)
        for up in (0, 1):
            won = up if outcome == "U" else 1 - up
            taker = s * (won - p) if side == "B" else s * (p - won)
            ok(x * (up - pi) == -taker, "makers' result is minus the taker's: %s %s up=%d" % (
                side, outcome, up))
    ok(maker_terms("B", "D", D("100"), D("0.01")) == (D("100"), D("0.99")),
       "a taker buying Down at 0.01 leaves makers long 100 Up at 0.99")
    ok(maker_terms("S", "D", D("10"), D("0.01")) == (D("-10"), D("0.99")),
       "a taker selling Down at 0.01 leaves makers short 10 Up at 0.99")
    # the four-maker transaction of the excluded span, by hand: makers +1 USDC if Up, -99 if Down
    x, pi = maker_terms("B", "D", D("100"), D("0.01"))
    ok(x * (1 - pi) == D("1.00") and x * (0 - pi) == D("-99.00"),
       "a 100-share Down purchase at 0.01: makers +1.00 on Up and -99.00 on Down")
    ok(rebate(D("100"), D("0.5")) == D("0.35"), "rebate of 100 shares at 0.50 is 0.35 USDC")
    ok(rebate(D("100"), D("0.99")) == D("0.01386"), "rebate of 100 shares at 0.99 is 0.01386 USDC")
    ok(rebate(D("100"), D("0.3")) == rebate(D("100"), D("0.7")), "the rebate is symmetric in p")
    ok(REBATE_COEF == FEE_SCHEDULE["rate"] * FEE_SCHEDULE["rebateRate"], "0.014 = 0.07 * 0.2")
    # bands
    ok([band_of(d) for d in (-1, 0, 59, 60, 239, 240, 299, 300)] ==
       ["pre", "w0", "w0", "w1", "w3", "last", "last", "post"], "band edges")
    ok(WINDOW == (0, 240) and WINDOW_BANDS == ("w0", "w1", "w2", "w3"), "the window is [T0, T0+240)")
    # aggregate on literal rows: a fill at T0 + 239 counts, at T0 + 240 does not
    t0 = 1788530400
    rows = [[t0 + 239, "B", "U", "10", "0.6"], [t0 + 240, "B", "U", "10", "0.6"],
            [t0 - 5, "S", "D", "4", "0.25"]]
    bands, win = aggregate(t0, rows)
    ok(win["n"] == 1 and win["sh"] == D("10") and win["X"] == D("-10") and win["C"] == D("-6.0"),
       "the window takes T0+239 and not T0+240")
    ok(bands["pre"]["X"] == D("-4") and bands["pre"]["C"] == D("-3.00"),
       "a Down sale before T0 leaves makers short 4 Up at 0.75")
    ok(bands["last"]["n"] == 1, "T0+240 is the last minute")
    # the window's sums equal the sums of its four bands
    ok(all(win[k] == sum((bands[b][k] for b in WINDOW_BANDS), D(0) if k != "n" else 0)
           for k in win), "the window is the sum of w0..w3")
    # qualification
    good = {"slug": "btc-updown-5m-1788530400", "outcomes": '["Up", "Down"]', "outcomePrices": '["0", "1"]',
            "closed": True, "feeType": FEE_TYPE,
            "feeSchedule": {"exponent": 1, "rate": D("0.07"), "takerOnly": True, "rebateRate": D("0.2")},
            "eventStartTime": "2026-09-04T14:00:00Z", "conditionId": "0x" + "ab" * 32,
            "clobTokenIds": '["123", "456"]'}
    ok(qualify(1788530400, good) is None, "a resolved, fee-schedule-conforming market qualifies")
    for key, val, why in (("outcomePrices", '["0.5", "0.5"]', "unresolved"), ("closed", False, "open"),
                          ("feeType", "crypto_fees", "fee"), ("eventStartTime", "2026-09-04T14:05:00Z", "start"),
                          ("conditionId", "0x12", "condition"), ("outcomes", '["Yes", "No"]', "outcomes"),
                          ("clobTokenIds", '["123"]', "tokens")):
        bad = dict(good)
        bad[key] = val
        ok(qualify(1788530400, bad) == why, "%s=%r reads %s" % (key, val, why))
    bad = dict(good)
    bad["feeSchedule"] = {"exponent": 1, "rate": D("0.07"), "takerOnly": True, "rebateRate": D("0.25")}
    ok(qualify(1788530400, bad) == "fee", "a 25% rebate is not this TZ's schedule")
    ok(qualify(1788530400, None) == "absent", "no document reads absent")
    ok(label_of(good) == 0 and label_of(dict(good, outcomePrices='["1", "0"]')) == 1, "labels")
    # the set walk: exclusions, the need-th member, nothing considered after it
    def fake_docs(t0s):
        return {"btc-updown-5m-%d" % t: dict(good, slug="btc-updown-5m-%d" % t, eventStartTime=iso(t),
                                            outcomePrices=('["1", "0"]' if (t // 300) % 7 else '["0.5", "0.5"]'))
                for t in t0s}
    cons, mem = candidates(1791049500, EXCLUDED, 5, fake_docs)
    ok([m[0] for m in mem] == [1791049500, 1791049800, 1791098100, 1791098700, 1791099000],
       "the walk takes the five members around the excluded span, past one unresolved")
    ok([t for t, st in cons if st != "member"] == [1791098400], "1791098400 reads unresolved")
    ok(not [t for t, _st in cons if 1791050100 <= t <= 1791097800],
       "no candidate of the explored span is considered")
    asked = []
    candidates(1791049500, EXCLUDED, 5, lambda ts: (asked.extend(ts), fake_docs(ts))[1])
    ok(asked == [t for t, _st in cons] and asked[-1] == mem[-1][0],
       "every document requested is a candidate considered, the last the 5th member's")
    ok(cons[-1][1] == "member" and cons[-1][0] == mem[-1][0], "nothing is considered after the 5th member")
    ok(excluded(1788350400, EXCLUDED) and excluded(1788524100, EXCLUDED) and
       not excluded(1788524400, EXCLUDED), "the 2026-09-02/04 span is excluded, its next market is not")
    ok(excluded(1791097800, EXCLUDED) and not excluded(1791098100, EXCLUDED),
       "the 2026-10-03/04 span ends at 1791097800")
    ok(excluded(1788998400, EXCLUDED) and excluded(1790452200, EXCLUDED) and
       not excluded(1788998100, EXCLUDED) and not excluded(1790452500, EXCLUDED),
       "the labelled span 1788998400 ... 1790452200 is excluded, its neighbours are not")
    ok(next_open(1788998100 + STEP, EXCLUDED) == 1790452500, "the walk steps over the labelled span")
    ok(START == 1788530400 and iso(START) == "2026-09-04T14:00:00Z", "the set starts at 2026-09-04 14:00 UTC")
    # the gate: Ville's threshold, independent of the code path, at a realistic V
    V = D("88119062784.573977477054291666666666666666666666667")
    sh = D("157239560.97379616666666666666666666666666666666667")
    c = gate_constants(V, sh)
    L = D(200).ln()
    ok(abs(c["thr"] - (L / LAMBDA + LAMBDA * V / 8)) == 0, "thr = L/lambda + lambda V/8")
    ok(abs(c["thr"] - (L * V / 2).sqrt()) / c["thr"] < D("1e-6"),
       "at the projected V the threshold is Hoeffding's sqrt(V ln(1/alpha) / 2)")
    ok(D("0.0030") < c["thr_per_share"] < D("0.0031"), "the projected threshold is 0.31 c a share")
    ok(D("0.97") < c["power"] < D("0.99"), "the projected power is 0.979")
    ok(reading(c["earn_at"], c)[0] == "EARN", "S at the EARN threshold reads EARN")
    ok(reading(c["earn_at"] - D("0.000001"), c)[0] == "UNDECIDABLE", "just below it does not")
    ok(reading(c["no_earn_at"], c)[0] == "NO EARN", "S at the NO EARN threshold reads NO EARN")
    ok(reading(c["no_earn_at"] + D("0.000001"), c)[0] == "UNDECIDABLE", "just above it does not")
    # the bound itself, by simulation under the least favourable null: every member's conditional
    # mean exactly 0, fair coins at the projected inventories; P(EARN) must be at most alpha
    import random
    rng = random.Random(23)
    xs = [D(rng.choice((3000, 4000, 5000, 6000))) for _ in range(2000)]
    Vs = sum(x * x for x in xs)
    cs = gate_constants(Vs, D(2000 * 40000))
    hits = 0
    for _ in range(400):
        S = sum(x * (1 if rng.random() < 0.5 else -1) / 2 for x in xs)
        hits += 1 if S >= cs["earn_at"] else 0
    ok(hits <= 2, "400 null runs at fair coins: %d read EARN, at most 2 expected at alpha 0.005" % hits)
    # the constants are label-free, and the score is not: two members, their labels flipped
    tmp = os.path.join(WORK, "selftest-tmp")
    shutil.rmtree(tmp, ignore_errors=True)
    try:
        cache = os.path.join(tmp, "cache")
        os.makedirs(cache)
        t0s = (1788530400, 1788530700)
        fills = {1788530400: [[1788530410, "B", "U", "120", "0.55"], [1788530500, "S", "D", "40", "0.3"]],
                 1788530700: [[1788530760, "B", "D", "75.5", "0.62"], [1788530650, "S", "U", "9", "0.5"]]}
        docs = [dict(good, slug="btc-updown-5m-%d" % t, eventStartTime=iso(t),
                     conditionId="0x%064x" % (i + 1)) for i, t in enumerate(t0s)]
        write_atomic(chunk_path(cache, t0s[0]), gz_bytes(dumps({"members": [
            {"t0": t, "condition": d["conditionId"], "rows": fills[t]} for t, d in zip(t0s, docs)]})))
        outs = []
        for k, prices in enumerate(('["1", "0"]', '["0", "1"]')):
            base = os.path.join(tmp, "b%d" % k)
            os.makedirs(base)
            st = {"start": t0s[0], "need": 2, "considered": [[t, "member"] for t in t0s],
                  "members": [{"t0": t, "doc": dict(kept_doc(d), outcomePrices=prices)}
                              for t, d in zip(t0s, docs)]}
            groups = [[(m["t0"], m["doc"]) for m in st["members"]]]
            const, paths = build_constants(base, st, cache, groups, "t")
            res = score(base, st, const, "t")
            with open(paths["constants.json"][0], "rb") as fh:
                outs.append((fh.read(), res["S"]))
        ok(outs[0][0] == outs[1][0], "the constants file is byte-identical with every label flipped")
        ok(outs[0][1] != outs[1][1], "the score moves when the labels flip (negative control)")
        # by hand: the window's X is -120 - 40 = -160 for the first member and +75.5 for the
        # second, whose Up sale at T0 - 50 is outside the window; S(Up) - S(Down) is their sum
        ok(outs[0][1] - outs[1][1] == D("-84.5"),
           "the score moves by the window's X, -160 + 75.5 = -84.5, by hand")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    # deterministic gzip and JSON
    ok(gz_bytes("abc\n") == gz_bytes("abc\n"), "gzip is deterministic")
    ok(dumps({"b": D("0.10"), "a": 1}) == '{"a":1,"b":"0.10"}\n', "JSON is sorted with Decimals as text")
    ok(fx(D("1E-7")) == "0.0000001", "no exponent form")
    # the audit hook
    try:
        open("/var/lib/btc-recorder/runtime.jsonl", "rb")
        refused = False
    except RuntimeError:
        refused = True
    except OSError:
        refused = False
    ok(refused and OPENS == ["/var/lib/btc-recorder/runtime.jsonl"],
       "an open under the recorder's root is refused before it happens")
    OPENS.clear()
    out("%d of %d checks passed" % (n[0], n[0]))


def main(argv):
    if not argv:
        sys.exit("usage: tz23-maker-m0.py MODE [ARG...]")
    mode, rest = argv[0], argv[1:]
    table = {"selftest": mode_selftest, "still": mode_still, "rehearse": mode_rehearse,
             "fetch": mode_fetch, "constants": mode_constants, "rebate": mode_rebate,
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
    out("opens under the capture roots: %d" % len(OPENS))


if __name__ == "__main__":
    main(sys.argv[1:])
```
