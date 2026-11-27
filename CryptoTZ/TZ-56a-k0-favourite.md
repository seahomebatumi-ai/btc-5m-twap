# TZ-56a — K0, its second run: does the favourite, acquired at a traded price in [0.80, 0.95) and held to settlement, earn after a taker's fee — on Kalshi, with Polymarket as its control?

**Canonical filename:** `TZ-56a-k0-favourite.md`. The committed file takes this name and no other.

**It replaces TZ-56**, BLOCKED at §3.5 on 2026-11-27, G-REHEARSAL 11 of 12, with nothing of the six days read (its
report; map §7 item 204). Its rules — the frames, the draw, the trades, the money, the test and the decisions — are
TZ-56's unchanged; its rehearsal is rebuilt, and its paths are its own.

**Executor model: Claude Opus 5.5.** Reads of two venues over the network, a gate's arithmetic, and the first label
read of a set no one has read.

**Required System Map revision:** `2026-11-28-a`.

**Required anchors**, from map §0. A mismatch on any one is BLOCKED before any work:

| anchor | required |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` |
| `A4` — executor contract | `6ac6e10aeabc` |
| `A5` — recorder | `0f6c90451cbd` |
| `A6` — pricer | `729f0bcdbee3` |

**The map's sections, rows and items this run rests on** (map §7 item 174), read in full: §0 and its table; §1; §3,
the units and the trees; §5, its phase table and "What has been read"; §6, the rows `host`, `host identity, for TZ host
gates`, `language`, `egress`, `Kalshi's public API`, `Polymarket's gamma and Data API outside the reward book`,
`disk`, `disk floors and caps, as each code reads them`, `memory`, `process supervision`, `sandbox limit — network`,
`GitHub Releases — the archives' destination`, `sandbox limit — destructive actions` and `harness — background output`;
§7 items 60, 63, 77, 82, 84, 87, 91, 93, 95, 96, 105, 118, 119, 120, 124, 131, 132, 137, 138, 144, 150, 151, 154, 156,
167, 174, 175, 177, 191, 201, 202, 203 and 204.

**Host gate:** §0.3 — the capture host, for its interpreter, its network, `gh` and the forensic store. It reads
nothing of any capture.

**When:** §3.6 and everything after it **no earlier than 2026-11-23 12:00:00 UTC**, epoch `1795435200` — an instant
already past when this TZ was written, which §3.6's command still waits for in its own text and `frame` and `draw`
assert: it is the instant by which a Polymarket market of the set must have closed (§1). From §3.6 on, about two and a
half to three and a half hours of wall clock, almost all of it the venues' rate limits (§6).

**What this TZ is.** The K track's first step, K0 (CANON PART II): public data alone, no money, no key, no new server.
The Architect's explorations of 2026-11-22 found the favourite–longshot bias present on Kalshi and absent on Polymarket
on the days they read (CANON §1.8); a day can be luck. This TZ fixes, before any of their data is read, a rule that
draws **5,000 members a venue** from Kalshi's binary markets closing **2026-11-16 to 2026-11-21** and from Polymarket's
CTF markets ending on the same days and closed by the instant above, reads each member's takers' acquisitions of the
favourite at a traded price in `[0.80, 0.95)` within the day before its close, prices each at settlement less the
taker's fee, and reads each venue **EARN**, **NO EARN** or **UNDECIDABLE** by two exact betting tests at `1/400` each —
`1/200` an answer, family-wise over the two venues. Its instrument, `research/tz56-k0-favourite.py` (Appendix A), is its
own whole code: the venues' listings and trades, the draw, the money, the tests, and every reply it reads kept and
replayable, so that its frames and draws are rebuilt from the kept replies byte for byte and **published as the Release
`tz-56a-k0-inputs`** (CANON hard rule 16; map §7 item 154). **Its rehearsal compares it with the Architect's own
implementation, Appendix B, on the same kept replies of 2026-11-12, a day already read** — the venue may rename a
series or close a market between the Architect's reading and this run, as it did to TZ-56, and two programs that read
the same bytes see the same venue (§1, why this TZ). The Architect ran both on 2026-11-27 over three sets of replies of
that day, his own of 17:52 and 20:48 UTC and a fresh one at 21:00, and they agreed on 12 figures of 12 each time.

---

## 0. Gates

### 0.0 The work tree, first

After contract §1 steps 1 and 2, and before anything else:

```
mkdir /root/tz56a-work /root/tz56a-work/logs; echo "exit=$?"
```

`exit=0` proves neither existed; anything else is BLOCKED. **From here every command's output goes to
`/root/tz56a-work/logs/`, one file per step, §0's included**, and nothing to the session's scratchpad; the one exception
is B-RECLAIM-OWN, §9.

### 0.1 The instrument and the reference, staged

Extract Appendices A and B from this TZ as the primary checkout carries it after contract §1's pull, with this script,
verbatim, its one argument the destination:

```
/root/tz04a-env/venv/bin/python -B - /root/tz56a-work/stage <<'EOF'
import hashlib, os, sys
SRC = "/root/btc-5m-twap/CryptoTZ/TZ-56a-k0-favourite.md"
DEST = sys.argv[1]
WANT = {
    "research/tz56-k0-favourite.py": "7241a14afe5bde0bdeed37fb17bb9a45d59cc88e83ac319789eebedc07b335db",
    "reference/tz56a-k0-reference.py": "9de780a0f5744d5cceb3074c0373020cda15dd4a7ac8bee288c13f9ab7a91f6c",
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
| `research/tz56-k0-favourite.py` | 2,269 | 116,543 | `7241a14afe5bde0bdeed37fb17bb9a45d59cc88e83ac319789eebedc07b335db` |
| `reference/tz56a-k0-reference.py` | 416 | 17,645 | `9de780a0f5744d5cceb3074c0373020cda15dd4a7ac8bee288c13f9ab7a91f6c` |

The staged instrument runs §0.2's `fingerprint` and §0.5's `number` alone, written **`I0`**: `nice -n 19
/root/tz04a-env/venv/bin/python -B /root/tz56a-work/stage/research/tz56-k0-favourite.py`, run from `/root/tz56a-work` —
every mode asserts that its current directory is the work tree (`main`). **The reference is staged and never committed**
— the repository keeps one implementation of K0's rules — and runs from its staged copy at §3.5 alone, written **`R`**:
`nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz56a-work/stage/reference/tz56a-k0-reference.py`. Both need the
standard library alone.

### 0.2 Fingerprint

`I0 fingerprint` performs contract §1 steps 3 and 4 inside the instrument and asserts them (`mode_fingerprint`),
against `SYSTEM-MAP.md` and the files of its §0 table in the primary checkout `/root/btc-5m-twap`: revision
`2026-11-28-a`; the six anchors, `A2`, `A4`, `A5` and `A6` re-derived as the first 12 hex characters of their files'
SHA-256; the table's **74** rows each printed in lines, bytes and SHA-256 — **71** `frozen` rows asserted equal to the
map, **2** `tracked`, **1** `reported`; and the map's own lines, bytes and SHA-256. It prints `FINGERPRINT PASS` or
stops at the first mismatch, which is BLOCKED.

### 0.3 Host gate

From `/root/btc-5m-twap`, with `S` first set to the scratchpad directory the session's system prompt names, output
verbatim into `logs/03-host-gate.log`:

```
date -u; date -u +%s
nproc; grep -E '^(MemTotal|MemAvailable|SwapTotal|SwapFree):' /proc/meminfo
uptime -s
df -B1 --output=source,size,avail /var/lib/btc-recorder
find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
grep -c e3975b5da44c5328adf3bf3914634cd878842c73 /var/lib/btc-recorder/runtime.jsonl
/root/tz04a-env/venv/bin/python -c 'import sys; print(sys.version.split()[0])'
TZ=UTC systemctl show btc-recorder.service btc-rewardbook.service btc-rewardbook-archive.service btc-rewardbook-archive.timer adv3-bot.service liq-guard.service -p Id -p MainPID -p NRestarts -p ActiveState -p UnitFileState -p ActiveEnterTimestamp
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
du -sb /var/lib/btc-rewardbook /root/btc-forensics
find /var/lib/btc-rewardbook -name '*.stream.jsonl.gz' -printf '%s\n' | awk '{s += $1} END {print s + 0}'
find /root/btc-forensics -type f | wc -l
gh auth status 2>&1 | grep -c 'Logged in'
git worktree list
echo "$S"; ls -la "$(dirname "$(dirname "$S")")"
```

- **H1** — `find` prints exactly one path.
- **H2** — `df` names source `/dev/vda2` and size `31612203008`; `grep -c` prints at least `1`. With H1 this is map §6's
  host identity.
- **H3** — the interpreter prints `3.12.`.
- **H4** — `gh auth status` counts at least `1` login: B-UPLOAD's route (map §6, git remote).
- **Memory gate** — `MemAvailable` at least `157,499,106` bytes (§0.4).
- **Disk gate** — `avail` at least `8,700,000,000` bytes (§0.4).

Any of these six failing is BLOCKED. **The rest is printed and carries no threshold:** the units — §3.3 records them for
G-STILL; `telemetry-watch.service`'s state, on which map §6's headroom is conditional; the reward book's store and the
forensic store, beside `df` (map §2.6, §7 item 175), and the margin `avail` + the reward book's stream files, the
`find`'s sum, − `7,300,000,000` − `445,535,636`; the worktrees; and the listing of the directory that holds the
session's own, whose UUID directories `I scratch` names live or earlier (§3.3).

### 0.4 Resource floors, in exact bytes

**Memory.** `MemAvailable` at least **`157,499,106`** bytes (`MEM_FLOOR`, and the reference's `FLOOR`): twice the
largest peak of any mode of Appendix A and of Appendix B in the Architect's runs under Python 3.12.3 on 2026-11-27, each
at its population's bound, modelled at the host's ratio TZ-37 measured, `1.199` (map §6 memory; §7 items 93, 131 and
156): the reference over 2026-11-12's kept replies peaked at **`65,679,360`** (`PEAK_BOUND`) — `2 × ⌈65,679,360 × 1.199⌉
= 157,499,106`, an identity the self-test asserts. **The instrument's memory does not grow with a listing, a frame or a
set of draws** (§5): `frame` over a synthetic six-day listing at its pages cap with every market kept — Kalshi `400`
pages of `1,000` a day, `2,400,000` rows, `45,580,288`; Polymarket `3,000` pages of `100` a day, `1,800,000` rows,
`39,645,184` — and at `GROUPS_MAX`'s `100,000` series-days, `45,658,112` and `40,656,896`; `draw` at its bounds,
`40,000` draws on Polymarket over `99,996` series-days, `56,422,400`, and `20,000` on Kalshi, `48,324,608`; `rehearse`
over 2026-11-12's two real listings, `57,057,280`; `redraw` over one real day, `56,573,952`; `score` at `5,000` members,
`44,044,288`; `pack`, `31,911,936`; `selftest`, `40,505,344`. **On the host, TZ-56's run of the same modes peaked below
the Architect's:** `rehearse` `54,476,800`, `0.956` of his; `selftest` `39,968,768`; `probe` `41,811,968` (map §7 item
131's rule takes the larger, his modelled). Every mode that reads a venue or the set, and the reference, re-reads
`MemAvailable` at its start, again every `60` s below the floor, five reads at most, the last deciding (`floor_check`,
map §7 item 137); the instrument asserts glibc took the mmap threshold and the arena count. Map §6 records the host:
`1,002,127,360` bytes in all, one processor, `MemAvailable` from `218,279,936` to `246,616,064` across TZ-54's, TZ-55's
and TZ-56's reads with the liquidation guard running.

**Disk.** `/dev/vda2` free at least **`8,700,000,000`** bytes at each such mode's start (`DISK_GATE`), and at least
**`7,400,000,000`** after every 200 replies a source serves and every sorted run or `100,000` frame rows written
(`DISK_FLOOR`): the reward book's `STREAM_FLOOR`, `7,300,000,000`, and one slot of its streams at the cut,
`100,000,000` (map §6, disk floors), so nothing this TZ writes can stop the reward book's streams; the gate adds
`1,300,000,000`, this run's tree at the draws' bounds on frames of the measured sizes, `1,016,000,000` [modelled from
the Architect's runs: kept listings `59,500` and `49,000` bytes a page over Kalshi's `690` and Polymarket's `2,500`
pages, the counts of §6; frame rows `155` and `371` bytes; kept trades `14,697` and `4,550` bytes a draw over `20,000`
and `40,000` draws; the frame's sort files while it is built, about twice its rows; frames and draws rebuilt by
`redraw`, the Release's gzipped copies, the rehearsal's `38,000,000` and the logs]. Expected about `720,000,000`. A
frame at its pages cap with every market kept would outgrow that margin, and `disk_check` BLOCKs it before free space
falls below the floor. TZ-56 read `10,039,721,984` bytes free at 20:17 UTC on 2026-11-27.

### 0.5 Refs and the number

`I0 number`, into `logs/05-number.log` (`mode_number`): **NUMBER** — `CryptoTZ/` on `origin/main` holds
`CryptoTZ/TZ-56a-k0-favourite.md` and no other file whose name begins with `TZ-56a-`, and `CryptoReports/` none (CANON
hard rule 2); `FAIL` is BLOCKED. Then `git -C /root/btc-5m-twap ls-remote origin`, into `logs/05-refs.log`, printed as
counts by prefix and every line that differs from map §1's read (map §7 item 177). **BLOCKED** where
`refs/heads/tz-56a-k0-favourite` or `refs/tags/tz-56a-k0-inputs` already exists, or `main` does not carry revision
`2026-11-28-a`.

---

## 1. Why this TZ exists

Function names here are Appendix A's.

**The question** — CANON PART II, the K track's K0: on Kalshi's binary markets closing 2026-11-16 to 2026-11-21, and
Polymarket's ending on the same days — each a sample by a rule fixed before any of them is read — does the favourite's
side, at a traded price in `[0.80, 0.95)` and held to settlement, earn after a taker's fee? **Why it is asked:** the
favourite–longshot bias is published on Kalshi (Bürgi, Deng and Whelan) and was present on Kalshi on 2026-11-12 in
the Architect's exploration, absent on Polymarket on its own days (CANON §1.8). It needs no speed and no queue place:
it lives in the price, and a slow bot that pays the price and waits for settlement collects it — if it is there after
the fee, on days nobody chose.

**Why this TZ — TZ-56's BLOCK** (its report; map §7 item 204). TZ-56's rehearsal compared the instrument's twelve
figures of 2026-11-12 with literals the Architect computed from the replies he read at 17:52 UTC on 2026-11-27. At 20:18
Polymarket served one series of that day under a new name — `claude-opus-released` had become `claude-opus-released-on`
— and the rehearsal's draw `k = 137` met its one market, a non-member: the draws' label-free digest differed, the other
eleven figures held, and §3.5 BLOCKED as written, before any request of the six days. The Architect reproduced the
Executor's frame and draws byte for byte at 20:48, beside his own of 17:52, the one row and the one draw that moved
between them. A literal taken from a venue's live replies measures the venue's edits as well as the code; two
implementations that read the same kept replies measure the code alone. **So this TZ's rehearsal runs the Architect's
own implementation, Appendix B, written apart from Appendix A and sharing no code with it, over the very replies
`rehearse` kept, and compares the twelve figures** (§3.5, §4.1). Nothing else of TZ-56 changes but its paths, its
`scratch` argument and its margin's stream files (map §7 items 150 and 175), and its memory floor, which now covers the
reference.

**The frames — every market of the six days, by the venue's own listing, fixed here.**

- **Kalshi** (`kalshi_class`, `listing_url`, `build_frame`): for each day `d` of 2026-11-16 to 2026-11-21, `GET
  /markets` with `limit=1000`, `min_close_ts=d−3600`, `max_close_ts=d+86400+3600` and `mve_filter=exclude` — combos
  are another product — page by page on its `cursor`. A market is a row where it closes in `[d, d + 86,400)` of one of
  the six days and is `binary`, `finalized`, resolved `yes` or `no` and traded (`volume_fp` above 0 — a market that
  never traded has no trade to read); otherwise it is counted by the first of `outside`, `type`, `status`, `result`,
  `volume` it fails. Its **key** is its series — the event ticker before its first hyphen, which `GET /series/{key}`
  must answer as its own ticker or the draw is BLOCKED.
- **Polymarket** (`poly_class`): for each day, gamma's `GET /markets/keyset` with `limit=100`, `closed=true` and
  `end_date_min`, `end_date_max` an hour past both ends, page by page on its `next_cursor` — gamma refuses an `offset`
  past about 5,000 (map §6). A market is a row where it **closed at or before 2026-11-23 12:00:00 UTC** (`CLOSED_BY`),
  its document is the CTF protocol's — `version` `v1`; before 2026-11-23 a `v2` document is the venue's Protocol V2
  pilot, its soak-test series and pilot listings — its `endDate` falls in one of the six days, it has two outcomes and
  two tokens, it resolved wholly to one (`outcomePrices` `["1","0"]` or `["0","1"]`), it carries its `closedTime` and an
  event; otherwise it is counted by the first of `late`, `version`, `outside`, `shape`, `result`, `close`, `event`.
  **Why the instant:** Polymarket keeps closing a day's markets for weeks, and since the migration its listing carries
  the pilot's markets of days already past — 2026-11-12's grew by `2,532` `v2` and `8` `v1` markets between 2026-11-22
  and 2026-11-27 (map §7 item 203) — so the frame takes the `v1` markets closed by a fixed instant, the same set
  whenever it is read. **No volume filter:** gamma's volume fields are absent on most closed markets, traded ones among
  them (map §6; §7 item 201). Its **key** is its event's series, or its event where it has none.
- A market listed more than once — by two days' listings, within an hour of the boundary between them, or twice by
  one — is classified at its first listing alone, and a listing that returns a market outside the range it asked for is
  BLOCKED; each frame is written sorted by day, key and id (`build_frame`). **A day's listing of more than `400` pages on
  Kalshi or `3,000` on Polymarket, or a frame of more than `100,000` series-days, is BLOCKED** (`FRAME_PAGES_MAX`,
  `GROUPS_MAX`): about three times the most pages either venue's listing took on the days the Architect counted (§6),
  and about thirty times six days of Kalshi's `517` series of 2026-11-12. **G-FRAME:** every one of the six days holds
  rows on both venues.

**The draw — two stages, with replacement, fixed here** (`uidx`, `run_draws`). A venue's **groups** are its
`(day, key)` pairs in order. Draw `k = 0, 1, 2, …` takes group `uidx("TZ-56-K0", venue, k, 1, groups)` and in it row
`uidx("TZ-56-K0", venue, k, 2, rows)` — the SHA-256 of `TZ-56-K0|<venue>|<k>|<stage>`, big-endian, modulo the count.
Every series and day weighs alike, so that no family of markets — a day's hundreds of strikes on one price — outweighs
the rest. A drawn market is read once and its result kept for every later draw of it. **A member** is a draw whose
market's fee is readable as below and which has at least one counted trade; every other draw is a non-member, recorded
with its reason — `no_trade`, or on Kalshi `fee_type` (not quadratic), `fee_changed` (a series fee change from a day
before the window to two after it) or `fee_event` (any override of its event's fee), on Polymarket `fee` (a schedule
that is not the venue's). **The draws run until the 5,000th member** — at most `20,000` draws on Kalshi and `40,000`
on Polymarket, more than twice what the 2026-11-12 rates need (§6); fewer members than 5,000 is G-SET's BLOCK.
Because each draw is independent and uniform at each stage, **the members are independent draws from one population:
the six days' qualifying markets, each weighed by its group's share** — so the test below is exact for that population
with no assumption about how markets move together, and its reading is about these six days (below).

**A member's trades** (`kalshi_trade`, `poly_trade`): every taker's trade of the market executed in **`[close −
86,400 s, close)`** — Kalshi's `close_time`, Polymarket's `closedTime` — that **acquired a side at a price `p` with
`0.80 ≤ p < 0.95`**: on Kalshi the side `taker_outcome_side` names at that side's price, block trades out; on
Polymarket a `BUY` of an outcome at its price, or a `SELL` of the other at `1 − p`, the same exposure at the price a bot
would pay at that instant, each fill's token asserted its outcome's. Kalshi's trades are read by `GET /markets/trades`
for the ticker between those instants, every page; Polymarket's by Data API v2's `/v2/trades` for the condition,
`taker_only=true`, newest first, until a page reaches past the hold. **The fee** (`kalshi_market`, `poly_kappa`) is the
taker's fee the venue states at the run: on Kalshi `M × 0.07 × p × (1 − p)` a contract, `M` its series'
`fee_multiplier`; on Polymarket `rate × p × (1 − p)` a share, `rate` its document's `feeSchedule` with `exponent` 1 and
`takerOnly` — or 0 where its fees are off. Polymarket's closed documents carry the venue's current rates, not those of
their days (§7 item 201): the reading counts the fee a taker pays now, which is the fee a bot of ours would pay.

**A member's money** (`money`): `y` = the mean over its counted trades of `1{the side won} − p − fee(p)` — the money a
contract of a taker who bought the favourite at a random one of those instants and held it to settlement. `y` lies in
`(−1, 1/5]`. Kalshi's side won where `result` is its side; Polymarket's where `outcomePrices` puts `1` on it. **A label
is read only by `score`** (§2 item 8).

**The test** (`bet_log`, `reading`) — Ville's inequality on two betting capitals a venue, the betting form of
Waudby-Smith and Ramdas (2023). `x = (y + 1) / (6/5)` maps a member into `(0, 1]`.

- **EARN** rejects that the population's mean `y` is at most `0`: the capital `∏ (1 + λᵢ (xᵢ − 5/6))`.
- **NO EARN** rejects that it is at least `δ = 1` cent a contract: the capital `∏ (1 + λᵢ (101/120 − xᵢ))`.
- `λᵢ = min(d / vᵢ, cap)`, `vᵢ` the running variance of the members before the i-th — `vᵢ = (1/4 + the sum over j < i of
  (xⱼ − μⱼ)²) / i`, `μⱼ = (1/2 + x₁ + … + xⱼ) / (j + 1)` — so every bet is fixed before its member is read. `d` is the
  named alternative's distance in `x`: `1/60` for each, EARN aiming at `+2` cents a contract and NO EARN at `−1` cent.
  `cap` is `3/5` and `60/19`: no factor falls below `1/2`.
- Under each null each capital is a nonnegative supermartingale, whatever the population, so the probability it ever
  reaches `400` is at most `1/400` (Ville). **EARN** where the EARN capital's log reaches `ln 400`, **NO EARN** where
  only the NO EARN capital's does, **UNDECIDABLE** otherwise; EARN first where both do. **False-reading probability:
  at most `1/400` a venue and answer, `1/200` an answer family-wise over the two venues** — exact for the population
  the draws sample, the hash being the draw's only source of chance.
- Every figure at 60 significant digits (`C60`); every member's money in exact rationals.

**Power, before any label — deciding nothing after one** (CANON PART II). The Architect simulated the test, his own
code, on the members of 2026-11-12 he drew by the same rule under another salt — Kalshi `300` members, mean `y`
`+2.20` cents, standard deviation `0.21`; Polymarket `300`, `+2.31` cents, `0.25` — single-side members' outcomes
redrawn at their prices shifted to the alternative, members that bought both sides kept as observed, 500 runs a point.
**At 5,000 members: EARN at a true `+2` cents — Kalshi `0.79`, Polymarket `0.86`; NO EARN at a true `−1` cent —
Kalshi `0.98`, Polymarket `0.91`.** At a true `0` NO EARN reads `0.22` and `0.17` of the time, at `+1` cent EARN `0.04`
and `0.07`: **between about `−0.5` and `+1.5` cents a contract the reading is most often UNDECIDABLE.** In-sample, on a
day the Architect read; no datum of K0.

**What a reading is, and is not.** The test is exact for the six days' population of qualifying markets, each weighed
by its group: **EARN says those six days paid the favourite's buyer after the fee, beyond what the draw's chance
explains.** It does not remove what moved every market of a week together — a calm week favours favourites — and it
counts the prices takers chose to pay, not those a bot of ours would meet at times of its own; `score` prints, barred,
the money day by day, on the trades at least `300` s before the close, on members that bought both sides, and by
category, so that the verdict sees both. Each is a reason K1 and K2 exist: a live step at the minimum size and a fixed
loss measures our own fills.

**The decisions, fixed now** (CANON PART II, the K track): **EARN on both venues** — the favourite runs first on
Polymarket, from the live host and the wallet already built, and Kalshi follows; **EARN on Kalshi alone** — K1;
**NO EARN on Kalshi** — the K track closes; **EARN on Polymarket while Kalshi is not EARN** — the favourite's live step
on Polymarket opens all the same, its own TZ, since that is the venue we already trade [the Architect's decision of
2026-11-22, fixed here before any of its days is read]; **UNDECIDABLE** closes nothing and admits nothing.

**The venues, read by the Architect on 2026-11-22 and again on 2026-11-27** (map §7 item 87's rule; map §6): Kalshi's
listing, trades, series, fee changes and historical cutoff — markets and trades before 2026-09-28 only through
`/historical/*` on 2026-11-27, six days later than on 2026-11-22, so `draw` asserts the cutoff leaves every member's
market and trades in the live set (`kalshi_open`); its fee schedule, `round up(M × 0.07 × C × P × (1 − P))` to a
centicent, effective 2026-07-07 — the rounding a centicent an order, which the reading leaves out; its rate limit, a
trades read `50` of a `600` bucket and refusals `429` with a reset of about `2.8` s, which `Net` waits out, twenty tries
at most. Polymarket's keyset listing, its closed documents' current fee terms and absent volumes, every document's
`version` and the pilot's markets in it (§7 item 203), and Data API v2's fills newest first. Kalshi's member agreement
restricts members located in Poland; its public data answers this host all the same — TZ-56's probe, 9 of 9 endpoints,
and its rehearsal's 355 requests, none refused (§7 item 202) — and §3.4's probe reads it first again.

**The path, proved by the Architect on 2026-11-27, from 20:48 to 21:10 UTC.** Under Python 3.12.3: `selftest` 67 of
67; `rehearse` against the venues, then the reference over its kept replies and `agree`, **12 of 12 figures equal**; the
same three steps on his earlier replies of 17:52 and 20:48, `rehearse` replaying them, 12 of 12 each; then the whole
path at one day's size on a test copy that changed only the days, the instants, the salt and the counts — its `frame`
and `draw` to 300 members a venue, kept since 2026-11-22, rebuilt by `redraw` with this file's code 4 of 4 files byte
for byte, `score` twice and `pack` twice, the same bytes. Its rates and peaks are §0.4's and §6's.

**What this TZ decides.**

1. **The instrument**, `research/tz56-k0-favourite.py`, on the branch `tz-56a-k0-favourite`; `main` carries it once the
   Boss merges after the verdict.
2. **The frames and the draws on disk under their SHA-256 in `state.json`, rebuilt from their kept replies byte for
   byte, and the instrument's commit on `origin`** — and only then the labels, read once a run by `score`.
3. **K0's reading on each venue**, and through §1's decisions the K track's next step.
4. **The Release `tz-56a-k0-inputs`** on a lightweight tag at the instrument's commit: both frames and draws, every reply
   kept, the score and the rehearsal's replies, verified by name, size, digest and a full anonymous download.
5. **Nothing on the host is touched** but this TZ's tree, the forensic store by exclusive create, and the directories
   earlier sessions left (§9).
6. **TZ-56's pull request #54, closed unmerged**, its branch `tz-56-k0-favourite` kept (§3.1).

**Data hygiene** (map §7 item 96). **No market of the set has been read by anyone:** the Architect's reads stop at
Kalshi's markets closing 2026-11-12 — its whole listing, about 1,500 drawn markets' trades and their series — and
Polymarket's ending 2026-11-12 — its keyset listing and about 1,300 drawn markets' fills — each read again on 2026-11-27
for the rehearsal; the counts of Kalshi's listings of 2026-11-08 to 2026-11-15 and of Polymarket's of 2026-11-06 to
2026-11-11 and 2026-11-13, pages and markets alone; TZ-56's run, which read 2026-11-12 again on the capture host and
nothing of the six days; and the venues' documentation, fee pages, series list, fee-change
lists and cutoff (CANON §1.8; map §5). Every constant of this TZ — the frames' rules, the salt, `NEED`, the hold, the
band, `δ`, the alternatives and `α` — was fixed on what 2026-11-12 showed and on the CANON alone; the instant and the
version rule on 2026-11-12's listing as it read on 2026-11-27. §2 bars any read of the six days outside the instrument's
modes.

---

## 2. Scope

**Repository paths this TZ may write, and no others:**

1. `research/tz56-k0-favourite.py` — new, byte for byte Appendix A's, on branch `tz-56a-k0-favourite`, then a pull
   request. Not merged by the Executor.
2. `CryptoReports/TZ-56a-k0-favourite-report.md` — straight to `main`, in one commit. **The one path pushed to `main`,
   and the exemption to item 7 below.**

**Remote objects it creates or changes:** the branch and its pull request; TZ-56's pull request #54, closed unmerged
with one comment naming this TZ, its branch kept; **and, by B-UPLOAD alone, the Release on the
lightweight tag `tz-56a-k0-inputs` at the instrument's commit**, published and not the latest, with §3.10's assets —
**the named exemption to items 8 and 10:** they carry the six days' prices, results and every reply, because publishing
a reading's inputs is CANON hard rule 16.

**Host paths it may write:** `/root/tz56a-work/**`; `/root/btc-forensics/`, by exclusive create only (§9); and in the
primary checkout `/root/btc-5m-twap`, its `.git` for the branch and the worktree, and its `CryptoReports/` for the
report. **Host paths it removes, under §9 alone:** `/root/tz56a-work/` with its worktree, and the directories `I scratch`
names earlier.

**Prohibited, each absolutely:**

1. No committed file is modified; every `frozen` row of map §0 is byte-identical at run end.
2. **Nothing under a capture's or a unit's own tree is opened, listed or written** — `/var/lib/btc-recorder`,
   `btc-chainbook`, `btc-pairbook`, `btc-rewardbook`, both archives' state, `/var/lib/adv3-bot`, `/etc/adv3-bot`,
   `/var/lib/liq-guard` and `/etc/liq-guard`: the instrument's audit hook refuses every open and listing there
   (`policy`); only §0.3's `df`, `find`, `grep -c` and `du -sb` and §3.13's repeat of them read those roots.
3. **No unit is signalled, started, stopped, enabled, disabled or changed.** `systemctl show`, `is-enabled` and
   `is-active` are this TZ's reads of a unit, and `journalctl -u` and `/var/log/apt/history.log` its reads of why one
   changed, at §3.13 alone.
4. `/root/tz04a-env/`, `/root/tz01-env/` and every tree of map §3 are not modified; `/root/btc-forensics/` only by §9's
   exclusive create.
5. **Requests:** `api.elections.kalshi.com`, `gamma-api.polymarket.com` and `data-api.polymarket.com`, anonymously,
   through `Net.get` and its headers `User-Agent: btc-5m-twap-tz56`, `Accept: application/json`, `Accept-Encoding:
   gzip`, in `probe`, `rehearse`, `frame` and `draw` alone; `api.github.com`, `github.com` and its download hosts in
   `verify` alone, anonymously; `git` against `origin`; `gh` for the pull requests, git's credential and B-UPLOAD; and
   none from the reference, whose audit hook refuses every socket and request. **No
   other request — no authenticated venue call, no order, no key of any venue — and no read of the six days by any
   command but the instrument's modes.** These bind every request of the session, the Executor's own included (map §7
   item 77).
6. **No process** but `git`, `systemctl` and `stat` from the instrument (`policy`); the shell's own commands as §0, §3
   and §9 name them, the reference `R` among them at §3.5 alone.
7. Nothing is pushed to `main` except the report of item 2.
8. **No label of the set is read before the frames and the draws are on disk under the SHA-256 `state.json` records, and
   the instrument's commit is on `origin`** — `score` asserts both (`label_gate`). A label is a Kalshi market's `result`
   or a Polymarket market's `outcomePrices`. Exemptions, each named because the body needs it: (a) `frame`, which keeps
   a market as a row only where it resolved to one side, keeps every reply verbatim and writes each row's label into the
   frame file uninterpreted — `draw` never reads a row's label; (b) `rehearse` and the reference, which read the labels
   of 2026-11-12, a day already read; (c) `score`, which reads the set's labels once a run, each run a line of the read
   ledger.
9. **The fail-fast stops a venue's draws** where after its 300th draw the time to 5,000 members projects past
   `10,800` s (`run_draws`) — BLOCKED.
10. **No single market's or trade's price, size or result is printed or written outside `/root/tz56a-work/`** but in the
    Release: the instrument prints sums over a frame, a day, a venue's members or a category of at least 30. **This
    binds the Executor's own reads** (map §7 item 118): no file under `run/`, `rehearsal/`, `redraw/` or `release/` is
    printed, whole or in part, by any command but the instrument's modes, the reference — which prints the same sums —
    and `sha256sum`, `stat`, `wc` and `du`;
    `state.json`, the read ledger, `release-set.json`, `verify.json` and every file under `logs/` may be printed.
11. No dataset, archive or binary enters git history.

---

## 3. The work, in this order

From §3.1 on, `nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz56a-work/wt/research/tz56-k0-favourite.py` is
written **`I`**; a mode is `I <mode>`, run from `/root/tz56a-work`. Every command's output goes to `logs/`, one file per
step, and is quoted in the report. **On a BLOCK before §3.1**, §9 runs with `I0` in place of `I` and B-RECLAIM-OWN
without its `worktree remove`; **on a BLOCK or a FAIL after it**, the run goes to §3.13 and §9, skipping every step that
needs a PASS it lacks.

**Where the session's permission classifier refuses a command of a block named B-…**, the Executor prints the block
unchanged, the Boss runs it verbatim in a root shell on the capture host, and the Executor verifies it through the reads
this TZ names — never from the Boss's account (map §6, destructive actions; §7 items 124, 138 and 144).

### 3.1 The branch and its file

```
git -C /root/btc-5m-twap fetch origin
git -C /root/btc-5m-twap worktree add -b tz-56a-k0-favourite /root/tz56a-work/wt origin/main
install -m 0644 /root/tz56a-work/stage/research/tz56-k0-favourite.py /root/tz56a-work/wt/research/tz56-k0-favourite.py
sha256sum /root/tz56a-work/wt/research/tz56-k0-favourite.py
git -C /root/tz56a-work/wt add research/tz56-k0-favourite.py
git -C /root/tz56a-work/wt commit -m "TZ-56a: K0's instrument, its second run - research/tz56-k0-favourite.py"
git -C /root/tz56a-work/wt push -u origin tz-56a-k0-favourite
git -C /root/btc-5m-twap ls-remote origin refs/heads/tz-56a-k0-favourite
```

`sha256sum` prints §0.1's hash; `ls-remote` prints the commit the worktree's `HEAD` names. The instrument is committed
and pushed before any run whose output a Validation row compares (map §7 item 84). Where `git push` fails on
the URL's credential, push through `credential.helper=!gh auth git-credential` (map §6, git remote). Then open the pull
request with `gh pr create --base main --head tz-56a-k0-favourite`, its title the commit's, and close TZ-56's, its
branch kept:

```
gh pr close 54 --repo seahomebatumi-ai/btc-5m-twap --comment "TZ-56 BLOCKED at G-REHEARSAL; superseded by TZ-56a, branch tz-56a-k0-favourite."
```

### 3.2 The self-test

`I selftest` into `logs/32-selftest.log`: **`SELFTEST PASS: 67 of 67 checks`**, no request (§7 V3).

### 3.3 The units, and the directories beside this session

`I still` into `logs/33-still.log` records the five units' `MainPID`, `NRestarts` and `ActiveState`. Then
`I scratch "$(dirname "$S")"` into `logs/33-scratch.log` — its argument the session's own directory, one level above
`$S` — names each UUID directory beside it live or earlier (map §7 items 91, 95 and 150). **B-RECLAIM-SCRATCH**, for
the earlier ones alone, one paste:

```
cd /root/tz56a-work && I=(nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz56a-work/wt/research/tz56-k0-favourite.py) && "${I[@]}" reclaim <each directory scratch named earlier> >> logs/33-reclaim-scratch.log 2>&1 && rm -rf <the same directories> && for d in <the same directories>; do test -e "$d"; echo "$d exit=$?"; done >> logs/33-reclaim-scratch.log
```

Each `test -e` prints `exit=1`. Where `scratch` names none earlier, the block is not run and the report says so.

### 3.4 G-PROBE

`I probe` into `logs/34-probe.log` (`mode_probe`): one request per endpoint through `Net.get` — Kalshi's exchange
status, historical cutoff, a listing page and a trades page of 2026-11-12, one series, both fee-change lists; gamma's
keyset page and a Data API trades page of 2026-11-12 — each asserted served `200` and parsed with its keys, its bytes,
SHA-256 and the request's headers printed, Kalshi's cutoff printed whole. **`G-PROBE PASS: 9 of 9`**; any refusal is
BLOCKED and printed in the venue's words (map §7 item 191) — Kalshi refusing this host's address among them (§7 item
202). No request of the six days.

### 3.5 G-REHEARSAL

`I rehearse` into `logs/35-rehearse.log` (`mode_rehearse`): 2026-11-12 on both venues, frame and draws to 60 members
under the salt `TZ-56-K0-REHEARSAL`, every reply kept under `rehearsal/`; its twelve figures and the SHA-256 of its eight
kept-reply files written to `rehearsal/instrument.json`. About six minutes. Then the reference over those replies, no
request:

```
cd /root/tz56a-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz56a-work/stage/reference/tz56a-k0-reference.py /root/tz56a-work/rehearsal > logs/35-reference.log 2>&1; echo "exit=$?" >> logs/35-reference.log
```

`exit=0` and `reference: wrote /root/tz56a-work/rehearsal/reference.json`. Then `I agree` into `logs/35-agree.log`
(`mode_agree`): the eight files still at the SHA-256 `rehearse` recorded, and the reference's record of them the same;
the twelve figures compared, each printed. **`G-REHEARSAL PASS: 12 of 12`**; any difference is BLOCKED.

### 3.6 The frames — G-FRAME

```
cd /root/tz56a-work && while [ "$(date -u +%s)" -lt 1795435200 ]; do sleep 60; done; date -u
```

then `I frame` into `logs/36-frame.log` (`mode_frame`), **in the background** (the harness's own; map §6, harness), the
log read until its last line. It frames Kalshi, then Polymarket, over the six days, every reply kept in
`run/raw-frame-<venue>.jsonl.gz` before it is used. **Where the process ends before its last line** — the session's
restart, a dropped connection — **`I frame` is run again, appending to the same log:** it replays every reply it kept,
asserting each answers the very request it makes, cuts off a reply cut short, and goes on from there (`Source`).
**`G-FRAME PASS`**: every one of the six days holds rows on both venues. About fifteen to twenty-five minutes (§6).

### 3.7 The draws — G-SET

`I draw` into `logs/37-draw.log` (`mode_draw`), in the background, run again on an early end exactly as §3.6. Kalshi's
draws, then Polymarket's, each to 5,000 members, every reply kept in `run/raw-draw-<venue>.jsonl.gz`; each venue's
draws written to `run/draws-<venue>.jsonl` and its SHA-256 to `state.json`. **`G-SET PASS: 5000 members on each venue`.**
The fail-fast (§2 item 9) prints its projection after each venue's 300th draw. About one and a half to two and a half
hours (§6).

### 3.8 DETERMINISM — the frames and the draws again, from the kept replies alone

`I redraw` into `logs/38-redraw.log` (`mode_redraw`): no request; both frames and both venues' draws rebuilt from the
kept replies under `redraw/`, each file's SHA-256 equal to the one `frame` and `draw` wrote and `state.json` records.
**`DETERMINISM PASS: 4 of 4`.**

### 3.9 The score, twice

`I score` into `logs/39-score-1.log`, then again into `logs/39-score-2.log` (`mode_score`): `label_gate` first; each
venue's members, mean money a contract after the fee, before it and the fee, both log capitals beside `ln 400`, and the
reading; the barred lines; `run/score.json` written by the first run and asserted byte for byte by the second
(**DETERMINISM**). The report prints the instant §3.1's push reached `origin` beside the instant of `score`'s first run
(map §7 item 63).

### 3.10 The pack

`I pack` into `logs/310-pack-1.log`, then again into `logs/310-pack-2.log` (`mode_pack`): the Release's thirteen assets
under `release/` — both frames and both draws gzipped, the four kept-reply files and the score as they are, the
rehearsal's four kept-reply files — each name, bytes and SHA-256 printed, `release-set.json` and `release-notes.md`
written by the first run and asserted byte for byte by the second.

### 3.11 B-UPLOAD — the Release

One paste, the Executor's attempt first, the Boss's where it is refused:

```
cd /root/tz56a-work && C=$(git -C wt rev-parse HEAD) && test "$(git -C /root/btc-5m-twap ls-remote origin refs/heads/tz-56a-k0-favourite | cut -f1)" = "$C" && grep -q "\"commit\": \"$C\"" release-set.json && gh release create tz-56a-k0-inputs --repo seahomebatumi-ai/btc-5m-twap --target "$C" --title "TZ-56a K0 inputs" --notes-file release-notes.md --latest=false >> logs/311-upload.log 2>&1 && gh release upload tz-56a-k0-inputs --repo seahomebatumi-ai/btc-5m-twap release/tz56a-* >> logs/311-upload.log 2>&1; echo "exit=$?" >> logs/311-upload.log; date -u >> logs/311-upload.log
```

`exit=0` and its date. B-UPLOAD sits inside the run at the point that needs it, never before `EXECUTE` (map §7 item
132). A failed upload of some assets is answered by `gh release upload … --clobber` of the same files,
one paste, and nothing else; the Release is never deleted.

### 3.12 G-TAG, G-UPLOAD and G-DOWNLOAD

At least `120` s after B-UPLOAD's date (map §6, GitHub Releases), `I verify` into `logs/312-verify.log`
(`mode_verify`), with no credential: the Release on `tz-56a-k0-inputs` holds the thirteen assets by name, size,
`uploaded` state and `sha256:` digest, none beyond them; each downloads anonymously to its set's bytes and SHA-256; the
tag on `origin` is lightweight at the pack's commit. **`G-UPLOAD PASS: 13 of 13 … G-DOWNLOAD PASS: 13 of 13 … G-TAG
PASS`**, `verify.json` written.

### 3.13 The units again, and the closing reads

`I still` into `logs/313-still.log`: **G-STILL** — the five units' `MainPID`, `NRestarts` and `ActiveState` as §3.3
recorded them; a change is FAIL, printed, its cause read from `journalctl -u <unit> --since <§3.3's instant>` and
`/var/log/apt/history.log`'s last 40 lines into the same log (map §7 item 120's rule), and changes no reading. Then
§0.3's commands again into `logs/313-host.log`, and `git -C /root/btc-5m-twap ls-remote origin` as §0.5 prints it.

---

## 4. The gates — fixed here, before any of their data exists

### 4.1 G-REHEARSAL

2026-11-12, read already: `rehearse`'s twelve figures — on each venue the frame's rows, its series-days and its other
rows by reason, the draws to 60 members, the draws' label-free SHA-256 (`draws_digest`) and the members' money before
the fee, summed — **equal to the reference's, Appendix B's, computed from the same eight kept-reply files**: each program
records every file's SHA-256, and `agree` asserts the two records equal and the files still at them. **PASS: 12 of 12
equal.** Recorded and compared with nothing: the members' fee coefficients, by their SHA-256 (§7 item 201). The
rehearsal's in-sample readings are printed nowhere.

**The Architect's runs of both programs, 2026-11-27, Python 3.12.3:**

| 2026-11-12's replies | Kalshi `draws_digest` | Polymarket `draws_digest` | the two programs |
|---|---|---|---|
| read at 17:52 UTC | `5b2a880d…e33c3` | `77444d74…30a3` | equal, 12 of 12 |
| read at 20:48 UTC — TZ-56's frame and draws, byte for byte | `5b2a880d…e33c3` | `2beb4bb3…5eef` | equal, 12 of 12 |
| read at 21:00 UTC, then the reference and `agree` | `5b2a880d…e33c3` | `2beb4bb3…5eef` | `G-REHEARSAL PASS: 12 of 12` |

### 4.2 G-PROBE — `9 of 9` endpoints served `200` and parsed (§3.4).

### 4.3 G-FRAME — on each venue, every one of the six days holds at least one row (§3.6).

### 4.4 G-SET — on each venue, `5,000` members within `20,000` (Kalshi) or `40,000` (Polymarket) draws; the fail-fast
of §2 item 9 not tripped (§3.7).

### 4.5 DETERMINISM — `redraw`'s four files and `score`'s and `pack`'s second runs, byte for byte (§3.8 to §3.10).

### 4.6 K0's reading, on each venue

| reading | where |
|---|---|
| **EARN** | the log of the EARN capital at or above `ln 400` = `5.991464547107981986870447152285081551353203245978056460308015820921932` |
| **NO EARN** | not EARN, and the log of the NO EARN capital at or above `ln 400` |
| **UNDECIDABLE** | neither |

`α = 1/400` a venue and answer by Ville's inequality; **`1/200` an answer family-wise over the two venues.** Power at
5,000 members, the Architect's simulation (§1): EARN `0.79` (Kalshi) and `0.86` (Polymarket) at a true `+2` cents a
contract; NO EARN `0.98` and `0.91` at a true `−1` cent. **Power qualifies a silence, never a reading** (map §7 item
60). Then §1's decisions.

### 4.7 G-UPLOAD, G-DOWNLOAD and G-TAG — `13 of 13` by the API's record, `13 of 13` by download, the tag lightweight at
the pack's commit (§3.12).

### 4.8 G-STILL — the five units unchanged from §3.3 to §3.13; recorded, reading nothing.

---

## 5. The instrument

`research/tz56-k0-favourite.py`, Appendix A, standard library alone, Python 3.12. Its modes are its docstring's.
**`Net`** makes every venue request: one at a time, at least `0.25` s apart on Kalshi and `0.1` s on gamma and the Data
API, gzip asked and undone, `429` and `5xx` and a dropped connection asked again after the venue's own reset hint or
`2^try` s, twenty tries at most, any other refusal BLOCKED in the venue's words. **`Sink` and `Source`** keep every
reply before it is used — one gzip member of one JSON line a reply, its URL, bytes, SHA-256 and body — and replay them
in order, each asserted to answer the very request the code makes, so that a mode run again resumes and `redraw`
rebuilds every file from them alone. **`build_frame`**, **`run_draws`**, **`money`**, **`bet_log`** and **`reading`**
are §1's rules. **Memory holds a page, a sorted run and the groups — never a listing, a frame or a set of draws:**
`build_frame` writes every listed market as a line of an index on disk, sorted by id to keep each market's first listing
and then, for the kept rows, by day, key and id (`sorted_lines`: runs of `50,000` lines merged in one pass);
`FrameIndex` holds a frame's groups, `100,000` at most, and reads each row's offset from a file beside the frame;
`run_draws` writes each draw as it is made, and `pack` compresses a megabyte at a time. **`policy`**, an audit hook
installed at import, refuses every open, listing, request and process §2 does not give the running mode. `score`, `pack`
and `verify` hold the label gate, the Release's set and its proof; `still`, `scratch` and `reclaim` the host's. Every
mode prints its peak, glibc's settings and the hook's refusals on every exit (map §7 item 151). **Every draw considered,
member or not, is a line of its venue's draws file with its reason, in order, published in the Release** — the
population disclosed whole (map §7 item 105); the logs print its counts.

**The reference**, `reference/tz56a-k0-reference.py`, Appendix B, standard library alone, Python 3.12: the Architect's
own implementation of §1's frames, draw and money, written apart from Appendix A and sharing no code with it — its own
listing walk, classification, groups, draws, sums, digest and money. It reads nothing but `rehearsal/`'s kept-reply
files: it indexes every kept reply by its request — the URL's host, path and query pairs, order aside — asserts each
whole by its own SHA-256, looks every request it makes up there, and BLOCKs on any it cannot find. **It makes no
request:** its audit hook refuses every socket and request, and every write but `rehearsal/reference.json`, which a
second run must write byte for byte the same.

---

## 6. Cost

At the populations' upper bounds, from the Architect's runs of 2026-11-22 and 2026-11-27 (§1, the path). **The
listings' pages a day on the days counted** (map §6): Kalshi `103` to `138`, 2026-11-08 to 2026-11-15; Polymarket
`245` to `987`, 2026-11-06 to 2026-11-13, the weekend the largest — 2026-11-21, a Saturday, is in the set.

| step | requests | wall clock | compute | at its bound |
|---|---|---|---|---|
| `probe` | 9 | under 30 s | under 1 s | — |
| `rehearse` | about 813 | about 6 min | under 30 s | 2026-11-27, 21:00 UTC: Kalshi's 103 pages and 252 requests in 223 s, 43 refused once; gamma's 288 pages and 170 Data API requests in 122 s |
| the reference, `agree` | 0 | under 1 min | about 10 s | 813 kept replies indexed and read again; `11` s on 2026-11-27 |
| `frame` | about 690 Kalshi and 2,500 gamma | about 15 to 25 min | about 3 min | `FRAME_PAGES_MAX` 400 and 3,000 a day: about 30 and 85 min, the synthetic caps sorted in `224` and `406` s |
| `draw`, Kalshi | about 10,000 | about 60 to 110 min | under 5 min | 20,000 draws, about 2 requests each at most; 2026-11-12: 507 draws, 982 requests, 387 s; at the bound with no network, `97` s |
| `draw`, Polymarket | about 14,000 | about 45 to 75 min | under 5 min | 40,000 draws; 2026-11-12: 864 draws, 643 requests, 180 s; at the bound with no network, `51` s |
| `redraw` | 0 | about 5 min | about 5 min | every kept reply parsed once more, the frames sorted again |
| `score` ×2, `pack` ×2 | 0 | under 2 min | under 2 min | 60,000 draws, 10,000 members' two capitals at 60 digits |
| `verify` | 2 API, 13 downloads | under 3 min | under 1 min | about 420,000,000 bytes, 720,000,000 at the draws' bounds, at map §6's 13,000,000 a second |

**The fail-fast:** a venue's draws projected past `10,800` s after its 300th draw (`run_draws`), from that venue's own
draws and members so far — at 2026-11-12's rates, 300 draws, 181 members and 180 s on Kalshi, it would project about
`4,970` s for about 8,300 draws, and on Polymarket, 300 draws, 96 members and 76 s, about `3,960` s, so it trips below
about half those rates. **No step reaches `3,600` s of compute**; the wall clock is the venues' rate limits, and every
step that waits on them resumes from its kept replies.

**What could BLOCK, and where:** a refusal of a venue (§3.4 or later, in its words); the rehearsal's twelve figures; a
listing past its pages cap or a frame past `100,000` series-days; a frame day without rows; fewer than 5,000 members;
the fail-fast; Kalshi's historical cutoff reaching into the days (`kalshi_open`); a series that does not answer as its
key; any replay that answers another request; the label gate; any determinism; the Release's proof. **Each is BLOCKED
where it stands; nothing is retried but a mode run again to resume.**

---

## 7. Validation

Every check is an assert of the mode named, quoted from its log.

| # | step | read | must print |
|---|---|---|---|
| **V1** | §0.2 | `I0 fingerprint` | `FINGERPRINT PASS: revision 2026-11-28-a; anchors 6 of 6, 4 re-derived; rows 74: frozen 71 of 71 equal, tracked 2, reported 1` |
| **V2** | §0.5 | `I0 number` | `NUMBER PASS - 2 of 2` |
| **V3** | §3.2 | `I selftest` | `SELFTEST PASS: 67 of 67 checks`; `opens, requests and processes refused: 0` |
| **V4** | §3.4 | `I probe` | `G-PROBE PASS: 9 of 9 endpoints served and parsed` |
| **V5** | §3.5 | `I rehearse`, the reference, `I agree` | `rehearsal: 12 figures and 8 kept-reply files written for agree`; the reference's twelve figures, `reference: wrote …reference.json` and `exit=0`; eight `kept … sha256` lines, twelve `G-REHEARSAL … equal` lines and `G-REHEARSAL PASS: 12 of 12 figures equal to the reference's on the same kept replies` |
| **V6** | §3.6 | `I frame` | `now <the run's instant>Z, at or after 2026-11-23T12:00:00Z`; each venue's day with its pages and markets listed; each venue's rows by day, six days each above 0; `G-FRAME PASS` |
| **V7** | §3.7 | `I draw` | each venue's projection line; `G-SET PASS: 5000 members on each venue` |
| **V8** | §3.8 | `I redraw` | four `… equal` lines and `DETERMINISM PASS: 4 of 4` |
| **V9** | §3.9 | `I score` twice | `label gate: …`; both venues' lines; `K0: Kalshi <reading>, Polymarket <reading>`; the second run `unchanged …score.json` |
| **V10** | §3.10 | `I pack` twice | thirteen `asset` lines; `PACK: 13 assets`; the second run's `unchanged` lines |
| **V11** | §3.11 | B-UPLOAD | `exit=0` and its date |
| **V12** | §3.12 | `I verify` | thirteen `V` lines, `api True`, `download True`; `G-UPLOAD PASS: 13 of 13 … G-DOWNLOAD PASS: 13 of 13 … G-TAG PASS: tz-56a-k0-inputs at <commit>` |
| **V13** | §3.13 | `I still` | `G-STILL PASS` or `FAIL` with its cause |
| **V14** | §9 | `I reclaim`, B-RECLAIM-OWN | `RECLAIM PASS: …`; each `test -e` `exit=1` |
| **V15** | every mode | its last lines | `peak memory of this run: <n> bytes`, recorded, not asserted; `malloc tuned: True`; `opens, requests and processes refused: 0` |

---

## 8. The report

The contract's §8, and in its `## 2. Measurements`: each venue's frame — rows, groups, the others by reason, rows by
day; its draws — considered, members, markets fetched, reasons, requests, retries, the time; the reference's output
whole; the score's every line, the barred ones under their own heading; the Release's assets; the closing of TZ-56's
pull request #54. In `## 4. Gate`: §4.6's
table filled for each venue — the two log capitals to six decimals, the mean money a contract after the fee to four, the
reading — and §1's decision it takes. Every figure is quoted from a log line the instrument or the reference printed
(map §7 item 82).
The report names by SHA-256 `state.json`, `release-set.json`, `verify.json` and `run/score.json`.

---

## 9. Reclaim — the host left clean (CANON hard rule 15)

In this order, once §3.13 has run:

1. **The report's draft**, `CryptoReports/TZ-56a-k0-favourite-report.md` in the primary checkout, uncommitted, naming by
   SHA-256 every file it cites — `state.json`, `release-set.json`, `verify.json` and `run/score.json` among them.
2. **`I reclaim /root/tz56a-work`** into `logs/9-reclaim.log` (`mode_reclaim`): every file the reports in
   `CryptoReports/` name by hash — the draft counts — or keep by name — `state.json`, `read-ledger.jsonl`,
   `release-set.json`, `verify.json`, `release-notes.md` and every file under `logs/` — copied into
   `/root/btc-forensics/` as `tz56a-work--<path with / as -->` by exclusive create and its hash checked, **but a file the
   Release holds by that hash, which is named with its asset and left to it** (map §7 item 167); the worktree asserted
   to hold no file but its `HEAD`'s, at its upstream's. **No `reclaim`'s output is filtered** (map §7 item 119):
   `RECLAIM PASS`.
3. **B-RECLAIM-OWN**, one paste, its output into the scratchpad — the one exception of §0.0 — and quoted whole in the
   report:

```
cd /root && git -C /root/btc-5m-twap worktree remove /root/tz56a-work/wt && rm -rf /root/tz56a-work && test -e /root/tz56a-work; echo "tz56a-work exit=$?"; git -C /root/btc-5m-twap worktree list
```

   `exit=1`, and the worktree list holds the primary checkout and `/root/btc-recorder-svc` alone.
4. **The report**, finished from the logs' forensic copies and B-RECLAIM-OWN's output, committed and pushed to `main`.

---

## 10. Pre-send checks

Performed on this file as sent, in a reading separate from its writing; every count below re-derived for it.

| # | check | result |
|---|---|---|
| **C1** | scope against body | **Named by the body, each inside §2.** *Repository, written:* `research/tz56-k0-favourite.py` on the branch `tz-56a-k0-favourite` and its pull request, the report on `main` — §2 items 1 and 2. *Read:* this file by §0.1's script; `SYSTEM-MAP.md` and its table's 73 files by `fingerprint`; `CryptoTZ/` and `CryptoReports/` names by `number`; `CryptoReports/*.md` by `reclaim`'s tokens; the refs by `ls-remote`. *Remote:* the branch, its pull request, TZ-56's pull request #54 closed unmerged, and the Release `tz-56a-k0-inputs` — §2's remote objects. *Host, written:* `/root/tz56a-work/**` — `logs`, `stage` with both appendices, `wt`, `run`, `rehearsal` with `instrument.json` and `reference.json`, `redraw`, `release`, `selftest` (made and removed by the self-test), `state.json`, `read-ledger.jsonl`, `release-set.json`, `release-notes.md`, `verify.json`, and beside each frame and draws file under `run/`, `rehearsal/` and `redraw/` the files its code writes and removes — `.rows`, `.ids`, `.kept`, `.run-N`, `.off` and `.tmp` — and `/root/btc-forensics/` by exclusive create; removed: the work tree and the earlier session directories — §2's host paths. *Read:* `/proc`, `df`, `du`, `find`, `grep -c` and `ls`, the stream files' sizes by `find -printf`; five units by `systemctl show`; `telemetry-watch.service` by `is-enabled`; `journalctl -u` and the package history at §3.13. *Network:* §2 item 5's three venue hosts, GitHub's for `verify`, `git` and `gh`; none from the reference. **Intersections found and resolved:** §0.3's and §3.13's reads of the recorder's and the reward book's roots — the stream files' `find` among them — against item 2 — item 2's named exemption; §3.13's `journalctl` and package history against item 3 — named there, at §3.13 alone; `frame`'s labels written into the frame file and `rehearse`'s, the reference's and `score`'s label reads against item 8 — its exemptions (a) to (c), the reference named in (b); the reference's process against item 6 — named there; the reference's prints and the index files under `run/`, `rehearsal/` and `redraw/` against item 10 — the reference named there, the index files under its bar and removed by the code that wrote them; PR #54's closing against §2's remote objects — named there; the Release's prices, results and replies against items 8 and 10 — the remote objects' named exemption. **By content class:** an output carrying a price, a size, a result or a reply — the frames, the draws, the kept replies, the index files, `instrument.json`, `reference.json` and `score.json`, all under `/root/tz56a-work/` and in the Release; every mode's log and the reference's print counts, sums over a venue's members, its days or a category of at least 30, hashes, sizes and keys — `probe` the keys of its replies and Kalshi's cutoff alone. **No other intersection.** |
| **C2** | origin of every expectation | **An identity between two implementations written apart, holding for every admissible reply:** §4.1's twelve figures — `rehearse`'s against the reference's, Appendix B, the Architect's own code sharing none with Appendix A, both computed from the same kept bytes; the Architect's three runs of both on 2026-11-27 (§4.1's table) are evidence, not expectations, and no literal of them is asserted. `ln 400` to 70 digits and the self-test's `bet_log` literals to 70 — `mpmath` at 110 digits, the bets' recursion written apart; the self-test's instants — `datetime`; its draw indices — `hashlib` directly; **`67` checks — counted by a tracer outside the self-test's own counter, `67` calls of `ok`**; §0.1's lines, bytes and SHA-256 — `wc` and `sha256sum` over the extracted bytes, and §0.1's script run against this file. **Quoted from a committed artifact:** V1's revision and `74`, `71`, `2`, `1` — map §0 of revision `2026-11-28-a`, which ships with this file; map §6's `7,300,000,000`, `445,535,636` and `MemAvailable` range; TZ-56's report for its figures, reads and peaks. **Integer arithmetic on this file's own constants, asserted by the self-test:** `MEM_FLOOR` `157,499,106` = `2 × ⌈65,679,360 × 1.199⌉`, the reference's `FLOOR` the same literal; `DISK_GATE` − `DISK_FLOOR` = `1,300,000,000`. **Measured by the Architect, not expectations:** §0.4's peaks and §6's rates, pages and times, which set floors, caps and bounds and are asserted by nothing; V15 records the host's peaks. **Inequalities, holding for every admissible value:** `MemAvailable` and free space at or above their floors; a day's pages and a frame's series-days at or below their caps; members at `5,000` within the draws' bounds; the fail-fast's projection at or below `10,800` s. **No expectation depends on a quantity this TZ measures.** |
| **C3** | shape of every diff | `research/tz56-k0-favourite.py` is new on `main`'s tree — TZ-56's pull request was never merged: no committed line is replaced. The reference is staged and never committed. No other file of the repository changes. |
| **C4** | cost of every check | §6, at the populations' upper bounds: `selftest` about `2` s; `fingerprint` about `1` s over 74 rows; `rehearse` about `6` min of wall clock, under `30` s of compute; the reference about `11` s and `agree` about `1` s; `frame` about `15` to `25` min on the counted days' pages, about `3` min of compute, and at its caps, `400` and `3,000` pages a day with every market kept, about `30` and `85` min of the venues' rate and `224` and `406` s of the Architect's compute on synthetic listings; `draw` at most `20,000` and `40,000` draws, about `1.5` to `3` h of wall clock in all, and at the bounds `97` and `51` s of compute with no network; `redraw` about `5` min of compute; `score` and `pack` under `2` min each; `verify` under `3` min; `reclaim` under `1` min over at most `1,300,000,000` bytes. **The fail-fast:** `10,800` s a venue, projected after its 300th draw from its own rate — at 2026-11-12's rates about `4,970` s on Kalshi and `3,960` s on Polymarket, so it trips below about half of them. **No check reaches `3,600` s of compute**; the wall clock is the venues' rate limits, and every waiting step resumes from its kept replies. |
| **C5** | every count | `67` checks — `mode_selftest`'s `ok` calls, by the tracer; `9` endpoints — `PROBES`, nine rows; `12` figures — six a venue, `REH_FIGURES`, `rows`, `keys`, `reasons`, `draws`, `digest` and `gross`, two venues; `8` kept-reply files — `REH_FILES`, and the reference's `FILES`, two kinds and their indexes on two venues; `7` Polymarket reasons — `POLY_REASONS`, and `5` Kalshi's — `KALSHI_REASONS`; `6` days — `DAYS`; `400` and `3,000` pages a day, `100,000` series-days and `50,000` lines a sorted run — `FRAME_PAGES_MAX`, `GROUPS_MAX`, `SORT_CHUNK`; `5,000` members, `20,000` and `40,000` draws — `NEED` and `DRAWS_MAX`; `60` members and `400` draws in the rehearsal — `REH_NEED` and `REH_DRAWS_MAX`, the reference's `NEED` and `DMAX`; `4` files rebuilt — two frames and two draws, `mode_redraw`'s loop; `13` assets — `release_plan`, six a venue and the score; `5` units — `UNITS`; `74` rows, `71` `frozen`, `2` `tracked`, `1` `reported` — map §0's table, read with `ROW` on revision `2026-11-28-a`; `15` V-rows and `8` gates of §4; `33` map items and `14` §6 rows in the header. Each re-derived from the set it counts. |
| **C6** | every population | **A venue's mean money, its two capitals and its reading** — its members, in draw order, a market drawn twice counted twice. **Its frame's counts** — every market its six days' listings returned, each once, at its first listing. **Its draws' reasons and markets fetched** — every draw considered. **Barred:** by day — the members whose market's day it is; slow — the members with a trade at least `300` s before the close, on those trades; mixed and single — the members that bought both sides, and one; by category — a Kalshi series' category or a Polymarket fee type with at least `30` members. **G-REHEARSAL** — 2026-11-12's frames, Polymarket's closed by 2026-11-27 00:00:00 UTC, and its 60 members a venue, computed by both programs from the same eight kept-reply files. **G-STILL** — the five units of §3.3. **Memory and disk floors** — each mode's and the reference's reads at its start, and the disk's while the instrument writes. |
| **C7** | every signature and every behaviour | **No committed function is named:** neither appendix imports the other or any committed file. **Appendix A's own, by its syntax tree:** `policy` lines 221 to 249; `finish_once` 308 to 319; `gz_file_once` 348 to 362; `memory_gate` 396 to 400 and `floor_check` 403 to 414; `uidx` 470 to 474; `Net` 488 to 532, `retry_wait` 535 to 544 — a refusal `429` or `5xx` asked again at line 511, the hint bounded at line 543; `Sink` 551 to 606 and `Source` 609 to 635 — a replay asserted to answer the request it makes at line 622; `kalshi_class` 644 to 662; `poly_kappa` 665 to 676 — fees off `Fr(0)` at line 669; `poly_class` 689 to 723 — `late` at line 697, `version` at line 699; `listing_url` 726 to 736; `tsv` 754 to 759; `sorted_lines` 762 to 789 — a run sorted at line 774, the runs merged at line 782; `build_frame` 792 to 861 — a day's pages capped at line 810, a listing outside its range BLOCKED at lines 816 to 818, a market kept at its first listing at line 836; `FrameIndex` 864 to 908 — its series-days capped at line 883; `kalshi_trade` 956 to 972 — block trades out at line 960, the hold at line 963, the band at line 970; `poly_trade` 975 to 993 — the hold at line 982, a `SELL` as the other side at `1 − p` at line 990, the band at line 991; `kalshi_open` 1005 to 1022 — the cutoff asserted at line 1011; `kalshi_market` 1025 to 1063 — `fee_type`, `fee_changed` and `fee_event` at lines 1041, 1043 and 1045; `poly_market` 1066 to 1090 — `fee` at line 1072; `run_draws` 1096 to 1147 — the two stages at lines 1117 and 1118, each draw written as made at line 1129, members counted at line 1132, the fail-fast at line 1139; `digest_line` 1150 to 1156 and `draws_digest` 1159 to 1164; `money` 1175 to 1181; `bet_log` 1198 to 1218 — the bet at line 1210, no factor below `1/2` at line 1212; `reading` 1225 to 1233 — EARN at line 1230, NO EARN at line 1232; `score_venue` 1236 to 1280; `mode_fingerprint` 1286 to 1313; `mode_number` 1324 to 1331; `mode_still` 1340 to 1354; `mode_scratch` 1383 to 1395; `mode_probe` 1414 to 1432; `venue_phase` 1435 to 1457; `mode_rehearse` 1460 to 1484 — `instrument.json` written once at line 1482; `agreement` 1487 to 1499 — the two records of the kept files asserted equal at line 1490; `mode_agree` 1502 to 1514 — G-REHEARSAL's assert at line 1513; `mode_frame` 1523 to 1547; `mode_draw` 1550 to 1570; `mode_redraw` 1573 to 1591; `label_gate` 1594 to 1609 — its assert at line 1608; `mode_score` 1612 to 1625; `release_plan` 1633 to 1647; `mode_pack` 1650 to 1678; `mode_verify` 1687 to 1733; `mode_reclaim` 1779 to 1837; `main` 1851 to 1875; `mode_selftest` 2016 to 2265. **Appendix B's own:** `_guard` 25 to 32 — every socket and request refused at line 27; `meminfo` 53 to 58; `sha_file` 61 to 66; `norm` 69 to 71; `Kept` 74 to 110 — a request kept twice BLOCKED at line 91, each reply asserted whole by its SHA-256 at line 100, a request with no kept reply BLOCKED at line 106; `t_us` 113 to 122; `pick` 129 to 130; `agg_add` 137 to 145; `kalshi_frame` 148 to 178 — a market at its first listing at line 157; `poly_frame` 181 to 235 — its first listing at line 190, `late` at line 195, `version` at line 198; `grouped` 238 to 245; `kalshi_draws` 248 to 310; `poly_draws` 313 to 357; `figures` 365 to 373 — the digest's line at line 368; `main` 376 to 412 — a second run's bytes asserted at line 402. **Each behaviour §1 and §5 attribute to Appendix A is pinned by a self-test check** — the instants, the draw's index, the floors' arithmetic and the memory gate's reads, the bets against `mpmath`, the three readings, the policy, the kept replies' replay, cut and resume, `agreement`'s twelve figures, a figure apart and other kept replies refused, the sort index's order and the sort on disk with its runs removed, the trades' band, hold, block and side, the fees, Polymarket's instant and version at their edges, both venues' frames with every reason and a market listed twice in one listing and once in two, their caps on pages and series-days, the draw sequence against `hashlib`, the draws' summary against the file, the money against hand sums, both venues rebuilt from their kept replies, and gzip a piece at a time equal to `gz`'s bytes; **Appendix B's are pinned by its agreement with Appendix A** on three sets of real replies (§4.1). **The venues' behaviours** — listing filters, cursors, fields, `version`, a series' slug, the cutoff, rate limits, fee terms, the fills' order — **are read from their documentation and their replies by the Architect on 2026-11-22 and 2026-11-27 and by TZ-56's run**. |
| **C8** | every cross-reference | **This file:** §0.0 to §0.5, §1, §2 items 1 to 11, §3.1 to §3.13, §4.1 to §4.8, §5, §6, §7's V1 to V15, §8, §9 and §10 — each reference resolved to the heading or item it names. **CANON `2026-11-22-a`:** PART II's K track — its question, its decisions, "UNDECIDABLE closes nothing and admits nothing" — and its gate rules; §1.1's Protocol V2 dates; §1.8's explorations and read sets; hard rules 2, 4, 15 and 16 — a correction a new TZ naming the old one; PART VI — each read in the file and supporting its sentence. **The map, revision `2026-11-28-a`:** §0, §1, §2.6, §3, §5, the fourteen §6 rows the header names and the thirty-three §7 items it lists, each read in full; every one the body cites supports its sentence, and every item the body cites is in the header's list. **TZ-56's report:** its status, §1, §2.1's log, §2.3's probe, host gate and self-test, §2.4's closing reads and §3's departures 1 and 3, each supporting the sentence that cites it. **The contract:** §1 steps 1 to 4 and §8. **The Boss's words:** none is quoted. |

---

## Appendix A — `research/tz56-k0-favourite.py`, byte for byte

Extracted by §0.1's script; the block's content is the file.


```python file=research/tz56-k0-favourite.py
#!/usr/bin/env python3
"""TZ-56a - K0, the K track's first step, again after TZ-56's BLOCK at G-REHEARSAL: on Kalshi's binary markets
closing 2026-11-16 to 2026-11-21, and on Polymarket's CTF markets ending on the same days and closed by 12:00 UTC on
2026-11-23, its control, does acquiring the favourite - the side a taker acquired at a traded price in [0.80, 0.95)
within the day before the market closed - and holding it to settlement earn after a taker's fee? Each venue's set is a two-stage random draw, a series and day and then a market of it, fixed in this file
before any of its data is read; each venue's reading two exact betting tests of the draws' mean; and the reading's
inputs, every venue reply it rests on, published as a Release.

    fingerprint   contract section 1 steps 3 and 4, asserted: the map's revision, anchors and rows
    number        CANON hard rule 2: no other TZ-56a specification or report on origin/main
    selftest      every rule of this file on literals, synthetic frames and temporary trees; no request
    still         the host's units: the first run records them, the second compares (G-STILL)
    scratch OWN   the UUID directories beside OWN, this session's, each named live or earlier
    probe         one live request per endpoint, through this file's own request function (G-PROBE)
    rehearse      2026-11-12, read already: both venues' frames and 60 members each, every reply kept, its
                  figures written for agree
    agree         G-REHEARSAL: those figures against the Architect's reference on the same kept replies
    frame         both venues' frames over the six days, every reply kept (G-FRAME)
    draw          both venues' draws to 5,000 members each, every reply kept (G-SET)
    redraw        the frames and the draws again from the kept replies alone, byte for byte (DETERMINISM)
    score         K0's reading on each venue; a second run writes the same bytes (DETERMINISM)
    pack          the Release's set: its assets, their bytes and SHA-256, its notes
    verify        G-TAG, G-UPLOAD and G-DOWNLOAD, with no credential
    reclaim TREE  TZ-56a section 9

Its requests: api.elections.kalshi.com, gamma-api.polymarket.com and data-api.polymarket.com, read anonymously,
in probe, rehearse, frame and draw alone; api.github.com, github.com and its download hosts in verify alone; git
against origin. An audit hook refuses every open, listing, request and process TZ-56a section 2 does not give the
running mode. It writes under /root/tz56a-work/ and, in reclaim, new files in /root/btc-forensics/ by exclusive create.
Exit 0: every assert of the mode held. Exit 1: an assert failed, and its message names it. Run it with
/root/tz04a-env/venv/bin/python.

Written for CryptoTZ/TZ-56a-k0-favourite.md. The TZ is the specification.
"""

import calendar
import collections
import array
import ctypes
import decimal
import gzip
import hashlib
import heapq
import http.client
import itertools
import json
import os
import re
import resource
import shutil
import socket
import struct
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import zlib
from decimal import Decimal as D
from fractions import Fraction as Fr

if not __debug__:
    sys.stderr.write("tz56: refuses to run with asserts disabled (-O); every check is an assert\n")
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
PYFILE = "tz56-k0-favourite.py"

# ---- the TZ's constants: none of them is measured by this run ------------------------------------------------

MAP_REVISION = "2026-11-28-a"
ANCHORS = {"A1": "229a944f2d51", "A2": "6c5089330629",
           "A3": "0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable",
           "A4": "6ac6e10aeabc", "A5": "0f6c90451cbd", "A6": "729f0bcdbee3"}
ANCHOR_FILES = {"A2": "research/twap-divergence.py", "A4": "BTC-EXECUTOR-INSTRUCTIONS.md",
                "A5": "research/recorder/recorder.py", "A6": "research/pfair.py"}
MAP_ROWS = {"frozen": 71, "tracked": 2, "reported": 1}
ROW = re.compile(r"^\| `([^`]+)` \| ([0-9,]+|—) \| ([0-9,]+|—) \| (frozen|tracked|reported) \| "
                 r"(?:`([0-9a-f]{64})`|[^|]*) \|$", re.M)
ANCHOR_ROW = re.compile(r"^\| `(A[0-9])` — [^|]*\| `([^`]+)` \|$", re.M)
NUMBER = "TZ-56a-"
OWN_TZ = "CryptoTZ/TZ-56a-k0-favourite.md"

DAY = 86400
US = 10 ** 6
W0 = 1794787200              # 2026-11-16 00:00:00 UTC, the set's first day
DAYS = tuple(W0 + i * DAY for i in range(6))     # 2026-11-16 ... 2026-11-21; 2026-11-22 00:00:00 UTC ends it
R0 = 1794441600              # 2026-11-12 00:00:00 UTC: the rehearsal's day, read already (CANON section 1.8)
NOT_BEFORE = 1795435200      # 2026-11-23 12:00:00 UTC: frame and every mode after it wait for this instant
CLOSED_BY = NOT_BEFORE       # a Polymarket market of the set closed after this instant is late, not a row
REH_CLOSED_BY = 1795737600   # 2026-11-27 00:00:00 UTC: the same for the rehearsal's day
MARGIN = 3600                # a day's listing reaches an hour past both of its ends; the frame keeps the day's own
HOLD_S = 86400               # a member's trades: executed in [close - 86,400 s, close)
SLOW_S = 300                 # the barred diagnostic: the same trades executed at least 300 s before the close
LO, HI = Fr(4, 5), Fr(19, 20)    # the favourite's band: a traded price p with 0.80 <= p < 0.95
SALT, REH_SALT = "TZ-56-K0", "TZ-56-K0-REHEARSAL"
NEED = 5000                  # members a venue
DRAWS_MAX = {"kalshi": 20000, "polymarket": 40000}   # draws a venue considers at most before G-SET is BLOCKED
REH_NEED = 60
REH_DRAWS_MAX = {"kalshi": 400, "polymarket": 400}
VENUES = ("kalshi", "polymarket")

# The test (TZ-56a section 1): y a member's mean after-fee money a contract, in (-1, 1/5]; x = (y + 1) / (6/5) in
# (0, 1]; EARN rejects a mean of y at most 0, NO EARN a mean at least DELTA, each by Ville's inequality on its own
# betting capital at alpha = 1/400 a venue and answer - 1/200 an answer family-wise over the two venues.
ALPHA_INV = 400
DELTA = Fr(1, 100)
MU_E, MU_N = Fr(2, 100), Fr(-1, 100)            # the named alternatives each bet aims at
Y_LO, Y_HI = Fr(-1), Fr(1, 5)
WIDTH = Y_HI - Y_LO
M0, M1 = (0 - Y_LO) / WIDTH, (DELTA - Y_LO) / WIDTH            # 5/6 and 101/120
D_E, D_N = (MU_E - 0) / WIDTH, (DELTA - MU_N) / WIDTH         # 1/60 each
CAP_E, CAP_N = Fr(1, 2) / M0, Fr(1, 2) / (1 - M1)             # 3/5 and 60/19: every factor at least 1/2
C60 = decimal.Context(prec=60, rounding=decimal.ROUND_HALF_EVEN)
KAPPA_MAX = Fr(7, 50)        # a fee coefficient above 0.14 is a failed assert: y > -1 needs it below 0.3125
KALSHI_FEE = Fr(7, 100)      # Kalshi's taker fee: multiplier x 0.07 x C x P x (1 - P) (its fee schedule)
KALSHI_FEE_TYPES = ("quadratic", "quadratic_with_maker_fees", "quadratic_with_combo_maker_fees")
MULT_MAX = Fr(2)
PROJECT_AFTER, FETCH_MAX_S = 300, 10800         # draw's fail-fast: a venue's projection after 300 draws
FRAME_PAGES_MAX = {"kalshi": 400, "polymarket": 3000}    # pages a venue's day may take before frame is BLOCKED
GROUPS_MAX = 100000          # series-days a venue's frame may hold before it is BLOCKED
SORT_CHUNK = 50000           # lines a sorted run of the frame's index holds: the sort's memory

UA = "btc-5m-twap-tz56"
HEADERS = {"User-Agent": UA, "Accept": "application/json", "Accept-Encoding": "gzip"}
KALSHI = "https://api.elections.kalshi.com/trade-api/v2"
GAMMA = "https://gamma-api.polymarket.com"
DATA = "https://data-api.polymarket.com"
VENUE_HOSTS = ("api.elections.kalshi.com", "gamma-api.polymarket.com", "data-api.polymarket.com")
GAP_S = {"api.elections.kalshi.com": 0.25, "gamma-api.polymarket.com": 0.1, "data-api.polymarket.com": 0.1}
RETRY_STATUS = (429, 500, 502, 503, 504)
TRIES = 20
TIMEOUT_S = 60
GH_HOSTS = ("api.github.com", "github.com", "release-assets.githubusercontent.com", "objects.githubusercontent.com")
REPO = "seahomebatumi-ai/btc-5m-twap"
TAG = "tz-56a-k0-inputs"

WORK = "/root/tz56a-work"
WT = WORK + "/wt"
STATE = WORK + "/state.json"
LEDGER = WORK + "/read-ledger.jsonl"
RUN = WORK + "/run"
REHEARSAL = WORK + "/rehearsal"
REDRAW = WORK + "/redraw"
RELEASE_DIR = WORK + "/release"
INSTRUMENT_FIGURES = REHEARSAL + "/instrument.json"     # rehearse's figures; agree compares them
REFERENCE_FIGURES = REHEARSAL + "/reference.json"       # the reference's, Appendix B's, on the same kept replies
REH_FIGURES = ("rows", "keys", "reasons", "draws", "digest", "gross")
REH_FILES = tuple("%s-%s.jsonl.gz%s" % (kind, v, ext) for v in ("kalshi", "polymarket")
                  for kind in ("raw-frame", "raw-draw") for ext in ("", ".idx"))
RELEASE_SET = WORK + "/release-set.json"
VERIFY_FILE = WORK + "/verify.json"
PRIMARY = "/root/btc-5m-twap"
REPORTS = PRIMARY + "/CryptoReports"
FORENSICS = "/root/btc-forensics"
BRANCH = "tz-56a-k0-favourite"
CAPTURE_ROOTS = ("/var/lib/btc-recorder", "/var/lib/btc-chainbook", "/var/lib/btc-pairbook",
                 "/var/lib/btc-rewardbook", "/var/lib/btc-pairbook-archive", "/var/lib/btc-rewardbook-archive",
                 "/var/lib/adv3-bot", "/etc/adv3-bot", "/var/lib/liq-guard", "/etc/liq-guard")
UNITS = ("btc-recorder.service", "btc-rewardbook.service", "btc-rewardbook-archive.timer", "adv3-bot.service",
         "liq-guard.service")
SHOW_ENV = {"LC_ALL": "C", "TZ": "UTC"}
UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
TOKEN = re.compile(r"[0-9a-f]{16,64}")
HEXISH = re.compile(r"0x[0-9a-fA-F]{8,}|[0-9a-fA-F]{32,}")
SHA40 = re.compile(r"[0-9a-f]{40}")
LIVE_S = 60
PEAK_BOUND = 65679360        # bytes: the largest peak of a mode or of the reference in the Architect's runs (TZ-56a 0.4)
MEM_FLOOR = 157499106        # MemAvailable: twice that peak at the host's ratio TZ-37 measured, 1.199, rounded up
MEM_RETRY_S, MEM_READS = 60, 5
DISK_FLOOR = 7400000000      # free bytes on /dev/vda2 while writing: the reward book's STREAM_FLOOR and one slot more
DISK_GATE = 8700000000       # free bytes at a mode's start: DISK_FLOOR and this run's bound, 1,300,000,000

# ---- the audit hook: TZ-56a section 2's reads, writes, requests and processes ---------------------------------

MODE = [None]
REFUSED = []
WRITE_FLAGS = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC
PROCESSES = {"git", "systemctl", "stat"}
NET_MODES = ("probe", "rehearse", "frame", "draw")


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


def policy(mode, event, args, work=None):
    """None where TZ-56a section 2 allows the event in this mode; otherwise the reason it is refused. Pure."""
    work = work or WORK
    if event == "urllib.Request":
        host = urllib.parse.urlsplit(args[0]).hostname if args and isinstance(args[0], str) else None
        if mode in NET_MODES and host in VENUE_HOSTS:
            return None
        if mode == "verify" and host in GH_HOSTS:
            return None
        return "a request to %s" % host
    if event == "subprocess.Popen":
        exe = args[0] if args and args[0] else (args[1][0] if len(args) > 1 and args[1] else "")
        exe = os.path.basename(os.fsdecode(exe) if isinstance(exe, bytes) else str(exe))
        return None if exe in PROCESSES else "a process %s" % exe
    p = _path(args[0]) if args else None
    if p is None:
        return None
    if any(_under(p, r) for r in CAPTURE_ROOTS):
        return "an open or listing under a capture's or a unit's own tree"
    if event in ("os.listdir", "os.scandir"):
        return None
    wm, fl = (args[1] if len(args) > 1 else None), (args[2] if len(args) > 2 else None)
    if _under(p, FORENSICS):
        if _writing(wm, fl):
            return None if mode == "reclaim" and _exclusive(wm, fl) else "a write into the forensic store"
        return None
    if _writing(wm, fl) and not _under(p, work):
        return "a write outside the work tree"
    return None


def _audit(event, args):
    if event not in ("open", "os.listdir", "os.scandir", "urllib.Request", "subprocess.Popen"):
        return
    why = policy(MODE[0], event, args)
    if why is not None:
        REFUSED.append((event, str(args[0]) if args else ""))
        raise GuardError("%s refused in mode %s, %s: %r" % (event, MODE[0], why, args[0] if args else None))


sys.addaudithook(_audit)

# ---- small helpers -------------------------------------------------------------------------------------------


def out(msg):
    sys.stdout.write("[%s] %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    sys.stdout.flush()


def utc(t):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(float(t)))


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
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, path)


def write_once(path, data):
    """The first run writes; a later run must produce the same bytes (contract section 6)."""
    if os.path.exists(path):
        got = sha256_file(path)
        assert got == sha256_bytes(data), "DETERMINISM: %s differs from the first run" % path
        out("unchanged %s %d bytes sha256 %s" % (path, len(data), got))
        return got
    write_atomic(path, data)
    out("wrote %s %d bytes sha256 %s" % (path, len(data), sha256_bytes(data)))
    return sha256_bytes(data)


def finish_once(tmp, path):
    """write_once for a file written a piece at a time to `tmp`, closed and synced: the first run renames it to
    `path`; a later run must have produced the same bytes, and its `tmp` is removed."""
    sha, size = sha256_file(tmp), os.path.getsize(tmp)
    if os.path.exists(path):
        os.remove(tmp)
        assert sha256_file(path) == sha, "DETERMINISM: %s differs from the first run" % path
        out("unchanged %s %d bytes sha256 %s" % (path, size, sha))
    else:
        os.replace(tmp, path)
        out("wrote %s %d bytes sha256 %s" % (path, size, sha))
    return sha


def fr_text(x):
    x = Fr(x)
    return "%d/%d" % (x.numerator, x.denominator)


def fr_of(s):
    a, b = s.split("/")
    return Fr(int(a), int(b))


def dec(x, places=12):
    """A figure for print, half-even to `places`; every comparison is made on the exact figure."""
    x = Fr(x)
    q = C60.divide(D(x.numerator), D(x.denominator))
    return format(q.quantize(D(1).scaleb(-places), rounding=decimal.ROUND_HALF_EVEN, context=C60), "f")


def jline(obj):
    return (json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True) + "\n").encode("ascii")


def gz(data):
    """A gzip member of fixed bytes: no name, mtime 0, level 6."""
    return gzip.compress(data, compresslevel=6, mtime=0)


def gz_file_once(src, dest):
    """`src` as one gzip member - zlib's own wrapper at level 6, the bytes gz() gives, since gzip.compress uses it at
    mtime 0 - read and written 1 MiB at a time, the disk's floor read every 256 MiB; the first run writes `dest`, a
    later run must produce the same bytes."""
    tmp = dest + ".tmp"
    z = zlib.compressobj(6, zlib.DEFLATED, 31)
    with open(src, "rb") as fi, open(tmp, "wb") as fo:
        for n, chunk in enumerate(iter(lambda: fi.read(1 << 20), b""), 1):
            fo.write(z.compress(chunk))
            if n % 256 == 0:
                disk_check()
        fo.write(z.flush())
        fo.flush()
        os.fsync(fo.fileno())
    return finish_once(tmp, dest)


def jloads(body):
    """A venue's reply: UTF-8 JSON, every number with a fraction read as Decimal, exact."""
    return json.loads(body.decode("utf-8"), parse_float=D)


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh, parse_float=D)


def load_state():
    return load_json(STATE) if os.path.exists(STATE) else {}


def save_state(st):
    write_atomic(STATE, json.dumps(st, sort_keys=True, indent=1, default=str).encode("utf-8") + b"\n")


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
    """MemAvailable at a mode's reads in order: the first, and one every MEM_RETRY_S after a read below MEM_FLOOR,
    MEM_READS at most (map section 7 item 137). The last decides: (passes, it). Pure."""
    assert 1 <= len(reads) <= MEM_READS and all(r < MEM_FLOOR for r in reads[:-1]), reads
    return reads[-1] >= MEM_FLOOR, reads[-1]


def floor_check(read=None, sleep=None, freef=None):
    read, sleep, freef = read or mem_available, sleep or time.sleep, freef or free_bytes
    assert MALLOC_TUNED, "BLOCKED: glibc did not take the mmap threshold and the arena count"
    reads, free = [read()], freef()
    out("MemAvailable %d bytes, floor %d; free %d bytes, gate %d" % (reads[0], MEM_FLOOR, free, DISK_GATE))
    while reads[-1] < MEM_FLOOR and len(reads) < MEM_READS:
        sleep(MEM_RETRY_S)
        reads.append(read())
        out("MemAvailable read %d of %d at most: %d bytes" % (len(reads), MEM_READS, reads[-1]))
    passes, final = memory_gate(reads)
    assert passes, "BLOCKED: MemAvailable %d bytes at read %d, every read below %d" % (final, len(reads), MEM_FLOOR)
    assert free >= DISK_GATE, "BLOCKED: %d bytes free, below %d" % (free, DISK_GATE)


def disk_check():
    free = free_bytes()
    assert free >= DISK_FLOOR, "BLOCKED: %d bytes free while writing, below %d" % (free, DISK_FLOOR)


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


def said(body):
    """A venue's refusal in its own words, its hexadecimal strings and UUIDs masked (map section 7 item 191)."""
    txt = body.decode("utf-8", "replace") if isinstance(body, bytes) else str(body)
    return UUID.sub("<uuid>", HEXISH.sub("<hex>", txt))[:400]


# ---- time and the draw ------------------------------------------------------------------------------------------


def us_of(s):
    """A venue's instant - ISO 8601 with T and Z, or gamma's `2026-11-12 00:01:21.5+00` - as integer microseconds UTC.
    Pure."""
    assert isinstance(s, str) and s, "an instant: %r" % (s,)
    t = s.strip().replace("T", " ")
    if t.endswith("Z"):
        t = t[:-1]
    for suf in ("+00:00:00", "+00:00", "+00"):
        if t.endswith(suf):
            t = t[:-len(suf)]
            break
    frac = "0"
    if "." in t:
        t, frac = t.split(".")
    assert re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}", t) and frac.isdigit() \
        and len(frac) <= 9, "an instant: %r" % (s,)
    secs = calendar.timegm(time.strptime(t, "%Y-%m-%d %H:%M:%S"))
    return secs * US + int((frac + "000000")[:6])


def iso(t):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(int(t)))


def uidx(salt, venue, k, stage, n):
    """Draw k's index at stage 1 or 2 among n: the SHA-256 of `salt|venue|k|stage`, big-endian, modulo n. Pure."""
    assert n >= 1 and stage in (1, 2) and k >= 0
    h = hashlib.sha256(("%s|%s|%d|%d" % (salt, venue, k, stage)).encode("ascii")).digest()
    return int.from_bytes(h, "big") % n


def day_of(us, days):
    """The day of `days` whose [d, d + 86,400 s) holds the instant, or None. Pure."""
    for d in days:
        if d * US <= us < (d + DAY) * US:
            return d
    return None


# ---- the network: three venue hosts, every header fixed; every reply kept and replayable ---------------------


class Net:
    """One request at a time, at least GAP_S apart a host; a reply refused with RETRY_STATUS or a dropped connection
    is asked again, TRIES at most; any other refusal is BLOCKED, printed in the venue's own words."""

    def __init__(self, sleep=None, opener=None):
        self.last, self.count, self.retries = {}, collections.Counter(), collections.Counter()
        self.sleep = sleep or time.sleep
        self.opener = opener or urllib.request.urlopen

    def get(self, url):
        host = urllib.parse.urlsplit(url).hostname
        assert host in VENUE_HOSTS, "a request to %s" % host
        for attempt in range(1, TRIES + 1):
            gap = GAP_S[host] - (time.monotonic() - self.last.get(host, -1e9))
            if gap > 0:
                self.sleep(gap)
            self.last[host] = time.monotonic()
            try:
                with self.opener(urllib.request.Request(url, headers=HEADERS), timeout=TIMEOUT_S) as r:
                    status, raw, enc = r.status, r.read(), r.headers.get("Content-Encoding")
            except urllib.error.HTTPError as e:
                raw, enc = e.read(), e.headers.get("Content-Encoding") if e.headers else None
                body = gzip.decompress(raw) if enc == "gzip" else raw
                if e.code in RETRY_STATUS:
                    hint = (e.headers.get("Retry-After") or e.headers.get("x-ratelimit-reset")) if e.headers else None
                    wait = retry_wait(attempt, hint)
                    self.retries[host] += 1
                    out("%s answered %d, attempt %d of %d; waiting %.1f s: %s" % (host, e.code, attempt, TRIES, wait,
                                                                               said(body)[:160]))
                    self.sleep(wait)
                    continue
                raise AssertionError("BLOCKED: %s answered %d: %s" % (redact(url), e.code, said(body)))
            except (urllib.error.URLError, TimeoutError, ConnectionError, socket.timeout, http.client.HTTPException) \
                    as e:
                wait = retry_wait(attempt, None)
                self.retries[host] += 1
                out("%s: %s, attempt %d of %d; waiting %.1f s" % (host, type(e).__name__, attempt, TRIES, wait))
                self.sleep(wait)
                continue
            assert enc in (None, "gzip", "identity"), "%s: Content-Encoding %r" % (host, enc)
            body = gzip.decompress(raw) if enc == "gzip" else raw
            assert status == 200, "BLOCKED: %s answered %d: %s" % (redact(url), status, said(body))
            self.count[host] += 1
            return body
        raise AssertionError("BLOCKED: %s: no reply in %d tries" % (redact(url), TRIES))


def retry_wait(attempt, hint):
    """Seconds before the next try: the venue's own hint where it gives one, within [1, 120]; otherwise 2 ** attempt
    within [2, 120]. Pure."""
    try:
        h = float(hint) if hint is not None else None
    except ValueError:
        h = None
    if h is not None and h > 0:
        return min(120.0, max(1.0, h))
    return float(min(120, max(2, 2 ** attempt)))


def redact(url):
    return url if len(url) < 200 else url[:200] + "..."


class Sink:
    """The kept replies of one phase: one gzip member a reply, appended in request order, and beside it an index of
    the file's length after each complete member, written and synced after the member. A member past the index's
    last length is a reply cut short by an exit, and is cut off before the phase resumes."""

    def __init__(self, path):
        self.path, self.index = path, path + ".idx"

    def lengths(self):
        if not os.path.exists(self.index):
            return []
        with open(self.index, encoding="ascii") as fh:
            return [int(x) for x in fh.read().split()]

    def records(self, ends=None):
        """The kept replies in order, each asserted whole by its own SHA-256."""
        ends = self.lengths() if ends is None else ends
        if not ends:
            return
        with open(self.path, "rb") as fh:
            start = 0
            for i, end in enumerate(ends):
                fh.seek(start)
                rec = json.loads(gzip.decompress(fh.read(end - start)).decode("ascii"))
                body = rec["body"].encode("utf-8")
                assert rec["i"] == i and len(body) == rec["bytes"] and sha256_bytes(body) == rec["sha256"], \
                    "%s: reply %d is not whole" % (self.path, i)
                yield rec["url"], body
                start = end

    def trim(self):
        ends = self.lengths()
        end = ends[-1] if ends else 0
        if os.path.exists(self.path):
            size = os.path.getsize(self.path)
            assert size >= end, "%s: %d bytes, its index %d" % (self.path, size, end)
            if size > end:
                with open(self.path, "r+b") as fh:
                    fh.truncate(end)
                out("%s: a reply cut short at %d bytes cut off" % (self.path, size))
        return len(ends)

    def append(self, i, url, body):
        rec = {"i": i, "url": url, "bytes": len(body), "sha256": sha256_bytes(body), "at": time.time_ns(),
               "body": body.decode("utf-8")}
        assert rec["body"].encode("utf-8") == body, "a reply that is not UTF-8"
        member = gz(jline(rec))
        with open(self.path, "ab") as fh:
            fh.write(member)
            fh.flush()
            os.fsync(fh.fileno())
            end = fh.tell()
        with open(self.index, "a", encoding="ascii") as fh:
            fh.write("%d\n" % end)
            fh.flush()
            os.fsync(fh.fileno())


class Source:
    """A phase's replies: those its sink kept, replayed in order and each asserted to answer the very request the
    phase makes; then, where live, the network, every new reply kept. The disk's floor is read every 200 replies."""

    def __init__(self, sink, net=None):
        self.sink, self.net = sink, net
        self.kept = sink.trim() if net is not None else len(sink.lengths())
        self.replay = sink.records(sink.lengths()[:self.kept])
        self.i, self.live = 0, 0

    def get(self, url):
        if self.i < self.kept:
            got_url, body = next(self.replay)
            assert got_url == url, "REPLAY: request %d is %s, the kept reply's %s" % (self.i, redact(url),
                                                                                   redact(got_url))
        else:
            assert self.net is not None, "REPLAY: request %d %s has no kept reply" % (self.i, redact(url))
            body = self.net.get(url)
            self.sink.append(self.i, url, body)
            self.live += 1
        self.i += 1
        if self.i % 200 == 0:
            disk_check()
        return body

    def json(self, url):
        return jloads(self.get(url))


# ---- the frames: every market of a venue's days, each kept as a row or counted by reason ----------------------

KALSHI_REASONS = ("outside", "type", "status", "result", "volume")
POLY_REASONS = ("late", "version", "outside", "shape", "result", "close", "event")


def kalshi_class(m, days):
    """A listed Kalshi market: (row, None) where it closes in one of `days`, is binary and finalized, resolved yes or
    no, and traded; otherwise (None, the first reason it fails, in KALSHI_REASONS' order). Pure."""
    close = us_of(m["close_time"])
    d = day_of(close, days)
    if d is None:
        return None, "outside"
    if m.get("market_type") != "binary":
        return None, "type"
    if m.get("status") != "finalized":
        return None, "status"
    if m.get("result") not in ("yes", "no"):
        return None, "result"
    if not D(str(m.get("volume_fp"))) > 0:
        return None, "volume"
    ev = m["event_ticker"]
    assert isinstance(ev, str) and ev, "an event ticker %r" % (ev,)
    return {"day": d, "key": ev.split("-")[0], "id": m["ticker"], "event": ev, "close_us": close,
            "label": m["result"]}, None


def poly_kappa(m):
    """A Polymarket market's taker fee coefficient from its own document: 0 where its fees are off; the rate of its
    schedule where that is the venue's - exponent 1, taker only, a rate in [0, 0.14]; None otherwise. Pure."""
    if m.get("feesEnabled") is False:
        return Fr(0)
    fs = m.get("feeSchedule")
    if m.get("feesEnabled") is True and isinstance(fs, dict) and fs.get("exponent") == 1 \
            and fs.get("takerOnly") is True:
        r = fs.get("rate")
        if isinstance(r, (int, D)) and not isinstance(r, bool) and 0 <= Fr(r) <= KAPPA_MAX:
            return Fr(r)
    return None


def jfield(v):
    """A gamma field that holds a JSON list as text: the list; a list as is; anything else an empty list. Pure."""
    if isinstance(v, list):
        return v
    if isinstance(v, str) and v:
        got = json.loads(v)
        return got if isinstance(got, list) else []
    return []


def poly_class(m, days, closed_by):
    """A listed Polymarket market: (row, None) where it closed at or before `closed_by`, its document is of the CTF
    protocol - `version` "v1"; before 2026-11-23 a "v2" document is the venue's Protocol V2 pilot - its end date
    falls in one of `days`, it has two outcomes and two tokens, it resolved wholly to one of them, it carries its
    close and an event; otherwise (None, the first reason it fails, in POLY_REASONS' order). Its key is its event's
    series, or its event where the event has none. Pure."""
    ct = m.get("closedTime")
    if isinstance(ct, str) and ct and us_of(ct) > closed_by * US:
        return None, "late"
    if m.get("version") != "v1":
        return None, "version"
    end = m.get("endDate")
    d = day_of(us_of(end), days) if isinstance(end, str) and end else None
    if d is None:
        return None, "outside"
    o, tk = jfield(m.get("outcomes")), jfield(m.get("clobTokenIds"))
    if len(o) != 2 or len(tk) != 2:
        return None, "shape"
    op = jfield(m.get("outcomePrices"))
    if op not in (["1", "0"], ["0", "1"]):
        return None, "result"
    if not m.get("closedTime"):
        return None, "close"
    ev = m.get("events") or []
    if not ev or not isinstance(ev[0], dict):
        return None, "event"
    ser = ev[0].get("series") or []
    if ser and isinstance(ser[0], dict) and ser[0].get("slug"):
        key = "series:" + ser[0]["slug"]
    else:
        key = "event:" + str(ev[0].get("slug") or ev[0].get("id"))
    kap = poly_kappa(m)
    return {"day": d, "key": key, "id": m["conditionId"], "close_us": us_of(m["closedTime"]),
            "label": "A" if op[0] == "1" else "B", "tokens": [str(tk[0]), str(tk[1])],
            "kappa": None if kap is None else fr_text(kap), "fee": m.get("feeType")}, None


def listing_url(venue, d, cursor):
    if venue == "kalshi":
        q = [("limit", 1000), ("min_close_ts", d - MARGIN), ("max_close_ts", d + DAY + MARGIN),
             ("mve_filter", "exclude")]
        if cursor:
            q.append(("cursor", cursor))
        return KALSHI + "/markets?" + urllib.parse.urlencode(q)
    q = [("limit", 100), ("closed", "true"), ("end_date_min", iso(d - MARGIN)), ("end_date_max", iso(d + DAY + MARGIN))]
    if cursor:
        q.append(("after_cursor", cursor))
    return GAMMA + "/markets/keyset?" + urllib.parse.urlencode(q)


def listing_page(venue, doc):
    """(the page's markets, the next cursor or None). Pure."""
    if venue == "kalshi":
        assert isinstance(doc.get("markets"), list), "a Kalshi listing without markets"
        return doc["markets"], doc.get("cursor") or None
    assert isinstance(doc.get("markets"), list), "a gamma keyset page without markets"
    return doc["markets"], doc.get("next_cursor") or None


def market_instant(venue, m):
    """The instant a venue's listing filters on: Kalshi's close, Polymarket's end date. Pure."""
    s = m.get("close_time") if venue == "kalshi" else m.get("endDate")
    return us_of(s) if isinstance(s, str) and s else None


def tsv(*fields):
    """One line of an index on disk: its fields tab-separated, in UTF-8, ending in a newline. No field holds a
    character below a space, so these lines sorted as bytes are their field tuples sorted as text, field by field. Pure."""
    for f in fields:
        assert isinstance(f, str) and (not f or min(f) >= " "), "a field with a control character: %r" % (f,)
    return ("\t".join(fields) + "\n").encode("utf-8")


def sorted_lines(path, chunk=None):
    """The lines of `path` sorted as bytes: runs of `chunk` lines sorted in memory and written beside it, then merged
    in one pass, one line a run in memory; every run is removed once merged. A generator."""
    chunk = chunk or SORT_CHUNK
    runs = []
    try:
        with open(path, "rb") as fh:
            while True:
                lines = list(itertools.islice(fh, chunk))
                if not lines:
                    break
                assert lines[-1].endswith(b"\n"), "%s ends without a newline" % path
                lines.sort()
                runs.append("%s.run-%d" % (path, len(runs)))
                with open(runs[-1], "wb") as fo:
                    fo.writelines(lines)
                lines = None
                disk_check()
        files = [open(r, "rb") for r in runs]
        try:
            yield from heapq.merge(*files)
        finally:
            for f in files:
                f.close()
    finally:
        for r in runs:
            if os.path.exists(r):
                os.remove(r)


def build_frame(venue, days, src, path, closed_by):
    """Every market each day's listing returns, classified: the kept rows written to `path`, one JSON line each,
    sorted by day, key and id; every other market counted by reason. A market listed more than once - by two days'
    listings, within MARGIN of the boundary between them, or twice by one - is classified at its first listing alone;
    a listing that returns a market outside the range it asked for is BLOCKED. Memory holds one page and one sorted
    run: every listed market is a line of an index on disk - its id, its place in the listings and its reason, or its
    row's day, key and offset in a file of rows - sorted by id to keep each market's first listing, and the kept rows'
    lines sorted by day, key and id to order the frame. A Polymarket market closed after `closed_by` is late.
    Returns (rows, keys, reasons, pages)."""
    rows_path, ids_path, kept_path = path + ".rows", path + ".ids", path + ".kept"
    reasons, pages, seq, off = collections.Counter(), 0, 0, 0
    with open(rows_path, "wb") as fr, open(ids_path, "wb") as fi:
        for d in days:
            cursor, n_pages, n_listed = None, 0, 0
            while True:
                items, cursor = listing_page(venue, src.json(listing_url(venue, d, cursor)))
                n_pages += 1
                pages += 1
                assert n_pages <= FRAME_PAGES_MAX[venue], "BLOCKED: %s's listing of %s past %d pages" % (
                    venue, iso(d), FRAME_PAGES_MAX[venue])
                for m in items:
                    mid = m["ticker"] if venue == "kalshi" else m["conditionId"]
                    assert isinstance(mid, str) and mid, "a market id %r" % (mid,)
                    t = market_instant(venue, m)
                    assert t is None or (d - MARGIN - 1) * US <= t <= (d + DAY + MARGIN + 1) * US, \
                        "BLOCKED: %s's listing of %s returned %s at %s, outside the range it asked for" % (
                            venue, iso(d), mid, t)
                    row, why = kalshi_class(m, days) if venue == "kalshi" else poly_class(m, days, closed_by)
                    if row is None:
                        fi.write(tsv(mid, "%012d" % seq, "-" + why))
                    else:
                        line = jline(row)
                        fi.write(tsv(mid, "%012d" % seq, "+", "%010d" % row["day"], row["key"], "%d" % off))
                        fr.write(line)
                        off += len(line)
                    seq += 1
                    n_listed += 1
                if not cursor:
                    break
            out("%s %s: %d pages, %d markets listed" % (venue, iso(d), n_pages, n_listed))
    with open(kept_path, "wb") as fk:
        prev = None
        for ln in sorted_lines(ids_path):
            f = ln[:-1].split(b"\t")
            if f[0] == prev:
                continue
            prev = f[0]
            if f[2] == b"+":
                fk.write(b"\t".join((f[3], f[4], f[0], f[5])) + b"\n")
            else:
                reasons[f[2][1:].decode("ascii")] += 1
    os.remove(ids_path)
    rows, keys, last = 0, 0, None
    with open(path + ".tmp", "wb") as fo, open(rows_path, "rb") as fr:
        for ln in sorted_lines(kept_path):
            day, key, mid, o = ln[:-1].split(b"\t")
            assert last is None or (day, key, mid) > last, "a row twice"
            keys += last is None or (day, key) != last[:2]
            last = (day, key, mid)
            fr.seek(int(o))
            fo.write(fr.readline())
            rows += 1
            if rows % 100000 == 0:
                disk_check()
        fo.flush()
        os.fsync(fo.fileno())
    os.remove(kept_path)
    os.remove(rows_path)
    os.replace(path + ".tmp", path)
    return rows, keys, dict(sorted(reasons.items())), pages


class FrameIndex:
    """A frame file's groups in file order - each a (day, key, first row, rows), GROUPS_MAX at most - in memory, one
    key and three integers a group, and each row's byte offset, eight bytes a row, in a file beside it, read back by
    seek; close() removes that file."""

    def __init__(self, path):
        self.path, self.off_path = path, path + ".off"
        self.days, self.keys, self.starts, self.counts = array.array("q"), [], array.array("q"), array.array("q")
        n, off, last = 0, 0, None
        with open(path, "rb") as fh, open(self.off_path, "wb") as fo:
            for line in fh:
                r = json.loads(line)
                fo.write(struct.pack("<q", off))
                off += len(line)
                g = (r["day"], r["key"])
                if g == last:
                    self.counts[-1] += 1
                else:
                    assert last is None or last < g, "%s is not sorted by day and key" % path
                    assert len(self.keys) < GROUPS_MAX, "BLOCKED: %s holds more than %d series-days" % (path, GROUPS_MAX)
                    self.days.append(g[0])
                    self.keys.append(g[1])
                    self.starts.append(n)
                    self.counts.append(1)
                    last = g
                n += 1
        self.rows = n
        self.fh, self.fo = open(path, "rb"), open(self.off_path, "rb")

    def __len__(self):
        return len(self.keys)

    def group(self, i):
        return self.days[i], self.keys[i], self.starts[i], self.counts[i]

    def row(self, i):
        assert 0 <= i < self.rows, "row %d of %d" % (i, self.rows)
        self.fo.seek(8 * i)
        self.fh.seek(struct.unpack("<q", self.fo.read(8))[0])
        return json.loads(self.fh.readline())

    def close(self):
        self.fh.close()
        self.fo.close()
        os.remove(self.off_path)


def frame_labels(path, ids):
    """The labels of the rows whose ids are in `ids`, read from the frame file: score alone calls it."""
    found = {}
    with open(path, "rb") as fh:
        for line in fh:
            r = json.loads(line)
            if r["id"] in ids:
                found[r["id"]] = r["label"]
    assert set(found) == set(ids), "labels missing for %d ids" % (len(set(ids) - set(found)))
    return found


# ---- a member's trades: label-free sums of the favourite acquired at a traded price in [LO, HI) ---------------

AGG_KEYS = ("n", "na", "nb", "sa", "sb", "q")
SUFFIXES = ("", "5")


def agg_new():
    return {k + s: (0 if k in ("n", "na", "nb") else Fr(0)) for s in SUFFIXES for k in AGG_KEYS}


def agg_add(a, side_a, p, slow):
    """One trade that acquired side A (Kalshi's yes, Polymarket's first outcome) or side B at price p: counted in the
    member's sums, and in its slow sums where it was executed at least SLOW_S before the close."""
    for s, on in (("", True), ("5", slow)):
        if on:
            a["n" + s] += 1
            if side_a:
                a["na" + s] += 1
                a["sa" + s] += p
            else:
                a["nb" + s] += 1
                a["sb" + s] += p
            a["q" + s] += p * (1 - p)


def agg_text(a):
    return {k: (v if isinstance(v, int) else fr_text(v)) for k, v in sorted(a.items())}


def agg_of(t):
    return {k: (v if isinstance(v, int) else fr_of(v)) for k, v in t.items()}


def kalshi_trade(t, ticker, close_us):
    """(side is A, price, slow) where a Kalshi trade acquired the favourite inside the hold; else None. Pure."""
    assert t["ticker"] == ticker, "a trade of %s in %s's reply" % (t["ticker"], ticker)
    assert isinstance(t["is_block_trade"], bool), "is_block_trade %r" % (t["is_block_trade"],)
    if t["is_block_trade"]:
        return None
    ts = us_of(t["created_time"])
    if not (close_us - HOLD_S * US <= ts < close_us):
        return None
    side = t["taker_outcome_side"]
    assert side in ("yes", "no"), "taker_outcome_side %r" % (side,)
    yes, no = Fr(t["yes_price_dollars"]), Fr(t["no_price_dollars"])
    assert yes + no == 1, "a trade whose prices do not sum to 1: %s %s" % (yes, no)
    p = yes if side == "yes" else no
    if not (LO <= p < HI):
        return None
    return side == "yes", p, ts < close_us - SLOW_S * US


def poly_trade(x, cid, close_us, tokens):
    """(side is A, price, slow) where a Polymarket taker's fill acquired the favourite inside the hold - a BUY of an
    outcome at p, or a SELL of the other at 1 - p; else None. Pure."""
    assert x["condition_id"] == cid, "a fill of %s in %s's reply" % (x["condition_id"], cid)
    oi = x["outcome_index"]
    assert oi in (0, 1) and str(x["token_id"]) == tokens[oi], "a fill whose token is not its outcome's"
    ts = int(x["timestamp"]) * US
    if not (close_us - HOLD_S * US <= ts < close_us):
        return None
    pr = Fr(x["price"])
    assert 0 < pr < 1, "a fill at %s" % pr
    if x["side"] == "BUY":
        side_a, p = oi == 0, pr
    else:
        assert x["side"] == "SELL", "a fill's side %r" % (x["side"],)
        side_a, p = oi == 1, 1 - pr
    if not (LO <= p < HI):
        return None
    return side_a, p, ts < close_us - SLOW_S * US


class Ctx:
    """What a venue's draws read once: Kalshi's cutoff and fee changes, and its series as each is first met - its fee
    type, fee multiplier and category alone."""

    def __init__(self, venue, days):
        self.venue, self.days = venue, days
        self.series, self.series_changes, self.event_changes, self.cutoff = {}, [], set(), None


def kalshi_open(src, ctx):
    """The first requests of Kalshi's draws: the archive's cutoff, asserted to leave every member's market and trades
    in the live set, then every series fee change and every event fee override the venue lists."""
    cut = src.json(KALSHI + "/historical/cutoff")
    ctx.cutoff = {k: cut.get(k) for k in ("market_settled_ts", "trades_created_ts")}
    first = ctx.days[0]
    assert us_of(cut["market_settled_ts"]) <= first * US and us_of(cut["trades_created_ts"]) <= (first - DAY) * US, \
        "BLOCKED: Kalshi's historical cutoff %r reaches into the days" % (ctx.cutoff,)
    ctx.series_changes = src.json(KALSHI + "/series/fee_changes?" + urllib.parse.urlencode(
        [("show_historical", "true")]))["series_fee_change_arr"]
    cursor = None
    while True:
        q = [("limit", 1000)] + ([("cursor", cursor)] if cursor else [])
        doc = src.json(KALSHI + "/events/fee_changes?" + urllib.parse.urlencode(q))
        ctx.event_changes.update(x["event_ticker"] for x in doc["event_fee_changes"])
        cursor = doc.get("cursor") or None
        if not cursor:
            break


def kalshi_market(row, src, ctx):
    """A drawn Kalshi market: (reason or None, sums, fee coefficient, pages, rows fetched, category). Its series' fee
    first: a fee type that is not quadratic, a series fee change from a day before the days to two after their
    last, or any override of its event's fee excludes it, unread. Then its trades inside the hold."""
    key = row["key"]
    s = ctx.series.get(key)
    if s is None:
        doc = src.json(KALSHI + "/series/" + urllib.parse.quote(key, safe=""))["series"]
        assert doc["ticker"] == key, "BLOCKED: series %r answers as %r" % (key, doc.get("ticker"))
        s = ctx.series[key] = (doc["fee_type"], doc["fee_multiplier"], doc.get("category"))
    ftype, mult, cat = s
    assert isinstance(mult, (int, D)) and not isinstance(mult, bool), "a fee multiplier %r" % (mult,)
    kappa = KALSHI_FEE * Fr(mult)
    lo, hi = (ctx.days[0] - DAY) * US, (ctx.days[-1] + 2 * DAY) * US
    a, pages, fetched = agg_new(), 0, 0
    if ftype not in KALSHI_FEE_TYPES:
        return "fee_type", a, kappa, 0, 0, cat
    if any(x["series_ticker"] == key and lo <= us_of(x["scheduled_ts"]) < hi for x in ctx.series_changes):
        return "fee_changed", a, kappa, 0, 0, cat
    if row["event"] in ctx.event_changes:
        return "fee_event", a, kappa, 0, 0, cat
    assert 0 <= Fr(mult) <= MULT_MAX and kappa <= KAPPA_MAX, "a fee multiplier %s" % mult
    c, ids, cursor = row["close_us"], set(), None
    cs = c // US
    while True:
        q = [("ticker", row["id"]), ("limit", 1000), ("min_ts", cs - HOLD_S - 1), ("max_ts", cs + 1)]
        doc = src.json(KALSHI + "/markets/trades?" + urllib.parse.urlencode(q + ([("cursor", cursor)] if cursor else [])))
        pages += 1
        for t in doc["trades"]:
            assert t["trade_id"] not in ids, "a trade returned twice"
            ids.add(t["trade_id"])
            fetched += 1
            hit = kalshi_trade(t, row["id"], c)
            if hit is not None:
                agg_add(a, *hit)
        cursor = doc.get("cursor") or None
        if not cursor:
            break
    return (None if a["n"] else "no_trade"), a, kappa, pages, fetched, cat


def poly_market(row, src, ctx):
    """A drawn Polymarket market: (reason or None, sums, fee coefficient, pages, rows fetched, fee type). Unread
    where its document's fee is not the venue's schedule; otherwise its takers' fills, newest first, read until one
    is older than the hold."""
    a, pages, fetched = agg_new(), 0, 0
    if row["kappa"] is None:
        return "fee", a, None, 0, 0, row.get("fee")
    kappa, c, cursor, last = fr_of(row["kappa"]), row["close_us"], None, None
    while True:
        q = [("condition", row["id"]), ("taker_only", "true"), ("limit", 1000)]
        doc = src.json(DATA + "/v2/trades?" + urllib.parse.urlencode(q + ([("cursor", cursor)] if cursor else [])))
        pages += 1
        rows = doc["data"]
        for x in rows:
            ts = int(x["timestamp"])
            assert last is None or ts <= last, "fills not newest first"
            last = ts
            fetched += 1
            hit = poly_trade(x, row["id"], c, row["tokens"])
            if hit is not None:
                agg_add(a, *hit)
        cursor = (doc.get("pagination") or {}).get("next_cursor") or None
        if not cursor or not rows or int(rows[-1]["timestamp"]) * US < c - HOLD_S * US:
            break
    return (None if a["n"] else "no_trade"), a, kappa, pages, fetched, row.get("fee")


# ---- the draws: a series and day, then a market of it, with replacement, until NEED members -------------------


def run_draws(venue, frame_path, days, src, salt, need, dmax, draws_path, clock=None):
    """Draw k picks group uidx(salt, venue, k, 1, groups) and in it row uidx(salt, venue, k, 2, rows); a drawn market
    is fetched once and its result kept, as text, for every later draw of it - one record of sums shared by every
    market with no counted trade. Each draw is a line of `draws_path` as it is made: the first run writes it, a later
    run must write the same bytes. Returns its summary: draws, members, markets fetched, reasons, groups, rows, the
    label-free digest and the file's SHA-256."""
    clock = clock or time.monotonic
    fx = FrameIndex(frame_path)
    try:
        assert len(fx), "BLOCKED: %s's frame is empty" % venue
        ctx = Ctx(venue, days)
        if venue == "kalshi":
            kalshi_open(src, ctx)
        fetch = kalshi_market if venue == "kalshi" else poly_market
        cache, texts, members, t0, empty = {}, {}, 0, clock(), agg_text(agg_new())
        why, dig, k = collections.Counter(), hashlib.sha256(), -1
        with open(draws_path + ".tmp", "wb") as fd:
            for k in range(dmax):
                if members == need:
                    k -= 1
                    break
                g = fx.group(uidx(salt, venue, k, 1, len(fx)))
                row = fx.row(g[2] + uidx(salt, venue, k, 2, g[3]))
                assert (row["day"], row["key"]) == (g[0], g[1]), "a row outside its group"
                hit = cache.get(row["id"])
                if hit is None:
                    reason, a, kappa, pages, fetched, cat = fetch(row, src, ctx)
                    kt = None if kappa is None else fr_text(kappa)
                    hit = cache[row["id"]] = (row["id"], reason, agg_text(a) if a["n"] else empty,
                                              texts.setdefault(kt, kt), pages, fetched, texts.setdefault(cat, cat))
                mid, reason, agg, kappa, pages, fetched, cat = hit
                rec = {"k": k, "day": g[0], "key": g[1], "id": mid, "reason": reason, "agg": agg, "kappa": kappa,
                       "pages": pages, "fetched": fetched, "cat": cat}
                fd.write(jline(rec))
                dig.update(digest_line(rec))
                why[str(reason)] += 1
                members += reason is None
                if k + 1 == PROJECT_AFTER and dmax > PROJECT_AFTER:
                    spent = clock() - t0
                    want = need * (k + 1) / max(members, 1)
                    proj = spent * want / (k + 1)
                    out("%s: %d draws, %d members, %d markets fetched in %.0f s; %d draws projected, %.0f s" % (
                        venue, k + 1, members, len(cache), spent, want, proj))
                    assert proj <= FETCH_MAX_S, "BLOCKED: %s's draws projected at %.0f s, above %d" % (
                        venue, proj, FETCH_MAX_S)
            fd.flush()
            os.fsync(fd.fileno())
        sha = finish_once(draws_path + ".tmp", draws_path)
        return {"draws": k + 1, "members": members, "markets": len(cache), "reasons": dict(sorted(why.items())),
                "groups": len(fx), "rows": fx.rows, "digest": dig.hexdigest(), "sha256": sha}
    finally:
        fx.close()


def digest_line(r):
    """A draw's line of the label-free text draws_digest hashes, in the Architect's own format (TZ-56a section 4.1).
    Pure."""
    a = r["agg"]
    return ("%d|%d|%s|%s|%s|%d|%d|%d|%s|%s|%s\n" % (
        r["k"], r["day"], r["key"], r["id"], r["reason"] or "member", a["n"], a["na"], a["nb"],
        a["sa"], a["sb"], a["q"])).encode("utf-8")


def draws_digest(recs):
    """The SHA-256 of a draw sequence's label-free text: each draw, its market, its reason and its sums. Pure."""
    h = hashlib.sha256()
    for r in recs:
        h.update(digest_line(r))
    return h.hexdigest()


def read_draws(path):
    with open(path, "rb") as fh:
        return [json.loads(line) for line in fh]


# ---- the money and the test (TZ-56a section 1) -------------------------------------------------------------------


def money(a, a_won, kappa, s=""):
    """A member's mean money a contract after the taker's fee, over its counted trades: the side that won pays 1,
    every trade cost its price and kappa p (1 - p). Pure."""
    n = a["n" + s]
    assert n > 0
    nw = a["na" + s] if a_won else a["nb" + s]
    return (nw - a["sa" + s] - a["sb" + s] - kappa * a["q" + s]) / n


def gross(a, a_won, s=""):
    return money(a, a_won, Fr(0), s)


def x_of(y):
    assert Y_LO < y <= Y_HI, "a member's money %s outside (-1, 1/5]" % y
    return (y - Y_LO) / WIDTH


def dec60(x):
    x = Fr(x)
    return C60.divide(D(x.numerator), D(x.denominator))


def bet_log(xs, m, d, cap, up):
    """The log of a betting capital on xs in [0, 1]: the sum of ln(1 + lam_i s_i), s_i = x_i - m where `up` (EARN,
    betting the mean is above m) and m - x_i otherwise (NO EARN), lam_i = min(d / v_i, cap) and v_i = (1/4 + the sum
    over j < i of (x_j - mu_j)^2) / (i + 1), mu_j = (1/2 + the sum of x_1..x_j) / (j + 1) - Waudby-Smith and Ramdas's
    running mean and variance, so every lam_i is fixed before x_i is read. Each factor is at least 1/2. At 60
    digits. Pure."""
    c = C60
    m, d, cap = dec60(m), dec60(d), dec60(cap)
    lk, sx, sv = D(0), D(0), D(0)
    for i, x in enumerate(xs):
        x = dec60(x)
        v = c.divide(c.add(D("0.25"), sv), D(i + 1))
        lam = min(c.divide(d, v), cap)
        f = c.add(D(1), c.multiply(lam, c.subtract(x, m) if up else c.subtract(m, x)))
        assert f >= D("0.5"), "a factor below 1/2"
        lk = c.add(lk, f.ln(c))
        sx = c.add(sx, x)
        mu = c.divide(c.add(D("0.5"), sx), D(i + 2))
        dv = c.subtract(x, mu)
        sv = c.add(sv, c.multiply(dv, dv))
    return lk


def threshold():
    return D(ALPHA_INV).ln(C60)


def reading(lk_e, lk_n):
    """K0's reading on one venue: EARN where the EARN capital reaches 1/alpha, NO EARN where only the NO EARN capital
    does, UNDECIDABLE otherwise - EARN first where both do. Pure."""
    L = threshold()
    if lk_e >= L:
        return "EARN"
    if lk_n >= L:
        return "NO EARN"
    return "UNDECIDABLE"


def score_venue(venue, frame_path, draws_path):
    """K0's reading on one venue from its frame and draws: every member's money, the two capitals and the reading;
    beside them, barred, the money by day, before the fee, on the trades at least SLOW_S before the close, on the
    members that bought both sides, and by category. The draws are read a line at a time; members alone are kept."""
    n_draws, why, drawn, mem = 0, collections.Counter(), set(), []
    with open(draws_path, "rb") as fh:
        for line in fh:
            r = json.loads(line)
            n_draws += 1
            why[str(r["reason"])] += 1
            drawn.add(r["id"])
            if r["reason"] is None:
                mem.append(r)
    labels = frame_labels(frame_path, {r["id"] for r in mem})
    a_label = "yes" if venue == "kalshi" else "A"
    ys, xs, gs, fees, slow, mixed, single = [], [], [], [], [], [], []
    by_day, by_cat = collections.defaultdict(list), collections.defaultdict(list)
    for r in mem:
        a, kappa = agg_of(r["agg"]), fr_of(r["kappa"])
        won = labels[r["id"]] == a_label
        y = money(a, won, kappa)
        ys.append(y)
        xs.append(x_of(y))
        gs.append(gross(a, won))
        fees.append(kappa * a["q"] / a["n"])
        by_day[r["day"]].append(y)
        by_cat[str(r["cat"])].append(y)
        (mixed if a["na"] and a["nb"] else single).append(y)
        if a["n5"]:
            slow.append(money(a, won, kappa, "5"))
    lk_e = bet_log(xs, M0, D_E, CAP_E, True)
    lk_n = bet_log(xs, M1, D_N, CAP_N, False)
    mean = lambda v: (sum(v, Fr(0)) / len(v)) if v else None
    doc = {"venue": venue, "draws": n_draws, "members": len(mem), "reasons": dict(sorted(why.items())),
           "markets_fetched": len(drawn),
           "mean_y": fr_text(mean(ys)), "mean_y_12": dec(mean(ys)), "mean_gross_12": dec(mean(gs)),
           "mean_fee_12": dec(mean(fees)), "log_capital_earn": format(lk_e, "f"),
           "log_capital_no_earn": format(lk_n, "f"), "threshold": format(threshold(), "f"),
           "reading": reading(lk_e, lk_n),
           "barred": {"by_day": {iso(d): [len(v), dec(mean(v))] for d, v in sorted(by_day.items())},
                      "slow": [len(slow), dec(mean(slow)) if slow else None],
                      "mixed": [len(mixed), dec(mean(mixed)) if mixed else None],
                      "single": [len(single), dec(mean(single)) if single else None],
                      "by_category": {k: [len(v), dec(mean(v))] for k, v in sorted(by_cat.items()) if len(v) >= 30}}}
    return doc


# ---- the session's modes -------------------------------------------------------------------------------------


def mode_fingerprint():
    with open(os.path.join(PRIMARY, "SYSTEM-MAP.md"), "rb") as fh:
        raw = fh.read()
    txt = raw.decode("utf-8")
    rev = re.findall(r"^\*\*Revision string:\*\* `([^`]+)`$", txt, re.M)
    assert rev == [MAP_REVISION], "BLOCKED: map revision %r, required %s" % (rev, MAP_REVISION)
    found = dict(ANCHOR_ROW.findall(txt))
    assert found == ANCHORS, "BLOCKED: anchors %r" % found
    for k, rel in sorted(ANCHOR_FILES.items()):
        h = sha256_file(os.path.join(PRIMARY, rel))[:12]
        assert h == ANCHORS[k], "BLOCKED: re-derived %s %s, the map %s" % (k, h, ANCHORS[k])
        out("re-derived %s %s sha256[:12] %s equal" % (k, rel, h))
    rows = ROW.findall(txt)
    states = {k: sum(1 for r in rows if r[3] == k) for k in MAP_ROWS}
    assert states == MAP_ROWS and len(rows) == sum(MAP_ROWS.values()), "BLOCKED: rows %r" % states
    for path, lines, nbytes, state, sha in rows:
        with open(os.path.join(PRIMARY, path), "rb") as fh:
            blob = fh.read()
        got = (blob.count(b"\n"), len(blob), sha256_bytes(blob))
        if state == "frozen":
            want = (int(lines.replace(",", "")), int(nbytes.replace(",", "")), sha)
            assert got == want, "BLOCKED: frozen row %s: %r, the map %r" % (path, got, want)
        out("%-48s %6d lines %8d bytes %s %s%s" % (path, got[0], got[1], got[2], state,
                                                  " equal" if state == "frozen" else ""))
    out("SYSTEM-MAP.md %d lines %d bytes sha256 %s" % (raw.count(b"\n"), len(raw), sha256_bytes(raw)))
    out("FINGERPRINT PASS: revision %s; anchors 6 of 6, 4 re-derived; rows %d: frozen %d of %d equal, tracked %d, "
        "reported %d" % (MAP_REVISION, len(rows), states["frozen"], MAP_ROWS["frozen"], states["tracked"],
                         states["reported"]))


def number_reading(names, own):
    """CANON hard rule 2: CryptoTZ/ holds this TZ's file and no other of its number; CryptoReports/ no report of it.
    Pure."""
    tz = [n for n in names if n.startswith("CryptoTZ/" + NUMBER)]
    rp = [n for n in names if n.startswith("CryptoReports/" + NUMBER)]
    return tz == [own] and not rp, tz, rp


def mode_number():
    names = git("ls-tree", "--name-only", "origin/main", "--", "CryptoTZ/", "CryptoReports/", tree=PRIMARY).split("\n")
    head = git("rev-parse", "origin/main", tree=PRIMARY)
    ok, tz, rp = number_reading(names, OWN_TZ)
    out("origin/main %s: %d paths under CryptoTZ/ and CryptoReports/; of the number %s: %s and %s" % (
        head, len(names), NUMBER, tz, rp))
    out("NUMBER %s" % ("PASS - 2 of 2" if ok else "FAIL"))
    assert ok, "BLOCKED: of the number %s, CryptoTZ/ holds %s and CryptoReports/ %s" % (NUMBER, tz, rp)


def still_reading(before, now):
    """G-STILL: every unit's MainPID, NRestarts and ActiveState as the first read recorded them. Pure."""
    changed = sorted(k for k in before if before[k] != now.get(k))
    return not changed, changed


def mode_still():
    st = load_state()
    now = {}
    for unit in UNITS:
        kv = show(unit, ["MainPID", "NRestarts", "ActiveState", "UnitFileState"])
        now[unit] = {k: kv.get(k) for k in ("MainPID", "NRestarts", "ActiveState")}
        out("%s %s %s" % (unit, now[unit], kv.get("UnitFileState")))
    if "still" not in st:
        st["still"] = {"at": utc(time.time()), "units": now}
        save_state(st)
        out("still: recorded")
        return
    ok, changed = still_reading(st["still"]["units"], now)
    out("G-STILL %s: %s since %s" % ("PASS" if ok else "FAIL", "unchanged" if ok else "changed %s" % changed,
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
    """The UUID directories beside `own`, this session's, each named live or earlier."""
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


PROBES = (
    ("kalshi exchange", KALSHI + "/exchange/status", ("exchange_active",)),
    ("kalshi cutoff", KALSHI + "/historical/cutoff", ("market_settled_ts", "trades_created_ts")),
    ("kalshi markets", None, ("markets", "cursor")),
    ("kalshi trades", KALSHI + "/markets/trades?" + urllib.parse.urlencode(
        [("ticker", "KXZEC15M-26NOV121900-00"), ("limit", 5)]), ("trades", "cursor")),
    ("kalshi series", KALSHI + "/series/KXBTCD", ("series",)),
    ("kalshi series fees", KALSHI + "/series/fee_changes?show_historical=true", ("series_fee_change_arr",)),
    ("kalshi event fees", KALSHI + "/events/fee_changes?limit=1000", ("event_fee_changes", "cursor")),
    ("gamma keyset", None, ("markets",)),
    ("data trades", DATA + "/v2/trades?" + urllib.parse.urlencode(
        [("condition", "0xbdc863ac40456c9cddb58e02610d985bfd08401b0d9a622ede786ed7a085e5bf"), ("taker_only", "true"),
         ("limit", 5)]), ("data", "pagination")),
)


def mode_probe():
    """G-PROBE: one live request per endpoint through Net.get, the requests every later mode makes, each asserted
    served and parsed; Kalshi's cutoff printed."""
    floor_check()
    net, ok = Net(), 0
    out("headers of every venue request: %s" % json.dumps(HEADERS, sort_keys=True))
    for name, url, keys in PROBES:
        url = url or listing_url("kalshi" if name.startswith("kalshi") else "polymarket", R0, None)
        body = net.get(url)
        doc = jloads(body)
        missing = [k for k in keys if k not in doc]
        out("%-18s GET %s -> 200, %d bytes, sha256 %s, keys %s%s" % (
            name, redact(url), len(body), sha256_bytes(body), sorted(doc)[:8], " MISSING %s" % missing if missing else ""))
        ok += not missing
        if name == "kalshi cutoff":
            out("kalshi historical cutoff: %s" % json.dumps({k: doc.get(k) for k in sorted(doc)}, sort_keys=True))
    out("retries %s" % dict(net.retries))
    assert ok == len(PROBES), "BLOCKED: G-PROBE %d of %d" % (ok, len(PROBES))
    out("G-PROBE PASS: %d of %d endpoints served and parsed" % (ok, len(PROBES)))


def venue_phase(venue, days, root, salt, need, dmax, live, label, closed_by):
    """One venue's frame and draws under `root`: its kept replies replayed and, where live, the network beside them.
    Returns the summary a mode prints and records."""
    os.makedirs(root, exist_ok=True)
    net = Net() if live else None
    fpath, dpath = os.path.join(root, "frame-%s.jsonl" % venue), os.path.join(root, "draws-%s.jsonl" % venue)
    t0 = time.monotonic()
    src = Source(Sink(os.path.join(root, "raw-frame-%s.jsonl.gz" % venue)), net)
    rows, keys, reasons, pages = build_frame(venue, days, src, fpath, closed_by)
    out("%s %s frame: %d rows in %d groups; others %s; %d pages, %d replayed, %d new, %.0f s" % (
        label, venue, rows, keys, reasons, pages, src.kept, src.live, time.monotonic() - t0))
    t1 = time.monotonic()
    src = Source(Sink(os.path.join(root, "raw-draw-%s.jsonl.gz" % venue)), net)
    sm = run_draws(venue, fpath, days, src, salt, need, dmax, dpath)
    assert (sm["groups"], sm["rows"]) == (keys, rows), "the frame file is not the frame"
    out("%s %s draws: %d considered, %d members, %d markets fetched; %s; %d requests, %d replayed, %d new, %.0f s" % (
        label, venue, sm["draws"], sm["members"], sm["markets"], sm["reasons"], src.i, src.kept, src.live,
        time.monotonic() - t1))
    if net is not None:
        out("%s %s retries %s, requests %s" % (label, venue, dict(net.retries), dict(net.count)))
    return {"rows": rows, "keys": keys, "reasons": reasons, "pages": pages, "draws": sm["draws"],
            "members": sm["members"], "digest": sm["digest"], "frame_sha256": sha256_file(fpath),
            "draws_sha256": sm["sha256"]}


def mode_rehearse():
    """2026-11-12 - read already - framed and drawn on both venues to REH_NEED members each, every reply kept; its
    figures - rows, series-days, the other rows by reason, draws, the draws' label-free SHA-256 and the members' money
    before the fee - and the SHA-256 of every kept-reply file written to rehearsal/instrument.json for `agree`."""
    floor_check()
    doc = {"venues": {}}
    for venue in VENUES:
        s = venue_phase(venue, (R0,), REHEARSAL, REH_SALT, REH_NEED, REH_DRAWS_MAX[venue], True, "rehearsal",
                        REH_CLOSED_BY)
        recs = read_draws(os.path.join(REHEARSAL, "draws-%s.jsonl" % venue))
        mem = [r for r in recs if r["reason"] is None]
        labels = frame_labels(os.path.join(REHEARSAL, "frame-%s.jsonl" % venue), {r["id"] for r in mem})
        a_label = "yes" if venue == "kalshi" else "A"
        g = sum((gross(agg_of(r["agg"]), labels[r["id"]] == a_label) for r in mem), Fr(0))
        kap = hashlib.sha256("".join("%s|%s\n" % (r["id"], r["kappa"]) for r in mem).encode()).hexdigest()
        doc["venues"][venue] = {"rows": s["rows"], "keys": s["keys"], "reasons": s["reasons"], "draws": s["draws"],
                                "digest": s["digest"], "gross": fr_text(g)}
        for k in REH_FIGURES:
            out("rehearsal %s %-8s %s" % (venue, k, doc["venues"][venue][k]))
        out("rehearsal %s members %d, money before the fee %s a contract; fee coefficients' sha256 %s (recorded)" % (
            venue, len(mem), dec(g / len(mem)), kap))
    doc["files"] = {n: sha256_file(os.path.join(REHEARSAL, n)) for n in REH_FILES}
    write_once(INSTRUMENT_FIGURES, json.dumps(doc, sort_keys=True, indent=1).encode("utf-8") + b"\n")
    out("rehearsal: %d figures and %d kept-reply files written for agree" % (len(VENUES) * len(REH_FIGURES),
                                                                             len(REH_FILES)))


def agreement(mine, ref):
    """G-REHEARSAL: (figures equal, figures compared, the lines to print) - the instrument's twelve figures against
    the reference's, both read from kept-reply files they record at the same SHA-256. Pure."""
    assert mine["files"] == ref["files"], "BLOCKED: the reference read other kept replies: %r and %r" % (
        mine["files"], ref["files"])
    lines, eq = [], 0
    for v in VENUES:
        for k in REH_FIGURES:
            a, b = mine["venues"][v][k], ref["venues"][v][k]
            lines.append("G-REHEARSAL %s %-8s %s, the reference's %s: %s" % (v, k, a, b, "equal" if a == b else
                                                                             "DIFFERENT"))
            eq += a == b
    return eq, len(VENUES) * len(REH_FIGURES), lines


def mode_agree():
    """G-REHEARSAL: rehearse's figures against the reference's, on the kept-reply files both record, each still at
    that SHA-256."""
    mine, ref = load_json(INSTRUMENT_FIGURES), load_json(REFERENCE_FIGURES)
    assert sorted(mine["files"]) == sorted(REH_FILES), "BLOCKED: rehearse recorded %r" % sorted(mine["files"])
    for n, h in sorted(mine["files"].items()):
        assert sha256_file(os.path.join(REHEARSAL, n)) == h, "BLOCKED: %s is not the file rehearse kept" % n
        out("kept %s sha256 %s" % (n, h))
    eq, total, lines = agreement(mine, ref)
    for ln in lines:
        out(ln)
    assert eq == total, "BLOCKED: G-REHEARSAL %d of %d" % (eq, total)
    out("G-REHEARSAL PASS: %d of %d figures equal to the reference's on the same kept replies" % (eq, total))


def clock_gate():
    now = time.time()
    assert now >= NOT_BEFORE, "BLOCKED: %s is before %s" % (utc(now), utc(NOT_BEFORE))
    out("now %s, at or after %s" % (utc(now), utc(NOT_BEFORE)))


def mode_frame():
    """G-FRAME: both venues' frames over the six days, every reply kept; resumes from its kept replies."""
    clock_gate()
    floor_check()
    st = load_state()
    for venue in VENUES:
        fpath = os.path.join(RUN, "frame-%s.jsonl" % venue)
        os.makedirs(RUN, exist_ok=True)
        net = Net()
        src = Source(Sink(os.path.join(RUN, "raw-frame-%s.jsonl.gz" % venue)), net)
        t0 = time.monotonic()
        rows, keys, reasons, pages = build_frame(venue, DAYS, src, fpath, CLOSED_BY)
        fx = FrameIndex(fpath)
        fx.close()
        per_day = collections.Counter()
        for i in range(len(fx)):
            per_day[fx.days[i]] += fx.counts[i]
        out("%s frame: %d rows in %d groups; others %s; %d pages, %d replayed, %d new, %.0f s; retries %s" % (
            venue, rows, keys, reasons, pages, src.kept, src.live, time.monotonic() - t0, dict(net.retries)))
        out("%s rows by day: %s" % (venue, {iso(d): per_day[d] for d in DAYS}))
        assert all(per_day[d] > 0 for d in DAYS), "BLOCKED: G-FRAME: %s holds a day with no row" % venue
        st.setdefault("frame", {})[venue] = {"rows": rows, "keys": keys, "reasons": reasons, "pages": pages,
                                             "sha256": sha256_file(fpath), "at": utc(time.time())}
        save_state(st)
    out("G-FRAME PASS: both venues framed, every day holding rows")


def mode_draw():
    """G-SET: both venues' draws to NEED members, every reply kept; resumes from its kept replies."""
    clock_gate()
    floor_check()
    st = load_state()
    for venue in VENUES:
        fpath = os.path.join(RUN, "frame-%s.jsonl" % venue)
        assert sha256_file(fpath) == st["frame"][venue]["sha256"], "BLOCKED: %s's frame is not frame's" % venue
        net = Net()
        src = Source(Sink(os.path.join(RUN, "raw-draw-%s.jsonl.gz" % venue)), net)
        t0 = time.monotonic()
        sm = run_draws(venue, fpath, DAYS, src, SALT, NEED, DRAWS_MAX[venue], os.path.join(RUN, "draws-%s.jsonl" % venue))
        out("%s draws: %d considered, %d members, %d markets fetched; %s; %d requests, %d replayed, %d new, %.0f s; "
            "retries %s" % (venue, sm["draws"], sm["members"], sm["markets"], sm["reasons"], src.i, src.kept, src.live,
                            time.monotonic() - t0, dict(net.retries)))
        assert sm["members"] == NEED, "BLOCKED: G-SET: %s has %d members in %d draws, %d needed" % (
            venue, sm["members"], sm["draws"], NEED)
        st.setdefault("draw", {})[venue] = {"draws": sm["draws"], "members": sm["members"], "sha256": sm["sha256"],
                                            "digest": sm["digest"], "at": utc(time.time())}
        save_state(st)
    out("G-SET PASS: %d members on each venue" % NEED)


def mode_redraw():
    """DETERMINISM: both venues' frames and draws built again from the kept replies alone, no request, each file
    byte for byte the one frame and draw wrote."""
    st = load_state()
    os.makedirs(REDRAW, exist_ok=True)
    ok = 0
    for venue in VENUES:
        fa, fb = os.path.join(RUN, "frame-%s.jsonl" % venue), os.path.join(REDRAW, "frame-%s.jsonl" % venue)
        build_frame(venue, DAYS, Source(Sink(os.path.join(RUN, "raw-frame-%s.jsonl.gz" % venue))), fb, CLOSED_BY)
        db = os.path.join(REDRAW, "draws-%s.jsonl" % venue)
        run_draws(venue, fb, DAYS, Source(Sink(os.path.join(RUN, "raw-draw-%s.jsonl.gz" % venue))), SALT, NEED,
                  DRAWS_MAX[venue], db)
        for a, b, want in ((fa, fb, st["frame"][venue]["sha256"]), (os.path.join(RUN, "draws-%s.jsonl" % venue), db,
                                                                     st["draw"][venue]["sha256"])):
            ha, hb = sha256_file(a), sha256_file(b)
            out("%s %s and %s: %s" % (os.path.basename(a), ha, hb, "equal" if ha == hb == want else "DIFFERENT"))
            ok += ha == hb == want
    assert ok == 4, "DETERMINISM FAIL: %d of 4" % ok
    out("DETERMINISM PASS: 4 of 4 files rebuilt from the kept replies, byte for byte")


def label_gate(st):
    """No label is read before the frames and the draws are on disk under their recorded SHA-256 and this file's
    commit is on origin (TZ-56a section 2 item 8)."""
    for venue in VENUES:
        for kind, name in (("frame", "frame-%s.jsonl"), ("draw", "draws-%s.jsonl")):
            assert sha256_file(os.path.join(RUN, name % venue)) == st[kind][venue]["sha256"], \
                "BLOCKED: %s %s is not as recorded" % (venue, kind)
    head = git("rev-parse", "HEAD")
    remote = [ln.split("\t")[0] for ln in git("ls-remote", "origin", "refs/heads/" + BRANCH, tree=PRIMARY).split("\n")
              if "\t" in ln]
    with open(os.path.join(HERE, PYFILE), "rb") as fh:
        mine = sha256_bytes(fh.read())
    committed = sha256_bytes(subprocess.run(["git", "-C", WT, "show", "HEAD:research/" + PYFILE],
                                            capture_output=True, check=True).stdout)
    assert remote == [head] and mine == committed, "BLOCKED: this file's commit is not on origin"
    out("label gate: frames and draws as recorded; HEAD %s on origin; this file %s, committed" % (head, mine))


def mode_score():
    st = load_state()
    label_gate(st)
    docs = {v: score_venue(v, os.path.join(RUN, "frame-%s.jsonl" % v), os.path.join(RUN, "draws-%s.jsonl" % v))
            for v in VENUES}
    for v, doc in docs.items():
        out("%s: %d members of %d draws; mean money a contract after the fee %s (before it %s, the fee %s); "
            "log capital EARN %s, NO EARN %s, threshold ln 400 = %s: %s" % (
                v, doc["members"], doc["draws"], doc["mean_y_12"], doc["mean_gross_12"], doc["mean_fee_12"],
                dec(Fr(D(doc["log_capital_earn"])), 6), dec(Fr(D(doc["log_capital_no_earn"])), 6),
                dec(Fr(D(doc["threshold"])), 6), doc["reading"]))
        out("%s barred: %s" % (v, json.dumps(doc["barred"], sort_keys=True)))
    write_once(os.path.join(RUN, "score.json"), json.dumps(docs, sort_keys=True, indent=1).encode("utf-8") + b"\n")
    out("K0: Kalshi %s, Polymarket %s" % (docs["kalshi"]["reading"], docs["polymarket"]["reading"]))


# ---- the Release of the reading's inputs (CANON hard rule 16) --------------------------------------------------

RELEASE_NOTES = WORK + "/release-notes.md"


def release_plan():
    """(asset name, source path, how): every file the reading rests on - the frames and draws gzipped, the kept
    replies and the score as they are, the rehearsal's kept replies. Pure."""
    plan = []
    for v in VENUES:
        plan += [("tz56a-frame-%s.jsonl.gz" % v, os.path.join(RUN, "frame-%s.jsonl" % v), "gzip"),
                 ("tz56a-draws-%s.jsonl.gz" % v, os.path.join(RUN, "draws-%s.jsonl" % v), "gzip"),
                 ("tz56a-raw-frame-%s.jsonl.gz" % v, os.path.join(RUN, "raw-frame-%s.jsonl.gz" % v), "link"),
                 ("tz56a-raw-draw-%s.jsonl.gz" % v, os.path.join(RUN, "raw-draw-%s.jsonl.gz" % v), "link"),
                 ("tz56a-rehearsal-raw-frame-%s.jsonl.gz" % v, os.path.join(REHEARSAL, "raw-frame-%s.jsonl.gz" % v),
                  "link"),
                 ("tz56a-rehearsal-raw-draw-%s.jsonl.gz" % v, os.path.join(REHEARSAL, "raw-draw-%s.jsonl.gz" % v),
                  "link")]
    plan.append(("tz56a-score.json", os.path.join(RUN, "score.json"), "link"))
    return plan


def mode_pack():
    st = load_state()
    label_gate(st)
    commit = git("rev-parse", "HEAD")
    os.makedirs(RELEASE_DIR, exist_ok=True)
    assets = []
    for name, src, how in release_plan():
        dest = os.path.join(RELEASE_DIR, name)
        if how == "gzip":
            gz_file_once(src, dest)
        elif not os.path.exists(dest):
            os.link(src, dest)
        assert os.path.samefile(dest, src) if how == "link" else True, "%s is not %s" % (dest, src)
        size, sha = os.path.getsize(dest), sha256_file(dest)
        assert size < 2147483648, "%s is over 2 GiB" % name
        assets.append({"asset": name, "bytes": size, "sha256": sha})
        out("asset %-44s %11d bytes sha256 %s" % (name, size, sha))
    doc = {"tag": TAG, "commit": commit, "repo": REPO, "assets": assets, "assets_n": len(assets),
           "bytes_total": sum(a["bytes"] for a in assets)}
    write_once(RELEASE_SET, json.dumps(doc, sort_keys=True, indent=1).encode("utf-8") + b"\n")
    notes = ("TZ-56a K0: the inputs of K0's reading - both venues' frames, draws and every venue reply they rest on, "
             "the score, and the rehearsal's replies of 2026-11-12. Instrument research/tz56-k0-favourite.py at %s. "
             "Every reply is one gzip member of one JSON line: url, bytes, sha256, body.\n" % commit)
    write_once(RELEASE_NOTES, notes.encode("utf-8"))
    st["pack"] = {"set_sha256": sha256_file(RELEASE_SET), "commit": commit, "assets_n": len(assets),
                  "bytes_total": doc["bytes_total"]}
    save_state(st)
    out("PACK: %d assets, %d bytes, at commit %s; set sha256 %s" % (len(assets), doc["bytes_total"], commit,
                                                                    st["pack"]["set_sha256"]))


def gh_get(url, accept="application/vnd.github+json"):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept, "X-GitHub-Api-Version": "2022-11-28"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.status, r.read(), r.geturl()


def mode_verify():
    """G-TAG, G-UPLOAD and G-DOWNLOAD with no credential: the Release on its tag holds every asset of the set by
    name, size and digest, and each downloads to the set's bytes; the tag is lightweight at the pack's commit."""
    st = load_state()
    with open(RELEASE_SET, "rb") as fh:
        raw = fh.read()
    assert sha256_bytes(raw) == st["pack"]["set_sha256"], "release-set.json is not the set pack wrote"
    doc = json.loads(raw)
    status, body, _u = gh_get("https://api.github.com/repos/%s/releases/tags/%s" % (REPO, TAG))
    rel = json.loads(body)
    status, body, _u = gh_get("https://api.github.com/repos/%s/releases/%d/assets?per_page=100" % (REPO, rel["id"]))
    have = {a["name"]: a for a in json.loads(body)}
    rows, ok_api, ok_dl = [], 0, 0
    for x in doc["assets"]:
        a = have.get(x["asset"], {})
        api = (a.get("size") == x["bytes"] and a.get("state") == "uploaded"
               and a.get("digest") in (None, "sha256:" + x["sha256"])
               and a.get("browser_download_url") == "https://github.com/%s/releases/download/%s/%s" % (
                   REPO, TAG, x["asset"]))
        h, n = hashlib.sha256(), 0
        req = urllib.request.Request(a.get("browser_download_url") or "https://github.com/%s/releases/download/%s/%s"
                                     % (REPO, TAG, x["asset"]), headers={"User-Agent": UA,
                                                                          "Accept": "application/octet-stream"})
        with urllib.request.urlopen(req, timeout=300) as r:
            for chunk in iter(lambda: r.read(1 << 20), b""):
                h.update(chunk)
                n += len(chunk)
        dl = n == x["bytes"] and h.hexdigest() == x["sha256"]
        ok_api += api
        ok_dl += dl
        rows.append({"asset": x["asset"], "bytes": x["bytes"], "sha256": x["sha256"], "api_ok": api,
                     "digest": a.get("digest"), "download_ok": dl, "download_bytes": n})
        out("V %-44s api %s digest %s download %s %d bytes" % (x["asset"], api, a.get("digest"), dl, n))
    beyond = sorted(set(have) - {x["asset"] for x in doc["assets"]})
    lines = [ln.split("\t") for ln in git("ls-remote", "origin", "refs/tags/" + TAG, "refs/tags/%s^{}" % TAG,
                                          tree=PRIMARY).split("\n") if "\t" in ln]
    tag_ok = lines == [[doc["commit"], "refs/tags/" + TAG]]
    out("tag %s on origin: %s; the pack's commit %s; the Release's target %s; assets beyond the set %s" % (
        TAG, lines, doc["commit"], rel.get("target_commitish"), beyond))
    n = doc["assets_n"]
    assert ok_api == n and ok_dl == n and not beyond and tag_ok and rel.get("draft") is False, \
        "VERIFY FAIL: api %d, download %d of %d; beyond %r; tag %s" % (ok_api, ok_dl, n, beyond, tag_ok)
    write_once(VERIFY_FILE, json.dumps({"tag": TAG, "release_id": rel["id"], "commit": doc["commit"],
                                        "assets": rows}, sort_keys=True, indent=1).encode("utf-8") + b"\n")
    out("G-UPLOAD PASS: %d of %d assets by name, size, state and digest; G-DOWNLOAD PASS: %d of %d downloads, %d "
        "bytes; G-TAG PASS: %s at %s" % (ok_api, n, ok_dl, n, sum(r["download_bytes"] for r in rows), TAG,
                                         doc["commit"]))


# ---- reclaim (CANON hard rule 15) -----------------------------------------------------------------------------


def report_tokens():
    tokens = set()
    for name in sorted(os.listdir(REPORTS)):
        if name.endswith(".md"):
            with open(os.path.join(REPORTS, name), encoding="utf-8", errors="replace") as fh:
                tokens.update(TOKEN.findall(fh.read()))
    return tokens


def by_name(tree, rel):
    return tree == WORK and (rel in ("state.json", "read-ledger.jsonl", "release-set.json", "verify.json",
                                     "release-notes.md") or rel.startswith("logs/"))


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


def released_by(path=None):
    """SHA-256 -> asset, for every asset verify proved by a full anonymous download (map section 7 item 167)."""
    path = VERIFY_FILE if path is None else path
    if not os.path.exists(path):
        return {}
    return {a["sha256"]: a["asset"] for a in load_json(path)["assets"] if a.get("download_ok") is True}


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
    released = released_by() if WORK in trees else {}
    before = sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    out("reclaim: %d report tokens; forensic store holds %d files; the Release %s proved %d assets" % (
        len(tokens), before, TAG, len(released)))
    considered = named = kept = copied = held = in_release = 0
    seen = set()
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
                if h in released and not is_kept:
                    in_release += 1
                    out("R release %s %s is %s of %s" % (h, path, released[h], TAG))
                    continue
                dest = os.path.join(FORENSICS, os.path.basename(tree) + "--" + rel.replace("/", "--"))
                if dest in seen or os.path.exists(dest):
                    got = sha256_file(dest)
                    assert got == h, "reclaim: %s exists with sha256 %s, source %s" % (dest, got, h)
                    held += 1
                    out("R held   %s %s" % (h, dest))
                    continue
                size, free = os.path.getsize(path), free_bytes()
                assert free - size >= DISK_FLOOR, "BLOCKED: reclaim: %d bytes free, %s is %d, the floor %d" % (
                    free, path, size, DISK_FLOOR)
                with open(path, "rb") as src, open(dest, "xb") as dst:
                    shutil.copyfileobj(src, dst, 1 << 20)
                assert sha256_file(dest) == h, "reclaim: %s did not copy whole" % dest
                seen.add(dest)
                copied += 1
                out("R copied %s %s" % (h, dest))
    after = sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    assert after == before + copied, "reclaim: store %d, expected %d" % (after, before + copied)
    out("RECLAIM PASS: %d files considered, %d named by a report, %d kept by name, %d copied, %d already held, %d left "
        "to the Release %s that holds them; forensic store %d -> %d files" % (
            considered, named, kept, copied, held, in_release, TAG, before, after))


def read_ledger(mode):
    """One line a mode that reads the venues or a label: this file's SHA-256 and the work tree's HEAD."""
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
    table = {"fingerprint": mode_fingerprint, "number": mode_number, "selftest": mode_selftest, "still": mode_still,
             "probe": mode_probe, "rehearse": mode_rehearse, "agree": mode_agree, "frame": mode_frame,
             "draw": mode_draw,
             "redraw": mode_redraw, "score": mode_score, "pack": mode_pack, "verify": mode_verify}
    try:
        if mode in ("rehearse", "frame", "draw", "redraw", "score", "pack"):
            read_ledger(mode)
        if mode == "reclaim":
            mode_reclaim(rest)
        elif mode == "scratch":
            assert len(rest) == 1, "scratch OWN"
            mode_scratch(rest[0])
        else:
            assert mode in table and not rest, "unknown mode %r" % (argv,)
            table[mode]()
    finally:    # printed on every exit, a BLOCK's and a failed assert's included
        out("malloc tuned: %s" % MALLOC_TUNED)
        out("peak memory of this run: %d bytes" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024))
        out("opens, requests and processes refused: %d" % len(REFUSED))


# ---- the self-test: literals, a synthetic world on both venues and temporary trees under the work tree ------------

ST_ROOT = WORK + "/selftest"
S0 = 1793145600                   # 2026-10-28 00:00:00 UTC: the synthetic world's first day; two days
ST_DAYS = (S0, S0 + DAY)
ST_CLOSED_BY = S0 + 4 * DAY       # 2026-11-01 00:00:00 UTC: a synthetic Polymarket market closed after it is late
ST_LKE = D("-1.744615088220908100869793218979768720033236687991073121285086525276")
ST_LKN = D("1.611895887381554669287919807853835047628972698029545531473306021404036")
ST_LN400 = D("5.991464547107981986870447152285081551353203245978056460308015820921932")


class FakeNet:
    """The network of the self-test: a reply for each URL it knows, a failed assert for any other."""

    def __init__(self, pages):
        self.pages, self.asked, self.count, self.retries = pages, [], collections.Counter(), collections.Counter()

    def get(self, url):
        self.asked.append(url)
        assert url in self.pages, "selftest: no reply for %s" % url
        return self.pages[url]


def _b(obj):
    return json.dumps(obj).encode("utf-8")


def _km(ticker, close, result="yes", vol="5.00", mtype="binary", status="finalized"):
    return {"ticker": ticker, "event_ticker": ticker.rsplit("-", 1)[0], "close_time": iso(close), "result": result,
            "volume_fp": vol, "market_type": mtype, "status": status}


def _kt(i, ticker, at_us, side, yes, block=False):
    t = at_us // US
    return {"trade_id": "t%d" % i, "ticker": ticker, "taker_outcome_side": side, "yes_price_dollars": yes,
            "no_price_dollars": format(D(1) - D(yes), "f"), "count_fp": "1.00",
            "is_block_trade": block,
            "created_time": time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(t)) + ".%06dZ" % (at_us % US)}


def _pm(cid, end, closed, prices, tokens, series=None, event="ev", outcomes=("Yes", "No"), fees=True, rate="0.05",
        exponent=1, version="v1"):
    return {"conditionId": cid, "endDate": iso(end), "closedTime": closed, "version": version,
            "outcomePrices": json.dumps(prices),
            "clobTokenIds": json.dumps(tokens), "outcomes": json.dumps(list(outcomes)),
            "events": [{"slug": event, "series": [{"slug": series}] if series else []}], "feesEnabled": fees,
            "feeSchedule": {"exponent": exponent, "rate": float(rate), "takerOnly": True} if fees else None,
            "feeType": "synthetic"}


def _pt(cid, tok, oi, side, price, ts):
    return {"condition_id": cid, "token_id": tok, "outcome_index": oi, "side": side, "price": float(price),
            "timestamp": ts, "outcome": "x", "size": 10.0}


def synthetic_world():
    """Both venues' synthetic replies over ST_DAYS: every reason of the frames and the draws met once."""
    P = {}
    k_list = lambda d, cur: (KALSHI + "/markets?limit=1000&min_close_ts=%d&max_close_ts=%d&mve_filter=exclude%s" % (
        d - 3600, d + 90000, "&cursor=" + cur if cur else ""))
    c1, c2, ce, cf, ca2 = S0 + 3600, S0 + 7200, S0 + DAY - 600, S0 + 50000, S0 + DAY + 3600
    P[k_list(S0, None)] = _b({"markets": [
        _km("KXA-26OCT28-T1", c1, "yes", "12.00"), _km("KXA-26OCT28-T2", c2, "no", "3.00"),
        _km("KXB-26OCT28-T1", S0 + 40000, "scalar"), _km("KXC-26OCT28-T1", S0 + 100, vol="0.00"),
        _km("KXD-26OCT28-T1", S0 + 200, mtype="scalar"), _km("KXA-26OCT28-T9", S0 + 300, status="determined"),
        _km("KXA-26OCT27-T1", S0 - 1800)], "cursor": "c1"})
    P[k_list(S0, "c1")] = _b({"markets": [_km("KXE-26OCT28-T1", ce), _km("KXF-26OCT28-T1", cf),
                                          _km("KXA-26OCT28-T2", c2, "no", "3.00")], "cursor": ""})
    P[k_list(S0 + DAY, None)] = _b({"markets": [_km("KXE-26OCT28-T1", ce), _km("KXA-26OCT29-T1", ca2),
                                                _km("KXG-26OCT29-T1", S0 + 2 * DAY + 1800)], "cursor": ""})
    P[KALSHI + "/historical/cutoff"] = _b({"market_settled_ts": "2026-09-22T00:00:00Z",
                                           "trades_created_ts": "2026-09-22T00:00:00Z"})
    P[KALSHI + "/series/fee_changes?show_historical=true"] = _b({"series_fee_change_arr": [
        {"series_ticker": "KXF", "scheduled_ts": iso(S0 + 100), "fee_type": "quadratic", "fee_multiplier": 1},
        {"series_ticker": "KXA", "scheduled_ts": iso(S0 - 5 * DAY), "fee_type": "quadratic", "fee_multiplier": 1}]})
    P[KALSHI + "/events/fee_changes?limit=1000"] = _b({"event_fee_changes": [{"event_ticker": "KXA-26OCT29"}],
                                                       "cursor": ""})
    for key, ftype in (("KXA", "quadratic"), ("KXE", "flat"), ("KXF", "quadratic")):
        P[KALSHI + "/series/" + key] = _b({"series": {"ticker": key, "fee_type": ftype, "fee_multiplier": 1,
                                                       "category": "Synthetic"}})
    kt = lambda t, c, cur: KALSHI + "/markets/trades?ticker=%s&limit=1000&min_ts=%d&max_ts=%d%s" % (
        t, c - 86401, c + 1, "&cursor=" + cur if cur else "")
    T1, T2 = "KXA-26OCT28-T1", "KXA-26OCT28-T2"
    P[kt(T1, c1, None)] = _b({"trades": [
        _kt(1, T1, (c1 - 1000) * US, "yes", "0.8500"), _kt(2, T1, (c1 - 100) * US, "no", "0.1000"),
        _kt(3, T1, (c1 - 50) * US, "yes", "0.9500"), _kt(4, T1, (c1 - DAY) * US, "yes", "0.8000"),
        _kt(5, T1, c1 * US, "yes", "0.8500"), _kt(6, T1, (c1 - 10) * US, "yes", "0.8500", True),
        _kt(7, T1, (c1 - 20) * US, "yes", "0.7999"), _kt(8, T1, (c1 - DAY) * US - 1, "yes", "0.8500")], "cursor": ""})
    P[kt(T2, c2, None)] = _b({"trades": [_kt(9, T2, (c2 - 3600) * US, "no", "0.1200")], "cursor": "n2"})
    P[kt(T2, c2, "n2")] = _b({"trades": [_kt(10, T2, (c2 - 200) * US, "yes", "0.8300")], "cursor": ""})
    p_list = lambda d, cur: GAMMA + "/markets/keyset?limit=100&closed=true&end_date_min=%s&end_date_max=%s%s" % (
        urllib.parse.quote(iso(d - 3600), safe=""), urllib.parse.quote(iso(d + 90000), safe=""),
        "&after_cursor=" + cur if cur else "")
    A1, A2, A3, A4, A5, A6 = ("0x" + c * 64 for c in "123456")
    B1, B2, C1 = "0x" + "b" * 64, "0x" + "c" * 64, "0x" + "d" * 64
    pa1, pb1 = S0 + 3600, S0 + 20000
    P[p_list(S0, None)] = _b({"markets": [
        _pm(A1, S0 + 1000, "2026-10-28 01:00:00+00", ["1", "0"], ["11", "12"], series="ser-a"),
        _pm(A2, S0 + 1000, "2026-10-28 01:00:00+00", ["0.5", "0.5"], ["13", "14"], series="ser-a"),
        _pm(A3, S0 + 1000, "2026-10-28 01:00:00+00", ["1", "0"], ["15", "16"], outcomes=("a", "b", "c")),
        _pm(A4, S0 + 1000, "", ["1", "0"], ["17", "18"]),
        dict(_pm(A5, S0 + 1000, "2026-10-28 01:00:00+00", ["1", "0"], ["19", "20"]), events=[]),
        _pm(A6, S0 - 1800, "2026-10-27 23:40:00+00", ["1", "0"], ["21", "22"]),
        _pm("0x" + "7" * 64, S0 + 1000, "2026-10-28 01:00:00+00", ["1", "0"], ["23", "24"], version="v2"),
        _pm("0x" + "8" * 64, S0 + 1000, "2026-11-01 00:00:01+00", ["1", "0"], ["25", "26"])], "next_cursor": "q2"})
    P[p_list(S0, "q2")] = _b({"markets": [
        _pm(B1, S0 + 2000, "2026-10-28T05:33:20.250000Z", ["0", "1"], ["31", "32"], event="ev-b",
            outcomes=("Over", "Under"), fees=False),
        _pm(B2, S0 + 2000, "2026-10-28 02:00:00+00", ["0", "1"], ["33", "34"], series="ser-a", exponent=2),
        _pm(A1, S0 + 1000, "2026-10-28 01:00:00+00", ["1", "0"], ["11", "12"], series="ser-a")]})
    P[p_list(S0 + DAY, None)] = _b({"markets": [
        _pm(C1, S0 + DAY + 500, "2026-10-29 00:10:00+00", ["1", "0"], ["41", "42"], series="ser-a", rate="0.01")]})
    dt = lambda cid, cur: DATA + "/v2/trades?condition=%s&taker_only=true&limit=1000%s" % (
        cid, "&cursor=" + cur if cur else "")
    P[dt(A1, None)] = _b({"data": [_pt(A1, "11", 0, "BUY", "0.85", pa1 - 100), _pt(A1, "12", 1, "SELL", "0.12", pa1 - 400),
                                   _pt(A1, "12", 1, "BUY", "0.92", pa1 - 500)], "pagination": {"next_cursor": "r2"}})
    P[dt(A1, "r2")] = _b({"data": [_pt(A1, "11", 0, "BUY", "0.95", pa1 - 600), _pt(A1, "11", 0, "BUY", "0.8", pa1 - DAY),
                                   _pt(A1, "11", 0, "BUY", "0.85", pa1 - DAY - 1)], "pagination": {"next_cursor": "r3"}})
    P[dt(B1, None)] = _b({"data": [_pt(B1, "31", 0, "SELL", "0.1", pb1 - 1000)], "pagination": {"next_cursor": None}})
    P[dt(C1, None)] = _b({"data": [_pt(C1, "41", 0, "BUY", "0.5", S0 + DAY + 100)], "pagination": {"next_cursor": None}})
    return P


def _expected_draws(salt, venue, groups, need, dmax, member_ids):
    """The draw sequence, computed with hashlib directly: (k, group index, row index) until `need` members."""
    seq, members = [], 0
    for k in range(dmax):
        if members == need:
            break
        h1 = int(hashlib.sha256(("%s|%s|%d|1" % (salt, venue, k)).encode()).hexdigest(), 16)
        gi = h1 % len(groups)
        h2 = int(hashlib.sha256(("%s|%s|%d|2" % (salt, venue, k)).encode()).hexdigest(), 16)
        ri = h2 % len(groups[gi])
        seq.append((k, gi, ri))
        members += groups[gi][ri] in member_ids
    return seq


def mode_selftest():
    checks = [0]

    def ok(cond, what):
        assert cond, "SELFTEST FAIL: %s" % what
        checks[0] += 1

    if os.path.exists(ST_ROOT):
        shutil.rmtree(ST_ROOT)
    os.makedirs(ST_ROOT)
    # instants, days and the draw's index
    ok(us_of("2026-11-12T23:59:59.123456Z") == 1794527999123456, "us_of ISO with micro")
    ok(us_of("2026-11-12 00:01:21+00") == 1794441681000000, "us_of gamma +00")
    ok(us_of("2026-11-12 22:00:02.179582+00") == 1794520802179582, "us_of gamma micro")
    ok(us_of("2026-11-13T00:00:00Z") == 1794528000000000, "us_of ISO Z")
    ok(us_of("2026-11-12 00:10:54.826688+00:00:00") == 1794442254826688, "us_of +00:00:00")
    ok(iso(W0) == "2026-11-16T00:00:00Z" and iso(DAYS[-1] + DAY) == "2026-11-22T00:00:00Z" and
       iso(R0) == "2026-11-12T00:00:00Z" and iso(NOT_BEFORE) == "2026-11-23T12:00:00Z", "the TZ's instants")
    ok(day_of(DAYS[0] * US, DAYS) == DAYS[0] and day_of((DAYS[-1] + DAY) * US - 1, DAYS) == DAYS[-1] and
       day_of((DAYS[-1] + DAY) * US, DAYS) is None and day_of(DAYS[0] * US - 1, DAYS) is None, "day_of's ends")
    ok(uidx("TZ-56-K0", "kalshi", 0, 1, 3100) == 2809 and uidx("TZ-56-K0", "polymarket", 17, 2, 5843) == 944 and
       uidx("TZ-56-K0-REHEARSAL", "kalshi", 59, 1, 517) == 159 and uidx("x", "y", 5, 1, 1) == 0, "uidx literals")
    # the floors: the memory floor is twice the peak at TZ-37's ratio, rounded up; the gate's reads; the disk's floors
    ok(MEM_FLOOR == 2 * -(-PEAK_BOUND * 1199 // 1000) and DISK_GATE - DISK_FLOOR == 1300000000, "the floors' arithmetic")
    ok(memory_gate([MEM_FLOOR]) == (True, MEM_FLOOR) and memory_gate([MEM_FLOOR - 1] * 4 + [MEM_FLOOR]) ==
       (True, MEM_FLOOR) and memory_gate([MEM_FLOOR - 1] * 5) == (False, MEM_FLOOR - 1), "the memory gate's reads")
    # the test's constants
    ok(M0 == Fr(5, 6) and M1 == Fr(101, 120) and D_E == D_N == Fr(1, 60) and CAP_E == Fr(3, 5) and
       CAP_N == Fr(60, 19) and 1 - CAP_E * M0 == Fr(1, 2) and 1 - CAP_N * (1 - M1) == Fr(1, 2), "the bets' constants")
    ok(abs(threshold() - ST_LN400) < D("1e-55"), "ln 400")
    xs = [Fr((7 * k + 3) % 41, 41) if k % 5 else Fr(40, 41) for k in range(40)]
    ok(abs(bet_log(xs, M0, D_E, CAP_E, True) - ST_LKE) < D("1e-50"), "bet_log EARN against mpmath")
    ok(abs(bet_log(xs, M1, D_N, CAP_N, False) - ST_LKN) < D("1e-50"), "bet_log NO EARN against mpmath")
    hi_seq = [x_of(Fr(1, 10)) if k % 20 else x_of(Fr(-9, 10)) for k in range(2000)]     # mean y 0.05
    lo_seq = [x_of(Fr(1, 10)) if k % 8 else x_of(Fr(-9, 10)) for k in range(2000)]      # mean y -0.025
    mid_seq = [x_of(Fr(1, 10)) if k % 11 else x_of(Fr(-9, 10)) for k in range(2000)]    # mean y about 0.009
    got = [reading(bet_log(s, M0, D_E, CAP_E, True), bet_log(s, M1, D_N, CAP_N, False))
           for s in (hi_seq, lo_seq, mid_seq)]
    ok(got == ["EARN", "NO EARN", "UNDECIDABLE"], "readings %r" % got)
    ok(reading(threshold(), threshold()) == "EARN" and reading(threshold() - D("1e-50"), threshold()) == "NO EARN",
       "reading at the threshold")
    for y in (Fr(1, 5), Fr(-999999, 1000000)):
        ok(0 < x_of(y) <= 1, "x_of %s" % y)
    try:
        x_of(Fr(-1))
        ok(False, "x_of accepts -1")
    except AssertionError:
        ok(True, "x_of refuses -1")
    # the policy
    ok(policy("frame", "urllib.Request", (KALSHI + "/markets",)) is None and
       policy("draw", "urllib.Request", (DATA + "/v2/trades",)) is None and
       policy("score", "urllib.Request", (KALSHI + "/markets",)) is not None and
       policy("verify", "urllib.Request", ("https://github.com/x",)) is None and
       policy("frame", "urllib.Request", ("https://github.com/x",)) is not None, "requests by mode")
    ok(policy("frame", "open", ("/var/lib/btc-rewardbook/x", "r", 0)) is not None and
       policy("frame", "os.listdir", ("/etc/liq-guard",)) is not None and
       policy("frame", "open", ("/root/elsewhere", "w", 0)) is not None and
       policy("frame", "open", (WORK + "/run/x", "wb", 0)) is None and
       policy("reclaim", "open", (FORENSICS + "/x", "xb", 0)) is None and
       policy("reclaim", "open", (FORENSICS + "/x", "wb", 0)) is not None and
       policy("frame", "open", (PRIMARY + "/SYSTEM-MAP.md", "r", 0)) is None, "opens by mode")
    ok(policy("frame", "subprocess.Popen", ("git", ["git"])) is None and
       policy("frame", "subprocess.Popen", ("gh", ["gh"])) is not None and
       policy("frame", "subprocess.Popen", ("/bin/sh", ["/bin/sh"])) is not None, "processes")
    ok(retry_wait(1, "2.675") == 2.675 and retry_wait(3, None) == 8.0 and retry_wait(9, None) == 120.0 and
       retry_wait(1, "x") == 2.0, "retry_wait")
    ok(said(b'{"e": "bad 0xabcdef0123456789 3f1c2d3e-1111-2222-3333-444455556666"}').count("<") == 2, "said masks")
    # the kept replies: append, replay, a mismatch, a reply cut short, and the network after the replay
    sk = Sink(os.path.join(ST_ROOT, "s.jsonl.gz"))
    for i, (u, b) in enumerate((("https://api.elections.kalshi.com/a", b'{"x": 1}'),
                                ("https://api.elections.kalshi.com/b", b'{"x": 2}'))):
        sk.append(i, u, b)
    src = Source(sk)
    ok(src.json("https://api.elections.kalshi.com/a") == {"x": 1} and src.json("https://api.elections.kalshi.com/b")
       == {"x": 2}, "replay")
    try:
        Source(sk).get("https://api.elections.kalshi.com/z")
        ok(False, "a replay that answers another request")
    except AssertionError:
        ok(True, "replay refuses another request")
    try:
        s2 = Source(sk)
        s2.get("https://api.elections.kalshi.com/a")
        s2.get("https://api.elections.kalshi.com/b")
        s2.get("https://api.elections.kalshi.com/c")
        ok(False, "a replay past its replies with no network")
    except AssertionError:
        ok(True, "no network past the replies")
    with open(sk.path, "ab") as fh:
        fh.write(gz(b'{"cut short')[:9])
    fake = FakeNet({"https://api.elections.kalshi.com/c": b'{"x": 3}'})
    s3 = Source(sk, fake)
    ok(s3.kept == 2 and os.path.getsize(sk.path) == sk.lengths()[-1], "a reply cut short is cut off")
    ok([s3.json(u)["x"] for u in ("https://api.elections.kalshi.com/a", "https://api.elections.kalshi.com/b",
                                  "https://api.elections.kalshi.com/c")] == [1, 2, 3] and fake.asked ==
       ["https://api.elections.kalshi.com/c"] and len(sk.lengths()) == 3, "the network after the replay, kept")
    ok([u for u, _b in sk.records()] == ["https://api.elections.kalshi.com/" + c for c in "abc"], "three kept")
    # the trades' rules
    c = S0 * US
    t = lambda side, yes, at, block=False: {"ticker": "T", "is_block_trade": block, "created_time":
                                            time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(at // US)) +
                                            ".%06dZ" % (at % US), "taker_outcome_side": side,
                                            "yes_price_dollars": yes, "no_price_dollars": format(D(1) - D(yes), "f")}
    ok(kalshi_trade(t("yes", "0.8000", c - DAY * US), "T", c) == (True, Fr(4, 5), True), "0.80 at the hold's start")
    ok(kalshi_trade(t("yes", "0.8000", c - DAY * US - 1), "T", c) is None, "before the hold")
    ok(kalshi_trade(t("yes", "0.8500", c), "T", c) is None, "at the close")
    ok(kalshi_trade(t("no", "0.0501", c - 1), "T", c) == (False, Fr(9499, 10000), False), "no at 0.9499")
    ok(kalshi_trade(t("no", "0.0500", c - 1), "T", c) is None, "no at 0.95")
    ok(kalshi_trade(t("yes", "0.8500", c - 1, True), "T", c) is None, "a block trade")
    ok(kalshi_trade(t("yes", "0.8500", c - SLOW_S * US), "T", c) == (True, Fr(17, 20), False) and
       kalshi_trade(t("yes", "0.8500", c - SLOW_S * US - 1), "T", c) == (True, Fr(17, 20), True), "slow's edge")
    px = lambda oi, side, pr, ts: {"condition_id": "C", "token_id": "t%d" % oi, "outcome_index": oi, "side": side,
                                   "price": D(pr), "timestamp": ts}
    ok(poly_trade(px(1, "SELL", "0.12", S0 - 10), "C", S0 * US, ["t0", "t1"]) == (True, Fr(22, 25), False) and
       poly_trade(px(0, "SELL", "0.12", S0 - 400), "C", S0 * US, ["t0", "t1"]) == (False, Fr(22, 25), True) and
       poly_trade(px(0, "BUY", "0.95", S0 - 10), "C", S0 * US, ["t0", "t1"]) is None and
       poly_trade(px(0, "SELL", "0.2", S0 - 10), "C", S0 * US, ["t0", "t1"]) == (False, Fr(4, 5), False) and
       poly_trade(px(0, "BUY", "0.9", S0), "C", S0 * US, ["t0", "t1"]) is None, "Polymarket's acquisitions")
    try:
        poly_trade(px(0, "BUY", "0.9", S0 - 1), "C", S0 * US, ["t9", "t1"])
        ok(False, "a fill whose token is not its outcome's")
    except AssertionError:
        ok(True, "a fill's token checked")
    ok(poly_kappa({"feesEnabled": False}) == 0 and poly_kappa({"feesEnabled": True, "feeSchedule": {
        "exponent": 1, "rate": D("0.05"), "takerOnly": True}}) == Fr(1, 20) and poly_kappa({"feesEnabled": True,
        "feeSchedule": {"exponent": 2, "rate": D("0.05"), "takerOnly": True}}) is None and poly_kappa(
        {"feesEnabled": True, "feeSchedule": {"exponent": 1, "rate": D("0.2"), "takerOnly": True}}) is None, "fees")
    pm = _pm("0x" + "9" * 64, S0 + 1000, iso(S0 + DAY), ["1", "0"], ["27", "28"])
    ok(poly_class(pm, ST_DAYS, S0 + DAY)[1] is None and poly_class(pm, ST_DAYS, S0 + DAY - 1)[1] == "late" and
       poly_class(dict(pm, version="v2"), ST_DAYS, S0 + DAY)[1] == "version" and
       poly_class({k: v for k, v in pm.items() if k != "version"}, ST_DAYS, S0 + DAY)[1] == "version",
       "Polymarket's close by the instant and its protocol version")
    # G-REHEARSAL's agreement: twelve figures on the same kept replies, one apart, and other kept replies refused
    fig = {v: {"rows": 3, "keys": 2, "reasons": {"outside": 1}, "draws": 5, "digest": "ab", "gross": "1/2"}
           for v in VENUES}
    mine = {"files": {n: "0" for n in REH_FILES}, "venues": fig}
    other = json.loads(json.dumps(mine))
    other["venues"]["polymarket"]["digest"] = "cd"
    ok(agreement(mine, json.loads(json.dumps(mine)))[:2] == (12, 12) and agreement(mine, other)[:2] == (11, 12) and
       len(REH_FILES) == 8, "twelve figures compared, one apart found")
    try:
        agreement(mine, dict(other, files=dict(mine["files"], **{REH_FILES[0]: "1"})))
        ok(False, "the reference on other kept replies")
    except AssertionError:
        ok(True, "the reference on other kept replies refused")
    # the frame's sort index: its lines sorted as bytes are (key, id) sorted as text
    pairs = [("KXA", "KXA-10"), ("KX", "KX-9"), ("KXAB", "KXAB-1"), ("KXA", "KXA-1"), ("KXA", "KXA-1 "),
             ("series:é", "x"), ("series:e", "y"), ("KXA", "KXA-1!"), ("event:Z", "a")]
    idx = sorted(tsv(k, i, "%d" % n) for n, (k, i) in enumerate(pairs))
    ok([tuple(e.decode("utf-8").split("\t")[:2]) for e in idx] == sorted(pairs), "the sort index orders as text")
    sp = os.path.join(ST_ROOT, "lines")
    with open(sp, "wb") as fh:
        fh.writelines(idx[::-1] + idx[2:5])
    ok(list(sorted_lines(sp, 3)) == sorted(idx[::-1] + idx[2:5]) and
       [n for n in os.listdir(ST_ROOT) if n.startswith("lines.run-")] == [], "sorted on disk, its runs removed")
    try:
        tsv("KX\tA", "KXA-1")
        ok(False, "a key with a tab")
    except AssertionError:
        ok(True, "a key or id below a space refused")
    # a synthetic world on both venues: frames, draws, the score, and the same bytes again from the kept replies
    world = synthetic_world()
    want_frame = {"kalshi": (5, 4, {"outside": 2, "result": 1, "status": 1, "type": 1, "volume": 1}),
                  "polymarket": (4, 3, {"close": 1, "event": 1, "late": 1, "outside": 1, "result": 1, "shape": 1,
                                        "version": 1})}
    members_of = {"kalshi": {"KXA-26OCT28-T1", "KXA-26OCT28-T2"}, "polymarket": {"0x" + "1" * 64, "0x" + "b" * 64}}
    y_of = {"KXA-26OCT28-T1": (2 - Fr(255, 100) - Fr(7, 100) * Fr(3775, 10000)) / 3,
            "KXA-26OCT28-T2": (1 - Fr(171, 100) - Fr(7, 100) * (Fr(88, 100) * Fr(12, 100) + Fr(83, 100) *
                                                                  Fr(17, 100))) / 2,
            "0x" + "1" * 64: (3 - Fr(345, 100) - Fr(5, 100) * Fr(4667, 10000)) / 4,
            "0x" + "b" * 64: Fr(1, 10)}
    reason_of = {"KXE-26OCT28-T1": "fee_type", "KXF-26OCT28-T1": "fee_changed", "KXA-26OCT29-T1": "fee_event",
                 "0x" + "c" * 64: "fee", "0x" + "d" * 64: "no_trade"}
    for venue in VENUES:
        net = FakeNet(world)
        root = os.path.join(ST_ROOT, venue)
        os.makedirs(root)
        fpath = os.path.join(root, "frame.jsonl")
        rows, keys, reasons, _pages = build_frame(venue, ST_DAYS, Source(Sink(os.path.join(root, "rf.gz")), net),
                                                  fpath, ST_CLOSED_BY)
        ok((rows, keys, reasons) == want_frame[venue], "%s frame %r" % (venue, (rows, keys, reasons)))
        fx = FrameIndex(fpath)
        groups = [fx.group(i) for i in range(len(fx))]
        rowlists = [[fx.row(g[2] + i)["id"] for i in range(g[3])] for g in groups]
        fx.close()
        ok(all(rl == sorted(rl) for rl in rowlists) and [g[:2] for g in groups] == sorted(g[:2] for g in groups)
           and not os.path.exists(fpath + ".off"), "%s's rows sorted by day, key and id" % venue)
        g_max, p_max = GROUPS_MAX, dict(FRAME_PAGES_MAX)
        try:
            globals()["GROUPS_MAX"] = len(groups)
            fx = FrameIndex(fpath)
            fx.close()
            held = len(fx) == len(groups)
            globals()["GROUPS_MAX"] = len(groups) - 1
            try:
                FrameIndex(fpath)
                held = False
            except AssertionError as e:
                held = held and "series-days" in str(e)
            globals()["FRAME_PAGES_MAX"] = dict(p_max, **{venue: 1})
            try:
                build_frame(venue, ST_DAYS, Source(Sink(os.path.join(root, "rf.gz"))), os.path.join(root, "capped"),
                            ST_CLOSED_BY)
                held = False
            except AssertionError as e:
                held = held and "past 1 pages" in str(e)
        finally:
            globals()["GROUPS_MAX"], globals()["FRAME_PAGES_MAX"] = g_max, p_max
        ok(held, "%s's frame capped at its series-days and at its pages a day" % venue)
        sm = run_draws(venue, fpath, ST_DAYS, Source(Sink(os.path.join(root, "rd.gz")), net), "SELFTEST", 3, 60,
                       os.path.join(root, "draws.jsonl"))
        recs, members = read_draws(os.path.join(root, "draws.jsonl")), sm["members"]
        seq = _expected_draws("SELFTEST", venue, rowlists, 3, 60, members_of[venue])
        ok([(r["k"], r["id"]) for r in recs] == [(k, rowlists[gi][ri]) for k, gi, ri in seq] and members == 3,
           "%s's draw sequence" % venue)
        ok(all((r["reason"] is None) == (r["id"] in members_of[venue]) and
               (r["reason"] is None or r["reason"] == reason_of[r["id"]]) for r in recs), "%s reasons" % venue)
        ok(sm["draws"] == len(recs) and sm["digest"] == draws_digest(recs) and sm["markets"] == len(
            {r["id"] for r in recs}) and sm["sha256"] == sha256_file(os.path.join(root, "draws.jsonl")),
           "%s's draw summary" % venue)
        doc = score_venue(venue, fpath, os.path.join(root, "draws.jsonl"))
        ys = [y_of[r["id"]] for r in recs if r["reason"] is None]
        ok(doc["mean_y"] == fr_text(sum(ys, Fr(0)) / len(ys)) and doc["members"] == 3, "%s money %s" % (
            venue, doc["mean_y"]))
        fb = os.path.join(root, "frame-again.jsonl")
        build_frame(venue, ST_DAYS, Source(Sink(os.path.join(root, "rf.gz"))), fb, ST_CLOSED_BY)
        again = run_draws(venue, fb, ST_DAYS, Source(Sink(os.path.join(root, "rd.gz"))), "SELFTEST", 3, 60,
                          os.path.join(root, "draws-again.jsonl"))
        ok(sha256_file(fb) == sha256_file(fpath) and again == dict(sm, sha256=again["sha256"]) and
           again["sha256"] == sm["sha256"], "%s rebuilt from its kept replies" % venue)
    a1 = agg_new()
    for side_a, p, slow in ((True, Fr(85, 100), True), (False, Fr(9, 10), False), (True, Fr(4, 5), True)):
        agg_add(a1, side_a, p, slow)
    ok(agg_of(json.loads(json.dumps(agg_text(a1)))) == a1 and a1["n5"] == 2 and a1["q"] == Fr(3775, 10000),
       "the sums round-trip")
    ok(money(a1, True, Fr(7, 100)) == y_of["KXA-26OCT28-T1"] and gross(a1, False) == (1 - Fr(255, 100)) / 3,
       "money and gross")
    ok(gz(b"abc") == gz(b"abc") and gzip.decompress(gz(b"abc")) == b"abc", "fixed gzip bytes")
    gp, ba = os.path.join(ST_ROOT, "g.bin"), bytearray()
    for k in range(400000):
        ba += b"%d\n" % (k * k)
    blob, ba = bytes(ba), None
    with open(gp, "wb") as fh:
        fh.write(blob)
    s1, s2 = gz_file_once(gp, gp + ".gz"), gz_file_once(gp, gp + ".gz")
    with open(gp + ".gz", "rb") as fh:
        ok(len(blob) > 3 << 20 and fh.read() == gz(blob) and s1 == s2, "gzip a piece at a time: gz's bytes, twice")
    shutil.rmtree(ST_ROOT)
    ok(not os.path.exists(ST_ROOT), "the self-test's tree removed")
    out("SELFTEST PASS: %d of %d checks" % (checks[0], checks[0]))


if __name__ == "__main__":
    main(sys.argv[1:])
```

## Appendix B — `reference/tz56a-k0-reference.py`, byte for byte

Extracted by §0.1's script, staged and never committed; the block's content is the file.

```python file=reference/tz56a-k0-reference.py
#!/usr/bin/env python3
"""TZ-56a's reference: the Architect's own implementation of K0's frame, draw and money, written apart from
research/tz56-k0-favourite.py and sharing no code with it. It reads the rehearsal's kept replies under DIR - the
files the instrument's `rehearse` kept, each reply asserted whole by its own SHA-256 - looks every request it makes up
among them, makes no request of its own, and writes DIR/reference.json: for 2026-11-12, on each venue, the frame's
rows, its series-days and its other rows by reason, the draws to 60 members, the draws' label-free SHA-256 and the
members' money before the fee. A second run must write the same bytes.

    python -B tz56a-k0-reference.py /root/tz56a-work/rehearsal

Exit 0: written or unchanged. Any other exit: an assert failed, and its message names it.
Written for CryptoTZ/TZ-56a-k0-favourite.md, Appendix B.
"""
import calendar, collections, gzip, hashlib, json, os, sys, time, urllib.parse
from decimal import Decimal
from fractions import Fraction

if not __debug__:
    sys.exit("reference: refuses to run with asserts disabled (-O)")

ROOT = "/root/tz56a-work/rehearsal"
OUT = "reference.json"


def _guard(event, args):
    # no request of any kind, and no write but its own output
    if event.startswith("socket.") or event == "urllib.Request":
        raise RuntimeError("reference: %s refused" % event)
    if event == "open" and len(args) > 1 and isinstance(args[1], str) and set(args[1]) & set("wax+"):
        p = os.path.abspath(os.fsdecode(args[0]))
        if p not in (os.path.join(ROOT, OUT), os.path.join(ROOT, OUT) + ".tmp"):
            raise RuntimeError("reference: a write to %s refused" % p)


sys.addaudithook(_guard)

R0 = 1794441600                  # 2026-11-12 00:00:00 UTC, the rehearsal's day
DAYS = (R0,)
SALT = "TZ-56-K0-REHEARSAL"
NEED, DMAX = 60, 400
CUT = 1795737600                 # 2026-11-27 00:00:00 UTC: a Polymarket market closed after it is late
LO, HI = Fraction(80, 100), Fraction(95, 100)
HOLD, SLOW = 86400 * 1000000, 300 * 1000000
KB = "https://api.elections.kalshi.com/trade-api/v2"
GB = "https://gamma-api.polymarket.com"
DB = "https://data-api.polymarket.com"
FLOOR, TRIES = 157499106, 5      # MemAvailable at its start, read again every 60 s below it, five reads at most
VENUES = ("kalshi", "polymarket")
FILES = tuple("%s-%s.jsonl.gz%s" % (kind, v, ext) for v in VENUES for kind in ("raw-frame", "raw-draw")
              for ext in ("", ".idx"))


def meminfo():
    with open("/proc/meminfo") as fh:
        for ln in fh:
            if ln.startswith("MemAvailable:"):
                return int(ln.split()[1]) * 1024
    raise SystemExit("reference: no MemAvailable")


def sha_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for b in iter(lambda: fh.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def norm(url):
    u = urllib.parse.urlsplit(url)
    return u.scheme, u.netloc, u.path, tuple(sorted(urllib.parse.parse_qsl(u.query, keep_blank_values=True)))


class Kept:
    """Every kept reply under ROOT, by its request: the file and the byte range of its gzip member."""

    def __init__(self):
        self.where = {}
        for v in VENUES:
            for kind in ("raw-frame", "raw-draw"):
                path = os.path.join(ROOT, "%s-%s.jsonl.gz" % (kind, v))
                with open(path + ".idx") as fh:
                    ends = [int(x) for x in fh.read().split()]
                assert ends and ends[-1] == os.path.getsize(path), "reference: %s and its index differ" % path
                start = 0
                with open(path, "rb") as fh:
                    for i, end in enumerate(ends):
                        rec = self._rec(fh, start, end)
                        assert rec["i"] == i, "reference: %s: member %d is %d" % (path, i, rec["i"])
                        key = norm(rec["url"])
                        assert key not in self.where, "reference: %s requested twice" % rec["url"]
                        self.where[key] = (path, start, end)
                        start = end

    @staticmethod
    def _rec(fh, start, end):
        fh.seek(start)
        rec = json.loads(gzip.decompress(fh.read(end - start)))
        body = rec["body"].encode("utf-8")
        assert len(body) == rec["bytes"] and hashlib.sha256(body).hexdigest() == rec["sha256"], \
            "reference: a kept reply that is not whole: %s" % rec["url"]
        return rec

    def json(self, url):
        hit = self.where.get(norm(url))
        assert hit is not None, "reference: no kept reply for %s" % url
        path, start, end = hit
        with open(path, "rb") as fh:
            rec = self._rec(fh, start, end)
        return json.loads(rec["body"], parse_float=Decimal)


def t_us(s):
    s = s.strip().replace("T", " ")
    if s[-1] == "Z":
        s = s[:-1]
    for suf in ("+00:00:00", "+00:00", "+00"):
        if s.endswith(suf):
            s = s[:-len(suf)]
            break
    whole, _, frac = s.partition(".")
    return calendar.timegm(time.strptime(whole, "%Y-%m-%d %H:%M:%S")) * 1000000 + int((frac + "000000")[:6] or 0)


def iso(t):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(t))


def pick(salt, venue, k, stage, n):
    return int(hashlib.sha256(("%s|%s|%d|%d" % (salt, venue, k, stage)).encode()).hexdigest(), 16) % n


def agg_new():
    return {"n": 0, "na": 0, "nb": 0, "sa": Fraction(0), "sb": Fraction(0), "q": Fraction(0)}


def agg_add(a, is_a, p):
    a["n"] += 1
    if is_a:
        a["na"] += 1
        a["sa"] += p
    else:
        a["nb"] += 1
        a["sb"] += p
    a["q"] += p * (1 - p)


def kalshi_frame(kept):
    seen, rows, why = set(), [], collections.Counter()
    for d in DAYS:
        cur = None
        while True:
            q = [("limit", 1000), ("min_close_ts", d - 3600), ("max_close_ts", d + 86400 + 3600),
                 ("mve_filter", "exclude")] + ([("cursor", cur)] if cur else [])
            j = kept.json(KB + "/markets?" + urllib.parse.urlencode(q))
            for m in j["markets"]:
                if m["ticker"] in seen:
                    continue
                seen.add(m["ticker"])
                c = t_us(m["close_time"])
                dd = [x for x in DAYS if x * 1000000 <= c < (x + 86400) * 1000000]
                if not dd:
                    why["outside"] += 1
                elif m["market_type"] != "binary":
                    why["type"] += 1
                elif m["status"] != "finalized":
                    why["status"] += 1
                elif m["result"] not in ("yes", "no"):
                    why["result"] += 1
                elif not Decimal(m["volume_fp"]) > 0:
                    why["volume"] += 1
                else:
                    rows.append((dd[0], m["event_ticker"].split("-")[0], m["ticker"], m["event_ticker"], c,
                                 m["result"]))
            cur = j.get("cursor") or None
            if not cur:
                break
    return rows, why


def poly_frame(kept):
    seen, rows, why = set(), [], collections.Counter()
    for d in DAYS:
        cur = None
        while True:
            q = [("limit", 100), ("closed", "true"), ("end_date_min", iso(d - 3600)),
                 ("end_date_max", iso(d + 86400 + 3600))] + ([("after_cursor", cur)] if cur else [])
            j = kept.json(GB + "/markets/keyset?" + urllib.parse.urlencode(q))
            for m in j["markets"]:
                if m["conditionId"] in seen:
                    continue
                seen.add(m["conditionId"])
                ct = m.get("closedTime")
                if ct and t_us(ct) > CUT * 1000000:
                    why["late"] += 1
                    continue
                if m.get("version") != "v1":
                    why["version"] += 1
                    continue
                e = t_us(m["endDate"])
                dd = [x for x in DAYS if x * 1000000 <= e < (x + 86400) * 1000000]
                if not dd:
                    why["outside"] += 1
                    continue
                o, tk = json.loads(m.get("outcomes") or "[]"), json.loads(m.get("clobTokenIds") or "[]")
                if len(o) != 2 or len(tk) != 2:
                    why["shape"] += 1
                    continue
                op = json.loads(m.get("outcomePrices") or "[]")
                if op not in (["1", "0"], ["0", "1"]):
                    why["result"] += 1
                    continue
                if not m.get("closedTime"):
                    why["close"] += 1
                    continue
                ev = m.get("events") or []
                if not ev:
                    why["event"] += 1
                    continue
                ser = ev[0].get("series") or []
                key = ("series:" + ser[0]["slug"]) if ser else ("event:" + ev[0]["slug"])
                fs = m.get("feeSchedule")
                if m.get("feesEnabled") is False:
                    kap = Fraction(0)
                elif (m.get("feesEnabled") is True and isinstance(fs, dict) and fs.get("exponent") == 1 and
                      fs.get("takerOnly") is True and 0 <= Fraction(str(fs.get("rate"))) <= Fraction(14, 100)):
                    kap = Fraction(str(fs["rate"]))
                else:
                    kap = None
                rows.append((dd[0], key, m["conditionId"], t_us(m["closedTime"]), "A" if op[0] == "1" else "B",
                             tuple(tk), kap))
            cur = j.get("next_cursor") or None
            if not cur:
                break
    return rows, why


def grouped(rows):
    groups = collections.defaultdict(list)
    for r in rows:
        groups[(r[0], r[1])].append(r)
    keys = sorted(groups)
    for k in keys:
        groups[k].sort(key=lambda r: r[2])
    return groups, keys


def kalshi_draws(kept, rows):
    groups, keys = grouped(rows)
    kept.json(KB + "/historical/cutoff")
    sfc = kept.json(KB + "/series/fee_changes?" + urllib.parse.urlencode([("show_historical", "true")]))
    sfc = sfc["series_fee_change_arr"]
    efc, cur = [], None
    while True:
        j = kept.json(KB + "/events/fee_changes?" + urllib.parse.urlencode([("limit", 1000)] +
                                                                           ([("cursor", cur)] if cur else [])))
        efc += j["event_fee_changes"]
        cur = j.get("cursor") or None
        if not cur:
            break
    lo, hi = (DAYS[0] - 86400) * 1000000, (DAYS[-1] + 2 * 86400) * 1000000
    sers, res, out, members = {}, {}, [], 0
    for k in range(DMAX):
        if members == NEED:
            break
        g = keys[pick(SALT, "kalshi", k, 1, len(keys))]
        r = groups[g][pick(SALT, "kalshi", k, 2, len(groups[g]))]
        tick = r[2]
        if tick not in res:
            key = r[1]
            if key not in sers:
                s = kept.json(KB + "/series/" + urllib.parse.quote(key, safe=""))["series"]
                assert s["ticker"] == key
                sers[key] = s
            s, reason, a = sers[key], None, agg_new()
            if s["fee_type"] not in ("quadratic", "quadratic_with_maker_fees", "quadratic_with_combo_maker_fees"):
                reason = "fee_type"
            elif any(x["series_ticker"] == key and lo <= t_us(x["scheduled_ts"]) < hi for x in sfc):
                reason = "fee_changed"
            elif any(x["event_ticker"] == r[3] for x in efc):
                reason = "fee_event"
            if reason is None:
                c, cur, ids = r[4], None, set()
                cs = c // 1000000
                while True:
                    q = [("ticker", tick), ("limit", 1000), ("min_ts", cs - 86401), ("max_ts", cs + 1)]
                    j = kept.json(KB + "/markets/trades?" + urllib.parse.urlencode(q + ([("cursor", cur)] if cur
                                                                                       else [])))
                    for t in j["trades"]:
                        assert t["ticker"] == tick and t["trade_id"] not in ids
                        ids.add(t["trade_id"])
                        if t["is_block_trade"]:
                            continue
                        ts = t_us(t["created_time"])
                        if not (c - HOLD <= ts < c):
                            continue
                        side = t["taker_outcome_side"]
                        p = Fraction(t["yes_price_dollars"] if side == "yes" else t["no_price_dollars"])
                        if LO <= p < HI:
                            agg_add(a, side == "yes", p)
                    cur = j.get("cursor") or None
                    if not cur:
                        break
                if a["n"] == 0:
                    reason = "no_trade"
            res[tick] = (reason, a)
        reason, a = res[tick]
        out.append((k, g[0], g[1], tick, reason, a, r[5]))
        members += reason is None
    return out, len(keys)


def poly_draws(kept, rows):
    groups, keys = grouped(rows)
    res, out, members = {}, [], 0
    for k in range(DMAX):
        if members == NEED:
            break
        g = keys[pick(SALT, "polymarket", k, 1, len(keys))]
        r = groups[g][pick(SALT, "polymarket", k, 2, len(groups[g]))]
        cid = r[2]
        if cid not in res:
            a, reason = agg_new(), (None if r[6] is not None else "fee")
            if reason is None:
                c, cur, last = r[3], None, None
                while True:
                    q = [("condition", cid), ("taker_only", "true"), ("limit", 1000)]
                    j = kept.json(DB + "/v2/trades?" + urllib.parse.urlencode(q + ([("cursor", cur)] if cur else [])))
                    fills = j["data"]
                    for x in fills:
                        assert x["condition_id"] == cid
                        tsv = int(x["timestamp"])
                        assert last is None or tsv <= last
                        last = tsv
                        oi = int(x["outcome_index"])
                        assert str(x["token_id"]) == r[5][oi]
                        ts = tsv * 1000000
                        if not (c - HOLD <= ts < c):
                            continue
                        pr = Fraction(str(x["price"]))
                        if x["side"] == "BUY":
                            is_a, p = oi == 0, pr
                        else:
                            assert x["side"] == "SELL"
                            is_a, p = oi == 1, 1 - pr
                        if LO <= p < HI:
                            agg_add(a, is_a, p)
                    cur = (j.get("pagination") or {}).get("next_cursor")
                    if not cur or not fills or int(fills[-1]["timestamp"]) * 1000000 < c - HOLD:
                        break
                if a["n"] == 0:
                    reason = "no_trade"
            res[cid] = (reason, a)
        reason, a = res[cid]
        out.append((k, g[0], g[1], cid, reason, a, r[4]))
        members += reason is None
    return out, len(keys)


def fr(x):
    x = Fraction(x)
    return "%d/%d" % (x.numerator, x.denominator)


def figures(rows, why, out, nkeys, a_wins):
    h, tot = hashlib.sha256(), Fraction(0)
    for (k, day, key, mid, reason, a, label) in out:
        h.update(("%d|%d|%s|%s|%s|%d|%d|%d|%s|%s|%s\n" % (k, day, key, mid, reason or "member", a["n"], a["na"],
                                                         a["nb"], fr(a["sa"]), fr(a["sb"]), fr(a["q"]))).encode())
        if reason is None:
            tot += ((a["na"] if label == a_wins else a["nb"]) - a["sa"] - a["sb"]) / a["n"]
    return {"rows": len(rows), "keys": nkeys, "reasons": dict(sorted(why.items())), "draws": len(out),
            "digest": h.hexdigest(), "gross": fr(tot)}


def main(argv):
    assert len(argv) == 1 and os.path.abspath(argv[0]) == ROOT, "usage: tz56a-k0-reference.py %s" % ROOT
    reads = [meminfo()]
    while reads[-1] < FLOOR and len(reads) < TRIES:
        time.sleep(60)
        reads.append(meminfo())
    print("reference: MemAvailable %s bytes, floor %d" % (reads, FLOOR))
    assert reads[-1] >= FLOOR, "reference: BLOCKED: MemAvailable below %d at every read" % FLOOR
    kept = Kept()
    print("reference: %d kept replies indexed" % len(kept.where))
    venues = {}
    rows, why = kalshi_frame(kept)
    out, nkeys = kalshi_draws(kept, rows)
    venues["kalshi"] = figures(rows, why, out, nkeys, "yes")
    rows = why = out = None
    rows, why = poly_frame(kept)
    out, nkeys = poly_draws(kept, rows)
    venues["polymarket"] = figures(rows, why, out, nkeys, "A")
    doc = {"files": {n: sha_file(os.path.join(ROOT, n)) for n in FILES}, "venues": venues}
    data = json.dumps(doc, sort_keys=True, indent=1).encode("utf-8") + b"\n"
    path = os.path.join(ROOT, OUT)
    for v in VENUES:
        for k in ("rows", "keys", "reasons", "draws", "digest", "gross"):
            print("reference: %s %-8s %s" % (v, k, venues[v][k]))
    if os.path.exists(path):
        with open(path, "rb") as fh:
            assert fh.read() == data, "reference: DETERMINISM: %s differs from the first run" % path
        print("reference: unchanged %s sha256 %s" % (path, hashlib.sha256(data).hexdigest()))
    else:
        with open(path + ".tmp", "wb") as fh:
            fh.write(data)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(path + ".tmp", path)
        print("reference: wrote %s sha256 %s" % (path, hashlib.sha256(data).hexdigest()))
    import resource
    print("reference: peak memory %d bytes" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024))


if __name__ == "__main__":
    main(sys.argv[1:])
```
