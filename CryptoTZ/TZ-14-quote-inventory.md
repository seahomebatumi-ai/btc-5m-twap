# TZ-14 — the quote inventory

**Canonical filename:** `TZ-14-quote-inventory.md`. The committed file takes this name and no other.

**Executor model: Opus.** First read of a capture no one has opened, a venue payload whose schema is
measured rather than assumed, clock arithmetic against the checkpoint grid, and multi-file diagnosis.

**Required System Map revision:** `2026-09-18-b`.

**Required anchors**, from map §0. A mismatch on any one is BLOCKED before any work:

| anchor | required |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-not-started` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` |
| `A6` — pricer | `729f0bcdbee3` |

---

## 0. Gates, host, interpreter, floor

**0.1 Fingerprint.** Read `SYSTEM-MAP.md` from `origin/main`. Its revision string must read
`2026-09-18-b` and its six anchors must equal the table above. Compute `wc -l`, `wc -c` and
`sha256sum` for every row of its §0 fingerprint table: the **20** `frozen` rows must equal the hashes
printed there, the **2** `tracked` rows are reported with no expectation, and `SYSTEM-MAP.md` itself
is reported. Any `frozen` mismatch is BLOCKED.

**0.2 Host gate**, all three or this is not the capture host and the run is BLOCKED:

- `/var/lib/btc-recorder/btc-updown-5m/` exists and holds interval directories; report the count and
  the first and last `T0`.
- A recorder process is running and the newest `runtime.jsonl` start record carries sha
  `4216c04673ced76b5b2ac60ef57c9abedc46f9b9`; report the pid and the `recv_ns`.
- The filesystem holding it is `/dev/vda2`, total `31,612,203,008` bytes.

**0.3 Interpreter.** Every command of the instrument runs on `/root/tz01-env/venv/bin/python` —
Python 3.12.x. Report the version. `import numpy` must succeed, because loading
`tz11a-student-link.py` imports it; if it fails the run is BLOCKED. The instrument itself computes
nothing in `numpy`. Scratch scripts that need only the standard library may run on the system
`python3`; none of them computes a measurement.

**0.4 Resource floor, in exact bytes, derived from map §6.** Free space on `/dev/vda2` at run start
must be at least `tz11a.FLOOR_START_BYTES` = `2,060,000,000`; every later read must be at least
`tz11a.FLOOR_BYTES` = `2,000,000,000`. Both are asserted, not compared by eye. Report every read with
its UTC instant, its reader and its bound.

**0.5 Preflight, twice, at least `1,800` s apart**, the first before the build and the second before
the first full run. Each records: `df -B1` on `/dev/vda2`; `du -sb /root/PROJECT_GAMING_PS5`; the
exit codes of `systemctl is-enabled telemetry-watch.service` and `systemctl is-active
telemetry-watch.service`. Report both, the elapsed seconds, and the implied bytes/day of each
quantity. **This run's own footprint — `/root/tz14-work` and `/root/.claude` — is stated separately at
both reads** (map §7 item 29). The preflight gates nothing beyond §0.4.

**0.6 The set must exist.** §3.1 forms the set by a count of qualifying units. If the capture does not
yet hold `1,200` qualifying slots with `T0 > 1789206600`, the run is **BLOCKED**, and the report
states the count reached, the number of units considered and the first and last `T0` examined. It is
not an error and no file is committed to `research/` in that case.

**0.7 The predecessor's tree.** `test -e /root/tz12-work` must print nothing and exit non-zero — map
§3 records that the Boss ran the handed removal block on 2026-09-18 and reported `GONE`, and this
verifies it from the filesystem rather than from his report. Report the result either way; a tree
still present is **not** BLOCKING and is reclaimed under §9 beside `/root/tz13-work/`.

**0.8 Refs.** Run `git ls-remote` against `origin` and report every ref it prints, before the branch
of §2 exists. Map §1 states the reading the Architect took on 2026-09-18: one branch, `main` at
`dad557d56f478d0bf6ec9e9b814030291b3f399c`. Report agreement or difference; a difference is recorded,
not BLOCKING, unless `main` no longer carries the revision §0.1 requires.

---

## 1. Why this TZ exists

Phase 2 is the decision point of this project, and it opens on an instrument that has never been
read. Tier C has stored fourteen order-book replies per interval since 2026-09-12 and **not one byte
has been opened by anything** (map §2.3). Nobody knows how many of those replies arrived, what a
reply contains, whether both sides of the book are quoted four minutes out, what the touch is worth
in size, or how far after its nominal checkpoint a read actually lands.

CANON PART II requires a Phase 2 gate to fix a threshold **and** a sampling rule before any score,
and — since revision `2026-09-18-a` — to state its false-failure probability and its power before any
reading it judges. None of that can be written against an unread capture. Writing it anyway is map §7
item 15's defect, committed at the one point in this project where it would be expensive: a gate
tuned to a market whose noise nobody has measured.

So Phase 2 is two TZs. **This one is the inventory**: it opens the capture, characterises it, and
computes **no statistic that is a function of both a quote and any pricer output**. It reads no
outcome into any printed number. Because it computes no score, Phase 2's sampling rule is still
correctable when the next TZ writes it, which is exactly what CANON PART II permits and what it stops
permitting the moment a score exists. **TZ-15 writes the gate and applies it once**, and is written
only after this report is on `main`.

That is TZ-12's position one phase later: TZ-12 read no label and computed no observed statistic of
any set, and TZ-13 then applied the gate it fixed. The pattern is the reason Phase 1's answer is
worth anything.

**This is not CANON hard rule 11's split, and the difference matters.** Rule 11 separates a
deployment from the measurement of what it produces, because wall-clock time has to pass between
them. Nothing is deployed here: Tier C has been writing since 2026-09-12 and the capture already
holds every byte this TZ reads, so both TZs could in principle run in one session. They are separated
for the other reason — that a gate written against an unread instrument is a gate written against a
guess.

**One thing this TZ must not be allowed to become.** A deviation between the market and `p_t` is not
evidence that the market is wrong. TZ-13 measured the Student pricer leaning under-confident at `tau`
90, 60 and 30, and map §4 states it plainly: a market quoting more confidently than `p_t` at those
`tau` is not, by that fact, mispricing. Nothing here is permitted to compare the two, so nothing here
can invite that reading.

---

## 2. Scope

**Repository paths this TZ may write, and no others:**

1. `research/tz14-quote-inventory.py` — new file, on branch `tz-14-quote-inventory`, then a pull
   request. Not merged by the Executor.
2. `CryptoReports/TZ-14-quote-inventory-report.md` — straight to `main`, in one commit, as contract
   §4.1 requires. **This is the one path this TZ pushes to `main`, and it is an exemption to item 4
   of the prohibitions below.**

**Prohibited, each absolutely:**

1. No committed file is modified. Every `frozen` row of map §0 is byte-identical at run end.
2. Nothing under `/var/lib/btc-recorder/` is created, written, moved or removed, and every file there
   is opened read-only. The recorder process is never signalled, stopped or restarted.
3. `/root/tz04a-env/`, `/root/tz01-env/` and `/root/btc-forensics/` are never removed or emptied.
   **Exemption:** §9 copies files *into* `/root/btc-forensics/` by exclusive create and removes
   nothing there.
4. Nothing is pushed to `main` except the report of item 2 above.
5. **No quantity that is a function of both a quote and any output of the pricer is computed,
   printed or written to disk.** **One exemption, named because §3.2 requires it:** `sigma_hat`,
   through which the frozen domain rule `pfair.ADMIT` partitions the members, so every figure below
   can be reported on the population Phase 2 will score. The admissibility flag is the **only**
   pricer-derived quantity any quote statistic is conditioned on, and it is a scale in USD/s, not a
   probability.
6. **No probability is computed anywhere in this TZ.** The instrument's own syntax tree contains no
   call of `pfair.p_fair`, `pfair.p_fair_student`, `pfair.state_and_sd`, `pfair.far_branch`,
   `pfair.near_branch`, `pfair.observations`, `pfair.corrected_sd`, `pfair.student_sd`,
   `pfair.phi`, `pfair.log_phi`, `pfair.t_cdf` or `pfair.log_t_cdf`, and V2 asserts the count is
   **0**. The `pfair` attributes it may name are exactly `merged_stream`, `reports`, `ADMIT`, `TAUS`,
   `GATED_TAUS`, `D`, `MS` and `config`; V2 asserts the set it names is a subset of those eight.
7. **No label enters any printed number.** A label is the venue's resolved outcome for an interval.
   **One exemption, named because the TZ's own body calls it:** `tz06.qualification`, which
   `tz06.scoring_set` calls for every unit considered, and `analyze.venue` inside it, which opens
   `resolution.json` and returns `price_to_beat` and `resolved_up` — the two values that decide
   membership. `tz10b.m2_labels` is **never called**, and `resolution.json` is opened by nothing else
   in this TZ. Neither value leaves the set formation: no table below is keyed, split or weighted by
   an outcome.
8. No fit is performed and no constant is produced. `tz11a.fit_student` is never called. Nothing this
   TZ measures becomes a literal in any file, a table, or a threshold in any later TZ without that
   TZ stating it and its origin itself.
9. No Release is created and no dataset, archive or binary enters git history.

---

## 3. The measurements

### 3.0 The two tau partitions, fixed here and used by every table below

- **`ADMITTED` = `(240, 180, 120, 90, 60)`** — the five `tau` Phase 1 did not disqualify inside the
  pricer's domain (map §5). Every table reports these first.
- **`OUTSIDE` = `(30, 10)`** — reported in the same tables, in a separately headed block, and
  **barred from supporting any Phase 2 or Phase 3 claim**. They cost nothing: the grid of §3.2 and
  the quote file of §3.3 already carry them.

`config.QUOTE_TAUS` must equal `pfair.TAUS` — the checkpoints the capture reads must be the
checkpoints the pricer prices, or nothing below is a comparison anyone can make later. Self-test 1
asserts it.

**The `Q` summary**, written once and meant everywhere below: the minimum, the quantiles at
`0.25 / 0.50 / 0.75 / 0.90 / 0.99` by the nearest-rank rule on the sorted values, and the maximum,
with the count the summary was taken over beside it. Where a quantity is reported "as the `Q`
summary", that is the whole of what is asked for.

**The row counts this TZ works in**, each re-derived in §7 from the set §3.1 defines: `1,200`
members; `8,400` checkpoints, `1,200 × 7`, of which `6,000` are at `ADMITTED`; and `16,800` reads at
full completeness, `1,200 × 7 × 2`. The last is an upper bound on what the capture can hold, not a
prediction that it does.

### 3.1 The set

**The first `1,200` qualifying slots with `T0 > 1789206600`**, formed by
`tz06.scoring_set(manifests, 1200, after=1789206600)` and by nothing else. Qualification is that
function's own committed rule and is not restated here (map §7 item 58: a count of qualifying units
is produced only by the committed set-formation code, named by function).

`1789206600` is chosen so the walk opens at the earliest interval directory with a larger `T0`, which
is **`1789206900`** — the first unit TZ-05a considered, quoted from map §2.3's read table, and the
first interval whose `tau = 240` checkpoint falls at or after the Tier C restart on `4216c04`.
**`quotes_complete` is not a membership condition and must not become one:** the rate at which the
quote capture is complete is the first thing this TZ measures, and a set that filtered on it would
measure nothing.

Asserted: the returned `ok` is `True`; the first member's `T0` is at least `1789206900`; every member
sits on the 300 s grid; the member list is strictly increasing. Reported: the number of units
considered, the members, every non-member with its reasons, the member-list SHA-256 through
`tz07b.member_list_sha`, the first and last member as epochs and as UTC, the span in days, and the
count of members per UTC weekday. **The set is expected to open on a Saturday** — map §2.3 puts
`1789206900` at 2026-09-12 09:55 UTC — **so it is the first scored set in this project to contain a
weekend by construction**, which is why the weekday composition is reported and why every per-`tau`
table below is also broken out weekday against weekend.

### 3.2 The domain, from the pricer's scale and nothing else

For each member: `s3 = pfair.merged_stream(t0, config.S3_STREAM)`, `grid = tz10b.grid_of(s3, t0)`,
and `sigma_hat = tz10b.sigma_hat_of(grid, tau)` at each of `pfair.TAUS`. These three calls are the
whole of this TZ's use of the pricer. The instrument assembles `{t0: {tau: {"sigma_hat": …}}}` and
obtains the admissible member lists from **`tz11a.admissible_members(walked, members, admit)`**
unchanged, at `admit = pfair.ADMIT` — the committed implementation of the domain rule, reused rather
than rewritten.

**`tz10b.grid_of` carries a precondition and this TZ states what happens when it fails.** Its body
asserts `len(grid) == GRID_POINTS and all(v is not None for v in grid)` — the one-second grid over
`[T0 − 300, T0 + 300]` must be whole — and raises otherwise. The committed set rule admits a member on
its manifest and on two `chainlink` reports, not on a whole grid, so the two can disagree. A member
that raises is **caught, listed by `T0`, counted, and excluded from this section's tables and from
nothing else**: its quote rows are read and reported exactly like any other member's. It is not
BLOCKING and no set is re-formed, because this TZ scores nothing and §3.2's population is disclosed
member by member.

Reported per `tau`: the admissible count, the share of members whose grid was whole, and the same
split weekday against weekend. **No floor and no minimum:** an inventory has nothing to fail. If a `tau`'s admissible
population is small the figure is the finding, and map §7 item 51's rule — that a filtered population
too small to support a statistic reads UNDECIDABLE — applies to the gate TZ-15 writes, not here.

### 3.3 The quote file, read for the first time

For each member, the instrument reads `quotes.jsonl.gz` — located exactly as the recorder's own
reader locates it, through `manifest._stream_path(dirpath, config.QUOTES_STEM)`, which prefers the
`.gz` and falls back to the plain `.jsonl` — and parses each line as the recorder wrote it:
`recv_ns`, `mono_ns`, `tau`, `token_id`, `status`, `raw`, and `error` where a read produced no reply.

**The integrity view is cross-checked against the committed reader.** The instrument calls
`manifest._quote_reads(dirpath)` on the same directory and asserts that the multiset of
`(tau, token_id, status, body_is_json)` it returns equals the instrument's own, member by member. The
instrument's reader exists only because `_quote_reads` discards `raw`; on every field both produce,
they must agree, and a disagreement is BLOCKING.

Reported over the `1,200` members:

1. Members with no quote file at all, with their `T0` listed.
2. The distribution of read lines per member: the count at each value from 0 to 14, and every member
   above 14 listed by `T0`. A member above 14 is a duplicate, which the recorder's append-mode write
   permits across a restart and which nothing has ever checked.
3. Duplicate `(tau, token_id)` pairs within a member: the count of members carrying any, and the
   count of pairs.
4. Lines that fail to parse, by member.
5. `status` as a histogram over the whole population, `null` included, with the `error` strings of
   the null rows grouped by their text and counted.
6. `body_is_json` false among `status == 200`.
7. `manifest.json`'s own `quotes_complete` against the instrument's recomputation of the same
   predicate from the same fields: the agreement count, and every disagreement listed.
8. The count of members whose window holds more than one recorder start record, from
   `manifest.json`'s `recorder_git_sha` being a list rather than a string, beside items 2 and 3.

### 3.4 The read geometry

Per read, `offset_ms = (recv_ns − config.quote_checkpoint_epoch(t0, tau) · 10⁹) / 10⁶`, asserted
equal to the value the member's `manifest.json` already carries in `quote_offsets_ms` for the same
`(tau, token_id, status)`. **A value disagreement, where both sides exist, is BLOCKING** — it is the
one place this TZ can discover that the manifest and the file disagree about what was captured. **A
member whose `manifest.json` carries no `quote_offsets_ms` key at all is listed, excluded from this
comparison with its reason, counted, and is not BLOCKING**: map §7 item 17 records that a manifest
written under an older schema is never compared against a rebuild under today's, and the key was
introduced by TZ-05a on the same commit that started Tier C.

Reported per `tau`, over the reads at that `tau`: the `Q` summary of `offset_ms`, the count negative,
the count above `1,000` ms and the count above `8,000` ms — `8,000` ms being `QUOTE_TIMEOUT_S × 1,000`,
and `QUOTE_TIMEOUT_S` is `8`, in seconds, in `research/recorder/recorder.py` as committed. Reported per
checkpoint: the `Q` summary of the absolute difference between the two tokens' `recv_ns`, which is how
far apart the two halves of one pair were actually read.

Reported per member: `manifest.json`'s `clock_offset_abs_max_ms`, the count of members above
`config.CLOCK_OFFSET_LIMIT_MS` = `50.0`, and the maximum over the set. Map §6 puts the worst measured
offset at `18.789` ms over the TZ-05a window; this is the first reading of it over 1,200 intervals,
and it bounds every latency claim Phase 3 will want to make.

**The direction matters and is stated here so no later TZ has to re-derive it.** A read is issued at
the checkpoint and its reply lands after it, so `offset_ms` is expected positive and the quote
carries information at least as new as the pricer's own checkpoint reading. That direction is
conservative for any future claim of an edge and adverse for none; the count of negative offsets is
reported because a negative one would mean the opposite, and would be a finding.

### 3.5 The book, measured and not assumed

Every `status == 200` body is parsed with `json.loads` and every price and size is carried in
`decimal.Decimal` from its string, never through a float (map §6: `decimal.Decimal` at 60 digits for
every price). **Nothing about the payload's shape is assumed.** Reported:

1. **The key set of the top-level object**, as a histogram of sorted key tuples with counts. Every
   distinct shape is listed, with one example `T0` and `tau` each.
2. **Per side**, `bids` and `asks`: the level count distribution, and the observed ordering —
   ascending by price, descending, or neither — as three counts per side. **The best price is taken
   as `max` over `bids` and `min` over `asks` and never from position `0`**, so the ordering is a
   measurement and not a dependency. Self-test 2 fixes that.
3. Empty sides: the count with no `bids`, with no `asks`, and with neither, per `tau`.
4. Best bid, best ask and the mid, per read; the spread `ask − bid` in probability points, reported
   per `tau` as the `Q` summary.
5. **Crossed or locked books:** the count with `best_bid >= best_ask`, listed by `T0` and `tau`.
6. Whether the reply carries `tick_size`, `min_order_size`, `timestamp`, `hash`, `market` and
   `asset_id`: present/absent counts for each, and for each present the distinct values with counts.
   Where `asset_id` is present, the count where it differs from the `token_id` the recorder
   requested, listed.
7. Where `tick_size` is present, the spread in ticks. Where it is absent, the spread in ticks is
   computed at `0.01`, **named in the table as carried from map §6's TZ-05a measurement and not
   measured here.**
8. Where `timestamp` is present, `recv_ns / 10⁶ − timestamp` in milliseconds — the venue's stated
   instant against ours — reported per `tau` as the `Q` summary, with the count negative and the unit
   the field was read in stated. This is the time basis Phase 3 needs and no one has read.

### 3.6 Executability

The size that can actually be taken, at the venue's own minimum order size. `MIN_SIZE` is taken from
the reply's `min_order_size` where §3.5 item 6 finds it present in **every** read of the population,
and otherwise from map §6's TZ-05a measurement, `5`; the table names which of the two was used and
the report states the count each way. Reported per `tau`, over the reads of §3.5:

1. `bid5` — the highest bid price whose size at that price is at least `MIN_SIZE` — and `ask5`, the
   lowest such ask. The count where either does not exist.
2. The **executable band** `[bid5, ask5]` and its width in probability points, as the `Q` summary.
3. **Cumulative size within `k` ticks of the executable touch**, defined exactly: for bids, the sum of
   the sizes of every level whose price is at or above `bid5 − k · tick`; for asks, at or below
   `ask5 + k · tick`; at `k = 0, 1, 2, 5`. Reported per side per `tau` as the `Q` summary, in shares.
4. The taker fee in probability points at each of `bid5` and `ask5`, from CANON §1.1's
   `fee = shares × 0.07 × p × (1 − p)`, evaluated in `Decimal`. Self-test 4 fixes it against CANON's
   own three published points.
5. **The round-trip cost**, `(ask5 − bid5) + fee(ask5) + fee(bid5)`, in probability points: the `Q`
   summary, per `tau`, weekday against weekend, admissible against not. **This is the single
   number that decides whether a Phase 3 can exist**, it is a function of the quotes alone, and it is
   reported here rather than asserted against anything.

### 3.7 The two tokens

Per checkpoint where both token ids returned `200` with a parseable body, all quantities in
probability points:

1. `best_bid_up + best_bid_down` and `best_ask_up + best_ask_down`: the `Q` summary per `tau`,
   and the counts of `bid_up + bid_down > 1` and `ask_up + ask_down < 1`, each listed by `T0` and
   `tau` where the count is at most 50 and summarised above that. Both are free lunches if they are
   executable, and item 5 below says whether they are.
2. `mid_up − (1 − mid_down)`: the two books' disagreement about the same probability.
3. The same two sums at the executable touch, `bid5` and `ask5`, which is the executable form of
   item 1.
4. The `outcomes` and `clobTokenIds` arrays of the member's `gamma.json`, read as the recorder reads
   them — `clobTokenIds` parsed as JSON, index by index against `outcomes`. Reported: the distinct
   `outcomes` arrays with counts. **The Up token is `clobTokenIds[i]` where `outcomes[i] == "Up"`**,
   which is the same string `analyze.venue` turns into `resolved_up` and which TZ-04b validated at
   200 of 200; no settled document is opened to establish it. A member whose `outcomes` is not a
   two-element array containing exactly `Up` and `Down` is **listed, excluded from the tables of
   items 1 to 3 and from §3.5's per-token breakdown, and counted** — never dropped silently and never
   guessed at by position.
5. Where a sum in item 3 is a free lunch, the size available at both touches and the profit in
   probability points after both taker fees, listed per occurrence.

### 3.8 The market document

From each member's `gamma.json`, present/absent counts and distinct values for: `orderPriceMinTickSize`,
any key matching `fee` case-insensitively, any key matching `reward` case-insensitively, `outcomes`,
`clobTokenIds`, `outcomePrices`, `closed`. Map §4 records that TZ-07a V9 found the `rewards` key
absent entirely from all 400 `gamma.json` documents it read — not null, not empty — and that whether
that is the endpoint, the query or the venue is unknown and uninvestigated. This repeats that read
over 1,200 documents and over the three further keys Phase 3 will need, and reports what it finds.
**No assumption rests on the answer in this TZ.**

### 3.9 A pre-registered prediction, barred from every gate and every reading

Written before any quote is opened, so the report can state which of these the data refutes. Each is
a statement about a statistic §3 already defines, over the population named. **Nothing in §7 reads
this section**, and no figure in it is an expectation any check asserts.

| # | prediction | population |
|---|---|---|
| P1 | `quotes_complete` holds for at least `90%` of members | the 1,200 |
| P2 | at every `tau` in `ADMITTED`, both sides of the Up book are non-empty in at least `95%` of `200` reads | reads per `tau` |
| P3 | the median executable band `ask5 − bid5` is between `1.0` and `4.0` probability points at every `tau` in `ADMITTED` | reads per `tau` |
| P4 | the median round-trip cost of §3.6 item 5 exceeds `3.5` probability points at every `tau` in `ADMITTED` | reads per `tau` |
| P5 | `bid_up + bid_down <= 1` at no fewer than `99.5%` of paired checkpoints | paired checkpoints |
| P6 | the median `offset_ms` is under `500` ms at every `tau`, and the `0.99` quantile under `1,000` ms | reads per `tau` |
| P7 | `timestamp` is present in at least `99%` of `200` replies, and the median of §3.5 item 8 is under `2,000` ms | reads per `tau` |

**P4 is the one that matters.** If it holds, a deviation between the market and `p_t` must exceed
about four probability points before it is worth anything after costs, and TZ-15's gate has to be
powered against that alternative rather than against a deviation of any size. If it fails, the
opposite. Either way the number is a fact about the venue and not about the pricer.

---

## 4. What this TZ does not decide

**There is no gate here, and that is deliberate.** Phases 0 and 1 could only disqualify; this TZ
cannot even do that. It admits nothing, closes nothing, and no reading in it is evidence that the
market is or is not mispriced — it computes no comparison that could bear on the question.

CANON PART II's requirement that Phase 2's gate fix a threshold and a sampling rule before any score,
with a stated false-failure probability and a stated power, falls on **TZ-15**, which is written once
this report is on `main` and applied once thereafter. Because nothing here scores the market against
the pricer, that sampling rule is still correctable when TZ-15 fixes it, and it stops being
correctable the moment TZ-15's first score exists.

**What TZ-15 will take from this report**, and the reason each figure above is asked for: the
completeness rate and the duplicate count, which decide the set rule; the admissible counts per
`tau`, which decide which `tau` can carry a powered gate at all; the read offsets, which decide
whether the quote and the pricer's checkpoint are close enough in time to be compared; the band width
and the round-trip cost, which fix the alternative the gate must have power against; and the
two-token consistency, which decides whether the Up book alone is the observation or both books are.

---

## 5. Implementation

### 5.1 The file, and the fixed order of the run

One new file, `research/tz14-quote-inventory.py`. It loads **`tz12-sized-gate.py`** once through an
`importlib` helper of the same shape as `tz11a._load`, and takes `tz11a`, `tz10b`, `tz07b`, `tz06`,
`pfair`, `config`, `D` and `load_manifests` from that one module object — the pattern TZ-13 §5.1 uses
and for its reason: TZ-12's instrument loads TZ-11a's, which loads TZ-10b's, which loads the other
three, so **loading any of them a second time would be two module objects with two copies of every
table**. `tz12` is loaded because §5.2 item 5 reads `tz12.TEST2_SHA256` and §6 reads
`tz12.SESSION_CEILING_S`; nothing else in this TZ calls it. `analyze` and `manifest` are then imported
by name, which works because `pfair.py` has already put `research/recorder/` on `sys.path`. The
instrument sets `OPENBLAS_NUM_THREADS`, `OMP_NUM_THREADS` and `MKL_NUM_THREADS` to `"1"` before that
load, because the chain imports `numpy`, and writes no other environment variable.

**Functions, each with the contract named here:** `the_set` (§3.1), `domain` (§3.2), `quote_lines`
(§3.3), `integrity` (§3.3), `geometry` (§3.4), `book_of` (§3.5), `best_of` (§3.5 item 2),
`touch_of` (§3.6 items 1–3), `fee_pp` (§3.6 item 4), `round_trip` (§3.6 item 5), `pairs` (§3.7),
`documents` (§3.7 item 4 and §3.8), `selftests` (§5.2), `v2_static`, `v6`, `build`, `tables`,
`csv_text`, `main`.

**The order of a full run, and the instrument asserts it:**

1. host read 1, at the `tz11a.FLOOR_START_BYTES` floor, through `tz11a.host_read(when, t0s, floor)`,
   **with `t0s` the empty set**, because §3.1's set does not exist yet. It supplies the floor, the
   recorder pid, the newest start record and the interval-directory count; its `read_set` hash is over
   nothing and V9 never compares it;
2. self-tests, §5.2, all six before anything is read from the capture;
3. `v6` and the static half of `v2_static`, over the instrument's own syntax tree;
4. the set, §3.1, with every assertion of that section;
5. the grids and the domain, §3.2; host read 2, now over the member set;
6. **the quote probe:** the first `20` members of §3.3 and §3.4 only, timed, with §6's fail-fast
   asserted before anything else is read;
7. §3.3 and §3.4 over the remaining members, with the manifest cross-checks of both sections;
8. §3.5, §3.6 and §3.7 over the parsed bodies; §3.7 item 4 and §3.8 over the `gamma.json` documents;
9. the tables, the disclosure and the observations file;
10. host read 3, and V9's four assertions between read 1 and read 3.

### 5.2 Self-tests — six items, run before the capture is touched, each an `assert`

1. **The checkpoint grid the capture and the pricer share.** `config.QUOTE_TAUS == pfair.TAUS`, one
   assertion. Then `config.quote_checkpoint_epoch(1789206900, tau)` at the seven `tau` equals
   `1789206960`, `1789207020`, `1789207080`, `1789207110`, `1789207140`, `1789207170`, `1789207190`.
   **The seven literals were computed by the Architect as `t0 + 300 − tau` and cross-checked against
   the `t` values `config.py`'s own docstring states — `{60, 120, 180, 210, 240, 270, 290}` — quoted
   from `research/recorder/config.py` as committed.** Eight assertions, seven literals.
2. **The best price does not depend on order.** Three synthetic books carrying the same four bid
   levels `0.49 / 0.50 / 0.51 / 0.52` and the same three ask levels `0.53 / 0.54 / 0.55` — ascending,
   descending, and shuffled to a fixed order written in the test — plus a fourth holding one level a
   side, `0.52` and `0.53`. `best_of` returns `0.52` for the bid and `0.53` for the ask on all four,
   which is eight assertions. On a book with `bids: []` it returns `None` for the bid and `0.53` for
   the ask, and on `asks: []` `0.52` and `None`: four more. **Twelve assertions, two numeric literals
   — `0.52` and `0.53` — and two `None`s, all exact by construction**, every numeric one compared as
   `Decimal`.
3. **The executable touch skips size below the minimum.** One synthetic book,
   `bids [{"0.52","3"}, {"0.51","10"}, {"0.50","2"}]` and `asks [{"0.53","4"}, {"0.54","9"}]`, at
   `MIN_SIZE = 5` and `tick = 0.01`: `best_of` gives `0.52` and `0.53`; `touch_of` gives
   `bid5 = 0.51` and `ask5 = 0.54`; the band `ask5 − bid5` is exactly `Decimal("0.03")`; and §3.6
   item 3's cumulative bid size at `k = 1`, the sum over levels priced at or above
   `bid5 − 1 · tick = 0.50`, is exactly `12` — `10` plus `2`, the `0.52` level excluded because it is
   above `bid5`. **Six assertions, six literals, exact by construction.** The band is compared for
   equality rather than within a tolerance, which holds only if no float touched it.
4. **The fee in probability points.** `fee_pp(p) = D("0.07") * p * (1 - p)` at `p` of `0.50`, `0.85`
   and `0.90` equals `D("0.0175")`, `D("0.008925")` and `D("0.0063")` exactly. **Quoted from CANON
   §1.1, which publishes the same three as `1.75`, `0.89` and `0.63` probability points, and computed
   independently by the Architect in exact decimal arithmetic**, agreeing at every digit CANON
   prints. Three assertions, three literals, each exact.
5. **The set-formation call shape.** `tz06.scoring_set(manifests, 400, after=1789296300)` produces a
   member list whose `tz07b.member_list_sha` equals `tz12.TEST2_SHA256`. **Quoted from a committed
   artifact:** that constant is in `research/tz12-sized-gate.py` and the same value is stated in
   TZ-11a's report §1.0 and in map §2.3. This proves the positional `need` and keyword-only `after`
   call shape before §3.1 uses it. **One assertion, one literal**, and the constant is read from the
   single `tz12` module object §5.1 already loaded — nothing is loaded a second time for it.
6. **The instrument's reader agrees with the committed one.** In `/root/tz14-work/selftest/`, and
   nowhere near the capture, the instrument writes one directory holding a `quotes.jsonl` of four
   lines it composes itself: two `status` `200` rows with one-level books, one `status` `503` row,
   and one line truncated mid-object. `manifest._quote_reads(dirpath)` and the instrument's
   `quote_lines(dirpath)` return the same multiset of `(tau, token_id, status, body_is_json)` — three
   entries, the torn line counted by neither — and the instrument's reader additionally returns the
   two raw bodies unchanged, byte for byte, asserted against the strings it wrote. The assertions are:
   the two multisets equal; the entry count is `3`; the `body_is_json` pattern is `true, true, false`
   in `recv_ns` order; the two raw bodies equal the strings written; and `test -e` on the directory
   fails after the test removes it. **Six assertions, one numeric literal — the entry count `3` — the
   rest exact by construction.** The directory's path is named in V9's enumeration of everything the
   instrument can write.

### 5.3 The shape of the diff

**One new file and nothing else.** No committed line is replaced: the list of replaced lines, read
from `origin/main`, is **empty**, so the diff is additive in the strict sense and `git diff
--name-only` against the merge base prints exactly `research/tz14-quote-inventory.py`.

---

## 6. Cost

Every figure is taken at the **maximum** of the population it bounds, never at a predicted share
(map §7 items 52 and 62), and the fail-fast is derived term by term from the same figures.

| step | basis | seconds |
|---|---|---|
| self-tests, `v6`, static `v2` | TZ-12 measured `6.1` for six self-tests | ~15 |
| set formation, §3.1 | TZ-12 measured `23.3` s for three formations over ~1,320 considered units = `0.0177` s per unit, at the walk's own upper bound of `2,200` units considered | ~50 |
| grids and `sigma_hat`, §3.2, 1,200 members | TZ-12 measured `91.6` s for `tz11a.walk_member` over 1,200 members; this TZ's per-member job is a strict subset of that call — the same `merged_stream`, the same `grid_of`, the same seven `sigma_hat_of`, without the anchor loop, without `tz07b.residual` and without the guard | ~92 |
| §3.3 – §3.8, 1,200 members × 14 replies | **unmeasured — nothing has opened a quote file.** Bounded by the enforced probe below, `0.200` s per member | ~240 |
| tables, disclosure, observations file | — | ~40 |
| three host reads, `read_set` over ~10,800 directory entries each | — | ~5 |
| **one full run** | | **~442** |
| **the session: build plus two full runs** | against `tz12.SESSION_CEILING_S` = `3,600` | **~950** |

**Fail-fast, asserted, both derived from the table:**

1. The probe of §5.1 step 6 — the first `20` members through §3.3 and §3.4 — is timed. If it exceeds
   **`4.0` s** the run is BLOCKED. `4.0 / 20 = 0.200` s per member; at 14 replies whose mean raw size
   map §6 puts at `61,896.5 / 14 = 4,421` bytes, that is `0.0143` s per reply, about `310` KB/s of
   JSON parsing — two orders of magnitude below what CPython does, so a breach means the file is not
   what this TZ thinks it is, not that the arithmetic was optimistic.
2. After §3.2, the run projects `elapsed + 1,200 / 20 × t_probe + 40` s and is BLOCKED if that
   exceeds **`1,200`** s. At the table's own figures that projection is `157 + 240 + 40 = 437` s, so
   the bound leaves a factor of `2.7` and still stops a run that would approach the `3,600` s ceiling
   across two runs.

Nothing here is sampled: §5.2 item 6's synthetic directory is a self-test, and the probe of item 1 is
a guard whose members are read again in full at step 7.

---

## 7. Validation

Each check states a count. Everything called **asserted** is a Python `assert` or a `SystemExit` in
the instrument that produces the numbers; everything else is **recorded, not asserted**.

| # | check | what it must produce |
|---|---|---|
| **V1** | gates — asserted | 6 of 6 anchors; 20 of 20 `frozen` rows and 2 of 2 `tracked`; host 3 of 3; §0.7's `test -e` result and §0.8's refs; the interpreter and its `numpy` version; every free-space read with its bound, and how many were asserted |
| **V2** | isolation — asserted two ways | **Static**, over the instrument's own syntax tree: the count of string constants scanned with docstrings exempt, the count carrying any of `resolution`, `resolved_up`, `priceToBeat` (**0**), the count of calls scanned, the count of calls of the twelve `pfair` probability entry points §2 item 6 names (**0**), the count of calls of `tz10b.m2_labels`, `tz11a.walk_member` and `tz11a.fit_student` (**0**), and the set of `pfair` attributes named, asserted a subset of the eight §2 item 6 allows. **At run time:** the count of opens of `resolution.json` by this instrument (**0**) |
| **V3** | determinism — asserted | two full runs from fresh processes on the same commit; the deterministic outputs byte-identical, by `cmp` and by SHA-256 pairs. Wall clock and peak RSS per run, reported. A file holding a clock reading or a timing is not compared and is named |
| **V4** | the instrument reproduces what is committed — asserted | `manifest._quote_reads` against `quote_lines` on **1,200 of 1,200** members, the multiset equal at every one (§3.3); `quote_offsets_ms` against the recomputed offsets at every read (§3.4); `manifest.json`'s `quotes_complete` against the recomputed predicate at every member, agreement count reported and every disagreement listed |
| **V5** | set identity — asserted | the member-list SHA-256 through `tz07b.member_list_sha`; `ok` is `True`; 1,200 members, strictly increasing, all on the 300 s grid, first at or after `1789206900`; the units considered; the four committed member-list hashes of map §2.3 are **not** recomputed and no committed set is re-formed, because this TZ scores none of them |
| **V6** | the diff — asserted | merge base and head; `git status --porcelain` for the two scoped paths; `git diff --name-only` naming one file; no attribute store, no `global`, no `nonlocal`; the `os.environ` writes, exactly the three of §5.1; the replaced-line list, **empty** |
| **V7** | the self-tests — asserted | 6 of 6 items, their assertion counts — **8, 12, 6, 3, 1, 6 = 36** — and their output verbatim |
| **V8** | the frozen literals are not moved — asserted | `research/pfair.py` hashes equal to map §0 at run start and at run end; `pfair.ADMIT` printed as read, at 7 of 7 `tau`. **`LINK_NU` and `LINK_SCALE` are neither read nor printed**: this TZ computes no probability, so the link tables have no place in it, and §2 item 6's allowed attribute set does not contain them |
| **V9** | the capture is untouched — asserted | `tz11a.host_read` at run start, after the domain and at run end. Three assertions between read 1 and read 3 — the recorder pid unchanged, the newest start record unchanged, the interval count not fallen — and a fourth, **the read-set hash unchanged, between read 2 and read 3 only**, because those two are over the same member set and read 1 is over the empty set (§5.1 step 1). The read set, its directory and file counts. Plus the enumeration of everything the instrument can write, `/root/tz14-work/selftest/` included, and the proof that every open under `/var/lib/btc-recorder/` is read-only — by enumerating every call site that opens a path under it and quoting its mode |
| **V10** | the fingerprint table | every row of map §0 in lines, bytes and SHA-256, with the new file beside them as it stands on the branch |
| **V11** | disclosure | the units considered in ascending `T0`, members and non-members with reasons; per `tau` the admissible `T0` list's `tz07b.member_list_sha` and its count; and the per-read observations file — **one row per member per `tau` per token id**, carrying `T0`, `tau`, `token_id`, the outcome string, `status`, `recv_ns`, `offset_ms`, the level counts, `best_bid`, `best_ask`, `bid5`, `ask5`, the four cumulative sizes, the venue `timestamp` and `sigma_hat` with the admissibility flag — **sufficient to reconstruct any single row of any table in §3 without re-running the pipeline** |

**Causality is not tested and this is why.** This TZ computes no quantity at decision time: it
computes no probability, no `state` and no `sd`. `sigma_hat` is produced by `tz10b.sigma_hat_of`
unchanged, which TZ-10b V2 proved bit-identical under perturbation strictly after the checkpoint
instant — **140 of 140 with 140 of 140 negative controls, quoted from map §4's TZ-10b row** — and
which TZ-13 §7 records TZ-11a V2 repeating at the same counts. A quote is an observation
stamped at its own `recv_ns` and is a function of nothing this project computes. The one causality
statement this TZ makes is §3.4's, and it is a measurement — the sign and size of `offset_ms` — not
an assertion.

---

## 8. The report

`CryptoReports/TZ-14-quote-inventory-report.md`, straight to `main` in one commit, and immutable once
committed.

It states, in this order: §0's gates, host, interpreter, refs and every free-space read; §1's
measurements in §3's order, each table at `ADMITTED` first and `OUTSIDE` in a separately headed
block, each naming its population, and each broken out weekday against weekend and admissible against
not; §3.9's seven predictions each marked held or refuted with the observed figure beside it; §2's
statement that no gate was applied and nothing was admitted or disqualified; §3's implementation, the
file's hash on the branch and the commit; §4's V1 … V11 with their counts; §5's publication and §9;
and a final section listing **every point where the text needed a reading and every workaround
chosen**, in the shape TZ-11a, TZ-12 and TZ-13 used.

The report states `wc -l` and `sha256sum` for the map and for every file the map's fingerprint table
lists. **A report is evidence, not acceptance**, and nothing in this TZ is accepted until the
Architect has re-derived its counts from its own disclosure.

---

## 9. Retention

In this order, each step only after the previous one exited 0:

1. **Copy first.** Every file under `/root/tz13-work/` whose SHA-256 is named by any committed report
   on `main`, and which `/root/btc-forensics/` does not already hold by hash, is copied there by
   exclusive create, with the hash asserted at source and destination. Assert that every file already
   in `/root/btc-forensics/` is unchanged — `197` of them at TZ-13's end. Report the counts before
   and after.
2. **Then the worktree**, `/root/tz13-work/wt`, `git worktree remove` without `--force`.
3. **Then the tree**, `rm -rf /root/tz13-work`, one command naming one tree, verified by `test -e`.
   **If the session's permission classifier refuses it, hand the Boss one exact block and verify the
   outcome from `test -e` afterwards, never from his report** (map §6). It refused this for TZ-12 and
   for TZ-13; expect it again.
4. If §0.7 found `/root/tz12-work` still present, it is reclaimed on the same three terms, reported
   separately.

`/root/tz14-work/` is the next TZ's to reclaim on the same terms. The capture is never deleted.

---

## 10. Pre-send checks

Performed against this file, start to end, as a separate reading after its last section was written.

**C1 — scope against body.** Enumerated from the finished file: **8** repository paths, **14** host
paths and **39** committed entry points and module attributes written as `module.name`, plus §2 item
6's eight-name allow-list of `pfair` attributes. Two of the eight repository paths are the ones §2
permits writing; the other six — `SYSTEM-MAP.md`, `research/pfair.py`,
`research/tz12-sized-gate.py`, `research/recorder/config.py`, `research/recorder/recorder.py` and the
directory `research/recorder/` — are named as **read**, and reading is not modifying, so prohibition
1 needs no exemption for them. Intersections with §2's prohibition list that do need one: **4**, each
written into §2 where the prohibition is made — `/root/btc-forensics/` against item 3, for §9's copy
by exclusive create; the report push against item 4, named in item 2; `sigma_hat` against item 5, for
§3.2's domain; and `tz06.qualification` with `analyze.venue` inside it against item 7, for the set
rule's own outcome read. `/var/lib/btc-recorder/**` intersects item 2 only as a read, and V9 carries
the proof by enumerating every call site that opens a path under it with its mode. The diff was
performed, not intended.

**C2 — origin of every expectation.** **23** fixed numeric expectations in §5 and §7, of four kinds.
**8** computed by the Architect independently of any implementation under test and cross-checked
against a committed artifact: the seven checkpoint epochs of self-test 1, each computed as
`t0 + 300 − tau` at `t0 = 1789206900` and checked against the `t` values `research/recorder/config.py`
states in its own docstring — `{60, 120, 180, 210, 240, 270, 290}` — and the equality
`config.QUOTE_TAUS == pfair.TAUS`, verified term by term against both files as committed. **3**
quoted from CANON §1.1 and computed exactly in decimal arithmetic: `0.0175`, `0.008925` and `0.0063`,
which CANON publishes as `1.75`, `0.89` and `0.63` probability points and which
`0.07 · p · (1 − p)` reproduces at every digit CANON prints. **1** quoted from a committed artifact:
`tz12.TEST2_SHA256`, also stated in TZ-11a's report §1.0 and in map §2.3. **11** exact by
construction — the test inputs and outputs of self-tests 2, 3 and 6 (`0.52`, `0.53`, `0.51`, `0.54`,
`0.03`, `0.50`, `12`, `5`, `0.01`, `3`) and V7's assertion total `36`, summed from §5.2's six items.
**None depends on a quantity this TZ measures.** V4's "1,200 of 1,200" is not an exception: it
asserts that two readers of the same bytes return the same multiset, which holds for every admissible
file content and for none of the market's properties. §6's two fail-fast bounds are resource guards
written as inequalities on wall-clock time; they assert no value and no reading depends on them, and
they are the only place a measured quantity enters an inequality at all.

**C3 — shape of every diff.** One new file, `research/tz14-quote-inventory.py`. The committed lines
the change replaces, read from `origin/main` at `dad557d56f478d0bf6ec9e9b814030291b3f399c`: **none** —
the path does not exist there. C3's bar on the phrase "insertions only" applies where that list is
not empty; here it is empty, and §5.3 says "additive in the strict sense" instead in any case.

**C4 — cost of every check.** §6 states each step in seconds, each at the maximum of the population
it bounds: set formation at `2,200` units considered, which is the whole capture minus the `573`
slots before the walk opens and not a share of it; the grids at all `1,200` members, at the rate
TZ-12 measured for a strictly larger per-member call; the quote pass at `1,200` members and `16,800`
replies, bounded by the enforced probe because **nothing has ever opened a quote file and there is no
measured rate for it**. **~442 s per run, ~950 s for the session**, against `tz12.SESSION_CEILING_S` =
`3,600`. Both fail-fast bounds are derived term by term beside them: `4.0 / 20 = 0.200` s per member
and `0.200 / 14 = 0.0143` s per `4,421`-byte reply, the byte figure from map §6's Tier C raw mean
divided by the fourteen reads `config.QUOTE_READS_PER_INTERVAL` fixes; and
`157 + 240 + 40 = 437 ≤ 1,200` s. Nothing is above `3,600` s and nothing is sampled: self-test 6's
synthetic directory is a test, and the probe's twenty members are read again in full at step 7.

**C5 — every count.** Re-derived from the sets §3 defines, each named beside its source: `1,200`
members, `8,400` checkpoints and `16,800` reads from §3.1 and §3.0; `6,000` checkpoints at `ADMITTED`
from §3.0's five-`tau` partition; `2,200` units considered from §6's upper bound; `20` `frozen` and
`2` `tracked` rows counted from map §0's fingerprint table as revision `2026-09-18-b` holds it — 23
rows, of which `SYSTEM-MAP.md` is the self-reference, `research/tz02-distribution.py` and
`.gitignore` are `tracked`, and the remaining twenty are `frozen`; `6` anchors from map §0's anchor
table; `36` assertions in V7, summed from §5.2 items 1 to 6 as `8 + 12 + 6 + 3 + 1 + 6`; `7 of 7`
`tau` in V8 from `pfair.TAUS`; `197` files in §9 from map §3's TZ-13 retention sentence; `140 of 140`
in §7's causality note from map §4's TZ-10b V2 row; `3` host reads from §5.1 steps 1, 5 and 10.

**C6 — every population.** Named for each statistic. **The 1,200 members**: §3.1's disclosure, §3.3
items 1, 2, 3, 4, 7 and 8, §3.4's clock-offset reading, §3.7 item 4 and §3.8. **The members whose
one-second grid is whole**: §3.2's admissible counts and shares. **The reads at a `tau`**, `1,200 × 2`
at full completeness: §3.3 items 5 and 6, §3.4's offsets, §3.5 items 1 to 8 and §3.6 items 1 to 5.
**The paired checkpoints at a `tau`** — both token ids at `200` with a parseable body, and the
member's `outcomes` a two-element `Up` / `Down` array: §3.7 items 1, 2, 3 and 5. **Each of those
four, split weekday against weekend and admissible against not**, wherever §3 says so. §3.9's seven
predictions each name their own population in the table's third column. No statistic in this TZ is
computed over a population that any label, any outcome or any pricer probability touches.

**C7 — every signature and every behaviour.** All **39** entry points and attributes were read from
`origin/main` at `dad557d56f478d0bf6ec9e9b814030291b3f399c` and each is quoted as the file holds it:
`tz06.scoring_set(manifests, need=SET_SIZE, *, after=None)`, whose body opens the walk at
`min(int(name) … if int(name) > after)` and returns `rows, members == need`, so §3.1's positional
`1,200`, keyword-only `after` and asserted `ok` are all correct;
`tz06.qualification(t0, manifests)`, whose body calls `venue(t0)` and appends on
`info["resolved_up"] is None` and `info["price_to_beat"] is None`, which is why §2 item 7 names it and
`analyze.venue` as one exemption; `analyze.venue(t0)`, which returns
`{"price_to_beat": …, "resolved_up": (outcome == "Up") …}`, the sentence §3.7 item 4 rests on;
`tz10b.grid_of(s3, t0)`, whose body asserts `len(grid) == GRID_POINTS and all(v is not None for v in
grid)` and raises otherwise — the precondition §3.2 now states in full, rather than discovering it in
a run; `tz10b.sigma_hat_of(grid, tau)`, whose body is
`pfair.realised_sigma(grid[:GRID_POINTS - tau])`; `tz11a.admissible_members(walked, members, admit)`,
whose body is a comprehension over `pfair.TAUS` keeping `walked[t0][tau]["sigma_hat"] >= admit[tau]`,
which is why §3.2 must hand it that exact shape and why it returns all seven `tau`;
`tz11a.host_read(when, t0s, floor)`, whose body asserts `free >= floor` and `doc["recorder_pids"]`
and whose `read_set_sha256` is `tz10b.read_set(t0s)` over the `t0s` handed in — the reason §5.1 step
1 states that read 1 passes the empty set and V9 compares the hash between reads 2 and 3 only;
`manifest._stream_path(dirpath, stream)`, whose body returns the `.jsonl.gz` where it exists and the
plain `.jsonl` otherwise; `manifest._quote_reads(dirpath)`, whose body skips a line lacking `recv_ns`
or `tau`, sets `body_is_json` from whether `rec.get("raw")` parses, and returns
`{"recv_ns", "tau", "token_id", "status", "body_is_json"}` and **not** `raw` — the whole reason §3.3
needs a reader of its own; `tz07b.member_list_sha(members)`, the SHA-256 of the sorted `T0` list
joined by newlines with no trailing newline; `config.quote_checkpoint_epoch(t0, tau)`, whose body is
`t0 + INTERVAL_S - tau`; and the constants `tz11a.FLOOR_START_BYTES` `2060000000`,
`tz11a.FLOOR_BYTES` `2000000000`, `tz12.SESSION_CEILING_S` `3600`, `config.CLOCK_OFFSET_LIMIT_MS`
`50.0`, `config.QUOTE_TAUS` `(240, 180, 120, 90, 60, 30, 10)` and `pfair.TAUS` `GATED_TAUS + (10,)`,
each read as an assignment in the file. **`QUOTE_TIMEOUT_S` in `research/recorder/recorder.py` is
`8`, in seconds**, and §3.4 says so and multiplies by `1,000` itself — an earlier draft of that
sentence called the constant `8,000`, which the file does not hold, and this check is what found it.
The entry points named only as never called — `tz10b.m2_labels(members)`,
`tz11a.walk_member(t0, manifests, guard)`, `tz11a.fit_student(r)` and the twelve `pfair` probability
functions of §2 item 6 — were read the same way, so V2's static count is over names that exist.

**C8 — every cross-reference.** **30** resolved by reading the referenced text, never from memory:
CANON PART II's sampling-rule and power clauses (§1, §3.2, §4); CANON §1.1's fee formula and its
three published points (§3.6, §5.2); CANON PART III hard rules 1, 2, 5, 8, 9 and 11 (the header, §8,
§3.1, §0.4, §1); map §0 (§0.1, V1, V10), §1 (§0.8), §2.3 (§1, §3.1), §3 (§0.7, §9), §4 (§1, §3.8,
§7), §5 (§3.0), §6 (§0.2, §0.4, §3.5, §3.6, §6, §9); map §7 items 15, 17, 29, 51, 52, 58 and 62 (§1,
§3.4, §0.5, §3.2, §6, §3.1, §6); contract §4.1 (§2, §8); TZ-13 §5.1 and §7 (§5.1, §7); TZ-11a's
report §1.0 (§5.2 item 5); and the committed text of `research/recorder/config.py`,
`research/recorder/recorder.py` and `research/tz12-sized-gate.py` (§5.2 item 1, §3.4, §5.2 item 5 and
§6). Each supports the sentence that makes it.
