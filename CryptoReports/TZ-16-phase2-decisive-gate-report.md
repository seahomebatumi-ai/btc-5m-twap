# TZ-16 — Phase 2's decisive gate, first look — REPORT

**Status: BLOCKED at §3.2's input assertion, V4 (a), before the build.** At `tau` 180 and 60, the `Σq` values §3.2 quotes from the TZ-15 report are not the sums of the file TZ-15 scored (§2).

- **Reading at each `tau` (240, 180, 120, 90, 60): none.** No set was formed, no quote was opened and no label was read.
- **Verdict (§4.4): none.**
- **Interlock (§3.10, §4.3): not read.** Block K-18a was not run, and the chain book service runs on as pid `2699889`.
- **Which TZ must follow:** neither §4.2's second look nor a confirmation, because nothing was read. A defective expectation stops the run and requires a new TZ (contract §6; TZ-16 §5.4).

§3.2 asserts, per `tau`, that `Σq` over TZ-15's selected rows "lies within `D("0.00005")` of
`233.5794 / 230.1412 / 208.2308 / 171.8683 / 114.1073`. Any difference is BLOCKED: the file is not the
one TZ-15 scored." The file §3.1 locates is `tz15-observations.csv`, SHA-256 `a7ac8a49…`, the hash the
TZ-15 report §12 names. It sums to `230.1410794878433773409` at `tau` 180 and to
`114.107227667538293020748` at `tau` 60. Those miss the quoted values by `0.000121` and `0.000072`.
TZ-15's own `tz15-constants.json`, at the SHA-256 `e6a93f93…` that report names, records the same two
sums to every digit. **The file is the one TZ-15 scored, and the two quoted figures are not its sums.**
§5.4 reads: "An expectation of §5.2 or §7 is never edited: a wrong one is BLOCKED." No implementation
can pass this assertion, because the file is fixed by its hash. The stop therefore came before anything
was built.

- **Every §0 gate passed first:**
  - 6 of 6 anchors, 4 of 4 re-derived, and 24 of 24 `frozen` rows.
  - H1 to H3, the resource gate, the trees, and the forensic store at `1,046`.
  - R-READY: `2,531` complete manifests after `1789669800`, the 2,400th at `1790451900`, and the
    clock `39,430` s past its `+3,900` bound (§1).
- **What else was checked, and is not the blocker:**
  - The other 18 of V4 (a)'s 20 comparisons hold, and V4 (b) holds at 15 of 15.
  - All 78 expectations of §5.2 reproduce exactly under an independent rational computation (§4).
- **The reserved span is untouched.**
  - Under `/var/lib/btc-recorder/`, this session opened only `manifest.json` files, through §0.8's
    command, and the recorder's top-level `runtime.jsonl`, through `grep -c`.
  - Nothing was opened under `/var/lib/btc-chainbook/`.
  - No quote file, `gamma.json`, settled document or stream was opened, and no label was read.
  - The recorder (pid `228592`) and the chain book service (pid `2699889`) were not signalled.

**Nothing TZ-16 asks for was computed.**

- `research/tz16-phase2-decisive-gate.py` was not written.
- No branch reached `origin`, and no pull request or Release exists. A local branch and worktree were
  created at start-up. They never held a commit, and both were removed before this report (§5).
- **Not computed:**
  - The set: no `tz06.scoring_set`, no walk and no pricer row.
  - The quotes, the selection, `U0`, `U1`, `c`, `d` and either power.
  - The interlock counts and any label.
- **§3.2's `ρ_k`, `f̂` and `f` are not reported.** A scratch probe computed them from TZ-15's file while
  locating the blocker (§5). Contract §9 bars partial measurements from this report.
- §9's retention did not run. `/root/tz15-work/` and `/root/tz18a-work/` are as they were, and nothing
  was copied into `/root/btc-forensics/`.

The TZ header names its executor model, and this session runs that model.

---

## 0. Fingerprint

**Where it was read.** `git fetch` brought `origin/main` to `86b51a4c984c907e364f545406137afdd6c9607c`.
The primary checkout `/root/btc-5m-twap` was fast-forwarded to it from `3a95ae1` on 2026-09-27.

**The TZ file.** `CryptoTZ/TZ-16-phase2-decisive-gate.md`: 946 lines, 69,118 bytes, SHA-256
`0e0752cdfacaa517102077052372a32de9557eb6baa37f5354a499b83c7196dd`. It landed at `86b51a4`.

- The copy it replaces, at `b20061e`, hashes to
  `e9b83e99c9c74b2c9590b6427f38e90c7eb43bc9f573b75e65c4ec035aff0f50`, as the header states.
- `git diff -U0 b20061e 86b51a4` over the file shows **3** hunks, as §10's re-reading states.
- The map was last changed at `f65cda5e921fbbffc36e66d86a55bbb9015475ec`.

**Map revision required:** `2026-09-23-b`. **Read:** `2026-09-23-b`.

| anchor | required by TZ-16 | read from map §0 | re-derived from the file |
|---|---|---|---|
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` | a Release asset, not a file anchor |
| `A2` — collector | `6c5089330629` | `6c5089330629` | `6c5089330629` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-undecidable-5tau` | same | not a file anchor |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b` | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` | `9fd1c7de0f74` | `9fd1c7de0f74` |
| `A6` — pricer | `729f0bcdbee3` | `729f0bcdbee3` | `729f0bcdbee3` |

**6 of 6 anchors match. The four file anchors re-derive: 4 of 4.**

**The instrument that asserts this at step 0 was never built.** This table comes from a scratch
script. It reads the map's rows by `tz14.fingerprint_rows`' rule: a table line of five cells, whose
first cell starts with a backtick and whose fourth is a state. It then hashes each path on
`origin/main` at `86b51a4`.

The table has 27 rows: **24 of 24 `frozen` rows equal the map**, 2 are `tracked` and 1 is `reported`.
Those are the counts §0.1 fixes. Every figure in the table is **recorded, not asserted**.

| path | lines | bytes | state | SHA-256 | equals the map |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 983 | 190,711 | reported | `f15257c4e41dd221f4b56d526ffd463b5b9bae24721b7e2be4b11f25e2c8545a` | — |
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

**Interpreter (§0.3):** `/root/tz01-env/venv/bin/python`, Python `3.12.3`, `numpy` `2.5.3`, and
`import numpy` succeeds.

---

## 1. Gates and host reads — §0.2 to §0.8

### 1.1 §0.2, the host gate — verbatim, from `/root/btc-5m-twap`

It was run through `bash -v`, which echoes each command before its output:

```
2026-09-27T07:47:00Z 1790495220
df -B1 --output=source,size,avail /var/lib/btc-recorder
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 13041119232
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
434596737	/root/PROJECT_GAMING_PS5
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
disabled
exit=1
systemctl is-active telemetry-watch.service; echo "exit=$?"
inactive
exit=3
for d in /root/tz15-work /root/tz16-work /root/tz18a-work /root/tz18a-svc; do test -e "$d"; echo "$d exit=$?"; done
/root/tz15-work exit=0
/root/tz16-work exit=1
/root/tz18a-work exit=0
/root/tz18a-svc exit=0
find /root/btc-forensics -type f | wc -l
1046
git worktree list
/root/btc-5m-twap           86b51a4 [main]
/root/tz15-work/wt          f7f171a [tz-15-phase2-gate]
/root/tz15-work/wt-report   c729008 (detached HEAD)
/root/tz18a-work/wt         ca4bbc1 [tz-18a-chainbook-capture]
/root/tz18a-work/wt-report  7d8cb75 (detached HEAD)
```

| check | required | read | result |
|---|---|---|---|
| **H1** | `find` prints exactly one path | one path | **holds** |
| **H2** | one line from the first `pgrep -fx`, then `exit=0` | `228592`, `exit=0`: the pid map §8 records | **holds** |
| **H3** | source `/dev/vda2`, size `31612203008`, `grep -c` at least `1` | `/dev/vda2`, `31612203008`, `1` | **holds** |
| **H4** — recorded | the chain book service | `2699889`, `exit=0`: the pid map §2.5 records | recorded |
| resource gate | `avail` at least `2,060,000,000` | `13,041,119,232` | **holds** |
| trees | `tz15-work`, `tz18a-work` and `tz18a-svc` exit `0`; `tz16-work` exits `1` | `0`, `0`, `0`; `1` | **holds** |
| forensic store | exactly `1,046` files | `1,046` | **holds** |
| `du`, `systemctl`, `git worktree list` | printed, no threshold | `434,596,737` bytes; `disabled` (1) and `inactive` (3); five worktrees, as map §3 counts | recorded |

### 1.2 §0.8, readiness — verbatim, from `/root/btc-5m-twap`

This opened each `manifest.json` under `/var/lib/btc-recorder/btc-updown-5m/` and nothing else:

```
2026-09-27T07:47:08Z 1790495228
complete 2531 at-2400 1790451900 now 1790495230
```

**R-READY holds.** There are `2,531` complete manifests with `T0 > 1789669800`, against the `2,400`
required. `now` is `1790495230`, which is at or past `t0s[2399] + 3,900` = `1790455800` by `39,430` s.
`1790451900` is Saturday 2026-09-26 19:45 UTC.

### 1.3 §0.5, preflight read 1 — before the build

```
2026-09-27T07:47:18Z 1790495238.205167374
df -B1 /dev/vda2
Filesystem       1B-blocks        Used   Available Use% Mounted on
/dev/vda2      31612203008 17135251456 13041082368  57% /
du -sb /root/PROJECT_GAMING_PS5
434611562	/root/PROJECT_GAMING_PS5
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
disabled
exit=1
systemctl is-active telemetry-watch.service; echo "exit=$?"
inactive
exit=3
test -e /root/tz16-work; echo "tz16-work exit=$?"
tz16-work exit=1
du -sb /root/.claude
192293605	/root/.claude
2026-09-27T07:47:18Z 1790495238.346031244
```

This session's own footprint at read 1 (map §7 item 29):

- `/root/tz16-work` did not exist, so its footprint was **0** bytes.
- `/root/.claude` held **192,293,605** bytes.

**§0.5's second read was not taken.** It belongs before the first run with `--score`, and no run of
any kind exists. §1.6 records a closing read instead.

### 1.4 §0.6, refs — `git ls-remote origin`, before any branch of §2 existed

```
86b51a4c984c907e364f545406137afdd6c9607c	HEAD
86b51a4c984c907e364f545406137afdd6c9607c	refs/heads/main
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
```

**Recorded differences, not BLOCKING:**

- `main` is at `86b51a4`, not map §1's `7d8cb75`. On `main`'s first-parent line five commits sit above
  `7d8cb75`:
  - `c0cd293`, PR #19's merge;
  - `f65cda5`, the map's upload;
  - `b20061e`, this TZ's first upload;
  - `cc92085`, which deleted that copy;
  - `86b51a4`, this TZ's second upload.

  §0.6 names four of them and does not name the deletion.
- `refs/heads/tz-18a-chainbook-capture` is still on `origin` at `ca4bbc1`, after PR #19's merge.
- `refs/pull/19/merge` is gone. Map §1 says GitHub keeps it only while the pull request is open.

**Neither BLOCKING condition holds.** `main` carries revision `2026-09-23-b`, and
`refs/heads/tz-16-phase2-decisive-gate` did not exist on `origin`. It still does not.

### 1.5 §0.4, every free-space read, with its instant, reader and bound

| UTC | free bytes on `/dev/vda2` | read by | bound | result |
|---|---|---|---|---|
| 2026-09-27T07:47:00Z | 13,041,119,232 | §0.2, `df -B1 --output=source,size,avail` | `2,060,000,000`, the resource gate | above; recorded, not asserted |
| 2026-09-27T07:47:18Z | 13,041,082,368 | §0.5 read 1, `df -B1 /dev/vda2` | `2,000,000,000` | above; recorded, not asserted |
| 2026-09-27T07:58:59Z | 13,035,532,288 | the closing read, `df -B1 --output=source,size,avail` | `2,000,000,000` | above; recorded, not asserted |
| 2026-09-27T08:05:15Z | 13,034,811,392 | this report's pre-commit check, `os.statvfs` on `/var/lib/btc-recorder` | `2,000,000,000` | above; **asserted** — the check aborts below the bound |

`tz11a.host_read` never ran, because the instrument that calls it was never built.

### 1.6 The closing read — verbatim, after the probes and the worktree's removal

```
2026-09-27T07:58:59Z 1790495939
df -B1 --output=source,size,avail /var/lib/btc-recorder
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 13035532288
pgrep -fx '/root/tz04a-env/venv/bin/python -B -u recorder.py'; echo "exit=$?"
228592
exit=0
grep -c 4216c04673ced76b5b2ac60ef57c9abedc46f9b9 /var/lib/btc-recorder/runtime.jsonl
1
pgrep -fx '/root/tz01-env/venv/bin/python -B -u /root/tz18a-svc/tz18a-chainbook-capture.py --serve'; echo "exit=$?"
2699889
exit=0
du -sb /root/PROJECT_GAMING_PS5
434747146	/root/PROJECT_GAMING_PS5
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
disabled
exit=1
systemctl is-active telemetry-watch.service; echo "exit=$?"
inactive
exit=3
for d in /root/tz15-work /root/tz16-work /root/tz18a-work /root/tz18a-svc; do test -e "$d"; echo "$d exit=$?"; done
/root/tz15-work exit=0
/root/tz16-work exit=0
/root/tz18a-work exit=0
/root/tz18a-svc exit=0
find /root/btc-forensics -type f | wc -l
1046
du -sb /root/tz16-work /root/.claude
3676338	/root/tz16-work
193213656	/root/.claude
git worktree list
/root/btc-5m-twap           86b51a4 [main]
/root/tz15-work/wt          f7f171a [tz-15-phase2-gate]
/root/tz15-work/wt-report   c729008 (detached HEAD)
/root/tz16-work/wt-report   86b51a4 (detached HEAD)
/root/tz18a-work/wt         ca4bbc1 [tz-18a-chainbook-capture]
/root/tz18a-work/wt-report  7d8cb75 (detached HEAD)
2026-09-27T07:58:59Z 1790495939
```

- **Nothing the gate reads has moved:**
  - The recorder is still pid `228592`, and its log still carries the `4216c04` start record.
  - The chain book service is still pid `2699889`.
  - The store still holds `1,046` files, and `telemetry-watch` is still `disabled` (1) and `inactive` (3).
- **Rates across the 701 s from read 1, as arithmetic on two reads:**
  - Free space moved by `−5,550,080` bytes, which is `−684,061,215` bytes/day at that rate.
  - `PROJECT_GAMING_PS5` grew `+135,584` bytes, `+16,711,066` bytes/day.
- **This session's own footprint:**
  - `/root/tz16-work` grew from 0 to `3,676,338` bytes. Most of it is the two checkouts of
    `86b51a4`, and one of those was removed before this read.
  - `/root/.claude` grew `+920,051` bytes.
  - With that footprint and the consumer's growth taken out, `818,107` bytes are left, about
    `100,833,730` bytes/day, for the capture and everything else. `df` counts blocks and `du -sb`
    counts apparent bytes, so this is approximate.
- **None of these figures gates anything.**

---

## 2. The blocker

TZ-16 §3.2, lines 264–268:

> **Asserted against the TZ-15 report §4 and §7, per `tau`:** `n` is `405 / 428 / 440 / 380 / 271`;
> `Σy` is `210 / 211 / 190 / 164 / 99`; `Σa` equals `D("216.2300")`, `D("212.5000")`, `D("192.1940")`,
> `D("156.7230")`, `D("102.5810")` as a value; and `Σq` lies within `D("0.00005")` of
> `233.5794 / 230.1412 / 208.2308 / 171.8683 / 114.1073`. Any difference is BLOCKED: the file is not
> the one TZ-15 scored.

§7 V4 (a), line 714, asserts it at step 4. §5.4, line 655, states: "An expectation of §5.2 or §7 is
never edited: a wrong one is BLOCKED." §10 C2, line 823, gives the values' origin: "V4 (a)'s twenty
values from the TZ-15 report §4 and §7 … each tolerance half a unit of the last digit printed."

**§3.1's location, read exactly as written.**

- Every regular file under `/root/tz15-work/` was hashed: 182 files.
- `a7ac8a495e00e21cd34af6ead7f05e9a2b741231c928bb61d4ec03ec0e610ce6` (`tz15-observations.csv`) has
  **2** copies. The first in sorted path order is `/root/tz15-work/run1/tz15-observations.csv`:
  940,729 bytes, 6,001 lines and TZ-15's 18 columns.
- `e6a93f9371e9fb32404482dac7b542c330399117ba0cf93e466b846e5878dfd3` (`tz15-constants.json`) has **5**
  copies, and the first is `/root/tz15-work/dev1/tz15-constants.json`.
- Both hashes are the ones the TZ-15 report prints, in §12 and §5. Neither file is absent, so §3.1's
  own BLOCK does not fire.

**§3.2's read, exactly as written.** The rows at each `tau` whose `selected` cell is `1` are taken in
ascending `T0`. `a` and `q` are read as `D(cell)` and `y` as `int(cell)`, in `Decimal` at 60 digits.
The `Σq` column was also re-summed in exact rationals, and the two agree exactly.

| `tau` | `n` | `Σy` | `Σa` | `Σq` read from the file | `Σq` quoted | `\|Σq − quoted\|` | within `0.00005` | TZ-15's `sum_q`, in its `tz15-constants.json` |
|---|---|---|---|---|---|---|---|---|
| 240 | 405 ✓ | 210 ✓ | 216.23 ✓ | 233.579362178548589456 | 233.5794 | 0.000037821451410544 | **yes** | 233.579362178548589456 — equal |
| 180 | 428 ✓ | 211 ✓ | 212.50 ✓ | **230.1410794878433773409** | 230.1412 | **0.0001205121566226591** | **no** | 230.1410794878433773409 — equal |
| 120 | 440 ✓ | 190 ✓ | 192.194 ✓ | 208.2308022961688662051 | 208.2308 | 0.0000022961688662051 | **yes** | 208.2308022961688662051 — equal |
| 90 | 380 ✓ | 164 ✓ | 156.723 ✓ | 171.86830345826790914045 | 171.8683 | 0.00000345826790914045 | **yes** | 171.86830345826790914045 — equal |
| 60 | 271 ✓ | 99 ✓ | 102.581 ✓ | **114.107227667538293020748** | 114.1073 | **0.000072332461706979252** | **no** | 114.107227667538293020748 — equal |

**18 of V4 (a)'s 20 comparisons hold. `Σq` fails at `tau` 180 and at `tau` 60.**

**Why this is a wrong expectation and not a wrong file:**

1. The file hashes to the SHA-256 the TZ-15 report §12 gives for `tz15-observations.csv`.
2. TZ-15's own constants file hashes to the value that report prints in §5 and §12. It records
   `sum_q` equal to this file's `Σq` at 5 of 5 `tau`, to every one of its digits. That instrument
   computed `sum_q` from its in-memory selection, before it wrote the observations file.
3. Every other quoted value holds, and so do V4 (b)'s 15 re-derivations of TZ-15's constants (§4.1).

**The two quoted figures are not TZ-15's sums.** Each equals the TZ-15 report §7's six-decimal
`mean q` times `n`, rounded to four decimals:

- `tau` 180: `0.537713 × 428 = 230.141164` → `230.1412`.
- `tau` 60: `0.421060 × 271 = 114.107260` → `114.1073`.

At 240 and 120 the same product gives `233.5793` and `208.2309`, where the report prints the true sums
rounded, `233.5794` and `208.2308`. At 90 both routes give `171.8683`.

**Why no implementation passes it.**

- The assertion compares a sum over a file whose bytes are fixed by hash with two literals it misses by
  2.4 and 1.4 times the tolerance.
- Any file that satisfied it would, by §3.1, not be the file §3.1 locates.
- Contract §2: "An unsatisfiable specification is answered with a BLOCKED report and a full stop."
- Contract §6: "A red test is either a product defect or a defective expectation. Both stop the run and
  both require a new TZ."

**The stop comes before the build**, as TZ-10, TZ-10a and TZ-11 stopped. The assertion is step 4 of
§5.1, after steps 0 to 3 open nothing but the recorder's `runtime.jsonl`, and its outcome does not
depend on any code this TZ would have written.

---

## 3. Evidence

The evidence is one scratch script outside the repository, `/root/tz16-work/scratch/evidence-v4a.py`.

- It applies §3.1 and §3.2 exactly as written.
- It re-derives V4 (b) through the committed `tz15.crit` and `tz15.pb_upper`. It loaded them from
  `research/tz15-phase2-gate.py` in a checkout of `86b51a4`, whose SHA-256 is map §0's `66ac0ae0…`.
- It computes none of TZ-16's own quantities.
- Through an audit hook, it asserts that it opened nothing under `/var/lib/btc-recorder/` or
  `/var/lib/btc-chainbook/`.
- It is **evidence for a stop, not a delivered check.** Its comparisons are printed, not asserted. It
  asserts only two things: that each `Decimal` sum of `q` equals its exact rational sum, and that it
  opened no capture file.

| file | lines | bytes | SHA-256 |
|---|---|---|---|
| `/root/tz16-work/scratch/evidence-v4a.py` | 131 | 6,029 | `d46753a35d2c56c8e947ced7d945410b3e6c8d89392a81ab53f74ac07b0eba71` |
| `/root/tz16-work/scratch/evidence-v4a.out` | 31 | 2,348 | `cc1b47384e338b407e98a388e2162e3f018590c5e020fbcd984b5c3b6fad1588` |

It was run as `/root/tz01-env/venv/bin/python -B evidence-v4a.py > evidence-v4a.out`, exit `0`.

### The output, verbatim

```
regular files hashed under /root/tz15-work: 182
tz15-observations.csv a7ac8a495e00e21cd34af6ead7f05e9a2b741231c928bb61d4ec03ec0e610ce6: 2 copies; read /root/tz15-work/run1/tz15-observations.csv
tz15-constants.json e6a93f9371e9fb32404482dac7b542c330399117ba0cf93e466b846e5878dfd3: 5 copies; read /root/tz15-work/dev1/tz15-constants.json
observations file: 940729 bytes, 6001 lines
columns: 18

tau | n | sum y | sum a | sum q (60-digit Decimal) | quoted | |sum q - quoted| | within 0.00005 | TZ-15's own sum_q in tz15-constants.json
240 | 405 True | 210 True | 216.23 True | 233.579362178548589456 | 233.5794 | 0.000037821451410544 | True | 233.579362178548589456 (equal to the file's: True)
180 | 428 True | 211 True | 212.50 True | 230.1410794878433773409 | 230.1412 | 0.0001205121566226591 | False | 230.1410794878433773409 (equal to the file's: True)
120 | 440 True | 190 True | 192.194 True | 208.2308022961688662051 | 208.2308 | 0.0000022961688662051 | True | 208.2308022961688662051 (equal to the file's: True)
90 | 380 True | 164 True | 156.723 True | 171.86830345826790914045 | 171.8683 | 0.00000345826790914045 | True | 171.86830345826790914045 (equal to the file's: True)
60 | 271 True | 99 True | 102.581 True | 114.107227667538293020748 | 114.1073 | 0.000072332461706979252 | False | 114.107227667538293020748 (equal to the file's: True)

V4 (a) comparisons: 18 of 20 hold; failing: ['sum q at tau 180', 'sum q at tau 60']

the quoted sum q against round(report mean q x n, 4):
  240: 0.576739 x 405 = 233.579295 -> 233.5793; quoted 233.5794
  180: 0.537713 x 428 = 230.141164 -> 230.1412; quoted 230.1412
  120: 0.473252 x 440 = 208.230880 -> 208.2309; quoted 208.2308
  90: 0.452285 x 380 = 171.868300 -> 171.8683; quoted 171.8683
  60: 0.421060 x 271 = 114.107260 -> 114.1073; quoted 114.1073

V4 (b) through tz15.crit([a ...], D('0.01')) and tz15.pb_upper([q ...]):
  240: s* 238 True | FP 0.007476034950200 True | POWER(s*) 0.325739887 True
  180: s* 232 True | FP 0.008749059108653 True | POWER(s*) 0.432618207 True
  120: s* 210 True | FP 0.007886034791558 True | POWER(s*) 0.430438487 True
  90: s* 173 True | FP 0.006740872863538 True | POWER(s*) 0.459935046 True
  60: s* 115 True | FP 0.008611872632895 True | POWER(s*) 0.467275598 True
V4 (b) comparisons: 15 of 15 hold

opens under either capture root during this probe: 0
```

### The script, verbatim

```python
# TZ-16 BLOCKED evidence, scratch only, never committed. It checks TZ-16 section 3.2 / V4 (a)
# and V4 (b) against TZ-15's two files as TZ-16 section 3.1 locates them. It computes none of
# TZ-16's own quantities: no rho, no f, no set, no quote, no label of the reserved span.
import decimal
import hashlib
import json
import os
import stat
import sys
from fractions import Fraction

OPENS = []


def _hook(event, args):
    if event == "open" and args and isinstance(args[0], str):
        path = os.path.abspath(args[0])
        if path.startswith(("/var/lib/btc-recorder/", "/var/lib/btc-chainbook/")):
            OPENS.append(path)


sys.addaudithook(_hook)

WORK = "/root/tz15-work"
OBS_SHA = "a7ac8a495e00e21cd34af6ead7f05e9a2b741231c928bb61d4ec03ec0e610ce6"
CON_SHA = "e6a93f9371e9fb32404482dac7b542c330399117ba0cf93e466b846e5878dfd3"
TAUS = (240, 180, 120, 90, 60)
# TZ-16 section 3.2, quoted from the TZ-15 report sections 4 and 7.
WANT_N = dict(zip(TAUS, (405, 428, 440, 380, 271)))
WANT_Y = dict(zip(TAUS, (210, 211, 190, 164, 99)))
WANT_A = dict(zip(TAUS, ("216.2300", "212.5000", "192.1940", "156.7230", "102.5810")))
WANT_Q = dict(zip(TAUS, ("233.5794", "230.1412", "208.2308", "171.8683", "114.1073")))
TOL_Q = "0.00005"
# TZ-16 V4 (b), quoted from the TZ-15 report section 5.
WANT_S = dict(zip(TAUS, (238, 232, 210, 173, 115)))
WANT_FP = dict(zip(TAUS, ("0.007476034950", "0.008749059109", "0.007886034792",
                          "0.006740872864", "0.008611872633")))
WANT_POW = dict(zip(TAUS, ("0.325740", "0.432618", "0.430438", "0.459935", "0.467276")))
# The TZ-15 report section 7's "mean q" column, six decimals, for the arithmetic of its origin.
REPORT_MEAN_Q = dict(zip(TAUS, ("0.576739", "0.537713", "0.473252", "0.452285", "0.421060")))

# Section 3.1: every regular file under the work root, by hash; the first in sorted path order.
found = {OBS_SHA: [], CON_SHA: []}
hashed = 0
for dirpath, dirnames, filenames in os.walk(WORK):
    dirnames.sort()
    for name in sorted(filenames):
        path = os.path.join(dirpath, name)
        if not stat.S_ISREG(os.lstat(path).st_mode):
            continue
        hashed += 1
        with open(path, "rb") as fh:
            digest = hashlib.sha256(fh.read()).hexdigest()
        if digest in found:
            found[digest].append(path)
print("regular files hashed under %s: %d" % (WORK, hashed))
for digest, label in ((OBS_SHA, "tz15-observations.csv"), (CON_SHA, "tz15-constants.json")):
    paths = sorted(found[digest])
    print("%s %s: %d copies; read %s" % (label, digest, len(paths), paths[0] if paths else None))
obs_path, con_path = sorted(found[OBS_SHA])[0], sorted(found[CON_SHA])[0]
with open(obs_path, "rb") as fh:
    body = fh.read()
print("observations file: %d bytes, %d lines" % (len(body), body.count(b"\n")))

# Section 3.2's read, in Decimal at 60 digits, with an exact rational beside it.
decimal.getcontext().prec = 60
D = decimal.Decimal
lines = body.decode("utf-8").splitlines()
head = lines[0].split(",")
ix = {n: i for i, n in enumerate(head)}
print("columns: %d" % len(head))
rows = [l.split(",") for l in lines[1:]]
with open(con_path, encoding="utf-8") as fh:
    con = json.load(fh)
print()
print("tau | n | sum y | sum a | sum q (60-digit Decimal) | quoted | |sum q - quoted| | within %s"
      " | TZ-15's own sum_q in %s" % (TOL_Q, os.path.basename(con_path)))
fails = []
for tau in TAUS:
    sel = sorted((r for r in rows if int(r[ix["tau"]]) == tau and r[ix["selected"]] == "1"),
                 key=lambda r: int(r[ix["T0"]]))
    n = len(sel)
    sy = sum(int(r[ix["y"]]) for r in sel)
    sa = sum((D(r[ix["a"]]) for r in sel), D(0))
    sq = sum((D(r[ix["q"]]) for r in sel), D(0))
    assert Fraction(sq) == sum(Fraction(r[ix["q"]]) for r in sel), "Decimal sum is not exact"
    dist = abs(sq - D(WANT_Q[tau]))
    ok = {"n": n == WANT_N[tau], "sum y": sy == WANT_Y[tau], "sum a": sa == D(WANT_A[tau]),
          "sum q": dist <= D(TOL_Q)}
    fails += ["%s at tau %d" % (k, tau) for k, v in ok.items() if not v]
    theirs = con["per_tau"][str(tau)]["sum_q"]
    print("%d | %d %s | %d %s | %s %s | %s | %s | %s | %s | %s (equal to the file's: %s)"
          % (tau, n, ok["n"], sy, ok["sum y"], sa, ok["sum a"], sq, WANT_Q[tau], dist,
             ok["sum q"], theirs, D(theirs) == sq))
print()
print("V4 (a) comparisons: %d of 20 hold; failing: %s" % (20 - len(fails), fails))
print()
print("the quoted sum q against round(report mean q x n, 4):")
for tau in TAUS:
    prod = D(REPORT_MEAN_Q[tau]) * WANT_N[tau]
    print("  %d: %s x %d = %s -> %s; quoted %s" % (tau, REPORT_MEAN_Q[tau], WANT_N[tau], prod,
                                                 prod.quantize(D("0.0001")), WANT_Q[tau]))

# V4 (b): TZ-15's constants re-derived through the committed tz15.crit and tz15.pb_upper.
sys.path.insert(0, "/root/tz16-work/wt/research")
import importlib.util  # noqa: E402
spec = importlib.util.spec_from_file_location(
    "tz15phase2gate", "/root/tz16-work/wt/research/tz15-phase2-gate.py")
tz15 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tz15)
print()
print("V4 (b) through tz15.crit([a ...], D('0.01')) and tz15.pb_upper([q ...]):")
held = 0
for tau in TAUS:
    sel = sorted((r for r in rows if int(r[ix["tau"]]) == tau and r[ix["selected"]] == "1"),
                 key=lambda r: int(r[ix["T0"]]))
    a = [tz15.D(r[ix["a"]]) for r in sel]
    q = [tz15.D(r[ix["q"]]) for r in sel]
    s_star, fp, _ = tz15.crit(a, tz15.D("0.01"))
    power = tz15.pb_upper(q)[s_star]
    c1 = s_star == WANT_S[tau]
    c2 = abs(fp - tz15.D(WANT_FP[tau])) <= tz15.D("5e-13")
    c3 = abs(power - tz15.D(WANT_POW[tau])) <= tz15.D("5e-7")
    held += c1 + c2 + c3
    print("  %d: s* %d %s | FP %s %s | POWER(s*) %s %s"
          % (tau, s_star, c1, fp.quantize(tz15.D("1e-15")), c2,
             power.quantize(tz15.D("1e-9")), c3))
print("V4 (b) comparisons: %d of 15 hold" % held)
print()
print("opens under either capture root during this probe: %d" % len(OPENS))
assert not OPENS, OPENS
```

The checkout the script loaded `tz15` from, `/root/tz16-work/wt`, was removed after the run (§5). Any
checkout of `86b51a4` holds the same `research/tz15-phase2-gate.py`, byte for byte.

---

## 4. Found in the same reading — not the blocker

### 4.1 The rest of V4 (a), and V4 (b)

- **V4 (a):** `n`, `Σy` and `Σa` hold at 5 of 5 `tau` each, and `Σq` at 240, 120 and 90. That is 18 of
  20 comparisons (§2).
- **V4 (b): 15 of 15 hold.** At every `tau`, `tz15.crit([a …], D("0.01"))` returns the quoted `s*`, and
  `FP` lies within `D("5e-13")` of the quoted value. `tz15.pb_upper([q …])` at `s*` lies within
  `D("5e-7")` (§3's output). The closest margins are `4.62e-13` at `tau` 90 and `4.42e-13` at 120,
  against `5e-13`, and `4.87e-7` at 120, against `5e-7`.
- These are TZ-15's constants re-derived from its own file. They are not quantities of TZ-16, and they
  support §2's point 3.

### 4.2 §5.2's 78 expectations reproduce under an independent computation

This comes from a second scratch probe, `/root/tz16-work/scratch/probe_selftests.py`: 68 lines, 3,246
bytes, SHA-256 `848ad2c0eb34fa5d43701164e7960b6120f740621b82b0351366d8d24589485f`.

- It writes `U` by enumerating outcomes, and the binomials from `math.comb`.
- It writes `up`, `low`, the two critical searches, the dependence statistic and Fisher's test in exact
  rationals, from §3.2, §3.7, §3.10 and §4.3's own definitions.
- It shares nothing with any instrument, and it reads nothing but its own literals.
- **It is recorded, not asserted.** No self-test was built.

Its output, saved as `probe_selftests.out` (19 lines, 1,232 bytes, SHA-256
`8a16bacea2d8635b572ffefbe211b06193b98c31b9631d6a9f5b318f31319ec4`):

```
item1 U [Fraction(1, 1), Fraction(61, 64), Fraction(45, 64), Fraction(19, 64), Fraction(3, 64)]
item1 up ['1', '1', '61/64', '45/64', '19/64', '3/64', '0']
item1 low ['0', '3/64', '19/64', '45/64', '61/64', '1', '1']
item2 (17, Fraction(1351, 1048576)) 1549/262144 1351/1048576 1549/262144
item3 (18, Fraction(1351, 1048576)) 1549/262144 17 16
item4 r=1 (9, Fraction(53731317297, 95367431640625)) 247462024753/95367431640625 53731317297/95367431640625 247462024753/95367431640625
item4 r=1.1 (8, Fraction(53731317297, 95367431640625)) 247462024753/95367431640625 9 10
item5a (4, Fraction(0, 1)) 729/1000
item5b (-1, Fraction(0, 1)) 1/8
item6 17 9 1351/1048576 53731317297/95367431640625 39238821216256/95367431640625 39238821216256/95367431640625 215955/524288 215955/524288
item7a ([Fraction(9, 16), Fraction(1, 8), Fraction(-5, 16)], Fraction(7, 4), Fraction(7, 4))
item7b ([Fraction(-7, 8), Fraction(3, 4), Fraction(-5, 8)], Fraction(-1, 2), Fraction(1, 1))
item7c ([Fraction(837, 68824), Fraction(-10645, 17206), Fraction(165, 9832)], Fraction(-1544, 8603), Fraction(1, 1))
item9 (3, 10, 0, 20) 6/203 HOLD
item9 (4, 10, 0, 20) 2/261 FIRE
item9 (2, 10, 1, 20) 51/203 HOLD
item9 (0, 10, 0, 20) 1 HOLD
item10 4 53/64
sqrt 1.1 True
```

- **Items 1 to 7, 9 and 10:** every numeric expectation §5.2 prints appears in this output. That covers
  item 1's fourteen `up` and `low` values, every critical count of items 2 to 6 with its tail, the two powers,
  item 7's nine `ρ`, three `f̂` and three `f`, the four `p_I` with their readings, `k* = 4` and
  `53/64`.
- `D("1.21").sqrt()` equals `D("1.1")` at 60 digits, which item 3's first assertion needs.
- **Items 8 and 11** are exact by construction, as §10 C2 says. Item 11's guard is the committed
  `tz15.label_free`, whose same four cases TZ-15's own self-test item 6 passed.

### 4.3 Points in the text a successor would meet — none was needed for this stop

Each is stated with where it sits. None was resolved.

1. **§1 cites "map §3, §9" for the reclaiming of the two trees.** The map has sections 0 to 8. §10 C8
   resolves "§9" as this TZ's own §9.
2. **§5.2 item 9 asserts "the interlock reading" beside `fisher_upper`.**
   - §5.1's function list carries the reading only inside `interlock`, which opens `window.json` and
     `runtime.jsonl`.
   - §5.1 step 2 runs the self-tests before any chain book file is opened.
3. **V8 is "asserted, steps 0 and 14".** A run without `--score` stops at step 11, so V8's run-end half
   has no step in those runs.
4. **§0.6 counts "this TZ's two uploads" above PR #19's merge and the map's upload.** The first-parent
   line also carries `cc92085`, the deletion between them (§1.4).
5. **§3.9's own-look statistic is "§3.2's `ρ_1`, `ρ_2`, `ρ_3`, `f̂` and `f` recomputed".** §3.2 asserts
   `n >= 4` and `v > 0` at every `tau`. An assertion there, reached after step 12, would stop a scored
   run after its label read.

---

## 5. What was not done, and what stayed on the host

- **No instrument.** `research/tz16-phase2-decisive-gate.py` does not exist anywhere. Consequently:
  - V1 to V13 have nothing to act on.
  - §0.1's step-0 assertion and §5.1's order never ran.
  - The fingerprint of §0 comes from a scratch script, so it is recorded, not asserted.
- **The branch and its worktree:**
  - At start-up, `git worktree add -b tz-16-phase2-decisive-gate /root/tz16-work/wt origin/main` created
    them, and `git worktree add --detach /root/tz16-work/wt-report origin/main` created the report
    checkout.
  - After the probes, `git -C /root/tz16-work/wt status --porcelain --untracked-files=all` printed
    nothing. `HEAD` was still `86b51a4`, and `git log origin/main..tz-16-phase2-decisive-gate` held
    **0** commits.
  - `git worktree remove /root/tz16-work/wt` then exited `0`, without `--force`, and
    `test -e /root/tz16-work/wt` exited `1`.
  - `git branch -d tz-16-phase2-decisive-gate` exited `0`: "Deleted branch tz-16-phase2-decisive-gate
    (was 86b51a4)."
  - Afterwards `git branch --list 'tz-16*'` and `git ls-remote origin 'refs/heads/tz-16*'` both print
    nothing.
  - The branch never held a commit of its own and was never pushed.
- **§9's retention did not run.** It runs "only after S2 and V3", and neither exists:
  - `/root/tz15-work/` holds its 182 regular files. They include both of §3.1's files, 2 and 5 copies
    by hash, and its label ledger. Its worktrees `wt` and `wt-report` are registered.
  - `/root/tz18a-work/` and its two worktrees are untouched.
  - `/root/btc-forensics/` holds `1,046` files at the opening and closing reads.
  - `/root/tz18a-svc/` was not touched.
- **The capture and the chain book:**
  - This session opened, under `/var/lib/btc-recorder/`, every `manifest.json` the series held at
    07:47:08Z, through §0.8's command. It opened the recorder's top-level `runtime.jsonl` twice, through
    `grep -c` at the host gate and at the closing read. Nothing else was opened there, and no interval
    directory's own `runtime.jsonl` was read.
  - Nothing under `/var/lib/btc-chainbook/` was opened.
  - Nothing was written under either root. Neither process was signalled.
- **`/root/tz16-work/`** is the next TZ's to reclaim. It holds the report checkout
  `/root/tz16-work/wt-report`, at `86b51a4` plus this report, and the files below. Every probe ran
  with `python -B`. Outside `/root/tz16-work/`, nothing was created or modified except:
  - this report on `main`;
  - git's own records of the worktrees and branch in `.git`;
  - the session store `/root/.claude`;
  - the contract §1 fast-forward of the primary checkout `/root/btc-5m-twap`, from `3a95ae1` to
    `86b51a4`.

  That fast-forward changed four paths: the TZ-18a report, this TZ,
  `SYSTEM-MAP.md` and `research/tz18a-chainbook-capture.py`. It changed none under `research/recorder/`,
  where the recorder runs, and it switched no branch, so §0.7 holds.

| file | lines | bytes | SHA-256 | what it is |
|---|---|---|---|---|
| `logs/r-ready.txt` | 87 | 3,719 | `4ac9a6f5d32cfdd593d4259086302076ae3f3e18872682ae3df0c0c032872c60` | §0.2, §0.8, §0.5 read 1 and §0.6, as printed |
| `logs/closing-read.txt` | 38 | 1,404 | `fd000a0835f1eeb7d8814c1feeb73afaebf6ea0c7c1dc66efdac0e821e763eb1` | §1.6's closing read, as printed |
| `scratch/probe_selftests.py` | 68 | 3,246 | `848ad2c0eb34fa5d43701164e7960b6120f740621b82b0351366d8d24589485f` | §4.2's independent check of §5.2 |
| `scratch/probe_selftests.out` | 19 | 1,232 | `8a16bacea2d8635b572ffefbe211b06193b98c31b9631d6a9f5b318f31319ec4` | its output |
| `scratch/probe_tz15files.py` | 31 | 1,829 | `f9c533417d3044e6d0a6eec5995328f38c4bb370b271382b2528c20e22d583c3` | the first probe of TZ-15's files — see below |
| `scratch/probe_sumq.py` | 12 | 890 | `6dec26af59fe0836fdb0e31ce995ca91d10482c46bbf193d70460bd01fd9ad45` | the second: `Σq` in exact rationals against the quoted values |
| `scratch/evidence-v4a.py` | 131 | 6,029 | `d46753a35d2c56c8e947ced7d945410b3e6c8d89392a81ab53f74ac07b0eba71` | §3's evidence |
| `scratch/evidence-v4a.out` | 31 | 2,348 | `cc1b47384e338b407e98a388e2162e3f018590c5e020fbcd984b5c3b6fad1588` | its output |
| `scratch/fingerprint.py` | 27 | 1,270 | `31b0ce335cc12854c86bc9eddb00067773ccbdd92ff396329ac0dcd1f4c0f301` | §0's table |
| `scratch/check-report.py` | 17 | 1,208 | `96a4f2d101e415941817ac10e57f13a76ae06194380a463ef560989bfaae6c55` | checks that each verbatim block here equals its source file, and that each row of this table is current |

**Disclosed: what the first probe computed.**

- `probe_tz15files.py` found the blocker first. Beside V4 (a) and V4 (b), it also computed §3.2's
  `ρ_1`, `ρ_2`, `ρ_3`, `f̂` and `f` from TZ-15's file at each `tau`.
- That read is §2 item 6's exemption (c): TZ-15's outcomes, below the reserve.
- Its output went to the terminal only and was not saved. **None of those values is reported here**,
  because contract §9 bars partial measurements from a BLOCKED report. They are re-derivable from
  TZ-15's file by §3.2's definition.
- The probe's module load is the same `tz15` chain `evidence-v4a.py` loads under its audit hook, and
  that chain opened nothing under either capture root.
- `probe_sumq.py` printed the same `Σq` comparison §3 prints, and nothing else.

---

## 6. Publication

- **This report is the one path this TZ pushes to `main`**, in one commit from
  `/root/tz16-work/wt-report`, as §2 item 2 and contract §4.1 require.
- **No branch, implementation commit, pull request or Release exists**, so contract §5's publication
  steps have nothing to publish.
- The §4.2 self-check's first two lines name an implementation commit and a branch on `origin`. There
  is neither, and what stands in their place is below:

```
$ git ls-remote origin 'refs/heads/tz-16*'
(no output)

$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
(no output)
```

No dataset, archive or binary is in git history. **The capture was never touched, and nothing of the
reserved span was read.**
