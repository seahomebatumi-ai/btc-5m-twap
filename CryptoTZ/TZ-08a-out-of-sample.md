# TZ-08a — Out-of-sample scoring of `p_fair` against the TZ-07a §8 gate

**Corrects TZ-08**, which was BLOCKED at its §7 V2 before any score existed. TZ-08 is immutable and
is not edited; this TZ replaces it in full. Five defects in TZ-08 are repaired here — §7 V2's
perturbation set, the standard error §6 asked of an instrument that computes none, G3's evaluation
route, §5's unsatisfiable default, and §9's false claim of exhaustiveness. Each repair is named at
the point it applies.

**Canonical filename:** `CryptoTZ/TZ-08a-out-of-sample.md`. The Executor names the committed file
from this line and from no other.

**Report:** `CryptoReports/TZ-08a-out-of-sample-report.md`. A re-execution writes
`CryptoReports/TZ-08a-out-of-sample-report-run2.md` and never reuses the first path.

**Model:** Opus. **Branch:** `tz-08a-out-of-sample`. **Merge:** the Boss only, after the
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
`9064dbd`.

**The gate document is pinned.** `CryptoTZ/TZ-07a-variance-time.md` must read `251` lines and
SHA-256 `0e4852301c493ed7e4cb98d8d880a2c6b42b55f01811976ca9131fc62e61c4e3`. A different file is a
different gate — BLOCKED.

**Host gate — all three, or this is not the capture host and the run is BLOCKED:**

1. `/var/lib/btc-recorder/` exists and holds interval directories.
2. The recorder process is running and the newest `runtime.jsonl` start record carries sha
   `4216c04673ced76b5b2ac60ef57c9abedc46f9b9`.
3. The filesystem holding it is `/dev/vda2`, total `31,612,203,008` bytes.

**Resource floor, derived from System Map §6:** free space on `/dev/vda2` at run start must be at
least `2,000,000,000` bytes. Below it, BLOCKED. **Free space is reported at run start and at run
end, both in exact bytes**, because TZ-08 measured `6,617,538,560` free against `7,855,497,216`
recorded a day earlier and the difference is not the capture. Scratch and outputs go to
`/root/tz08a-work/`, outside the repository.

**Fingerprint report.** `wc -l` and `sha256sum` for `SYSTEM-MAP.md` and every row of the map's
fingerprint table, at run start. Every `frozen` row matches or BLOCKED, except the single row
authorized in §5, reported before and after.

---

## 1. Purpose

Score the pricer merged at `fb5c426` on 400 intervals disjoint in time from the 400 that produced
`SD_SCALE`, against the gate TZ-07a §8 fixed before any of this data existed. First out-of-sample
test of anything in this project.

Secondary, changing no verdict: the out-of-sample reading of the pre-registered prediction in
System Map §7 item 22, and of the settlement dispersion `Λ` against the frozen constants.

**Phase 1 can only disqualify.** A passing gate is not an edge and is not reported as one.

---

## 2. Scope prohibitions

Each prohibition names its own exemptions. There are none where none are named.

1. **`research/pfair.py` is not touched.** Not a line, not a literal, not a comment. `SD_SCALE`
   does not move — not before the score, not after it, not if the score fails. SHA-256
   `cb72abb8dd8a460908d0b4cd50da472ddd1c72b57be35b4cf90303503d47e01f` at run start and at run end.
   **Exempt: nothing.**
2. **No gate threshold is written in this TZ or introduced into code.** See §4. **Exempt:
   nothing.**
3. **No quote is read.** `quotes.jsonl.gz` is never opened. `quotes_complete` and
   `quote_offsets_ms` are not membership conditions, are not reported, are not aggregated.
   **Exempt: nothing.**
4. **No result scored under `A6 = 9bd4213a60a3` is re-opened**, and neither TZ-07a nor TZ-07b is
   re-run except where §7 V1 requires it as a regression. **Exempt: §7 V1 only.**
5. **No file outside the two paths named in §5 is created, modified or deleted** in the
   repository. **Exempt: the report, written to the path in the header.**

Outcome documents **are** read. This is a calibration TZ; the labels are the venue's own
`resolution.json` resolutions and nothing else.

**TZ-08's probe changes nothing here.** It priced 720 observations for its perturbation counts and
computed no calibration statistic and no label comparison. No constant was informed by it and the
set below is untouched by it.

---

## 3. The set — already formed, disclosed and locked by hash

TZ-08 formed this set with the committed code before any score existed, and published it. It is
now fixed. **This TZ re-derives it and asserts equality; it does not re-select it.**

| property | value |
|---|---|
| rule | the first 400 qualifying units, in `T0` order, with `T0 > 1789166400` |
| qualifying condition | exactly TZ-06 §4's five conditions, by the same code |
| units considered | 433, every grid slot from `1789166700` to `1789296300` |
| members | 400 |
| non-members | 33, every one failing on `disconnect`, none for any other reason |
| first member | `1789166700` |
| last member | `1789296300` |
| member-list SHA-256 | `3b17729c050e5fbf8fed1bd0877d5dd5c229370609cd672c84eeed1ddc3d5762` |

The hash is over the sorted `T0` list as decimal ASCII joined by newlines with no trailing newline,
computed by `tz07b-settlement-dispersion.member_list_sha`.

**Assertions, all before any score:**

- the re-derived member list hashes to `3b17729c050e5fbf8fed1bd0877d5dd5c229370609cd672c84eeed1ddc3d5762`;
- 400 members, 433 units considered, 33 non-members, every one on `disconnect`;
- intersection with the TZ-06 member list is empty;
- `min(T0)` is `1789166700`, strictly greater than `1789166400`;
- the TZ-06 list, re-derived by the unmodified code path, hashes to
  `6d94a346a47a04a1a0849968effd9023d7585fe628b304ba2ae7a15953ee67f9`.

Any one failing is BLOCKED. **The set is never shrunk, never re-ordered, never re-selected**, and
directories written after TZ-08's run cannot change it: it is a prefix of the ordered universe, not
a suffix.

**Disclosure.** Every unit considered is listed in `T0` order, member and non-member alike, each
non-member with its exclusion reason.

**Stated so the verdict cannot over-claim:** these 400 intervals are contiguous in wall-clock time
and span about a day and a half. The set is out of sample; it is not a second volatility regime.

---

## 4. The gate — imported, never restated

**The gate is TZ-07a §8 exactly as committed. This TZ does not restate it, and no threshold, floor
or band is typed anywhere in this file.** The gate does not move, and the Architect's prediction
that part of it will fail is not a reason to touch it.

1. The Executor reads `CryptoTZ/TZ-07a-variance-time.md` (pinned in §0) and reproduces §8
   **verbatim** as section 0 of the report.
2. **G1 and G2 are computed by the committed code** — `tz06-calibration.py`, including its own
   `MAX_FAILING_BINS`. No threshold is re-typed.
3. **G3 is not computed in code, and no G3 threshold is introduced.** TZ-08 established that
   `tz07a-variance-time.py` runs the scale statistic as a diagnostic with no threshold attached.
   The Executor therefore **reports the statistic and does not judge it**: per tau, `lambda_hat`,
   `ll_at_lambda_hat`, `ll_at_one`, `likelihood_ratio`, `chi_square_1df_p` and `n`, exactly as
   `lambda_hat` returns them. The report additionally quotes verbatim the `LAMBDA_LO`, `LAMBDA_HI`
   and `LAMBDA_TOL` block of `tz07a-variance-time.py` with the comment above it, and states each
   constant's value. **The Architect applies §8 to that table in the verdict.** The report states
   no G3 pass or fail.
4. **No standard error is computed, reported or referred to anywhere.** TZ-08 asked for one; the
   instrument computes none, and §2.2 forbids adding the formula. The scale statistic's distance
   from 1 is carried by the likelihood ratio and its chi-square p-value, which the instrument does
   compute.
5. If the committed §8 text and the behaviour of the code disagree in any particular, the run is
   **BLOCKED**, the disagreement is stated, and no score is printed. The gate is not reconciled by
   the Executor.

**Taus.** G1, G2 and the scale statistic are evaluated at the six taus TZ-07a §8 gates. `tau = 10`
is computed and reported as a diagnostic only: no threshold, excluded from every gate count.

**Preconditions imported with their own floors.** `TZ-06 P` and `TZ-06 V3` are re-run on the new
set by the unmodified code path, with the floors that code already carries. Below either floor the
calibration score is uninterpretable and the run is **BLOCKED**. No new floor is invented. Both
keep the `TZ-06` prefix throughout, because this TZ's own checks are numbered `V` as well.

---

## 5. The change authorized — minimal diff, exactly two paths

**One `frozen` row may change: `research/tz06-calibration.py`.** Additive only:

- keyword-only parameters bounding the set-formation window and the member count;
- the member count defaults to the literal already there, `SET_SIZE`;
- **the window's lower bound defaults to `None`, and `None` reproduces the present expression
  unchanged.** TZ-08 required a default equal to "the literal presently in the file"; there is no
  such literal, the bound being `min(int(name) for name in os.listdir(...))`. A default of `None`
  is what preserves behaviour, and §7 V1 is what proves it did.
- no formula, no threshold, no qualifying condition, no ordering, no output format altered, nothing
  removed.

**One new file: `research/tz08a-out-of-sample.py`** — a driver. It holds the window constant, the
member-list assertions, the disclosure table and the report tables. **It holds no formula and no
threshold**, and calls `pfair.py`, `tz06-calibration.py`, `tz07a-variance-time.py` and
`tz07b-settlement-dispersion.py` for everything else, importing M6's disconnect rule from
`tz07a-variance-time.py` rather than reimplementing it.

`git diff --name-only` against the merge base must list exactly these two paths, plus the report.
Any third path is BLOCKED.

---

## 6. What is computed

Per tau, over the 400 members:

1. **G1** — the Brier table and its baseline, by the committed code.
2. **G2** — the shape statistic, with **eligible-bin counts reported per estimator**, not pooled
   into one column.
3. **The scale statistic** — the six values `lambda_hat` returns, per §4.3, judged by nobody in the
   report.
4. **`TZ-06 P`** and **`TZ-06 V3`** — counts, residual medians and worsts.
5. `tau = 10` — the same quantities, marked diagnostic and thresholdless.

Per-observation rows go to `/root/tz08a-work/tz08a-observations.csv`, outside the repository, so
any single row is reconstructible without re-running. Line count, byte count and SHA-256 reported.

---

## 7. Validation

Written by the Architect. The Executor runs these; it does not design them, extend them, or edit a
test to make it pass.

**V1 — the edit is behaviour-preserving.** Run `tz06-calibration.py` on the TZ-06 window with no
arguments. Six `Brier` values reproduced to all six decimals, `TZ-06 P` at 397 of 400, member-list
SHA-256 `6d94a346a47a04a1a0849968effd9023d7585fe628b304ba2ae7a15953ee67f9`. Any deviation in any
digit is BLOCKED.

**V2 — causality by perturbation, never by truncation.**

*Sample.* 120 members, by a deterministic rule stated in the report, constructed to include every
member of the 400 carrying a recorded disconnect under TZ-07a M6's criterion, filled out from the
remainder in `T0` order. Six gated taus, 720 observations.

*Perturbation set.* Every `chainlink` and `twap60` report whose `timestamp` is **strictly greater
than** the checkpoint instant, by the committed `tz06-calibration.perturb_after` (`ts > ts_ms`),
unmodified. **This is the repair of TZ-08's defect:** TZ-08 wrote "at or after", the feed stamps
every report on a whole second, every checkpoint is a whole second, and the report standing exactly
at the instant is the one `S_t` reads — so TZ-08's test and its negative control demanded opposite
outcomes from perturbing the same report. Strictly-after is also the wording TZ-06 V4 and TZ-07a V2
carry, so this check remains comparable with theirs.

*Disjointness, asserted before the counts are printed.* The perturbation set (`ts > ts_ms`) and the
negative control's subject, the report `tz06-calibration.last_readable` returns (`ts <= ts_ms`),
are disjoint by construction. The report asserts per observation that no report belongs to both,
and states the count: 720 of 720 disjoint, or BLOCKED.

*Counts.* Perturbation leaves `state`, `sd_corrected` and `p_fair_corrected` bit-identical: **720
of 720 observations and 120 of 120 members.** Negative control — perturbing the `chainlink` report
`last_readable` returns — changes the output: **720 of 720 observations and 120 of 120 members.**
Both, or BLOCKED.

*On the record, because it is what makes strictly-after correct here.* The count of `chainlink`
reports over the 400 members whose `timestamp` is not a multiple of 1,000 ms, and the count of the
2,400 checkpoints carrying a report at the exact instant.

**V3 — determinism.** Two full runs, byte-identical outputs. Outputs carry no wall-clock timestamp
and no path that varies between runs.

**V4 — set integrity.** Every assertion of §3, the member-list hash, and the full disclosure table.

**V5 — no pricer drift.** `sha256sum research/pfair.py` equals
`cb72abb8dd8a460908d0b4cd50da472ddd1c72b57be35b4cf90303503d47e01f` at run start **and** at run end.
`git diff --name-only` lists exactly the two paths of §5.

**V6 — fingerprint table.** Every row reported with `wc -l` and `sha256sum`; every `frozen` row
matching, except `research/tz06-calibration.py`, reported before and after.

**V7 — the pre-registered prediction (System Map §7 item 22).** Print the predicted scale statistic
against `lambda_hat`, per tau, with the difference. **No threshold. This table cannot pass or fail
anything** — it is printed so that a prediction recorded in writing before the set existed is
tested by the set rather than by the Architect's later reading of it.

| tau | predicted | `lambda_hat` | difference |
|---|---|---|---|
| 240 | `0.999` | — | — |
| 180 | `0.946` | — | — |
| 120 | `0.945` | — | — |
| 90 | `0.761` | — | — |
| 60 | `0.787` | — | — |
| 30 | `1.012` | — | — |

**V8 — out-of-sample dispersion of the settlement quantity.** Run the TZ-07b instrument unmodified
on the 400 members: the `Λ` table at all seven taus, the admissible-anchor count, the count dropped
by M6's rule with the members contributing them, and `Λ_oos` against the frozen `SD_SCALE` literal
at each tau as a ratio. **No threshold, and this authorizes no change to any constant.**

**V9 — tail and robust-scale diagnostic.** On the same 400: empirical tail fractions against the
normal's at one and three `Λ`, and `MAD / 0.674490` and `IQR / 1.348980` against `Λ`, per tau. No
threshold. The out-of-sample counterpart of the table that produced item 22.

---

## 8. Report

Path as in the header. Section numbers asserted unique in the pre-delivery change list. Required
sections, in order: the verbatim TZ-07a §8; the fingerprint block; the host gate with free space at
start and end; the set with its full disclosure table and hash; G1; G2; the scale-statistic table
and the quoted constants block; `TZ-06 P` and `TZ-06 V3`; the `tau = 10` diagnostic; V1 through V9;
the observations-file fingerprint; anything found and unresolved.

**Counts are counts.** "All checks passed" is not a result and is grounds for rejection.

---

## 9. BLOCKED conditions

**This list is not exhaustive, and TZ-08's claim that its equivalent was is the fifth defect
repaired here.** Any check in §7 failing the count it states is BLOCKED, whether or not it appears
below. The list names what stops the run before §7 is reached:

1. Map revision, any anchor, or the map's last-touching commit not matching §0.
2. `CryptoTZ/TZ-07a-variance-time.md` not matching its pinned line count and hash, or unreadable.
3. Any of the three host-gate checks failing.
4. Free space on `/dev/vda2` below `2,000,000,000` bytes at run start.
5. Any assertion of §3 failing.
6. TZ-07a §8 contradicted by the code that implements G1 or G2.
7. `pfair.py` differing from its frozen hash at either check.
8. A third repository path in the diff.
9. `TZ-06 P` or `TZ-06 V3` below the floor the existing code carries.
10. Any read forbidden by §2.

A BLOCKED report is a valid, useful and cheap result. It is published like any other.

---

## 10. What this TZ does not decide

Nothing about what happens if the scale statistic lands where the Architect predicted at `tau` 90
and 60. Editing a constant, a gate or an estimator after seeing a score is tuning, and no such edit
is authorized here in any branch of the outcome. The disposition of item 22 is decided in a later
TZ, from this report.
