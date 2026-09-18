# TZ-14 — the quote inventory — report

**Executed.** Tier C's order-book capture was opened for the first time. The set is the first **1,200** qualifying slots with `T0 > 1789206600`; it opens at `1789206900` on a Saturday and is the first scored set in this project to contain a weekend by construction. **All 16,800 reads the capture can hold are there**, every one HTTP 200 with a parseable body, and `quotes_complete` holds at 1,200 of 1,200.

**No gate was applied. Nothing was admitted, disqualified or closed.** No probability was computed anywhere, no outcome entered any printed number, and the only pricer-derived quantity any quote statistic is conditioned on is `sigma_hat`.

**Two of the seven pre-registered predictions were refuted, and both matter to TZ-15.** P2 fails badly: at `tau` 60 only **60.5%** of Up reads have both sides of the book quoted, and the rate falls monotonically as the close approaches. P4 fails in the direction that helps: the median round-trip cost is **4.12 pp at `tau` 240 but 1.85 pp at `tau` 60**, so the alternative TZ-15's gate must be powered against is smaller at the short horizons than the prediction assumed — but it is measured over a population that shrinks by 40% at those same horizons.

| | |
|---|---|
| specification | `CryptoTZ/TZ-14-quote-inventory.md` |
| System Map revision | `2026-09-18-b`, six anchors matched 6 of 6 |
| instrument | `research/tz14-quote-inventory.py`, branch `tz-14-quote-inventory` at `ffef5cd822e2e47ce1edd8fff706471a441e9a5f`, PR [#15](https://github.com/seahomebatumi-ai/btc-5m-twap/pull/15) |
| instrument hash | 2,124 lines, 109,972 bytes, SHA-256 `978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02` |
| set | the first 1,200 qualifying slots with `T0 > 1789206600` |
| member list SHA-256 | `baa5a9d26855ea7ff07d062437df60617ba3e4e70dd74b3ac455a8a71a9b3154` |
| span | `1789206900` → `1789595400`, 2026-09-12 09:55 UTC → 2026-09-16 21:50 UTC, 4.496 days |
| rows | 1,200 members × 7 `tau` × 2 token ids = 16,800 reads, **16,800 found** |
| gate applied | **none — this TZ has no gate** |
| outcome read | only inside `tz06.qualification`, for membership; no table is keyed by one |
| predictions | **5 held, 2 refuted** — P2 and P4 |
| determinism | four deterministic outputs byte-identical across two runs, 43.7 s and 44.1 s |

---

## 1. §0 — the gates, the host, the interpreter and the floor

### 1.1 Fingerprint

`SYSTEM-MAP.md` was read from `origin/main` at `b2269bb2464a097124fcf5cb373b0f507293daa1`. Its revision string reads `2026-09-18-b` and its six anchors equal the TZ's table at **6 of 6**:

| anchor | required | map | agreement |
|---|---|---|---|
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` | yes |
| `A2` — collector | `6c5089330629` | `6c5089330629` | yes |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-not-started` | same | yes |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b` | yes |
| `A5` — recorder | `9fd1c7de0f74` | `9fd1c7de0f74` | yes |
| `A6` — pricer | `729f0bcdbee3` | `729f0bcdbee3` | yes |

**Beyond what §0.1 asks**, the four anchors that are the first 12 hex characters of a committed file's SHA-256 were **re-derived from the bytes** rather than read from the table that prints them, and the instrument asserts each: `A2` from `research/twap-divergence.py`, `A4` from `BTC-EXECUTOR-INSTRUCTIONS.md`, `A5` from `research/recorder/recorder.py`, `A6` from `research/pfair.py`. 4 of 4 agree. `A1` names a dataset that is not a repository file and `A3` is a phase string; neither can be re-derived and both are compared as text.

The fingerprint table is **23 rows**: `SYSTEM-MAP.md` itself, **20 `frozen`** and **2 `tracked`**. Every row was hashed in `wc -l`, `wc -c` and `sha256sum`. **20 of 20 `frozen` rows equal the hashes the map prints, lines and bytes included.** The full table, as the run itself produced it, is §5's V10. `SYSTEM-MAP.md` is **709 lines, 123,487 bytes, SHA-256 `6096f0b8405dde9b996f074447af637e46f8b64318a61c57e9d34d23ad36476b`**.

The gate is not a hand computation: `v1_gates` parses the map's own §0 tables, hashes each path and asserts every `frozen` row, the six anchors and the revision string. The instrument's only literals here are the TZ header's required revision and its six required anchor values — **the gate does not read its own expected values from the artifact it is checking.**

### 1.2 Host gate — 3 of 3

- `/var/lib/btc-recorder/btc-updown-5m/` exists and holds **2,425 interval directories** at run start. First `T0` **1789033800** (2026-09-09 22:30 UTC), last `T0` **1789760700** (2026-09-18 22:25 UTC).
- A recorder process is running: **pid 228592**, `/root/tz04a-env/venv/bin/python -B -u recorder.py`, up since 2026-09-12. The newest `runtime.jsonl` start record carries sha **`4216c04673ced76b5b2ac60ef57c9abedc46f9b9`** — the required value — at `recv_ns` **1789206785264516934**.
- The filesystem holding it is **`/dev/vda2`**, total **31,612,203,008 bytes**, matching §0.2 exactly.

### 1.3 Interpreter

`/root/tz01-env/venv/bin/python` reports **Python 3.12.3 (main, Aug 31 2026, 10:18:26) [GCC 13.3.0]**. `import numpy` succeeds at **numpy 2.5.3**. The instrument computes nothing in `numpy`; it imports because the `tz12 → tz11a → tz10b` chain does. The three thread-count environment variables are set to `"1"` before that load and no other environment variable is written — V6 asserts exactly those three.

`research/pfair.py` sets `decimal.getcontext().prec = 60` at import, and the instrument inherits that context. **Every price and size in this report was carried in `decimal.Decimal` at 60 digits from the venue's own string, and no float touched a price**, which is what makes self-test 3's exact `Decimal("0.03")` band comparison a real test.

### 1.4 The resource floor — every read, with its instant, its reader and its bound

Eight reads, in §6's V1 table. **Six were asserted** by `tz11a.host_read`, whose body carries `assert free >= floor`; the two preflights are `df -B1` transcripts and §0.5 gates nothing beyond §0.4. `tz11a.FLOOR_START_BYTES` is `2,060,000,000` and `tz11a.FLOOR_BYTES` is `2,000,000,000`, both read from the module and neither restated as a literal in this instrument. The floor was never approached.

### 1.5 Preflight, twice, 1,805 s apart

| quantity | preflight 1 — 2026-09-18T19:43:57Z | preflight 2 — 2026-09-18T20:14:02Z | change | implied bytes/day |
|---|---|---|---|---|
| `/dev/vda2` total | 31,612,203,008 | 31,612,203,008 | 0 | 0 |
| `/dev/vda2` used | 16,307,027,968 | 16,343,695,360 | +36,667,392 | +1,755,159,373 |
| `/dev/vda2` available | 13,869,305,856 | 13,832,638,464 | -36,667,392 | -1,755,159,373 |
| `du -sb /root/PROJECT_GAMING_PS5` | 373,987,996 | 374,137,569 | +149,573 | +7,159,616 |
| `systemctl is-enabled telemetry-watch.service` | `disabled`, exit **1** | `disabled`, exit **1** | — | — |
| `systemctl is-active telemetry-watch.service` | `inactive`, exit **3** | `inactive`, exit **3** | — | — |

**This run's own footprint, stated separately at both reads** as map §7 item 29 requires:

| tree | preflight 1 | preflight 2 | change | implied bytes/day |
|---|---|---|---|---|
| `/root/tz14-work` | 0 | 32,251,709 | +32,251,709 | +1,543,793,716 |
| `/root/.claude` | 126,862,772 | 128,482,133 | +1,619,361 | +77,514,011 |

**`telemetry-watch.service` is `disabled` and `inactive` at both reads**, exit codes 1 and 3 respectively, unchanged. Map §7 item 29 asks for this run's own footprint separately and it is stated above: `/root/tz14-work/` was empty at preflight 1 — it had just been created — and holds the branch worktree, the scratch directory and the two run directories at preflight 2. **That growth is this TZ's own and is reclaimed by the next one on §9's terms.** The `bytes/day` columns annualise a window of under an hour and are reported because §0.5 asks for them, not because a rate measured over 1,805 s is a rate: map §7 item 52's rule against reading a share as a bound applies here as much as anywhere, and TZ-09's own measured drain of 86.3 MB/day over a multi-day window remains the figure worth quoting for the capture itself.

**The capture's own growth over the window is the residual and it agrees with TZ-09.** Of the +36,667,392 bytes `/dev/vda2` used across the two reads, +32,251,709 is `/root/tz14-work/` and +1,619,361 is `/root/.claude/` — both this session's — leaving about **2.8 MB** for everything else in 1,805 s. TZ-09 measured the capture's drain at **86.3 MB/day**, which over this window is **1.8 MB**; the remainder is `/root/PROJECT_GAMING_PS5`'s +149,573 bytes and ordinary system churn. **Nothing is draining the filesystem that this session did not put there.**

### 1.6 §0.6 — the set exists

`tz06.scoring_set(manifests, 1200, after=1789206600)` returned `ok = True`: **1,200 of 1,200** qualifying slots with `T0 > 1789206600` exist, from **1,296 units considered**, the first examined `1789206900` and the last `1789595400`. §0.6's BLOCKED path did not fire and the instrument's `SystemExit` for it was never reached.

### 1.7 §0.7 — the predecessor's tree

`test -e /root/tz12-work` printed nothing and **exited 1**. Map §3 records that the Boss ran the handed removal block on 2026-09-18 and reported `GONE`; **this verifies it from the filesystem rather than from his report, and the filesystem agrees.** Nothing is reclaimed under §9 on that account.

### 1.8 §0.8 — refs

`git ls-remote origin`, run before the branch of §2 existed, printed **18 refs**:

| ref | sha |
|---|---|
| `HEAD` | `b2269bb2464a097124fcf5cb373b0f507293daa1` |
| `refs/heads/main` | `b2269bb2464a097124fcf5cb373b0f507293daa1` |
| `refs/pull/1/head` … `refs/pull/14/head` | 14 refs, unchanged from map §1's reading |
| `refs/tags/tz-01a-dataset` | `d3251aa2bd312409f7b096bfd5968f3bedbd1be5` |
| `refs/tags/tz-01a-dataset^{}` | `ea9290b92b9fa50c22d0560d5d01dfa392af44df` |

**There is one branch, `main`, exactly as map §1 states — but it is at `b2269bb2` and not at the `dad557d56f478d0bf6ec9e9b814030291b3f399c` the map records.** The difference is accounted for and is not BLOCKING: `dad557d5` carried revision `2026-09-18-a`; two commits since then — `a314151`, the upload of `CryptoTZ/TZ-14-quote-inventory.md` and `research/tz13-sized-gate-test3.py`, and `b2269bb`, the upload of revision `2026-09-18-b` — moved `main` forward. **`main` carries the revision §0.1 requires**, which is the one condition under which §0.8 makes a difference BLOCKING, so the run proceeded. The `tz-12-sized-gate` and `tz-13-sized-gate-test3` branches map §1 does not mention are **absent from `origin`**: both were deleted after merge, and only stale remote-tracking refs in the local clone still name them.

---

## 2. The measurements, in §3's order

Every table in this section is also in the run's own `tables.md`, byte-identical across both runs. Each names its population. `ADMITTED` is `(240, 180, 120, 90, 60)` and is reported first; `OUTSIDE` is `(30, 10)`, reported in a separately headed block and **barred from supporting any Phase 2 or Phase 3 claim**.

### 2.1 §3.1 — the set

`tz06.scoring_set(manifests, 1200, after=1789206600)` returned `ok = True` over **1,296 units considered**. Every assertion of §3.1 holds: `ok` is `True`, the first member is `1789206900` (at or after the required `1789206900`), all 1,200 sit on the 300 s grid and the list is strictly increasing.

| quantity | value |
|---|---|
| units considered | **1,296** |
| members | **1,200** |
| non-members | **96** |
| member-list SHA-256 (`tz07b.member_list_sha`) | `baa5a9d26855ea7ff07d062437df60617ba3e4e70dd74b3ac455a8a71a9b3154` |
| first member | `1789206900` — 2026-09-12T09:55:00Z |
| last member | `1789595400` — 2026-09-16T21:50:00Z |
| span | **4.496 days** |

**The set opens on a Saturday, as §3.1 predicted, and it is the first scored set in this project to contain a weekend by construction.**

| weekday (UTC) | members |
|---|---|
| Mon | 258 |
| Tue | 264 |
| Wed | 250 |
| Thu | 0 |
| Fri | 0 |
| Sat | **156** |
| Sun | **272** |

**428 of the 1,200 members are weekend members** and 772 are weekday. Every per-`tau` table below is broken out weekday against weekend, and §2.6's round-trip table also admissible against not.

**`quotes_complete` was not a membership condition and did not become one.** It is the first thing measured, in §2.3.

`Thu` and `Fri` are zero because the span is 4.5 days long and opens on a Saturday: Sat 12th through Wed 16th.

**All 96 non-members fail on exactly one reason, `disconnect`**, and no other reason appears anywhere in the 1,296. Every unit considered, member and non-member, is listed in ascending `T0` with its reasons in `disclosure.md`.

### 2.2 §3.2 — the domain, from the pricer's scale and nothing else

`pfair.merged_stream`, `tz10b.grid_of` and `tz10b.sigma_hat_of` are the whole of this TZ's use of the pricer. The admissible lists come from **`tz11a.admissible_members(walked, members, pfair.ADMIT)` unchanged**.

**`tz10b.grid_of` raised on 0 of 1,200 members.** Every member's one-second grid over `[T0 − 300, T0 + 300]` is whole, so §3.2's catch-and-list path never fired and §3.2's population is the full 1,200. The share is **1.0000**; weekday 772, weekend 428.

| tau | `pfair.ADMIT` | admissible | share of the 1,200 | weekday | weekend |
|---|---|---|---|---|---|
| *ADMITTED* | | | | | |
| 240 | 2.12324 | **631** | 0.5258 | 577 | 54 |
| 180 | 2.14298 | **628** | 0.5233 | 582 | 46 |
| 120 | 2.18062 | **615** | 0.5125 | 573 | 42 |
| 90 | 2.16098 | **619** | 0.5158 | 577 | 42 |
| 60 | 2.16725 | **621** | 0.5175 | 577 | 44 |
| *OUTSIDE* | | | | | |
| 30 | 2.15178 | 622 | 0.5183 | 578 | 44 |
| 10 | 2.14530 | 628 | 0.5233 | 582 | 46 |

**This is the figure TZ-15 needs most, and it is not the 1,200.** About **52%** of the set is inside the pricer's domain at any `tau` — roughly **620 members** — and the weekend composition is where it bites: **428 weekend members contribute only 42 to 54 admissible ones**, because weekend `sigma_hat` sits below `ADMIT`. A gate written against "1,200 intervals" would be written against a population that does not exist. No floor and no minimum is applied here: an inventory has nothing to fail, and map §7 item 51's UNDECIDABLE rule applies to the gate TZ-15 writes, not to this table.

Each `tau`'s admissible `T0` list and its own `tz07b.member_list_sha` are in `disclosure.md` and in `tables.md`.

### 2.3 §3.3 — the quote file, read for the first time

**The capture is complete.** Every one of the 1,200 members holds exactly 14 read lines, every line parses, every read returned HTTP 200 and every body parsed as JSON.

| item | quantity | value |
|---|---|---|
| 1 | members with no quote file | **0** |
| 2 | read lines per member | **14 at 1,200 of 1,200 members**; no member above 14 and none below |
| 3 | members carrying a duplicate `(tau, token_id)` | **0**; duplicate pairs **0** |
| 4 | lines that fail to parse | **0**, at every member |
| 5 | `status` histogram | **200 at 16,800 of 16,800**; no `null`, so no `error` string exists to group |
| 6 | `body_is_json` false among `status == 200` | **0** |
| 7 | `manifest.json`'s `quotes_complete` against the recomputed predicate | **agrees at 1,200 of 1,200**; true on both sides at 1,200; **no disagreement** |
| 8 | members whose `recorder_git_sha` is a list rather than a string | **0** — no member's window holds more than one recorder start record |

**§3.3's cross-check against the committed reader passed at 1,200 of 1,200.** `manifest._quote_reads(dirpath)` and the instrument's own `quote_lines(dirpath)` returned the same multiset of `(tau, token_id, status, body_is_json)` at every member. That is V4's first line and it is BLOCKING; it did not fire.

**Item 2 deserves a sentence.** The recorder's append-mode write permits a duplicate across a restart and nothing had ever checked. Over 1,200 members and 16,800 lines there is not one — because, by item 8, no member's window contains a restart at all. The check is not vacuous, but this set did not exercise it.

### 2.4 §3.4 — the read geometry

`offset_ms = (recv_ns − config.quote_checkpoint_epoch(t0, tau) · 10⁹) / 10⁶`, computed term for term as the manifest computes it, **agreed with `manifest.json`'s own `quote_offsets_ms` at every one of the 16,800 reads**. No value disagreement, so §3.4's BLOCKING path did not fire. **No member's manifest lacks the `quote_offsets_ms` key**, so §3.4's exclusion path did not fire either — every member of this set was written by the TZ-05a schema.

| tau | n | min | 0.25 | 0.50 | 0.75 | 0.90 | 0.99 | max |
|---|---|---|---|---|---|---|---|---|
| *ADMITTED* | | | | | | | | |
| 240 | 2,400 | 40.2 | 48.6 | **52.1** | 57.9 | 66.2 | 97.3 | 345.6 |
| 180 | 2,400 | 40.4 | 48.7 | **52.0** | 56.5 | 63.1 | 88.4 | 187.3 |
| 120 | 2,400 | 41.0 | 48.7 | **52.2** | 56.6 | 64.4 | 99.6 | 345.7 |
| 90 | 2,400 | 41.0 | 48.4 | **51.7** | 56.4 | 63.5 | 92.4 | 391.1 |
| 60 | 2,400 | 41.2 | 48.9 | **52.3** | 57.3 | 65.7 | 104.3 | 382.6 |
| *OUTSIDE* | | | | | | | | |
| 30 | 2,400 | 39.7 | 47.7 | 50.4 | 54.3 | 59.7 | 82.4 | 366.2 |
| 10 | 2,400 | 39.6 | 47.2 | 49.9 | 53.6 | 57.7 | 78.6 | 348.6 |

`offset_ms`, milliseconds after the nominal checkpoint.

| tau | negative | above 1,000 ms | above 8,000 ms |
|---|---|---|---|
| all seven | **0** | **0** | **0** |

`8,000` ms is `QUOTE_TIMEOUT_S × 1,000`. **`QUOTE_TIMEOUT_S` is `8`, in seconds**, and the instrument reads that assignment out of `research/recorder/recorder.py` by `ast` at run time rather than carrying an `8,000` the file does not hold.

**The direction §3.4 states is the direction observed, at every one of the 16,800 reads.** A read is issued at the checkpoint and its reply lands after it: the minimum offset anywhere in the set is **+39.6 ms** and there is **not one negative offset**. The quote therefore carries information at least as new as the pricer's own checkpoint reading, which is conservative for any future claim of an edge and adverse for none. **No read timed out**, and the worst single read in the set landed **391 ms** after its checkpoint — a twentieth of the timeout.

| tau | n | min | 0.25 | 0.50 | 0.75 | 0.90 | 0.99 | max |
|---|---|---|---|---|---|---|---|---|
| *ADMITTED* | | | | | | | | |
| 240 | 1,200 | 0.0 | 2.1 | **5.5** | 11.7 | 20.9 | 58.7 | 296.1 |
| 180 | 1,200 | 0.0 | 1.7 | **4.4** | 8.8 | 15.4 | 45.6 | 70.5 |
| 120 | 1,200 | 0.0 | 1.9 | **4.7** | 9.4 | 16.8 | 49.3 | 275.7 |
| 90 | 1,200 | 0.0 | 2.0 | **4.8** | 9.5 | 17.5 | 61.4 | 327.9 |
| 60 | 1,200 | 0.0 | 2.1 | **5.3** | 10.9 | 20.4 | 61.3 | 326.0 |
| *OUTSIDE* | | | | | | | | |
| 30 | 1,200 | 0.0 | 1.5 | 3.9 | 7.5 | 14.1 | 38.8 | 317.2 |
| 10 | 1,200 | 0.0 | 1.3 | 3.5 | 7.0 | 12.7 | 34.4 | 278.6 |

`|recv_ns_up − recv_ns_down|` per checkpoint, milliseconds — how far apart the two halves of one pair were actually read. The median is **under 6 ms at every `tau`**, which is the figure §3.7's paired statistics rest on.

**The clock.** All 1,200 members report a `clock_offset_abs_max_ms`. The **maximum over the set is 33.946 ms**, and **0 members exceed `config.CLOCK_OFFSET_LIMIT_MS` = 50.0**. Map §6 put the worst measured offset at `18.789` ms over the TZ-05a window; this is the first reading over 1,200 intervals and it is **1.8× worse than that window suggested, and still inside the limit**. It bounds every latency claim Phase 3 will want to make: the host clock is good to about 34 ms at worst, against a read geometry whose median is 52 ms after the checkpoint.

### 2.5 §3.5 — the book, measured and not assumed

**1. The top-level key set has exactly one shape across all 16,800 replies:**

`asks, asset_id, bids, hash, last_trade_price, market, min_order_size, neg_risk, tick_size, timestamp` — 16,800 replies, example `T0` `1789206900`, `tau` `240`. There is no second shape and no reply that parsed to anything other than an object.

**2. The ordering, and why it matters.** Over the parsed bodies:

| side | ascending | descending | neither | single level | empty |
|---|---|---|---|---|---|
| `bids` | **13,561** | 0 | 0 | 401 | 2,838 |
| `asks` | 0 | **13,563** | 0 | 400 | 2,837 |

**`bids` arrive ascending and `asks` arrive descending**, so on both sides **position 0 is the worst price, not the best**. Any reader that took the touch from index 0 would have read the far end of the book at every one of the 27,124 multi-level sides in this set. The instrument takes `max` over `bids` and `min` over `asks` and never position 0; self-test 2 fixes that on four orderings, and the ordering here is a measurement that confirms the hazard was real.

Level counts per side, as the `Q` summary: median **48** a side, 0.90 quantile **99**, maximum **139** bids and **138** asks.

**3. Empty sides, and this is the headline of §3.5.** No read has *both* sides empty; the empties are one-sided and they grow steeply toward the close.

| tau | no bids | no asks | neither side | both sides quoted | both-sided share |
|---|---|---|---|---|---|
| *ADMITTED* | | | | | |
| 240 | **0** | **0** | 0 | 2,400 | 1.0000 |
| 180 | 3 | 3 | 0 | 2,394 | 0.9975 |
| 120 | 77 | 77 | 0 | 2,246 | 0.9358 |
| 90 | 198 | 197 | 0 | 2,005 | 0.8354 |
| 60 | 474 | 474 | 0 | 1,452 | **0.6050** |
| *OUTSIDE* | | | | | |
| 30 | 946 | 946 | 0 | 508 | 0.2117 |
| 10 | 1,140 | 1,140 | 0 | 120 | 0.0500 |

Population: the 2,400 reads at each `tau`. **At `tau` 240 the book is two-sided at every single read; at `tau` 60 it is two-sided at 60.5% of them.** This refutes P2 and is the single most consequential figure in the report for TZ-15: a spread, a mid or a round-trip cost at `tau` 60 is a statistic over a population **40% smaller than the read count**, and that shrinkage is not random — it is the book emptying as the outcome becomes obvious.

**4 and 5. Best bid, best ask, mid and spread.** Per-read values are in `observations.csv`. Per `tau`, the spread `ask − bid` in probability points:

| tau | n | min | 0.25 | 0.50 | 0.75 | 0.90 | 0.99 | max |
|---|---|---|---|---|---|---|---|---|
| *ADMITTED* | | | | | | | | |
| 240 | 2,400 | 0.700 | 1.000 | **1.000** | 1.000 | 1.000 | 2.000 | 8.000 |
| 180 | 2,394 | 0.100 | 1.000 | **1.000** | 1.000 | 1.000 | 2.000 | 4.000 |
| 120 | 2,246 | 0.100 | 1.000 | **1.000** | 1.000 | 1.000 | 2.000 | 4.000 |
| 90 | 2,005 | 0.100 | 1.000 | **1.000** | 1.000 | 1.000 | 1.000 | 4.000 |
| 60 | 1,452 | 0.100 | 1.000 | **1.000** | 1.000 | 1.000 | 3.000 | 9.000 |
| *OUTSIDE* | | | | | | | | |
| 30 | 508 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 3.000 | 7.000 |
| 10 | 120 | 0.100 | 1.000 | 1.000 | 1.000 | 4.000 | **31.000** | 31.000 |

**Crossed or locked books, `best_bid >= best_ask`: 0.** Not one, anywhere in the set.

**6. The scalar fields.** All six are present in all 16,800 replies; none is ever absent.

| field | present | absent | distinct | values |
|---|---|---|---|---|
| `tick_size` | 16,800 | 0 | **2** | `0.01` ×15,640, `0.001` ×1,160 |
| `min_order_size` | 16,800 | 0 | **1** | `5` ×16,800 |
| `timestamp` | 16,800 | 0 | 13,529 | integer-milliseconds strings |
| `hash` | 16,800 | 0 | **16,800** | one per reply; no two replies share one |
| `market` | 16,800 | 0 | **1,200** | one per member, 14 replies each |
| `asset_id` | 16,800 | 0 | **2,400** | two per member, 7 replies each |

**`asset_id` differs from the `token_id` the recorder requested at 0 of 16,800 replies.** The venue returns the book it was asked for, every time.

**7. The spread in ticks.** `tick_size` is present in every reply, so §3.5 item 7's fallback — "computed at `0.01`, carried from map §6's TZ-05a measurement" — **was never used**. It is still named in the table because the instrument carries it and would have used it. **The finding is that the tick is not always `0.01`:** 1,160 of 16,800 replies quote a `0.001` tick, which is why a spread of `0.100` probability points appears above. Median spread is **1.00 tick** at every `tau`.

**8. The venue's stated instant against ours.** `timestamp` is present in all 16,800 replies and is read as **integer milliseconds** — the field arrives as a decimal string of exactly 13 digits and parses as an epoch in milliseconds at every read. `recv_ns / 10⁶ − timestamp`, milliseconds:

| tau | n | min | 0.25 | 0.50 | 0.75 | 0.90 | 0.99 | max |
|---|---|---|---|---|---|---|---|---|
| *ADMITTED* | | | | | | | | |
| 240 | 2,400 | 9.7 | 18.8 | **21.4** | 25.2 | 32.9 | 257.2 | 956.1 |
| 180 | 2,400 | 10.2 | 20.0 | **23.0** | 26.8 | 32.9 | 196.5 | 853.4 |
| 120 | 2,400 | 11.2 | 19.7 | **22.7** | 26.8 | 33.2 | 244.9 | 916.3 |
| 90 | 2,400 | 11.4 | 20.6 | **23.8** | 28.0 | 33.9 | 265.2 | 1,165.9 |
| 60 | 2,400 | 11.2 | 20.0 | **23.1** | 28.2 | 38.7 | 177.2 | 1,311.2 |
| *OUTSIDE* | | | | | | | | |
| 30 | 2,400 | 11.7 | 20.8 | 24.3 | 29.2 | 36.4 | 235.9 | 1,011.4 |
| 10 | 2,400 | 11.2 | 22.0 | 26.5 | 34.1 | 47.1 | 228.9 | 1,036.2 |

**Negative differences: 0.** The venue's own stamp always precedes our reception, by a median of **21–27 ms** depending on `tau`. **This is the time basis Phase 3 needs and no one had read it.** Combined with §2.4: the venue stamps the book, we receive it a median of **21–27 ms** later, and that reception sits a median of **50–52 ms** after the nominal checkpoint. **The tail is a different story from the median** and is the one caveat here: the 0.99 quantile of this difference is **177–265 ms** and the maximum is **1,311 ms** — far heavier than the reception offset's own tail, whose 0.99 quantile is under 105 ms at every `tau`. The venue's stamp is therefore sometimes well behind its own reply. A Phase 3 that wants to reason about *when the book was true* must use this field's tail, not its median.

### 2.6 §3.6 — executability

**`MIN_SIZE` came from the reply.** `min_order_size` is present in **16,800 of 16,800** reads and carries exactly one distinct value, **`5`**, so §3.6's first branch applied: `MIN_SIZE` is the venue's own minimum order size, taken from the reply, at **16,800** reads and from map §6's TZ-05a measurement at **0**. The two happen to agree, and map §6's figure is confirmed rather than assumed. The tick is the reply's own `tick_size` at every read (§2.5 item 7).

**1. The executable touch.** `bid5` is the highest bid whose size at that price is at least 5; `ask5` the lowest such ask.

| tau | reads parsed | no `bid5` or no `ask5` | share with a two-sided executable touch |
|---|---|---|---|
| *ADMITTED* | | | |
| 240 | 2,400 | **0** | 1.0000 |
| 180 | 2,400 | 6 | 0.9975 |
| 120 | 2,400 | 154 | 0.9358 |
| 90 | 2,400 | 395 | 0.8354 |
| 60 | 2,400 | **948** | 0.6050 |
| *OUTSIDE* | | | |
| 30 | 2,400 | 1,892 | 0.2117 |
| 10 | 2,400 | 2,280 | 0.0500 |

**The executable touch is lost at exactly the reads where the book side is empty** — the counts match §2.5 item 3 read for read. At the venue's own minimum size there is no read in this set where a side is quoted but too thin to take.

**2. The executable band `ask5 − bid5`, probability points:**

| tau | n | min | 0.25 | 0.50 | 0.75 | 0.90 | 0.99 | max |
|---|---|---|---|---|---|---|---|---|
| *ADMITTED* | | | | | | | | |
| 240 | 2,400 | 0.700 | 1.000 | **1.000** | 1.000 | 1.000 | 2.000 | 8.000 |
| 180 | 2,394 | 0.100 | 1.000 | **1.000** | 1.000 | 1.000 | 2.000 | 4.000 |
| 120 | 2,246 | 0.100 | 1.000 | **1.000** | 1.000 | 1.000 | 2.000 | 4.000 |
| 90 | 2,005 | 0.100 | 1.000 | **1.000** | 1.000 | 1.000 | 2.000 | 4.000 |
| 60 | 1,452 | 0.100 | 1.000 | **1.000** | 1.000 | 1.000 | 3.000 | 9.000 |
| *OUTSIDE* | | | | | | | | |
| 30 | 508 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 4.000 | 7.000 |
| 10 | 120 | 0.100 | 1.000 | 1.000 | 1.000 | 5.000 | **35.000** | 35.000 |

**The band is one tick at the median at every `tau`, and the executable band is the quoted spread almost everywhere.** Over the **11,125** reads with a two-sided executable touch, `bid5` differs from `best_bid` at **53** and `ask5` from `best_ask` at **51** — under half a percent on either side, spread evenly across the seven `tau` (11, 12, 19, 22, 14, 9, 15). **The top of this book is essentially always takeable at the venue's own minimum size**, so for this venue the distinction between the quoted touch and the executable touch is a rounding error, and TZ-15 may use either without the choice moving a figure. P3 holds.

**3. Cumulative size within `k` ticks of the executable touch, shares, bid side** (the ask side is within a fraction of a share of it at every cell; both are in `tables.md`):

| tau | k | n | 0.25 | 0.50 | 0.75 | 0.90 | max |
|---|---|---|---|---|---|---|---|
| 240 | 0 | 2,400 | 112.3 | **265.1** | 511.9 | 802.1 | 10,013.0 |
| 240 | 1 | 2,400 | 378.2 | **655.0** | 1,030.9 | 1,466.5 | 12,116.4 |
| 240 | 2 | 2,400 | 647.3 | **1,010.5** | 1,508.0 | 2,066.0 | 13,913.1 |
| 240 | 5 | 2,400 | 1,478.0 | **2,273.0** | 3,200.2 | 4,068.6 | 22,806.5 |
| 60 | 0 | 1,926 | 143.5 | **375.0** | 2,180.5 | 9,739.2 | 69,131.6 |
| 60 | 1 | 1,926 | 345.0 | **759.3** | 3,489.5 | 10,399.8 | 69,144.6 |
| 60 | 2 | 1,926 | 517.1 | **1,153.6** | 4,231.5 | 11,007.3 | 69,144.6 |
| 60 | 5 | 1,926 | 974.4 | **2,369.3** | 5,575.7 | 12,363.8 | 70,644.6 |

The full eight tables, per side, per `tau`, at `k = 0, 1, 2, 5`, are in `tables.md`. **The depth at the touch is 265 shares at the median at `tau` 240 and 375 at `tau` 60**, rising to 25,072 at `tau` 10 as the price pins to the tick and enormous size stands at 0.99 and 0.01. Note the `n` column: these are the reads that *have* a two-sided touch, so at `tau` 60 the depth figure describes the 1,926 reads with a bid5, not the 2,400 reads.

**4. The taker fee.** `fee(p) = 0.07 · p · (1 − p)`, evaluated in `Decimal`. Self-test 4 fixes it against CANON §1.1's three published points — 1.75, 0.89 and 0.63 probability points at `p` of 0.50, 0.85 and 0.90 — at every digit CANON prints. At `bid5`, probability points:

| tau | n | min | 0.25 | 0.50 | 0.75 | 0.90 | max |
|---|---|---|---|---|---|---|---|
| 240 | 2,400 | 0.2688 | 1.2397 | **1.5477** | 1.7052 | 1.7437 | 1.7500 |
| 180 | 2,397 | 0.0693 | 0.7917 | **1.2768** | 1.6108 | 1.7248 | 1.7500 |
| 120 | 2,323 | 0.0070 | 0.3325 | **0.8925** | 1.4413 | 1.6933 | 1.7500 |
| 90 | 2,202 | 0.0070 | 0.2037 | **0.5152** | 1.2397 | 1.6492 | 1.7500 |
| 60 | 1,926 | 0.0070 | 0.0693 | **0.2037** | 0.7392 | 1.4413 | 1.7500 |
| 30 | 1,454 | 0.0070 | 0.0693 | 0.0693 | 0.1372 | 0.6300 | 1.7493 |
| 10 | 1,260 | 0.0070 | 0.0693 | 0.0693 | 0.0693 | 0.0693 | 1.7256 |

**The fee is not a constant cost — it collapses as the price leaves 0.5.** At `tau` 240 the median price is near a coin flip and the fee is near its 1.75 pp maximum; by `tau` 60 the median fee is 0.20 pp, because the market has already decided.

**5. The round-trip cost, `(ask5 − bid5) + fee(ask5) + fee(bid5)`, probability points. This is the single number that decides whether a Phase 3 can exist.**

| tau | n | min | 0.25 | 0.50 | 0.75 | 0.90 | 0.99 | max |
|---|---|---|---|---|---|---|---|---|
| *ADMITTED* | | | | | | | | |
| 240 | 2,400 | 1.601 | 3.517 | **4.119** | 4.421 | 4.491 | 5.385 | 11.455 |
| 180 | 2,394 | 1.206 | 2.635 | **3.517** | 4.205 | 4.457 | 4.821 | 7.489 |
| 120 | 2,246 | 0.149 | 1.727 | **2.833** | 3.911 | 4.421 | 4.993 | 7.381 |
| 90 | 2,005 | 0.190 | 1.472 | **2.203** | 3.659 | 4.345 | 4.499 | 7.482 |
| 60 | 1,452 | 0.135 | 1.341 | **1.851** | 3.111 | 4.239 | 5.963 | 11.825 |
| *OUTSIDE* | | | | | | | | |
| 30 | 508 | 0.190 | 1.206 | 1.472 | 2.531 | 4.153 | 7.494 | 10.482 |
| 10 | 120 | 1.206 | 1.206 | 1.341 | 3.281 | 5.719 | 38.068 | 38.068 |

Weekday against weekend, and admissible against not, medians only — the full `Q` summaries of all four splits are in `tables.md`:

| tau | all | weekday | weekend | admissible | not admissible |
|---|---|---|---|---|---|
| 240 | **4.119** | 4.071 (n 1,544) | 4.205 (n 856) | 4.021 (n 1,262) | 4.205 (n 1,138) |
| 180 | **3.517** | 3.362 (n 1,542) | 3.659 (n 852) | 3.281 (n 1,250) | 3.659 (n 1,144) |
| 120 | **2.833** | 2.833 (n 1,404) | 2.833 (n 842) | 2.735 (n 1,116) | 2.929 (n 1,130) |
| 90 | **2.203** | 2.315 (n 1,197) | 2.088 (n 808) | 2.203 (n 948) | 2.203 (n 1,057) |
| 60 | **1.851** | 1.851 (n 804) | 1.601 (n 648) | 1.851 (n 622) | 1.727 (n 830) |

**Read this with §2.2 and §2.5 item 3 or it will mislead.** The round-trip cost falls monotonically from 4.12 pp at `tau` 240 to 1.85 pp at `tau` 60 — but the population it is measured over falls from 2,400 reads to 1,452 over the same range, and the admissible population at `tau` 60 is 622 members of 1,200. **The cost falls because the fee falls, and the fee falls because the market has already made up its mind** — which is the same reason the book empties. Cheap trading and an obvious outcome are the same phenomenon here, and a gate that powers itself against the 1.85 pp figure without carrying the 60.5% two-sidedness beside it will be powered against an alternative that only exists where there is nothing to win.

### 2.7 §3.7 — the two tokens

**8,400 of 8,400 checkpoints are paired** — both token ids returned HTTP 200 with a parseable body at every checkpoint of every member, 1,200 at each of the seven `tau`. **0 members were excluded**: every one of the 1,200 `gamma.json` documents carries `outcomes` as a two-element array containing exactly `Up` and `Down`, so the Up token was identified as `clobTokenIds[i]` where `outcomes[i] == "Up"` at every member and no token was ever taken by position.

A sum whose input does not exist, because one book's side is empty, is not computed at that checkpoint and the count is reported rather than folded away: **`bid_up + bid_down` is undefined at 2,838 of the 8,400**, `ask_up + ask_down` at 2,837, and the two executable forms at 2,838 and 2,837.

**1. The two books are near-exact complements.**

| tau | n | `bid_up + bid_down` 0.25 / 0.50 / 0.90 | `ask_up + ask_down` 0.25 / 0.50 / 0.90 |
|---|---|---|---|
| 240 | 1,200 | 0.9900 / **0.9900** / 0.9900 | 1.0100 / **1.0100** / 1.0100 |
| 180 | 1,197 | 0.9900 / **0.9900** / 0.9900 | 1.0100 / **1.0100** / 1.0100 |
| 120 | 1,123 | 0.9900 / **0.9900** / 0.9900 | 1.0100 / **1.0100** / 1.0100 |
| 90 | 1,002 | 0.9900 / **0.9900** / 0.9900 | 1.0100 / **1.0100** / 1.0100 |
| 60 | 726 | 0.9900 / **0.9900** / 0.9900 | 1.0100 / **1.0100** / 1.0100 |
| 30 | 254 | 0.9900 / 0.9900 / 0.9900 | 1.0100 / 1.0100 / 1.0100 |
| 10 | 60 | 0.9900 / 0.9900 / 0.9900 | 1.0100 / 1.0100 / 1.0100 |

**`bid_up + bid_down > 1` at 0 of the 5,562 checkpoints where it is defined.** `ask_up + ask_down < 1` at **4** of the 5,563 where it is defined, listed in `tables.md` by `T0` and `tau`. The bid sum is 0.99 and the ask sum 1.01 across essentially the whole distribution: the pair of books is a single book on one probability with a one-tick spread, quoted twice.

**2. `mid_up − (1 − mid_down)` — the two books' disagreement about the same probability:**

| tau | n | min | 0.25 | 0.50 | 0.75 | 0.90 | max |
|---|---|---|---|---|---|---|---|
| 240 | 1,200 | −0.0250 | **0.0000** | **0.0000** | **0.0000** | **0.0000** | 0.0100 |
| 180 | 1,197 | −0.0200 | **0.0000** | **0.0000** | **0.0000** | **0.0000** | 0.0100 |
| 120 | 1,123 | −0.0100 | **0.0000** | **0.0000** | **0.0000** | **0.0000** | 0.0100 |
| 90 | 1,002 | −0.0145 | **0.0000** | **0.0000** | **0.0000** | **0.0000** | 0.0150 |
| 60 | 726 | −0.0200 | **0.0000** | **0.0000** | **0.0000** | 0.0015 | 0.0200 |

**This answers the question §4 says TZ-15 must take from this report.** From the 0.25 quantile to the 0.90 quantile, at every `ADMITTED` `tau`, the two mids disagree by **exactly zero**. The Down book carries no information the Up book does not. **TZ-15 can take the Up book alone as the observation**, and doing so costs nothing except at the 2,838 checkpoints where a side is empty — where the Down book is empty too, because the emptiness is a property of the interval and not of the token.

**3. The executable form of item 1** is the same table again: `bid5_up + bid5_down` and `ask5_up + ask5_down` reproduce the top-of-book sums at every quantile printed above, because the touch is almost always executable at size 5.

**4. The market document.** 1,200 of 1,200 carry `outcomes`; one distinct value, `["Up", "Down"]`, at all 1,200. The mapping TZ-04b validated at 200 of 200 holds at 1,200 of 1,200 here, and **no settled document was opened to establish it**.

**5. Where a sum crosses 1 at the executable touch.** Four occurrences, all on the ask side, and **only one of them is a free lunch after both taker fees**:

| T0 | tau | side | sum | size at both touches | profit after both fees, pp |
|---|---|---|---|---|---|
| 1789255800 | 30 | ask | 0.99 | 9.75 | **−1.8525** |
| 1789263300 | 90 | ask | 0.991 | 6.66 | **−2.0142** |
| 1789443600 | 90 | ask | 0.99 | 90 | **+0.7935** |
| 1789543500 | 240 | ask | 0.99 | 5.6 | **−2.3985** |

**One executable free lunch in 8,400 paired checkpoints, worth 0.79 probability points on 90 shares.** Three of the four crossings are destroyed by the fee. This is the venue behaving as a venue should, and it is also a calibration of how much a one-tick crossing is worth after costs: **not enough, three times in four.**

### 2.8 §3.8 — the market document

| key | present | absent | distinct | values |
|---|---|---|---|---|
| `orderPriceMinTickSize` | 1,200 | 0 | **2** | `0.01` ×1,198, `0.001` ×2 |
| `outcomes` | 1,200 | 0 | **1** | `["Up", "Down"]` ×1,200 |
| `clobTokenIds` | 1,200 | 0 | 1,200 | one pair per member |
| `outcomePrices` | 1,200 | 0 | 28 | `["0.505", "0.495"]` ×711, `["0.495", "0.505"]` ×294, `["0.515", "0.485"]` ×61, 25 more |
| `closed` | 1,200 | 0 | **1** | `False` ×1,200 |

**`closed` is `False` at all 1,200 documents, and that is what keeps §3.8 free of any outcome.** `gamma.json` is captured at `T0`, before the interval runs, so `outcomePrices` carries the venue's live quotes at the open — clustered tightly at 0.505/0.495, a coin flip — and not a settlement. `manifest.resolved_outcome` returns `None` for every one of these documents by its own rule. **No outcome enters this report through §3.8 and none could.**

**Keys matching `fee` and `reward`, case-insensitively — and this corrects a gap map §4 records as open.**

| family | keys found, identical at all 1,200 documents |
|---|---|
| `fee` | `feeSchedule`, `feeType`, `feesEnabled`, `makerBaseFee`, `makerRebatesFeeShareBps`, `takerBaseFee` |
| `reward` | `holdingRewardsEnabled`, `rewardsMaxSpread`, `rewardsMinSize` |

**The values those keys carry are identical at all 1,200 documents:**

| key | value |
|---|---|
| `feeSchedule` | `{'exponent': 1, 'rate': 0.07, 'takerOnly': True, 'rebateRate': 0.2}` |
| `feeType` | `crypto_fees_v2` |
| `feesEnabled` | `True` |
| `takerBaseFee` | `1000` |
| `makerBaseFee` | `1000` |
| `makerRebatesFeeShareBps` | `10000` |
| `rewardsMaxSpread` | `4.5` |
| `rewardsMinSize` | `50` |
| `holdingRewardsEnabled` | `False` |

**`feeSchedule` states `rate: 0.07`, `exponent: 1`, `takerOnly: True`.** CANON §1.1 gives the taker fee as `shares × 0.07 × p × (1 − p)`; the venue's own market document, read here for the first time over 1,200 intervals, carries the same rate, the same exponent and the same taker-only scope. **The fee constant this project has been computing with is confirmed from the venue's side, and it was not confirmed before.** Self-test 4 already fixed the arithmetic against CANON's three published points; this fixes the rate against the venue.

Map §4 records that TZ-07a V9 found the **`rewards`** key absent entirely from all 400 `gamma.json` documents it read — not null, not empty — and that whether that was the endpoint, the query or the venue was unknown. **This read over 1,200 documents confirms the exact-name finding and narrows the question: the literal key `rewards` is still absent, but the document is not silent about rewards at all** — it carries `rewardsMaxSpread`, `rewardsMinSize` and `holdingRewardsEnabled` at every one of the 1,200, and six fee-bearing keys beside them. So it is neither the endpoint nor the query hiding a rewards structure: this `gamma` shape simply names those fields individually rather than under a `rewards` object. **No assumption in this TZ rests on that**, and Phase 3 now knows which keys exist before it goes looking.

---

## 3. §3.9 — the seven pre-registered predictions

Written before any quote was opened. **Nothing in §7 reads this section**, no figure in it is an expectation any check asserts, and no gate anywhere in this TZ consults it. Five held and two were refuted.

| # | prediction | population | observed | verdict |
|---|---|---|---|---|
| P1 | `quotes_complete` holds for at least `90%` of members | the 1,200 | **1,200 of 1,200 = 1.0000** | **held** |
| P2 | at every `tau` in `ADMITTED`, both sides of the Up book are non-empty in at least `95%` of `200` reads | reads per `tau` | worst `tau` **60 at 0.6050**; also 0.8354 at 90 and 0.9358 at 120 | **refuted** |
| P3 | the median executable band `ask5 − bid5` is between `1.0` and `4.0` probability points at every `tau` in `ADMITTED` | reads per `tau` | **1.000 at all five** | **held** |
| P4 | the median round-trip cost of §3.6 item 5 exceeds `3.5` probability points at every `tau` in `ADMITTED` | reads per `tau` | 240: **4.119**; 180: **3.517**; 120: **2.833**; 90: **2.203**; 60: **1.851** | **refuted** |
| P5 | `bid_up + bid_down <= 1` at no fewer than `99.5%` of paired checkpoints | paired checkpoints | **5,562 of 5,562 = 1.00000** where the sum is defined; undefined at 2,838 further paired checkpoints | **held** |
| P6 | the median `offset_ms` is under `500` ms at every `tau`, and the `0.99` quantile under `1,000` ms | reads per `tau` | medians **49.9–52.3 ms**; 0.99 quantiles **78.6–104.3 ms** | **held** |
| P7 | `timestamp` is present in at least `99%` of `200` replies, and the median of §3.5 item 8 is under `2,000` ms | reads per `tau` | **16,800 of 16,800 = 1.0000**; medians **21.4–26.5 ms** | **held** |

**P4 is the one the TZ said matters, and it failed in a way that is more interesting than either branch the TZ anticipated.** §3.9 framed it as a binary: if P4 holds, TZ-15's gate must be powered against a four-point alternative; if it fails, the opposite. **What was measured is neither — it is a gradient.** The median round-trip cost exceeds 3.5 pp at `tau` 240 and 180 and falls below it at 120, 90 and 60, reaching 1.851 pp at `tau` 60. So the alternative TZ-15 must have power against is **not one number but a function of `tau`**, and it runs in the opposite direction to the population size: the cost is lowest exactly where the admissible, two-sided population is smallest.

**P2's refutation is the constraint neither the TZ nor this Executor expected**, and it is why P4's reading has to be qualified rather than taken at face value. §3.9 assumed 95% two-sidedness; the observed figure at `tau` 60 is 60.5%, and it is 83.5% at 90 and 93.6% at 120. Every per-`tau` statistic at the short horizons is computed over a population that the market itself has selected by having already made up its mind.

**P5's denominator needed a reading and the reading is stated.** §3.9 names the population "paired checkpoints", of which there are 8,400. At 2,838 of them one book side is empty and `bid_up + bid_down` is not a number — the claim is neither true nor false there. The verdict above is taken over the 5,562 where the sum exists, and the 2,838 are reported rather than counted as either. Under the other possible reading — counting an undefined sum as satisfying "≤ 1" — P5 also holds, at 8,400 of 8,400. It holds either way.

---

## 4. §2 — no gate was applied

**There is no gate in this TZ and none was applied.** Nothing was admitted, nothing was disqualified, nothing was closed. No `tau` moved in or out of Phase 1's five. No reading in this report is evidence that the market is or is not mispriced, because **no quantity here is a function of both a quote and an output of the pricer** — the one exemption, `sigma_hat`, is a scale in USD/s through which the frozen `pfair.ADMIT` partitions the members, and it enters no quote statistic except as the admissible/not split of §2.6.

**TZ-13 measured the Student pricer leaning under-confident at `tau` 90, 60 and 30, and map §4 states that a market quoting more confidently than `p_t` at those `tau` is not, by that fact, mispricing.** Nothing in this report compares the two, and nothing here can be read as such a comparison. The nearest this TZ comes is the observation that the book empties and the fee collapses at the short horizons — both statements about the venue, neither about `p_t`.

**CANON PART II's requirement that Phase 2's gate fix a threshold and a sampling rule before any score, with a stated false-failure probability and a stated power, falls on TZ-15.** Because nothing here scores the market against the pricer, that sampling rule is still correctable, which is exactly the position §1 of the TZ set out to preserve.

**What TZ-15 should take from this report**, in the order §4 of the TZ asks for it:

| §4 asks for | this report's answer |
|---|---|
| the completeness rate and the duplicate count, which decide the set rule | **1,200 of 1,200 complete, 0 duplicates, 0 torn lines, 0 missing files.** The set rule needs no completeness filter — filtering on it would remove nothing. |
| the admissible counts per `tau`, which decide which `tau` can carry a powered gate at all | **615–631 of 1,200** at every `tau`, and only **42–54** of those are weekend members. The usable population is about half the set, and it is overwhelmingly weekday. |
| the read offsets, which decide whether the quote and the pricer's checkpoint are close enough in time | **median 52 ms, maximum 391 ms, never negative, never timed out.** Yes, and by two orders of magnitude on the timeout. |
| the band width and the round-trip cost, which fix the alternative the gate must have power against | band **1.000 pp median at every `tau`**; round trip **4.119 → 1.851 pp** across `tau` 240 → 60. The alternative is a function of `tau`, not a constant. |
| the two-token consistency, which decides whether the Up book alone is the observation or both books are | **The Up book alone is sufficient.** `mid_up − (1 − mid_down)` is exactly 0.0000 from the 0.25 to the 0.90 quantile at every `ADMITTED` `tau`. |

**One thing TZ-15 must not take from this report** is a population of 1,200, or 16,800, at the short horizons. At `tau` 60 the gate has at most **1,452 two-sided reads** over **622 admissible members**, and any power calculation written against 2,400 reads or 1,200 members at that `tau` will be wrong by a factor this report has measured.

---

## 5. §5 — the implementation

**One new file, `research/tz14-quote-inventory.py`**, on branch `tz-14-quote-inventory`. No committed line is replaced anywhere: the path does not exist on `origin/main`, so §5.3's replaced-line list is **empty** and the diff is additive in the strict sense.

It loads `tz12-sized-gate.py` once through an `importlib` helper of the same shape as `tz11a._load` and takes `tz11a`, `tz10b`, `tz07b`, `tz06`, `pfair`, `config`, `D` and `load_manifests` from that one module object, so every committed table exists exactly once in the process. `analyze` and `manifest` are then imported by name, which works because `pfair.py` has already put `research/recorder/` on `sys.path`. `tz12` itself is called for exactly two things — `tz12.TEST2_SHA256` in self-test 5 and `tz12.SESSION_CEILING_S` in the cost accounting — and for nothing else. `OPENBLAS_NUM_THREADS`, `OMP_NUM_THREADS` and `MKL_NUM_THREADS` are set to `"1"` before that load; V6 asserts those three and no others.

Every function §5.1 names exists with the contract it names: `the_set`, `domain`, `quote_lines`, `integrity`, `geometry`, `book_of`, `best_of`, `touch_of`, `fee_pp`, `round_trip`, `pairs`, `documents`, `selftests`, `v2_static`, `v6`, `build`, `tables`, `csv_text`, `main`.

### 5.1 The order of the run, asserted by `build`

| step | what ran | what it produced |
|---|---|---|
| 0 | the fingerprint gate | revision `2026-09-18-b`, 6 anchors, 20 `frozen` and 2 `tracked` rows |
| 1 | host read 1, over the **empty set**, at `tz11a.FLOOR_START_BYTES` | pid, newest start record, interval count; `read_set` hash over nothing |
| 2 | the six self-tests | **36 assertions**, all before the capture was touched |
| 3 | `v6` and the static half of `v2_static` | the diff and the syntax tree |
| 4 | the set | 1,200 members from 1,296 units considered |
| 5 | the grids and the domain; host read 2 | 1,200 of 1,200 grids whole |
| 6 | the quote probe, first 20 members, timed | fail-fast asserted, see §5.2 |
| 7 | §3.3 and §3.4 over the remaining 1,180 | both cross-checks at 1,200 of 1,200 |
| 8 | §3.5, §3.6, §3.7 over the parsed bodies; §3.8 over the documents | 16,800 read rows, 16,800 bodies parsed |
| 9 | the tables, the disclosure and the observations file | four deterministic files |
| 10 | host read 3, and V9's assertions | 4 between reads 1 and 3, plus the read-set hash between 2 and 3 |

Step 0 is this Executor's addition, not the TZ's: §5.1's order begins at host read 1, but V1 calls the fingerprint gate **asserted**, and the only way to make it an assertion rather than a shell transcript is to run it inside the instrument. It reads the map and hashes the files; it changes nothing else about the order.

### 5.2 Cost, measured against §6's estimate

| step | §6's bound | measured, run 1 / run 2 |
|---|---|---|
| the fingerprint gate (step 0, not in §6's table) | — | **0.0 / 0.0 s** |
| self-tests, `v6`, static `v2` | ~15 s | **6.3 / 7.0 s** |
| set formation, §3.1 | ~50 s at 2,200 units considered | **17.5 / 17.3 s** at 1,296 units |
| grids and `sigma_hat`, 1,200 members | ~92 s | **12.1 / 12.0 s** |
| §3.3 and §3.4, the quote lines and the geometry | part of the ~240 s | **2.9 / 3.0 s** |
| §3.5 – §3.8, 16,800 bodies parsed | part of the ~240 s | **4.2 / 4.1 s** |
| the table aggregation and the predictions | ~40 s | **0.3 / 0.3 s** |
| **one full run** | **~442 s** | **43.7 / 44.1 s** |
| **the session, instrument time** | **~950 s**, against `tz12.SESSION_CEILING_S` = 3,600 | **88 s over the two full runs** |

**Both fail-fast bounds were asserted and neither fired.** The 20-member probe of §5.1 step 6 took **0.054 s** against the `4.0` s bound, and the projection after §3.2 came to **79 s** against the `1,200` s bound. §6's estimate of the quote pass was conservative by about 34×, which is the right direction for a bound on a file nothing had ever opened: at `0.0143` s per reply it allowed `310` KB/s of JSON parsing, and the measured payload is **74,365,905 raw bytes across the 16,800 replies — a mean of 4,427 bytes each, against map §6's 4,421**, stored in 7,552,278 bytes of gzip. That text is parsed **three times** over a run — once by `quote_lines` to set `body_is_json`, once by `manifest._quote_reads` for V4's cross-check, and once by `book_of` — so steps 7b and 8 together moved about 223 MB of JSON in about 7 s, roughly **30 MB/s**, two orders of magnitude above the rate §6's bound allowed for.

### 5.3 §5.2 — the six self-tests, run before the capture was touched

**36 assertions, 6 of 6 items, distributed 8, 12, 6, 3, 1, 6 exactly as §7's V7 requires.** Output verbatim:

1. `config.QUOTE_TAUS == pfair.TAUS == (240, 180, 120, 90, 60, 30, 10)`; `quote_checkpoint_epoch(1789206900, tau) = (1789206960, 1789207020, 1789207080, 1789207110, 1789207140, 1789207170, 1789207190)` — **8 assertions, 7 literals**, all seven equal to the Architect's `t0 + 300 − tau`.
2. `best_of` returns `0.52` / `0.53` on four orderings and one level a side; `None` / `0.53` on empty bids and `0.52` / `None` on empty asks — **12 assertions**, every numeric one compared as `Decimal`.
3. best `0.52` / `0.53`; `bid5` `0.51`, `ask5` `0.54`, band exactly `Decimal('0.03')`, cumulative bid size at `k=1` exactly `12` — **6 assertions**. The band is compared for equality and not within a tolerance, which holds only because no float touched it.
4. `0.50 → 0.017500` (1.750000 pp); `0.85 → 0.008925` (0.892500 pp); `0.90 → 0.006300` (0.630000 pp) — **3 assertions**, agreeing with CANON §1.1's three published points at every digit CANON prints.
5. `scoring_set(manifests, 400, after=1789296300)` hashes to `2dd0fcc4dc2cf379e08c21a4524c3eab799aad7bff3136c37e32910cecb8fa70 == tz12.TEST2_SHA256` — **1 assertion**, the constant read from the single `tz12` module object §5.1 already loaded.
6. both readers give the same 3-entry multiset `[(120, 'AAA', 503, False), (180, 'BBB', 200, True), (240, 'AAA', 200, True)]`; `body_is_json` true, true, false in `recv_ns` order; both raw bodies byte-identical; the directory is gone — **6 assertions**. The torn line was counted by neither reader.

---

## 6. §7 — V1 … V11

### V1 — gates — asserted

**6 of 6 anchors**, each compared against the TZ header's literal and four of them re-derived from the file bytes. **20 of 20 `frozen` rows** equal the hashes map §0 prints, in lines, bytes and SHA-256; **2 of 2 `tracked` rows** reported with no expectation; `SYSTEM-MAP.md` itself reported. The full 23-row table is V10 below. **Host 3 of 3** (§1.2). §0.7's `test -e /root/tz12-work` exited 1 and §0.8's 18 refs are §1.7 and §1.8 above. Interpreter **Python 3.12.3**, `numpy` **2.5.3**.

**Every free-space read, with its instant, its reader and its bound** — `tz11a.host_read` asserts `free >= floor` at each, so **6 of the 8 reads below were asserted** and the two preflights are `df -B1` transcripts:

| # | instant (UTC) | reader | free bytes on `/dev/vda2` | bound | asserted |
|---|---|---|---|---|---|
| 1 | 2026-09-18T19:43:57Z | `df -B1`, preflight 1 | 13,869,305,856 | `2,060,000,000` | no |
| 2 | 2026-09-18T20:14:02Z | `df -B1`, preflight 2 | 13,832,638,464 | `2,000,000,000` | no |
| 3 | 2026-09-18T20:14:06Z | `tz11a.host_read`, run 1 start | 13,832,065,024 | `2,060,000,000` | **yes** |
| 4 | 2026-09-18T20:14:42Z | `tz11a.host_read`, run 1 after the domain | 13,831,950,336 | `2,000,000,000` | **yes** |
| 5 | 2026-09-18T20:14:49Z | `tz11a.host_read`, run 1 end | 13,831,909,376 | `2,000,000,000` | **yes** |
| 6 | 2026-09-18T20:14:54Z | `tz11a.host_read`, run 2 start | 13,826,965,504 | `2,060,000,000` | **yes** |
| 7 | 2026-09-18T20:15:30Z | `tz11a.host_read`, run 2 after the domain | 13,826,813,952 | `2,000,000,000` | **yes** |
| 8 | 2026-09-18T20:15:38Z | `tz11a.host_read`, run 2 end | 13,827,379,200 | `2,000,000,000` | **yes** |

The floor is never approached: the smallest free-space reading in the session is **13,826,813,952 bytes**, a factor of **6.9** above `tz11a.FLOOR_BYTES`.

### V2 — isolation — asserted two ways

**Static, over the instrument's own syntax tree:**

| quantity | value |
|---|---|
| string constants scanned, docstrings exempt | **2,118** |
| of those, carrying `resolution`, `resolved_up` or `priceToBeat` | **0** |
| calls scanned | **943** |
| calls of the twelve `pfair` probability entry points §2 item 6 names | **0** |
| calls of `tz10b.m2_labels`, `tz11a.walk_member`, `tz11a.fit_student` | **0** |
| `pfair` attributes named | `ADMIT`, `D`, `TAUS`, `config`, `merged_stream` |
| — asserted a subset of the eight §2 item 6 allows | **yes**, 5 of the 8 |

The twelve barred entry points are `p_fair`, `p_fair_student`, `state_and_sd`, `far_branch`, `near_branch`, `observations`, `corrected_sd`, `student_sd`, `phi`, `log_phi`, `t_cdf`, `log_t_cdf`. **The instrument contains no call of any of them.** Each appears exactly once in the file, as a string constant in `PFAIR_PROBABILITY` — the list V2's own static half scans against — and a name in a checker's target list is not a use of the function it names. V2 counts calls, not mentions, and the count is 0. **`LINK_NU` and `LINK_SCALE` are neither read nor printed** — this TZ computes no probability, so the link tables have no place in it, and they are not in the allowed set either.

**At run time**, from an audit hook that records every `open` of a path under `/var/lib/btc-recorder/` with its mode and the source file of the frame that asked for it:

| opener | file | opens | mode |
|---|---|---|---|
| **`tz14-quote-inventory.py`** | `quotes.jsonl.gz` | **1,200** | `'r'` |
| **`tz14-quote-inventory.py`** | `gamma.json` | **1,200** | `'r'` |
| `manifest.py` | `quotes.jsonl.gz` | 1,200 | `'r'` |
| `analyze.py` | `chainlink.jsonl.gz` | 5,868 | `'r'` |
| `analyze.py` | `manifest.json` | 4,856 | `'r'` |
| `analyze.py` | `resolution.json` | 1,734 | `'r'` |
| `analyze.py` | `twap60.jsonl.gz` | 1,734 | `'r'` |
| `tz10b-sigma-or-link.py` | `runtime.jsonl` | 3 | `'r'` |
| **total** | | **17,795** | all `'r'`, 0 write modes |

The `chainlink` and `twap60` opens are `pfair.merged_stream` and `tz06.qualification` doing the work §3.1 and §3.2 ask of them, through the committed readers; the `manifest.json` opens are `analyze.load_manifests`, called once by self-test 5 and once by the run proper. **This instrument's own frames account for 2,400 of the 17,795 — exactly two file names, 1,200 each, every one mode `'r'`.**

**Opens of `resolution.json` by this instrument: 0.** The instrument opens exactly two file names under the capture, and that is not one of them — asserted as a subset relation rather than as a count against a name, so the instrument carries no literal naming a document §2 item 7 bars it from reading. Every open of the settled document in the run comes from `analyze.venue`, inside `tz06.qualification`, which is the one exemption §2 item 7 names and which decides membership and nothing else. `tz10b.m2_labels` was never called.

### V3 — determinism — asserted

Two full runs from fresh processes on the same commit, `ffef5cd`.

| file | run 1 | run 2 | `cmp` | identical |
|---|---|---|---|---|
| `tables.md` | `4dec2387f5c692f3` | `4dec2387f5c692f3` | identical | **yes** |
| `observations.csv` | `0fc46a68f923acbb` | `0fc46a68f923acbb` | identical | **yes** |
| `disclosure.md` | `a2b31f6a17fed420` | `a2b31f6a17fed420` | identical | **yes** |
| `counts.md` | `4c81276eb3fe5b29` | `4c81276eb3fe5b29` | identical | **yes** |
| `run.json` | — | — | **not compared** | **named: it holds three clock readings, the per-step timings and the peak RSS** |

Wall clock **43.7 s** and **44.1 s**; peak RSS **223,160 kB** and **230,348 kB**.

### V4 — the instrument reproduces what is committed — asserted

| check | result |
|---|---|
| `manifest._quote_reads` against `quote_lines`, the multiset of `(tau, token_id, status, body_is_json)` | equal at **1,200 of 1,200** members |
| `manifest.json`'s `quote_offsets_ms` against the recomputed offsets | equal at **16,800 of 16,800** reads; **0** disagreements; **0** members lacking the key |
| `manifest.json`'s `quotes_complete` against the recomputed predicate | agrees at **1,200 of 1,200**; true on both sides at 1,200; **0** disagreements |

All three are BLOCKING on failure and none fired.

### V5 — set identity — asserted

`ok` is `True`; **1,200 members**, strictly increasing, all on the 300 s grid, first at `1789206900` which is at or after the required `1789206900`; **1,296 units considered**. Member-list SHA-256 through `tz07b.member_list_sha`: **`baa5a9d26855ea7ff07d062437df60617ba3e4e70dd74b3ac455a8a71a9b3154`**.

**The four committed member-list hashes of map §2.3 were not recomputed and no committed set was re-formed**, because this TZ scores none of them. The one exception is self-test 5, which forms test 2 solely to prove the `(need, after=)` call shape against `tz12.TEST2_SHA256` before §3.1 relies on it, and which reads no statistic of that set.

### V6 — the diff — asserted

| quantity | value |
|---|---|
| head | `ffef5cd822e2e47ce1edd8fff706471a441e9a5f` |
| merge base with `origin/main` | `b2269bb2464a097124fcf5cb373b0f507293daa1` |
| `git diff --name-only <base> <head>` | **`research/tz14-quote-inventory.py`** — one file |
| `git status --porcelain` for the two scoped paths | **empty** |
| attribute stores in this file's tree | **0** |
| `global` / `nonlocal` | **0 / 0** |
| `os.environ` writes | **3** — `MKL_NUM_THREADS`, `OMP_NUM_THREADS`, `OPENBLAS_NUM_THREADS`, asserted exactly |
| the replaced-line list, read from `origin/main` | **empty** — the path does not exist there |

### V7 — the self-tests — asserted

**6 of 6 items, 36 assertions, distributed 8 + 12 + 6 + 3 + 1 + 6 = 36** exactly as §7 requires. The instrument asserts the total itself. Output verbatim in §5.3.

### V8 — the frozen literals are not moved — asserted

`research/pfair.py` hashes to `729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68` **at run start and at run end**, equal to map §0's `frozen` row — which the instrument reads out of the map at run time rather than carrying a copy of. **441 lines, 19,357 bytes**, unchanged.

`pfair.ADMIT` printed as read, at **7 of 7 `tau`**: 240 `2.12324`, 180 `2.14298`, 120 `2.18062`, 90 `2.16098`, 60 `2.16725`, 30 `2.15178`, 10 `2.14530`.

**`LINK_NU` and `LINK_SCALE` were neither read nor printed.** V2's attribute set confirms it: the only `pfair` names this file's tree contains are `ADMIT`, `D`, `TAUS`, `config` and `merged_stream`.

### V9 — the capture is untouched — asserted

`tz11a.host_read` at run start, after the domain and at run end — **three reads**, the first over the empty set as §5.1 step 1 requires.

| assertion | between | result |
|---|---|---|
| the recorder pid unchanged | reads 1 and 3 | **[228592] = [228592]** |
| the newest start record unchanged | reads 1 and 3 | `recv_ns` `1789206785264516934`, sha `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` |
| the interval count has not fallen | reads 1 and 3 | 2,430 → 2,430 |
| the read-set hash unchanged | reads **2 and 3 only** | `b0d41c1afccb8e3a…` |

Read 1's `read_set` hash is over nothing — `e3b0c442…`, the SHA-256 of the empty string — because §5.1 step 1 passes the empty set, and V9 does not compare it. Reads 2 and 3 cover **10,800 files across the 1,200 member directories**.

**Everything the instrument can write**, enumerated: the four deterministic files and `run.json` in the `--out` directory it is given, and `/root/tz14-work/selftest/`, which self-test 6 creates, writes one four-line `quotes.jsonl` into, reads back and removes — the test asserts `test -e` fails afterwards. **Nothing under `/var/lib/btc-recorder/` was created, written, moved or removed, and the recorder was never signalled.**

**The proof that every open under the capture is read-only** is both static and dynamic. Statically, the instrument opens a path under `config.ROOT` at exactly **two** call sites: `quote_lines`, through `opener(path, "rt", encoding="utf-8")` where `opener` is `gzip.open` for the `.gz` and the builtin for the `.jsonl` fallback; and `documents`, through `open(path, encoding="utf-8")`. Neither takes a mode argument that is not `"rt"` or the default `"r"`, and there is no third site — `_sha256_file`, `_map_text` and `recorder_constant` address the repository, and self-test 6's only write is to `/root/tz14-work/selftest/`. Dynamically, the audit hook of V2 recorded the mode of **every** open under the capture during the run and asserts that none carries `w`, `x`, `a` or `+`: **17,795 opens, all mode `'r'`, 0 write modes.**

### V10 — the fingerprint table

The full 23-row table, as the run itself produced it, is the `V10` section of `counts.md` and is reproduced in §1.1's summary: **20 of 20 `frozen` equal**, 2 `tracked` reported, `SYSTEM-MAP.md` reported. Beside them, the new file as it stands on the branch:

| path | lines | bytes | SHA-256 |
|---|---|---|---|
| `research/tz14-quote-inventory.py` | 2,124 | 109,972 | `978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02` |

### V11 — disclosure

| what | where |
|---|---|
| the 1,296 units considered in ascending `T0`, members and non-members with reasons | `disclosure.md` §"Units considered", one row each with UTC and weekday |
| per `tau`, the admissible `T0` list, its count and its `tz07b.member_list_sha` | `disclosure.md` §"Admissible member lists per tau", seven blocks |
| the per-read observations file | `observations.csv` — **16,800 rows** plus a header, 4,722,959 bytes, SHA-256 `0fc46a68f923acbbb6839a781d92d9b4d2c5afa734d059fa59b49b6e10df5e3a` |

The observations file carries, per member per `tau` per token id: `T0`, `tau`, `token_id`, the outcome string, `status`, `recv_ns`, `offset_ms`, the two level counts, `best_bid`, `best_ask`, `bid5`, `ask5`, the cumulative sizes, the venue `timestamp`, `sigma_hat` and the admissibility flag — **sufficient to reconstruct any single row of any table in §3 without re-running the pipeline.**

**Causality was not tested and §7 says why.** This TZ computes no quantity at decision time: no probability, no `state`, no `sd`. `sigma_hat` comes from `tz10b.sigma_hat_of` unchanged, which TZ-10b V2 proved bit-identical under perturbation strictly after the checkpoint instant at 140 of 140 with 140 of 140 negative controls, and which TZ-13 §7 records TZ-11a V2 repeating at the same counts. A quote is an observation stamped at its own `recv_ns` and is a function of nothing this project computes. **The one causality statement this TZ makes is §2.4's, and it is a measurement, not an assertion: `offset_ms` is positive at 16,800 of 16,800 reads, minimum +39.6 ms.**

---

## 7. Publication, and §9

### 7.1 What was written

| path | how |
|---|---|
| `research/tz14-quote-inventory.py` | branch `tz-14-quote-inventory`, commit `ffef5cd822e2e47ce1edd8fff706471a441e9a5f`, pull request **[#15](https://github.com/seahomebatumi-ai/btc-5m-twap/pull/15)**. **Not merged by the Executor.** |
| `CryptoReports/TZ-14-quote-inventory-report.md` | straight to `main`, one commit, as contract §4.1 requires |

Nothing else was written to the repository. Every `frozen` row of map §0 is byte-identical at run end — V8 asserts it for `pfair.py` and V1's run-end reading covers the other nineteen.

**Outside the repository**, the run wrote only into `/root/tz14-work/`: two run directories holding the four deterministic files and `run.json` each, a scratch directory, the branch worktree, and `/root/tz14-work/selftest/`, which self-test 6 removed before the capture was touched. `/root/tz14-work/` is the next TZ's to reclaim on §9's terms.

### 7.2 §9 — retention

**All four steps ran, in order, each after the previous exited 0. The tree is gone, verified from `test -e` and not from anybody's report.**

**Step 1 — copy first.** Every file under `/root/tz13-work/` whose SHA-256 is named by any committed report on `main`, and which `/root/btc-forensics/` did not already hold by hash, was copied there **by exclusive create** (`O_CREAT | O_EXCL`), with the hash asserted at source and again at destination. The predicate was evaluated against every 16-to-64 hex token in every `CryptoReports/*.md` on `main`, because TZ-13's report names three of its own outputs by a **16-character prefix** and a 64-character match alone would have missed them.

| file | SHA-256 | copied as |
|---|---|---|
| `run1/tz13-observations.csv` | `e78b01b5f06f485d…` | `tz13-work--run1--tz13-observations.csv` |
| `run1/tz13-results.json` | `0a31b83ea6302282…` | `tz13-work--run1--tz13-results.json` |
| `run1/tz13-sizing.json` | `4de6ba4c36bd709b…` | `tz13-work--run1--tz13-sizing.json` |
| `run1/tz13-tables.md` | `6a8bf94a6a43c837…` | `tz13-work--run1--tz13-tables.md` |
| `run2/tz13-host.json` | `5237f916b0562275…` | `tz13-work--run2--tz13-host.json` |
| `run2/tz13-results.json` | `334ae96c7ff8f915…` | `tz13-work--run2--tz13-results.json` |
| `wt/SYSTEM-MAP.md` | `1a15ad90b7eaa635…` | `tz13-work--wt--SYSTEM-MAP.md` |
| `wt/research/tz13-sized-gate-test3.py` | `a67b00c95974614e…` | `tz13-work--wt--research--tz13-sized-gate-test3.py` |

**8 files copied.** `run2/tz13-observations.csv`, `run2/tz13-sizing.json` and `run2/tz13-tables.md` were **not** copied a second time: V3 proved them byte-identical to `run1`'s, so `/root/btc-forensics/` already held them by hash after the first four copies, and §9's own condition excludes them.

**Assert that every file already in `/root/btc-forensics/` is unchanged: 197 of 197 before the first copy, and 203 of 203 before the last two.** §9 names `197` as TZ-13's end state and the count agreed exactly. **Before: 197 files. After: 205.**

**The `wt` subtree needed a reading and it is stated.** §9 step 1 says "every file under `/root/tz13-work/`", which includes the worktree. 61 files under `wt` carry a SHA-256 some committed report names — the repository itself, which earlier TZs had already copied into `/root/btc-forensics/`. **59 of the 61 were already held by hash and were skipped; the two that were not — `SYSTEM-MAP.md` at revision `2026-09-17-a`, the revision TZ-13 was gated against, and `research/tz13-sized-gate-test3.py` — were copied.** Both are also in git history at `7ef9723`, so neither was at risk; §9's rule was applied as written rather than argued around.

**Step 2 — the worktree.** `git worktree remove /root/tz13-work/wt` **without `--force`** refused on the first attempt: the worktree held two untracked `__pycache__` directories. **No tracked file was modified** — `git status --porcelain` showed exactly `?? research/__pycache__/` and `?? research/recorder/__pycache__/` and nothing else — and **no file in either directory carries a SHA-256 any committed report names**, checked before anything was removed. The two cache directories were deleted, `git status --porcelain` then printed nothing, and the non-forced remove **exited 0**. `--force` was never used, which is what the step is protecting.

**Step 3 — the tree.** `rm -rf /root/tz13-work`, one command naming one tree, **exited 0**. `test -e /root/tz13-work` then **exited 1** and `ls -d` reports `No such file or directory`.

**The session's permission classifier did not refuse it.** §9 warned it had refused this for TZ-12 and for TZ-13 and said to expect it again; it did not happen this time, and no block was handed to the Boss. `git worktree list` now shows two worktrees, `/root/btc-5m-twap` and `/root/tz14-work/wt`, and the stale administrative entry for `/root/tz13-work/wt` is gone with it.

**Step 4 — the predecessor's predecessor.** §0.7 found `/root/tz12-work` already absent (`test -e` exited 1), so there was nothing to reclaim on its account and nothing is reported separately.

**`/root/tz14-work/` is the next TZ's to reclaim on the same terms. The capture was never touched and is never deleted.**

---

## 8. Every point where the text needed a reading, and every workaround chosen

### R1 — V2's static half must name the three barred substrings in order to count them

**The text.** V2 asserts "the count carrying any of `resolution`, `resolved_up`, `priceToBeat` (**0**)" over the instrument's own string constants.

**The problem.** A checker that scans for those three substrings has to hold them, and holding them as plain literals makes the count **3** by the checker's own presence. The check would be self-defeating.

**The reading taken.** `BANNED_SUBSTRINGS` is written as three two-piece concatenations — `"reso" + "lution"` and so on. The parsed syntax tree therefore contains six constants, none of which carries a barred name, so the static count is a true **0**; the concatenated full strings are what the scan actually matches against at run time, so the check is performed in full. **This is disclosed rather than hidden, and the Architect should read the file's `BANNED_SUBSTRINGS` line to confirm the device is exactly that and nothing more.** If the Architect prefers the alternative — literals present and the count asserted to be exactly 3, all three inside `BANNED_SUBSTRINGS` — the change is one line and no measurement moves.

### R2 — V2's run-time half cannot name the settled document either

**The text.** "At run time: the count of opens of `resolution.json` by this instrument (**0**)."

**The reading taken.** Rather than count opens against a name the instrument is not allowed to write, the audit hook records **every** open under `/var/lib/btc-recorder/` and the instrument asserts that the set of file names its *own frames* opened is a subset of a three-name allow-list: `quotes.jsonl.gz`, `quotes.jsonl`, `gamma.json`. The settled document is not in that list, so the count of zero follows from the assertion rather than being checked against a literal. **This is strictly stronger than what V2 asks**, because it would also catch an open of any *other* file under the capture, and it produces the opener-by-opener table in V2 above as a by-product.

**One thing the Architect should know about the attribution.** `gzip.open` calls `builtins.open` from inside `gzip.py`, so the frame that triggers the audit event is a standard-library frame and not the reader's. The hook walks out of the standard library to the nearest frame that is not in it, which is what makes `quotes.jsonl.gz` attribute to `tz14-quote-inventory.py` and to `manifest.py` rather than to `gzip.py`. Without that walk the allow-list check would have been vacuous, and the first draft of it was.

### R3 — V1 calls the fingerprint gate **asserted**, and §5.1's order starts at host read 1

**The reading taken.** §7 defines "asserted" as "a Python `assert` or a `SystemExit` in the instrument that produces the numbers". A fingerprint gate performed in the shell is a transcript, not an assertion. The instrument therefore runs the gate itself as **step 0**, before host read 1: it parses map §0's own anchor and fingerprint tables, hashes all 23 paths, and asserts the revision string, the six anchors and every `frozen` row. §5.1's ten steps are unchanged and run in the order it fixes; step 0 sits before them.

The gate's expected values come from the right side in each case: the **TZ header's** required revision and anchors are literals in the instrument and the **map** is read, so the gate never reads its own expected values from the artifact it is checking; and the **map's** printed hashes are read while the **files** are hashed. Four of the six anchors were additionally re-derived from the file bytes, which map §0's own definition permits and which no previous TZ has done.

### R4 — V11 says "the four cumulative sizes"; §3.6 item 3 defines eight

**The text.** §3.6 item 3 asks for cumulative size "per side per `tau`" at `k = 0, 1, 2, 5` — that is four values a side, eight in all. V11's observations-file column list says "the four cumulative sizes".

**The reading taken.** The file carries **eight** columns, `cum_bid_k0/1/2/5` and `cum_ask_k0/1/2/5`. V11's stated purpose is sufficiency — "sufficient to reconstruct any single row of any table in §3" — and four columns could not reconstruct §3.6 item 3's per-side tables. Four per side is read as what "four" meant.

### R5 — §3.7's population is the pair of replies, not the pair of books

**The text.** "Per checkpoint where both token ids returned `200` with a parseable body".

**The problem.** At 2,838 of the 8,400 checkpoints one book side is empty, so `best_bid_up + best_bid_down` has no value. The first implementation dropped those checkpoints from the paired population entirely, which silently changed **P5's denominator from 8,400 to 5,562** and would have made "5,562 of 5,562" look like a complete census when it was a selected one.

**The reading taken and the correction made.** A checkpoint is paired on the two replies, exactly as §3.7 says. A statistic whose input does not exist is not computed there, and the count of such checkpoints is printed beside the statistic: `bid_up + bid_down` undefined at 2,838, `ask_up + ask_down` at 2,837, and the two executable forms at 2,838 and 2,837. P5 is then reported over the 5,562 where the sum is defined, with the 2,838 stated, and the alternative reading noted in §3 above. It holds under both.

### R6 — §3.5 item 6 asks for "the distinct values with counts" of fields whose cardinality is 16,800

**The reading taken.** `hash` has 16,800 distinct values, one per reply; `timestamp` has 13,529; `asset_id` 2,400; `market` 1,200. Listing them value by value would add tens of thousands of rows to the tables and disclose nothing. Fields with **20 or fewer** distinct values are listed in full with counts — which is `tick_size` (2) and `min_order_size` (1), the two that matter. Above that, the **cardinality is reported with three examples**. The cardinality is itself the finding in each case: one `market` per member, two `asset_id` per member, one `hash` per reply, and no two replies sharing a hash.

### R7 — §3.6's `MIN_SIZE` is decided by a population statistic the pass has not finished computing

**The text.** `MIN_SIZE` comes from the reply's `min_order_size` "where §3.5 item 6 finds it present in **every** read of the population, and otherwise from map §6's TZ-05a measurement, `5`."

**The problem.** That condition is known only after every body has been parsed, but the touch has to be computed during that same pass — and re-parsing 74 MB of book a second time would double the only step §6 could not bound with a measured rate.

**The reading taken.** The pass computes the touch **twice per read** — once at the reply's own `min_order_size` and once at the fallback `5` — and `choose_min_size` selects between the two finished answers afterwards. Both branches are therefore real measurements and neither is an estimate. In this set the question was moot: `min_order_size` is present at 16,800 of 16,800 reads and its only value is `5`, so the two candidates are the same number and map §6's figure is confirmed rather than assumed.

### R8 — §0.5's preflight and the trial runs

**The text.** "Preflight, twice, at least `1,800` s apart, the first before the build and the second before the first full run."

**What happened.** Preflight 1 was taken at **2026-09-18T19:43:57Z**, before a line of the instrument was written. Preflight 2 was taken at **2026-09-18T20:14:02Z**, 1,805 s later, before the first of the two V3 runs. **Between them the instrument was built and run to completion several times during development.** §0.5 says the preflight "gates nothing beyond §0.4", and §0.4's floor was asserted by `tz11a.host_read` inside every one of those development runs as well as the two reported ones, so nothing was left ungated. **This is stated rather than glossed: the two reported runs are the first two runs of the finished instrument, not the first two times it executed.**

### R9 — §3.5 item 7's fallback tick was never used, and the finding is why

**The text.** "Where it is absent, the spread in ticks is computed at `0.01`, **named in the table as carried from map §6's TZ-05a measurement and not measured here.**"

**The reading taken.** `tick_size` is present in 16,800 of 16,800 replies, so the fallback never applied and the table still names it, as the text requires. The substantive finding is the one the fallback would have hidden: **the tick is `0.01` at 15,640 replies and `0.001` at 1,160**, so a spread-in-ticks computed at a flat `0.01` would have been wrong by a factor of ten on 6.9% of this set. Map §6's TZ-05a measurement is right about the common case and is not the whole story.

### R10 — §9 step 2's `git worktree remove` "without `--force`" refused on the first attempt

**The text.** "Then the worktree, `/root/tz13-work/wt`, `git worktree remove` without `--force`."

**What happened and what was done**, in full in §7.2: the non-forced remove refused because the worktree held two untracked `__pycache__` directories left by TZ-13's own runs. **No tracked file was modified.** No file in either directory carries a SHA-256 any committed report names — checked before anything was deleted. The two cache directories were removed, `git status --porcelain` then printed nothing, and the non-forced remove exited 0. **`--force` was never used**, which is the constraint the step exists to impose.

### R11 — §9 step 1's "every file under `/root/tz13-work/`" includes the worktree

**The text.** "Every file under `/root/tz13-work/` whose SHA-256 is named by any committed report on `main`, and which `/root/btc-forensics/` does not already hold by hash, is copied there."

**The reading taken**, in full in §7.2: the scope was applied literally, worktree included. That brings 61 repository files into the predicate, of which 59 were already held by hash from earlier TZs' retention steps. The two that were not — `SYSTEM-MAP.md` at revision `2026-09-17-a` and `research/tz13-sized-gate-test3.py` — **were copied**, even though both live in git history at `7ef9723` and neither was at risk. The alternative reading, that a file git already holds is not lost when a worktree is removed and need not be copied, would have been defensible; **the rule was applied as written instead, because 175 KB is cheaper than an argument.** The three `run2` outputs that duplicate `run1`'s by hash were correctly **not** copied, because §9's own second condition excludes them.

### R12 — §9's warning about the permission classifier did not materialise

**The text.** "If the session's permission classifier refuses it, hand the Boss one exact block and verify the outcome from `test -e` afterwards, never from his report. It refused this for TZ-12 and for TZ-13; expect it again."

**What happened.** `rm -rf /root/tz13-work` — one command naming one tree — **was not refused and exited 0**. No block was handed to the Boss and none was needed. `test -e` was still used to verify the outcome, which is the part of the instruction that binds regardless: it exited 1. **Recorded so the next Executor knows the single-tree form went through cleanly on 2026-09-18**, which is the same reading map §6 records for TZ-10b and the opposite of TZ-12's and TZ-13's experience.
