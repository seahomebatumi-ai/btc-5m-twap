# TZ-20 report — the capture under systemd

**READING: PASS at every gate.** G-UNIT 2 of 2 units at `0` restarts and 2 of 2 at `1` · G-START 2 of 2 ·
G-CB 2 of 2 windows, `checkpoints_complete` **14 of 14** against a pass mark of 13 · G-REC 6 of 6 manifests,
`quotes_complete` 6 of 6, sha 6 of 6, `complete` **6 of 6** against a pass mark of 4 · G-RESTART-C PASS, the
chain book restarted by systemd **5.5 s** after its stop · G-RESTART-R PASS, the recorder's restart gap
**6.9 s**, recorded.

**Both captures run as systemd system units, and K-20R and K-20C were never run.** At `I final` (08:27:50 UTC)
`btc-recorder.service` ran as pid `4067771` and `btc-chainbook.service` as pid `4064090`. Each is the sole instance
of its argv, inside `/system.slice/<unit>` and no `/user.slice` path, `enabled` and `active`/`running`, with
`NRestarts` `1`. The newest recorder `start` record names `4216c04673ced76b5b2ac60ef57c9abedc46f9b9`. These were
read by the Executor from systemd and `/proc`, never from an account.

**One block was refused by the session's classifier.** B-START-REC (`systemctl enable --now`) was refused as
"Unauthorized Persistence". The Executor took both start marks; the Boss ran B-START-REC and B-START-CB verbatim;
the Executor verified both. B-KILL-CB and B-KILL-REC (`systemctl kill`) were not refused.

| field | value |
|---|---|
| TZ | `CryptoTZ/TZ-20-capture-under-systemd.md`, 1,632 lines, 93,425 bytes, SHA-256 `178f2a339e60b5eacd6fecb4cf6f91f6165c832092aa04e47bc9a1971597c7ba`, landed at `2d61a16` |
| map revision | `2026-10-04-a`, equal; anchors 6 of 6; re-derived 4 of 4; rows hashed 28; `frozen` equal 25 of 25 |
| executor model | Opus, as the TZ names |
| branch | `tz-20-capture-under-systemd` at `0956da12bd26decbef0fd643b6f223102c7788ba`, pushed; pull request #21, open, not merged |
| units | `btc-recorder.service`, `btc-chainbook.service`; `/etc/systemd/system/`, byte-identical to the branch's `deploy/systemd/` |
| recorder code | `/root/btc-recorder-svc`, a detached worktree at `4216c04` |
| chain book code | `/root/tz18a-svc/tz18a-chainbook-capture.py`, `e9cb9b47…`, unchanged |
| pricer | not read, not called, not scored; `A6` `729f0bcdbee3` is stated so that what was not scored is not in doubt |

No price, size, spread, mid, book level, outcome or label was read, printed or written by this TZ's commands,
except §9's whole-file copies into the forensic store (§2 item 6's exemption), from which no value was extracted.

---

## 0. Fingerprint

**Revision string read:** `2026-10-04-a`, equal to the value TZ-20's header requires. `main` was fast-forwarded
from `b96be84` to `2d61a16` by contract §1's pull, and the map and the TZ were read there.

| anchor | required | read from the map | re-derived from the file | verdict |
|---|---|---|---|---|
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` | not a file anchor | equal |
| `A2` — collector | `6c5089330629` | `6c5089330629` | `6c5089330629` | equal |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` | same | not a file anchor | equal |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b` | `437b45ea196b` | equal |
| `A5` — recorder | `9fd1c7de0f74` | `9fd1c7de0f74` | `9fd1c7de0f74` | equal |
| `A6` — pricer | `729f0bcdbee3` | `729f0bcdbee3` | `729f0bcdbee3` | equal |

### 0.1 The 28 rows of the map's §0 table (V1)

The table was parsed from the map at `2d61a16`, and every path was hashed in the primary checkout. Each `frozen`
row was asserted equal in lines, bytes and SHA-256. The script's output, verbatim:

```text
git HEAD 2d61a16a0a4314e42369d5af497c07dd97968481
revision string 2026-10-04-a
A1 map 229a944f2d51 TZ 229a944f2d51 equal
A2 map 6c5089330629 TZ 6c5089330629 equal
A3 map 0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable TZ 0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable equal
A4 map 437b45ea196b TZ 437b45ea196b equal
A5 map 9fd1c7de0f74 TZ 9fd1c7de0f74 equal
A6 map 729f0bcdbee3 TZ 729f0bcdbee3 equal
A2 re-derived research/twap-divergence.py 6c5089330629 equal
A4 re-derived BTC-EXECUTOR-INSTRUCTIONS.md 437b45ea196b equal
A5 re-derived research/recorder/recorder.py 9fd1c7de0f74 equal
A6 re-derived research/pfair.py 729f0bcdbee3 equal
table rows 28
SYSTEM-MAP.md                                   1080   217181 7e99182f15edf1d1dbb9b6812bc747a4d321f4145f55b43e223b8918b6338003 reported
BTC-EXECUTOR-INSTRUCTIONS.md                     234    11128 437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b frozen equal
research/twap-divergence.py                     1135    50928 6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473 frozen equal
research/selftest-twap-divergence.py             376    16736 ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a frozen equal
research/tz02-distribution.py                    334    14511 f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4 tracked (map equal)
research/pfair.py                                441    19357 729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68 frozen equal
research/selftest-pfair.py                       619    32559 b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa frozen equal
research/tz06-calibration.py                     577    27138 715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f frozen equal
research/tz07a-variance-time.py                  623    28414 513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771 frozen equal
research/tz07b-settlement-dispersion.py          515    24926 424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc frozen equal
research/tz08a-out-of-sample.py                  745    38822 37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c frozen equal
research/tz09-disk-inventory.py                  894    41004 b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6 frozen equal
research/tz10b-sigma-or-link.py                 1224    61018 406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088 frozen equal
research/tz11a-student-link.py                  1231    64732 0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839 frozen equal
research/tz12-sized-gate.py                     1157    61637 d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999 frozen equal
research/tz13-sized-gate-test3.py               1074    53901 a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd frozen equal
research/tz14-quote-inventory.py                2124   109972 978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02 frozen equal
research/tz15-phase2-gate.py                    1517    73799 66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3 frozen equal
research/tz16a-phase2-decisive-gate.py          2198   111192 3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125 frozen equal
research/tz17-settlement-chain.py               1102    38622 e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92 frozen equal
research/tz18a-chainbook-capture.py             1683    69517 e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae frozen equal
research/recorder/recorder.py                    608    25658 9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03 frozen equal
research/recorder/config.py                      112     4773 8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d frozen equal
research/recorder/manifest.py                    254    10002 79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045 frozen equal
research/recorder/analyze.py                     813    34705 eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d frozen equal
research/recorder/probe.py                       227     9324 50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2 frozen equal
research/recorder/selftest.py                    573    30591 c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90 frozen equal
.gitignore                                         5      252 9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b tracked (map equal)
frozen 25 of 25 equal; tracked 2; reported 1
V1 PASS: 6 anchors, 4 re-derived, 25 of 25 frozen equal
```

`SYSTEM-MAP.md` is the `reported` row: 1,080 lines, 217,181 bytes, SHA-256
`7e99182f15edf1d1dbb9b6812bc747a4d321f4145f55b43e223b8918b6338003`. Both `tracked` rows equal the map's values.

### 0.2 Host gate — the opening reads, verbatim (V2)

§0.2's block was run from `/root/btc-5m-twap` as one `bash -c`:

```text
Sun Oct  4 07:31:26 AM UTC 2026
1791099086
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 13356335104
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json
1
exit=1
exit=1
systemd 255 (255.4-1ubuntu8.17)
units exit=1
Linger=no
#KillUserProcesses=no
#KillExcludeUsers=root
483479266	/root/PROJECT_GAMING_PS5
disabled
exit=1
inactive
exit=3
/root/tz16a-work exit=0
/root/tz18a-svc exit=0
/root/tz19-work exit=0
/root/tz20-work exit=1
/root/btc-recorder-svc exit=1
1072
3.12.3 17.1
3.12.3
/root/btc-5m-twap           2d61a16 [main]
/root/tz16a-work/wt         5076b43 [tz-16a-phase2-decisive-gate]
/root/tz16a-work/wt-report  5935ca5 (detached HEAD)
/root/tz19-work/wt-report   b96be84 (detached HEAD)
```

| condition | read | verdict |
|---|---|---|
| H1 — `find` prints exactly one path | `/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json` | PASS |
| H2 — source `/dev/vda2`, size `31612203008`, `grep -c` at least 1 | `/dev/vda2`, `31612203008`, `1` | PASS |
| H3 — both processes down | both `pgrep -fx` printed no line, `exit=1` and `exit=1` | PASS |
| H4 — systemd at least `240` | `systemd 255 (255.4-1ubuntu8.17)` | PASS |
| H5 — `units exit=1` | `units exit=1` | PASS |
| H6 — `/root/tz18a-svc` `0`; `/root/tz20-work`, `/root/btc-recorder-svc` `1` | `0`; `1`, `1` | PASS |
| H6, recorded — `/root/tz16a-work`, `/root/tz19-work` | `0`, `0`: both present, reclaimed by §9 | recorded |
| H7 — forensic store exactly `1,072` files | `1072` | PASS |
| H8 — `3.12.` and a `websockets` version; `3.12.` | `3.12.3 17.1`; `3.12.3` | PASS |
| resource gate — `avail` at least `2,260,000,000` | `13,356,335,104` | PASS |
| recorded, no threshold | `Linger=no`; `#KillUserProcesses=no`, `#KillExcludeUsers=root`; `/root/PROJECT_GAMING_PS5` `483,479,266` bytes; `telemetry-watch.service` `disabled` (1), `inactive` (3); four worktrees | — |

S1 to S7 complete the gate (§2.2): `STATE PASS`.

### 0.3 Free space — every read, its instant, its reader and the bound (§0.3)

The bound is `2,260,000,000` bytes: the chain book's `RESOURCE_FLOOR` `2,200,000,000` plus `60,000,000`.

| instant (UTC) | reader | free bytes | above the bound by |
|---|---|---|---|
| 2026-10-04 07:31:26 | §0.2 `df -B1` (host gate) | `13,356,335,104` | `11,096,335,104` |
| 2026-10-04 07:33:30 | `df -B1`, after B-RECLAIM-OLD | `13,378,670,592` | `11,118,670,592` |
| 2026-10-04 07:39:17 | the recorder's own `start` record, `free_bytes` (`shutil.disk_usage`) | `13,377,339,392` | `11,117,339,392` |
| 2026-10-04 08:27:07 | the recorder's second `start` record, `free_bytes` | `13,375,229,952` | `11,115,229,952` |
| 2026-10-04 08:28:01 | §3.6's repeat of §0.2 `df -B1` (closing) | `13,375,016,960` | `11,115,016,960` |
| after B-RECLAIM-OWN | `df -B1` (§2.17) | `13,375,545,344` at 08:34:09 | `11,115,545,344` |

The chain book also asserts its own floor at start and before every window (`guard_resources`); it prints no
figure. No `asserts` were counted in its `stop` record (§2.10).

### 0.4 Refs (§0.4)

`git ls-remote origin` ran at 07:31:32 UTC, before the branch existed:

```text
Sun Oct  4 07:31:32 AM UTC 2026
2d61a16a0a4314e42369d5af497c07dd97968481	HEAD
2d61a16a0a4314e42369d5af497c07dd97968481	refs/heads/main
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
exit=0

1
2d61a16 Add files via upload
c068361 Update SYSTEM-MAP.md
```

There are 24 ref lines. `refs/heads/main` is at `2d61a16a0a4314e42369d5af497c07dd97968481`, not map §1's
`b96be84`, because two uploads sit above it: `c068361`, revision `2026-10-04-a` of the map, and `2d61a16`, this
TZ. This is recorded, not BLOCKING. `main` carries revision `2026-10-04-a` (the `grep -c` prints `1`), and no
`refs/heads/tz-20-capture-under-systemd` existed. The other 22 lines equal map §1's list.

---

## 1. Input

| read | what | detail |
|---|---|---|
| `CryptoTZ/TZ-20-capture-under-systemd.md` | the TZ, in full, at `2d61a16` | SHA-256 `178f2a33…`, 1,632 lines |
| `SYSTEM-MAP.md` | the map, in full, at `2d61a16` | SHA-256 `7e99182f…`, 1,080 lines |
| the 28 table paths | hashed | §0.1 |
| `/var/lib/btc-recorder/runtime.jsonl` | read by `state`, `start`, `rec`, `restart-rec` and `final`, read-only | `60,690` newlines at `state`, `60,786` at `final` |
| `/var/lib/btc-chainbook/runtime.jsonl` | read by `state`, `start`, `cb`, `restart-cb` and `final`, read-only | `4` records at `state`, `7` at `final` |
| six `manifest.json` | G-REC's intervals `1791099900` … `1791101400`, read once each by `rec`'s deciding run | §2.9 |
| two `window.json` | G-CB's windows `1791099900` and `1791100800`, read once each by `cb`'s deciding run | §2.9 |
| `recorder.log`, `service.log` | `tail -n 40`, §2 item 2 exemption (b) | §2.15 |
| §0.2's `grep -c` and `find` | §2 item 2 exemption (a) | §0.2 and §2.15 |
| the live venue | §3.3's six HTTP requests, two SNTP bursts and one RTDS subscription | §2.5 |
| `/root/tz16a-work/**`, `/root/tz19-work/**`, `/root/tz20-work/**` | hashed whole by `reclaim`; named files copied whole; no value extracted | §2.3, §2.17 |
| `CryptoReports/*.md` | hex runs alone, by `reclaim` | §2.3, §2.17 |

**Nothing was re-collected.** This TZ's commands created nothing under either capture root. The two units wrote
their own trees, as the processes always have.

---

## 2. Measurements

### 2.1 §3.1 — the branch and its three files (V4)

```text
Sun Oct  4 07:31:40 AM UTC 2026
exit=0
Preparing worktree (new branch 'tz-20-capture-under-systemd')
branch 'tz-20-capture-under-systemd' set up to track 'origin/main'.
HEAD is now at 2d61a16 Add files via upload
exit=0
exit=0
```

§3.1's extraction script ran verbatim against the branch worktree's copy of this TZ. It asserted all three hashes,
and `wc`/`sha256sum` follow it:

```text
Sun Oct  4 07:31:50 AM UTC 2026
deploy/systemd/btc-chainbook.service 22 724 a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2
deploy/systemd/btc-recorder.service 23 707 3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1
research/tz20-capture-under-systemd.py 771 36528 104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7
exit=0
   23   707 deploy/systemd/btc-recorder.service
   22   724 deploy/systemd/btc-chainbook.service
  771 36528 research/tz20-capture-under-systemd.py
  816 37959 total
3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1  deploy/systemd/btc-recorder.service
a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2  deploy/systemd/btc-chainbook.service
104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7  research/tz20-capture-under-systemd.py
```

| path | lines | bytes | SHA-256 | TZ's table |
|---|---|---|---|---|
| `deploy/systemd/btc-recorder.service` | 23 | 707 | `3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1` | equal |
| `deploy/systemd/btc-chainbook.service` | 22 | 724 | `a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2` | equal |
| `research/tz20-capture-under-systemd.py` | 771 | 36,528 | `104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7` | equal |

The three files were committed alone as `0956da12bd26decbef0fd643b6f223102c7788ba` (816 insertions, no deletions)
and pushed. The pull request is #21:

```text
Sun Oct  4 07:32:48 AM UTC 2026
remote: 
remote: Create a pull request for 'tz-20-capture-under-systemd' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-20-capture-under-systemd        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-20-capture-under-systemd -> tz-20-capture-under-systemd
branch 'tz-20-capture-under-systemd' set up to track 'origin/tz-20-capture-under-systemd'.
exit=0
```

```text
Sun Oct  4 07:32:57 AM UTC 2026
https://github.com/seahomebatumi-ai/btc-5m-twap/pull/21
exit=0
```

### 2.2 §3.2 — `I state` (V3)

```text
[2026-10-04T07:33:03Z] S1 processes with an argument ending in recorder.py: []
[2026-10-04T07:33:03Z] S2 processes with an argument ending in tz18a-chainbook-capture.py: []
[2026-10-04T07:33:04Z] S3 /var/lib/btc-recorder/runtime.jsonl: 60690 newlines, 60690 records, 0 torn, 4 start, 0 stop, ends with a newline True
[2026-10-04T07:33:04Z] S3 newest start {"captured_bytes": 55159600, "free_bytes": 7871356928, "kind": "start", "recv_ns": 1789206785264516934, "sha": "4216c04673ced76b5b2ac60ef57c9abedc46f9b9"}
[2026-10-04T07:33:04Z] S3 last record {"burst": 4, "ip": "193.70.94.182", "kind": "clock", "offset_ms": -8.15427303314209, "recv_ns": 1790940944342950552, "rejected": {}, "rejected_count": 0, "rtt_ms": 1.077413558959961, "server": "pool.ntp.org"}
[2026-10-04T07:33:04Z] S4 1 start pid 2608993 wall_ns 1790117616052072857 2026-09-22T22:53:36Z
[2026-10-04T07:33:04Z] S4 2 stop pid 2608993 wall_ns 1790145840007723380 2026-09-23T06:44:00Z
[2026-10-04T07:33:04Z] S4 3 start pid 2699889 wall_ns 1790185190022755903 2026-09-23T17:39:50Z
[2026-10-04T07:33:04Z] S4 4 stop pid 2699889 wall_ns 1791017775066372007 2026-10-03T08:56:15Z
[2026-10-04T07:33:04Z] S5 /etc/systemd/system/btc-recorder.service absent
[2026-10-04T07:33:04Z] S5 /etc/systemd/system/btc-chainbook.service absent
[2026-10-04T07:33:04Z] S5 /root/btc-recorder-svc absent
[2026-10-04T07:33:04Z] S6 /root/tz18a-svc/tz18a-chainbook-capture.py sha256 e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae, commit.txt ca4bbc1dd583cbb62f3c0c985938d229b526ce7e
[2026-10-04T07:33:04Z] S7 /root/tz04a-env/venv/bin/python executable
[2026-10-04T07:33:04Z] S7 /root/tz01-env/venv/bin/python executable
[2026-10-04T07:33:04Z] STATE PASS: S1 to S7
[2026-10-04T07:33:04Z] opens under the capture roots: 2
exit=0
```

S1 to S7, seven of seven. S3 read `60,690` newlines with the newest `start` at `1789206785264516934`, sha
`4216c04…`, and the last record at `1790940944342950552`. S4 read four records, the last a `stop` of `2699889` at
`1791017775066372007`. All values equal TZ-19's read.

### 2.3 §9 B-RECLAIM-OLD — after §3.2, before §3.3

`du -sb` was read first, then `reclaim` over both trees. The file-by-file lines (245 `R copied`) are in
Appendix B. The rest of the output, verbatim:

```text
Sun Oct  4 07:33:18 AM UTC 2026
22398514	/root/tz16a-work
4179670	/root/tz19-work
[2026-10-04T07:33:18Z] reclaim: 1532 report tokens; forensic store holds 1072 files
[2026-10-04T07:33:19Z] RECLAIM PASS: 2394 files considered, 244 named by a report, 1 kept by name, 245 copied, 0 already held; forensic store 1072 -> 1317 files
[2026-10-04T07:33:19Z] opens under the capture roots: 0
exit=0
```

| count | value |
|---|---|
| files considered | `2,394` |
| named by a committed report | `244` |
| kept by name (and not also named) | `1` — `/root/tz16a-work/label-ledger.jsonl` |
| copied | `245` |
| already held | `0` |
| forensic store | `1,072` → `1,317`, asserted `after == before + copied` |

Of the copies, `16,384,393` bytes in all: `tz16a-work--wt--*` 70, `tz16a-work--wt-report--*` 68,
`tz16a-work--run-s1--*` 6, `tz16a-work--run-s2--*` 6, `tz16a-work--run-d1--*` 2, `tz16a-work--run-d2--*` 2,
`tz16a-work--label-ledger.jsonl` 1, `tz19-work--wt-report--*` 71, `tz19-work--logs--*` 10 and
`tz19-work--scratch--*` 9. `/root/tz19-work` measured `4,179,670` bytes here, against TZ-19's closing
`4,111,590`. `/root/tz16a-work` measured `22,398,514`, the same as at TZ-19's read.

`RECLAIM PASS` was printed before any removal. Then:

```text
Sun Oct  4 07:33:24 AM UTC 2026
exit=0
exit=0
exit=0
```

```text
Sun Oct  4 07:33:26 AM UTC 2026
exit=0
```

```text
Sun Oct  4 07:33:30 AM UTC 2026
exit=0
```

```text
Sun Oct  4 07:33:30 AM UTC 2026
exit=1
exit=1
/root/btc-5m-twap   2d61a16 [main]
/root/tz20-work/wt  0956da1 [tz-20-capture-under-systemd]
1317
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 13378670592
```

All three `git worktree remove --force` exited `0`, and both `rm -rf` exited `0`; **none was refused by the
classifier**. `test -e` exits `1` for both trees. Two worktrees remain: the primary checkout and this TZ's branch
worktree.

### 2.4 §3.3 — the recorder's tree (V5)

```text
Sun Oct  4 07:34:13 AM UTC 2026
Preparing worktree (detached HEAD 4216c04)
HEAD is now at 4216c04 TZ-05a: Tier C quote snapshots, SNTP reply validation
exit=0
4216c04673ced76b5b2ac60ef57c9abedc46f9b9
9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03  /root/btc-recorder-svc/research/recorder/recorder.py
8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d  /root/btc-recorder-svc/research/recorder/config.py
79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045  /root/btc-recorder-svc/research/recorder/manifest.py
608103	/root/btc-recorder-svc
```

`HEAD` is `4216c04673ced76b5b2ac60ef57c9abedc46f9b9`, and the three hashes equal map §0's frozen rows
(`9fd1c7de…`, `8111dfe4…`, `79c99010…`): 3 of 3. The tree is `608,103` bytes. After both request-path modes ran,
`git status --short` in it printed nothing, so `-B` left no `__pycache__` (§2.5).

### 2.5 §3.3 — the request paths, before either process started (V6, CANON hard rule 14)

`path-recorder` ran from `/root/btc-recorder-svc/research/recorder` under `/root/tz04a-env/venv/bin/python`:

```text
Sun Oct  4 07:34:17 AM UTC 2026
[2026-10-04T07:34:17Z] P0 recorder.py /root/btc-recorder-svc/research/recorder/recorder.py, git_sha 4216c04673ced76b5b2ac60ef57c9abedc46f9b9, websockets 17.1, User-Agent 'btc-5m-twap-recorder/TZ-04a'
[2026-10-04T07:34:17Z] P1 https://gamma-api.polymarket.com/markets/slug/btc-updown-5m-1791099000: served, 4783 bytes, JSON, token ids ['109839917003196335266660461939697493013372937473038681520184674127566169066868', '78701044426166951859941343724644580886039103500917922813749594725846648581938']
[2026-10-04T07:34:17Z] P2 https://clob.polymarket.com/book?token_id=109839917003196335266660461939697493013372937473038681520184674127566169066868: status 200, 2892 bytes, JSON
[2026-10-04T07:34:17Z] P3 SNTP 108.61.73.243 (108.61.73.243): 4 accepted, offset 2.591 ms, rtt 96.372 ms, rejected {}
[2026-10-04T07:34:17Z] P3 SNTP pool.ntp.org (178.215.228.24): 4 accepted, offset 1.941 ms, rtt 17.241 ms, rejected {}
[2026-10-04T07:34:19Z] P4 wss://ws-live-data.polymarket.com: 6 frames in at most 30 s, topics ['crypto_prices', 'crypto_prices_chainlink', 'crypto_prices_twap_sixty', 'crypto_prices_twap_thirty']
[2026-10-04T07:34:19Z] PATH-RECORDER PASS: P0 to P4
[2026-10-04T07:34:19Z] opens under the capture roots: 0
exit=0
```

`path-chainbook` ran under `/root/tz01-env/venv/bin/python`. It is followed by `git status --short` of the
recorder's tree:

```text
Sun Oct  4 07:34:22 AM UTC 2026
[2026-10-04T07:34:22Z] P5 /root/tz18a-svc/tz18a-chainbook-capture.py sha256 e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae; build_request headers [('Accept', 'application/json'), ('User-agent', 'btc-5m-twap-tz18a')]
[2026-10-04T07:34:22Z] P6 document btc-updown-15m-1791099000: status 200, 5159 bytes, sha256 171ef5426090b4b0cead0dec0e08950742218d369d12cb7bbdc88dd35612c2f8, token ids ['63380134452087518376865621372728114927730386442481850859819261057037381792387', '99688941387591643076775467532176647621248931847816808521978669726790995024603']
[2026-10-04T07:34:22Z] P6 document btc-updown-5m-1791099000: status 200, 4783 bytes, sha256 cd9f99d99f80c343abec69d19dcc03e6292c0ec0af8b38c0b3841eed622499fd, token ids ['109839917003196335266660461939697493013372937473038681520184674127566169066868', '78701044426166951859941343724644580886039103500917922813749594725846648581938']
[2026-10-04T07:34:22Z] P7 /book btc-updown-15m-1791099000 token 63380134452087518376865621372728114927730386442481850859819261057037381792387: status 200, 2860 bytes, JSON
[2026-10-04T07:34:22Z] P7 /book btc-updown-5m-1791099000 token 109839917003196335266660461939697493013372937473038681520184674127566169066868: status 200, 2890 bytes, JSON
[2026-10-04T07:34:22Z] PATH-CHAINBOOK PASS: P5 to P7, 4 requests
[2026-10-04T07:34:22Z] opens under the capture roots: 0
exit=0
status exit=0
```

| item | result |
|---|---|
| P0 — `recorder.py` and `config.py` from the new tree, `git_sha()` | `4216c04…`, PASS |
| P1 — the market document of `btc-updown-5m-1791099000` through `recorder.fetch` | served, `4,783` bytes, JSON, two token ids — PASS |
| P2 — the first token's book through `recorder.fetch_status` | `200`, `2,892` bytes, JSON — PASS |
| P3 — SNTP through `recorder.sntp_best` | **2 of 2 answered**: `108.61.73.243` 4 accepted, `pool.ntp.org` (`178.215.228.24`) 4 accepted, none rejected — PASS |
| P4 — RTDS as `rtds()` subscribes | 6 frames, **4 of 4** topics within 30 s, both required ones present — PASS |
| P5 — the service's copy, its hash, `SERVICE_ARGV`, `build_request`'s headers | `e9cb9b47…`; `Accept: application/json`, `User-Agent: btc-5m-twap-tz18a` — PASS |
| P6 — `btc-updown-15m-1791099000` and `btc-updown-5m-1791099000` through `http_get`, `0.2` s apart | `200`, `5,159` and `4,783` bytes, two token ids each — PASS |
| P7 — one book of each | `200`, `2,860` and `2,890` bytes, JSON — PASS |
| requests | 2 through the recorder's functions and 4 through `http_get` (`COUNTERS["requests"] == 4` asserted): **6 HTTP**, 2 SNTP bursts, 1 RTDS subscription |

P1 and P6's five-minute request name the same slug, `btc-updown-5m-1791099000`, read 5 s apart through the two
processes' functions. Every header is the fixed one §3.3 names.

### 2.6 §3.4 — B-INSTALL (V7)

```text
Sun Oct  4 07:34:27 AM UTC 2026
exit=0
exit=0
exit=0
exit=0
```

Both `cmp` exited `0`, and so did `daemon-reload`. `systemd-analyze verify` printed nothing and exited `0`, with no
finding on either unit or on any other unit. B-INSTALL was not refused.

### 2.7 §3.4 — B-START-REC and B-START-CB: refused, then run by the Boss

The Executor ran the `start-rec` mark and B-START-REC as one command. **The session's classifier refused the whole
command** — "Permission for this action was denied by the Claude Code auto mode classifier. Reason: [Unauthorized
Persistence]" — so neither part ran. The Executor confirmed that `instants.json` was absent and that both units
were `disabled`/`inactive`. It then took both marks, in order, before handing either block over:

```text
[2026-10-04T07:35:15Z] MARK start-rec {"cb_pid": 0, "ns": 1791099315100620892, "rec_pid": 0} (2026-10-04T07:35:15Z)
[2026-10-04T07:35:15Z] opens under the capture roots: 0
exit=0
```

```text
[2026-10-04T07:35:16Z] MARK start-cb {"cb_pid": 0, "ns": 1791099316160377527, "rec_pid": 0} (2026-10-04T07:35:16Z)
[2026-10-04T07:35:16Z] opens under the capture roots: 0
exit=0
```

```text
Sun Oct  4 07:35:16 AM UTC 2026 B-START-REC refused by the session's permission classifier ([Unauthorized Persistence]) when the Executor ran: systemctl enable --now btc-recorder.service; nothing ran (instants.json absent, both units disabled/inactive). Marks start-rec and start-cb taken by the Executor; B-START-REC and B-START-CB handed to the Boss.
```

The Boss ran both blocks verbatim in a root shell on the VPS, B-START-REC first. His account, pasted into the
session, follows. It is recorded here and is not the verification:

```text
The Boss's account, pasted into the session (not the verification; see 21-...):
root@vultr:~# systemctl enable --now btc-recorder.service; echo "exit=$?"
Created symlink /etc/systemd/system/multi-user.target.wants/btc-recorder.service → /etc/systemd/system/btc-recorder.service.
exit=0
root@vultr:~# systemctl enable --now btc-chainbook.service; echo "exit=$?"
Created symlink /etc/systemd/system/multi-user.target.wants/btc-chainbook.service → /etc/systemd/system/btc-chainbook.service.
exit=0
```

**Verified by the Executor at 07:41:14 UTC**, from systemd:

```text
Sun Oct  4 07:41:14 AM UTC 2026
1791099674
enabled
enabled
exit=0
active
active
exit=0
MainPID=4060666
NRestarts=0
ExecMainStartTimestamp=Sun 2026-10-04 07:39:16 UTC
Id=btc-recorder.service

MainPID=4060777
NRestarts=0
ExecMainStartTimestamp=Sun 2026-10-04 07:39:45 UTC
Id=btc-chainbook.service
```

B-START-REC took effect at 07:39:16 UTC and B-START-CB at 07:39:45. That is `242.8` s and `269.4` s after their
marks, by the start records (§2.8).

### 2.8 §3.5 step 1 — G-UNIT at 0 restarts, then G-START

`I unit 0` ran at 07:41:22, `96` s after B-START-CB took effect:

```text
Sun Oct  4 07:41:22 AM UTC 2026
[2026-10-04T07:41:22Z] U btc-recorder.service {"ActiveState": "active", "ControlGroup": "/system.slice/btc-recorder.service", "ExecMainStartTimestamp": "Sun 2026-10-04 07:39:16 UTC", "FragmentPath": "/etc/systemd/system/btc-recorder.service", "MainPID": "4060666", "MemoryCurrent": "225062912", "MemoryMax": "536870912", "MemoryPeak": "226471936", "NRestarts": "0", "Result": "success", "SubState": "running", "UnitFileState": "enabled"}
[2026-10-04T07:41:22Z] G-UNIT btc-recorder.service: pid 4060666, argv equal, cgroup /system.slice/btc-recorder.service, NRestarts 0, MemoryMax 536870912; memory in use 225062912, peak 226471936 (recorded)
[2026-10-04T07:41:22Z] U btc-chainbook.service {"ActiveState": "active", "ControlGroup": "/system.slice/btc-chainbook.service", "ExecMainStartTimestamp": "Sun 2026-10-04 07:39:45 UTC", "FragmentPath": "/etc/systemd/system/btc-chainbook.service", "MainPID": "4060777", "MemoryCurrent": "18632704", "MemoryMax": "201326592", "MemoryPeak": "21262336", "NRestarts": "0", "Result": "success", "SubState": "running", "UnitFileState": "enabled"}
[2026-10-04T07:41:22Z] G-UNIT btc-chainbook.service: pid 4060777, argv equal, cgroup /system.slice/btc-chainbook.service, NRestarts 0, MemoryMax 201326592; memory in use 18632704, peak 21262336 (recorded)
[2026-10-04T07:41:22Z] G-UNIT PASS: 2 of 2 units, sole instances 4060666 and 4060777, NRestarts 0 each
[2026-10-04T07:41:22Z] opens under the capture roots: 0
exit=0
```

```text
Sun Oct  4 07:41:22 AM UTC 2026
[2026-10-04T07:41:23Z] R {"captured_bytes": 567066220, "free_bytes": 13377339392, "kind": "start", "recv_ns": 1791099557936046519, "sha": "4216c04673ced76b5b2ac60ef57c9abedc46f9b9"}
[2026-10-04T07:41:23Z] R {"detected_recv_ns": 1791099558966009182, "end_recv_ns": 1791099559177430242, "kind": "disconnect", "reason": "startup", "start_recv_ns": 1790940978479700775}
[2026-10-04T07:41:23Z] G-START recorder: start 2026-10-04T07:39:17Z sha 4216c04673ced76b5b2ac60ef57c9abedc46f9b9, free 13377339392, captured 567066220; the gap 2026-10-02T11:36:18Z to 2026-10-04T07:39:19Z, 158580.7 s
[2026-10-04T07:41:23Z] C {"argv": ["/root/tz18a-svc/tz18a-chainbook-capture.py", "--serve"], "commit": "ca4bbc1dd583cbb62f3c0c985938d229b526ce7e", "event": "start", "file_sha256": "e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae", "pid": 4060777, "wall_ns": 1791099585558186401}
[2026-10-04T07:41:23Z] G-START chain book: start 2026-10-04T07:39:45Z pid 4060777 commit ca4bbc1dd583cbb62f3c0c985938d229b526ce7e
[2026-10-04T07:41:23Z] G-START PASS: 2 of 2
[2026-10-04T07:41:23Z] opens under the capture roots: 2
exit=0
```

### 2.9 §3.5 steps 2 and 4 — G-CB and G-REC, every run

Runs were spaced at most 600 s apart. Every NOT YET exited `3`.

| run | instant (UTC) | `cb` | `rec` |
|---|---|---|---|
| 1 | 07:41:36 | NOT YET — `1791099900`, `1791100800` pending | NOT YET — all six pending |
| 2 | 07:51:24 / 07:51:25 | NOT YET — both pending | NOT YET — all six pending |
| 3 | 08:01:12 | NOT YET — `1791100800` pending | NOT YET — five pending |
| 4 | 08:10:49 | NOT YET — `1791100800` pending | NOT YET — `1791101100`, `1791101400` pending |
| 5 | 08:15:53 / 08:15:54 | **PASS** | NOT YET — `1791101400` pending |
| 6 | 08:22:00 | — | **PASS** |

`cb` ran 5 times and `rec` 6 times, within §6's bounds of 5 and 13. The gaps between consecutive runs were 588,
588, 577 and 304 s for `cb`, and 589, 587, 577, 305 and 366 s for `rec`. The NOT YET runs, verbatim:

```text
Sun Oct  4 07:41:36 AM UTC 2026
[2026-10-04T07:41:36Z] NOT YET: windows [1791099900, 1791100800] pending, the last deadline 2026-10-04T08:16:05Z; run this mode again at or after 2026-10-04T07:46:36Z
exit=3
```
```text
Sun Oct  4 07:41:36 AM UTC 2026
[2026-10-04T07:41:36Z] NOT YET: intervals [1791099900, 1791100200, 1791100500, 1791100800, 1791101100, 1791101400] pending, the last deadline 2026-10-04T09:15:00Z; run this mode again at or after 2026-10-04T07:46:36Z
exit=3
```
```text
Sun Oct  4 07:51:24 AM UTC 2026
[2026-10-04T07:51:24Z] NOT YET: windows [1791099900, 1791100800] pending, the last deadline 2026-10-04T08:16:05Z; run this mode again at or after 2026-10-04T07:56:24Z
exit=3
```
```text
Sun Oct  4 07:51:24 AM UTC 2026
[2026-10-04T07:51:25Z] NOT YET: intervals [1791099900, 1791100200, 1791100500, 1791100800, 1791101100, 1791101400] pending, the last deadline 2026-10-04T09:15:00Z; run this mode again at or after 2026-10-04T07:56:25Z
exit=3
```
```text
Sun Oct  4 08:01:12 AM UTC 2026
[2026-10-04T08:01:12Z] NOT YET: windows [1791100800] pending, the last deadline 2026-10-04T08:16:05Z; run this mode again at or after 2026-10-04T08:06:12Z
exit=3
```
```text
Sun Oct  4 08:01:12 AM UTC 2026
[2026-10-04T08:01:12Z] NOT YET: intervals [1791100200, 1791100500, 1791100800, 1791101100, 1791101400] pending, the last deadline 2026-10-04T09:15:00Z; run this mode again at or after 2026-10-04T08:06:12Z
exit=3
```
```text
Sun Oct  4 08:10:49 AM UTC 2026
[2026-10-04T08:10:49Z] NOT YET: windows [1791100800] pending, the last deadline 2026-10-04T08:16:05Z; run this mode again at or after 2026-10-04T08:15:49Z
exit=3
```
```text
Sun Oct  4 08:10:49 AM UTC 2026
[2026-10-04T08:10:49Z] NOT YET: intervals [1791101100, 1791101400] pending, the last deadline 2026-10-04T09:15:00Z; run this mode again at or after 2026-10-04T08:15:49Z
exit=3
```
```text
Sun Oct  4 08:15:53 AM UTC 2026
[2026-10-04T08:15:54Z] NOT YET: intervals [1791101400] pending, the last deadline 2026-10-04T09:15:00Z; run this mode again at or after 2026-10-04T08:20:54Z
exit=3
```

The deciding runs:

```text
Sun Oct  4 08:15:53 AM UTC 2026
[2026-10-04T08:15:53Z] G-CB window 1791099900 2026-10-04T07:45:00Z: documents_ok True, checkpoints_complete 7 of 7, missed 0, status_counts {"200": 28}
[2026-10-04T08:15:53Z] G-CB window 1791100800 2026-10-04T08:00:00Z: documents_ok True, checkpoints_complete 7 of 7, missed 0, status_counts {"200": 28}
[2026-10-04T08:15:53Z] G-CB PASS: windows 2 of 2, documents_ok 2 of 2, missed 0 at 2 of 2, checkpoints complete 14 of 14, PASS at 13 or more
[2026-10-04T08:15:53Z] opens under the capture roots: 3
exit=0
```

```text
Sun Oct  4 08:22:00 AM UTC 2026
[2026-10-04T08:22:00Z] G-REC interval 1791099900 2026-10-04T07:45:00Z: complete True, quotes_complete True, disconnects 0, gamma_present True, resolution_present True, clock |offset| max 24.651765823364258 ms, sha 4216c04673ced76b5b2ac60ef57c9abedc46f9b9
[2026-10-04T08:22:00Z] G-REC interval 1791100200 2026-10-04T07:50:00Z: complete True, quotes_complete True, disconnects 0, gamma_present True, resolution_present True, clock |offset| max 26.319265365600586 ms, sha 4216c04673ced76b5b2ac60ef57c9abedc46f9b9
[2026-10-04T08:22:00Z] G-REC interval 1791100500 2026-10-04T07:55:00Z: complete True, quotes_complete True, disconnects 0, gamma_present True, resolution_present True, clock |offset| max 27.254581451416016 ms, sha 4216c04673ced76b5b2ac60ef57c9abedc46f9b9
[2026-10-04T08:22:00Z] G-REC interval 1791100800 2026-10-04T08:00:00Z: complete True, quotes_complete True, disconnects 0, gamma_present True, resolution_present True, clock |offset| max 6.338238716125488 ms, sha 4216c04673ced76b5b2ac60ef57c9abedc46f9b9
[2026-10-04T08:22:00Z] G-REC interval 1791101100 2026-10-04T08:05:00Z: complete True, quotes_complete True, disconnects 0, gamma_present True, resolution_present True, clock |offset| max 23.922324180603027 ms, sha 4216c04673ced76b5b2ac60ef57c9abedc46f9b9
[2026-10-04T08:22:00Z] G-REC interval 1791101400 2026-10-04T08:10:00Z: complete True, quotes_complete True, disconnects 0, gamma_present True, resolution_present True, clock |offset| max 23.922324180603027 ms, sha 4216c04673ced76b5b2ac60ef57c9abedc46f9b9
[2026-10-04T08:22:00Z] G-REC PASS: manifests 6 of 6, quotes_complete 6 of 6, sha 6 of 6, complete 6 of 6, PASS at 4 or more
[2026-10-04T08:22:00Z] opens under the capture roots: 7
exit=0
```

**G-CB's population**: the chain book's start record is at `w0` = 07:39:45.558. The first `T ≡ 0 (mod 900)` with
`T + 625 >= w0 + 60` is `1791099900` (07:45:00), then `1791100800` (08:00:00). Window `1791099000`, which the
service also ran because it started before `T + 624`, does not qualify, because its document instant 07:40:25
falls 20 s short of `w0 + 60`.

**G-REC's population**: the recorder's start record is at `r0` = 07:39:17.936. The first `T0 ≡ 0 (mod 300)` with
`T0 − 90 >= r0 + 60` is `1791099900`, and the six run to `1791101400` (08:10:00). Their deadlines, `T0 + 3,900`,
run 08:50:00 to 09:15:00, and all six manifests were present at 08:22:00.

### 2.10 §3.5 step 3 — B-KILL-CB and G-RESTART-C

G-UNIT, G-START and G-CB read PASS by 08:15:53, when `now % 900` was `53`, inside `[15, 480]`. The mark came
first, then the block. **The classifier did not refuse it**:

```text
Sun Oct  4 08:16:09 AM UTC 2026
now%900=69
[2026-10-04T08:16:09Z] MARK kill-cb {"cb_pid": 4060777, "ns": 1791101769207752242, "rec_pid": 4060666} (2026-10-04T08:16:09Z)
[2026-10-04T08:16:09Z] opens under the capture roots: 0
exit=0
```

```text
Sun Oct  4 08:16:12 AM UTC 2026
now%900=72
exit=0
```

The signal went at `now % 900` = `72`, at 08:16:12 UTC. That is inside window `1791101700`'s idle stretch, between
the close of `1791100800` at 08:15:05 and `1791101700`'s document at 08:25:25. `I restart-cb` ran 44 s later:

```text
Sun Oct  4 08:16:56 AM UTC 2026
[2026-10-04T08:16:56Z] G-RESTART-C records since start-cb: [('start', 4060777, 1791099585558186401), ('stop', 4060777, 1791101773011104496), ('start', 4064090, 1791101778487584488)]
[2026-10-04T08:16:56Z] U btc-chainbook.service {"ActiveState": "active", "ControlGroup": "/system.slice/btc-chainbook.service", "ExecMainStartTimestamp": "Sun 2026-10-04 08:16:18 UTC", "FragmentPath": "/etc/systemd/system/btc-chainbook.service", "MainPID": "4064090", "MemoryCurrent": "18501632", "MemoryMax": "201326592", "MemoryPeak": "18735104", "NRestarts": "1", "Result": "success", "SubState": "running", "UnitFileState": "enabled"}
[2026-10-04T08:16:56Z] G-UNIT btc-chainbook.service: pid 4064090, argv equal, cgroup /system.slice/btc-chainbook.service, NRestarts 1, MemoryMax 201326592; memory in use 18501632, peak 18735104 (recorded)
[2026-10-04T08:16:56Z] G-RESTART-C PASS: stop of 4060777 at 2026-10-04T08:16:13Z with counters {"asserts": 0, "bytes_written": 75318, "recorder_opens": 0, "requests": 90, "write_checks": 12}; start of 4064090 5.5 s later
[2026-10-04T08:16:56Z] opens under the capture roots: 1
exit=0
```

The records since the `start-cb` mark are exactly `start` (`4060777`), `stop` (`4060777`, at
`1791101773011104496`, 08:16:13.011, `3.80` s after the mark) and `start` (`4064090`, at `1791101778487584488`,
08:16:18.487). The new start came **`5.476` s** after the stop, against the bound of 60. Commit and file hash
equal, `NRestarts` `1`. **No window was lost:** `service.log` (§2.15) shows window `1791101700`'s documents and
checkpoints served by the new process from 08:25:25.

### 2.11 §3.5 step 5 — B-KILL-REC and G-RESTART-R

G-REC and G-RESTART-C read PASS by 08:22:00. The first instant after that at which `now % 300` lay in
`[122, 128]` was 08:22:02 to 08:22:08. It passed while the Executor was reading G-REC's output: `now % 300` read
`123` at 08:22:03, too late to take the mark and then send the signal inside the stretch. **The block ran at the
next such stretch, 08:27:02 to 08:27:08** (§6 item 3). A timed script took the mark at `T0 + 119`, for
`T0 = 1791102300`. It then waited for `T0 + 122`, re-checked that `now % 300` lay in `[122, 128]` (and would have
sent nothing otherwise), and ran the block verbatim. **The classifier did not refuse it**:

```text
Sun Oct  4 08:26:59 AM UTC 2026
now%300=119
[2026-10-04T08:26:59Z] MARK kill-rec {"cb_pid": 4064090, "ns": 1791102419149894359, "rec_pid": 4060666} (2026-10-04T08:26:59Z)
[2026-10-04T08:26:59Z] opens under the capture roots: 0
exit=0
```

```text
Sun Oct  4 08:27:02 AM UTC 2026
1791102422.039193456
now%300=122
exit=0
```

The signal went at `1791102422.039` (08:27:02.039 UTC), `now % 300` = `122`. `I restart-rec` ran 35 s later:

```text
Sun Oct  4 08:27:37 AM UTC 2026
[2026-10-04T08:27:37Z] R {"captured_bytes": 567066220, "free_bytes": 13377339392, "kind": "start", "recv_ns": 1791099557936046519, "sha": "4216c04673ced76b5b2ac60ef57c9abedc46f9b9"}
[2026-10-04T08:27:37Z] R {"captured_bytes": 567966600, "free_bytes": 13375229952, "kind": "start", "recv_ns": 1791102427832661053, "sha": "4216c04673ced76b5b2ac60ef57c9abedc46f9b9"}
[2026-10-04T08:27:37Z] R {"detected_recv_ns": 1791099558966009182, "end_recv_ns": 1791099559177430242, "kind": "disconnect", "reason": "startup", "start_recv_ns": 1790940978479700775}
[2026-10-04T08:27:37Z] R {"detected_recv_ns": 1791102428182744930, "end_recv_ns": 1791102428372998387, "kind": "disconnect", "reason": "startup", "start_recv_ns": 1791102421438750212}
[2026-10-04T08:27:37Z] U btc-recorder.service {"ActiveState": "active", "ControlGroup": "/system.slice/btc-recorder.service", "ExecMainStartTimestamp": "Sun 2026-10-04 08:27:07 UTC", "FragmentPath": "/etc/systemd/system/btc-recorder.service", "MainPID": "4067771", "MemoryCurrent": "91164672", "MemoryMax": "536870912", "MemoryPeak": "102223872", "NRestarts": "1", "Result": "success", "SubState": "running", "UnitFileState": "enabled"}
[2026-10-04T08:27:37Z] G-UNIT btc-recorder.service: pid 4067771, argv equal, cgroup /system.slice/btc-recorder.service, NRestarts 1, MemoryMax 536870912; memory in use 91164672, peak 102223872 (recorded)
[2026-10-04T08:27:37Z] G-RESTART-R PASS: pid 4060666 replaced by 4067771; the gap 2026-10-04T08:27:01Z to 2026-10-04T08:27:08Z, 6.9 s, recorded
[2026-10-04T08:27:37Z] opens under the capture roots: 1
exit=0
```

Since the `start-rec` mark there are exactly two `start` records, the second at `1791102427832661053`
(08:27:07.833), `8.68` s after the `kill-rec` mark, sha `4216c04…`. There are exactly two `startup` gaps, the
second starting at `1791102421438750212`. That is `2.289` s after the mark, so not earlier than `mark − 5 s`, and
before the second start. It lasted **`6.934` s** against the bound of 60. There is no `halt`. `NRestarts` is `1`,
and MainPID `4067771` differs from the mark's `4060666`.

### 2.12 §3.5 step 6 — `I final` (V14)

```text
Sun Oct  4 08:27:50 AM UTC 2026
[2026-10-04T08:27:50Z] U btc-recorder.service {"ActiveState": "active", "ControlGroup": "/system.slice/btc-recorder.service", "ExecMainStartTimestamp": "Sun 2026-10-04 08:27:07 UTC", "FragmentPath": "/etc/systemd/system/btc-recorder.service", "MainPID": "4067771", "MemoryCurrent": "91250688", "MemoryMax": "536870912", "MemoryPeak": "102223872", "NRestarts": "1", "Result": "success", "SubState": "running", "UnitFileState": "enabled"}
[2026-10-04T08:27:50Z] G-UNIT btc-recorder.service: pid 4067771, argv equal, cgroup /system.slice/btc-recorder.service, NRestarts 1, MemoryMax 536870912; memory in use 91250688, peak 102223872 (recorded)
[2026-10-04T08:27:50Z] U btc-chainbook.service {"ActiveState": "active", "ControlGroup": "/system.slice/btc-chainbook.service", "ExecMainStartTimestamp": "Sun 2026-10-04 08:16:18 UTC", "FragmentPath": "/etc/systemd/system/btc-chainbook.service", "MainPID": "4064090", "MemoryCurrent": "12701696", "MemoryMax": "201326592", "MemoryPeak": "18735104", "NRestarts": "1", "Result": "success", "SubState": "running", "UnitFileState": "enabled"}
[2026-10-04T08:27:50Z] G-UNIT btc-chainbook.service: pid 4064090, argv equal, cgroup /system.slice/btc-chainbook.service, NRestarts 1, MemoryMax 201326592; memory in use 12701696, peak 18735104 (recorded)
[2026-10-04T08:27:50Z] G-UNIT PASS: 2 of 2 units, sole instances 4067771 and 4064090, NRestarts 1 each
[2026-10-04T08:27:51Z] FINAL recorder runtime.jsonl: 60786 newlines, 0 torn; since start-rec {"clock": 92, "disconnect": 2, "start": 2}
[2026-10-04T08:27:51Z] FINAL chain book runtime.jsonl: 7 records, 0 torn; since start-cb ['start', 'stop', 'start']
[2026-10-04T08:27:51Z] FINAL PASS: recorder pid 4067771, chain book pid 4064090, newest recorder start sha 4216c04673ced76b5b2ac60ef57c9abedc46f9b9
[2026-10-04T08:27:51Z] opens under the capture roots: 2
exit=0
```

Since `start-rec` the recorder wrote `2` `start`, `2` `disconnect` (both `startup`) and `92` `clock` records, and
no `halt`. Since `start-cb` the chain book wrote `start`, `stop`, `start`. No torn line in either file. From
B-START-REC's effect at 07:39:16 to `I final` at 08:27:50 was `2,914` s, against §6's bound of `6,500`.

### 2.13 The gap — every `startup` record G-START and G-RESTART-R read

| record | `start_recv_ns` | `detected_recv_ns` | `end_recv_ns` | duration |
|---|---|---|---|---|
| G-START's: the capture lost since 2026-10-02 | `1790940978479700775` — **2026-10-02 11:36:18.479 UTC** | `1791099558966009182` — 2026-10-04 07:39:18.966 | `1791099559177430242` — 2026-10-04 07:39:19.177 | `158,580.698` s |
| G-RESTART-R's: the stray `SIGTERM` | `1791102421438750212` — 2026-10-04 08:27:01.438 | `1791102428182744930` — 08:27:08.182 | `1791102428372998387` — 08:27:08.372 | `6.934` s |

The first gap starts inside G-START's bound,
`[1790940810 × 10^9, 1790941110 × 10^9)` = `[11:33:30, 11:38:30)` on 2026-10-02. **Its start is the old
recorder's last frame on disk, 2026-10-02 11:36:18.479 UTC.** That is the second in which TZ-19's report §3.2 puts
logind's removal of root's session 7379. This reading names the instant and nothing more: the pid-to-session link
is still not read. The gap is recorded and not filled. By the recorder's own log (§2.15), the first new interval it
opened was `1791099300`, with five checkpoints already passed. RTDS holds no replay, so the `527` intervals
`1790941200` to `1791099000` were never captured. The chain book's first window after its start was
`1791099000`, so the `90` windows `1791018000` to `1791098100` are lost too.

### 2.14 Memory — each unit's memory in use and its peak at every read, and the host's

| read | instant (UTC) | recorder in use / peak (bytes) | chain book in use / peak (bytes) |
|---|---|---|---|
| G-UNIT, `I unit 0` | 07:41:22 | `225,062,912` / `226,471,936` | `18,632,704` / `21,262,336` |
| G-UNIT inside `I restart-cb` | 08:16:56 | — | `18,501,632` / `18,735,104` |
| G-UNIT inside `I restart-rec` | 08:27:37 | `91,164,672` / `102,223,872` | — |
| G-UNIT inside `I final` | 08:27:50 | `91,250,688` / `102,223,872` | `12,701,696` / `18,735,104` |
| §3.6 `systemctl show` | 08:28:08 | `45,346,816` / `102,223,872` | `10,178,560` / `18,735,104` |
| journal, the first recorder process's whole life, 07:39:16–08:27:02 | 08:27:02 | **`215.9M` memory peak, `17.8M` memory swap peak**, `11.236` s CPU | — |

`MemoryMax` reads `536870912` and `201326592` at every read, as asserted. **The peak is per process start:** each
unit's `MemoryPeak` reset when systemd restarted it, so the peaks read at `I final` are the second processes',
`102,223,872` and `18,735,104`. The first recorder's whole-life peak is in the journal only, `215.9M`. That
peak is at least the `226,471,936` bytes (`215.98` MiB) read at 07:41:22, 126 s after the start. systemd prints
one truncated decimal, so `215.9M` puts it below `216.0` MiB: within `0.02` MiB of that early read. What filled
it was not read. `MemoryCurrent` is the control group's charge, page cache
included.

**The host, `free -b` at 08:28:08:** total `1,002,127,360` bytes of memory, `271,712,256` available,
`378,605,568` buff/cache; swap `3,250,581,504` total, `722,706,432` used. **The recorder's ceiling,
`536,870,912`, is 53.6% of the host's total memory, and the two ceilings together, `738,197,504`, are 73.7% of
it.** No ceiling was reached, and no unit restarted except by B-KILL-CB or B-KILL-REC. No `MemorySwapMax` is set
in either unit, and the first recorder process used swap (17.8M at its peak). This is recorded for the map's next
revision, as §3.6 asks, and carries no threshold here.

### 2.15 §3.6 — the closing reads (V16)

§0.2's block again, at 08:28:01 UTC:

```text
Sun Oct  4 08:28:01 AM UTC 2026
1791102481
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 13375016960
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json
3
4067771
exit=0
4064090
exit=0
systemd 255 (255.4-1ubuntu8.17)
units exit=0
Linger=no
#KillUserProcesses=no
#KillExcludeUsers=root
484056746	/root/PROJECT_GAMING_PS5
disabled
exit=1
inactive
exit=3
/root/tz16a-work exit=1
/root/tz18a-svc exit=0
/root/tz19-work exit=1
/root/tz20-work exit=0
/root/btc-recorder-svc exit=0
1317
3.12.3 17.1
3.12.3
/root/btc-5m-twap       2d61a16 [main]
/root/btc-recorder-svc  4216c04 (detached HEAD)
/root/tz20-work/wt      0956da1 [tz-20-capture-under-systemd]
```

Each `pgrep -fx` now prints exactly one pid, `4067771` and `4064090`, the units' MainPIDs. `units exit=0`. The
`grep -c` now reads `3`: the old start record and the two new ones. `/root/tz16a-work` and `/root/tz19-work` read
`exit=1`. The store holds `1317` files. The consumer reads `disabled` (1) and `inactive` (3), the tree at
`484,056,746` bytes: disabled and inactive at both of this TZ's reads, twenty-eight such reads running, and
`577,480` bytes larger than at the host gate `3,395` s earlier.

The rest of §3.6, at 08:28:08 UTC, verbatim:

```text
Sun Oct  4 08:28:08 AM UTC 2026
enabled
enabled
exit=0
active
active
exit=0
2026-10-04T07:39:16+00:00 vultr systemd[1]: Started btc-recorder.service - btc-5m-twap recorder, Tier A and Tier C.
2026-10-04T07:39:45+00:00 vultr systemd[1]: Started btc-chainbook.service - btc-5m-twap chain book, fifteen-minute and five-minute books.
2026-10-04T08:16:12+00:00 vultr systemd[1]: btc-chainbook.service: Sent signal SIGTERM to main process 4060777 (python) on client request.
2026-10-04T08:16:13+00:00 vultr systemd[1]: btc-chainbook.service: Deactivated successfully.
2026-10-04T08:16:18+00:00 vultr systemd[1]: btc-chainbook.service: Scheduled restart job, restart counter is at 1.
2026-10-04T08:16:18+00:00 vultr systemd[1]: Started btc-chainbook.service - btc-5m-twap chain book, fifteen-minute and five-minute books.
2026-10-04T08:27:02+00:00 vultr systemd[1]: btc-recorder.service: Sent signal SIGTERM to main process 4060666 (python) on client request.
2026-10-04T08:27:02+00:00 vultr systemd[1]: btc-recorder.service: Deactivated successfully.
2026-10-04T08:27:02+00:00 vultr systemd[1]: btc-recorder.service: Consumed 11.236s CPU time, 215.9M memory peak, 17.8M memory swap peak.
2026-10-04T08:27:07+00:00 vultr systemd[1]: btc-recorder.service: Scheduled restart job, restart counter is at 1.
2026-10-04T08:27:07+00:00 vultr systemd[1]: Started btc-recorder.service - btc-5m-twap recorder, Tier A and Tier C.
--- tail recorder.log
2026-10-02T10:18:33Z closed 1790935800 complete=False quotes_complete=True msgs={'twap60': 382, 'twap30': 384, 'chainlink': 384, 'binance': 390}
2026-10-02T10:23:33Z closed 1790936100 complete=True quotes_complete=True msgs={'twap60': 413, 'twap30': 414, 'chainlink': 414, 'binance': 420}
2026-10-02T10:28:49Z closed 1790936400 complete=True quotes_complete=True msgs={'twap60': 417, 'twap30': 418, 'chainlink': 418, 'binance': 420}
2026-10-02T10:33:03Z closed 1790936700 complete=True quotes_complete=True msgs={'twap60': 410, 'twap30': 411, 'chainlink': 410, 'binance': 420}
2026-10-02T10:38:19Z closed 1790937000 complete=True quotes_complete=True msgs={'twap60': 405, 'twap30': 406, 'chainlink': 405, 'binance': 420}
2026-10-02T10:44:04Z closed 1790937300 complete=True quotes_complete=True msgs={'twap60': 419, 'twap30': 418, 'chainlink': 419, 'binance': 420}
2026-10-02T10:50:49Z closed 1790937600 complete=True quotes_complete=True msgs={'twap60': 420, 'twap30': 419, 'chainlink': 420, 'binance': 420}
2026-10-02T10:53:19Z closed 1790937900 complete=True quotes_complete=True msgs={'twap60': 418, 'twap30': 417, 'chainlink': 418, 'binance': 420}
2026-10-02T10:59:18Z closed 1790938200 complete=True quotes_complete=True msgs={'twap60': 413, 'twap30': 412, 'chainlink': 412, 'binance': 420}
2026-10-02T11:04:34Z closed 1790938500 complete=True quotes_complete=True msgs={'twap60': 411, 'twap30': 412, 'chainlink': 412, 'binance': 420}
2026-10-02T11:08:19Z closed 1790938800 complete=True quotes_complete=True msgs={'twap60': 415, 'twap30': 415, 'chainlink': 414, 'binance': 420}
2026-10-02T11:13:49Z closed 1790939100 complete=True quotes_complete=True msgs={'twap60': 417, 'twap30': 416, 'chainlink': 416, 'binance': 420}
2026-10-02T11:19:03Z closed 1790939400 complete=True quotes_complete=True msgs={'twap60': 413, 'twap30': 414, 'chainlink': 415, 'binance': 420}
2026-10-02T11:24:48Z closed 1790939700 complete=True quotes_complete=True msgs={'twap60': 409, 'twap30': 410, 'chainlink': 409, 'binance': 420}
2026-10-02T11:30:03Z closed 1790940000 complete=True quotes_complete=True msgs={'twap60': 411, 'twap30': 411, 'chainlink': 410, 'binance': 420}
2026-10-02T11:33:48Z closed 1790940300 complete=True quotes_complete=True msgs={'twap60': 419, 'twap30': 418, 'chainlink': 419, 'binance': 420}
2026-10-04T07:39:16Z recorder sha=4216c04673ced76b5b2ac60ef57c9abedc46f9b9 root=/var/lib/btc-recorder
2026-10-04T07:39:17Z pre-run floors: free=13377339392 (floor 2000000000) captured=567066220 (cap 4000000000)
2026-10-04T07:39:18Z recovering interval 1790940600
2026-10-04T07:39:18Z recovering interval 1790940900
2026-10-04T07:39:18Z S7 unresolved at deadline for 1790940600
2026-10-04T07:39:18Z closed 1790940600 complete=False quotes_complete=True msgs={'twap60': 415, 'twap30': 416, 'chainlink': 415, 'binance': 420}
2026-10-04T07:39:18Z S7 unresolved at deadline for 1790940900
2026-10-04T07:39:18Z closed 1790940900 complete=False quotes_complete=False msgs={'twap60': 168, 'twap30': 168, 'chainlink': 168, 'binance': 169}
2026-10-04T07:39:19Z interval 1791099300: 5 checkpoints had already passed and are not read
2026-10-04T07:39:19Z RTDS connected
2026-10-04T07:44:18Z closed 1791099300 complete=False quotes_complete=False msgs={'twap60': 70, 'twap30': 70, 'chainlink': 69, 'binance': 72}
2026-10-04T07:49:33Z closed 1791099600 complete=False quotes_complete=True msgs={'twap60': 365, 'twap30': 366, 'chainlink': 365, 'binance': 372}
2026-10-04T07:54:33Z closed 1791099900 complete=True quotes_complete=True msgs={'twap60': 415, 'twap30': 415, 'chainlink': 415, 'binance': 420}
2026-10-04T08:02:03Z closed 1791100200 complete=True quotes_complete=True msgs={'twap60': 408, 'twap30': 408, 'chainlink': 408, 'binance': 420}
2026-10-04T08:04:03Z closed 1791100500 complete=True quotes_complete=True msgs={'twap60': 415, 'twap30': 416, 'chainlink': 416, 'binance': 420}
2026-10-04T08:08:33Z closed 1791100800 complete=True quotes_complete=True msgs={'twap60': 416, 'twap30': 416, 'chainlink': 416, 'binance': 420}
2026-10-04T08:13:33Z closed 1791101100 complete=True quotes_complete=True msgs={'twap60': 416, 'twap30': 416, 'chainlink': 417, 'binance': 420}
2026-10-04T08:19:33Z closed 1791101400 complete=True quotes_complete=True msgs={'twap60': 416, 'twap30': 416, 'chainlink': 416, 'binance': 420}
2026-10-04T08:24:33Z closed 1791101700 complete=True quotes_complete=True msgs={'twap60': 417, 'twap30': 417, 'chainlink': 416, 'binance': 420}
2026-10-04T08:27:07Z recorder sha=4216c04673ced76b5b2ac60ef57c9abedc46f9b9 root=/var/lib/btc-recorder
2026-10-04T08:27:07Z pre-run floors: free=13375229952 (floor 2000000000) captured=567966600 (cap 4000000000)
2026-10-04T08:27:08Z recovering interval 1791102000
2026-10-04T08:27:08Z interval 1791102300: 2 checkpoints had already passed and are not read
2026-10-04T08:27:08Z RTDS connected
--- tail service.log
[2026-10-04T07:39:45Z] start record: {"argv": ["/root/tz18a-svc/tz18a-chainbook-capture.py", "--serve"], "commit": "ca4bbc1dd583cbb62f3c0c985938d229b526ce7e", "event": "start", "file_sha256": "e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae", "pid": 4060777, "wall_ns": 1791099585558186401}
[2026-10-04T07:39:45Z] window 1791099000: document at 1791099625 (2026-10-04T07:40:25Z), close at 1791099905
[2026-10-04T07:40:25Z] window 1791099000: documents_ok=True statuses=[200, 200]
[2026-10-04T07:40:55Z] window 1791099000 tau' 245: statuses=[200, 200, 200, 200] skew_ns=4519769 complete=True (complete)
[2026-10-04T07:41:55Z] window 1791099000 tau' 185: statuses=[200, 200, 200, 200] skew_ns=5529849 complete=True (complete)
[2026-10-04T07:42:55Z] window 1791099000 tau' 125: statuses=[200, 200, 200, 200] skew_ns=22635824 complete=True (complete)
[2026-10-04T07:43:25Z] window 1791099000 tau' 95: statuses=[200, 200, 200, 200] skew_ns=4675808 complete=True (complete)
[2026-10-04T07:43:55Z] window 1791099000 tau' 65: statuses=[200, 200, 200, 200] skew_ns=43592897 complete=True (complete)
[2026-10-04T07:44:25Z] window 1791099000 tau' 35: statuses=[200, 200, 200, 200] skew_ns=6020455 complete=True (complete)
[2026-10-04T07:44:45Z] window 1791099000 tau' 15: statuses=[200, 200, 200, 200] skew_ns=4796280 complete=True (complete)
[2026-10-04T07:45:05Z] window 1791099000 closed: complete 7 of 7, missed 0, lines 28
[2026-10-04T07:45:05Z] window 1791099900: document at 1791100525 (2026-10-04T07:55:25Z), close at 1791100805
[2026-10-04T07:55:25Z] window 1791099900: documents_ok=True statuses=[200, 200]
[2026-10-04T07:55:55Z] window 1791099900 tau' 245: statuses=[200, 200, 200, 200] skew_ns=7164425 complete=True (complete)
[2026-10-04T07:56:55Z] window 1791099900 tau' 185: statuses=[200, 200, 200, 200] skew_ns=8843245 complete=True (complete)
[2026-10-04T07:57:55Z] window 1791099900 tau' 125: statuses=[200, 200, 200, 200] skew_ns=14011932 complete=True (complete)
[2026-10-04T07:58:25Z] window 1791099900 tau' 95: statuses=[200, 200, 200, 200] skew_ns=3954634 complete=True (complete)
[2026-10-04T07:58:55Z] window 1791099900 tau' 65: statuses=[200, 200, 200, 200] skew_ns=5574568 complete=True (complete)
[2026-10-04T07:59:25Z] window 1791099900 tau' 35: statuses=[200, 200, 200, 200] skew_ns=2246064 complete=True (complete)
[2026-10-04T07:59:45Z] window 1791099900 tau' 15: statuses=[200, 200, 200, 200] skew_ns=7184708 complete=True (complete)
[2026-10-04T08:00:05Z] window 1791099900 closed: complete 7 of 7, missed 0, lines 28
[2026-10-04T08:00:05Z] window 1791100800: document at 1791101425 (2026-10-04T08:10:25Z), close at 1791101705
[2026-10-04T08:10:25Z] window 1791100800: documents_ok=True statuses=[200, 200]
[2026-10-04T08:10:55Z] window 1791100800 tau' 245: statuses=[200, 200, 200, 200] skew_ns=5415278 complete=True (complete)
[2026-10-04T08:11:55Z] window 1791100800 tau' 185: statuses=[200, 200, 200, 200] skew_ns=15932497 complete=True (complete)
[2026-10-04T08:12:55Z] window 1791100800 tau' 125: statuses=[200, 200, 200, 200] skew_ns=15347272 complete=True (complete)
[2026-10-04T08:13:25Z] window 1791100800 tau' 95: statuses=[200, 200, 200, 200] skew_ns=12351996 complete=True (complete)
[2026-10-04T08:13:55Z] window 1791100800 tau' 65: statuses=[200, 200, 200, 200] skew_ns=9522687 complete=True (complete)
[2026-10-04T08:14:25Z] window 1791100800 tau' 35: statuses=[200, 200, 200, 200] skew_ns=9863542 complete=True (complete)
[2026-10-04T08:14:45Z] window 1791100800 tau' 15: statuses=[200, 200, 200, 200] skew_ns=11822836 complete=True (complete)
[2026-10-04T08:15:05Z] window 1791100800 closed: complete 7 of 7, missed 0, lines 28
[2026-10-04T08:15:05Z] window 1791101700: document at 1791102325 (2026-10-04T08:25:25Z), close at 1791102605
[2026-10-04T08:16:13Z] stop record written; requests 90, bytes 76103
[2026-10-04T08:16:18Z] stale pid file (pid 4060777, cmdline '') replaced
[2026-10-04T08:16:18Z] start record: {"argv": ["/root/tz18a-svc/tz18a-chainbook-capture.py", "--serve"], "commit": "ca4bbc1dd583cbb62f3c0c985938d229b526ce7e", "event": "start", "file_sha256": "e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae", "pid": 4064090, "wall_ns": 1791101778487584488}
[2026-10-04T08:16:18Z] window 1791101700: document at 1791102325 (2026-10-04T08:25:25Z), close at 1791102605
[2026-10-04T08:25:25Z] window 1791101700: documents_ok=True statuses=[200, 200]
[2026-10-04T08:25:55Z] window 1791101700 tau' 245: statuses=[200, 200, 200, 200] skew_ns=4838464 complete=True (complete)
[2026-10-04T08:26:55Z] window 1791101700 tau' 185: statuses=[200, 200, 200, 200] skew_ns=16422042 complete=True (complete)
[2026-10-04T08:27:55Z] window 1791101700 tau' 125: statuses=[200, 200, 200, 200] skew_ns=2590407 complete=True (complete)
--- instants
{"kill-cb": {"cb_pid": 4060777, "ns": 1791101769207752242, "rec_pid": 4060666}, "kill-rec": {"cb_pid": 4064090, "ns": 1791102419149894359, "rec_pid": 4060666}, "start-cb": {"cb_pid": 0, "ns": 1791099316160377527, "rec_pid": 0}, "start-rec": {"cb_pid": 0, "ns": 1791099315100620892, "rec_pid": 0}}
MemoryCurrent=45346816
MemoryPeak=102223872
MemoryMax=536870912

MemoryCurrent=10178560
MemoryPeak=18735104
MemoryMax=201326592
               total        used        free      shared  buff/cache   available
Mem:      1002127360   730415104    79081472      192512   378605568   271712256
Swap:     3250581504   722706432  2527875072
4343161	/root/tz20-work
608103	/root/btc-recorder-svc
205149681	/root/.claude
```

The journal holds systemd's own lines and nothing else: two starts, one `SIGTERM` "on client request" to each
unit, each "Deactivated successfully", one "Scheduled restart job, restart counter is at 1" each, and the two
restarts. The log tails carry statuses, counts, times and skews, and no price.

### 2.16 `instants.json` — every instant

| mark | `ns` | UTC | `rec_pid` | `cb_pid` |
|---|---|---|---|---|
| `start-rec` | `1791099315100620892` | 2026-10-04 07:35:15.100 | `0` | `0` |
| `start-cb` | `1791099316160377527` | 2026-10-04 07:35:16.160 | `0` | `0` |
| `kill-cb` | `1791101769207752242` | 2026-10-04 08:16:09.207 | `4060666` | `4060777` |
| `kill-rec` | `1791102419149894359` | 2026-10-04 08:26:59.149 | `4060666` | `4064090` |

### 2.17 §9 B-RECLAIM-OWN — last, after §3.6, with this report drafted

Run from the primary checkout, after §3.6 and with this report drafted in `CryptoReports/`. `reclaim` ran first, and its `RECLAIM PASS` preceded every removal. Each command followed alone, then the verification reads with one further `df` for §0.3. The output went to the session's scratchpad, not into the tree being reclaimed (§6 item 2). The 121 `R copied` lines are in Appendix C. The rest, verbatim:

```text
Sun Oct  4 08:33:56 AM UTC 2026
4344069	/root/tz20-work
[2026-10-04T08:33:56Z] reclaim: 1557 report tokens; forensic store holds 1317 files
[2026-10-04T08:33:56Z] RECLAIM PASS: 141 files considered, 75 named by a report, 46 kept by name, 121 copied, 0 already held; forensic store 1317 -> 1438 files
[2026-10-04T08:33:56Z] opens under the capture roots: 0
exit=0
Sun Oct  4 08:34:01 AM UTC 2026
exit=0
Sun Oct  4 08:34:05 AM UTC 2026
exit=0
Sun Oct  4 08:34:09 AM UTC 2026
exit=1
/root/btc-5m-twap       2d61a16 [main]
/root/btc-recorder-svc  4216c04 (detached HEAD)
1438
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 13375545344
  tz-20-capture-under-systemd
0956da12bd26decbef0fd643b6f223102c7788ba	refs/heads/tz-20-capture-under-systemd
active
active
```

| count | value |
|---|---|
| files considered | `141` (`/root/tz20-work` was `4,344,069` bytes) |
| named by a committed report or this draft | `75` |
| kept by name (and not also named) | `46` — `instants.json` and the 45 files of `logs/` |
| copied | `121`, `2,865,201` bytes: `tz20-work--wt--*` 75, `tz20-work--logs--*` 45, `tz20-work--instants.json` 1 |
| already held | `0` |
| forensic store | `1,317` → `1,438`, asserted `after == before + copied`; the `find` count reads `1438` |

`instants.json` is held as `tz20-work--instants.json`, SHA-256
`bc21d105e4870a19a7f77f2bb7f64eb9ac2096fc5cde635d012dff2f4a77854f`. The three branch files are held as
`tz20-work--wt--deploy--systemd--btc-recorder.service` `3cd713fb…`,
`tz20-work--wt--deploy--systemd--btc-chainbook.service` `a7b042fe…` and
`tz20-work--wt--research--tz20-capture-under-systemd.py` `104c93ce…`.

`git worktree remove --force /root/tz20-work/wt` exited `0`, and so did `rm -rf /root/tz20-work`. **Neither was
refused by the classifier.** `test -e /root/tz20-work` exits `1`. After `git worktree prune`, `git worktree list`
names `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else. The branch `tz-20-capture-under-systemd`
stays at `0956da1`, as a local ref and on `origin`. Both units read `active` after the removal. **Kept:**
`/root/btc-recorder-svc` and `/root/tz18a-svc`, the two units' code, and the capture and the forensic store.

Over the whole TZ, V18 counts 4 worktrees removed (`/root/tz16a-work/wt`, `/root/tz16a-work/wt-report`,
`/root/tz19-work/wt-report`, `/root/tz20-work/wt`) of the 6 registered once §3.1 and §3.3 had added two to the
four found at the host gate. That leaves 2. Three trees are gone.

---

## 3. Publication

| item | value |
|---|---|
| branch | `tz-20-capture-under-systemd`, pushed at 07:32:48 UTC; it stays on `origin` and as a local ref |
| implementation commit | `0956da12bd26decbef0fd643b6f223102c7788ba`, parent `2d61a16` |
| pull request | #21, `https://github.com/seahomebatumi-ai/btc-5m-twap/pull/21`, open against `main`, head `0956da1`, **not merged** |
| Release | none; none is required, and no dataset, archive or binary entered git history |
| report | this file, straight to `main`, one commit |

**Contract §4.2's self-check (V15)**, run at 08:28:55 UTC, after the push and the pull request and before this
report's commit:

```text
Sun Oct  4 08:28:55 AM UTC 2026
fetch exit=0
$ git rev-list origin/main | grep -c 0956da12bd26decbef0fd643b6f223102c7788ba
0
$ git diff --name-only origin/main origin/tz-20-capture-under-systemd
deploy/systemd/btc-chainbook.service
deploy/systemd/btc-recorder.service
research/tz20-capture-under-systemd.py
$ git diff --name-status origin/main origin/tz-20-capture-under-systemd
A	deploy/systemd/btc-chainbook.service
A	deploy/systemd/btc-recorder.service
A	research/tz20-capture-under-systemd.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
grep exit=1
2d61a16a0a4314e42369d5af497c07dd97968481
0956da12bd26decbef0fd643b6f223102c7788ba
{"baseRefName":"main","headRefOid":"0956da12bd26decbef0fd643b6f223102c7788ba","number":21,"state":"OPEN","url":"https://github.com/seahomebatumi-ai/btc-5m-twap/pull/21"}
```

The first line prints `0`. The diff names exactly the three paths, all `A`dded. The `grep` prints nothing.

---

## 4. Gate

| gate | quoted from TZ-20 §4 | deciding numbers | reading |
|---|---|---|---|
| **G-UNIT** | "every check of §4.1", at §3.5 step 1 with `0` restarts and at `I final` with `1` each | 2 of 2 at `0` (07:41:22); 2 of 2 at `1` (08:27:50); every property, argv, cwd, control group and sole-instance check held at both | **PASS** |
| **G-START** | "every check of §4.2" | recorder: 1 start (sha `4216c04…`), 1 `startup` gap starting at `1790940978479700775` inside `[1790940810 × 10^9, 1790941110 × 10^9)`, no `halt`; chain book: 1 record, a `start`, 6 of 6 fields equal | **PASS** |
| **G-CB** | "both `window.json` present by `T + 965`, `documents_ok` true at 2 of 2, `missed` `0` at 2 of 2, `checkpoints_complete` summed at least `13` of `14`" | present 2 of 2; `documents_ok` 2 of 2; `missed` 0 at 2 of 2; **`14` of `14`**, margin 1.000 checkpoint | **PASS** |
| **G-REC** | "`manifest.json` present by `T0 + 3,900` at 6 of 6, `quotes_complete` true at 6 of 6, `recorder_git_sha` `4216c04…` at 6 of 6, `complete` true at least 4 of 6" | 6 of 6; 6 of 6; 6 of 6; **`complete` 6 of 6**, margin 2.000 intervals | **PASS** |
| **G-RESTART-C** | "§4.5" | `start`, `stop`, `start`; pids `4060777`, `4060777`, `4064090`; stop `3.803` s after the mark; restart **`5.476` s** after the stop, against 60.000; `NRestarts` `1` | **PASS** |
| **G-RESTART-R** | "§4.5" | 2 starts, the second `8.683` s after the mark; 2 `startup` gaps, the second starting `2.289` s after the mark, lasting **`6.934` s** against 60.000; no `halt`; pid `4060666` → `4067771`, `NRestarts` `1` | **PASS** |

Family-wise false failure of G-CB and G-REC, as fixed: at most `0.024`. Nothing was tuned, and no gate was
re-read. **Under PASS neither K-20R nor K-20C was run.**

---

## 5. Validation

| # | check | count | asserted |
|---|---|---|---|
| **V1** | §0.1's fingerprint | 6 anchors, 4 re-derived, **25 of 25** `frozen` equal, 2 `tracked`, 1 `reported`; 28 rows | asserted by the fingerprint script (exit 0) |
| **V2** | §0.2's host gate | H1 to H8 and the resource gate, each read named in §0.2 | recorded, not asserted: compared by the Executor in §0.2's table |
| **V3** | `I state` | **S1 to S7**, `STATE PASS` | asserted, exit 0 |
| **V4** | §3.1's three files | **3 of 3** hashes asserted by §3.1's script; lines and bytes equal by `wc`; the branch diff names exactly 3 paths, all `A` | hashes asserted; lines, bytes and the diff recorded, not asserted |
| **V5** | §3.3's recorder tree | `HEAD` equal; **3 of 3** frozen hashes equal | recorded, not asserted: compared by the Executor |
| **V6** | §3.3's request paths | P0 to P4 and P5 to P7; 4 HTTP through `http_get` (asserted), 2 through the recorder's functions, SNTP **2 of 2**, RTDS **4 of 4** topics | asserted, both modes exit 0 |
| **V7** | B-INSTALL | **2 of 2** `cmp` equal; `daemon-reload` exit 0; `systemd-analyze verify` exit 0, no output | recorded, not asserted: exit statuses read |
| **V8** | G-UNIT | **2 of 2** at `0` restarts; **2 of 2** at `1` in `I final`, and each again inside its restart mode | asserted |
| **V9** | G-START | recorder 1 start and 1 gap; chain book 1 start record, 6 of 6 fields equal | asserted, exit 0 |
| **V10** | G-CB | 2 windows: `documents_ok` 2, `missed` 0 at 2, `checkpoints_complete` 14 of 14 | asserted, exit 0 |
| **V11** | G-REC | 6 intervals: manifests 6, `quotes_complete` 6, sha 6, `complete` 6 | asserted, exit 0 |
| **V12** | G-RESTART-C and G-RESTART-R | `start`/`stop`/`start`, pids `4060777`→`4064090`, gap `5.476` s; 2 starts and 2 gaps, pids `4060666`→`4067771`, gap `6.934` s | asserted, both exit 0 |
| **V13** | opens under the capture roots | the printed counts: `state` 2, `path-recorder` 0, `path-chainbook` 0, each `mark` 0 (4 runs), `unit 0` 0, `start` 2, `cb` (PASS run) 3, `rec` (PASS run) 7, `restart-cb` 1, `restart-rec` 1, `final` 2, `reclaim` (old) 0, `reclaim` (own) 0. **No refusal in any run** | the audit hook raises on a refusal; no run raised. The 9 NOT YET runs print no count (§6 item 5) |
| **V14** | `I final` | both units, `NRestarts` `1`, sole instances `4067771` and `4064090`, newest recorder start `4216c04…` | asserted, exit 0 |
| **V15** | contract §4.2's self-check | `0`; 3 paths; nothing | recorded, not asserted; run after the push and the PR, before this report's commit (§3) |
| **V16** | §3.6's closing reads | every read printed (§2.15) | recorded, not asserted |
| **V17** | §9's two `reclaim` runs | old: considered `2,394`, named `244`, kept by name `1`, copied `245`, held `0`, store `1,072` → `1,317`; own: considered `141`, named `75`, kept by name `46`, copied `121`, held `0`, store `1,317` → `1,438` | `after == before + copied` asserted in each |
| **V18** | §9's removals | 4 of 4 `git worktree remove --force` exit 0; `test -e` exit 1 for `/root/tz16a-work`, `/root/tz19-work` and `/root/tz20-work`; `git worktree list` names `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else | recorded, not asserted: exit statuses read |

---

## 6. What could not be implemented as written

1. **B-START-REC was refused by the session's permission classifier** as "[Unauthorized Persistence]". It was
   tried together with its mark, as one command, and neither ran. Per §3, the Executor took the `start-rec` and
   `start-cb` marks (07:35:15 and 07:35:16) and handed B-START-REC and B-START-CB over together. The Boss ran
   them at 07:39:16 and 07:39:45. So **the `start-cb` mark precedes B-START-REC's effect too**, and both marks
   precede their blocks by about four minutes, not seconds. No gate depends on that interval: G-START reads
   records at or after each mark and found exactly one `start` in each file.
2. **§0's outputs were written first outside the host paths §2 lists.** §0.2's H6 requires `/root/tz20-work` to
   be absent at the gate, and §3 sends every output to `/root/tz20-work/logs/`. So the fingerprint, the host gate,
   the refs and §3.1's three git commands were written to this session's scratchpad (a directory under `/tmp`),
   then copied into `logs/` after §3.1's `mkdir`, byte for byte (`cp -n`). For the same reason the reverse way,
   **B-RECLAIM-OWN's own output was written to the scratchpad and not into the tree it reclaims**. A log growing
   inside `/root/tz20-work/logs/` while `reclaim` hashes and copies it would fail its own "copy whole" assert. It
   is quoted in §2.17 and is not in the forensic store. The fingerprint script printed no instant; it ran before
   the host gate at 07:31:26.
3. **B-KILL-REC ran at the second qualifying stretch after G-REC's PASS, not the first.** §3.5 step 5 says "at the
   first instant at which `now % 300` lies between `122` and `128`". After the PASS at 08:22:00, that first instant
   was 08:22:02, and it passed while the output was being read. The block ran at 08:27:02.039, `now % 300` = 122.
   A timed script sequenced it: the mark at `T0 + 119`, the block verbatim at `T0 + 122`, a guard that would have
   sent nothing outside `[122, 128]`, and `I restart-rec` 35 s later. B-KILL-CB ran at 08:16:12, 19 s into the
   stretch that was already open when G-CB passed at 08:15:53, after its mark at 08:16:09.
4. **`reclaim` own read this report's draft as well as the committed reports.** §8 requires the report to be drafted in the
   primary checkout before B-RECLAIM-OWN, and `report_tokens` reads every `.md` in `CryptoReports/`, committed or
   not. So the hex runs of this draft counted as a committed report's. The report was committed after it,
   changed only by filling §2.17, §0.3's last row, V13, V17, V18 and Appendix C from B-RECLAIM-OWN's
   output, and by four prose corrections, none of which adds a hex run.
5. **The NOT YET runs print no count of opens under the capture roots.** `not_yet` exits `3` inside the mode, before
   `main`'s last line prints the count. Nine runs did so: `cb` 4 times and `rec` 5 times. V13 lists the printed
   counts of every other run. The audit hook raises on any refused open, and none of the nine raised.
6. **`/root/tz19-work` measured `4,179,670` bytes**, `68,080` more than TZ-19's closing read of `4,111,590`. The
   cause was not read. Every file in it was considered by `reclaim`.
7. **The memory figures need §2.14's two qualifications.** `MemoryPeak` resets with each restart. The first
   recorder process's peak is the journal's `215.9M`. The first chain book process printed no such line, and its
   highest read is `21,262,336` at 07:41:22. And the ceilings are large beside the host: the
   recorder's alone is 53.6% of `MemTotal`, and the first recorder process used swap, which `MemoryMax` does not
   bound. These are measurements. The TZ fixes the ceilings, and they are not re-derived here.
8. §0.2 says "before anything else". Contract §1's fingerprint (§0.1) ran first, as the contract orders. It read
   files only.

---

## Appendix B — B-RECLAIM-OLD, every file copied

`reclaim /root/tz16a-work /root/tz19-work`, the 245 `R copied` lines, verbatim, in the order printed: the SHA-256
of the source, then the destination in `/root/btc-forensics/`.

<details><summary>245 lines</summary>

```text
[2026-10-04T07:33:18Z] R copied 0bfa34fcae0a03bebd80ce95b8d09ca32cf37098ef6549f36d3322e30c14c4ac /root/btc-forensics/tz16a-work--label-ledger.jsonl
[2026-10-04T07:33:18Z] R copied d79c9f44957d923e828b9157952f1f7b2a01cf9e35deead91ebc44faa16493be /root/btc-forensics/tz16a-work--run-d1--tz16a-constants.json
[2026-10-04T07:33:18Z] R copied 81e276922890a3fcd4c91f3e6e5bc30412f6747db1c6e2ccf4b368da46dc915a /root/btc-forensics/tz16a-work--run-d1--tz16a-disclosure.md
[2026-10-04T07:33:18Z] R copied d79c9f44957d923e828b9157952f1f7b2a01cf9e35deead91ebc44faa16493be /root/btc-forensics/tz16a-work--run-d2--tz16a-constants.json
[2026-10-04T07:33:18Z] R copied 81e276922890a3fcd4c91f3e6e5bc30412f6747db1c6e2ccf4b368da46dc915a /root/btc-forensics/tz16a-work--run-d2--tz16a-disclosure.md
[2026-10-04T07:33:18Z] R copied d79c9f44957d923e828b9157952f1f7b2a01cf9e35deead91ebc44faa16493be /root/btc-forensics/tz16a-work--run-s1--tz16a-constants.json
[2026-10-04T07:33:18Z] R copied 81e276922890a3fcd4c91f3e6e5bc30412f6747db1c6e2ccf4b368da46dc915a /root/btc-forensics/tz16a-work--run-s1--tz16a-disclosure.md
[2026-10-04T07:33:18Z] R copied d22c90df32a6241c405fba00e5542b463d3623e31f87539ab37a1261b149f77f /root/btc-forensics/tz16a-work--run-s1--tz16a-observations.csv
[2026-10-04T07:33:18Z] R copied b2b554920754dd95b1c0a771cef7c49d7bda917d54eb62c3d7498845f1faaa5c /root/btc-forensics/tz16a-work--run-s1--tz16a-readings.json
[2026-10-04T07:33:18Z] R copied 8b41cd251a25edc98293d523428bb9439dd67b7686b35c473e754bfde8ae5f04 /root/btc-forensics/tz16a-work--run-s1--tz16a-run.json
[2026-10-04T07:33:18Z] R copied 47294fbe42ffe67862a1b8beecffceca0a117c27a06a96029c9ee15ae47f2e24 /root/btc-forensics/tz16a-work--run-s1--tz16a-tables.md
[2026-10-04T07:33:18Z] R copied d79c9f44957d923e828b9157952f1f7b2a01cf9e35deead91ebc44faa16493be /root/btc-forensics/tz16a-work--run-s2--tz16a-constants.json
[2026-10-04T07:33:18Z] R copied 81e276922890a3fcd4c91f3e6e5bc30412f6747db1c6e2ccf4b368da46dc915a /root/btc-forensics/tz16a-work--run-s2--tz16a-disclosure.md
[2026-10-04T07:33:18Z] R copied d22c90df32a6241c405fba00e5542b463d3623e31f87539ab37a1261b149f77f /root/btc-forensics/tz16a-work--run-s2--tz16a-observations.csv
[2026-10-04T07:33:18Z] R copied b2b554920754dd95b1c0a771cef7c49d7bda917d54eb62c3d7498845f1faaa5c /root/btc-forensics/tz16a-work--run-s2--tz16a-readings.json
[2026-10-04T07:33:18Z] R copied 5de9b93781af36b8fd790ed9b7cb6814745a78efed0f16f848fa1ea25e0932ee /root/btc-forensics/tz16a-work--run-s2--tz16a-run.json
[2026-10-04T07:33:18Z] R copied 47294fbe42ffe67862a1b8beecffceca0a117c27a06a96029c9ee15ae47f2e24 /root/btc-forensics/tz16a-work--run-s2--tz16a-tables.md
[2026-10-04T07:33:18Z] R copied 8680f8c0eb69788a3f13a78de76ab8794fd8d70835e8c722beb93ee7fc11f6f4 /root/btc-forensics/tz16a-work--wt--.git
[2026-10-04T07:33:18Z] R copied 9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b /root/btc-forensics/tz16a-work--wt--.gitignore
[2026-10-04T07:33:18Z] R copied 437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b /root/btc-forensics/tz16a-work--wt--BTC-EXECUTOR-INSTRUCTIONS.md
[2026-10-04T07:33:18Z] R copied bd8d04323544a2756e26797cf0d5f0b2d6deed3dd303e351c5f09c5daee6723f /root/btc-forensics/tz16a-work--wt--SYSTEM-MAP.md
[2026-10-04T07:33:18Z] R copied 6077fb6a0fb62d5803e70ee5d6f0b8bc8332d756da0af637606eca99bf44f65b /root/btc-forensics/tz16a-work--wt--CryptoReports--TZ-01-twap-divergence-report.md
[2026-10-04T07:33:18Z] R copied bc655c569ec10dffcf817f9dc6373575749b3f147441af640c7738ec5feb47bc /root/btc-forensics/tz16a-work--wt--CryptoReports--TZ-01a-twap-divergence-corrected-report.md
[2026-10-04T07:33:18Z] R copied c7db53c035d389f05a784ba4c9b398a417c9aa7614112ac0d1afa842ccdedef2 /root/btc-forensics/tz16a-work--wt--CryptoReports--TZ-02-divergence-distribution-report.md
[2026-10-04T07:33:18Z] R copied e14cdd5067ed53bfbb4bef6de150331fbcb1ef259793953f165d25ee11a4d397 /root/btc-forensics/tz16a-work--wt--CryptoReports--TZ-03-repo-hygiene-report.md
[2026-10-04T07:33:18Z] R copied 237116cc437dd9216927cf175a0c66921cff2296385bb4b4914cd8d3be74cf51 /root/btc-forensics/tz16a-work--wt--CryptoReports--TZ-04-market-recorder-report.md
[2026-10-04T07:33:18Z] R copied 975843f66a9c0d563c165e681b69482fbefbf8aca880bdd9f87216997e63292c /root/btc-forensics/tz16a-work--wt--CryptoReports--TZ-04a-market-recorder-corrected-report.md
[2026-10-04T07:33:18Z] R copied a18ffd566085cea8f10feba139fadda0f1592f38adddde7e008792c46e8a8e9c /root/btc-forensics/tz16a-work--wt--CryptoReports--TZ-04b-market-recorder-scoring-report.md
[2026-10-04T07:33:18Z] R copied ec548d0e1a4b9bf09695d079b7513428b022460a2b411f9c8ee54f4698778daf /root/btc-forensics/tz16a-work--wt--CryptoReports--TZ-05-quote-capture-report.md
[2026-10-04T07:33:18Z] R copied cddca348120ae278f3c399ea21353f57e8b3722f3b0372e247cc985ab1351805 /root/btc-forensics/tz16a-work--wt--CryptoReports--TZ-05a-quote-capture-deploy-report.md
[2026-10-04T07:33:18Z] R copied 33863ce6d62443dd070646854b135438ee624c96b5204cd9851cfbca9939396f /root/btc-forensics/tz16a-work--wt--CryptoReports--TZ-06-pfair-calibration-report.md
[2026-10-04T07:33:18Z] R copied 4056137f8de8ef6fa39e43a348a1f60bdfee10f7ffe2c29ebb6e4f6e7894c5b4 /root/btc-forensics/tz16a-work--wt--CryptoReports--TZ-07-variance-time-report.md
[2026-10-04T07:33:18Z] R copied 15c26ec8b7ac670bb136177fd3a87dcd56935077714feff48f833dd08b3af72b /root/btc-forensics/tz16a-work--wt--CryptoReports--TZ-07a-variance-time-report.md
[2026-10-04T07:33:18Z] R copied 44b2ee1a80c80867aa17bf6b0c378fccbf203655dfc39a7f323861aab4d7cf80 /root/btc-forensics/tz16a-work--wt--CryptoReports--TZ-07b-settlement-dispersion-report.md
[2026-10-04T07:33:18Z] R copied b0d0c8ed31c28bfa52dc449da4a06d33318f17221a6f9d94ce9bcc8f7ecccffe /root/btc-forensics/tz16a-work--wt--CryptoReports--TZ-08-out-of-sample-report.md
[2026-10-04T07:33:18Z] R copied 86d4ba81e196ace179c65067a3620bb77dba20019f428ecd1c6e588bde6c1188 /root/btc-forensics/tz16a-work--wt--CryptoReports--TZ-08a-out-of-sample-report.md
[2026-10-04T07:33:18Z] R copied 0553061fb9f4793e0e73167042af0a770c5d640fae56f2fb1c7611b494c45815 /root/btc-forensics/tz16a-work--wt--CryptoReports--TZ-17-settlement-chain-report.md
[2026-10-04T07:33:18Z] R copied 455f58e0616daeacfb67ee7302d84520826780720b5c56c7e7a06463ec63dd57 /root/btc-forensics/tz16a-work--wt--CryptoTZ--TZ-01-twap-divergence.md
[2026-10-04T07:33:18Z] R copied a8c4c7c22881236903797e2ffc2d8c87d6e9fc74cd282c7e40feb9eaecab65e3 /root/btc-forensics/tz16a-work--wt--CryptoTZ--TZ-01a-twap-divergence-corrected.md
[2026-10-04T07:33:18Z] R copied c8abadec3bb4763a383f397f8ef188cda4228ed1d356f635f8674456d586f2a3 /root/btc-forensics/tz16a-work--wt--CryptoTZ--TZ-02-divergence-distribution.md
[2026-10-04T07:33:18Z] R copied 0cd150f54862e6c640510acba90c36f1c351e97d0e9b068a573822455668d56e /root/btc-forensics/tz16a-work--wt--CryptoTZ--TZ-03-repo-hygiene.md
[2026-10-04T07:33:18Z] R copied 95b2fd8d752a759f7b274aa0fc8ca62b54d9d27d84bc91cc33cc1014c518fe09 /root/btc-forensics/tz16a-work--wt--CryptoTZ--TZ-04-market-recorder.md
[2026-10-04T07:33:18Z] R copied fff99e417a5117ab9e5186e793adea8bec9be9140864776a84ef0f7c1f20988b /root/btc-forensics/tz16a-work--wt--CryptoTZ--TZ-04a-market-recorder-corrected.md
[2026-10-04T07:33:18Z] R copied f4ab08b6a58f84401d38124ff54a665aaa0808a0fb3b376a1362fcb63960effc /root/btc-forensics/tz16a-work--wt--CryptoTZ--TZ-04b-market-recorder-scoring.md
[2026-10-04T07:33:18Z] R copied 4b9a41fb3301712e6629fb565c47e50a38cb3c85e605122394797ed9094285fe /root/btc-forensics/tz16a-work--wt--CryptoTZ--TZ-05-quote-capture.md
[2026-10-04T07:33:18Z] R copied 16f4821308e0f931a469acd0c7d1facffc4c3bb6c75bcd266305d1acc241410b /root/btc-forensics/tz16a-work--wt--CryptoTZ--TZ-05a-quote-capture-deploy.md
[2026-10-04T07:33:18Z] R copied ec2135c810be9e736946c004b7a4ced0d5a00a322061c89a1519f2d4a30f8373 /root/btc-forensics/tz16a-work--wt--CryptoTZ--TZ-06-pfair-calibration.md
[2026-10-04T07:33:18Z] R copied 759d8ed001ed6746a6b7badd430fa1b3b362849594429849cf196bd892342e2b /root/btc-forensics/tz16a-work--wt--CryptoTZ--TZ-07-variance-time.md
[2026-10-04T07:33:18Z] R copied 0e4852301c493ed7e4cb98d8d880a2c6b42b55f01811976ca9131fc62e61c4e3 /root/btc-forensics/tz16a-work--wt--CryptoTZ--TZ-07a-variance-time.md
[2026-10-04T07:33:18Z] R copied 476344ccf393c8e3f3eb7a70e97f71af7433a45a02af069978b2e8138c155541 /root/btc-forensics/tz16a-work--wt--CryptoTZ--TZ-07b-settlement-dispersion.md
[2026-10-04T07:33:18Z] R copied bacb45ec2c0a3ed824972fe0b536a99f5ef3bad68e78a5c07fbf0c1a09d77d00 /root/btc-forensics/tz16a-work--wt--CryptoTZ--TZ-08-out-of-sample.md
[2026-10-04T07:33:18Z] R copied 3c6ea77fabe9716b6bde98cdba728b67cb62a14f8172ac59bffd47dd04f5e687 /root/btc-forensics/tz16a-work--wt--CryptoTZ--TZ-08a-out-of-sample.md
[2026-10-04T07:33:18Z] R copied db811fea3dea51b58c4a7894cb9666e60b6fcb5b2e86073ba7c89cc9c6fe09e1 /root/btc-forensics/tz16a-work--wt--CryptoTZ--TZ-09-disk-inventory.md
[2026-10-04T07:33:18Z] R copied c08bea39dd3582d4ce8373ee5dabbe1d06357722fedad5c9f97e92f65ab4054a /root/btc-forensics/tz16a-work--wt--CryptoTZ--TZ-10-sigma-or-link.md
[2026-10-04T07:33:18Z] R copied 2688836d8e4dd981d7e9bef324d81844b4be6884e2d1d5b4c103f65db6b5e403 /root/btc-forensics/tz16a-work--wt--CryptoTZ--TZ-10a-sigma-or-link.md
[2026-10-04T07:33:18Z] R copied 8705ca3783784511f8a4f33b23a1664566fb2bda7159d860295a522aadafe49b /root/btc-forensics/tz16a-work--wt--CryptoTZ--TZ-10b-sigma-or-link.md
[2026-10-04T07:33:18Z] R copied 15220788b164ee4d53d32892061bbc2ebd1509acf30282dd453af2c6df86775f /root/btc-forensics/tz16a-work--wt--CryptoTZ--TZ-11-student-link-and-domain.md
[2026-10-04T07:33:18Z] R copied dcd05f165d9057326a930814649cf81c9033980f6fb354cde8dd1fd15628c076 /root/btc-forensics/tz16a-work--wt--CryptoTZ--TZ-11a-student-link-and-domain.md
[2026-10-04T07:33:18Z] R copied cb845f93f61cc8558bcf611c38e5b6a1b859219574bb20e0e806e802263e5d6a /root/btc-forensics/tz16a-work--wt--CryptoTZ--TZ-12-sized-gate.md
[2026-10-04T07:33:18Z] R copied 0e0752cdfacaa517102077052372a32de9557eb6baa37f5354a499b83c7196dd /root/btc-forensics/tz16a-work--wt--CryptoTZ--TZ-16-phase2-decisive-gate.md
[2026-10-04T07:33:18Z] R copied 4e9ec4895337f21693a05bf7f6d6c163e77d6649273c225074c732ceefc2b771 /root/btc-forensics/tz16a-work--wt--CryptoTZ--TZ-16a-phase2-decisive-gate.md
[2026-10-04T07:33:18Z] R copied b989a1d32ee66cf7c95495773484037e9399542829b311045f6e938637001ba1 /root/btc-forensics/tz16a-work--wt--CryptoTZ--TZ-18a-chainbook-capture-redeploy.md
[2026-10-04T07:33:18Z] R copied 729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68 /root/btc-forensics/tz16a-work--wt--research--pfair.py
[2026-10-04T07:33:18Z] R copied b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa /root/btc-forensics/tz16a-work--wt--research--selftest-pfair.py
[2026-10-04T07:33:18Z] R copied ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a /root/btc-forensics/tz16a-work--wt--research--selftest-twap-divergence.py
[2026-10-04T07:33:18Z] R copied 6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473 /root/btc-forensics/tz16a-work--wt--research--twap-divergence.py
[2026-10-04T07:33:18Z] R copied f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4 /root/btc-forensics/tz16a-work--wt--research--tz02-distribution.py
[2026-10-04T07:33:18Z] R copied 715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f /root/btc-forensics/tz16a-work--wt--research--tz06-calibration.py
[2026-10-04T07:33:18Z] R copied 513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771 /root/btc-forensics/tz16a-work--wt--research--tz07a-variance-time.py
[2026-10-04T07:33:18Z] R copied 424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc /root/btc-forensics/tz16a-work--wt--research--tz07b-settlement-dispersion.py
[2026-10-04T07:33:18Z] R copied 37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c /root/btc-forensics/tz16a-work--wt--research--tz08a-out-of-sample.py
[2026-10-04T07:33:18Z] R copied b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6 /root/btc-forensics/tz16a-work--wt--research--tz09-disk-inventory.py
[2026-10-04T07:33:18Z] R copied 406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088 /root/btc-forensics/tz16a-work--wt--research--tz10b-sigma-or-link.py
[2026-10-04T07:33:18Z] R copied 0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839 /root/btc-forensics/tz16a-work--wt--research--tz11a-student-link.py
[2026-10-04T07:33:18Z] R copied d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999 /root/btc-forensics/tz16a-work--wt--research--tz12-sized-gate.py
[2026-10-04T07:33:18Z] R copied a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd /root/btc-forensics/tz16a-work--wt--research--tz13-sized-gate-test3.py
[2026-10-04T07:33:18Z] R copied 978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02 /root/btc-forensics/tz16a-work--wt--research--tz14-quote-inventory.py
[2026-10-04T07:33:18Z] R copied 66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3 /root/btc-forensics/tz16a-work--wt--research--tz15-phase2-gate.py
[2026-10-04T07:33:18Z] R copied 3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125 /root/btc-forensics/tz16a-work--wt--research--tz16a-phase2-decisive-gate.py
[2026-10-04T07:33:18Z] R copied e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92 /root/btc-forensics/tz16a-work--wt--research--tz17-settlement-chain.py
[2026-10-04T07:33:18Z] R copied e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae /root/btc-forensics/tz16a-work--wt--research--tz18a-chainbook-capture.py
[2026-10-04T07:33:18Z] R copied eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d /root/btc-forensics/tz16a-work--wt--research--recorder--analyze.py
[2026-10-04T07:33:18Z] R copied 8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d /root/btc-forensics/tz16a-work--wt--research--recorder--config.py
[2026-10-04T07:33:18Z] R copied 79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045 /root/btc-forensics/tz16a-work--wt--research--recorder--manifest.py
[2026-10-04T07:33:18Z] R copied 50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2 /root/btc-forensics/tz16a-work--wt--research--recorder--probe.py
[2026-10-04T07:33:18Z] R copied 9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03 /root/btc-forensics/tz16a-work--wt--research--recorder--recorder.py
[2026-10-04T07:33:18Z] R copied c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90 /root/btc-forensics/tz16a-work--wt--research--recorder--selftest.py
[2026-10-04T07:33:18Z] R copied 9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b /root/btc-forensics/tz16a-work--wt-report--.gitignore
[2026-10-04T07:33:18Z] R copied 437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b /root/btc-forensics/tz16a-work--wt-report--BTC-EXECUTOR-INSTRUCTIONS.md
[2026-10-04T07:33:18Z] R copied bd8d04323544a2756e26797cf0d5f0b2d6deed3dd303e351c5f09c5daee6723f /root/btc-forensics/tz16a-work--wt-report--SYSTEM-MAP.md
[2026-10-04T07:33:18Z] R copied 6077fb6a0fb62d5803e70ee5d6f0b8bc8332d756da0af637606eca99bf44f65b /root/btc-forensics/tz16a-work--wt-report--CryptoReports--TZ-01-twap-divergence-report.md
[2026-10-04T07:33:18Z] R copied bc655c569ec10dffcf817f9dc6373575749b3f147441af640c7738ec5feb47bc /root/btc-forensics/tz16a-work--wt-report--CryptoReports--TZ-01a-twap-divergence-corrected-report.md
[2026-10-04T07:33:18Z] R copied c7db53c035d389f05a784ba4c9b398a417c9aa7614112ac0d1afa842ccdedef2 /root/btc-forensics/tz16a-work--wt-report--CryptoReports--TZ-02-divergence-distribution-report.md
[2026-10-04T07:33:18Z] R copied e14cdd5067ed53bfbb4bef6de150331fbcb1ef259793953f165d25ee11a4d397 /root/btc-forensics/tz16a-work--wt-report--CryptoReports--TZ-03-repo-hygiene-report.md
[2026-10-04T07:33:18Z] R copied 237116cc437dd9216927cf175a0c66921cff2296385bb4b4914cd8d3be74cf51 /root/btc-forensics/tz16a-work--wt-report--CryptoReports--TZ-04-market-recorder-report.md
[2026-10-04T07:33:18Z] R copied 975843f66a9c0d563c165e681b69482fbefbf8aca880bdd9f87216997e63292c /root/btc-forensics/tz16a-work--wt-report--CryptoReports--TZ-04a-market-recorder-corrected-report.md
[2026-10-04T07:33:18Z] R copied a18ffd566085cea8f10feba139fadda0f1592f38adddde7e008792c46e8a8e9c /root/btc-forensics/tz16a-work--wt-report--CryptoReports--TZ-04b-market-recorder-scoring-report.md
[2026-10-04T07:33:18Z] R copied ec548d0e1a4b9bf09695d079b7513428b022460a2b411f9c8ee54f4698778daf /root/btc-forensics/tz16a-work--wt-report--CryptoReports--TZ-05-quote-capture-report.md
[2026-10-04T07:33:18Z] R copied cddca348120ae278f3c399ea21353f57e8b3722f3b0372e247cc985ab1351805 /root/btc-forensics/tz16a-work--wt-report--CryptoReports--TZ-05a-quote-capture-deploy-report.md
[2026-10-04T07:33:18Z] R copied 33863ce6d62443dd070646854b135438ee624c96b5204cd9851cfbca9939396f /root/btc-forensics/tz16a-work--wt-report--CryptoReports--TZ-06-pfair-calibration-report.md
[2026-10-04T07:33:18Z] R copied 4056137f8de8ef6fa39e43a348a1f60bdfee10f7ffe2c29ebb6e4f6e7894c5b4 /root/btc-forensics/tz16a-work--wt-report--CryptoReports--TZ-07-variance-time-report.md
[2026-10-04T07:33:18Z] R copied 15c26ec8b7ac670bb136177fd3a87dcd56935077714feff48f833dd08b3af72b /root/btc-forensics/tz16a-work--wt-report--CryptoReports--TZ-07a-variance-time-report.md
[2026-10-04T07:33:18Z] R copied 44b2ee1a80c80867aa17bf6b0c378fccbf203655dfc39a7f323861aab4d7cf80 /root/btc-forensics/tz16a-work--wt-report--CryptoReports--TZ-07b-settlement-dispersion-report.md
[2026-10-04T07:33:18Z] R copied b0d0c8ed31c28bfa52dc449da4a06d33318f17221a6f9d94ce9bcc8f7ecccffe /root/btc-forensics/tz16a-work--wt-report--CryptoReports--TZ-08-out-of-sample-report.md
[2026-10-04T07:33:18Z] R copied 86d4ba81e196ace179c65067a3620bb77dba20019f428ecd1c6e588bde6c1188 /root/btc-forensics/tz16a-work--wt-report--CryptoReports--TZ-08a-out-of-sample-report.md
[2026-10-04T07:33:18Z] R copied 0553061fb9f4793e0e73167042af0a770c5d640fae56f2fb1c7611b494c45815 /root/btc-forensics/tz16a-work--wt-report--CryptoReports--TZ-17-settlement-chain-report.md
[2026-10-04T07:33:18Z] R copied 455f58e0616daeacfb67ee7302d84520826780720b5c56c7e7a06463ec63dd57 /root/btc-forensics/tz16a-work--wt-report--CryptoTZ--TZ-01-twap-divergence.md
[2026-10-04T07:33:18Z] R copied a8c4c7c22881236903797e2ffc2d8c87d6e9fc74cd282c7e40feb9eaecab65e3 /root/btc-forensics/tz16a-work--wt-report--CryptoTZ--TZ-01a-twap-divergence-corrected.md
[2026-10-04T07:33:18Z] R copied c8abadec3bb4763a383f397f8ef188cda4228ed1d356f635f8674456d586f2a3 /root/btc-forensics/tz16a-work--wt-report--CryptoTZ--TZ-02-divergence-distribution.md
[2026-10-04T07:33:18Z] R copied 0cd150f54862e6c640510acba90c36f1c351e97d0e9b068a573822455668d56e /root/btc-forensics/tz16a-work--wt-report--CryptoTZ--TZ-03-repo-hygiene.md
[2026-10-04T07:33:18Z] R copied 95b2fd8d752a759f7b274aa0fc8ca62b54d9d27d84bc91cc33cc1014c518fe09 /root/btc-forensics/tz16a-work--wt-report--CryptoTZ--TZ-04-market-recorder.md
[2026-10-04T07:33:18Z] R copied fff99e417a5117ab9e5186e793adea8bec9be9140864776a84ef0f7c1f20988b /root/btc-forensics/tz16a-work--wt-report--CryptoTZ--TZ-04a-market-recorder-corrected.md
[2026-10-04T07:33:18Z] R copied f4ab08b6a58f84401d38124ff54a665aaa0808a0fb3b376a1362fcb63960effc /root/btc-forensics/tz16a-work--wt-report--CryptoTZ--TZ-04b-market-recorder-scoring.md
[2026-10-04T07:33:18Z] R copied 4b9a41fb3301712e6629fb565c47e50a38cb3c85e605122394797ed9094285fe /root/btc-forensics/tz16a-work--wt-report--CryptoTZ--TZ-05-quote-capture.md
[2026-10-04T07:33:18Z] R copied 16f4821308e0f931a469acd0c7d1facffc4c3bb6c75bcd266305d1acc241410b /root/btc-forensics/tz16a-work--wt-report--CryptoTZ--TZ-05a-quote-capture-deploy.md
[2026-10-04T07:33:18Z] R copied ec2135c810be9e736946c004b7a4ced0d5a00a322061c89a1519f2d4a30f8373 /root/btc-forensics/tz16a-work--wt-report--CryptoTZ--TZ-06-pfair-calibration.md
[2026-10-04T07:33:18Z] R copied 759d8ed001ed6746a6b7badd430fa1b3b362849594429849cf196bd892342e2b /root/btc-forensics/tz16a-work--wt-report--CryptoTZ--TZ-07-variance-time.md
[2026-10-04T07:33:18Z] R copied 0e4852301c493ed7e4cb98d8d880a2c6b42b55f01811976ca9131fc62e61c4e3 /root/btc-forensics/tz16a-work--wt-report--CryptoTZ--TZ-07a-variance-time.md
[2026-10-04T07:33:18Z] R copied 476344ccf393c8e3f3eb7a70e97f71af7433a45a02af069978b2e8138c155541 /root/btc-forensics/tz16a-work--wt-report--CryptoTZ--TZ-07b-settlement-dispersion.md
[2026-10-04T07:33:18Z] R copied bacb45ec2c0a3ed824972fe0b536a99f5ef3bad68e78a5c07fbf0c1a09d77d00 /root/btc-forensics/tz16a-work--wt-report--CryptoTZ--TZ-08-out-of-sample.md
[2026-10-04T07:33:18Z] R copied 3c6ea77fabe9716b6bde98cdba728b67cb62a14f8172ac59bffd47dd04f5e687 /root/btc-forensics/tz16a-work--wt-report--CryptoTZ--TZ-08a-out-of-sample.md
[2026-10-04T07:33:18Z] R copied db811fea3dea51b58c4a7894cb9666e60b6fcb5b2e86073ba7c89cc9c6fe09e1 /root/btc-forensics/tz16a-work--wt-report--CryptoTZ--TZ-09-disk-inventory.md
[2026-10-04T07:33:18Z] R copied c08bea39dd3582d4ce8373ee5dabbe1d06357722fedad5c9f97e92f65ab4054a /root/btc-forensics/tz16a-work--wt-report--CryptoTZ--TZ-10-sigma-or-link.md
[2026-10-04T07:33:18Z] R copied 2688836d8e4dd981d7e9bef324d81844b4be6884e2d1d5b4c103f65db6b5e403 /root/btc-forensics/tz16a-work--wt-report--CryptoTZ--TZ-10a-sigma-or-link.md
[2026-10-04T07:33:18Z] R copied 8705ca3783784511f8a4f33b23a1664566fb2bda7159d860295a522aadafe49b /root/btc-forensics/tz16a-work--wt-report--CryptoTZ--TZ-10b-sigma-or-link.md
[2026-10-04T07:33:18Z] R copied 15220788b164ee4d53d32892061bbc2ebd1509acf30282dd453af2c6df86775f /root/btc-forensics/tz16a-work--wt-report--CryptoTZ--TZ-11-student-link-and-domain.md
[2026-10-04T07:33:18Z] R copied dcd05f165d9057326a930814649cf81c9033980f6fb354cde8dd1fd15628c076 /root/btc-forensics/tz16a-work--wt-report--CryptoTZ--TZ-11a-student-link-and-domain.md
[2026-10-04T07:33:18Z] R copied cb845f93f61cc8558bcf611c38e5b6a1b859219574bb20e0e806e802263e5d6a /root/btc-forensics/tz16a-work--wt-report--CryptoTZ--TZ-12-sized-gate.md
[2026-10-04T07:33:18Z] R copied 0e0752cdfacaa517102077052372a32de9557eb6baa37f5354a499b83c7196dd /root/btc-forensics/tz16a-work--wt-report--CryptoTZ--TZ-16-phase2-decisive-gate.md
[2026-10-04T07:33:18Z] R copied 4e9ec4895337f21693a05bf7f6d6c163e77d6649273c225074c732ceefc2b771 /root/btc-forensics/tz16a-work--wt-report--CryptoTZ--TZ-16a-phase2-decisive-gate.md
[2026-10-04T07:33:18Z] R copied b989a1d32ee66cf7c95495773484037e9399542829b311045f6e938637001ba1 /root/btc-forensics/tz16a-work--wt-report--CryptoTZ--TZ-18a-chainbook-capture-redeploy.md
[2026-10-04T07:33:18Z] R copied 729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68 /root/btc-forensics/tz16a-work--wt-report--research--pfair.py
[2026-10-04T07:33:18Z] R copied b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa /root/btc-forensics/tz16a-work--wt-report--research--selftest-pfair.py
[2026-10-04T07:33:18Z] R copied ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a /root/btc-forensics/tz16a-work--wt-report--research--selftest-twap-divergence.py
[2026-10-04T07:33:18Z] R copied 6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473 /root/btc-forensics/tz16a-work--wt-report--research--twap-divergence.py
[2026-10-04T07:33:18Z] R copied f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4 /root/btc-forensics/tz16a-work--wt-report--research--tz02-distribution.py
[2026-10-04T07:33:18Z] R copied 715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f /root/btc-forensics/tz16a-work--wt-report--research--tz06-calibration.py
[2026-10-04T07:33:18Z] R copied 513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771 /root/btc-forensics/tz16a-work--wt-report--research--tz07a-variance-time.py
[2026-10-04T07:33:18Z] R copied 424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc /root/btc-forensics/tz16a-work--wt-report--research--tz07b-settlement-dispersion.py
[2026-10-04T07:33:18Z] R copied 37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c /root/btc-forensics/tz16a-work--wt-report--research--tz08a-out-of-sample.py
[2026-10-04T07:33:18Z] R copied b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6 /root/btc-forensics/tz16a-work--wt-report--research--tz09-disk-inventory.py
[2026-10-04T07:33:18Z] R copied 406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088 /root/btc-forensics/tz16a-work--wt-report--research--tz10b-sigma-or-link.py
[2026-10-04T07:33:18Z] R copied 0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839 /root/btc-forensics/tz16a-work--wt-report--research--tz11a-student-link.py
[2026-10-04T07:33:18Z] R copied d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999 /root/btc-forensics/tz16a-work--wt-report--research--tz12-sized-gate.py
[2026-10-04T07:33:18Z] R copied a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd /root/btc-forensics/tz16a-work--wt-report--research--tz13-sized-gate-test3.py
[2026-10-04T07:33:18Z] R copied 978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02 /root/btc-forensics/tz16a-work--wt-report--research--tz14-quote-inventory.py
[2026-10-04T07:33:18Z] R copied 66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3 /root/btc-forensics/tz16a-work--wt-report--research--tz15-phase2-gate.py
[2026-10-04T07:33:18Z] R copied e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92 /root/btc-forensics/tz16a-work--wt-report--research--tz17-settlement-chain.py
[2026-10-04T07:33:18Z] R copied e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae /root/btc-forensics/tz16a-work--wt-report--research--tz18a-chainbook-capture.py
[2026-10-04T07:33:18Z] R copied eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d /root/btc-forensics/tz16a-work--wt-report--research--recorder--analyze.py
[2026-10-04T07:33:18Z] R copied 8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d /root/btc-forensics/tz16a-work--wt-report--research--recorder--config.py
[2026-10-04T07:33:18Z] R copied 79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045 /root/btc-forensics/tz16a-work--wt-report--research--recorder--manifest.py
[2026-10-04T07:33:18Z] R copied 50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2 /root/btc-forensics/tz16a-work--wt-report--research--recorder--probe.py
[2026-10-04T07:33:18Z] R copied 9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03 /root/btc-forensics/tz16a-work--wt-report--research--recorder--recorder.py
[2026-10-04T07:33:18Z] R copied c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90 /root/btc-forensics/tz16a-work--wt-report--research--recorder--selftest.py
[2026-10-04T07:33:18Z] R copied b0957d7b54a242242e18c1455fc9920d01c8c59e85ebbc720bea5000fad20abb /root/btc-forensics/tz19-work--logs--closing-read.txt
[2026-10-04T07:33:18Z] R copied 78e8bbc81644fd32d33f283d31acea6b4a7491ccb335128c3c4252892b154262 /root/btc-forensics/tz19-work--logs--figures.txt
[2026-10-04T07:33:18Z] R copied 2bc52857222528fff26e3477cccd2c6ec1fb76ce0eec1e57f50e811c03eb12ce /root/btc-forensics/tz19-work--logs--fingerprint.txt
[2026-10-04T07:33:18Z] R copied dced313af2c8afdec1f033680885637f8d1f763d744997d34f95adbf0726ec1b /root/btc-forensics/tz19-work--logs--host-gate.txt
[2026-10-04T07:33:18Z] R copied 4b676b6b4ed0db91d50c29c27bd68f146267573ccd8d6766a9802b58282e5cad /root/btc-forensics/tz19-work--logs--probe-recorder-pids.txt
[2026-10-04T07:33:18Z] R copied 5c458749a51e4eee6bb08483c69f6bacc10f1dc92551f5378568422bb784a552 /root/btc-forensics/tz19-work--logs--r-ready.txt
[2026-10-04T07:33:18Z] R copied 6564382ca47e692fc8e2725f4f63d8eb6e03c9b425b385f59855e079096c7926 /root/btc-forensics/tz19-work--logs--refs.txt
[2026-10-04T07:33:18Z] R copied 10a48e91cf7b63c0add006ea2b611f55735ce64675178f13a204082846b852a4 /root/btc-forensics/tz19-work--logs--selfcheck.txt
[2026-10-04T07:33:18Z] R copied 34c0a5dd9313ec22f97b98e317f372e563756def68d48d517138af5cd06e285c /root/btc-forensics/tz19-work--logs--stop-evidence-redacted.txt
[2026-10-04T07:33:18Z] R copied 599695bb915c3812da28dd18b512978e9c94b7f2bbc3dd682beb13bcb755c800 /root/btc-forensics/tz19-work--logs--stop-evidence.txt
[2026-10-04T07:33:18Z] R copied 6f62b8073693ee745177f2d82a8bcc376cf49f522877103dd5ba4886d3197d77 /root/btc-forensics/tz19-work--scratch--check-report.py
[2026-10-04T07:33:18Z] R copied 05a55cb7d6350932c223b94ae7c61dbab2aa9a4019501c8a6a7f3ea609dcdf21 /root/btc-forensics/tz19-work--scratch--closing-read.sh
[2026-10-04T07:33:18Z] R copied e280a0f22fefd6864f8ba82c986a1bffe13ddce5a611796237f19ac14ac8ce19 /root/btc-forensics/tz19-work--scratch--figures.py
[2026-10-04T07:33:18Z] R copied 7489abeed3787f3603831998b55e6f88b6d2f88927b5ec4d700f5263f1d69ceb /root/btc-forensics/tz19-work--scratch--fill.py
[2026-10-04T07:33:18Z] R copied cc4dba48699fb113231e73456a50b9e50ae640d2af22f36daa80e2dc0f19a05d /root/btc-forensics/tz19-work--scratch--fingerprint.py
[2026-10-04T07:33:18Z] R copied f07f92337bf5dd8ab41a1f6b976ece8c0efa5488692ddeebd4cffc576b038e8b /root/btc-forensics/tz19-work--scratch--probe-recorder-pids.py
[2026-10-04T07:33:18Z] R copied 1aa56f67ec72f09e70e98d38c3c8f5f67e18c311a4c20111cc4c083d5c912135 /root/btc-forensics/tz19-work--scratch--redact.py
[2026-10-04T07:33:18Z] R copied df1dbfa8a6364f6bb2b6e1571146685edad4ca53990b2f13f6d03d88189d1884 /root/btc-forensics/tz19-work--scratch--report-template.md
[2026-10-04T07:33:18Z] R copied 4c50eec5180ce88dcd63669fa89de50e8301bab42658659c7cc839f3bc6f6e97 /root/btc-forensics/tz19-work--scratch--stop-evidence.sh
[2026-10-04T07:33:18Z] R copied fdbc86802d9416183be9d1dc746cce8372394b184b9e864edaa9b0bcb42c6d89 /root/btc-forensics/tz19-work--wt-report--.git
[2026-10-04T07:33:18Z] R copied 9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b /root/btc-forensics/tz19-work--wt-report--.gitignore
[2026-10-04T07:33:18Z] R copied 437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b /root/btc-forensics/tz19-work--wt-report--BTC-EXECUTOR-INSTRUCTIONS.md
[2026-10-04T07:33:18Z] R copied b26544de6b7c5a7554c548160c4937805542ec512686458aad7baaa7ca1a0cdd /root/btc-forensics/tz19-work--wt-report--SYSTEM-MAP.md
[2026-10-04T07:33:18Z] R copied 6077fb6a0fb62d5803e70ee5d6f0b8bc8332d756da0af637606eca99bf44f65b /root/btc-forensics/tz19-work--wt-report--CryptoReports--TZ-01-twap-divergence-report.md
[2026-10-04T07:33:18Z] R copied bc655c569ec10dffcf817f9dc6373575749b3f147441af640c7738ec5feb47bc /root/btc-forensics/tz19-work--wt-report--CryptoReports--TZ-01a-twap-divergence-corrected-report.md
[2026-10-04T07:33:18Z] R copied c7db53c035d389f05a784ba4c9b398a417c9aa7614112ac0d1afa842ccdedef2 /root/btc-forensics/tz19-work--wt-report--CryptoReports--TZ-02-divergence-distribution-report.md
[2026-10-04T07:33:18Z] R copied e14cdd5067ed53bfbb4bef6de150331fbcb1ef259793953f165d25ee11a4d397 /root/btc-forensics/tz19-work--wt-report--CryptoReports--TZ-03-repo-hygiene-report.md
[2026-10-04T07:33:18Z] R copied 237116cc437dd9216927cf175a0c66921cff2296385bb4b4914cd8d3be74cf51 /root/btc-forensics/tz19-work--wt-report--CryptoReports--TZ-04-market-recorder-report.md
[2026-10-04T07:33:19Z] R copied 975843f66a9c0d563c165e681b69482fbefbf8aca880bdd9f87216997e63292c /root/btc-forensics/tz19-work--wt-report--CryptoReports--TZ-04a-market-recorder-corrected-report.md
[2026-10-04T07:33:19Z] R copied a18ffd566085cea8f10feba139fadda0f1592f38adddde7e008792c46e8a8e9c /root/btc-forensics/tz19-work--wt-report--CryptoReports--TZ-04b-market-recorder-scoring-report.md
[2026-10-04T07:33:19Z] R copied ec548d0e1a4b9bf09695d079b7513428b022460a2b411f9c8ee54f4698778daf /root/btc-forensics/tz19-work--wt-report--CryptoReports--TZ-05-quote-capture-report.md
[2026-10-04T07:33:19Z] R copied cddca348120ae278f3c399ea21353f57e8b3722f3b0372e247cc985ab1351805 /root/btc-forensics/tz19-work--wt-report--CryptoReports--TZ-05a-quote-capture-deploy-report.md
[2026-10-04T07:33:19Z] R copied 33863ce6d62443dd070646854b135438ee624c96b5204cd9851cfbca9939396f /root/btc-forensics/tz19-work--wt-report--CryptoReports--TZ-06-pfair-calibration-report.md
[2026-10-04T07:33:19Z] R copied 4056137f8de8ef6fa39e43a348a1f60bdfee10f7ffe2c29ebb6e4f6e7894c5b4 /root/btc-forensics/tz19-work--wt-report--CryptoReports--TZ-07-variance-time-report.md
[2026-10-04T07:33:19Z] R copied 15c26ec8b7ac670bb136177fd3a87dcd56935077714feff48f833dd08b3af72b /root/btc-forensics/tz19-work--wt-report--CryptoReports--TZ-07a-variance-time-report.md
[2026-10-04T07:33:19Z] R copied 44b2ee1a80c80867aa17bf6b0c378fccbf203655dfc39a7f323861aab4d7cf80 /root/btc-forensics/tz19-work--wt-report--CryptoReports--TZ-07b-settlement-dispersion-report.md
[2026-10-04T07:33:19Z] R copied b0d0c8ed31c28bfa52dc449da4a06d33318f17221a6f9d94ce9bcc8f7ecccffe /root/btc-forensics/tz19-work--wt-report--CryptoReports--TZ-08-out-of-sample-report.md
[2026-10-04T07:33:19Z] R copied 86d4ba81e196ace179c65067a3620bb77dba20019f428ecd1c6e588bde6c1188 /root/btc-forensics/tz19-work--wt-report--CryptoReports--TZ-08a-out-of-sample-report.md
[2026-10-04T07:33:19Z] R copied 0553061fb9f4793e0e73167042af0a770c5d640fae56f2fb1c7611b494c45815 /root/btc-forensics/tz19-work--wt-report--CryptoReports--TZ-17-settlement-chain-report.md
[2026-10-04T07:33:19Z] R copied 455f58e0616daeacfb67ee7302d84520826780720b5c56c7e7a06463ec63dd57 /root/btc-forensics/tz19-work--wt-report--CryptoTZ--TZ-01-twap-divergence.md
[2026-10-04T07:33:19Z] R copied a8c4c7c22881236903797e2ffc2d8c87d6e9fc74cd282c7e40feb9eaecab65e3 /root/btc-forensics/tz19-work--wt-report--CryptoTZ--TZ-01a-twap-divergence-corrected.md
[2026-10-04T07:33:19Z] R copied c8abadec3bb4763a383f397f8ef188cda4228ed1d356f635f8674456d586f2a3 /root/btc-forensics/tz19-work--wt-report--CryptoTZ--TZ-02-divergence-distribution.md
[2026-10-04T07:33:19Z] R copied 0cd150f54862e6c640510acba90c36f1c351e97d0e9b068a573822455668d56e /root/btc-forensics/tz19-work--wt-report--CryptoTZ--TZ-03-repo-hygiene.md
[2026-10-04T07:33:19Z] R copied 95b2fd8d752a759f7b274aa0fc8ca62b54d9d27d84bc91cc33cc1014c518fe09 /root/btc-forensics/tz19-work--wt-report--CryptoTZ--TZ-04-market-recorder.md
[2026-10-04T07:33:19Z] R copied fff99e417a5117ab9e5186e793adea8bec9be9140864776a84ef0f7c1f20988b /root/btc-forensics/tz19-work--wt-report--CryptoTZ--TZ-04a-market-recorder-corrected.md
[2026-10-04T07:33:19Z] R copied f4ab08b6a58f84401d38124ff54a665aaa0808a0fb3b376a1362fcb63960effc /root/btc-forensics/tz19-work--wt-report--CryptoTZ--TZ-04b-market-recorder-scoring.md
[2026-10-04T07:33:19Z] R copied 4b9a41fb3301712e6629fb565c47e50a38cb3c85e605122394797ed9094285fe /root/btc-forensics/tz19-work--wt-report--CryptoTZ--TZ-05-quote-capture.md
[2026-10-04T07:33:19Z] R copied 16f4821308e0f931a469acd0c7d1facffc4c3bb6c75bcd266305d1acc241410b /root/btc-forensics/tz19-work--wt-report--CryptoTZ--TZ-05a-quote-capture-deploy.md
[2026-10-04T07:33:19Z] R copied ec2135c810be9e736946c004b7a4ced0d5a00a322061c89a1519f2d4a30f8373 /root/btc-forensics/tz19-work--wt-report--CryptoTZ--TZ-06-pfair-calibration.md
[2026-10-04T07:33:19Z] R copied 759d8ed001ed6746a6b7badd430fa1b3b362849594429849cf196bd892342e2b /root/btc-forensics/tz19-work--wt-report--CryptoTZ--TZ-07-variance-time.md
[2026-10-04T07:33:19Z] R copied 0e4852301c493ed7e4cb98d8d880a2c6b42b55f01811976ca9131fc62e61c4e3 /root/btc-forensics/tz19-work--wt-report--CryptoTZ--TZ-07a-variance-time.md
[2026-10-04T07:33:19Z] R copied 476344ccf393c8e3f3eb7a70e97f71af7433a45a02af069978b2e8138c155541 /root/btc-forensics/tz19-work--wt-report--CryptoTZ--TZ-07b-settlement-dispersion.md
[2026-10-04T07:33:19Z] R copied bacb45ec2c0a3ed824972fe0b536a99f5ef3bad68e78a5c07fbf0c1a09d77d00 /root/btc-forensics/tz19-work--wt-report--CryptoTZ--TZ-08-out-of-sample.md
[2026-10-04T07:33:19Z] R copied 3c6ea77fabe9716b6bde98cdba728b67cb62a14f8172ac59bffd47dd04f5e687 /root/btc-forensics/tz19-work--wt-report--CryptoTZ--TZ-08a-out-of-sample.md
[2026-10-04T07:33:19Z] R copied db811fea3dea51b58c4a7894cb9666e60b6fcb5b2e86073ba7c89cc9c6fe09e1 /root/btc-forensics/tz19-work--wt-report--CryptoTZ--TZ-09-disk-inventory.md
[2026-10-04T07:33:19Z] R copied c08bea39dd3582d4ce8373ee5dabbe1d06357722fedad5c9f97e92f65ab4054a /root/btc-forensics/tz19-work--wt-report--CryptoTZ--TZ-10-sigma-or-link.md
[2026-10-04T07:33:19Z] R copied 2688836d8e4dd981d7e9bef324d81844b4be6884e2d1d5b4c103f65db6b5e403 /root/btc-forensics/tz19-work--wt-report--CryptoTZ--TZ-10a-sigma-or-link.md
[2026-10-04T07:33:19Z] R copied 8705ca3783784511f8a4f33b23a1664566fb2bda7159d860295a522aadafe49b /root/btc-forensics/tz19-work--wt-report--CryptoTZ--TZ-10b-sigma-or-link.md
[2026-10-04T07:33:19Z] R copied 15220788b164ee4d53d32892061bbc2ebd1509acf30282dd453af2c6df86775f /root/btc-forensics/tz19-work--wt-report--CryptoTZ--TZ-11-student-link-and-domain.md
[2026-10-04T07:33:19Z] R copied dcd05f165d9057326a930814649cf81c9033980f6fb354cde8dd1fd15628c076 /root/btc-forensics/tz19-work--wt-report--CryptoTZ--TZ-11a-student-link-and-domain.md
[2026-10-04T07:33:19Z] R copied cb845f93f61cc8558bcf611c38e5b6a1b859219574bb20e0e806e802263e5d6a /root/btc-forensics/tz19-work--wt-report--CryptoTZ--TZ-12-sized-gate.md
[2026-10-04T07:33:19Z] R copied 0e0752cdfacaa517102077052372a32de9557eb6baa37f5354a499b83c7196dd /root/btc-forensics/tz19-work--wt-report--CryptoTZ--TZ-16-phase2-decisive-gate.md
[2026-10-04T07:33:19Z] R copied 4e9ec4895337f21693a05bf7f6d6c163e77d6649273c225074c732ceefc2b771 /root/btc-forensics/tz19-work--wt-report--CryptoTZ--TZ-16a-phase2-decisive-gate.md
[2026-10-04T07:33:19Z] R copied b989a1d32ee66cf7c95495773484037e9399542829b311045f6e938637001ba1 /root/btc-forensics/tz19-work--wt-report--CryptoTZ--TZ-18a-chainbook-capture-redeploy.md
[2026-10-04T07:33:19Z] R copied 9d6d3457978fa210cbdb0cb87aa54c7059f86cb3544ce29ff388be610c784f07 /root/btc-forensics/tz19-work--wt-report--CryptoTZ--TZ-19-phase2-second-look.md
[2026-10-04T07:33:19Z] R copied 729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68 /root/btc-forensics/tz19-work--wt-report--research--pfair.py
[2026-10-04T07:33:19Z] R copied b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa /root/btc-forensics/tz19-work--wt-report--research--selftest-pfair.py
[2026-10-04T07:33:19Z] R copied ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a /root/btc-forensics/tz19-work--wt-report--research--selftest-twap-divergence.py
[2026-10-04T07:33:19Z] R copied 6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473 /root/btc-forensics/tz19-work--wt-report--research--twap-divergence.py
[2026-10-04T07:33:19Z] R copied f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4 /root/btc-forensics/tz19-work--wt-report--research--tz02-distribution.py
[2026-10-04T07:33:19Z] R copied 715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f /root/btc-forensics/tz19-work--wt-report--research--tz06-calibration.py
[2026-10-04T07:33:19Z] R copied 513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771 /root/btc-forensics/tz19-work--wt-report--research--tz07a-variance-time.py
[2026-10-04T07:33:19Z] R copied 424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc /root/btc-forensics/tz19-work--wt-report--research--tz07b-settlement-dispersion.py
[2026-10-04T07:33:19Z] R copied 37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c /root/btc-forensics/tz19-work--wt-report--research--tz08a-out-of-sample.py
[2026-10-04T07:33:19Z] R copied b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6 /root/btc-forensics/tz19-work--wt-report--research--tz09-disk-inventory.py
[2026-10-04T07:33:19Z] R copied 406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088 /root/btc-forensics/tz19-work--wt-report--research--tz10b-sigma-or-link.py
[2026-10-04T07:33:19Z] R copied 0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839 /root/btc-forensics/tz19-work--wt-report--research--tz11a-student-link.py
[2026-10-04T07:33:19Z] R copied d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999 /root/btc-forensics/tz19-work--wt-report--research--tz12-sized-gate.py
[2026-10-04T07:33:19Z] R copied a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd /root/btc-forensics/tz19-work--wt-report--research--tz13-sized-gate-test3.py
[2026-10-04T07:33:19Z] R copied 978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02 /root/btc-forensics/tz19-work--wt-report--research--tz14-quote-inventory.py
[2026-10-04T07:33:19Z] R copied 66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3 /root/btc-forensics/tz19-work--wt-report--research--tz15-phase2-gate.py
[2026-10-04T07:33:19Z] R copied 3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125 /root/btc-forensics/tz19-work--wt-report--research--tz16a-phase2-decisive-gate.py
[2026-10-04T07:33:19Z] R copied e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92 /root/btc-forensics/tz19-work--wt-report--research--tz17-settlement-chain.py
[2026-10-04T07:33:19Z] R copied e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae /root/btc-forensics/tz19-work--wt-report--research--tz18a-chainbook-capture.py
[2026-10-04T07:33:19Z] R copied eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d /root/btc-forensics/tz19-work--wt-report--research--recorder--analyze.py
[2026-10-04T07:33:19Z] R copied 8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d /root/btc-forensics/tz19-work--wt-report--research--recorder--config.py
[2026-10-04T07:33:19Z] R copied 79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045 /root/btc-forensics/tz19-work--wt-report--research--recorder--manifest.py
[2026-10-04T07:33:19Z] R copied 50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2 /root/btc-forensics/tz19-work--wt-report--research--recorder--probe.py
[2026-10-04T07:33:19Z] R copied 9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03 /root/btc-forensics/tz19-work--wt-report--research--recorder--recorder.py
[2026-10-04T07:33:19Z] R copied c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90 /root/btc-forensics/tz19-work--wt-report--research--recorder--selftest.py
```

</details>

## Appendix C — B-RECLAIM-OWN, every file copied

`reclaim /root/tz20-work`, the 121 `R copied` lines, verbatim, in the order printed. They include `instants.json`
and the 45 files of `logs/` (§2's logs `00` to `44`), each by its SHA-256 in the store.

<details><summary>121 lines</summary>

```text
[2026-10-04T08:33:56Z] R copied bc21d105e4870a19a7f77f2bb7f64eb9ac2096fc5cde635d012dff2f4a77854f /root/btc-forensics/tz20-work--instants.json
[2026-10-04T08:33:56Z] R copied a41ffc522c17ade796ee6801e8590c3c0043e5f6eaf3860c3d7e93622fdc4960 /root/btc-forensics/tz20-work--logs--00-fingerprint.log
[2026-10-04T08:33:56Z] R copied 55829ca2fbeed679cc6b2b3ef38990a6970052997f54a20a42bf198e83cf3cb7 /root/btc-forensics/tz20-work--logs--01-host-gate.log
[2026-10-04T08:33:56Z] R copied 083986a1d786b81ea451df4941d6c2796e9576ac0906ea5d458859d150c5bc70 /root/btc-forensics/tz20-work--logs--02-refs.log
[2026-10-04T08:33:56Z] R copied 19179b355f0182640c1efa6abdf0db972a03913231b90096a870a5cd20c109f9 /root/btc-forensics/tz20-work--logs--03-branch.log
[2026-10-04T08:33:56Z] R copied 63fdf501f3997f253037c09687902c6275bf8d2e96fe889b5e3fe465b8623ac1 /root/btc-forensics/tz20-work--logs--04-extract.log
[2026-10-04T08:33:56Z] R copied 2adcea80aadf0d10ecc9bc551373e72626ebf55c4e0b914aac6ddeb926e4a124 /root/btc-forensics/tz20-work--logs--05-push.log
[2026-10-04T08:33:56Z] R copied a0765adddc96aaeb9a9fdf7e98aa639c998c0ba2089017a4529e2a9b618c9420 /root/btc-forensics/tz20-work--logs--06-pr.log
[2026-10-04T08:33:56Z] R copied 367ce892198487355fecded1155dbe421d65b00535210054035686c86fc5fa37 /root/btc-forensics/tz20-work--logs--07-state.log
[2026-10-04T08:33:56Z] R copied 4313286b104138b5eee7df8671cf53715ee407cec1323970cee68ef574ea3c36 /root/btc-forensics/tz20-work--logs--08-reclaim-old.log
[2026-10-04T08:33:56Z] R copied a0885a72f2060b4cf07be63361b8c239cc6c4d54aa4f474993d63ebfcd3e0a87 /root/btc-forensics/tz20-work--logs--09-worktrees-old.log
[2026-10-04T08:33:56Z] R copied ef9f01a5d8cc64a64315ef57b76cff86db8cf4a1bbd6aebf3cead19d38ea0a42 /root/btc-forensics/tz20-work--logs--10-rm-tz16a.log
[2026-10-04T08:33:56Z] R copied 4546fb75901c7e3a35b4e600ab6be9c021215f286b9ed9f4225967e9d96efe57 /root/btc-forensics/tz20-work--logs--11-rm-tz19.log
[2026-10-04T08:33:56Z] R copied a95f8ee83eb03cc5a87f1121e6288d22e7ef2802360cc6096f9740dc71a85d88 /root/btc-forensics/tz20-work--logs--12-reclaim-old-verify.log
[2026-10-04T08:33:56Z] R copied e006943d2f22c49e604e238cb3a655510973fed39fb46f61f2ae2c5b95531674 /root/btc-forensics/tz20-work--logs--13-recorder-tree.log
[2026-10-04T08:33:56Z] R copied 70c824f000be67a747bc4dc9d4b55d6deb49fd5f5b781f39ff410a00f16f54a9 /root/btc-forensics/tz20-work--logs--14-path-recorder.log
[2026-10-04T08:33:56Z] R copied 470838a4046faea0df70935414d2b7de1f87fa98b7bfeaaef15e8ab990a1075b /root/btc-forensics/tz20-work--logs--15-path-chainbook.log
[2026-10-04T08:33:56Z] R copied 289d254be509d321e457ae5d01f74b7274dab212a596df7f8ac8181a90bddde9 /root/btc-forensics/tz20-work--logs--16-install.log
[2026-10-04T08:33:56Z] R copied 94d4842d367bb95a41f1caeae5b90b2c3b2ea223decf80a4770f5bbb5b31b814 /root/btc-forensics/tz20-work--logs--17-mark-start-rec.log
[2026-10-04T08:33:56Z] R copied 94fa4638e039dcd220325afb626c52d8ec95f75ad3500be8d9d805a58a70938e /root/btc-forensics/tz20-work--logs--18-mark-start-cb.log
[2026-10-04T08:33:56Z] R copied 606f1461b6ac6739b93bf8472270a4809cf6117b26a8754b465513dfd7a28df0 /root/btc-forensics/tz20-work--logs--19-classifier-refusal-start.log
[2026-10-04T08:33:56Z] R copied af6d44d0ad7be039ccf6ab77419eec0a4fb6358924bb5f018d765e0f3d24d25d /root/btc-forensics/tz20-work--logs--20-boss-start-blocks.log
[2026-10-04T08:33:56Z] R copied 219ea94c5cec1474658340a900dc81a906b8a9b3ee3f4254d12bb4455ec1565f /root/btc-forensics/tz20-work--logs--21-start-verify.log
[2026-10-04T08:33:56Z] R copied 7641b2a8d21421b593248f8aefeae244bb2c2f29d8e40e39f0d295da5e8d0796 /root/btc-forensics/tz20-work--logs--22-unit-0.log
[2026-10-04T08:33:56Z] R copied aeb262465b261303953fccd96637e1f18b88996e0fec8f77876f5e8afad5993f /root/btc-forensics/tz20-work--logs--23-start.log
[2026-10-04T08:33:56Z] R copied c08e4b530f66e3a16d63bc5b3e8a75a9c78715605b2eafb81c90256c9283efc1 /root/btc-forensics/tz20-work--logs--24-cb-01.log
[2026-10-04T08:33:56Z] R copied 6df0b77c1a58e6cc77d09390a21ea1e4c07b76f8f3141218ece3148671e10682 /root/btc-forensics/tz20-work--logs--25-rec-01.log
[2026-10-04T08:33:56Z] R copied db828de225a0aa5af2643702fb2a46940ad4f5472ade65e88cac060843beff37 /root/btc-forensics/tz20-work--logs--26-cb-02.log
[2026-10-04T08:33:56Z] R copied c611b64c7788bf80247ba955e8ec2f014063bdd6cbb66f564389460d23986a53 /root/btc-forensics/tz20-work--logs--27-rec-02.log
[2026-10-04T08:33:56Z] R copied be0374083cd8c7b65861b7e107b1c99277a046d1f36c04709e31be4b8cddc35e /root/btc-forensics/tz20-work--logs--28-cb-03.log
[2026-10-04T08:33:56Z] R copied e0839d65c1e942c2e4b7eb8a90638778ffc71f174835058e9ec1b8234c526520 /root/btc-forensics/tz20-work--logs--29-rec-03.log
[2026-10-04T08:33:56Z] R copied 0e1b75409b24b93f74fed358488a7967d1521a3ffb479a481864ac304bfabed3 /root/btc-forensics/tz20-work--logs--30-cb-04.log
[2026-10-04T08:33:56Z] R copied 6115741c9fc97620e828acef0952ee1f3a8151867b34872f8ae782390522d107 /root/btc-forensics/tz20-work--logs--31-rec-04.log
[2026-10-04T08:33:56Z] R copied fc8fd013093200e576d20a3c15c2d2809fd0c38295b2e6d1a2b3168f64d6d912 /root/btc-forensics/tz20-work--logs--32-cb-05.log
[2026-10-04T08:33:56Z] R copied 1cc31cbd2f9826e556c57fab767fb4e8213474d9750fa8a0e380530cbcee333a /root/btc-forensics/tz20-work--logs--33-rec-05.log
[2026-10-04T08:33:56Z] R copied a272a824ba885f910921a16b2e3e29c059c8cd699cb0b64b730490f0b29de47b /root/btc-forensics/tz20-work--logs--34-mark-kill-cb.log
[2026-10-04T08:33:56Z] R copied 5cf6b6dd6517e8d87f8df870d7ebc3e605804e5732ee6c34331f83c828e2c93b /root/btc-forensics/tz20-work--logs--35-kill-cb.log
[2026-10-04T08:33:56Z] R copied e05fd074eacf4bfdc002d232fdc05e3adc03cbb3047c05180864deb7184dd403 /root/btc-forensics/tz20-work--logs--36-restart-cb.log
[2026-10-04T08:33:56Z] R copied 2f1f6016f2be6066e0ead18479599de10e01d45077b461f058e1e22f25680fe7 /root/btc-forensics/tz20-work--logs--37-rec-06.log
[2026-10-04T08:33:56Z] R copied 32346f355dee0c696d7e6c8442bde9a2ebedc69fdc9f1c05f77ae6dee46f8e23 /root/btc-forensics/tz20-work--logs--38-mark-kill-rec.log
[2026-10-04T08:33:56Z] R copied f167e3dacc00c27c563b5a7c9b466405efe7ae993b425775e1f0cad3b1b4a728 /root/btc-forensics/tz20-work--logs--39-kill-rec.log
[2026-10-04T08:33:56Z] R copied 424a0eb542a45bba645e60bb48f14a3fcae4ab04e4486f4703301b371bee96fd /root/btc-forensics/tz20-work--logs--40-restart-rec.log
[2026-10-04T08:33:56Z] R copied 3f9db04080ac7f7887919ac17c2dc24037a7a5016b42197b6d5653cab8eba268 /root/btc-forensics/tz20-work--logs--41-final.log
[2026-10-04T08:33:56Z] R copied 2347563bcbe5ed858e195eea5ca44b0067ae0027c53d6cc64360a9cd88fa1fdd /root/btc-forensics/tz20-work--logs--42-closing-host-block.log
[2026-10-04T08:33:56Z] R copied 9c04c5f5dfe30118e659df93be0a2dc9ca9757583b27384528fbb7a5dba83459 /root/btc-forensics/tz20-work--logs--43-closing-reads.log
[2026-10-04T08:33:56Z] R copied 078f44bb648740bad33f129a2c2150f2d5a9329231afd82028f62683f2ad3831 /root/btc-forensics/tz20-work--logs--44-separation-check.log
[2026-10-04T08:33:56Z] R copied 29056cf78851d10feffeff525270a25158f7321f4cb80fe4157b4b07f3dc7042 /root/btc-forensics/tz20-work--wt--.git
[2026-10-04T08:33:56Z] R copied 9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b /root/btc-forensics/tz20-work--wt--.gitignore
[2026-10-04T08:33:56Z] R copied 437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b /root/btc-forensics/tz20-work--wt--BTC-EXECUTOR-INSTRUCTIONS.md
[2026-10-04T08:33:56Z] R copied 7e99182f15edf1d1dbb9b6812bc747a4d321f4145f55b43e223b8918b6338003 /root/btc-forensics/tz20-work--wt--SYSTEM-MAP.md
[2026-10-04T08:33:56Z] R copied 6077fb6a0fb62d5803e70ee5d6f0b8bc8332d756da0af637606eca99bf44f65b /root/btc-forensics/tz20-work--wt--CryptoReports--TZ-01-twap-divergence-report.md
[2026-10-04T08:33:56Z] R copied bc655c569ec10dffcf817f9dc6373575749b3f147441af640c7738ec5feb47bc /root/btc-forensics/tz20-work--wt--CryptoReports--TZ-01a-twap-divergence-corrected-report.md
[2026-10-04T08:33:56Z] R copied c7db53c035d389f05a784ba4c9b398a417c9aa7614112ac0d1afa842ccdedef2 /root/btc-forensics/tz20-work--wt--CryptoReports--TZ-02-divergence-distribution-report.md
[2026-10-04T08:33:56Z] R copied e14cdd5067ed53bfbb4bef6de150331fbcb1ef259793953f165d25ee11a4d397 /root/btc-forensics/tz20-work--wt--CryptoReports--TZ-03-repo-hygiene-report.md
[2026-10-04T08:33:56Z] R copied 237116cc437dd9216927cf175a0c66921cff2296385bb4b4914cd8d3be74cf51 /root/btc-forensics/tz20-work--wt--CryptoReports--TZ-04-market-recorder-report.md
[2026-10-04T08:33:56Z] R copied 975843f66a9c0d563c165e681b69482fbefbf8aca880bdd9f87216997e63292c /root/btc-forensics/tz20-work--wt--CryptoReports--TZ-04a-market-recorder-corrected-report.md
[2026-10-04T08:33:56Z] R copied a18ffd566085cea8f10feba139fadda0f1592f38adddde7e008792c46e8a8e9c /root/btc-forensics/tz20-work--wt--CryptoReports--TZ-04b-market-recorder-scoring-report.md
[2026-10-04T08:33:56Z] R copied ec548d0e1a4b9bf09695d079b7513428b022460a2b411f9c8ee54f4698778daf /root/btc-forensics/tz20-work--wt--CryptoReports--TZ-05-quote-capture-report.md
[2026-10-04T08:33:56Z] R copied cddca348120ae278f3c399ea21353f57e8b3722f3b0372e247cc985ab1351805 /root/btc-forensics/tz20-work--wt--CryptoReports--TZ-05a-quote-capture-deploy-report.md
[2026-10-04T08:33:56Z] R copied 33863ce6d62443dd070646854b135438ee624c96b5204cd9851cfbca9939396f /root/btc-forensics/tz20-work--wt--CryptoReports--TZ-06-pfair-calibration-report.md
[2026-10-04T08:33:56Z] R copied 4056137f8de8ef6fa39e43a348a1f60bdfee10f7ffe2c29ebb6e4f6e7894c5b4 /root/btc-forensics/tz20-work--wt--CryptoReports--TZ-07-variance-time-report.md
[2026-10-04T08:33:56Z] R copied 15c26ec8b7ac670bb136177fd3a87dcd56935077714feff48f833dd08b3af72b /root/btc-forensics/tz20-work--wt--CryptoReports--TZ-07a-variance-time-report.md
[2026-10-04T08:33:56Z] R copied 44b2ee1a80c80867aa17bf6b0c378fccbf203655dfc39a7f323861aab4d7cf80 /root/btc-forensics/tz20-work--wt--CryptoReports--TZ-07b-settlement-dispersion-report.md
[2026-10-04T08:33:56Z] R copied b0d0c8ed31c28bfa52dc449da4a06d33318f17221a6f9d94ce9bcc8f7ecccffe /root/btc-forensics/tz20-work--wt--CryptoReports--TZ-08-out-of-sample-report.md
[2026-10-04T08:33:56Z] R copied 86d4ba81e196ace179c65067a3620bb77dba20019f428ecd1c6e588bde6c1188 /root/btc-forensics/tz20-work--wt--CryptoReports--TZ-08a-out-of-sample-report.md
[2026-10-04T08:33:56Z] R copied 0553061fb9f4793e0e73167042af0a770c5d640fae56f2fb1c7611b494c45815 /root/btc-forensics/tz20-work--wt--CryptoReports--TZ-17-settlement-chain-report.md
[2026-10-04T08:33:56Z] R copied 455f58e0616daeacfb67ee7302d84520826780720b5c56c7e7a06463ec63dd57 /root/btc-forensics/tz20-work--wt--CryptoTZ--TZ-01-twap-divergence.md
[2026-10-04T08:33:56Z] R copied a8c4c7c22881236903797e2ffc2d8c87d6e9fc74cd282c7e40feb9eaecab65e3 /root/btc-forensics/tz20-work--wt--CryptoTZ--TZ-01a-twap-divergence-corrected.md
[2026-10-04T08:33:56Z] R copied c8abadec3bb4763a383f397f8ef188cda4228ed1d356f635f8674456d586f2a3 /root/btc-forensics/tz20-work--wt--CryptoTZ--TZ-02-divergence-distribution.md
[2026-10-04T08:33:56Z] R copied 0cd150f54862e6c640510acba90c36f1c351e97d0e9b068a573822455668d56e /root/btc-forensics/tz20-work--wt--CryptoTZ--TZ-03-repo-hygiene.md
[2026-10-04T08:33:56Z] R copied 95b2fd8d752a759f7b274aa0fc8ca62b54d9d27d84bc91cc33cc1014c518fe09 /root/btc-forensics/tz20-work--wt--CryptoTZ--TZ-04-market-recorder.md
[2026-10-04T08:33:56Z] R copied fff99e417a5117ab9e5186e793adea8bec9be9140864776a84ef0f7c1f20988b /root/btc-forensics/tz20-work--wt--CryptoTZ--TZ-04a-market-recorder-corrected.md
[2026-10-04T08:33:56Z] R copied f4ab08b6a58f84401d38124ff54a665aaa0808a0fb3b376a1362fcb63960effc /root/btc-forensics/tz20-work--wt--CryptoTZ--TZ-04b-market-recorder-scoring.md
[2026-10-04T08:33:56Z] R copied 4b9a41fb3301712e6629fb565c47e50a38cb3c85e605122394797ed9094285fe /root/btc-forensics/tz20-work--wt--CryptoTZ--TZ-05-quote-capture.md
[2026-10-04T08:33:56Z] R copied 16f4821308e0f931a469acd0c7d1facffc4c3bb6c75bcd266305d1acc241410b /root/btc-forensics/tz20-work--wt--CryptoTZ--TZ-05a-quote-capture-deploy.md
[2026-10-04T08:33:56Z] R copied ec2135c810be9e736946c004b7a4ced0d5a00a322061c89a1519f2d4a30f8373 /root/btc-forensics/tz20-work--wt--CryptoTZ--TZ-06-pfair-calibration.md
[2026-10-04T08:33:56Z] R copied 759d8ed001ed6746a6b7badd430fa1b3b362849594429849cf196bd892342e2b /root/btc-forensics/tz20-work--wt--CryptoTZ--TZ-07-variance-time.md
[2026-10-04T08:33:56Z] R copied 0e4852301c493ed7e4cb98d8d880a2c6b42b55f01811976ca9131fc62e61c4e3 /root/btc-forensics/tz20-work--wt--CryptoTZ--TZ-07a-variance-time.md
[2026-10-04T08:33:56Z] R copied 476344ccf393c8e3f3eb7a70e97f71af7433a45a02af069978b2e8138c155541 /root/btc-forensics/tz20-work--wt--CryptoTZ--TZ-07b-settlement-dispersion.md
[2026-10-04T08:33:56Z] R copied bacb45ec2c0a3ed824972fe0b536a99f5ef3bad68e78a5c07fbf0c1a09d77d00 /root/btc-forensics/tz20-work--wt--CryptoTZ--TZ-08-out-of-sample.md
[2026-10-04T08:33:56Z] R copied 3c6ea77fabe9716b6bde98cdba728b67cb62a14f8172ac59bffd47dd04f5e687 /root/btc-forensics/tz20-work--wt--CryptoTZ--TZ-08a-out-of-sample.md
[2026-10-04T08:33:56Z] R copied db811fea3dea51b58c4a7894cb9666e60b6fcb5b2e86073ba7c89cc9c6fe09e1 /root/btc-forensics/tz20-work--wt--CryptoTZ--TZ-09-disk-inventory.md
[2026-10-04T08:33:56Z] R copied c08bea39dd3582d4ce8373ee5dabbe1d06357722fedad5c9f97e92f65ab4054a /root/btc-forensics/tz20-work--wt--CryptoTZ--TZ-10-sigma-or-link.md
[2026-10-04T08:33:56Z] R copied 2688836d8e4dd981d7e9bef324d81844b4be6884e2d1d5b4c103f65db6b5e403 /root/btc-forensics/tz20-work--wt--CryptoTZ--TZ-10a-sigma-or-link.md
[2026-10-04T08:33:56Z] R copied 8705ca3783784511f8a4f33b23a1664566fb2bda7159d860295a522aadafe49b /root/btc-forensics/tz20-work--wt--CryptoTZ--TZ-10b-sigma-or-link.md
[2026-10-04T08:33:56Z] R copied 15220788b164ee4d53d32892061bbc2ebd1509acf30282dd453af2c6df86775f /root/btc-forensics/tz20-work--wt--CryptoTZ--TZ-11-student-link-and-domain.md
[2026-10-04T08:33:56Z] R copied dcd05f165d9057326a930814649cf81c9033980f6fb354cde8dd1fd15628c076 /root/btc-forensics/tz20-work--wt--CryptoTZ--TZ-11a-student-link-and-domain.md
[2026-10-04T08:33:56Z] R copied cb845f93f61cc8558bcf611c38e5b6a1b859219574bb20e0e806e802263e5d6a /root/btc-forensics/tz20-work--wt--CryptoTZ--TZ-12-sized-gate.md
[2026-10-04T08:33:56Z] R copied 0e0752cdfacaa517102077052372a32de9557eb6baa37f5354a499b83c7196dd /root/btc-forensics/tz20-work--wt--CryptoTZ--TZ-16-phase2-decisive-gate.md
[2026-10-04T08:33:56Z] R copied 4e9ec4895337f21693a05bf7f6d6c163e77d6649273c225074c732ceefc2b771 /root/btc-forensics/tz20-work--wt--CryptoTZ--TZ-16a-phase2-decisive-gate.md
[2026-10-04T08:33:56Z] R copied b989a1d32ee66cf7c95495773484037e9399542829b311045f6e938637001ba1 /root/btc-forensics/tz20-work--wt--CryptoTZ--TZ-18a-chainbook-capture-redeploy.md
[2026-10-04T08:33:56Z] R copied 9d6d3457978fa210cbdb0cb87aa54c7059f86cb3544ce29ff388be610c784f07 /root/btc-forensics/tz20-work--wt--CryptoTZ--TZ-19-phase2-second-look.md
[2026-10-04T08:33:56Z] R copied 178f2a339e60b5eacd6fecb4cf6f91f6165c832092aa04e47bc9a1971597c7ba /root/btc-forensics/tz20-work--wt--CryptoTZ--TZ-20-capture-under-systemd.md
[2026-10-04T08:33:56Z] R copied a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2 /root/btc-forensics/tz20-work--wt--deploy--systemd--btc-chainbook.service
[2026-10-04T08:33:56Z] R copied 3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1 /root/btc-forensics/tz20-work--wt--deploy--systemd--btc-recorder.service
[2026-10-04T08:33:56Z] R copied 729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68 /root/btc-forensics/tz20-work--wt--research--pfair.py
[2026-10-04T08:33:56Z] R copied b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa /root/btc-forensics/tz20-work--wt--research--selftest-pfair.py
[2026-10-04T08:33:56Z] R copied ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a /root/btc-forensics/tz20-work--wt--research--selftest-twap-divergence.py
[2026-10-04T08:33:56Z] R copied 6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473 /root/btc-forensics/tz20-work--wt--research--twap-divergence.py
[2026-10-04T08:33:56Z] R copied f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4 /root/btc-forensics/tz20-work--wt--research--tz02-distribution.py
[2026-10-04T08:33:56Z] R copied 715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f /root/btc-forensics/tz20-work--wt--research--tz06-calibration.py
[2026-10-04T08:33:56Z] R copied 513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771 /root/btc-forensics/tz20-work--wt--research--tz07a-variance-time.py
[2026-10-04T08:33:56Z] R copied 424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc /root/btc-forensics/tz20-work--wt--research--tz07b-settlement-dispersion.py
[2026-10-04T08:33:56Z] R copied 37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c /root/btc-forensics/tz20-work--wt--research--tz08a-out-of-sample.py
[2026-10-04T08:33:56Z] R copied b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6 /root/btc-forensics/tz20-work--wt--research--tz09-disk-inventory.py
[2026-10-04T08:33:56Z] R copied 406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088 /root/btc-forensics/tz20-work--wt--research--tz10b-sigma-or-link.py
[2026-10-04T08:33:56Z] R copied 0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839 /root/btc-forensics/tz20-work--wt--research--tz11a-student-link.py
[2026-10-04T08:33:56Z] R copied d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999 /root/btc-forensics/tz20-work--wt--research--tz12-sized-gate.py
[2026-10-04T08:33:56Z] R copied a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd /root/btc-forensics/tz20-work--wt--research--tz13-sized-gate-test3.py
[2026-10-04T08:33:56Z] R copied 978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02 /root/btc-forensics/tz20-work--wt--research--tz14-quote-inventory.py
[2026-10-04T08:33:56Z] R copied 66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3 /root/btc-forensics/tz20-work--wt--research--tz15-phase2-gate.py
[2026-10-04T08:33:56Z] R copied 3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125 /root/btc-forensics/tz20-work--wt--research--tz16a-phase2-decisive-gate.py
[2026-10-04T08:33:56Z] R copied e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92 /root/btc-forensics/tz20-work--wt--research--tz17-settlement-chain.py
[2026-10-04T08:33:56Z] R copied e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae /root/btc-forensics/tz20-work--wt--research--tz18a-chainbook-capture.py
[2026-10-04T08:33:56Z] R copied 104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7 /root/btc-forensics/tz20-work--wt--research--tz20-capture-under-systemd.py
[2026-10-04T08:33:56Z] R copied eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d /root/btc-forensics/tz20-work--wt--research--recorder--analyze.py
[2026-10-04T08:33:56Z] R copied 8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d /root/btc-forensics/tz20-work--wt--research--recorder--config.py
[2026-10-04T08:33:56Z] R copied 79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045 /root/btc-forensics/tz20-work--wt--research--recorder--manifest.py
[2026-10-04T08:33:56Z] R copied 50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2 /root/btc-forensics/tz20-work--wt--research--recorder--probe.py
[2026-10-04T08:33:56Z] R copied 9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03 /root/btc-forensics/tz20-work--wt--research--recorder--recorder.py
[2026-10-04T08:33:56Z] R copied c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90 /root/btc-forensics/tz20-work--wt--research--recorder--selftest.py
```

</details>
