# TZ-11a — the Student link and the domain it is priced on — REPORT

**Status: executed.** Every §0 gate passed. Test 2 was formed at run time and holds 400 members.
Every check TZ-11a §7 names was run. Both full runs completed with every instrument `assert`
holding, and their three deterministic outputs are byte-identical. **There is no verdict here:
§4's verdict is the Architect's.** Each gate row below is the instrument's comparison of one
reported number against §4's quoted threshold.

- **The three tables, measured on the fit set alone and frozen into `pfair.py`** (§3.2), at `tau`
  240 / 180 / 120 / 90 / 60 / 30 / 10:
  - `ADMIT`: 2.12324 / 2.14298 / 2.18062 / 2.16098 / 2.16725 / 2.15178 / 2.14530.
  - `LINK_NU`: 9.62070 / 13.7083 / 20.2258 / 16.0482 / 9.51490 / 4.79579 / 2.13489.
  - `LINK_SCALE`: 1.30678 / 1.36658 / 1.40748 / 1.37085 / 1.27997 / 1.08185 / 0.643873.
  
  All fourteen fitted values lie inside their search intervals.
- **What the domain rule admits** (M2): 280 of 400 on the fit set, by construction. On test 1 it
  admits **28 to 35 of 400** per `tau`, and on test 2 **231 to 237 of 400**.
- **The gate rows, per test set** (§2):
  - **Test 1:**
    - G1: 7 of 7.
    - G2: 0 failing bins, **of 0 eligible**. At 28 to 35 admissible checkpoints per `tau`, no bin
      reaches `tz06.BIN_MIN_N` = 20.
    - G3: 3 of 7, FAIL at `tau` 240, 180, 30 and 10.
    - G4: 3 of 7, FAIL at `tau` 120, 90, 60 and 30.
  - **Test 2:**
    - G1: 7 of 7.
    - G2: 0 failing of 24 eligible.
    - G3: 5 of 7, FAIL at `tau` 90 and 60.
    - G4: 7 of 7.
  - Two of test 1's gated `λ̂`, at `tau` 180 and 10, sit on the lower bound, `0.5`, of the
    committed search interval. That is the edge of the search, not an interior maximiser.
- **The pre-registered prediction** (§4.1):
  - G1 and G2 came out as predicted.
  - G3 and G4 did not. Test 1's G4 holds at `tau = 240` and fails at 120, 90, 60 and 30. Test 2's G4
    holds at all seven `tau`.
- **M5:** `T0 1789268400` is **not admissible** at `tau = 30`. Its `sigma_hat` is `0.689147`,
  against `ADMIT[30]` of `2.15178`. Under test 1's all-member `λ̂` of `0.767339`, its
  contribution is `-11.902827` at `λ̂` and `-10.653379` at 1.
- **Validation:**
  - V2: 140 of 140 both ways.
  - V3: 3 of 3 outputs byte-identical.
  - V4: 7 + 7 + 7 reproduced. The committed `λ̂` is reproduced to ten decimals, and the 50-member
    guard holds.
  - V5: 2 asserted, 1 reported.
  - V6: the diff has the shape §5.3 names.
  - V7: 116 of 116.
  - V8: 21 of 21.
  - V9: the capture was unchanged across both runs.
  - V12: recorded, not asserted.
- **Publication:** branch `tz-11a-student-link` at `274651805c765bb977c635d75fd1ebdb2c8f550a`, pull request https://github.com/seahomebatumi-ai/btc-5m-twap/pull/12, not
  merged. Anchor `A6` would move from `45b307b221d4` to `729f0bcdbee3`.

Nothing was written under `/var/lib/btc-recorder/`, and no `quotes.jsonl.gz` or `gamma.json` was
opened. The live recorder, pid `228592` on `4216c04`, was not signalled or restarted.

Executor model: **Opus** (`claude-opus-5`), as the TZ requires.

---

## 0. Fingerprint, host and every free-space read

The spec was read from `origin/main` = `72e709241092aa9b76e25ffc109a0106c3c23076`, fast-forwarded into the primary checkout
from `53f196f` on 2026-09-14. The map was last changed at `53f196f510a2e98cc1b403a8df497a8410e6821f`, and the TZ-11a file
arrived at `72e709241092aa9b76e25ffc109a0106c3c23076`. The host gate ran at 2026-09-14T18:26:09Z and the fingerprint check at
2026-09-14T20:35:46Z.

**Map revision required:** `2026-09-14-e`. **Read:** `2026-09-14-e`.

| anchor | required by TZ-11a §0 | read from map §0 | recomputed from the file |
|---|---|---|---|
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` | not recomputed — a Release asset, not on disk |
| `A2` — collector | `6c5089330629` | `6c5089330629` | `6c5089330629` |
| `A3` — phase | `0-complete / 1-answered-no / 2-not-started` | `0-complete / 1-answered-no / 2-not-started` | — a string |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b` | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` | `9fd1c7de0f74` | `9fd1c7de0f74` |
| `A6` — pricer | `45b307b221d4` | `45b307b221d4` | `45b307b221d4` |

**6 of 6 anchors match.** `A1` is a Release asset and is not on disk.

### Fingerprint table

Every row of the map's §0 table, computed on `main` at `72e7092`. Lines are `wc -l` and bytes are
`wc -c`. The scratch script `/root/tz11a-work/gate-check.py` parsed the map's own table, compared
each row, and asserted the frozen count, the tracked count, the revision string and the six
anchors. This report's assembler recomputed all 20 rows on `main` again at assembly and asserted
each unchanged.

| path | lines | bytes | state | SHA-256 | matches map |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 569 | 84,446 | reported | `59ee3054d2e3ac2e1335b9e163a63e32ca8721e3dbf5bb4370c338066bcd72b6` | — |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | yes |
| `research/twap-divergence.py` | 1,135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | yes |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | yes |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | — (equal to the map) |
| `research/pfair.py` | 313 | 13,985 | frozen | `45b307b221d410a7812759a89941dc7645dfda165a8e01a60aef5b17851a5d1e` | yes |
| `research/selftest-pfair.py` | 441 | 22,643 | frozen | `7e641c93ea0244890f2726629b9f28a76d8f078b43da47e9cd9a16dbb43f223a` | yes |
| `research/tz06-calibration.py` | 577 | 27,138 | frozen | `715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f` | yes |
| `research/tz07a-variance-time.py` | 619 | 28,219 | frozen | `4321637751a3b847fa7e59309555b802dcc9d5ba68c7407a8ec20ab76c1b3d5e` | yes |
| `research/tz07b-settlement-dispersion.py` | 515 | 24,926 | frozen | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` | yes |
| `research/tz08a-out-of-sample.py` | 745 | 38,822 | frozen | `37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c` | yes |
| `research/tz09-disk-inventory.py` | 894 | 41,004 | frozen | `b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6` | yes |
| `research/tz10b-sigma-or-link.py` | 1,224 | 61,018 | frozen | `406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088` | yes |
| `research/recorder/recorder.py` | 608 | 25,658 | frozen | `9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03` | yes |
| `research/recorder/config.py` | 112 | 4,773 | frozen | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | yes |
| `research/recorder/manifest.py` | 254 | 10,002 | frozen | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | yes |
| `research/recorder/analyze.py` | 813 | 34,705 | frozen | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` | yes |
| `research/recorder/probe.py` | 227 | 9,324 | frozen | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | yes |
| `research/recorder/selftest.py` | 573 | 30,591 | frozen | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` | yes |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | — (equal to the map) |

**17 of 17 `frozen` rows match on lines, bytes and SHA-256, and 2 of 2 `tracked` rows equal the map.**

TZ-11a §2 authorizes three `frozen` rows to move and adds one file. On branch
`tz-11a-student-link` they read:

| path, on branch `tz-11a-student-link` | lines | bytes | SHA-256 |
|---|---|---|---|
| `research/pfair.py` | 441 | 19,357 | `729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68` |
| `research/selftest-pfair.py` | 619 | 32,559 | `b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa` |
| `research/tz07a-variance-time.py` | 623 | 28,414 | `513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771` |
| `research/tz11a-student-link.py` | 1,231 | 64,732 | `0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839` |

**`A6` before this TZ: `45b307b221d4`. After, on the branch: `729f0bcdbee3`.** The map is the
Architect's to revise; this report only states the value.

The TZ file:

| path | lines | bytes | SHA-256 |
|---|---|---|---|
| `CryptoTZ/TZ-11a-student-link-and-domain.md` | 655 | 42,064 | `dcd05f165d9057326a930814649cf81c9033980f6fb354cde8dd1fd15628c076` |

### Worktree hygiene — a disclosure, not a gate

At the host gate, `git worktree list --porcelain` printed four worktrees to the terminal: the
primary checkout on `main` at `72e7092`, `/root/tz09-work/wt`, `/root/tz09-work/wt-report` and
`/root/tz10b-work/wt`. That listing was not saved to a file. The run then added
`/root/tz11a-work/wt` on a new branch, `tz-11a-student-link`, at `72e7092`, and built everything
in it. The listing saved at 2026-09-14T20:57:42Z, after that addition and before the commit was amended
(§6 item 19), verbatim:

```
worktree /root/btc-5m-twap
HEAD 72e709241092aa9b76e25ffc109a0106c3c23076
branch refs/heads/main

worktree /root/tz09-work/wt
HEAD e45f38e89b5ee18e64a16a654b341d74fadcac26
branch refs/heads/tz-09-disk-inventory

worktree /root/tz09-work/wt-report
HEAD 33483975ca7fd1a1d6778e66c1ea94ab4e28c82f
detached

worktree /root/tz10b-work/wt
HEAD d34606ee9a592e51293eaad0996c7cae3b84dfcd
branch refs/heads/tz-10b-sigma-or-link

worktree /root/tz11a-work/wt
HEAD 4f481f133f011e316e3f724383f8df9dd9272469
branch refs/heads/tz-11a-student-link
```

The primary checkout `/root/btc-5m-twap` stayed on `main` for the whole run. The recorder runs
from it.

### Host gate and resource floor

| check | required | observed |
|---|---|---|
| `/var/lib/btc-recorder/btc-updown-5m/` exists and holds interval directories | yes | yes: 1,256 directories at the host gate, `1789033800` to `1789410300` |
| recorder running; newest `runtime.jsonl` start record sha | `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` | pid `228592`, `/root/tz04a-env/venv/bin/python -B -u recorder.py`, started Sat Sep 12 09:53:04 2026. The newest start record is `recv_ns` `1789206785264516934`, sha `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` |
| filesystem | `/dev/vda2`, total `31,612,203,008` bytes | `/dev/vda2`, total `31,612,203,008` bytes |
| free space at run start | at least `2,060,000,000` bytes | `14,315,757,568` bytes at 2026-09-14T18:25:45Z (§0 preflight read 1) |

**All three host checks pass, and so does the floor.**

### Every read of free space in the run

TZ-11a §0 requires the first to be at least `2,060,000,000` bytes and every later one at least
`2,000,000,000`.

| UTC | free bytes on `/dev/vda2` | read by | bound | at or above it |
|---|---|---|---|---|
| 2026-09-14T18:25:45Z | 14,315,757,568 | §0 preflight read 1 (`df`) | 2,060,000,000 | yes — recorded, not asserted |
| 2026-09-14T18:26:09Z | 14,315,511,808 | host gate (`df`) | 2,000,000,000 | yes — recorded, not asserted |
| 2026-09-14T20:36:02Z | 14,302,855,168 | §0 preflight read 2 (`df`) | 2,000,000,000 | yes — recorded, not asserted |
| 2026-09-14T23:29:01Z | 14,288,502,784 | full run 1, run start (`os.statvfs`) | 2,060,000,000 | yes — asserted |
| 2026-09-14T23:30:39Z | 14,288,683,008 | full run 1, after the walk (`os.statvfs`) | 2,000,000,000 | yes — asserted |
| 2026-09-14T23:33:30Z | 14,288,232,448 | full run 1, run end (`os.statvfs`) | 2,000,000,000 | yes — asserted |
| 2026-09-14T23:33:56Z | 14,282,534,912 | full run 2, run start (`os.statvfs`) | 2,060,000,000 | yes — asserted |
| 2026-09-14T23:35:34Z | 14,282,735,616 | full run 2, after the walk (`os.statvfs`) | 2,000,000,000 | yes — asserted |
| 2026-09-14T23:38:23Z | 14,282,285,056 | full run 2, run end (`os.statvfs`) | 2,000,000,000 | yes — asserted |
| 2026-09-15T05:06:00Z | 14,264,078,336 | this report's assembler (`os.statvfs`) | 2,000,000,000 | yes — asserted |

10 reads in all. 7 are asserted by a Python `assert` that aborts below the bound; the other 3 were compared by reading them, so they are **recorded, not asserted**. An `os.statvfs` read is `f_bavail · f_frsize`, the quantity `df -B1` prints as `Avail`. The smoke runs of §6 also asserted the floor, and their reads were not kept.

### The §0 preflight — recorded, and gating nothing beyond the floor

§0 asks for `df -B1 /dev/vda2`, `du -x -B1 -s /root/PROJECT_GAMING_PS5` and
`systemctl is-enabled` / `is-active telemetry-watch.service`, taken at run start and again at
least `1,800` s later, each captured with its exit status. Both reads were taken and are reported
as read. No file of that project was opened: `du` reads sizes only.

| read | taken (UTC) | free bytes on `/dev/vda2` | `du` of `/root/PROJECT_GAMING_PS5` (bytes) | `is-enabled` (exit) | `is-active` (exit) |
|---|---|---|---|---|---|
| 1 | 2026-09-14T18:25:45Z | 14,315,757,568 | 355,405,824 | `disabled` (1) | `inactive` (3) |
| 2 | 2026-09-14T20:36:02Z | 14,302,855,168 | 356,073,472 | `disabled` (1) | `inactive` (3) |

The two reads are **7,817 s** apart, more than the `1,800` s asked for: a usage limit paused the
session between them (§6).

- **Free space:** it changed by `-12,902,400` bytes, **`-142,608,080` bytes/day** at that rate.
- **`PROJECT_GAMING_PS5`:** it changed by `+667,648` bytes, **`+7,379,402` bytes/day**.
- **`telemetry-watch.service`:** `disabled` (exit 1) and `inactive` (exit 3) at both reads.

**This run's own footprint, stated separately** (System Map §7 item 29): `/root/tz11a-work` held
`8,192` bytes on disk at read 1 and `24,576` at read 2, and the session store
`/root/.claude` `109,555,712` and `109,744,128`. Both are inside the free-space figure. At
assembly `/root/tz11a-work` held `19,210,240` bytes. This is arithmetic on two reads; it applies
no rule from TZ-09 and gates nothing.

---

## 1. The measurements, in §3's order, per set before pooled

### 1.0 The three sets

- fit (TZ-06 400): 443 units considered (1789033800 … 1789166400), 400 members (1789035000 … 1789166400), 43 non-members (disconnect: 41, disconnect + no chainlink at or before T0-300: 2); member list `6d94a346a47a04a1a0849968effd9023d7585fe628b304ba2ae7a15953ee67f9`
- test 1 (TZ-08a 400): 433 units considered (1789166700 … 1789296300), 400 members (1789166700 … 1789296300), 33 non-members (disconnect: 33); member list `3b17729c050e5fbf8fed1bd0877d5dd5c229370609cd672c84eeed1ddc3d5762`
- test 2 (first 400 after 1789296300): 438 units considered (1789296600 … 1789427700), 400 members (1789296900 … 1789427700), 38 non-members (disconnect: 38); member list `2dd0fcc4dc2cf379e08c21a4524c3eab799aad7bff3136c37e32910cecb8fa70`

- **The fit set** is TZ-06's 400. `tz06.scoring_set` formed it at its defaults.
- **Test 1** is TZ-08a's 400, formed by `tz08a.the_set` with every assertion that function makes.
- **Test 2** did not exist when the TZ was written. It was formed at run time by
  `tz06.scoring_set(manifests, need=400, after=1789296300)`.
  - It considered 438 grid slots and admitted 400 members. Its last member is
    `1789427700`.
  - The 38 non-members all fail on `disconnect`, a condition read from the manifest, which
    does not change once written.
  - Its member-list SHA-256 is `2dd0fcc4dc2cf379e08c21a4524c3eab799aad7bff3136c37e32910cecb8fa70`, computed by `tz07b.member_list_sha`: the sorted
    `T0` list as decimal ASCII, joined by newlines, with no trailing newline. It is reported, not
    asserted. §3.0 names no expected value for it.

The two committed hashes are asserted equal to §3.0's values. The three sets are asserted pairwise
disjoint: three asserts. Every unit each walk considered is disclosed in V11.

Before the run, a scratch probe watched test 2 fill. It called `tz06.scoring_set` unmodified and
carried out counts only, as the table shows. The run started once the 400th member had qualified.
That member's directory was last written at 23:25:03Z, and run 1 started at 23:28:35Z. V9's
read-set hash confirms that no file in any directory the run reads changed during either run.

| probe (UTC) | test-2 members |
|---|---|
| 2026-09-14T20:40:18Z | 370 |
| 2026-09-14T20:55:37Z | 372 |
| 2026-09-14T20:56:17Z | 372 |
| 2026-09-14T21:06:23Z | 374 |
| 2026-09-14T21:16:30Z | 376 |
| 2026-09-14T21:26:35Z | 379 |
| 2026-09-14T21:36:41Z | 381 |
| 2026-09-14T21:46:48Z | 383 |
| 2026-09-14T21:56:54Z | 384 |
| 2026-09-14T22:06:59Z | 385 |
| 2026-09-14T22:17:06Z | 387 |
| 2026-09-14T22:27:12Z | 390 |
| 2026-09-14T22:37:18Z | 392 |
| 2026-09-14T22:47:24Z | 393 |
| 2026-09-14T22:57:30Z | 394 |
| 2026-09-14T23:07:36Z | 396 |
| 2026-09-14T23:17:42Z | 398 |
| 2026-09-14T23:27:49Z | 400 |

### 1.1 M1 — the link, fitted on the fit set, with no label

`r(a, tau) = Y(a, tau) / (sigma · sqrt(H(tau)))` at every admissible anchor, walked exactly as
`tz07b.member_r` walks it, each Decimal `r` converted to a float once, in ascending `T0` then
ascending anchor, into one `numpy.float64` array per population and `tau`. A symmetric Student's
`t` is fitted by maximum likelihood: `ν` over `[2.05, 60.0]` by golden section to a relative
tolerance of `1e-8`, and at each `ν` the scale `s` over `[0.10, 10.0]` by golden section to the
same tolerance. "Search edge" says whether `ν̂` or `ŝ` sits on a bound of its interval; the best
normal is the zero-mean normal at the root mean square of `r` (§6). `κ` is TZ-10b's, computed by
`tz10b.shape`: the uncentred root mean square over `MAD / 0.674490`. No label is read.

**Fit (TZ-06 400), all members.**

| tau | members | anchors | `ν̂` | `ŝ` | search edge | `ll` at optimum | `ll`, best normal | normal scale | **`κ`** | `log(ν̂ / LINK_NU)` | evaluations |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 240 | 400 | 143255 | 10.936829 | 1.368423 | interior | -261581.819 | -263606.292 | 1.523760 | **1.0467** | +0.1282 | 2070 |
| 180 | 400 | 167255 | 14.029509 | 1.383146 | interior | -303699.084 | -304696.566 | 1.496023 | **1.0336** | +0.0232 | 2070 |
| 120 | 400 | 191343 | 16.079077 | 1.399169 | interior | -347849.148 | -348611.341 | 1.496277 | **1.0566** | -0.2294 | 2024 |
| 90 | 400 | 203416 | 11.738856 | 1.347463 | interior | -366973.725 | -368266.159 | 1.479154 | **1.0984** | -0.3127 | 2070 |
| 60 | 400 | 215620 | 7.249717 | 1.236313 | interior | -382358.470 | -385272.218 | 1.444658 | **1.1566** | -0.2719 | 2116 |
| 30 | 400 | 227920 | 3.775771 | 0.997621 | interior | -386463.412 | -397770.611 | 1.385806 | **1.3209** | -0.2391 | 2202 |
| 10 | 400 | 236125 | 2.050000 | 0.569972 | nu at 2.05 | -335679.762 | -380286.473 | 1.211176 | **1.9460** | -0.0406 | 2341 |

**Fit (TZ-06 400), admissible members.**

| tau | members | anchors | `ν̂` | `ŝ` | search edge | `ll` at optimum | `ll`, best normal | normal scale | **`κ`** | `log(ν̂ / LINK_NU)` | evaluations |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 240 | 280 | 100605 | 9.620697 | 1.306781 | interior | -180379.824 | -182482.621 | 1.484256 | **1.0559** | -0.0000 | 2116 |
| 180 | 280 | 117405 | 13.708283 | 1.366580 | interior | -211970.209 | -212707.493 | 1.481126 | **1.0320** | -0.0000 | 2070 |
| 120 | 280 | 134265 | 20.225838 | 1.407477 | interior | -243122.942 | -243382.392 | 1.482549 | **1.0403** | +0.0000 | 2024 |
| 90 | 280 | 142695 | 16.048243 | 1.370851 | interior | -256510.146 | -256886.455 | 1.464201 | **1.0801** | +0.0000 | 2024 |
| 60 | 280 | 151164 | 9.514899 | 1.279971 | interior | -268078.934 | -269260.350 | 1.436641 | **1.1223** | -0.0000 | 2116 |
| 30 | 280 | 159684 | 4.795792 | 1.081847 | interior | -273916.630 | -279628.899 | 1.394032 | **1.2385** | +0.0000 | 2162 |
| 10 | 280 | 165369 | 2.134894 | 0.643873 | interior | -245467.279 | -267670.924 | 1.221024 | **1.6645** | +0.0000 | 2300 |

- **The Student `t` beats the best normal at every one of the 42 fits.** Its log-likelihood at the
  optimum exceeds the zero-mean normal's on the same anchors.
- **`κ` on the fit set** reads 1.0467 / 1.0336 / 1.0566 / 1.0984 / 1.1566 / 1.3209 / 1.9460 over all members, and 1.0559 / 1.0320 / 1.0403 / 1.0801 / 1.1223 / 1.2385 / 1.6645 over the
  admissible members, at `tau` 240 … 10.
- **`LINK_NU` and `LINK_SCALE` come from the admissible fit**, and every one is interior to its
  search interval. The all-member fit is reported beside them and is not frozen. Its `ν̂` at
  `tau = 10` sits on the lower edge of the search, `2.05`.

### 1.2 M2 — the domain, measured on the fit set

`ADMIT[tau]` is `statistics.quantiles(values, n=10, method="inclusive")[2]` over the 400 fit
members' `sigma_hat` at that `tau`: `pfair.realised_sigma` over `[T0 − 300, T0 + 300 − tau]`, the
pricer's own `sigma_live`, asserted equal at every observation. A member is admissible at `tau`
when its `sigma_hat` is at or above the committed six-digit literal. The counts on the two test
sets are what the rule costs there, measured.

| tau | `ADMIT` measured | six significant digits | `pfair.ADMIT` | admissible, fit | admissible, test 1 | admissible, test 2 |
|---|---|---|---|---|---|---|
| 240 | 2.123235637 | 2.12324 | 2.12324 | 280 of 400 | 35 of 400 | 231 of 400 |
| 180 | 2.142979535 | 2.14298 | 2.14298 | 280 of 400 | 29 of 400 | 237 of 400 |
| 120 | 2.180624456 | 2.18062 | 2.18062 | 280 of 400 | 28 of 400 | 233 of 400 |
| 90 | 2.160983936 | 2.16098 | 2.16098 | 280 of 400 | 28 of 400 | 234 of 400 |
| 60 | 2.167251322 | 2.16725 | 2.16725 | 280 of 400 | 28 of 400 | 233 of 400 |
| 30 | 2.151775167 | 2.15178 | 2.15178 | 280 of 400 | 28 of 400 | 235 of 400 |
| 10 | 2.145299155 | 2.14530 | 2.14530 | 280 of 400 | 30 of 400 | 235 of 400 |

- On the fit set the rule admits 280 of 400 at every `tau`, as a 30th percentile must.
- **On test 1 it admits 35 / 29 / 28 / 28 / 28 / 28 / 30 of 400** at `tau` 240 … 10. That excludes 91.2% to 93.0% of
  the set.
- **On test 2 it admits 231 / 237 / 233 / 234 / 233 / 235 / 235.** That excludes 40.8% to 42.2%.
- The rule and its threshold are the fit set's. What they cost on the test sets is measured here,
  not argued.

### 1.3 M3 — does the link transfer?

The identical search, refitted independently on each test set, all members and admissible members,
reading no label. `log(ν̂ / LINK_NU)` is taken against the frozen literal. Each population is its
own table; no pooled figure is computed.

**Test 1 (TZ-08a 400), all members.**

| tau | members | anchors | `ν̂` | `ŝ` | search edge | `ll` at optimum | `ll`, best normal | normal scale | **`κ`** | `log(ν̂ / LINK_NU)` | evaluations |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 240 | 400 | 142381 | 4.681313 | 1.184624 | interior | -257942.622 | -268383.948 | 1.593658 | **1.2140** | -0.7203 | 2162 |
| 180 | 400 | 166418 | 4.870300 | 1.140661 | interior | -293704.243 | -306333.926 | 1.524721 | **1.2818** | -1.0348 | 2162 |
| 120 | 400 | 190855 | 3.155750 | 0.942255 | interior | -323648.348 | -333656.012 | 1.389965 | **1.4218** | -1.8577 | 2250 |
| 90 | 400 | 203152 | 2.050000 | 0.718653 | nu at 2.05 | -329439.308 | -349352.809 | 1.350836 | **1.6900** | -2.0578 | 2298 |
| 60 | 400 | 215492 | 2.050000 | 0.585815 | nu at 2.05 | -322481.122 | -364818.101 | 1.315235 | **2.2510** | -1.5350 | 2338 |
| 30 | 400 | 227865 | 2.050000 | 0.404465 | nu at 2.05 | -287182.046 | -376942.742 | 1.265287 | **3.4565** | -0.8499 | 2344 |
| 10 | 400 | 236125 | 2.050000 | 0.225467 | nu at 2.05 | -181787.440 | -360183.796 | 1.112329 | **5.2803** | -0.0406 | 2430 |

**Test 1 (TZ-08a 400), admissible members.**

| tau | members | anchors | `ν̂` | `ŝ` | search edge | `ll` at optimum | `ll`, best normal | normal scale | **`κ`** | `log(ν̂ / LINK_NU)` | evaluations |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 240 | 35 | 12629 | 14.461092 | 0.972878 | interior | -18460.198 | -18514.711 | 1.048236 | **1.0688** | +0.4075 | 2115 |
| 180 | 29 | 12203 | 17.304545 | 1.066569 | interior | -18816.724 | -18860.975 | 1.135034 | **1.0131** | +0.2330 | 2024 |
| 120 | 28 | 13462 | 8.939429 | 1.124839 | interior | -22230.113 | -22396.717 | 1.277315 | **1.0457** | -0.8165 | 2116 |
| 90 | 28 | 14302 | 5.599950 | 1.017264 | interior | -23191.838 | -23525.371 | 1.253528 | **1.1607** | -1.0528 | 2202 |
| 60 | 28 | 15142 | 3.247500 | 0.863570 | interior | -24207.331 | -25067.180 | 1.266852 | **1.3560** | -1.0750 | 2251 |
| 30 | 28 | 15982 | 2.050000 | 0.577300 | nu at 2.05 | -23009.302 | -25779.116 | 1.214182 | **1.9268** | -0.8499 | 2340 |
| 10 | 30 | 17724 | 2.050000 | 0.305560 | nu at 2.05 | -18095.289 | -26729.672 | 1.093264 | **4.1781** | -0.0406 | 2389 |

**Test 2 (first 400 after 1789296300), all members.**

| tau | members | anchors | `ν̂` | `ŝ` | search edge | `ll` at optimum | `ll`, best normal | normal scale | **`κ`** | `log(ν̂ / LINK_NU)` | evaluations |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 240 | 400 | 143121 | 7.545790 | 1.443286 | interior | -275130.436 | -277593.169 | 1.683090 | **1.1017** | -0.2429 | 2116 |
| 180 | 400 | 167121 | 11.345608 | 1.440557 | interior | -313173.174 | -314338.654 | 1.587191 | **1.0570** | -0.1892 | 2070 |
| 120 | 400 | 191188 | 10.047361 | 1.382188 | interior | -352634.321 | -354371.970 | 1.544326 | **1.0915** | -0.6996 | 2070 |
| 90 | 400 | 203274 | 7.687341 | 1.315291 | interior | -371365.297 | -374182.422 | 1.524765 | **1.1262** | -0.7360 | 2116 |
| 60 | 400 | 215456 | 5.290317 | 1.181195 | interior | -383988.021 | -389288.608 | 1.473844 | **1.2154** | -0.5870 | 2162 |
| 30 | 400 | 227766 | 3.043193 | 0.924278 | interior | -384808.553 | -399868.598 | 1.400281 | **1.4161** | -0.4548 | 2250 |
| 10 | 400 | 236011 | 2.050000 | 0.538602 | nu at 2.05 | -327537.361 | -379368.262 | 1.207412 | **2.1142** | -0.0406 | 2342 |

**Test 2 (first 400 after 1789296300), admissible members.**

| tau | members | anchors | `ν̂` | `ŝ` | search edge | `ll` at optimum | `ll`, best normal | normal scale | **`κ`** | `log(ν̂ / LINK_NU)` | evaluations |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 240 | 231 | 82980 | 8.610653 | 1.390539 | interior | -154994.982 | -156198.064 | 1.589500 | **1.0968** | -0.1109 | 2116 |
| 180 | 237 | 99366 | 11.685348 | 1.391902 | interior | -182526.221 | -183226.234 | 1.529613 | **1.0466** | -0.1597 | 2070 |
| 120 | 233 | 111614 | 11.284539 | 1.396743 | interior | -205764.807 | -206593.499 | 1.540374 | **1.0689** | -0.5835 | 2070 |
| 90 | 234 | 119145 | 10.411407 | 1.366014 | interior | -217920.287 | -218770.880 | 1.517759 | **1.0788** | -0.4327 | 2070 |
| 60 | 233 | 125703 | 7.613244 | 1.270928 | interior | -225504.451 | -227145.022 | 1.474117 | **1.1270** | -0.2230 | 2116 |
| 30 | 235 | 133988 | 4.625274 | 1.083524 | interior | -231160.332 | -235737.939 | 1.405590 | **1.2443** | -0.0362 | 2162 |
| 10 | 235 | 138749 | 2.118037 | 0.642137 | interior | -206162.184 | -224219.174 | 1.217826 | **1.6803** | -0.0079 | 2300 |

**V12 item 2 — `ν̂` without its most influential member.** A member's influence is its own
contribution to the log-likelihood at `(ν̂, ŝ)`, summed over its anchors. One exact refit drops the
member with the largest contribution in magnitude, for each admissible population at each `tau`:
21 refits. Recorded, not asserted.

| population | tau | members | most influential T0 | its anchors | its contribution | `ν̂` | `ν̂` without | `ŝ` | `ŝ` without | search edge without |
|---|---|---|---|---|---|---|---|---|---|---|
| fit | 240 | 280 | 1789141800 | 346 | -2116.837 | 9.620697 | 14.562958 | 1.306781 | 1.334166 | interior |
| fit | 180 | 280 | 1789141800 | 406 | -1870.594 | 13.708283 | 20.782958 | 1.366580 | 1.387704 | interior |
| fit | 120 | 280 | 1789149600 | 481 | -1654.080 | 20.225838 | 27.761227 | 1.407477 | 1.418372 | interior |
| fit | 90 | 280 | 1789058700 | 511 | -1346.748 | 16.048243 | 15.875286 | 1.370851 | 1.365763 | interior |
| fit | 60 | 280 | 1789063500 | 541 | -1346.264 | 9.514899 | 9.684774 | 1.279971 | 1.279145 | interior |
| fit | 30 | 280 | 1789129500 | 571 | -1246.141 | 4.795792 | 4.875688 | 1.081847 | 1.084024 | interior |
| fit | 10 | 280 | 1789137600 | 591 | -1095.145 | 2.134894 | 2.127906 | 0.643873 | 0.641907 | interior |
| test1 | 240 | 35 | 1789292100 | 361 | -1324.565 | 14.461092 | 60.000000 | 0.972878 | 0.955674 | nu at 60 |
| test1 | 180 | 29 | 1789292100 | 421 | -1270.008 | 17.304545 | 60.000000 | 1.066569 | 1.050460 | nu at 60 |
| test1 | 120 | 28 | 1789292100 | 481 | -1270.536 | 8.939429 | 12.467871 | 1.124839 | 1.119097 | interior |
| test1 | 90 | 28 | 1789292100 | 511 | -1181.097 | 5.599950 | 5.957056 | 1.017264 | 1.002601 | interior |
| test1 | 60 | 28 | 1789288800 | 541 | -1171.374 | 3.247500 | 3.177479 | 0.863570 | 0.839085 | interior |
| test1 | 30 | 28 | 1789292100 | 571 | -1210.842 | 2.050000 | 2.050000 | 0.577300 | 0.557963 | nu at 2.05 |
| test1 | 10 | 30 | 1789292100 | 591 | -1177.896 | 2.050000 | 2.050000 | 0.305560 | 0.291295 | nu at 2.05 |
| test2 | 240 | 231 | 1789336800 | 361 | -1580.137 | 8.610653 | 9.822670 | 1.390539 | 1.395926 | interior |
| test2 | 180 | 237 | 1789402500 | 421 | -1645.295 | 11.685348 | 14.028271 | 1.391902 | 1.400022 | interior |
| test2 | 120 | 233 | 1789402500 | 481 | -1630.647 | 11.284539 | 14.129713 | 1.396743 | 1.413035 | interior |
| test2 | 90 | 234 | 1789313100 | 511 | -1416.983 | 10.411407 | 10.789298 | 1.366014 | 1.365227 | interior |
| test2 | 60 | 233 | 1789313100 | 541 | -1289.009 | 7.613244 | 7.695369 | 1.270928 | 1.269570 | interior |
| test2 | 30 | 235 | 1789395900 | 571 | -1241.294 | 4.625274 | 4.598802 | 1.083524 | 1.079985 | interior |
| test2 | 10 | 235 | 1789395900 | 591 | -1108.120 | 2.118037 | 2.109362 | 0.642137 | 0.639665 | interior |

- **`ν̂` over all members:**
  - fit: 10.94 / 14.03 / 16.08 / 11.74 / 7.25 / 3.776 / 2.05;
  - test 1: 4.681 / 4.87 / 3.156 / 2.05 / 2.05 / 2.05 / 2.05;
  - test 2: 7.546 / 11.35 / 10.05 / 7.687 / 5.29 / 3.043 / 2.05.
- **`ν̂` over admissible members:**
  - test 1: 14.46 / 17.3 / 8.939 / 5.6 / 3.247 / 2.05 / 2.05;
  - test 2: 8.611 / 11.69 / 11.28 / 10.41 / 7.613 / 4.625 / 2.118.
- **The log ratio against `LINK_NU`, over all members:** it lies beyond `log 2` at
  6 of 7 `tau` on test 1 and at 2 of 7 on test 2.
- **`κ` per population**, at `tau` 240 … 10:
  - test 1: 1.2140 / 1.2818 / 1.4218 / 1.6900 / 2.2510 / 3.4565 / 5.2803 over all members, and 1.0688 / 1.0131 / 1.0457 / 1.1607 / 1.3560 / 1.9268 / 4.1781 over the admissible ones;
  - test 2: 1.1017 / 1.0570 / 1.0915 / 1.1262 / 1.2154 / 1.4161 / 2.1142 over all members, and 1.0968 / 1.0466 / 1.0689 / 1.0788 / 1.1270 / 1.2443 / 1.6803 over the admissible ones.
- **8 of the 42 primary fits put `ν̂` on the lower edge of the search, `2.05`:**
  fit, all members, at `tau` 10; test 1, all members, at `tau` 90, 60, 30 and 10; test 1, admissible members, at `tau` 30 and 10; test 2, all members, at `tau` 10. Each such value is the edge of the search, not a maximiser. No `ŝ` sits on an edge.
- **Test 1's admissible populations are small:** 28 to 35 members, 12,203 to 17,724 anchors.
  - One member, `1789292100`, is the most influential in 6 of its 7.
  - Refitted without it, `ν̂` moves to the upper edge, `60`, at `tau` 240 and 180.
  - The influence refits that land on a search edge are, in all, 4: test 1 at `tau = 240` (`ν̂` without 60.000000); test 1 at `tau = 180` (`ν̂` without 60.000000); test 1 at `tau = 30` (`ν̂` without 2.050000); test 1 at `tau = 10` (`ν̂` without 2.050000).

### 1.4 M4 — the scoring, and a place a label is read

At the checkpoint of every member of test 1 and of test 2, `sd_t = pfair.student_sd(tau,
sigma_hat)` and `p_t = pfair.p_fair_student(state, sd_t, tau)`. `Brier(p_fair)` is the committed
link, `pfair.p_fair` with `pfair.corrected_sd`, on the identical rows. The bin table is
`tz06.table_for`, unmodified. `λ̂` is `tz07a.lambda_hat` with `log_cdf` bound to
`pfair.log_t_cdf` at `LINK_NU[tau]`. Beside it is the observation whose own contribution to
`ll(λ̂) − ll(1)` is largest in magnitude, and `λ̂` refitted without it (V12 item 1, recorded, not
asserted). `κ` is taken over the checkpoint rows' `r / LINK_SCALE[tau]`. The all-member blocks are
reported and not gated.

#### test 1 (TZ-08a 400), admissible checkpoints

| tau | n | `Brier(p_t)` | `Brier(p_fair)`, `corrected_sd` | eligible bins | failing bins | `κ` of `r / LINK_SCALE` | rows with no checkpoint `r` | saturated `p_t` | saturated `p_fair` |
|---|---|---|---|---|---|---|---|---|---|
| 240 | 35 | 0.207596 | 0.208455 | 0 | 0 | 1.3059 | 0 | 0 | 0 |
| 180 | 29 | 0.139315 | 0.141602 | 0 | 0 | 0.9505 | 0 | 0 | 0 |
| 120 | 28 | 0.164591 | 0.164570 | 0 | 0 | 0.9543 | 0 | 0 | 0 |
| 90 | 28 | 0.126241 | 0.127557 | 0 | 0 | 1.8990 | 0 | 0 | 0 |
| 60 | 28 | 0.079479 | 0.081538 | 0 | 0 | 1.2429 | 0 | 0 | 0 |
| 30 | 28 | 0.034513 | 0.035279 | 0 | 0 | 1.0087 | 0 | 0 | 11 |
| 10 | 30 | 0.000006 | 0.000000 | 0 | 0 | 3.3230 | 0 | 0 | 22 |

`λ̂` under the Student likelihood at `LINK_NU[tau]`:

| tau | n | `λ̂` | `ll(λ̂)` | `ll(1)` | LR | p | most influential (T0, label, z) | its contribution | `λ̂` without it | shift |
|---|---|---|---|---|---|---|---|---|---|---|
| 240 | 35 | 0.798944 | -20.807442 | -20.916134 | 0.217385 | 0.64104 | 1789182600, 0, 0.6689 | -0.2056 | 0.638074 | -0.160870 |
| 180 | 29 | 0.500000 | -11.212538 | -12.689625 | 2.954174 | 0.0856561 | 1789182600, 0, 0.6360 | -0.8687 | 0.500000 | +0.000000 |
| 120 | 28 | 0.989133 | -13.757892 | -13.758316 | 0.000849 | 0.976759 | 1789190700, 0, 1.0066 | -0.0159 | 0.783089 | -0.206044 |
| 90 | 28 | 1.080903 | -11.608285 | -11.633860 | 0.051149 | 0.821075 | 1789227300, 1, -1.5443 | +0.1932 | 0.731603 | -0.349300 |
| 60 | 28 | 1.146360 | -8.076115 | -8.131594 | 0.110958 | 0.739056 | 1789227300, 1, -2.1750 | +0.4568 | 0.500000 | -0.646360 |
| 30 | 28 | 0.605213 | -2.827868 | -3.090454 | 0.525171 | 0.468644 | 1789167900, 1, -0.3113 | -0.1992 | 0.500000 | -0.105213 |
| 10 | 30 | 0.500000 | -0.008349 | -0.036140 | 0.055582 | 0.81362 | 1789190100, 0, -6.9042 | +0.0066 | 0.500000 | +0.000000 |

##### test 1 (TZ-08a 400), admissible, tau = 240 — `p_t`

n = 35 · observed Up rate 0.5143 · Brier 0.207596

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| 0.0–0.1 | 0 | — | 0 | — | no | — |
| 0.1–0.2 | 2 | 0.1651 | 0 | — | no | — |
| 0.2–0.3 | 3 | 0.2373 | 0 | — | no | — |
| 0.3–0.4 | 6 | 0.3569 | 2 | — | no | — |
| 0.4–0.5 | 8 | 0.4516 | 4 | — | no | — |
| 0.5–0.6 | 7 | 0.5481 | 6 | — | no | — |
| 0.6–0.7 | 4 | 0.6475 | 3 | — | no | — |
| 0.7–0.8 | 4 | 0.7469 | 2 | — | no | — |
| 0.8–0.9 | 0 | — | 0 | — | no | — |
| 0.9–1.0 | 1 | 0.9517 | 1 | — | no | — |

##### test 1 (TZ-08a 400), admissible, tau = 180 — `p_t`

n = 29 · observed Up rate 0.5517 · Brier 0.139315

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| 0.0–0.1 | 1 | 0.0727 | 0 | — | no | — |
| 0.1–0.2 | 3 | 0.1310 | 0 | — | no | — |
| 0.2–0.3 | 1 | 0.2470 | 0 | — | no | — |
| 0.3–0.4 | 6 | 0.3566 | 2 | — | no | — |
| 0.4–0.5 | 2 | 0.4290 | 0 | — | no | — |
| 0.5–0.6 | 3 | 0.5455 | 3 | — | no | — |
| 0.6–0.7 | 5 | 0.6295 | 4 | — | no | — |
| 0.7–0.8 | 3 | 0.7398 | 2 | — | no | — |
| 0.8–0.9 | 3 | 0.8363 | 3 | — | no | — |
| 0.9–1.0 | 2 | 0.9589 | 2 | — | no | — |

##### test 1 (TZ-08a 400), admissible, tau = 120 — `p_t`

n = 28 · observed Up rate 0.5357 · Brier 0.164591

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| 0.0–0.1 | 3 | 0.0653 | 0 | — | no | — |
| 0.1–0.2 | 3 | 0.1419 | 1 | — | no | — |
| 0.2–0.3 | 4 | 0.2574 | 1 | — | no | — |
| 0.3–0.4 | 2 | 0.3410 | 1 | — | no | — |
| 0.4–0.5 | 3 | 0.4432 | 1 | — | no | — |
| 0.5–0.6 | 0 | — | 0 | — | no | — |
| 0.6–0.7 | 6 | 0.6513 | 5 | — | no | — |
| 0.7–0.8 | 1 | 0.7020 | 1 | — | no | — |
| 0.8–0.9 | 3 | 0.8389 | 2 | — | no | — |
| 0.9–1.0 | 3 | 0.9610 | 3 | — | no | — |

##### test 1 (TZ-08a 400), admissible, tau = 90 — `p_t`

n = 28 · observed Up rate 0.5000 · Brier 0.126241

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| 0.0–0.1 | 8 | 0.0412 | 1 | — | no | — |
| 0.1–0.2 | 2 | 0.1606 | 0 | — | no | — |
| 0.2–0.3 | 0 | — | 0 | — | no | — |
| 0.3–0.4 | 0 | — | 0 | — | no | — |
| 0.4–0.5 | 3 | 0.4517 | 0 | — | no | — |
| 0.5–0.6 | 3 | 0.5338 | 2 | — | no | — |
| 0.6–0.7 | 2 | 0.6750 | 2 | — | no | — |
| 0.7–0.8 | 4 | 0.7583 | 4 | — | no | — |
| 0.8–0.9 | 1 | 0.8645 | 1 | — | no | — |
| 0.9–1.0 | 5 | 0.9414 | 4 | — | no | — |

##### test 1 (TZ-08a 400), admissible, tau = 60 — `p_t`

n = 28 · observed Up rate 0.4643 · Brier 0.079479

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| 0.0–0.1 | 11 | 0.0176 | 1 | — | no | — |
| 0.1–0.2 | 1 | 0.1850 | 0 | — | no | — |
| 0.2–0.3 | 1 | 0.2312 | 0 | — | no | — |
| 0.3–0.4 | 1 | 0.3266 | 0 | — | no | — |
| 0.4–0.5 | 1 | 0.4191 | 0 | — | no | — |
| 0.5–0.6 | 2 | 0.5846 | 1 | — | no | — |
| 0.6–0.7 | 2 | 0.6139 | 2 | — | no | — |
| 0.7–0.8 | 0 | — | 0 | — | no | — |
| 0.8–0.9 | 2 | 0.8443 | 2 | — | no | — |
| 0.9–1.0 | 7 | 0.9730 | 7 | — | no | — |

##### test 1 (TZ-08a 400), admissible, tau = 30 — `p_t`

n = 28 · observed Up rate 0.5000 · Brier 0.034513

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| 0.0–0.1 | 12 | 0.0084 | 0 | — | no | — |
| 0.1–0.2 | 1 | 0.1382 | 0 | — | no | — |
| 0.2–0.3 | 1 | 0.2514 | 0 | — | no | — |
| 0.3–0.4 | 2 | 0.3904 | 2 | — | no | — |
| 0.4–0.5 | 0 | — | 0 | — | no | — |
| 0.5–0.6 | 0 | — | 0 | — | no | — |
| 0.6–0.7 | 1 | 0.6855 | 1 | — | no | — |
| 0.7–0.8 | 0 | — | 0 | — | no | — |
| 0.8–0.9 | 1 | 0.8363 | 1 | — | no | — |
| 0.9–1.0 | 10 | 0.9895 | 10 | — | no | — |

##### test 1 (TZ-08a 400), admissible, tau = 10 — `p_t` (printed, not pooled by G2)

n = 30 · observed Up rate 0.4667 · Brier 0.000006

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| 0.0–0.1 | 16 | 0.0008 | 0 | — | no | — |
| 0.1–0.2 | 0 | — | 0 | — | no | — |
| 0.2–0.3 | 0 | — | 0 | — | no | — |
| 0.3–0.4 | 0 | — | 0 | — | no | — |
| 0.4–0.5 | 0 | — | 0 | — | no | — |
| 0.5–0.6 | 0 | — | 0 | — | no | — |
| 0.6–0.7 | 0 | — | 0 | — | no | — |
| 0.7–0.8 | 0 | — | 0 | — | no | — |
| 0.8–0.9 | 0 | — | 0 | — | no | — |
| 0.9–1.0 | 14 | 0.9984 | 14 | — | no | — |

#### test 1 (TZ-08a 400), all checkpoints — reported, not gated

| tau | n | `Brier(p_t)` | `Brier(p_fair)`, `corrected_sd` | eligible bins | failing bins | `κ` of `r / LINK_SCALE` | rows with no checkpoint `r` | saturated `p_t` | saturated `p_fair` |
|---|---|---|---|---|---|---|---|---|---|
| 240 | 400 | 0.201606 | 0.202616 | 8 | 0 | 1.6067 | 0 | 0 | 0 |
| 180 | 400 | 0.185412 | 0.185387 | 10 | 0 | 1.6837 | 0 | 0 | 0 |
| 120 | 400 | 0.136137 | 0.136366 | 10 | 0 | 1.8385 | 0 | 0 | 0 |
| 90 | 400 | 0.102855 | 0.103550 | 8 | 0 | 2.1605 | 0 | 0 | 0 |
| 60 | 400 | 0.067238 | 0.068347 | 3 | 0 | 2.3228 | 0 | 0 | 8 |
| 30 | 400 | 0.020667 | 0.021643 | 2 | 0 | 3.9398 | 0 | 0 | 168 |
| 10 | 400 | 0.003912 | 0.003853 | 2 | 0 | 7.0929 | 0 | 0 | 342 |

`λ̂` under the Student likelihood at `LINK_NU[tau]`:

| tau | n | `λ̂` | `ll(λ̂)` | `ll(1)` | LR | p | most influential (T0, label, z) | its contribution | `λ̂` without it | shift |
|---|---|---|---|---|---|---|---|---|---|---|
| 240 | 400 | 0.930480 | -235.348933 | -235.494137 | 0.290408 | 0.589959 | 1789249500, 1, -1.8664 | -0.2282 | 0.878886 | -0.051594 |
| 180 | 400 | 1.188325 | -220.322943 | -221.659369 | 2.672852 | 0.102073 | 1789261200, 0, 2.1165 | +0.6031 | 1.142573 | -0.045752 |
| 120 | 400 | 1.040777 | -170.009434 | -170.098811 | 0.178753 | 0.672447 | 1789205700, 1, -2.6976 | +0.2305 | 0.987186 | -0.053591 |
| 90 | 400 | 1.008744 | -134.493555 | -134.497465 | 0.007819 | 0.929538 | 1789268400, 1, -2.3364 | +0.0400 | 0.963154 | -0.045591 |
| 60 | 400 | 1.154181 | -100.817312 | -101.560105 | 1.485587 | 0.222902 | 1789225800, 1, -4.2326 | +0.8874 | 1.058465 | -0.095716 |
| 30 | 400 | 0.767339 | -35.763489 | -36.480572 | 1.434168 | 0.231085 | 1789268400, 1, -13.8584 | -1.2494 | 0.599384 | -0.167955 |
| 10 | 400 | 0.755717 | -5.032639 | -5.192557 | 0.319835 | 0.571707 | 1789293300, 0, 0.8745 | -0.2638 | 0.512128 | -0.243589 |

##### test 1 (TZ-08a 400), all, tau = 240 — `p_t`

n = 400 · observed Up rate 0.5050 · Brier 0.201606

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| 0.0–0.1 | 14 | 0.0577 | 2 | — | no | — |
| 0.1–0.2 | 25 | 0.1527 | 0 | [0, 9] | yes | ok |
| 0.2–0.3 | 35 | 0.2444 | 9 | [3, 15] | yes | ok |
| 0.3–0.4 | 39 | 0.3552 | 10 | [7, 22] | yes | ok |
| 0.4–0.5 | 83 | 0.4586 | 37 | [27, 50] | yes | ok |
| 0.5–0.6 | 94 | 0.5447 | 59 | [39, 63] | yes | ok |
| 0.6–0.7 | 43 | 0.6448 | 34 | [19, 35] | yes | ok |
| 0.7–0.8 | 35 | 0.7474 | 24 | [19, 32] | yes | ok |
| 0.8–0.9 | 20 | 0.8373 | 16 | [12, 20] | yes | ok |
| 0.9–1.0 | 12 | 0.9274 | 11 | — | no | — |

##### test 1 (TZ-08a 400), all, tau = 180 — `p_t`

n = 400 · observed Up rate 0.5050 · Brier 0.185412

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| 0.0–0.1 | 38 | 0.0512 | 4 | [0, 6] | yes | ok |
| 0.1–0.2 | 42 | 0.1552 | 11 | [1, 13] | yes | ok |
| 0.2–0.3 | 26 | 0.2510 | 4 | [1, 13] | yes | ok |
| 0.3–0.4 | 36 | 0.3522 | 11 | [6, 20] | yes | ok |
| 0.4–0.5 | 46 | 0.4510 | 20 | [12, 29] | yes | ok |
| 0.5–0.6 | 53 | 0.5415 | 28 | [19, 38] | yes | ok |
| 0.6–0.7 | 45 | 0.6539 | 33 | [21, 37] | yes | ok |
| 0.7–0.8 | 41 | 0.7466 | 28 | [23, 37] | yes | ok |
| 0.8–0.9 | 39 | 0.8475 | 34 | [27, 38] | yes | ok |
| 0.9–1.0 | 34 | 0.9464 | 29 | [28, 34] | yes | ok |

##### test 1 (TZ-08a 400), all, tau = 120 — `p_t`

n = 400 · observed Up rate 0.5050 · Brier 0.136137

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| 0.0–0.1 | 81 | 0.0423 | 4 | [0, 9] | yes | ok |
| 0.1–0.2 | 33 | 0.1413 | 6 | [0, 10] | yes | ok |
| 0.2–0.3 | 22 | 0.2469 | 2 | [1, 11] | yes | ok |
| 0.3–0.4 | 25 | 0.3437 | 9 | [3, 15] | yes | ok |
| 0.4–0.5 | 43 | 0.4537 | 22 | [11, 28] | yes | ok |
| 0.5–0.6 | 31 | 0.5422 | 20 | [10, 24] | yes | ok |
| 0.6–0.7 | 33 | 0.6445 | 21 | [14, 28] | yes | ok |
| 0.7–0.8 | 22 | 0.7295 | 16 | [10, 21] | yes | ok |
| 0.8–0.9 | 41 | 0.8557 | 36 | [29, 40] | yes | ok |
| 0.9–1.0 | 69 | 0.9610 | 66 | [61, 69] | yes | ok |

##### test 1 (TZ-08a 400), all, tau = 90 — `p_t`

n = 400 · observed Up rate 0.5050 · Brier 0.102855

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| 0.0–0.1 | 111 | 0.0281 | 5 | [0, 8] | yes | ok |
| 0.1–0.2 | 23 | 0.1485 | 2 | [0, 8] | yes | ok |
| 0.2–0.3 | 18 | 0.2536 | 3 | — | no | — |
| 0.3–0.4 | 14 | 0.3603 | 4 | — | no | — |
| 0.4–0.5 | 27 | 0.4554 | 10 | [6, 19] | yes | ok |
| 0.5–0.6 | 32 | 0.5482 | 23 | [10, 25] | yes | ok |
| 0.6–0.7 | 32 | 0.6470 | 20 | [14, 27] | yes | ok |
| 0.7–0.8 | 21 | 0.7500 | 19 | [10, 20] | yes | ok |
| 0.8–0.9 | 23 | 0.8582 | 22 | [15, 23] | yes | ok |
| 0.9–1.0 | 99 | 0.9715 | 94 | [91, 99] | yes | ok |

##### test 1 (TZ-08a 400), all, tau = 60 — `p_t`

n = 400 · observed Up rate 0.5050 · Brier 0.067238

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| 0.0–0.1 | 137 | 0.0128 | 5 | [0, 6] | yes | ok |
| 0.1–0.2 | 18 | 0.1506 | 1 | — | no | — |
| 0.2–0.3 | 16 | 0.2436 | 1 | — | no | — |
| 0.3–0.4 | 12 | 0.3609 | 4 | — | no | — |
| 0.4–0.5 | 14 | 0.4525 | 3 | — | no | — |
| 0.5–0.6 | 15 | 0.5473 | 11 | — | no | — |
| 0.6–0.7 | 18 | 0.6492 | 14 | — | no | — |
| 0.7–0.8 | 16 | 0.7412 | 13 | — | no | — |
| 0.8–0.9 | 22 | 0.8505 | 21 | [14, 22] | yes | ok |
| 0.9–1.0 | 132 | 0.9840 | 129 | [125, 132] | yes | ok |

##### test 1 (TZ-08a 400), all, tau = 30 — `p_t`

n = 400 · observed Up rate 0.5050 · Brier 0.020667

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| 0.0–0.1 | 172 | 0.0062 | 1 | [0, 4] | yes | ok |
| 0.1–0.2 | 10 | 0.1463 | 1 | — | no | — |
| 0.2–0.3 | 4 | 0.2577 | 0 | — | no | — |
| 0.3–0.4 | 7 | 0.3532 | 2 | — | no | — |
| 0.4–0.5 | 4 | 0.4308 | 0 | — | no | — |
| 0.5–0.6 | 4 | 0.5482 | 1 | — | no | — |
| 0.6–0.7 | 5 | 0.6475 | 5 | — | no | — |
| 0.7–0.8 | 5 | 0.7510 | 5 | — | no | — |
| 0.8–0.9 | 8 | 0.8453 | 7 | — | no | — |
| 0.9–1.0 | 181 | 0.9910 | 180 | [175, 181] | yes | ok |

##### test 1 (TZ-08a 400), all, tau = 10 — `p_t` (printed, not pooled by G2)

n = 400 · observed Up rate 0.5050 · Brier 0.003912

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| 0.0–0.1 | 194 | 0.0025 | 0 | [0, 3] | yes | ok |
| 0.1–0.2 | 1 | 0.1460 | 0 | — | no | — |
| 0.2–0.3 | 1 | 0.2042 | 0 | — | no | — |
| 0.3–0.4 | 0 | — | 0 | — | no | — |
| 0.4–0.5 | 1 | 0.4895 | 1 | — | no | — |
| 0.5–0.6 | 0 | — | 0 | — | no | — |
| 0.6–0.7 | 2 | 0.6913 | 1 | — | no | — |
| 0.7–0.8 | 2 | 0.7776 | 1 | — | no | — |
| 0.8–0.9 | 0 | — | 0 | — | no | — |
| 0.9–1.0 | 199 | 0.9982 | 199 | [196, 199] | yes | ok |

#### test 2 (first 400 after 1789296300), admissible checkpoints

| tau | n | `Brier(p_t)` | `Brier(p_fair)`, `corrected_sd` | eligible bins | failing bins | `κ` of `r / LINK_SCALE` | rows with no checkpoint `r` | saturated `p_t` | saturated `p_fair` |
|---|---|---|---|---|---|---|---|---|---|
| 240 | 231 | 0.192904 | 0.193272 | 5 | 0 | 1.2548 | 0 | 0 | 0 |
| 180 | 237 | 0.154989 | 0.155255 | 7 | 0 | 1.2432 | 0 | 0 | 0 |
| 120 | 233 | 0.113918 | 0.114066 | 5 | 0 | 1.1180 | 0 | 0 | 0 |
| 90 | 234 | 0.077851 | 0.078222 | 3 | 0 | 1.3215 | 0 | 0 | 0 |
| 60 | 233 | 0.037888 | 0.038377 | 2 | 0 | 1.1902 | 0 | 0 | 12 |
| 30 | 235 | 0.017575 | 0.017348 | 2 | 0 | 1.4946 | 0 | 0 | 110 |
| 10 | 235 | 0.003640 | 0.003532 | 2 | 0 | 1.5243 | 0 | 0 | 213 |

`λ̂` under the Student likelihood at `LINK_NU[tau]`:

| tau | n | `λ̂` | `ll(λ̂)` | `ll(1)` | LR | p | most influential (T0, label, z) | its contribution | `λ̂` without it | shift |
|---|---|---|---|---|---|---|---|---|---|---|
| 240 | 231 | 0.932553 | -129.787592 | -129.883317 | 0.191449 | 0.661713 | 1789348200, 0, 1.4021 | -0.1544 | 0.880505 | -0.052048 |
| 180 | 237 | 0.968834 | -111.584268 | -111.613361 | 0.058186 | 0.809387 | 1789366200, 0, 2.1976 | -0.1323 | 0.899018 | -0.069816 |
| 120 | 233 | 0.934540 | -82.552903 | -82.697740 | 0.289674 | 0.59043 | 1789338600, 1, -1.9094 | -0.2613 | 0.874845 | -0.059695 |
| 90 | 234 | 0.811435 | -56.815606 | -57.908764 | 2.186316 | 0.139242 | 1789375200, 0, 1.3630 | -0.5342 | 0.764473 | -0.046962 |
| 60 | 233 | 0.643500 | -26.852617 | -29.583835 | 5.462436 | 0.0194295 | 1789402200, 0, 1.1431 | -0.9598 | 0.572921 | -0.070579 |
| 30 | 235 | 1.074689 | -12.970777 | -13.003984 | 0.066414 | 0.796631 | 1789403700, 1, -1.8131 | +0.1596 | 0.874933 | -0.199757 |
| 10 | 235 | 1.131246 | -2.892073 | -2.909968 | 0.035790 | 0.849951 | 1789360500, 0, 1.7046 | +0.1684 | 0.500000 | -0.631246 |

##### test 2 (first 400 after 1789296300), admissible, tau = 240 — `p_t`

n = 231 · observed Up rate 0.4935 · Brier 0.192904

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| 0.0–0.1 | 8 | 0.0635 | 0 | — | no | — |
| 0.1–0.2 | 17 | 0.1604 | 1 | — | no | — |
| 0.2–0.3 | 28 | 0.2468 | 7 | [2, 13] | yes | ok |
| 0.3–0.4 | 36 | 0.3537 | 12 | [6, 20] | yes | ok |
| 0.4–0.5 | 33 | 0.4486 | 19 | [8, 22] | yes | ok |
| 0.5–0.6 | 29 | 0.5525 | 17 | [9, 23] | yes | ok |
| 0.6–0.7 | 37 | 0.6435 | 21 | [16, 31] | yes | ok |
| 0.7–0.8 | 16 | 0.7504 | 15 | — | no | — |
| 0.8–0.9 | 16 | 0.8524 | 12 | — | no | — |
| 0.9–1.0 | 11 | 0.9495 | 10 | — | no | — |

##### test 2 (first 400 after 1789296300), admissible, tau = 180 — `p_t`

n = 237 · observed Up rate 0.5021 · Brier 0.154989

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| 0.0–0.1 | 27 | 0.0470 | 1 | [0, 5] | yes | ok |
| 0.1–0.2 | 29 | 0.1508 | 3 | [0, 10] | yes | ok |
| 0.2–0.3 | 19 | 0.2523 | 6 | — | no | — |
| 0.3–0.4 | 28 | 0.3532 | 11 | [4, 17] | yes | ok |
| 0.4–0.5 | 24 | 0.4362 | 10 | [4, 17] | yes | ok |
| 0.5–0.6 | 15 | 0.5470 | 9 | — | no | — |
| 0.6–0.7 | 22 | 0.6563 | 15 | [9, 20] | yes | ok |
| 0.7–0.8 | 27 | 0.7521 | 21 | [14, 25] | yes | ok |
| 0.8–0.9 | 18 | 0.8596 | 17 | — | no | — |
| 0.9–1.0 | 28 | 0.9580 | 26 | [23, 28] | yes | ok |

##### test 2 (first 400 after 1789296300), admissible, tau = 120 — `p_t`

n = 233 · observed Up rate 0.5021 · Brier 0.113918

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| 0.0–0.1 | 49 | 0.0331 | 1 | [0, 6] | yes | ok |
| 0.1–0.2 | 25 | 0.1450 | 4 | [0, 9] | yes | ok |
| 0.2–0.3 | 20 | 0.2382 | 6 | [1, 10] | yes | ok |
| 0.3–0.4 | 7 | 0.3403 | 3 | — | no | — |
| 0.4–0.5 | 12 | 0.4606 | 4 | — | no | — |
| 0.5–0.6 | 16 | 0.5502 | 7 | — | no | — |
| 0.6–0.7 | 15 | 0.6386 | 10 | — | no | — |
| 0.7–0.8 | 25 | 0.7615 | 21 | [13, 24] | yes | ok |
| 0.8–0.9 | 19 | 0.8558 | 17 | — | no | — |
| 0.9–1.0 | 45 | 0.9791 | 44 | [41, 45] | yes | ok |

##### test 2 (first 400 after 1789296300), admissible, tau = 90 — `p_t`

n = 234 · observed Up rate 0.5000 · Brier 0.077851

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| 0.0–0.1 | 65 | 0.0251 | 0 | [0, 6] | yes | ok |
| 0.1–0.2 | 20 | 0.1348 | 4 | [0, 7] | yes | ok |
| 0.2–0.3 | 10 | 0.2599 | 1 | — | no | — |
| 0.3–0.4 | 13 | 0.3460 | 4 | — | no | — |
| 0.4–0.5 | 10 | 0.4426 | 3 | — | no | — |
| 0.5–0.6 | 7 | 0.5461 | 5 | — | no | — |
| 0.6–0.7 | 11 | 0.6584 | 8 | — | no | — |
| 0.7–0.8 | 14 | 0.7431 | 11 | — | no | — |
| 0.8–0.9 | 17 | 0.8417 | 15 | — | no | — |
| 0.9–1.0 | 67 | 0.9826 | 66 | [62, 67] | yes | ok |

##### test 2 (first 400 after 1789296300), admissible, tau = 60 — `p_t`

n = 233 · observed Up rate 0.5064 · Brier 0.037888

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| 0.0–0.1 | 87 | 0.0139 | 0 | [0, 5] | yes | ok |
| 0.1–0.2 | 10 | 0.1397 | 0 | — | no | — |
| 0.2–0.3 | 7 | 0.2450 | 1 | — | no | — |
| 0.3–0.4 | 5 | 0.3791 | 2 | — | no | — |
| 0.4–0.5 | 8 | 0.4688 | 5 | — | no | — |
| 0.5–0.6 | 2 | 0.5195 | 1 | — | no | — |
| 0.6–0.7 | 6 | 0.6408 | 3 | — | no | — |
| 0.7–0.8 | 6 | 0.7429 | 6 | — | no | — |
| 0.8–0.9 | 14 | 0.8510 | 12 | — | no | — |
| 0.9–1.0 | 88 | 0.9860 | 88 | [83, 88] | yes | ok |

##### test 2 (first 400 after 1789296300), admissible, tau = 30 — `p_t`

n = 235 · observed Up rate 0.5064 · Brier 0.017575

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| 0.0–0.1 | 112 | 0.0062 | 1 | [0, 4] | yes | ok |
| 0.1–0.2 | 1 | 0.1611 | 1 | — | no | — |
| 0.2–0.3 | 1 | 0.2484 | 0 | — | no | — |
| 0.3–0.4 | 1 | 0.3599 | 0 | — | no | — |
| 0.4–0.5 | 3 | 0.4678 | 2 | — | no | — |
| 0.5–0.6 | 0 | — | 0 | — | no | — |
| 0.6–0.7 | 2 | 0.6580 | 2 | — | no | — |
| 0.7–0.8 | 2 | 0.7401 | 1 | — | no | — |
| 0.8–0.9 | 3 | 0.8621 | 2 | — | no | — |
| 0.9–1.0 | 110 | 0.9955 | 110 | [107, 110] | yes | ok |

##### test 2 (first 400 after 1789296300), admissible, tau = 10 — `p_t` (printed, not pooled by G2)

n = 235 · observed Up rate 0.5106 · Brier 0.003640

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| 0.0–0.1 | 113 | 0.0006 | 0 | [0, 1] | yes | ok |
| 0.1–0.2 | 1 | 0.1043 | 0 | — | no | — |
| 0.2–0.3 | 0 | — | 0 | — | no | — |
| 0.3–0.4 | 0 | — | 0 | — | no | — |
| 0.4–0.5 | 0 | — | 0 | — | no | — |
| 0.5–0.6 | 0 | — | 0 | — | no | — |
| 0.6–0.7 | 0 | — | 0 | — | no | — |
| 0.7–0.8 | 0 | — | 0 | — | no | — |
| 0.8–0.9 | 4 | 0.8767 | 3 | — | no | — |
| 0.9–1.0 | 117 | 0.9989 | 117 | [115, 117] | yes | ok |

#### test 2 (first 400 after 1789296300), all checkpoints — reported, not gated

| tau | n | `Brier(p_t)` | `Brier(p_fair)`, `corrected_sd` | eligible bins | failing bins | `κ` of `r / LINK_SCALE` | rows with no checkpoint `r` | saturated `p_t` | saturated `p_fair` |
|---|---|---|---|---|---|---|---|---|---|
| 240 | 400 | 0.191923 | 0.192552 | 9 | 0 | 1.4198 | 0 | 0 | 0 |
| 180 | 400 | 0.151225 | 0.151598 | 10 | 0 | 1.3107 | 0 | 0 | 0 |
| 120 | 400 | 0.116998 | 0.117198 | 10 | 0 | 1.2727 | 0 | 0 | 0 |
| 90 | 400 | 0.079806 | 0.080331 | 6 | 0 | 1.4597 | 0 | 0 | 0 |
| 60 | 400 | 0.042425 | 0.042841 | 2 | 0 | 1.5140 | 0 | 0 | 26 |
| 30 | 400 | 0.014863 | 0.014984 | 2 | 0 | 1.9746 | 0 | 0 | 192 |
| 10 | 400 | 0.002485 | 0.002747 | 2 | 0 | 2.3577 | 0 | 0 | 365 |

`λ̂` under the Student likelihood at `LINK_NU[tau]`:

| tau | n | `λ̂` | `ll(λ̂)` | `ll(1)` | LR | p | most influential (T0, label, z) | its contribution | `λ̂` without it | shift |
|---|---|---|---|---|---|---|---|---|---|---|
| 240 | 400 | 0.922878 | -224.289365 | -224.505127 | 0.431523 | 0.511243 | 1789369200, 1, -1.6303 | -0.2166 | 0.886002 | -0.036876 |
| 180 | 400 | 0.921651 | -184.077502 | -184.403682 | 0.652359 | 0.41927 | 1789366200, 0, 2.1976 | -0.3517 | 0.880707 | -0.040944 |
| 120 | 400 | 1.074298 | -150.252131 | -150.545698 | 0.587135 | 0.443529 | 1789361700, 1, -3.0398 | +0.4722 | 1.012798 | -0.061500 |
| 90 | 400 | 0.979536 | -109.402154 | -109.423194 | 0.042081 | 0.837466 | 1789329600, 0, 3.5262 | -0.1558 | 0.903320 | -0.076216 |
| 60 | 400 | 0.883813 | -62.844452 | -63.298999 | 0.909093 | 0.340355 | 1789329600, 0, 6.0539 | -0.9741 | 0.767149 | -0.116663 |
| 30 | 400 | 1.107460 | -23.763059 | -23.858817 | 0.191516 | 0.661658 | 1789304100, 1, -6.7468 | +0.4457 | 0.856929 | -0.250530 |
| 10 | 400 | 0.764670 | -3.682217 | -3.782577 | 0.200719 | 0.654141 | 1789360500, 0, 1.7046 | -0.4107 | 0.500000 | -0.264670 |

##### test 2 (first 400 after 1789296300), all, tau = 240 — `p_t`

n = 400 · observed Up rate 0.5125 · Brier 0.191923

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| 0.0–0.1 | 12 | 0.0640 | 1 | — | no | — |
| 0.1–0.2 | 26 | 0.1537 | 2 | [0, 9] | yes | ok |
| 0.2–0.3 | 44 | 0.2516 | 12 | [4, 19] | yes | ok |
| 0.3–0.4 | 56 | 0.3532 | 17 | [11, 29] | yes | ok |
| 0.4–0.5 | 58 | 0.4489 | 31 | [16, 36] | yes | ok |
| 0.5–0.6 | 57 | 0.5533 | 30 | [22, 41] | yes | ok |
| 0.6–0.7 | 62 | 0.6432 | 36 | [30, 49] | yes | ok |
| 0.7–0.8 | 34 | 0.7399 | 31 | [18, 31] | yes | ok |
| 0.8–0.9 | 27 | 0.8453 | 22 | [17, 27] | yes | ok |
| 0.9–1.0 | 24 | 0.9502 | 23 | [19, 24] | yes | ok |

##### test 2 (first 400 after 1789296300), all, tau = 180 — `p_t`

n = 400 · observed Up rate 0.5125 · Brier 0.151225

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| 0.0–0.1 | 43 | 0.0521 | 1 | [0, 7] | yes | ok |
| 0.1–0.2 | 46 | 0.1496 | 6 | [1, 14] | yes | ok |
| 0.2–0.3 | 29 | 0.2510 | 9 | [2, 14] | yes | ok |
| 0.3–0.4 | 45 | 0.3529 | 18 | [8, 24] | yes | ok |
| 0.4–0.5 | 41 | 0.4400 | 16 | [10, 26] | yes | ok |
| 0.5–0.6 | 32 | 0.5456 | 14 | [10, 25] | yes | ok |
| 0.6–0.7 | 31 | 0.6579 | 21 | [13, 27] | yes | ok |
| 0.7–0.8 | 50 | 0.7468 | 42 | [29, 45] | yes | ok |
| 0.8–0.9 | 29 | 0.8566 | 27 | [19, 29] | yes | ok |
| 0.9–1.0 | 54 | 0.9564 | 51 | [47, 54] | yes | ok |

##### test 2 (first 400 after 1789296300), all, tau = 120 — `p_t`

n = 400 · observed Up rate 0.5125 · Brier 0.116998

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| 0.0–0.1 | 82 | 0.0321 | 3 | [0, 7] | yes | ok |
| 0.1–0.2 | 39 | 0.1459 | 6 | [1, 12] | yes | ok |
| 0.2–0.3 | 30 | 0.2451 | 8 | [2, 14] | yes | ok |
| 0.3–0.4 | 20 | 0.3450 | 7 | [2, 13] | yes | ok |
| 0.4–0.5 | 22 | 0.4475 | 9 | [4, 16] | yes | ok |
| 0.5–0.6 | 26 | 0.5535 | 12 | [8, 21] | yes | ok |
| 0.6–0.7 | 25 | 0.6457 | 16 | [10, 22] | yes | ok |
| 0.7–0.8 | 32 | 0.7585 | 27 | [18, 30] | yes | ok |
| 0.8–0.9 | 30 | 0.8565 | 27 | [20, 30] | yes | ok |
| 0.9–1.0 | 94 | 0.9760 | 90 | [87, 94] | yes | ok |

##### test 2 (first 400 after 1789296300), all, tau = 90 — `p_t`

n = 400 · observed Up rate 0.5125 · Brier 0.079806

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| 0.0–0.1 | 107 | 0.0248 | 3 | [0, 8] | yes | ok |
| 0.1–0.2 | 34 | 0.1355 | 4 | [0, 10] | yes | ok |
| 0.2–0.3 | 24 | 0.2519 | 4 | [1, 12] | yes | ok |
| 0.3–0.4 | 22 | 0.3453 | 6 | [2, 14] | yes | ok |
| 0.4–0.5 | 13 | 0.4469 | 5 | — | no | — |
| 0.5–0.6 | 12 | 0.5578 | 8 | — | no | — |
| 0.6–0.7 | 19 | 0.6563 | 15 | — | no | — |
| 0.7–0.8 | 18 | 0.7481 | 15 | — | no | — |
| 0.8–0.9 | 27 | 0.8485 | 24 | [18, 27] | yes | ok |
| 0.9–1.0 | 124 | 0.9810 | 121 | [117, 124] | yes | ok |

##### test 2 (first 400 after 1789296300), all, tau = 60 — `p_t`

n = 400 · observed Up rate 0.5125 · Brier 0.042425

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| 0.0–0.1 | 148 | 0.0154 | 2 | [0, 7] | yes | ok |
| 0.1–0.2 | 18 | 0.1465 | 0 | — | no | — |
| 0.2–0.3 | 12 | 0.2394 | 3 | — | no | — |
| 0.3–0.4 | 9 | 0.3784 | 2 | — | no | — |
| 0.4–0.5 | 9 | 0.4694 | 5 | — | no | — |
| 0.5–0.6 | 5 | 0.5534 | 3 | — | no | — |
| 0.6–0.7 | 10 | 0.6504 | 6 | — | no | — |
| 0.7–0.8 | 11 | 0.7518 | 10 | — | no | — |
| 0.8–0.9 | 18 | 0.8545 | 15 | — | no | — |
| 0.9–1.0 | 160 | 0.9863 | 159 | [153, 160] | yes | ok |

##### test 2 (first 400 after 1789296300), all, tau = 30 — `p_t`

n = 400 · observed Up rate 0.5125 · Brier 0.014863

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| 0.0–0.1 | 188 | 0.0054 | 2 | [0, 4] | yes | ok |
| 0.1–0.2 | 3 | 0.1597 | 1 | — | no | — |
| 0.2–0.3 | 2 | 0.2351 | 0 | — | no | — |
| 0.3–0.4 | 1 | 0.3599 | 0 | — | no | — |
| 0.4–0.5 | 5 | 0.4589 | 3 | — | no | — |
| 0.5–0.6 | 1 | 0.5600 | 1 | — | no | — |
| 0.6–0.7 | 2 | 0.6580 | 2 | — | no | — |
| 0.7–0.8 | 2 | 0.7401 | 1 | — | no | — |
| 0.8–0.9 | 5 | 0.8493 | 4 | — | no | — |
| 0.9–1.0 | 191 | 0.9954 | 191 | [187, 191] | yes | ok |

##### test 2 (first 400 after 1789296300), all, tau = 10 — `p_t` (printed, not pooled by G2)

n = 400 · observed Up rate 0.5125 · Brier 0.002485

| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |
|---|---|---|---|---|---|---|
| 0.0–0.1 | 192 | 0.0011 | 0 | [0, 2] | yes | ok |
| 0.1–0.2 | 1 | 0.1043 | 0 | — | no | — |
| 0.2–0.3 | 1 | 0.2574 | 0 | — | no | — |
| 0.3–0.4 | 0 | — | 0 | — | no | — |
| 0.4–0.5 | 0 | — | 0 | — | no | — |
| 0.5–0.6 | 0 | — | 0 | — | no | — |
| 0.6–0.7 | 0 | — | 0 | — | no | — |
| 0.7–0.8 | 1 | 0.7743 | 1 | — | no | — |
| 0.8–0.9 | 4 | 0.8767 | 3 | — | no | — |
| 0.9–1.0 | 201 | 0.9985 | 201 | [199, 201] | yes | ok |

- **The two links on identical rows.** On the admissible checkpoints, `Brier(p_t)` is below
  `Brier(p_fair)` at 10 of the 14 set-and-`tau` rows. The largest difference in
  either direction is 0.002287.
- **Saturation.** `p_t` is never exactly 0.0 or 1.0: the count is 0 in all 28 blocks. `p_fair`
  reaches exactly 0.0 or 1.0 at up to 365 of 400 checkpoints (test 2, all checkpoints, `tau = 10`).
- **Eligible bins.** On test 1's admissible checkpoints, no bin is eligible at any of the 7 `tau`.
- **`λ̂` on a search edge.**
  - 2 of the 28 `λ̂` sit on the lower edge of the committed interval `[0.5, 3.0]`:
    test 1 admissible at `tau = 180` and test 1 admissible at `tau = 10`.
  - Refitted without the most influential observation, 6 land on it:
    test 1 admissible at `tau = 180`, test 1 admissible at `tau = 60`, test 1 admissible at `tau = 30`, test 1 admissible at `tau = 10`, test 2 admissible at `tau = 10` and test 2 all at `tau = 10`.
- **Which observation is most influential.** At 17 of the 28 fits, the observation
  with the largest contribution in magnitude is not the one with the largest signed contribution.
  The table names the first (§6).

### 1.5 M5 — the observation the old gate hung on

| quantity | value |
|---|---|
| `state` | -16.3366330882182757066666666666666666666666666666666666667 |
| `sigma_hat` | 0.689147462686640081059058205788363313362436274789092000140454 |
| `ADMIT` | 2.15178 |
| `admissible` | False |
| `sd_corrected` | 1.51003097750581631290789363073119692292336748584138763672806 |
| `sd_student` | 1.17882466789434870445400503994526334134163060921591359190239 |
| `z_corrected` | -10.818740364652784 |
| `z_student` | -13.858407898266373 |
| `p_fair` | 0.0 |
| `p_t` | 2.3620887357747395e-05 |
| `log_phi_z_corrected` | -61.831158401311896 |
| `log_t_cdf_z_student` | -10.653379179833514 |
| `LINK_NU` | 4.79579 |
| `resolved_up` | 1 |
| contribution under the admissible-member `λ̂` | not a member |
| all-member `λ̂` · contribution to `ll(λ̂)` · to `ll(1)` | 0.767339 · -11.902827 · -10.653379 |

- **`T0 1789268400` is not a member of test 1's admissible rows at `tau = 30`.** The admissible
  pair of contributions is therefore `not a member`, and the all-member pair carries the section,
  as §3.5 directs.
- **Under the old link:** `z` is `-10.818740`, `p_fair` is exactly `0.0`, and `log Φ(z)` is
  `-61.831158`.
- **Under the Student link:** `sd_t` is smaller than `corrected_sd`, which puts `z` at
  `-13.858408`. `p_t` is `2.362089e-05` and `log F_ν(z)` is `-10.653379`.
- **Its pull on `λ̂`.** Under test 1's all-member Student `λ̂`, `0.767339`, its contribution is
  `-11.902827` at `λ̂` against `-10.653379` at `λ = 1`: this observation prefers `λ = 1`. It
  is still the single most influential observation of that fit. Refitted without it, `λ̂` is
  `0.599384`.
- **No conclusion is drawn from one observation.**

### 1.6 The observations file

One row per member per `tau`, 1,200 members by 7 `tau`, in set, `T0` and `tau` order:
8,401 lines, 4,413,283 bytes, SHA-256 `576c803f27da436c6affa6211e7f4fb3d91e61f32077f7a0aac575ded2014f3b`. Columns: `T0`, `set`, `tau`, `admissible`, `label`, `K`, `S_t`, `m_r`, `state`, `sigma_hat`, `ADMIT`, `sd_corrected`, `sd_student`, `z_corrected`, `z_student`, `p_fair_corrected`, `p_t`, `log_phi_z_corrected`, `log_t_cdf_z_student`, `Y`, `r`. The
`label` column is filled on the two test sets only: no label of the fit set was read. Any single
row's `p_t`, `p_fair`, `z` and `sd` can be recomputed by hand from its `state`, `sigma_hat` and
the three tables in §3.2.

---

## 2. The gate tables and the prediction

§4's gate, quoted, fixed before test 1 was scored and before test 2 existed:

| gate | statistic | threshold | judged on |
|---|---|---|---|
| G1 — discrimination | `Brier` of `p_t` | strictly below `0.2496` | every scored `tau`, each test set |
| G2 — bin calibration | `tz06.calibration`, unmodified | at most `tz06.MAX_FAILING_BINS` = 2 failing bins, summed over `pfair.GATED_TAUS` | six `tau`, as `tz06.build` pools them, each test set |
| G3 — scale | `λ̂` under the Student likelihood | `\|λ̂ − 1\| <= 0.15` | every scored `tau`, each test set |
| G4 — shape transfer | `ν̂` refitted on the set | `\|log(ν̂_set / LINK_NU[tau])\| <= log(2)` | every scored `tau`, each test set |

Every row below is one comparison of a reported number against the quoted threshold, made by the
instrument. Nothing is tuned, and no threshold is reinterpreted. **The verdict is the
Architect's.**

#### test 1 (TZ-08a 400)

| tau | G1 `Brier(p_t)` | G1 | G3 `λ̂` | `\|λ̂ − 1\|` | G3 | G4 `ν̂_set` | `LINK_NU` | `\|log(ν̂_set / LINK_NU)\|` | G4 |
|---|---|---|---|---|---|---|---|---|---|
| 240 | 0.207596 | pass | 0.798944 | 0.201056 | FAIL | 14.461092 | 9.62070 | 0.407545 | pass |
| 180 | 0.139315 | pass | 0.500000 | 0.500000 | FAIL | 17.304545 | 13.7083 | 0.232968 | pass |
| 120 | 0.164591 | pass | 0.989133 | 0.010867 | pass | 8.939429 | 20.2258 | 0.816487 | FAIL |
| 90 | 0.126241 | pass | 1.080903 | 0.080903 | pass | 5.599950 | 16.0482 | 1.052839 | FAIL |
| 60 | 0.079479 | pass | 1.146360 | 0.146360 | pass | 3.247500 | 9.51490 | 1.074974 | FAIL |
| 30 | 0.034513 | pass | 0.605213 | 0.394787 | FAIL | 2.050000 | 4.79579 | 0.849899 | FAIL |
| 10 | 0.000006 | pass | 0.500000 | 0.500000 | FAIL | 2.050000 | 2.13489 | 0.040575 | pass |

G2: failing bins over `pfair.GATED_TAUS` 240: 0, 180: 0, 120: 0, 90: 0, 60: 0, 30: 0 — total **0** of 0 eligible, allowance 2: **pass**. `tau = 10`, printed and not pooled: 0 failing of 0 eligible.

G1 7 of 7 · G3 3 of 7 · G4 3 of 7

#### test 2 (first 400 after 1789296300)

| tau | G1 `Brier(p_t)` | G1 | G3 `λ̂` | `\|λ̂ − 1\|` | G3 | G4 `ν̂_set` | `LINK_NU` | `\|log(ν̂_set / LINK_NU)\|` | G4 |
|---|---|---|---|---|---|---|---|---|---|
| 240 | 0.192904 | pass | 0.932553 | 0.067447 | pass | 8.610653 | 9.62070 | 0.110917 | pass |
| 180 | 0.154989 | pass | 0.968834 | 0.031166 | pass | 11.685348 | 13.7083 | 0.159666 | pass |
| 120 | 0.113918 | pass | 0.934540 | 0.065460 | pass | 11.284539 | 20.2258 | 0.583525 | pass |
| 90 | 0.077851 | pass | 0.811435 | 0.188565 | FAIL | 10.411407 | 16.0482 | 0.432695 | pass |
| 60 | 0.037888 | pass | 0.643500 | 0.356500 | FAIL | 7.613244 | 9.51490 | 0.222970 | pass |
| 30 | 0.017575 | pass | 1.074689 | 0.074689 | pass | 4.625274 | 4.79579 | 0.036203 | pass |
| 10 | 0.003640 | pass | 1.131246 | 0.131246 | pass | 2.118037 | 2.13489 | 0.007925 | pass |

G2: failing bins over `pfair.GATED_TAUS` 240: 0, 180: 0, 120: 0, 90: 0, 60: 0, 30: 0 — total **0** of 24 eligible, allowance 2: **pass**. `tau = 10`, printed and not pooled: 0 failing of 2 eligible.

G1 7 of 7 · G3 5 of 7 · G4 7 of 7

- **Where the FAIL rows are:**
  - G3 on test 1 at `tau` 240, 180, 30 and 10, `|λ̂ − 1|` = 240: 0.201056, 180: 0.500000, 30: 0.394787, 10: 0.500000;
  - G3 on test 2 at `tau` 90 and 60, 90: 0.188565, 60: 0.356500;
  - G4 on test 1 at `tau` 120, 90, 60 and 30, `|log(ν̂_set / LINK_NU)|` = 120: 0.816487, 90: 1.052839, 60: 1.074974, 30: 0.849899, against
    `log 2` = 0.693147.
- **G1** passes at 7 of 7 on both sets.
- **G2** passes on both sets, and on test 1 it had nothing to judge: 0 eligible bins at every
  `tau`. `tau = 10` is printed beside G2 and not pooled, as `tz06.build` treats it. On test 2 it
  reads 0 failing of 2 eligible.
- **Two of test 1's G3 rows sit on the search edge.** `λ̂` is `0.500000` at `tau` 180 and 10.
  Their distance from 1 is the distance to the interval's bound (§6).

**The pre-registered prediction, §4.1, beside what was measured:**

| quantity | predicted | measured |
|---|---|---|
| G1 | passes, 7 of 7, on both test sets | test 1: 7 of 7 · test 2: 7 of 7 |
| G2 | passes on both test sets | test 1: 0 failing bins of **0 eligible** · test 2: 0 failing of 24 eligible — both at or below 2 |
| G3 | holds at tau 240, 180, 120 and 90 on both sets; fails at 30 or at 10 on at least one | test 1: holds at 120, 90 and 60, fails at 240, 180, 30 and 10 · test 2: holds at 240, 180, 120, 30 and 10, fails at 90 and 60 |
| G4 | holds at tau <= 120; fails at tau = 240 on test 1 | test 1: holds at 240, 180 and 10, fails at 120, 90, 60 and 30 · test 2: holds at all seven |
| overall | NO, and the failing gate is G4 at long tau | rows marked FAIL: G3 on both test sets, G4 on test 1 at 120, 90, 60 and 30. G4 at `tau = 240` passes on both sets |

---

## 3. The implementation and the three frozen tables

### 3.1 What was built

Branch `tz-11a-student-link`, one commit, `274651805c765bb977c635d75fd1ebdb2c8f550a`, four files:

| file | change | lines | bytes | SHA-256 |
|---|---|---|---|---|
| `research/pfair.py` | twelve names after `log_phi`, insertions only: +128 −0 | 441 | 19,357 | `729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68` |
| `research/selftest-pfair.py` | the six §5.2 items, as family `TZ-11a section 5.2`, insertions only: +178 −0 | 619 | 32,559 | `b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa` |
| `research/tz07a-variance-time.py` | `log_cdf=None` on two functions: four replaced lines and a four-line insertion: +8 −4 | 623 | 28,414 | `513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771` |
| `research/tz11a-student-link.py` | new: the instrument: +1231 −0 | 1,231 | 64,732 | `0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839` |

### 3.2 The three tables

Measured on the fit set alone, by the instrument's `--emit` path before the commit, frozen into
`pfair.py` as Decimal literals at six significant digits, and asserted by V8 in both full runs to
equal the run's own measurement before anything was printed:

```
ADMIT = {240: D("2.12324"), 180: D("2.14298"), 120: D("2.18062"), 90: D("2.16098"),
         60: D("2.16725"), 30: D("2.15178"), 10: D("2.14530")}
LINK_NU = {240: D("9.62070"), 180: D("13.7083"), 120: D("20.2258"), 90: D("16.0482"),
           60: D("9.51490"), 30: D("4.79579"), 10: D("2.13489")}
LINK_SCALE = {240: D("1.30678"), 180: D("1.36658"), 120: D("1.40748"), 90: D("1.37085"),
              60: D("1.27997"), 30: D("1.08185"), 10: D("0.643873")}
```

### 3.3 Where every quantity comes from

| quantity | committed source |
|---|---|
| `Y(a, tau)` and the anchor enumeration | `tz07b.residual`, walked exactly as `tz07b.member_r` walks it; guarded by V4's fourth assertion |
| the horizon `sigma · sqrt(H(tau))` | `tz07b.horizon_sd` |
| M6's disconnect rule | `tz07a.excluded_seconds` and `tz07a.excluded_prefix`, through `tz07b` |
| the fit set and test 2 | `tz06.scoring_set`, at its defaults and at `need=400, after=1789296300` |
| test 1 | `tz08a.the_set`, with every assertion it makes |
| `sigma_hat` | `pfair.realised_sigma` on `pfair.second_grid`, via `tz10b.sigma_hat_of`; asserted equal to `pfair.observations`' `sigma_live` |
| `state`, `K`, `S_t`, `m_r` | `pfair.observations` |
| `sd_t`, `p_t` | `pfair.student_sd`, `pfair.p_fair_student` |
| `p_fair`, `sd` of the old link | `tz07a.corrected`, which is `pfair.corrected_sd` and `pfair.p_fair` |
| `log F_ν`, `log Φ` | `pfair.log_t_cdf`, `pfair.log_phi` |
| `λ̂` | `tz07a.lambda_hat(pairs, log_cdf)`, the committed search |
| `κ` | `tz10b.shape` |
| the bin table and `Brier` | `tz06.table_for`, `tz06.brier` |
| labels | `tz10b.m2_labels`, on the two test sets only |
| the host reads | `tz10b.free_bytes`, `recorder_pids`, `newest_start`, `read_set` |

The Student log-likelihood of §3.1 and the golden-section search are the instrument's own: no
committed file carries either.

### 3.4 `pfair.py`, the whole diff, as V6 read it

```diff
diff --git a/research/pfair.py b/research/pfair.py
index a87fedf..b6023d9 100644
--- a/research/pfair.py
+++ b/research/pfair.py
@@ -82,6 +82,134 @@ def log_phi(z):
     return log_phi_asymptotic_branch(z)
 
 
+# ---- TZ-11a section 5.1: the Student link, and the domain it is priced on -------------
+
+# `Phi` is not the law of the settlement residual (TZ-10b), and a Student's `t` with a measured
+# `nu(tau)` is the replacement TZ-11a scores. Its CDF is the regularized incomplete beta,
+# `F_nu(z) = I_x(nu/2, 1/2) / 2` with `x = nu / (nu + z*z)` for `z <= 0`, and the leading factor
+# of `I_x` is taken in logs: `log_betainc_reg` never forms a probability it then has to take
+# the log of, so the far tail stays finite where `phi` returns exactly 0.0. `phi`, `log_phi` and
+# `p_fair` are not touched - they are the old link, and every committed score is quoted from
+# them.
+LOG_BETA_CF_MAX = 300          # continued-fraction iterations before raising
+LOG_BETA_TOL = 1e-16           # its relative convergence tolerance
+
+
+def log_beta(a, b):
+    """`log B(a, b) = lgamma(a) + lgamma(b) - lgamma(a + b)`."""
+    return math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b)
+
+
+def _betacf(a, b, x):
+    """The continued fraction for `I_x(a, b)`, by the modified Lentz method.
+
+    Raises rather than returning an unconverged value when `LOG_BETA_CF_MAX` iterations do not
+    bring a step within `LOG_BETA_TOL` of one.
+    """
+    tiny = 1e-300
+    qab, qap, qam = a + b, a + 1.0, a - 1.0
+    c = 1.0
+    d = 1.0 - qab * x / qap
+    if abs(d) < tiny:
+        d = tiny
+    d = 1.0 / d
+    h = d
+    for m in range(1, LOG_BETA_CF_MAX + 1):
+        m2 = 2 * m
+        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
+        d = 1.0 + aa * d
+        if abs(d) < tiny:
+            d = tiny
+        c = 1.0 + aa / c
+        if abs(c) < tiny:
+            c = tiny
+        d = 1.0 / d
+        h *= d * c
+        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
+        d = 1.0 + aa * d
+        if abs(d) < tiny:
+            d = tiny
+        c = 1.0 + aa / c
+        if abs(c) < tiny:
+            c = tiny
+        d = 1.0 / d
+        delta = d * c
+        h *= delta
+        if abs(delta - 1.0) < LOG_BETA_TOL:
+            return h
+    raise ArithmeticError("the continued fraction for I_x(%r, %r) at x = %r did not converge "
+                          "in %d iterations" % (a, b, x, LOG_BETA_CF_MAX))
+
+
+def log_betainc_reg(a, b, x):
+    """`log I_x(a, b)`, the log of the regularized incomplete beta function.
+
+    Below the mean-like split `(a + 1) / (a + b + 2)` the continued fraction converges fast and
+    is used directly; above it the symmetry `I_x(a, b) = 1 - I_{1-x}(b, a)` is taken.
+    """
+    if x >= 1:
+        return 0.0
+    if x <= 0:
+        raise ValueError("log I_x(a, b) needs x > 0, got %r" % (x,))
+    if x < (a + 1) / (a + b + 2):
+        return (a * math.log(x) + b * math.log1p(-x) - math.log(a) - log_beta(a, b)
+                + math.log(_betacf(a, b, x)))
+    return math.log1p(-math.exp(log_betainc_reg(b, a, 1 - x)))
+
+
+def log_t_cdf(z, nu):
+    """`log F_nu(z)`, the log CDF of Student's `t` with `nu` degrees of freedom."""
+    if z <= 0:
+        return log_betainc_reg(nu / 2, 0.5, nu / (nu + z * z)) - math.log(2)
+    return math.log1p(-math.exp(log_t_cdf(-z, nu)))
+
+
+def t_cdf(z, nu):
+    """`F_nu(z)`."""
+    return math.exp(log_t_cdf(z, nu))
+
+
+# TZ-11a sections 3.1 and 3.2, measured on the TZ-06 400 alone and on nothing else, from the
+# feed and the manifests - no label was read to produce any of them. `ADMIT[tau]` is the 30th
+# percentile of `sigma_hat` over those 400 at that tau: the Student pricer quotes only where the
+# causal `sigma_hat` is at or above it. `LINK_NU` and `LINK_SCALE` are the maximum-likelihood
+# `nu` and `s` of a symmetric Student's `t` fitted to `r = Y / (sigma * sqrt(H(tau)))` over
+# every admissible anchor of the admissible members. Six significant digits each.
+#
+# These are **literals, not a fit performed at run time**, for the reason `SD_SCALE` is: a pricer
+# that re-derives its constants from the data it is pointed at cannot be tested out of sample.
+# The keys are every tau the pricer serves, `10` included, and an unmeasured tau raises.
+ADMIT = {240: D("2.12324"), 180: D("2.14298"), 120: D("2.18062"), 90: D("2.16098"),
+         60: D("2.16725"), 30: D("2.15178"), 10: D("2.14530")}
+LINK_NU = {240: D("9.62070"), 180: D("13.7083"), 120: D("20.2258"), 90: D("16.0482"),
+           60: D("9.51490"), 30: D("4.79579"), 10: D("2.13489")}
+LINK_SCALE = {240: D("1.30678"), 180: D("1.36658"), 120: D("1.40748"), 90: D("1.37085"),
+              60: D("1.27997"), 30: D("1.08185"), 10: D("0.643873")}
+
+
+def student_sd(tau, sigma):
+    """TZ-11a section 3.4's `sd_t`: the same horizon, at the scale of the fitted Student law.
+
+        sd_t = LINK_SCALE[tau] * sigma * sqrt(H(tau)),   H as `corrected_sd` has it
+
+    `sigma` is `realised_sigma` over the causal window, exactly as `corrected_sd` receives it.
+    """
+    assert tau in LINK_SCALE, "tau = %s has no measured Student scale; TZ-11a measured %s" % (
+        tau, sorted(LINK_SCALE))
+    if tau < SETTLEMENT_S:
+        h = D(tau) ** 3 / D(TAU_CUBED_DIVISOR)
+    else:
+        h = D(tau - 40)
+    return LINK_SCALE[tau] * sigma * h.sqrt()
+
+
+def p_fair_student(state, sd, tau):
+    """`F_nu(state / sd)` at `nu = LINK_NU[tau]`. The division is the last Decimal operation."""
+    assert tau in LINK_NU, "tau = %s has no measured degrees of freedom; TZ-11a measured %s" % (
+        tau, sorted(LINK_NU))
+    return t_cdf(float(state / sd), float(LINK_NU[tau]))
+
+
 def far_branch(tau, s_t, k, sigma):
     """TZ-06 section 3, `tau >= 60`.
 
```

---

## 4. Validation, V1 … V12

Every check TZ-11a §7 names was run. Each subsection gives its count and says whether it is
asserted.

- **Asserted in the instrument:** V2, V4, V5, V6, V7, V8 and V9. Each is an `assert` that aborts
  the run when it is false. Both full runs reached their end, so each held on both.
- **Asserted by this report's assembler:** V3, and the last free-space read.
- **Asserted where §0 says so:** V1's reads.
- **Reported:** V10 and V11.
- **Recorded, not asserted:** V12, as §7 directs.

### V1 — gates

Fingerprint **6 of 6** anchors. Frozen rows **17 of 17**, tracked rows **2 of 2**. Host **3 of 3**. Free space at **10 of 10** reads is at or above its bound (§0); 7 of them are asserted. `numpy` is present: `/root/tz01-env/venv/bin/python`, version `2.5.3`, so §0's `numpy` condition does not block.

### V2 — causality, by perturbation — asserted

| count | value |
|---|---|
| `members` | 20 |
| `checkpoints` | 140 |
| `sigma_hat_bit_identical` | 140 |
| `student_sd_bit_identical` | 140 |
| `control_moved_sigma_hat` | 140 |
| `control_moved_student_sd` | 140 |
| `control_subject_stamped_at_the_checkpoint_instant` | 133 |
| `fewest_reports_perturbed_in_one_checkpoint` | 31 |

Sample: 1789035000, 1789035300, 1789035900, 1789036200, 1789036500, 1789036800, 1789037100, 1789037400, 1789037700, 1789038000, 1789038300, 1789038600, 1789038900, 1789039200, 1789039500, 1789039800, 1789040100, 1789040400, 1789040700, 1789041000

The tested quantities are `sigma_hat` and `pfair.student_sd(tau, sigma_hat)`, and nothing else.
They are the causal inputs to `p_t`. `Y`, `r`, `ν̂`, `ŝ` and every outcome are functions of the
future and exempt, as V2's own row names them.

- **Sample:** the first 20 fit members, at all seven `tau`.
- **Perturbation:** every `chainlink` report stamped strictly after `T0 + (300 − tau)` is
  multiplied by `tz06.PERTURBATION` through the committed `tz06.perturb_after`.
- **Negative control:** `tz06.perturb_one` on `tz06.last_readable`.
- **Asserted before counting:** at each checkpoint, that the control's report lies outside the
  perturbed set, and that at least one report was perturbed.

**140 of 140 bit-identical, for both quantities. The control moves both at 140 of 140.** Each
count is asserted.

### V3 — determinism — asserted by the assembler

| run | started (UTC) | ended (UTC) | wall (s) | peak RSS (KB) | exit |
|---|---|---|---|---|---|
| 1 | 2026-09-14T23:28:35Z | 2026-09-14T23:33:31Z | 295.93 | 122,720 | 0 |
| 2 | 2026-09-14T23:33:31Z | 2026-09-14T23:38:24Z | 292.86 | 142,884 | 0 |

| output | lines | bytes | SHA-256, run 1 | SHA-256, run 2 | identical |
|---|---|---|---|---|---|
| `tz11a-results.json` | 50,270 | 1,332,123 | `3b149e162c6807b827041e90e268a27633ab385ee11240c6de39a7bf92a4960b` | `3b149e162c6807b827041e90e268a27633ab385ee11240c6de39a7bf92a4960b` | yes |
| `tz11a-tables.md` | 3,479 | 273,814 | `c6f35a45d0699bdfbdaf60082f6f8d8acf76b5e1e87853fdd2496f86abc7d77a` | `c6f35a45d0699bdfbdaf60082f6f8d8acf76b5e1e87853fdd2496f86abc7d77a` | yes |
| `tz11a-observations.csv` | 8,401 | 4,413,283 | `576c803f27da436c6affa6211e7f4fb3d91e61f32077f7a0aac575ded2014f3b` | `576c803f27da436c6affa6211e7f4fb3d91e61f32077f7a0aac575ded2014f3b` | yes |

Two full runs, each from a fresh process on the same commit, `274651805c765bb977c635d75fd1ebdb2c8f550a`, in
`/root/tz01-env/venv`. **3 of 3 deterministic outputs are byte-identical.**

- `cmp` returned 0 for each.
- The assembler that writes this report asserts the three SHA-256 pairs equal.
- `tz11a-host.json` holds each run's own clock, disk reads and timings. It differs by
  construction and is not compared. Its contents are in §0 and V9.

**The cost, measured (§3.1's statement).**

| quantity | value |
|---|---|
| first fit | 2.74 s in run 1 and 2.78 s in run 2, against the `60` s fail-fast |
| projection for 63 fits | 173 s |
| all fits, run 1 | 63 fits, 158.7 s |
| slowest fit | 9.31 s |
| most anchors in one fit | 236,125 |
| most likelihood evaluations in one fit | 2,430 |
| set formation, the V6, V7 and V2 checks, and the walk of 1,200 members | 123.2 s |
| whole run 1 | 294.3 s |

The ceiling is CANON's `3,600` s.

### V4 — the instrument reproduces what is committed — asserted

| tau | fit anchors | `RMS(r)`, fit | TZ-07b printed | test-1 anchors | `RMS(r)`, test 1 | TZ-08a printed | `RMS(u)`, test 1 | TZ-08a printed |
|---|---|---|---|---|---|---|---|---|
| 240 | 143255 | 1.523759717 | 1.523760 | 142381 | 1.593657530 | 1.593658 | 1.045871745 | 1.045872 |
| 180 | 167255 | 1.496022752 | 1.496023 | 166418 | 1.524720971 | 1.524721 | 1.019184884 | 1.019185 |
| 120 | 191343 | 1.496276837 | 1.496277 | 190855 | 1.389965274 | 1.389965 | 0.928947305 | 0.928947 |
| 90 | 203416 | 1.479154254 | 1.479154 | 203152 | 1.350835970 | 1.350836 | 0.913251509 | 0.913252 |
| 60 | 215620 | 1.444657989 | 1.444658 | 215492 | 1.315235496 | 1.315235 | 0.910411790 | 0.910412 |
| 30 | 227920 | 1.385805790 | 1.385806 | 227865 | 1.265286515 | 1.265287 | 0.913030296 | 0.913030 |
| 10 | 236125 | 1.211176004 | 1.211176 | 236125 | 1.112329039 | 1.112329 | 0.918384583 | 0.918385 |

`tz07a.lambda_hat` at its default, tau = 30, n = 400: 2.0418426092 (expected 2.0418426092)

`tz07b.member_r` guard: 50 members = 20 first fit members + 15 fit and 16 test-1 members M6 drops a second of, overlap 1789035900: 1789035000, 1789035300, 1789035900, 1789036200, 1789036500, 1789036800, 1789037100, 1789037400, 1789037700, 1789038000, 1789038300, 1789038600, 1789038900, 1789039200, 1789039500, 1789039800, 1789040100, 1789040400, 1789040700, 1789041000, 1789043100, 1789050300, 1789057500, 1789064700, 1789071900, 1789073100, 1789080300, 1789102500, 1789128300, 1789131600, 1789138800, 1789141800, 1789149000, 1789162500, 1789169700, 1789170600, 1789177800, 1789185000, 1789197000, 1789200300, 1789206900, 1789214100, 1789221300, 1789252800, 1789260000, 1789267200, 1789274400, 1789278300, 1789285500, 1789292700

Four assertions, each a count:

1. **TZ-07b's `Λ`, 7 of 7 on the fit set.** It comes from this instrument's own walk of `r`, as
   the uncentred root mean square printed at six decimals.
2. **TZ-08a V8's `Λ_oos` and `Λ_oos / SD_SCALE`, 7 of 7 each on test 1.** The second is the RMS
   of `u`. Both are compared against that report's printed columns.
3. **`tz07a.lambda_hat` at its default** returns `2.0418426092` at `tau = 30` on the TZ-08a 400,
   to ten decimals. The committed `Φ` path runs unchanged. This reads those 400 labels, the third
   outcome read §2 names.
4. **The committed `tz07b.member_r`, called beside this run's walk on 50 members.** Every `r`, the
   Decimal sum of squares, the dropped count and the checkpoint `r` are asserted identical.
   - The 50 are re-derived at run time over the fit set and test 1 only: 20 first fit members,
     plus 15 fit members and 16 test-1 members that M6 drops a second of.
   - The one overlap is `1789035900`.
   - The count is asserted equal to 50.

### V5 — set identity — asserted

- Fit set: `6d94a346a47a04a1a0849968effd9023d7585fe628b304ba2ae7a15953ee67f9`.
- Test 1: `3b17729c050e5fbf8fed1bd0877d5dd5c229370609cd672c84eeed1ddc3d5762`.

Both are asserted equal to §3.0's values. Test 2's hash, `2dd0fcc4dc2cf379e08c21a4524c3eab799aad7bff3136c37e32910cecb8fa70`, is computed the same way
and reported. **2 asserted, 1 reported.** The three sets are asserted pairwise disjoint.

### V6 — the diff, in its real shape — asserted

merge base `72e709241092aa9b76e25ffc109a0106c3c23076` · head `274651805c765bb977c635d75fd1ebdb2c8f550a`

| file | lines added | lines removed | top-level objects before | byte-identical after | exempt | objects added |
|---|---|---|---|---|---|---|
| `pfair.py` | 128 | 0 | 25 | 25 | — | `ADMIT`, `LINK_NU`, `LINK_SCALE`, `LOG_BETA_CF_MAX`, `LOG_BETA_TOL`, `_betacf`, `log_beta`, `log_betainc_reg`, `log_t_cdf`, `p_fair_student`, `student_sd`, `t_cdf` |
| `selftest-pfair.py` | 178 | 0 | 29 | 29 | — | `F3_AT_MINUS_10_819`, `LOG_F3_AT_MINUS_10_819`, `LOG_T_CDF_LITERALS`, `LOG_T_CDF_ZS`, `NORMAL_LIMIT_BOUND`, `NORMAL_LIMIT_EXPECTED`, `NORMAL_LIMIT_NU`, `TZ11A_RELATIVE`, `tz11a_item_1_the_literals`, `tz11a_item_2_symmetry`, `tz11a_item_3_the_normal_limit`, `tz11a_item_4_shape`, `tz11a_item_5_the_pathology_removed`, `tz11a_item_6_the_tables` |
| `tz07a-variance-time.py` | 8 | 4 | 41 | 39 | `lambda_hat`, `log_likelihood` | — |

Attribute assignments in the instrument: none · name bindings scanned: 526

```diff
diff --git a/research/tz07a-variance-time.py b/research/tz07a-variance-time.py
index fab0357..42fbcb6 100644
--- a/research/tz07a-variance-time.py
+++ b/research/tz07a-variance-time.py
@@ -267,10 +267,14 @@ def corrected_observations(t0, s1, s3, taus=pfair.GATED_TAUS):
 
 # ---- M3, in-sample diagnostics ----------------------------------------------------
 
-def log_likelihood(pairs, lam):
+def log_likelihood(pairs, lam, log_cdf=None):
     """`sum( y log Phi(z/lam) + (1-y) log(1 - Phi(z/lam)) )`, section 8 G3."""
     total = 0.0
     for z, y in pairs:
+        if log_cdf is not None:
+            u = z / lam
+            total += log_cdf(u) if y else log_cdf(-u)
+            continue
         p = pfair.phi(z / lam)
         q = p if y else 1.0 - p
         if q <= 0.0:
@@ -279,7 +283,7 @@ def log_likelihood(pairs, lam):
     return total
 
 
-def lambda_hat(pairs):
+def lambda_hat(pairs, log_cdf=None):
     """Section 8 G3's `lambda-hat`: ternary search over [0.5, 3.0] to 1e-9.
 
     Reported here as a section 5 diagnostic with no threshold. The same definition is the one
@@ -289,12 +293,12 @@ def lambda_hat(pairs):
     while hi - lo > LAMBDA_TOL:
         a = lo + (hi - lo) / 3.0
         b = hi - (hi - lo) / 3.0
-        if log_likelihood(pairs, a) < log_likelihood(pairs, b):
+        if log_likelihood(pairs, a, log_cdf) < log_likelihood(pairs, b, log_cdf):
             lo = a
         else:
             hi = b
     lam = (lo + hi) / 2.0
-    ll_hat, ll_one = log_likelihood(pairs, lam), log_likelihood(pairs, 1.0)
+    ll_hat, ll_one = log_likelihood(pairs, lam, log_cdf), log_likelihood(pairs, 1.0, log_cdf)
     ratio = 2.0 * (ll_hat - ll_one)
     return {"lambda_hat": lam, "ll_at_lambda_hat": ll_hat, "ll_at_one": ll_one,
             "likelihood_ratio": ratio,
```

- **The run is of committed files.** `git status --porcelain` is empty for the five paths.
- **The diff is taken against `git merge-base HEAD main`:**
  - `pfair.py` (+128) and `selftest-pfair.py` (+178) hold insertions
    only.
  - `tz07a-variance-time.py` holds 8 inserted lines and exactly four removed
    ones. The removed set is asserted equal, string for string, to the four texts §5.3 names.
- **Every top-level object each file held before is byte-identical after.** A top-level object
  here is a function, a class, or an assignment to a plain name, compared by exact source text
  through `ast`.
  - This covers the ten `pfair.py` objects V6 names, asserted by name.
  - The exceptions are `tz07a.log_likelihood` and `tz07a.lambda_hat`, whose diff is printed below
    in full.
- **`pfair.py` gains exactly the twelve names of §5.1.**
- **The instrument assigns no attribute.** Its `ast` holds no attribute in a store or delete
  context, and no `setattr` or `delattr` call. 526 name bindings were scanned.

### V7 — the self-tests — asserted

**The six self-tests of §5.2: 6 of 6**, each an `assert` that aborts `selftest-pfair.py`. The instrument runs that file as a subprocess and asserts its exit status 0 and the family counts TZ-07b section 6 30, TZ-10b section 5.2 6, TZ-11a section 5.2 6, V5 56, section 3 machinery 18 — **116 checks in all**, against the 110 the file held before. The six items' output, verbatim:

```
tz11a_item_1_the_literals
      nu = 2    z = 0        log_t_cdf -0.693147180559945  literal -0.693147180559945  relative 4.81e-16
      nu = 2    z = -1       log_t_cdf -1.55435868307644  literal -1.55435868307644  relative 3.14e-15
      nu = 2    z = -3       log_t_cdf -3.04213264974235  literal -3.04213264974235  relative 2.92e-16
      nu = 2    z = -5       log_t_cdf -3.96992886866936  literal -3.96992886866936  relative 7.83e-16
      nu = 2    z = -8       log_t_cdf -4.87513859809586  literal -4.87513859809586  relative 7.29e-16
      nu = 2    z = -10.819  log_t_cdf -5.46847054829008  literal -5.46847054829007  relative 1.14e-15
      nu = 2    z = -20      log_t_cdf -6.68835316116258  literal -6.68835316116258  relative 3.98e-16
      nu = 2    z = -50      log_t_cdf -8.51779297152817  literal -8.51779297152817  relative 4.17e-16
      nu = 2.5  z = 0        log_t_cdf -0.693147180559945  literal -0.693147180559945  relative 4.81e-16
      nu = 2.5  z = -1       log_t_cdf -1.5993365353695  literal -1.59933653536950  relative 3.05e-15
      nu = 2.5  z = -3       log_t_cdf -3.31626685434013  literal -3.31626685434013  relative 6.7e-16
      nu = 2.5  z = -5       log_t_cdf -4.44598122091119  literal -4.44598122091119  relative 4e-16
      nu = 2.5  z = -8       log_t_cdf -5.56532867478168  literal -5.56532867478168  relative 3.19e-16
      nu = 2.5  z = -10.819  log_t_cdf -6.30324233817012  literal -6.30324233817012  relative 1.41e-16
      nu = 2.5  z = -20      log_t_cdf -7.82481099775613  literal -7.82481099775613  relative 1.14e-16
      nu = 2.5  z = -50      log_t_cdf -10.1104508277657  literal -10.1104508277657  relative 3.69e-15
      nu = 3    z = 0        log_t_cdf -0.693147180559945  literal -0.693147180559945  relative 4.81e-16
      nu = 3    z = -1       log_t_cdf -1.63218922449412  literal -1.63218922449412  relative 1.09e-15
      nu = 3    z = -3       log_t_cdf -3.54618467545091  literal -3.54618467545091  relative 7.51e-16
      nu = 3    z = -5       log_t_cdf -4.86702610492042  literal -4.86702610492042  relative 1.82e-16
      nu = 3    z = -8       log_t_cdf -6.19564464966101  literal -6.19564464966101  relative 7.17e-16
      nu = 3    z = -10.819  log_t_cdf -7.07657843379202  literal -7.07657843379202  relative 1.26e-16
      nu = 3    z = -20      log_t_cdf -8.89844171394626  literal -8.89844171394626  relative 0
      nu = 3    z = -50      log_t_cdf -11.639784763244  literal -11.6397847632440  relative 1.83e-15
      nu = 4    z = 0        log_t_cdf -0.693147180559945  literal -0.693147180559945  relative 4.81e-16
      nu = 4    z = -1       log_t_cdf -1.67691149318135  literal -1.67691149318135  relative 2.65e-15
      nu = 4    z = -3       log_t_cdf -3.91347485706189  literal -3.91347485706189  relative 2.27e-16
      nu = 4    z = -5       log_t_cdf -5.58727573561669  literal -5.58727573561669  relative 7.95e-16
      nu = 4    z = -8       log_t_cdf -7.32032286818778  literal -7.32032286818778  relative 6.07e-16
      nu = 4    z = -10.819  log_t_cdf -8.48264615644609  literal -8.48264615644609  relative 4.19e-16
      nu = 4    z = -20      log_t_cdf -10.9009041296344  literal -10.9009041296344  relative 8.15e-16
      nu = 4    z = -50      log_t_cdf -14.5521443574038  literal -14.5521443574038  relative 9.77e-16
      nu = 7    z = 0        log_t_cdf -0.693147180559945  literal -0.693147180559945  relative 4.81e-16
      nu = 7    z = -1       log_t_cdf -1.74120896160071  literal -1.74120896160071  relative 1.02e-15
      nu = 7    z = -3       log_t_cdf -4.60806807421352  literal -4.60806807421352  relative 9.64e-16
      nu = 7    z = -5       log_t_cdf -7.15283904545879  literal -7.15283904545879  relative 0
      nu = 7    z = -8       log_t_cdf -9.9961598857227  literal -9.99615988572270  relative 3.55e-16
      nu = 7    z = -10.819  log_t_cdf -11.9667403968485  literal -11.9667403968485  relative 4.01e-15
      nu = 7    z = -20      log_t_cdf -16.1409126343562  literal -16.1409126343562  relative 1.54e-15
      nu = 7    z = -50      log_t_cdf -22.5096639254306  literal -22.5096639254306  relative 1.58e-16
      worst relative difference over the 40: 4.01e-15
  ok  item 1: log_t_cdf equals all 40 literals to 12 significant digits and within 1e-12 relative
tz11a_item_2_symmetry
      15 pairs, worst |F(z) + F(-z) - 1| 0
  ok  item 2: exp(log_t_cdf(z)) + exp(log_t_cdf(-z)) equals 1 to 12 significant digits at 15 pairs
tz11a_item_3_the_normal_limit
      z = -3  t_cdf(z, 1e6) 0.00134993126975073  phi 0.0013498980316301  relative 2.46e-05
      z = -2  t_cdf(z, 1e6) 0.022750266909072  phi 0.0227501319481792  relative 5.93e-06
      z = -1  t_cdf(z, 1e6) 0.158655375157886  phi 0.158655253931457  relative 7.64e-07
      z = 0  t_cdf(z, 1e6) 0.5  phi 0.5  relative 0
      z = 1  t_cdf(z, 1e6) 0.841344624842114  phi 0.841344746068543  relative 1.44e-07
      z = 2  t_cdf(z, 1e6) 0.977249733090928  phi 0.977249868051821  relative 1.38e-07
      z = 3  t_cdf(z, 1e6) 0.998650068730249  phi 0.99865010196837  relative 3.33e-08
      worst relative gap 2.46e-05, expected 2.46e-5, bound 0.0001
  ok  item 3: the worst relative gap between t_cdf(z, 1e6) and phi(z) over -3 ... 3 is below 1e-4
tz11a_item_4_shape
      nu = 2.05: 65001 points over -60 ... 5, 0 steps not strictly increasing; 40001 points over -200 ... 200, 0 values not finite
      nu = 3: 65001 points over -60 ... 5, 0 steps not strictly increasing; 40001 points over -200 ... 200, 0 values not finite
      nu = 60: 65001 points over -60 ... 5, 0 steps not strictly increasing; 40001 points over -200 ... 200, 0 values not finite
  ok  item 4: log_t_cdf is strictly increasing over -60 ... 5 and finite over -200 ... 200 at nu = 2.05, 3 and 60
tz11a_item_5_the_pathology_removed
      z -10.819  p_fair 0.0  log(p_fair) finite False
      5a: t_cdf(z, 3.0) 8.4465826393e-04  literal 8.4465826393e-04  relative 7.86e-14
      5a: log_t_cdf(z, 3.0) -7.07657843379202  literal -7.07657843379202  relative 1.26e-16
      5b: LINK_NU[30] 4.79579  p_fair_student 7.5023342705e-05  log_t_cdf(z, LINK_NU[30]) -9.4977112567791
  ok  item 5: 5a - phi is 0.0 and its log not finite, F_3 and log F_3 equal the literals; 5b - 0 < p_fair_student < 1e-2 and log_t_cdf at LINK_NU[30] is finite and inside (-40, -5)
tz11a_item_6_the_tables
      keys [10, 30, 60, 90, 120, 180, 240]  refused at tau = 100: ['student_sd', 'p_fair_student']  student_sd(30, 3.25) 5.55930389081138691802487984419737188676981368215335196422065
  ok  item 6: ADMIT, LINK_NU and LINK_SCALE are keyed by exactly pfair.TAUS; student_sd and p_fair_student raise at tau = 100; student_sd(30, 3.25) is its own table's identity
```

### V8 — the frozen literals — asserted

| table | tau | measured | six significant digits | `pfair.py` | equal |
|---|---|---|---|---|---|
| `ADMIT` | 240 | 2.12323563710977700863992290532836048954679137061092591268262 | 2.12324 | 2.12324 | yes |
| `ADMIT` | 180 | 2.14297953483601541833671123634419195958769456009357218733673 | 2.14298 | 2.14298 | yes |
| `ADMIT` | 120 | 2.18062445594454858665628785168648813207862990507317274088634 | 2.18062 | 2.18062 | yes |
| `ADMIT` | 90 | 2.16098393609846481568421260052095142761829878674908147511798 | 2.16098 | 2.16098 | yes |
| `ADMIT` | 60 | 2.16725132207611032551760330806404666763461071720549872543518 | 2.16725 | 2.16725 | yes |
| `ADMIT` | 30 | 2.15177516748816903237227067411384315111044198774715490464266 | 2.15178 | 2.15178 | yes |
| `ADMIT` | 10 | 2.14529915495351733740895978316262608043242687009752754952761 | 2.14530 | 2.14530 | yes |
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

For each of `ADMIT`, `LINK_NU` and `LINK_SCALE`, at each `tau`, the committed literal is asserted
equal to the run's own measurement at six significant digits, before any table is printed.
**21 of 21, in both runs.**

### V9 — the capture is untouched — asserted

| run | read | UTC | recorder pids | newest start sha | `recv_ns` | interval directories | read-set SHA-256 | files |
|---|---|---|---|---|---|---|---|---|
| 1 | run start | 2026-09-14T23:29:01Z | [228592] | `4216c04673ce…` | 1789206785264516934 | 1,317 | `33ab86854231c723…` | 11,251 |
| 1 | after the walk | 2026-09-14T23:30:39Z | [228592] | `4216c04673ce…` | 1789206785264516934 | 1,317 | `33ab86854231c723…` | 11,251 |
| 1 | run end | 2026-09-14T23:33:30Z | [228592] | `4216c04673ce…` | 1789206785264516934 | 1,318 | `33ab86854231c723…` | 11,251 |
| 2 | run start | 2026-09-14T23:33:56Z | [228592] | `4216c04673ce…` | 1789206785264516934 | 1,318 | `33ab86854231c723…` | 11,251 |
| 2 | after the walk | 2026-09-14T23:35:34Z | [228592] | `4216c04673ce…` | 1789206785264516934 | 1,318 | `33ab86854231c723…` | 11,251 |
| 2 | run end | 2026-09-14T23:38:23Z | [228592] | `4216c04673ce…` | 1789206785264516934 | 1,318 | `33ab86854231c723…` | 11,251 |

Each full run read the host three times: at its start, after the walk, and at its end. Between its
first and last read, it asserted:

- the same recorder pid;
- the same newest start record, its sha and its `recv_ns`;
- an interval count that did not fall;
- an equal SHA-256 over the name, size and modification time of every file in every interval
  directory the run reads. That is 1,314 directories and 11,251 files: every unit
  the three walks considered, and each member's predecessor.

| run | read | UTC | recorder pids | newest start sha | `recv_ns` | interval directories | read-set SHA-256 | files |
|---|---|---|---|---|---|---|---|---|
| 1 | run start | 2026-09-14T23:29:01Z | [228592] | `4216c04673ce…` | 1789206785264516934 | 1,317 | `33ab86854231c723…` | 11,251 |
| 1 | after the walk | 2026-09-14T23:30:39Z | [228592] | `4216c04673ce…` | 1789206785264516934 | 1,317 | `33ab86854231c723…` | 11,251 |
| 1 | run end | 2026-09-14T23:33:30Z | [228592] | `4216c04673ce…` | 1789206785264516934 | 1,318 | `33ab86854231c723…` | 11,251 |
| 2 | run start | 2026-09-14T23:33:56Z | [228592] | `4216c04673ce…` | 1789206785264516934 | 1,318 | `33ab86854231c723…` | 11,251 |
| 2 | after the walk | 2026-09-14T23:35:34Z | [228592] | `4216c04673ce…` | 1789206785264516934 | 1,318 | `33ab86854231c723…` | 11,251 |
| 2 | run end | 2026-09-14T23:38:23Z | [228592] | `4216c04673ce…` | 1789206785264516934 | 1,318 | `33ab86854231c723…` | 11,251 |

What the instrument can write, enumerated as System Map §7 item 32 requires:

- **Files:** four outputs, into the `--out` directory, which is asserted to lie outside
  `/var/lib/btc-recorder/`.
- **Subprocesses:** two, each a fixed argument list with no shell:
  - `git`, in six read-only forms: `merge-base`, `rev-parse`, `status --porcelain`, `diff`,
    `diff --unified=0` and `show`, each through `tz10b.git`;
  - `python -B selftest-pfair.py`.
- **Reads:** the committed readers open the capture read-only. The instrument's own reads of the
  host are `os.statvfs`, `os.stat`, `os.listdir`, `/proc/<pid>/cmdline` and `runtime.jsonl`, all
  through `tz10b`'s helpers, and all read-only.

### V10 — the fingerprint table

Every row of map §0 is in §0 in lines, bytes and SHA-256. **The frozen rows match on `main`: 17 of
17.** The four rows TZ-11a changes or adds are reported beside them, as they stand on the branch.

### V11 — disclosure

Every unit each of the three walks considered, in order, members and non-members alike, with the
reason for each non-member; then every member's admissibility at every `tau`, with its
`sigma_hat` and the `ADMIT[tau]` it was compared against.

#### The fit-set walk

| # | T0 | open (UTC) | member | reason not a member |
|---|---|---|---|---|
| 1 | 1789033800 | 2026-09-10 09:50 | — | disconnect + no chainlink at or before T0-300 |
| 2 | 1789034100 | 2026-09-10 09:55 | — | disconnect + no chainlink at or before T0-300 |
| 3 | 1789034400 | 2026-09-10 10:00 | — | disconnect |
| 4 | 1789034700 | 2026-09-10 10:05 | — | disconnect |
| 5 | 1789035000 | 2026-09-10 10:10 | 1 | — |
| 6 | 1789035300 | 2026-09-10 10:15 | 2 | — |
| 7 | 1789035600 | 2026-09-10 10:20 | — | disconnect |
| 8 | 1789035900 | 2026-09-10 10:25 | 3 | — |
| 9 | 1789036200 | 2026-09-10 10:30 | 4 | — |
| 10 | 1789036500 | 2026-09-10 10:35 | 5 | — |
| 11 | 1789036800 | 2026-09-10 10:40 | 6 | — |
| 12 | 1789037100 | 2026-09-10 10:45 | 7 | — |
| 13 | 1789037400 | 2026-09-10 10:50 | 8 | — |
| 14 | 1789037700 | 2026-09-10 10:55 | 9 | — |
| 15 | 1789038000 | 2026-09-10 11:00 | 10 | — |
| 16 | 1789038300 | 2026-09-10 11:05 | 11 | — |
| 17 | 1789038600 | 2026-09-10 11:10 | 12 | — |
| 18 | 1789038900 | 2026-09-10 11:15 | 13 | — |
| 19 | 1789039200 | 2026-09-10 11:20 | 14 | — |
| 20 | 1789039500 | 2026-09-10 11:25 | 15 | — |
| 21 | 1789039800 | 2026-09-10 11:30 | 16 | — |
| 22 | 1789040100 | 2026-09-10 11:35 | 17 | — |
| 23 | 1789040400 | 2026-09-10 11:40 | 18 | — |
| 24 | 1789040700 | 2026-09-10 11:45 | 19 | — |
| 25 | 1789041000 | 2026-09-10 11:50 | 20 | — |
| 26 | 1789041300 | 2026-09-10 11:55 | 21 | — |
| 27 | 1789041600 | 2026-09-10 12:00 | 22 | — |
| 28 | 1789041900 | 2026-09-10 12:05 | 23 | — |
| 29 | 1789042200 | 2026-09-10 12:10 | 24 | — |
| 30 | 1789042500 | 2026-09-10 12:15 | 25 | — |
| 31 | 1789042800 | 2026-09-10 12:20 | — | disconnect |
| 32 | 1789043100 | 2026-09-10 12:25 | 26 | — |
| 33 | 1789043400 | 2026-09-10 12:30 | 27 | — |
| 34 | 1789043700 | 2026-09-10 12:35 | 28 | — |
| 35 | 1789044000 | 2026-09-10 12:40 | 29 | — |
| 36 | 1789044300 | 2026-09-10 12:45 | 30 | — |
| 37 | 1789044600 | 2026-09-10 12:50 | 31 | — |
| 38 | 1789044900 | 2026-09-10 12:55 | 32 | — |
| 39 | 1789045200 | 2026-09-10 13:00 | 33 | — |
| 40 | 1789045500 | 2026-09-10 13:05 | 34 | — |
| 41 | 1789045800 | 2026-09-10 13:10 | 35 | — |
| 42 | 1789046100 | 2026-09-10 13:15 | 36 | — |
| 43 | 1789046400 | 2026-09-10 13:20 | 37 | — |
| 44 | 1789046700 | 2026-09-10 13:25 | 38 | — |
| 45 | 1789047000 | 2026-09-10 13:30 | 39 | — |
| 46 | 1789047300 | 2026-09-10 13:35 | 40 | — |
| 47 | 1789047600 | 2026-09-10 13:40 | 41 | — |
| 48 | 1789047900 | 2026-09-10 13:45 | 42 | — |
| 49 | 1789048200 | 2026-09-10 13:50 | 43 | — |
| 50 | 1789048500 | 2026-09-10 13:55 | 44 | — |
| 51 | 1789048800 | 2026-09-10 14:00 | 45 | — |
| 52 | 1789049100 | 2026-09-10 14:05 | 46 | — |
| 53 | 1789049400 | 2026-09-10 14:10 | 47 | — |
| 54 | 1789049700 | 2026-09-10 14:15 | 48 | — |
| 55 | 1789050000 | 2026-09-10 14:20 | — | disconnect |
| 56 | 1789050300 | 2026-09-10 14:25 | 49 | — |
| 57 | 1789050600 | 2026-09-10 14:30 | 50 | — |
| 58 | 1789050900 | 2026-09-10 14:35 | 51 | — |
| 59 | 1789051200 | 2026-09-10 14:40 | 52 | — |
| 60 | 1789051500 | 2026-09-10 14:45 | 53 | — |
| 61 | 1789051800 | 2026-09-10 14:50 | 54 | — |
| 62 | 1789052100 | 2026-09-10 14:55 | 55 | — |
| 63 | 1789052400 | 2026-09-10 15:00 | 56 | — |
| 64 | 1789052700 | 2026-09-10 15:05 | 57 | — |
| 65 | 1789053000 | 2026-09-10 15:10 | 58 | — |
| 66 | 1789053300 | 2026-09-10 15:15 | 59 | — |
| 67 | 1789053600 | 2026-09-10 15:20 | 60 | — |
| 68 | 1789053900 | 2026-09-10 15:25 | 61 | — |
| 69 | 1789054200 | 2026-09-10 15:30 | 62 | — |
| 70 | 1789054500 | 2026-09-10 15:35 | 63 | — |
| 71 | 1789054800 | 2026-09-10 15:40 | 64 | — |
| 72 | 1789055100 | 2026-09-10 15:45 | 65 | — |
| 73 | 1789055400 | 2026-09-10 15:50 | 66 | — |
| 74 | 1789055700 | 2026-09-10 15:55 | 67 | — |
| 75 | 1789056000 | 2026-09-10 16:00 | 68 | — |
| 76 | 1789056300 | 2026-09-10 16:05 | 69 | — |
| 77 | 1789056600 | 2026-09-10 16:10 | 70 | — |
| 78 | 1789056900 | 2026-09-10 16:15 | 71 | — |
| 79 | 1789057200 | 2026-09-10 16:20 | — | disconnect |
| 80 | 1789057500 | 2026-09-10 16:25 | 72 | — |
| 81 | 1789057800 | 2026-09-10 16:30 | 73 | — |
| 82 | 1789058100 | 2026-09-10 16:35 | 74 | — |
| 83 | 1789058400 | 2026-09-10 16:40 | 75 | — |
| 84 | 1789058700 | 2026-09-10 16:45 | 76 | — |
| 85 | 1789059000 | 2026-09-10 16:50 | 77 | — |
| 86 | 1789059300 | 2026-09-10 16:55 | 78 | — |
| 87 | 1789059600 | 2026-09-10 17:00 | 79 | — |
| 88 | 1789059900 | 2026-09-10 17:05 | 80 | — |
| 89 | 1789060200 | 2026-09-10 17:10 | 81 | — |
| 90 | 1789060500 | 2026-09-10 17:15 | 82 | — |
| 91 | 1789060800 | 2026-09-10 17:20 | 83 | — |
| 92 | 1789061100 | 2026-09-10 17:25 | 84 | — |
| 93 | 1789061400 | 2026-09-10 17:30 | 85 | — |
| 94 | 1789061700 | 2026-09-10 17:35 | 86 | — |
| 95 | 1789062000 | 2026-09-10 17:40 | 87 | — |
| 96 | 1789062300 | 2026-09-10 17:45 | 88 | — |
| 97 | 1789062600 | 2026-09-10 17:50 | 89 | — |
| 98 | 1789062900 | 2026-09-10 17:55 | 90 | — |
| 99 | 1789063200 | 2026-09-10 18:00 | 91 | — |
| 100 | 1789063500 | 2026-09-10 18:05 | 92 | — |
| 101 | 1789063800 | 2026-09-10 18:10 | 93 | — |
| 102 | 1789064100 | 2026-09-10 18:15 | 94 | — |
| 103 | 1789064400 | 2026-09-10 18:20 | — | disconnect |
| 104 | 1789064700 | 2026-09-10 18:25 | 95 | — |
| 105 | 1789065000 | 2026-09-10 18:30 | 96 | — |
| 106 | 1789065300 | 2026-09-10 18:35 | 97 | — |
| 107 | 1789065600 | 2026-09-10 18:40 | 98 | — |
| 108 | 1789065900 | 2026-09-10 18:45 | 99 | — |
| 109 | 1789066200 | 2026-09-10 18:50 | 100 | — |
| 110 | 1789066500 | 2026-09-10 18:55 | 101 | — |
| 111 | 1789066800 | 2026-09-10 19:00 | 102 | — |
| 112 | 1789067100 | 2026-09-10 19:05 | 103 | — |
| 113 | 1789067400 | 2026-09-10 19:10 | 104 | — |
| 114 | 1789067700 | 2026-09-10 19:15 | 105 | — |
| 115 | 1789068000 | 2026-09-10 19:20 | 106 | — |
| 116 | 1789068300 | 2026-09-10 19:25 | 107 | — |
| 117 | 1789068600 | 2026-09-10 19:30 | 108 | — |
| 118 | 1789068900 | 2026-09-10 19:35 | 109 | — |
| 119 | 1789069200 | 2026-09-10 19:40 | 110 | — |
| 120 | 1789069500 | 2026-09-10 19:45 | 111 | — |
| 121 | 1789069800 | 2026-09-10 19:50 | 112 | — |
| 122 | 1789070100 | 2026-09-10 19:55 | 113 | — |
| 123 | 1789070400 | 2026-09-10 20:00 | 114 | — |
| 124 | 1789070700 | 2026-09-10 20:05 | 115 | — |
| 125 | 1789071000 | 2026-09-10 20:10 | 116 | — |
| 126 | 1789071300 | 2026-09-10 20:15 | 117 | — |
| 127 | 1789071600 | 2026-09-10 20:20 | — | disconnect |
| 128 | 1789071900 | 2026-09-10 20:25 | 118 | — |
| 129 | 1789072200 | 2026-09-10 20:30 | 119 | — |
| 130 | 1789072500 | 2026-09-10 20:35 | 120 | — |
| 131 | 1789072800 | 2026-09-10 20:40 | — | disconnect |
| 132 | 1789073100 | 2026-09-10 20:45 | 121 | — |
| 133 | 1789073400 | 2026-09-10 20:50 | 122 | — |
| 134 | 1789073700 | 2026-09-10 20:55 | 123 | — |
| 135 | 1789074000 | 2026-09-10 21:00 | 124 | — |
| 136 | 1789074300 | 2026-09-10 21:05 | 125 | — |
| 137 | 1789074600 | 2026-09-10 21:10 | 126 | — |
| 138 | 1789074900 | 2026-09-10 21:15 | 127 | — |
| 139 | 1789075200 | 2026-09-10 21:20 | 128 | — |
| 140 | 1789075500 | 2026-09-10 21:25 | 129 | — |
| 141 | 1789075800 | 2026-09-10 21:30 | 130 | — |
| 142 | 1789076100 | 2026-09-10 21:35 | 131 | — |
| 143 | 1789076400 | 2026-09-10 21:40 | 132 | — |
| 144 | 1789076700 | 2026-09-10 21:45 | 133 | — |
| 145 | 1789077000 | 2026-09-10 21:50 | 134 | — |
| 146 | 1789077300 | 2026-09-10 21:55 | 135 | — |
| 147 | 1789077600 | 2026-09-10 22:00 | 136 | — |
| 148 | 1789077900 | 2026-09-10 22:05 | 137 | — |
| 149 | 1789078200 | 2026-09-10 22:10 | 138 | — |
| 150 | 1789078500 | 2026-09-10 22:15 | 139 | — |
| 151 | 1789078800 | 2026-09-10 22:20 | 140 | — |
| 152 | 1789079100 | 2026-09-10 22:25 | 141 | — |
| 153 | 1789079400 | 2026-09-10 22:30 | 142 | — |
| 154 | 1789079700 | 2026-09-10 22:35 | 143 | — |
| 155 | 1789080000 | 2026-09-10 22:40 | — | disconnect |
| 156 | 1789080300 | 2026-09-10 22:45 | 144 | — |
| 157 | 1789080600 | 2026-09-10 22:50 | 145 | — |
| 158 | 1789080900 | 2026-09-10 22:55 | 146 | — |
| 159 | 1789081200 | 2026-09-10 23:00 | 147 | — |
| 160 | 1789081500 | 2026-09-10 23:05 | 148 | — |
| 161 | 1789081800 | 2026-09-10 23:10 | 149 | — |
| 162 | 1789082100 | 2026-09-10 23:15 | 150 | — |
| 163 | 1789082400 | 2026-09-10 23:20 | 151 | — |
| 164 | 1789082700 | 2026-09-10 23:25 | 152 | — |
| 165 | 1789083000 | 2026-09-10 23:30 | 153 | — |
| 166 | 1789083300 | 2026-09-10 23:35 | 154 | — |
| 167 | 1789083600 | 2026-09-10 23:40 | 155 | — |
| 168 | 1789083900 | 2026-09-10 23:45 | 156 | — |
| 169 | 1789084200 | 2026-09-10 23:50 | 157 | — |
| 170 | 1789084500 | 2026-09-10 23:55 | 158 | — |
| 171 | 1789084800 | 2026-09-11 00:00 | 159 | — |
| 172 | 1789085100 | 2026-09-11 00:05 | 160 | — |
| 173 | 1789085400 | 2026-09-11 00:10 | — | disconnect |
| 174 | 1789085700 | 2026-09-11 00:15 | — | disconnect |
| 175 | 1789086000 | 2026-09-11 00:20 | 161 | — |
| 176 | 1789086300 | 2026-09-11 00:25 | 162 | — |
| 177 | 1789086600 | 2026-09-11 00:30 | 163 | — |
| 178 | 1789086900 | 2026-09-11 00:35 | 164 | — |
| 179 | 1789087200 | 2026-09-11 00:40 | 165 | — |
| 180 | 1789087500 | 2026-09-11 00:45 | 166 | — |
| 181 | 1789087800 | 2026-09-11 00:50 | 167 | — |
| 182 | 1789088100 | 2026-09-11 00:55 | 168 | — |
| 183 | 1789088400 | 2026-09-11 01:00 | 169 | — |
| 184 | 1789088700 | 2026-09-11 01:05 | 170 | — |
| 185 | 1789089000 | 2026-09-11 01:10 | — | disconnect |
| 186 | 1789089300 | 2026-09-11 01:15 | — | disconnect |
| 187 | 1789089600 | 2026-09-11 01:20 | 171 | — |
| 188 | 1789089900 | 2026-09-11 01:25 | 172 | — |
| 189 | 1789090200 | 2026-09-11 01:30 | 173 | — |
| 190 | 1789090500 | 2026-09-11 01:35 | 174 | — |
| 191 | 1789090800 | 2026-09-11 01:40 | 175 | — |
| 192 | 1789091100 | 2026-09-11 01:45 | 176 | — |
| 193 | 1789091400 | 2026-09-11 01:50 | — | disconnect |
| 194 | 1789091700 | 2026-09-11 01:55 | — | disconnect |
| 195 | 1789092000 | 2026-09-11 02:00 | 177 | — |
| 196 | 1789092300 | 2026-09-11 02:05 | 178 | — |
| 197 | 1789092600 | 2026-09-11 02:10 | 179 | — |
| 198 | 1789092900 | 2026-09-11 02:15 | 180 | — |
| 199 | 1789093200 | 2026-09-11 02:20 | 181 | — |
| 200 | 1789093500 | 2026-09-11 02:25 | 182 | — |
| 201 | 1789093800 | 2026-09-11 02:30 | 183 | — |
| 202 | 1789094100 | 2026-09-11 02:35 | 184 | — |
| 203 | 1789094400 | 2026-09-11 02:40 | 185 | — |
| 204 | 1789094700 | 2026-09-11 02:45 | 186 | — |
| 205 | 1789095000 | 2026-09-11 02:50 | 187 | — |
| 206 | 1789095300 | 2026-09-11 02:55 | 188 | — |
| 207 | 1789095600 | 2026-09-11 03:00 | 189 | — |
| 208 | 1789095900 | 2026-09-11 03:05 | 190 | — |
| 209 | 1789096200 | 2026-09-11 03:10 | 191 | — |
| 210 | 1789096500 | 2026-09-11 03:15 | 192 | — |
| 211 | 1789096800 | 2026-09-11 03:20 | 193 | — |
| 212 | 1789097100 | 2026-09-11 03:25 | 194 | — |
| 213 | 1789097400 | 2026-09-11 03:30 | 195 | — |
| 214 | 1789097700 | 2026-09-11 03:35 | 196 | — |
| 215 | 1789098000 | 2026-09-11 03:40 | 197 | — |
| 216 | 1789098300 | 2026-09-11 03:45 | 198 | — |
| 217 | 1789098600 | 2026-09-11 03:50 | — | disconnect |
| 218 | 1789098900 | 2026-09-11 03:55 | — | disconnect |
| 219 | 1789099200 | 2026-09-11 04:00 | 199 | — |
| 220 | 1789099500 | 2026-09-11 04:05 | 200 | — |
| 221 | 1789099800 | 2026-09-11 04:10 | 201 | — |
| 222 | 1789100100 | 2026-09-11 04:15 | 202 | — |
| 223 | 1789100400 | 2026-09-11 04:20 | 203 | — |
| 224 | 1789100700 | 2026-09-11 04:25 | 204 | — |
| 225 | 1789101000 | 2026-09-11 04:30 | 205 | — |
| 226 | 1789101300 | 2026-09-11 04:35 | 206 | — |
| 227 | 1789101600 | 2026-09-11 04:40 | 207 | — |
| 228 | 1789101900 | 2026-09-11 04:45 | 208 | — |
| 229 | 1789102200 | 2026-09-11 04:50 | — | disconnect |
| 230 | 1789102500 | 2026-09-11 04:55 | 209 | — |
| 231 | 1789102800 | 2026-09-11 05:00 | 210 | — |
| 232 | 1789103100 | 2026-09-11 05:05 | 211 | — |
| 233 | 1789103400 | 2026-09-11 05:10 | 212 | — |
| 234 | 1789103700 | 2026-09-11 05:15 | 213 | — |
| 235 | 1789104000 | 2026-09-11 05:20 | 214 | — |
| 236 | 1789104300 | 2026-09-11 05:25 | 215 | — |
| 237 | 1789104600 | 2026-09-11 05:30 | 216 | — |
| 238 | 1789104900 | 2026-09-11 05:35 | 217 | — |
| 239 | 1789105200 | 2026-09-11 05:40 | 218 | — |
| 240 | 1789105500 | 2026-09-11 05:45 | 219 | — |
| 241 | 1789105800 | 2026-09-11 05:50 | 220 | — |
| 242 | 1789106100 | 2026-09-11 05:55 | 221 | — |
| 243 | 1789106400 | 2026-09-11 06:00 | 222 | — |
| 244 | 1789106700 | 2026-09-11 06:05 | 223 | — |
| 245 | 1789107000 | 2026-09-11 06:10 | 224 | — |
| 246 | 1789107300 | 2026-09-11 06:15 | — | disconnect |
| 247 | 1789107600 | 2026-09-11 06:20 | — | disconnect |
| 248 | 1789107900 | 2026-09-11 06:25 | 225 | — |
| 249 | 1789108200 | 2026-09-11 06:30 | 226 | — |
| 250 | 1789108500 | 2026-09-11 06:35 | 227 | — |
| 251 | 1789108800 | 2026-09-11 06:40 | 228 | — |
| 252 | 1789109100 | 2026-09-11 06:45 | 229 | — |
| 253 | 1789109400 | 2026-09-11 06:50 | 230 | — |
| 254 | 1789109700 | 2026-09-11 06:55 | 231 | — |
| 255 | 1789110000 | 2026-09-11 07:00 | 232 | — |
| 256 | 1789110300 | 2026-09-11 07:05 | 233 | — |
| 257 | 1789110600 | 2026-09-11 07:10 | 234 | — |
| 258 | 1789110900 | 2026-09-11 07:15 | 235 | — |
| 259 | 1789111200 | 2026-09-11 07:20 | 236 | — |
| 260 | 1789111500 | 2026-09-11 07:25 | 237 | — |
| 261 | 1789111800 | 2026-09-11 07:30 | 238 | — |
| 262 | 1789112100 | 2026-09-11 07:35 | 239 | — |
| 263 | 1789112400 | 2026-09-11 07:40 | 240 | — |
| 264 | 1789112700 | 2026-09-11 07:45 | 241 | — |
| 265 | 1789113000 | 2026-09-11 07:50 | 242 | — |
| 266 | 1789113300 | 2026-09-11 07:55 | 243 | — |
| 267 | 1789113600 | 2026-09-11 08:00 | 244 | — |
| 268 | 1789113900 | 2026-09-11 08:05 | 245 | — |
| 269 | 1789114200 | 2026-09-11 08:10 | 246 | — |
| 270 | 1789114500 | 2026-09-11 08:15 | — | disconnect |
| 271 | 1789114800 | 2026-09-11 08:20 | — | disconnect |
| 272 | 1789115100 | 2026-09-11 08:25 | 247 | — |
| 273 | 1789115400 | 2026-09-11 08:30 | 248 | — |
| 274 | 1789115700 | 2026-09-11 08:35 | 249 | — |
| 275 | 1789116000 | 2026-09-11 08:40 | 250 | — |
| 276 | 1789116300 | 2026-09-11 08:45 | 251 | — |
| 277 | 1789116600 | 2026-09-11 08:50 | 252 | — |
| 278 | 1789116900 | 2026-09-11 08:55 | 253 | — |
| 279 | 1789117200 | 2026-09-11 09:00 | 254 | — |
| 280 | 1789117500 | 2026-09-11 09:05 | 255 | — |
| 281 | 1789117800 | 2026-09-11 09:10 | 256 | — |
| 282 | 1789118100 | 2026-09-11 09:15 | 257 | — |
| 283 | 1789118400 | 2026-09-11 09:20 | 258 | — |
| 284 | 1789118700 | 2026-09-11 09:25 | 259 | — |
| 285 | 1789119000 | 2026-09-11 09:30 | 260 | — |
| 286 | 1789119300 | 2026-09-11 09:35 | 261 | — |
| 287 | 1789119600 | 2026-09-11 09:40 | 262 | — |
| 288 | 1789119900 | 2026-09-11 09:45 | 263 | — |
| 289 | 1789120200 | 2026-09-11 09:50 | 264 | — |
| 290 | 1789120500 | 2026-09-11 09:55 | 265 | — |
| 291 | 1789120800 | 2026-09-11 10:00 | 266 | — |
| 292 | 1789121100 | 2026-09-11 10:05 | 267 | — |
| 293 | 1789121400 | 2026-09-11 10:10 | 268 | — |
| 294 | 1789121700 | 2026-09-11 10:15 | — | disconnect |
| 295 | 1789122000 | 2026-09-11 10:20 | — | disconnect |
| 296 | 1789122300 | 2026-09-11 10:25 | 269 | — |
| 297 | 1789122600 | 2026-09-11 10:30 | 270 | — |
| 298 | 1789122900 | 2026-09-11 10:35 | 271 | — |
| 299 | 1789123200 | 2026-09-11 10:40 | 272 | — |
| 300 | 1789123500 | 2026-09-11 10:45 | 273 | — |
| 301 | 1789123800 | 2026-09-11 10:50 | 274 | — |
| 302 | 1789124100 | 2026-09-11 10:55 | 275 | — |
| 303 | 1789124400 | 2026-09-11 11:00 | 276 | — |
| 304 | 1789124700 | 2026-09-11 11:05 | 277 | — |
| 305 | 1789125000 | 2026-09-11 11:10 | 278 | — |
| 306 | 1789125300 | 2026-09-11 11:15 | 279 | — |
| 307 | 1789125600 | 2026-09-11 11:20 | 280 | — |
| 308 | 1789125900 | 2026-09-11 11:25 | 281 | — |
| 309 | 1789126200 | 2026-09-11 11:30 | 282 | — |
| 310 | 1789126500 | 2026-09-11 11:35 | 283 | — |
| 311 | 1789126800 | 2026-09-11 11:40 | 284 | — |
| 312 | 1789127100 | 2026-09-11 11:45 | 285 | — |
| 313 | 1789127400 | 2026-09-11 11:50 | 286 | — |
| 314 | 1789127700 | 2026-09-11 11:55 | — | disconnect |
| 315 | 1789128000 | 2026-09-11 12:00 | — | disconnect |
| 316 | 1789128300 | 2026-09-11 12:05 | 287 | — |
| 317 | 1789128600 | 2026-09-11 12:10 | 288 | — |
| 318 | 1789128900 | 2026-09-11 12:15 | 289 | — |
| 319 | 1789129200 | 2026-09-11 12:20 | 290 | — |
| 320 | 1789129500 | 2026-09-11 12:25 | 291 | — |
| 321 | 1789129800 | 2026-09-11 12:30 | 292 | — |
| 322 | 1789130100 | 2026-09-11 12:35 | 293 | — |
| 323 | 1789130400 | 2026-09-11 12:40 | 294 | — |
| 324 | 1789130700 | 2026-09-11 12:45 | — | disconnect |
| 325 | 1789131000 | 2026-09-11 12:50 | — | disconnect |
| 326 | 1789131300 | 2026-09-11 12:55 | — | disconnect |
| 327 | 1789131600 | 2026-09-11 13:00 | 295 | — |
| 328 | 1789131900 | 2026-09-11 13:05 | 296 | — |
| 329 | 1789132200 | 2026-09-11 13:10 | 297 | — |
| 330 | 1789132500 | 2026-09-11 13:15 | 298 | — |
| 331 | 1789132800 | 2026-09-11 13:20 | 299 | — |
| 332 | 1789133100 | 2026-09-11 13:25 | 300 | — |
| 333 | 1789133400 | 2026-09-11 13:30 | 301 | — |
| 334 | 1789133700 | 2026-09-11 13:35 | 302 | — |
| 335 | 1789134000 | 2026-09-11 13:40 | 303 | — |
| 336 | 1789134300 | 2026-09-11 13:45 | 304 | — |
| 337 | 1789134600 | 2026-09-11 13:50 | 305 | — |
| 338 | 1789134900 | 2026-09-11 13:55 | 306 | — |
| 339 | 1789135200 | 2026-09-11 14:00 | 307 | — |
| 340 | 1789135500 | 2026-09-11 14:05 | 308 | — |
| 341 | 1789135800 | 2026-09-11 14:10 | 309 | — |
| 342 | 1789136100 | 2026-09-11 14:15 | 310 | — |
| 343 | 1789136400 | 2026-09-11 14:20 | 311 | — |
| 344 | 1789136700 | 2026-09-11 14:25 | 312 | — |
| 345 | 1789137000 | 2026-09-11 14:30 | 313 | — |
| 346 | 1789137300 | 2026-09-11 14:35 | 314 | — |
| 347 | 1789137600 | 2026-09-11 14:40 | 315 | — |
| 348 | 1789137900 | 2026-09-11 14:45 | 316 | — |
| 349 | 1789138200 | 2026-09-11 14:50 | — | disconnect |
| 350 | 1789138500 | 2026-09-11 14:55 | — | disconnect |
| 351 | 1789138800 | 2026-09-11 15:00 | 317 | — |
| 352 | 1789139100 | 2026-09-11 15:05 | 318 | — |
| 353 | 1789139400 | 2026-09-11 15:10 | 319 | — |
| 354 | 1789139700 | 2026-09-11 15:15 | 320 | — |
| 355 | 1789140000 | 2026-09-11 15:20 | 321 | — |
| 356 | 1789140300 | 2026-09-11 15:25 | 322 | — |
| 357 | 1789140600 | 2026-09-11 15:30 | 323 | — |
| 358 | 1789140900 | 2026-09-11 15:35 | 324 | — |
| 359 | 1789141200 | 2026-09-11 15:40 | — | disconnect |
| 360 | 1789141500 | 2026-09-11 15:45 | — | disconnect |
| 361 | 1789141800 | 2026-09-11 15:50 | 325 | — |
| 362 | 1789142100 | 2026-09-11 15:55 | 326 | — |
| 363 | 1789142400 | 2026-09-11 16:00 | 327 | — |
| 364 | 1789142700 | 2026-09-11 16:05 | 328 | — |
| 365 | 1789143000 | 2026-09-11 16:10 | 329 | — |
| 366 | 1789143300 | 2026-09-11 16:15 | 330 | — |
| 367 | 1789143600 | 2026-09-11 16:20 | 331 | — |
| 368 | 1789143900 | 2026-09-11 16:25 | 332 | — |
| 369 | 1789144200 | 2026-09-11 16:30 | 333 | — |
| 370 | 1789144500 | 2026-09-11 16:35 | 334 | — |
| 371 | 1789144800 | 2026-09-11 16:40 | 335 | — |
| 372 | 1789145100 | 2026-09-11 16:45 | 336 | — |
| 373 | 1789145400 | 2026-09-11 16:50 | 337 | — |
| 374 | 1789145700 | 2026-09-11 16:55 | 338 | — |
| 375 | 1789146000 | 2026-09-11 17:00 | 339 | — |
| 376 | 1789146300 | 2026-09-11 17:05 | 340 | — |
| 377 | 1789146600 | 2026-09-11 17:10 | 341 | — |
| 378 | 1789146900 | 2026-09-11 17:15 | 342 | — |
| 379 | 1789147200 | 2026-09-11 17:20 | 343 | — |
| 380 | 1789147500 | 2026-09-11 17:25 | 344 | — |
| 381 | 1789147800 | 2026-09-11 17:30 | 345 | — |
| 382 | 1789148100 | 2026-09-11 17:35 | 346 | — |
| 383 | 1789148400 | 2026-09-11 17:40 | — | disconnect |
| 384 | 1789148700 | 2026-09-11 17:45 | — | disconnect |
| 385 | 1789149000 | 2026-09-11 17:50 | 347 | — |
| 386 | 1789149300 | 2026-09-11 17:55 | 348 | — |
| 387 | 1789149600 | 2026-09-11 18:00 | 349 | — |
| 388 | 1789149900 | 2026-09-11 18:05 | 350 | — |
| 389 | 1789150200 | 2026-09-11 18:10 | 351 | — |
| 390 | 1789150500 | 2026-09-11 18:15 | 352 | — |
| 391 | 1789150800 | 2026-09-11 18:20 | 353 | — |
| 392 | 1789151100 | 2026-09-11 18:25 | 354 | — |
| 393 | 1789151400 | 2026-09-11 18:30 | 355 | — |
| 394 | 1789151700 | 2026-09-11 18:35 | 356 | — |
| 395 | 1789152000 | 2026-09-11 18:40 | 357 | — |
| 396 | 1789152300 | 2026-09-11 18:45 | 358 | — |
| 397 | 1789152600 | 2026-09-11 18:50 | 359 | — |
| 398 | 1789152900 | 2026-09-11 18:55 | 360 | — |
| 399 | 1789153200 | 2026-09-11 19:00 | — | disconnect |
| 400 | 1789153500 | 2026-09-11 19:05 | — | disconnect |
| 401 | 1789153800 | 2026-09-11 19:10 | 361 | — |
| 402 | 1789154100 | 2026-09-11 19:15 | 362 | — |
| 403 | 1789154400 | 2026-09-11 19:20 | 363 | — |
| 404 | 1789154700 | 2026-09-11 19:25 | 364 | — |
| 405 | 1789155000 | 2026-09-11 19:30 | 365 | — |
| 406 | 1789155300 | 2026-09-11 19:35 | 366 | — |
| 407 | 1789155600 | 2026-09-11 19:40 | 367 | — |
| 408 | 1789155900 | 2026-09-11 19:45 | 368 | — |
| 409 | 1789156200 | 2026-09-11 19:50 | 369 | — |
| 410 | 1789156500 | 2026-09-11 19:55 | 370 | — |
| 411 | 1789156800 | 2026-09-11 20:00 | 371 | — |
| 412 | 1789157100 | 2026-09-11 20:05 | 372 | — |
| 413 | 1789157400 | 2026-09-11 20:10 | 373 | — |
| 414 | 1789157700 | 2026-09-11 20:15 | 374 | — |
| 415 | 1789158000 | 2026-09-11 20:20 | 375 | — |
| 416 | 1789158300 | 2026-09-11 20:25 | 376 | — |
| 417 | 1789158600 | 2026-09-11 20:30 | 377 | — |
| 418 | 1789158900 | 2026-09-11 20:35 | 378 | — |
| 419 | 1789159200 | 2026-09-11 20:40 | 379 | — |
| 420 | 1789159500 | 2026-09-11 20:45 | 380 | — |
| 421 | 1789159800 | 2026-09-11 20:50 | 381 | — |
| 422 | 1789160100 | 2026-09-11 20:55 | 382 | — |
| 423 | 1789160400 | 2026-09-11 21:00 | — | disconnect |
| 424 | 1789160700 | 2026-09-11 21:05 | — | disconnect |
| 425 | 1789161000 | 2026-09-11 21:10 | 383 | — |
| 426 | 1789161300 | 2026-09-11 21:15 | 384 | — |
| 427 | 1789161600 | 2026-09-11 21:20 | 385 | — |
| 428 | 1789161900 | 2026-09-11 21:25 | 386 | — |
| 429 | 1789162200 | 2026-09-11 21:30 | — | disconnect |
| 430 | 1789162500 | 2026-09-11 21:35 | 387 | — |
| 431 | 1789162800 | 2026-09-11 21:40 | 388 | — |
| 432 | 1789163100 | 2026-09-11 21:45 | 389 | — |
| 433 | 1789163400 | 2026-09-11 21:50 | 390 | — |
| 434 | 1789163700 | 2026-09-11 21:55 | 391 | — |
| 435 | 1789164000 | 2026-09-11 22:00 | 392 | — |
| 436 | 1789164300 | 2026-09-11 22:05 | 393 | — |
| 437 | 1789164600 | 2026-09-11 22:10 | 394 | — |
| 438 | 1789164900 | 2026-09-11 22:15 | 395 | — |
| 439 | 1789165200 | 2026-09-11 22:20 | 396 | — |
| 440 | 1789165500 | 2026-09-11 22:25 | 397 | — |
| 441 | 1789165800 | 2026-09-11 22:30 | 398 | — |
| 442 | 1789166100 | 2026-09-11 22:35 | 399 | — |
| 443 | 1789166400 | 2026-09-11 22:40 | 400 | — |

#### The test-1 walk

| # | T0 | open (UTC) | member | reason not a member |
|---|---|---|---|---|
| 1 | 1789166700 | 2026-09-11 22:45 | 1 | — |
| 2 | 1789167000 | 2026-09-11 22:50 | 2 | — |
| 3 | 1789167300 | 2026-09-11 22:55 | 3 | — |
| 4 | 1789167600 | 2026-09-11 23:00 | 4 | — |
| 5 | 1789167900 | 2026-09-11 23:05 | 5 | — |
| 6 | 1789168200 | 2026-09-11 23:10 | 6 | — |
| 7 | 1789168500 | 2026-09-11 23:15 | 7 | — |
| 8 | 1789168800 | 2026-09-11 23:20 | 8 | — |
| 9 | 1789169100 | 2026-09-11 23:25 | 9 | — |
| 10 | 1789169400 | 2026-09-11 23:30 | — | disconnect |
| 11 | 1789169700 | 2026-09-11 23:35 | 10 | — |
| 12 | 1789170000 | 2026-09-11 23:40 | — | disconnect |
| 13 | 1789170300 | 2026-09-11 23:45 | — | disconnect |
| 14 | 1789170600 | 2026-09-11 23:50 | 11 | — |
| 15 | 1789170900 | 2026-09-11 23:55 | 12 | — |
| 16 | 1789171200 | 2026-09-12 00:00 | 13 | — |
| 17 | 1789171500 | 2026-09-12 00:05 | 14 | — |
| 18 | 1789171800 | 2026-09-12 00:10 | 15 | — |
| 19 | 1789172100 | 2026-09-12 00:15 | 16 | — |
| 20 | 1789172400 | 2026-09-12 00:20 | 17 | — |
| 21 | 1789172700 | 2026-09-12 00:25 | 18 | — |
| 22 | 1789173000 | 2026-09-12 00:30 | 19 | — |
| 23 | 1789173300 | 2026-09-12 00:35 | 20 | — |
| 24 | 1789173600 | 2026-09-12 00:40 | 21 | — |
| 25 | 1789173900 | 2026-09-12 00:45 | 22 | — |
| 26 | 1789174200 | 2026-09-12 00:50 | 23 | — |
| 27 | 1789174500 | 2026-09-12 00:55 | 24 | — |
| 28 | 1789174800 | 2026-09-12 01:00 | 25 | — |
| 29 | 1789175100 | 2026-09-12 01:05 | 26 | — |
| 30 | 1789175400 | 2026-09-12 01:10 | 27 | — |
| 31 | 1789175700 | 2026-09-12 01:15 | 28 | — |
| 32 | 1789176000 | 2026-09-12 01:20 | 29 | — |
| 33 | 1789176300 | 2026-09-12 01:25 | 30 | — |
| 34 | 1789176600 | 2026-09-12 01:30 | 31 | — |
| 35 | 1789176900 | 2026-09-12 01:35 | 32 | — |
| 36 | 1789177200 | 2026-09-12 01:40 | — | disconnect |
| 37 | 1789177500 | 2026-09-12 01:45 | — | disconnect |
| 38 | 1789177800 | 2026-09-12 01:50 | 33 | — |
| 39 | 1789178100 | 2026-09-12 01:55 | 34 | — |
| 40 | 1789178400 | 2026-09-12 02:00 | 35 | — |
| 41 | 1789178700 | 2026-09-12 02:05 | 36 | — |
| 42 | 1789179000 | 2026-09-12 02:10 | 37 | — |
| 43 | 1789179300 | 2026-09-12 02:15 | 38 | — |
| 44 | 1789179600 | 2026-09-12 02:20 | 39 | — |
| 45 | 1789179900 | 2026-09-12 02:25 | 40 | — |
| 46 | 1789180200 | 2026-09-12 02:30 | 41 | — |
| 47 | 1789180500 | 2026-09-12 02:35 | 42 | — |
| 48 | 1789180800 | 2026-09-12 02:40 | 43 | — |
| 49 | 1789181100 | 2026-09-12 02:45 | 44 | — |
| 50 | 1789181400 | 2026-09-12 02:50 | 45 | — |
| 51 | 1789181700 | 2026-09-12 02:55 | 46 | — |
| 52 | 1789182000 | 2026-09-12 03:00 | 47 | — |
| 53 | 1789182300 | 2026-09-12 03:05 | 48 | — |
| 54 | 1789182600 | 2026-09-12 03:10 | 49 | — |
| 55 | 1789182900 | 2026-09-12 03:15 | 50 | — |
| 56 | 1789183200 | 2026-09-12 03:20 | 51 | — |
| 57 | 1789183500 | 2026-09-12 03:25 | 52 | — |
| 58 | 1789183800 | 2026-09-12 03:30 | 53 | — |
| 59 | 1789184100 | 2026-09-12 03:35 | 54 | — |
| 60 | 1789184400 | 2026-09-12 03:40 | — | disconnect |
| 61 | 1789184700 | 2026-09-12 03:45 | — | disconnect |
| 62 | 1789185000 | 2026-09-12 03:50 | 55 | — |
| 63 | 1789185300 | 2026-09-12 03:55 | 56 | — |
| 64 | 1789185600 | 2026-09-12 04:00 | 57 | — |
| 65 | 1789185900 | 2026-09-12 04:05 | 58 | — |
| 66 | 1789186200 | 2026-09-12 04:10 | 59 | — |
| 67 | 1789186500 | 2026-09-12 04:15 | 60 | — |
| 68 | 1789186800 | 2026-09-12 04:20 | 61 | — |
| 69 | 1789187100 | 2026-09-12 04:25 | — | disconnect |
| 70 | 1789187400 | 2026-09-12 04:30 | — | disconnect |
| 71 | 1789187700 | 2026-09-12 04:35 | 62 | — |
| 72 | 1789188000 | 2026-09-12 04:40 | 63 | — |
| 73 | 1789188300 | 2026-09-12 04:45 | 64 | — |
| 74 | 1789188600 | 2026-09-12 04:50 | 65 | — |
| 75 | 1789188900 | 2026-09-12 04:55 | 66 | — |
| 76 | 1789189200 | 2026-09-12 05:00 | 67 | — |
| 77 | 1789189500 | 2026-09-12 05:05 | 68 | — |
| 78 | 1789189800 | 2026-09-12 05:10 | 69 | — |
| 79 | 1789190100 | 2026-09-12 05:15 | 70 | — |
| 80 | 1789190400 | 2026-09-12 05:20 | 71 | — |
| 81 | 1789190700 | 2026-09-12 05:25 | 72 | — |
| 82 | 1789191000 | 2026-09-12 05:30 | 73 | — |
| 83 | 1789191300 | 2026-09-12 05:35 | 74 | — |
| 84 | 1789191600 | 2026-09-12 05:40 | 75 | — |
| 85 | 1789191900 | 2026-09-12 05:45 | 76 | — |
| 86 | 1789192200 | 2026-09-12 05:50 | 77 | — |
| 87 | 1789192500 | 2026-09-12 05:55 | 78 | — |
| 88 | 1789192800 | 2026-09-12 06:00 | 79 | — |
| 89 | 1789193100 | 2026-09-12 06:05 | 80 | — |
| 90 | 1789193400 | 2026-09-12 06:10 | 81 | — |
| 91 | 1789193700 | 2026-09-12 06:15 | 82 | — |
| 92 | 1789194000 | 2026-09-12 06:20 | 83 | — |
| 93 | 1789194300 | 2026-09-12 06:25 | — | disconnect |
| 94 | 1789194600 | 2026-09-12 06:30 | — | disconnect |
| 95 | 1789194900 | 2026-09-12 06:35 | 84 | — |
| 96 | 1789195200 | 2026-09-12 06:40 | 85 | — |
| 97 | 1789195500 | 2026-09-12 06:45 | 86 | — |
| 98 | 1789195800 | 2026-09-12 06:50 | 87 | — |
| 99 | 1789196100 | 2026-09-12 06:55 | 88 | — |
| 100 | 1789196400 | 2026-09-12 07:00 | 89 | — |
| 101 | 1789196700 | 2026-09-12 07:05 | — | disconnect |
| 102 | 1789197000 | 2026-09-12 07:10 | 90 | — |
| 103 | 1789197300 | 2026-09-12 07:15 | 91 | — |
| 104 | 1789197600 | 2026-09-12 07:20 | 92 | — |
| 105 | 1789197900 | 2026-09-12 07:25 | 93 | — |
| 106 | 1789198200 | 2026-09-12 07:30 | 94 | — |
| 107 | 1789198500 | 2026-09-12 07:35 | 95 | — |
| 108 | 1789198800 | 2026-09-12 07:40 | 96 | — |
| 109 | 1789199100 | 2026-09-12 07:45 | 97 | — |
| 110 | 1789199400 | 2026-09-12 07:50 | 98 | — |
| 111 | 1789199700 | 2026-09-12 07:55 | 99 | — |
| 112 | 1789200000 | 2026-09-12 08:00 | — | disconnect |
| 113 | 1789200300 | 2026-09-12 08:05 | 100 | — |
| 114 | 1789200600 | 2026-09-12 08:10 | 101 | — |
| 115 | 1789200900 | 2026-09-12 08:15 | 102 | — |
| 116 | 1789201200 | 2026-09-12 08:20 | 103 | — |
| 117 | 1789201500 | 2026-09-12 08:25 | 104 | — |
| 118 | 1789201800 | 2026-09-12 08:30 | 105 | — |
| 119 | 1789202100 | 2026-09-12 08:35 | 106 | — |
| 120 | 1789202400 | 2026-09-12 08:40 | 107 | — |
| 121 | 1789202700 | 2026-09-12 08:45 | 108 | — |
| 122 | 1789203000 | 2026-09-12 08:50 | 109 | — |
| 123 | 1789203300 | 2026-09-12 08:55 | 110 | — |
| 124 | 1789203600 | 2026-09-12 09:00 | 111 | — |
| 125 | 1789203900 | 2026-09-12 09:05 | 112 | — |
| 126 | 1789204200 | 2026-09-12 09:10 | 113 | — |
| 127 | 1789204500 | 2026-09-12 09:15 | 114 | — |
| 128 | 1789204800 | 2026-09-12 09:20 | 115 | — |
| 129 | 1789205100 | 2026-09-12 09:25 | 116 | — |
| 130 | 1789205400 | 2026-09-12 09:30 | 117 | — |
| 131 | 1789205700 | 2026-09-12 09:35 | 118 | — |
| 132 | 1789206000 | 2026-09-12 09:40 | 119 | — |
| 133 | 1789206300 | 2026-09-12 09:45 | 120 | — |
| 134 | 1789206600 | 2026-09-12 09:50 | — | disconnect |
| 135 | 1789206900 | 2026-09-12 09:55 | 121 | — |
| 136 | 1789207200 | 2026-09-12 10:00 | 122 | — |
| 137 | 1789207500 | 2026-09-12 10:05 | 123 | — |
| 138 | 1789207800 | 2026-09-12 10:10 | 124 | — |
| 139 | 1789208100 | 2026-09-12 10:15 | 125 | — |
| 140 | 1789208400 | 2026-09-12 10:20 | 126 | — |
| 141 | 1789208700 | 2026-09-12 10:25 | 127 | — |
| 142 | 1789209000 | 2026-09-12 10:30 | 128 | — |
| 143 | 1789209300 | 2026-09-12 10:35 | 129 | — |
| 144 | 1789209600 | 2026-09-12 10:40 | 130 | — |
| 145 | 1789209900 | 2026-09-12 10:45 | 131 | — |
| 146 | 1789210200 | 2026-09-12 10:50 | 132 | — |
| 147 | 1789210500 | 2026-09-12 10:55 | 133 | — |
| 148 | 1789210800 | 2026-09-12 11:00 | 134 | — |
| 149 | 1789211100 | 2026-09-12 11:05 | 135 | — |
| 150 | 1789211400 | 2026-09-12 11:10 | 136 | — |
| 151 | 1789211700 | 2026-09-12 11:15 | 137 | — |
| 152 | 1789212000 | 2026-09-12 11:20 | 138 | — |
| 153 | 1789212300 | 2026-09-12 11:25 | 139 | — |
| 154 | 1789212600 | 2026-09-12 11:30 | 140 | — |
| 155 | 1789212900 | 2026-09-12 11:35 | 141 | — |
| 156 | 1789213200 | 2026-09-12 11:40 | 142 | — |
| 157 | 1789213500 | 2026-09-12 11:45 | 143 | — |
| 158 | 1789213800 | 2026-09-12 11:50 | — | disconnect |
| 159 | 1789214100 | 2026-09-12 11:55 | 144 | — |
| 160 | 1789214400 | 2026-09-12 12:00 | 145 | — |
| 161 | 1789214700 | 2026-09-12 12:05 | 146 | — |
| 162 | 1789215000 | 2026-09-12 12:10 | 147 | — |
| 163 | 1789215300 | 2026-09-12 12:15 | 148 | — |
| 164 | 1789215600 | 2026-09-12 12:20 | 149 | — |
| 165 | 1789215900 | 2026-09-12 12:25 | 150 | — |
| 166 | 1789216200 | 2026-09-12 12:30 | 151 | — |
| 167 | 1789216500 | 2026-09-12 12:35 | 152 | — |
| 168 | 1789216800 | 2026-09-12 12:40 | 153 | — |
| 169 | 1789217100 | 2026-09-12 12:45 | 154 | — |
| 170 | 1789217400 | 2026-09-12 12:50 | 155 | — |
| 171 | 1789217700 | 2026-09-12 12:55 | 156 | — |
| 172 | 1789218000 | 2026-09-12 13:00 | 157 | — |
| 173 | 1789218300 | 2026-09-12 13:05 | 158 | — |
| 174 | 1789218600 | 2026-09-12 13:10 | 159 | — |
| 175 | 1789218900 | 2026-09-12 13:15 | 160 | — |
| 176 | 1789219200 | 2026-09-12 13:20 | 161 | — |
| 177 | 1789219500 | 2026-09-12 13:25 | 162 | — |
| 178 | 1789219800 | 2026-09-12 13:30 | 163 | — |
| 179 | 1789220100 | 2026-09-12 13:35 | 164 | — |
| 180 | 1789220400 | 2026-09-12 13:40 | 165 | — |
| 181 | 1789220700 | 2026-09-12 13:45 | 166 | — |
| 182 | 1789221000 | 2026-09-12 13:50 | — | disconnect |
| 183 | 1789221300 | 2026-09-12 13:55 | 167 | — |
| 184 | 1789221600 | 2026-09-12 14:00 | 168 | — |
| 185 | 1789221900 | 2026-09-12 14:05 | 169 | — |
| 186 | 1789222200 | 2026-09-12 14:10 | 170 | — |
| 187 | 1789222500 | 2026-09-12 14:15 | 171 | — |
| 188 | 1789222800 | 2026-09-12 14:20 | 172 | — |
| 189 | 1789223100 | 2026-09-12 14:25 | — | disconnect |
| 190 | 1789223400 | 2026-09-12 14:30 | — | disconnect |
| 191 | 1789223700 | 2026-09-12 14:35 | 173 | — |
| 192 | 1789224000 | 2026-09-12 14:40 | 174 | — |
| 193 | 1789224300 | 2026-09-12 14:45 | 175 | — |
| 194 | 1789224600 | 2026-09-12 14:50 | 176 | — |
| 195 | 1789224900 | 2026-09-12 14:55 | 177 | — |
| 196 | 1789225200 | 2026-09-12 15:00 | 178 | — |
| 197 | 1789225500 | 2026-09-12 15:05 | 179 | — |
| 198 | 1789225800 | 2026-09-12 15:10 | 180 | — |
| 199 | 1789226100 | 2026-09-12 15:15 | 181 | — |
| 200 | 1789226400 | 2026-09-12 15:20 | 182 | — |
| 201 | 1789226700 | 2026-09-12 15:25 | 183 | — |
| 202 | 1789227000 | 2026-09-12 15:30 | 184 | — |
| 203 | 1789227300 | 2026-09-12 15:35 | 185 | — |
| 204 | 1789227600 | 2026-09-12 15:40 | 186 | — |
| 205 | 1789227900 | 2026-09-12 15:45 | 187 | — |
| 206 | 1789228200 | 2026-09-12 15:50 | 188 | — |
| 207 | 1789228500 | 2026-09-12 15:55 | 189 | — |
| 208 | 1789228800 | 2026-09-12 16:00 | 190 | — |
| 209 | 1789229100 | 2026-09-12 16:05 | 191 | — |
| 210 | 1789229400 | 2026-09-12 16:10 | 192 | — |
| 211 | 1789229700 | 2026-09-12 16:15 | 193 | — |
| 212 | 1789230000 | 2026-09-12 16:20 | 194 | — |
| 213 | 1789230300 | 2026-09-12 16:25 | — | disconnect |
| 214 | 1789230600 | 2026-09-12 16:30 | — | disconnect |
| 215 | 1789230900 | 2026-09-12 16:35 | 195 | — |
| 216 | 1789231200 | 2026-09-12 16:40 | 196 | — |
| 217 | 1789231500 | 2026-09-12 16:45 | 197 | — |
| 218 | 1789231800 | 2026-09-12 16:50 | 198 | — |
| 219 | 1789232100 | 2026-09-12 16:55 | 199 | — |
| 220 | 1789232400 | 2026-09-12 17:00 | 200 | — |
| 221 | 1789232700 | 2026-09-12 17:05 | 201 | — |
| 222 | 1789233000 | 2026-09-12 17:10 | 202 | — |
| 223 | 1789233300 | 2026-09-12 17:15 | 203 | — |
| 224 | 1789233600 | 2026-09-12 17:20 | 204 | — |
| 225 | 1789233900 | 2026-09-12 17:25 | 205 | — |
| 226 | 1789234200 | 2026-09-12 17:30 | 206 | — |
| 227 | 1789234500 | 2026-09-12 17:35 | 207 | — |
| 228 | 1789234800 | 2026-09-12 17:40 | 208 | — |
| 229 | 1789235100 | 2026-09-12 17:45 | 209 | — |
| 230 | 1789235400 | 2026-09-12 17:50 | 210 | — |
| 231 | 1789235700 | 2026-09-12 17:55 | 211 | — |
| 232 | 1789236000 | 2026-09-12 18:00 | 212 | — |
| 233 | 1789236300 | 2026-09-12 18:05 | 213 | — |
| 234 | 1789236600 | 2026-09-12 18:10 | 214 | — |
| 235 | 1789236900 | 2026-09-12 18:15 | 215 | — |
| 236 | 1789237200 | 2026-09-12 18:20 | 216 | — |
| 237 | 1789237500 | 2026-09-12 18:25 | — | disconnect |
| 238 | 1789237800 | 2026-09-12 18:30 | — | disconnect |
| 239 | 1789238100 | 2026-09-12 18:35 | 217 | — |
| 240 | 1789238400 | 2026-09-12 18:40 | 218 | — |
| 241 | 1789238700 | 2026-09-12 18:45 | 219 | — |
| 242 | 1789239000 | 2026-09-12 18:50 | 220 | — |
| 243 | 1789239300 | 2026-09-12 18:55 | 221 | — |
| 244 | 1789239600 | 2026-09-12 19:00 | 222 | — |
| 245 | 1789239900 | 2026-09-12 19:05 | 223 | — |
| 246 | 1789240200 | 2026-09-12 19:10 | 224 | — |
| 247 | 1789240500 | 2026-09-12 19:15 | 225 | — |
| 248 | 1789240800 | 2026-09-12 19:20 | 226 | — |
| 249 | 1789241100 | 2026-09-12 19:25 | 227 | — |
| 250 | 1789241400 | 2026-09-12 19:30 | 228 | — |
| 251 | 1789241700 | 2026-09-12 19:35 | 229 | — |
| 252 | 1789242000 | 2026-09-12 19:40 | 230 | — |
| 253 | 1789242300 | 2026-09-12 19:45 | 231 | — |
| 254 | 1789242600 | 2026-09-12 19:50 | 232 | — |
| 255 | 1789242900 | 2026-09-12 19:55 | 233 | — |
| 256 | 1789243200 | 2026-09-12 20:00 | 234 | — |
| 257 | 1789243500 | 2026-09-12 20:05 | 235 | — |
| 258 | 1789243800 | 2026-09-12 20:10 | 236 | — |
| 259 | 1789244100 | 2026-09-12 20:15 | 237 | — |
| 260 | 1789244400 | 2026-09-12 20:20 | 238 | — |
| 261 | 1789244700 | 2026-09-12 20:25 | — | disconnect |
| 262 | 1789245000 | 2026-09-12 20:30 | — | disconnect |
| 263 | 1789245300 | 2026-09-12 20:35 | 239 | — |
| 264 | 1789245600 | 2026-09-12 20:40 | 240 | — |
| 265 | 1789245900 | 2026-09-12 20:45 | 241 | — |
| 266 | 1789246200 | 2026-09-12 20:50 | 242 | — |
| 267 | 1789246500 | 2026-09-12 20:55 | 243 | — |
| 268 | 1789246800 | 2026-09-12 21:00 | 244 | — |
| 269 | 1789247100 | 2026-09-12 21:05 | 245 | — |
| 270 | 1789247400 | 2026-09-12 21:10 | 246 | — |
| 271 | 1789247700 | 2026-09-12 21:15 | 247 | — |
| 272 | 1789248000 | 2026-09-12 21:20 | 248 | — |
| 273 | 1789248300 | 2026-09-12 21:25 | 249 | — |
| 274 | 1789248600 | 2026-09-12 21:30 | 250 | — |
| 275 | 1789248900 | 2026-09-12 21:35 | 251 | — |
| 276 | 1789249200 | 2026-09-12 21:40 | 252 | — |
| 277 | 1789249500 | 2026-09-12 21:45 | 253 | — |
| 278 | 1789249800 | 2026-09-12 21:50 | 254 | — |
| 279 | 1789250100 | 2026-09-12 21:55 | 255 | — |
| 280 | 1789250400 | 2026-09-12 22:00 | 256 | — |
| 281 | 1789250700 | 2026-09-12 22:05 | 257 | — |
| 282 | 1789251000 | 2026-09-12 22:10 | 258 | — |
| 283 | 1789251300 | 2026-09-12 22:15 | 259 | — |
| 284 | 1789251600 | 2026-09-12 22:20 | 260 | — |
| 285 | 1789251900 | 2026-09-12 22:25 | — | disconnect |
| 286 | 1789252200 | 2026-09-12 22:30 | — | disconnect |
| 287 | 1789252500 | 2026-09-12 22:35 | — | disconnect |
| 288 | 1789252800 | 2026-09-12 22:40 | 261 | — |
| 289 | 1789253100 | 2026-09-12 22:45 | 262 | — |
| 290 | 1789253400 | 2026-09-12 22:50 | 263 | — |
| 291 | 1789253700 | 2026-09-12 22:55 | 264 | — |
| 292 | 1789254000 | 2026-09-12 23:00 | 265 | — |
| 293 | 1789254300 | 2026-09-12 23:05 | 266 | — |
| 294 | 1789254600 | 2026-09-12 23:10 | 267 | — |
| 295 | 1789254900 | 2026-09-12 23:15 | 268 | — |
| 296 | 1789255200 | 2026-09-12 23:20 | 269 | — |
| 297 | 1789255500 | 2026-09-12 23:25 | 270 | — |
| 298 | 1789255800 | 2026-09-12 23:30 | 271 | — |
| 299 | 1789256100 | 2026-09-12 23:35 | 272 | — |
| 300 | 1789256400 | 2026-09-12 23:40 | 273 | — |
| 301 | 1789256700 | 2026-09-12 23:45 | 274 | — |
| 302 | 1789257000 | 2026-09-12 23:50 | 275 | — |
| 303 | 1789257300 | 2026-09-12 23:55 | 276 | — |
| 304 | 1789257600 | 2026-09-13 00:00 | 277 | — |
| 305 | 1789257900 | 2026-09-13 00:05 | 278 | — |
| 306 | 1789258200 | 2026-09-13 00:10 | 279 | — |
| 307 | 1789258500 | 2026-09-13 00:15 | 280 | — |
| 308 | 1789258800 | 2026-09-13 00:20 | 281 | — |
| 309 | 1789259100 | 2026-09-13 00:25 | 282 | — |
| 310 | 1789259400 | 2026-09-13 00:30 | 283 | — |
| 311 | 1789259700 | 2026-09-13 00:35 | — | disconnect |
| 312 | 1789260000 | 2026-09-13 00:40 | 284 | — |
| 313 | 1789260300 | 2026-09-13 00:45 | 285 | — |
| 314 | 1789260600 | 2026-09-13 00:50 | 286 | — |
| 315 | 1789260900 | 2026-09-13 00:55 | 287 | — |
| 316 | 1789261200 | 2026-09-13 01:00 | 288 | — |
| 317 | 1789261500 | 2026-09-13 01:05 | 289 | — |
| 318 | 1789261800 | 2026-09-13 01:10 | 290 | — |
| 319 | 1789262100 | 2026-09-13 01:15 | 291 | — |
| 320 | 1789262400 | 2026-09-13 01:20 | 292 | — |
| 321 | 1789262700 | 2026-09-13 01:25 | 293 | — |
| 322 | 1789263000 | 2026-09-13 01:30 | 294 | — |
| 323 | 1789263300 | 2026-09-13 01:35 | 295 | — |
| 324 | 1789263600 | 2026-09-13 01:40 | 296 | — |
| 325 | 1789263900 | 2026-09-13 01:45 | 297 | — |
| 326 | 1789264200 | 2026-09-13 01:50 | 298 | — |
| 327 | 1789264500 | 2026-09-13 01:55 | 299 | — |
| 328 | 1789264800 | 2026-09-13 02:00 | 300 | — |
| 329 | 1789265100 | 2026-09-13 02:05 | 301 | — |
| 330 | 1789265400 | 2026-09-13 02:10 | 302 | — |
| 331 | 1789265700 | 2026-09-13 02:15 | 303 | — |
| 332 | 1789266000 | 2026-09-13 02:20 | 304 | — |
| 333 | 1789266300 | 2026-09-13 02:25 | 305 | — |
| 334 | 1789266600 | 2026-09-13 02:30 | 306 | — |
| 335 | 1789266900 | 2026-09-13 02:35 | — | disconnect |
| 336 | 1789267200 | 2026-09-13 02:40 | 307 | — |
| 337 | 1789267500 | 2026-09-13 02:45 | 308 | — |
| 338 | 1789267800 | 2026-09-13 02:50 | 309 | — |
| 339 | 1789268100 | 2026-09-13 02:55 | 310 | — |
| 340 | 1789268400 | 2026-09-13 03:00 | 311 | — |
| 341 | 1789268700 | 2026-09-13 03:05 | 312 | — |
| 342 | 1789269000 | 2026-09-13 03:10 | 313 | — |
| 343 | 1789269300 | 2026-09-13 03:15 | 314 | — |
| 344 | 1789269600 | 2026-09-13 03:20 | 315 | — |
| 345 | 1789269900 | 2026-09-13 03:25 | 316 | — |
| 346 | 1789270200 | 2026-09-13 03:30 | 317 | — |
| 347 | 1789270500 | 2026-09-13 03:35 | 318 | — |
| 348 | 1789270800 | 2026-09-13 03:40 | 319 | — |
| 349 | 1789271100 | 2026-09-13 03:45 | 320 | — |
| 350 | 1789271400 | 2026-09-13 03:50 | 321 | — |
| 351 | 1789271700 | 2026-09-13 03:55 | 322 | — |
| 352 | 1789272000 | 2026-09-13 04:00 | 323 | — |
| 353 | 1789272300 | 2026-09-13 04:05 | 324 | — |
| 354 | 1789272600 | 2026-09-13 04:10 | 325 | — |
| 355 | 1789272900 | 2026-09-13 04:15 | 326 | — |
| 356 | 1789273200 | 2026-09-13 04:20 | 327 | — |
| 357 | 1789273500 | 2026-09-13 04:25 | 328 | — |
| 358 | 1789273800 | 2026-09-13 04:30 | 329 | — |
| 359 | 1789274100 | 2026-09-13 04:35 | — | disconnect |
| 360 | 1789274400 | 2026-09-13 04:40 | 330 | — |
| 361 | 1789274700 | 2026-09-13 04:45 | 331 | — |
| 362 | 1789275000 | 2026-09-13 04:50 | 332 | — |
| 363 | 1789275300 | 2026-09-13 04:55 | 333 | — |
| 364 | 1789275600 | 2026-09-13 05:00 | 334 | — |
| 365 | 1789275900 | 2026-09-13 05:05 | 335 | — |
| 366 | 1789276200 | 2026-09-13 05:10 | 336 | — |
| 367 | 1789276500 | 2026-09-13 05:15 | 337 | — |
| 368 | 1789276800 | 2026-09-13 05:20 | 338 | — |
| 369 | 1789277100 | 2026-09-13 05:25 | 339 | — |
| 370 | 1789277400 | 2026-09-13 05:30 | 340 | — |
| 371 | 1789277700 | 2026-09-13 05:35 | 341 | — |
| 372 | 1789278000 | 2026-09-13 05:40 | — | disconnect |
| 373 | 1789278300 | 2026-09-13 05:45 | 342 | — |
| 374 | 1789278600 | 2026-09-13 05:50 | 343 | — |
| 375 | 1789278900 | 2026-09-13 05:55 | 344 | — |
| 376 | 1789279200 | 2026-09-13 06:00 | 345 | — |
| 377 | 1789279500 | 2026-09-13 06:05 | 346 | — |
| 378 | 1789279800 | 2026-09-13 06:10 | 347 | — |
| 379 | 1789280100 | 2026-09-13 06:15 | 348 | — |
| 380 | 1789280400 | 2026-09-13 06:20 | 349 | — |
| 381 | 1789280700 | 2026-09-13 06:25 | 350 | — |
| 382 | 1789281000 | 2026-09-13 06:30 | 351 | — |
| 383 | 1789281300 | 2026-09-13 06:35 | 352 | — |
| 384 | 1789281600 | 2026-09-13 06:40 | 353 | — |
| 385 | 1789281900 | 2026-09-13 06:45 | 354 | — |
| 386 | 1789282200 | 2026-09-13 06:50 | 355 | — |
| 387 | 1789282500 | 2026-09-13 06:55 | 356 | — |
| 388 | 1789282800 | 2026-09-13 07:00 | 357 | — |
| 389 | 1789283100 | 2026-09-13 07:05 | 358 | — |
| 390 | 1789283400 | 2026-09-13 07:10 | 359 | — |
| 391 | 1789283700 | 2026-09-13 07:15 | 360 | — |
| 392 | 1789284000 | 2026-09-13 07:20 | 361 | — |
| 393 | 1789284300 | 2026-09-13 07:25 | 362 | — |
| 394 | 1789284600 | 2026-09-13 07:30 | 363 | — |
| 395 | 1789284900 | 2026-09-13 07:35 | 364 | — |
| 396 | 1789285200 | 2026-09-13 07:40 | — | disconnect |
| 397 | 1789285500 | 2026-09-13 07:45 | 365 | — |
| 398 | 1789285800 | 2026-09-13 07:50 | 366 | — |
| 399 | 1789286100 | 2026-09-13 07:55 | 367 | — |
| 400 | 1789286400 | 2026-09-13 08:00 | 368 | — |
| 401 | 1789286700 | 2026-09-13 08:05 | 369 | — |
| 402 | 1789287000 | 2026-09-13 08:10 | 370 | — |
| 403 | 1789287300 | 2026-09-13 08:15 | 371 | — |
| 404 | 1789287600 | 2026-09-13 08:20 | 372 | — |
| 405 | 1789287900 | 2026-09-13 08:25 | 373 | — |
| 406 | 1789288200 | 2026-09-13 08:30 | 374 | — |
| 407 | 1789288500 | 2026-09-13 08:35 | 375 | — |
| 408 | 1789288800 | 2026-09-13 08:40 | 376 | — |
| 409 | 1789289100 | 2026-09-13 08:45 | 377 | — |
| 410 | 1789289400 | 2026-09-13 08:50 | 378 | — |
| 411 | 1789289700 | 2026-09-13 08:55 | 379 | — |
| 412 | 1789290000 | 2026-09-13 09:00 | 380 | — |
| 413 | 1789290300 | 2026-09-13 09:05 | 381 | — |
| 414 | 1789290600 | 2026-09-13 09:10 | 382 | — |
| 415 | 1789290900 | 2026-09-13 09:15 | 383 | — |
| 416 | 1789291200 | 2026-09-13 09:20 | 384 | — |
| 417 | 1789291500 | 2026-09-13 09:25 | 385 | — |
| 418 | 1789291800 | 2026-09-13 09:30 | 386 | — |
| 419 | 1789292100 | 2026-09-13 09:35 | 387 | — |
| 420 | 1789292400 | 2026-09-13 09:40 | — | disconnect |
| 421 | 1789292700 | 2026-09-13 09:45 | 388 | — |
| 422 | 1789293000 | 2026-09-13 09:50 | 389 | — |
| 423 | 1789293300 | 2026-09-13 09:55 | 390 | — |
| 424 | 1789293600 | 2026-09-13 10:00 | 391 | — |
| 425 | 1789293900 | 2026-09-13 10:05 | 392 | — |
| 426 | 1789294200 | 2026-09-13 10:10 | 393 | — |
| 427 | 1789294500 | 2026-09-13 10:15 | 394 | — |
| 428 | 1789294800 | 2026-09-13 10:20 | 395 | — |
| 429 | 1789295100 | 2026-09-13 10:25 | 396 | — |
| 430 | 1789295400 | 2026-09-13 10:30 | 397 | — |
| 431 | 1789295700 | 2026-09-13 10:35 | 398 | — |
| 432 | 1789296000 | 2026-09-13 10:40 | 399 | — |
| 433 | 1789296300 | 2026-09-13 10:45 | 400 | — |

#### The test-2 walk

| # | T0 | open (UTC) | member | reason not a member |
|---|---|---|---|---|
| 1 | 1789296600 | 2026-09-13 10:50 | — | disconnect |
| 2 | 1789296900 | 2026-09-13 10:55 | 1 | — |
| 3 | 1789297200 | 2026-09-13 11:00 | 2 | — |
| 4 | 1789297500 | 2026-09-13 11:05 | 3 | — |
| 5 | 1789297800 | 2026-09-13 11:10 | 4 | — |
| 6 | 1789298100 | 2026-09-13 11:15 | 5 | — |
| 7 | 1789298400 | 2026-09-13 11:20 | 6 | — |
| 8 | 1789298700 | 2026-09-13 11:25 | 7 | — |
| 9 | 1789299000 | 2026-09-13 11:30 | 8 | — |
| 10 | 1789299300 | 2026-09-13 11:35 | 9 | — |
| 11 | 1789299600 | 2026-09-13 11:40 | 10 | — |
| 12 | 1789299900 | 2026-09-13 11:45 | 11 | — |
| 13 | 1789300200 | 2026-09-13 11:50 | 12 | — |
| 14 | 1789300500 | 2026-09-13 11:55 | 13 | — |
| 15 | 1789300800 | 2026-09-13 12:00 | 14 | — |
| 16 | 1789301100 | 2026-09-13 12:05 | 15 | — |
| 17 | 1789301400 | 2026-09-13 12:10 | 16 | — |
| 18 | 1789301700 | 2026-09-13 12:15 | 17 | — |
| 19 | 1789302000 | 2026-09-13 12:20 | 18 | — |
| 20 | 1789302300 | 2026-09-13 12:25 | 19 | — |
| 21 | 1789302600 | 2026-09-13 12:30 | 20 | — |
| 22 | 1789302900 | 2026-09-13 12:35 | 21 | — |
| 23 | 1789303200 | 2026-09-13 12:40 | 22 | — |
| 24 | 1789303500 | 2026-09-13 12:45 | 23 | — |
| 25 | 1789303800 | 2026-09-13 12:50 | — | disconnect |
| 26 | 1789304100 | 2026-09-13 12:55 | 24 | — |
| 27 | 1789304400 | 2026-09-13 13:00 | 25 | — |
| 28 | 1789304700 | 2026-09-13 13:05 | 26 | — |
| 29 | 1789305000 | 2026-09-13 13:10 | 27 | — |
| 30 | 1789305300 | 2026-09-13 13:15 | 28 | — |
| 31 | 1789305600 | 2026-09-13 13:20 | 29 | — |
| 32 | 1789305900 | 2026-09-13 13:25 | — | disconnect |
| 33 | 1789306200 | 2026-09-13 13:30 | — | disconnect |
| 34 | 1789306500 | 2026-09-13 13:35 | 30 | — |
| 35 | 1789306800 | 2026-09-13 13:40 | 31 | — |
| 36 | 1789307100 | 2026-09-13 13:45 | 32 | — |
| 37 | 1789307400 | 2026-09-13 13:50 | 33 | — |
| 38 | 1789307700 | 2026-09-13 13:55 | 34 | — |
| 39 | 1789308000 | 2026-09-13 14:00 | 35 | — |
| 40 | 1789308300 | 2026-09-13 14:05 | 36 | — |
| 41 | 1789308600 | 2026-09-13 14:10 | 37 | — |
| 42 | 1789308900 | 2026-09-13 14:15 | 38 | — |
| 43 | 1789309200 | 2026-09-13 14:20 | 39 | — |
| 44 | 1789309500 | 2026-09-13 14:25 | 40 | — |
| 45 | 1789309800 | 2026-09-13 14:30 | 41 | — |
| 46 | 1789310100 | 2026-09-13 14:35 | 42 | — |
| 47 | 1789310400 | 2026-09-13 14:40 | 43 | — |
| 48 | 1789310700 | 2026-09-13 14:45 | 44 | — |
| 49 | 1789311000 | 2026-09-13 14:50 | 45 | — |
| 50 | 1789311300 | 2026-09-13 14:55 | 46 | — |
| 51 | 1789311600 | 2026-09-13 15:00 | 47 | — |
| 52 | 1789311900 | 2026-09-13 15:05 | 48 | — |
| 53 | 1789312200 | 2026-09-13 15:10 | 49 | — |
| 54 | 1789312500 | 2026-09-13 15:15 | 50 | — |
| 55 | 1789312800 | 2026-09-13 15:20 | 51 | — |
| 56 | 1789313100 | 2026-09-13 15:25 | 52 | — |
| 57 | 1789313400 | 2026-09-13 15:30 | — | disconnect |
| 58 | 1789313700 | 2026-09-13 15:35 | 53 | — |
| 59 | 1789314000 | 2026-09-13 15:40 | 54 | — |
| 60 | 1789314300 | 2026-09-13 15:45 | 55 | — |
| 61 | 1789314600 | 2026-09-13 15:50 | 56 | — |
| 62 | 1789314900 | 2026-09-13 15:55 | 57 | — |
| 63 | 1789315200 | 2026-09-13 16:00 | 58 | — |
| 64 | 1789315500 | 2026-09-13 16:05 | 59 | — |
| 65 | 1789315800 | 2026-09-13 16:10 | 60 | — |
| 66 | 1789316100 | 2026-09-13 16:15 | 61 | — |
| 67 | 1789316400 | 2026-09-13 16:20 | 62 | — |
| 68 | 1789316700 | 2026-09-13 16:25 | 63 | — |
| 69 | 1789317000 | 2026-09-13 16:30 | 64 | — |
| 70 | 1789317300 | 2026-09-13 16:35 | 65 | — |
| 71 | 1789317600 | 2026-09-13 16:40 | 66 | — |
| 72 | 1789317900 | 2026-09-13 16:45 | 67 | — |
| 73 | 1789318200 | 2026-09-13 16:50 | 68 | — |
| 74 | 1789318500 | 2026-09-13 16:55 | 69 | — |
| 75 | 1789318800 | 2026-09-13 17:00 | — | disconnect |
| 76 | 1789319100 | 2026-09-13 17:05 | 70 | — |
| 77 | 1789319400 | 2026-09-13 17:10 | 71 | — |
| 78 | 1789319700 | 2026-09-13 17:15 | — | disconnect |
| 79 | 1789320000 | 2026-09-13 17:20 | 72 | — |
| 80 | 1789320300 | 2026-09-13 17:25 | 73 | — |
| 81 | 1789320600 | 2026-09-13 17:30 | 74 | — |
| 82 | 1789320900 | 2026-09-13 17:35 | 75 | — |
| 83 | 1789321200 | 2026-09-13 17:40 | 76 | — |
| 84 | 1789321500 | 2026-09-13 17:45 | 77 | — |
| 85 | 1789321800 | 2026-09-13 17:50 | 78 | — |
| 86 | 1789322100 | 2026-09-13 17:55 | 79 | — |
| 87 | 1789322400 | 2026-09-13 18:00 | 80 | — |
| 88 | 1789322700 | 2026-09-13 18:05 | 81 | — |
| 89 | 1789323000 | 2026-09-13 18:10 | 82 | — |
| 90 | 1789323300 | 2026-09-13 18:15 | 83 | — |
| 91 | 1789323600 | 2026-09-13 18:20 | 84 | — |
| 92 | 1789323900 | 2026-09-13 18:25 | 85 | — |
| 93 | 1789324200 | 2026-09-13 18:30 | 86 | — |
| 94 | 1789324500 | 2026-09-13 18:35 | 87 | — |
| 95 | 1789324800 | 2026-09-13 18:40 | 88 | — |
| 96 | 1789325100 | 2026-09-13 18:45 | 89 | — |
| 97 | 1789325400 | 2026-09-13 18:50 | 90 | — |
| 98 | 1789325700 | 2026-09-13 18:55 | 91 | — |
| 99 | 1789326000 | 2026-09-13 19:00 | 92 | — |
| 100 | 1789326300 | 2026-09-13 19:05 | 93 | — |
| 101 | 1789326600 | 2026-09-13 19:10 | 94 | — |
| 102 | 1789326900 | 2026-09-13 19:15 | — | disconnect |
| 103 | 1789327200 | 2026-09-13 19:20 | 95 | — |
| 104 | 1789327500 | 2026-09-13 19:25 | 96 | — |
| 105 | 1789327800 | 2026-09-13 19:30 | 97 | — |
| 106 | 1789328100 | 2026-09-13 19:35 | 98 | — |
| 107 | 1789328400 | 2026-09-13 19:40 | 99 | — |
| 108 | 1789328700 | 2026-09-13 19:45 | 100 | — |
| 109 | 1789329000 | 2026-09-13 19:50 | 101 | — |
| 110 | 1789329300 | 2026-09-13 19:55 | 102 | — |
| 111 | 1789329600 | 2026-09-13 20:00 | 103 | — |
| 112 | 1789329900 | 2026-09-13 20:05 | 104 | — |
| 113 | 1789330200 | 2026-09-13 20:10 | 105 | — |
| 114 | 1789330500 | 2026-09-13 20:15 | 106 | — |
| 115 | 1789330800 | 2026-09-13 20:20 | 107 | — |
| 116 | 1789331100 | 2026-09-13 20:25 | 108 | — |
| 117 | 1789331400 | 2026-09-13 20:30 | 109 | — |
| 118 | 1789331700 | 2026-09-13 20:35 | 110 | — |
| 119 | 1789332000 | 2026-09-13 20:40 | 111 | — |
| 120 | 1789332300 | 2026-09-13 20:45 | 112 | — |
| 121 | 1789332600 | 2026-09-13 20:50 | 113 | — |
| 122 | 1789332900 | 2026-09-13 20:55 | 114 | — |
| 123 | 1789333200 | 2026-09-13 21:00 | 115 | — |
| 124 | 1789333500 | 2026-09-13 21:05 | 116 | — |
| 125 | 1789333800 | 2026-09-13 21:10 | 117 | — |
| 126 | 1789334100 | 2026-09-13 21:15 | — | disconnect |
| 127 | 1789334400 | 2026-09-13 21:20 | 118 | — |
| 128 | 1789334700 | 2026-09-13 21:25 | 119 | — |
| 129 | 1789335000 | 2026-09-13 21:30 | 120 | — |
| 130 | 1789335300 | 2026-09-13 21:35 | 121 | — |
| 131 | 1789335600 | 2026-09-13 21:40 | 122 | — |
| 132 | 1789335900 | 2026-09-13 21:45 | 123 | — |
| 133 | 1789336200 | 2026-09-13 21:50 | 124 | — |
| 134 | 1789336500 | 2026-09-13 21:55 | 125 | — |
| 135 | 1789336800 | 2026-09-13 22:00 | 126 | — |
| 136 | 1789337100 | 2026-09-13 22:05 | 127 | — |
| 137 | 1789337400 | 2026-09-13 22:10 | 128 | — |
| 138 | 1789337700 | 2026-09-13 22:15 | 129 | — |
| 139 | 1789338000 | 2026-09-13 22:20 | 130 | — |
| 140 | 1789338300 | 2026-09-13 22:25 | 131 | — |
| 141 | 1789338600 | 2026-09-13 22:30 | 132 | — |
| 142 | 1789338900 | 2026-09-13 22:35 | 133 | — |
| 143 | 1789339200 | 2026-09-13 22:40 | 134 | — |
| 144 | 1789339500 | 2026-09-13 22:45 | 135 | — |
| 145 | 1789339800 | 2026-09-13 22:50 | 136 | — |
| 146 | 1789340100 | 2026-09-13 22:55 | 137 | — |
| 147 | 1789340400 | 2026-09-13 23:00 | 138 | — |
| 148 | 1789340700 | 2026-09-13 23:05 | 139 | — |
| 149 | 1789341000 | 2026-09-13 23:10 | 140 | — |
| 150 | 1789341300 | 2026-09-13 23:15 | — | disconnect |
| 151 | 1789341600 | 2026-09-13 23:20 | 141 | — |
| 152 | 1789341900 | 2026-09-13 23:25 | 142 | — |
| 153 | 1789342200 | 2026-09-13 23:30 | 143 | — |
| 154 | 1789342500 | 2026-09-13 23:35 | 144 | — |
| 155 | 1789342800 | 2026-09-13 23:40 | 145 | — |
| 156 | 1789343100 | 2026-09-13 23:45 | 146 | — |
| 157 | 1789343400 | 2026-09-13 23:50 | 147 | — |
| 158 | 1789343700 | 2026-09-13 23:55 | 148 | — |
| 159 | 1789344000 | 2026-09-14 00:00 | 149 | — |
| 160 | 1789344300 | 2026-09-14 00:05 | 150 | — |
| 161 | 1789344600 | 2026-09-14 00:10 | 151 | — |
| 162 | 1789344900 | 2026-09-14 00:15 | 152 | — |
| 163 | 1789345200 | 2026-09-14 00:20 | 153 | — |
| 164 | 1789345500 | 2026-09-14 00:25 | 154 | — |
| 165 | 1789345800 | 2026-09-14 00:30 | 155 | — |
| 166 | 1789346100 | 2026-09-14 00:35 | 156 | — |
| 167 | 1789346400 | 2026-09-14 00:40 | 157 | — |
| 168 | 1789346700 | 2026-09-14 00:45 | 158 | — |
| 169 | 1789347000 | 2026-09-14 00:50 | 159 | — |
| 170 | 1789347300 | 2026-09-14 00:55 | 160 | — |
| 171 | 1789347600 | 2026-09-14 01:00 | 161 | — |
| 172 | 1789347900 | 2026-09-14 01:05 | 162 | — |
| 173 | 1789348200 | 2026-09-14 01:10 | 163 | — |
| 174 | 1789348500 | 2026-09-14 01:15 | — | disconnect |
| 175 | 1789348800 | 2026-09-14 01:20 | 164 | — |
| 176 | 1789349100 | 2026-09-14 01:25 | 165 | — |
| 177 | 1789349400 | 2026-09-14 01:30 | 166 | — |
| 178 | 1789349700 | 2026-09-14 01:35 | 167 | — |
| 179 | 1789350000 | 2026-09-14 01:40 | 168 | — |
| 180 | 1789350300 | 2026-09-14 01:45 | 169 | — |
| 181 | 1789350600 | 2026-09-14 01:50 | 170 | — |
| 182 | 1789350900 | 2026-09-14 01:55 | 171 | — |
| 183 | 1789351200 | 2026-09-14 02:00 | 172 | — |
| 184 | 1789351500 | 2026-09-14 02:05 | 173 | — |
| 185 | 1789351800 | 2026-09-14 02:10 | 174 | — |
| 186 | 1789352100 | 2026-09-14 02:15 | 175 | — |
| 187 | 1789352400 | 2026-09-14 02:20 | 176 | — |
| 188 | 1789352700 | 2026-09-14 02:25 | 177 | — |
| 189 | 1789353000 | 2026-09-14 02:30 | 178 | — |
| 190 | 1789353300 | 2026-09-14 02:35 | 179 | — |
| 191 | 1789353600 | 2026-09-14 02:40 | 180 | — |
| 192 | 1789353900 | 2026-09-14 02:45 | 181 | — |
| 193 | 1789354200 | 2026-09-14 02:50 | 182 | — |
| 194 | 1789354500 | 2026-09-14 02:55 | 183 | — |
| 195 | 1789354800 | 2026-09-14 03:00 | 184 | — |
| 196 | 1789355100 | 2026-09-14 03:05 | 185 | — |
| 197 | 1789355400 | 2026-09-14 03:10 | 186 | — |
| 198 | 1789355700 | 2026-09-14 03:15 | — | disconnect |
| 199 | 1789356000 | 2026-09-14 03:20 | 187 | — |
| 200 | 1789356300 | 2026-09-14 03:25 | 188 | — |
| 201 | 1789356600 | 2026-09-14 03:30 | 189 | — |
| 202 | 1789356900 | 2026-09-14 03:35 | 190 | — |
| 203 | 1789357200 | 2026-09-14 03:40 | 191 | — |
| 204 | 1789357500 | 2026-09-14 03:45 | 192 | — |
| 205 | 1789357800 | 2026-09-14 03:50 | 193 | — |
| 206 | 1789358100 | 2026-09-14 03:55 | 194 | — |
| 207 | 1789358400 | 2026-09-14 04:00 | 195 | — |
| 208 | 1789358700 | 2026-09-14 04:05 | 196 | — |
| 209 | 1789359000 | 2026-09-14 04:10 | 197 | — |
| 210 | 1789359300 | 2026-09-14 04:15 | 198 | — |
| 211 | 1789359600 | 2026-09-14 04:20 | 199 | — |
| 212 | 1789359900 | 2026-09-14 04:25 | 200 | — |
| 213 | 1789360200 | 2026-09-14 04:30 | 201 | — |
| 214 | 1789360500 | 2026-09-14 04:35 | 202 | — |
| 215 | 1789360800 | 2026-09-14 04:40 | 203 | — |
| 216 | 1789361100 | 2026-09-14 04:45 | 204 | — |
| 217 | 1789361400 | 2026-09-14 04:50 | 205 | — |
| 218 | 1789361700 | 2026-09-14 04:55 | 206 | — |
| 219 | 1789362000 | 2026-09-14 05:00 | 207 | — |
| 220 | 1789362300 | 2026-09-14 05:05 | 208 | — |
| 221 | 1789362600 | 2026-09-14 05:10 | 209 | — |
| 222 | 1789362900 | 2026-09-14 05:15 | — | disconnect |
| 223 | 1789363200 | 2026-09-14 05:20 | 210 | — |
| 224 | 1789363500 | 2026-09-14 05:25 | 211 | — |
| 225 | 1789363800 | 2026-09-14 05:30 | 212 | — |
| 226 | 1789364100 | 2026-09-14 05:35 | 213 | — |
| 227 | 1789364400 | 2026-09-14 05:40 | 214 | — |
| 228 | 1789364700 | 2026-09-14 05:45 | 215 | — |
| 229 | 1789365000 | 2026-09-14 05:50 | 216 | — |
| 230 | 1789365300 | 2026-09-14 05:55 | 217 | — |
| 231 | 1789365600 | 2026-09-14 06:00 | 218 | — |
| 232 | 1789365900 | 2026-09-14 06:05 | 219 | — |
| 233 | 1789366200 | 2026-09-14 06:10 | 220 | — |
| 234 | 1789366500 | 2026-09-14 06:15 | 221 | — |
| 235 | 1789366800 | 2026-09-14 06:20 | 222 | — |
| 236 | 1789367100 | 2026-09-14 06:25 | — | disconnect |
| 237 | 1789367400 | 2026-09-14 06:30 | — | disconnect |
| 238 | 1789367700 | 2026-09-14 06:35 | 223 | — |
| 239 | 1789368000 | 2026-09-14 06:40 | 224 | — |
| 240 | 1789368300 | 2026-09-14 06:45 | 225 | — |
| 241 | 1789368600 | 2026-09-14 06:50 | 226 | — |
| 242 | 1789368900 | 2026-09-14 06:55 | 227 | — |
| 243 | 1789369200 | 2026-09-14 07:00 | 228 | — |
| 244 | 1789369500 | 2026-09-14 07:05 | 229 | — |
| 245 | 1789369800 | 2026-09-14 07:10 | 230 | — |
| 246 | 1789370100 | 2026-09-14 07:15 | 231 | — |
| 247 | 1789370400 | 2026-09-14 07:20 | 232 | — |
| 248 | 1789370700 | 2026-09-14 07:25 | 233 | — |
| 249 | 1789371000 | 2026-09-14 07:30 | 234 | — |
| 250 | 1789371300 | 2026-09-14 07:35 | 235 | — |
| 251 | 1789371600 | 2026-09-14 07:40 | 236 | — |
| 252 | 1789371900 | 2026-09-14 07:45 | 237 | — |
| 253 | 1789372200 | 2026-09-14 07:50 | 238 | — |
| 254 | 1789372500 | 2026-09-14 07:55 | 239 | — |
| 255 | 1789372800 | 2026-09-14 08:00 | 240 | — |
| 256 | 1789373100 | 2026-09-14 08:05 | 241 | — |
| 257 | 1789373400 | 2026-09-14 08:10 | 242 | — |
| 258 | 1789373700 | 2026-09-14 08:15 | 243 | — |
| 259 | 1789374000 | 2026-09-14 08:20 | 244 | — |
| 260 | 1789374300 | 2026-09-14 08:25 | — | disconnect |
| 261 | 1789374600 | 2026-09-14 08:30 | — | disconnect |
| 262 | 1789374900 | 2026-09-14 08:35 | 245 | — |
| 263 | 1789375200 | 2026-09-14 08:40 | 246 | — |
| 264 | 1789375500 | 2026-09-14 08:45 | 247 | — |
| 265 | 1789375800 | 2026-09-14 08:50 | 248 | — |
| 266 | 1789376100 | 2026-09-14 08:55 | — | disconnect |
| 267 | 1789376400 | 2026-09-14 09:00 | — | disconnect |
| 268 | 1789376700 | 2026-09-14 09:05 | — | disconnect |
| 269 | 1789377000 | 2026-09-14 09:10 | — | disconnect |
| 270 | 1789377300 | 2026-09-14 09:15 | 249 | — |
| 271 | 1789377600 | 2026-09-14 09:20 | 250 | — |
| 272 | 1789377900 | 2026-09-14 09:25 | 251 | — |
| 273 | 1789378200 | 2026-09-14 09:30 | 252 | — |
| 274 | 1789378500 | 2026-09-14 09:35 | 253 | — |
| 275 | 1789378800 | 2026-09-14 09:40 | 254 | — |
| 276 | 1789379100 | 2026-09-14 09:45 | 255 | — |
| 277 | 1789379400 | 2026-09-14 09:50 | 256 | — |
| 278 | 1789379700 | 2026-09-14 09:55 | 257 | — |
| 279 | 1789380000 | 2026-09-14 10:00 | 258 | — |
| 280 | 1789380300 | 2026-09-14 10:05 | 259 | — |
| 281 | 1789380600 | 2026-09-14 10:10 | 260 | — |
| 282 | 1789380900 | 2026-09-14 10:15 | 261 | — |
| 283 | 1789381200 | 2026-09-14 10:20 | 262 | — |
| 284 | 1789381500 | 2026-09-14 10:25 | 263 | — |
| 285 | 1789381800 | 2026-09-14 10:30 | 264 | — |
| 286 | 1789382100 | 2026-09-14 10:35 | 265 | — |
| 287 | 1789382400 | 2026-09-14 10:40 | 266 | — |
| 288 | 1789382700 | 2026-09-14 10:45 | 267 | — |
| 289 | 1789383000 | 2026-09-14 10:50 | 268 | — |
| 290 | 1789383300 | 2026-09-14 10:55 | 269 | — |
| 291 | 1789383600 | 2026-09-14 11:00 | 270 | — |
| 292 | 1789383900 | 2026-09-14 11:05 | — | disconnect |
| 293 | 1789384200 | 2026-09-14 11:10 | — | disconnect |
| 294 | 1789384500 | 2026-09-14 11:15 | 271 | — |
| 295 | 1789384800 | 2026-09-14 11:20 | 272 | — |
| 296 | 1789385100 | 2026-09-14 11:25 | 273 | — |
| 297 | 1789385400 | 2026-09-14 11:30 | 274 | — |
| 298 | 1789385700 | 2026-09-14 11:35 | 275 | — |
| 299 | 1789386000 | 2026-09-14 11:40 | 276 | — |
| 300 | 1789386300 | 2026-09-14 11:45 | 277 | — |
| 301 | 1789386600 | 2026-09-14 11:50 | 278 | — |
| 302 | 1789386900 | 2026-09-14 11:55 | 279 | — |
| 303 | 1789387200 | 2026-09-14 12:00 | 280 | — |
| 304 | 1789387500 | 2026-09-14 12:05 | 281 | — |
| 305 | 1789387800 | 2026-09-14 12:10 | 282 | — |
| 306 | 1789388100 | 2026-09-14 12:15 | 283 | — |
| 307 | 1789388400 | 2026-09-14 12:20 | 284 | — |
| 308 | 1789388700 | 2026-09-14 12:25 | 285 | — |
| 309 | 1789389000 | 2026-09-14 12:30 | 286 | — |
| 310 | 1789389300 | 2026-09-14 12:35 | 287 | — |
| 311 | 1789389600 | 2026-09-14 12:40 | 288 | — |
| 312 | 1789389900 | 2026-09-14 12:45 | — | disconnect |
| 313 | 1789390200 | 2026-09-14 12:50 | — | disconnect |
| 314 | 1789390500 | 2026-09-14 12:55 | 289 | — |
| 315 | 1789390800 | 2026-09-14 13:00 | 290 | — |
| 316 | 1789391100 | 2026-09-14 13:05 | 291 | — |
| 317 | 1789391400 | 2026-09-14 13:10 | 292 | — |
| 318 | 1789391700 | 2026-09-14 13:15 | 293 | — |
| 319 | 1789392000 | 2026-09-14 13:20 | 294 | — |
| 320 | 1789392300 | 2026-09-14 13:25 | 295 | — |
| 321 | 1789392600 | 2026-09-14 13:30 | 296 | — |
| 322 | 1789392900 | 2026-09-14 13:35 | 297 | — |
| 323 | 1789393200 | 2026-09-14 13:40 | 298 | — |
| 324 | 1789393500 | 2026-09-14 13:45 | 299 | — |
| 325 | 1789393800 | 2026-09-14 13:50 | — | disconnect |
| 326 | 1789394100 | 2026-09-14 13:55 | — | disconnect |
| 327 | 1789394400 | 2026-09-14 14:00 | 300 | — |
| 328 | 1789394700 | 2026-09-14 14:05 | 301 | — |
| 329 | 1789395000 | 2026-09-14 14:10 | 302 | — |
| 330 | 1789395300 | 2026-09-14 14:15 | 303 | — |
| 331 | 1789395600 | 2026-09-14 14:20 | 304 | — |
| 332 | 1789395900 | 2026-09-14 14:25 | 305 | — |
| 333 | 1789396200 | 2026-09-14 14:30 | 306 | — |
| 334 | 1789396500 | 2026-09-14 14:35 | 307 | — |
| 335 | 1789396800 | 2026-09-14 14:40 | 308 | — |
| 336 | 1789397100 | 2026-09-14 14:45 | 309 | — |
| 337 | 1789397400 | 2026-09-14 14:50 | 310 | — |
| 338 | 1789397700 | 2026-09-14 14:55 | 311 | — |
| 339 | 1789398000 | 2026-09-14 15:00 | 312 | — |
| 340 | 1789398300 | 2026-09-14 15:05 | 313 | — |
| 341 | 1789398600 | 2026-09-14 15:10 | 314 | — |
| 342 | 1789398900 | 2026-09-14 15:15 | 315 | — |
| 343 | 1789399200 | 2026-09-14 15:20 | 316 | — |
| 344 | 1789399500 | 2026-09-14 15:25 | 317 | — |
| 345 | 1789399800 | 2026-09-14 15:30 | 318 | — |
| 346 | 1789400100 | 2026-09-14 15:35 | 319 | — |
| 347 | 1789400400 | 2026-09-14 15:40 | 320 | — |
| 348 | 1789400700 | 2026-09-14 15:45 | 321 | — |
| 349 | 1789401000 | 2026-09-14 15:50 | — | disconnect |
| 350 | 1789401300 | 2026-09-14 15:55 | — | disconnect |
| 351 | 1789401600 | 2026-09-14 16:00 | 322 | — |
| 352 | 1789401900 | 2026-09-14 16:05 | 323 | — |
| 353 | 1789402200 | 2026-09-14 16:10 | 324 | — |
| 354 | 1789402500 | 2026-09-14 16:15 | 325 | — |
| 355 | 1789402800 | 2026-09-14 16:20 | 326 | — |
| 356 | 1789403100 | 2026-09-14 16:25 | 327 | — |
| 357 | 1789403400 | 2026-09-14 16:30 | 328 | — |
| 358 | 1789403700 | 2026-09-14 16:35 | 329 | — |
| 359 | 1789404000 | 2026-09-14 16:40 | 330 | — |
| 360 | 1789404300 | 2026-09-14 16:45 | 331 | — |
| 361 | 1789404600 | 2026-09-14 16:50 | 332 | — |
| 362 | 1789404900 | 2026-09-14 16:55 | 333 | — |
| 363 | 1789405200 | 2026-09-14 17:00 | 334 | — |
| 364 | 1789405500 | 2026-09-14 17:05 | 335 | — |
| 365 | 1789405800 | 2026-09-14 17:10 | 336 | — |
| 366 | 1789406100 | 2026-09-14 17:15 | 337 | — |
| 367 | 1789406400 | 2026-09-14 17:20 | 338 | — |
| 368 | 1789406700 | 2026-09-14 17:25 | 339 | — |
| 369 | 1789407000 | 2026-09-14 17:30 | 340 | — |
| 370 | 1789407300 | 2026-09-14 17:35 | 341 | — |
| 371 | 1789407600 | 2026-09-14 17:40 | 342 | — |
| 372 | 1789407900 | 2026-09-14 17:45 | 343 | — |
| 373 | 1789408200 | 2026-09-14 17:50 | — | disconnect |
| 374 | 1789408500 | 2026-09-14 17:55 | — | disconnect |
| 375 | 1789408800 | 2026-09-14 18:00 | 344 | — |
| 376 | 1789409100 | 2026-09-14 18:05 | 345 | — |
| 377 | 1789409400 | 2026-09-14 18:10 | 346 | — |
| 378 | 1789409700 | 2026-09-14 18:15 | 347 | — |
| 379 | 1789410000 | 2026-09-14 18:20 | 348 | — |
| 380 | 1789410300 | 2026-09-14 18:25 | 349 | — |
| 381 | 1789410600 | 2026-09-14 18:30 | 350 | — |
| 382 | 1789410900 | 2026-09-14 18:35 | 351 | — |
| 383 | 1789411200 | 2026-09-14 18:40 | 352 | — |
| 384 | 1789411500 | 2026-09-14 18:45 | 353 | — |
| 385 | 1789411800 | 2026-09-14 18:50 | 354 | — |
| 386 | 1789412100 | 2026-09-14 18:55 | — | disconnect |
| 387 | 1789412400 | 2026-09-14 19:00 | — | disconnect |
| 388 | 1789412700 | 2026-09-14 19:05 | 355 | — |
| 389 | 1789413000 | 2026-09-14 19:10 | 356 | — |
| 390 | 1789413300 | 2026-09-14 19:15 | 357 | — |
| 391 | 1789413600 | 2026-09-14 19:20 | 358 | — |
| 392 | 1789413900 | 2026-09-14 19:25 | 359 | — |
| 393 | 1789414200 | 2026-09-14 19:30 | 360 | — |
| 394 | 1789414500 | 2026-09-14 19:35 | 361 | — |
| 395 | 1789414800 | 2026-09-14 19:40 | 362 | — |
| 396 | 1789415100 | 2026-09-14 19:45 | 363 | — |
| 397 | 1789415400 | 2026-09-14 19:50 | 364 | — |
| 398 | 1789415700 | 2026-09-14 19:55 | 365 | — |
| 399 | 1789416000 | 2026-09-14 20:00 | — | disconnect |
| 400 | 1789416300 | 2026-09-14 20:05 | — | disconnect |
| 401 | 1789416600 | 2026-09-14 20:10 | 366 | — |
| 402 | 1789416900 | 2026-09-14 20:15 | 367 | — |
| 403 | 1789417200 | 2026-09-14 20:20 | 368 | — |
| 404 | 1789417500 | 2026-09-14 20:25 | 369 | — |
| 405 | 1789417800 | 2026-09-14 20:30 | 370 | — |
| 406 | 1789418100 | 2026-09-14 20:35 | 371 | — |
| 407 | 1789418400 | 2026-09-14 20:40 | 372 | — |
| 408 | 1789418700 | 2026-09-14 20:45 | 373 | — |
| 409 | 1789419000 | 2026-09-14 20:50 | 374 | — |
| 410 | 1789419300 | 2026-09-14 20:55 | 375 | — |
| 411 | 1789419600 | 2026-09-14 21:00 | 376 | — |
| 412 | 1789419900 | 2026-09-14 21:05 | 377 | — |
| 413 | 1789420200 | 2026-09-14 21:10 | 378 | — |
| 414 | 1789420500 | 2026-09-14 21:15 | 379 | — |
| 415 | 1789420800 | 2026-09-14 21:20 | 380 | — |
| 416 | 1789421100 | 2026-09-14 21:25 | 381 | — |
| 417 | 1789421400 | 2026-09-14 21:30 | 382 | — |
| 418 | 1789421700 | 2026-09-14 21:35 | 383 | — |
| 419 | 1789422000 | 2026-09-14 21:40 | 384 | — |
| 420 | 1789422300 | 2026-09-14 21:45 | — | disconnect |
| 421 | 1789422600 | 2026-09-14 21:50 | 385 | — |
| 422 | 1789422900 | 2026-09-14 21:55 | 386 | — |
| 423 | 1789423200 | 2026-09-14 22:00 | 387 | — |
| 424 | 1789423500 | 2026-09-14 22:05 | 388 | — |
| 425 | 1789423800 | 2026-09-14 22:10 | 389 | — |
| 426 | 1789424100 | 2026-09-14 22:15 | 390 | — |
| 427 | 1789424400 | 2026-09-14 22:20 | 391 | — |
| 428 | 1789424700 | 2026-09-14 22:25 | 392 | — |
| 429 | 1789425000 | 2026-09-14 22:30 | 393 | — |
| 430 | 1789425300 | 2026-09-14 22:35 | — | disconnect |
| 431 | 1789425600 | 2026-09-14 22:40 | — | disconnect |
| 432 | 1789425900 | 2026-09-14 22:45 | 394 | — |
| 433 | 1789426200 | 2026-09-14 22:50 | 395 | — |
| 434 | 1789426500 | 2026-09-14 22:55 | 396 | — |
| 435 | 1789426800 | 2026-09-14 23:00 | 397 | — |
| 436 | 1789427100 | 2026-09-14 23:05 | 398 | — |
| 437 | 1789427400 | 2026-09-14 23:10 | 399 | — |
| 438 | 1789427700 | 2026-09-14 23:15 | 400 | — |

#### Admissibility, every member at every `tau`

`ADMIT`: 240: 2.12324 · 180: 2.14298 · 120: 2.18062 · 90: 2.16098 · 60: 2.16725 · 30: 2.15178 · 10: 2.14530. Each cell is `sigma_hat`, then `yes` when it is at or above `ADMIT[tau]`.

| T0 | set | 240 | 180 | 120 | 90 | 60 | 30 | 10 |
|---|---|---|---|---|---|---|---|---|
| 1789035000 | fit | 2.530100 yes | 2.535763 yes | 2.451468 yes | 2.383351 yes | 2.324210 yes | 2.782980 yes | 2.809884 yes |
| 1789035300 | fit | 2.732358 yes | 2.659931 yes | 2.565003 yes | 2.532382 yes | 2.592436 yes | 2.560318 yes | 2.518737 yes |
| 1789035900 | fit | 1.666503 no | 1.786661 no | 1.711453 no | 1.674793 no | 1.652006 no | 1.621526 no | 1.617702 no |
| 1789036200 | fit | 1.952055 no | 1.855279 no | 1.877148 no | 1.916708 no | 2.086885 no | 2.216858 yes | 2.218363 yes |
| 1789036500 | fit | 2.693919 yes | 2.641654 yes | 2.771478 yes | 2.725614 yes | 2.685583 yes | 2.633004 yes | 2.627609 yes |
| 1789036800 | fit | 2.425491 yes | 2.268113 yes | 2.223990 yes | 2.218395 yes | 2.195106 yes | 2.166689 yes | 2.137723 no |
| 1789037100 | fit | 1.769768 no | 2.230761 yes | 2.120833 no | 2.220145 yes | 2.195129 yes | 2.150723 no | 2.117092 no |
| 1789037400 | fit | 2.352499 yes | 2.347522 yes | 2.273226 yes | 2.235631 yes | 2.179576 yes | 2.143024 no | 2.119635 no |
| 1789037700 | fit | 1.717512 no | 3.900346 yes | 3.912500 yes | 3.940714 yes | 3.857076 yes | 3.765029 yes | 3.721680 yes |
| 1789038000 | fit | 4.652285 yes | 4.493305 yes | 4.413524 yes | 4.311366 yes | 4.199896 yes | 4.145086 yes | 4.820953 yes |
| 1789038300 | fit | 4.459566 yes | 4.443853 yes | 4.404055 yes | 4.330603 yes | 4.218626 yes | 4.121416 yes | 4.125275 yes |
| 1789038600 | fit | 3.620700 yes | 3.496621 yes | 3.321449 yes | 3.270945 yes | 3.197510 yes | 3.216254 yes | 3.190003 yes |
| 1789038900 | fit | 3.238627 yes | 3.368266 yes | 3.540687 yes | 3.460048 yes | 3.384878 yes | 3.302489 yes | 3.320030 yes |
| 1789039200 | fit | 3.669327 yes | 3.563799 yes | 3.377575 yes | 3.277560 yes | 3.197172 yes | 3.123632 yes | 3.081732 yes |
| 1789039500 | fit | 1.813881 no | 1.984453 no | 1.957838 no | 2.045530 no | 2.034525 no | 1.997005 no | 1.965995 no |
| 1789039800 | fit | 1.935624 no | 1.952598 no | 1.894579 no | 2.381396 yes | 2.395338 yes | 2.370467 yes | 2.345172 yes |
| 1789040100 | fit | 2.430043 yes | 2.334917 yes | 2.232447 yes | 2.615434 yes | 2.606959 yes | 2.563081 yes | 2.519962 yes |
| 1789040400 | fit | 2.220871 yes | 2.144627 yes | 2.169106 no | 2.556754 yes | 2.510251 yes | 2.453148 yes | 2.428600 yes |
| 1789040700 | fit | 2.366736 yes | 2.227366 yes | 2.477131 yes | 2.412816 yes | 2.636600 yes | 2.616830 yes | 2.577844 yes |
| 1789041000 | fit | 2.853605 yes | 2.675480 yes | 2.629899 yes | 2.746381 yes | 2.767463 yes | 3.200606 yes | 3.150441 yes |
| 1789041300 | fit | 3.483343 yes | 3.306494 yes | 3.144231 yes | 3.207532 yes | 3.146729 yes | 3.072481 yes | 3.051561 yes |
| 1789041600 | fit | 2.597760 yes | 2.693205 yes | 2.719552 yes | 2.719533 yes | 2.698697 yes | 2.809714 yes | 2.772218 yes |
| 1789041900 | fit | 2.969603 yes | 3.290144 yes | 3.409489 yes | 3.383309 yes | 3.477553 yes | 3.439408 yes | 3.384689 yes |
| 1789042200 | fit | 3.359677 yes | 3.325086 yes | 3.212843 yes | 3.254519 yes | 3.240110 yes | 3.305368 yes | 3.264241 yes |
| 1789042500 | fit | 3.728425 yes | 3.723366 yes | 3.580150 yes | 3.516643 yes | 3.581262 yes | 3.848203 yes | 3.815713 yes |
| 1789043100 | fit | 3.128885 yes | 2.923014 yes | 2.787130 yes | 2.770332 yes | 2.749660 yes | 2.696909 yes | 2.653110 yes |
| 1789043400 | fit | 13.390416 yes | 13.587998 yes | 13.415267 yes | 13.243426 yes | 12.976745 yes | 12.970085 yes | 12.898407 yes |
| 1789043700 | fit | 16.908960 yes | 16.518456 yes | 15.683285 yes | 15.327698 yes | 15.335682 yes | 15.098588 yes | 14.961075 yes |
| 1789044000 | fit | 10.609360 yes | 10.219858 yes | 10.050037 yes | 9.878880 yes | 9.673183 yes | 9.469817 yes | 9.339000 yes |
| 1789044300 | fit | 7.210525 yes | 7.708239 yes | 8.927244 yes | 8.813612 yes | 9.120328 yes | 8.943687 yes | 8.882865 yes |
| 1789044600 | fit | 9.226316 yes | 8.826510 yes | 8.491693 yes | 8.305154 yes | 8.383366 yes | 8.349627 yes | 8.229327 yes |
| 1789044900 | fit | 6.087281 yes | 5.910867 yes | 6.350690 yes | 6.196740 yes | 6.336993 yes | 6.537499 yes | 6.446716 yes |
| 1789045200 | fit | 6.524558 yes | 6.513269 yes | 6.314404 yes | 6.188987 yes | 6.073676 yes | 5.986534 yes | 6.170721 yes |
| 1789045500 | fit | 5.560786 yes | 5.414205 yes | 5.254035 yes | 5.217077 yes | 5.196300 yes | 5.198736 yes | 5.350784 yes |
| 1789045800 | fit | 5.205628 yes | 5.348872 yes | 5.459767 yes | 5.606325 yes | 5.672296 yes | 5.727040 yes | 5.698402 yes |
| 1789046100 | fit | 6.285508 yes | 6.516200 yes | 6.320126 yes | 6.201155 yes | 6.175591 yes | 6.103100 yes | 6.085381 yes |
| 1789046400 | fit | 5.862737 yes | 5.940168 yes | 5.762980 yes | 5.679966 yes | 5.598513 yes | 5.501797 yes | 5.440335 yes |
| 1789046700 | fit | 4.929192 yes | 4.681277 yes | 4.543478 yes | 4.527401 yes | 4.433035 yes | 4.351311 yes | 4.285920 yes |
| 1789047000 | fit | 4.862487 yes | 5.744626 yes | 6.003760 yes | 6.025415 yes | 6.019759 yes | 6.021723 yes | 6.057570 yes |
| 1789047300 | fit | 7.588296 yes | 7.373051 yes | 7.538386 yes | 7.492755 yes | 7.348400 yes | 7.299333 yes | 7.263448 yes |
| 1789047600 | fit | 6.704451 yes | 6.502466 yes | 6.629850 yes | 6.588260 yes | 6.484672 yes | 6.432696 yes | 6.377319 yes |
| 1789047900 | fit | 5.799749 yes | 5.636682 yes | 5.508478 yes | 5.530599 yes | 5.449950 yes | 5.594583 yes | 5.605937 yes |
| 1789048200 | fit | 5.147602 yes | 4.981960 yes | 5.020540 yes | 5.060083 yes | 5.141018 yes | 5.195895 yes | 5.196959 yes |
| 1789048500 | fit | 5.061758 yes | 5.008831 yes | 4.748329 yes | 4.679775 yes | 4.666554 yes | 4.606958 yes | 4.552092 yes |
| 1789048800 | fit | 3.980512 yes | 4.023500 yes | 4.064326 yes | 4.120070 yes | 4.251229 yes | 4.312633 yes | 4.303428 yes |
| 1789049100 | fit | 4.839938 yes | 4.825583 yes | 4.799940 yes | 4.783279 yes | 4.742027 yes | 4.675676 yes | 4.637846 yes |
| 1789049400 | fit | 4.581799 yes | 4.703573 yes | 4.673656 yes | 4.592485 yes | 4.483420 yes | 4.427562 yes | 4.417975 yes |
| 1789049700 | fit | 4.000295 yes | 4.072788 yes | 4.097045 yes | 4.141943 yes | 4.099263 yes | 4.101808 yes | 4.256026 yes |
| 1789050300 | fit | 7.167226 yes | 6.948240 yes | 6.703509 yes | 6.557272 yes | 6.393257 yes | 6.231612 yes | 6.348237 yes |
| 1789050600 | fit | 4.850116 yes | 4.639115 yes | 4.606730 yes | 4.550410 yes | 4.470245 yes | 4.403307 yes | 4.359347 yes |
| 1789050900 | fit | 3.450560 yes | 3.450468 yes | 3.320765 yes | 3.288791 yes | 3.389907 yes | 3.401196 yes | 3.355303 yes |
| 1789051200 | fit | 3.052954 yes | 3.236843 yes | 3.166717 yes | 3.146056 yes | 3.088083 yes | 3.034076 yes | 2.987037 yes |
| 1789051500 | fit | 2.793427 yes | 2.802964 yes | 2.866506 yes | 2.860909 yes | 2.845320 yes | 2.882493 yes | 2.868132 yes |
| 1789051800 | fit | 2.900457 yes | 2.741500 yes | 2.779568 yes | 2.849069 yes | 2.799139 yes | 2.737199 yes | 2.699213 yes |
| 1789052100 | fit | 2.269082 yes | 2.265751 yes | 2.309735 yes | 2.416856 yes | 2.394138 yes | 2.377162 yes | 2.338997 yes |
| 1789052400 | fit | 2.493887 yes | 2.454149 yes | 2.648929 yes | 2.722186 yes | 2.746722 yes | 2.756737 yes | 2.726559 yes |
| 1789052700 | fit | 3.064629 yes | 3.077225 yes | 3.133799 yes | 3.103945 yes | 3.064728 yes | 3.047463 yes | 3.014501 yes |
| 1789053000 | fit | 3.002390 yes | 2.927235 yes | 2.796012 yes | 2.832028 yes | 2.806388 yes | 2.744849 yes | 2.711309 yes |
| 1789053300 | fit | 2.418353 yes | 2.348504 yes | 2.675574 yes | 2.603606 yes | 2.576998 yes | 2.570059 yes | 2.553995 yes |
| 1789053600 | fit | 2.718176 yes | 2.927959 yes | 2.976946 yes | 2.999549 yes | 3.009603 yes | 2.961898 yes | 2.975686 yes |
| 1789053900 | fit | 3.045188 yes | 2.882422 yes | 2.797881 yes | 2.848422 yes | 2.847555 yes | 2.827099 yes | 2.793538 yes |
| 1789054200 | fit | 2.445541 yes | 2.498167 yes | 2.653311 yes | 2.665365 yes | 2.654783 yes | 2.597699 yes | 2.644083 yes |
| 1789054500 | fit | 3.163717 yes | 3.225223 yes | 3.145912 yes | 3.093127 yes | 3.011437 yes | 3.035998 yes | 2.991508 yes |
| 1789054800 | fit | 3.167725 yes | 3.131045 yes | 3.029206 yes | 3.041452 yes | 2.981684 yes | 2.928589 yes | 2.889837 yes |
| 1789055100 | fit | 2.828206 yes | 3.001035 yes | 2.865076 yes | 2.830386 yes | 2.768557 yes | 2.730324 yes | 2.738437 yes |
| 1789055400 | fit | 3.228262 yes | 3.059717 yes | 3.045307 yes | 3.028759 yes | 2.957634 yes | 2.916383 yes | 2.880708 yes |
| 1789055700 | fit | 2.864725 yes | 3.150180 yes | 3.052158 yes | 2.991459 yes | 2.972500 yes | 2.932027 yes | 2.913426 yes |
| 1789056000 | fit | 3.015635 yes | 3.287131 yes | 3.453092 yes | 3.440590 yes | 3.385602 yes | 3.367242 yes | 3.326531 yes |
| 1789056300 | fit | 3.596994 yes | 3.385005 yes | 3.276350 yes | 3.270454 yes | 3.306192 yes | 3.262682 yes | 3.298302 yes |
| 1789056600 | fit | 3.418982 yes | 3.253072 yes | 3.219524 yes | 3.181193 yes | 3.124481 yes | 3.046002 yes | 2.997382 yes |
| 1789056900 | fit | 2.965367 yes | 2.928958 yes | 2.918154 yes | 3.046649 yes | 3.041902 yes | 3.010756 yes | 3.001390 yes |
| 1789057500 | fit | 3.450258 yes | 3.313154 yes | 3.192211 yes | 3.130928 yes | 3.067348 yes | 2.995280 yes | 2.960831 yes |
| 1789057800 | fit | 2.320927 yes | 2.250593 yes | 2.261149 yes | 2.232902 yes | 2.183919 yes | 2.727588 yes | 2.728855 yes |
| 1789058100 | fit | 3.118491 yes | 3.296915 yes | 3.403890 yes | 3.431951 yes | 3.417744 yes | 3.350535 yes | 3.341099 yes |
| 1789058400 | fit | 3.383448 yes | 3.232764 yes | 3.111457 yes | 3.088164 yes | 3.018224 yes | 3.016442 yes | 3.037330 yes |
| 1789058700 | fit | 2.508017 yes | 2.673630 yes | 2.717468 yes | 2.797298 yes | 2.761161 yes | 2.744933 yes | 2.709206 yes |
| 1789059000 | fit | 2.754990 yes | 2.667574 yes | 2.646231 yes | 2.680865 yes | 2.633149 yes | 2.613657 yes | 2.572602 yes |
| 1789059300 | fit | 2.376029 yes | 2.287203 yes | 2.177766 no | 2.231919 yes | 2.193640 yes | 2.142671 no | 2.115496 no |
| 1789059600 | fit | 2.035828 no | 2.085925 no | 2.750239 yes | 2.809934 yes | 2.756582 yes | 2.741544 yes | 2.718892 yes |
| 1789059900 | fit | 3.077008 yes | 3.012636 yes | 2.949578 yes | 2.884070 yes | 2.804280 yes | 2.732316 yes | 2.702838 yes |
| 1789060200 | fit | 2.085921 no | 1.984259 no | 2.199587 yes | 2.334827 yes | 2.286714 yes | 2.247965 yes | 2.216006 yes |
| 1789060500 | fit | 2.336575 yes | 2.521367 yes | 2.470131 yes | 2.484870 yes | 2.433569 yes | 2.381082 yes | 2.418091 yes |
| 1789060800 | fit | 3.375561 yes | 3.348635 yes | 3.252485 yes | 3.218382 yes | 3.139612 yes | 3.201532 yes | 3.183013 yes |
| 1789061100 | fit | 3.956830 yes | 3.726108 yes | 3.743981 yes | 3.764671 yes | 3.695410 yes | 3.615491 yes | 3.556993 yes |
| 1789061400 | fit | 3.519330 yes | 3.298169 yes | 4.175992 yes | 4.156401 yes | 4.152159 yes | 4.116530 yes | 4.213793 yes |
| 1789061700 | fit | 5.746136 yes | 5.525877 yes | 5.282026 yes | 5.200823 yes | 5.121290 yes | 5.013640 yes | 4.932699 yes |
| 1789062000 | fit | 4.766014 yes | 4.705121 yes | 4.505553 yes | 4.448688 yes | 4.344416 yes | 4.270351 yes | 4.228076 yes |
| 1789062300 | fit | 3.233863 yes | 3.415088 yes | 3.301011 yes | 3.249394 yes | 3.221506 yes | 3.210207 yes | 3.165644 yes |
| 1789062600 | fit | 2.855823 yes | 2.771498 yes | 2.647160 yes | 2.597066 yes | 2.649522 yes | 2.639921 yes | 2.630638 yes |
| 1789062900 | fit | 2.242987 yes | 2.121629 no | 2.125099 no | 2.073767 no | 2.032172 no | 2.009178 no | 1.980899 no |
| 1789063200 | fit | 1.786338 no | 1.922379 no | 1.922334 no | 1.952674 no | 1.950153 no | 1.911215 no | 1.914272 no |
| 1789063500 | fit | 2.401630 yes | 2.389219 yes | 2.294045 yes | 2.322941 yes | 2.287794 yes | 2.493896 yes | 2.491969 yes |
| 1789063800 | fit | 2.929701 yes | 2.755462 yes | 2.604518 yes | 2.541813 yes | 2.551806 yes | 2.491630 yes | 2.453937 yes |
| 1789064100 | fit | 1.845927 no | 2.177160 yes | 2.335763 yes | 2.271438 yes | 2.309721 yes | 2.265418 yes | 2.254945 yes |
| 1789064700 | fit | 1.953877 no | 1.943686 no | 1.883487 no | 1.920385 no | 1.907091 no | 1.922618 no | 1.892355 no |
| 1789065000 | fit | 1.664810 no | 1.560757 no | 1.620057 no | 1.650554 no | 1.712943 no | 1.737587 no | 1.776530 no |
| 1789065300 | fit | 1.840617 no | 1.950072 no | 1.899847 no | 1.878848 no | 1.882647 no | 1.900503 no | 1.876282 no |
| 1789065600 | fit | 1.784777 no | 1.718607 no | 1.631092 no | 1.656694 no | 1.623667 no | 1.610668 no | 1.592548 no |
| 1789065900 | fit | 1.324918 no | 1.342644 no | 1.384632 no | 1.371211 no | 1.340670 no | 1.976208 no | 2.038833 no |
| 1789066200 | fit | 2.615979 yes | 3.168437 yes | 3.111409 yes | 3.025159 yes | 3.159405 yes | 3.104428 yes | 3.120371 yes |
| 1789066500 | fit | 3.403394 yes | 3.220529 yes | 3.067434 yes | 3.040623 yes | 2.975449 yes | 2.974140 yes | 2.927885 yes |
| 1789066800 | fit | 2.121215 no | 2.238939 yes | 2.181880 yes | 2.140018 no | 2.189344 yes | 2.165497 yes | 2.163338 yes |
| 1789067100 | fit | 2.225875 yes | 2.086171 no | 2.124613 no | 2.074460 no | 2.023707 no | 2.969012 yes | 2.933419 yes |
| 1789067400 | fit | 3.318368 yes | 3.190094 yes | 3.007878 yes | 2.956474 yes | 2.878141 yes | 2.888819 yes | 2.861399 yes |
| 1789067700 | fit | 2.077454 no | 1.935865 no | 1.908707 no | 1.867803 no | 1.886530 no | 1.857180 no | 1.825962 no |
| 1789068000 | fit | 1.632448 no | 1.620109 no | 1.594307 no | 1.595697 no | 1.639633 no | 1.820693 no | 1.792632 no |
| 1789068300 | fit | 2.964055 yes | 2.752246 yes | 2.613997 yes | 2.542702 yes | 2.494815 yes | 2.524237 yes | 2.502239 yes |
| 1789068600 | fit | 3.353856 yes | 3.181273 yes | 3.012259 yes | 2.940570 yes | 2.894513 yes | 2.909700 yes | 2.868928 yes |
| 1789068900 | fit | 2.732022 yes | 2.581987 yes | 2.533408 yes | 2.465584 yes | 2.438741 yes | 2.383244 yes | 2.342953 yes |
| 1789069200 | fit | 2.551643 yes | 2.388414 yes | 2.280518 yes | 2.294675 yes | 2.253792 yes | 2.828986 yes | 2.831662 yes |
| 1789069500 | fit | 2.845661 yes | 2.734780 yes | 2.660345 yes | 2.624648 yes | 2.605367 yes | 2.573886 yes | 2.533775 yes |
| 1789069800 | fit | 1.991849 no | 2.563860 yes | 2.715852 yes | 2.659519 yes | 2.620618 yes | 2.554530 yes | 2.522185 yes |
| 1789070100 | fit | 2.846431 yes | 2.670417 yes | 2.521553 yes | 2.554856 yes | 2.584352 yes | 2.605848 yes | 2.588837 yes |
| 1789070400 | fit | 2.392754 yes | 2.231413 yes | 2.198894 yes | 2.405430 yes | 2.343156 yes | 2.316421 yes | 2.302694 yes |
| 1789070700 | fit | 2.261993 yes | 2.365733 yes | 2.413265 yes | 2.424601 yes | 2.391141 yes | 2.347420 yes | 2.343451 yes |
| 1789071000 | fit | 2.258153 yes | 2.237074 yes | 2.194188 yes | 2.130780 no | 2.090214 no | 2.083307 no | 2.056760 no |
| 1789071300 | fit | 1.875078 no | 1.861337 no | 1.779604 no | 1.731771 no | 1.687823 no | 1.676433 no | 1.657625 no |
| 1789071900 | fit | 1.543601 no | 1.480889 no | 1.448539 no | 1.412815 no | 1.426098 no | 1.394282 no | 1.381783 no |
| 1789072200 | fit | 1.244950 no | 1.484115 no | 1.496328 no | 1.509058 no | 1.539263 no | 1.517787 no | 1.547189 no |
| 1789072500 | fit | 1.746222 no | 1.654711 no | 1.649040 no | 1.602496 no | 1.557879 no | 1.523266 no | 1.543400 no |
| 1789073100 | fit | 1.126628 no | 1.061241 no | 1.144888 no | 1.133524 no | 1.226998 no | 1.207414 no | 1.196752 no |
| 1789073400 | fit | 1.393789 no | 1.488504 no | 1.774134 no | 1.725799 no | 1.686003 no | 1.665269 no | 1.639182 no |
| 1789073700 | fit | 1.621393 no | 1.542395 no | 1.485163 no | 1.474263 no | 1.576846 no | 1.539078 no | 1.519797 no |
| 1789074000 | fit | 1.212676 no | 1.691111 no | 1.724067 no | 1.680499 no | 1.642030 no | 1.603423 no | 1.576305 no |
| 1789074300 | fit | 1.900222 no | 1.775330 no | 2.188127 yes | 2.169997 yes | 2.137734 no | 2.111739 no | 2.079080 no |
| 1789074600 | fit | 2.168415 yes | 2.033842 no | 1.936305 no | 1.950832 no | 1.959408 no | 1.908608 no | 1.878191 no |
| 1789074900 | fit | 1.444406 no | 1.341993 no | 1.345880 no | 1.535874 no | 1.500403 no | 1.462562 no | 1.440682 no |
| 1789075200 | fit | 1.374847 no | 1.477176 no | 1.384706 no | 1.358886 no | 1.335930 no | 1.323772 no | 1.302706 no |
| 1789075500 | fit | 1.413915 no | 1.505566 no | 1.413731 no | 1.386980 no | 1.353533 no | 1.322310 no | 1.301470 no |
| 1789075800 | fit | 1.372828 no | 1.388821 no | 1.300140 no | 1.262065 no | 1.276995 no | 1.250692 no | 1.229748 no |
| 1789076100 | fit | 1.672885 no | 1.641833 no | 1.545555 no | 1.733264 no | 1.685022 no | 1.646140 no | 1.619088 no |
| 1789076400 | fit | 1.398659 no | 1.476668 no | 1.432555 no | 1.576569 no | 2.172395 yes | 2.793436 yes | 2.752351 yes |
| 1789076700 | fit | 3.324964 yes | 3.192478 yes | 3.017733 yes | 2.969103 yes | 2.952726 yes | 2.881365 yes | 2.841860 yes |
| 1789077000 | fit | 2.119264 no | 1.968587 no | 1.927812 no | 1.877227 no | 1.909137 no | 1.885676 no | 1.855375 no |
| 1789077300 | fit | 1.521971 no | 1.595359 no | 1.621825 no | 1.707981 no | 1.665633 no | 1.622909 no | 1.596240 no |
| 1789077600 | fit | 1.810312 no | 1.774125 no | 1.753287 no | 2.196834 yes | 2.140099 no | 2.119792 no | 2.174976 yes |
| 1789077900 | fit | 2.467610 yes | 2.309922 yes | 2.256523 yes | 2.247857 yes | 2.207689 yes | 2.152226 yes | 2.115750 no |
| 1789078200 | fit | 1.632387 no | 1.537304 no | 1.662143 no | 1.682358 no | 1.703722 no | 1.673486 no | 1.662072 no |
| 1789078500 | fit | 2.527885 yes | 2.376104 yes | 2.246067 yes | 2.203746 yes | 2.154055 no | 2.106382 no | 2.070672 no |
| 1789078800 | fit | 1.351756 no | 1.390584 no | 1.547722 no | 1.545226 no | 1.507318 no | 1.516223 no | 1.492916 no |
| 1789079100 | fit | 1.656671 no | 1.584515 no | 1.493072 no | 1.622382 no | 1.580275 no | 1.569728 no | 1.587769 no |
| 1789079400 | fit | 1.533562 no | 1.500238 no | 1.709249 no | 2.088327 no | 2.045986 no | 2.041317 no | 2.018415 no |
| 1789079700 | fit | 2.236021 yes | 2.181206 yes | 2.223430 yes | 2.163324 yes | 2.494091 yes | 2.478612 yes | 2.443847 yes |
| 1789080300 | fit | 2.610582 yes | 2.695940 yes | 2.593748 yes | 2.625361 yes | 2.553383 yes | 2.509700 yes | 2.467691 yes |
| 1789080600 | fit | 2.369354 yes | 2.383829 yes | 2.431433 yes | 2.462769 yes | 2.400723 yes | 2.346331 yes | 2.308147 yes |
| 1789080900 | fit | 2.133390 yes | 2.126697 no | 2.019088 no | 2.008683 no | 1.955394 no | 2.031969 no | 2.013746 no |
| 1789081200 | fit | 2.023419 no | 1.967174 no | 1.945929 no | 2.054487 no | 2.003029 no | 2.795141 yes | 2.800864 yes |
| 1789081500 | fit | 3.751113 yes | 3.725589 yes | 3.675870 yes | 3.693637 yes | 4.450379 yes | 4.518346 yes | 4.481975 yes |
| 1789081800 | fit | 5.003893 yes | 5.315978 yes | 5.087546 yes | 5.119687 yes | 4.991165 yes | 5.191493 yes | 5.177003 yes |
| 1789082100 | fit | 5.883900 yes | 6.284363 yes | 6.069558 yes | 5.971264 yes | 5.890328 yes | 5.785343 yes | 5.714497 yes |
| 1789082400 | fit | 5.754505 yes | 5.433930 yes | 5.243657 yes | 5.107741 yes | 5.013261 yes | 4.921407 yes | 4.870720 yes |
| 1789082700 | fit | 3.045457 yes | 2.988859 yes | 2.990415 yes | 2.992095 yes | 2.938967 yes | 2.903504 yes | 2.960849 yes |
| 1789083000 | fit | 2.931867 yes | 2.905022 yes | 2.923207 yes | 2.885263 yes | 2.814428 yes | 2.802709 yes | 2.792069 yes |
| 1789083300 | fit | 2.642643 yes | 2.645683 yes | 2.889934 yes | 2.891784 yes | 2.884683 yes | 2.909724 yes | 2.925441 yes |
| 1789083600 | fit | 2.951992 yes | 2.869047 yes | 2.794816 yes | 2.887763 yes | 2.926332 yes | 2.964926 yes | 2.945758 yes |
| 1789083900 | fit | 2.912414 yes | 2.889500 yes | 2.799274 yes | 2.734399 yes | 2.691574 yes | 2.680606 yes | 2.647538 yes |
| 1789084200 | fit | 2.509513 yes | 2.724362 yes | 2.645244 yes | 2.659699 yes | 2.596325 yes | 2.577719 yes | 2.626470 yes |
| 1789084500 | fit | 3.221644 yes | 3.332023 yes | 3.222053 yes | 3.440992 yes | 3.423063 yes | 3.357139 yes | 3.523993 yes |
| 1789084800 | fit | 4.166619 yes | 4.570296 yes | 4.591409 yes | 4.496351 yes | 4.399910 yes | 4.346451 yes | 4.328536 yes |
| 1789085100 | fit | 4.958920 yes | 4.819294 yes | 4.685056 yes | 4.613225 yes | 4.664620 yes | 4.589615 yes | 4.536266 yes |
| 1789086000 | fit | 2.402475 yes | 2.346679 yes | 2.354756 yes | 2.555587 yes | 2.495586 yes | 2.481968 yes | 2.444799 yes |
| 1789086300 | fit | 2.507595 yes | 2.613765 yes | 2.541615 yes | 2.771237 yes | 2.888936 yes | 2.942846 yes | 2.892918 yes |
| 1789086600 | fit | 2.941113 yes | 3.039610 yes | 3.341627 yes | 3.401883 yes | 3.374092 yes | 3.303231 yes | 3.702354 yes |
| 1789086900 | fit | 4.074851 yes | 3.953618 yes | 3.832295 yes | 3.733593 yes | 3.697480 yes | 3.624842 yes | 3.594289 yes |
| 1789087200 | fit | 2.603169 yes | 2.847742 yes | 2.786032 yes | 2.848091 yes | 2.810103 yes | 2.767298 yes | 2.726073 yes |
| 1789087500 | fit | 2.551439 yes | 2.460960 yes | 2.443208 yes | 2.389627 yes | 2.368318 yes | 2.392520 yes | 2.357942 yes |
| 1789087800 | fit | 2.043733 no | 2.054035 no | 2.122005 no | 2.089480 no | 2.203931 yes | 2.398130 yes | 2.377859 yes |
| 1789088100 | fit | 2.653533 yes | 2.583374 yes | 2.507459 yes | 2.463631 yes | 2.430875 yes | 2.409591 yes | 2.368978 yes |
| 1789088400 | fit | 2.192914 yes | 2.155750 yes | 2.290551 yes | 2.263961 yes | 2.223654 yes | 2.232702 yes | 2.218502 yes |
| 1789088700 | fit | 2.477451 yes | 2.349339 yes | 2.323363 yes | 2.285685 yes | 2.232656 yes | 2.177124 yes | 2.165985 yes |
| 1789089600 | fit | 3.468348 yes | 4.161498 yes | 3.990440 yes | 3.900853 yes | 3.806048 yes | 3.853756 yes | 3.798078 yes |
| 1789089900 | fit | 3.661355 yes | 3.707738 yes | 3.509531 yes | 3.405853 yes | 3.480560 yes | 3.417144 yes | 3.366769 yes |
| 1789090200 | fit | 2.772001 yes | 2.655061 yes | 2.879032 yes | 3.016117 yes | 3.109530 yes | 3.064775 yes | 3.027221 yes |
| 1789090500 | fit | 4.208617 yes | 4.294637 yes | 4.324660 yes | 4.208783 yes | 4.111226 yes | 4.053690 yes | 4.016181 yes |
| 1789090800 | fit | 3.820294 yes | 3.730090 yes | 3.649805 yes | 3.795278 yes | 3.754061 yes | 3.695508 yes | 3.664717 yes |
| 1789091100 | fit | 3.294800 yes | 3.167636 yes | 3.180424 yes | 3.162608 yes | 3.118893 yes | 3.058117 yes | 3.012170 yes |
| 1789092000 | fit | 1.833133 no | 1.936396 no | 1.890465 no | 1.834606 no | 1.784228 no | 1.861956 no | 1.847611 no |
| 1789092300 | fit | 2.179541 yes | 2.253297 yes | 2.466541 yes | 2.498305 yes | 2.554008 yes | 2.523132 yes | 2.495181 yes |
| 1789092600 | fit | 2.700453 yes | 2.644305 yes | 2.615587 yes | 2.566414 yes | 2.743579 yes | 2.685536 yes | 2.643792 yes |
| 1789092900 | fit | 2.673932 yes | 2.703847 yes | 2.723865 yes | 2.674695 yes | 2.652798 yes | 2.594473 yes | 2.552275 yes |
| 1789093200 | fit | 2.619173 yes | 2.699511 yes | 2.616244 yes | 2.635693 yes | 2.571347 yes | 2.526433 yes | 2.501650 yes |
| 1789093500 | fit | 2.242272 yes | 2.445732 yes | 2.472715 yes | 2.500993 yes | 2.442157 yes | 2.399847 yes | 2.360979 yes |
| 1789093800 | fit | 2.310752 yes | 2.241375 yes | 2.185252 yes | 2.134341 no | 2.076700 no | 2.079727 no | 2.092406 no |
| 1789094100 | fit | 1.844854 no | 1.860991 no | 2.145452 no | 2.090084 no | 2.186384 yes | 2.185069 yes | 2.150692 yes |
| 1789094400 | fit | 2.402170 yes | 2.320988 yes | 2.371689 yes | 2.387094 yes | 2.366827 yes | 2.315583 yes | 2.293060 yes |
| 1789094700 | fit | 2.170963 yes | 2.069320 no | 2.241496 yes | 2.244572 yes | 2.211209 yes | 2.155406 yes | 2.124102 no |
| 1789095000 | fit | 2.179114 yes | 2.036947 no | 2.005350 no | 1.998463 no | 1.999741 no | 2.743747 yes | 2.748660 yes |
| 1789095300 | fit | 3.160321 yes | 2.978984 yes | 3.012291 yes | 2.932952 yes | 2.853502 yes | 2.787055 yes | 2.742808 yes |
| 1789095600 | fit | 2.151181 yes | 2.248609 yes | 2.213190 yes | 2.155523 no | 2.102322 no | 2.181697 yes | 2.146125 yes |
| 1789095900 | fit | 2.109441 no | 2.685271 yes | 2.605365 yes | 2.534678 yes | 2.476257 yes | 2.488316 yes | 2.451921 yes |
| 1789096200 | fit | 2.847388 yes | 2.827003 yes | 3.246327 yes | 3.291509 yes | 3.517793 yes | 3.456251 yes | 3.412143 yes |
| 1789096500 | fit | 4.205392 yes | 4.082179 yes | 4.255440 yes | 4.227169 yes | 4.124506 yes | 4.023485 yes | 3.981681 yes |
| 1789096800 | fit | 3.714038 yes | 3.589210 yes | 3.791063 yes | 3.720864 yes | 3.621430 yes | 3.538336 yes | 3.482451 yes |
| 1789097100 | fit | 2.652968 yes | 2.524965 yes | 2.398916 yes | 2.438134 yes | 2.400603 yes | 2.351486 yes | 2.315536 yes |
| 1789097400 | fit | 2.165376 yes | 2.005994 no | 2.013876 no | 1.987532 no | 2.011832 no | 1.990606 no | 2.028809 no |
| 1789097700 | fit | 2.467720 yes | 2.458375 yes | 2.398786 yes | 2.446469 yes | 2.460697 yes | 2.411107 yes | 2.381661 yes |
| 1789098000 | fit | 2.292837 yes | 2.288253 yes | 2.565661 yes | 2.837904 yes | 2.858504 yes | 2.796528 yes | 2.750395 yes |
| 1789098300 | fit | 2.960632 yes | 2.780381 yes | 2.708557 yes | 2.642742 yes | 2.582472 yes | 2.517083 yes | 2.516934 yes |
| 1789099200 | fit | 2.068742 no | 2.258764 yes | 2.217373 yes | 2.154938 no | 2.188052 yes | 2.270856 yes | 2.236414 yes |
| 1789099500 | fit | 2.185509 yes | 2.156307 yes | 2.243166 yes | 2.190050 yes | 2.364690 yes | 2.363377 yes | 2.329583 yes |
| 1789099800 | fit | 2.285192 yes | 2.512054 yes | 2.427255 yes | 2.361917 yes | 2.360499 yes | 2.307134 yes | 2.305943 yes |
| 1789100100 | fit | 2.124102 yes | 2.022185 no | 2.599489 yes | 2.534203 yes | 2.485138 yes | 2.456222 yes | 2.414902 yes |
| 1789100400 | fit | 2.405862 yes | 2.292649 yes | 2.411742 yes | 2.354674 yes | 2.302474 yes | 2.250160 yes | 2.223234 yes |
| 1789100700 | fit | 2.362112 yes | 2.288480 yes | 2.346429 yes | 2.298116 yes | 2.293211 yes | 2.329246 yes | 2.320183 yes |
| 1789101000 | fit | 2.402015 yes | 2.308880 yes | 2.220994 yes | 2.185191 yes | 2.135174 no | 2.080591 no | 2.045863 no |
| 1789101300 | fit | 1.312074 no | 1.252635 no | 1.288523 no | 1.288867 no | 1.255602 no | 1.298627 no | 1.276937 no |
| 1789101600 | fit | 1.077044 no | 1.296495 no | 1.218896 no | 1.324596 no | 1.317643 no | 1.289295 no | 1.272875 no |
| 1789101900 | fit | 1.409081 no | 1.362055 no | 1.300971 no | 1.295739 no | 1.259795 no | 1.251298 no | 1.239754 no |
| 1789102500 | fit | 0.810862 no | 0.789351 no | 0.807560 no | 0.807108 no | 0.813719 no | 0.804234 no | 0.794147 no |
| 1789102800 | fit | 0.933965 no | 0.873680 no | 0.820451 no | 0.798222 no | 0.781822 no | 0.820988 no | 0.817282 no |
| 1789103100 | fit | 0.763285 no | 0.767218 no | 0.806331 no | 0.994028 no | 1.017473 no | 1.004523 no | 1.042956 no |
| 1789103400 | fit | 1.264674 no | 1.224810 no | 1.843412 no | 1.833594 no | 1.784760 no | 2.248694 yes | 2.211893 yes |
| 1789103700 | fit | 2.665888 yes | 2.635470 yes | 2.478295 yes | 2.424922 yes | 2.364679 yes | 2.307995 yes | 2.275122 yes |
| 1789104000 | fit | 1.480980 no | 2.065293 no | 2.007271 no | 1.956433 no | 1.910043 no | 1.867131 no | 1.838580 no |
| 1789104300 | fit | 2.029769 no | 1.899379 no | 2.049341 no | 2.008240 no | 1.956111 no | 1.914880 no | 1.889344 no |
| 1789104600 | fit | 1.728799 no | 1.647756 no | 2.242936 yes | 2.193819 yes | 2.143630 no | 2.126885 no | 2.092798 no |
| 1789104900 | fit | 2.302177 yes | 2.139135 no | 2.017739 no | 1.958634 no | 1.941394 no | 2.136860 no | 2.100825 no |
| 1789105200 | fit | 1.770364 no | 1.717822 no | 1.682160 no | 1.653731 no | 1.623948 no | 1.586703 no | 1.574307 no |
| 1789105500 | fit | 1.344080 no | 1.378225 no | 1.338931 no | 1.300891 no | 1.280646 no | 1.269849 no | 1.252636 no |
| 1789105800 | fit | 1.117254 no | 1.044535 no | 1.092738 no | 1.083752 no | 1.058891 no | 1.054802 no | 1.085603 no |
| 1789106100 | fit | 1.112885 no | 1.051519 no | 0.992620 no | 0.967652 no | 0.996937 no | 0.984425 no | 0.971706 no |
| 1789106400 | fit | 1.118728 no | 1.173953 no | 1.228902 no | 1.213255 no | 1.248255 no | 1.230758 no | 1.226648 no |
| 1789106700 | fit | 1.393326 no | 1.352203 no | 1.311909 no | 1.287059 no | 1.267357 no | 1.240187 no | 1.243205 no |
| 1789107000 | fit | 0.973192 no | 0.957615 no | 1.028617 no | 1.126289 no | 1.832114 no | 2.013913 no | 2.084791 no |
| 1789107900 | fit | 1.221950 no | 1.141388 no | 1.140291 no | 1.114406 no | 1.366131 no | 1.334696 no | 1.315550 no |
| 1789108200 | fit | 1.385355 no | 1.398838 no | 1.829437 no | 1.785618 no | 1.766889 no | 1.765932 no | 1.741400 no |
| 1789108500 | fit | 2.068792 no | 2.004339 no | 1.989701 no | 1.939780 no | 1.965836 no | 1.916929 no | 1.886790 no |
| 1789108800 | fit | 1.609348 no | 1.536679 no | 1.476636 no | 1.486939 no | 1.475075 no | 1.442198 no | 1.465381 no |
| 1789109100 | fit | 1.161364 no | 1.093783 no | 1.046180 no | 1.066817 no | 1.037810 no | 1.017240 no | 1.051575 no |
| 1789109400 | fit | 0.862774 no | 0.905071 no | 0.871570 no | 0.865707 no | 0.879970 no | 0.862520 no | 0.853663 no |
| 1789109700 | fit | 0.815936 no | 0.831330 no | 0.794422 no | 0.771067 no | 0.757652 no | 0.788945 no | 0.824258 no |
| 1789110000 | fit | 0.804388 no | 0.755388 no | 0.742846 no | 0.737430 no | 0.724932 no | 0.773846 no | 0.827590 no |
| 1789110300 | fit | 0.856151 no | 0.939383 no | 0.973002 no | 0.976767 no | 0.964773 no | 0.993603 no | 1.003946 no |
| 1789110600 | fit | 1.381453 no | 1.384650 no | 1.334630 no | 1.536825 no | 1.545047 no | 1.524887 no | 1.506369 no |
| 1789110900 | fit | 1.670873 no | 1.566186 no | 1.471222 no | 1.440282 no | 1.539760 no | 1.507378 no | 1.496681 no |
| 1789111200 | fit | 1.124574 no | 1.363451 no | 1.326951 no | 1.324107 no | 1.336641 no | 1.367270 no | 1.564768 no |
| 1789111500 | fit | 2.498193 yes | 2.429303 yes | 2.276882 yes | 2.235178 yes | 2.182291 yes | 2.127358 no | 2.094593 no |
| 1789111800 | fit | 1.779956 no | 1.875016 no | 1.760531 no | 1.717069 no | 1.694906 no | 2.345706 yes | 2.316946 yes |
| 1789112100 | fit | 2.473795 yes | 2.328076 yes | 2.181849 yes | 2.129875 no | 2.097360 no | 2.045454 no | 2.016366 no |
| 1789112400 | fit | 1.185772 no | 1.109650 no | 1.058794 no | 1.079729 no | 1.088576 no | 1.063886 no | 1.052845 no |
| 1789112700 | fit | 1.002741 no | 1.119445 no | 1.090384 no | 1.079305 no | 1.099983 no | 1.080574 no | 1.068508 no |
| 1789113000 | fit | 1.252070 no | 1.534436 no | 1.495145 no | 1.460187 no | 1.456396 no | 1.417849 no | 1.393928 no |
| 1789113300 | fit | 1.398828 no | 1.765872 no | 1.709117 no | 1.658482 no | 1.611791 no | 1.614047 no | 1.587256 no |
| 1789113600 | fit | 1.534317 no | 1.480279 no | 1.476195 no | 1.493341 no | 1.625461 no | 1.586992 no | 1.606077 no |
| 1789113900 | fit | 1.488199 no | 1.416038 no | 1.337241 no | 1.300240 no | 1.356398 no | 1.324234 no | 1.311622 no |
| 1789114200 | fit | 0.939845 no | 1.204783 no | 1.181636 no | 1.165711 no | 1.160984 no | 1.155706 no | 1.140708 no |
| 1789115100 | fit | 4.656427 yes | 4.412763 yes | 4.140245 yes | 4.110733 yes | 4.008912 yes | 3.913588 yes | 3.869484 yes |
| 1789115400 | fit | 3.194898 yes | 3.040584 yes | 3.013976 yes | 3.009213 yes | 2.939974 yes | 2.921197 yes | 2.873070 yes |
| 1789115700 | fit | 2.408213 yes | 2.261558 yes | 2.143936 no | 2.094765 no | 2.117438 no | 2.062069 no | 2.044946 no |
| 1789116000 | fit | 1.412931 no | 1.408597 no | 1.373213 no | 1.367468 no | 1.329878 no | 1.301084 no | 1.282562 no |
| 1789116300 | fit | 0.973177 no | 0.996987 no | 0.977414 no | 0.957786 no | 0.965141 no | 0.941560 no | 0.993068 no |
| 1789116600 | fit | 1.481615 no | 1.446633 no | 1.365925 no | 1.328100 no | 1.300670 no | 1.371795 no | 1.354481 no |
| 1789116900 | fit | 1.409303 no | 1.347686 no | 1.280272 no | 1.242799 no | 1.215313 no | 1.184833 no | 1.165491 no |
| 1789117200 | fit | 0.656464 no | 0.675772 no | 0.682267 no | 0.955782 no | 1.058277 no | 1.034728 no | 1.028245 no |
| 1789117500 | fit | 1.235875 no | 1.165959 no | 1.110563 no | 1.430034 no | 1.390556 no | 1.357870 no | 1.369592 no |
| 1789117800 | fit | 1.385244 no | 1.346110 no | 1.271229 no | 1.469247 no | 1.437317 no | 1.442160 no | 1.419540 no |
| 1789118100 | fit | 1.326182 no | 1.277007 no | 1.222505 no | 1.315844 no | 1.312969 no | 1.299999 no | 1.286525 no |
| 1789118400 | fit | 1.166041 no | 1.109868 no | 1.155972 no | 1.165184 no | 1.143740 no | 1.136844 no | 1.131830 no |
| 1789118700 | fit | 1.025293 no | 0.996208 no | 0.953779 no | 0.953846 no | 0.934065 no | 1.284422 no | 1.267426 no |
| 1789119000 | fit | 1.380391 no | 1.289747 no | 1.252020 no | 1.220819 no | 1.186710 no | 1.529595 no | 1.514990 no |
| 1789119300 | fit | 2.190108 yes | 2.257315 yes | 3.008859 yes | 2.928202 yes | 2.847214 yes | 2.827679 yes | 2.852304 yes |
| 1789119600 | fit | 3.765185 yes | 3.552198 yes | 3.555848 yes | 3.468595 yes | 3.407689 yes | 3.355192 yes | 3.299328 yes |
| 1789119900 | fit | 2.571590 yes | 2.394974 yes | 2.280446 yes | 2.217825 yes | 2.176635 yes | 2.135475 no | 2.100389 no |
| 1789120200 | fit | 1.237882 no | 1.716521 no | 1.634851 no | 1.588132 no | 1.560748 no | 1.535739 no | 1.511258 no |
| 1789120500 | fit | 1.757806 no | 1.699479 no | 1.608289 no | 1.610597 no | 1.588040 no | 1.565453 no | 1.541273 no |
| 1789120800 | fit | 1.118763 no | 1.070371 no | 2.947062 yes | 2.971307 yes | 2.901101 yes | 2.845002 yes | 2.800686 yes |
| 1789121100 | fit | 3.728715 yes | 3.471159 yes | 3.253890 yes | 3.167409 yes | 3.081745 yes | 3.209118 yes | 3.168462 yes |
| 1789121400 | fit | 2.156315 yes | 2.059099 no | 2.184352 yes | 2.211590 yes | 2.171136 yes | 2.434458 yes | 2.395459 yes |
| 1789122300 | fit | 2.418845 yes | 2.416612 yes | 2.310030 yes | 2.248287 yes | 2.185945 yes | 2.128456 no | 2.105908 no |
| 1789122600 | fit | 1.284815 no | 1.204368 no | 1.876287 no | 1.938943 no | 1.888390 no | 1.875597 no | 1.856280 no |
| 1789122900 | fit | 2.074492 no | 2.107505 no | 2.025012 no | 2.008840 no | 1.967023 no | 1.931079 no | 1.898868 no |
| 1789123200 | fit | 2.341378 yes | 2.252091 yes | 2.176095 no | 2.139873 no | 2.080864 no | 2.044793 no | 2.049762 no |
| 1789123500 | fit | 2.326475 yes | 2.210287 yes | 2.145236 no | 2.083247 no | 2.024929 no | 2.004015 no | 1.970725 no |
| 1789123800 | fit | 1.058935 no | 1.451139 no | 1.389978 no | 1.388130 no | 1.360446 no | 1.335197 no | 1.313907 no |
| 1789124100 | fit | 1.333636 no | 1.283515 no | 1.276378 no | 1.294537 no | 1.281920 no | 1.340418 no | 1.365894 no |
| 1789124400 | fit | 1.383608 no | 1.457799 no | 1.499628 no | 1.533550 no | 1.535892 no | 1.579537 no | 1.567822 no |
| 1789124700 | fit | 1.781696 no | 2.399053 yes | 2.566867 yes | 2.521603 yes | 2.461445 yes | 2.403292 yes | 2.387713 yes |
| 1789125000 | fit | 3.027831 yes | 3.109568 yes | 2.986299 yes | 3.064978 yes | 3.016123 yes | 2.937227 yes | 2.996862 yes |
| 1789125300 | fit | 3.530277 yes | 3.536202 yes | 3.399479 yes | 3.313217 yes | 3.241502 yes | 3.168642 yes | 3.201044 yes |
| 1789125600 | fit | 2.972507 yes | 2.803562 yes | 2.768868 yes | 2.720058 yes | 2.668373 yes | 2.617198 yes | 2.574241 yes |
| 1789125900 | fit | 2.184525 yes | 2.104195 no | 2.105239 no | 2.074093 no | 2.076181 no | 2.022031 no | 1.991867 no |
| 1789126200 | fit | 2.165068 yes | 2.058730 no | 1.945734 no | 1.968494 no | 1.948682 no | 1.897201 no | 2.153289 yes |
| 1789126500 | fit | 1.919156 no | 1.953419 no | 1.992469 no | 2.009392 no | 1.966240 no | 1.974010 no | 1.945771 no |
| 1789126800 | fit | 1.843658 no | 1.747344 no | 1.869207 no | 1.853107 no | 1.822085 no | 1.837702 no | 1.815414 no |
| 1789127100 | fit | 1.840318 no | 2.160613 yes | 2.258663 yes | 2.241402 yes | 2.179296 yes | 2.177377 yes | 2.155732 yes |
| 1789127400 | fit | 2.659261 yes | 2.499896 yes | 2.479591 yes | 2.451178 yes | 2.453553 yes | 2.464957 yes | 2.439460 yes |
| 1789128300 | fit | 3.026325 yes | 2.991668 yes | 3.136060 yes | 3.050811 yes | 2.976509 yes | 2.965158 yes | 2.928350 yes |
| 1789128600 | fit | 3.251596 yes | 3.181223 yes | 3.115350 yes | 3.113130 yes | 3.042113 yes | 3.051770 yes | 3.020441 yes |
| 1789128900 | fit | 3.835236 yes | 4.061946 yes | 3.980769 yes | 3.893300 yes | 4.208871 yes | 4.195278 yes | 4.176613 yes |
| 1789129200 | fit | 4.827940 yes | 4.957980 yes | 4.699837 yes | 4.624667 yes | 4.543780 yes | 4.504193 yes | 4.461006 yes |
| 1789129500 | fit | 3.680099 yes | 3.754740 yes | 3.604293 yes | 3.664354 yes | 3.945610 yes | 3.968727 yes | 9.213254 yes |
| 1789129800 | fit | 29.735992 yes | 28.942455 yes | 27.672332 yes | 27.131567 yes | 26.936372 yes | 26.800266 yes | 26.655967 yes |
| 1789130100 | fit | 32.770517 yes | 30.927778 yes | 29.580957 yes | 28.967506 yes | 28.199996 yes | 27.753578 yes | 27.345725 yes |
| 1789130400 | fit | 15.079913 yes | 14.435347 yes | 14.007862 yes | 13.884297 yes | 13.659682 yes | 13.364504 yes | 13.253828 yes |
| 1789131600 | fit | 8.191082 yes | 7.862209 yes | 7.587876 yes | 7.473560 yes | 7.429204 yes | 7.255558 yes | 7.234395 yes |
| 1789131900 | fit | 5.868821 yes | 5.628768 yes | 5.555667 yes | 5.722587 yes | 5.678229 yes | 5.769010 yes | 5.740566 yes |
| 1789132200 | fit | 5.691573 yes | 5.609323 yes | 5.425065 yes | 5.841625 yes | 5.771198 yes | 5.729206 yes | 5.648495 yes |
| 1789132500 | fit | 5.325688 yes | 5.212435 yes | 5.096866 yes | 5.133786 yes | 5.009821 yes | 4.947249 yes | 4.874234 yes |
| 1789132800 | fit | 4.645725 yes | 4.689276 yes | 4.634946 yes | 4.660881 yes | 4.641756 yes | 4.554110 yes | 4.535891 yes |
| 1789133100 | fit | 5.187959 yes | 5.682333 yes | 5.677045 yes | 6.019750 yes | 6.210889 yes | 6.127766 yes | 6.107973 yes |
| 1789133400 | fit | 7.637128 yes | 8.138093 yes | 8.525664 yes | 8.473201 yes | 8.354937 yes | 8.408861 yes | 8.300727 yes |
| 1789133700 | fit | 9.564105 yes | 9.858503 yes | 10.181778 yes | 10.306347 yes | 10.153913 yes | 10.000909 yes | 9.897701 yes |
| 1789134000 | fit | 11.643149 yes | 11.800790 yes | 11.362772 yes | 11.366906 yes | 11.286983 yes | 11.079439 yes | 11.035801 yes |
| 1789134300 | fit | 11.823860 yes | 11.429953 yes | 11.119870 yes | 10.903613 yes | 10.730501 yes | 11.034375 yes | 11.398262 yes |
| 1789134600 | fit | 11.306891 yes | 11.627685 yes | 11.859788 yes | 11.883941 yes | 11.827986 yes | 11.573271 yes | 11.485663 yes |
| 1789134900 | fit | 11.898995 yes | 11.395420 yes | 10.961230 yes | 10.886348 yes | 10.856826 yes | 11.252408 yes | 11.311323 yes |
| 1789135200 | fit | 13.167956 yes | 13.254603 yes | 13.724135 yes | 14.835138 yes | 14.676743 yes | 14.522316 yes | 14.380374 yes |
| 1789135500 | fit | 16.668764 yes | 16.056573 yes | 15.290738 yes | 15.201825 yes | 14.913407 yes | 14.839584 yes | 14.708441 yes |
| 1789135800 | fit | 11.196033 yes | 10.976651 yes | 10.843855 yes | 10.733407 yes | 10.637170 yes | 10.530434 yes | 10.464689 yes |
| 1789136100 | fit | 9.555025 yes | 9.421850 yes | 9.996522 yes | 10.020206 yes | 9.861436 yes | 9.768521 yes | 9.647930 yes |
| 1789136400 | fit | 9.570964 yes | 9.141258 yes | 8.740667 yes | 8.528581 yes | 8.448648 yes | 8.340907 yes | 8.224088 yes |
| 1789136700 | fit | 6.743170 yes | 6.759378 yes | 6.634185 yes | 6.728969 yes | 6.699914 yes | 6.841235 yes | 6.741632 yes |
| 1789137000 | fit | 7.174314 yes | 7.047303 yes | 7.119929 yes | 7.233745 yes | 7.101862 yes | 7.358967 yes | 7.342836 yes |
| 1789137300 | fit | 7.591136 yes | 7.639565 yes | 7.527514 yes | 7.417138 yes | 7.292350 yes | 7.378071 yes | 7.310731 yes |
| 1789137600 | fit | 6.781191 yes | 6.472262 yes | 6.246377 yes | 6.150437 yes | 6.021081 yes | 6.033025 yes | 5.988060 yes |
| 1789137900 | fit | 4.784084 yes | 4.686515 yes | 5.226051 yes | 5.616511 yes | 7.898895 yes | 8.069111 yes | 8.004300 yes |
| 1789138800 | fit | 4.396886 yes | 4.809495 yes | 5.140146 yes | 5.227037 yes | 5.176021 yes | 5.245707 yes | 5.172431 yes |
| 1789139100 | fit | 6.227934 yes | 6.024177 yes | 5.904619 yes | 5.826348 yes | 5.828882 yes | 5.776650 yes | 5.703948 yes |
| 1789139400 | fit | 4.902455 yes | 4.781611 yes | 4.941980 yes | 4.920364 yes | 5.168499 yes | 5.274196 yes | 5.267989 yes |
| 1789139700 | fit | 5.805594 yes | 5.677685 yes | 5.436345 yes | 5.340696 yes | 5.275072 yes | 5.169352 yes | 5.181696 yes |
| 1789140000 | fit | 4.502408 yes | 4.422537 yes | 4.290780 yes | 4.357335 yes | 4.595420 yes | 4.521458 yes | 4.497454 yes |
| 1789140300 | fit | 3.938047 yes | 3.984343 yes | 3.849509 yes | 3.805509 yes | 3.711114 yes | 3.748143 yes | 3.724130 yes |
| 1789140600 | fit | 3.059405 yes | 3.526465 yes | 3.574326 yes | 3.490062 yes | 3.447936 yes | 3.400353 yes | 3.424332 yes |
| 1789140900 | fit | 3.448023 yes | 4.508964 yes | 4.625540 yes | 4.556978 yes | 4.500287 yes | 4.467179 yes | 4.406004 yes |
| 1789141800 | fit | 4.408432 yes | 5.772126 yes | 8.601598 yes | 8.855236 yes | 9.680970 yes | 10.400503 yes | 10.965180 yes |
| 1789142100 | fit | 16.538634 yes | 16.197711 yes | 15.655683 yes | 15.280328 yes | 15.117729 yes | 14.833324 yes | 14.627270 yes |
| 1789142400 | fit | 13.417413 yes | 12.522129 yes | 11.927401 yes | 11.629099 yes | 11.381835 yes | 11.239336 yes | 11.096865 yes |
| 1789142700 | fit | 7.035410 yes | 6.706373 yes | 6.854731 yes | 6.704094 yes | 6.703561 yes | 6.590298 yes | 6.518232 yes |
| 1789143000 | fit | 5.667113 yes | 5.439781 yes | 5.447355 yes | 5.566780 yes | 5.604079 yes | 5.610023 yes | 5.572542 yes |
| 1789143300 | fit | 5.610787 yes | 5.374866 yes | 5.375707 yes | 5.707832 yes | 6.151472 yes | 6.485859 yes | 6.487542 yes |
| 1789143600 | fit | 8.280758 yes | 8.740433 yes | 8.526691 yes | 8.401929 yes | 8.311561 yes | 8.159639 yes | 8.122481 yes |
| 1789143900 | fit | 8.142506 yes | 7.903640 yes | 7.743014 yes | 7.620143 yes | 7.415457 yes | 7.549841 yes | 7.571892 yes |
| 1789144200 | fit | 6.425370 yes | 6.520494 yes | 6.605971 yes | 6.602675 yes | 6.488733 yes | 6.501912 yes | 6.419102 yes |
| 1789144500 | fit | 6.199105 yes | 5.954773 yes | 5.822558 yes | 5.723825 yes | 5.592977 yes | 5.496215 yes | 5.428551 yes |
| 1789144800 | fit | 4.464670 yes | 4.412530 yes | 4.201593 yes | 4.212759 yes | 4.103393 yes | 4.003893 yes | 3.938453 yes |
| 1789145100 | fit | 3.764916 yes | 3.647973 yes | 4.088433 yes | 4.032750 yes | 4.108138 yes | 4.064544 yes | 4.038588 yes |
| 1789145400 | fit | 4.912855 yes | 4.700118 yes | 4.637356 yes | 4.637746 yes | 4.557505 yes | 4.451648 yes | 4.401226 yes |
| 1789145700 | fit | 4.026522 yes | 3.818975 yes | 4.041689 yes | 4.144385 yes | 4.061044 yes | 4.047116 yes | 3.989888 yes |
| 1789146000 | fit | 4.094173 yes | 3.981708 yes | 4.443931 yes | 4.405323 yes | 4.321358 yes | 4.257733 yes | 4.249481 yes |
| 1789146300 | fit | 4.525869 yes | 4.337060 yes | 4.927663 yes | 4.823107 yes | 4.759577 yes | 4.679126 yes | 4.620483 yes |
| 1789146600 | fit | 4.196810 yes | 4.215204 yes | 4.160579 yes | 4.089675 yes | 3.975171 yes | 4.051801 yes | 4.009083 yes |
| 1789146900 | fit | 3.494646 yes | 3.555623 yes | 3.693975 yes | 3.625227 yes | 3.618513 yes | 3.565710 yes | 3.543506 yes |
| 1789147200 | fit | 3.444039 yes | 3.633835 yes | 3.668615 yes | 3.690805 yes | 3.713963 yes | 3.632641 yes | 3.580000 yes |
| 1789147500 | fit | 3.409682 yes | 3.286826 yes | 3.267979 yes | 3.182868 yes | 3.098408 yes | 3.033072 yes | 3.013707 yes |
| 1789147800 | fit | 2.360181 yes | 2.864811 yes | 2.747228 yes | 2.702891 yes | 2.709008 yes | 2.676796 yes | 2.774552 yes |
| 1789148100 | fit | 3.021396 yes | 2.983669 yes | 2.908326 yes | 2.942176 yes | 2.874770 yes | 3.120815 yes | 3.079342 yes |
| 1789149000 | fit | 2.365959 yes | 2.244712 yes | 2.359986 yes | 2.305877 yes | 2.270769 yes | 2.210733 yes | 2.209023 yes |
| 1789149300 | fit | 1.933785 no | 2.259796 yes | 2.405101 yes | 2.371738 yes | 2.635484 yes | 2.570331 yes | 2.526771 yes |
| 1789149600 | fit | 2.985547 yes | 3.510266 yes | 3.575105 yes | 5.546511 yes | 5.657742 yes | 5.675458 yes | 5.657572 yes |
| 1789149900 | fit | 7.769494 yes | 8.326906 yes | 8.106237 yes | 8.021998 yes | 8.063641 yes | 7.921498 yes | 7.815311 yes |
| 1789150200 | fit | 7.923932 yes | 7.624657 yes | 7.181359 yes | 7.036545 yes | 6.874613 yes | 6.836598 yes | 6.863725 yes |
| 1789150500 | fit | 6.119736 yes | 5.883412 yes | 5.660471 yes | 5.535070 yes | 5.455785 yes | 5.334020 yes | 5.266969 yes |
| 1789150800 | fit | 5.065517 yes | 5.117500 yes | 4.915801 yes | 4.784035 yes | 4.686337 yes | 4.565041 yes | 4.492784 yes |
| 1789151100 | fit | 4.300333 yes | 4.647771 yes | 4.555674 yes | 4.543607 yes | 4.481587 yes | 4.419155 yes | 4.371767 yes |
| 1789151400 | fit | 3.834567 yes | 3.751665 yes | 3.697400 yes | 3.726019 yes | 3.641801 yes | 3.658101 yes | 3.601808 yes |
| 1789151700 | fit | 3.247068 yes | 3.136374 yes | 3.095757 yes | 3.079650 yes | 3.013220 yes | 3.063203 yes | 3.013271 yes |
| 1789152000 | fit | 2.833547 yes | 3.173888 yes | 3.174210 yes | 3.095991 yes | 3.045032 yes | 2.970574 yes | 2.937025 yes |
| 1789152300 | fit | 4.386853 yes | 4.440363 yes | 4.220674 yes | 4.231156 yes | 4.652200 yes | 4.554298 yes | 4.793974 yes |
| 1789152600 | fit | 5.656493 yes | 5.283510 yes | 4.983201 yes | 4.933197 yes | 4.909641 yes | 4.878037 yes | 4.829200 yes |
| 1789152900 | fit | 3.685233 yes | 3.561777 yes | 3.383795 yes | 3.284427 yes | 3.233697 yes | 3.166801 yes | 3.125963 yes |
| 1789153800 | fit | 3.499256 yes | 3.595914 yes | 3.447874 yes | 3.378914 yes | 3.310034 yes | 3.231824 yes | 3.188969 yes |
| 1789154100 | fit | 2.577960 yes | 2.566877 yes | 3.120574 yes | 3.086236 yes | 3.066403 yes | 3.026420 yes | 3.094386 yes |
| 1789154400 | fit | 3.690386 yes | 3.583510 yes | 3.403051 yes | 3.303479 yes | 3.215113 yes | 3.268614 yes | 3.231395 yes |
| 1789154700 | fit | 2.949824 yes | 2.799242 yes | 2.701308 yes | 2.651676 yes | 2.611424 yes | 2.563105 yes | 2.542314 yes |
| 1789155000 | fit | 2.319264 yes | 2.287069 yes | 2.205941 yes | 2.218501 yes | 2.200143 yes | 2.163311 yes | 2.160641 yes |
| 1789155300 | fit | 2.332608 yes | 2.376139 yes | 2.251891 yes | 3.086211 yes | 3.045911 yes | 3.112132 yes | 3.065639 yes |
| 1789155600 | fit | 3.885752 yes | 3.676308 yes | 3.449742 yes | 3.359795 yes | 3.286085 yes | 3.202819 yes | 3.162709 yes |
| 1789155900 | fit | 2.430806 yes | 2.475822 yes | 2.451761 yes | 2.409767 yes | 2.503530 yes | 2.591262 yes | 2.568651 yes |
| 1789156200 | fit | 2.727387 yes | 2.564203 yes | 2.572749 yes | 2.499368 yes | 2.461884 yes | 2.455179 yes | 2.603127 yes |
| 1789156500 | fit | 2.439779 yes | 2.410267 yes | 2.357512 yes | 2.414307 yes | 2.372534 yes | 2.365140 yes | 2.340153 yes |
| 1789156800 | fit | 2.574404 yes | 2.453563 yes | 2.799458 yes | 3.045078 yes | 2.999736 yes | 2.948070 yes | 2.905705 yes |
| 1789157100 | fit | 2.937523 yes | 2.762332 yes | 2.696414 yes | 2.618696 yes | 2.546333 yes | 2.503145 yes | 2.474180 yes |
| 1789157400 | fit | 1.467621 no | 2.233370 yes | 2.191379 yes | 2.184080 yes | 2.151511 no | 2.095035 no | 2.075696 no |
| 1789157700 | fit | 2.332674 yes | 2.236794 yes | 2.111401 no | 2.369816 yes | 2.316484 yes | 2.280278 yes | 2.256528 yes |
| 1789158000 | fit | 1.819235 no | 1.742711 no | 1.852683 no | 1.843434 no | 1.795136 no | 1.811834 no | 1.827517 no |
| 1789158300 | fit | 2.101698 no | 1.971890 no | 1.867018 no | 1.821991 no | 2.182301 yes | 2.125548 no | 2.143372 no |
| 1789158600 | fit | 2.374891 yes | 2.378507 yes | 3.826131 yes | 3.824812 yes | 3.814089 yes | 3.719869 yes | 3.660013 yes |
| 1789158900 | fit | 4.104327 yes | 3.919972 yes | 3.768217 yes | 3.667870 yes | 3.567480 yes | 3.478256 yes | 3.420844 yes |
| 1789159200 | fit | 1.712430 no | 3.169142 yes | 3.011582 yes | 2.949841 yes | 2.899455 yes | 2.873318 yes | 2.896996 yes |
| 1789159500 | fit | 3.355694 yes | 3.212226 yes | 3.020437 yes | 2.932205 yes | 2.929830 yes | 2.913524 yes | 2.987343 yes |
| 1789159800 | fit | 2.395973 yes | 2.638931 yes | 3.366197 yes | 3.384435 yes | 3.303928 yes | 3.313394 yes | 3.282099 yes |
| 1789160100 | fit | 3.966960 yes | 3.809343 yes | 3.603719 yes | 3.505962 yes | 3.476128 yes | 3.393260 yes | 3.372181 yes |
| 1789161000 | fit | 1.823379 no | 1.853008 no | 1.785152 no | 1.843333 no | 1.965337 no | 2.004850 no | 1.979339 no |
| 1789161300 | fit | 2.218792 yes | 2.091456 no | 2.007325 no | 1.951886 no | 1.904672 no | 1.854197 no | 1.822859 no |
| 1789161600 | fit | 0.920276 no | 1.008752 no | 0.954334 no | 0.933201 no | 0.934023 no | 0.997677 no | 0.985458 no |
| 1789161900 | fit | 1.577700 no | 1.673472 no | 1.677697 no | 1.875530 no | 1.840312 no | 1.792394 no | 1.773702 no |
| 1789162500 | fit | 1.270481 no | 1.240234 no | 1.488893 no | 1.546830 no | 1.525209 no | 1.509497 no | 1.552099 no |
| 1789162800 | fit | 1.980521 no | 1.852122 no | 1.777435 no | 1.762062 no | 1.733509 no | 1.714071 no | 1.686691 no |
| 1789163100 | fit | 1.584847 no | 1.663775 no | 1.791200 no | 1.863685 no | 1.812552 no | 1.851994 no | 1.822776 no |
| 1789163400 | fit | 1.924340 no | 1.863552 no | 1.881467 no | 1.915081 no | 1.984072 no | 1.936372 no | 1.907504 no |
| 1789163700 | fit | 1.962004 no | 2.180696 yes | 2.149725 no | 2.090457 no | 2.158188 no | 2.136811 no | 2.251895 yes |
| 1789164000 | fit | 3.697709 yes | 4.087685 yes | 4.106631 yes | 4.085152 yes | 4.031937 yes | 4.039655 yes | 3.982317 yes |
| 1789164300 | fit | 5.003300 yes | 4.707040 yes | 4.493337 yes | 4.402720 yes | 4.305378 yes | 4.220074 yes | 4.182911 yes |
| 1789164600 | fit | 3.219301 yes | 3.094486 yes | 2.939934 yes | 2.856336 yes | 2.791178 yes | 2.724631 yes | 2.680463 yes |
| 1789164900 | fit | 2.881768 yes | 2.741945 yes | 2.579008 yes | 2.503947 yes | 2.434972 yes | 2.372065 yes | 2.332624 yes |
| 1789165200 | fit | 2.682663 yes | 2.812917 yes | 2.860741 yes | 2.852608 yes | 2.781373 yes | 2.709567 yes | 2.675584 yes |
| 1789165500 | fit | 2.273055 yes | 2.553279 yes | 2.440447 yes | 2.720229 yes | 3.206178 yes | 3.148962 yes | 3.097955 yes |
| 1789165800 | fit | 3.464401 yes | 3.381724 yes | 3.258990 yes | 3.268356 yes | 3.202277 yes | 3.354568 yes | 3.319399 yes |
| 1789166100 | fit | 4.208472 yes | 4.028024 yes | 3.857851 yes | 4.010258 yes | 3.899847 yes | 3.822064 yes | 3.764854 yes |
| 1789166400 | fit | 4.058978 yes | 3.787812 yes | 3.615944 yes | 3.536714 yes | 3.451114 yes | 4.002708 yes | 4.030606 yes |
| 1789166700 | test1 | 3.327154 yes | 3.081911 yes | 3.020548 yes | 2.930684 yes | 2.879952 yes | 2.804751 yes | 2.792778 yes |
| 1789167000 | test1 | 2.225456 yes | 2.116756 no | 3.207792 yes | 3.120585 yes | 3.143553 yes | 3.076755 yes | 3.100083 yes |
| 1789167300 | test1 | 4.016702 yes | 3.841934 yes | 4.239661 yes | 4.388302 yes | 4.282528 yes | 4.347644 yes | 4.365860 yes |
| 1789167600 | test1 | 4.464864 yes | 4.243873 yes | 3.984651 yes | 3.867185 yes | 3.760131 yes | 3.669500 yes | 3.615708 yes |
| 1789167900 | test1 | 1.987307 no | 2.023783 no | 2.164847 no | 2.150379 no | 2.146571 no | 2.169167 yes | 2.242740 yes |
| 1789168200 | test1 | 2.399686 yes | 2.359283 yes | 2.605161 yes | 2.609120 yes | 2.597186 yes | 2.585304 yes | 2.565745 yes |
| 1789168500 | test1 | 2.490850 yes | 2.356422 yes | 2.230590 yes | 2.201879 yes | 2.141666 no | 2.085488 no | 2.054317 no |
| 1789168800 | test1 | 1.136128 no | 1.071844 no | 1.068058 no | 1.161207 no | 1.157254 no | 1.141875 no | 1.171329 no |
| 1789169100 | test1 | 1.261614 no | 1.326197 no | 1.299883 no | 1.308010 no | 1.272607 no | 1.239582 no | 1.219216 no |
| 1789169700 | test1 | 0.641416 no | 0.607359 no | 0.765153 no | 0.745341 no | 0.739419 no | 0.721709 no | 0.711106 no |
| 1789170600 | test1 | 2.772032 yes | 2.593349 yes | 2.536567 yes | 2.487845 yes | 2.417785 yes | 2.365165 yes | 2.330580 yes |
| 1789170900 | test1 | 1.213914 no | 1.143614 no | 1.092007 no | 1.064785 no | 1.161445 no | 1.158135 no | 1.156031 no |
| 1789171200 | test1 | 1.320514 no | 2.755056 yes | 2.606698 yes | 2.543935 yes | 2.479898 yes | 2.419227 yes | 2.382056 yes |
| 1789171500 | test1 | 3.099831 yes | 2.964358 yes | 2.779519 yes | 2.751964 yes | 2.678101 yes | 2.615873 yes | 2.579623 yes |
| 1789171800 | test1 | 1.686360 no | 1.568336 no | 1.509612 no | 1.467887 no | 1.433345 no | 1.397515 no | 1.374151 no |
| 1789172100 | test1 | 1.096820 no | 1.129531 no | 1.063473 no | 1.035994 no | 1.027282 no | 1.000948 no | 0.985352 no |
| 1789172400 | test1 | 1.100739 no | 1.048068 no | 1.038723 no | 1.011398 no | 0.985814 no | 0.961700 no | 0.949836 no |
| 1789172700 | test1 | 0.833034 no | 0.943978 no | 0.887499 no | 0.863947 no | 0.885605 no | 0.862223 no | 0.874768 no |
| 1789173000 | test1 | 1.143979 no | 1.069833 no | 1.075758 no | 1.045847 no | 1.118187 no | 1.093007 no | 1.075044 no |
| 1789173300 | test1 | 1.289575 no | 1.251843 no | 1.247828 no | 1.212292 no | 1.179348 no | 1.154437 no | 1.156636 no |
| 1789173600 | test1 | 0.944670 no | 0.880001 no | 1.209655 no | 1.207448 no | 1.177109 no | 1.149215 no | 1.133859 no |
| 1789173900 | test1 | 1.133587 no | 1.050643 no | 1.083233 no | 1.060825 no | 1.031525 no | 1.005317 no | 0.990948 no |
| 1789174200 | test1 | 0.584179 no | 0.677124 no | 0.639293 no | 0.821708 no | 0.799929 no | 0.792667 no | 0.920988 no |
| 1789174500 | test1 | 1.100130 no | 1.058250 no | 0.991508 no | 0.997636 no | 0.973412 no | 0.948523 no | 0.934380 no |
| 1789174800 | test1 | 1.003119 no | 0.957065 no | 1.028844 no | 1.026676 no | 1.006888 no | 1.018199 no | 1.027671 no |
| 1789175100 | test1 | 1.632746 no | 1.565842 no | 1.481483 no | 1.440790 no | 1.408874 no | 1.391956 no | 1.372720 no |
| 1789175400 | test1 | 0.898085 no | 0.866533 no | 0.826886 no | 0.802420 no | 0.780885 no | 0.767653 no | 0.795563 no |
| 1789175700 | test1 | 0.626159 no | 0.612563 no | 0.586369 no | 0.596626 no | 0.598934 no | 0.585269 no | 0.665110 no |
| 1789176000 | test1 | 0.778163 no | 0.789638 no | 0.800293 no | 0.791964 no | 0.773314 no | 0.754542 no | 0.754389 no |
| 1789176300 | test1 | 0.899840 no | 0.935480 no | 0.917493 no | 0.895887 no | 0.961046 no | 0.941374 no | 0.925727 no |
| 1789176600 | test1 | 0.982764 no | 0.930198 no | 0.874902 no | 0.860108 no | 0.841332 no | 0.819770 no | 0.806256 no |
| 1789176900 | test1 | 0.493212 no | 0.489446 no | 0.472473 no | 0.737328 no | 0.803309 no | 0.790390 no | 1.182935 no |
| 1789177800 | test1 | 0.967670 no | 0.915077 no | 1.910942 no | 1.869996 no | 1.818750 no | 1.796415 no | 1.767395 no |
| 1789178100 | test1 | 2.081621 no | 1.930164 no | 1.832246 no | 1.782004 no | 1.759827 no | 1.786691 no | 1.801532 no |
| 1789178400 | test1 | 1.130850 no | 1.175432 no | 1.128885 no | 1.121602 no | 1.092419 no | 1.075013 no | 1.070319 no |
| 1789178700 | test1 | 0.994764 no | 1.019624 no | 0.956603 no | 0.961380 no | 0.949164 no | 0.929341 no | 0.914509 no |
| 1789179000 | test1 | 0.717849 no | 0.678618 no | 0.651877 no | 0.640162 no | 0.637018 no | 0.628495 no | 0.698485 no |
| 1789179300 | test1 | 0.567352 no | 0.535029 no | 0.506884 no | 0.494961 no | 0.486857 no | 0.476454 no | 0.468973 no |
| 1789179600 | test1 | 0.232468 no | 0.262374 no | 0.354205 no | 0.347880 no | 0.342884 no | 0.553930 no | 0.561338 no |
| 1789179900 | test1 | 0.900468 no | 0.838603 no | 0.815728 no | 0.809454 no | 0.822520 no | 0.959736 no | 0.974031 no |
| 1789180200 | test1 | 1.041579 no | 0.977787 no | 0.919444 no | 0.898227 no | 0.873672 no | 0.914813 no | 0.917659 no |
| 1789180500 | test1 | 1.469560 no | 1.362147 no | 1.328829 no | 1.336713 no | 1.341255 no | 1.341147 no | 1.334015 no |
| 1789180800 | test1 | 2.097723 no | 1.956705 no | 1.864163 no | 1.849216 no | 1.802195 no | 1.754332 no | 1.724573 no |
| 1789181100 | test1 | 2.310290 yes | 2.158155 yes | 2.028699 no | 1.969346 no | 1.931212 no | 1.922010 no | 1.892631 no |
| 1789181400 | test1 | 1.869408 no | 2.343140 yes | 2.236731 yes | 2.181941 yes | 2.123226 no | 2.069306 no | 2.034928 no |
| 1789181700 | test1 | 1.880392 no | 1.795140 no | 1.683241 no | 1.635294 no | 1.693440 no | 1.648352 no | 1.994151 no |
| 1789182000 | test1 | 2.341919 yes | 2.181232 yes | 2.041757 no | 2.044706 no | 2.002500 no | 2.002080 no | 1.976676 no |
| 1789182300 | test1 | 1.257637 no | 1.434077 no | 2.665544 yes | 2.664374 yes | 2.589456 yes | 2.520672 yes | 2.478256 yes |
| 1789182600 | test1 | 3.087213 yes | 2.867681 yes | 2.701318 yes | 2.628826 yes | 2.573136 yes | 2.504620 yes | 2.461953 yes |
| 1789182900 | test1 | 2.038047 no | 1.897757 no | 1.794903 no | 1.741693 no | 1.693026 no | 1.649492 no | 1.621848 no |
| 1789183200 | test1 | 1.975506 no | 1.899122 no | 1.783928 no | 1.756559 no | 1.708427 no | 1.666694 no | 1.638581 no |
| 1789183500 | test1 | 1.242117 no | 1.243824 no | 1.166128 no | 1.192810 no | 1.690438 no | 1.663443 no | 1.639662 no |
| 1789183800 | test1 | 1.734586 no | 1.610574 no | 1.520514 no | 1.481406 no | 1.439779 no | 1.401491 no | 1.377632 no |
| 1789184100 | test1 | 0.595659 no | 0.559110 no | 0.539475 no | 0.533659 no | 0.518962 no | 0.519885 no | 0.539634 no |
| 1789185000 | test1 | 0.614000 no | 0.577685 no | 0.563274 no | 0.561486 no | 0.549527 no | 0.545069 no | 0.687155 no |
| 1789185300 | test1 | 0.650561 no | 0.638883 no | 0.608469 no | 0.593587 no | 0.585082 no | 0.572953 no | 0.571215 no |
| 1789185600 | test1 | 0.401083 no | 0.537457 no | 0.757296 no | 0.743210 no | 0.724811 no | 0.717815 no | 0.706047 no |
| 1789185900 | test1 | 1.068824 no | 0.994468 no | 0.970872 no | 0.943895 no | 0.921570 no | 0.917085 no | 0.906634 no |
| 1789186200 | test1 | 0.816848 no | 0.758976 no | 0.720798 no | 0.748505 no | 0.742095 no | 0.727966 no | 0.716658 no |
| 1789186500 | test1 | 0.473161 no | 1.113861 no | 1.084440 no | 1.075237 no | 1.079922 no | 1.053328 no | 1.071351 no |
| 1789186800 | test1 | 1.711947 no | 1.587738 no | 1.529748 no | 1.484522 no | 1.442992 no | 1.407332 no | 1.383639 no |
| 1789187700 | test1 | 0.645449 no | 0.603762 no | 0.716756 no | 0.696121 no | 0.677032 no | 0.659697 no | 0.649721 no |
| 1789188000 | test1 | 0.649734 no | 0.783990 no | 1.713311 no | 1.699332 no | 1.912197 no | 2.317327 yes | 2.294624 yes |
| 1789188300 | test1 | 2.867610 yes | 2.695573 yes | 2.528685 yes | 2.480457 yes | 2.433812 yes | 2.379933 yes | 2.340109 yes |
| 1789188600 | test1 | 0.889097 no | 0.829522 no | 0.796330 no | 0.775771 no | 0.777193 no | 0.757828 no | 0.745430 no |
| 1789188900 | test1 | 0.672243 no | 0.635935 no | 0.598501 no | 0.582906 no | 0.569603 no | 0.554894 no | 0.555815 no |
| 1789189200 | test1 | 0.611369 no | 0.714200 no | 0.762639 no | 0.831318 no | 0.837059 no | 0.834251 no | 0.835762 no |
| 1789189500 | test1 | 1.142371 no | 1.102250 no | 1.032814 no | 1.002872 no | 0.984618 no | 1.057701 no | 1.043746 no |
| 1789189800 | test1 | 1.008073 no | 1.759831 no | 1.947394 no | 1.911043 no | 1.863707 no | 1.966437 no | 1.967008 no |
| 1789190100 | test1 | 2.372340 yes | 2.532105 yes | 2.380670 yes | 2.311136 yes | 2.246188 yes | 2.186880 yes | 2.150156 yes |
| 1789190400 | test1 | 1.492341 no | 1.429081 no | 2.126806 no | 2.088168 no | 2.060215 no | 2.022853 no | 2.010217 no |
| 1789190700 | test1 | 2.323666 yes | 2.401309 yes | 2.400016 yes | 2.332582 yes | 2.386043 yes | 2.361046 yes | 2.326739 yes |
| 1789191000 | test1 | 2.617036 yes | 2.443113 yes | 2.294755 yes | 2.241471 yes | 2.178742 yes | 2.123939 no | 2.120872 no |
| 1789191300 | test1 | 1.755373 no | 1.955849 no | 1.833670 no | 1.785660 no | 1.736386 no | 1.691058 no | 1.662905 no |
| 1789191600 | test1 | 1.469930 no | 1.394352 no | 1.393037 no | 1.351508 no | 1.317474 no | 1.282676 no | 1.260922 no |
| 1789191900 | test1 | 0.972702 no | 0.901820 no | 0.844564 no | 0.819609 no | 0.797083 no | 0.775955 no | 0.763810 no |
| 1789192200 | test1 | 0.149911 no | 0.224943 no | 0.242543 no | 0.428939 no | 0.466611 no | 0.468619 no | 0.472476 no |
| 1789192500 | test1 | 0.915682 no | 1.089698 no | 1.401660 no | 1.479503 no | 1.440450 no | 1.415079 no | 1.394668 no |
| 1789192800 | test1 | 1.698533 no | 1.631737 no | 1.532650 no | 1.489385 no | 1.448593 no | 1.413882 no | 1.391413 no |
| 1789193100 | test1 | 0.596975 no | 0.565658 no | 0.671303 no | 0.656107 no | 0.689449 no | 0.697851 no | 0.725070 no |
| 1789193400 | test1 | 1.127973 no | 1.222899 no | 1.146250 no | 1.113590 no | 1.083249 no | 1.062796 no | 1.044708 no |
| 1789193700 | test1 | 1.127319 no | 1.106264 no | 1.052014 no | 1.026686 no | 0.998550 no | 0.977267 no | 0.960925 no |
| 1789194000 | test1 | 0.546955 no | 0.545701 no | 0.523384 no | 0.521517 no | 0.516389 no | 0.513254 no | 0.510300 no |
| 1789194900 | test1 | 1.497166 no | 1.388775 no | 1.317340 no | 1.280825 no | 1.245498 no | 1.212626 no | 1.192059 no |
| 1789195200 | test1 | 0.804552 no | 0.759208 no | 1.015239 no | 0.989846 no | 0.965730 no | 0.943569 no | 0.928523 no |
| 1789195500 | test1 | 0.951233 no | 0.891309 no | 1.106665 no | 1.078198 no | 1.355126 no | 1.330666 no | 1.310146 no |
| 1789195800 | test1 | 1.487795 no | 1.385876 no | 1.354973 no | 1.322450 no | 1.290120 no | 1.257652 no | 1.238852 no |
| 1789196100 | test1 | 0.755978 no | 0.744297 no | 0.706038 no | 0.685417 no | 0.672501 no | 0.655225 no | 0.645537 no |
| 1789196400 | test1 | 0.433107 no | 0.495282 no | 0.505821 no | 0.492622 no | 0.489340 no | 0.513245 no | 0.517824 no |
| 1789197000 | test1 | 0.641868 no | 0.618596 no | 0.582846 no | 0.565472 no | 0.551330 no | 0.541962 no | 0.536196 no |
| 1789197300 | test1 | 0.309908 no | 0.511594 no | 0.499979 no | 0.501290 no | 0.487435 no | 0.474894 no | 0.470874 no |
| 1789197600 | test1 | 0.543931 no | 1.036111 no | 0.988143 no | 0.960801 no | 0.934604 no | 0.920158 no | 0.908573 no |
| 1789197900 | test1 | 1.039905 no | 1.049913 no | 0.982691 no | 0.954005 no | 0.927949 no | 0.904626 no | 0.889574 no |
| 1789198200 | test1 | 0.482181 no | 0.473326 no | 0.603819 no | 0.587606 no | 0.571936 no | 0.557563 no | 0.549391 no |
| 1789198500 | test1 | 0.538593 no | 0.500578 no | 0.583700 no | 0.567566 no | 0.553361 no | 0.539095 no | 0.531272 no |
| 1789198800 | test1 | 0.489812 no | 0.459229 no | 0.431670 no | 0.421222 no | 0.417979 no | 0.407764 no | 0.401795 no |
| 1789199100 | test1 | 0.814608 no | 0.905240 no | 0.850426 no | 0.825473 no | 0.804680 no | 0.785714 no | 0.773793 no |
| 1789199400 | test1 | 0.952753 no | 0.890535 no | 0.853622 no | 0.831958 no | 0.966654 no | 0.943727 no | 0.955332 no |
| 1789199700 | test1 | 0.789983 no | 0.737900 no | 0.815769 no | 0.813905 no | 0.908607 no | 0.991953 no | 1.620313 no |
| 1789200300 | test1 | 1.476606 no | 1.368201 no | 1.281239 no | 1.283465 no | 1.248005 no | 1.219010 no | 1.199207 no |
| 1789200600 | test1 | 1.749430 no | 1.631416 no | 1.610749 no | 1.923507 no | 1.979909 no | 2.016457 no | 2.068675 no |
| 1789200900 | test1 | 2.445828 yes | 2.656982 yes | 2.520691 yes | 2.463555 yes | 2.395965 yes | 2.335504 yes | 2.295615 yes |
| 1789201200 | test1 | 1.648085 no | 1.534033 no | 1.436105 no | 1.393861 no | 1.405882 no | 1.373955 no | 1.415216 no |
| 1789201500 | test1 | 1.157933 no | 1.098366 no | 1.036268 no | 1.005355 no | 0.978977 no | 0.955940 no | 0.939745 no |
| 1789201800 | test1 | 0.487524 no | 0.464799 no | 0.438954 no | 0.427788 no | 0.417264 no | 0.408836 no | 0.402088 no |
| 1789202100 | test1 | 0.328902 no | 0.412843 no | 0.727290 no | 0.743369 no | 0.729844 no | 0.716167 no | 0.708677 no |
| 1789202400 | test1 | 0.853492 no | 0.800925 no | 0.752573 no | 0.730137 no | 0.710391 no | 0.691974 no | 0.680365 no |
| 1789202700 | test1 | 0.238666 no | 0.233497 no | 0.226367 no | 0.222593 no | 0.243256 no | 0.259358 no | 0.259472 no |
| 1789203000 | test1 | 0.317366 no | 0.324967 no | 0.335082 no | 0.337791 no | 0.353250 no | 0.382409 no | 0.569210 no |
| 1789203300 | test1 | 0.784235 no | 0.993619 no | 0.989164 no | 0.960763 no | 1.009120 no | 0.983695 no | 0.967524 no |
| 1789203600 | test1 | 0.999715 no | 1.108599 no | 1.057322 no | 1.029472 no | 1.007045 no | 0.983198 no | 0.967520 no |
| 1789203900 | test1 | 0.827478 no | 0.832525 no | 0.859825 no | 0.836461 no | 0.837367 no | 0.817627 no | 0.807787 no |
| 1789204200 | test1 | 0.750564 no | 1.150579 no | 1.084088 no | 1.106398 no | 1.088564 no | 1.131323 no | 1.130546 no |
| 1789204500 | test1 | 1.254345 no | 1.196232 no | 1.461249 no | 1.433038 no | 1.395991 no | 1.368476 no | 1.346183 no |
| 1789204800 | test1 | 1.190777 no | 1.108262 no | 1.042174 no | 1.021584 no | 1.011915 no | 1.536361 no | 1.511423 no |
| 1789205100 | test1 | 1.614457 no | 1.499386 no | 1.406274 no | 1.379839 no | 1.636070 no | 1.602212 no | 1.575970 no |
| 1789205400 | test1 | 1.649980 no | 1.533917 no | 1.436286 no | 1.436126 no | 1.396443 no | 1.365783 no | 1.358931 no |
| 1789205700 | test1 | 0.716151 no | 0.690476 no | 0.655309 no | 1.553148 no | 1.520778 no | 1.480897 no | 1.457875 no |
| 1789206000 | test1 | 1.786494 no | 1.657109 no | 1.552615 no | 1.527388 no | 1.927861 no | 1.904434 no | 1.871992 no |
| 1789206300 | test1 | 1.632565 no | 1.545737 no | 1.449778 no | 1.410307 no | 1.380644 no | 1.346051 no | 1.325885 no |
| 1789206900 | test1 | 1.537982 no | 1.441005 no | 1.351705 no | 1.314089 no | 1.292481 no | 1.265424 no | 1.248086 no |
| 1789207200 | test1 | 0.545832 no | 0.584338 no | 0.692342 no | 0.687171 no | 0.671377 no | 0.656366 no | 0.673928 no |
| 1789207500 | test1 | 0.774765 no | 0.727328 no | 0.701034 no | 0.696086 no | 0.678204 no | 0.663072 no | 0.653535 no |
| 1789207800 | test1 | 0.460168 no | 0.438247 no | 0.411498 no | 0.400185 no | 0.391238 no | 0.381496 no | 0.375021 no |
| 1789208100 | test1 | 0.180248 no | 0.167296 no | 0.323122 no | 0.340702 no | 0.334203 no | 0.328456 no | 0.328305 no |
| 1789208400 | test1 | 0.390418 no | 0.567070 no | 0.548516 no | 0.533003 no | 0.519229 no | 0.506315 no | 0.498196 no |
| 1789208700 | test1 | 0.513381 no | 0.482705 no | 0.463682 no | 0.454143 no | 0.443576 no | 0.433613 no | 0.427369 no |
| 1789209000 | test1 | 0.222048 no | 0.426592 no | 0.410360 no | 0.400180 no | 0.393147 no | 0.389686 no | 0.384257 no |
| 1789209300 | test1 | 0.447166 no | 0.418188 no | 0.393097 no | 0.382985 no | 0.372251 no | 0.403148 no | 0.396271 no |
| 1789209600 | test1 | 0.417259 no | 0.566769 no | 0.604253 no | 0.586337 no | 0.570219 no | 0.555570 no | 0.546282 no |
| 1789209900 | test1 | 0.627006 no | 0.589952 no | 0.598482 no | 1.037812 no | 1.008619 no | 0.981791 no | 0.965773 no |
| 1789210200 | test1 | 1.069856 no | 0.993352 no | 0.965916 no | 0.950600 no | 0.936274 no | 0.947210 no | 0.936204 no |
| 1789210500 | test1 | 1.434221 no | 1.390763 no | 1.302870 no | 1.265319 no | 1.230521 no | 1.197980 no | 1.177927 no |
| 1789210800 | test1 | 1.399787 no | 1.336649 no | 1.557267 no | 1.511182 no | 1.468893 no | 1.434456 no | 1.412795 no |
| 1789211100 | test1 | 1.265158 no | 1.172392 no | 1.117942 no | 1.125709 no | 1.099665 no | 1.071142 no | 1.053207 no |
| 1789211400 | test1 | 0.522753 no | 0.586217 no | 0.554941 no | 0.538948 no | 0.528072 no | 0.572645 no | 0.562975 no |
| 1789211700 | test1 | 0.509338 no | 0.475974 no | 0.847902 no | 0.871763 no | 0.847464 no | 0.825418 no | 0.812105 no |
| 1789212000 | test1 | 0.913507 no | 0.937949 no | 0.957691 no | 0.931779 no | 0.935769 no | 0.911052 no | 0.895851 no |
| 1789212300 | test1 | 0.810148 no | 0.753632 no | 0.707415 no | 0.686324 no | 0.672657 no | 0.659768 no | 0.652042 no |
| 1789212600 | test1 | 0.479190 no | 0.448791 no | 0.586136 no | 0.570281 no | 0.612321 no | 0.599589 no | 0.595825 no |
| 1789212900 | test1 | 0.656374 no | 0.812072 no | 0.762473 no | 0.739815 no | 0.718994 no | 0.701497 no | 0.689519 no |
| 1789213200 | test1 | 0.660084 no | 0.615014 no | 0.587059 no | 0.578171 no | 0.609397 no | 0.610148 no | 0.606261 no |
| 1789213500 | test1 | 0.512587 no | 0.493283 no | 0.481680 no | 0.470493 no | 0.460777 no | 0.449581 no | 0.442520 no |
| 1789214100 | test1 | 0.541583 no | 0.509020 no | 0.483966 no | 0.474764 no | 0.462106 no | 0.451240 no | 0.448868 no |
| 1789214400 | test1 | 0.248219 no | 0.241088 no | 0.327847 no | 0.345080 no | 0.363078 no | 0.362342 no | 0.375772 no |
| 1789214700 | test1 | 0.660307 no | 0.650312 no | 0.626270 no | 0.625832 no | 0.614337 no | 0.607135 no | 0.598114 no |
| 1789215000 | test1 | 1.168220 no | 1.175716 no | 1.138722 no | 1.105899 no | 1.076030 no | 1.089489 no | 1.072162 no |
| 1789215300 | test1 | 1.248749 no | 1.571840 no | 1.470884 no | 1.483360 no | 1.442086 no | 1.404475 no | 1.380997 no |
| 1789215600 | test1 | 1.279945 no | 1.198387 no | 1.141363 no | 1.111090 no | 1.086858 no | 1.060781 no | 1.045338 no |
| 1789215900 | test1 | 0.632599 no | 0.594756 no | 0.611631 no | 0.617396 no | 0.850130 no | 0.877708 no | 0.863064 no |
| 1789216200 | test1 | 1.030836 no | 0.961179 no | 0.908003 no | 0.882247 no | 0.860802 no | 0.843946 no | 0.838981 no |
| 1789216500 | test1 | 0.403480 no | 0.387655 no | 0.382356 no | 0.379649 no | 0.407432 no | 0.406867 no | 0.404443 no |
| 1789216800 | test1 | 0.426115 no | 0.407091 no | 0.399112 no | 0.389595 no | 0.411591 no | 0.723054 no | 0.773561 no |
| 1789217100 | test1 | 0.915772 no | 0.853581 no | 0.880436 no | 0.862136 no | 0.852124 no | 0.889764 no | 0.877235 no |
| 1789217400 | test1 | 0.718321 no | 0.854590 no | 0.800109 no | 0.863746 no | 0.853229 no | 0.847586 no | 0.845620 no |
| 1789217700 | test1 | 0.902308 no | 0.841796 no | 0.962679 no | 0.938742 no | 0.951070 no | 1.343014 no | 1.424200 no |
| 1789218000 | test1 | 1.622536 no | 1.517315 no | 1.797434 no | 1.744826 no | 1.737808 no | 1.691660 no | 1.663785 no |
| 1789218300 | test1 | 1.398332 no | 1.328112 no | 1.459547 no | 1.463245 no | 1.518383 no | 1.543364 no | 1.517756 no |
| 1789218600 | test1 | 1.459043 no | 1.409800 no | 1.329559 no | 1.695847 no | 1.770757 no | 1.925465 no | 2.009614 no |
| 1789218900 | test1 | 2.190110 yes | 2.035715 no | 1.966469 no | 1.911401 no | 1.868051 no | 2.099339 no | 2.076097 no |
| 1789219200 | test1 | 1.635208 no | 1.614698 no | 1.562150 no | 1.525022 no | 1.507422 no | 1.468769 no | 1.455019 no |
| 1789219500 | test1 | 1.562556 no | 2.097985 no | 1.995611 no | 1.983261 no | 1.931699 no | 2.230877 yes | 2.193946 yes |
| 1789219800 | test1 | 2.619436 yes | 2.440678 yes | 2.364151 yes | 2.586585 yes | 2.522616 yes | 2.461176 yes | 2.422651 yes |
| 1789220100 | test1 | 1.748424 no | 1.630587 no | 1.534089 no | 1.492711 no | 1.451638 no | 1.421030 no | 1.404256 no |
| 1789220400 | test1 | 0.667465 no | 0.618628 no | 0.581498 no | 0.625611 no | 1.262372 no | 1.600664 no | 1.575254 no |
| 1789220700 | test1 | 1.963911 no | 1.850394 no | 1.731074 no | 1.679568 no | 1.650106 no | 1.606242 no | 1.583697 no |
| 1789221300 | test1 | 1.463327 no | 1.442800 no | 1.455010 no | 1.413159 no | 1.409478 no | 1.423947 no | 1.412739 no |
| 1789221600 | test1 | 1.102430 no | 1.020891 no | 0.956075 no | 0.929167 no | 0.905394 no | 0.882512 no | 0.868026 no |
| 1789221900 | test1 | 0.283067 no | 0.413534 no | 0.387641 no | 0.376871 no | 0.366291 no | 0.357652 no | 0.351547 no |
| 1789222200 | test1 | 0.486515 no | 0.631163 no | 0.601520 no | 0.584696 no | 0.569860 no | 0.555105 no | 0.545850 no |
| 1789222500 | test1 | 0.605781 no | 0.613636 no | 0.587621 no | 0.587389 no | 0.581205 no | 0.584192 no | 0.585288 no |
| 1789222800 | test1 | 0.761488 no | 0.810690 no | 1.070287 no | 1.038337 no | 1.009089 no | 1.082405 no | 1.065100 no |
| 1789223700 | test1 | 1.363035 no | 1.263138 no | 1.255155 no | 1.288346 no | 1.252131 no | 1.218931 no | 1.199758 no |
| 1789224000 | test1 | 0.778318 no | 0.734650 no | 0.712019 no | 0.691188 no | 0.671868 no | 0.654266 no | 0.974686 no |
| 1789224300 | test1 | 1.066362 no | 0.997885 no | 1.010836 no | 0.987011 no | 0.959969 no | 0.934768 no | 0.926117 no |
| 1789224600 | test1 | 0.676342 no | 0.684674 no | 0.705552 no | 0.932797 no | 0.947727 no | 0.981398 no | 0.964680 no |
| 1789224900 | test1 | 1.081243 no | 1.027539 no | 1.038277 no | 1.052524 no | 1.032561 no | 1.017330 no | 1.007125 no |
| 1789225200 | test1 | 0.736624 no | 0.690389 no | 0.650976 no | 0.632021 no | 0.615474 no | 0.613926 no | 0.603808 no |
| 1789225500 | test1 | 0.580953 no | 0.568517 no | 0.544579 no | 0.535560 no | 0.685092 no | 0.683392 no | 0.680614 no |
| 1789225800 | test1 | 0.755284 no | 0.794874 no | 0.800230 no | 0.791932 no | 0.802763 no | 1.227645 no | 1.211860 no |
| 1789226100 | test1 | 1.427447 no | 1.626279 no | 1.541182 no | 1.502819 no | 1.462546 no | 1.455154 no | 1.435290 no |
| 1789226400 | test1 | 1.714846 no | 1.610137 no | 1.516687 no | 1.472204 no | 1.431424 no | 1.393990 no | 1.370368 no |
| 1789226700 | test1 | 0.794598 no | 1.513874 no | 1.439087 no | 1.399305 no | 1.370846 no | 1.358361 no | 1.364577 no |
| 1789227000 | test1 | 1.590225 no | 1.472709 no | 1.377714 no | 2.198849 yes | 2.137118 no | 2.081627 no | 2.047991 no |
| 1789227300 | test1 | 2.095132 no | 1.941946 no | 2.327709 yes | 2.264758 yes | 2.212251 yes | 2.394608 yes | 2.372076 yes |
| 1789227600 | test1 | 2.247228 yes | 2.088546 no | 2.005463 no | 1.952522 no | 1.897902 no | 1.847370 no | 1.815803 no |
| 1789227900 | test1 | 0.765013 no | 0.753997 no | 1.541356 no | 1.495904 no | 1.455201 no | 1.416401 no | 1.392194 no |
| 1789228200 | test1 | 1.636694 no | 1.516251 no | 1.420181 no | 1.378404 no | 1.339760 no | 1.362098 no | 1.348760 no |
| 1789228500 | test1 | 0.582685 no | 1.969432 no | 2.090851 no | 2.034603 no | 2.002331 no | 2.095904 no | 2.060112 no |
| 1789228800 | test1 | 2.576756 yes | 2.408398 yes | 2.271897 yes | 2.211938 yes | 2.156487 no | 2.099761 no | 2.065260 no |
| 1789229100 | test1 | 2.031538 no | 1.883507 no | 1.991555 no | 1.936074 no | 1.920747 no | 1.882733 no | 1.874424 no |
| 1789229400 | test1 | 2.327338 yes | 2.192039 yes | 2.050576 no | 1.989411 no | 1.933991 no | 1.882636 no | 1.850494 no |
| 1789229700 | test1 | 0.464968 no | 0.525376 no | 0.547668 no | 0.547903 no | 0.548864 no | 0.538122 no | 0.530632 no |
| 1789230000 | test1 | 0.609108 no | 0.674348 no | 0.643875 no | 0.676759 no | 0.677758 no | 0.670867 no | 0.676490 no |
| 1789230900 | test1 | 0.706777 no | 0.878839 no | 0.823162 no | 0.798663 no | 0.777800 no | 0.778669 no | 0.772260 no |
| 1789231200 | test1 | 0.921992 no | 0.854048 no | 0.893046 no | 0.866535 no | 0.842380 no | 0.819965 no | 0.815448 no |
| 1789231500 | test1 | 0.768455 no | 0.715811 no | 0.675878 no | 0.655725 no | 0.640954 no | 0.737939 no | 0.890994 no |
| 1789231800 | test1 | 0.871729 no | 0.807174 no | 0.855253 no | 0.830145 no | 0.806834 no | 0.785331 no | 0.773051 no |
| 1789232100 | test1 | 0.469458 no | 0.548019 no | 1.087779 no | 1.243489 no | 1.277926 no | 1.479988 no | 1.473670 no |
| 1789232400 | test1 | 1.946569 no | 1.805793 no | 1.713858 no | 1.662785 no | 1.653285 no | 2.074420 no | 2.041721 no |
| 1789232700 | test1 | 1.840650 no | 1.837537 no | 1.719272 no | 1.674436 no | 1.627810 no | 1.584882 no | 1.558126 no |
| 1789233000 | test1 | 0.776891 no | 1.851464 no | 1.733152 no | 1.683690 no | 1.636286 no | 1.600499 no | 1.574922 no |
| 1789233300 | test1 | 1.869545 no | 1.756091 no | 1.930405 no | 1.882020 no | 1.829083 no | 1.782999 no | 1.752523 no |
| 1789233600 | test1 | 1.250523 no | 1.260795 no | 1.180144 no | 1.149105 no | 1.117089 no | 1.276695 no | 1.274679 no |
| 1789233900 | test1 | 1.082519 no | 1.002854 no | 0.938411 no | 0.910681 no | 0.885050 no | 0.861650 no | 0.847024 no |
| 1789234200 | test1 | 0.113740 no | 0.108067 no | 0.779943 no | 0.757603 no | 0.736568 no | 0.804113 no | 0.790747 no |
| 1789234500 | test1 | 1.007368 no | 1.116226 no | 1.061363 no | 1.034645 no | 1.145613 no | 1.116883 no | 1.132643 no |
| 1789234800 | test1 | 1.104629 no | 1.049216 no | 1.014478 no | 0.984876 no | 0.957277 no | 0.932414 no | 0.918101 no |
| 1789235100 | test1 | 0.555395 no | 0.514646 no | 0.956155 no | 0.929957 no | 1.013564 no | 0.991732 no | 0.985148 no |
| 1789235400 | test1 | 1.145567 no | 1.061842 no | 1.149300 no | 1.145921 no | 1.114119 no | 1.086973 no | 1.106597 no |
| 1789235700 | test1 | 0.925523 no | 0.917369 no | 0.891415 no | 0.865877 no | 0.841634 no | 0.819486 no | 0.811622 no |
| 1789236000 | test1 | 0.715917 no | 0.676191 no | 0.635645 no | 0.617046 no | 0.600027 no | 0.585701 no | 0.601383 no |
| 1789236300 | test1 | 0.702072 no | 1.181671 no | 1.173413 no | 1.142710 no | 1.113414 no | 1.084991 no | 1.074961 no |
| 1789236600 | test1 | 1.693281 no | 1.754566 no | 1.644939 no | 1.602176 no | 1.598043 no | 1.586278 no | 1.561449 no |
| 1789236900 | test1 | 1.562005 no | 1.509369 no | 2.489638 yes | 2.420746 yes | 2.355544 yes | 2.299057 yes | 2.259889 yes |
| 1789237200 | test1 | 2.506510 yes | 2.321979 yes | 2.172906 no | 2.108223 no | 2.323818 yes | 2.329441 yes | 2.324076 yes |
| 1789238100 | test1 | 1.546154 no | 1.530811 no | 1.908848 no | 1.894356 no | 1.841954 no | 1.793645 no | 1.763512 no |
| 1789238400 | test1 | 1.677712 no | 1.591117 no | 1.495926 no | 1.470732 no | 1.446183 no | 1.412132 no | 1.388869 no |
| 1789238700 | test1 | 0.708071 no | 0.660958 no | 0.619995 no | 0.607588 no | 0.592190 no | 0.578800 no | 0.647364 no |
| 1789239000 | test1 | 0.502693 no | 0.465990 no | 0.447560 no | 0.799181 no | 0.779080 no | 0.787542 no | 0.778520 no |
| 1789239300 | test1 | 0.870459 no | 0.846907 no | 0.819650 no | 0.807469 no | 0.837068 no | 0.921438 no | 0.940379 no |
| 1789239600 | test1 | 0.974169 no | 0.924953 no | 0.880692 no | 0.859513 no | 0.967218 no | 0.947331 no | 0.948233 no |
| 1789239900 | test1 | 0.882004 no | 0.836794 no | 0.828336 no | 1.408952 no | 1.370220 no | 1.335183 no | 1.312703 no |
| 1789240200 | test1 | 1.481903 no | 1.458446 no | 1.503481 no | 1.485028 no | 1.638880 no | 1.917672 no | 1.888397 no |
| 1789240500 | test1 | 1.991250 no | 1.851875 no | 1.735212 no | 1.683921 no | 1.642531 no | 1.600787 no | 1.575702 no |
| 1789240800 | test1 | 0.913202 no | 0.905562 no | 0.940434 no | 0.923917 no | 0.923081 no | 0.899957 no | 0.890413 no |
| 1789241100 | test1 | 1.129569 no | 1.144447 no | 1.816690 no | 1.808877 no | 1.786687 no | 1.792133 no | 1.890084 no |
| 1789241400 | test1 | 2.204550 yes | 2.044706 no | 1.928848 no | 2.354759 yes | 2.376978 yes | 2.323791 yes | 2.285060 yes |
| 1789241700 | test1 | 1.944040 no | 1.822235 no | 1.829101 no | 1.779378 no | 1.832417 no | 1.784577 no | 1.760207 no |
| 1789242000 | test1 | 1.783227 no | 1.703088 no | 1.602440 no | 1.556286 no | 1.516709 no | 1.516386 no | 1.492160 no |
| 1789242300 | test1 | 1.588576 no | 1.590285 no | 1.533860 no | 1.493231 no | 1.475285 no | 1.459492 no | 1.440492 no |
| 1789242600 | test1 | 0.961163 no | 0.896222 no | 0.859104 no | 0.839432 no | 0.821087 no | 0.800359 no | 0.787883 no |
| 1789242900 | test1 | 0.800991 no | 0.954545 no | 1.000957 no | 1.020916 no | 1.059400 no | 1.105425 no | 1.087343 no |
| 1789243200 | test1 | 1.429706 no | 1.392901 no | 1.376145 no | 1.406701 no | 1.368132 no | 1.336413 no | 1.315412 no |
| 1789243500 | test1 | 1.098535 no | 1.030420 no | 0.968701 no | 0.940223 no | 0.924556 no | 0.944956 no | 0.942895 no |
| 1789243800 | test1 | 0.677687 no | 0.640809 no | 0.617015 no | 0.621418 no | 0.604615 no | 0.588810 no | 0.579562 no |
| 1789244100 | test1 | 0.440130 no | 0.446005 no | 0.670522 no | 0.664153 no | 0.648424 no | 0.638645 no | 0.629517 no |
| 1789244400 | test1 | 0.717309 no | 0.688370 no | 0.652034 no | 0.690180 no | 0.721893 no | 0.713316 no | 0.704992 no |
| 1789245300 | test1 | 0.896239 no | 0.881616 no | 0.911608 no | 0.931702 no | 0.915902 no | 0.904537 no | 0.889289 no |
| 1789245600 | test1 | 0.713733 no | 0.661781 no | 1.209113 no | 1.187154 no | 1.221001 no | 1.280312 no | 1.343608 no |
| 1789245900 | test1 | 1.611111 no | 1.497112 no | 1.407857 no | 1.420441 no | 1.450065 no | 1.429092 no | 1.409594 no |
| 1789246200 | test1 | 0.952358 no | 0.953448 no | 2.078405 no | 2.017803 no | 1.974534 no | 1.922094 no | 1.889621 no |
| 1789246500 | test1 | 2.239020 yes | 2.074356 no | 1.940981 no | 1.883597 no | 1.830930 no | 1.797668 no | 1.766962 no |
| 1789246800 | test1 | 0.447471 no | 1.365095 no | 1.282900 no | 1.249581 no | 1.215500 no | 1.183331 no | 1.163827 no |
| 1789247100 | test1 | 1.437487 no | 1.338686 no | 1.308098 no | 1.292259 no | 1.259318 no | 1.237899 no | 1.219274 no |
| 1789247400 | test1 | 0.621071 no | 0.625997 no | 1.704583 no | 1.713917 no | 1.712046 no | 1.749165 no | 1.721015 no |
| 1789247700 | test1 | 2.122198 no | 1.965537 no | 1.841316 no | 1.786823 no | 1.738118 no | 1.697200 no | 1.668554 no |
| 1789248000 | test1 | 0.294405 no | 0.273786 no | 0.256928 no | 0.367243 no | 0.357030 no | 0.349189 no | 0.343945 no |
| 1789248300 | test1 | 0.525554 no | 0.573304 no | 0.610125 no | 0.592136 no | 0.575618 no | 0.560566 no | 0.556242 no |
| 1789248600 | test1 | 0.641438 no | 0.615826 no | 0.589113 no | 0.577604 no | 0.580832 no | 0.568167 no | 0.559874 no |
| 1789248900 | test1 | 0.554463 no | 0.521628 no | 0.505855 no | 0.545798 no | 0.538551 no | 0.527680 no | 0.518953 no |
| 1789249200 | test1 | 0.578682 no | 0.682042 no | 0.652086 no | 0.687077 no | 0.668198 no | 0.943302 no | 0.928261 no |
| 1789249500 | test1 | 1.207254 no | 1.475146 no | 1.511261 no | 1.580587 no | 1.727676 no | 1.682193 no | 1.654372 no |
| 1789249800 | test1 | 2.303347 yes | 2.154335 yes | 2.094968 no | 2.064688 no | 2.040424 no | 1.996890 no | 1.985831 no |
| 1789250100 | test1 | 1.980759 no | 1.851717 no | 1.735594 no | 1.880556 no | 1.854230 no | 1.924506 no | 1.929601 no |
| 1789250400 | test1 | 1.819237 no | 1.739342 no | 2.150290 no | 2.086161 no | 2.027851 no | 1.973787 no | 1.948310 no |
| 1789250700 | test1 | 2.189945 yes | 2.094072 no | 1.963171 no | 1.905124 no | 2.186374 yes | 2.128367 no | 2.199211 yes |
| 1789251000 | test1 | 2.198198 yes | 2.070893 no | 1.937522 no | 1.926049 no | 1.881514 no | 1.834927 no | 1.804255 no |
| 1789251300 | test1 | 1.420425 no | 1.323391 no | 1.263991 no | 1.280720 no | 1.279446 no | 1.250733 no | 1.230535 no |
| 1789251600 | test1 | 0.795458 no | 0.786097 no | 0.774846 no | 1.122449 no | 1.098889 no | 1.073365 no | 1.056010 no |
| 1789252800 | test1 | 0.461859 no | 0.434859 no | 0.456192 no | 0.443062 no | 0.724163 no | 0.708242 no | 0.710647 no |
| 1789253100 | test1 | 0.794756 no | 0.827730 no | 0.807312 no | 0.784357 no | 0.762470 no | 0.746695 no | 0.735779 no |
| 1789253400 | test1 | 0.784630 no | 0.852756 no | 0.819042 no | 0.823119 no | 0.803449 no | 0.784293 no | 0.774480 no |
| 1789253700 | test1 | 0.848286 no | 0.791966 no | 0.746671 no | 0.727282 no | 0.855712 no | 0.838068 no | 0.827551 no |
| 1789254000 | test1 | 0.652064 no | 0.682348 no | 0.661811 no | 0.731628 no | 0.715177 no | 0.720897 no | 0.721520 no |
| 1789254300 | test1 | 0.664646 no | 0.790473 no | 0.760930 no | 0.775517 no | 0.755043 no | 0.741892 no | 0.729481 no |
| 1789254600 | test1 | 0.792062 no | 0.734076 no | 0.694436 no | 0.675151 no | 0.660405 no | 0.661371 no | 0.655165 no |
| 1789254900 | test1 | 0.541129 no | 0.601262 no | 0.673820 no | 0.660243 no | 0.646427 no | 0.630876 no | 0.624128 no |
| 1789255200 | test1 | 0.757185 no | 0.720988 no | 0.741337 no | 0.781729 no | 0.761066 no | 0.745317 no | 0.821928 no |
| 1789255500 | test1 | 0.918389 no | 0.867505 no | 0.813768 no | 0.789929 no | 0.771420 no | 0.753932 no | 0.741951 no |
| 1789255800 | test1 | 0.404901 no | 0.458377 no | 0.465208 no | 0.461622 no | 0.451580 no | 0.445849 no | 0.438407 no |
| 1789256100 | test1 | 0.399992 no | 0.483517 no | 0.456190 no | 0.466545 no | 0.455030 no | 0.585625 no | 0.622398 no |
| 1789256400 | test1 | 0.706104 no | 0.659807 no | 0.626383 no | 0.729239 no | 0.777207 no | 0.763761 no | 0.757152 no |
| 1789256700 | test1 | 0.681892 no | 0.698434 no | 0.656387 no | 0.637629 no | 0.620391 no | 0.680202 no | 0.668705 no |
| 1789257000 | test1 | 0.924339 no | 0.865002 no | 0.813486 no | 0.789571 no | 0.768965 no | 0.765833 no | 0.753011 no |
| 1789257300 | test1 | 0.909211 no | 0.855763 no | 0.825278 no | 0.802705 no | 0.781742 no | 0.763713 no | 0.751561 no |
| 1789257600 | test1 | 0.583003 no | 0.571267 no | 0.605830 no | 0.589729 no | 0.577034 no | 0.562849 no | 0.554597 no |
| 1789257900 | test1 | 0.472135 no | 0.444399 no | 0.421772 no | 0.421344 no | 0.411947 no | 0.405506 no | 0.399457 no |
| 1789258200 | test1 | 0.505062 no | 0.915592 no | 0.878933 no | 0.855321 no | 0.834853 no | 0.813100 no | 0.804363 no |
| 1789258500 | test1 | 1.022577 no | 0.959354 no | 0.897939 no | 0.872045 no | 0.847769 no | 0.825334 no | 0.811350 no |
| 1789258800 | test1 | 0.270939 no | 0.253039 no | 0.241165 no | 0.243033 no | 0.240698 no | 0.277568 no | 0.273669 no |
| 1789259100 | test1 | 0.235155 no | 0.289411 no | 0.342427 no | 0.338495 no | 0.417802 no | 0.412666 no | 0.405778 no |
| 1789259400 | test1 | 0.476661 no | 0.443017 no | 0.416170 no | 0.404165 no | 0.393565 no | 0.383348 no | 0.377164 no |
| 1789260000 | test1 | 0.963310 no | 0.965349 no | 1.131240 no | 1.098229 no | 1.068472 no | 1.077786 no | 1.063516 no |
| 1789260300 | test1 | 1.345043 no | 1.246373 no | 1.257413 no | 1.250081 no | 1.217824 no | 1.187911 no | 1.187138 no |
| 1789260600 | test1 | 0.946091 no | 0.877082 no | 0.837379 no | 1.264916 no | 1.229638 no | 1.197042 no | 1.176593 no |
| 1789260900 | test1 | 1.327342 no | 1.230126 no | 1.151038 no | 1.117757 no | 1.086715 no | 1.057858 no | 1.039776 no |
| 1789261200 | test1 | 0.113928 no | 0.266481 no | 0.551643 no | 0.536520 no | 0.530499 no | 0.516409 no | 0.509730 no |
| 1789261500 | test1 | 0.715369 no | 0.663361 no | 1.058538 no | 1.027311 no | 0.998578 no | 0.971987 no | 0.956554 no |
| 1789261800 | test1 | 1.073191 no | 1.078532 no | 1.059538 no | 1.501351 no | 1.533904 no | 1.727369 no | 1.845795 no |
| 1789262100 | test1 | 2.129519 yes | 1.986271 no | 1.860006 no | 1.804775 no | 1.759792 no | 1.726744 no | 1.697331 no |
| 1789262400 | test1 | 1.213146 no | 1.125935 no | 1.062731 no | 1.209416 no | 1.395694 no | 1.360816 no | 1.338128 no |
| 1789262700 | test1 | 1.246297 no | 1.183952 no | 1.354464 no | 1.849275 no | 1.813989 no | 1.835895 no | 1.839825 no |
| 1789263000 | test1 | 2.050587 no | 1.903674 no | 1.783999 no | 1.730802 no | 1.682684 no | 1.637888 no | 1.611045 no |
| 1789263300 | test1 | 0.421830 no | 0.425701 no | 0.484475 no | 0.486269 no | 0.487249 no | 0.481204 no | 0.479182 no |
| 1789263600 | test1 | 1.649034 no | 1.553408 no | 1.461985 no | 1.511287 no | 1.477688 no | 1.440172 no | 1.415857 no |
| 1789263900 | test1 | 0.821993 no | 0.769290 no | 0.791533 no | 0.770115 no | 0.749416 no | 0.730137 no | 0.717721 no |
| 1789264200 | test1 | 1.127821 no | 1.067723 no | 0.998944 no | 0.969177 no | 0.942061 no | 0.917491 no | 0.902169 no |
| 1789264500 | test1 | 0.275236 no | 0.356358 no | 0.556259 no | 0.599304 no | 0.712220 no | 0.693874 no | 0.682105 no |
| 1789264800 | test1 | 0.856447 no | 0.803579 no | 0.777289 no | 0.758399 no | 0.738229 no | 0.720288 no | 0.708493 no |
| 1789265100 | test1 | 0.612272 no | 0.812988 no | 0.777232 no | 0.762191 no | 0.740815 no | 0.770503 no | 0.761978 no |
| 1789265400 | test1 | 0.923387 no | 0.856587 no | 0.802704 no | 0.779175 no | 0.757648 no | 0.741407 no | 0.728910 no |
| 1789265700 | test1 | 0.252011 no | 0.249408 no | 0.274209 no | 0.266598 no | 0.279823 no | 0.272725 no | 0.269993 no |
| 1789266000 | test1 | 0.389800 no | 0.362313 no | 0.340376 no | 0.330883 no | 0.324132 no | 0.315850 no | 0.310542 no |
| 1789266300 | test1 | 1.410212 no | 1.327090 no | 1.243924 no | 1.207014 no | 1.173162 no | 1.141898 no | 1.122389 no |
| 1789266600 | test1 | 1.410964 no | 1.910676 no | 1.787870 no | 1.734843 no | 1.686144 no | 1.641228 no | 1.613192 no |
| 1789267200 | test1 | 1.603878 no | 1.537242 no | 1.438747 no | 1.507094 no | 1.528374 no | 1.529353 no | 1.871338 no |
| 1789267500 | test1 | 1.781516 no | 1.675772 no | 1.588913 no | 1.543965 no | 1.523703 no | 1.484566 no | 1.460059 no |
| 1789267800 | test1 | 0.584827 no | 0.545953 no | 0.513453 no | 1.151680 no | 1.122060 no | 1.234572 no | 1.214333 no |
| 1789268100 | test1 | 1.535237 no | 1.455802 no | 1.367812 no | 1.328444 no | 1.295712 no | 1.261561 no | 1.240194 no |
| 1789268400 | test1 | 0.709852 no | 0.712935 no | 0.725233 no | 0.721670 no | 0.707379 no | 0.689147 no | 1.408206 no |
| 1789268700 | test1 | 1.847999 no | 1.711727 no | 1.603624 no | 1.555800 no | 1.512408 no | 1.472204 no | 1.447321 no |
| 1789269000 | test1 | 0.785741 no | 0.789491 no | 0.749933 no | 0.806738 no | 0.785190 no | 0.963714 no | 0.947553 no |
| 1789269300 | test1 | 0.961097 no | 0.900138 no | 0.854395 no | 0.837387 no | 0.814822 no | 0.793135 no | 0.779585 no |
| 1789269600 | test1 | 0.307663 no | 0.286804 no | 0.274860 no | 0.268840 no | 0.264355 no | 0.265329 no | 0.260955 no |
| 1789269900 | test1 | 0.174555 no | 0.302230 no | 0.514458 no | 0.597625 no | 0.591601 no | 0.576422 no | 0.568410 no |
| 1789270200 | test1 | 0.872136 no | 0.808302 no | 0.896404 no | 0.875880 no | 0.852060 no | 0.877009 no | 0.862466 no |
| 1789270500 | test1 | 0.850644 no | 0.904747 no | 0.898053 no | 0.968670 no | 0.944669 no | 0.922949 no | 0.907697 no |
| 1789270800 | test1 | 0.805382 no | 0.746667 no | 0.709203 no | 0.689720 no | 0.670469 no | 0.652726 no | 0.641666 no |
| 1789271100 | test1 | 0.234945 no | 0.980164 no | 0.918967 no | 0.898306 no | 0.873494 no | 0.881250 no | 0.867941 no |
| 1789271400 | test1 | 1.116659 no | 1.052476 no | 0.985145 no | 1.135867 no | 1.104326 no | 1.074965 no | 1.057023 no |
| 1789271700 | test1 | 0.794007 no | 0.740129 no | 0.749691 no | 0.783217 no | 1.142690 no | 1.117329 no | 1.101857 no |
| 1789272000 | test1 | 1.186771 no | 1.109112 no | 1.043669 no | 1.014572 no | 0.989335 no | 0.967980 no | 0.951800 no |
| 1789272300 | test1 | 1.577166 no | 1.510484 no | 1.413831 no | 1.372783 no | 1.334375 no | 1.299103 no | 1.277377 no |
| 1789272600 | test1 | 1.621594 no | 1.519217 no | 1.438116 no | 1.396103 no | 2.021420 no | 1.969999 no | 1.945431 no |
| 1789272900 | test1 | 1.989665 no | 1.863606 no | 1.744307 no | 1.708242 no | 1.672258 no | 1.628350 no | 1.600739 no |
| 1789273200 | test1 | 0.766973 no | 0.808797 no | 0.761265 no | 0.746553 no | 0.742784 no | 0.726865 no | 0.744254 no |
| 1789273500 | test1 | 0.601191 no | 0.562742 no | 0.529904 no | 0.515008 no | 0.501684 no | 0.637701 no | 0.633201 no |
| 1789273800 | test1 | 0.596800 no | 0.574479 no | 0.548154 no | 0.581269 no | 0.591981 no | 0.577017 no | 0.569644 no |
| 1789274400 | test1 | 0.512856 no | 0.508665 no | 0.480597 no | 0.473613 no | 0.469696 no | 0.471759 no | 0.464313 no |
| 1789274700 | test1 | 0.379353 no | 0.351994 no | 0.330679 no | 0.322066 no | 0.316076 no | 0.310566 no | 0.310940 no |
| 1789275000 | test1 | 0.157128 no | 0.161978 no | 0.160734 no | 0.159139 no | 0.161940 no | 0.159688 no | 0.171135 no |
| 1789275300 | test1 | 0.175199 no | 0.250488 no | 0.344771 no | 0.335067 no | 0.844304 no | 0.826255 no | 0.965661 no |
| 1789275600 | test1 | 1.225762 no | 1.135974 no | 1.065727 no | 1.039471 no | 1.015043 no | 1.004786 no | 0.987670 no |
| 1789275900 | test1 | 0.382284 no | 0.360848 no | 0.340939 no | 0.331840 no | 0.513111 no | 0.499621 no | 0.491905 no |
| 1789276200 | test1 | 0.545990 no | 0.506690 no | 0.484023 no | 0.477576 no | 0.467399 no | 0.457083 no | 0.464557 no |
| 1789276500 | test1 | 0.287552 no | 0.304137 no | 0.384672 no | 0.375652 no | 0.367455 no | 0.364423 no | 0.366411 no |
| 1789276800 | test1 | 0.551323 no | 0.513161 no | 0.481301 no | 0.467056 no | 0.454229 no | 0.442573 no | 0.435259 no |
| 1789277100 | test1 | 0.430484 no | 0.407878 no | 0.385516 no | 0.374102 no | 0.368907 no | 0.386531 no | 0.402115 no |
| 1789277400 | test1 | 0.525178 no | 0.486675 no | 0.456021 no | 0.444149 no | 0.434037 no | 0.422772 no | 0.415637 no |
| 1789277700 | test1 | 0.436926 no | 0.405023 no | 0.390056 no | 0.378466 no | 0.368080 no | 0.358458 no | 0.352431 no |
| 1789278300 | test1 | 0.316495 no | 0.480068 no | 0.464232 no | 0.450990 no | 0.452675 no | 0.452181 no | 0.444460 no |
| 1789278600 | test1 | 0.490023 no | 0.464342 no | 0.439517 no | 0.430414 no | 0.420479 no | 0.414040 no | 0.408457 no |
| 1789278900 | test1 | 0.189526 no | 0.177102 no | 0.169537 no | 0.165148 no | 0.161864 no | 0.160324 no | 0.209079 no |
| 1789279200 | test1 | 0.243378 no | 0.233664 no | 0.237919 no | 0.231302 no | 0.225384 no | 0.220111 no | 0.220288 no |
| 1789279500 | test1 | 0.221339 no | 0.267077 no | 0.328788 no | 0.434398 no | 0.422295 no | 0.414103 no | 0.407193 no |
| 1789279800 | test1 | 0.486346 no | 0.500378 no | 0.623576 no | 0.639175 no | 0.681678 no | 0.679942 no | 0.697842 no |
| 1789280100 | test1 | 1.213625 no | 1.158615 no | 1.093934 no | 1.061782 no | 1.038201 no | 1.011886 no | 0.998387 no |
| 1789280400 | test1 | 1.044008 no | 0.968931 no | 0.913771 no | 0.909554 no | 0.884727 no | 0.861400 no | 0.846724 no |
| 1789280700 | test1 | 0.323519 no | 0.301577 no | 0.283818 no | 0.277698 no | 0.278482 no | 0.272037 no | 0.269952 no |
| 1789281000 | test1 | 0.138862 no | 0.147708 no | 0.142195 no | 0.164524 no | 0.161564 no | 0.161134 no | 0.158522 no |
| 1789281300 | test1 | 0.191623 no | 0.293617 no | 0.312314 no | 0.438628 no | 0.446684 no | 0.478731 no | 0.487797 no |
| 1789281600 | test1 | 0.605688 no | 0.607655 no | 0.605684 no | 0.592363 no | 0.828337 no | 0.852865 no | 0.859417 no |
| 1789281900 | test1 | 1.327624 no | 1.234150 no | 1.155123 no | 1.120818 no | 1.089271 no | 1.188345 no | 1.168706 no |
| 1789282200 | test1 | 1.223487 no | 1.330331 no | 1.247836 no | 1.212060 no | 1.541483 no | 1.500933 no | 1.669286 no |
| 1789282500 | test1 | 1.793415 no | 1.749547 no | 1.718736 no | 1.889316 no | 1.850751 no | 1.902142 no | 1.879721 no |
| 1789282800 | test1 | 1.889181 no | 1.779030 no | 1.714100 no | 1.683545 no | 1.656227 no | 1.613678 no | 1.586554 no |
| 1789283100 | test1 | 1.243884 no | 1.172382 no | 1.099250 no | 1.070027 no | 1.039910 no | 1.012566 no | 0.995825 no |
| 1789283400 | test1 | 0.313077 no | 0.290753 no | 0.274305 no | 0.269267 no | 0.266861 no | 0.262857 no | 0.258836 no |
| 1789283700 | test1 | 0.203273 no | 0.232828 no | 0.238412 no | 0.310755 no | 0.302847 no | 0.295251 no | 0.291138 no |
| 1789284000 | test1 | 0.317790 no | 0.295228 no | 0.276497 no | 0.269120 no | 0.268295 no | 0.335726 no | 0.339684 no |
| 1789284300 | test1 | 0.313644 no | 0.291967 no | 0.743236 no | 0.724032 no | 0.710732 no | 0.694645 no | 0.682863 no |
| 1789284600 | test1 | 0.866113 no | 0.817650 no | 0.991847 no | 0.962380 no | 0.961023 no | 0.968056 no | 0.952324 no |
| 1789284900 | test1 | 0.911755 no | 0.849035 no | 1.415891 no | 1.388542 no | 1.353951 no | 1.322556 no | 1.299952 no |
| 1789285500 | test1 | 2.024906 no | 1.875627 no | 1.755026 no | 1.702675 no | 1.663926 no | 1.624118 no | 1.874096 no |
| 1789285800 | test1 | 1.313034 no | 1.243365 no | 1.182155 no | 1.209199 no | 1.189461 no | 1.162505 no | 1.142727 no |
| 1789286100 | test1 | 1.312217 no | 1.237591 no | 1.158387 no | 1.123980 no | 1.097863 no | 1.069601 no | 1.095496 no |
| 1789286400 | test1 | 1.265521 no | 1.220423 no | 1.532206 no | 1.488036 no | 1.527245 no | 1.486900 no | 1.464149 no |
| 1789286700 | test1 | 1.574466 no | 1.459578 no | 1.401175 no | 1.359908 no | 1.322480 no | 1.386943 no | 1.366232 no |
| 1789287000 | test1 | 1.223731 no | 1.146609 no | 1.102486 no | 1.166023 no | 1.166808 no | 1.350020 no | 1.326972 no |
| 1789287300 | test1 | 1.371295 no | 1.270882 no | 1.317451 no | 1.287653 no | 1.259889 no | 1.240739 no | 1.225486 no |
| 1789287600 | test1 | 0.906566 no | 0.897596 no | 0.851306 no | 0.837338 no | 0.816063 no | 0.822486 no | 0.840078 no |
| 1789287900 | test1 | 0.752163 no | 0.711987 no | 0.672953 no | 0.670021 no | 0.674348 no | 0.672808 no | 0.664449 no |
| 1789288200 | test1 | 1.054536 no | 1.466936 no | 1.420666 no | 1.588313 no | 2.206522 yes | 2.305826 yes | 2.343513 yes |
| 1789288500 | test1 | 3.272752 yes | 3.154307 yes | 3.030138 yes | 2.941628 yes | 2.865143 yes | 3.152784 yes | 3.262152 yes |
| 1789288800 | test1 | 3.270039 yes | 3.100082 yes | 2.995948 yes | 2.959903 yes | 2.895588 yes | 2.859585 yes | 2.816379 yes |
| 1789289100 | test1 | 2.236467 yes | 2.309815 yes | 2.181109 yes | 2.117736 no | 2.059970 no | 2.033806 no | 2.006734 no |
| 1789289400 | test1 | 1.774015 no | 1.674554 no | 1.838770 no | 1.798121 no | 1.921714 no | 1.929689 no | 1.932209 no |
| 1789289700 | test1 | 2.133331 yes | 2.257955 yes | 2.214266 yes | 2.151649 no | 2.168839 yes | 2.116339 no | 2.081787 no |
| 1789290000 | test1 | 1.886129 no | 1.753848 no | 1.798378 no | 1.857754 no | 1.820364 no | 1.781551 no | 1.773094 no |
| 1789290300 | test1 | 1.695355 no | 1.711797 no | 1.811686 no | 1.760048 no | 1.712992 no | 1.685827 no | 1.659256 no |
| 1789290600 | test1 | 1.577895 no | 1.723126 no | 1.734110 no | 1.726582 no | 1.687657 no | 1.648621 no | 1.620509 no |
| 1789290900 | test1 | 2.105574 no | 2.060973 no | 1.968820 no | 1.947297 no | 1.893391 no | 1.874882 no | 1.845139 no |
| 1789291200 | test1 | 2.084168 no | 1.987011 no | 1.893263 no | 1.862444 no | 1.827655 no | 1.851307 no | 2.846722 yes |
| 1789291500 | test1 | 4.144275 yes | 3.952782 yes | 3.710185 yes | 3.622025 yes | 3.537910 yes | 3.461106 yes | 3.419060 yes |
| 1789291800 | test1 | 3.017095 yes | 3.104090 yes | 3.095329 yes | 3.107851 yes | 3.062479 yes | 3.030771 yes | 2.991871 yes |
| 1789292100 | test1 | 2.856272 yes | 3.196774 yes | 3.153710 yes | 3.380747 yes | 3.336320 yes | 3.264217 yes | 3.224530 yes |
| 1789292700 | test1 | 1.082965 no | 1.159473 no | 1.243260 no | 1.274571 no | 1.239148 no | 1.242086 no | 1.221866 no |
| 1789293000 | test1 | 1.173142 no | 1.092309 no | 1.040922 no | 1.144065 no | 1.164216 no | 1.270875 no | 1.262010 no |
| 1789293300 | test1 | 1.346030 no | 1.429472 no | 1.556148 no | 1.520892 no | 1.480416 no | 1.469703 no | 1.744027 no |
| 1789293600 | test1 | 2.087151 no | 1.942589 no | 1.851645 no | 1.800406 no | 1.752045 no | 1.707712 no | 1.681496 no |
| 1789293900 | test1 | 0.996821 no | 0.933235 no | 0.902129 no | 0.887348 no | 1.126167 no | 1.097342 no | 1.078887 no |
| 1789294200 | test1 | 1.168189 no | 1.268665 no | 1.412598 no | 1.461203 no | 1.512202 no | 1.475598 no | 1.452100 no |
| 1789294500 | test1 | 1.515063 no | 1.416672 no | 1.325666 no | 1.309749 no | 1.292704 no | 1.304369 no | 1.285568 no |
| 1789294800 | test1 | 0.908829 no | 0.862574 no | 0.840166 no | 0.824565 no | 0.811225 no | 0.799679 no | 0.802823 no |
| 1789295100 | test1 | 0.748872 no | 0.701617 no | 0.664539 no | 0.649200 no | 0.639549 no | 0.670135 no | 0.672821 no |
| 1789295400 | test1 | 0.541530 no | 0.621667 no | 0.611223 no | 0.667898 no | 0.703761 no | 0.698046 no | 0.701462 no |
| 1789295700 | test1 | 0.806068 no | 0.764777 no | 0.828540 no | 0.846472 no | 0.830473 no | 0.835268 no | 0.826859 no |
| 1789296000 | test1 | 0.822708 no | 0.809529 no | 0.803601 no | 0.814028 no | 0.846915 no | 0.859811 no | 0.848205 no |
| 1789296300 | test1 | 1.138312 no | 1.063673 no | 1.032433 no | 1.002542 no | 0.976425 no | 0.950743 no | 0.935336 no |
| 1789296900 | test2 | 1.343308 no | 1.327805 no | 1.794787 no | 1.900730 no | 1.875285 no | 1.844014 no | 1.813923 no |
| 1789297200 | test2 | 2.330450 yes | 2.252582 yes | 3.449587 yes | 3.423685 yes | 3.354390 yes | 3.346137 yes | 3.298013 yes |
| 1789297500 | test2 | 3.659192 yes | 3.443881 yes | 3.306571 yes | 3.262798 yes | 3.198501 yes | 3.143253 yes | 3.090620 yes |
| 1789297800 | test2 | 1.794593 no | 1.980413 no | 2.030990 no | 2.029620 no | 2.010377 no | 1.969508 no | 1.971914 no |
| 1789298100 | test2 | 2.048176 no | 1.993663 no | 2.018372 no | 2.045560 no | 1.989853 no | 2.254904 yes | 2.216873 yes |
| 1789298400 | test2 | 2.227335 yes | 2.231650 yes | 2.213224 yes | 2.157842 no | 2.098326 no | 2.065036 no | 2.041997 no |
| 1789298700 | test2 | 1.509204 no | 1.410095 no | 1.322814 no | 1.312803 no | 1.278719 no | 1.244784 no | 1.284147 no |
| 1789299000 | test2 | 0.782785 no | 0.739310 no | 0.750597 no | 0.795926 no | 0.804110 no | 0.856001 no | 0.860217 no |
| 1789299300 | test2 | 1.325029 no | 1.350665 no | 1.313838 no | 1.339561 no | 1.304601 no | 1.283432 no | 1.270353 no |
| 1789299600 | test2 | 1.446063 no | 1.475964 no | 1.391364 no | 1.350361 no | 1.335030 no | 1.306202 no | 1.283901 no |
| 1789299900 | test2 | 0.993728 no | 0.943419 no | 0.984658 no | 0.963989 no | 0.989363 no | 0.993979 no | 0.978969 no |
| 1789300200 | test2 | 1.149530 no | 1.072467 no | 1.073805 no | 1.050790 no | 1.031554 no | 1.007744 no | 0.995836 no |
| 1789300500 | test2 | 1.007783 no | 0.984757 no | 1.101009 no | 1.075854 no | 1.076521 no | 1.088068 no | 1.070397 no |
| 1789300800 | test2 | 1.250394 no | 1.170008 no | 1.114579 no | 1.086194 no | 1.065437 no | 1.052922 no | 1.036262 no |
| 1789301100 | test2 | 0.993801 no | 0.977268 no | 0.932263 no | 0.907893 no | 0.885116 no | 0.863857 no | 0.849588 no |
| 1789301400 | test2 | 0.803791 no | 0.852477 no | 0.812614 no | 0.828638 no | 0.813223 no | 0.801195 no | 0.795017 no |
| 1789301700 | test2 | 1.168068 no | 1.348801 no | 1.401005 no | 1.370964 no | 1.333087 no | 1.320747 no | 1.301186 no |
| 1789302000 | test2 | 1.520967 no | 1.431533 no | 1.358856 no | 1.363158 no | 1.346855 no | 1.315221 no | 1.295691 no |
| 1789302300 | test2 | 0.699356 no | 0.651917 no | 0.631956 no | 0.726235 no | 0.714686 no | 0.703933 no | 0.699436 no |
| 1789302600 | test2 | 1.230070 no | 1.234595 no | 1.168297 no | 1.141488 no | 1.114753 no | 1.089651 no | 1.172479 no |
| 1789302900 | test2 | 1.460194 no | 1.561372 no | 1.533653 no | 1.497252 no | 1.457885 no | 1.454630 no | 1.435276 no |
| 1789303200 | test2 | 1.487849 no | 1.580188 no | 1.652286 no | 1.614883 no | 1.584530 no | 1.543126 no | 1.519759 no |
| 1789303500 | test2 | 1.654979 no | 1.551428 no | 1.499569 no | 1.465924 no | 1.466885 no | 1.471129 no | 1.468240 no |
| 1789304100 | test2 | 1.163665 no | 1.092499 no | 1.078971 no | 1.051104 no | 1.143469 no | 1.134690 no | 1.658757 no |
| 1789304400 | test2 | 1.851249 no | 1.723442 no | 1.621699 no | 1.593377 no | 1.549254 no | 1.534021 no | 1.540310 no |
| 1789304700 | test2 | 1.265950 no | 1.196512 no | 1.172200 no | 1.268968 no | 1.264365 no | 1.232899 no | 1.212615 no |
| 1789305000 | test2 | 1.367179 no | 1.271841 no | 1.300730 no | 1.262800 no | 1.231107 no | 1.200053 no | 1.180081 no |
| 1789305300 | test2 | 0.747951 no | 0.762819 no | 0.873746 no | 0.853659 no | 0.857660 no | 0.839521 no | 0.830626 no |
| 1789305600 | test2 | 1.034793 no | 1.100687 no | 1.186891 no | 1.181245 no | 1.183600 no | 1.468696 no | 1.479509 no |
| 1789306500 | test2 | 1.904343 no | 1.769963 no | 1.735528 no | 1.695241 no | 1.652538 no | 1.613345 no | 1.588014 no |
| 1789306800 | test2 | 0.918621 no | 1.095593 no | 1.074765 no | 1.119304 no | 1.120367 no | 1.093581 no | 1.078992 no |
| 1789307100 | test2 | 1.324882 no | 1.381397 no | 1.321143 no | 1.305044 no | 1.287380 no | 1.281001 no | 1.346126 no |
| 1789307400 | test2 | 1.468182 no | 1.436654 no | 1.690173 no | 1.780028 no | 1.734199 no | 1.740726 no | 1.717435 no |
| 1789307700 | test2 | 1.784537 no | 1.657376 no | 1.556939 no | 1.515512 no | 1.487952 no | 1.475543 no | 1.451186 no |
| 1789308000 | test2 | 0.794150 no | 0.767873 no | 0.774917 no | 0.870970 no | 0.855520 no | 0.835550 no | 0.830369 no |
| 1789308300 | test2 | 0.891097 no | 0.953495 no | 0.995039 no | 1.028672 no | 1.005899 no | 0.998317 no | 1.002876 no |
| 1789308600 | test2 | 1.034795 no | 1.071553 no | 1.084412 no | 1.065892 no | 1.097134 no | 1.079810 no | 1.064263 no |
| 1789308900 | test2 | 2.129978 yes | 2.334890 yes | 2.271363 yes | 2.249791 yes | 2.325853 yes | 2.276919 yes | 2.241049 yes |
| 1789309200 | test2 | 2.707113 yes | 2.519438 yes | 2.402755 yes | 2.389530 yes | 2.340042 yes | 2.294913 yes | 2.260190 yes |
| 1789309500 | test2 | 1.445948 no | 1.356480 no | 1.317757 no | 1.301235 no | 1.364526 no | 1.418276 no | 1.395299 no |
| 1789309800 | test2 | 1.353309 no | 1.263064 no | 1.194016 no | 1.248564 no | 1.223257 no | 1.224429 no | 1.204763 no |
| 1789310100 | test2 | 1.163863 no | 1.796961 no | 1.757309 no | 1.713061 no | 1.742401 no | 1.889211 no | 1.934501 no |
| 1789310400 | test2 | 2.512130 yes | 2.545233 yes | 2.428771 yes | 2.356763 yes | 2.313642 yes | 2.263238 yes | 2.224705 yes |
| 1789310700 | test2 | 2.123034 no | 2.162596 yes | 2.054020 no | 2.005775 no | 1.956865 no | 1.931483 no | 1.899355 no |
| 1789311000 | test2 | 1.629124 no | 1.585087 no | 2.003578 no | 1.963575 no | 1.913676 no | 1.866111 no | 1.849644 no |
| 1789311300 | test2 | 1.820508 no | 1.709187 no | 1.653668 no | 1.694469 no | 1.735897 no | 1.691052 no | 1.679230 no |
| 1789311600 | test2 | 2.263888 yes | 2.105871 no | 2.035979 no | 1.982713 no | 1.932524 no | 1.898258 no | 1.867777 no |
| 1789311900 | test2 | 2.077110 no | 1.937821 no | 1.855614 no | 1.816088 no | 1.764984 no | 1.720246 no | 1.692924 no |
| 1789312200 | test2 | 0.875214 no | 0.815234 no | 0.771922 no | 0.782554 no | 0.926697 no | 0.904514 no | 0.889552 no |
| 1789312500 | test2 | 0.999920 no | 1.089259 no | 1.082524 no | 1.091509 no | 1.163483 no | 1.177282 no | 1.161554 no |
| 1789312800 | test2 | 1.220086 no | 1.203286 no | 1.224764 no | 1.261536 no | 1.353976 no | 1.505858 no | 1.608694 no |
| 1789313100 | test2 | 2.166714 yes | 2.079567 no | 2.235962 yes | 2.169525 yes | 2.348934 yes | 2.345414 yes | 2.318786 yes |
| 1789313700 | test2 | 1.275951 no | 1.288561 no | 1.207329 no | 1.172323 no | 1.146285 no | 1.116009 no | 1.097879 no |
| 1789314000 | test2 | 0.780148 no | 0.850637 no | 0.798682 no | 0.787870 no | 1.908639 no | 1.871572 no | 1.842472 no |
| 1789314300 | test2 | 2.284410 yes | 2.206374 yes | 2.066892 no | 2.008561 no | 2.001485 no | 1.950039 no | 1.918926 no |
| 1789314600 | test2 | 1.015961 no | 1.080979 no | 1.083193 no | 1.054715 no | 1.163369 no | 1.133948 no | 1.131324 no |
| 1789314900 | test2 | 1.265180 no | 1.315040 no | 1.237425 no | 1.206780 no | 1.251494 no | 1.250904 no | 1.229738 no |
| 1789315200 | test2 | 1.236665 no | 1.184610 no | 1.216084 no | 1.215111 no | 1.186276 no | 1.278232 no | 1.300536 no |
| 1789315500 | test2 | 1.241321 no | 1.649999 no | 1.735614 no | 1.712532 no | 1.692992 no | 1.868653 no | 1.863459 no |
| 1789315800 | test2 | 2.307934 yes | 2.581885 yes | 2.908767 yes | 2.857419 yes | 2.782323 yes | 2.709749 yes | 2.666211 yes |
| 1789316100 | test2 | 2.879852 yes | 2.694664 yes | 2.526089 yes | 2.452516 yes | 2.424009 yes | 2.360879 yes | 2.321508 yes |
| 1789316400 | test2 | 1.434525 no | 1.477196 no | 1.398859 no | 1.403777 no | 1.368765 no | 1.368098 no | 1.468196 no |
| 1789316700 | test2 | 1.436951 no | 1.543810 no | 1.540823 no | 1.529422 no | 1.508835 no | 1.475703 no | 1.454562 no |
| 1789317000 | test2 | 1.261545 no | 1.603549 no | 1.535777 no | 1.495268 no | 1.453914 no | 1.415960 no | 1.399738 no |
| 1789317300 | test2 | 1.368142 no | 1.276382 no | 1.216173 no | 1.217185 no | 1.245014 no | 1.213641 no | 1.203775 no |
| 1789317600 | test2 | 1.033060 no | 1.422288 no | 2.156908 no | 2.243468 yes | 2.365529 yes | 2.315045 yes | 2.301140 yes |
| 1789317900 | test2 | 2.927688 yes | 2.731112 yes | 2.582194 yes | 2.508980 yes | 2.446168 yes | 2.439408 yes | 2.399662 yes |
| 1789318200 | test2 | 1.198846 no | 1.224419 no | 1.192607 no | 1.172058 no | 1.144178 no | 1.204481 no | 1.188581 no |
| 1789318500 | test2 | 1.011720 no | 1.329844 no | 1.398539 no | 1.388107 no | 1.399954 no | 1.369585 no | 1.359103 no |
| 1789319100 | test2 | 1.043982 no | 0.976690 no | 0.952343 no | 0.932925 no | 0.913997 no | 1.119327 no | 1.164011 no |
| 1789319400 | test2 | 1.392541 no | 1.337580 no | 1.374715 no | 1.730006 no | 1.704651 no | 1.686126 no | 1.660819 no |
| 1789320000 | test2 | 1.088600 no | 1.214105 no | 1.185540 no | 1.160274 no | 1.135034 no | 1.105479 no | 1.116824 no |
| 1789320300 | test2 | 0.997909 no | 0.926155 no | 0.912817 no | 0.916396 no | 0.932364 no | 0.928563 no | 0.913052 no |
| 1789320600 | test2 | 0.632111 no | 1.200103 no | 1.147289 no | 1.118201 no | 1.119173 no | 1.100483 no | 1.088510 no |
| 1789320900 | test2 | 1.330574 no | 1.403617 no | 1.324817 no | 1.337873 no | 1.301388 no | 1.275006 no | 1.254424 no |
| 1789321200 | test2 | 1.020637 no | 0.967507 no | 0.913496 no | 0.898613 no | 0.874450 no | 0.851464 no | 0.840802 no |
| 1789321500 | test2 | 0.459859 no | 0.739129 no | 0.707932 no | 0.687426 no | 1.021470 no | 0.999166 no | 0.983694 no |
| 1789321800 | test2 | 1.240699 no | 1.174077 no | 1.149794 no | 1.126438 no | 1.133708 no | 1.119972 no | 1.102702 no |
| 1789322100 | test2 | 0.976287 no | 0.933424 no | 0.885251 no | 0.861029 no | 0.837906 no | 0.816596 no | 0.848048 no |
| 1789322400 | test2 | 1.039047 no | 1.022623 no | 0.975859 no | 0.948167 no | 0.925456 no | 0.914604 no | 0.901686 no |
| 1789322700 | test2 | 0.895262 no | 0.837411 no | 0.821403 no | 0.812906 no | 0.833022 no | 0.822471 no | 0.816489 no |
| 1789323000 | test2 | 0.657843 no | 0.614188 no | 0.575377 no | 0.568204 no | 0.692889 no | 1.223539 no | 1.205447 no |
| 1789323300 | test2 | 1.435447 no | 1.499501 no | 1.427865 no | 1.386848 no | 1.351283 no | 1.350588 no | 1.345420 no |
| 1789323600 | test2 | 1.061565 no | 1.010854 no | 0.987130 no | 0.964046 no | 1.052900 no | 1.033332 no | 1.025945 no |
| 1789323900 | test2 | 0.914129 no | 0.960947 no | 0.924676 no | 0.906808 no | 0.883531 no | 0.862696 no | 0.848077 no |
| 1789324200 | test2 | 1.114001 no | 1.081878 no | 1.060955 no | 1.121413 no | 1.091474 no | 1.142412 no | 1.123334 no |
| 1789324500 | test2 | 1.283736 no | 1.246353 no | 1.191869 no | 1.165954 no | 1.135342 no | 1.107072 no | 1.089943 no |
| 1789324800 | test2 | 0.580721 no | 0.552835 no | 0.749869 no | 0.743897 no | 0.742907 no | 0.725132 no | 0.712921 no |
| 1789325100 | test2 | 0.740893 no | 0.698941 no | 0.665786 no | 0.647760 no | 0.631798 no | 0.617753 no | 0.607812 no |
| 1789325400 | test2 | 0.531875 no | 0.518673 no | 0.498931 no | 0.494548 no | 0.487911 no | 0.475011 no | 0.466962 no |
| 1789325700 | test2 | 0.678042 no | 0.638494 no | 0.679645 no | 0.686358 no | 0.673938 no | 0.671259 no | 0.661198 no |
| 1789326000 | test2 | 0.935830 no | 0.872985 no | 0.979016 no | 0.955491 no | 0.946628 no | 0.962470 no | 0.947364 no |
| 1789326300 | test2 | 0.922674 no | 0.867298 no | 1.245498 no | 1.221705 no | 2.078365 no | 2.026141 no | 2.033833 no |
| 1789326600 | test2 | 2.462973 yes | 2.286986 yes | 2.186443 yes | 2.127986 no | 2.111882 no | 2.058238 no | 2.024179 no |
| 1789327200 | test2 | 1.122182 no | 1.074316 no | 1.249613 no | 1.215218 no | 1.182548 no | 1.154344 no | 1.135302 no |
| 1789327500 | test2 | 0.958178 no | 0.891775 no | 0.840607 no | 0.821163 no | 0.807280 no | 0.800280 no | 0.791659 no |
| 1789327800 | test2 | 0.432884 no | 1.008914 no | 0.968423 no | 0.973310 no | 0.950108 no | 1.032572 no | 1.021352 no |
| 1789328100 | test2 | 1.280517 no | 1.189463 no | 1.250592 no | 1.223502 no | 1.191822 no | 1.161339 no | 1.145355 no |
| 1789328400 | test2 | 0.802856 no | 0.757558 no | 0.740121 no | 0.739809 no | 0.743448 no | 0.725742 no | 0.714805 no |
| 1789328700 | test2 | 0.535817 no | 0.516808 no | 0.514453 no | 0.533532 no | 0.519565 no | 0.509293 no | 0.521649 no |
| 1789329000 | test2 | 0.450720 no | 0.423492 no | 0.563569 no | 0.548492 no | 0.675836 no | 0.669491 no | 0.677682 no |
| 1789329300 | test2 | 0.791721 no | 0.737890 no | 0.734251 no | 0.717830 no | 0.698487 no | 0.681263 no | 0.670409 no |
| 1789329600 | test2 | 0.480378 no | 0.519812 no | 0.493084 no | 0.478913 no | 0.465684 no | 0.660952 no | 0.659258 no |
| 1789329900 | test2 | 0.776041 no | 0.853404 no | 0.824995 no | 0.809738 no | 0.791707 no | 0.770633 no | 0.759770 no |
| 1789330200 | test2 | 0.644087 no | 0.743831 no | 0.704064 no | 0.684519 no | 0.679597 no | 0.830662 no | 0.816507 no |
| 1789330500 | test2 | 0.900793 no | 0.842336 no | 0.807675 no | 0.784572 no | 0.763117 no | 0.742911 no | 0.731513 no |
| 1789330800 | test2 | 0.638078 no | 0.723004 no | 0.698730 no | 0.680368 no | 0.661310 no | 0.643703 no | 0.632732 no |
| 1789331100 | test2 | 0.563427 no | 0.539064 no | 0.565079 no | 0.551132 no | 0.536584 no | 0.582700 no | 0.574109 no |
| 1789331400 | test2 | 0.587307 no | 0.667491 no | 1.020872 no | 1.006200 no | 0.982689 no | 0.961570 no | 0.945954 no |
| 1789331700 | test2 | 1.676759 no | 1.617158 no | 1.532549 no | 1.497467 no | 1.491013 no | 1.454268 no | 1.433866 no |
| 1789332000 | test2 | 1.496980 no | 1.407171 no | 1.334531 no | 1.300304 no | 1.281163 no | 1.252713 no | 1.236922 no |
| 1789332300 | test2 | 0.636056 no | 0.761421 no | 0.738952 no | 0.758550 no | 0.769429 no | 0.761869 no | 1.562765 no |
| 1789332600 | test2 | 1.910211 no | 1.771547 no | 1.675356 no | 1.626583 no | 1.581626 no | 1.540404 no | 1.515795 no |
| 1789332900 | test2 | 0.410533 no | 0.417121 no | 0.450620 no | 0.440616 no | 0.431572 no | 0.422110 no | 0.416391 no |
| 1789333200 | test2 | 0.686163 no | 0.653133 no | 0.638856 no | 0.624940 no | 0.615954 no | 0.604297 no | 0.622856 no |
| 1789333500 | test2 | 0.931025 no | 0.866396 no | 0.819267 no | 0.797136 no | 0.777120 no | 0.779044 no | 0.790683 no |
| 1789333800 | test2 | 0.885046 no | 0.962862 no | 0.961613 no | 1.004909 no | 0.991401 no | 0.991935 no | 0.975266 no |
| 1789334400 | test2 | 0.923164 no | 0.862966 no | 1.420738 no | 1.398070 no | 1.359558 no | 1.333495 no | 1.315242 no |
| 1789334700 | test2 | 1.477271 no | 1.376723 no | 1.325906 no | 1.288001 no | 1.270755 no | 1.238533 no | 1.217950 no |
| 1789335000 | test2 | 0.681854 no | 0.641925 no | 1.013481 no | 0.984813 no | 0.959940 no | 0.938319 no | 0.927478 no |
| 1789335300 | test2 | 1.051820 no | 1.039289 no | 0.990489 no | 1.033815 no | 1.005322 no | 0.980007 no | 1.104579 no |
| 1789335600 | test2 | 1.197150 no | 1.204875 no | 1.152476 no | 1.137234 no | 1.170328 no | 1.140732 no | 1.147151 no |
| 1789335900 | test2 | 1.109828 no | 1.033377 no | 1.158363 no | 1.337345 no | 1.317428 no | 1.305340 no | 1.291321 no |
| 1789336200 | test2 | 1.430814 no | 1.329981 no | 1.426441 no | 1.384997 no | 1.346836 no | 1.314991 no | 1.302666 no |
| 1789336500 | test2 | 1.128392 no | 1.045459 no | 1.014090 no | 0.985709 no | 0.959770 no | 1.249783 no | 1.231038 no |
| 1789336800 | test2 | 2.474471 yes | 2.962637 yes | 3.535684 yes | 3.661707 yes | 3.652281 yes | 3.733073 yes | 3.724739 yes |
| 1789337100 | test2 | 4.889395 yes | 9.379860 yes | 9.123078 yes | 9.134149 yes | 8.947348 yes | 8.751524 yes | 8.651389 yes |
| 1789337400 | test2 | 10.137588 yes | 9.478718 yes | 8.985947 yes | 8.743946 yes | 8.534993 yes | 8.336063 yes | 8.205678 yes |
| 1789337700 | test2 | 3.552383 yes | 3.973330 yes | 4.040988 yes | 4.097048 yes | 4.133943 yes | 4.073234 yes | 4.045310 yes |
| 1789338000 | test2 | 4.363133 yes | 4.350080 yes | 4.205793 yes | 4.189883 yes | 4.154528 yes | 4.145627 yes | 4.082054 yes |
| 1789338300 | test2 | 3.287699 yes | 3.226886 yes | 3.304820 yes | 3.507572 yes | 3.446554 yes | 3.423757 yes | 3.401537 yes |
| 1789338600 | test2 | 3.205789 yes | 3.123203 yes | 3.077564 yes | 3.039884 yes | 3.164819 yes | 3.259969 yes | 3.221769 yes |
| 1789338900 | test2 | 3.361193 yes | 3.252970 yes | 3.369485 yes | 3.295192 yes | 3.231296 yes | 3.219425 yes | 3.178539 yes |
| 1789339200 | test2 | 3.015271 yes | 3.029022 yes | 2.929976 yes | 2.885940 yes | 2.866808 yes | 2.820860 yes | 2.788846 yes |
| 1789339500 | test2 | 2.394795 yes | 2.280767 yes | 2.265134 yes | 2.524683 yes | 2.469142 yes | 2.658325 yes | 2.616869 yes |
| 1789339800 | test2 | 2.739209 yes | 2.632529 yes | 2.596024 yes | 2.795905 yes | 2.743045 yes | 2.720368 yes | 2.690776 yes |
| 1789340100 | test2 | 2.262122 yes | 2.569080 yes | 2.641199 yes | 2.976292 yes | 2.940843 yes | 3.032313 yes | 3.014724 yes |
| 1789340400 | test2 | 3.440815 yes | 3.300128 yes | 3.267350 yes | 3.275577 yes | 3.224868 yes | 3.181488 yes | 3.128918 yes |
| 1789340700 | test2 | 2.589874 yes | 2.491123 yes | 2.504438 yes | 2.495822 yes | 2.500500 yes | 2.444559 yes | 2.418002 yes |
| 1789341000 | test2 | 2.208424 yes | 2.225066 yes | 2.144197 no | 2.436304 yes | 2.420138 yes | 2.458204 yes | 2.474421 yes |
| 1789341600 | test2 | 2.965214 yes | 3.248440 yes | 3.124719 yes | 3.093178 yes | 3.075860 yes | 3.139326 yes | 3.091804 yes |
| 1789341900 | test2 | 2.696743 yes | 2.603623 yes | 2.610021 yes | 2.577193 yes | 2.509870 yes | 2.468323 yes | 2.507671 yes |
| 1789342200 | test2 | 2.825405 yes | 3.139593 yes | 3.191878 yes | 3.162776 yes | 3.076006 yes | 3.015195 yes | 2.976798 yes |
| 1789342500 | test2 | 3.735617 yes | 3.572260 yes | 3.511105 yes | 3.446398 yes | 3.446006 yes | 3.367543 yes | 3.359376 yes |
| 1789342800 | test2 | 2.823619 yes | 2.700332 yes | 2.890956 yes | 2.812565 yes | 2.751446 yes | 2.728498 yes | 2.727985 yes |
| 1789343100 | test2 | 2.660178 yes | 2.897427 yes | 2.750204 yes | 2.724176 yes | 2.726604 yes | 2.658074 yes | 2.615682 yes |
| 1789343400 | test2 | 2.424807 yes | 2.312211 yes | 2.174523 no | 2.128848 no | 2.073364 no | 2.022540 no | 1.988191 no |
| 1789343700 | test2 | 1.252827 no | 1.351275 no | 1.504231 no | 1.616152 no | 1.584815 no | 1.573894 no | 1.571783 no |
| 1789344000 | test2 | 2.048296 no | 2.126547 no | 2.068818 no | 2.028788 no | 2.070824 no | 2.069762 no | 2.053258 no |
| 1789344300 | test2 | 2.301633 yes | 2.241958 yes | 2.449934 yes | 3.085883 yes | 3.169577 yes | 3.144768 yes | 3.123613 yes |
| 1789344600 | test2 | 3.627548 yes | 3.665904 yes | 3.489066 yes | 3.462143 yes | 3.386615 yes | 3.320053 yes | 3.268646 yes |
| 1789344900 | test2 | 2.567930 yes | 2.413899 yes | 2.453866 yes | 2.499306 yes | 2.509224 yes | 2.685494 yes | 2.649665 yes |
| 1789345200 | test2 | 2.701900 yes | 2.695928 yes | 2.872710 yes | 2.883939 yes | 2.897739 yes | 2.860287 yes | 2.833198 yes |
| 1789345500 | test2 | 3.031225 yes | 3.512046 yes | 3.490044 yes | 3.557455 yes | 4.412569 yes | 4.590996 yes | 4.669008 yes |
| 1789345800 | test2 | 5.850977 yes | 5.679905 yes | 5.555501 yes | 5.489444 yes | 5.921614 yes | 5.809596 yes | 5.744725 yes |
| 1789346100 | test2 | 5.198856 yes | 5.341071 yes | 5.192125 yes | 5.135944 yes | 5.037591 yes | 4.972138 yes | 4.925415 yes |
| 1789346400 | test2 | 4.028460 yes | 3.779831 yes | 3.686901 yes | 3.613391 yes | 3.529085 yes | 3.484138 yes | 3.438751 yes |
| 1789346700 | test2 | 2.867427 yes | 3.155297 yes | 2.995029 yes | 2.918856 yes | 2.853728 yes | 2.819797 yes | 2.972889 yes |
| 1789347000 | test2 | 3.287826 yes | 3.104251 yes | 2.973248 yes | 2.902780 yes | 2.853346 yes | 2.860720 yes | 2.820266 yes |
| 1789347300 | test2 | 1.807293 no | 1.769130 no | 1.797686 no | 1.773775 no | 1.781931 no | 1.784150 no | 1.755873 no |
| 1789347600 | test2 | 2.115785 no | 2.324961 yes | 2.206433 yes | 2.144112 no | 2.207418 yes | 2.183336 yes | 2.177578 yes |
| 1789347900 | test2 | 2.580151 yes | 2.888668 yes | 3.022864 yes | 2.937270 yes | 2.922595 yes | 3.065808 yes | 3.069157 yes |
| 1789348200 | test2 | 3.291372 yes | 3.355540 yes | 3.295066 yes | 3.281685 yes | 3.207913 yes | 3.151124 yes | 3.114034 yes |
| 1789348800 | test2 | 2.969238 yes | 2.866933 yes | 2.799615 yes | 2.893683 yes | 2.865720 yes | 2.834353 yes | 2.799252 yes |
| 1789349100 | test2 | 2.387177 yes | 2.678725 yes | 2.639042 yes | 2.641055 yes | 2.636612 yes | 2.585242 yes | 2.557499 yes |
| 1789349400 | test2 | 2.531746 yes | 2.511638 yes | 2.484477 yes | 2.610977 yes | 2.624143 yes | 2.660321 yes | 2.638203 yes |
| 1789349700 | test2 | 2.715352 yes | 2.727272 yes | 2.679742 yes | 2.625116 yes | 2.599705 yes | 2.595948 yes | 2.579907 yes |
| 1789350000 | test2 | 2.987336 yes | 3.364767 yes | 3.343453 yes | 3.337654 yes | 3.642019 yes | 3.645721 yes | 3.606928 yes |
| 1789350300 | test2 | 4.229241 yes | 3.969691 yes | 3.859997 yes | 3.790285 yes | 3.721010 yes | 3.713443 yes | 3.665590 yes |
| 1789350600 | test2 | 2.628073 yes | 2.883083 yes | 2.811378 yes | 2.789411 yes | 2.725446 yes | 2.669090 yes | 2.647490 yes |
| 1789350900 | test2 | 2.592523 yes | 2.683344 yes | 2.809230 yes | 4.260631 yes | 4.236118 yes | 4.197156 yes | 4.197088 yes |
| 1789351200 | test2 | 4.966058 yes | 4.643320 yes | 4.418181 yes | 4.413214 yes | 4.301023 yes | 4.202567 yes | 4.133643 yes |
| 1789351500 | test2 | 2.468561 yes | 2.846061 yes | 2.830511 yes | 2.892268 yes | 3.027892 yes | 3.135471 yes | 3.119148 yes |
| 1789351800 | test2 | 3.670925 yes | 3.708861 yes | 4.428598 yes | 4.366012 yes | 4.248302 yes | 4.139491 yes | 4.125164 yes |
| 1789352100 | test2 | 4.411897 yes | 4.186245 yes | 3.941176 yes | 3.828514 yes | 3.740720 yes | 3.707931 yes | 3.662791 yes |
| 1789352400 | test2 | 2.531219 yes | 2.466180 yes | 2.695397 yes | 2.854340 yes | 2.891832 yes | 2.895723 yes | 2.878986 yes |
| 1789352700 | test2 | 6.442909 yes | 6.546722 yes | 6.453398 yes | 6.288737 yes | 6.149682 yes | 6.061858 yes | 5.963390 yes |
| 1789353000 | test2 | 7.300932 yes | 7.066893 yes | 6.768568 yes | 6.581426 yes | 6.403980 yes | 6.269352 yes | 6.166642 yes |
| 1789353300 | test2 | 3.815802 yes | 3.675164 yes | 3.494431 yes | 3.530270 yes | 3.445246 yes | 3.413865 yes | 3.381292 yes |
| 1789353600 | test2 | 2.553608 yes | 2.457398 yes | 2.559795 yes | 2.589162 yes | 2.537825 yes | 2.551604 yes | 2.525162 yes |
| 1789353900 | test2 | 2.520569 yes | 2.609905 yes | 2.572391 yes | 2.523309 yes | 2.513910 yes | 2.615826 yes | 2.596585 yes |
| 1789354200 | test2 | 3.197534 yes | 3.120273 yes | 4.058844 yes | 4.052881 yes | 4.049980 yes | 4.028809 yes | 3.979311 yes |
| 1789354500 | test2 | 4.757194 yes | 4.514327 yes | 4.321978 yes | 4.214825 yes | 4.137667 yes | 4.044665 yes | 3.977847 yes |
| 1789354800 | test2 | 3.130637 yes | 3.128864 yes | 3.236878 yes | 3.263555 yes | 3.445484 yes | 3.370645 yes | 3.341945 yes |
| 1789355100 | test2 | 3.808761 yes | 3.696946 yes | 3.642002 yes | 3.705850 yes | 3.884448 yes | 3.882183 yes | 3.904114 yes |
| 1789355400 | test2 | 3.928966 yes | 3.696284 yes | 3.537973 yes | 3.448148 yes | 3.364623 yes | 3.401638 yes | 3.369790 yes |
| 1789356000 | test2 | 2.017059 no | 2.010488 no | 2.265180 yes | 2.518532 yes | 2.483664 yes | 2.439382 yes | 2.460113 yes |
| 1789356300 | test2 | 2.996987 yes | 3.158195 yes | 3.058800 yes | 3.192417 yes | 3.136349 yes | 3.060339 yes | 3.014912 yes |
| 1789356600 | test2 | 2.923996 yes | 3.069619 yes | 3.001136 yes | 3.009756 yes | 2.961666 yes | 2.929543 yes | 2.887443 yes |
| 1789356900 | test2 | 3.294916 yes | 3.095768 yes | 2.940216 yes | 2.981803 yes | 2.946369 yes | 2.913245 yes | 2.874659 yes |
| 1789357200 | test2 | 2.957093 yes | 2.801456 yes | 2.698229 yes | 2.687174 yes | 2.614625 yes | 2.557824 yes | 2.519452 yes |
| 1789357500 | test2 | 1.676765 no | 1.685348 no | 1.668834 no | 1.697849 no | 1.826650 no | 1.852597 no | 1.822726 no |
| 1789357800 | test2 | 1.931816 no | 1.877336 no | 1.776699 no | 1.762678 no | 1.758557 no | 1.754404 no | 1.800285 no |
| 1789358100 | test2 | 1.644229 no | 1.609083 no | 1.564688 no | 1.525324 no | 1.663972 no | 1.647964 no | 1.636631 no |
| 1789358400 | test2 | 1.660116 no | 1.969322 no | 1.882138 no | 1.838583 no | 1.866468 no | 1.962998 no | 1.930777 no |
| 1789358700 | test2 | 2.210601 yes | 2.224216 yes | 2.494272 yes | 2.427551 yes | 2.373121 yes | 2.316518 yes | 2.277628 yes |
| 1789359000 | test2 | 2.123268 yes | 2.089263 no | 1.988951 no | 1.930408 no | 1.887339 no | 1.978552 no | 1.962309 no |
| 1789359300 | test2 | 1.521851 no | 2.592087 yes | 2.435562 yes | 2.366937 yes | 2.303710 yes | 2.256181 yes | 2.222407 yes |
| 1789359600 | test2 | 2.638948 yes | 2.613912 yes | 2.539456 yes | 2.571948 yes | 2.538403 yes | 2.839006 yes | 2.805420 yes |
| 1789359900 | test2 | 2.907948 yes | 2.804839 yes | 2.714088 yes | 2.677967 yes | 2.741262 yes | 2.700359 yes | 2.661918 yes |
| 1789360200 | test2 | 2.148997 yes | 2.070958 no | 2.061351 no | 2.050702 no | 2.003275 no | 2.470822 yes | 2.447627 yes |
| 1789360500 | test2 | 2.341776 yes | 2.219807 yes | 2.168464 no | 2.294370 yes | 2.314387 yes | 2.279763 yes | 2.243027 yes |
| 1789360800 | test2 | 1.698885 no | 1.636570 no | 1.589537 no | 1.661424 no | 1.859947 no | 1.879764 no | 1.861560 no |
| 1789361100 | test2 | 1.825111 no | 2.506973 yes | 2.379450 yes | 2.318481 yes | 2.282266 yes | 2.265790 yes | 2.236529 yes |
| 1789361400 | test2 | 2.341734 yes | 2.250242 yes | 2.274570 yes | 2.209762 yes | 2.152696 no | 2.102442 no | 2.093629 no |
| 1789361700 | test2 | 1.407587 no | 1.378552 no | 1.598412 no | 1.841841 no | 1.914828 no | 1.873115 no | 1.977742 no |
| 1789362000 | test2 | 2.462631 yes | 2.568007 yes | 2.932544 yes | 2.859595 yes | 2.779203 yes | 2.706644 yes | 2.660435 yes |
| 1789362300 | test2 | 2.718309 yes | 2.655277 yes | 2.542651 yes | 2.547159 yes | 2.483167 yes | 2.419408 yes | 2.378312 yes |
| 1789362600 | test2 | 1.648157 no | 1.576711 no | 1.532283 no | 1.549103 no | 1.521621 no | 1.561162 no | 1.546504 no |
| 1789363200 | test2 | 1.195907 no | 1.148553 no | 1.229792 no | 1.255188 no | 1.231431 no | 1.233019 no | 1.220975 no |
| 1789363500 | test2 | 1.139910 no | 1.071435 no | 1.067307 no | 1.055083 no | 1.026509 no | 1.009425 no | 1.033618 no |
| 1789363800 | test2 | 1.011225 no | 1.050799 no | 0.996375 no | 1.170637 no | 1.159555 no | 1.147219 no | 1.130194 no |
| 1789364100 | test2 | 1.266000 no | 1.250407 no | 1.507912 no | 1.491118 no | 1.502286 no | 1.472234 no | 1.447695 no |
| 1789364400 | test2 | 1.703302 no | 1.623846 no | 1.765407 no | 1.772067 no | 1.758321 no | 1.717536 no | 1.688318 no |
| 1789364700 | test2 | 1.673659 no | 1.606430 no | 1.609519 no | 1.592974 no | 1.563842 no | 1.557891 no | 1.547926 no |
| 1789365000 | test2 | 1.207675 no | 1.156537 no | 1.108640 no | 1.077959 no | 1.054827 no | 1.060853 no | 1.052814 no |
| 1789365300 | test2 | 1.179627 no | 1.156534 no | 1.143108 no | 1.158480 no | 1.146041 no | 1.118046 no | 1.137995 no |
| 1789365600 | test2 | 1.606381 no | 1.822140 no | 1.871057 no | 1.819205 no | 1.859542 no | 1.863134 no | 1.872061 no |
| 1789365900 | test2 | 2.525259 yes | 2.407905 yes | 2.487815 yes | 2.656738 yes | 2.621264 yes | 2.631322 yes | 2.588021 yes |
| 1789366200 | test2 | 2.438039 yes | 2.922984 yes | 2.925887 yes | 2.941350 yes | 2.917491 yes | 2.872729 yes | 2.826381 yes |
| 1789366500 | test2 | 2.955783 yes | 2.746557 yes | 2.632109 yes | 2.559124 yes | 2.487572 yes | 2.423649 yes | 2.382897 yes |
| 1789366800 | test2 | 1.468610 no | 1.420486 no | 1.366173 no | 1.359514 no | 1.359920 no | 1.334953 no | 1.313352 no |
| 1789367700 | test2 | 3.895675 yes | 3.633109 yes | 3.426587 yes | 3.591855 yes | 3.495088 yes | 3.455177 yes | 3.396779 yes |
| 1789368000 | test2 | 2.054753 no | 2.748015 yes | 3.076574 yes | 3.152164 yes | 3.368465 yes | 3.305132 yes | 3.350811 yes |
| 1789368300 | test2 | 3.949979 yes | 4.005025 yes | 3.803261 yes | 3.784033 yes | 3.683618 yes | 3.585871 yes | 3.631536 yes |
| 1789368600 | test2 | 2.721925 yes | 2.636591 yes | 2.531863 yes | 2.472556 yes | 2.405569 yes | 2.350983 yes | 2.326939 yes |
| 1789368900 | test2 | 1.446468 no | 1.381313 no | 1.317450 no | 1.288901 no | 1.254967 no | 1.223967 no | 1.206486 no |
| 1789369200 | test2 | 1.554013 no | 2.076806 no | 2.118030 no | 2.076643 no | 2.038784 no | 2.016224 no | 2.009483 no |
| 1789369500 | test2 | 2.670396 yes | 2.597363 yes | 2.475922 yes | 2.459111 yes | 2.440165 yes | 2.397659 yes | 2.444905 yes |
| 1789369800 | test2 | 2.029160 no | 2.001355 no | 1.984594 no | 1.937027 no | 1.888706 no | 1.859389 no | 1.837224 no |
| 1789370100 | test2 | 1.387161 no | 1.465457 no | 1.731485 no | 1.711469 no | 1.924365 no | 1.894909 no | 1.871872 no |
| 1789370400 | test2 | 2.153220 yes | 2.028392 no | 1.925535 no | 1.906566 no | 1.911860 no | 1.876890 no | 1.868296 no |
| 1789370700 | test2 | 1.452254 no | 1.438510 no | 1.424937 no | 1.386609 no | 1.354402 no | 1.358890 no | 1.396247 no |
| 1789371000 | test2 | 1.503931 no | 1.438913 no | 1.373231 no | 1.355220 no | 1.353784 no | 1.338716 no | 1.320677 no |
| 1789371300 | test2 | 1.298269 no | 1.259472 no | 1.333774 no | 1.295824 no | 1.260457 no | 1.228519 no | 1.296170 no |
| 1789371600 | test2 | 1.732559 no | 1.651612 no | 2.139300 no | 2.148007 no | 2.236290 yes | 2.235738 yes | 2.212562 yes |
| 1789371900 | test2 | 3.081982 yes | 3.029812 yes | 3.054527 yes | 2.983053 yes | 2.907735 yes | 2.879229 yes | 2.830280 yes |
| 1789372200 | test2 | 2.545814 yes | 2.459262 yes | 2.586126 yes | 2.547125 yes | 2.483224 yes | 2.417339 yes | 2.378156 yes |
| 1789372500 | test2 | 2.327972 yes | 2.180213 yes | 2.219500 yes | 2.155389 no | 2.096573 no | 2.044200 no | 2.010019 no |
| 1789372800 | test2 | 2.519239 yes | 2.558037 yes | 2.529812 yes | 2.619332 yes | 2.566987 yes | 2.510624 yes | 2.518313 yes |
| 1789373100 | test2 | 3.108292 yes | 3.135727 yes | 3.212156 yes | 3.272439 yes | 3.221317 yes | 3.180445 yes | 3.136726 yes |
| 1789373400 | test2 | 3.449893 yes | 3.768826 yes | 3.638479 yes | 3.680858 yes | 3.589430 yes | 3.525420 yes | 3.486433 yes |
| 1789373700 | test2 | 3.406768 yes | 3.221473 yes | 3.594276 yes | 3.530179 yes | 3.473809 yes | 3.392493 yes | 3.358530 yes |
| 1789374000 | test2 | 2.967763 yes | 2.887360 yes | 2.753491 yes | 2.679171 yes | 2.614825 yes | 2.552481 yes | 2.519027 yes |
| 1789374900 | test2 | 3.461357 yes | 3.305540 yes | 3.202159 yes | 3.115288 yes | 3.069475 yes | 3.234298 yes | 3.191450 yes |
| 1789375200 | test2 | 2.697773 yes | 2.608185 yes | 2.494338 yes | 2.431209 yes | 2.447782 yes | 2.467134 yes | 2.434716 yes |
| 1789375500 | test2 | 2.181587 yes | 2.065409 no | 2.306295 yes | 2.259744 yes | 2.203299 yes | 2.154279 yes | 2.131428 no |
| 1789375800 | test2 | 2.172358 yes | 2.092936 no | 2.149484 no | 2.133954 no | 2.136060 no | 2.086752 no | 2.066971 no |
| 1789377300 | test2 | 2.513816 yes | 2.553562 yes | 2.602653 yes | 2.543437 yes | 2.498766 yes | 2.705209 yes | 2.695326 yes |
| 1789377600 | test2 | 3.017304 yes | 3.311974 yes | 3.156124 yes | 3.107156 yes | 3.026255 yes | 2.960488 yes | 2.912093 yes |
| 1789377900 | test2 | 2.447181 yes | 2.852832 yes | 2.739389 yes | 2.716172 yes | 2.679080 yes | 2.619556 yes | 2.818378 yes |
| 1789378200 | test2 | 3.557342 yes | 3.540374 yes | 3.697879 yes | 3.789606 yes | 3.704030 yes | 3.615823 yes | 3.555254 yes |
| 1789378500 | test2 | 3.729952 yes | 3.562124 yes | 3.362978 yes | 3.268963 yes | 3.279379 yes | 3.217525 yes | 3.177432 yes |
| 1789378800 | test2 | 2.789017 yes | 2.818318 yes | 2.761627 yes | 2.745994 yes | 2.686472 yes | 2.645796 yes | 2.602848 yes |
| 1789379100 | test2 | 2.798483 yes | 2.746738 yes | 2.974368 yes | 2.930908 yes | 2.948536 yes | 3.035449 yes | 3.062569 yes |
| 1789379400 | test2 | 3.634854 yes | 3.893411 yes | 4.935658 yes | 5.023377 yes | 5.072073 yes | 5.119103 yes | 5.076864 yes |
| 1789379700 | test2 | 6.205646 yes | 5.921692 yes | 5.938733 yes | 5.842471 yes | 5.697056 yes | 5.587088 yes | 5.512394 yes |
| 1789380000 | test2 | 4.261041 yes | 4.028678 yes | 3.957987 yes | 4.100852 yes | 4.111894 yes | 4.116831 yes | 4.061312 yes |
| 1789380300 | test2 | 3.563106 yes | 3.614209 yes | 3.485325 yes | 3.625589 yes | 3.546786 yes | 3.456420 yes | 3.401455 yes |
| 1789380600 | test2 | 2.890080 yes | 2.848828 yes | 2.790978 yes | 2.711048 yes | 2.640028 yes | 2.590515 yes | 2.580941 yes |
| 1789380900 | test2 | 2.143915 yes | 2.172896 yes | 2.110784 no | 2.141280 no | 2.087227 no | 2.208852 yes | 2.238309 yes |
| 1789381200 | test2 | 2.312365 yes | 2.271673 yes | 2.246037 yes | 2.475766 yes | 2.474647 yes | 2.485480 yes | 2.460606 yes |
| 1789381500 | test2 | 2.332861 yes | 2.298573 yes | 2.247079 yes | 2.193101 yes | 2.132836 no | 2.096745 no | 2.064427 no |
| 1789381800 | test2 | 1.603527 no | 1.664112 no | 1.789384 no | 1.761651 no | 1.735164 no | 1.709921 no | 1.698475 no |
| 1789382100 | test2 | 1.716162 no | 1.768234 no | 1.706569 no | 1.661096 no | 1.648654 no | 1.608282 no | 1.849864 no |
| 1789382400 | test2 | 1.761693 no | 1.750122 no | 1.651750 no | 2.042214 no | 2.064473 no | 2.034473 no | 2.040396 no |
| 1789382700 | test2 | 2.082880 no | 1.956709 no | 1.992991 no | 1.940905 no | 1.894613 no | 1.865050 no | 1.842254 no |
| 1789383000 | test2 | 1.430716 no | 2.477070 yes | 2.442161 yes | 2.398080 yes | 2.620322 yes | 2.588899 yes | 2.546795 yes |
| 1789383300 | test2 | 3.080809 yes | 2.930669 yes | 2.758247 yes | 2.697774 yes | 2.666866 yes | 2.617419 yes | 2.573260 yes |
| 1789383600 | test2 | 1.927971 no | 2.691355 yes | 2.600153 yes | 2.551075 yes | 2.539164 yes | 2.643970 yes | 2.680409 yes |
| 1789384500 | test2 | 1.659548 no | 1.727205 no | 1.675490 no | 1.637820 no | 1.594031 no | 1.558134 no | 1.536614 no |
| 1789384800 | test2 | 1.639248 no | 1.564794 no | 1.502471 no | 1.469801 no | 1.431815 no | 1.396664 no | 1.381612 no |
| 1789385100 | test2 | 1.294498 no | 1.440606 no | 1.522695 no | 1.483830 no | 1.591382 no | 1.563911 no | 1.541823 no |
| 1789385400 | test2 | 1.980184 no | 1.927986 no | 2.708577 yes | 2.820630 yes | 3.066530 yes | 3.043081 yes | 3.191054 yes |
| 1789385700 | test2 | 3.889503 yes | 3.828772 yes | 3.743630 yes | 3.661110 yes | 3.639667 yes | 3.576774 yes | 3.518861 yes |
| 1789386000 | test2 | 2.809074 yes | 2.685477 yes | 2.566124 yes | 2.557556 yes | 2.502463 yes | 2.456172 yes | 2.419814 yes |
| 1789386300 | test2 | 1.932453 no | 1.822152 no | 1.746957 no | 1.711469 no | 1.669787 no | 1.651722 no | 1.635892 no |
| 1789386600 | test2 | 1.444276 no | 1.384858 no | 1.361010 no | 1.362895 no | 1.494096 no | 1.790155 no | 1.766680 no |
| 1789386900 | test2 | 2.076647 no | 2.163497 yes | 2.146516 no | 2.089045 no | 2.034138 no | 2.145421 no | 2.112426 no |
| 1789387200 | test2 | 1.955854 no | 2.665708 yes | 2.779181 yes | 2.741217 yes | 2.702796 yes | 2.649631 yes | 2.610842 yes |
| 1789387500 | test2 | 3.080078 yes | 3.050310 yes | 2.917741 yes | 3.143997 yes | 3.147991 yes | 3.072291 yes | 3.033269 yes |
| 1789387800 | test2 | 2.838810 yes | 2.641911 yes | 2.478118 yes | 2.455093 yes | 2.431471 yes | 2.419377 yes | 2.407656 yes |
| 1789388100 | test2 | 1.794512 no | 2.441592 yes | 2.448592 yes | 2.387670 yes | 2.346028 yes | 2.468772 yes | 2.462682 yes |
| 1789388400 | test2 | 3.386987 yes | 3.218179 yes | 3.117372 yes | 3.051551 yes | 2.976918 yes | 2.984520 yes | 2.935213 yes |
| 1789388700 | test2 | 2.609371 yes | 2.464198 yes | 2.482328 yes | 2.443326 yes | 2.382107 yes | 2.346271 yes | 2.314370 yes |
| 1789389000 | test2 | 2.024556 no | 2.065734 no | 2.168692 no | 2.164305 yes | 2.110546 no | 2.082534 no | 2.327368 yes |
| 1789389300 | test2 | 4.844565 yes | 5.413190 yes | 5.235081 yes | 5.165586 yes | 5.071095 yes | 4.989504 yes | 4.917905 yes |
| 1789389600 | test2 | 5.916079 yes | 6.224194 yes | 5.935065 yes | 5.868045 yes | 5.784655 yes | 5.652006 yes | 5.560467 yes |
| 1789390500 | test2 | 3.034666 yes | 3.205531 yes | 3.060586 yes | 3.003332 yes | 2.939010 yes | 2.890700 yes | 2.861853 yes |
| 1789390800 | test2 | 3.575392 yes | 3.574683 yes | 3.677216 yes | 3.723028 yes | 4.115201 yes | 4.098608 yes | 4.116139 yes |
| 1789391100 | test2 | 4.649467 yes | 4.820621 yes | 4.649630 yes | 4.749348 yes | 4.699557 yes | 4.669746 yes | 4.661369 yes |
| 1789391400 | test2 | 4.305614 yes | 4.203927 yes | 4.001437 yes | 4.381448 yes | 4.295953 yes | 4.234723 yes | 4.172070 yes |
| 1789391700 | test2 | 3.921935 yes | 4.108228 yes | 4.012834 yes | 3.928743 yes | 3.929915 yes | 3.984473 yes | 3.954340 yes |
| 1789392000 | test2 | 3.803959 yes | 3.728475 yes | 3.526998 yes | 3.433915 yes | 3.342816 yes | 3.330463 yes | 3.290123 yes |
| 1789392300 | test2 | 2.477341 yes | 2.548155 yes | 2.493626 yes | 2.583845 yes | 2.568096 yes | 2.522772 yes | 2.487500 yes |
| 1789392600 | test2 | 4.718764 yes | 5.966434 yes | 6.721199 yes | 6.683809 yes | 6.557695 yes | 6.459435 yes | 6.456851 yes |
| 1789392900 | test2 | 8.917945 yes | 9.634853 yes | 9.730780 yes | 9.759316 yes | 9.713289 yes | 9.597261 yes | 9.545377 yes |
| 1789393200 | test2 | 9.396646 yes | 9.056192 yes | 8.728773 yes | 8.622848 yes | 8.484039 yes | 8.395325 yes | 8.398277 yes |
| 1789393500 | test2 | 6.370871 yes | 6.308695 yes | 6.229666 yes | 6.103466 yes | 6.014910 yes | 5.920623 yes | 6.002840 yes |
| 1789394400 | test2 | 6.559916 yes | 6.241140 yes | 6.222661 yes | 6.256714 yes | 6.178872 yes | 6.116021 yes | 6.274672 yes |
| 1789394700 | test2 | 6.520904 yes | 6.328240 yes | 6.133127 yes | 6.093977 yes | 5.975896 yes | 5.888262 yes | 5.813808 yes |
| 1789395000 | test2 | 5.237389 yes | 5.281717 yes | 5.139562 yes | 5.115494 yes | 5.041083 yes | 5.025386 yes | 4.989730 yes |
| 1789395300 | test2 | 4.686900 yes | 4.397070 yes | 4.408754 yes | 4.446697 yes | 4.675186 yes | 4.787282 yes | 4.753127 yes |
| 1789395600 | test2 | 4.734019 yes | 4.916232 yes | 5.008361 yes | 5.049498 yes | 5.107092 yes | 5.066560 yes | 5.070954 yes |
| 1789395900 | test2 | 5.231214 yes | 5.345456 yes | 5.327820 yes | 5.258415 yes | 5.220171 yes | 5.225067 yes | 5.231784 yes |
| 1789396200 | test2 | 5.693088 yes | 6.385844 yes | 6.386447 yes | 6.359166 yes | 6.340786 yes | 6.396788 yes | 6.417505 yes |
| 1789396500 | test2 | 7.153663 yes | 6.749873 yes | 6.442901 yes | 6.314112 yes | 6.212917 yes | 6.106185 yes | 6.115993 yes |
| 1789396800 | test2 | 4.261233 yes | 4.315360 yes | 4.170508 yes | 4.140564 yes | 4.133182 yes | 4.058472 yes | 4.097272 yes |
| 1789397100 | test2 | 4.366428 yes | 4.351957 yes | 4.244934 yes | 4.220178 yes | 4.144620 yes | 4.342881 yes | 4.336992 yes |
| 1789397400 | test2 | 4.616697 yes | 4.510985 yes | 4.655514 yes | 4.669250 yes | 4.578090 yes | 4.514311 yes | 4.970996 yes |
| 1789397700 | test2 | 5.197585 yes | 5.002639 yes | 4.764187 yes | 4.661855 yes | 4.935897 yes | 4.977527 yes | 4.923971 yes |
| 1789398000 | test2 | 4.846976 yes | 5.286351 yes | 5.262268 yes | 5.198740 yes | 5.155453 yes | 5.148792 yes | 5.154525 yes |
| 1789398300 | test2 | 6.974850 yes | 6.893268 yes | 6.695832 yes | 6.571307 yes | 6.573104 yes | 6.466834 yes | 6.529517 yes |
| 1789398600 | test2 | 6.903243 yes | 6.641055 yes | 6.401272 yes | 6.252934 yes | 6.084873 yes | 5.953245 yes | 5.864146 yes |
| 1789398900 | test2 | 3.502139 yes | 3.538537 yes | 3.882394 yes | 3.880362 yes | 3.868817 yes | 3.981813 yes | 3.932071 yes |
| 1789399200 | test2 | 4.193920 yes | 4.137638 yes | 4.057279 yes | 4.037450 yes | 3.937351 yes | 3.973602 yes | 4.111680 yes |
| 1789399500 | test2 | 4.243510 yes | 4.153179 yes | 4.009561 yes | 3.964190 yes | 3.873104 yes | 3.846698 yes | 3.786347 yes |
| 1789399800 | test2 | 3.538679 yes | 3.531578 yes | 4.440499 yes | 4.493635 yes | 4.540122 yes | 4.440033 yes | 4.381860 yes |
| 1789400100 | test2 | 5.419194 yes | 5.253476 yes | 5.527216 yes | 5.439593 yes | 5.432399 yes | 5.394031 yes | 5.416537 yes |
| 1789400400 | test2 | 5.732380 yes | 5.568257 yes | 5.494406 yes | 5.402540 yes | 5.259729 yes | 5.163630 yes | 5.121529 yes |
| 1789400700 | test2 | 4.989401 yes | 4.781424 yes | 4.568177 yes | 4.461032 yes | 4.741096 yes | 4.946992 yes | 5.063951 yes |
| 1789401600 | test2 | 3.626441 yes | 3.483034 yes | 3.318096 yes | 3.246481 yes | 3.162186 yes | 3.127246 yes | 3.169041 yes |
| 1789401900 | test2 | 2.651567 yes | 2.644608 yes | 2.756658 yes | 2.703880 yes | 2.650106 yes | 2.595210 yes | 2.579103 yes |
| 1789402200 | test2 | 2.633088 yes | 2.613788 yes | 2.506940 yes | 2.443891 yes | 2.459370 yes | 2.441415 yes | 2.427682 yes |
| 1789402500 | test2 | 2.501845 yes | 2.656982 yes | 3.036263 yes | 4.071545 yes | 4.145592 yes | 4.817095 yes | 4.903607 yes |
| 1789402800 | test2 | 6.571972 yes | 6.324322 yes | 6.177461 yes | 6.001576 yes | 5.872326 yes | 5.824591 yes | 5.735605 yes |
| 1789403100 | test2 | 4.714477 yes | 4.603262 yes | 4.624670 yes | 4.597832 yes | 4.584985 yes | 4.489249 yes | 4.454352 yes |
| 1789403400 | test2 | 4.006609 yes | 4.226597 yes | 4.195212 yes | 4.119680 yes | 4.029297 yes | 3.932890 yes | 3.866267 yes |
| 1789403700 | test2 | 3.394142 yes | 3.249569 yes | 3.369219 yes | 3.320686 yes | 3.343768 yes | 3.299834 yes | 3.367370 yes |
| 1789404000 | test2 | 3.092634 yes | 2.995217 yes | 2.868107 yes | 2.795192 yes | 2.731320 yes | 2.675878 yes | 2.637355 yes |
| 1789404300 | test2 | 2.202446 yes | 2.176668 yes | 3.215906 yes | 3.579796 yes | 3.576863 yes | 3.510573 yes | 3.475297 yes |
| 1789404600 | test2 | 4.258167 yes | 4.008522 yes | 4.058404 yes | 4.019351 yes | 3.967609 yes | 4.132800 yes | 4.122613 yes |
| 1789404900 | test2 | 3.824731 yes | 3.801222 yes | 3.717647 yes | 3.629935 yes | 3.563618 yes | 3.499954 yes | 3.449366 yes |
| 1789405200 | test2 | 3.026203 yes | 2.914149 yes | 3.031808 yes | 2.988457 yes | 2.968720 yes | 2.900507 yes | 2.864468 yes |
| 1789405500 | test2 | 2.471996 yes | 3.559792 yes | 3.454762 yes | 3.426982 yes | 3.394407 yes | 3.308261 yes | 3.294437 yes |
| 1789405800 | test2 | 3.646886 yes | 3.477966 yes | 3.364196 yes | 3.284187 yes | 3.253983 yes | 3.179942 yes | 3.142284 yes |
| 1789406100 | test2 | 2.063215 no | 2.152404 yes | 2.145487 no | 2.645631 yes | 2.610816 yes | 2.623224 yes | 2.599856 yes |
| 1789406400 | test2 | 2.896214 yes | 3.077215 yes | 3.092544 yes | 3.117906 yes | 3.365866 yes | 3.361118 yes | 3.372134 yes |
| 1789406700 | test2 | 3.747660 yes | 3.946870 yes | 3.940467 yes | 3.896108 yes | 3.828960 yes | 3.826450 yes | 3.776243 yes |
| 1789407000 | test2 | 3.750842 yes | 3.732229 yes | 3.585760 yes | 3.588402 yes | 3.673507 yes | 3.594298 yes | 3.541366 yes |
| 1789407300 | test2 | 3.666048 yes | 3.504249 yes | 3.458696 yes | 3.492811 yes | 3.405530 yes | 3.400695 yes | 3.370665 yes |
| 1789407600 | test2 | 3.336458 yes | 3.240988 yes | 3.306394 yes | 3.215602 yes | 3.193152 yes | 3.120939 yes | 3.090212 yes |
| 1789407900 | test2 | 2.480142 yes | 2.560704 yes | 2.661290 yes | 2.817188 yes | 2.797781 yes | 2.839257 yes | 2.815565 yes |
| 1789408800 | test2 | 3.246129 yes | 3.216847 yes | 3.094939 yes | 3.107305 yes | 3.538135 yes | 3.531694 yes | 3.515221 yes |
| 1789409100 | test2 | 3.711937 yes | 3.625274 yes | 3.484361 yes | 3.400332 yes | 3.382075 yes | 3.314064 yes | 3.470994 yes |
| 1789409400 | test2 | 2.944811 yes | 3.047339 yes | 2.892193 yes | 2.841140 yes | 2.771540 yes | 2.741078 yes | 2.723890 yes |
| 1789409700 | test2 | 3.107146 yes | 3.126668 yes | 3.018395 yes | 3.058797 yes | 3.797731 yes | 3.948236 yes | 4.004093 yes |
| 1789410000 | test2 | 5.809774 yes | 5.652286 yes | 5.638926 yes | 5.629089 yes | 5.817674 yes | 6.025089 yes | 6.069486 yes |
| 1789410300 | test2 | 6.868814 yes | 6.427168 yes | 6.133279 yes | 6.021769 yes | 5.856354 yes | 5.747530 yes | 5.713552 yes |
| 1789410600 | test2 | 4.037906 yes | 3.910592 yes | 3.750962 yes | 3.714948 yes | 3.652505 yes | 3.617360 yes | 3.580631 yes |
| 1789410900 | test2 | 2.936203 yes | 3.362336 yes | 3.308947 yes | 3.226184 yes | 3.168678 yes | 3.097969 yes | 3.052178 yes |
| 1789411200 | test2 | 3.341004 yes | 3.279679 yes | 4.223262 yes | 4.486103 yes | 4.471041 yes | 4.594538 yes | 4.569191 yes |
| 1789411500 | test2 | 5.508112 yes | 5.576513 yes | 5.324913 yes | 5.489835 yes | 5.394147 yes | 5.353491 yes | 5.269022 yes |
| 1789411800 | test2 | 4.819720 yes | 4.795244 yes | 4.600946 yes | 4.518621 yes | 4.447868 yes | 4.376605 yes | 4.328911 yes |
| 1789412700 | test2 | 3.985349 yes | 3.806321 yes | 4.079198 yes | 4.040490 yes | 3.972952 yes | 3.890636 yes | 3.832599 yes |
| 1789413000 | test2 | 3.482586 yes | 3.380394 yes | 3.261657 yes | 3.216980 yes | 3.206602 yes | 3.158055 yes | 3.135136 yes |
| 1789413300 | test2 | 3.350969 yes | 3.260971 yes | 3.263672 yes | 3.240263 yes | 3.193604 yes | 3.205462 yes | 3.173606 yes |
| 1789413600 | test2 | 3.253791 yes | 3.087807 yes | 2.928023 yes | 2.874976 yes | 2.844847 yes | 2.783572 yes | 2.763855 yes |
| 1789413900 | test2 | 2.469037 yes | 2.352752 yes | 2.909851 yes | 2.853157 yes | 2.851459 yes | 2.792596 yes | 2.758994 yes |
| 1789414200 | test2 | 3.368183 yes | 4.565294 yes | 4.428863 yes | 4.384100 yes | 4.287882 yes | 4.527502 yes | 4.502406 yes |
| 1789414500 | test2 | 4.909203 yes | 4.763644 yes | 4.499575 yes | 4.395773 yes | 4.445608 yes | 4.343970 yes | 4.273735 yes |
| 1789414800 | test2 | 3.080326 yes | 2.984739 yes | 2.887269 yes | 2.841423 yes | 2.808734 yes | 2.784809 yes | 2.782421 yes |
| 1789415100 | test2 | 2.708002 yes | 2.693589 yes | 2.632067 yes | 2.854884 yes | 2.856283 yes | 2.852629 yes | 2.815872 yes |
| 1789415400 | test2 | 2.733076 yes | 2.635539 yes | 2.547857 yes | 2.509295 yes | 2.485733 yes | 2.451167 yes | 2.418298 yes |
| 1789415700 | test2 | 2.231439 yes | 2.244832 yes | 2.176644 no | 2.133477 no | 2.134561 no | 2.141764 no | 2.127359 no |
| 1789416600 | test2 | 1.914858 no | 1.968344 no | 3.242533 yes | 3.505764 yes | 3.649494 yes | 3.597528 yes | 3.600193 yes |
| 1789416900 | test2 | 4.639374 yes | 4.786593 yes | 4.830963 yes | 4.846323 yes | 5.015298 yes | 5.112568 yes | 5.074637 yes |
| 1789417200 | test2 | 5.157237 yes | 4.955264 yes | 4.822264 yes | 4.866662 yes | 5.446180 yes | 5.536430 yes | 5.551434 yes |
| 1789417500 | test2 | 5.689691 yes | 5.743066 yes | 5.755106 yes | 5.593276 yes | 5.492845 yes | 5.377573 yes | 5.412637 yes |
| 1789417800 | test2 | 4.900553 yes | 4.643992 yes | 4.581497 yes | 4.513692 yes | 4.435736 yes | 4.392487 yes | 5.001786 yes |
| 1789418100 | test2 | 5.421420 yes | 5.193514 yes | 4.946985 yes | 4.830767 yes | 4.700325 yes | 4.586128 yes | 4.514787 yes |
| 1789418400 | test2 | 3.235819 yes | 3.050039 yes | 2.976448 yes | 2.918982 yes | 2.861710 yes | 2.827907 yes | 2.800135 yes |
| 1789418700 | test2 | 1.952911 no | 2.372888 yes | 2.298651 yes | 2.335416 yes | 2.280980 yes | 2.274448 yes | 2.278707 yes |
| 1789419000 | test2 | 2.626899 yes | 2.546312 yes | 2.467643 yes | 2.521198 yes | 2.546483 yes | 2.533766 yes | 2.507852 yes |
| 1789419300 | test2 | 2.433520 yes | 2.600460 yes | 2.615825 yes | 2.698328 yes | 2.650938 yes | 2.660948 yes | 2.619967 yes |
| 1789419600 | test2 | 2.910832 yes | 3.399332 yes | 6.177327 yes | 6.473941 yes | 6.368819 yes | 6.559653 yes | 6.462797 yes |
| 1789419900 | test2 | 7.973058 yes | 7.725758 yes | 7.386641 yes | 7.177131 yes | 6.985304 yes | 6.813288 yes | 6.722396 yes |
| 1789420200 | test2 | 4.030702 yes | 4.377906 yes | 4.224129 yes | 4.106564 yes | 3.996905 yes | 3.930528 yes | 3.935057 yes |
| 1789420500 | test2 | 3.777008 yes | 3.566493 yes | 3.638677 yes | 3.585215 yes | 3.930542 yes | 4.021743 yes | 4.013189 yes |
| 1789420800 | test2 | 4.096015 yes | 3.999451 yes | 3.784787 yes | 3.711654 yes | 3.618934 yes | 3.536889 yes | 3.478132 yes |
| 1789421100 | test2 | 2.896050 yes | 3.183173 yes | 3.108880 yes | 3.058046 yes | 2.977112 yes | 2.971486 yes | 3.378647 yes |
| 1789421400 | test2 | 3.682570 yes | 3.462009 yes | 3.385233 yes | 3.382908 yes | 3.394633 yes | 3.391890 yes | 3.341139 yes |
| 1789421700 | test2 | 3.225642 yes | 3.437258 yes | 3.479453 yes | 3.578775 yes | 3.526918 yes | 3.468270 yes | 3.451617 yes |
| 1789422000 | test2 | 3.993539 yes | 3.835192 yes | 3.694746 yes | 3.615135 yes | 3.571617 yes | 3.598950 yes | 3.591881 yes |
| 1789422600 | test2 | 2.472654 yes | 2.350924 yes | 2.240256 yes | 2.212037 yes | 2.179782 yes | 2.122110 no | 2.120708 no |
| 1789422900 | test2 | 1.340174 no | 1.540301 no | 1.446207 no | 1.448359 no | 1.415387 no | 1.454637 no | 1.478850 no |
| 1789423200 | test2 | 1.988785 no | 2.172663 yes | 2.204167 yes | 2.389355 yes | 2.347389 yes | 2.413160 yes | 2.405069 yes |
| 1789423500 | test2 | 3.173840 yes | 3.026681 yes | 3.093587 yes | 3.032176 yes | 3.082990 yes | 3.008780 yes | 3.035637 yes |
| 1789423800 | test2 | 3.499801 yes | 3.405009 yes | 3.271585 yes | 3.265904 yes | 3.289329 yes | 3.234959 yes | 3.180154 yes |
| 1789424100 | test2 | 3.111516 yes | 2.966978 yes | 2.923640 yes | 2.961450 yes | 2.895904 yes | 2.840640 yes | 3.182707 yes |
| 1789424400 | test2 | 2.824153 yes | 2.767712 yes | 2.733852 yes | 2.670340 yes | 2.648498 yes | 2.609747 yes | 2.567783 yes |
| 1789424700 | test2 | 2.956270 yes | 2.801187 yes | 2.823168 yes | 2.951131 yes | 2.904033 yes | 2.871390 yes | 3.128432 yes |
| 1789425000 | test2 | 3.610563 yes | 3.974703 yes | 3.929969 yes | 3.815430 yes | 3.856652 yes | 3.792679 yes | 3.820060 yes |
| 1789425900 | test2 | 2.343611 yes | 2.430962 yes | 2.507506 yes | 2.461478 yes | 2.608391 yes | 2.666221 yes | 2.628376 yes |
| 1789426200 | test2 | 2.578261 yes | 2.420974 yes | 2.432305 yes | 2.363618 yes | 2.299914 yes | 2.258852 yes | 2.221161 yes |
| 1789426500 | test2 | 1.391869 no | 1.373158 no | 1.320452 no | 1.287647 no | 1.253145 no | 1.224983 no | 1.205733 no |
| 1789426800 | test2 | 1.535101 no | 1.671762 no | 1.647482 no | 1.993133 no | 1.992803 no | 1.970737 no | 1.952321 no |
| 1789427100 | test2 | 2.516846 yes | 3.407028 yes | 3.363747 yes | 3.272322 yes | 3.187420 yes | 3.117088 yes | 3.070673 yes |
| 1789427400 | test2 | 3.185204 yes | 3.161598 yes | 2.961632 yes | 2.879924 yes | 2.804357 yes | 2.742499 yes | 2.695730 yes |
| 1789427700 | test2 | 2.087800 no | 2.076201 no | 2.106209 no | 2.048457 no | 2.084726 no | 2.129511 no | 2.135191 no |

### V12 — influence — recorded, not asserted

- **Item 1.** Every one of the 28 Student `λ̂` in §1.4 carries its value recomputed without its
  single most influential observation. That observation is named by `T0`, label and `z`.
  - Influence is the observation's own contribution to `ll(λ̂) − ll(1)`.
  - Each recomputation is an exact refit by the same committed search.
- **Item 2.** Every admissible population's `ν̂` carries one exact refit without its
  largest-magnitude contributing member. That is 21 refits, in §1.3.
- Both are recorded, not asserted. Neither moves a gate.

---

## 5. Publication

- **Branch.** `tz-11a-student-link`, one commit, `274651805c765bb977c635d75fd1ebdb2c8f550a`, four files, pushed to `origin`.
  After the push, `git ls-remote origin tz-11a-student-link` printed:

  ```
  274651805c765bb977c635d75fd1ebdb2c8f550a	refs/heads/tz-11a-student-link
  ```

- **Pull request.** https://github.com/seahomebatumi-ai/btc-5m-twap/pull/12, opened with `gh pr create` against `main`. **It is not merged:**
  merge is the Boss's, after the Architect's verdict.
- **No Release.** No dataset, archive or binary entered git history, and the third command below
  prints nothing.
- **This report** is the only path the run adds to `main`, in one commit.

**The separation self-check of contract §4.2, verbatim.** It was run after the branch was pushed
and before this report was committed. `/root/tz11a-work/separation.py` runs the three commands as
the contract writes them and asserts each result:

- the first prints `0`;
- the second lists the four implementation files and nothing else;
- the third prints nothing.

```
$ git rev-list origin/main | grep -c 274651805c765bb977c635d75fd1ebdb2c8f550a
0
$ git diff --name-only origin/main origin/tz-11a-student-link
research/pfair.py
research/selftest-pfair.py
research/tz07a-variance-time.py
research/tz11a-student-link.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
```

**§9, first: every file a committed report names by SHA-256, preserved before anything was
reclaimed.** `/root/tz11a-work/copy-forensics.py` read every 64-hex-digit string in the 20
reports on `main` and hashed every file under `/root/tz10b-work` and `/root/tz11-work`. It then
copied each file whose hash a report names, and which `/root/btc-forensics/` did not already hold,
by exclusive create (`open(..., "xb")`). It asserts each hash at both ends and asserts that every
file already in `/root/btc-forensics/` is unchanged.

| source | destination in `/root/btc-forensics/` | bytes | SHA-256 at the source | SHA-256 at the destination | named by |
|---|---|---|---|---|---|
| `/root/tz10b-work/tz10b-observations.csv` | `tz10b-work--tz10b-observations.csv` | 5,553,429 | `142ea46b765bbdb1796f0da03b198755ac7904aacb748e91419db0a8b423eacd` | `142ea46b765bbdb1796f0da03b198755ac7904aacb748e91419db0a8b423eacd` | TZ-10b-sigma-or-link-report.md, TZ-11-student-link-and-domain-report.md |
| `/root/tz10b-work/run-1/tz10b-observations.csv` | `tz10b-work--run-1--tz10b-observations.csv` | 5,553,429 | `142ea46b765bbdb1796f0da03b198755ac7904aacb748e91419db0a8b423eacd` | `142ea46b765bbdb1796f0da03b198755ac7904aacb748e91419db0a8b423eacd` | TZ-10b-sigma-or-link-report.md, TZ-11-student-link-and-domain-report.md |
| `/root/tz10b-work/run-1/tz10b-results.json` | `tz10b-work--run-1--tz10b-results.json` | 332,640 | `994297738a539d67417911cd32f713f05892e36d443a8139ad4e844d50d1383d` | `994297738a539d67417911cd32f713f05892e36d443a8139ad4e844d50d1383d` | TZ-10b-sigma-or-link-report.md, TZ-11-student-link-and-domain-report.md |
| `/root/tz10b-work/run-1/tz10b-tables.md` | `tz10b-work--run-1--tz10b-tables.md` | 119,347 | `4dc3bfa41dee5dfd89ab2bd3345c28d43e314b9fefa77d4e2f5528d43236d39f` | `4dc3bfa41dee5dfd89ab2bd3345c28d43e314b9fefa77d4e2f5528d43236d39f` | TZ-10b-sigma-or-link-report.md, TZ-11-student-link-and-domain-report.md |
| `/root/tz10b-work/run-2/tz10b-observations.csv` | `tz10b-work--run-2--tz10b-observations.csv` | 5,553,429 | `142ea46b765bbdb1796f0da03b198755ac7904aacb748e91419db0a8b423eacd` | `142ea46b765bbdb1796f0da03b198755ac7904aacb748e91419db0a8b423eacd` | TZ-10b-sigma-or-link-report.md, TZ-11-student-link-and-domain-report.md |
| `/root/tz10b-work/run-2/tz10b-results.json` | `tz10b-work--run-2--tz10b-results.json` | 332,640 | `994297738a539d67417911cd32f713f05892e36d443a8139ad4e844d50d1383d` | `994297738a539d67417911cd32f713f05892e36d443a8139ad4e844d50d1383d` | TZ-10b-sigma-or-link-report.md, TZ-11-student-link-and-domain-report.md |
| `/root/tz10b-work/run-2/tz10b-tables.md` | `tz10b-work--run-2--tz10b-tables.md` | 119,347 | `4dc3bfa41dee5dfd89ab2bd3345c28d43e314b9fefa77d4e2f5528d43236d39f` | `4dc3bfa41dee5dfd89ab2bd3345c28d43e314b9fefa77d4e2f5528d43236d39f` | TZ-10b-sigma-or-link-report.md, TZ-11-student-link-and-domain-report.md |
| `/root/tz10b-work/wt/.git` | `tz10b-work--wt--.git` | 44 | `8680f8c0eb69788a3f13a78de76ab8794fd8d70835e8c722beb93ee7fc11f6f4` | `8680f8c0eb69788a3f13a78de76ab8794fd8d70835e8c722beb93ee7fc11f6f4` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/SYSTEM-MAP.md` | `tz10b-work--wt--SYSTEM-MAP.md` | 64,249 | `b3e9fdb585cf00bfeba0be11337d0b374b9cbd676ae353a7bf9f130b6e502f19` | `b3e9fdb585cf00bfeba0be11337d0b374b9cbd676ae353a7bf9f130b6e502f19` | TZ-10b-sigma-or-link-report.md |
| `/root/tz10b-work/wt/CryptoReports/TZ-01-twap-divergence-report.md` | `tz10b-work--wt--CryptoReports--TZ-01-twap-divergence-report.md` | 56,532 | `6077fb6a0fb62d5803e70ee5d6f0b8bc8332d756da0af637606eca99bf44f65b` | `6077fb6a0fb62d5803e70ee5d6f0b8bc8332d756da0af637606eca99bf44f65b` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/CryptoReports/TZ-01a-twap-divergence-corrected-report.md` | `tz10b-work--wt--CryptoReports--TZ-01a-twap-divergence-corrected-report.md` | 59,427 | `bc655c569ec10dffcf817f9dc6373575749b3f147441af640c7738ec5feb47bc` | `bc655c569ec10dffcf817f9dc6373575749b3f147441af640c7738ec5feb47bc` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/CryptoReports/TZ-02-divergence-distribution-report.md` | `tz10b-work--wt--CryptoReports--TZ-02-divergence-distribution-report.md` | 66,803 | `c7db53c035d389f05a784ba4c9b398a417c9aa7614112ac0d1afa842ccdedef2` | `c7db53c035d389f05a784ba4c9b398a417c9aa7614112ac0d1afa842ccdedef2` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/CryptoReports/TZ-03-repo-hygiene-report.md` | `tz10b-work--wt--CryptoReports--TZ-03-repo-hygiene-report.md` | 14,910 | `e14cdd5067ed53bfbb4bef6de150331fbcb1ef259793953f165d25ee11a4d397` | `e14cdd5067ed53bfbb4bef6de150331fbcb1ef259793953f165d25ee11a4d397` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/CryptoReports/TZ-04-market-recorder-report.md` | `tz10b-work--wt--CryptoReports--TZ-04-market-recorder-report.md` | 7,573 | `237116cc437dd9216927cf175a0c66921cff2296385bb4b4914cd8d3be74cf51` | `237116cc437dd9216927cf175a0c66921cff2296385bb4b4914cd8d3be74cf51` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/CryptoReports/TZ-04a-market-recorder-corrected-report.md` | `tz10b-work--wt--CryptoReports--TZ-04a-market-recorder-corrected-report.md` | 9,868 | `975843f66a9c0d563c165e681b69482fbefbf8aca880bdd9f87216997e63292c` | `975843f66a9c0d563c165e681b69482fbefbf8aca880bdd9f87216997e63292c` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/CryptoReports/TZ-04b-market-recorder-scoring-report.md` | `tz10b-work--wt--CryptoReports--TZ-04b-market-recorder-scoring-report.md` | 68,352 | `a18ffd566085cea8f10feba139fadda0f1592f38adddde7e008792c46e8a8e9c` | `a18ffd566085cea8f10feba139fadda0f1592f38adddde7e008792c46e8a8e9c` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/CryptoReports/TZ-05-quote-capture-report.md` | `tz10b-work--wt--CryptoReports--TZ-05-quote-capture-report.md` | 12,343 | `ec548d0e1a4b9bf09695d079b7513428b022460a2b411f9c8ee54f4698778daf` | `ec548d0e1a4b9bf09695d079b7513428b022460a2b411f9c8ee54f4698778daf` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/CryptoReports/TZ-05a-quote-capture-deploy-report.md` | `tz10b-work--wt--CryptoReports--TZ-05a-quote-capture-deploy-report.md` | 26,565 | `cddca348120ae278f3c399ea21353f57e8b3722f3b0372e247cc985ab1351805` | `cddca348120ae278f3c399ea21353f57e8b3722f3b0372e247cc985ab1351805` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/CryptoReports/TZ-06-pfair-calibration-report.md` | `tz10b-work--wt--CryptoReports--TZ-06-pfair-calibration-report.md` | 60,833 | `33863ce6d62443dd070646854b135438ee624c96b5204cd9851cfbca9939396f` | `33863ce6d62443dd070646854b135438ee624c96b5204cd9851cfbca9939396f` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/CryptoReports/TZ-07-variance-time-report.md` | `tz10b-work--wt--CryptoReports--TZ-07-variance-time-report.md` | 11,745 | `4056137f8de8ef6fa39e43a348a1f60bdfee10f7ffe2c29ebb6e4f6e7894c5b4` | `4056137f8de8ef6fa39e43a348a1f60bdfee10f7ffe2c29ebb6e4f6e7894c5b4` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/CryptoReports/TZ-07a-variance-time-report.md` | `tz10b-work--wt--CryptoReports--TZ-07a-variance-time-report.md` | 38,555 | `15c26ec8b7ac670bb136177fd3a87dcd56935077714feff48f833dd08b3af72b` | `15c26ec8b7ac670bb136177fd3a87dcd56935077714feff48f833dd08b3af72b` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/CryptoReports/TZ-07b-settlement-dispersion-report.md` | `tz10b-work--wt--CryptoReports--TZ-07b-settlement-dispersion-report.md` | 27,788 | `44b2ee1a80c80867aa17bf6b0c378fccbf203655dfc39a7f323861aab4d7cf80` | `44b2ee1a80c80867aa17bf6b0c378fccbf203655dfc39a7f323861aab4d7cf80` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/CryptoReports/TZ-08-out-of-sample-report.md` | `tz10b-work--wt--CryptoReports--TZ-08-out-of-sample-report.md` | 18,738 | `b0d0c8ed31c28bfa52dc449da4a06d33318f17221a6f9d94ce9bcc8f7ecccffe` | `b0d0c8ed31c28bfa52dc449da4a06d33318f17221a6f9d94ce9bcc8f7ecccffe` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/CryptoReports/TZ-08a-out-of-sample-report.md` | `tz10b-work--wt--CryptoReports--TZ-08a-out-of-sample-report.md` | 77,715 | `86d4ba81e196ace179c65067a3620bb77dba20019f428ecd1c6e588bde6c1188` | `86d4ba81e196ace179c65067a3620bb77dba20019f428ecd1c6e588bde6c1188` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/CryptoTZ/TZ-01-twap-divergence.md` | `tz10b-work--wt--CryptoTZ--TZ-01-twap-divergence.md` | 10,121 | `455f58e0616daeacfb67ee7302d84520826780720b5c56c7e7a06463ec63dd57` | `455f58e0616daeacfb67ee7302d84520826780720b5c56c7e7a06463ec63dd57` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/CryptoTZ/TZ-01a-twap-divergence-corrected.md` | `tz10b-work--wt--CryptoTZ--TZ-01a-twap-divergence-corrected.md` | 8,118 | `a8c4c7c22881236903797e2ffc2d8c87d6e9fc74cd282c7e40feb9eaecab65e3` | `a8c4c7c22881236903797e2ffc2d8c87d6e9fc74cd282c7e40feb9eaecab65e3` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/CryptoTZ/TZ-02-divergence-distribution.md` | `tz10b-work--wt--CryptoTZ--TZ-02-divergence-distribution.md` | 7,208 | `c8abadec3bb4763a383f397f8ef188cda4228ed1d356f635f8674456d586f2a3` | `c8abadec3bb4763a383f397f8ef188cda4228ed1d356f635f8674456d586f2a3` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/CryptoTZ/TZ-03-repo-hygiene.md` | `tz10b-work--wt--CryptoTZ--TZ-03-repo-hygiene.md` | 4,657 | `0cd150f54862e6c640510acba90c36f1c351e97d0e9b068a573822455668d56e` | `0cd150f54862e6c640510acba90c36f1c351e97d0e9b068a573822455668d56e` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/CryptoTZ/TZ-04-market-recorder.md` | `tz10b-work--wt--CryptoTZ--TZ-04-market-recorder.md` | 10,008 | `95b2fd8d752a759f7b274aa0fc8ca62b54d9d27d84bc91cc33cc1014c518fe09` | `95b2fd8d752a759f7b274aa0fc8ca62b54d9d27d84bc91cc33cc1014c518fe09` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/CryptoTZ/TZ-04a-market-recorder-corrected.md` | `tz10b-work--wt--CryptoTZ--TZ-04a-market-recorder-corrected.md` | 12,445 | `fff99e417a5117ab9e5186e793adea8bec9be9140864776a84ef0f7c1f20988b` | `fff99e417a5117ab9e5186e793adea8bec9be9140864776a84ef0f7c1f20988b` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/CryptoTZ/TZ-04b-market-recorder-scoring.md` | `tz10b-work--wt--CryptoTZ--TZ-04b-market-recorder-scoring.md` | 15,466 | `f4ab08b6a58f84401d38124ff54a665aaa0808a0fb3b376a1362fcb63960effc` | `f4ab08b6a58f84401d38124ff54a665aaa0808a0fb3b376a1362fcb63960effc` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/CryptoTZ/TZ-05-quote-capture.md` | `tz10b-work--wt--CryptoTZ--TZ-05-quote-capture.md` | 8,506 | `4b9a41fb3301712e6629fb565c47e50a38cb3c85e605122394797ed9094285fe` | `4b9a41fb3301712e6629fb565c47e50a38cb3c85e605122394797ed9094285fe` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/CryptoTZ/TZ-05a-quote-capture-deploy.md` | `tz10b-work--wt--CryptoTZ--TZ-05a-quote-capture-deploy.md` | 10,876 | `16f4821308e0f931a469acd0c7d1facffc4c3bb6c75bcd266305d1acc241410b` | `16f4821308e0f931a469acd0c7d1facffc4c3bb6c75bcd266305d1acc241410b` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/CryptoTZ/TZ-06-pfair-calibration.md` | `tz10b-work--wt--CryptoTZ--TZ-06-pfair-calibration.md` | 14,400 | `ec2135c810be9e736946c004b7a4ced0d5a00a322061c89a1519f2d4a30f8373` | `ec2135c810be9e736946c004b7a4ced0d5a00a322061c89a1519f2d4a30f8373` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/CryptoTZ/TZ-07-variance-time.md` | `tz10b-work--wt--CryptoTZ--TZ-07-variance-time.md` | 11,924 | `759d8ed001ed6746a6b7badd430fa1b3b362849594429849cf196bd892342e2b` | `759d8ed001ed6746a6b7badd430fa1b3b362849594429849cf196bd892342e2b` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/CryptoTZ/TZ-07b-settlement-dispersion.md` | `tz10b-work--wt--CryptoTZ--TZ-07b-settlement-dispersion.md` | 15,032 | `476344ccf393c8e3f3eb7a70e97f71af7433a45a02af069978b2e8138c155541` | `476344ccf393c8e3f3eb7a70e97f71af7433a45a02af069978b2e8138c155541` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/CryptoTZ/TZ-09-disk-inventory.md` | `tz10b-work--wt--CryptoTZ--TZ-09-disk-inventory.md` | 12,139 | `db811fea3dea51b58c4a7894cb9666e60b6fcb5b2e86073ba7c89cc9c6fe09e1` | `db811fea3dea51b58c4a7894cb9666e60b6fcb5b2e86073ba7c89cc9c6fe09e1` | TZ-09-disk-inventory-report.md |
| `/root/tz10b-work/wt/CryptoTZ/TZ-10-sigma-or-link.md` | `tz10b-work--wt--CryptoTZ--TZ-10-sigma-or-link.md` | 17,794 | `c08bea39dd3582d4ce8373ee5dabbe1d06357722fedad5c9f97e92f65ab4054a` | `c08bea39dd3582d4ce8373ee5dabbe1d06357722fedad5c9f97e92f65ab4054a` | TZ-10-sigma-or-link-report.md |
| `/root/tz10b-work/wt/CryptoTZ/TZ-10a-sigma-or-link.md` | `tz10b-work--wt--CryptoTZ--TZ-10a-sigma-or-link.md` | 22,088 | `2688836d8e4dd981d7e9bef324d81844b4be6884e2d1d5b4c103f65db6b5e403` | `2688836d8e4dd981d7e9bef324d81844b4be6884e2d1d5b4c103f65db6b5e403` | TZ-10a-sigma-or-link-report.md |
| `/root/tz10b-work/wt/CryptoTZ/TZ-10b-sigma-or-link.md` | `tz10b-work--wt--CryptoTZ--TZ-10b-sigma-or-link.md` | 26,443 | `8705ca3783784511f8a4f33b23a1664566fb2bda7159d860295a522aadafe49b` | `8705ca3783784511f8a4f33b23a1664566fb2bda7159d860295a522aadafe49b` | TZ-10b-sigma-or-link-report.md |
| `/root/tz10b-work/wt/research/pfair.py` | `tz10b-work--wt--research--pfair.py` | 13,985 | `45b307b221d410a7812759a89941dc7645dfda165a8e01a60aef5b17851a5d1e` | `45b307b221d410a7812759a89941dc7645dfda165a8e01a60aef5b17851a5d1e` | TZ-10b-sigma-or-link-report.md, TZ-11-student-link-and-domain-report.md |
| `/root/tz10b-work/wt/research/selftest-pfair.py` | `tz10b-work--wt--research--selftest-pfair.py` | 22,643 | `7e641c93ea0244890f2726629b9f28a76d8f078b43da47e9cd9a16dbb43f223a` | `7e641c93ea0244890f2726629b9f28a76d8f078b43da47e9cd9a16dbb43f223a` | TZ-10b-sigma-or-link-report.md, TZ-11-student-link-and-domain-report.md |
| `/root/tz10b-work/wt/research/tz09-disk-inventory.py` | `tz10b-work--wt--research--tz09-disk-inventory.py` | 41,004 | `b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6` | `b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6` | TZ-09-disk-inventory-report.md, TZ-10-sigma-or-link-report.md, TZ-10a-sigma-or-link-report.md, TZ-10b-sigma-or-link-report.md, TZ-11-student-link-and-domain-report.md |
| `/root/tz10b-work/wt/research/tz10b-sigma-or-link.py` | `tz10b-work--wt--research--tz10b-sigma-or-link.py` | 61,018 | `406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088` | `406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088` | TZ-10b-sigma-or-link-report.md, TZ-11-student-link-and-domain-report.md |
| `/root/tz11-work/probe-m6.py` | `tz11-work--probe-m6.py` | 1,098 | `78e36b4ee9ba07aee43003bdcdd92b1734b4fefde088d48577361f85fec206d9` | `78e36b4ee9ba07aee43003bdcdd92b1734b4fefde088d48577361f85fec206d9` | TZ-11-student-link-and-domain-report.md |
| `/root/tz11-work/probe-selftests.out` | `tz11-work--probe-selftests.out` | 2,228 | `52b93f42b2f703a79f67c062582c66dfe86432d23fb58b27e74f1b49304d4dce` | `52b93f42b2f703a79f67c062582c66dfe86432d23fb58b27e74f1b49304d4dce` | TZ-11-student-link-and-domain-report.md |
| `/root/tz11-work/probe-selftests.py` | `tz11-work--probe-selftests.py` | 7,024 | `ede6a0b4948f66fbf6c3d6156e1225444ab8b42936f36cbc8a6fc6afeb14df9b` | `ede6a0b4948f66fbf6c3d6156e1225444ab8b42936f36cbc8a6fc6afeb14df9b` | TZ-11-student-link-and-domain-report.md |

Copied at 2026-09-14T23:39:02Z. `/root/btc-forensics/` held **94** files before and **141** after; **94 of 94** of the files already there hash exactly as before.

**§9, then: the two trees reclaimed, one command naming one tree each, verified by `test -e`.**

Each command was run on its own, after `copy-forensics.py` had exited 0, and its output is quoted
verbatim. The worktree was removed first so that git keeps no stale record of it; the branch
`tz-10b-sigma-or-link` itself was not deleted.

```
$ git -C /root/btc-5m-twap worktree remove /root/tz10b-work/wt
exit 0

$ rm -rf /root/tz10b-work; echo "rm exit $?"; test -e /root/tz10b-work; echo "test -e /root/tz10b-work exit $? at $(date -u +%Y-%m-%dT%H:%M:%SZ)"
rm exit 0
test -e /root/tz10b-work exit 1 at 2026-09-14T23:40:21Z

$ rm -rf /root/tz11-work; echo "rm exit $?"; test -e /root/tz11-work; echo "test -e /root/tz11-work exit $? at $(date -u +%Y-%m-%dT%H:%M:%SZ)"
rm exit 0
test -e /root/tz11-work exit 1 at 2026-09-14T23:40:23Z
```

Neither command was refused. `test -e` exits 1, so neither path exists.

**`/root/tz11a-work/`** is reclaimed by the next TZ once this report is on `main`, on the same
terms. The files this report names by SHA-256 are the three deterministic outputs of each full
run (V3), and `/root/btc-forensics/` receives a copy of each first.

---

## 6. What could not be implemented as written, and every reading chosen

These are every point where the text needed a reading, and every workaround. None changes a
threshold, a definition or a formula.

1. **The interpreter.** System `python3` has no `numpy`, and §0 blocks the run if `numpy` is
   absent. The instrument therefore runs on `/root/tz01-env/venv/bin/python`: Python 3.12.3 with
   `numpy` 2.5.3, the virtual environment built for TZ-01. V7's self-test subprocess runs on the
   same interpreter, and the self-tests themselves use the standard library only.
2. **"Relative tolerance of `1e-8`"** is read as: the golden-section bracket shrinks until its
   width is at most `1e-8` times its midpoint. "Search edge" means that one end of the final
   bracket never moved off its bound. That test is exact, and it is what the tables mark.
3. **"The best-fitting normal"** is read as the zero-mean normal at the root mean square of `r`.
   The Student fit has no location parameter either, and the model's residual has mean zero.
4. **§3.4 item 4's "`κ` of `r / ŝ` on the admissible rows"** is read as `κ` over the checkpoint
   rows of M4, with `ŝ` = `LINK_SCALE[tau]`, the scale M4 prices with. Rows whose checkpoint
   anchor M6 drops carry no `r`. They are left out and counted: every such count is 0.
5. **V12 item 1's "most influential"** is read as the observation whose contribution to
   `ll(λ̂) − ll(1)` is largest **in magnitude**, matching item 2's explicit
   "largest-magnitude". At 17 of the 28 fits, that observation is not the one
   with the largest signed contribution. The JSON output names both.
6. **V12 item 2 is applied literally.** A member's contribution is the sum of its log-densities at
   `(ν̂, ŝ)`. Those are mostly negative, and larger in magnitude for members with more anchors or
   wider residuals. The member removed is the one with the largest sum in magnitude.
7. **§5.2 items 1 and 2, "to 12 significant digits".** Both readings are asserted: equality
   under `%.11e`, and the stated `1e-12` relative tolerance. Item 5a's "10 significant digits"
   is equality under `%.9e`, TZ-10b's reading.
8. **§5.2 item 5's "two asserts".** 5a is a plain `assert` and 5b is the item's counted check.
   Both abort the file, and the family counts six, as V7 requires.
9. **V4's "TZ-08a V8's seven `RMS(u)`".** §10 C5 speaks of "TZ-08a V8's six ratios". TZ-08a's
   V8 table printed seven rows, `tau = 10` included, so all seven are asserted, and the `Λ_oos`
   column beside them too.
10. **V6's "every top-level object"** is read as TZ-10b's definition: functions, classes, and
    assignments to plain names. `selftest-pfair.py`'s `if __name__ == "__main__":` block gains the
    new family's lines, and its module docstring gains one paragraph. Both are insertions, and
    neither is a named object.
11. **§3.1's cost statement bounds one evaluation at "at most 198,000 anchors".** The all-member
    populations hold up to 236,125. The cost was measured instead, and is in V3: the
    first fit took 2.74 s, and the whole run 294.3 s, against CANON's `3,600`.
12. **G1 is computed by the committed `tz06.table_for`**, with its `brier_constant` argument set
    to §4's `0.2496`, so `beats_constant` is G1's strict inequality. G2's allowance is
    `tz06.MAX_FAILING_BINS`, read from the code.
13. **G2 on test 1 had 0 eligible bins at every `tau`.** The sum of failing bins is 0, which is
    at most 2, so the row reads pass. With nothing eligible, it could not have failed.
14. **`λ̂` on the search edge.** The committed `lambda_hat` searches `[0.5, 3.0]`. Two gated
    values sit at `0.5`: test 1's admissible `λ̂` at `tau` 180 and 10. G3 compares them with 1
    as §4 writes it, and each reads FAIL with a distance of `0.5`. That distance is the distance
    to the interval's bound, not to an interior maximiser.
15. **Admissibility compares `sigma_hat` with the committed six-digit literal**, not with the
    unrounded measurement, because the pricer quotes against the literal. V8 asserts that each
    literal equals the measurement at six significant digits. The admissible populations are
    asserted identical wherever they are formed.
16. **`p_fair_student`** evaluates `t_cdf(float(state / sd), float(LINK_NU[tau]))`, exactly as
    §5.1 writes it. It raises on a `tau` outside its tables, as §3.2 and item 6 require. The
    `_betacf` guard constant `1e-300` is local to the function, so `pfair.py` gains exactly
    twelve names.
17. **V4's third assertion is not given an influence figure under V12.** It reproduces a committed
    `λ̂` under the old link, and is not a statistic this TZ reports as a measurement.
18. **The §0 preflight's scratch footprint.** The two `du` reads of `/root/tz11a-work` and
    `/root/.claude` were printed to the terminal by the same commands that took the preflight
    reads, and were not saved to the preflight files. §0 quotes them from that output.
19. **The timeline.**
    - The host gate, preflight read 1 and the scratch tree came at 18:25–18:26Z.
    - A usage limit then paused the session until about 20:35Z. Nothing ran during the pause.
    - The fingerprint check ran at 2026-09-14T20:35:46Z, and preflight read 2 followed at 20:36:02Z.
    - The branch worktree was created next, then the build.
    - `--emit` measured the three tables at about 20:52Z, and the self-tests ran with them in
      place.
    - One local commit was made. Three smoke passes of the whole instrument followed, on the full
      fit set and on test sets as they then stood.
    - The smoke found one defect: the M5 table's `admissible` flag was overwritten by a result key
      of the same name. It was fixed and folded into the one unpushed commit with `git commit
      --amend`. The pushed branch has one commit, and the worktree listing in §0 shows the
      pre-amend head.
    - Nothing a smoke pass printed is reported as a measurement here. The tables were frozen
      before the first smoke pass ran, and nothing was re-fitted after it.
    - Test 2 completed at 23:27:49Z. The two full runs ran from 23:28:35Z to 23:38:24Z, and
      publication and §9 followed by 23:41Z.
    - A second usage limit paused the session after this report's text was drafted: the last
      scratch file before it was written at 23:45:01Z, and work resumed at 05:04Z on 2026-09-15.
      Nothing ran during the pause. `origin/main` was still `72e7092` and PR #12 still open when
      work resumed. The assembler's free-space read, and every later step, come after it.
20. **Test 1's figures were visible before the formal runs.** The second and third smoke passes
    used the full, committed test 1, so their M4 and M3 figures for test 1 are the ones reported
    here. The tables, the thresholds and the code had been fixed before those passes, and the
    formal runs changed nothing but the addition of the complete test 2.
