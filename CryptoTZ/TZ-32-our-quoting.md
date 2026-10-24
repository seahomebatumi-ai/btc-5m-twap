# TZ-32 — W1, our quoting: does a quote of ours, simulated on the pair book's streams with queue position, the taker delay and our own cancels, keep the named makers' edge?

**Canonical filename:** `TZ-32-our-quoting.md`. The committed file takes this name and no other.

**Executor model: Opus.** A replay at venue time of stored streams, a gate's arithmetic, and the first label read of a
set no one has scored.

**Required System Map revision:** `2026-10-23-a`.

**Required anchors**, from map §0. A mismatch on any one is BLOCKED before any work:

| anchor | required |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `0f6c90451cbd` |
| `A6` — pricer | `729f0bcdbee3` |

**Host gate:** §0.3. This TZ runs on the capture host for its interpreter, its network, the pair book's `window.json`
files, the archive's ledger and the forensic store; it reads no stream stored on the host — every stream it replays is
a Release asset the archive made.

**When:** §3.6 and everything after it **no earlier than 2026-10-27 03:20:00 UTC**, epoch `1793071200`: §3.6's first
command waits for that instant in its own text, and `fetch` then waits for the archive's ledger to reach the last
candidate, `1793068200`, re-reading it every 60 s and stopping BLOCKED at 2026-10-27 06:00:00 UTC (§1). The archive's
calendar run of 2026-10-27 03:00:20 UTC is the first that moves that window. Everything before §3.6 may run earlier. At
most about `6,000` s of wall clock from §3.6 on at §6's bounds, most of it the replay held to the pair book's idle
stretch; an archive that has not moved the last candidate by 06:00:00 UTC stops `fetch` BLOCKED there, `9,600` s after
§3.6's instant.

**What this TZ is.** The W track's second step, W1 (CANON PART II). W0 read W-EARN (TZ-31): the ten makers named on
M0's last 864 markets kept `0.828` c a share on 1,008 markets whose fills no one had read — `0.747` c on the 336 of them
that are the pair book's five-minute legs. Whether a quote of ours keeps any of it — behind theirs in the queue, met by
the same takers, cancelled no faster — is W1's question. This TZ fixes **one quoting rule** (§1): a bid and an ask of
five shares at the five-minute leg's touch, from `T0` to `T0 + 295`, each replaced when the touch moves, a position cap
of twenty shares. It replays that rule, label-free, on the pair book's stored streams of **the first 288 qualifying
windows from `1792754100`**, whose five-minute legs open after `1792753800`, W0's last member — streams no one has
read — at venue time: the leg's book rebuilt from every stored frame and checked against the venue's own book frame at
every match, every order arriving one way latency after the host decides it, refused where it would cross, queued at
its level, filled only by matches the venue printed or by the orders that would have crossed it once the 150 ms taker
delay has passed, and cancelled by our own messages. It reads W1 once, by TZ-23's thresholds: **W1-EARN** on the
variant that makes every unmeasurable assumption against us, **W1-NO-EARN** on the variant that makes every one for us,
**UNDECIDABLE** otherwise, each answer's false-reading probability at most `0.005`. The instrument,
`research/tz32-our-quoting.py` (Appendix A), loads TZ-23's file by its bytes for the documents, every position, cost
and rebate, the thresholds, the power, the reading and the labels; its own code is the replay, the set rule over
`window.json` and the archive's record, the downloads held to the pair book's idle stretch, and the modes.

---

## 0. Gates

### 0.0 The work tree, first

After contract §1 steps 1 and 2, and before anything else:

```
mkdir /root/tz32-work /root/tz32-work/logs; echo "exit=$?"
```

`exit=0` proves neither existed; anything else is BLOCKED. **From here every command's output goes to
`/root/tz32-work/logs/`, one file per step, §0's included**, and nothing to the session's scratchpad. The one exception
is B-RECLAIM-OWN, §9.

### 0.1 The instrument, staged

Extract Appendix A from this TZ as the primary checkout carries it after contract §1's pull, with this script, verbatim,
its one argument the destination:

```
/root/tz04a-env/venv/bin/python -B - /root/tz32-work/stage <<'EOF'
import hashlib, os, sys
SRC = "/root/btc-5m-twap/CryptoTZ/TZ-32-our-quoting.md"
DEST = sys.argv[1]
WANT = {
    "research/tz32-our-quoting.py": "6ec367e6ed995b315063d2d808dd6a3995878011afd76abfbb7b106b645a9c61",
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
| `research/tz32-our-quoting.py` | 2,576 | 138,209 | `6ec367e6ed995b315063d2d808dd6a3995878011afd76abfbb7b106b645a9c61` |

Then the instrument's one dependency beside it, TZ-23's file as `main` carries it:

```
install -m 0644 /root/btc-5m-twap/research/tz23-maker-m0.py /root/tz32-work/stage/research/; echo "exit=$?"
sha256sum /root/tz32-work/stage/research/tz23-maker-m0.py
```

which must print `6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f` — map §0's row; the instrument
asserts it again each time it loads the file (Appendix A lines 66 to 78). A failed assert or another hash is BLOCKED.
The staged copy runs §0.2's `fingerprint` alone, written **`I0`**:
`nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz32-work/stage/research/tz32-our-quoting.py`, run from
`/root/tz32-work` — every mode asserts that its current directory is the work tree (line 2556).

### 0.2 Fingerprint

`I0 fingerprint` performs contract §1 steps 3 and 4 inside the instrument and asserts them, against `SYSTEM-MAP.md` and
the files of its §0 table in the primary checkout `/root/btc-5m-twap`: revision `2026-10-23-a`; the six anchors; `A2`,
`A4`, `A5` and `A6` re-derived as the first 12 hex characters of those files' SHA-256; the table's **43** rows, each
printed in lines, bytes and SHA-256 — **40** `frozen` rows asserted equal to the map, **2** `tracked` and **1**
`reported`; TZ-23's file a `frozen` row and the primary checkout's copy of it `6b3ace2c…`; and the map's own lines,
bytes and SHA-256 (lines 1518 to 1551). It prints `FINGERPRINT PASS` or stops at the first mismatch, which is BLOCKED.

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
stat -c '%s %n' /var/lib/btc-pairbook-archive/ledger.jsonl
TZ=UTC systemctl show btc-recorder.service btc-pairbook.service btc-pairbook-archive.service btc-pairbook-archive.timer btc-chainbook.service crypto-deploy.service crypto-announce.service -p Id -p MainPID -p NRestarts -p ActiveState -p SubState -p UnitFileState -p ActiveEnterTimestamp -p Result
TZ=UTC systemctl list-timers btc-pairbook-archive.timer apt-daily-upgrade.timer apt-daily.timer --all --no-pager
journalctl -u btc-pairbook-archive.timer -o short-iso --since 2026-10-22 --no-pager
journalctl _PID=1 -o short-iso --since 2026-10-22 --no-pager | grep -E 'Reload|btc-pairbook|btc-recorder' | tail -n 80
grep -E '^(Start-Date|Commandline|Upgrade|End-Date)' /var/log/apt/history.log | tail -n 40
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
systemctl is-active telemetry-watch.service; echo "exit=$?"
git -C /root/btc-recorder-svc rev-parse HEAD
cat /root/btc-pairbook-svc/commit.txt /root/btc-pairbook-archive-svc/commit.txt
for d in /root/tz31-work /root/tz18a-svc /root/btc-recorder-svc /root/btc-pairbook-svc /root/btc-pairbook-archive-svc /var/lib/btc-pairbook-archive; do test -e "$d"; echo "$d exit=$?"; done
find /root/btc-forensics -type f | wc -l
git worktree list
du -sb /var/lib/btc-pairbook /var/lib/btc-pairbook-archive /root/.claude /root/PROJECT_GAMING_PS5
echo "$S"; ls -la "$(dirname "$(dirname "$S")")"
```

- **H1** — `find` prints exactly one path.
- **H2** — `df` names source `/dev/vda2` and size `31612203008`; `grep -c` prints at least `1`. With H1 this is map §6's
  host identity.
- **H3** — the interpreter prints `3.12.`.
- **H4** — the forensic store this TZ reads and writes is the host's: `stat` and `sha256sum` print `16570` bytes and
  `ec71b1a7ce7db37ff29a49156006541dd5729c1df2c829c481eb64181228e4dd` — TZ-27's `set.json`, copied there by TZ-27's §9,
  asserted by TZ-30's and TZ-31's host gates, and the rehearsal's list of TZ-27's 51 assets (§4.1).
- **Memory gate** — `MemAvailable` at least `81,928,192` bytes (§0.4).
- **Disk gate** — `avail` at least `5,400,000,000` bytes (§0.4).

Any of these six failing is BLOCKED. **The rest is printed and carries no threshold:** the boots; the archive's ledger's
size; the seven units — this TZ needs none of them running: it reads the pair book's `window.json` files and the
archive's ledger and Releases, G-STILL reads the recorder and the pair book (§4.6), and the hold reads the archive's
service; the timers, among them the package manager's, whose runs restarted both capture units on 2026-10-22 and
2026-10-23 (map §6, process supervision); the archive timer's journal, systemd's reload and restart records and the
package history, beside which §3.4 reads the archive's runs off its calendar (map §7 item 115);
`telemetry-watch.service`'s two states, on which map §6's headroom is conditional; the three code trees' commits,
`e3975b5…`, `e8b46a8…` and `d8194fd…` by map §3; `/root/tz31-work` absent and the code and state trees present, by map
§3; the forensic store's count, map §3's `1,997`; the worktrees, map §3's two; `du` of the pair book's store beside
`df`, as map §2.5 asks, and of the archive's state; and the listing of the directory that holds the session's own, whose
UUID directories `I scratch` names live or earlier (§9).

### 0.4 Resource floors, in exact bytes

**Disk.** `/dev/vda2` free at least **`5,400,000,000`** bytes: the pair book's `STREAM_FLOOR`, `4,500,000,000`
(`research/tz26-nesting-b3-capture.py` line 132), below which no stream opens for a window, plus `900,000,000` for this
session — so nothing this TZ writes can stop the pair book's capture. **Every unit re-reads free space before its
download and stops BLOCKED where the download would leave less than `5,400,000,000`** (lines 1239 to 1272). The
session's peak is its tree and §9's copies together, about `435,000,000` bytes at the bound (§6): the replay's units and
their concatenation, about `60,200,000` each, one window's files at the pair book's cut, at most `200,000,000`, the
rehearsal's tree, the rescore's, the set, the logs, the stage and the worktree, and §9's copies of what the report
names. The allowance is that peak twice over, rounded up (map §6, disk).

**Memory.** `MemAvailable` at least **`81,928,192`** bytes: twice the largest peak of any mode in the Architect's runs
of this instrument under Python 3.12.3 (map §7 item 97's rule) — `rehearse`'s `40,964,096` over TZ-27's 51 windows at
02:51 UTC on 2026-10-24, under an earlier text of the same replay; with these bytes `rescore` `40,423,424`, `replay`
`40,157,184` over the stand-in's 48 windows and `32,890,880` again, `rehearse` `36,417,536`, `score` `32,927,744`,
`selftest` `31,637,504` and `fetch` `31,617,024` (map §6, memory). A replay holds one window's books and orders at a
time and reads its stream files line by line, so the peak does not grow with the set. Every mode that reads the venue,
the archive's Releases or a set — `rehearse`, `fetch`, `replay`, `rescore` and `score` — re-reads `MemAvailable` and
free space at its start and stops BLOCKED below either floor, and asserts that glibc took TZ-23's mmap threshold and
arena count (lines 353 to 360). Map §6 records the host: `1,002,127,360` bytes in all, one processor; TZ-31 read
`271,716,352` bytes available at its host gate with its session open. Every mode runs under `nice -n 19`.

### 0.5 Refs

`git ls-remote origin` before §3.1's push, every ref reported. Map §1 records, read on 2026-10-24 at 02:39 UTC,
`main` at `7e08b7996a3504a88536e7a9cfcf3c48083c7837`, PR #30's merge, nine branches, twenty-one tags —
`tz-01a-dataset` and `tz-27-pairbook-streams`, annotated, and nineteen lightweight `pairbook-streams-*` — and **63** ref
lines; every later run of the archive adds one tag — **67** after its calendar runs of 2026-10-24 to 2026-10-27, and
one more for each run off the calendar. The upload that carries revision `2026-10-23-a` and this TZ sits above
`7e08b79`, in one commit or more; every commit on `main`'s first-parent line above it is reported with the paths it
changed. A difference is recorded, not BLOCKING, unless `main` does not carry revision `2026-10-23-a` or
`refs/heads/tz-32-our-quoting` already exists — either is BLOCKED.

---

## 1. Why this TZ exists

Line numbers here are Appendix A's unless a file is named; `tz23` is `research/tz23-maker-m0.py` at `7e08b79`.

**The question** — CANON PART II, the W track's W1: does our quoting, simulated on the pair book's streams with queue
position, the taker delay and our own cancels, keep the named makers' edge? **W0 answered who earns, not whether we
would** (map §4, §5): the ten makers named on the formation kept `26,777.413` USDC on `3,233,296.886` shares of W0's
1,008 markets, `0.828` c a share — `0.590` c at settlement and `0.238` c of rebate — and `0.747` c a share on the 336
markets that are the pair book's five-minute legs, `T0 ≡ 600` modulo 900. Their quotes are theirs: where they rest in
the queue, which takers meet them, how fast they move away from a stale price. B3 found the stale side of the book gone,
on one leg at least, before a taker's order matched (TZ-30). A quote of ours would rest behind theirs, be met by the
same takers and cancel through the same latency; W1 asks what that leaves.

**The quoting rule, ours, fixed here before any stream of the set has been read.** On the five-minute leg of a
window — the market `btc-updown-5m-{T+600}`, `T0 = T + 600` — on the host's clock from `T0` to `T0 + 295`:

1. **Where:** a bid at the leg's best bid and an ask at its best ask, as the host's rebuilt book stands after each frame
   of the leg's market it receives — joining the touch, never improving it — each **five shares**, the venue's minimum
   order, which every member's document must state (`orderMinSize` `5`). In Up shares: a bid buys Up at `p`; an ask
   sells Up at `p`, the same order as buying Down at `1 − p`, since the venue's book for Up holds every order on both
   tokens.
2. **When not:** no quote on a side while either best is missing or the touch's price is outside `[0.05, 0.95]`; no bid
   while the position the host knows of is `+20` shares or more, no ask while it is `−20` or less; a live quote whose
   target is gone is cancelled.
3. **Replace:** a live quote whose price is no longer the target is cancelled and a new one sent at the target, the same
   instant, without waiting for the cancel's acknowledgement. A quote the host has learned is filled, cancelled or
   refused is replaced at the next frame of the leg.
4. **Post-only:** an order that would cross when it arrives — a bid at or above the venue's best ask then, an ask at or
   below its best bid — is refused, as the venue refuses a post-only order that would match.
5. **Stop:** at `T0 + 295` on the host's clock every live quote is cancelled, and none is sent after it. A disconnect of
   the stream, and the end of each stream file, cancel every live quote at the host's instant.

**The replay, at venue time** (lines 639 to 1102). The streams are the pair book's own files, every frame one line with
its host receipt `recv_ns` and the venue's frame verbatim (map §2.5); the replay reads them in the order stored and
keeps the leg's market alone. The host's clock is each line's `recv_ns`; the venue's is each frame's `timestamp`, in
milliseconds.

- **Latency:** a message the host sends at host instant `h` reaches the venue at `h + L`, `L = 50` ms one way, as B3's
  replay took it (TZ-30); the host learns of a fill, a refusal or a cancel's effect `L` after the venue makes it. A
  message due at the venue at `τ` takes effect before every frame stamped after `τ` and after every frame stamped at or
  before it.
- **The book:** the leg's Up book, seeded by the subscription's book frame and moved by every `price_change` entry of
  the Up token — a size of zero removes the level; every other book frame of the Up token replaces it, after its touch
  and every level are compared with the book rebuilt to it (G-BOOK, §4.3). Prices are integers of thousandths and sizes
  of hundredths, read exactly from the venue's text (lines 653 to 674).
- **A match:** the entries of the Up token that share one venue stamp form a block. **A block that the Up token's own
  book frame with the same stamp closes is a match**, and any other block is not: on TZ-27's 51 windows, `67,413` of
  the `68,574` matches so read have a `last_trade_price` frame of the leg within 50 ms, and `67,688` of its `68,628`
  such frames a match within 50 ms. In a match, a side is hit where its best level at the block's start decreased; its
  consumption runs from that level outward, each level's decrease within the block, while every level before it was
  emptied (lines 784 to 810).
- **A fill at a match:** a resting order of ours on the hit side fills where the sweep reaches its price, for
  `min(its remaining size, max(0, T − Q))`, `T` the consumption at its price and beyond it and `Q` the size queued ahead
  of it — the taker's order, had ours been there, would have met ours before the levels beyond it. Then `Q` falls by
  the consumption at its price. Our order is five shares in a book of hundreds, and the book is not changed by it.
- **The queue:** an order arriving at a level joins behind the size displayed there then, `Q` that size; where the level
  later shrinks with no trade, `Q` is held at most at the level's size — every departure from behind ours first
  (lines 752 to 782 and 833 to 885).
- **A crossing order — the taker delay.** Where the book's opposite side comes to our resting order's price with no
  trade — a bid of ours at `p` alone at its level, and an ask arriving at `p` or below — that ask, had ours been there,
  would have been a taker against ours. The venue holds a marketable order on these markets **150 ms** before it
  matches, and a held order cannot be cancelled (CANON §1.1; the venue's order lifecycle). So the replay counts one
  crossing event at the frame's stamp plus 150 ms, for the opposite side's displayed size at prices crossing ours; where
  our order still rests then — our cancel not yet arrived — it fills, for what is left of it (lines 812 to 831 and 752
  to 782).
- **The variants.** Two quantities a stored stream cannot show — where in the queue our order stands, and whether an
  order that would have crossed ours was a taker or a post-only order the venue would have refused — are bracketed.
  Every variant replays the same quotes on the same frames (lines 113 to 116 and 687 to 721):

| variant | latency | queue | departures | crossing orders | role |
|---|---|---|---|---|---|
| **`behind`** | 50 ms | behind the displayed size | from behind ours first | takers after 150 ms | **gated: W1-EARN** — every assumption against us |
| **`front`** | 50 ms | first at its level | — | refused, never takers | **gated: W1-NO-EARN** — every assumption for us |
| `prop` | 50 ms | behind | in proportion to the size ahead and behind | takers | barred |
| `behind_nocross` | 50 ms | behind | from behind first | refused | barred |
| `front_cross` | 50 ms | first | — | takers | barred |
| `L0`, `L100`, `L250` | 0, 100, 250 ms | behind | from behind first | takers | barred |
| `front_L0` | 0 ms | first | — | refused | barred |

**Money, by TZ-23's own arithmetic** (lines 1106 to 1137). A fill of our bid is a taker's sale of Up into it, a fill of
our ask a taker's purchase; with the taker's side so written, TZ-23's `aggregate` gives our own position — `+s` Up at
`p` for a filled bid, `−s` at `p` for a filled ask — its cost `C`, and the rebate `R = 0.014 · s · p · (1 − p)` at the
fill's price (tz23 lines 316 to 360). A member's money at settlement is `X · up − C + R`, over every fill before
`T0 + 300`; a fill outside `[T0, T0 + 300)` is a failed assert. **The self-test proves it against fill-by-fill
arithmetic written apart from TZ-23's** — `s (up − p)` for a bid, `s (p − up)` for an ask, each with its rebate — at
either outcome, and over a synthetic set end to end (lines 2090 to 2549).

**The set.** The candidates are the 350 windows **`1792754100` … `1793068200`**, 2026-10-23 11:15 UTC to 2026-10-27
02:30 UTC, in steps of 900. A candidate is a **member** where its `window.json` shows a stream opened, not cut, not
stopped, not joined late, subscribed by `T + 600`, its last frame at or after `T + 900`, no gap between frames above
15 s, and every one of its files in the archive's Release assets — TZ-30's stream rule (lines 529 to 553) — and its
leg's settled document passes TZ-23's `qualify`, unchanged, states `orderMinSize` `5`, and carries the condition and
the two tokens `window.json` carries for the leg (lines 556 to 584). **The members are the first 288**, walked in order:
`window.json` of every candidate first, then the documents of the stream rule's survivors in requests of twenty by
TZ-23's `gamma_docs`, each held to the idle stretch, and no request after the 288th member. **The walk stops BLOCKED
past 62 non-members** before the 288th member — TZ-30's B3 set had 7 in 775 — and at 288 members if every candidate
qualifies the set runs to `1793012400`, 2026-10-26 11:00 UTC, its member list's SHA-256
`3ec41ed926dd72965f11d66eecd59b3474baa7ada6e7ef2381e37e7e616b93dd` — 51 legs on Friday, 96 on Saturday, 96 on Sunday
and 45 on Monday — recorded and asserted by nothing. 288 windows are three days; the power below.

**The test**, TZ-23's (its §1, "The test"), on each gated variant's own sum. Order the members by `T` and let `G_m` be
everything public before `T0_m + 300`. A variant's `X_m`, `C_m` and `R_m` are functions of the leg's stream before
`T0_m + 300`, known at `G_m`, and `up_m`, fixed by the reading at `T0_m + 300`, is known at `G_(m+1)`; so `D_m = X_m
(up_m − q_m)`, `q_m` the probability of Up given `G_m`, are martingale differences, each in an interval of length
`|X_m|`, and `exp(λ M_n − λ² V_n / 8)` is a supermartingale whose probability of ever reaching `1/α` is at most `α`
(Ville). With `S = Σ (X_m up_m − C_m + R_m)` and `Sh` the variant's shares, **`thr = L/λ + λ V / 8`**, `L = ln(1/α)`:
EARN at `S >= thr` rejects that the variant's expected money given what was public is at most nothing; NO EARN at `S <=
δ · Sh − thr` rejects that it is at least half a tick a share (tz23 lines 410 to 433). `α = 0.005` for each answer and
`δ = 0.005` are TZ-23's. **W1-EARN** is `behind`'s EARN: even at the back of every queue, every departure from behind
it and every crossing order a taker, our quotes earned. **W1-NO-EARN** is `front`'s NO EARN: even first in every queue
and never met by a crossing order, our quotes kept less than half a tick a share. **UNDECIDABLE** otherwise; W1-EARN
first where both hold. Each answer's false-reading probability is at most `0.005` under its own variant's null; the
true queue and the true crossing orders lie between the two variants, and an answer that one variant reaches against
its own assumptions the other cannot reverse. The bound assumes no independence between windows, no calibration and no
distribution, and holds at any look.

**`λ`, fixed before any member is read:** `sqrt(8 L / V)` at the projection's per-member `V` over 576 members — twice
the set, so that a later look at the same constants keeps its power — `0.014605` for `behind` and `0.016557` for `front`
(line 120).

**The projection, and the power**, before any label and deciding nothing: TZ-23's normal approximation at the largest
variance the outcomes allow, `Φ((δ · Sh − thr) / (sqrt(V) / 2))` (tz23 lines 420 to 422). The Architect replayed the
rule, through the instrument's own replay code, on the 302 windows `1792451700` … `1792722600` of the pair book's
streams, every five-minute leg of them one of W0's markets, already read: per member `V` `344.97` and `Sh` `696.9`
shares for `behind`, `268.45` and `2,441.6` for `front`. **Scaled to 288 members**, `behind`'s `thr` is `544.152` USDC,
`0.271` c a share, and the power of W1-EARN against half a tick a share `0.998`; `front`'s NO EARN bound is `3,035.903`
USDC, `0.432` c a share, and the power of W1-NO-EARN against nothing above `0.99999`. Every figure here is the
Architect's computation at 80 digits, independent of the instrument; the self-test asserts the instrument's `thr` within
`1e-20` of it and its power inside `(0.99822, 0.99823)` and `(0.99999, 1.00001)` (lines 2083 to 2087). **The projection
rests on two quantities, the set's `V` and `Sh` per member**, and the set is mostly a weekend where the 302 were
weekdays: `replay` prints both, `thr` and the power at them before any label is read.

**What the 302 windows showed, barred and in-sample** — they framed the rule, and none of them is in the set: `behind`
`−1.227` c a share, `0.276` c of it rebate; `front` `+0.068` c, `0.270` c of it rebate; `front_L0` `+0.138` c; `L250`
`−1.578` c, its crossing fills `64,007` shares of `205,426`, where at 50 ms they were `1,680` of `210,474` — the taker
delay is what keeps a 50 ms quote clear of most crossing orders. **What carries over is the test, not the figure.**

**The venue, re-read by the Architect on 2026-10-23** (map §7 item 87's rule; CANON §1.1). The changelog's newest
entries are of 2026-10-21 and touch neither the crypto markets' fee, rebate, taker delay, order types, tick, minimum
size nor the market websocket; its entry of 2026-09-04 sets the crypto taker delay at **150 ms** from 14:00 UTC that
day. The order-lifecycle page says a post-only order that would match immediately "is rejected instead of executed",
and that during the delay "the order is pending and cannot be canceled"; it still gives the delay as 250 ms, the value
before 2026-08-17, and the changelog's later entry governs. A change of the fee or the rebate would make the set's
documents fail `qualify` and the walk count them as non-members.

**The path, proved on the venue's own record the same day.** The Architect's independent reference — written from this
section's rule alone, every line parsed whole as JSON, every price and size a `Fraction` of its own text, the money in
`Fraction`s, sharing no code with the instrument or TZ-23's — replayed TZ-27's 51 windows: **its 135,900 unit lines
byte for byte the instrument's** — every variant's every fill, band and kind, the book's counts, the frames and the lag
(§4.1). Then the whole path on a stand-in set of the 48 windows `1792680300` … `1792722600`, every leg one of W0's
markets: `fetch` over a stand-in of the pair book's `window.json` with two non-members placed before them, `replay`
twice, `rescore` and `score` twice, under Python 3.12.3 (§6). §0.4 and §6 are those runs' measurements.

**Every unit inside the pair book's idle stretch, and none near or during the archive's run** — TZ-30's rule and code
(lines 380 to 410): a unit — one window's stream files downloaded, verified by their bytes and SHA-256, replayed and
removed — starts only at seconds 15 to 590 of a 900-second window less its budget, its download at `2,000,000` bytes a
second and `45` s beside it, never from its budget and `60` s before 03:00:20 UTC to `60` s after it, and never while
`btc-pairbook-archive.service` reads `active`, `activating`, `deactivating`, `reloading` or `refreshing`; a hold longer
than `7,200` s is BLOCKED, and every unit's start and end is written to a timing file. A request for documents is
budgeted at `120` s and held the same way. After its first 24 units a run projects its replays' processor time over all
its members' bytes and stops BLOCKED above its bound (lines 1295 to 1317).

**What this TZ decides.**

1. **The instrument**, `research/tz32-our-quoting.py`, on the branch `tz-32-our-quoting`; `main` carries it once the
   Boss merges after the verdict.
2. **The set, formed; every member's unit, replayed label-free; the constants on disk with their SHA-256 and the units'
   in `state.json`; the instrument's commit on `origin`** — and only then the labels, read once a run.
3. **W1's reading.** W1-EARN opens W2, live at minimum size with a fixed loss limit (CANON PART II): even with every
   assumption against it, the rule earned at settlement with the rebate. W1-NO-EARN closes W1 for this rule: even with
   every assumption for it, a quote at the touch keeps less than half a tick a share — the named makers' edge is not
   the touch's to take. UNDECIDABLE leaves W1 open, and a later TZ may extend the same sum at the same constants. Where
   both bounds hold the reading is W1-EARN.
4. **The archive's record**, read from its own ledger and printed (§3.4).
5. **Nothing on the host is touched** but this TZ's tree, the forensic store by exclusive create, and the directories
   earlier sessions left (§9).

**Data hygiene.** **No stream of any window of the set has been read by anyone, and no settled document of its legs.**
The pair book's streams read before this TZ are TZ-30's, `1791706500` … `1792403100` and TZ-27's 51, and the
Architect's for this TZ: TZ-27's 51 again, for the reference, and the 651 windows `1792137600` … `1792722600`, for the
exploration and the projection — of them `1792404000` … `1792722600` read first by the Architect, every five-minute leg
of them one of M0's or W0's markets, whose fills TZ-29 and TZ-31 had read. **Nothing of a window at or after
`1792723500` has been read**; the set's first candidate is `1792754100`, and the 34 windows between are W0's legs and
no member. The legs' settled documents of the set's candidates, `1792754700` … `1793068800`, are after W0's last
member and after every document any TZ has read. Nothing of this TZ was chosen on the set: the rule, the variants, `L`,
`λ`, `α`, `δ` and the set rule were fixed on the 302 and TZ-27's 51. §2 bars any read of a member outside the
instrument.

---

## 2. Scope

**Repository paths this TZ may write, and no others:**

1. `research/tz32-our-quoting.py` — new, byte for byte Appendix A's, on branch `tz-32-our-quoting`, then a pull
   request. Not merged by the Executor.
2. `CryptoReports/TZ-32-our-quoting-report.md` — straight to `main`, in one commit. **The one path pushed to `main`,
   and the exemption to item 7 below.**

**Host paths this TZ may write:** `/root/tz32-work/**`; `/root/btc-forensics/`, by exclusive create only (§9); and in
the primary checkout `/root/btc-5m-twap`, its `.git` for the branch and the worktree, and its `CryptoReports/` for the
report. **Host paths it removes, under §9 and nothing else:** `/root/tz32-work/` with its worktree, and the directories
`I scratch` names earlier.

**Prohibited, each absolutely:**

1. No committed file is modified; every `frozen` row of map §0 is byte-identical at run end.
2. **Nothing under `/var/lib/btc-recorder/` or `/var/lib/btc-chainbook/` is opened, listed or written** — TZ-23's audit
   hook refuses every open there and this instrument's every open and listing (lines 203 to 293); only §0.3's `df`,
   `find` and `grep -c`, at both of its runs, and B-RECLAIM-OWN's `df` touch the recorder's root.
3. **Under `/var/lib/btc-pairbook/` nothing is written or listed, and nothing is opened but `<T>/window.json` of a
   candidate, `T` at or after `1792754100`, for reading, by `I fetch` alone** — the named exemption; the hook refuses
   every other open and every listing there, and `du -sb` at §0.3, at both of its runs, reads the store's size. **No
   stream file stored there is opened by anything.** `window.json` carries counts, times, slugs, condition and token
   ids and no price (map §2.5).
4. **Under `/var/lib/btc-pairbook-archive/` nothing is written or listed; `ledger.jsonl` is opened for reading by
   `I archive`, `I fetch` and `I still`, and every complete run's `runs/<A>/set.json` by `I archive` and `I fetch`** —
   the named exemptions; nothing else there is opened but by `du -sb` and `stat` at §0.3. The ledger's records and the
   sets carry events, counts, times, ids, tags, asset names, sizes and hashes and no price: TZ-28's run asserts each
   record against TZ-27's forbidden keys before writing it (`research/tz28-pairbook-archive-timer.py` lines 212 to 220).
5. **No unit is signalled, started, stopped, enabled, disabled or changed.** `systemctl show`, `is-active`,
   `is-enabled`, `list-timers` and `journalctl` are this TZ's only reads of a unit and of systemd.
6. `/root/tz04a-env/`, `/root/tz01-env/`, `/root/tz18a-svc/`, `/root/btc-recorder-svc/`, `/root/btc-pairbook-svc/` and
   `/root/btc-pairbook-archive-svc/` are not modified; `/root/btc-forensics/` only by §9's exclusive create, and the one
   file of it the rehearsal and §0.3 read is read and never written.
7. Nothing is pushed to `main` except the report of item 2.
8. **No label of the set is read before §3.7's constants are on disk with their SHA-256 and the units' in `state.json`
   and the instrument's commit is on `origin`.** A label is the outcome a member's `outcomePrices` states. Three
   exemptions, each named because the body requires it: (a) `qualify`, which asks only whether `outcomePrices` is one of
   the two resolved forms, and `fetch`, which carries each member's document in `w1-set.json`, `outcomePrices` with it,
   and never interprets it — `replay` reads no document but its condition and tokens, and the self-test asserts the
   constants byte-identical with every label flipped; (b) `rehearse`, which reads the labels of TZ-27's 51 legs, every
   one read by TZ-30's rehearsal; (c) `score`, which reads the set's labels once a run, its determinism run included,
   each run a line in the ledger.
9. **Requests:** `gamma-api.polymarket.com/markets`, through TZ-23's `http_json` and its two headers, `User-Agent:
   btc-5m-twap-m0/TZ-23` and `Accept: application/json` (tz23 lines 81, 82 and 233 to 253), in `rehearse` and `fetch`
   alone, each request held by §1's rule; **the archive's Release assets**, from `github.com` and the hosts it redirects
   a download to, `release-assets.githubusercontent.com` and `objects.githubusercontent.com`, anonymously, with
   `User-Agent: btc-5m-twap-tz32` and `Accept: application/octet-stream` (lines 144 and 607 to 637), in `rehearse`,
   `replay` and `rescore` alone, each held by §1's rule; `git` against `origin`, `I archive`'s `git ls-remote` among
   them; and `gh` for the pull request and for git's credential alone. **No other request** — no CLOB, no websocket, no
   Data API, no GitHub API, no authenticated call — and the hook refuses any other host in every mode (lines 203 to
   293).
10. **No stream asset is downloaded but a member's of the set and TZ-27's 51**, and none is read but by the
    instrument's replay, in its unit, before its removal.
11. **No single fill's, member's or window's price, size or outcome is printed or written outside `/root/tz32-work/`**:
    the instrument prints sums over a set — a variant's, a band's, a kind's — and the report quotes them. **This binds
    the Executor's own reads as strictly as the instrument** (map §7 item 118): no file under
    `/root/tz32-work/rehearsal/`, `/root/tz32-work/set/`, `/root/tz32-work/replay/`, `/root/tz32-work/rescore/` or
    `/root/tz32-work/streams/` is printed, whole or in part, by any command but the instrument's modes and `sha256sum`,
    `stat`, `wc -l` and `du`, which print hashes, sizes and counts; the timing files carry windows, seconds and bytes
    and may be printed, and so may `state.json`, the label ledger and every file under `logs/`. The one exemption is
    §9's byte-for-byte copies into `/root/btc-forensics/` of the files the report names by hash.
12. No Release is created, and no dataset, archive or binary enters git history.

---

## 3. The work, in this order

From §3.1 on, `nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz32-work/wt/research/tz32-our-quoting.py` is written
**`I`**; a mode is `I <mode>`, run from `/root/tz32-work`. Every command's output goes to `logs/`, one file per step,
and is quoted in the report. **§9's B-RECLAIM-SCRATCH runs after §3.3 and before §3.4; B-RECLAIM-OWN runs last, after
§3.11.** On a BLOCK before §3.1, B-RECLAIM-OWN runs with `I0` in place of `I` and without its `git worktree remove`
line; on a BLOCK or a FAIL after it, the run goes to §3.11 and §9, skipping every step that needs a PASS it lacks.

**Where the session's permission classifier refuses a command of a block named B-…**, the Executor prints the block, the
Boss runs it verbatim in a root shell on the VPS, and the Executor verifies it through the reads this TZ names — never
from the Boss's account.

### 3.1 The branch and its file

```
git -C /root/btc-5m-twap fetch origin
git -C /root/btc-5m-twap worktree add -b tz-32-our-quoting /root/tz32-work/wt origin/main
```

Then §0.1's script again, verbatim but for its argument, `/root/tz32-work/wt`; it must print the same lines, bytes and
SHA-256 as at §0.1. `sha256sum /root/tz32-work/wt/research/tz23-maker-m0.py` must print `6b3ace2c…`: `main` carries
TZ-23's file. `I fingerprint` must print `FINGERPRINT PASS` again, from the worktree. Commit the one file alone on the
branch, then push it and set its upstream **through `gh`'s stored login, as TZ-29, TZ-30 and TZ-31 did** (map §7 item
114):

```
git -C /root/tz32-work/wt -c credential.helper= -c 'credential.helper=!gh auth git-credential' push https://github.com/seahomebatumi-ai/btc-5m-twap.git tz-32-our-quoting:refs/heads/tz-32-our-quoting; echo "exit=$?"
git -C /root/tz32-work/wt fetch origin +refs/heads/tz-32-our-quoting:refs/remotes/origin/tz-32-our-quoting; echo "exit=$?"
git -C /root/tz32-work/wt branch --set-upstream-to=origin/tz-32-our-quoting; echo "exit=$?"
date -u +%FT%T.%NZ; git -C /root/tz32-work/wt ls-remote origin refs/heads/tz-32-our-quoting
git -C /root/tz32-work/wt rev-parse HEAD
```

— the instant the commit is on `origin`, and its hash there, which must be the worktree's `HEAD` — and open the pull
request against `main` with `gh pr create`. A failed assert or a non-zero exit here is BLOCKED. **The push is what lets
§3.9 read a label:** `score` refuses a `HEAD` that `origin` does not carry (lines 1847 to 1869). The token in `origin`'s
URL is not touched.

### 3.2 The self-test

`I selftest` must print `74 of 74 checks passed`. It reaches no network but a listener of its own on
`127.0.0.1`, and runs on literals, on a synthetic window of two stream files and on temporary trees under
`/root/tz32-work/selftest-tmp/`, which it removes (lines 2090 to 2549). A red self-test stops the run here, and it goes
to §3.11 and §9.

### 3.3 The units, and the directories beside this session

`I still` records the recorder's and the pair book's `MainPID`, `NRestarts` and `ActiveState` in `state.json`, with the
instant, and prints their `MemoryCurrent` and `MemoryPeak` and the archive's two units' states. Then
`I scratch "$(dirname "$S")"` lists every UUID directory beside this session's own and names each **live** — born from 1
s before to 60 s after the start of a running process whose `argv[0]` is `claude` or ends in `/claude.exe` — or
**earlier**.

### 3.4 The archive's record

`I archive`: the archive's two units by `systemctl show`; `ledger.jsonl` read whole, its size and SHA-256, every
complete record printed with its UTC stamp; every run summarized — its start on the calendar or off it, its set, its
restart and its terminal record; every complete run's `set.json` asserted by the SHA-256 its set record carries, with
its files, bytes and windows; the windows the assets reach, at and after `1792754100`; the tags `origin` carries beside
the sets; and whether the archive is halted (lines 415 to 524 and 1640 to 1670). **Printed facts, no threshold:** its
exit is recorded and gates nothing. The report sets each run off the calendar beside §0.3's boots, the timer's journal,
systemd's reload records and the package history (map §7 item 115).

### 3.5 G-REHEARSAL

`I rehearse`: TZ-27's 51 windows, their legs' documents read by TZ-23's `gamma_docs` held to the idle stretch, their 51
stream assets downloaded from `tz-27-pairbook-streams` by the sizes and SHA-256 TZ-27's `set.json` in the forensic store
carries, every unit held, replayed, removed — against the Architect's reference (§4.1). **A network failure is
resumable:** the units on disk are kept, the documents are read again and must be the first run's bytes, and
`I rehearse` may be run again twice, 600 s apart; a third failure is BLOCKED. A FAIL stops the run here, and it goes to
§3.11 and §9.

### 3.6 The instant, then the set — G-SET

First, in its own text, the instant:

```
t=$(date -u +%s); while [ "$t" -lt 1793071200 ]; do sleep 30; t=$(date -u +%s); done; echo "instant reached: $t $(date -u)"
```

Run it in the background where the instant is more than five minutes away, and go on only once it prints. Then
`I fetch`, in the background, its output to `logs/`, read until it prints `G-SET PASS` or fails (§4.2). It first waits
for the archive's ledger to reach `1793068200`; then reads the 350 candidates' `window.json` and requests the stream
rule's survivors' documents in twenties, each request held; `w1-set.json` is written once and its SHA-256 recorded in
`state.json`. **A network failure is resumable:** `I fetch` may be run again twice, 600 s apart, and a third failure is
BLOCKED; a second run that completes must write the same bytes.

### 3.7 The replay, twice — G-BOOK

`I replay`, in the background, its output to `logs/`, read until it prints the constants or fails: every member's unit,
held, downloaded, replayed and removed, each unit's file under `replay/units/`; after its first 24 units it projects its
replays' processor time and stops BLOCKED above `3,000` s; then the units concatenated, G-BOOK (§4.3), the lag, every
variant's sums and each gated variant's thresholds and power (§1, §4.5), the constants' and the units' SHA-256 in
`state.json`. **A network failure is resumable:** the units on disk are kept, and `I replay` may be run again twice,
600 s apart; a third failure is BLOCKED. Then `I replay` again, which replays nothing and must print `unchanged` for
`replay/w1-units.txt` and `replay/w1-constants.json` — contract §6's determinism.

### 3.8 The rescore — DETERMINISM

`I rescore`: every sixteenth member, 18 of 288, downloaded again and replayed again into `rescore/units/`; each unit
file must be byte for byte the replay's (§4.4).

### 3.9 The score, twice

`I score`, then `I score` again. The first reads the labels and prints the reading; the second must print `unchanged`
for `replay/w1-scored.csv` and `replay/w1-reading.json`. The ledger then holds two lines.

### 3.10 The units again — G-STILL

`I still` (§4.6).

### 3.11 The closing reads

§0.3's block again, `I archive` again, then:

```
TZ=UTC systemctl show btc-recorder.service btc-pairbook.service btc-pairbook-archive.service -p MainPID -p NRestarts -p ActiveState -p MemoryCurrent -p MemoryPeak
journalctl -u btc-recorder.service -u btc-pairbook.service -o short-iso --since -24h --no-pager | tail -n 60
free -b
du -sb /root/tz32-work /root/.claude
cat /root/tz32-work/state.json /root/tz32-work/label-ledger.jsonl
```

---

## 4. The gates — fixed here, before any of their data exists

| gate | population | PASS | false failure | power, against |
|---|---|---|---|---|
| **G-REHEARSAL** | TZ-27's 51 windows, `1791660600` … `1791705600` | §4.1's 11 checks equal, exactly | `0` — the same stored bytes replayed by the same rule, equal to the Architect's independent reference on 2026-10-23 | `1`, any change in a stream asset, a document, a fill, a queue, a cancel, a crossing, a band, a sum or the arithmetic |
| **G-SET** | the walk from `1792754100` | 288 members, at most 62 non-members before the 288th | `0` | — |
| **G-BOOK** | every match frame of the members' legs | the rebuilt touch equal to the venue's own at no fewer than 99 in 100 | a count, not an estimate: the rebuilt touch was equal at `68,652` of `68,677` on TZ-27's 51 windows and at `67,282` of `67,389` on the stand-in's 48 | `1`, a lost frame, a misread entry or a missed session |
| **DETERMINISM** | 18 of the 288 members, every sixteenth | each unit file byte for byte the replay's | `0` | `1`, any difference between two downloads or two replays |
| **W1** | `behind`'s and `front`'s fills before `T0 + 300` over the set's 288 members | §4.5 | at most `0.005` for each answer | TZ-23's normal approximation, printed before any label: projected `0.998` for W1-EARN against half a tick a share and above `0.99999` for W1-NO-EARN against nothing |
| **G-STILL** | the recorder and the pair book, §3.3 to §3.10 | unchanged, or the pair book moved by the archive's own restarts alone | `0` — systemd and the archive's ledger read directly | `1`, a restart or a stop that is not the archive's |

### 4.1 G-REHEARSAL

Over TZ-27's 51 windows, **11 checks**: the rehearsal's unit lines, **135,900**, and their SHA-256,
**`52b1c637a51d6b7af3c29ba3aadd75a5e2f0d39410969ee15b61155a4fc3ac60`**, the Architect's; and for each of the nine
variants its fills, shares, `X`, `C`, `R`, `V` and `S` over the 51, with the labels the legs' documents state — 23 Up —
equal to Appendix A's `REF` (lines 161 to 180), as text of twelve decimals. The Architect's lines come from its own
reference, which shares no code with this instrument or TZ-23's (§1); its unit for each window was byte for byte the
instrument's at 51 of 51, under Python 3.12.3. `rehearse` prints `G-REHEARSAL PASS: 11 of 11`. **A FAIL means the
stored record differs from what the Architect replayed, or that the instrument replays otherwise**, and the reading
would not be what §1 describes.

### 4.2 G-SET

`fetch` prints `G-SET PASS` when the walk from `1792754100` has formed 288 members with at most 62 non-members before
the 288th; every member's files are in the archive's assets by their own names, sizes and SHA-256; and `w1-set.json` is
written, its SHA-256 in `state.json`. Every non-member is listed with its reason, and the members by the weekday of
their leg.

### 4.3 G-BOOK

At every match frame of the members — every book frame of the leg's Up token but a subscription's — the touch the replay
rebuilt from the leg's entries, the best bid and its size and the best ask and its size, equals the venue's own at **no
fewer than 99 in 100** (lines 904 to 926, 1005 to 1009 and 1365 to 1368). `replay` prints the counts, and the count of
frames equal at every level beside them, barred: the rebuilt book differs from the venue's far from the touch more often
— at `121` of TZ-27's `68,677` and at `541` of the stand-in's `67,389` — where no quote of this rule rests (map §7 item
121). `score` reads no reading where G-BOOK fails: a FAIL means the replay's touch is not the venue's, and its fills are
not ours.

### 4.4 DETERMINISM

`rescore` downloads every sixteenth member's stream files again, replays them again, and requires each unit file byte
for byte the replay's — 18 of 18.

### 4.5 W1's reading

| condition, on `behind`'s and `front`'s `S`, `V` and `Sh` over the set | reading |
|---|---|
| `behind`'s `S >= thr` | **W1-EARN** — whatever the power |
| else `front`'s `S <= δ · Sh − thr` | **W1-NO-EARN** — whatever the power |
| otherwise | **UNDECIDABLE** |

Each variant read by TZ-23's `reading` on its own thresholds (tz23 lines 426 to 433; lines 1371 to 1378 and 1434 to
1513). Where both hold the reading is W1-EARN, and the report states that `front` reached its NO EARN bound too. **No
row reads a power.** The report prints both gated variants' `S`, its settlement and rebate parts, each per share, both
margins of each, and, barred from every reading, every variant's `S` and shares, each band's and each kind's — fills at
a match and fills against a crossing order — and each variant's per-member extremes.

**What a reading establishes, and what it does not.** W1-EARN says that on these 288 windows the rule's quotes, at the
back of every queue, every departure from behind them and every crossing order a taker after the venue's delay, were
filled in their favour beyond what the outcomes' noise explains — rebate included; it says nothing of a quote placed
live, whose fills move the book this replay holds fixed — W2's. W1-NO-EARN says that the rule's quotes, first in every
queue and never met by a crossing order, kept less than half a tick a share: no quote at the touch keeps the named
makers' edge on these legs, rebate included. Neither speaks of another rule, another latency or another leg.

### 4.6 G-STILL

From §3.3 to §3.10 the recorder keeps its `MainPID`, `NRestarts` and `ActiveState`, and the pair book keeps them or is
moved by the archive's own restarts alone — its ledger's `restart` records since §3.3's read, a chain from the recorded
`MainPID` to the current one, `NRestarts` one higher at each, the unit `active` (lines 1554 to 1571). **This TZ signals
nothing**, so a FAIL runs no block, and the report names what changed beside §3.11's journal of both units — a package
upgrade restarted both on 2026-10-22 and 2026-10-23 (map §6, process supervision; §7 item 120).

---

## 5. The instrument

`research/tz32-our-quoting.py`, Appendix A, fixed by the Architect as this TZ's Validation and written byte for byte.
**The standard library alone**, run under `/root/tz04a-env` — Python 3.12.3, the recorder's interpreter, which nothing
here modifies. It imports nothing from the repository: it **loads** `research/tz23-maker-m0.py` from its own directory,
asserts its SHA-256 `6b3ace2c…` and executes those very bytes (lines 66 to 78), so TZ-23's audit hook, its 60-digit
context and its malloc settings are installed and TZ-23's functions are the ones every step calls: `gamma_docs` and
`http_json` for every document, `qualify` for every leg, `aggregate` — and through it `maker_terms` and `rebate` — for
every position, cost and rebate, `gate_constants` for the thresholds and the power, `reading` for each gated variant's
word and `label_of` for the labels. **Its own code** is its audit hook (lines 203 to 293), the idle stretch and the
archive's run (lines 380 to 410), the archive's ledger, sets and asset map (lines 415 to 524), the stream and leg rules
(lines 529 to 553 and 556 to 584), the downloads (lines 144 and 607 to 637), the replay — the integers, the book, the
blocks, the sweep, the queues, the crossings, the latency, the quoting rule and the line reader (lines 639 to 1102) —
the unit and its money (lines 1106 to 1137), the units held (lines 1239 to 1272), the constants and the score (lines
1344 to 1513), G-STILL (lines 1554 to 1571), the modes, the synthetic window and the self-test. One mode a run; each
prints its findings with UTC stamps, its peak memory, whether glibc took its two settings, and its opens refused by
either hook. A price is an integer of thousandths and a size of hundredths from the venue's own text, every sum of money
a `Decimal` at 60 digits in the main thread, and every figure a unit file carries has twelve decimals exactly (lines
1112 to 1118). Exit `0` is every assert held; exit `1` a failed assert, named, or a BLOCK whose message says so. Run
with `-O` it refuses to start (lines 57 to 59).

---

## 6. Cost

Measured in the Architect's runs of 2026-10-23 and 2026-10-24 under Python 3.12.3 on two cores of an Intel Xeon — the
host has one (map §6), and TZ-29's `constants` ran there about `1.17` times faster a row than in this sandbox (TZ-30 §6)
— the last of them, from 03:18 UTC on 2026-10-24, of Appendix A's bytes: the self-test, `rehearse` twice and the
stand-in's whole path. Taken at the population's upper bound: **the replay at 288 members of the busiest run's mean a
window**, `1792045110`'s 14 files, `352,241,341` bytes — `25,160,096` a window, the largest of the archive's 19 runs by
its own ledger — so **`7,246,107,648` bytes**; the rescore at 18 of them, `452,881,728`; the rehearsal fixed at TZ-27's
51, `678,739,504`; the walk at all 350 candidates' `window.json` and at most 18 document requests, one a twenty. **A
replay's processor time grows with its bytes**: with these bytes `0.2097` s a megabyte over TZ-27's 51 windows and
`0.2157` over the stand-in's 48, its first 24 units `0.2304`; **`0.2440`, the slowest measured** — the stand-in's first
24 units at 02:30 UTC that day, under an earlier text of this file whose replay differed only in not counting the touch
— which every bound below takes.

| check | population | measured | bound |
|---|---|---|---|
| `fetch`, the walk | 350 candidates, at most 18 requests, each held | the stand-in's 50 candidates and 3 requests in `2` s, the first request inside the stretch | `30` s of requests at `0.5` s each; holds of at most `445` s before the first and inside the stretch after it |
| `fetch`, the archive's wait | its ledger read every 60 s from §3.6's instant | — | until the run of 2026-10-27 03:00:20 UTC completes — its runs took `750` to `2,181` s by its ledger (map §2.5) — and **BLOCKED at 06:00:00 UTC** |
| `replay`, the processor | the members' bytes, at most `7,246,107,648` | `193.9` s for the stand-in's 48 windows, `898,626,570` bytes — `0.2157` s a megabyte, its first 24 units `0.2304`, the slowest unit `0.2758` | **`1,768` s** at `0.2440`; about `1,510` on the host at TZ-30's ratio; **projected over the members' own bytes after the first 24 units, BLOCKED above `3,000` s** |
| `replay`, the downloads | the same bytes | `23.9` MB a second here; on the host `13` to `14` MB a second (map §6, GitHub) | `557` s at `13` MB a second |
| `replay`, wall | 288 units, each started in seconds 15 to 590 less its budget | `233` s of units for the stand-in's 48, each inside its idle stretch — two of them — the longest `7.1` s; `616` s of wall clock, `383` of it held | about `4,100` s: `2,330` s of units at about `515` of every `900` |
| `replay`, the second run | 288 unit files concatenated, the constants written | `0.1` s and `32,890,880` bytes at 48 | `5` s |
| `rescore` | 18 members, one in 16 | `13.7` s of replay for the stand-in's 3, `63,759,453` bytes | **`111` s** at the bound's 18 windows and `0.2440`; **projected after its first 6 units, BLOCKED above `300` s** |
| `rehearse` | TZ-27's 51 windows, `678,739,504` bytes, fixed | `142.4` s of replay at `0.2097`, its first 24 units `0.2077`; `190` s of wall clock, none of it held | **`166` s** at `0.2440`; **projected after 24 units, BLOCKED above `240` s**; about `700` s of wall clock |
| `score`, twice | 288 members' units, the labels | `0.1` s a run at 48 | `5` s a run |
| `selftest`, `fingerprint`, `still`, `scratch`, `archive`, each `reclaim` | — | `selftest` under `1` s; the rest TZ-31's and TZ-30's, under `2` s each by their own stamps | `30` s in all |

**Processor at those bounds at most `2,075` s** — the replay's `1,768`, the rehearsal's `166`, the rescore's `111` and
the rest's `30` — **under `3,600`, so nothing is sampled. The fail-fast bounds are derived from the same figures:** the
replay's `3,000` s is its bound `1.70` times, the rescore's `300` its own `2.70` times and the rehearsal's `240` its own
`1.45` times, so that with the rest's `30` s the session's processor stays under `3,600` s with every one at its
fail-fast bound together, `3,570` s. **Wall clock at those bounds about `6,000` s from §3.6 on** — the archive's wait at
most about `1,000` s if its run of 2026-10-27 lasts no longer than its longest so far, the walk `500`, the replay
`4,100`, the rescore `300` and the rest about `100`; an archive that has not moved the last candidate by 06:00:00 UTC
stops `fetch` BLOCKED there, `9,600` s after §3.6's instant. Before §3.6, about `800` s, the rehearsal's `700` of it.
**A hold longer than `7,200` s stops BLOCKED:** the longest wait the idle stretch makes is `445` s, from second 470 to
second 15 of the next window for a request's budget, the calendar guard adds a unit's budget and `120` s, and the
archive's longest run, `1792446859`, lasted `2,181` s from its `start` to its `complete` record — a hold of `7,200` s is
all three together twice over.

**Disk, at the bound.** A unit keeps no copy of a stream: it downloads its window's files, asserts before the download
that `5,400,000,000` bytes stay free once they land, replays them and removes them. The stand-in's 48 units wrote
`7,464,075` bytes of unit files, `8.306` bytes a thousand of stream; at the bound's bytes the replay's units and their
concatenation are about `60,200,000` bytes each, the rescore's `3,800,000`, the rehearsal's tree `14,055,361`, the set
about `270,000`, the logs about `10,000,000` and the stage and the worktree about `8,000,000` — with one window's files
at the pair book's cut, at most `200,000,000` for two stream files, about `357,000,000` bytes; §9's copies of what the
report names, about `78,000,000`. The session's allowance, `900,000,000`, is their sum, about `435,000,000`, twice over,
rounded up (§0.4).

---

## 7. Validation

| # | check | count |
|---|---|---|
| **V1** | §0.2's fingerprint, at §0.2 and §3.1 | `FINGERPRINT PASS`: revision `2026-10-23-a`; anchors 6 of 6, 4 re-derived; 43 rows, 40 of 40 `frozen` equal |
| **V2** | §0.3's host gate | H1 to H4, the memory and the disk gate; the rest printed |
| **V3** | §0.1's and §3.1's file | 1 of 1 hash asserted at each, lines and bytes; TZ-23's file `6b3ace2c…` at each; the branch's diff against `origin/main` names exactly one path, `A`, 2,576 lines |
| **V4** | the self-test | `74 of 74` |
| **V5** | the archive's record | the ledger's size, SHA-256 and records, every run's line, every complete run's set, the windows the assets reach, the tags; recorded, gating nothing |
| **V6** | G-REHEARSAL | `11 of 11`: 135,900 lines, their SHA-256, and 9 variants' totals |
| **V7** | G-SET | 288 members; the candidates considered; every non-member with its reason; the document requests; the members by weekday |
| **V8** | the replay, twice | every unit inside the idle stretch or listed; the projection after 24 units against `3,000` s; G-BOOK; 2 of 2 files `unchanged` at the second run |
| **V9** | DETERMINISM | `18 of 18` |
| **V10** | the score, twice | the reading; 2 of 2 files `unchanged`; 2 ledger lines; the instant §3.1's `ls-remote` printed the instrument's commit on `origin`, beside `state.json`'s `constants_at` and the first ledger line's `at`, the first label read of the set (map §7 item 63) |
| **V11** | G-STILL | PASS, or what changed named beside §3.11's journal |
| **V12** | the hooks | `opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0` at every mode |
| **V13** | memory | every mode's printed peak, against §0.4's floor; `malloc tuned: True` at every mode |
| **V14** | contract §4.2's self-check | run after the push and the pull request and before the report's commit |
| **V15** | §3.11's closing reads | every read printed |
| **V16** | §9's `reclaim` runs | files considered, named by a report, kept by name, copied and already held; the store's count after equal to before plus the copies; every line of B-RECLAIM-OWN's output quoted unfiltered |
| **V17** | §9's removals | `git worktree remove` without `--force` exit `0`; `test -e` exit `1` for `/root/tz32-work` and each directory removed; `git worktree list` naming `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else |

---

## 8. The report

`CryptoReports/TZ-32-our-quoting-report.md`, in contract §8's order. **In its first lines:** W1's reading, with
`behind`'s and `front`'s `S`, each one's two parts, both bounds and both margins, each per share; G-REHEARSAL, G-SET,
G-BOOK and DETERMINISM; the set — candidates considered, members, first and last, non-members; the instant of the first
label read beside the instant the instrument's commit reached `origin` and the constants' `state.json` record (map §7
item 63's rule); and G-STILL. Beyond what V1 to V17 print: the set — **every non-member with its reason**, the members
by weekday, the member list's SHA-256 and the set file's; every variant's messages, crossings, fills, shares, `X`, `C`,
`R`, `V` and members with a fill; the thresholds, both per share, and the power at the set's own `V` and `Sh`; the
capture's lag; **the reading**; and, barred, every variant's `S`, its parts and `S` a share, each band's and each
kind's, and its per-member extremes; **the timing files' summary lines and every unit that ended after second 590**; the
archive's record as `I archive` printed it, at both reads, and each run off the calendar beside §0.3's boots, the
timer's journal, systemd's records and the package history; both units at both reads, memory included; both ledger
lines; every block the classifier refused, who ran it and when; every free-space and `MemAvailable` read with its
instant and bound; §9's counts and removals; and every file the run wrote, by SHA-256, but the unit files — the replay's
288, the rescore's 18 and the rehearsal's 51 — which the concatenated files carry and §9 lets go with the tree. **The
report is drafted in the primary checkout `/root/btc-5m-twap` before B-RECLAIM-OWN and committed after it**, so the
removal of this TZ's tree is in it.

---

## 9. Reclaim — the host left clean (CANON hard rule 15)

**What a file is kept for:** a committed report prints its SHA-256, whole or as a prefix of 16 to 64 hex characters, or
it is kept by name: `state.json`, `label-ledger.jsonl` and every file under `logs/`. `reclaim` copies each into
`/root/btc-forensics/` as `<tree>--<path with / as -->`, by exclusive create, and verifies its hash; a name already
there with the same hash is counted as held, and with another hash is a failed assert (lines 1903 to 1949). The branch
worktree is not copied: `reclaim` asserts that `git status --porcelain --ignored` in it prints nothing and that its
`HEAD` is its upstream's, so `git worktree remove` needs no `--force`. The report draft in `CryptoReports/` counts as a
report. The unit files are not named — `w1-units.txt` and `rehearsal-lines.txt` hold their bytes in order — and go with
the tree; the downloads are removed by each unit as it ends. **No `reclaim`'s output is filtered**: every line it prints
is quoted (map §7 item 119).

**B-RECLAIM-SCRATCH**, after §3.3 and before §3.4, for every directory `I scratch` named **earlier** — none it named
live, and never this session's own; map §3 names TZ-31's pair, `917cd7ac…` and `19ca9482…`, unless a reboot of the host
emptied `/tmp` (map §6, process supervision):

```
I reclaim <each earlier directory, by its full path>
rm -rf <one such directory>; echo "exit=$?"
test -e <that directory>; echo "exit=$?"
```

One `I reclaim` names every earlier directory; then one `rm -rf` and one `test -e` a directory. `reclaim` refuses a
directory born from 1 s before to 60 s after a running claude process started, and any path but `/root/tz32-work` that
is not a UUID directory under `/tmp/` whose parent's name carries `btc-5m-twap`; it prints `RECLAIM PASS` before any
removal. If `I scratch` names none earlier, the block is recorded as empty and skipped.

**B-RECLAIM-OWN**, last, after §3.11 and with the report drafted. **Its output is written to no file; the report quotes
it verbatim from the session**, every line of it:

```
I reclaim /root/tz32-work
git -C /root/btc-5m-twap worktree remove /root/tz32-work/wt; echo "exit=$?"
rm -rf /root/tz32-work; echo "exit=$?"
test -e /root/tz32-work; echo "exit=$?"
git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
find /root/btc-forensics -type f | wc -l
df -B1 --output=source,size,avail /var/lib/btc-recorder
```

The branch `tz-32-our-quoting` stays on `origin` and as a local ref; only its working tree goes. **Kept:**
`/root/btc-recorder-svc/`, `/root/btc-pairbook-svc/` and `/root/btc-pairbook-archive-svc/` are the running units' code,
`/root/tz18a-svc/` the disabled chain book's; the three capture roots, the archive's state and the forensic store are
data, never scratch. **A refused `rm -rf` is handed to the Boss** by §3's route, one tree per command, and verified by
`test -e`.

---

## 10. Pre-send checks

Performed by the Architect on 2026-10-24 against this file as sent, in a reading separate from its writing, with the
repository at `origin/main` `7e08b7996a3504a88536e7a9cfcf3c48083c7837` and map revision `2026-10-23-a` as it ships with
this TZ. `tz23` is `research/tz23-maker-m0.py` at that commit, `6b3ace2c…`; any other line number without a file is
Appendix A's, the extracted file's.

| # | check | result |
|---|---|---|
| **C1** | scope against body | **Repository paths the body names or cites — thirteen, one class, and the files of the map's table:** `CryptoTZ/TZ-32-our-quoting.md`, read by §0.1's script; `SYSTEM-MAP.md` and the files of its table's 43 rows, read by `fingerprint` — `BTC-EXECUTOR-INSTRUCTIONS.md`, `research/twap-divergence.py`, `research/recorder/recorder.py` and `research/pfair.py` among them, the four anchors it re-derives; `BTC-EXECUTOR-INSTRUCTIONS.md`, cited for contract §1, §4.2, §6 and §8; `research/tz32-our-quoting.py`, staged and written on the branch; `research/tz23-maker-m0.py`, installed beside the staged copy and loaded by its bytes in both places, never modified; `research/tz26-nesting-b3-capture.py` and `research/tz28-pairbook-archive-timer.py`, cited for their lines, and `research/tz27-pairbook-archive.py`, cited for the forbidden keys TZ-28's run asserts through it (its lines 151 to 154 and 331 to 337), all three read by no step; `CryptoTZ/TZ-23-maker-m0.md`, cited for its §1 and §4.3, `CryptoTZ/TZ-27-pairbook-archive.md`, cited for its §9, and `CryptoTZ/TZ-30-nesting-b3-measure.md`, cited for its §6, its stream rule and its host gate, and `CryptoTZ/TZ-31-who-earns.md`, cited for its host gate, all read by no step; every `CryptoReports/*.md`, read by `reclaim` for hashes (lines 1872 to 1878) — TZ-30's and TZ-31's among them, cited for their figures and stamps and read by no other step; `CryptoReports/TZ-32-our-quoting-report.md`, written to `main`. **Entry points:** Appendix A's eleven modes (lines 2552 to 2572); §0.1's script; `install`; `sha256sum`; `git` — `fetch`, `worktree add`, `remove`, `prune` and `list`, `add`, `commit`, `push`, `ls-remote`, `rev-parse`, `branch`, `status`, and contract §4.2's `rev-list`, `diff` and `ls-tree`; `gh pr create` and `gh auth git-credential`; `systemctl show`, `is-active`, `is-enabled` and `list-timers`; `journalctl`; `df`, `du`, `find`, `grep`, `tail`, `wc`, `stat`, `ls`, `free`, `cat`, `date`, `sleep`, `echo`, `dirname`, `uptime`, `nproc`, `mkdir`, `rm -rf` and `test -e`. **Outputs:** under `/root/tz32-work/` — `logs/`, `state.json`, `label-ledger.jsonl`, `stage/research/`'s two files, the worktree `wt/`, `selftest-tmp/` (removed by the self-test), `streams/` (each download removed by its unit), `rehearsal/` — `docs.json`, `units/`, `rehearsal-lines.txt`, the timing file — `set/w1-set.json`, `replay/` — `units/`, `w1-units.txt`, `w1-constants.json`, `w1-scored.csv`, `w1-reading.json`, the timing file — and `rescore/` — `units/`, the timing file; copies of them in `/root/btc-forensics/` by §9; the report. **By content class:** `w1-set.json` carries every member's document with its `outcomePrices`, and `rehearsal/docs.json` TZ-27's 51 legs' — §2 item 8's exemptions (a) and (b), and the self-test's flip check holds the constants label-free; the scored file carries each member's label and money — item 8 (c), after the constants and the push; the downloads carry every frame of a member's window — item 10, each removed by its unit; the unit files and their concatenations carry every fill's price and size and a member's figures — item 11, inside the work tree, and the forensic copies of the files the report names by hash, item 11's one exemption; `window.json` is read by `fetch` alone — item 3's exemption — and the archive's ledger and sets by `archive`, `fetch` and `still` — item 4's; the constants and reading files and every log carry sums over a set, non-members' `T` and reasons, windows, seconds and bytes, and the archive's records, which carry no price. **No intersection is left unnamed.** |
| **C2** | origin of every expectation | **§5's literals** are Appendix A's, fixed by the Architect and measured by nothing: exits `0` and `1`, `-O` refused (lines 57 to 59); `6b3ace2c…` is map §0's row. **§7's, by kind.** Quoted from a committed artifact: V1's revision `2026-10-23-a`, `6` anchors, `4` re-derived, `43` rows and `40` `frozen`, map `2026-10-23-a` §0, which ships in this upload; V3's `6b3ace2c…`, map §0; V13's floor, `81,928,192`, map §6's memory row in the same revision; V17's two worktrees, map §3. Computed by an implementation independent of the one under test: V3's `6ec367e6ed995b315063d2d808dd6a3995878011afd76abfbb7b106b645a9c61`, `2,576` lines and `138,209` bytes, by `hashlib` over the extracted bytes; V4's `74`, a static count of the self-test's `ok` calls over its syntax tree, each inside a loop counted once an iteration, and the Architect's run of those bytes under Python 3.12.3 printed `74 of 74`; V6's `11` = 2 + 9 from `mode_rehearse`'s structure, and `REF`'s values — `135,900` lines, `52b1c637…`, the nine variants' totals — from the Architect's reference, every line parsed as JSON and the money in `Fraction`s, sharing no code with the instrument; the self-test's synthetic unit, `100` lines and `6b179243…`, the same reference's over `synth_stream`'s two files; the projection's `thr` `544.15157376119198419…` and `480.01412536394127695…` within `1e-20`, each recomputed at 80 digits by `mpmath` and again by Python's `decimal`, and the powers `0.998222663` and `1.0` inside their bands; `LAST_T` `1793068200`, the calendar run at `1793070020` and `ARCHIVE_WAIT_UNTIL` `1793080800`, integer arithmetic and `date -u -d @…`. Fixed by this TZ and measured by nothing: V7's `288` and `62`, V8's `3,000` and `2` files, V9's `18`, V10's `2` files and `2` lines, V12's `0` and `0`, V17's exits `0` and `1`; G-BOOK's `99` in `100`. **No expectation depends on a quantity this TZ measures:** V16's count is an identity, after = before + copied, true at every admissible value. |
| **C3** | shape of every diff | Three paths, each new: `git cat-file -e 7e08b79:<path>` exits `128` for `research/tz32-our-quoting.py`, `CryptoReports/TZ-32-our-quoting-report.md` and `CryptoTZ/TZ-32-our-quoting.md`, so no change replaces any committed line; V3 asserts `A`. The map is a replacement file, called additive nowhere. PART VI's two words for an additive diff appear nowhere in this TZ — `grep -c` prints `0`. |
| **C4** | cost of every check | §6, at the population's upper bound: the replay at 288 members of the busiest run's mean, `25,160,096` bytes a window, `7,246,107,648` bytes, the rescore at 18 of them, `452,881,728`, the rehearsal fixed at `678,739,504`, every one at the slowest measured rate, `0.2440` s a megabyte — **`1,768`, `111` and `166` s, with the rest's `30`, `2,075` s of single-session processor, under `3,600`, so nothing is sampled**; the walk at 350 candidates' `window.json` and at most 18 requests. **The fail-fast bounds, derived in §6 from the same figures:** the replay's `3,000` s is `1,768` times `1.70`, the rescore's `300` is `111` times `2.70` and the rehearsal's `240` is `166` times `1.45`, so that with the rest's `30` the session stays under `3,600` s with all of them at their bounds together, `3,570`; the rescore projects after its first 6 units of 18 and the others after 24; a hold's `7,200` s is the idle stretch's longest wait, `445` s, the calendar guard's budget and `120` s, and the archive's longest run, `2,181` s, together twice over; `fetch`'s wait ends at 2026-10-27 06:00:00 UTC, `10,780` s after the calendar run that moves the last candidate starts and `9,600` s after §3.6's instant. Wall clock about `6,000` s from §3.6 at those bounds. Disk at the same bound: the tree about `357,000,000` and §9's copies about `78,000,000`, twice their sum rounded up to `900,000,000` (§0.4). |
| **C5** | every count | **The candidates:** `350` = (`1793068200` − `1792754100`) / 900 + 1 = `288` + `62`. **The set, if every candidate qualifies:** `1792754100` … `1793012400`, member list `3ec41ed9…`, and its legs by weekday — `51` on Friday, `96` on Saturday, `96` on Sunday, `45` on Monday — counted by a script over `time.gmtime`; at most `18` document requests, ⌈350 / 20⌉. **The rescore:** `18` = the members 0, 16, … 272. **The spans:** TZ-27's `51` = (`1791705600` − `1791660600`) / 900 + 1; the projection's `302` = (`1792722600` − `1792451700`) / 900 + 1; the stand-in's `48` = (`1792722600` − `1792680300`) / 900 + 1; the exploration's `651` = (`1792722600` − `1792137600`) / 900 + 1; the unread windows between, `34` = (`1792753200` − `1792723500`) / 900 + 1. **The rehearsal:** `135,900` lines over 51 units, each unit's `1 + 9 × 8 + 3 + its fills` lines, summed by the reference; `68,652` and `68,556` of `68,677` match frames, its book lines summed. V1's `43` rows = `40` + `2` + `1`, read from the map, and `4` re-derived anchors: `A2`, `A4`, `A5`, `A6`. V4's `74`, counted over the syntax tree. V6's `11` = 2 + 9. V8's `2` files = the units' concatenation + the constants; V10's `2` = the scored file + the reading. The forensic store: `1,997` before §9 by map §3. The refs: `63` lines by map §1, `67` after four calendar runs. |
| **C6** | every population | W1's `S`, its settlement and rebate parts, `X`, `C`, `R`, `V`, `Sh`, `thr`, both margins and the power: the gated variant's fills before `T0 + 300` over the set's 288 members. Every barred figure — each variant's `S` and shares, each band's and each kind's, the per-member extremes: that variant's fills over the 288. G-BOOK's counts: every book frame of the members' legs' Up token but a subscription's. The lag: every `price_change` frame of the members' legs. G-REHEARSAL's 11: TZ-27's 51 windows. DETERMINISM: every sixteenth member, 18. The projection, `thr` `0.271` c and `0.432` c and the powers: the 302 windows' per-member `V` and `Sh` scaled to 288; the stand-in's figures: its 48 windows. The non-members and their reasons: the candidates considered. The timing lines: each unit and each request. Each memory peak: one mode's process. `MemAvailable` and free space: the host at each read. G-STILL: the two capture units between §3.3 and §3.10. The archive's record: its ledger's complete lines and every complete run's `set.json` at each read, and the tags `origin` carries. `reclaim`'s counts: every file of the trees it walks. |
| **C7** | every signature and every behaviour | **tz23 at `7e08b79`, every function the TZ names, as the file holds it:** `def http_json(url, tries=8):` (233) — one `urllib.request.Request(url, headers=HEADERS, method="GET")` a try (238), `HEADERS` the two of lines 81 and 82; `def gamma_docs(t0s):` (256) — `q = [("slug", "btc-updown-5m-%d" % t) for t in t0s]` (258), `("closed", "true"), ("limit", str(len(t0s) + 5))` (259), one request, `by[d["slug"]] = d` (265), so `docs_of` passes the legs' `T + 600` and reads each by its slug (lines 592 to 602); `def qualify(t0, doc):` (375) — its eight words at lines 379 to 394, `outcomePrices` read only as `not in (["1", "0"], ["0", "1"])` (382), `feeSchedule` against `FEE_SCHEDULE` (386; 69), `eventStartTime != iso(t0)` (388), `CONDITION` `0x[0-9a-f]{64}` (390), two digit tokens (393), called with the leg's `T + 600` (lines 556 to 584); `def kept_doc(doc):` (398) — nine keys, `orderMinSize` not among them, so `leg_problem` reads it from the full document before `kept_doc`; `def maker_terms(side, outcome, s, p):` (316) — `return (-s, p) if side == "B" else (s, p)` (321) for `U`, which on a taker's side `S` for our bid and `B` for our ask gives `+s` and `−s` Up at `p` (lines 1106 to 1137); `def rebate(s, p):` (326) — `return REBATE_COEF * s * p * (1 - p)` (328), `REBATE_COEF = D("0.014")` (70); `def aggregate(t0, rows):` (342) — `ts, side, outcome, s, p = row[:5]` (347), the band `band_of(ts - t0)` (350) of `BANDS` (61 and 62), `b["X"] += x`, `b["C"] += x * pi`, `b["R"] += rebate(s, p)` (353 to 355); `def zero():` (338); `def label_of(doc):` (403) — `return {("1", "0"): 1, ("0", "1"): 0}[...]` (405); `def gate_constants(V, sh, lam=LAMBDA, alpha=ALPHA, delta=DELTA):` (410) — `thr = L / lam + lam * V / 8` (414), `"earn_at": thr, "no_earn_at": delta * sh - thr` (416), the power `0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))` with `sd = float(V.sqrt()) / 2.0` (420 to 422) — called with this TZ's `lam`, `alpha` and `delta` (lines 1361 to 1362), not its defaults; `def reading(S, c):` (426) — `earn` first, then `no_earn` (427 to 433); `def iso(t0):` (363); `def mem_available():` (204); `def _malloc_tune():` (112) — `mallopt(-3, 131072)` and `mallopt(-8, 2)` (120); `def _audit(event, args):` (128) — every `open` under `CAPTURE_ROOTS`, the recorder's and the chain book's (103), refused (130 to 136); `getcontext().prec = 60` (52); `DELTA = D("0.005")` (72), `ALPHA = D("0.005")` (71), `FEE_TYPE` (68). **`research/tz26-nesting-b3-capture.py` at `7e08b79`:** `STREAM_FLOOR = 4500000000` (132) and `WINDOW_STREAM_MAX = 100000000` (134), a window's stream cut at that many stored bytes. **`research/tz28-pairbook-archive-timer.py` at `7e08b79`:** `def write(self, env, rec):` (212) — `tz27.forbid(rec, "ledger.jsonl")` (215) before the append (216 and 217), every record with `wall_ns` (213), which G-STILL reads. **Appendix A's own, each sentence against its lines:** the load by bytes (lines 66 to 78); the hook (lines 203 to 293) — `FIRST_T <= int(m.group(1)) <= LAST_T and mode == "fetch"` for `window.json`, the ledger in `archive`, `fetch` and `still`, a `set.json` in `archive` and `fetch`, `DL_HOSTS` in `rehearse`, `replay` and `rescore`, `GAMMA_HOST` in `rehearse` and `fetch`, `PROCESSES` `git`, `systemctl` and `stat`; the idle stretch and the archive's run (lines 380 to 410) — `IDLE[0] <= p <= IDLE[1] - budget`, the calendar span, `RUNNING`, `HOLD_MAX_S`; the archive's wait (lines 508 to 524) — `assert now < ARCHIVE_WAIT_UNTIL`, `sleep(60)`; the stream rule (lines 529 to 553) and the leg's (lines 556 to 584); the downloads (lines 144 and 607 to 637) — `n == nbytes and h.hexdigest() == sha`, `DL_TRIES` attempts; the replay (lines 639 to 1102) — `advance`'s unmatched end of a block of another stamp before `resolve`, `resolve`'s `P[0][0] < vt_ns`, the refusal `o.p >= opp` and `o.p <= opp`, `o.q = 0 if v.front else` the level's size, `sweep`'s `c < pre` and `c <= 0` stops, `close_block`'s `min(o.s, max(0, tot - o.q))` and `o.q = max(0, o.q - at.get(o.p, 0))` and `if lv < o.q: o.q = lv`, `cross_check`'s `t + TAKER_DELAY_NS` and `v.cross`, `stop`'s `self.stop_ns`, `decide`'s `p_lo <= tgt <= p_hi` and `x_cap`; the money (lines 1106 to 1137) — `FLIP = {"b": "S", "a": "B"}` and `assert bands["pre"]["n"] == 0 and bands["post"]["n"] == 0`; the unit's disk assert, `free - nbytes >= DISK_FLOOR`, and its budget, `5 + -(-nbytes // DL_RATE) + UNIT_BUDGET_S` (lines 1239 to 1272); the projection, `if done == project_after` (lines 1295 to 1317); G-BOOK's `D(touch_equal) >= BOOK_EQUAL_MIN * snapshots` (lines 1365 to 1368); `w1_reading`'s order (lines 1371 to 1378); `score`'s refusal of a `HEAD` `origin` does not carry and of constants or units not `state.json`'s (lines 1847 to 1869); `still_reading`'s chain of restart records (lines 1554 to 1571). Every sentence matched its lines; none was rewritten after this reading. |
| **C8** | every cross-reference | **This TZ's own:** §0.0 to §0.5, §1, §2's items 1 to 12 and exemptions (a) to (c), §3 to §3.11, §4 to §4.6, §5, §6, §7's V1 to V17, §8, §9's two blocks — each resolved to the text it names. **CANON `2026-10-23-a`:** PART II's W track — W1's row, "simulated on the pair book's streams with queue position, the taker delay and our own cancels", "measured on windows whose five-minute legs open after `1792753800`", W2 behind W1 — §1.1's 150 ms taker delay, maker rebate and minimum order, PART II's gate standard, hard rules 13 and 15. **Map `2026-10-23-a`:** §0's rows and anchors; §1's refs, 63 lines; §2.5's archive record — 19 runs, `25,160,096` bytes a window at the busiest — its windows read and unread, and its reserve; §3's forensic store at `1,997`, TZ-31's pair, the two worktrees and the code trees' commits; §4's W0 row; §5's W track; §6's host identity, disk, memory, taker delay, GitHub, process supervision and harness rows; §7's items 63, 87, 97, 114, 115, 118, 119, 120 and 121. **Contract:** §1 steps 1 to 4, §4.2, §6's determinism, §8's order. **TZ-23:** §1's "The test" and §4.3's table. **TZ-27:** its §9's copy of `set.json`, which TZ-30's and TZ-31's host gates asserted. **TZ-30:** §6's host ratio, `1.17`, its stream rule and its H4, `16570` bytes and `ec71b1a7…`. **TZ-31:** its H4, the same two. Each read in its file, not from memory, and each supports the sentence that cites it. |

**Converted to BLOCK conditions under CANON hard rule 13**, because the Architect's session cannot reach the host: H1 to
H4 — the host's identity, its interpreter and its forensic store; the memory and the disk gate, and `floor_check` at
every mode that reads the venue, the Releases or a set, and each unit's disk assert; §0.2's fingerprint against the
primary checkout as it will be; §0.5's two refs conditions; the instant, which §3.6's first command waits for; the
archive's reach, which `fetch` waits for; the set's 288 members and every one's files in the archive's assets, which
G-SET asserts; G-REHEARSAL, which replays again the record the Architect replayed on 2026-10-24 and stops on any change
in it; and G-BOOK, which reads the members' own frames. **Printed and gating nothing:** the archive's ledger, the units,
the boots, the timers, the timer's journal, systemd's records, the package history and the tags — the Architect could
not read them, and no gate of this TZ needs them but G-STILL, which reads them itself.

---

## Appendix A — `research/tz32-our-quoting.py`, byte for byte

Extracted by §0.1's script; the block's content is the file.

```python file=research/tz32-our-quoting.py
#!/usr/bin/env python3
"""TZ-32 - W1, our quoting: does a quote of ours at the touch of the five-minute leg, simulated on the pair book's
streams with queue position, the 150 ms taker delay and our own cancels, keep the named makers' edge?

    fingerprint       contract section 1 steps 3 and 4, asserted: the map's revision, anchors and rows
    selftest          every rule of this file, on literals, on synthetic streams and on temporary trees
    still             the recorder's and the pair book's MainPID, NRestarts and ActiveState: the first run
                      records them, the second compares, the archive's own restarts read from its ledger
                      (G-STILL)
    scratch OWN       the UUID directories beside OWN, this session's, each named live or earlier
    archive           the pair book archive's ledger and the set.json of every run, read and printed, and the
                      asset of every stream file the archive has moved
    rehearse          the quoting rule over TZ-27's 51 windows, every unit held to the idle stretch, against the
                      Architect's independent replay (G-REHEARSAL)
    fetch             the candidates from 1792754100, once the archive has moved them: window.json and the
                      five-minute leg's settled document of each, and the set (G-SET)
    replay            label-free: every member's streams downloaded, replayed and removed, every unit held to the
                      idle stretch; the constants, thresholds and power on disk (G-BOOK)
    rescore           every sixteenth member replayed again, from a second download (DETERMINISM)
    score             the labels, read once, and W1's reading
    reclaim TREE...   section 9

It loads research/tz23-maker-m0.py from beside itself, executed from the bytes whose SHA-256 it asserts, and calls
TZ-23's functions for the documents' rule, every request for them, every position, cost and rebate, the thresholds,
the power, the reading and the labels: it writes no second implementation of any of them. Its own code is the replay
of a window's streams - the leg's Up book rebuilt, each match read from the venue's own book frame, our quotes placed,
queued, filled and cancelled at venue time - and the archive's record, the downloads, the units held to the idle
stretch and G-STILL, written again for its own hook. Its requests are TZ-23's to gamma-api.polymarket.com, through
TZ-23's http_json and its two headers; downloads of Release assets from github.com, with User-Agent:
btc-5m-twap-tz32; and git against origin. An audit hook refuses every open, listing, request and process TZ-32
section 2 does not give the running mode. It writes under /root/tz32-work/ and, in reclaim, new files in
/root/btc-forensics/ by exclusive create. It prints sums over a set, and of a single window its figures inside the work
tree alone. Exit 0: every assert of the mode held. Exit 1: an assert failed, and its message names it. Run it with
the recorder's interpreter, /root/tz04a-env.

Written for CryptoTZ/TZ-32-our-quoting.md. The TZ is the specification.
"""

import collections
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
import types
import urllib.error
import urllib.parse
import urllib.request

if not __debug__:
    sys.stderr.write("tz32: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(2)

HERE = os.path.dirname(os.path.abspath(__file__))
TZ23_NAME = "tz23-maker-m0.py"
TZ23_SHA256 = "6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f"


def load_tz23(path):
    """TZ-23's instrument, executed from the very bytes whose SHA-256 is asserted. It installs its audit hook - every
    open under the recorder's and the chain book's roots refused - sets the main thread's decimal precision to 60
    digits and tunes glibc's malloc."""
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

MAP_REVISION = "2026-10-23-a"
ANCHORS = {"A1": "229a944f2d51", "A2": "6c5089330629",
           "A3": "0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable",
           "A4": "437b45ea196b", "A5": "0f6c90451cbd", "A6": "729f0bcdbee3"}
ANCHOR_FILES = {"A2": "research/twap-divergence.py", "A4": "BTC-EXECUTOR-INSTRUCTIONS.md",
                "A5": "research/recorder/recorder.py", "A6": "research/pfair.py"}
MAP_ROWS = {"frozen": 40, "tracked": 2, "reported": 1}
ROW = re.compile(r"^\| `([^`]+)` \| ([0-9,]+|—) \| ([0-9,]+|—) \| (frozen|tracked|reported) \| "
                 r"`?([0-9a-f]{64}|self-reference[^|]*?)`? \|$", re.M)
ANCHOR_ROW = re.compile(r"^\| `(A[0-9])` — [^|]*\| `([^`]+)` \|$", re.M)

WINDOW = 900
W0_LAST = 1792753800         # W0's last member, 2026-10-23 11:10 UTC (TZ-31): no fill of a later market has been read
FIRST_T = 1792754100         # the first window whose five-minute leg, FIRST_T + 600, opens after W0_LAST
NEED = 288                   # members: three days of windows, one leg a window
NONMEMBER_MAX = 62           # the walk is BLOCKED past this many non-members before the 288th member
LAST_T = FIRST_T + (NEED + NONMEMBER_MAX - 1) * WINDOW     # 1793068200: the candidates' last window, 350 in all
ARCHIVE_WAIT_UNTIL = 1793080800    # 2026-10-27 06:00:00 UTC: fetch waits for the archive to reach LAST_T until then
LEG = 600                    # a window's five-minute leg opens at T + 600 and closes at T + 900
MIN_SIZE = 5                 # the venue's minimum order, asserted in every member's document
# The quoting rule (TZ-32 section 1): host seconds after the leg's open, the price band in thousandths, the
# position cap and the order's size in hundredths of a share
PARAMS = {"start": 0, "stop": 295, "p_lo": 50, "p_hi": 950, "x_cap": 2000, "size": 500}
# (name, one-way latency ms, first in its level's queue, departures from the level in proportion, an order that
# crosses ours a taker after the delay): the first two are gated - behind, every assumption against us, for W1-EARN;
# front, every assumption for us, for W1-NO-EARN - and the rest barred from every reading
VARIANTS = (("behind", 50, False, False, True), ("front", 50, True, False, False), ("prop", 50, False, True, True),
            ("behind_nocross", 50, False, False, False), ("front_cross", 50, True, False, True),
            ("L0", 0, False, False, True), ("L100", 100, False, False, True), ("L250", 250, False, False, True),
            ("front_L0", 0, True, False, False))
GATED = ("behind", "front")
ALPHA = D("0.005")           # each answer's false-reading probability
DELTA = tz23.DELTA           # half a tick a share, TZ-23's and W0's bar
LAMBDA = {"behind": D("0.014605"), "front": D("0.016557")}    # fixed before any member is read: TZ-32 section 1
BOOK_EQUAL_MIN = D("0.99")   # G-BOOK: the rebuilt touch equals the venue's own book frame's at 99% of match frames
RESCORE_EVERY = 16           # rescore replays members 0, 16, 32, ...: 18 of 288
REPLAY_CPU_MAX = 3000        # processor seconds the replays may take, projected after their first 24 units
RESCORE_CPU_MAX = 300
REHEARSAL_CPU_MAX = 240
PROJECT_AFTER = 24           # a replay or the rehearsal projects its processor time after its first 24 units,
RESCORE_PROJECT_AFTER = 6    # the rescore, of 18, after its first 6
UNIT_BUDGET_S = 45           # a unit's budget beside its download: replay and deletion
DL_RATE = 2000000            # bytes a second a download is budgeted at, TZ-28's
DL_TRIES = 6
WALK_BUDGET_S = 120          # a request for documents starts no later than second 470
DOC_CHUNK = 20               # TZ-23's chunk: twenty slugs a request
IDLE = (15, 590)             # the pair book's idle stretch: a unit starts at second 15 or later, ends by 590
ARCHIVE_UNIT = "btc-pairbook-archive.service"
ARCHIVE_TIMER = "btc-pairbook-archive.timer"
ARCHIVE_CALENDAR_S = 10820   # the archive's calendar run, 03:00:20 UTC
ARCHIVE_LEAD_S = 60          # nothing starts from budget + 60 s before it to 60 s after it
RUNNING = ("active", "activating", "deactivating", "reloading", "refreshing")
HOLD_MAX_S = 7200
MEM_FLOOR = 81928192         # MemAvailable: twice the largest peak of any mode the Architect measured (TZ-32 section 0.4)
DISK_FLOOR = 5400000000      # free bytes on /dev/vda2: the pair book's STREAM_FLOOR and this session's (TZ-32 section 0.4)

UA = "btc-5m-twap-tz32"
DL_HEADERS = {"User-Agent": UA, "Accept": "application/octet-stream"}
REPO = "seahomebatumi-ai/btc-5m-twap"
DL_URL = "https://github.com/" + REPO + "/releases/download/%s/%s"
DL_HOSTS = ("github.com", "release-assets.githubusercontent.com", "objects.githubusercontent.com")
GAMMA_HOST = "gamma-api.polymarket.com"
ASSET_RE = re.compile(r"([0-9]{10})-(stream(?:\.[1-9][0-9]*)?\.jsonl\.gz)")
STREAM_FILE_RE = re.compile(r"stream(?:\.[1-9][0-9]*)?\.jsonl\.gz")
SUBSCRIBE_BY_S = 600         # the stream subscribed by T + 600
LAST_FRAME_S = 900           # and its last frame at or after T + 900
GAP_MAX_NS = 15 * 10 ** 9    # with no gap between frames above 15 s

# the rehearsal: TZ-27's 51 windows, its set.json in the forensic store (TZ-27's report), and the Architect's lines
# over them from an independent replay (TZ-32 section 4.1)
REHEARSAL_TS = tuple(range(1791660600, 1791705600 + 1, WINDOW))
TZ27_TAG = "tz-27-pairbook-streams"
TZ27_SET = "/root/btc-forensics/tz27-work--archive--set.json"
TZ27_SET_SHA = "ec71b1a7ce7db37ff29a49156006541dd5729c1df2c829c481eb64181228e4dd"
REF = {"lines": 135900, "digest": "52b1c637a51d6b7af3c29ba3aadd75a5e2f0d39410969ee15b61155a4fc3ac60", "totals": {
    # fills, shares, X, C, R, V and S over the 51 windows, the labels the legs' settled documents state: 23 Up
    "behind": [7219, "29749.980000000000", "148.620000000000", "186.702990000000", "73.284744755460",
               "14541.894000000000", "-314.048245244540"],
    "front": [26214, "99744.330000000000", "52.850000000000", "88.478290000000", "244.042849013460",
              "14316.016700000000", "-16.225440986540"],
    "prop": [10076, "38817.950000000000", "108.130000000000", "150.934090000000", "94.534436869460",
             "15627.275900000000", "-301.729653130540"],
    "behind_nocross": [7188, "29598.260000000000", "141.500000000000", "176.187790000000", "72.852862339460",
                       "14476.772200000000", "-307.324927660540"],
    "front_cross": [26232, "99839.700000000000", "46.180000000000", "85.580190000000", "244.315285023460",
                    "13867.026400000000", "-9.624904976540"],
    "L0": [9236, "37841.480000000000", "120.560000000000", "246.148810000000", "92.467183565260",
           "13402.157600000000", "-295.291626434740"],
    "L100": [6410, "26551.630000000000", "172.350000000000", "117.943900000000", "65.091487813800",
             "15468.213300000000", "-264.942412186200"],
    "L250": [6636, "28849.690000000000", "57.350000000000", "-59.683100000000", "71.022929390000",
             "16803.875300000000", "-242.283970610000"],
    "front_L0": [32813, "126600.190000000000", "81.090000000000", "153.311610000000", "311.240369556060",
                 "13631.537300000000", "17.878759556060"]}}

WORK = "/root/tz32-work"
WT = WORK + "/wt"
STATE = WORK + "/state.json"
LEDGER = WORK + "/label-ledger.jsonl"
PRIMARY = "/root/btc-5m-twap"
REPORTS = PRIMARY + "/CryptoReports"
FORENSICS = "/root/btc-forensics"
BRANCH = "tz-32-our-quoting"
UNITS = {"recorder": "btc-recorder.service", "pairbook": "btc-pairbook.service"}
PAIRBOOK = "/var/lib/btc-pairbook"
RECORDER = "/var/lib/btc-recorder"
CHAINBOOK = "/var/lib/btc-chainbook"
ARCHIVE_STATE = "/var/lib/btc-pairbook-archive"
ARCHIVE_LEDGER = ARCHIVE_STATE + "/ledger.jsonl"
SHOW_ENV = {"TZ": "UTC", "LC_ALL": "C", "SYSTEMD_COLORS": "0", "SYSTEMD_PAGER": ""}
UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
TOKEN = re.compile(r"[0-9a-f]{16,64}")
LIVE_S = 60

# ---- the audit hook: TZ-32 section 2's reads, writes, requests and processes -----------------------------

MODE = [None]
REFUSED = []
WRITE_FLAGS = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC
PB_WINDOW = re.compile(r"/var/lib/btc-pairbook/([0-9]{10})/window\.json")
ARCHIVE_SET = re.compile(r"/var/lib/btc-pairbook-archive/runs/([0-9]{10})/set\.json")
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


def policy(mode, event, args):
    """None where TZ-32 section 2 allows the event in this mode; otherwise the reason it is refused."""
    if event == "urllib.Request":
        host = urllib.parse.urlsplit(args[0]).hostname if args and isinstance(args[0], str) else None
        if mode in ("rehearse", "replay", "rescore") and host in DL_HOSTS:
            return None
        if mode in ("rehearse", "fetch") and host == GAMMA_HOST:
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
        if any(_under(p, r) for r in (RECORDER, CHAINBOOK, PAIRBOOK, ARCHIVE_STATE)):
            return "a listing under a capture root or the archive's state"
        return None
    wm, fl = (args[1] if len(args) > 1 else None), (args[2] if len(args) > 2 else None)
    w = _writing(wm, fl)
    if _under(p, CHAINBOOK) or _under(p, RECORDER):
        return "an open under the recorder's or the chain book's root"
    if _under(p, PAIRBOOK):
        m = PB_WINDOW.fullmatch(p)
        if not w and m is not None and FIRST_T <= int(m.group(1)) <= LAST_T and mode == "fetch":
            return None
        return "an open under the pair book's root"
    if _under(p, ARCHIVE_STATE):
        if not w and mode in ("archive", "fetch") and (p == ARCHIVE_LEDGER or ARCHIVE_SET.fullmatch(p)):
            return None
        if not w and mode == "still" and p == ARCHIVE_LEDGER:
            return None
        return "an open under the archive's state"
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
    if why is not None:
        REFUSED.append((event, str(args[0]) if args else ""))
        raise GuardError("%s refused in mode %s, %s: %r" % (event, MODE[0], why, args[0] if args else None))


sys.addaudithook(_audit)

# ---- small helpers ----------------------------------------------------------------------------------------


def q12(x):
    """A figure for print, half-even to 12 places; every sum and comparison is made on the exact figure."""
    s = fx(D(x).quantize(D("0.000000000001")))
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


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh, parse_float=D)


def load_state():
    return load_json(STATE) if os.path.exists(STATE) else {}


def save_state(st):
    write_atomic(STATE, (json.dumps(st, sort_keys=True, indent=1, default=tz23._dec) + "\n").encode("utf-8"))


def free_bytes(path=WORK):
    st = os.statvfs(path)
    return st.f_bavail * st.f_frsize


def floor_check():
    """Before a mode that reads the venue, the archive's Releases or a set: glibc's two settings, the memory and the
    disk floor."""
    assert tz23.MALLOC_TUNED, "BLOCKED: glibc did not take the mmap threshold and the arena count"
    avail, free = tz23.mem_available(), free_bytes()
    out("MemAvailable %d bytes, floor %d; free %d bytes, floor %d" % (avail, MEM_FLOOR, free, DISK_FLOOR))
    assert avail >= MEM_FLOOR, "BLOCKED: MemAvailable %d bytes, below %d" % (avail, MEM_FLOOR)
    assert free >= DISK_FLOOR, "BLOCKED: %d bytes free, below %d" % (free, DISK_FLOOR)


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

# ---- the clock: the pair book's idle stretch and the archive's run -------------------------------------------


def archive_state():
    cp = subprocess.run(["systemctl", "is-active", ARCHIVE_UNIT], capture_output=True, text=True)
    return cp.stdout.strip()


def quiet(now, budget, state_of=archive_state):
    """None where a unit of `budget` seconds may start at `now`; otherwise why not: it starts inside the pair
    book's idle stretch and ends by its second 590, never near or during the archive's run."""
    p = int(now) % WINDOW
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
    """Until a unit of `budget` seconds may start; returns that instant and the seconds waited."""
    assert budget <= IDLE[1] - IDLE[0], "a unit of %d s fits no idle stretch" % budget
    t0 = clock()
    while True:
        now = clock()
        why = quiet(now, budget, state_of)
        if why is None:
            return now, now - t0
        assert now - t0 <= HOLD_MAX_S, "BLOCKED: held %.0f s, the last reason %s" % (now - t0, why)
        sleep(1.0)

# ---- the archive's record: its ledger, every run's set.json, and the asset of every stream file -------------


def ledger_records(path=ARCHIVE_LEDGER):
    with open(path, "rb") as fh:
        raw = fh.read()
    lines = raw.split(b"\n")
    tail = lines.pop()
    return raw, [json.loads(ln) for ln in lines if ln.strip()], tail


def archived_sets(recs, state=ARCHIVE_STATE):
    """Every run whose ledger holds a complete record: its set.json, asserted by the SHA-256 its set record carries,
    its tag, assets and counts against that record."""
    runs, order = {}, []
    for r in recs:
        a = r.get("run")
        if a not in runs:
            runs[a] = []
            order.append(a)
        runs[a].append(r)
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
    """T -> {file: {tag, asset, bytes, sha256}}, every stream file once; a file in two sets is a failed assert."""
    m = {}
    for s in sets:
        for x in s["doc"]["assets"]:
            mt = ASSET_RE.fullmatch(x["asset"])
            assert mt and int(mt.group(1)) == x["T"] and mt.group(2) == x["file"], "an asset named %r" % x["asset"]
            row = m.setdefault(x["T"], {})
            assert x["file"] not in row, "window %d: %s in two sets" % (x["T"], x["file"])
            row[x["file"]] = {"tag": s["tag"], "asset": x["asset"], "bytes": x["bytes"], "sha256": x["sha256"]}
    return m


def ledger_summary(recs):
    """The archive's runs from its own records: each run's events, set, restart and terminal record, and whether it
    began on the calendar; whether the archive is halted."""
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
        sec = a % 86400 if isinstance(a, int) else None
        when = "calendar" if sec == ARCHIVE_CALENDAR_S else ("off-calendar, second %s of the day" % sec)
        parts = ["run %s %s, %s: %d records; terminal %s" % (a, utc(a) if isinstance(a, int) else "-", when, len(rs),
                                                            term[-1] if term else "none")]
        for r in [r for r in rs if r.get("event") == "set"][-1:]:
            parts.append("set %s: %s files, %s bytes, windows %s to %s" % (
                r.get("tag"), r.get("assets_n"), r.get("bytes_total"), r.get("first_T"), r.get("last_T")))
        for r in [r for r in rs if r.get("event") == "restart"][-1:]:
            parts.append("restart: window %s, pid %s after %s, NRestarts %s" % (
                r.get("W"), r.get("pid"), r.get("stopped"), r.get("NRestarts")))
        for r in [r for r in rs if r.get("event") == "complete"][-1:]:
            parts.append("complete: requests %s, started outside %s, ended outside %s, rate %s a day" % (
                r.get("requests"), r.get("started_outside"), r.get("ended_outside"), r.get("rate_per_day")))
        for r in rs:
            if r.get("event") in ("deferred", "halt", "refused", "timer-disabled"):
                parts.append("%s in %s: %s" % (r.get("event"), r.get("phase"), r.get("reason", r.get("exit"))))
        lines.append("; ".join(parts))
    flags = [r.get("event") for r in recs if r.get("event") in ("halt", "clear")]
    return {"runs": order, "lines": lines, "halted": bool(flags) and flags[-1] == "halt",
            "terminal": {a: [r.get("event") for r in runs[a] if r.get("event") in ("complete", "empty", "halt")]
                         for a in order}}


def archived_to():
    """The asset map of every complete run, and the last window it reaches."""
    _raw, recs, _tail = ledger_records()
    amap = asset_map(archived_sets(recs))
    return amap, max(amap)


def wait_archive(clock=time.time, sleep=time.sleep, read=archived_to):
    """Until the archive has moved every window to LAST_T: its ledger read again every 60 s, BLOCKED at
    ARCHIVE_WAIT_UNTIL. Returns the asset map and the seconds waited."""
    t0 = clock()
    amap, last = read()
    said = None
    while last < LAST_T:
        now = clock()
        assert now < ARCHIVE_WAIT_UNTIL, "BLOCKED: the archive has moved windows to %d, below %d, at %s" % (
            last, LAST_T, utc(now))
        if said is None or now - said >= 1800:
            out("the archive has moved windows to %d; the candidates end at %d; its ledger read again every 60 s "
                "until %s" % (last, LAST_T, utc(ARCHIVE_WAIT_UNTIL)))
            said = now
        sleep(60)
        amap, last = read()
    return amap, clock() - t0

# ---- the set: TZ-32 section 1's rules for a window -------------------------------------------------------------


def stream_problem(w, t, assets):
    """The first stream condition window.json `w` fails, or None: opened, not cut, not stopped, not joined late,
    subscribed by T + 600, its last frame at or after T + 900, no gap above 15 s, every file of it archived."""
    st = w.get("stream") if isinstance(w, dict) else None
    if not isinstance(st, dict):
        return "stream: none"
    if w.get("joined_late") is not False or w.get("stopped") is not False:
        return "stream: joined late or stopped"
    if st.get("opened") is not True or st.get("off_reason") is not None or not st.get("files"):
        return "stream: not opened"
    if st.get("cut") is not False:
        return "stream: cut"
    sub, last, gap = st.get("subscribed_wall_ns"), st.get("last_frame_wall_ns"), st.get("max_gap_ns")
    if not (type(sub) is int and sub <= (t + SUBSCRIBE_BY_S) * 10 ** 9):
        return "stream: subscribed late"
    if not (type(last) is int and last >= (t + LAST_FRAME_S) * 10 ** 9):
        return "stream: ended early"
    if not (type(gap) is int and gap <= GAP_MAX_NS):
        return "stream: a gap above 15 s"
    files = st["files"]
    if not (all(isinstance(f, str) and STREAM_FILE_RE.fullmatch(f) for f in files) and len(set(files)) == len(files)):
        return "stream: files"
    if sorted(assets.get(t, {})) != sorted(files):
        return "stream: not archived"
    return None


def leg_problem(w, t, doc):
    """The first rule the window's five-minute leg fails, or None: its settled document by TZ-23's qualify, unchanged,
    orderMinSize 5, and its condition and tokens those window.json carries for the leg."""
    if doc is None:
        return "document: absent"
    why = tz23.qualify(t + LEG, doc)
    if why is not None:
        return "document: %s" % why
    v = doc.get("orderMinSize")
    if isinstance(v, bool) or not isinstance(v, (int, D)) or D(v) != MIN_SIZE:
        return "document: order size"
    mk = (w.get("markets") or {}).get("m5") if isinstance(w, dict) else None
    if not isinstance(mk, dict) or mk.get("slug") != "btc-updown-5m-%d" % (t + LEG):
        return "window.json: the leg's slug"
    if not (mk.get("conditionId") == doc["conditionId"] and loads_maybe(mk.get("clobTokenIds")) ==
            json.loads(doc["clobTokenIds"]) and loads_maybe(mk.get("outcomes")) == ["Up", "Down"]):
        return "window.json: the leg's condition or tokens"
    return None


def loads_maybe(v):
    """A field window.json carries verbatim from the venue's document, JSON text inside JSON, parsed; anything else
    as it is (TZ-24's rule)."""
    if isinstance(v, str):
        try:
            return json.loads(v)
        except ValueError:
            return None
    return v


def window_json(t, root=PAIRBOOK):
    with open(os.path.join(root, str(t), "window.json"), "rb") as fh:
        return json.loads(fh.read())


def docs_of(ts, holdf=hold):
    """The settled documents of the five-minute legs of windows ts, TZ-23's gamma_docs in requests of twenty, each
    started inside the idle stretch; by window."""
    by = {}
    for i in range(0, len(ts), DOC_CHUNK):
        chunk = ts[i:i + DOC_CHUNK]
        holdf(WALK_BUDGET_S)
        got = tz23.gamma_docs([t + LEG for t in chunk])
        for t in chunk:
            by[t] = got.get("btc-updown-5m-%d" % (t + LEG))
    return by

# ---- downloads: one Release asset, by its tag and name, verified by its bytes and SHA-256 ----------------------


def download(tag, asset, nbytes, sha, dest, url_of=None, tries=DL_TRIES, sleep=time.sleep):
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

# ---- the replay: one window's streams, W1's quoting rule (TZ-32 section 1) ----------------------------------

MS_NS = 10 ** 6
PRICE_UNIT = 1000          # a price as an integer of thousandths: the venue prints at most three decimals
SIZE_UNIT = 100            # a book size as an integer of hundredths: the venue prints at most two decimals
TAKER_DELAY_NS = 150 * MS_NS     # the venue's crypto taker delay (CANON section 1.1): a crossing order waits this long
SEND, CANCEL, CROSS = 0, 1, 2
_PRICE = re.compile(r"(0|[1-9][0-9]*)(?:\.([0-9]{1,3}))?")
_SIZE = re.compile(r"(0|[1-9][0-9]*)(?:\.([0-9]{1,2}))?")


_PRICES, _SIZES = {}, {}


def price_int(s):
    """A price's text as an integer of thousandths, exactly; any other text is a failed assert. Each text is parsed
    once and remembered."""
    v = _PRICES.get(s)
    if v is None:
        m = _PRICE.fullmatch(s)
        assert m, "a price %r" % (s,)
        v = _PRICES[s] = int(m.group(1)) * PRICE_UNIT + int((m.group(2) or "").ljust(3, "0"))
    return v


def size_int(s):
    """A book size's text as an integer of hundredths, exactly; any other text is a failed assert. Each text is parsed
    once and remembered, at most 2 ** 16 of them, and forgotten at each window's start."""
    v = _SIZES.get(s)
    if v is None:
        m = _SIZE.fullmatch(s)
        assert m, "a size %r" % (s,)
        v = int(m.group(1)) * SIZE_UNIT + int((m.group(2) or "").ljust(2, "0"))
        if len(_SIZES) < 1 << 16:
            _SIZES[s] = v
    return v


class Order:
    __slots__ = ("side", "p", "s", "q", "state", "done_at", "xing")

    def __init__(self, side, p, s):
        self.side, self.p, self.s, self.q = side, p, s, None
        self.state = "sent"            # sent, then resting, then filled, cancelled or refused
        self.done_at = None            # the venue instant it left the book or was refused
        self.xing = False              # a crossing order is held against it


class Variant:
    """One way of placing the same quotes, replayed beside the others on the same books."""

    def __init__(self, name, L_ms, front=False, prop=False, cross=True):
        self.name, self.L, self.front, self.prop, self.cross = name, L_ms * MS_NS, front, prop, cross
        self.pend, self.seq, self.fills, self.resting = [], 0, [], []
        self.live = {"b": None, "a": None}
        self.n = {"sent": 0, "cancels": 0, "refused": 0, "crossings": 0}
        self.unknown, self.x_known = [], 0

    def fill(self, vt, side, p, f, kind):
        self.fills.append((vt, side, p, f, kind))
        heapq.heappush(self.unknown, (vt, f if side == "b" else -f))

    def known_x(self, h):
        """Up shares, in hundredths, of every fill the host has learned of by h: a fill reaches it L after the venue
        makes it."""
        u = self.unknown
        while u and u[0][0] + self.L <= h:
            self.x_known += heapq.heappop(u)[1]
        return self.x_known

    def _push(self, tau, kind, o, c=0):
        self.seq += 1
        heapq.heappush(self.pend, (tau, self.seq, kind, o, c))

    def send(self, h, side, p, s):
        o = Order(side, p, s)
        self._push(h + self.L, SEND, o)
        self.n["sent"] += 1
        return o

    def cancel(self, h, o):
        self._push(h + self.L, CANCEL, o)
        self.n["cancels"] += 1


class Window:
    """One window's replay, frames in the order the pair book stored them: the five-minute leg's Up book rebuilt,
    every variant's orders placed, filled and cancelled at venue time, and each match's book frame compared with the
    book rebuilt to it (TZ-32 section 1)."""

    def __init__(self, T, params, variants):
        self.T, self.T0, self.pm, self.vs = T, T + 600, params, variants
        self.bids, self.asks = {}, {}
        self.seeded, self.stopped = False, False
        self.block, self.bvt, self.touch0 = [], None, (None, None)
        self.start_ns = (self.T0 + params["start"]) * 10 ** 9
        self.stop_ns = (self.T0 + params["stop"]) * 10 ** 9
        self.c = {"matches": 0, "two_sided": 0, "snapshots": 0, "snapshots_equal": 0, "touch_equal": 0, "sessions": 0,
                  "closes": 0}

    def best(self, side):
        bk = self.bids if side == "b" else self.asks
        if not bk:
            return None
        return max(bk) if side == "b" else min(bk)

    def advance(self, vt_ns):
        """Before a frame of the leg stamped vt_ns: a block of another stamp ends, unmatched; then every variant's
        events due before vt_ns take effect, in their own order, on the book as it stands."""
        if self.block and vt_ns != self.bvt:
            self.close_block(False)
        self.resolve(vt_ns)

    def resolve(self, vt_ns):
        """Every variant's events due before venue instant vt_ns, in the order of their instants: an order arrives -
        refused where it would cross, else resting behind the level's displayed size, or first in it at front - a
        cancel takes its order off, and a crossing order held for the taker delay fills what is left of its own."""
        for v in self.vs:
            P = v.pend
            if not P or P[0][0] >= vt_ns:
                continue
            while P and P[0][0] < vt_ns:
                tau, _seq, kind, o, c = heapq.heappop(P)
                if kind == SEND:
                    opp = self.best("a" if o.side == "b" else "b")
                    if opp is not None and (o.p >= opp if o.side == "b" else o.p <= opp):
                        o.state, o.done_at = "refused", tau
                        v.n["refused"] += 1
                        continue
                    o.q = 0 if v.front else (self.bids if o.side == "b" else self.asks).get(o.p, 0)
                    o.state = "resting"
                    v.resting.append(o)
                elif kind == CANCEL:
                    if o.state in ("sent", "resting"):
                        o.state, o.done_at = "cancelled", tau
                else:
                    o.xing = False
                    if o.state == "resting":
                        f = min(o.s, c)
                        o.s -= f
                        v.fill(tau, o.side, o.p, f, "x")
                        if o.s == 0:
                            o.state, o.done_at = "filled", tau
            v.resting = [o for o in v.resting if o.state == "resting"]

    def sweep(self, side, t0):
        """A match's consumption on `side` from the side's best level at the block's start, t0, outward: each level's
        decrease while every level before it was emptied; [(price, consumed)], the last possibly partial."""
        cur = self.bids if side == "b" else self.asks
        first, dec = {}, {}
        for sd, p, old, new in self.block:
            if sd != side:
                continue
            if p not in first:
                first[p] = old
            dec[p] = first[p] - new
        if dec.get(t0, 0) <= 0:
            return []
        levels = sorted((p for p in set(first) | set(cur) if (p <= t0 if side == "b" else p >= t0)),
                        reverse=(side == "b"))
        out = []
        for p in levels:
            pre = first[p] if p in first else cur.get(p, 0)
            if pre <= 0:
                continue
            c = dec.get(p, 0)
            if c <= 0:
                break
            out.append((p, c))
            if c < pre:
                break
        return out

    def cross_check(self, t):
        """Where the opposite side now reaches a resting order's price, the orders there would have been takers
        against it: one crossing event, at t plus the taker delay, for their displayed size, in a variant that
        counts them."""
        bb, ba = self.best("b"), self.best("a")
        for v in self.vs:
            if not v.cross:
                continue
            for o in v.resting:
                if o.state != "resting" or o.xing:
                    continue
                c = 0
                if o.side == "b" and ba is not None and ba <= o.p:
                    c = sum(s for p, s in self.asks.items() if p <= o.p)
                elif o.side == "a" and bb is not None and bb >= o.p:
                    c = sum(s for p, s in self.bids.items() if p >= o.p)
                if c > 0:
                    o.xing = True
                    v._push(t + TAKER_DELAY_NS, CROSS, o, c)
                    v.n["crossings"] += 1

    def close_block(self, match):
        """The entries sharing one venue stamp end. Where the Up token's book frame with that stamp closes them they
        are a match: every resting order its sweep reaches fills. Then every resting order's queue ahead is held at
        most at its level's displayed size, and the book is checked for crossings."""
        pre, took = {}, {}
        for sd, p, old, _new in self.block:
            pre.setdefault((sd, p), old)
        if match and self.block:
            hit = 0
            for side, t0 in (("b", self.touch0[0]), ("a", self.touch0[1])):
                if t0 is None:
                    continue
                sw = self.sweep(side, t0)
                if not sw:
                    continue
                hit += 1
                last = sw[-1][0]
                at = dict(sw)
                for p, c in sw:
                    took[(side, p)] = c
                for v in self.vs:
                    gone = False
                    for o in v.resting:
                        if o.side != side or o.state != "resting":
                            continue
                        f = 0
                        if (last <= o.p) if side == "b" else (last >= o.p):
                            tot = sum(c for p, c in sw if (p <= o.p if side == "b" else p >= o.p))
                            f = min(o.s, max(0, tot - o.q))
                        o.q = max(0, o.q - at.get(o.p, 0))
                        if f > 0:
                            o.s -= f
                            v.fill(self.bvt, side, o.p, f, "m")
                            if o.s == 0:
                                o.state, o.done_at, gone = "filled", self.bvt, True
                    if gone:
                        v.resting = [o for o in v.resting if o.state == "resting"]
            if hit:
                self.c["matches"] += 1
            if hit == 2:
                self.c["two_sided"] += 1
        for v in self.vs:
            for o in v.resting:
                lv = (self.bids if o.side == "b" else self.asks).get(o.p, 0)
                if v.prop and (o.side, o.p) in pre:
                    left = pre[(o.side, o.p)] - took.get((o.side, o.p), 0)
                    if left > lv and o.q > 0:
                        o.q = o.q * lv // left
                if lv < o.q:
                    o.q = lv
        t = self.bvt
        self.block, self.bvt = [], None
        self.cross_check(t)

    # -- the stream's items, as the replay hands them over --------------------------------------------------------

    def entries(self, vt_ns, ents):
        """The Up token's price_change entries of one frame: each sets or removes one level."""
        assert not self.block or vt_ns == self.bvt, "entries of another stamp inside a block"
        if not self.block:
            self.bvt = vt_ns
            self.touch0 = (self.best("b"), self.best("a"))
        for side, p, s in ents:
            bk = self.bids if side == "b" else self.asks
            old = bk.get(p, 0)
            if s == 0:
                bk.pop(p, None)
            else:
                bk[p] = s
            self.block.append((side, p, old, s))

    def book(self, vt_ns, bids, asks, seed):
        """A book frame of the Up token. A subscription's frame seeds the book; any other closes the block it shares
        a stamp with as a match, is compared with the book rebuilt to it, and replaces it."""
        if seed:
            if self.block:
                self.close_block(False)
            self.seeded = True
        else:
            self.c["snapshots"] += 1
            if self.block:
                self.close_block(vt_ns == self.bvt)
            if bids == self.bids and asks == self.asks:
                self.c["snapshots_equal"] += 1
                self.c["touch_equal"] += 1
            elif touch_of(bids, asks) == touch_of(self.bids, self.asks):
                self.c["touch_equal"] += 1
        self.bids, self.asks = bids, asks
        for v in self.vs:
            for o in v.resting:
                lv = (self.bids if o.side == "b" else self.asks).get(o.p, 0)
                if lv < o.q:
                    o.q = lv
        self.cross_check(vt_ns)

    def session(self, kind, h):
        """connect and subscribe empty the book until the subscription's frame; a close that is not the stream's end
        takes every live order off, the cancels reaching the venue at h + L."""
        if self.block:
            self.close_block(False)
        if kind in ("connect", "subscribe"):
            self.bids, self.asks, self.seeded = {}, {}, False
            if kind == "subscribe":
                self.c["sessions"] += 1
        elif kind == "close":
            self.c["closes"] += 1
            for v in self.vs:
                for side in ("b", "a"):
                    o = v.live[side]
                    if o is not None:
                        v.cancel(h, o)
                        v.live[side] = None

    def stop(self):
        """The host's timer at T0 + stop: every live order of every variant cancelled at that instant, the cancels
        reaching the venue L later; no quote after it."""
        for v in self.vs:
            for side in ("b", "a"):
                o = v.live[side]
                if o is not None:
                    v.cancel(self.stop_ns, o)
                    v.live[side] = None
        self.stopped = True

    def decide(self, h):
        """Every variant's quotes, after a frame of the leg's market reaches the host at h (TZ-32 section 1)."""
        pm = self.pm
        if self.stopped or not self.seeded or h < self.start_ns:
            return
        bb, ba = self.best("b"), self.best("a")
        for v in self.vs:
            x = None
            for side in ("b", "a"):
                o = v.live[side]
                if o is not None and o.done_at is not None and o.done_at + v.L <= h:
                    o = v.live[side] = None
                tgt = None
                if bb is not None and ba is not None:
                    tgt = bb if side == "b" else ba
                    if not pm["p_lo"] <= tgt <= pm["p_hi"]:
                        tgt = None
                if tgt is not None:
                    if x is None:
                        x = v.known_x(h)
                    if x >= pm["x_cap"] if side == "b" else x <= -pm["x_cap"]:
                        tgt = None
                if tgt is None:
                    if o is not None:
                        v.cancel(h, o)
                        v.live[side] = None
                elif o is None:
                    v.live[side] = v.send(h, side, tgt, pm["size"])
                elif o.p != tgt:
                    v.cancel(h, o)
                    v.live[side] = v.send(h, side, tgt, pm["size"])

    def finish(self):
        if self.block:
            self.close_block(False)
        self.resolve(1 << 62)


# A price_change frame as the venue sends it and the pair book stores it, matched whole: two entries, each field a
# run of digits, hex or BUY/SELL, where no escape can occur (TZ-30's PC_LINE, its fields kept for the Up token).
_ENTRY = (r'\{\\"asset_id\\":\\"([0-9]+)\\", \\"price\\":\\"([0-9.]+)\\", \\"size\\":\\"([0-9.]+)\\", '
          r'\\"side\\":\\"(BUY|SELL)\\", \\"hash\\":\\"[0-9a-f]*\\", \\"best_bid\\":\\"[0-9.]+\\", '
          r'\\"best_ask\\":\\"[0-9.]+\\"\}')
PC_LINE = re.compile(r'\{"recv_ns":([0-9]+),"mono_ns":-?[0-9]+,"raw":"\{\\"market\\":\\"(0x[0-9a-f]{64})\\", '
                     r'\\"price_changes\\":\[' + _ENTRY + ', ' + _ENTRY + r'\], \\"timestamp\\":\\"([0-9]+)\\", '
                     r'\\"event_type\\":\\"price_change\\"\}"\}\n?')


def touch_of(bids, asks):
    """A book's touch: the best bid and its size, the best ask and its size, None for an empty side."""
    bb = max(bids) if bids else None
    ba = min(asks) if asks else None
    return bb, bids.get(bb), ba, asks.get(ba)


def side_of(levels):
    """A side of a book frame: every level by its price, a later one replacing an earlier, then those of size 0
    removed (TZ-30's rule)."""
    out = {}
    for lv in levels:
        out[price_int(lv["price"])] = size_int(lv["size"])
    return {p: s for p, s in out.items() if s}


def replay(paths, w, cond, up_token, lag):
    """Every line of the window's stream files, in the order stored, into the Window `w`, the five-minute leg's
    market alone: the host's stop timer fires before the first line received at or after T0 + stop, and the end of
    each file takes every live order off as a close does. Returns the counts of lines read; `lag` gathers, for every
    price_change frame of the leg, its host receipt less its venue stamp in whole milliseconds."""
    n = {"lines": 0, "frames": 0, "leg_frames": 0, "skipped": 0}
    fast = PC_LINE.fullmatch
    last_h = 0
    _SIZES.clear()
    for path in paths:
        with gzip.open(path, "rt", encoding="utf-8") as fh:
            for line in fh:
                n["lines"] += 1
                mt = fast(line)
                if mt is not None:
                    n["frames"] += 1
                    g = mt.groups()
                    h = last_h = int(g[0])
                    if not w.stopped and h >= w.stop_ns:
                        w.stop()
                    if g[1] != cond:
                        continue
                    n["leg_frames"] += 1
                    ms = int(g[10])
                    vt = ms * MS_NS
                    lag[h // MS_NS - ms] = lag.get(h // MS_NS - ms, 0) + 1
                    ents = [("b" if g[j + 3] == "BUY" else "a", price_int(g[j + 1]), size_int(g[j + 2]))
                            for j in (2, 6) if g[j] == up_token]
                    assert len(ents) == 1, "a price_change frame of the leg without one Up entry"
                    w.advance(vt)
                    w.entries(vt, ents)
                    w.decide(h)
                    continue
                if not line.strip():
                    continue
                o = json.loads(line)
                h = o.get("recv_ns")
                assert type(h) is int, "a line without its host receipt"
                last_h = max(last_h, h)
                if not w.stopped and h >= w.stop_ns:
                    w.stop()
                if "event" in o:
                    ev = o["event"]
                    if ev in ("connect", "subscribe") or (ev == "close" and o.get("reason") != "end"):
                        w.session(ev, h)
                    continue
                raw = o.get("raw")
                if raw is None or raw == "PONG":
                    n["skipped"] += 1
                    continue
                try:
                    fr = json.loads(raw)
                except ValueError:
                    n["skipped"] += 1
                    continue
                n["frames"] += 1
                mine = False
                for it in (fr if isinstance(fr, list) else (fr,)):
                    if not isinstance(it, dict) or it.get("market") != cond:
                        continue
                    mine = True
                    et = it.get("event_type")
                    if et == "book":
                        if it.get("asset_id") != up_token:
                            continue
                        vt = int(it["timestamp"]) * MS_NS
                        w.advance(vt)
                        w.book(vt, side_of(it["bids"]), side_of(it["asks"]), isinstance(fr, list))
                    elif et == "price_change":
                        ms = int(it["timestamp"])
                        vt = ms * MS_NS
                        lag[h // MS_NS - ms] = lag.get(h // MS_NS - ms, 0) + 1
                        ents = [("b" if pc["side"] == "BUY" else "a", price_int(pc["price"]), size_int(pc["size"]))
                                for pc in it["price_changes"] if pc["asset_id"] == up_token]
                        w.advance(vt)
                        w.entries(vt, ents)
                if mine:
                    n["leg_frames"] += 1
                    w.decide(h)
        w.session("close", last_h)
    w.finish()
    return n

# ---- a member's money: TZ-23's aggregate on our own fills --------------------------------------------------------

FLIP = {"b": "S", "a": "B"}      # a fill of our bid is a taker selling Up into it; a fill of our ask, a taker buying
LIFE_BANDS = ("pre", "w0", "w1", "w2", "w3", "last", "post")
UNIT_BANDS = ("w0", "w1", "w2", "w3", "last")
E12 = D("0.000000000001")


def x12(x):
    """An exact figure as fixed-point text with exactly twelve decimals, the unit's one form of a number; a figure
    with more decimals is a failed assert."""
    q = x.quantize(E12)
    assert q == x, "a figure of more than twelve decimals: %s" % x
    s = fx(q)
    return s[1:] if s.startswith("-") and q == 0 else s


def own_rows(fills):
    """Our fills as TZ-23's aggregate reads a taker's row, in Up shares: its maker_terms on the taker's side give our
    own position - our bid filled, +s Up at p; our ask filled, -s Up at p - and its rebate 0.014 s p (1 - p)."""
    return [[vt // 10 ** 9, FLIP[side], "U", fx(D(f) / SIZE_UNIT), fx(D(p) / PRICE_UNIT)]
            for vt, side, p, f, _kind in fills]


def sums_of(t0, fills):
    """A variant's sums over a member, by band and over its life - every fill before T0 + 300; a fill outside
    [T0, T0 + 300) is a failed assert."""
    bands, _win = tz23.aggregate(t0, own_rows(fills))
    assert bands["pre"]["n"] == 0 and bands["post"]["n"] == 0, "a fill of ours outside [T0, T0 + 300)"
    life = tz23.zero()
    for name in LIFE_BANDS:
        for k in life:
            life[k] += bands[name][k]
    return life, bands


def lag_quantiles(hist):
    """Of a histogram of whole milliseconds: the count, the nearest-rank 50th, 90th and 99th percentiles, the least
    and the largest, in integers alone."""
    n = sum(hist.values())
    if n == 0:
        return 0, None, None, None, None, None
    ks = sorted(hist)
    ranks = [-(-q * n // 100) for q in (50, 90, 99)]
    got, c = [], 0
    for k in ks:
        c += hist[k]
        while len(got) < 3 and c >= ranks[len(got)]:
            got.append(k)
    return n, got[0], got[1], got[2], ks[0], ks[-1]


def make_variants():
    return [Variant(name, L, front=fr, prop=pr, cross=cr) for name, L, fr, pr, cr in VARIANTS]


def sums_line(z):
    return "n %d sh %s X %s C %s R %s" % (z["n"], x12(z["sh"]), x12(z["X"]), x12(z["C"]), x12(z["R"]))


def member_unit(m, paths):
    """A member's lines, label-free: every variant's messages and sums over the leg's life, by band and by the kind of
    fill, the book's match frames against the rebuilt book, the frames read, the lag, and every fill of every
    variant."""
    T = m["T"]
    w = Window(T, PARAMS, make_variants())
    lag = {}
    n = replay(paths, w, m["condition"], m["up"], lag)
    lines = ["%d member leg %d files %d bytes %d" % (T, T + LEG, len(m["files"]), sum(f["bytes"] for f in m["files"]))]
    for v in w.vs:
        life, bands = sums_of(T + LEG, v.fills)
        lines.append("%d variant %s sent %d cancels %d refused %d crossings %d %s" % (
            T, v.name, v.n["sent"], v.n["cancels"], v.n["refused"], v.n["crossings"], sums_line(life)))
        for b in UNIT_BANDS:
            lines.append("%d band %s %s %s" % (T, v.name, b, sums_line(bands[b])))
        for kind in ("m", "x"):
            kl, _kb = sums_of(T + LEG, [f for f in v.fills if f[4] == kind])
            lines.append("%d kind %s %s %s" % (T, v.name, kind, sums_line(kl)))
    c = w.c
    lines.append("%d book snapshots %d equal %d touch_equal %d matches %d two_sided %d sessions %d closes %d" % (
        T, c["snapshots"], c["snapshots_equal"], c["touch_equal"], c["matches"], c["two_sided"], c["sessions"],
        c["closes"]))
    lines.append("%d frames lines %d frames %d leg %d skipped %d" % (T, n["lines"], n["frames"], n["leg_frames"],
                                                                    n["skipped"]))
    lines.append("%d lag frames %s p50 %s p90 %s p99 %s min %s max %s" % ((T,) + lag_quantiles(lag)))
    for v in w.vs:
        for vt, side, p, f, kind in v.fills:
            lines.append("%d fill %s %d %s %d %d %s" % (T, v.name, vt // MS_NS, side, p, f, kind))
    return lines


def parse_sums(f, i):
    """Five fields of a sums_line starting at f[i]: n, sh, X, C, R."""
    assert f[i::2][:5] == ["n", "sh", "X", "C", "R"], "a sums field %r" % f[i:]
    return {"n": int(f[i + 1]), "sh": D(f[i + 3]), "X": D(f[i + 5]), "C": D(f[i + 7]), "R": D(f[i + 9])}


def parse_unit(T, text):
    """A member's unit file, read back: every variant's sums over the life, by band and by kind, the book's counts
    and the lag. Asserts the file is the member's and whole."""
    rows = text.split("\n")
    assert rows[-1] == "" and rows[0].startswith("%d member " % T), "unit %d: not whole" % T
    got = {"T": T, "variants": {}, "bands": {}, "kinds": {}}
    names = [v[0] for v in VARIANTS]
    for ln in rows[:-1]:
        f = ln.split(" ")
        assert int(f[0]) == T, "unit %d: a line of %s" % (T, f[0])
        if f[1] == "variant":
            assert f[3:11:2] == ["sent", "cancels", "refused", "crossings"], "unit %d: a variant line" % T
            z = parse_sums(f, 11)
            z.update({"sent": int(f[4]), "cancels": int(f[6]), "refused": int(f[8]), "crossings": int(f[10])})
            got["variants"][f[2]] = z
        elif f[1] == "band":
            got["bands"][(f[2], f[3])] = parse_sums(f, 4)
        elif f[1] == "kind":
            got["kinds"][(f[2], f[3])] = parse_sums(f, 4)
        elif f[1] == "book":
            kv = dict(zip(f[2::2], f[3::2]))
            got["book"] = {k: int(v) for k, v in kv.items()}
        elif f[1] == "lag":
            got["lag"] = {k: (None if v == "None" else int(v)) for k, v in zip(f[2::2], f[3::2])}
    assert sorted(got["variants"]) == sorted(names) and "book" in got and "lag" in got and \
        len(got["bands"]) == len(names) * len(UNIT_BANDS) and len(got["kinds"]) == 2 * len(names), \
        "unit %d: incomplete" % T
    return got

# ---- units: one window held to the idle stretch, its streams downloaded, replayed and removed -----------------


def stream_index(name):
    m = re.fullmatch(r"stream(?:\.([1-9][0-9]*))?\.jsonl\.gz", name)
    assert m, "a stream file named %r" % name
    return int(m.group(1) or 0)


def run_unit(T, files, dl_dir, replay_fn, timing, holdf=hold, dl=download):
    """One window: started where `holdf` allows, its stream files downloaded and verified by bytes and SHA-256,
    replayed by `replay_fn`, and removed whatever the replay did; its start and end written to `timing`."""
    nbytes = sum(f["bytes"] for f in files)
    budget = 5 + -(-nbytes // DL_RATE) + UNIT_BUDGET_S
    start, waited = holdf(budget)
    free = free_bytes()
    assert free - nbytes >= DISK_FLOOR, "BLOCKED: %d bytes free, %d to download, the floor %d" % (free, nbytes,
                                                                                                  DISK_FLOOR)
    os.makedirs(dl_dir, exist_ok=True)
    paths, retries = [], 0
    t0 = time.time()
    try:
        for f in sorted(files, key=lambda f: stream_index(f["file"])):
            dest = os.path.join(dl_dir, f["asset"])
            _n, _secs, k = dl(f["tag"], f["asset"], f["bytes"], f["sha256"], dest)
            retries += k
            paths.append(dest)
        t1, c1 = time.time(), time.process_time()
        lines = replay_fn(paths)
        cpu = time.process_time() - c1
    finally:
        for p in paths:
            if os.path.exists(p):
                os.remove(p)
    end = time.time()
    W = int(start) // WINDOW * WINDOW
    rec = {"T": T, "window": W, "start_second": round(start - W, 3), "end_second": round(end - W, 3),
           "waited_s": round(waited, 3), "download_s": round(t1 - t0, 3), "replay_s": round(end - t1, 3),
           "cpu_s": round(cpu, 3), "bytes": nbytes, "retries": retries, "budget_s": budget,
           "inside": end <= W + IDLE[1]}
    with open(timing, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, sort_keys=True) + "\n")
    return lines, rec


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
            r["T"], r["start_second"], r["window"], r["end_second"]))
    return recs, outside


def replay_units(members, udir, timing, cpu_max, dl_dir, unit_fn=run_unit, project_after=PROJECT_AFTER):
    """Every member's unit not already on disk; after the first `project_after` of this run, the replays' processor
    time projected over every member's bytes, BLOCKED above cpu_max."""
    os.makedirs(udir, exist_ok=True)
    total = sum(f["bytes"] for m in members for f in m["files"])
    t0, done, cpu, nb = time.time(), 0, 0.0, 0
    out("units to replay %d, %d bytes of streams in all" % (len(members), total))
    for m in members:
        path = os.path.join(udir, "%d.txt" % m["T"])
        if os.path.exists(path):
            continue
        unit, rec = unit_fn(m["T"], m["files"], dl_dir, lambda paths, m=m: member_unit(m, paths), timing)
        write_atomic(path, ("\n".join(unit) + "\n").encode("utf-8"))
        done += 1
        cpu += rec["cpu_s"]
        nb += rec["bytes"]
        if done == project_after:
            proj = cpu / nb * total
            out("projected %.0f s of replay for %d bytes after %d units at %.4f s a megabyte" % (
                proj, total, done, cpu / nb * 1e6))
            assert proj <= cpu_max, "BLOCKED: replay projected at %.0f s, above %d" % (proj, cpu_max)
        if done % 24 == 0:
            out("units %d this run, %.0f s" % (done, time.time() - t0))


def concat_units(members, udir, path):
    """The members' unit files, read back in order and concatenated into `path`, written once: [parsed unit]."""
    rows, h, nlines = [], hashlib.sha256(), 0
    with open(path + ".new", "wb") as wfh:
        for m in members:
            with open(os.path.join(udir, "%d.txt" % m["T"]), "rb") as fh:
                data = fh.read()
            rows.append(parse_unit(m["T"], data.decode("utf-8")))
            h.update(data)
            nlines += data.count(b"\n")
            wfh.write(data)
    sha = h.hexdigest()
    if os.path.exists(path):
        os.remove(path + ".new")
        assert sha256_file(path) == sha, "determinism: %s differs from the first run" % path
        out("unchanged %s sha256 %s" % (path, sha))
    else:
        os.replace(path + ".new", path)
        out("wrote %s %d bytes sha256 %s" % (path, os.path.getsize(path), sha))
    return rows, sha, nlines

# ---- the gate: TZ-23's thresholds on each gated variant, and W1's reading -------------------------------------


def variant_sums(rows):
    """Over the members: each variant's fills, shares, X, C and R summed, V the sum of X squared, the members with a
    fill, and its messages."""
    tot = {}
    for name, *_ in VARIANTS:
        t = {"n": 0, "sh": D(0), "X": D(0), "C": D(0), "R": D(0), "V": D(0), "members_with_fills": 0, "sent": 0,
             "cancels": 0, "refused": 0, "crossings": 0}
        for r in rows:
            v = r["variants"][name]
            for k in ("n", "sh", "X", "C", "R", "sent", "cancels", "refused", "crossings"):
                t[k] += v[k]
            t["V"] += v["X"] * v["X"]
            t["members_with_fills"] += 1 if v["n"] else 0
        tot[name] = t
    return tot


def gate_of(name, t):
    return tz23.gate_constants(t["V"], t["sh"], lam=LAMBDA[name], alpha=ALPHA, delta=DELTA)


def book_reading(snapshots, touch_equal):
    """G-BOOK: PASS where the touch rebuilt from the leg's entries - the best bid and its size, the best ask and its
    size - equals the venue's own book frame's at no fewer than BOOK_EQUAL_MIN of the match frames read."""
    return "PASS" if snapshots > 0 and D(touch_equal) >= BOOK_EQUAL_MIN * snapshots else "FAIL"


def w1_reading(res):
    """W1's word from the two gated variants' own TZ-23 readings: W1-EARN where `behind` reaches its EARN bound,
    else W1-NO-EARN where `front` reaches its NO EARN bound, else UNDECIDABLE."""
    if res["behind"]["earn"]:
        return "W1-EARN"
    if res["front"]["no_earn"]:
        return "W1-NO-EARN"
    return "UNDECIDABLE"


def build_constants(s, rows, label, base):
    """Label-free: every variant's sums over the set, G-BOOK's counts, the capture's lag, and each gated variant's
    thresholds and power; the constants file written once."""
    tot = variant_sums(rows)
    bk = {k: sum(r["book"][k] for r in rows) for k in rows[0]["book"]}
    lg = [r["lag"] for r in rows if r["lag"]["frames"]]
    p50s, p99s = sorted(x["p50"] for x in lg), sorted(x["p99"] for x in lg)
    lagd = {"members": len(lg), "frames": sum(x["frames"] for x in lg), "p50_median": p50s[(len(p50s) - 1) // 2],
            "p99_median": p99s[(len(p99s) - 1) // 2], "p99_max": p99s[-1], "max": max(x["max"] for x in lg),
            "min": min(x["min"] for x in lg), "p99_above_1000": sum(1 for v in p99s if v > 1000)}
    gates = {g: gate_of(g, tot[g]) for g in GATED}
    const = {"label": label, "members": len(rows), "first": rows[0]["T"], "last": rows[-1]["T"],
             "member_list_sha": sha256_bytes(("\n".join(str(r["T"]) for r in rows) + "\n").encode()),
             "variants": tot, "gates": gates, "book": bk, "g_book": book_reading(bk["snapshots"], bk["touch_equal"]),
             "lag": lagd, "params": PARAMS, "variants_def": [list(v) for v in VARIANTS], "set_sha": s.get("sha")}
    path = os.path.join(base, "%s-constants.json" % label)
    sha = write_once(path, dumps(const).encode("utf-8"))
    return const, sha


def show_constants(const):
    out("members %d, first %d %s, last %d %s; member list sha256 %s" % (
        const["members"], const["first"], utc(const["first"]), const["last"], utc(const["last"]),
        const["member_list_sha"]))
    bk = const["book"]
    out("G-BOOK %s: match frames %d, the rebuilt touch equal to the venue's at %d (%s); every level equal at %d (%s), "
        "barred; matches read %d, two-sided %d; sessions %d, closes %d" % (
            const["g_book"], bk["snapshots"], bk["touch_equal"], q12(D(bk["touch_equal"]) / max(bk["snapshots"], 1)),
            bk["equal"], q12(D(bk["equal"]) / max(bk["snapshots"], 1)), bk["matches"], bk["two_sided"],
            bk["sessions"], bk["closes"]))
    lg = const["lag"]
    out("the capture's lag, a price_change frame's host receipt less its venue stamp, over %d members and %d frames of "
        "the leg: the median member's median %d ms; its 99th percentile %d ms at the median member and %d ms at the "
        "worst, above 1,000 ms at %d members; the longest %d ms, the least %d ms" % (
            lg["members"], lg["frames"], lg["p50_median"], lg["p99_median"], lg["p99_max"], lg["p99_above_1000"],
            lg["max"], lg["min"]))
    for name, *_ in VARIANTS:
        t = const["variants"][name]
        out("%s%s: sent %d, cancels %d, refused %d, crossings %d; members with a fill %d; fills %d, shares %s, X %s, "
            "C %s, R %s, V %s" % (name, "" if name in GATED else ", barred from every reading", t["sent"],
                                  t["cancels"], t["refused"], t["crossings"], t["members_with_fills"], t["n"],
                                  fx(t["sh"]), fx(t["X"]), fx(t["C"]), fx(t["R"]), fx(t["V"])))
    for g in GATED:
        c = const["gates"][g]
        out("%s: V %s; Sh %s; lambda %s; L %s; thr %s (%s a share)" % (
            g, fx(c["V"]), fx(c["sh"]), fx(c["lambda"]), q12(c["L"]), q12(c["thr"]),
            q12(c["thr_per_share"]) if "thr_per_share" in c else "-"))
        out("%s: EARN at S >= %s; NO EARN at S <= %s (%s a share); power %s" % (
            g, q12(c["earn_at"]), q12(c["no_earn_at"]),
            q12(c["no_earn_per_share"]) if "no_earn_per_share" in c else "-", fx(c["power"])))
    out("W1 reads W1-EARN on behind's EARN bound and W1-NO-EARN on front's NO EARN bound (TZ-32 section 4.5)")


def score_rows(s, rows, const, label, base):
    """The labels, read once from the set's own documents; each variant's money, by member and band; each gated
    variant's TZ-23 reading and W1's."""
    ups = {m["T"]: tz23.label_of(m["doc"]) for m in s["members"]}
    assert sorted(ups) == [r["T"] for r in rows], "score: the members are not the units'"
    res = {"label": label, "members": len(rows), "ups": sum(ups.values()), "variants": {}}
    lines = ["T,up," + ",".join("S_%s" % name for name, *_ in VARIANTS)]
    per = {name: [] for name, *_ in VARIANTS}
    for r in rows:
        up = ups[r["T"]]
        cells = [str(r["T"]), str(up)]
        for name, *_ in VARIANTS:
            v = r["variants"][name]
            m = v["X"] * up - v["C"] + v["R"]
            per[name].append(m)
            cells.append(fx(m))
        lines.append(",".join(cells))
    for name, *_ in VARIANTS:
        t = const["variants"][name]
        X, C, R, sh = D(t["X"]), D(t["C"]), D(t["R"]), D(t["sh"])
        settle = sum((r["variants"][name]["X"] * ups[r["T"]] for r in rows), D(0)) - C
        S = settle + R
        bands = {}
        for b in ("w0", "w1", "w2", "w3", "last"):
            bs = bsh = D(0)
            for r in rows:
                z = r["bands"][(name, b)]
                bs += z["X"] * ups[r["T"]] - z["C"] + z["R"]
                bsh += z["sh"]
            bands[b] = {"S": bs, "sh": bsh, "per_share": bs / bsh if bsh else None}
        kinds = {}
        for kd in ("m", "x"):
            ks = ksh = D(0)
            for r in rows:
                z = r["kinds"][(name, kd)]
                ks += z["X"] * ups[r["T"]] - z["C"] + z["R"]
                ksh += z["sh"]
            kinds[kd] = {"S": ks, "sh": ksh, "per_share": ks / ksh if ksh else None}
        pm = sorted(per[name])
        e = {"S": S, "settlement": settle, "rebate": R, "sh": sh, "per_share": S / sh if sh else None,
             "settlement_per_share": settle / sh if sh else None, "rebate_per_share": R / sh if sh else None,
             "bands": bands, "kinds": kinds, "member_min": pm[0], "member_median": pm[(len(pm) - 1) // 2],
             "member_max": pm[-1], "members_above": sum(1 for x in pm if x > 0),
             "members_below": sum(1 for x in pm if x < 0)}
        if name in GATED:
            c = const["gates"][name]
            word, earn, no_earn = tz23.reading(S, {"earn_at": D(c["earn_at"]), "no_earn_at": D(c["no_earn_at"])})
            e.update({"word": word, "earn": earn, "no_earn": no_earn, "margin_earn": S - D(c["earn_at"]),
                      "margin_no_earn": D(c["no_earn_at"]) - S})
        res["variants"][name] = e
    res["reading"] = w1_reading(res["variants"]) if const["g_book"] == "PASS" else None
    sc = os.path.join(base, "%s-scored.csv" % label)
    res["scored_sha"] = write_once(sc, ("\n".join(lines) + "\n").encode("utf-8"))
    rp = os.path.join(base, "%s-reading.json" % label)
    res["reading_sha"] = write_once(rp, dumps(res).encode("utf-8"))
    out("labels: %d members, %d Up" % (len(rows), res["ups"]))
    for name, *_ in VARIANTS:
        e = res["variants"][name]
        out("%s%s: S %s = settlement %s + rebate %s on %s shares; per share %s = %s + %s" % (
            name, "" if name in GATED else ", barred from every reading", q12(e["S"]), q12(e["settlement"]),
            q12(e["rebate"]), fx(e["sh"]), q12(e["per_share"]) if e["per_share"] is not None else "-",
            q12(e["settlement_per_share"]) if e["per_share"] is not None else "-",
            q12(e["rebate_per_share"]) if e["per_share"] is not None else "-"))
        if name in GATED:
            out("%s: %s; EARN %s (margin %s); NO EARN %s (margin %s)" % (
                name, e["word"], e["earn"], q12(e["margin_earn"]), e["no_earn"], q12(e["margin_no_earn"])))
        for b, z in e["bands"].items():
            if z["sh"]:
                out("barred: %s band %-4s shares %s, S %s, per share %s" % (name, b, fx(z["sh"]), q12(z["S"]),
                                                                           q12(z["per_share"])))
        for kd, z in e["kinds"].items():
            if z["sh"]:
                out("barred: %s fills %s shares %s, S %s, per share %s" % (
                    name, "at a match" if kd == "m" else "against a crossing order", fx(z["sh"]), q12(z["S"]),
                    q12(z["per_share"])))
        out("barred: %s per member S min %s, median %s, max %s; above zero %d, below %d" % (
            name, q12(e["member_min"]), q12(e["member_median"]), q12(e["member_max"]), e["members_above"],
            e["members_below"]))
    out("the score's files: %s sha256 %s; %s sha256 %s" % (sc, res["scored_sha"], rp, res["reading_sha"]))
    return res

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
        out("%-44s %6d lines %8d bytes %s %s%s" % (path, got[0], got[1], got[2], state,
                                                  " equal" if state == "frozen" else ""))
    assert any(r[0] == "research/" + TZ23_NAME and r[3] == "frozen" and r[4] == TZ23_SHA256 for r in rows), \
        "%s: not the map's frozen row" % TZ23_NAME
    with open(os.path.join(PRIMARY, "research", TZ23_NAME), "rb") as fh:
        t23 = sha256_bytes(fh.read())
    assert t23 == TZ23_SHA256, "the primary checkout's %s sha256 %s" % (TZ23_NAME, t23)
    out("SYSTEM-MAP.md %d lines %d bytes sha256 %s" % (raw.count(b"\n"), len(raw), sha256_bytes(raw)))
    out("FINGERPRINT PASS: revision %s; anchors 6 of 6, 4 re-derived; rows %d: frozen %d of %d equal, tracked %d, "
        "reported %d; %s is the file this instrument loads, a frozen row" % (
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
    """The archive's own record, read whole: its complete lines, each printed, its runs summarized, every complete
    run's set.json asserted by its set record's SHA-256, and the windows its assets reach."""
    for unit in (ARCHIVE_TIMER, ARCHIVE_UNIT):
        out("%s %s" % (unit, show(unit, ["ActiveState", "SubState", "UnitFileState", "Result", "ExecMainStatus",
                                         "LastTriggerUSec", "NextElapseUSecRealtime"])))
    raw, recs, tail = ledger_records()
    out("ledger %s: %d bytes sha256 %s, %d complete records, %d bytes of a line still written" % (
        ARCHIVE_LEDGER, len(raw), sha256_bytes(raw), len(recs), len(tail)))
    for r in recs:
        out("L %s %s" % (utc(r["wall_ns"] / 1e9), json.dumps(r, sort_keys=True)))
    summ = ledger_summary(recs)
    for ln in summ["lines"]:
        out(ln)
    sets = archived_sets(recs)
    amap = asset_map(sets)
    for s in sets:
        ts = sorted(x["T"] for x in s["doc"]["assets"])
        out("set %s run %d sha256 %s: %d files, %d bytes, windows %s to %s" % (
            s["tag"], s["run"], s["sha256"], s["doc"]["assets_n"], s["doc"]["bytes_total"], ts[0] if ts else "-",
            ts[-1] if ts else "-"))
    after = sorted(t for t in amap if t >= FIRST_T)
    out("the archive's assets: %d windows, %d files, to window %d; at or after %d: %d windows, to %s" % (
        len(amap), sum(len(v) for v in amap.values()), max(amap), FIRST_T, len(after), after[-1] if after else "-"))
    tags = sorted(ln.split("\t")[1][len("refs/tags/"):] for ln in git(
        "ls-remote", "origin", "refs/tags/pairbook-streams-*", tree=PRIMARY).split("\n") if "\t" in ln)
    stags = [s["tag"] for s in sets]
    out("tags on origin %d: %s" % (len(tags), tags))
    out("complete runs' sets %d; their tags not on origin %s; halted %s; runs without a terminal record %s" % (
        len(stags), sorted(set(stags) - set(tags)), summ["halted"],
        [a for a, t in summ["terminal"].items() if not t]))


def rehearsal_members(base):
    """TZ-27's 51 windows, their legs' settled documents read by TZ-23's gamma_docs held to the idle stretch at every
    run, a later run's bytes the first's; every one a member, its condition and Up token its document's."""
    with open(TZ27_SET, "rb") as fh:
        raw = fh.read()
    assert sha256_bytes(raw) == TZ27_SET_SHA, "TZ-27's set.json in the forensic store"
    doc = json.loads(raw)
    assert doc["tag"] == TZ27_TAG and tuple(x["T"] for x in doc["assets"]) == REHEARSAL_TS and all(
        x["file"] == "stream.jsonl.gz" for x in doc["assets"]), "TZ-27's set: 51 windows, one file each"
    os.makedirs(base, exist_ok=True)
    got = docs_of(list(REHEARSAL_TS))
    by = {t: tz23.kept_doc(d) if d is not None else None for t, d in got.items()}
    write_once(os.path.join(base, "docs.json"), dumps({str(t): d for t, d in sorted(by.items())}).encode("utf-8"))
    members = []
    for x in doc["assets"]:
        t, d = x["T"], by.get(x["T"])
        why = tz23.qualify(t + LEG, d)
        assert why is None, "G-REHEARSAL: window %d's leg %s" % (t, why)
        tok = json.loads(d["clobTokenIds"])
        members.append({"T": t, "condition": d["conditionId"], "up": tok[0], "doc": d,
                        "files": [{"file": x["file"], "tag": TZ27_TAG, "asset": x["asset"], "bytes": x["bytes"],
                                   "sha256": x["sha256"]}]})
    return members


def rehearsal_figures(rows, ups):
    """The figures G-REHEARSAL compares beside the lines: each variant's fills, shares, X, C, R, V and S."""
    tot = variant_sums(rows)
    fig = {}
    for name, *_ in VARIANTS:
        t = tot[name]
        S = sum((r["variants"][name]["X"] * ups[r["T"]] for r in rows), D(0)) - t["C"] + t["R"]
        fig[name] = [t["n"], x12(t["sh"]), x12(t["X"]), x12(t["C"]), x12(t["R"]), x12(t["V"]), x12(S)]
    return fig


def mode_rehearse():
    floor_check()
    base = os.path.join(WORK, "rehearsal")
    members = rehearsal_members(base)
    udir, timing = os.path.join(base, "units"), os.path.join(base, "rehearsal-timing.jsonl")
    replay_units(members, udir, timing, REHEARSAL_CPU_MAX, os.path.join(WORK, "streams"))
    timing_summary(timing)
    rows, sha, nlines = concat_units(members, udir, os.path.join(base, "rehearsal-lines.txt"))
    ups = {m["T"]: tz23.label_of(m["doc"]) for m in members}
    fig = rehearsal_figures(rows, ups)
    checks = {"lines": nlines == REF["lines"], "digest": sha == REF["digest"]}
    for name, *_ in VARIANTS:
        checks["totals " + name] = fig[name] == REF["totals"].get(name)
        out("G-REHEARSAL %-8s %s; the Architect's %s" % (name, fig[name], REF["totals"].get(name)))
    out("G-REHEARSAL lines %d, the Architect's %d; sha256 %s, the Architect's %s" % (nlines, REF["lines"], sha,
                                                                                    REF["digest"]))
    bad = sorted(k for k, v in checks.items() if not v)
    assert not bad, "G-REHEARSAL FAIL: %s" % bad
    out("G-REHEARSAL PASS: %d of %d - %d lines byte for byte and %d variants' totals equal to the Architect's" % (
        len(checks), len(checks), nlines, len(VARIANTS)))


def mode_fetch():
    """The candidates from FIRST_T, once the archive has moved every one to LAST_T: each window's stream conditions
    from its window.json, then its leg's settled document by TZ-23's gamma_docs, held to the idle stretch, in
    requests of twenty and in order until NEED members (G-SET). No price of the store is read."""
    floor_check()
    amap, waited = wait_archive()
    out("the archive has moved windows to %d, at or after %d, after %.0f s waited" % (max(amap), LAST_T, waited))
    base = os.path.join(WORK, "set")
    os.makedirs(base, exist_ok=True)
    ts = list(range(FIRST_T, LAST_T + 1, WINDOW))
    wj, status = {}, {}
    for t in ts:
        try:
            wj[t] = window_json(t)
        except FileNotFoundError:
            wj[t] = None
        status[t] = stream_problem(wj[t], t, amap)
    considered, members, by = [], [], {}
    pending = [t for t in ts if status[t] is None]
    k = 0
    for t in ts:
        if len(members) == NEED:
            break
        if status[t] is None:
            if t not in by:
                chunk = pending[k:k + DOC_CHUNK]
                k += len(chunk)
                by.update(docs_of(chunk))
            why = leg_problem(wj[t], t, by.get(t))
            if why is None:
                d = by[t]
                tok = json.loads(d["clobTokenIds"])
                members.append({"T": t, "condition": d["conditionId"], "up": tok[0], "doc": tz23.kept_doc(d),
                                "files": [dict(amap[t][f], file=f) for f in wj[t]["stream"]["files"]]})
                status[t] = "member"
            else:
                status[t] = why
        considered.append([t, status[t]])
        assert len(considered) - len(members) <= NONMEMBER_MAX, \
            "BLOCKED: %d non-members before the %dth member" % (len(considered) - len(members), NEED)
    assert len(members) == NEED, "BLOCKED: %d members among the %d candidates" % (len(members), len(considered))
    mts = [m["T"] for m in members]
    s = {"first_T": FIRST_T, "need": NEED, "considered": considered, "members": members,
         "member_list_sha": sha256_bytes(("\n".join(map(str, mts)) + "\n").encode())}
    path = os.path.join(base, "w1-set.json")
    sha = write_once(path, dumps(s).encode("utf-8"))
    st = load_state()
    st["set_sha"], st["set_at"] = sha, utc(time.time())
    save_state(st)
    nb = sum(f["bytes"] for m in members for f in m["files"])
    out("G-SET PASS: %d members of %d considered, %d (%s) to %d (%s); %d stream files, %d bytes; member list sha256 "
        "%s; %s sha256 %s" % (len(members), len(considered), mts[0], utc(mts[0]), mts[-1], utc(mts[-1]),
                              sum(len(m["files"]) for m in members), nb, s["member_list_sha"], path, sha))
    out("document requests %d for %d windows" % (-(-k // DOC_CHUNK), k))
    out("non-members %d: %s" % (len(considered) - len(members),
                               json.dumps([[t, w] for t, w in considered if w != "member"])))
    days = {}
    for t in mts:
        d = time.strftime("%a", time.gmtime(t + LEG))
        days[d] = days.get(d, 0) + 1
    out("members by the weekday of their leg %s" % json.dumps(days, sort_keys=True))


def the_set():
    path = os.path.join(WORK, "set", "w1-set.json")
    st = load_state()
    sha = sha256_file(path)
    assert sha == st.get("set_sha"), "the set %s is not the one state.json records" % sha
    s = load_json(path)
    assert len(s["members"]) == NEED and s["first_T"] == FIRST_T, "the set"
    s["sha"] = sha
    return s


def mode_replay():
    """Label-free: every member's streams downloaded, replayed and removed, each unit held to the idle stretch; the
    units concatenated, and the constants - G-BOOK, the lag, every variant's sums, each gated variant's thresholds
    and power - written once, their SHA-256 in state.json."""
    floor_check()
    s = the_set()
    base = os.path.join(WORK, "replay")
    udir = os.path.join(base, "units")
    replay_units(s["members"], udir, os.path.join(base, "replay-timing.jsonl"), REPLAY_CPU_MAX,
                 os.path.join(WORK, "streams"))
    timing_summary(os.path.join(base, "replay-timing.jsonl"))
    rows, wsha, nlines = concat_units(s["members"], udir, os.path.join(base, "w1-units.txt"))
    out("units %d lines" % nlines)
    const, csha = build_constants(s, rows, "w1", base)
    show_constants(const)
    st = load_state()
    st["constants_sha"], st["units_sha"], st["constants_at"] = csha, wsha, utc(time.time())
    save_state(st)
    out("constants sha256 %s, units sha256 %s, in state.json" % (csha, wsha))


def mode_rescore():
    """Every RESCORE_EVERY-th member from a second download and a second replay; each unit file byte for byte the
    replay's (DETERMINISM)."""
    floor_check()
    s = the_set()
    chosen = s["members"][::RESCORE_EVERY]
    udir = os.path.join(WORK, "rescore", "units")
    replay_units(chosen, udir, os.path.join(WORK, "rescore", "rescore-timing.jsonl"), RESCORE_CPU_MAX,
                 os.path.join(WORK, "streams"), project_after=RESCORE_PROJECT_AFTER)
    timing_summary(os.path.join(WORK, "rescore", "rescore-timing.jsonl"))
    same = 0
    for m in chosen:
        a = sha256_file(os.path.join(WORK, "replay", "units", "%d.txt" % m["T"]))
        b = sha256_file(os.path.join(udir, "%d.txt" % m["T"]))
        same += a == b
        if a != b:
            out("rescore: %d differs, %s against %s" % (m["T"], a, b))
    assert same == len(chosen), "DETERMINISM FAIL: %d of %d" % (same, len(chosen))
    out("DETERMINISM PASS: %d of %d members' unit files byte for byte the replay's" % (same, len(chosen)))


def mode_score():
    floor_check()
    s = the_set()
    st = load_state()
    base = os.path.join(WORK, "replay")
    cpath = os.path.join(base, "w1-constants.json")
    assert sha256_file(cpath) == st.get("constants_sha"), "score: not the constants recorded"
    head = git("rev-parse", "HEAD")
    assert "origin/" + BRANCH in git("branch", "-r", "--contains", head).split(), \
        "score: HEAD %s is not on origin" % head
    const = load_json(cpath)
    assert const["member_list_sha"] == s["member_list_sha"] and const["set_sha"] == s["sha"], \
        "score: the constants are not the set's"
    rows, wsha, _n = concat_units(s["members"], os.path.join(base, "units"), os.path.join(base, "w1-units.txt"))
    assert wsha == st.get("units_sha"), "score: not the units recorded"
    with open(LEDGER, "a", encoding="utf-8") as fh:
        fh.write(dumps({"at": utc(time.time()), "head": head, "members": len(rows),
                        "member_list_sha": s["member_list_sha"], "constants_sha": st["constants_sha"]}))
    res = score_rows(s, rows, const, "w1", base)
    if res["variants"]["behind"]["earn"] and res["variants"]["front"]["no_earn"]:
        out("both bounds hold: behind reaches EARN and front NO EARN; the reading is W1-EARN (TZ-32 section 4.5)")
    assert const["g_book"] == "PASS", "G-BOOK FAIL: the reading is not read"
    out("W1 READING: %s" % res["reading"])


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

# ---- the self-test: literals, a synthetic window and temporary trees under the work tree -----------------------

SYN_T = 1792800000
SYN = {"m15": {"Up": "4001", "Down": "4002", "condition": "0x" + "a1" * 32},
       "m5": {"Up": "5001", "Down": "5002", "condition": "0x" + "b2" * 32}}


def _lv(levels):
    return [{"price": p, "size": s} for p, s in levels]


def _book(tok, cond, ts, bids, asks):
    """A book frame as the venue sends it: bids ascending, asks descending."""
    return {"market": cond, "asset_id": tok, "timestamp": str(ts), "hash": "0a", "event_type": "book",
            "bids": _lv(sorted(bids, key=lambda z: D(z[0]))), "asks": _lv(sorted(asks, key=lambda z: -D(z[0])))}


def _pc(cond, ts, entries):
    """A price_change frame in the venue's own key order: (token, side, price, size) entries, best bid and ask
    filler."""
    return {"market": cond, "price_changes": [{"asset_id": tok, "price": p, "size": s, "side": side, "hash": "0a1b",
                                               "best_bid": "0.5", "best_ask": "0.5"} for tok, side, p, s in entries],
            "timestamp": str(ts), "event_type": "price_change"}


def synth_frames(T=SYN_T, mp=SYN):
    """Two stream files of one window, every rule of TZ-32 section 1 met at least once: each entry is (host seconds
    after T, an event or a frame), the venue's stamps milliseconds after T * 1000."""
    c15, c5 = mp["m15"]["condition"], mp["m5"]["condition"]
    x, y, yc = mp["m15"]["Up"], mp["m5"]["Up"], mp["m5"]["Down"]
    v = lambda s: T * 1000 + int(round(s * 1000))

    def up(s, side, p, size):
        """A price_change of the leg: the Up entry and its Down mirror."""
        mirror = ("SELL" if side == "BUY" else "BUY", fx(1 - D(p)))
        return _pc(c5, v(s), [(y, side, p, size), (yc, mirror[0], mirror[1], size)])

    def other(s):
        return _pc(c15, v(s), [(x, "BUY", "0.40", "10"), (mp["m15"]["Down"], "SELL", "0.60", "10")])

    def books(s, yb, ya):
        return [_book(x, c15, v(s), [("0.40", "10")], [("0.60", "10")]),
                _book(mp["m15"]["Down"], c15, v(s), [("0.40", "10")], [("0.60", "10")]),
                _book(yc, c5, v(s), [("0.47", "1")], [("0.53", "1")]), _book(y, c5, v(s), yb, ya)]

    def session(t, b):
        return [(t, {"event": "connect", "seg": 0}), (t + 0.05, {"event": "open", "seg": 0, "status": 101}),
                (t + 0.1, {"event": "subscribe", "seg": 0}), (t + 0.3, b)]

    def bk(s, bids, asks):
        return _book(y, c5, v(s), bids, asks)

    first = session(594.9, books(595.15, [("0.47", "200"), ("0.48", "100")], [("0.53", "300"), ("0.52", "100")])) + [
        (599.000, up(598.990, "BUY", "0.46", "50")),
        (600.020, up(600.000, "SELL", "0.54", "40")),
        (601.020, up(601.000, "BUY", "0.48", "70")),
        (601.021, bk(601.000, [("0.48", "70"), ("0.47", "200"), ("0.46", "50")],
                     [("0.52", "100"), ("0.53", "300"), ("0.54", "40")])),
        (601.500, other(601.490)),
        (602.010, up(602.000, "BUY", "0.48", "0")),
        (602.011, up(602.000, "BUY", "0.47", "150")),
        (602.012, bk(602.000, [("0.47", "150"), ("0.46", "50")], [("0.52", "100"), ("0.53", "300"), ("0.54", "40")])),
        (603.000, up(602.990, "SELL", "0.52", "0")),
        (603.010, up(603.005, "BUY", "0.52", "25")),
        (603.100, up(603.090, "BUY", "0.46", "60")),
        (603.400, bk(603.300, [("0.52", "25"), ("0.47", "150"), ("0.46", "60")], [("0.53", "300"), ("0.54", "40")])),
        (605.000, up(604.995, "BUY", "0.52", "0")),
        (607.000, up(606.995, "BUY", "0.49", "40")),
        (607.020, up(607.010, "BUY", "0.49", "0")),
        (607.030, up(607.020, "SELL", "0.49", "15")),
        (607.300, up(607.290, "SELL", "0.49", "0")),
        (610.000, up(609.990, "BUY", "0.46", "61")),
        (610.200, up(610.190, "BUY", "0.47", "140")),
        (610.201, bk(610.190, [("0.47", "140"), ("0.46", "61")], [("0.53", "300"), ("0.54", "40")])),
        (610.400, up(610.390, "BUY", "0.46", "62")),
        (610.600, up(610.590, "BUY", "0.47", "130")),
        (610.601, bk(610.590, [("0.47", "130"), ("0.46", "62")], [("0.53", "300"), ("0.54", "40")])),
        (610.800, up(610.790, "BUY", "0.46", "63")),
        (611.000, up(610.990, "BUY", "0.47", "120")),
        (611.001, bk(610.990, [("0.47", "120"), ("0.46", "63")], [("0.53", "300"), ("0.54", "40")])),
        (611.200, up(611.190, "BUY", "0.46", "64")),
        (611.400, up(611.390, "BUY", "0.47", "110")),
        (611.401, bk(611.390, [("0.47", "110"), ("0.46", "64")], [("0.53", "300"), ("0.54", "40")])),
        (611.600, up(611.590, "BUY", "0.46", "65")),
        (620.000, up(619.990, "SELL", "0.96", "10")),
        (620.010, up(620.000, "SELL", "0.53", "0")),
        (620.020, up(620.010, "SELL", "0.54", "0")),
        (620.500, other(620.490)),
        (621.000, up(620.990, "SELL", "0.53", "20")),
        (650.000, {"event": "close", "seg": 0, "reason": "closed", "code": 1006})]
    second = session(651.0, books(651.25, [("0.45", "100"), ("0.46", "80")], [("0.55", "60"), ("0.54", "200")])) + [
        (651.500, up(651.490, "SELL", "0.54", "190")),
        (652.000, up(651.990, "SELL", "0.54", "150")),
        (652.001, bk(651.990, [("0.46", "80"), ("0.45", "100")], [("0.54", "150"), ("0.55", "60")])),
        (700.000, _pc(c5, v(699.990), [(y, "BUY", "0.46", "90"), (yc, "SELL", "0.54", "90"),
                                       (y, "BUY", "0.44", "30")])),
        (894.000, up(893.990, "BUY", "0.46", "95")),
        (895.0005, other(894.990)),
        (895.020, up(895.010, "BUY", "0.46", "0")),
        (895.100, up(895.090, "BUY", "0.45", "0")),
        (895.200, bk(895.090, [("0.44", "30")], [("0.54", "150"), ("0.55", "60")])),
        (905.000, {"event": "close", "seg": 0, "reason": "end", "code": None}), (905.010, {"event": "end"})]
    return first, second


def synth_stream(dirpath, T=SYN_T, mp=SYN):
    """The two files of synth_frames, in the pair book's line format, deterministic gzip; a PONG and a blank line
    in each."""
    paths = []
    for name, rows in zip(("%d-stream.jsonl.gz" % T, "%d-stream.1.jsonl.gz" % T), synth_frames(T, mp)):
        lines = []
        for s, obj in rows:
            rn = T * 10 ** 9 + int(round(s * 10 ** 7)) * 100
            if "event" in obj:
                lines.append(json.dumps(dict({"recv_ns": rn, "mono_ns": rn}, **obj), separators=(",", ":")))
            else:
                lines.append(json.dumps({"recv_ns": rn, "mono_ns": rn,
                                         "raw": json.dumps(obj, separators=(", ", ":"))}, separators=(",", ":")))
        lines.insert(3, json.dumps({"recv_ns": (T + 595) * 10 ** 9, "mono_ns": 0, "raw": "PONG"}, separators=(",", ":")))
        lines.insert(5, "")
        p = os.path.join(dirpath, name)
        with open(p, "wb") as fh:
            fh.write(gzip.compress(("\n".join(lines) + "\n").encode(), mtime=0))
        paths.append(p)
    return paths


# the Architect's reference over synth_stream's two files: its unit's lines and their SHA-256 (TZ-32 section 4.1)
SYN_LINES = 100
SYN_DIGEST = "6b179243c4feb9b0fcd76d45637e2a962626d8a8141a13e95dcddefb105ccd7e"
# the projection: each gated variant's V and Sh over the Architect's 302 windows of W0's span, every one read by W0,
# and the Architect's independent threshold and power at them scaled to 288 members (TZ-32 section 1)
PROJ_N = 302
PROJ = {"behind": (D("104180.3858"), D("210474.22"),
                   {"thr": D("544.1515737611919841909513296747519798286"), "power": (D("0.99822"), D("0.99823"))}),
        "front": (D("81071.5419"), D("737365.95"),
                  {"thr": D("480.0141253639412769515206627775781806438"), "power": (D("0.99999"), D("1.00001"))})}


def money_by_fill(fills, up):
    """The self-test's own arithmetic, written apart from TZ-23's: a fill of our bid at p for s shares pays
    s (up - p), of our ask s (p - up), and each the rebate 0.014 s p (1 - p); in Fractions, summed."""
    from fractions import Fraction
    tot = Fraction(0)
    for _vt, side, p, f, _kind in fills:
        s, pr = Fraction(f, 100), Fraction(p, 1000)
        tot += (s * (up - pr) if side == "b" else s * (pr - up)) + Fraction(14, 1000) * s * pr * (1 - pr)
    return tot


def mode_selftest():
    import random
    import threading
    import http.server
    from fractions import Fraction
    n = [0]

    def ok(cond, what):
        assert cond, "selftest: " + what
        n[0] += 1
        out("  ok  " + what)

    def fails(fn):
        try:
            fn()
        except AssertionError:
            return True
        return False

    # TZ-23's file, as loaded, and the constants this file takes from it
    ok(tz23.__file__ == os.path.join(HERE, TZ23_NAME) and sys.modules["tz23"] is tz23,
       "TZ-23's instrument loaded from beside this file, from its asserted bytes")
    ok(tz23.MALLOC_TUNED, "glibc took the 128 KiB mmap threshold and the two arenas")
    ok(tz23.getcontext().prec == 60, "the main thread sums at 60 digits")
    ok(DELTA == D("0.005") and tz23.REBATE_COEF == D("0.014") and
       tz23.FEE_SCHEDULE == {"exponent": 1, "rate": D("0.07"), "takerOnly": True, "rebateRate": D("0.2")} and
       tz23.FEE_TYPE == "crypto_fees_v2", "half a tick a share; the fee 0.07 s p (1 - p), the rebate a fifth of it, as "
                                          "the documents must state")
    ok(tz23.HEADERS == {"User-Agent": "btc-5m-twap-m0/TZ-23", "Accept": "application/json"} and
       DL_HEADERS == {"User-Agent": "btc-5m-twap-tz32", "Accept": "application/octet-stream"},
       "every document request carries TZ-23's two headers, every download this file's")
    ok([b[0] for b in tz23.BANDS] == list(LIFE_BANDS) and tz23.BANDS[-2] == ("last", 240, 300) and
       UNIT_BANDS == LIFE_BANDS[1:-1], "a leg's life is TZ-23's bands w0 to last, [T0, T0 + 300)")
    # the set: its windows, its last candidate and the archive's run that moves it
    ok(FIRST_T % WINDOW == 0 and FIRST_T + LEG - WINDOW == W0_LAST and utc(FIRST_T) == "2026-10-23T11:15:00Z" and
       utc(FIRST_T + LEG) == "2026-10-23T11:25:00Z", "the first window is 2026-10-23 11:15 UTC, the one after the "
                                                    "window whose leg is W0's last member")
    cal = (LAST_T + 910 + 60) // 86400 * 86400 + ARCHIVE_CALENDAR_S
    cal = cal if cal >= LAST_T + 970 else cal + 86400
    ok(LAST_T == 1793068200 and utc(LAST_T) == "2026-10-27T02:30:00Z" and utc(cal) == "2026-10-27T03:00:20Z" and
       cal < ARCHIVE_WAIT_UNTIL and utc(ARCHIVE_WAIT_UNTIL) == "2026-10-27T06:00:00Z",
       "the candidates end at 2026-10-27 02:30 UTC, which the calendar run of 03:00:20 moves; fetch waits to 06:00")
    ok(NEED == 288 and RESCORE_EVERY == 16 and len(range(0, NEED, RESCORE_EVERY)) == 18,
       "288 members; the rescore replays 18 of them")
    # the venue's numbers as exact integers
    ok([price_int(x) for x in ("0.5", "0.505", "1", "0", "0.07")] == [500, 505, 1000, 0, 70] and
       [size_int(x) for x in ("12.34", "5", "0.1", "1000000")] == [1234, 500, 10, 100000000],
       "prices in thousandths and sizes in hundredths, exactly")
    ok(all(fails(lambda t=t: price_int(t)) for t in ("0.5051", "1e-3", "-0.5", ".5", "0.5 ")) and
       all(fails(lambda t=t: size_int(t)) for t in ("1.234", "1e2", "-1", "")),
       "any other text of a price or a size is a failed assert")
    ok(x12(D("1.5")) == "1.500000000000" and x12(D("-0")) == "0.000000000000" and
       x12(D("-2.25")) == "-2.250000000000" and fails(lambda: x12(D("1e-13"))),
       "a unit's figure has twelve decimals exactly, and a figure with more is a failed assert")
    # our money: TZ-23's aggregate on our flipped rows, against this file's own arithmetic
    T0 = SYN_T + LEG
    fl = [(T0 * 10 ** 9 + 5 * 10 ** 9, "b", 480, 500, "m"), ((T0 + 61) * 10 ** 9, "a", 520, 1234, "x"),
          ((T0 + 299) * 10 ** 9 + 999 * MS_NS, "b", 70, 1, "m"), ((T0 + 200) * 10 ** 9, "a", 955, 250, "m")]
    life, bands = sums_of(T0, fl)
    ok(life["n"] == 4 and life["sh"] == D("19.85") and life["X"] == D("5") - D("12.34") + D("0.01") - D("2.5") and
       life["C"] == D("2.4") - D("6.4168") + D("0.0007") - D("2.3875") and bands["w0"]["n"] == 1 and
       bands["w1"]["n"] == 1 and bands["last"]["n"] == 1 and bands["w3"]["n"] == 1,
       "own rows: our bid +s Up at p, our ask -s at p; each fill in its band of [T0, T0 + 300)")
    ok(all(Fraction(str(life["X"] * up - life["C"] + life["R"])) == money_by_fill(fl, up) for up in (0, 1)),
       "X up - C + R equals the fill-by-fill money with the rebate, at either outcome")
    ok(fails(lambda: sums_of(T0, [((T0 + 300) * 10 ** 9, "b", 500, 500, "m")])) and
       fails(lambda: sums_of(T0, [(T0 * 10 ** 9 - 1, "b", 500, 500, "m")])),
       "a fill of ours at T0 + 300 or before T0 is a failed assert")
    # the synthetic window, replayed, against the Architect's reference and against its own rules by hand
    tmp = os.path.join(WORK, "selftest-tmp")
    shutil.rmtree(tmp, ignore_errors=True)
    os.makedirs(tmp)
    try:
        paths = synth_stream(tmp)
        mem = {"T": SYN_T, "condition": SYN["m5"]["condition"], "up": SYN["m5"]["Up"],
               "files": [{"bytes": os.path.getsize(p)} for p in paths]}
        lines = member_unit(mem, paths)
        body = ("\n".join(lines) + "\n").encode("utf-8")
        ok(len(lines) == SYN_LINES and sha256_bytes(body) == SYN_DIGEST,
           "the synthetic window's unit, %d lines, byte for byte the Architect's reference" % SYN_LINES)
        fills = {}
        for ln in lines:
            f = ln.split(" ")
            if f[1] == "fill":
                fills.setdefault(f[2], []).append((int(f[3]), f[4], int(f[5]), int(f[6]), f[7]))
        ms = SYN_T * 1000
        ok(fills["front"][0] == (ms + 601000, "b", 480, 500, "m") and "behind" in fills and
           fills["behind"] == [(ms + 602000, "b", 480, 500, "m")],
           "front, first in its queue, fills at the first sale into its bid; behind, after the 100 shares displayed "
           "ahead of it, fills only when a sweep of 120 takes the level and 50 beyond")
        ok((ms + 603155, "a", 520, 500, "x") in fills["L250"] and
           not any(k == "x" for _t, _s, _p, _f, k in fills["behind"] + fills["L100"] + fills["front"]),
           "a bid placed at 0.52 against our ask fills it 150 ms later where our cancel arrives after that, at 250 "
           "ms; at 50 and 100 ms the cancel arrives first; front counts no crossing")
        ok(sum(1 for t, s, _p, _f, _k in fills["front"] if s == "b") == 4 and
           sum(1 for t, s, _p, _f, _k in fills["front_L0"] if s == "b") == 4,
           "front stops bidding once its known position reaches 20 shares")
        ok((ms + 895090, "b", 460, 500, "m") in fills["L100"] and (ms + 895090, "b", 460, 500, "m") in fills["L250"]
           and all(t < ms + 895000 for t, *_r in fills["behind"] + fills["front"]),
           "the stop at T0 + 295 cancels every order; at 100 and 250 ms the cancel arrives after a sale at "
           "T0 + 295.090, at 50 ms before it")
        got = parse_unit(SYN_T, body.decode("utf-8"))
        ok(got["variants"]["behind"]["refused"] == 1 and got["variants"]["L0"]["refused"] == 0 and
           got["variants"]["L0"]["crossings"] == 1 and got["book"] == {
               "snapshots": 9, "equal": 9, "touch_equal": 9, "matches": 8, "two_sided": 0, "sessions": 2, "closes": 3},
           "a bid arriving 50 ms after the ask came down to its price is refused, at 0 ms it is not; 9 book frames, "
           "every one equal to the rebuilt book, 8 matches, 2 sessions, 3 closes")
        for name, *_r in VARIANTS:
            mine = [x for x in fills.get(name, [])]
            z = got["variants"][name]
            ok(Fraction(str(z["X"] - z["C"] + z["R"])) == money_by_fill([(t * MS_NS,) + tuple(r) for t, *r in mine], 1)
               and z["n"] == len(mine), "%s: the unit's sums are its fills' money" % name)
        # the json path and the fast path: the same frames, every one formatted out of the fast path's reach
        slow = os.path.join(tmp, "slow")
        os.makedirs(slow)
        sp = []
        for p in paths:
            with gzip.open(p, "rt", encoding="utf-8") as fh:
                rows = fh.read().split("\n")
            rows = [r.replace('\\", \\"', '\\",\\"') for r in rows]
            q = os.path.join(slow, os.path.basename(p))
            with open(q, "wb") as fh:
                fh.write(gzip.compress("\n".join(rows).encode(), mtime=0))
            sp.append(q)
        ok(not any(PC_LINE.fullmatch(r) for q in sp for r in gzip.open(q, "rt", encoding="utf-8")) and
           sha256_bytes(("\n".join(member_unit(dict(mem, files=[{"bytes": os.path.getsize(p)} for p in paths]),
                                               sp)) + "\n").encode()) == SYN_DIGEST,
           "the same frames read by the general path alone give the same unit, byte for byte")
        # a set of three synthetic members: constants label-free, the score against the fill-by-fill money
        units = os.path.join(tmp, "units")
        os.makedirs(units)
        members, docs = [], []
        good = {"slug": "", "outcomes": '["Up", "Down"]', "outcomePrices": '["1", "0"]', "closed": True,
                "feeType": tz23.FEE_TYPE, "feeSchedule": dict(tz23.FEE_SCHEDULE), "eventStartTime": "",
                "conditionId": SYN["m5"]["condition"], "clobTokenIds": '["5001", "5002"]'}
        for k in range(3):
            t = SYN_T + k * WINDOW
            d = os.path.join(tmp, "w%d" % k)
            os.makedirs(d)
            ps = synth_stream(d, T=t)
            m = {"T": t, "condition": SYN["m5"]["condition"], "up": SYN["m5"]["Up"],
                 "files": [{"bytes": os.path.getsize(p)} for p in ps],
                 "doc": dict(good, slug="btc-updown-5m-%d" % (t + LEG), eventStartTime=tz23.iso(t + LEG),
                             outcomePrices='["1", "0"]' if k != 1 else '["0", "1"]')}
            write_atomic(os.path.join(units, "%d.txt" % t), ("\n".join(member_unit(m, ps)) + "\n").encode())
            members.append(m)
        s = {"members": members, "sha": "0" * 64}
        rows, wsha, nl = concat_units(members, units, os.path.join(tmp, "x-units.txt"))
        ok(nl == 3 * SYN_LINES and len(rows) == 3, "three members' units read back, %d lines" % (3 * SYN_LINES))
        const, csha = build_constants(s, rows, "x", tmp)
        res = score_rows(s, rows, const, "x", tmp)
        for name, *_r in VARIANTS:
            want = Fraction(0)
            for m in members:
                up = tz23.label_of(m["doc"])
                with open(os.path.join(units, "%d.txt" % m["T"]), encoding="utf-8") as fh:
                    fz = [ln.split(" ") for ln in fh.read().split("\n") if " fill %s " % name in ln]
                want += money_by_fill([(int(f[3]) * MS_NS, f[4], int(f[5]), int(f[6]), f[7]) for f in fz], up)
            ok(Fraction(str(res["variants"][name]["S"])) == want and
               sum((z["S"] for z in res["variants"][name]["bands"].values()), D(0)) == res["variants"][name]["S"] and
               sum((z["S"] for z in res["variants"][name]["kinds"].values()), D(0)) == res["variants"][name]["S"],
               "%s: S over the synthetic set is its fills' money; the bands' and the kinds' sums add to it" % name)
        flipped = [dict(m, doc=dict(m["doc"], outcomePrices='["0", "1"]' if m["doc"]["outcomePrices"] == '["1", "0"]'
                                    else '["1", "0"]')) for m in members]
        os.makedirs(os.path.join(tmp, "f"))
        c2, csha2 = build_constants({"members": flipped, "sha": "0" * 64}, rows, "x", os.path.join(tmp, "f"))
        r2 = score_rows({"members": flipped, "sha": "0" * 64}, rows, c2, "x", os.path.join(tmp, "f"))
        ok(csha2 == csha and r2["variants"]["front"]["S"] != res["variants"]["front"]["S"],
           "the constants are byte-identical with every label flipped, and the score moves (negative control)")
        ok(build_constants(s, rows, "x", tmp)[1] == csha, "a second constants run finds its file unchanged")
        # units: held, downloaded in order, replayed and removed; a unit on disk is not replayed again
        calls = []

        def fake_dl(tag, asset, nbytes, sha, dest):
            calls.append(asset)
            shutil.copyfile(os.path.join(tmp, asset), dest)
            return nbytes, 0.0, 0

        files = [{"file": "stream.1.jsonl.gz", "tag": "t", "asset": "%d-stream.1.jsonl.gz" % SYN_T, "bytes": 1,
                  "sha256": ""}, {"file": "stream.jsonl.gz", "tag": "t", "asset": "%d-stream.jsonl.gz" % SYN_T,
                                  "bytes": 1, "sha256": ""}]
        clk = [SYN_T + 20.0]
        u, rec = run_unit(SYN_T, files, os.path.join(tmp, "dl"), lambda ps: member_unit(mem, ps),
                          os.path.join(tmp, "timing.jsonl"), holdf=lambda b: (clk[0], 0.0), dl=fake_dl)
        ok(calls == ["%d-stream.jsonl.gz" % SYN_T, "%d-stream.1.jsonl.gz" % SYN_T] and
           sha256_bytes(("\n".join(u) + "\n").encode()) == SYN_DIGEST and os.listdir(os.path.join(tmp, "dl")) == []
           and rec["T"] == SYN_T and rec["bytes"] == 2 and rec["budget_s"] == 5 + 1 + UNIT_BUDGET_S,
           "a unit downloads its files in stream order, replays them, removes them, and is timed")
        seen = []
        replay_units([dict(mem, files=files)], os.path.join(tmp, "ru"), os.path.join(tmp, "t2.jsonl"), 1, tmp,
                     unit_fn=lambda T, f, d, fn, tm: (seen.append(T) or (["%d member x" % T], {"cpu_s": 0,
                                                                                                "bytes": 1})))
        replay_units([dict(mem, files=files)], os.path.join(tmp, "ru"), os.path.join(tmp, "t2.jsonl"), 1, tmp,
                     unit_fn=lambda T, f, d, fn, tm: (seen.append(T) or (["%d member x" % T], {"cpu_s": 0,
                                                                                                "bytes": 1})))
        ok(seen == [SYN_T], "a unit already on disk is not replayed again")
        few = [dict(mem, T=SYN_T + k * WINDOW, files=[{"bytes": 10 ** 6}]) for k in range(RESCORE_EVERY + 2)]
        cnt6 = []
        ok(fails(lambda: replay_units(few, os.path.join(tmp, "rq"), os.path.join(tmp, "t4.jsonl"), 30, tmp,
                                      unit_fn=lambda T, f, d, fn, tm: (cnt6.append(T) or (
                                          ["%d member x" % T], {"cpu_s": 5.0, "bytes": 10 ** 6})),
                                      project_after=RESCORE_PROJECT_AFTER)) and len(cnt6) == RESCORE_PROJECT_AFTER,
           "the rescore's 18, projected above its bound, stop BLOCKED after the first %d" % RESCORE_PROJECT_AFTER)
        many = [dict(mem, T=SYN_T + k * WINDOW, files=[{"bytes": 10 ** 6}]) for k in range(PROJECT_AFTER + 5)]
        cnt = []
        ok(fails(lambda: replay_units(many, os.path.join(tmp, "rp"), os.path.join(tmp, "t3.jsonl"), 100, tmp,
                                      unit_fn=lambda T, f, d, fn, tm: (cnt.append(T) or (
                                          ["%d member x" % T], {"cpu_s": 5.0, "bytes": 10 ** 6})))) and
           len(cnt) == PROJECT_AFTER, "the replays projected above their bound stop BLOCKED after the first %d "
                                      "units" % PROJECT_AFTER)
        # downloads against a local server: whole and verified, retried, then BLOCKED
        root = os.path.join(tmp, "srv")
        os.makedirs(root)
        blob = os.urandom(70000)
        with open(os.path.join(root, "a.gz"), "wb") as fh:
            fh.write(blob)

        class H(http.server.SimpleHTTPRequestHandler):
            def __init__(self, *a, **k):
                super().__init__(*a, directory=root, **k)

            def log_message(self, *a):
                pass

        srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), H)
        th = threading.Thread(target=srv.serve_forever, daemon=True)
        th.start()
        try:
            urllib.request.install_opener(urllib.request.build_opener(urllib.request.ProxyHandler({})))
            url = lambda t, a: "http://127.0.0.1:%d/%s" % (srv.server_address[1], a)
            dest = os.path.join(tmp, "got.gz")
            nb, _s, k = download("t", "a.gz", len(blob), sha256_bytes(blob), dest, url_of=url, sleep=lambda s: None)
            with open(dest, "rb") as fh:
                ok(nb == len(blob) and k == 0 and fh.read() == blob, "a download arrives whole, verified by its bytes "
                                                                     "and SHA-256")
            slept = []
            ok(fails(lambda: download("t", "a.gz", len(blob), "0" * 64, dest + "2", url_of=url,
                                      sleep=slept.append)) and len(slept) == DL_TRIES and
               not os.path.exists(dest + "2.part") and not os.path.exists(dest + "2"),
               "a download whose SHA-256 differs is tried %d times and stops BLOCKED, leaving nothing" % DL_TRIES)
            slept.clear()
            ok(fails(lambda: download("t", "missing.gz", 1, "0" * 64, dest + "3", url_of=url, sleep=slept.append))
               and len(slept) == DL_TRIES, "a missing asset is tried %d times and stops BLOCKED" % DL_TRIES)
        finally:
            srv.shutdown()
            srv.server_close()
            urllib.request.install_opener(None)
        # the archive's record: every complete run's set.json against its record, each stream file in one set
        st_root = os.path.join(tmp, "archive")
        recs = []
        for a, ts in ((1792724420, [1792722600]), (1792810820, [1792723500, 1792724400])):
            doc = {"tag": "pairbook-streams-%d" % a, "assets_n": len(ts), "bytes_total": 10 * len(ts),
                   "assets": [{"T": t, "file": "stream.jsonl.gz", "asset": "%d-stream.jsonl.gz" % t, "bytes": 10,
                               "sha256": "0" * 64} for t in ts]}
            raw = json.dumps(doc).encode()
            os.makedirs(os.path.join(st_root, "runs", str(a)))
            with open(os.path.join(st_root, "runs", str(a), "set.json"), "wb") as fh:
                fh.write(raw)
            recs += [{"event": "start", "run": a, "wall_ns": 1}, {"event": "set", "run": a, "wall_ns": 2,
                                                                  "tag": doc["tag"], "assets_n": len(ts),
                                                                  "bytes_total": 10 * len(ts),
                                                                  "sha256": sha256_bytes(raw)},
                     {"event": "complete", "run": a, "wall_ns": 3}]
        amap = asset_map(archived_sets(recs, state=st_root))
        ok(sorted(amap) == [1792722600, 1792723500, 1792724400] and
           amap[1792724400]["stream.jsonl.gz"]["tag"] == "pairbook-streams-1792810820" and
           archived_sets(recs[:-1], state=st_root)[-1]["run"] == 1792724420,
           "every complete run's set.json gives its windows' assets; a run without its complete record gives none")
        bad = [dict(r, sha256="1" * 64) if r["event"] == "set" else r for r in recs]
        ok(fails(lambda: archived_sets(bad, state=st_root)) and fails(lambda: asset_map(
            archived_sets(recs, state=st_root) * 2)), "a set.json whose SHA-256 is not its record's, or a stream file "
                                                     "in two sets, is a failed assert")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    # the archive's wait
    clock = [float(LAST_T)]
    reads = []

    def reader(last):
        def r():
            reads.append(clock[0])
            return {last: {}}, last
        return r

    _a, waited = wait_archive(clock=lambda: clock[0], sleep=lambda s: clock.__setitem__(0, clock[0] + s),
                              read=reader(LAST_T))
    ok(waited == 0 and len(reads) == 1, "fetch starts at once where the archive has moved every candidate")
    clock[0] = ARCHIVE_WAIT_UNTIL - 125.0
    ok(fails(lambda: wait_archive(clock=lambda: clock[0], sleep=lambda s: clock.__setitem__(0, clock[0] + s),
                                  read=reader(LAST_T - WINDOW))) and clock[0] >= ARCHIVE_WAIT_UNTIL,
       "an archive short of the last candidate is read every 60 s and stops BLOCKED at 2026-10-27 06:00 UTC")
    # the set's rules on literal window.json and documents
    t = FIRST_T
    st = {"opened": True, "off_reason": None, "files": ["stream.jsonl.gz"], "cut": False,
          "subscribed_wall_ns": (t + 595) * 10 ** 9, "last_frame_wall_ns": (t + 904) * 10 ** 9,
          "max_gap_ns": 3 * 10 ** 9}
    wj = {"joined_late": False, "stopped": False, "stream": st,
          "markets": {"m5": {"slug": "btc-updown-5m-%d" % (t + LEG), "conditionId": "0x" + "c" * 64,
                             "clobTokenIds": '["11", "22"]', "outcomes": '["Up", "Down"]'}}}
    have = {t: {"stream.jsonl.gz": {}}}
    cases = [({}, None), ({"joined_late": True}, "stream: joined late or stopped"),
             ({"stream": dict(st, opened=False)}, "stream: not opened"), ({"stream": dict(st, cut=True)}, "stream: cut"),
             ({"stream": dict(st, subscribed_wall_ns=(t + 600) * 10 ** 9 + 1)}, "stream: subscribed late"),
             ({"stream": dict(st, last_frame_wall_ns=(t + 900) * 10 ** 9 - 1)}, "stream: ended early"),
             ({"stream": dict(st, max_gap_ns=GAP_MAX_NS + 1)}, "stream: a gap above 15 s"),
             ({"stream": dict(st, files=["stream.jsonl.gz", "stream.1.jsonl.gz"])}, "stream: not archived")]
    ok(all(stream_problem(dict(wj, **chg), t, have) == want for chg, want in cases) and
       stream_problem(None, t, have) == "stream: none",
       "a window's stream: opened, not cut or stopped, subscribed by T + 600, its last frame at or after T + 900, no "
       "gap above 15 s, every file archived")
    doc = {"slug": "btc-updown-5m-%d" % (t + LEG), "outcomes": '["Up", "Down"]', "outcomePrices": '["0", "1"]',
           "closed": True, "feeType": tz23.FEE_TYPE, "feeSchedule": dict(tz23.FEE_SCHEDULE),
           "eventStartTime": tz23.iso(t + LEG), "conditionId": "0x" + "c" * 64, "clobTokenIds": '["11", "22"]',
           "orderMinSize": 5}
    ok(leg_problem(wj, t, doc) is None and leg_problem(wj, t, dict(doc, orderMinSize=D(10))) == "document: order size"
       and leg_problem(wj, t, dict(doc, conditionId="0x" + "d" * 64)) == "window.json: the leg's condition or tokens"
       and leg_problem(wj, t, dict(doc, clobTokenIds='["22", "11"]')) == "window.json: the leg's condition or tokens"
       and leg_problem(wj, t, dict(doc, feeSchedule={})) == "document: fee" and leg_problem(wj, t, None) ==
       "document: absent" and leg_problem(wj, t + WINDOW, dict(doc, eventStartTime=tz23.iso(t + WINDOW + LEG))) ==
       "window.json: the leg's slug", "a leg's document: TZ-23's qualify, minimum order 5, and the condition and "
                                     "tokens window.json carries for it")
    # the clock: the idle stretch, the archive's calendar run and its service
    W = 1792458000
    idle = lambda s="inactive": (lambda: s)
    ok(quiet(W + 14, 60, idle()) is not None and quiet(W + 15, 60, idle()) is None and
       quiet(W + 530, 60, idle()) is None and quiet(W + 531, 60, idle()) is not None and
       quiet(W + 700, 60, idle()) is not None, "a unit of 60 s starts from second 15 to 530 of a window")
    calw = W // 86400 * 86400 + ARCHIVE_CALENDAR_S
    ok(quiet(calw - 5, 60, idle()) is not None and quiet(calw + 61, 60, idle()) is None and
       all(quiet(W + 100, 60, idle(s)) is not None for s in RUNNING) and quiet(W + 100, 60, idle("failed")) is None,
       "nothing starts near the archive's calendar run or while its service runs")
    clock = [W + 600.25]
    t1, waited = hold(60, clock=lambda: clock[0], sleep=lambda s: clock.__setitem__(0, clock[0] + s), state_of=idle())
    ok(int(t1) == W + 900 + 15, "held from second 600, a unit starts at second 15 of the next window")
    # the gate: TZ-23's thresholds on this TZ's lambda, W1's table and G-BOOK
    for g in GATED:
        vf, sf, want = PROJ[g]
        c = tz23.gate_constants(vf * NEED / PROJ_N, sf * NEED / PROJ_N, lam=LAMBDA[g], alpha=ALPHA, delta=DELTA)
        ok(abs(c["thr"] - want["thr"]) < D("1e-20") and want["power"][0] < c["power"] < want["power"][1],
           "%s: at the projected V and Sh the threshold is %s and the power between %s and %s, the Architect's" % (
               g, fx(want["thr"]), want["power"][0], want["power"][1]))
    T_ = {"earn": True, "no_earn": False}
    F_ = {"earn": False, "no_earn": False}
    ok(w1_reading({"behind": T_, "front": dict(F_, no_earn=True)}) == "W1-EARN" and
       w1_reading({"behind": F_, "front": dict(F_, no_earn=True)}) == "W1-NO-EARN" and
       w1_reading({"behind": dict(F_, no_earn=True), "front": dict(F_, earn=True)}) == "UNDECIDABLE" and
       w1_reading({"behind": T_, "front": F_}) == "W1-EARN",
       "W1-EARN on behind's EARN bound, first; W1-NO-EARN on front's NO EARN bound; UNDECIDABLE otherwise")
    c = tz23.gate_constants(D(10 ** 4), D(10 ** 6), lam=LAMBDA["front"], alpha=ALPHA, delta=DELTA)
    th = {"earn_at": c["earn_at"], "no_earn_at": c["no_earn_at"]}
    ok(c["earn_at"] == c["thr"] and c["no_earn_at"] == DELTA * D(10 ** 6) - c["thr"] and c["thr"] < c["no_earn_at"]
       and [tz23.reading(x, th)[0] for x in (c["thr"] - 1, c["thr"], c["no_earn_at"] + 1)] ==
       ["NO EARN", "EARN", "EARN"], "TZ-23's reading on this TZ's lambda: EARN at S >= thr, NO EARN at "
                                   "S <= delta Sh - thr, EARN first where both hold")
    c2 = tz23.gate_constants(D(10 ** 9), D(10 ** 5), lam=LAMBDA["front"], alpha=ALPHA, delta=DELTA)
    th2 = {"earn_at": c2["earn_at"], "no_earn_at": c2["no_earn_at"]}
    ok(c2["no_earn_at"] < c2["thr"] and [tz23.reading(x, th2)[0] for x in (
        c2["no_earn_at"], c2["no_earn_at"] + 1, c2["thr"] - 1, c2["thr"])] ==
       ["NO EARN", "UNDECIDABLE", "UNDECIDABLE", "EARN"], "UNDECIDABLE between the bounds where they part")
    ok(book_reading(1000, 990) == "PASS" and book_reading(1000, 989) == "FAIL" and book_reading(0, 0) == "FAIL" and
       touch_of({480: 100, 470: 5}, {520: 7}) == (480, 100, 520, 7) and touch_of({}, {520: 7}) == (None, None, 520, 7),
       "G-BOOK: the rebuilt touch, each best price and its size, equal at 99 of every 100 match frames; a set with "
       "none fails")
    # G-STILL: unchanged, or the pair book moved by a chain of the archive's own restart records
    u0 = {"recorder": {"MainPID": "4148534", "NRestarts": "2", "ActiveState": "active"},
          "pairbook": {"MainPID": "2221487", "NRestarts": "19", "ActiveState": "active"}}
    u2 = {"recorder": dict(u0["recorder"]), "pairbook": {"MainPID": "30", "NRestarts": "21", "ActiveState": "active"}}
    chain = [{"event": "restart", "stopped": 2221487, "pid": 20, "NRestarts": "20"},
             {"event": "restart", "stopped": 20, "pid": 30, "NRestarts": "21"}]
    ok(still_reading(u0, json.loads(json.dumps(u0)), []) == (True, "unchanged") and
       still_reading(u0, u2, chain)[0] and not still_reading(u0, u2, chain[:1])[0] and
       not still_reading(u0, u2, chain[::-1])[0] and not still_reading(u0, u2, [])[0] and
       not still_reading(u0, dict(u2, recorder=dict(u0["recorder"], MainPID="1")), chain)[0],
       "G-STILL: unchanged, or the pair book moved by a chain of the archive's restart records; any other change fails")
    # the archive's ledger, summarized from literal records
    recs = [{"event": "start", "run": 1792378820, "wall_ns": 1}, {"event": "set", "run": 1792378820, "wall_ns": 2,
            "tag": "pairbook-streams-1792378820", "assets_n": 96, "bytes_total": 10, "first_T": 1792291500,
            "last_T": 1792377000}, {"event": "complete", "run": 1792378820, "wall_ns": 3},
            {"event": "start", "run": 1792045110, "wall_ns": 4},
            {"event": "halt", "run": 1792045110, "wall_ns": 6, "phase": "restart", "reason": "x"}]
    summ = ledger_summary(recs)
    ok(summ["runs"] == [1792378820, 1792045110] and "calendar" in summ["lines"][0] and
       "off-calendar, second 22710" in summ["lines"][1] and summ["halted"] and
       summ["terminal"] == {1792378820: ["complete"], 1792045110: ["halt"]},
       "the ledger's runs, terminals, calendar and halt")
    # the fingerprint's rows, on literal lines
    lines = ("| `research/tz23-maker-m0.py` | 1,184 | 54,885 | frozen | `%s` |\n"
             "| `SYSTEM-MAP.md` | — | — | reported | self-reference; report the value you compute |\n"
             "| `A6` — pricer | `729f0bcdbee3` |\n" % TZ23_SHA256)
    ok(ROW.findall(lines) == [("research/tz23-maker-m0.py", "1,184", "54,885", "frozen", TZ23_SHA256),
                              ("SYSTEM-MAP.md", "—", "—", "reported",
                               "self-reference; report the value you compute")] and
       dict(ANCHOR_ROW.findall(lines)) == {"A6": "729f0bcdbee3"}, "the map's rows and anchors parse")
    ok(reclaimable(WORK) and not reclaimable(FORENSICS) and not reclaimable("/tmp/x/" + "0" * 8 + "-0000-0000-0000-"
                                                                           + "0" * 12),
       "reclaim takes the work tree and refuses the forensic store and a directory outside a session's")
    # the audit hook: section 2's reads, writes, requests and processes, each refused before it happens
    pw = PAIRBOOK + "/%d/window.json" % FIRST_T
    ok(policy("fetch", "open", (pw, "rb", 0)) is None and
       policy("fetch", "open", (PAIRBOOK + "/%d/window.json" % (FIRST_T - WINDOW), "rb", 0)) is not None and
       policy("fetch", "open", (PAIRBOOK + "/%d/window.json" % (LAST_T + WINDOW), "rb", 0)) is not None and
       policy("fetch", "open", (PAIRBOOK + "/%d/stream.jsonl.gz" % FIRST_T, "rb", 0)) is not None and
       policy("replay", "open", (pw, "rb", 0)) is not None and policy("fetch", "open", (pw, "wb", 0)) is not None and
       policy("fetch", "os.listdir", (PAIRBOOK,)) is not None,
       "the pair book's root: window.json of a candidate read by fetch alone, nothing else opened, listed or written")
    ok(policy("archive", "open", (ARCHIVE_LEDGER, "rb", 0)) is None and
       policy("still", "open", (ARCHIVE_LEDGER, "rb", 0)) is None and
       policy("fetch", "open", (ARCHIVE_STATE + "/runs/1792724420/set.json", "rb", 0)) is None and
       policy("still", "open", (ARCHIVE_STATE + "/runs/1792724420/set.json", "rb", 0)) is not None and
       policy("score", "open", (ARCHIVE_LEDGER, "rb", 0)) is not None and
       policy("archive", "open", (ARCHIVE_LEDGER, "ab", os.O_WRONLY)) is not None and
       policy("archive", "open", (ARCHIVE_STATE + "/archive.log", "rb", 0)) is not None,
       "the archive's state: its ledger read by archive, fetch and still, its runs' set.json by archive and fetch, "
       "nothing written")
    ok(all(policy(m, "urllib.Request", ("https://github.com/x",)) is None for m in ("rehearse", "replay", "rescore"))
       and policy("fetch", "urllib.Request", ("https://github.com/x",)) is not None and
       all(policy(m, "urllib.Request", ("https://gamma-api.polymarket.com/markets",)) is None
           for m in ("rehearse", "fetch")) and
       policy("replay", "urllib.Request", ("https://gamma-api.polymarket.com/markets",)) is not None and
       policy("score", "urllib.Request", ("https://data-api.polymarket.com/v2/trades",)) is not None and
       policy("fetch", "urllib.Request", ("https://clob.polymarket.com/book",)) is not None,
       "downloads in rehearse, replay and rescore alone; documents in rehearse and fetch alone; nothing else")
    ok(policy("reclaim", "open", (FORENSICS + "/x", "xb", 0)) is None and
       policy("reclaim", "open", (FORENSICS + "/x", "wb", 0)) is not None and
       policy("score", "open", (FORENSICS + "/x", "xb", 0)) is not None and
       policy("score", "open", ("/root/elsewhere", "wb", 0)) is not None and
       policy("score", "open", (FORENSICS + "/x", "rb", 0)) is None and
       policy("score", "subprocess.Popen", ("/usr/bin/curl", ["curl"])) is not None and
       policy("score", "subprocess.Popen", ("git", ["git"])) is None,
       "the forensic store written by reclaim's exclusive create alone, nothing outside the work tree, and no "
       "process but git, systemctl and stat")
    MODE[0] = "selftest"
    refused = []
    for p in (PAIRBOOK + "/runtime.jsonl", ARCHIVE_LEDGER, CHAINBOOK + "/runtime.jsonl"):
        try:
            open(p, "rb")
            refused.append("opened")
        except GuardError:
            refused.append("tz32")
        except RuntimeError:
            refused.append("tz23")
        except OSError:
            refused.append("not refused")
    ok(refused == ["tz32", "tz32", "tz23"] and tz23.OPENS[-1] == CHAINBOOK + "/runtime.jsonl",
       "opens under the pair book's root and of the archive's ledger are refused by this hook, under the chain book's "
       "root by TZ-23's, each before it happens")
    tz23.OPENS.clear()
    del REFUSED[:]
    out("%d of %d checks passed" % (n[0], n[0]))


def main(argv):
    if not argv:
        sys.exit("usage: tz32-our-quoting.py MODE [ARG...]")
    mode, rest = argv[0], argv[1:]
    assert os.getcwd() == WORK, "run from %s, not %s" % (WORK, os.getcwd())
    MODE[0] = mode
    table = {"fingerprint": mode_fingerprint, "selftest": mode_selftest, "still": mode_still,
             "archive": mode_archive, "rehearse": mode_rehearse, "fetch": mode_fetch, "replay": mode_replay,
             "rescore": mode_rescore, "score": mode_score}
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
