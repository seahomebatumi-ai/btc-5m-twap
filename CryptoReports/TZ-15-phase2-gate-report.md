# TZ-15 — the Phase 2 gate — report

**Executed.** Both scored runs completed, V1 … V12 all produced their counts, and no gate FAILed.
**One step is outstanding and it is a host permission, not a measurement:** §9 step 3's
`rm -rf /root/tz14-work` was refused by the session's classifier, and §15 hands the Boss the exact
block. Steps 1 and 2 of §9 both exited 0 and every file worth keeping is already in
`/root/btc-forensics/`.

**The reading is `UNDECIDABLE` at all five admitted `tau`.** No `tau` reads EDGE: the number of
selected trades that won fell short of the critical count at every one of them. No `tau` reads
NO EDGE either, and that was fixed before any label existed: the exact `POWER` against "the pricer
is right" is `0.33 … 0.47` at `k = 1`, below §4's `0.8` floor at all five. **Phase 2 is not decided
by this run.** The projection says a decision costs `k = 2` more capture at `tau` 90 and `k = 3` at
the other four.

| | |
|---|---|
| instrument | `research/tz15-phase2-gate.py`, 1,517 lines, 73,799 bytes |
| SHA-256 on the branch | `66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3` |
| branch / commit | `tz-15-phase2-gate` at `f7f171a2e1e8b4b3eafa810f5022f1ca1c5a65b1` |
| pull request | **#16**, open, not merged by the Executor |
| scored runs | 2, byte-identical on all five compared files (V3) |
| session wall clock | **627.2 s** over five runs, against `tz12.SESSION_CEILING_S` = `3,600` |

---

## 0. Gates, host, interpreter, refs, trees

### 0.1 Fingerprint — asserted inside the instrument as step 0 of §5.1

`SYSTEM-MAP.md` was read in the checkout the instrument runs from — `/root/tz15-work/wt`, a branch
cut from `origin/main` after revision `2026-09-19-a` landed.

| check | required | read | result |
|---|---|---|---|
| revision string | `2026-09-19-a` | `2026-09-19-a` | **match** |
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` | match |
| `A2` — collector | `6c5089330629` | `6c5089330629` | match |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-inventory-complete` | same | match |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b` | match |
| `A5` — recorder | `9fd1c7de0f74` | `9fd1c7de0f74` | match |
| `A6` — pricer | `729f0bcdbee3` | `729f0bcdbee3` | match |

**6 of 6 anchors matched.** The four that are the first 12 hex characters of a committed file's
SHA-256 were also **re-derived from those files' bytes**, as TZ-14 did:

| anchor | path | first 12 hex of SHA-256 |
|---|---|---|
| `A2` | `research/twap-divergence.py` | `6c5089330629` |
| `A4` | `BTC-EXECUTOR-INSTRUCTIONS.md` | `437b45ea196b` |
| `A5` | `research/recorder/recorder.py` | `9fd1c7de0f74` |
| `A6` | `research/pfair.py` | `729f0bcdbee3` |

Every row of the §0 fingerprint table was hashed in lines, bytes and SHA-256 through
`tz14.fingerprint_rows()`: **21 of 21 `frozen` rows equal the hashes printed there, 2 of 2 `tracked`
rows reported with no expectation, and `SYSTEM-MAP.md` itself reported (1).** No `frozen` mismatch,
so the BLOCKED path did not fire. The expected revision, the six anchors and the count `21` are
literals of the instrument — the gate never read its own expected values from the file it checks.
**`tz14.v1_gates` was not called**: it asserts revision `2026-09-18-b` and twenty rows.

### 0.2 Host gate — all three met

| condition | read |
|---|---|
| `/var/lib/btc-recorder/btc-updown-5m/` holds interval directories | **2,573** at the scored run 1 listing, taken **2026-09-19T08:10:02Z**; first `T0` `1789033800`, last `T0` `1789805400`. Run 2's listing, **2026-09-19T08:12:18Z**: **2,573**, first `1789033800`, last `1789805400`. The Executor's own shell listing at **2026-09-19T07:39:40Z**: **2,567**, first `1789033800`, last `1789803600` |
| a recorder process is running and the newest `runtime.jsonl` start record carries sha `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` | **pid 228592**, start sha `4216c04673ced76b5b2ac60ef57c9abedc46f9b9`, `recv_ns` **`1789206785264516934`** |
| the filesystem holding it is `/dev/vda2`, total `31,612,203,008` bytes | `/dev/vda2`, **31,612,203,008** bytes |

The recorder was never signalled, stopped or restarted. Its working directory is
`/root/btc-5m-twap/research/recorder`, which is why the report below was committed from a detached
worktree and that checkout's working tree was never switched.

### 0.3 Interpreter

Every command of the instrument ran on `/root/tz01-env/venv/bin/python`.

- **Python `3.12.3` (main, Aug 31 2026, 10:18:26) [GCC 13.3.0]** — 3.12.x as required.
- **`numpy` `2.5.3`**; `import numpy` succeeded, because the committed chain the instrument loads
  imports it. The instrument itself computes nothing in `numpy`.

### 0.4 Resource floor — exact bytes, both bounds asserted

`tz11a.FLOOR_START_BYTES` = **2,060,000,000** at run start, `tz11a.FLOOR_BYTES` = **2,000,000,000**
at every later read. **Fifteen reads over five runs, every one asserted, every one through
`tz11a.host_read`**; the lowest free-space reading of the session was **13,757,030,400** bytes,
6.9 times the start floor.

| run | reader | UTC | free bytes | bound | asserted |
|---|---|---|---|---|---|
| dev 1 | `host_read("start", …)` | 2026-09-19T07:43:34Z | 13,764,177,920 | 2,060,000,000 | yes |
| dev 1 | `host_read("after the rows", …)` | 2026-09-19T07:45:27Z | 13,764,190,208 | 2,000,000,000 | yes |
| dev 1 | `host_read("end", …)` | 2026-09-19T07:45:38Z | 13,764,411,392 | 2,000,000,000 | yes |
| dev 2 | `host_read("start", …)` | 2026-09-19T07:46:01Z | 13,763,137,536 | 2,060,000,000 | yes |
| dev 2 | `host_read("after the rows", …)` | 2026-09-19T07:47:54Z | 13,762,838,528 | 2,000,000,000 | yes |
| dev 2 | `host_read("end", …)` | 2026-09-19T07:48:04Z | 13,762,486,272 | 2,000,000,000 | yes |
| dev 3 | `host_read("start", …)` | 2026-09-19T07:48:34Z | 13,761,171,456 | 2,060,000,000 | yes |
| dev 3 | `host_read("after the rows", …)` | 2026-09-19T07:50:31Z | 13,760,696,320 | 2,000,000,000 | yes |
| dev 3 | `host_read("end", …)` | 2026-09-19T07:50:42Z | 13,760,913,408 | 2,000,000,000 | yes |
| **scored 1** | `host_read("start", …)` | 2026-09-19T08:10:02Z | 13,758,611,456 | 2,060,000,000 | yes |
| **scored 1** | `host_read("after the rows", …)` | 2026-09-19T08:11:55Z | 13,758,873,600 | 2,000,000,000 | yes |
| **scored 1** | `host_read("end", …)` | 2026-09-19T08:12:06Z | 13,758,488,576 | 2,000,000,000 | yes |
| **scored 2** | `host_read("start", …)` | 2026-09-19T08:12:18Z | 13,757,308,928 | 2,060,000,000 | yes |
| **scored 2** | `host_read("after the rows", …)` | 2026-09-19T08:14:11Z | 13,757,390,848 | 2,000,000,000 | yes |
| **scored 2** | `host_read("end", …)` | 2026-09-19T08:14:22Z | 13,757,030,400 | 2,000,000,000 | yes |

### 0.5 Preflight, twice, 1,817 s apart

Read 1 at **2026-09-19T07:39:33Z** (epoch `1789803573`), before the build. Read 2 at
**2026-09-19T08:09:50Z** (epoch `1789805390`), before the first scored run. **Elapsed 1,817 s**,
above the required `1,800`.

| quantity | read 1 | read 2 | delta | bytes/day |
|---|---|---|---|---|
| `/dev/vda2` used (`df -B1`) | 16,408,260,608 | 16,417,656,832 | **+9,396,224** | **+446.8 MB/day** |
| `/dev/vda2` available | 13,768,073,216 | 13,758,676,992 | −9,396,224 | — |
| `du -sb /root/PROJECT_GAMING_PS5` | 377,747,683 | 377,910,258 | +162,575 | +7.73 MB/day |
| `systemctl is-enabled telemetry-watch.service` | `disabled`, exit **1** | `disabled`, exit **1** | unchanged | — |
| `systemctl is-active telemetry-watch.service` | `inactive`, exit **3** | `inactive`, exit **3** | unchanged | — |

**This run's own footprint, stated separately at both reads** (map §7 item 29):

| path | read 1 | read 2 | delta | bytes/day |
|---|---|---|---|---|
| `/root/tz15-work` | **did not exist** | 7,250,569 | +7,250,569 | +344.8 MB/day |
| `/root/.claude` | 133,322,853 | 133,930,657 | +607,804 | +28.9 MB/day |

**The residual is the capture's own drain and nothing else.** Of the +9,396,224 bytes `/dev/vda2`
used across the window, **+7,250,569 is `/root/tz15-work/` and +607,804 is `/root/.claude/`** —
both this session's — and +162,575 is `/root/PROJECT_GAMING_PS5`. That leaves **1,375,276 bytes**,
**65.4 MB/day**, for everything else in 1,817 s. TZ-09 measured the capture's drain at **86.3
MB/day**, which over this window is **1.82 MB**; the residual sits just under it. **Nothing is
draining the filesystem that this session did not put there.** The preflight gated nothing beyond
§0.4.

### 0.6 Refs — a difference, recorded, not BLOCKING

`git ls-remote origin` at **2026-09-19T07:39:40Z**, before the branch of §2 existed, returned
**19 refs**: `HEAD` and `refs/heads/main` both at
`041b5bc42e09e82e0ea858f06e41226f15ffc886`, fifteen `refs/pull/N/head` for N = 1 … 15, and
`refs/tags/tz-01a-dataset` with its peeled `^{}`.

**Map §1 records one branch, `main` at `93d13415b8f29cea6cc6626c86488676c6538dcf`. `origin/main` is
at `041b5bc42e09e82e0ea858f06e41226f15ffc886` — a difference, recorded here and not BLOCKING.** The
two commits between them are `704f3f3`, which replaced `SYSTEM-MAP.md` with revision
`2026-09-19-a`, and `041b5bc`, which uploaded `CryptoTZ/TZ-15-phase2-gate.md`. **`main` carries the
revision §0.1 requires**, so the exception clause does not fire; map §1's ls-remote was simply taken
at `93d1341`, before this revision's own upload landed.

The instrument's own read at step 0 of the scored runs, after the push, returned **22 refs** — the
19 above plus `refs/heads/tz-15-phase2-gate` at `f7f171a2…`, `refs/pull/16/head` at the same commit,
and `refs/pull/16/merge` at `9ccdedaa…`. `origin` carries exactly one branch besides this TZ's own.

### 0.7 The trees

| tree | required | read |
|---|---|---|
| `/root/tz13-work` | `test -e` exits non-zero — map §3 records TZ-14's §9 removing it | **exit 1, absent** ✅ |
| `/root/tz14-work/` | must exist; V4 reads a TZ-14 output from it before §9 reclaims it | **present**, 12 entries: `run1`, `run1.log`, `run2`, `run2.log`, `scratch`, `trial`, `trial2` … `trial6`, `wt` ✅ |

Both asserted inside the instrument at step 0.

---

## 1. §3.1 — the set, asserted by hash

`rows, members, doc = tz14.the_set(load_manifests())`, unchanged. It formed the first 1,200
qualifying slots with `T0 > 1789206600` through `tz06.scoring_set` and asserted its own five
conditions.

| assertion | required | read |
|---|---|---|
| `tz07b.member_list_sha(members)` | `baa5a9d26855ea7ff07d062437df60617ba3e4e70dd74b3ac455a8a71a9b3154` | **equal** |
| `len(rows)` — the units considered | `1296` | **1,296** |
| every member `T0` at most | `1789595400` | **max is 1789595400** |

1,200 members, 96 non-members, all 96 failing on `disconnect` alone — the same walk TZ-14 made.

---

## 2. §3.2 — the pricer at each checkpoint

For each member `tz11a.walk_member(t0, manifests, False)`, then
`tz11a.checkpoint_row(t0, "tz14set", tau, walked[tau])` at each `tau` in `ADMITTED`, and **the row
kept is the nine-key projection** `T0`, `tau`, `state`, `sigma_hat`, `admissible`, `sd_student`,
`z_student`, `p_t`, `label`. **6,000 pricer rows**, `1,200 × 5`. **No `AssertionError` came out of
`walk_member` in any of the five runs**, so the BLOCKED path at §3.2 was never reached.

**The admissible count at each `tau` equals TZ-14's, asserted:**

| `tau` | required (TZ-14 report §2.2) | read |
|---|---|---|
| 240 | 631 | **631** |
| 180 | 628 | **628** |
| 120 | 615 | **615** |
| 90 | 619 | **619** |
| 60 | 621 | **621** |

---

## 3. §3.3 — the quotes at each admitted checkpoint

`tz14.documents(t0)` and `tz14.quote_lines(config.interval_dir(t0))` per member; for each read at a
`tau` in `ADMITTED` whose `status` is `200` and whose `body_is_json` is true,
`tz14.touch_of(tz14.book_of(read["raw"]), D(str(book["min_order_size"])), D(str(book["tick_size"])))`
— the venue's own minimum size and tick from the same reply.

**Not one read was listed, counted or dropped: 0 reads were non-`200`, 0 had `ok` false, 0 lacked
`min_order_size` or `tick_size`, and 0 named a token outside the member's mapping.** TZ-14 found
none of these in this set and neither did this run. **12,000 admitted reads at full completeness,
12,000 read.**

---

## 4. §3.4 — the label-free report, per `tau`

Everything below was computed, printed and written to disk **before any label existed**.

| `tau` | admissible | eligible | selected | Up | Down | weekday | weekend | both edges positive | priced at or below `0.10` |
|---|---|---|---|---|---|---|---|---|---|
| 240 | 631 | **631** | **405** | 207 | 198 | 368 | 37 | 0 | 2 |
| 180 | 628 | **628** | **428** | 216 | 212 | 396 | 32 | 0 | 34 |
| 120 | 615 | **615** | **440** | 225 | 215 | 405 | 35 | 0 | 105 |
| 90 | 619 | **619** | **380** | 191 | 189 | 349 | 31 | 0 | 116 |
| 60 | 621 | **621** | **271** | 133 | 138 | 245 | 26 | 0 | 109 |

**Eligibility equals admissibility at every `tau`** — it was counted, not assumed, and P1 holds.
**Both edges are positive at no checkpoint at any `tau`**, which is what a two-sided binary pair
whose asks sum to at least one implies; §5.2 item 5's fifth case fixes the tie rule against a
synthetic book instead.

**The price paid and the edge `p_t` claims, over the selected members at that `tau`**

| `tau` | `n` | mean `a` | mean `q − a` | mean after fee | min `a` | 0.25 | median | 0.75 | 0.90 | 0.99 | max |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 240 | 405 | 0.533901 | 0.042838 | 0.029589 | 0.1 | 0.32 | 0.53 | 0.76 | 0.86 | 0.95 | 0.96 |
| 180 | 428 | 0.496495 | 0.041217 | 0.030813 | 0.02 | 0.2 | 0.41 | 0.83 | 0.94 | 0.98 | 0.99 |
| 120 | 440 | 0.436805 | 0.036447 | 0.028406 | 0.01 | 0.11 | 0.3 | 0.86 | 0.97 | 0.99 | 0.999 |
| 90 | 380 | 0.412429 | 0.039856 | 0.032501 | 0.001 | 0.08 | 0.26 | 0.86 | 0.98 | 0.996 | 0.999 |
| 60 | 271 | 0.378528 | 0.042532 | 0.036243 | 0.001 | 0.05 | 0.2 | 0.82 | 0.98 | 0.99 | 0.999 |

**The market's mid against `p_t`, over the eligible checkpoints whose Up book is two-sided at the
touch.** `D = p − (bid_up + ask_up) / 2`.

| `tau` | two-sided books | min `D` | 0.25 | median | 0.75 | max | market more confident |
|---|---|---|---|---|---|---|---|
| 240 | 631 | −0.32164628 | −0.02660973 | +0.00168087 | +0.02859334 | +0.31708373 | 300 of 631 (**0.4754**) |
| 180 | 625 | −0.25720016 | −0.02425745 | +0.00302929 | +0.02712734 | +0.40726506 | 338 of 625 (**0.5408**) |
| 120 | 558 | −0.16110807 | −0.02537020 | +0.00197190 | +0.02614962 | +0.14644957 | 331 of 558 (**0.5932**) |
| 90 | 474 | −0.43038402 | −0.02663312 | −0.00064366 | +0.02246992 | +0.18499352 | 294 of 474 (**0.6203**) |
| 60 | 311 | −0.39901168 | −0.02543324 | +0.00003954 | +0.02362899 | +0.27147884 | 184 of 311 (**0.5916**) |

The median deviation is within `0.003` of zero at every `tau`: `p_t` and the market's mid agree on
average and disagree by a few points of probability in each direction. **The market is the more
confident of the two at a majority of checkpoints at every `tau` but 240**, rising to 0.62 at 90.

---

## 5. §3.5 — the gate's constants, exact, on disk before any label

`U0 = pb_upper([a …])` under the null — a market calibrated at its own ask — and
`U1 = pb_upper([q …])` under the alternative — the pricer right — over the selected members in
ascending `T0`, all of it in `Decimal` at the 60 digits `pfair.py` sets. `s*` is the smallest `s`
with `U0(s) ≤ 0.01`; `FP = U0(s*)`; `POWER = U1(s*)`.

**`tz15-constants.json` was written at `2026-09-19T08:12:06Z` in scored run 1** (`08:14:22Z` in
run 2), before §3.6 began. The label read of that run is stamped at the same UTC second — step 8
ended at 124.7 s and step 10 began at 124.9 s, 0.2 s apart — so **the ordering is proven by the step
order and by the two `label is None` assertions that bracket the write, not by a clock that resolves
only to the second.** SHA-256
`e6a93f9371e9fb32404482dac7b542c330399117ba0cf93e466b846e5878dfd3` — **byte-identical across both
scored runs and all three runs without `--score`.**

| `tau` | `n` | `s*` | `FP` (exact) | `POWER` | `k = 2`: `s*` / `POWER` | `k = 3`: `s*` / `POWER` | smallest `k` at `0.8` |
|---|---|---|---|---|---|---|---|
| 240 | 405 | **238** | 0.007476034950 | **0.325740** | 462 / 0.678112 | 685 / 0.860367 | **3** |
| 180 | 428 | **232** | 0.008749059109 | **0.432618** | 452 / 0.778800 | 671 / 0.922855 | **3** |
| 120 | 440 | **210** | 0.007886034792 | **0.430438** | 409 / 0.775024 | 606 / 0.932298 | **3** |
| 90 | 380 | **173** | 0.006740872864 | **0.459935** | 335 / 0.836507 | 497 / 0.951694 | **2** |
| 60 | 271 | **115** | 0.008611872633 | **0.467276** | 223 / 0.777048 | 329 / 0.935187 | **3** |

`s* ≤ n` at every `tau`, so the `s* = n + 1` branch — a count no outcome can reach — did not fire
anywhere and every `FP` is a computed tail rather than a constructed zero. `FP ≤ 0.01` at all five.

**The instrument asserted, between the write and the label read, that every one of the 6,000 pricer
rows still carried `label is None`.** That assertion ran twice — once at step 7 and once at step 8,
after the constants file was closed.

**What the constants settled before any outcome was read: NO EDGE was unreachable.** `POWER` is
`0.33 … 0.47` at `k = 1`, below §4's `0.8` floor at all five `tau`. Under §4's table a `tau` can
therefore only read EDGE (if `S ≥ s*`) or UNDECIDABLE (if `S < s*`). **This was fixed by the
selection and the prices alone**, and it refutes P5 without reference to a single label.

---

## 6. §3.6 — the labels, read once

**The push precedes the label read, by 23 minutes and 48 seconds.**

| event | instant | evidence |
|---|---|---|
| `git push -u origin tz-15-phase2-gate` **completed** | **2026-09-19T07:48:18Z** | the Executor's own transcript, timestamped either side of the push; `git ls-remote` immediately after returned `f7f171a2e1e8b4b3eafa810f5022f1ca1c5a65b1  refs/heads/tz-15-phase2-gate` |
| **scored run 1** label read | **2026-09-19T08:12:06Z** | the ledger line and `tz15-run.json` |
| **scored run 2** label read | **2026-09-19T08:14:22Z** | the ledger line and `tz15-run.json` |

Before each read the instrument asserted that `HEAD` is contained in `origin/tz-15-phase2-gate` —
`git rev-parse HEAD` and `git branch -r --contains HEAD`, each a fixed argument list with no shell.
`git branch -r --contains` returned exactly `["origin/tz-15-phase2-gate"]` in both runs.

Then **`tz10b.m2_labels(sorted(E))`** was called **once**, where `E` is the union over `ADMITTED` of
the eligible members: **678 members**, `tz07b.member_list_sha(E)` =
`77944a015d4cff89583a95087bafd95097a2f037dc70cab195a61696bfc2dc36`.

**The ledger, printed whole** — `/root/tz15-work/label-ledger.jsonl`, two lines, one per scored run,
**both carrying the reported commit and no other**:

```
{"head": "f7f171a2e1e8b4b3eafa810f5022f1ca1c5a65b1", "member_list_sha256": "77944a015d4cff89583a95087bafd95097a2f037dc70cab195a61696bfc2dc36", "members": 678, "utc": "2026-09-19T08:12:06Z"}
{"head": "f7f171a2e1e8b4b3eafa810f5022f1ca1c5a65b1", "member_list_sha256": "77944a015d4cff89583a95087bafd95097a2f037dc70cab195a61696bfc2dc36", "members": 678, "utc": "2026-09-19T08:14:22Z"}
```

**No ledger line carries any other commit**, so V5's disclosure clause does not arise. The three
runs without `--score` stopped after §3.5 with their constants on disk and appended nothing.

---

## 7. §3.7 and §4 — the observed statistic and the reading

**`S` is the number of selected trades that won** — the label for `Up`, one minus the label for
`Down`. `T = (S − Σa) / n` is the gross profit per share, `T_fee = T − Σfee(a) / n` after the fee.

| `tau` | `n` | **`S`** | `s*` | `Σ a` | `Σ q` | win rate | mean `a` | mean `q` | **`T`** | **`T_fee`** | `FP` | `POWER` | **reading** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 240 | 405 | **210** | 238 | 216.2300 | 233.5794 | 0.518519 | 0.533901 | 0.576739 | **−0.015383** | −0.028631 | 0.007476034950 | 0.325740 | **UNDECIDABLE** |
| 180 | 428 | **211** | 232 | 212.5000 | 230.1412 | 0.492991 | 0.496495 | 0.537713 | **−0.003505** | −0.013909 | 0.008749059109 | 0.432618 | **UNDECIDABLE** |
| 120 | 440 | **190** | 210 | 192.1940 | 208.2308 | 0.431818 | 0.436805 | 0.473252 | **−0.004986** | −0.013027 | 0.007886034792 | 0.430438 | **UNDECIDABLE** |
| 90 | 380 | **164** | 173 | 156.7230 | 171.8683 | 0.431579 | 0.412429 | 0.452285 | **+0.019150** | +0.011795 | 0.006740872864 | 0.459935 | **UNDECIDABLE** |
| 60 | 271 | **99** | 115 | 102.5810 | 114.1073 | 0.365314 | 0.378528 | 0.421060 | **−0.013214** | −0.019504 | 0.008611872633 | 0.467276 | **UNDECIDABLE** |

`n ≥ 2` at every `tau`, so no ratio of §3.7 was printed as undefined and no denominator was empty.

### §4 — the reading, condition by condition

**Every `tau` falls through the same two rows of §4's table.** `n ≠ 0`, so not the first row.
`S < s*` at all five, so not EDGE. `POWER < 0.8` at all five, so not NO EDGE. **The condition that
left each `tau` UNDECIDABLE is `S < s*` and `POWER < 0.8`.**

| `tau` | `S` vs `s*` | margin | `POWER` vs `0.8` | which row |
|---|---|---|---|---|
| 240 | 210 < 238 | 28 short | 0.325740 < 0.8 | fourth |
| 180 | 211 < 232 | 21 short | 0.432618 < 0.8 | fourth |
| 120 | 190 < 210 | 20 short | 0.430438 < 0.8 | fourth |
| 90 | 164 < 173 | 9 short | 0.459935 < 0.8 | fourth |
| 60 | 99 < 115 | 16 short | 0.467276 < 0.8 | fourth |

**The family bound.** The exact per-`tau` `FP` sum to **`0.039463874347`** over the five `tau`. By
Bonferroni the probability of EDGE anywhere under the null is at most that, whatever the dependence
between the five — and the five tests are dependent, because the five `tau` of one member share one
outcome. The bound does not assume otherwise.

### The verdict

**Neither of §4's two closing verdicts applies.** No `tau` read EDGE, so Phase 2 does not read YES
anywhere and no confirmation TZ on the reserved span is triggered. Not all five read NO EDGE, so
Phase 2 does not read NO for the Student pricer either. **The third case holds: no `tau` is closed,
and every UNDECIDABLE `tau` carries the projection's multiple** —

| `tau` | multiple `k` at which `POWER ≥ 0.8` | what a decision there costs |
|---|---|---|
| 240 | **3** | three times 1,200 qualifying slots |
| 180 | **3** | three times 1,200 qualifying slots |
| 120 | **3** | three times 1,200 qualifying slots |
| 90 | **2** | two times 1,200 qualifying slots |
| 60 | **3** | three times 1,200 qualifying slots |

**`T_fee` is printed beside every reading as the first figure Phase 3 would start from, and it gates
nothing here.** It is negative at four of five `tau` and `+0.011795` per share at `tau` 90 — a figure
whose own gate did not clear, and which this TZ does not read as an edge.

### Influence — recorded, not a reading

With `x = y − a` per selected member, the member whose `|x − T|` is largest was removed — ties to the
smallest `T0` — and `S`, `s*`, `FP`, `POWER` and the reading recomputed exactly on the remaining
`n − 1`.

| `tau` | removed `T0` | side | `a` | `n − 1` | `S` | `s*` | `POWER` | reading | changed? |
|---|---|---|---|---|---|---|---|---|---|
| 240 | 1789583700 | Down | 0.94 | 404 | 210 | 237 | 0.327963 | UNDECIDABLE | no |
| 180 | 1789366200 | Up | 0.97 | 427 | 211 | 231 | 0.433716 | UNDECIDABLE | no |
| 120 | 1789561800 | Down | 0.99 | 439 | 190 | 209 | 0.430569 | UNDECIDABLE | no |
| 90 | 1789227300 | Up | 0.03 | 379 | 163 | 173 | 0.455688 | UNDECIDABLE | no |
| 60 | 1789227300 | Up | 0.02 | 270 | 98 | 115 | 0.465161 | UNDECIDABLE | no |

**No single member moves any reading.** The most influential trade at every `tau` is a long shot
taken at a price near `0` or near `1`, which is where one outcome moves `T` the most.

### Diagnostics — each barred from every reading

Over the eligible checkpoints whose Up book is two-sided at the touch, and the lag-1 autocorrelation
over the selected members in `T0` order.

| `tau` | two-sided books | mean label | mean mid | mean `p_t` | **Brier mid** | **Brier `p_t`** | lag-1 autocorrelation of `y` |
|---|---|---|---|---|---|---|---|
| 240 | 631 | 0.502377 | 0.494754 | 0.495415 | **0.194343** | 0.197496 | −0.070791 |
| 180 | 625 | 0.508800 | 0.485666 | 0.487175 | **0.162310** | 0.163895 | +0.044270 |
| 120 | 558 | 0.501792 | 0.470655 | 0.472166 | **0.130165** | 0.132436 | +0.020378 |
| 90 | 474 | 0.510549 | 0.495018 | 0.492654 | **0.112033** | 0.112809 | +0.129100 |
| 60 | 311 | 0.508039 | 0.494484 | 0.493637 | **0.075900** | 0.079970 | +0.138468 |

**The market's mid beats `p_t` on the Brier score at all five `tau`**, by `0.0008` to `0.0041`.
Each autocorrelation is defined — three or more selected members and a `y` that is not constant at
every `tau`. **The lag-1 autocorrelation of `y` is small and positive at four of five `tau`, largest
at `tau` 60 (`+0.138`) and 90 (`+0.129`).** §4 assumes the outcomes of different intervals are
independent given the market's prices; this is the figure that bears on it, and it gates nothing.
A positive dependence of this size would make the true tail slightly heavier than the exact
binomial one, which pushes against EDGE and not toward it — so it cannot have manufactured a reading
this run did not make.

---

## 8. §3.8 — the five pre-registered predictions, barred from every gate

| # | prediction | population | observed | verdict |
|---|---|---|---|---|
| **P1** | the eligible count equals the admissible count at every `tau` in `ADMITTED` | admissible members per `tau` | 240: 631 of 631; 180: 628 of 628; 120: 615 of 615; 90: 619 of 619; 60: 621 of 621 | **held** |
| **P2** | at `tau = 60` more than half of the selected trades are priced at or below `0.10` | selected members at 60 | **109 of 271** — 40.2%, not a majority | **refuted** |
| **P3** | at `tau = 60` the selected trades win less often than their prices implied: `S < Σ a` | selected members at 60 | **`S` = 99 against `Σ a` = 102.581** | **held** |
| **P4** | no `tau` reads EDGE | the five readings | all five UNDECIDABLE | **held** |
| **P5** | at least one `tau` reads NO EDGE — the gate has the power to decide somewhere | the five readings | **none does**; `POWER` is `0.33 … 0.47` against a `0.8` floor | **refuted** |

**Which part of the basis failed, and which held.** §3.8's basis was that TZ-13 put `λ̂` at `0.7436`
at `tau = 60` — the Student scale too wide there, overpricing long shots — and that TZ-14 found half
the admissible checkpoints at 60 one-sided, books where the only trade is the long shot.

- **The direction held.** P3 is the direct test of "the pricer buys long shots it overrates and they
  lose", and at `tau` 60 the selected trades won 99 times against 102.58 implied by their prices.
  `T` is negative at four of the five `tau`.
- **The share failed.** P2 assumed the one-sided long shot would dominate *selection* at 60. It
  dominates the *book* — the median price paid at 60 is `0.20` and the lower quartile `0.05` — but
  the selection rule also takes near-certain sides at `0.98` and `0.99`, and 162 of the 271 selected
  trades at 60 are priced above `0.10`. The prediction confused the shape of the book with the shape
  of the selection.
- **P5 failed on power, not on direction.** It assumed the gate would be able to close somewhere.
  It cannot at `k = 1`: the pricer's own claimed edge — a mean `q − a` of `0.036` to `0.043` — is
  too small relative to the binomial spread at `n = 271 … 440` for `U1(s*)` to reach `0.8`. **This
  was computable before any label existed and is recorded in `tz15-constants.json`.**

---

## 9. Implementation

| | |
|---|---|
| file | `research/tz15-phase2-gate.py` — **one new file and nothing else** |
| lines / bytes | 1,517 / 73,799 |
| SHA-256 on the branch | `66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3` |
| branch | `tz-15-phase2-gate` |
| commit | `f7f171a2e1e8b4b3eafa810f5022f1ca1c5a65b1` |
| merge base | `041b5bc42e09e82e0ea858f06e41226f15ffc886` |
| pull request | **#16** — open, **not merged by the Executor** |

**The load, and its named side effects.** The instrument sets `OPENBLAS_NUM_THREADS`,
`OMP_NUM_THREADS` and `MKL_NUM_THREADS` to `"1"`, then loads `tz14-quote-inventory.py` **once**
through an `importlib` helper of the same shape as `tz11a._load`, and takes `tz12`, `tz11a`,
`tz10b`, `tz07b`, `tz06`, `pfair`, `config`, `D` and `load_manifests` from that one module object;
`analyze` and `manifest` are then imported by name. **Nothing is loaded a second time.** `tz14`'s
module body writes the same three environment variables and installs an audit hook that records the
basename of every open under the capture root for the life of the process; nothing can remove it,
and this instrument never reads `tz14.CAPTURE_OPENS`. **The instrument installs its own hook**,
which records the absolute path, the mode and the current step of §5.1. `tz14.v1_gates`,
`tz14.selftests`, `tz14.build` and `tz14.main` were never called.

**The order of a run, asserted, as the step marks from scored run 1 show:**

```
step 0 gates at 0.6 s
step 1 host read 1 at 0.6 s
step 2 self-tests at 1.0 s
step 3 v6 and v2 static at 1.1 s
step 4 the set at 20.5 s
step 5 the rows and host read 2 at 114.0 s
step 6 the quotes and V4 (c) at 118.4 s
step 7 selection and the first label-free assertion at 118.5 s
step 8 the constants and the second label-free assertion at 124.7 s
step 10 the label read at 124.9 s
step 11 the statistic, the readings and the verdict at 125.3 s
step 12 V4 (d) at 125.3 s
step 13 host read 3, V9 and the files at 125.5 s
elapsed 125.5 s, peak RSS 86412 kB
```

Step 9 is absent because that is the stop for a run without `--score`; the three development runs
show `step 9 host read 3 and V9` and no steps 10 to 13.

---

## 10. §6 — cost, measured against the table

| step | §6 stated | measured (scored run 1) |
|---|---|---|
| gate, self-tests, `v6`, static `v2` | ~15 s | **1.1 s** |
| the set, §3.1 | ~18 s | **19.4 s** |
| the rows, §3.2 | ~100 s | **93.5 s** |
| the quotes, §3.3, and V4 against TZ-14 | ~11 s | **4.4 s** |
| the recursions, §3.5 and §3.7 | ~47 s | **6.3 s** at §3.5 (`n` = 271 … 440, not the unfiltered 1,200) |
| the labels, V4 against TZ-13, tables, host reads | ~25 s | **0.8 s** |
| **one scored run** | **~216 s** | **125.5 s** (run 2: **125.1 s**) |
| **the session** | **~870 s** | **627.2 s** — dev 124.4 + 124.5 + 127.7, scored 125.5 + 125.1 |

Against `tz12.SESSION_CEILING_S` = `3,600`, the session used **17.4%**. Peak RSS across the five
runs: **93,120 kB**. Nothing was sampled and no simulation was run: the constants are exact.

**Fail-fast 1, asserted.** Item 8 of §5.2 timed one recursion over 1,200 weights: **`t8` = 0.3775 s**
in scored run 1 and **0.3787 s** in run 2. The projection `215,976,010 × t8 / 1,440,000` is
**56.6 s** and **56.8 s**, against the **`950` s** bound. The host is about **1.22×** slower than the
Architect's machine per unit — **`2.6213e-7` s here against the Architect's `2.153e-7`, a ratio of
1.22** — well inside the 20× the bound admits.

**Fail-fast 2, asserted.** Elapsed after §3.2 was **114.0 s** in run 1 and **113.9 s** in run 2,
against the **`600` s** bound. §6's table put it at about 133 s.

---

## 11. Validation — V1 … V12

| # | check | what it produced |
|---|---|---|
| **V1** | gates — **asserted, step 0** | **6 of 6** anchors, four of them re-derived from the files' bytes; **21 of 21 `frozen`**, **2 of 2 `tracked`**, 1 reported; **host 3 of 3** with the listing's instant (2,573 directories at 2026-09-19T08:10:02Z, first `1789033800`, last `1789805400`; pid 228592; start sha `4216c04673…`; `/dev/vda2` at 31,612,203,008 bytes); §0.6's 19 refs before the branch and 22 after; §0.7's two trees; Python 3.12.3 and `numpy` 2.5.3; **15 free-space reads, every one with its bound and every one asserted** — §0.4's table |
| **V2** | isolation — **asserted two ways** | **Static, step 3:** 1,311 string constants scanned with 40 docstrings exempt, **0** carrying any of `tz14.BANNED_SUBSTRINGS` (matched against that committed tuple; the instrument writes none of the three itself); 743 calls scanned, **0** of the twelve `pfair` entry points of §2 item 6; **exactly 1** call site of `tz10b.m2_labels`; **0** calls of `analyze.venue` and **0** of `tz11a.fit_student`. **At run time, from the instrument's own hook:** opens whose basename carries `tz14.BANNED_SUBSTRINGS[0]` during **steps 5 to 9: 0**; during **step 10: 678**, exactly the number of members passed to `tz10b.m2_labels`; the only other such opens are the **1,296 at step 4**, from `analyze.venue` inside `tz06.qualification`, which §2 item 5 names. **Every pricer row carried exactly §2 item 7's nine keys with `label is None` at steps 7 and 8 — 6,000 rows, twice** |
| **V3** | determinism — **BLOCKING on any difference, checked by `cmp` after the second scored run** | **PASS.** Two runs with `--score` from fresh processes on `f7f171a2…`: `tz15-constants.json`, `tz15-readings.json`, `tz15-tables.md`, `tz15-observations.csv` and `tz15-disclosure.md` **byte-identical by `cmp`**, SHA-256 pairs equal (see §12). `tz15-constants.json` is also **byte-identical to all three runs without `--score`** on that commit and to the two on the pre-commit tree. Wall clock 125.5 s / 125.1 s; peak RSS 86,412 kB / 90,444 kB. `tz15-run.json` holds instants and timings, is not compared, and is named here |
| **V4** | the inputs are the committed ones — **asserted** | **(a) step 4:** member-list SHA-256 `baa5a9d26855…` equal, **1,296** units considered, last member `1789595400`. **(b) step 5:** admissible **631 / 628 / 615 / 619 / 621** at `tau` 240 … 60, equal to TZ-14's. **(c) step 6:** `/root/tz14-work/run1/observations.csv`, SHA-256 `0fc46a68f923acbbb6839a781d92d9b4d2c5afa734d059fa59b49b6e10df5e3a` — **agrees at 12,000 of 12,000 admitted reads** on `outcome`, `bid5`, `ask5`, `sigma_hat` and `admissible`, each value formatted by `tz14.cell` and compared with the string that file holds; **0 cells differ**. **(d) step 12:** `/root/btc-forensics/tz13-work--run1--tz13-observations.csv` at SHA-256 `e78b01b5f06f485d15fe944fb37b17688507d278cb78add5143e12304a322f44`; its members with `T0 ≤ 1789595400` are **exactly** this set's **520** members with `T0 ≥ 1789428000`; **`repr(p_t)` equal at 2,600 of 2,600** checkpoints and **the label equal at 2,025 of 2,025** where one was read here; **0 differ** |
| **V5** | the push precedes the label read — **asserted, step 10** | `HEAD` `f7f171a2e1e8b4b3eafa810f5022f1ca1c5a65b1`, `git branch -r --contains HEAD` → `["origin/tz-15-phase2-gate"]`, in both scored runs. **Push completed 2026-09-19T07:48:18Z; label read 08:12:06Z and 08:14:22Z** — see §6's table. The ledger is printed whole above; **both lines carry the reported commit and no other**, so the disclosure clause does not arise |
| **V6** | the diff — **asserted, step 3** | merge base `041b5bc42e09e82e0ea858f06e41226f15ffc886`, head `f7f171a2e1e8b4b3eafa810f5022f1ca1c5a65b1`; `git status --porcelain` for the two scoped paths: **empty**; `git diff --name-only` names **exactly `research/tz15-phase2-gate.py`**; **0** attribute stores, **0** `global`, **0** `nonlocal` in the file's own tree; the `os.environ` writes are **exactly the three** — `MKL_NUM_THREADS`, `OMP_NUM_THREADS`, `OPENBLAS_NUM_THREADS`; the replaced-line list is **empty**, and the path does not exist at the merge base |
| **V7** | the self-tests — **asserted, step 2** | **7 of 7 items and 33 assertions, distributed 6, 3, 1, 3, 11, 4, 5.** Item 8's time: 0.3775 s (run 1), 0.3787 s (run 2). Output verbatim in §13 |
| **V8** | the frozen files are not moved — **asserted, steps 0 and 13** | `research/pfair.py` `729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68` and `research/tz14-quote-inventory.py` `978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02` — **equal to map §0 at run start and at run end**, in every run |
| **V9** | the capture is untouched — **asserted, step 13, or step 9 without `--score`** | `tz11a.host_read` at steps 1, 5 and 13. Between reads 1 and 3: pid **228592** unchanged, start record `4216c04673…` with `recv_ns` `1789206785264516934` unchanged, directory count **2,573 → 2,573** in run 1 and **2,573 → 2,574** in run 2 — risen, not fallen. Read-set SHA-256 `b0d41c1afccb8e3a09cf2baad50ceb619913ba76f36f00748abfd77ef102bea7` **unchanged between reads 2 and 3**, in both. From the hook: **14,435 opens in run 1, every one in mode `r`, none with `w`, `x`, `a` or `+`**; **0 opens of any file but `manifest.json` in a directory whose `T0` exceeds `1789669800`**. Opens per basename (run 1): `chainlink.jsonl.gz` 4,992; `gamma.json` 1,200; `manifest.json` 2,570; `quotes.jsonl.gz` 1,200; `resolution.json` 1,974; `runtime.jsonl` 3; `twap60.jsonl.gz` 2,496. **Everything the instrument can write, enumerated**: the six files of its `--out` directory and `/root/tz15-work/label-ledger.jsonl` |
| **V10** | the fingerprint table | §12 below — every row of map §0 in lines, bytes and SHA-256, with the new file beside them as it stands on the branch |
| **V11** | disclosure | `tz15-disclosure.md`: the **1,296 units in ascending `T0`** with UTC, weekday and reasons; per `tau`, the eligible and the selected `T0` lists each with its count and `tz07b.member_list_sha` (§12); and `tz15-observations.csv` — **6,000 rows plus a header, one per member per `tau` in `ADMITTED`**, carrying `T0`, `tau`, `sigma_hat`, `admissible`, `p_t`, `ask_up`, `bid_up`, `ask_dn`, `bid_dn`, `e_up`, `e_dn`, `selected`, `side`, `a`, `q`, `fee`, the label and `y` — **sufficient to reconstruct every number of §3.4, §3.5 and §3.7 without re-running** |
| **V12** | influence and diagnostics — recorded | §7's influence table beside each reading, §7's diagnostics, and §8's five predictions each marked held or refuted with the figure beside it |

### The member-list hashes of every disclosed population

| `tau` | eligible | `tz07b.member_list_sha` | selected | `tz07b.member_list_sha` |
|---|---|---|---|---|
| 240 | 631 | `d6f7181c46f679db0bb260962a7eee0fadc2c525b360f682a3b2f702f82e1be9` | 405 | `01de2a62ef220439eff393142d4e394f27d98f3fe163571b47aad2cf40a7c8d1` |
| 180 | 628 | `3dab9225e6756fa6f64a41628e908ff2875ceb1e9c18414db56cbb751255abca` | 428 | `7fdbff7f1ae25caf3c6b05754292a68c4440e07ce2c3b4488de8869fada06228` |
| 120 | 615 | `7d63458a55cef1bcccd8d1caec527a6363deda27bbe71e9959ccde54a9ad1247` | 440 | `55de8ccb01b32ef8b3223fb19e475f8715bb0efb9b9311c6b70f51eccc19b944` |
| 90 | 619 | `acc4861a77d7d7cc09b6c7bbe4c55b62999c3a6ca2d2b685603ec1adeb5a8a17` | 380 | `58eb4daaf0c8d563b0bf1bb4d3322ac5b730ff3eb0653bc9884e5b9032b2d25b` |
| 60 | 621 | `42d1cdffd55371928fe25f81622096c559f87e8bcd3da241f3fef6543d98603c` | 271 | `363da573872e773077ee4977265402fb691017ecae46a2c1fdfc25aa57ea9cd1` |

The union over `ADMITTED` of the eligible members — the 678 handed to `tz10b.m2_labels` — hashes to
`77944a015d4cff89583a95087bafd95097a2f037dc70cab195a61696bfc2dc36`.

---

## 12. V10 — the fingerprint table, as this run read it

`wc -l` and `sha256sum` for the map and every file its §0 table lists, read on the branch.

| path | lines | bytes | state | SHA-256 | equals the map |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 770 | 139,400 | reported | `7e3306e6b92551a178cb23292d526be881c5c848e394e47e7b4101b48acc6ec3` | — |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | yes |
| `research/twap-divergence.py` | 1,135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | yes |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | yes |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | — |
| `research/pfair.py` | 441 | 19,357 | frozen | `729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68` | yes |
| `research/selftest-pfair.py` | 619 | 32,559 | frozen | `b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa` | yes |
| `research/tz06-calibration.py` | 577 | 27,138 | frozen | `715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f` | yes |
| `research/tz07a-variance-time.py` | 623 | 28,414 | frozen | `513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771` | yes |
| `research/tz07b-settlement-dispersion.py` | 515 | 24,926 | frozen | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` | yes |
| `research/tz08a-out-of-sample.py` | 745 | 38,822 | frozen | `37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c` | yes |
| `research/tz09-disk-inventory.py` | 894 | 41,004 | frozen | `b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6` | yes |
| `research/tz10b-sigma-or-link.py` | 1,224 | 61,018 | frozen | `406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088` | yes |
| `research/tz11a-student-link.py` | 1,231 | 64,732 | frozen | `0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839` | yes |
| `research/tz12-sized-gate.py` | 1,157 | 61,637 | frozen | `d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999` | yes |
| `research/tz13-sized-gate-test3.py` | 1,074 | 53,901 | frozen | `a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd` | yes |
| `research/tz14-quote-inventory.py` | 2,124 | 109,972 | frozen | `978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02` | yes |
| `research/recorder/recorder.py` | 608 | 25,658 | frozen | `9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03` | yes |
| `research/recorder/config.py` | 112 | 4,773 | frozen | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | yes |
| `research/recorder/manifest.py` | 254 | 10,002 | frozen | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | yes |
| `research/recorder/analyze.py` | 813 | 34,705 | frozen | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` | yes |
| `research/recorder/probe.py` | 227 | 9,324 | frozen | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | yes |
| `research/recorder/selftest.py` | 573 | 30,591 | frozen | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` | yes |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | — |
| **`research/tz15-phase2-gate.py`** — **the new file, on the branch** | **1,517** | **73,799** | new | `66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3` | not in map §0 |

**21 of 21 `frozen` rows equal, 2 of 2 `tracked` reported, `SYSTEM-MAP.md` reported. Every `frozen`
row is byte-identical at run end to what it was at run start.**

### V3 — the compared files, both scored runs

| file | scored run 1 | scored run 2 | `cmp` |
|---|---|---|---|
| `tz15-constants.json` | `e6a93f9371e9fb32404482dac7b542c330399117ba0cf93e466b846e5878dfd3` | same | **identical** |
| `tz15-readings.json` | `85b90d8e6c4ec96004ddcc277e501b0394f6b952d739716aa620ab37a03f2e56` | same | **identical** |
| `tz15-tables.md` | `96953d02765b6deae6d799a22c333681d53f3e4cd9f64f982be01721a31a12ab` | same | **identical** |
| `tz15-observations.csv` | `a7ac8a495e00e21cd34af6ead7f05e9a2b741231c928bb61d4ec03ec0e610ce6` | same | **identical** |
| `tz15-disclosure.md` | `4d9f442507d34cac54480da69dc55b8728bbebf2372c7889ee5620682215b188` | same | **identical** |
| `tz15-run.json` | `e79d80967678cec754285fc42d8dd28cd203275f334ecf3d6457fa8bdc953f5b` | differs | **not compared** — it holds instants and timings, and is named here as §7 requires |

---

## 13. V7 — the self-tests, verbatim

```
item 1: pb_upper over four coins gives 5 tails, 1.000000, 0.953125, 0.703125, 0.296875, 0.046875 — 6 assertions
item 2: twenty fair coins give s* = 16, FP = 0.00590896606445312500, U(15) = 0.02069473266601562500 — 3 assertions
item 3: twenty coins at 0.8 give U(16) = 0.62964826390266904576 — 1 assertion
item 4: three coins at 0.9 give U(3) = 0.729, s* = 4, FP = 0 — 3 assertions
item 5: five selections — Up at 0.60, nothing, Down at 0.60, nothing, Up on the tie at 0.40 — 11 assertions
item 6: the guard passes two clean rows and raises on a label, on Y and on r — 4 assertions
item 7: five readings, the 0.8 floor inclusive — 5 assertions
item 8: one recursion over 1200 weights took 0.3775 s; the run projects 56.6 s of recursion against the 950 s bound
```

**7 of 7 items, 33 assertions, 6 + 3 + 1 + 3 + 11 + 4 + 5**, all run before anything was read from
the capture. The Architect's independent expectations were reproduced exactly: `61/64`, `45/64`,
`19/64` and `3/64`; `1549/262144` and `5425/262144`; `60047937765376 / 5^20`; `0.729`; and
`fee(0.60) = fee(0.40) = 0.0168`, `fee(0.41) = 0.016933` with every edge following by subtraction.

---

## 14. Publication and §4.2's separation self-check

Run verbatim, as the contract requires:

```
$ git rev-list origin/main | grep -c f7f171a2e1e8b4b3eafa810f5022f1ca1c5a65b1
0

$ git diff --name-only origin/main origin/tz-15-phase2-gate
research/tz15-phase2-gate.py

$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
(no output)
```

`main` does **not** carry the implementation commit; the branch differs from `main` by exactly one
implementation file; no dataset, archive or binary is in git history. **No Release was created.**
This report is the one path this TZ pushes to `main`, in one commit, as §2 item 2 and contract §4.1
require.

---

## 15. §9 — retention

Performed in order, each step only after the previous one exited 0, and **only after both scored
runs**.

### Step 1 — copy first. **205 → 211 files, 6 copied.**

Every file under `/root/tz14-work/` whose SHA-256 is named by any committed report on `main`, and
which `/root/btc-forensics/` did not already hold by hash, was copied there **by exclusive create**
(`O_CREAT | O_EXCL`), with the hash asserted at source and again at destination. **The predicate is
TZ-14's**: every 16-to-64 hexadecimal token in every `CryptoReports/*.md`, matched against both the
full SHA-256 and its 16-character prefix, because reports name some outputs by prefix alone and a
64-character match would miss them. **25 committed reports plus this one were scanned, yielding 519
distinct hex tokens.**

**86 files under `/root/tz14-work/` carry a SHA-256 a committed report names. 60 were already held
by hash. Of the remaining 26, 20 duplicate one another** — TZ-14's two scored runs and its six
trial directories left byte-identical copies of the same four outputs — **so 6 distinct files were
copied**, the first in sorted path order for each hash, and §9's own condition excluded the other
20 as soon as the first copy landed:

| copied as | SHA-256 | source |
|---|---|---|
| `tz14-work--run1--counts.md` | `4c81276eb3fe5b2972e4e719a29f2b12a508858421eaf63be43fc870c77766a2` | `run1/counts.md` |
| `tz14-work--run1--disclosure.md` | `a2b31f6a17fed4206f4875916fdad417f083e643f63834dfa3da32f6a01f90e0` | `run1/disclosure.md` |
| `tz14-work--run1--observations.csv` | `0fc46a68f923acbbb6839a781d92d9b4d2c5afa734d059fa59b49b6e10df5e3a` | `run1/observations.csv` — **the file V4 (c) read** |
| `tz14-work--run1--tables.md` | `4dec2387f5c692f3d9d37ddb72a00f64b419a8b45843de04ff9a4e22f4bf3e31` | `run1/tables.md` |
| `tz14-work--wt--SYSTEM-MAP.md` | `6096f0b8405dde9b996f074447af637e46f8b64318a61c57e9d34d23ad36476b` | `wt/SYSTEM-MAP.md` — revision `2026-09-18-b`, the revision TZ-14 was gated against |
| `tz14-work--wt--research--tz14-quote-inventory.py` | `978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02` | `wt/research/tz14-quote-inventory.py` |

**Assert that every file already there is unchanged: 205 of 205.** §9 names `205` as TZ-14's end
state and the count agreed exactly; all 205 were re-hashed after the copy and the 137 distinct
hashes over them are the same 137 read before it, with **0** files carrying content that was not
there before. **Before: 205 files. After: 211.**

The last two rows are also in git history — the map at `b2269bb2` and the instrument at `ffef5cd`
— so neither was at risk; §9's rule was applied as written rather than argued around.

### Step 2 — the worktree. **Exited 0, without `--force`.**

`git status --porcelain` in `/root/tz14-work/wt` printed **nothing** — unlike TZ-13's tree, it
carried no `__pycache__` — so `git worktree remove /root/tz14-work/wt` **exited 0 on the first
attempt and `--force` was never used**. `test -e /root/tz14-work/wt` then **exited 1**, and
`git worktree list` now shows three worktrees — `/root/btc-5m-twap`, `/root/tz15-work/wt` and
`/root/tz15-work/wt-report` — with no stale entry for the removed one.

### Step 3 — the tree. **BLOCKED: the session's permission classifier refused it.**

`rm -rf /root/tz14-work`, one command naming one tree, was **denied by the Claude Code auto-mode
classifier** with reason `[Irreversible Local Destruction]`. §9 anticipates exactly this and names
the remedy: hand the Boss one exact block and verify the outcome from `test -e` afterwards, **never
from his report** (map §6). **The block is below and the step is not complete.**

```
rm -rf /root/tz14-work
test -e /root/tz14-work ; echo "exit=$?   # 1 means the tree is gone"
```

**State at the moment of the refusal, for the Boss to compare against:** `test -e /root/tz14-work`
exits **0**; the tree holds **39,278,075 bytes** in eleven entries — `run1`, `run1.log`, `run2`,
`run2.log`, `scratch`, `trial`, `trial2`, `trial3`, `trial4`, `trial5`, `trial6` — the `wt`
subtree having already been removed by step 2. **Nothing in it is unpreserved:** step 1 copied every
file it holds whose hash any committed report names, and `/root/btc-forensics/` now holds all six.
Steps 1 and 2 both exited 0, so the ordering §9 requires is intact and only the final removal is
outstanding.

**This is the one part of TZ-15 that is not finished, and it is a host permission, not a
measurement.** No reading, constant or validation above depends on it.

`/root/tz15-work/`, the label ledger included, is the next TZ's to reclaim on the same terms.
**The capture was never touched and is never deleted.**

---

## 16. Every point where the text needed a reading, with the workaround chosen

1. **§5.3 and V6: "`git diff --name-only` names one file" is only true after the commit.** Every
   development run necessarily precedes it, and at the merge base the path does not exist, so the
   diff is empty there. **Workaround:** V6 asserts `set(names) ⊆ {research/tz15-phase2-gate.py}` at
   every run — empty before the commit, **exactly one file on the scored commit** — and reports the
   list either way. Both readings are in §11.

2. **§5.2: `Decimal` results carry trailing zeros, so item 1's tails print as `1.000000` and item
   2's `FP` as `0.00590896606445312500`.** `Decimal("1.000000") == Decimal("1")` is true and
   `str()` of the two differs. **Workaround:** every self-test compares **as a `Decimal` value**,
   never as a string — which §5.2 item 5 states explicitly for the edges and which items 1 to 4
   require for the same reason. The printed forms above are the values as computed.

3. **V4 (c): "its two runs left two identical copies and either is read" — eight files match.**
   `/root/tz14-work/` holds the hash `0fc46a68f923acbb…` at `run1/`, `run2/` and six `trial*/`
   directories, all byte-identical. **Workaround:** the instrument takes the first in sorted order,
   `/root/tz14-work/run1/observations.csv`, reports the path and reports the count of copies found
   (**8**). The check is unaffected: every copy is the same bytes.

4. **§4's power comparison against a float.** `POWER` is a `Decimal` in every path of the run, but
   §5.2 item 7 writes its cases as `0.79`, `0.8` and `0.85`, and `Decimal("0.8") <= float(0.8)` is
   true only because the float rounds up. **Workaround:** `reading` normalises a non-`Decimal`
   power through `D(str(power))`, so the `0.8` floor is exact whichever type it is handed; the
   self-tests pass `Decimal`s.

5. **§3.4's "a side whose ask does not exist has no edge" and `documents`' empty mapping.** A member
   whose `gamma.json` is unusable has an empty token map, so every read at that member names a token
   outside the mapping. **Workaround:** that case is one of the four §3.3 lists, counted and
   contributing no touch; it never raises. **It did not occur: 0 of 12,000.**

6. **§0.6's ref difference.** `origin/main` is two commits ahead of the value map §1 records. This
   is recorded, not BLOCKING, because `main` carries revision `2026-09-19-a` — the two commits are
   this revision's own map upload and this TZ's own spec. See §0.6.

7. **§3.7's "the market more confident than the pricer" needs a denominator.** §3.4 gives the
   population as the eligible checkpoints whose Up book is two-sided at the touch. **Workaround:**
   reported as a count **and** a share over exactly that population, both in §4's third table.

8. **V9's directory-count clause says "not fallen", and in scored run 2 it rose** from 2,573 to
   2,574 — the recorder opened a new interval mid-run. That satisfies the clause as written and is
   recorded here rather than treated as a difference.

---

## 17. What this TZ establishes, and what it does not

**Established.** Where the Student pricer said the executable ask was cheap after CANON §1.1's taker
fee, and a share of that side was taken on paper at each of 1,924 selected checkpoints across five
`tau`, **the side it chose did not win often enough to reject a market calibrated at its own ask at
any `tau`**, at an exact false-positive rate of `0.0067` to `0.0088` per `tau` and `0.0395` over the
family. The gross profit per share is negative at four of five `tau`.

**Not established, and the honest reason.** **The converse does not follow.** `POWER` — the exact
probability this gate would have read EDGE if the pricer were right about its own claimed edge — is
`0.33` to `0.47`, below §4's `0.8` closing standard at every `tau`. **A coin-flip chance of missing
the edge the pricer itself claims is not a closing standard**, which is exactly why §4 set the floor
there and why no `tau` is closed. Phase 2 is open at all five.

**What it costs to close.** `k = 2` at `tau` 90 and `k = 3` at 240, 180, 120 and 60 — the first
`k × 1,200` qualifying slots with `T0 > 1789669800`, map §2.3's reserved span, whose quotes and
outcomes no one has opened. **The projection is barred from every reading here and is recorded only
as that cost.**

**What the gate does not decide**, and §4 names each: depth beyond `5` shares, the 50 ms taker delay
and the oracle basis — all Phase 3's.

**A report is evidence, not acceptance.** No reading above stands until the Architect has re-derived
`s*`, `FP` and `POWER` from `tz15-constants.json` and `S` from `tz15-observations.csv`. Both files
are byte-identical across two independent scored runs and their hashes are in §12.
