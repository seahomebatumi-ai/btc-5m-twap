# TZ-15 — the Phase 2 gate

**Canonical filename:** `TZ-15-phase2-gate.md`. The committed file takes this name and no other.

**Executor model: Opus.** Gate arithmetic, an exact tail computation, a label read, and the first
statistic in this project that puts a quote beside the pricer.

**Required System Map revision:** `2026-09-19-a`.

**Required anchors**, from map §0. A mismatch on any one is BLOCKED before any work:

| anchor | required |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-inventory-complete` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` |
| `A6` — pricer | `729f0bcdbee3` |

---

## 0. Gates, host, interpreter, floor

**0.1 Fingerprint, asserted inside the instrument as step 0 of §5.1** (map §7 item 66: a check called
asserted has a step). Read `SYSTEM-MAP.md` in the checkout the instrument runs from, a branch cut from
`origin/main` after this revision landed. Its revision string must read `2026-09-19-a` and its six
anchors must equal the table above; the four that are the first 12 hex characters of a committed
file's SHA-256 — `A2`, `A4`, `A5`, `A6` — are also re-derived from those files' bytes, as TZ-14 did.
Hash every row of its §0 fingerprint table in lines, bytes and SHA-256: the **21** `frozen` rows must
equal the hashes printed there, the **2** `tracked` rows are reported with no expectation, and
`SYSTEM-MAP.md` itself is reported. Any `frozen` mismatch is BLOCKED. The rows are read with
`tz14.fingerprint_rows()`; the expected revision, the six anchors and the count `21` are literals of
this instrument, so the gate never reads its own expected values from the file it checks. **`tz14.v1_gates` is not called**: it
asserts revision `2026-09-18-b` and twenty rows (map §3).

**0.2 Host gate**, all three or this is not the capture host and the run is BLOCKED:

- `/var/lib/btc-recorder/btc-updown-5m/` exists and holds interval directories; report the count, the
  first and the last `T0`, **each with the UTC instant the listing was taken**.
- A recorder process is running and the newest `runtime.jsonl` start record carries sha
  `4216c04673ced76b5b2ac60ef57c9abedc46f9b9`; report the pid and the `recv_ns`.
- The filesystem holding it is `/dev/vda2`, total `31,612,203,008` bytes.

**0.3 Interpreter.** Every command of the instrument runs on `/root/tz01-env/venv/bin/python` —
Python 3.12.x. Report the version and `numpy`'s. `import numpy` must succeed, because the committed
chain the instrument loads imports it; the instrument itself computes nothing in `numpy`.

**0.4 Resource floor, in exact bytes, derived from map §6.** Free space on `/dev/vda2` at run start
must be at least `tz11a.FLOOR_START_BYTES` = `2,060,000,000`; every later read at least
`tz11a.FLOOR_BYTES` = `2,000,000,000`. Both asserted. Report every read with its UTC instant, its
reader and its bound.

**0.5 Preflight, twice, at least `1,800` s apart**, the first before the build and the second before
the first scored run. Each records `df -B1` on `/dev/vda2`, `du -sb /root/PROJECT_GAMING_PS5`, and the
exit codes of `systemctl is-enabled telemetry-watch.service` and `systemctl is-active
telemetry-watch.service`. Report both, the elapsed seconds and the implied bytes/day of each quantity.
**This run's own footprint — `/root/tz15-work` and `/root/.claude` — is stated separately at both
reads** (map §7 item 29). The preflight gates nothing beyond §0.4.

**0.6 Refs.** Run `git ls-remote` against `origin` before the branch of §2 exists and report every ref.
Map §1 records one branch, `main` at `93d13415b8f29cea6cc6626c86488676c6538dcf`. A difference is
recorded, not BLOCKING, unless `main` no longer carries the revision §0.1 requires.

**0.7 The trees.** `test -e /root/tz13-work` must exit non-zero — map §3 records TZ-14's §9 removing
it. `/root/tz14-work/` must exist: V4 reads a TZ-14 output from it before §9 reclaims it. Report both.

---

## 1. Why this TZ exists

Phase 2 is the decision point, and TZ-14 has made its gate writable: the quote capture is complete,
the book is characterised, and no statistic of a quote against the pricer has been computed, so the
sampling rule below is fixed while it is still free to be fixed (CANON PART II).

**The gate does not score the deviation between the market and `p_t`, and that is deliberate.** Phase
1 only failed to disqualify the Student pricer, and TZ-13 measured it leaning under-confident at `tau`
90, 60 and 30. A gap between `p_t` and the quote is therefore as likely to be the pricer's error as
the market's, and a test of "is the gap non-zero" would find one every time and mean nothing — the
old G3's defect (map §7 item 49) moved to the decision point.

**The gate asks the only question that decides anything: where `p_t` says the executable ask is cheap
after the taker fee, is the market actually wrong?** At each admissible checkpoint the instrument
takes, on paper and one share, the side `p_t` says is underpriced by more than the fee, and the
venue's outcomes say whether that side won more often than the ask it paid implied. The null is **a
market calibrated at its own ask**. Under it the outcome of each trade is a coin weighted by the price
paid, whatever `p_t` says — so the pricer's miscalibration cannot manufacture a false edge: a wrong
`p_t` only selects trades that do no better than the prices paid. The number of wins is a sum of
independent coins with known weights, so its distribution is computed **exactly**, with no
simulation: the false-positive probability and the power against "the pricer is right" are exact
numbers, and both are on disk before any outcome is read.

**The set is TZ-14's**, re-formed and asserted by hash. Its outcomes were read by earlier TZs, to score
the pricers; its quotes were read by TZ-14 alone; **outcome, quote and `p_t` together have never been
seen by anyone**, and the null above uses no outcome at all. A reading of EDGE is nevertheless not
enough to open Phase 3: it is confirmed first on the span map §2.3 reserves, whose quotes and outcomes
no one has opened (§4).

**The selection threshold is not a knob.** A trade is selected where the edge on one side is positive
after CANON §1.1's taker fee, computed by `tz14.fee_pp` — the fee the trade would actually pay. No
constant of this TZ was chosen by looking at a quote beside a price.

---

## 2. Scope

**Repository paths this TZ may write, and no others:**

1. `research/tz15-phase2-gate.py` — new file, on branch `tz-15-phase2-gate`, then a pull request. Not
   merged by the Executor.
2. `CryptoReports/TZ-15-phase2-gate-report.md` — straight to `main`, in one commit, as contract §4.1
   requires. **This is the one path this TZ pushes to `main`, and it is an exemption to item 4 of the
   prohibitions below.**

**Prohibited, each absolutely:**

1. No committed file is modified. Every `frozen` row of map §0 is byte-identical at run end.
2. Nothing under `/var/lib/btc-recorder/` is created, written, moved or removed; every file there is
   opened read-only. The recorder is never signalled, stopped or restarted.
3. `/root/tz04a-env/`, `/root/tz01-env/` and `/root/btc-forensics/` are never removed or emptied.
   **Exemption:** §9 copies files *into* `/root/btc-forensics/` by exclusive create.
4. Nothing is pushed to `main` except the report of item 2 above.
5. **No label is read before §3.5's constants are on disk and the scoring commit is on `origin`.** A
   label is the venue's resolved outcome. **Three exemptions, each named because the TZ's own body
   requires it:** `tz06.qualification`, which `tz14.the_set` reaches through `tz06.scoring_set` for
   every unit considered and which reads `resolved_up` and `priceToBeat` through `analyze.venue` to
   decide membership; `tz10b.m2_labels`, the one label reader this TZ calls, once per scored run, at
   §3.6; and V4's read of TZ-13's observations file, which carries a `label` column and is opened only
   after §3.6.
6. **The instrument computes no probability itself.** `p_t` is the `p_t` field of
   `tz11a.checkpoint_row`, and nothing else in the instrument's own syntax tree calls any of
   `pfair.p_fair`, `pfair.p_fair_student`, `pfair.state_and_sd`, `pfair.far_branch`,
   `pfair.near_branch`, `pfair.observations`, `pfair.corrected_sd`, `pfair.student_sd`, `pfair.phi`,
   `pfair.log_phi`, `pfair.t_cdf` or `pfair.log_t_cdf`. **Exemption:** `tz11a.checkpoint_row` computes
   `p_t` and three further link quantities internally; the instrument keeps `p_t` alone.
7. **No settlement-derived quantity enters any row.** `tz11a.walk_member` computes `Y` and `r`, which
   are functions of the oracle after the checkpoint, and `tz11a.checkpoint_row` returns them. The
   instrument builds its rows from an explicit key allow-list — `T0`, `tau`, `state`, `sigma_hat`,
   `admissible`, `sd_student`, `z_student`, `p_t`, `label` — and V2 asserts that every such pricer row
   carries exactly those nine.
8. **The reserved span of map §2.3 is not touched.** No quote file, `gamma.json`, `resolution.json` or
   stream is opened in any interval directory with `T0 > 1789669800`. `manifest.json` is excepted,
   because `analyze.load_manifests` reads every manifest for every set formation.
9. No fit is performed and no constant is produced for any file. The gate's constants are computed per
   run from committed code and written to this run's own output.
10. No Release is created and no dataset, archive or binary enters git history.

---

## 3. The measurements

### 3.0 Partitions and counts

- **`ADMITTED` = `(240, 180, 120, 90, 60)`** — the five `tau` open for Phase 2 (map §5). No figure of
  this TZ is computed at `tau` 30 or 10; the committed functions it calls compute them internally, and
  they are discarded.
- The set is **1,200** members; the scored checkpoints are **6,000**, `1,200 × 5`; the admitted reads
  are **12,000** at full completeness, `6,000 × 2`.
- Every quantity below is per `tau`, over members, **one checkpoint per member per `tau`**. The five
  `tau` of one member share one outcome, so the five tests are dependent; §4's family bound does not
  assume otherwise.

### 3.1 The set

`rows, members, doc = tz14.the_set(manifests)` with `manifests = load_manifests()`, unchanged. It forms
the first 1,200 qualifying slots with `T0 > 1789206600` through `tz06.scoring_set` and asserts its own
five conditions. **Asserted here:** `tz07b.member_list_sha(members)` equals
`baa5a9d26855ea7ff07d062437df60617ba3e4e70dd74b3ac455a8a71a9b3154`, quoted from the TZ-14 report §2.1
and V5 and from map §2.3; `len(rows)` is `1296`, the units §2.1 of that report counts; and every member
`T0` is at most `1789595400`, the last member it names.

### 3.2 The pricer at each checkpoint

For each member, `walked = tz11a.walk_member(t0, manifests, False)`, then for each `tau` in `ADMITTED`
`full = tz11a.checkpoint_row(t0, "tz14set", tau, walked[tau])`, and the row kept is
`{k: full[k] for k in ("T0", "tau", "state", "sigma_hat", "admissible", "sd_student", "z_student",
"p_t", "label")}` — **the pricer row**. `label` is `None` there by `checkpoint_row`'s own body and stays
`None` until §3.6. Everything §3.3 and §3.4 derive is kept in separate records keyed by `(T0, tau)`,
never in the pricer row. `walk_member`'s body and the calls inside it assert, among other things, that
the grid is whole and that every kept anchor has a mean. **An `AssertionError` from it is BLOCKING**,
with the member and the message reported: every member of this set was walked without one by committed
code before — by TZ-11a as test 1 or test 2, or by TZ-13 as test 3 — so a failure now means something
under the pricer has changed.

**Asserted: the admissible count at each `tau` equals TZ-14's** — `631`, `628`, `615`, `619` and `621`
at `tau` 240 … 60, quoted from the TZ-14 report §2.2.

### 3.3 The quotes at each admitted checkpoint

For each member, `docs = tz14.documents(t0)` and `lines = tz14.quote_lines(config.interval_dir(t0))`.
For each read at a `tau` in `ADMITTED` whose `status` is `200` and whose `body_is_json` is true:
`book = tz14.book_of(read["raw"])`, then
`touch = tz14.touch_of(book, D(str(book["min_order_size"])), D(str(book["tick_size"])))` — the venue's
own minimum size and tick from the same reply, exactly as TZ-14 computed the touch it committed. The
read's side is `docs["tokens"][read["token_id"]]`, `Up` or `Down`. **A read that is not `200`, whose
`book_of` result has `ok` false, whose book lacks `min_order_size` or `tick_size` — `book_of` marks each
with a `_present` key — or that names a token outside the member's mapping is listed, counted and
contributes no touch — not BLOCKING.** TZ-14 found none of these in this set.

Per member per `tau`: `ask_up`, `bid_up`, `ask_dn`, `bid_dn` — each `touch["ask5"]` or
`touch["bid5"]` of that side's reply, a `Decimal` or `None`.

### 3.4 Eligibility, selection, and what the pricer claims — label-free

**Eligible at `tau`:** an admissible member at whose checkpoint `ask_up` or `ask_dn` exists. TZ-14
found no read empty on both sides, so eligibility is predicted to equal admissibility; it is counted,
not assumed.

**The edges, exact.** `p = D(repr(row["p_t"]))` — the float's shortest representation, taken exactly.
Where `ask_up` exists, `e_up = p − ask_up − tz14.fee_pp(ask_up)`; where `ask_dn` exists,
`e_dn = (1 − p) − ask_dn − tz14.fee_pp(ask_dn)`. A side whose ask does not exist has no edge. Every
edge is a `Decimal`; no float enters a comparison.

**Selected** where the larger existing edge is strictly positive. The side is `Up` where `e_up` exists
and is at least `e_dn` wherever `e_dn` exists, and `Down` otherwise; **a tie goes to `Up`**, and the count of
checkpoints where both edges are positive is reported. For a selected member: the price paid `a` —
`ask_up` or `ask_dn` — and `q = p` for `Up` or `1 − p` for `Down`, the probability `p_t` gives the side
bought. Buying `Down` at its ask is the executable form of selling `Up`, and it is the trade used here
because it is the trade a taker can place.

**Reported per `tau`, before any label exists:** the admissible, eligible and selected counts, the
selected by side and by weekday against weekend, and the count of selected trades priced at or below
`0.10`; the `Q` summary of `a` and of `q − a`, the edge `p_t` claims; the mean claimed edge
`Σ(q − a) / n` and the mean after-fee claim `Σ(q − a − fee(a)) / n`; and over eligible checkpoints
whose Up book is two-sided at the touch, the `Q` summary of `D = p − (bid_up + ask_up) / 2` and the
share at which `|p − 0.5| < |mid − 0.5|` — the market more confident than the pricer. The `Q` summary
is `tz14.q_summary` unchanged.

### 3.5 The gate's constants — exact, from the market's prices and `p_t` alone, on disk before any label

**The statistic.** For a selected member, `y = 1` where the side bought won — the label for `Up`, one
minus the label for `Down` — and `0` otherwise. **`S = Σ y`**, the number of selected trades that won,
over the `n` selected members at that `tau`. The gross profit per share is
`T = (S − Σ a) / n` and after the fee `T_fee = T − Σ fee(a) / n`; both are functions of `S` alone, so
the test on `S` is the test on either.

**The null — the market calibrated at its own ask:** each `y` is an independent coin with probability
`a`. **The alternative — the pricer right:** each `y` is an independent coin with probability `q`.
Under either, `S` is a sum of independent coins with known weights, and its distribution is computed
exactly by one recursion, `pb_upper(weights)`: the probability mass of the count after each coin is
the mass before it times `1 − w` plus the mass before it shifted by one, times `w`; the upper tails
`U(s) = P(S ≥ s)` for `s = 0 … n` are summed from the top. **All of it is `Decimal` at the 60 digits
`pfair.py` sets on import, and the coins are taken in ascending `T0`**, so the result is identical on
every run.

**At each `tau`:**

- `U0 = pb_upper([a ...])` and `U1 = pb_upper([q ...])`, over the selected members.
- **`s*`** is the smallest `s` in `0 … n` with `U0(s) <= 0.01`; where none exists, `s* = n + 1`, which
  no outcome can reach.
- **`FP = U0(s*)`** — the exact probability that a market calibrated at its ask reads EDGE — and `0`
  where `s* = n + 1`.
- **`POWER = U1(s*)`** — the exact probability of EDGE if the pricer is right — and `0` where
  `s* = n + 1`.
- **The projection**, barred from every reading: `s*` and `POWER` over the selected rows repeated two
  and three times, and the smallest of `1`, `2`, `3` at which `POWER >= 0.8`, or none.

These, with every selected member's `T0`, side, `a`, `q` and `fee(a)`, are written to
**`tz15-constants.json`** before §3.6 begins. The instrument asserts, between the write and the label
read, that every pricer row still carries `label is None`.

### 3.6 The labels, read once

Only when the run was started with `--score`. Before the read the instrument asserts that `HEAD` is
contained in `origin/tz-15-phase2-gate` — `git rev-parse HEAD` and `git branch -r --contains HEAD`,
each a fixed argument list with no shell — so no label is read by a commit that is not on `origin`
(map §7 items 54 and 63). Then **`tz10b.m2_labels(sorted(E))`**, where `E` is the union over `ADMITTED`
of the eligible members, is called once, and the instrument appends one line to
`/root/tz15-work/label-ledger.jsonl`: the UTC instant, `HEAD`, the member count and
`tz07b.member_list_sha(E)`.

A run started without `--score` stops after §3.5 with its constants on disk and reads no label.
**Every development run is such a run.**

### 3.7 The observed statistic, the reading, and what surrounds it

Per `tau`: `S`, `n`, `Σ a`, `Σ q`, `T`, `T_fee`, the win rate `S / n` beside the mean price paid and
the mean `q`, and §4's reading. **Where `n = 0` every ratio of this section is printed as undefined
and no unit leaves or joins any denominator; influence needs `n >= 2`, and the autocorrelation needs
three selected members and a `y` that is not constant, and each is printed as undefined otherwise**
(map §7 item 64).

**Influence** (map §7 item 27): with `x = y − a` per selected member, the member whose `|x − T|` is
largest — ties to the smallest `T0` — is removed; `S`, `s*`, `FP`, `POWER` and the reading are
recomputed exactly on the remaining `n − 1` and printed beside the value §4 reads. Recorded, not a
reading.

**Diagnostics, each barred from every reading:** over the eligible checkpoints whose Up book is
two-sided at the touch, the mean label, the mean market mid and the mean `p_t`, and the Brier score of
the mid and of `p_t`; and the lag-1 autocorrelation of `y` over the selected members in `T0` order,
which bears on §4's independence assumption and gates nothing.

### 3.8 A pre-registered prediction, barred from every gate and every reading

Written before any quote has been put beside a price. Each names its population.

| # | prediction | population |
|---|---|---|
| P1 | the eligible count equals the admissible count at every `tau` in `ADMITTED` | admissible members per `tau` |
| P2 | at `tau = 60` more than half of the selected trades are priced at or below `0.10` | selected members at 60 |
| P3 | at `tau = 60` the selected trades win less often than their prices implied: `S < Σ a` | selected members at 60 |
| P4 | no `tau` reads EDGE | the five readings |
| P5 | at least one `tau` reads NO EDGE — the gate has the power to decide somewhere | the five readings |

**The basis is written so the report can say which part failed.** TZ-13 put `λ̂` at `0.7436` at
`tau = 60`: the Student pricer's scale is too wide there, so it overprices long shots, and TZ-14 found
half of the admissible checkpoints at 60 one-sided — books where the only trade is the long shot. If
the market is calibrated, the pricer will buy long shots it overrates, and they will lose.

---

## 4. The gate

**Reading per `tau`, in this order:**

| condition | reading |
|---|---|
| `n = 0` | **UNDECIDABLE** — nothing was selected, so nothing is measured |
| `S >= s*` | **EDGE** — whatever `POWER` is |
| `S < s*` and `POWER >= 0.8` | **NO EDGE** |
| `S < s*` and `POWER < 0.8` | **UNDECIDABLE** |

This is CANON PART II's rule with the polarity of Phase 2: EDGE is the null rejected beyond a critical
count whose false-positive rate is exact, so it stands whatever the power; the power decides only
between NO EDGE and UNDECIDABLE. **The power floor is `0.8`, not `tz12.POWER_TO_PASS`'s `0.5`**,
because NO EDGE closes the question at that `tau`, and a coin-flip chance of missing the edge the
pricer itself claims is not a closing standard. The power is exact, so no simulation band applies.

**Family.** `FP <= 0.01` at each of five `tau`, so the probability of EDGE anywhere under the null is at
most `0.05` by Bonferroni, whatever the dependence between the five. The exact per-`tau` `FP` and their
sum are printed.

**The verdict:**

- **Any EDGE** — Phase 2 reads **YES at those `tau`, subject to confirmation.** The market's executable
  ask was cheaper than its outcomes, on the side the pricer chose, beyond what a calibrated market does
  one time in a hundred. **Phase 3 does not open on it.** A confirmation TZ applies this gate, with this
  selection rule and these thresholds unchanged, to the first `k × 1,200` qualifying slots with
  `T0 > 1789669800` — map §2.3's reserved span — where `k` is the projection's multiple at that `tau`.
- **NO EDGE at all five** — Phase 2 reads **NO for the Student pricer, inside its domain, at the five
  `tau`**: where it disagreed with the market by more than the fee, its side did not win more often
  than the market's own prices allowed, and the test had the power to see the edge the pricer claimed.
  It says nothing about any other pricer.
- **Otherwise** — the `tau` that read NO EDGE are closed; each UNDECIDABLE `tau` carries the
  projection's multiple, which is how much more capture a decision there costs.

**What the gate assumes, named.** The outcomes of different intervals are independent given the
market's prices. Adjacent 5-minute outcomes are increments of the oracle over disjoint windows, whose
only shared reading is the boundary average; §3.7's autocorrelation is printed so the assumption is
visible. **What the gate does not decide:** depth beyond `5` shares, the 50 ms taker delay and the
oracle basis — Phase 3's. `T_fee` is printed beside every reading as the first figure Phase 3 will
start from, and gates nothing here.

---

## 5. Implementation

### 5.1 The file, and the fixed order of the run

One new file, `research/tz15-phase2-gate.py`. It sets `OPENBLAS_NUM_THREADS`, `OMP_NUM_THREADS` and
`MKL_NUM_THREADS` to `"1"`, then loads **`tz14-quote-inventory.py`** once through an `importlib`
helper of the same shape as `tz11a._load`, and takes `tz12`, `tz11a`, `tz10b`, `tz07b`, `tz06`,
`pfair`, `config`, `D` and `load_manifests` from that one module object; `analyze` and `manifest` are
then imported by name. **Nothing is loaded a second time**, because `tz14` already loaded `tz12` and
everything below it (map §3). **The load has side effects this TZ names:** `tz14` writes the same three
environment variables and installs an audit hook that records the basename of every open under the
capture root for the life of the process; nothing can remove it, and this instrument does not read
`tz14.CAPTURE_OPENS`. **The instrument installs its own hook**, which records the absolute path, the
mode and the current step of §5.1 for every open under `config.ROOT`. It never calls `tz14.v1_gates`,
`tz14.selftests`, `tz14.build` or `tz14.main`.

**Functions, each with the contract named here:** `v1_gates` (§0.1), `pb_upper` (§3.5), `crit`
(§3.5), `edges` (§3.4), `select` (§3.4), `label_free` (§2 items 5 and 7), `reading` (§4), `the_rows`
(§3.2), `the_quotes` (§3.3), `constants` (§3.5), `projection` (§3.5), `labels` (§3.6), `observed`
(§3.7), `influence` (§3.7), `diagnostics` (§3.7), `v4_tz14` and `v4_tz13` (V4), `selftests` (§5.2),
`v2_static`, `v6`, `build`, `tables`, `csv_text`, `main`.

**The order of a run, and the instrument asserts it:**

0. `v1_gates`, §0.1;
1. host read 1, through `tz11a.host_read(when, t0s, floor)` at `tz11a.FLOOR_START_BYTES`, with `t0s`
   the empty set — it supplies the floor, the pid, the start record and the directory count;
2. the self-tests of §5.2, all seven, before anything is read from the capture, and then item 8's timed
   recursion, **the first fail-fast of §6**;
3. `v6` and the static half of `v2_static`;
4. the set, §3.1;
5. the rows, §3.2, and the admissible-count assertion; host read 2, over the members;
6. the quotes, §3.3, and **V4's comparison with TZ-14's observations**;
7. eligibility, selection and the label-free report, §3.4; **the first `label is None` assertion**;
8. the constants and the projection, §3.5, written to `tz15-constants.json`; **the second assertion**;
9. without `--score`: host read 3 and V9's assertions, and stop;
10. with `--score`: the push assertion and the label read, §3.6;
11. the observed statistic, the readings, the verdict, influence and diagnostics, §3.7 and §4;
12. V4's comparison with TZ-13's observations;
13. the tables, the disclosure and the observations file; host read 3 and V9's assertions.

### 5.2 Self-tests — seven items, run before the capture is touched, each an `assert`

1. **The exact tail against an independent enumeration.** `pb_upper([D("0.25"), D("0.5"),
   D("0.75"), D("0.5")])` has length `5` and equals `1`, `0.953125`, `0.703125`, `0.296875`,
   `0.046875` exactly. **Computed by the Architect by enumerating all sixteen outcomes in exact
   rational arithmetic** — an implementation that shares nothing with the recursion — as `64/64`,
   `61/64`, `45/64`, `19/64` and `3/64`, each a terminating decimal. Six assertions: the length and the
   five tails.
2. **The critical count against the binomial closed form.** Over twenty copies of `D("0.5")`,
   `crit(weights, D("0.01"))` returns `s* = 16` with `FP = 0.005908966064453125` exactly, and
   `pb_upper` at `15` is `0.020694732666015625`, above `0.01`. **Both computed by the Architect from
   `math.comb` in exact rationals** as `1549/262144` and `5425/262144`. Three assertions, three
   literals.
3. **The power against the binomial closed form.** Over twenty copies of `D("0.8")`, `pb_upper` at `16`
   is `0.62964826390266904576` exactly — **computed by the Architect as
   `Σ C(20, k) 0.8^k 0.2^(20−k)` for `k = 16 … 20` in exact rationals**, `60047937765376 / 5^20`, whose
   expansion terminates at the twentieth decimal. One assertion, one literal.
4. **The unreachable count.** Over three copies of `D("0.9")`, `pb_upper` at `3` is `0.729`, and
   `crit(weights, D("0.01"))` returns `s* = 4` with `FP = 0`. Three assertions, three literals, each
   exact by construction.
5. **Selection, exact, through `tz14.fee_pp`.** With `p` and the two asks: `(0.7, 0.60, 0.41)` selects
   `Up` at `0.60` with edge `Decimal("0.0832")`; `(0.605, 0.60, 0.41)` selects nothing;
   `(0.3, 0.41, 0.60)` selects `Down` at `0.60` with edge `Decimal("0.0832")`; `(0.7, None, 0.41)`
   selects nothing and raises nothing; `(0.5, 0.40, 0.40)` has both edges positive, selects `Up` by the
   tie rule, with edge `Decimal("0.0832")`. **Eleven assertions, exact by construction**, every edge
   compared as a `Decimal` value: `fee(0.60) = fee(0.40) = 0.0168` and `fee(0.41) = 0.016933`, and
   every edge follows by subtraction.
6. **The isolation guard.** `label_free` passes on two rows carrying only the allowed keys with
   `label` `None`, and raises on a row whose `label` is `1`, on a row carrying the key `Y` and on a row
   carrying the key `r`. Four assertions.
7. **The reading rule.** `reading(n=0, S=0, s_star=1, power=0)` is UNDECIDABLE;
   `reading(10, 8, 8, 0.1)` is EDGE; `reading(10, 7, 8, 0.85)` is NO EDGE; `reading(10, 7, 8, 0.79)` is
   UNDECIDABLE; `reading(10, 7, 8, 0.8)` is NO EDGE, the floor inclusive. Five assertions.

**Item 8 is a timing, not a test:** `pb_upper` over 1,200 fixed weights `D("0.37")` is timed once, and
§6's fail-fast reads it. It asserts nothing about the result.

**Thirty-three assertions over seven items: 6, 3, 1, 3, 11, 4, 5.**

### 5.3 The shape of the diff

**One new file and nothing else.** The list of committed lines the change replaces, read from
`origin/main`, is **empty**, and `git diff --name-only` against the merge base prints exactly
`research/tz15-phase2-gate.py`.

---

## 6. Cost

Every figure is taken at the **maximum** of the population it bounds (map §7 items 52 and 62): a
selected population at its unfiltered size, the 1,200 members.

| step | basis | seconds |
|---|---|---|
| gate, self-tests, `v6`, static `v2` | TZ-14 measured `6.3` and `7.0` for its own — its report §5.2 | ~15 |
| the set, §3.1 | TZ-14 measured `17.5` and `17.3` for these same 1,296 units — its report §5.2 | ~18 |
| the rows, §3.2 | TZ-12 measured `91.6` for `tz11a.walk_member` over 1,200 members, quoted in TZ-13 §6; 6,000 `checkpoint_row` calls at no more than 1 ms each | ~100 |
| the quotes, §3.3, and V4 against TZ-14 | TZ-14 measured `7.1` for 16,800 replies parsed up to three times — its report §5.2; here 12,000 once, and one 4.7 MB file compared | ~11 |
| the recursions, §3.5 and §3.7 | at `n = 1,200` per `tau`: two at `n`, two at `n − 1` for influence, two at `2n` and two at `3n` for the projection — `43,195,202` units of `n²` per `tau`, `215,976,010` over five. **Measured by the Architect on another machine at `2.153e-7` s per unit**, `0.31` s at `n = 1,200` and `2.64` s at `n = 3,600` | ~47 |
| the labels, V4 against TZ-13, tables, host reads | one small `json` open per labelled member; one 2.8 MB file | ~25 |
| **one scored run** | | **~216** |
| **the session: build, development runs without labels, two scored runs** | four runs at most, against `tz12.SESSION_CEILING_S` = `3,600` | **~870** |

**Fail-fast, both asserted, both derived from the table:**

1. Item 8 of §5.2 times one recursion over 1,200 weights, `t8`. The run projects the recursions at the
   upper bound as `215,976,010 × t8 / 1,440,000` and is BLOCKED if that exceeds **`950`** s — which
   admits a host up to `20` times slower than the Architect's machine:
   `215,976,010 × 2.153e-7 = 46.5` s, times `20` is `930`.
2. After §3.2 the run asserts its elapsed time is at most **`600`** s. The table puts it at about `133`
   s; the bound allows `4.5` times that, and it stops a run that would take two scored runs past the
   ceiling.

Nothing is sampled. No simulation is run: the constants are exact.

---

## 7. Validation

Each check states a count. **Asserted** means a Python `assert` or a `SystemExit` in the instrument
that produces the numbers, at the step of §5.1 named beside it; everything else is **recorded, not
asserted**.

| # | check | what it must produce |
|---|---|---|
| **V1** | gates — asserted, step 0 | 6 of 6 anchors; 21 of 21 `frozen` and 2 of 2 `tracked`; host 3 of 3 with the listing's instant; §0.6's refs; §0.7's two trees; the interpreter and `numpy` versions; every free-space read with its bound and whether it was asserted |
| **V2** | isolation — asserted two ways | **Static**, over the instrument's own tree, step 3: string constants scanned with docstrings exempt, and those carrying any of `tz14.BANNED_SUBSTRINGS` (**0** — the instrument matches against that committed tuple and writes none of the three itself); calls of the twelve `pfair` entry points of §2 item 6 (**0**); call sites of `tz10b.m2_labels` (**exactly 1**); calls of `analyze.venue` and `tz11a.fit_student` (**0**). **At run time**, from the instrument's own hook: opens whose basename carries `tz14.BANNED_SUBSTRINGS[0]` during steps 5 to 9 (**0**), and during step 10 exactly the number of members passed to `tz10b.m2_labels`; every pricer row carrying exactly §2 item 7's nine keys at steps 7 and 8, and `label is None` on every pricer row at both |
| **V3** | determinism — **BLOCKING on any difference, checked by `cmp` after the second scored run** — the one check here that is not an assertion inside a run, because it compares two | two runs with `--score` from fresh processes on the same pushed commit: `tz15-constants.json`, `tz15-readings.json`, `tz15-tables.md`, `tz15-observations.csv` and `tz15-disclosure.md` — none of which carries a clock reading — byte-identical by `cmp` and SHA-256 pairs, and `tz15-constants.json` also byte-identical to every run without `--score` on that commit. Wall clock and peak RSS per run. `tz15-run.json` holds instants and timings, is not compared, and is named |
| **V4** | the inputs are the committed ones — asserted | **(a)** the set's hash and its 1,296 units, step 4. **(b)** the admissible counts `631 / 628 / 615 / 619 / 621`, step 5. **(c)** step 6: a file under `/root/tz14-work/` whose SHA-256 is `0fc46a68f923acbbb6839a781d92d9b4d2c5afa734d059fa59b49b6e10df5e3a` — TZ-14's `observations.csv`, quoted from the TZ-14 report V11; its two runs left two identical copies and either is read — agrees at **12,000 of 12,000** admitted reads on `outcome`, `bid5`, `ask5`, `sigma_hat` and `admissible`, each of this run's values formatted by `tz14.cell` and compared with the string that file holds. **(d)** step 12: `/root/btc-forensics/tz13-work--run1--tz13-observations.csv` — the copy TZ-14's §9 made, named in its report §7.2 — asserted at SHA-256 `e78b01b5f06f485d15fe944fb37b17688507d278cb78add5143e12304a322f44` from the TZ-13 report V11; its members with `T0 <= 1789595400` are exactly this set's members with `T0 >= 1789428000`, and on those members at every `tau` in `ADMITTED`, `repr(p_t)` equals its `p_t` cell, and where a label was read here, the label equals its `label` cell |
| **V5** | the push precedes the label read — asserted, step 10 | `HEAD` in `origin/tz-15-phase2-gate` before the read; the push's completion instant from the Executor's own `git push` transcript beside the instrument's label-read instant; the ledger printed whole, and every line's commit equal to the reported one. A ledger line of any other commit is disclosed and explained |
| **V6** | the diff — asserted, step 3 | merge base and head; `git status --porcelain` for the two scoped paths; `git diff --name-only` naming one file; no attribute store, no `global`, no `nonlocal` in the file's own tree; the `os.environ` writes, exactly the three of §5.1; the replaced-line list, **empty** |
| **V7** | the self-tests — asserted, step 2 | 7 of 7 items and **33** assertions, distributed `6, 3, 1, 3, 11, 4, 5`; item 8's time; the output verbatim |
| **V8** | the frozen files are not moved — asserted, steps 0 and 13 | `research/pfair.py` and `research/tz14-quote-inventory.py` hash equal to map §0 at run start and at run end |
| **V9** | the capture is untouched — asserted, step 13, or step 9 in a run without `--score` | `tz11a.host_read` at steps 1, 5 and 13; between reads 1 and 3 the pid unchanged, the start record unchanged and the directory count not fallen; the read-set hash unchanged between reads 2 and 3 only. From the instrument's hook: every open under the capture root in mode `r` with no `w`, `x`, `a` or `+`; **no open of any file but `manifest.json` in a directory whose `T0` exceeds `1789669800`**; the count of opens per basename; and the enumeration of everything the instrument can write — the files of its `--out` directory and `/root/tz15-work/label-ledger.jsonl` |
| **V10** | the fingerprint table | every row of map §0 in lines, bytes and SHA-256, with the new file beside them as it stands on the branch |
| **V11** | disclosure | the 1,296 units in ascending `T0` with reasons; per `tau`, the eligible and the selected `T0` lists, each with its count and `tz07b.member_list_sha`; and the observations file — **one row per member per `tau` in `ADMITTED`**, carrying `T0`, `tau`, `sigma_hat`, `admissible`, `p_t`, `ask_up`, `bid_up`, `ask_dn`, `bid_dn`, `e_up`, `e_dn`, `selected`, `side`, `a`, `q`, `fee(a)`, the label and `y` — **sufficient to reconstruct every number of §3.4, §3.5 and §3.7 without re-running** |
| **V12** | influence and diagnostics — recorded | per `tau`, §3.7's influence line beside the reading; the diagnostics; §3.8's five predictions each marked held or refuted with the figure beside it |

**Causality is not re-tested and this is why.** `p_t` is `tz11a.checkpoint_row`'s own, which TZ-10b
V2 proved bit-identical under perturbation strictly after the checkpoint instant — 140 of 140 with 140
of 140 negative controls, map §4's TZ-10b row — and V4 (d) proves it equal, value for value, to what
TZ-13 computed. Every quote lands after its checkpoint: TZ-14 measured the offset positive at 16,800 of
16,800 reads, minimum `+39.6` ms — its report §2.4. The label is the one future quantity, and it
enters nothing before step 10.

---

## 8. The report

`CryptoReports/TZ-15-phase2-gate-report.md`, straight to `main` in one commit, immutable once
committed.

In this order: §0's gates, host, interpreter, refs, trees and every free-space read; §3.4's label-free
report per `tau`; §3.5's constants per `tau` — `n`, `s*`, `FP`, `POWER`, the projection — with the
instant `tz15-constants.json` was written; the instant of the push and the instant of the label read,
side by side; §3.7's statistic, influence and diagnostics; **§4's reading per `tau` and the verdict**,
naming for each UNDECIDABLE which condition left it there; §3.8's predictions; the implementation, the
file's hash on the branch and the commit; V1 … V12 with their counts; publication and §9; and every
point where the text needed a reading, with the workaround chosen.

The report states `wc -l` and `sha256sum` for the map and every file its fingerprint table lists. **A
report is evidence, not acceptance**: no reading of this TZ stands until the Architect has re-derived
`s*`, `FP` and `POWER` from the constants file and `S` from the observations file.

---

## 9. Retention

In this order, each step only after the previous one exited 0, and **only after both scored runs**:

1. **Copy first.** Every file under `/root/tz14-work/` whose SHA-256 is named by any committed report
   on `main` — matched against every hexadecimal token of 16 to 64 characters those reports print, the
   predicate TZ-14 used — and which `/root/btc-forensics/` does not already hold by hash, is copied
   there by exclusive create, the hash asserted at source and destination. Assert that every file
   already there — `205` at TZ-14's end — is unchanged. Report the counts before and after.
2. **Then the worktree**, `/root/tz14-work/wt`, `git worktree remove` without `--force`.
3. **Then the tree**, `rm -rf /root/tz14-work`, one command naming one tree, verified by `test -e`. If
   the session's classifier refuses it, hand the Boss one exact block and verify the outcome from
   `test -e` afterwards, never from his report (map §6).

`/root/tz15-work/`, the label ledger included, is the next TZ's to reclaim on the same terms. The
capture is never deleted.

---

## 10. Pre-send checks

Performed against this file, start to end, as a separate reading after its last section was written.
**The first reading found 24 defects in the draft's body and 3 in this section's own first draft;
a second full reading, made after this section was written, found 8 more in the body.** All were
repaired before the file was sent. Among them: a recursion count that omitted influence's alternative
tail, a file located as "the one" where two copies exist, a walk failure that was both "not BLOCKING"
and fatal to an asserted count, V3 called asserted with no step in the run, and §3.7's ratios given no
rule for an empty population. None of the second reading's eight moved a count or a threshold.

**C1 — scope against body.** Enumerated from §0 to §9 of the finished file: **5** repository paths,
**15** host paths and **44** committed entry points and module attributes written as `module.name`. Two of the
five repository paths are the ones §2 permits writing; `SYSTEM-MAP.md`, `research/pfair.py` and
`research/tz14-quote-inventory.py` are named as **read**, which prohibition 1 does not touch.
Intersections with §2's prohibition list that need an exemption: **6**, each written into §2 where the
prohibition is made — `/root/btc-forensics/` against item 3, for §9's copy; the report push against
item 4, named in item 2; `tz06.qualification` with `analyze.venue` inside it, `tz10b.m2_labels`, and
V4's read of TZ-13's observations file against item 5, three of the six in one item; and
`tz11a.checkpoint_row`'s internal link quantities against item 6. The twelve `pfair` entry points and
`tz11a.fit_student`, `tz14.v1_gates`, `tz14.selftests`, `tz14.build` and `tz14.main` are named only as
never called. `/var/lib/btc-recorder/**` meets item 2 and item 8 only as a read, and V9 carries both
proofs. The diff was performed, not intended.

**C2 — origin of every expectation.** **52** fixed numeric expectations in §5 and §7, counted literal
by literal, of CANON's two kinds. **32 computed by the Architect with an implementation independent of
the one under test:** 10 by exact rationals — the length-and-five-tails of self-test 1 by enumerating
sixteen outcomes, and `16`, `0.005908966064453125`, `0.020694732666015625` and `0.62964826390266904576`
of self-tests 2 and 3 from `math.comb` — each re-derived a second time in a separate computation
before this section was written; 8 by exact decimal arithmetic done by hand, `0.729`, `4` and `0` of
self-test 4 and the two prices `0.60` and three edges `0.0832` of self-test 5, re-derived in `Decimal`
beside the literals; and 14 counts that follow from this TZ's own text — V1's three host conditions,
V2's five zero-or-one call and open counts and nine keys, V4 (c)'s `12,000`, V6's one file, three
writes and empty list, and V7's `7`, `33` and six-part split. **20 quoted from committed artifacts,
named in place:** V1's six anchors and the `21` and `2` row counts from map §0; V4's member-list hash,
`1,296` and last member `1789595400` from the TZ-14 report §2.1, the five admissible counts from its
§2.2, the observations hash from its V11, the TZ-13 observations hash from that report's V11, and test
3's first member `1789428000` from map §2.3; and V9's `1789669800` from map §2.3. **The two §6
fail-fast bounds, `950` s and `600` s, are resource guards on wall-clock time**, inequalities that
assert no measured value. **None depends on a quantity this TZ measures**: §4's thresholds — `0.01`,
`0.8`, `n + 1` — are literals of this TZ, and every constant the gate reads is computed at run time
from prices and `p_t` and never compared with a figure written here.

**C3 — shape of every diff.** One new file, `research/tz15-phase2-gate.py`. The committed lines the
change replaces, read from `origin/main` at `93d13415b8f29cea6cc6626c86488676c6538dcf`: **none** — the
path does not exist there. C3's bar on the phrase for a non-empty list does not arise; §5.3 says
"empty".

**C4 — cost of every check.** §6 states every step at the maximum of its population: the 1,296 units
TZ-14 measured at `17.5` s; the 1,200 walks at TZ-12's measured `91.6` s; 12,000 replies against
TZ-14's measured `7.1` s for 16,800 parsed up to three times; and the recursions at the unfiltered
`n = 1,200`, counted as `43,195,202` units of `n²` per `tau` — two at `n`, two at `n − 1`, two at `2n`,
two at `3n` — `215,976,010` over five, at the Architect's measured `2.153e-7` s per unit. **~216 s per
scored run, ~870 s for the session**, against `3,600`. Both fail-fast bounds are derived beside their
figures: `215,976,010 × 2.153e-7 = 46.5` s, `× 20 = 930 ≤ 950`; and `15 + 18 + 100 = 133 ≤ 600`.
Nothing is sampled and nothing is simulated.

**C5 — every count.** Re-derived from the sets §3 defines, each beside its source, prose included (map
§7 item 66): `1,200` members from §3.1; `6,000` checkpoints as `1,200 × 5` and `12,000` reads as
`6,000 × 2`, §3.0, the latter again in V4 (c); `1,296` units from the TZ-14 report §2.1; the five
admissible counts from its §2.2; `21` `frozen`, `2` `tracked` and `1` `reported` rows counted by
parsing map §0 exactly as `tz14.fingerprint_rows` parses it; `6` anchors from map §0; the `12` `pfair`
entry points and the `9` allowed keys counted from §2 items 6 and 7; `5` conditions of `tz14.the_set`
counted from its body; `3` further link quantities of `tz11a.checkpoint_row` counted from its return
statement; `33` assertions as `6 + 3 + 1 + 3 + 11 + 4 + 5` from §5.2, the eleven of item 5 counted
case by case; `4` reading rows in §4's table; `5` predictions in §3.8; `205` files from map §3; `3`
host reads at steps 1, 5 and 13 of §5.1; and every row of §7 that says **asserted** names its step in
§5.1 — V3, which compares two runs, says instead that it is BLOCKING and checked by `cmp`.

**C6 — every population.** §3.2's admissible counts: the 1,200 members, per `tau`. §3.4's eligible
count: the admissible members; its selected count, by side and by calendar, and the `Q` summaries of
`a` and `q − a` and both means: **the selected members at that `tau`**; `D` and the confidence share:
the eligible members whose Up book is two-sided at the touch. §3.5's `U0`, `U1`, `s*`, `FP` and
`POWER`: the selected members at that `tau`; the projection: the same rows repeated twice and three
times. §3.7's `S`, `T`, `T_fee` and win rate: the selected members; influence: the selected members
less one; the Brier scores and means: the eligible two-sided checkpoints; the autocorrelation: the
selected members in `T0` order. §4's family bound: the five `tau`. V4 (c): the 12,000 admitted reads;
V4 (d): this set's members with `T0 >= 1789428000` at the five `tau`. §3.8: each prediction's third
column.

**C7 — every signature and every behaviour.** All **46** names this file writes as `module.name` — the
44 of §0 to §9 and `analyze.load_json` and `pfair.TAUS`, which this section cites — were read from
`origin/main` at `93d13415b8f29cea6cc6626c86488676c6538dcf`, and each one this TZ calls is quoted as
the file holds it: `tz14.the_set(manifests)`, whose body calls
`tz06.scoring_set(manifests, SET_NEED, after=SET_AFTER)`, asserts five conditions and returns
`rows, members, doc`, `rows` holding every unit considered; `tz11a.walk_member(t0, manifests, guard)`,
whose body returns a dict keyed by `pfair.TAUS` whose entries carry `priced`, `sigma_hat`, `Y` and `r`
and calls the tz07b cross-check only when `guard` is true; `tz11a.checkpoint_row(t0, name, tau, row)`,
whose return statement carries every one of §2 item 7's nine keys, `"label": None` among them, beside
`Y` and `r`; `tz14.quote_lines(dirpath)`, which returns `raw`; `tz14.book_of(raw)`, which returns early
with no `min_order_size` key when `ok` is false — the reason §3.3 tests `ok` first — and otherwise marks
each field with a `_present` key; `tz14.touch_of(book, min_size, tick)`, whose `ask5` is the lowest ask
with size at least `min_size`, independent of `tick`; `tz14.fee_pp(p)`, whose body is
`FEE_RATE * p * (D(1) - p)`; `tz14.documents(t0)`, whose `tokens` maps each id string to its outcome
string and is empty unless `outcomes` is exactly `Up` and `Down`; `tz14.cell(value)`, which gives `""`,
`"1"`/`"0"` or `str(value)`; `tz14.fingerprint_rows()`, which reads the map beside its own directory
and keeps five-cell rows whose state is `frozen`, `tracked` or `reported` — **run against this
revision's map it returns 21, 2 and 1, and every `frozen` hash equals `main`**; `tz10b.m2_labels(members)`,
which calls `venue(t0)` once per member, asserts each outcome and returns `1` or `0`;
`analyze.load_json`, one `open` per call, which V2's run-time count relies on;
`tz11a.host_read(when, t0s, floor)`, whose `read_set` covers only the `t0s` handed in — the reason V9
compares reads 2 and 3 alone; `tz07b.member_list_sha(members)`; `pfair.t_cdf`, whose body returns
`math.exp(...)`, a float, the reason §3.4 takes `D(repr(p_t))`; `tz14.BANNED_SUBSTRINGS`, whose first
entry is `"reso" + "lution"`; and the constants `tz11a.FLOOR_START_BYTES` `2060000000`,
`tz11a.FLOOR_BYTES` `2000000000`, `tz12.POWER_TO_PASS` `0.5` and `tz12.SESSION_CEILING_S` `3600`.
**The import itself is a behaviour and is quoted too:** `tz14`'s module body writes the three
environment variables, loads `tz12-sized-gate.py`, and calls `sys.addaudithook(_audit)`, whose hook
appends a basename, a mode and a caller to `CAPTURE_OPENS` and does nothing else.

**C8 — every cross-reference.** **28** resolved by reading the referenced text: CANON PART II's
sampling-rule and power clauses (§1, §4) and CANON §1.1's fee (§1); map §0 (§0.1, V1, V8, V10), §2.3
(§1, §2, §3.1, §4, V4, V9), §3 (§0.1, §0.7, §5.1, §9), §4 (§3.8, §7), §5 (§3.0) and §6 (§0.2, §0.4,
§9); map §7 items 27 (§3.7), 29 (§0.5), 49 (§1), 52 and 62 (§6), 54 and 63 (§3.6), 64 (§3.7) and 66
(§0.1); contract §4.1 (§2); the TZ-14 report §2.1 (§3.1, V4), §2.2 (§3.2, V4), §2.4 (§7), §5.2 (§6), §7.2
(V4) and V11 (V4); the TZ-13 report V11 (V4) and TZ-13 §6 (§6); and `tz12.POWER_TO_PASS` (§4) and
`tz12.SESSION_CEILING_S` (§6). Each supports the sentence that makes it.
