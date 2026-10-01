# TZ-19 — Phase 2's second look, tau 240

**Canonical filename:** `TZ-19-phase2-second-look.md`. The committed file takes this name and no other.

**Executor model: Opus.** An exact gate at a new error allocation, the reserved span's second label read, a
reproduction of the first look that must hold to the last digit, and a stop block for a running process.

**Required System Map revision:** `2026-09-27-b`.

**Required anchors**, from map §0. A mismatch on any one is BLOCKED before any work:

| anchor | required |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` |
| `A6` — pricer | `729f0bcdbee3` |

**Host gate:** §0.2. This TZ touches the capture host and runs nowhere else.

**When:** once §0.8's readiness condition holds. **Until it holds, the Executor stops with no report, no branch
and no file written** — the one stop of this TZ that is not BLOCKED (§0.8) — and `EXECUTE TZ-19` is sent again
later. At the rate TZ-16a's span completed, 92.0% of slots, the condition first holds around 2026-10-01 12:00
UTC.

**What this TZ is.** TZ-16a §4.2's second look, applied unchanged: `tau` 240 alone, the one `tau` TZ-16a's first
look left UNDECIDABLE; the first 3,600 qualifying slots after `1789669800`, TZ-16a's 2,400 among them; TZ-16a
§3.4 to §3.7 at that `tau`; TZ-16a's own `r`, recomputed and asserted equal; `α2 = β2 = D("0.008")`; TZ-16a
§4.1's table; and the eight functions TZ-16a §4.2 names, imported from `research/tz16a-phase2-decisive-gate.py`
and written nowhere again. **No threshold, error allocation, selection, fee, domain or pricer of this TZ differs
from TZ-16a's.** Six things TZ-16a §4.2 does not fix are fixed here, before any label of the look is read:

1. **§0.8:** TZ-16a §0.8's readiness condition at 3,600, 24 slots of margin beside it, and a stop without a
   report until both hold.
2. **§3.2 and §3.6:** the first look inside this one is asserted TZ-16a's to the last digit — its members, and
   at `tau` 240 its selection and all six of its constants — before any label is read.
3. **§4.3:** what each reading means for Phase 2, for Phase 3 and for map §2.3's reserve — UNDECIDABLE included,
   for which TZ-16a named no third look and this TZ fixes none.
4. **§3.10:** the chain book's interlock over this look's own units (map §2.5).
5. **§5.3:** the rehearsal inside the instrument that map §7 item 84 requires.
6. **§9:** the reclaiming of `/root/tz16a-work/`, and of `/root/tz15-work/` and `/root/tz18a-work/` where the
   blocks TZ-16a §9 handed the Boss were not run.

---

## 0. Gates, host, interpreter, floor, preflight, refs, trees, readiness

### 0.1 Fingerprint — asserted inside the instrument as step 0 of §5.1

Read `SYSTEM-MAP.md` in the checkout the instrument runs from, a branch cut from `origin/main` after this TZ
landed. Its revision string must read `2026-09-27-b` and its six anchors must equal the table above; `A2`, `A4`,
`A5` and `A6` are also re-derived as the first 12 hex characters of those files' SHA-256. Every row of its §0
fingerprint table is hashed in lines, bytes and SHA-256 through `tz14.fingerprint_rows()`: the **25** `frozen`
rows must equal the hashes printed there — `research/tz16a-phase2-decisive-gate.py` at
`3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125` among them, on `main` since PR #20's merge —
the **2** `tracked` rows are reported with no expectation, and the **1** `reported` row, `SYSTEM-MAP.md` itself,
is reported. Any `frozen` mismatch is BLOCKED. The expected revision, the six anchors and the counts `25`, `2`
and `1` are literals of this instrument, so the gate never reads its own expected values from the file it
checks. **None of `tz14.v1_gates`, `tz15.v1_gates` and `tz16a.v1_gates` is called:** they assert revisions
`2026-09-18-b`, `2026-09-19-a` and `2026-09-27-a`.

### 0.2 Host gate

From `/root/btc-5m-twap`, before anything else, output verbatim into the report:

```
df -B1 --output=source,size,avail /var/lib/btc-recorder
find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
pgrep -fx '/root/tz04a-env/venv/bin/python -B -u recorder.py'; echo "exit=$?"
grep -c 4216c04673ced76b5b2ac60ef57c9abedc46f9b9 /var/lib/btc-recorder/runtime.jsonl
pgrep -fx '/root/tz01-env/venv/bin/python -B -u /root/tz18a-svc/tz18a-chainbook-capture.py --serve'; echo "exit=$?"
du -sb /root/PROJECT_GAMING_PS5
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
systemctl is-active telemetry-watch.service; echo "exit=$?"
for d in /root/tz15-work /root/tz16a-work /root/tz18a-work /root/tz18a-svc /root/tz19-work; do test -e "$d"; echo "$d exit=$?"; done
find /root/btc-forensics -type f | wc -l
git worktree list
```

- **H1** — `find` prints exactly one path.
- **H2** — the first `pgrep -fx` prints exactly one line and `exit=0`. `-fx` matches the whole command line, so
  the shell evaluating this block, which carries the pattern as a substring, cannot match it. Map §8 records the
  recorder as pid `228592`; another pid is disclosed, not BLOCKING.
- **H3** — `df` names source `/dev/vda2` and size `31612203008`, and the `grep -c` line, which reads the
  recorder's own top-level log and no interval directory, prints at least `1`. With H1 these are map §6's
  host-identity row; the newest start record's sha is asserted by the instrument at step 1.
- **H4 — recorded, not BLOCKING:** the second `pgrep -fx`, the chain book service, which map §2.5 records as pid
  `2699889`. §3.10 reads the service's own record and does not depend on this line.
- **Resource gate** — `avail` at least `2,060,000,000` bytes (§0.4).
- **Trees** — `/root/tz16a-work` and `/root/tz18a-svc` exit `0`, and `/root/tz19-work` exits `1`. Anything else
  is BLOCKED. **`/root/tz15-work` and `/root/tz18a-work` are recorded, not BLOCKING:** map §3 records both as
  handed to the Boss by TZ-16a §9, their removal to be verified by this §0 and not by his account. `exit=1` is
  that verification; `exit=0` means the block was not run, and §9 reclaims the tree.
- **Forensic store** — exactly `1,072` files, map §3's count at TZ-16a's end. Anything else is BLOCKED.
- `du`, both `systemctl` reads and `git worktree list` are printed and carry no threshold; map §3 registers
  three worktrees at TZ-16a's end.

### 0.3 Interpreter

Every command of the instrument runs on `/root/tz01-env/venv/bin/python` — Python 3.12.x (map §6). Report its
version and `numpy`'s. `import numpy` must succeed, because the committed chain the instrument loads imports it;
the instrument itself computes nothing in `numpy`.

### 0.4 Resource floor, in exact bytes, derived from map §6

Free space on `/dev/vda2` at run start at least `tz11a.FLOOR_START_BYTES` = `2,060,000,000`; every later read at
least `tz11a.FLOOR_BYTES` = `2,000,000,000`, map §6's floor. The `60,000,000` bytes between them bound what this
TZ writes: TZ-16a's tree held `22,167,020` bytes at its closing read (map §3) after four runs over five `tau`,
and this TZ's runs carry one `tau` over one and a half times the members. Both asserted; every read reported
with its UTC instant, its reader and its bound.

### 0.5 Preflight, twice, at least 1,800 s apart

The first after R-READY and before the build, the second before the first run with `--score`: `df -B1` on
`/dev/vda2`, `du -sb /root/PROJECT_GAMING_PS5`, and the exit codes of
`systemctl is-enabled telemetry-watch.service` and `systemctl is-active telemetry-watch.service`. Both reported
with the elapsed seconds and the implied bytes per day of each quantity; this session's own footprint —
`/root/tz19-work` and `/root/.claude` — stated separately at both (map §7 item 29), and `/root/tz16a-work`,
TZ-16a's, beside them. Gates nothing beyond §0.4.

### 0.6 Refs

`git ls-remote origin` before the branch of §2 exists, every ref reported. Map §1 records `main` at
`5935ca57e1fbac30999b0682832d5be7a63c7f40`, the TZ-16a report, and three branches. **Read by the Architect with
`git ls-remote` on 2026-09-28:** `main` at `84b60206c0182b4fe5dbc457357a95726cec5faa`, PR #20's merge, whose
first parent `0126a5b` uploaded revision `2026-09-27-b`; `main` the only branch on `origin`, both
`tz-16a-phase2-decisive-gate` and `tz-18a-chainbook-capture` deleted; `refs/pull/20/head` at `5076b43`. The
upload that carries this TZ sits above `84b6020`. Every commit on `main`'s first-parent line above `5935ca5` is
reported with the paths it changed, and their number is recorded, not asserted. A difference is recorded, not
BLOCKING, unless `main` no longer carries revision `2026-09-27-b` or `refs/heads/tz-19-phase2-second-look`
already exists — either is BLOCKED.

### 0.7 The recorder's working tree

The recorder runs from `/root/btc-5m-twap/research/recorder` (TZ-15 report §0.2), so that checkout's working
tree is never switched: the branch is built in `/root/tz19-work/wt` and the report committed from
`/root/tz19-work/wt-report`, both added with `git worktree add` from `origin`. `/root/tz16a-work/wt` and
`/root/tz16a-work/wt-report`, TZ-16a's, are left as they are until §9.

### 0.8 Readiness — the one condition that depends on the calendar

After §0.2 and before anything else, from `/root/btc-5m-twap`, reading manifests and nothing else under the
capture root (map §2.3's exception):

```
/root/tz01-env/venv/bin/python -B - <<'EOF'
import glob, json, time
t0s = []
for p in glob.glob('/var/lib/btc-recorder/btc-updown-5m/*/manifest.json'):
    with open(p, encoding='utf-8') as fh:
        d = json.load(fh)
    if d['T0_epoch'] > 1789669800 and d['complete'] is True:
        t0s.append(d['T0_epoch'])
t0s.sort()
now = int(time.time())
at = lambda k: t0s[k - 1] if len(t0s) >= k else None
print('complete', len(t0s), 'at-3600', at(3600), 'at-3624', at(3624), 'now', now)
EOF
```

**R-READY:** at least `3,624` complete manifests with `T0 > 1789669800`, and `now >= t0s[3623] + 3,900`. It
contains TZ-16a §4.2's condition — TZ-16a §0.8's at 3,600: at least `3,600` and `now >= t0s[3599] + 3,900` — and
adds 24 slots of margin. **R-READY is a necessary condition, read from manifests; the sufficient one is §3.2's
clock condition, asserted on the set's own 3,600th member** (map §7 item 84), and R-READY implies it whenever at
most 24 complete units before that member fail a further condition of the set rule: 1 of TZ-16a's 2,608 units
did (TZ-16a report §2). `3,900` s is the recorder's outcome deadline, `S7_DEADLINE_S` = `3600` s after `T0` in
`research/recorder/recorder.py`, plus `300` s for the close that writes the manifest after it.

**NOT YET.** Where R-READY does not hold, the Executor prints the line and §0.2's output in the session and
stops: no branch, no worktree, no directory, no commit and no report. No file of any interval directory but its
manifest has been opened and no report exists, so TZ-19 has not executed (CANON hard rule 5), and
`EXECUTE TZ-19` is sent again later. **This TZ wins over contract §9 for this one condition,** which is a date
and not a defect of the specification; the report of the run that executes names every NOT YET its session saw.
Every other failure is BLOCKED, as the contract says.

---

## 1. Why this TZ exists

TZ-16a's first look read NO EDGE at `tau` 180, 120, 90 and 60 and left 240 UNDECIDABLE: the side the Student
pricer called cheap after the fee won `538` of `945` trades, 10 above NO EDGE's `d` = `528` and 28 short of
EDGE's `c` = `566` (TZ-16a report §6). Its §4.2 fixed, before any label of the span was read, the one further
look that decides 240, and map §5 describes it. The two answers, each from its own exact test:

- **EDGE** — the null is a market calibrated at its own ask: each selected trade wins with the probability of
  the price paid. EDGE where the wins reach beyond that law's upper tail.
- **NO EDGE** — the null is the pricer's own law: each selected trade wins with the probability `p_t` gives the
  side bought. NO EDGE where the wins fall below that law's lower tail.
- **UNDECIDABLE** between them.

**The allocation is TZ-16a's:** `0.002` spent at the first look and `0.008` at this one, so each answer's
false-reading probability at `tau` 240 is at most `0.01` over the two looks by the union bound, whatever the
dependence between them (TZ-16a §1). **Power was sized before any label was read** — TZ-16a's projection gave
`0.911` for EDGE and `0.913` for NO EDGE (TZ-16a report §4) — and decides nothing here.

**The dependence is TZ-16a's `r` at `tau` 240, which is `1`.** On TZ-15's labelled set `f̂` was `0.741`, a
negative dependence, which thins the tails and is never used to narrow them (TZ-16a §1 and §3.2); on TZ-16a's
own look it was `0.955` (TZ-16a report §6). §3.1 recomputes it from TZ-15's file and asserts it equal.

**Selection, fee, domain and pricer are TZ-15's, unchanged:** `tz15.select`, `tz14.fee_pp`, `pfair.ADMIT`
through `tz11a.checkpoint_row`, `A6` `729f0bcdbee3`. No constant of this TZ was chosen by looking at a quote
beside a price.

**The set is formed from the capture alone,** as TZ-16a's was: the recorder writes an interval's manifest only
after its outcome poll ends, up to `3600` s after `T0`, so a walk formed inside that window could count a slow
interval as a non-member and a later walk admit it. §0.8 and §3.2 bar that.

**Two duties carried here by the map:** the chain book's interlock on Tier C over this look's units (map §2.5;
this TZ's §3.10), and the reclaiming of `/root/tz16a-work/` (map §3; this TZ's §9).

---

## 2. Scope

**Repository paths this TZ may write, and no others:**

1. `research/tz19-phase2-second-look.py` — new file, on branch `tz-19-phase2-second-look`, then a pull request.
   Not merged by the Executor.
2. `CryptoReports/TZ-19-phase2-second-look-report.md` — straight to `main`, in one commit, as contract §4.1
   requires. **The one path pushed to `main`, and the exemption to item 5 below.**

**Host paths this TZ may write:** `/root/tz19-work/**` — its worktrees, run directories and label ledger — and
`/root/btc-forensics/`, by exclusive create only (§9). **Host paths it removes, under §9 and nothing else:**
`/root/tz16a-work/`, its two worktrees first, and `/root/tz15-work/` and `/root/tz18a-work/` where §0.2 finds
them.

**Prohibited, each absolutely:**

1. No committed file is modified. Every `frozen` row of map §0 is byte-identical at run end.
2. Nothing under `/var/lib/btc-recorder/` is created, written, moved or removed; every file there is opened
   read-only. The recorder is never signalled, stopped or restarted.
3. Nothing under `/var/lib/btc-chainbook/` is created, written, moved or removed, and **only files named
   `window.json` and the file `runtime.jsonl` are opened there**, read-only — map §2.5's exception, counts,
   times and token ids. No `books.jsonl.gz`, no `documents.jsonl`, no reply body. The chain book service is
   never signalled. **Exemption:** block K-18a, under §4.2's FIRE and no other condition.
4. `/root/tz04a-env/`, `/root/tz01-env/`, `/root/btc-forensics/` and `/root/tz18a-svc/` are never removed or
   emptied. **Exemption:** §9 copies files into `/root/btc-forensics/` by exclusive create.
5. Nothing is pushed to `main` except the report of item 2 above.
6. **No label of the span is read before §3.7's constants are on disk and the scoring commit is on `origin`.** A
   label is the venue's resolved outcome. **Three exemptions, each named because this TZ's body requires it:**
   (a) `tz06.qualification`, which `tz06.scoring_set` calls for every unit considered and which reads
   `resolved_up` and `priceToBeat` through `analyze.venue` to decide membership on their existence alone — in
   this look's set and in the rehearsal's (§5.3), which lies below the reserve;
   (b) `tz10b.m2_labels`, the one label reader this TZ calls, once per scored run at §3.8;
   (c) `tz16a.dependence` over the store's copy of TZ-15's observations file (§3.1), whose `label` and `y`
   columns are outcomes of TZ-15's set, below the reserve, read and scored by TZ-15, and enter `r` and V4 (a)'s
   sums alone. **The rehearsal reads no label at all:** its labels are synthetic (§5.3).
7. **The instrument computes no probability itself.** `p_t` is the `p_t` field of `tz11a.checkpoint_row`, and
   nothing in the instrument's own syntax tree calls any of the twelve `pfair` entry points
   `tz15.PFAIR_PROBABILITY` names. **Exemption:** `tz11a.checkpoint_row` computes `p_t` and three further link
   quantities internally; the instrument keeps `p_t` alone.
8. **No settlement-derived quantity enters any pricer row:** the rows carry exactly the nine keys of
   `tz15.ROW_KEYS`, asserted by `tz15.label_free`.
9. **The reserve beyond this look is not touched.** No file but `manifest.json` is opened in any interval
   directory whose `T0` exceeds the last unit §3.2 considers — the 3,600th member — nor, in the rehearsal, the
   last unit of its own set.
10. **Nothing is read at another `tau`.** No touch, selection, price, constant, label or statistic of the span
    is taken at any `tau` but 240. The committed functions compute others internally — `tz11a.walk_member` at
    every `pfair.TAUS`, `tz14.quote_lines` over all fourteen reads of a quote file, `tz16a.dependence` over
    TZ-15's five `tau` — and TZ-16a's constants file holds all five, parsed whole for `per_tau["240"]` alone
    (§3.6); the rest is discarded. The labels read are those of the members eligible at 240, and no others.
    §3.10's `quotes_complete` is a manifest's flag for its whole interval, not a figure at any `tau`.
11. **No request to any venue**, by the instrument or by the session: no HTTP, no websocket, no socket. `git`
    against `origin` is the only network use.
12. No fit is performed, and no constant is produced for any file but this run's own output: §3.7's constants.
13. No Release is created, and no dataset, archive or binary enters git history.

---

## 3. The measurements

### 3.0 Partitions and counts

- **`LOOK_TAU` = `240`**, the one `tau` of this look (§2 item 10).
- **This look:** the first **3,600** qualifying slots with `T0 > 1789669800`; checkpoints **3,600** =
  `3,600 × 1`; reads at `tau` 240 **7,200** at full completeness = `3,600 × 2`.
- **Two parts, by `T0` alone:** the **first** — units with `T0 <= 1790452200`, TZ-16a's **2,608** units
  considered and **2,400** members (TZ-16a report §2) — and the **later** — units with `T0 > 1790452200`, whose
  members number **1,200** = `3,600 − 2,400`.
- **TZ-15's labelled set, for §3.1 alone:** its selected members at `tau` 240, **405** (TZ-15 report §4).
- One checkpoint per member. The two looks share the first part's outcomes, so they are dependent; the union
  bound of §4.1 holds whatever that dependence is.

### 3.1 `r`, carried from TZ-16a

`/root/btc-forensics/tz15-work--run1--tz15-observations.csv`, the copy TZ-16a §9 made (TZ-16a report §12), must
be a regular file whose SHA-256 is `a7ac8a495e00e21cd34af6ead7f05e9a2b741231c928bb61d4ec03ec0e610ce6` (TZ-15
report §12); **absent or different: BLOCKED** at step 4, before any file of the span is opened. Then
`dep, data_rows = tz16a.dependence(path)` — which reads TZ-15's eighteen columns, selects each `tau`'s selected
rows in ascending `T0`, and asserts the dependence defined at each of TZ-16a's five `tau` — and, at `tau` 240,
**V4 (a), twelve comparisons, each an equality of values and each BLOCKING:**

- `dep[240]`'s `n` is `405`, `sum_y` is `210`, `sum_a` equals `D("216.23")` and `sum_q` equals
  `D("233.579362178548589456")`; the dependence's `sum_x` equals `D("-6.23")` and `sum_x2` equals `D("73.3583")`
  — six values `tz16a.tables` printed exactly, TZ-16a report §1;
- `ρ_1`, `ρ_2`, `ρ_3` and `f̂`, each rounded to 20 significant digits by `decimal.Context(prec=20).plus` — the
  rounding `tz16a._sig` printed them with — equal `D("-0.092709701432514573337")`,
  `D("-0.11424575696332938083")`, `D("0.077424548483935820626")` and `D("0.74093818017618373293")`, TZ-16a
  report §1;
- `f` equals `D(1)`, and **`r` equals `D(1)`** — the value TZ-16a §4.2 requires this look to carry, printed by
  `tz16a.tables` in TZ-16a report §1 and §4.

`r` is `1`, so the tails of §3.7 are the exact Poisson-binomial tails (TZ-16a §3.7). **Printed:** the path, its
SHA-256, `data_rows`, and the twelve figures as computed beside the values they equal.

### 3.2 The set

`rows, whole = tz06.scoring_set(manifests, 3600, after=1789669800)`, `manifests = load_manifests()`, unchanged;
`members` the `T0` of every row whose `member` is set. **Asserted:** `whole` is true; `len(members)` is `3600`;
the first unit considered has `T0 = 1789670100`; consecutive units differ by exactly `300`; the last unit
considered is the last member; **and the host clock at this step is at least `members[-1] + 3900`** (§0.8's
reason). A failure of `whole` or of the clock condition is BLOCKED, with the counts, the first and last unit and
the clock printed, before any quote file or market document is opened.

**The first part is TZ-16a's set — V4 (b), BLOCKING:** the units considered with `T0 <= 1790452200` number
exactly `2,608`, and `tz07b.member_list_sha` over their members equals
`3dde75b6d634a5b35fb3b2d654840781c0142de2bfbb64f601549bc3b5c02ab2`, printed by `tz16a.tables`, TZ-16a report §2;
the Architect re-derived it on 2026-09-28 from the 208 non-members that report discloses. So `members[:2400]` is
TZ-16a's set, and `members[2400:]` the later part's 1,200.

**Printed, for the whole set and for each part:** the units considered, the members, `tz07b.member_list_sha` of
those members, the first and last member in UTC, the members per weekday by `tz14.weekday_of`, the weekend
members by `tz14.is_weekend`, and every non-member with its reasons.

### 3.3 The pricer at `tau` 240

For each member, `walked = tz11a.walk_member(t0, manifests, False)`, then
`full = tz11a.checkpoint_row(t0, "tz19set", 240, walked[240])`, and the row kept is
`{k: full[k] for k in tz15.ROW_KEYS}` — **the pricer row**, `label` `None` by `checkpoint_row`'s own body until
§3.8. Everything §3.4 to §3.7 derive is kept in records keyed by `T0`, never in the pricer row. **An
`AssertionError` from `walk_member` is BLOCKING**, the member and the message printed. Printed, whole and per
part: the admissible count, weekday and weekend by `tz14.is_weekend`.

### 3.4 The quotes at `tau` 240

TZ-15 §3.3's rule, unchanged, at `tau` 240 alone — TZ-16a §3.5's text with "a `tau` in `ADMITTED`" read as
"`tau` 240". Per member `docs = tz14.documents(t0)` and `lines = tz14.quote_lines(config.interval_dir(t0))`; for
each read whose `tau` is `240`, whose `status` is `200` and whose `body_is_json` is true:
`book = tz14.book_of(read["raw"])`, then
`touch = tz14.touch_of(book, D(str(book["min_order_size"])), D(str(book["tick_size"])))` — the venue's own
minimum size and tick from the same reply. The read's side is `docs["tokens"][read["token_id"]]`. **A read at
240 that is not `200` or not JSON, whose `book_of` result has `ok` false, whose book lacks `min_order_size` or
`tick_size` (`book_of`'s `_present` keys), or whose token is outside the member's mapping, and a member whose
`gamma.json` is not usable, is listed with its reason, counted and contributes no touch — not BLOCKING.** A read
at any other `tau` is skipped before `book_of`. Per member: `ask_up`, `bid_up`, `ask_dn`, `bid_dn`, each
`touch["ask5"]` or `touch["bid5"]` of that side's reply, or `None`. Printed, whole and per part: the reads at
240 present, the reads used, and the listed reads by reason.

### 3.5 Eligibility, selection, and what the pricer claims — label-free

TZ-15 §3.4's rule, unchanged. **Eligible:** an admissible member at whose checkpoint `ask_up` or `ask_dn`
exists. `p = D(repr(row["p_t"]))`; `tz15.select(p, ask_up, ask_dn)` takes the side with the larger after-fee
edge where it is strictly positive — the fee through `tz14.fee_pp`, a tie to `Up` — and gives the price paid `a`
and `q`, the probability `p_t` gives the side bought: `p` for `Up`, `1 − p` for `Down`; the fee of a selected
trade is `tz14.fee_pp(a)`.

**Reported, whole and per part, before any label exists** — TZ-16a §3.6's list at `tau` 240: the admissible,
eligible and selected counts; the selected by side and by weekday against weekend; the count of checkpoints
where both edges are positive; the count of selected trades priced at or below `0.10`; `tz14.q_summary` of `a`
and of `q − a`; the mean claimed edge `Σ(q − a) / n` and after the fee `Σ(q − a − fee(a)) / n`; and, over
eligible checkpoints whose Up book is two-sided at the touch, `tz14.q_summary` of
`D = p − (bid_up + ask_up) / 2` and the share at which `|p − 0.5| < |mid − 0.5|`.

### 3.6 The first look, reproduced — label-free and BLOCKING

Over the first part's 2,400 members at `tau` 240, before any label, **V4 (c), twenty-seven comparisons**. Any
difference is BLOCKED.

**Eighteen against values TZ-16a's instrument printed** — rows 1 to 4, 6, 8 and 9 in TZ-16a report §3 by
`tz16a.tables`; rows 5 and 7 in TZ-16a report §10's V11 table, from `tz16a.disclosure_text`; rows 10 to 18 in
TZ-16a report §4 by `tz16a.tables`:

| # | quantity, over the first part at `tau` 240 | TZ-16a's value |
|---|---|---|
| 1 | admissible members | `1483` |
| 2 | reads at 240 present | `4800` |
| 3 | reads at 240 used | `4800` |
| 4 | eligible members | `1483` |
| 5 | `tz07b.member_list_sha` of the eligible | `5fc5b94e5cb5d391a5c46308268fe2c99a5d10ddd5edb22e3a1e0d7860e49484` |
| 6 | selected members, `n1` | `945` |
| 7 | `tz07b.member_list_sha` of the selected | `2c1c39aec57a5730bc6fe0a79ca189e74994344869c7713a8f7bab43ddc449cb` |
| 8 | selected `Up` | `496` |
| 9 | selected `Down` | `449` |
| 10 | distinct prices among the selected `a` | `89` |
| 11 | `Σa` | `D("525.72")` |
| 12 | `Σq` | `D("567.902433683916709065")` |
| 13 | `c` | `566` |
| 14 | `d` | `528` |
| 15 | `FP_E` | `D("0.00170213713160056625910163243813095567039655765171302527338886")` |
| 16 | `FP_N` | `D("0.001631685734694615821240826196880574159722358531144310508872")` |
| 17 | `POWER_E` | `D("0.571920372074725632384781778978885030004533830294336119721187")` |
| 18 | `POWER_N` | `D("0.580550561108921789752401844256881201279560773392839507672289")` |

Rows 13 to 18 are `tz16a.look_constants(a1, q1, r, D("0.002"), D("0.002"))`, `a1` and `q1` the first part's
selected weights in ascending `T0` and `r` §3.1's.

**Nine against TZ-16a's own constants file** — the file its instrument wrote before any label was read, so the
check is equality with that file's values and each literal above is that value at full precision (map §7 item
82). `tz16a-constants.json` is every regular file under `/root/tz16a-work/` whose SHA-256 is
`d79c9f44957d923e828b9157952f1f7b2a01cf9e35deead91ebc44faa16493be` (TZ-16a report §4 and §10), located at step
4; TZ-16a's four runs left four copies, the first in sorted path order is read, and the number of copies is
reported; **none: BLOCKED** at step 4. It is parsed as JSON for `per_tau["240"]` and nothing else: its
`members`, a list of records with the keys `T0`, `side`, `a`, `q` and `fee`, equals the first part's selected
records at 240 in ascending `T0` — `T0` and `side` as written, `a`, `q` and `fee` as `Decimal` values, one
comparison over the list; and its `mu0`, `mu1` and its `look`'s `c`, `d`, `FP_E`, `FP_N`, `POWER_E` and
`POWER_N` equal this run's rows 11 to 18 as values — eight. The file holds no label: TZ-16a wrote it at its step
9, before its step 12's read (TZ-16a §5.1).

Each comparison is an equality of integers, of strings for rows 5 and 7 and the sides, or of `Decimal` values.
**This look's coins contain the first look's:** a difference means the pipeline no longer reproduces the look
TZ-16a read, and nothing is read on it.

### 3.7 The gate's constants — exact, from prices, `p_t` and `r`, on disk before any label

Over the `n` selected members of the whole set at `tau` 240, in ascending `T0`: the weights `a` and `q`;
`U0 = tz15.pb_upper(a)` and `U1 = tz15.pb_upper(q)`; `μ0 = Σa` and `μ1 = Σq`; and
**`tz16a.look_constants(a, q, r, D("0.008"), D("0.008"), (U0, U1))`** — TZ-16a §3.7's six figures at
`α2 = β2 = D("0.008")`:

- **`c`** — the smallest `s` in `0 … n` with `up(U0, μ0, r, s) <= α2`, and `n + 1` where none exists; **`FP_E`**
  at it, `0` where `c = n + 1`: the probability that a market calibrated at its ask reads EDGE.
- **`d`** — the largest `s` in `0 … n` with `low(U1, μ1, r, s) <= β2`, and `−1` where none exists; **`FP_N`** at
  it, `0` where `d = −1`: the probability that NO EDGE is read if the pricer is right.
- **`POWER_E`** and **`POWER_N`**, each `0` at its unreachable end. They decide nothing.

**Asserted:** `FP_E <= α2` and `FP_N <= β2`; and **V4 (d)** — `r` is `1`, so `c` and `FP_E` equal the first two
values `tz15.crit(a, D("0.008"))` returns. At `r = 1` TZ-16a §3.7's independence columns are this look's own,
and no projection is computed: no look follows this one.

**Printed, for the Architect's re-derivation** (map §7 item 70): `n`, `μ0`, the null's weights as a table of
distinct prices with their counts — which fixes `U0` exactly — and `Σq`, `Σq²`, `Σq³`, `Σq⁴`, which fix the
alternative's first four cumulants. **The two looks' combined rates:** this look's `FP_E` plus the first look's,
§3.6 row 15, and this look's `FP_N` plus the first look's, row 16, each at most `0.01`. **Per part,
label-free:** the selected count, `Σa` and `Σq` of the first part — §3.6's rows 6, 11 and 12 — and of the later
part.

All of it, with every selected member's `T0`, side, `a`, `q` and `fee(a)` and §3.1's figures, is written to
**`tz19-constants.json`** before §3.8 begins. `tz15.label_free` is asserted over every pricer row before and
after the write.

### 3.8 The labels, read once

Only in a run started with `--score`. Before the read the instrument asserts that
`origin/tz-19-phase2-second-look` is among the branches `git branch -r --contains HEAD` prints, with `HEAD` from
`git rev-parse HEAD` — each a fixed argument list with no shell — so no label is read by a commit that is not on
`origin` (map §7 items 54 and 63). Then **`tz10b.m2_labels(sorted(E))`** is called once, `E` the members
eligible at 240, and one line is appended to `/root/tz19-work/label-ledger.jsonl`: the UTC instant, `HEAD`, the
member count and `tz07b.member_list_sha(E)`. A run with none of `--selftest`, `--rehearse` and `--score` stops
after §3.10 with its constants on disk and reads no label; **every run on the span before the push is such a
run**; the rehearsal, on TZ-14's span, reads none (§5.3); and `--selftest` stops at step 3, before any interval
directory is opened (§5.1).

### 3.9 The observed statistic, the reading, and what surrounds it

At `tau` 240: `y` the label for `Up` and one minus it for `Down`; **`S = Σy`** over the selected trades;
`T = (S − μ0) / n`; `T_fee = T − Σfee(a) / n`; the win rate `S / n` beside the mean `a` and the mean `q`; and
§4.1's reading, `tz16a.read_look(n, S, c, d)`, with the row of §4.1 that gave it and its claim-rejected flag.
Where `n = 0` every ratio is printed as undefined and no unit leaves or joins any denominator (map §7 item 64).

**Influence** (map §7 item 27), where `n >= 2`: with `x = y − a`, the member whose `|x − T|` is largest — ties
to the smallest `T0` — is removed, and `μ0`, `μ1`, `U0`, `U1`, `c`, `d`, `FP_E`, `FP_N`, `S` and the reading are
recomputed exactly on the `n − 1` through `tz16a.look_constants` at the same `r`, `α2` and `β2`, printed beside
the value §4.1 reads. Recorded, not a reading; where `n < 2` it is printed as undefined.

**The split by part, barred from every reading:** `S` over the first part's selected trades, printed beside
TZ-16a's `538` (TZ-16a report §6) — the same outcomes read a second time, recorded and not asserted, because
nothing after step 12 raises — and over the later part's selected trades `n`, `S`, `μ0`, `μ1` and `T`, `T`
undefined where that `n` is `0`.

**Diagnostics, each barred from every reading:** over the eligible checkpoints whose Up book is two-sided at the
touch, the mean label, the mean mid, the mean `p_t`, and the Brier score of the mid and of `p_t`, each printed
as undefined where no such checkpoint exists; and **`tz16a.residual_dependence` over this look's selected
residuals `y − a` in `T0` order** — `ρ_1`, `ρ_2`, `ρ_3`, `f̂` and `f`, or undefined with its reason — the
after-the-fact check of the dependence §3.1 carries.

**Nothing from step 12 onward raises on the labels or on any quantity computed from them.** Every figure of this
section is total, as its sentences above state. The assertions after step 12 are facts about the run — V8's,
V9's and host read 3's — and no label can trip one: a stop after the read would leave labels read and no reading
(map §7 item 83).

### 3.10 The chain book's interlock on Tier C — label-free and price-free

**`tz16a.interlock(rows, manifests)`, unchanged,** `rows` §3.2's units considered — every unit this look
considered, map §2.5's duty for this look's own units. TZ-16a §3.10 and §4.3 define every term and the function
implements them: a unit is **exposed** where `T0 >= 1790185200`, `T0 mod 900 = 600` and
`/var/lib/btc-chainbook/{T0 − 600}/window.json` is present, **fully loaded** where that file's `missed` is the
integer `0`; every other unit with a manifest is the **control**; a **failure** is a manifest whose
`quotes_complete` is not JSON `true`; a unit with no manifest is listed apart; `p_I` is Fisher's one-sided exact
test in `Fraction`; the chain book's `runtime.jsonl` is read for the start record of pid `2699889` at `wall_ns`
`1790185190022755903` and any `stop` record after it; the reading and its power come from
`tz16a.interlock_reading` and `tz16a.interlock_power`, which it calls. **Printed:** the four counts, and the
same split by era, `T0 < 1790185200` and after; the fully loaded count; every failure's `T0`; `p_I` exactly and
to ten decimals; §4.2's reading and its power; every record of the chain book's `runtime.jsonl`.

### 3.11 Predictions, pre-registered, barred from every gate and every reading

| # | prediction | population |
|---|---|---|
| P1 | the eligible count equals the admissible count | the 3,600 members at `tau` 240 |
| P2 | the reading is NO EDGE | §4.1's reading |
| P3 | `f < 1.3` on this look's own residuals | §3.9's own-look `residual_dependence` |
| P4 | the interlock reads HOLD | §4.2's reading |
| P5 | the mid's Brier score is below `p_t`'s | §3.9's eligible two-sided Up books at `tau` 240 |

**The basis, written so the report can say which part failed.** On the first look the side won `538` against the
ask's `525.72` and the pricer's `567.902` (TZ-16a report §6). The count's variance is `Σw(1 − w)` under each
law: `178.316` under the pricer's — `Σq − Σq²`, both printed in TZ-16a report §4 — and `185.517` under the ask's
— `Σa − Σa²`, from that section's distinct-price table. The shortfall against the claim was `−2.239` standard
deviations and the excess over the ask `+0.902`. Kept at the same rate per trade over one and a half times the
trades, each scales by `√1.5`: the first to `−2.743`, past NO EDGE's `0.008` lower quantile of the normal,
`−2.409`, and the second to `+1.104`, short of EDGE's `+2.409`. P1 rests on the book at 240 — both sides quoted
at every read four minutes out (map §2.3) and 1,483 of 1,483 admissible members eligible on the first look. P3
rests on the martingale property of a calibrated market's residuals: `f̂` was `0.741` on TZ-15's set and `0.955`
on the first look at 240. P4 rests on the base rate: `0` of `2,016` before the service started (map §4), and `0`
of `297` exposed and `0` of `2,311` control on the first look. P5 rests on both earlier sets, where the mid's
Brier score was the lower at every `tau` (map §4).

---

## 4. The gate

### 4.1 The reading at `tau` 240 — TZ-16a §4.1's table, unchanged, in this order

| condition | reading |
|---|---|
| `n = 0` | **UNDECIDABLE** — nothing was selected, so nothing is measured |
| `S >= c` | **EDGE** — whatever the powers are |
| `S <= d` | **NO EDGE** — whatever the powers are |
| otherwise | **UNDECIDABLE** |

Through `tz16a.read_look`. Where `S >= c` and `S <= d` both hold — the side won more often than its price
implied and less often than the pricer claimed — the reading is EDGE and the report states that the claimed size
is also rejected. **No row reads a power:** each answer comes from its own exact test, and power decides nothing
after a label is read (CANON PART II).

**Error rates, fixed here, under the model each test scores** — independent coins at the stated weights, their
count's deviation widened by `r`, which is `1`: `FP_E <= 0.008` and `FP_N <= 0.008` at `tau` 240 on this look,
each exact under that model. With the first look's `0.002`, each answer's false-reading probability at 240 is at
most `0.01` by the union bound, whatever the dependence between the looks; both sums are printed (§3.7).
**Power, stated before any label and deciding nothing:** `POWER_E` against the pricer's law and `POWER_N`
against the market calibrated at its ask.

### 4.2 The interlock — TZ-16a §4.3, unchanged

**FIRE** where `f_E >= 1` and `p_I <= 0.01`; otherwise **HOLD**. False-alarm probability at most `0.01`,
exactly, under exchangeability. **Power, printed:** `k*`, the smallest `k >= 1` at which `k` exposed failures
and none in the control give `p_I <= 0.01`, and the exact probability that a binomial count over `m_E` exposed
units at `q` = `0.01`, `0.02` and `0.05` reaches `k*`.

**Under FIRE**, after V3's comparison and before §9, block K-18a — TZ-18a §6.1, verbatim:

```
P=$(pgrep -fx '/root/tz01-env/venv/bin/python -B -u /root/tz18a-svc/tz18a-chainbook-capture.py --serve'); echo "pid=[$P]"; test -n "$P" && kill -TERM $P; echo "exit=$?"
```

The Executor runs the block once. If the session's classifier refuses it (map §6), the Executor prints it, the
Boss runs it verbatim in a root shell on the VPS, and the Executor waits. **Verification is the Executor's,
never the Boss's account:** `30` s after the block, `pgrep -fx` with the same argv prints no line and exits `1`,
and `/var/lib/btc-chainbook/runtime.jsonl` holds a `stop` record with the pid the block printed, later than that
pid's `start`. If the process is alive `120` s after the block, the same block with `-KILL` in place of `-TERM`
is authorized by the same route; a `stop` record then missing is disclosed beside the `pgrep` read, which
decides. **Under HOLD the block is never run.**

**Phase 2's reading stands under either.** A read the load broke removes a checkpoint from eligibility, an event
fixed before the outcome and blind to it, so it cannot move `S` against either law.

### 4.3 The verdict — fixed here, before any label of this look is read

Through `verdict_of(reading)`, a pure function whose three answers §5.2 item 14 fixes word for word:

| reading at 240 | Phase 2 | what follows | map §2.3's reserve |
|---|---|---|---|
| **NO EDGE** | **NO EDGE at all five `tau`**, closed, for the Student pricer inside its domain — 180, 120, 90 and 60 by TZ-16a's first look, 240 by this one. It says nothing about any other pricer | no Phase 2 TZ; Phase 3 does not open | **released** once this report is on `main` |
| **EDGE** | **YES at 240, subject to confirmation** on the qualifying slots after this look's 3,600th member (TZ-16a §4.2); NO EDGE at the other four | the confirmation TZ, written only on this EDGE and before any label of those slots is read; Phase 3 does not open on it | **held** for the slots after the 3,600th member, on map §2.3's terms; released up to it once this report is on `main` |
| **UNDECIDABLE** | **240 undecided, and final under TZ-16a's rule:** its two looks and their `0.01` per answer are spent, and this TZ fixes no third. It closes nothing and admits nothing (CANON PART II); NO EDGE at the other four | no Phase 2 TZ; Phase 3 does not open | **released** once this report is on `main` |

**What the gate assumes, named:** that outcomes of different intervals depend on one another, given the prices,
no more than `r = 1` allows at 240 — to the third neighbour, and as TZ-15's span showed it; §3.9 prints the same
statistic on this look after the fact. **What it does not decide:** depth beyond the venue's minimum size, the
50 ms taker delay and the oracle basis — Phase 3's. `T_fee` is printed beside the reading and gates nothing.
**This report on `main` is Phase 2's second look, the one TZ-16a §4.2 fixed and map §5 describes**, and the
condition map §2.3 sets before the backup track's B2 reads the span.

---

## 5. Implementation

### 5.1 The file, and the fixed order of the run

One new file, `research/tz19-phase2-second-look.py`. It loads **`tz16a-phase2-decisive-gate.py`** once, through
an `importlib` helper of the shape of `tz16a._load`, bound to the module-level name `tz16a`, and takes `tz15`,
`tz14`, `tz12`, `tz11a`, `tz10b`, `tz07b`, `tz06`, `pfair`, `config`, `D` and `load_manifests` from that one
module object; `analyze` and `manifest` are then imported by name. **Nothing is loaded a second time.** **The
load has side effects this TZ names:** `tz16a`'s module body loads `tz15`, whose body writes
`OPENBLAS_NUM_THREADS`, `OMP_NUM_THREADS` and `MKL_NUM_THREADS`, loads `tz14` — which writes the same three,
loads `tz12` and everything below it, and installs an audit hook appending to `tz14.CAPTURE_OPENS` — and
installs its own hook appending to `tz15.OPENS`; `tz16a`'s body then installs a hook appending to `tz16a.OPENS`.
None of the three can be removed, and this instrument reads none of their lists. **It installs its own hook**,
which records the absolute path, the mode, the flags and the current step of this section for every open under
`/var/lib/btc-recorder/` and `/var/lib/btc-chainbook/`.

**From `tz16a` it calls ten functions and no other:** `up`, `low`, `critical_upper`, `critical_lower`,
`look_constants`, `dependence`, `residual_dependence` and `read_look` — the eight TZ-16a §4.2 names — and
`interlock` and `selftests`; it may also call nine of `tz16a`'s total helpers, `_fixed`, `_sig`, `_exact`,
`_frac10`, `_ratio`, `_jsonable`, `_dumps`, `_utc` and `_row_of`, and read its constants. Every such call is
written `tz16a.<name>(…)`. **It defines no function named any of these twelve:** the eight, `interlock`,
`fisher_upper`, `interlock_reading` and `interlock_power`. From `tz15` it calls `pb_upper`, `crit`, `select` and
`label_free` and reads `ROW_KEYS` and `PFAIR_PROBABILITY`. **It calls none of these eleven:** `analyze.venue`,
`tz11a.fit_student`, `tz14.v1_gates`, `tz14.selftests`, `tz14.build`, `tz14.main`, `tz15.v1_gates`,
`tz15.selftests`, `tz15.reading`, `tz15.build`, `tz15.main`.

**Functions, each with the contract named here:** `v1_gates` (§0.1); `carried_r` (§3.1, V4 (a)); `the_set`
(§3.2, V4 (b)); `rehearsal_set` (§5.3); `rows_at` (§3.3); `quotes_at` (§3.4); `trades_at` (§3.5);
`label_free_at` (§3.5, whole and per part); `first_look` (§3.6, V4 (c)); `constants_at(trades, r, alpha, beta)`
(§3.7 and V4 (d)); `labels` (§3.8); `synthetic_labels` (§5.3); `observed_at(trades, consts, read)`,
`influence_at(trades, consts, obs)`, `split_at(trades, read)` and `diagnostics_at(trades, read)` (§3.9, each
total); `verdict_of(reading)` (§4.3, pure); `predictions_at` (§3.11); `v2_static`, `v6` and `selftests` (§5.2);
`build`, `tables`, `csv_text`, `disclosure_text`, `readings_text`, `constants_text`, `run_text` and `main`.
`trades` is keyed by `T0` and holds one record per member at `tau` 240, with the keys `T0`, `tau`, `admissible`,
`eligible`, `selected`, `side`, `a`, `q`, `fee`, `p`, `ask_up`, `bid_up`, `ask_dn`, `bid_dn`, `e_up`, `e_dn`,
`edge` and `both_positive`. **`constants_at`, `observed_at`, `influence_at`, `split_at`, `diagnostics_at` and
`verdict_of` are pure:** each is a function of its arguments alone and opens nothing, so §5.2 calls them with
literals.

**Modes:** `--selftest` runs steps 0 to 3 and stops — the only file it opens under a capture root is the
recorder's `runtime.jsonl`, through host read 1; `--rehearse` runs §5.3; a run with none of `--selftest`,
`--rehearse` and `--score` stops at step 11; `--score` runs to the end. `--out` names the run directory, under
`/root/tz19-work/` and not existing before the run; every mode but `--selftest` requires it. **Every mode prints
each host read it makes — its UTC instant, its free bytes and its bound — so §0.4's list is complete** (map §7
item 84).

**The order of a run, and the instrument asserts it:**

0. `v1_gates`, §0.1, and V8's start half;
1. host read 1, through `tz11a.host_read(when, t0s, floor)` at `tz11a.FLOOR_START_BYTES` with `t0s` empty; its
   `newest_start_sha` asserted equal to `4216c04673ced76b5b2ac60ef57c9abedc46f9b9`;
2. the self-tests of §5.2, before any interval directory or chain book file is opened, **the first fail-fast of
   §6** among them;
3. `v6` and `v2_static`;
4. §3.1 — the store's file, `r`, V4 (a); and TZ-16a's constants file, located by hash (§3.6);
5. the set, §3.2, with its clock condition and V4 (b) — in `--rehearse`, §5.3's set;
6. the rows, §3.3; host read 2 over the members; **the second fail-fast of §6**;
7. the quotes, §3.4;
8. eligibility, selection and the label-free report, §3.5; **the first `label_free` assertion**; §3.6's V4 (c),
   except in `--rehearse`;
9. the constants, §3.7, with V4 (d), written to `tz19-constants.json`; **the second assertion**;
10. the interlock, §3.10;
11. with none of the three flags: the label-free files, host read 3, V8 and V9, and stop;
12. with `--score`: the push assertion and the label read, §3.8 — in `--rehearse`, §5.3's synthetic labels;
13. the observed statistic, the reading, the verdict, influence, the split and the diagnostics, §3.9 and §4, and
    the predictions, §3.11;
14. the files; host read 3; V8 and V9.

### 5.2 Self-tests — fifteen items, before any interval directory is opened, each an `assert`

**Items 1 to 12 are TZ-16a's, run by calling `tz16a.selftests()` unchanged** — its eleven items and **82**
assertions, distributed `14, 5, 4, 6, 6, 6, 19, 8, 8, 2, 4`, with TZ-16a §5.2's expectations, over seven of the
eight imported functions — `up`, `low`, `critical_upper`, `critical_lower`, `look_constants`,
`residual_dependence` and `read_look` — and `fisher_upper`, `interlock_reading`, `interlock_power`,
`tz15.pb_upper`, `tz15.crit` and `tz15.label_free`; the eighth, `dependence`, reads a file and is exercised at
step 4 by V4 (a)'s twelve comparisons. Its item 12 is the timing `t12` of `tz15.pb_upper` over 1,200 copies of
`D("0.37")`, which it returns as `t12_s` and which carries TZ-16a's own fail-fast (§6). **Items 13 to 15 are
this TZ's**, each an `assert`; every numeric comparison is between `Fraction` values converted exactly from
`Decimal`, a reading or a reason is compared with the exact word this TZ writes for it, a flag as a boolean, and
`None` as `None`.

13. **`tz16a.look_constants` at this look's allocation.** `a` twenty copies of `D("0.5")`, `q` twenty copies of
    `D("0.8")`, `r = D(1)`, `α = β = D("0.008")`: `c = 16`; `d = 10`; `FP_E = 1549/262144`;
    `FP_N = 247462024753/95367431640625`; `POWER_E = 60047937765376/95367431640625`; `POWER_N = 308333/524288`;
    and `tz15.crit(a, D("0.008"))` returns `16` and `1549/262144`. The denominators are `2^18`, `5^20` and
    `2^19`. **Eight assertions.**
14. **`verdict_of`.** `verdict_of("NO EDGE")` returns `phase2` `"NO EDGE at all five tau"`, `follows` `"none"`
    and `reserve` `"released"`; `verdict_of("EDGE")` returns `"YES at 240, subject to confirmation"`,
    `"a confirmation at tau 240"` and `"held after the 3,600th member"`; `verdict_of("UNDECIDABLE")` returns
    `"240 undecided, both looks spent"`, `"none"` and `"released"`. **Nine assertions.**
15. **The code after the label read is total**, on literal trade records at `tau` 240, `T0` the integers from
    `1`, each `admissible` and `eligible` with `ask_dn` and `bid_dn` `None`, and every other key of §5.1's
    record `None` or `False` unless named here: a **selected** record carries side `Up`, `a`, `q`, `p = q`,
    `ask_up = a`, `bid_up = a − D("0.01")` and `fee = tz14.fee_pp(a)`; the one **unselected** record, in (a),
    carries `p = D("0.5")`, `ask_up = D("0.5")` and `bid_up = D("0.49")`. Each case runs through `constants_at`
    at `r = D(1)` and `α = β = D("0.008")`, then `observed_at`, `influence_at` and `diagnostics_at`, with the
    labels given:
    (a) one record, unselected, label `1`: the reading `"UNDECIDABLE"`, the row `"n = 0"`, `T` `None`, influence
        undefined with the reason `"n < 2"`, and the own-look dependence undefined with the reason `"n < 4"`;
    (b) three records selected, `a = q = D("0.5")`, labels `1, 0, 1`: influence defined, and the own-look
        dependence undefined with the reason `"n < 4"`;
    (c) four records selected, `a = q = D("0.5")`, labels all `1`: the own-look dependence undefined with the
        reason `"v = 0"`;
    (d) ten records selected, `a = D("0.1")`, `q = D("0.9")`, labels `1` at the first five and `0` at the rest:
        `c = 5`, `d = 5`, `FP_E = 8174687/5000000000`, `FP_N = 8174687/5000000000`, `S = 5`, the reading
        `"EDGE"` and the claim-rejected flag `True`. **Fifteen assertions:** 5, 2, 1 and 7.

**One hundred and fourteen assertions over fourteen items:** TZ-16a's `14, 5, 4, 6, 6, 6, 19, 8, 8, 2, 4`, 82,
and this TZ's `8, 9, 15`, 32. Item 12 is a timing, not a test.

### 5.3 The rehearsal — `--rehearse`

Map §7 item 84: a TZ that forbids the code after its label read to raise provides, inside the instrument, a
rehearsal of that code on an already-scored span with synthetic labels.
**`--rehearse --out /root/tz19-work/<name>`** runs steps 0 to 10, 12, 13 and 14 of §5.1 with three differences
and no others:

- **Step 5** forms `rehearsal_set(manifests)`: `tz06.scoring_set(manifests, 40, after=1789206600)` — the first
  40 qualifying slots of TZ-14's set, whose quotes TZ-14 read and TZ-15 scored (map §2.3) — asserting `whole`
  and 40 members; no clock condition and no V4 (b). The whole rehearsal set is one part.
- **Step 8** skips V4 (c).
- **Step 12** reads no label: `synthetic_labels(E)`, `E` the rehearsal's members eligible at 240, gives each the
  label `int(hashlib.sha256(str(t0).encode("ascii")).hexdigest(), 16) % 2`. No push is asserted, no ledger line
  is written, and `tz10b.m2_labels` is not called.

Everything else — §3.1's `r`, the rows, quotes, trades and constants at 240 over the rehearsal's members, the
interlock over its units, and every function of steps 13 and 14 — is the code a scored run executes, writing the
same six files into its `--out`; `tz19-readings.json` and `tz19-run.json` carry `mode` `rehearse`, and
`tz19-tables.md` is titled a rehearsal with synthetic labels. **Its opens:** the settled document at step 5 once
per unit of its own set that has a manifest and that file, the set rule's own read, and `0` times at step 12;
nothing under the capture root with `T0 > 1789669800` but `manifest.json`.

### 5.4 The shape of the diff

One new file and nothing else. The list of committed lines the change replaces, read from `origin/main`, is
**empty**; `git diff --name-only` against the merge base prints exactly `research/tz19-phase2-second-look.py` on
the scoring commit, and a subset of it on any earlier tree.

### 5.5 What may be fixed inside the session

Before the scoring commit is pushed, a failed self-test or assertion whose cause is the instrument's own code
may be fixed, committed, and the run repeated; each such fix is disclosed with its commit, and H is repeated on
the commit that is pushed. **From the push onward, every clause that reads BLOCKED binds whatever caused the
failure, the Executor's own code included** (map §7 item 78). An expectation of §5.2 or §7 is never edited: a
wrong one is BLOCKED.

### 5.6 The runs, in this order

| run | what |
|---|---|
| **R-READY** | §0.2's host gate; then §0.8 — NOT YET stops here; then §0.5's first read and §0.6 |
| **B** | the two worktrees of §0.7; the build; `--selftest` as often as needed, and `--rehearse` at most five times in the session, H included |
| **C** | commit, before any run on the span, so that the runs a Validation row compares are of one commit |
| **H** | `--rehearse` on that commit, into `/root/tz19-work/rehearsal-c/` |
| **D1, D2** | at most two runs with none of the three flags, into `run-d1/` and `run-d2/`, each naming the commit it ran on; a fix between them only as §5.5 allows |
| **P** | push the branch; print `P_push`, `date -u +%s` as `git push` exits `0`, and `git ls-remote origin refs/heads/tz-19-phase2-second-look` |
| **S1, S2** | two runs with `--score` from fresh processes on the pushed commit, into `run-s1/` and `run-s2/`, after §0.5's second read |
| **V3** | `cmp` of S1's and S2's compared files, and of their constants with every run of that commit with none of the three flags |
| **K** | block K-18a, only under FIRE (§4.2) |
| **RT** | retention, §9 |
| **RP** | the report, from `/root/tz19-work/wt-report`, straight to `main` |

---

## 6. Cost

Every figure at the maximum of the population it bounds (map §7 items 52 and 62). Rates are this host's,
measured by TZ-16a in its scored run S1 (TZ-16a report §9).

| step | basis | seconds |
|---|---|---|
| gates, self-tests, `v6`, `v2_static` | TZ-16a measured `0.80`, its 82 assertions and item 12 among them; items 13 to 15 hold at most 20 coins | ~2 |
| the store's file and `r`, §3.1, and TZ-16a's constants file, §3.6 | TZ-16a measured `0.45` for step 4 with 182 files hashed; here one, and the files of `/root/tz16a-work/`, `22,167,020` bytes (map §3), with one `793,470`-byte parse | ~1 |
| the set, §3.2 | TZ-16a measured `40.85` for 2,608 units, `0.01566` a unit; here at most `4,500` units — 3,600 members at 80%, below the lowest share any set has qualified, 90.3% (map §2.3, TZ-06) | ~71 |
| the rows, §3.3 | TZ-16a measured `187.04` for 2,400 walks, `0.07793` a walk; here 3,600 | ~281 |
| the quotes, §3.4 | TZ-16a measured `8.24` for 2,400 members' files; here 3,600 | ~13 |
| the recursions, §3.6, §3.7 and §3.9 | at the unfiltered `n = 3,600`: two at `n` for `U0` and `U1`, one at `n` inside `tz15.crit` for V4 (d), two at `n − 1` for influence, and V4 (c)'s two at the first part's unfiltered `2,400` — `5 × 3,600² + 2 × 2,400²` = **`76,320,000`** units of `n²`, at the `0.3363` s per `1,440,000` TZ-16a's item 12 measured | ~18 |
| the interlock, §3.10 | at most one `window.json` per exposed unit, a third of 4,500; TZ-16a measured `0.44` for 297 | ~3 |
| labels, statistics, files, host reads | TZ-16a measured `5.03` for its steps 12 to 14 with 1,618 labels; here at most 3,600 | ~12 |
| **one run** | | **~401** |
| **a rehearsal** | steps 0 to 4, `2 + 1`; TZ-16a's whole step 5, `41`, as a bound for `load_manifests` and the 40-slot walk; 40 walks, `3`: `47` to its step 6, and about `1` for its quotes, constants, interlock, labels and files | ~48 |
| **the session: two runs with no flag, two with `--score`, and five rehearsals** | against `tz12.SESSION_CEILING_S` = `3600` | **~1,844** |

**Fail-fast, both asserted, both derived from the table:**

1. Item 12's timing, `t12`: the run projects `76,320,000 × t12 / 1,440,000` = `53 × t12` s of recursion and is
   BLOCKED above **`100`** s — `5.6` times the table's `18`. `tz16a.selftests` carries TZ-16a's own bound on the
   same `t12` — BLOCKED where its projection of `275,069,310` units exceeds `400` s, at `t12 > 2.094` s — and it
   binds too: either stop is BLOCKED.
2. After step 6 the run's elapsed time must be at most **`540`** s — the table's `2 + 1 + 71 + 281 = 355` s,
   times `1.52` — and in `--rehearse` at most **`72`** s — the rehearsal row's `47` s, times `1.52`, rounded up.

At both edges one run costs at most `540 + 13 + 100 + 3 + 12 = 668` s and four runs `2,672` s; a rehearsal at
most `72 + 1 = 73` s and five `365` s; `3,037` s in all, inside `3600`. Nothing is sampled and no simulation is
run: every constant is exact.

---

## 7. Validation

Each check states a count. **Asserted** means a Python `assert` or a `SystemExit` in the instrument that
produces the numbers, at the step of §5.1 named beside it; everything else is **recorded, not asserted**. Every
assertion holds on every run that reaches its step, in every mode.

| # | check | what it must produce |
|---|---|---|
| **V1** | gates — asserted, step 0, and §0 | 6 of 6 anchors, four re-derived; 25 of 25 `frozen`, 2 `tracked`, 1 `reported`; H1 to H3, H4 printed; R-READY's line and every NOT YET the session saw; §0.6's refs; the trees and the forensic count; the interpreter and `numpy` versions; every free-space read with its bound |
| **V2** | isolation — asserted two ways | **Static, step 3,** over the instrument's own tree: string constants carrying any of `tz14.BANNED_SUBSTRINGS`, docstrings exempt — **0**; calls of the twelve `pfair` entry points of `tz15.PFAIR_PROBABILITY` — **0**; call sites of `tz10b.m2_labels` — **exactly 1**; calls of §5.1's eleven never-called names — **0**; calls written `tz16a.<name>(…)` naming anything but §5.1's ten functions and nine helpers — **0**; function definitions named any of §5.1's twelve — **0**; imports of `urllib`, `http`, `socket`, `ssl`, `requests` or `websockets` — **0**; `subprocess.run` — exactly one call site, whose argument list begins with the literal `"git"`, with no `shell` keyword. **At run time,** from the instrument's hook: opens whose basename carries `tz14.BANNED_SUBSTRINGS[0]` — at step 5 one per unit considered that has a manifest and that file, the set rule's own read; at every other step before 12, **0**; at step 12 exactly the members handed to `tz10b.m2_labels` with `--score`, and **0** with `--rehearse`; and every pricer row carrying exactly `tz15.ROW_KEYS` with `label is None` at steps 8 and 9 |
| **V3** | determinism — **BLOCKING on any difference, checked by `cmp` after S2**, the one check that compares two runs | `tz19-constants.json`, `tz19-readings.json`, `tz19-tables.md`, `tz19-observations.csv` and `tz19-disclosure.md`, byte-identical between S1 and S2, with SHA-256 pairs; `tz19-constants.json` also byte-identical to every run of that commit with none of the three flags — the rehearsal's set is another, and its files are compared with nothing. `tz19-run.json` holds instants and timings, is not compared, and is named |
| **V4** | inputs — asserted | **(a) step 4:** the store's file by hash, and §3.1's **12 of 12**. **(b) step 5:** §3.2's assertions, and the first part's `2,608` units and member-list hash. **(c) step 8:** §3.6's **27 of 27**, the constants file located at step 4. **(d) step 9:** `c` and `FP_E` equal `tz15.crit`'s at `D("0.008")`. `--rehearse` asserts (a) and (d) |
| **V5** | the push precedes the label read — asserted, step 12 | `HEAD` among the branches containing it as `origin/tz-19-phase2-second-look`; `P_push` beside each label-read instant; the ledger printed whole, every line's commit equal to the reported one; a ledger line of any other commit disclosed and explained |
| **V6** | the diff — asserted, step 3 | merge base and head; `git status --porcelain` for the two scoped paths; `git diff --name-only` a subset of `{research/tz19-phase2-second-look.py}`, and exactly it on the scoring commit; no `global`, no `nonlocal`, no attribute store and no `os.environ` write in the file's own tree; the replaced-line list **empty** |
| **V7** | the self-tests — asserted, step 2 | TZ-16a's 11 of 11 items and **82** assertions, distributed `14, 5, 4, 6, 6, 6, 19, 8, 8, 2, 4`; item 12's time; this TZ's 3 of 3 items and **32** assertions, distributed `8, 9, 15`; **114** in all; the output verbatim |
| **V8** | the frozen files are not moved — asserted at step 0 and at the run's last step, 14 with `--score` or `--rehearse` and 11 with none of the three flags; `--selftest`, which stops at step 3, asserts step 0's half alone | `research/pfair.py`, `research/tz14-quote-inventory.py`, `research/tz15-phase2-gate.py` and `research/tz16a-phase2-decisive-gate.py`, each equal to map §0 at run start and at run end |
| **V9** | the captures are untouched — asserted at the run's last step, 14 with `--score` or `--rehearse` and 11 with none of the three flags; `--selftest`, which stops at step 3, asserts none of it | `tz11a.host_read` at steps 1, 6 and that last step: pid and start record unchanged between the first and the last, the directory count not fallen, the read-set hash unchanged between reads 2 and 3. From the hook: every open in mode `r`, none with `w`, `x`, `a` or `+`; **no open of any file but `manifest.json` in an interval directory whose `T0` exceeds the last member**; under `/var/lib/btc-chainbook/`, no open of any file but `window.json` and `runtime.jsonl`; the count of opens per basename; everything the instrument can write, enumerated — its `--out` directory and `/root/tz19-work/label-ledger.jsonl` |
| **V10** | the fingerprint table | every row of map §0 in lines, bytes and SHA-256, and the new file beside them as it stands on the branch |
| **V11** | disclosure | `tz19-disclosure.md`: every unit considered in ascending `T0` with UTC, weekday, part, reasons, the manifest's `quotes_complete` and the interlock group; the eligible and the selected `T0` lists at 240, whole and per part, each with its count and `tz07b.member_list_sha`; the listed reads of §3.4 by reason. `tz19-observations.csv`: **3,600 rows and a header**, one per member at `tau` 240, TZ-15's eighteen columns in TZ-15's order, `tz16a.OBS_COLUMNS` — sufficient to reconstruct every number of §3.5, §3.7 and §3.9 without re-running |
| **V12** | influence, the split, diagnostics, predictions — recorded | §3.9's influence line beside the reading, or undefined; the split by part, the first part's `S` beside TZ-16a's `538`; the diagnostics, §3.9's own-look `ρ_k` and `f` among them, or undefined with its reason; §3.11's five predictions, each held or refuted with its figure |
| **V13** | the interlock — asserted, step 10 | `m_E + m_C` plus the units with no manifest equal the units considered; `f_E <= m_E` and `f_C <= m_C`; `p_I` exact; §4.2's reading and power; under FIRE, run K's verification per §4.2 |
| **V14** | the rehearsal — asserted, run H | on the commit that is pushed: steps 0 to 10, 12, 13 and 14 visited in order; 40 members; V4 (a) and (d); the settled document opened at step 5 once per rehearsal unit with a manifest and that file, and **0** times at step 12; the six files written, with their SHA-256; its reading and its synthetic label count printed |

**Causality is not re-tested, and this is why.** `p_t` is `tz11a.checkpoint_row`'s own, which TZ-10b V2 proved
bit-identical under perturbation strictly after the checkpoint — 140 of 140, with 140 of 140 negative controls
(map §4). Every quote lands after its checkpoint, `+39.6` ms at the earliest over 16,800 reads (map §2.3). The
label is the one future quantity, and it enters nothing before step 12.

---

## 8. The report

`CryptoReports/TZ-19-phase2-second-look-report.md`, straight to `main` in one commit, immutable once committed.

**In its first ten lines:** the reading at `tau` 240, with `S`, `c` and `d`; Phase 2's verdict over the five
`tau`, per §4.3; the interlock's reading; what follows; and the disposition of map §2.3's reserve.

Then, in this order: §0's gates, host reads, readiness — every NOT YET the session saw among them — refs, trees
and every free-space read; §3.1's file and its twelve figures; §3.2's set, whole and per part, with V4 (b); §3.3
to §3.5's label-free report, whole and per part; §3.6's twenty-seven comparisons, with the constants file's path
and copies; §3.7's constants — `n`, `μ0`, the null's distinct prices with their counts, `Σq` to `Σq⁴`, `r`, `c`,
`d`, `FP_E`, `FP_N`, `POWER_E`, `POWER_N` and the two looks' combined rates — with the instant
`tz19-constants.json` was written; `P_push` beside each label-read instant (map §7 item 63); §3.9 — `S`, `T`,
`T_fee`, the reading and the row of §4.1 that gave it, influence, the split and the diagnostics; §3.10 and §4.2;
§3.11; the implementation, the file's hash on the branch and its commit; the rehearsal, H's output; V1 to V14
with their counts; publication with contract §4.2's self-check; §9; and every point where the text needed a
reading, with the workaround chosen. The order is this TZ's, with contract §8's content inside it.

It states `wc -l` and `sha256sum` for the map and every file its fingerprint table lists. **A report is
evidence, not acceptance:** no reading stands until the Architect has re-derived `c` and `FP_E` exactly from the
distinct-price table, `d`, `FP_N` and the powers within the four-cumulant approximation, and `S` from the counts
printed.

---

## 9. Retention

In this order, each step only after the previous one exited `0`, only after S2 and V3, and after run K where it
ran:

1. **Copy first.** Every file under `/root/tz16a-work/`, worktrees included, and under `/root/tz15-work/` and
   `/root/tz18a-work/` where §0.2 found them, whose SHA-256 is named by any committed report on `main` — every
   hexadecimal token of 16 to 64 characters those reports print, matched against the full hash and its
   16-character prefix, the predicate TZ-14, TZ-15 and TZ-16a used — and, by name,
   `/root/tz16a-work/label-ledger.jsonl`; each that `/root/btc-forensics/` does not already hold by hash is
   copied there by exclusive create, under its path below `/root/` with `/` replaced by `--`, the hash asserted
   at source and destination. Assert that the **1,072** files already there are unchanged. Report the counts
   before and after.
2. **Then the two worktrees:** `/root/tz16a-work/wt` and `/root/tz16a-work/wt-report`, each by
   `git worktree remove` without `--force`; an untracked `__pycache__` in one is deleted first and named; each
   verified by `test -e`.
3. **Then the trees:** `rm -rf /root/tz16a-work`, and `rm -rf /root/tz15-work` and `rm -rf /root/tz18a-work`
   where §0.2 found them — one command naming one tree each, each verified by `test -e`. If the session's
   classifier refuses one, hand the Boss that one exact block and verify the outcome from `test -e` afterwards,
   never from his report (map §6).

**Never removed:** `/root/tz18a-svc/`, from which the service runs — under FIRE its stop is verified and the
tree stays for the next TZ; both capture roots; `/root/tz01-env/`; `/root/tz04a-env/`; `/root/btc-forensics/`.
`/root/tz19-work/`, the label ledger included, is the next TZ's to reclaim on the same terms.

---

## 10. Pre-send checks

Performed against this file, start to end, as a separate reading after its last section was written, with the
repository cloned at `origin/main` `84b60206c0182b4fe5dbc457357a95726cec5faa` — PR #20's merge, above the upload
of map revision `2026-09-27-b`, which this file requires and which ships unchanged — the TZ-16a report at
`5935ca5`, and TZ-16a itself. **The first separate reading, with C1 to C8 run beside it, found twelve defects,
each repaired before the file was sent:** §0.8 said nothing under the capture root but manifests had been opened
at a NOT YET, while §0.2's `grep -c` reads the recorder's top-level `runtime.jsonl`; §0.8 did not name R-READY a
necessary condition beside the sufficient one, as map §7 item 84 requires; §5.1 did not make every mode print
the host reads §0.4 asks to be reported, which map §7 item 84 also requires; §3.8 stopped every run without
`--score` after §3.10, which the rehearsal is not; §3.10's `rows` did not say which rows; §5.2 credited TZ-16a's
self-tests with all eight imported functions, and `dependence` is not among them (C7); §5.1 left unstated the
purity map §7 item 83 requires of the functions §5.2 calls with literals; §6 bounded the session at its
fail-fast edges without bounding the rehearsals (C4); §1 and §4.3 said map §5 assigns the look to this TZ, where
map §5 describes it and names no TZ (C8); §3.11 printed `−2.742` for a figure that computes to `−2.74256`; §3.11
cited map §2.5 for the `2,016` base rate, which map §4 carries (C8); and the header said TZ-16a §4.2 "left" six
things to this TZ, two of which are the map's duties. **One improvement was made in the same reading:** §3.6
compares the first look against TZ-16a's own constants file, located by hash, as well as against its printed
values (map §7 item 82). **A second full reading, after those repairs, found four more, each repaired:** V3 and
§5.6 compared the constants file with every run without `--score`, which takes in the rehearsal, whose set is
another — V3 could not have held; §5.6's D1 and D2 and §5.1's modes named runs by `--score` alone where three
flags exist; §3.8 called every development run one that stops at step 11, which the rehearsal is not; and §2
item 10 did not say that §3.10's `quotes_complete` is a whole interval's flag and not a figure at another `tau`.
**A third full reading found two, both in this section's own text, each repaired:** C2 credited all 82 of
TZ-16a's expectations to computation, where 16 are exact by construction; and C7 named `_exact` as the printer
of every §3.1 sum, where `n` and `sum_y` print with `%d` and `sum_a` and `sum_q` with `%s`. **A fourth full
reading found two, each repaired:** §1 cited TZ-16a §3.2 alone for a sentence that is TZ-16a §1's; and §3.9
called the later part's `n` undefined where only its `T` can be. **A fifth full reading found one, repaired:**
§3.8, §5.1's step 11, V8 and V9 scoped a run's stop by `--score` and `--rehearse` alone, which takes in
`--selftest`, a run that stops at step 3 with nothing on disk; the same reading re-indented §2 item 6's
exemptions (b) and (c), which the file's reflow had misaligned. **A sixth full reading found one, in this
section's own text, repaired:** C8 listed map §3's references without §6, whose cost table cites it. **A seventh
full reading found none.**

**C1 — scope against body.** Enumerated from §0 to §9 by a script over this file's own text, then read: **8**
repository paths — two written, `research/tz19-phase2-second-look.py` and
`CryptoReports/TZ-19-phase2-second-look-report.md`; six read or named, `SYSTEM-MAP.md`, `research/pfair.py`,
`research/recorder/recorder.py` for one constant, `research/tz14-quote-inventory.py`,
`research/tz15-phase2-gate.py` and `research/tz16a-phase2-decisive-gate.py`; **40** host paths and path
fragments; **57** committed entry points and module attributes written as `module.name`; **6** output files and
the label ledger. Intersections with §2's prohibitions, by path and by content class: **12**, each resolved in
§2 where the prohibition is made — K-18a against item 3, as its exemption; §3.10's reads of `window.json` and
`runtime.jsonl` against item 3, which names them; §9's copy against item 4, as its exemption; the report's push
against item 5, as path 2; `tz06.qualification` with `analyze.venue` inside it, in the look's set and the
rehearsal's, `tz10b.m2_labels`, and `tz16a.dependence` over TZ-15's file against item 6, as its exemptions (a)
to (c); `tz11a.checkpoint_row`'s internal link quantities against item 7, as its exemption; the committed
loader's read of every manifest against item 9, which excepts `manifest.json`; `tz11a.walk_member`,
`tz14.quote_lines` and `tz16a.dependence` computing at other `tau`, and TZ-16a's constants file holding them,
against item 10, which names all four; `git` against item 11, which names it; and the rehearsal's opens of
TZ-14's span against items 6, 9 and 10 — below the reserve, named in item 6 (a) and item 9, and outside item
10's span. **By content class:** `tz19-constants.json`, `tz19-observations.csv`, `tz19-readings.json`,
`tz19-tables.md`, `tz19-disclosure.md` and the report carry prices, labels and outcomes of the span map §2.3
reserves for this look — item 6 orders their label content after the constants and the push, item 9 confines
them to this look's members and item 10 to `tau` 240; TZ-16a's constants file carries prices of the span and no
label, and TZ-15's observations file labels of TZ-15's set below the reserve, exemption (c); the rehearsal's six
files carry prices of TZ-14's already-scored span and synthetic labels, and no outcome; no output carries a
chain book price, since item 3 opens no body; and no fifteen-minute settled document is opened. §9's removal of
`/root/tz16a-work/`, `/root/tz15-work/` and `/root/tz18a-work/` meets no prohibition, and §2 names it. The diff
was performed, not intended.

**C2 — origin of every expectation.** **§5.2: 114 expectations**, one per assertion. **82**, items 1 to 11, are
TZ-16a §5.2's, quoted from the committed `tz16a.selftests` at `3cae67ee…` and run unchanged — 66 computed there
by the Architect in exact rationals and 16 exact by construction (TZ-16a §10 C2). **Item 13's eight** were
computed by the Architect on 2026-09-28 in exact rationals from `math.comb` binomials, an implementation that
shares nothing with the code under test, compared with tolerance `0`; two of them coincide with TZ-16a's own
item 2 (`up` at 16, `1549/262144`) and item 4 (`low` at 10, `247462024753/95367431640625`), an independent
cross-check. **Item 14's nine** are exact by construction, this TZ's words. **Item 15's fifteen:** (d)'s
`c = 5`, `d = 5` and the two rates `8174687/5000000000` — `P(Bin(10, 0.1) >= 5)` and `P(Bin(10, 0.9) <= 5)` —
computed the same way, with the neighbouring tails `7996999/625000000` above `0.008` on both sides; (d)'s
`S = 5`, `"EDGE"` and `True` by construction from its labels and §4.1's table; (a) to (c)'s eight by
construction — the row is `tz16a._row_of`'s word, the two dependence reasons `tz16a.residual_dependence`'s,
`"n < 2"` and "defined" this TZ's influence contract, and `T` `None` its ratio rule. **Quoted from committed
artifacts**, each from a figure its instrument printed, the printing function named: §3.1's twelve from TZ-16a
report §1, `tz16a.tables` — `ρ_1` to `ρ_3` and `f̂` also re-derived by the Architect in exact rationals from
that section's exact sums, 4 of 4 at 20 digits; §3.2's `2,608` and member-list hash from TZ-16a report §2,
`tz16a.tables`, the hash re-derived from the 208 non-members that section discloses; §3.6's eighteen from TZ-16a
report §3 and §4, `tz16a.tables`, and §10's V11 table, `tz16a.disclosure_text` — `c = 566` and `FP_E` also
re-derived exactly from §4's distinct-price table, agreeing to `6e-63`, and `POWER_N` to 16 digits; §3.6's nine
further comparisons are equalities with TZ-16a's constants file itself, located by its hash from TZ-16a report
§4 and §10 (map §7 item 82); §3.1's file hash from the TZ-15 report §12; §0.2's `1,072` and three worktrees from
map §3, and `31612203008` and the start sha from map §6; V1's six anchors and the counts `25`, `2`, `1` from map
§0. **From this TZ's own text:** V2's zero-or-one counts, V4's `12` and `27`, V7's counts, V11's `3,600`, V14's
`40`, §0.8's `3,624`, and `3,900` from `S7_DEADLINE_S` plus `300`. **§6's `100`, `540` and `72` s are resource
guards on wall-clock time.** **None depends on a quantity this TZ measures:** `S`, `c`, `d`, the rates, the
powers, the own-look `f` and the interlock counts are compared with no literal; V4 (d) compares two computations
of the same run; and V4 (c)'s literals and file are TZ-16a's committed values, fixed before this TZ was written.

**C3 — shape of every diff.** One new file, `research/tz19-phase2-second-look.py`, absent from `origin/main` at
`84b6020`: the committed lines the change replaces are **none**, and the phrase C3 bars for a non-empty list
does not occur in this file.

**C4 — cost of every check.** §6 recomputed by script on 2026-09-28 from TZ-16a report §9's S1 figures: at most
`4,500` units for the set at `0.01566` s a unit, `70.5` s; `3,600` walks at `0.07793` s, `280.6` s; `3,600`
quote files at `0.00343` s, `12.4` s; the recursions at the unfiltered `n = 3,600` and the first part's `2,400`,
**`76,320,000`** units, `17.8` s at `0.3363` s per `1,440,000`; at most `1,500` `window.json` at `0.00148` s,
`2.2` s; at most `3,600` labels with steps 12 to 14 at `0.00311` s, `11.2` s: **~401 s a run**; a rehearsal `47`
s to its step 6 and ~48 s in all; **~1,844 s** for four runs and five rehearsals, against `3,600`. Both
fail-fast bounds are derived beside their figures: `100 = 5.6 × 18`, `540 = 1.52 × 355` rounded,
`72 = 1.52 × 47` rounded up; at both edges `668` s a run and `73` s a rehearsal, `3,037` s in all. What this TZ
adds to TZ-16a's run at `tau` 240 — V4 (c)'s two recursions at `2,400`, the hashing of `/root/tz16a-work/` and
one JSON parse, and items 13 to 15 at most 20 coins each — sits inside the table. Nothing is sampled and nothing
is simulated.

**C5 — every count**, each beside its source: `3,600` members, `3,600` checkpoints = `3,600 × 1`, `7,200` reads
= `3,600 × 2` (§3.0); `2,608` units and `2,400` members of the first part from TZ-16a report §2's table, and
`1,200` = `3,600 − 2,400`; `405` from the TZ-15 report §4's `selected` column; `25`, `2` and `1` by parsing map
revision `2026-09-27-b`'s §0 under `tz14.fingerprint_rows`' rule, run by the Architect — 28 rows, and every
`frozen` hash equal to its file at `84b6020`, 25 of 25; `6` anchors from map §0 by `tz16a`'s anchor pattern;
`1,072` files and three worktrees from map §3; `2,016` from map §4; four copies of TZ-16a's constants file from
TZ-16a report §4's "byte-identical in all four runs"; §3.1's `12` = `6 + 4 + 2`; §3.6's `27` = `18 + 1 + 8`, its
table's eighteen rows, the member list, and `mu0`, `mu1` and the look's six; the `11` never-called names, the
`10` functions, `9` helpers and `12` never-defined names counted from §5.1's lists; `12` `pfair` entry points
and `9` row keys counted from `tz15.PFAIR_PROBABILITY` and `tz15.ROW_KEYS` in committed code; `82` =
`14 + 5 + 4 + 6 + 6 + 6 + 19 + 8 + 8 + 2 + 4` over `11` items, from `tz16a.SELFTEST_COUNTS`; `32` =
`8 + 9 + 15`, item 13's `8` = `6 + 2`, item 14's `9` = `3 × 3`, item 15's `15` = `5 + 2 + 1 + 7`; `114` =
`82 + 32` over `14` items; `18` columns from `tz16a.OBS_COLUMNS`; `6` barred imports and `5` compared files from
V2's and V3's own lists; `4` files in V8; `3` host reads, at steps 1, 6 and the last; `40` rehearsal members and
`6` rehearsal files; §9's `2` worktrees and at most `3` trees; `4` rows in §4.1, `3` readings in §4.3, `5`
predictions in §3.11, `14` Validation rows, and the header's `6` things. Every row of §7 that says asserted
names its step in §5.1 — V1 0, V2 3 and 5 to 12, V4 4, 5, 8 and 9, V5 12, V6 3, V7 2, V8 0 and the last, V9 the
last, V13 10, V14 run H's — and V3, which compares two runs, is BLOCKING by `cmp` instead.

**C6 — every population.** §3.1's twelve figures: TZ-15's selected members at `tau` 240, in `T0` order. §3.2:
the units considered and the members, whole and per part. §3.3's admissible counts: the members, whole and per
part. §3.4's reads: the members' quote files, reads at `tau` 240. §3.5's eligible count: the admissible members;
the selected counts, the summaries of `a` and `q − a` and both means: the selected members; `D` and the
confidence share: the eligible checkpoints whose Up book is two-sided at the touch; each whole and per part.
§3.6: the first part's 2,400 members at 240, and its 945 selected for rows 10 to 18 and the file's member list.
§3.7's `U0`, `U1`, `c`, `d`, the rates, the powers, the distinct-price table and the power sums: the selected
members of the whole set at 240; the combined rates: the two looks; the per-part sums: each part's selected
members. §3.9's `S`, `T`, `T_fee` and win rate: the selected members; influence: them less one; the split: each
part's selected; the Brier scores and means: the eligible two-sided checkpoints; the own-look
`residual_dependence`: the selected in `T0` order. §3.10's counts and `p_I`: the units considered that have a
manifest; its power: the `m_E` exposed units. §4.1's rates: the selected at 240, on this look and over the two.
§3.11: each prediction's third column. V4 (a): TZ-15's selected at 240; (b): the first part's units; (c): the
first part's members. The rehearsal: its 40 members and its units considered.

**C7 — every signature and every behaviour**, read from `origin/main` at
`84b60206c0182b4fe5dbc457357a95726cec5faa`, where every file below is byte-identical to its map §0 `frozen` row.
All 57 `module.name` references resolve, through `ast`, to a top-level name of the file map §3 assigns the
module, and so do the twenty-two bare `tz16a` names §5.1 lists. Each called function as the file holds it, with
the lines the sentences rely on:

- `tz16a.dependence(path)` — `selected, data_rows = _tz15_selected(path)`, which runs
  `assert header == OBS_COLUMNS`, keeps rows `if tau in per_tau and cells[ix["selected"]] == "1"` and
  `return {tau: sorted(rows) for tau, rows in per_tau.items()}, len(lines) - 1`; then per `tau` in `ADMITTED`
  `assert dep["defined"]`, entries carrying `n`, `sum_a`, `sum_q`, `sum_y` and `dependence`, and
  `return out, data_rows`.
- `tz16a.residual_dependence(x)` — `return {"defined": False, "why": "n < 4", "n": n}` where `n < 4`, the same
  with `"v = 0"` where `v == 0`, `f = max(D(1), f_hat)`, `"r": f.sqrt()`, and `sum_x`, `sum_x2`, `rho` and
  `f_hat` among its keys.
- `tz16a.look_constants(a, q, r, alpha, beta, tails=None)` — `c, fp_e = critical_upper(U0, mu0, r, alpha)`,
  `d, fp_n = critical_lower(U1, mu1, r, beta)`, `power_e = up(U1, mu1, r, c) if c <= n else D(0)` and
  `power_n = low(U0, mu0, r, d) if d >= 0 else D(0)`; `critical_upper(U, mu, r, alpha)` ends
  `return n + 1, D(0)` and `critical_lower(U, mu, r, beta)` `return -1, D(0)`; `up(U, mu, r, s)` and
  `low(U, mu, r, s)` as TZ-16a §3.7 defines them.
- `tz16a.read_look(n, S, c, d)` — `return "UNDECIDABLE", False` at `n == 0`, `return "EDGE", S <= d` at
  `S >= c`, then `"NO EDGE"` at `S <= d`, then `"UNDECIDABLE"`; `tz16a._row_of(n, reading)` returns `"S >= c"`,
  `"S <= d"`, or `"n = 0" if n == 0 else "otherwise"`.
- `tz16a.interlock(considered, manifests)` — `unit["failure"] = doc.get("quotes_complete") is not True`;
  exposure `if t0 >= EXPOSED_FROM and t0 % WINDOW_S == EXPOSED_OFFSET` and the window file present;
  `unit["fully_loaded"] = isinstance(missed, int) and not isinstance(missed, bool) and missed == 0`;
  `p_i = fisher_upper(f_e, m_e, f_c, m_c)`, `reading = interlock_reading(f_e, p_i)` and
  `interlock_power(m_e, m_c, q)` per `q`; the start record matched on `event`, `SERVICE_PID` `2699889` and
  `SERVICE_START_NS` `1790185190022755903`, and the stops after it. `interlock_reading` returns
  `"FIRE" if f_E >= 1 and p_I <= FIRE_AT else "HOLD"`, `FIRE_AT = Fraction(1, 100)`.
- `tz16a.selftests()` — `SELFTEST_COUNTS = (14, 5, 4, 6, 6, 6, 19, 8, 8, 2, 4)`, asserted; its items call the
  functions §5.2 lists and never `dependence`; item 12 times `tz15.pb_upper([T12_WEIGHT] * T12_WEIGHTS)` with
  `T12_WEIGHT = D("0.37")` and `T12_WEIGHTS = 1200`, `if projected > RECURSION_LIMIT_S: raise SystemExit(…)`
  with `RECURSION_UNITS = 275069310` and `RECURSION_LIMIT_S = 400.0`, and returns `"t12_s": t12` among its keys.
- `tz16a._sig(value, digits=20)` returns `str(decimal.Context(prec=digits).plus(value))`. `tz16a.tables` prints
  §3.1's `n` and `sum_y` with `%d`, `sum_a` and `sum_q` with `%s`, `sum_x` and `sum_x2` with `_exact`, and the
  `ρ_k`, `f̂`, `f` and `r` with `_sig`, the exact constants with `%s`, `mu0` with `_exact`, the first power sum
  with `%s` and each `tau`'s distinct-price count; `tz16a.disclosure_text` prints `tz07b.member_list_sha` of
  each eligible and selected list. `tz16a.constants_text` writes `"per_tau": {tau: …}` through `_jsonable`,
  which makes every key a string, and `constants` sets each `tau`'s `members` to
  `{"T0", "side", "a", "q", "fee"}` records of the selected trades in ascending `T0`, `mu0`, `mu1` and `look`;
  `build` writes it at `_step(run, "9")` and reads labels at `_step(run, "12")`. `tz16a.OBS_COLUMNS` holds 18
  names; `tz16a`'s body runs `tz15 = _load("tz15phase2gate", "tz15-phase2-gate.py")` and
  `sys.addaudithook(_audit)`.
- `tz15.pb_upper(weights)` returns `U(s)` for `s = 0 … n`; `tz15.crit(weights, alpha)` ends
  `return s_star, (upper[s_star] if s_star <= n else D(0)), upper`; `tz15.select(p, ask_up, ask_dn)` returns
  `e_up`, `e_dn`, `selected`, `side`, `a`, `q`, `edge` and `both_positive`, with
  `if not existing or max(existing) <= 0: return out` and
  `if e_up is not None and (e_dn is None or e_up >= e_dn)` for `Up` at `q = p`, else `Down` at `q = D(1) - p`;
  `tz15.label_free(rows)` runs `assert set(row) == set(ROW_KEYS)` and `assert row["label"] is None`; `tz15`'s
  body writes the three environment variables, loads `tz14` and calls `sys.addaudithook(_audit)`, appending to
  `OPENS`.
- `tz06.scoring_set(manifests, need=SET_SIZE, *, after=None)` — opens at
  `min(int(name) … if int(name) > after)`, walks `while members < need and t0 <= last` with
  `t0 += config.INTERVAL_S`, and `return rows, members == need`, each row `{"T0", "reasons", "member"}`;
  `tz06.qualification(t0, manifests)` reads `venue(t0)` and appends `"no resolved outcome"` and
  `"no priceToBeat"` on `None` alone, beside the stream conditions. `tz14.the_set` calls
  `tz06.scoring_set(manifests, SET_NEED, after=SET_AFTER)` with `1200` and `1789206600`, so the rehearsal's 40
  are TZ-14's first 40.
- `tz11a.walk_member(t0, manifests, guard)` — `for tau in pfair.TAUS:` with its four assertions, and `out[tau]`
  carrying `sigma_hat`, `priced`, `Y` and `r`; `tz11a.checkpoint_row(t0, name, tau, row)` returns `"set": name`,
  `"admissible": row["sigma_hat"] >= pfair.ADMIT[tau]`, `"p_t": pfair.p_fair_student(…)`, `"Y"`, `"r"` and
  `"label": None`; `tz11a.host_read(when, t0s, floor)` runs `assert free >= floor` and
  `assert doc["recorder_pids"]` and returns `newest_start_sha`, `newest_start_recv_ns`, `interval_directories`
  and `read_set_sha256`.
- `tz10b.m2_labels(members)` — `info = venue(t0)`,
  `assert info is not None and info["resolved_up"] is not None`, `out[t0] = 1 if info["resolved_up"] else 0`.
  `tz07b.member_list_sha(members)` — the SHA-256 of the sorted list joined by newlines, no trailing newline.
- `tz14.fingerprint_rows()`, `tz14.documents(t0)`, `tz14.quote_lines(dirpath)`, `tz14.book_of(raw)`,
  `tz14.touch_of(book, min_size, tick)`, `tz14.fee_pp(p)`, `tz14.q_summary(values)`, `tz14.weekday_of(t0)` and
  `tz14.is_weekend(t0)` — as TZ-16a §10 C7 quotes them, the file byte-identical since: `fingerprint_rows` keeps
  a line of five cells whose first starts with a backtick and whose fourth is `frozen`, `tracked` or `reported`;
  `quote_lines` returns every line's read with `tau`, `token_id` as a string, `status`, `raw` and
  `body_is_json`; `book_of` sets `ok` and a `_present` key per `BODY_FIELDS`, which holds `tick_size` and
  `min_order_size`; `touch_of` returns `bid5` and `ask5`; `fee_pp` is `FEE_RATE * p * (D(1) - p)`;
  `BANNED_SUBSTRINGS[0]` is `"reso" + "lution"`.
- The constants `tz11a.FLOOR_START_BYTES` `2060000000`, `tz11a.FLOOR_BYTES` `2000000000` and
  `tz12.SESSION_CEILING_S` `3600`; `pfair`'s `decimal.getcontext().prec = 60`; `config.interval_dir(t0)`; and
  `S7_DEADLINE_S = 3600` in `research/recorder/recorder.py`, whose `close_interval` runs
  `await self.fetch_s7(t0, path)` before `doc = manifest.write(path)`.

**C8 — every cross-reference**, resolved by reading the referenced text: CANON PART II's gate rules (§4.1, §4.3)
and hard rule 5 (§0.8); map revision `2026-09-27-b` §0 (the header, §0.1, §2, §7), §1 (§0.6), §2.3 (the header,
§0.8, §3.11, §4.3, §5.3, §6, §7, §8), §2.5 (the header, §0.2, §1, §2, §3.10), §3 (§0.2, §0.4, §1, §6), §4
(§3.11, §7), §5 (§1, §4.3), §6 (§0.2, §0.3, §0.4, §4.2, §9) and §8 (§0.2); map §7 items 27, 29, 52, 54, 62, 63,
64, 70, 78, 82, 83 and 84; contract §4.1 (§2), §4.2 and §8 (§8) and §9 (§0.8); TZ-16a §0.8, §1, §3.2, §3.4 to
§3.7, §3.10, §4.1, §4.2, §4.3, §5.1, §5.2, §9 and §10; the TZ-16a report §1, §2, §3, §4, §6, §9, §10 and §12;
the TZ-15 report §0.2, §4 and §12; TZ-15 §3.3 and §3.4; and TZ-18a §6.1. **Checked mechanically as well:** every
`§` of this file that names its own section resolves to one of its headers, and every map item named exists in
map §7 of revision `2026-09-27-b`. Each supports the sentence that makes it.

**Checks this session could not perform:** none of C1 to C8 — the repository was reachable. **What only the host
holds is converted into BLOCK conditions the Executor evaluates** (CANON hard rule 13): the store's copy of
TZ-15's file by hash and §3.1's twelve figures (V4 (a)); TZ-16a's constants file by hash, the first part's
identity and the first look's twenty-seven comparisons (V4 (b) and (c)); the trees and the forensic count
(§0.2); and R-READY (§0.8), whose failure stops as NOT YET. This session re-derived instead, from committed text
alone, the expected values those conditions compare against: the member-list hash, `ρ_1` to `ρ_3` and `f̂`, and
`c`, `FP_E` and `POWER_N` of the first look at 240.
