# TZ-12 — the gate's own error rates — REPORT

**Status: executed.** Every §0 gate passed. The instrument was built, `--emit` measured the two
literals, and two full runs completed with every instrument `assert` holding. Their three
deterministic outputs are byte-identical. **This report reads no label and carries no verdict:**
§4's gate is fixed here for TZ-13, and no observed statistic of any set is computed under it.

- **The one table this TZ freezes** (M1, the fit set alone, no label). `SIGMA_LOG_NU`, the
  member-bootstrap standard deviation of `log ν̂` over 24 refits of the 280 admissible fit
  members, is 0.476750 / 0.338445 / 0.361253 / 0.236061 / 0.0876792 / 0.0557673 / 0.0326229 at `tau` 240 … 10. It is 0.24 to 0.48 at `tau` 240 … 90 and 0.03 to 0.09 at 60 … 10.
  **`tau = 10` is censored:** 7 of 24 refits put `ν̂*` on the search's lower bound
  `2.05`. Every other `tau` has at most one bound hit.
- **TZ-11a's gate, sized after the fact** (M2). Labels were drawn from the frozen pricer's own
  `p_t`: 20,000 null replicates per population, 14 populations.
  - **Old G3** fails an exactly correct pricer, per `tau`, with probability
    0.345 / 0.247 / 0.224 / 0.259 / 0.337 / 0.620 / 0.703 on test 2's admissible rows, at `tau` 240 … 10. Some `tau` fails with
    probability at least **0.703**, or **0.979** under independence
    across `tau`. On test 1 the per-`tau` figure is 0.684 to 1.000, and some `tau` fails
    with probability **1.000**.
  - **Old G1** fails a correct pricer at `tau = 240` on test 1 with probability
    0.0985 (1970 of 20,000). On test 2 it does so in 0 of 20,000 replicates at every `tau`.
  - **Old G2** has 0 eligible bins at every gated `tau` on test 1. On test 2 the six-`tau` total
    reaches 3 with probability 0.000080 under independent per-`tau` draws.
- **§4's constants** (M3), from the predictions alone.
  - **G1 could PASS** at 7 of 7 `tau` on both test sets: `P1` is at least 0.8580
    everywhere. `P0` is 0 of 20,000 at every `tau` on test 2. On test 1 it exceeds `0.001` at
    `tau` 240, 180, 120, 90, where G1 could not FAIL.
  - **G3 could PASS on test 2 at `tau` 120 and 90 only.** `P3`, the power against
    `λ = 1.5`, is 0.2780 / 0.4990 / 0.6255 / 0.6180 / 0.4785 / 0.1645 / 0.0180 at `tau` 240 … 10. On test 1, `P3` is at most 0.0700 at
    every `tau`, so G3 could not PASS anywhere there.
  - **G2:** on test 2, `E` is 2 to 7 over the six gated `tau`, with `k2 = 2` at every one.
    On test 1, `E = 0` everywhere, so G2 would read UNDECIDABLE.
  - **G4:** on test 2, `c4` is 2.668 / 1.881 / 2.017 / 1.316 / 0.490 / 0.311 / 0.182 and `P4` is 0.0027 / 0.0087 / 0.0068 / 0.0374 / 0.9412 / 1.0000 / 1.0000 at `tau` 240 … 10. `tau = 10`
    is censored and reads UNDECIDABLE.
- **The pre-registered prediction** (§4.1): the M1, M2 and M3-G1 rows hold. **The M3-G3 row does
  not:** on test 2, `P3` is below `0.5` at `tau` 180 (0.4990, 998 of 2,000) and 60 (0.4785),
  where the Architect predicted at least `0.5`. The TZ-13 row is not measurable here.
- **Validation:**
  - V1: 6 of 6 anchors, 18 of 18 frozen rows, host 3 of 3.
  - V2: 8,400 of 8,400 rows unlabelled, and no forbidden constant or call.
  - V3: 3 of 3 outputs byte-identical.
  - V4: 7 + 14 + 21.
  - V5: 3 hashes.
  - V6: one file.
  - V7: 6 of 6.
  - V8: 8 of 8.
  - V9: the capture was unchanged across both runs.
  - Guards: 1,400 and 280 comparisons.
  - V12: recorded.
- **Publication:** branch `tz-12-sized-gate` at `6dc0e24ae1542f98789967bf48057268731a2030`, one commit and one file.
  https://github.com/seahomebatumi-ai/btc-5m-twap/pull/13 is open and not merged. §9 copied 50 files into `/root/btc-forensics/`,
  removed three worktrees, and reclaimed `/root/tz09-work/`. The session's permission classifier
  refused the removal of `/root/tz11a-work/`, so the Boss ran that one-line block, and `test -e`
  confirmed the tree gone afterwards (§5).

Nothing was written under `/var/lib/btc-recorder/`. No settled document of any interval after
`1789427700` was opened, and no quote file or market document was opened at all. The live recorder,
pid `228592` on `4216c04`, was not signalled or restarted.

Executor model: **Opus** (`claude-opus-5`), as the TZ requires.

---

## 0. Fingerprint, host, interpreter and every free-space read

The spec was read from `origin/main` = `104af7c633230aa75efc809f6c5d5fc280975e6e`, fast-forwarded into the primary checkout
from `773c052` on 2026-09-15. The map was last changed at `324b78b4fd03040ba18a2a49f79afe9d99a6c441`, and the TZ-12 file
arrived at `104af7c633230aa75efc809f6c5d5fc280975e6e`. The host gate ran at 2026-09-15T12:08:47Z and the fingerprint check at
2026-09-15T12:09:21Z.

**Map revision required:** `2026-09-15-a`. **Read:** `2026-09-15-a`.

| anchor | required by TZ-12 §0 | read from map §0 | recomputed from the file |
|---|---|---|---|
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` | not recomputed — a Release asset, not on disk |
| `A2` — collector | `6c5089330629` | `6c5089330629` | `6c5089330629` |
| `A3` — phase | `0-complete / 1-answered-no / 2-not-started` | `0-complete / 1-answered-no / 2-not-started` | — a string |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b` | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` | `9fd1c7de0f74` | `9fd1c7de0f74` |
| `A6` — pricer | `729f0bcdbee3` | `729f0bcdbee3` | `729f0bcdbee3` |

**6 of 6 anchors match.** `A1` is a Release asset and is not on disk.

### Fingerprint table

Every row of the map's §0 table, computed on `main` at `104af7c`. Lines are `wc -l` and bytes are
`wc -c`. The scratch script `/root/tz12-work/gate-check.py` parsed the map's own table, compared
each row, and asserted the frozen count, the tracked count, the revision string and the six
anchors. This report's assembler recomputed all 21 rows on `main` again at assembly and asserted
each unchanged.

| path | lines | bytes | state | SHA-256 | matches map |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 637 | 100,096 | reported | `5bc43954e277fdb78a5496b938bb317c0c61635f071a7b168b90fcd2e3088017` | — |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | yes |
| `research/twap-divergence.py` | 1,135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | yes |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | yes |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | — (equal to the map) |
| `research/pfair.py` | 441 | 19,357 | frozen | `729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68` | yes |
| `research/selftest-pfair.py` | 619 | 32,559 | frozen | `b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa` | yes |
| `research/tz06-calibration.py` | 577 | 27,138 | frozen | `715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f` | yes |
| `research/tz07a-variance-time.py` | 623 | 28,414 | frozen | `513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771` | yes |
| `research/tz07b-settlement-dispersion.py` | 515 | 24,926 | frozen | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` | yes |
| `research/tz08a-out-of-sample.py` | 745 | 38,822 | frozen | `37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c` | yes |
| `research/tz09-disk-inventory.py` | 894 | 41,004 | frozen | `b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6` | yes |
| `research/tz10b-sigma-or-link.py` | 1,224 | 61,018 | frozen | `406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088` | yes |
| `research/tz11a-student-link.py` | 1,231 | 64,732 | frozen | `0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839` | yes |
| `research/recorder/recorder.py` | 608 | 25,658 | frozen | `9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03` | yes |
| `research/recorder/config.py` | 112 | 4,773 | frozen | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | yes |
| `research/recorder/manifest.py` | 254 | 10,002 | frozen | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | yes |
| `research/recorder/analyze.py` | 813 | 34,705 | frozen | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` | yes |
| `research/recorder/probe.py` | 227 | 9,324 | frozen | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | yes |
| `research/recorder/selftest.py` | 573 | 30,591 | frozen | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` | yes |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | — (equal to the map) |

**18 of 18 `frozen` rows match on lines, bytes and SHA-256, and 2 of 2 `tracked` rows equal the map.**

TZ-12 moves no `frozen` row and adds one file. On branch `tz-12-sized-gate` it reads:

| path, on branch `tz-12-sized-gate` | lines | bytes | SHA-256 |
|---|---|---|---|
| `research/tz12-sized-gate.py` | 1,157 | 61,637 | `d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999` |

`A6` is unmoved: `research/pfair.py` is not in the branch's diff (V6).

The TZ file:

| path | lines | bytes | SHA-256 |
|---|---|---|---|
| `CryptoTZ/TZ-12-sized-gate.md` | 911 | 47,068 | `cb845f93f61cc8558bcf611c38e5b6a1b859219574bb20e0e806e802263e5d6a` |

### Worktrees

At the host gate the primary checkout `/root/btc-5m-twap` was on `main` at `104af7c`, with three
other worktrees registered: `/root/tz09-work/wt`, `/root/tz09-work/wt-report` and
`/root/tz11a-work/wt`. The run added `/root/tz12-work/wt` on a new branch, `tz-12-sized-gate`, at
`104af7c`, and built everything in it. The primary checkout stayed on `main` for the whole run.
§9 then removed the three older worktrees (§5).

### Host gate and resource floor

| check | required | observed |
|---|---|---|
| `/var/lib/btc-recorder/btc-updown-5m/` exists and holds interval directories | yes | yes: 1,469 directories at the host gate, `1789033800` to `1789474200` |
| recorder running; newest `runtime.jsonl` start record sha | `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` | pid `228592`, `/root/tz04a-env/venv/bin/python -B -u recorder.py`, started Sat Sep 12 09:53:04 2026. The newest start record is `recv_ns` `1789206785264516934`, sha `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` |
| filesystem | `/dev/vda2`, total `31,612,203,008` bytes | `/dev/vda2`, total `31,612,203,008` bytes |
| free space at run start | at least `2,060,000,000` bytes | `14,229,139,456` bytes at 2026-09-15T12:08:47Z |

**All three host checks pass, and so does the floor.**

### Interpreter

Every Python command of this TZ ran on `/root/tz01-env/venv/bin/python`: **Python
3.12.3**, **`numpy` 2.5.3**. `numpy` imports, so §0 does not block. The
instrument sets `OPENBLAS_NUM_THREADS`, `OMP_NUM_THREADS` and `MKL_NUM_THREADS` to `"1"` before its
first `import numpy`; V6 asserts those three are its only environment writes. The two scratch
scripts that parse the map and the reports, `gate-check.py` and `scan-forensics.py`, need only the
standard library and ran on the system `python3`, which is also 3.12.3 (§6).

### Every read of free space in the run

TZ-12 §0 requires the first to be at least `2,060,000,000` bytes and every later one at least
`2,000,000,000`.

| UTC | free bytes on `/dev/vda2` | read by | bound | at or above it |
|---|---|---|---|---|
| 2026-09-15T12:08:47Z | 14,229,147,648 | §0 preflight read 1 (`df`) | 2,060,000,000 | yes — recorded, not asserted |
| 2026-09-15T12:08:47Z | 14,229,139,456 | host gate (`df`) | 2,000,000,000 | yes — recorded, not asserted |
| 2026-09-15T16:17:14Z | 14,210,494,464 | `--emit`, start (`os.statvfs`) | 2,060,000,000 | yes — asserted |
| 2026-09-15T16:25:22Z | 14,209,740,800 | §0 preflight read 2 (`df`) | 2,000,000,000 | yes — recorded, not asserted |
| 2026-09-15T16:25:58Z | 14,210,125,824 | full run 1, run start (`os.statvfs`) | 2,060,000,000 | yes — asserted |
| 2026-09-15T16:27:59Z | 14,209,683,456 | full run 1, after the walk (`os.statvfs`) | 2,000,000,000 | yes — asserted |
| 2026-09-15T16:36:03Z | 14,209,331,200 | full run 1, run end (`os.statvfs`) | 2,000,000,000 | yes — asserted |
| 2026-09-15T16:36:05Z | 14,207,995,904 | full run 2, run start (`os.statvfs`) | 2,060,000,000 | yes — asserted |
| 2026-09-15T16:38:04Z | 14,207,688,704 | full run 2, after the walk (`os.statvfs`) | 2,000,000,000 | yes — asserted |
| 2026-09-15T16:46:04Z | 14,207,672,320 | full run 2, run end (`os.statvfs`) | 2,000,000,000 | yes — asserted |
| 2026-09-15T21:13:13Z | 14,206,689,280 | this report's assembler (`os.statvfs`) | 2,000,000,000 | yes — asserted |

11 reads in all. 8 are asserted by a Python `assert` that aborts below the bound; the other 3 were compared by reading them, so they are **recorded, not asserted**. An `os.statvfs` read is `f_bavail · f_frsize`, the quantity `df -B1` prints as `Avail`.

### The §0 preflight — recorded, and gating nothing beyond the floor

| read | taken (UTC) | free bytes on `/dev/vda2` | `du` of `/root/PROJECT_GAMING_PS5` (bytes) | `is-enabled` (exit) | `is-active` (exit) |
|---|---|---|---|---|---|
| 1 | 2026-09-15T12:08:47Z | 14,229,147,648 | 360,812,544 | `disabled` (1) | `inactive` (3) |
| 2 | 2026-09-15T16:25:22Z | 14,209,740,800 | 361,918,464 | `disabled` (1) | `inactive` (3) |

The two reads are **15,395 s** apart, more than the `1,800` s asked for: a usage limit paused
the session between them (§6). No file of that project was opened: `du` reads sizes only.

- **Free space:** it changed by `-19,406,848` bytes, **`-108,915,341` bytes/day** at that rate.
- **`PROJECT_GAMING_PS5`:** it changed by `+1,105,920` bytes, **`+6,206,657` bytes/day**.
- **`telemetry-watch.service`:** `disabled` (exit 1) and `inactive` (exit 3) at both reads.

**This run's own footprint, stated separately** (System Map §7 item 29): `/root/tz12-work` held
`8,192` bytes on disk at read 1 and `2,666,496` at read 2, and the session store
`/root/.claude` `114,741,248` and `114,225,152`. Both are inside the free-space figure. At
assembly `/root/tz12-work` held `5,636,096` bytes. This is arithmetic on two reads, and it
gates nothing.

---

## 1. The measurements, in §3's order, per set before pooled

### 1.0 The sets, the walk, the rows

- fit (TZ-06 400): 443 units considered (1789033800 … 1789166400), 400 members (1789035000 … 1789166400), 43 non-members (disconnect: 41, disconnect + no chainlink at or before T0-300: 2); member list `6d94a346a47a04a1a0849968effd9023d7585fe628b304ba2ae7a15953ee67f9`; disclosure rows SHA-256 `9177813a50a68da8170fdfab8e2a106e6b0f5598b885f8aa0db656b51b555bef`
- test 1 (TZ-08a 400): 433 units considered (1789166700 … 1789296300), 400 members (1789166700 … 1789296300), 33 non-members (disconnect: 33); member list `3b17729c050e5fbf8fed1bd0877d5dd5c229370609cd672c84eeed1ddc3d5762`; disclosure rows SHA-256 `898f12c6631d3b9063026394373a17a0550e45918a10fbe2a43c53348de0ee6c`
- test 2 (first 400 after 1789296300): 438 units considered (1789296600 … 1789427700), 400 members (1789296900 … 1789427700), 38 non-members (disconnect: 38); member list `2dd0fcc4dc2cf379e08c21a4524c3eab799aad7bff3136c37e32910cecb8fa70`; disclosure rows SHA-256 `4ed308770ca84baa7b985caf7478d6d939b43f2376b8dc4cdefde361847aa70c`

- The three sets were formed by `tz11a.the_sets(manifests)`, unmodified. Inside it, the fit set's
  and test 1's member-list hashes are asserted equal to their committed values, and the three sets
  are asserted pairwise disjoint.
- Test 2's hash is asserted equal to `TEST2_SHA256`, the value TZ-11a's report states in its §1.0.
  **3 hashes asserted.**
- Each set's unit-by-unit disclosure, as `tz11a.the_sets` returns it, is hashed above, and this
  report's assembler asserts the three hashes equal to the same serialization of the disclosure
  in TZ-11a's committed run output (`tz11a-work--run-1--tz11a-results.json`, SHA-256 `3b149e162c6807b827041e90e268a27633ab385ee11240c6de39a7bf92a4960b`, the file TZ-11a's report V3 names, now in `/root/btc-forensics/`): **3 of 3 equal**. The
  unit-by-unit listing is therefore TZ-11a's V11 and is not repeated.
- Every member was walked with `tz11a.walk_member(t0, manifests, False)`: the fit set first, then
  test 1, then test 2, each in ascending `T0` — **1,200 members**. Every member at every `tau`
  became one row through `tz11a.checkpoint_row`: **8,400 rows**, every one with `label = None`.
- **The admissible rows** of a set at `tau` are its rows with `admissible` true: `sigma_hat` at or
  above the committed literal `pfair.ADMIT[tau]`. Their `T0` list is asserted equal to
  `tz11a.admissible_members(walked, members, pfair.ADMIT)[tau]` and their count to TZ-11a's §1.2,
  **21 of 21 counts**:

| set | tau | admissible members | TZ-11a §1.2 | `tz07b.member_list_sha` of the admissible `T0` list |
|---|---|---|---|---|
| fit | 240 | 280 | 280 | `f34ed3719ada27d45ba89df3109a49850b2c31ff226a2ba781657b94d0ef359b` |
| fit | 180 | 280 | 280 | `15b311fdeacc0b77e41f44fc0815c0002293b89eb703ee2bfca599fedb43487e` |
| fit | 120 | 280 | 280 | `86cc4557a191622a901a5448791d274df79a02fd7423cb4929e32e3889df9509` |
| fit | 90 | 280 | 280 | `e5565285dc34a163217a943f6e2d22fb8597e588f55e1d8c5372b34f67be1c92` |
| fit | 60 | 280 | 280 | `593d42d83e14d8ddd2e448a9adac24b06111c98cb9381dc5061e7ae5708965ad` |
| fit | 30 | 280 | 280 | `5f912a591aceae27a42d7fc2994e36788092d376c3e4f60731bcbd8f5865cdf8` |
| fit | 10 | 280 | 280 | `9989d6f5ca61a6d383fdba0a01eccbbe86c470ee51703529d1c84a7c197f7c25` |
| test1 | 240 | 35 | 35 | `170b3fa8e02e79e8ab22d365b3e491ea769d578b5a54e7cf7603dc310257340d` |
| test1 | 180 | 29 | 29 | `56f9ecf8244315252254ba466d87decf6b666b6bec11c3a8773c50cf15c7092e` |
| test1 | 120 | 28 | 28 | `3b9dc77b4df80101d078a833f7cc7216adaa7f87abd838efe8d0cf0581c3c4bd` |
| test1 | 90 | 28 | 28 | `ac4382254b0772521e80e204eefbb91f5d4a6b0ae0613021b5b5051b13b5789f` |
| test1 | 60 | 28 | 28 | `0b94bbcb885ce86f3b9048d9cfcfde4a942b1e428e4318d0e2b81e0199578e07` |
| test1 | 30 | 28 | 28 | `b73364ae4c7ed9599e985ea94d3678ab814b1102f770fe4b0746adba3d736dfb` |
| test1 | 10 | 30 | 30 | `47dd4074333eed01c2015ff439ca8d75780f348688bad6c1bad23d1569ef9e01` |
| test2 | 240 | 231 | 231 | `94fa624c5b7b438af54ddad9faf5c19dc4c2bf685fdd01c00fb38cf89d1556fc` |
| test2 | 180 | 237 | 237 | `d6f6fa8fd458d980d25db9ef941ae05054f4b1bf1cd054231e9406db4568e67d` |
| test2 | 120 | 233 | 233 | `482940f46cca9ac51dacaf1434ee4fc20e1e650541010a9dca0c669fc88508b6` |
| test2 | 90 | 234 | 234 | `1357e8043ab26ffe5935bf4e3081b876feca754b0ab56ecd3b3870030afc8f86` |
| test2 | 60 | 233 | 233 | `829bdf3b7f715379cbdc34befe7ad0828c5d70030b41e3fcbea93e86c05109c3` |
| test2 | 30 | 235 | 235 | `5b1ac87ae6d8a079d88287457ef1ccb0648f2754890f2cf13e97b1bbbd61416a` |
| test2 | 10 | 235 | 235 | `b9196072bb593333e463eb20aad37b312f6b688ba9c44232f9e1ec9cfc10376a` |

### 1.1 M1 — the member-bootstrap spread of `log ν̂`, on the fit set alone

At each `tau`, the fit set's 280 admissible members in ascending `T0` were resampled with
replacement, 24 times, from the stream `SeedSequence([20260915, 0, tau, 9])`: one
`rng.integers(0, 280, size=280)` per replicate, the drawn members sorted with duplicates kept and
adjacent. Each resample was fitted by the committed `tz11a.fit_student` over
`tz11a.population(walked, drawn, tau)[0]`. `x_b = log ν̂*`, and `SIGMA_LOG_NU[tau]` is
`statistics.stdev` of the 24 `x_b`, denominator 23. A `tau` is censored when more than 2 of its 24
replicates put `ν̂*` on a search bound. No outcome is read: M1's inputs are the feed and the
manifests.

| tau | `SIGMA_LOG_NU`, measured | six significant digits | mean of `x_b` | `log LINK_NU` | difference | smallest `ν̂*` | largest `ν̂*` | skewness `g1` | `ν̂*` on a bound (lower, upper) | `ŝ*` on a bound | censored | distinct members | anchors | evaluations (min … max, total) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 240 | 0.476749533 | 0.476750 | 2.467049 | 2.263917 | +0.203132 | 7.2411 | 60.0000 | +1.9713 | 1 (0, 1) | 0 | no | 165 … 185 | 99940 … 100910 | 1932 … 2116, 49864 |
| 180 | 0.338445036 | 0.338445 | 2.625845 | 2.618001 | +0.007844 | 6.1851 | 36.1389 | +0.4469 | 0 (0, 0) | 0 | no | 169 … 187 | 116518 … 117636 | 1978 … 2116, 49404 |
| 120 | 0.361252596 | 0.361253 | 3.121944 | 3.006959 | +0.114985 | 13.2644 | 60.0000 | +0.6936 | 1 (0, 1) | 0 | no | 166 … 188 | 133778 … 134655 | 1932 … 2070, 48208 |
| 90 | 0.236060804 | 0.236061 | 2.807257 | 2.775597 | +0.031660 | 10.8333 | 33.0333 | +0.9243 | 0 (0, 0) | 0 | no | 169 … 181 | 142292 … 143014 | 1978 … 2070, 49082 |
| 60 | 0.087679169 | 0.0876792 | 2.272945 | 2.252859 | +0.020086 | 7.8934 | 11.0106 | -0.6405 | 0 (0, 0) | 0 | no | 168 … 189 | 150954 … 151372 | 2070 … 2116, 50232 |
| 30 | 0.055767260 | 0.0557673 | 1.581690 | 1.567738 | +0.013952 | 4.3511 | 5.3898 | -0.1940 | 0 (0, 0) | 0 | no | 167 … 192 | 159570 … 159837 | 2162 … 2163, 51891 |
| 10 | 0.032622855 | 0.0326229 | 0.751290 | 0.758415 | -0.007125 | 2.0500 | 2.2619 | +0.5562 | 7 (7, 0) | 0 | yes | 170 … 190 | 165269 … 165442 | 2300 … 2339, 55532 |

- **`SIGMA_LOG_NU`**, frozen at six significant digits: 0.476750 / 0.338445 / 0.361253 / 0.236061 / 0.0876792 / 0.0557673 / 0.0326229 at `tau` 240 … 10.
- **Censored:** `tau` 10 — more than 2 of 24 replicates on a search bound (10: 7 of 24); every other `tau` has at most 2.
- The skewness is `g1 = m3 / m2^1.5` with population moments. Every replicate's draw hash,
  distinct-member count, anchors, `ν̂*`, `ŝ*`, four bound flags, evaluations and `log ν̂*` are in
  `tz12-bootstrap.csv`, 168 rows; its full drawn list is in `tz12-results.json` (V11).

**Seconds, run 1** (from `tz12-host.json`; they differ between runs by construction):

| tau | replicates | seconds, total | seconds per replicate, mean | slowest replicate | evaluations | anchor-evaluations |
|---|---|---|---|---|---|---|
| 240 | 24 | 36.8 | 1.53 | 1.70 | 49,864 | 5,016,889,168 |
| 180 | 24 | 41.8 | 1.74 | 1.98 | 49,404 | 5,795,369,294 |
| 120 | 24 | 46.5 | 1.94 | 2.13 | 48,208 | 6,470,436,728 |
| 90 | 24 | 51.2 | 2.13 | 2.66 | 49,082 | 7,004,626,448 |
| 60 | 24 | 56.7 | 2.36 | 2.51 | 50,232 | 7,590,340,032 |
| 30 | 24 | 67.4 | 2.81 | 3.11 | 51,891 | 8,285,989,383 |
| 10 | 24 | 90.3 | 3.76 | 3.93 | 55,532 | 9,183,089,880 |
| all | 168 | 390.7 | 2.33 | — | 354,213 | 49,346,740,933 |

### 1.2 M2 — TZ-11a's gate, sized after the fact, from predictions alone

Each of the 14 populations — test 1's and test 2's admissible rows at each `tau` — received 20,000
null replicates, their labels drawn from the pricer's own `p_t` (§3.4). The columns are TZ-11a
§4's gates applied to those replicates:

- **old G1:** the fraction of null replicates whose `tz06.brier` is at or above `0.2496`;
- **old G2:** the fraction with at least one failing bin, and the distribution of failing bins;
- **old G3:** the fraction with `|λ̂*_grid − 1| > 0.15`;
- **old G4:** `2 (1 − Φ(log 2 / s))`, `s = SIGMA_LOG_NU[tau] · sqrt(1 + 280 / m)`, a normal
  approximation.

The per-set G2 figure is **under independent per-`tau` draws**: a member's label is shared across
`tau`, and the true joint cannot be simulated from marginal predictions. **These figures describe a
committed verdict and change nothing about it.**

#### test 1 (TZ-08a 400), admissible rows

| tau | n | old G1: null Brier `>= 0.2496` | old G2: null `F >= 1` | null `F` distribution | old G3: null `\|λ̂_grid − 1\| > 0.15` | null `λ̂_grid` at 0.5 | old G4, normal approximation |
|---|---|---|---|---|---|---|---|
| 240 | 35 | 0.0985 (1970 of 20,000) | 0.0000 (0 of 20,000) | 0: 20000 | 0.7637 (15273 of 20,000) | 0.0706 (1411 of 20,000) | 0.6279 |
| 180 | 29 | 0.0338 (676 of 20,000) | 0.0000 (0 of 20,000) | 0: 20000 | 0.7341 (14682 of 20,000) | 0.0660 (1320 of 20,000) | 0.5304 |
| 120 | 28 | 0.0145 (290 of 20,000) | 0.0000 (0 of 20,000) | 0: 20000 | 0.6929 (13858 of 20,000) | 0.0549 (1099 of 20,000) | 0.5629 |
| 90 | 28 | 0.0016 (33 of 20,000) | 0.0000 (0 of 20,000) | 0: 20000 | 0.6839 (13679 of 20,000) | 0.0893 (1786 of 20,000) | 0.3760 |
| 60 | 28 | 0.0000 (0 of 20,000) | 0.0000 (0 of 20,000) | 0: 20000 | 0.7416 (14832 of 20,000) | 0.1635 (3270 of 20,000) | 0.0171 |
| 30 | 28 | 0.0000 (0 of 20,000) | 0.0000 (0 of 20,000) | 0: 20000 | 0.7877 (15755 of 20,000) | 0.2500 (4999 of 20,000) | 0.0002 |
| 10 | 30 | 0.0000 (0 of 20,000) | 0.0000 (0 of 20,000), not gated | 0: 20000 | 1.0000 (20000 of 20,000) | 0.9645 (19290 of 20,000) | 0.0000 |

Old G2, the six-tau total of failing bins reaching 3, under independent per-tau draws: **0.000000** (0 eligible bins over the six gated tau). Old G3, some tau fails: at least **1.0000** (the largest per-tau fraction); **1.0000** as `1 − Π(1 − fraction)`.

#### test 2 (first 400 after 1789296300), admissible rows

| tau | n | old G1: null Brier `>= 0.2496` | old G2: null `F >= 1` | null `F` distribution | old G3: null `\|λ̂_grid − 1\| > 0.15` | null `λ̂_grid` at 0.5 | old G4, normal approximation |
|---|---|---|---|---|---|---|---|
| 240 | 231 | 0.0000 (0 of 20,000) | 0.0299 (597 of 20,000) | 0: 19403, 1: 587, 2: 10 | 0.3453 (6906 of 20,000) | 0.0000 (0 of 20,000) | 0.3283 |
| 180 | 237 | 0.0000 (0 of 20,000) | 0.0247 (494 of 20,000) | 0: 19506, 1: 486, 2: 8 | 0.2467 (4934 of 20,000) | 0.0000 (0 of 20,000) | 0.1655 |
| 120 | 233 | 0.0000 (0 of 20,000) | 0.0149 (299 of 20,000) | 0: 19701, 1: 296, 2: 3 | 0.2240 (4479 of 20,000) | 0.0000 (0 of 20,000) | 0.1960 |
| 90 | 234 | 0.0000 (0 of 20,000) | 0.0057 (114 of 20,000) | 0: 19886, 1: 114 | 0.2586 (5171 of 20,000) | 0.0000 (0 of 20,000) | 0.0476 |
| 60 | 233 | 0.0000 (0 of 20,000) | 0.0022 (43 of 20,000) | 0: 19957, 1: 43 | 0.3367 (6735 of 20,000) | 0.0006 (12 of 20,000) | 0.0000 |
| 30 | 235 | 0.0000 (0 of 20,000) | 0.0013 (25 of 20,000) | 0: 19975, 1: 25 | 0.6202 (12404 of 20,000) | 0.0648 (1295 of 20,000) | 0.0000 |
| 10 | 235 | 0.0000 (0 of 20,000) | 0.0019 (38 of 20,000), not gated | 0: 19962, 1: 38 | 0.7034 (14068 of 20,000) | 0.4345 (8690 of 20,000) | 0.0000 |

Old G2, the six-tau total of failing bins reaching 3, under independent per-tau draws: **0.000080** (24 eligible bins over the six gated tau). Old G3, some tau fails: at least **0.7034** (the largest per-tau fraction); **0.9788** as `1 − Π(1 − fraction)`.

---

## 2. §4's constants per population, and the prediction beside what was measured

Every label-free constant §4 defines, for each of the 14 populations, from §3.4's arithmetic on the
rows' predictions alone. `P0` is the null fraction with Brier at or above `0.2496`; `P1` the
fraction of 2,000 coin replicates (labels at `1/2`) at or above it. `k2` is the smallest `k`,
`1 <= k <= E`, with at most 20 of the 20,000 null `F` at or above it. `crit3` is the 19,950th
smallest of the 20,000 null `LR`. `P3`, `P_under` and `P_double` are the fractions of 2,000
replicates drawn at `λ = 1.5`, `1/1.5` and `2` with `LR > crit3`. `c4 = Z4 · SIGMA_LOG_NU ·
U_BOOT · sqrt(1 + 280 / m)`, and `P4` is §4's formula. "Could PASS" is `P1 >= 0.5` for G1 and
`P3 >= 0.5` for G3.

**No observed statistic of either test set is computed under §4.** Tests 1 and 2 were judged by
TZ-11a §4, and this TZ reads none of their labels.

#### test 1 (TZ-08a 400), admissible rows

| tau | m | G1 `P0` | G1 `P1` | G2 `E` | G2 `k2` | null `F >= k2` | G3 `crit3` | G3 `P3` (λ = 1.5) | `P_under` (λ = 1/1.5) | `P_double` (λ = 2) | G4 `c4` | G4 `s` | G4 `P4` | `LINK_NU / 2 < 2.05` | censored | G1 could PASS | G3 could PASS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 240 | 35 | 0.0985 (1970 of 20,000) | 0.8580 (1716 of 2,000) | 0 | — | — | 6.858509 | 0.0200 (40 of 2,000) | 0.0035 (7 of 2,000) | 0.0405 (81 of 2,000) | 5.381827 | 1.430250 | 0.0005 | no | no | yes | no |
| 180 | 29 | 0.0338 (676 of 20,000) | 0.9160 (1832 of 2,000) | 0 | — | — | 7.119029 | 0.0370 (74 of 2,000) | 0.0025 (5 of 2,000) | 0.1285 (257 of 2,000) | 4.157058 | 1.104761 | 0.0009 | no | no | yes | no |
| 120 | 28 | 0.0145 (290 of 20,000) | 0.9410 (1882 of 2,000) | 0 | — | — | 7.612406 | 0.0525 (105 of 2,000) | 0.0065 (13 of 2,000) | 0.1630 (326 of 2,000) | 4.508433 | 1.198141 | 0.0007 | no | no | yes | no |
| 90 | 28 | 0.0016 (33 of 20,000) | 0.9615 (1923 of 2,000) | 0 | — | — | 7.554070 | 0.0700 (140 of 2,000) | 0.0000 (0 of 2,000) | 0.2780 (556 of 2,000) | 2.946038 | 0.782926 | 0.0020 | no | no | yes | no |
| 60 | 28 | 0.0000 (0 of 20,000) | 0.9845 (1969 of 2,000) | 0 | — | — | 7.202405 | 0.0570 (114 of 2,000) | 0.0000 (0 of 2,000) | 0.2610 (522 of 2,000) | 1.094235 | 0.290799 | 0.0839 | no | no | yes | no |
| 30 | 28 | 0.0000 (0 of 20,000) | 0.9870 (1974 of 2,000) | 0 | — | — | 7.190446 | 0.0275 (55 of 2,000) | 0.0000 (0 of 2,000) | 0.1135 (227 of 2,000) | 0.695975 | 0.184959 | 0.4939 | no | no | yes | no |
| 10 | 30 | 0.0000 (0 of 20,000) | 0.9965 (1993 of 2,000) | 0 (printed, not gated) | — | — | 4.077555 | 0.0055 (11 of 2,000) | 0.0010 (2 of 2,000) | 0.0160 (32 of 2,000) | 0.394603 | 0.104868 | 0.9978 | yes | yes | yes | no |

#### test 2 (first 400 after 1789296300), admissible rows

| tau | m | G1 `P0` | G1 `P1` | G2 `E` | G2 `k2` | null `F >= k2` | G3 `crit3` | G3 `P3` (λ = 1.5) | `P_under` (λ = 1/1.5) | `P_double` (λ = 2) | G4 `c4` | G4 `s` | G4 `P4` | `LINK_NU / 2 < 2.05` | censored | G1 could PASS | G3 could PASS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 240 | 231 | 0.0000 (0 of 20,000) | 1.0000 (2000 of 2,000) | 5 | 2 | 10 | 8.854495 | 0.2780 (556 of 2,000) | 0.3645 (729 of 2,000) | 0.7635 (1527 of 2,000) | 2.668167 | 0.709080 | 0.0027 | no | no | yes | no |
| 180 | 237 | 0.0000 (0 of 20,000) | 1.0000 (2000 of 2,000) | 7 | 2 | 8 | 9.234764 | 0.4990 (998 of 2,000) | 0.4980 (996 of 2,000) | 0.9545 (1909 of 2,000) | 1.880949 | 0.499872 | 0.0087 | no | no | yes | no |
| 120 | 233 | 0.0000 (0 of 20,000) | 1.0000 (2000 of 2,000) | 5 | 2 | 3 | 9.385526 | 0.6255 (1251 of 2,000) | 0.4610 (922 of 2,000) | 0.9930 (1986 of 2,000) | 2.017019 | 0.536034 | 0.0068 | no | no | yes | yes |
| 90 | 234 | 0.0000 (0 of 20,000) | 1.0000 (2000 of 2,000) | 3 | 2 | 0 | 9.127945 | 0.6180 (1236 of 2,000) | 0.3660 (732 of 2,000) | 0.9950 (1990 of 2,000) | 1.316484 | 0.349863 | 0.0374 | no | no | yes | yes |
| 60 | 233 | 0.0000 (0 of 20,000) | 1.0000 (2000 of 2,000) | 2 | 2 | 0 | 9.122797 | 0.4785 (957 of 2,000) | 0.1860 (372 of 2,000) | 0.9785 (1957 of 2,000) | 0.489548 | 0.130100 | 0.9412 | no | no | yes | no |
| 30 | 235 | 0.0000 (0 of 20,000) | 1.0000 (2000 of 2,000) | 2 | 2 | 0 | 6.910353 | 0.1645 (329 of 2,000) | 0.0000 (0 of 2,000) | 0.6505 (1301 of 2,000) | 0.310647 | 0.082556 | 1.0000 | no | no | yes | no |
| 10 | 235 | 0.0000 (0 of 20,000) | 1.0000 (2000 of 2,000) | 2 (printed, not gated) | 2 | 0 | 7.164746 | 0.0180 (36 of 2,000) | 0.0000 (0 of 2,000) | 0.0770 (154 of 2,000) | 0.181723 | 0.048294 | 1.0000 | yes | yes | yes | no |

**The pre-registered prediction (§4.1), beside what was measured.** The comparison is the
instrument's arithmetic on the reported numbers; it is recorded, not asserted.

| quantity | predicted | measured | holds |
|---|---|---|---|
| M1 | each SIGMA_LOG_NU at tau 240, 180 and 120 is larger than each at 90, 60 and 30; tau = 10 is censored | SIGMA_LOG_NU 240: 0.4767 / 180: 0.3384 / 120: 0.3613 / 90: 0.2361 / 60: 0.0877 / 30: 0.0558 / 10: 0.0326; censored [10] | yes |
| M2, old G3 | on test 2's admissible rows the per-tau false-failure fraction lies in 0.15 ... 0.40 at tau 240 ... 60 and above 0.40 at 30 and at 10; on test 1's it is above 0.60 at every tau | test 2: 0.345 / 0.247 / 0.224 / 0.259 / 0.337 / 0.620 / 0.703; test 1: 0.764 / 0.734 / 0.693 / 0.684 / 0.742 / 0.788 / 1.000 | yes |
| M3, G1 | P0 <= 0.001 at every tau on test 2; above 0.001 at tau = 240 on test 1 | P0 on test 2: 0.00000 / 0.00000 / 0.00000 / 0.00000 / 0.00000 / 0.00000 / 0.00000; on test 1 at tau 240: 0.09850 | yes |
| M3, G3 | P3 >= 0.5 at tau 180, 120, 90 and 60 on test 2, and below 0.5 at 240, 30 and 10; below 0.5 at every tau on test 1 | P3 on test 2: 0.2780 / 0.4990 / 0.6255 / 0.6180 / 0.4785 / 0.1645 / 0.0180; on test 1: 0.0200 / 0.0370 / 0.0525 / 0.0700 / 0.0570 / 0.0275 / 0.0055 | no |
| TZ-13 | no gate FAILs on test 3, and the admitted domain is tau 180, 120, 90 and 60 | not measured here: test 3 is not formed | — |

---

## 3. The implementation, the two frozen literals, and where every quantity comes from

### 3.1 What was built

One new file on branch `tz-12-sized-gate`, one commit, `6dc0e24ae1542f98789967bf48057268731a2030`:

| path | change | lines | bytes | SHA-256 |
|---|---|---|---|---|
| `research/tz12-sized-gate.py` | new: the sized gate and this TZ's instrument, +1157 −0 | 1,157 | 61,637 | `d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999` |

No committed file changes (V6). Importing the file writes the three environment variables of §0
and loads `tz11a-student-link.py` once, through an `importlib` helper of the same shape as
`tz11a._load`; `tz10b`, `tz08a`, `tz07b`, `tz07a` and `tz06` are taken from that module and
never loaded a second time. It keeps the loaded module as `tz11a`, so TZ-13 can load this file
with the same helper and call §4 from it.

The functions §5.1 names, each with the contract written there: `lambda_grid`, `grid_tables`,
`draw`, `grid_lr`, `bin_counter`, `k2_of`, `crit_of`, `g4_power`, `g4_constants`, `constants`,
`readings`, `verdict`, `bootstrap`, `emit`, `build`, `tables` and `main`. It also defines a few
helpers: `stream` (§3.4 item 1's generator), `brier_scores`, `m1_literals`, `selftests`,
`own_tree`, `docstring_nodes`, `v2_static`, `v6`, `v4_fits`, `read_range`, `per_set`,
`prediction`, `disclosure_sha` and `csv_text`.

### 3.2 The two frozen literals

`--emit` ran once, from 2026-09-15T16:17:13Z to 2026-09-15T16:24:47Z: a host read at the start floor, the fit set
through `tz11a.fit_set`, its walk, V4's seven timed fits with the fail-fast (**27.4 s**,
against the `40` s limit), and M1. It printed the two literals, which were pasted into the file
verbatim:

```python
SIGMA_LOG_NU = {240: D("0.476750"), 180: D("0.338445"), 120: D("0.361253"), 90: D("0.236061"),
                60: D("0.0876792"), 30: D("0.0557673"), 10: D("0.0326229")}
SIGMA_LOG_NU_CENSORED = frozenset({10})
```

`--emit` never reads them. Each full run asserts them against its own measurement before M2
starts (V8).

### 3.3 Where every quantity comes from

| quantity | computed by |
|---|---|
| the three sets, their disclosure and their hashes | `tz11a.the_sets`, which calls `tz06.scoring_set` and `tz08a.the_set`; outcomes are read only inside `tz06.qualification` |
| `r`, `sigma_hat`, the checkpoint `state` | `tz11a.walk_member`, unmodified, `guard = False` |
| `z_student`, `p_t`, `admissible` | `tz11a.checkpoint_row` → `pfair.student_sd`, `pfair.p_fair_student`, `pfair.ADMIT` |
| `ADMIT` check | `tz11a.measure_admit`, `tz11a.check_literals` |
| `ν̂`, `ŝ`, every bootstrap fit | `tz11a.fit_student` over `tz11a.population` |
| `SIGMA_LOG_NU`, its check | `statistics.stdev`; `tz07a.six_significant` inside `tz11a.check_literals` |
| the Student log CDF on the grid | `pfair.log_t_cdf` |
| the alternatives' label probabilities | `pfair.t_cdf` |
| Brier | `tz06.brier` |
| bins, `E`, regions | `tz06.calibration` on the predictions with every label 0, `tz06.bin_of` |
| the scale search the grid is checked against | `tz07a.lambda_hat(pairs, tz11a.student_log_cdf(nu))` |
| G1's threshold, the old bands, the floors, `NU_LO` | `tz11a.G1_BRIER`, `tz11a.G3_BAND`, `tz11a.G4_BAND`, `tz11a.FLOOR_START_BYTES`, `tz11a.FLOOR_BYTES`, `tz11a.NU_LO` — read, not retyped |
| the old G2 allowance | `tz06.MAX_FAILING_BINS` |
| `Z4`, `U_BOOT` | `statistics.NormalDist().inv_cdf` and `math.sqrt`, as §5.1 writes them |
| host reads | `tz11a.host_read`, which calls `tz10b.free_bytes`, `recorder_pids`, `newest_start`, `read_set` |
| git | `tz10b.git`, fixed argument lists, no shell |

---

## 4. Validation, V1 … V12

Each check states its count. Everything called asserted is a Python `assert`, or a `SystemExit`,
that aborts the run in the instrument that produces the numbers; the rest says **recorded, not
asserted**.

### V1 — gates — asserted

Fingerprint **6 of 6** anchors. Frozen rows **18 of 18**, tracked rows **2 of 2**. Host **3 of 3**. Interpreter: Python `3.12.3`, `numpy` `2.5.3`. Free space at **11 of 11** reads is at or above its bound (§0); 8 of them are asserted.

### V2 — label isolation, asserted two ways

**Static**, over the instrument's own syntax tree (`v2_static`), asserted:

| count | value |
|---|---|
| string constants scanned, docstrings exempt | 990 (26 docstrings) |
| string constants carrying a forbidden word | 0 |
| calls scanned | 489 |
| calls of a label entry point | 0 |
| calls of `lambda_hat`, each with exactly two positional arguments | 2 of 2 |
| checkpoint rows with `label is None` after M3 | 8400 of 8400 |

- The forbidden words — `resolution`, `resolved_up`, `priceToBeat`, `quotes.jsonl`, `gamma.json` —
  are carried in `v2_static`'s own docstring and read from it through `ast.get_docstring`, because
  the TZ exempts docstrings and a list written as an ordinary string constant would fail its own
  check (§6).
- **Run time**, asserted after M3: **8,400 of 8,400** checkpoint rows carry `label is None`.
- `tz06.qualification`'s reads are the exemption §2 names. Causality is not re-tested: `p_t` and
  `sigma_hat` are TZ-11a's, and this TZ adds no quantity computed at decision time.

### V3 — determinism — asserted by the assembler

| run | started (UTC) | ended (UTC) | wall (s) | peak RSS (KB) | exit |
|---|---|---|---|---|---|
| 1 | 2026-09-15T16:25:58Z | 2026-09-15T16:36:04Z | 606.54 | 140,260 | 0 |
| 2 | 2026-09-15T16:36:04Z | 2026-09-15T16:46:05Z | 600.38 | 177,116 | 0 |

| output | lines | bytes | SHA-256, run 1 | SHA-256, run 2 | identical |
|---|---|---|---|---|---|
| `tz12-results.json` | 51,475 | 1,268,807 | `af7ef999e30964d9855e7a56eba47b24ad84f50bffca858fc4c746e42d9a89ce` | `af7ef999e30964d9855e7a56eba47b24ad84f50bffca858fc4c746e42d9a89ce` | yes |
| `tz12-tables.md` | 234 | 19,171 | `853b86cb8b74a1ff5635ec00e5289f6a703ca73a1c04bcc89f4dbaa190f5a9db` | `853b86cb8b74a1ff5635ec00e5289f6a703ca73a1c04bcc89f4dbaa190f5a9db` | yes |
| `tz12-bootstrap.csv` | 169 | 25,491 | `a7b81f74efcec68f59ae28ef6e43b2f7bb2758a6b45a27f47451a1188df2298d` | `a7b81f74efcec68f59ae28ef6e43b2f7bb2758a6b45a27f47451a1188df2298d` | yes |

Two full runs, each from a fresh process on the same commit, `6dc0e24ae1542f98789967bf48057268731a2030`, in
`/root/tz01-env/venv`. **3 of 3 deterministic outputs are byte-identical.** `cmp` returned 0
for each, and the assembler that writes this report asserts the three SHA-256 pairs equal. The
literals `--emit` printed equal both runs' measurements (V8). `tz12-host.json` holds each run's own
clock, disk reads and timings; it differs by construction and is not compared.

**The cost, measured, beside §3.1's and §3.4's statements.**

| quantity | §3.1 / §3.4 / §10 C4 statement | run 1 | run 2 |
|---|---|---|---|
| self-tests, six items (item 3: 1,005,402 `log_t_cdf` calls) | about 5 s | 6.1 s | 5.5 s |
| V6, V2's static half and the three set formations | — | 23.3 s | 23.4 s |
| the walk of 1,200 members | about 120 s with the sets | 91.6 s | 90.5 s |
| V4's seven fits, `t` | fail-fast above 40 s | 16.2 s | 16.3 s |
| projection `75 t + 500` | against CANON's 3,600 s | 1715 s | 1719 s |
| M1, 168 fits | about 457 s | 390.7 s | 385.9 s |
| M1 anchor-evaluations, and seconds per anchor-evaluation | `2,061,924,102` per replicate-set; `9.2e-9` s | 49,346,740,933 in all 24 sets; 7.92e-09 s | — |
| M2 and M3, 14 populations with the guards | about 100 s | 76.1 s | 76.6 s |
| whole run | the session about 1,900 s | 604.8 s | 598.9 s |
| `--emit` (walk of the fit set, V4's seven fits, M1) | M1 runs three times | 453.91 s wall, 81,540 KB peak RSS | — |

### V4 — the instrument reproduces what is committed — asserted

| table | tau | measured | six significant digits | literal | equal |
|---|---|---|---|---|---|
| `ADMIT` | 240 | 2.123235637109777 | 2.12324 | 2.12324 | yes |
| `ADMIT` | 180 | 2.1429795348360154 | 2.14298 | 2.14298 | yes |
| `ADMIT` | 120 | 2.1806244559445487 | 2.18062 | 2.18062 | yes |
| `ADMIT` | 90 | 2.160983936098465 | 2.16098 | 2.16098 | yes |
| `ADMIT` | 60 | 2.1672513220761105 | 2.16725 | 2.16725 | yes |
| `ADMIT` | 30 | 2.151775167488169 | 2.15178 | 2.15178 | yes |
| `ADMIT` | 10 | 2.145299154953517 | 2.14530 | 2.14530 | yes |
| `LINK_NU` | 240 | 9.62069666016924 | 9.62070 | 9.62070 | yes |
| `LINK_NU` | 180 | 13.708283482793757 | 13.7083 | 13.7083 | yes |
| `LINK_NU` | 120 | 20.225837973569792 | 20.2258 | 20.2258 | yes |
| `LINK_NU` | 90 | 16.04824317883318 | 16.0482 | 16.0482 | yes |
| `LINK_NU` | 60 | 9.514898659020202 | 9.51490 | 9.51490 | yes |
| `LINK_NU` | 30 | 4.795792061357863 | 4.79579 | 4.79579 | yes |
| `LINK_NU` | 10 | 2.134894035876875 | 2.13489 | 2.13489 | yes |
| `LINK_SCALE` | 240 | 1.3067808185007417 | 1.30678 | 1.30678 | yes |
| `LINK_SCALE` | 180 | 1.366580457230551 | 1.36658 | 1.36658 | yes |
| `LINK_SCALE` | 120 | 1.407477002976878 | 1.40748 | 1.40748 | yes |
| `LINK_SCALE` | 90 | 1.3708512138036095 | 1.37085 | 1.37085 | yes |
| `LINK_SCALE` | 60 | 1.2799710934777488 | 1.27997 | 1.27997 | yes |
| `LINK_SCALE` | 30 | 1.0818473897340763 | 1.08185 | 1.08185 | yes |
| `LINK_SCALE` | 10 | 0.6438734625246281 | 0.643873 | 0.643873 | yes |

| tau | anchors | `ν̂` | `ŝ` | search edge | evaluations |
|---|---|---|---|---|---|
| 240 | 100605 | 9.620697 | 1.306781 | interior | 2116 |
| 180 | 117405 | 13.708283 | 1.366580 | interior | 2070 |
| 120 | 134265 | 20.225838 | 1.407477 | interior | 2024 |
| 90 | 142695 | 16.048243 | 1.370851 | interior | 2024 |
| 60 | 151164 | 9.514899 | 1.279971 | interior | 2116 |
| 30 | 159684 | 4.795792 | 1.081847 | interior | 2162 |
| 10 | 165369 | 2.134894 | 0.643873 | interior | 2300 |

**`ADMIT` 7 of 7; `LINK_NU` and `LINK_SCALE` 14 of 14; admissible counts 21 of 21**, each through `tz11a.check_literals` or an `assert`. The seven fits were timed
together and carried §3.1's fail-fast (V3's cost table).

### V5 — set identity — asserted

The fit set's and test 1's hashes are asserted inside `tz11a.the_sets`; test 2's is asserted
against `TEST2_SHA256`; the three sets are asserted pairwise disjoint inside `tz11a.the_sets`.
**3 hashes asserted.** No other set is formed. Test 3 is not formed, walked or read.

### V6 — the diff — asserted

merge base `104af7c633230aa75efc809f6c5d5fc280975e6e` · head `6dc0e24ae1542f98789967bf48057268731a2030` · `git status --porcelain` for the two paths: empty · `git diff --name-only`: research/tz12-sized-gate.py · attribute stores: none · `global`/`nonlocal`: none · `os.environ` writes: OPENBLAS_NUM_THREADS, OMP_NUM_THREADS, MKL_NUM_THREADS · `SIGMA_LOG_NU` keys: [240, 180, 120, 90, 60, 30, 10]

### V7 — the self-tests — asserted

**6 of 6**, run before the walk in every full run, each an `assert`. Item 5 makes 22 assertions.
Their output, verbatim from run 1:

```
item 1: Z4 3.0233414397391534 against 3.02334143973915, relative 1.11e-15; U_BOOT 1.2446022592404145 against 1.24460225924042, relative 4.44e-15
item 2: crit_of 19949; k2_of 3, 1, None
item 3: committed search lambda 2.524551 LR 51.357331; grid lambda 2.525 LR 51.357329; |dLR| 1.55e-06, |dlambda| 0.000449
item 4: g4_power(log 2, 0.1) 0.5; g4_power(0, 0.1) 1.0
item 5: 19 readings and 3 verdicts as fixed: 22 assertions; verdicts CLOSED / NOT DISQUALIFIED on [90, 60] / UNDECIDED
item 6: SeedSequence([20260915, 2, 60, 0]) twice: first 1000 doubles identical; purpose 1's first double 0.5237832833209253 differs from purpose 0's 0.9120398243372819
self-tests: 6 of 6 items passed
```

### V8 — the frozen literals — asserted

| table | tau | measured | six significant digits | literal | equal |
|---|---|---|---|---|---|
| `SIGMA_LOG_NU` | 240 | 0.4767495325224112 | 0.476750 | 0.476750 | yes |
| `SIGMA_LOG_NU` | 180 | 0.33844503637783335 | 0.338445 | 0.338445 | yes |
| `SIGMA_LOG_NU` | 120 | 0.36125259597645115 | 0.361253 | 0.361253 | yes |
| `SIGMA_LOG_NU` | 90 | 0.23606080410791574 | 0.236061 | 0.236061 | yes |
| `SIGMA_LOG_NU` | 60 | 0.08767916898690369 | 0.0876792 | 0.0876792 | yes |
| `SIGMA_LOG_NU` | 30 | 0.05576726045414961 | 0.0557673 | 0.0557673 | yes |
| `SIGMA_LOG_NU` | 10 | 0.03262285492738584 | 0.0326229 | 0.0326229 | yes |

`SIGMA_LOG_NU_CENSORED` = [10]; this run's censored set = [10]. 8 assertions.

### V9 — the capture is untouched — asserted

`tz11a.host_read` ran at run start, after the walk and at run end, with TZ-11a's four assertions
between the first read and the last: the recorder pid unchanged, the newest start record
unchanged, the interval count not fallen, and the read-set hash unchanged. The read set is every
unit the three set formations consider and each member's predecessor: **1,314
directories, 11,251 files**.

| run | read | UTC | recorder pids | newest start sha | `recv_ns` | interval directories | read-set SHA-256 | files |
|---|---|---|---|---|---|---|---|---|
| 1 | run start | 2026-09-15T16:25:58Z | [228592] | `4216c04673ce…` | 1789206785264516934 | 1,520 | `33ab86854231c723…` | 11,251 |
| 1 | after the walk | 2026-09-15T16:27:59Z | [228592] | `4216c04673ce…` | 1789206785264516934 | 1,520 | `33ab86854231c723…` | 11,251 |
| 1 | run end | 2026-09-15T16:36:03Z | [228592] | `4216c04673ce…` | 1789206785264516934 | 1,522 | `33ab86854231c723…` | 11,251 |
| 2 | run start | 2026-09-15T16:36:05Z | [228592] | `4216c04673ce…` | 1789206785264516934 | 1,522 | `33ab86854231c723…` | 11,251 |
| 2 | after the walk | 2026-09-15T16:38:04Z | [228592] | `4216c04673ce…` | 1789206785264516934 | 1,522 | `33ab86854231c723…` | 11,251 |
| 2 | run end | 2026-09-15T16:46:04Z | [228592] | `4216c04673ce…` | 1789206785264516934 | 1,524 | `33ab86854231c723…` | 11,251 |

What the instrument can write, enumerated:

- four files into `--out`, which is asserted to lie outside the capture (`main`);
- `git` subprocesses through `tz10b.git`, in read-only forms — `merge-base`, `rev-parse`,
  `status --porcelain`, `diff --name-only` — each a fixed argument list with no shell;
- nothing else. The file imports no deletion API, and its only `open` for writing is the loop over
  the four outputs.

### V10 — the fingerprint table

Every row of map §0, in lines, bytes and SHA-256, is in §0: **18 `frozen` rows and 2 `tracked`**,
with the new file beside them as it stands on the branch.

### V11 — disclosure

- The three member-list hashes, and each set's units considered with their non-member reasons, are
  in §1.0, with the hash of each set's unit-by-unit disclosure and its equality to TZ-11a's.
- Per set and `tau`, the admissible `T0` list's `tz07b.member_list_sha` and its count: §1.0.
- Per bootstrap replicate, its draw hash, distinct-member count and anchors: `tz12-bootstrap.csv`,
  168 rows, SHA-256 `a7b81f74efcec68f59ae28ef6e43b2f7bb2758a6b45a27f47451a1188df2298d`. Its full drawn list: `tz12-results.json`, under `M1`.

### V12 — influence — recorded, not asserted

| tau | `SIGMA_LOG_NU` | leave one replicate out: smallest | largest |
|---|---|---|---|
| 240 | 0.476750 | 0.334694 | 0.487408 |
| 180 | 0.338445 | 0.275500 | 0.346039 |
| 120 | 0.361253 | 0.302633 | 0.369361 |
| 90 | 0.236061 | 0.188836 | 0.241275 |
| 60 | 0.087679 | 0.077501 | 0.089633 |
| 30 | 0.055767 | 0.051617 | 0.057021 |
| 10 | 0.032623 | 0.030213 | 0.033354 |

| set | tau | `crit3`, 20,000 null | `crit3`, first 10,000 (rank 9975) | null `LR` median |
|---|---|---|---|---|
| test1 | 240 | 6.858509 | 6.767262 | 0.460721 |
| test1 | 180 | 7.119029 | 7.135928 | 0.493515 |
| test1 | 120 | 7.612406 | 7.632961 | 0.472396 |
| test1 | 90 | 7.554070 | 7.554070 | 0.484658 |
| test1 | 60 | 7.202405 | 7.202405 | 0.505330 |
| test1 | 30 | 7.190446 | 7.424733 | 0.525171 |
| test1 | 10 | 4.077555 | 4.077555 | 0.055582 |
| test2 | 240 | 8.854495 | 8.831764 | 0.444704 |
| test2 | 180 | 9.234764 | 9.278007 | 0.451887 |
| test2 | 120 | 9.385526 | 9.517483 | 0.455779 |
| test2 | 90 | 9.127945 | 9.020739 | 0.466699 |
| test2 | 60 | 9.122797 | 9.233219 | 0.466010 |
| test2 | 30 | 6.910353 | 7.171496 | 0.478747 |
| test2 | 10 | 7.164746 | 7.584123 | 1.172548 |

Neither moves anything.

**Section 3.4 item 7's guards**, asserted inside `constants` in every run: 1,400 failing-bin
comparisons (100 per population, each `tz06.calibration` on that replicate's own pairs) and 280
`LR` comparisons (20 per population, each the committed `tz07a.lambda_hat` with the Student log CDF,
within `0.02`). The largest differences:

| set | tau | bins compared | `LR` compared | largest `\|ΔLR\|` | largest `\|Δλ̂\|` | null `λ̂_grid` at 0.85 | at 1.15 |
|---|---|---|---|---|---|---|---|
| test1 | 240 | 100 | 20 | 1.71e-06 | 0.000417 | 14 | 11 |
| test1 | 180 | 100 | 20 | 2.47e-06 | 0.00044 | 20 | 13 |
| test1 | 120 | 100 | 20 | 3.62e-06 | 0.0005 | 25 | 15 |
| test1 | 90 | 100 | 20 | 1.58e-06 | 0.000453 | 27 | 16 |
| test1 | 60 | 100 | 20 | 2.86e-06 | 0.000491 | 0 | 8 |
| test1 | 30 | 100 | 20 | 3.96e-07 | 0.00044 | 0 | 0 |
| test1 | 10 | 100 | 20 | 3.25e-10 | 3.87e-10 | 0 | 0 |
| test2 | 240 | 100 | 20 | 2.3e-05 | 0.000488 | 34 | 32 |
| test2 | 180 | 100 | 20 | 1.41e-05 | 0.000481 | 26 | 29 |
| test2 | 120 | 100 | 20 | 1.21e-05 | 0.000467 | 32 | 28 |
| test2 | 90 | 100 | 20 | 7.79e-06 | 0.000353 | 32 | 27 |
| test2 | 60 | 100 | 20 | 1.13e-05 | 0.000478 | 26 | 24 |
| test2 | 30 | 100 | 20 | 3.47e-06 | 0.000465 | 21 | 21 |
| test2 | 10 | 100 | 20 | 3.01e-07 | 0.000455 | 0 | 0 |

---

## 5. Publication and §9

- **Branch.** `tz-12-sized-gate`: one commit, `6dc0e24ae1542f98789967bf48057268731a2030`, one file, pushed to `origin`. After
  the push, `git ls-remote origin tz-12-sized-gate` printed:

  ```
  6dc0e24ae1542f98789967bf48057268731a2030	refs/heads/tz-12-sized-gate
  ```

- **Pull request.** https://github.com/seahomebatumi-ai/btc-5m-twap/pull/13, opened with `gh pr create` against `main`. **It is not merged:**
  merge is the Boss's, after the Architect's verdict.
- **No Release.** No dataset, archive or binary entered git history, and the third command below
  prints nothing.
- **This report** is the only path the run adds to `main`, in one commit.

**The separation self-check of contract §4.2, verbatim.** It ran after the branch was pushed and
before this report was committed. `/root/tz12-work/separation.py` runs the three commands as the
contract writes them and asserts each result: the first prints `0`, the second lists the one
implementation file and nothing else, and the third prints nothing.

```
$ git rev-list origin/main | grep -c 6dc0e24ae1542f98789967bf48057268731a2030
0
$ git diff --name-only origin/main origin/tz-12-sized-gate
research/tz12-sized-gate.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
```

**§9, step 1: every file a committed report names by SHA-256, copied before anything was
reclaimed.** `/root/tz12-work/copy-forensics.py` read every 64-hex-digit string in the 21 reports
on `main` and hashed every file under `/root/tz11a-work/` and `/root/tz09-work/`. It copied each
file whose hash a report names, and which `/root/btc-forensics/` did not already hold, by
exclusive create (`open(..., "xb")`). It asserts each hash at both ends and asserts that every file
already in `/root/btc-forensics/` is unchanged.

| source | destination in `/root/btc-forensics/` | bytes | SHA-256 at the source | SHA-256 at the destination | named by |
|---|---|---|---|---|---|
| `/root/tz11a-work/run-1/tz11a-observations.csv` | `tz11a-work--run-1--tz11a-observations.csv` | 4,413,283 | `576c803f27da436c6affa6211e7f4fb3d91e61f32077f7a0aac575ded2014f3b` | `576c803f27da436c6affa6211e7f4fb3d91e61f32077f7a0aac575ded2014f3b` | TZ-11a-student-link-and-domain-report.md |
| `/root/tz11a-work/run-1/tz11a-results.json` | `tz11a-work--run-1--tz11a-results.json` | 1,332,123 | `3b149e162c6807b827041e90e268a27633ab385ee11240c6de39a7bf92a4960b` | `3b149e162c6807b827041e90e268a27633ab385ee11240c6de39a7bf92a4960b` | TZ-11a-student-link-and-domain-report.md |
| `/root/tz11a-work/run-1/tz11a-tables.md` | `tz11a-work--run-1--tz11a-tables.md` | 273,814 | `c6f35a45d0699bdfbdaf60082f6f8d8acf76b5e1e87853fdd2496f86abc7d77a` | `c6f35a45d0699bdfbdaf60082f6f8d8acf76b5e1e87853fdd2496f86abc7d77a` | TZ-11a-student-link-and-domain-report.md |
| `/root/tz11a-work/run-2/tz11a-observations.csv` | `tz11a-work--run-2--tz11a-observations.csv` | 4,413,283 | `576c803f27da436c6affa6211e7f4fb3d91e61f32077f7a0aac575ded2014f3b` | `576c803f27da436c6affa6211e7f4fb3d91e61f32077f7a0aac575ded2014f3b` | TZ-11a-student-link-and-domain-report.md |
| `/root/tz11a-work/run-2/tz11a-results.json` | `tz11a-work--run-2--tz11a-results.json` | 1,332,123 | `3b149e162c6807b827041e90e268a27633ab385ee11240c6de39a7bf92a4960b` | `3b149e162c6807b827041e90e268a27633ab385ee11240c6de39a7bf92a4960b` | TZ-11a-student-link-and-domain-report.md |
| `/root/tz11a-work/run-2/tz11a-tables.md` | `tz11a-work--run-2--tz11a-tables.md` | 273,814 | `c6f35a45d0699bdfbdaf60082f6f8d8acf76b5e1e87853fdd2496f86abc7d77a` | `c6f35a45d0699bdfbdaf60082f6f8d8acf76b5e1e87853fdd2496f86abc7d77a` | TZ-11a-student-link-and-domain-report.md |
| `/root/tz11a-work/wt/.git` | `tz11a-work--wt--.git` | 45 | `29056cf78851d10feffeff525270a25158f7321f4cb80fe4157b4b07f3dc7042` | `29056cf78851d10feffeff525270a25158f7321f4cb80fe4157b4b07f3dc7042` | TZ-09-disk-inventory-report.md |
| `/root/tz11a-work/wt/SYSTEM-MAP.md` | `tz11a-work--wt--SYSTEM-MAP.md` | 84,446 | `59ee3054d2e3ac2e1335b9e163a63e32ca8721e3dbf5bb4370c338066bcd72b6` | `59ee3054d2e3ac2e1335b9e163a63e32ca8721e3dbf5bb4370c338066bcd72b6` | TZ-11a-student-link-and-domain-report.md |
| `/root/tz11a-work/wt/CryptoTZ/TZ-11-student-link-and-domain.md` | `tz11a-work--wt--CryptoTZ--TZ-11-student-link-and-domain.md` | 29,765 | `15220788b164ee4d53d32892061bbc2ebd1509acf30282dd453af2c6df86775f` | `15220788b164ee4d53d32892061bbc2ebd1509acf30282dd453af2c6df86775f` | TZ-11-student-link-and-domain-report.md |
| `/root/tz11a-work/wt/CryptoTZ/TZ-11a-student-link-and-domain.md` | `tz11a-work--wt--CryptoTZ--TZ-11a-student-link-and-domain.md` | 42,064 | `dcd05f165d9057326a930814649cf81c9033980f6fb354cde8dd1fd15628c076` | `dcd05f165d9057326a930814649cf81c9033980f6fb354cde8dd1fd15628c076` | TZ-11a-student-link-and-domain-report.md |
| `/root/tz11a-work/wt/research/pfair.py` | `tz11a-work--wt--research--pfair.py` | 19,357 | `729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68` | `729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68` | TZ-11a-student-link-and-domain-report.md |
| `/root/tz11a-work/wt/research/selftest-pfair.py` | `tz11a-work--wt--research--selftest-pfair.py` | 32,559 | `b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa` | `b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa` | TZ-11a-student-link-and-domain-report.md |
| `/root/tz11a-work/wt/research/tz07a-variance-time.py` | `tz11a-work--wt--research--tz07a-variance-time.py` | 28,414 | `513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771` | `513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771` | TZ-11a-student-link-and-domain-report.md |
| `/root/tz11a-work/wt/research/tz11a-student-link.py` | `tz11a-work--wt--research--tz11a-student-link.py` | 64,732 | `0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839` | `0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839` | TZ-11a-student-link-and-domain-report.md |
| `/root/tz09-work/after-r4.json` | `tz09-work--after-r4.json` | 1,082 | `d72114f02ad80c1f2c216b5d46a48aabd032b96b88ef6e11241b2aae998ab1b4` | `d72114f02ad80c1f2c216b5d46a48aabd032b96b88ef6e11241b2aae998ab1b4` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/before-r4.json` | `tz09-work--before-r4.json` | 1,081 | `0307104e58b6f54fa036346d79329341496e9e73ce294ef21cc3e1c287f85178` | `0307104e58b6f54fa036346d79329341496e9e73ce294ef21cc3e1c287f85178` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/df-r4-1.json` | `tz09-work--df-r4-1.json` | 473 | `a78e7866e2b12f813af2fecc3f2409aac3c5d1158342c4bd6e8cbef4ffedbb25` | `a78e7866e2b12f813af2fecc3f2409aac3c5d1158342c4bd6e8cbef4ffedbb25` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/df-r4-2.json` | `tz09-work--df-r4-2.json` | 471 | `20e3ecb52bd8ca43c82c0b649244b3d9d266496f21c16a968b0116acbcdcf26a` | `20e3ecb52bd8ca43c82c0b649244b3d9d266496f21c16a968b0116acbcdcf26a` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/df-r4-3.json` | `tz09-work--df-r4-3.json` | 473 | `aca58323b7effb4bc51f3df319d3258bd1cf8ddf051a8150bda92edac9952258` | `aca58323b7effb4bc51f3df319d3258bd1cf8ddf051a8150bda92edac9952258` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/df-r4-4.json` | `tz09-work--df-r4-4.json` | 473 | `2fa3ba1beb0a513d7232775c11c8c9517bdd7ee471d33ec14d8823290dbde574` | `2fa3ba1beb0a513d7232775c11c8c9517bdd7ee471d33ec14d8823290dbde574` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/df-r4-5.json` | `tz09-work--df-r4-5.json` | 473 | `38b4573d98f0154918c4f251d212c2b0ff0efa0f30a35e56443c0c585c7a16d7` | `38b4573d98f0154918c4f251d212c2b0ff0efa0f30a35e56443c0c585c7a16d7` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/end.json` | `tz09-work--end.json` | 1,082 | `816b4616854fe6e24bf166d729d4b6aa1e029e3ca5f517e8f3a68f41adac9fd8` | `816b4616854fe6e24bf166d729d4b6aa1e029e3ca5f517e8f3a68f41adac9fd8` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/gate.json` | `tz09-work--gate.json` | 8,140 | `ca10945591ffd04057ee51b15243b30f69588a136b303687bfccd65f085654f5` | `ca10945591ffd04057ee51b15243b30f69588a136b303687bfccd65f085654f5` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/m3-post.json` | `tz09-work--m3-post.json` | 217,866 | `66786edc8e818ff188c27dfb99ab2190e59a004e12adb6317b0d353b95613ee5` | `66786edc8e818ff188c27dfb99ab2190e59a004e12adb6317b0d353b95613ee5` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/m3.json` | `tz09-work--m3.json` | 217,564 | `fdc186632c2275c45f77df6676e40dc298ddd4e82e6c811b58c812d71eaad076` | `fdc186632c2275c45f77df6676e40dc298ddd4e82e6c811b58c812d71eaad076` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/m6.json` | `tz09-work--m6.json` | 798 | `7a7c084276909b258a6fc68a711320f91caae4bb9058588acc8aa13ae3788e0b` | `7a7c084276909b258a6fc68a711320f91caae4bb9058588acc8aa13ae3788e0b` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/prefix-script.py` | `tz09-work--prefix-script.py` | 38,979 | `8320b91dec2be4a437e61c759eae1e23b012424313460d4f8660245dc8167450` | `8320b91dec2be4a437e61c759eae1e23b012424313460d4f8660245dc8167450` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/r1-plan.tsv` | `tz09-work--r1-plan.tsv` | 10,030 | `043a971961011f7d32282ef82a436b99f49ca1a3c608e996f29831668058f29f` | `043a971961011f7d32282ef82a436b99f49ca1a3c608e996f29831668058f29f` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/r1-run2-plan.tsv` | `tz09-work--r1-run2-plan.tsv` | 10,030 | `043a971961011f7d32282ef82a436b99f49ca1a3c608e996f29831668058f29f` | `043a971961011f7d32282ef82a436b99f49ca1a3c608e996f29831668058f29f` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/r1-run2.json` | `tz09-work--r1-run2.json` | 121,573 | `3424b043bcd8a562dabeaed88201916bf99f77838d77f5ccb01760fc397c21a9` | `3424b043bcd8a562dabeaed88201916bf99f77838d77f5ccb01760fc397c21a9` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/r1.json` | `tz09-work--r1.json` | 121,573 | `3424b043bcd8a562dabeaed88201916bf99f77838d77f5ccb01760fc397c21a9` | `3424b043bcd8a562dabeaed88201916bf99f77838d77f5ccb01760fc397c21a9` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/r1c-plan.tsv` | `tz09-work--r1c-plan.tsv` | 10,030 | `043a971961011f7d32282ef82a436b99f49ca1a3c608e996f29831668058f29f` | `043a971961011f7d32282ef82a436b99f49ca1a3c608e996f29831668058f29f` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/r1c.json` | `tz09-work--r1c.json` | 121,573 | `3424b043bcd8a562dabeaed88201916bf99f77838d77f5ccb01760fc397c21a9` | `3424b043bcd8a562dabeaed88201916bf99f77838d77f5ccb01760fc397c21a9` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/r1d-plan.tsv` | `tz09-work--r1d-plan.tsv` | 10,030 | `043a971961011f7d32282ef82a436b99f49ca1a3c608e996f29831668058f29f` | `043a971961011f7d32282ef82a436b99f49ca1a3c608e996f29831668058f29f` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/r1d.json` | `tz09-work--r1d.json` | 121,573 | `3424b043bcd8a562dabeaed88201916bf99f77838d77f5ccb01760fc397c21a9` | `3424b043bcd8a562dabeaed88201916bf99f77838d77f5ccb01760fc397c21a9` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/r3-cp.log` | `tz09-work--r3-cp.log` | 19,403 | `2b60a43abd55a159c5e5b97355031efb1154359b7d5564ac909626da162b5935` | `2b60a43abd55a159c5e5b97355031efb1154359b7d5564ac909626da162b5935` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/r4.log` | `tz09-work--r4.log` | 2,707 | `9515daf5c66617e83e4b00d17e4c86dc62796db5577966c9e7c85f447a4065b9` | `9515daf5c66617e83e4b00d17e4c86dc62796db5577966c9e7c85f447a4065b9` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/r5.json` | `tz09-work--r5.json` | 484 | `cc2804e428fa06de77413cd78279996e46657752178225abb72b0e69a048cd1d` | `cc2804e428fa06de77413cd78279996e46657752178225abb72b0e69a048cd1d` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/retention.json` | `tz09-work--retention.json` | 178 | `9dbfdbe4c4871b1a419e9f124765d41d0a1c9990beb6eb3cd67027b8db1ec674` | `9dbfdbe4c4871b1a419e9f124765d41d0a1c9990beb6eb3cd67027b8db1ec674` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/t0.json` | `tz09-work--t0.json` | 294,813 | `c6c163ab0200fd055d864f04933a851911cf8bb968e4fffbae36d18c0e8ccf01` | `c6c163ab0200fd055d864f04933a851911cf8bb968e4fffbae36d18c0e8ccf01` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/t0b.json` | `tz09-work--t0b.json` | 294,816 | `8956ba5509c342a7466161353879496bcfe19a7dd3c4330f98322362af41c332` | `8956ba5509c342a7466161353879496bcfe19a7dd3c4330f98322362af41c332` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/t1.json` | `tz09-work--t1.json` | 295,775 | `a09c7df9c997749a403b132cc646b6aa854dc74261f3cd083fe5a9bed95ea64b` | `a09c7df9c997749a403b132cc646b6aa854dc74261f3cd083fe5a9bed95ea64b` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/t2.json` | `tz09-work--t2.json` | 298,819 | `37590a70483d24a14cfe16d5c2b06af643a89ad66244fab3356102467698b4ae` | `37590a70483d24a14cfe16d5c2b06af643a89ad66244fab3356102467698b4ae` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/v10.json` | `tz09-work--v10.json` | 628 | `df8251cfeb5703e4c7f1145909187f0e7a81f246514c55bb06000edbddd3e802` | `df8251cfeb5703e4c7f1145909187f0e7a81f246514c55bb06000edbddd3e802` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/v3.json` | `tz09-work--v3.json` | 3,866 | `165b9c35ca4e3f076db108cb48db8d05591a146f5d1d73476b88a08bc5398622` | `165b9c35ca4e3f076db108cb48db8d05591a146f5d1d73476b88a08bc5398622` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/v6.json` | `tz09-work--v6.json` | 51,743 | `abad040d1d57e75e02491fbf55dc8a5008882df6916cd8312b5c96366ed67f0c` | `abad040d1d57e75e02491fbf55dc8a5008882df6916cd8312b5c96366ed67f0c` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/v7.json` | `tz09-work--v7.json` | 113 | `8d4b4e919881fd835d2d7fe4d6497e5e141106635fdf210ec6183706c25520ac` | `8d4b4e919881fd835d2d7fe4d6497e5e141106635fdf210ec6183706c25520ac` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/v8.json` | `tz09-work--v8.json` | 498 | `9ff20385c438234785a873acdcb05b12358f8bcbc3f351caa999e49b4d528ece` | `9ff20385c438234785a873acdcb05b12358f8bcbc3f351caa999e49b4d528ece` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/wt/SYSTEM-MAP.md` | `tz09-work--wt--SYSTEM-MAP.md` | 48,655 | `588645c3366837f27b8ad6b1ca0acc79febfef16858ba6b060f53482c80a6f10` | `588645c3366837f27b8ad6b1ca0acc79febfef16858ba6b060f53482c80a6f10` | TZ-09-disk-inventory-report.md |
| `/root/tz09-work/wt-report/SYSTEM-MAP.md` | `tz09-work--wt-report--SYSTEM-MAP.md` | 48,655 | `588645c3366837f27b8ad6b1ca0acc79febfef16858ba6b060f53482c80a6f10` | `588645c3366837f27b8ad6b1ca0acc79febfef16858ba6b060f53482c80a6f10` | TZ-09-disk-inventory-report.md |

Copied at 2026-09-15T16:47:34Z. 272 files hashed under the two trees; 50 copied. `/root/btc-forensics/` held **141** files before and **191** after; **141 of 141** of the files already there hash exactly as before.

**§9, step 2: the three worktrees, one `git worktree remove` each, never `--force`**, run after
step 1 had exited 0. Verbatim:

```
$ git -C /root/btc-5m-twap worktree remove /root/tz11a-work/wt
exit 0

$ git -C /root/btc-5m-twap worktree remove /root/tz09-work/wt
exit 0

$ git -C /root/btc-5m-twap worktree remove /root/tz09-work/wt-report
exit 0

$ git -C /root/btc-5m-twap worktree list
/root/btc-5m-twap   104af7c [main]
/root/tz12-work/wt  6dc0e24 [tz-12-sized-gate]
```

Git refused none of them. `git worktree remove` deletes no branch, and this run deleted none:
`tz-11a-student-link` and `tz-09-disk-inventory` both still exist locally. **Neither exists on
`origin` any more.** At assembly, `git ls-remote origin` listed `tz-12-sized-gate` and neither of
the other two, although System Map §1, read on 2026-09-15, lists both there. This run's only
branch push was `git push -u origin tz-12-sized-gate` (§6).

**§9, step 3: the two trees, one command naming one tree each.** The two commands were issued
after step 2 succeeded, as two separate calls at the same moment, not chained. Verbatim:

```
$ rm -rf /root/tz11a-work; echo "rm exit $?"; test -e /root/tz11a-work; echo "test -e /root/tz11a-work exit $? at $(date -u +%Y-%m-%dT%H:%M:%SZ)"
Permission for this action was denied by the Claude Code auto mode classifier. Reason: [Irreversible Local Destruction].

$ rm -rf /root/tz09-work; echo "rm exit $?"; test -e /root/tz09-work; echo "test -e /root/tz09-work exit $? at $(date -u +%Y-%m-%dT%H:%M:%SZ)"
rm exit 0
test -e /root/tz09-work exit 1 at 2026-09-15T16:49:31Z
```

- **`/root/tz09-work/` is gone:** `rm` exited 0, and `test -e` exits 1.
- **The removal of `/root/tz11a-work/` was refused** by the session's permission classifier before
  it ran, the same class of refusal System Map §6 records for `kill` and for multi-tree `rm -rf`.
  This single-tree form had not been refused before (TZ-10b, TZ-11a). As §9 requires, the Boss
  was handed one exact block:

  ```
  rm -rf /root/tz11a-work
  ```

  The Boss reported the block done. It was verified here afterwards, not from that report:

  ```
  $ test -e /root/tz11a-work; echo "test -e /root/tz11a-work exit $? at $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  test -e /root/tz11a-work exit 1 at 2026-09-15T17:59:20Z
  ```

  `test -e` exits 1, so `/root/tz11a-work/` no longer exists.

**`/root/tz12-work/`** is TZ-13's to reclaim once this report is on `main`, on the same terms. The
files this report names by SHA-256 are the three deterministic outputs of each full run (V3), and
`/root/btc-forensics/` receives a copy of each first.

---

## 6. What could not be implemented as written, and every reading chosen

These are every point where the text needed a reading, and every workaround. None changes a
threshold, a definition or a formula.

1. **The interpreter.** Every command of the instrument ran on `/root/tz01-env/venv/bin/python`,
   Python 3.12.3 with `numpy` 2.5.3, as §0 requires. Four scratch scripts use the standard library
   only and ran on the system `python3`, also 3.12.3: `gate-check.py`, `scan-forensics.py`,
   `copy-forensics.py` and `separation.py`. None of them computes a measurement.
2. **The first host read comes before the sets exist.** §5.1's fixed order puts host read 1
   first and the sets fourth, while `tz11a.host_read` needs the read set at read 1. The instrument
   therefore passes read 1 every five-minute slot from `1789033800` to `1789427700`, the first unit
   the fit set considers and the last unit test 2 considers (TZ-11a report §1.0). At step 4 it
   asserts that list equal to "every unit the three set formations consider and each member's
   predecessor", as formed. It is 1,314 directories either way, and V9's four assertions compare
   read 1 with read 3 over the same set.
3. **V2's static half runs at step 3, beside V6.** §5.1's order names only V2's run-time check,
   at step 10. The static half reads the file's own syntax tree, as V6 does, so it runs with V6,
   before any capture file is read. The run-time half runs at step 10 as written.
4. **Where V2's forbidden words live.** V2 forbids any string constant other than a docstring
   from containing `resolution`, `resolved_up`, `priceToBeat`, `quotes.jsonl` or `gamma.json`. A
   check that searches for those words has to hold them somewhere. They sit in `v2_static`'s own
   docstring, between two marker lines, and are read from it through `ast.get_docstring`. Every
   other string constant is scanned, and the check fails if any one of them carries a word.
5. **The matrix product is formed in row blocks.** §3.4 item 4 describes one product per
   population. The instrument computes `L` for 500 replicates at a time, and each purpose's
   replicates in their own products: the null's 20,000, then the three power purposes' 2,000
   each. This host has 1 GB of memory, and the live recorder shares it: one `L` for 26,000
   replicates would be 520 MB. Each replicate's row of `L` is the same sum over the same
   population. `Y` itself is drawn in one call per purpose, and the TZ allows either.
6. **The coin purpose enters no product.** Its 2,000 replicates feed G1's `P1` through
   `tz06.brier` alone, as §3.4 item 8 counts them.
7. **V12's `crit3` from the first 10,000 null replicates** is read at the same quantile as the
   full value: rank 9,975 of 10,000, against 19,950 of 20,000.
8. **The old G3 comparison at the band's edges.** "`|λ̂*_grid − 1| > 0.15`" is evaluated in
   doubles, exactly as TZ-11a's committed gate evaluated `abs(λ̂ − 1.0) <= G3_BAND`. On the grid,
   `λ = 0.85` gives `|0.85 − 1| = 0.15000000000000002`, above the band, and `λ = 1.15` gives
   `0.1499999999999999`, inside it. The guards table reports how many null replicates landed on
   each of those two grid values.
9. **G2 at `tau = 10`.** `readings` computes G2 at every `tau` and carries a `G2_gated` flag
   from `constants`. `verdict` counts a G2 FAIL only where it is set, at `pfair.GATED_TAUS`, so G2
   at `tau = 10` is printed and never closes anything, as §4 writes it.
10. **Self-test item 5's inputs.** Each of the 19 rows sets the inputs the TZ names. Every other
    input of `readings` is held at one fixed filler, which cannot change the named gate's reading
    under §4. Only the named gate's reading is asserted, one assertion per row. The 3 verdict
    rows are built from seven `tau` of readings, and the second asserts the admitted set equal to
    `{90, 60}`.
11. **G1's `P0 <= 0.001` is compared as a fraction.** `20 / 20,000` is the same double as the
    literal `0.001`, so "at most 20 of 20,000" and "`P0 <= 0.001`" agree. The counts are printed
    beside every fraction.
12. **Two diagnostics beyond §3.2's list:** the fraction of null replicates whose `λ̂_grid` sits
    at the grid's lower edge `0.5`, and the null `LR` median. Both come from arrays §3.4 already
    computes, and neither enters a constant. The first is what makes old G3 fail at short `tau`:
    with no confident prediction contradicted, the maximiser runs to the edge.
13. **"Two bounds" on "some `tau` fails".** The largest per-`tau` fraction is a lower bound.
    `1 − Π(1 − fraction)` is the value under independence across `tau`, and it is not an upper
    bound in general, since a member's label is shared across `tau`. Both are reported as §3.2
    names them.
14. **M1's seconds are kept out of the compared outputs.** §3.1 asks for "the evaluations,
    anchors and seconds" per `tau`, and §5.1 forbids a wall-clock time in the three compared
    files. The seconds are therefore in `tz12-host.json`, and §1.1 prints run 1's.
15. **V6's `git status` for the report path** was run before the report existed. An absent
    path prints nothing, so that half is vacuous at run time. The report's own separation is shown
    by contract §4.2's self-check (§5).
16. **The preflight's second read** came after `--emit`, 15,395 s after the first. A usage limit
    paused the session from about 12:25:31Z to about 16:12Z, the bounds taken from scratch-file
    modification times. Nothing ran during the pause. Every build, emit and run step came after
    it.
17. **§9's "which that tree does not already hold by hash"** is read against
    `/root/btc-forensics/` as it stood when the copy step began. TZ-11a applied the same reading to
    `/root/tz10b-work/`. Both runs' identical outputs are therefore copied, which is §0's "TZ-11a's
    six run outputs, `12,038,440` bytes together".
18. **One commit, never amended.** `6dc0e24ae1542f98789967bf48057268731a2030` was made once, after `--emit` and a smoke of
    `constants` on synthetic rows, and before any `--out` pass. Both full runs are of it, and it
    is the commit that was pushed. No `--out` pass ran on any other commit.
19. **§9 ran before this report was committed.** §9 lists "the report goes straight to `main`"
    before "then, in this order", while §8 puts §9 inside the report, and a committed report is
    never edited (contract §3.2). The branch, the pull request and the separation self-check came
    first. The copy, the three worktree removals and the two tree removals followed, in that
    order, each after the previous one succeeded. This report, which records all of them, was
    committed last. TZ-11a did the same.
20. **`P3` at `tau = 180` on test 2 is `998` of `2,000`, two replicates short of `0.5`.** At
    2,000 replicates, one Monte Carlo standard error at `P3 = 0.5` is `sqrt(0.25 / 2000)`, or
    `0.0112`. That is arithmetic on §3.4's fixed count, and it changes nothing. §4 is applied
    as written, the prediction row is reported as not holding, and `R_POWER` is not re-chosen
    after seeing the number.
21. **Two branches the map lists on `origin` are gone from it.** System Map §1, revision
    `2026-09-15-a`, lists `tz-11a-student-link` at `2746518` and `tz-09-disk-inventory` at `e45f38e`
    on `origin`, read by `git ls-remote` on 2026-09-15. At this report's assembly,
    `git ls-remote origin` prints neither.
    - Both still exist locally, at those commits.
    - This run made one branch push, `git push -u origin tz-12-sized-gate`, and ran no command
      that deletes a branch, locally or on the remote.
    - When the two remote branches went is not measured: no `ls-remote` of them was taken before
      this run's publication.
    - Both commits are reachable from `main`, because PR #12 and PR #10 merged them, so no commit
      is lost.
    
    The assembler asserts all of this: the remote heads, the two local heads, and both
    ancestries.
