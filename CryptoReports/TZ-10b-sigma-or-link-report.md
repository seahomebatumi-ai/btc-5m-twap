# TZ-10b — `sigma` or the link: the discriminating measurement — REPORT

**Status: executed.** Every gate passed, every check TZ-10b §7 names was run, and the
instrument's asserts held on two full runs whose outputs are byte-identical. The numbers are
reported here and **the verdict of §4 is the Architect's** — the instrument carries no
threshold and judges nothing.

- **The two readings of §4, at the two `tau` the gate failed at:**
  - `f`, from `κ`: **-1.3793** at `tau = 60` and **-0.9437** at `tau = 30`. `κ_post` is above
    `κ_hat` at 7 of 7 `tau`. Standardized by the successor interval's `sigma`, the
    residual is further from a normal's shape than under the pricer's own `sigma`, not closer.
  - `g`, from `λ̂`: **-2.6605** at 60 and **0.2115** at 30.
  - M4's out-of-sample `R²`: **-0.0189**, and 0.1090 in sample.
- **Where those numbers fall in §4's tables.** This is arithmetic for the Architect, not a
  verdict (§2).
  - `f` is in §4.1's row "link-dominant" at both `tau`.
  - `g` reads "anything else — mixed": 0.2115 at `tau = 30` lies between 0.20 and 0.50.
  - The two readings disagree, which §4.2 makes **mixed**. §4.3 then compares `R²` -0.0189
    with 0.10, and that row reads "TZ-11 replaces the link".
- **The pre-registered prediction failed on all three of its quantities** (§2).
- **`sigma_win`**, the self-normalizing upper bound, puts `κ` between 0.9375 and
  1.0056 at every `tau`. No reading of §4 uses it.
- **The host.** §6's two reads find `PROJECT_GAMING_PS5` idle, `+1,372,160` bytes over
  12,977 s. A third read, taken after the runs, finds it writing again: `+36,524,032` bytes
  since read 2, the largest part of it one capture file of 30,516,707 bytes (§0).
- **Validation:**
  - V2: 140 of 140 both ways.
  - V3: 3 of 3 outputs byte-identical over two full runs.
  - V4: 14 of 14.
  - V5: 2 of 2.
  - V6: insertions only.
  - V7: 6 of 6 self-tests, and the `λ̂` comparison **under the reading stated in §6 item 1**.
  - V8: the capture unchanged across both runs.
- **Publication:** branch `tz-10b-sigma-or-link` at `d34606ee9a592e51293eaad0996c7cae3b84dfcd`, pull request https://github.com/seahomebatumi-ai/btc-5m-twap/pull/11, not
  merged. Anchor `A6` would move to `45b307b221d4`.

Nothing was written under `/var/lib/btc-recorder/`, and no `quotes.jsonl.gz` was opened. The
live recorder, pid `228592` on `4216c04`, was not signalled or restarted.

Executor model: **Opus** (`claude-opus-5`), as the TZ requires.

---

## 0. Fingerprint

Read from `origin/main` = `e75f83609b8ce52f4195c5ab015fccb634275c31`, fast-forwarded into the
primary checkout from `d015d3c` on 2026-09-14. The map was last changed at
`c86eb60074b7ff2ffe46fa3522e04c17c04b3ae6`, and the TZ-10b file arrived at `e75f836`. The run
started at 2026-09-14T06:55:40Z.

**Map revision required:** `2026-09-14-c`. **Read:** `2026-09-14-c`.

| anchor | required by TZ-10b §0 | read from map §0 | recomputed from the file |
|---|---|---|---|
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` | not recomputed — a Release asset, not on disk |
| `A2` — collector | `6c5089330629` | `6c5089330629` | `6c5089330629` |
| `A3` — phase | `0-complete / 1-answered-no / 2-not-started` | `0-complete / 1-answered-no / 2-not-started` | — a string |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b` | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` | `9fd1c7de0f74` | `9fd1c7de0f74` |
| `A6` — pricer | `cb72abb8dd8a` | `cb72abb8dd8a` | `cb72abb8dd8a` |

**6 of 6 anchors match.**

### Fingerprint table

Every row of the map's §0 table, computed on `main` at `e75f836`. Lines are `wc -l` and bytes
are `wc -c`. The scratch script `/root/tz10b-work/gate-check.py` parsed the map's own table,
compared each row and asserted the frozen count.

| path | lines | bytes | state | SHA-256 | matches map |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 470 | 64,249 | reported | `b3e9fdb585cf00bfeba0be11337d0b374b9cbd676ae353a7bf9f130b6e502f19` | — |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | yes |
| `research/twap-divergence.py` | 1,135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | yes |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | yes |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | — (equal to the map) |
| `research/pfair.py` | 281 | 12,499 | frozen | `cb72abb8dd8a460908d0b4cd50da472ddd1c72b57be35b4cf90303503d47e01f` | yes |
| `research/selftest-pfair.py` | 306 | 15,647 | frozen | `97de9782d319c82ee6a7d81ddbd8e00d590d85ffe2daa41abe3d71ae92712c94` | yes |
| `research/tz06-calibration.py` | 577 | 27,138 | frozen | `715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f` | yes |
| `research/tz07a-variance-time.py` | 619 | 28,219 | frozen | `4321637751a3b847fa7e59309555b802dcc9d5ba68c7407a8ec20ab76c1b3d5e` | yes |
| `research/tz07b-settlement-dispersion.py` | 515 | 24,926 | frozen | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` | yes |
| `research/tz08a-out-of-sample.py` | 745 | 38,822 | frozen | `37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c` | yes |
| `research/tz09-disk-inventory.py` | 894 | 41,004 | frozen | `b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6` | yes |
| `research/recorder/recorder.py` | 608 | 25,658 | frozen | `9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03` | yes |
| `research/recorder/config.py` | 112 | 4,773 | frozen | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | yes |
| `research/recorder/manifest.py` | 254 | 10,002 | frozen | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | yes |
| `research/recorder/analyze.py` | 813 | 34,705 | frozen | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` | yes |
| `research/recorder/probe.py` | 227 | 9,324 | frozen | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | yes |
| `research/recorder/selftest.py` | 573 | 30,591 | frozen | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` | yes |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | — (equal to the map) |

**Frozen rows matching on main: 16 of 16; tracked rows equal to the map: 2 of 2.** The assert `frozen == matched == 16` is in the scratch script, not in the
instrument.

TZ-10b §2 authorizes two of those rows to move, `research/pfair.py` (anchor `A6`) and
`research/selftest-pfair.py`, and adds one file. On branch `tz-10b-sigma-or-link` they now read:

| path, on branch `tz-10b-sigma-or-link` | lines | bytes | SHA-256 |
|---|---|---|---|
| `research/pfair.py` | 313 | 13,985 | `45b307b221d410a7812759a89941dc7645dfda165a8e01a60aef5b17851a5d1e` |
| `research/selftest-pfair.py` | 441 | 22,643 | `7e641c93ea0244890f2726629b9f28a76d8f078b43da47e9cd9a16dbb43f223a` |
| `research/tz10b-sigma-or-link.py` | 1,224 | 61,018 | `406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088` |

The new `A6` would be `45b307b221d4`. The map is the Architect's to revise; this report only
states the value.

The TZ file:

| path | lines | bytes | SHA-256 |
|---|---|---|---|
| `CryptoTZ/TZ-10b-sigma-or-link.md` | 429 | 26,443 | `8705ca3783784511f8a4f33b23a1664566fb2bda7159d860295a522aadafe49b` |

### Worktree hygiene — a disclosure, not a gate

`git worktree list --porcelain` at run start, verbatim:

```
worktree /root/btc-5m-twap
HEAD e75f83609b8ce52f4195c5ab015fccb634275c31
branch refs/heads/main

worktree /root/tz09-work/wt
HEAD e45f38e89b5ee18e64a16a654b341d74fadcac26
branch refs/heads/tz-09-disk-inventory

worktree /root/tz09-work/wt-report
HEAD 33483975ca7fd1a1d6778e66c1ea94ab4e28c82f
detached
```

`prunable` entries: **0**, counted by `git worktree list --porcelain | grep -c
'^prunable'`. The primary checkout `/root/btc-5m-twap` is on branch **`main`**, and it stayed
there for the whole run. After that read, this run added one worktree,
`/root/tz10b-work/wt`, on branch `tz-10b-sigma-or-link`, and built everything in it. The
recorder runs from the primary checkout, which never left `main`.

### Host gate and resource floor

| check | required | observed |
|---|---|---|
| `/var/lib/btc-recorder/` exists and holds interval directories | yes | yes: `btc-updown-5m/` held 1,118 directories at run start, `1789033800` to `1789368900` |
| recorder running; newest `runtime.jsonl` start record sha | `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` | pid `228592`, `/root/tz04a-env/venv/bin/python -B -u recorder.py`, started Sat Sep 12 09:53:04 2026. The newest start record is `recv_ns` `1789206785264516934`, sha `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` |
| filesystem | `/dev/vda2`, total `31,612,203,008` bytes | `/dev/vda2`, total `31,612,203,008` bytes |
| free space at run start | at least `10,327,051,118` bytes | `14,398,554,112` bytes at 2026-09-14T06:55:45Z |

**All three host checks pass, and so does the floor.**

### Every read of free space in the run

TZ-10b §0 requires each to be at or above `3,000,000,000` bytes.

| UTC | free bytes on `/dev/vda2` | read by | at or above `3,000,000,000` |
|---|---|---|---|
| 2026-09-14T06:55:45Z | 14,398,554,112 | §0 gate and §6 read 1 (`df`) | yes — recorded, not asserted |
| 2026-09-14T10:32:02Z | 14,388,191,232 | §6 read 2 (`df`) | yes — recorded, not asserted |
| 2026-09-14T10:32:37Z | 14,388,572,160 | smoke test, `host_read` (`os.statvfs`) | yes — asserted |
| 2026-09-14T10:34:52Z | 14,387,945,472 | end-to-end smoke, run start (`os.statvfs`) | yes — asserted |
| 2026-09-14T10:35:02Z | 14,387,912,704 | end-to-end smoke, run end (`os.statvfs`) | yes — asserted |
| 2026-09-14T10:37:17Z | 14,387,339,264 | full run 1, run start (`os.statvfs`) | yes — asserted |
| 2026-09-14T10:52:15Z | 14,377,746,432 | full run 1, run end (`os.statvfs`) | yes — asserted |
| 2026-09-14T10:52:36Z | 14,372,044,800 | full run 2, run start (`os.statvfs`) | yes — asserted |
| 2026-09-14T11:08:01Z | 14,343,909,376 | full run 2, run end (`os.statvfs`) | yes — asserted |
| 2026-09-14T11:12:25Z | 14,321,958,912 | third host read, after the runs (`df`) | yes — recorded, not asserted |
| 2026-09-14T11:14:04Z | 14,320,291,840 | this report's assembler (`df`) | yes — asserted |

An `os.statvfs` read is `f_bavail · f_frsize`, the quantity `df -B1` prints as `Avail`.

### The §6 preflight — recorded, gating nothing beyond the floor

§6 asks for two reads of `df` and `du -x -B1 -s /root/PROJECT_GAMING_PS5`, taken at least
`1,800` s apart. Both were taken and are reported as read.

| read | `df` taken (UTC) | free bytes on `/dev/vda2` | `du -x -B1 -s /root/PROJECT_GAMING_PS5` (bytes) | `du` finished (UTC) |
|---|---|---|---|---|
| 1 | 2026-09-14T06:55:45Z | 14,398,554,112 | 336,822,272 | 2026-09-14T06:55:45Z |
| 2 | 2026-09-14T10:32:02Z | 14,388,191,232 | 338,194,432 | 2026-09-14T10:32:02Z |

The two reads are **12,977 s** apart. That is far more than the `1,800` s asked for: the
session was paused by a usage limit between the two (§6 item 15).

- **Free space:** it changed by `-10,362,880` bytes, a fall of **`68,995,363` bytes/day**
  at that rate.
- **`PROJECT_GAMING_PS5`:** it changed by `+1,372,160` bytes, **`9,135,750` bytes/day**.

This run's own apparatus is inside the free-space figure (System Map §7 item 29's rule).
`/root/tz10b-work`, which did not exist before 06:55:40Z, held `1,667,072` bytes on
disk once the files written after read 2 are subtracted (70 files and 6 directories whose last write preceded read 2; the instrument, rewritten after read 2, held about 61 KB more at the time). The session store
under `/root/.claude` also grew and was not measured. This is arithmetic on two reads, applies no
rule from TZ-09, and gates nothing.

**A third read, beyond §6's two.** The table of free-space reads above falls faster during run 2
than during run 1. So the same pair of reads was taken once more after the runs:

| read | `df` taken (UTC) | free bytes on `/dev/vda2` | `du -x -B1 -s /root/PROJECT_GAMING_PS5` (bytes) | `du` finished (UTC) |
|---|---|---|---|---|
| 3 | 2026-09-14T11:12:25Z | 14,321,958,912 | 374,718,464 | 2026-09-14T11:12:25Z |

- **Since read 2,** 2,423 s earlier, `PROJECT_GAMING_PS5` grew by `+36,524,032` bytes, and
  free space changed by `-66,232,320` bytes.
- **This run's own share of that fall** is at most `18,554,880` bytes. `/root/tz10b-work`
  held `20,221,952` bytes on disk at 2026-09-14T11:13:42Z, just after read 3, against
  `1,667,072` at read 2.
- **What was written:** 29 files in that tree were written after read 2, `51,876,622`
  bytes in all. The largest is `/root/PROJECT_GAMING_PS5/netaudit/telemetry/captures/AUTO-20260914-105542-20260914-105603.pcap`, 30,516,707 bytes, last written at
  2026-09-14T11:11:03Z. It is a capture file in the `netaudit/telemetry/captures` subtree that map §6
  names as the consumer.
- **What that means:** that project was writing again during this run's later hour, although
  reads 1 and 2 alone would say it was idle.

This read goes beyond what §6 asks for, and it gates nothing (§6 item 17).

---

## 1. The measurements, in §3's order

### 1.0 Input and the sets

**What was read.**

- Every `manifest.json`, through `analyze.load_manifests`.
- The `chainlink` stream of each of the 800 members, with its predecessor (the run-up window) and
  its successor (`sigma_post`) merged in by `pfair.merged_stream`.
- The `twap60` stream of each member, for `K` inside `pfair.observations`.
- `resolution.json` in exactly the two places TZ-10b §2 names:
  - inside `tz06-calibration.qualification`, for every unit the two walks considered —
    443 and 433 units;
  - in the instrument's `m2_labels`, for the 800 members, where M2 alone reads it.
- No `quotes.jsonl.gz` and no `gamma.json` was opened. Nothing was re-collected.

**The sets.** Both committed sets were re-derived by the committed code and asserted equal to
the hashes in TZ-10b §3.0 (V5). TZ-08a's set came through TZ-08a's own `the_set`, with every
assertion TZ-08a made.

- TZ-06: 443 units considered (1789033800 … 1789166400), 400 members (1789035000 … 1789166400), 43 non-members (disconnect: 41, disconnect + no chainlink at or before T0-300: 2); member list `6d94a346a47a04a1a0849968effd9023d7585fe628b304ba2ae7a15953ee67f9`
- TZ-08a: 433 units considered (1789166700 … 1789296300), 400 members (1789166700 … 1789296300), 33 non-members (disconnect: 33); member list `3b17729c050e5fbf8fed1bd0877d5dd5c229370609cd672c84eeed1ddc3d5762`
- `sigma_post` arm: 753 of 800 qualify, 47 do not (successor manifest not complete: 5, successor manifest not complete + disconnect inside [T0+300, T0+600]: 42)
- intersection: 753 members, 376 TZ-06 and 377 TZ-08a; member list `5cc0b9ceba02a5a9f9ebdeb4dfa421b89a90a58d0f414b8d95cc359cf2902590`

**The `sigma_post` arm.** **753 of 800 members qualify** and 47 do not (successor manifest not complete: 5; successor manifest not complete + disconnect inside [T0+300, T0+600]: 42). The intersection is therefore **753 members — 376 of the TZ-06 400 and 377 of the TZ-08a 400**, member-list SHA-256 `5cc0b9ceba02a5a9f9ebdeb4dfa421b89a90a58d0f414b8d95cc359cf2902590`. Non-qualifiers leave that arm only. The full list,
member by member and in order, is in V10 (§4).

### 1.1 M1 — the shape, three ways

Over the intersection, per `tau`, per arm. Then `sigma_hat` alone over the full 800, as §3.0
asks for V4.

- **Under `sigma_hat`,** `κ` rises as `tau` falls, from 1.1209 at 240 to 3.2288 at 10.
  - It sits below TZ-08a V9's implied values at every `tau`. Those were read on the TZ-08a 400
    alone; these are read over the intersection of both sets.
  - `Λ_u` runs from 0.955 to 1.026. That is near 1, as §3.0 says it must be:
    exactly 1 on the TZ-06 400, which V4 shows.
- **Under `sigma_post`,** `κ` is above `κ_hat` at 7 of 7 `tau`: 2.1908 against
  1.5005 at 60, and 2.8957 against 1.9753 at 30.
  - `Λ_u` runs from 1.354 to 1.497.
  - Standardized by the successor interval's realised scale, the residual is further from a
    normal's shape, not closer.
- **Under `sigma_win`, the upper bound,** `κ` lies between 0.9375 and 1.0056 at every
  `tau`, and the tail beyond three robust sigma is at or below the normal's `0.0027`.
  - Divided by its own window's realised scale, `Y` is no heavier-tailed than a normal.
  - That is the self-normalization §3.0 warns of, and it is an upper bound only.

#### M1, `sigma_hat`, over the intersection

| tau | anchors | `Lambda_u` | `MAD/0.674490` | `IQR/1.348980` | **`kappa`** | `kappa` published (TZ-08a V9) | `P(\|u\| > 3 MAD/0.674490)` | normal |
|---|---|---|---|---|---|---|---|---|
| 240 | 268806 | 1.026319 | 0.915610 | 0.915425 | **1.1209** | 1.22 | 0.0136 | 0.0027 |
| 180 | 314023 | 1.009055 | 0.890780 | 0.891192 | **1.1328** | 1.28 | 0.0127 | 0.0027 |
| 120 | 359714 | 0.959652 | 0.808108 | 0.810275 | **1.1875** | 1.43 | 0.0193 | 0.0027 |
| 90 | 382644 | 0.955108 | 0.738901 | 0.737988 | **1.2926** | 1.69 | 0.0344 | 0.0027 |
| 60 | 405748 | 0.957690 | 0.638263 | 0.639742 | **1.5005** | 2.27 | 0.0629 | 0.0027 |
| 30 | 428981 | 0.959582 | 0.485779 | 0.485932 | **1.9753** | 3.45 | 0.1128 | 0.0027 |
| 10 | 444486 | 0.962157 | 0.297990 | 0.297965 | **3.2288** | 5.26 | 0.1730 | 0.0027 |

#### M1, `sigma_post`, over the intersection

| tau | anchors | `Lambda_u` | `MAD/0.674490` | `IQR/1.348980` | **`kappa`** | `kappa` published (TZ-08a V9) | `P(\|u\| > 3 MAD/0.674490)` | normal |
|---|---|---|---|---|---|---|---|---|
| 240 | 268806 | 1.354008 | 0.886500 | 0.885673 | **1.5274** | 1.22 | 0.0460 | 0.0027 |
| 180 | 314023 | 1.408733 | 0.887990 | 0.884839 | **1.5864** | 1.28 | 0.0489 | 0.0027 |
| 120 | 359714 | 1.429710 | 0.835274 | 0.835364 | **1.7117** | 1.43 | 0.0604 | 0.0027 |
| 90 | 382644 | 1.449028 | 0.768457 | 0.769887 | **1.8856** | 1.69 | 0.0731 | 0.0027 |
| 60 | 405748 | 1.462115 | 0.667401 | 0.668675 | **2.1908** | 2.27 | 0.0939 | 0.0027 |
| 30 | 428981 | 1.477171 | 0.510119 | 0.510056 | **2.8957** | 3.45 | 0.1339 | 0.0027 |
| 10 | 444486 | 1.497291 | 0.319178 | 0.319242 | **4.6911** | 5.26 | 0.1813 | 0.0027 |

#### M1, `sigma_win` — upper bound, over the intersection

| tau | anchors | `Lambda_u` | `MAD/0.674490` | `IQR/1.348980` | **`kappa`** | `kappa` published (TZ-08a V9) | `P(\|u\| > 3 MAD/0.674490)` | normal |
|---|---|---|---|---|---|---|---|---|
| 240 | 268806 | 0.931241 | 0.975239 | 0.975316 | **0.9549** | 1.22 | 0.0012 | 0.0027 |
| 180 | 314023 | 0.955557 | 1.011844 | 1.012037 | **0.9444** | 1.28 | 0.0007 | 0.0027 |
| 120 | 359714 | 0.955089 | 0.989831 | 0.990399 | **0.9649** | 1.43 | 0.0009 | 0.0027 |
| 90 | 382644 | 0.948996 | 0.960465 | 0.962721 | **0.9881** | 1.69 | 0.0014 | 0.0027 |
| 60 | 405748 | 0.931398 | 0.926211 | 0.926934 | **1.0056** | 2.27 | 0.0018 | 0.0027 |
| 30 | 428981 | 0.890023 | 0.896455 | 0.896582 | **0.9928** | 3.45 | 0.0004 | 0.0027 |
| 10 | 444464 | 0.857228 | 0.914344 | 0.914316 | **0.9375** | 5.26 | 0.0000 | 0.0027 |

#### M1, `sigma_hat` over the full 800

| tau | anchors | `Lambda_u` | `MAD/0.674490` | `IQR/1.348980` | **`kappa`** | `P(\|u\| > 3 MAD/0.674490)` |
|---|---|---|---|---|---|---|
| 240 | 285636 | 1.023123 | 0.913214 | 0.913289 | **1.1204** | 0.0134 |
| 180 | 333673 | 1.009615 | 0.891427 | 0.892063 | **1.1326** | 0.0125 |
| 120 | 382198 | 0.965172 | 0.806713 | 0.808931 | **1.1964** | 0.0198 |
| 90 | 406568 | 0.957638 | 0.736040 | 0.735667 | **1.3011** | 0.0351 |
| 60 | 431112 | 0.956268 | 0.636766 | 0.638052 | **1.5018** | 0.0631 |
| 30 | 455785 | 0.957507 | 0.485217 | 0.485445 | **1.9734** | 0.1126 |
| 10 | 472250 | 0.960058 | 0.299169 | 0.298991 | **3.2091** | 0.1724 |

#### M1, anchors

| tau | possible, intersection | dropped by M6, intersection | possible, 800 | dropped by M6, 800 | `sigma_win` undefined | members contributing a drop |
|---|---|---|---|---|---|---|
| 240 | 271833 | 3027 | 288800 | 3164 | 0 | 31 |
| 180 | 317013 | 2990 | 336800 | 3127 | 0 | 31 |
| 120 | 362193 | 2479 | 384800 | 2602 | 0 | 31 |
| 90 | 384783 | 2139 | 408800 | 2232 | 0 | 31 |
| 60 | 407373 | 1625 | 432800 | 1688 | 0 | 31 |
| 30 | 429963 | 982 | 456800 | 1015 | 0 | 31 |
| 10 | 445023 | 537 | 472800 | 550 | 22 | 31 |

Members contributing a dropped anchor (31): 1789035900, 1789043100, 1789050300, 1789057500, 1789064700, 1789071900, 1789073100, 1789080300, 1789102500, 1789128300, 1789131600, 1789138800, 1789141800, 1789149000, 1789162500, 1789169700, 1789170600, 1789177800, 1789185000, 1789197000, 1789200300, 1789206900, 1789214100, 1789221300, 1789252800, 1789260000, 1789267200, 1789274400, 1789278300, 1789285500, 1789292700

`sigma_win` undefined — a flat span, `Y = 0` over `sigma = 0`: 1789276200 at tau 10: 11 anchors, 1789276500 at tau 10: 11 anchors

### 1.2 M2 — `λ̂`, three ways

The TZ-07a §8 scale statistic, recomputed with each `sigma`. The likelihood uses `pfair.log_phi`
and never `log(phi(...))` (§3.2). Every `λ̂` is printed with its value recomputed without its
single most influential observation, and that observation is named by `T0` and `tau` — for
each table, `tau` is the row.

- On the pooled intersection, `λ̂` is:
  - under `sigma_hat`, 1.125529 at `tau = 60` and 1.753224 at `tau = 30`;
  - under `sigma_post`, 1.459495 and 1.593924.
- On TZ-08a's full 400 under `sigma_hat`, the table is TZ-08a's own corrected `λ̂`, recomputed
  with `log_phi`. V7 compares it at `tau = 30`.
- At `tau = 30` one observation dominates. Under `sigma_hat` and under `sigma_post` the most
  influential observation, pooled, is `T0 1789268400`, the observation M5 reports. Without it,
  `λ̂` is 0.856516 and 0.950838.

#### M2, `sigma_hat`, intersection, TZ-06

| tau | n | `lambda_hat` | `ll_at_lambda_hat` | `ll_at_one` | LR | p | most influential (T0, label, z) | `lambda_hat` without it | shift |
|---|---|---|---|---|---|---|---|---|---|
| 240 | 376 | 1.005241 | -224.635688 | -224.636533 | 0.001690 | 0.967207 | 1789081500, 0, 1.2401 | 0.970875 | -0.034366 |
| 180 | 376 | 0.948910 | -183.466780 | -183.605168 | 0.276776 | 0.598822 | 1789037700, 0, 1.6739 | 0.913744 | -0.035165 |
| 120 | 376 | 0.962925 | -146.051136 | -146.133529 | 0.164787 | 0.684787 | 1789164000, 1, -1.8435 | 0.926155 | -0.036770 |
| 90 | 376 | 0.765628 | -98.230404 | -101.316300 | 6.171791 | 0.0129803 | 1789043100, 1, -1.2153 | 0.738626 | -0.027002 |
| 60 | 376 | 0.806436 | -62.823822 | -64.285792 | 2.923940 | 0.0872745 | 1789166400, 0, 1.3615 | 0.760598 | -0.045838 |
| 30 | 376 | 1.031593 | -21.700280 | -21.716061 | 0.031561 | 0.858994 | 1789103100, 1, -3.3168 | 0.500000 | -0.531593 |
| 10 | 376 | 1.304050 | -7.287323 | -7.566613 | 0.558580 | 0.454833 | 1789103100, 1, -1.7804 | 0.601106 | -0.702944 |

#### M2, `sigma_hat`, intersection, TZ-08a

| tau | n | `lambda_hat` | `ll_at_lambda_hat` | `ll_at_one` | LR | p | most influential (T0, label, z) | `lambda_hat` without it | shift |
|---|---|---|---|---|---|---|---|---|---|
| 240 | 377 | 0.889904 | -224.003172 | -224.375506 | 0.744668 | 0.38817 | 1789249500, 1, -1.6006 | 0.831193 | -0.058711 |
| 180 | 377 | 1.167059 | -209.404425 | -210.497150 | 2.185451 | 0.13932 | 1789261200, 0, 1.9333 | 1.117716 | -0.049342 |
| 120 | 377 | 1.039855 | -160.909018 | -160.998608 | 0.179180 | 0.672079 | 1789205700, 1, -2.5375 | 0.976780 | -0.063075 |
| 90 | 377 | 1.017164 | -126.862200 | -126.878944 | 0.033488 | 0.854799 | 1789268400, 1, -2.1653 | 0.968725 | -0.048438 |
| 60 | 377 | 1.331429 | -99.339273 | -104.330288 | 9.982031 | 0.00158075 | 1789225800, 1, -3.7501 | 1.215857 | -0.115573 |
| 30 | 377 | 2.104499 | -54.834979 | -86.833785 | 63.997612 | 1.2457e-15 | 1789268400, 1, -10.8187 | 0.672003 | -1.432496 |
| 10 | 377 | 0.647367 | -4.048933 | -4.495109 | 0.892350 | 0.344841 | 1789293300, 0, 0.4649 | 0.500000 | -0.147367 |

#### M2, `sigma_hat`, intersection, pooled

| tau | n | `lambda_hat` | `ll_at_lambda_hat` | `ll_at_one` | LR | p | most influential (T0, label, z) | `lambda_hat` without it | shift |
|---|---|---|---|---|---|---|---|---|---|
| 240 | 753 | 0.950826 | -448.863651 | -449.012039 | 0.296775 | 0.585912 | 1789249500, 1, -1.6006 | 0.923263 | -0.027564 |
| 180 | 753 | 1.050867 | -393.863700 | -394.102318 | 0.477237 | 0.489677 | 1789261200, 0, 1.9333 | 1.027729 | -0.023138 |
| 120 | 753 | 1.001337 | -307.131929 | -307.132137 | 0.000417 | 0.983712 | 1789205700, 1, -2.5375 | 0.969739 | -0.031599 |
| 90 | 753 | 0.904612 | -227.157104 | -228.195243 | 2.076279 | 0.149604 | 1789268400, 1, -2.1653 | 0.876357 | -0.028255 |
| 60 | 753 | 1.125529 | -167.240218 | -168.616080 | 2.751724 | 0.0971496 | 1789225800, 1, -3.7501 | 1.049738 | -0.075791 |
| 30 | 753 | 1.753224 | -82.166052 | -108.549846 | 52.767588 | 3.75446e-13 | 1789268400, 1, -10.8187 | 0.856516 | -0.896708 |
| 10 | 753 | 1.007426 | -12.061313 | -12.061722 | 0.000818 | 0.977188 | 1789103100, 1, -1.7804 | 0.626757 | -0.380669 |

#### M2, `sigma_post`, intersection, TZ-06

| tau | n | `lambda_hat` | `ll_at_lambda_hat` | `ll_at_one` | LR | p | most influential (T0, label, z) | `lambda_hat` without it | shift |
|---|---|---|---|---|---|---|---|---|---|
| 240 | 376 | 1.263439 | -229.657724 | -231.373984 | 3.432520 | 0.0639245 | 1789129800, 1, -1.8166 | 1.197322 | -0.066116 |
| 180 | 376 | 1.125154 | -190.689183 | -191.421875 | 1.465383 | 0.226076 | 1789129800, 1, -2.3725 | 1.064042 | -0.061112 |
| 120 | 376 | 1.110990 | -152.715241 | -153.409718 | 1.388956 | 0.238582 | 1789147200, 1, -2.4941 | 1.055061 | -0.055929 |
| 90 | 376 | 0.822112 | -100.749111 | -102.442674 | 3.387127 | 0.0657073 | 1789164000, 1, -1.5226 | 0.784236 | -0.037876 |
| 60 | 376 | 0.947344 | -67.505371 | -67.615745 | 0.220747 | 0.638471 | 1789166400, 0, 2.8752 | 0.799897 | -0.147447 |
| 30 | 376 | 0.565642 | -14.172515 | -16.772779 | 5.200528 | 0.02258 | 1789103100, 1, -1.1736 | 0.500000 | -0.065642 |
| 10 | 376 | 1.194634 | -6.678918 | -6.792315 | 0.226794 | 0.633911 | 1789119600, 0, 1.4048 | 0.719180 | -0.475454 |

#### M2, `sigma_post`, intersection, TZ-08a

| tau | n | `lambda_hat` | `ll_at_lambda_hat` | `ll_at_one` | LR | p | most influential (T0, label, z) | `lambda_hat` without it | shift |
|---|---|---|---|---|---|---|---|---|---|
| 240 | 377 | 1.087547 | -224.223530 | -224.413896 | 0.380732 | 0.537212 | 1789258200, 0, 2.1905 | 0.983282 | -0.104266 |
| 180 | 377 | 1.437891 | -207.217364 | -213.301544 | 12.168358 | 0.000486071 | 1789246200, 0, 3.1566 | 1.322630 | -0.115261 |
| 120 | 377 | 1.229823 | -164.145952 | -166.454638 | 4.617372 | 0.0316497 | 1789227300, 1, -2.7519 | 1.153306 | -0.076516 |
| 90 | 377 | 1.386088 | -142.000986 | -149.020741 | 14.039509 | 0.00017901 | 1789269000, 0, 5.0555 | 1.189622 | -0.196466 |
| 60 | 377 | 1.823338 | -116.942392 | -145.076302 | 56.267819 | 6.32421e-14 | 1789269000, 0, 8.1890 | 1.411867 | -0.411471 |
| 30 | 377 | 1.936926 | -51.933092 | -75.364410 | 46.862636 | 7.61406e-12 | 1789268400, 1, -8.8107 | 1.127410 | -0.809516 |
| 10 | 377 | 0.723196 | -5.626528 | -5.939322 | 0.625589 | 0.428978 | 1789293300, 0, 0.8609 | 0.500000 | -0.223196 |

#### M2, `sigma_post`, intersection, pooled

| tau | n | `lambda_hat` | `ll_at_lambda_hat` | `ll_at_one` | LR | p | most influential (T0, label, z) | `lambda_hat` without it | shift |
|---|---|---|---|---|---|---|---|---|---|
| 240 | 753 | 1.180880 | -454.166930 | -455.787880 | 3.241901 | 0.0717773 | 1789258200, 0, 2.1905 | 1.132845 | -0.048036 |
| 180 | 753 | 1.267624 | -399.160806 | -404.723418 | 11.125226 | 0.000851615 | 1789246200, 0, 3.1566 | 1.213938 | -0.053686 |
| 120 | 753 | 1.165018 | -317.135918 | -319.864356 | 5.456876 | 0.0194915 | 1789227300, 1, -2.7519 | 1.129947 | -0.035071 |
| 90 | 753 | 1.132608 | -249.624086 | -251.463415 | 3.678658 | 0.0551132 | 1789269000, 0, 5.0555 | 1.018689 | -0.113919 |
| 60 | 753 | 1.459495 | -194.068350 | -212.692046 | 37.247392 | 1.04054e-09 | 1789269000, 0, 8.1890 | 1.207577 | -0.251919 |
| 30 | 753 | 1.593924 | -76.394050 | -92.137189 | 31.486277 | 2.00855e-08 | 1789268400, 1, -8.8107 | 0.950838 | -0.643086 |
| 10 | 753 | 0.959286 | -12.719845 | -12.731638 | 0.023584 | 0.877947 | 1789119600, 0, 1.4048 | 0.721583 | -0.237703 |

#### M2, `sigma_win` — upper bound, intersection, TZ-06

| tau | n | `lambda_hat` | `ll_at_lambda_hat` | `ll_at_one` | LR | p | most influential (T0, label, z) | `lambda_hat` without it | shift |
|---|---|---|---|---|---|---|---|---|---|
| 240 | 376 | 1.073816 | -221.955679 | -222.121261 | 0.331163 | 0.564975 | 1789129800, 1, -1.3714 | 1.035006 | -0.038810 |
| 180 | 376 | 1.052417 | -182.694637 | -182.830466 | 0.271659 | 0.602221 | 1789037700, 0, 2.0351 | 1.005013 | -0.047404 |
| 120 | 376 | 1.067093 | -142.760714 | -142.995388 | 0.469348 | 0.493287 | 1789164000, 1, -2.3031 | 1.011795 | -0.055298 |
| 90 | 376 | 0.943497 | -98.908083 | -99.058843 | 0.301520 | 0.582931 | 1789043100, 1, -1.8566 | 0.893487 | -0.050010 |
| 60 | 376 | 0.917769 | -58.951007 | -59.144525 | 0.387034 | 0.533862 | 1789115100, 1, -1.3438 | 0.867405 | -0.050364 |
| 30 | 376 | 0.883887 | -14.096830 | -14.253275 | 0.312890 | 0.575912 | 1789103100, 1, -1.8999 | 0.533920 | -0.349967 |
| 10 | 376 | 1.485486 | -5.417777 | -5.773791 | 0.712027 | 0.398772 | 1789103100, 1, -1.1594 | 1.016269 | -0.469217 |

#### M2, `sigma_win` — upper bound, intersection, TZ-08a

| tau | n | `lambda_hat` | `ll_at_lambda_hat` | `ll_at_one` | LR | p | most influential (T0, label, z) | `lambda_hat` without it | shift |
|---|---|---|---|---|---|---|---|---|---|
| 240 | 377 | 1.082736 | -217.600868 | -217.785800 | 0.369863 | 0.543079 | 1789182600, 0, 1.9665 | 1.002932 | -0.079804 |
| 180 | 377 | 1.157683 | -186.214600 | -187.079901 | 1.730602 | 0.188334 | 1789182600, 0, 1.7050 | 1.113288 | -0.044395 |
| 120 | 377 | 1.012835 | -135.426644 | -135.433274 | 0.013259 | 0.908327 | 1789205400, 0, 1.8154 | 0.962255 | -0.050579 |
| 90 | 377 | 0.886998 | -96.948516 | -97.434135 | 0.971238 | 0.324372 | 1789224600, 0, 1.3987 | 0.846384 | -0.040614 |
| 60 | 377 | 0.975407 | -63.769935 | -63.787328 | 0.034785 | 0.852048 | 1789269000, 0, 1.4213 | 0.925776 | -0.049631 |
| 30 | 377 | 0.712400 | -17.440022 | -18.517493 | 2.154942 | 0.142112 | 1789268400, 1, -1.3596 | 0.500000 | -0.212400 |
| 10 | 377 | 2.723334 | -8.789858 | -19.532886 | 21.486055 | 3.56411e-06 | 1789249800, 0, 5.4057 | 0.634707 | -2.088627 |

#### M2, `sigma_win` — upper bound, intersection, pooled

| tau | n | `lambda_hat` | `ll_at_lambda_hat` | `ll_at_one` | LR | p | most influential (T0, label, z) | `lambda_hat` without it | shift |
|---|---|---|---|---|---|---|---|---|---|
| 240 | 753 | 1.078052 | -439.557549 | -439.907061 | 0.699025 | 0.403112 | 1789182600, 0, 1.9665 | 1.040645 | -0.037406 |
| 180 | 753 | 1.098069 | -369.105037 | -369.910368 | 1.610661 | 0.204399 | 1789037700, 0, 2.0351 | 1.071629 | -0.026440 |
| 120 | 753 | 1.043917 | -278.250255 | -278.428662 | 0.356814 | 0.550281 | 1789164000, 1, -2.3031 | 1.012246 | -0.031671 |
| 90 | 753 | 0.918774 | -195.932134 | -196.492978 | 1.121688 | 0.289555 | 1789043100, 1, -1.8566 | 0.890571 | -0.028204 |
| 60 | 753 | 0.947286 | -122.771932 | -122.931852 | 0.319840 | 0.571704 | 1789269000, 0, 1.4213 | 0.921802 | -0.025484 |
| 30 | 753 | 0.799295 | -31.773113 | -32.770768 | 1.995312 | 0.157787 | 1789103100, 1, -1.8999 | 0.646139 | -0.153157 |
| 10 | 753 | 2.397604 | -14.740630 | -25.306676 | 21.132093 | 4.28688e-06 | 1789249800, 0, 5.4057 | 1.098592 | -1.299011 |

#### M2, `sigma_hat`, full sets, TZ-06

| tau | n | `lambda_hat` | `ll_at_lambda_hat` | `ll_at_one` | LR | p | most influential (T0, label, z) | `lambda_hat` without it | shift |
|---|---|---|---|---|---|---|---|---|---|
| 240 | 400 | 0.998828 | -239.108296 | -239.108341 | 0.000090 | 0.992438 | 1789081500, 0, 1.2401 | 0.966328 | -0.032500 |
| 180 | 400 | 0.946207 | -195.052783 | -195.217136 | 0.328705 | 0.566423 | 1789037700, 0, 1.6739 | 0.913313 | -0.032894 |
| 120 | 400 | 0.944915 | -153.488816 | -153.684905 | 0.392178 | 0.531157 | 1789164000, 1, -1.8435 | 0.909978 | -0.034937 |
| 90 | 400 | 0.761224 | -104.291327 | -107.692209 | 6.801765 | 0.00910678 | 1789043100, 1, -1.2153 | 0.735589 | -0.025634 |
| 60 | 400 | 0.786869 | -64.728818 | -66.609484 | 3.761331 | 0.0524508 | 1789166400, 0, 1.3615 | 0.741845 | -0.045024 |
| 30 | 400 | 1.012182 | -22.499331 | -22.501796 | 0.004929 | 0.944028 | 1789103100, 1, -3.3168 | 0.500000 | -0.512182 |
| 10 | 400 | 1.252581 | -7.506033 | -7.714489 | 0.416912 | 0.518482 | 1789103100, 1, -1.7804 | 0.579092 | -0.673489 |

#### M2, `sigma_hat`, full sets, TZ-08a

| tau | n | `lambda_hat` | `ll_at_lambda_hat` | `ll_at_one` | LR | p | most influential (T0, label, z) | `lambda_hat` without it | shift |
|---|---|---|---|---|---|---|---|---|---|
| 240 | 400 | 0.862850 | -235.758917 | -236.399763 | 1.281692 | 0.257585 | 1789249500, 1, -1.6006 | 0.808268 | -0.054582 |
| 180 | 400 | 1.139746 | -220.492395 | -221.318571 | 1.652352 | 0.198639 | 1789261200, 0, 1.9333 | 1.093058 | -0.046688 |
| 120 | 400 | 1.029147 | -170.378939 | -170.429638 | 0.101398 | 0.750159 | 1789205700, 1, -2.5375 | 0.968817 | -0.060330 |
| 90 | 400 | 1.012168 | -135.175778 | -135.184612 | 0.017668 | 0.894254 | 1789268400, 1, -2.1653 | 0.965772 | -0.046396 |
| 60 | 400 | 1.294919 | -104.665576 | -108.839345 | 8.347539 | 0.0038621 | 1789225800, 1, -3.7501 | 1.180672 | -0.114247 |
| 30 | 400 | 2.041844 | -57.940127 | -88.462422 | 61.044589 | 5.57967e-15 | 1789268400, 1, -10.8187 | 0.641189 | -1.400654 |
| 10 | 400 | 0.607433 | -4.430659 | -5.027133 | 1.192949 | 0.274736 | 1789293300, 0, 0.4649 | 0.500000 | -0.107433 |

#### M2, `sigma_hat`, full sets, pooled

| tau | n | `lambda_hat` | `ll_at_lambda_hat` | `ll_at_one` | LR | p | most influential (T0, label, z) | `lambda_hat` without it | shift |
|---|---|---|---|---|---|---|---|---|---|
| 240 | 800 | 0.934000 | -475.217998 | -475.508104 | 0.580212 | 0.446229 | 1789249500, 1, -1.6006 | 0.908190 | -0.025810 |
| 180 | 800 | 1.036271 | -416.405298 | -416.535707 | 0.260817 | 0.609559 | 1789261200, 0, 1.9333 | 1.014435 | -0.021837 |
| 120 | 800 | 0.986732 | -324.092620 | -324.114543 | 0.043847 | 0.834139 | 1789205700, 1, -2.5375 | 0.956610 | -0.030122 |
| 90 | 800 | 0.899267 | -241.653893 | -242.876821 | 2.445856 | 0.117836 | 1789268400, 1, -2.1653 | 0.872314 | -0.026953 |
| 60 | 800 | 1.095068 | -174.609527 | -175.448829 | 1.678605 | 0.19511 | 1789225800, 1, -3.7501 | 1.020703 | -0.074365 |
| 30 | 800 | 1.708313 | -86.135099 | -110.964218 | 49.658237 | 1.83e-12 | 1789268400, 1, -10.8187 | 0.829047 | -0.879266 |
| 10 | 800 | 0.965833 | -12.732118 | -12.741622 | 0.019009 | 0.890341 | 1789103100, 1, -1.7804 | 0.594105 | -0.371727 |

### 1.3 M3 — where the heavy tail lives

Under `sigma_hat`, within deciles of two stratifiers over the intersection's members.

- **Deciles of `sigma_hat`, causal.** Within-stratum `κ` does not fall toward 1.
  - Its size-weighted mean is at or above the pooled `κ` at 7 of 7 `tau`:
    1.6752 against 1.5005 at 60, and 2.3051 against 1.9753 at 30.
  - On §3.3's own test, the excess kurtosis lives within the strata.
  - The strata are far from alike. The lowest decile of `sigma_hat` has `κ` 3.227 at 30 and
    2.611 at 60; the highest has 1.119 and 1.077. The heavy tail sits in the
    low-`sigma_hat` deciles.
- **Deciles of `log(sigma_post / sigma_hat)`, non-causal.**
  - The size-weighted mean is at or above the pooled `κ` at 5 of 7 `tau`:
    2.0762 against 1.9753 at 30.
  - At 60 and at 30 the two extreme deciles carry the two largest stratum `κ`: 2.115 and
    1.989 at 60, 3.449 and 2.655 at 30.

#### M3, deciles of sigma_hat — causal

| tau | pooled `kappa` | size-weighted mean of stratum `kappa` | median of stratum `kappa` | stratum `kappa`, 1 … 10 | stratum tail, 1 … 10 |
|---|---|---|---|---|---|
| 240 | 1.1209 | 1.1346 | 1.0829 | 1.709 / 1.036 / 1.086 / 1.012 / 1.029 / 1.081 / 1.185 / 1.139 / 1.085 / 0.984 | 0.0662 / 0.0087 / 0.0132 / 0.0067 / 0.0045 / 0.0090 / 0.0183 / 0.0119 / 0.0086 / 0.0001 |
| 180 | 1.1328 | 1.1534 | 1.0855 | 1.856 / 1.152 / 1.114 / 1.044 / 1.129 / 1.098 / 1.063 / 1.073 / 0.977 / 1.031 | 0.0627 / 0.0156 / 0.0148 / 0.0041 / 0.0131 / 0.0100 / 0.0093 / 0.0095 / 0.0041 / 0.0082 |
| 120 | 1.1875 | 1.2428 | 1.1816 | 1.866 / 1.459 / 1.276 / 1.235 / 1.256 / 1.128 / 1.042 / 1.070 / 1.040 / 1.058 | 0.1144 / 0.0600 / 0.0309 / 0.0257 / 0.0284 / 0.0060 / 0.0064 / 0.0112 / 0.0058 / 0.0073 |
| 90 | 1.2926 | 1.3882 | 1.2557 | 2.145 / 1.870 / 1.487 / 1.490 / 1.304 / 1.208 / 1.087 / 1.112 / 1.102 / 1.079 | 0.1405 / 0.1131 / 0.0609 / 0.0626 / 0.0434 / 0.0225 / 0.0098 / 0.0116 / 0.0122 / 0.0084 |
| 60 | 1.5005 | 1.6752 | 1.5358 | 2.611 / 2.514 / 2.108 / 1.852 / 1.638 / 1.433 / 1.229 / 1.123 / 1.165 / 1.077 | 0.1607 / 0.1688 / 0.1393 / 0.1048 / 0.0823 / 0.0568 / 0.0265 / 0.0123 / 0.0198 / 0.0080 |
| 30 | 1.9753 | 2.3051 | 2.2498 | 3.227 / 3.591 / 3.417 / 3.112 / 2.574 / 1.925 / 1.473 / 1.288 / 1.321 / 1.119 | 0.1525 / 0.1877 / 0.2011 / 0.2004 / 0.1615 / 0.1042 / 0.0589 / 0.0354 / 0.0340 / 0.0145 |
| 10 | 3.2288 | 3.6031 | 4.1161 | 4.027 / 4.469 / 5.222 / 5.269 / 5.142 / 4.205 / 2.676 / 1.910 / 1.755 / 1.345 | 0.1406 / 0.1539 / 0.1752 / 0.1906 / 0.2013 / 0.2142 / 0.1598 / 0.1012 / 0.0826 / 0.0383 |

Strata bounds and sizes, per tau (members, anchors, from … to):

- tau 240: 1: 76, 26770, 0.11374 … 0.545832; 2: 75, 26990, 0.54599 … 0.805382; 3: 75, 26758, 0.806068 … 1.08124; 4: 76, 27015, 1.08252 … 1.37129; 5: 75, 26203, 1.37283 … 1.69328; 6: 75, 26890, 1.69535 … 2.1017; 7: 76, 27419, 2.10557 … 2.43081; 8: 75, 26877, 2.43978 … 3.07701; 9: 75, 26895, 3.08721 … 4.46467; 10: 75, 26989, 4.46486 … 32.7705
- tau 180: 1: 76, 31344, 0.108067 … 0.573304; 2: 75, 31367, 0.577685 … 0.832525; 3: 75, 31205, 0.836794 … 1.07184; 4: 76, 31601, 1.07853 … 1.38882; 5: 75, 30947, 1.39058 … 1.71173; 6: 75, 31319, 1.7118 … 2.08593; 7: 76, 31979, 2.08617 … 2.45356; 8: 75, 31304, 2.45415 … 3.13105; 9: 75, 31497, 3.13637 … 4.44385; 10: 75, 31460, 4.49331 … 30.9278
- tau 120: 1: 76, 35971, 0.142195 … 0.605684; 2: 75, 35952, 0.60583 … 0.837379; 3: 75, 36075, 0.840166 … 1.08323; 4: 76, 35931, 1.08409 … 1.40627; 5: 75, 35543, 1.40786 … 1.74431; 6: 75, 35882, 1.75329 … 2.12201; 7: 76, 36539, 2.12461 … 2.52069; 8: 75, 35874, 2.52155 … 3.09533; 9: 75, 35987, 3.09576 … 4.44393; 10: 75, 35960, 4.49334 … 29.581
- tau 90: 1: 76, 38341, 0.159139 … 0.607588; 2: 75, 38203, 0.617046 … 0.846472; 3: 75, 38233, 0.855321 … 1.1059; 4: 76, 38264, 1.1064 … 1.43003; 5: 75, 37946, 1.43304 … 1.74483; 6: 75, 38237, 1.75656 … 2.09008; 7: 76, 38813, 2.09046 … 2.5216; 8: 75, 38150, 2.5342 … 3.06498; 9: 75, 38247, 3.07965 … 4.40532; 10: 75, 38210, 4.44869 … 28.9675
- tau 60: 1: 76, 40813, 0.161564 … 0.620391; 2: 75, 40391, 0.637018 … 0.847464; 3: 75, 40513, 0.847769 … 1.09966; 4: 76, 40714, 1.09998 … 1.43334; 5: 75, 40294, 1.43732 … 1.75204; 6: 75, 40504, 1.75979 … 2.10232; 7: 76, 41093, 2.11744 … 2.49481; 8: 75, 40441, 2.49559 … 3.01822; 9: 75, 40512, 3.04211 … 4.43303; 10: 75, 40473, 4.45038 … 28.2
- tau 30: 1: 76, 43196, 0.159688 … 0.637701; 2: 75, 42701, 0.638645 … 0.8614; 3: 75, 42793, 0.86165 … 1.10542; 4: 76, 43206, 1.11688 … 1.4164; 5: 75, 42632, 1.41785 … 1.783; 6: 75, 42784, 1.78458 … 2.11634; 7: 76, 43341, 2.11979 … 2.52067; 8: 75, 42750, 2.52313 … 3.03077; 9: 75, 42825, 3.03307 … 4.35131; 10: 75, 42753, 4.40331 … 27.7536
- tau 10: 1: 76, 44806, 0.158522 … 0.647364; 2: 75, 44231, 0.649721 … 0.867941; 3: 75, 44313, 0.868026 … 1.1066; 4: 76, 44826, 1.12239 … 1.40959; 5: 75, 44250, 1.41274 … 1.77653; 6: 75, 44286, 1.79263 … 2.09459; 7: 76, 44885, 2.10039 … 2.50165; 8: 75, 44290, 2.50224 … 2.99686; 9: 75, 44325, 2.99738 … 4.37177; 10: 75, 44274, 4.40123 … 27.3457

#### M3, deciles of log(sigma_post / sigma_hat) — non-causal, diagnostic only

| tau | pooled `kappa` | size-weighted mean of stratum `kappa` | median of stratum `kappa` | stratum `kappa`, 1 … 10 | stratum tail, 1 … 10 |
|---|---|---|---|---|---|
| 240 | 1.1209 | 1.1012 | 1.0647 | 1.058 / 1.071 / 1.043 / 1.088 / 1.001 / 0.946 / 1.147 / 1.058 / 1.134 / 1.464 | 0.0027 / 0.0145 / 0.0076 / 0.0061 / 0.0061 / 0.0036 / 0.0172 / 0.0127 / 0.0182 / 0.0392 |
| 180 | 1.1328 | 1.1313 | 1.0891 | 1.144 / 1.174 / 1.029 / 1.062 / 1.075 / 0.984 / 1.101 / 1.078 / 1.156 / 1.511 | 0.0140 / 0.0172 / 0.0062 / 0.0104 / 0.0042 / 0.0021 / 0.0160 / 0.0082 / 0.0187 / 0.0307 |
| 120 | 1.1875 | 1.1946 | 1.1658 | 1.310 / 1.175 / 1.091 / 1.155 / 1.061 / 1.177 / 1.104 / 1.157 / 1.259 / 1.460 | 0.0452 / 0.0188 / 0.0109 / 0.0144 / 0.0048 / 0.0213 / 0.0126 / 0.0174 / 0.0281 / 0.0555 |
| 90 | 1.2926 | 1.3107 | 1.2576 | 1.568 / 1.309 / 1.197 / 1.222 / 1.127 / 1.274 / 1.224 / 1.241 / 1.445 / 1.501 | 0.0740 / 0.0342 / 0.0227 / 0.0215 / 0.0116 / 0.0323 / 0.0227 / 0.0231 / 0.0586 / 0.0652 |
| 60 | 1.5005 | 1.5477 | 1.4927 | 2.115 / 1.583 / 1.312 / 1.302 / 1.265 / 1.335 / 1.500 / 1.485 / 1.590 / 1.989 | 0.1295 / 0.0702 / 0.0376 / 0.0349 / 0.0321 / 0.0403 / 0.0630 / 0.0626 / 0.0754 / 0.1215 |
| 30 | 1.9753 | 2.0762 | 1.8714 | 3.449 / 2.216 / 1.733 / 1.491 / 1.639 / 1.585 / 1.876 / 1.867 / 2.245 / 2.655 | 0.1981 / 0.1350 / 0.0883 / 0.0597 / 0.0759 / 0.0733 / 0.1034 / 0.1015 / 0.1403 / 0.1486 |
| 10 | 3.2288 | 3.3318 | 3.0100 | 5.771 / 3.729 / 2.866 / 2.402 / 2.499 / 2.479 / 2.871 / 3.149 / 3.739 / 3.800 | 0.1935 / 0.1814 / 0.1608 / 0.1375 / 0.1419 / 0.1446 / 0.1604 / 0.1725 / 0.1830 / 0.1636 |

Strata bounds and sizes, per tau (members, anchors, from … to):

- tau 240: 1: 76, 26680, -2.3905 … -0.730525; 2: 75, 26879, -0.720128 … -0.471285; 3: 75, 26961, -0.470321 … -0.276505; 4: 76, 26880, -0.276296 … -0.147623; 5: 75, 26799, -0.146276 … -0.0347903; 6: 75, 26985, -0.0340272 … 0.0965434; 7: 76, 26890, 0.0966929 … 0.230223; 8: 75, 27075, 0.231527 … 0.409843; 9: 75, 26670, 0.414682 … 0.70613; 10: 75, 26987, 0.719371 … 2.50833
- tau 180: 1: 76, 31234, -2.39868 … -0.719954; 2: 75, 31319, -0.719306 … -0.482625; 3: 75, 31372, -0.482571 … -0.280857; 4: 76, 31814, -0.276528 … -0.147094; 5: 75, 31195, -0.146642 … -0.0515232; 6: 75, 31286, -0.0506568 … 0.0786416; 7: 76, 31906, 0.0802762 … 0.2059; 8: 75, 31240, 0.207335 … 0.38793; 9: 75, 31324, 0.3887 … 0.667138; 10: 75, 31333, 0.671447 … 2.35863
- tau 120: 1: 76, 35974, -2.33258 … -0.721472; 2: 75, 35871, -0.720297 … -0.479602; 3: 75, 35943, -0.472135 … -0.282782; 4: 76, 36423, -0.281956 … -0.172932; 5: 75, 35938, -0.172644 … -0.0468456; 6: 75, 35469, -0.0468328 … 0.0541588; 7: 76, 36556, 0.0556302 … 0.181247; 8: 75, 35824, 0.184535 … 0.364684; 9: 75, 35837, 0.365583 … 0.606573; 10: 75, 35879, 0.607281 … 2.27674
- tau 90: 1: 76, 38356, -2.36316 … -0.707295; 2: 75, 38151, -0.699676 … -0.470929; 3: 75, 38223, -0.465604 … -0.28528; 4: 76, 38733, -0.282982 … -0.175881; 5: 75, 38189, -0.170593 … -0.0463421; 6: 75, 37786, -0.0452173 … 0.0430791; 7: 76, 38826, 0.0464417 … 0.164823; 8: 75, 38104, 0.165547 … 0.36508; 9: 75, 38117, 0.365126 … 0.603419; 10: 75, 38159, 0.608132 … 2.26022
- tau 60: 1: 76, 40766, -2.33487 … -0.704346; 2: 75, 40444, -0.703579 … -0.466668; 3: 75, 40503, -0.463544 … -0.291993; 4: 76, 40951, -0.285986 … -0.163198; 5: 75, 40469, -0.163005 … -0.0484156; 6: 75, 40233, -0.0481125 … 0.0540219; 7: 76, 41031, 0.0588923 … 0.173928; 8: 75, 40389, 0.175707 … 0.356247; 9: 75, 40512, 0.358292 … 0.57301; 10: 75, 40450, 0.579901 … 2.18627
- tau 30: 1: 76, 43196, -2.41122 … -0.728769; 2: 75, 42754, -0.721468 … -0.455461; 3: 75, 42783, -0.455124 … -0.290227; 4: 76, 43291, -0.28811 … -0.166849; 5: 75, 42749, -0.165423 … -0.0465663; 6: 75, 42633, -0.0446457 … 0.0615552; 7: 76, 43324, 0.0625508 … 0.171187; 8: 75, 42761, 0.17317 … 0.343364; 9: 75, 42730, 0.349033 … 0.552973; 10: 75, 42760, 0.553823 … 2.18043
- tau 10: 1: 76, 44816, -2.40964 … -0.715192; 2: 75, 44284, -0.71478 … -0.455879; 3: 75, 44313, -0.453671 … -0.297878; 4: 76, 44851, -0.296915 … -0.168415; 5: 75, 44270, -0.164024 … -0.0457231; 6: 75, 44246, -0.0449194 … 0.0634412; 7: 76, 44851, 0.0648918 … 0.175649; 8: 75, 44285, 0.176097 … 0.329558; 9: 75, 44270, 0.331548 … 0.55305; 10: 75, 44300, 0.554209 … 2.05905

### 1.4 M4 — is the scale error knowable in advance?

- Fitted on the TZ-06 share, the four regressors give `R²` 0.1090 in sample. Out of sample, on
  the TZ-08a share and against the in-sample mean, they give -0.0189.
- The mean response moved between the two shares, from -0.022295 to -0.092298. The
  out-of-sample figure carries that shift.
- No model is adopted.

Fitted on 2632 observations (TZ-06 share of the intersection), evaluated on 2639 (TZ-08a share). Response `log(sigma_post / sigma_hat)`; mean -0.022295 in sample, -0.092298 out of sample.

| term | coefficient |
|---|---|
| intercept | 0.201309 |
| log(sigma_60 / sigma_300) | 0.0734455 |
| log sigma_hat | -0.214085 |
| \|move over the last 30 s\| / (sigma_hat * sqrt(30)) | 0.0126319 |
| tau | 4.62975e-07 |

In-sample `R2` **0.1090** · out-of-sample `R2` **-0.0189**

### 1.5 M5 — the observation the gate hangs on

`T0 1789268400`. `sigma_win` here is the checkpoint's own span, `[T0 + 300 − tau, T0 + 300]`.
`z`, `p_fair` and `log_phi(z)` are under `sigma_hat` and `corrected_sd`, as the pricer reads
them. **No conclusion is drawn from one point.**

| tau | `sigma_hat` | `sigma_post` | `sigma_win` | `Y` | `u` hat | `u` post | `u` win | `state` | `z` | `p_fair` | `log_phi(z)` | resolved |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 30 | 0.689147 | 0.846215 | 5.483703 | 17.969017 | 11.899767 | 9.691034 | 1.495466 | -16.336633 | -10.818740 | 0.0 | -61.831158 | Up |
| 10 | 1.408206 | 0.846215 | 0.532965 | -0.328541 | -0.633034 | -1.053447 | -1.672611 | 1.960925 | 3.778313 | 0.9999210528651188 | -0.000079 | Up |

### 1.6 The observations file

`/root/tz10b-work/tz10b-observations.csv`, the path §5.1 names: **5,601 lines,
5,553,429 bytes, SHA-256 `142ea46b765bbdb1796f0da03b198755ac7904aacb748e91419db0a8b423eacd`**. It is a byte copy of run 1's file, and V3 shows run
2's identical. It holds one row per member per `tau` at the checkpoint, 800 × 7 plus a header.
The 28 columns are:

`T0`, `set`, `tau`, `intersection`, `label`, `K`, `S_t`, `m_r`, `state`, `sigma_hat`, `sigma_post`, `sigma_win`, `sd_hat`, `sd_post`, `sd_win`, `z_hat`, `z_post`, `z_win`, `log_phi_z_hat`, `p_fair_hat`, `Y`, `r`, `u_hat`, `u_post`, `u_win`, `sigma_60`, `sigma_300`, `move_30`

A row carries every input and output of its observation. That is enough to rebuild its `z`,
`p_fair`, `log_phi(z)`, its M4 regressors and response, and its `Y`, `r` and three `u` at the
checkpoint anchor without re-running anything. Decimals are written at full precision and
floats by `repr`.

---

## 2. §4's two readings, and the prediction

| tau | `kappa_hat` | `kappa_post` | **`f`** | `lambda_hat`, pooled | `lambda_post`, pooled | **`g`, pooled** | `g`, TZ-06 | `g`, TZ-08a |
|---|---|---|---|---|---|---|---|---|
| 240 | 1.1209 | 1.5274 | **-3.3615** | 0.950826 | 1.180880 | **-2.6784** | -49.2602 | 0.2048 |
| 180 | 1.1328 | 1.5864 | **-3.4166** | 1.050867 | 1.267624 | **-4.2613** | -1.4497 | -1.6212 |
| 120 | 1.1875 | 1.7117 | **-2.7950** | 1.001337 | 1.165018 | **-122.3939** | -1.9937 | -4.7665 |
| 90 | 1.2926 | 1.8856 | **-2.0267** | 0.904612 | 1.132608 | **-0.3902** | 0.2410 | -21.4945 |
| **60** | 1.5005 | 2.1908 | **-1.3793** | 1.125529 | 1.459495 | **-2.6605** | 0.7280 | -1.4842 |
| **30** | 1.9753 | 2.8957 | **-0.9437** | 1.753224 | 1.593924 | **0.2115** | -12.7485 | 0.1517 |
| 10 | 3.2288 | 4.6911 | **-0.6561** | 1.007426 | 0.959286 | **-4.4828** | 0.3599 | 0.2150 |

The §4 numbers, and where they fall in §4's tables. This is arithmetic on the reported numbers,
for the Architect's verdict. The instrument applies no threshold.

| reading | `tau = 60` | `tau = 30` | the row of §4 the numbers fall in |
|---|---|---|---|
| §4.1, `f` from `κ` | -1.3793 | -0.9437 | link-dominant |
| §4.2, `g` from `λ̂`, pooled intersection | -2.6605 | 0.2115 | anything else — mixed |
| §4.3, out-of-sample `R²` — one figure over all `tau` | -0.0189 | -0.0189 | TZ-11 replaces the link, if the verdict is mixed |

- **§4.1.** `f` is negative at both `tau`, because `κ_post` exceeds `κ_hat`: 2.1908 against
  1.5005 at 60, and 2.8957 against 1.9753 at 30. Both are at or below 0.20, the row
  "link-dominant".
- **§4.2.** `g(60)` = -2.6605 is at or below 0.20. `g(30)` = 0.2115 is above 0.20, by
  0.0115, and below 0.50. The two `tau` do not fall in one row, so §4.2's table reads
  "anything else": mixed.
- **The two readings disagree.** §4.2 says: "Where they disagree, the verdict is mixed, and the
  disagreement is the finding." §4.3 then decides on M4. Out-of-sample `R²` -0.0189 is below
  0.10, and that row reads "TZ-11 replaces the link".
- **`g(30)` rests on one observation, which V11 names.**
  - Under both `sigma_hat` and `sigma_post`, the most influential observation at `tau = 30` is
    `T0 1789268400`. Without it, `λ̂` is 0.856516 and 0.950838.
  - The same formula applied to those two figures gives 0.6574. That is arithmetic on
    V11's numbers, not a reading §4.2 defines: §4.2 is defined on `λ̂` as M2 computes it.
  - At `tau = 60` the two arms' most influential observations are different members,
    `1789225800` and `1789269000`, so no such figure is formed there.

**The pre-registered prediction (§4.4).**

| quantity | predicted | observed | inside the predicted range |
|---|---|---|---|
| `f(60)` | 0.5 to 0.7 | -1.3793 | no |
| `f(30)` | 0.6 to 0.8 | -0.9437 | no |
| out-of-sample `R²` | 0.05 to 0.15 | -0.0189 | no |

The prediction was "mixed, leaning σ". **It failed on all three quantities, and each fell on the
link's side of §4's tables:**

- `f` is not between 0.5 and 0.8 but negative at both `tau`. The scale taken from the successor
  interval, which does not lag, leaves the residual further from a normal's shape, not closer.
- `R²` is not between 0.05 and 0.15 but below zero. The four causal regressors do not forecast
  the mixing variable on a new set.
- The only standardization that brings `κ` to about 1 is `sigma_win`, the window's own realised
  scale. §3.0 labels it an upper bound, and no reading uses it.

---

## 3. Implementation and `log_phi`

### 3.1 What was built

Branch `tz-10b-sigma-or-link`, one commit, `d34606ee9a592e51293eaad0996c7cae3b84dfcd`, three files. **Insertions only:**
nothing on `main` is removed or altered.

| file | change | lines | bytes | SHA-256 |
|---|---|---|---|---|
| `research/pfair.py` | `log_phi` and its two branches, after `phi`: +32 −0 | 313 | 13,985 | `45b307b221d410a7812759a89941dc7645dfda165a8e01a60aef5b17851a5d1e` |
| `research/selftest-pfair.py` | the six §5.2 items, as family `TZ-10b section 5.2`: +135 −0 | 441 | 22,643 | `7e641c93ea0244890f2726629b9f28a76d8f078b43da47e9cd9a16dbb43f223a` |
| `research/tz10b-sigma-or-link.py` | new: the instrument: +1224 −0 | 1,224 | 61,018 | `406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088` |

### 3.2 Where every quantity comes from

**No formula is reimplemented.** The instrument holds the sets' assertions, the `sigma_post`
qualification rule, the V2 sample, the strata, the regression and the tables, and nothing of
the model.

| quantity | committed source |
|---|---|
| `Y(a, tau)` and the anchor enumeration | `tz07b.residual`, walked exactly as `tz07b.member_r` walks it; the walk is guarded (V4 below) |
| the horizon `sigma · sqrt(H(tau))` | `tz07b.horizon_sd`, which takes it from `pfair.state_and_sd` |
| M6's disconnect rule | `tz07a.excluded_seconds` and `tz07a.excluded_prefix`, through `tz07b` |
| the sets | `tz06.scoring_set`, through `tz08a.the_set` for the TZ-08a 400 |
| the three `sigma`s | `pfair.realised_sigma` on `pfair.second_grid`; only the span differs |
| `sd` | `pfair.corrected_sd(tau, s)` — `tau` first, the signature as the file has it |
| `state`, `K`, `S_t`, `m_r`, `sigma_live` | `pfair.observations`; `sigma_hat == sigma_live` is asserted at every observation |
| `p_fair` | `pfair.p_fair` |
| `log Phi` | `pfair.log_phi`, added by this TZ (§3.3) |
| `λ̂` | `tz07a.lambda_hat`, the committed search and constants (see §6 item 5) |
| the robust scales and their constants | `tz07b.MAD_TO_SIGMA`, `tz07b.IQR_TO_SIGMA`, and `statistics.median` and inclusive quartiles, as `tz07b.dispersion` takes them |
| the stream reader | `analyze.reports`, through `pfair` |

### 3.3 `log_phi`

`pfair.py` gains four top-level names and nothing else: `LOG_PHI_CROSSOVER = -35`,
`log_phi_erfc_branch`, `log_phi_asymptotic_branch` and `log_phi`. The two branches are exposed
because §5.2 item 2 compares them one against the other, and a test must not carry a second copy
of either formula. The whole diff, as V6 printed it:

```diff
diff --git a/research/pfair.py b/research/pfair.py
index b7dc2c4..a87fedf 100644
--- a/research/pfair.py
+++ b/research/pfair.py
@@ -50,6 +50,38 @@ def phi(z):
     return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))
 
 
+# ---- TZ-10b section 5.2: the tail-accurate log of Phi ------------------------------
+
+# `phi` above is `0.5 * (1 + erf)`, the sum of two doubles near 1 once `z` is far below zero:
+# it loses relative accuracy below about `z = -4.5` and returns exactly 0.0 below about
+# `z = -8.37`, which sent TZ-08a's `ll(1)` to `-inf` at `tau = 30`. A likelihood over `Phi`
+# carries a tail-accurate `log Phi` beside it (System Map section 7 item 26), and this is that
+# function. `phi` is not touched: changing it would be a change to the section 1.2 link.
+#
+# Two branches, as TZ-10b section 5.2 writes them. Above the crossover `erfc` of a positive
+# argument keeps its relative accuracy; at and below it the asymptotic series takes over,
+# truncated after `-15/z**6`. The two agree to 10 significant digits at -30, -32 and -34.
+LOG_PHI_CROSSOVER = -35
+
+
+def log_phi_erfc_branch(z):
+    """`log(0.5 * erfc(-z / sqrt(2)))`: `log Phi(z)` for `z > LOG_PHI_CROSSOVER`."""
+    return math.log(0.5 * math.erfc(-z / math.sqrt(2)))
+
+
+def log_phi_asymptotic_branch(z):
+    """The asymptotic series for `log Phi(z)`, for `z <= LOG_PHI_CROSSOVER`."""
+    return (-0.5 * z * z - 0.5 * math.log(2 * math.pi) - math.log(-z)
+            + math.log1p(-1 / z ** 2 + 3 / z ** 4 - 15 / z ** 6))
+
+
+def log_phi(z):
+    """`log Phi(z)`, finite at every finite `z`: the branch TZ-10b section 5.2 selects."""
+    if z > LOG_PHI_CROSSOVER:
+        return log_phi_erfc_branch(z)
+    return log_phi_asymptotic_branch(z)
+
+
 def far_branch(tau, s_t, k, sigma):
     """TZ-06 section 3, `tau >= 60`.
 
```

`selftest-pfair.py` gains the six §5.2 items as their own family, counted on their own. Its row
in the map's §0 table is `frozen`, though no anchor names it. TZ-10b §2 authorizes that row to
move, and the map's next revision carries its new line count, byte count and hash. The output of
those six items, printed by the committed file and captured by V7:

```
tz10b_item_1_the_literals
      z = 0        erfc       log_phi -0.693147180559945  literal -0.693147180559945  relative 4.81e-16
      z = -1       erfc       log_phi -1.84102164500926  literal -1.84102164500926  relative 1.81e-15
      z = -2       erfc       log_phi -3.78318433368203  literal -3.78318433368203  relative 3.52e-16
      z = -3       erfc       log_phi -6.60772622151035  literal -6.60772622151035  relative 2.69e-16
      z = -4       erfc       log_phi -10.3601014865273  literal -10.3601014865273  relative 1.03e-15
      z = -5       erfc       log_phi -15.0649983939887  literal -15.0649983939887  relative 1.53e-15
      z = -6       erfc       log_phi -20.7367689499747  literal -20.7367689499747  relative 1.71e-16
      z = -8       erfc       log_phi -35.0134371599145  literal -35.0134371599145  relative 1.22e-15
      z = -10.819  erfc       log_phi -61.8339909672382  literal -61.8339909672382  relative 6.89e-16
      z = -15      erfc       log_phi -116.131384845712  literal -116.131384845712  relative 2.94e-15
      z = -20      erfc       log_phi -203.917155371097  literal -203.917155371097  relative 1.12e-15
      z = -30      erfc       log_phi -454.321243956343  literal -454.321243956343  relative 2.5e-16
      z = -36      asymptotic log_phi -652.503227593835  literal -652.503227593798  relative 5.73e-14
      z = -40      asymptotic log_phi -804.60844201377  literal -804.608442013754  relative 1.95e-14
  ok  item 1: log_phi equals all 14 literals to 12 significant digits
tz10b_item_2_the_branches_agree_at_the_crossover
      z = -30  erfc -454.321243956343  asymptotic -454.321243956502  relative 3.49e-13
      z = -32  erfc -516.385648625725  asymptotic -516.38564862582  relative 1.84e-13
      z = -34  erfc -582.446162246872  asymptotic -582.44616224693  relative 1.01e-13
  ok  item 2: the two branches agree to 10 significant digits at -30, -32 and -34
tz10b_item_3_the_identity_where_phi_is_sound
      z = -3  exp(log_phi) 0.0013498980316301  phi 0.0013498980316301  relative 5.3e-15
      z = -2  exp(log_phi) 0.0227501319481792  phi 0.0227501319481792  relative 6.1e-16
      z = -1  exp(log_phi) 0.158655253931457  phi 0.158655253931457  relative 0
      z = 0  exp(log_phi) 0.5  phi 0.5  relative 0
      z = 1  exp(log_phi) 0.841344746068543  phi 0.841344746068543  relative 0
      z = 2  exp(log_phi) 0.977249868051821  phi 0.977249868051821  relative 0
      z = 3  exp(log_phi) 0.99865010196837  phi 0.99865010196837  relative 0
  ok  item 3: exp(log_phi(z)) equals pfair.phi(z) to 12 significant digits at -3 ... 3
tz10b_item_4_the_composition_at_live_scale
      z = -10.819  S_t 99502.987762732  recovered z -10.819  log_phi -61.8339909672382  relative 6.89e-16
      z = -8       S_t 99632.554473783  recovered z -8.0  log_phi -35.0134371599145  relative 1.22e-15
      z = -3       S_t 99862.364177669  recovered z -3.0  log_phi -6.60772622151035  relative 2.69e-16
      z = 0        S_t 100000.250000000  recovered z 0.0  log_phi -0.693147180559945  relative 4.81e-16
  ok  item 4: at K = 100000.25, sigma = 3.25, tau = 240 the composition is finite and equals item 1's literal to 12 significant digits
tz10b_item_5_shape
      45001 points over -40 ... 5: 0 steps not strictly increasing
      80001 points over -40 ... 40: 0 values not finite
  ok  item 5: strictly increasing over -40 ... 5 and finite over -40 ... 40
tz10b_item_6_the_pathology_removed
      phi 0.0  log(phi) finite False  log_phi -61.8339909672382  exp(log_phi) 1.399068e-27
  ok  item 6: at z = -10.819 phi is exactly 0.0, log(phi) is not finite, log_phi is finite and exp(log_phi) is 1.399068e-27 and positive
```

---

## 4. Validation, V1 … V11

Every check TZ-10b §7 names was run, and each subsection gives its count and says whether it is
asserted:

- **Asserted in the instrument:** V2, V4, V5, V6, V7 and V8. Each is an `assert` that aborts the
  run when false. Both full runs reached their end, so each held on both.
- **Asserted by this report's assembler:** V3.
- **V1:** its reads are asserted where §0 says so.
- **Reports, with no assert:** V9 and V10.
- **Recorded, not asserted:** V11.

### V1 — gates

Fingerprint **6 of 6** anchors. Frozen rows **16 of 16**. Host **3 of 3**. Free space at
**11 of 11** reads is at or above `3,000,000,000` bytes, and the first is above the
`10,327,051,118` floor (§0). 8 of the 11 are asserted by a Python `assert` that aborts below the bound; the other 3 were compared by reading them, so they are **recorded, not asserted**.

### V2 — causality of the causal arm — asserted

The denominator and nothing else: `sigma_hat`, and `pfair.corrected_sd(tau, sigma_hat)` beside
it. The sample is the first 20 TZ-06 members in `T0` order, at all seven `tau`. Every `chainlink`
report stamped **strictly after** `T0 + (300 − tau)` is multiplied by `tz06.PERTURBATION` through
the committed `tz06.perturb_after`. The negative control is `tz06.perturb_one` on
`tz06.last_readable`. Before any count is taken, the run asserts per checkpoint that the control's
report lies outside the perturbed set and that the perturbation changed at least one report.

| count | value |
|---|---|
| `members` | 20 |
| `checkpoints` | 140 |
| `sigma_hat_bit_identical` | 140 |
| `corrected_sd_bit_identical` | 140 |
| `control_moved_sigma_hat` | 140 |
| `control_moved_corrected_sd` | 140 |
| `control_subject_stamped_at_the_checkpoint_instant` | 133 |
| `fewest_reports_perturbed_in_one_checkpoint` | 31 |

Sample: 1789035000, 1789035300, 1789035900, 1789036200, 1789036500, 1789036800, 1789037100, 1789037400, 1789037700, 1789038000, 1789038300, 1789038600, 1789038900, 1789039200, 1789039500, 1789039800, 1789040100, 1789040400, 1789040700, 1789041000

**`sigma_hat` bit-identical at 140 of 140 checkpoints, `corrected_sd` at
140 of 140. The control moves `sigma_hat` at 140 of 140.** Each is
asserted. The `sigma_post` and `sigma_win` arms are non-causal by construction and exempt, as
V2's own row says.

### V3 — determinism — asserted by the assembler

Two full runs, each from a fresh process on the same commit:

| run | started (UTC) | ended (UTC) | wall (s) | peak RSS (KB) | exit |
|---|---|---|---|---|---|
| 1 | 2026-09-14T10:37:00Z | 2026-09-14T10:52:16Z | 915.98 | 175,704 | 0 |
| 2 | 2026-09-14T10:52:16Z | 2026-09-14T11:08:02Z | 946.11 | 172,880 | 0 |

| output | lines | bytes | SHA-256, run 1 | SHA-256, run 2 | identical |
|---|---|---|---|---|---|
| `tz10b-results.json` | 13,445 | 332,640 | `994297738a539d67417911cd32f713f05892e36d443a8139ad4e844d50d1383d` | `994297738a539d67417911cd32f713f05892e36d443a8139ad4e844d50d1383d` | yes |
| `tz10b-tables.md` | 2,140 | 119,347 | `4dc3bfa41dee5dfd89ab2bd3345c28d43e314b9fefa77d4e2f5528d43236d39f` | `4dc3bfa41dee5dfd89ab2bd3345c28d43e314b9fefa77d4e2f5528d43236d39f` | yes |
| `tz10b-observations.csv` | 5,601 | 5,553,429 | `142ea46b765bbdb1796f0da03b198755ac7904aacb748e91419db0a8b423eacd` | `142ea46b765bbdb1796f0da03b198755ac7904aacb748e91419db0a8b423eacd` | yes |

**The three deterministic outputs are byte-identical across the two runs: 3 of 3.** `cmp`
returned 0 for each, and the assembler that writes this report asserts the three SHA-256 pairs
equal. `tz10b-host.json` holds each run's own clock and disk reads, so it differs by
construction and is not part of the comparison. Its contents are in V1 and V8.

### V4 — the instrument reproduces the committed measurement — asserted

On `r`, not on `u` (§3.0). The uncentred RMS of `r` under `sigma_hat` is asserted equal to each
committed table as its report printed it, at six decimals. For these values that is seven
significant digits, one more than V4 requires. `RMS(u) · SD_SCALE[tau]` is asserted equal to
`RMS(r)` at six significant digits.

| set | tau | anchors | `RMS(r)` | published | `RMS(u)` | `RMS(u) · SD_SCALE` | relative difference |
|---|---|---|---|---|---|---|---|
| TZ-06 | 240 | 143255 | 1.523759717 | 1.523760 | 0.999999814 | 1.523759717 | 1.00e-59 |
| TZ-06 | 180 | 167255 | 1.496022752 | 1.496023 | 1.000001840 | 1.496022752 | 1.00e-59 |
| TZ-06 | 120 | 191343 | 1.496276837 | 1.496277 | 0.999997886 | 1.496276837 | 1.30e-59 |
| TZ-06 | 90 | 203416 | 1.479154254 | 1.479154 | 1.000002876 | 1.479154254 | 0.00e+00 |
| TZ-06 | 60 | 215620 | 1.444657989 | 1.444658 | 0.999998608 | 1.444657989 | 7.00e-60 |
| TZ-06 | 30 | 227920 | 1.385805790 | 1.385806 | 0.999996962 | 1.385805790 | 1.00e-59 |
| TZ-06 | 10 | 236125 | 1.211176004 | 1.211176 | 0.999996701 | 1.211176004 | 1.00e-59 |
| TZ-08a | 240 | 142381 | 1.593657530 | 1.593658 | 1.045871745 | 1.593657530 | 1.00e-59 |
| TZ-08a | 180 | 166418 | 1.524720971 | 1.524721 | 1.019184884 | 1.524720971 | 7.00e-60 |
| TZ-08a | 120 | 190855 | 1.389965274 | 1.389965 | 0.928947305 | 1.389965274 | 1.40e-59 |
| TZ-08a | 90 | 203152 | 1.350835970 | 1.350836 | 0.913251509 | 1.350835970 | 1.00e-59 |
| TZ-08a | 60 | 215492 | 1.315235496 | 1.315235 | 0.910411790 | 1.315235496 | 1.00e-59 |
| TZ-08a | 30 | 227865 | 1.265286515 | 1.265287 | 0.913030296 | 1.265286515 | 1.00e-59 |
| TZ-08a | 10 | 236125 | 1.112329039 | 1.112329 | 0.918384583 | 1.112329039 | 1.00e-59 |

**TZ-07b's `Λ` reproduced at 7 of 7 `tau` on the TZ-06 400, and TZ-08a V8's `Λ_oos` at 7 of 7
on the TZ-08a 400.** `RMS(u) · SD_SCALE` equals `RMS(r)` at 14 of 14, the largest relative
difference being `1.4e-59`: 60-digit rounding. `RMS(u)` under `sigma_hat` on the TZ-06
400 is `1` to within the rounding of the six-digit literal, as §3.0 says it must be.

**The anchor walk is guarded as well.** On 50 members — the first 20 TZ-06 members, plus
every member whose grid M6 drops a second of (31 of them) — the instrument calls the committed
`tz07b.member_r` beside its own walk. It asserts that every `r` value, the Decimal sum of squares,
the dropped count and the checkpoint `r` are identical. System Map §7 item 24's rule is why the
guard holds the M6 members by construction.

### V5 — set identity — asserted

TZ-06: `6d94a346a47a04a1a0849968effd9023d7585fe628b304ba2ae7a15953ee67f9`. TZ-08a: `3b17729c050e5fbf8fed1bd0877d5dd5c229370609cd672c84eeed1ddc3d5762`. Both are computed by `tz07b.member_list_sha`, the
sorted `T0` list as decimal ASCII joined by newlines with no trailing newline, and asserted
equal to TZ-10b §3.0's values. **2 of 2.** The two sets share no member, which is asserted too.

### V6 — `pfair.py` additive only — asserted

The run is of committed files. That is asserted by `git status --porcelain`, which is empty for
the three files. The diff against the merge base, `git merge-base HEAD main`, is asserted to
hold insertions only, for `pfair.py` and for `selftest-pfair.py`. Every top-level function and
assignment either file held before is asserted byte-identical after, compared by its exact
source text through `ast`. That covers `SD_SCALE`, `corrected_sd`, `phi`, `TAUS`, `far_branch`,
`near_branch` and `state_and_sd` — `state` is formed inside the two branches. `pfair.py`'s
added names are asserted to be exactly the four of §3.3.

| file | lines added | lines removed | top-level objects before | byte-identical after | objects added |
|---|---|---|---|---|---|
| `pfair.py` | 32 | 0 | 21 | 21 | `LOG_PHI_CROSSOVER`, `log_phi`, `log_phi_asymptotic_branch`, `log_phi_erfc_branch` |
| `selftest-pfair.py` | 135 | 0 | 20 | 20 | `LOG_PHI_LITERALS`, `relative`, `significant`, `tz10b_item_1_the_literals`, `tz10b_item_2_the_branches_agree_at_the_crossover`, `tz10b_item_3_the_identity_where_phi_is_sound`, `tz10b_item_4_the_composition_at_live_scale`, `tz10b_item_5_shape`, `tz10b_item_6_the_pathology_removed` |

The diff to `pfair.py` is printed in full in §3.3.

### V7 — `log_phi` — asserted

**The six self-tests of §5.2: 6 of 6**, each an `assert` that aborts `selftest-pfair.py`. The
instrument runs that file as a subprocess and asserts its exit status 0 and the four family
counts TZ-07b section 6 30, TZ-10b section 5.2 6, V5 56, section 3 machinery 18, **110 checks in all**. The 104 that were there are
unchanged, and V6 proves it. The six items' output is in §3.3.

**`λ̂` at `tau = 30` under `sigma_hat`, on TZ-08a's 400:**

| quantity | value |
|---|---|
| `λ̂`, committed search, `log(phi(...))` — TZ-08a's computation | 2.0418426092 |
| `λ̂`, committed search, `log_phi` — M2 | 2.0418435851 |
| difference | +9.759e-07 |
| `ll_at_one`, `log(phi(...))` · `log_phi` | -inf · -88.462422 |
| quoted by TZ-10b §7 V7 · printed by TZ-08a | 2.0418 · 2.041843 |

The committed search with `log(phi(...))` returns TZ-08a's value. That is asserted as `2.0418`
at four decimals, as TZ-10b quotes it, and as `2.041843` at six, as TZ-08a's report printed it.
With `log_phi` it moves by **`+9.759e-07`**. "Expected to agree past the sixth decimal" is
asserted as a difference below `1e-6`. **At six printed decimals the two values differ in the
last digit, `2.041843` against `2.041844`.** The reading is §6 item 1, stated before anything
else there.

### V8 — the capture is untouched — asserted

Each full run read the host twice, at its start and at its end. It asserted, between the two:

- the same recorder pid;
- the same newest start record, its sha and `recv_ns`;
- an interval count that did not fall;
- an equal SHA-256 over the name, size and modification time of every file in every interval
  directory the run reads — 872 directories, 7,276 files.

| run | read | UTC | recorder pids | newest start sha | `recv_ns` | interval directories | read-set SHA-256 | files |
|---|---|---|---|---|---|---|---|---|
| 1 | run start | 2026-09-14T10:37:17Z | [228592] | `4216c04673ce…` | 1789206785264516934 | 1,162 | `49796c381ca624a6…` | 7,276 |
| 1 | run end | 2026-09-14T10:52:15Z | [228592] | `4216c04673ce…` | 1789206785264516934 | 1,165 | `49796c381ca624a6…` | 7,276 |
| 2 | run start | 2026-09-14T10:52:36Z | [228592] | `4216c04673ce…` | 1789206785264516934 | 1,165 | `49796c381ca624a6…` | 7,276 |
| 2 | run end | 2026-09-14T11:08:01Z | [228592] | `4216c04673ce…` | 1789206785264516934 | 1,168 | `49796c381ca624a6…` | 7,276 |

What the instrument can write, enumerated as System Map §7 item 32 requires:

- **Files:** four outputs, into the `--out` directory. That directory is asserted to lie outside
  `/var/lib/btc-recorder/`.
- **Subprocesses:** two, each a fixed argument list with no shell — `git`, in six read-only
  forms (`merge-base`, `rev-parse`, `status --porcelain`, `diff`, `diff --unified=0`, `show`),
  and `python3 -B selftest-pfair.py`.
- **Reads:** the committed readers open the capture read-only (`gzip.open(…, "rt")`, `open(…)`
  for JSON). The instrument's own reads of the host are `os.statvfs`, `os.stat`,
  `os.listdir`, `/proc/<pid>/cmdline` and `runtime.jsonl`, all read-only.

### V9 — fingerprint table

Every row of map §0 is in §0 in lines, bytes and SHA-256. **The frozen rows match: 16 of 16.**
The two rows TZ-10b moves are reported beside them, as they stand on the branch.

### V10 — disclosure

Every unit each walk considered, in order, members and non-members alike, with the reason for
each non-member. Then every member's `sigma_post` qualification, in order.

#### The TZ-06 walk

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

#### The TZ-08a walk

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

#### The `sigma_post` arm

| # | T0 | set | qualifies | reason |
|---|---|---|---|---|
| 1 | 1789035000 | TZ-06 | yes | — |
| 2 | 1789035300 | TZ-06 | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 3 | 1789035900 | TZ-06 | yes | — |
| 4 | 1789036200 | TZ-06 | yes | — |
| 5 | 1789036500 | TZ-06 | yes | — |
| 6 | 1789036800 | TZ-06 | yes | — |
| 7 | 1789037100 | TZ-06 | yes | — |
| 8 | 1789037400 | TZ-06 | yes | — |
| 9 | 1789037700 | TZ-06 | yes | — |
| 10 | 1789038000 | TZ-06 | yes | — |
| 11 | 1789038300 | TZ-06 | yes | — |
| 12 | 1789038600 | TZ-06 | yes | — |
| 13 | 1789038900 | TZ-06 | yes | — |
| 14 | 1789039200 | TZ-06 | yes | — |
| 15 | 1789039500 | TZ-06 | yes | — |
| 16 | 1789039800 | TZ-06 | yes | — |
| 17 | 1789040100 | TZ-06 | yes | — |
| 18 | 1789040400 | TZ-06 | yes | — |
| 19 | 1789040700 | TZ-06 | yes | — |
| 20 | 1789041000 | TZ-06 | yes | — |
| 21 | 1789041300 | TZ-06 | yes | — |
| 22 | 1789041600 | TZ-06 | yes | — |
| 23 | 1789041900 | TZ-06 | yes | — |
| 24 | 1789042200 | TZ-06 | yes | — |
| 25 | 1789042500 | TZ-06 | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 26 | 1789043100 | TZ-06 | yes | — |
| 27 | 1789043400 | TZ-06 | yes | — |
| 28 | 1789043700 | TZ-06 | yes | — |
| 29 | 1789044000 | TZ-06 | yes | — |
| 30 | 1789044300 | TZ-06 | yes | — |
| 31 | 1789044600 | TZ-06 | yes | — |
| 32 | 1789044900 | TZ-06 | yes | — |
| 33 | 1789045200 | TZ-06 | yes | — |
| 34 | 1789045500 | TZ-06 | yes | — |
| 35 | 1789045800 | TZ-06 | yes | — |
| 36 | 1789046100 | TZ-06 | yes | — |
| 37 | 1789046400 | TZ-06 | yes | — |
| 38 | 1789046700 | TZ-06 | yes | — |
| 39 | 1789047000 | TZ-06 | yes | — |
| 40 | 1789047300 | TZ-06 | yes | — |
| 41 | 1789047600 | TZ-06 | yes | — |
| 42 | 1789047900 | TZ-06 | yes | — |
| 43 | 1789048200 | TZ-06 | yes | — |
| 44 | 1789048500 | TZ-06 | yes | — |
| 45 | 1789048800 | TZ-06 | yes | — |
| 46 | 1789049100 | TZ-06 | yes | — |
| 47 | 1789049400 | TZ-06 | yes | — |
| 48 | 1789049700 | TZ-06 | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 49 | 1789050300 | TZ-06 | yes | — |
| 50 | 1789050600 | TZ-06 | yes | — |
| 51 | 1789050900 | TZ-06 | yes | — |
| 52 | 1789051200 | TZ-06 | yes | — |
| 53 | 1789051500 | TZ-06 | yes | — |
| 54 | 1789051800 | TZ-06 | yes | — |
| 55 | 1789052100 | TZ-06 | yes | — |
| 56 | 1789052400 | TZ-06 | yes | — |
| 57 | 1789052700 | TZ-06 | yes | — |
| 58 | 1789053000 | TZ-06 | yes | — |
| 59 | 1789053300 | TZ-06 | yes | — |
| 60 | 1789053600 | TZ-06 | yes | — |
| 61 | 1789053900 | TZ-06 | yes | — |
| 62 | 1789054200 | TZ-06 | yes | — |
| 63 | 1789054500 | TZ-06 | yes | — |
| 64 | 1789054800 | TZ-06 | yes | — |
| 65 | 1789055100 | TZ-06 | yes | — |
| 66 | 1789055400 | TZ-06 | yes | — |
| 67 | 1789055700 | TZ-06 | yes | — |
| 68 | 1789056000 | TZ-06 | yes | — |
| 69 | 1789056300 | TZ-06 | yes | — |
| 70 | 1789056600 | TZ-06 | yes | — |
| 71 | 1789056900 | TZ-06 | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 72 | 1789057500 | TZ-06 | yes | — |
| 73 | 1789057800 | TZ-06 | yes | — |
| 74 | 1789058100 | TZ-06 | yes | — |
| 75 | 1789058400 | TZ-06 | yes | — |
| 76 | 1789058700 | TZ-06 | yes | — |
| 77 | 1789059000 | TZ-06 | yes | — |
| 78 | 1789059300 | TZ-06 | yes | — |
| 79 | 1789059600 | TZ-06 | yes | — |
| 80 | 1789059900 | TZ-06 | yes | — |
| 81 | 1789060200 | TZ-06 | yes | — |
| 82 | 1789060500 | TZ-06 | yes | — |
| 83 | 1789060800 | TZ-06 | yes | — |
| 84 | 1789061100 | TZ-06 | yes | — |
| 85 | 1789061400 | TZ-06 | yes | — |
| 86 | 1789061700 | TZ-06 | yes | — |
| 87 | 1789062000 | TZ-06 | yes | — |
| 88 | 1789062300 | TZ-06 | yes | — |
| 89 | 1789062600 | TZ-06 | yes | — |
| 90 | 1789062900 | TZ-06 | yes | — |
| 91 | 1789063200 | TZ-06 | yes | — |
| 92 | 1789063500 | TZ-06 | yes | — |
| 93 | 1789063800 | TZ-06 | yes | — |
| 94 | 1789064100 | TZ-06 | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 95 | 1789064700 | TZ-06 | yes | — |
| 96 | 1789065000 | TZ-06 | yes | — |
| 97 | 1789065300 | TZ-06 | yes | — |
| 98 | 1789065600 | TZ-06 | yes | — |
| 99 | 1789065900 | TZ-06 | yes | — |
| 100 | 1789066200 | TZ-06 | yes | — |
| 101 | 1789066500 | TZ-06 | yes | — |
| 102 | 1789066800 | TZ-06 | yes | — |
| 103 | 1789067100 | TZ-06 | yes | — |
| 104 | 1789067400 | TZ-06 | yes | — |
| 105 | 1789067700 | TZ-06 | yes | — |
| 106 | 1789068000 | TZ-06 | yes | — |
| 107 | 1789068300 | TZ-06 | yes | — |
| 108 | 1789068600 | TZ-06 | yes | — |
| 109 | 1789068900 | TZ-06 | yes | — |
| 110 | 1789069200 | TZ-06 | yes | — |
| 111 | 1789069500 | TZ-06 | yes | — |
| 112 | 1789069800 | TZ-06 | yes | — |
| 113 | 1789070100 | TZ-06 | yes | — |
| 114 | 1789070400 | TZ-06 | yes | — |
| 115 | 1789070700 | TZ-06 | yes | — |
| 116 | 1789071000 | TZ-06 | yes | — |
| 117 | 1789071300 | TZ-06 | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 118 | 1789071900 | TZ-06 | yes | — |
| 119 | 1789072200 | TZ-06 | yes | — |
| 120 | 1789072500 | TZ-06 | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 121 | 1789073100 | TZ-06 | yes | — |
| 122 | 1789073400 | TZ-06 | yes | — |
| 123 | 1789073700 | TZ-06 | yes | — |
| 124 | 1789074000 | TZ-06 | yes | — |
| 125 | 1789074300 | TZ-06 | yes | — |
| 126 | 1789074600 | TZ-06 | yes | — |
| 127 | 1789074900 | TZ-06 | yes | — |
| 128 | 1789075200 | TZ-06 | yes | — |
| 129 | 1789075500 | TZ-06 | yes | — |
| 130 | 1789075800 | TZ-06 | yes | — |
| 131 | 1789076100 | TZ-06 | yes | — |
| 132 | 1789076400 | TZ-06 | yes | — |
| 133 | 1789076700 | TZ-06 | yes | — |
| 134 | 1789077000 | TZ-06 | yes | — |
| 135 | 1789077300 | TZ-06 | yes | — |
| 136 | 1789077600 | TZ-06 | yes | — |
| 137 | 1789077900 | TZ-06 | yes | — |
| 138 | 1789078200 | TZ-06 | yes | — |
| 139 | 1789078500 | TZ-06 | yes | — |
| 140 | 1789078800 | TZ-06 | yes | — |
| 141 | 1789079100 | TZ-06 | yes | — |
| 142 | 1789079400 | TZ-06 | yes | — |
| 143 | 1789079700 | TZ-06 | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 144 | 1789080300 | TZ-06 | yes | — |
| 145 | 1789080600 | TZ-06 | yes | — |
| 146 | 1789080900 | TZ-06 | yes | — |
| 147 | 1789081200 | TZ-06 | yes | — |
| 148 | 1789081500 | TZ-06 | yes | — |
| 149 | 1789081800 | TZ-06 | yes | — |
| 150 | 1789082100 | TZ-06 | yes | — |
| 151 | 1789082400 | TZ-06 | yes | — |
| 152 | 1789082700 | TZ-06 | yes | — |
| 153 | 1789083000 | TZ-06 | yes | — |
| 154 | 1789083300 | TZ-06 | yes | — |
| 155 | 1789083600 | TZ-06 | yes | — |
| 156 | 1789083900 | TZ-06 | yes | — |
| 157 | 1789084200 | TZ-06 | yes | — |
| 158 | 1789084500 | TZ-06 | yes | — |
| 159 | 1789084800 | TZ-06 | yes | — |
| 160 | 1789085100 | TZ-06 | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 161 | 1789086000 | TZ-06 | yes | — |
| 162 | 1789086300 | TZ-06 | yes | — |
| 163 | 1789086600 | TZ-06 | yes | — |
| 164 | 1789086900 | TZ-06 | yes | — |
| 165 | 1789087200 | TZ-06 | yes | — |
| 166 | 1789087500 | TZ-06 | yes | — |
| 167 | 1789087800 | TZ-06 | yes | — |
| 168 | 1789088100 | TZ-06 | yes | — |
| 169 | 1789088400 | TZ-06 | yes | — |
| 170 | 1789088700 | TZ-06 | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 171 | 1789089600 | TZ-06 | yes | — |
| 172 | 1789089900 | TZ-06 | yes | — |
| 173 | 1789090200 | TZ-06 | yes | — |
| 174 | 1789090500 | TZ-06 | yes | — |
| 175 | 1789090800 | TZ-06 | yes | — |
| 176 | 1789091100 | TZ-06 | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 177 | 1789092000 | TZ-06 | yes | — |
| 178 | 1789092300 | TZ-06 | yes | — |
| 179 | 1789092600 | TZ-06 | yes | — |
| 180 | 1789092900 | TZ-06 | yes | — |
| 181 | 1789093200 | TZ-06 | yes | — |
| 182 | 1789093500 | TZ-06 | yes | — |
| 183 | 1789093800 | TZ-06 | yes | — |
| 184 | 1789094100 | TZ-06 | yes | — |
| 185 | 1789094400 | TZ-06 | yes | — |
| 186 | 1789094700 | TZ-06 | yes | — |
| 187 | 1789095000 | TZ-06 | yes | — |
| 188 | 1789095300 | TZ-06 | yes | — |
| 189 | 1789095600 | TZ-06 | yes | — |
| 190 | 1789095900 | TZ-06 | yes | — |
| 191 | 1789096200 | TZ-06 | yes | — |
| 192 | 1789096500 | TZ-06 | yes | — |
| 193 | 1789096800 | TZ-06 | yes | — |
| 194 | 1789097100 | TZ-06 | yes | — |
| 195 | 1789097400 | TZ-06 | yes | — |
| 196 | 1789097700 | TZ-06 | yes | — |
| 197 | 1789098000 | TZ-06 | yes | — |
| 198 | 1789098300 | TZ-06 | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 199 | 1789099200 | TZ-06 | yes | — |
| 200 | 1789099500 | TZ-06 | yes | — |
| 201 | 1789099800 | TZ-06 | yes | — |
| 202 | 1789100100 | TZ-06 | yes | — |
| 203 | 1789100400 | TZ-06 | yes | — |
| 204 | 1789100700 | TZ-06 | yes | — |
| 205 | 1789101000 | TZ-06 | yes | — |
| 206 | 1789101300 | TZ-06 | yes | — |
| 207 | 1789101600 | TZ-06 | yes | — |
| 208 | 1789101900 | TZ-06 | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 209 | 1789102500 | TZ-06 | yes | — |
| 210 | 1789102800 | TZ-06 | yes | — |
| 211 | 1789103100 | TZ-06 | yes | — |
| 212 | 1789103400 | TZ-06 | yes | — |
| 213 | 1789103700 | TZ-06 | yes | — |
| 214 | 1789104000 | TZ-06 | yes | — |
| 215 | 1789104300 | TZ-06 | yes | — |
| 216 | 1789104600 | TZ-06 | yes | — |
| 217 | 1789104900 | TZ-06 | yes | — |
| 218 | 1789105200 | TZ-06 | yes | — |
| 219 | 1789105500 | TZ-06 | yes | — |
| 220 | 1789105800 | TZ-06 | yes | — |
| 221 | 1789106100 | TZ-06 | yes | — |
| 222 | 1789106400 | TZ-06 | yes | — |
| 223 | 1789106700 | TZ-06 | yes | — |
| 224 | 1789107000 | TZ-06 | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 225 | 1789107900 | TZ-06 | yes | — |
| 226 | 1789108200 | TZ-06 | yes | — |
| 227 | 1789108500 | TZ-06 | yes | — |
| 228 | 1789108800 | TZ-06 | yes | — |
| 229 | 1789109100 | TZ-06 | yes | — |
| 230 | 1789109400 | TZ-06 | yes | — |
| 231 | 1789109700 | TZ-06 | yes | — |
| 232 | 1789110000 | TZ-06 | yes | — |
| 233 | 1789110300 | TZ-06 | yes | — |
| 234 | 1789110600 | TZ-06 | yes | — |
| 235 | 1789110900 | TZ-06 | yes | — |
| 236 | 1789111200 | TZ-06 | yes | — |
| 237 | 1789111500 | TZ-06 | yes | — |
| 238 | 1789111800 | TZ-06 | yes | — |
| 239 | 1789112100 | TZ-06 | yes | — |
| 240 | 1789112400 | TZ-06 | yes | — |
| 241 | 1789112700 | TZ-06 | yes | — |
| 242 | 1789113000 | TZ-06 | yes | — |
| 243 | 1789113300 | TZ-06 | yes | — |
| 244 | 1789113600 | TZ-06 | yes | — |
| 245 | 1789113900 | TZ-06 | yes | — |
| 246 | 1789114200 | TZ-06 | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 247 | 1789115100 | TZ-06 | yes | — |
| 248 | 1789115400 | TZ-06 | yes | — |
| 249 | 1789115700 | TZ-06 | yes | — |
| 250 | 1789116000 | TZ-06 | yes | — |
| 251 | 1789116300 | TZ-06 | yes | — |
| 252 | 1789116600 | TZ-06 | yes | — |
| 253 | 1789116900 | TZ-06 | yes | — |
| 254 | 1789117200 | TZ-06 | yes | — |
| 255 | 1789117500 | TZ-06 | yes | — |
| 256 | 1789117800 | TZ-06 | yes | — |
| 257 | 1789118100 | TZ-06 | yes | — |
| 258 | 1789118400 | TZ-06 | yes | — |
| 259 | 1789118700 | TZ-06 | yes | — |
| 260 | 1789119000 | TZ-06 | yes | — |
| 261 | 1789119300 | TZ-06 | yes | — |
| 262 | 1789119600 | TZ-06 | yes | — |
| 263 | 1789119900 | TZ-06 | yes | — |
| 264 | 1789120200 | TZ-06 | yes | — |
| 265 | 1789120500 | TZ-06 | yes | — |
| 266 | 1789120800 | TZ-06 | yes | — |
| 267 | 1789121100 | TZ-06 | yes | — |
| 268 | 1789121400 | TZ-06 | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 269 | 1789122300 | TZ-06 | yes | — |
| 270 | 1789122600 | TZ-06 | yes | — |
| 271 | 1789122900 | TZ-06 | yes | — |
| 272 | 1789123200 | TZ-06 | yes | — |
| 273 | 1789123500 | TZ-06 | yes | — |
| 274 | 1789123800 | TZ-06 | yes | — |
| 275 | 1789124100 | TZ-06 | yes | — |
| 276 | 1789124400 | TZ-06 | yes | — |
| 277 | 1789124700 | TZ-06 | yes | — |
| 278 | 1789125000 | TZ-06 | yes | — |
| 279 | 1789125300 | TZ-06 | yes | — |
| 280 | 1789125600 | TZ-06 | yes | — |
| 281 | 1789125900 | TZ-06 | yes | — |
| 282 | 1789126200 | TZ-06 | yes | — |
| 283 | 1789126500 | TZ-06 | yes | — |
| 284 | 1789126800 | TZ-06 | yes | — |
| 285 | 1789127100 | TZ-06 | yes | — |
| 286 | 1789127400 | TZ-06 | no | successor manifest not complete |
| 287 | 1789128300 | TZ-06 | yes | — |
| 288 | 1789128600 | TZ-06 | yes | — |
| 289 | 1789128900 | TZ-06 | yes | — |
| 290 | 1789129200 | TZ-06 | yes | — |
| 291 | 1789129500 | TZ-06 | yes | — |
| 292 | 1789129800 | TZ-06 | yes | — |
| 293 | 1789130100 | TZ-06 | yes | — |
| 294 | 1789130400 | TZ-06 | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 295 | 1789131600 | TZ-06 | yes | — |
| 296 | 1789131900 | TZ-06 | yes | — |
| 297 | 1789132200 | TZ-06 | yes | — |
| 298 | 1789132500 | TZ-06 | yes | — |
| 299 | 1789132800 | TZ-06 | yes | — |
| 300 | 1789133100 | TZ-06 | yes | — |
| 301 | 1789133400 | TZ-06 | yes | — |
| 302 | 1789133700 | TZ-06 | yes | — |
| 303 | 1789134000 | TZ-06 | yes | — |
| 304 | 1789134300 | TZ-06 | yes | — |
| 305 | 1789134600 | TZ-06 | yes | — |
| 306 | 1789134900 | TZ-06 | yes | — |
| 307 | 1789135200 | TZ-06 | yes | — |
| 308 | 1789135500 | TZ-06 | yes | — |
| 309 | 1789135800 | TZ-06 | yes | — |
| 310 | 1789136100 | TZ-06 | yes | — |
| 311 | 1789136400 | TZ-06 | yes | — |
| 312 | 1789136700 | TZ-06 | yes | — |
| 313 | 1789137000 | TZ-06 | yes | — |
| 314 | 1789137300 | TZ-06 | yes | — |
| 315 | 1789137600 | TZ-06 | yes | — |
| 316 | 1789137900 | TZ-06 | no | successor manifest not complete |
| 317 | 1789138800 | TZ-06 | yes | — |
| 318 | 1789139100 | TZ-06 | yes | — |
| 319 | 1789139400 | TZ-06 | yes | — |
| 320 | 1789139700 | TZ-06 | yes | — |
| 321 | 1789140000 | TZ-06 | yes | — |
| 322 | 1789140300 | TZ-06 | yes | — |
| 323 | 1789140600 | TZ-06 | yes | — |
| 324 | 1789140900 | TZ-06 | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 325 | 1789141800 | TZ-06 | yes | — |
| 326 | 1789142100 | TZ-06 | yes | — |
| 327 | 1789142400 | TZ-06 | yes | — |
| 328 | 1789142700 | TZ-06 | yes | — |
| 329 | 1789143000 | TZ-06 | yes | — |
| 330 | 1789143300 | TZ-06 | yes | — |
| 331 | 1789143600 | TZ-06 | yes | — |
| 332 | 1789143900 | TZ-06 | yes | — |
| 333 | 1789144200 | TZ-06 | yes | — |
| 334 | 1789144500 | TZ-06 | yes | — |
| 335 | 1789144800 | TZ-06 | yes | — |
| 336 | 1789145100 | TZ-06 | yes | — |
| 337 | 1789145400 | TZ-06 | yes | — |
| 338 | 1789145700 | TZ-06 | yes | — |
| 339 | 1789146000 | TZ-06 | yes | — |
| 340 | 1789146300 | TZ-06 | yes | — |
| 341 | 1789146600 | TZ-06 | yes | — |
| 342 | 1789146900 | TZ-06 | yes | — |
| 343 | 1789147200 | TZ-06 | yes | — |
| 344 | 1789147500 | TZ-06 | yes | — |
| 345 | 1789147800 | TZ-06 | yes | — |
| 346 | 1789148100 | TZ-06 | no | successor manifest not complete |
| 347 | 1789149000 | TZ-06 | yes | — |
| 348 | 1789149300 | TZ-06 | yes | — |
| 349 | 1789149600 | TZ-06 | yes | — |
| 350 | 1789149900 | TZ-06 | yes | — |
| 351 | 1789150200 | TZ-06 | yes | — |
| 352 | 1789150500 | TZ-06 | yes | — |
| 353 | 1789150800 | TZ-06 | yes | — |
| 354 | 1789151100 | TZ-06 | yes | — |
| 355 | 1789151400 | TZ-06 | yes | — |
| 356 | 1789151700 | TZ-06 | yes | — |
| 357 | 1789152000 | TZ-06 | yes | — |
| 358 | 1789152300 | TZ-06 | yes | — |
| 359 | 1789152600 | TZ-06 | yes | — |
| 360 | 1789152900 | TZ-06 | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 361 | 1789153800 | TZ-06 | yes | — |
| 362 | 1789154100 | TZ-06 | yes | — |
| 363 | 1789154400 | TZ-06 | yes | — |
| 364 | 1789154700 | TZ-06 | yes | — |
| 365 | 1789155000 | TZ-06 | yes | — |
| 366 | 1789155300 | TZ-06 | yes | — |
| 367 | 1789155600 | TZ-06 | yes | — |
| 368 | 1789155900 | TZ-06 | yes | — |
| 369 | 1789156200 | TZ-06 | yes | — |
| 370 | 1789156500 | TZ-06 | yes | — |
| 371 | 1789156800 | TZ-06 | yes | — |
| 372 | 1789157100 | TZ-06 | yes | — |
| 373 | 1789157400 | TZ-06 | yes | — |
| 374 | 1789157700 | TZ-06 | yes | — |
| 375 | 1789158000 | TZ-06 | yes | — |
| 376 | 1789158300 | TZ-06 | yes | — |
| 377 | 1789158600 | TZ-06 | yes | — |
| 378 | 1789158900 | TZ-06 | yes | — |
| 379 | 1789159200 | TZ-06 | yes | — |
| 380 | 1789159500 | TZ-06 | yes | — |
| 381 | 1789159800 | TZ-06 | yes | — |
| 382 | 1789160100 | TZ-06 | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 383 | 1789161000 | TZ-06 | yes | — |
| 384 | 1789161300 | TZ-06 | yes | — |
| 385 | 1789161600 | TZ-06 | yes | — |
| 386 | 1789161900 | TZ-06 | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 387 | 1789162500 | TZ-06 | yes | — |
| 388 | 1789162800 | TZ-06 | yes | — |
| 389 | 1789163100 | TZ-06 | yes | — |
| 390 | 1789163400 | TZ-06 | yes | — |
| 391 | 1789163700 | TZ-06 | yes | — |
| 392 | 1789164000 | TZ-06 | yes | — |
| 393 | 1789164300 | TZ-06 | yes | — |
| 394 | 1789164600 | TZ-06 | yes | — |
| 395 | 1789164900 | TZ-06 | yes | — |
| 396 | 1789165200 | TZ-06 | yes | — |
| 397 | 1789165500 | TZ-06 | yes | — |
| 398 | 1789165800 | TZ-06 | yes | — |
| 399 | 1789166100 | TZ-06 | yes | — |
| 400 | 1789166400 | TZ-06 | yes | — |
| 401 | 1789166700 | TZ-08a | yes | — |
| 402 | 1789167000 | TZ-08a | yes | — |
| 403 | 1789167300 | TZ-08a | yes | — |
| 404 | 1789167600 | TZ-08a | yes | — |
| 405 | 1789167900 | TZ-08a | yes | — |
| 406 | 1789168200 | TZ-08a | yes | — |
| 407 | 1789168500 | TZ-08a | yes | — |
| 408 | 1789168800 | TZ-08a | yes | — |
| 409 | 1789169100 | TZ-08a | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 410 | 1789169700 | TZ-08a | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 411 | 1789170600 | TZ-08a | yes | — |
| 412 | 1789170900 | TZ-08a | yes | — |
| 413 | 1789171200 | TZ-08a | yes | — |
| 414 | 1789171500 | TZ-08a | yes | — |
| 415 | 1789171800 | TZ-08a | yes | — |
| 416 | 1789172100 | TZ-08a | yes | — |
| 417 | 1789172400 | TZ-08a | yes | — |
| 418 | 1789172700 | TZ-08a | yes | — |
| 419 | 1789173000 | TZ-08a | yes | — |
| 420 | 1789173300 | TZ-08a | yes | — |
| 421 | 1789173600 | TZ-08a | yes | — |
| 422 | 1789173900 | TZ-08a | yes | — |
| 423 | 1789174200 | TZ-08a | yes | — |
| 424 | 1789174500 | TZ-08a | yes | — |
| 425 | 1789174800 | TZ-08a | yes | — |
| 426 | 1789175100 | TZ-08a | yes | — |
| 427 | 1789175400 | TZ-08a | yes | — |
| 428 | 1789175700 | TZ-08a | yes | — |
| 429 | 1789176000 | TZ-08a | yes | — |
| 430 | 1789176300 | TZ-08a | yes | — |
| 431 | 1789176600 | TZ-08a | yes | — |
| 432 | 1789176900 | TZ-08a | no | successor manifest not complete |
| 433 | 1789177800 | TZ-08a | yes | — |
| 434 | 1789178100 | TZ-08a | yes | — |
| 435 | 1789178400 | TZ-08a | yes | — |
| 436 | 1789178700 | TZ-08a | yes | — |
| 437 | 1789179000 | TZ-08a | yes | — |
| 438 | 1789179300 | TZ-08a | yes | — |
| 439 | 1789179600 | TZ-08a | yes | — |
| 440 | 1789179900 | TZ-08a | yes | — |
| 441 | 1789180200 | TZ-08a | yes | — |
| 442 | 1789180500 | TZ-08a | yes | — |
| 443 | 1789180800 | TZ-08a | yes | — |
| 444 | 1789181100 | TZ-08a | yes | — |
| 445 | 1789181400 | TZ-08a | yes | — |
| 446 | 1789181700 | TZ-08a | yes | — |
| 447 | 1789182000 | TZ-08a | yes | — |
| 448 | 1789182300 | TZ-08a | yes | — |
| 449 | 1789182600 | TZ-08a | yes | — |
| 450 | 1789182900 | TZ-08a | yes | — |
| 451 | 1789183200 | TZ-08a | yes | — |
| 452 | 1789183500 | TZ-08a | yes | — |
| 453 | 1789183800 | TZ-08a | yes | — |
| 454 | 1789184100 | TZ-08a | no | successor manifest not complete |
| 455 | 1789185000 | TZ-08a | yes | — |
| 456 | 1789185300 | TZ-08a | yes | — |
| 457 | 1789185600 | TZ-08a | yes | — |
| 458 | 1789185900 | TZ-08a | yes | — |
| 459 | 1789186200 | TZ-08a | yes | — |
| 460 | 1789186500 | TZ-08a | yes | — |
| 461 | 1789186800 | TZ-08a | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 462 | 1789187700 | TZ-08a | yes | — |
| 463 | 1789188000 | TZ-08a | yes | — |
| 464 | 1789188300 | TZ-08a | yes | — |
| 465 | 1789188600 | TZ-08a | yes | — |
| 466 | 1789188900 | TZ-08a | yes | — |
| 467 | 1789189200 | TZ-08a | yes | — |
| 468 | 1789189500 | TZ-08a | yes | — |
| 469 | 1789189800 | TZ-08a | yes | — |
| 470 | 1789190100 | TZ-08a | yes | — |
| 471 | 1789190400 | TZ-08a | yes | — |
| 472 | 1789190700 | TZ-08a | yes | — |
| 473 | 1789191000 | TZ-08a | yes | — |
| 474 | 1789191300 | TZ-08a | yes | — |
| 475 | 1789191600 | TZ-08a | yes | — |
| 476 | 1789191900 | TZ-08a | yes | — |
| 477 | 1789192200 | TZ-08a | yes | — |
| 478 | 1789192500 | TZ-08a | yes | — |
| 479 | 1789192800 | TZ-08a | yes | — |
| 480 | 1789193100 | TZ-08a | yes | — |
| 481 | 1789193400 | TZ-08a | yes | — |
| 482 | 1789193700 | TZ-08a | yes | — |
| 483 | 1789194000 | TZ-08a | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 484 | 1789194900 | TZ-08a | yes | — |
| 485 | 1789195200 | TZ-08a | yes | — |
| 486 | 1789195500 | TZ-08a | yes | — |
| 487 | 1789195800 | TZ-08a | yes | — |
| 488 | 1789196100 | TZ-08a | yes | — |
| 489 | 1789196400 | TZ-08a | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 490 | 1789197000 | TZ-08a | yes | — |
| 491 | 1789197300 | TZ-08a | yes | — |
| 492 | 1789197600 | TZ-08a | yes | — |
| 493 | 1789197900 | TZ-08a | yes | — |
| 494 | 1789198200 | TZ-08a | yes | — |
| 495 | 1789198500 | TZ-08a | yes | — |
| 496 | 1789198800 | TZ-08a | yes | — |
| 497 | 1789199100 | TZ-08a | yes | — |
| 498 | 1789199400 | TZ-08a | yes | — |
| 499 | 1789199700 | TZ-08a | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 500 | 1789200300 | TZ-08a | yes | — |
| 501 | 1789200600 | TZ-08a | yes | — |
| 502 | 1789200900 | TZ-08a | yes | — |
| 503 | 1789201200 | TZ-08a | yes | — |
| 504 | 1789201500 | TZ-08a | yes | — |
| 505 | 1789201800 | TZ-08a | yes | — |
| 506 | 1789202100 | TZ-08a | yes | — |
| 507 | 1789202400 | TZ-08a | yes | — |
| 508 | 1789202700 | TZ-08a | yes | — |
| 509 | 1789203000 | TZ-08a | yes | — |
| 510 | 1789203300 | TZ-08a | yes | — |
| 511 | 1789203600 | TZ-08a | yes | — |
| 512 | 1789203900 | TZ-08a | yes | — |
| 513 | 1789204200 | TZ-08a | yes | — |
| 514 | 1789204500 | TZ-08a | yes | — |
| 515 | 1789204800 | TZ-08a | yes | — |
| 516 | 1789205100 | TZ-08a | yes | — |
| 517 | 1789205400 | TZ-08a | yes | — |
| 518 | 1789205700 | TZ-08a | yes | — |
| 519 | 1789206000 | TZ-08a | yes | — |
| 520 | 1789206300 | TZ-08a | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 521 | 1789206900 | TZ-08a | yes | — |
| 522 | 1789207200 | TZ-08a | yes | — |
| 523 | 1789207500 | TZ-08a | yes | — |
| 524 | 1789207800 | TZ-08a | yes | — |
| 525 | 1789208100 | TZ-08a | yes | — |
| 526 | 1789208400 | TZ-08a | yes | — |
| 527 | 1789208700 | TZ-08a | yes | — |
| 528 | 1789209000 | TZ-08a | yes | — |
| 529 | 1789209300 | TZ-08a | yes | — |
| 530 | 1789209600 | TZ-08a | yes | — |
| 531 | 1789209900 | TZ-08a | yes | — |
| 532 | 1789210200 | TZ-08a | yes | — |
| 533 | 1789210500 | TZ-08a | yes | — |
| 534 | 1789210800 | TZ-08a | yes | — |
| 535 | 1789211100 | TZ-08a | yes | — |
| 536 | 1789211400 | TZ-08a | yes | — |
| 537 | 1789211700 | TZ-08a | yes | — |
| 538 | 1789212000 | TZ-08a | yes | — |
| 539 | 1789212300 | TZ-08a | yes | — |
| 540 | 1789212600 | TZ-08a | yes | — |
| 541 | 1789212900 | TZ-08a | yes | — |
| 542 | 1789213200 | TZ-08a | yes | — |
| 543 | 1789213500 | TZ-08a | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 544 | 1789214100 | TZ-08a | yes | — |
| 545 | 1789214400 | TZ-08a | yes | — |
| 546 | 1789214700 | TZ-08a | yes | — |
| 547 | 1789215000 | TZ-08a | yes | — |
| 548 | 1789215300 | TZ-08a | yes | — |
| 549 | 1789215600 | TZ-08a | yes | — |
| 550 | 1789215900 | TZ-08a | yes | — |
| 551 | 1789216200 | TZ-08a | yes | — |
| 552 | 1789216500 | TZ-08a | yes | — |
| 553 | 1789216800 | TZ-08a | yes | — |
| 554 | 1789217100 | TZ-08a | yes | — |
| 555 | 1789217400 | TZ-08a | yes | — |
| 556 | 1789217700 | TZ-08a | yes | — |
| 557 | 1789218000 | TZ-08a | yes | — |
| 558 | 1789218300 | TZ-08a | yes | — |
| 559 | 1789218600 | TZ-08a | yes | — |
| 560 | 1789218900 | TZ-08a | yes | — |
| 561 | 1789219200 | TZ-08a | yes | — |
| 562 | 1789219500 | TZ-08a | yes | — |
| 563 | 1789219800 | TZ-08a | yes | — |
| 564 | 1789220100 | TZ-08a | yes | — |
| 565 | 1789220400 | TZ-08a | yes | — |
| 566 | 1789220700 | TZ-08a | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 567 | 1789221300 | TZ-08a | yes | — |
| 568 | 1789221600 | TZ-08a | yes | — |
| 569 | 1789221900 | TZ-08a | yes | — |
| 570 | 1789222200 | TZ-08a | yes | — |
| 571 | 1789222500 | TZ-08a | yes | — |
| 572 | 1789222800 | TZ-08a | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 573 | 1789223700 | TZ-08a | yes | — |
| 574 | 1789224000 | TZ-08a | yes | — |
| 575 | 1789224300 | TZ-08a | yes | — |
| 576 | 1789224600 | TZ-08a | yes | — |
| 577 | 1789224900 | TZ-08a | yes | — |
| 578 | 1789225200 | TZ-08a | yes | — |
| 579 | 1789225500 | TZ-08a | yes | — |
| 580 | 1789225800 | TZ-08a | yes | — |
| 581 | 1789226100 | TZ-08a | yes | — |
| 582 | 1789226400 | TZ-08a | yes | — |
| 583 | 1789226700 | TZ-08a | yes | — |
| 584 | 1789227000 | TZ-08a | yes | — |
| 585 | 1789227300 | TZ-08a | yes | — |
| 586 | 1789227600 | TZ-08a | yes | — |
| 587 | 1789227900 | TZ-08a | yes | — |
| 588 | 1789228200 | TZ-08a | yes | — |
| 589 | 1789228500 | TZ-08a | yes | — |
| 590 | 1789228800 | TZ-08a | yes | — |
| 591 | 1789229100 | TZ-08a | yes | — |
| 592 | 1789229400 | TZ-08a | yes | — |
| 593 | 1789229700 | TZ-08a | yes | — |
| 594 | 1789230000 | TZ-08a | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 595 | 1789230900 | TZ-08a | yes | — |
| 596 | 1789231200 | TZ-08a | yes | — |
| 597 | 1789231500 | TZ-08a | yes | — |
| 598 | 1789231800 | TZ-08a | yes | — |
| 599 | 1789232100 | TZ-08a | yes | — |
| 600 | 1789232400 | TZ-08a | yes | — |
| 601 | 1789232700 | TZ-08a | yes | — |
| 602 | 1789233000 | TZ-08a | yes | — |
| 603 | 1789233300 | TZ-08a | yes | — |
| 604 | 1789233600 | TZ-08a | yes | — |
| 605 | 1789233900 | TZ-08a | yes | — |
| 606 | 1789234200 | TZ-08a | yes | — |
| 607 | 1789234500 | TZ-08a | yes | — |
| 608 | 1789234800 | TZ-08a | yes | — |
| 609 | 1789235100 | TZ-08a | yes | — |
| 610 | 1789235400 | TZ-08a | yes | — |
| 611 | 1789235700 | TZ-08a | yes | — |
| 612 | 1789236000 | TZ-08a | yes | — |
| 613 | 1789236300 | TZ-08a | yes | — |
| 614 | 1789236600 | TZ-08a | yes | — |
| 615 | 1789236900 | TZ-08a | yes | — |
| 616 | 1789237200 | TZ-08a | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 617 | 1789238100 | TZ-08a | yes | — |
| 618 | 1789238400 | TZ-08a | yes | — |
| 619 | 1789238700 | TZ-08a | yes | — |
| 620 | 1789239000 | TZ-08a | yes | — |
| 621 | 1789239300 | TZ-08a | yes | — |
| 622 | 1789239600 | TZ-08a | yes | — |
| 623 | 1789239900 | TZ-08a | yes | — |
| 624 | 1789240200 | TZ-08a | yes | — |
| 625 | 1789240500 | TZ-08a | yes | — |
| 626 | 1789240800 | TZ-08a | yes | — |
| 627 | 1789241100 | TZ-08a | yes | — |
| 628 | 1789241400 | TZ-08a | yes | — |
| 629 | 1789241700 | TZ-08a | yes | — |
| 630 | 1789242000 | TZ-08a | yes | — |
| 631 | 1789242300 | TZ-08a | yes | — |
| 632 | 1789242600 | TZ-08a | yes | — |
| 633 | 1789242900 | TZ-08a | yes | — |
| 634 | 1789243200 | TZ-08a | yes | — |
| 635 | 1789243500 | TZ-08a | yes | — |
| 636 | 1789243800 | TZ-08a | yes | — |
| 637 | 1789244100 | TZ-08a | yes | — |
| 638 | 1789244400 | TZ-08a | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 639 | 1789245300 | TZ-08a | yes | — |
| 640 | 1789245600 | TZ-08a | yes | — |
| 641 | 1789245900 | TZ-08a | yes | — |
| 642 | 1789246200 | TZ-08a | yes | — |
| 643 | 1789246500 | TZ-08a | yes | — |
| 644 | 1789246800 | TZ-08a | yes | — |
| 645 | 1789247100 | TZ-08a | yes | — |
| 646 | 1789247400 | TZ-08a | yes | — |
| 647 | 1789247700 | TZ-08a | yes | — |
| 648 | 1789248000 | TZ-08a | yes | — |
| 649 | 1789248300 | TZ-08a | yes | — |
| 650 | 1789248600 | TZ-08a | yes | — |
| 651 | 1789248900 | TZ-08a | yes | — |
| 652 | 1789249200 | TZ-08a | yes | — |
| 653 | 1789249500 | TZ-08a | yes | — |
| 654 | 1789249800 | TZ-08a | yes | — |
| 655 | 1789250100 | TZ-08a | yes | — |
| 656 | 1789250400 | TZ-08a | yes | — |
| 657 | 1789250700 | TZ-08a | yes | — |
| 658 | 1789251000 | TZ-08a | yes | — |
| 659 | 1789251300 | TZ-08a | yes | — |
| 660 | 1789251600 | TZ-08a | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 661 | 1789252800 | TZ-08a | yes | — |
| 662 | 1789253100 | TZ-08a | yes | — |
| 663 | 1789253400 | TZ-08a | yes | — |
| 664 | 1789253700 | TZ-08a | yes | — |
| 665 | 1789254000 | TZ-08a | yes | — |
| 666 | 1789254300 | TZ-08a | yes | — |
| 667 | 1789254600 | TZ-08a | yes | — |
| 668 | 1789254900 | TZ-08a | yes | — |
| 669 | 1789255200 | TZ-08a | yes | — |
| 670 | 1789255500 | TZ-08a | yes | — |
| 671 | 1789255800 | TZ-08a | yes | — |
| 672 | 1789256100 | TZ-08a | yes | — |
| 673 | 1789256400 | TZ-08a | yes | — |
| 674 | 1789256700 | TZ-08a | yes | — |
| 675 | 1789257000 | TZ-08a | yes | — |
| 676 | 1789257300 | TZ-08a | yes | — |
| 677 | 1789257600 | TZ-08a | yes | — |
| 678 | 1789257900 | TZ-08a | yes | — |
| 679 | 1789258200 | TZ-08a | yes | — |
| 680 | 1789258500 | TZ-08a | yes | — |
| 681 | 1789258800 | TZ-08a | yes | — |
| 682 | 1789259100 | TZ-08a | yes | — |
| 683 | 1789259400 | TZ-08a | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 684 | 1789260000 | TZ-08a | yes | — |
| 685 | 1789260300 | TZ-08a | yes | — |
| 686 | 1789260600 | TZ-08a | yes | — |
| 687 | 1789260900 | TZ-08a | yes | — |
| 688 | 1789261200 | TZ-08a | yes | — |
| 689 | 1789261500 | TZ-08a | yes | — |
| 690 | 1789261800 | TZ-08a | yes | — |
| 691 | 1789262100 | TZ-08a | yes | — |
| 692 | 1789262400 | TZ-08a | yes | — |
| 693 | 1789262700 | TZ-08a | yes | — |
| 694 | 1789263000 | TZ-08a | yes | — |
| 695 | 1789263300 | TZ-08a | yes | — |
| 696 | 1789263600 | TZ-08a | yes | — |
| 697 | 1789263900 | TZ-08a | yes | — |
| 698 | 1789264200 | TZ-08a | yes | — |
| 699 | 1789264500 | TZ-08a | yes | — |
| 700 | 1789264800 | TZ-08a | yes | — |
| 701 | 1789265100 | TZ-08a | yes | — |
| 702 | 1789265400 | TZ-08a | yes | — |
| 703 | 1789265700 | TZ-08a | yes | — |
| 704 | 1789266000 | TZ-08a | yes | — |
| 705 | 1789266300 | TZ-08a | yes | — |
| 706 | 1789266600 | TZ-08a | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 707 | 1789267200 | TZ-08a | yes | — |
| 708 | 1789267500 | TZ-08a | yes | — |
| 709 | 1789267800 | TZ-08a | yes | — |
| 710 | 1789268100 | TZ-08a | yes | — |
| 711 | 1789268400 | TZ-08a | yes | — |
| 712 | 1789268700 | TZ-08a | yes | — |
| 713 | 1789269000 | TZ-08a | yes | — |
| 714 | 1789269300 | TZ-08a | yes | — |
| 715 | 1789269600 | TZ-08a | yes | — |
| 716 | 1789269900 | TZ-08a | yes | — |
| 717 | 1789270200 | TZ-08a | yes | — |
| 718 | 1789270500 | TZ-08a | yes | — |
| 719 | 1789270800 | TZ-08a | yes | — |
| 720 | 1789271100 | TZ-08a | yes | — |
| 721 | 1789271400 | TZ-08a | yes | — |
| 722 | 1789271700 | TZ-08a | yes | — |
| 723 | 1789272000 | TZ-08a | yes | — |
| 724 | 1789272300 | TZ-08a | yes | — |
| 725 | 1789272600 | TZ-08a | yes | — |
| 726 | 1789272900 | TZ-08a | yes | — |
| 727 | 1789273200 | TZ-08a | yes | — |
| 728 | 1789273500 | TZ-08a | yes | — |
| 729 | 1789273800 | TZ-08a | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 730 | 1789274400 | TZ-08a | yes | — |
| 731 | 1789274700 | TZ-08a | yes | — |
| 732 | 1789275000 | TZ-08a | yes | — |
| 733 | 1789275300 | TZ-08a | yes | — |
| 734 | 1789275600 | TZ-08a | yes | — |
| 735 | 1789275900 | TZ-08a | yes | — |
| 736 | 1789276200 | TZ-08a | yes | — |
| 737 | 1789276500 | TZ-08a | yes | — |
| 738 | 1789276800 | TZ-08a | yes | — |
| 739 | 1789277100 | TZ-08a | yes | — |
| 740 | 1789277400 | TZ-08a | yes | — |
| 741 | 1789277700 | TZ-08a | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 742 | 1789278300 | TZ-08a | yes | — |
| 743 | 1789278600 | TZ-08a | yes | — |
| 744 | 1789278900 | TZ-08a | yes | — |
| 745 | 1789279200 | TZ-08a | yes | — |
| 746 | 1789279500 | TZ-08a | yes | — |
| 747 | 1789279800 | TZ-08a | yes | — |
| 748 | 1789280100 | TZ-08a | yes | — |
| 749 | 1789280400 | TZ-08a | yes | — |
| 750 | 1789280700 | TZ-08a | yes | — |
| 751 | 1789281000 | TZ-08a | yes | — |
| 752 | 1789281300 | TZ-08a | yes | — |
| 753 | 1789281600 | TZ-08a | yes | — |
| 754 | 1789281900 | TZ-08a | yes | — |
| 755 | 1789282200 | TZ-08a | yes | — |
| 756 | 1789282500 | TZ-08a | yes | — |
| 757 | 1789282800 | TZ-08a | yes | — |
| 758 | 1789283100 | TZ-08a | yes | — |
| 759 | 1789283400 | TZ-08a | yes | — |
| 760 | 1789283700 | TZ-08a | yes | — |
| 761 | 1789284000 | TZ-08a | yes | — |
| 762 | 1789284300 | TZ-08a | yes | — |
| 763 | 1789284600 | TZ-08a | yes | — |
| 764 | 1789284900 | TZ-08a | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 765 | 1789285500 | TZ-08a | yes | — |
| 766 | 1789285800 | TZ-08a | yes | — |
| 767 | 1789286100 | TZ-08a | yes | — |
| 768 | 1789286400 | TZ-08a | yes | — |
| 769 | 1789286700 | TZ-08a | yes | — |
| 770 | 1789287000 | TZ-08a | yes | — |
| 771 | 1789287300 | TZ-08a | yes | — |
| 772 | 1789287600 | TZ-08a | yes | — |
| 773 | 1789287900 | TZ-08a | yes | — |
| 774 | 1789288200 | TZ-08a | yes | — |
| 775 | 1789288500 | TZ-08a | yes | — |
| 776 | 1789288800 | TZ-08a | yes | — |
| 777 | 1789289100 | TZ-08a | yes | — |
| 778 | 1789289400 | TZ-08a | yes | — |
| 779 | 1789289700 | TZ-08a | yes | — |
| 780 | 1789290000 | TZ-08a | yes | — |
| 781 | 1789290300 | TZ-08a | yes | — |
| 782 | 1789290600 | TZ-08a | yes | — |
| 783 | 1789290900 | TZ-08a | yes | — |
| 784 | 1789291200 | TZ-08a | yes | — |
| 785 | 1789291500 | TZ-08a | yes | — |
| 786 | 1789291800 | TZ-08a | yes | — |
| 787 | 1789292100 | TZ-08a | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |
| 788 | 1789292700 | TZ-08a | yes | — |
| 789 | 1789293000 | TZ-08a | yes | — |
| 790 | 1789293300 | TZ-08a | yes | — |
| 791 | 1789293600 | TZ-08a | yes | — |
| 792 | 1789293900 | TZ-08a | yes | — |
| 793 | 1789294200 | TZ-08a | yes | — |
| 794 | 1789294500 | TZ-08a | yes | — |
| 795 | 1789294800 | TZ-08a | yes | — |
| 796 | 1789295100 | TZ-08a | yes | — |
| 797 | 1789295400 | TZ-08a | yes | — |
| 798 | 1789295700 | TZ-08a | yes | — |
| 799 | 1789296000 | TZ-08a | yes | — |
| 800 | 1789296300 | TZ-08a | no | successor manifest not complete + disconnect inside [T0+300, T0+600] |

### V11 — influence

Every `λ̂` in M2, all 84 of them, is printed with its value recomputed without its single most
influential observation. That observation is the one whose removal moves `λ̂` furthest, found by
removing each observation in turn and searching again. It is named by `T0` in the tables of §1.2,
with its label and `z`. There is no condition on these numbers, so they are **recorded, not
asserted**. At `tau = 30`, under `sigma_hat` and under `sigma_post`, the pooled table's most influential
observation is `T0 1789268400`, the observation M5 reports. §6 item 6 lists every value that
lands on a bound of the search interval, with or without its most influential observation.

---

## 5. Publication

- **Branch.** `tz-10b-sigma-or-link`, one commit, `d34606ee9a592e51293eaad0996c7cae3b84dfcd`, pushed to `origin`. After the
  push, `git ls-remote origin tz-10b-sigma-or-link` printed:

  ```
  d34606ee9a592e51293eaad0996c7cae3b84dfcd	refs/heads/tz-10b-sigma-or-link
  ```

- **Pull request.** https://github.com/seahomebatumi-ai/btc-5m-twap/pull/11, opened with `gh pr create` against `main`. **It is not merged:**
  merge is the Boss's, after the Architect's verdict.
- **No Release.** No dataset, archive or binary entered git history, and the third command below
  prints nothing.
- **This report** is the only path the run adds to `main`, in one commit.

**The separation self-check of contract §4.2, verbatim.** It was run after the branch was pushed
and before this report was committed. `/root/tz10b-work/separation.py` runs the three commands as
the contract writes them and asserts each result:

- the first prints `0`;
- the second lists the three implementation files and nothing else;
- the third prints nothing.

```
$ git rev-list origin/main | grep -c d34606ee9a592e51293eaad0996c7cae3b84dfcd
0
$ git diff --name-only origin/main origin/tz-10b-sigma-or-link
research/pfair.py
research/selftest-pfair.py
research/tz10b-sigma-or-link.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
```

**§9, first: the three scratch files committed reports name by SHA-256, preserved before
anything was reclaimed.** `/root/tz10b-work/copy-forensics.py` did the copying. It asserts each
hash at both ends and asserts that every file already in `/root/btc-forensics/` is unchanged.

| source | destination in `/root/btc-forensics/` | bytes | SHA-256 at the source | SHA-256 at the destination | equal to the hash its report names |
|---|---|---|---|---|---|
| `/root/tz10-work/probe-log-phi.py` | `tz10-work--probe-log-phi.py` | 2,685 | `5eef7ae91f1ac0fbd70b2b6b724c6f4688194c537f3c09d89f42d3b2298fd481` | `5eef7ae91f1ac0fbd70b2b6b724c6f4688194c537f3c09d89f42d3b2298fd481` | yes |
| `/root/tz10a-work/probe-v2.py` | `tz10a-work--probe-v2.py` | 3,657 | `523cfca70e32d7f19357fd6a3023c19fd79b56c20d16651ca06d5e6f30508468` | `523cfca70e32d7f19357fd6a3023c19fd79b56c20d16651ca06d5e6f30508468` | yes |
| `/root/tz10a-work/probe-selftests.py` | `tz10a-work--probe-selftests.py` | 2,917 | `b67ee8b24a103a38467b69d7df424309862a5567e07d6340a53d527d37a4e747` | `b67ee8b24a103a38467b69d7df424309862a5567e07d6340a53d527d37a4e747` | yes |

Copied at 2026-09-14T11:08:46Z. `/root/btc-forensics/` held **91** files before and **94** after; **91 of 91** of the files already there hash exactly as before.

**§9, then: the two trees reclaimed, one command each, as the retention rule directs.**

Each removal was one command naming one tree, and **neither was refused** by the permission
classifier. This was the single-tree case §9 says had not been tested: TZ-09's refused removal
named five trees in one command.

| tree | what it held — file (apparent bytes) | on disk before | command | refused | `test -e` at 2026-09-14T11:09:47Z |
|---|---|---|---|---|---|
| `/root/tz10-work` | `probe-log-phi.py` (2,685) | 8,192 | `rm -rf /root/tz10-work` | no | absent |
| `/root/tz10a-work` | `assemble-report.py` (3,005), `preflight2.txt` (123), `probe-selftests.py` (2,917), `probe-v2.py` (3,657), `report-draft.md` (20,128) | 40,960 | `rm -rf /root/tz10a-work` | no | absent |

`49,152` bytes on disk were recovered. Of the files these trees held, the three that a committed
report names by SHA-256 were copied first (above). After the removals the three copies still hash
to the named values, and `/root/btc-forensics/` holds 94 files.

**`/root/tz10b-work/`** is reclaimed by the next TZ once this report is on `main`, on the same
terms. The files this report names by SHA-256 are the three deterministic outputs of each full
run (V3) and the observations file at the path §5.1 names (§1.6). A copy of each goes to
`/root/btc-forensics/` first.

---

## 6. What could not be implemented as written, and every reading chosen

Each item below says where it sits and what was done. The first is the only one on which a
check's verdict turns.

1. **V7's λ̂ comparison — a reading on which the check turns.**
   - V7 fixes: "compared against TZ-08a's `2.0418` and expected to agree past the sixth
     decimal".
   - The committed search returns `2.0418426092` with `log(phi(...))` and `2.0418435851` with
     `log_phi`, a difference of `+9.759e-07`.
   - Three readings are possible:
     - (a) the difference is below `1e-6` — this passes;
     - (b) the two values are equal once each is rounded to six decimals — this **fails**,
       `2.041843` against `2.041844`;
     - (c) they are equal at the four decimals TZ-10b quotes — this passes.
   - **The run asserts (a).** Map §7 item 26 records exactly this pair, "2.041843 against
     2.041844 evaluated tail-accurately", and calls `λ̂` "unaffected past its sixth decimal". So
     the expectation V7 writes is the relation the map already states between these two numbers.
   - If the Architect meant (b), V7 fails as written and this run is BLOCKED at V7. No other
     check reads V7's comparison.
2. **`sigma_win` is zero at 22 admissible anchors.**
   - Where: all at `tau = 10`, in `1789276200` (11) and `1789276500` (11).
   - Why: the feed did not change across `[a, a + 10]`. So `sigma_win` is 0, `Y` is 0 too, and
     `u` is `0 / 0`, which has no value.
   - TZ-10b gives the `sigma_win` arm no admissibility rule. Those anchors are left out of that
     arm alone, and counted and listed under M1.
   - The other two arms keep them, the intersection is formed by the `sigma_post` rule only, and
     no reading of §4 reads `sigma_win`.
   - At the checkpoint, which is what M2 scores, 0 observations have a flat span.
3. **§2 against §9 on `/root/btc-forensics/`.**
   - §2 lists `/root/btc-forensics/` under "may not be touched", and §9 requires three files to be
     copied into it.
   - §9 was read as the one named exception: those three files were added, and nothing else. Each
     was written by exclusive create (`open(…, "xb")`), which cannot overwrite a file.
   - Every file already there is unchanged, and §5 shows the hash listing before and after.
   - This is the class of map §7 item 23: a prohibition that does not name its exemption.
4. **§3.2 writes `corrected_sd(s, tau)`.** That is the argument order map §7 item 39 corrected,
   and §2 states the committed signature, `corrected_sd(tau, sigma)`, in words. §2 was followed:
   every call is `pfair.corrected_sd(tau, s)`.
5. **How `λ̂` gets its `log_phi` likelihood.**
   - §3.2 requires TZ-07a §8's scale statistic with a `log_phi` likelihood. The committed
     `tz07a.lambda_hat` reaches its likelihood through the module-level name `log_likelihood`.
   - For the length of each call, the instrument binds that name to its own `log_phi` form and
     restores it in a `finally`. So the search, the interval `[0.5, 3.0]`, the tolerance `1e-9` and
     the fields returned are all the committed ones.
   - Restoration is asserted before V7 calls the original. No file is modified; the alternative
     was a second copy of the search.
6. **"Most influential observation"** is not defined by §3.2 or V11.
   - Read as the observation whose removal moves `λ̂` furthest, by exact leave-one-out with a new
     search per removal. On a tie, the first in `T0` order.
   - None of the 84 `λ̂` sit on a bound of the search interval `[0.5, 3.0]`. Recomputed without the most influential observation, 7 land on one: `sigma_hat` on the full TZ-06 400 at `tau = 30` (0.500000); `sigma_hat` on the full TZ-08a 400 at `tau = 10` (0.500000); `sigma_hat` on the intersection's TZ-06 share at `tau = 30` (0.500000); `sigma_hat` on the intersection's TZ-08a share at `tau = 10` (0.500000); `sigma_post` on the intersection's TZ-06 share at `tau = 30` (0.500000); `sigma_post` on the intersection's TZ-08a share at `tau = 10` (0.500000); `sigma_win` on the intersection's TZ-08a share at `tau = 30` (0.500000). A value on a bound is the edge of the search, not an interior maximiser.
7. **Deciles in M3.**
   - Read as ten equal-count groups of the intersection's members, ranked by the stratifier at
     that `tau`. Member `k` of `N` falls in stratum `floor(10k / N)`, and ties go by `T0`.
   - Each member's anchors all go with it: both stratifiers are one value per member per `tau`.
     `sigma_hat` is TZ-07b's single `sigma` per member per `tau`, and `sigma_post` is one per
     member.
8. **M2's sets.**
   - §3.2 names "the TZ-06 400, the TZ-08a 400 and the pooled set". §3.0 says §4's verdict is
     computed on the intersection and on nothing else.
   - M2 is reported, for all three arms, on the intersection's TZ-06 share, its TZ-08a share, and
     pooled. `sigma_hat` is also reported on the full 400s and the full 800, because V7 is
     defined on TZ-08a's full 400.
   - `g` is read on the pooled intersection, with each share's `g` beside it.
9. **M4's model and its rows.**
   - "Ordinary least squares" is read with an intercept: an out-of-sample `R²` "computed against
     the in-sample mean" presupposes one. The normal equations are solved in 60-digit Decimal.
   - One row per intersection member per `tau`, at the checkpoint, the decision time §3.4 names:
     2,632 rows fitted on the TZ-06 share, 2,639 evaluated on the TZ-08a share.
   - The regressors are read off the one-second grid the pricer reads, and M6 is not applied to
     them: they are decision-time quantities, formed as the pricer would form them.
   - `sigma_60` and `sigma_300` are `pfair.realised_sigma` over `[T0 + t − 60, T0 + t]` and
     `[T0 + t − 300, T0 + t]`. The move is the grid at `T0 + t` minus the grid at `T0 + t − 30`.
10. **The observations file has one row per member per `tau`**, 5,600 rows, at the checkpoint.
    That is the unit of TZ-06's and TZ-08a's files. It is not one row per anchor, which would be
    about 2.8 million. Every row can be rebuilt from its own columns; the anchor-level values
    behind M1 and M3 can be re-derived only by re-running.
11. **`sigma_post` qualification.**
    - "Its manifest is complete" is read as the successor manifest's `complete` field.
    - "The disconnect rule admits the whole span" is read as `tz07a.excluded_seconds`, applied to
      the successor as it is to any member, excluding no second of `[T0 + 300, T0 + 600]`.
    - All 47 non-qualifiers fail on the successor's manifest, and 42 of them
      also on a disconnect inside the span.
    - `sigma_post`'s stream is the successor's merged stream: its own directory and the member's.
12. **`sigma_win` at M2's checkpoint** is computed from the grid whether or not M6 drops the
    checkpoint anchor. M2 scores observations, as G3 did, and not anchors.
13. **What the instrument does beyond the TZ's text.** Each item adds a condition and none
    weakens one:
    - V2 also counts `corrected_sd` under the control. It asserts that the control's report lies
      outside the perturbed set and that every checkpoint perturbs at least one report.
    - V4 is asserted at six printed decimals, which is seven significant digits.
    - V4's anchor-walk guard covers 50 members.
    - V8 carries the read-set hash.
14. **The report's structure.**
    - TZ-10b §8 fixes `## 1` … `## 6`, and contract §8 puts `## 0. Fingerprint` first. The TZ's
      structure is followed with `## 0` in front of it, since the contract lets a TZ win for its
      own task.
    - There is no "Gate" section: §4's verdict is the Architect's.
    - Section numbers are asserted unique by the assembler.
15. **The timeline.**
    - A usage limit paused the session between 07:20:23Z (the last file the session wrote before it) and 10:31:48Z. Nothing ran during
      the pause.
    - The gates, the fingerprint and §6 read 1 came before it. Every build, check and run came
      after it, against the same `main` at `e75f836`.
    - That is why the two §6 reads are 12,977 s apart.
16. **What stayed in scratch.**
    - Four probes ran before anything was built, as TZ-10 and TZ-10a taught:
      `probe-selftests.py` (§5.2, 6 of 6), `probe-v2.py` (V2 as written, 140 of 140 both ways),
      `probe-data.py` (the `sigma_post` counts and V7's value) and `probe-zeros.py` (the flat
      spans behind item 2).
    - Two smoke tests exercised the instrument on seven and on thirty members.
    - None of those is a delivered check, and no number in this report comes from them.
17. **A third host read, beyond §6's two.**
    - §6 asks for two reads at least 1,800 s apart, and both are reported as read.
    - The free-space table showed a faster fall during run 2. So one more `df` and `du` pair was
      taken after the runs, and it is reported beside them in §0. It changes no check and gates
      nothing.
    - The names, sizes and modification times of the files that project wrote were read with
      `find -printf`. No file of that project was opened.
