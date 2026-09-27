# TZ-16a — Phase 2's decisive gate, first look

**Canonical filename:** `TZ-16a-phase2-decisive-gate.md`. The committed file takes this name and no other.

**Executor model: Opus.** Two exact tails under two hypotheses, a dependence measurement that sets
them, the first label read of the reserved span, and a stop block for a running process.

**Required System Map revision:** `2026-09-27-a`.

**Required anchors**, from map §0. A mismatch on any one is BLOCKED before any work:

| anchor | required |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-undecidable-5tau` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` |
| `A6` — pricer | `729f0bcdbee3` |

**Host gate:** §0.2. This TZ touches the capture host and runs nowhere else.

**When:** as soon as §0.8's readiness condition holds — mechanical, BLOCKING before the build, with
nothing in an interval directory opened but manifests. §3.3's clock condition then asserts the same guard
on the members themselves. No date is set beyond these two.

**This TZ replaces TZ-16**, `CryptoTZ/TZ-16-phase2-decisive-gate.md` at SHA-256
`0e0752cdfacaa517102077052372a32de9557eb6baa37f5354a499b83c7196dd`, whose execution stopped BLOCKED at
its own §3.2 and V4 (a) before anything was built: `CryptoReports/TZ-16-phase2-decisive-gate-report.md`,
committed at `a9e0b45`. Two of the twenty values V4 (a) quoted were wrong — the TZ-15 report's `Σ q`
column, which TZ-15's instrument never printed, misstates the sum of TZ-15's own file at `tau` 180 and
60 (map §7 item 82). TZ-16 and its report stay on `main` unchanged. **That execution read nothing of
the reserved span** — no set, no quote, no market document, no label (its report §5) — so **no score of
the span exists, and this TZ carries TZ-16's sampling rule, thresholds, error allocation, selection,
predictions and self-test expectations unchanged.** It differs from TZ-16 in these places and no others:

1. **§3.1, §3.2, V4 (a) and §8:** `Σq` is asserted **equal** to the `sum_q` TZ-15's instrument wrote
   into `tz15-constants.json` — now parsed for `n`, `sum_a` and `sum_q` and nothing else — and to that
   file's values at full precision; no figure is quoted that TZ-15's instrument did not print.
2. **§3.2, §3.9, §4.2, §5.1, §5.2 item 7, V7 and V12:** the dependence arithmetic is one total function,
   `residual_dependence`; the own-look diagnostic after the label read raises nothing, and its two
   undefined cases are self-tested — four assertions more, 82 in all.
3. **§3.9:** influence names `μ0` and `μ1` among what it recomputes, every figure there is total, and
   nothing from step 12 onward raises on the labels.
4. **§5.1 and §5.2 item 9:** the interlock's reading is a pure function, `interlock_reading`, which
   the self-test calls with literals.
5. **V8 and V9:** their last step is 14 with `--score` and 11 without.
6. **§0.2, §0.5, §0.6, §0.7, §2 and §9:** the host as TZ-16 left it — `/root/tz16-work/` present, six
   worktrees — the commits above map §1's head reported and not counted, TZ-15's constants file among
   §2's named reads, and `/root/tz16-work/` reclaimed beside the two trees TZ-16 was to reclaim.
7. **§1 and §4.4:** references to this TZ's own sections no longer read as map sections, and the
   reading this report makes is named as the one CANON PART II calls TZ-16's.
8. **§3.11:** one paragraph on the predictions' provenance; the predictions are TZ-16's.
9. **§5.2's opening paragraph:** it no longer calls every expectation computed or every comparison
   numeric — §10 C2 names each expectation's origin; a reading or a reason compares as a word, a flag
   as a boolean.
10. **Names and revision:** `tz16a` for the instrument, its outputs, its tree and its set label,
    `tz-16a-phase2-decisive-gate` for the branch, and map revision `2026-09-27-a` in the header and
    §0.1; and §10, performed afresh.

---

## 0. Gates, host, interpreter, floor, refs, trees, readiness

### 0.1 Fingerprint — asserted inside the instrument as step 0 of §5.1

Read `SYSTEM-MAP.md` in the checkout the instrument runs from, a branch cut from `origin/main` after
this TZ landed. Its revision string must read `2026-09-27-a` and its six anchors must equal the table
above; `A2`, `A4`, `A5` and `A6` are also re-derived as the first 12 hex characters of those files'
SHA-256. Every row of its §0 fingerprint table is hashed in lines, bytes and SHA-256 through
`tz14.fingerprint_rows()`: the **24** `frozen` rows must equal the hashes printed there, the **2**
`tracked` rows are reported with no expectation, and the **1** `reported` row, `SYSTEM-MAP.md` itself,
is reported. Any `frozen` mismatch is BLOCKED. The expected revision, the six anchors and the counts
`24`, `2` and `1` are literals of this instrument, so the gate never reads its own expected values from
the file it checks. **Neither `tz14.v1_gates` nor `tz15.v1_gates` is called:** they assert revisions
`2026-09-18-b` and `2026-09-19-a`.

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
for d in /root/tz15-work /root/tz16-work /root/tz16a-work /root/tz18a-work /root/tz18a-svc; do test -e "$d"; echo "$d exit=$?"; done
find /root/btc-forensics -type f | wc -l
git worktree list
```

- **H1** — `find` prints exactly one path.
- **H2** — the first `pgrep -fx` prints exactly one line and `exit=0`. `-fx` matches the whole command
  line, so the shell evaluating this block, which carries the pattern as a substring, cannot match it.
  Map §8 records the recorder as pid `228592`; another pid is disclosed, not BLOCKING.
- **H3** — `df` names source `/dev/vda2` and size `31612203008`, and the `grep -c` line, which reads the
  recorder's own top-level log and no interval directory, prints at least `1`. With H1 these are map
  §6's host-identity row; the newest start record's sha is asserted by the instrument at step 1.
- **H4 — recorded, not BLOCKING:** the second `pgrep -fx`, the chain book service, which map §2.5
  records as pid `2699889`. §3.10 reads the service's own record and does not depend on this line.
- **Resource gate** — `avail` at least `2,060,000,000` bytes (§0.4).
- **Trees** — `/root/tz15-work`, `/root/tz16-work`, `/root/tz18a-work` and `/root/tz18a-svc` exit `0`;
  `/root/tz16a-work` exits `1`. Anything else is BLOCKED.
- **Forensic store** — exactly `1,046` files, map §3's count at TZ-16's end. Anything else is BLOCKED.
- `du`, both `systemctl` reads and `git worktree list` are printed and carry no threshold; map §3
  counts six worktrees at TZ-16's end.

### 0.3 Interpreter

Every command of the instrument runs on `/root/tz01-env/venv/bin/python` — Python 3.12.x (map §6).
Report its version and `numpy`'s. `import numpy` must succeed, because the committed chain the
instrument loads imports it; the instrument itself computes nothing in `numpy`.

### 0.4 Resource floor, in exact bytes, derived from map §6

Free space on `/dev/vda2` at run start at least `tz11a.FLOOR_START_BYTES` = `2,060,000,000`; every
later read at least `tz11a.FLOOR_BYTES` = `2,000,000,000`, map §6's floor. The `60,000,000` bytes
between them bound what this TZ writes: TZ-15's tree of the same shape measured `7,250,569` bytes
(map §6), and this one holds twice the rows. Both asserted; every read reported with its UTC instant,
its reader and its bound.

### 0.5 Preflight, twice, at least 1,800 s apart

The first before the build, the second before the first run with `--score`: `df -B1` on `/dev/vda2`,
`du -sb /root/PROJECT_GAMING_PS5`, and the exit codes of `systemctl is-enabled telemetry-watch.service`
and `systemctl is-active telemetry-watch.service`. Both reported with the elapsed seconds and the
implied bytes per day of each quantity; this session's own footprint — `/root/tz16a-work` and
`/root/.claude` — stated separately at both (map §7 item 29), and `/root/tz16-work`, TZ-16's, beside
them. Gates nothing beyond §0.4.

### 0.6 Refs

`git ls-remote origin` before the branch of §2 exists, every ref reported. Map §1 records `main` at
`a9e0b45f25769071940ddaefb4fdf1b374f12e78`, the TZ-16 report. The upload that carries revision
`2026-09-27-a` and this TZ sits above it, in one commit or more; every commit on `main`'s first-parent
line above `a9e0b45` is reported with the paths it changed, and their number is recorded, not asserted.
A difference is recorded, not BLOCKING, unless `main` no longer carries revision `2026-09-27-a` or
`refs/heads/tz-16a-phase2-decisive-gate` already exists — either is BLOCKED.

### 0.7 The recorder's working tree

The recorder runs from `/root/btc-5m-twap/research/recorder` (TZ-15 report §0.2), so that checkout's
working tree is never switched: the branch is built in `/root/tz16a-work/wt` and the report committed
from `/root/tz16a-work/wt-report`, both added with `git worktree add` from `origin`.
`/root/tz16-work/wt-report`, TZ-16's report checkout, is left as it is until §9.

### 0.8 Readiness — the one condition that depends on the calendar

Before the build, from `/root/btc-5m-twap`, reading manifests and nothing else under the capture root
(map §2.3's exception):

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
print('complete', len(t0s), 'at-2400', t0s[2399] if len(t0s) >= 2400 else None, 'now', now)
EOF
```

**R-READY:** at least `2,400` complete manifests with `T0 > 1789669800`, and `now >= t0s[2399] + 3,900`.
Otherwise **BLOCKED**, the printed line in the report, before the build. `complete` is the first
condition of the committed set rule, so no run formed earlier can succeed; §3.3 asserts the
sufficient form on the members themselves. `3,900` s is the recorder's outcome deadline,
`S7_DEADLINE_S` = `3600` s after `T0` in `research/recorder/recorder.py`, plus `300` s for the close
that writes the manifest after it (§1).

---

## 1. Why this TZ exists

TZ-15 applied Phase 2's first gate once, to 1,200 slots, and decided nothing: EDGE was reachable and
not read, and NO EDGE had no test at all — power stood in for one (map §7 item 69). This TZ is the
decisive gate map §5 fixes and CANON PART II requires — TZ-16's, corrected (header) — on the span map
§2.3 reserves, whose quotes and outcomes no one has opened: **each answer from its own exact test**, at
a false-reading probability fixed here, before any label of the span is read.

- **EDGE** — the null is a market calibrated at its own ask: each trade the Student pricer selects
  wins with the probability of the price paid. EDGE where the wins reach beyond that law's upper tail.
- **NO EDGE** — the null is the pricer's own law: each selected trade wins with the probability `p_t`
  gives the side bought. NO EDGE where the wins fall below that law's lower tail.
- **UNDECIDABLE** between them.

**Two looks, fixed now.** This TZ is the first: the first 2,400 qualifying slots after `1789669800`.
Each `tau` it leaves UNDECIDABLE is read once more, on the first 3,600, by a later TZ that applies
§4.2's rule unchanged. Each answer's one per cent per `tau` is split `0.002` at this look and `0.008`
at the second — little spent early, the O'Brien–Fleming allocation at two thirds of the information,
rounded — and the looks are combined by the union bound, which holds whatever the dependence between
them. Over the five `tau` each answer's false-reading probability is at most `0.05`.

**Dependence, measured before any label of the span is read** (map §7 item 71). Both tails assume that
the outcomes of different intervals are independent given the prices. The assumption is measured on
the null's own residual `y − a` over TZ-15's labelled set, below the reserve, and the critical values
are derived under what it shows. Negative dependence thins the tails and is never used to narrow them.

**Selection, fee, domain and pricer are TZ-15's, unchanged:** `tz15.select`, `tz14.fee_pp`,
`pfair.ADMIT` through `tz11a.checkpoint_row`, `A6` `729f0bcdbee3`. No constant of this TZ was chosen by
looking at a quote beside a price.

**The set is formed from the capture alone.** The recorder writes an interval's manifest only after its
outcome poll ends, up to `3600` s after `T0`; a walk formed inside that window could count a slow
interval as a non-member and a later walk admit it. §0.8 and §3.3 bar that.

**Two duties carried here by the map:** the chain book's interlock on Tier C, continued over this set
with a test finer than G-TIERC's two units (map §2.5; this TZ's §3.10), and the reclaiming of
`/root/tz15-work/`, `/root/tz16-work/` and `/root/tz18a-work/` (map §3; this TZ's §9).

---

## 2. Scope

**Repository paths this TZ may write, and no others:**

1. `research/tz16a-phase2-decisive-gate.py` — new file, on branch `tz-16a-phase2-decisive-gate`, then a
   pull request. Not merged by the Executor.
2. `CryptoReports/TZ-16a-phase2-decisive-gate-report.md` — straight to `main`, in one commit, as contract
   §4.1 requires. **The one path pushed to `main`, and the exemption to item 5 below.**

**Host paths this TZ may write:** `/root/tz16a-work/**` — its worktrees, run directories and label
ledger — and `/root/btc-forensics/`, by exclusive create only (§9). **Host paths it removes, under §9
and nothing else:** `/root/tz15-work/`, `/root/tz16-work/` and `/root/tz18a-work/`, their five
worktrees first.

**Prohibited, each absolutely:**

1. No committed file is modified. Every `frozen` row of map §0 is byte-identical at run end.
2. Nothing under `/var/lib/btc-recorder/` is created, written, moved or removed; every file there is
   opened read-only. The recorder is never signalled, stopped or restarted.
3. Nothing under `/var/lib/btc-chainbook/` is created, written, moved or removed, and **only files
   named `window.json` and the file `runtime.jsonl` are opened there**, read-only — map §2.5's
   exception, counts, times and token ids. No `books.jsonl.gz`, no `documents.jsonl`, no reply body.
   The chain book service is never signalled. **Exemption:** block K-18a, under §4.3's FIRE and no
   other condition.
4. `/root/tz04a-env/`, `/root/tz01-env/`, `/root/btc-forensics/` and `/root/tz18a-svc/` are never
   removed or emptied. **Exemption:** §9 copies files into `/root/btc-forensics/` by exclusive create.
5. Nothing is pushed to `main` except the report of item 2 above.
6. **No label of the span is read before §3.7's constants are on disk and the scoring commit is on
   `origin`.** A label is the venue's resolved outcome. **Three exemptions, each named because this
   TZ's body requires it:** (a) `tz06.qualification`, which `tz06.scoring_set` calls for every unit
   considered and which reads `resolved_up` and `priceToBeat` through `analyze.venue` to decide
   membership on their existence alone; (b) `tz10b.m2_labels`, the one label reader this TZ calls,
   once per scored run at §3.8; (c) §3.1 and §3.2's reads of TZ-15's two files — the observations file,
   whose `label` and `y` columns are outcomes of TZ-15's set, below the reserve, read and scored by
   TZ-15, and enter `f` and V4 (a)'s `Σy` alone; and the constants file, which holds no label and gives
   §3.2 three values per `tau`.
7. **The instrument computes no probability itself.** `p_t` is the `p_t` field of
   `tz11a.checkpoint_row`, and nothing in the instrument's own syntax tree calls any of the twelve
   `pfair` entry points `tz15.PFAIR_PROBABILITY` names. **Exemption:** `tz11a.checkpoint_row` computes
   `p_t` and three further link quantities internally; the instrument keeps `p_t` alone.
8. **No settlement-derived quantity enters any pricer row:** the rows carry exactly the nine keys of
   `tz15.ROW_KEYS`, asserted by `tz15.label_free`.
9. **The reserve beyond this look is not touched.** No file but `manifest.json` is opened in any
   interval directory whose `T0` exceeds the last unit §3.3 considers — the 2,400th member.
10. **No request to any venue**, by the instrument or by the session: no HTTP, no websocket, no socket.
    `git` against `origin` is the only network use.
11. No fit is performed, and no constant is produced for any file but this run's own output: `f` of
    §3.2 and the constants of §3.7.
12. No Release is created, and no dataset, archive or binary enters git history.

---

## 3. The measurements

### 3.0 Partitions and counts

- **`ADMITTED` = `tz15.ADMITTED` = `(240, 180, 120, 90, 60)`**, the five `tau` open for Phase 2 (map
  §5). No figure is computed at `tau` 30 or 10; the committed functions compute them internally and
  they are discarded.
- **This look:** the first **2,400** qualifying slots with `T0 > 1789669800`; checkpoints **12,000** =
  `2,400 × 5`; admitted reads **24,000** at full completeness = `12,000 × 2`.
- **TZ-15's labelled set, for §3.2 alone:** its selected members per `tau`, **405 / 428 / 440 / 380 /
  271** at `tau` 240 … 60 (TZ-15 report §4).
- One checkpoint per member per `tau`. The five `tau` of one member share one outcome, so the five
  tests are dependent; every family bound of §4 holds whatever that dependence is.

### 3.1 TZ-15's outputs, located by hash

Under `/root/tz15-work/`, every regular file whose SHA-256 equals
`a7ac8a495e00e21cd34af6ead7f05e9a2b741231c928bb61d4ec03ec0e610ce6` — `tz15-observations.csv` — and
every one equal to `e6a93f9371e9fb32404482dac7b542c330399117ba0cf93e466b846e5878dfd3` —
`tz15-constants.json` — both from the TZ-15 report §12. The first of each in sorted path order is read,
and the number of copies reported; the TZ-16 session found 2 and 5 (its report §2). **Either absent:
BLOCKED.** **The constants file is parsed as JSON for three values per `tau` in `ADMITTED` and nothing
else:** `per_tau[str(tau)]["n"]`, an integer, and `per_tau[str(tau)]["sum_a"]` and
`per_tau[str(tau)]["sum_q"]`, each a string read as `D(...)` — what `tz15.build` wrote from its own
selection before any label existed (§10 C7). V4 (b) re-derives the rest from the observations file.

### 3.2 The dependence, measured on TZ-15's labelled set

From the observations file — TZ-15's eighteen columns, each cell as `tz14.cell` wrote it — per `tau`
in `ADMITTED`, the rows whose `selected` cell is `1`, in ascending `T0`; `a` read as `D(cell)`, `q` as
`D(cell)` and `y` as `int(cell)`; `Σa` and `Σq` summed in `Decimal`, exact at these magnitudes.
**Asserted per `tau`, each an equality; any difference is BLOCKED, because the file is then not the one
TZ-15 scored:**

- `n` is `405 / 428 / 440 / 380 / 271` — the `selected` column `tz15.tables` printed, TZ-15 report §4 —
  and equals the constants file's `n`;
- `Σy` is `210 / 211 / 190 / 164 / 99` — the `S` column `tz15.tables` printed, TZ-15 report §7;
- `Σa` equals `D("216.2300")`, `D("212.5000")`, `D("192.1940")`, `D("156.7230")`, `D("102.5810")` as a
  value — the `sum a` column `tz15.tables` printed, TZ-15 report §7, exact because no price carries more
  than three decimals — and equals the constants file's `sum_a` as a value;
- `Σq` equals the constants file's `sum_q` as a value, and equals, as a value,
  `D("233.579362178548589456")`, `D("230.1410794878433773409")`, `D("208.2308022961688662051")`,
  `D("171.86830345826790914045")` and `D("114.107227667538293020748")` — that file's `sum_q` at full
  precision, as the TZ-16 report §3 printed it from the file at `e6a93f93…`.

**The TZ-15 report's `Σ q` column is quoted nowhere:** `tz15.tables` prints no `sum q`, and the column
misstates the file at `tau` 180 and 60 (map §7 item 82).

Then, per `tau`, **`residual_dependence(x)`** over `x_i = y_i − a_i` in that order, all in `Decimal` at
the 60 digits `pfair.py` sets on import: `x̄ = Σx / n`; `v = Σ(x_i − x̄)²`; for `k = 1, 2, 3`

`ρ_k = Σ_{i=1}^{n−k} (x_i − x̄)(x_{i+k} − x̄) / v`;

`f̂ = 1 + 2(ρ_1 + ρ_2 + ρ_3)`, **`f = max(1, f̂)`** and **`r = f.sqrt()`**. **`residual_dependence` is
total:** where `n < 4` it returns the result undefined with the reason `"n < 4"`, and otherwise where
`v = 0` undefined with the reason `"v = 0"`; it raises on neither. **`dependence` applies it to TZ-15's
set at every `tau` and asserts the result defined** — BLOCKING at step 4, before any file of the span
is opened.

`f` is the variance of a sum of residuals over the sum of their variances, estimated to the third
neighbour in selection order. **The direction is derived, not asserted** (map §7 item 71): a positive
dependence widens the law of the count, so independent critical values would sit too close to its
centre — `c` too low, toward a false EDGE, and `d` too high, toward a false NO EDGE — and §3.7's `r`
moves both back out. A negative dependence narrows the law, the independent values are then
conservative, and `f = 1` keeps them.

**Printed per `tau`, for the Architect's exact re-derivation** (map §7 item 70): `n`, `Σx`, `Σx²`, and
for each `k` the three sums `P_k = Σ_{i=1}^{n−k} x_i x_{i+k}`, `A_k = Σ_{i=1}^{n−k} x_i` and
`B_k = Σ_{i=k+1}^{n} x_i`, exact; the three `ρ_k`, `f̂`, `f` and `r` to 20 significant digits.

### 3.3 The set

`rows, whole = tz06.scoring_set(manifests, 2400, after=1789669800)`, `manifests = load_manifests()`,
unchanged; `members` the `T0` of every row whose `member` is set. **Asserted:** `whole` is true;
`len(members)` is `2400`; the first unit considered has `T0 = 1789670100`; consecutive units differ by
exactly `300`; **and the host clock at this step is at least `members[-1] + 3900`** (§0.8's reason). A
failure of `whole` or of the clock condition is BLOCKED, with the counts, the first and last unit and
the clock printed, before any quote file or market document is opened. Printed: the units considered,
the members, `tz07b.member_list_sha(members)`, the first and last member in UTC, the members per
weekday by `tz14.weekday_of`, and every non-member with its reasons.

### 3.4 The pricer at each checkpoint

For each member, `walked = tz11a.walk_member(t0, manifests, False)`; for each `tau` in `ADMITTED`,
`full = tz11a.checkpoint_row(t0, "tz16aset", tau, walked[tau])`, and the row kept is
`{k: full[k] for k in tz15.ROW_KEYS}` — **the pricer row**, `label` `None` by `checkpoint_row`'s own
body until §3.8. Everything §3.5 to §3.7 derive is kept in records keyed by `(T0, tau)`, never in the
pricer row. **An `AssertionError` from `walk_member` is BLOCKING**, the member and the message printed.
Printed per `tau`: the admissible count, weekday and weekend by `tz14.is_weekend`.

### 3.5 The quotes at each admitted checkpoint

TZ-15 §3.3's rule, unchanged. Per member `docs = tz14.documents(t0)` and
`lines = tz14.quote_lines(config.interval_dir(t0))`; for each read at a `tau` in `ADMITTED` whose
`status` is `200` and whose `body_is_json` is true: `book = tz14.book_of(read["raw"])`, then
`touch = tz14.touch_of(book, D(str(book["min_order_size"])), D(str(book["tick_size"])))` — the venue's
own minimum size and tick from the same reply. The read's side is `docs["tokens"][read["token_id"]]`.
**A read that is not `200` or not JSON, whose `book_of` result has `ok` false, whose book lacks
`min_order_size` or `tick_size` (`book_of`'s `_present` keys), or whose token is outside the member's
mapping, and a member whose `gamma.json` is not usable, is listed with its reason, counted and
contributes no touch — not BLOCKING.** Per member per `tau`: `ask_up`, `bid_up`, `ask_dn`, `bid_dn`,
each `touch["ask5"]` or `touch["bid5"]` of that side's reply, or `None`. Printed per `tau`: the reads
present, the reads used, and the listed reads by reason.

### 3.6 Eligibility, selection, and what the pricer claims — label-free

TZ-15 §3.4's rule, unchanged. **Eligible at `tau`:** an admissible member at whose checkpoint `ask_up`
or `ask_dn` exists. `p = D(repr(row["p_t"]))`; `tz15.select(p, ask_up, ask_dn)` takes the side with
the larger after-fee edge where it is strictly positive — the fee through `tz14.fee_pp`, a tie to
`Up` — and gives the price paid `a` and `q`, the probability `p_t` gives the side bought: `p` for `Up`,
`1 − p` for `Down`.

**Reported per `tau`, before any label exists:** the admissible, eligible and selected counts; the
selected by side and by weekday against weekend; the count of checkpoints where both edges are
positive; the count of selected trades priced at or below `0.10`; `tz14.q_summary` of `a` and of
`q − a`; the mean claimed edge `Σ(q − a) / n` and after the fee `Σ(q − a − fee(a)) / n`; and, over
eligible checkpoints whose Up book is two-sided at the touch, `tz14.q_summary` of
`D = p − (bid_up + ask_up) / 2` and the share at which `|p − 0.5| < |mid − 0.5|`.

### 3.7 The gate's constants — exact, from prices, `p_t` and `f`, on disk before any label

Per `tau`, over the `n` selected members in ascending `T0`: the weights `a` and `q`;
`U0 = tz15.pb_upper([a ...])` and `U1 = tz15.pb_upper([q ...])`; `μ0 = Σa` and `μ1 = Σq`; and `r` from
§3.2 at that `tau`.

**The tails under the dependence measured** — two functions and no others, both `Decimal`:

- `up(U, μ, r, s)`, the probability that the count reaches `s`: with `k = ⌊μ + (s − μ) / r⌋`, it is `1`
  where `k <= 0`, `0` where `k > n`, and `U[k]` otherwise.
- `low(U, μ, r, s)`, the probability that the count stays at or below `s`: with
  `k = ⌈μ + (s − μ) / r⌉`, it is `0` where `k < 0`, `1` where `k >= n`, and `1 − U[k + 1]` otherwise.

Each reads the independent law at the deviation shrunk by `r` — a variance larger by `f` — and rounds
toward the heavier tail. **At `r = 1` both are the exact Poisson-binomial tails:** `μ + (s − μ) / 1` is
`s` exactly, because every `a` and every `q = D(repr(p_t))` has far fewer than 60 significant digits.

**At each `tau`, with `α1 = β1 = D("0.002")`:**

- **`c`** — the smallest `s` in `0 … n` with `up(U0, μ0, r, s) <= α1`, and `n + 1` where none exists.
  **`FP_E = up(U0, μ0, r, c)`**, `0` where `c = n + 1`: the probability that a market calibrated at its
  ask reads EDGE.
- **`d`** — the largest `s` in `0 … n` with `low(U1, μ1, r, s) <= β1`, and `−1` where none exists.
  **`FP_N = low(U1, μ1, r, d)`**, `0` where `d = −1`: the probability that NO EDGE is read if the
  pricer is right.
- **`POWER_E = up(U1, μ1, r, c)`**, the probability of EDGE if the pricer is right, and
  **`POWER_N = low(U0, μ0, r, d)`**, the probability of NO EDGE if the market is calibrated at its ask;
  each `0` at its unreachable end. They size the look and decide nothing.
- **Independence beside it**, barred from every reading: the same six at `r = D(1)`. There `c` is
  asserted equal to the first value `tz15.crit([a ...], α1)` returns, and `FP_E` to the second.
- **The second look's projection**, barred from every reading: the same six at
  `α2 = β2 = D("0.008")` and the same `r`, over the selected weights followed by those at even
  positions — `w + w[::2]`, `n + ⌈n/2⌉` coins, one and a half times this look. Its `POWER_E` and
  `POWER_N` bound the two looks' deciding probability from below.

Also per `tau`, for the Architect's re-derivation (map §7 item 70): `n`, `μ0`, the null's weights as a
table of distinct prices with their counts — which fixes `U0` exactly — and `Σq`, `Σq²`, `Σq³`, `Σq⁴`,
which fix the alternative's first four cumulants.

All of it, with every selected member's `T0`, side, `a`, `q` and `fee(a)` and §3.2's figures, is written
to **`tz16a-constants.json`** before §3.8 begins. `tz15.label_free` is asserted over every pricer row
before and after the write.

### 3.8 The labels, read once

Only in a run started with `--score`. Before the read the instrument asserts that
`origin/tz-16a-phase2-decisive-gate` is among the branches `git branch -r --contains HEAD` prints, with
`HEAD` from `git rev-parse HEAD` — each a fixed argument list with no shell — so no label is read by a
commit that is not on `origin` (map §7 items 54 and 63). Then **`tz10b.m2_labels(sorted(E))`** is
called once, `E` the union over `ADMITTED` of the eligible members, and one line is appended to
`/root/tz16a-work/label-ledger.jsonl`: the UTC instant, `HEAD`, the member count and
`tz07b.member_list_sha(E)`. A run without `--score` stops after §3.10 with its constants on disk and
reads no label; **every development run is such a run.**

### 3.9 The observed statistic, the reading, and what surrounds it

Per `tau`: `y` the label for `Up` and one minus it for `Down`; **`S = Σy`**; `T = (S − μ0) / n`;
`T_fee = T − Σfee(a) / n`; the win rate `S / n` beside the mean `a` and the mean `q`; and §4.1's reading
with the row that gave it. Where `n = 0` every ratio is printed as undefined and no unit leaves or joins
any denominator (map §7 item 64).

**Influence** (map §7 item 27), where `n >= 2`: with `x = y − a`, the member whose `|x − T|` is largest —
ties to the smallest `T0` — is removed, and `μ0`, `μ1`, `U0`, `U1`, `c`, `d`, `FP_E`, `FP_N`, `S` and the
reading are recomputed exactly on the `n − 1` at the same `r`, printed beside the value §4.1 reads.
Recorded, not a reading; where `n < 2` it is printed as undefined.

**Diagnostics, each barred from every reading:** over the eligible checkpoints whose Up book is
two-sided at the touch, the mean label, the mean mid, the mean `p_t`, and the Brier score of the mid
and of `p_t`, each printed as undefined where no such checkpoint exists; and **`residual_dependence`
over this look's own selected residuals in `T0` order** — `ρ_1`, `ρ_2`, `ρ_3`, `f̂` and `f`, or undefined
with its reason — the after-the-fact check of the assumption that the dependence carried over from
TZ-15's span.

**Nothing from step 12 onward raises on the labels or on any quantity computed from them.** Every
figure of this section is total, as its sentences above state. The assertions after step 12 are facts
about the run — V8's, V9's and host read 3's — and no label can trip one: a stop after the read would
leave labels read and no reading (map §7 item 83).

### 3.10 The chain book's interlock on Tier C — label-free and price-free

Map §2.5: since 2026-09-23 17:39:50 UTC every chain book window `T` loads the five-minute interval
`E = T + 600`.

- **Considered:** every unit §3.3 considers.
- **Exposed:** a considered unit with `T0 >= 1790185200` — `E` of window `1790184600`, the first the
  service ran (TZ-18a report §4) — with `T0 mod 900 = 600` and
  `/var/lib/btc-chainbook/{T0 − 600}/window.json` present; **fully loaded** where that file's `missed`
  is `0`. Every other considered unit with a manifest is the **control** — TZ-18's windows, `1790117100`
  to `1790145000`, among them: each sent two refused requests and read no book (map §2.5).
- **Failure:** the unit's manifest `quotes_complete` is not JSON `true`. A unit with no manifest is
  listed apart and belongs to neither group.
- **`f_E`, `m_E`, `f_C`, `m_C`** — failures and units, exposed and control. **`p_I`** is the exact
  probability, under exchangeability of exposure and failure, that a hypergeometric draw of `m_E`
  units from `m_E + m_C` holding `f_E + f_C` failures holds at least `f_E` of them: Fisher's one-sided
  exact test, in `Fraction`.
- From `/var/lib/btc-chainbook/runtime.jsonl`, every record's `event`, `pid` and `wall_ns`: the start
  record of pid `2699889` at `wall_ns` `1790185190022755903` (TZ-18a report §2.4), and whether a `stop`
  record follows it.
- **Printed:** the four counts, and the same split by era, `T0 < 1790185200` and after; the fully loaded
  count; every failure's `T0`; `p_I` exactly and to ten decimals; §4.3's reading and its power.

### 3.11 Predictions, pre-registered, barred from every gate and every reading

| # | prediction | population |
|---|---|---|
| P1 | the eligible count equals the admissible count at every `tau` | admissible members per `tau` |
| P2 | no `tau` reads EDGE | the five readings |
| P3 | NO EDGE at `tau` 240, 180, 120 and 60, and not at 90 | the five readings |
| P4 | `f < 1.3` at all five `tau` | §3.2, per `tau` |
| P5 | the interlock reads HOLD | §4.3's reading |

**The basis, written so the report can say which part failed.** On TZ-15's set the outcomes fell below
the pricer's claim by more than the one-per-cent lower tail of its own law at `tau` 240, 120 and 60 and
to that boundary at 180, while 90 sat near `0.12` (map §4). Doubling the set scales a persistent
shortfall's deviation by about `√2`, past `0.002` at four `tau` and not at 90. P4 rests on the
martingale property of a calibrated market's residuals — `ρ_k` near `0`, each with noise near `1/√n`.
P5 rests on the base rate, `0` of `2,016` in the week before the service started (map §2.5).

**P1 to P5 are TZ-16's, word for word.** The TZ-16 session computed §3.2's `ρ_k`, `f̂` and `f` from
TZ-15's file in a scratch probe and printed none of it in its report (its report §5), so P4 is still a
prediction written without the figure it predicts.

---

## 4. The gate

### 4.1 Reading per `tau`, this look, in this order

| condition | reading |
|---|---|
| `n = 0` | **UNDECIDABLE** — nothing was selected, so nothing is measured |
| `S >= c` | **EDGE** — whatever the powers are |
| `S <= d` | **NO EDGE** — whatever the powers are |
| otherwise | **UNDECIDABLE** |

Where `S >= c` and `S <= d` both hold — the side won more often than its price implied and less often
than the pricer claimed — the reading is EDGE and the report states that the claimed size is also
rejected. **No row reads a power:** each answer comes from its own exact test, and power decides nothing
after a label is read (CANON PART II).

**Error rates, fixed here, under the model each test scores** — independent coins at the stated
weights, their count's deviation widened by `r`: `FP_E <= 0.002` and `FP_N <= 0.002` at each `tau` on
this look, each exact under that model. With the second look's `0.008`, each answer's false-reading
probability is at most `0.01` per `tau` by the union bound, and at most `0.05` over the five `tau`,
whatever the dependence between `tau` and between looks. The exact `FP_E` and `FP_N` per `tau`, and
their sums over `tau`, are printed.

**Power, stated before any label and deciding nothing:** `POWER_E` against the pricer's law and
`POWER_N` against the market calibrated at its ask, per `tau`, beside the second look's projection.

### 4.2 The second look — fixed here, read by a later TZ

For each `tau` this look leaves UNDECIDABLE, and for no other: the first **3,600** qualifying slots with
`T0 > 1789669800`, formed by `tz06.scoring_set(manifests, 3600, after=1789669800)` with §0.8's and §3.3's
conditions at `3,600`, this look's 2,400 members among them; §3.4 to §3.7 unchanged; **`r` per `tau`
this TZ's own**, recomputed by this instrument's `dependence` from TZ-15's observations file as §9
preserves it and asserted equal to this report's printed value; `α2 = β2 = D("0.008")`; and §4.1's
table. That TZ imports `up`, `low`, `critical_upper`, `critical_lower`, `look_constants`, `dependence`,
`residual_dependence` and `read_look` from this instrument and writes none of them again.

**An EDGE either look reads is confirmed on the qualifying slots after the second look's 3,600th**, which
stay reserved on map §2.3's terms. The confirmation TZ is written only if an EDGE exists, and before any
label of those slots is read.

### 4.3 The interlock

**FIRE** where `f_E >= 1` and `p_I <= 0.01`; otherwise **HOLD**. False-alarm probability at most `0.01`,
exactly, under exchangeability. **Power, printed:** `k*`, the smallest `k >= 1` at which `k` exposed
failures and none in the control give `p_I <= 0.01`, and the exact probability that a binomial count
over `m_E` exposed units at `q` = `0.01`, `0.02` and `0.05` reaches `k*` — a disturbance that breaks that
share of exposed intervals against a control at its base rate `0`.

**Under FIRE**, after V3's comparison and before §9, block K-18a — TZ-18a §6.1, verbatim:

```
P=$(pgrep -fx '/root/tz01-env/venv/bin/python -B -u /root/tz18a-svc/tz18a-chainbook-capture.py --serve'); echo "pid=[$P]"; test -n "$P" && kill -TERM $P; echo "exit=$?"
```

The Executor runs the block once. If the session's classifier refuses it (map §6), the Executor prints
it, the Boss runs it verbatim in a root shell on the VPS, and the Executor waits. **Verification is the
Executor's, never the Boss's account:** `30` s after the block, `pgrep -fx` with the same argv prints no
line and exits `1`, and `/var/lib/btc-chainbook/runtime.jsonl` holds a `stop` record with the pid the
block printed, later than that pid's `start`. If the process is alive `120` s after the block, the same
block with `-KILL` in place of `-TERM` is authorized by the same route; a `stop` record then missing is
disclosed beside the `pgrep` read, which decides. **Under HOLD the block is never run.**

**Phase 2's readings stand under either.** A read the load broke removes a checkpoint from eligibility,
an event fixed before the outcome and blind to it, so it cannot move `S` against either law.

### 4.4 The verdict

- **EDGE at any `tau`** — Phase 2 reads **YES at those `tau`, subject to confirmation** (§4.2). Phase 3
  does not open on it.
- **NO EDGE at all five** — Phase 2 reads **NO for the Student pricer, inside its domain, at the five
  `tau`**: where it disagreed with the market by more than the fee, its side did not win at the rate it
  claimed. It says nothing about any other pricer.
- **Otherwise** — each `tau` reading NO EDGE is closed; each UNDECIDABLE `tau` goes to §4.2's second
  look; each EDGE awaits confirmation.

**What the gate assumes, named:** that outcomes of different intervals depend on one another, given the
prices, no more than `f` measures — to the third neighbour, and as TZ-15's span showed it; §3.9 prints
the same statistic on this look after the fact. **What it does not decide:** depth beyond the venue's
minimum size, the 50 ms taker delay and the oracle basis — Phase 3's. `T_fee` is printed beside every
reading and gates nothing. **This report on `main` is Phase 2's decisive first reading** — the one
CANON PART II calls TZ-16's, which map §5 assigns to this TZ — and the condition CANON PART II sets
before the backup track's B2 is written.

---

## 5. Implementation

### 5.1 The file, and the fixed order of the run

One new file, `research/tz16a-phase2-decisive-gate.py`. It loads **`tz15-phase2-gate.py`** once, through
an `importlib` helper of the shape of `tz15._load`, and takes `tz14`, `tz12`, `tz11a`, `tz10b`,
`tz07b`, `tz06`, `pfair`, `config`, `D` and `load_manifests` from that one module object; `analyze` and
`manifest` are then imported by name. **Nothing is loaded a second time.** **The load has side effects
this TZ names:** `tz15`'s module body writes `OPENBLAS_NUM_THREADS`, `OMP_NUM_THREADS` and
`MKL_NUM_THREADS`, loads `tz14` — which writes the same three, loads `tz12` and everything below it, and
installs an audit hook appending to `tz14.CAPTURE_OPENS` — and installs its own hook appending to
`tz15.OPENS`; neither hook can be removed, and this instrument reads neither list. **It installs its own
hook**, which records the absolute path, the mode and the current step of this section for every open
under `/var/lib/btc-recorder/` and `/var/lib/btc-chainbook/`.

From `tz15` it calls `pb_upper`, `crit`, `select` and `label_free` and reads `ADMITTED`, `ROW_KEYS` and
`PFAIR_PROBABILITY`. **It calls none of these eleven:** `analyze.venue`, `tz11a.fit_student`,
`tz14.v1_gates`, `tz14.selftests`, `tz14.build`, `tz14.main`, `tz15.v1_gates`, `tz15.selftests`,
`tz15.reading`, `tz15.build`, `tz15.main`.

**Functions, each with the contract named here:** `v1_gates` (§0.1), `locate` (§3.1),
`residual_dependence` (§3.2 and §3.9, total), `dependence` (§3.2, asserting), `up` and `low` (§3.7),
`critical_upper` and `critical_lower` (§3.7, returning `c` with `FP_E` and `d` with `FP_N`),
`look_constants` (§3.7, the six figures), `read_look` (§4.1, the reading and the
claim-rejected flag), `the_set` (§3.3), `the_rows` (§3.4), `the_quotes` (§3.5), `the_trades` (§3.6),
`labels` (§3.8), `observed` (§3.9), `influence` (§3.9), `diagnostics` (§3.9), `interlock` (§3.10, the
reads of `window.json` and `runtime.jsonl` and the four counts), `fisher_upper` (§3.10), and
`interlock_reading` and `interlock_power` (§4.3), `v2_static`, `v6`, `selftests` (§5.2), `build`,
`tables`, `csv_text`, `main`. **`fisher_upper`, `interlock_reading` and `interlock_power` are pure:** each
is a function of its integer or `Fraction` arguments alone and opens nothing; `interlock` calls all
three. `interlock_reading(f_E, p_I)` returns `"FIRE"` where `f_E >= 1` and `p_I <= Fraction(1, 100)`,
and `"HOLD"` otherwise.

**Modes:** `--selftest` runs steps 0 to 3 and stops — the only file it opens under a capture root is
the recorder's `runtime.jsonl`, through host read 1; a run with neither
flag stops at step 11; `--score` runs to the end. `--out` names the run directory, under
`/root/tz16a-work/`.

**The order of a run, and the instrument asserts it:**

0. `v1_gates`, §0.1;
1. host read 1, through `tz11a.host_read(when, t0s, floor)` at `tz11a.FLOOR_START_BYTES` with `t0s`
   empty; its `newest_start_sha` asserted equal to `4216c04673ced76b5b2ac60ef57c9abedc46f9b9`;
2. the eleven self-test items of §5.2, before any interval directory or chain book file is opened, then
   item 12's timed recursion, **the first fail-fast of §6**;
3. `v6` and `v2_static`;
4. §3.1 and §3.2 — TZ-15's files, V4 (a) and (b), and `f` per `tau`;
5. the set, §3.3, with its clock condition;
6. the rows, §3.4; host read 2 over the members; **the second fail-fast of §6**;
7. the quotes, §3.5;
8. eligibility, selection and the label-free report, §3.6; **the first `label_free` assertion**;
9. the constants, §3.7, written to `tz16a-constants.json`; **the second assertion**; V4 (d);
10. the interlock, §3.10;
11. without `--score`: host read 3 and V9's assertions, and stop;
12. with `--score`: the push assertion and the label read, §3.8;
13. the observed statistic, the readings, the verdict, influence and diagnostics, §3.9 and §4;
14. the tables, the disclosure and the observations file; host read 3 and V9's assertions.

### 5.2 Self-tests — eleven items, before any interval directory is opened, each an `assert`

Every expectation below is exact, and §10 C2 names how each was obtained: computed by the Architect with
an implementation that shares nothing with the code under test — the outcomes enumerated, or
`math.comb`, in exact rationals — or fixed by construction. **Every numeric comparison is between
`Decimal` or `Fraction` values, never between strings;** a reading or a reason is compared with the
exact word this TZ writes for it, a flag as a boolean, and item 11 asserts whether a call raises.

1. **`up` and `low` at `r = 1` against enumeration.** Over `w = [D("0.25"), D("0.5"), D("0.75"),
   D("0.5")]`, `U = tz15.pb_upper(w)`, `μ = D("2")`, `r = D(1)`: `up` at `s = −1 … 5` is `1`, `1`,
   `61/64`, `45/64`, `19/64`, `3/64`, `0`; `low` at `s = −1 … 5` is `0`, `3/64`, `19/64`, `45/64`,
   `61/64`, `1`, `1`. From the sixteen outcomes. **Fourteen assertions.**
2. **`critical_upper` at `r = 1`, and `tz15.crit` beside it.** Twenty copies of `D("0.5")`,
   `μ = D("10")`, `α = D("0.002")`: `c = 17`; `FP_E = 1351/1048576 = 0.00128841400146484375`; `up` at
   `16` is `1549/262144 = 0.005908966064453125`, above `α`; and `tz15.crit(w, D("0.002"))` returns `17`
   and the same `FP_E`. **Five assertions.**
3. **`critical_upper` under dependence.** The same coins, `r = D("1.21").sqrt()`: `r == D("1.1")`;
   `c = 18`, because `⌊10 + 8/1.1⌋ = 17`; `FP_E = 1351/1048576`; and `up` at `17` is `1549/262144`,
   because `⌊10 + 7/1.1⌋ = 16`. **Four assertions.**
4. **`critical_lower` against the binomial.** Twenty copies of `D("0.8")`, `μ = D("16")`,
   `β = D("0.002")`. At `r = D(1)`: `d = 9`; `FP_N = 53731317297/95367431640625 =
   0.00056341369766019072`; `low` at `10` is `247462024753/95367431640625`, above `β`. At `r = D("1.1")`:
   `d = 8`, because `⌈16 − 8/1.1⌉ = 9`; the same `FP_N`; and `low` at `9` is
   `247462024753/95367431640625`, because `⌈16 − 7/1.1⌉ = 10`. The denominator is `5^20`. **Six
   assertions.**
5. **The unreachable ends.** Three copies of `D("0.9")`, `μ = D("2.7")`, `α = D("0.002")`, `r = D(1)`:
   `c = 4 = n + 1`, `FP_E = 0`, and `up` at `3` is `0.729`. Three copies of `D("0.5")`, `μ = D("1.5")`,
   `β = D("0.002")`: `d = −1`, `FP_N = 0`, and `low` at `0` is `0.125`. **Six assertions.**
6. **`look_constants` at `r = 1`.** `a` twenty copies of `D("0.5")`, `q` twenty copies of `D("0.8")`,
   `α1 = β1 = D("0.002")`: `c = 17`; `d = 9`; `FP_E = 1351/1048576`;
   `FP_N = 53731317297/95367431640625`; `POWER_E = 39238821216256/95367431640625 =
   0.41144886195656851456`, the binomial `P(S >= 17)` at `0.8`; `POWER_N = 215955/524288 =
   0.4119014739990234375`, the binomial `P(S <= 9)` at `0.5`. **Six assertions.**
7. **`residual_dependence` against exact rationals**, over `x_i = y_i − a_i`. (a) `a` sixteen copies of
   `D("0.5")`, `y` = `1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0`: `ρ = 9/16, 1/8, −5/16`, `f̂ = 7/4`, `f = 7/4`.
   (b) `a` eight copies
   of `D("0.5")`, `y` = `1,0,1,0,1,0,1,0`: `ρ = −7/8, 3/4, −5/8`, `f̂ = −1/2`, `f = 1`. (c) `a` =
   `0.30, 0.55, 0.62, 0.41, 0.48, 0.70, 0.25, 0.53`, `y` = `1,1,0,0,1,1,0,1`:
   `ρ = 837/68824, −10645/17206, 165/9832`, `f̂ = −1544/8603`, `f = 1`. Each `ρ` and `f̂` within
   `D("1e-50")` of its fraction, each `f` exact. (d) `a` three copies of `D("0.5")`, `y` = `1,0,1`:
   undefined, reason `"n < 4"`. (e) `a` four copies of `D("0.5")`, `y` = `1,1,1,1`: undefined, reason
   `"v = 0"`. **Nineteen assertions**, fifteen values and four for (d) and (e).
8. **`read_look`.** `(n, S, c, d)` = `(0, 0, 1, −1)` → UNDECIDABLE; `(10, 8, 8, 2)` → EDGE, flag false;
   `(10, 2, 8, 2)` → NO EDGE; `(10, 5, 8, 2)` → UNDECIDABLE; `(10, 6, 6, 6)` → EDGE, flag true;
   `(10, 6, 7, 6)` → NO EDGE. **Eight assertions**, six readings and two flags.
9. **`fisher_upper` and `interlock_reading`,** called with literals. `(f_E, m_E, f_C, m_C)` =
   `(3, 10, 0, 20)` → `p_I = 6/203`, HOLD; `(4, 10, 0, 20)` → `2/261`, FIRE; `(2, 10, 1, 20)` → `51/203`,
   HOLD; `(0, 10, 0, 20)` → `1`, HOLD — each reading `interlock_reading(f_E, p_I)`. **Eight assertions.**
10. **`interlock_power`.** `m_E = 10`, `m_C = 20`: `k* = 4`, and at `q = 1/2` the power is `53/64`.
    **Two assertions.**
11. **The isolation guard, `tz15.label_free`:** it passes on two rows carrying `tz15.ROW_KEYS` with
    `label` `None`, and raises on a row whose `label` is `1`, on one carrying `Y` and on one carrying
    `r`. **Four assertions.**

**Item 12 is a timing, not a test:** `tz15.pb_upper` over 1,200 copies of `D("0.37")`, timed once; §6's
first fail-fast reads it.

**Eighty-two assertions over eleven items: 14, 5, 4, 6, 6, 6, 19, 8, 8, 2, 4.**

### 5.3 The shape of the diff

One new file and nothing else. The list of committed lines the change replaces, read from `origin/main`,
is **empty**; `git diff --name-only` against the merge base prints exactly
`research/tz16a-phase2-decisive-gate.py` on the scoring commit, and a subset of it on any earlier tree.

### 5.4 What may be fixed inside the session

Before the scoring commit is pushed, a failed self-test or assertion whose cause is the instrument's own
code may be fixed and the run repeated; each such fix is disclosed with its commit. **From the push
onward, every clause that reads BLOCKED binds whatever caused the failure, the Executor's own code
included** (map §7 item 78). An expectation of §5.2 or §7 is never edited: a wrong one is BLOCKED.

### 5.5 The runs, in this order

| run | what |
|---|---|
| **R-READY** | §0.2's host gate; then §0.8; then §0.5's first read and §0.6 |
| **B** | the two worktrees of §0.7; the build; `--selftest` as often as needed |
| **D1, D2** | at most two runs without `--score`, into `run-d1/` and `run-d2/`, each naming the tree or commit it ran on; a fix between them only as §5.4 allows |
| **C** | commit; push the branch; print `P_push`, `date -u +%s` as `git push` exits `0`, and `git ls-remote origin refs/heads/tz-16a-phase2-decisive-gate` |
| **S1, S2** | two runs with `--score` from fresh processes on the same pushed commit, into `run-s1/` and `run-s2/`, after §0.5's second read |
| **V3** | `cmp` of S1's and S2's compared files, and of their constants with every run without `--score` on that commit |
| **K** | block K-18a, only under FIRE (§4.3) |
| **RT** | retention, §9 |
| **P** | the report, from `/root/tz16a-work/wt-report`, straight to `main` |

---

## 6. Cost

Every figure at the maximum of the population it bounds (map §7 items 52 and 62). Rates are this
host's, measured by TZ-15 (its report §10), unless named.

| step | basis | seconds |
|---|---|---|
| gates, self-tests, `v6`, `v2_static` | TZ-15 measured `1.1`; the §5.2 recursions hold at most 20 coins | ~15 |
| TZ-15's files and `f`, §3.1 and §3.2 | one 6,001-line CSV; three lags over at most 440 residuals per `tau` | ~2 |
| the set, §3.3 | TZ-15 measured `19.4` for 1,296 units, `0.0150` a unit; here at most `3,600` units — every slot through about 2026-10-01, where map §5 puts 3,600 qualifying | ~54 |
| the rows, §3.4 | TZ-15 measured `93.5` for 1,200 walks; here 2,400 | ~187 |
| the quotes, §3.5 | TZ-15 measured `4.4` for 12,000 reads; here 24,000 | ~9 |
| the recursions, §3.7, §3.9 and V4 | at the unfiltered `n = 2,400` per `tau`: two at `n` for `U0` and `U1`, one at `n` inside `tz15.crit` for V4 (d), two at `3,600` for the projection, two at `n − 1` for influence — `54,710,402` units of `n²` per `tau`, `273,552,010` over five — and V4 (b)'s two per `tau` at TZ-15's `n`, `1,517,300`: **`275,069,310`** units, at the `0.3775` s per `1,440,000` TZ-15's item 8 measured | ~72 |
| the interlock, §3.10 | at most one `window.json` per exposed unit, a third of 3,600 | ~2 |
| labels, tables, host reads | one small `json` open per labelled member, at most 2,400 | ~10 |
| **one run** | | **~351** |
| **the session: two runs without `--score` and two with, at most** | against `tz12.SESSION_CEILING_S` = `3600` | **~1,404** |

**Fail-fast, both asserted, both derived from the table:**

1. Item 12's timing, `t12`: the run projects `275,069,310 × t12 / 1,440,000` s of recursion and is
   BLOCKED above **`400`** s — `5.5` times the table's `72`.
2. After step 6 the run's elapsed time must be at most **`450`** s — the table's
   `15 + 2 + 54 + 187 = 258` s, times `1.74`.

At both edges one run costs at most `450 + 400 + 9 + 2 + 10 = 871` s, and four runs `3,484` s, inside
`3600`. Nothing is sampled and no simulation is run: every constant is exact.

---

## 7. Validation

Each check states a count. **Asserted** means a Python `assert` or a `SystemExit` in the instrument that
produces the numbers, at the step of §5.1 named beside it; everything else is **recorded, not
asserted**. Every assertion holds on every run that reaches its step, with and without `--score`.

| # | check | what it must produce |
|---|---|---|
| **V1** | gates — asserted, step 0, and §0 | 6 of 6 anchors, four re-derived; 24 of 24 `frozen`, 2 `tracked`, 1 `reported`; H1 to H3, H4 printed; R-READY's line; §0.6's refs; the trees and the forensic count; the interpreter and `numpy` versions; every free-space read with its bound |
| **V2** | isolation — asserted two ways | **Static, step 3,** over the instrument's own tree: string constants carrying any of `tz14.BANNED_SUBSTRINGS`, docstrings exempt — **0**; calls of the twelve `pfair` entry points of `tz15.PFAIR_PROBABILITY` — **0**; call sites of `tz10b.m2_labels` — **exactly 1**; calls of §5.1's eleven — **0**; imports of `urllib`, `http`, `socket`, `ssl`, `requests` or `websockets` — **0**; `subprocess.run` — exactly one call site, whose argument list begins with the literal `"git"`, with no `shell` keyword. **At run time,** from the instrument's hook: opens whose basename carries `tz14.BANNED_SUBSTRINGS[0]` — at step 5 one per unit considered that has a manifest and that file, the set rule's own read; at every other step before 12, **0**; at step 12 exactly the members handed to `tz10b.m2_labels`; and every pricer row carrying exactly `tz15.ROW_KEYS` with `label is None` at steps 8 and 9 |
| **V3** | determinism — **BLOCKING on any difference, checked by `cmp` after S2**, the one check that compares two runs | `tz16a-constants.json`, `tz16a-readings.json`, `tz16a-tables.md`, `tz16a-observations.csv` and `tz16a-disclosure.md`, byte-identical between S1 and S2, with SHA-256 pairs; `tz16a-constants.json` also byte-identical to every run without `--score` on that commit. `tz16a-run.json` holds instants and timings, is not compared, and is named |
| **V4** | inputs — asserted | **(a) step 4:** both TZ-15 files by hash; the constants file's `n`, `sum_a` and `sum_q` per `tau`, as read; and §3.2's twenty literal comparisons — `n`, `Σy`, `Σa` and `Σq` at five `tau` — and fifteen equalities with the constants file — `n`, `Σa` and `Σq` at five `tau` — **35 of 35**. **(b) step 4:** TZ-15's constants re-derived from its observations file per `tau` — `tz15.crit([a ...], D("0.01"))` gives `s*` = `238 / 232 / 210 / 173 / 115` with `FP` within `D("5e-13")` of `0.007476034950 / 0.008749059109 / 0.007886034792 / 0.006740872864 / 0.008611872633`, and `tz15.pb_upper([q ...])` at `s*` lies within `D("5e-7")` of `0.325740 / 0.432618 / 0.430438 / 0.459935 / 0.467276` (TZ-15 report §5); this closes map §7 item 70 for TZ-15. **(c) step 5:** §3.3's assertions. **(d) step 9:** at every `tau`, §3.7's `c` and `FP_E` at `r = 1` equal `tz15.crit`'s |
| **V5** | the push precedes the label read — asserted, step 12 | `HEAD` among the branches containing it as `origin/tz-16a-phase2-decisive-gate`; `P_push` beside each label-read instant; the ledger printed whole, every line's commit equal to the reported one; a ledger line of any other commit disclosed and explained |
| **V6** | the diff — asserted, step 3 | merge base and head; `git status --porcelain` for the two scoped paths; `git diff --name-only` a subset of `{research/tz16a-phase2-decisive-gate.py}`, and exactly it on the scoring commit; no `global`, no `nonlocal`, no attribute store and no `os.environ` write in the file's own tree; the replaced-line list **empty** |
| **V7** | the self-tests — asserted, step 2 | 11 of 11 items and **82** assertions, distributed `14, 5, 4, 6, 6, 6, 19, 8, 8, 2, 4`; item 12's time; the output verbatim |
| **V8** | the frozen files are not moved — asserted at step 0 and at the run's last step, 14 with `--score` and 11 without | `research/pfair.py`, `research/tz14-quote-inventory.py` and `research/tz15-phase2-gate.py`, each equal to map §0 at run start and at run end |
| **V9** | the captures are untouched — asserted at the run's last step, 14 with `--score` and 11 without | `tz11a.host_read` at steps 1, 6 and that last step: pid and start record unchanged between the first and the last, the directory count not fallen, the read-set hash unchanged between reads 2 and 3. From the hook: every open in mode `r`, none with `w`, `x`, `a` or `+`; **no open of any file but `manifest.json` in an interval directory whose `T0` exceeds the last member**; under `/var/lib/btc-chainbook/`, no open of any file but `window.json` and `runtime.jsonl`; the count of opens per basename; everything the instrument can write, enumerated — its `--out` directory and `/root/tz16a-work/label-ledger.jsonl` |
| **V10** | the fingerprint table | every row of map §0 in lines, bytes and SHA-256, and the new file beside them as it stands on the branch |
| **V11** | disclosure | `tz16a-disclosure.md`: every unit considered in ascending `T0` with UTC, weekday, reasons, the manifest's `quotes_complete` and the interlock group; per `tau` the eligible and the selected `T0` lists, each with its count and `tz07b.member_list_sha`; the listed reads of §3.5 by reason. `tz16a-observations.csv`: **12,000 rows and a header**, one per member per `tau` in `ADMITTED`, TZ-15's eighteen columns in TZ-15's order — sufficient to reconstruct every number of §3.6, §3.7 and §3.9 without re-running |
| **V12** | influence, diagnostics, predictions — recorded | §3.9's influence line beside each reading, or undefined; the diagnostics, §3.9's own-look `ρ_k` and `f` among them, or undefined with its reason; §3.11's five predictions, each held or refuted with its figure |
| **V13** | the interlock — asserted, step 10 | `m_E + m_C` plus the units with no manifest equal the units considered; `f_E <= m_E` and `f_C <= m_C`; `p_I` exact; §4.3's reading and power; under FIRE, run K's verification per §4.3 |

**Causality is not re-tested, and this is why.** `p_t` is `tz11a.checkpoint_row`'s own, which TZ-10b V2
proved bit-identical under perturbation strictly after the checkpoint — 140 of 140, with 140 of 140
negative controls (map §4). Every quote lands after its checkpoint, `+39.6` ms at the earliest over
16,800 reads (map §2.3). The label is the one future quantity, and it enters nothing before step 12.

---

## 8. The report

`CryptoReports/TZ-16a-phase2-decisive-gate-report.md`, straight to `main` in one commit, immutable once
committed.

**In its first ten lines:** the reading at each `tau`; the verdict; the interlock's reading; and which
TZ must follow — §4.2's second look, a confirmation, both or neither.

Then, in this order: §0's gates, host reads, refs, trees and every free-space read; §3.1 and §3.2 with
the constants file's three values per `tau` and the item-70 sums; §3.3's set; §3.4 to §3.6's label-free
report per `tau`; §3.7's constants per `tau` —
`n`, `μ0`, the null's distinct prices with their counts, `Σq` to `Σq⁴`, `r`, `c`, `d`, `FP_E`, `FP_N`,
`POWER_E`, `POWER_N`, the independence columns and the projection — with the instant
`tz16a-constants.json` was written; `P_push` beside each label-read instant (map §7 item 63); §3.9 —
`S`, `T`, `T_fee`, the reading and the row of §4.1 that gave it, influence, diagnostics; §3.10 and
§4.3; §3.11; the implementation, the file's hash on the branch and its commit; V1 to V13 with their
counts; publication with contract §4.2's self-check; §9; and every point where the text needed a
reading, with the workaround chosen.

It states `wc -l` and `sha256sum` for the map and every file its fingerprint table lists. **A report is
evidence, not acceptance:** no reading stands until the Architect has re-derived `c` and `FP_E` exactly
from the distinct-price table and `r`, `d`, `FP_N` and the powers within the four-cumulant
approximation, `f` from §3.2's sums, and `S` from the counts printed.

---

## 9. Retention

In this order, each step only after the previous one exited `0`, only after S2 and V3, and after run K
where it ran:

1. **Copy first.** Every file under `/root/tz15-work/`, `/root/tz16-work/` and `/root/tz18a-work/`,
   worktrees included, whose SHA-256 is named by any committed report on `main` — every hexadecimal
   token of 16 to 64
   characters those reports print, matched against the full hash and its 16-character prefix, the
   predicate TZ-14 and TZ-15 used — and, by name, `/root/tz15-work/label-ledger.jsonl`; each that
   `/root/btc-forensics/` does not already hold by hash is copied there by exclusive create, under its
   path below `/root/` with `/` replaced by `--`, the hash asserted at source and destination. Assert
   that the **1,046** files already there are unchanged, and that both of §3.1's files are held. Report
   the counts before and after.
2. **Then the five worktrees:** `/root/tz15-work/wt`, `/root/tz15-work/wt-report`,
   `/root/tz16-work/wt-report`, `/root/tz18a-work/wt` and `/root/tz18a-work/wt-report`, each by
   `git worktree remove` without `--force`; an untracked `__pycache__` in one is deleted first and
   named; each verified by `test -e`.
3. **Then the three trees:** `rm -rf /root/tz15-work`, `rm -rf /root/tz16-work` and
   `rm -rf /root/tz18a-work`, one command naming one tree each, each verified by `test -e`. If the
   session's classifier refuses one, hand the Boss that one exact block and verify the outcome from
   `test -e` afterwards, never from his report (map §6).

**Never removed:** `/root/tz18a-svc/`, from which the service runs — under FIRE its stop is verified and
the tree stays for the next TZ; both capture roots; `/root/tz01-env/`; `/root/tz04a-env/`.
`/root/tz16a-work/`, the label ledger included, is the next TZ's to reclaim on the same terms.

---

## 10. Pre-send checks

Performed against this file, start to end, as a separate reading after its last section was written,
with the repository cloned at `origin/main` `a9e0b45f25769071940ddaefb4fdf1b374f12e78`, the TZ-16
report, and against map revision `2026-09-27-a`, which ships with this file. **The first separate
reading found two defects, both carried from TZ-16 and both repaired before the file was sent:** §5.2's
opening paragraph called every expectation computed by an independent implementation and every
comparison numeric, while items 7 (d) and (e), 8 and 9 compare words or flags, item 11 asserts whether a
call raises, and items 7 (d) and (e), 8 and 11 are fixed by construction; and §2 item 6 (c) said TZ-15's labels enter `f` alone, while V4 (a) sums
`y` as well. The first repair added one entry to the header's list of differences. **A second full
reading, after the repairs, found none.**

**C1 — scope against body.** Enumerated from §0 to §9 by a script over this file's own text, then read:
**9** repository paths — two written, `research/tz16a-phase2-decisive-gate.py` and
`CryptoReports/TZ-16a-phase2-decisive-gate-report.md`; five read, `SYSTEM-MAP.md`, `research/pfair.py`,
`research/tz14-quote-inventory.py`, `research/tz15-phase2-gate.py` and `research/recorder/recorder.py`,
the last for one constant; and two named as the TZ this one replaces and its report, which the
instrument neither reads nor writes; **39** host paths and path fragments; **45** committed entry points
and module attributes written as `module.name`; **6** output files and the ledger. Intersections with
§2's prohibitions, by path and by content class: **10**, each resolved in §2 where the prohibition is
made — K-18a against item 3, as its exemption; §3.10's reads of `window.json` and `runtime.jsonl`
against item 3, which names them; §9's copy against item 4, as its exemption; the report's push against
item 5, as path 2; `tz06.qualification` with `analyze.venue` inside it, `tz10b.m2_labels`, and §3.1 and
§3.2's reads of TZ-15's two files against item 6, as its exemptions (a) to (c); `tz11a.checkpoint_row`'s
internal link quantities against item 7; the committed loader's read of every manifest against item 9,
which excepts `manifest.json`; and `git` against item 10, which names it. **By content class:**
`tz16a-constants.json`, `tz16a-observations.csv`, `tz16a-readings.json` and the report carry prices,
labels and outcomes of the span map §2.3 reserves for this TZ — item 6 orders their label content after
the constants and the push, and item 9 confines them to this look's members; TZ-15's constants file
carries prices of TZ-15's set and no label; no output carries a chain book price, since item 3 opens no
body; and no fifteen-minute settled document is opened. §9's removal of `/root/tz15-work/`,
`/root/tz16-work/` and `/root/tz18a-work/` meets no prohibition, and §2 names it. The diff was
performed, not intended.

**C2 — origin of every expectation.** **§5.2: 82 expectations**, one per assertion. **66** computed by the
Architect on 2026-09-27 in exact rationals, by an implementation that shares nothing with the code under
test — item 1's fourteen by enumerating the sixteen outcomes; items 2, 4, 5, 6 and 10's twenty-five from
`math.comb` binomials and hypergeometrics; item 3's four from the same law, the two floors written beside
them and `D("1.21").sqrt()` at 60 digits; item 7's fifteen values as exact rational autocovariances; item
9's eight from `math.comb` in integers and §4.3's reading rule — and **16** exact by construction: item
7's four for (d) and (e), whose three residuals and whose constant residuals fix the outcome, item 8's
eight and item 11's four. Each is compared with tolerance `0`, or `D("1e-50")` for item 7's sixty-digit
quotients, ten decades inside an exact reference. **Quoted from committed artifacts** — from a report,
only a figure its instrument printed, the printing function named: step 1's start-record sha from map §6; V1's six anchors and the counts `24`,
`2`, `1` from map §0; V4 (a)'s `n` from the `selected` column and its `Σy` and `Σa` from the `S` and
`sum a` columns that `tz15.tables` prints — the TZ-15 report §4 and §7 — and its five `Σq` from the
TZ-16 report §3, the verbatim output of a script, printed there beside it, whose line prints the
constants file's `sum_q` string; V4 (b)'s fifteen from the TZ-15 report §5, the `s*`, `FP` and `POWER`
columns `tz15.tables` prints, each tolerance half a unit of the last digit printed; the two TZ-15 hashes
from the TZ-15 report §12. **No value is quoted from a figure a report's author composed** (map §7 item
82): the TZ-15 report's `Σ q` column is used nowhere, and V4 (a)'s fifteen further comparisons are
equalities with the constants file itself, located by hash. **From this TZ's own text:** V2's
zero-or-one counts, V4 (a)'s `35`, V7's `11`, `82` and split, and V11's `12,000` = `2,400 × 5` over
TZ-15's eighteen committed columns. **§6's `400` and `450` s are resource guards on wall-clock time**,
and §0.8's `2,400` and `3,900` are this TZ's literals, the second derived from `S7_DEADLINE_S`. **None
depends on a quantity this TZ measures:** `f`, `r`, `c`, `d`, the powers, `S` and the interlock counts are
compared with no literal, and V4 (d) compares two computations of the same run.

**C3 — shape of every diff.** One new file, `research/tz16a-phase2-decisive-gate.py`, absent from
`origin/main` at `a9e0b45`: the committed lines the change replaces are **none**, and the phrase C3 bars
for a non-empty list does not occur in this file.

**C4 — cost of every check.** §6 states each step at its population's maximum, unchanged from TZ-16 and
recomputed by script on 2026-09-27: 3,600 units for the set at TZ-15's measured `0.0150` s a unit; 2,400
walks at `93.5` s per 1,200; 24,000 reads at `4.4` s per 12,000; the recursions at the unfiltered
`n = 2,400` per `tau` — seven per `tau`, three at `n`, two at `3,600`, two at `n − 1`, `54,710,402` units
of `n²` — plus V4 (b)'s `1,517,300`: **`275,069,310` units, `72.1` s** at TZ-15's `0.3775` s per
`1,440,000`. **~351 s a run and ~1,404 s for four**, against `3,600`. What this TZ adds to TZ-16 — one
JSON parse of a file TZ-15 wrote, and two self-test cases of three and four residuals — sits inside the
table's `~2` and `~15` s. Both fail-fast bounds are derived beside their figures: `400 = 5.5 × 72` and
`450 = 1.74 × (15 + 2 + 54 + 187)`; at both edges `871` s a run and `3,484` s for four. Nothing is
sampled and nothing is simulated.

**C5 — every count**, each beside its source: `2,400` members (§3.3), `12,000` = `2,400 × 5` and
`24,000` = `12,000 × 2` (§3.0); `405 / 428 / 440 / 380 / 271` from the TZ-15 report §4's `selected`
column and `210 / 211 / 190 / 164 / 99` from its §7's `S` column; `2` and `5` copies from the TZ-16
report §2; `24`, `2` and `1` by parsing map revision `2026-09-27-a`'s §0 under `tz14.fingerprint_rows`'
rule, run by the Architect — 27 rows; `6` anchors from map §0, found by `tz15.v1_gates`' anchor pattern
over that revision; `1,046` files and six worktrees from map §3, which reads them from the TZ-16 report
§1.6; `2,016` from map §2.5; the eleven never-called names counted from §5.1's list; `12` `pfair` entry
points and `9` row keys counted from `tz15.PFAIR_PROBABILITY` and `tz15.ROW_KEYS` in committed code;
`82` = `14 + 5 + 4 + 6 + 6 + 6 + 19 + 8 + 8 + 2 + 4`, counted item by item over `11` items, item 7's `19`
= `15 + 4`; V4 (a)'s `35` = `20 + 15`, four quantities at five `tau` and three at five; V4 (b)'s `15`,
three at five `tau`; `18` columns from `tz15.csv_text`'s header; `6` barred imports and `5` compared files
from V2's and V3's own lists; `3` host reads, at steps 1, 6 and the last; §9's `5` worktrees — §0.2's six
less the primary checkout — and `3` trees; `4` rows in §4.1, `5` predictions in §3.11, `13` Validation
rows, and the header's `10` differences. Every row of §7 that says asserted names its step in §5.1 — V1 0,
V2 3 and 5 to 12, V4 4, 5 and 9, V5 12, V6 3, V7 2, V8 0 and the last, V9 the last, V13 10 — and V3,
which compares two runs, is BLOCKING by `cmp` instead.

**C6 — every population.** §3.2's sums, `ρ_k`, `f̂` and `f`: TZ-15's selected members at that `tau`, in
`T0` order; the constants file's `n`, `sum_a` and `sum_q`: the same members, as TZ-15's instrument
selected them. §3.3: the units considered and the members. §3.4's admissible counts: the members, per
`tau`. §3.5's reads: the members' quote files at the five `tau`. §3.6's eligible count: the admissible
members; the selected counts, the `Q` summaries of `a` and `q − a` and both means: the selected members
at that `tau`; `D` and the confidence share: the eligible checkpoints whose Up book is two-sided at the
touch. §3.7's `U0`, `U1`, `c`, `d`, `FP_E`, `FP_N`, `POWER_E`, `POWER_N`, the distinct-price table and the
power sums: the selected members at that `tau`; the projection: those weights and their even-position
half. §3.9's `S`, `T`, `T_fee` and win rate: the selected members; influence: them less one; the Brier
scores and means: the eligible two-sided checkpoints; the own-look `residual_dependence`: the selected
members in `T0` order. §3.10's four counts and `p_I`: the units considered that have a manifest; its
power: the `m_E` exposed units. §4's family bounds: the five `tau` and the two looks. V4 (a) and (b):
TZ-15's selected members per `tau`. §3.11: each prediction's third column.

**C7 — every signature and every behaviour**, read from `origin/main` at
`a9e0b45f25769071940ddaefb4fdf1b374f12e78`, where every file below is byte-identical to its map §0
`frozen` row. All 45 `module.name` references resolve, through `ast`, to a top-level name of the file map
§3 assigns the module. Each called function as the file holds it, with the lines the sentences rely on:

- `tz06.scoring_set(manifests, need=SET_SIZE, *, after=None)` — opens the walk at
  `min(int(name) for name in os.listdir(...) if int(name) > after)`, walks
  `while members < need and t0 <= last` with `t0 += config.INTERVAL_S`, and `return rows, members == need`,
  each row `{"T0", "reasons", "member"}`.
- `tz06.qualification(t0, manifests)` — `why = list(reasons_for(manifests.get(t0)))`, then
  `info = venue(t0) if manifests.get(t0) else None` and `if info["resolved_up"] is None`,
  `if info["price_to_beat"] is None`: existence alone. `analyze.reasons_for(doc)` returns
  `["no manifest"]` for `None`, else collects `disconnect`, `no S6` and `no S7`, and asserts
  `doc["complete"] == (not why)` — so `complete` is the first condition, as §0.8 says.
  `analyze.load_manifests()` keys each manifest by `doc["T0_epoch"]`, the key §0.8 reads.
- `tz11a.walk_member(t0, manifests, guard)` — reads `pfair.reports(t0, ...)` and
  `pfair.merged_stream(t0, ...)`; asserts `sigma_hat == priced[tau]["sigma_live"]`, `horizon > 0`, a mean
  at every kept anchor and at least one kept anchor; returns a dict keyed by `pfair.TAUS`.
- `tz11a.checkpoint_row(t0, name, tau, row)` — returns
  `"admissible": row["sigma_hat"] >= pfair.ADMIT[tau]`, `"p_t": pfair.p_fair_student(...)`, three further
  link quantities, `"Y"`, `"r"` and `"label": None`; `name` lands in a `"set"` key the pricer row drops.
- `tz11a.host_read(when, t0s, floor)` — `assert free >= floor`, `assert doc["recorder_pids"]`; returns
  `newest_start_sha` from `tz10b.newest_start`, which opens `RUNTIME_PATH`, the recorder's top-level
  `runtime.jsonl`, and `read_set_sha256` from `tz10b.read_set`, which calls `os.stat` and opens nothing.
- `tz10b.m2_labels(members)` — `info = venue(t0)`,
  `assert info is not None and info["resolved_up"] is not None`, `out[t0] = 1 if info["resolved_up"] else 0`.
- `tz07b.member_list_sha(members)` — the SHA-256 of the sorted `T0` list joined by newlines, with no
  trailing newline.
- `tz14.fingerprint_rows()` — a line of five cells whose first starts with a backtick and whose fourth is
  `frozen`, `tracked` or `reported`; `tz14.documents(t0)`, whose `tokens` maps each id string to its
  outcome and is empty unless `outcomes` is exactly Up and Down; `tz14.quote_lines(dirpath)`, each read
  carrying `tau`, `token_id` as a string, `status`, `raw` and `body_is_json`; `tz14.book_of(raw)`, with
  `ok` and a `_present` key for each of `BODY_FIELDS`, which holds `tick_size` and `min_order_size`;
  `tz14.touch_of(book, min_size, tick)`, with `ask5` and `bid5`; `tz14.fee_pp(p)`,
  `FEE_RATE * p * (D(1) - p)`; `tz14.q_summary(values)`; `tz14.cell(value)`, `str(value)` for a
  `Decimal`; `tz14.weekday_of(t0)`; `tz14.is_weekend(t0)`; and `tz14.BANNED_SUBSTRINGS`, whose first entry
  is `"reso" + "lution"`.
- `tz15.pb_upper(weights)`, which returns `U(s)` for `s = 0 … n`; `tz15.crit(weights, alpha)`,
  `return s_star, (upper[s_star] if s_star <= n else D(0)), upper`; `tz15.select(p, ask_up, ask_dn)`,
  with keys `e_up`, `e_dn`, `selected`, `side`, `a`, `q`, `edge` and `both_positive`;
  `tz15.label_free(rows)`, `assert set(row) == set(ROW_KEYS)` and `assert row["label"] is None`;
  `tz15._load(name, filename)`; and `tz15.ADMITTED`, `tz15.ROW_KEYS`, `tz15.PFAIR_PROBABILITY`.
- **The two TZ-15 functions §3.1 and §3.2 now lean on.** `tz15.tables(doc)` prints `f["selected"]` in
  its §3.4 table and `o["S"]` and `_s(o["sum_a"], 4)` in its §3.7 table, and prints **no `sum_q`
  anywhere** — which is why the TZ-15 report's `Σ q` column is quoted nowhere. `tz15.build(score, out_dir)`
  writes `tz15-constants.json` at its step 8, before its step 10's label read, as
  `json.dumps({..., "per_tau": {str(tau): {"n": consts[tau]["n"], ..., "sum_a": str(consts[tau]["sum_a"]),
  "sum_q": str(consts[tau]["sum_q"]), ...}}}, indent=2, sort_keys=True)`, where `constants` sets
  `"n": n` and `"sum_q": sum(weights_q, D(0))` over the selected rows of that `tau` in ascending `T0`.
- The constants `tz11a.FLOOR_START_BYTES` `2060000000`, `tz11a.FLOOR_BYTES` `2000000000`,
  `tz12.SESSION_CEILING_S` `3600`, `pfair.ADMIT`, `pfair`'s `decimal.getcontext().prec = 60`, and
  `S7_DEADLINE_S = 3600` in `research/recorder/recorder.py`, whose `close_interval` runs
  `await self.fetch_s7(t0, path)` before `doc = manifest.write(path)`.
- **The chain book's files**, read from `research/tz18a-chainbook-capture.py`: `window.json` is written
  under `os.path.join(CHAINBOOK_ROOT, str(T))`, its keys `missed` and `T` among them; `runtime_record`
  appends records carrying `event`, `pid` and `wall_ns` to `runtime.jsonl` under `CHAINBOOK_ROOT`. §4.3's
  K-18a is TZ-18a §6.1's block, character for character.
- **The loads are behaviours and are quoted too:** `tz15`'s module body writes the three environment
  variables, loads `tz14` through `_load` and calls `sys.addaudithook(_audit)`, whose hook appends to
  `OPENS` for opens under `config.ROOT`; `tz14`'s writes the same three, loads `tz12` and installs its
  own hook.

**C8 — every cross-reference**, resolved by reading the referenced text: CANON PART II's gate rule, its
B2 row and its naming of TZ-16 as the decisive gate (§1, §4.1, §4.4); map revision `2026-09-27-a` §0
(the header, §0.1, §2, V1, V8, V10), §1 (§0.6), §2.3 (§0.8, §1, §4.2, §7), §2.5 (§0.2, §1, §2, §3.10,
§3.11), §3 (§0.2, §1), §4 (§3.11, §7), §5 (§1, §3.0, §4.4, §6), §6 (§0.2, §0.3, §0.4, §4.3, §9) and §8
(§0.2); map §7 items 27, 29, 52, 54, 62, 63, 64, 69, 70, 71, 78, 82 and 83; contract §4.1 and §4.2 (§2, §8); the TZ-15 report
§0.2, §4, §5, §7, §10 and §12; TZ-15 §3.3 and §3.4 (§3.5, §3.6); the TZ-16 report §2, §3 and §5 (the
header, §3.1, §3.2, §3.11); TZ-18a §6.1; and the TZ-18a report §2.4 and §4. **Checked mechanically as
well:** every `§` of this file that names its own section resolves to one of its headers, and every map
item named exists in map §7 of the revision this file ships with. Each supports the sentence that makes
it.

**Checks this session could not perform:** none of C1 to C8 — the repository was reachable. **What only
the host holds is converted into BLOCK conditions the Executor evaluates** (CANON hard rule 13): TZ-15's
two files by hash and the constants file's fifteen values (§3.1, §3.2, V4 (a)) — this session cannot read
either file, and checked instead that the TZ-16 report's five `Σq` reproduce every `mean q` and
`mean q − a` TZ-15's instrument printed, 10 of 10, and that at `tau` 180 the printed `mean q − a` alone
excludes the value TZ-16 quoted; the trees, the forensic count and the worktrees (§0.2); and R-READY
(§0.8).
