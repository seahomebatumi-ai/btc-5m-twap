# TZ-45 — L0's second rule, rule W, on five days no one had read; the reading's inputs off the host — REPORT

**Status: L0-W reads EARN. Every gate PASS. The reading's inputs are off the host.**

- **The reading — EARN** (`logs/80-score.log`; `logs/81-score-again.log`, `reading.json` `unchanged`). On each of the five member days, the least of the four `pess` variants, each less its adverse hits, is at or above `θ = 10` USDC. The smallest of the five is **`28.680`**, `pess-bt` on 2026-11-12. The most of the four `opt` variants is at or above `θ` on every day, the largest **`227.562`**, `opt-fr` on 2026-11-09. `L0-W EARN: EARN True, NO EARN False`, `reading.json` SHA-256 `874f576a9c082c32674d63b3134a9325d7add2935712f2118f994406cb2c1e08`.

| day | block | the least, hits charged | variant | the most | variant |
|---|---|---|---|---|---|
| 2026-11-09 (`1794182400`) | 96 slots from 00:00 | **`123.437`** | `pess-bt` | `227.562` | `opt-fr` |
| 2026-11-10 (`1794268800`) | 96 slots from 00:00 | **`71.089`** | `pess-br` | `145.457` | `opt-ft` |
| 2026-11-11 (`1794355200`) | 87 slots from 02:15 | **`46.862`** | `pess-bt` | `113.798` | `opt-fr` |
| 2026-11-12 (`1794441600`) | 96 slots from 00:00 | **`28.680`** | `pess-bt` | `104.729` | `opt-fr` |
| 2026-11-13 (`1794528000`) | 85 slots from 00:00 | **`86.201`** | `pess-bt` | `145.351` | `opt-fr` |

- **Every day's money of the eight gated variants, with its parts and its hits**, in USDC to three decimals. The figures are sums over a day's 150 members, from `logs/80-score.log`, whose twelve-decimal lines are quoted in full in §2.4. `gated` is `total − hits` for the `pess` variants and `total` for the `opt` variants. `total = paid + rebate + marks`. The marks are **a proxy**: each position is valued at its market's outcome where its document states one, else at the block's last midpoint.

| day | variant | gated | total | reward paid | reward before the 1-pUSD minimum | rebate | marks (proxy) | hits | markets paid | markets quoting | fills | shares |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 11-09 | `pess-bt` | **123.437** | 170.877 | 181.104 | 184.529 | 0.000 | -10.227 | 47.440 | 13 | 30 | 38 | 541.970 |
| 11-09 | `pess-br` | **170.171** | 217.611 | 214.774 | 217.370 | 0.000 | 2.837 | 47.440 | 14 | 30 | 25 | 317.490 |
| 11-09 | `pess-ft` | **123.637** | 171.077 | 181.104 | 184.529 | 0.000 | -10.027 | 47.440 | 13 | 30 | 38 | 541.970 |
| 11-09 | `pess-fr` | **170.371** | 217.811 | 214.774 | 217.370 | 0.000 | 3.037 | 47.440 | 14 | 30 | 25 | 317.490 |
| 11-09 | `opt-bt` | **180.820** | 180.820 | 189.661 | 189.661 | 1.385 | -10.227 | 47.440 | 13 | 30 | 38 | 541.970 |
| 11-09 | `opt-br` | **227.414** | 227.414 | 223.724 | 223.724 | 0.853 | 2.837 | 47.440 | 14 | 30 | 25 | 317.490 |
| 11-09 | `opt-ft` | **180.968** | 180.968 | 189.608 | 189.608 | 1.387 | -10.027 | 47.440 | 13 | 30 | 38 | 541.970 |
| 11-09 | `opt-fr` | **227.562** | 227.562 | 223.671 | 223.671 | 0.854 | 3.037 | 47.440 | 14 | 30 | 25 | 317.490 |
| 11-10 | `pess-bt` | **78.094** | 127.974 | 115.409 | 118.245 | 0.000 | 12.565 | 49.880 | 19 | 30 | 90 | 1303.430 |
| 11-10 | `pess-br` | **71.089** | 120.969 | 118.545 | 122.466 | 0.000 | 2.423 | 49.880 | 17 | 30 | 53 | 814.340 |
| 11-10 | `pess-ft` | **78.094** | 127.974 | 115.409 | 118.245 | 0.000 | 12.565 | 49.880 | 19 | 30 | 90 | 1303.430 |
| 11-10 | `pess-fr` | **71.089** | 120.969 | 118.545 | 122.466 | 0.000 | 2.423 | 49.880 | 17 | 30 | 53 | 814.340 |
| 11-10 | `opt-bt` | **145.457** | 145.457 | 129.575 | 129.575 | 3.317 | 12.565 | 49.880 | 20 | 30 | 90 | 1303.430 |
| 11-10 | `opt-br` | **141.904** | 141.904 | 137.504 | 137.504 | 1.977 | 2.423 | 49.880 | 20 | 30 | 53 | 814.340 |
| 11-10 | `opt-ft` | **145.457** | 145.457 | 129.575 | 129.575 | 3.317 | 12.565 | 49.880 | 20 | 30 | 90 | 1303.430 |
| 11-10 | `opt-fr` | **141.904** | 141.904 | 137.504 | 137.504 | 1.977 | 2.423 | 49.880 | 20 | 30 | 53 | 814.340 |
| 11-11 | `pess-bt` | **46.862** | 89.442 | 89.593 | 92.025 | 0.000 | -0.152 | 42.580 | 17 | 29 | 24 | 264.820 |
| 11-11 | `pess-br` | **67.103** | 109.683 | 111.337 | 111.980 | 0.000 | -1.654 | 42.580 | 20 | 29 | 14 | 169.120 |
| 11-11 | `pess-ft` | **46.862** | 89.442 | 89.593 | 92.025 | 0.000 | -0.152 | 42.580 | 17 | 29 | 24 | 264.820 |
| 11-11 | `pess-fr` | **67.103** | 109.683 | 111.337 | 111.980 | 0.000 | -1.654 | 42.580 | 20 | 29 | 14 | 169.120 |
| 11-11 | `opt-bt` | **95.432** | 95.432 | 95.006 | 95.006 | 0.578 | -0.152 | 42.580 | 18 | 29 | 24 | 264.820 |
| 11-11 | `opt-br` | **113.798** | 113.798 | 115.114 | 115.114 | 0.338 | -1.654 | 42.580 | 20 | 29 | 14 | 169.120 |
| 11-11 | `opt-ft` | **95.432** | 95.432 | 95.006 | 95.006 | 0.578 | -0.152 | 42.580 | 18 | 29 | 24 | 264.820 |
| 11-11 | `opt-fr` | **113.798** | 113.798 | 115.114 | 115.114 | 0.338 | -1.654 | 42.580 | 20 | 29 | 14 | 169.120 |
| 11-12 | `pess-bt` | **28.680** | 57.500 | 64.306 | 68.241 | 0.000 | -6.807 | 28.820 | 7 | 20 | 14 | 193.150 |
| 11-12 | `pess-br` | **68.261** | 97.281 | 95.477 | 98.991 | 0.000 | 1.803 | 29.020 | 8 | 20 | 9 | 103.150 |
| 11-12 | `pess-ft` | **28.680** | 57.500 | 64.306 | 68.241 | 0.000 | -6.807 | 28.820 | 7 | 20 | 14 | 193.150 |
| 11-12 | `pess-fr` | **68.261** | 97.281 | 95.477 | 98.991 | 0.000 | 1.803 | 29.020 | 8 | 20 | 9 | 103.150 |
| 11-12 | `opt-bt` | **64.186** | 64.186 | 70.594 | 70.594 | 0.398 | -6.807 | 28.820 | 8 | 20 | 14 | 193.150 |
| 11-12 | `opt-br` | **104.729** | 104.729 | 102.756 | 102.756 | 0.170 | 1.803 | 29.020 | 9 | 20 | 9 | 103.150 |
| 11-12 | `opt-ft` | **64.186** | 64.186 | 70.594 | 70.594 | 0.398 | -6.807 | 28.820 | 8 | 20 | 14 | 193.150 |
| 11-12 | `opt-fr` | **104.729** | 104.729 | 102.756 | 102.756 | 0.170 | 1.803 | 29.020 | 9 | 20 | 9 | 103.150 |
| 11-13 | `pess-bt` | **86.201** | 114.121 | 113.602 | 116.471 | 0.000 | 0.519 | 27.920 | 8 | 18 | 42 | 603.610 |
| 11-13 | `pess-br` | **106.873** | 134.773 | 137.583 | 139.753 | 0.000 | -2.811 | 27.900 | 8 | 18 | 37 | 481.760 |
| 11-13 | `pess-ft` | **86.201** | 114.121 | 113.602 | 116.471 | 0.000 | 0.519 | 27.920 | 8 | 18 | 42 | 603.610 |
| 11-13 | `pess-fr` | **106.873** | 134.773 | 137.583 | 139.753 | 0.000 | -2.811 | 27.900 | 8 | 18 | 37 | 481.760 |
| 11-13 | `opt-bt` | **125.385** | 125.385 | 123.397 | 123.397 | 1.468 | 0.519 | 27.920 | 9 | 18 | 42 | 603.610 |
| 11-13 | `opt-br` | **145.351** | 145.351 | 146.975 | 146.975 | 1.187 | -2.811 | 27.900 | 9 | 18 | 37 | 481.760 |
| 11-13 | `opt-ft` | **125.385** | 125.385 | 123.397 | 123.397 | 1.468 | 0.519 | 27.920 | 9 | 18 | 42 | 603.610 |
| 11-13 | `opt-fr` | **145.351** | 145.351 | 146.975 | 146.975 | 1.187 | -2.811 | 27.900 | 9 | 18 | 37 | 481.760 |

- **G-REHEARSAL PASS: 2 of 2.** TZ-43's rule gave 451 lines, `1ab40f4b…`. Rule W gave 1,351 lines, `9c8c1a34…`. Both are equal to the expected lines. **G-SET PASS:** 5 members of 5 candidates considered, `1794182400` to `1794528000`, with 0 non-members. The set holds 359 distinct markets, 16 of them resolved by their documents, and 460 stream files of `6,734,268,496` bytes. **G-BOOK PASS:** the rebuilt touch equals the venue's at `70,125` of `70,144` book frames, `0.99973`. **DETERMINISM PASS:** the replay's 24 of 24 slot lines, and the pack's 7 of 7 outputs.
- **The set:** five candidates considered, 2026-11-09 to 2026-11-13, every one a member. 2026-11-11 is a block of 87 slots from 02:15 UTC; its slot of 02:00 UTC `ended early`. 2026-11-13 is a block of 85 slots from 00:00 UTC; its 11 slots from 21:15 UTC fail, the first three `stream: not opened`. 2026-11-14 was not reached: the walk stops at its fifth member.
- **The Release:** id **`446880816`**, on the lightweight tag **`tz-45-l0-rule-w-inputs`**, at the instrument's commit **`01756f665893096ab38ae10dfbe58f074f8fb648`**. It is published and not the latest. It holds **28 assets, `109,165,516` bytes**: five day archives (`78,653,440` bytes), this run's 22 work files (`30,340,669` bytes) and the manifest (`171,407` bytes), each listed in §2.6.
  - **G-SOURCE PASS: 22 of 22**, at both `pack` runs.
  - **G-PACK PASS: 5 days of 5.** 970 members, `77,903,892` bytes of members. **No file of replies withheld: 0 files, 0 bytes.** No stream or other name was opened. No day ran over its budget.
  - **G-RESERVE PASS** at both runs. The store was opened 1,455 times — 970 members kept and 485 files of replies scanned — and listed 5 times, once a day.
  - **G-UPLOAD PASS: 28 of 28. G-DOWNLOAD PASS: 28 of 28** anonymous downloads, `109165516` bytes. **G-TAG PASS:** `tz-45-l0-rule-w-inputs` at `01756f665893096ab38ae10dfbe58f074f8fb648`, lightweight.
- **Order of commit and reads:** the instrument's commit was on `origin` at **`2026-11-16T07:50:28.452174496Z`** (`logs/13-push.log`). The read ledger's first line is at `2026-11-16T07:51:29Z` (`rehearse`), and its first `fetch` line at `2026-11-16T07:52:01Z`.
- **G-STILL PASS:** the recorder, the pair book, the reward book and the advisor were unchanged from 07:50:52 to 10:23:49 UTC.
- **The advisor's `commit.txt`** reads `4e6db2d16dda3da14957120d636f537dfc0bcc87` at both host gates, equal to map §3's `4e6db2d…`.
- **The classifier refused no block.** B-RECLAIM-SCRATCH — one `reclaim`, then five single-tree `rm -rf` with their `test -e` — ran in the session unrefused. **B-UPLOAD was the Boss's by its own text.** It was handed over at 08:37:24 UTC. The Boss ran it once, at 10:20:43 UTC, and it completed, `exit=0`. B-RECLAIM-OWN is §9, below.

Run on 2026-11-16, from 07:48:22 UTC (§0.0) to the end of §9. The logs were under `/root/tz45-work/logs/`; §9 copied them into `/root/btc-forensics/` as `tz45-work--logs--<name>`. The model the TZ names, Claude Opus 5.5, is the model this session is configured to run.

---

## 0. Fingerprint

**Map revision read:** `2026-11-13-a` (map §0), equal to the TZ header's. **Anchors read**, each equal to the TZ header's:

| anchor | map §0 | TZ header |
|---|---|---|
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` |
| `A2` — collector | `6c5089330629` | `6c5089330629`, re-derived |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` | the same |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b`, re-derived |
| `A5` — recorder | `0f6c90451cbd` | `0f6c90451cbd`, re-derived |
| `A6` — pricer | `729f0bcdbee3` | `729f0bcdbee3`, re-derived |

**§0.0, the instant.** The session's first run of the clock line printed `now 1794815302 2026-11-16T07:48:22Z, second of the day 28102` and `inside=0`. Its run into `logs/00-instant.log`:

```
now 1794815329 2026-11-16T07:48:49Z, second of the day 28129
inside=0
```

**§0.0, the readiness read.** The session's first run printed the same five candidates and `ready=1: 5 members of 5, candidates to 2026-11-13; 9778073600 bytes free, 8350000000 needed; at 1794815318`. Its run into `logs/00-ready.log`:

```
candidate 1794182400 2026-11-09: member - longest run of whole slots 96 from 00:00; 0 slots fail
candidate 1794268800 2026-11-10: member - longest run of whole slots 96 from 00:00; 0 slots fail
candidate 1794355200 2026-11-11: member - longest run of whole slots 87 from 02:15; 1 slots fail, the first 02:00, ended early
candidate 1794441600 2026-11-12: member - longest run of whole slots 96 from 00:00; 0 slots fail
candidate 1794528000 2026-11-13: member - longest run of whole slots 85 from 00:00; 11 slots fail, the first 21:15, no whole stream
ready=1: 5 members of 5, candidates to 2026-11-13; 9777897472 bytes free, 8350000000 needed; at 1794815329
```

**§0.1, the instrument staged** (`logs/01-stage.log`), and again into the worktree at §3.1 (`logs/11-worktree.log`):

```
/root/tz45-work/stage/research/tz45-l0-rule-w.py 4299 233655 4720e78573e54b1325dd24af7c30e0de59bfb4c1879d309a23fa6bab6b32d2d4
/root/tz45-work/stage/research/tz27-pairbook-archive.py 2078 106284 2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673
exit=0
/root/tz45-work/wt/research/tz45-l0-rule-w.py 4299 233655 4720e78573e54b1325dd24af7c30e0de59bfb4c1879d309a23fa6bab6b32d2d4
/root/tz45-work/wt/research/tz27-pairbook-archive.py 2078 106284 2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673
```

**§0.2 and §3.1, the fingerprint** (`logs/02-fingerprint.log`, `logs/12-fingerprint.log`). The map's §0 table lists 63 files; the instrument printed every row, equal at both runs:

| path | lines | bytes | SHA-256 | row |
|---|---|---|---|---|
| `SYSTEM-MAP.md` | 2,105 | 610,703 | `3c8455a75aeefc5c993783cfbd5845c104b797810ddb3dc6ba59a7c920f3ff5d` | reported |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | frozen equal |
| `research/twap-divergence.py` | 1,135 | 50,928 | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | frozen equal |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | frozen equal |
| `research/tz02-distribution.py` | 334 | 14,511 | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | tracked |
| `research/pfair.py` | 441 | 19,357 | `729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68` | frozen equal |
| `research/selftest-pfair.py` | 619 | 32,559 | `b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa` | frozen equal |
| `research/tz06-calibration.py` | 577 | 27,138 | `715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f` | frozen equal |
| `research/tz07a-variance-time.py` | 623 | 28,414 | `513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771` | frozen equal |
| `research/tz07b-settlement-dispersion.py` | 515 | 24,926 | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` | frozen equal |
| `research/tz08a-out-of-sample.py` | 745 | 38,822 | `37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c` | frozen equal |
| `research/tz09-disk-inventory.py` | 894 | 41,004 | `b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6` | frozen equal |
| `research/tz10b-sigma-or-link.py` | 1,224 | 61,018 | `406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088` | frozen equal |
| `research/tz11a-student-link.py` | 1,231 | 64,732 | `0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839` | frozen equal |
| `research/tz12-sized-gate.py` | 1,157 | 61,637 | `d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999` | frozen equal |
| `research/tz13-sized-gate-test3.py` | 1,074 | 53,901 | `a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd` | frozen equal |
| `research/tz14-quote-inventory.py` | 2,124 | 109,972 | `978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02` | frozen equal |
| `research/tz15-phase2-gate.py` | 1,517 | 73,799 | `66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3` | frozen equal |
| `research/tz16a-phase2-decisive-gate.py` | 2,198 | 111,192 | `3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125` | frozen equal |
| `research/tz17-settlement-chain.py` | 1,102 | 38,622 | `e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92` | frozen equal |
| `research/tz18a-chainbook-capture.py` | 1,683 | 69,517 | `e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae` | frozen equal |
| `research/tz20-capture-under-systemd.py` | 771 | 36,528 | `104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7` | frozen equal |
| `research/tz21-recorder-memory.py` | 1,284 | 59,009 | `d6d2dc195809f2160fda7856980d8ccfbf0006ba0836943ff789c877f9d5795f` | frozen equal |
| `research/tz23-maker-m0.py` | 1,184 | 54,885 | `6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f` | frozen equal |
| `research/tz24-nesting-b2.py` | 1,535 | 76,142 | `4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b` | frozen equal |
| `research/tz26-nesting-b3-capture.py` | 2,492 | 118,466 | `caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec` | frozen equal |
| `research/tz27-pairbook-archive.py` | 2,078 | 106,284 | `2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673` | frozen equal |
| `research/tz28-pairbook-archive-timer.py` | 1,438 | 74,576 | `46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4` | frozen equal |
| `research/tz29-maker-m0-second-look.py` | 1,225 | 68,959 | `18defff93d08c13ea4638a518c88a3fec5541fcf53fb6827451e727f2204d905` | frozen equal |
| `research/tz30-nesting-b3-measure.py` | 2,518 | 131,119 | `93dbbf1c4f84553a7bc041387ef92c3c0d8747c384d383b4fcd0b247fcd131ab` | frozen equal |
| `research/tz31-who-earns.py` | 1,523 | 84,775 | `7073188c8fbaa19568e8c6e4d6379e40ea57cf2a1341ebde0ea6a08f2c544765` | frozen equal |
| `research/tz32-our-quoting.py` | 2,576 | 138,209 | `6ec367e6ed995b315063d2d808dd6a3995878011afd76abfbb7b106b645a9c61` | frozen equal |
| `research/tz33-reward-book-capture.py` | 3,542 | 175,160 | `a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670` | frozen equal |
| `research/tz34-rewardbook-archive-timer.py` | 1,791 | 99,388 | `1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72` | frozen equal |
| `research/tz35-advisor-deploy.py` | 802 | 42,049 | `d50787db5113c3f748806a60a3e71211b665cb5235296e43d0e9a747a529e6f5` | frozen equal |
| `research/tz36-advisor-trust.py` | 582 | 32,925 | `a0fb9d53afe435d37354862eb8fd299256bf551fdbdb25a5c828d2cc7376d4f5` | frozen equal |
| `research/tz37-capital-allocation.py` | 808 | 51,269 | `eec1f30b971ed1d6db31e27eb0c321276c1b107a1654e013996d023b1a6a04eb` | frozen equal |
| `research/tz38-adv3-pit-validation.py` | 1,782 | 90,181 | `579474b65329662f7bed735994381241a928a2c65a726cec3f933dc7afd4427b` | frozen equal |
| `research/tz39-advisor-checks.py` | 1,139 | 73,892 | `18294b0916d77b226083a18f9521f06e2fddb423bbc947a2e1100fd42b2980f3` | frozen equal |
| `research/tz40-advisor-strong.py` | 1,436 | 95,474 | `4403b27185f7e9aaa090dedfca457af6c4f70b6b020f0d2fcd9f9fbb96b6054b` | frozen equal |
| `research/tz42-advisor-registry.py` | 2,088 | 134,077 | `b6c45490b2f86f5c4678c645041ef1556b1199a6bc814470de904aedf7f5105f` | frozen equal |
| `research/tz43-l0-our-quote.py` | 3,056 | 152,905 | `48c3550b3f9a990fa8bc43ad8464b181ec2eb0a086b3b6f3a0ceed52da4a30cf` | frozen equal |
| `research/tz44-l0-inputs-release.py` | 1,616 | 90,703 | `0b78807d9c5dec087138b0c9a329cb8c976157ab5c8a3fd4deee7cb31e89e190` | frozen equal |
| `research/recorder/recorder.py` | 651 | 27,821 | `0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7` | frozen equal |
| `research/recorder/config.py` | 112 | 4,773 | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | frozen equal |
| `research/recorder/manifest.py` | 254 | 10,002 | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | frozen equal |
| `research/recorder/analyze.py` | 813 | 34,705 | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` | frozen equal |
| `research/recorder/probe.py` | 227 | 9,324 | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | frozen equal |
| `research/recorder/selftest.py` | 573 | 30,591 | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` | frozen equal |
| `deploy/systemd/btc-recorder.service` | 23 | 707 | `3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1` | frozen equal |
| `deploy/systemd/btc-chainbook.service` | 22 | 724 | `a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2` | frozen equal |
| `deploy/systemd/btc-pairbook.service` | 22 | 761 | `ba02fe4175b961c387ea8066eb084704e69efc7fd0a48d8f623a0198334f8dd8` | frozen equal |
| `deploy/systemd/btc-pairbook-archive.service` | 17 | 794 | `2e7fd45382af3da3b2ec29ced8d69870ef3d4481da4c6f327b90fc6cb5af78e7` | frozen equal |
| `deploy/systemd/btc-pairbook-archive.timer` | 13 | 417 | `07581f4f331fbf9d2a1113cac42a2872d65ac69a872991bff7d2bda235eac913` | frozen equal |
| `deploy/systemd/btc-rewardbook.service` | 23 | 817 | `7691720c7b2261a606af54bfa20b5068b89455ea54512c55dde861d6d8063bec` | frozen equal |
| `deploy/systemd/btc-rewardbook-archive.service` | 17 | 810 | `a9abb1f092b3fb8359d37ea88df00dca8557d0f0482d04c12f0fbdd32601e33f` | frozen equal |
| `deploy/systemd/btc-rewardbook-archive.timer` | 13 | 428 | `bf5af0252c420d8db1579b82e5da21472cdb6bc871fa8035ecf6f1edc9720a0f` | frozen equal |
| `deploy/systemd/adv3-bot.service` | 27 | 863 | `82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66` | frozen equal |
| `advisor/RULE-ADV-3.txt` | 33 | 3,203 | `ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169` | frozen equal |
| `advisor/adv3.py` | 895 | 51,834 | `81ef0112d3fe4b86566e51a51aab924d9776ff37a927e65982ecb0bb7c1f34e1` | frozen equal |
| `advisor/adv3-bot.py` | 2,548 | 157,438 | `c3d9fff54f3585cfc4c33b5f7e1f93b390e62b03e0b4725fee2d6fdda6d04c11` | frozen equal |
| `advisor/selftest-adv3.py` | 256 | 19,111 | `6f29b82f2b2ca82cd2ff4bbb370e032354dbb4743497330530777429b3af7398` | frozen equal |
| `.gitignore` | 5 | 252 | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | tracked |

```
[2026-11-16T07:49:03Z] re-derived A2 research/twap-divergence.py sha256[:12] 6c5089330629 equal
[2026-11-16T07:49:03Z] re-derived A4 BTC-EXECUTOR-INSTRUCTIONS.md sha256[:12] 437b45ea196b equal
[2026-11-16T07:49:03Z] re-derived A5 research/recorder/recorder.py sha256[:12] 0f6c90451cbd equal
[2026-11-16T07:49:03Z] re-derived A6 research/pfair.py sha256[:12] 729f0bcdbee3 equal
[2026-11-16T07:49:03Z] SYSTEM-MAP.md 2105 lines 610703 bytes sha256 3c8455a75aeefc5c993783cfbd5845c104b797810ddb3dc6ba59a7c920f3ff5d
[2026-11-16T07:49:03Z] FINGERPRINT PASS: revision 2026-11-13-a; anchors 6 of 6, 4 re-derived; rows 63: frozen 60 of 60 equal, tracked 2, reported 1
[2026-11-16T07:50:10Z] FINGERPRINT PASS: revision 2026-11-13-a; anchors 6 of 6, 4 re-derived; rows 63: frozen 60 of 60 equal, tracked 2, reported 1
```

**§0.3, the host gate** (`logs/03-host-gate.log`, 07:49:10 UTC). **11 checks of 11:**

| check | read | result |
|---|---|---|
| H1 | `find` printed exactly one path, `/var/lib/btc-recorder/btc-updown-5m/1792953900/manifest.json` | PASS |
| H2 | `df`: source `/dev/vda2`, size `31612203008` | PASS |
| H2 | `grep -c e3975b5…` printed `4` | PASS |
| H3 | `3.12.3` | PASS |
| H4 | `stat`: `71648` ledger, `32516` `runs/1793263627/set.json`, `137247` the pair book archive's ledger | PASS |
| H5 | `btc-recorder.service` `active` / `enabled`, MainPID `1555954`, `NRestarts` `0` | PASS |
| H5 | `btc-pairbook.service` `active` / `enabled`, MainPID `1871674`, `NRestarts` `5` | PASS |
| H5 | `btc-rewardbook.service` `active` / `enabled`, MainPID `1556307`, `NRestarts` `0` | PASS |
| H5 | `adv3-bot.service` `active` / `enabled`, MainPID `1555970`, `NRestarts` `0` | PASS |
| memory | `MemAvailable read 1 07:49:29: 494649344`, floor `172,658,448` | PASS |
| disk | `avail` `9777135616`, bound `8,350,000,000` | PASS |

**§0.5, NUMBER and the refs.**

```
[2026-11-16T07:49:46Z] origin/main 4bb14d8a59a48291dcf7b295b2f7197c3cca88bb: 109 paths under CryptoTZ/ and CryptoReports/; of the number TZ-45-: ['CryptoTZ/TZ-45-l0-rule-w.md'] and []
[2026-11-16T07:49:46Z] NUMBER PASS - 2 of 2
[2026-11-16T07:49:46Z] malloc tuned: True
[2026-11-16T07:49:46Z] peak memory of this run: 47083520 bytes
[2026-11-16T07:49:46Z] opens refused: 0, by TZ-27's hook: 0; reward book opens: 0, listings: 0
[2026-11-16T07:50:05Z] NUMBER PASS - 2 of 2
```

`git ls-remote origin` printed **157 ref lines** (`logs/05-refs.log`). The Architect read 151 on 2026-11-15 at 05:24 UTC. The six more are three `pairbook-streams-*` tags (57 against 54) and three `rewardbook-streams-*` tags (30 against 27), the archives' runs since that read. `HEAD` and `refs/heads/main` were at `4bb14d8a59a48291dcf7b295b2f7197c3cca88bb`. The listing held 20 `tz-*` branches, 43 pull heads, 0 merge refs, the lightweight `tz-44-l0-inputs`, and the two annotated tags with their peeled lines. **Neither `refs/heads/tz-45-l0-rule-w` nor `refs/tags/tz-45-l0-rule-w-inputs` existed.** The last `rewardbook-streams-*` tag was `rewardbook-streams-1794792620` and the last `pairbook-streams-*` tag `pairbook-streams-1794798020`. The difference is recorded, not BLOCKING.

**Commits on `main`'s first-parent line above `5192aff`**, with the paths each changed:

```
4bb14d8a59a48291dcf7b295b2f7197c3cca88bb 2026-11-16T03:13:31+04:00 Add files via upload        A CryptoTZ/TZ-45-l0-rule-w.md
879d95c910abfcf273ede0f8871d5d69df7fe51a 2026-11-16T03:12:38+04:00 Delete CryptoTZ/TZ-45-l0-rule-w.md   D CryptoTZ/TZ-45-l0-rule-w.md
6500f052043d4869ebbc77faf450598c4543766b 2026-11-15T14:31:59+04:00 Add files via upload        A CryptoTZ/TZ-45-l0-rule-w.md
```

`6500f05` is the first file, whose execution never began (the TZ's header). `879d95c` removed it, and `4bb14d8` uploaded the corrected file this run executed.

---

## 1. Input

| what | read by | lines | bytes | SHA-256 |
|---|---|---|---|---|
| `CryptoTZ/TZ-45-l0-rule-w.md`, at `4bb14d8` | the session, in full; §0.1's script | 5,029 | 378,049 | `fe6d8668d5b1afe15ae2fe4f6048bbc0430580844a93eef960f05fcb78a18888` |
| `SYSTEM-MAP.md` | the session; `fingerprint` | 2,105 | 610,703 | `3c8455a75aeefc5c993783cfbd5845c104b797810ddb3dc6ba59a7c920f3ff5d` |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | the session; `fingerprint` | 234 | 11,128 | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` |
| `research/tz45-l0-rule-w.py`, Appendix A | every mode | 4,299 | 233,655 | `4720e78573e54b1325dd24af7c30e0de59bfb4c1879d309a23fa6bab6b32d2d4` |
| `research/tz27-pairbook-archive.py` | loaded by the instrument | 2,078 | 106,284 | `2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673` |

The file at `6500f05`, the first upload, has SHA-256 `fa1a35ea69e46abd9f23ab5f9949eef76b79e954db1b128121e7f4ba39493586`; it was not executed.

**The reward book's store, `/var/lib/btc-rewardbook/`**, was read in three places:

- **§0.0's read** listed the five candidate days' directories and opened their `<S>.<k>.slot.json`.
- **`I fetch`** opened the store 950 times and listed it 5 times. It read each day's `select.<a>.json` and `select.<a>.replies.jsonl.gz`, and each slot's `<S>.<k>.slot.json` and `<S>.<k>.rewards.jsonl.gz`.
- **`I pack`** opened it 1,455 times and listed it 5 times at each of its two runs.

Nothing else under the store was opened or listed, and **no stream file stored there was opened.** The polls served: 43,200 of 43,200 on 2026-11-09, 43,199 of 43,200 on 2026-11-10, 39,150 of 39,150 on 2026-11-11, 43,200 of 43,200 on 2026-11-12 and 38,250 of 38,250 on 2026-11-13, over each member's block.

**The archive's state:** `ledger.jsonl` (`71,648` bytes, SHA-256 `30c915eacbbeca8905da2eafd20d1477b86f9930b96436e06b5325478ba26cc5`, 189 complete records) and each of the 30 complete runs' `set.json`.

**The streams:** 460 stream assets, `6,734,268,496` bytes, downloaded anonymously from the archive's Releases. Each was downloaded by the bytes and SHA-256 its set records, replayed in its unit, and removed. The rehearsal's four assets, `47,329,972` bytes, came from `rewardbook-streams-1793263627`. The rescore downloaded the first 24 slots of 2026-11-09 again, `332,948,448` bytes.

**The venue:** the members' gamma documents, requested once each by `I fetch`, as printed in §2.1.

**Nothing was re-collected:** the store was read as stored, and no stream, selection or poll was requested from the venue. Nothing of a day before `1794182400` and no day after `1794528000` was opened or listed.

---

## 2. Measurements

### 2.1 The set, as `I fetch` printed it (`logs/60-fetch.log`)

```
[2026-11-16T07:52:04Z] candidate 1794182400 (2026-11-09T00:00:00Z): MEMBER 1 of 5 - 150 markets, 96 slots from 2026-11-09T00:00:00Z, 0 slots failing, 96 stream files, 1266123741 bytes; polls 43200 served of 43200, 297 without a row
[2026-11-16T07:52:07Z] candidate 1794268800 (2026-11-10T00:00:00Z): MEMBER 2 of 5 - 150 markets, 96 slots from 2026-11-10T00:00:00Z, 0 slots failing, 96 stream files, 1358308364 bytes; polls 43199 served of 43200, 966 without a row
[2026-11-16T07:52:09Z] candidate 1794355200 (2026-11-11T00:00:00Z): MEMBER 3 of 5 - 150 markets, 87 slots from 2026-11-11T02:15:00Z, 1 slots failing; 1794362400 (2026-11-11T02:00:00Z) stream: ended early, 87 stream files, 1345660463 bytes; polls 39150 served of 39150, 1633 without a row
[2026-11-16T07:52:12Z] candidate 1794441600 (2026-11-12T00:00:00Z): MEMBER 4 of 5 - 150 markets, 96 slots from 2026-11-12T00:00:00Z, 0 slots failing, 96 stream files, 1459311456 bytes; polls 43200 served of 43200, 5207 without a row
[2026-11-16T07:52:15Z] candidate 1794528000 (2026-11-13T00:00:00Z): MEMBER 5 of 5 - 150 markets, 85 slots from 2026-11-13T00:00:00Z, 11 slots failing; 1794604500 (2026-11-13T21:15:00Z) stream: not opened; 1794605400 (2026-11-13T21:30:00Z) stream: not opened; 1794606300 (2026-11-13T21:45:00Z) stream: not opened, 85 stream files, 1304864472 bytes; polls 38250 served of 38250, 984 without a row
[2026-11-16T07:52:16Z] gamma request: 50 ids, closed False, 50 documents, 421010 bytes, sha256 5609c219c3e9642ca67bdc7928040d768ce16e69e86908073da7e81d0afdc7d5, retries 0
[2026-11-16T07:52:16Z] gamma request: 50 ids, closed True, 0 documents, 3 bytes, sha256 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570, retries 0
[2026-11-16T07:52:16Z] gamma request: 50 ids, closed False, 48 documents, 396346 bytes, sha256 2dfcefc6eef30f13681b2b5ebad443e70181ee8abc05d9bbafc0bdcf702aa064, retries 0
[2026-11-16T07:52:16Z] gamma request: 50 ids, closed True, 2 documents, 18751 bytes, sha256 63a8980fa5c0377f2b2c93e5f23813b782088e9d840aa2144cbd06f58e8cda50, retries 0
[2026-11-16T07:52:16Z] gamma request: 50 ids, closed False, 46 documents, 349825 bytes, sha256 c2e0fa602418f551e62746488dd689a7051a7d2f57d6fc25c6d7a3181d7e62e2, retries 0
[2026-11-16T07:52:16Z] gamma request: 50 ids, closed True, 4 documents, 42202 bytes, sha256 ee889b5b9c52f62c06640f1ee711b54cb72fea31c1482189c930d4675c1933b6, retries 0
[2026-11-16T07:52:16Z] gamma request: 50 ids, closed False, 46 documents, 369109 bytes, sha256 712722003b543dbdeadee15bb868e8e1663c0acdb94a1e4712dedd84fdc9535c, retries 0
[2026-11-16T07:52:16Z] gamma request: 50 ids, closed True, 4 documents, 46898 bytes, sha256 8116bf714bcfc98776102ea96cda2dcf57eeb2f996d7a16074ba359dd749ecda, retries 0
[2026-11-16T07:52:16Z] gamma request: 50 ids, closed False, 48 documents, 385934 bytes, sha256 76c1dbc3304bdb99e409227266ec5434280fef0c802ddbf471341a0d73bdc20f, retries 0
[2026-11-16T07:52:16Z] gamma request: 50 ids, closed True, 2 documents, 27610 bytes, sha256 0d8d69352be7acad79591589bfe31f7b116a387ea914b2f416f0cc99d5917a8d, retries 0
[2026-11-16T07:52:16Z] gamma request: 50 ids, closed False, 48 documents, 410550 bytes, sha256 b734e57f29b4f5875a88e05d3485cde0d75175bf5e50643f91333c646270c297, retries 0
[2026-11-16T07:52:16Z] gamma request: 50 ids, closed True, 2 documents, 16599 bytes, sha256 2191332ba1b48c82c29798c875006811f7f19e503088a32a38431c6671d721fe, retries 0
[2026-11-16T07:52:16Z] gamma request: 50 ids, closed False, 48 documents, 365292 bytes, sha256 3dd291de1ae94131f45b8efdb23b8f118f2718e4f137216263d543a15b587a20, retries 0
[2026-11-16T07:52:16Z] gamma request: 50 ids, closed True, 2 documents, 23106 bytes, sha256 4bc701fcc0a0cf5e854a37b4faa170664842049cb08da5a860174b71a1ac7ed4, retries 0
[2026-11-16T07:52:16Z] gamma request: 9 ids, closed False, 9 documents, 74217 bytes, sha256 6d700b695cfa1cdc7fab1b16e2c3a104f7a9e391c7c331b3f6873b6a35521854, retries 0
[2026-11-16T07:52:16Z] gamma request: 9 ids, closed True, 0 documents, 3 bytes, sha256 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570, retries 0
[2026-11-16T07:52:16Z] G-SET PASS: 5 members of 5 candidates considered, 1794182400 to 1794528000; 359 distinct markets, 16 resolved by their documents; 460 stream files, 6734268496 bytes; set.json sha256 25eb1cba98ccd6d68fac5ad8c86da06677fd400483e8f27761ec21a23cffd462
[2026-11-16T07:52:16Z] peak memory of this run: 75780096 bytes
[2026-11-16T07:52:16Z] opens refused: 0, by TZ-27's hook: 0; reward book opens: 950, listings: 5
```

### 2.2 The replay (`logs/70-replay.log`; `logs/71-replay-again.log` replayed 0 of 5 days and printed G-BOOK again)

```
[2026-11-16T07:52:27Z] days to replay 5 of 5, 6734268496 bytes of streams
[2026-11-16T07:53:33Z] projected 782 s of replay for 6734268496 bytes after 24 units at 0.1161 s a megabyte
[2026-11-16T08:03:10Z] day 1794182400 (2026-11-09T00:00:00Z) replayed in 642 s: 96 slots, 10176649 lines; slots sha256 071bb0609497f08d85da6712446dc60b17796d909d3a6f30ec6a22d53cce20f8, day sha256 8486a5888ff2cbb23446c633e7991e5895accb8576cc13a8f37fff70cbe01aa7
[2026-11-16T08:07:51Z] day 1794268800 (2026-11-10T00:00:00Z) replayed in 281 s: 96 slots, 10719838 lines; slots sha256 876bf5a6d8c9a0f5f8db04f7a89cdbaafe7a8d6e2aac7f61a2c8d406fba9b58e, day sha256 fd162966f292d9d8c958c99c696bc2ecd20cfa12e87114b88ee61bd7255a9fe3
[2026-11-16T08:19:21Z] day 1794355200 (2026-11-11T00:00:00Z) replayed in 690 s: 87 slots, 11282942 lines; slots sha256 981c985e5f4208eee0ddb10f4b5d3cb1eff5e1daa7a52a36bfcd19733e5924a2, day sha256 900307a8e41ca4579491482654cf1d3bc756268a166f5641455cb26e6b90c673
[2026-11-16T08:30:45Z] day 1794441600 (2026-11-12T00:00:00Z) replayed in 684 s: 96 slots, 11917748 lines; slots sha256 a3351cecbb54249db9e42b4de635afccaf70c78ffff4090b42a1cbfbb60ed801, day sha256 9ce2ca6d1e356196f18db4090bc7091323f63cb66fc1ca768ae8c3d8c4be162f
[2026-11-16T08:35:05Z] day 1794528000 (2026-11-13T00:00:00Z) replayed in 261 s: 85 slots, 10488304 lines; slots sha256 74d6c047066307175769f4c5cac13fdcd0aaeba7d5d28f80acaeeb779688cdaa, day sha256 6dfb638cd08f7c338347d620ed3ed9e9e0aebcf200fab34bb6aeb0a6b7050084
[2026-11-16T08:35:05Z] units 460: inside the idle stretch 460, ending after second 590 0; longest 7.9 s, download 5.0 s and replay 6.7 s at most; 1141 s waited; processor 861.1 s; 6734268496 bytes downloaded; retries 0; windows 2026-11-16T07:45:00Z to 2026-11-16T08:30:00Z
[2026-11-16T08:35:05Z] day 1794182400: book frames 11258, the rebuilt touch equal at 11255, every level equal at 11239; matches 11212; subscribes 1, closes 1
[2026-11-16T08:35:05Z] day 1794268800: book frames 15070, the rebuilt touch equal at 15065, every level equal at 15052; matches 15008; subscribes 1, closes 1
[2026-11-16T08:35:05Z] day 1794355200: book frames 11517, the rebuilt touch equal at 11515, every level equal at 11498; matches 11496; subscribes 1, closes 1
[2026-11-16T08:35:05Z] day 1794441600: book frames 19472, the rebuilt touch equal at 19467, every level equal at 19442; matches 19430; subscribes 2, closes 2
[2026-11-16T08:35:05Z] day 1794528000: book frames 12827, the rebuilt touch equal at 12823, every level equal at 12809; matches 12807; subscribes 2, closes 2
[2026-11-16T08:35:05Z] G-BOOK PASS: the rebuilt touch equal to the venue's book frame at 70125 of 70144 frames, at least 99/100 required; barred: every level equal at 70040
[2026-11-16T08:35:05Z] peak memory of this run: 64401408 bytes
[2026-11-16T08:35:05Z] opens refused: 0, by TZ-27's hook: 0; reward book opens: 0, listings: 0
[2026-11-16T08:35:18Z] days to replay 0 of 5, 0 bytes of streams
[2026-11-16T08:35:18Z] G-BOOK PASS: the rebuilt touch equal to the venue's book frame at 70125 of 70144 frames, at least 99/100 required; barred: every level equal at 70040
```

**G-BOOK by day**, the touch equal at, of the `book` frames of the members' first tokens other than a seed:

| day | frames | touch equal | every level equal (barred) |
|---|---|---|---|
| 2026-11-09 | 11,258 | 11,255 | 11,239 |
| 2026-11-10 | 15,070 | 15,065 | 15,052 |
| 2026-11-11 | 11,517 | 11,515 | 11,498 |
| 2026-11-12 | 19,472 | 19,467 | 19,442 |
| 2026-11-13 | 12,827 | 12,823 | 12,809 |
| **total** | **70,144** | **70,125** | 70,040 |

**The timing files:** `timing-replay.jsonl` holds 460 lines — 460 units inside the idle stretch and 0 ending after second 590. `timing-rescore.jsonl` holds 24 — 24 inside and 0 after second 590. **No unit of either ended after second 590.**

### 2.3 The rescore (`logs/75-rescore.log`)

```
[2026-11-16T08:35:40Z] projected 40 s of replay for 332948448 bytes after 6 units at 0.1200 s a megabyte
[2026-11-16T08:36:25Z] wrote /root/tz45-work/rescore.txt 28476 bytes sha256 f8e6d6c5c5e8b2440865c21875017b472f390903aeac22114c9c28319345a4da
[2026-11-16T08:36:25Z] units 24: inside the idle stretch 24, ending after second 590 0; longest 4.5 s, download 2.7 s and replay 3.3 s at most; 0 s waited; processor 39.9 s; 332948448 bytes downloaded; retries 0; windows 2026-11-16T08:30:00Z to 2026-11-16T08:30:00Z
[2026-11-16T08:36:25Z] DETERMINISM PASS: 24 of 24 slot lines of day 1794182400 equal to the replay's
```

### 2.4 The score, every day's money by variant, as `I score` printed it (`logs/80-score.log`; `central` barred)

```
[2026-11-16T08:36:38Z] power: every day's least at or above 10 with probability 0.90 each: 0.590490000000
[2026-11-16T08:36:38Z] power: every day's least at or above 10 with probability 0.95 each: 0.773780937500
[2026-11-16T08:36:38Z] power: every day's least at or above 10 with probability 0.99 each: 0.950990049900
[2026-11-16T08:36:38Z] false reading: 2^-5 = 0.031250000000 for each answer, under independent days
[2026-11-16T08:36:38Z] G-BOOK PASS: the rebuilt touch equal to the venue's book frame at 70125 of 70144 frames, at least 99/100 required; barred: every level equal at 70040
[2026-11-16T08:36:38Z] day 1794182400 pess-bt gated 123.436658293768: total 170.876658293768 = paid 181.103568293768 of reward 184.529326135701 on 13 of 150 markets + rebate 0.000000000000 + marks -10.226910000000; hits 47.440000000000 on 30 quoting markets; fills 38, 541.970000000000 shares, 219.650000000000 against crossing orders; scored 85.184937715012 h; marks {'mid': 147, 'outcome': 3}
[2026-11-16T08:36:38Z] day 1794182400 pess-br gated 170.170623980550: total 217.610623980550 = paid 214.773833980550 of reward 217.370452840546 on 14 of 150 markets + rebate 0.000000000000 + marks 2.836790000000; hits 47.440000000000 on 30 quoting markets; fills 25, 317.490000000000 shares, 0.000000000000 against crossing orders; scored 97.010873163661 h; marks {'mid': 147, 'outcome': 3}
[2026-11-16T08:36:38Z] day 1794182400 pess-ft gated 123.636658293768: total 171.076658293768 = paid 181.103568293768 of reward 184.528835221073 on 13 of 150 markets + rebate 0.000000000000 + marks -10.026910000000; hits 47.440000000000 on 30 quoting markets; fills 38, 541.970000000000 shares, 219.650000000000 against crossing orders; scored 85.159531967270 h; marks {'mid': 147, 'outcome': 3}
[2026-11-16T08:36:38Z] day 1794182400 pess-fr gated 170.370623980550: total 217.810623980550 = paid 214.773833980550 of reward 217.369961925919 on 14 of 150 markets + rebate 0.000000000000 + marks 3.036790000000; hits 47.440000000000 on 30 quoting markets; fills 25, 317.490000000000 shares, 0.000000000000 against crossing orders; scored 96.985467415919 h; marks {'mid': 147, 'outcome': 3}
[2026-11-16T08:36:38Z] day 1794182400 opt-bt  gated 180.819736315628: total 180.819736315628 = paid 189.661348475378 of reward 189.661348475378 on 13 of 150 markets + rebate 1.385297840250 + marks -10.226910000000; hits 47.440000000000 on 30 quoting markets; fills 38, 541.970000000000 shares, 219.650000000000 against crossing orders; scored 85.287162504694 h; marks {'mid': 147, 'outcome': 3}
[2026-11-16T08:36:38Z] day 1794182400 opt-br  gated 227.413611662863: total 227.413611662863 = paid 223.724184972613 of reward 223.724184972613 on 14 of 150 markets + rebate 0.852636690250 + marks 2.836790000000; hits 47.440000000000 on 30 quoting markets; fills 25, 317.490000000000 shares, 0.000000000000 against crossing orders; scored 97.113097953343 h; marks {'mid': 147, 'outcome': 3}
[2026-11-16T08:36:38Z] day 1794182400 opt-ft  gated 180.968085035610: total 180.968085035610 = paid 189.608437195360 of reward 189.608437195360 on 13 of 150 markets + rebate 1.386557840250 + marks -10.026910000000; hits 47.440000000000 on 30 quoting markets; fills 38, 541.970000000000 shares, 219.650000000000 against crossing orders; scored 85.261756756952 h; marks {'mid': 147, 'outcome': 3}
[2026-11-16T08:36:38Z] day 1794182400 opt-fr  gated 227.561960382845: total 227.561960382845 = paid 223.671273692595 of reward 223.671273692595 on 14 of 150 markets + rebate 0.853896690250 + marks 3.036790000000; hits 47.440000000000 on 30 quoting markets; fills 25, 317.490000000000 shares, 0.000000000000 against crossing orders; scored 97.087692205601 h; marks {'mid': 147, 'outcome': 3}
[2026-11-16T08:36:38Z] day 1794182400 central gated 172.523771477069: total 172.523771477069 = paid 181.365383636819 of reward 184.794526457177 on 13 of 150 markets + rebate 1.385297840250 + marks -10.226910000000; hits 47.440000000000 on 30 quoting markets; fills 38, 541.970000000000 shares, 219.650000000000 against crossing orders; scored 85.184937715012 h; marks {'mid': 147, 'outcome': 3}, barred
[2026-11-16T08:36:38Z] day 1794182400: the least of pess-bt/pess-br/pess-ft/pess-fr, each less its hits, 123.436658293768 (pess-bt); the most of opt-bt/opt-br/opt-ft/opt-fr, 227.561960382845 (opt-fr)
[2026-11-16T08:36:38Z] day 1794268800 pess-bt gated 78.094476917559: total 127.974476917559 = paid 115.409201917559 of reward 118.245405422412 on 19 of 150 markets + rebate 0.000000000000 + marks 12.565275000000; hits 49.880000000000 on 30 quoting markets; fills 90, 1303.430000000000 shares, 533.020000000000 against crossing orders; scored 87.639805053722 h; marks {'mid': 145, 'outcome': 5}
[2026-11-16T08:36:38Z] day 1794268800 pess-br gated 71.088712287783: total 120.968712287783 = paid 118.545422287783 of reward 122.466310324383 on 17 of 150 markets + rebate 0.000000000000 + marks 2.423290000000; hits 49.880000000000 on 30 quoting markets; fills 53, 814.340000000000 shares, 0.000000000000 against crossing orders; scored 94.899627093761 h; marks {'mid': 145, 'outcome': 5}
[2026-11-16T08:36:38Z] day 1794268800 pess-ft gated 78.094476917559: total 127.974476917559 = paid 115.409201917559 of reward 118.245405422412 on 19 of 150 markets + rebate 0.000000000000 + marks 12.565275000000; hits 49.880000000000 on 30 quoting markets; fills 90, 1303.430000000000 shares, 533.020000000000 against crossing orders; scored 87.639805053722 h; marks {'mid': 145, 'outcome': 5}
[2026-11-16T08:36:38Z] day 1794268800 pess-fr gated 71.088712287783: total 120.968712287783 = paid 118.545422287783 of reward 122.466310324383 on 17 of 150 markets + rebate 0.000000000000 + marks 2.423290000000; hits 49.880000000000 on 30 quoting markets; fills 53, 814.340000000000 shares, 0.000000000000 against crossing orders; scored 94.899627093761 h; marks {'mid': 145, 'outcome': 5}
[2026-11-16T08:36:38Z] day 1794268800 opt-bt  gated 145.457197234497: total 145.457197234497 = paid 129.575325208247 of reward 129.575325208247 on 20 of 150 markets + rebate 3.316597026250 + marks 12.565275000000; hits 49.880000000000 on 30 quoting markets; fills 90, 1303.430000000000 shares, 533.020000000000 against crossing orders; scored 87.761302573061 h; marks {'mid': 145, 'outcome': 5}
[2026-11-16T08:36:38Z] day 1794268800 opt-br  gated 141.904096519035: total 141.904096519035 = paid 137.503899171910 of reward 137.503899171910 on 20 of 150 markets + rebate 1.976907347125 + marks 2.423290000000; hits 49.880000000000 on 30 quoting markets; fills 53, 814.340000000000 shares, 0.000000000000 against crossing orders; scored 94.989139461736 h; marks {'mid': 145, 'outcome': 5}
[2026-11-16T08:36:38Z] day 1794268800 opt-ft  gated 145.457197234497: total 145.457197234497 = paid 129.575325208247 of reward 129.575325208247 on 20 of 150 markets + rebate 3.316597026250 + marks 12.565275000000; hits 49.880000000000 on 30 quoting markets; fills 90, 1303.430000000000 shares, 533.020000000000 against crossing orders; scored 87.761302573061 h; marks {'mid': 145, 'outcome': 5}
[2026-11-16T08:36:38Z] day 1794268800 opt-fr  gated 141.904096519035: total 141.904096519035 = paid 137.503899171910 of reward 137.503899171910 on 20 of 150 markets + rebate 1.976907347125 + marks 2.423290000000; hits 49.880000000000 on 30 quoting markets; fills 53, 814.340000000000 shares, 0.000000000000 against crossing orders; scored 94.989139461736 h; marks {'mid': 145, 'outcome': 5}
[2026-11-16T08:36:38Z] day 1794268800 central gated 132.446470404454: total 132.446470404454 = paid 116.564598378204 of reward 119.453285863666 on 19 of 150 markets + rebate 3.316597026250 + marks 12.565275000000; hits 49.880000000000 on 30 quoting markets; fills 90, 1303.430000000000 shares, 533.020000000000 against crossing orders; scored 87.639805053722 h; marks {'mid': 145, 'outcome': 5}, barred
[2026-11-16T08:36:38Z] day 1794268800: the least of pess-bt/pess-br/pess-ft/pess-fr, each less its hits, 71.088712287783 (pess-br); the most of opt-bt/opt-br/opt-ft/opt-fr, 145.457197234497 (opt-ft)
[2026-11-16T08:36:38Z] day 1794355200 pess-bt gated 46.861687328044: total 89.441687328044 = paid 89.593187328044 of reward 92.024603482477 on 17 of 150 markets + rebate 0.000000000000 + marks -0.151500000000; hits 42.580000000000 on 29 quoting markets; fills 24, 264.820000000000 shares, 95.700000000000 against crossing orders; scored 88.420849114434 h; marks {'mid': 139, 'outcome': 11}
[2026-11-16T08:36:38Z] day 1794355200 pess-br gated 67.103361256514: total 109.683361256514 = paid 111.337361256514 of reward 111.980114672768 on 20 of 150 markets + rebate 0.000000000000 + marks -1.654000000000; hits 42.580000000000 on 29 quoting markets; fills 14, 169.120000000000 shares, 0.000000000000 against crossing orders; scored 96.648551186099 h; marks {'mid': 139, 'outcome': 11}
[2026-11-16T08:36:38Z] day 1794355200 pess-ft gated 46.861687328044: total 89.441687328044 = paid 89.593187328044 of reward 92.024603482477 on 17 of 150 markets + rebate 0.000000000000 + marks -0.151500000000; hits 42.580000000000 on 29 quoting markets; fills 24, 264.820000000000 shares, 95.700000000000 against crossing orders; scored 88.420849114434 h; marks {'mid': 139, 'outcome': 11}
[2026-11-16T08:36:38Z] day 1794355200 pess-fr gated 67.103361256514: total 109.683361256514 = paid 111.337361256514 of reward 111.980114672768 on 20 of 150 markets + rebate 0.000000000000 + marks -1.654000000000; hits 42.580000000000 on 29 quoting markets; fills 14, 169.120000000000 shares, 0.000000000000 against crossing orders; scored 96.648551186099 h; marks {'mid': 139, 'outcome': 11}
[2026-11-16T08:36:38Z] day 1794355200 opt-bt  gated 95.432330916439: total 95.432330916439 = paid 95.005807443939 of reward 95.005807443939 on 18 of 150 markets + rebate 0.578023472500 + marks -0.151500000000; hits 42.580000000000 on 29 quoting markets; fills 24, 264.820000000000 shares, 95.700000000000 against crossing orders; scored 88.478768813136 h; marks {'mid': 139, 'outcome': 11}
[2026-11-16T08:36:38Z] day 1794355200 opt-br  gated 113.798472475131: total 113.798472475131 = paid 115.114302852631 of reward 115.114302852631 on 20 of 150 markets + rebate 0.338169622500 + marks -1.654000000000; hits 42.580000000000 on 29 quoting markets; fills 14, 169.120000000000 shares, 0.000000000000 against crossing orders; scored 96.708452636610 h; marks {'mid': 139, 'outcome': 11}
[2026-11-16T08:36:38Z] day 1794355200 opt-ft  gated 95.432330916439: total 95.432330916439 = paid 95.005807443939 of reward 95.005807443939 on 18 of 150 markets + rebate 0.578023472500 + marks -0.151500000000; hits 42.580000000000 on 29 quoting markets; fills 24, 264.820000000000 shares, 95.700000000000 against crossing orders; scored 88.478768813136 h; marks {'mid': 139, 'outcome': 11}
[2026-11-16T08:36:38Z] day 1794355200 opt-fr  gated 113.798472475131: total 113.798472475131 = paid 115.114302852631 of reward 115.114302852631 on 20 of 150 markets + rebate 0.338169622500 + marks -1.654000000000; hits 42.580000000000 on 29 quoting markets; fills 14, 169.120000000000 shares, 0.000000000000 against crossing orders; scored 96.708452636610 h; marks {'mid': 139, 'outcome': 11}
[2026-11-16T08:36:38Z] day 1794355200 central gated 91.754017242820: total 91.754017242820 = paid 91.327493770320 of reward 92.948886023496 on 18 of 150 markets + rebate 0.578023472500 + marks -0.151500000000; hits 42.580000000000 on 29 quoting markets; fills 24, 264.820000000000 shares, 95.700000000000 against crossing orders; scored 88.420849114434 h; marks {'mid': 139, 'outcome': 11}, barred
[2026-11-16T08:36:38Z] day 1794355200: the least of pess-bt/pess-br/pess-ft/pess-fr, each less its hits, 46.861687328044 (pess-bt); the most of opt-bt/opt-br/opt-ft/opt-fr, 113.798472475131 (opt-fr)
[2026-11-16T08:36:38Z] day 1794441600 pess-bt gated 28.679658265034: total 57.499658265034 = paid 64.306408265034 of reward 68.241333303331 on 7 of 150 markets + rebate 0.000000000000 + marks -6.806750000000; hits 28.820000000000 on 20 quoting markets; fills 14, 193.150000000000 shares, 90.000000000000 against crossing orders; scored 47.124852821102 h; marks {'outcome': 5, 'mid': 145}
[2026-11-16T08:36:38Z] day 1794441600 pess-br gated 68.260676485620: total 97.280676485620 = paid 95.477426485620 of reward 98.991031823402 on 8 of 150 markets + rebate 0.000000000000 + marks 1.803250000000; hits 29.020000000000 on 20 quoting markets; fills 9, 103.150000000000 shares, 0.000000000000 against crossing orders; scored 52.486444827517 h; marks {'outcome': 5, 'mid': 145}
[2026-11-16T08:36:38Z] day 1794441600 pess-ft gated 28.679658265034: total 57.499658265034 = paid 64.306408265034 of reward 68.241333303331 on 7 of 150 markets + rebate 0.000000000000 + marks -6.806750000000; hits 28.820000000000 on 20 quoting markets; fills 14, 193.150000000000 shares, 90.000000000000 against crossing orders; scored 47.124852821102 h; marks {'outcome': 5, 'mid': 145}
[2026-11-16T08:36:38Z] day 1794441600 pess-fr gated 68.260676485620: total 97.280676485620 = paid 95.477426485620 of reward 98.991031823402 on 8 of 150 markets + rebate 0.000000000000 + marks 1.803250000000; hits 29.020000000000 on 20 quoting markets; fills 9, 103.150000000000 shares, 0.000000000000 against crossing orders; scored 52.486444827517 h; marks {'outcome': 5, 'mid': 145}
[2026-11-16T08:36:38Z] day 1794441600 opt-bt  gated 64.185618383038: total 64.185618383038 = paid 70.594284138288 of reward 70.594284138288 on 8 of 150 markets + rebate 0.398084244750 + marks -6.806750000000; hits 28.820000000000 on 20 quoting markets; fills 14, 193.150000000000 shares, 90.000000000000 against crossing orders; scored 47.230450695510 h; marks {'outcome': 5, 'mid': 145}
[2026-11-16T08:36:38Z] day 1794441600 opt-br  gated 104.729043240317: total 104.729043240317 = paid 102.755990945567 of reward 102.755990945567 on 9 of 150 markets + rebate 0.169802294750 + marks 1.803250000000; hits 29.020000000000 on 20 quoting markets; fills 9, 103.150000000000 shares, 0.000000000000 against crossing orders; scored 52.592042701925 h; marks {'outcome': 5, 'mid': 145}
[2026-11-16T08:36:38Z] day 1794441600 opt-ft  gated 64.185618383038: total 64.185618383038 = paid 70.594284138288 of reward 70.594284138288 on 8 of 150 markets + rebate 0.398084244750 + marks -6.806750000000; hits 28.820000000000 on 20 quoting markets; fills 14, 193.150000000000 shares, 90.000000000000 against crossing orders; scored 47.230450695510 h; marks {'outcome': 5, 'mid': 145}
[2026-11-16T08:36:38Z] day 1794441600 opt-fr  gated 104.729043240317: total 104.729043240317 = paid 102.755990945567 of reward 102.755990945567 on 9 of 150 markets + rebate 0.169802294750 + marks 1.803250000000; hits 29.020000000000 on 20 quoting markets; fills 9, 103.150000000000 shares, 0.000000000000 against crossing orders; scored 52.592042701925 h; marks {'outcome': 5, 'mid': 145}
[2026-11-16T08:36:38Z] day 1794441600 central gated 59.061478254124: total 59.061478254124 = paid 65.470144009374 of reward 68.513776306785 on 8 of 150 markets + rebate 0.398084244750 + marks -6.806750000000; hits 28.820000000000 on 20 quoting markets; fills 14, 193.150000000000 shares, 90.000000000000 against crossing orders; scored 47.124852821102 h; marks {'outcome': 5, 'mid': 145}, barred
[2026-11-16T08:36:38Z] day 1794441600: the least of pess-bt/pess-br/pess-ft/pess-fr, each less its hits, 28.679658265034 (pess-bt); the most of opt-bt/opt-br/opt-ft/opt-fr, 104.729043240317 (opt-fr)
[2026-11-16T08:36:38Z] day 1794528000 pess-bt gated 86.201077294943: total 114.121077294943 = paid 113.601652294943 of reward 116.471064519652 on 8 of 150 markets + rebate 0.000000000000 + marks 0.519425000000; hits 27.920000000000 on 18 quoting markets; fills 42, 603.610000000000 shares, 130.840000000000 against crossing orders; scored 29.125498259104 h; marks {'mid': 150}
[2026-11-16T08:36:38Z] day 1794528000 pess-br gated 106.872541324010: total 134.772541324010 = paid 137.583366324010 of reward 139.752721628065 on 8 of 150 markets + rebate 0.000000000000 + marks -2.810825000000; hits 27.900000000000 on 18 quoting markets; fills 37, 481.760000000000 shares, 0.000000000000 against crossing orders; scored 32.096623895557 h; marks {'mid': 150}
[2026-11-16T08:36:38Z] day 1794528000 pess-ft gated 86.201077294943: total 114.121077294943 = paid 113.601652294943 of reward 116.471064519652 on 8 of 150 markets + rebate 0.000000000000 + marks 0.519425000000; hits 27.920000000000 on 18 quoting markets; fills 42, 603.610000000000 shares, 130.840000000000 against crossing orders; scored 29.125498259104 h; marks {'mid': 150}
[2026-11-16T08:36:38Z] day 1794528000 pess-fr gated 106.872541324010: total 134.772541324010 = paid 137.583366324010 of reward 139.752721628065 on 8 of 150 markets + rebate 0.000000000000 + marks -2.810825000000; hits 27.900000000000 on 18 quoting markets; fills 37, 481.760000000000 shares, 0.000000000000 against crossing orders; scored 32.096623895557 h; marks {'mid': 150}
[2026-11-16T08:36:38Z] day 1794528000 opt-bt  gated 125.384874428017: total 125.384874428017 = paid 123.397272976142 of reward 123.397272976142 on 9 of 150 markets + rebate 1.468176451875 + marks 0.519425000000; hits 27.920000000000 on 18 quoting markets; fills 42, 603.610000000000 shares, 130.840000000000 against crossing orders; scored 29.214151913321 h; marks {'mid': 150}
[2026-11-16T08:36:38Z] day 1794528000 opt-br  gated 145.351473469262: total 145.351473469262 = paid 146.975098117387 of reward 146.975098117387 on 9 of 150 markets + rebate 1.187200351875 + marks -2.810825000000; hits 27.900000000000 on 18 quoting markets; fills 37, 481.760000000000 shares, 0.000000000000 against crossing orders; scored 32.216755095135 h; marks {'mid': 150}
[2026-11-16T08:36:38Z] day 1794528000 opt-ft  gated 125.384874428017: total 125.384874428017 = paid 123.397272976142 of reward 123.397272976142 on 9 of 150 markets + rebate 1.468176451875 + marks 0.519425000000; hits 27.920000000000 on 18 quoting markets; fills 42, 603.610000000000 shares, 130.840000000000 against crossing orders; scored 29.214151913321 h; marks {'mid': 150}
[2026-11-16T08:36:38Z] day 1794528000 opt-fr  gated 145.351473469262: total 145.351473469262 = paid 146.975098117387 of reward 146.975098117387 on 9 of 150 markets + rebate 1.187200351875 + marks -2.810825000000; hits 27.900000000000 on 18 quoting markets; fills 37, 481.760000000000 shares, 0.000000000000 against crossing orders; scored 32.216755095135 h; marks {'mid': 150}
[2026-11-16T08:36:38Z] day 1794528000 central gated 116.991524328167: total 116.991524328167 = paid 115.003922876292 of reward 118.058851414482 on 8 of 150 markets + rebate 1.468176451875 + marks 0.519425000000; hits 27.920000000000 on 18 quoting markets; fills 42, 603.610000000000 shares, 130.840000000000 against crossing orders; scored 29.125498259104 h; marks {'mid': 150}, barred
[2026-11-16T08:36:38Z] day 1794528000: the least of pess-bt/pess-br/pess-ft/pess-fr, each less its hits, 86.201077294943 (pess-bt); the most of opt-bt/opt-br/opt-ft/opt-fr, 145.351473469262 (opt-fr)
[2026-11-16T08:36:38Z] days whose least is at or above 10: 5 of 5, the least 28.679658265034; days whose most is below it: 0 of 5, the most 227.561960382845
[2026-11-16T08:36:38Z] pess-bt: over the 5 days 363.273558099347, a day 72.654711619869
[2026-11-16T08:36:38Z] pess-br: over the 5 days 483.495915334475, a day 96.699183066895
[2026-11-16T08:36:38Z] pess-ft: over the 5 days 363.473558099347, a day 72.694711619869
[2026-11-16T08:36:38Z] pess-fr: over the 5 days 483.695915334475, a day 96.739183066895
[2026-11-16T08:36:38Z] opt-bt: over the 5 days 611.279757277618, a day 122.255951455524
[2026-11-16T08:36:38Z] opt-br: over the 5 days 733.196697366609, a day 146.639339473322
[2026-11-16T08:36:38Z] opt-ft: over the 5 days 611.428105997600, a day 122.285621199520
[2026-11-16T08:36:38Z] opt-fr: over the 5 days 733.345046086591, a day 146.669009217318
[2026-11-16T08:36:38Z] central: over the 5 days 572.777261706635, a day 114.555452341327, barred
[2026-11-16T08:36:38Z] L0-W EARN: EARN True, NO EARN False; reading.json sha256 874f576a9c082c32674d63b3134a9325d7add2935712f2118f994406cb2c1e08
```

`logs/81-score-again.log` printed every one of those lines again, identically, and `unchanged /root/tz45-work/reading.json sha256 874f576a9c082c32674d63b3134a9325d7add2935712f2118f994406cb2c1e08`.

### 2.5 The pack, every day (`logs/82-pack.log`; `logs/83-pack-again.log`, there `unchanged`)

```
[2026-11-16T08:36:51Z] G-SOURCE PASS: 22 of 22 equal to this run's own record, 30340669 bytes; held 0.0 s, from second 411, 0.08 s
[2026-11-16T08:36:52Z] day 1794182400 (2026-11-09): 194 names - select 2, slot 96, rewards 96, stream 0 and other 0 never opened; rewardbook-inputs-1794182400.tar 194 members, 16195174 bytes, of 97 files of replies scanned; withheld 0, 0 bytes; wrote 16353280 bytes sha256 3f1cefb098f538dde99dadc13aba9a6c0be2e44bcc761ccfa6516350e8d0d9db; budget 63 s, held 0.0 s, from second 411, 1.27 s
[2026-11-16T08:36:54Z] day 1794268800 (2026-11-10): 194 names - select 2, slot 96, rewards 96, stream 0 and other 0 never opened; rewardbook-inputs-1794268800.tar 194 members, 16000346 bytes, of 97 files of replies scanned; withheld 0, 0 bytes; wrote 16148480 bytes sha256 35a219bcd999c17bba8b8b8f664fd3d3107c4367e1f573dfe38ba2509ea34f8c; budget 63 s, held 0.0 s, from second 412, 1.37 s
[2026-11-16T08:36:55Z] day 1794355200 (2026-11-11): 194 names - select 2, slot 96, rewards 96, stream 0 and other 0 never opened; rewardbook-inputs-1794355200.tar 194 members, 15707431 bytes, of 97 files of replies scanned; withheld 0, 0 bytes; wrote 15861760 bytes sha256 fd5df7d694a8d25d246c3189bdf8a9a64597a8d040ad2585d46852f5ce7fc2c6; budget 62 s, held 0.0 s, from second 414, 1.41 s
[2026-11-16T08:36:56Z] day 1794441600 (2026-11-12): 194 names - select 2, slot 96, rewards 96, stream 0 and other 0 never opened; rewardbook-inputs-1794441600.tar 194 members, 14569896 bytes, of 97 files of replies scanned; withheld 0, 0 bytes; wrote 14714880 bytes sha256 840a13670100aee0cc584b06b1b4cc85cbfc0161ef0a183603d9056fa7024dfb; budget 60 s, held 0.0 s, from second 415, 1.25 s
[2026-11-16T08:36:58Z] day 1794528000 (2026-11-13): 194 names - select 2, slot 96, rewards 96, stream 0 and other 0 never opened; rewardbook-inputs-1794528000.tar 194 members, 15431045 bytes, of 97 files of replies scanned; withheld 0, 0 bytes; wrote 15575040 bytes sha256 ed98acd9ccd70d492dd0fdba4f4e4a465531f92a557b165ea2046c5aee826f48; budget 61 s, held 0.0 s, from second 416, 1.24 s
[2026-11-16T08:36:58Z] wrote /root/tz45-work/out/tz45-manifest.json 171407 bytes sha256 23843e59372a48409a287f91f8a14d243d7b0bb29228748f1d6b2b8572f806b3
[2026-11-16T08:36:58Z] wrote /root/tz45-work/release-set.json 6082 bytes sha256 442055028a700f7b4694a70b44267d41fa7fdec3e0a178057ec23ba88273057f
[2026-11-16T08:36:58Z] G-PACK PASS: 5 days of 5, 970 members, 77903892 bytes of members, 78653440 bytes of archives; withheld 0 files of replies, 0 bytes; streams 0 and other names 0 never opened; 28 assets, 109165516 bytes; days over their budget 0; outputs {'wrote': 7}
[2026-11-16T08:36:58Z] G-RESERVE PASS: the store opened 1455 times - once a member kept, 970, and once a file of replies scanned, 485 - and listed 5 times, one a day; no other open or listing under /var/lib/btc-rewardbook
[2026-11-16T08:37:10Z] G-SOURCE PASS: 22 of 22 equal to this run's own record, 30340669 bytes; held 0.0 s, from second 430, 0.08 s
[2026-11-16T08:37:18Z] unchanged /root/tz45-work/out/tz45-manifest.json 171407 bytes sha256 23843e59372a48409a287f91f8a14d243d7b0bb29228748f1d6b2b8572f806b3
[2026-11-16T08:37:18Z] unchanged /root/tz45-work/release-set.json 6082 bytes sha256 442055028a700f7b4694a70b44267d41fa7fdec3e0a178057ec23ba88273057f
[2026-11-16T08:37:18Z] G-PACK PASS: 5 days of 5, 970 members, 77903892 bytes of members, 78653440 bytes of archives; withheld 0 files of replies, 0 bytes; streams 0 and other names 0 never opened; 28 assets, 109165516 bytes; days over their budget 0; outputs {'unchanged': 7}
[2026-11-16T08:37:18Z] G-RESERVE PASS: the store opened 1455 times - once a member kept, 970, and once a file of replies scanned, 485 - and listed 5 times, one a day; no other open or listing under /var/lib/btc-rewardbook
[2026-11-16T08:37:18Z] DETERMINISM PASS: 7 of 7 outputs unchanged
```

**Files withheld: none**, 0 files and 0 bytes, on every day.

### 2.6 The Release's set — every asset by name, bytes and SHA-256, in upload order (`release-set.json`, SHA-256 `442055028a700f7b4694a70b44267d41fa7fdec3e0a178057ec23ba88273057f`)

| # | asset | bytes | SHA-256 — local, as `pack` wrote it |
|---|---|---|---|
| 1 | `rewardbook-inputs-1794182400.tar` | 16,353,280 | `3f1cefb098f538dde99dadc13aba9a6c0be2e44bcc761ccfa6516350e8d0d9db` |
| 2 | `rewardbook-inputs-1794268800.tar` | 16,148,480 | `35a219bcd999c17bba8b8b8f664fd3d3107c4367e1f573dfe38ba2509ea34f8c` |
| 3 | `rewardbook-inputs-1794355200.tar` | 15,861,760 | `fd5df7d694a8d25d246c3189bdf8a9a64597a8d040ad2585d46852f5ce7fc2c6` |
| 4 | `rewardbook-inputs-1794441600.tar` | 14,714,880 | `840a13670100aee0cc584b06b1b4cc85cbfc0161ef0a183603d9056fa7024dfb` |
| 5 | `rewardbook-inputs-1794528000.tar` | 15,575,040 | `ed98acd9ccd70d492dd0fdba4f4e4a465531f92a557b165ea2046c5aee826f48` |
| 6 | `tz45-set.json` | 4,432 | `25eb1cba98ccd6d68fac5ad8c86da06677fd400483e8f27761ec21a23cffd462` |
| 7 | `tz45-reading.json` | 23,431 | `874f576a9c082c32674d63b3134a9325d7add2935712f2118f994406cb2c1e08` |
| 8 | `tz45-fetch-1794182400.json` | 55,682 | `6d6b0bd4e2dd39b936787c41b1dfd56e1e225dadebb25c79937e7771308090e5` |
| 9 | `tz45-fetch-1794182400.polls.jsonl` | 5,771,356 | `bafbfb4a04b2a83d110a75fc03d311bfb53802667d7ec0938c295cb4656ccaa1` |
| 10 | `tz45-days-1794182400.json` | 415,576 | `8486a5888ff2cbb23446c633e7991e5895accb8576cc13a8f37fff70cbe01aa7` |
| 11 | `tz45-days-1794182400.slots.txt` | 118,051 | `071bb0609497f08d85da6712446dc60b17796d909d3a6f30ec6a22d53cce20f8` |
| 12 | `tz45-fetch-1794268800.json` | 55,693 | `3c90f5a48be59c5d1ef4822adee950eac4c14f0b9572142c495b3d6af9b4be15` |
| 13 | `tz45-fetch-1794268800.polls.jsonl` | 5,743,103 | `3a48a45a0ed5d93e6cbda1c16de951ddfa56a1b45112b4087f8c83d7051bbba1` |
| 14 | `tz45-days-1794268800.json` | 417,507 | `fd162966f292d9d8c958c99c696bc2ecd20cfa12e87114b88ee61bd7255a9fe3` |
| 15 | `tz45-days-1794268800.slots.txt` | 118,803 | `876bf5a6d8c9a0f5f8db04f7a89cdbaafe7a8d6e2aac7f61a2c8d406fba9b58e` |
| 16 | `tz45-fetch-1794355200.json` | 53,508 | `065f89f2e2cc1214ec1ee634a3e1d4dc21f9ce0ff102d0ae94645b0b067b0c73` |
| 17 | `tz45-fetch-1794355200.polls.jsonl` | 5,193,469 | `63d997837a0146a08ffb13324b5fac96fb494191da197df91c68a457650d493d` |
| 18 | `tz45-days-1794355200.json` | 414,400 | `900307a8e41ca4579491482654cf1d3bc756268a166f5641455cb26e6b90c673` |
| 19 | `tz45-days-1794355200.slots.txt` | 107,907 | `981c985e5f4208eee0ddb10f4b5d3cb1eff5e1daa7a52a36bfcd19733e5924a2` |
| 20 | `tz45-fetch-1794441600.json` | 55,683 | `0ae5be7dc825fcb75068f52302be92d6fa4da2ced9a9895e96d8b8a5947b7a48` |
| 21 | `tz45-fetch-1794441600.polls.jsonl` | 5,600,221 | `d35cd64290914e370d59252760504435a6a503a636e5410972d552af223f4481` |
| 22 | `tz45-days-1794441600.json` | 406,921 | `9ce2ca6d1e356196f18db4090bc7091323f63cb66fc1ca768ae8c3d8c4be162f` |
| 23 | `tz45-days-1794441600.slots.txt` | 118,366 | `a3351cecbb54249db9e42b4de635afccaf70c78ffff4090b42a1cbfbb60ed801` |
| 24 | `tz45-fetch-1794528000.json` | 53,341 | `1a6c2d17a63bf78e718477ad0af8a547d3a088240d0bc9e8754c78f675e800d8` |
| 25 | `tz45-fetch-1794528000.polls.jsonl` | 5,099,550 | `8b9ed8b9936807ece05718c96558aa9896cd92502a1f7f983ecc9923e67e56f0` |
| 26 | `tz45-days-1794528000.json` | 407,006 | `6dfb638cd08f7c338347d620ed3ed9e9e0aebcf200fab34bb6aeb0a6b7050084` |
| 27 | `tz45-days-1794528000.slots.txt` | 106,663 | `74d6c047066307175769f4c5cac13fdcd0aaeba7d5d28f80acaeeb779688cdaa` |
| 28 | `tz45-manifest.json` | 171,407 | `23843e59372a48409a287f91f8a14d243d7b0bb29228748f1d6b2b8572f806b3` |

**Each asset's record and download, as `I verify` printed it** (`logs/88-verify.log`). The download column is the full anonymous download hashed as it arrived, equal to the local SHA-256 above:

```
[2026-11-16T10:23:35Z] V rewardbook-inputs-1794182400.tar id 754391172 state uploaded api True bytes 16353280 digest sha256:3f1cefb098f538dde99dadc13aba9a6c0be2e44bcc761ccfa6516350e8d0d9db url True download True
[2026-11-16T10:23:35Z] V rewardbook-inputs-1794268800.tar id 754391257 state uploaded api True bytes 16148480 digest sha256:35a219bcd999c17bba8b8b8f664fd3d3107c4367e1f573dfe38ba2509ea34f8c url True download True
[2026-11-16T10:23:35Z] V rewardbook-inputs-1794355200.tar id 754391320 state uploaded api True bytes 15861760 digest sha256:fd5df7d694a8d25d246c3189bdf8a9a64597a8d040ad2585d46852f5ce7fc2c6 url True download True
[2026-11-16T10:23:35Z] V rewardbook-inputs-1794441600.tar id 754391410 state uploaded api True bytes 14714880 digest sha256:840a13670100aee0cc584b06b1b4cc85cbfc0161ef0a183603d9056fa7024dfb url True download True
[2026-11-16T10:23:35Z] V rewardbook-inputs-1794528000.tar id 754391547 state uploaded api True bytes 15575040 digest sha256:ed98acd9ccd70d492dd0fdba4f4e4a465531f92a557b165ea2046c5aee826f48 url True download True
[2026-11-16T10:23:35Z] V tz45-set.json id 754391644 state uploaded api True bytes 4432 digest sha256:25eb1cba98ccd6d68fac5ad8c86da06677fd400483e8f27761ec21a23cffd462 url True download True
[2026-11-16T10:23:35Z] V tz45-reading.json id 754391695 state uploaded api True bytes 23431 digest sha256:874f576a9c082c32674d63b3134a9325d7add2935712f2118f994406cb2c1e08 url True download True
[2026-11-16T10:23:35Z] V tz45-fetch-1794182400.json id 754391756 state uploaded api True bytes 55682 digest sha256:6d6b0bd4e2dd39b936787c41b1dfd56e1e225dadebb25c79937e7771308090e5 url True download True
[2026-11-16T10:23:35Z] V tz45-fetch-1794182400.polls.jsonl id 754391796 state uploaded api True bytes 5771356 digest sha256:bafbfb4a04b2a83d110a75fc03d311bfb53802667d7ec0938c295cb4656ccaa1 url True download True
[2026-11-16T10:23:35Z] V tz45-days-1794182400.json id 754391841 state uploaded api True bytes 415576 digest sha256:8486a5888ff2cbb23446c633e7991e5895accb8576cc13a8f37fff70cbe01aa7 url True download True
[2026-11-16T10:23:35Z] V tz45-days-1794182400.slots.txt id 754391886 state uploaded api True bytes 118051 digest sha256:071bb0609497f08d85da6712446dc60b17796d909d3a6f30ec6a22d53cce20f8 url True download True
[2026-11-16T10:23:35Z] V tz45-fetch-1794268800.json id 754391927 state uploaded api True bytes 55693 digest sha256:3c90f5a48be59c5d1ef4822adee950eac4c14f0b9572142c495b3d6af9b4be15 url True download True
[2026-11-16T10:23:35Z] V tz45-fetch-1794268800.polls.jsonl id 754391969 state uploaded api True bytes 5743103 digest sha256:3a48a45a0ed5d93e6cbda1c16de951ddfa56a1b45112b4087f8c83d7051bbba1 url True download True
[2026-11-16T10:23:35Z] V tz45-days-1794268800.json id 754392064 state uploaded api True bytes 417507 digest sha256:fd162966f292d9d8c958c99c696bc2ecd20cfa12e87114b88ee61bd7255a9fe3 url True download True
[2026-11-16T10:23:35Z] V tz45-days-1794268800.slots.txt id 754392118 state uploaded api True bytes 118803 digest sha256:876bf5a6d8c9a0f5f8db04f7a89cdbaafe7a8d6e2aac7f61a2c8d406fba9b58e url True download True
[2026-11-16T10:23:35Z] V tz45-fetch-1794355200.json id 754392159 state uploaded api True bytes 53508 digest sha256:065f89f2e2cc1214ec1ee634a3e1d4dc21f9ce0ff102d0ae94645b0b067b0c73 url True download True
[2026-11-16T10:23:35Z] V tz45-fetch-1794355200.polls.jsonl id 754392219 state uploaded api True bytes 5193469 digest sha256:63d997837a0146a08ffb13324b5fac96fb494191da197df91c68a457650d493d url True download True
[2026-11-16T10:23:35Z] V tz45-days-1794355200.json id 754392301 state uploaded api True bytes 414400 digest sha256:900307a8e41ca4579491482654cf1d3bc756268a166f5641455cb26e6b90c673 url True download True
[2026-11-16T10:23:35Z] V tz45-days-1794355200.slots.txt id 754392360 state uploaded api True bytes 107907 digest sha256:981c985e5f4208eee0ddb10f4b5d3cb1eff5e1daa7a52a36bfcd19733e5924a2 url True download True
[2026-11-16T10:23:35Z] V tz45-fetch-1794441600.json id 754392429 state uploaded api True bytes 55683 digest sha256:0ae5be7dc825fcb75068f52302be92d6fa4da2ced9a9895e96d8b8a5947b7a48 url True download True
[2026-11-16T10:23:35Z] V tz45-fetch-1794441600.polls.jsonl id 754392494 state uploaded api True bytes 5600221 digest sha256:d35cd64290914e370d59252760504435a6a503a636e5410972d552af223f4481 url True download True
[2026-11-16T10:23:35Z] V tz45-days-1794441600.json id 754392554 state uploaded api True bytes 406921 digest sha256:9ce2ca6d1e356196f18db4090bc7091323f63cb66fc1ca768ae8c3d8c4be162f url True download True
[2026-11-16T10:23:35Z] V tz45-days-1794441600.slots.txt id 754392617 state uploaded api True bytes 118366 digest sha256:a3351cecbb54249db9e42b4de635afccaf70c78ffff4090b42a1cbfbb60ed801 url True download True
[2026-11-16T10:23:35Z] V tz45-fetch-1794528000.json id 754392669 state uploaded api True bytes 53341 digest sha256:1a6c2d17a63bf78e718477ad0af8a547d3a088240d0bc9e8754c78f675e800d8 url True download True
[2026-11-16T10:23:35Z] V tz45-fetch-1794528000.polls.jsonl id 754392718 state uploaded api True bytes 5099550 digest sha256:8b9ed8b9936807ece05718c96558aa9896cd92502a1f7f983ecc9923e67e56f0 url True download True
[2026-11-16T10:23:35Z] V tz45-days-1794528000.json id 754392783 state uploaded api True bytes 407006 digest sha256:6dfb638cd08f7c338347d620ed3ed9e9e0aebcf200fab34bb6aeb0a6b7050084 url True download True
[2026-11-16T10:23:35Z] V tz45-days-1794528000.slots.txt id 754392830 state uploaded api True bytes 106663 digest sha256:74d6c047066307175769f4c5cac13fdcd0aaeba7d5d28f80acaeeb779688cdaa url True download True
[2026-11-16T10:23:35Z] V tz45-manifest.json id 754392897 state uploaded api True bytes 171407 digest sha256:23843e59372a48409a287f91f8a14d243d7b0bb29228748f1d6b2b8572f806b3 url True download True
[2026-11-16T10:23:35Z] tag tz-45-l0-rule-w-inputs on origin: 01756f665893096ab38ae10dfbe58f074f8fb648, peeled None; the pack's commit 01756f665893096ab38ae10dfbe58f074f8fb648; the Release's target 01756f665893096ab38ae10dfbe58f074f8fb648
[2026-11-16T10:23:35Z] G-TAG/G-UPLOAD/G-DOWNLOAD release published on the tag                             True
[2026-11-16T10:23:35Z] G-TAG/G-UPLOAD/G-DOWNLOAD no asset missing                                         True
[2026-11-16T10:23:35Z] G-TAG/G-UPLOAD/G-DOWNLOAD no asset beyond the set                                  True
[2026-11-16T10:23:35Z] G-TAG/G-UPLOAD/G-DOWNLOAD every asset uploaded, its bytes and digest the set's     True
[2026-11-16T10:23:35Z] G-TAG/G-UPLOAD/G-DOWNLOAD every download the set's bytes and SHA-256               True
[2026-11-16T10:23:35Z] G-TAG/G-UPLOAD/G-DOWNLOAD the tag on origin lightweight, at the pack's commit      True
[2026-11-16T10:23:35Z] transfers 61, upload's and verify's: 0 started outside the idle stretch, 0 ended after its second 590; 0.0 s held
[2026-11-16T10:23:35Z] G-UPLOAD PASS: 28 of 28 assets by name, bytes, state and digest; G-DOWNLOAD PASS: 28 of 28 downloads, 109165516 bytes; G-TAG PASS: tz-45-l0-rule-w-inputs at 01756f665893096ab38ae10dfbe58f074f8fb648
```

### 2.7 B-UPLOAD — who ran it and when (`logs/85-upload.log`, `logs/86-upload-wait.log`)

**The Boss ran it**, in a root shell on the VPS, **once**: `run begun` at `2026-11-16T10:20:43.285319850Z`, `exit=0` at 10:21:16 UTC. The paste was handed over at 08:37:24 UTC. At 09:13:27 UTC, when the log did not yet exist, the same paste was restated to the Boss once in the session; that restatement is recorded in `86-upload-wait.log` as a reminder, not as a second hand-over. The run came 6,199 s after the first hand-over, inside the `21,600` s.

```
2026-11-16T10:20:43.285319850Z
run begun
[2026-11-16T10:20:43Z] MemAvailable 254685184 bytes, floor 172658448; free 9210212352 bytes, floor 7500000000
[2026-11-16T10:20:43Z] set 442055028a700f7b4694a70b44267d41fa7fdec3e0a178057ec23ba88273057f: 28 assets, 109165516 bytes, at commit 01756f665893096ab38ae10dfbe58f074f8fb648
[2026-11-16T10:20:43Z] credential: the primary checkout's remote URL
[2026-11-16T10:20:45Z] created the Release on tz-45-l0-rule-w-inputs, id 446880816, target 01756f665893096ab38ae10dfbe58f074f8fb648
[2026-11-16T10:21:16Z] U {"action": "complete", "assets": 28, "at": "2026-11-16T10:21:16Z", "created": true, "credential": "the primary checkout's remote URL", "held": 0, "release_id": 446880816, "sent": 28, "wall_ns": 1794824476653778408}
[2026-11-16T10:21:16Z] transfers so far 31: 0 started outside the idle stretch, 0 ended after its second 590; 0.0 s held
[2026-11-16T10:21:16Z] UPLOAD COMPLETE: Release 446880816 on tz-45-l0-rule-w-inputs, 28 assets - 28 sent, 0 already held - 109165516 bytes
exit=0
```

```
hand-over 1 of B-UPLOAD
2026-11-16T08:37:24Z
85-upload.log absent: 0 exit lines
2026-11-16T09:03:03Z
exit lines 0 of 1; runs begun 0; upload processes 0
tail: cannot open '/root/tz45-work/logs/85-upload.log' for reading: No such file or directory
reminder of hand-over 1 (the same paste, not run yet)
2026-11-16T09:13:27Z
2026-11-16T10:21:41Z
exit lines 1 of 1; runs begun 1; upload processes 0
[2026-11-16T10:21:16Z] transfers so far 31: 0 started outside the idle stretch, 0 ended after its second 590; 0.0 s held
[2026-11-16T10:21:16Z] UPLOAD COMPLETE: Release 446880816 on tz-45-l0-rule-w-inputs, 28 assets - 28 sent, 0 already held - 109165516 bytes
[2026-11-16T10:21:16Z] malloc tuned: True
[2026-11-16T10:21:16Z] peak memory of this run: 47976448 bytes
[2026-11-16T10:21:16Z] opens refused: 0, by TZ-27's hook: 0; reward book opens: 0, listings: 0
exit=0
```

The first run of the wait block printed `exit lines 0 of 1; runs begun 0; upload processes 0` — the Boss had not yet run the paste. The second printed `exit lines 1 of 1; runs begun 1; upload processes 0` with `UPLOAD COMPLETE` and `exit=0`. `upload.jsonl` holds 29 lines, its last `complete`. `transfers.jsonl` holds 61 lines, upload's 31 and verify's 30.

### 2.8 The archive's record (`logs/40-archive.log`; `logs/97-archive-again.log` equal to it line for line but for the stamps)

```
[2026-11-16T07:51:21Z] btc-rewardbook-archive.timer {'NextElapseUSecRealtime': 'Tue 2026-11-17 01:30:20 UTC', 'LastTriggerUSec': 'Mon 2026-11-16 01:30:20 UTC', 'Result': 'success', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-11-16T07:51:21Z] btc-rewardbook-archive.service {'Result': 'success', 'ExecMainStatus': '0', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-11-16T07:51:21Z] ledger /var/lib/btc-rewardbook-archive/ledger.jsonl: 71648 bytes sha256 30c915eacbbeca8905da2eafd20d1477b86f9930b96436e06b5325478ba26cc5, 189 complete records, 0 bytes of a line still written
[2026-11-16T07:51:21Z] run 1793263627 2026-10-29T08:47:07Z, off-calendar, second 31627 of the day: 9 records; terminal complete; set rewardbook-streams-1793263627: 86 files, 890975956 bytes, slots 1793187000 to 1793262600; deferred in verify: AssertionError: VERIFY FAIL: ["every asset uploaded, its bytes and digest the set's", "every download the set's bytes and SHA-256", 'no asset missing', 'release published on the tag']; missing ['1793145600-1793187000.0.stream.jsonl.gz', '1793145600-1793187900.0.stream.jsonl.gz', '1793145600-1793188800.0.stream.jsonl.gz', '1793145600-1793189700.0.stream.jsonl.gz', '1793145600-1793190600.0.stream.js
[2026-11-16T07:51:21Z] run 1793286490 2026-10-29T15:08:10Z, off-calendar, second 54490 of the day: 6 records; terminal complete; set rewardbook-streams-1793286490: 25 files, 311356103 bytes, slots 1793263500 to 1793285100
[2026-11-16T07:51:21Z] run 1793306720 2026-10-29T20:45:20Z, off-calendar, second 74720 of the day: 6 records; terminal complete; set rewardbook-streams-1793306720: 22 files, 214907420 bytes, slots 1793286000 to 1793304900
[2026-11-16T07:51:21Z] run 1793321975 2026-10-30T00:59:35Z, off-calendar, second 3575 of the day: 6 records; terminal complete; set rewardbook-streams-1793321975: 17 files, 170618975 bytes, slots 1793305800 to 1793320200
[2026-11-16T07:51:21Z] run 1793323820 2026-10-30T01:30:20Z, calendar: 6 records; terminal complete; set rewardbook-streams-1793323820: 2 files, 21768368 bytes, slots 1793321100 to 1793322000
[2026-11-16T07:51:21Z] run 1793357934 2026-10-30T10:58:54Z, off-calendar, second 39534 of the day: 7 records; terminal complete; set rewardbook-streams-1793357934: 38 files, 396718353 bytes, slots 1793322900 to 1793356200
[2026-11-16T07:51:21Z] run 1793410220 2026-10-31T01:30:20Z, calendar: 6 records; terminal complete; set rewardbook-streams-1793410220: 58 files, 630678090 bytes, slots 1793357100 to 1793408400
[2026-11-16T07:51:21Z] run 1793496620 2026-11-01T01:30:20Z, calendar: 6 records; terminal complete; set rewardbook-streams-1793496620: 96 files, 728577330 bytes, slots 1793409300 to 1793494800
[2026-11-16T07:51:21Z] run 1793583020 2026-11-02T01:30:20Z, calendar: 6 records; terminal complete; set rewardbook-streams-1793583020: 96 files, 880493103 bytes, slots 1793495700 to 1793581200
[2026-11-16T07:51:21Z] run 1793669420 2026-11-03T01:30:20Z, calendar: 6 records; terminal complete; set rewardbook-streams-1793669420: 96 files, 964839522 bytes, slots 1793582100 to 1793667600
[2026-11-16T07:51:21Z] run 1793755820 2026-11-04T01:30:20Z, calendar: 6 records; terminal complete; set rewardbook-streams-1793755820: 96 files, 700449067 bytes, slots 1793668500 to 1793754000
[2026-11-16T07:51:21Z] run 1793775818 2026-11-04T07:03:38Z, off-calendar, second 25418 of the day: 6 records; terminal complete; set rewardbook-streams-1793775818: 23 files, 154883747 bytes, slots 1793754900 to 1793774700
[2026-11-16T07:51:21Z] run 1793842220 2026-11-05T01:30:20Z, calendar: 6 records; terminal complete; set rewardbook-streams-1793842220: 73 files, 604227513 bytes, slots 1793775600 to 1793840400
[2026-11-16T07:51:21Z] run 1793862240 2026-11-05T07:04:00Z, off-calendar, second 25440 of the day: 6 records; terminal complete; set rewardbook-streams-1793862240: 23 files, 307460576 bytes, slots 1793841300 to 1793861100
[2026-11-16T07:51:21Z] run 1793928620 2026-11-06T01:30:20Z, calendar: 9 records; terminal complete; set rewardbook-streams-1793928620: 73 files, 959342877 bytes, slots 1793862000 to 1793926800; deferred in verify: AssertionError: VERIFY FAIL: ["every download the set's bytes and SHA-256"]; missing []; beyond []
[2026-11-16T07:51:21Z] run 1793991789 2026-11-06T19:03:09Z, off-calendar, second 68589 of the day: 6 records; terminal complete; set rewardbook-streams-1793991789: 71 files, 1086535575 bytes, slots 1793927700 to 1793990700
[2026-11-16T07:51:21Z] run 1794015020 2026-11-07T01:30:20Z, calendar: 6 records; terminal complete; set rewardbook-streams-1794015020: 25 files, 416674608 bytes, slots 1793991600 to 1794013200
[2026-11-16T07:51:21Z] run 1794101420 2026-11-08T01:30:20Z, calendar: 6 records; terminal complete; set rewardbook-streams-1794101420: 96 files, 1639742990 bytes, slots 1794014100 to 1794099600
[2026-11-16T07:51:21Z] run 1794187820 2026-11-09T01:30:20Z, calendar: 6 records; terminal complete; set rewardbook-streams-1794187820: 96 files, 1776573596 bytes, slots 1794100500 to 1794186000
[2026-11-16T07:51:21Z] run 1794274220 2026-11-10T01:30:20Z, calendar: 6 records; terminal complete; set rewardbook-streams-1794274220: 96 files, 1251430567 bytes, slots 1794186900 to 1794272400
[2026-11-16T07:51:21Z] run 1794360620 2026-11-11T01:30:20Z, calendar: 6 records; terminal complete; set rewardbook-streams-1794360620: 96 files, 1385120758 bytes, slots 1794273300 to 1794358800
[2026-11-16T07:51:21Z] run 1794447020 2026-11-12T01:30:20Z, calendar: 6 records; terminal complete; set rewardbook-streams-1794447020: 96 files, 1504752064 bytes, slots 1794359700 to 1794445200
[2026-11-16T07:51:21Z] run 1794522601 2026-11-12T22:30:01Z, off-calendar, second 81001 of the day: 6 records; terminal complete; set rewardbook-streams-1794522601: 84 files, 1290341538 bytes, slots 1794446100 to 1794520800
[2026-11-16T07:51:21Z] run 1794533420 2026-11-13T01:30:20Z, calendar: 6 records; terminal complete; set rewardbook-streams-1794533420: 12 files, 150295740 bytes, slots 1794521700 to 1794531600
[2026-11-16T07:51:21Z] run 1794619820 2026-11-14T01:30:20Z, calendar: 6 records; terminal complete; set rewardbook-streams-1794619820: 80 files, 1229012293 bytes, slots 1794532500 to 1794603600
[2026-11-16T07:51:21Z] run 1794638496 2026-11-14T06:41:36Z, off-calendar, second 24096 of the day: 7 records; terminal complete; set rewardbook-streams-1794638496: 20 files, 281359405 bytes, slots 1794620700 to 1794636900
[2026-11-16T07:51:21Z] run 1794706220 2026-11-15T01:30:20Z, calendar: 6 records; terminal complete; set rewardbook-streams-1794706220: 75 files, 895420557 bytes, slots 1794637800 to 1794704400
[2026-11-16T07:51:21Z] run 1794745827 2026-11-15T12:30:27Z, off-calendar, second 45027 of the day: 7 records; terminal complete; set rewardbook-streams-1794745827: 44 files, 462130216 bytes, slots 1794705300 to 1794744000
[2026-11-16T07:51:21Z] run 1794786586 2026-11-15T23:49:46Z, off-calendar, second 85786 of the day: 6 records; terminal complete; set rewardbook-streams-1794786586: 46 files, 473624826 bytes, slots 1794744900 to 1794785400
[2026-11-16T07:51:21Z] run 1794792620 2026-11-16T01:30:20Z, calendar: 6 records; terminal complete; set rewardbook-streams-1794792620: 6 files, 68188364 bytes, slots 1794786300 to 1794790800
[2026-11-16T07:51:21Z] the archive's assets: 1767 files of 1765 slots, to slot 1794790800; at or after 1794182400: 659 slots, to 1794790800
[2026-11-16T07:51:21Z] complete runs' sets 30; their tags not on origin []; halted False; runs without a terminal record []
[2026-11-16T07:51:21Z] the rehearsal's four assets are in set rewardbook-streams-1793263627, bytes and SHA-256 equal
```

**Runs off the calendar since TZ-44's read**, set beside §0.3's reads of systemd:

- `1794638496`, 06:41:36 UTC on 2026-11-14. The package manager's run of 06:11:34 to 06:11:52 UTC that day (libc6) restarted the recorder, the reward book and the advisor at 06:11:41 to 06:11:44 UTC. This is their `ActiveEnterTimestamp`, and their `NRestarts` read `0`.
- `1794745827`, 12:30:27 UTC on 2026-11-15, 1,800 s after `crypto-deploy.service` reloaded systemd at 12:00:26 UTC.
- `1794786586`, 23:49:46 UTC on 2026-11-15, 1,800 s after its eleven reloads at 23:19:41 to 23:19:45 UTC. The pair book's archive ran off its calendar at 12:10:27 and 23:29:46 UTC the same day, 600 s after each burst, and restarted the pair book at 12:30:15 and 23:34:47 UTC.

Every run is complete, and its tag is on `origin`.

### 2.9 The host, at §0.3 and §3.14 (`logs/03-host-gate.log`, `logs/96-host-gate-again.log`)

| read | §0.3, 07:49:10 UTC | §3.14, 10:23:57 UTC |
|---|---|---|
| boots | one, `48a803f0…`, up since 2026-08-02 07:24:32 | the same |
| `MemAvailable` (meminfo) | `292332 kB` | `215220 kB` |
| memory gate read | `494649344` at 07:49:29 | `458924032` at 10:24:18 |
| `/dev/vda2` avail | `9777135616` | `9206390784` |
| `telemetry-watch.service` | `disabled` (1), `inactive` (3) | `disabled` (1), `inactive` (3) |
| advisor `commit.txt` | `4e6db2d16dda3da14957120d636f537dfc0bcc87` | the same |
| `/root/tz44-work` | absent (exit 1) | absent (exit 1) |
| code trees | the six present | the six present |
| forensic store | 2,532 files | 2,532 files |
| worktrees | `/root/btc-5m-twap` and `/root/btc-recorder-svc` | the same, with `/root/tz45-work/wt` |
| `du -sb /var/lib/btc-rewardbook` | `644259524` | `786228486` |
| `du -sb /var/lib/btc-pairbook` | `616099052` | `912787175` |
| `du -sb /var/lib/btc-rewardbook-archive` | `5593470` | `5593470` |
| `du -sb /root/btc-forensics` | `583581855` | `583581855` |
| `du -sb /root/.claude-8j` | `24704103` | `24704103` |
| journal | 2.9G | 2.9G |

**Every tree of the disk by `du -xsb`**, at §0.3 then §3.14:

| tree | §0.3 | §3.14 |
|---|---|---|
| `/usr` | 4,547,965,470 | 4,547,965,470 |
| `/var/log` | 3,895,083,270 | 3,896,669,048 |
| `/root` | 3,454,766,985 | 3,581,224,277 |
| `/var/lib` | 3,389,427,923 | 3,830,459,943 |
| `/home` | 264,747,867 | 264,747,867 |
| `/var/cache` | 159,152,487 | 159,152,487 |
| `/srv` | 50,729,004 | 50,848,062 |
| `/tmp` | 5,199,970 | 5,199,703 |
| `/opt` | 1,968 | 1,968 |

**The sixteen largest of `/var/lib` and `/root`**, at §0.3: `/var/lib/btc-recorder` 1,628,979,449; `/root/PROJECT_GAMING_PS5` 671,284,684; `/var/lib/btc-rewardbook` 644,214,075; `/var/lib/btc-pairbook` 616,099,052; `/root/btc-forensics` 583,581,855; `/root/tz01-env` 517,113,206; `/root/crypto-auto` 392,741,782; `/root/btc-5m-twap` 336,316,170; `/var/lib/apt` 216,446,304; `/root/my_real_estate_bot` 194,157,457; `/var/lib/cryptorun` 54,435,435; `/var/lib/containerd` 53,018,674; `/var/lib/cryptopaper` 49,249,909; `/var/lib/btc-chainbook` 43,108,667; `/root/seahome_webapp.git` 42,137,787; `/var/lib/dpkg` 30,903,680. At §3.14 `/root/tz45-work` stood among them at 125,680,659.

**The timers**, at both reads: the reward book archive's next run 2026-11-17 01:30:20 UTC, last 2026-11-16 01:30:20. The pair book archive's next 2026-11-17 03:00:20, last 2026-11-16 03:00:20. `apt-daily-upgrade.timer` last fired 2026-11-16 06:07:18 UTC, with its next run 2026-11-17 06:28:33. `apt-daily.timer` fired at 09:32:40 UTC during the run; the package history records no upgrade after 2026-11-14 06:11:52.

**systemd's reload records since 2026-11-12, and its records of these units**, were the same at both reads. They end at 03:15:41 UTC on 2026-11-16, the pair book archive's calendar run, which restarted the pair book to pid `1871674`, `NRestarts` `5`. **No reload, start, stop or restart was recorded between 07:49 and 10:24 UTC.** The package history's last entries are on 2026-11-11 (perl, apache2-utils, python3-pyasn1), 2026-11-12 (linux 6.8.0-149) and 2026-11-14 06:11:34 to 06:11:52 UTC (libc6 2.39-0ubuntu8.12, apache2-utils).

### 2.10 The eighteen slots without a stream, 2026-11-13 21:15 UTC to 2026-11-14 01:30 UTC

The rest of this section is what this run read; it does not establish the cause.

- **The slot records.** Of 2026-11-13, 11 slots fail, 21:15 to 23:45 UTC. `fetch` printed the first three, 21:15, 21:30 and 21:45, as `stream: not opened`; §0.0's read printed the first, 21:15, as `no whole stream`. **The first failing slot is 21:15 UTC**, as the archive's asset names showed the Architect; the 23:15 UTC that an earlier session named is not what this read finds. 2026-11-14 was not a candidate, so its seven slots were not read.
- **The reward book's journal** from 20:45 UTC on 2026-11-13 to 02:15 UTC on 2026-11-14 reads `-- No entries --` at both host gates. The unit's output goes to `/var/lib/btc-rewardbook/service.log`, which this TZ does not open. Its process was the same, `3137952`, `NRestarts` `1`, at the archive's start records of 01:30:20 UTC on both 2026-11-13 and 2026-11-14 (`logs/40-archive.log`).
- **The archive's ledger records the disk at that night's end.** Its calendar run of 2026-11-14 took 80 stream files, slots `1794532500` to `1794603600` (01:15 to 21:00 UTC on 2026-11-13), and recorded `free_before` **`6,874,419,200`** bytes before its removal at 01:36:02 UTC and `free_after` `8,103,866,368`. The first is below the reward book's `STREAM_FLOOR`, `7,300,000,000`, below which no stream opens for a slot (TZ-33 §1; map §2.6). Its `complete` record reads `store_stream_bytes` `0`. The calendar run of 2026-11-13 had recorded `free_bytes` `8,866,500,608` at 01:32:52 UTC that day.
- **These facts are consistent with the disk floor having stopped the streams, and they do not prove it.** Each slot record's own `off_reason` would name it. Those records are members of `rewardbook-inputs-1794528000.tar` in this Release, and this TZ's instrument prints no field of them.
- **What took the room** cannot be named from two `du` reads of today. §2.9 gives every tree and the largest by name.

### 2.11 The four units, at §3.3 and §3.13 (`logs/30-still.log`, `logs/95-still.log`; memory at §3.14 from `logs/98-closing.log`)

| unit | MainPID | NRestarts | ActiveState | MemoryCurrent §3.3 | §3.13 | §3.14 | MemoryPeak |
|---|---|---|---|---|---|---|---|
| `btc-recorder.service` | `1555954` | `0` | active | 11,673,600 | 26,787,840 | 52,465,664 | 390,193,152 |
| `btc-pairbook.service` | `1871674` | `5` | active | 3,219,456 | 10,792,960 | 7,475,200 | 56,143,872 |
| `btc-rewardbook.service` | `1556307` | `0` | active | 14,073,856 | 22,851,584 | 13,185,024 | 45,936,640 |
| `adv3-bot.service` | `1555970` | `0` | active | 7,233,536 | 5,550,080 | 5,619,712 | 48,467,968 |

The MainPID, NRestarts and ActiveState columns are the same at all three reads. Both archives' services were `inactive` and their timers `active` / `waiting` at §3.3, at §3.13 and at §3.14. `I still` at §3.13: `the reward book archive's runs with records since the first read: []`, `G-STILL PASS: unchanged since 2026-11-16T07:50:52Z`.

### 2.12 The read ledger (`read-ledger.jsonl`, 9 lines)

```
{"at": "2026-11-16T07:51:29Z", "at_ns": 1794815489065443263, "file_sha256": "4720e78573e54b1325dd24af7c30e0de59bfb4c1879d309a23fa6bab6b32d2d4", "head": "01756f665893096ab38ae10dfbe58f074f8fb648", "mode": "rehearse"}
{"at": "2026-11-16T07:52:01Z", "at_ns": 1794815521518538495, "file_sha256": "4720e78573e54b1325dd24af7c30e0de59bfb4c1879d309a23fa6bab6b32d2d4", "head": "01756f665893096ab38ae10dfbe58f074f8fb648", "mode": "fetch"}
{"at": "2026-11-16T07:52:27Z", "at_ns": 1794815547767744038, "file_sha256": "4720e78573e54b1325dd24af7c30e0de59bfb4c1879d309a23fa6bab6b32d2d4", "head": "01756f665893096ab38ae10dfbe58f074f8fb648", "mode": "replay"}
{"at": "2026-11-16T08:35:18Z", "at_ns": 1794818118853752443, "file_sha256": "4720e78573e54b1325dd24af7c30e0de59bfb4c1879d309a23fa6bab6b32d2d4", "head": "01756f665893096ab38ae10dfbe58f074f8fb648", "mode": "replay"}
{"at": "2026-11-16T08:35:24Z", "at_ns": 1794818124130204908, "file_sha256": "4720e78573e54b1325dd24af7c30e0de59bfb4c1879d309a23fa6bab6b32d2d4", "head": "01756f665893096ab38ae10dfbe58f074f8fb648", "mode": "rescore"}
{"at": "2026-11-16T08:36:38Z", "at_ns": 1794818198046308028, "file_sha256": "4720e78573e54b1325dd24af7c30e0de59bfb4c1879d309a23fa6bab6b32d2d4", "head": "01756f665893096ab38ae10dfbe58f074f8fb648", "mode": "score"}
{"at": "2026-11-16T08:36:45Z", "at_ns": 1794818205396295287, "file_sha256": "4720e78573e54b1325dd24af7c30e0de59bfb4c1879d309a23fa6bab6b32d2d4", "head": "01756f665893096ab38ae10dfbe58f074f8fb648", "mode": "score"}
{"at": "2026-11-16T08:36:51Z", "at_ns": 1794818211509589861, "file_sha256": "4720e78573e54b1325dd24af7c30e0de59bfb4c1879d309a23fa6bab6b32d2d4", "head": "01756f665893096ab38ae10dfbe58f074f8fb648", "mode": "pack"}
{"at": "2026-11-16T08:37:10Z", "at_ns": 1794818230838655077, "file_sha256": "4720e78573e54b1325dd24af7c30e0de59bfb4c1879d309a23fa6bab6b32d2d4", "head": "01756f665893096ab38ae10dfbe58f074f8fb648", "mode": "pack"}
```

### 2.13 Every free-space and `MemAvailable` read, with its instant and bound

The bounds are a memory floor of `172,658,448` at every mode and a free-space floor of `7,500,000,000` at every mode (`floor_check`). At the host gates the bounds are `172,658,448` and `8,350,000,000` at §0.3, and the reads are recorded with no bound at §3.14.

| instant (UTC) | read by | `MemAvailable` | free bytes |
|---|---|---|---|
| 07:48:38 | §0.0's read, the session's run | — | 9,778,073,600 |
| 07:48:49 | §0.0's read, `logs/00-ready.log` | — | 9,777,897,472 |
| 07:49:10 / 07:49:29 | §0.3 | 494,649,344 | 9,777,135,616 |
| 07:51:29 | `rehearse` | 222,765,056 | 9,759,412,224 |
| 07:52:01 | `fetch` | 216,186,880 | 9,758,478,336 |
| 07:52:27 | `replay` | 232,222,720 | 9,730,289,664 |
| 08:35:18 | `replay`, again | 203,485,184 | 9,611,173,888 |
| 08:35:24 | `rescore` | 188,846,080 | 9,611,046,912 |
| 08:36:38 | `score` | 285,118,464 | 9,610,264,576 |
| 08:36:45 | `score`, again | 261,500,928 | 9,610,027,008 |
| 08:36:51 | `pack` | 260,747,264 | 9,610,387,456 |
| 08:37:10 | `pack`, again | 273,567,744 | 9,531,191,296 |
| 10:20:43 | `upload` | 254,685,184 | 9,210,212,352 |
| 10:21:51 | `verify` | 199,684,096 | 9,208,877,056 |
| 10:23:57 / 10:24:18 | §3.14 | 458,924,032 | 9,206,390,784 |
| 10:24 | §3.14's closing `df` | — | 9,205,227,520 |

Every memory read passed at its first read. None fell below its floor. `selftest`'s three floor lines at 07:50:45 UTC are its own synthetic checks of the floor (`172658447`, `7499999999`) and not reads of the host.

### 2.14 Every mode's printed peak, against §0.4's `86,329,224`

| mode | log | peak bytes |
|---|---|---|
| `fingerprint` (staged) | `02-fingerprint.log` | 47,476,736 |
| `number` (staged) | `05-number.log` | 47,083,520 |
| `number` (staged, §3.1) | `10-number.log` | 47,345,664 |
| `fingerprint` | `12-fingerprint.log` | 47,218,688 |
| `selftest` | `20-selftest.log` | 47,824,896 |
| `still` | `30-still.log` | 47,349,760 |
| `scratch` | `31-scratch.log` | 47,353,856 |
| `reclaim` (scratch) | `32-reclaim-scratch.log` | 47,357,952 |
| `archive` | `40-archive.log` | 47,562,752 |
| `rehearse` | `50-rehearse.log` | 62,910,464 |
| `fetch` | `60-fetch.log` | **75,780,096** |
| `replay` | `70-replay.log` | 64,401,408 |
| `replay`, again | `71-replay-again.log` | 46,960,640 |
| `rescore` | `75-rescore.log` | 63,975,424 |
| `score` | `80-score.log` | 53,071,872 |
| `score`, again | `81-score-again.log` | 53,207,040 |
| `pack` | `82-pack.log` | 47,828,992 |
| `pack`, again | `83-pack-again.log` | 47,828,992 |
| `upload` | `85-upload.log` | 47,976,448 |
| `verify` | `88-verify.log` | 48,087,040 |
| `still` | `95-still.log` | 47,349,760 |
| `archive`, again | `97-archive-again.log` | 47,169,536 |

Every peak is under the modelled host peak of `86,329,224`. **`fetch`'s `75,780,096` is above the Architect's bound of `72,000,000`** on any mode's peak, set from his runs over six candidates (§0.4). It is recorded here, gates nothing, and is named in §6.

### 2.15 Every file the run wrote, by SHA-256 (outside the branch worktree, at §3.14)

```
8486a5888ff2cbb23446c633e7991e5895accb8576cc13a8f37fff70cbe01aa7      415576  days/1794182400.json
071bb0609497f08d85da6712446dc60b17796d909d3a6f30ec6a22d53cce20f8      118051  days/1794182400.slots.txt
fd162966f292d9d8c958c99c696bc2ecd20cfa12e87114b88ee61bd7255a9fe3      417507  days/1794268800.json
876bf5a6d8c9a0f5f8db04f7a89cdbaafe7a8d6e2aac7f61a2c8d406fba9b58e      118803  days/1794268800.slots.txt
900307a8e41ca4579491482654cf1d3bc756268a166f5641455cb26e6b90c673      414400  days/1794355200.json
981c985e5f4208eee0ddb10f4b5d3cb1eff5e1daa7a52a36bfcd19733e5924a2      107907  days/1794355200.slots.txt
9ce2ca6d1e356196f18db4090bc7091323f63cb66fc1ca768ae8c3d8c4be162f      406921  days/1794441600.json
a3351cecbb54249db9e42b4de635afccaf70c78ffff4090b42a1cbfbb60ed801      118366  days/1794441600.slots.txt
6dfb638cd08f7c338347d620ed3ed9e9e0aebcf200fab34bb6aeb0a6b7050084      407006  days/1794528000.json
74d6c047066307175769f4c5cac13fdcd0aaeba7d5d28f80acaeeb779688cdaa      106663  days/1794528000.slots.txt
6d6b0bd4e2dd39b936787c41b1dfd56e1e225dadebb25c79937e7771308090e5       55682  fetch/1794182400.json
bafbfb4a04b2a83d110a75fc03d311bfb53802667d7ec0938c295cb4656ccaa1     5771356  fetch/1794182400.polls.jsonl
3c90f5a48be59c5d1ef4822adee950eac4c14f0b9572142c495b3d6af9b4be15       55693  fetch/1794268800.json
3a48a45a0ed5d93e6cbda1c16de951ddfa56a1b45112b4087f8c83d7051bbba1     5743103  fetch/1794268800.polls.jsonl
065f89f2e2cc1214ec1ee634a3e1d4dc21f9ce0ff102d0ae94645b0b067b0c73       53508  fetch/1794355200.json
63d997837a0146a08ffb13324b5fac96fb494191da197df91c68a457650d493d     5193469  fetch/1794355200.polls.jsonl
0ae5be7dc825fcb75068f52302be92d6fa4da2ced9a9895e96d8b8a5947b7a48       55683  fetch/1794441600.json
d35cd64290914e370d59252760504435a6a503a636e5410972d552af223f4481     5600221  fetch/1794441600.polls.jsonl
1a6c2d17a63bf78e718477ad0af8a547d3a088240d0bc9e8754c78f675e800d8       53341  fetch/1794528000.json
8b9ed8b9936807ece05718c96558aa9896cd92502a1f7f983ecc9923e67e56f0     5099550  fetch/1794528000.polls.jsonl
3f1cefb098f538dde99dadc13aba9a6c0be2e44bcc761ccfa6516350e8d0d9db    16353280  out/rewardbook-inputs-1794182400.tar
35a219bcd999c17bba8b8b8f664fd3d3107c4367e1f573dfe38ba2509ea34f8c    16148480  out/rewardbook-inputs-1794268800.tar
fd5df7d694a8d25d246c3189bdf8a9a64597a8d040ad2585d46852f5ce7fc2c6    15861760  out/rewardbook-inputs-1794355200.tar
840a13670100aee0cc584b06b1b4cc85cbfc0161ef0a183603d9056fa7024dfb    14714880  out/rewardbook-inputs-1794441600.tar
ed98acd9ccd70d492dd0fdba4f4e4a465531f92a557b165ea2046c5aee826f48    15575040  out/rewardbook-inputs-1794528000.tar
23843e59372a48409a287f91f8a14d243d7b0bb29228748f1d6b2b8572f806b3      171407  out/tz45-manifest.json
4eb9555208ecfecb19273bf1c6b8694009ddd6f0e335d7ff73dae82a604cb0cc        1922  read-ledger.jsonl
874f576a9c082c32674d63b3134a9325d7add2935712f2118f994406cb2c1e08       23431  reading.json
1ab40f4b2a9b4f263e92959dc78a67dc9583731889cce70b22edad59091944cd      103261  rehearsal-base.txt
9c8c1a343a5a95be0ade7c4a017ff51707fac11bb55d8d8904b1e20024f85bf6      330249  rehearsal-w.txt
442055028a700f7b4694a70b44267d41fa7fdec3e0a178057ec23ba88273057f        6082  release-set.json
f8e6d6c5c5e8b2440865c21875017b472f390903aeac22114c9c28319345a4da       28476  rescore.txt
25eb1cba98ccd6d68fac5ad8c86da06677fd400483e8f27761ec21a23cffd462        4432  set.json
2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673      106284  stage/research/tz27-pairbook-archive.py
4720e78573e54b1325dd24af7c30e0de59bfb4c1879d309a23fa6bab6b32d2d4      233655  stage/research/tz45-l0-rule-w.py
77cc1f28043c79486a829bd8c22bcde458859c362b4c96c25136c11f967c192c        1072  state.json
3d68f3f01085343905629a03d2ed92313eadfa97a7e15ac44ee394b350b296f8      103553  timing-replay.jsonl
9322e2519ce255872d716783f732a3d9e56986e0b7971e2ce9871ca9a65cb07a        5418  timing-rescore.jsonl
8ed46c1ea5af3dfad5300bb21cfef523ac7f5d65662835cd41bee975c9560a6a       11443  transfers.jsonl
94dd43a742d96c94f1e1b9b662b67e8da91f6f2e840923fcf62fd16a9d0f8faf        9260  upload.jsonl
58cbf30b30b4f5e182c6d8aeafff9765ce845442b3b53dd43a448839ac35b7b5       13996  verify.json
```

The logs, 34 files, are under `logs/`: `00-instant.log` to `99-selfcheck.log`, as §3's table names them. §9 kept each by name. At §3.14 `du -sb /root/tz45-work` read `125,790,880` bytes, the worktree included.

---

## 3. Publication

| item | value |
|---|---|
| branch | `tz-45-l0-rule-w`, on `origin` at `01756f665893096ab38ae10dfbe58f074f8fb648` |
| commit | `01756f665893096ab38ae10dfbe58f074f8fb648` — `research/tz45-l0-rule-w.py`, 4,299 lines added, nothing else |
| on `origin` at | `2026-11-16T07:50:28.452174496Z`, pushed through the URL's own credential, `gh`'s route not needed |
| pull request | #45, `https://github.com/seahomebatumi-ai/btc-5m-twap/pull/45`, against `main`; not merged |
| Release | id `446880816`, published, not the latest |
| tag | `tz-45-l0-rule-w-inputs`, lightweight, at `01756f665893096ab38ae10dfbe58f074f8fb648`; `ls-remote` prints no peeled line |
| assets | 28, `109,165,516` bytes — §2.6, each by name, bytes and SHA-256 |
| local hash = downloaded hash | 28 of 28: `pack`'s SHA-256 of each file, and `verify`'s SHA-256 of each full anonymous download, equal (`G-DOWNLOAD PASS`) |

**`logs/13-push.log`, the commit's arrival:**

```
01756f665893096ab38ae10dfbe58f074f8fb648 TZ-45: L0's second rule, rule W - the instrument
2026-11-16T07:50:28.452174496Z
01756f665893096ab38ae10dfbe58f074f8fb648	refs/heads/tz-45-l0-rule-w
01756f665893096ab38ae10dfbe58f074f8fb648
```

**Contract §4.2's self-check and its two lines more** (`logs/99-selfcheck.log`, `C` = `01756f665893096ab38ae10dfbe58f074f8fb648`):

```
Mon Nov 16 10:24:58 AM UTC 2026
From https://github.com/seahomebatumi-ai/btc-5m-twap
 * [new tag]         tz-45-l0-rule-w-inputs -> tz-45-l0-rule-w-inputs
0
research/tz45-l0-rule-w.py
4299	0	research/tz45-l0-rule-w.py
0
```

The first count is `0`, so `main` does not carry the implementation commit. The diff names `research/tz45-l0-rule-w.py` alone, `4299` added and `0` removed. The `.parquet` / `.zip` grep printed nothing. The last count is `0`: no `.tar` or manifest is in either tree. **The report is the one path this TZ pushes to `main`.**

---

## 4. Gate

> | condition, on each day's least and most over the set's 5 days (§1) | reading |
> |---|---|
> | every day's least at or above `θ = 10` USDC, and some day's most at or above it | **EARN** |
> | every day's most below `θ`, and some day's least below it | **NO EARN** |
> | otherwise | **UNDECIDABLE** |

**The deciding numbers:**

- The smallest of the five days' least is **`28.680`** USDC, at or above `10`. Every day's least is at or above `θ`: 5 of 5.
- The largest of the five days' most is **`227.562`**, at or above `10`. No day's most is below `θ`: 0 of 5.

**L0-W: EARN.** Nothing was tuned and no gate was reinterpreted.

**What it establishes and what it does not** (TZ §1). EARN says that on five days no one had read, each over a block of twenty hours or more, rule W's quotes kept at least `10` USDC a day under every assumption held against them: every corner of the queue place and the crossing orders, the competitors at the most the book or the venue allows, the reward unpaid on any member-day under `1` and credited only through the last confirming poll, no rebate, and one adverse fill charged in every market quoted. The positions were marked to each market's midpoint at the block's end, a proxy. **It proves no income.** The false reading is `2⁻⁵ = 0.03125` under independent days, which is named and not measured. The days share markets. EARN opens L1, a live step of a fixed loss limit in a TZ of its own (CANON PART II), and nothing more.

**Barred and printed** (TZ §7): `central` read `572.777` over the 5 days, `114.555` a day. Each variant's total and mean day are in §2.4.

---

## 5. Validation — in TZ-45 §7's numbering

| # | expected | read | asserted |
|---|---|---|---|
| **V1** | `FINGERPRINT PASS: revision 2026-11-13-a; anchors 6 of 6, 4 re-derived; rows 63: frozen 60 of 60 equal, tracked 2, reported 1`, twice | that line, at §0.2 and at §3.1 — §0 | yes, `fingerprint` |
| **V2** | at §0.3 11 checks, at §3.14 9 | §0.3: 11 of 11. §3.14: H1 one path; H2 `/dev/vda2` `31612203008` and `grep -c` `4`; H3 `3.12.3`; H4 the three files; H5 the four units `active` / `enabled` — 9 of 9. The two reads recorded, `458924032` at 10:24:18 and `9206390784` — §0, §2.9 | checked by the Executor against the log; not asserted by a script |
| **V3** | `NUMBER PASS - 2 of 2`, twice | at §0.5 and at §3.1 — §0 | yes, `number` |
| **V4** | two lines a run: 4,299 / 233,655 / `4720e785…`; 2,078 / 106,284 / `2cba96bc…` | both runs — §0 | yes, the script's asserts |
| **V5** | `SELFTEST PASS: 73 checks` | `[2026-11-16T07:50:45Z] SELFTEST PASS: 73 checks` — 73 `ok` lines | yes |
| **V6** | the archive's record at §3.4 and §3.14 | both reads — §2.8. The ledger was `71648` bytes, `30c915ea…`, 189 complete records, at both. There were 30 complete runs, every one's tag on `origin`, and the archive was not halted. Its assets reach slot `1794790800`, 659 slots at or after `1794182400`. The rehearsal's four assets were in `rewardbook-streams-1793263627`, their bytes and SHA-256 equal | yes, `archive` |
| **V7** | `451` / `1ab40f4b…`; `1351` / `9c8c1a34…`; `G-REHEARSAL PASS: 2 of 2` | see below | yes |
| **V8** | 5 members; every candidate with its verdict; each member's markets, slots, files, bytes and polls; the document requests | §2.1 | yes, `fetch` |
| **V9** | every unit inside the idle stretch or listed; the projection after 24 units against `3,000`; every day's two files; G-BOOK; no day replayed at the second run | 460 of 460 inside the stretch, 0 after second 590. Projected `782` s after 24 units. 10 day files. G-BOOK `70125` of `70144`. `days to replay 0 of 5` — §2.2 | yes, `replay` |
| **V10** | `24 of 24` | `DETERMINISM PASS: 24 of 24 slot lines of day 1794182400 equal to the replay's` | yes, `rescore` |
| **V11** | the power's three lines and the false reading's; nine variants on each of the five days; each day's least and most; the reading; `unchanged`; the read ledger's lines; the commit on `origin` before the first `fetch` line | §2.4, §2.12. The power is `0.590490000000`, `0.773780937500` and `0.950990049900`; the false reading `0.031250000000`. Commit on `origin` 07:50:28.452 UTC, before the read ledger's first line (07:51:29, `rehearse`) and its first `fetch` line (07:52:01) | yes, `score`; the order checked by the Executor |
| **V12** | `G-SOURCE PASS: 22 of 22 equal to this run's own record`, both runs | `G-SOURCE PASS: 22 of 22 equal to this run's own record, 30340669 bytes`, at both | yes, `pack` |
| **V13** | every candidate day with its names, members, bytes, files scanned, withheld, archive and excluded names; `days over their budget 0`; assets `23` and one a candidate day; `G-RESERVE PASS`; `wrote` then `unchanged`, two and one a candidate day; `DETERMINISM PASS` | 5 days. 28 assets — 23 + 5. Days over their budget 0. G-RESERVE PASS, 5 listings. `outputs {'wrote': 7}`, then `{'unchanged': 7}`. `DETERMINISM PASS: 7 of 7 outputs unchanged` — §2.5 | yes, `pack` |
| **V14** | each run's `exit=` and its last lines; `credential:`; `UPLOAD COMPLETE: Release <id> on tz-45-l0-rule-w-inputs`; `upload.jsonl`'s last line `complete`; the transfers' line | one run, `exit=0`. `credential: the primary checkout's remote URL`. `UPLOAD COMPLETE: Release 446880816 on tz-45-l0-rule-w-inputs, 28 assets - 28 sent, 0 already held - 109165516 bytes`. Last line `complete`. `transfers so far 31: 0 started outside the idle stretch, 0 ended after its second 590; 0.0 s held` — §2.7 | yes, `upload` |
| **V15** | `G-UPLOAD PASS: n of n …; G-DOWNLOAD PASS: n of n downloads, <bytes>; G-TAG PASS: …`, `n` the set's assets, the bytes `bytes_total` | `G-UPLOAD PASS: 28 of 28 assets by name, bytes, state and digest; G-DOWNLOAD PASS: 28 of 28 downloads, 109165516 bytes; G-TAG PASS: tz-45-l0-rule-w-inputs at 01756f665893096ab38ae10dfbe58f074f8fb648`. `release-set.json`'s `bytes_total` is `109165516`. `transfers 61, upload's and verify's: 0 started outside the idle stretch, 0 ended after its second 590; 0.0 s held`. One run of `verify` | yes, `verify` |
| **V16** | `G-STILL PASS`, or FAIL with what changed | `G-STILL PASS: unchanged since 2026-11-16T07:50:52Z` — §2.11 | yes, `still` |
| **V17** | first count `0`; the diff naming `research/tz45-l0-rule-w.py` alone, `4299` / `0`; nothing `.parquet` or `.zip`; the last count `0` | as required — §3 | printed and checked by the Executor |
| **V18** | `opens refused: 0, by TZ-27's hook: 0` at every mode; `reward book opens` above `0` at `fetch` and `pack` alone | every mode's closing line reads `opens refused: 0, by TZ-27's hook: 0`. `reward book opens: 950, listings: 5` at `fetch`, `1455, listings: 5` at both `pack` runs, and `0, listings: 0` at every other mode | yes, the hook counts |
| **V19** | every mode's peak against `86,329,224`; no read below `172,658,448` or `7,500,000,000`; `malloc tuned: True` at every mode | §2.13 and §2.14. Every peak is under `86,329,224`, every read above its floor, and `malloc tuned: True` at all 22 runs | yes, `floor_check` and `memory_gate`; the peaks are printed |
| **V20** | §9's `reclaim` runs | B-RECLAIM-SCRATCH's below. B-RECLAIM-OWN's is §9, below | yes, `reclaim` |
| **V21** | `git worktree remove` without `--force` exit `0`; `test -e` exit `1` for `/root/tz45-work` and each directory removed; `git worktree list` naming the two | §3.3's five: each `exit=0`, then `exit=1`. §9's are below | printed |
| **V22** | every block the classifier refused | **none.** B-RECLAIM-SCRATCH ran in the session. B-UPLOAD was not tried by the Executor; it is the Boss's by its own text, and he ran it at 10:20:43 UTC — §2.7 | — |

**V7, G-REHEARSAL** (`logs/50-rehearse.log`):

```
[2026-11-16T07:51:30Z] downloaded 1793232000-1793232000.0.stream.jsonl.gz: 11579610 bytes in 1.3 s, sha256 bafa2d5e0ed6293ab1a4a8466431db62100413766eac72c5c6a13d18a591271f, retries 0, held 0 s
[2026-11-16T07:51:31Z] downloaded 1793232000-1793232900.0.stream.jsonl.gz: 10715152 bytes in 1.4 s, sha256 46076896c752257334186cf66c256d6c76685dccd274dbd7f6ab9d1b5917e370, retries 0, held 0 s
[2026-11-16T07:51:32Z] downloaded 1793232000-1793233800.0.stream.jsonl.gz: 11443056 bytes in 0.8 s, sha256 2881148ced021d3c865fdc976183de94869fbe4876f9e70d3b6747394834a4a9, retries 0, held 0 s
[2026-11-16T07:51:33Z] downloaded 1793232000-1793234700.0.stream.jsonl.gz: 13592154 bytes in 0.9 s, sha256 ca030bcb13717dd12c41d485f8abf83c1f8c4ac92fbef2625cbd6a6aecca9496, retries 0, held 0 s
[2026-11-16T07:51:45Z] rehearsal of TZ-43's rule: 150 markets, 387633 lines of stream, 5.7 s of processor, held 0 s; 451 lines sha256 1ab40f4b2a9b4f263e92959dc78a67dc9583731889cce70b22edad59091944cd against 451 lines sha256 1ab40f4b2a9b4f263e92959dc78a67dc9583731889cce70b22edad59091944cd: equal
[2026-11-16T07:51:45Z] rehearsal of rule W: 150 markets, 387633 lines of stream, 5.4 s of processor, held 0 s; 1351 lines sha256 9c8c1a343a5a95be0ade7c4a017ff51707fac11bb55d8d8904b1e20024f85bf6 against 1351 lines sha256 9c8c1a343a5a95be0ade7c4a017ff51707fac11bb55d8d8904b1e20024f85bf6: equal
[2026-11-16T07:51:45Z] G-REHEARSAL PASS: 2 of 2 replays equal - TZ-43's rule to TZ-43's own lines, rule W to the Architect's second implementation
```

### §3.3 — `I still`, `I scratch` and B-RECLAIM-SCRATCH (V20, V21)

```
[2026-11-16T07:50:52Z] running 1738600 started 2026-11-15T10:28:51Z claude
[2026-11-16T07:50:52Z] running 1738611 started 2026-11-15T10:28:53Z claude
[2026-11-16T07:50:52Z] running 1738619 started 2026-11-15T10:28:53Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-16T07:50:52Z] running 1738645 started 2026-11-15T10:28:55Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-16T07:50:52Z] running 1901633 started 2026-11-16T07:46:51Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-16T07:50:52Z] 38f3be57-0238-5ea4-b9d4-f1eebc9ee01c born 2026-11-13T07:32:17Z: earlier
[2026-11-16T07:50:52Z] 4d2d9437-830e-42e6-a940-c4076e8879af born 2026-11-13T07:32:16Z: earlier
[2026-11-16T07:50:52Z] 52c5059d-9f3d-41ee-a5d4-2f0f134c1c02 born 2026-11-15T10:33:00Z: earlier
[2026-11-16T07:50:52Z] 95cf58d2-1ec6-4c73-a622-38d04665f5ae born 2026-11-15T10:28:56Z: live, process [1738600, 1738611, 1738619, 1738645]
[2026-11-16T07:50:52Z] b93843c6-34fe-4b95-8041-0ae0aad4b8ab born 2026-11-16T07:46:52Z: live, process [1901633]
[2026-11-16T07:50:52Z] ba77db14-7684-5807-a005-06722af50f2c born 2026-11-15T10:33:01Z: earlier
[2026-11-16T07:50:52Z] c78295f5-9a1d-4177-ac5a-b93cd56a49da born 2026-11-08T07:15:42Z: earlier
[2026-11-16T07:50:52Z] ccca2df8-e51d-56bc-8205-06299775095a born 2026-11-15T10:28:57Z: live, process [1738600, 1738611, 1738619, 1738645]
[2026-11-16T07:50:52Z] malloc tuned: True
[2026-11-16T07:50:52Z] peak memory of this run: 47353856 bytes
[2026-11-16T07:50:52Z] opens refused: 0, by TZ-27's hook: 0; reward book opens: 0, listings: 0
```

The directories `I scratch` named **earlier** were 38f3be57, 4d2d9437, 52c5059d, ba77db14 and c78295f5. Each was reclaimed and removed. The **live** ones were 95cf58d2, b93843c6 and ccca2df8; they were not touched, and neither was this session's own, `892ec9bf-0691-50df-8231-a07862dcb100`. The block ran in the session, not refused. Its full output (`logs/32-reclaim-scratch.log`):

```
2026-11-16T07:51:06.414255133Z
[2026-11-16T07:51:06Z] reclaim: 3884 report tokens; forensic store holds 2532 files; the Release tz-45-l0-rule-w-inputs proved 0 assets
[2026-11-16T07:51:06Z] RECLAIM PASS: 2 files considered, 0 named by a report, 0 kept by name, 0 copied, 0 already held, 0 left to the Release tz-45-l0-rule-w-inputs that holds them; forensic store 2532 -> 2532 files
[2026-11-16T07:51:06Z] malloc tuned: True
[2026-11-16T07:51:06Z] peak memory of this run: 47357952 bytes
[2026-11-16T07:51:06Z] opens refused: 0, by TZ-27's hook: 0; reward book opens: 0, listings: 0
exit=0
2026-11-16T07:51:15.727591614Z
/tmp/claude-0/-root-btc-5m-twap/38f3be57-0238-5ea4-b9d4-f1eebc9ee01c
exit=0
exit=1
/tmp/claude-0/-root-btc-5m-twap/4d2d9437-830e-42e6-a940-c4076e8879af
exit=0
exit=1
/tmp/claude-0/-root-btc-5m-twap/52c5059d-9f3d-41ee-a5d4-2f0f134c1c02
exit=0
exit=1
/tmp/claude-0/-root-btc-5m-twap/ba77db14-7684-5807-a005-06722af50f2c
exit=0
exit=1
/tmp/claude-0/-root-btc-5m-twap/c78295f5-9a1d-4177-ac5a-b93cd56a49da
exit=0
exit=1
```

### §9 — B-RECLAIM-OWN (V20, V21)

B-RECLAIM-OWN ran last, after §3.14 and with this report drafted in `CryptoReports/`, in the session. The classifier refused nothing. Its output was written to no file, as §9 requires, and is quoted here verbatim from the session, every line of it. `reclaim` ran first and printed `RECLAIM PASS` before the removals:

```
$ cd /root/tz45-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz45-work/wt/research/tz45-l0-rule-w.py reclaim /root/tz45-work
[2026-11-16T10:31:07Z] reclaim: 3955 report tokens; forensic store holds 2532 files; the Release tz-45-l0-rule-w-inputs proved 28 assets
[2026-11-16T10:31:07Z] reclaim: /root/tz45-work/wt skipped: no file but its HEAD's, and HEAD 01756f665893096ab38ae10dfbe58f074f8fb648 is its upstream's
[2026-11-16T10:31:07Z] R copied 4eb9555208ecfecb19273bf1c6b8694009ddd6f0e335d7ff73dae82a604cb0cc /root/btc-forensics/tz45-work--read-ledger.jsonl
[2026-11-16T10:31:07Z] R release 874f576a9c082c32674d63b3134a9325d7add2935712f2118f994406cb2c1e08 /root/tz45-work/reading.json is tz45-reading.json of tz-45-l0-rule-w-inputs
[2026-11-16T10:31:07Z] R copied 1ab40f4b2a9b4f263e92959dc78a67dc9583731889cce70b22edad59091944cd /root/btc-forensics/tz45-work--rehearsal-base.txt
[2026-11-16T10:31:07Z] R copied 9c8c1a343a5a95be0ade7c4a017ff51707fac11bb55d8d8904b1e20024f85bf6 /root/btc-forensics/tz45-work--rehearsal-w.txt
[2026-11-16T10:31:07Z] R copied 442055028a700f7b4694a70b44267d41fa7fdec3e0a178057ec23ba88273057f /root/btc-forensics/tz45-work--release-set.json
[2026-11-16T10:31:07Z] R copied f8e6d6c5c5e8b2440865c21875017b472f390903aeac22114c9c28319345a4da /root/btc-forensics/tz45-work--rescore.txt
[2026-11-16T10:31:07Z] R release 25eb1cba98ccd6d68fac5ad8c86da06677fd400483e8f27761ec21a23cffd462 /root/tz45-work/set.json is tz45-set.json of tz-45-l0-rule-w-inputs
[2026-11-16T10:31:07Z] R copied 77cc1f28043c79486a829bd8c22bcde458859c362b4c96c25136c11f967c192c /root/btc-forensics/tz45-work--state.json
[2026-11-16T10:31:07Z] R copied 3d68f3f01085343905629a03d2ed92313eadfa97a7e15ac44ee394b350b296f8 /root/btc-forensics/tz45-work--timing-replay.jsonl
[2026-11-16T10:31:07Z] R copied 9322e2519ce255872d716783f732a3d9e56986e0b7971e2ce9871ca9a65cb07a /root/btc-forensics/tz45-work--timing-rescore.jsonl
[2026-11-16T10:31:07Z] R copied 8ed46c1ea5af3dfad5300bb21cfef523ac7f5d65662835cd41bee975c9560a6a /root/btc-forensics/tz45-work--transfers.jsonl
[2026-11-16T10:31:07Z] R copied 94dd43a742d96c94f1e1b9b662b67e8da91f6f2e840923fcf62fd16a9d0f8faf /root/btc-forensics/tz45-work--upload.jsonl
[2026-11-16T10:31:07Z] R copied 58cbf30b30b4f5e182c6d8aeafff9765ce845442b3b53dd43a448839ac35b7b5 /root/btc-forensics/tz45-work--verify.json
[2026-11-16T10:31:07Z] R release 8486a5888ff2cbb23446c633e7991e5895accb8576cc13a8f37fff70cbe01aa7 /root/tz45-work/days/1794182400.json is tz45-days-1794182400.json of tz-45-l0-rule-w-inputs
[2026-11-16T10:31:07Z] R release 071bb0609497f08d85da6712446dc60b17796d909d3a6f30ec6a22d53cce20f8 /root/tz45-work/days/1794182400.slots.txt is tz45-days-1794182400.slots.txt of tz-45-l0-rule-w-inputs
[2026-11-16T10:31:07Z] R release fd162966f292d9d8c958c99c696bc2ecd20cfa12e87114b88ee61bd7255a9fe3 /root/tz45-work/days/1794268800.json is tz45-days-1794268800.json of tz-45-l0-rule-w-inputs
[2026-11-16T10:31:07Z] R release 876bf5a6d8c9a0f5f8db04f7a89cdbaafe7a8d6e2aac7f61a2c8d406fba9b58e /root/tz45-work/days/1794268800.slots.txt is tz45-days-1794268800.slots.txt of tz-45-l0-rule-w-inputs
[2026-11-16T10:31:07Z] R release 900307a8e41ca4579491482654cf1d3bc756268a166f5641455cb26e6b90c673 /root/tz45-work/days/1794355200.json is tz45-days-1794355200.json of tz-45-l0-rule-w-inputs
[2026-11-16T10:31:07Z] R release 981c985e5f4208eee0ddb10f4b5d3cb1eff5e1daa7a52a36bfcd19733e5924a2 /root/tz45-work/days/1794355200.slots.txt is tz45-days-1794355200.slots.txt of tz-45-l0-rule-w-inputs
[2026-11-16T10:31:07Z] R release 9ce2ca6d1e356196f18db4090bc7091323f63cb66fc1ca768ae8c3d8c4be162f /root/tz45-work/days/1794441600.json is tz45-days-1794441600.json of tz-45-l0-rule-w-inputs
[2026-11-16T10:31:07Z] R release a3351cecbb54249db9e42b4de635afccaf70c78ffff4090b42a1cbfbb60ed801 /root/tz45-work/days/1794441600.slots.txt is tz45-days-1794441600.slots.txt of tz-45-l0-rule-w-inputs
[2026-11-16T10:31:07Z] R release 6dfb638cd08f7c338347d620ed3ed9e9e0aebcf200fab34bb6aeb0a6b7050084 /root/tz45-work/days/1794528000.json is tz45-days-1794528000.json of tz-45-l0-rule-w-inputs
[2026-11-16T10:31:07Z] R release 74d6c047066307175769f4c5cac13fdcd0aaeba7d5d28f80acaeeb779688cdaa /root/tz45-work/days/1794528000.slots.txt is tz45-days-1794528000.slots.txt of tz-45-l0-rule-w-inputs
[2026-11-16T10:31:07Z] R release 6d6b0bd4e2dd39b936787c41b1dfd56e1e225dadebb25c79937e7771308090e5 /root/tz45-work/fetch/1794182400.json is tz45-fetch-1794182400.json of tz-45-l0-rule-w-inputs
[2026-11-16T10:31:07Z] R release bafbfb4a04b2a83d110a75fc03d311bfb53802667d7ec0938c295cb4656ccaa1 /root/tz45-work/fetch/1794182400.polls.jsonl is tz45-fetch-1794182400.polls.jsonl of tz-45-l0-rule-w-inputs
[2026-11-16T10:31:07Z] R release 3c90f5a48be59c5d1ef4822adee950eac4c14f0b9572142c495b3d6af9b4be15 /root/tz45-work/fetch/1794268800.json is tz45-fetch-1794268800.json of tz-45-l0-rule-w-inputs
[2026-11-16T10:31:07Z] R release 3a48a45a0ed5d93e6cbda1c16de951ddfa56a1b45112b4087f8c83d7051bbba1 /root/tz45-work/fetch/1794268800.polls.jsonl is tz45-fetch-1794268800.polls.jsonl of tz-45-l0-rule-w-inputs
[2026-11-16T10:31:07Z] R release 065f89f2e2cc1214ec1ee634a3e1d4dc21f9ce0ff102d0ae94645b0b067b0c73 /root/tz45-work/fetch/1794355200.json is tz45-fetch-1794355200.json of tz-45-l0-rule-w-inputs
[2026-11-16T10:31:07Z] R release 63d997837a0146a08ffb13324b5fac96fb494191da197df91c68a457650d493d /root/tz45-work/fetch/1794355200.polls.jsonl is tz45-fetch-1794355200.polls.jsonl of tz-45-l0-rule-w-inputs
[2026-11-16T10:31:07Z] R release 0ae5be7dc825fcb75068f52302be92d6fa4da2ced9a9895e96d8b8a5947b7a48 /root/tz45-work/fetch/1794441600.json is tz45-fetch-1794441600.json of tz-45-l0-rule-w-inputs
[2026-11-16T10:31:07Z] R release d35cd64290914e370d59252760504435a6a503a636e5410972d552af223f4481 /root/tz45-work/fetch/1794441600.polls.jsonl is tz45-fetch-1794441600.polls.jsonl of tz-45-l0-rule-w-inputs
[2026-11-16T10:31:07Z] R release 1a6c2d17a63bf78e718477ad0af8a547d3a088240d0bc9e8754c78f675e800d8 /root/tz45-work/fetch/1794528000.json is tz45-fetch-1794528000.json of tz-45-l0-rule-w-inputs
[2026-11-16T10:31:07Z] R release 8b9ed8b9936807ece05718c96558aa9896cd92502a1f7f983ecc9923e67e56f0 /root/tz45-work/fetch/1794528000.polls.jsonl is tz45-fetch-1794528000.polls.jsonl of tz-45-l0-rule-w-inputs
[2026-11-16T10:31:07Z] R copied 69b7f55f6e0a33c65fa2f3aa6e24fd6267fb58c7e56e6b0095b3fbc95195ef17 /root/btc-forensics/tz45-work--logs--00-instant.log
[2026-11-16T10:31:07Z] R copied e9e5eef98db72da04ac12de4dec3bd9693dae9921da069eca97e28ca8faa60d9 /root/btc-forensics/tz45-work--logs--00-ready.log
[2026-11-16T10:31:07Z] R copied 6cb73385830e99fef267e71525d15d2e0d5e3b35f34257eab5af9190beb09694 /root/btc-forensics/tz45-work--logs--01-stage.log
[2026-11-16T10:31:07Z] R copied 03d82841fa95ba95ba5b399515b3611ae2df53af5b9ce40f205cdb4d661061a1 /root/btc-forensics/tz45-work--logs--02-fingerprint.log
[2026-11-16T10:31:07Z] R copied 2299161662b78b8ba2a6ab0a911145c7ffe0192e63bf9cf61714ded2af3addd5 /root/btc-forensics/tz45-work--logs--03-host-gate.log
[2026-11-16T10:31:07Z] R copied 08feab30cd99078e1611da8c4fa7f49b72eaac300bbd31acc3374e4c06f7bd64 /root/btc-forensics/tz45-work--logs--05-number.log
[2026-11-16T10:31:07Z] R copied e2d64e77f2d49658da9dbc20423f781cf8b8b0e1d0107aa71c9c734e0fe0c217 /root/btc-forensics/tz45-work--logs--05-refs.log
[2026-11-16T10:31:07Z] R copied 8042211fe617315173efce1ac6e6589327252bb319ad1cd597728d32b1a713d6 /root/btc-forensics/tz45-work--logs--10-number.log
[2026-11-16T10:31:07Z] R copied b5c83a40abc92388b857bbe53f62d37025d3d8902c7f5c6e7391772481a8cc47 /root/btc-forensics/tz45-work--logs--11-worktree.log
[2026-11-16T10:31:07Z] R copied 619f3aa0bec3907e0c663deae378e07c592fc7c520d86c59c57b69df5e4ff9f8 /root/btc-forensics/tz45-work--logs--12-fingerprint.log
[2026-11-16T10:31:07Z] R copied 77ab1cd3afae778684a0e9404a3419b7298e311ca462d8daebb9421199ac2fd8 /root/btc-forensics/tz45-work--logs--13-push.log
[2026-11-16T10:31:07Z] R copied e8d90a760ebde185747a35f044a7af59035314c753c579d520a0b6e1e5f1c786 /root/btc-forensics/tz45-work--logs--14-pr.log
[2026-11-16T10:31:07Z] R copied a621b2eb10b650ae50f874baa639a43c1d2d9f6f26684a2abe592e67f57b0d6f /root/btc-forensics/tz45-work--logs--20-selftest.log
[2026-11-16T10:31:07Z] R copied 0276fdc31fccd4fbd3bf1a3b196719db6c93ed6d07c3cc8a537ac78a0a23e7a6 /root/btc-forensics/tz45-work--logs--30-still.log
[2026-11-16T10:31:07Z] R copied 2d7e3a5194e6cf1c369e22e0e24f6082c6107e68ebbbc46344e189cb8fedbe1a /root/btc-forensics/tz45-work--logs--31-scratch.log
[2026-11-16T10:31:07Z] R copied 66e75b50a5862257c5858321c023545067c75bb743a04706cf9b715902306acb /root/btc-forensics/tz45-work--logs--32-reclaim-scratch.log
[2026-11-16T10:31:07Z] R copied 131f48a0266588ed289141ac7e2ce93ea85edc559b1c8b3ed5569c9b1f3ecded /root/btc-forensics/tz45-work--logs--40-archive.log
[2026-11-16T10:31:07Z] R copied bbb53b1bcc5ff61ee2352d5dd91cb9949f3645cb7e0385b7f26dc28cc79c3040 /root/btc-forensics/tz45-work--logs--50-rehearse.log
[2026-11-16T10:31:07Z] R copied 10c3ef53edaaadd9fcab143de26632fbf2a34aff10a048afa71e8c72b5dccc61 /root/btc-forensics/tz45-work--logs--60-fetch.log
[2026-11-16T10:31:07Z] R copied d73f54bc1e2433cd7d99adc628b56410b791b5696544c511e910b9554fc48146 /root/btc-forensics/tz45-work--logs--70-replay.log
[2026-11-16T10:31:07Z] R copied 8e88d8db692177f6efb6c8016eebbe78e655b84a6d40e3c8c3752cb1a74fedd7 /root/btc-forensics/tz45-work--logs--71-replay-again.log
[2026-11-16T10:31:07Z] R copied 798a64632932a97a5780cd78fbb11058db20fdc5117f9c9607b86a46b64fb584 /root/btc-forensics/tz45-work--logs--75-rescore.log
[2026-11-16T10:31:07Z] R copied d2d580f9be4767f2fb03e16533797ca788a776fddeb959c366812e3e48748ba7 /root/btc-forensics/tz45-work--logs--80-score.log
[2026-11-16T10:31:07Z] R copied 89b71cb487191ba322243ac6f1f59ae2e2aa46e53f62bb9d08a8f9d678bcb82b /root/btc-forensics/tz45-work--logs--81-score-again.log
[2026-11-16T10:31:07Z] R copied 303bfdfbe4f0332081d8f94b2a0ac59380622e8f4063f684e21599754fe3d348 /root/btc-forensics/tz45-work--logs--82-pack.log
[2026-11-16T10:31:07Z] R copied 9655999a22a515df819b526a1c9fbbf065f4a77f12adc552193863b87ed77f1d /root/btc-forensics/tz45-work--logs--83-pack-again.log
[2026-11-16T10:31:07Z] R copied e5b369d7ab95400faa502e89bb623205e63fa66f2798e2f007c61e43b4022c1e /root/btc-forensics/tz45-work--logs--85-upload.log
[2026-11-16T10:31:07Z] R copied 01e39dda314c0e31632328d67c5d84a59e5f90aff5c34ffa1cc84b0cd6c17591 /root/btc-forensics/tz45-work--logs--86-upload-wait.log
[2026-11-16T10:31:07Z] R copied e2e97e0d2ddeceb8cfbd801c67a7d632a7c9ef7df65c03cdd14e95cc0aa440c9 /root/btc-forensics/tz45-work--logs--88-verify.log
[2026-11-16T10:31:07Z] R copied a6379a2fed55ffdac14553c62bb29cc2f10c9c12bbc32a22b55398f280cb8f39 /root/btc-forensics/tz45-work--logs--95-still.log
[2026-11-16T10:31:07Z] R copied 6787bf095a4aea851d5aa058787b78d1872389c344bfbb9f627e4d0eae0948e0 /root/btc-forensics/tz45-work--logs--96-host-gate-again.log
[2026-11-16T10:31:07Z] R copied 3637846061854c2c8d107dd1c44a24cc4102cf610f546e1b1dfe01a09d2a8a3a /root/btc-forensics/tz45-work--logs--97-archive-again.log
[2026-11-16T10:31:07Z] R copied c990a91fbfb1b0a8a683efff1c06eab809e746247662ea9753239f42f566bc5a /root/btc-forensics/tz45-work--logs--98-closing.log
[2026-11-16T10:31:07Z] R copied 4a5495dc117a98ca3c0e8bad3f3c64fab35cd9577c2c50ab11b0a14b31468cea /root/btc-forensics/tz45-work--logs--99-selfcheck.log
[2026-11-16T10:31:07Z] R release 3f1cefb098f538dde99dadc13aba9a6c0be2e44bcc761ccfa6516350e8d0d9db /root/tz45-work/out/rewardbook-inputs-1794182400.tar is rewardbook-inputs-1794182400.tar of tz-45-l0-rule-w-inputs
[2026-11-16T10:31:07Z] R release 35a219bcd999c17bba8b8b8f664fd3d3107c4367e1f573dfe38ba2509ea34f8c /root/tz45-work/out/rewardbook-inputs-1794268800.tar is rewardbook-inputs-1794268800.tar of tz-45-l0-rule-w-inputs
[2026-11-16T10:31:07Z] R release fd5df7d694a8d25d246c3189bdf8a9a64597a8d040ad2585d46852f5ce7fc2c6 /root/tz45-work/out/rewardbook-inputs-1794355200.tar is rewardbook-inputs-1794355200.tar of tz-45-l0-rule-w-inputs
[2026-11-16T10:31:07Z] R release 840a13670100aee0cc584b06b1b4cc85cbfc0161ef0a183603d9056fa7024dfb /root/tz45-work/out/rewardbook-inputs-1794441600.tar is rewardbook-inputs-1794441600.tar of tz-45-l0-rule-w-inputs
[2026-11-16T10:31:07Z] R release ed98acd9ccd70d492dd0fdba4f4e4a465531f92a557b165ea2046c5aee826f48 /root/tz45-work/out/rewardbook-inputs-1794528000.tar is rewardbook-inputs-1794528000.tar of tz-45-l0-rule-w-inputs
[2026-11-16T10:31:07Z] R release 23843e59372a48409a287f91f8a14d243d7b0bb29228748f1d6b2b8572f806b3 /root/tz45-work/out/tz45-manifest.json is tz45-manifest.json of tz-45-l0-rule-w-inputs
[2026-11-16T10:31:07Z] R copied 2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673 /root/btc-forensics/tz45-work--stage--research--tz27-pairbook-archive.py
[2026-11-16T10:31:07Z] R copied 4720e78573e54b1325dd24af7c30e0de59bfb4c1879d309a23fa6bab6b32d2d4 /root/btc-forensics/tz45-work--stage--research--tz45-l0-rule-w.py
[2026-11-16T10:31:07Z] RECLAIM PASS: 75 files considered, 41 named by a report, 34 kept by name, 47 copied, 0 already held, 28 left to the Release tz-45-l0-rule-w-inputs that holds them; forensic store 2532 -> 2579 files
[2026-11-16T10:31:07Z] malloc tuned: True
[2026-11-16T10:31:07Z] peak memory of this run: 47693824 bytes
[2026-11-16T10:31:07Z] opens refused: 0, by TZ-27's hook: 0; reward book opens: 0, listings: 0
reclaim exit=0

$ cd /root/btc-5m-twap && git -C /root/btc-5m-twap worktree remove /root/tz45-work/wt; echo "exit=$?"
exit=0
$ rm -rf /root/tz45-work; echo "exit=$?"
exit=0
$ test -e /root/tz45-work; echo "exit=$?"
exit=1
$ git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
/root/btc-5m-twap       4bb14d8 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
$ find /root/btc-forensics -type f | wc -l
2579
$ df -B1 --output=source,size,avail /var/lib/btc-recorder
Filesystem       1B-blocks      Avail
/dev/vda2      31612203008 9301143552
```

**V20:** 75 files considered. 41 were named by a report, 34 kept by name (the 34 logs) and 47 copied: the 34 logs, `state.json`, `read-ledger.jsonl`, `release-set.json`, `upload.jsonl`, `transfers.jsonl`, `verify.json`, `rehearsal-base.txt`, `rehearsal-w.txt`, `rescore.txt`, both timing files and the two staged instruments. 0 were already held, and 28 were left to the Release that holds them. The forensic store went from 2,532 to 2,579 files, before plus the 47 copies. **V21:** `git worktree remove` without `--force` exited `0`, and `test -e /root/tz45-work` exited `1`. `git worktree list` names `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else. The branch `tz-45-l0-rule-w` stays on `origin` and as a local ref. Free space after §9 was `9,301,143,552` bytes.

---

## 6. What could not be implemented as written

1. **The fifth member came sooner than the TZ's header expected.** The header expected 2026-11-14 as the fifth member, with 2026-11-11 behind it. The walk found 2026-11-11 a member: a block of 87 slots from 02:15 UTC, its slot of 02:00 UTC `ended early`. So the five members are 2026-11-09 to 2026-11-13 and no candidate is a non-member. This is the set's rule as written, not a deviation. The candidate days `pack` took are therefore five, and the assets 28 (`23` and one a candidate day).
2. **`fetch`'s peak memory, `75,780,096` bytes, is above the Architect's bound of `72,000,000`** (§0.4: "the Architect's bound on any mode's peak … set above the largest his runs of these bytes gave"). It is below the modelled host peak of `86,329,224` that V19 sets it beside. No gate reads it.
3. **The Boss's first reply was not the paste.** After the hand-over at 08:37:24 UTC, the Boss's next message asked the session to continue, and the log did not exist. The Executor did not run B-UPLOAD, which is the Boss's by its own text. At 09:13:27 UTC it restated the same paste once, in plain words, and recorded that as a reminder in `86-upload-wait.log`. The Boss ran the paste at 10:20:43 UTC, the first and only run. The wait block's first run printed `0 of 1` after its last sleep and its second `1 of 1`. Neither was run inside a loop or a background task.
4. **Lines the Executor added to its logs beyond the TZ's commands.**
   - `01-stage.log` ends with an `exit=0` line.
   - `10-number.log` and `11-worktree.log` begin with a `date -u` line and carry `fetch exit=`, `exit=`, `worktree exit=` and `stage exit=` lines.
   - `13-push.log` begins with a `date -u` line and carries `commit exit=`, `ls-remote exit=` and `push exit=` lines, and the commit's `git show --stat`.
   - `14-pr.log` begins with a `date -u` line and ends with `exit=0`.
   - `32-reclaim-scratch.log` carries each removed directory's path before its `rm -rf`.
   - `99-selfcheck.log` begins with a `date -u` line.
   - `05-refs.log` carries, after `ls-remote`'s 157 lines, the `git log --first-parent --name-status 5192aff..origin/main` that §0.5 asks to be reported. A `git fetch origin` ran before that log, to resolve `origin/main`.

   None of these lines changes what a command printed.
5. **How the TZ's blocks were run verbatim.** §0.0's readiness read, §0.1's staging script, §0.3's host gate and §3.14's closing block were each run by extracting their lines from the committed TZ with `sed -n` and piping them to `bash`, so their text was the TZ's character for character. §0.1's script at §3.1 differed in its argument alone, `/root/tz45-work/wt`. §0.3's block ran with `S` set to this session's scratchpad, `/tmp/claude-0/-root-btc-5m-twap/892ec9bf-0691-50df-8231-a07862dcb100/scratchpad`.
6. **The cause of the eighteen streamless slots is not established** (§2.10). The reward book's journal holds no entry for those hours, its own log is under the store and not opened by this TZ, and the slot records' `off_reason` is not printed by the instrument. The archive's ledger records `6,874,419,200` bytes free before its removal at 01:36:02 UTC on 2026-11-14, below `STREAM_FLOOR`. That is consistent with the floor stopping the streams, and is not proof of it.
7. **The read ledger holds no line for `upload` or `verify`.** §3.1 says every mode that reads the store, a Release or the set writes the worktree's `HEAD` and its own SHA-256 into `read-ledger.jsonl`. The instrument writes that line in `rehearse`, `fetch`, `replay`, `rescore`, `score` and `pack` (9 lines). `upload` and `verify` assert the pack's commit and the worktree's `HEAD` themselves (§2.7), and write no ledger line. This was recorded, not changed.
8. **The model was not read from the session's metadata.** The TZ names Claude Opus 5.5, and the session's configuration names `claude-opus-5-5`. No call to read the serving model was made.
