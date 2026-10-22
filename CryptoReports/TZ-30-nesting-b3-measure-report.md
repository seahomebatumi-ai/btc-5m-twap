# TZ-30 report — B3's measurement: can a violation of the nested pair be captured?

**B3 READING: NO CAPTURE.** All eight blocks of 96 members fall below `θ = 10` USDC: `S_b` = `−67.383`, `−28.097`, `−3.846`, `−258.298`, `−58.149`, `−46.664`, `−131.702` and `−1.917` USDC. The largest is `−1.917`. Each answer's false-reading probability is `2^-8 = 0.00390625` under independent blocks.

| block | first member | last member | `S_b`, USDC | against `θ = 10` |
|---|---|---|---|---|
| 1 | `1791706500` 2026-10-11 08:15 | `1791792000` 2026-10-12 08:00 | `−67.382523204295` | below |
| 2 | `1791792900` 2026-10-12 08:15 | `1791880200` 2026-10-13 08:30 | `−28.096568278984` | below |
| 3 | `1791881100` 2026-10-13 08:45 | `1791967500` 2026-10-14 08:45 | `−3.846111778517` | below |
| 4 | `1791968400` 2026-10-14 09:00 | `1792054800` 2026-10-15 09:00 | `−258.297909224847` | below |
| 5 | `1792055700` 2026-10-15 09:15 | `1792142100` 2026-10-16 09:15 | `−58.149298476613` | below |
| 6 | `1792143000` 2026-10-16 09:30 | `1792229400` 2026-10-17 09:30 | `−46.663873186684` | below |
| 7 | `1792230300` 2026-10-17 09:45 | `1792316700` 2026-10-18 09:45 | `−131.702127989504` | below |
| 8 | `1792317600` 2026-10-18 10:00 | `1792403100` 2026-10-19 09:45 | `−1.916692656212` | below |

- **G-REBUILD PASS.** The members' stored replies were `21,504`, all four tokens' `/book` replies. TZ-24's `line_check` read `10,752` of the two legs' replies valid. `10,693` of those were compared (`0.994512648810`, floor `0.90`), and the rebuilt touch equalled the reply's at `10,688` (`0.999532404377` of compared, floor `0.98`). `9,836` were equal at every level. Not compared: `59` unseeded, `0` unresolved.
- **G-REHEARSAL PASS: 9 of 9.** 357 lines, SHA-256 `402b378a274613153410aa068abaaa798d68d4770a22239a07442ba42411bade`, and all 7 variants' totals equal to the Architect's.
- **G-SET PASS.** 768 members of 775 candidates considered, `1791706500` to `1792403100`, with 7 non-members before the 768th member (at most 168 allowed). The second run printed `unchanged`. Member list SHA-256 `4d4a7f5f6397b63b945c0a85f8457e1cd3701a4754b5c1b3252904b1647bb9de`; `b3-set.json` SHA-256 `df4ae686b06a24d461e554e0fbbe36192619b1404550204b65513cb85dd965d9`.
- **DETERMINISM PASS: 48 of 48.**
- **G-STILL PASS:** unchanged since 2026-10-22T03:24:37Z.
- **Before the first price read.** The instrument's commit `fcd9ca566e9b948f0426707e7c3b5684f7f03b04` was on `origin` at `2026-10-22T03:24:19.294321725Z` (§3.1's `ls-remote`). The set's `state.json` record was written at `2026-10-22T03:33:00Z` by the first `strikes` run; the second run rewrote `set_at` to `03:33:10Z` with the same SHA-256 (§6 item 2). The first price read of a member, the first `score` ledger line, was at `2026-10-22T03:33:15Z`.

Instrument: `research/tz30-nesting-b3-measure.py`, SHA-256 `93dbbf1c…`, branch `tz-30-nesting-b3-measure`, PR #29, not merged. Executed on the capture host 2026-10-22, 03:22 to 04:56 UTC.

---

## 0. Fingerprint

**Map revision read:** `2026-10-20-a`, the revision the TZ header requires. **Anchors:** six of six as required: `A1` `229a944f2d51`, `A2` `6c5089330629`, `A3` `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable`, `A4` `437b45ea196b`, `A5` `0f6c90451cbd`, `A6` `729f0bcdbee3`. `A2`, `A4`, `A5` and `A6` were re-derived from the files themselves. `I0 fingerprint` (§0.2, 03:23:33Z, staged copy) and `I fingerprint` (§3.1, 03:24:04Z, worktree) both printed:

```
FINGERPRINT PASS: revision 2026-10-20-a; anchors 6 of 6, 4 re-derived; rows 41: frozen 38 of 38 equal, tracked 2, reported 1; the 6 files this instrument executes are frozen rows
```

The map's §0 table, every row as `I0 fingerprint` printed it at the primary checkout `c836913`:

| path | lines | bytes | state | SHA-256 | vs map |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 1526 | 355344 | reported | `682f2146201d72f3844008d2caded8bcc51f2e222c8ab2f4b551df0bc4190a4f` | — |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | equal |
| `research/twap-divergence.py` | 1135 | 50928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | equal |
| `research/selftest-twap-divergence.py` | 376 | 16736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | equal |
| `research/tz02-distribution.py` | 334 | 14511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | — |
| `research/pfair.py` | 441 | 19357 | frozen | `729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68` | equal |
| `research/selftest-pfair.py` | 619 | 32559 | frozen | `b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa` | equal |
| `research/tz06-calibration.py` | 577 | 27138 | frozen | `715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f` | equal |
| `research/tz07a-variance-time.py` | 623 | 28414 | frozen | `513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771` | equal |
| `research/tz07b-settlement-dispersion.py` | 515 | 24926 | frozen | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` | equal |
| `research/tz08a-out-of-sample.py` | 745 | 38822 | frozen | `37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c` | equal |
| `research/tz09-disk-inventory.py` | 894 | 41004 | frozen | `b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6` | equal |
| `research/tz10b-sigma-or-link.py` | 1224 | 61018 | frozen | `406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088` | equal |
| `research/tz11a-student-link.py` | 1231 | 64732 | frozen | `0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839` | equal |
| `research/tz12-sized-gate.py` | 1157 | 61637 | frozen | `d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999` | equal |
| `research/tz13-sized-gate-test3.py` | 1074 | 53901 | frozen | `a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd` | equal |
| `research/tz14-quote-inventory.py` | 2124 | 109972 | frozen | `978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02` | equal |
| `research/tz15-phase2-gate.py` | 1517 | 73799 | frozen | `66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3` | equal |
| `research/tz16a-phase2-decisive-gate.py` | 2198 | 111192 | frozen | `3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125` | equal |
| `research/tz17-settlement-chain.py` | 1102 | 38622 | frozen | `e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92` | equal |
| `research/tz18a-chainbook-capture.py` | 1683 | 69517 | frozen | `e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae` | equal |
| `research/tz20-capture-under-systemd.py` | 771 | 36528 | frozen | `104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7` | equal |
| `research/tz21-recorder-memory.py` | 1284 | 59009 | frozen | `d6d2dc195809f2160fda7856980d8ccfbf0006ba0836943ff789c877f9d5795f` | equal |
| `research/tz23-maker-m0.py` | 1184 | 54885 | frozen | `6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f` | equal |
| `research/tz24-nesting-b2.py` | 1535 | 76142 | frozen | `4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b` | equal |
| `research/tz26-nesting-b3-capture.py` | 2492 | 118466 | frozen | `caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec` | equal |
| `research/tz27-pairbook-archive.py` | 2078 | 106284 | frozen | `2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673` | equal |
| `research/tz28-pairbook-archive-timer.py` | 1438 | 74576 | frozen | `46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4` | equal |
| `research/tz29-maker-m0-second-look.py` | 1225 | 68959 | frozen | `18defff93d08c13ea4638a518c88a3fec5541fcf53fb6827451e727f2204d905` | equal |
| `research/recorder/recorder.py` | 651 | 27821 | frozen | `0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7` | equal |
| `research/recorder/config.py` | 112 | 4773 | frozen | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | equal |
| `research/recorder/manifest.py` | 254 | 10002 | frozen | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | equal |
| `research/recorder/analyze.py` | 813 | 34705 | frozen | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` | equal |
| `research/recorder/probe.py` | 227 | 9324 | frozen | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | equal |
| `research/recorder/selftest.py` | 573 | 30591 | frozen | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` | equal |
| `deploy/systemd/btc-recorder.service` | 23 | 707 | frozen | `3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1` | equal |
| `deploy/systemd/btc-chainbook.service` | 22 | 724 | frozen | `a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2` | equal |
| `deploy/systemd/btc-pairbook.service` | 22 | 761 | frozen | `ba02fe4175b961c387ea8066eb084704e69efc7fd0a48d8f623a0198334f8dd8` | equal |
| `deploy/systemd/btc-pairbook-archive.service` | 17 | 794 | frozen | `2e7fd45382af3da3b2ec29ced8d69870ef3d4481da4c6f327b90fc6cb5af78e7` | equal |
| `deploy/systemd/btc-pairbook-archive.timer` | 13 | 417 | frozen | `07581f4f331fbf9d2a1113cac42a2872d65ac69a872991bff7d2bda235eac913` | equal |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | — |

`SYSTEM-MAP.md`: 1,526 lines, 355,344 bytes, SHA-256 `682f2146201d72f3844008d2caded8bcc51f2e222c8ab2f4b551df0bc4190a4f`.

**Model:** the TZ names Opus. This session runs the Opus model the harness configures.

### 0.0 Work tree, 0.1 staging

`mkdir /root/tz30-work /root/tz30-work/logs; echo "exit=$?"` printed `exit=0`, so neither directory existed before. §0.1's script, run verbatim, printed:

```
/root/tz30-work/stage/research/tz30-nesting-b3-measure.py 2518 131119 93dbbf1c4f84553a7bc041387ef92c3c0d8747c384d383b4fcd0b247fcd131ab
exit=0
```

### 0.3 Host gate — `logs/03-host-gate.log`, verbatim

```
Thu Oct 22 03:23:43 AM UTC 2026
1792639423
1
MemTotal:         978640 kB
MemAvailable:     286140 kB
SwapTotal:       3174396 kB
SwapFree:        2789452 kB
2026-08-02 07:24:32
IDX BOOT ID                          FIRST ENTRY                 LAST ENTRY
 -5 23a31fad2f064f04b9e138eac29658f3 Tue 2026-06-09 06:23:40 UTC Fri 2026-06-26 14:13:44 UTC
 -4 a38e17445ce341bc8b877be9d3d4f648 Fri 2026-06-26 14:13:52 UTC Tue 2026-07-14 16:15:10 UTC
 -3 5f4d18a6ba8041bd80e7d1e192c5ee28 Tue 2026-07-14 16:15:20 UTC Fri 2026-07-17 01:01:21 UTC
 -2 b1b399c70c6e4dcc934755f70a2ca231 Fri 2026-07-17 01:01:43 UTC Fri 2026-07-24 14:55:46 UTC
 -1 285d6962c92c407d837d1ce329b93aa4 Fri 2026-07-24 14:55:54 UTC Sun 2026-08-02 07:23:49 UTC
  0 48a803f03549473383be5baecf790d4e Sun 2026-08-02 07:24:34 UTC Thu 2026-10-22 03:23:30 UTC
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 12500103168
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json
1
3.12.3 2.5.3
16570 /root/btc-forensics/tz27-work--archive--set.json
ec71b1a7ce7db37ff29a49156006541dd5729c1df2c829c481eb64181228e4dd  /root/btc-forensics/tz27-work--archive--set.json
MainPID=4148534
Result=success
NRestarts=2
Id=btc-recorder.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Sun 2026-10-04 22:22:07 UTC

MainPID=2221487
Result=success
NRestarts=19
Id=btc-pairbook.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Thu 2026-10-22 03:03:38 UTC

MainPID=0
Result=success
NRestarts=0
Id=btc-pairbook-archive.service
ActiveState=inactive
SubState=dead
UnitFileState=static
ActiveEnterTimestamp=

Result=success
Id=btc-pairbook-archive.timer
ActiveState=active
SubState=waiting
UnitFileState=enabled
ActiveEnterTimestamp=Sun 2026-10-11 15:08:11 UTC

MainPID=0
Result=success
NRestarts=0
Id=btc-chainbook.service
ActiveState=inactive
SubState=dead
UnitFileState=disabled
ActiveEnterTimestamp=
NEXT                        LEFT LAST                           PASSED UNIT                       ACTIVATES
Fri 2026-10-23 03:00:20 UTC  23h Thu 2026-10-22 03:00:20 UTC 23min ago btc-pairbook-archive.timer btc-pairbook-archive.service

1 timers listed.
-- No entries --
End-Date: 2026-10-15  06:09:16
Start-Date: 2026-10-15  06:09:18
Commandline: /usr/bin/unattended-upgrade
End-Date: 2026-10-15  06:09:19
Start-Date: 2026-10-15  06:09:21
Commandline: /usr/bin/unattended-upgrade
End-Date: 2026-10-15  06:09:21
Start-Date: 2026-10-15  06:09:23
Commandline: /usr/bin/unattended-upgrade
End-Date: 2026-10-15  06:09:24
Start-Date: 2026-10-15  06:09:26
Commandline: /usr/bin/unattended-upgrade
End-Date: 2026-10-15  06:09:27
Start-Date: 2026-10-15  06:09:29
Commandline: /usr/bin/unattended-upgrade
End-Date: 2026-10-15  06:09:29
Start-Date: 2026-10-16  06:08:05
Commandline: /usr/bin/unattended-upgrade
Upgrade: libcurl3t64-gnutls:amd64 (8.5.0-2ubuntu10.15, 8.5.0-2ubuntu10.16), libcurl4t64:amd64 (8.5.0-2ubuntu10.15, 8.5.0-2ubuntu10.16), curl:amd64 (8.5.0-2ubuntu10.15, 8.5.0-2ubuntu10.16)
End-Date: 2026-10-16  06:08:06
Start-Date: 2026-10-16  06:08:09
Commandline: /usr/bin/unattended-upgrade
Upgrade: apache2-utils:amd64 (2.4.58-1ubuntu8.16, 2.4.58-1ubuntu8.17)
End-Date: 2026-10-16  06:08:10
Start-Date: 2026-10-20  06:28:05
Commandline: /usr/bin/unattended-upgrade
Upgrade: git:amd64 (1:2.43.0-1ubuntu7.3, 1:2.43.0-1ubuntu7.4), git-man:amd64 (1:2.43.0-1ubuntu7.3, 1:2.43.0-1ubuntu7.4)
End-Date: 2026-10-20  06:28:07
Start-Date: 2026-10-20  06:28:11
Commandline: /usr/bin/unattended-upgrade
Upgrade: libxtst6:amd64 (2:1.2.3-1.1build1, 2:1.2.3-1.1ubuntu0.1)
End-Date: 2026-10-20  06:28:11
Start-Date: 2026-10-21  06:12:47
Commandline: /usr/bin/unattended-upgrade
Upgrade: tzdata:amd64 (2026c-0ubuntu0.24.04.1, 2026e-0ubuntu0.24.04.1)
End-Date: 2026-10-21  06:12:48
Start-Date: 2026-10-21  06:12:51
Commandline: /usr/bin/unattended-upgrade
Upgrade: python3-jwt:amd64 (2.7.0-1ubuntu0.3, 2.7.0-1ubuntu0.4)
End-Date: 2026-10-21  06:12:52
disabled
exit=1
inactive
exit=3
e3975b5da44c5328adf3bf3914634cd878842c73
e8b46a85d61e1a17841962846f6d3012046c2d70
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3
/root/tz29-work exit=1
/root/tz18a-svc exit=0
/root/btc-recorder-svc exit=0
/root/btc-pairbook-svc exit=0
/root/btc-pairbook-archive-svc exit=0
/var/lib/btc-pairbook-archive exit=0
1896
/root/btc-5m-twap       c836913 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
72776879	/var/lib/btc-pairbook
4978552	/var/lib/btc-pairbook-archive
130910822	/root/.claude
608422394	/root/PROJECT_GAMING_PS5
/tmp/claude-0/-root-btc-5m-twap/2f1eadf7-1958-5f4f-857d-ccf68aa47272/scratchpad
total 40
drwx------ 10 root root 4096 Oct 22 03:22 .
drwx------ 25 root root 4096 Oct 22 03:22 ..
drwx------  4 root root 4096 Oct 22 03:22 2f1eadf7-1958-5f4f-857d-ccf68aa47272
drwx------  3 root root 4096 Oct 21 09:34 46827096-4c4d-4533-b0f6-e40cc63578f6
drwx------  3 root root 4096 Oct 20 04:24 6a6870c2-3843-4a2b-83cf-b2f45c5500a1
drwx------  3 root root 4096 Oct 21 09:25 6e88615c-345d-5a08-be99-6375cc1a1073
drwx------  4 root root 4096 Oct 20 04:24 7a160398-f4cf-54ee-b771-c3006d558bde
drwx------  3 root root 4096 Oct 22 03:22 c498ebed-32dd-4005-9ebd-4fcce8ce6682
drwx------  3 root root 4096 Oct 21 09:25 c79ceacd-d598-415d-89bf-67860a65609f
drwx------  3 root root 4096 Oct 21 09:37 eff3ddd1-cb45-4950-82cd-35b28b9c2c61
```

- **H1** — `find` printed exactly one path. PASS.
- **H2** — source `/dev/vda2`, size `31612203008`; `grep -c` printed `1`. PASS.
- **H3** — `3.12.3 2.5.3`. PASS.
- **H4** — `16570` bytes, SHA-256 `ec71b1a7ce7db37ff29a49156006541dd5729c1df2c829c481eb64181228e4dd`. PASS.
- **Memory gate** — `MemAvailable` 286,140 kB = `293,007,360` bytes, at least `116,711,424`. PASS.
- **Disk gate** — `avail` `12,500,103,168` bytes, at least `4,800,000,000`. PASS.

Recorded, carrying no threshold:

- One boot since 2026-08-02 07:24:34 UTC.
- The timer's journal since 2026-10-14 holds no entries.
- `telemetry-watch.service` reads `disabled` (exit 1) and `inactive` (exit 3).
- The three code trees are at `e3975b5…`, `e8b46a8…` and `d8194fd…`, as map §3 states.
- `/root/tz29-work` is absent (exit 1); the five code and state trees are present.
- The forensic store holds `1,896` files, map §3's count.
- Two worktrees, as map §3 states.
- The pair book's store is `72,776,879` bytes by `du`.
- Since TZ-29, two `claude` processes started at 2026-10-21 09:37:15/17 (pids `2113303` and `2113313`), beside this session's process `2223043`. Map §3 names pids `337573` and `337576`; neither is running.

### 0.5 Refs — `logs/04-refs.log`, verbatim (read 03:23:52 UTC, before §3.1's push)

```
2026-10-22T03:23:52.553790912Z
c836913bc6b594dea134815bff0a6aad4976d910	HEAD
c836913bc6b594dea134815bff0a6aad4976d910	refs/heads/main
7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8	refs/heads/tz-23-maker-m0
6f045cffc3601b589d3b8b7a6a9af6f73991e18b	refs/heads/tz-24-nesting-b2
e8b46a85d61e1a17841962846f6d3012046c2d70	refs/heads/tz-26-nesting-b3-capture
bce5a85be7850a33f95192265b916cc9c5e0aaf1	refs/heads/tz-27-pairbook-archive
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/heads/tz-28-pairbook-archive-timer
f6425f713034724210dc120d2108bcfad63cadc6	refs/heads/tz-29-maker-m0-second-look
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
0956da12bd26decbef0fd643b6f223102c7788ba	refs/pull/21/head
e3975b5da44c5328adf3bf3914634cd878842c73	refs/pull/22/head
7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8	refs/pull/23/head
6f045cffc3601b589d3b8b7a6a9af6f73991e18b	refs/pull/24/head
e8b46a85d61e1a17841962846f6d3012046c2d70	refs/pull/25/head
bce5a85be7850a33f95192265b916cc9c5e0aaf1	refs/pull/26/head
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/pull/27/head
f6425f713034724210dc120d2108bcfad63cadc6	refs/pull/28/head
ee2f6327390ef4d0c6169d1fba1a2ed4ae936dc3	refs/pull/3/head
0e13a5c76dfa2469ff25b3b0dd282872decf6f25	refs/pull/4/head
4216c04673ced76b5b2ac60ef57c9abedc46f9b9	refs/pull/5/head
5ed667afd1b53f036b9f938fcce13c0d709cd77f	refs/pull/6/head
c44af687203d14d5d485d4297c04cfb827096af9	refs/pull/7/head
26bbb61aed774a88355dd5204d8b69fda9135a68	refs/pull/8/head
e2625ea2b5473c311d59a48f32540ce39d58e591	refs/pull/9/head
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1791731892
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1791774020
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1791860420
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1791946820
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792033220
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792045110
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792119620
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792206020
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792226137
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792292420
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792378820
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792446859
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792465220
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792495417
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792551620
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792618744
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792638020
d3251aa2bd312409f7b096bfd5968f3bedbd1be5	refs/tags/tz-01a-dataset
ea9290b92b9fa50c22d0560d5d01dfa392af44df	refs/tags/tz-01a-dataset^{}
e299d4e45f48b7efaa8cb18bd54b139fc0627630	refs/tags/tz-27-pairbook-streams
bce5a85be7850a33f95192265b916cc9c5e0aaf1	refs/tags/tz-27-pairbook-streams^{}
ls-remote exit=0
lines: 57
c836913bc6b594dea134815bff0a6aad4976d910 2026-10-21T10:56:50+04:00 Update SYSTEM-MAP.md

M	SYSTEM-MAP.md
f05e16e70f9f874aa72e2ea4b461be465976fbbb 2026-10-21T10:54:54+04:00 Add files via upload

A	CryptoTZ/TZ-30-nesting-b3-measure.md
**Revision string:** `2026-10-20-a`
```

There are **57** ref lines against map §1's 54. The three added lines are the archive's tags `pairbook-streams-1792551620` (calendar run 2026-10-21 03:00:20), `pairbook-streams-1792618744` (off-calendar run, 2026-10-21 21:39:04) and `pairbook-streams-1792638020` (calendar run 2026-10-22 03:00:20). §0.5 expects one tag a run, so this is consistent with it. Nothing else differs. `main` is at `c836913`, which carries revision `2026-10-20-a`. Two commits on `main`'s first-parent line sit above `33ec8e3`: `f05e16e` (adds `CryptoTZ/TZ-30-nesting-b3-measure.md`) and `c836913` (modifies `SYSTEM-MAP.md`). `refs/heads/tz-30-nesting-b3-measure` did not exist. Neither BLOCK condition holds.

---

## 1. Input

**Nothing was re-collected.**

- **The pair book's store** (`/var/lib/btc-pairbook/`): read only, by the instrument alone.
  - `window.json` of the 936 candidates `1791706500` … `1792548000`, by `fetch`.
  - `window.json` and `books.jsonl.gz` of the 768 members by `score` (first run), and of the 48 rescored members by `rescore`.
  - No stream file was opened and nothing was listed.
- **The streams**: downloaded anonymously from the archive's Release assets under `User-Agent: btc-5m-twap-tz30`. Each was verified by its set's bytes and SHA-256 and removed after its replay.
  - `rehearse`: 51 assets of TZ-27's Release, `678,739,504` bytes.
  - `score`: 768 assets, `15,337,505,351` bytes.
  - `rescore`: 48 assets, `961,101,669` bytes.
  - Retries `0` in all three; no stream file remains on the host.
- **The recorder's `twap60`**: the two interval files `btc-updown-5m/<T>` and `btc-updown-5m/<T+600>` of the candidates walked, read by `strikes` alone, twice.
- **The venue's documents**: through gamma `/markets` by TZ-24's `http_json`.
  - `rehearse`: 6 document requests for TZ-27's 51 windows.
  - `fetch`: 94 document requests for the 936 candidates, cached in `fetch/docs/` (94 files).
- **The archive's state**: `ledger.jsonl` (40,441 bytes, SHA-256 `40c413bbad353da5eddc7b8e4766bb9ec808474bea89f2257c2cf2c910798e3e`, 170 complete records) and every complete run's `set.json`, by `archive` and `fetch`; the ledger alone by `still`.
- **The forensic store**: TZ-27's `set.json`, `ec71b1a7…`, read by `rehearse` and §0.3.
- No member's price was read before 03:33:15Z, the first `score` ledger line. The two document walks and the strikes ran before it, under §2 item 8's exemptions (a) and (b).

---

## 2. Measurements

### 2.1 The candidates and the set

`I fetch` (`logs/17-fetch.log`):

```
[2026-10-22T03:32:32Z] MemAvailable 235171840 bytes, floor 116711424; free 12460699648 bytes, floor 4800000000
[2026-10-22T03:32:33Z] the archive has moved windows to 1792636200, at or after 1792548000, after 0 s waited
[2026-10-22T03:32:33Z] the walk starts at second 153 of window 1792639800 after 0 s held; 936 candidates 1791706500 to 1792548000
[2026-10-22T03:32:34Z] projected 8 s for 94 document requests after 20
[2026-10-22T03:32:41Z] the set formed in 8.1 s: 936 considered, 932 members, 94 document requests, /root/tz30-work/fetch/set.json sha256 3b7dd4140eae89e1d88c5d450e7d67c87f5568a44963f7afc08afa5649ca04b4
[2026-10-22T03:32:41Z] wrote /root/tz30-work/fetch/candidates.json 224756 bytes sha256 939f9b9863653b33135c417af391e1cac2130e2f2722903a738accbf2d73cfdc
[2026-10-22T03:32:41Z] FETCH: 936 windows considered, 1791706500 to 1792548000; by status {"5m document: readings": 1, "candidate": 931, "incomplete": 3, "stream: subscribed late": 1}
[2026-10-22T03:32:41Z] peak memory of this run: 59604992 bytes
[2026-10-22T03:32:41Z] refused: 0 by this file's hook, 0 by TZ-24's
exit=0
```

The archive had already moved every window to `1792636200` (17 complete runs), so `fetch` waited **0 s**.

`I strikes`, first run (`logs/18-strikes-1.log`):

```
[2026-10-22T03:32:48Z] MemAvailable 242438144 bytes, floor 116711424; free 12459044864 bytes, floor 4800000000
[2026-10-22T03:33:00Z] wrote /root/tz30-work/b3-set.json 880811 bytes sha256 df4ae686b06a24d461e554e0fbbe36192619b1404550204b65513cb85dd965d9
[2026-10-22T03:33:00Z] G-SET PASS: 768 members of 775 considered, 1791706500 to 1792403100, member list sha256 4d4a7f5f6397b63b945c0a85f8457e1cd3701a4754b5c1b3252904b1647bb9de, /root/tz30-work/b3-set.json sha256 df4ae686b06a24d461e554e0fbbe36192619b1404550204b65513cb85dd965d9
[2026-10-22T03:33:00Z] block 1: 96 members, 1791706500 (2026-10-11T08:15:00Z) to 1791792000 (2026-10-12T08:00:00Z)
[2026-10-22T03:33:00Z] block 2: 96 members, 1791792900 (2026-10-12T08:15:00Z) to 1791880200 (2026-10-13T08:30:00Z)
[2026-10-22T03:33:00Z] block 3: 96 members, 1791881100 (2026-10-13T08:45:00Z) to 1791967500 (2026-10-14T08:45:00Z)
[2026-10-22T03:33:00Z] block 4: 96 members, 1791968400 (2026-10-14T09:00:00Z) to 1792054800 (2026-10-15T09:00:00Z)
[2026-10-22T03:33:00Z] block 5: 96 members, 1792055700 (2026-10-15T09:15:00Z) to 1792142100 (2026-10-16T09:15:00Z)
[2026-10-22T03:33:00Z] block 6: 96 members, 1792143000 (2026-10-16T09:30:00Z) to 1792229400 (2026-10-17T09:30:00Z)
[2026-10-22T03:33:00Z] block 7: 96 members, 1792230300 (2026-10-17T09:45:00Z) to 1792316700 (2026-10-18T09:45:00Z)
[2026-10-22T03:33:00Z] block 8: 96 members, 1792317600 (2026-10-18T10:00:00Z) to 1792403100 (2026-10-19T09:45:00Z)
[2026-10-22T03:33:00Z] non-members 7: [[1791865800, "strike: published 28000 ms after 1791865800"], [1791879300, "incomplete"], [1791890100, "strike: published 7000 ms after 1791890100"], [1791977400, "incomplete"], [1792095300, "incomplete"], [1792161000, "stream: subscribed late"], [1792315800, "strike: published 6000 ms after 1792316400"]]
[2026-10-22T03:33:00Z] members by weekday {"Fri": 95, "Mon": 136, "Sat": 96, "Sun": 158, "Thu": 95, "Tue": 93, "Wed": 95}; pair A 379, B 389 by D_hat
[2026-10-22T03:33:00Z] barred: the sign of D_hat agrees with D's at 768 of 768; |D_hat - D| median 0.000000000005246336, max 1.197922565060434816 USD; the strike at T + 600 received a median 1560 ms, at most 2771 ms, after its publication
[2026-10-22T03:33:00Z] each answer's false-reading probability 0.00390625 under independent blocks; power {"0.90": "0.4304672100000000", "0.95": "0.6634204312890625", "0.99": "0.9227446944279201"}
[2026-10-22T03:33:00Z] peak memory of this run: 37699584 bytes
[2026-10-22T03:33:00Z] refused: 0 by this file's hook, 0 by TZ-24's
exit=0
```

The second run (`logs/19-strikes-2.log`) printed `unchanged /root/tz30-work/b3-set.json sha256 df4ae686…`. Every other finding line was identical; only the `MemAvailable`/free read and the peak memory differ.

**Every non-member, with its reason, counted by rule.** The walk stopped at the 768th member, `1792403100`, after 775 candidates.

| rule | count | windows |
|---|---|---|
| (a) TZ-24's set rule — `window.json` `incomplete` | 3 | `1791879300`, `1791977400`, `1792095300` |
| (b) the stream — `subscribed late` | 1 | `1792161000` |
| (c) the order size | 0 | — |
| (d) the strikes — published more than 2 s after the boundary | 3 | `1791865800` (28,000 ms after `1791865800`), `1791890100` (7,000 ms after `1791890100`), `1792315800` (6,000 ms after `1792316400`) |
| (d) `D̂` zero | 0 | — |

After the 768th member, `fetch` read `1792433700` as `5m document: readings`, a rule (a) failure. `strikes` never considered it.

**Members by weekday:** Mon 136, Tue 93, Wed 95, Thu 95, Fri 95, Sat 96, Sun 158. **By pair**, by `D̂`'s sign: A 379, B 389. The member list is not the all-qualify list, whose `02fb856a…` is asserted by nothing, because seven candidates failed.

### 2.2 G-REBUILD

```
G-REBUILD PASS: stored replies 21504, valid 10752, compared 10693 (0.994512648810 of valid), equal at the touch 10688 (0.999532404377 of compared), every level equal 9836; not compared: unseeded 59, unresolved 0
```

**Stored replies unequal to the rebuilt book at the touch, by member and instant** (from the unit files' `unequal_ms`), five in four members:

| member `T` | reply timestamp, ms | second of window |
|---|---|---|
| `1791725400` | `1791726115036` | `T + 715.036` |
| `1791909000` | `1791909805032` | `T + 805.032` |
| `1792008000` | `1792008885027` | `T + 885.027` |
| `1792400400` | `1792401235032` | `T + 835.032` |
| `1792400400` | `1792401265030` | `T + 865.030` |

The 59 unseeded replies fall in 27 members: `1792067400`, `1792077300` and `1792164600` have 4 each; `1791867600` has 1; the other 23 have 2 each. No valid reply was unresolved, and no leg reply failed `line_check` (`bad {}` at all 768).

### 2.3 The lag

```
the capture's lag, a price_change frame's host receipt less its venue stamp, over 768 members and 180454126 frames: the median member's median 17 ms; its 99th percentile 150 ms at the median member and 25059 ms at the worst, above 1,000 ms at 117 members; the longest 28325 ms, the least 3 ms
```

### 2.4 The reading and the barred diagnostics — `logs/20-score-1.log`, verbatim

```
[2026-10-22T03:33:15Z] MemAvailable 260354048 bytes, floor 116711424; free 12458053632 bytes, floor 4800000000
[2026-10-22T03:33:15Z] units to replay 768, 15337505351 bytes of streams in all
[2026-10-22T03:34:27Z] projected 1778 s of replay for 15337505351 bytes after 24 units at 0.1160 s a megabyte
[2026-10-22T03:34:27Z] units 24 this run, 71 s
[2026-10-22T03:35:34Z] units 48 this run, 139 s
[2026-10-22T03:36:52Z] units 72 this run, 217 s
[2026-10-22T03:38:14Z] units 96 this run, 298 s
[2026-10-22T03:46:01Z] units 120 this run, 765 s
[2026-10-22T03:47:25Z] units 144 this run, 850 s
[2026-10-22T03:48:49Z] units 168 this run, 934 s
[2026-10-22T03:50:29Z] units 192 this run, 1034 s
[2026-10-22T03:52:04Z] units 216 this run, 1128 s
[2026-10-22T03:53:28Z] units 240 this run, 1212 s
[2026-10-22T04:01:00Z] units 264 this run, 1665 s
[2026-10-22T04:02:23Z] units 288 this run, 1747 s
[2026-10-22T04:03:57Z] units 312 this run, 1842 s
[2026-10-22T04:05:32Z] units 336 this run, 1936 s
[2026-10-22T04:06:57Z] units 360 this run, 2022 s
[2026-10-22T04:08:36Z] units 384 this run, 2121 s
[2026-10-22T04:16:31Z] units 408 this run, 2596 s
[2026-10-22T04:17:58Z] units 432 this run, 2683 s
[2026-10-22T04:19:26Z] units 456 this run, 2771 s
[2026-10-22T04:20:55Z] units 480 this run, 2859 s
[2026-10-22T04:22:23Z] units 504 this run, 2947 s
[2026-10-22T04:23:49Z] units 528 this run, 3033 s
[2026-10-22T04:31:31Z] units 552 this run, 3495 s
[2026-10-22T04:32:46Z] units 576 this run, 3570 s
[2026-10-22T04:33:57Z] units 600 this run, 3642 s
[2026-10-22T04:35:10Z] units 624 this run, 3714 s
[2026-10-22T04:36:14Z] units 648 this run, 3778 s
[2026-10-22T04:37:18Z] units 672 this run, 3843 s
[2026-10-22T04:38:33Z] units 696 this run, 3917 s
[2026-10-22T04:46:04Z] units 720 this run, 4368 s
[2026-10-22T04:47:29Z] units 744 this run, 4453 s
[2026-10-22T04:48:52Z] units 768 this run, 4537 s
[2026-10-22T04:48:52Z] units 768: inside the idle stretch 768, ending after second 590 0; longest 7.5 s, download 3.5 s and replay 4.9 s at most; 1892 s waited; 15337505351 bytes downloaded; retries 0; windows 2026-10-22T03:30:00Z to 2026-10-22T04:45:00Z
[2026-10-22T04:48:52Z] wrote /root/tz30-work/score/b3-windows.txt 2226927 bytes sha256 ecf3ce88e9f7ebe17dd0bf5bf2947e379b734508e2a88d45b7d2a507a24750d5
[2026-10-22T04:48:52Z] G-REBUILD PASS: stored replies 21504, valid 10752, compared 10693 (0.994512648810 of valid), equal at the touch 10688 (0.999532404377 of compared), every level equal 9836; not compared: unseeded 59, unresolved 0
[2026-10-22T04:48:52Z] the capture's lag, a price_change frame's host receipt less its venue stamp, over 768 members and 180454126 frames: the median member's median 17 ms; its 99th percentile 150 ms at the median member and 25059 ms at the worst, above 1,000 ms at 117 members; the longest 28325 ms, the least 3 ms
[2026-10-22T04:48:52Z] block 1: 1791706500 to 1791792000, S -67.382523204295 USDC, below theta 10
[2026-10-22T04:48:52Z] block 2: 1791792900 to 1791880200, S -28.096568278984 USDC, below theta 10
[2026-10-22T04:48:52Z] block 3: 1791881100 to 1791967500, S -3.846111778517 USDC, below theta 10
[2026-10-22T04:48:52Z] block 4: 1791968400 to 1792054800, S -258.297909224847 USDC, below theta 10
[2026-10-22T04:48:52Z] block 5: 1792055700 to 1792142100, S -58.149298476613 USDC, below theta 10
[2026-10-22T04:48:52Z] block 6: 1792143000 to 1792229400, S -46.663873186684 USDC, below theta 10
[2026-10-22T04:48:52Z] block 7: 1792230300 to 1792316700, S -131.702127989504 USDC, below theta 10
[2026-10-22T04:48:52Z] block 8: 1792317600 to 1792403100, S -1.916692656212 USDC, below theta 10
[2026-10-22T04:48:52Z] barred: primary  attempts 532, void 2, windows with an attempt 75; shares sought 31574.095097000000, bought matched 11100.473833300000, excess 14828.703265700000 of which sold 14281.950837900000, held 546.752427800000; the touch's ceiling 666.783691791697; P&L -596.055104795655 USDC, with the band's bonus -584.071904795655
[2026-10-22T04:48:52Z] barred: L0       attempts 624, void 2, windows with an attempt 75; shares sought 43396.046883100000, bought matched 18965.015060400000, excess 18031.649743900000 of which sold 17821.332870900000, held 210.316873000000; the touch's ceiling 928.842721829865; P&L -774.236991254665 USDC, with the band's bonus -762.253791254665
[2026-10-22T04:48:52Z] barred: L25      attempts 571, void 2, windows with an attempt 75; shares sought 39267.476251700000, bought matched 14668.759230300000, excess 17886.808737400000 of which sold 17386.821245900000, held 499.987491500000; the touch's ceiling 809.194115796783; P&L -815.840099391103 USDC, with the band's bonus -803.856899391103
[2026-10-22T04:48:52Z] barred: L100     attempts 475, void 3, windows with an attempt 75; shares sought 26944.838008500000, bought matched 8563.390356200000, excess 13019.733522400000 of which sold 12500.377895000000, held 519.355627400000; the touch's ceiling 667.295256296329; P&L -649.220716387664 USDC, with the band's bonus -649.220716387664
[2026-10-22T04:48:52Z] barred: L250     attempts 405, void 3, windows with an attempt 75; shares sought 21605.540956400000, bought matched 4960.402398900000, excess 9979.909440800000 of which sold 8864.364096500000, held 1115.545344300000; the touch's ceiling 388.338964154820; P&L -358.523981752534 USDC, with the band's bonus -358.523981752534
[2026-10-22T04:48:52Z] barred: nodelay  attempts 735, void 2, windows with an attempt 75; shares sought 52693.344573500000, bought matched 30041.555744900000, excess 17620.953171100000 of which sold 17153.190263000000, held 467.762908100000; the touch's ceiling 1212.126443640871; P&L -354.493952303515 USDC, with the band's bonus -330.515792303515
[2026-10-22T04:48:52Z] barred: top      attempts 576, void 2, windows with an attempt 75; shares sought 32620.740000000000, bought matched 11529.120000000000, excess 15340.630000000000 of which sold 14805.070000000000, held 535.560000000000; the touch's ceiling 678.280633987100; P&L -533.206685551300 USDC, with the band's bonus -521.206685551300
[2026-10-22T04:48:52Z] barred: block 1 without its most influential member 1791727200 (-40.063412847868 USDC): S -27.319110356427, its side holds
[2026-10-22T04:48:52Z] barred: block 2 without its most influential member 1791873000 (-22.479719632689 USDC): S -5.616848646294, its side holds
[2026-10-22T04:48:52Z] barred: block 3 without its most influential member 1791912600 (-2.267535860068 USDC): S -1.578575918449, its side holds
[2026-10-22T04:48:52Z] barred: block 4 without its most influential member 1792020600 (-254.530357633639 USDC): S -3.767551591208, its side holds
[2026-10-22T04:48:52Z] barred: block 5 without its most influential member 1792116900 (-35.537037773921 USDC): S -22.612260702692, its side holds
[2026-10-22T04:48:52Z] barred: block 6 without its most influential member 1792190700 (-33.940892584783 USDC): S -12.722980601901, its side holds
[2026-10-22T04:48:52Z] barred: block 7 without its most influential member 1792262700 (-71.533007177415 USDC): S -60.169120812089, its side holds
[2026-10-22T04:48:52Z] barred: block 8 without its most influential member 1792361700 (-0.738107285191 USDC): S -1.178585371020, its side holds
[2026-10-22T04:48:52Z] barred: primary's excess held to settlement instead of sold: P&L 587.493173291511 USDC
[2026-10-22T04:48:52Z] barred: the reading with each block's most influential member removed: NO CAPTURE
[2026-10-22T04:48:52Z] barred: per member P&L min -254.530357633639, median 0.000000000000, max 8.587502890290; members above zero 18, below 55, at zero 695
[2026-10-22T04:48:52Z] wrote /root/tz30-work/score/b3-reading.json 5079 bytes sha256 181de4d449d507d31d8a224eb53adeadcbc4ccddfd1a831d05cf306b3746d2a0
[2026-10-22T04:48:52Z] B3 READING: NO CAPTURE
[2026-10-22T04:48:52Z] peak memory of this run: 60055552 bytes
[2026-10-22T04:48:52Z] refused: 0 by this file's hook, 0 by TZ-24's
exit=0
```

The second `score` (`logs/21-score-2.log`) replayed nothing. It printed `unchanged` for `score/b3-windows.txt` (`ecf3ce88e9f7ebe17dd0bf5bf2947e379b734508e2a88d45b7d2a507a24750d5`) and for `score/b3-reading.json` (`181de4d449d507d31d8a224eb53adeadcbc4ccddfd1a831d05cf306b3746d2a0`). Every block, barred, G-REBUILD and lag line was byte-identical to the first run's.

**The barred diagnostics, summarized from the lines above. They gate nothing.**

- All seven variants lose:
  - primary: 532 attempts in 75 windows, `−596.055` USDC.
  - `L0`: `−774.237`.
  - `L25`: `−815.840`.
  - `L100`: `−649.221`.
  - `L250`: `−358.524`.
  - `nodelay`: `−354.494`.
  - `top`: `−533.207`.
- The touch's ceiling at detection is `666.784` USDC for the primary.
- With the band's bonus, the primary reads `−584.072`.
- With the primary's excess held to settlement instead of sold, it reads `+587.493` USDC. That is direction, which the rule bars.
- Without each block's most influential member, every side holds, and the reading stays NO CAPTURE.
- Per member: minimum `−254.530357633639` (member `1792020600`, block 4), median `0`, maximum `8.587502890290`. 18 members above zero, 55 below, 695 at zero.

### 2.5 G-REHEARSAL — `logs/16-rehearse.log`, verbatim

```
[2026-10-22T03:25:14Z] MemAvailable 311447552 bytes, floor 116711424; free 12489986048 bytes, floor 4800000000
[2026-10-22T03:30:15Z] the set formed in 0.6 s: 51 considered, 51 members, 6 document requests, /root/tz30-work/rehearsal/set.json sha256 3724aa5df21b8589949c84fc60ad35a1319c1ec1f85d2a957e7adf5e4385c11c
[2026-10-22T03:32:24Z] units 51: inside the idle stretch 51, ending after second 590 0; longest 4.9 s, download 2.3 s and replay 3.7 s at most; 0 s waited; 678739504 bytes downloaded; retries 0; windows 2026-10-22T03:30:00Z to 2026-10-22T03:30:00Z
[2026-10-22T03:32:24Z] wrote /root/tz30-work/rehearsal/rehearsal-lines.txt 55392 bytes sha256 402b378a274613153410aa068abaaa798d68d4770a22239a07442ba42411bade
[2026-10-22T03:32:24Z] G-REHEARSAL L0       attempts 139, pnl -23.646658648482; the Architect's [139, '-23.646658648482']
[2026-10-22T03:32:24Z] G-REHEARSAL L100     attempts 113, pnl -117.369164961585; the Architect's [113, '-117.369164961585']
[2026-10-22T03:32:24Z] G-REHEARSAL L25      attempts 132, pnl -50.344323117306; the Architect's [132, '-50.344323117306']
[2026-10-22T03:32:24Z] G-REHEARSAL L250     attempts 91, pnl -169.125533904780; the Architect's [91, '-169.125533904780']
[2026-10-22T03:32:24Z] G-REHEARSAL nodelay  attempts 166, pnl -0.893613644133; the Architect's [166, '-0.893613644133']
[2026-10-22T03:32:24Z] G-REHEARSAL primary  attempts 125, pnl -95.936018771005; the Architect's [125, '-95.936018771005']
[2026-10-22T03:32:24Z] G-REHEARSAL top      attempts 143, pnl -100.148749740000; the Architect's [143, '-100.148749740000']
[2026-10-22T03:32:24Z] G-REHEARSAL lines 357, the Architect's 357; sha256 402b378a274613153410aa068abaaa798d68d4770a22239a07442ba42411bade, the Architect's 402b378a274613153410aa068abaaa798d68d4770a22239a07442ba42411bade
[2026-10-22T03:32:24Z] G-REHEARSAL PASS: 9 of 9 - 357 lines byte for byte and 7 variants' totals equal to the Architect's
[2026-10-22T03:32:24Z] peak memory of this run: 56459264 bytes
[2026-10-22T03:32:24Z] refused: 0 by this file's hook, 0 by TZ-24's
exit=0
```

The walk was held from 03:25:14 to 03:30:15 UTC to the idle stretch. Its six document requests formed all 51 members.

### 2.6 DETERMINISM — `logs/22-rescore.log`, verbatim

```
[2026-10-22T04:49:09Z] MemAvailable 258691072 bytes, floor 116711424; free 12338012160 bytes, floor 4800000000
[2026-10-22T04:49:09Z] units to replay 48, 961101669 bytes of streams in all
[2026-10-22T04:50:21Z] projected 102 s of replay for 961101669 bytes after 24 units at 0.1061 s a megabyte
[2026-10-22T04:50:21Z] units 24 this run, 72 s
[2026-10-22T04:51:33Z] units 48 this run, 144 s
[2026-10-22T04:51:33Z] units 48: inside the idle stretch 48, ending after second 590 0; longest 6.5 s, download 2.1 s and replay 5.8 s at most; 0 s waited; 961101669 bytes downloaded; retries 0; windows 2026-10-22T04:45:00Z to 2026-10-22T04:45:00Z
[2026-10-22T04:51:33Z] DETERMINISM PASS: 48 of 48 members' unit files byte for byte the score's
[2026-10-22T04:51:33Z] peak memory of this run: 59305984 bytes
[2026-10-22T04:51:33Z] refused: 0 by this file's hook, 0 by TZ-24's
exit=0
```

### 2.7 The units' clock

| mode | timing summary, as printed |
|---|---|
| `16-rehearse` | `units 51: inside the idle stretch 51, ending after second 590 0; longest 4.9 s, download 2.3 s and replay 3.7 s at most; 0 s waited; 678739504 bytes downloaded; retries 0; windows 2026-10-22T03:30:00Z to 2026-10-22T03:30:00Z` |
| `20-score-1` | `units 768: inside the idle stretch 768, ending after second 590 0; longest 7.5 s, download 3.5 s and replay 4.9 s at most; 1892 s waited; 15337505351 bytes downloaded; retries 0; windows 2026-10-22T03:30:00Z to 2026-10-22T04:45:00Z` |
| `22-rescore` | `units 48: inside the idle stretch 48, ending after second 590 0; longest 6.5 s, download 2.1 s and replay 5.8 s at most; 0 s waited; 961101669 bytes downloaded; retries 0; windows 2026-10-22T04:45:00Z to 2026-10-22T04:45:00Z` |

**Every unit ended inside the idle stretch.** 0 of 867 ended after second 590, so none is listed. Downloads needed no retries. The score's projection after 24 units was `1778 s of replay for 15337505351 bytes … at 0.1160 s a megabyte` (bound `3,190`). The rescore's was `102 s … at 0.1061 s a megabyte` (bound `210`). The walk's was `8 s for 94 document requests after 20` (bound `120`).

### 2.8 The archive's record — G-ASSETS

`I archive` at §3.4 printed the following, in full (`logs/15-archive-1.log`, SHA-256 `7a95c9c97df1de1f2e0c39e4393d8252935e541cfc7bd401220bcb290325f546`):

<details><summary>214 lines — every complete ledger record, every run, every set, the tags and G-ASSETS</summary>

```
[2026-10-22T03:25:09Z] btc-pairbook-archive.timer {'NextElapseUSecRealtime': 'Fri 2026-10-23 03:00:20 UTC', 'LastTriggerUSec': 'Thu 2026-10-22 03:00:20 UTC', 'Result': 'success', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-10-22T03:25:09Z] btc-pairbook-archive.service {'Result': 'success', 'ExecMainStatus': '0', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-10-22T03:25:09Z] ledger /var/lib/btc-pairbook-archive/ledger.jsonl: 40441 bytes sha256 40c413bbad353da5eddc7b8e4766bb9ec808474bea89f2257c2cf2c910798e3e, 170 complete records, 0 bytes of a line still written
[2026-10-22T03:25:09Z] L 2026-10-11T15:18:12Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "2a4b998acb9f4883b26999bb278624bf", "phase_at": 192, "resumed": false, "run": 1791731892, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1791731892810556801}
[2026-10-22T03:25:09Z] L 2026-10-11T15:18:13Z {"assets_n": 28, "bytes_total": 430047476, "closed": 79, "deferred": 0, "event": "set", "first_T": 1791706500, "last_T": 1791730800, "open": 0, "run": 1791731892, "sha256": "ec3983419485fa67317468917eb7b60e2d0e529be4334c7297831ff562471ad0", "tag": "pairbook-streams-1791731892", "unclosed": 0, "wall_ns": 1791731893762719408, "windows_considered": 79}
[2026-10-22T03:25:09Z] L 2026-10-11T15:18:57Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 409746510, "run": 1791731892, "sent": 28, "wall_ns": 1791731937181037882}
[2026-10-22T03:25:09Z] L 2026-10-11T15:21:30Z {"assets_n": 28, "bytes_total": 430047476, "event": "verify", "release_id": 409746510, "run": 1791731892, "verify_sha256": "032adfdbaea0b81d7ea5063eb43130c09396908f05d74be0f1818d2bb2342f64", "wall_ns": 1791732090814504593}
[2026-10-22T03:25:09Z] L 2026-10-11T15:21:31Z {"already": 0, "event": "delete", "free_after": 12969091072, "free_before": 12538937344, "freed": 430047476, "gone": 28, "removed": 28, "run": 1791731892, "wall_ns": 1791732091732399708, "windows_kept": 28}
[2026-10-22T03:25:09Z] L 2026-10-11T15:21:31Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "815823", "NRestarts": "2", "ns": 1791732091741955625}, "phase": 391, "run": 1791731892, "wall_ns": 1791732091741960838}
[2026-10-22T03:25:09Z] L 2026-10-11T15:21:31Z {"event": "kill", "exit": 0, "phase": 391, "run": 1791731892, "wall_ns": 1791732091746593097}
[2026-10-22T03:25:09Z] L 2026-10-11T15:22:01Z {"NRestarts": "3", "W": 1791731700, "event": "restart", "free_bytes": 12969062400, "gap_ns": 5548461176, "pid": 851381, "run": 1791731892, "stopped": 815823, "stream_bytes": 0, "wall_ns": 1791732121761569347}
[2026-10-22T03:25:09Z] L 2026-10-11T15:30:41Z {"T": 1791731700, "event": "resume", "reading": "PASS", "run": 1791731892, "wall_ns": 1791732641000772037}
[2026-10-22T03:25:09Z] L 2026-10-11T15:30:41Z {"assets_n": 28, "bytes_total": 430047476, "ended_outside": 0, "event": "complete", "free_bytes": 12949487616, "peak_rss": 36884480, "rate_per_day": 1474448489, "requests": 61, "run": 1791731892, "started_outside": 0, "stops": [["the cap", 1792200292], ["the floor, base 43500000 bytes a day", 1792213576], ["the floor, base 187760570 bytes a day", 1792171837]], "store_stream_bytes": 19346486, "wall_ns": 1791732641002785194}
[2026-10-22T03:25:09Z] L 2026-10-12T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "b458725447bd4a0c865999eab0a904ad", "phase_at": 20, "resumed": false, "run": 1791774020, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1791774020508107799}
[2026-10-22T03:25:09Z] L 2026-10-12T03:00:22Z {"assets_n": 46, "bytes_total": 794522712, "closed": 125, "deferred": 0, "event": "set", "first_T": 1791731700, "last_T": 1791772200, "open": 1, "run": 1791774020, "sha256": "c8f02de3fbed47c4cfa91e66d774427f20990f634d271237bf3c6f25887ffb99", "tag": "pairbook-streams-1791774020", "unclosed": 0, "wall_ns": 1791774022193879442, "windows_considered": 125}
[2026-10-22T03:25:09Z] L 2026-10-12T03:01:35Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 410101186, "run": 1791774020, "sent": 46, "wall_ns": 1791774095014644950}
[2026-10-22T03:25:09Z] L 2026-10-12T03:04:44Z {"assets_n": 46, "bytes_total": 794522712, "event": "verify", "release_id": 410101186, "run": 1791774020, "verify_sha256": "0f86d9494743193ae4dd5ddb59e37a08eebc8bb7318ea4d98def44406d025aec", "wall_ns": 1791774284631917592}
[2026-10-22T03:25:09Z] L 2026-10-12T03:04:46Z {"already": 0, "event": "delete", "free_after": 12960145408, "free_before": 12165431296, "freed": 794522712, "gone": 46, "removed": 46, "run": 1791774020, "wall_ns": 1791774286328338970, "windows_kept": 46}
[2026-10-22T03:25:09Z] L 2026-10-12T03:04:46Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "851381", "NRestarts": "3", "ns": 1791774286341020683}, "phase": 286, "run": 1791774020, "wall_ns": 1791774286341025663}
[2026-10-22T03:25:09Z] L 2026-10-12T03:04:46Z {"event": "kill", "exit": 0, "phase": 286, "run": 1791774020, "wall_ns": 1791774286345765034}
[2026-10-22T03:25:09Z] L 2026-10-12T03:05:16Z {"NRestarts": "4", "W": 1791774000, "event": "restart", "free_bytes": 12960112640, "gap_ns": 5455854888, "pid": 911226, "run": 1791774020, "stopped": 851381, "stream_bytes": 25646773, "wall_ns": 1791774316361306454}
[2026-10-22T03:25:09Z] L 2026-10-12T03:15:41Z {"T": 1791774000, "event": "resume", "reading": "PASS", "run": 1791774020, "wall_ns": 1791774941000362333}
[2026-10-22T03:25:09Z] L 2026-10-12T03:15:41Z {"assets_n": 46, "bytes_total": 794522712, "ended_outside": 0, "event": "complete", "free_bytes": 12948570112, "peak_rss": 37670912, "rate_per_day": 1658134355, "requests": 97, "run": 1791774020, "started_outside": 0, "stops": [["the cap", 1792189855], ["the floor, base 43500000 bytes a day", 1792203914], ["the floor, base 187760570 bytes a day", 1792170389]], "store_stream_bytes": 37220758, "wall_ns": 1791774941002570067}
[2026-10-22T03:25:09Z] L 2026-10-13T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "5e59db817b3d42ef91641fbb34bc17cc", "phase_at": 20, "resumed": false, "run": 1791860420, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1791860420531436360}
[2026-10-22T03:25:09Z] L 2026-10-13T03:00:24Z {"assets_n": 96, "bytes_total": 1925987888, "closed": 221, "deferred": 0, "event": "set", "first_T": 1791773100, "last_T": 1791858600, "open": 1, "run": 1791860420, "sha256": "de9209f2e76e5c42bd1395ea6e9c17ab0fc4c497be6a9311cd1e07c101f9b777", "tag": "pairbook-streams-1791860420", "unclosed": 0, "wall_ns": 1791860424671646762, "windows_considered": 221}
[2026-10-22T03:25:09Z] L 2026-10-13T03:03:13Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 411210796, "run": 1791860420, "sent": 96, "wall_ns": 1791860593421247948}
[2026-10-22T03:25:09Z] L 2026-10-13T03:07:31Z {"assets_n": 96, "bytes_total": 1925987888, "event": "verify", "release_id": 411210796, "run": 1791860420, "verify_sha256": "a5969978f8bfb614451c41257e7eb70a13c12126932ef03d4cfbd2f2c41ad022", "wall_ns": 1791860851109946296}
[2026-10-22T03:25:09Z] L 2026-10-13T03:07:35Z {"already": 0, "event": "delete", "free_after": 12876316672, "free_before": 10949902336, "freed": 1925987888, "gone": 96, "removed": 96, "run": 1791860420, "wall_ns": 1791860855219206873, "windows_kept": 96}
[2026-10-22T03:25:09Z] L 2026-10-13T03:07:35Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "911226", "NRestarts": "4", "ns": 1791860855230756130}, "phase": 455, "run": 1791860420, "wall_ns": 1791860855230762191}
[2026-10-22T03:25:09Z] L 2026-10-13T03:07:35Z {"event": "kill", "exit": 0, "phase": 455, "run": 1791860420, "wall_ns": 1791860855235973960}
[2026-10-22T03:25:09Z] L 2026-10-13T03:08:05Z {"NRestarts": "5", "W": 1791860400, "event": "restart", "free_bytes": 12876300288, "gap_ns": 5561093708, "pid": 1027378, "run": 1791860420, "stopped": 911226, "stream_bytes": 23131514, "wall_ns": 1791860885252051875}
[2026-10-22T03:25:09Z] L 2026-10-13T03:15:41Z {"T": 1791860400, "event": "resume", "reading": "PASS", "run": 1791860420, "wall_ns": 1791861341000349433}
[2026-10-22T03:25:09Z] L 2026-10-13T03:15:41Z {"assets_n": 96, "bytes_total": 1925987888, "ended_outside": 0, "event": "complete", "free_bytes": 12857700352, "peak_rss": 37941248, "rate_per_day": 1925987888, "requests": 197, "run": 1791860420, "started_outside": 0, "stops": [["the cap", 1792218357], ["the floor, base 43500000 bytes a day", 1792227987], ["the floor, base 187760570 bytes a day", 1792202964]], "store_stream_bytes": 41556131, "wall_ns": 1791861341004126797}
[2026-10-22T03:25:09Z] L 2026-10-14T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "f4f5335f60584baeab0eabd568d20823", "phase_at": 20, "resumed": false, "run": 1791946820, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1791946820511249708}
[2026-10-22T03:25:09Z] L 2026-10-14T03:00:24Z {"assets_n": 96, "bytes_total": 2039544263, "closed": 317, "deferred": 0, "event": "set", "first_T": 1791859500, "last_T": 1791945000, "open": 1, "run": 1791946820, "sha256": "9c78ba5221e0bc8d9d8699d920e17c58d76b6052fce7c0e86af4948bdc38aa1e", "tag": "pairbook-streams-1791946820", "unclosed": 0, "wall_ns": 1791946824807088559, "windows_considered": 317}
[2026-10-22T03:25:09Z] L 2026-10-14T03:03:21Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 412296623, "run": 1791946820, "sent": 96, "wall_ns": 1791947001852058175}
[2026-10-22T03:25:09Z] L 2026-10-14T03:07:45Z {"assets_n": 96, "bytes_total": 2039544263, "event": "verify", "release_id": 412296623, "run": 1791946820, "verify_sha256": "086fc6331ec202ef5c6b56257a52cbc12673053f82408a3cd4b3cf203ae44c95", "wall_ns": 1791947265299596860}
[2026-10-22T03:25:09Z] L 2026-10-14T03:07:49Z {"already": 0, "event": "delete", "free_after": 12842123264, "free_before": 10802130944, "freed": 2039544263, "gone": 96, "removed": 96, "run": 1791946820, "wall_ns": 1791947269716703785, "windows_kept": 96}
[2026-10-22T03:25:09Z] L 2026-10-14T03:07:49Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1027378", "NRestarts": "5", "ns": 1791947269728675162}, "phase": 469, "run": 1791946820, "wall_ns": 1791947269728680763}
[2026-10-22T03:25:09Z] L 2026-10-14T03:07:49Z {"event": "kill", "exit": 0, "phase": 469, "run": 1791946820, "wall_ns": 1791947269733842747}
[2026-10-22T03:25:09Z] L 2026-10-14T03:08:19Z {"NRestarts": "6", "W": 1791946800, "event": "restart", "free_bytes": 12842098688, "gap_ns": 5560847791, "pid": 1155982, "run": 1791946820, "stopped": 1027378, "stream_bytes": 17222124, "wall_ns": 1791947299751305660}
[2026-10-22T03:25:09Z] L 2026-10-14T03:15:41Z {"T": 1791946800, "event": "resume", "reading": "PASS", "run": 1791946820, "wall_ns": 1791947741000324294}
[2026-10-22T03:25:09Z] L 2026-10-14T03:15:41Z {"assets_n": 96, "bytes_total": 2039544263, "ended_outside": 0, "event": "complete", "free_bytes": 12820799488, "peak_rss": 38072320, "rate_per_day": 2039544263, "requests": 197, "run": 1791946820, "started_outside": 0, "stops": [["the cap", 1792285007], ["the floor, base 43500000 bytes a day", 1792292869], ["the floor, base 187760570 bytes a day", 1792270515]], "store_stream_bytes": 38533208, "wall_ns": 1791947741004939814}
[2026-10-22T03:25:09Z] L 2026-10-15T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "08fd4972db8347a4897a6ecd018049e4", "phase_at": 20, "resumed": false, "run": 1792033220, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792033220507675615}
[2026-10-22T03:25:09Z] L 2026-10-15T03:00:25Z {"assets_n": 96, "bytes_total": 2103892072, "closed": 413, "deferred": 0, "event": "set", "first_T": 1791945900, "last_T": 1792031400, "open": 1, "run": 1792033220, "sha256": "3272c87234da82333365144d0c39bb0f75e895943e7e34ec7ff1e559c1ad8715", "tag": "pairbook-streams-1792033220", "unclosed": 0, "wall_ns": 1792033225025238523, "windows_considered": 413}
[2026-10-22T03:25:09Z] L 2026-10-15T03:03:26Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 413374764, "run": 1792033220, "sent": 96, "wall_ns": 1792033406364376177}
[2026-10-22T03:25:09Z] L 2026-10-15T03:07:54Z {"assets_n": 96, "bytes_total": 2103892072, "event": "verify", "release_id": 413374764, "run": 1792033220, "verify_sha256": "ff1dbc619728c35ab3732813ed23e83065603970c79ae62379097e59b1f13fa0", "wall_ns": 1792033674329218632}
[2026-10-22T03:25:09Z] L 2026-10-15T03:07:58Z {"already": 0, "event": "delete", "free_after": 12590329856, "free_before": 10485972992, "freed": 2103892072, "gone": 96, "removed": 96, "run": 1792033220, "wall_ns": 1792033678892316224, "windows_kept": 96}
[2026-10-22T03:25:09Z] L 2026-10-15T03:15:15Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1155982", "NRestarts": "6", "ns": 1792034115012851485}, "phase": 15, "run": 1792033220, "wall_ns": 1792034115012856996}
[2026-10-22T03:25:09Z] L 2026-10-15T03:15:15Z {"event": "kill", "exit": 0, "phase": 15, "run": 1792033220, "wall_ns": 1792034115018137811}
[2026-10-22T03:25:09Z] L 2026-10-15T03:15:45Z {"NRestarts": "7", "W": 1792034100, "event": "restart", "free_bytes": 12572676096, "gap_ns": 5531970911, "pid": 1284485, "run": 1792033220, "stopped": 1155982, "stream_bytes": 29667971, "wall_ns": 1792034145058520440}
[2026-10-22T03:25:09Z] L 2026-10-15T03:30:41Z {"T": 1792034100, "event": "resume", "reading": "PASS", "run": 1792033220, "wall_ns": 1792035041000365330}
[2026-10-22T03:25:09Z] L 2026-10-15T03:30:41Z {"assets_n": 96, "bytes_total": 2103892072, "ended_outside": 0, "event": "complete", "free_bytes": 12548313088, "peak_rss": 38199296, "rate_per_day": 2103892072, "requests": 197, "run": 1792033220, "started_outside": 0, "stops": [["the cap", 1792361344], ["the floor, base 43500000 bytes a day", 1792358863], ["the floor, base 187760570 bytes a day", 1792338478]], "store_stream_bytes": 54308421, "wall_ns": 1792035041006683547}
[2026-10-22T03:25:09Z] L 2026-10-15T06:18:30Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "1fd2e68b26a04a328b7551cbafc2eabe", "phase_at": 210, "resumed": false, "run": 1792045110, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792045110608854708}
[2026-10-22T03:25:09Z] L 2026-10-15T06:18:31Z {"assets_n": 14, "bytes_total": 352241341, "closed": 427, "deferred": 0, "event": "set", "first_T": 1792032300, "last_T": 1792044000, "open": 0, "run": 1792045110, "sha256": "0337b76512886f5dd78d71cfb303a343631f73624e2eb539ed79ed7f32cc0b8e", "tag": "pairbook-streams-1792045110", "unclosed": 0, "wall_ns": 1792045111425201892, "windows_considered": 427}
[2026-10-22T03:25:09Z] L 2026-10-15T06:19:00Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 413477311, "run": 1792045110, "sent": 14, "wall_ns": 1792045140771279777}
[2026-10-22T03:25:09Z] L 2026-10-15T06:21:20Z {"assets_n": 14, "bytes_total": 352241341, "event": "verify", "release_id": 413477311, "run": 1792045110, "verify_sha256": "52fc16f3058d99f3207b8fe2e61473302a0f89a9e1a2e0f5c8eb71f413e8e379", "wall_ns": 1792045280782420614}
[2026-10-22T03:25:09Z] L 2026-10-15T06:21:21Z {"already": 0, "event": "delete", "free_after": 12826914816, "free_before": 12474617856, "freed": 352241341, "gone": 14, "removed": 14, "run": 1792045110, "wall_ns": 1792045281527345757, "windows_kept": 14}
[2026-10-22T03:25:09Z] L 2026-10-15T06:21:21Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1284485", "NRestarts": "7", "ns": 1792045281539516731}, "phase": 381, "run": 1792045110, "wall_ns": 1792045281539522189}
[2026-10-22T03:25:09Z] L 2026-10-15T06:21:21Z {"event": "kill", "exit": 0, "phase": 381, "run": 1792045110, "wall_ns": 1792045281543696309}
[2026-10-22T03:25:09Z] L 2026-10-15T06:21:51Z {"NRestarts": "8", "W": 1792044900, "event": "restart", "free_bytes": 12826902528, "gap_ns": 5495918230, "pid": 1312748, "run": 1792045110, "stopped": 1284485, "stream_bytes": 0, "wall_ns": 1792045311558979330}
[2026-10-22T03:25:09Z] L 2026-10-15T06:30:41Z {"T": 1792044900, "event": "resume", "reading": "PASS", "run": 1792045110, "wall_ns": 1792045841024547052}
[2026-10-22T03:25:09Z] L 2026-10-15T06:30:41Z {"assets_n": 14, "bytes_total": 352241341, "ended_outside": 0, "event": "complete", "free_bytes": 12813713408, "peak_rss": 37543936, "rate_per_day": 2415369195, "requests": 33, "run": 1792045110, "started_outside": 0, "stops": [["the cap", 1792331549], ["the floor, base 43500000 bytes a day", 1792337969], ["the floor, base 187760570 bytes a day", 1792321779]], "store_stream_bytes": 12817136, "wall_ns": 1792045841098825002}
[2026-10-22T03:25:09Z] L 2026-10-16T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "5fd01e0598954380beeca3f3ac4c3f62", "phase_at": 20, "resumed": false, "run": 1792119620, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792119620165748278}
[2026-10-22T03:25:09Z] L 2026-10-16T03:00:24Z {"assets_n": 82, "bytes_total": 1804368058, "closed": 509, "deferred": 0, "event": "set", "first_T": 1792044900, "last_T": 1792117800, "open": 1, "run": 1792119620, "sha256": "adc52d666ace24c2145e55ef9d62602717d7726c791319304613be33c58459b6", "tag": "pairbook-streams-1792119620", "unclosed": 0, "wall_ns": 1792119624014812901, "windows_considered": 509}
[2026-10-22T03:25:09Z] L 2026-10-16T03:02:57Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 414488168, "run": 1792119620, "sent": 82, "wall_ns": 1792119777429141022}
[2026-10-22T03:25:09Z] L 2026-10-16T03:07:24Z {"assets_n": 82, "bytes_total": 1804368058, "event": "verify", "release_id": 414488168, "run": 1792119620, "verify_sha256": "96164ee15cef51426beba1050e8a4f47856762d5800a75fe9966f68164302e2a", "wall_ns": 1792120044830268724}
[2026-10-22T03:25:09Z] L 2026-10-16T03:07:28Z {"already": 0, "event": "delete", "free_after": 12728901632, "free_before": 10924134400, "freed": 1804368058, "gone": 82, "removed": 82, "run": 1792119620, "wall_ns": 1792120048628416638, "windows_kept": 82}
[2026-10-22T03:25:09Z] L 2026-10-16T03:07:28Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1312748", "NRestarts": "8", "ns": 1792120048640224099}, "phase": 448, "run": 1792119620, "wall_ns": 1792120048640229054}
[2026-10-22T03:25:09Z] L 2026-10-16T03:07:28Z {"event": "kill", "exit": 0, "phase": 448, "run": 1792119620, "wall_ns": 1792120048645966122}
[2026-10-22T03:25:09Z] L 2026-10-16T03:07:58Z {"NRestarts": "9", "W": 1792119600, "event": "restart", "free_bytes": 12728885248, "gap_ns": 5420693633, "pid": 1420617, "run": 1792119620, "stopped": 1312748, "stream_bytes": 12133793, "wall_ns": 1792120078665650185}
[2026-10-22T03:25:09Z] L 2026-10-16T03:15:41Z {"T": 1792119600, "event": "resume", "reading": "PASS", "run": 1792119620, "wall_ns": 1792120541000363636}
[2026-10-22T03:25:09Z] L 2026-10-16T03:15:41Z {"assets_n": 82, "bytes_total": 1804368058, "ended_outside": 0, "event": "complete", "free_bytes": 12710682624, "peak_rss": 38199296, "rate_per_day": 2112430897, "requests": 169, "run": 1792119620, "started_outside": 0, "stops": [["the cap", 1792446508], ["the floor, base 43500000 bytes a day", 1792449588], ["the floor, base 187760570 bytes a day", 1792428951]], "store_stream_bytes": 30286238, "wall_ns": 1792120541008367106}
[2026-10-22T03:25:09Z] L 2026-10-17T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "df3acd4ed1af4d05bc9ec4fa5085ebee", "phase_at": 20, "resumed": false, "run": 1792206020, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792206020485538925}
[2026-10-22T03:25:09Z] L 2026-10-17T03:00:24Z {"assets_n": 96, "bytes_total": 2048827436, "closed": 605, "deferred": 0, "event": "set", "first_T": 1792118700, "last_T": 1792204200, "open": 1, "run": 1792206020, "sha256": "0915abd5810c2b901012aa6d34388eabcc76d7be8b327d651632ac9335bbe188", "tag": "pairbook-streams-1792206020", "unclosed": 0, "wall_ns": 1792206024973916528, "windows_considered": 605}
[2026-10-22T03:25:09Z] L 2026-10-17T03:03:23Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 415548049, "run": 1792206020, "sent": 96, "wall_ns": 1792206203238800300}
[2026-10-22T03:25:09Z] L 2026-10-17T03:07:35Z {"assets_n": 96, "bytes_total": 2048827436, "event": "verify", "release_id": 415548049, "run": 1792206020, "verify_sha256": "747508e351bb13bb1aa11a99791ab87d1ea798e92c66dd1ec6126aad4f67f97c", "wall_ns": 1792206455599715552}
[2026-10-22T03:25:09Z] L 2026-10-17T03:07:40Z {"already": 0, "event": "delete", "free_after": 12725805056, "free_before": 10676551680, "freed": 2048827436, "gone": 96, "removed": 96, "run": 1792206020, "wall_ns": 1792206460092686139, "windows_kept": 96}
[2026-10-22T03:25:09Z] L 2026-10-17T03:07:40Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1420617", "NRestarts": "9", "ns": 1792206460108197241}, "phase": 460, "run": 1792206020, "wall_ns": 1792206460108202947}
[2026-10-22T03:25:09Z] L 2026-10-17T03:07:40Z {"event": "kill", "exit": 0, "phase": 460, "run": 1792206020, "wall_ns": 1792206460112982086}
[2026-10-22T03:25:09Z] L 2026-10-17T03:08:10Z {"NRestarts": "10", "W": 1792206000, "event": "restart", "free_bytes": 12725788672, "gap_ns": 5487288436, "pid": 1560378, "run": 1792206020, "stopped": 1420617, "stream_bytes": 10686101, "wall_ns": 1792206490133956812}
[2026-10-22T03:25:09Z] L 2026-10-17T03:15:41Z {"T": 1792206000, "event": "resume", "reading": "PASS", "run": 1792206020, "wall_ns": 1792206941000351565}
[2026-10-22T03:25:09Z] L 2026-10-17T03:15:41Z {"assets_n": 96, "bytes_total": 2048827436, "ended_outside": 0, "event": "complete", "free_bytes": 12715110400, "peak_rss": 38330368, "rate_per_day": 2048827436, "requests": 197, "run": 1792206020, "started_outside": 0, "stops": [["the cap", 1792543404], ["the floor, base 43500000 bytes a day", 1792546173], ["the floor, base 187760570 bytes a day", 1792524292]], "store_stream_bytes": 21346173, "wall_ns": 1792206941009261301}
[2026-10-22T03:25:09Z] L 2026-10-17T08:35:37Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "ab6b527c633847f79ce14ed1afdf3623", "phase_at": 337, "resumed": false, "run": 1792226137, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792226137790990342}
[2026-10-22T03:25:09Z] L 2026-10-17T08:35:38Z {"assets_n": 23, "bytes_total": 397545662, "closed": 628, "deferred": 0, "event": "set", "first_T": 1792205100, "last_T": 1792224900, "open": 0, "run": 1792226137, "sha256": "3db64b34a3949064d28cadc5a023e4402ebacc5cf7a2adab2fe09d13971312c4", "tag": "pairbook-streams-1792226137", "unclosed": 0, "wall_ns": 1792226138787331150, "windows_considered": 628}
[2026-10-22T03:25:09Z] L 2026-10-17T08:36:15Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 415679936, "run": 1792226137, "sent": 23, "wall_ns": 1792226175895145126}
[2026-10-22T03:25:09Z] L 2026-10-17T08:38:40Z {"assets_n": 23, "bytes_total": 397545662, "event": "verify", "release_id": 415679936, "run": 1792226137, "verify_sha256": "f26e295363dadaea4d9a2de3d5e86de06da641bf85ecec538e4a36b7e89de14f", "wall_ns": 1792226320606064836}
[2026-10-22T03:25:09Z] L 2026-10-17T08:38:41Z {"already": 0, "event": "delete", "free_after": 12799180800, "free_before": 12401537024, "freed": 397545662, "gone": 23, "removed": 23, "run": 1792226137, "wall_ns": 1792226321481880383, "windows_kept": 23}
[2026-10-22T03:25:09Z] L 2026-10-17T08:45:15Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1560378", "NRestarts": "10", "ns": 1792226715015188081}, "phase": 15, "run": 1792226137, "wall_ns": 1792226715015194823}
[2026-10-22T03:25:09Z] L 2026-10-17T08:45:15Z {"event": "kill", "exit": 0, "phase": 15, "run": 1792226137, "wall_ns": 1792226715020774740}
[2026-10-22T03:25:09Z] L 2026-10-17T08:45:45Z {"NRestarts": "11", "W": 1792226700, "event": "restart", "free_bytes": 12783226880, "gap_ns": 5530075996, "pid": 1595407, "run": 1792226137, "stopped": 1560378, "stream_bytes": 15521838, "wall_ns": 1792226745041554142}
[2026-10-22T03:25:09Z] L 2026-10-17T09:00:41Z {"T": 1792226700, "event": "resume", "reading": "PASS", "run": 1792226137, "wall_ns": 1792227641000413386}
[2026-10-22T03:25:09Z] L 2026-10-17T09:00:41Z {"assets_n": 23, "bytes_total": 397545662, "ended_outside": 0, "event": "complete", "free_bytes": 12773187584, "peak_rss": 37543936, "rate_per_day": 1659321024, "requests": 51, "run": 1792226137, "started_outside": 0, "stops": [["the cap", 1792642879], ["the floor, base 43500000 bytes a day", 1792647417], ["the floor, base 187760570 bytes a day", 1792614631]], "store_stream_bytes": 25293180, "wall_ns": 1792227641009539425}
[2026-10-22T03:25:09Z] L 2026-10-18T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "15934402892b403b858ea4b973f03c89", "phase_at": 20, "resumed": false, "run": 1792292420, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792292420527428655}
[2026-10-22T03:25:09Z] L 2026-10-18T03:00:23Z {"assets_n": 73, "bytes_total": 1197040692, "closed": 701, "deferred": 0, "event": "set", "first_T": 1792225800, "last_T": 1792290600, "open": 1, "run": 1792292420, "sha256": "7ddfeae4a937bc90c14d8047d3ab843035a2be145d8d407738f9620b098c0b08", "tag": "pairbook-streams-1792292420", "unclosed": 0, "wall_ns": 1792292423275187616, "windows_considered": 701}
[2026-10-22T03:25:09Z] L 2026-10-18T03:02:20Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 416201489, "run": 1792292420, "sent": 73, "wall_ns": 1792292540828362894}
[2026-10-22T03:25:09Z] L 2026-10-18T03:05:48Z {"assets_n": 73, "bytes_total": 1197040692, "event": "verify", "release_id": 416201489, "run": 1792292420, "verify_sha256": "a3eb29ead036c8a97f023ecb53572112300e5b22defa9d984ba1887dcddf95e3", "wall_ns": 1792292748968235081}
[2026-10-22T03:25:09Z] L 2026-10-18T03:05:51Z {"already": 0, "event": "delete", "free_after": 12776620032, "free_before": 11579240448, "freed": 1197040692, "gone": 73, "removed": 73, "run": 1792292420, "wall_ns": 1792292751530232000, "windows_kept": 73}
[2026-10-22T03:25:09Z] L 2026-10-18T03:05:51Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1595407", "NRestarts": "11", "ns": 1792292751542647421}, "phase": 351, "run": 1792292420, "wall_ns": 1792292751542652085}
[2026-10-22T03:25:09Z] L 2026-10-18T03:05:51Z {"event": "kill", "exit": 0, "phase": 351, "run": 1792292420, "wall_ns": 1792292751546822604}
[2026-10-22T03:25:09Z] L 2026-10-18T03:06:21Z {"NRestarts": "12", "W": 1792292400, "event": "restart", "free_bytes": 12776607744, "gap_ns": 5504206730, "pid": 1692402, "run": 1792292420, "stopped": 1595407, "stream_bytes": 12437717, "wall_ns": 1792292781569460854}
[2026-10-22T03:25:09Z] L 2026-10-18T03:15:41Z {"T": 1792292400, "event": "resume", "reading": "PASS", "run": 1792292420, "wall_ns": 1792293341000328710}
[2026-10-22T03:25:09Z] L 2026-10-18T03:15:41Z {"assets_n": 73, "bytes_total": 1197040692, "ended_outside": 0, "event": "complete", "free_bytes": 12764577792, "peak_rss": 37937152, "rate_per_day": 1574190499, "requests": 151, "run": 1792292420, "started_outside": 0, "stops": [["the cap", 1792731097], ["the floor, base 43500000 bytes a day", 1792734747], ["the floor, base 187760570 bytes a day", 1792698607]], "store_stream_bytes": 24161003, "wall_ns": 1792293341010228074}
[2026-10-22T03:25:09Z] L 2026-10-19T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "b6aa8a5cde4c4cc392165b8f31b1bec0", "phase_at": 20, "resumed": false, "run": 1792378820, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792378820477080166}
[2026-10-22T03:25:09Z] L 2026-10-19T03:00:24Z {"assets_n": 96, "bytes_total": 1755430954, "closed": 797, "deferred": 0, "event": "set", "first_T": 1792291500, "last_T": 1792377000, "open": 1, "run": 1792378820, "sha256": "948f4d39cca953e07be1c1c561f5115f6200f5aa8330fe78434c058d6e607528", "tag": "pairbook-streams-1792378820", "unclosed": 0, "wall_ns": 1792378824458122339, "windows_considered": 797}
[2026-10-22T03:25:09Z] L 2026-10-19T03:03:08Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 416860290, "run": 1792378820, "sent": 96, "wall_ns": 1792378988043909754}
[2026-10-22T03:25:09Z] L 2026-10-19T03:07:11Z {"assets_n": 96, "bytes_total": 1755430954, "event": "verify", "release_id": 416860290, "run": 1792378820, "verify_sha256": "86b0b971d6eaeb1c8fd7dd87f44b2f739282eec95c52919b65b79ea293db2551", "wall_ns": 1792379231626951320}
[2026-10-22T03:25:09Z] L 2026-10-19T03:07:15Z {"already": 0, "event": "delete", "free_after": 12737359872, "free_before": 10981560320, "freed": 1755430954, "gone": 96, "removed": 96, "run": 1792378820, "wall_ns": 1792379235366652736, "windows_kept": 96}
[2026-10-22T03:25:09Z] L 2026-10-19T03:07:15Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1692402", "NRestarts": "12", "ns": 1792379235374600961}, "phase": 435, "run": 1792378820, "wall_ns": 1792379235374606661}
[2026-10-22T03:25:09Z] L 2026-10-19T03:07:15Z {"event": "kill", "exit": 0, "phase": 435, "run": 1792378820, "wall_ns": 1792379235379253859}
[2026-10-22T03:25:09Z] L 2026-10-19T03:07:45Z {"NRestarts": "13", "W": 1792378800, "event": "restart", "free_bytes": 12737351680, "gap_ns": 5404558972, "pid": 1814768, "run": 1792378820, "stopped": 1692402, "stream_bytes": 20988190, "wall_ns": 1792379265403200749}
[2026-10-22T03:25:09Z] L 2026-10-19T03:15:41Z {"T": 1792378800, "event": "resume", "reading": "PASS", "run": 1792378820, "wall_ns": 1792379741000400500}
[2026-10-22T03:25:09Z] L 2026-10-19T03:15:41Z {"assets_n": 96, "bytes_total": 1755430954, "ended_outside": 0, "event": "complete", "free_bytes": 12720193536, "peak_rss": 38592512, "rate_per_day": 1755430954, "requests": 197, "run": 1792378820, "started_outside": 0, "stops": [["the cap", 1792771618], ["the floor, base 43500000 bytes a day", 1792774544], ["the floor, base 187760570 bytes a day", 1792745234]], "store_stream_bytes": 38026457, "wall_ns": 1792379741011807328}
[2026-10-22T03:25:09Z] L 2026-10-19T21:54:19Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "7efdb0d05f6f4814b803f423a1351eae", "phase_at": 559, "resumed": false, "run": 1792446859, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792446859827562789}
[2026-10-22T03:25:09Z] L 2026-10-19T21:54:23Z {"assets_n": 76, "bytes_total": 1702929677, "closed": 873, "deferred": 0, "event": "set", "first_T": 1792377900, "last_T": 1792445400, "open": 1, "run": 1792446859, "sha256": "8491aab13dd6df082e8a4e847bd4e676a5edbeabd050e9a1767a79d7ecfb72d3", "tag": "pairbook-streams-1792446859", "unclosed": 0, "wall_ns": 1792446863665163186, "windows_considered": 873}
[2026-10-22T03:25:09Z] L 2026-10-19T22:02:33Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 417794290, "run": 1792446859, "sent": 76, "wall_ns": 1792447353191732798}
[2026-10-22T03:25:09Z] L 2026-10-19T22:09:37Z {"assets_n": 76, "bytes_total": 1702929677, "event": "verify", "release_id": 417794290, "run": 1792446859, "verify_sha256": "dfa62b04b0291467b86d37271e00e2242c0fea6b9e1caa987e7a9b31fafd3f6b", "wall_ns": 1792447777762252351}
[2026-10-22T03:25:09Z] L 2026-10-19T22:09:41Z {"already": 0, "event": "delete", "free_after": 12726702080, "free_before": 11023396864, "freed": 1702929677, "gone": 76, "removed": 76, "run": 1792446859, "wall_ns": 1792447781500420485, "windows_kept": 76}
[2026-10-22T03:25:09Z] L 2026-10-19T22:15:15Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1814768", "NRestarts": "13", "ns": 1792448115017795294}, "phase": 15, "run": 1792446859, "wall_ns": 1792448115017801355}
[2026-10-22T03:25:09Z] L 2026-10-19T22:15:15Z {"event": "kill", "exit": 0, "phase": 15, "run": 1792446859, "wall_ns": 1792448115024251292}
[2026-10-22T03:25:09Z] L 2026-10-19T22:15:45Z {"NRestarts": "14", "W": 1792448100, "event": "restart", "free_bytes": 12707540992, "gap_ns": 5638947193, "pid": 1915093, "run": 1792446859, "stopped": 1814768, "stream_bytes": 30931694, "wall_ns": 1792448145064395857}
[2026-10-22T03:25:09Z] L 2026-10-19T22:30:41Z {"T": 1792448100, "event": "resume", "reading": "PASS", "run": 1792446859, "wall_ns": 1792449041000625272}
[2026-10-22T03:25:09Z] L 2026-10-19T22:30:41Z {"assets_n": 76, "bytes_total": 1702929677, "ended_outside": 0, "event": "complete", "free_bytes": 12678688768, "peak_rss": 37539840, "rate_per_day": 2151069065, "requests": 157, "run": 1792446859, "started_outside": 0, "stops": [["the cap", 1792767956], ["the floor, base 43500000 bytes a day", 1792771035], ["the floor, base 187760570 bytes a day", 1792751174]], "store_stream_bytes": 60078470, "wall_ns": 1792449041020984137}
[2026-10-22T03:25:09Z] L 2026-10-20T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "39b80e28726849c6b2c7c78015f76beb", "phase_at": 20, "resumed": false, "run": 1792465220, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792465220508369328}
[2026-10-22T03:25:09Z] L 2026-10-20T03:00:21Z {"assets_n": 20, "bytes_total": 428604581, "closed": 893, "deferred": 0, "event": "set", "first_T": 1792446300, "last_T": 1792463400, "open": 1, "run": 1792465220, "sha256": "08a4bf67291e8988351d7b031e9a6250ded7ec726fb2a80a1c28559d6b827e6b", "tag": "pairbook-streams-1792465220", "unclosed": 0, "wall_ns": 1792465221560132886, "windows_considered": 893}
[2026-10-22T03:25:09Z] L 2026-10-20T03:01:05Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 417955485, "run": 1792465220, "sent": 20, "wall_ns": 1792465265840619699}
[2026-10-22T03:25:09Z] L 2026-10-20T03:03:38Z {"assets_n": 20, "bytes_total": 428604581, "event": "verify", "release_id": 417955485, "run": 1792465220, "verify_sha256": "1417b0845ea746c17a126d8311895714cd28b5cdbefbb3f27cc38e7b2d8a516a", "wall_ns": 1792465418377004134}
[2026-10-22T03:25:09Z] L 2026-10-20T03:03:39Z {"already": 0, "event": "delete", "free_after": 12736249856, "free_before": 12307550208, "freed": 428604581, "gone": 20, "removed": 20, "run": 1792465220, "wall_ns": 1792465419274331805, "windows_kept": 20}
[2026-10-22T03:25:09Z] L 2026-10-20T03:03:39Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1915093", "NRestarts": "14", "ns": 1792465419285640926}, "phase": 219, "run": 1792465220, "wall_ns": 1792465419285646173}
[2026-10-22T03:25:09Z] L 2026-10-20T03:03:39Z {"event": "kill", "exit": 0, "phase": 219, "run": 1792465220, "wall_ns": 1792465419290626015}
[2026-10-22T03:25:09Z] L 2026-10-20T03:04:09Z {"NRestarts": "15", "W": 1792465200, "event": "restart", "free_bytes": 12736208896, "gap_ns": 5521442701, "pid": 1942330, "run": 1792465220, "stopped": 1915093, "stream_bytes": 21234976, "wall_ns": 1792465449314599186}
[2026-10-22T03:25:09Z] L 2026-10-20T03:15:41Z {"T": 1792465200, "event": "resume", "reading": "PASS", "run": 1792465220, "wall_ns": 1792466141000339712}
[2026-10-22T03:25:09Z] L 2026-10-20T03:15:41Z {"assets_n": 20, "bytes_total": 428604581, "ended_outside": 0, "event": "complete", "free_bytes": 12714721280, "peak_rss": 37937152, "rate_per_day": 2057301988, "requests": 45, "run": 1792465220, "started_outside": 0, "stops": [["the cap", 1792800340], ["the floor, base 43500000 bytes a day", 1792803989], ["the floor, base 187760570 bytes a day", 1792782280]], "store_stream_bytes": 42260469, "wall_ns": 1792466141012853604}
[2026-10-22T03:25:09Z] L 2026-10-20T11:23:37Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "8b75ff2677d249a6a9fe69e50db1c2ae", "phase_at": 517, "resumed": false, "run": 1792495417, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792495417844843187}
[2026-10-22T03:25:09Z] L 2026-10-20T11:23:39Z {"assets_n": 34, "bytes_total": 764815296, "closed": 927, "deferred": 0, "event": "set", "first_T": 1792464300, "last_T": 1792494000, "open": 0, "run": 1792495417, "sha256": "e323ee33788d09b6cc52062cea9cd4914bc06d83a423f00e8704115f5ee8077e", "tag": "pairbook-streams-1792495417", "unclosed": 0, "wall_ns": 1792495419680991102, "windows_considered": 927}
[2026-10-22T03:25:09Z] L 2026-10-20T11:30:29Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 418317989, "run": 1792495417, "sent": 34, "wall_ns": 1792495829134879887}
[2026-10-22T03:25:09Z] L 2026-10-20T11:33:19Z {"assets_n": 34, "bytes_total": 764815296, "event": "verify", "release_id": 418317989, "run": 1792495417, "verify_sha256": "c2b18808ac9dd1fa1af41eb8e9b6f3b616698bb12dcfc8910b97f44dc91c36ac", "wall_ns": 1792495999645679199}
[2026-10-22T03:25:09Z] L 2026-10-20T11:33:21Z {"already": 0, "event": "delete", "free_after": 12638756864, "free_before": 11873771520, "freed": 764815296, "gone": 34, "removed": 34, "run": 1792495417, "wall_ns": 1792496001362671467, "windows_kept": 34}
[2026-10-22T03:25:09Z] L 2026-10-20T11:33:21Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1942330", "NRestarts": "15", "ns": 1792496001380557653}, "phase": 201, "run": 1792495417, "wall_ns": 1792496001380565155}
[2026-10-22T03:25:09Z] L 2026-10-20T11:33:21Z {"event": "kill", "exit": 0, "phase": 201, "run": 1792495417, "wall_ns": 1792496001386376172}
[2026-10-22T03:25:09Z] L 2026-10-20T11:33:51Z {"NRestarts": "16", "W": 1792495800, "event": "restart", "free_bytes": 12638744576, "gap_ns": 5668185588, "pid": 1997029, "run": 1792495417, "stopped": 1942330, "stream_bytes": 20135691, "wall_ns": 1792496031413213462}
[2026-10-22T03:25:09Z] L 2026-10-20T11:45:41Z {"T": 1792495800, "event": "resume", "reading": "PASS", "run": 1792495417, "wall_ns": 1792496741000411804}
[2026-10-22T03:25:09Z] L 2026-10-20T11:45:41Z {"assets_n": 34, "bytes_total": 764815296, "ended_outside": 0, "event": "complete", "free_bytes": 12627136512, "peak_rss": 37408768, "rate_per_day": 2159478482, "requests": 73, "run": 1792495417, "started_outside": 0, "stops": [["the cap", 1792815561], ["the floor, base 43500000 bytes a day", 1792815484], ["the floor, base 187760570 bytes a day", 1792795894]], "store_stream_bytes": 31416312, "wall_ns": 1792496741014150948}
[2026-10-22T03:25:09Z] L 2026-10-21T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "b930c6730bf241b99c68a735c088800c", "phase_at": 20, "resumed": false, "run": 1792551620, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792551620436317477}
[2026-10-22T03:25:09Z] L 2026-10-21T03:00:23Z {"assets_n": 62, "bytes_total": 1362902551, "closed": 989, "deferred": 0, "event": "set", "first_T": 1792494900, "last_T": 1792549800, "open": 1, "run": 1792551620, "sha256": "86c50466510f2054e4aa0455af33787059c1cc16b6a2f3dc81b5ef002ecb9ae5", "tag": "pairbook-streams-1792551620", "unclosed": 0, "wall_ns": 1792551623641943166, "windows_considered": 989}
[2026-10-22T03:25:09Z] L 2026-10-21T03:02:34Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 419096475, "run": 1792551620, "sent": 62, "wall_ns": 1792551754079483237}
[2026-10-22T03:25:09Z] L 2026-10-21T03:06:11Z {"assets_n": 62, "bytes_total": 1362902551, "event": "verify", "release_id": 419096475, "run": 1792551620, "verify_sha256": "fcd57c3250da0c73a0a463197880ede0b4caba30b2d3531b5e67c74d89101b77", "wall_ns": 1792551971026358089}
[2026-10-22T03:25:09Z] L 2026-10-21T03:06:13Z {"already": 0, "event": "delete", "free_after": 12585439232, "free_before": 11222228992, "freed": 1362902551, "gone": 62, "removed": 62, "run": 1792551620, "wall_ns": 1792551973979858662, "windows_kept": 62}
[2026-10-22T03:25:09Z] L 2026-10-21T03:06:13Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1997029", "NRestarts": "16", "ns": 1792551973992391945}, "phase": 373, "run": 1792551620, "wall_ns": 1792551973992396231}
[2026-10-22T03:25:09Z] L 2026-10-21T03:06:13Z {"event": "kill", "exit": 0, "phase": 373, "run": 1792551620, "wall_ns": 1792551973997452972}
[2026-10-22T03:25:09Z] L 2026-10-21T03:06:44Z {"NRestarts": "17", "W": 1792551600, "event": "restart", "free_bytes": 12585414656, "gap_ns": 5552861113, "pid": 2076364, "run": 1792551620, "stopped": 1997029, "stream_bytes": 21344325, "wall_ns": 1792552004023624781}
[2026-10-22T03:25:09Z] L 2026-10-21T03:15:41Z {"T": 1792551600, "event": "resume", "reading": "PASS", "run": 1792551620, "wall_ns": 1792552541000652508}
[2026-10-22T03:25:09Z] L 2026-10-21T03:15:41Z {"assets_n": 62, "bytes_total": 1362902551, "ended_outside": 0, "event": "complete", "free_bytes": 12568043520, "peak_rss": 38330368, "rate_per_day": 2110300724, "requests": 129, "run": 1792551620, "started_outside": 0, "stops": [["the cap", 1792878503], ["the floor, base 43500000 bytes a day", 1792876191], ["the floor, base 187760570 bytes a day", 1792855874]], "store_stream_bytes": 38435764, "wall_ns": 1792552541015556785}
[2026-10-22T03:25:09Z] L 2026-10-21T21:39:04Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "ddf646820072487fbca10fe0ea1d6d9d", "phase_at": 544, "resumed": false, "run": 1792618744, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792618744805106316}
[2026-10-22T03:25:09Z] L 2026-10-21T21:39:08Z {"assets_n": 75, "bytes_total": 1697351287, "closed": 1064, "deferred": 0, "event": "set", "first_T": 1792550700, "last_T": 1792617300, "open": 0, "run": 1792618744, "sha256": "14628f1239ce9548ab9a88bfae0a8017382eac3a6c54f823b79c7acf8e9f2d70", "tag": "pairbook-streams-1792618744", "unclosed": 0, "wall_ns": 1792618748723134556, "windows_considered": 1064}
[2026-10-22T03:25:09Z] L 2026-10-21T21:47:16Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 420082380, "run": 1792618744, "sent": 75, "wall_ns": 1792619236058059430}
[2026-10-22T03:25:09Z] L 2026-10-21T21:51:01Z {"assets_n": 75, "bytes_total": 1697351287, "event": "verify", "release_id": 420082380, "run": 1792618744, "verify_sha256": "954d28907c55dac360cea2a28a7781c4ca0500ef6c8313c3c86a6853539dbbce", "wall_ns": 1792619461695303474}
[2026-10-22T03:25:09Z] L 2026-10-21T21:51:05Z {"already": 0, "event": "delete", "free_after": 12533227520, "free_before": 10835509248, "freed": 1697351287, "gone": 75, "removed": 75, "run": 1792618744, "wall_ns": 1792619465416013472, "windows_kept": 75}
[2026-10-22T03:25:09Z] L 2026-10-21T21:51:05Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "2076364", "NRestarts": "17", "ns": 1792619465433993359}, "phase": 365, "run": 1792618744, "wall_ns": 1792619465433999513}
[2026-10-22T03:25:09Z] L 2026-10-21T21:51:05Z {"event": "kill", "exit": 0, "phase": 365, "run": 1792618744, "wall_ns": 1792619465439433263}
[2026-10-22T03:25:09Z] L 2026-10-21T21:51:35Z {"NRestarts": "18", "W": 1792619100, "event": "restart", "free_bytes": 12533202944, "gap_ns": 5745862259, "pid": 2192943, "run": 1792618744, "stopped": 2076364, "stream_bytes": 28722461, "wall_ns": 1792619495470455301}
[2026-10-22T03:25:09Z] L 2026-10-21T22:00:41Z {"T": 1792619100, "event": "resume", "reading": "PASS", "run": 1792618744, "wall_ns": 1792620041000434452}
[2026-10-22T03:25:09Z] L 2026-10-21T22:00:41Z {"assets_n": 75, "bytes_total": 1697351287, "ended_outside": 0, "event": "complete", "free_bytes": 12508360704, "peak_rss": 37806080, "rate_per_day": 2172609647, "requests": 155, "run": 1792618744, "started_outside": 0, "stops": [["the cap", 1792936072], ["the floor, base 43500000 bytes a day", 1792932264], ["the floor, base 187760570 bytes a day", 1792913182]], "store_stream_bytes": 53078752, "wall_ns": 1792620041014703750}
[2026-10-22T03:25:09Z] L 2026-10-22T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "2ead70f2934e426f9db2802c9f366424", "phase_at": 20, "resumed": false, "run": 1792638020, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792638020509862222}
[2026-10-22T03:25:09Z] L 2026-10-22T03:00:21Z {"assets_n": 21, "bytes_total": 391495954, "closed": 1085, "deferred": 0, "event": "set", "first_T": 1792618200, "last_T": 1792636200, "open": 1, "run": 1792638020, "sha256": "bcccbdcea9b48dfb0ce8b98e2ce6eb1faeb741091d2f4b96a260cd633af8810d", "tag": "pairbook-streams-1792638020", "unclosed": 0, "wall_ns": 1792638021492965919, "windows_considered": 1085}
[2026-10-22T03:25:09Z] L 2026-10-22T03:01:03Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 420262131, "run": 1792638020, "sent": 21, "wall_ns": 1792638063331313560}
[2026-10-22T03:25:09Z] L 2026-10-22T03:03:31Z {"assets_n": 21, "bytes_total": 391495954, "event": "verify", "release_id": 420262131, "run": 1792638020, "verify_sha256": "c53531cd81ef4f93c4a7a970b2c0c542146e78ed84d309d0afb42f14ab7123c9", "wall_ns": 1792638211785126344}
[2026-10-22T03:25:09Z] L 2026-10-22T03:03:32Z {"already": 0, "event": "delete", "free_after": 12514353152, "free_before": 12122759168, "freed": 391495954, "gone": 21, "removed": 21, "run": 1792638020, "wall_ns": 1792638212641898392, "windows_kept": 21}
[2026-10-22T03:25:09Z] L 2026-10-22T03:03:32Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "2192943", "NRestarts": "18", "ns": 1792638212654633160}, "phase": 212, "run": 1792638020, "wall_ns": 1792638212654637695}
[2026-10-22T03:25:09Z] L 2026-10-22T03:03:32Z {"event": "kill", "exit": 0, "phase": 212, "run": 1792638020, "wall_ns": 1792638212659732496}
[2026-10-22T03:25:09Z] L 2026-10-22T03:04:02Z {"NRestarts": "19", "W": 1792638000, "event": "restart", "free_bytes": 12514340864, "gap_ns": 5643787804, "pid": 2221487, "run": 1792638020, "stopped": 2192943, "stream_bytes": 27860091, "wall_ns": 1792638242689438971}
[2026-10-22T03:25:09Z] L 2026-10-22T03:15:41Z {"T": 1792638000, "event": "resume", "reading": "PASS", "run": 1792638020, "wall_ns": 1792638941000342309}
[2026-10-22T03:25:09Z] L 2026-10-22T03:15:41Z {"assets_n": 21, "bytes_total": 391495954, "ended_outside": 0, "event": "complete", "free_bytes": 12499591168, "peak_rss": 38195200, "rate_per_day": 1789695789, "requests": 47, "run": 1792638020, "started_outside": 0, "stops": [["the cap", 1793023110], ["the floor, base 43500000 bytes a day", 1793015968], ["the floor, base 187760570 bytes a day", 1792988463]], "store_stream_bytes": 42282498, "wall_ns": 1792638941017392845}
[2026-10-22T03:25:09Z] run 1791731892 2026-10-11T15:18:12Z, off-calendar, second 55092 of the day: 10 records; terminal complete; set pairbook-streams-1791731892: 28 files, 430047476 bytes, windows 1791706500 to 1791730800; restart: window 1791731700, pid 851381 after 815823, NRestarts 3; complete: requests 61, started outside 0, ended outside 0, rate 1474448489 a day
[2026-10-22T03:25:09Z] run 1791774020 2026-10-12T03:00:20Z, calendar: 10 records; terminal complete; set pairbook-streams-1791774020: 46 files, 794522712 bytes, windows 1791731700 to 1791772200; restart: window 1791774000, pid 911226 after 851381, NRestarts 4; complete: requests 97, started outside 0, ended outside 0, rate 1658134355 a day
[2026-10-22T03:25:09Z] run 1791860420 2026-10-13T03:00:20Z, calendar: 10 records; terminal complete; set pairbook-streams-1791860420: 96 files, 1925987888 bytes, windows 1791773100 to 1791858600; restart: window 1791860400, pid 1027378 after 911226, NRestarts 5; complete: requests 197, started outside 0, ended outside 0, rate 1925987888 a day
[2026-10-22T03:25:09Z] run 1791946820 2026-10-14T03:00:20Z, calendar: 10 records; terminal complete; set pairbook-streams-1791946820: 96 files, 2039544263 bytes, windows 1791859500 to 1791945000; restart: window 1791946800, pid 1155982 after 1027378, NRestarts 6; complete: requests 197, started outside 0, ended outside 0, rate 2039544263 a day
[2026-10-22T03:25:09Z] run 1792033220 2026-10-15T03:00:20Z, calendar: 10 records; terminal complete; set pairbook-streams-1792033220: 96 files, 2103892072 bytes, windows 1791945900 to 1792031400; restart: window 1792034100, pid 1284485 after 1155982, NRestarts 7; complete: requests 197, started outside 0, ended outside 0, rate 2103892072 a day
[2026-10-22T03:25:09Z] run 1792045110 2026-10-15T06:18:30Z, off-calendar, second 22710 of the day: 10 records; terminal complete; set pairbook-streams-1792045110: 14 files, 352241341 bytes, windows 1792032300 to 1792044000; restart: window 1792044900, pid 1312748 after 1284485, NRestarts 8; complete: requests 33, started outside 0, ended outside 0, rate 2415369195 a day
[2026-10-22T03:25:09Z] run 1792119620 2026-10-16T03:00:20Z, calendar: 10 records; terminal complete; set pairbook-streams-1792119620: 82 files, 1804368058 bytes, windows 1792044900 to 1792117800; restart: window 1792119600, pid 1420617 after 1312748, NRestarts 9; complete: requests 169, started outside 0, ended outside 0, rate 2112430897 a day
[2026-10-22T03:25:09Z] run 1792206020 2026-10-17T03:00:20Z, calendar: 10 records; terminal complete; set pairbook-streams-1792206020: 96 files, 2048827436 bytes, windows 1792118700 to 1792204200; restart: window 1792206000, pid 1560378 after 1420617, NRestarts 10; complete: requests 197, started outside 0, ended outside 0, rate 2048827436 a day
[2026-10-22T03:25:09Z] run 1792226137 2026-10-17T08:35:37Z, off-calendar, second 30937 of the day: 10 records; terminal complete; set pairbook-streams-1792226137: 23 files, 397545662 bytes, windows 1792205100 to 1792224900; restart: window 1792226700, pid 1595407 after 1560378, NRestarts 11; complete: requests 51, started outside 0, ended outside 0, rate 1659321024 a day
[2026-10-22T03:25:09Z] run 1792292420 2026-10-18T03:00:20Z, calendar: 10 records; terminal complete; set pairbook-streams-1792292420: 73 files, 1197040692 bytes, windows 1792225800 to 1792290600; restart: window 1792292400, pid 1692402 after 1595407, NRestarts 12; complete: requests 151, started outside 0, ended outside 0, rate 1574190499 a day
[2026-10-22T03:25:09Z] run 1792378820 2026-10-19T03:00:20Z, calendar: 10 records; terminal complete; set pairbook-streams-1792378820: 96 files, 1755430954 bytes, windows 1792291500 to 1792377000; restart: window 1792378800, pid 1814768 after 1692402, NRestarts 13; complete: requests 197, started outside 0, ended outside 0, rate 1755430954 a day
[2026-10-22T03:25:09Z] run 1792446859 2026-10-19T21:54:19Z, off-calendar, second 78859 of the day: 10 records; terminal complete; set pairbook-streams-1792446859: 76 files, 1702929677 bytes, windows 1792377900 to 1792445400; restart: window 1792448100, pid 1915093 after 1814768, NRestarts 14; complete: requests 157, started outside 0, ended outside 0, rate 2151069065 a day
[2026-10-22T03:25:09Z] run 1792465220 2026-10-20T03:00:20Z, calendar: 10 records; terminal complete; set pairbook-streams-1792465220: 20 files, 428604581 bytes, windows 1792446300 to 1792463400; restart: window 1792465200, pid 1942330 after 1915093, NRestarts 15; complete: requests 45, started outside 0, ended outside 0, rate 2057301988 a day
[2026-10-22T03:25:09Z] run 1792495417 2026-10-20T11:23:37Z, off-calendar, second 41017 of the day: 10 records; terminal complete; set pairbook-streams-1792495417: 34 files, 764815296 bytes, windows 1792464300 to 1792494000; restart: window 1792495800, pid 1997029 after 1942330, NRestarts 16; complete: requests 73, started outside 0, ended outside 0, rate 2159478482 a day
[2026-10-22T03:25:09Z] run 1792551620 2026-10-21T03:00:20Z, calendar: 10 records; terminal complete; set pairbook-streams-1792551620: 62 files, 1362902551 bytes, windows 1792494900 to 1792549800; restart: window 1792551600, pid 2076364 after 1997029, NRestarts 17; complete: requests 129, started outside 0, ended outside 0, rate 2110300724 a day
[2026-10-22T03:25:09Z] run 1792618744 2026-10-21T21:39:04Z, off-calendar, second 77944 of the day: 10 records; terminal complete; set pairbook-streams-1792618744: 75 files, 1697351287 bytes, windows 1792550700 to 1792617300; restart: window 1792619100, pid 2192943 after 2076364, NRestarts 18; complete: requests 155, started outside 0, ended outside 0, rate 2172609647 a day
[2026-10-22T03:25:09Z] run 1792638020 2026-10-22T03:00:20Z, calendar: 10 records; terminal complete; set pairbook-streams-1792638020: 21 files, 391495954 bytes, windows 1792618200 to 1792636200; restart: window 1792638000, pid 2221487 after 2192943, NRestarts 19; complete: requests 47, started outside 0, ended outside 0, rate 1789695789 a day
[2026-10-22T03:25:09Z] set of run 1791731892: pairbook-streams-1791731892, 28 assets, 430047476 bytes, windows 1791706500 to 1791730800, sha256 ec3983419485fa67317468917eb7b60e2d0e529be4334c7297831ff562471ad0
[2026-10-22T03:25:09Z] set of run 1791774020: pairbook-streams-1791774020, 46 assets, 794522712 bytes, windows 1791731700 to 1791772200, sha256 c8f02de3fbed47c4cfa91e66d774427f20990f634d271237bf3c6f25887ffb99
[2026-10-22T03:25:09Z] set of run 1791860420: pairbook-streams-1791860420, 96 assets, 1925987888 bytes, windows 1791773100 to 1791858600, sha256 de9209f2e76e5c42bd1395ea6e9c17ab0fc4c497be6a9311cd1e07c101f9b777
[2026-10-22T03:25:09Z] set of run 1791946820: pairbook-streams-1791946820, 96 assets, 2039544263 bytes, windows 1791859500 to 1791945000, sha256 9c78ba5221e0bc8d9d8699d920e17c58d76b6052fce7c0e86af4948bdc38aa1e
[2026-10-22T03:25:09Z] set of run 1792033220: pairbook-streams-1792033220, 96 assets, 2103892072 bytes, windows 1791945900 to 1792031400, sha256 3272c87234da82333365144d0c39bb0f75e895943e7e34ec7ff1e559c1ad8715
[2026-10-22T03:25:09Z] set of run 1792045110: pairbook-streams-1792045110, 14 assets, 352241341 bytes, windows 1792032300 to 1792044000, sha256 0337b76512886f5dd78d71cfb303a343631f73624e2eb539ed79ed7f32cc0b8e
[2026-10-22T03:25:09Z] set of run 1792119620: pairbook-streams-1792119620, 82 assets, 1804368058 bytes, windows 1792044900 to 1792117800, sha256 adc52d666ace24c2145e55ef9d62602717d7726c791319304613be33c58459b6
[2026-10-22T03:25:09Z] set of run 1792206020: pairbook-streams-1792206020, 96 assets, 2048827436 bytes, windows 1792118700 to 1792204200, sha256 0915abd5810c2b901012aa6d34388eabcc76d7be8b327d651632ac9335bbe188
[2026-10-22T03:25:09Z] set of run 1792226137: pairbook-streams-1792226137, 23 assets, 397545662 bytes, windows 1792205100 to 1792224900, sha256 3db64b34a3949064d28cadc5a023e4402ebacc5cf7a2adab2fe09d13971312c4
[2026-10-22T03:25:09Z] set of run 1792292420: pairbook-streams-1792292420, 73 assets, 1197040692 bytes, windows 1792225800 to 1792290600, sha256 7ddfeae4a937bc90c14d8047d3ab843035a2be145d8d407738f9620b098c0b08
[2026-10-22T03:25:09Z] set of run 1792378820: pairbook-streams-1792378820, 96 assets, 1755430954 bytes, windows 1792291500 to 1792377000, sha256 948f4d39cca953e07be1c1c561f5115f6200f5aa8330fe78434c058d6e607528
[2026-10-22T03:25:09Z] set of run 1792446859: pairbook-streams-1792446859, 76 assets, 1702929677 bytes, windows 1792377900 to 1792445400, sha256 8491aab13dd6df082e8a4e847bd4e676a5edbeabd050e9a1767a79d7ecfb72d3
[2026-10-22T03:25:09Z] set of run 1792465220: pairbook-streams-1792465220, 20 assets, 428604581 bytes, windows 1792446300 to 1792463400, sha256 08a4bf67291e8988351d7b031e9a6250ded7ec726fb2a80a1c28559d6b827e6b
[2026-10-22T03:25:09Z] set of run 1792495417: pairbook-streams-1792495417, 34 assets, 764815296 bytes, windows 1792464300 to 1792494000, sha256 e323ee33788d09b6cc52062cea9cd4914bc06d83a423f00e8704115f5ee8077e
[2026-10-22T03:25:09Z] set of run 1792551620: pairbook-streams-1792551620, 62 assets, 1362902551 bytes, windows 1792494900 to 1792549800, sha256 86c50466510f2054e4aa0455af33787059c1cc16b6a2f3dc81b5ef002ecb9ae5
[2026-10-22T03:25:09Z] set of run 1792618744: pairbook-streams-1792618744, 75 assets, 1697351287 bytes, windows 1792550700 to 1792617300, sha256 14628f1239ce9548ab9a88bfae0a8017382eac3a6c54f823b79c7acf8e9f2d70
[2026-10-22T03:25:09Z] set of run 1792638020: pairbook-streams-1792638020, 21 assets, 391495954 bytes, windows 1792618200 to 1792636200, sha256 bcccbdcea9b48dfb0ce8b98e2ce6eb1faeb741091d2f4b96a260cd633af8810d
[2026-10-22T03:25:09Z] tags on origin 17; the sets' tags not on origin []
[2026-10-22T03:25:09Z] runs 17; complete 17; without a terminal record []; halted False
[2026-10-22T03:25:09Z] G-ASSETS: 1034 windows 1791706500 to 1792636200, 1034 stream files, 21197547900 bytes; windows with more than one file []; windows missing between []
[2026-10-22T03:25:09Z] the candidates 1791706500 to 1792548000: 936 windows moved, 19056891926 bytes; every window to 1792548000 moved
[2026-10-22T03:25:09Z] peak memory of this run: 34357248 bytes
[2026-10-22T03:25:09Z] refused: 0 by this file's hook, 0 by TZ-24's
exit=0
```

</details>

The second read, at §3.11 (`logs/25-archive-2.log`, `85e18aad6352b08f8220978043db2a9223c2286b2642f1165432c240991f8027`), is the same 214 lines but one. `diff` of the two without their stamps:

```
212c212
<  peak memory of this run: 34357248 bytes
---
>  peak memory of this run: 33964032 bytes
```

**In short:**

- 17 runs, all `complete`, none halted; no request started or ended outside the idle stretch.
- Their 17 sets are contiguous, 1,034 windows `1791706500` … `1792636200`, one stream file each, `21,197,547,900` bytes, with no window missing.
- The 936 candidates `1791706500` … `1792548000` are all moved, `19,056,891,926` bytes.
- Each run restarted the pair book once: `NRestarts` 3 → 19, pid `2221487` since 2026-10-22 03:03:38 UTC.
- The latest `upload` record's credential is `"the primary checkout's remote URL"` (run `1792638020`, Release `420262131`, 2026-10-22 03:01:03Z). The two runs before it carry the same credential, Releases `419096475` and `420082380`.

**Runs off the calendar, beside §0.3's reads:**

| run | UTC | since map §2.5 | §0.3: boots | timer journal since 10-14 | package history near it |
|---|---|---|---|---|---|
| `1791731892` | 2026-10-11 15:18:12 | known — TZ-28's first run | one boot since 2026-08-02 | — | — |
| `1792045110` | 2026-10-15 06:18:30 | known | no boot | no entries | `unattended-upgrade`, 2026-10-15 06:09:16 – 06:09:29 |
| `1792226137` | 2026-10-17 08:35:37 | known | no boot | no entries | no entry in the last 40 lines that day |
| `1792446859` | 2026-10-19 21:54:19 | known | no boot | no entries | none |
| `1792495417` | 2026-10-20 11:23:37 | read by map §2.5 from its tag alone; here from its ledger: 34 files, `1792464300` … `1792494000`, `764,815,296` bytes | no boot | no entries | `unattended-upgrade` 2026-10-20 06:28 (git, libxtst6), five hours before |
| `1792618744` | 2026-10-21 21:39:04 | **new** — 75 files, `1792550700` … `1792617300`, `1,697,351,287` bytes, Release `420082380` | no boot | no entries | `unattended-upgrade` 2026-10-21 06:12 (tzdata, python3-jwt), fifteen hours before |

Each off-calendar run is the timer's 600 s elapse after a start of the timer with no boot, as map §7 item 115 describes. What started the timer is not read by this TZ.

### 2.9 The units, memory and disk

| read | instant UTC | recorder `MainPID` / `NRestarts` / state | `MemoryCurrent` / `MemoryPeak` | pair book `MainPID` / `NRestarts` / state | `MemoryCurrent` / `MemoryPeak` |
|---|---|---|---|---|---|
| §3.3 `I still` | 03:24:37 | `4148534` / `2` / active | `12,234,752` / `271,831,040` | `2221487` / `19` / active | `6,946,816` / `48,750,592` |
| §3.10 `I still` | 04:51:37 | `4148534` / `2` / active | `129,482,752` / `271,831,040` | `2221487` / `19` / active | `4,034,560` / `49,520,640` |
| §3.11 `systemctl show` | 04:51:53 | `4148534` / `2` / active | `28,278,784` / `271,831,040` | `2221487` / `19` / active | `1,646,592` / `49,520,640` |

The archive's service read `inactive` and its timer `active (waiting)` at every read, the next run at 2026-10-23 03:00:20 UTC.

**Every `MemAvailable` and free-space read**, against the floors `116,711,424` and `4,800,000,000` bytes:

| instant UTC | read by | `MemAvailable` | free on `/dev/vda2` |
|---|---|---|---|
| 03:23:43 | §0.3 host gate | `293,007,360` | `12,500,103,168` |
| 03:25:14 | `rehearse` | `311,447,552` | `12,489,986,048` |
| 03:32:32 | `fetch` | `235,171,840` | `12,460,699,648` |
| 03:32:48 | `strikes` 1 | `242,438,144` | `12,459,044,864` |
| 03:33:00 | `strikes` 2 | `257,478,656` | `12,458,115,072` |
| 03:33:15 | `score` 1 | `260,354,048` | `12,458,053,632` |
| ~04:03 | Executor's `free -b` / `df` mid-score | `287,739,904` | `12,415,541,248` |
| 04:49:02 | `score` 2 | `268,652,544` | `12,338,057,216` |
| 04:49:09 | `rescore` | `258,691,072` | `12,338,012,160` |
| 04:51:51 | §3.11 host gate | `311,377,920` | `12,337,651,712` |
| 04:51:53 | §3.11 `free -b` | `356,196,352` available | — |

The §3.11 host gate's `MemAvailable` reads 304,080 kB. No unit stopped on its disk assert. Every assert is `free − nbytes ≥ 4,800,000,000`, and the lowest free read was `12.34` GB.

**Peak memory by mode**, the instrument's own print:

| mode | peak, bytes |
|---|---|
| `fingerprint` (§0.2, §3.1) | `31,080,448` / `31,211,520` |
| `selftest` | `52,273,152` |
| `still` (§3.3, §3.10) | `29,638,656` / `29,507,584` |
| `scratch` | `29,908,992` |
| `reclaim` (B-RECLAIM-SCRATCH) | `32,260,096` |
| `archive` (§3.4, §3.11) | `34,357,248` / `33,964,032` |
| `rehearse` | `56,459,264` |
| `fetch` | `59,604,992` |
| `strikes` ×2 | `37,699,584` / `37,703,680` |
| `score` ×2 | `60,055,552` / `41,099,264` |
| `rescore` | `59,305,984` |

The largest is `score`'s, `60,055,552`. That is `1.70 M` above the Architect's measured `58,355,712`, and half of the floor's `116,711,424` is `58,355,712`. The floor itself was met at every read (§6 item 4).

### 2.10 Every ledger line — `label-ledger.jsonl`

```
{"at":"2026-10-22T03:33:15Z","head":"fcd9ca566e9b948f0426707e7c3b5684f7f03b04","member_list_sha":"4d4a7f5f6397b63b945c0a85f8457e1cd3701a4754b5c1b3252904b1647bb9de","members":768,"mode":"score","set_sha":"df4ae686b06a24d461e554e0fbbe36192619b1404550204b65513cb85dd965d9"}
{"at":"2026-10-22T04:49:02Z","head":"fcd9ca566e9b948f0426707e7c3b5684f7f03b04","member_list_sha":"4d4a7f5f6397b63b945c0a85f8457e1cd3701a4754b5c1b3252904b1647bb9de","members":768,"mode":"score","set_sha":"df4ae686b06a24d461e554e0fbbe36192619b1404550204b65513cb85dd965d9"}
{"at":"2026-10-22T04:49:09Z","head":"fcd9ca566e9b948f0426707e7c3b5684f7f03b04","mode":"rescore","set_sha":"df4ae686b06a24d461e554e0fbbe36192619b1404550204b65513cb85dd965d9"}
```

### 2.11 Every file the run wrote, by SHA-256

Excluded, as the TZ allows: the 768 + 48 unit files (`b3-windows.txt` holds the score's, and DETERMINISM proved the rescore's equal), the downloaded streams (no unit keeps one), and the two document caches (`fetch/docs/` 94 files, `rehearsal/docs/` 6 files). The table was read at 04:52 UTC, before the report draft:

| SHA-256 | bytes | path under `/root/tz30-work/` |
|---|---|---|
| `df4ae686b06a24d461e554e0fbbe36192619b1404550204b65513cb85dd965d9` | 880811 | `b3-set.json` |
| `939f9b9863653b33135c417af391e1cac2130e2f2722903a738accbf2d73cfdc` | 224756 | `fetch/candidates.json` |
| `3b7dd4140eae89e1d88c5d450e7d67c87f5568a44963f7afc08afa5649ca04b4` | 657536 | `fetch/set.json` |
| `dc0b2f9d35aaf2faed866a08d64692c7db691bcd0890fcc720f8bd67f1d829e5` | 716 | `label-ledger.jsonl` |
| `d81c0cb60afec1811b4b60a29e948560692028d501a8e0dc015931eb1707bc3e` | 160 | `logs/00-contract-step1-pull.log` |
| `5ee341c4e26e6cc69f3d9d96cb6408d565cf0f68d65f5f8d339662e1833fd699` | 97 | `logs/00-worktree-mkdir.log` |
| `d92df6dc66eb3c63d86f563208859ce0d506d88bf2fbd2f46e3be69b8d9b313d` | 142 | `logs/01-stage.log` |
| `9b89b8fc9db90738186d8f8b8432ce8042484ef6e1aa59a9ffd0fc0af4f1cea5` | 7970 | `logs/02-I0-fingerprint.log` |
| `b5a56235daf2ee752895869af0fb609f9300aaa41e9a637b654e23b585bc63a6` | 5330 | `logs/03-host-gate.log` |
| `ae315f13b6c28404ef47a80cec63c6405eca7f67ff99380300ff45857b7410fc` | 4150 | `logs/04-refs.log` |
| `f106cbfb0771efcd7bdb3ebfdbfc3e1b6f08ada202bd37ba71a7f6a06f46e1a2` | 555 | `logs/05-branch-worktree.log` |
| `d621953fa668aa132b30077b0e0c95a566df021869a48020ea35ff752892748a` | 139 | `logs/06-stage-wt.log` |
| `d4fce34c3271f0de5ad151f8b2ea85cc1fa1e86956638bcdd065bd6524fb8602` | 7970 | `logs/07-I-fingerprint.log` |
| `bece7bfb24a12684be1a417de3ad078e11198558d9e5f30701a5db3841ee81b2` | 1009 | `logs/08-commit-push.log` |
| `466cb08e631692af1994d5f18e8128bd070d5891e7f62de1b4d185c35e6aa79f` | 63 | `logs/09-pr-create.log` |
| `5ec84e5797d2090ffd86eb2864d3ab1f89fb1039eb376c1e6d9e9c549902e771` | 6258 | `logs/10-selftest.log` |
| `0d2c56a181d4612cda0fad519b420acea5fbff56345f1ec296f7af0d655379a2` | 784 | `logs/11-still-1.log` |
| `2adbead1cd5cd5ad9be6c908167730af02ad2b92490d39018531a0dcec80306e` | 1125 | `logs/12-scratch.log` |
| `e538f6be50e4eba01a5f7f1c219740f0722f85a4ffdd4479001814af5bfbce30` | 377 | `logs/13-reclaim-scratch.log` |
| `e2a86713dc6b5398bcc4b1637602c3d9670f2eb039d59d3196b42d58565485f2` | 1061 | `logs/14-rm-scratch.log` |
| `7a95c9c97df1de1f2e0c39e4393d8252935e541cfc7bd401220bcb290325f546` | 59118 | `logs/15-archive-1.log` |
| `41940c052a4eafe41e4481e7d9a10903f364e82362eb39c6ddda8d83f2a89509` | 2058 | `logs/16-rehearse.log` |
| `c39e2e247ec903007fb4841c095a0865b829dbd67b38e469e038fd9e33f98142` | 1097 | `logs/17-fetch.log` |
| `f86b0d1c16eb30bd3fc25ab44a6ad644632bea12cea18c2303c16914c2f4da82` | 2519 | `logs/18-strikes-1.log` |
| `bfa615642452189c1e979bbd0fd744fed6be129a8af244667ff82699110b8df7` | 2510 | `logs/19-strikes-2.log` |
| `fee26592ffacd048d552a2ca51395dd64a581dff817d62d5a6793bbe1baa593b` | 7934 | `logs/20-score-1.log` |
| `582d0678ab787effd774e4466a87253669e1c688b77409bfdb2fae6561a36a9f` | 6219 | `logs/21-score-2.log` |
| `163f6471b6c92700e6e5ec5626a97254e18454eb0d6f3733b0c7499b9efaa4e5` | 872 | `logs/22-rescore.log` |
| `ca140e8e08a75d59a6c5413e640dbc5d6fc6d054bf2d11a2fd7d000e65db729b` | 820 | `logs/23-still-2.log` |
| `9b481f244b5ee0c24e60956dcb8fff1cf8a5bb7da09e6c8216386da440e54ede` | 5001 | `logs/24-host-gate-2.log` |
| `85e18aad6352b08f8220978043db2a9223c2286b2642f1165432c240991f8027` | 59118 | `logs/25-archive-2.log` |
| `4caefbc0d5433ef1dc5c7bd0cac688a3d3f45fe98bb84511317cee2d88c1a391` | 1687 | `logs/26-closing-reads.log` |
| `9803109b5300a5c2a4f3908c55b594020e03b7dce8fe1b1767a3bea2e1ea8037` | 572 | `logs/27-separation-check.log` |
| `402b378a274613153410aa068abaaa798d68d4770a22239a07442ba42411bade` | 55392 | `rehearsal/rehearsal-lines.txt` |
| `e5c24ab103a788e20897b7902d428c5dfc2f513f6d5f140f9b755f14569899b7` | 11431 | `rehearsal/rehearsal-timing.jsonl` |
| `3724aa5df21b8589949c84fc60ad35a1319c1ec1f85d2a957e7adf5e4385c11c` | 36027 | `rehearsal/set.json` |
| `c02f2a43045456097b7203de21ee1914a5c3b957bfbad8e8589ca99e70c6b947` | 10818 | `rescore/rescore-timing.jsonl` |
| `181de4d449d507d31d8a224eb53adeadcbc4ccddfd1a831d05cf306b3746d2a0` | 5079 | `score/b3-reading.json` |
| `ecf3ce88e9f7ebe17dd0bf5bf2947e379b734508e2a88d45b7d2a507a24750d5` | 2226927 | `score/b3-windows.txt` |
| `f9b2da01717b88e3daade3588b6dd56468c1e75191b39062c65f4e4b0f69b333` | 172898 | `score/score-timing.jsonl` |
| `93dbbf1c4f84553a7bc041387ef92c3c0d8747c384d383b4fcd0b247fcd131ab` | 131119 | `stage/research/tz30-nesting-b3-measure.py` |
| `142945acbb53ef7296f7ae8154147eaebe08ecef1cdac4463441a3ec68add12c` | 413 | `state.json` |

`stage/` holds §0.1's staged copy. Its bytes are Appendix A's, the same as the branch file. `wt/` is the branch worktree; it holds exactly the pushed `HEAD`, as §9's `reclaim` asserts.

---

## 3. Publication

- **Branch** `tz-30-nesting-b3-measure`. One commit `fcd9ca566e9b948f0426707e7c3b5684f7f03b04` above `c836913`, adding `research/tz30-nesting-b3-measure.py` (2,518 lines, 131,119 bytes, `93dbbf1c4f84553a7bc041387ef92c3c0d8747c384d383b4fcd0b247fcd131ab`) and nothing else.
- **Push:** through `gh`'s stored login, as §3.1 prescribes; the token in `origin`'s URL was not touched. The commit was on `origin` at `2026-10-22T03:24:19.294321725Z`, at the worktree's `HEAD`.
- **Pull request** [#29](https://github.com/seahomebatumi-ai/btc-5m-twap/pull/29), open, against `main`, head `fcd9ca5`. Not merged.
- **Release:** none created or changed. No dataset, stream or binary entered git.
- **The report**, this file, goes to `main` in one commit by §8's route.

§3.1's commands (`logs/05-branch-worktree.log`, `logs/06-stage-wt.log`, `logs/08-commit-push.log`, `logs/09-pr-create.log`):

```
From https://github.com/seahomebatumi-ai/btc-5m-twap
 * [new tag]         pairbook-streams-1792495417 -> pairbook-streams-1792495417
 * [new tag]         pairbook-streams-1792551620 -> pairbook-streams-1792551620
 * [new tag]         pairbook-streams-1792618744 -> pairbook-streams-1792618744
 * [new tag]         pairbook-streams-1792638020 -> pairbook-streams-1792638020
exit=0
Preparing worktree (new branch 'tz-30-nesting-b3-measure')
branch 'tz-30-nesting-b3-measure' set up to track 'origin/main'.
HEAD is now at c836913 Update SYSTEM-MAP.md
exit=0
/root/tz30-work/wt/research/tz30-nesting-b3-measure.py 2518 131119 93dbbf1c4f84553a7bc041387ef92c3c0d8747c384d383b4fcd0b247fcd131ab
exit=0
commit exit=0
fcd9ca566e9b948f0426707e7c3b5684f7f03b04 2026-10-22T03:24:17+00:00
 research/tz30-nesting-b3-measure.py | 2518 +++++++++++++++++++++++++++++++++++
 1 file changed, 2518 insertions(+)
A	research/tz30-nesting-b3-measure.py
2518	0	research/tz30-nesting-b3-measure.py
remote: 
remote: Create a pull request for 'tz-30-nesting-b3-measure' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-30-nesting-b3-measure        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-30-nesting-b3-measure -> tz-30-nesting-b3-measure
exit=0
From https://github.com/seahomebatumi-ai/btc-5m-twap
 * [new branch]      tz-30-nesting-b3-measure -> origin/tz-30-nesting-b3-measure
exit=0
branch 'tz-30-nesting-b3-measure' set up to track 'origin/tz-30-nesting-b3-measure'.
exit=0
2026-10-22T03:24:19.294321725Z
fcd9ca566e9b948f0426707e7c3b5684f7f03b04	refs/heads/tz-30-nesting-b3-measure
fcd9ca566e9b948f0426707e7c3b5684f7f03b04
https://github.com/seahomebatumi-ai/btc-5m-twap/pull/29
exit=0
```

**Contract §4.2's separation self-check**, run after the push and the pull request and before the report's commit (`logs/27-separation-check.log`):

```
2026-10-22T04:52:03.352959948Z
$ git rev-list origin/main | grep -c fcd9ca566e9b948f0426707e7c3b5684f7f03b04
0
$ git diff --name-only origin/main origin/tz-30-nesting-b3-measure
research/tz30-nesting-b3-measure.py
$ git diff --name-status origin/main origin/tz-30-nesting-b3-measure
A	research/tz30-nesting-b3-measure.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
grep exit=1
{"baseRefName":"main","headRefOid":"fcd9ca566e9b948f0426707e7c3b5684f7f03b04","number":29,"state":"OPEN","url":"https://github.com/seahomebatumi-ai/btc-5m-twap/pull/29"}
```

The first line prints `0`. The diff names one path. The `ls-tree` grep prints nothing (exit 1).

---

## 4. Gate

> | condition, on the eight blocks' `S_b` | reading |
> |---|---|
> | every `S_b ≥ 10` USDC | **CAPTURE** |
> | every `S_b < 10` USDC | **NO CAPTURE** |
> | otherwise | **UNDECIDABLE** |
>
> Read by `reading` inside `score`, and kept only after G-REBUILD PASS.

**G-REBUILD PASS** is the precondition: compared `0.995` of valid (floor `0.90`), equal `0.999` of compared (floor `0.98`). **The deciding number** is the largest block sum, `−1.917` USDC (block 8), below `θ = 10.000`. Every `S_b < 10`, so **B3 reads NO CAPTURE**. Nothing was tuned, and no gate was reinterpreted.

| gate | reading |
|---|---|
| G-REHEARSAL | **PASS**, 9 of 9 |
| G-SET | **PASS**, 768 members, 7 non-members before the 768th, written twice the same |
| G-REBUILD | **PASS**, `10,693 / 10,752 = 0.995`, `10,688 / 10,693 = 0.999` |
| B3 | **NO CAPTURE**, 8 of 8 blocks below `θ` |
| DETERMINISM | **PASS**, 48 of 48 |
| G-STILL | **PASS**, unchanged |

---

## 5. Validation

### V1 — fingerprint, at §0.2 and §3.1

`FINGERPRINT PASS` at both. Revision `2026-10-20-a`; anchors 6 of 6, 4 re-derived; 41 rows, with 38 of 38 `frozen` equal, 2 `tracked` and 1 `reported`; the 6 files the instrument executes are `frozen` rows. **Asserted**, inside the instrument.

### V2 — host gate

H1, H2, H3 and H4, the memory gate and the disk gate: 6 of 6 hold (§0.3). These were read from the printed block and judged by the Executor, as the TZ provides. The rest was printed.

### V3 — the file

1 of 1 hash asserted at §0.1 and again at §3.1: 2,518 lines, 131,119 bytes. The branch's diff against `origin/main` names exactly one path, `A	research/tz30-nesting-b3-measure.py`, `2518 0`. The commit on `origin` is the worktree's `HEAD`, `fcd9ca5…`. **Asserted** by the extraction script, and read from git.

### V4 — self-test

`42 of 42 checks passed`. **Asserted** (`logs/10-selftest.log`, exit 0).

### V5 — the archive's record and G-ASSETS, at §3.4 and §3.11

Both runs exited 0, so every assert held: every `set.json` against its `set` record's SHA-256, the ledger read whole, and the tags on `origin`. The ledger was 40,441 bytes, `40c413bb…`, 170 records. 17 runs, 17 complete, none halted. The latest `upload` record's credential: "the primary checkout's remote URL". 17 tags on `origin`, none missing. 1,034 windows covered, 0 missing. All 936 candidates moved. **Recorded**, as V5 says.

### V6 — G-REHEARSAL

`9 of 9`: 357 lines, SHA-256 `402b378a…` equal, and 7 of 7 variants' attempts and totals equal. **Asserted.**

### V7 — the archive's run and the walk

The archive's last window was `1792636200`, with 0 s waited. 936 candidates were considered. `FETCH` printed `{"5m document: readings": 1, "candidate": 931, "incomplete": 3, "stream: subscribed late": 1}`. **Asserted** (`considered` equals the 936 windows).

### V8 — G-SET, twice

768 members; 775 candidates considered; 7 non-members, each with its reason (§2.1). The second run printed `unchanged`. The set's SHA-256 `df4ae686…` is in `state.json`. **Asserted** (`write_once`, non-member bound, `len == 768`).

### V9 — the score, twice

- G-REBUILD's counts and reading are in §2.2.
- The lag is in §2.3, the eight blocks and the reading in §2.4.
- The second run printed `unchanged` for 2 of 2 files.
- One ledger line a run, 2 lines in all.
- The commit was on `origin` at `03:24:19.294Z` (§3.1's `ls-remote`). The first `score` line's `at` is `03:33:15Z`, the first price read of a member, 8 min 56 s later.

**Asserted:** `score` refuses a `HEAD` that `origin` does not carry; `unchanged` is a hash assert; G-REBUILD's `PASS` is asserted before `B3 READING` prints.

### V10 — DETERMINISM

`48 of 48`. **Asserted.**

### V11 — G-STILL

PASS. Unchanged from 03:24:37Z to 04:51:37Z: recorder `4148534` / `2` / active, pair book `2221487` / `19` / active. No archive run fell inside the session. **Asserted** by `still`.

### V12 — the hooks

Every mode printed `refused: 0 by this file's hook, 0 by TZ-24's`: 16 of 16 runs before B-RECLAIM-OWN. Those are 2 `fingerprint`, `selftest`, 2 `still`, `scratch`, `reclaim` (B-RECLAIM-SCRATCH), 2 `archive`, `rehearse`, `fetch`, 2 `strikes`, 2 `score` and `rescore`. B-RECLAIM-OWN's `reclaim` is quoted in V18.

### V13 — memory and disk

Every mode's printed peak is below `116,711,424`; the highest is `60,055,552`. Every `MemAvailable` read was at least `235,171,840` and every free read at least `12,337,651,712` (§2.9). No unit was stopped by its disk assert. **Asserted** per mode (`floor_check`) and per unit.

### V14 — the units' clock

See §2.7. 867 units, every one inside the idle stretch; none ended after second 590. Downloads needed 0 retries.

### V15 — contract §4.2's self-check

See §3: run at 04:52:03 UTC, after the push and the pull request and before the report's commit. First line `0`.

### V16 — §3.11's closing reads

Every read was printed: `logs/24-host-gate-2.log`, `logs/25-archive-2.log` and `logs/26-closing-reads.log`. The host gate's second read and the closing reads follow, verbatim:

```
Thu Oct 22 04:51:51 AM UTC 2026
1792644711
1
MemTotal:         978640 kB
MemAvailable:     304080 kB
SwapTotal:       3174396 kB
SwapFree:        2752920 kB
2026-08-02 07:24:32
IDX BOOT ID                          FIRST ENTRY                 LAST ENTRY
 -5 23a31fad2f064f04b9e138eac29658f3 Tue 2026-06-09 06:23:40 UTC Fri 2026-06-26 14:13:44 UTC
 -4 a38e17445ce341bc8b877be9d3d4f648 Fri 2026-06-26 14:13:52 UTC Tue 2026-07-14 16:15:10 UTC
 -3 5f4d18a6ba8041bd80e7d1e192c5ee28 Tue 2026-07-14 16:15:20 UTC Fri 2026-07-17 01:01:21 UTC
 -2 b1b399c70c6e4dcc934755f70a2ca231 Fri 2026-07-17 01:01:43 UTC Fri 2026-07-24 14:55:46 UTC
 -1 285d6962c92c407d837d1ce329b93aa4 Fri 2026-07-24 14:55:54 UTC Sun 2026-08-02 07:23:49 UTC
  0 48a803f03549473383be5baecf790d4e Sun 2026-08-02 07:24:34 UTC Thu 2026-10-22 04:51:50 UTC
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 12337651712
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json
1
3.12.3 2.5.3
16570 /root/btc-forensics/tz27-work--archive--set.json
ec71b1a7ce7db37ff29a49156006541dd5729c1df2c829c481eb64181228e4dd  /root/btc-forensics/tz27-work--archive--set.json
MainPID=4148534
Result=success
NRestarts=2
Id=btc-recorder.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Sun 2026-10-04 22:22:07 UTC

MainPID=2221487
Result=success
NRestarts=19
Id=btc-pairbook.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Thu 2026-10-22 03:03:38 UTC

MainPID=0
Result=success
NRestarts=0
Id=btc-pairbook-archive.service
ActiveState=inactive
SubState=dead
UnitFileState=static
ActiveEnterTimestamp=

Result=success
Id=btc-pairbook-archive.timer
ActiveState=active
SubState=waiting
UnitFileState=enabled
ActiveEnterTimestamp=Sun 2026-10-11 15:08:11 UTC

MainPID=0
Result=success
NRestarts=0
Id=btc-chainbook.service
ActiveState=inactive
SubState=dead
UnitFileState=disabled
ActiveEnterTimestamp=
NEXT                        LEFT LAST                              PASSED UNIT                       ACTIVATES
Fri 2026-10-23 03:00:20 UTC  22h Thu 2026-10-22 03:00:20 UTC 1h 51min ago btc-pairbook-archive.timer btc-pairbook-archive.service

1 timers listed.
-- No entries --
End-Date: 2026-10-15  06:09:16
Start-Date: 2026-10-15  06:09:18
Commandline: /usr/bin/unattended-upgrade
End-Date: 2026-10-15  06:09:19
Start-Date: 2026-10-15  06:09:21
Commandline: /usr/bin/unattended-upgrade
End-Date: 2026-10-15  06:09:21
Start-Date: 2026-10-15  06:09:23
Commandline: /usr/bin/unattended-upgrade
End-Date: 2026-10-15  06:09:24
Start-Date: 2026-10-15  06:09:26
Commandline: /usr/bin/unattended-upgrade
End-Date: 2026-10-15  06:09:27
Start-Date: 2026-10-15  06:09:29
Commandline: /usr/bin/unattended-upgrade
End-Date: 2026-10-15  06:09:29
Start-Date: 2026-10-16  06:08:05
Commandline: /usr/bin/unattended-upgrade
Upgrade: libcurl3t64-gnutls:amd64 (8.5.0-2ubuntu10.15, 8.5.0-2ubuntu10.16), libcurl4t64:amd64 (8.5.0-2ubuntu10.15, 8.5.0-2ubuntu10.16), curl:amd64 (8.5.0-2ubuntu10.15, 8.5.0-2ubuntu10.16)
End-Date: 2026-10-16  06:08:06
Start-Date: 2026-10-16  06:08:09
Commandline: /usr/bin/unattended-upgrade
Upgrade: apache2-utils:amd64 (2.4.58-1ubuntu8.16, 2.4.58-1ubuntu8.17)
End-Date: 2026-10-16  06:08:10
Start-Date: 2026-10-20  06:28:05
Commandline: /usr/bin/unattended-upgrade
Upgrade: git:amd64 (1:2.43.0-1ubuntu7.3, 1:2.43.0-1ubuntu7.4), git-man:amd64 (1:2.43.0-1ubuntu7.3, 1:2.43.0-1ubuntu7.4)
End-Date: 2026-10-20  06:28:07
Start-Date: 2026-10-20  06:28:11
Commandline: /usr/bin/unattended-upgrade
Upgrade: libxtst6:amd64 (2:1.2.3-1.1build1, 2:1.2.3-1.1ubuntu0.1)
End-Date: 2026-10-20  06:28:11
Start-Date: 2026-10-21  06:12:47
Commandline: /usr/bin/unattended-upgrade
Upgrade: tzdata:amd64 (2026c-0ubuntu0.24.04.1, 2026e-0ubuntu0.24.04.1)
End-Date: 2026-10-21  06:12:48
Start-Date: 2026-10-21  06:12:51
Commandline: /usr/bin/unattended-upgrade
Upgrade: python3-jwt:amd64 (2.7.0-1ubuntu0.3, 2.7.0-1ubuntu0.4)
End-Date: 2026-10-21  06:12:52
disabled
exit=1
inactive
exit=3
e3975b5da44c5328adf3bf3914634cd878842c73
e8b46a85d61e1a17841962846f6d3012046c2d70
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3
/root/tz29-work exit=1
/root/tz18a-svc exit=0
/root/btc-recorder-svc exit=0
/root/btc-pairbook-svc exit=0
/root/btc-pairbook-archive-svc exit=0
/var/lib/btc-pairbook-archive exit=0
1896
/root/btc-5m-twap       c836913 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/root/tz30-work/wt      fcd9ca5 [tz-30-nesting-b3-measure]
212905368	/var/lib/btc-pairbook
4978552	/var/lib/btc-pairbook-archive
131539431	/root/.claude
609225967	/root/PROJECT_GAMING_PS5
/tmp/claude-0/-root-btc-5m-twap/2f1eadf7-1958-5f4f-857d-ccf68aa47272/scratchpad
total 20
drwx------  5 root root 4096 Oct 22 03:25 .
drwx------ 25 root root 4096 Oct 22 03:22 ..
drwx------  4 root root 4096 Oct 22 03:22 2f1eadf7-1958-5f4f-857d-ccf68aa47272
drwx------  3 root root 4096 Oct 22 03:22 c498ebed-32dd-4005-9ebd-4fcce8ce6682
drwx------  3 root root 4096 Oct 21 09:37 eff3ddd1-cb45-4950-82cd-35b28b9c2c61
2026-10-22T04:51:53.667993886Z
MainPID=4148534
NRestarts=2
MemoryCurrent=28278784
MemoryPeak=271831040
ActiveState=active

MainPID=2221487
NRestarts=19
MemoryCurrent=1646592
MemoryPeak=49520640
ActiveState=active

MainPID=0
NRestarts=0
MemoryCurrent=[not set]
MemoryPeak=[not set]
ActiveState=inactive
               total        used        free      shared  buff/cache   available
Mem:      1002127360   645931008    77086720       45056   431312896   356196352
Swap:     3250581504   445132800  2805448704
15410874	/root/tz30-work
131539431	/root/.claude
{
 "set_at": "2026-10-22T03:33:10Z",
 "set_sha": "df4ae686b06a24d461e554e0fbbe36192619b1404550204b65513cb85dd965d9",
 "still": {
  "at": "2026-10-22T03:24:37Z",
  "at_ns": 1792639477371659358,
  "units": {
   "pairbook": {
    "ActiveState": "active",
    "MainPID": "2221487",
    "NRestarts": "19"
   },
   "recorder": {
    "ActiveState": "active",
    "MainPID": "4148534",
    "NRestarts": "2"
   }
  }
 }
}
{"at":"2026-10-22T03:33:15Z","head":"fcd9ca566e9b948f0426707e7c3b5684f7f03b04","member_list_sha":"4d4a7f5f6397b63b945c0a85f8457e1cd3701a4754b5c1b3252904b1647bb9de","members":768,"mode":"score","set_sha":"df4ae686b06a24d461e554e0fbbe36192619b1404550204b65513cb85dd965d9"}
{"at":"2026-10-22T04:49:02Z","head":"fcd9ca566e9b948f0426707e7c3b5684f7f03b04","member_list_sha":"4d4a7f5f6397b63b945c0a85f8457e1cd3701a4754b5c1b3252904b1647bb9de","members":768,"mode":"score","set_sha":"df4ae686b06a24d461e554e0fbbe36192619b1404550204b65513cb85dd965d9"}
{"at":"2026-10-22T04:49:09Z","head":"fcd9ca566e9b948f0426707e7c3b5684f7f03b04","mode":"rescore","set_sha":"df4ae686b06a24d461e554e0fbbe36192619b1404550204b65513cb85dd965d9"}
```

### V17 — §9's `reclaim` runs

**B-RECLAIM-SCRATCH**, run after §3.3 and before §3.4 (`logs/13-reclaim-scratch.log`):

```
[2026-10-22T03:24:49Z] reclaim: 2636 report tokens; forensic store holds 1896 files
[2026-10-22T03:24:49Z] RECLAIM PASS: 10 files considered, 0 named by a report, 0 kept by name, 0 copied, 0 already held; forensic store 1896 -> 1896 files
[2026-10-22T03:24:49Z] peak memory of this run: 32260096 bytes
[2026-10-22T03:24:49Z] refused: 0 by this file's hook, 0 by TZ-24's
exit=0
```

`I scratch` named five directories earlier and two live (`logs/12-scratch.log`):

```
[2026-10-22T03:24:37Z] running 2113303 started 2026-10-21T09:37:15Z claude
[2026-10-22T03:24:37Z] running 2113313 started 2026-10-21T09:37:17Z claude
[2026-10-22T03:24:37Z] running 2223043 started 2026-10-22T03:22:17Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-10-22T03:24:37Z] 46827096-4c4d-4533-b0f6-e40cc63578f6 born 2026-10-21T09:34:40Z: earlier
[2026-10-22T03:24:37Z] 6a6870c2-3843-4a2b-83cf-b2f45c5500a1 born 2026-10-20T04:24:47Z: earlier
[2026-10-22T03:24:37Z] 6e88615c-345d-5a08-be99-6375cc1a1073 born 2026-10-21T09:25:17Z: earlier
[2026-10-22T03:24:37Z] 7a160398-f4cf-54ee-b771-c3006d558bde born 2026-10-20T04:24:48Z: earlier
[2026-10-22T03:24:37Z] c498ebed-32dd-4005-9ebd-4fcce8ce6682 born 2026-10-22T03:22:17Z: live, process [2223043]
[2026-10-22T03:24:37Z] c79ceacd-d598-415d-89bf-67860a65609f born 2026-10-21T09:25:15Z: earlier
[2026-10-22T03:24:37Z] eff3ddd1-cb45-4950-82cd-35b28b9c2c61 born 2026-10-21T09:37:21Z: live, process [2113303, 2113313]
[2026-10-22T03:24:37Z] peak memory of this run: 29908992 bytes
[2026-10-22T03:24:37Z] refused: 0 by this file's hook, 0 by TZ-24's
exit=0
```

The removals were one `rm -rf` and one `test -e` per directory (`logs/14-rm-scratch.log`). **None was refused by the session's classifier.**

```
2026-10-22T03:25:09.360919469Z
rm -rf /tmp/claude-0/-root-btc-5m-twap/46827096-4c4d-4533-b0f6-e40cc63578f6; echo "exit=$?"  -> exit=0 (run 03:24:5x UTC, one command each, none refused)
test -e 46827096-4c4d-4533-b0f6-e40cc63578f6 exit=1
rm -rf /tmp/claude-0/-root-btc-5m-twap/6a6870c2-3843-4a2b-83cf-b2f45c5500a1; echo "exit=$?"  -> exit=0 (run 03:24:5x UTC, one command each, none refused)
test -e 6a6870c2-3843-4a2b-83cf-b2f45c5500a1 exit=1
rm -rf /tmp/claude-0/-root-btc-5m-twap/6e88615c-345d-5a08-be99-6375cc1a1073; echo "exit=$?"  -> exit=0 (run 03:24:5x UTC, one command each, none refused)
test -e 6e88615c-345d-5a08-be99-6375cc1a1073 exit=1
rm -rf /tmp/claude-0/-root-btc-5m-twap/7a160398-f4cf-54ee-b771-c3006d558bde; echo "exit=$?"  -> exit=0 (run 03:24:5x UTC, one command each, none refused)
test -e 7a160398-f4cf-54ee-b771-c3006d558bde exit=1
rm -rf /tmp/claude-0/-root-btc-5m-twap/c79ceacd-d598-415d-89bf-67860a65609f; echo "exit=$?"  -> exit=0 (run 03:24:5x UTC, one command each, none refused)
test -e c79ceacd-d598-415d-89bf-67860a65609f exit=1
```

`c498ebed-…`, live by process `2223043`, this session's own, was kept, and so was `eff3ddd1-…`, live by `2113303` and `2113313`. Map §3 names TZ-29's pair, `7a160398-…` and `6a6870c2-…`; both were among the five removed. The other three, born 2026-10-21 09:25–09:34 UTC, came from sessions on the host after TZ-29; no report names them.

**B-RECLAIM-OWN**, below in V18.

### V18 — §9's removals

B-RECLAIM-OWN ran last, after §3.11 and with this report drafted. Its output was written to no file and is quoted verbatim from the session. Each line ran as its own command, and **none was refused by the session's classifier.**

```
$ cd /root/tz30-work && I reclaim /root/tz30-work; echo "exit=$?"
[2026-10-22T04:55:21Z] reclaim: 2746 report tokens; forensic store holds 1896 files
[2026-10-22T04:55:21Z] reclaim: /root/tz30-work/wt skipped: no file but its HEAD's, and HEAD fcd9ca566e9b948f0426707e7c3b5684f7f03b04 is its upstream's
[2026-10-22T04:55:21Z] R copied df4ae686b06a24d461e554e0fbbe36192619b1404550204b65513cb85dd965d9 /root/btc-forensics/tz30-work--b3-set.json
[2026-10-22T04:55:21Z] R copied dc0b2f9d35aaf2faed866a08d64692c7db691bcd0890fcc720f8bd67f1d829e5 /root/btc-forensics/tz30-work--label-ledger.jsonl
[2026-10-22T04:55:21Z] R copied 142945acbb53ef7296f7ae8154147eaebe08ecef1cdac4463441a3ec68add12c /root/btc-forensics/tz30-work--state.json
[2026-10-22T04:55:21Z] R copied 939f9b9863653b33135c417af391e1cac2130e2f2722903a738accbf2d73cfdc /root/btc-forensics/tz30-work--fetch--candidates.json
[2026-10-22T04:55:21Z] R copied 3b7dd4140eae89e1d88c5d450e7d67c87f5568a44963f7afc08afa5649ca04b4 /root/btc-forensics/tz30-work--fetch--set.json
[2026-10-22T04:55:21Z] R copied d81c0cb60afec1811b4b60a29e948560692028d501a8e0dc015931eb1707bc3e /root/btc-forensics/tz30-work--logs--00-contract-step1-pull.log
[2026-10-22T04:55:21Z] R copied 5ee341c4e26e6cc69f3d9d96cb6408d565cf0f68d65f5f8d339662e1833fd699 /root/btc-forensics/tz30-work--logs--00-worktree-mkdir.log
[2026-10-22T04:55:21Z] R copied d92df6dc66eb3c63d86f563208859ce0d506d88bf2fbd2f46e3be69b8d9b313d /root/btc-forensics/tz30-work--logs--01-stage.log
[2026-10-22T04:55:21Z] R copied 9b89b8fc9db90738186d8f8b8432ce8042484ef6e1aa59a9ffd0fc0af4f1cea5 /root/btc-forensics/tz30-work--logs--02-I0-fingerprint.log
[2026-10-22T04:55:21Z] R copied b5a56235daf2ee752895869af0fb609f9300aaa41e9a637b654e23b585bc63a6 /root/btc-forensics/tz30-work--logs--03-host-gate.log
[2026-10-22T04:55:21Z] R copied ae315f13b6c28404ef47a80cec63c6405eca7f67ff99380300ff45857b7410fc /root/btc-forensics/tz30-work--logs--04-refs.log
[2026-10-22T04:55:21Z] R copied f106cbfb0771efcd7bdb3ebfdbfc3e1b6f08ada202bd37ba71a7f6a06f46e1a2 /root/btc-forensics/tz30-work--logs--05-branch-worktree.log
[2026-10-22T04:55:21Z] R copied d621953fa668aa132b30077b0e0c95a566df021869a48020ea35ff752892748a /root/btc-forensics/tz30-work--logs--06-stage-wt.log
[2026-10-22T04:55:21Z] R copied d4fce34c3271f0de5ad151f8b2ea85cc1fa1e86956638bcdd065bd6524fb8602 /root/btc-forensics/tz30-work--logs--07-I-fingerprint.log
[2026-10-22T04:55:21Z] R copied bece7bfb24a12684be1a417de3ad078e11198558d9e5f30701a5db3841ee81b2 /root/btc-forensics/tz30-work--logs--08-commit-push.log
[2026-10-22T04:55:21Z] R copied 466cb08e631692af1994d5f18e8128bd070d5891e7f62de1b4d185c35e6aa79f /root/btc-forensics/tz30-work--logs--09-pr-create.log
[2026-10-22T04:55:21Z] R copied 5ec84e5797d2090ffd86eb2864d3ab1f89fb1039eb376c1e6d9e9c549902e771 /root/btc-forensics/tz30-work--logs--10-selftest.log
[2026-10-22T04:55:21Z] R copied 0d2c56a181d4612cda0fad519b420acea5fbff56345f1ec296f7af0d655379a2 /root/btc-forensics/tz30-work--logs--11-still-1.log
[2026-10-22T04:55:21Z] R copied 2adbead1cd5cd5ad9be6c908167730af02ad2b92490d39018531a0dcec80306e /root/btc-forensics/tz30-work--logs--12-scratch.log
[2026-10-22T04:55:21Z] R copied e538f6be50e4eba01a5f7f1c219740f0722f85a4ffdd4479001814af5bfbce30 /root/btc-forensics/tz30-work--logs--13-reclaim-scratch.log
[2026-10-22T04:55:21Z] R copied e2a86713dc6b5398bcc4b1637602c3d9670f2eb039d59d3196b42d58565485f2 /root/btc-forensics/tz30-work--logs--14-rm-scratch.log
[2026-10-22T04:55:21Z] R copied 7a95c9c97df1de1f2e0c39e4393d8252935e541cfc7bd401220bcb290325f546 /root/btc-forensics/tz30-work--logs--15-archive-1.log
[2026-10-22T04:55:21Z] R copied 41940c052a4eafe41e4481e7d9a10903f364e82362eb39c6ddda8d83f2a89509 /root/btc-forensics/tz30-work--logs--16-rehearse.log
[2026-10-22T04:55:21Z] R copied c39e2e247ec903007fb4841c095a0865b829dbd67b38e469e038fd9e33f98142 /root/btc-forensics/tz30-work--logs--17-fetch.log
[2026-10-22T04:55:21Z] R copied f86b0d1c16eb30bd3fc25ab44a6ad644632bea12cea18c2303c16914c2f4da82 /root/btc-forensics/tz30-work--logs--18-strikes-1.log
[2026-10-22T04:55:21Z] R copied bfa615642452189c1e979bbd0fd744fed6be129a8af244667ff82699110b8df7 /root/btc-forensics/tz30-work--logs--19-strikes-2.log
[2026-10-22T04:55:21Z] R copied fee26592ffacd048d552a2ca51395dd64a581dff817d62d5a6793bbe1baa593b /root/btc-forensics/tz30-work--logs--20-score-1.log
[2026-10-22T04:55:21Z] R copied 582d0678ab787effd774e4466a87253669e1c688b77409bfdb2fae6561a36a9f /root/btc-forensics/tz30-work--logs--21-score-2.log
[2026-10-22T04:55:21Z] R copied 163f6471b6c92700e6e5ec5626a97254e18454eb0d6f3733b0c7499b9efaa4e5 /root/btc-forensics/tz30-work--logs--22-rescore.log
[2026-10-22T04:55:21Z] R copied ca140e8e08a75d59a6c5413e640dbc5d6fc6d054bf2d11a2fd7d000e65db729b /root/btc-forensics/tz30-work--logs--23-still-2.log
[2026-10-22T04:55:21Z] R copied 9b481f244b5ee0c24e60956dcb8fff1cf8a5bb7da09e6c8216386da440e54ede /root/btc-forensics/tz30-work--logs--24-host-gate-2.log
[2026-10-22T04:55:21Z] R copied 85e18aad6352b08f8220978043db2a9223c2286b2642f1165432c240991f8027 /root/btc-forensics/tz30-work--logs--25-archive-2.log
[2026-10-22T04:55:21Z] R copied 4caefbc0d5433ef1dc5c7bd0cac688a3d3f45fe98bb84511317cee2d88c1a391 /root/btc-forensics/tz30-work--logs--26-closing-reads.log
[2026-10-22T04:55:21Z] R copied 9803109b5300a5c2a4f3908c55b594020e03b7dce8fe1b1767a3bea2e1ea8037 /root/btc-forensics/tz30-work--logs--27-separation-check.log
[2026-10-22T04:55:21Z] R copied 402b378a274613153410aa068abaaa798d68d4770a22239a07442ba42411bade /root/btc-forensics/tz30-work--rehearsal--rehearsal-lines.txt
[2026-10-22T04:55:21Z] R copied e5c24ab103a788e20897b7902d428c5dfc2f513f6d5f140f9b755f14569899b7 /root/btc-forensics/tz30-work--rehearsal--rehearsal-timing.jsonl
[2026-10-22T04:55:21Z] R copied 3724aa5df21b8589949c84fc60ad35a1319c1ec1f85d2a957e7adf5e4385c11c /root/btc-forensics/tz30-work--rehearsal--set.json
[2026-10-22T04:55:21Z] R copied c02f2a43045456097b7203de21ee1914a5c3b957bfbad8e8589ca99e70c6b947 /root/btc-forensics/tz30-work--rescore--rescore-timing.jsonl
[2026-10-22T04:55:21Z] R copied 181de4d449d507d31d8a224eb53adeadcbc4ccddfd1a831d05cf306b3746d2a0 /root/btc-forensics/tz30-work--score--b3-reading.json
[2026-10-22T04:55:22Z] R copied ecf3ce88e9f7ebe17dd0bf5bf2947e379b734508e2a88d45b7d2a507a24750d5 /root/btc-forensics/tz30-work--score--b3-windows.txt
[2026-10-22T04:55:22Z] R copied f9b2da01717b88e3daade3588b6dd56468c1e75191b39062c65f4e4b0f69b333 /root/btc-forensics/tz30-work--score--score-timing.jsonl
[2026-10-22T04:55:22Z] R copied 93dbbf1c4f84553a7bc041387ef92c3c0d8747c384d383b4fcd0b247fcd131ab /root/btc-forensics/tz30-work--stage--research--tz30-nesting-b3-measure.py
[2026-10-22T04:55:22Z] RECLAIM PASS: 958 files considered, 42 named by a report, 0 kept by name, 42 copied, 0 already held; forensic store 1896 -> 1938 files
[2026-10-22T04:55:22Z] peak memory of this run: 33914880 bytes
[2026-10-22T04:55:22Z] refused: 0 by this file's hook, 0 by TZ-24's
exit=0
$ git -C /root/btc-5m-twap worktree remove /root/tz30-work/wt; echo "exit=$?"
exit=0
$ rm -rf /root/tz30-work; echo "exit=$?"
exit=0
$ test -e /root/tz30-work; echo "exit=$?"
exit=1
$ git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
/root/btc-5m-twap       c836913 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
$ find /root/btc-forensics -type f | wc -l
1938
$ df -B1 --output=source,size,avail /var/lib/btc-recorder
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 12347899904
```

**V17 counts:** 958 files considered, 42 named by a report, 0 kept by name, 42 copied, 0 already held. The store went from `1,896` to `1,938`, equal to before plus the copies. The 42 include `state.json`, `label-ledger.jsonl`, `b3-set.json` and the 28 logs. The `reclaim` counts these under "named by a report" first, since this draft prints each one's hash, and so it prints `0 kept by name`.

**V18:**
- `git worktree remove` without `--force`: exit `0`.
- `test -e /root/tz30-work`: exit `1`.
- Each of B-RECLAIM-SCRATCH's five directories: `test -e` exit `1` (V17).
- `git worktree list` names `/root/btc-5m-twap` and `/root/btc-recorder-svc`, and nothing else.
- The branch `tz-30-nesting-b3-measure` stays on `origin` and as a local ref.
- `/root/btc-recorder-svc/`, `/root/btc-pairbook-svc/`, `/root/btc-pairbook-archive-svc/`, `/root/tz18a-svc/`, the three capture roots, the archive's state and the forensic store were not touched.
- This session's own directory, `2f1eadf7-…` (born with its process `2223043` at 03:22:17 UTC, beside `c498ebed-…`), is the next TZ's to reclaim.

---

## 6. What could not be implemented as written

1. **The run took place a day later than the TZ's schedule.** It ran on 2026-10-22 from 03:22 UTC; the "When" paragraph plans it for 2026-10-21. By then the archive had run three more times: calendar runs `1792551620` and `1792638020`, and the off-calendar `1792618744`. So `fetch` waited 0 s and `ls-remote` printed 57 lines rather than 55. No candidate's data was affected: every candidate was moved by the run of 2026-10-21 03:00:20 or earlier. The session's §0.3 started at 03:23:43, 20 minutes after today's calendar run had restarted the pair book at 03:03:38. The instrument's calendar guard held nothing, because the first unit started after 03:25.
2. **`state.json`'s `set_at` holds the second `strikes` run's instant.** The first `strikes` run wrote the set at 03:33:00Z. The second run printed `unchanged` for `b3-set.json` and wrote `set_at` `03:33:10Z` into `state.json` with the same `set_sha`, as `mode_strikes` does on every run. Both instants precede the first price read, 03:33:15Z. The first instant is recorded in `logs/18-strikes-1.log` and the second in `state.json` `142945ac…`.
3. **Commands whose output went to the session and not to `logs/`.** §0.0 asks that every command's output go to `logs/`.
   - Contract §1's `git pull`, and `mkdir` before `logs/` existed: `logs/00-*.log` re-record their state and output.
   - The single-directory `rm -rf` and `test -e` lines of B-RECLAIM-SCRATCH, each run as its own command: their outputs are re-recorded in `logs/14-rm-scratch.log`.
   - The Executor's own reads while the score ran and while drafting:
     - `tail -3` of `score/score-timing.jsonl`, with `free -b` and `df` at about 04:03 UTC. These are counts, times and bytes.
     - Greps of the logs.
     - A read of `fetch/candidates.json`'s statuses.
     - Greps of the unit files' `rebuild` lines for §2.2's unequal instants and unseeded counts.
     - **`head -c 1500` of one unit file, `score/units/1791706500.txt`.**
4. **§2 item 10 was not kept at one read.** The `head -c 1500` in item 3 printed the first member's unit lines to the session's terminal. Those lines are its seven variants' shares, ceilings and P&L, its `D` and `D̂`, and its rebuild counts. Claude Code keeps the terminal's transcript under `/root/.claude/`, outside `/root/tz30-work/`, so a single member's figures were written outside the work tree. That member is `1791706500`, block 1's first; its figures are in the forensic store's `b3-windows.txt` too. No other single member's price, size or side left the tree. The report quotes only what item 10 allows: the barred diagnostics' extremes and most influential members, and the unequal replies by member and instant.
5. **`score`'s peak memory, `60,055,552` bytes, is above the Architect's largest measured peak, `58,355,712`**, on which §0.4's floor was set at twice that. The floor held at every read: the lowest `MemAvailable` was `235,171,840`. This is recorded, not gating.
6. **B-RECLAIM-SCRATCH removed three directories map §3 does not name.** They are `46827096-…`, `6e88615c-…` and `c79ceacd-…`, born 2026-10-21 09:25–09:34 UTC. `I scratch` named them earlier by its rule, and §9 removes every directory so named. They came from sessions on the host after TZ-29 that no report names. `reclaim` found no file in them named by a report. Map §3's two `claude` processes, `337573` and `337576`, are no longer running. Two later ones, `2113303` and `2113313`, started 2026-10-21 09:37; their directory `eff3ddd1-…` was named live and kept.
7. **The off-calendar run `1792618744`**, 2026-10-21 21:39:04 UTC, is new since the map. No boot and no timer journal entry accompany it, and §0.3's package history shows nothing near it. This is recorded, as §3.4 asks; its cause is not read by this TZ.

Nothing else: every step of §3 ran in order, every gate passed or read as stated, and no threshold, rule or test was changed.
