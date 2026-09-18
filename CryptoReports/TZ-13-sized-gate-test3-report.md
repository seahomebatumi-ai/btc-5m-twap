# TZ-13 — the sized gate on test 3 — report

**Executed.** Test 3 was formed, walked, sized from the pricer's own predictions, and only then scored. Every gate of TZ-12 was applied unchanged. **No gate FAILs at any `tau`.** Five `tau` read NOT DISQUALIFIED — 240, 180, 120, 90 and 60 — and two read UNDECIDABLE, 30 and 10, both left there by G3 for want of power. §4.3's straddle band fired at no `tau` and weakened nothing.

**This is not a confirmed edge.** Phase 1 can only disqualify. A `tau` that survives here is admitted to Phase 2 and to nothing else, and no verdict below is final until the Architect has re-derived its gate arithmetic.

| | |
|---|---|
| specification | `CryptoTZ/TZ-13-sized-gate-test3.md` |
| System Map revision | `2026-09-17-a`, six anchors matched 6 of 6 |
| instrument | `research/tz13-sized-gate-test3.py`, branch `tz-13-sized-gate-test3` at `7ef9723` |
| set | test 3 — the first 750 qualifying slots with `T0 > 1789427700` |
| member list SHA-256 | `0f618581ae8be86beed445fc5ad90b8d1d6352271ca8cfd5f5943207011273f2` |
| rows | 750 × 7 = 5,250, every one `label is None` until step 11 |
| outcome read | once, `tz10b.m2_labels`, at `2026-09-18T03:56:03Z` |
| constants on disk before it | `2026-09-18T03:36:31Z` |
| verdict | NOT DISQUALIFIED at `tau` 240, 180, 120, 90, 60; UNDECIDABLE at 30 and 10 |

---

## 1. §0 — the gates, the host, the interpreter and the floor

### 1.1 Fingerprint

`SYSTEM-MAP.md` was read from `origin/main` at `2c7694a9833cd408279c6583f3128124cd5a0f85`. Its revision string reads `2026-09-17-a` and its six anchors equal the TZ's table at **6 of 6**:

| anchor | required | read | equal |
|---|---|---|---|
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` | yes |
| `A2` — collector | `6c5089330629` | `6c5089330629` | yes |
| `A3` — phase | `0-complete / 1-answered-no / 2-not-started` | `0-complete / 1-answered-no / 2-not-started` | yes |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b` | yes |
| `A5` — recorder | `9fd1c7de0f74` | `9fd1c7de0f74` | yes |
| `A6` — pricer | `729f0bcdbee3` | `729f0bcdbee3` | yes |

The **19 `frozen` rows all matched** the hashes the map prints, at run start and again at run end; the 2 `tracked` rows and `SYSTEM-MAP.md` itself are reported with no expectation. The full table is §5's V10.

### 1.2 Host gate — 3 of 3

| check | required | read |
|---|---|---|
| interval directories | exist, non-empty | `/var/lib/btc-recorder/btc-updown-5m/` held **2,170** directories at the §0 read (2026-09-17T22:37Z), first `T0` `1789033800`, last `T0` `1789684500`; **2,229** at run 1's first `tz11a.host_read` and **2,240** at run 2's last |
| recorder process | newest `runtime.jsonl` start record carries sha `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` | pid **228592**, `recv_ns` **1789206785264516934**, sha **`4216c04673ced76b5b2ac60ef57c9abedc46f9b9`** |
| filesystem | `/dev/vda2`, total `31,612,203,008` bytes | `/dev/vda2`, **31,612,203,008** bytes |

**The recorder was never signalled, stopped or restarted.** Its pid and its newest start record are identical at every one of the six asserted reads.

### 1.3 Interpreter

Every command of the instrument ran on `/root/tz01-env/venv/bin/python` — **Python 3.12.3**, **numpy 2.5.3**. Two scratch probes (the §0.6 existence check and a cost timing) ran on the same interpreter; neither computes a measurement that appears below. No scratch script ran on the system `python3`.

### 1.4 The resource floor — every read, with its instant, its reader and its bound

`tz11a.FLOOR_START_BYTES` = `2,060,000,000`; `tz11a.FLOOR_BYTES` = `2,000,000,000`. Both are asserted inside `tz11a.host_read`, never compared by eye.

| # | instant (UTC) | reader | free bytes | bound | asserted |
|---|---|---|---|---|---|
| — | 2026-09-17T22:37:08Z | preflight 1, `df -B1` | 13,946,990,592 | 2,060,000,000 | no |
| — | 2026-09-18T03:30:36Z | preflight 2, `df -B1` | 13,926,305,792 | 2,060,000,000 | no |
| 1 | 2026-09-18T03:30:49Z | run 1, `tz11a.host_read` (run start) | 13,926,256,640 | 2,060,000,000 | **yes** |
| 2 | 2026-09-18T03:33:55Z | run 1, `tz11a.host_read` (after the walk) | 13,926,162,432 | 2,000,000,000 | **yes** |
| 3 | 2026-09-18T03:57:08Z | run 1, `tz11a.host_read` (run end) | 13,925,285,888 | 2,000,000,000 | **yes** |
| 4 | 2026-09-18T04:01:38Z | run 2, `tz11a.host_read` (run start) | 13,922,467,840 | 2,060,000,000 | **yes** |
| 5 | 2026-09-18T04:04:32Z | run 2, `tz11a.host_read` (after the walk) | 13,921,832,960 | 2,000,000,000 | **yes** |
| 6 | 2026-09-18T04:28:10Z | run 2, `tz11a.host_read` (run end) | 13,910,257,664 | 2,000,000,000 | **yes** |
| — | 2026-09-18T04:33:39Z | run end, `df -B1` | 13,907,984,384 | 2,000,000,000 | no |

**6 of 6 asserted reads passed.** The lowest free-space reading of the session is **13,907,984,384 bytes**, 6.95× the floor.

### 1.5 Preflight, twice, 17,608 s apart

§0.5 requires two preflights at least 1,800 s apart, the first before the build and the second before the first full run. The first was taken before the instrument was written; the second immediately before run 1. **Elapsed: 17,608 s (4.891 h).**

| quantity | preflight 1 (2026-09-17T22:37:08Z) | preflight 2 (2026-09-18T03:30:36Z) | delta | implied per day |
|---|---|---|---|---|
| `df -B1` available on `/dev/vda2` | 13,946,990,592 | 13,926,305,792 | −20,684,800 | **−101.50 MB/day** |
| `du -sb /root/PROJECT_GAMING_PS5` | 367,914,928 | 369,501,594 | +1,586,666 | **+7.79 MB/day** |
| `systemctl is-enabled telemetry-watch.service` | `disabled`, exit **1** | `disabled`, exit **1** | — | — |
| `systemctl is-active telemetry-watch.service` | `inactive`, exit **3** | `inactive`, exit **3** | — | — |

**This run's own footprint, stated separately at both reads** (map §7 item 29):

| path | preflight 1 | preflight 2 | delta | implied per day |
|---|---|---|---|---|
| `/root/tz13-work` | absent (0) | 3,053,309 | +3,053,309 | +14.98 MB/day |
| `/root/.claude` | 123,370,753 | 123,940,886 | +570,133 | +2.80 MB/day |

`/root/tz13-work` grew to **8,969,380 bytes** by run end — the two run directories, the git worktree and the scratch probes. The per-day figure above is an artefact of a tree that is built once and then stops growing; it is not a drain. The preflight gates nothing beyond §0.4 and nothing here is a gate.

### 1.6 §0.6 — the set exists

The capture holds **750** qualifying slots with `T0 > 1789427700`. **807** units were considered, from `1789428000` to `1789669800`. The run is not BLOCKED.

---

## 2. The measurements, in §3's order

### 2.1 §3.1 — test 3

Formed by the committed set rule, called exactly as the file holds it:

```
tz06.scoring_set(manifests, 750, after=1789427700)
```

| field | value |
|---|---|
| units considered | **807**, `1789428000` … `1789669800` |
| members | **750**, `1789428000` … `1789669800` |
| non-members | **57** — `disconnect`: 57 |
| qualifying rate | **0.9294** |
| member-list SHA-256 | `0f618581ae8be86beed445fc5ad90b8d1d6352271ca8cfd5f5943207011273f2` — **reported, not compared**: no committed artifact names it |
| first-400 member-list SHA-256 | `edc2a5c5e703a5ac7d811ed9ca571a063136073e9c5d758df4c410662465c2db` |
| unit-by-unit disclosure SHA-256 | `d8c49f783b6225be3029e3629e7eb58d69c314bf4c127f5c7864ccaf77e4d595` |

**§3.1's four assertions, each of which would have aborted the run:**

1. **750 members, every `T0` strictly greater than `1789427700`** — the first member is `1789428000`. Asserted.
2. **Disjoint from each of the three committed sets**, formed in the same run by `tz11a.the_sets(manifests)`. Three pairwise intersections, **each empty**. Asserted.
3. **`tz06.scoring_set(manifests, 400, after=1789427700)` returns exactly the first 400 members of test 3, in the same order.** Asserted — test 3 is a superset of the set map revision `2026-09-15-a` defined.
4. The member-list SHA-256 is `tz07b.member_list_sha` over the sorted `T0` list, **reported, not compared**.

**The three committed sets, re-formed in this run and hash-asserted:**

| set | units | members | non-members | member-list SHA-256 | equals |
|---|---|---|---|---|---|
| fit | 443 | 400 | 43 (disconnect: 41, disconnect + no chainlink at or before T0-300: 2) | `6d94a346a47a04a1a0849968effd9023d7585fe628b304ba2ae7a15953ee67f9` | `tz11a.FIT_SHA256` ✓ |
| test1 | 433 | 400 | 33 (disconnect: 33) | `3b17729c050e5fbf8fed1bd0877d5dd5c229370609cd672c84eeed1ddc3d5762` | `tz11a.TEST1_SHA256` ✓ |
| test2 | 438 | 400 | 38 (disconnect: 38) | `2dd0fcc4dc2cf379e08c21a4524c3eab799aad7bff3136c37e32910cecb8fa70` | `tz12.TEST2_SHA256` ✓ |

**Disclosure — every unit considered, in ascending `T0`.** The full 807-row list is the run's `tz13-results.json` under `disclosure`, one row per unit with its reasons, and its SHA-256 is `d8c49f783b6225be3029e3629e7eb58d69c314bf4c127f5c7864ccaf77e4d595`. All **750** members carry an empty reason list. All **57** non-members fail on exactly one reason, `disconnect`; no other reason appears anywhere in the 807. The non-member `T0`s are:

```
  1789429800  1789430100  1789437000  1789437300  1789441200  1789441500  1789444500  1789444800  1789451700
  1789452000  1789458900  1789459200  1789466100  1789466400  1789470300  1789473900  1789475400  1789475700
  1789478100  1789485300  1789490700  1789491000  1789496700  1789502700  1789503000  1789510200  1789517400
  1789521300  1789528500  1789535700  1789542900  1789549200  1789551300  1789554000  1789561200  1789568400
  1789575600  1789582800  1789590000  1789596600  1789598700  1789601700  1789608900  1789616100  1789623300
  1789630500  1789632900  1789633200  1789640400  1789644300  1789644600  1789647000  1789653900  1789656000
  1789656300  1789663200  1789663500
```

| reason | non-members | share of 807 |
|---|---|---|
| `disconnect` | 57 | 0.0706 |
| **total** | **57** | **0.0706** |

Qualifying rate **0.9294**.

### 2.2 §3.2 — the walk, the rows, the domain

Every member was walked by `tz11a.walk_member(t0, manifests, guard)` with `guard` **false**, in ascending `T0`, and every member at every `tau` in `pfair.TAUS` became one row through `tz11a.checkpoint_row(t0, "test3", tau, row)` — **750 × 7 = 5,250 rows, every one carrying `label = None` until step 11**.

**The guarded pass.** `tz11a.walk_member` was run a second time with `guard` **true** over a sample formed mechanically, and its size re-derived at run time:

| component | members |
|---|---|
| the first 25 in ascending `T0` | 25 |
| the last 25 | 25 |
| the 25 with the largest count of excluded seconds, ties by ascending `T0` | 25 |
| overlap between the three lists | 0 |
| **union — the sample** | **75** of at most 75 |
| rows produced and compared | **525** (75 members × 7 `tau`) |
| rows **asserted identical** to the unguarded row | **525 of 525** |

Only **39** of the 750 members have any excluded second at all, so the third list is drawn from a population of 39; the largest count is 34 seconds and the 25th largest is 3.

**The domain.** A row is admissible when its `sigma_hat` is at or above the committed literal `pfair.ADMIT[tau]`. Every statistic below names the population it is computed over, and every gate reads **test 3's admissible rows at that `tau`**.

| `tau` | `pfair.ADMIT[tau]` | admissible members | share of 750 | member-list SHA-256 |
|---|---|---|---|---|
| 240 | `2.12324` | **521** | 0.6947 | `887ee8b330cc366a1455fa84f83cbf743b91f03d37cc1a1a9639644052c615d5` |
| 180 | `2.14298` | **523** | 0.6973 | `4cd2ba8ecf548c8103baae78cc266b7e2ab4e0e31cc31f1d2a8c9730d2e9aba6` |
| 120 | `2.18062` | **514** | 0.6853 | `787a7f616fea75149e75be1e5ee1b1319500300967d7680699673258f02820f5` |
| 90 | `2.16098` | **520** | 0.6933 | `ed9eb7fb90339035af0bdfc4fbc16a10e95c4e12c5afa323d7ebc9321376a23f` |
| 60 | `2.16725` | **521** | 0.6947 | `f7a887c47081e614c8155df0d345a81ea6c3b8847f4120e00ad67ca52dcb422e` |
| 30 | `2.15178` | **523** | 0.6973 | `ab5aaa23c449c91c3f257da0d59935160e6a6fa3ad2923aa4fcd4f65cd6b5fa6` |
| 10 | `2.14530` | **528** | 0.7040 | `72a8def0121d6463057670cd28957c70f4a696993379af544498760415d27a85` |

The admissible share lies between **0.6853** and **0.7040** — every `tau` above the 0.65 upper end of §4.4's prediction 2.

### 2.3 §3.3 — the constants, from predictions alone, written before any outcome was read

For each `tau`, over test 3's admissible rows at that `tau`:

```
tz12.constants(rows, tau, tz12.SET_CODES["test3"])
```

This is the frozen sizing arithmetic, called unchanged: `R_NULL = 20,000` null replicates with labels drawn from the pricer's own `p_t`, `R_POWER = 2,000` at each of `LAMBDA_OVER = 1.5`, `LAMBDA_UNDER = 1/1.5` and `LAMBDA_DOUBLE = 2`, 2,000 coin replicates, the λ grid, `k2_of`, `crit_of` and `g4_constants`.

**The whole of §3.3 is a property of the predictions. No outcome existed in the process when it ran, and the instrument asserted that twice** — immediately before the first `tz12.constants` call and immediately after the last:

| step | instant (UTC) | rows | `label is None` |
|---|---|---|---|
| 7 — before the first `tz12.constants` call | 2026-09-18T03:33:55Z | 5,250 | **5,250 of 5,250** |
| 9 — after the last | 2026-09-18T03:36:31Z | 5,250 | **5,250 of 5,250** |

**The two instants §3.3 requires:** the constants were written to disk at **2026-09-18T03:36:31Z** (`tz13-sizing.json`), and `tz10b.m2_labels` was called at **2026-09-18T03:56:03Z** — **19 minutes 32 seconds later**, and after §3.6's projection had also run.

**Test 3's admissible rows, per `tau`:**

| `tau` | `m` | G1 `P0` | G1 `P1` | G2 `E` | G2 `k2` | null `F >= k2` | G3 `crit3` | G3 `P3` (λ = 1.5) | `P_under` (λ = 1/1.5) | `P_double` (λ = 2) | G4 `c4` | G4 `s` | G4 `P4` | censored |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 240 | 521 | 0.0000 (0 of 20,000) | 1.0000 (2000 of 2,000) | 8 | 2 | 16 | 9.397211 | 0.6890 (1378 of 2,000) | 0.8610 (1722 of 2,000) | 0.9935 (1987 of 2,000) | 2.224364 | 0.591137 | 0.0048 | no |
| 180 | 523 | 0.0000 (0 of 20,000) | 1.0000 (2000 of 2,000) | 10 | 3 | 0 | 8.764159 | 0.9295 (1859 of 2,000) | 0.9685 (1937 of 2,000) | 1.0000 (2000 of 2,000) | 1.578021 | 0.419368 | 0.0174 | no |
| 120 | 514 | 0.0000 (0 of 20,000) | 1.0000 (2000 of 2,000) | 10 | 2 | 16 | 8.927718 | 0.9755 (1951 of 2,000) | 0.9680 (1936 of 2,000) | 1.0000 (2000 of 2,000) | 1.689499 | 0.448994 | 0.0132 | no |
| 90 | 520 | 0.0000 (0 of 20,000) | 1.0000 (2000 of 2,000) | 9 | 3 | 0 | 8.886025 | 0.9675 (1935 of 2,000) | 0.9210 (1842 of 2,000) | 1.0000 (2000 of 2,000) | 1.101756 | 0.292798 | 0.0814 | no |
| 60 | 521 | 0.0000 (0 of 20,000) | 1.0000 (2000 of 2,000) | 4 | 2 | 0 | 8.967324 | 0.9090 (1818 of 2,000) | 0.6500 (1300 of 2,000) | 0.9995 (1999 of 2,000) | 0.409083 | 0.108716 | 0.9955 | no |
| 30 | 523 | 0.0000 (0 of 20,000) | 1.0000 (2000 of 2,000) | 2 | 2 | 0 | 9.504963 | 0.3230 (646 of 2,000) | 0.0850 (170 of 2,000) | 0.9155 (1831 of 2,000) | 0.260019 | 0.069101 | 1.0000 | no |
| 10 | 528 | 0.0000 (0 of 20,000) | 1.0000 (2000 of 2,000) | 2 | 2 | 0 | 7.087974 | 0.0495 (99 of 2,000) | 0.0000 (0 of 2,000) | 0.1815 (363 of 2,000) | 0.151855 | 0.040356 | 1.0000 | yes |

`P0` is **0 of 20,000 at every `tau`** — the frozen pricer's own predictions never produce a Brier at or above `0.2496` under its own null. `P1` is **2,000 of 2,000 at every `tau`** — a coin-flip pricer would be caught every time. **G1 therefore carries power at all seven `tau`.**

`P3` reaches `tz12.POWER_TO_PASS` = `0.5` at **five `tau`** — 240, 180, 120, 90 and 60 — and falls below it at 30 (0.3230) and 10 (0.0495). **G3 can decide at five `tau` and cannot at two.**

`P4` is below `0.5` at `tau` 240, 180, 120 and 90 (0.0048, 0.0174, 0.0132, 0.0814) and at or above it at 60, 30 and 10. `tau = 10` is in `tz12.SIGMA_LOG_NU_CENSORED`.

**The null failing-bin distribution**, per `tau`, as `tz12.constants` returns it:

| `tau` | `E` | `k2` | null `F` distribution |
|---|---|---|---|
| 240 | 8 | 2 | 0: 19075, 1: 909, 2: 16 |
| 180 | 10 | 3 | 0: 19035, 1: 942, 2: 23 |
| 120 | 10 | 2 | 0: 19136, 1: 848, 2: 16 |
| 90 | 9 | 3 | 0: 19087, 1: 889, 2: 24 |
| 60 | 4 | 2 | 0: 19784, 1: 216 |
| 30 | 2 | 2 | 0: 19937, 1: 63 |
| 10 | 2 | 2 | 0: 19961, 1: 39 |

### 2.4 §3.4 — the outcomes, read once

`tz10b.m2_labels(members)` was called **once**, for test 3's 750 members, at **2026-09-18T03:56:03Z** — after §3.3's output was on disk and after §3.6's projection had run.

| field | value |
|---|---|
| members | 750 |
| outcomes returned | **750** |
| members with no outcome available | **0** |
| resolved Up | 378 (0.5040) |
| calls to a label entry point in the whole run | **1** |

**No member was excluded for want of an outcome**, at any `tau`. This is structural, not luck: `tz06.qualification` refuses membership to any interval whose settled document carries no resolved outcome, so every member of a set formed by that rule has one. The instrument nevertheless carries the exclusion path and reports it as 0.

### 2.5 §3.5 — the observed statistics

Per `tau`, over **test 3's admissible rows**, with the outcomes of §3.4.

| `tau` | `m` | observed Up rate | Brier | `tz11a.G1_BRIER` | beats it | eligible bins | failing bins | `λ̂` | LR at `λ̂` | `ν̂` | `ŝ` | `pfair.LINK_NU` | `log(ν̂ / LINK_NU)` | search edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 240 | 521 | 0.5086 | **0.195660** | 0.2496 | yes | 8 | **0** | 1.023832 | 0.051273 | 30.0060 | 1.4274 | `9.62070` | +1.137481 | interior |
| 180 | 523 | 0.5105 | **0.164347** | 0.2496 | yes | 10 | **0** | 1.032342 | 0.136147 | 36.9921 | 1.4448 | `13.7083` | +0.992702 | interior |
| 120 | 514 | 0.5058 | **0.120071** | 0.2496 | yes | 10 | **0** | 0.991405 | 0.011166 | 21.8215 | 1.4372 | `20.2258` | +0.075935 | interior |
| 90 | 520 | 0.5058 | **0.085445** | 0.2496 | yes | 9 | **0** | 0.884356 | 1.905677 | 17.0651 | 1.4053 | `16.0482` | +0.061440 | interior |
| 60 | 521 | 0.5029 | **0.040467** | 0.2496 | yes | 4 | **0** | 0.743647 | 6.230197 | 10.3917 | 1.3168 | `9.51490` | +0.088149 | interior |
| 30 | 523 | 0.4990 | **0.012540** | 0.2496 | yes | 2 | **0** | 0.685459 | 3.135393 | 5.2627 | 1.1149 | `4.79579` | +0.092911 | interior |
| 10 | 528 | 0.5000 | **0.003350** | 0.2496 | yes | 2 | **0** | 1.187572 | 0.129835 | 2.0639 | 0.6310 | `2.13489` | -0.033800 | interior |

- **Brier** is `tz06.brier(pairs)` over `(p_t, label)`. It is **below `0.2496` at every `tau`**, by a wide margin — from 0.195660 at `tau` 240 down to 0.003350 at `tau` 10.
- **Bins** are `tz06.calibration` and `tz06.table_for(tau, rows, "p_t", G1_BRIER)`, by the committed definitions. **The failing-bin count is 0 at every `tau`**, against `k2` of 2 or 3.
- **Scale** is `tz07a.lambda_hat(pairs, tz11a.student_log_cdf(nu))` with `nu = pfair.LINK_NU[tau]` — the committed search under the committed Student log CDF, through the keyword parameter the file already holds.
- **Shape** is `tz11a.fit_student(r)` over `tz11a.population(walked, members, tau)` for test 3's admissible members, with the search-edge status read through `tz11a.bound_note(fit)`. **No search constant is named by this report.** Every fit landed **interior** — no `ν̂` or `ŝ` sits on a bound at any `tau`.

`λ̂` runs from 1.023832 at `tau` 240 down to 0.685459 at `tau` 30 and back to 1.187572 at `tau` 10. The largest likelihood ratio is **6.230197 at `tau` 60**, against a `crit3` of **8.967324** — well inside. **G3 does not FAIL anywhere.**

`|log(ν̂ / LINK_NU)|` is largest at `tau` 240 (1.137481) and 180 (0.992702), against `c4` of 2.224364 and 1.578021. **G4 does not FAIL anywhere either.**

**Influence** (map §7 items 27 and 40). Every statistic a verdict table reads is reported a second time, recomputed without its single most influential member — `λ̂` through `tz11a.lambda_with_influence` and `ν̂` through `tz11a.influence_refit`. **Both are reported, not asserted, and the gate is judged on the value §4 defines.**

| `tau` | `λ̂` | `λ̂` without | shift | held-out `T0` | `ν̂` | `ν̂` without | shift | held-out `T0` | `log(ν̂ / LINK_NU)` without |
|---|---|---|---|---|---|---|---|---|---|
| 240 | 1.023832 | 0.991986 | -0.031846 | `1789549500` | 30.0060 | 60.0000 | +29.9940 | `1789493400` | +1.830428 |
| 180 | 1.032342 | 0.996432 | -0.035909 | `1789583700` | 36.9921 | 47.3023 | +10.3102 | `1789493400` | +1.238558 |
| 120 | 0.991405 | 0.943300 | -0.048106 | `1789561800` | 21.8215 | 23.9983 | +2.1768 | `1789469400` | +0.171023 |
| 90 | 0.884356 | 0.855910 | -0.028446 | `1789611000` | 17.0651 | 18.2866 | +1.2215 | `1789469400` | +0.130574 |
| 60 | 0.743647 | 0.681465 | -0.062182 | `1789590600` | 10.3917 | 10.6230 | +0.2313 | `1789561800` | +0.110166 |
| 30 | 0.685459 | 0.597908 | -0.087551 | `1789611000` | 5.2627 | 5.2800 | +0.0173 | `1789561800` | +0.096187 |
| 10 | 1.187572 | 0.754356 | -0.433216 | `1789586700` | 2.0639 | 2.0584 | -0.0056 | `1789587000` | -0.036508 |

The one figure worth naming: at `tau` 240 the single most influential member moves `ν̂` from 30.0060 to **60.0000, the upper search bound**. That is a property of the held-out refit and **it is not the value the gate reads**; the gate reads 30.0060, interior. At `tau` 10 the `λ̂` shift is the largest at -0.433216. None of these figures enters a verdict.

### 2.6 §3.6 — how the gate's power grows with the population — **a projection**

> **This is a projection and it is barred from every gate reading.** A repeated row is not a new observation: it holds the scale of the likelihood fixed while multiplying its weight, which is what a larger set would do to the non-centrality and is **not** what a larger set would do to anything else. No verdict, threshold or admission below reads this table.

For each `tau`, `tz12.constants` was called two more times, on test 3's admissible rows for that `tau` repeated twice and three times.

| `tau` | `n` at 1× | `P3` 1× | `P3` 2× | `P3` 3× | `P1` 1× / 2× / 3× | `P4` 1× / 2× / 3× | smallest multiple at which `P3` reaches `tz12.POWER_TO_PASS` |
|---|---|---|---|---|---|---|---|
| 240 | 521 | 0.6890 | 0.9650 | 0.9980 | 1.0000 / 1.0000 / 1.0000 | 0.0048 / 0.0067 / 0.0077 | **1** |
| 180 | 523 | 0.9295 | 0.9985 | 1.0000 | 1.0000 / 1.0000 / 1.0000 | 0.0174 / 0.0260 / 0.0303 | **1** |
| 120 | 514 | 0.9755 | 1.0000 | 1.0000 | 1.0000 / 1.0000 / 1.0000 | 0.0132 / 0.0196 / 0.0229 | **1** |
| 90 | 520 | 0.9675 | 1.0000 | 1.0000 | 1.0000 / 1.0000 / 1.0000 | 0.0814 / 0.1237 / 0.1448 | **1** |
| 60 | 521 | 0.9090 | 0.9990 | 1.0000 | 1.0000 / 1.0000 / 1.0000 | 0.9955 / 0.9994 / 0.9998 | **1** |
| 30 | 523 | 0.3230 | 0.7095 | 0.8925 | 1.0000 / 1.0000 / 1.0000 | 1.0000 / 1.0000 / 1.0000 | **2** |
| 10 | 528 | 0.0495 | 0.0715 | 0.1235 | 1.0000 / 1.0000 / 1.0000 | 1.0000 / 1.0000 / 1.0000 | **not reached at 3×** |

Five `tau` already reach the floor at 1×. `tau = 30` reaches it at **2×** — about 1,046 admissible members, which at test 3's 0.6973 admissible share is about **1,500 scored members**, and at its 0.9294 qualifying rate about **1,600 units considered**. **`tau = 10` does not reach the floor at 3×** (0.1235), which is §4.4's prediction 6 and it holds.

**The set size for Phase 2 is therefore a measurement and not an extrapolation**, under the stated caveat: to give G3 power at every `tau` down to 30, roughly twice test 3's scored population is needed; `tau = 10` is out of reach of anything this projection can see.

---

## 3. The verdict

Fixed before any outcome of test 3 was read. Per `tau`, over test 3's admissible rows. The thresholds are TZ-12's, read from the committed files at run time and not restated here as new numbers.

**§4.2 — the family-wise rate, stated, not recomputed:** `tz12.FAMILY_ALPHA` = **0.048**, as 7 × 0.001 for G1, 6 × 0.001 for G2 and 7 × 0.0025 each for G3 and G4. `tz12.ALPHA` = `{G1: 0.001, G2: 0.001, G3: 0.0025, G4: 0.0025}`, `tz12.COUNT_BOUND` = **20**, `tz12.CRIT_RANK` = **19,950**.

### 3.1 The verdict table

| `tau` | G1 | G2 | G3 | G4 | **verdict** | left there by | did §4.3's band do it? |
|---|---|---|---|---|---|---|---|
| 240 | PASS | NO FAIL | PASS | UNDECIDABLE | **NOT DISQUALIFIED** | — | **no** |
| 180 | PASS | NO FAIL | PASS | UNDECIDABLE | **NOT DISQUALIFIED** | — | **no** |
| 120 | PASS | NO FAIL | PASS | UNDECIDABLE | **NOT DISQUALIFIED** | — | **no** |
| 90 | PASS | NO FAIL | PASS | UNDECIDABLE | **NOT DISQUALIFIED** | — | **no** |
| 60 | PASS | NO FAIL | PASS | NO FAIL | **NOT DISQUALIFIED** | — | **no** |
| 30 | PASS | NO FAIL | UNDECIDABLE | NO FAIL | **UNDECIDABLE** | G3 | **no** |
| 10 | PASS | NO FAIL *(printed, not gated)* | UNDECIDABLE | UNDECIDABLE | **UNDECIDABLE** | G3 | **no** |

**Five `tau` read NOT DISQUALIFIED: 240, 180, 120, 90 and 60.** At each, G1 and G3 both PASS with power and no gate FAILs.

**Two `tau` read UNDECIDABLE: 30 and 10, and G3 left both there.** `P3` is 0.3230 at 30 and 0.0495 at 10, both below `tz12.POWER_TO_PASS` = 0.5, so the gate could not have caught a 1.5× overconfidence at least half the time and its silence means nothing. **A `tau` that reads UNDECIDABLE closes nothing and admits nothing.**

**No gate FAILs at any `tau`.** The failing list `tz12.verdict` returns is empty, and the family verdict it returns is **NOT DISQUALIFIED**, admitting `240, 180, 120, 90, 60`.

### 3.2 §4.3's straddle rule — applied, and it changed nothing

For each gate whose power `P` decides UNDECIDABLE, the `tau` reads UNDECIDABLE whenever `|P − 0.5| <= 1.96 · sqrt(P(1−P)/2000)`. At `P = 0.5` that band is `0.5 ± 0.021913466179498`.

| `tau` | G1's `P1` | inside the band | G3's `P3` | inside the band | G4's `P4` | inside the band |
|---|---|---|---|---|---|---|
| 240 | 1.0000 | no | 0.6890 | no | 0.0048 | no |
| 180 | 1.0000 | no | 0.9295 | no | 0.0174 | no |
| 120 | 1.0000 | no | 0.9755 | no | 0.0132 | no |
| 90 | 1.0000 | no | 0.9675 | no | 0.0814 | no |
| 60 | 1.0000 | no | 0.9090 | no | 0.9955 | no |
| 30 | 1.0000 | no | 0.3230 | no | 1.0000 | no |
| 10 | 1.0000 | no | 0.0495 | no | 1.0000 | no |

**The band covers no power at any `tau`, for any gate — 0 of 21.** The nearest approach is G3 at `tau` 240, `P3` = 0.6890, which is 0.1890 above the floor and 8.6× the band's half-width. §4.3 was applied after `tz12.verdict` and weakened nothing.

The correction is legitimate and this sentence is the statement CANON PART II requires: **no score under this gate exists, on any set, computed by anyone** — TZ-12 read no outcome and produced no observed statistic — **and no outcome of test 3 had been read by anyone** before step 11 of this run. Tests 1 and 2 are never scored under this gate; test 2's rows enter this run only through V4, whose figures are label-free.

### 3.3 §4.4 — the pre-registered prediction, beside what was measured

Recorded, not asserted. It decides nothing.

| # | predicted | measured | holds |
|---|---|---|---|
| 1 | test 3 forms from 810 to 840 units considered, a qualifying rate between 0.88 and 0.93 | **807** units considered; rate **0.9294** | **no** — the rate is inside, the unit count is 3 below the lower end |
| 2 | the admissible share of 750 lies between 0.50 and 0.65 at every `tau` | 0.6947 / 0.6973 / 0.6853 / 0.6933 / 0.6947 / 0.6973 / 0.7040 | **no** — every `tau` is above 0.65 |
| 3 | `P3 >= 0.8` at `tau` 180, 120, 90 and 60; `P3` between 0.45 and 0.70 at 240; `P3 < 0.3` at 30; `P3 < 0.1` at 10 | 0.6890 / 0.9295 / 0.9755 / 0.9675 / 0.9090 / 0.3230 / 0.0495 | **no** — the first three clauses hold; `P3` at 30 is 0.3230, above 0.3 |
| 4 | `P0 <= 0.001` and `P1 >= 0.95` at every `tau` | `P0` = 0.0000 at all seven; `P1` = 1.0000 at all seven | **yes** |
| 5 | the verdict reads NOT DISQUALIFIED at `tau` 180, 120 and 90; DISQUALIFIED at 60, through G3, with `λ̂ > 1`; UNDECIDABLE at 240, 30 and 10 | NOT DISQUALIFIED at 240, 180, 120, 90 and 60; UNDECIDABLE at 30 and 10; `λ̂` at 60 is **0.743647**, below 1 | **no** — 180, 120, 90, 30 and 10 hold; 240 and 60 do not, and 60 fails in the opposite direction to the prediction |
| 6 | in §3.6, `tau = 10` does not reach `tz12.POWER_TO_PASS` at 3× | `P3` at 3× is **0.1235** | **yes** |

**Two of six hold.** The two that hold are the two that are properties of the pricer alone (4 and 6). The four that do not are all about the *size and quality* of the set: more members qualified than predicted, far more of them were admissible, and the extra population bought G3 enough power that `tau` 240 and 60 became decidable rather than undecidable — and, having become decidable, they passed.

---

## 4. §5 — the implementation

**One new file, and nothing else.** `research/tz13-sized-gate-test3.py`, on branch `tz-13-sized-gate-test3`.

| | |
|---|---|
| commit | `7ef972397a12bce0cc76b1f58ceda3e5caa43cdc` |
| merge base | `2c7694a9833cd408279c6583f3128124cd5a0f85` |
| lines | **1,074** |
| bytes | **53,901** |
| SHA-256 on the branch | `a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd` |
| `git diff --name-only` against the merge base | `research/tz13-sized-gate-test3.py` — **one path** |
| committed lines the change replaces | **0** — the diff is additive in the strict sense |

It loads `tz12-sized-gate.py` once through an `importlib` helper of the same shape as `tz11a._load`, and takes `tz11a`, `tz10b`, `tz08a`, `tz07b`, `tz07a`, `tz06` and `pfair` from that module rather than loading any of them a second time. It sets `OPENBLAS_NUM_THREADS`, `OMP_NUM_THREADS` and `MKL_NUM_THREADS` to `"1"` before its first `import numpy`, and writes no other environment variable — **3 of 3, asserted by V6**.

**The functions §5.1 names, each present with the contract named there:** `the_set`, `walk`, `guard_sample`, `admissible`, `sizing`, `labels`, `observed`, `straddle`, `weaken`, `projection`, `selftests`, `v2_static`, `v6`, `build`, `tables`, `csv_text`, `main`.

**The order of the run, asserted by `build` and recorded in its output:**

1. host read 1
2. self-tests
3. v6 and v2 static
4. the four sets
5. the walk and the guarded pass
6. the domain
7. label is None, 5,250 of 5,250
8. tz12.constants, written to disk
9. label is None again
10. the projection
11. tz10b.m2_labels
12. the readings and the verdict
13. host read 3 and V9

### 4.1 Cost, measured against §6's estimate

| step | §6 estimated | run 1 measured | run 2 measured |
|---|---|---|---|
| self-tests | ~10 s | 7 s (timed standalone; not separately timed in-run) | — |
| `tz12.constants`, 7 `tau` on test 3 at ~521 admissible | ~75 s | **155 s** | — |
| V4: `tz12.constants`, 7 `tau` on test 2's rows | ~40 s | **66 s** | — |
| V4's seven fits | — | 16.2 s | 17.1 s |
| **one full run** | **~770 s** | **1579.6 s** | **1591.3 s** |
| **the session, two full runs** | **~1,540 s** against `tz12.SESSION_CEILING_S` = 3,600 | **3171 s** | |

**§6's per-run estimate is low by a factor of about 2.05.** The gap is §3.6's projection, which §6 budgets at ~375 s: `tz12.constants` is dominated by `grid_tables`, which builds two `n × 2,501` tables through `pfair.log_t_cdf` in pure Python, so its cost is very close to linear in `n`, and the 1× + 2× + 3× sequence costs about six times the 1× call rather than five. The session still finished at **3171 s against a 3,600 s ceiling**, and no fail-fast fired.

**Fail-fast, asserted, both runs:** the first `tz12.constants` call took **18.37 s** (run 1) and **18.60 s** (run 2), against the 120 s bound; the implied projection `35 t + 500` was **1143 s** and **1151 s**, against the 3,000 s bound. `tz12.v4_fits`' own fail-fast on seven fits — 40 s — saw **16.2 s** and **17.1 s**. **No check here was sampled: every one ran in full.**

### 4.2 §5.2 — the six self-tests, run before the capture was touched

**6 of 6 items passed, 31 assertions.** Their output, verbatim from run 1:

```
item 1: straddle at 0.5 / 0.478086 / 0.521914 / 0.48 / 0.52 is True / False / False / True / True; half-width 0.02191346617949794 against 0.021913466179498, relative 2.66e-15
item 2: PASS@0.50->UNDECIDABLE PASS@0.70->PASS PASS@0.30->PASS FAIL@0.50->UNDECIDABLE FAIL@0.70->FAIL FAIL@0.30->FAIL UNDECIDABLE@0.50->UNDECIDABLE UNDECIDABLE@0.70->UNDECIDABLE UNDECIDABLE@0.30->UNDECIDABLE
item 3: scoring_set(manifests, 400, after=1789296300) -> 400 members, 2dd0fcc4dc2cf379e08c21a4524c3eab799aad7bff3136c37e32910cecb8fa70
item 4: t_cdf(-2.0, 1)=0.14758361765043318 rel 5.6e-16; t_cdf(-0.5, 1)=0.3524163823495669 rel 4.4e-16; t_cdf(-2.0, 2)=0.091751709536136872 rel 1.2e-15; t_cdf(-0.5, 2)=0.33333333333333343 rel 4.4e-16; symmetry 4 of 4
item 5: g4_power(0.6931471805599453, 0.1)=0.5 rel 0; g4_power(0.0, 0.1)=1 rel 0; g4_power(2.668167, 0.70908)=0.0026747531069279962 rel 2.1e-14
item 6: 1000 doubles identical; test2 first 0.91203982433728192, purpose 1 first 0.42998364148543644, test3 first 0.86605429628368014
```

| item | subject | assertions |
|---|---|---|
| 1 | the straddle band and its half-width against the Architect's 40-digit literal | 6 |
| 2 | weakening only, over nine fixed rows | 9 |
| 3 | the set-formation call shape, against `tz12.TEST2_SHA256` | 1 |
| 4 | the Student CDF at `ν` 1 and 2 against closed forms, and its symmetry | 8 |
| 5 | `tz12.g4_power` at three fixed arguments | 3 |
| 6 | stream separation | 4 |
| **total** | | **31** |

Item 1's half-width computed in IEEE double is `0.02191346617949794`, against the Architect's literal `0.021913466179498`, a relative difference of **2.66e-15** — inside the `1e-12` the item fixes. Item 4's four literals agree to between **4.4e-16** and **1.2e-15**. Item 5's third value agrees to **2.1e-14**, inside the `1e-9` the item fixes, and the first two are exact.

**Unlike TZ-10, TZ-10a and TZ-11, this TZ's §5.2 is passable as written.** Every expectation it fixes is either a closed form independent of the implementation under test, or a value quoted from a committed artifact — none is a quantity this TZ measures.

---

## 5. §7 — V1 … V12

### V1 — gates — asserted

| | |
|---|---|
| anchors | **6 of 6** |
| `frozen` rows of map §0 | **19 of 19**, at run start and at run end |
| `tracked` rows | **2 of 2**, reported with no expectation |
| host gate | **3 of 3** |
| interpreter | `/root/tz01-env/venv/bin/python`, Python 3.12.3, numpy 2.5.3 |
| free-space reads | **8 recorded**, of which **6 asserted** by `tz11a.host_read` — 2 at the `2,060,000,000` start floor and 4 at the `2,000,000,000` floor; every one with its instant, reader and bound in §1.4 |

### V2 — outcome isolation — asserted two ways

**Static, over the instrument's own syntax tree:**

| | |
|---|---|
| string constants scanned, docstrings exempt | **817** |
| docstrings exempted | 28 |
| carrying any of `resolution`, `resolved_up`, `priceToBeat`, `quotes.jsonl`, `gamma.json` | **0** |
| calls scanned | **388** |
| calls of an outcome entry point **outside §3.4** | **0** |
| calls of an outcome entry point **inside §3.4's `labels`** | **1** |

The entry points scanned for are `m2_labels`, `venue`, `qualification`, `score_member` and `score`.

**At run time:** **5,250 of 5,250** rows carried `label is None` at step 7 and again at step 9, and `tz10b.m2_labels` was called **exactly once** in the run, at step 11 — counted by a ledger the instrument asserts at the end of `build`.

### V3 — determinism — asserted

Two full runs from fresh processes on the same commit `7ef9723`.

| output | run 1 SHA-256 | run 2 SHA-256 | `cmp` | compared |
|---|---|---|---|---|
| `tz13-tables.md` | `6a8bf94a6a43c837` | `6a8bf94a6a43c837` | identical | **yes** |
| `tz13-observations.csv` | `e78b01b5f06f485d` | `e78b01b5f06f485d` | identical | **yes** |
| `tz13-sizing.json` | `4de6ba4c36bd709b` | `4de6ba4c36bd709b` | identical | **yes** |
| `tz13-results.json` | `0a31b83ea6302282` | `334ae96c7ff8f915` | differs | **no — it holds a clock reading** |
| `tz13-host.json` | `a134584614236768` | `5237f916b0562275` | differs | **no — it holds clock readings and timings** |

**The three deterministic outputs are byte-identical, by `cmp` and by SHA-256 pair.**

`tz13-results.json` is named as a file holding a clock reading, as V3's own rule provides. Beyond what V3 asks, its difference was enumerated: **exactly 7 scalar fields differ, and all 7 are UTC instants** — `clock.labels_read`, `clock.rows_unlabelled_first`, `clock.rows_unlabelled_second`, `clock.sizing_written`, `labels.utc`, `rows_unlabelled[0].utc`, `rows_unlabelled[1].utc`. With those seven normalised the two files hash to the same value, `4a373352de4a2ee62e49aef21985fff36b187522fd92e58d1f18f97487b6261b`. **No measured quantity moved between the runs.**

| run | wall clock | peak RSS |
|---|---|---|
| 1 | 1579.6 s (26:21.53 by `/usr/bin/time`) | 456,952 KB |
| 2 | 1591.3 s (26:33.85) | 474,700 KB |

### V4 — the instrument reproduces what is committed — asserted

| what | count | result |
|---|---|---|
| `pfair.ADMIT` re-measured on the fit set through `tz11a.measure_admit` and `tz11a.check_literals` | **7 of 7** | equal |
| `pfair.LINK_NU` re-measured from seven fits on the fit set's admissible populations | **7 of 7** | equal |
| `pfair.LINK_SCALE`, the same | **7 of 7** | equal |
| `tz12.SIGMA_LOG_NU` equal to the frozen literals | **7 of 7** | equal |
| **`tz12.constants` on test 2's admissible rows reproduces the TZ-12 report's §2 test-2 table** | **77 of 77** | **equal, 0 mismatched** |

The 77 values are 7 `tau` × 11 columns — `E`, `k2`, `P0`, `P1`, `crit3`, `P3`, `P_under`, `P_double`, `c4`, `s`, `P4`. `E` and `k2` are compared as integers; `P0`, `P1`, `P3`, `P_under` and `P_double` are compared by their **exact replicate counts**, which is how the TZ-12 report prints them; `crit3`, `c4` and `s` at the six decimals that report prints and `P4` at its four. **This is what proves the gate is applied unchanged**, and a mismatch would have been BLOCKED.

`tz12.SIGMA_LOG_NU` as read: 240: `0.476750` / 180: `0.338445` / 120: `0.361253` / 90: `0.236061` / 60: `0.0876792` / 30: `0.0557673` / 10: `0.0326229`. `tz12.SIGMA_LOG_NU_CENSORED` as read: `{10}`.

### V5 — set identity — asserted

| | |
|---|---|
| fit set hash equals `tz11a.FIT_SHA256` | `6d94a346a47a04a1a0849968effd9023d7585fe628b304ba2ae7a15953ee67f9` ✓ |
| test 1 hash equals `tz11a.TEST1_SHA256` | `3b17729c050e5fbf8fed1bd0877d5dd5c229370609cd672c84eeed1ddc3d5762` ✓ |
| test 2 hash equals `tz12.TEST2_SHA256` | `2dd0fcc4dc2cf379e08c21a4524c3eab799aad7bff3136c37e32910cecb8fa70` ✓ |
| the four sets pairwise disjoint | **6 of 6** intersections empty (3 among the committed three, asserted inside `tz11a.the_sets`; 3 between test 3 and each of them) |
| §3.1's four assertions | **4 of 4**, including the first-400 superset check |
| test 3's own hash | `0f618581ae8be86beed445fc5ad90b8d1d6352271ca8cfd5f5943207011273f2` — **reported, not compared** |

### V6 — the diff — asserted

| | |
|---|---|
| merge base | `2c7694a9833cd408279c6583f3128124cd5a0f85` |
| head | `7ef972397a12bce0cc76b1f58ceda3e5caa43cdc` |
| `git status --porcelain` for the two scoped paths | **empty** |
| `git diff --name-only` | `research/tz13-sized-gate-test3.py` — **one file** |
| attribute stores, `setattr`, `delattr` | **0** |
| `global` or `nonlocal` | **0** |
| `os.environ` writes | **`OPENBLAS_NUM_THREADS`, `OMP_NUM_THREADS`, `MKL_NUM_THREADS`** — exactly the three of §5.1 |
| **the replaced-line list** | **empty — 0 lines** |

The instrument threads a mutable `ledger` dict through `build` rather than rebinding anything, so the once-only outcome read is counted without a `global`, a `nonlocal` or an attribute store.

### V7 — the self-tests — asserted

**6 of 6 items, 31 assertions**, their counts and their verbatim output in §4.2 above.

### V8 — the frozen literals are not moved — asserted

`research/pfair.py` and `research/tz12-sized-gate.py` were hashed at run start and at run end and both equal map §0:

| path | map §0 | run start | run end |
|---|---|---|---|
| `research/pfair.py` | `729f0bcdbee3a629…` | `729f0bcdbee3a629…` | `729f0bcdbee3a629…` |
| `research/tz12-sized-gate.py` | `d2769c201932e2a6…` | `d2769c201932e2a6…` | `d2769c201932e2a6…` |

All **19** `frozen` rows were re-hashed at run end and all 19 still match — the full table is V10. `tz12.SIGMA_LOG_NU` and `tz12.SIGMA_LOG_NU_CENSORED` are printed as read in V4.

### V9 — the capture is untouched — asserted

`tz11a.host_read` at run start, after the walk and at run end, with four assertions between the first and the last:

| assertion | run 1 | run 2 |
|---|---|---|
| the recorder pid unchanged | `[228592]` → `[228592]` ✓ | `[228592]` → `[228592]` ✓ |
| the newest start record unchanged | `recv_ns` 1789206785264516934, sha `4216c046…` ✓ | same ✓ |
| the interval count not fallen | 2,229 → 2,234 ✓ | 2,235 → 2,240 ✓ |
| the read-set hash unchanged | `ddfb68af672635a7…` ✓ | `ddfb68af672635a7…` ✓ |

**The read set** is every five-minute slot from `1789033800` — the first unit the fit set considers — to `1789669800`, test 3's last unit: **2,121 slots, 2,121 directories present, 18,514 files**, hashed by name, size and modification time so that a write to any of them between two reads would change it. The instrument asserts at step 4 that the four set formations consider nothing outside this range.

**Everything the instrument can write**, enumerated: the four files it emits into the `--out` directory (`tz13-results.json`, `tz13-tables.md`, `tz13-observations.csv`, `tz13-host.json`) and `tz13-sizing.json`, written mid-run at step 8. `main` refuses to run at all if the `--out` directory is inside the capture. **Nothing under `/var/lib/btc-recorder/` was created, written, moved or removed, and the recorder was never signalled.** No quote file (`quotes.jsonl.gz`) and no market document was opened, anywhere, for any interval — V2's static half proves no string constant in the instrument even names one.

### V10 — the fingerprint table

Every row of map §0, in lines, bytes and SHA-256, with the new file beside them as it stands on the branch. Read from the working tree during the run; the `origin/main` blobs were hashed separately at §0 and agree row for row.

| path | lines | bytes | state | SHA-256 | equals map §0 |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 695 | 113,563 | reported | `1a15ad90b7eaa6352a4eac01a437ad1bf629a3c57c1965a83567f8dc74992645` | n/a |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | **yes** |
| `research/twap-divergence.py` | 1,135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | **yes** |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | **yes** |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | n/a |
| `research/pfair.py` | 441 | 19,357 | frozen | `729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68` | **yes** |
| `research/selftest-pfair.py` | 619 | 32,559 | frozen | `b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa` | **yes** |
| `research/tz06-calibration.py` | 577 | 27,138 | frozen | `715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f` | **yes** |
| `research/tz07a-variance-time.py` | 623 | 28,414 | frozen | `513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771` | **yes** |
| `research/tz07b-settlement-dispersion.py` | 515 | 24,926 | frozen | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` | **yes** |
| `research/tz08a-out-of-sample.py` | 745 | 38,822 | frozen | `37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c` | **yes** |
| `research/tz09-disk-inventory.py` | 894 | 41,004 | frozen | `b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6` | **yes** |
| `research/tz10b-sigma-or-link.py` | 1,224 | 61,018 | frozen | `406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088` | **yes** |
| `research/tz11a-student-link.py` | 1,231 | 64,732 | frozen | `0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839` | **yes** |
| `research/tz12-sized-gate.py` | 1,157 | 61,637 | frozen | `d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999` | **yes** |
| `research/recorder/recorder.py` | 608 | 25,658 | frozen | `9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03` | **yes** |
| `research/recorder/config.py` | 112 | 4,773 | frozen | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | **yes** |
| `research/recorder/manifest.py` | 254 | 10,002 | frozen | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | **yes** |
| `research/recorder/analyze.py` | 813 | 34,705 | frozen | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` | **yes** |
| `research/recorder/probe.py` | 227 | 9,324 | frozen | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | **yes** |
| `research/recorder/selftest.py` | 573 | 30,591 | frozen | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` | **yes** |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | n/a |
| `research/tz13-sized-gate-test3.py` | 1,074 | 53,901 | new | `a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd` | n/a — new on the branch |

**19 of 19 `frozen` rows match.** `SYSTEM-MAP.md` is a self-reference and is reported: **695 lines, 113,563 bytes, `1a15ad90b7eaa6352a4eac01a437ad1bf629a3c57c1965a83567f8dc74992645`** — the map grew from the 637 lines and 100,096 bytes it records for revision `2026-09-15-a` when this revision was written.

### V11 — disclosure

| what | where |
|---|---|
| test 3's 807 units considered, in ascending `T0`, members and non-members with reasons | `tz13-results.json` → `disclosure`; the 57 non-members are listed in full in §2.1 above; SHA-256 `d8c49f783b6225be3029e3629e7eb58d69c314bf4c127f5c7864ccaf77e4d595` |
| per `tau`, the admissible `T0` list's `tz07b.member_list_sha` and its count | §2.2's domain table — 7 hashes, 7 counts |
| the per-member observations file, one row per member per `tau` | `tz13-observations.csv` — **5,250 rows** plus a header, 2,764,524 bytes, SHA-256 `e78b01b5f06f485d15fe944fb37b17688507d278cb78add5143e12304a322f44`, byte-identical across both runs |

The CSV carries `tz11a.CSV_HEADER`'s 21 columns — `T0`, `set`, `tau`, `admissible`, `label`, `K`, `S_t`, `m_r`, `state`, `sigma_hat`, `ADMIT`, `sd_corrected`, `sd_student`, `z_corrected`, `z_student`, `p_fair_corrected`, `p_t`, `log_phi_z_corrected`, `log_t_cdf_z_student`, `Y`, `r` — **sufficient to reconstruct any single row without re-running**.

### V12 — influence — recorded

Per `tau`, `λ̂` and `ν̂` recomputed without the single most influential member, beside the value §4 reads — the full table is in §2.5. And `crit3` from the first 10,000 null replicates beside the value from 20,000:

| `tau` | `crit3` from 20,000 (rank 19,950) | `crit3` from 10,000 (rank 9,975) | difference |
|---|---|---|---|
| 240 | 9.397211 | 9.398990 | +0.001779 |
| 180 | 8.764159 | 8.979699 | +0.215540 |
| 120 | 8.927718 | 8.805114 | -0.122603 |
| 90 | 8.886025 | 8.868302 | -0.017723 |
| 60 | 8.967324 | 9.197467 | +0.230143 |
| 30 | 9.504963 | 9.287580 | -0.217384 |
| 10 | 7.087974 | 6.690687 | -0.397288 |

The largest half-sample shift is -0.397288 at `tau` 10, against observed likelihood ratios that never exceed 6.230197, and against a smallest `crit3` of 7.087974. **No `tau`'s G3 reading would change under the half-sample `crit3`.**

**Causality is not re-tested and this is why:** every quantity this TZ computes at decision time — `state`, `sigma_hat`, `sd`, `p_t` — is produced by `tz11a.walk_member` and `tz11a.checkpoint_row` unchanged, and TZ-11a V2 and TZ-10b V2 each proved them bit-identical under perturbation strictly after the checkpoint instant, 140 of 140 with 140 of 140 negative controls. This TZ adds no quantity computed at decision time. `Y`, the settlement residual, is a function of the future by construction and is never a subject of a causality check (map §7 item 36).

---

## 6. Publication, and §9

### 6.1 What was written

| path | destination | state |
|---|---|---|
| `research/tz13-sized-gate-test3.py` | branch `tz-13-sized-gate-test3`, then a pull request | **not merged by the Executor** |
| `CryptoReports/TZ-13-sized-gate-test3-report.md` | straight to `main`, one commit | this file |

**Nothing else.** No committed file was modified: every `frozen` row of map §0 is byte-identical at run end (V8, V10). Nothing was pushed to `main` except this report. No Release was created and no dataset, archive or binary entered git history.

### 6.2 §9 — retention

**Step 1 — copy first.** Every file under `/root/tz12-work/` whose SHA-256 is named by any committed report on `main`, and which `/root/btc-forensics/` did not already hold by hash, was copied there by exclusive create (`O_CREAT | O_EXCL`), with the hash asserted at source and at destination.

| | |
|---|---|
| distinct 64-hex strings named by committed reports on `main` | 290 |
| files under `/root/tz12-work/`, excluding `.git` internals | 122 |
| named by a committed report **and copied** | **6** |
| named by a committed report and **already held by hash** | 60 |
| not named by any committed report, not copied | 56 |
| files in `/root/btc-forensics/` **before** | **191** |
| asserted unchanged | **191 of 191** |
| files in `/root/btc-forensics/` **after** | **197** |

The six copied:

```
5bc43954e277fdb7  wt/SYSTEM-MAP.md                  -> tz12-work--wt--SYSTEM-MAP.md
cb845f93f61cc855  wt/CryptoTZ/TZ-12-sized-gate.md   -> tz12-work--wt--CryptoTZ--TZ-12-sized-gate.md
d2769c201932e2a6  wt/research/tz12-sized-gate.py    -> tz12-work--wt--research--tz12-sized-gate.py
a7b81f74efcec68f  run-2/tz12-bootstrap.csv          -> tz12-work--run-2--tz12-bootstrap.csv
af7ef999e30964d9  run-2/tz12-results.json           -> tz12-work--run-2--tz12-results.json
853b86cb8b74a1ff  run-2/tz12-tables.md              -> tz12-work--run-2--tz12-tables.md
```

TZ-12's run-1 outputs hash identically to its run-2 outputs — that TZ's own V3 — so they deduplicate against the copies just made and are not stored twice. **Nothing was removed from `/root/btc-forensics/`.**

**Step 2 — the worktree.** `git worktree remove /root/tz12-work/wt` **without `--force`**, exit 0. `test -e /root/tz12-work/wt` afterwards: **gone**. `git worktree list` now shows two entries, `/root/btc-5m-twap` on `main` and `/root/tz13-work/wt` on this TZ's branch.

**Step 3 — the tree. NOT DONE — the session's permission classifier refused it.** `rm -rf /root/tz12-work`, one command naming one tree, was denied with *Irreversible Local Destruction*. This is the same refusal TZ-12 met and the opposite of TZ-10b, where a single-tree `rm -rf` was allowed; the classifier's behaviour on this command is not stable across sessions. **Per §9 the Boss is handed one exact block**, and the outcome will be verified from `test -e`, never from his report (map §6):

```bash
rm -rf /root/tz12-work
test -e /root/tz12-work && echo STILL-THERE || echo GONE
```

`/root/tz12-work` stands at **2,954,530 bytes**, 122 files, with its git worktree already removed and every file a committed report names already preserved in `/root/btc-forensics/`. **Nothing is lost if it is deleted, and nothing is at risk while it waits.**

`/root/tz13-work/` is the next TZ's to reclaim on the same terms. **The capture is never deleted.**

---

## 7. Every point where the text needed a reading, and every workaround chosen

In the shape TZ-11a and TZ-12 used. **Six readings, one workaround, and one measured correction to §6's cost model.**

### R1 — `tz12.verdict` returns a family verdict; §4.1 asks for a per-`tau` one

**The text.** §3.5 says "the per-`tau` verdict by `tz12.verdict(per_tau)`". §4.1 says "DISQUALIFIED if any gate FAILs. NOT DISQUALIFIED only if G1 and G3 both PASS with power and no gate FAILs. UNDECIDABLE otherwise."

**What the committed file does.** `tz12.verdict` takes the seven `tau`'s readings *together* and returns one family-level answer — `CLOSED`, `UNDECIDED` or `NOT DISQUALIFIED` — with an `admitted` list. It cannot return a per-`tau` verdict; that is not its shape.

**The reading taken.** `tz12.verdict` is called **unchanged**, on the committed readings and again on the weakened ones, and both its answers are reported: **NOT DISQUALIFIED**, admitting `240, 180, 120, 90, 60`, in both cases. §4.1's per-`tau` verdict is then derived from the same readings by §4.1's own rule, which is the only rule the TZ states for it. The two agree by construction: the `tau` §4.1 calls NOT DISQUALIFIED are exactly `tz12.verdict`'s `admitted` list.

### R2 — §4's G4 names three UNDECIDABLE clauses; the committed `tz12.readings` carries one

**The text.** §4 G4: "UNDECIDABLE if `P4 < tz12.POWER_TO_PASS`, if `tau` is in `tz12.SIGMA_LOG_NU_CENSORED`, or if the fit lands on a search edge as `tz11a.bound_note` reports it." §3.5: the readings are "produced by `tz12.readings(consts, observed)` … and then weakened by §4.3 and by nothing else."

**What the committed file does.** `tz12.readings` returns `UNDECIDABLE` for G4 **only** when `consts["censored"]` is set. It takes `observed["nu_on_bound"]` and passes it straight through to its output without reading it, and it never looks at `P4`. So two of §4's three clauses are not in the committed function.

**The tension.** §3.5 forbids weakening by anything but §4.3, yet §4 — the section titled "The gate" — states clauses §4.3 cannot produce: `P4` = 0.0048 at `tau` 240 is nowhere near the straddle band, so §4.3 will never turn that G4 into UNDECIDABLE, but §4 says it is.

**The reading taken.** §4 is the definition of the gate and §3.5 is the description of how it is computed, so §4 controls. `tz12.readings` is called unchanged; §4's two further G4 clauses are then applied in a separate function that **can only turn a reading into UNDECIDABLE**, never the reverse; §4.3's band is applied last. **The committed reading is reported beside the weakened one at every `tau`, so both are on the record.**

**And it changed nothing.** G4 does not FAIL at any `tau` on test 3 — the largest `|log(ν̂ / LINK_NU)|` is 1.137481 at `tau` 240 against a `c4` of 2.224364. Since §4.1 reads G4 only through "no gate FAILs", and G4 never PASSes under any reading, **the per-`tau` verdict is identical at all seven `tau` under both readings.** The clause that moved is recorded — G4 reads `NO FAIL` under the committed function and `UNDECIDABLE` under §4 at `tau` 240, 180, 120 and 90 — and the answer does not depend on which is preferred.

### R3 — §3.6 asks for a row multiset; `tz12.constants` asserts one row per member

**The text.** §3.6: "`tz12.constants` is called two more times on row multisets built by repeating test 3's admissible rows for that `tau` twice and three times."

**What the committed file does.** `tz12.constants` opens with `assert t0s == sorted(set(t0s))` — one row per member, in ascending `T0`. A literal multiset of repeated rows has duplicate `T0`s and **fails that assertion immediately**. The call §3.6 asks for cannot be made against the file as committed.

**The workaround chosen.** Each copy carries the synthetic key `T0 * multiple + copy_index`, which is strictly increasing across the whole multiset and unique within it, so the committed assertion passes untouched. **The `T0` enters that assertion and `members_sha256` and nothing else**: `constants` reads its statistics from `z_student` and `p_t` alone, and every one of them — the grid tables, the bin counter, the Brier scores, the likelihood ratio — is invariant to the order and the labels of the rows. `tz12-sized-gate.py` was not modified.

**This is a projection either way** and §3.6 already says so; the workaround does not make it more or less one. No verdict, threshold or admission reads the table.

### R4 — §6's walked-member count omits the fit set

**The text.** §6 budgets "walk of 1,150 members", and C5 derives 1,150 as "§3.1 plus test 2's 400 in V4" — test 3's 750 plus test 2's 400.

**Why that is short.** V4's first two assertions re-measure `pfair.ADMIT` through `tz11a.measure_admit(walked, fit)` and `pfair.LINK_NU` and `pfair.LINK_SCALE` from seven fits over **the fit set's admissible populations**. Both need the fit set's 400 members walked. The true count is **1,550** — test 3's 750, test 2's 400 and the fit set's 400.

**What was done.** All 1,550 were walked. **Test 1 was not walked**: it is formed for §3.1's disjointness assertion and its hash check, and nothing below reads a row of it — which keeps the count at 1,550 rather than 1,950. The walk is not the run's dominant cost and the overrun is not where §6's estimate went wrong; see R6.

### R5 — V3's "three deterministic outputs" against a mid-run file and two clock-bearing ones

**The text.** V3: "the three deterministic outputs byte-identical … A file holding a clock reading is not compared and is named."

**The reading taken.** The run emits five files. `tz13-tables.md`, `tz13-observations.csv` and `tz13-sizing.json` are the three deterministic outputs and are **byte-identical across the two runs by `cmp` and by SHA-256 pair**. `tz13-results.json` and `tz13-host.json` hold clock readings and are named as such, exactly as V3's rule provides — §3.3 requires the report to state two instants and §3.4 a third, and they have to be recorded somewhere.

**Beyond what V3 asks**, `tz13-results.json`'s difference was enumerated field by field: **7 scalar fields differ and all 7 are UTC instants**, and with those normalised the two files hash identically. No measured quantity moved.

`tz13-sizing.json` is the file §3.3 requires to be on disk before §3.4 begins. It is a strict subset of `tz13-results.json`'s content and is compared as one of the three.

### R6 — §6's cost model is low by about a factor of two, and the shortfall is §3.6

**The text.** §6: ~770 s per run, ~1,540 s for the session, with §3.6's projection at ~375 s as "five times the base".

**What was measured.** A full run took **1580 s** and **1591 s**. The projection is the gap: `tz12.constants` is dominated by `grid_tables`, which builds two `n × 2,501` float64 tables through `pfair.log_t_cdf` in pure Python. That cost is close to linear in `n`, so the 1× + 2× + 3× sequence costs about **six** times the 1× call, not five, and the 1× call itself is on ~521 admissible rows rather than the ~436 §6 assumes.

**No gate was affected.** Both of the TZ's own fail-fasts were evaluated in full and both passed with room: the first `tz12.constants` call at **18.37 s** against 120 s, and the implied `35 t + 500` projection at **1143 s** against 3,000 s. The session's two runs total **3171 s** against `tz12.SESSION_CEILING_S` = **3,600 s**. Nothing was sampled to save time — §3.2's guarded pass is the one sampled quantity and it is sampled under §3.2's own rule, as a guard and not as a measurement.

**A note for the Architect:** a third run in this session would have exceeded the ceiling. If a later TZ wants both a projection and a third run, the projection wants a cheaper `grid_tables` — vectorising `pfair.log_t_cdf` over the λ grid would pay for itself several times over, and it is a change to a frozen file, so it needs a TZ that authorizes it.

### W1 — the one workaround, restated plainly

R3's synthetic `T0` keys are the **only** place where this run did something other than what a committed function does with the arguments the TZ names. It was forced by an assertion inside `tz12.constants` that §3.6's instruction cannot satisfy, it touches a field no statistic reads, and it is confined to a table that is barred from every gate. Everything else — the set rule, the walk, the rows, the domain, the sizing, the outcome read, the four gates and the verdict — ran the committed code on the arguments the TZ specifies.

---

## 8. What this does and does not establish

**Established.** Under TZ-12's sized gate, applied once to a set of 750 intervals no one had scored and whose outcomes no one had read: **no gate FAILs at any `tau`.** At `tau` 240, 180, 120, 90 and 60 the gate had the power to catch a 1.5× overconfidence at least half the time and did not fire. Those five `tau` are **NOT DISQUALIFIED** and are admitted to Phase 2.

**Not established.** `tau` 30 and 10 read **UNDECIDABLE**: G3's power against the named alternative is 0.3230 and 0.0495, below the 0.5 floor, so its silence carries no information. They close nothing and admit nothing.

**Not established, and cannot be by this TZ.** That the pricer has an edge. Phase 1 can only disqualify. Five `tau` survived a test that was sized to catch a specific, named failure; that is the whole of the claim.

**Worth the Architect's attention.** `λ̂` is **below 1 at `tau` 90, 60 and 30** (0.8844, 0.7436, 0.6855) — the data prefer a *narrower* scale than the pricer uses, which is under-confidence, the opposite of the alternative G3 is sized against. `P_under`, the power against λ = 1/1.5, is 0.6500 at `tau` 60 and 0.0850 at 30, so the gate is weaker in that direction where the drift actually is. A gate sized against overconfidence alone will not see this, and the observed Brier — 0.040467 at `tau` 60, against 0.2496 — says the predictions are far from uninformative while their scale is drifting.

---

**A report is evidence, not acceptance.** No verdict of this TZ is final until the Architect has re-derived its gate arithmetic. Every figure above is reproducible from `research/tz13-sized-gate-test3.py` at `7ef9723` on branch `tz-13-sized-gate-test3`, run as `python -B tz13-sized-gate-test3.py --out <directory>`.
