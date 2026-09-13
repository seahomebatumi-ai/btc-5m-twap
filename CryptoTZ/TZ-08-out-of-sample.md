# TZ-08 — Out-of-sample scoring of `p_fair` against the TZ-07a §8 gate

**Canonical filename:** `CryptoTZ/TZ-08-out-of-sample.md`. The Executor names the committed file
from this line and from no other.

**Report:** `CryptoReports/TZ-08-out-of-sample-report.md`. A re-execution writes
`CryptoReports/TZ-08-out-of-sample-report-run2.md` and never reuses the first path.

**Model:** Opus. **Branch:** `tz-08-out-of-sample`. **Merge:** the Boss only, after the
Architect's verdict.

---

## 0. Fingerprint gate — compared before any work; mismatch is BLOCKED

**Required System Map revision:** `2026-09-13-b`.

| anchor | required value |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-open / 2-not-started` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` |
| `A6` — pricer | `cb72abb8dd8a` |

**Map provenance.** On `main`, `git log -1 --format=%H -- SYSTEM-MAP.md` must begin with
`9064dbd`. If the last commit touching the map is any other commit, the map on `main` is not the
file this TZ was written against — **BLOCKED**, and the report states the commit found.

**Host gate — all three, or this is not the capture host and the run is BLOCKED:**

1. `/var/lib/btc-recorder/` exists and holds interval directories.
2. The recorder process is running and the newest `runtime.jsonl` start record carries sha
   `4216c04673ced76b5b2ac60ef57c9abedc46f9b9`.
3. The filesystem holding it is `/dev/vda2`, total `31,612,203,008` bytes.

**Resource floor, derived from System Map §6:** free space on `/dev/vda2` at run start must be at
least `2,000,000,000` bytes. Below it, BLOCKED. Scratch and outputs go to `/root/tz08-work/`,
outside the repository.

**Fingerprint report.** The report states `wc -l` and `sha256sum` for `SYSTEM-MAP.md` and for
every row of the map's fingerprint table, at run start. Every `frozen` row must match the hash
printed there, with the single exception authorized in §5, which is reported before and after.

---

## 1. Purpose

Score the pricer merged at `fb5c426` on a set of intervals **disjoint in time** from the 400 that
produced `SD_SCALE`, against the gate TZ-07a §8 fixed before any of this data existed. This is
the first out-of-sample test of anything in this project.

Secondary, and it changes no verdict: record the out-of-sample reading of the two quantities that
decide what comes after — the pre-registered prediction of System Map §7 item 22, and the
settlement-dispersion `Λ` measured on the new set against the frozen constants.

**Phase 1 can only disqualify.** A passing gate is not an edge and is not reported as one.

---

## 2. Scope prohibitions

Each prohibition names its own exemptions. There are none where none are named.

1. **`research/pfair.py` is not touched.** Not a line, not a literal, not a comment. `SD_SCALE`
   does not move — not before the score, not after it, not if the score fails. Its SHA-256 must
   read `cb72abb8dd8a460908d0b4cd50da472ddd1c72b57be35b4cf90303503d47e01f` at run start and at
   run end. **Exempt: nothing.**
2. **No gate threshold is written in this TZ or introduced into code.** See §4. **Exempt:
   nothing.**
3. **No quote is read.** `quotes.jsonl.gz` is never opened. `quotes_complete` and
   `quote_offsets_ms` are not membership conditions, are not reported as statistics, and are not
   aggregated. Phase 2's gate does not exist yet and no market statistic may precede it.
   **Exempt: nothing.**
4. **No result scored under `A6 = 9bd4213a60a3` is re-opened**, and neither TZ-07a nor TZ-07b is
   re-run except where §7 V1 requires it as a regression. **Exempt: §7 V1 only.**
5. **No file outside the two paths named in §5 is created, modified or deleted** in the
   repository. **Exempt: the report, written to the path in the header.**

Outcome documents **are** read. This is a calibration TZ; the labels are the venue's own
`resolution.json` resolutions and nothing else. That is the opposite of TZ-07b §2 and is
deliberate.

---

## 3. Set formation — the sampling rule, fixed here, before any score exists

- **Universe:** every interval directory under `/var/lib/btc-recorder/` whose `T0` is strictly
  greater than `1789166400`, ordered by `T0` ascending.
- **Qualifying condition:** exactly TZ-06 §4's five conditions, evaluated **by the same code that
  evaluated them for TZ-06**. No new predicate is written and no condition is added, relaxed or
  reordered.
- **Members:** the **first 400 qualifying units in `T0` order.** The set is never shrunk, never
  re-ordered, never re-selected, and is not adjusted after any score is seen.
- **Fewer than 400 qualify → BLOCKED.** No partial table, no partial score, no gate arithmetic on
  a short set. The report states the count found and stops.
- **Disclosure:** every unit considered is listed in `T0` order, member and non-member alike,
  each non-member with its exclusion reason. A count the Architect cannot re-derive is not
  evidence.
- **Member-list fingerprint:** SHA-256 of the sorted `T0` list rendered as decimal ASCII joined by
  newlines with no trailing newline — the TZ-07b convention. Reported.
- **Disjointness, asserted, not assumed:**
  - the intersection of the TZ-08 member list with the TZ-06 member list is empty;
  - `min(T0)` over TZ-08 members is strictly greater than `1789166400`;
  - the TZ-06 member list, re-derived in this run by the unmodified code path, hashes to
    `6d94a346a47a04a1a0849968effd9023d7585fe628b304ba2ae7a15953ee67f9`.

  Any one of the three failing is BLOCKED.

**Stated so the verdict cannot over-claim:** these 400 intervals are contiguous in wall-clock time
and span roughly a day and a half. The set is out of sample; it is not a second volatility regime.

---

## 4. The gate — imported, never restated

**The gate is TZ-07a §8 exactly as committed. This TZ does not restate it, and no threshold, floor
or band is typed anywhere in this file.** The gate does not move, and the Architect's prediction
that part of it will fail is not a reason to touch it.

The Executor:

1. reads `CryptoTZ/TZ-07a-variance-time.md` from `main`, reports its `wc -l` and `sha256sum`, and
   reproduces §8 **verbatim** as section 0 of the report;
2. computes G1, G2 and G3 by calling the code that already implements them —
   `research/tz06-calibration.py` for the Brier table, the calibration bins and the gate tables,
   `research/tz07a-variance-time.py` for the scale statistic and its standard error. **No
   threshold constant is re-typed, re-derived or recomputed in the new file.**
3. If the committed §8 text and the behaviour of that code disagree in any particular, the run is
   **BLOCKED**, the disagreement is stated in the report, and no score is printed. The gate is not
   reconciled by the Executor.

**Taus.** G1, G2 and G3 are evaluated at the six taus TZ-07a §8 gates. `tau = 10` is computed and
reported as a diagnostic only: it carries no threshold, it cannot pass or fail anything, and it is
excluded from every gate count.

**Preconditions imported with their own floors.** `TZ-06 P` (reconstructed close TWAP agreeing
in sign with the venue's outcome) and `TZ-06 V3` (price to beat equals the settlement feed's
reading at the open) are re-run on the new set by the unmodified code path, with the floors that
code already carries. Below either floor, the calibration score is uninterpretable and the run is
**BLOCKED**. No new floor is invented for either. Both keep the `TZ-06` prefix everywhere in this
TZ and in the report, because this TZ's own validation checks are numbered `V` as well.

---

## 5. The change authorized — minimal diff, exactly two paths

**One `frozen` row may change: `research/tz06-calibration.py`.** Additive only:

- keyword-only parameters that bound the set-formation window and the member count, each
  defaulting to the literal presently in the file, so that a call with no arguments is behaviour-
  identical;
- no formula, no threshold, no qualifying condition, no ordering and no output format altered;
- nothing removed.

**One new file: `research/tz08-out-of-sample.py`** — a driver. It holds the new window constant,
the member-list fingerprint, the disclosure table, the report tables, and its own asserts. **It
holds no formula and no threshold**, and calls `pfair.py`, `tz06-calibration.py`,
`tz07a-variance-time.py` and `tz07b-settlement-dispersion.py` for everything else. It imports
M6's disconnect rule from `tz07a-variance-time.py` rather than reimplementing it.

`git diff --name-only` against the merge base must list exactly these two paths, plus the report.
Any third path is BLOCKED.

---

## 6. What is computed

Per tau, over the 400 members:

1. **G1** — the Brier table and its baseline, by the existing code.
2. **G2** — the shape statistic, per tau, with **eligible-bin counts reported per estimator**, not
   pooled into one column.
3. **G3** — the scale statistic with its standard error and its distance from 1 in standard
   errors.
4. **`TZ-06 P`** and **`TZ-06 V3`** — reported with counts and residual medians and worsts.
5. `tau = 10` — the same quantities, marked as diagnostic and thresholdless.

Per-observation rows are written to `/root/tz08-work/tz08-observations.csv`, outside the
repository, so any single row is reconstructible without re-running the pipeline. Line count,
byte count and SHA-256 are reported.

---

## 7. Validation

Written by the Architect. The Executor runs these; it does not design them, extend them, or edit a
test to make it pass.

**V1 — the edit is behaviour-preserving.** Run `tz06-calibration.py` on the TZ-06 window with no
arguments. All six `Brier` values reproduced to all six decimals, `P` at 397 of 400, member-list
SHA-256 `6d94a346a47a04a1a0849968effd9023d7585fe628b304ba2ae7a15953ee67f9`. Any deviation in any
digit is BLOCKED — the parameterisation is then not additive and the score that follows it would
be uninterpretable.

**V2 — causality by perturbation, never by truncation.** 120 members, selected by a deterministic
rule stated in the report, **constructed to include every member of the 400 that carries a
recorded disconnect** and filled out from the remainder in `T0` order. Perturb every observation
timestamped at or after the checkpoint: output bit-identical, 120 of 120. Negative control:
perturbing the last readable report changes the output, 120 of 120. Both counts, or BLOCKED.

**V3 — determinism.** Two full runs, byte-identical outputs. The outputs carry no wall-clock
timestamp and no path that varies between runs.

**V4 — set integrity.** The three disjointness assertions of §3, the member-list hash, and the
full disclosure table.

**V5 — no pricer drift.** `sha256sum research/pfair.py` equals
`cb72abb8dd8a460908d0b4cd50da472ddd1c72b57be35b4cf90303503d47e01f` at run start **and** at run
end. `git diff --name-only` lists exactly the two paths of §5.

**V6 — fingerprint table.** Every row of the map's fingerprint table reported with `wc -l` and
`sha256sum`; every `frozen` row matching, except `research/tz06-calibration.py`, reported before
and after.

**V7 — the pre-registered prediction (System Map §7 item 22).** Print the predicted scale statistic
against the measured, per tau, with the difference. **No threshold. This table cannot pass or fail
anything** — it is printed so that a prediction recorded in writing before the set existed is
tested by the set rather than by the Architect's later reading of it.

| tau | predicted | measured | difference |
|---|---|---|---|
| 240 | `0.999` | — | — |
| 180 | `0.946` | — | — |
| 120 | `0.945` | — | — |
| 90 | `0.761` | — | — |
| 60 | `0.787` | — | — |
| 30 | `1.012` | — | — |

**V8 — out-of-sample dispersion of the settlement quantity.** Run the TZ-07b instrument unmodified
on the 400 TZ-08 members: the `Λ` table at all seven taus, the admissible-anchor count, the count
dropped by M6's rule and the members contributing them, and `Λ_oos` against the frozen `SD_SCALE`
literal at each tau as a ratio. **No threshold, and this measurement authorizes no change to any
constant.** It exists because item 22 asks a question about the residual's shape and the next TZ
should not need a fourth measurement round to answer it.

**V9 — tail and robust-scale diagnostic.** On the same 400: the empirical tail fractions against
the normal's at one and three `Λ`, and `MAD / 0.674490` and `IQR / 1.348980` against `Λ`, per tau.
No threshold. This is the out-of-sample counterpart of the table that produced item 22.

---

## 8. Report

Path as in the header. Section numbers are asserted unique in the pre-delivery change list.
Required sections, in order: the verbatim TZ-07a §8; the fingerprint block; the host gate; set
formation with the full disclosure table and the member-list hash; the gate tables G1, G2, G3;
`TZ-06 P` and `TZ-06 V3`; the `tau = 10` diagnostic; V1 through V9; the observations-file
fingerprint; anything the Executor found and could not resolve.

**Counts are counts.** "All checks passed" is not a result and is grounds for rejection of the
report.

---

## 9. BLOCKED conditions — exhaustive

Any one of these stops the run before a score is printed, and the report says which:

1. Map revision, any anchor, or the map's last-touching commit not matching §0.
2. Any of the three host-gate checks failing.
3. Free space on `/dev/vda2` below `2,000,000,000` bytes.
4. Fewer than 400 qualifying units in the universe of §3.
5. Any of the three disjointness assertions of §3 failing.
6. `CryptoTZ/TZ-07a-variance-time.md` unreadable, or its §8 contradicted by the code that
   implements the gate.
7. V1 deviating in any digit.
8. `pfair.py` differing from its frozen hash at either check.
9. A third repository path in the diff.
10. `TZ-06 P` or `TZ-06 V3` below the floor the existing code carries.
11. Any read forbidden by §2.

A BLOCKED report is a valid, useful and cheap result. It is published like any other.

---

## 10. What this TZ does not decide

Nothing about what happens if G3 fails at `tau` 90 and 60, which the Architect has predicted in
writing that it will. Editing a constant, a gate or an estimator after seeing a score is tuning,
and no such edit is authorized here in any branch of the outcome. The disposition of item 22 is
decided in a later TZ, from this report.
