# TZ-05a — Quote Capture, deployment only

**Canonical filename:** `TZ-05a-quote-capture-deploy.md` — the Executor names the committed file from this
line and from no other source.

| item | value |
|---|---|
| supersedes | `TZ-05-quote-capture.md`, which stays committed and unedited, as does its BLOCKED report |
| destination | `CryptoTZ/TZ-05a-quote-capture-deploy.md` |
| report | `CryptoReports/TZ-05a-quote-capture-deploy-report.md` → straight to `main` |
| code | `research/recorder/**` → branch `tz-05a-quote-capture`, from `main` → PR. **Never straight to `main`.** |
| Executor model | **Opus** — it changes a running capture process and touches clock discipline |

## 0. Fingerprint gate

| anchor | required value |
|---|---|
| System Map revision | `2026-09-11-c` |
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-open / 2-not-started` |
| `A4` — executor contract | `437b45ea196b` |

**Host gate.** This TZ modifies the running capture process, so it executes on the capture host and
nowhere else. Before any other work, check all three, mechanically:

| check | required |
|---|---|
| `/var/lib/btc-recorder/` | exists, and holds interval directories |
| the recorder process | running, and its commit recorded in the newest `runtime.jsonl` start record |
| the filesystem holding that path | device `/dev/vda2`, total exactly `31,612,203,008` bytes — System Map §6 |

Any mismatch, on the anchors or on the host gate → **BLOCKED** before any work, with the three
observed values reported and nothing else done.

---

## 1. Why this TZ exists

TZ-05 was blocked twice over, and only one of the two was routing. The `EXECUTE` trigger reached an
ephemeral cloud container instead of the VPS — that is fixed by the host gate above and by the
delivery block. The second is mine: **TZ-05 required a restart of the capture process and then
scored 200 intervals captured after that restart.** Sixty thousand seconds must pass between the
two, so no session could ever satisfy it, on any host.

The split is therefore permanent, not a workaround:

- **This TZ deploys.** It adds Tier C, applies both recorder repairs, restarts the process, and
  proves the deployment works over the first four intervals. Minutes, not hours.
- **TZ-05b scores.** It defines its set from the restart record this report names, and runs when
  the capture exists. It is written after this report, because the commit it anchors on does not
  exist yet.

Why Tier C at all: Phase 0 is closed and Phase 2 asks where the market quotes. Polymarket quotes
are archived nowhere, so every interval not captured is gone. The full order book costs a measured
`1,913,827,421` bytes per day compressed against `8,489,132,032` free — 4.4 days — so it is not
captured. Seven snapshots per interval are what a Phase 2 decision actually reads, and they cost
about `2.4` MB per day.

## 2. Scope

Read-only capture, integrity accounting, and the two repairs in §5. Nothing else.

**Not in scope, and their appearance in the diff is grounds for rejection:** any order path, any
CLOB authentication, any wallet, key, signer or credential; any pricing arithmetic; any label; any
Parquet conversion; any file under `engine/`; any edit to `research/twap-divergence.py` or
`research/selftest-twap-divergence.py`; any Release upload; any deletion of anything on the host
the recorder did not write.

**And one more, which is the point of §7:** no aggregation and **no market statistic of any kind**.
Not a spread, not a mid, not a depth figure, not a distribution over any quoted quantity. The
report states completeness, timing, venue parameters and bytes — nothing that could be used to
choose a Phase 2 threshold.

## 3. Tier C — quote snapshots

Tier A continues unchanged. Tier C is added to the same process.

**Token ids** come from the Gamma document already captured as S6, which carries both
`clobTokenIds` and `outcomes`. The report states which field maps to which outcome, verbatim.

**Checkpoints.** For each live market, at `tau ∈ {240, 180, 120, 90, 60, 30, 10}` seconds
remaining — that is `t ∈ {60, 120, 180, 210, 240, 270, 290}` — issue one `GET` to the CLOB REST
order-book endpoint for **each** of the two token ids. Fourteen reads per interval.

The endpoint and its parameter form are read from the current Polymarket documentation at
implementation time and stated verbatim in the report. Do not carry a URL from memory.

**Storage.** One file per interval, alongside the Tier A streams, in the same line format as every
other stream — `recv_ns`, `mono_ns`, and the response body verbatim, unparsed and unrounded — plus
`tau`, `token_id` and the HTTP status on each line:

```
/var/lib/btc-recorder/btc-updown-5m/<T0_epoch>/quotes.jsonl.gz
```

A non-200 response is stored as received with its status. A failed read is recorded, never retried
into the next checkpoint's slot and never filled.

**Manifest.** `manifest.json` gains `quotes_complete`, defined as **all 14 reads returned HTTP 200
and each response body parsed as JSON**, and `quote_offsets_ms`, the signed difference between each
read's `recv_ns` and its intended checkpoint instant. `complete` keeps its TZ-04b meaning and is
not touched — the two flags are independent, and Phase 2 membership will be defined from both in
the TZ that first aggregates.

**Floors.** Unchanged from TZ-04b §4: stop cleanly at `2_000_000_000` bytes free or
`4_000_000_000` bytes of cumulative capture, whichever first, checked before the first frame and at
every interval close. Tier A and Tier C together are measured at roughly 25 MB per day against
`8,489,132,032` free, so neither floor is near.

**Restart.** Adding Tier C restarts the recorder. That is safe: the Phase 0 scoring set is closed
and reported, so no set in flight depends on continuity. Write a restart record naming the new
commit, exactly as `3895356` did.

## 4. Venue parameters to capture

Recorded because CANON §1.4 lists them as unverified, and because they are venue constants rather
than market observations:

- the minimum tick size for these markets, from the Gamma document and from the book response;
- the published fee rate on the market document;
- the two token ids and their outcome labels.

The report states each as returned, once, with its source field named.

## 5. Repairs

**R-a — the read-only proof (System Map §7 item 9).** The TZ-04b instrument matched its own regex
and three docstrings that deny the capability, so it could never return zero. Replace it:

```
grep -rniE "(private[_-]?key|signer|create[_-]?order|post[_-]?order|api[_-]?secret|passphrase|l1[_-]?auth|l2[_-]?auth|wallet)" \
  research/recorder/ --include=*.py --exclude=analyze.py | grep -vE ':[[:space:]]*#|"""'
```

State the command and the number of matching lines. **A non-zero result is reported as returned and
never reworded away.** The excluded file is named in the report, and its own read-only status is
carried by the merge-base diff instead.

**R-b — SNTP reply validation (System Map §7 item 10).** The client accepts replies it must reject.
Reject, and count as rejected rather than as an offset, any reply with: leap indicator `3`, stratum
`0` or above `15`, a zero transmit timestamp, or a transmit timestamp more than `86_400` seconds
from the host clock. Rejections are counted per server and reported. Nothing is filtered after the
fact — the fix is at the point of reception.

## 6. Deployment validation

**Written by the Architect. The Executor runs these and does not design, extend, relax or
substitute them.** Every result is a **count**.

Scored over the **first four intervals** whose whole window lies after the Tier C restart record,
disclosed in order, one row each, members and failures alike.

| # | check | reported as |
|---|---|---|
| W1 | the restart | the restart record verbatim, the new commit sha, the process id and its start time, and confirmation that exactly one start record exists on that commit |
| W2 | reads | per interval and per `tau`: the HTTP status of each of the 14 reads, and how many intervals have `quotes_complete` |
| W3 | checkpoint timing | `quote_offsets_ms` for every successful read, per `tau` — min, median, max |
| W4 | venue parameters | tick size, fee rate, both token ids and their outcome labels, each with the source field named, exactly as §4 requires |
| W5 | footprint | bytes of `quotes.jsonl.gz` per interval, raw and compressed, the projected bytes per day, and free space before the restart and at authoring, in exact bytes |
| W6 | read-only proof | the §5 R-a command and its match count, reported as returned |
| W7 | clock, after R-b | SNTP samples accepted and rejected per server over the window, with rejection reasons and counts. A short window may yield few samples; report what there is |
| W8 | determinism | the manifest rebuild over the four intervals, `sha256sum` before and after |

**Acceptance, fixed here before any data is seen: at least one of the four intervals must have all
14 reads at HTTP 200.** One clean interval proves the code path end to end. If none does, the
report is BLOCKED and carries the failure counts by `tau`, by token and by status — and proposes
nothing. The other three intervals are reported as counts, with no threshold attached: this is a
deployment check, not a gate, and nothing here may be read as a market observation.

## 7. Deliverable

Report as soon as the fourth interval after the restart record has closed and its manifest is
written. **The recorder is left running.**

The report contains, and contains nothing else of substance:

1. The fingerprint table — `wc -l` and `sha256sum` for `SYSTEM-MAP.md` and for every file the map's
   fingerprint table lists at authoring time.
2. The host gate's three observed values.
3. W1–W8, as counts.
4. The order-book endpoint used, verbatim, and where in the current documentation it was read.

Publication is part of execution: a run that exists only on the VPS has not been delivered.

## 7. What this TZ deliberately does not contain

**No Phase 2 gate, and no number from which one could be chosen.** The gate is a threshold plus a
sampling rule, and the CANON fixes both before any score exists. It will be stated in the TZ that
first aggregates these quotes, before that aggregation runs — which is possible only because this
TZ aggregates nothing. That is why §2 forbids reporting even a spread.

**No scoring set, and no Phase 2 interval count.** TZ-05b does that, anchored on the restart record
this report names.

**No pricer.** `p_fair` is corrected and validated in TZ-06, against venue-resolved labels.

**No depth or latency work.** Phase 3 needs the full book and a clean clock; it gets neither until
Phase 2 has a result worth executing on.
