# TZ-16a — Phase 2's decisive gate, first look — REPORT

**Status: executed.** Two scored runs on the pushed commit `5076b43` each read the labels once, and their outputs are byte-identical.

- **Reading at each `tau`:** 240 **UNDECIDABLE**; 180 **NO EDGE**; 120 **NO EDGE**; 90 **NO EDGE**; 60 **NO EDGE**. No `tau` reads EDGE.
- **Verdict (§4.4):** NO EDGE at `tau` 180, 120, 90 and 60, each closed: where the Student pricer disagreed with the market by more than the fee, its side did not win at the rate it claimed. `tau` 240 is UNDECIDABLE.
- **Interlock (§3.10, §4.3): HOLD.** 0 failures among 297 exposed units and 0 among 2,311 control units; `p_I = 1`. Block K-18a was not run.
- **Which TZ must follow:** §4.2's second look, at `tau` 240 alone. No confirmation TZ, because no `tau` reads EDGE.

**What decided each reading.** Each reading is the count `S` of wins against the look's two critical counts, `c` for EDGE and `d` for NO EDGE:

| `tau` | `S` | `c` | `d` | reading |
|---|---|---|---|---|
| 240 | 538 | 566 | 528 | UNDECIDABLE: 28 below `c` and 10 above `d` |
| 180 | 547 | 592 | 559 | NO EDGE: 12 below `d` |
| 120 | 506 | 538 | 510 | NO EDGE: 4 below `d` |
| 90 | 418 | 463 | 432 | NO EDGE: 14 below `d` |
| 60 | 256 | 296 | 273 | NO EDGE: 17 below `d` |

- **Error allocation.** Each false-reading probability is at most `0.002` per `tau` on this look, as §4.1 fixes. Summed over the five `tau`, `FP_E` is `0.008634492672` and `FP_N` is `0.008376619469`.
- **Influence.** Removing the single most influential member moves no reading.
- **The same set's constants,** written to disk before either label read, are byte-identical across all four runs.
- **B2.** This report on `main` is Phase 2's decisive first reading, the one CANON PART II calls TZ-16's (map §5). Map §5 says B2 is "written only after TZ-16a's first reading is on `main`".

The TZ header names its executor model, and this session runs that model. **This report follows the TZ's §8 order.** That order puts publication after validation and retention after publication, where contract §8 orders the sections differently. The contract's preamble lets the TZ win for this task.

---

## 0. Gates, host, interpreter, floor, refs, trees and readiness — §0

### 0.1 Fingerprint — asserted inside the instrument at step 0 (V1, V10)

**Where it was read.**

- `git fetch` brought `origin/main` to `0c2d3f0e2d29b72abcbed4be671c998f220510f0`.
- The primary checkout `/root/btc-5m-twap` was fast-forwarded to it from `86b51a4` (contract §1).
- The instrument read the map in its own checkout, `/root/tz16a-work/wt` at `5076b43`. The branch changes one path, so the map there is `origin/main`'s byte for byte.

**The TZ file.** `CryptoTZ/TZ-16a-phase2-decisive-gate.md` has 1,043 lines and 78,589 bytes, SHA-256 `4e9ec4895337f21693a05bf7f6d6c163e77d6649273c225074c732ceefc2b771`. It landed at `0c2d3f0`. The file it replaces, `CryptoTZ/TZ-16-phase2-decisive-gate.md`, hashes to `0e0752cdfacaa517102077052372a32de9557eb6baa37f5354a499b83c7196dd`, as the header states.

**Map revision required:** `2026-09-27-a`. **Read:** `2026-09-27-a`.

| anchor | required by TZ-16a | read from map §0 | re-derived by the instrument |
|---|---|---|---|
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` | a Release asset, not a file anchor |
| `A2` — collector | `6c5089330629` | `6c5089330629` | `6c5089330629` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-undecidable-5tau` | same | not a file anchor |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b` | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` | `9fd1c7de0f74` | `9fd1c7de0f74` |
| `A6` — pricer | `729f0bcdbee3` | `729f0bcdbee3` | `729f0bcdbee3` |

**6 of 6 anchors, 4 of 4 re-derived, 24 of 24 `frozen` rows equal to the map, 2 `tracked` and 1 `reported`.**

- All of it is asserted at step 0 by `v1_gates`. The expected revision, anchors and counts are literals of the instrument, and the rows are read by `tz14.fingerprint_rows()`.
- It held in all seven instrument runs: three with `--selftest`, then D1, D2, S1 and S2.
- `tz14.v1_gates` and `tz15.v1_gates` were not called (V2).

The table below is S1's own record of step 0 (`tz16a-run.json`). The last row is this TZ's file as it stands on the branch (V10).

| path | lines | bytes | state | SHA-256 | equals the map |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 1,002 | 197,723 | reported | `bd8d04323544a2756e26797cf0d5f0b2d6deed3dd303e351c5f09c5daee6723f` | — |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | **yes** |
| `research/twap-divergence.py` | 1,135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | **yes** |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | **yes** |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | — |
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
| `research/tz13-sized-gate-test3.py` | 1,074 | 53,901 | frozen | `a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd` | **yes** |
| `research/tz14-quote-inventory.py` | 2,124 | 109,972 | frozen | `978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02` | **yes** |
| `research/tz15-phase2-gate.py` | 1,517 | 73,799 | frozen | `66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3` | **yes** |
| `research/tz17-settlement-chain.py` | 1,102 | 38,622 | frozen | `e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92` | **yes** |
| `research/tz18a-chainbook-capture.py` | 1,683 | 69,517 | frozen | `e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae` | **yes** |
| `research/recorder/recorder.py` | 608 | 25,658 | frozen | `9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03` | **yes** |
| `research/recorder/config.py` | 112 | 4,773 | frozen | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | **yes** |
| `research/recorder/manifest.py` | 254 | 10,002 | frozen | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | **yes** |
| `research/recorder/analyze.py` | 813 | 34,705 | frozen | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` | **yes** |
| `research/recorder/probe.py` | 227 | 9,324 | frozen | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | **yes** |
| `research/recorder/selftest.py` | 573 | 30,591 | frozen | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` | **yes** |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | — |
| `research/tz16a-phase2-decisive-gate.py` — this TZ's file, on the branch at `5076b43` | 2,198 | 111,192 | new | `3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125` | — |

### 0.2 Host gate — verbatim, from `/root/btc-5m-twap`, before anything else

It was run through `bash -v`, which echoes each command before its output. `git fetch` and contract §1's fast-forward preceded it.

```
2026-09-27T12:04:09Z 1790510649
df -B1 --output=source,size,avail /var/lib/btc-recorder
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 13024239616
find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json
pgrep -fx '/root/tz04a-env/venv/bin/python -B -u recorder.py'; echo "exit=$?"
228592
exit=0
grep -c 4216c04673ced76b5b2ac60ef57c9abedc46f9b9 /var/lib/btc-recorder/runtime.jsonl
1
pgrep -fx '/root/tz01-env/venv/bin/python -B -u /root/tz18a-svc/tz18a-chainbook-capture.py --serve'; echo "exit=$?"
2699889
exit=0
du -sb /root/PROJECT_GAMING_PS5
435703872	/root/PROJECT_GAMING_PS5
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
disabled
exit=1
systemctl is-active telemetry-watch.service; echo "exit=$?"
inactive
exit=3
for d in /root/tz15-work /root/tz16-work /root/tz16a-work /root/tz18a-work /root/tz18a-svc; do test -e "$d"; echo "$d exit=$?"; done
/root/tz15-work exit=0
/root/tz16-work exit=0
/root/tz16a-work exit=1
/root/tz18a-work exit=0
/root/tz18a-svc exit=0
find /root/btc-forensics -type f | wc -l
1046
git worktree list
/root/btc-5m-twap           0c2d3f0 [main]
/root/tz15-work/wt          f7f171a [tz-15-phase2-gate]
/root/tz15-work/wt-report   c729008 (detached HEAD)
/root/tz16-work/wt-report   a9e0b45 (detached HEAD)
/root/tz18a-work/wt         ca4bbc1 [tz-18a-chainbook-capture]
/root/tz18a-work/wt-report  7d8cb75 (detached HEAD)
2026-09-27T12:04:09Z 1790510649
```

| check | required | read | result |
|---|---|---|---|
| **H1** | `find` prints exactly one path | one path | **holds** |
| **H2** | the first `pgrep -fx` prints one line and `exit=0` | `228592`, `exit=0`, the pid map §8 records | **holds** |
| **H3** | source `/dev/vda2`, size `31612203008`, `grep -c` at least `1` | `/dev/vda2`, `31612203008`, `1` | **holds** |
| **H4** — recorded | the chain book service | `2699889`, `exit=0`, the pid map §2.5 records | recorded |
| resource gate | `avail` at least `2,060,000,000` | `13,024,239,616` | **holds** |
| trees | `tz15-work`, `tz16-work`, `tz18a-work` and `tz18a-svc` exit `0`; `tz16a-work` exits `1` | `0`, `0`, `0`, `0`; `1` | **holds** |
| forensic store | exactly `1,046` files | `1,046` | **holds** |
| `du`, `systemctl`, `git worktree list` | printed, no threshold | `435,703,872` bytes; `disabled` (1), `inactive` (3); six worktrees, as map §3 counts | recorded |

Step 1 of every run then asserted that the recorder's newest start record carries `4216c04673ced76b5b2ac60ef57c9abedc46f9b9`, through `tz11a.host_read`.

### 0.3 Interpreter

Every instrument command ran on `/root/tz01-env/venv/bin/python`: Python `3.12.3`, `numpy` `2.5.3`. `import numpy` succeeds, and the committed chain the instrument loads imports it. The instrument itself computes nothing in `numpy`. Every run used `python -B`, so no `__pycache__` was written into the checkout.

### 0.4 Resource floor — every free-space read, with its instant, reader and bound

| UTC | free bytes on `/dev/vda2` | read by | bound | status |
|---|---|---|---|---|
| 2026-09-27T12:04:09Z | 13,024,239,616 | §0.2 host gate, `df -B1 --output=source,size,avail` | `2,060,000,000`, the resource gate | checked by the Executor; recorded |
| 2026-09-27T12:04:28Z | 13,024,112,640 | §0.5 read 1, `df -B1 /dev/vda2` | `2,000,000,000` | recorded |
| 2026-09-27T16:34:10Z | 12,975,820,800 | D1, host read 1 — `tz11a.host_read` | `2,060,000,000` | **asserted** |
| 2026-09-27T16:37:58Z | 12,975,570,944 | D1, host read 2 — `tz11a.host_read` | `2,000,000,000` | **asserted** |
| 2026-09-27T16:38:17Z | 12,972,339,200 | D1, host read 3 — `tz11a.host_read` | `2,000,000,000` | **asserted** |
| 2026-09-27T16:39:05Z | 12,971,999,232 | D2, host read 1 — `tz11a.host_read` | `2,060,000,000` | **asserted** |
| 2026-09-27T16:42:57Z | 12,971,675,648 | D2, host read 2 — `tz11a.host_read` | `2,000,000,000` | **asserted** |
| 2026-09-27T16:43:16Z | 12,968,472,576 | D2, host read 3 — `tz11a.host_read` | `2,000,000,000` | **asserted** |
| 2026-09-27T16:43:39Z | 12,968,292,352 | §0.5 read 2, `df -B1 /dev/vda2` | `2,000,000,000` | recorded |
| 2026-09-27T16:43:51Z | 12,968,222,720 | S1, host read 1 — `tz11a.host_read` | `2,060,000,000` | **asserted** |
| 2026-09-27T16:47:39Z | 12,960,112,640 | S1, host read 2 — `tz11a.host_read` | `2,000,000,000` | **asserted** |
| 2026-09-27T16:48:01Z | 12,956,852,224 | S1, host read 3 — `tz11a.host_read` | `2,000,000,000` | **asserted** |
| 2026-09-27T16:48:31Z | 12,956,655,616 | S2, host read 1 — `tz11a.host_read` | `2,060,000,000` | **asserted** |
| 2026-09-27T16:52:19Z | 12,956,442,624 | S2, host read 2 — `tz11a.host_read` | `2,000,000,000` | **asserted** |
| 2026-09-27T16:52:41Z | 12,953,186,304 | S2, host read 3 — `tz11a.host_read` | `2,000,000,000` | **asserted** |
| 2026-09-27T16:56:03Z | 12,969,000,960 | the closing read, `df -B1 --output=source,size,avail` | `2,000,000,000` | recorded |

**Lowest reading: `12,953,186,304` bytes**, S2's host read 3 at 16:52:41Z.

- Every asserted read is `tz11a.host_read`'s `assert free >= floor`. That is `2,060,000,000` at a run's start and `2,000,000,000` after (§0.4).
- **Not in the table:** the three `--selftest` runs also asserted host read 1 at `2,060,000,000` and passed. That mode prints no host read and writes no run file, so their instants and values were not kept (§13 item 4).
- By the closing read, `/root/tz16a-work` held `22,167,020` bytes: both worktrees, the four run directories, the logs and the scratch harnesses. That is inside the `60,000,000` bytes §0.4 allows between the two floors.

### 0.5 Preflight — twice, 16,750.8 s apart

Read 1, before the build:

```
2026-09-27T12:04:28Z 1790510668.487515285
df -B1 /dev/vda2
Filesystem       1B-blocks        Used   Available Use% Mounted on
/dev/vda2      31612203008 17152221184 13024112640  57% /
du -sb /root/PROJECT_GAMING_PS5
435720325	/root/PROJECT_GAMING_PS5
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
disabled
exit=1
systemctl is-active telemetry-watch.service; echo "exit=$?"
inactive
exit=3
test -e /root/tz16a-work; echo "tz16a-work exit=$?"
tz16a-work exit=1
du -sb /root/.claude
195260975	/root/.claude
du -sb /root/tz16-work
3724492	/root/tz16-work
2026-09-27T12:04:28Z 1790510668.629182091
```

Read 2, before the first run with `--score`. It came 11 s after the push and 11 s before S1 started.

```
2026-09-27T16:43:39Z 1790527419.287294814
df -B1 /dev/vda2
Filesystem       1B-blocks        Used   Available Use% Mounted on
/dev/vda2      31612203008 17208041472 12968292352  58% /
du -sb /root/PROJECT_GAMING_PS5
437488794	/root/PROJECT_GAMING_PS5
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
disabled
exit=1
systemctl is-active telemetry-watch.service; echo "exit=$?"
inactive
exit=3
du -sb /root/tz16a-work
15701634	/root/tz16a-work
du -sb /root/.claude
197209080	/root/.claude
du -sb /root/tz16-work
3724492	/root/tz16-work
2026-09-27T16:43:39Z 1790527419.776184572
```

**Across the 16,750.8 s between them:**

- **Free space** moved by `−55,820,288` bytes, `−287,918,962` bytes/day at that rate.
- **`/root/PROJECT_GAMING_PS5`** grew `+1,768,469` bytes, `+9,121,697` bytes/day.
- **`telemetry-watch.service`** read `disabled` (1) and `inactive` (3) at both.

**This session's own footprint (map §7 item 29), stated separately at both reads:**

| read | `/root/tz16a-work` | `/root/.claude` | `/root/tz16-work`, TZ-16's |
|---|---|---|---|
| read 1 | did not exist (`exit=1`), `0` | `195,260,975` | `3,724,492` |
| read 2 | `15,701,634` | `197,209,080` | `3,724,492` |

- The footprint and the consumer's growth come to `19,418,208` bytes. Taking them out leaves `36,402,080` bytes, about `187,760,570` bytes/day, for the capture, the chain book and everything else on the shared host.
- `df` counts blocks and `du -sb` counts apparent bytes, so the remainder is approximate.
- These rates gate nothing beyond §0.4.

### 0.6 Refs — `git ls-remote origin`, before the branch existed

```
2026-09-27T12:04:34Z 1790510674
0c2d3f0e2d29b72abcbed4be671c998f220510f0	HEAD
0c2d3f0e2d29b72abcbed4be671c998f220510f0	refs/heads/main
ca4bbc1dd583cbb62f3c0c985938d229b526ce7e	refs/heads/tz-18a-chainbook-capture
d9e58e8febd8548221598eed137cf40d31496047	refs/pull/1/head
e45f38e89b5ee18e64a16a654b341d74fadcac26	refs/pull/10/head
d34606ee9a592e51293eaad0996c7cae3b84dfcd	refs/pull/11/head
274651805c765bb977c635d75fd1ebdb2c8f550a	refs/pull/12/head
6dc0e24ae1542f98789967bf48057268731a2030	refs/pull/13/head
7ef972397a12bce0cc76b1f58ceda3e5caa43cdc	refs/pull/14/head
ffef5cd822e2e47ce1edd8fff706471a441e9a5f	refs/pull/15/head
f7f171a2e1e8b4b3eafa810f5022f1ca1c5a65b1	refs/pull/16/head
8f1bc93e454275ddb3f0e060bed3bb9f2f9cf31b	refs/pull/17/head
8caa0b41d5cdf9e74e92b11d4317d59a2ee7b567	refs/pull/18/head
ca4bbc1dd583cbb62f3c0c985938d229b526ce7e	refs/pull/19/head
3895356aff853f2fcb1b030b1502acb95b16f0a5	refs/pull/2/head
ee2f6327390ef4d0c6169d1fba1a2ed4ae936dc3	refs/pull/3/head
0e13a5c76dfa2469ff25b3b0dd282872decf6f25	refs/pull/4/head
4216c04673ced76b5b2ac60ef57c9abedc46f9b9	refs/pull/5/head
5ed667afd1b53f036b9f938fcce13c0d709cd77f	refs/pull/6/head
c44af687203d14d5d485d4297c04cfb827096af9	refs/pull/7/head
26bbb61aed774a88355dd5204d8b69fda9135a68	refs/pull/8/head
e2625ea2b5473c311d59a48f32540ce39d58e591	refs/pull/9/head
d3251aa2bd312409f7b096bfd5968f3bedbd1be5	refs/tags/tz-01a-dataset
ea9290b92b9fa50c22d0560d5d01dfa392af44df	refs/tags/tz-01a-dataset^{}
---first-parent above a9e0b45
0c2d3f0e2d29b72abcbed4be671c998f220510f0 2026-09-27 16:00:57 +0400 Add files via upload
188578c674d045eb7179e512f9978d8d2ce276cc 2026-09-27 16:00:38 +0400 Update SYSTEM-MAP.md
== 0c2d3f0e2d29b72abcbed4be671c998f220510f0
A	CryptoTZ/TZ-16a-phase2-decisive-gate.md
== 188578c674d045eb7179e512f9978d8d2ce276cc
M	SYSTEM-MAP.md
count=2
--- revision on main
**Revision 2026-09-27-a.** Written by the Architect; the Executor never edits it. This is a
--- tz-16a branch on origin?
exit=0
```

**Recorded, not BLOCKING:**

- `main` stands at `0c2d3f0`, not at map §1's `a9e0b45`. Two commits sit above `a9e0b45` on the first-parent line: `188578c`, which modifies `SYSTEM-MAP.md`, and `0c2d3f0`, which adds this TZ. Their number is recorded, not asserted.
- **Neither BLOCKING condition holds.** `main` carries revision `2026-09-27-a`, and `refs/heads/tz-16a-phase2-decisive-gate` did not exist: the block's last `ls-remote` printed no ref line.
- After step C it reads `5076b4305c7800fc7eed0cd3fe05d9577d1b6cf7 refs/heads/tz-16a-phase2-decisive-gate` (§5).

### 0.7 The recorder's working tree

- The primary checkout `/root/btc-5m-twap`, where the recorder runs from `research/recorder`, was never switched off `main`.
- Its one change was contract §1's fast-forward from `86b51a4` to `0c2d3f0`. That touched three paths — the TZ-16 report, this TZ and `SYSTEM-MAP.md` — and none under `research/recorder/`.
- The branch was built in `/root/tz16a-work/wt`, and this report was committed from `/root/tz16a-work/wt-report`. Both were added with `git worktree add` from `origin/main`.
- `/root/tz16-work/wt-report` was left as it was until §9 (§12).

### 0.8 Readiness — verbatim, from `/root/btc-5m-twap`, reading manifests and nothing else

```
2026-09-27T12:04:17Z 1790510657
complete 2577 at-2400 1790451900 now 1790510659
2026-09-27T12:04:19Z 1790510659
```

**R-READY holds.**

- There are `2,577` complete manifests with `T0 > 1789669800`, against the `2,400` required.
- `now` is `1790510659`. That is at or past `t0s[2399] + 3,900` = `1790455800`, by `54,859` s.
- §3.3 then asserted the sufficient form on the members themselves (§2).

---

## 1. §3.1 and §3.2 — TZ-15's two files, and the dependence they give

**§3.1 — TZ-15's two files, located by hash:**

Regular files hashed under `/root/tz15-work`: 182.

| file | SHA-256 | copies | read |
|---|---|---|---|
| `tz15-observations.csv` | `a7ac8a495e00e21cd34af6ead7f05e9a2b741231c928bb61d4ec03ec0e610ce6` | 2 | `/root/tz15-work/run1/tz15-observations.csv` |
| `tz15-constants.json` | `e6a93f9371e9fb32404482dac7b542c330399117ba0cf93e466b846e5878dfd3` | 5 | `/root/tz15-work/dev1/tz15-constants.json` |

**The constants file's three values per `tau`, as read:** `per_tau[str(tau)]["n"]`, an integer, and `["sum_a"]` and `["sum_q"]`, JSON strings read as `D(...)`. Nothing else was taken from it. This is `tz16a-constants.json`'s `tz15_constants_per_tau`:

| `tau` | `n` | `sum_a` | `sum_q` |
|---|---|---|---|
| 240 | 405 | `216.23` | `233.579362178548589456` |
| 180 | 428 | `212.50` | `230.1410794878433773409` |
| 120 | 440 | `192.194` | `208.2308022961688662051` |
| 90 | 380 | `156.723` | `171.86830345826790914045` |
| 60 | 271 | `102.581` | `114.107227667538293020748` |

**§3.2's read of the observations file, against its literals and the constants file — V4 (a) and V4 (b):**

| `tau` | `n` | constants `n` | `sum y` | `sum a` | constants `sum_a` | `sum q` | constants `sum_q` |
|---|---|---|---|---|---|---|---|
| 240 | 405 | 405 | 210 | 216.23 | 216.23 | 233.579362178548589456 | 233.579362178548589456 |
| 180 | 428 | 428 | 211 | 212.50 | 212.50 | 230.1410794878433773409 | 230.1410794878433773409 |
| 120 | 440 | 440 | 190 | 192.194 | 192.194 | 208.2308022961688662051 | 208.2308022961688662051 |
| 90 | 380 | 380 | 164 | 156.723 | 156.723 | 171.86830345826790914045 | 171.86830345826790914045 |
| 60 | 271 | 271 | 99 | 102.581 | 102.581 | 114.107227667538293020748 | 114.107227667538293020748 |

**V4 (a): 35 of 35 comparisons hold; V4 (b): 15 of 15.**

| `tau` | `s*` | `FP` | quoted | gap | `POWER` at `s*` | quoted | gap |
|---|---|---|---|---|---|---|---|
| 240 | 238 | 0.007476034950200 | 0.007476034950 | 2.00E-13 | 0.325739887 | 0.325740 | 1.13E-7 |
| 180 | 232 | 0.008749059108653 | 0.008749059109 | 3.47E-13 | 0.432618207 | 0.432618 | 2.07E-7 |
| 120 | 210 | 0.007886034791558 | 0.007886034792 | 4.42E-13 | 0.430438487 | 0.430438 | 4.87E-7 |
| 90 | 173 | 0.006740872863538 | 0.006740872864 | 4.62E-13 | 0.459935046 | 0.459935 | 4.58E-8 |
| 60 | 115 | 0.008611872632895 | 0.008611872633 | 1.05E-13 | 0.467275598 | 0.467276 | 4.02E-7 |

**V4 (a) holds at 35 of 35.** Of these comparisons:

- **20 are against §3.2's literals:** `n`, `Σy`, `Σa` and `Σq` at each of the five `tau`.
- **15 are equalities with the constants file:** `n`, `Σa` and `Σq` at each `tau`.

Every comparison is an equality of values. `Σq` equals TZ-15's `sum_q` to every digit, and so equals the five full-precision literals. **V4 (b) holds at 15 of 15**, re-deriving TZ-15's constants through the committed `tz15.crit` and `tz15.pb_upper`. The closest margins are `4.62E-13` against `5e-13` at `tau` 90, and `4.87E-7` against `5e-7` at 120.

**§3.2 — the dependence, with the exact sums the Architect re-derives it from (map §7 item 70):**

Exact sums over `x = y - a` in ascending `T0`:

| `tau` | `n` | `sum x` | `sum x^2` |
|---|---|---|---|
| 240 | 405 | -6.23 | 73.3583 |
| 180 | 428 | -1.50 | 63.1864 |
| 120 | 440 | -2.194 | 51.851422 |
| 90 | 380 | 7.277 | 43.689311 |
| 60 | 271 | -3.581 | 19.397391 |

| `tau` | `k` | `P_k` | `A_k` | `B_k` |
|---|---|---|---|---|
| 240 | 1 | -6.7053 | -5.92 | -5.94 |
| 240 | 2 | -8.2970 | -5.39 | -5.55 |
| 240 | 3 | 5.7364 | -4.92 | -5.43 |
| 180 | 1 | -2.9604 | -1.28 | -1.32 |
| 180 | 2 | 5.7469 | -0.99 | -0.96 |
| 180 | 3 | -2.1622 | -1.05 | -0.56 |
| 120 | 1 | 1.68331 | -2.434 | -2.144 |
| 120 | 2 | 1.228546 | -2.474 | -3.074 |
| 120 | 3 | -1.40824 | -2.524 | -2.904 |
| 90 | 1 | 3.45140 | 7.317 | 7.647 |
| 90 | 2 | 1.61117 | 7.177 | 6.677 |
| 90 | 3 | 0.95431 | 7.167 | 6.747 |
| 60 | 1 | 0.77481 | -3.501 | -3.481 |
| 60 | 2 | -0.29716 | -2.521 | -4.461 |
| 60 | 3 | 0.47961 | -2.531 | -4.571 |

To 20 significant digits:

| `tau` | `rho_1` | `rho_2` | `rho_3` | `f_hat` | `f` | `r` |
|---|---|---|---|---|---|---|
| 240 | -0.092709701432514573337 | -0.11424575696332938083 | 0.077424548483935820626 | 0.74093818017618373293 | 1 | 1 |
| 180 | -0.046916964185936119115 | 0.090933751112762824493 | -0.034228921159829873200 | 1.0195757315339936644 | 1.0195757315339936644 | 1.0097404278001320396 |
| 120 | 0.032241167200307063529 | 0.023375014349432735570 | -0.027477377500369136556 | 1.0562776080987413251 | 1.0562776080987413251 | 1.0277536709244785398 |
| 90 | 0.075862928388760765339 | 0.034086991721894132916 | 0.018969279187419256306 | 1.2578383985961483091 | 1.2578383985961483091 | 1.1215339489271594533 |
| 60 | 0.037710170582569403265 | -0.017697614632921305340 | 0.022354418430052358183 | 1.0847339487594009122 | 1.0847339487594009122 | 1.0415056162879780228 |

**How the dependence sets `r`:**

- **At `tau` 240**, `f_hat` is below 1, a negative dependence. `f = 1` keeps the independent law there, as §3.2 derives.
- **At the other four `tau`**, `f` is `1.0196`, `1.0563`, `1.2578` and `1.0847`. That moves `c` up and `d` down: 180 goes from `591`/`560` to `592`/`559`, 120 from `537`/`511` to `538`/`510`, 90 from `459`/`436` to `463`/`432`, and 60 from `294`/`275` to `296`/`273` (§4's independence columns). Each critical value moves outward, away from the law's centre.
- **An independent check, recorded, not asserted:** a scratch probe recomputed every `rho_k` from TZ-15's file in exact rationals, sharing no code with the instrument. The largest gap to the instrument's 60-digit values is `4.19e-60`.

---

## 2. §3.3 — the set

| units considered | members | first unit | last unit | member-list SHA-256 |
|---|---|---|---|---|
| 2608 | 2400 | 1789670100 | 1790452200 | `3dde75b6d634a5b35fb3b2d654840781c0142de2bfbb64f601549bc3b5c02ab2` |

First member `1789670100` (2026-09-17T18:35:00Z), last `1790452200` (2026-09-26T19:50:00Z). Weekend members: 762.

| weekday | members |
|---|---|
| Fri | 531 |
| Mon | 264 |
| Sat | 492 |
| Sun | 270 |
| Thu | 322 |
| Tue | 261 |
| Wed | 260 |

Non-members, 208, by reason:

| reasons | units |
|---|---|
| disconnect | 207 |
| no chainlink at or before T0-300 | 1 |

Every non-member, by reason:

- disconnect: 1789670400, 1789670700, 1789671600, 1789671900, 1789674300, 1789681500, 1789688700, 1789695900, 1789700700, 1789701000, 1789707900, 1789708200, 1789715100, 1789715400, 1789722300, 1789722600, 1789729500, 1789729800, 1789736700, 1789737000, 1789743900, 1789744200, 1789751400, 1789758600, 1789765800, 1789767600, 1789767900, 1789768800, 1789776000, 1789783200, 1789790400, 1789797600, 1789803300, 1789803600, 1789807800, 1789815000, 1789822200, 1789829400, 1789836600, 1789839000, 1789839300, 1789845900, 1789846200, 1789853400, 1789855200, 1789862400, 1789869600, 1789876800, 1789884000, 1789891200, 1789895700, 1789902900, 1789910100, 1789916700, 1789917000, 1789923900, 1789924200, 1789931100, 1789931400, 1789938300, 1789938600, 1789945500, 1789945800, 1789949400, 1789956600, 1789963800, 1789971000, 1789978200, 1789985400, 1789986600, 1789986900, 1789993800, 1789994100, 1789998300, 1789998600, 1790005500, 1790005800, 1790012700, 1790013000, 1790019900, 1790020200, 1790023200, 1790023500, 1790024700, 1790025000, 1790031300, 1790031600, 1790035200, 1790038800, 1790039100, 1790046000, 1790046300, 1790046600, 1790053500, 1790053800, 1790058600, 1790059500, 1790059800, 1790061600, 1790063700, 1790070900, 1790078100, 1790083500, 1790083800, 1790084400, 1790091600, 1790091900, 1790098800, 1790099100, 1790106000, 1790106300, 1790113200, 1790113500, 1790117400, 1790124600, 1790127600, 1790129700, 1790130000, 1790130900, 1790131200, 1790134200, 1790134500, 1790134800, 1790135100, 1790142000, 1790142300, 1790149200, 1790149500, 1790156400, 1790158500, 1790160000, 1790160900, 1790168100, 1790174700, 1790181900, 1790189100, 1790196300, 1790198100, 1790200800, 1790201100, 1790206800, 1790210400, 1790210700, 1790217600, 1790217900, 1790224800, 1790225100, 1790232000, 1790232300, 1790239200, 1790239500, 1790241900, 1790242200, 1790249100, 1790249400, 1790256300, 1790256600, 1790263500, 1790263800, 1790265900, 1790273100, 1790276100, 1790283300, 1790290500, 1790292300, 1790299500, 1790306700, 1790310900, 1790311200, 1790317500, 1790317800, 1790324700, 1790325000, 1790331900, 1790332200, 1790339100, 1790339400, 1790346300, 1790346600, 1790353500, 1790353800, 1790360700, 1790361000, 1790367900, 1790368200, 1790370300, 1790370600, 1790377500, 1790377800, 1790384700, 1790385000, 1790390100, 1790390400, 1790391000, 1790398200, 1790405400, 1790407200, 1790414400, 1790421600, 1790428800, 1790429100, 1790436000, 1790436300, 1790443200, 1790443500, 1790450400, 1790450700
- no chainlink at or before T0-300: 1790188800

**§3.3's assertions hold in every run (V4 (c)):**

- `whole` is true.
- There are `2,400` members.
- The first unit considered is `1789670100`.
- Consecutive units differ by exactly `300` at all `2,607` steps.
- The walk's last unit is the 2,400th member, `1790452200`.
- The clock stood at least `1790456100` = `1790452200 + 3,900` at the step. The margin was `70,791` s in D1, `71,085` in D2, `71,372` in S1 and `71,651` in S2.

**Why the 2,400th member is not §0.8's 2,400th.** §0.8 counts complete manifests, and its 2,400th is `1790451900`. The set rule also requires the feed conditions of `tz06.qualification`. Unit `1790188800` is complete but fails its fifth condition, `no chainlink at or before T0-300`. So the set's 2,400th member is the next qualifying slot, `1790452200`, and §3.3's clock condition was asserted on it.

---

## 3. §3.4 to §3.6 — the label-free report, per `tau`

**§3.4 — the pricer at each checkpoint:**

| `tau` | admissible | weekday | weekend |
|---|---|---|---|
| 240 | 1483 | 1281 | 202 |
| 180 | 1504 | 1295 | 209 |
| 120 | 1492 | 1288 | 204 |
| 90 | 1517 | 1309 | 208 |
| 60 | 1515 | 1306 | 209 |

**§3.5 — the quotes at each admitted checkpoint:**

| `tau` | reads present | reads used | listed |
|---|---|---|---|
| 240 | 4800 | 4800 | 0 |
| 180 | 4800 | 4800 | 0 |
| 120 | 4800 | 4800 | 0 |
| 90 | 4800 | 4800 | 0 |
| 60 | 4800 | 4800 | 0 |

Listed, by reason:

| `tau` | reason | count |
|---|---|---|
| — | none listed | 0 |

**All `24,000` admitted reads were present and all `24,000` were used,** 2,400 members × 5 `tau` × 2 tokens. Not one was listed.

**§3.6 — eligibility, selection and the claim, before any label:**

| `tau` | admissible | eligible | selected | Up | Down | weekday | weekend | both edges positive | at or below 0.10 |
|---|---|---|---|---|---|---|---|---|---|
| 240 | 1483 | 1483 | 945 | 496 | 449 | 809 | 136 | 0 | 5 |
| 180 | 1504 | 1504 | 1038 | 530 | 508 | 882 | 156 | 0 | 63 |
| 120 | 1492 | 1492 | 1058 | 533 | 525 | 906 | 152 | 0 | 197 |
| 90 | 1517 | 1517 | 937 | 489 | 448 | 799 | 138 | 0 | 254 |
| 60 | 1515 | 1515 | 641 | 319 | 322 | 556 | 85 | 0 | 208 |

| `tau` | `n` | min `a` | 0.25 | median `a` | 0.75 | max `a` | mean `q - a` | mean `q - a - fee(a)` |
|---|---|---|---|---|---|---|---|---|
| 240 | 945 | 0.04 | 0.36 | 0.56 | 0.75 | 0.96 | 0.044637 | 0.030896 |
| 180 | 1038 | 0.01 | 0.26 | 0.5 | 0.84 | 0.99 | 0.043341 | 0.032156 |
| 120 | 1058 | 0.01 | 0.15 | 0.37 | 0.9 | 0.999 | 0.040358 | 0.031714 |
| 90 | 937 | 0.001 | 0.09 | 0.35 | 0.91 | 0.999 | 0.040400 | 0.032860 |
| 60 | 641 | 0.001 | 0.06 | 0.31 | 0.83 | 0.999 | 0.048134 | 0.040644 |

| `tau` | `q - a`: min | 0.25 | median | 0.75 | 0.90 | max |
|---|---|---|---|---|---|---|
| 240 | 0.005944 | 0.025376 | 0.038625 | 0.054325 | 0.075804 | 0.341054 |
| 180 | 0.002738 | 0.020515 | 0.033504 | 0.053177 | 0.081045 | 0.420750 |
| 120 | 0.000832 | 0.015872 | 0.028365 | 0.050951 | 0.082786 | 0.510794 |
| 90 | 0.000332 | 0.012096 | 0.027236 | 0.053819 | 0.084900 | 0.617359 |
| 60 | 0.000135 | 0.011878 | 0.029104 | 0.064678 | 0.110624 | 0.490565 |

Over the eligible checkpoints whose Up book is two-sided at the touch, `D = p - (bid_up + ask_up) / 2`:

| `tau` | books | min `D` | 0.25 | median | 0.75 | max | market more confident |
|---|---|---|---|---|---|---|---|
| 240 | 1483 | -0.351054 | -0.025907 | 0.002500 | 0.032126 | 0.352801 | 638 (0.4302) |
| 180 | 1501 | -0.430750 | -0.027223 | -0.000072 | 0.026788 | 0.443337 | 747 (0.4977) |
| 120 | 1375 | -0.488448 | -0.025512 | 0.000208 | 0.026245 | 0.515794 | 735 (0.5345) |
| 90 | 1188 | -0.499517 | -0.022053 | 0.001010 | 0.024435 | 0.622359 | 648 (0.5455) |
| 60 | 767 | -0.499974 | -0.027416 | -0.000154 | 0.023669 | 0.499520 | 417 (0.5437) |

- **P1 held:** at every `tau` the eligible count equals the admissible count, because every admissible checkpoint had at least one ask.
- **No checkpoint had both edges positive.**
- **The mean claimed edge after the fee** is `0.031` to `0.041` a share. It is §3.6's `Σ(q − a − fee(a)) / n`, what `p_t` says the chosen side is worth above its price.

---

## 4. §3.7 — the gate's constants, exact, on disk before any label

**`tz16a-constants.json` was written at 16:38:16Z in D1, 16:43:14Z in D2, 16:47:56Z in S1 and 16:52:36Z in S2.**

- Each scored run's label read followed its own write by one second: 16:47:57Z and 16:52:37Z (§5).
- The file is byte-identical in all four runs: 34,914 lines, 793,470 bytes, SHA-256 `d79c9f44957d923e828b9157952f1f7b2a01cf9e35deead91ebc44faa16493be`.
- It holds every selected member's `T0`, side, `a`, `q` and `fee(a)`, and §3.2's figures.

`alpha1 = beta1 = 0.002`; the look at the `r` of section 3.2:

| `tau` | `n` | `mu0` | `mu1` | `r` | `c` | `d` | `FP_E` | `FP_N` | `POWER_E` | `POWER_N` |
|---|---|---|---|---|---|---|---|---|---|---|
| 240 | 945 | 525.72 | 567.902433683917 | 1 | 566 | 528 | 0.001702137132 | 0.001631685735 | 0.571920 | 0.580551 |
| 180 | 1038 | 552.67 | 597.657602231728 | 1.0097404278001320396 | 592 | 559 | 0.001658386054 | 0.001792623709 | 0.685225 | 0.702155 |
| 120 | 1058 | 503.229 | 545.927577972221 | 1.0277536709244785398 | 538 | 510 | 0.001889366917 | 0.001525981843 | 0.764162 | 0.738129 |
| 90 | 937 | 428.471 | 466.325493108492 | 1.1215339489271594533 | 463 | 432 | 0.001482865309 | 0.001795019069 | 0.643712 | 0.656637 |
| 60 | 641 | 269.395 | 300.248976989127 | 1.0415056162879780228 | 296 | 273 | 0.001901737260 | 0.001631309114 | 0.711766 | 0.690706 |

`FP_E` sums to 0.008634492672 and `FP_N` to 0.008376619469 over the five `tau`.

Independence beside it, at `r = 1`, barred from every reading:

| `tau` | `c` | `d` | `FP_E` | `FP_N` | `POWER_E` | `POWER_N` | `tz15.crit` `s*` / `FP` |
|---|---|---|---|---|---|---|---|
| 240 | 566 | 528 | 0.001702137132 | 0.001631685735 | 0.571920 | 0.580551 | 566 / 0.001702137132 |
| 180 | 591 | 560 | 0.001658386054 | 0.001792623709 | 0.712503 | 0.728488 | 591 / 0.001658386054 |
| 120 | 537 | 511 | 0.001889366917 | 0.001525981843 | 0.789755 | 0.765726 | 537 / 0.001889366917 |
| 90 | 459 | 436 | 0.001482865309 | 0.001795019069 | 0.775562 | 0.788269 | 459 / 0.001482865309 |
| 60 | 294 | 275 | 0.001901737260 | 0.001631309114 | 0.786809 | 0.769956 | 294 / 0.001901737260 |

The second look's projection, `w + w[::2]` at `alpha2 = beta2 = 0.008` and the same `r`, barred from every reading:

| `tau` | coins | `c` | `d` | `FP_E` | `FP_N` | `POWER_E` | `POWER_N` |
|---|---|---|---|---|---|---|---|
| 240 | 1418 | 833 | 814 | 0.007299414989 | 0.007350830108 | 0.910837 | 0.913332 |
| 180 | 1557 | 869 | 856 | 0.007426844628 | 0.006778880043 | 0.960959 | 0.958725 |
| 120 | 1587 | 786 | 777 | 0.007072747713 | 0.006613765535 | 0.976541 | 0.974975 |
| 90 | 1406 | 674 | 660 | 0.006634950668 | 0.007541666690 | 0.939443 | 0.943687 |
| 60 | 962 | 430 | 420 | 0.007526807389 | 0.006417504423 | 0.964446 | 0.959543 |

Exact, per `tau`:

- `tau` 240: `r` = `1`; `FP_E` = `0.00170213713160056625910163243813095567039655765171302527338886`; `FP_N` = `0.001631685734694615821240826196880574159722358531144310508872`; `POWER_E` = `0.571920372074725632384781778978885030004533830294336119721187`; `POWER_N` = `0.580550561108921789752401844256881201279560773392839507672289`.
- `tau` 180: `r` = `1.00974042780013203963531654106012822765689129834789291209633`; `FP_E` = `0.00165838605401066308541442302544168971228123878231947457380540`; `FP_N` = `0.001792623709048277327860942604033713380806885563431034534280`; `POWER_E` = `0.685225387372448045154015942650350997331212718997453995994992`; `POWER_N` = `0.702155074819087915217425976301341280408208329025629608062565`.
- `tau` 120: `r` = `1.02775367092447853979986524705284618999809185484554100433916`; `FP_E` = `0.00188936691680744770666921738479406630141554252894181688127650`; `FP_N` = `0.001525981842674500637067099138143468469005834040582999015174`; `POWER_E` = `0.764161778054508407663595082551191601547765088434392567244235`; `POWER_N` = `0.738129448427879213622075797531056901557829055263907915865076`.
- `tau` 90: `r` = `1.12153394892715945334107623489942953244477295959725034224215`; `FP_E` = `0.00148286530937610585810741117195610648704106633841765119829472`; `FP_N` = `0.001795019069296722370955658558392981336666683323079875542070`; `POWER_E` = `0.643712464813069730686331508325454500595236118793395630255811`; `POWER_N` = `0.656636695961461364977748425465405385828517472176219106571321`.
- `tau` 60: `r` = `1.04150561628797802283456126098129350476554783778870317506575`; `FP_E` = `0.00190173726043769822040285231157977634378582342200149541846598`; `FP_N` = `0.001631309113761531227076003949363442203494789335145754473668`; `POWER_E` = `0.711765919365976906017912760841543057694104857267657120317600`; `POWER_N` = `0.690705604899489066423829763168630777091391275011325869379042`.

The alternative's first four power sums, `sum q^k`:

| `tau` | `sum q` | `sum q^2` | `sum q^3` | `sum q^4` |
|---|---|---|---|---|
| 240 | 567.902433683916709065 | 389.586073249713394816658036795 | 290.489341289786542459261291987 | 228.496684705598604973574606904 |
| 180 | 597.6576022317281542348 | 434.684982539584552846449176203 | 353.540338923903782803472517101 | 304.360588803733582145671182046 |
| 120 | 545.92757797222115388586 | 409.169528177902322058169336827 | 351.197639928839486104774793420 | 318.472695560617585381272715219 |
| 90 | 466.325493108492484387386 | 359.807467139352595641686676967 | 315.558026646797897692871809130 | 290.211566584040406923970335074 |
| 60 | 300.248976989126970216706 | 228.364282115028004002906611533 | 197.205694837400973241336866548 | 179.038224967047019563561680682 |

The null's weights as distinct prices with their counts — they fix `U0` exactly:

- `tau` 240, 945 coins, 89 distinct prices: 0.04 × 1, 0.07 × 2, 0.09 × 2, 0.11 × 1, 0.12 × 3, 0.13 × 5, 0.14 × 1, 0.15 × 3, 0.16 × 1, 0.17 × 8, 0.18 × 6, 0.19 × 8, 0.2 × 7, 0.21 × 14, 0.22 × 13, 0.23 × 14, 0.24 × 10, 0.25 × 10, 0.26 × 9, 0.27 × 13, 0.28 × 10, 0.29 × 8, 0.3 × 16, 0.31 × 16, 0.32 × 8, 0.33 × 16, 0.34 × 10, 0.35 × 14, 0.36 × 12, 0.37 × 11, 0.38 × 11, 0.39 × 11, 0.4 × 5, 0.41 × 16, 0.42 × 10, 0.43 × 11, 0.44 × 21, 0.45 × 10, 0.46 × 10, 0.47 × 14, 0.48 × 15, 0.49 × 9, 0.5 × 8, 0.51 × 9, 0.52 × 3, 0.53 × 16, 0.54 × 10, 0.55 × 20, 0.56 × 15, 0.57 × 15, 0.58 × 13, 0.59 × 6, 0.6 × 12, 0.61 × 8, 0.62 × 8, 0.63 × 9, 0.64 × 6, 0.65 × 12, 0.66 × 18, 0.67 × 10, 0.68 × 17, 0.69 × 14, 0.7 × 10, 0.71 × 13, 0.72 × 15, 0.73 × 18, 0.74 × 17, 0.75 × 18, 0.76 × 12, 0.77 × 15, 0.78 × 15, 0.79 × 11, 0.8 × 19, 0.81 × 15, 0.82 × 12, 0.83 × 17, 0.84 × 15, 0.85 × 13, 0.86 × 12, 0.87 × 11, 0.88 × 9, 0.89 × 16, 0.9 × 12, 0.91 × 7, 0.92 × 2, 0.93 × 8, 0.94 × 7, 0.95 × 1, 0.96 × 1
- `tau` 180, 1038 coins, 98 distinct prices: 0.01 × 2, 0.03 × 3, 0.04 × 8, 0.05 × 5, 0.06 × 11, 0.07 × 5, 0.08 × 8, 0.09 × 11, 0.1 × 10, 0.11 × 6, 0.12 × 10, 0.13 × 11, 0.14 × 13, 0.15 × 16, 0.16 × 16, 0.17 × 12, 0.18 × 14, 0.19 × 13, 0.2 × 11, 0.21 × 10, 0.22 × 18, 0.23 × 14, 0.24 × 12, 0.25 × 13, 0.26 × 8, 0.27 × 12, 0.28 × 7, 0.29 × 16, 0.3 × 9, 0.31 × 14, 0.32 × 14, 0.33 × 17, 0.34 × 11, 0.35 × 13, 0.36 × 7, 0.37 × 14, 0.38 × 10, 0.39 × 13, 0.4 × 11, 0.41 × 10, 0.42 × 14, 0.43 × 10, 0.44 × 10, 0.45 × 15, 0.46 × 8, 0.47 × 8, 0.48 × 7, 0.49 × 7, 0.5 × 10, 0.51 × 6, 0.52 × 6, 0.53 × 8, 0.54 × 7, 0.55 × 7, 0.56 × 6, 0.57 × 3, 0.58 × 10, 0.59 × 9, 0.6 × 7, 0.61 × 6, 0.62 × 7, 0.63 × 5, 0.64 × 6, 0.65 × 5, 0.66 × 3, 0.67 × 11, 0.68 × 9, 0.69 × 10, 0.7 × 6, 0.71 × 9, 0.72 × 3, 0.73 × 5, 0.74 × 10, 0.75 × 8, 0.76 × 13, 0.77 × 6, 0.78 × 9, 0.79 × 6, 0.8 × 10, 0.81 × 6, 0.82 × 12, 0.83 × 14, 0.84 × 20, 0.85 × 12, 0.86 × 11, 0.87 × 13, 0.88 × 16, 0.89 × 16, 0.9 × 19, 0.91 × 12, 0.92 × 18, 0.93 × 21, 0.94 × 18, 0.95 × 24, 0.96 × 18, 0.97 × 16, 0.98 × 18, 0.99 × 11
- `tau` 120, 1058 coins, 103 distinct prices: 0.01 × 11, 0.014 × 1, 0.02 × 10, 0.03 × 18, 0.04 × 32, 0.05 × 18, 0.06 × 29, 0.07 × 21, 0.08 × 20, 0.09 × 15, 0.1 × 22, 0.11 × 17, 0.12 × 15, 0.13 × 16, 0.14 × 16, 0.15 × 15, 0.16 × 15, 0.161 × 1, 0.17 × 16, 0.18 × 14, 0.19 × 12, 0.2 × 15, 0.21 × 15, 0.22 × 9, 0.23 × 18, 0.24 × 17, 0.25 × 10, 0.26 × 11, 0.27 × 10, 0.28 × 16, 0.29 × 15, 0.3 × 9, 0.31 × 9, 0.32 × 6, 0.33 × 16, 0.34 × 6, 0.35 × 6, 0.36 × 6, 0.37 × 5, 0.38 × 6, 0.39 × 7, 0.4 × 10, 0.41 × 10, 0.42 × 6, 0.43 × 7, 0.44 × 5, 0.45 × 5, 0.46 × 4, 0.47 × 4, 0.48 × 4, 0.49 × 1, 0.5 × 9, 0.51 × 10, 0.52 × 5, 0.53 × 3, 0.54 × 5, 0.55 × 4, 0.56 × 2, 0.57 × 3, 0.58 × 1, 0.59 × 4, 0.6 × 5, 0.61 × 6, 0.62 × 3, 0.63 × 4, 0.64 × 4, 0.65 × 6, 0.66 × 4, 0.67 × 5, 0.68 × 1, 0.69 × 5, 0.7 × 7, 0.71 × 5, 0.72 × 6, 0.73 × 3, 0.74 × 4, 0.75 × 7, 0.76 × 3, 0.77 × 7, 0.78 × 4, 0.79 × 2, 0.81 × 3, 0.82 × 1, 0.83 × 10, 0.84 × 7, 0.85 × 5, 0.86 × 3, 0.87 × 9, 0.88 × 8, 0.89 × 7, 0.9 × 11, 0.91 × 7, 0.92 × 14, 0.93 × 21, 0.94 × 19, 0.95 × 28, 0.96 × 35, 0.97 × 39, 0.98 × 44, 0.988 × 1, 0.99 × 45, 0.997 × 1, 0.999 × 1
- `tau` 90, 937 coins, 108 distinct prices: 0.001 × 2, 0.01 × 24, 0.02 × 21, 0.021 × 1, 0.03 × 28, 0.031 × 1, 0.04 × 35, 0.05 × 36, 0.06 × 27, 0.07 × 21, 0.08 × 26, 0.09 × 17, 0.1 × 15, 0.11 × 17, 0.12 × 18, 0.13 × 16, 0.14 × 18, 0.15 × 10, 0.16 × 12, 0.17 × 7, 0.18 × 7, 0.19 × 6, 0.2 × 7, 0.21 × 9, 0.22 × 4, 0.23 × 6, 0.24 × 6, 0.25 × 8, 0.26 × 3, 0.27 × 9, 0.28 × 7, 0.29 × 6, 0.3 × 7, 0.31 × 5, 0.32 × 10, 0.33 × 6, 0.34 × 8, 0.35 × 5, 0.36 × 9, 0.37 × 3, 0.38 × 7, 0.39 × 8, 0.4 × 4, 0.41 × 1, 0.42 × 4, 0.43 × 4, 0.44 × 8, 0.45 × 7, 0.46 × 5, 0.47 × 10, 0.48 × 8, 0.49 × 5, 0.5 × 3, 0.51 × 3, 0.52 × 1, 0.53 × 2, 0.54 × 3, 0.55 × 2, 0.56 × 1, 0.57 × 2, 0.58 × 3, 0.59 × 3, 0.6 × 3, 0.61 × 5, 0.62 × 5, 0.63 × 4, 0.64 × 6, 0.65 × 4, 0.66 × 2, 0.67 × 6, 0.68 × 1, 0.69 × 7, 0.7 × 2, 0.71 × 4, 0.74 × 3, 0.75 × 4, 0.76 × 3, 0.77 × 4, 0.78 × 2, 0.79 × 4, 0.8 × 3, 0.81 × 6, 0.82 × 10, 0.83 × 4, 0.84 × 3, 0.85 × 3, 0.86 × 6, 0.87 × 7, 0.88 × 3, 0.89 × 5, 0.9 × 4, 0.91 × 7, 0.92 × 6, 0.922 × 1, 0.93 × 7, 0.94 × 15, 0.95 × 20, 0.96 × 28, 0.965 × 1, 0.968 × 1, 0.97 × 37, 0.971 × 1, 0.98 × 46, 0.989 × 1, 0.99 × 61, 0.997 × 1, 0.998 × 1, 0.999 × 3
- `tau` 60, 641 coins, 108 distinct prices: 0.001 × 9, 0.006 × 1, 0.01 × 49, 0.019 × 1, 0.02 × 16, 0.03 × 20, 0.04 × 34, 0.05 × 17, 0.06 × 18, 0.07 × 16, 0.08 × 12, 0.09 × 4, 0.093 × 1, 0.1 × 10, 0.108 × 1, 0.11 × 5, 0.12 × 7, 0.13 × 10, 0.14 × 5, 0.15 × 10, 0.16 × 8, 0.17 × 2, 0.18 × 2, 0.19 × 6, 0.2 × 6, 0.21 × 5, 0.22 × 7, 0.23 × 3, 0.24 × 1, 0.25 × 5, 0.256 × 1, 0.26 × 3, 0.27 × 3, 0.28 × 5, 0.29 × 7, 0.3 × 6, 0.31 × 5, 0.32 × 5, 0.33 × 6, 0.34 × 7, 0.35 × 4, 0.36 × 3, 0.37 × 4, 0.38 × 9, 0.39 × 7, 0.4 × 3, 0.41 × 1, 0.411 × 1, 0.42 × 5, 0.43 × 3, 0.44 × 1, 0.45 × 1, 0.46 × 6, 0.47 × 1, 0.48 × 4, 0.49 × 3, 0.5 × 1, 0.51 × 4, 0.52 × 3, 0.53 × 2, 0.54 × 1, 0.55 × 3, 0.56 × 3, 0.58 × 1, 0.59 × 4, 0.6 × 4, 0.61 × 4, 0.62 × 2, 0.63 × 2, 0.64 × 2, 0.65 × 3, 0.66 × 1, 0.67 × 4, 0.68 × 2, 0.69 × 2, 0.7 × 3, 0.71 × 1, 0.72 × 4, 0.73 × 3, 0.74 × 3, 0.75 × 2, 0.76 × 4, 0.77 × 4, 0.78 × 3, 0.79 × 4, 0.8 × 4, 0.81 × 1, 0.83 × 2, 0.84 × 3, 0.85 × 3, 0.86 × 5, 0.87 × 2, 0.88 × 3, 0.89 × 9, 0.9 × 7, 0.91 × 4, 0.92 × 3, 0.93 × 5, 0.94 × 6, 0.943 × 1, 0.95 × 12, 0.96 × 16, 0.97 × 24, 0.98 × 27, 0.987 × 1, 0.99 × 26, 0.997 × 2, 0.999 × 1

- **V4 (d) holds at 5 of 5 `tau`.** At `r = 1`, `c` and `FP_E` equal the first two values `tz15.crit([a ...], D("0.002"))` returns: the last column of the independence table.
- **An independent check, recorded, not asserted:** a scratch probe re-derived `c`, `d`, `FP_E`, `FP_N` and both powers in `float64` from this file alone. It shares no code with the instrument. `c` and `d` agree at 5 of 5 `tau` each, `FP_E` to `6e-15` relative and `FP_N` to `1e-12` relative, and both powers to six decimals.

---

## 5. §3.8 — the labels, read once per scored run (V5)

**`P_push` beside each label-read instant.** `git push` of `5076b43` exited `0` at `1790527408`, 2026-09-27T16:43:28Z (§11).

| run | label read started | after `P_push` | `HEAD` | members read | member-list SHA-256 |
|---|---|---|---|---|---|
| S1 | `1790527677053053525` ns, 16:47:57Z | 269.1 s | `5076b43` | 1,618 | `ab75a1b02ad1c6f304da70e7139e0b5c3dafc8cd0bd2cea080e82afa3c9239c2` |
| S2 | `1790527957451640385` ns, 16:52:37Z | 549.5 s | `5076b43` | 1,618 | `ab75a1b02ad1c6f304da70e7139e0b5c3dafc8cd0bd2cea080e82afa3c9239c2` |

**The mechanics of each read:**

- Before each read, the instrument asserted that `origin/tz-16a-phase2-decisive-gate` is among the branches `git branch -r --contains HEAD` prints. It was the only one.
- `E`, the union over `ADMITTED` of the eligible members, is `1,618` members. The instrument asserted before the read that every selected member is in it.
- `tz10b.m2_labels(sorted(E))` returned 1,618 labels, `821` of them `Up`. It opened exactly 1,618 settled documents at step 12 (V2).

**The ledger, `/root/tz16a-work/label-ledger.jsonl`, whole:**

```
{"head": "5076b4305c7800fc7eed0cd3fe05d9577d1b6cf7", "member_list_sha256": "ab75a1b02ad1c6f304da70e7139e0b5c3dafc8cd0bd2cea080e82afa3c9239c2", "members": 1618, "utc": "2026-09-27T16:47:57Z"}
{"head": "5076b4305c7800fc7eed0cd3fe05d9577d1b6cf7", "member_list_sha256": "ab75a1b02ad1c6f304da70e7139e0b5c3dafc8cd0bd2cea080e82afa3c9239c2", "members": 1618, "utc": "2026-09-27T16:52:37Z"}
```

**Two lines, one per scored run, both of `5076b4305c7800fc7eed0cd3fe05d9577d1b6cf7`, the pushed commit.** No line of any other commit exists. D1 and D2 read no label, so neither wrote a ledger line.

---

## 6. §3.9 and §4 — the observed statistic, the readings, influence and diagnostics

§4.1, in its order:

| condition | reading |
|---|---|
| `n = 0` | UNDECIDABLE |
| `S >= c` | EDGE, whatever the powers are |
| `S <= d` | NO EDGE, whatever the powers are |
| otherwise | UNDECIDABLE |

**The observed statistic and the reading, per `tau`:**

| `tau` | `n` | `S` | `c` | `d` | `sum a` | win rate | mean `a` | mean `q` | `T` | `T_fee` | row | **reading** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 240 | 945 | 538 | 566 | 528 | 525.72 | 0.569312 | 0.556317 | 0.600955 | 0.012995 | -0.000747 | `otherwise` | **UNDECIDABLE** |
| 180 | 1038 | 547 | 592 | 559 | 552.67 | 0.526975 | 0.532437 | 0.575778 | -0.005462 | -0.016648 | `S <= d` | **NO EDGE** |
| 120 | 1058 | 506 | 538 | 510 | 503.229 | 0.478261 | 0.475642 | 0.516000 | 0.002619 | -0.006025 | `S <= d` | **NO EDGE** |
| 90 | 937 | 418 | 463 | 432 | 428.471 | 0.446105 | 0.457280 | 0.497679 | -0.011175 | -0.018714 | `S <= d` | **NO EDGE** |
| 60 | 641 | 256 | 296 | 273 | 269.395 | 0.399376 | 0.420273 | 0.468407 | -0.020897 | -0.028387 | `S <= d` | **NO EDGE** |

**Error rates of this look, exact under the model each test scores:** `FP_E` sums to 0.008634492672 and `FP_N` to 0.008376619469 over the five `tau`.

**The verdict.** NO EDGE, closed: 180, 120, 90, 60. UNDECIDABLE, to section 4.2's second look: 240. No tau reads EDGE.

**Which TZ must follow:** section 4.2's second look at tau 240.

**`n` is never 0,** so the first row gives nothing. **`S >= c` holds at no `tau`**, so no EDGE and no claim-rejected flag.

**`S <= d` holds at 180, 120, 90 and 60:**

- The chosen side won `0.527`, `0.478`, `0.446` and `0.399` of the time.
- The pricer claimed `0.576`, `0.516`, `0.498` and `0.468`.
- The mean ask was `0.532`, `0.476`, `0.457` and `0.420`.

**At 240 neither tail is reached.** The side won `0.569` of the time against a mean ask of `0.556` and a claim of `0.601`. `S = 538` is 28 short of `c` and 10 above `d`.

**Where the side won against its price.**

- **Gross of the fee,** it won more often than its price implied at 240 and at 120: `T` is `+0.012995` and `+0.002619`.
- **After the fee,** it lost at every `tau`: `T_fee` runs from `−0.000747` to `−0.028387`.

**Power, stated before any label and deciding nothing** (§3.7):

| `tau` | this look's `POWER_E` | this look's `POWER_N` | second look's projection, `POWER_E` / `POWER_N` |
|---|---|---|---|
| 240 | 0.571920 | 0.580551 | 0.910837 / 0.913332 |
| 180 | 0.685225 | 0.702155 | 0.960959 / 0.958725 |
| 120 | 0.764162 | 0.738129 | 0.976541 / 0.974975 |
| 90 | 0.643712 | 0.656637 | 0.939443 / 0.943687 |
| 60 | 0.711766 | 0.690706 | 0.964446 / 0.959543 |

**Influence — recorded, not a reading:**

| `tau` | removed `T0` | side | `a` | `n - 1` | `S` | `c` | `d` | `FP_E` | `FP_N` | reading |
|---|---|---|---|---|---|---|---|---|---|---|
| 240 | 1790087700 | Down | 0.94 | 944 | 538 | 565 | 527 | 0.001724214994 | 0.001621093835 | UNDECIDABLE |
| 180 | 1790268000 | Up | 0.99 | 1037 | 547 | 591 | 558 | 0.001662101518 | 0.001789427602 | NO EDGE |
| 120 | 1789775700 | Up | 0.98 | 1057 | 506 | 537 | 509 | 0.001898608356 | 0.001518078155 | NO EDGE |
| 90 | 1790355900 | Up | 0.02 | 936 | 417 | 463 | 432 | 0.001471943002 | 0.001813507740 | NO EDGE |
| 60 | 1790238600 | Down | 0.02 | 640 | 255 | 296 | 273 | 0.001884675247 | 0.001657497626 | NO EDGE |

**Removing the single most influential member moves no reading** (map §7 item 27). At 120, the reading closest to its boundary, `S` stays `506` and `d` falls to `509`: still NO EDGE.

**Diagnostics — each barred from every reading:**

| `tau` | two-sided books | mean label | mean mid | mean `p_t` | Brier mid | Brier `p_t` |
|---|---|---|---|---|---|---|
| 240 | 1483 | 0.509777 | 0.499582 | 0.502537 | 0.208730 | 0.210339 |
| 180 | 1501 | 0.504997 | 0.511399 | 0.511242 | 0.162696 | 0.164387 |
| 120 | 1375 | 0.503273 | 0.509596 | 0.509839 | 0.129979 | 0.130224 |
| 90 | 1188 | 0.501684 | 0.495812 | 0.498783 | 0.115733 | 0.116381 |
| 60 | 767 | 0.504563 | 0.495538 | 0.496944 | 0.108815 | 0.114801 |

The dependence on this look's own selected residuals, in `T0` order:

| `tau` | `n` | `rho_1` | `rho_2` | `rho_3` | `f_hat` | `f` |
|---|---|---|---|---|---|---|
| 240 | 945 | 0.0362221 | -0.0201322 | -0.0385151 | 0.955150 | 1 |
| 180 | 1038 | 0.0339974 | 0.0213864 | -0.0432686 | 1.02423 | 1.02423 |
| 120 | 1058 | 0.0269063 | 0.00565371 | -0.0230542 | 1.01901 | 1.01901 |
| 90 | 937 | 0.00821318 | 0.0151464 | 0.000233706 | 1.04719 | 1.04719 |
| 60 | 641 | -0.0119931 | -0.0744425 | -0.0708955 | 0.685338 | 1 |

**What the diagnostics show:**

- **The market's mid beats `p_t` on the Brier score at 5 of 5 `tau`,** over the eligible two-sided Up books. That is the same pattern TZ-15 found on its set.
- **The dependence on this look's own residuals** gives `f` = `1`, `1.02423`, `1.01901`, `1.04719` and `1`. That is at or below the `f` §3.2 carried from TZ-15's set at 240, 120, 90 and 60.
- **At 180 it is above:** `1.02423` against `1.0195757315339936644`.

These figures are recorded after the fact, and no reading rests on them (§3.9).

---

## 7. §3.10 and §4.3 — the interlock

**The interlock's counts, its test and its power:**

| group | units | failures |
|---|---|---|
| exposed | 297 | 0 |
| control | 2311 | 0 |
| no manifest, apart | 0 | — |
| considered | 2608 | — |

| era | exposed | exposed failures | control | control failures | no manifest |
|---|---|---|---|---|---|
| `T0 < 1790185200` | 0 | 0 | 1717 | 0 | 0 |
| `T0 >= 1790185200` | 297 | 0 | 594 | 0 | 0 |

Fully loaded exposed units: 297 of 297.
Failures, every `T0`: none.
Units with no manifest: none.

`p_I` = 1 (1.0000000000). **Reading: HOLD.**

| `q` | `k*` | P(Bin(`m_E`, `q`) >= `k*`) |
|---|---|---|
| 1/100 | 3 | 0.57115842049062728293 |
| 1/50 | 3 | 0.93713036773227105893 |
| 1/20 | 3 | 0.99996650145078868219 |

The chain book's `runtime.jsonl`, every record (3; 0 unparsed):

| event | pid | `wall_ns` |
|---|---|---|
| start | 2608993 | 1790117616052072857 |
| stop | 2608993 | 1790145840007723380 |
| start | 2699889 | 1790185190022755903 |

The start record of pid 2699889 at `wall_ns` 1790185190022755903: found. A `stop` record of that pid after it: no.

**How the units split:**

- **Considered:** the 2,608 units §3.3 considered, all with a manifest.
- **Exposed:** 297. These are the units with `T0 >= 1790185200`, `T0 mod 900 = 600` and the window `T0 − 600`'s `window.json` present, every one of them fully loaded.
- **Control:** 2,311. That is every other unit: 1,717 before the service started, TZ-18's refused windows among them, and 594 after it.

**Failures.** `quotes_complete` is JSON `true` at 2,608 of 2,608. So `f_E = f_C = 0` and `p_I = 1` exactly, and **§4.3 reads HOLD**.

**Power.** `k*` is `3`. A disturbance that breaks 1% of exposed intervals against a control at its base rate of 0 would have read FIRE with probability `0.5712`, 2% with `0.9371`, and 5% with `0.99997`.

**The service's record.** The chain book's `runtime.jsonl` holds the start record of pid `2699889` at `1790185190022755903`, and no `stop` record after it. **Block K-18a was not run.** The service runs on as pid `2699889` (closing read, §12).

---

## 8. §3.11 — the five pre-registered predictions

| # | prediction | observed | verdict |
|---|---|---|---|
| P1 | the eligible count equals the admissible count at every tau | 240: 1483 of 1483, 180: 1504 of 1504, 120: 1492 of 1492, 90: 1517 of 1517, 60: 1515 of 1515 | **held** |
| P2 | no tau reads EDGE | 240: UNDECIDABLE, 180: NO EDGE, 120: NO EDGE, 90: NO EDGE, 60: NO EDGE | **held** |
| P3 | NO EDGE at tau 240, 180, 120 and 60, and not at 90 | 240: UNDECIDABLE, 180: NO EDGE, 120: NO EDGE, 90: NO EDGE, 60: NO EDGE | **refuted** |
| P4 | f < 1.3 at all five tau | 240: 1, 180: 1.01958, 120: 1.05628, 90: 1.25784, 60: 1.08473 | **held** |
| P5 | the interlock reads HOLD | HOLD, f_E = 0 of m_E = 297, f_C = 0 of m_C = 2311, p_I = 1 | **held** |

**P3 is refuted, on two rows of five.**

- **The prediction:** NO EDGE at 240, 180, 120 and 60, and not at 90.
- **The reading:** NO EDGE at 180, 120, 90 and 60, and UNDECIDABLE at 240.

**Which part of its basis failed** (§3.11):

- **The basis held at 180, 120 and 60.** It said that on TZ-15's set the outcomes fell below the pricer's claim past its lower tail at 240, 120 and 60, and to that boundary at 180. It also said that doubling the set would carry a persistent shortfall past `0.002`.
- **At 240 the shortfall did not persist far enough to be rejected.** The side won `538` against the pricer's expected `567.902433683917` and the ask's `525.72`. `538` is 10 above `d = 528`, so NO EDGE was not read.
- **At 90, where TZ-15's set sat near `0.12`, this look's outcomes reached the lower tail.** `S = 418` is 14 below `d = 432`, and that `d` had already been moved outward by the variance factor `1.2578`.

P1, P2, P4 and P5 held. P4's largest `f` is `1.2578` at 90, against its `1.3`.

---

## 9. Implementation

**One new file, `research/tz16a-phase2-decisive-gate.py`,** on branch `tz-16a-phase2-decisive-gate` at commit `5076b4305c7800fc7eed0cd3fe05d9577d1b6cf7`:

- 2,198 lines, 111,192 bytes, SHA-256 `3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125`.
- One commit, and no fix after it.
- Pull request #20, open and unmerged.

**What it loads.**

- It loads `tz15-phase2-gate.py` once, through `_load`, and takes `tz14`, `tz12`, `tz11a`, `tz10b`, `tz07b`, `tz06`, `pfair`, `config`, `D` and `load_manifests` from that module object. It then imports `analyze` and `manifest` by name.
- **The load's side effects, as §5.1 names them:** `tz15` and `tz14` each write the three thread-count variables and install an audit hook. This instrument reads neither hook's list.
- **Its own hook** records the absolute path, the mode and the step for every open under `/var/lib/btc-recorder/` and `/var/lib/btc-chainbook/`. V2 and V9 are asserted from it.

**What it calls, and what it writes once.**

- From `tz15` it calls `pb_upper`, `crit`, `select` and `label_free`, and reads `ADMITTED`, `ROW_KEYS` and `PFAIR_PROBABILITY`.
- It writes §5.1's functions once each: `v1_gates`, `locate`, `residual_dependence` (total), `dependence`, `up`, `low`, `critical_upper`, `critical_lower`, `look_constants`, `read_look`, `the_set`, `the_rows`, `the_quotes`, `the_trades`, `labels`, `observed`, `influence`, `diagnostics`, `interlock`, `fisher_upper`, `interlock_reading`, `interlock_power`, `v2_static`, `v6`, `selftests`, `build`, `tables`, `csv_text` and `main`.
- `fisher_upper`, `interlock_reading` and `interlock_power` are pure, and self-test items 9 and 10 call them with literals.

**How a run is ordered and made total.**

- `build` asserts §5.1's order step by step: `0 … 3` with `--selftest`, `0 … 11` without `--score`, and `0 … 10, 12, 13, 14` with it.
- Everything computed after step 12 is total: a ratio at `n = 0`, influence at `n < 2`, and `residual_dependence` at `n < 4` or `v = 0` each return undefined with a reason. The formatting helpers catch every arithmetic error and print the value instead.
- A scratch edge-case harness exercised each of those paths before the push (§13 item 1).

**Cost against §6's table** — S1's step marks from `tz16a-run.json`, in seconds, each a difference of two marks recorded to the millisecond:

| step | §6's basis | measured in S1 |
|---|---|---|
| gates, self-tests, `v6`, `v2_static` (steps 0 to 3), with the module load | ~15 | 0.80 |
| TZ-15's files and `f` (step 4) | ~2 | 0.45 |
| the set (step 5) | ~54 | 40.85 |
| the rows (step 6) | ~187 | 187.04 |
| the quotes (step 7) | ~9 | 8.24 |
| selection and the constants, with V4 (d) and the projection (steps 8 and 9) | ~72 for all recursions | 8.18 |
| the interlock (step 10) | ~2 | 0.44 |
| labels, statistic, influence, diagnostics, files, host read 3 (steps 12 to 14) | ~10 | 5.03 |
| **one run** | **~351** | **251.03** |
| **the session's four runs, D1 + D2 + S1 + S2** | **~1,404** against `3,600` | **1,002.2** |

**Both fail-fast bounds held in every run:**

- **Item 12's timing:** `t12` was `0.3363` s in S1, projecting `64.2` s of recursion against the `400` s bound.
- **Elapsed after step 6:** `228.8` s in S1 against the `450` s bound. The other runs read `228.3`, `232.1` and `228.3` s.

---

## 10. Validation — V1 to V13

"Asserted" means an `assert` or a `SystemExit` in the instrument, at the step named. Everything else is recorded, not asserted.

- **V1 — gates, asserted at step 0.** It holds in every run.
  - 6 of 6 anchors, 4 of 4 re-derived; 24 of 24 `frozen`, 2 `tracked`, 1 `reported` (§0.1).
  - H1 to H3 hold and H4 is printed (§0.2). R-READY's line (§0.8), §0.6's refs, the trees and the forensic count of `1,046` hold (§0.2).
  - The interpreter and `numpy` versions (§0.3) and every free-space read with its bound (§0.4).
- **V2 — isolation, asserted two ways.**
  - **Static, step 3:**
    - 2,109 non-docstring string constants were scanned, and 0 carry any of `tz14.BANNED_SUBSTRINGS`.
    - 1,240 calls were scanned. None calls the twelve `pfair` entry points, and none calls any of §5.1's eleven names.
    - `tz10b.m2_labels` has exactly 1 call site.
    - There are 0 imports of `urllib`, `http`, `socket`, `ssl`, `requests` or `websockets`.
    - `subprocess.run` has exactly 1 call site. Its argument list begins with the literal `"git"`, and it has no `shell` keyword.
  - **Run time, from the instrument's hook:**
    - The settled document was opened `2,608` times at step 5, equal to the units considered that have a manifest and that file.
    - It was opened `0` times at every other step before 12.
    - It was opened `1,618` times at step 12, equal to the members handed to `tz10b.m2_labels`. Each count is asserted per step in S1 and S2.
    - Every pricer row carries exactly `tz15.ROW_KEYS` with `label is None`, over all 12,000 rows, asserted at steps 8 and 9.
- **V3 — determinism, BLOCKING by `cmp` after S2.**
  - **5 of 5 compared files are byte-identical between S1 and S2.**
  - **`tz16a-constants.json` is byte-identical to both runs without `--score` on that commit**, D1 and D2: 2 of 2.
  - `tz16a-run.json` holds instants and timings and is not compared. Its hashes are `8b41cd25…` for S1 and `5de9b937…` for S2.

```
2026-09-27T16:53:00Z
cmp run-s1/tz16a-constants.json run-s2/tz16a-constants.json exit=0
cmp run-s1/tz16a-readings.json run-s2/tz16a-readings.json exit=0
cmp run-s1/tz16a-tables.md run-s2/tz16a-tables.md exit=0
cmp run-s1/tz16a-observations.csv run-s2/tz16a-observations.csv exit=0
cmp run-s1/tz16a-disclosure.md run-s2/tz16a-disclosure.md exit=0
cmp run-s1/tz16a-constants.json run-d1/tz16a-constants.json exit=0
cmp run-s1/tz16a-constants.json run-d2/tz16a-constants.json exit=0
d79c9f44957d923e828b9157952f1f7b2a01cf9e35deead91ebc44faa16493be  run-s1/tz16a-constants.json
81e276922890a3fcd4c91f3e6e5bc30412f6747db1c6e2ccf4b368da46dc915a  run-s1/tz16a-disclosure.md
d22c90df32a6241c405fba00e5542b463d3623e31f87539ab37a1261b149f77f  run-s1/tz16a-observations.csv
b2b554920754dd95b1c0a771cef7c49d7bda917d54eb62c3d7498845f1faaa5c  run-s1/tz16a-readings.json
8b41cd251a25edc98293d523428bb9439dd67b7686b35c473e754bfde8ae5f04  run-s1/tz16a-run.json
47294fbe42ffe67862a1b8beecffceca0a117c27a06a96029c9ee15ae47f2e24  run-s1/tz16a-tables.md
d79c9f44957d923e828b9157952f1f7b2a01cf9e35deead91ebc44faa16493be  run-s2/tz16a-constants.json
81e276922890a3fcd4c91f3e6e5bc30412f6747db1c6e2ccf4b368da46dc915a  run-s2/tz16a-disclosure.md
d22c90df32a6241c405fba00e5542b463d3623e31f87539ab37a1261b149f77f  run-s2/tz16a-observations.csv
b2b554920754dd95b1c0a771cef7c49d7bda917d54eb62c3d7498845f1faaa5c  run-s2/tz16a-readings.json
5de9b93781af36b8fd790ed9b7cb6814745a78efed0f16f848fa1ea25e0932ee  run-s2/tz16a-run.json
47294fbe42ffe67862a1b8beecffceca0a117c27a06a96029c9ee15ae47f2e24  run-s2/tz16a-tables.md
d79c9f44957d923e828b9157952f1f7b2a01cf9e35deead91ebc44faa16493be  run-d1/tz16a-constants.json
d79c9f44957d923e828b9157952f1f7b2a01cf9e35deead91ebc44faa16493be  run-d2/tz16a-constants.json
  34914  793470 run-s1/tz16a-constants.json
   2700  338934 run-s1/tz16a-disclosure.md
  12001 1951410 run-s1/tz16a-observations.csv
   2642   70117 run-s1/tz16a-readings.json
   1991   44401 run-s1/tz16a-run.json
    322   26001 run-s1/tz16a-tables.md
  54570 3224333 total
```

- **V4 — inputs, asserted.**
  - **(a) step 4:** 35 of 35.
  - **(b) step 4:** 15 of 15 (§1).
  - **(c) step 5:** §3.3's assertions (§2).
  - **(d) step 9:** 5 of 5 `tau` (§4).
  - TZ-15's two files were located by hash: 2 and 5 copies among 182 regular files.
- **V5 — the push precedes the label read, asserted at step 12.** `HEAD` `5076b43` is contained in `origin/tz-16a-phase2-decisive-gate` in both scored runs. `P_push` stands beside both label-read instants, and the ledger is printed whole, 2 lines, both of `5076b43` (§5).
- **V6 — the diff, asserted at step 3.**
  - Merge base `0c2d3f0`, head `5076b43`, `git status --porcelain` empty for the two scoped paths.
  - `git diff --name-only` names exactly `research/tz16a-phase2-decisive-gate.py`. In a scored run this is asserted as equality, and in the others as a subset.
  - 0 `global`, 0 `nonlocal`, 0 attribute stores and 0 environment writes in the file's own tree.
  - The replaced-line list is empty: the path does not exist at the merge base.
- **V7 — the self-tests, asserted at step 2.** 11 of 11 items, **82** assertions, distributed `14, 5, 4, 6, 6, 6, 19, 8, 8, 2, 4`. Item 12's time is above. S1's output, verbatim:

```
item 1: up and low at s = -1 ... 5 over four coins, against the sixteen outcomes — 14 assertions
item 2: twenty fair coins give c = 17, FP_E = 0.00128841400146484375; tz15.crit gives 17 and 0.00128841400146484375 — 5 assertions
item 3: at r = 1.1 the same coins give c = 18, FP_E = 0.00128841400146484375 — 4 assertions
item 4: twenty coins at 0.8 give d = 9 at r = 1 and d = 8 at r = 1.1, FP_N = 0.00056341369766019072 both — 6 assertions
item 5: three coins at 0.9 give c = 4, FP_E = 0; three at 0.5 give d = -1, FP_N = 0 — 6 assertions
item 6: c = 17, d = 9, POWER_E = 0.41144886195656851456, POWER_N = 0.41190147399902343750 — 6 assertions
item 7: three residual series against exact rationals and the two undefined cases, 'n < 4' and 'v = 0' — 19 assertions
item 8: six readings and two claim-rejected flags — 8 assertions
item 9: four Fisher tails, 6/203, 2/261, 51/203 and 1, and their readings HOLD, FIRE, HOLD, HOLD — 8 assertions
item 10: k* = 4 and the power at q = 1/2 is 53/64 — 2 assertions
item 11: the guard passes two clean rows and raises on a label, on Y and on r — 4 assertions
item 12: one recursion over 1200 weights took 0.3363 s; the run projects 64.2 s of recursion against the 400 s bound
V7: 11 of 11 items, 82 assertions, per item [14, 5, 4, 6, 6, 6, 19, 8, 8, 2, 4]
```

- **V8 — the frozen files, asserted at step 0 and at the run's last step, 14 with `--score` and 11 without.** `research/pfair.py` `729f0bcdbee3…`, `research/tz14-quote-inventory.py` `978ee4ff9927…` and `research/tz15-phase2-gate.py` `66ac0ae0fdd2…` equal map §0. That held at step 0 in every run, and at the last step of D1, D2, S1 and S2. A `--selftest` run stops at step 3 and has no last-step half.
- **V9 — the captures are untouched, asserted at the last step.** In S1:
  - The recorder pid is `[228592]` at host reads 1 and 3, and its start record's sha and `recv_ns` `1789206785264516934` are unchanged.
  - The directory count reads `4980` at all three reads.
  - The read-set hash `b918ee7f41faa029…`, over 21,600 files, is unchanged between reads 2 and 3.
  - **29,329** opens, every one in mode `r`: `chainlink.jsonl.gz` 10,016, `gamma.json` 2,400, `manifest.json` 4,978, `quotes.jsonl.gz` 2,400, settled documents 4,226, `runtime.jsonl` 4, `twap60.jsonl.gz` 5,008 and `window.json` 297.
    - Of the four `runtime.jsonl` opens, three are the recorder's through host reads 1 to 3, and one is the chain book's.
    - **0** opens can write.
    - **0** files other than `manifest.json` were opened in an interval directory past the last member, `1790452200`.
    - **0** chain book files other than `window.json` and `runtime.jsonl` were opened.
  - Everything the instrument can write is its `--out` directory and `/root/tz16a-work/label-ledger.jsonl`. S2 reads the same, with 4,981 directories.
- **V10 — the fingerprint table** (§0.1), with the new file beside it.
- **V11 — disclosure.**
  - `tz16a-disclosure.md` lists every one of the 2,608 units considered in ascending `T0`, with UTC, weekday, reasons, the manifest's `quotes_complete` and the interlock group.
  - Per `tau` it gives the eligible and the selected lists, with counts and `tz07b.member_list_sha`. The hashes are below.
  - The listed reads of §3.5 are none.
  - `tz16a-observations.csv` has **12,000 rows and a header** (12,001 lines), TZ-15's eighteen columns in TZ-15's order. The row count is asserted at step 8.

| `tau` | eligible | its SHA-256 | selected | its SHA-256 |
|---|---|---|---|---|
| 240 | 1,483 | `5fc5b94e5cb5d391a5c46308268fe2c99a5d10ddd5edb22e3a1e0d7860e49484` | 945 | `2c1c39aec57a5730bc6fe0a79ca189e74994344869c7713a8f7bab43ddc449cb` |
| 180 | 1,504 | `bd85f46bd949470235309766c405843bcf93fa0850dcff5c436d85d7d248e1bf` | 1,038 | `8f7a2652e603f6f25f55d7f5d9da07fd32bdedeb0963202a19faa895f517ac28` |
| 120 | 1,492 | `be1452c5dd788c526d196418f2ba96edbdbeaba9a43833474948d8aca394d22e` | 1,058 | `a92bdd9bb1fba4a2dade286d1e7e69cbcd1029500143a87f8b12ed0e9d163d4a` |
| 90 | 1,517 | `9bc6eea1f2cfe430683f5b34d8b7a2a004ebf5f3d793040267d693b330ad5039` | 937 | `82bf5a0a74ce10a331c729e126f12bb6c41cf01c83ccd5440f95209091e44b9b` |
| 60 | 1,515 | `6603450b3c5e54d5d629ec334ca0821ac90c34a908267571b38c0f1f1510328f` | 641 | `f8d801138d94d48b2aba2eb37b2b12ceec56c3a189bb97cdf41639a7795dc71c` |

- **V12 — influence, diagnostics and predictions, recorded** (§6, §8).
- **V13 — the interlock, asserted at step 10.**
  - `m_E + m_C` plus the units with no manifest is `297 + 2,311 + 0 = 2,608`, the units considered.
  - `f_E = 0 <= 297` and `f_C = 0 <= 2,311`.
  - `p_I = 1` exactly, as a `Fraction`.
  - The reading is HOLD, with its power (§7).
  - Run K was not needed.

The output files, S1's run, with S2's identical except `tz16a-run.json` (V3):

| file | lines | bytes | SHA-256 |
|---|---|---|---|
| `tz16a-constants.json` | 34,914 | 793,470 | `d79c9f44957d923e828b9157952f1f7b2a01cf9e35deead91ebc44faa16493be` |
| `tz16a-readings.json` | 2,642 | 70,117 | `b2b554920754dd95b1c0a771cef7c49d7bda917d54eb62c3d7498845f1faaa5c` |
| `tz16a-tables.md` | 322 | 26,001 | `47294fbe42ffe67862a1b8beecffceca0a117c27a06a96029c9ee15ae47f2e24` |
| `tz16a-observations.csv` | 12,001 | 1,951,410 | `d22c90df32a6241c405fba00e5542b463d3623e31f87539ab37a1261b149f77f` |
| `tz16a-disclosure.md` | 2,700 | 338,934 | `81e276922890a3fcd4c91f3e6e5bc30412f6747db1c6e2ccf4b368da46dc915a` |
| `tz16a-run.json` | 1,991 | 44,401 | `8b41cd251a25edc98293d523428bb9439dd67b7686b35c473e754bfde8ae5f04` |

---

## 11. Publication

- **Branch:** `tz-16a-phase2-decisive-gate` on `origin` at `5076b4305c7800fc7eed0cd3fe05d9577d1b6cf7`.
- **Pull request:** [#20](https://github.com/seahomebatumi-ai/btc-5m-twap/pull/20), open and not merged.
- **No Release,** and no dataset, archive or binary in git history. The run outputs stay on the host in `/root/tz16a-work/run-*`.

The push, verbatim:

```
5076b4305c7800fc7eed0cd3fe05d9577d1b6cf7
remote: 
remote: Create a pull request for 'tz-16a-phase2-decisive-gate' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-16a-phase2-decisive-gate        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-16a-phase2-decisive-gate -> tz-16a-phase2-decisive-gate
branch 'tz-16a-phase2-decisive-gate' set up to track 'origin/tz-16a-phase2-decisive-gate'.
push exit=0
P_push 1790527408 2026-09-27T16:43:28Z
5076b4305c7800fc7eed0cd3fe05d9577d1b6cf7	refs/heads/tz-16a-phase2-decisive-gate
  origin/tz-16a-phase2-decisive-gate
```

**Contract §4.2's self-check**, run after the push and the pull request and before this report's commit, verbatim:

```
$ git rev-list origin/main | grep -c 5076b4305c7800fc7eed0cd3fe05d9577d1b6cf7
0
$ git diff --name-only origin/main origin/tz-16a-phase2-decisive-gate
research/tz16a-phase2-decisive-gate.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
(grep exit=1)
```

The first line is `0`: the implementation commit is not on `main`. The second names the implementation file alone, and the third prints nothing.

**This report** is the one path this TZ pushes to `main`, in one commit from `/root/tz16a-work/wt-report`, as §2 item 2 and contract §4.1 require.

---

## 12. §9 — retention

It ran in §9's order, only after S2 and V3. Run K did not run. Each step started only after the previous one exited `0`.

### Step 1 — copy first. **1,046 → 1,072 files, 26 copied.**

**The predicate is TZ-14's, applied as TZ-15 applied it.** It takes every 16-to-64 hexadecimal token of every `CryptoReports/*.md` on `origin/main`, matched against each file's full SHA-256 and against its 16-character prefix. It adds `/root/tz15-work/label-ledger.jsonl` by name.

- **29 committed reports were scanned, yielding 1,408 distinct tokens.**
- **487** regular files were hashed under the three trees, worktrees included. **355** carry a SHA-256 a committed report names.
- **329** of them were already held by hash, and **26** were copied.
- Each copy used exclusive create (`O_CREAT | O_EXCL`), named by its path below `/root/` with `/` replaced by `--`, and its hash was asserted at source and destination.
- **The 1,046 files already there hash unchanged: 1,046 of 1,046.** Both of §3.1's files are held.
- **Before: 1,046 files. After: 1,072.**

```
2026-09-27T16:53:29Z
reports scanned 29, distinct 16-to-64 hex tokens 1408
store before: 1046 files, 978 distinct hashes
files hashed under the three trees 487; named 355; already held 329; to copy 26
  copy /root/tz15-work/dev1/tz15-constants.json -> tz15-work--dev1--tz15-constants.json  e6a93f9371e9fb32404482dac7b542c330399117ba0cf93e466b846e5878dfd3
  copy /root/tz15-work/dev1/tz15-disclosure.md -> tz15-work--dev1--tz15-disclosure.md  4d9f442507d34cac54480da69dc55b8728bbebf2372c7889ee5620682215b188
  copy /root/tz15-work/label-ledger.jsonl -> tz15-work--label-ledger.jsonl  9f9909583893e8f40f38b1925f09866160f9a9233eaab902960eb882cb76bcb5
  copy /root/tz15-work/run1/tz15-observations.csv -> tz15-work--run1--tz15-observations.csv  a7ac8a495e00e21cd34af6ead7f05e9a2b741231c928bb61d4ec03ec0e610ce6
  copy /root/tz15-work/run1/tz15-readings.json -> tz15-work--run1--tz15-readings.json  85b90d8e6c4ec96004ddcc277e501b0394f6b952d739716aa620ab37a03f2e56
  copy /root/tz15-work/run1/tz15-run.json -> tz15-work--run1--tz15-run.json  e79d80967678cec754285fc42d8dd28cd203275f334ecf3d6457fa8bdc953f5b
  copy /root/tz15-work/run1/tz15-tables.md -> tz15-work--run1--tz15-tables.md  96953d02765b6deae6d799a22c333681d53f3e4cd9f64f982be01721a31a12ab
  copy /root/tz15-work/wt-report/.git -> tz15-work--wt-report--.git  fdbc86802d9416183be9d1dc746cce8372394b184b9e864edaa9b0bcb42c6d89
  copy /root/tz15-work/wt-report/SYSTEM-MAP.md -> tz15-work--wt-report--SYSTEM-MAP.md  7e3306e6b92551a178cb23292d526be881c5c848e394e47e7b4101b48acc6ec3
  copy /root/tz16-work/logs/closing-read.txt -> tz16-work--logs--closing-read.txt  fd000a0835f1eeb7d8814c1feeb73afaebf6ea0c7c1dc66efdac0e821e763eb1
  copy /root/tz16-work/logs/r-ready.txt -> tz16-work--logs--r-ready.txt  4ac9a6f5d32cfdd593d4259086302076ae3f3e18872682ae3df0c0c032872c60
  copy /root/tz16-work/scratch/check-report.py -> tz16-work--scratch--check-report.py  96a4f2d101e415941817ac10e57f13a76ae06194380a463ef560989bfaae6c55
  copy /root/tz16-work/scratch/evidence-v4a.out -> tz16-work--scratch--evidence-v4a.out  cc1b47384e338b407e98a388e2162e3f018590c5e020fbcd984b5c3b6fad1588
  copy /root/tz16-work/scratch/evidence-v4a.py -> tz16-work--scratch--evidence-v4a.py  d46753a35d2c56c8e947ced7d945410b3e6c8d89392a81ab53f74ac07b0eba71
  copy /root/tz16-work/scratch/fingerprint.py -> tz16-work--scratch--fingerprint.py  31b0ce335cc12854c86bc9eddb00067773ccbdd92ff396329ac0dcd1f4c0f301
  copy /root/tz16-work/scratch/probe_selftests.out -> tz16-work--scratch--probe_selftests.out  8a16bacea2d8635b572ffefbe211b06193b98c31b9631d6a9f5b318f31319ec4
  copy /root/tz16-work/scratch/probe_selftests.py -> tz16-work--scratch--probe_selftests.py  848ad2c0eb34fa5d43701164e7960b6120f740621b82b0351366d8d24589485f
  copy /root/tz16-work/scratch/probe_sumq.py -> tz16-work--scratch--probe_sumq.py  6dec26af59fe0836fdb0e31ce995ca91d10482c46bbf193d70460bd01fd9ad45
  copy /root/tz16-work/scratch/probe_tz15files.py -> tz16-work--scratch--probe_tz15files.py  f9c533417d3044e6d0a6eec5995328f38c4bb370b271382b2528c20e22d583c3
  copy /root/tz16-work/wt-report/CryptoTZ/TZ-16-phase2-decisive-gate.md -> tz16-work--wt-report--CryptoTZ--TZ-16-phase2-decisive-gate.md  0e0752cdfacaa517102077052372a32de9557eb6baa37f5354a499b83c7196dd
  copy /root/tz16-work/wt-report/CryptoTZ/TZ-18a-chainbook-capture-redeploy.md -> tz16-work--wt-report--CryptoTZ--TZ-18a-chainbook-capture-redeploy.md  b989a1d32ee66cf7c95495773484037e9399542829b311045f6e938637001ba1
  copy /root/tz16-work/wt-report/SYSTEM-MAP.md -> tz16-work--wt-report--SYSTEM-MAP.md  f15257c4e41dd221f4b56d526ffd463b5b9bae24721b7e2be4b11f25e2c8545a
  copy /root/tz16-work/wt-report/research/tz18a-chainbook-capture.py -> tz16-work--wt-report--research--tz18a-chainbook-capture.py  e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae
  copy /root/tz18a-work/run-1/tz18a-prestart.json -> tz18a-work--run-1--tz18a-prestart.json  d6d06a4fc9229f1eabc77ddea5fe10a9b4f5e84d2cde243f516cd366159d4d0e
  copy /root/tz18a-work/run-2/tz18a-proof.json -> tz18a-work--run-2--tz18a-proof.json  2f9831f3c74893e01384aeb36863b8aa9dd7a25db27ad0b08c1c8998f9a06eea
  copy /root/tz18a-work/wt-report/SYSTEM-MAP.md -> tz18a-work--wt-report--SYSTEM-MAP.md  704070149009b9581de1210d371d0edba9f3dc9a608151a90d0498d31d447b00
store after: 1072 files; the 1046 already there unchanged; both section 3.1 files held
exit=0
1072
2026-09-27T16:53:30Z
```

### Step 2 — the five worktrees. **Each exited `0`, without `--force`.**

None held an untracked file or a `__pycache__`, so nothing was deleted first.

```
git worktree remove /root/tz15-work/wt exit=0
test -e /root/tz15-work/wt exit=1
git worktree remove /root/tz15-work/wt-report exit=0
test -e /root/tz15-work/wt-report exit=1
git worktree remove /root/tz16-work/wt-report exit=0
test -e /root/tz16-work/wt-report exit=1
git worktree remove /root/tz18a-work/wt exit=0
test -e /root/tz18a-work/wt exit=1
git worktree remove /root/tz18a-work/wt-report exit=0
test -e /root/tz18a-work/wt-report exit=1
/root/btc-5m-twap           0c2d3f0 [main]
/root/tz16a-work/wt         5076b43 [tz-16a-phase2-decisive-gate]
/root/tz16a-work/wt-report  0c2d3f0 (detached HEAD)
```

### Step 3 — the three trees. **One removed; two refused by the session's permission classifier.**

Each ran as its own command, naming one tree:

```
2026-09-27 section 9 step 3, one command naming one tree each, in order:
rm -rf /root/tz15-work   -> REFUSED by the session's permission classifier ([Irreversible Local Destruction]); not run
rm -rf /root/tz16-work   -> exit=0; test -e /root/tz16-work exit=1
rm -rf /root/tz18a-work  -> REFUSED by the session's permission classifier ([Irreversible Local Destruction]); not run
Handed to the Boss, each its own block:
rm -rf /root/tz15-work; echo "exit=$?"; test -e /root/tz15-work; echo "test -e exit=$?"
rm -rf /root/tz18a-work; echo "exit=$?"; test -e /root/tz18a-work; echo "test -e exit=$?"
```

- **`/root/tz16-work` is gone:** `rm -rf` exited `0`, and `test -e` exits `1`.
- **`rm -rf /root/tz15-work` and `rm -rf /root/tz18a-work` were refused** by the session's permission classifier. It named "Irreversible Local Destruction". Map §6 records this as unpredictable. Each was left, per §9, for the Boss to run as its own exact block, in a root shell on the VPS:

```
rm -rf /root/tz15-work; echo "exit=$?"; test -e /root/tz15-work; echo "test -e exit=$?"
rm -rf /root/tz18a-work; echo "exit=$?"; test -e /root/tz18a-work; echo "test -e exit=$?"
```

**Verification is the Executor's**, from `test -e` exiting `1`, never from the Boss's account. Neither block had been run when this report was committed. So the verification falls to the next TZ's §0, as TZ-17's did for TZ-15's refused tree (map §3).

- **What those two trees still hold:** everything but their worktrees. Every file a committed report names by hash is in the store, and so is `/root/tz15-work/label-ledger.jsonl`.
- **Never removed:** `/root/tz18a-svc/` (the service runs from it), both capture roots, `/root/tz01-env/` and `/root/tz04a-env/`.
- **`/root/tz16a-work/`**, the label ledger included, is the next TZ's to reclaim on the same terms.

### The closing read — verbatim, after retention

```
2026-09-27T16:56:03Z 1790528163
df -B1 --output=source,size,avail /var/lib/btc-recorder
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 12969000960
pgrep -fx '/root/tz04a-env/venv/bin/python -B -u recorder.py'; echo "exit=$?"
228592
exit=0
grep -c 4216c04673ced76b5b2ac60ef57c9abedc46f9b9 /var/lib/btc-recorder/runtime.jsonl
1
pgrep -fx '/root/tz01-env/venv/bin/python -B -u /root/tz18a-svc/tz18a-chainbook-capture.py --serve'; echo "exit=$?"
2699889
exit=0
du -sb /root/PROJECT_GAMING_PS5
437198309	/root/PROJECT_GAMING_PS5
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
disabled
exit=1
systemctl is-active telemetry-watch.service; echo "exit=$?"
inactive
exit=3
for d in /root/tz15-work /root/tz16-work /root/tz16a-work /root/tz18a-work /root/tz18a-svc; do test -e "$d"; echo "$d exit=$?"; done
/root/tz15-work exit=0
/root/tz16-work exit=1
/root/tz16a-work exit=0
/root/tz18a-work exit=0
/root/tz18a-svc exit=0
find /root/btc-forensics -type f | wc -l
1072
du -sb /root/tz16a-work /root/.claude
22167020	/root/tz16a-work
197428143	/root/.claude
git worktree list
/root/btc-5m-twap           0c2d3f0 [main]
/root/tz16a-work/wt         5076b43 [tz-16a-phase2-decisive-gate]
/root/tz16a-work/wt-report  0c2d3f0 (detached HEAD)
2026-09-27T16:56:03Z 1790528163
```

The recorder is still pid `228592`, and its log still carries the `4216c04` start record. The chain book service is still pid `2699889`, and `telemetry-watch` is still `disabled` (1) and `inactive` (3). Neither process was signalled at any point.

---

## 13. Every point where the text needed a reading, with the workaround chosen

1. **The pipeline was exercised before the span, on data below the reserve.**
   - **Why:** D1 and D2 are the only runs without `--score` §5.5 allows, and nothing after the label read may raise. So before D1, scratch harnesses outside the repository drove the instrument's own functions end to end.
   - **The data:** 40 and 150 slots of TZ-14's already-scored span (`AFTER` `1789206600` and `1789473600`), a fake chain book root under `/root/tz16a-work/scratch`, and synthetic labels, a hash of `T0`.
   - **What stood in for the label reader:** a fake that opened dummy files in the scratch directory. It read no label of any set.
   - **A second harness** took synthetic trades through every post-label path: `n = 0`, `1` and `3`; a constant residual (`v = 0`); and EDGE with the claimed size also rejected. Nothing raised.
   - **What they opened of the reserved span:** `manifest.json` alone, through `load_manifests`, which map §2.3 excepts. Their set rule opened settled documents of TZ-14's units, existence only, and step 4 read TZ-15's two files under exemption (c).
   - They are neither D1 nor D2, and their outputs stay in `/root/tz16a-work/scratch/`.
   - They caught one formatting defect, zeros printed as `0E-12`, which was fixed before the commit.
2. **The commit came before D1.** §5.5 places "commit; push" after D2. The file was committed locally as `5076b43` before D1, and pushed only after D2. That way D1 and D2 ran on the very commit S1 and S2 scored, and V3's comparison "with every run without `--score` on that commit" has two members. No fix was needed between the runs, so there is one commit.
3. **A run without `--score` writes its label-free files at step 11.** §5.1's step 11 names host read 3 and V9's assertions. The instrument also writes the label-free tables, disclosure, observations and readings there, before host read 3. `label` and `y` are empty in them. The output code thus ran twice on the span before the push, and D1 and D2 compare byte for byte. Only `tz16a-constants.json` of those runs enters V3.
4. **The `--selftest` runs' free-space reads are not reported.** §0.4 asks for every read with its instant. The three `--selftest` runs each asserted host read 1 at `2,060,000,000` and exited `0`, but that mode prints no host read and writes no run file. Their values are lost, and the bound held at each.
5. **§0.8's 2,400th and the set's 2,400th differ by one slot.** The reason is `1790188800`'s fifth set-rule condition (§2). §3.3's clock condition was asserted on the set's own 2,400th member.
6. **§3.5's reasons are this instrument's own words.** TZ-15's rule is unchanged, but TZ-15 printed its reasons in other words. The reasons here are `status …, JSON …`, `the reply body is not an object`, `the reply names no size or no tick`, `the token is outside the mapping` and `market document: …`. None fired.
7. **The row of §4.1 is derived, not recomputed.** `read_look` returns the reading and the flag, as §5.1 fixes. The row printed beside each reading is a function of that reading and `n`, and repeats no comparison.
8. **The instrument adds assertions to the TZ's text, each before any label.** None fired. They cover:
   - the anchor-row count, 6;
   - the 12,000 pricer rows and the 12,000 observation rows;
   - that every selected member is eligible, before the read;
   - `FP_E <= alpha1` and `FP_N <= beta1`;
   - `fisher_upper`'s argument ranges;
   - in a scored run, V6's `git status --porcelain` empty for the scoped paths, so the scored file is the committed one.
9. **"Fully loaded" is `missed == 0` as an integer.** A boolean or absent `missed` would not count. All 297 exposed windows read the integer `0`.
10. **§4.3's power is printed to 20 significant digits in the tables.** The exact `Fraction` runs to hundreds of digits, and `tz16a-readings.json` carries it in full.
11. **The report's section order is the TZ's** (§8), with contract §8's content inside it, as the contract's preamble allows.
12. **Retention step 3 was partly refused** (§12). §9's fallback was taken: the two blocks are handed to the Boss, and verification from `test -e` is left to the next TZ.
