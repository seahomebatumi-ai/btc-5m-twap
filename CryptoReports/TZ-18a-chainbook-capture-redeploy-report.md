# TZ-18a report — the chain book capture, redeployed

**READING P-START: served.** Both venue endpoints answered `200` to §3.2's request from this
host, before the service started: the fifteen-minute document in `5,364` bytes and the order
book in `3,456` bytes, each parsing as JSON.

**READING G-DEPLOY: PASS** — complete **14 of the first 14** qualifying checkpoints; incomplete 0, missed 0. Every one of the 84 book reads of the three considered windows returned `200` and parsed as JSON; the largest skew is `28,425,839` ns = `0.0284` s, 35x inside the bound.

**READING G-TIERC: PASS** — **2** counted fully loaded exposed intervals of the 2 counted, which is exactly the PASS minimum; **0** counted exposed intervals whose `quotes_complete` is not `true`. The control window carries no load and reads `true` at 7 of 7.

**The service is still running.** The pair of readings is (PASS, PASS), so §6 R5 does not run and block K-18a was never authorized. Verified by the Executor at the session's end, never from an account: `pgrep -fx` with `SERVICE_ARGV` printed exactly one line, `2699889`, and exited `0`; `/var/lib/btc-chainbook/service.pid` reads `2699889`; `/proc/2699889/cmdline` is `SERVICE_ARGV` NUL-joined, byte for byte; and `runtime.jsonl` holds exactly one `start` record written in this session, pid `2699889`, with no `stop` after it.

| field | value |
|---|---|
| TZ | `CryptoTZ/TZ-18a-chainbook-capture-redeploy.md`, SHA-256 `b989a1d32ee66cf7c95495773484037e9399542829b311045f6e938637001ba1` |
| map revision | `2026-09-23-a`, equal; anchors 6 of 6; re-derived 4 of 4; rows hashed 25 of 25; `frozen` equal 23 of 23 |
| branch | `tz-18a-chainbook-capture` at `ca4bbc1dd583cbb62f3c0c985938d229b526ce7e`, pushed, unmerged |
| file added | `research/tz18a-chainbook-capture.py`, SHA-256 `e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae`, 1,683 lines, 69,357 bytes |
| derived from | `8caa0b4:research/tz18-chainbook-capture.py`, SHA-256 `33753b2b…`, 1,420 lines, 57,409 bytes |
| pricer | not read, not called, not scored; `A6` `729f0bcdbee3` is stated so that what was not scored is not in doubt |

Nothing here measures a price. No settled market document was requested or read.

---
## 0. Fingerprint

**Revision string read:** `2026-09-23-a` — equal to the value TZ-18a's header requires.

| anchor | required | read from the map | re-derived from the file | verdict |
|---|---|---|---|---|
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` | not a file anchor | equal |
| `A2` — collector | `6c5089330629` | `6c5089330629` | `6c5089330629` | equal |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-undecidable-5tau` | same | not a file anchor | equal |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b` | `437b45ea196b` | equal |
| `A5` — recorder | `9fd1c7de0f74` | `9fd1c7de0f74` | `9fd1c7de0f74` | equal |
| `A6` — pricer | `729f0bcdbee3` | `729f0bcdbee3` | `729f0bcdbee3` | equal |

### 0.1 The 26 rows of the map's §0 table

| path | lines | bytes | state | SHA-256 | verdict |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 936 | 178,241 | reported | `704070149009b9581de1210d371d0edba9f3dc9a608151a90d0498d31d447b00` | self-reference, reported |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | **equal** |
| `research/twap-divergence.py` | 1,135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | **equal** |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | **equal** |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | tracked, no expectation |
| `research/pfair.py` | 441 | 19,357 | frozen | `729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68` | **equal** |
| `research/selftest-pfair.py` | 619 | 32,559 | frozen | `b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa` | **equal** |
| `research/tz06-calibration.py` | 577 | 27,138 | frozen | `715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f` | **equal** |
| `research/tz07a-variance-time.py` | 623 | 28,414 | frozen | `513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771` | **equal** |
| `research/tz07b-settlement-dispersion.py` | 515 | 24,926 | frozen | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` | **equal** |
| `research/tz08a-out-of-sample.py` | 745 | 38,822 | frozen | `37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c` | **equal** |
| `research/tz09-disk-inventory.py` | 894 | 41,004 | frozen | `b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6` | **equal** |
| `research/tz10b-sigma-or-link.py` | 1,224 | 61,018 | frozen | `406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088` | **equal** |
| `research/tz11a-student-link.py` | 1,231 | 64,732 | frozen | `0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839` | **equal** |
| `research/tz12-sized-gate.py` | 1,157 | 61,637 | frozen | `d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999` | **equal** |
| `research/tz13-sized-gate-test3.py` | 1,074 | 53,901 | frozen | `a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd` | **equal** |
| `research/tz14-quote-inventory.py` | 2,124 | 109,972 | frozen | `978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02` | **equal** |
| `research/tz15-phase2-gate.py` | 1,517 | 73,799 | frozen | `66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3` | **equal** |
| `research/tz17-settlement-chain.py` | 1,102 | 38,622 | frozen | `e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92` | **equal** |
| `research/recorder/recorder.py` | 608 | 25,658 | frozen | `9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03` | **equal** |
| `research/recorder/config.py` | 112 | 4,773 | frozen | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | **equal** |
| `research/recorder/manifest.py` | 254 | 10,002 | frozen | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | **equal** |
| `research/recorder/analyze.py` | 813 | 34,705 | frozen | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` | **equal** |
| `research/recorder/probe.py` | 227 | 9,324 | frozen | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | **equal** |
| `research/recorder/selftest.py` | 573 | 30,591 | frozen | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` | **equal** |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | tracked, no expectation |

Rows in the table: **26**; hashed: **25**; `frozen`: **23**, all **23** equal; `tracked`: 2; the self-reference row: 1.
`SYSTEM-MAP.md` itself: SHA-256 `704070149009b9581de1210d371d0edba9f3dc9a608151a90d0498d31d447b00`, 936 lines, 178,241 bytes — the value §10's pre-send
check names as `704070149009…`, and byte-equal to the project copy.

### 0.2 Host gate — the opening reads, verbatim

```
$ df -B1 --output=source,size,avail /var/lib/btc-recorder
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 13427335168

$ find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json

$ pgrep -fx '/root/tz04a-env/venv/bin/python -B -u recorder.py'; echo "exit=$?"
228592
exit=0

$ grep -rl --include=runtime.jsonl 4216c04673ced76b5b2ac60ef57c9abedc46f9b9 /var/lib/btc-recorder | head -n 1
/var/lib/btc-recorder/btc-updown-5m/1789488300/runtime.jsonl

$ du -sb /root/PROJECT_GAMING_PS5
409118861	/root/PROJECT_GAMING_PS5

$ systemctl is-enabled telemetry-watch.service; echo "exit=$?"
disabled
exit=1

$ systemctl is-active telemetry-watch.service; echo "exit=$?"
inactive
exit=3

$ for d in /root/tz15-work /root/tz17-work /root/tz18-work /root/tz18-svc /root/tz18a-work /root/tz18a-svc; do test -e "$d"; echo "$d exit=$?"; done
/root/tz15-work exit=0
/root/tz17-work exit=0
/root/tz18-work exit=0
/root/tz18-svc exit=0
/root/tz18a-work exit=1
/root/tz18a-svc exit=1

$ find /root/btc-forensics -type f | wc -l
211

$ git worktree list
/root/btc-5m-twap          3a95ae1 [main]
/root/tz15-work/wt         f7f171a [tz-15-phase2-gate]
/root/tz15-work/wt-report  c729008 (detached HEAD)
/root/tz17-work/wt         8f1bc93 [tz-17-settlement-chain]
/root/tz17-work/wt-report  c4f2099 (detached HEAD)
/root/tz18-work/wt         8caa0b4 [tz-18-chainbook-capture]
/root/tz18-work/wt-report  202b791 (detached HEAD)
```

| condition | required | read | verdict |
|---|---|---|---|
| **H1** | `find` prints exactly one path | one path, `/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json` | **holds** |
| **H2** | `pgrep -fx` prints exactly one line and `exit=0` | one line, `228592`, `exit=0` | **holds** |
| **H3** | `df` source `/dev/vda2`, size `31612203008` | `/dev/vda2`, `31612203008` | **holds** |
| resource gate | `avail >= 2,200,000,000` | `13,427,335,168` | **holds**, 6.1× the floor |
| trees | `/root/tz17-work` and `/root/tz18-work` exit `0`; `/root/tz18a-work` and `/root/tz18a-svc` exit `1` | `0`, `0`, `1`, `1` | **holds** |
| forensic store | exactly `211` files | `211` | **holds** |

`/root/tz15-work` exits `0` — TZ-16's, untouched. `/root/tz18-svc` exits `0` — §9 reclaims it.
`du -sb /root/PROJECT_GAMING_PS5` is `409,118,861` bytes; `telemetry-watch.service` is `disabled`
(`exit=1`) and `inactive` (`exit=3`); `git worktree list` shows seven entries, the main checkout and
six worktrees. None of the last four carries a threshold.

The three reads H1, H3 and the `grep` over `runtime.jsonl` — which returned the single path
`/var/lib/btc-recorder/btc-updown-5m/1789488300/runtime.jsonl` — are the map §6 host-identity row,
and they agree with it.

### 0.3 Repository reads

```
$ git ls-tree -r --name-only origin/main | grep -c '^CryptoReports/TZ-18-chainbook-capture-deploy-report.md$'
1
$ git ls-tree -r --name-only origin/main | grep -c '^research/tz18a-chainbook-capture.py$'
0
$ git ls-tree -r --name-only origin/main | grep -c '^research/tz18-chainbook-capture.py$'
0
$ git ls-remote origin refs/heads/tz-18a-chainbook-capture | wc -l
0
$ git show 8caa0b41d5cdf9e74e92b11d4317d59a2ee7b567:research/tz18-chainbook-capture.py | sha256sum
33753b2bb1e322a081e6cba8bad976268e2d6046dc350e6ceae3e748ad6e4bfe  -
$ git show origin/main:CryptoTZ/TZ-18a-chainbook-capture-redeploy.md | sha256sum
b989a1d32ee66cf7c95495773484037e9399542829b311045f6e938637001ba1  -
```

The TZ-18 report count is `1`; the `tz18a` path count `0`; the `ls-remote` count `0`; the base
blob hashes to `33753b2b…`, the value §0.3 requires. The `tz18-` path count is `0`, so PR #18 is
still unmerged, as map §1 records. This TZ's own hash is printed for the Architect's comparison.

`origin/main` at the fetch was `3a95ae1`, one commit past the `fda5eb6` of §10's pre-send check:
`3a95ae1` is an upload commit that left `SYSTEM-MAP.md` byte-identical — its SHA-256 is the
`704070149009…` §10 names.

### 0.4 The TZ-18 service — stopped, verified from its own record

```
$ pgrep -fx '/root/tz01-env/venv/bin/python -B -u /root/tz18-svc/tz18-chainbook-capture.py --serve'; echo "exit=$?"
exit=1
$ test -e /proc/2608993; echo "proc exit=$?"
proc exit=1
```

Every record in `/var/lib/btc-chainbook/runtime.jsonl` before this session — counts, times and ids
only, the map §2.5 exception:

| # | event | pid | `wall_ns` | UTC | commit | `file_sha256` |
|---|---|---|---|---|---|---|
| 1 | `start` | 2608993 | 1790117616052072857 | 2026-09-22T22:53:36.052073Z | `8caa0b41d5cdf9e74e92b11d4317d59a2ee7b567` | `33753b2bb1e322a081e6cba8bad976268e2d6046dc350e6ceae3e748ad6e4bfe` |
| 2 | `stop` | 2608993 | 1790145840007723380 | 2026-09-23T06:44:00.007723Z | — | — |

- **K0** — `pgrep` printed no line and exited `1`. **Holds**; block K-18 was never authorized and
  never run. The `/proc/2608993` read agrees but does not decide.
- **K1** — exactly one `start` record carries pid `2608993`, with `wall_ns`
  `1790117616052072857`, commit `8caa0b4…` and `file_sha256` equal to the base blob's hash of
  §0.3. **Holds.**
- **K2** — a `stop` record carries pid `2608993` and `wall_ns` `1790145840007723380`, later than
  that start's by `28,223,955,650,523` ns — 7 h 50 m 24 s. **Holds.**
  **`K_stop` = `1790145840007723380` ns = 2026-09-23T06:44:00.007723Z.**

R1 ran at `1790185179`, which is `K_stop` + `39,339` s — more than the `900` s §6 R1 requires, so
no window directory this service opens could already exist.

**Window directories under `/var/lib/btc-chainbook/` at the opening read, by name only:** `32`
directories, the smallest `1790117100`, the largest `1790145000`. Nothing inside any of them was
opened. Beside them the root holds `runtime.jsonl`, `service.log` and `service.pid`.

### 0.5 The diagnostic slug — a disclosure, not a block

Every regular file under `/root/tz18-work/` not beneath `wt/` or `wt-report/`, sorted by path,
with bytes and SHA-256 — **30 files**:

| bytes | SHA-256 | path |
|---|---|---|
| 1,543 | `4dbcea4b996aac4326114475effc46a84eb6fd6c0b9b1f31173c05657cece650` | `/root/tz18-work/R1.log` |
| 6,369 | `1f25ef50d93dfcb5ef272099cd3db4c10e6727f3590917357308cb90a45cae56` | `/root/tz18-work/R4.log` |
| 1,543 | `baa5370fde714c96dd2d8efc1bcc4f3f66ad4b5915cf955f7744fb924f77edd1` | `/root/tz18-work/R6.log` |
| 1,587 | `23c86372c0680273d8378c244817435af8945e013f711c1435a42659acc4b4f4` | `/root/tz18-work/host-close-block.md` |
| 232,762 | `0bbb345dc457768c387c45bb583035ce0074d6cdd432ff26b6a7e60f1bcb8e67` | `/root/tz18-work/predebug/tz18-verify.csv` |
| 787 | `76b12513e8772704d53589b0a09f329cb5d7c58362ef445b3e56a3ca136d3e3a` | `/root/tz18-work/predebug/tz18-verify.json` |
| 3,135 | `e36879a8d82828de6f80e9eacf65806a75988bd7419297b41904275d03ba749d` | `/root/tz18-work/preflight-fingerprint.txt` |
| 1,039 | `0311630949e413edc99bc656f6219efc3820f343ff4677e9affc26f1b673bdfe` | `/root/tz18-work/preflight-host-close.txt` |
| 1,030 | `4414105a8d3db98a0b275be505c715f0e4a9268a107d348422a905ee95f5a79b` | `/root/tz18-work/preflight-host-open.txt` |
| 899 | `7b9b95825ba938b55ac27ee2e793b95cc1308bcb4625cf7213684033413fc955` | `/root/tz18-work/preflight-repo.txt` |
| 131 | `1608e99c4bd10fd221758b32f7e4863d13a5dc06cd9a6602fc86b1b6a5210d15` | `/root/tz18-work/r1-head.txt` |
| 3,523 | `d825a8c05e175727394cfc72362831414e2b304e30a86f18c36e4fc6b7698c43` | `/root/tz18-work/report-fingerprint-rows.md` |
| 3,201 | `a3a8766000ad9f39974d95c6b030ce473ef1b0b7a5e99786164798d609a9be52` | `/root/tz18-work/report-head-top.md` |
| 3,060 | `de55ba74ee9a96bb3d04e326213c369400e2e76ec9009698fc70bd70528df45f` | `/root/tz18-work/report-head.md` |
| 5,518 | `6aa62eca4ee1dc7b52f2cba7a383b4c6648bfaa9f0ed8cc114bdd2ef34a85bcb` | `/root/tz18-work/report-sec0b.md` |
| 2,025 | `e847bc62c6098d3ce14038c9087d1f93c2d544537aab6a48688e2605785cf388` | `/root/tz18-work/report-sec1.md` |
| 464 | `bbdf5d08e0d7efe6eb018ab0642f73e47af0a8a860f5b539422ac37f6d66687c` | `/root/tz18-work/report-sec2-head.md` |
| 974 | `e389d24c9c9839e5e5074433ea980a4b7a1976dcb17a119d76c8d66d0aafdeaf` | `/root/tz18-work/report-sec2-tail.md` |
| 1,572 | `a7602fc363e331f383fec221dffda0473e694a53d8536bcc0bf97ff4a895b322` | `/root/tz18-work/report-sec3.md` |
| 5,359 | `a7b231e7cd84e20244d85322ba6d0109fd9cb380b743a00985923ecd1ebec754` | `/root/tz18-work/report-sec4.md` |
| 3,533 | `5f4800a20b1df11db512cf8cc457f4924ab280bea8f4bed9ac613cd597baed89` | `/root/tz18-work/report-sec5.md` |
| 7,060 | `338f40db1fe0ffa51509dcf6d2ab6585e87704570e8e70d4d40c339856b202bd` | `/root/tz18-work/report-sec6.md` |
| 232,762 | `0bbb345dc457768c387c45bb583035ce0074d6cdd432ff26b6a7e60f1bcb8e67` | `/root/tz18-work/run-1/tz18-verify.csv` |
| 787 | `76b12513e8772704d53589b0a09f329cb5d7c58362ef445b3e56a3ca136d3e3a` | `/root/tz18-work/run-1/tz18-verify.json` |
| 11,211 | `95b8f17324e39b23dd2872faa10d330a72f883ea4770b2ddd6942e2cde452ae1` | `/root/tz18-work/run-2/tz18-proof.json` |
| 232,762 | `0bbb345dc457768c387c45bb583035ce0074d6cdd432ff26b6a7e60f1bcb8e67` | `/root/tz18-work/run-3/tz18-verify.csv` |
| 787 | `76b12513e8772704d53589b0a09f329cb5d7c58362ef445b3e56a3ca136d3e3a` | `/root/tz18-work/run-3/tz18-verify.json` |
| 6,526 | `444ce5a9fa8f7c7244b0fd3b0cf36d37891fb54111b89d2686eac8294eaaa315` | `/root/tz18-work/sec2-body.md` |
| 2,208 | `18a4ae5df74b0a40b05fd637f64e063fbeefe576f16988b5efff54760008d4b6` | `/root/tz18-work/sec2-close.md` |
| 510 | `ef9f829111bd6a59dbec91f261fb91f35537646f4c2068d04277f674b5fe4b1f` | `/root/tz18-work/v14-v15.txt` |

**No file under `/root/tz18-work/` outside the two worktrees has a name ending in `.py` or
`.sh`.** §0.5 asks that each such script be printed in full in Appendix A and that the report name,
from those scripts, every slug and every token id they requested, with each fifteen-minute slug's
`T`. There is no script to read, so the report cannot name the slug of the `5,462`-byte settled
fifteen-minute document that map §7 item 77 records. §0.5 provides for exactly this: "If no script
is found, the report says so; that is a disclosure, not a block." Appendix A is therefore empty, and
no other file's content was read — each of the thirty was opened only to hash it.

The `5,462` bytes remain unattributed by this report. What the host still holds about those
requests, if anything, is in `/root/tz18-work/host-close-block.md` and the fifteen `report-*.md`
and `sec2-*.md` drafts above, whose contents §0.5 forbids reading. §9 copies all thirty into
`/root/btc-forensics/` byte for byte, so a later TZ that is authorized to read them can still do so.

### 0.6 Trees and interpreter

Two worktrees were created from `origin/main` at `3a95ae1`: `/root/tz18a-work/wt` on branch
`tz-18a-chainbook-capture`, and `/root/tz18a-work/wt-report` detached. `sha256sum` of every file
under `/root/btc-forensics/` was written to `/root/tz18a-work/forensics-before.sha256` —
**211 lines**, matching the §0.2 count. The interpreter for every run was
`/root/tz01-env/venv/bin/python`, **Python 3.12.3**, the map §6 version. Neither `/root/tz01-env/`
nor `/root/tz04a-env/` was touched.

---
## 1. Input

Nothing was re-collected. The one input that did not already exist on the host is what the
capture recorded in this session.

| read | where from | size | hash |
|---|---|---|---|
| the base blob | `git show 8caa0b4:research/tz18-chainbook-capture.py`, served as `refs/pull/18/head` | 1,420 lines, 57,409 bytes | `33753b2bb1e322a081e6cba8bad976268e2d6046dc350e6ceae3e748ad6e4bfe` |
| `SYSTEM-MAP.md` and the 25 hashed rows | `/root/btc-5m-twap` at `3a95ae1` | 26 files, 1,062,750 bytes in total | §0.1 |
| `/var/lib/btc-chainbook/runtime.jsonl` | the chain book store | 2 records before this session | §0.4 |
| the 2,016 five-minute manifests of the week before R1 | `/var/lib/btc-recorder/btc-updown-5m/` | 2,016 opened | §2.3 |
| the 30 files under `/root/tz18-work/` outside its worktrees | the host | 30 files | §0.5 |
| every committed report on `main` | `/root/tz18a-work/wt/CryptoReports/` | 27 reports | §2.8, hexadecimal tokens only |

---

## 2. Measurements

### 2.1 The instrument

| field | value |
|---|---|
| path | `research/tz18a-chainbook-capture.py` |
| SHA-256 | `e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae` |
| lines | 1,683 |
| bytes | 69,357 |
| branch | `tz-18a-chainbook-capture` |
| branch commit | `ca4bbc1dd583cbb62f3c0c985938d229b526ce7e` |
| `P_push` | `1790185159` = 2026-09-23T17:39:19Z, taken as `git push` exited `0` |
| `git ls-remote origin refs/heads/tz-18a-chainbook-capture` | `ca4bbc1dd583cbb62f3c0c985938d229b526ce7e	refs/heads/tz-18a-chainbook-capture` |

**The branch carries two commits, and the report states why.** The first, `9973e44`, was pushed at
`1790185028`. Its `--prestart` run aborted on its own assert in §3.4 step 3: `base_rate` returned
`2,017` slots because it included `T0 = p − 300`, whose five-minute interval closes at `p` itself,
and §3.4 step 3's window `[p − 604,800, p)` is half open. The second, `ca4bbc1`, re-derives the
whole file from `8caa0b4` — V3 re-asserted, `33753b2b…` — re-applies D1 to D16, and fixes that one
expression. **No live request was made under `9973e44`:** the abort happened at step 3, before
step 4's live window and step 5's first request, and the run's request counter was `0`. Every
figure below comes from `ca4bbc1`. `P_push` above is the second push; the first is disclosed here
and nowhere relied on.

### 2.2 V4 — the hunk map

`diff -u` between the base blob and the new file:

| # | `diff -u` hunk header | base lines | D-item(s) |
|---|---|---|---|
| 1 | `@@ -1,18 +1,18 @@` | 1–18 | **D1** |
| 2 | `@@ -22,6 +22,7 @@` | 22–27 | **D2** |
| 3 | `@@ -32,7 +33,6 @@` | 32–38 | **D2** |
| 4 | `@@ -52,7 +52,7 @@` | 52–58 | **D3** |
| 5 | `@@ -67,14 +67,13 @@` | 67–80 | **D3** + **D6** |
| 6 | `@@ -82,7 +81,7 @@` | 82–88 | **D4** |
| 7 | `@@ -95,34 +94,25 @@` | 95–128 | **D5** + **D6** |
| 8 | `@@ -136,12 +126,13 @@` | 136–147 | **D5** + **D6** + **D13** |
| 9 | `@@ -357,12 +348,6 @@` | 357–368 | **D6** |
| 10 | `@@ -423,15 +408,31 @@` | 423–437 | **D7** |
| 11 | `@@ -446,6 +447,9 @@` | 446–451 | **D7** |
| 12 | `@@ -454,7 +458,7 @@` | 454–460 | **D7** |
| 13 | `@@ -515,10 +519,31 @@` | 515–524 | **D8** |
| 14 | `@@ -530,16 +555,24 @@` | 530–545 | **D8** |
| 15 | `@@ -560,6 +593,8 @@` | 560–565 | **D9** |
| 16 | `@@ -755,13 +790,23 @@` | 755–767 | **D10** |
| 17 | `@@ -783,199 +828,204 @@` | 783–981 | **D6** + **D14** |
| 18 | `@@ -994,13 +1044,24 @@` | 994–1006 | **D11** |
| 19 | `@@ -1018,9 +1079,18 @@` | 1018–1026 | **D11** |
| 20 | `@@ -1034,8 +1104,12 @@` | 1034–1041 | **D12** |
| 21 | `@@ -1051,42 +1125,83 @@` | 1051–1092 | **D12** + **D13** |
| 22 | `@@ -1094,7 +1209,7 @@` | 1094–1100 | **D13** |
| 23 | `@@ -1103,48 +1218,50 @@` | 1103–1150 | **D13** |
| 24 | `@@ -1153,43 +1270,77 @@` | 1153–1195 | **D13** |
| 25 | `@@ -1198,46 +1349,46 @@` | 1198–1243 | **D13** + **D15** |
| 26 | `@@ -1249,11 +1400,11 @@` | 1249–1259 | **D15** |
| 27 | `@@ -1262,6 +1413,10 @@` | 1262–1267 | **D15** |
| 28 | `@@ -1282,36 +1437,104 @@` | 1282–1317 | **D15** |
| 29 | `@@ -1326,16 +1549,31 @@` | 1326–1341 | **D15** |
| 30 | `@@ -1379,9 +1617,33 @@` | 1379–1387 | **D15** |
| 31 | `@@ -1390,15 +1652,16 @@` | 1390–1404 | **D16** |
| 32 | `@@ -1407,8 +1670,8 @@` | 1407–1414 | **D16** |

**32 hunks. 26 map to exactly one D-item; 6 carry two or three. None is unassigned.**

Six hunks carry more than one D-item because §3.3's own base-line assignments put those D-items
within three lines of each other, which is `diff -u`'s context: D6 removes base line 75, between
D3's 71 and 76; D5's new constants replace the block D6 removes at 98–115; D13's `PROOF_JSON_KEYS`
at 138–142 sits beside D5's new `PRESTART_JSON_KEYS` and D6's `VERIFY_JSON_KEYS` at 143–145; D14's
`--prestart` section stands where D6 removed `--verify-tz17` at 785–979; D12's `manifest_scan` ends
at 1067 and D13's `mode_prove` begins at 1070; and D13's `mode_prove` ends at 1236 three lines
before D15's `mode_selftest` at 1239. At `diff -U0` the same change set decomposes into 97 blocks,
each inside one D-item's base range. V4 is **disclosed for the Architect's check, not asserted**,
and this is the disclosure.

### 2.3 P-START — the request path, proved on this host before the service started

`--prestart`, run as R1 from `/root/tz18a-svc/tz18a-chainbook-capture.py` with
`--repo /root/tz18a-work/wt --out /root/tz18a-work/run-1`, started `1790185179` and exited `0` at
`1790185180`.

**Processes (step 2).** 174 `/proc/{pid}/cmdline` read, `0` vanished mid-scan; pids whose command
line equals `SERVICE_ARGV`: **0**; equal to `OLD_SERVICE_ARGV`: **0**. Both counts are `0`, as
step 2 requires.

**The base rate (step 3).** `p = 1790184900` (2026-09-23T17:35:00Z). The `2,016` slots
`T0 = p − 605,100, …, p − 600` in steps of `300` — the five-minute intervals closing in
`[p − 604,800, p)`:

| quantity | value |
|---|---|
| slots | `2,016` |
| directories present | `2,016` |
| manifests read, `m` | `2,016` |
| manifests whose `quotes_complete` is not JSON `true`, `f` | **`0`** |
| `p_false_alarm(f, m, 5) = 1 − (1 − f/m)^5` | **`0`** exactly, `0.0000000000` to ten decimals |

**G-TIERC's false-failure probability is exactly `0`, stated before any interval it judges
existed.** G-DEPLOY's is `0` by §4. Family-wise over both gates it is `0`.

**The live window (step 4).** `T* = 1790184600`. At the read `now − T*` was `580` s, neither below
`30` nor above `840`, so neither wait was taken and `T*` stood. `btc-updown-15m-1790184600` closes
at `1790185500`; at the instant of the request, `1790185180`, it was open. **No settled market
document was requested.**

**The two requests (steps 5 and 6).** Every request carried exactly the header block of §3.2 —
five fields on the wire, `Accept-Encoding: identity`, `Host`, `Accept: application/json`,
`User-Agent: btc-5m-twap-tz18a`, `Connection: close`, none repeated, the request line
`GET <path-and-query> HTTP/1.1`. The two fields `build_request` sets are `Accept` and `User-Agent`;
the other three are `http.client`'s and `urllib`'s. S3 asserts that block on a loopback listener at
every run, and R0 asserted it before R1 opened any socket.

| # | method | URL | status | bytes | SHA-256 | parses JSON | elapsed |
|---|---|---|---|---|---|---|---|
| 1 | `GET` | `https://gamma-api.polymarket.com/markets/slug/btc-updown-15m-1790184600` | **200** | 5,364 | `99ad8aeeb88afd4f8e16e674577951cd5604af9777c90dc7192447111b6b15f3` | **true** | 37,639,766 ns = 37.6 ms |
| 2 | `GET` | `https://clob.polymarket.com/book?token_id=1102863109…65972` | **200** | 3,456 | `e3f26b4580f260d1edc9b48caafc8d68a40a26e849c9c7f1341dede50ce2e977` | **true** | 45,769,782 ns = 45.8 ms |

`recv_wall_ns` was `1790185180726159557` for request 1 and `1790185180772138170` for request 2.

**The two token ids**, the only values taken from request 1's body besides its status, byte count
and hash:

```
110286310952091361060679136017957318741160413157872213853175639614637635165972
103839176219195552985567711328642354049523736946228017126111314897310072323120
```

They are two, distinct and non-empty. The request counter at exit was `2`.

**READING P-START: served.** TZ-18's build, at the same two endpoints under Python's default
agent, was answered `403`, `error code: 1010`, at every one of its 64 requests (its `service.log`,
`documents_ok=False statuses=[403, 403]`). The one changed field is the binding difference, and
this host proved it, not a second host's report of it.

### 2.4 The service

```
$ setsid nohup /root/tz01-env/venv/bin/python -B -u \
    /root/tz18a-svc/tz18a-chainbook-capture.py --serve \
    >> /var/lib/btc-chainbook/service.log 2>&1 &
```

| field | value |
|---|---|
| pid | `2699889` |
| `/proc/2699889/cmdline` | `/root/tz01-env/venv/bin/python\0-B\0-u\0/root/tz18a-svc/tz18a-chainbook-capture.py\0--serve\0` |
| equal to `SERVICE_ARGV` NUL-joined | **yes**, byte for byte |
| `pgrep -fx` with `SERVICE_ARGV` | exactly one line, `2699889` |
| `/var/lib/btc-chainbook/service.pid` | `2699889` |
| `start` record pid | `2699889` |
| `start` record `wall_ns` | `1790185190022755903` = 2026-09-23T17:39:50.022756Z — **`s`** |
| `start` record commit | `ca4bbc1dd583cbb62f3c0c985938d229b526ce7e`, equal to `origin/tz-18a-chainbook-capture` |
| `start` record `file_sha256` | `e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae`, equal to the branch blob's |
| `start` records written in this session | exactly **1** |
| copy at `/root/tz18a-svc/tz18a-chainbook-capture.py` | `e9cb9b47…`, equal to the branch blob |
| `/root/tz18a-svc/commit.txt` | `ca4bbc1dd583cbb62f3c0c985938d229b526ce7e` + newline, 41 bytes, 40 lowercase hex |

The `start` record's `config` carries the two headers and the service argv, which D9 added:

```json
"headers": [["Accept", "application/json"], ["User-Agent", "btc-5m-twap-tz18a"]],
"service_argv": ["/root/tz01-env/venv/bin/python", "-B", "-u",
                 "/root/tz18a-svc/tz18a-chainbook-capture.py", "--serve"],
"doc_offset": 625
```

**D8 replaced the stale pid file, and said so:** `stale pid file (pid 2608993, cmdline '')
replaced`. Pid `2608993` was TZ-18's service; its `/proc` entry is gone, so `same_service` held for
neither `SERVICE_ARGV` nor `OLD_SERVICE_ARGV`, and the file was unlinked and recreated. TZ-18's
build would have compared a substring of a command line that no longer exists (map §7 item 76);
this one compares the exact argv and gets the same answer for the right reason.

**`s − K_stop` = `39,350` s**, far above the `900` s §6 R1 requires.

### 2.5 Request accounting, stored bytes and the cost

| source | requests | to |
|---|---|---|
| R0, `--selftest` | **3** | `127.0.0.1` only — S3 items 2, 4 and 5 send one each; item 1 sends none |
| R1, `--prestart` | **2** | `gamma-api.polymarket.com` once, `clob.polymarket.com` once |
| R4, `--prove` | **0** | — |
| R4b, `--prove` | **0** | — |
| the service | **90** over the three considered windows — `2` documents and `28` books each, every one issued, and window `1790187300` was still under way at the closing read | the two venue hosts |

The declared rate is **30 requests per 900 s window** — `2 + 4 × 7` — so `2,880` a day and
`0.033` per second. None falls in the second of a scheduled recorder request of the same market:
the document is fetched at `T + 625`, `20` s after S6's first attempt at `T + 605`, and the seven
checkpoints at `T + 655, 715, 775, 805, 835, 865, 885` each fall five seconds before Tier C's reads
of the same five-minute market at `T + 660, 720, 780, 810, 840, 870, 890`. S1 asserts both, five
asserts. S6's retries, three seconds apart after a failure, are unscheduled and are not claimed.

**The service's requests, per considered window, by status:**

| window `T` | `documents_ok` | checkpoints complete | missed | book statuses | `documents.jsonl` | `books.jsonl.gz` | `window.json` | total bytes |
|---|---|---|---|---|---|---|---|---|
| `1790184600` | `true` | **7 of 7** | 0 | `200` × 28 | 12,058 | 15,157 | 937 | **28,152** |
| `1790185500` | `true` | **7 of 7** | 0 | `200` × 28 | 11,894 | 15,730 | 934 | **28,558** |
| `1790186400` | `true` | **7 of 7** | 0 | `200` × 28 | 11,856 | 15,903 | 933 | **28,692** |

Over the three considered windows the book statuses are **`200` × 84** — not one non-200, not one
null. Each window's two document fetches were `200` as well, so `90` of `90` requests succeeded.

**The cost, measured:**

| quantity | figure | derivation |
|---|---|---|
| requests per window | `30` | `2 + 4 × 7`, all 30 issued in each of the three windows |
| requests per day | `2,880` | `30 × 96` |
| added venue rate | `0.033` req/s | `2,880 / 86,400` |
| stored bytes, measured | `85,402` over 3 windows; mean **`28,467.3`** a window | `os.stat` on the three files of each |
| projected per day | **`2,732,864` bytes = `2.73` MB** | `28,467.3 × 96`; TZ-18 §3.9 projected `31,250` a window and `3.0` MB a day |
| write cap in days | **`73.2` days** | `200,000,000 / 2,732,864` — TZ-18 §3.9's projection gave about `66` |
| `df` avail | opening `13,427,335,168` → closing `13,430,845,440`, **`+3,510,272`** | §0.2 opening and closing |

`avail` **rose** across the session: §9 removed three trees totalling more than it copied into
`/root/btc-forensics/`, and the capture's own three windows cost `85,402` bytes. The resource gate
`avail >= 2,200,000,000` was asserted inside the instrument at every run and at every window, and
held at `6.1` times the floor throughout.

### 2.6 Every output file

| run | path | SHA-256 | lines | bytes |
|---|---|---|---|---|
| R1 | `/root/tz18a-work/run-1/tz18a-prestart.json` | `d6d06a4fc9229f1eabc77ddea5fe10a9b4f5e84d2cde243f516cd366159d4d0e` | 81 | 2,061 |
| R4 | `/root/tz18a-work/run-2/tz18a-proof.json` | `2f9831f3c74893e01384aeb36863b8aa9dd7a25db27ad0b08c1c8998f9a06eea` | 846 | 17,963 |
| R4b | `/root/tz18a-work/run-3/tz18a-proof.json` | `2f9831f3c74893e01384aeb36863b8aa9dd7a25db27ad0b08c1c8998f9a06eea` | 846 | 17,963 |

**V8 — determinism.** `cmp /root/tz18a-work/run-2/tz18a-proof.json
/root/tz18a-work/run-3/tz18a-proof.json` printed nothing and exited `0`; both files hash to
`2f9831f3c74893e01384aeb36863b8aa9dd7a25db27ad0b08c1c8998f9a06eea`, 846 lines, 17,963 bytes. Two
runs with one `A` wrote the same bytes, which is what `considered` and D12's `st_mtime_ns` rule are
for.

Any row of this report is re-derivable by the Architect from `tz18a-prestart.json`,
`tz18a-proof.json` and the stored window files, without re-running anything.

### 2.7 TZ-18's three outputs, and their copies

The TZ-18 report printed no hash of any of its files (map §3). These are theirs:

| path | bytes | lines | SHA-256 |
|---|---|---|---|
| `/root/tz18-work/run-1/tz18-verify.csv` | 232,762 | 1,001 | `0bbb345dc457768c387c45bb583035ce0074d6cdd432ff26b6a7e60f1bcb8e67` |
| `/root/tz18-work/run-1/tz18-verify.json` | 787 | 45 | `76b12513e8772704d53589b0a09f329cb5d7c58362ef445b3e56a3ca136d3e3a` |
| `/root/tz18-work/run-2/tz18-proof.json` | 11,211 | 557 | `95b8f17324e39b23dd2872faa10d330a72f883ea4770b2ddd6942e2cde452ae1` |

The two verify files together are `233,549` bytes, the figure TZ-18 report §2.6 states.

The `run-3/` and `predebug/` copies of the first two are **equal to them by hash**:

| copy | SHA-256 | equal to |
|---|---|---|
| `/root/tz18-work/run-3/tz18-verify.csv` | `0bbb345dc457768c387c45bb583035ce0074d6cdd432ff26b6a7e60f1bcb8e67` | `run-1/tz18-verify.csv` |
| `/root/tz18-work/run-3/tz18-verify.json` | `76b12513e8772704d53589b0a09f329cb5d7c58362ef445b3e56a3ca136d3e3a` | `run-1/tz18-verify.json` |
| `/root/tz18-work/predebug/tz18-verify.csv` | `0bbb345dc457768c387c45bb583035ce0074d6cdd432ff26b6a7e60f1bcb8e67` | `run-1/tz18-verify.csv` |
| `/root/tz18-work/predebug/tz18-verify.json` | `76b12513e8772704d53589b0a09f329cb5d7c58362ef445b3e56a3ca136d3e3a` | `run-1/tz18-verify.json` |

Four of four equal. None of these files was parsed; each was opened only to hash it and to copy it
(P2's named exemption).

### 2.8 Retention — §9, in order

**Step 1, copy first.** Every file under `/root/tz17-work/`, `/root/tz18-work/` and
`/root/tz18-svc/`, worktrees included, whose SHA-256 is named by any committed report on `main` —
matched against every hexadecimal token of 16 to 64 characters those reports print, the predicate
TZ-14 and TZ-15 used — plus the files §9 names here.

| quantity | value |
|---|---|
| committed reports read for tokens | **27** |
| distinct hexadecimal tokens of 16–64 characters | **1,339** |
| files under the three trees | **1,237** |
| selected | **1,147** — 986 from `/root/tz17-work`, 159 from `/root/tz18-work`, 2 from `/root/tz18-svc` |
| copied by exclusive create | **835** |
| already held by hash, so not copied | **312** |

Each copy's hash was asserted at source and at destination, and each landed under its path below
`/root/` with `/` replaced by `--`, in sorted path order — for instance
`tz17-work--raw--btc-updown-15m-1788998400.body`. Nothing was parsed; only §0.5's thirty were
listed by name, and none of their contents read.

**Step 2, then assert.** TZ-17's CSV was extracted from its committed report as TZ-18 §3.7 step 1
extracts it:

| assertion | expected | read | verdict |
|---|---|---|---|
| CSV SHA-256 | `96b5e21e2cc59e2f3bde332d60457533158bd16c2eeaaaba844bf35b1efc63ee` | equal | **holds** |
| CSV bytes | `99,075` | `99,075` | **holds** |
| CSV lines | `201` | `201` | **holds** |
| distinct values in the five `sha_*` columns | `801` in `1,000` cells | `801` in `1,000` | **holds** |
| all `801` held by the store, by hash | 801 | **801**, missing `0` | **holds** |
| `tz17-candidates.csv` `96b5e21e…` | held | **held** | **holds** |
| `tz17-summary.json` `fb20cbf15751fdaac3dd0d2736192f891d746b91eab1db9bcef81d6a4e788937` | held | **held** | **holds** |
| `tz18-verify.csv` `0bbb345d…` | held | **held** | **holds** |
| `tz18-verify.json` `76b12513…` | held | **held** | **holds** |
| `tz18-proof.json` `95b8f173…` | held | **held** | **holds** |
| the `211` files of `forensics-before.sha256` hash unchanged | 211 | **211**, changed or gone `0` | **holds** |

Store before: **211** files, 143 distinct hashes. Store after: **1,046** files, 978 distinct
hashes, `134,111,602` bytes.

**Step 3, then the worktrees.** `/root/tz17-work/wt`'s untracked `research/__pycache__/` was
deleted first — it was the only `__pycache__` in the four. Each worktree was then removed by
`git worktree remove` **without `--force`**, and each exited `0` with `test -e` exiting `1`
afterwards:

```
git worktree remove /root/tz17-work/wt          exit=0, test -e exit=1
git worktree remove /root/tz17-work/wt-report   exit=0, test -e exit=1
git worktree remove /root/tz18-work/wt          exit=0, test -e exit=1
git worktree remove /root/tz18-work/wt-report   exit=0, test -e exit=1
```

Four of four. None refused, so none stayed.

**Step 4, then the trees.** One command naming one tree each, each verified by `test -e`. The
session's classifier accepted all three:

```
rm -rf /root/tz17-work    exit=0, test -e exit=1
rm -rf /root/tz18-work    exit=0, test -e exit=1
rm -rf /root/tz18-svc     exit=0, test -e exit=1
```

Nothing was handed to the Boss. `git worktree list` now shows five entries: the main checkout,
TZ-16's two under `/root/tz15-work/`, and this TZ's two.

`/root/tz18a-work/` is the next TZ's to reclaim on the same terms. `/root/tz18a-svc/` is **not**
scratch — the service runs from it. `/root/tz15-work/` stays TZ-16's and was not touched.
**The capture was never deleted:** `/var/lib/btc-chainbook/` keeps TZ-18's 32 windows beside this
service's, all reserved on map §2.5's terms, and nothing of it entered git history.

### 2.9 Host gate — the closing reads, verbatim

```
$ df -B1 --output=source,size,avail /var/lib/btc-recorder
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 13430845440

$ find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json

$ pgrep -fx '/root/tz04a-env/venv/bin/python -B -u recorder.py'; echo "exit=$?"
228592
exit=0

$ grep -rl --include=runtime.jsonl 4216c04673ced76b5b2ac60ef57c9abedc46f9b9 /var/lib/btc-recorder | head -n 1
/var/lib/btc-recorder/btc-updown-5m/1789488300/runtime.jsonl

$ du -sb /root/PROJECT_GAMING_PS5
409325276	/root/PROJECT_GAMING_PS5

$ systemctl is-enabled telemetry-watch.service; echo "exit=$?"
disabled
exit=1

$ systemctl is-active telemetry-watch.service; echo "exit=$?"
inactive
exit=3

$ for d in /root/tz15-work /root/tz17-work /root/tz18-work /root/tz18-svc /root/tz18a-work /root/tz18a-svc; do test -e "$d"; echo "$d exit=$?"; done
/root/tz15-work exit=0
/root/tz17-work exit=1
/root/tz18-work exit=1
/root/tz18-svc exit=1
/root/tz18a-work exit=0
/root/tz18a-svc exit=0

$ find /root/btc-forensics -type f | wc -l
1046

$ git worktree list
/root/btc-5m-twap           3a95ae1 [main]
/root/tz15-work/wt          f7f171a [tz-15-phase2-gate]
/root/tz15-work/wt-report   c729008 (detached HEAD)
/root/tz18a-work/wt         ca4bbc1 [tz-18a-chainbook-capture]
/root/tz18a-work/wt-report  3a95ae1 (detached HEAD)
```

Beside the opening reads of §0.2: `df` names the same source and size and `avail` is `+3,510,272`
higher; H1's path and the `runtime.jsonl` path are unchanged; the recorder is the same pid `228592`
and was never signalled, reniced or touched; `telemetry-watch.service` is still `disabled` and
`inactive`; `/root/tz17-work`, `/root/tz18-work` and `/root/tz18-svc` now exit `1` and
`/root/tz18a-work` and `/root/tz18a-svc` exit `0`; the forensic store is `1,046` files; and
`git worktree list` shows five entries where it showed seven. `du -sb /root/PROJECT_GAMING_PS5`
moved from `409,118,861` to `409,325,276` bytes — `+206,415`, not this TZ's writing, and it carries
no threshold.

## 3. Publication

| step | value |
|---|---|
| branch | `tz-18a-chainbook-capture` |
| commits | `9973e44193dc09a0ae7c26a9f2038ffbd0687ae5` then `ca4bbc1dd583cbb62f3c0c985938d229b526ce7e` (§2.1) |
| head | `ca4bbc1dd583cbb62f3c0c985938d229b526ce7e`, pushed, **unmerged** |
| `P_push` | `1790185159` |
| pull request | [#19](https://github.com/seahomebatumi-ai/btc-5m-twap/pull/19), open, unmerged |
| Release asset | none — this TZ requires no Release |
| report | `CryptoReports/TZ-18a-chainbook-capture-redeploy-report.md`, pushed to `main` from `/root/tz18a-work/wt-report` with `git push origin HEAD:main` |

**V14** — after the push and before the report commit:

```
$ git diff --name-only origin/main origin/tz-18a-chainbook-capture
research/tz18a-chainbook-capture.py
```

Exactly one path. No committed file changed.

**V15 — contract §4.2's separation self-check, verbatim:**

```
$ git rev-list origin/main | grep -c ca4bbc1dd583cbb62f3c0c985938d229b526ce7e
0
$ git diff --name-only origin/main origin/tz-18a-chainbook-capture
research/tz18a-chainbook-capture.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
```

The first line prints `0`: the implementation is not on `main`. The third prints nothing.

---
## 4. Gate

Both gates are quoted from TZ-18a §4, which fixed every threshold, population and sampling rule
before any of their data existed. Nothing below is tuned and no gate is reinterpreted.

### P-START — the precondition of CANON hard rule 14

> §3.4 served and parsed at both endpoints under §3.2's request, or **BLOCKED** with nothing
> started.

**READING P-START: served.** Request 1 status `200`, `5,364` bytes, parses as JSON, two distinct
non-empty token ids; request 2 status `200`, `3,456` bytes, parses as JSON. The request counter at
exit was `2`. §2.3 carries the whole of it. The service was started only after this run exited `0`.

### G-DEPLOY — does the capture record both books at one instant?

> **Unit:** a checkpoint. **Qualifying:** its window's document instant `T + 625 >= s + 60` and its
> own instant `<= s + 3,900`.
> **Complete:** four stored replies, all HTTP `200`, each body non-empty and parsing as JSON, and a
> skew `<= 1,000,000,000` ns.
> **Reading:** of the first 14 qualifying checkpoints, `>= 13` complete → **PASS**; `<= 12` →
> **FAIL**; fewer than 14 qualifying by the budget end → **UNDECIDABLE**.

False-failure probability under a capture that loses nothing: **exactly `0`**. Power, exactly
`1 − (1−p)^14 − 14·p·(1−p)^13`, recomputed in `Fraction` by S7 to a tolerance of `1E-18`:
`p = 0.25` → `0.899031627923250198364257812500`; `p = 0.10` →
`0.415370859484330000000000000000`; `p = 0.05` → `0.152985562588816560668945312500`.

**Considered windows: 3** — `1790184600`, `1790185500`, `1790186400`. 32 of the 35 window
directories on disk were **not** considered and were never opened: TZ-18's own, whose document
instants all precede `s`.

**Qualifying: 14 of 21 considered checkpoints.** The seven of window `1790184600` do not qualify:
its document instant `1790185225` falls `25` s short of `s + 60` = `1790185250.02`, so every one
reads `no document_instant_before_start+60`. §6 item 7 names why that window is still opened and
still counted for G-TIERC. The fourteen of windows `1790185500` and `1790186400` all qualify; the
last, at `1790187285`, is `1,805` s inside the budget end `s + 3,900` = `1790189090`.

**READING G-DEPLOY: PASS — complete 14 of the first 14 qualifying checkpoints.** Incomplete `0`,
missed `0`. Every one of the 84 book reads of the three considered windows returned HTTP `200` with
a non-empty body that parses as JSON, and every skew is two orders of magnitude inside the
`1,000,000,000` ns bound.

**V9 — the disclosure, every checkpoint of every considered window, in order of instant:**

| window `T` | `tau'` | instant | qualifying / reason | statuses | recv deltas ns | skew ns | complete / reason |
|---|---|---|---|---|---|---|---|
| `1790184600` | 245 | `1790185255` | no — `document_instant_before_start+60` | 200,200,200,200 | 2387645,0,4280141,10143166 | `10,143,166` | **yes** complete |
| `1790184600` | 185 | `1790185315` | no — `document_instant_before_start+60` | 200,200,200,200 | 2223269,4571463,1952177,0 | `4,571,463` | **yes** complete |
| `1790184600` | 125 | `1790185375` | no — `document_instant_before_start+60` | 200,200,200,200 | 2633699,1420956,0,24285442 | `24,285,442` | **yes** complete |
| `1790184600` | 95 | `1790185405` | no — `document_instant_before_start+60` | 200,200,200,200 | 0,2231217,3761998,17304549 | `17,304,549` | **yes** complete |
| `1790184600` | 65 | `1790185435` | no — `document_instant_before_start+60` | 200,200,200,200 | 12412550,2531226,8004243,0 | `12,412,550` | **yes** complete |
| `1790184600` | 35 | `1790185465` | no — `document_instant_before_start+60` | 200,200,200,200 | 1022389,0,1957938,4565488 | `4,565,488` | **yes** complete |
| `1790184600` | 15 | `1790185485` | no — `document_instant_before_start+60` | 200,200,200,200 | 9975815,25638136,0,4651542 | `25,638,136` | **yes** complete |
| `1790185500` | 245 | `1790186155` | **yes** qualifying | 200,200,200,200 | 6249098,22107301,0,7996185 | `22,107,301` | **yes** complete |
| `1790185500` | 185 | `1790186215` | **yes** qualifying | 200,200,200,200 | 0,3054540,1046357,3614329 | `3,614,329` | **yes** complete |
| `1790185500` | 125 | `1790186275` | **yes** qualifying | 200,200,200,200 | 17580262,3908961,4984130,0 | `17,580,262` | **yes** complete |
| `1790185500` | 95 | `1790186305` | **yes** qualifying | 200,200,200,200 | 4044216,1802483,3702601,0 | `4,044,216` | **yes** complete |
| `1790185500` | 65 | `1790186335` | **yes** qualifying | 200,200,200,200 | 0,7150195,6702197,5454659 | `7,150,195` | **yes** complete |
| `1790185500` | 35 | `1790186365` | **yes** qualifying | 200,200,200,200 | 0,356421,5627650,2552585 | `5,627,650` | **yes** complete |
| `1790185500` | 15 | `1790186385` | **yes** qualifying | 200,200,200,200 | 18435451,0,12088381,3948746 | `18,435,451` | **yes** complete |
| `1790186400` | 245 | `1790187055` | **yes** qualifying | 200,200,200,200 | 942567,0,1190143,711555 | `1,190,143` | **yes** complete |
| `1790186400` | 185 | `1790187115` | **yes** qualifying | 200,200,200,200 | 3319339,8130570,0,8418519 | `8,418,519` | **yes** complete |
| `1790186400` | 125 | `1790187175` | **yes** qualifying | 200,200,200,200 | 1805919,8325083,28425839,0 | `28,425,839` | **yes** complete |
| `1790186400` | 95 | `1790187205` | **yes** qualifying | 200,200,200,200 | 13000071,0,4749742,11388359 | `13,000,071` | **yes** complete |
| `1790186400` | 65 | `1790187235` | **yes** qualifying | 200,200,200,200 | 1193397,7011856,0,2386353 | `7,011,856` | **yes** complete |
| `1790186400` | 35 | `1790187265` | **yes** qualifying | 200,200,200,200 | 0,2346419,6176981,3503606 | `6,176,981` | **yes** complete |
| `1790186400` | 15 | `1790187285` | **yes** qualifying | 200,200,200,200 | 0,11125626,343797,9342632 | `11,125,626` | **yes** complete |

**21 of 21 disclosed.** `recv deltas ns` are each reply's receive stamp minus the earliest of the
four, so one is always `0`.

### The skews — the number the next TZ sizes its pairing rule from

Over the **21** considered checkpoints that produced four replies:

| statistic | ns | ms |
|---|---|---|
| minimum | `1,190,143` | 1.19 |
| median | `10,143,166` | 10.14 |
| maximum | `28,425,839` | 28.43 |

The largest skew observed is `28,425,839` ns — **`0.0284` s, 35 times inside G-DEPLOY's
`1,000,000,000` ns bound.** A pairing rule that treats four books as simultaneous within `50` ms
would have admitted every one of the 21; within `30` ms, 20 of 21.

**V10 — concurrency, recorded and not asserted.** Considered checkpoints with four non-null send
stamps: **21**. Checkpoints where the last send did not precede the first receive: **0**. TZ-18
asserted this at the end of `--prove` and could not print a count when it failed; here the count is
the disclosure, and it is zero.

### G-TIERC — did the new capture disturb Tier C, under the load it actually applied?

> **Exposed interval:** `E = T + 600` of a considered window that issued at least one request;
> **fully loaded** when it issued all 30.
> **Counted:** `E`'s `manifest.json` exists with `st_mtime_ns <= A · 10^9`.
> **FAIL:** any counted exposed interval whose `quotes_complete` is not `true`.
> **PASS:** no FAIL, and at least **two** counted fully loaded exposed intervals.
> **UNDECIDABLE:** otherwise.

False-failure probability, `1 − (1 − f/m)^5` over the week before R1: `f = 0`, `m = 2,016`, so
**exactly `0`** — §2.3, printed by `--prestart` before the service started. Power at the PASS
minimum of two fully loaded intervals, `1 − (1 − q)^2`: `q = 1` → `1`; `q = 0.5` → `0.75`;
`q = 0.25` → `0.4375`. **Two units see a gross disturbance and nothing finer.**

**`A` = `1790187453`** = 2026-09-23T18:17:33Z, from R3: `min(floor(now), floor(s) + 3,900)` =
`min(1790187453, 1790189090)`. R3 ended at its 38th minute-check, the first at which
`/var/lib/btc-chainbook/1790186400/window.json` and the manifests of `E1 = 1790186100` and
`E2 = 1790187000` all existed. `s <= A <= now` was asserted inside the instrument.

Proof window `[1790185190, 1790187453]`, length `2,263` s; control window
`[1790182927, 1790185190]`, the same length, by construction `[2·int(s) − A, int(s)]`.

**Per considered window:**

| window `T` | issued | fully loaded | `E` | counted at `A` | `quotes_complete` |
|---|---|---|---|---|---|
| `1790184600` | **30 of 30** | yes | `1790185200` | **yes** | **`true`** |
| `1790185500` | **30 of 30** | yes | `1790186100` | **yes** | **`true`** |
| `1790186400` | **30 of 30** | yes | `1790187000` | **no** — `no_manifest_by_as_of` | — |

**READING G-TIERC: PASS.** Exposed intervals `3`; counted at `A` `2`; counted **and** fully loaded
`2`, which is exactly the PASS minimum; counted exposed intervals whose `quotes_complete` is not
`true`: **`0`**.

`E2 = 1790187000` is exposed and fully loaded but **not counted**, and the reason is the boundary
D12 exists to draw: its interval closes at `1790187300`, the recorder wrote its `manifest.json`
between R3's checks at `1790187393` and `1790187453`, and `A` is `1790187453` — so its
`st_mtime_ns` exceeds `A · 10^9` by a fraction of a second. D12 counts a manifest only at
`st_mtime_ns <= A · 10^9`, which is what makes R4 and R4b read the same set (V8). The gate reaches
PASS on the two that do count; the third is disclosed and excluded, not discarded.

**The proof and control windows, interval by interval, printed beside the gate and not gated:**

| window | five-minute intervals | manifests counted at `A` | `quotes_complete` true | exposed |
|---|---|---|---|---|
| proof `[1790185190, 1790187453]` | 8 | 6 | **6** | 3 |
| control `[1790182927, 1790185190]` | 7 | 7 | **7** | 0 |

Every counted interval in both windows reads `quotes_complete = true` and `complete = true`. The
two proof-window intervals not counted are `1790186700` (closes `1790187000`) and `1790187000`
(closes `1790187300`), both by `no_manifest_by_as_of`. **The control window carries none of the
capture's load — exposure `0` — and is the control it is described as.** Tier C read `true` on both
sides of the boundary.

**What the pair of readings means, in the words §4 fixed before the data.** Both markets' books are
recorded within one second of each other at `>= 13` of 14 checkpoints under the declared request —
here at 14 of 14, the largest skew `0.0284` s — and Tier C held at every exposed interval the proof
saw. **The service therefore keeps running after this session**, from its copy of the branch blob,
unmerged, until the Architect's verdict; R5 did not run and block K-18a was never authorized. The
pair says nothing about any price, book or edge, nor about a disturbance finer than two units can
see: G-TIERC's power at its PASS minimum is `1` against a disturbance that breaks every exposed
interval, `0.75` at `q = 0.5` and `0.4375` at `q = 0.25`.

---

## 5. Validation

Every row below is an `assert` that aborts the run unless the row says otherwise in plain words.
Counts come from the run; none is typed.

| # | row | asserted count | runs it held on |
|---|---|---|---|
| **V1** | the fingerprint gate inside the instrument | revision equal; anchors **6 of 6**; re-derived **4 of 4**; rows hashed **25 of 25**; `frozen` equal **23 of 23** | R1, R4, R4b |
| **V2** | host and resource gates | H1, H2, H3 compared by the Executor (§0.2), all three hold; `avail >= 2,200,000,000` asserted inside the instrument at every run and every window — `13,427,335,168` at §0.2, `13,430,845,440` at the closing read | §0, R1, R4, R4b, the service |
| **V3** | the base blob hashes to `33753b2b…` before the first edit | equal, and re-asserted for the second commit | B, twice |
| **V4** | every `diff -u` hunk maps to one D-item | **26 of 32** at `-U3`, **97 of 97** at `-U0`; §2.2 — **disclosed, not asserted** | B |
| **V5** | the write guard: every open for writing checked against the three roots | R0 **6**, R1 **1**, R4 **1**, R4b **1**; the service's per its stop record | all |
| **V6** | the open guard under `/var/lib/btc-recorder/`: every basename `manifest.json` | R0 **0**, R1 **2,016** (at most 2,016), R4 **15** and R4b **15** — **equal** | all |
| **V7** | requests | R0 **3**, each to `127.0.0.1`; R1 **2**; R4 **0**; R4b **0** | R0, R1, R4, R4b |
| **V8** | determinism: `tz18a-proof.json` byte-identical between R4 and R4b | **byte-identical**; `cmp` printed nothing and exited `0`; both hash to `2f9831f3c74893e01384aeb36863b8aa9dd7a25db27ad0b08c1c8998f9a06eea`, 846 lines, 17,963 bytes | R4b |
| **V9** | every considered checkpoint disclosed in order, qualifying or not, with its reason, four statuses and skew | **21 of 21** considered checkpoints disclosed in order of instant, each with its qualifying verdict and reason, its four statuses, its four receive deltas and its skew — §4 | R4 |
| **V10** | concurrency per considered checkpoint with four sends | considered checkpoints with four non-null send stamps **21**; last send not before the first receive **0** — **recorded, not asserted** | R4 |
| **V11** | the key sets of `window.json`, `tz18a-prestart.json` and `tz18a-proof.json` fixed in the source and asserted before each write, no forbidden key at any depth | `window.json` **9 keys** and its two market blocks **4 keys** each, asserted at every window close; `tz18a-prestart.json` **8 keys**; `tz18a-proof.json` **12 keys** | all |
| **V12** | the `start` record, `pgrep`, `service.pid`, `/proc/{pid}/cmdline`, exactly one `start` this session | all six checks hold — §2.4 | R2, and at the session's end |
| **V13** | the write cap, summed as written, `<= 200,000,000` | R0 **0**, R1 **2,061**, R4 **17,963**, R4b **17,963**; the service still running, so no `stop` record; `85,402` bytes of window files at the closing read, 0.04% of the cap | all |
| **V14** | `git diff --name-only origin/main origin/tz-18a-chainbook-capture` prints exactly one path | **1**, `research/tz18a-chainbook-capture.py` | after the push |
| **V15** | contract §4.2's separation self-check, verbatim | first line `0` — §3 | after the push |
| **V16** | order: `P_push` < R1's first `recv_wall_ns` < `s` < R4's start; and `s >= K_stop + 900` | `P_push` `1790185159` < R1's first `recv_wall_ns` `1790185180.726159557` < `s` `1790185190.022755903` < R4's start `1790187469`; and `s − K_stop` = **`39,350`** s ≥ `900` | R4 |
| **V17** | where R5 ran, the stop verified as §6.1 says | **R5 did not run** — the pair of readings is (PASS, PASS), so §6 R5's condition is not met and block K-18a was never authorized | R5 |
| **V18** | retention: the `211` files hash unchanged; every hash §9 step 2 names held; counts before and after | the `211` files hash unchanged, changed or gone **0**; all `801` TZ-17 body hashes held; all five named hashes held; store **211 → 1,046** files — §2.8 | R6 |

---

## 6. What could not be implemented as written

Seven items. None changes a threshold, a population or a reading.

**1. §0.5's diagnostic scripts do not exist, so the slug cannot be named.** No file under
`/root/tz18-work/` outside its two worktrees ends in `.py` or `.sh` — the thirty files are one
`.md` block, fifteen report drafts, four `preflight-*.txt`/`*.log` logs, three `R*.log`, one
`.txt`, and the six output files of TZ-18's three run directories. §0.5 provides for this in
terms: "If no script is found, the report says so; that is a disclosure, not a block." **Appendix A
is therefore empty**, and the report cannot name the slug of the `5,462`-byte settled
fifteen-minute document, its `T`, or the token ids those requests used. P5 forbids asking the venue,
and §0.5 forbids reading any of the thirty files' contents. §9 copies all thirty into
`/root/btc-forensics/` byte for byte, so a TZ that is authorized to read them still can.

**2. V4's one-to-one hunk map does not hold at `diff -u`'s default context; it holds at `-U0`.**
26 of the 32 hunks carry exactly one D-item. Six carry two or three, because §3.3's own base-line
assignments place those D-items within three lines of one another — the full account is in §2.2.
V4 is written "disclosed for the Architect's check, not asserted", so this is a disclosure and not
a failed assert. At `diff -U0` the change set decomposes into 97 blocks, each inside one D-item's
base range.

**3. The branch carries two commits, and the first one's `--prestart` aborted.** `base_rate`
returned `2,017` slots instead of `2,016`: it admitted `T0 = p − 300`, whose five-minute interval
closes at `p`, which §3.4 step 3's half-open window `[p − 604,800, p)` excludes. The instrument's
own assert stopped the run at step 3, **before step 4's live window and before any request** — the
request counter was `0` at the abort. `ca4bbc1` re-derives the whole file from `8caa0b4` with V3
re-asserted and re-applies D1 to D16. Nothing was forced and no history was rewritten. Every figure
in this report comes from `ca4bbc1`.

**4. `mode_prestart` needed two pure helpers D14 does not name.** D14 names `base_rate` and
`p_false_alarm`. The mode also needs `decimals_of(fraction, places)`, which renders an exact
`Fraction` to ten decimals in integer arithmetic — D2 removed `Decimal`, whose only users D6
removed, so there is no other way to print the ten decimals §3.4 step 3 asks for — and
`parses_json(raw)`, the predicate §3.4 steps 5 and 6 require and §3.6 already needed. Both are
pure, both take nothing from what they read, and neither touches a threshold.

**5. `manifest_scan`'s rows gained a `reason` key, and `--prove` marks exposure on them
afterwards.** D12 fixes the signature as taking `A`, so the scan cannot know which intervals are
exposed; §3.6 nonetheless asks that the printed intervals say "whether it is exposed". `mode_prove`
therefore sets `exposed` on each row after both scans return, from the set of `E` values of the
considered windows that issued at least one request. The `reason` key carries D12's
`no_manifest_by_as_of`. Neither affects G-TIERC, which reads only the per-window rows.

**6. Each checkpoint record gained a `sends_stamped` count.** C6 fixes V10's population as
"considered checkpoints with four non-null send stamps", and TZ-18's `concurrency_ok` returns
`None` both when the sends are fewer than four and when no reply arrived, so the two cases are not
separable from its return value alone. `sends_stamped` makes the population explicit and is what
V10's count is taken over.

**7. A window can be considered and still qualify for no G-DEPLOY unit.** `considered(T, s, A)`
admits a window whose document instant is at or after `s`; `qualifies` needs it at or after
`s + 60`. The window at `1790184600` fell between the two: its document was fetched `35` s after
the service started, so it is opened, its thirty requests are counted for G-TIERC, and its seven
checkpoints are disclosed by V9 as `no document_instant_before_start+60`. That is what the two
rules say, not a deviation from them, but it is the reason G-DEPLOY's qualifying count comes from
two windows and G-TIERC's exposure from three.

---

## Appendix A — the diagnostic scripts

**Empty.** §0.5 asks that every file under `/root/tz18-work/`, outside `wt/` and `wt-report/`, whose
name ends in `.py` or `.sh` be printed here in full. The list in §0.5 is thirty files and none of
them has such a name:

```
$ find /root/tz18-work -type f -not -path '/root/tz18-work/wt/*' \
    -not -path '/root/tz18-work/wt-report/*' \( -name '*.py' -o -name '*.sh' \)
(no output; exit 0)
```

No other file's content was read; each of the thirty was opened only to hash it, and §9 copied all
thirty into `/root/btc-forensics/` byte for byte. The requests map §7 item 77 records — among them
the `5,462`-byte live settled fifteen-minute document — were made by the TZ-18 Executor outside its
instrument, and this host retains no script that names their slugs.
