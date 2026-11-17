# TZ-46 report — the capture's room

**TZ:** `CryptoTZ/TZ-46-capture-room.md` (upload `13f3143`, the one commit on `main`'s first-parent line above `53e5690`). **Executor model:** Claude Opus 5.5, the model the TZ names. **Run:** 2026-11-17, from 14:14:56 to about 17:10 UTC, on the capture host (`vultr`, `/dev/vda2`). **Result:** every gate PASS — FINGERPRINT, NUMBER 2 of 2, SELFTEST 29 checks, G-FORENSIC 47 of 47, G-PAIR 8 of 8, G-TIMER 11 of 11 (twice), FIRST 4 of 4, G-STILL, G-ROOM (margin 2,908,396,574 bytes). No block was refused by the session's classifier; the Executor ran every block itself, and none was run by the Boss. Branch `tz-46-capture-room` at `c9d1071`, PR #46. Under PASS, no block of §4.8 ran.

## 0. Fingerprint

`SYSTEM-MAP.md`: revision **`2026-11-16-a`**, 2,122 lines, 624,694 bytes, SHA-256 `f7df7b839d7f65259d51f23db6e63277a68e4e0152ff1c676156117d705bdcea`. The anchors as the map holds them and as the instrument asserts them: `A1` `229a944f2d51`, `A2` `6c5089330629`, `A3` `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable`, `A4` `437b45ea196b`, `A5` `0f6c90451cbd`, `A6` `729f0bcdbee3`. `A2`, `A4`, `A5` and `A6` were re-derived from their files' SHA-256 (§5 V1). `I0 fingerprint` at 14:15:48Z and `I fingerprint` at 14:16:50Z both printed `FINGERPRINT PASS: revision 2026-11-16-a; anchors 6 of 6, 4 re-derived; rows 64: frozen 61 of 61 equal, tracked 2, reported 1`.

The table below has every row of map §0's table, as `fingerprint` printed it from the primary checkout at `13f3143`:

| path | lines | bytes | SHA-256 | class |
|---|---|---|---|---|
| `SYSTEM-MAP.md` | 2122 | 624694 | `f7df7b839d7f65259d51f23db6e63277a68e4e0152ff1c676156117d705bdcea` | reported |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11128 | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | frozen equal |
| `research/twap-divergence.py` | 1135 | 50928 | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | frozen equal |
| `research/selftest-twap-divergence.py` | 376 | 16736 | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | frozen equal |
| `research/tz02-distribution.py` | 334 | 14511 | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | tracked |
| `research/pfair.py` | 441 | 19357 | `729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68` | frozen equal |
| `research/selftest-pfair.py` | 619 | 32559 | `b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa` | frozen equal |
| `research/tz06-calibration.py` | 577 | 27138 | `715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f` | frozen equal |
| `research/tz07a-variance-time.py` | 623 | 28414 | `513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771` | frozen equal |
| `research/tz07b-settlement-dispersion.py` | 515 | 24926 | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` | frozen equal |
| `research/tz08a-out-of-sample.py` | 745 | 38822 | `37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c` | frozen equal |
| `research/tz09-disk-inventory.py` | 894 | 41004 | `b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6` | frozen equal |
| `research/tz10b-sigma-or-link.py` | 1224 | 61018 | `406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088` | frozen equal |
| `research/tz11a-student-link.py` | 1231 | 64732 | `0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839` | frozen equal |
| `research/tz12-sized-gate.py` | 1157 | 61637 | `d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999` | frozen equal |
| `research/tz13-sized-gate-test3.py` | 1074 | 53901 | `a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd` | frozen equal |
| `research/tz14-quote-inventory.py` | 2124 | 109972 | `978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02` | frozen equal |
| `research/tz15-phase2-gate.py` | 1517 | 73799 | `66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3` | frozen equal |
| `research/tz16a-phase2-decisive-gate.py` | 2198 | 111192 | `3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125` | frozen equal |
| `research/tz17-settlement-chain.py` | 1102 | 38622 | `e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92` | frozen equal |
| `research/tz18a-chainbook-capture.py` | 1683 | 69517 | `e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae` | frozen equal |
| `research/tz20-capture-under-systemd.py` | 771 | 36528 | `104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7` | frozen equal |
| `research/tz21-recorder-memory.py` | 1284 | 59009 | `d6d2dc195809f2160fda7856980d8ccfbf0006ba0836943ff789c877f9d5795f` | frozen equal |
| `research/tz23-maker-m0.py` | 1184 | 54885 | `6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f` | frozen equal |
| `research/tz24-nesting-b2.py` | 1535 | 76142 | `4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b` | frozen equal |
| `research/tz26-nesting-b3-capture.py` | 2492 | 118466 | `caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec` | frozen equal |
| `research/tz27-pairbook-archive.py` | 2078 | 106284 | `2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673` | frozen equal |
| `research/tz28-pairbook-archive-timer.py` | 1438 | 74576 | `46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4` | frozen equal |
| `research/tz29-maker-m0-second-look.py` | 1225 | 68959 | `18defff93d08c13ea4638a518c88a3fec5541fcf53fb6827451e727f2204d905` | frozen equal |
| `research/tz30-nesting-b3-measure.py` | 2518 | 131119 | `93dbbf1c4f84553a7bc041387ef92c3c0d8747c384d383b4fcd0b247fcd131ab` | frozen equal |
| `research/tz31-who-earns.py` | 1523 | 84775 | `7073188c8fbaa19568e8c6e4d6379e40ea57cf2a1341ebde0ea6a08f2c544765` | frozen equal |
| `research/tz32-our-quoting.py` | 2576 | 138209 | `6ec367e6ed995b315063d2d808dd6a3995878011afd76abfbb7b106b645a9c61` | frozen equal |
| `research/tz33-reward-book-capture.py` | 3542 | 175160 | `a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670` | frozen equal |
| `research/tz34-rewardbook-archive-timer.py` | 1791 | 99388 | `1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72` | frozen equal |
| `research/tz35-advisor-deploy.py` | 802 | 42049 | `d50787db5113c3f748806a60a3e71211b665cb5235296e43d0e9a747a529e6f5` | frozen equal |
| `research/tz36-advisor-trust.py` | 582 | 32925 | `a0fb9d53afe435d37354862eb8fd299256bf551fdbdb25a5c828d2cc7376d4f5` | frozen equal |
| `research/tz37-capital-allocation.py` | 808 | 51269 | `eec1f30b971ed1d6db31e27eb0c321276c1b107a1654e013996d023b1a6a04eb` | frozen equal |
| `research/tz38-adv3-pit-validation.py` | 1782 | 90181 | `579474b65329662f7bed735994381241a928a2c65a726cec3f933dc7afd4427b` | frozen equal |
| `research/tz39-advisor-checks.py` | 1139 | 73892 | `18294b0916d77b226083a18f9521f06e2fddb423bbc947a2e1100fd42b2980f3` | frozen equal |
| `research/tz40-advisor-strong.py` | 1436 | 95474 | `4403b27185f7e9aaa090dedfca457af6c4f70b6b020f0d2fcd9f9fbb96b6054b` | frozen equal |
| `research/tz42-advisor-registry.py` | 2088 | 134077 | `b6c45490b2f86f5c4678c645041ef1556b1199a6bc814470de904aedf7f5105f` | frozen equal |
| `research/tz43-l0-our-quote.py` | 3056 | 152905 | `48c3550b3f9a990fa8bc43ad8464b181ec2eb0a086b3b6f3a0ceed52da4a30cf` | frozen equal |
| `research/tz44-l0-inputs-release.py` | 1616 | 90703 | `0b78807d9c5dec087138b0c9a329cb8c976157ab5c8a3fd4deee7cb31e89e190` | frozen equal |
| `research/tz45-l0-rule-w.py` | 4299 | 233655 | `4720e78573e54b1325dd24af7c30e0de59bfb4c1879d309a23fa6bab6b32d2d4` | frozen equal |
| `research/recorder/recorder.py` | 651 | 27821 | `0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7` | frozen equal |
| `research/recorder/config.py` | 112 | 4773 | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | frozen equal |
| `research/recorder/manifest.py` | 254 | 10002 | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | frozen equal |
| `research/recorder/analyze.py` | 813 | 34705 | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` | frozen equal |
| `research/recorder/probe.py` | 227 | 9324 | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | frozen equal |
| `research/recorder/selftest.py` | 573 | 30591 | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` | frozen equal |
| `deploy/systemd/btc-recorder.service` | 23 | 707 | `3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1` | frozen equal |
| `deploy/systemd/btc-chainbook.service` | 22 | 724 | `a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2` | frozen equal |
| `deploy/systemd/btc-pairbook.service` | 22 | 761 | `ba02fe4175b961c387ea8066eb084704e69efc7fd0a48d8f623a0198334f8dd8` | frozen equal |
| `deploy/systemd/btc-pairbook-archive.service` | 17 | 794 | `2e7fd45382af3da3b2ec29ced8d69870ef3d4481da4c6f327b90fc6cb5af78e7` | frozen equal |
| `deploy/systemd/btc-pairbook-archive.timer` | 13 | 417 | `07581f4f331fbf9d2a1113cac42a2872d65ac69a872991bff7d2bda235eac913` | frozen equal |
| `deploy/systemd/btc-rewardbook.service` | 23 | 817 | `7691720c7b2261a606af54bfa20b5068b89455ea54512c55dde861d6d8063bec` | frozen equal |
| `deploy/systemd/btc-rewardbook-archive.service` | 17 | 810 | `a9abb1f092b3fb8359d37ea88df00dca8557d0f0482d04c12f0fbdd32601e33f` | frozen equal |
| `deploy/systemd/btc-rewardbook-archive.timer` | 13 | 428 | `bf5af0252c420d8db1579b82e5da21472cdb6bc871fa8035ecf6f1edc9720a0f` | frozen equal |
| `deploy/systemd/adv3-bot.service` | 27 | 863 | `82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66` | frozen equal |
| `advisor/RULE-ADV-3.txt` | 33 | 3203 | `ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169` | frozen equal |
| `advisor/adv3.py` | 895 | 51834 | `81ef0112d3fe4b86566e51a51aab924d9776ff37a927e65982ecb0bb7c1f34e1` | frozen equal |
| `advisor/adv3-bot.py` | 2548 | 157438 | `c3d9fff54f3585cfc4c33b5f7e1f93b390e62b03e0b4725fee2d6fdda6d04c11` | frozen equal |
| `advisor/selftest-adv3.py` | 256 | 19111 | `6f29b82f2b2ca82cd2ff4bbb370e032354dbb4743497330530777429b3af7398` | frozen equal |
| `.gitignore` | 5 | 252 | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | tracked |

## 1. Input

**Nothing was re-collected.** Every read was of the host as it stood and of GitHub, anonymously.

- **This TZ**, at `13f3143`. §0.1's script extracted Appendix A at the hashes of its table. Into the stage both files were `created`. Into the worktree the instrument was `created` and the timer `replaced` over TZ-34's `bf5af025…`:
```
/root/tz46-work/stage/deploy/systemd/btc-rewardbook-archive.timer 12 435 7b0804285af6987340838bd59573897d013cf97edc5d4132cda7f3f9ba3e3824 created
/root/tz46-work/stage/research/tz46-capture-room.py 1644 88254 363b269c462d14da1656feb7bad92fec43adb1593209131fe5ca6e5c9f6755f6 created
exit=0
```
```
Tue Nov 17 02:16:50 PM UTC 2026
Preparing worktree (new branch 'tz-46-capture-room')
branch 'tz-46-capture-room' set up to track 'origin/main'.
HEAD is now at 13f3143 Add files via upload
worktree exit=0
/root/tz46-work/wt/deploy/systemd/btc-rewardbook-archive.timer 12 435 7b0804285af6987340838bd59573897d013cf97edc5d4132cda7f3f9ba3e3824 replaced
/root/tz46-work/wt/research/tz46-capture-room.py 1644 88254 363b269c462d14da1656feb7bad92fec43adb1593209131fe5ca6e5c9f6755f6 created
exit=0
```
- **The readiness read, §0.0.** It was first run in the session at 14:14:56Z (`ready=1`, second 51296, 8,731,217,920 bytes free). That was before `/root/tz46-work` existed. It was run again into `00-ready.log`:
```
Tue Nov 17 02:15:41 PM UTC 2026
the rewardbook archive: 195 records; its last run 1794879020, complete; halted False
the pairbook archive: 585 records; its last run 1794884420, complete; halted False
btc-recorder.service active enabled
btc-pairbook.service active enabled
btc-rewardbook.service active enabled
adv3-bot.service active enabled
btc-pairbook-archive.timer active enabled
btc-rewardbook-archive.timer active enabled
ready=1: second 51341 of the day, the band 27000 to 63000; 8730017792 bytes free, 7600000000 needed; at 1794924941 2026-11-17T14:15:41Z
```
- **The host gate, §0.3**, quoted whole. H1 printed one path. H2: `/dev/vda2`, `31612203008`, `grep -c` `4`. H3: `3.12.3`. H4: the five `cmp` exited `0`; `commit.txt` read `6a61525…` (the reward book's archive) and `d8194fd…` (the pair book's); the four `sha256sum` equal map §0's rows. H5: the four units are `active`/`enabled` and both timers `active`/`enabled`. The memory gate's read was 562,360,320 ≥ 133,073,162. The disk gate: `avail` 8,729,411,584 ≥ 7,600,000,000. **12 of 12.**
```
Tue Nov 17 02:16:04 PM UTC 2026
1794924964
2026-08-02 07:24:32
IDX BOOT ID                          FIRST ENTRY                 LAST ENTRY
  0 48a803f03549473383be5baecf790d4e Sun 2026-08-23 13:40:30 UTC Tue 2026-11-17 14:16:00 UTC
1
MemTotal:         978640 kB
MemAvailable:     304292 kB
SwapTotal:       3174396 kB
SwapFree:        2460004 kB
Filesystem       1B-blocks      Avail
/dev/vda2      31612203008 8729411584
/var/lib/btc-recorder/btc-updown-5m/1794396600/manifest.json
4
3.12.3
btc-pairbook.service cmp exit=0
btc-pairbook-archive.service cmp exit=0
btc-pairbook-archive.timer cmp exit=0
btc-rewardbook-archive.service cmp exit=0
btc-rewardbook-archive.timer cmp exit=0
6a615257277d3c94dafd4d39783499560a344648
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3
1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72  /root/btc-rewardbook-archive-svc/tz34-rewardbook-archive-timer.py
46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4  /root/btc-pairbook-archive-svc/tz28-pairbook-archive-timer.py
a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670  /root/btc-rewardbook-svc/tz33-reward-book-capture.py
caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec  /root/btc-pairbook-svc/tz26-nesting-b3-capture.py
MainPID=1555954
Result=success
NRestarts=0
Id=btc-recorder.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Sat 2026-11-14 06:11:41 UTC

MainPID=2012336
Result=success
NRestarts=6
Id=btc-pairbook.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Tue 2026-11-17 03:15:20 UTC

MainPID=1556307
Result=success
NRestarts=0
Id=btc-rewardbook.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Sat 2026-11-14 06:11:44 UTC

MainPID=1555970
Result=success
NRestarts=0
Id=adv3-bot.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Sat 2026-11-14 06:11:41 UTC

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
Id=btc-rewardbook-archive.service
ActiveState=inactive
SubState=dead
UnitFileState=static
ActiveEnterTimestamp=

Result=success
Id=btc-rewardbook-archive.timer
ActiveState=active
SubState=waiting
UnitFileState=enabled
ActiveEnterTimestamp=Thu 2026-10-29 08:17:07 UTC

MainPID=0
Result=success
NRestarts=0
Id=btc-chainbook.service
ActiveState=inactive
SubState=dead
UnitFileState=disabled
ActiveEnterTimestamp=
NEXT                        LEFT LAST                         PASSED UNIT                         ACTIVATES
Wed 2026-11-18 01:30:20 UTC  11h Tue 2026-11-17 01:30:20 UTC 12h ago btc-rewardbook-archive.timer btc-rewardbook-archive.service
Wed 2026-11-18 03:00:20 UTC  12h Tue 2026-11-17 03:00:20 UTC 11h ago btc-pairbook-archive.timer   btc-pairbook-archive.service
Wed 2026-11-18 05:28:29 UTC  15h Tue 2026-11-17 07:14:28 UTC  7h ago apt-daily.timer              apt-daily.service
Wed 2026-11-18 06:25:08 UTC  16h Tue 2026-11-17 06:28:33 UTC  7h ago apt-daily-upgrade.timer      apt-daily-upgrade.service

4 timers listed.
2026-11-15T23:19:43+00:00 vultr systemd[1]: Reloading requested from client PID 1847511 ('systemctl') (unit crypto-deploy.service)...
2026-11-15T23:19:43+00:00 vultr systemd[1]: Reloading...
2026-11-15T23:19:44+00:00 vultr systemd[1]: Reloading finished in 446 ms.
2026-11-15T23:19:44+00:00 vultr systemd[1]: Reloading requested from client PID 1847587 ('systemctl') (unit crypto-deploy.service)...
2026-11-15T23:19:44+00:00 vultr systemd[1]: Reloading...
2026-11-15T23:19:44+00:00 vultr systemd[1]: Reloading finished in 341 ms.
2026-11-15T23:19:44+00:00 vultr systemd[1]: Reloading requested from client PID 1847691 ('systemctl') (unit crypto-deploy.service)...
2026-11-15T23:19:44+00:00 vultr systemd[1]: Reloading...
2026-11-15T23:19:44+00:00 vultr systemd[1]: Reloading finished in 249 ms.
2026-11-15T23:19:44+00:00 vultr systemd[1]: Reloading requested from client PID 1847744 ('systemctl') (unit crypto-deploy.service)...
2026-11-15T23:19:44+00:00 vultr systemd[1]: Reloading...
2026-11-15T23:19:45+00:00 vultr systemd[1]: Reloading finished in 250 ms.
2026-11-15T23:19:45+00:00 vultr systemd[1]: Reloading requested from client PID 1847797 ('systemctl') (unit crypto-deploy.service)...
2026-11-15T23:19:45+00:00 vultr systemd[1]: Reloading...
2026-11-15T23:19:45+00:00 vultr systemd[1]: Reloading finished in 249 ms.
2026-11-15T23:19:45+00:00 vultr systemd[1]: Reloading requested from client PID 1847850 ('systemctl') (unit crypto-deploy.service)...
2026-11-15T23:19:45+00:00 vultr systemd[1]: Reloading...
2026-11-15T23:19:45+00:00 vultr systemd[1]: Reloading finished in 255 ms.
2026-11-15T23:19:45+00:00 vultr systemd[1]: Reloading requested from client PID 1847903 ('systemctl') (unit crypto-deploy.service)...
2026-11-15T23:19:45+00:00 vultr systemd[1]: Reloading...
2026-11-15T23:19:45+00:00 vultr systemd[1]: Reloading finished in 248 ms.
2026-11-15T23:29:46+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
2026-11-15T23:34:47+00:00 vultr systemd[1]: btc-pairbook.service: Sent signal SIGTERM to main process 1767557 (python) on client request.
2026-11-15T23:34:47+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-11-15T23:34:47+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 19min 4.229s CPU time, 60.2M memory peak, 40.8M memory swap peak.
2026-11-15T23:34:52+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 4.
2026-11-15T23:34:52+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-11-15T23:45:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Deactivated successfully.
2026-11-15T23:45:41+00:00 vultr systemd[1]: Finished btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release.
2026-11-15T23:45:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Consumed 15.455s CPU time.
2026-11-15T23:49:46+00:00 vultr systemd[1]: Starting btc-rewardbook-archive.service - btc-5m-twap reward book archive, the stream files of closed slots to a Release...
2026-11-15T23:53:32+00:00 vultr systemd[1]: btc-rewardbook-archive.service: Deactivated successfully.
2026-11-15T23:53:32+00:00 vultr systemd[1]: Finished btc-rewardbook-archive.service - btc-5m-twap reward book archive, the stream files of closed slots to a Release.
2026-11-15T23:53:32+00:00 vultr systemd[1]: btc-rewardbook-archive.service: Consumed 7.770s CPU time.
2026-11-16T01:30:20+00:00 vultr systemd[1]: Starting btc-rewardbook-archive.service - btc-5m-twap reward book archive, the stream files of closed slots to a Release...
2026-11-16T01:32:36+00:00 vultr systemd[1]: btc-rewardbook-archive.service: Deactivated successfully.
2026-11-16T01:32:36+00:00 vultr systemd[1]: Finished btc-rewardbook-archive.service - btc-5m-twap reward book archive, the stream files of closed slots to a Release.
2026-11-16T01:32:36+00:00 vultr systemd[1]: btc-rewardbook-archive.service: Consumed 1.311s CPU time.
2026-11-16T03:00:20+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
2026-11-16T03:03:14+00:00 vultr systemd[1]: btc-pairbook.service: Sent signal SIGTERM to main process 1849495 (python) on client request.
2026-11-16T03:03:14+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-11-16T03:03:14+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 6min 37.637s CPU time, 44.4M memory peak, 36.2M memory swap peak.
2026-11-16T03:03:19+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 5.
2026-11-16T03:03:19+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-11-16T03:15:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Deactivated successfully.
2026-11-16T03:15:41+00:00 vultr systemd[1]: Finished btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release.
2026-11-16T03:15:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Consumed 5.137s CPU time.
2026-11-17T01:30:20+00:00 vultr systemd[1]: Starting btc-rewardbook-archive.service - btc-5m-twap reward book archive, the stream files of closed slots to a Release...
2026-11-17T01:36:08+00:00 vultr systemd[1]: btc-rewardbook-archive.service: Deactivated successfully.
2026-11-17T01:36:08+00:00 vultr systemd[1]: Finished btc-rewardbook-archive.service - btc-5m-twap reward book archive, the stream files of closed slots to a Release.
2026-11-17T01:36:08+00:00 vultr systemd[1]: btc-rewardbook-archive.service: Consumed 18.734s CPU time.
2026-11-17T03:00:20+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
2026-11-17T03:15:15+00:00 vultr systemd[1]: btc-pairbook.service: Sent signal SIGTERM to main process 1871674 (python) on client request.
2026-11-17T03:15:15+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-11-17T03:15:15+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 50min 3.867s CPU time, 53.6M memory peak, 41.5M memory swap peak.
2026-11-17T03:15:20+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 6.
2026-11-17T03:15:20+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-11-17T03:30:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Deactivated successfully.
2026-11-17T03:30:41+00:00 vultr systemd[1]: Finished btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release.
2026-11-17T03:30:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Consumed 37.405s CPU time.
3460315175	/root
4346671262	/var/lib
3972719165	/var/log
159564972	/var/cache
4547965470	/usr
264747867	/home
1968	/opt
51333327	/srv
5199683	/tmp
31271831	/var/lib/btc-pairbook-archive
42137787	/root/seahome_webapp.git
43108667	/var/lib/btc-chainbook
50037627	/var/lib/cryptopaper
53018674	/var/lib/containerd
59154198	/var/lib/cryptorun
194157457	/root/my_real_estate_bot
216486933	/var/lib/apt
337345084	/root/btc-5m-twap
392741782	/root/crypto-auto
517113206	/root/tz01-env
584947343	/root/btc-forensics
672306068	/root/PROJECT_GAMING_PS5
928514545	/var/lib/btc-rewardbook
1255843205	/var/lib/btc-pairbook
1655304787	/var/lib/btc-recorder
928514545	/var/lib/btc-rewardbook
1255843205	/var/lib/btc-pairbook
5842782	/var/lib/btc-rewardbook-archive
31271831	/var/lib/btc-pairbook-archive
1655308862	/var/lib/btc-recorder
584947343	/root/btc-forensics
24704103	/root/.claude-8j
2579
Archived and active journals take up 2.9G in the file system.
[Journal]
Storage=auto
ls: cannot access '/etc/systemd/journald.conf.d': No such file or directory
$nrconf{blacklist} = [
    qr(^/usr/bin/sudo(\.dpkg-new)?$),
    qr(^/sbin/(dhclient|dhcpcd5|pump|udhcpc)(\.dpkg-new)?$),
    qr(^/usr/bin/apt-get(\.dpkg-new)?$),
];
$nrconf{override_rc} = {
    qr(^dbus) => 0,
    qr(^gdm) => 0,
    qr(^kdm) => 0,
    qr(^nodm) => 0,
    qr(^sddm) => 0,
    qr(^wdm) => 0,
    qr(^xdm) => 0,
    qr(^lightdm) => 0,
    qr(^slim) => 0,
    qr(^lxdm) => 0,
    qr(^bird) => 0,
    qr(^network) => 0,
    qr(^NetworkManager) => 0,
    qr(^ModemManager) => 0,
total 12
drwxr-xr-x 2 root root 4096 Feb 10  2026 .
drwxr-xr-x 6 root root 4096 Feb 10  2026 ..
-rw-r--r-- 1 root root  241 Dec  5  2024 README.needrestart
Start-Date: 2026-11-12  06:21:27
Commandline: /usr/bin/unattended-upgrade
End-Date: 2026-11-12  06:21:28
Start-Date: 2026-11-12  06:21:30
Commandline: /usr/bin/unattended-upgrade
End-Date: 2026-11-12  06:21:31
Start-Date: 2026-11-12  06:21:33
Commandline: /usr/bin/unattended-upgrade
End-Date: 2026-11-12  06:21:34
Start-Date: 2026-11-12  06:21:36
Commandline: /usr/bin/unattended-upgrade
End-Date: 2026-11-12  06:21:36
Start-Date: 2026-11-14  06:11:34
Commandline: /usr/bin/unattended-upgrade
Upgrade: libc6:amd64 (2.39-0ubuntu8.9, 2.39-0ubuntu8.12), locales:amd64 (2.39-0ubuntu8.9, 2.39-0ubuntu8.12), libc-dev-bin:amd64 (2.39-0ubuntu8.9, 2.39-0ubuntu8.12), libc-bin:amd64 (2.39-0ubuntu8.9, 2.39-0ubuntu8.12), libc-devtools:amd64 (2.39-0ubuntu8.9, 2.39-0ubuntu8.12), libc6-dev:amd64 (2.39-0ubuntu8.9, 2.39-0ubuntu8.12)
End-Date: 2026-11-14  06:11:40
Start-Date: 2026-11-14  06:11:50
Commandline: /usr/bin/unattended-upgrade
Upgrade: apache2-utils:amd64 (2.4.58-1ubuntu8.18, 2.4.58-1ubuntu8.19)
End-Date: 2026-11-14  06:11:52
disabled
exit=1
inactive
exit=3
/root/btc-recorder-svc exit=0
/root/btc-pairbook-svc exit=0
/root/btc-pairbook-archive-svc exit=0
/root/btc-rewardbook-svc exit=0
/root/btc-rewardbook-archive-svc exit=0
/root/adv3-bot-svc exit=0
/root/tz45-work exit=1
/root/btc-5m-twap       13f3143 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/tmp/claude-0/-root-btc-5m-twap/ccca2df8-e51d-56bc-8205-06299775095a/scratchpad
total 24
drwx------  6 root root 4096 Nov 16 07:51 .
drwx------ 40 root root 4096 Nov 16 07:46 ..
drwx------  4 root root 4096 Nov 16 07:47 892ec9bf-0691-50df-8231-a07862dcb100
drwx------  3 root root 4096 Nov 15 10:28 95cf58d2-1ec6-4c73-a622-38d04665f5ae
drwx------  3 root root 4096 Nov 16 07:46 b93843c6-34fe-4b95-8041-0ae0aad4b8ab
drwx------  4 root root 4096 Nov 17 14:14 ccca2df8-e51d-56bc-8205-06299775095a
MemAvailable read 1 14:16:24: 562360320
```
- **Refs, §0.5.** `git ls-remote origin` printed 162 ref lines against the Architect's 160 of 2026-11-16 23:05 UTC. The differences: `HEAD` and `refs/heads/main` at `13f3143` (the upload) in place of `53e5690`; and two new tags from the 2026-11-17 calendar runs, `rewardbook-streams-1794879020` (31 rewardbook tags) and `pairbook-streams-1794884420` (58 pairbook tags). There was no `refs/heads/tz-46-capture-room`, no merge ref, and 44 pull heads. The one commit on `main`'s first-parent line above `53e5690` is `13f3143 Add files via upload`, which adds `CryptoTZ/TZ-46-capture-room.md`.
```
Tue Nov 17 02:16:36 PM UTC 2026
[2026-11-17T14:16:36Z] origin/main 13f3143131de9f3c7ef687f5803aa910daa4405b: 111 paths under CryptoTZ/ and CryptoReports/; of the number TZ-46-: ['CryptoTZ/TZ-46-capture-room.md'] and []
[2026-11-17T14:16:36Z] NUMBER PASS - 2 of 2
[2026-11-17T14:16:36Z] peak memory of this run: 26075136 bytes
[2026-11-17T14:16:36Z] opens refused: 0; reward book opens: 0; API requests 0, downloads 0, 0 bytes; files removed 0
exit=0
```
```
Tue Nov 17 02:16:36 PM UTC 2026
13f3143131de9f3c7ef687f5803aa910daa4405b	HEAD
13f3143131de9f3c7ef687f5803aa910daa4405b	refs/heads/main
7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8	refs/heads/tz-23-maker-m0
6f045cffc3601b589d3b8b7a6a9af6f73991e18b	refs/heads/tz-24-nesting-b2
e8b46a85d61e1a17841962846f6d3012046c2d70	refs/heads/tz-26-nesting-b3-capture
bce5a85be7850a33f95192265b916cc9c5e0aaf1	refs/heads/tz-27-pairbook-archive
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/heads/tz-28-pairbook-archive-timer
f6425f713034724210dc120d2108bcfad63cadc6	refs/heads/tz-29-maker-m0-second-look
fcd9ca566e9b948f0426707e7c3b5684f7f03b04	refs/heads/tz-30-nesting-b3-measure
404288fb03ffd3619b2183f121d45688def8fba8	refs/heads/tz-31-who-earns
b601f756edea59adf536d7ef05226d6f06bcef13	refs/heads/tz-32-our-quoting
2dcd70e08b18b93c64bb67d9849ac1216ce40e41	refs/heads/tz-33-reward-book-capture
6a615257277d3c94dafd4d39783499560a344648	refs/heads/tz-34-rewardbook-archive-timer
6c74b62bfef7afad2c71c742411124387327a588	refs/heads/tz-35-advisor-bot
444628905625809f24dd1fa51159b4093b763789	refs/heads/tz-36-advisor-trust-block
6d70c6aaa5457365743d2fb80e13e0817af8d292	refs/heads/tz-37-capital-allocation
8f37199aa4f9e14cb08534b1be3b7c258af917c2	refs/heads/tz-38-adv3-pit-validation
fc687582ebc4064b7483e2ac5cb9ca5b1af9c9f5	refs/heads/tz-39-advisor-checks
433ce139eedc112862ecf678cda6eaa2577d73d3	refs/heads/tz-40-strong-every-rank
4e6db2d16dda3da14957120d636f537dfc0bcc87	refs/heads/tz-42-advisor-registry
ab0f3873a66eb302225c3849da362bfe301e93df	refs/heads/tz-43-l0-our-quote
ab0a8be170786ee9b4c9bfd18ed5a522db669932	refs/heads/tz-44-l0-inputs-release
01756f665893096ab38ae10dfbe58f074f8fb648	refs/heads/tz-45-l0-rule-w
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
fcd9ca566e9b948f0426707e7c3b5684f7f03b04	refs/pull/29/head
ee2f6327390ef4d0c6169d1fba1a2ed4ae936dc3	refs/pull/3/head
404288fb03ffd3619b2183f121d45688def8fba8	refs/pull/30/head
b601f756edea59adf536d7ef05226d6f06bcef13	refs/pull/31/head
2dcd70e08b18b93c64bb67d9849ac1216ce40e41	refs/pull/32/head
6a615257277d3c94dafd4d39783499560a344648	refs/pull/34/head
6c74b62bfef7afad2c71c742411124387327a588	refs/pull/35/head
444628905625809f24dd1fa51159b4093b763789	refs/pull/36/head
6d70c6aaa5457365743d2fb80e13e0817af8d292	refs/pull/37/head
8f37199aa4f9e14cb08534b1be3b7c258af917c2	refs/pull/38/head
fc687582ebc4064b7483e2ac5cb9ca5b1af9c9f5	refs/pull/39/head
0e13a5c76dfa2469ff25b3b0dd282872decf6f25	refs/pull/4/head
433ce139eedc112862ecf678cda6eaa2577d73d3	refs/pull/40/head
4e6db2d16dda3da14957120d636f537dfc0bcc87	refs/pull/41/head
cca11090695ae824c94a6f097959d93355ce3986	refs/pull/42/head
ab0f3873a66eb302225c3849da362bfe301e93df	refs/pull/43/head
ab0a8be170786ee9b4c9bfd18ed5a522db669932	refs/pull/44/head
01756f665893096ab38ae10dfbe58f074f8fb648	refs/pull/45/head
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
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792650248
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792724420
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792810820
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792850109
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792897220
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792908757
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792930875
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792983620
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793070020
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793082340
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793156420
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793169873
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793187616
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793242820
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793260762
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793356734
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793415620
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793502020
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793588420
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793674820
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793761220
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793774618
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793847620
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793861040
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793934020
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793968389
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793990589
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1794020420
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1794106820
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1794193220
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1794279620
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1794366020
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1794452420
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1794521401
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1794625220
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1794637296
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1794711620
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1794744627
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1794785386
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1794798020
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1794884420
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793263627
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793286490
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793306720
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793321975
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793323820
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793357934
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793410220
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793496620
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793583020
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793669420
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793755820
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793775818
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793842220
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793862240
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793928620
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793991789
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794015020
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794101420
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794187820
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794274220
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794360620
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794447020
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794522601
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794533420
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794619820
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794638496
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794706220
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794745827
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794786586
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794792620
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794879020
d3251aa2bd312409f7b096bfd5968f3bedbd1be5	refs/tags/tz-01a-dataset
ea9290b92b9fa50c22d0560d5d01dfa392af44df	refs/tags/tz-01a-dataset^{}
e299d4e45f48b7efaa8cb18bd54b139fc0627630	refs/tags/tz-27-pairbook-streams
bce5a85be7850a33f95192265b916cc9c5e0aaf1	refs/tags/tz-27-pairbook-streams^{}
ab0a8be170786ee9b4c9bfd18ed5a522db669932	refs/tags/tz-44-l0-inputs
01756f665893096ab38ae10dfbe58f074f8fb648	refs/tags/tz-45-l0-rule-w-inputs
exit=0
```

## 2. Measurements

### 2.1 The room — before and after
```
Tue Nov 17 02:17:51 PM UTC 2026
[2026-11-17T14:17:52Z] MemAvailable read 1: 294379520 bytes, floor 133073162
[2026-11-17T14:17:52Z] free 8710725632 bytes, floor 2300000000
[2026-11-17T14:17:52Z] free 8710725632 bytes on /var/lib at 2026-11-17T14:17:52Z
[2026-11-17T14:17:52Z] the reward book's store: 21 directories; 51 stream files, 611687347 bytes; 3911 other files, 318622388 bytes
[2026-11-17T14:17:52Z] the pair book's store: 3627 directories; 46 stream files, 1151737742 bytes; 10884 other files, 104105463 bytes
[2026-11-17T14:17:52Z] the forensic store: 2579 files, 584947343 bytes
[2026-11-17T14:17:52Z] the reward book archive's ledger: 195 records, 0 bytes of a line still written
[2026-11-17T14:17:52Z]   run 1794447020 2026-11-12T01:30:20Z complete: 96 files 1504752064 bytes; free before removal 7419768832, after 8924979200; store's streams at its end 30355123; rate a day 1504752064
[2026-11-17T14:17:52Z]   run 1794522601 2026-11-12T22:30:01Z complete: 84 files 1290341538 bytes; free before removal 7867957248, after 9158684672; store's streams at its end 17560197; rate a day 1474676043
[2026-11-17T14:17:52Z]   run 1794533420 2026-11-13T01:30:20Z complete: 12 files 150295740 bytes; free before removal 8716177408, after 8866500608; store's streams at its end 18232178; rate a day 1202365920
[2026-11-17T14:17:52Z]   run 1794619820 2026-11-14T01:30:20Z complete: 80 files 1229012293 bytes; free before removal 6874419200, after 8103866368; store's streams at its end 0; rate a day 1474814751
[2026-11-17T14:17:52Z]   run 1794638496 2026-11-14T06:41:36Z complete: 20 files 281359405 bytes; free before removal 10382114816, after 10663542784; store's streams at its end 15480164; rate a day 1421605414
[2026-11-17T14:17:52Z]   run 1794706220 2026-11-15T01:30:20Z complete: 75 files 895420557 bytes; free before removal 8173604864, after 9069420544; store's streams at its end 12342328; rate a day 1146138312
[2026-11-17T14:17:52Z]   run 1794745827 2026-11-15T12:30:27Z complete: 44 files 462130216 bytes; free before removal 10074243072, after 10536591360; store's streams at its end 23481626; rate a day 1008284107
[2026-11-17T14:17:52Z]   run 1794786586 2026-11-15T23:49:46Z complete: 46 files 473624826 bytes; free before removal 10169692160, after 10643542016; store's streams at its end 5149102; rate a day 988434419
[2026-11-17T14:17:52Z]   run 1794792620 2026-11-16T01:30:20Z complete: 6 files 68188364 bytes; free before removal 10400702464, after 10468909056; store's streams at its end 14846639; rate a day 1091013824
[2026-11-17T14:17:52Z]   run 1794879020 2026-11-17T01:30:20Z complete: 81 files 1196646926 bytes; free before removal 6875881472, after 8072974336; store's streams at its end 0; rate a day 1418248208
[2026-11-17T14:17:52Z] the pair book archive's ledger: 585 records, 0 bytes of a line still written
[2026-11-17T14:17:52Z]   run 1794366020 2026-11-11T03:00:20Z complete: 96 files 2132682010 bytes; free before removal 8912961536, after 11046055936; store's streams at its end 57929215; rate a day 2132682010
[2026-11-17T14:17:52Z]   run 1794452420 2026-11-12T03:00:20Z complete: 96 files 2198550653 bytes; free before removal 8728158208, after 10927165440; store's streams at its end 43412885; rate a day 2198550653
[2026-11-17T14:17:52Z]   run 1794521401 2026-11-12T22:10:01Z complete: 77 files 1785949160 bytes; free before removal 8633180160, after 10419458048; store's streams at its end 473845433; rate a day 2226637913
[2026-11-17T14:17:52Z]   run 1794625220 2026-11-14T03:00:20Z complete: 115 files 2736056905 bytes; free before removal 7907991552, after 10644602880; store's streams at its end 48597984; rate a day 2284012720
[2026-11-17T14:17:52Z]   run 1794637296 2026-11-14T06:21:36Z complete: 14 files 243922720 bytes; free before removal 10213285888, after 10457255936; store's streams at its end 52144293; rate a day 1672612937
[2026-11-17T14:17:52Z]   run 1794711620 2026-11-15T03:00:20Z complete: 82 files 1744188017 bytes; free before removal 8881881088, after 10626433024; store's streams at its end 57782153; rate a day 2041976215
[2026-11-17T14:17:52Z]   run 1794744627 2026-11-15T12:10:27Z complete: 37 files 934906012 bytes; free before removal 9226797056, after 10161893376; store's streams at its end 100551791; rate a day 2425702085
[2026-11-17T14:17:52Z]   run 1794785386 2026-11-15T23:29:46Z complete: 45 files 1027399417 bytes; free before removal 9173057536, after 10200657920; store's streams at its end 38875877; rate a day 2191785422
[2026-11-17T14:17:52Z]   run 1794798020 2026-11-16T03:00:20Z complete: 14 files 318038938 bytes; free before removal 10241372160, after 10559459328; store's streams at its end 59274466; rate a day 2180838432
[2026-11-17T14:17:52Z]   run 1794884420 2026-11-17T03:00:20Z complete: 96 files 2573559241 bytes; free before removal 7872217088, after 10446286848; store's streams at its end 84362539; rate a day 2573559241
[2026-11-17T14:17:52Z] room: free 8710725632 + the reward book's stream files 611687347 = 9322412979; less its stream floor 7300000000 and the most its store holds between two runs, 445535636 = 14 slots of 31823974, the margin 1576877343; with the pair book's 46 stream files 10474150721
[2026-11-17T14:17:52Z] at 43500000 bytes a day beside the streams the margin lasts 36.3 days, to 2026-12-23T20:17:57Z [modelled]
[2026-11-17T14:17:52Z] at 187760570 bytes a day beside the streams the margin lasts 8.4 days, to 2026-11-25T23:51:29Z [modelled]
[2026-11-17T14:17:52Z] peak memory of this run: 27516928 bytes
[2026-11-17T14:17:52Z] opens refused: 0; reward book opens: 0; API requests 0, downloads 0, 0 bytes; files removed 0
exit=0
```
```
Tue Nov 17 05:02:01 PM UTC 2026
[2026-11-17T17:02:01Z] MemAvailable read 1: 292356096 bytes, floor 133073162
[2026-11-17T17:02:01Z] free 10607034368 bytes, floor 2300000000
[2026-11-17T17:02:02Z] free 10607034368 bytes on /var/lib at 2026-11-17T17:02:02Z
[2026-11-17T17:02:02Z] the reward book's store: 21 directories; 4 stream files, 46897842 bytes; 3933 other files, 320282060 bytes
[2026-11-17T17:02:02Z] the pair book's store: 3629 directories; 2 stream files, 42468017 bytes; 10890 other files, 104167525 bytes
[2026-11-17T17:02:02Z] the pair book's window 1794924900 2026-11-17T14:15:00Z: 18799261 bytes of stream
[2026-11-17T17:02:02Z] the pair book's window 1794925800 2026-11-17T14:30:00Z: 23668756 bytes of stream
[2026-11-17T17:02:02Z] the forensic store: 2532 files, 355893557 bytes
[2026-11-17T17:02:02Z] the reward book archive's ledger: 207 records, 0 bytes of a line still written
[2026-11-17T17:02:02Z]   run 1794533420 2026-11-13T01:30:20Z complete: 12 files 150295740 bytes; free before removal 8716177408, after 8866500608; store's streams at its end 18232178; rate a day 1202365920
[2026-11-17T17:02:02Z]   run 1794619820 2026-11-14T01:30:20Z complete: 80 files 1229012293 bytes; free before removal 6874419200, after 8103866368; store's streams at its end 0; rate a day 1474814751
[2026-11-17T17:02:02Z]   run 1794638496 2026-11-14T06:41:36Z complete: 20 files 281359405 bytes; free before removal 10382114816, after 10663542784; store's streams at its end 15480164; rate a day 1421605414
[2026-11-17T17:02:02Z]   run 1794706220 2026-11-15T01:30:20Z complete: 75 files 895420557 bytes; free before removal 8173604864, after 9069420544; store's streams at its end 12342328; rate a day 1146138312
[2026-11-17T17:02:02Z]   run 1794745827 2026-11-15T12:30:27Z complete: 44 files 462130216 bytes; free before removal 10074243072, after 10536591360; store's streams at its end 23481626; rate a day 1008284107
[2026-11-17T17:02:02Z]   run 1794786586 2026-11-15T23:49:46Z complete: 46 files 473624826 bytes; free before removal 10169692160, after 10643542016; store's streams at its end 5149102; rate a day 988434419
[2026-11-17T17:02:02Z]   run 1794792620 2026-11-16T01:30:20Z complete: 6 files 68188364 bytes; free before removal 10400702464, after 10468909056; store's streams at its end 14846639; rate a day 1091013824
[2026-11-17T17:02:02Z]   run 1794879020 2026-11-17T01:30:20Z complete: 81 files 1196646926 bytes; free before removal 6875881472, after 8072974336; store's streams at its end 0; rate a day 1418248208
[2026-11-17T17:02:02Z]   run 1794928547 2026-11-17T15:15:47Z complete: 53 files 652685158 bytes; free before removal 9986568192, after 10639491072; store's streams at its end 18589742; rate a day 1182222172
[2026-11-17T17:02:02Z]   run 1794933020 2026-11-17T16:30:20Z complete: 5 files 71537680 bytes; free before removal 10566414336, after 10637975552; store's streams at its end 17204028; rate a day 1373523456
[2026-11-17T17:02:02Z] the pair book archive's ledger: 595 records, 0 bytes of a line still written
[2026-11-17T17:02:02Z]   run 1794452420 2026-11-12T03:00:20Z complete: 96 files 2198550653 bytes; free before removal 8728158208, after 10927165440; store's streams at its end 43412885; rate a day 2198550653
[2026-11-17T17:02:02Z]   run 1794521401 2026-11-12T22:10:01Z complete: 77 files 1785949160 bytes; free before removal 8633180160, after 10419458048; store's streams at its end 473845433; rate a day 2226637913
[2026-11-17T17:02:02Z]   run 1794625220 2026-11-14T03:00:20Z complete: 115 files 2736056905 bytes; free before removal 7907991552, after 10644602880; store's streams at its end 48597984; rate a day 2284012720
[2026-11-17T17:02:02Z]   run 1794637296 2026-11-14T06:21:36Z complete: 14 files 243922720 bytes; free before removal 10213285888, after 10457255936; store's streams at its end 52144293; rate a day 1672612937
[2026-11-17T17:02:02Z]   run 1794711620 2026-11-15T03:00:20Z complete: 82 files 1744188017 bytes; free before removal 8881881088, after 10626433024; store's streams at its end 57782153; rate a day 2041976215
[2026-11-17T17:02:02Z]   run 1794744627 2026-11-15T12:10:27Z complete: 37 files 934906012 bytes; free before removal 9226797056, after 10161893376; store's streams at its end 100551791; rate a day 2425702085
[2026-11-17T17:02:02Z]   run 1794785386 2026-11-15T23:29:46Z complete: 45 files 1027399417 bytes; free before removal 9173057536, after 10200657920; store's streams at its end 38875877; rate a day 2191785422
[2026-11-17T17:02:02Z]   run 1794798020 2026-11-16T03:00:20Z complete: 14 files 318038938 bytes; free before removal 10241372160, after 10559459328; store's streams at its end 59274466; rate a day 2180838432
[2026-11-17T17:02:02Z]   run 1794884420 2026-11-17T03:00:20Z complete: 96 files 2573559241 bytes; free before removal 7872217088, after 10446286848; store's streams at its end 84362539; rate a day 2573559241
[2026-11-17T17:02:02Z]   run 1794925184 2026-11-17T14:19:44Z complete: 46 files 1151737742 bytes; free before removal 8904314880, after 10056265728; store's streams at its end 42468017; rate a day 2403626592
[2026-11-17T17:02:02Z] room: free 10607034368 + the reward book's stream files 46897842 = 10653932210; less its stream floor 7300000000 and the most its store holds between two runs, 445535636 = 14 slots of 31823974, the margin 2908396574; with the pair book's 2 stream files 10696400227
[2026-11-17T17:02:02Z] at 43500000 bytes a day beside the streams the margin lasts 66.9 days, to 2027-01-23T13:39:59Z [modelled]
[2026-11-17T17:02:02Z] at 187760570 bytes a day beside the streams the margin lasts 15.5 days, to 2026-12-03T04:47:31Z [modelled]
[2026-11-17T17:02:02Z] G-ROOM PASS: the margin 2908396574 bytes, at least 2000000000 asked
[2026-11-17T17:02:02Z] peak memory of this run: 27254784 bytes
[2026-11-17T17:02:02Z] opens refused: 0; reward book opens: 0; API requests 0, downloads 0, 0 bytes; files removed 0
exit=0
```
| | before (14:17:52Z) | after (17:02:02Z) |
|---|---|---|
| free on `/var/lib` | 8,710,725,632 | 10,607,034,368 |
| reward book: stream files / bytes | 51 / 611,687,347 | 4 / 46,897,842 |
| reward book: other files / bytes | 3,911 / 318,622,388 | 3,933 / 320,282,060 |
| pair book: directories | 3,627 | 3,629 |
| pair book: stream files / bytes | 46 / 1,151,737,742 | 2 / 42,468,017 |
| pair book: other files / bytes | 10,884 / 104,105,463 | 10,890 / 104,167,525 |
| forensic store: files / bytes | 2,579 / 584,947,343 | 2,532 / 355,893,557 |
| the room (free + reward book streams) | 9,322,412,979 | 10,653,932,210 |
| margin over 7,300,000,000 + PEAK 445,535,636 | 1,576,877,343 | **2,908,396,574** |
| days at 43,500,000 / 187,760,570 a day [modelled] | 36.3 / 8.4 | 66.9 / 15.5 |

### 2.2 The trees

Both host gates' `du -xsb` lines, the sixteen largest names, the journal (`2.9G`, `journald.conf` `[Journal] Storage=auto` alone, no drop-in directory) and needrestart's configuration are in §1's `03-host-gate.log` and in `91-host-gate-again.log`. The second host gate is quoted whole here. H1 to H3 were checked again and hold. H4 and H5 are printed only: the timer's `cmp` against `main`'s TZ-34 file now differs, and the pair book is disabled.
```
Tue Nov 17 05:02:19 PM UTC 2026
1794934939
2026-08-02 07:24:32
IDX BOOT ID                          FIRST ENTRY                 LAST ENTRY
  0 48a803f03549473383be5baecf790d4e Sun 2026-08-23 13:40:30 UTC Tue 2026-11-17 17:02:18 UTC
1
MemTotal:         978640 kB
MemAvailable:     269572 kB
SwapTotal:       3174396 kB
SwapFree:        2434952 kB
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10606698496
/var/lib/btc-recorder/btc-updown-5m/1794396600/manifest.json
4
3.12.3
btc-pairbook.service cmp exit=0
btc-pairbook-archive.service cmp exit=0
btc-pairbook-archive.timer cmp exit=0
btc-rewardbook-archive.service cmp exit=0
deploy/systemd/btc-rewardbook-archive.timer /etc/systemd/system/btc-rewardbook-archive.timer differ: byte 43, line 1
btc-rewardbook-archive.timer cmp exit=1
6a615257277d3c94dafd4d39783499560a344648
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3
1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72  /root/btc-rewardbook-archive-svc/tz34-rewardbook-archive-timer.py
46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4  /root/btc-pairbook-archive-svc/tz28-pairbook-archive-timer.py
a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670  /root/btc-rewardbook-svc/tz33-reward-book-capture.py
caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec  /root/btc-pairbook-svc/tz26-nesting-b3-capture.py
MainPID=1555954
Result=success
NRestarts=0
Id=btc-recorder.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Sat 2026-11-14 06:11:41 UTC

MainPID=0
Result=success
NRestarts=0
Id=btc-pairbook.service
ActiveState=inactive
SubState=dead
UnitFileState=disabled
ActiveEnterTimestamp=

MainPID=1556307
Result=success
NRestarts=0
Id=btc-rewardbook.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Sat 2026-11-14 06:11:44 UTC

MainPID=1555970
Result=success
NRestarts=0
Id=adv3-bot.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Sat 2026-11-14 06:11:41 UTC

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
ActiveState=inactive
SubState=dead
UnitFileState=disabled
ActiveEnterTimestamp=

MainPID=0
Result=success
NRestarts=0
Id=btc-rewardbook-archive.service
ActiveState=inactive
SubState=dead
UnitFileState=static
ActiveEnterTimestamp=

Result=success
Id=btc-rewardbook-archive.timer
ActiveState=active
SubState=waiting
UnitFileState=enabled
ActiveEnterTimestamp=Tue 2026-11-17 16:05:49 UTC

MainPID=0
Result=success
NRestarts=0
Id=btc-chainbook.service
ActiveState=inactive
SubState=dead
UnitFileState=disabled
ActiveEnterTimestamp=
NEXT                            LEFT LAST                           PASSED UNIT                         ACTIVATES
Tue 2026-11-17 19:30:20 UTC 2h 28min Tue 2026-11-17 16:30:20 UTC 31min ago btc-rewardbook-archive.timer btc-rewardbook-archive.service
Wed 2026-11-18 04:00:41 UTC      10h Tue 2026-11-17 07:14:28 UTC    9h ago apt-daily.timer              apt-daily.service
Wed 2026-11-18 06:16:03 UTC      13h Tue 2026-11-17 06:28:33 UTC   10h ago apt-daily-upgrade.timer      apt-daily-upgrade.service

3 timers listed.
2026-11-16T01:32:36+00:00 vultr systemd[1]: Finished btc-rewardbook-archive.service - btc-5m-twap reward book archive, the stream files of closed slots to a Release.
2026-11-16T01:32:36+00:00 vultr systemd[1]: btc-rewardbook-archive.service: Consumed 1.311s CPU time.
2026-11-16T03:00:20+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
2026-11-16T03:03:14+00:00 vultr systemd[1]: btc-pairbook.service: Sent signal SIGTERM to main process 1849495 (python) on client request.
2026-11-16T03:03:14+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-11-16T03:03:14+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 6min 37.637s CPU time, 44.4M memory peak, 36.2M memory swap peak.
2026-11-16T03:03:19+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 5.
2026-11-16T03:03:19+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-11-16T03:15:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Deactivated successfully.
2026-11-16T03:15:41+00:00 vultr systemd[1]: Finished btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release.
2026-11-16T03:15:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Consumed 5.137s CPU time.
2026-11-17T01:30:20+00:00 vultr systemd[1]: Starting btc-rewardbook-archive.service - btc-5m-twap reward book archive, the stream files of closed slots to a Release...
2026-11-17T01:36:08+00:00 vultr systemd[1]: btc-rewardbook-archive.service: Deactivated successfully.
2026-11-17T01:36:08+00:00 vultr systemd[1]: Finished btc-rewardbook-archive.service - btc-5m-twap reward book archive, the stream files of closed slots to a Release.
2026-11-17T01:36:08+00:00 vultr systemd[1]: btc-rewardbook-archive.service: Consumed 18.734s CPU time.
2026-11-17T03:00:20+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
2026-11-17T03:15:15+00:00 vultr systemd[1]: btc-pairbook.service: Sent signal SIGTERM to main process 1871674 (python) on client request.
2026-11-17T03:15:15+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-11-17T03:15:15+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 50min 3.867s CPU time, 53.6M memory peak, 41.5M memory swap peak.
2026-11-17T03:15:20+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 6.
2026-11-17T03:15:20+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-11-17T03:30:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Deactivated successfully.
2026-11-17T03:30:41+00:00 vultr systemd[1]: Finished btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release.
2026-11-17T03:30:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Consumed 37.405s CPU time.
2026-11-17T14:19:44+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
2026-11-17T14:32:48+00:00 vultr systemd[1]: btc-pairbook.service: Sent signal SIGTERM to main process 2012336 (python) on client request.
2026-11-17T14:32:48+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-11-17T14:32:48+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 22min 59.529s CPU time, 61.2M memory peak, 39.4M memory swap peak.
2026-11-17T14:32:53+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 7.
2026-11-17T14:32:53+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-11-17T14:45:42+00:00 vultr systemd[1]: btc-pairbook-archive.service: Deactivated successfully.
2026-11-17T14:45:42+00:00 vultr systemd[1]: Finished btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release.
2026-11-17T14:45:42+00:00 vultr systemd[1]: btc-pairbook-archive.service: Consumed 18.321s CPU time, 86.8M memory peak, 25.3M memory swap peak.
2026-11-17T14:45:45+00:00 vultr systemd[1]: Reloading requested from client PID 2082030 ('systemctl') (unit user@0.service)...
2026-11-17T14:45:45+00:00 vultr systemd[1]: Reloading...
2026-11-17T14:45:46+00:00 vultr systemd[1]: Reloading finished in 371 ms.
2026-11-17T14:45:46+00:00 vultr systemd[1]: btc-pairbook-archive.timer: Deactivated successfully.
2026-11-17T14:45:46+00:00 vultr systemd[1]: Stopped btc-pairbook-archive.timer - btc-5m-twap pair book archive, once a day.
2026-11-17T14:45:46+00:00 vultr systemd[1]: Reloading requested from client PID 2082086 ('systemctl') (unit user@0.service)...
2026-11-17T14:45:46+00:00 vultr systemd[1]: Reloading...
2026-11-17T14:45:46+00:00 vultr systemd[1]: Reloading finished in 561 ms.
2026-11-17T14:45:46+00:00 vultr systemd[1]: Stopping btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed...
2026-11-17T14:45:47+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-11-17T14:45:47+00:00 vultr systemd[1]: Stopped btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-11-17T14:45:47+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 28.557s CPU time, 58.3M memory peak, 20.2M memory swap peak.
2026-11-17T15:15:47+00:00 vultr systemd[1]: Starting btc-rewardbook-archive.service - btc-5m-twap reward book archive, the stream files of closed slots to a Release...
2026-11-17T15:21:45+00:00 vultr systemd[1]: btc-rewardbook-archive.service: Deactivated successfully.
2026-11-17T15:21:45+00:00 vultr systemd[1]: Finished btc-rewardbook-archive.service - btc-5m-twap reward book archive, the stream files of closed slots to a Release.
2026-11-17T15:21:45+00:00 vultr systemd[1]: btc-rewardbook-archive.service: Consumed 11.585s CPU time, 50.9M memory peak, 7.1M memory swap peak.
2026-11-17T16:05:49+00:00 vultr systemd[1]: Reloading requested from client PID 2089535 ('systemctl') (unit user@0.service)...
2026-11-17T16:05:49+00:00 vultr systemd[1]: Reloading...
2026-11-17T16:05:49+00:00 vultr systemd[1]: Reloading finished in 346 ms.
2026-11-17T16:05:49+00:00 vultr systemd[1]: btc-rewardbook-archive.timer: Deactivated successfully.
2026-11-17T16:05:49+00:00 vultr systemd[1]: Stopped btc-rewardbook-archive.timer - btc-5m-twap reward book archive, every three hours.
2026-11-17T16:05:49+00:00 vultr systemd[1]: Stopping btc-rewardbook-archive.timer - btc-5m-twap reward book archive, every three hours...
2026-11-17T16:05:49+00:00 vultr systemd[1]: Started btc-rewardbook-archive.timer - btc-5m-twap reward book archive, every three hours.
2026-11-17T16:30:20+00:00 vultr systemd[1]: Starting btc-rewardbook-archive.service - btc-5m-twap reward book archive, the stream files of closed slots to a Release...
2026-11-17T16:32:46+00:00 vultr systemd[1]: btc-rewardbook-archive.service: Deactivated successfully.
2026-11-17T16:32:46+00:00 vultr systemd[1]: Finished btc-rewardbook-archive.service - btc-5m-twap reward book archive, the stream files of closed slots to a Release.
2026-11-17T16:32:46+00:00 vultr systemd[1]: btc-rewardbook-archive.service: Consumed 1.419s CPU time, 58.5M memory peak, 0B memory swap peak.
3247637408	/root
2680271463	/var/lib
3973819096	/var/log
159564972	/var/cache
4547965470	/usr
264747867	/home
1968	/opt
51333327	/srv
5213959	/tmp
32154911	/var/lib/btc-pairbook-archive
42137787	/root/seahome_webapp.git
43108667	/var/lib/btc-chainbook
50041829	/var/lib/cryptopaper
53018674	/var/lib/containerd
59154198	/var/lib/cryptorun
146635542	/var/lib/btc-pairbook
194157457	/root/my_real_estate_bot
216486933	/var/lib/apt
337402781	/root/btc-5m-twap
355893557	/root/btc-forensics
367704114	/var/lib/btc-rewardbook
392741782	/root/crypto-auto
517113206	/root/tz01-env
672410091	/root/PROJECT_GAMING_PS5
1657840396	/var/lib/btc-recorder
367726903	/var/lib/btc-rewardbook
146635542	/var/lib/btc-pairbook
6032107	/var/lib/btc-rewardbook-archive
32154911	/var/lib/btc-pairbook-archive
1657845482	/var/lib/btc-recorder
355893557	/root/btc-forensics
24704103	/root/.claude-8j
2532
Archived and active journals take up 2.9G in the file system.
[Journal]
Storage=auto
ls: cannot access '/etc/systemd/journald.conf.d': No such file or directory
$nrconf{blacklist} = [
    qr(^/usr/bin/sudo(\.dpkg-new)?$),
    qr(^/sbin/(dhclient|dhcpcd5|pump|udhcpc)(\.dpkg-new)?$),
    qr(^/usr/bin/apt-get(\.dpkg-new)?$),
];
$nrconf{override_rc} = {
    qr(^dbus) => 0,
    qr(^gdm) => 0,
    qr(^kdm) => 0,
    qr(^nodm) => 0,
    qr(^sddm) => 0,
    qr(^wdm) => 0,
    qr(^xdm) => 0,
    qr(^lightdm) => 0,
    qr(^slim) => 0,
    qr(^lxdm) => 0,
    qr(^bird) => 0,
    qr(^network) => 0,
    qr(^NetworkManager) => 0,
    qr(^ModemManager) => 0,
total 12
drwxr-xr-x 2 root root 4096 Feb 10  2026 .
drwxr-xr-x 6 root root 4096 Feb 10  2026 ..
-rw-r--r-- 1 root root  241 Dec  5  2024 README.needrestart
Start-Date: 2026-11-12  06:21:27
Commandline: /usr/bin/unattended-upgrade
End-Date: 2026-11-12  06:21:28
Start-Date: 2026-11-12  06:21:30
Commandline: /usr/bin/unattended-upgrade
End-Date: 2026-11-12  06:21:31
Start-Date: 2026-11-12  06:21:33
Commandline: /usr/bin/unattended-upgrade
End-Date: 2026-11-12  06:21:34
Start-Date: 2026-11-12  06:21:36
Commandline: /usr/bin/unattended-upgrade
End-Date: 2026-11-12  06:21:36
Start-Date: 2026-11-14  06:11:34
Commandline: /usr/bin/unattended-upgrade
Upgrade: libc6:amd64 (2.39-0ubuntu8.9, 2.39-0ubuntu8.12), locales:amd64 (2.39-0ubuntu8.9, 2.39-0ubuntu8.12), libc-dev-bin:amd64 (2.39-0ubuntu8.9, 2.39-0ubuntu8.12), libc-bin:amd64 (2.39-0ubuntu8.9, 2.39-0ubuntu8.12), libc-devtools:amd64 (2.39-0ubuntu8.9, 2.39-0ubuntu8.12), libc6-dev:amd64 (2.39-0ubuntu8.9, 2.39-0ubuntu8.12)
End-Date: 2026-11-14  06:11:40
Start-Date: 2026-11-14  06:11:50
Commandline: /usr/bin/unattended-upgrade
Upgrade: apache2-utils:amd64 (2.4.58-1ubuntu8.18, 2.4.58-1ubuntu8.19)
End-Date: 2026-11-14  06:11:52
disabled
exit=1
inactive
exit=3
/root/btc-recorder-svc exit=0
/root/btc-pairbook-svc exit=0
/root/btc-pairbook-archive-svc exit=0
/root/btc-rewardbook-svc exit=0
/root/btc-rewardbook-archive-svc exit=0
/root/adv3-bot-svc exit=0
/root/tz45-work exit=1
/root/btc-5m-twap       13f3143 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/root/tz46-work/wt      c9d1071 [tz-46-capture-room]
/tmp/claude-0/-root-btc-5m-twap/ccca2df8-e51d-56bc-8205-06299775095a/scratchpad
total 16
drwx------  4 root root 4096 Nov 17 14:17 .
drwx------ 40 root root 4096 Nov 16 07:46 ..
drwx------  3 root root 4096 Nov 15 10:28 95cf58d2-1ec6-4c73-a622-38d04665f5ae
drwx------  4 root root 4096 Nov 17 14:14 ccca2df8-e51d-56bc-8205-06299775095a
MemAvailable read 1 17:02:42: 304521216
```
### 2.3 The forensic store

`forensics` found 47 files a published Release holds by bytes and SHA-256, all 47 in `tz-44-l0-inputs`, at least 13 expected. It read 93 Releases and 5,496 assets with a digest. It made 6 API requests (at most 40) and 47 full anonymous downloads of 229,053,786 bytes, each equal. Plan `forensics-plan.json` has SHA-256 `becd4c5c35bd6484a659bd1c211d9a515401d73db13a1cab03aa43a6ee6f414f`. Every `P` row:
```
Tue Nov 17 02:18:00 PM UTC 2026
[2026-11-17T14:18:00Z] MemAvailable read 1: 315105280 bytes, floor 133073162
[2026-11-17T14:18:00Z] free 8710569984 bytes, floor 2300000000
[2026-11-17T14:18:02Z] the forensic store /root/btc-forensics: 2579 files, 584947343 bytes, hashed in 1.9 s
[2026-11-17T14:18:07Z] the repository's Releases read anonymously: 93, 5496 assets with a digest
[2026-11-17T14:18:07Z] files a Release holds by bytes and SHA-256: 47; held by none: 2532
[2026-11-17T14:18:08Z] P /root/btc-forensics/tz43-work--days--1793404800.json 145864 d93f998fba7795f30379c06e2058c55f4eba9d0c340536a3d5a4d1636b765ee6: tz43-days-1793404800.json of tz-44-l0-inputs, asset 742816771, api True, download 200 equal
[2026-11-17T14:18:08Z] P /root/btc-forensics/tz43-work--days--1793404800.slots.txt 47260 ec4494031d22891f22ec2822287c0127c4f96f39dac1337f3980419813052400: tz43-days-1793404800.slots.txt of tz-44-l0-inputs, asset 742816818, api True, download 200 equal
[2026-11-17T14:18:08Z] P /root/btc-forensics/tz43-work--days--1793491200.json 147006 50e19969a8196ef3fe8b069056b75bb3ff5f5ba1c41a9ad70a48bd7e88ebaaae: tz43-days-1793491200.json of tz-44-l0-inputs, asset 742816879, api True, download 200 equal
[2026-11-17T14:18:09Z] P /root/btc-forensics/tz43-work--days--1793491200.slots.txt 47077 5a7169dbcdb3186b588e2bd77ef5017dc792f1ead7cc8d2b9c11a55cee90f763: tz43-days-1793491200.slots.txt of tz-44-l0-inputs, asset 742816931, api True, download 200 equal
[2026-11-17T14:18:09Z] P /root/btc-forensics/tz43-work--days--1793577600.json 146744 93c76d1594b1edef03e192c02cc67b0264e43ca4b77b6d49939845f5876dc57c: tz43-days-1793577600.json of tz-44-l0-inputs, asset 742816979, api True, download 200 equal
[2026-11-17T14:18:10Z] P /root/btc-forensics/tz43-work--days--1793577600.slots.txt 46799 aae9a59997c591b90672bec21ea2489e2f7e654eba03590bc8d1ff411a186e1c: tz43-days-1793577600.slots.txt of tz-44-l0-inputs, asset 742817035, api True, download 200 equal
[2026-11-17T14:18:10Z] P /root/btc-forensics/tz43-work--days--1793664000.json 147691 a80c3d721fce47537ff927c42b989cd4409d25b7c3a1e2c4e024a2463d48c54d: tz43-days-1793664000.json of tz-44-l0-inputs, asset 742817084, api True, download 200 equal
[2026-11-17T14:18:11Z] P /root/btc-forensics/tz43-work--days--1793664000.slots.txt 46785 dc9dff0e13153ee045ada2cb805c9567ce9bb4b490f88c40aa0821442fe8660b: tz43-days-1793664000.slots.txt of tz-44-l0-inputs, asset 742817122, api True, download 200 equal
[2026-11-17T14:18:11Z] P /root/btc-forensics/tz43-work--days--1793750400.json 155059 4f9ca91d2798fb9f7b496e98baa02d4fe9f6efb5f60f979540f682fb7fdadfa9: tz43-days-1793750400.json of tz-44-l0-inputs, asset 742817176, api True, download 200 equal
[2026-11-17T14:18:12Z] P /root/btc-forensics/tz43-work--days--1793750400.slots.txt 47105 71101c5d670141ce064c671824d5c8c8c1615ffce4801b1a422baa3df4281cdc: tz43-days-1793750400.slots.txt of tz-44-l0-inputs, asset 742817228, api True, download 200 equal
[2026-11-17T14:18:13Z] P /root/btc-forensics/tz43-work--days--1793836800.json 149722 e7266b1d2d05e1191095e9cd184e6bb15571ea7380fa1e4f51db90a5342e200d: tz43-days-1793836800.json of tz-44-l0-inputs, asset 742817282, api True, download 200 equal
[2026-11-17T14:18:13Z] P /root/btc-forensics/tz43-work--days--1793836800.slots.txt 46750 ec5792be99ff4169b4574b3a8ce04855ad7a5fcd51aba1b51baf4cc9d8ce44e5: tz43-days-1793836800.slots.txt of tz-44-l0-inputs, asset 742817327, api True, download 200 equal
[2026-11-17T14:18:13Z] P /root/btc-forensics/tz43-work--days--1794009600.json 146104 f3018bb242bff3b1d7483622cd4065074cc42faa90b1e8357d223c2796a6dfd5: tz43-days-1794009600.json of tz-44-l0-inputs, asset 742817397, api True, download 200 equal
[2026-11-17T14:18:14Z] P /root/btc-forensics/tz43-work--days--1794009600.slots.txt 46914 a0fdb71edc318fb7e41989c1aca3b591c9b3e4db39274e87588354639725c1e6: tz43-days-1794009600.slots.txt of tz-44-l0-inputs, asset 742817476, api True, download 200 equal
[2026-11-17T14:18:14Z] P /root/btc-forensics/tz43-work--days--1794096000.json 144626 910ed69e85ab28dc81a334538d229a66ba17107260325c1afe5eae95de02e91f: tz43-days-1794096000.json of tz-44-l0-inputs, asset 742817521, api True, download 200 equal
[2026-11-17T14:18:15Z] P /root/btc-forensics/tz43-work--days--1794096000.slots.txt 46970 00caaab0888d85779398751281da3e9219cfdf9742c77b5914499cf0c4421436: tz43-days-1794096000.slots.txt of tz-44-l0-inputs, asset 742817562, api True, download 200 equal
[2026-11-17T14:18:15Z] P /root/btc-forensics/tz43-work--fetch--1793404800.json 55310 5f56487e44aadcba1df2bc1316a889605baf83a4fcafc965b5ee4a18a6fec9b2: tz43-fetch-1793404800.json of tz-44-l0-inputs, asset 742816011, api True, download 200 equal
[2026-11-17T14:18:16Z] P /root/btc-forensics/tz43-work--fetch--1793404800.polls.jsonl 4990923 53ae4e79d354b3f8b35d497654159162b9c2290deb0d69b6f62b79c3fe8c1d71: tz43-fetch-1793404800.polls.jsonl of tz-44-l0-inputs, asset 742816068, api True, download 200 equal
[2026-11-17T14:18:17Z] P /root/btc-forensics/tz43-work--fetch--1793491200.json 55330 55f95448c4ba6abe1d1b154ff0e014ef190ffb7be861a7f6cb1a3bcddec7a1bd: tz43-fetch-1793491200.json of tz-44-l0-inputs, asset 742816109, api True, download 200 equal
[2026-11-17T14:18:17Z] P /root/btc-forensics/tz43-work--fetch--1793491200.polls.jsonl 5010687 1aac9148f26b55664b248be60b62394defc1b117b63bcd952c632bf96b3ebf54: tz43-fetch-1793491200.polls.jsonl of tz-44-l0-inputs, asset 742816152, api True, download 200 equal
[2026-11-17T14:18:18Z] P /root/btc-forensics/tz43-work--fetch--1793577600.json 55447 8589729bfe267feb57208833064bc71006e592e22edd8290d70bbc2b4474d9b5: tz43-fetch-1793577600.json of tz-44-l0-inputs, asset 742816189, api True, download 200 equal
[2026-11-17T14:18:18Z] P /root/btc-forensics/tz43-work--fetch--1793577600.polls.jsonl 5027379 19d765c78c93e9d4175328615ae3dc27b3e2f0c1dd7f6084eeab672a9e56427c: tz43-fetch-1793577600.polls.jsonl of tz-44-l0-inputs, asset 742816218, api True, download 200 equal
[2026-11-17T14:18:19Z] P /root/btc-forensics/tz43-work--fetch--1793664000.json 55449 1405b48ac2459f052b5b36dea8e85dd6cb0e112b49ac21030955d96f890eec02: tz43-fetch-1793664000.json of tz-44-l0-inputs, asset 742816263, api True, download 200 equal
[2026-11-17T14:18:19Z] P /root/btc-forensics/tz43-work--fetch--1793664000.polls.jsonl 5014920 4a5ef449ed6b1d2bf1378b817671b9bb3cac477c5a9fa6e5068d9673b24977cb: tz43-fetch-1793664000.polls.jsonl of tz-44-l0-inputs, asset 742816321, api True, download 200 equal
[2026-11-17T14:18:20Z] P /root/btc-forensics/tz43-work--fetch--1793750400.json 55543 1ed8768bd80b54220c0437e15fc424943a8829b716d7ba70f2b586f5ae14099c: tz43-fetch-1793750400.json of tz-44-l0-inputs, asset 742816379, api True, download 200 equal
[2026-11-17T14:18:21Z] P /root/btc-forensics/tz43-work--fetch--1793750400.polls.jsonl 4967708 f06145aa32845b9f3a65b8616e5842218b03869a3fc18d5a4bf1aaaa57fec920: tz43-fetch-1793750400.polls.jsonl of tz-44-l0-inputs, asset 742816445, api True, download 200 equal
[2026-11-17T14:18:21Z] P /root/btc-forensics/tz43-work--fetch--1793836800.json 55625 7d502a56ad2a4a3f95150bbcfc8c52c1190f2b977d9d1a72e2e1c4b3c2f5ba25: tz43-fetch-1793836800.json of tz-44-l0-inputs, asset 742816478, api True, download 200 equal
[2026-11-17T14:18:23Z] P /root/btc-forensics/tz43-work--fetch--1793836800.polls.jsonl 5055307 7918f3b6629489fcff4fd22cdb049a89e1e1ef63b86738c73ec680e17e5eff5d: tz43-fetch-1793836800.polls.jsonl of tz-44-l0-inputs, asset 742816529, api True, download 200 equal
[2026-11-17T14:18:23Z] P /root/btc-forensics/tz43-work--fetch--1794009600.json 55639 29e17ecde5f5d705e297bdc2be7e5e150aa50d06c3ac66ba9b1c4c13225b5708: tz43-fetch-1794009600.json of tz-44-l0-inputs, asset 742816581, api True, download 200 equal
[2026-11-17T14:18:24Z] P /root/btc-forensics/tz43-work--fetch--1794009600.polls.jsonl 5037697 91582ccfb9145559277d196f61e804e6be205d0b18d6168a1db6975711d6cf15: tz43-fetch-1794009600.polls.jsonl of tz-44-l0-inputs, asset 742816632, api True, download 200 equal
[2026-11-17T14:18:24Z] P /root/btc-forensics/tz43-work--fetch--1794096000.json 55660 a3ebc56744facb5c00f862c1f5d70a564672b68b5cc276398f32ae7f1bc0c552: tz43-fetch-1794096000.json of tz-44-l0-inputs, asset 742816680, api True, download 200 equal
[2026-11-17T14:18:25Z] P /root/btc-forensics/tz43-work--fetch--1794096000.polls.jsonl 5047340 7b0d86338359fbb4d5f4f7b54c6f36e0d45f2ed5c4d6d5731358c8e4e3099a82: tz43-fetch-1794096000.polls.jsonl of tz-44-l0-inputs, asset 742816730, api True, download 200 equal
[2026-11-17T14:18:25Z] P /root/btc-forensics/tz43-work--reading.json 9377 175d366101cd825437a1cd393aa57642965f7ffb9fe831746c2d9b2187d50be1: tz43-reading.json of tz-44-l0-inputs, asset 742817620, api True, download 200 equal
[2026-11-17T14:18:26Z] P /root/btc-forensics/tz43-work--set.json 6175 904f1b9b8244a15fe48549e39ffc879f68ad31de6963a41c05f5afc607edf0f7: tz43-set.json of tz-44-l0-inputs, asset 742817656, api True, download 200 equal
[2026-11-17T14:18:27Z] P /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793145600.tar 9256960 b268ef086a2d2d23afa6cb33b354eddd0d3589aca1621aa15901b6441667f9f6: rewardbook-inputs-1793145600.tar of tz-44-l0-inputs, asset 742815102, api True, download 200 equal
[2026-11-17T14:18:28Z] P /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793232000.tar 15482880 b214536add4d9b43cd6f634cd8c26cb92d9f82b0c6bd6508564a8b21a2529dc1: rewardbook-inputs-1793232000.tar of tz-44-l0-inputs, asset 742815172, api True, download 200 equal
[2026-11-17T14:18:42Z] P /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793318400.tar 16384000 e3189d4cf76f5acb2a14351610c7ea9dc1bd294e19cee310eef80b421b2b910f: rewardbook-inputs-1793318400.tar of tz-44-l0-inputs, asset 742815291, api True, download 200 equal
[2026-11-17T14:18:49Z] P /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793404800.tar 16445440 563a3ccf2df5e48641dff892de6f50d4421c071cd42ae7cbb147b3ed8b2f3c1f: rewardbook-inputs-1793404800.tar of tz-44-l0-inputs, asset 742815370, api True, download 200 equal
[2026-11-17T14:18:50Z] P /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793491200.tar 16291840 0614a35f95eb4fe7f9ad7f8689fc5f1876b811e6dc9fa6028e2a0a6e7da8b751: rewardbook-inputs-1793491200.tar of tz-44-l0-inputs, asset 742815436, api True, download 200 equal
[2026-11-17T14:18:56Z] P /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793577600.tar 16588800 67043eb13198b2c599b042b0385f06d925db74ff0f25e264e8555627dd987dbb: rewardbook-inputs-1793577600.tar of tz-44-l0-inputs, asset 742815512, api True, download 200 equal
[2026-11-17T14:18:57Z] P /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793664000.tar 16558080 92614b11fe80d5cca913c4633f2bcd0f96200ae0f0050ef2a74c68a491b67a45: rewardbook-inputs-1793664000.tar of tz-44-l0-inputs, asset 742815601, api True, download 200 equal
[2026-11-17T14:18:58Z] P /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793750400.tar 15513600 a8ec58f4cc250a12c63bcb743d7f0ddd03596e374990794a0c803167ad3e6442: rewardbook-inputs-1793750400.tar of tz-44-l0-inputs, asset 742815675, api True, download 200 equal
[2026-11-17T14:18:59Z] P /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793836800.tar 16117760 4179070b6d7add6a682f4d8f26664b2920b6113fe4119cf274b5460c437400e6: rewardbook-inputs-1793836800.tar of tz-44-l0-inputs, asset 742815751, api True, download 200 equal
[2026-11-17T14:19:00Z] P /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793923200.tar 15728640 ba31ef522351e3875dcd4e7ff1b7989787cc71515f82668972e037ba8612bf6f: rewardbook-inputs-1793923200.tar of tz-44-l0-inputs, asset 742815828, api True, download 200 equal
[2026-11-17T14:19:01Z] P /root/btc-forensics/tz44-work--out--rewardbook-inputs-1794009600.tar 15759360 df1e1592fbdc9425ce3ba8fc7ed3eec99458081b63ddf1c04eecb6c1a7651d45: rewardbook-inputs-1794009600.tar of tz-44-l0-inputs, asset 742815888, api True, download 200 equal
[2026-11-17T14:19:02Z] P /root/btc-forensics/tz44-work--out--rewardbook-inputs-1794096000.tar 16363520 0d8730b7a60cafaf47bf81ed5dcdc8bd8d68ca23ce9c86f70db06bbd02b1c2ec: rewardbook-inputs-1794096000.tar of tz-44-l0-inputs, asset 742815919, api True, download 200 equal
[2026-11-17T14:19:02Z] P /root/btc-forensics/tz44-work--out--tz44-manifest.json 392914 491dcaf037e15e26d25512b609afbe68655952f321d92fa8ef208ee966650c8b: tz44-manifest.json of tz-44-l0-inputs, asset 742817691, api True, download 200 equal
[2026-11-17T14:19:02Z] files proved against tz-44-l0-inputs: 47, at least 13 expected
[2026-11-17T14:19:02Z] FORENSICS PLAN: 47 files, 229053786 bytes, each held by a public Release and proved; 47 rows, 0 not proved; 6 API requests, 47 downloads, 229053786 bytes; forensics-plan.json sha256 becd4c5c35bd6484a659bd1c211d9a515401d73db13a1cab03aa43a6ee6f414f
[2026-11-17T14:19:02Z] peak memory of this run: 45858816 bytes
[2026-11-17T14:19:02Z] opens refused: 0; reward book opens: 0; API requests 6, downloads 47, 229053786 bytes; files removed 0
exit=0
```
B-FORENSICS, every `X` row and G-FORENSIC (`forensics-removed.jsonl`, 47 lines, SHA-256 `f95519f5b0b95474e979de30142914c32fc666f56146ed41146e35a8ae2de2a6`):
```
2026-11-17T14:19:16.260063361Z
[2026-11-17T14:19:16Z] MemAvailable read 1: 323493888 bytes, floor 133073162
[2026-11-17T14:19:16Z] free 8709038080 bytes, floor 2300000000
[2026-11-17T14:19:16Z] X /root/btc-forensics/tz43-work--days--1793404800.json 145864 d93f998fba7795f30379c06e2058c55f4eba9d0c340536a3d5a4d1636b765ee6 removed: tz43-days-1793404800.json of tz-44-l0-inputs
[2026-11-17T14:19:16Z] X /root/btc-forensics/tz43-work--days--1793404800.slots.txt 47260 ec4494031d22891f22ec2822287c0127c4f96f39dac1337f3980419813052400 removed: tz43-days-1793404800.slots.txt of tz-44-l0-inputs
[2026-11-17T14:19:16Z] X /root/btc-forensics/tz43-work--days--1793491200.json 147006 50e19969a8196ef3fe8b069056b75bb3ff5f5ba1c41a9ad70a48bd7e88ebaaae removed: tz43-days-1793491200.json of tz-44-l0-inputs
[2026-11-17T14:19:16Z] X /root/btc-forensics/tz43-work--days--1793491200.slots.txt 47077 5a7169dbcdb3186b588e2bd77ef5017dc792f1ead7cc8d2b9c11a55cee90f763 removed: tz43-days-1793491200.slots.txt of tz-44-l0-inputs
[2026-11-17T14:19:16Z] X /root/btc-forensics/tz43-work--days--1793577600.json 146744 93c76d1594b1edef03e192c02cc67b0264e43ca4b77b6d49939845f5876dc57c removed: tz43-days-1793577600.json of tz-44-l0-inputs
[2026-11-17T14:19:16Z] X /root/btc-forensics/tz43-work--days--1793577600.slots.txt 46799 aae9a59997c591b90672bec21ea2489e2f7e654eba03590bc8d1ff411a186e1c removed: tz43-days-1793577600.slots.txt of tz-44-l0-inputs
[2026-11-17T14:19:16Z] X /root/btc-forensics/tz43-work--days--1793664000.json 147691 a80c3d721fce47537ff927c42b989cd4409d25b7c3a1e2c4e024a2463d48c54d removed: tz43-days-1793664000.json of tz-44-l0-inputs
[2026-11-17T14:19:16Z] X /root/btc-forensics/tz43-work--days--1793664000.slots.txt 46785 dc9dff0e13153ee045ada2cb805c9567ce9bb4b490f88c40aa0821442fe8660b removed: tz43-days-1793664000.slots.txt of tz-44-l0-inputs
[2026-11-17T14:19:16Z] X /root/btc-forensics/tz43-work--days--1793750400.json 155059 4f9ca91d2798fb9f7b496e98baa02d4fe9f6efb5f60f979540f682fb7fdadfa9 removed: tz43-days-1793750400.json of tz-44-l0-inputs
[2026-11-17T14:19:16Z] X /root/btc-forensics/tz43-work--days--1793750400.slots.txt 47105 71101c5d670141ce064c671824d5c8c8c1615ffce4801b1a422baa3df4281cdc removed: tz43-days-1793750400.slots.txt of tz-44-l0-inputs
[2026-11-17T14:19:16Z] X /root/btc-forensics/tz43-work--days--1793836800.json 149722 e7266b1d2d05e1191095e9cd184e6bb15571ea7380fa1e4f51db90a5342e200d removed: tz43-days-1793836800.json of tz-44-l0-inputs
[2026-11-17T14:19:16Z] X /root/btc-forensics/tz43-work--days--1793836800.slots.txt 46750 ec5792be99ff4169b4574b3a8ce04855ad7a5fcd51aba1b51baf4cc9d8ce44e5 removed: tz43-days-1793836800.slots.txt of tz-44-l0-inputs
[2026-11-17T14:19:16Z] X /root/btc-forensics/tz43-work--days--1794009600.json 146104 f3018bb242bff3b1d7483622cd4065074cc42faa90b1e8357d223c2796a6dfd5 removed: tz43-days-1794009600.json of tz-44-l0-inputs
[2026-11-17T14:19:16Z] X /root/btc-forensics/tz43-work--days--1794009600.slots.txt 46914 a0fdb71edc318fb7e41989c1aca3b591c9b3e4db39274e87588354639725c1e6 removed: tz43-days-1794009600.slots.txt of tz-44-l0-inputs
[2026-11-17T14:19:16Z] X /root/btc-forensics/tz43-work--days--1794096000.json 144626 910ed69e85ab28dc81a334538d229a66ba17107260325c1afe5eae95de02e91f removed: tz43-days-1794096000.json of tz-44-l0-inputs
[2026-11-17T14:19:16Z] X /root/btc-forensics/tz43-work--days--1794096000.slots.txt 46970 00caaab0888d85779398751281da3e9219cfdf9742c77b5914499cf0c4421436 removed: tz43-days-1794096000.slots.txt of tz-44-l0-inputs
[2026-11-17T14:19:16Z] X /root/btc-forensics/tz43-work--fetch--1793404800.json 55310 5f56487e44aadcba1df2bc1316a889605baf83a4fcafc965b5ee4a18a6fec9b2 removed: tz43-fetch-1793404800.json of tz-44-l0-inputs
[2026-11-17T14:19:16Z] X /root/btc-forensics/tz43-work--fetch--1793404800.polls.jsonl 4990923 53ae4e79d354b3f8b35d497654159162b9c2290deb0d69b6f62b79c3fe8c1d71 removed: tz43-fetch-1793404800.polls.jsonl of tz-44-l0-inputs
[2026-11-17T14:19:16Z] X /root/btc-forensics/tz43-work--fetch--1793491200.json 55330 55f95448c4ba6abe1d1b154ff0e014ef190ffb7be861a7f6cb1a3bcddec7a1bd removed: tz43-fetch-1793491200.json of tz-44-l0-inputs
[2026-11-17T14:19:16Z] X /root/btc-forensics/tz43-work--fetch--1793491200.polls.jsonl 5010687 1aac9148f26b55664b248be60b62394defc1b117b63bcd952c632bf96b3ebf54 removed: tz43-fetch-1793491200.polls.jsonl of tz-44-l0-inputs
[2026-11-17T14:19:16Z] X /root/btc-forensics/tz43-work--fetch--1793577600.json 55447 8589729bfe267feb57208833064bc71006e592e22edd8290d70bbc2b4474d9b5 removed: tz43-fetch-1793577600.json of tz-44-l0-inputs
[2026-11-17T14:19:17Z] X /root/btc-forensics/tz43-work--fetch--1793577600.polls.jsonl 5027379 19d765c78c93e9d4175328615ae3dc27b3e2f0c1dd7f6084eeab672a9e56427c removed: tz43-fetch-1793577600.polls.jsonl of tz-44-l0-inputs
[2026-11-17T14:19:17Z] X /root/btc-forensics/tz43-work--fetch--1793664000.json 55449 1405b48ac2459f052b5b36dea8e85dd6cb0e112b49ac21030955d96f890eec02 removed: tz43-fetch-1793664000.json of tz-44-l0-inputs
[2026-11-17T14:19:17Z] X /root/btc-forensics/tz43-work--fetch--1793664000.polls.jsonl 5014920 4a5ef449ed6b1d2bf1378b817671b9bb3cac477c5a9fa6e5068d9673b24977cb removed: tz43-fetch-1793664000.polls.jsonl of tz-44-l0-inputs
[2026-11-17T14:19:17Z] X /root/btc-forensics/tz43-work--fetch--1793750400.json 55543 1ed8768bd80b54220c0437e15fc424943a8829b716d7ba70f2b586f5ae14099c removed: tz43-fetch-1793750400.json of tz-44-l0-inputs
[2026-11-17T14:19:17Z] X /root/btc-forensics/tz43-work--fetch--1793750400.polls.jsonl 4967708 f06145aa32845b9f3a65b8616e5842218b03869a3fc18d5a4bf1aaaa57fec920 removed: tz43-fetch-1793750400.polls.jsonl of tz-44-l0-inputs
[2026-11-17T14:19:17Z] X /root/btc-forensics/tz43-work--fetch--1793836800.json 55625 7d502a56ad2a4a3f95150bbcfc8c52c1190f2b977d9d1a72e2e1c4b3c2f5ba25 removed: tz43-fetch-1793836800.json of tz-44-l0-inputs
[2026-11-17T14:19:17Z] X /root/btc-forensics/tz43-work--fetch--1793836800.polls.jsonl 5055307 7918f3b6629489fcff4fd22cdb049a89e1e1ef63b86738c73ec680e17e5eff5d removed: tz43-fetch-1793836800.polls.jsonl of tz-44-l0-inputs
[2026-11-17T14:19:17Z] X /root/btc-forensics/tz43-work--fetch--1794009600.json 55639 29e17ecde5f5d705e297bdc2be7e5e150aa50d06c3ac66ba9b1c4c13225b5708 removed: tz43-fetch-1794009600.json of tz-44-l0-inputs
[2026-11-17T14:19:17Z] X /root/btc-forensics/tz43-work--fetch--1794009600.polls.jsonl 5037697 91582ccfb9145559277d196f61e804e6be205d0b18d6168a1db6975711d6cf15 removed: tz43-fetch-1794009600.polls.jsonl of tz-44-l0-inputs
[2026-11-17T14:19:17Z] X /root/btc-forensics/tz43-work--fetch--1794096000.json 55660 a3ebc56744facb5c00f862c1f5d70a564672b68b5cc276398f32ae7f1bc0c552 removed: tz43-fetch-1794096000.json of tz-44-l0-inputs
[2026-11-17T14:19:17Z] X /root/btc-forensics/tz43-work--fetch--1794096000.polls.jsonl 5047340 7b0d86338359fbb4d5f4f7b54c6f36e0d45f2ed5c4d6d5731358c8e4e3099a82 removed: tz43-fetch-1794096000.polls.jsonl of tz-44-l0-inputs
[2026-11-17T14:19:17Z] X /root/btc-forensics/tz43-work--reading.json 9377 175d366101cd825437a1cd393aa57642965f7ffb9fe831746c2d9b2187d50be1 removed: tz43-reading.json of tz-44-l0-inputs
[2026-11-17T14:19:17Z] X /root/btc-forensics/tz43-work--set.json 6175 904f1b9b8244a15fe48549e39ffc879f68ad31de6963a41c05f5afc607edf0f7 removed: tz43-set.json of tz-44-l0-inputs
[2026-11-17T14:19:17Z] X /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793145600.tar 9256960 b268ef086a2d2d23afa6cb33b354eddd0d3589aca1621aa15901b6441667f9f6 removed: rewardbook-inputs-1793145600.tar of tz-44-l0-inputs
[2026-11-17T14:19:17Z] X /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793232000.tar 15482880 b214536add4d9b43cd6f634cd8c26cb92d9f82b0c6bd6508564a8b21a2529dc1 removed: rewardbook-inputs-1793232000.tar of tz-44-l0-inputs
[2026-11-17T14:19:17Z] X /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793318400.tar 16384000 e3189d4cf76f5acb2a14351610c7ea9dc1bd294e19cee310eef80b421b2b910f removed: rewardbook-inputs-1793318400.tar of tz-44-l0-inputs
[2026-11-17T14:19:17Z] X /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793404800.tar 16445440 563a3ccf2df5e48641dff892de6f50d4421c071cd42ae7cbb147b3ed8b2f3c1f removed: rewardbook-inputs-1793404800.tar of tz-44-l0-inputs
[2026-11-17T14:19:17Z] X /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793491200.tar 16291840 0614a35f95eb4fe7f9ad7f8689fc5f1876b811e6dc9fa6028e2a0a6e7da8b751 removed: rewardbook-inputs-1793491200.tar of tz-44-l0-inputs
[2026-11-17T14:19:17Z] X /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793577600.tar 16588800 67043eb13198b2c599b042b0385f06d925db74ff0f25e264e8555627dd987dbb removed: rewardbook-inputs-1793577600.tar of tz-44-l0-inputs
[2026-11-17T14:19:17Z] X /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793664000.tar 16558080 92614b11fe80d5cca913c4633f2bcd0f96200ae0f0050ef2a74c68a491b67a45 removed: rewardbook-inputs-1793664000.tar of tz-44-l0-inputs
[2026-11-17T14:19:17Z] X /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793750400.tar 15513600 a8ec58f4cc250a12c63bcb743d7f0ddd03596e374990794a0c803167ad3e6442 removed: rewardbook-inputs-1793750400.tar of tz-44-l0-inputs
[2026-11-17T14:19:17Z] X /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793836800.tar 16117760 4179070b6d7add6a682f4d8f26664b2920b6113fe4119cf274b5460c437400e6 removed: rewardbook-inputs-1793836800.tar of tz-44-l0-inputs
[2026-11-17T14:19:17Z] X /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793923200.tar 15728640 ba31ef522351e3875dcd4e7ff1b7989787cc71515f82668972e037ba8612bf6f removed: rewardbook-inputs-1793923200.tar of tz-44-l0-inputs
[2026-11-17T14:19:17Z] X /root/btc-forensics/tz44-work--out--rewardbook-inputs-1794009600.tar 15759360 df1e1592fbdc9425ce3ba8fc7ed3eec99458081b63ddf1c04eecb6c1a7651d45 removed: rewardbook-inputs-1794009600.tar of tz-44-l0-inputs
[2026-11-17T14:19:17Z] X /root/btc-forensics/tz44-work--out--rewardbook-inputs-1794096000.tar 16363520 0d8730b7a60cafaf47bf81ed5dcdc8bd8d68ca23ce9c86f70db06bbd02b1c2ec removed: rewardbook-inputs-1794096000.tar of tz-44-l0-inputs
[2026-11-17T14:19:17Z] X /root/btc-forensics/tz44-work--out--tz44-manifest.json 392914 491dcaf037e15e26d25512b609afbe68655952f321d92fa8ef208ee966650c8b removed: tz44-manifest.json of tz-44-l0-inputs
[2026-11-17T14:19:17Z] G-FORENSIC every planned file absent                    True
[2026-11-17T14:19:17Z] G-FORENSIC every removal recorded once                  True
[2026-11-17T14:19:17Z] G-FORENSIC the store less exactly the planned files     True
[2026-11-17T14:19:17Z] G-FORENSIC PASS: 47 of 47 removed, 229053786 bytes; this run 47 files, 229053786 bytes; free 8709017600 before, 8938147840 after
[2026-11-17T14:19:17Z] peak memory of this run: 28332032 bytes
[2026-11-17T14:19:17Z] opens refused: 0; reward book opens: 0; API requests 0, downloads 0, 0 bytes; files removed 47
exit=0
```
The store went from 2,579 files and 584,947,343 bytes to 2,532 files and 355,893,557 bytes. Free space went from 8,709,038,080 to 8,938,147,840.

### 2.4 The pair book — B-PAIR-OFF, whole

The final run is `1794925184`, started by hand at 14:19:44Z after the `pairoff` mark at 14:19:44Z. It moved 46 stream files, 1,151,737,742 bytes, to Release `448733841` under tag `pairbook-streams-1794925184` at `d8194fd…`. It restarted the pair book (pid 2012336 → 2080877, `NRestarts` 7) for window 1794925800, its resume read `PASS`, and it ended `complete` with `started_outside 0` and `ended_outside 0`. `pairwait=0`. Both `systemctl disable --now` stops ran at 14:45:45–47Z, each exiting `0`. G-PAIR: **8 of 8**. The residual is two windows, 1794924900 (18,799,261 bytes) and 1794925800 (23,668,756 bytes): 42,468,017 bytes in all.
```
2026-11-17T14:19:44.121175020Z
[2026-11-17T14:19:44Z] band pairoff OPEN: second 51584 of the day, the band 27000 to 68400
[2026-11-17T14:19:44Z] peak memory of this run: 26206208 bytes
[2026-11-17T14:19:44Z] opens refused: 0; reward book opens: 0; API requests 0, downloads 0, 0 bytes; files removed 0
[2026-11-17T14:19:44Z] adv3-bot.service {'MainPID': '1555970', 'NRestarts': '0', 'ActiveState': 'active'}, UnitFileState enabled, MemoryCurrent 5914624, MemoryPeak 48467968
[2026-11-17T14:19:44Z] btc-pairbook.service {'MainPID': '2012336', 'NRestarts': '6', 'ActiveState': 'active'}, UnitFileState enabled, MemoryCurrent 1982464, MemoryPeak 64192512
[2026-11-17T14:19:44Z] btc-recorder.service {'MainPID': '1555954', 'NRestarts': '0', 'ActiveState': 'active'}, UnitFileState enabled, MemoryCurrent 12767232, MemoryPeak 390193152
[2026-11-17T14:19:44Z] btc-rewardbook.service {'MainPID': '1556307', 'NRestarts': '0', 'ActiveState': 'active'}, UnitFileState enabled, MemoryCurrent 16920576, MemoryPeak 45936640
[2026-11-17T14:19:44Z] btc-rewardbook-archive.timer {'NextElapseUSecRealtime': 'Wed 2026-11-18 01:30:20 UTC', 'LastTriggerUSec': 'Tue 2026-11-17 01:30:20 UTC', 'Result': 'success', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-11-17T14:19:44Z] btc-rewardbook-archive.service {'Result': 'success', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-11-17T14:19:44Z] btc-pairbook-archive.timer {'NextElapseUSecRealtime': 'Wed 2026-11-18 03:00:20 UTC', 'LastTriggerUSec': 'Tue 2026-11-17 03:00:20 UTC', 'Result': 'success', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-11-17T14:19:44Z] btc-pairbook-archive.service {'Result': 'success', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-11-17T14:19:44Z] mark pairoff at 2026-11-17T14:19:44Z
[2026-11-17T14:19:44Z] peak memory of this run: 26341376 bytes
[2026-11-17T14:19:44Z] opens refused: 0; reward book opens: 0; API requests 0, downloads 0, 0 bytes; files removed 0
2026-11-17T14:19:44.517166384Z
[2026-11-17T14:45:45Z] R {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "14794a6f9074429b9abe8d602efe0867", "phase_at": 284, "resumed": false, "run": 1794925184, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1794925184718301895}
[2026-11-17T14:45:45Z] R {"assets_n": 46, "bytes_total": 1151737742, "closed": 3627, "deferred": 0, "event": "set", "first_T": 1794883500, "last_T": 1794924000, "open": 0, "run": 1794925184, "sha256": "0dc6ad3a1d72f3a994b863e19f27d078c1ba14967352aa4708a69b5c5f51f770", "tag": "pairbook-streams-1794925184", "unclosed": 0, "wall_ns": 1794925187999550923, "windows_considered": 3627}
[2026-11-17T14:45:45Z] R {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 448733841, "run": 1794925184, "sent": 46, "wall_ns": 1794925293719407612}
[2026-11-17T14:45:45Z] R {"assets_n": 46, "bytes_total": 1151737742, "event": "verify", "release_id": 448733841, "run": 1794925184, "verify_sha256": "97ac1d26e90007de8eed71aca41e7db83973e71c026ea4a61ff803d6eaac99e7", "wall_ns": 1794925965687292163}
[2026-11-17T14:45:45Z] R {"already": 0, "event": "delete", "free_after": 10056265728, "free_before": 8904314880, "freed": 1151737742, "gone": 46, "removed": 46, "run": 1794925184, "wall_ns": 1794925968357751566, "windows_kept": 46}
[2026-11-17T14:45:45Z] R {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "2012336", "NRestarts": "6", "ns": 1794925968395287827}, "phase": 168, "run": 1794925184, "wall_ns": 1794925968395480332}
[2026-11-17T14:45:45Z] R {"event": "kill", "exit": 0, "phase": 168, "run": 1794925184, "wall_ns": 1794925968400672033}
[2026-11-17T14:45:45Z] R {"NRestarts": "7", "W": 1794925800, "event": "restart", "free_bytes": 10056183808, "gap_ns": 6164444294, "pid": 2080877, "run": 1794925184, "stopped": 2012336, "stream_bytes": 18799261, "wall_ns": 1794925998527009819}
[2026-11-17T14:45:45Z] R {"T": 1794925800, "event": "resume", "reading": "PASS", "run": 1794925184, "wall_ns": 1794926741047976078}
[2026-11-17T14:45:45Z] R {"assets_n": 46, "bytes_total": 1151737742, "ended_outside": 0, "event": "complete", "free_bytes": 10019958784, "peak_rss": 38199296, "rate_per_day": 2403626592, "requests": 97, "run": 1794925184, "started_outside": 0, "stops": [["the cap", 1795212779], ["the floor, base 43500000 bytes a day", 1795121632], ["the floor, base 187760570 bytes a day", 1795110783]], "store_stream_bytes": 42468017, "wall_ns": 1794926741621860011}
[2026-11-17T14:45:45Z] PAIRWAIT run 1794925184: complete; the service inactive, Result success, ExecMainStatus 0
[2026-11-17T14:45:45Z] peak memory of this run: 27787264 bytes
[2026-11-17T14:45:45Z] opens refused: 0; reward book opens: 0; API requests 0, downloads 0, 0 bytes; files removed 0
pairwait=0
2026-11-17T14:45:45.732620982Z
Removed "/etc/systemd/system/timers.target.wants/btc-pairbook-archive.timer".
timer exit=0
Removed "/etc/systemd/system/multi-user.target.wants/btc-pairbook.service".
pairbook exit=0
2026-11-17T14:45:47.389894682Z
[2026-11-17T14:46:17Z] R {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "14794a6f9074429b9abe8d602efe0867", "phase_at": 284, "resumed": false, "run": 1794925184, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1794925184718301895}
[2026-11-17T14:46:17Z] R {"assets_n": 46, "bytes_total": 1151737742, "closed": 3627, "deferred": 0, "event": "set", "first_T": 1794883500, "last_T": 1794924000, "open": 0, "run": 1794925184, "sha256": "0dc6ad3a1d72f3a994b863e19f27d078c1ba14967352aa4708a69b5c5f51f770", "tag": "pairbook-streams-1794925184", "unclosed": 0, "wall_ns": 1794925187999550923, "windows_considered": 3627}
[2026-11-17T14:46:17Z] R {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 448733841, "run": 1794925184, "sent": 46, "wall_ns": 1794925293719407612}
[2026-11-17T14:46:17Z] R {"assets_n": 46, "bytes_total": 1151737742, "event": "verify", "release_id": 448733841, "run": 1794925184, "verify_sha256": "97ac1d26e90007de8eed71aca41e7db83973e71c026ea4a61ff803d6eaac99e7", "wall_ns": 1794925965687292163}
[2026-11-17T14:46:17Z] R {"already": 0, "event": "delete", "free_after": 10056265728, "free_before": 8904314880, "freed": 1151737742, "gone": 46, "removed": 46, "run": 1794925184, "wall_ns": 1794925968357751566, "windows_kept": 46}
[2026-11-17T14:46:17Z] R {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "2012336", "NRestarts": "6", "ns": 1794925968395287827}, "phase": 168, "run": 1794925184, "wall_ns": 1794925968395480332}
[2026-11-17T14:46:17Z] R {"event": "kill", "exit": 0, "phase": 168, "run": 1794925184, "wall_ns": 1794925968400672033}
[2026-11-17T14:46:17Z] R {"NRestarts": "7", "W": 1794925800, "event": "restart", "free_bytes": 10056183808, "gap_ns": 6164444294, "pid": 2080877, "run": 1794925184, "stopped": 2012336, "stream_bytes": 18799261, "wall_ns": 1794925998527009819}
[2026-11-17T14:46:17Z] R {"T": 1794925800, "event": "resume", "reading": "PASS", "run": 1794925184, "wall_ns": 1794926741047976078}
[2026-11-17T14:46:17Z] R {"assets_n": 46, "bytes_total": 1151737742, "ended_outside": 0, "event": "complete", "free_bytes": 10019958784, "peak_rss": 38199296, "rate_per_day": 2403626592, "requests": 97, "run": 1794925184, "started_outside": 0, "stops": [["the cap", 1795212779], ["the floor, base 43500000 bytes a day", 1795121632], ["the floor, base 187760570 bytes a day", 1795110783]], "store_stream_bytes": 42468017, "wall_ns": 1794926741621860011}
[2026-11-17T14:46:17Z] the run begun or resumed after the pairoff mark: 1794925184; the tag pairbook-streams-1794925184 at d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3, peeled None; the archive's commit d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3
[2026-11-17T14:46:17Z] the pair book {'MainPID': '0', 'Result': 'success', 'NRestarts': '0', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'disabled'}; its archive's timer {'NextElapseUSecRealtime': '', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'disabled'}; its archive's service {'Result': 'success', 'ExecMainStatus': '0', 'ActiveState': 'inactive'}; processes of the pair book []
[2026-11-17T14:46:18Z] RESIDUAL window 1794924900 2026-11-17T14:15:00Z: 18799261 bytes of stream
[2026-11-17T14:46:18Z] RESIDUAL window 1794925800 2026-11-17T14:30:00Z: 23668756 bytes of stream
[2026-11-17T14:46:18Z] the pair book's store: 2 stream files, 42468017 bytes, in 2 windows; 10890 other files, 104167525 bytes
[2026-11-17T14:46:18Z] G-PAIR the run complete                               True
[2026-11-17T14:46:18Z] G-PAIR the pair book restarted and resumed by it      True
[2026-11-17T14:46:18Z] G-PAIR every request inside the idle stretch          True
[2026-11-17T14:46:18Z] G-PAIR its tag at the archive's commit                True
[2026-11-17T14:46:18Z] G-PAIR the pair book stopped and disabled             True
[2026-11-17T14:46:18Z] G-PAIR no process of the pair book                    True
[2026-11-17T14:46:18Z] G-PAIR its archive's timer stopped and disabled       True
[2026-11-17T14:46:18Z] G-PAIR its archive's service idle                     True
[2026-11-17T14:46:18Z] G-PAIR PASS: 8 of 8
[2026-11-17T14:46:18Z] peak memory of this run: 27910144 bytes
[2026-11-17T14:46:18Z] opens refused: 0; reward book opens: 0; API requests 0, downloads 0, 0 bytes; files removed 0
pair exit=0
exit=0
```
### 2.5 The timer — B-TIMER, whole, and G-TIMER again

The band wait (`60-band-timer.log`) made 80 reads from 14:46:40Z, 79 closed (`exit=3`), and opened at 16:05:48Z. Its last two reads:
```
Tue Nov 17 04:04:48 PM UTC 2026
[2026-11-17T16:04:48Z] band timer closed: second 57888 of the day, 3888 of its step; the next elapse 2026-11-17T16:30:20Z
[2026-11-17T16:04:48Z] peak memory of this run: 26337280 bytes
[2026-11-17T16:04:48Z] opens refused: 0; reward book opens: 0; API requests 0, downloads 0, 0 bytes; files removed 0
Tue Nov 17 04:05:48 PM UTC 2026
[2026-11-17T16:05:48Z] band timer OPEN: second 57948 of the day, 3948 of its step; the next elapse 2026-11-17T16:30:20Z
[2026-11-17T16:05:48Z] peak memory of this run: 26337280 bytes
[2026-11-17T16:05:48Z] opens refused: 0; reward book opens: 0; API requests 0, downloads 0, 0 bytes; files removed 0
exit=0
```
```
2026-11-17T16:05:48.989805527Z
[2026-11-17T16:05:49Z] band timer OPEN: second 57949 of the day, 3949 of its step; the next elapse 2026-11-17T16:30:20Z
[2026-11-17T16:05:49Z] peak memory of this run: 26337280 bytes
[2026-11-17T16:05:49Z] opens refused: 0; reward book opens: 0; API requests 0, downloads 0, 0 bytes; files removed 0
[2026-11-17T16:05:49Z] adv3-bot.service {'MainPID': '1555970', 'NRestarts': '0', 'ActiveState': 'active'}, UnitFileState enabled, MemoryCurrent 5648384, MemoryPeak 48467968
[2026-11-17T16:05:49Z] btc-pairbook.service {'MainPID': '0', 'NRestarts': '0', 'ActiveState': 'inactive'}, UnitFileState disabled, MemoryCurrent [not set], MemoryPeak [not set]
[2026-11-17T16:05:49Z] btc-recorder.service {'MainPID': '1555954', 'NRestarts': '0', 'ActiveState': 'active'}, UnitFileState enabled, MemoryCurrent 235696128, MemoryPeak 390193152
[2026-11-17T16:05:49Z] btc-rewardbook.service {'MainPID': '1556307', 'NRestarts': '0', 'ActiveState': 'active'}, UnitFileState enabled, MemoryCurrent 20254720, MemoryPeak 45936640
[2026-11-17T16:05:49Z] btc-rewardbook-archive.timer {'NextElapseUSecRealtime': 'Wed 2026-11-18 01:30:20 UTC', 'LastTriggerUSec': 'Tue 2026-11-17 15:15:47 UTC', 'Result': 'success', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-11-17T16:05:49Z] btc-rewardbook-archive.service {'Result': 'success', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-11-17T16:05:49Z] btc-pairbook-archive.timer {'NextElapseUSecRealtime': '', 'LastTriggerUSec': '', 'Result': 'success', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'disabled'}
[2026-11-17T16:05:49Z] btc-pairbook-archive.service {'Result': 'success', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-11-17T16:05:49Z] mark timer at 2026-11-17T16:05:49Z
[2026-11-17T16:05:49Z] peak memory of this run: 26337280 bytes
[2026-11-17T16:05:49Z] opens refused: 0; reward book opens: 0; API requests 0, downloads 0, 0 bytes; files removed 0
2026-11-17T16:05:49.301191338Z
2026-11-17T16:05:49.700035388Z
[2026-11-17T16:05:54Z] the timer: {'Unit': 'btc-rewardbook-archive.service', 'TimersCalendar': '{ OnCalendar=*-*-* 01/3:30:20 UTC ; next_elapse=Tue 2026-11-17 16:30:20 UTC }', 'NextElapseUSecRealtime': 'Tue 2026-11-17 16:30:20 UTC', 'NextElapseUSecMonotonic': '0', 'LastTriggerUSec': 'Tue 2026-11-17 15:15:47 UTC', 'AccuracyUSec': '1s', 'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'waiting', 'FragmentPath': '/etc/systemd/system/btc-rewardbook-archive.timer', 'UnitFileState': 'enabled', 'ActiveEnterTimestamp': 'Tue 2026-11-17 16:05:49 UTC'}; installed sha256 7b0804285af6987340838bd59573897d013cf97edc5d4132cda7f3f9ba3e3824; the pair book archive's timer {'ActiveState': 'inactive', 'UnitFileState': 'disabled'}
[2026-11-17T16:05:54Z] G-TIMER loaded                                               True
[2026-11-17T16:05:54Z] G-TIMER active, waiting or running                           True
[2026-11-17T16:05:54Z] G-TIMER enabled                                              True
[2026-11-17T16:05:54Z] G-TIMER its fragment                                         True
[2026-11-17T16:05:54Z] G-TIMER its unit                                             True
[2026-11-17T16:05:54Z] G-TIMER one calendar, every third hour from 01:30:20 UTC     True
[2026-11-17T16:05:54Z] G-TIMER no run on a start of the timer                       True
[2026-11-17T16:05:54Z] G-TIMER accuracy 1 s                                         True
[2026-11-17T16:05:54Z] G-TIMER the next elapse the calendar's                       True
[2026-11-17T16:05:54Z] G-TIMER installed byte for byte                              True
[2026-11-17T16:05:54Z] G-TIMER the pair book archive's timer stopped and disabled   True
[2026-11-17T16:05:54Z] G-TIMER PASS: 11 of 11; the next run at 2026-11-17T16:30:20Z
[2026-11-17T16:05:54Z] peak memory of this run: 26337280 bytes
[2026-11-17T16:05:54Z] opens refused: 0; reward book opens: 0; API requests 0, downloads 0, 0 bytes; files removed 0
exit=0
```
```
Tue Nov 17 05:01:55 PM UTC 2026
[2026-11-17T17:01:55Z] the timer: {'Unit': 'btc-rewardbook-archive.service', 'TimersCalendar': '{ OnCalendar=*-*-* 01/3:30:20 UTC ; next_elapse=Tue 2026-11-17 19:30:20 UTC }', 'NextElapseUSecRealtime': 'Tue 2026-11-17 19:30:20 UTC', 'NextElapseUSecMonotonic': '0', 'LastTriggerUSec': 'Tue 2026-11-17 16:30:20 UTC', 'AccuracyUSec': '1s', 'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'waiting', 'FragmentPath': '/etc/systemd/system/btc-rewardbook-archive.timer', 'UnitFileState': 'enabled', 'ActiveEnterTimestamp': 'Tue 2026-11-17 16:05:49 UTC'}; installed sha256 7b0804285af6987340838bd59573897d013cf97edc5d4132cda7f3f9ba3e3824; the pair book archive's timer {'ActiveState': 'inactive', 'UnitFileState': 'disabled'}
[2026-11-17T17:01:55Z] G-TIMER loaded                                               True
[2026-11-17T17:01:55Z] G-TIMER active, waiting or running                           True
[2026-11-17T17:01:55Z] G-TIMER enabled                                              True
[2026-11-17T17:01:55Z] G-TIMER its fragment                                         True
[2026-11-17T17:01:55Z] G-TIMER its unit                                             True
[2026-11-17T17:01:55Z] G-TIMER one calendar, every third hour from 01:30:20 UTC     True
[2026-11-17T17:01:55Z] G-TIMER no run on a start of the timer                       True
[2026-11-17T17:01:55Z] G-TIMER accuracy 1 s                                         True
[2026-11-17T17:01:55Z] G-TIMER the next elapse the calendar's                       True
[2026-11-17T17:01:55Z] G-TIMER installed byte for byte                              True
[2026-11-17T17:01:55Z] G-TIMER the pair book archive's timer stopped and disabled   True
[2026-11-17T17:01:55Z] G-TIMER PASS: 11 of 11; the next run at 2026-11-17T19:30:20Z
[2026-11-17T17:01:55Z] peak memory of this run: 26075136 bytes
[2026-11-17T17:01:55Z] opens refused: 0; reward book opens: 0; API requests 0, downloads 0, 0 bytes; files removed 0
exit=0
```
### 2.6 The first run on the new calendar

The first elapse after the `timer` mark (16:05:49Z) was E = 16:30:20Z. Run `1794933020` started at 16:30:20Z, by `TRIGGER_UNIT` `btc-rewardbook-archive.timer`, trigger 16:30:20Z, as a new set. **No start record falls between the mark and E.** The run took 5 files, 71,537,680 bytes, of slots 1794927600 to 1794931200, to Release `448903582` under tag `rewardbook-streams-1794933020` (lightweight, at `6a61525…`). It made 15 requests and 5 removals, 0 started and 0 ended outside the idle stretch. Free space went 10,566,414,336 → 10,637,975,552. The service ran 16:30:20 to 16:32:46 UTC, `Result success`, `ExecMainStatus 0`. G-NEXT covered one slot, 1794933900, decided at 16:44:54Z and streamed by the reward book's process 1556307. B-RETRY did not run. Every `first` read:
```
Tue Nov 17 04:31:29 PM UTC 2026
[2026-11-17T16:31:29Z] NOT YET: run 1794933020 running; the service activating
[2026-11-17T16:31:29Z] peak memory of this run: 26603520 bytes
[2026-11-17T16:31:29Z] opens refused: 0; reward book opens: 0; API requests 0, downloads 0, 0 bytes; files removed 0
exit=3
Tue Nov 17 04:36:29 PM UTC 2026
[2026-11-17T16:36:29Z] R {"commit": "6a615257277d3c94dafd4d39783499560a344648", "event": "start", "file_sha256": "1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72", "invocation": "f3aea761826943c6917151346afe0a37", "phase_at": 20, "resumed": false, "rewardbook": {"ActiveState": "active", "MainPID": "1556307", "NRestarts": "0"}, "run": 1794933020, "trigger": {"monotonic_usec": "9277548091323", "realtime_usec": "1794933020369808", "unit": "btc-rewardbook-archive.timer"}, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "tz28_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "wall_ns": 1794933020661142457}
[2026-11-17T16:36:29Z] R {"assets_n": 5, "bytes_total": 71537680, "closed": 5, "deferred": 0, "event": "set", "first_S": 1794927600, "last_S": 1794931200, "open": 2, "run": 1794933020, "sha256": "a3e8f70b8b44d873e420ef9f2a8f83f019b168fbe9f114e2424dbadce279ebd3", "slots_considered": 5, "streamless": 1934, "tag": "rewardbook-streams-1794933020", "unclosed": 0, "wall_ns": 1794933020840827849}
[2026-11-17T16:36:29Z] R {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 448903582, "run": 1794933020, "sent": 5, "wall_ns": 1794933030746952886}
[2026-11-17T16:36:29Z] R {"assets_n": 5, "bytes_total": 71537680, "event": "verify", "release_id": 448903582, "run": 1794933020, "verify_sha256": "0e8556fe68e05eb4f85569d8879f818f503be4c3990919afb9c17e2b2dd20dd5", "wall_ns": 1794933166522886046}
[2026-11-17T16:36:29Z] R {"already": 0, "event": "delete", "free_after": 10637975552, "free_before": 10566414336, "freed": 71537680, "gone": 5, "quiet_s": 0, "removed": 5, "run": 1794933020, "slots_kept": 5, "wall_ns": 1794933166737779085}
[2026-11-17T16:36:29Z] R {"assets_n": 5, "bytes_total": 71537680, "ended_outside": 0, "event": "complete", "free_bytes": 10637971456, "held_s": 0, "peak_rss": 39821312, "rate_per_day": 1373523456, "removals": 5, "requests": 15, "rewardbook_at_end": {"ActiveState": "active", "MainPID": "1556307", "NRestarts": "0"}, "rewardbook_at_start": {"ActiveState": "active", "MainPID": "1556307", "NRestarts": "0"}, "run": 1794933020, "started_outside": 0, "stops": [["the cap", 1795183699], ["the floor, base 43500000 bytes a day", 1795136691], ["the floor, base 187760570 bytes a day", 1795117886]], "store_stream_bytes": 17204028, "wall_ns": 1794933166747222228}
[2026-11-17T16:36:29Z] NOT YET: run 1794933020 complete; G-NEXT's last slot 1794933900 is due at 2026-11-17T17:00:40Z
[2026-11-17T16:36:29Z] peak memory of this run: 26468352 bytes
[2026-11-17T16:36:29Z] opens refused: 0; reward book opens: 0; API requests 0, downloads 0, 0 bytes; files removed 0
exit=3
Tue Nov 17 04:41:29 PM UTC 2026
[2026-11-17T16:41:30Z] R {"commit": "6a615257277d3c94dafd4d39783499560a344648", "event": "start", "file_sha256": "1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72", "invocation": "f3aea761826943c6917151346afe0a37", "phase_at": 20, "resumed": false, "rewardbook": {"ActiveState": "active", "MainPID": "1556307", "NRestarts": "0"}, "run": 1794933020, "trigger": {"monotonic_usec": "9277548091323", "realtime_usec": "1794933020369808", "unit": "btc-rewardbook-archive.timer"}, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "tz28_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "wall_ns": 1794933020661142457}
[2026-11-17T16:41:30Z] R {"assets_n": 5, "bytes_total": 71537680, "closed": 5, "deferred": 0, "event": "set", "first_S": 1794927600, "last_S": 1794931200, "open": 2, "run": 1794933020, "sha256": "a3e8f70b8b44d873e420ef9f2a8f83f019b168fbe9f114e2424dbadce279ebd3", "slots_considered": 5, "streamless": 1934, "tag": "rewardbook-streams-1794933020", "unclosed": 0, "wall_ns": 1794933020840827849}
[2026-11-17T16:41:30Z] R {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 448903582, "run": 1794933020, "sent": 5, "wall_ns": 1794933030746952886}
[2026-11-17T16:41:30Z] R {"assets_n": 5, "bytes_total": 71537680, "event": "verify", "release_id": 448903582, "run": 1794933020, "verify_sha256": "0e8556fe68e05eb4f85569d8879f818f503be4c3990919afb9c17e2b2dd20dd5", "wall_ns": 1794933166522886046}
[2026-11-17T16:41:30Z] R {"already": 0, "event": "delete", "free_after": 10637975552, "free_before": 10566414336, "freed": 71537680, "gone": 5, "quiet_s": 0, "removed": 5, "run": 1794933020, "slots_kept": 5, "wall_ns": 1794933166737779085}
[2026-11-17T16:41:30Z] R {"assets_n": 5, "bytes_total": 71537680, "ended_outside": 0, "event": "complete", "free_bytes": 10637971456, "held_s": 0, "peak_rss": 39821312, "rate_per_day": 1373523456, "removals": 5, "requests": 15, "rewardbook_at_end": {"ActiveState": "active", "MainPID": "1556307", "NRestarts": "0"}, "rewardbook_at_start": {"ActiveState": "active", "MainPID": "1556307", "NRestarts": "0"}, "run": 1794933020, "started_outside": 0, "stops": [["the cap", 1795183699], ["the floor, base 43500000 bytes a day", 1795136691], ["the floor, base 187760570 bytes a day", 1795117886]], "store_stream_bytes": 17204028, "wall_ns": 1794933166747222228}
[2026-11-17T16:41:30Z] NOT YET: run 1794933020 complete; G-NEXT's last slot 1794933900 is due at 2026-11-17T17:00:40Z
[2026-11-17T16:41:30Z] peak memory of this run: 26730496 bytes
[2026-11-17T16:41:30Z] opens refused: 0; reward book opens: 0; API requests 0, downloads 0, 0 bytes; files removed 0
exit=3
Tue Nov 17 04:46:30 PM UTC 2026
[2026-11-17T16:46:30Z] R {"commit": "6a615257277d3c94dafd4d39783499560a344648", "event": "start", "file_sha256": "1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72", "invocation": "f3aea761826943c6917151346afe0a37", "phase_at": 20, "resumed": false, "rewardbook": {"ActiveState": "active", "MainPID": "1556307", "NRestarts": "0"}, "run": 1794933020, "trigger": {"monotonic_usec": "9277548091323", "realtime_usec": "1794933020369808", "unit": "btc-rewardbook-archive.timer"}, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "tz28_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "wall_ns": 1794933020661142457}
[2026-11-17T16:46:30Z] R {"assets_n": 5, "bytes_total": 71537680, "closed": 5, "deferred": 0, "event": "set", "first_S": 1794927600, "last_S": 1794931200, "open": 2, "run": 1794933020, "sha256": "a3e8f70b8b44d873e420ef9f2a8f83f019b168fbe9f114e2424dbadce279ebd3", "slots_considered": 5, "streamless": 1934, "tag": "rewardbook-streams-1794933020", "unclosed": 0, "wall_ns": 1794933020840827849}
[2026-11-17T16:46:30Z] R {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 448903582, "run": 1794933020, "sent": 5, "wall_ns": 1794933030746952886}
[2026-11-17T16:46:30Z] R {"assets_n": 5, "bytes_total": 71537680, "event": "verify", "release_id": 448903582, "run": 1794933020, "verify_sha256": "0e8556fe68e05eb4f85569d8879f818f503be4c3990919afb9c17e2b2dd20dd5", "wall_ns": 1794933166522886046}
[2026-11-17T16:46:30Z] R {"already": 0, "event": "delete", "free_after": 10637975552, "free_before": 10566414336, "freed": 71537680, "gone": 5, "quiet_s": 0, "removed": 5, "run": 1794933020, "slots_kept": 5, "wall_ns": 1794933166737779085}
[2026-11-17T16:46:30Z] R {"assets_n": 5, "bytes_total": 71537680, "ended_outside": 0, "event": "complete", "free_bytes": 10637971456, "held_s": 0, "peak_rss": 39821312, "rate_per_day": 1373523456, "removals": 5, "requests": 15, "rewardbook_at_end": {"ActiveState": "active", "MainPID": "1556307", "NRestarts": "0"}, "rewardbook_at_start": {"ActiveState": "active", "MainPID": "1556307", "NRestarts": "0"}, "run": 1794933020, "started_outside": 0, "stops": [["the cap", 1795183699], ["the floor, base 43500000 bytes a day", 1795136691], ["the floor, base 187760570 bytes a day", 1795117886]], "store_stream_bytes": 17204028, "wall_ns": 1794933166747222228}
[2026-11-17T16:46:30Z] NOT YET: run 1794933020 complete; G-NEXT's last slot 1794933900 is due at 2026-11-17T17:00:40Z
[2026-11-17T16:46:30Z] peak memory of this run: 26599424 bytes
[2026-11-17T16:46:30Z] opens refused: 0; reward book opens: 0; API requests 0, downloads 0, 0 bytes; files removed 0
exit=3
Tue Nov 17 04:51:30 PM UTC 2026
[2026-11-17T16:51:30Z] R {"commit": "6a615257277d3c94dafd4d39783499560a344648", "event": "start", "file_sha256": "1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72", "invocation": "f3aea761826943c6917151346afe0a37", "phase_at": 20, "resumed": false, "rewardbook": {"ActiveState": "active", "MainPID": "1556307", "NRestarts": "0"}, "run": 1794933020, "trigger": {"monotonic_usec": "9277548091323", "realtime_usec": "1794933020369808", "unit": "btc-rewardbook-archive.timer"}, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "tz28_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "wall_ns": 1794933020661142457}
[2026-11-17T16:51:30Z] R {"assets_n": 5, "bytes_total": 71537680, "closed": 5, "deferred": 0, "event": "set", "first_S": 1794927600, "last_S": 1794931200, "open": 2, "run": 1794933020, "sha256": "a3e8f70b8b44d873e420ef9f2a8f83f019b168fbe9f114e2424dbadce279ebd3", "slots_considered": 5, "streamless": 1934, "tag": "rewardbook-streams-1794933020", "unclosed": 0, "wall_ns": 1794933020840827849}
[2026-11-17T16:51:30Z] R {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 448903582, "run": 1794933020, "sent": 5, "wall_ns": 1794933030746952886}
[2026-11-17T16:51:30Z] R {"assets_n": 5, "bytes_total": 71537680, "event": "verify", "release_id": 448903582, "run": 1794933020, "verify_sha256": "0e8556fe68e05eb4f85569d8879f818f503be4c3990919afb9c17e2b2dd20dd5", "wall_ns": 1794933166522886046}
[2026-11-17T16:51:30Z] R {"already": 0, "event": "delete", "free_after": 10637975552, "free_before": 10566414336, "freed": 71537680, "gone": 5, "quiet_s": 0, "removed": 5, "run": 1794933020, "slots_kept": 5, "wall_ns": 1794933166737779085}
[2026-11-17T16:51:30Z] R {"assets_n": 5, "bytes_total": 71537680, "ended_outside": 0, "event": "complete", "free_bytes": 10637971456, "held_s": 0, "peak_rss": 39821312, "rate_per_day": 1373523456, "removals": 5, "requests": 15, "rewardbook_at_end": {"ActiveState": "active", "MainPID": "1556307", "NRestarts": "0"}, "rewardbook_at_start": {"ActiveState": "active", "MainPID": "1556307", "NRestarts": "0"}, "run": 1794933020, "started_outside": 0, "stops": [["the cap", 1795183699], ["the floor, base 43500000 bytes a day", 1795136691], ["the floor, base 187760570 bytes a day", 1795117886]], "store_stream_bytes": 17204028, "wall_ns": 1794933166747222228}
[2026-11-17T16:51:30Z] NOT YET: run 1794933020 complete; G-NEXT's last slot 1794933900 is due at 2026-11-17T17:00:40Z
[2026-11-17T16:51:30Z] peak memory of this run: 26341376 bytes
[2026-11-17T16:51:30Z] opens refused: 0; reward book opens: 0; API requests 0, downloads 0, 0 bytes; files removed 0
exit=3
Tue Nov 17 04:56:30 PM UTC 2026
[2026-11-17T16:56:30Z] R {"commit": "6a615257277d3c94dafd4d39783499560a344648", "event": "start", "file_sha256": "1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72", "invocation": "f3aea761826943c6917151346afe0a37", "phase_at": 20, "resumed": false, "rewardbook": {"ActiveState": "active", "MainPID": "1556307", "NRestarts": "0"}, "run": 1794933020, "trigger": {"monotonic_usec": "9277548091323", "realtime_usec": "1794933020369808", "unit": "btc-rewardbook-archive.timer"}, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "tz28_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "wall_ns": 1794933020661142457}
[2026-11-17T16:56:30Z] R {"assets_n": 5, "bytes_total": 71537680, "closed": 5, "deferred": 0, "event": "set", "first_S": 1794927600, "last_S": 1794931200, "open": 2, "run": 1794933020, "sha256": "a3e8f70b8b44d873e420ef9f2a8f83f019b168fbe9f114e2424dbadce279ebd3", "slots_considered": 5, "streamless": 1934, "tag": "rewardbook-streams-1794933020", "unclosed": 0, "wall_ns": 1794933020840827849}
[2026-11-17T16:56:30Z] R {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 448903582, "run": 1794933020, "sent": 5, "wall_ns": 1794933030746952886}
[2026-11-17T16:56:30Z] R {"assets_n": 5, "bytes_total": 71537680, "event": "verify", "release_id": 448903582, "run": 1794933020, "verify_sha256": "0e8556fe68e05eb4f85569d8879f818f503be4c3990919afb9c17e2b2dd20dd5", "wall_ns": 1794933166522886046}
[2026-11-17T16:56:30Z] R {"already": 0, "event": "delete", "free_after": 10637975552, "free_before": 10566414336, "freed": 71537680, "gone": 5, "quiet_s": 0, "removed": 5, "run": 1794933020, "slots_kept": 5, "wall_ns": 1794933166737779085}
[2026-11-17T16:56:30Z] R {"assets_n": 5, "bytes_total": 71537680, "ended_outside": 0, "event": "complete", "free_bytes": 10637971456, "held_s": 0, "peak_rss": 39821312, "rate_per_day": 1373523456, "removals": 5, "requests": 15, "rewardbook_at_end": {"ActiveState": "active", "MainPID": "1556307", "NRestarts": "0"}, "rewardbook_at_start": {"ActiveState": "active", "MainPID": "1556307", "NRestarts": "0"}, "run": 1794933020, "started_outside": 0, "stops": [["the cap", 1795183699], ["the floor, base 43500000 bytes a day", 1795136691], ["the floor, base 187760570 bytes a day", 1795117886]], "store_stream_bytes": 17204028, "wall_ns": 1794933166747222228}
[2026-11-17T16:56:30Z] NOT YET: run 1794933020 complete; G-NEXT's last slot 1794933900 is due at 2026-11-17T17:00:40Z
[2026-11-17T16:56:30Z] peak memory of this run: 26337280 bytes
[2026-11-17T16:56:30Z] opens refused: 0; reward book opens: 0; API requests 0, downloads 0, 0 bytes; files removed 0
exit=3
Tue Nov 17 05:01:30 PM UTC 2026
[2026-11-17T17:01:30Z] R {"commit": "6a615257277d3c94dafd4d39783499560a344648", "event": "start", "file_sha256": "1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72", "invocation": "f3aea761826943c6917151346afe0a37", "phase_at": 20, "resumed": false, "rewardbook": {"ActiveState": "active", "MainPID": "1556307", "NRestarts": "0"}, "run": 1794933020, "trigger": {"monotonic_usec": "9277548091323", "realtime_usec": "1794933020369808", "unit": "btc-rewardbook-archive.timer"}, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "tz28_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "wall_ns": 1794933020661142457}
[2026-11-17T17:01:30Z] R {"assets_n": 5, "bytes_total": 71537680, "closed": 5, "deferred": 0, "event": "set", "first_S": 1794927600, "last_S": 1794931200, "open": 2, "run": 1794933020, "sha256": "a3e8f70b8b44d873e420ef9f2a8f83f019b168fbe9f114e2424dbadce279ebd3", "slots_considered": 5, "streamless": 1934, "tag": "rewardbook-streams-1794933020", "unclosed": 0, "wall_ns": 1794933020840827849}
[2026-11-17T17:01:30Z] R {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 448903582, "run": 1794933020, "sent": 5, "wall_ns": 1794933030746952886}
[2026-11-17T17:01:30Z] R {"assets_n": 5, "bytes_total": 71537680, "event": "verify", "release_id": 448903582, "run": 1794933020, "verify_sha256": "0e8556fe68e05eb4f85569d8879f818f503be4c3990919afb9c17e2b2dd20dd5", "wall_ns": 1794933166522886046}
[2026-11-17T17:01:30Z] R {"already": 0, "event": "delete", "free_after": 10637975552, "free_before": 10566414336, "freed": 71537680, "gone": 5, "quiet_s": 0, "removed": 5, "run": 1794933020, "slots_kept": 5, "wall_ns": 1794933166737779085}
[2026-11-17T17:01:30Z] R {"assets_n": 5, "bytes_total": 71537680, "ended_outside": 0, "event": "complete", "free_bytes": 10637971456, "held_s": 0, "peak_rss": 39821312, "rate_per_day": 1373523456, "removals": 5, "requests": 15, "rewardbook_at_end": {"ActiveState": "active", "MainPID": "1556307", "NRestarts": "0"}, "rewardbook_at_start": {"ActiveState": "active", "MainPID": "1556307", "NRestarts": "0"}, "run": 1794933020, "started_outside": 0, "stops": [["the cap", 1795183699], ["the floor, base 43500000 bytes a day", 1795136691], ["the floor, base 187760570 bytes a day", 1795117886]], "store_stream_bytes": 17204028, "wall_ns": 1794933166747222228}
[2026-11-17T17:01:30Z] G-TRIGGER, by TRIGGER_UNIT btc-rewardbook-archive.timer: the elapse 2026-11-17T16:30:20Z, the trigger 2026-11-17T16:30:20Z, the run's start record 2026-11-17T16:30:20Z, a new set
[2026-11-17T17:01:30Z] G-RUN: run 1794933020 complete, 0 deferrals; the service Result success, ExecMainStatus 0, Tue 2026-11-17 16:30:20 UTC to Tue 2026-11-17 16:32:46 UTC; 15 requests and 5 removals, 0 started and 0 ended outside the idle stretch; 5 files, 71537680 bytes
[2026-11-17T17:01:31Z] G-TAG: rewardbook-streams-1794933020 at 6a615257277d3c94dafd4d39783499560a344648, peeled None; the archive's commit 6a615257277d3c94dafd4d39783499560a344648
[2026-11-17T17:01:31Z] G-NEXT slot 1794933900 2026-11-17T16:45:00Z, decided at 2026-11-17T16:44:54Z: PASS - index 0 streamed by 1556307
[2026-11-17T17:01:31Z] READING G-NEXT: PASS over 1 slots, the reward book's process at the run's start 1556307
[2026-11-17T17:01:31Z] READING G-TRIGGER  PASS
[2026-11-17T17:01:31Z] READING G-RUN      PASS
[2026-11-17T17:01:31Z] READING G-TAG      PASS
[2026-11-17T17:01:31Z] READING G-NEXT     PASS
[2026-11-17T17:01:31Z] FIRST PASS: 4 of 4
[2026-11-17T17:01:31Z] peak memory of this run: 26603520 bytes
[2026-11-17T17:01:31Z] opens refused: 0; reward book opens: 2; API requests 0, downloads 0, 0 bytes; files removed 0
exit=0
```
### 2.7 Both archives' runs since §3.3, beside the reloads they followed

| run | start | archive | trigger | files / bytes | the reload it followed |
|---|---|---|---|---|---|
| `1794925184` | 14:19:44Z | pair book | by hand, B-PAIR-OFF | 46 / 1,151,737,742 | — |
| `1794928547` | 15:15:47Z | reward book | **off its calendar**: TZ-34's `OnActiveSec=1800`, 1,800 s after B-PAIR-OFF's reload at 14:45:46–47Z, as §3 predicted; tag `rewardbook-streams-1794928547` | 53 / 652,685,158; free 9,986,568,192 → 10,639,491,072 | `disable --now` ×2, 14:45:45 and 14:45:46Z |
| `1794933020` | 16:30:20Z | reward book | the new calendar's first elapse | 5 / 71,537,680 | B-TIMER's `daemon-reload` at 16:05:49Z set nothing off |

The off-calendar run ended at 15:21:45Z, 44 minutes before B-TIMER's band opened. It did not hold the band closed.

### 2.8 G-STILL's two reads, and the units' memory
```
Tue Nov 17 02:17:35 PM UTC 2026
[2026-11-17T14:17:35Z] adv3-bot.service {'MainPID': '1555970', 'NRestarts': '0', 'ActiveState': 'active'}, UnitFileState enabled, MemoryCurrent 5902336, MemoryPeak 48467968
[2026-11-17T14:17:35Z] btc-pairbook.service {'MainPID': '2012336', 'NRestarts': '6', 'ActiveState': 'active'}, UnitFileState enabled, MemoryCurrent 2269184, MemoryPeak 64192512
[2026-11-17T14:17:35Z] btc-recorder.service {'MainPID': '1555954', 'NRestarts': '0', 'ActiveState': 'active'}, UnitFileState enabled, MemoryCurrent 12218368, MemoryPeak 390193152
[2026-11-17T14:17:35Z] btc-rewardbook.service {'MainPID': '1556307', 'NRestarts': '0', 'ActiveState': 'active'}, UnitFileState enabled, MemoryCurrent 14381056, MemoryPeak 45936640
[2026-11-17T14:17:35Z] btc-rewardbook-archive.timer {'NextElapseUSecRealtime': 'Wed 2026-11-18 01:30:20 UTC', 'LastTriggerUSec': 'Tue 2026-11-17 01:30:20 UTC', 'Result': 'success', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-11-17T14:17:35Z] btc-rewardbook-archive.service {'Result': 'success', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-11-17T14:17:35Z] btc-pairbook-archive.timer {'NextElapseUSecRealtime': 'Wed 2026-11-18 03:00:20 UTC', 'LastTriggerUSec': 'Tue 2026-11-17 03:00:20 UTC', 'Result': 'success', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-11-17T14:17:35Z] btc-pairbook-archive.service {'Result': 'success', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-11-17T14:17:35Z] still: recorded
[2026-11-17T14:17:35Z] peak memory of this run: 26337280 bytes
[2026-11-17T14:17:35Z] opens refused: 0; reward book opens: 0; API requests 0, downloads 0, 0 bytes; files removed 0
exit=0
```
```
Tue Nov 17 05:01:55 PM UTC 2026
[2026-11-17T17:01:55Z] adv3-bot.service {'MainPID': '1555970', 'NRestarts': '0', 'ActiveState': 'active'}, UnitFileState enabled, MemoryCurrent 5726208, MemoryPeak 48467968
[2026-11-17T17:01:55Z] btc-pairbook.service {'MainPID': '0', 'NRestarts': '0', 'ActiveState': 'inactive'}, UnitFileState disabled, MemoryCurrent [not set], MemoryPeak [not set]
[2026-11-17T17:01:55Z] btc-recorder.service {'MainPID': '1555954', 'NRestarts': '0', 'ActiveState': 'active'}, UnitFileState enabled, MemoryCurrent 70356992, MemoryPeak 390193152
[2026-11-17T17:01:55Z] btc-rewardbook.service {'MainPID': '1556307', 'NRestarts': '0', 'ActiveState': 'active'}, UnitFileState enabled, MemoryCurrent 24051712, MemoryPeak 45936640
[2026-11-17T17:01:55Z] btc-rewardbook-archive.timer {'NextElapseUSecRealtime': 'Tue 2026-11-17 19:30:20 UTC', 'LastTriggerUSec': 'Tue 2026-11-17 16:30:20 UTC', 'Result': 'success', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-11-17T17:01:55Z] btc-rewardbook-archive.service {'Result': 'success', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-11-17T17:01:55Z] btc-pairbook-archive.timer {'NextElapseUSecRealtime': '', 'LastTriggerUSec': '', 'Result': 'success', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'disabled'}
[2026-11-17T17:01:55Z] btc-pairbook-archive.service {'Result': 'success', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-11-17T17:01:55Z] the pair book archive's restart record 2026-11-17T14:33:18Z: run 1794925184, pid 2080877 after 2012336, NRestarts 7
[2026-11-17T17:01:55Z] the reward book archive's runs with records since the first read: [1794928547, 1794933020]
[2026-11-17T17:01:55Z] G-STILL PASS: the pair book stopped by B-PAIR-OFF after 1 restart records of its archive since 2026-11-17T14:17:35Z
[2026-11-17T17:01:55Z] peak memory of this run: 27127808 bytes
[2026-11-17T17:01:55Z] opens refused: 0; reward book opens: 0; API requests 0, downloads 0, 0 bytes; files removed 0
exit=0
```
### 2.9 The directories beside this session — B-RECLAIM-SCRATCH
```
Tue Nov 17 02:17:35 PM UTC 2026
[2026-11-17T14:17:35Z] running 1738600 started 2026-11-15T10:28:51Z claude
[2026-11-17T14:17:35Z] running 1738611 started 2026-11-15T10:28:53Z claude
[2026-11-17T14:17:35Z] running 1738619 started 2026-11-15T10:28:53Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-17T14:17:35Z] running 1738645 started 2026-11-15T10:28:55Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-17T14:17:35Z] 892ec9bf-0691-50df-8231-a07862dcb100 born 2026-11-16T07:46:53Z: earlier
[2026-11-17T14:17:35Z] 95cf58d2-1ec6-4c73-a622-38d04665f5ae born 2026-11-15T10:28:56Z: live, process [1738600, 1738611, 1738619, 1738645]
[2026-11-17T14:17:35Z] b93843c6-34fe-4b95-8041-0ae0aad4b8ab born 2026-11-16T07:46:52Z: earlier
[2026-11-17T14:17:35Z] peak memory of this run: 26337280 bytes
[2026-11-17T14:17:35Z] opens refused: 0; reward book opens: 0; API requests 0, downloads 0, 0 bytes; files removed 0
exit=0
```
```
2026-11-17T14:17:47.550017817Z
[2026-11-17T14:17:47Z] reclaim: 3989 report tokens; the forensic store holds 2579 files
[2026-11-17T14:17:47Z] RECLAIM PASS: 14 files considered, 0 named by a report, 0 kept by name, 0 copied, 0 already held; the forensic store 2579 -> 2579 files
[2026-11-17T14:17:47Z] peak memory of this run: 30486528 bytes
[2026-11-17T14:17:47Z] opens refused: 0; reward book opens: 0; API requests 0, downloads 0, 0 bytes; files removed 0
exit=0
2026-11-17T14:17:47.824320833Z
exit=0
exit=1
exit=0
exit=1
```
### 2.10 Every free-space and `MemAvailable` read

| instant (UTC) | where | free bytes | bound | MemAvailable | floor 133,073,162 |
|---|---|---|---|---|---|
| 14:14:56 | §0.0 in the session | 8,731,217,920 | 7,600,000,000 | — | — |
| 14:15:41 | §0.0, `00-ready.log` | 8,730,017,792 | 7,600,000,000 | — | — |
| 14:16:04 / 14:16:24 | §0.3 host gate | 8,729,411,584 | 7,600,000,000 | 562,360,320 | PASS |
| 14:17:27 | `selftest` (5 reads) | 8,711,196,672 to 8,711,229,440 | 2,300,000,000 | 328,486,912 to 328,634,368 | above |
| 14:17:52 | `room before` | 8,710,725,632 | 2,300,000,000 | 294,379,520 | above |
| 14:18:00 | `forensics` | 8,710,569,984 | 2,300,000,000 | 315,105,280 | above |
| 14:19:16 | `forensics-remove` | 8,709,038,080 → 8,938,147,840 | 2,300,000,000 | 323,493,888 | above |
| 17:02:01 | `room after` | 10,607,034,368 | 2,300,000,000 | 292,356,096 | above |
| 17:02:19 / 17:02:42 | §3.10 host gate again | 10,606,698,496 | recorded | 304,521,216 | recorded |
| 17:03 | `92-closing.log` | 10,605,719,552 | recorded | 450,113,536 (`free -b` available) | recorded |

### 2.11 The closing reads
```
Tue Nov 17 05:03:03 PM UTC 2026
total 84
drwxr-xr-x  5 root root  4096 Nov 17 17:02 .
drwx------ 31 root root  4096 Nov 17 14:15 ..
-rw-r--r--  1 root root 29538 Nov 17 14:19 forensics-plan.json
-rw-r--r--  1 root root 18982 Nov 17 14:19 forensics-removed.jsonl
drwxr-xr-x  2 root root  4096 Nov 17 17:03 logs
-rw-r--r--  1 root root   544 Nov 17 17:02 room-after.json
-rw-r--r--  1 root root  1737 Nov 17 14:17 room-before.json
drwxr-xr-x  4 root root  4096 Nov 17 14:15 stage
-rw-r--r--  1 root root  3368 Nov 17 16:05 state.json
drwxr-xr-x  7 root root  4096 Nov 17 14:16 wt
7a32ec020d0b124612a0812403241c6eebcacf667aa21473a6693b77ad1898ad  state.json
1e8c05d977bcb3c5817c56157df53057e6e2974d7fabceaa9226c3d8ab429bbd  room-before.json
bea263a47c88413fa7315a38938a705e7873de52f6f3b9ee0696fdff98029deb  room-after.json
becd4c5c35bd6484a659bd1c211d9a515401d73db13a1cab03aa43a6ee6f414f  forensics-plan.json
f95519f5b0b95474e979de30142914c32fc666f56146ed41146e35a8ae2de2a6  forensics-removed.jsonl
47 forensics-removed.jsonl
{
 "forensics": {
  "at": "2026-11-17T14:19:02Z",
  "plan_sha256": "becd4c5c35bd6484a659bd1c211d9a515401d73db13a1cab03aa43a6ee6f414f",
  "planned_n": 47
 },
 "marks": {
  "pairoff": {
   "archives": {
    "btc-pairbook-archive.service": {
     "ActiveState": "inactive",
     "Result": "success",
     "SubState": "dead",
     "UnitFileState": "static"
    },
    "btc-pairbook-archive.timer": {
     "ActiveState": "active",
     "LastTriggerUSec": "Tue 2026-11-17 03:00:20 UTC",
     "NextElapseUSecRealtime": "Wed 2026-11-18 03:00:20 UTC",
     "Result": "success",
     "SubState": "waiting",
     "UnitFileState": "enabled"
    },
    "btc-rewardbook-archive.service": {
     "ActiveState": "inactive",
     "Result": "success",
     "SubState": "dead",
     "UnitFileState": "static"
    },
    "btc-rewardbook-archive.timer": {
     "ActiveState": "active",
     "LastTriggerUSec": "Tue 2026-11-17 01:30:20 UTC",
     "NextElapseUSecRealtime": "Wed 2026-11-18 01:30:20 UTC",
     "Result": "success",
     "SubState": "waiting",
     "UnitFileState": "enabled"
    }
   },
   "ns": 1794925184463970426,
   "units": {
    "advisor": {
     "ActiveState": "active",
     "MainPID": "1555970",
     "NRestarts": "0"
    },
    "pairbook": {
     "ActiveState": "active",
     "MainPID": "2012336",
     "NRestarts": "6"
    },
    "recorder": {
     "ActiveState": "active",
     "MainPID": "1555954",
     "NRestarts": "0"
    },
    "rewardbook": {
     "ActiveState": "active",
     "MainPID": "1556307",
     "NRestarts": "0"
    }
   }
  },
  "timer": {
   "archives": {
    "btc-pairbook-archive.service": {
     "ActiveState": "inactive",
     "Result": "success",
     "SubState": "dead",
     "UnitFileState": "static"
    },
    "btc-pairbook-archive.timer": {
     "ActiveState": "inactive",
     "LastTriggerUSec": "",
     "NextElapseUSecRealtime": "",
     "Result": "success",
     "SubState": "dead",
     "UnitFileState": "disabled"
    },
    "btc-rewardbook-archive.service": {
     "ActiveState": "inactive",
     "Result": "success",
     "SubState": "dead",
     "UnitFileState": "static"
    },
    "btc-rewardbook-archive.timer": {
     "ActiveState": "active",
     "LastTriggerUSec": "Tue 2026-11-17 15:15:47 UTC",
     "NextElapseUSecRealtime": "Wed 2026-11-18 01:30:20 UTC",
     "Result": "success",
     "SubState": "waiting",
     "UnitFileState": "enabled"
    }
   },
   "ns": 1794931549233302658,
   "units": {
    "advisor": {
     "ActiveState": "active",
     "MainPID": "1555970",
     "NRestarts": "0"
    },
    "pairbook": {
     "ActiveState": "inactive",
     "MainPID": "0",
     "NRestarts": "0"
    },
    "recorder": {
     "ActiveState": "active",
     "MainPID": "1555954",
     "NRestarts": "0"
    },
    "rewardbook": {
     "ActiveState": "active",
     "MainPID": "1556307",
     "NRestarts": "0"
    }
   }
  }
 },
 "still": {
  "at": "2026-11-17T14:17:35Z",
  "at_ns": 1794925055807253439,
  "units": {
   "advisor": {
    "ActiveState": "active",
    "MainPID": "1555970",
    "NRestarts": "0"
   },
   "pairbook": {
    "ActiveState": "active",
    "MainPID": "2012336",
    "NRestarts": "6"
   },
   "recorder": {
    "ActiveState": "active",
    "MainPID": "1555954",
    "NRestarts": "0"
   },
   "rewardbook": {
    "ActiveState": "active",
    "MainPID": "1556307",
    "NRestarts": "0"
   }
  }
 }
}
MainPID=1555954
Result=success
NRestarts=0
MemoryCurrent=9818112
MemoryPeak=390193152
Id=btc-recorder.service
ActiveState=active
SubState=running
UnitFileState=enabled

MainPID=0
Result=success
NRestarts=0
MemoryCurrent=[not set]
MemoryPeak=[not set]
Id=btc-pairbook.service
ActiveState=inactive
SubState=dead
UnitFileState=disabled

MainPID=1556307
Result=success
NRestarts=0
MemoryCurrent=13549568
MemoryPeak=45936640
Id=btc-rewardbook.service
ActiveState=active
SubState=running
UnitFileState=enabled

MainPID=1555970
Result=success
NRestarts=0
MemoryCurrent=6443008
MemoryPeak=48467968
Id=adv3-bot.service
ActiveState=active
SubState=running
UnitFileState=enabled

MainPID=0
Result=success
NRestarts=0
MemoryCurrent=[not set]
MemoryPeak=[not set]
Id=btc-pairbook-archive.service
ActiveState=inactive
SubState=dead
UnitFileState=static

Result=success
Id=btc-pairbook-archive.timer
ActiveState=inactive
SubState=dead
UnitFileState=disabled

MainPID=0
Result=success
NRestarts=0
MemoryCurrent=[not set]
MemoryPeak=61399040
Id=btc-rewardbook-archive.service
ActiveState=inactive
SubState=dead
UnitFileState=static

Result=success
Id=btc-rewardbook-archive.timer
ActiveState=active
SubState=waiting
UnitFileState=enabled
NEXT                            LEFT LAST                           PASSED UNIT                         ACTIVATES
Tue 2026-11-17 19:30:20 UTC 2h 27min Tue 2026-11-17 16:30:20 UTC 32min ago btc-rewardbook-archive.timer btc-rewardbook-archive.service

1 timers listed.
cmp exit=0
2026-11-17T14:19:44+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
2026-11-17T14:32:48+00:00 vultr systemd[1]: btc-pairbook.service: Sent signal SIGTERM to main process 2012336 (python) on client request.
2026-11-17T14:32:48+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-11-17T14:32:48+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 22min 59.529s CPU time, 61.2M memory peak, 39.4M memory swap peak.
2026-11-17T14:32:53+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 7.
2026-11-17T14:32:53+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-11-17T14:45:42+00:00 vultr systemd[1]: btc-pairbook-archive.service: Deactivated successfully.
2026-11-17T14:45:42+00:00 vultr systemd[1]: Finished btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release.
2026-11-17T14:45:42+00:00 vultr systemd[1]: btc-pairbook-archive.service: Consumed 18.321s CPU time, 86.8M memory peak, 25.3M memory swap peak.
2026-11-17T14:45:46+00:00 vultr systemd[1]: btc-pairbook-archive.timer: Deactivated successfully.
2026-11-17T14:45:46+00:00 vultr systemd[1]: Stopped btc-pairbook-archive.timer - btc-5m-twap pair book archive, once a day.
2026-11-17T14:45:46+00:00 vultr systemd[1]: Stopping btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed...
2026-11-17T14:45:47+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-11-17T14:45:47+00:00 vultr systemd[1]: Stopped btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-11-17T14:45:47+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 28.557s CPU time, 58.3M memory peak, 20.2M memory swap peak.
2026-11-17T15:15:47+00:00 vultr systemd[1]: Starting btc-rewardbook-archive.service - btc-5m-twap reward book archive, the stream files of closed slots to a Release...
2026-11-17T15:21:45+00:00 vultr systemd[1]: btc-rewardbook-archive.service: Deactivated successfully.
2026-11-17T15:21:45+00:00 vultr systemd[1]: Finished btc-rewardbook-archive.service - btc-5m-twap reward book archive, the stream files of closed slots to a Release.
2026-11-17T15:21:45+00:00 vultr systemd[1]: btc-rewardbook-archive.service: Consumed 11.585s CPU time, 50.9M memory peak, 7.1M memory swap peak.
2026-11-17T16:05:49+00:00 vultr systemd[1]: btc-rewardbook-archive.timer: Deactivated successfully.
2026-11-17T16:05:49+00:00 vultr systemd[1]: Stopped btc-rewardbook-archive.timer - btc-5m-twap reward book archive, every three hours.
2026-11-17T16:05:49+00:00 vultr systemd[1]: Stopping btc-rewardbook-archive.timer - btc-5m-twap reward book archive, every three hours...
2026-11-17T16:05:49+00:00 vultr systemd[1]: Started btc-rewardbook-archive.timer - btc-5m-twap reward book archive, every three hours.
2026-11-17T16:30:20+00:00 vultr systemd[1]: Starting btc-rewardbook-archive.service - btc-5m-twap reward book archive, the stream files of closed slots to a Release...
2026-11-17T16:32:46+00:00 vultr systemd[1]: btc-rewardbook-archive.service: Deactivated successfully.
2026-11-17T16:32:46+00:00 vultr systemd[1]: Finished btc-rewardbook-archive.service - btc-5m-twap reward book archive, the stream files of closed slots to a Release.
2026-11-17T16:32:46+00:00 vultr systemd[1]: btc-rewardbook-archive.service: Consumed 1.419s CPU time, 58.5M memory peak, 0B memory swap peak.
-- No entries --
[2026-11-17T15:21:43Z] L {"assets_n": 53, "bytes_total": 652685158, "event": "verify", "release_id": 448806639, "run": 1794928547, "verify_sha256": "42d4929f60e5af78461f4fee1b60f5594213bccd6c32d68d01bd3404808536cb", "wall_ns": 1794928903187753548}
[2026-11-17T15:21:43Z] X 1794873600-1794879900.0.stream.jsonl.gz 15692888 28db739266c69128f2e7670f62e3aa14724b5445ae218fe5b52c974965317b8b removed at second 403
[2026-11-17T15:21:43Z] X 1794873600-1794880800.0.stream.jsonl.gz 14150934 9fc72ab8889ed67b49ea27a51c6376dbf4e09ea4c9f1a24af010a9b18a9b006a removed at second 403
[2026-11-17T15:21:43Z] X 1794873600-1794881700.0.stream.jsonl.gz 11750717 bcd633c3bacd971995d085acd8e0d0eae8ca426d309f3cc3e78f03e9ecc20c17 removed at second 403
[2026-11-17T15:21:43Z] X 1794873600-1794882600.0.stream.jsonl.gz 10353947 9290d998b13eaefb808948ea5ea7313b18a7c3a8904df66498b39310e8917cc3 removed at second 403
[2026-11-17T15:21:43Z] X 1794873600-1794883500.0.stream.jsonl.gz 8130492 b17db58ec21dec04cd156c1d752bb62883d869116c29eabd69782d0ab675edc1 removed at second 403
[2026-11-17T15:21:43Z] X 1794873600-1794884400.0.stream.jsonl.gz 10534362 a73feba7b92a7ae998993ded7c61812be242f350b0971cd735f5ccb5e9ae82d9 removed at second 403
[2026-11-17T15:21:43Z] X 1794873600-1794885300.0.stream.jsonl.gz 10079252 b347de79b0d08c994efd4429a37c3b74de25c08bd6695f970301fb1adefbe9d6 removed at second 403
[2026-11-17T15:21:43Z] X 1794873600-1794886200.0.stream.jsonl.gz 9808747 258ffc5825e5c383810fc753274a1c320e5950b7215c89009f7f7d2ff2aebd5f removed at second 403
[2026-11-17T15:21:43Z] X 1794873600-1794887100.0.stream.jsonl.gz 9021246 26db49f20c30ac92de5bd11d621bc8d9e0abba489782d2e00fe0260d507cf8aa removed at second 403
[2026-11-17T15:21:43Z] X 1794873600-1794888000.0.stream.jsonl.gz 10315144 bf3a1409ea1b08596311b15ddbffb540e829a6d17e78772273413f74217887aa removed at second 403
[2026-11-17T15:21:43Z] X 1794873600-1794888900.0.stream.jsonl.gz 9323623 93cfdc67abee8225e5ae4eb6251e6e83665c007913cb4fcd59b316322861501f removed at second 403
[2026-11-17T15:21:43Z] X 1794873600-1794889800.0.stream.jsonl.gz 9444952 70a7965a2d879fea31cab0d9173433c35cda41412d5cd4535b025ee4f358bd95 removed at second 403
[2026-11-17T15:21:43Z] X 1794873600-1794890700.0.stream.jsonl.gz 10630912 8e7a44edef314e3e6bb5797eff9a0293d2cba8544327d215ae0e1c26f79d2701 removed at second 403
[2026-11-17T15:21:43Z] X 1794873600-1794891600.0.stream.jsonl.gz 9610232 0d085af7a9145a10d870c692ae940eef094054ed1a4584cf0ba09dd373d6da91 removed at second 403
[2026-11-17T15:21:43Z] X 1794873600-1794892500.0.stream.jsonl.gz 9841833 c45a89a81c955a5b3ec3b292a489ffde22c6b67f3ef814fe937a99918c90cfc3 removed at second 403
[2026-11-17T15:21:43Z] X 1794873600-1794893400.0.stream.jsonl.gz 12763006 85abddd1c661a1228b6e53ed114d7678a7be8b8858876a68c8f9c5ac5a7aba14 removed at second 403
[2026-11-17T15:21:43Z] X 1794873600-1794894300.0.stream.jsonl.gz 10446314 7ee48b1110bf2435fd3741e69bf3dcc728ea81731d254fb355b17f22455138a3 removed at second 403
[2026-11-17T15:21:43Z] X 1794873600-1794895200.0.stream.jsonl.gz 10322926 e041b2d01a09d44828456b03725a058e064167528dc1e0c8afe5492733529d5c removed at second 403
[2026-11-17T15:21:43Z] X 1794873600-1794896100.0.stream.jsonl.gz 8352713 78e36b2b401c47a26cb751bac7cd1f85e58cb25ebd078c203fddc4950e2e8c8f removed at second 403
[2026-11-17T15:21:43Z] X 1794873600-1794897000.0.stream.jsonl.gz 12851278 c1d08d26b2ed2fd682d6d9814e5cc806d15eb736b116bbcf83a7ef84c058903b removed at second 403
[2026-11-17T15:21:43Z] X 1794873600-1794897900.0.stream.jsonl.gz 10284593 f7cea38ff2fbbad94fa1f6f7d32e9a9a4f5b1ea6f030fe0ff9113b8c81dff357 removed at second 403
[2026-11-17T15:21:44Z] X 1794873600-1794898800.0.stream.jsonl.gz 9719587 6350de40200a342f3a68fbcecea0a3fad29b4bcdf40eb4f2ca262cfcc6421640 removed at second 404
[2026-11-17T15:21:44Z] X 1794873600-1794899700.0.stream.jsonl.gz 8812084 78b9f0909cfe011f01485674d318aa31804b76ceb97034025bfcc569348fde8b removed at second 404
[2026-11-17T15:21:44Z] X 1794873600-1794900600.0.stream.jsonl.gz 9960348 07a4b93c9b13dc3cdbb22e0f4ad59b634eee67d53b98f8f370b0934a2c8746eb removed at second 404
[2026-11-17T15:21:44Z] X 1794873600-1794901500.0.stream.jsonl.gz 9905464 4272bcdcd88cc50af91f9a0782fcb2949821d54b5f25b7c1702e495ffa777145 removed at second 404
[2026-11-17T15:21:44Z] X 1794873600-1794902400.0.stream.jsonl.gz 11652571 bc20ffacbfee9e470a963ec9f134a4a96cc10e857badb04600d21ef3c898f935 removed at second 404
[2026-11-17T15:21:44Z] X 1794873600-1794903300.0.stream.jsonl.gz 12075781 6d265aa99323bb5393a18e312ca224b7627d12124b5f1f7c6127e5654e49aaf5 removed at second 404
[2026-11-17T15:21:44Z] X 1794873600-1794904200.0.stream.jsonl.gz 11569472 d7715b8fec1890e1a4e22ad9bd6749d01dfc3196012a5b85fc521f3ae70f3d01 removed at second 404
[2026-11-17T15:21:44Z] X 1794873600-1794905100.0.stream.jsonl.gz 11343410 e59528f82767ef43584c6004c56a35ed72c6679dfaf8e987ce8b7a2f8a061399 removed at second 404
[2026-11-17T15:21:44Z] X 1794873600-1794906000.0.stream.jsonl.gz 11368620 f9cd297992a88632f0d021382158ae68629b75f7d19fa857412a02064cf33dea removed at second 404
[2026-11-17T15:21:44Z] X 1794873600-1794906900.0.stream.jsonl.gz 10720459 a7cf89b9c378010a70b296e16062e4f259ac2c45b7e73b4b852afe7f55fda243 removed at second 404
[2026-11-17T15:21:44Z] X 1794873600-1794907800.0.stream.jsonl.gz 11966894 8c2c6f2d7b76a0dc76b265ddc83df4bba12631720d03720820be6e2874bc8684 removed at second 404
[2026-11-17T15:21:44Z] X 1794873600-1794908700.0.stream.jsonl.gz 11470359 a5dcc120d6acfef4b396847aa4ba073e21da48a4dc9c9708dbf6fe6c8a05c584 removed at second 404
[2026-11-17T15:21:44Z] X 1794873600-1794909600.0.stream.jsonl.gz 11323377 e94b2255b63460ea1107af4e40896842abfc87a2b8e57532d94c96be857eba67 removed at second 404
[2026-11-17T15:21:44Z] X 1794873600-1794910500.0.stream.jsonl.gz 14328128 90d488ffff5b18244d107fe6d57e536db2d3dc43b7ba7884df7dac3b88855d48 removed at second 404
[2026-11-17T15:21:44Z] X 1794873600-1794911400.0.stream.jsonl.gz 13879735 e5ef04b5670a8e605f493dc15b90ac58cf8d0297814eb2d1f8ed171e63c3f6bc removed at second 404
[2026-11-17T15:21:44Z] X 1794873600-1794912300.0.stream.jsonl.gz 15186643 9395a864a85228d663e40b37024980f7e3586f7aa3783a933f2be82a2c806bf3 removed at second 404
[2026-11-17T15:21:44Z] X 1794873600-1794913200.0.stream.jsonl.gz 16686829 d959c14a7c5d56829355d7c53b82a8a4268fe98393c86c5a2e864ccac9365cfb removed at second 404
[2026-11-17T15:21:44Z] X 1794873600-1794914100.0.stream.jsonl.gz 14609091 8db6ce3b628abacdf7077a6f36ff89f8d87a92fc82221901262edaee646e9a0d removed at second 404
[2026-11-17T15:21:44Z] X 1794873600-1794915000.0.stream.jsonl.gz 13321536 f067ff6afaa4e40a87fcef3dbd8551335f8319777da08eb7d949750c7637f8f1 removed at second 404
[2026-11-17T15:21:44Z] X 1794873600-1794915900.0.stream.jsonl.gz 13672104 5be00d59c05b4ed672812061ea7b0a2b0adee498fe47756699f0bb9937c94e29 removed at second 404
[2026-11-17T15:21:44Z] X 1794873600-1794916800.0.stream.jsonl.gz 15336193 13e0c5902246fbecbb30e9052c70e9c70a95fc05f627b3ec82f7c2ba6e69155e removed at second 404
[2026-11-17T15:21:44Z] X 1794873600-1794917700.0.stream.jsonl.gz 14899640 948416466c102cb777f8c0c2e3d20d300c8ac82e44b5b1616af0ba22711b75d0 removed at second 404
[2026-11-17T15:21:44Z] X 1794873600-1794918600.0.stream.jsonl.gz 17578881 e02f86333b42573a9205726e5052b4613ae58e29bdb7f59dfcb46149e4d634c8 removed at second 404
[2026-11-17T15:21:44Z] X 1794873600-1794919500.0.stream.jsonl.gz 15137957 29d0b0c28bc5070bc6ff611a46d88b466a01d5a0e13c43f8133fbd603028e353 removed at second 404
[2026-11-17T15:21:44Z] X 1794873600-1794920400.0.stream.jsonl.gz 14936094 68e58495f341a09d079fdedb12ac288175f4f4bf3d1ba9258872e0214323a0ad removed at second 404
[2026-11-17T15:21:45Z] X 1794873600-1794921300.0.stream.jsonl.gz 14482834 8b320e004e14a75ffd92f028e027a216baf3b956ffa2130316f8565e99797b67 removed at second 405
[2026-11-17T15:21:45Z] X 1794873600-1794922200.0.stream.jsonl.gz 16974774 dcd862006525ea023e95af41b17d7cfb7058a64113ecdc11ea912c349841afe0 removed at second 405
[2026-11-17T15:21:45Z] X 1794873600-1794923100.0.stream.jsonl.gz 15454418 5c4e2633e24eae20f78448a94ce49e556d156a9ced4872d0f788ee9b9709da1f removed at second 405
[2026-11-17T15:21:45Z] X 1794873600-1794924000.0.stream.jsonl.gz 16191136 7d6a178ffd7bbeacfb318affc6f5102ef996be6489e65d3cbb356d17c91da210 removed at second 405
[2026-11-17T15:21:45Z] X 1794873600-1794924900.0.stream.jsonl.gz 15636458 30f1e722122f073867f4ebae89608ad8d3b15a2d9c43f5488b236e58f4a443d1 removed at second 405
[2026-11-17T15:21:45Z] X 1794873600-1794925800.0.stream.jsonl.gz 14393715 728703462bd97d2e09da73ee34b35d066b637c9f344d37be5451d6447e429c74 removed at second 405
[2026-11-17T15:21:45Z] X 1794873600-1794926700.0.stream.jsonl.gz 14380455 b8aa5bebd723abcde052f831a3673d231bdf1af7b7dc8d0d40c449bdf71464c3 removed at second 405
[2026-11-17T15:21:45Z] G-DELETE every file of the set absent         True
[2026-11-17T15:21:45Z] G-DELETE each removal recorded                True
[2026-11-17T15:21:45Z] G-DELETE each slot keeps its slot.json        True
[2026-11-17T15:21:45Z] L {"already": 0, "event": "delete", "free_after": 10639491072, "free_before": 9986568192, "freed": 652685158, "gone": 53, "quiet_s": 0, "removed": 53, "run": 1794928547, "slots_kept": 53, "wall_ns": 1794928905313319080}
[2026-11-17T15:21:45Z] at the set's rate the cap stops the streams in 3.37 days, at 2026-11-21T00:11:17Z
[2026-11-17T15:21:45Z] at the set's rate the floor, base 43500000 bytes a day stops the streams in 2.72 days, at 2026-11-20T08:45:02Z
[2026-11-17T15:21:45Z] at the set's rate the floor, base 187760570 bytes a day stops the streams in 2.44 days, at 2026-11-20T01:51:54Z
[2026-11-17T15:21:45Z] L {"assets_n": 53, "bytes_total": 652685158, "ended_outside": 0, "event": "complete", "free_bytes": 10639491072, "held_s": 0, "peak_rss": 40087552, "rate_per_day": 1182222172, "removals": 53, "requests": 111, "rewardbook_at_end": {"ActiveState": "active", "MainPID": "1556307", "NRestarts": "0"}, "rewardbook_at_start": {"ActiveState": "active", "MainPID": "1556307", "NRestarts": "0"}, "run": 1794928547, "started_outside": 0, "stops": [["the cap", 1795219877], ["the floor, base 43500000 bytes a day", 1795164302], ["the floor, base 187760570 bytes a day", 1795139514]], "store_stream_bytes": 18589742, "wall_ns": 1794928905336728163}
[2026-11-17T15:21:45Z] COMPLETE: run 1794928547, 53 files, 652685158 bytes, Release rewardbook-streams-1794928547
[2026-11-17T15:21:45Z] peak memory of this run: 40087552 bytes
[2026-11-17T15:21:45Z] opens refused: 0 by TZ-27's hook, 0 by this file's; store opens 160; requests 111, uploads 53, downloads 53 (652685158 bytes); files removed 53
[2026-11-17T16:30:20Z] run: pid 2091982, commit 6a615257277d3c94dafd4d39783499560a344648, file sha256 1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72, invocation f3aea761826943c6917151346afe0a37
[2026-11-17T16:30:20Z] L {"commit": "6a615257277d3c94dafd4d39783499560a344648", "event": "start", "file_sha256": "1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72", "invocation": "f3aea761826943c6917151346afe0a37", "phase_at": 20, "resumed": false, "rewardbook": {"ActiveState": "active", "MainPID": "1556307", "NRestarts": "0"}, "run": 1794933020, "trigger": {"monotonic_usec": "9277548091323", "realtime_usec": "1794933020369808", "unit": "btc-rewardbook-archive.timer"}, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "tz28_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "wall_ns": 1794933020661142457}
[2026-11-17T16:30:20Z] MemAvailable 301453312 bytes, floor 73121792; free 10568540160 bytes, floor 2002000000
[2026-11-17T16:30:20Z] SLOT 1794927600 2026-11-17T15:00:00Z closed   stream files 1, 12835147 bytes, taken 1
[2026-11-17T16:30:20Z] SLOT 1794928500 2026-11-17T15:15:00Z closed   stream files 1, 12895500 bytes, taken 1
[2026-11-17T16:30:20Z] SLOT 1794929400 2026-11-17T15:30:00Z closed   stream files 1, 15269398 bytes, taken 1
[2026-11-17T16:30:20Z] SLOT 1794930300 2026-11-17T15:45:00Z closed   stream files 1, 16378985 bytes, taken 1
[2026-11-17T16:30:20Z] SLOT 1794931200 2026-11-17T16:00:00Z closed   stream files 1, 14158650 bytes, taken 1
[2026-11-17T16:30:20Z] S 1794873600-1794927600.0.stream.jsonl.gz 12835147 4ad412e2b76b1a0818b95d58b8727e2631c9f23e5ca3cdb2839304f9c0e33653
[2026-11-17T16:30:20Z] S 1794873600-1794928500.0.stream.jsonl.gz 12895500 c30dd934591935a9da7a879b40acddc2d7bcbb10332292a39963d1a9bd231d7a
[2026-11-17T16:30:20Z] S 1794873600-1794929400.0.stream.jsonl.gz 15269398 d95a86415e7862d0a57f516abacfd388697a56a57c74657e25e1efb1fdccf64c
[2026-11-17T16:30:20Z] S 1794873600-1794930300.0.stream.jsonl.gz 16378985 a12a82c4d980b9376d045bc0267a1784ed08c40fe7aecc26482b4bd4d4ba69b8
[2026-11-17T16:30:20Z] S 1794873600-1794931200.0.stream.jsonl.gz 14158650 47ca06e1f8fd5ed20c7113a95c06a0f695c01e5b4009d8a6d8dd62a2c6358c4e
[2026-11-17T16:30:20Z] L {"assets_n": 5, "bytes_total": 71537680, "closed": 5, "deferred": 0, "event": "set", "first_S": 1794927600, "last_S": 1794931200, "open": 2, "run": 1794933020, "sha256": "a3e8f70b8b44d873e420ef9f2a8f83f019b168fbe9f114e2424dbadce279ebd3", "slots_considered": 5, "streamless": 1934, "tag": "rewardbook-streams-1794933020", "unclosed": 0, "wall_ns": 1794933020840827849}
[2026-11-17T16:30:20Z] credential: the primary checkout's remote URL
[2026-11-17T16:30:22Z] created the Release on rewardbook-streams-1794933020, id 448903582
[2026-11-17T16:30:24Z] U {"action": "uploaded", "asset": "1794873600-1794927600.0.stream.jsonl.gz", "at": "2026-11-17T16:30:24Z", "bytes": 12835147, "digest": "sha256:4ad412e2b76b1a0818b95d58b8727e2631c9f23e5ca3cdb2839304f9c0e33653", "id": 759792459, "sha256": "4ad412e2b76b1a0818b95d58b8727e2631c9f23e5ca3cdb2839304f9c0e33653"}
[2026-11-17T16:30:25Z] U {"action": "uploaded", "asset": "1794873600-1794928500.0.stream.jsonl.gz", "at": "2026-11-17T16:30:25Z", "bytes": 12895500, "digest": "sha256:c30dd934591935a9da7a879b40acddc2d7bcbb10332292a39963d1a9bd231d7a", "id": 759792544, "sha256": "c30dd934591935a9da7a879b40acddc2d7bcbb10332292a39963d1a9bd231d7a"}
[2026-11-17T16:30:27Z] U {"action": "uploaded", "asset": "1794873600-1794929400.0.stream.jsonl.gz", "at": "2026-11-17T16:30:27Z", "bytes": 15269398, "digest": "sha256:d95a86415e7862d0a57f516abacfd388697a56a57c74657e25e1efb1fdccf64c", "id": 759792659, "sha256": "d95a86415e7862d0a57f516abacfd388697a56a57c74657e25e1efb1fdccf64c"}
[2026-11-17T16:30:29Z] U {"action": "uploaded", "asset": "1794873600-1794930300.0.stream.jsonl.gz", "at": "2026-11-17T16:30:29Z", "bytes": 16378985, "digest": "sha256:a12a82c4d980b9376d045bc0267a1784ed08c40fe7aecc26482b4bd4d4ba69b8", "id": 759792767, "sha256": "a12a82c4d980b9376d045bc0267a1784ed08c40fe7aecc26482b4bd4d4ba69b8"}
[2026-11-17T16:30:30Z] U {"action": "uploaded", "asset": "1794873600-1794931200.0.stream.jsonl.gz", "at": "2026-11-17T16:30:30Z", "bytes": 14158650, "digest": "sha256:47ca06e1f8fd5ed20c7113a95c06a0f695c01e5b4009d8a6d8dd62a2c6358c4e", "id": 759792859, "sha256": "47ca06e1f8fd5ed20c7113a95c06a0f695c01e5b4009d8a6d8dd62a2c6358c4e"}
[2026-11-17T16:30:30Z] U {"action": "complete", "assets": 5, "at": "2026-11-17T16:30:30Z", "credential": "the primary checkout's remote URL", "held": 0, "release_id": 448903582, "sent": 5, "wall_ns": 1794933030746889922}
[2026-11-17T16:30:30Z] L {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 448903582, "run": 1794933020, "sent": 5, "wall_ns": 1794933030746952886}
[2026-11-17T16:32:32Z] D 1794873600-1794927600.0.stream.jsonl.gz equal bytes 12835147 sha256 4ad412e2b76b1a0818b95d58b8727e2631c9f23e5ca3cdb2839304f9c0e33653
[2026-11-17T16:32:33Z] D 1794873600-1794928500.0.stream.jsonl.gz equal bytes 12895500 sha256 c30dd934591935a9da7a879b40acddc2d7bcbb10332292a39963d1a9bd231d7a
[2026-11-17T16:32:34Z] D 1794873600-1794929400.0.stream.jsonl.gz equal bytes 15269398 sha256 d95a86415e7862d0a57f516abacfd388697a56a57c74657e25e1efb1fdccf64c
[2026-11-17T16:32:37Z] D 1794873600-1794930300.0.stream.jsonl.gz equal bytes 16378985 sha256 a12a82c4d980b9376d045bc0267a1784ed08c40fe7aecc26482b4bd4d4ba69b8
[2026-11-17T16:32:46Z] D 1794873600-1794931200.0.stream.jsonl.gz equal bytes 14158650 sha256 47ca06e1f8fd5ed20c7113a95c06a0f695c01e5b4009d8a6d8dd62a2c6358c4e
[2026-11-17T16:32:46Z] V 1794873600-1794927600.0.stream.jsonl.gz id 759792459 state uploaded api True bytes 12835147 digest sha256:4ad412e2b76b1a0818b95d58b8727e2631c9f23e5ca3cdb2839304f9c0e33653 url True download True
[2026-11-17T16:32:46Z] V 1794873600-1794928500.0.stream.jsonl.gz id 759792544 state uploaded api True bytes 12895500 digest sha256:c30dd934591935a9da7a879b40acddc2d7bcbb10332292a39963d1a9bd231d7a url True download True
[2026-11-17T16:32:46Z] V 1794873600-1794929400.0.stream.jsonl.gz id 759792659 state uploaded api True bytes 15269398 digest sha256:d95a86415e7862d0a57f516abacfd388697a56a57c74657e25e1efb1fdccf64c url True download True
[2026-11-17T16:32:46Z] V 1794873600-1794930300.0.stream.jsonl.gz id 759792767 state uploaded api True bytes 16378985 digest sha256:a12a82c4d980b9376d045bc0267a1784ed08c40fe7aecc26482b4bd4d4ba69b8 url True download True
[2026-11-17T16:32:46Z] V 1794873600-1794931200.0.stream.jsonl.gz id 759792859 state uploaded api True bytes 14158650 digest sha256:47ca06e1f8fd5ed20c7113a95c06a0f695c01e5b4009d8a6d8dd62a2c6358c4e url True download True
[2026-11-17T16:32:46Z] G-UPLOAD/G-DOWNLOAD release published on the tag                         True
[2026-11-17T16:32:46Z] G-UPLOAD/G-DOWNLOAD no asset missing                                     True
[2026-11-17T16:32:46Z] G-UPLOAD/G-DOWNLOAD no asset beyond the set                              True
[2026-11-17T16:32:46Z] G-UPLOAD/G-DOWNLOAD every asset uploaded, its bytes and digest the set's True
[2026-11-17T16:32:46Z] G-UPLOAD/G-DOWNLOAD every download the set's bytes and SHA-256           True
[2026-11-17T16:32:46Z] L {"assets_n": 5, "bytes_total": 71537680, "event": "verify", "release_id": 448903582, "run": 1794933020, "verify_sha256": "0e8556fe68e05eb4f85569d8879f818f503be4c3990919afb9c17e2b2dd20dd5", "wall_ns": 1794933166522886046}
[2026-11-17T16:32:46Z] X 1794873600-1794927600.0.stream.jsonl.gz 12835147 4ad412e2b76b1a0818b95d58b8727e2631c9f23e5ca3cdb2839304f9c0e33653 removed at second 166
[2026-11-17T16:32:46Z] X 1794873600-1794928500.0.stream.jsonl.gz 12895500 c30dd934591935a9da7a879b40acddc2d7bcbb10332292a39963d1a9bd231d7a removed at second 166
[2026-11-17T16:32:46Z] X 1794873600-1794929400.0.stream.jsonl.gz 15269398 d95a86415e7862d0a57f516abacfd388697a56a57c74657e25e1efb1fdccf64c removed at second 166
[2026-11-17T16:32:46Z] X 1794873600-1794930300.0.stream.jsonl.gz 16378985 a12a82c4d980b9376d045bc0267a1784ed08c40fe7aecc26482b4bd4d4ba69b8 removed at second 166
[2026-11-17T16:32:46Z] X 1794873600-1794931200.0.stream.jsonl.gz 14158650 47ca06e1f8fd5ed20c7113a95c06a0f695c01e5b4009d8a6d8dd62a2c6358c4e removed at second 166
[2026-11-17T16:32:46Z] G-DELETE every file of the set absent         True
[2026-11-17T16:32:46Z] G-DELETE each removal recorded                True
[2026-11-17T16:32:46Z] G-DELETE each slot keeps its slot.json        True
[2026-11-17T16:32:46Z] L {"already": 0, "event": "delete", "free_after": 10637975552, "free_before": 10566414336, "freed": 71537680, "gone": 5, "quiet_s": 0, "removed": 5, "run": 1794933020, "slots_kept": 5, "wall_ns": 1794933166737779085}
[2026-11-17T16:32:46Z] at the set's rate the cap stops the streams in 2.90 days, at 2026-11-20T14:08:19Z
[2026-11-17T16:32:46Z] at the set's rate the floor, base 43500000 bytes a day stops the streams in 2.36 days, at 2026-11-20T01:04:51Z
[2026-11-17T16:32:46Z] at the set's rate the floor, base 187760570 bytes a day stops the streams in 2.14 days, at 2026-11-19T19:51:26Z
[2026-11-17T16:32:46Z] L {"assets_n": 5, "bytes_total": 71537680, "ended_outside": 0, "event": "complete", "free_bytes": 10637971456, "held_s": 0, "peak_rss": 39821312, "rate_per_day": 1373523456, "removals": 5, "requests": 15, "rewardbook_at_end": {"ActiveState": "active", "MainPID": "1556307", "NRestarts": "0"}, "rewardbook_at_start": {"ActiveState": "active", "MainPID": "1556307", "NRestarts": "0"}, "run": 1794933020, "started_outside": 0, "stops": [["the cap", 1795183699], ["the floor, base 43500000 bytes a day", 1795136691], ["the floor, base 187760570 bytes a day", 1795117886]], "store_stream_bytes": 17204028, "wall_ns": 1794933166747222228}
[2026-11-17T16:32:46Z] COMPLETE: run 1794933020, 5 files, 71537680 bytes, Release rewardbook-streams-1794933020
[2026-11-17T16:32:46Z] peak memory of this run: 39821312 bytes
[2026-11-17T16:32:46Z] opens refused: 0 by TZ-27's hook, 0 by this file's; store opens 16; requests 15, uploads 5, downloads 5 (71537680 bytes); files removed 5
[2026-11-17T14:32:45Z] V 1794899700-stream.jsonl.gz id 759345248 state uploaded api True bytes 24489039 digest sha256:766bcac9b1095120fd50155c4c658cca36d3222c9d50c3688680122643168e47 url True download True
[2026-11-17T14:32:45Z] V 1794900600-stream.jsonl.gz id 759345348 state uploaded api True bytes 14687235 digest sha256:a205f2f47e6c9e97a8f466e38cf5ce5821b3eab25a88e563246a6db56b8ceac1 url True download True
[2026-11-17T14:32:45Z] V 1794901500-stream.jsonl.gz id 759345439 state uploaded api True bytes 29907565 digest sha256:76a97f0247d71b2e5863798444286979a50e8be9163f5dc1a165dd82f0068830 url True download True
[2026-11-17T14:32:45Z] V 1794902400-stream.jsonl.gz id 759345563 state uploaded api True bytes 15330083 digest sha256:8a18262c9eb1dd538511e8073cc1cbee20fd3b9b3320c976b071e0a5169880e0 url True download True
[2026-11-17T14:32:45Z] V 1794903300-stream.jsonl.gz id 759345719 state uploaded api True bytes 26282212 digest sha256:03e8e016233c8ad5b585a0aa8349128e6b3744857e02f4ace5696de03e83f21c url True download True
[2026-11-17T14:32:45Z] V 1794904200-stream.jsonl.gz id 759345846 state uploaded api True bytes 23191903 digest sha256:1425fcccafda50354d39c41df7193dce03d5e8fba7c71db6f21228ce696394ba url True download True
[2026-11-17T14:32:45Z] V 1794905100-stream.jsonl.gz id 759345970 state uploaded api True bytes 25197830 digest sha256:8921bb450b03d4bf847638b7ce75cfe26225906fa0b0baf5ff245313b3b9b72b url True download True
[2026-11-17T14:32:45Z] V 1794906000-stream.jsonl.gz id 759346125 state uploaded api True bytes 26961355 digest sha256:8e53cbd0124a1400edd26e7101a0ccdd629f122c7a8f619f2a701a09e9fd879e url True download True
[2026-11-17T14:32:45Z] V 1794906900-stream.jsonl.gz id 759346312 state uploaded api True bytes 23142422 digest sha256:963d911bda31d743013c91ab65654d889613c79752ad2ada78f1f1a63b1257f7 url True download True
[2026-11-17T14:32:45Z] V 1794907800-stream.jsonl.gz id 759346477 state uploaded api True bytes 23025122 digest sha256:78801b4c01fed98d893a42d9535cb1d9075fe93df975c61fd3d69bd1c7924e30 url True download True
[2026-11-17T14:32:45Z] V 1794908700-stream.jsonl.gz id 759346621 state uploaded api True bytes 21507439 digest sha256:b4c12b3e95e11354e290fefc1f7cd32b43d221509f4d85c5cb0f2ce2f06cdc17 url True download True
[2026-11-17T14:32:45Z] V 1794909600-stream.jsonl.gz id 759346771 state uploaded api True bytes 31615582 digest sha256:bab49e1d1716b94ad9e25cb5b269f162f797cdca094e4ac656265b38b23a821c url True download True
[2026-11-17T14:32:45Z] V 1794910500-stream.jsonl.gz id 759346916 state uploaded api True bytes 30849129 digest sha256:18ea3643046f08869fcd5cb46f8a639f8bdd68586798fe9131af4dd59bca379d url True download True
[2026-11-17T14:32:45Z] V 1794911400-stream.jsonl.gz id 759347079 state uploaded api True bytes 34236316 digest sha256:0079cf62046631670e05e209f119c97f0e6d5729987d5a57bcc4cd99be8c4bd8 url True download True
[2026-11-17T14:32:45Z] V 1794912300-stream.jsonl.gz id 759347230 state uploaded api True bytes 18766404 digest sha256:e5bdf92bf504ab5888561e36605f39ac2b3ea813a118a8dced4c7f952b24a877 url True download True
[2026-11-17T14:32:45Z] V 1794913200-stream.jsonl.gz id 759347343 state uploaded api True bytes 17188797 digest sha256:6673e234aebbfdbf535150c0d991dfe0c68ce63f06650c3f340e6a8927d68130 url True download True
[2026-11-17T14:32:45Z] V 1794914100-stream.jsonl.gz id 759347460 state uploaded api True bytes 28922324 digest sha256:a4bce15c37c2f679da89eccf1333572e50a16a2c41809e3cf36456edf1a69d63 url True download True
[2026-11-17T14:32:45Z] V 1794915000-stream.jsonl.gz id 759347625 state uploaded api True bytes 20914935 digest sha256:8038a2878fee8c54d647c35ae5dcbe7eb6d7b97ab1e1c74498cf81d6879fe6d1 url True download True
[2026-11-17T14:32:45Z] V 1794915900-stream.jsonl.gz id 759347754 state uploaded api True bytes 28674409 digest sha256:d61cc5363a0ad5adf1966c870bfcc10129400578d8c2ae0e5d73216531b00647 url True download True
[2026-11-17T14:32:45Z] V 1794916800-stream.jsonl.gz id 759347843 state uploaded api True bytes 21160720 digest sha256:ac08bd75f285a11669bae318a486f5544d052576dcb8f6dfef2f258635985243 url True download True
[2026-11-17T14:32:45Z] V 1794917700-stream.jsonl.gz id 759347983 state uploaded api True bytes 20816736 digest sha256:7cb98c1f220281b9433f17c54b4cc09534d12051c3476805901e7a14b490d356 url True download True
[2026-11-17T14:32:45Z] V 1794918600-stream.jsonl.gz id 759348063 state uploaded api True bytes 30698017 digest sha256:8eebaa6c7987e9cbc37be54dac0eb66200e1c10b45246e85e80d3dc85f114f04 url True download True
[2026-11-17T14:32:45Z] V 1794919500-stream.jsonl.gz id 759348185 state uploaded api True bytes 22299577 digest sha256:e87e29aa125638d5e41207988ba14174959ace4dfd8246502828be7d5b19a118 url True download True
[2026-11-17T14:32:45Z] V 1794920400-stream.jsonl.gz id 759348291 state uploaded api True bytes 32897035 digest sha256:04ce41f111e466994258fb00b4dc9321bdecd448180c7d2f4fa273f5039d1a4a url True download True
[2026-11-17T14:32:45Z] V 1794921300-stream.jsonl.gz id 759348391 state uploaded api True bytes 22893772 digest sha256:4548a89dd67189eb48402837bb8dd9059e2a333c093f2b8257de52cf5f18f136 url True download True
[2026-11-17T14:32:45Z] V 1794922200-stream.jsonl.gz id 759348468 state uploaded api True bytes 26054861 digest sha256:55fc7b32cf03314a7a7330cf95d7e09a4157c38a91e01041206965cdce591aa9 url True download True
[2026-11-17T14:32:45Z] V 1794923100-stream.jsonl.gz id 759348582 state uploaded api True bytes 22053959 digest sha256:22dd131545ceecd902f3d716a07a8b8b9e5249313aeac8ee563358c55af8d2fd url True download True
[2026-11-17T14:32:45Z] V 1794924000-stream.jsonl.gz id 759348692 state uploaded api True bytes 22649656 digest sha256:3bc622b838a7fdd53f22b17e87c0aa4c3401f59f4400ed4a629fdd0aa74af1b3 url True download True
[2026-11-17T14:32:45Z] G-UPLOAD/G-DOWNLOAD release published on the tag                         True
[2026-11-17T14:32:45Z] G-UPLOAD/G-DOWNLOAD no asset missing                                     True
[2026-11-17T14:32:45Z] G-UPLOAD/G-DOWNLOAD no asset beyond the set                              True
[2026-11-17T14:32:45Z] G-UPLOAD/G-DOWNLOAD every asset uploaded, its bytes and digest the set's True
[2026-11-17T14:32:45Z] G-UPLOAD/G-DOWNLOAD every download the set's bytes and SHA-256           True
[2026-11-17T14:32:45Z] L {"assets_n": 46, "bytes_total": 1151737742, "event": "verify", "release_id": 448733841, "run": 1794925184, "verify_sha256": "97ac1d26e90007de8eed71aca41e7db83973e71c026ea4a61ff803d6eaac99e7", "wall_ns": 1794925965687292163}
[2026-11-17T14:32:45Z] X 1794883500-stream.jsonl.gz 37665977 518ac663e1aaa237e24ec4a525c38cf9db3eb5533a9f7cedd9e400d1cc71defc removed
[2026-11-17T14:32:45Z] X 1794884400-stream.jsonl.gz 30091192 d1a69958a702c81d80bf71923e580737660634eb6b7047fb32fd58f607f1f1f4 removed
[2026-11-17T14:32:45Z] X 1794885300-stream.jsonl.gz 16605370 d3f564d1da59bfc480bd26f89c8f9164611c3d1736c3abe6e50910bf8c7ce571 removed
[2026-11-17T14:32:45Z] X 1794886200-stream.jsonl.gz 37351313 9459a393e5f7130a439c1e721a8d6d2157f751ba7a4f27a7eca6399a28059a06 removed
[2026-11-17T14:32:46Z] X 1794887100-stream.jsonl.gz 32968177 b37d88c443a3bdf83fdda74da48f6d14e23a1c41e9a1b951727d04c0ae89d91c removed
[2026-11-17T14:32:46Z] X 1794888000-stream.jsonl.gz 32268614 860c6244deed1d54b02f0a2fa31b96c87abbce2be971d42543e8aa537410589e removed
[2026-11-17T14:32:46Z] X 1794888900-stream.jsonl.gz 22326306 e83c1436612589cb0ad9cb4486c1386097dff144ff2b21c884d3a7c9d28d0c96 removed
[2026-11-17T14:32:46Z] X 1794889800-stream.jsonl.gz 23998193 31614f803fa2d7a455d86436f5f8b9266d5443c58e2d6f4c21d01a0618342dba removed
[2026-11-17T14:32:46Z] X 1794890700-stream.jsonl.gz 29937386 3a30ee6ae8399b3038ab351aff310126c93ec91f8c11f12c6e1b530bba028c58 removed
[2026-11-17T14:32:46Z] X 1794891600-stream.jsonl.gz 14018351 ea6372f311d7faf66760f69c36f359904cc9801128e084de88c9f265c8158640 removed
[2026-11-17T14:32:46Z] X 1794892500-stream.jsonl.gz 28094861 771fe93015e2942b8c4ec3487a3ad1f44c06aae8f191b275f5ea1380d667a695 removed
[2026-11-17T14:32:46Z] X 1794893400-stream.jsonl.gz 19729627 b7ee53f2e24a704e1d61e21ea0fb5e14795e08b328e10fcc82c683853ea2115f removed
[2026-11-17T14:32:46Z] X 1794894300-stream.jsonl.gz 26792400 0b49ac665b46cb1307bddc6bd2b04f3ee189f0aeee7470ab6290f7364f430612 removed
[2026-11-17T14:32:46Z] X 1794895200-stream.jsonl.gz 19855926 7e570f6ed11013b139f782b763bb369440c7adf6f72ec8cdf17058d4f4ff68cf removed
[2026-11-17T14:32:46Z] X 1794896100-stream.jsonl.gz 27122009 8363d0e1953062be2af8ca5f9430d2bea029de3da6ea91d225ea5c725998fcca removed
[2026-11-17T14:32:46Z] X 1794897000-stream.jsonl.gz 17444930 48e1d357888713cba2faff4aad75d99a7fec0ff6cfbfdea0cb077c450077b8a2 removed
[2026-11-17T14:32:46Z] X 1794897900-stream.jsonl.gz 27405751 896283e8c97341c21a732221812c55647b10c2c84a95703e904342c4a5b45c73 removed
[2026-11-17T14:32:46Z] X 1794898800-stream.jsonl.gz 21646925 4862d2f6bf3cd861fdcd409f0ce7a8321b9a6d734d9dca0ec2a35f28b4312096 removed
[2026-11-17T14:32:46Z] X 1794899700-stream.jsonl.gz 24489039 766bcac9b1095120fd50155c4c658cca36d3222c9d50c3688680122643168e47 removed
[2026-11-17T14:32:46Z] X 1794900600-stream.jsonl.gz 14687235 a205f2f47e6c9e97a8f466e38cf5ce5821b3eab25a88e563246a6db56b8ceac1 removed
[2026-11-17T14:32:46Z] X 1794901500-stream.jsonl.gz 29907565 76a97f0247d71b2e5863798444286979a50e8be9163f5dc1a165dd82f0068830 removed
[2026-11-17T14:32:46Z] X 1794902400-stream.jsonl.gz 15330083 8a18262c9eb1dd538511e8073cc1cbee20fd3b9b3320c976b071e0a5169880e0 removed
[2026-11-17T14:32:47Z] X 1794903300-stream.jsonl.gz 26282212 03e8e016233c8ad5b585a0aa8349128e6b3744857e02f4ace5696de03e83f21c removed
[2026-11-17T14:32:47Z] X 1794904200-stream.jsonl.gz 23191903 1425fcccafda50354d39c41df7193dce03d5e8fba7c71db6f21228ce696394ba removed
[2026-11-17T14:32:47Z] X 1794905100-stream.jsonl.gz 25197830 8921bb450b03d4bf847638b7ce75cfe26225906fa0b0baf5ff245313b3b9b72b removed
[2026-11-17T14:32:47Z] X 1794906000-stream.jsonl.gz 26961355 8e53cbd0124a1400edd26e7101a0ccdd629f122c7a8f619f2a701a09e9fd879e removed
[2026-11-17T14:32:47Z] X 1794906900-stream.jsonl.gz 23142422 963d911bda31d743013c91ab65654d889613c79752ad2ada78f1f1a63b1257f7 removed
[2026-11-17T14:32:47Z] X 1794907800-stream.jsonl.gz 23025122 78801b4c01fed98d893a42d9535cb1d9075fe93df975c61fd3d69bd1c7924e30 removed
[2026-11-17T14:32:47Z] X 1794908700-stream.jsonl.gz 21507439 b4c12b3e95e11354e290fefc1f7cd32b43d221509f4d85c5cb0f2ce2f06cdc17 removed
[2026-11-17T14:32:47Z] X 1794909600-stream.jsonl.gz 31615582 bab49e1d1716b94ad9e25cb5b269f162f797cdca094e4ac656265b38b23a821c removed
[2026-11-17T14:32:47Z] X 1794910500-stream.jsonl.gz 30849129 18ea3643046f08869fcd5cb46f8a639f8bdd68586798fe9131af4dd59bca379d removed
[2026-11-17T14:32:47Z] X 1794911400-stream.jsonl.gz 34236316 0079cf62046631670e05e209f119c97f0e6d5729987d5a57bcc4cd99be8c4bd8 removed
[2026-11-17T14:32:47Z] X 1794912300-stream.jsonl.gz 18766404 e5bdf92bf504ab5888561e36605f39ac2b3ea813a118a8dced4c7f952b24a877 removed
[2026-11-17T14:32:47Z] X 1794913200-stream.jsonl.gz 17188797 6673e234aebbfdbf535150c0d991dfe0c68ce63f06650c3f340e6a8927d68130 removed
[2026-11-17T14:32:47Z] X 1794914100-stream.jsonl.gz 28922324 a4bce15c37c2f679da89eccf1333572e50a16a2c41809e3cf36456edf1a69d63 removed
[2026-11-17T14:32:47Z] X 1794915000-stream.jsonl.gz 20914935 8038a2878fee8c54d647c35ae5dcbe7eb6d7b97ab1e1c74498cf81d6879fe6d1 removed
[2026-11-17T14:32:47Z] X 1794915900-stream.jsonl.gz 28674409 d61cc5363a0ad5adf1966c870bfcc10129400578d8c2ae0e5d73216531b00647 removed
[2026-11-17T14:32:47Z] X 1794916800-stream.jsonl.gz 21160720 ac08bd75f285a11669bae318a486f5544d052576dcb8f6dfef2f258635985243 removed
[2026-11-17T14:32:47Z] X 1794917700-stream.jsonl.gz 20816736 7cb98c1f220281b9433f17c54b4cc09534d12051c3476805901e7a14b490d356 removed
[2026-11-17T14:32:48Z] X 1794918600-stream.jsonl.gz 30698017 8eebaa6c7987e9cbc37be54dac0eb66200e1c10b45246e85e80d3dc85f114f04 removed
[2026-11-17T14:32:48Z] X 1794919500-stream.jsonl.gz 22299577 e87e29aa125638d5e41207988ba14174959ace4dfd8246502828be7d5b19a118 removed
[2026-11-17T14:32:48Z] X 1794920400-stream.jsonl.gz 32897035 04ce41f111e466994258fb00b4dc9321bdecd448180c7d2f4fa273f5039d1a4a removed
[2026-11-17T14:32:48Z] X 1794921300-stream.jsonl.gz 22893772 4548a89dd67189eb48402837bb8dd9059e2a333c093f2b8257de52cf5f18f136 removed
[2026-11-17T14:32:48Z] X 1794922200-stream.jsonl.gz 26054861 55fc7b32cf03314a7a7330cf95d7e09a4157c38a91e01041206965cdce591aa9 removed
[2026-11-17T14:32:48Z] X 1794923100-stream.jsonl.gz 22053959 22dd131545ceecd902f3d716a07a8b8b9e5249313aeac8ee563358c55af8d2fd removed
[2026-11-17T14:32:48Z] X 1794924000-stream.jsonl.gz 22649656 3bc622b838a7fdd53f22b17e87c0aa4c3401f59f4400ed4a629fdd0aa74af1b3 removed
[2026-11-17T14:32:48Z] G-DELETE every file of the set absent         True
[2026-11-17T14:32:48Z] G-DELETE each removal recorded by delete      True
[2026-11-17T14:32:48Z] G-DELETE each window keeps its window.json    True
[2026-11-17T14:32:48Z] L {"already": 0, "event": "delete", "free_after": 10056265728, "free_before": 8904314880, "freed": 1151737742, "gone": 46, "removed": 46, "run": 1794925184, "wall_ns": 1794925968357751566, "windows_kept": 46}
[2026-11-17T14:32:48Z] L {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "2012336", "NRestarts": "6", "ns": 1794925968395287827}, "phase": 168, "run": 1794925184, "wall_ns": 1794925968395480332}
[2026-11-17T14:32:48Z] L {"event": "kill", "exit": 0, "phase": 168, "run": 1794925184, "wall_ns": 1794925968400672033}
[2026-11-17T14:33:18Z] G-RESTART a stop of the marked process   True
[2026-11-17T14:33:18Z] G-RESTART stopped inside the band        True
[2026-11-17T14:33:18Z] G-RESTART a start of another process     True
[2026-11-17T14:33:18Z] G-RESTART within 60 s                    True
[2026-11-17T14:33:18Z] G-RESTART the same code                  True
[2026-11-17T14:33:18Z] G-COUNTER started before its window's documents    True
[2026-11-17T14:33:18Z] G-COUNTER the counter equals the store             True
[2026-11-17T14:33:18Z] G-COUNTER the counter below the cap                True
[2026-11-17T14:33:18Z] G-COUNTER no file of the set left                  True
[2026-11-17T14:33:18Z] G-UNIT active                   True
[2026-11-17T14:33:18Z] G-UNIT enabled                  True
[2026-11-17T14:33:18Z] G-UNIT fragment                 True
[2026-11-17T14:33:18Z] G-UNIT control group            True
[2026-11-17T14:33:18Z] G-UNIT ceiling                  True
[2026-11-17T14:33:18Z] G-UNIT argv                     True
[2026-11-17T14:33:18Z] G-UNIT cwd                      True
[2026-11-17T14:33:18Z] G-UNIT cgroup                   True
[2026-11-17T14:33:18Z] G-UNIT sole instance            True
[2026-11-17T14:33:18Z] G-UNIT restarts                 True
[2026-11-17T14:33:18Z] G-UNIT the new start's process  True
[2026-11-17T14:33:18Z] L {"NRestarts": "7", "W": 1794925800, "event": "restart", "free_bytes": 10056183808, "gap_ns": 6164444294, "pid": 2080877, "run": 1794925184, "stopped": 2012336, "stream_bytes": 18799261, "wall_ns": 1794925998527009819}
[2026-11-17T14:45:41Z] window 1794925800: pid 2080877, documents True; stream opened True, off_reason None, files ['stream.jsonl.gz'], segments 1, frames 282976, stored_bytes 23668756
[2026-11-17T14:45:41Z] G-RESUME run by the restarted process   True
[2026-11-17T14:45:41Z] G-RESUME the stream opened              True
[2026-11-17T14:45:41Z] G-RESUME no reason to keep it off       True
[2026-11-17T14:45:41Z] G-RESUME a stream file                  True
[2026-11-17T14:45:41Z] L {"T": 1794925800, "event": "resume", "reading": "PASS", "run": 1794925184, "wall_ns": 1794926741047976078}
[2026-11-17T14:45:41Z] at the set's rate the cap stops the streams in 3.31 days, at 2026-11-20T22:12:59Z
[2026-11-17T14:45:41Z] at the set's rate the floor, base 43500000 bytes a day stops the streams in 2.26 days, at 2026-11-19T20:53:52Z
[2026-11-17T14:45:41Z] at the set's rate the floor, base 187760570 bytes a day stops the streams in 2.13 days, at 2026-11-19T17:53:03Z
[2026-11-17T14:45:41Z] L {"assets_n": 46, "bytes_total": 1151737742, "ended_outside": 0, "event": "complete", "free_bytes": 10019958784, "peak_rss": 38199296, "rate_per_day": 2403626592, "requests": 97, "run": 1794925184, "started_outside": 0, "stops": [["the cap", 1795212779], ["the floor, base 43500000 bytes a day", 1795121632], ["the floor, base 187760570 bytes a day", 1795110783]], "store_stream_bytes": 42468017, "wall_ns": 1794926741621860011}
[2026-11-17T14:45:41Z] COMPLETE: run 1794925184, 46 files, 1151737742 bytes, Release pairbook-streams-1794925184
[2026-11-17T14:45:41Z] peak memory of this run: 38199296 bytes
[2026-11-17T14:45:41Z] opens refused: 0; store opens 140; requests 97, uploads 46, downloads 46 (1151737742 bytes); files removed 46
[2026-11-17T12:15:10Z] slot 1794916800 (2026-11-17T12:00:00Z) index 0: 150 markets; stream opened, 127016 frames, 1 segments, 15336193 bytes; polls 450 served of 450, 429 with a row, 0 missed
[2026-11-17T12:30:10Z] slot 1794917700 (2026-11-17T12:15:00Z) index 0: 150 markets; stream opened, 124569 frames, 1 segments, 14899640 bytes; polls 450 served of 450, 431 with a row, 0 missed
[2026-11-17T12:45:10Z] slot 1794918600 (2026-11-17T12:30:00Z) index 0: 150 markets; stream opened, 151806 frames, 2 segments, 17578881 bytes; polls 450 served of 450, 432 with a row, 0 missed
[2026-11-17T13:00:10Z] slot 1794919500 (2026-11-17T12:45:00Z) index 0: 150 markets; stream opened, 129057 frames, 1 segments, 15137957 bytes; polls 450 served of 450, 432 with a row, 0 missed
[2026-11-17T13:15:10Z] slot 1794920400 (2026-11-17T13:00:00Z) index 0: 150 markets; stream opened, 126443 frames, 1 segments, 14936094 bytes; polls 450 served of 450, 432 with a row, 0 missed
[2026-11-17T13:30:10Z] slot 1794921300 (2026-11-17T13:15:00Z) index 0: 150 markets; stream opened, 123047 frames, 1 segments, 14482834 bytes; polls 450 served of 450, 432 with a row, 0 missed
[2026-11-17T13:45:10Z] slot 1794922200 (2026-11-17T13:30:00Z) index 0: 150 markets; stream opened, 143491 frames, 1 segments, 16974774 bytes; polls 450 served of 450, 433 with a row, 0 missed
[2026-11-17T14:00:10Z] slot 1794923100 (2026-11-17T13:45:00Z) index 0: 150 markets; stream opened, 130728 frames, 1 segments, 15454418 bytes; polls 450 served of 450, 435 with a row, 0 missed
[2026-11-17T14:15:10Z] slot 1794924000 (2026-11-17T14:00:00Z) index 0: 150 markets; stream opened, 134814 frames, 1 segments, 16191136 bytes; polls 450 served of 450, 435 with a row, 0 missed
[2026-11-17T14:30:10Z] slot 1794924900 (2026-11-17T14:15:00Z) index 0: 150 markets; stream opened, 128698 frames, 1 segments, 15636458 bytes; polls 450 served of 450, 434 with a row, 0 missed
[2026-11-17T14:45:10Z] slot 1794925800 (2026-11-17T14:30:00Z) index 0: 150 markets; stream opened, 121924 frames, 1 segments, 14393715 bytes; polls 450 served of 450, 435 with a row, 0 missed
[2026-11-17T15:00:10Z] slot 1794926700 (2026-11-17T14:45:00Z) index 0: 150 markets; stream opened, 124332 frames, 1 segments, 14380455 bytes; polls 450 served of 450, 434 with a row, 0 missed
[2026-11-17T15:15:10Z] slot 1794927600 (2026-11-17T15:00:00Z) index 0: 150 markets; stream opened, 103597 frames, 1 segments, 12835147 bytes; polls 450 served of 450, 435 with a row, 0 missed
[2026-11-17T15:30:10Z] slot 1794928500 (2026-11-17T15:15:00Z) index 0: 150 markets; stream opened, 106477 frames, 1 segments, 12895500 bytes; polls 450 served of 450, 435 with a row, 0 missed
[2026-11-17T15:45:10Z] slot 1794929400 (2026-11-17T15:30:00Z) index 0: 150 markets; stream opened, 129926 frames, 1 segments, 15269398 bytes; polls 450 served of 450, 435 with a row, 0 missed
[2026-11-17T16:00:10Z] slot 1794930300 (2026-11-17T15:45:00Z) index 0: 150 markets; stream opened, 136749 frames, 1 segments, 16378985 bytes; polls 450 served of 450, 431 with a row, 0 missed
[2026-11-17T16:15:10Z] slot 1794931200 (2026-11-17T16:00:00Z) index 0: 150 markets; stream opened, 114690 frames, 1 segments, 14158650 bytes; polls 450 served of 450, 429 with a row, 0 missed
[2026-11-17T16:30:10Z] slot 1794932100 (2026-11-17T16:15:00Z) index 0: 150 markets; stream opened, 121322 frames, 1 segments, 14390252 bytes; polls 450 served of 450, 432 with a row, 0 missed
[2026-11-17T16:45:10Z] slot 1794933000 (2026-11-17T16:30:00Z) index 0: 150 markets; stream opened, 109891 frames, 1 segments, 13545800 bytes; polls 450 served of 450, 429 with a row, 0 missed
[2026-11-17T17:00:10Z] slot 1794933900 (2026-11-17T16:45:00Z) index 0: 150 markets; stream opened, 142196 frames, 1 segments, 16862011 bytes; polls 450 served of 450, 429 with a row, 0 missed
[2026-11-17T13:00:10Z] window 1794920400 (2026-11-17T13:00:00Z): documents from 2026-11-17T13:09:05Z
[2026-11-17T13:15:10Z] window 1794920400 closed: documents True in 2 attempts; checkpoints 7 of 7, missed 0; stream opened, 398605 frames, 1 segments, 32897035 bytes stored
[2026-11-17T13:15:10Z] window 1794921300 (2026-11-17T13:15:00Z): documents from 2026-11-17T13:24:05Z
[2026-11-17T13:30:10Z] window 1794921300 closed: documents True in 2 attempts; checkpoints 7 of 7, missed 0; stream opened, 279375 frames, 1 segments, 22893772 bytes stored
[2026-11-17T13:30:10Z] window 1794922200 (2026-11-17T13:30:00Z): documents from 2026-11-17T13:39:05Z
[2026-11-17T13:45:10Z] window 1794922200 closed: documents True in 2 attempts; checkpoints 7 of 7, missed 0; stream opened, 313531 frames, 1 segments, 26054861 bytes stored
[2026-11-17T13:45:10Z] window 1794923100 (2026-11-17T13:45:00Z): documents from 2026-11-17T13:54:05Z
[2026-11-17T14:00:10Z] window 1794923100 closed: documents True in 2 attempts; checkpoints 7 of 7, missed 0; stream opened, 271840 frames, 2 segments, 22053959 bytes stored
[2026-11-17T14:00:10Z] window 1794924000 (2026-11-17T14:00:00Z): documents from 2026-11-17T14:09:05Z
[2026-11-17T14:15:10Z] window 1794924000 closed: documents True in 2 attempts; checkpoints 7 of 7, missed 0; stream opened, 275749 frames, 1 segments, 22649656 bytes stored
[2026-11-17T14:15:10Z] window 1794924900 (2026-11-17T14:15:00Z): documents from 2026-11-17T14:24:05Z
[2026-11-17T14:30:10Z] window 1794924900 closed: documents True in 2 attempts; checkpoints 7 of 7, missed 0; stream opened, 227414 frames, 1 segments, 18799261 bytes stored
[2026-11-17T14:30:10Z] window 1794925800 (2026-11-17T14:30:00Z): documents from 2026-11-17T14:39:05Z
[2026-11-17T14:32:48Z] stop record written; requests 1350, sessions 58, frames 13347396, stream bytes 1102779834, other bytes 1304207
[2026-11-17T14:32:54Z] stale pid file (pid 2012336) replaced
[2026-11-17T14:32:54Z] start record: pid 2080877 commit e8b46a85d61e1a17841962846f6d3012046c2d70 file_sha256 caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec; free 10056183808 bytes, streams 18799261 bytes
[2026-11-17T14:32:54Z] window 1794925800 (2026-11-17T14:30:00Z): documents from 2026-11-17T14:39:05Z
[2026-11-17T14:45:10Z] window 1794925800 closed: documents True in 2 attempts; checkpoints 7 of 7, missed 0; stream opened, 282976 frames, 1 segments, 23668756 bytes stored
[2026-11-17T14:45:10Z] window 1794926700 (2026-11-17T14:45:00Z): documents from 2026-11-17T14:54:05Z
[2026-11-17T14:45:46Z] stop record written; requests 30, sessions 1, frames 282976, stream bytes 23668756, other bytes 32125
16076468	/root/tz46-work
368198237	/var/lib/btc-rewardbook
146635542	/var/lib/btc-pairbook
355893557	/root/btc-forensics
2532
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10605719552
               total        used        free      shared  buff/cache   available
Mem:      1002127360   552013824   102395904      253952   554565632   450113536
Swap:     3250581504   801951744  2448629760
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794745827
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794786586
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794792620
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794879020
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794928547
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794933020
```

## 3. Publication

- **Branch** `tz-46-capture-room`, **commit `c9d1071bb565b4cc1b22e5debb4ba4c6f87a9c5b`**, on `origin` at 2026-11-17T14:17:10Z. It holds two paths: `research/tz46-capture-room.py` (new, 1,644 lines, 88,254 bytes, `363b269c462d14da1656feb7bad92fec43adb1593209131fe5ca6e5c9f6755f6`) and `deploy/systemd/btc-rewardbook-archive.timer` (12 lines, 435 bytes, `7b0804285af6987340838bd59573897d013cf97edc5d4132cda7f3f9ba3e3824`, replacing `bf5af025…`). The push went through the remote URL's own credential. **Pull request #46**, https://github.com/seahomebatumi-ai/btc-5m-twap/pull/46, opened with `gh pr create`. It is not merged: merging is the Boss's step, after the Architect's verdict.
- **Host deployment:** `/etc/systemd/system/btc-rewardbook-archive.timer` is now the branch's file (`cmp exit=0` in `92-closing.log`). Until the merge, the host's timer is ahead of `main`, as the TZ's header states.
- **Release assets:** this TZ publishes none of its own. The archives' own runs made Releases `448733841` (`pairbook-streams-1794925184`), `rewardbook-streams-1794928547` and `448903582` (`rewardbook-streams-1794933020`). Each was proved by its archive's own `verify` record and its tag read on `origin`.
```
Tue Nov 17 02:17:02 PM UTC 2026
M  deploy/systemd/btc-rewardbook-archive.timer
A  research/tz46-capture-room.py
commit exit=0
13f3143131de9f3c7ef687f5803aa910daa4405b	HEAD
13f3143131de9f3c7ef687f5803aa910daa4405b	refs/heads/main
7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8	refs/heads/tz-23-maker-m0
6f045cffc3601b589d3b8b7a6a9af6f73991e18b	refs/heads/tz-24-nesting-b2
e8b46a85d61e1a17841962846f6d3012046c2d70	refs/heads/tz-26-nesting-b3-capture
bce5a85be7850a33f95192265b916cc9c5e0aaf1	refs/heads/tz-27-pairbook-archive
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/heads/tz-28-pairbook-archive-timer
f6425f713034724210dc120d2108bcfad63cadc6	refs/heads/tz-29-maker-m0-second-look
fcd9ca566e9b948f0426707e7c3b5684f7f03b04	refs/heads/tz-30-nesting-b3-measure
404288fb03ffd3619b2183f121d45688def8fba8	refs/heads/tz-31-who-earns
b601f756edea59adf536d7ef05226d6f06bcef13	refs/heads/tz-32-our-quoting
2dcd70e08b18b93c64bb67d9849ac1216ce40e41	refs/heads/tz-33-reward-book-capture
6a615257277d3c94dafd4d39783499560a344648	refs/heads/tz-34-rewardbook-archive-timer
6c74b62bfef7afad2c71c742411124387327a588	refs/heads/tz-35-advisor-bot
444628905625809f24dd1fa51159b4093b763789	refs/heads/tz-36-advisor-trust-block
6d70c6aaa5457365743d2fb80e13e0817af8d292	refs/heads/tz-37-capital-allocation
8f37199aa4f9e14cb08534b1be3b7c258af917c2	refs/heads/tz-38-adv3-pit-validation
fc687582ebc4064b7483e2ac5cb9ca5b1af9c9f5	refs/heads/tz-39-advisor-checks
433ce139eedc112862ecf678cda6eaa2577d73d3	refs/heads/tz-40-strong-every-rank
4e6db2d16dda3da14957120d636f537dfc0bcc87	refs/heads/tz-42-advisor-registry
ab0f3873a66eb302225c3849da362bfe301e93df	refs/heads/tz-43-l0-our-quote
ab0a8be170786ee9b4c9bfd18ed5a522db669932	refs/heads/tz-44-l0-inputs-release
01756f665893096ab38ae10dfbe58f074f8fb648	refs/heads/tz-45-l0-rule-w
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
fcd9ca566e9b948f0426707e7c3b5684f7f03b04	refs/pull/29/head
ee2f6327390ef4d0c6169d1fba1a2ed4ae936dc3	refs/pull/3/head
404288fb03ffd3619b2183f121d45688def8fba8	refs/pull/30/head
b601f756edea59adf536d7ef05226d6f06bcef13	refs/pull/31/head
2dcd70e08b18b93c64bb67d9849ac1216ce40e41	refs/pull/32/head
6a615257277d3c94dafd4d39783499560a344648	refs/pull/34/head
6c74b62bfef7afad2c71c742411124387327a588	refs/pull/35/head
444628905625809f24dd1fa51159b4093b763789	refs/pull/36/head
6d70c6aaa5457365743d2fb80e13e0817af8d292	refs/pull/37/head
8f37199aa4f9e14cb08534b1be3b7c258af917c2	refs/pull/38/head
fc687582ebc4064b7483e2ac5cb9ca5b1af9c9f5	refs/pull/39/head
0e13a5c76dfa2469ff25b3b0dd282872decf6f25	refs/pull/4/head
433ce139eedc112862ecf678cda6eaa2577d73d3	refs/pull/40/head
4e6db2d16dda3da14957120d636f537dfc0bcc87	refs/pull/41/head
cca11090695ae824c94a6f097959d93355ce3986	refs/pull/42/head
ab0f3873a66eb302225c3849da362bfe301e93df	refs/pull/43/head
ab0a8be170786ee9b4c9bfd18ed5a522db669932	refs/pull/44/head
01756f665893096ab38ae10dfbe58f074f8fb648	refs/pull/45/head
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
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792650248
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792724420
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792810820
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792850109
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792897220
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792908757
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792930875
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792983620
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793070020
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793082340
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793156420
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793169873
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793187616
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793242820
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793260762
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793356734
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793415620
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793502020
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793588420
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793674820
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793761220
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793774618
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793847620
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793861040
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793934020
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793968389
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793990589
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1794020420
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1794106820
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1794193220
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1794279620
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1794366020
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1794452420
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1794521401
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1794625220
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1794637296
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1794711620
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1794744627
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1794785386
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1794798020
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1794884420
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793263627
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793286490
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793306720
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793321975
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793323820
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793357934
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793410220
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793496620
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793583020
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793669420
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793755820
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793775818
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793842220
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793862240
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793928620
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793991789
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794015020
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794101420
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794187820
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794274220
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794360620
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794447020
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794522601
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794533420
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794619820
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794638496
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794706220
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794745827
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794786586
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794792620
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1794879020
d3251aa2bd312409f7b096bfd5968f3bedbd1be5	refs/tags/tz-01a-dataset
ea9290b92b9fa50c22d0560d5d01dfa392af44df	refs/tags/tz-01a-dataset^{}
e299d4e45f48b7efaa8cb18bd54b139fc0627630	refs/tags/tz-27-pairbook-streams
bce5a85be7850a33f95192265b916cc9c5e0aaf1	refs/tags/tz-27-pairbook-streams^{}
ab0a8be170786ee9b4c9bfd18ed5a522db669932	refs/tags/tz-44-l0-inputs
01756f665893096ab38ae10dfbe58f074f8fb648	refs/tags/tz-45-l0-rule-w-inputs
ls-remote exit=0
remote: 
remote: Create a pull request for 'tz-46-capture-room' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-46-capture-room        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-46-capture-room -> tz-46-capture-room
branch 'tz-46-capture-room' set up to track 'origin/tz-46-capture-room'.
push exit=0
2026-11-17T14:17:10.253028593Z
c9d1071bb565b4cc1b22e5debb4ba4c6f87a9c5b	refs/heads/tz-46-capture-room
c9d1071bb565b4cc1b22e5debb4ba4c6f87a9c5b
3	4	deploy/systemd/btc-rewardbook-archive.timer
1644	0	research/tz46-capture-room.py
```
```
Tue Nov 17 02:17:19 PM UTC 2026
https://github.com/seahomebatumi-ai/btc-5m-twap/pull/46
exit=0
```
Contract §4.2's self-check, `99-selfcheck.log`:
```
Tue Nov 17 05:03:13 PM UTC 2026
From https://github.com/seahomebatumi-ai/btc-5m-twap
 * [new tag]         pairbook-streams-1794925184 -> pairbook-streams-1794925184
 * [new tag]         rewardbook-streams-1794928547 -> rewardbook-streams-1794928547
 * [new tag]         rewardbook-streams-1794933020 -> rewardbook-streams-1794933020
0
deploy/systemd/btc-rewardbook-archive.timer
research/tz46-capture-room.py
3	4	deploy/systemd/btc-rewardbook-archive.timer
1644	0	research/tz46-capture-room.py
grep exit=1
```
The first line printed `0`: the implementation commit is not on `main`. The diff holds only the two implementation paths, at `3 4` and `1644 0`. No `.parquet` or `.zip` is on `main` (`grep exit=1`).

## 4. Gate

| gate | as the TZ fixes it | deciding number | verdict |
|---|---|---|---|
| G-FORENSIC (§4.1) | every planned file absent, each removal recorded once, the store less exactly the planned files; a plan of at least 13 against `tz-44-l0-inputs` | 47 of 47 removed, 229,053,786 bytes; 47 ≥ 13 | **PASS** |
| G-PAIR (§4.2) | eight checks | 8 of 8 | **PASS** |
| G-TIMER (§4.3) | eleven checks, in B-TIMER and at §3.9 | 11 of 11, twice | **PASS** |
| G-TRIGGER (§4.4) | `TRIGGER_UNIT` the timer, trigger in [E, E+60], start record within 60 s | trigger − E = 0.000 s | **PASS** |
| G-RUN (§4.4) | complete, ≤ 1 deferral, `success`/`0`, 0 outside | 0 deferrals; 0 / 0 outside | **PASS** |
| G-TAG (§4.4) | lightweight at `6a61525…` | `rewardbook-streams-1794933020`, peeled None | **PASS** |
| G-NEXT (§4.4) | no FAIL slot, at least one slot | 1 slot, PASS | **PASS** |
| G-STILL (§4.6) | recorder, reward book, advisor unchanged; pair book only by its archive's restarts, then stopped | 1 restart record, then stopped | **PASS** |
| G-ROOM (§4.7) | margin ≥ 2,000,000,000 bytes | **2,908,396,574.000** | **PASS** |

`FIRST PASS: 4 of 4`. Nothing was tuned, and no threshold was read other than as written.

## 5. Validation

- **V1** — `FINGERPRINT PASS` at §0.2 and §3.1: revision `2026-11-16-a`, anchors 6 of 6 with 4 re-derived, rows 64 = 61 + 2 + 1, frozen 61 of 61 equal. **Asserted.**
- **V2** — `NUMBER PASS - 2 of 2` at §0.5 (14:16:36Z) and §3.1 (14:16:50Z, after the fetch). Refs: 162 against 160, every difference named in §1. **Asserted.**
- **V3** — §0.1's script at §0.1 and §3.1: two files at the table's lines, bytes and SHA-256; in the worktree the timer `replaced` from `bf5af025…`. **Asserted.**
- **V4** — the branch: two paths, `--numstat` `1644 0` and `3 4`, and the commit on `origin` (`c9d1071…`) equal to the worktree's `HEAD`. **Asserted by §3.1's reads.**
- **V5** — `SELFTEST PASS: 29 checks`, `opens refused: 1` (check 28's own refusal), peak 28,692,480. **Asserted.**
```
Tue Nov 17 02:17:27 PM UTC 2026
[2026-11-17T14:17:27Z] ok 1 the eight elapses of a day are systemd's iterations of *-*-* 01/3:30:20 UTC
[2026-11-17T14:17:27Z] ok 2 the next elapse is strictly after the instant, across midnight too
[2026-11-17T14:17:27Z] ok 3 B-TIMER's band: 25 to 10 minutes before an elapse, 10:05:20 to 19:20:20 UTC, neither archive running
[2026-11-17T14:17:27Z] ok 4 B-PAIR-OFF's band: 07:30:00 to 19:00:00 UTC, neither archive running
[2026-11-17T14:17:27Z] ok 5 G-TIMER: 11 checks; a run on a start, a second calendar, another elapse, the unit disabled, another accuracy, another unit, TZ-34's file or the pair book archive's timer enabled each read FAIL
[2026-11-17T14:17:27Z] ok 6 systemctl's stamps under TZ=UTC
[2026-11-17T14:17:27Z] ok 7 G-TRIGGER: the timer's own trigger at the elapse; another unit, a trigger 1,800 s early, a late record and no trigger at all each read FAIL; LastTriggerUSec where systemd set none
[2026-11-17T14:17:27Z] ok 8 a ledger's first start since an instant - a pending set resumed counts by its new start - and a run's state from its last start
[2026-11-17T14:17:27Z] ok 9 G-NEXT's slots across the removals, and its reading the worst
[2026-11-17T14:17:27Z] ok 10 G-NEXT's verdict of one slot
[2026-11-17T14:17:27Z] ok 11 G-STILL: unchanged; moved by its archive's restarts; stopped after B-PAIR-OFF alone; anything else FAIL
[2026-11-17T14:17:27Z] ok 12 G-PAIR: 8 checks; a deferred run, another tag, the pair book enabled or running, its timer enabled, no restart, a request outside the idle stretch or the service running each read FAIL
[2026-11-17T14:17:27Z] ok 13 G-ROOM at its bound, and a byte below it
[2026-11-17T14:17:27Z] ok 14 NUMBER: this TZ's file alone of its number, and no report
[2026-11-17T14:17:27Z] ok 15 reclaim keeps by name the state, the plan, the removals, both room files and the logs
[2026-11-17T14:17:27Z] ok 16 the branch's timer: its SHA-256, one calendar, accuracy 1 s, its unit, no monotonic trigger
[2026-11-17T14:17:27Z] ok 17 STREAM_FLOOR is the reward book's own, line 190 of its file as its unit runs it
[2026-11-17T14:17:27Z] ok 18 the hook: writes in the work tree alone; of the reward book its slot records and runtime.jsonl read, nothing else opened; nothing of the pair book or the recorder opened
[2026-11-17T14:17:27Z] ok 19 the hook: a forensic file removed only by forensics-remove and only where planned; the store written only by reclaim's exclusive create
[2026-11-17T14:17:27Z] ok 20 the hook: GitHub's hosts alone are reached
[2026-11-17T14:17:27Z] ok 21 both stores' stream and other files by their own names
[2026-11-17T14:17:27Z] MemAvailable read 1: 328486912 bytes, floor 133073162
[2026-11-17T14:17:27Z] free 8711229440 bytes, floor 2300000000
[2026-11-17T14:17:27Z] the forensic store /root/tz46-work/selftest-tmp/forensics: 7 files, 6202 bytes, hashed in 0.0 s
[2026-11-17T14:17:27Z] the repository's Releases read anonymously: 123, 4 assets with a digest
[2026-11-17T14:17:27Z] files a Release holds by bytes and SHA-256: 4; held by none: 3
[2026-11-17T14:17:27Z] P /root/tz46-work/selftest-tmp/forensics/a.tar 3000 f2eb889620bb1c00f5799d261cfa20adb68b0488ed8aa0945df50a5631867432: a.tar of tz-44-l0-inputs, asset 11, api True, download 200 equal
[2026-11-17T14:17:27Z] P /root/tz46-work/selftest-tmp/forensics/g.bin 41 b7d0d3ab41ac744e564347dd64f45a9f7faf4d7d99d495ac566669d886c942ce: g.bin of rewardbook-streams-1, asset 22, api True, download 200 NOT EQUAL
[2026-11-17T14:17:27Z] P /root/tz46-work/selftest-tmp/forensics/h.bin 42 8e713a4ea4cdb2e161e76784cdc2ce21877bfb1ccb904989cc549110bd0132d5: h.bin of rewardbook-streams-1, asset 23, api True, download 200 equal
[2026-11-17T14:17:27Z] P /root/tz46-work/selftest-tmp/forensics/sub/d.copy 3000 f2eb889620bb1c00f5799d261cfa20adb68b0488ed8aa0945df50a5631867432: a.tar of tz-44-l0-inputs, asset 11, api True, download 200 equal
[2026-11-17T14:17:27Z] files proved against tz-44-l0-inputs: 2, at least 3 expected
[2026-11-17T14:17:27Z] ok 22 forensics: fewer files proved against a named Release than expected is BLOCKED, and no plan is written
[2026-11-17T14:17:27Z] MemAvailable read 1: 328597504 bytes, floor 133073162
[2026-11-17T14:17:27Z] free 8711225344 bytes, floor 2300000000
[2026-11-17T14:17:27Z] the forensic store /root/tz46-work/selftest-tmp/forensics: 7 files, 6202 bytes, hashed in 0.0 s
[2026-11-17T14:17:27Z] the repository's Releases read anonymously: 123, 4 assets with a digest
[2026-11-17T14:17:27Z] files a Release holds by bytes and SHA-256: 4; held by none: 3
[2026-11-17T14:17:27Z] P /root/tz46-work/selftest-tmp/forensics/a.tar 3000 f2eb889620bb1c00f5799d261cfa20adb68b0488ed8aa0945df50a5631867432: a.tar of tz-44-l0-inputs, asset 11, api True, download 200 equal
[2026-11-17T14:17:27Z] P /root/tz46-work/selftest-tmp/forensics/g.bin 41 b7d0d3ab41ac744e564347dd64f45a9f7faf4d7d99d495ac566669d886c942ce: g.bin of rewardbook-streams-1, asset 22, api True, download 200 NOT EQUAL
[2026-11-17T14:17:27Z] P /root/tz46-work/selftest-tmp/forensics/h.bin 42 8e713a4ea4cdb2e161e76784cdc2ce21877bfb1ccb904989cc549110bd0132d5: h.bin of rewardbook-streams-1, asset 23, api True, download 200 equal
[2026-11-17T14:17:27Z] P /root/tz46-work/selftest-tmp/forensics/sub/d.copy 3000 f2eb889620bb1c00f5799d261cfa20adb68b0488ed8aa0945df50a5631867432: a.tar of tz-44-l0-inputs, asset 11, api True, download 200 equal
[2026-11-17T14:17:27Z] files proved against tz-44-l0-inputs: 2, at least 2 expected
[2026-11-17T14:17:27Z] FORENSICS PLAN: 3 files, 6042 bytes, each held by a public Release and proved; 4 rows, 1 not proved; 9 API requests, 3 downloads, 3083 bytes; forensics-plan.json sha256 e9339f36ed3b2cd014d81be33eb1276471aece94e3b687ed7c34408eaac7d274
[2026-11-17T14:17:27Z] ok 23 forensics: a file and its copy held by one asset, downloaded once; a digest of other bytes, an asset not uploaded, a draft and an empty file left; a download of other bytes not planned; 7 pages, 2 asset lists
[2026-11-17T14:17:27Z] ok 24 every request names this file's User-Agent and carries no credential
[2026-11-17T14:17:27Z] MemAvailable read 1: 328634368 bytes, floor 133073162
[2026-11-17T14:17:27Z] free 8711196672 bytes, floor 2300000000
[2026-11-17T14:17:27Z] ok 25 a planned file changed after its proof: BLOCKED, nothing removed
[2026-11-17T14:17:27Z] MemAvailable read 1: 328634368 bytes, floor 133073162
[2026-11-17T14:17:27Z] free 8711196672 bytes, floor 2300000000
[2026-11-17T14:17:27Z] X /root/tz46-work/selftest-tmp/forensics/a.tar 3000 f2eb889620bb1c00f5799d261cfa20adb68b0488ed8aa0945df50a5631867432 removed: a.tar of tz-44-l0-inputs
[2026-11-17T14:17:27Z] X /root/tz46-work/selftest-tmp/forensics/h.bin 42 8e713a4ea4cdb2e161e76784cdc2ce21877bfb1ccb904989cc549110bd0132d5 removed: h.bin of rewardbook-streams-1
[2026-11-17T14:17:27Z] X /root/tz46-work/selftest-tmp/forensics/sub/d.copy 3000 f2eb889620bb1c00f5799d261cfa20adb68b0488ed8aa0945df50a5631867432 removed: a.tar of tz-44-l0-inputs
[2026-11-17T14:17:27Z] G-FORENSIC every planned file absent                    True
[2026-11-17T14:17:27Z] G-FORENSIC every removal recorded once                  True
[2026-11-17T14:17:27Z] G-FORENSIC the store less exactly the planned files     True
[2026-11-17T14:17:27Z] G-FORENSIC PASS: 3 of 3 removed, 6042 bytes; this run 3 files, 6042 bytes; free 8711196672 before, 8711204864 after
[2026-11-17T14:17:27Z] ok 26 forensics-remove: the three proved files gone, every other file kept
[2026-11-17T14:17:27Z] MemAvailable read 1: 328634368 bytes, floor 133073162
[2026-11-17T14:17:27Z] free 8711204864 bytes, floor 2300000000
[2026-11-17T14:17:27Z] G-FORENSIC every planned file absent                    True
[2026-11-17T14:17:27Z] G-FORENSIC every removal recorded once                  True
[2026-11-17T14:17:27Z] G-FORENSIC the store less exactly the planned files     True
[2026-11-17T14:17:27Z] G-FORENSIC PASS: 3 of 3 removed, 6042 bytes; this run 0 files, 0 bytes; free 8711204864 before, 8711204864 after
[2026-11-17T14:17:27Z] ok 27 forensics-remove again removes nothing and records nothing twice
[2026-11-17T14:17:27Z] ok 28 the hook refuses a removal in the real forensic store outside forensics-remove
[2026-11-17T14:17:28Z] ok 29 the temporary trees removed
[2026-11-17T14:17:28Z] SELFTEST PASS: 29 checks
[2026-11-17T14:17:28Z] peak memory of this run: 28692480 bytes
[2026-11-17T14:17:28Z] opens refused: 1; reward book opens: 0; API requests 9, downloads 3, 3083 bytes; files removed 0
exit=0
```
- **V6** — `still: recorded`. `scratch` named 2 directories earlier and 1 live; this session's own is not listed. `RECLAIM PASS`, then each removal's `test -e` gave `exit=1`, 2 of 2. **Asserted.**
- **V7** — `room before`: every count printed (§2.1). **Recorded, not asserted**: it is a baseline.
- **V8** — `FORENSICS PLAN:` 47 files proved against `tz-44-l0-inputs` (≥ 13), 6 API requests (≤ 40). Then `G-FORENSIC PASS: 47 of 47 removed`, 229,053,786 bytes, free 8,709,038,080 → 8,938,147,840. **Asserted.**
- **V9** — B-PAIR-OFF: `pairwait=0`; `timer exit=0` and `pairbook exit=0`; `G-PAIR PASS: 8 of 8`; residual 2 windows, 42,468,017 bytes. G-PAIR's verdict **printed**; the stops' exits **recorded**.
- **V10** — B-TIMER inside its band (opened 16:05:48Z, 3,948 s into its step): the `timer` mark, the `install`, the `daemon-reload` and the `restart`, each chained on `&&` and so each `exit=0`; then `G-TIMER PASS: 11 of 11`, with the block's `exit=0`. **Asserted.**
- **V11** — `FIRST PASS: 4 of 4` after 6 `NOT YET` reads, with no B-RETRY. **Printed, exit `0`.**
- **V12** — `G-STILL PASS`; `G-TIMER PASS: 11 of 11` again, next run 19:30:20Z. G-STILL **printed**; G-TIMER **asserted**.
- **V13** — `G-ROOM PASS`: the room 10,653,932,210, the margin 2,908,396,574, lasting 66.9 days at 43,500,000 a day and 15.5 days at 187,760,570 a day [modelled]. **Printed, exit `0`.**
- **V14** — every mode's printed peak is under 66,536,581. The largest is `forensics`, 45,858,816. The others run from 26,075,136 (`number`, `timer`) to 30,486,528 (`reclaim`), across 111 peak lines in 19 logs. Every memory read is in §2.10. **Recorded.**
- **V15** — every free-space read with its instant: §2.10. **Recorded.**
- **V16** — contract §4.2's self-check: `0`; the two paths; their `--numstat`; nothing (§3). **Asserted.**
- **V17** — §9: see §5.1 below. **Asserted where a command asserts it.**

### 5.1 B-RECLAIM-OWN (§9), verbatim from the session

Run at 17:05:34Z by the Executor, not refused. Every line printed:

```
[2026-11-17T17:05:34Z] reclaim: 4139 report tokens; the forensic store holds 2532 files
[2026-11-17T17:05:34Z] reclaim: /root/tz46-work/wt skipped: no file but its HEAD's, and HEAD c9d1071bb565b4cc1b22e5debb4ba4c6f87a9c5b is its upstream's
[2026-11-17T17:05:34Z] R copied becd4c5c35bd6484a659bd1c211d9a515401d73db13a1cab03aa43a6ee6f414f /root/btc-forensics/tz46-work--forensics-plan.json
[2026-11-17T17:05:34Z] R copied f95519f5b0b95474e979de30142914c32fc666f56146ed41146e35a8ae2de2a6 /root/btc-forensics/tz46-work--forensics-removed.jsonl
[2026-11-17T17:05:34Z] R copied bea263a47c88413fa7315a38938a705e7873de52f6f3b9ee0696fdff98029deb /root/btc-forensics/tz46-work--room-after.json
[2026-11-17T17:05:34Z] R copied 1e8c05d977bcb3c5817c56157df53057e6e2974d7fabceaa9226c3d8ab429bbd /root/btc-forensics/tz46-work--room-before.json
[2026-11-17T17:05:34Z] R copied 7a32ec020d0b124612a0812403241c6eebcacf667aa21473a6693b77ad1898ad /root/btc-forensics/tz46-work--state.json
[2026-11-17T17:05:34Z] R copied 4aaf2718ec55e00fca4b90449c7812bba42e2ba5c7d25bb0286c3b16d5b1a225 /root/btc-forensics/tz46-work--logs--00-ready.log
[2026-11-17T17:05:34Z] R copied a33fa4dcdbe0d5b1d28f1466ba6984734eb25b8cb69d2518cca0783a9e9fc711 /root/btc-forensics/tz46-work--logs--01-stage.log
[2026-11-17T17:05:34Z] R copied ae1c59a5782b339e58a121fff0a0c75df1e2c0b30bb952ce96027644f154dd2d /root/btc-forensics/tz46-work--logs--02-fingerprint.log
[2026-11-17T17:05:34Z] R copied 12a6ced0825eb5a3e4998cb3d298d1374244f91577343540f207724cb573e2d5 /root/btc-forensics/tz46-work--logs--03-host-gate.log
[2026-11-17T17:05:34Z] R copied d9a8034a8151e7f61a65d4282678164266600e2a640bc390287267c7ad995a4c /root/btc-forensics/tz46-work--logs--05-number.log
[2026-11-17T17:05:34Z] R copied a26a6606e17a29aed86e20290edefc0e5b35e3545fb701755bb1b7ec19673a65 /root/btc-forensics/tz46-work--logs--05-refs.log
[2026-11-17T17:05:34Z] R copied 5ce881d3415456a9b5f747db4d8da50388f20092e86efc27a972e83a50d325b2 /root/btc-forensics/tz46-work--logs--10-number.log
[2026-11-17T17:05:34Z] R copied 5d1ef37428a138bb1d92fe0f4e3224360dd27b58e198c87f1a4c5e1e67d244d3 /root/btc-forensics/tz46-work--logs--11-worktree.log
[2026-11-17T17:05:34Z] R copied 7f10d16a334581c7709e05f455bd469fc0858252e3c74e5df06aca68e61334a3 /root/btc-forensics/tz46-work--logs--12-fingerprint.log
[2026-11-17T17:05:34Z] R copied caf3f5b4cc2b05356936d13e045c2793d660190554923110f71c359db44f3b32 /root/btc-forensics/tz46-work--logs--13-push.log
[2026-11-17T17:05:34Z] R copied 96815abbc38c6d224a094826f8b00682e153b47ec4a2c75c532c0273c8312872 /root/btc-forensics/tz46-work--logs--14-pr.log
[2026-11-17T17:05:34Z] R copied dd3bd1faeb9aebd7a2dea9deb80e95ebfa25dcbc52a9eba31ab56edd2b4dbf93 /root/btc-forensics/tz46-work--logs--20-selftest.log
[2026-11-17T17:05:34Z] R copied 70935f2baf390d13ad2c1077ff60808682998de208f5780aebf7edce0d56b87b /root/btc-forensics/tz46-work--logs--30-still.log
[2026-11-17T17:05:34Z] R copied c4f5e24a8ab4a3c40b468f42517616360e9570fc001a6ae528690c7fe494de50 /root/btc-forensics/tz46-work--logs--31-scratch.log
[2026-11-17T17:05:34Z] R copied 37e10829d5b752a974f7fb091207ed6064c24d66e851af605d9bdca08b92f036 /root/btc-forensics/tz46-work--logs--32-reclaim-scratch.log
[2026-11-17T17:05:34Z] R copied 6666fa3ba7bd862bdecdd815260905d6a18ee40911a2b4e0c494e80a4061852d /root/btc-forensics/tz46-work--logs--35-room-before.log
[2026-11-17T17:05:34Z] R copied ba1a54ec500c4b890c9a9d7742106674fd8477f0ec5b6ae7d50cb24119eaf39d /root/btc-forensics/tz46-work--logs--40-forensics.log
[2026-11-17T17:05:34Z] R copied 99b9055383a84b4def30303caf1a69bfbef0aa18fb8e2d6e4a5778ccfbe5e3fc /root/btc-forensics/tz46-work--logs--41-B-FORENSICS.log
[2026-11-17T17:05:34Z] R copied 0d60e80b8f80f060a22affc9a3b3a084d6d9fa6f054d5214f53993cd5fb862fa /root/btc-forensics/tz46-work--logs--50-B-PAIR-OFF.log
[2026-11-17T17:05:34Z] R copied 39e214d0702d7b07f82d5c4365142fd751ee16ad01ef63ae6613da21f4851574 /root/btc-forensics/tz46-work--logs--60-band-timer.log
[2026-11-17T17:05:34Z] R copied 05d198944d01cf097de331c88c66a3a015fc3f4cb96c53ee0cea3c9a7e7a88e1 /root/btc-forensics/tz46-work--logs--61-B-TIMER.log
[2026-11-17T17:05:34Z] R copied 6e90622eca448e2bb01d73c599f24c9909de9e4525824f542e98ca9cc4ad3c54 /root/btc-forensics/tz46-work--logs--70-first.log
[2026-11-17T17:05:34Z] R copied be62444a621deba510a9c4c95129d1079cd86acdafdf292a7072379b10d2dd9b /root/btc-forensics/tz46-work--logs--80-still.log
[2026-11-17T17:05:34Z] R copied 7dfdce2202a66e8ccce6cc90df32b5758bc84abe9d2eb004092fb83b89c12205 /root/btc-forensics/tz46-work--logs--81-timer-again.log
[2026-11-17T17:05:34Z] R copied 3bb90cbd6fe94aac72499aa203cd191eea2b52b887e98f4f33d4a4054713486f /root/btc-forensics/tz46-work--logs--90-room-after.log
[2026-11-17T17:05:34Z] R copied 430f9666d8aced790e4dcdd4c40a5a5ef786cb32d5be18d4e8dcaebd6adff566 /root/btc-forensics/tz46-work--logs--91-host-gate-again.log
[2026-11-17T17:05:34Z] R copied 939fd8ead5f9ed10b116cb74b3f739d572a0b37da6c4c5a0d80acaf7c1cf81a9 /root/btc-forensics/tz46-work--logs--92-closing.log
[2026-11-17T17:05:34Z] R copied bde0c6f276a1f69acb8fbb36c343cd36d1cddd9f2f261342cf3786549ee3192e /root/btc-forensics/tz46-work--logs--99-selfcheck.log
[2026-11-17T17:05:34Z] R copied 7b0804285af6987340838bd59573897d013cf97edc5d4132cda7f3f9ba3e3824 /root/btc-forensics/tz46-work--stage--deploy--systemd--btc-rewardbook-archive.timer
[2026-11-17T17:05:34Z] R copied 363b269c462d14da1656feb7bad92fec43adb1593209131fe5ca6e5c9f6755f6 /root/btc-forensics/tz46-work--stage--research--tz46-capture-room.py
[2026-11-17T17:05:34Z] RECLAIM PASS: 35 files considered, 7 named by a report, 28 kept by name, 35 copied, 0 already held; the forensic store 2532 -> 2567 files
[2026-11-17T17:05:34Z] peak memory of this run: 30347264 bytes
[2026-11-17T17:05:34Z] opens refused: 0; reward book opens: 0; API requests 0, downloads 0, 0 bytes; files removed 0
exit=0
exit=0
exit=1
/root/btc-5m-twap       13f3143 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
2567
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10618736640
```

`RECLAIM PASS` came before the removals: 35 files copied by exclusive create and each hash verified, with the worktree `pristine` and so skipped. The removals: `git worktree remove` `exit=0`, `rm -rf` `exit=0`, and `test -e /root/tz46-work` `exit=1`. The worktrees left are the primary checkout and `/root/btc-recorder-svc`. The forensic store holds **2,567** files: 2,579 at TZ-45's close, less G-FORENSIC's 47, plus §9's 35, plus B-RECLAIM-SCRATCH's 0. Free space is 10,618,736,640. The branch `tz-46-capture-room` stays on `origin` and as a local ref. Two earlier directories were removed by B-RECLAIM-SCRATCH (§2.9). The live one, `95cf58d2…`, and this session's own were kept.

## 6. What could not be implemented as written

1. **`SYSTEM-MAP.md` was not read whole by the Executor** (contract §1 step 2). The file is 624,694 bytes, and the session's context cannot hold it. Its revision line, its §0 table and its anchors were read and asserted by `fingerprint` (64 rows). The parts the TZ cites were applied as the TZ quotes them. This is a departure from the contract's wording, named here.
2. **`gh pr create`.** §3.1 fixes it. The session's harness notes say GitHub actions go through its own tools. The TZ's command was used, through the host's `gh`, which is logged in as `seahomebatumi-ai`, and it opened PR #46. §10 C1 names this as `gh`'s credential.
3. **§0.0 was run twice.** It was first run in the session, before `/root/tz46-work` existed, as §0.0 orders. It was then run again into `00-ready.log` after the `mkdir`. Both read `ready=1`.
4. **The band wait and B-TIMER were one background command.** §3.7's 60-s `I band timer` loop into `60-band-timer.log` was chained directly to B-TIMER's paste, unchanged, so the block ran in the first second its band was open (16:05:48–49Z). The `first` loop of §3.8 was also a background command: it waited until E + 60 = 16:31:20Z and read at 16:31:29Z, then every 300 s.
5. **No classifier refusals.** Every block (B-RECLAIM-SCRATCH, B-FORENSICS, B-PAIR-OFF, B-TIMER, B-RECLAIM-OWN) ran in the session on the first try, and none was handed to the Boss. K-46T, B-RETRY and B-START-RB were not needed.
6. **An off-calendar run, as predicted.** The reward book's archive ran off its calendar at 15:15:47Z (run `1794928547`), 1,800 s after B-PAIR-OFF's reload. This is TZ-34's `OnActiveSec=1800`, which §3 foresaw. It ended at 15:21:45Z, before the band, and is reported in §2.7.
7. **Nothing else.**
