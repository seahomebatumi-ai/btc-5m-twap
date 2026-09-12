# TZ-06 — p_fair calibration against venue-resolved labels

**Canonical filename:** `TZ-06-pfair-calibration.md` — the Executor names the committed file from
this line and from no other source.

| item | value |
|---|---|
| destination | `CryptoTZ/TZ-06-pfair-calibration.md` |
| report | `CryptoReports/TZ-06-pfair-calibration-report.md` → straight to `main` |
| code | `research/pfair.py`, `research/selftest-pfair.py`, `research/tz06-calibration.py` → branch `tz-06-pfair-calibration`, from `main` → PR. **Never straight to `main`.** |
| authorized frozen-row changes | `research/recorder/analyze.py` and `research/recorder/selftest.py`, under §5 R-c only. No other frozen row may move, and the report states the new hash of each. |
| Executor model | **Opus** — the pricer formulas, causality and gate arithmetic |

## 0. Fingerprint gate

| anchor | required value |
|---|---|
| System Map revision | `2026-09-12-a` |
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-open / 2-not-started` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` |

**Host gate.** This TZ reads the capture, so it executes on the capture host and nowhere else.
Before any other work, check all three, mechanically:

| check | required |
|---|---|
| `/var/lib/btc-recorder/` | exists, and holds interval directories |
| the recorder process | running, and the newest `runtime.jsonl` start record carries sha `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` |
| the filesystem holding that path | device `/dev/vda2`, total exactly `31,612,203,008` bytes |

Any mismatch, on the anchors or on the host gate → **BLOCKED** before any work, with the three
observed values reported and nothing else done.

---

## 1. Why this TZ exists

Phase 0 is closed: the venue settles on the trailing-TWAP comparison, 200 of 200. Phase 1 asks the
last question that can be answered without touching the market — **is the pricer calibrated
against labels the venue itself produced?**

No implementation of the current pricer exists. Everything in `research/` implements the
superseded interval-integral reading, which is closed and is not a candidate. This TZ writes the
first implementation and scores it against 400 venue resolutions already on disk.

**Phase 1 can only disqualify.** Passing means the pricer was not caught being wrong. It is not an
edge, it is not permission to build an engine, and it says nothing about where the market quotes.

## 2. Scope

Read-only over the capture already on disk. **No write of any kind under
`/var/lib/btc-recorder/`.** Scratch space and outputs live under `/root/tz06-work/`.

**Not in scope, and their appearance in the diff or the report is grounds for rejection:**

- **Any read of `quotes.jsonl.gz`.** Tier C is Phase 2, and a Phase 2 gate must be fixed before
  anyone has seen a quote. This TZ is executed by a session that must remain able to write it.
- any market statistic of any kind — spread, mid, depth, quoted probability, fee applied to
  anything;
- any label that is not the venue's own resolved outcome;
- any second implementation of a §3 formula or of the stream reader named in §3;
- any change to what the recorder captures, or to `recorder.py`, `config.py`, `manifest.py`,
  `probe.py`;
- any edit to `research/twap-divergence.py`, `research/selftest-twap-divergence.py`,
  `research/tz02-distribution.py`;
- any file under `engine/`; any Release upload; any deletion of anything the recorder wrote.

## 3. The pricer — one implementation, in `research/pfair.py`

**The model, verbatim. This file is its only implementation, in this repository and in any
language, and both the pipeline and the self-tests call it.**

```
tau >= 60:
    state = S_t - K
    sd    = sigma * sqrt(tau - 40)

tau < 60:
    m_r   = mean oracle price over [t0 + 240, t0 + t]     # realised part of the window
    state = ((60 - tau) * m_r + tau * S_t) / 60 - K
    sd    = sigma * tau**1.5 / (60 * sqrt(3))

p_fair    = Phi(state / sd)
```

`t = 300 - tau`. The two branches meet at `tau = 60`, where both give `sd = sigma * sqrt(20)`.
**At `tau >= 60` the running average of the interval has weight zero** — the settlement window is
the last 60 seconds and nothing before it enters. `Phi` is the standard normal CDF, from
`math.erf`. Arithmetic is `decimal.Decimal` up to the final division, exactly as `analyze.py`
handles prices.

**The reader is not rewritten.** `research/recorder/analyze.py` already holds the only
implementation: `reports(t0, stream)` — `type == "update"` frames only, `payload.timestamp` in
milliseconds, `payload.full_accuracy_value` at full precision — together with
`last_at_or_before`, `first_at_or_after`, `venue`, `published_equal`, `load_manifests` and
`reasons_for`. Import them.

**All timestamps are the venue payload's own `timestamp`, never the recorder's `recv_ns`.** The
local clock is not a pricing input and this TZ makes no latency claim anywhere.

| symbol | definition | source |
|---|---|---|
| `K` | the first `twap60` report with `timestamp >= T0 * 1000` | `twap60.jsonl.gz` — causal, and the same reading TZ-04b's R1 validated at 200 of 200 |
| label | `Up` → 1, `Down` → 0 | `manifest.resolved_outcome` on `resolution.json` |
| `S_t` | the last `chainlink` report with `timestamp <= (T0 + t) * 1000` | `chainlink.jsonl.gz` |
| `m_r` | the **time-weighted** mean of the `chainlink` step function over `[T0 + 240, T0 + t]`, seeded by the last report at or before `T0 + 240`. Used only at `tau < 60`. | `chainlink.jsonl.gz` |
| `sigma_live` | realised per-second dollar volatility over `[T0 - 300, T0 + t]`: a one-second grid of the `chainlink` step function, first differences `d`, `sigma = sqrt(sum(d^2) / n)`. Causal, moves as the interval runs. | `chainlink.jsonl.gz` |
| `sigma_pre` | the same estimator over `[T0 - 300, T0]`, fixed for the interval | `chainlink.jsonl.gz` |

The run-up window `[T0 - 300, T0]` is read from the **preceding** interval's directory, whose
window extends to `T0 - 300 + 330`; where both directories cover an instant, the readings are the
same feed and are merged by `timestamp`, deduplicated.

A step function between two reports is what an event feed's price **is** between them, and reading
it that way is not gap-filling. A report that never arrived is never invented, and no value is
carried across a stream gap the manifest records as a disconnect.

## 4. The scoring set

Ordered by `T0`, from the earliest interval directory on the host. An interval **qualifies** when
all of the following hold, each mechanical:

1. `manifest.json` is present and its `complete` is true;
2. `resolution.json` carries a decided outcome — `manifest.resolved_outcome` is not `None`;
3. `resolution.json` carries a non-null `events[0].eventMetadata.priceToBeat`;
4. `twap60` carries at least one report with `timestamp >= T0 * 1000`;
5. `chainlink` carries at least one report at or before `T0 - 300` and at least one at or before
   `T0 + 290`.

`quotes_complete` is **not** a qualifying condition and is not read. The clock offset is **not** a
qualifying condition: this TZ makes no latency claim, and intervals captured before `4216c04`
carry the System Map §7 item 10 artefact.

**Set size: the first 400 intervals that qualify.** If fewer than 400 qualify across the whole
capture, the report is **BLOCKED** and states the counts by failure reason. The set is never
shrunk to fit what is there.

Every unit considered is disclosed in `T0` order, one row each, members and non-members alike,
with the reason each non-member was excluded. Anti-cherry-picking is the disclosure, never
continuity: the set may span any number of restarts, disconnects and commits.

## 5. Repairs

**R-c — `analyze.py` cannot run (System Map §7 item 12).** Line 207 asserts that no start record
follows the `3895356` start. The TZ-05a restart made that permanently false, so the instrument
behind the Phase 0 count is dead.

The assert encoded a real guarantee — that the analysis does not score across a restart boundary —
and the repair keeps it while dropping the impossibility. Anchor on the identity of the analysis's
own start record and **bound the span at the next start record** instead of asserting there is
none: keep the existing assert that exactly one start exists on `RECORDER_SHA`, compute the next
start's `recv_ns` where one exists, and require every scored interval's window to close before it.

**Acceptance for R-c: the repaired analyzer reproduces TZ-04b exactly** — 215 units considered,
200 members, 15 non-members with the same reasons, R1 200 of 200, R2 175 of 200, R3 181 of 200.
Any difference is reported as a count and is a finding, not something to correct. The committed
TZ-04b report is not edited.

Self-tests for R-c go in `research/recorder/selftest.py`, which must still pass whole.

## 6. Validation

**Written by the Architect. The Executor runs these and does not design, extend, relax or
substitute them.** Every result is a **count**.

**P — precondition, evaluated and reported before any calibration score exists.** Reconstruct the
trailing 60-second average at the close from the `chainlink` feed alone, over `[T0 + 240, T0 +
300]`, by the same machinery §3 uses for `m_r`, and compare its sign against `K` with the venue's
resolved outcome. **At least 396 of the 400 must agree.** TZ-04b reached 200 of 200 using the
settlement feed's own reports; a reconstruction one step removed from that feed is allowed a 1%
shortfall and no more. **If P fails, the `chainlink` feed does not support the averaging the model
requires: the report states the counts, the gate below is not evaluated, Phase 1 stays open, and
the report proposes nothing.**

| # | check | reported as |
|---|---|---|
| V1 | set formation | every unit considered, in `T0` order, member or not, with the reason for each non-member; the member count; the counts by failure reason |
| V2 | feed adequacy | for `chainlink` and `twap60`: median and maximum gap between consecutive report timestamps inside `[T0 - 300, T0 + 300]`, over the members. Plus P's counts and the reconstruction residual against the venue's own `twap60` report at the close — median absolute and worst, in USD |
| V3 | `K` reconstruction | reconstructed `K` against the captured `priceToBeat`, judged by `published_equal`: count equal, median absolute residual, worst residual, in USD. No threshold — it extends TZ-04b's 198 of 200 to 400 |
| V4 | causality by perturbation | for the first 20 members and every scored `tau`: perturb every `chainlink` and `twap60` report timestamped after the checkpoint instant and require bit-identical `p_fair`; plus a negative control perturbing the last readable report, which must change it. Both counts |
| V5 | the model at realistic magnitudes | analytic self-tests in `research/selftest-pfair.py`, every fixed expectation at `K` near `100,000` and never at 0: the branches agree at `tau = 60`; at `tau >= 60` the realised path has zero weight; at `tau < 60` the realised mean enters with weight `(60 - tau) / 60`; `p_fair` moves the right way in `state` and in `sigma`. Each an assert that aborts the run |
| V6 | **calibration, `sigma_live` — the gate** | per scored `tau`: `n`, the observed Up rate, `Brier(p_fair)`, `Brier(constant)`, and the ten fixed bins with `n`, mean prediction, observed Up count and the interval bounds |
| V7 | `tau = 10` | the same table, **no threshold attached** |
| V8 | `sigma_pre` | Brier and failing-bin counts at every scored `tau`, **no threshold attached** |
| V9 | R-c | the reproduction counts of §5 |
| V10 | determinism | a second full run produces byte-identical output |

**Forensics.** The pipeline writes one row per scored observation — `T0`, `tau`, `K`, `S_t`,
`m_r`, `sigma_live`, `sigma_pre`, `state`, `sd`, `p_fair`, label — to
`/root/tz06-work/tz06-observations.csv`, outside the repository. The report states its path, line
count and `sha256sum`, so any single row is reconstructible without re-running anything.

### The gate — fixed here, before any data is seen

Scored `tau ∈ {240, 180, 120, 90, 60, 30}`: the decision window. `tau = 10` is measured and
carries no threshold. The gate reads `sigma_live` only; `sigma_pre` is reported alongside and
cannot rescue or condemn anything. *(Decided here rather than after the fact: gating on whichever
variant scores better would be tuning.)*

- **G1 — the pricer must beat a constant.** At every one of the six taus,
  `Brier(p_fair) < Brier(c)`, where `c` is the observed Up rate over the 400.
- **G2 — calibration.** Fixed bins `[0, 0.1), [0.1, 0.2), … [0.9, 1.0]`. A bin is **eligible**
  when it holds at least 20 of the 400. An eligible bin **fails** when its observed Up count falls
  outside the central 99% region of `Binomial(n, p̄)`, `p̄` the mean prediction in that bin,
  computed exactly rather than by a normal approximation. **Across the six taus, at most 2
  eligible bins may fail.**

Either one violated → **Phase 1 answers no**, the pricer is disqualified, the report states the
counts and proposes nothing. A failed gate is a valid, useful and cheap result.

No bin edge, no set size, no tau list and no threshold moves after this file is committed.
Passing both does not confirm an edge and licenses no engine work: Phase 2 remains the decision
point.

## 7. Deliverable

The report contains, and contains nothing else of substance:

1. the fingerprint table — `wc -l` and `sha256sum` for `SYSTEM-MAP.md` and for every file the
   map's fingerprint table lists at authoring time, plus the post-change hashes of the two files
   §0 authorizes;
2. the host gate's three observed values;
3. the §4 set disclosure;
4. P and V1–V10, as counts;
5. the gate arithmetic in full, re-derivable by hand from the tables printed;
6. the branch, the implementation commit and the pull request.

Publication is part of execution: a run that exists only on the VPS has not been delivered.

## 8. What this TZ deliberately does not contain

**No quote is read**, so the Phase 2 gate is still unwritten by someone who has seen no market
data. **No market statistic**, no depth, no fee applied to anything, no engine, no deployment.
Merge is deployment and there is nothing here to deploy: passing does not make `p_fair` live.
