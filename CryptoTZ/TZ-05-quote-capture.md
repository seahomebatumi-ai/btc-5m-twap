# TZ-05 — Quote Capture

**Canonical filename:** `TZ-05-quote-capture.md` — the Executor names the committed file from this
line and from no other source.

| item | value |
|---|---|
| destination | `CryptoTZ/TZ-05-quote-capture.md` |
| report | `CryptoReports/TZ-05-quote-capture-report.md` → straight to `main` |
| code | `research/recorder/**` → branch `tz-05-quote-capture`, from `main` after PR #3 → PR. **Never straight to `main`.** |
| Executor model | **Opus** — it changes a running capture process and touches clock discipline |

## 0. Fingerprint gate

| anchor | required value |
|---|---|
| System Map revision | `2026-09-11-b` |
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-open / 2-not-started` |
| `A4` — executor contract | `437b45ea196b` |

Any mismatch → **BLOCKED** before any work, with the computed values reported and nothing else
done.

---

## 1. Why this TZ exists

Phase 0 is closed: the venue settles on the 60-second Chainlink TWAP at the close against the same
feed at the open, measured 200 of 200. Phase 2 asks where the **market** quotes relative to that,
and Polymarket quotes are archived nowhere. Every interval not captured is gone.

The full order-book stream costs a measured `1,913,827,421` bytes per day compressed against
`8,489,132,032` bytes free — 4.4 days. It is therefore not captured. What Phase 2 needs is not the
firehose but the executable quote at the moments a decision would be taken, so this TZ captures
exactly that: a full book snapshot at seven fixed points in each interval, `14` HTTP reads per
interval, a measured `~2.4` MB per day. Architect's decision; the discarded alternative is a block
storage volume plus continuous depth capture, which buys Phase 3 data before Phase 2 has a result.

This TZ also repairs the two defects the TZ-04b report surfaced — System Map §7 items 9 and 10.

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

## 6. Validation

**Written by the Architect. The Executor runs these and does not design, extend, relax or
substitute them.** Every result is a **count**.

Scored over the first **200 intervals** whose whole window lies after the Tier C restart record,
disclosed in order, members and non-members alike, exactly as TZ-04b §6 required.

| # | check | reported as |
|---|---|---|
| W1 | quote completeness | of 200 intervals: how many have `quotes_complete`; for the rest, the count of missing reads broken down by `tau`, by token, and by HTTP status |
| W2 | checkpoint timing | over all successful reads, the distribution of `quote_offsets_ms` — min, p50, p90, p99, max — reported per `tau` |
| W3 | venue parameters | tick size, fee rate, token ids and outcome labels, each with its source field |
| W4 | footprint | bytes per interval for `quotes.jsonl.gz`, raw and compressed, and the projected bytes per day; free space at the restart and at authoring, in exact bytes |
| W5 | read-only proof | the §5 R-a command and its match count |
| W6 | clock, after R-b | samples accepted and rejected per server, rejection reasons with counts, and mean and maximum absolute offset over accepted samples only |
| W7 | determinism | the TZ-04b manifest rebuild, re-run over the 200 disclosed intervals, `sha256sum` before and after |

## 7. What this TZ deliberately does not contain

**No Phase 2 gate, and no number from which one could be chosen.** The gate is a threshold plus a
sampling rule, and the CANON fixes both before any score exists. It will be stated in the TZ that
first aggregates these quotes, before that aggregation runs — which is possible only because this
TZ aggregates nothing. That is why §2 forbids reporting even a spread.

**No pricer.** `p_fair` is corrected and validated in TZ-06, against venue-resolved labels.

**No depth or latency work.** Phase 3 needs the full book and a clean clock; it gets neither until
Phase 2 has a result worth executing on.
