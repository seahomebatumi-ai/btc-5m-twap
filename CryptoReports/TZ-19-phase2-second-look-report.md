# TZ-19 — Phase 2's second look, tau 240 — REPORT

**Status: BLOCKED at §0.2's host gate, H2, before the build.** The recorder is not running: no process runs `recorder.py`, and its last log record is dated 2026-10-02 11:35:44 UTC (§2, §3).

- **Reading at `tau` 240: none.** No set was formed, no quote file was opened and no label was read.
- **Phase 2's verdict (§4.3): none.** No row of §4.3's table applies without a reading. TZ-16a's readings stand as its report gives them: NO EDGE at `tau` 180, 120, 90 and 60, and UNDECIDABLE at 240 after the first look.
- **Interlock (§3.10, §4.2): not read**, and block K-18a was not run. The chain book service is not running either: its `runtime.jsonl` holds a `stop` record for pid `2699889` at 2026-10-03 08:56:15 UTC. H4 records it and does not block (§3).
- **What follows:** nothing this report can name, because a BLOCKED report suggests no fix (contract §9).
- **Map §2.3's reserve: unchanged.** No reading exists to release any of it, and no file of the span but `manifest.json` was opened.

§0.2's H2 requires that "the first `pgrep -fx` prints exactly one line and `exit=0`". At the host gate
(22:32:50Z) and again at the closing read (22:40:48Z) it printed no line and `exit=1`. Map §6's host-identity
row requires that "the recorder process is running" and ends: "All three, or it is not the capture host."
The instrument's step 1 would stop on the same fact. It calls `tz11a.host_read`, and
`research/tz11a-student-link.py:190` runs `assert doc["recorder_pids"], "V9: no recorder process at %s" % when`.
A copy of the body of `tz10b.recorder_pids`, run against `/proc`, returns `[]` (§3.1). §2 item 2 forbids this
TZ to bring the recorder back: "The recorder is never signalled, stopped or restarted." **No implementation can
pass H2 or step 1 while no recorder runs**, so the run stopped at §0.2. No branch, build worktree or
instrument file was created.

- **Every other §0 gate passed:**
  - the fingerprint: 6 of 6 anchors, 4 of 4 re-derived, and 25 of 25 `frozen` rows (§0);
  - H1, both lines H3 reads, the resource gate, the trees, and the forensic store at `1,072` (§1.1);
  - R-READY: `3,885` complete manifests after `1789669800`, the 3,624th at `1790853000`, and the clock
    `209,897` s past its `+3,900` bound. **So this stop is not a NOT YET**, and the session saw none (§1.2).
- **The capture has a gap from 2026-10-02 11:35 UTC.** The newest interval directory is `1790940900`. None
  exists for any of the `419` five-minute `T0` values after it, up to the host gate's instant (§3.3).
- **This session did not stop either process.** Both had stopped before its first command, at 22:32:50Z on
  2026-10-03, and it signalled neither. The cause of either stop is not established here (§3.3).
- **The reserved span is untouched.** Under `/var/lib/btc-recorder/` this session opened only `manifest.json`
  files and the recorder's top-level `runtime.jsonl`. Under `/var/lib/btc-chainbook/` it opened only
  `runtime.jsonl` (§4).

---

## 0. Fingerprint

`SYSTEM-MAP.md` read in `/root/btc-5m-twap` at `main` `6003102`, after contract §1's fast-forward.

- **Revision string:** `2026-09-27-b`, equal to the TZ header's.
- **Anchors, 6 of 6 equal** to the TZ header's table:

| anchor | TZ-19 header | map §0 |
|---|---|---|
| `A1` | `229a944f2d51` | `229a944f2d51` |
| `A2` | `6c5089330629` | `6c5089330629` |
| `A3` | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` | same |
| `A4` | `437b45ea196b` | `437b45ea196b` |
| `A5` | `9fd1c7de0f74` | `9fd1c7de0f74` |
| `A6` | `729f0bcdbee3` | `729f0bcdbee3` |

- **Re-derived, 4 of 4:** `A2`, `A4`, `A5` and `A6` equal the first 12 hex characters of the SHA-256 of
  `research/twap-divergence.py`, `BTC-EXECUTOR-INSTRUCTIONS.md`, `research/recorder/recorder.py` and
  `research/pfair.py`.
- **Rows:** 28 under `tz14.fingerprint_rows`' rule, applied by the scratch script, **25 `frozen`, 2 `tracked`, 1 `reported`**, the counts
  §0.1 fixes. **25 of 25 `frozen` rows are equal** to the map.

| path | lines | bytes | state | SHA-256 | against map §0 |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 1,045 | 209,705 | reported | `b26544de6b7c5a7554c548160c4937805542ec512686458aad7baaa7ca1a0cdd` | — |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | equal |
| `research/twap-divergence.py` | 1,135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | equal |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | equal |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | — |
| `research/pfair.py` | 441 | 19,357 | frozen | `729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68` | equal |
| `research/selftest-pfair.py` | 619 | 32,559 | frozen | `b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa` | equal |
| `research/tz06-calibration.py` | 577 | 27,138 | frozen | `715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f` | equal |
| `research/tz07a-variance-time.py` | 623 | 28,414 | frozen | `513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771` | equal |
| `research/tz07b-settlement-dispersion.py` | 515 | 24,926 | frozen | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` | equal |
| `research/tz08a-out-of-sample.py` | 745 | 38,822 | frozen | `37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c` | equal |
| `research/tz09-disk-inventory.py` | 894 | 41,004 | frozen | `b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6` | equal |
| `research/tz10b-sigma-or-link.py` | 1,224 | 61,018 | frozen | `406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088` | equal |
| `research/tz11a-student-link.py` | 1,231 | 64,732 | frozen | `0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839` | equal |
| `research/tz12-sized-gate.py` | 1,157 | 61,637 | frozen | `d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999` | equal |
| `research/tz13-sized-gate-test3.py` | 1,074 | 53,901 | frozen | `a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd` | equal |
| `research/tz14-quote-inventory.py` | 2,124 | 109,972 | frozen | `978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02` | equal |
| `research/tz15-phase2-gate.py` | 1,517 | 73,799 | frozen | `66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3` | equal |
| `research/tz16a-phase2-decisive-gate.py` | 2,198 | 111,192 | frozen | `3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125` | equal |
| `research/tz17-settlement-chain.py` | 1,102 | 38,622 | frozen | `e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92` | equal |
| `research/tz18a-chainbook-capture.py` | 1,683 | 69,517 | frozen | `e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae` | equal |
| `research/recorder/recorder.py` | 608 | 25,658 | frozen | `9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03` | equal |
| `research/recorder/config.py` | 112 | 4,773 | frozen | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | equal |
| `research/recorder/manifest.py` | 254 | 10,002 | frozen | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | equal |
| `research/recorder/analyze.py` | 813 | 34,705 | frozen | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` | equal |
| `research/recorder/probe.py` | 227 | 9,324 | frozen | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | equal |
| `research/recorder/selftest.py` | 573 | 30,591 | frozen | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` | equal |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | — |

The table comes from `scratch/fingerprint.py` (§4), not from an instrument, so it is **recorded, not
asserted**. The TZ this session read is `CryptoTZ/TZ-19-phase2-second-look.md` at `6003102`: 1,101 lines,
90,230 bytes, SHA-256 `9d6d3457978fa210cbdb0cb87aa54c7059f86cb3544ce29ff388be610c784f07`.

---

## 1. Gates and host reads

### 1.1 §0.2, the host gate — verbatim, from `/root/btc-5m-twap`

```
$ date -u; date -u +%s
Sat Oct  3 10:32:50 PM UTC 2026
1791066770
$ df -B1 --output=source,size,avail /var/lib/btc-recorder
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 13243400192
$ find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json
$ pgrep -fx '/root/tz04a-env/venv/bin/python -B -u recorder.py'; echo "exit=$?"
exit=1
$ grep -c 4216c04673ced76b5b2ac60ef57c9abedc46f9b9 /var/lib/btc-recorder/runtime.jsonl
1
$ pgrep -fx '/root/tz01-env/venv/bin/python -B -u /root/tz18a-svc/tz18a-chainbook-capture.py --serve'; echo "exit=$?"
exit=1
$ du -sb /root/PROJECT_GAMING_PS5
480935474	/root/PROJECT_GAMING_PS5
$ systemctl is-enabled telemetry-watch.service; echo "exit=$?"
disabled
exit=1
$ systemctl is-active telemetry-watch.service; echo "exit=$?"
inactive
exit=3
$ for d in /root/tz15-work /root/tz16a-work /root/tz18a-work /root/tz18a-svc /root/tz19-work; do test -e "$d"; echo "$d exit=$?"; done
/root/tz15-work exit=1
/root/tz16a-work exit=0
/root/tz18a-work exit=1
/root/tz18a-svc exit=0
/root/tz19-work exit=1
$ find /root/btc-forensics -type f | wc -l
1072
$ git worktree list
/root/btc-5m-twap           6003102 [main]
/root/tz16a-work/wt         5076b43 [tz-16a-phase2-decisive-gate]
/root/tz16a-work/wt-report  5935ca5 (detached HEAD)
```

| gate | requires | read | result |
|---|---|---|---|
| H1 | `find` prints exactly one path | one path | PASS |
| **H2** | the first `pgrep -fx` prints exactly one line and `exit=0` | no line, `exit=1` | **FAIL — the blocker** |
| H3 | `df` names `/dev/vda2` and `31612203008`; `grep -c` prints at least `1` | `/dev/vda2`, `31612203008`; `1` | both lines PASS. Map §6's host identity, which they complete with H1, also requires a running recorder and fails with H2 |
| H4 | recorded, not BLOCKING | no line, `exit=1` | recorded: the chain book service is not running |
| resource gate | `avail` at least `2,060,000,000` | `13,243,400,192` | PASS |
| trees | `/root/tz16a-work` and `/root/tz18a-svc` exit `0`, `/root/tz19-work` exits `1` | `0`, `0`, `1` | PASS |
| trees, recorded | `/root/tz15-work`, `/root/tz18a-work` | `exit=1`, `exit=1` | **both blocks TZ-16a §9 handed the Boss were run**; this read is the verification §0.2 names |
| forensic store | exactly `1,072` files | `1,072` | PASS |
| `du`, `systemctl`, worktrees | printed, no threshold | `480,935,474` bytes; disabled, `exit=1`; inactive, `exit=3`; three worktrees, as map §3 registers | — |

### 1.2 §0.8, readiness — verbatim, from `/root/btc-5m-twap`

```
$ /root/tz01-env/venv/bin/python -B - <<'EOF'   # TZ-19 §0.8's script, verbatim
complete 3885 at-3600 1790845500 at-3624 1790853000 now 1791066797
```

**R-READY holds:** `3,885` complete manifests is at least `3,624`, and `now` `1791066797` is at least
`t0s[3623] + 3,900` = `1790856900`, by `209,897` s. The 3,600th complete manifest has `T0`
`1790845500`. **The session saw no NOT YET.**

**A reading of the order, disclosed.** §0.8 runs "after §0.2 and before anything else", and §0.2 had already
failed when it ran. It was run to settle which stop applies: under NOT YET the session writes no report,
whereas a failed gate requires one. It opened `manifest.json` files and nothing else under the capture root,
which is map §2.3's exception.

### 1.3 §0.6, refs — `git ls-remote origin`, before any branch of §2 existed

```
$ git ls-remote origin   # 2026-10-03T22:37:48Z
6003102ac6bd5d05e4d5a289f7c21d86b4522a51	HEAD
6003102ac6bd5d05e4d5a289f7c21d86b4522a51	refs/heads/main
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
5076b4305c7800fc7eed0cd3fe05d9577d1b6cf7	refs/pull/20/head
ee2f6327390ef4d0c6169d1fba1a2ed4ae936dc3	refs/pull/3/head
0e13a5c76dfa2469ff25b3b0dd282872decf6f25	refs/pull/4/head
4216c04673ced76b5b2ac60ef57c9abedc46f9b9	refs/pull/5/head
5ed667afd1b53f036b9f938fcce13c0d709cd77f	refs/pull/6/head
c44af687203d14d5d485d4297c04cfb827096af9	refs/pull/7/head
26bbb61aed774a88355dd5204d8b69fda9135a68	refs/pull/8/head
e2625ea2b5473c311d59a48f32540ce39d58e591	refs/pull/9/head
d3251aa2bd312409f7b096bfd5968f3bedbd1be5	refs/tags/tz-01a-dataset
ea9290b92b9fa50c22d0560d5d01dfa392af44df	refs/tags/tz-01a-dataset^{}
$ git log --first-parent 5935ca5..origin/main, with the paths each commit changed
6003102 Add files via upload
    CryptoTZ/TZ-19-phase2-second-look.md
84b6020 Merge pull request #20 from seahomebatumi-ai/tz-16a-phase2-decisive-gate
    research/tz16a-phase2-decisive-gate.py
0126a5b Update SYSTEM-MAP.md
    SYSTEM-MAP.md
count 3
```

- `main` is at `6003102`, one commit above PR #20's merge `84b6020`: the upload that carries this TZ, as §0.6
  expects. It still carries revision `2026-09-27-b`.
- `main` is the only branch on `origin`, and `refs/pull/20/head` is at `5076b43`. Both match the Architect's
  read of 2026-09-28.
- `refs/heads/tz-19-phase2-second-look` does not exist.
- **3** commits stand on `main`'s first-parent line above `5935ca5`. That number is recorded, not asserted.

### 1.4 §0.4 and §0.5, every free-space read

§0.5's first read comes after R-READY and before the build. This run stopped at §0.2, so §0.5 never ran as
a read of its own. The host gate and the closing read carry its four quantities:

| instant (UTC) | reader | `/dev/vda2` free | bound | `du -sb /root/PROJECT_GAMING_PS5` | `telemetry-watch` enabled / active |
|---|---|---|---|---|---|
| 2026-10-03 22:32:50 | §0.2, `df -B1` | `13,243,400,192` | `2,060,000,000` | `480,935,474` | disabled (`1`) / inactive (`3`) |
| 2026-10-03 22:40:48 | closing read, `df -B1` | `13,238,452,224` | `2,000,000,000` | `480,881,647` | disabled (`1`) / inactive (`3`) |

At the closing read this session's own footprint was `4,111,590` bytes in `/root/tz19-work` and
`202,400,364` in `/root/.claude`. `/root/tz16a-work`, which belongs to TZ-16a, held `22,398,514`; map §3
records `22,167,020` at TZ-16a's closing read. That difference is recorded, not explained.

### 1.5 The closing read — §0.2's block again, then `du -sb` of the three trees, verbatim

```
$ date -u; date -u +%s
Sat Oct  3 10:40:48 PM UTC 2026
1791067248
$ df -B1 --output=source,size,avail /var/lib/btc-recorder
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 13238452224
$ find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json
$ pgrep -fx '/root/tz04a-env/venv/bin/python -B -u recorder.py'; echo "exit=$?"
exit=1
$ grep -c 4216c04673ced76b5b2ac60ef57c9abedc46f9b9 /var/lib/btc-recorder/runtime.jsonl
1
$ pgrep -fx '/root/tz01-env/venv/bin/python -B -u /root/tz18a-svc/tz18a-chainbook-capture.py --serve'; echo "exit=$?"
exit=1
$ du -sb /root/PROJECT_GAMING_PS5
480881647	/root/PROJECT_GAMING_PS5
$ systemctl is-enabled telemetry-watch.service; echo "exit=$?"
disabled
exit=1
$ systemctl is-active telemetry-watch.service; echo "exit=$?"
inactive
exit=3
$ for d in /root/tz15-work /root/tz16a-work /root/tz18a-work /root/tz18a-svc /root/tz19-work; do test -e "$d"; echo "$d exit=$?"; done
/root/tz15-work exit=1
/root/tz16a-work exit=0
/root/tz18a-work exit=1
/root/tz18a-svc exit=0
/root/tz19-work exit=0
$ find /root/btc-forensics -type f | wc -l
1072
$ git worktree list
/root/btc-5m-twap           6003102 [main]
/root/tz16a-work/wt         5076b43 [tz-16a-phase2-decisive-gate]
/root/tz16a-work/wt-report  5935ca5 (detached HEAD)
/root/tz19-work/wt-report   6003102 (detached HEAD)
$ du -sb /root/tz19-work /root/.claude /root/tz16a-work
4111590	/root/tz19-work
202400364	/root/.claude
22398514	/root/tz16a-work
```

---

## 2. The blocker

**§0.2's H2 fails, and with it map §6's host identity and the instrument's step 1.** H2 requires that the
first `pgrep -fx '/root/tz04a-env/venv/bin/python -B -u recorder.py'` "prints exactly one line and
`exit=0`". It printed no line and `exit=1` at both reads (§1.1, §1.5). Map §8 records the recorder as pid
`228592`. A different pid would have been disclosed, not BLOCKING. No pid at all fails the gate. Map §6's
host-identity row makes the same requirement: "the recorder process is running … All three, or it is not
the capture host." §5.1 step 1 calls `tz11a.host_read`, which asserts `doc["recorder_pids"]` at
`research/tz11a-student-link.py:190`. `doc["recorder_pids"]` comes from `tz10b.recorder_pids`, every
`/proc` entry with an argument ending in `recorder.py`, and that is empty now (§3.1). V9 also asserts that
the pid is unchanged between the first and last host reads. **§2 item 2 forbids the remedy within this TZ:**
"The recorder is never signalled, stopped or restarted." TZ-19 §0.8 reads: "Every other failure is BLOCKED,
as the contract says", and contract §9 counts an unsatisfiable TZ among its reasons. The stop came at §0.2,
before anything was built.

---

## 3. Evidence

### 3.1 No process runs `recorder.py` — the committed function's body, run against `/proc`

```
$ date -u +%FT%TZ
2026-10-03T22:41:45Z
$ /root/tz01-env/venv/bin/python -B /root/tz19-work/scratch/probe-recorder-pids.py
recorder_pids [] -> tz11a.host_read's assert doc['recorder_pids'] would fail
```

The probe, verbatim. It copies the function's body, so that no committed module was loaded:

```python
# TZ-19 BLOCKED evidence, scratch only: the body of the committed tz10b.recorder_pids
# (research/tz10b-sigma-or-link.py:165-177), copied so that no committed module is loaded.
import os
out = []
for name in os.listdir("/proc"):
    if not name.isdigit():
        continue
    try:
        with open(os.path.join("/proc", name, "cmdline"), "rb") as fh:
            argv = fh.read().split(b"\0")
    except OSError:
        continue
    if any(arg.endswith(b"recorder.py") for arg in argv):
        out.append(int(name))
print("recorder_pids", sorted(out), "-> tz11a.host_read's assert doc['recorder_pids'] would", "pass" if out else "fail")
```

### 3.2 When each process stopped — verbatim, four lines of another project omitted

`scratch/stop-evidence.sh` (§4) wrote `logs/stop-evidence.txt`. Below is that file with one change:
`scratch/redact.py` replaced four journal lines of another project on this host with one marker line. The
full file stays on the host, and its SHA-256 is in §4.

```
$ date -u +%FT%TZ
2026-10-03T22:39:08Z
# every process whose executable is a python and whose argv names either program
$ ps -eo pid,args | awk '$2 ~ /python/ && /recorder[.]py|tz18a-chainbook-capture[.]py/' | wc -l
0
$ ps -eo pid,args | awk '$2 ~ /python/' | wc -l   # python processes of any kind, for scale
8

# The recorder's top-level runtime.jsonl
$ wc -l < /var/lib/btc-recorder/runtime.jsonl
60690
$ grep -n '"kind": "start"' /var/lib/btc-recorder/runtime.jsonl | tail -1
5453:{"captured_bytes": 55159600, "free_bytes": 7871356928, "kind": "start", "recv_ns": 1789206785264516934, "sha": "4216c04673ced76b5b2ac60ef57c9abedc46f9b9"}
$ grep -c '"kind": "stop"' /var/lib/btc-recorder/runtime.jsonl
0
$ tail -1 /var/lib/btc-recorder/runtime.jsonl
{"burst": 4, "ip": "193.70.94.182", "kind": "clock", "offset_ms": -8.15427303314209, "recv_ns": 1790940944342950552, "rejected": {}, "rejected_count": 0, "rtt_ms": 1.077413558959961, "server": "pool.ntp.org"}
$ stat -c '%y %n' /var/lib/btc-recorder/runtime.jsonl
2026-10-02 11:35:44.342299844 +0000 /var/lib/btc-recorder/runtime.jsonl
$ date -u -d @1789206785; date -u -d @1790940944
Sat Sep 12 09:53:05 AM UTC 2026
Fri Oct  2 11:35:44 AM UTC 2026

# The newest interval directories, by name, with the directory's own mtime
$ ls /var/lib/btc-recorder/btc-updown-5m | sort -n | tail -3 | xargs -I{} stat -c '%y %n' /var/lib/btc-recorder/btc-updown-5m/{}
2026-10-02 11:33:48.301156806 +0000 /var/lib/btc-recorder/btc-updown-5m/1790940300
2026-10-02 11:35:33.022188340 +0000 /var/lib/btc-recorder/btc-updown-5m/1790940600
2026-10-02 11:35:05.016912483 +0000 /var/lib/btc-recorder/btc-updown-5m/1790940900

# The chain book's runtime.jsonl: event, pid, wall_ns and counters of each record
1 start pid 2608993 wall_ns 1790117616052072857 2026-09-22T22:53:36Z counters None
2 stop pid 2608993 wall_ns 1790145840007723380 2026-09-23T06:44:00Z counters {'asserts': 0, 'bytes_written': 45540, 'recorder_opens': 0, 'requests': 64, 'write_checks': 98}
3 start pid 2699889 wall_ns 1790185190022755903 2026-09-23T17:39:50Z counters None
4 stop pid 2699889 wall_ns 1791017775066372007 2026-10-03T08:56:15Z counters {'asserts': 0, 'bytes_written': 24457260, 'recorder_opens': 0, 'requests': 27756, 'write_checks': 2781}
$ ls /var/lib/btc-chainbook | grep -E '^[0-9]+$' | sort -n | tail -2
1791016200
1791017100

# systemd-logind, at the recorder's start and at its last write
$ journalctl -u systemd-logind --since '2026-09-12 09:50' --until '2026-09-12 09:55' --no-pager
Sep 12 09:52:10 vultr systemd-logind[833]: New session 7379 of user root.
$ journalctl -u systemd-logind --since '2026-10-02 11:18' --until '2026-10-02 11:37' --no-pager
Oct 02 11:18:06 vultr systemd-logind[833]: New session 10935 of user root.
Oct 02 11:24:35 vultr systemd-logind[833]: Session 10935 logged out. Waiting for processes to exit.
Oct 02 11:24:35 vultr systemd-logind[833]: Removed session 10935.
Oct 02 11:24:38 vultr systemd-logind[833]: New session 10936 of user root.
Oct 02 11:36:18 vultr systemd-logind[833]: Removed session 7379.
Oct 02 11:36:26 vultr systemd-logind[833]: Session 10936 logged out. Waiting for processes to exit.
Oct 02 11:36:26 vultr systemd-logind[833]: Removed session 10936.
Oct 02 11:36:30 vultr systemd-logind[833]: New session 10939 of user root.

# Every journal line at 2026-10-02 11:36:18
$ journalctl --since '2026-10-02 11:36:18' --until '2026-10-02 11:36:19' --no-pager
[4 lines omitted: they belong to another project on this host. In this second one of its units was deactivated, and a second unit's process logged "Received SIGTERM signal" and stopped polling]
Oct 02 11:36:18 vultr systemd[1]: session-7379.scope: Deactivated successfully.
Oct 02 11:36:18 vultr systemd[1]: session-7379.scope: Consumed 1h 27min 9.324s CPU time, 177.0M memory peak, 57.7M memory swap peak.
Oct 02 11:36:18 vultr systemd-logind[833]: Removed session 7379.
Oct 02 11:36:18 vultr kernel: bash (3813753): drop_caches: 3

# The chain book's stop, 2026-10-03 08:56:15: root's user manager stopping
$ journalctl --since '2026-10-03 08:56:00' --until '2026-10-03 08:56:16' --no-pager | grep -E 'logind|user@0|tmux-spawn|exit.target'
Oct 03 08:56:04 vultr systemd-logind[833]: Session 11095 logged out. Waiting for processes to exit.
Oct 03 08:56:04 vultr systemd-logind[833]: Removed session 11095.
Oct 03 08:56:14 vultr systemd[1]: Stopping user@0.service - User Manager for UID 0...
Oct 03 08:56:14 vultr systemd[2607743]: Activating special unit exit.target...
Oct 03 08:56:14 vultr systemd[2607743]: Stopping tmux-spawn-315ec8a4-f008-4219-8440-d24d19ccc793.scope - tmux child pane 2607979 launched by process 2607969...
Oct 03 08:56:14 vultr systemd[2607743]: Stopping tmux-spawn-5efd6e86-847c-439f-a4c3-0a42e49ae219.scope - tmux child pane 2948853 launched by process 2948852...
Oct 03 08:56:14 vultr systemd[2607743]: Stopped tmux-spawn-5efd6e86-847c-439f-a4c3-0a42e49ae219.scope - tmux child pane 2948853 launched by process 2948852.
Oct 03 08:56:14 vultr systemd[2607743]: tmux-spawn-5efd6e86-847c-439f-a4c3-0a42e49ae219.scope: Consumed 1h 50min 7.849s CPU time.
Oct 03 08:56:15 vultr systemd[2607743]: Stopped tmux-spawn-315ec8a4-f008-4219-8440-d24d19ccc793.scope - tmux child pane 2607979 launched by process 2607969.
Oct 03 08:56:15 vultr systemd[2607743]: tmux-spawn-315ec8a4-f008-4219-8440-d24d19ccc793.scope: Consumed 33min 4.093s CPU time.
Oct 03 08:56:15 vultr systemd[2607743]: Reached target exit.target - Exit the Session.
Oct 03 08:56:15 vultr systemd[1]: user@0.service: Deactivated successfully.
Oct 03 08:56:15 vultr systemd[1]: Stopped user@0.service - User Manager for UID 0.
Oct 03 08:56:15 vultr systemd[1]: user@0.service: Consumed 4h 21min 29.706s CPU time, 749.0M memory peak, 1.5G memory swap peak.

# logind configuration
$ grep -hE '^[[:space:]]*#?[[:space:]]*(KillUserProcesses|KillExcludeUsers)' /etc/systemd/logind.conf; loginctl show-user root -p Linger
#KillUserProcesses=no
#KillExcludeUsers=root
Linger=no
```

### 3.3 The figures, computed from the literals above

```
recorder start record 2026-09-12T09:53:05Z
recorder last record  2026-10-02T11:35:44Z
recorder ran (s) 1734159 days 20.07
silent at host gate (s) 125826 hours 34.95
T0 values in (newest_dir, gate], none with a directory 419 2026-10-02T11:40:00Z 2026-10-03T22:30:00Z
chain book ran (s) 832585 days 9.64 stop 2026-10-03T08:56:15Z
chain book silent at host gate (s) 48995 hours 13.61
R-READY clock margin (s) 209897 bound 1790856900 2026-10-01T12:15:00Z
resource gate True 11183400192
session 7379 opened, s before the start record 55
session 7379 removed, s after the last record 34
root session 11095 logout to chain book stop record (s) 11
```

**The recorder.**
- Its newest `start` record is line 5,453 of 60,690, `recv_ns` `1789206785264516934`
  (2026-09-12T09:53:05Z), sha `4216c04673ced76b5b2ac60ef57c9abedc46f9b9`.
- Its last record is a `clock` record at `recv_ns` `1790940944342950552` (2026-10-02T11:35:44Z). The run
  lasted 20.07 days, and the log had been silent for `125,826` s (34.95 h) at the host gate.
- The file holds **no `stop` record after any of its starts**, so this stop's missing one tells nothing
  about how it ended.
- The newest interval directory is `1790940900`, 2026-10-02 11:35:00 UTC. No directory exists for any of
  the `419` `T0` values from 2026-10-02T11:40:00Z to 2026-10-03T22:30:00Z.

**Root's login session 7379**, as `systemd-logind` logged it.
- It opened `55` s before the recorder's newest `start` record.
- logind removed it `34` s after the recorder's last record.
- Sessions 10935 and 10936 in the same excerpt each have a "logged out" line before "Removed". 7379 has no
  such line.
- In the same second, another project's process logged `Received SIGTERM signal`, and the kernel logged
  `drop_caches` from a `bash` process.

**Nothing read here ties the recorder's pid to session 7379. The cause of the stop is not established.**

**The chain book service.**
- `start`: pid `2699889`, `wall_ns` `1790185190022755903` (2026-09-23T17:39:50Z).
- `stop`: the same pid, `wall_ns` `1791017775066372007` (2026-10-03T08:56:15Z), after 9.64 days.
- Its counters at the stop: `asserts` 0, `bytes_written` 24,457,260, `recorder_opens` 0, `requests` 27,756,
  `write_checks` 2,781.
- The `stop` record came `11` s after root's login session 11095 logged out. It falls within 08:56:14 to
  08:56:15, the span in which root's user manager, `user@0.service`, stopped two tmux pane scopes and then
  itself.
- `KillUserProcesses` is commented out in `/etc/systemd/logind.conf`, and root's `Linger` is `no`.
- The newest window directory is `1791017100`.

**Nothing read here ties pid `2699889` to either pane scope. That cause is not established either.**
Block K-18a was never run: TZ-16a read HOLD, and this TZ stopped before §3.10.

**This session.** Its first command ran at 2026-10-03 22:32:50Z, after both stops. It ran no `kill`,
`pkill` or `systemctl stop`, and it wrote nothing under either capture root. The one process it stopped was
its own unfinished journal search (§4).

---

## 4. What was not done, and what stayed on the host

- **No instrument.** `research/tz19-phase2-second-look.py` was never written. So:
  - V1 to V14 have nothing to act on;
  - §5.1's order never ran, step 0 included;
  - §0's fingerprint comes from a scratch script and is recorded, not asserted.
- **No branch.** `tz-19-phase2-second-look` exists neither locally nor on `origin`, and the build worktree
  `/root/tz19-work/wt` was never created. The only worktree added was the report checkout:
  `git worktree add --detach /root/tz19-work/wt-report origin/main`, at `6003102`.
- **§9's retention did not run.** It runs "only after S2 and V3", and neither exists:
  - `/root/tz16a-work/` stays on disk with its two worktrees registered;
  - `/root/tz15-work/` and `/root/tz18a-work/` were absent at both reads;
  - `/root/btc-forensics/` held `1,072` files at both reads, and nothing was copied there;
  - `/root/tz18a-svc/` was not touched.
- **The capture roots.** Nothing was written, moved or removed under either root.
  - `/var/lib/btc-recorder/` — opened:
    - every `manifest.json` the series held at 22:33:17Z, through §0.8's command;
    - the recorder's top-level `runtime.jsonl`, through `grep -c` at both reads, through §3.2's script
      (`wc -l`, `grep -n`, `grep -c`, `tail -1`), and through three earlier reads of the same kind (a
      `tail -3`, a `grep -c .`, and a `grep -n` for `start` and `stop` records).
  - `/var/lib/btc-recorder/` — read without opening any file:
    - `ls` of the series directory;
    - `stat` of `runtime.jsonl` and of the three newest interval directories;
    - §0.2's `find`, which names one manifest without opening it.
  - `/var/lib/btc-recorder/` — **not opened:** no quote file, `gamma.json`, settled document, stream, or
    interval-level `runtime.jsonl`.
  - `/var/lib/btc-chainbook/` — opened only `runtime.jsonl`: an early `tail -5` of the first 400 characters of
    each line, an early `python` read of its four records, and §3.2's script. `ls` listed the root.
  - `/var/lib/btc-chainbook/` — **not opened:** no `window.json`, `books.jsonl.gz` or `documents.jsonl`.
- **The system journal** was read with `journalctl`, as §3.2 prints. One unfiltered search over the whole
  journal was started in the background. The session stopped it unfinished, through its own task control,
  and it had printed nothing.
- **`/root/tz19-work/`** is the next TZ's to reclaim. It holds the report checkout and the files below,
  and every Python probe ran with `-B`.
- **Outside `/root/tz19-work/`**, nothing was created or modified except:
  - this report on `main`;
  - git's records of the worktree in `.git`;
  - the session store `/root/.claude`;
  - contract §1's fast-forward of the primary checkout `/root/btc-5m-twap`, from `0c2d3f0` to `6003102`.
- **That fast-forward** changed four paths:
  - `CryptoReports/TZ-16a-phase2-decisive-gate-report.md`;
  - `CryptoTZ/TZ-19-phase2-second-look.md`;
  - `SYSTEM-MAP.md`;
  - `research/tz16a-phase2-decisive-gate.py`.

  It changed nothing under `research/recorder/` and switched no branch.

| file | lines | bytes | SHA-256 | what it is |
|---|---|---|---|---|
| `logs/closing-read.txt` | 39 | 1,539 | `b0957d7b54a242242e18c1455fc9920d01c8c59e85ebbc720bea5000fad20abb` | the closing read (§1.5) |
| `logs/figures.txt` | 12 | 640 | `78e8bbc81644fd32d33f283d31acea6b4a7491ccb335128c3c4252892b154262` | §3.3, as printed |
| `logs/fingerprint.txt` | 36 | 4,201 | `2bc52857222528fff26e3477cccd2c6ec1fb76ce0eec1e57f50e811c03eb12ce` | §0's table |
| `logs/host-gate.txt` | 34 | 1,357 | `dced313af2c8afdec1f033680885637f8d1f763d744997d34f95adbf0726ec1b` | §0.2, as printed (§1.1) |
| `logs/probe-recorder-pids.txt` | 4 | 199 | `4b676b6b4ed0db91d50c29c27bd68f146267573ccd8d6766a9802b58282e5cad` | §3.1, as printed |
| `logs/r-ready.txt` | 2 | 148 | `5c458749a51e4eee6bb08483c69f6bacc10f1dc92551f5378568422bb784a552` | §0.8, as printed (§1.2) |
| `logs/refs.txt` | 33 | 1,788 | `6564382ca47e692fc8e2725f4f63d8eb6e03c9b425b385f59855e079096c7926` | §0.6, as printed (§1.3) |
| `logs/selfcheck.txt` | 8 | 179 | `10a48e91cf7b63c0add006ea2b611f55735ce64675178f13a204082846b852a4` | §5, as printed |
| `logs/stop-evidence-redacted.txt` | 81 | 5,984 | `34c0a5dd9313ec22f97b98e317f372e563756def68d48d517138af5cd06e285c` | §3.2, as printed here |
| `logs/stop-evidence.txt` | 84 | 6,247 | `599695bb915c3812da28dd18b512978e9c94b7f2bbc3dd682beb13bcb755c800` | §3.2's evidence, whole |
| `scratch/check-report.py` | 68 | 5,383 | `6f62b8073693ee745177f2d82a8bcc376cf49f522877103dd5ba4886d3197d77` | checks this report's verbatim blocks, figures and this table |
| `scratch/closing-read.sh` | 17 | 1,920 | `05a55cb7d6350932c223b94ae7c61dbab2aa9a4019501c8a6a7f3ea609dcdf21` | writes `logs/closing-read.txt` |
| `scratch/figures.py` | 25 | 2,136 | `e280a0f22fefd6864f8ba82c986a1bffe13ddce5a611796237f19ac14ac8ce19` | writes `logs/figures.txt` |
| `scratch/fill.py` | 52 | 2,652 | `7489abeed3787f3603831998b55e6f88b6d2f88927b5ec4d700f5263f1d69ceb` | fills the template |
| `scratch/fingerprint.py` | 32 | 1,903 | `cc4dba48699fb113231e73456a50b9e50ae640d2af22f36daa80e2dc0f19a05d` | writes `logs/fingerprint.txt` |
| `scratch/probe-recorder-pids.py` | 15 | 641 | `f07f92337bf5dd8ab41a1f6b976ece8c0efa5488692ddeebd4cffc576b038e8b` | §3.1's probe |
| `scratch/redact.py` | 18 | 980 | `1aa56f67ec72f09e70e98d38c3c8f5f67e18c311a4c20111cc4c083d5c912135` | writes `logs/stop-evidence-redacted.txt` |
| `scratch/report-template.md` | 292 | 16,367 | `df1dbfa8a6364f6bb2b6e1571146685edad4ca53990b2f13f6d03d88189d1884` | this report, before its placeholders are filled |
| `scratch/stop-evidence.sh` | 54 | 3,942 | `4c50eec5180ce88dcd63669fa89de50e8301bab42658659c7cc839f3bc6f6e97` | writes `logs/stop-evidence.txt` |

---

## 5. Publication

- **This report is the one path this TZ pushes to `main`.** It goes in one commit from
  `/root/tz19-work/wt-report`, as §2 item 2 and contract §4.1 require.
- **No branch, implementation commit, pull request or Release exists**, so contract §5's publication steps
  have nothing to publish.
- The first two lines of contract §4.2's self-check name an implementation commit and a branch on
  `origin`. Neither exists, so the reads below stand in their place:

```
$ git ls-remote origin 'refs/heads/tz-19*'
(no output)

$ git branch --list 'tz-19*'
(no output)

$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
(no output)
```

No dataset, archive or binary is in git history. **Nothing of the reserved span was read, and no label of
any interval was read.**
