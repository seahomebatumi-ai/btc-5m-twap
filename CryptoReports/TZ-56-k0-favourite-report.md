# TZ-56 — K0: the favourite held to settlement, Kalshi and Polymarket — REPORT

**Status: BLOCKED at §3.5, G-REHEARSAL — 11 of 12 figures equal to the Architect's.** The one that differs is Polymarket's draws' label-free SHA-256 (`draws_digest`): `rehearse` printed `2beb4bb36415d1f8528b51eb366c3c2643d516a6657399a760d9dfcd0ac85eef`, where §4.1 has the Architect's `77444d74bc736a3519399f2ff9a250b4e6b18486a2a8f9465d924beb505f30a3`. §3.5 reads "any difference is BLOCKED". No frame, draw or label of the six days 2026-11-16 to 2026-11-21 was read: `frame` never ran, and no request of the set was made. Following §3, the run went to §3.13 and §9 and skipped every step that needs a PASS it lacks: §3.6 to §3.12. There is no Release `tz-56-k0-inputs`, no tag and no K0 reading.
- Executor model: Claude Opus 5.5, the model the TZ names.
- Branch `tz-56-k0-favourite` at `a8f6a8905a8d3a5c374ad33fc6ebad0d3cc56058`, pull request #54, open and not merged.
- The host: the capture host (H1, H2). The work tree `/root/tz56-work`, reclaimed by §9.

## 0. Fingerprint

`I0 fingerprint` (`logs/02-fingerprint.log`), contract §1 steps 3 and 4 asserted inside the instrument:

```
FINGERPRINT PASS: revision 2026-11-27-a; anchors 6 of 6, 4 re-derived; rows 74: frozen 71 of 71 equal, tracked 2, reported 1
```

Revision string read: `2026-11-27-a`. Anchors read from map §0, equal to the TZ header's six:

| anchor | map §0 | TZ header | re-derived |
|---|---|---|---|
| `A1` | `229a944f2d51` | `229a944f2d51` | — |
| `A2` | `6c5089330629` | `6c5089330629` | equal |
| `A3` | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` | — |
| `A4` | `6ac6e10aeabc` | `6ac6e10aeabc` | equal |
| `A5` | `0f6c90451cbd` | `0f6c90451cbd` | equal |
| `A6` | `729f0bcdbee3` | `729f0bcdbee3` | equal |

```
re-derived A2 research/twap-divergence.py sha256[:12] 6c5089330629 equal
re-derived A4 BTC-EXECUTOR-INSTRUCTIONS.md sha256[:12] 6ac6e10aeabc equal
re-derived A5 research/recorder/recorder.py sha256[:12] 0f6c90451cbd equal
re-derived A6 research/pfair.py sha256[:12] 729f0bcdbee3 equal
```

The map's §0 table, every row as `fingerprint` printed it, `wc -l`, bytes and `sha256sum` of the file in the primary checkout at `20e45f4`. There are 74 rows: 71 `frozen` equal, 2 `tracked`, 1 `reported`.

| path | lines | bytes | SHA-256 | state |
|---|---|---|---|---|
| `SYSTEM-MAP.md` | 1,110 | 211,418 | `b4becdf63ac1da212f422465e68be372a4df102da01f9805582b38ebb84b13ee` | reported |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 235 | 11,255 | `6ac6e10aeabc3bf83926c509e6d5f868998918f34e32e7e3882e95aad83e2617` | frozen equal |
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
| `research/tz45-l0-rule-w.py` | 4,299 | 233,655 | `4720e78573e54b1325dd24af7c30e0de59bfb4c1879d309a23fa6bab6b32d2d4` | frozen equal |
| `research/tz46-capture-room.py` | 1,644 | 88,254 | `363b269c462d14da1656feb7bad92fec43adb1593209131fe5ca6e5c9f6755f6` | frozen equal |
| `research/tz49-live-host.py` | 2,127 | 113,254 | `efcc5ead077b396fe18d243f3c65fa9824baca56e6db5312058971e0dfe6049b` | frozen equal |
| `research/tz53-l1-account.py` | 3,324 | 188,378 | `e4b72d0e285f1d8736a056012d3c9056f7f103e8e899742e10e488932c910c94` | frozen equal |
| `research/tz54-liq-guard.py` | 3,323 | 188,349 | `fd8f8c21d3dc5c36655a6948ce593a03d06ca8f783955ea7d18df5a57ea0e4bf` | frozen equal |
| `research/tz55-liq-guard-v2.py` | 3,323 | 188,383 | `1f7e9e8393ec3efda564a2ee0ff8356228f1ab2e435acad5f6f4729a9870bf35` | frozen equal |
| `docs/l1-sign.html` | 218 | 11,846 | `f1d92e7dd8a8cd15b7b96b86b357ebf80db4e10844b3fc269e92cef0aecba528` | frozen equal |
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
| `deploy/systemd/btc-rewardbook-archive.timer` | 12 | 435 | `7b0804285af6987340838bd59573897d013cf97edc5d4132cda7f3f9ba3e3824` | frozen equal |
| `deploy/systemd/adv3-bot.service` | 27 | 863 | `82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66` | frozen equal |
| `deploy/systemd/l1-bot.service` | 29 | 1,014 | `a6305d0e7a220ea88f5a4d2be612cac35f3dbe527d7c3b7ed12fd7c47f956266` | frozen equal |
| `engine/l1-bot.py` | 3,656 | 188,968 | `98851b3c0df447ed7c846edfbf18b9ea1611d12228a4d9a3c1fda3b4f22da214` | frozen equal |
| `deploy/systemd/liq-guard.service` | 30 | 1,086 | `11bff792d802cbf1abe9ee4f496c24517cce0e63a0dbf6aa49f277b7cdc55157` | frozen equal |
| `guard/liq-guard.py` | 2,772 | 148,628 | `6b851f3f93578dadcb683d33969b4d235daf2c852dbdce74c66e978946ec840a` | frozen equal |
| `advisor/RULE-ADV-3.txt` | 33 | 3,203 | `ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169` | frozen equal |
| `advisor/adv3.py` | 895 | 51,834 | `81ef0112d3fe4b86566e51a51aab924d9776ff37a927e65982ecb0bb7c1f34e1` | frozen equal |
| `advisor/adv3-bot.py` | 2,548 | 157,438 | `c3d9fff54f3585cfc4c33b5f7e1f93b390e62b03e0b4725fee2d6fdda6d04c11` | frozen equal |
| `advisor/selftest-adv3.py` | 256 | 19,111 | `6f29b82f2b2ca82cd2ff4bbb370e032354dbb4743497330530777429b3af7398` | frozen equal |
| `.gitignore` | 5 | 252 | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | tracked |

## 1. The blocker

§3.5's G-REHEARSAL compares twelve figures of 2026-11-12, six on each venue, with the Architect's independent implementation (§4.1). It must print `G-REHEARSAL PASS: 12 of 12`, and "any difference is BLOCKED". `I rehearse` ran from 20:18:39 to 20:21:21 UTC on 2026-11-27 and made 813 requests (Kalshi 355; gamma 288 and the Data API 170), none refused and none retried.

- **Kalshi:** 6 of 6 figures equal.
- **Polymarket:** 5 of 6 equal — rows `22,811`, groups `302`, draws `179`, the members' money before the fee `185183838496465774244150701/58500928021680144000000000`, and the other rows `outside 3,116`, `result 317`.
- **The sixth Polymarket figure differs:** `draws_digest` reads `2beb4bb3…5eef` against the Architect's `77444d74…30a3`.

So `mode_rehearse` asserted `BLOCKED: G-REHEARSAL 11 of 12` and exited `1`.

The digest is the SHA-256 over every draw considered, members and non-members alike. Each draw contributes one line of `digest_line` (Appendix A lines 1158 to 1164): `k|day|key|id|reason|n|na|nb|sa|sb|q`. That is the draw's index, its group, its market, its reason (`member` or `no_trade`) and its sums over the counted fills. The draw count, the draws' order and the members' money are all equal. So the two texts differ in a line's market, reason or sums, which the other five figures do not show. Which line differs is not read: no file under `rehearsal/` is printed (§2 item 10), and the TZ provides no step that compares one. The run stops here (contract §9; §6 "Each is BLOCKED where it stands").

## 2. The evidence

### 2.1 `I rehearse` — `logs/35-rehearse.log`, whole

```
Fri Nov 27 08:18:39 PM UTC 2026
[2026-11-27T20:18:39Z] read ledger: {"at": "2026-11-27T20:18:39Z", "at_ns": 1795810719921728462, "file_sha256": "1b94d50b613968df8ad9529e2c2af7d2a547d6177157367c22e1353cace1b524", "head": "a8f6a8905a8d3a5c374ad33fc6ebad0d3cc56058", "mode": "rehearse"}
[2026-11-27T20:18:39Z] MemAvailable 228384768 bytes, floor 136636736; free 10018377728 bytes, gate 8700000000
[2026-11-27T20:19:13Z] kalshi 2026-11-12T00:00:00Z: 103 pages, 102796 markets listed
[2026-11-27T20:19:13Z] rehearsal kalshi frame: 28563 rows in 517 groups; others {'outside': 10096, 'result': 735, 'volume': 63402}; 103 pages, 0 replayed, 103 new, 34 s
[2026-11-27T20:20:17Z] wrote /root/tz56-work/rehearsal/draws-kalshi.jsonl 29738 bytes sha256 3fdc9fe7f548beb1c7ec706c533c47ead8e581ffdc4a92965ba7ec4600561673
[2026-11-27T20:20:17Z] rehearsal kalshi draws: 103 considered, 60 members, 101 markets fetched; {'None': 60, 'no_trade': 43}; 252 requests, 0 replayed, 252 new, 64 s
[2026-11-27T20:20:17Z] rehearsal kalshi retries {}, requests {'api.elections.kalshi.com': 355}
[2026-11-27T20:20:17Z] rehearsal kalshi, recorded and compared with nothing: {}
[2026-11-27T20:20:17Z] G-REHEARSAL kalshi rows     28563, the Architect's 28563: equal
[2026-11-27T20:20:17Z] G-REHEARSAL kalshi keys     517, the Architect's 517: equal
[2026-11-27T20:20:17Z] G-REHEARSAL kalshi draws    103, the Architect's 103: equal
[2026-11-27T20:20:17Z] G-REHEARSAL kalshi digest   5b2a880d9c7f595f48cdfc2409b453005ee21b13ba66dca71253883e8bbe33c3, the Architect's 5b2a880d9c7f595f48cdfc2409b453005ee21b13ba66dca71253883e8bbe33c3: equal
[2026-11-27T20:20:17Z] G-REHEARSAL kalshi gross    628139564649870191653025003192713847/229113710652283845071852508980640000, the Architect's 628139564649870191653025003192713847/229113710652283845071852508980640000: equal
[2026-11-27T20:20:17Z] G-REHEARSAL kalshi reasons  {'outside': 10096, 'result': 735, 'volume': 63402}, the Architect's {'outside': 10096, 'result': 735, 'volume': 63402}: equal
[2026-11-27T20:20:17Z] rehearsal kalshi members 60, money before the fee 0.045693436304 a contract; fee coefficients' sha256 bdc75793cb9f9ae42ac92eb975a803082ed416fed480589d1a6e6b2027e36d1a (recorded)
[2026-11-27T20:20:52Z] polymarket 2026-11-12T00:00:00Z: 288 pages, 28777 markets listed
[2026-11-27T20:20:53Z] rehearsal polymarket frame: 22811 rows in 302 groups; others {'late': 1, 'outside': 3116, 'result': 317, 'version': 2532}; 288 pages, 0 replayed, 288 new, 35 s
[2026-11-27T20:21:20Z] wrote /root/tz56-work/rehearsal/draws-polymarket.jsonl 65838 bytes sha256 ffa9366c8641c68f61fd708d46a650d1a2b73eec915b7f979c341bc61ef75a7f
[2026-11-27T20:21:20Z] rehearsal polymarket draws: 179 considered, 60 members, 163 markets fetched; {'None': 60, 'no_trade': 119}; 170 requests, 0 replayed, 170 new, 28 s
[2026-11-27T20:21:20Z] rehearsal polymarket retries {}, requests {'gamma-api.polymarket.com': 288, 'data-api.polymarket.com': 170}
[2026-11-27T20:21:21Z] rehearsal polymarket, recorded and compared with nothing: {'late': 1, 'version': 2532}
[2026-11-27T20:21:21Z] G-REHEARSAL polymarket rows     22811, the Architect's 22811: equal
[2026-11-27T20:21:21Z] G-REHEARSAL polymarket keys     302, the Architect's 302: equal
[2026-11-27T20:21:21Z] G-REHEARSAL polymarket draws    179, the Architect's 179: equal
[2026-11-27T20:21:21Z] G-REHEARSAL polymarket digest   2beb4bb36415d1f8528b51eb366c3c2643d516a6657399a760d9dfcd0ac85eef, the Architect's 77444d74bc736a3519399f2ff9a250b4e6b18486a2a8f9465d924beb505f30a3: DIFFERENT
[2026-11-27T20:21:21Z] G-REHEARSAL polymarket gross    185183838496465774244150701/58500928021680144000000000, the Architect's 185183838496465774244150701/58500928021680144000000000: equal
[2026-11-27T20:21:21Z] G-REHEARSAL polymarket reasons  {'outside': 3116, 'result': 317}, the Architect's {'outside': 3116, 'result': 317}: equal
[2026-11-27T20:21:21Z] rehearsal polymarket members 60, money before the fee 0.052758091412 a contract; fee coefficients' sha256 df4f7bcc269442f80715338b9e57e669696772d59bc6a23be4eb5999a87b97fa (recorded)
[2026-11-27T20:21:21Z] malloc tuned: True
[2026-11-27T20:21:21Z] peak memory of this run: 54476800 bytes
[2026-11-27T20:21:21Z] opens, requests and processes refused: 0
Traceback (most recent call last):
  File "/root/tz56-work/wt/research/tz56-k0-favourite.py", line 2237, in <module>
    main(sys.argv[1:])
  File "/root/tz56-work/wt/research/tz56-k0-favourite.py", line 1852, in main
    table[mode]()
  File "/root/tz56-work/wt/research/tz56-k0-favourite.py", line 1495, in mode_rehearse
    assert passes == total, "BLOCKED: G-REHEARSAL %d of %d" % (passes, total)
           ^^^^^^^^^^^^^^^
AssertionError: BLOCKED: G-REHEARSAL 11 of 12
exit=1
```

The background task that ran it reported exit code `0`, because the command ended with `echo "exit=$?"`. The instrument's own status is the log's `exit=1`.

### 2.2 The rehearsal's files, by SHA-256 — `logs/9-evidence-hashes.log`, whole

These are the kept replies, frames and draws the twelve figures were computed from. They are named here by hash, so `reclaim` copies each into `/root/btc-forensics/` (§9; CANON hard rule 15). That way the Polymarket draw text can be rebuilt from its kept replies and set beside the Architect's, line by line. Each file was read with `sha256sum` and `stat` alone; none is printed.

```
Fri Nov 27 08:21:58 PM UTC 2026
3fdc9fe7f548beb1c7ec706c533c47ead8e581ffdc4a92965ba7ec4600561673 29738 rehearsal/draws-kalshi.jsonl
ffa9366c8641c68f61fd708d46a650d1a2b73eec915b7f979c341bc61ef75a7f 65838 rehearsal/draws-polymarket.jsonl
83de241cfea6aeff53b8341c9d6e2668d48efae5640b8557f46474afe5b931bb 4442378 rehearsal/frame-kalshi.jsonl
c22fb7d561851e76cd9720e7ecf611e61fb8426078a057a6ecce864fcd66a433 8465021 rehearsal/frame-polymarket.jsonl
dab24eeea64510d67558c5d82236934266232478328428330e3328d26eb5f406 2079827 rehearsal/raw-draw-kalshi.jsonl.gz
f5e312b22a714982e545cc944d5774c6d7f65c8184cdb48687b18cedd5f57cde 1817 rehearsal/raw-draw-kalshi.jsonl.gz.idx
3fd4630cd5497218ff1072ac5e9b83f69caf64ae0868ad72c10973a3f84b7b75 1671307 rehearsal/raw-draw-polymarket.jsonl.gz
659745acebe3fcb0110d78bfa88f82978eabad4a6f07e8a3c07e2b0ce966d41c 1271 rehearsal/raw-draw-polymarket.jsonl.gz.idx
a586e51e260b19eb37be6bc71eba67aea46878b5a4d1848d9c75c496b1453373 6151548 rehearsal/raw-frame-kalshi.jsonl.gz
199376f8b5316c6aaa88991c95951d7627078565af90e3be4eb1c1aadf8e6ca3 804 rehearsal/raw-frame-kalshi.jsonl.gz.idx
343d45b2707cecf24d3f3cf2dc66ca14b5cd26ef15cd41e39839b0a10e4ee291 14472988 rehearsal/raw-frame-polymarket.jsonl.gz
63c3a54f551c83f1b9629ef4b9f451627016b24a31a53335d74b291150f0b4bc 2371 rehearsal/raw-frame-polymarket.jsonl.gz.idx
total 32
drwxr-xr-x  6 root root 4096 Nov 27 20:18 .
drwx------ 32 root root 4096 Nov 27 20:17 ..
drwxr-xr-x  2 root root 4096 Nov 27 20:21 logs
-rw-r--r--  1 root root  216 Nov 27 20:18 read-ledger.jsonl
drwxr-xr-x  2 root root 4096 Nov 27 20:21 rehearsal
drwxr-xr-x  3 root root 4096 Nov 27 20:17 stage
-rw-r--r--  1 root root  621 Nov 27 20:18 state.json
drwxr-xr-x 10 root root 4096 Nov 27 20:17 wt
```

### 2.3 What passed before it

#### §0.0 — `logs/00-worktree.log`

```
Fri Nov 27 08:17:12 PM UTC 2026
mkdir /root/tz56-work /root/tz56-work/logs; echo "exit=$?"
exit=0
```

#### §0.1 — `logs/01-stage.log`

```
Fri Nov 27 08:17:12 PM UTC 2026
/root/tz56-work/stage/research/tz56-k0-favourite.py 2237 114644 1b94d50b613968df8ad9529e2c2af7d2a547d6177157367c22e1353cace1b524
exit=0
```

#### §0.3 — `logs/03-host-gate.log`

```
Fri Nov 27 08:17:25 PM UTC 2026
1795810645
1
MemTotal:         978640 kB
MemAvailable:     223716 kB
SwapTotal:       3174396 kB
SwapFree:        2699224 kB
2026-08-02 07:24:32
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10039721984
/var/lib/btc-recorder/btc-updown-5m/1794396600/manifest.json
5
3.12.3
MainPID=3525462
NRestarts=0
Id=btc-recorder.service
ActiveState=active
UnitFileState=enabled
ActiveEnterTimestamp=Fri 2026-11-27 06:26:20 UTC

MainPID=3525511
NRestarts=0
Id=btc-rewardbook.service
ActiveState=active
UnitFileState=enabled
ActiveEnterTimestamp=Fri 2026-11-27 06:26:22 UTC

MainPID=0
NRestarts=0
Id=btc-rewardbook-archive.service
ActiveState=inactive
UnitFileState=static
ActiveEnterTimestamp=

Id=btc-rewardbook-archive.timer
ActiveState=active
UnitFileState=enabled
ActiveEnterTimestamp=Tue 2026-11-17 16:05:49 UTC

MainPID=3525469
NRestarts=0
Id=adv3-bot.service
ActiveState=active
UnitFileState=enabled
ActiveEnterTimestamp=Fri 2026-11-27 06:26:20 UTC

MainPID=3525503
NRestarts=0
Id=liq-guard.service
ActiveState=active
UnitFileState=enabled
ActiveEnterTimestamp=Fri 2026-11-27 06:26:22 UTC
disabled
exit=1
514962891	/var/lib/btc-rewardbook
359692015	/root/btc-forensics
2841
1
/root/btc-5m-twap       20e45f4 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/tmp/claude-0/-root-btc-5m-twap/f05cea76-0be2-5057-94c5-39713a008e6e/scratchpad
total 64
drwx------ 16 root root 4096 Nov 27 20:16 .
drwx------ 48 root root 4096 Nov 27 20:16 ..
drwx------  3 root root 4096 Nov 20 18:51 0736470b-13a0-4e8d-931f-5ecf4df19205
drwx------  3 root root 4096 Nov 25 22:46 14b0bf22-9b3d-5114-ae1e-88801e8819ce
drwx------  3 root root 4096 Nov 27 19:47 2d86e605-226e-4543-82c4-0e68f00eb851
drwx------  3 root root 4096 Nov 27 19:23 54158118-b10a-4d9c-a8c6-8f105e70d6f3
drwx------  3 root root 4096 Nov 22 09:18 6c04aed0-6057-4e03-a1b5-56678f8a595f
drwx------  3 root root 4096 Nov 20 18:51 6f0f41a7-6da7-5e8a-80e1-a2a85a4a8e5c
drwx------  3 root root 4096 Nov 25 22:46 7123abac-62f9-42cc-9fa9-5198a10b37c2
drwx------  3 root root 4096 Nov 27 19:41 860e27fb-81a3-4d7c-b748-b9d5ae1cc5c8
drwx------  3 root root 4096 Nov 27 19:43 96027802-bb60-4eac-b19f-046e75ba8949
drwx------  3 root root 4096 Nov 27 19:33 b6258107-0dab-42e0-98d3-e94730b41617
drwx------  4 root root 4096 Nov 22 09:18 d8d0feb2-4f8e-5084-a026-9e20a0303c89
drwx------  3 root root 4096 Nov 27 19:41 edfd5742-e105-564d-b1bc-16a84a7355a9
drwx------  4 root root 4096 Nov 27 20:16 f05cea76-0be2-5057-94c5-39713a008e6e
drwx------  3 root root 4096 Nov 27 20:16 f22e0a97-2a88-44f5-8f8b-da5078b1ee7d
```

H1: one `manifest.json` path. H2: `/dev/vda2`, `31612203008`, and `grep -c` `5`. H3: `3.12.3`. H4: `1` login. **Memory gate:** `MemAvailable` `223,716 kB` = `229,085,184` bytes, at or above `136,636,736`. **Disk gate:** `avail` `10,039,721,984` bytes, at or above `8,700,000,000`. All six pass. `telemetry-watch.service` reads `disabled`, exit `1`. The reward book's store is `514,962,891` bytes and the forensic store `359,692,015` bytes in `2,841` files.

**The margin** is `10,039,721,984` + `514,962,891` − `7,300,000,000` − `445,535,636` = **`2,809,149,239`** bytes. It takes `du -sb` of the reward book's whole store in place of its stream files alone (§3 item 3). Worktrees: the primary checkout and `/root/btc-recorder-svc`. The units entered `active` at 06:26:20 to 06:26:22 UTC on 2026-11-27, `NRestarts` `0`, a start before this run that this run did not read.

#### §0.2 — `logs/02-fingerprint.log`

Its 74 row lines are §0's table. Its pass line and `exit=0` are:

```
[2026-11-27T20:17:19Z] FINGERPRINT PASS: revision 2026-11-27-a; anchors 6 of 6, 4 re-derived; rows 74: frozen 71 of 71 equal, tracked 2, reported 1
[2026-11-27T20:17:19Z] malloc tuned: True
[2026-11-27T20:17:19Z] peak memory of this run: 29573120 bytes
[2026-11-27T20:17:19Z] opens, requests and processes refused: 0
exit=0
```

#### §0.5 — `logs/05-number.log`

```
Fri Nov 27 08:17:33 PM UTC 2026
[2026-11-27T20:17:34Z] origin/main 20e45f40b0c33cc7ecad805a6044055adf06fb4f: 131 paths under CryptoTZ/ and CryptoReports/; of the number TZ-56-: ['CryptoTZ/TZ-56-k0-favourite.md'] and []
[2026-11-27T20:17:34Z] NUMBER PASS - 2 of 2
[2026-11-27T20:17:34Z] malloc tuned: True
[2026-11-27T20:17:34Z] peak memory of this run: 28459008 bytes
[2026-11-27T20:17:34Z] opens, requests and processes refused: 0
exit=0
```

#### §0.5 — `logs/05-refs.log`

```
Fri Nov 27 08:17:34 PM UTC 2026
exit=0
lines: 262
    114 refs/tags/rewardbook-
     59 refs/tags/pairbook-
     52 refs/pull/N/head
      2 refs/tags/tz-27
      2 refs/tags/tz-01
      1 refs/tags/tz-45
      1 refs/tags/tz-44
      1 refs/heads/tz-55
      1 refs/heads/tz-54
      1 refs/heads/tz-53
      1 refs/heads/tz-52
      1 refs/heads/tz-51
      1 refs/heads/tz-50
      1 refs/heads/tz-49
      1 refs/heads/tz-46
      1 refs/heads/tz-45
      1 refs/heads/tz-44
      1 refs/heads/tz-43
      1 refs/heads/tz-42
      1 refs/heads/tz-40
      1 refs/heads/tz-39
      1 refs/heads/tz-38
      1 refs/heads/tz-37
      1 refs/heads/tz-36
      1 refs/heads/tz-35
      1 refs/heads/tz-34
      1 refs/heads/tz-33
      1 refs/heads/tz-32
      1 refs/heads/tz-31
      1 refs/heads/tz-30
ref lines: 262
  HEAD: 1
  refs/heads/*: 30
  refs/pull/N/head: 52
  refs/tags/other: 6
  refs/tags/pairbook-streams-*: 59
  refs/tags/rewardbook-streams-*: 114
lines that differ from map §1's read of 2026-11-22 (219 lines):
   20e45f40b0c33cc7ecad805a6044055adf06fb4f HEAD
   20e45f40b0c33cc7ecad805a6044055adf06fb4f refs/heads/main
   rewardbook-streams-* tags after 1795332620: 44, 1795343420 ... 1795807820, each lightweight at {'6a615257277d3c94dafd4d39783499560a344648'}
  refs/heads/tz-56-k0-favourite present: False
  refs/tags/tz-56-k0-inputs present: False
  heads: ['main', 'tz-23-maker-m0', 'tz-24-nesting-b2', 'tz-26-nesting-b3-capture', 'tz-27-pairbook-archive', 'tz-28-pairbook-archive-timer', 'tz-29-maker-m0-second-look', 'tz-30-nesting-b3-measure', 'tz-31-who-earns', 'tz-32-our-quoting', 'tz-33-reward-book-capture', 'tz-34-rewardbook-archive-timer', 'tz-35-advisor-bot', 'tz-36-advisor-trust-block', 'tz-37-capital-allocation', 'tz-38-adv3-pit-validation', 'tz-39-advisor-checks', 'tz-40-strong-every-rank', 'tz-42-advisor-registry', 'tz-43-l0-our-quote', 'tz-44-l0-inputs-release', 'tz-45-l0-rule-w', 'tz-46-capture-room', 'tz-49-live-host-ipv4-keys', 'tz-50-l1-account-round-trip', 'tz-51-l1-account-round-trip-rerun', 'tz-52-l1-round-trip', 'tz-53-l1-unit', 'tz-54-liq-guard', 'tz-55-liq-guard-v2']
  pull heads: 52 max 53
```

`logs/05-refs.log` holds the raw read's line count and then two counts by prefix:

- The first was bucketed wrongly by a `sed`; I replaced it (§3 item 4).
- The second is the Executor's `python3` count.

`origin` read 262 lines against map §1's 219:

- `refs/pull/53/merge` is gone, since PR #53 is merged.
- `HEAD` and `main` are at `20e45f4`.
- There are 44 more `rewardbook-streams-*` tags, `1795343420` … `1795807820`, each at `6a61525…`.

Neither `refs/heads/tz-56-k0-favourite` nor `refs/tags/tz-56-k0-inputs` existed, and `main` carries revision `2026-11-27-a`. The raw read is `logs/05-refs-raw.txt`, kept by name and not quoted.

#### §3.1 — `logs/31-branch.log`

```
Fri Nov 27 08:17:51 PM UTC 2026
exit=0
Preparing worktree (new branch 'tz-56-k0-favourite')
branch 'tz-56-k0-favourite' set up to track 'origin/main'.
HEAD is now at 20e45f4 Add files via upload
exit=0
exit=0
1b94d50b613968df8ad9529e2c2af7d2a547d6177157367c22e1353cace1b524  /root/tz56-work/wt/research/tz56-k0-favourite.py
exit=0
[tz-56-k0-favourite a8f6a89] TZ-56: K0's instrument - research/tz56-k0-favourite.py
 Committer: root <root@vultr.guest>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 2237 insertions(+)
 create mode 100644 research/tz56-k0-favourite.py
exit=0
remote: 
remote: Create a pull request for 'tz-56-k0-favourite' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-56-k0-favourite        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-56-k0-favourite -> tz-56-k0-favourite
branch 'tz-56-k0-favourite' set up to track 'origin/tz-56-k0-favourite'.
exit=0
a8f6a8905a8d3a5c374ad33fc6ebad0d3cc56058	refs/heads/tz-56-k0-favourite
a8f6a8905a8d3a5c374ad33fc6ebad0d3cc56058
Fri Nov 27 08:17:54 PM UTC 2026
```

#### §3.1 — `logs/31-pr.log`

```
Fri Nov 27 08:18:00 PM UTC 2026
https://github.com/seahomebatumi-ai/btc-5m-twap/pull/54
exit=0
```

#### §3.2 — `logs/32-selftest.log`

```
Fri Nov 27 08:18:05 PM UTC 2026
[2026-11-27T20:18:05Z] /root/tz56-work/selftest/s.jsonl.gz: a reply cut short at 342 bytes cut off
[2026-11-27T20:18:05Z] kalshi 2026-10-28T00:00:00Z: 2 pages, 10 markets listed
[2026-11-27T20:18:05Z] kalshi 2026-10-29T00:00:00Z: 1 pages, 3 markets listed
[2026-11-27T20:18:05Z] wrote /root/tz56-work/selftest/kalshi/draws.jsonl 3575 bytes sha256 c064fe4b075651b9d104107bd76d238fb7608ee966b24171e7e3a8b2fcf01fc7
[2026-11-27T20:18:05Z] kalshi 2026-10-28T00:00:00Z: 2 pages, 10 markets listed
[2026-11-27T20:18:05Z] kalshi 2026-10-29T00:00:00Z: 1 pages, 3 markets listed
[2026-11-27T20:18:05Z] wrote /root/tz56-work/selftest/kalshi/draws-again.jsonl 3575 bytes sha256 c064fe4b075651b9d104107bd76d238fb7608ee966b24171e7e3a8b2fcf01fc7
[2026-11-27T20:18:05Z] polymarket 2026-10-28T00:00:00Z: 2 pages, 11 markets listed
[2026-11-27T20:18:05Z] polymarket 2026-10-29T00:00:00Z: 1 pages, 1 markets listed
[2026-11-27T20:18:05Z] wrote /root/tz56-work/selftest/polymarket/draws.jsonl 2196 bytes sha256 e0c6443703841058abb77f5272769cc831769ef4dc650a1bf096e6370fbfe8ba
[2026-11-27T20:18:05Z] polymarket 2026-10-28T00:00:00Z: 2 pages, 11 markets listed
[2026-11-27T20:18:05Z] polymarket 2026-10-29T00:00:00Z: 1 pages, 1 markets listed
[2026-11-27T20:18:05Z] wrote /root/tz56-work/selftest/polymarket/draws-again.jsonl 2196 bytes sha256 e0c6443703841058abb77f5272769cc831769ef4dc650a1bf096e6370fbfe8ba
[2026-11-27T20:18:06Z] wrote /root/tz56-work/selftest/g.bin.gz 1879160 bytes sha256 7375869fd6ef83a4d3f8191239fb19290f84fefc02a66058e7c7b2e3a862692c
[2026-11-27T20:18:06Z] unchanged /root/tz56-work/selftest/g.bin.gz 1879160 bytes sha256 7375869fd6ef83a4d3f8191239fb19290f84fefc02a66058e7c7b2e3a862692c
[2026-11-27T20:18:06Z] SELFTEST PASS: 65 of 65 checks
[2026-11-27T20:18:06Z] malloc tuned: True
[2026-11-27T20:18:06Z] peak memory of this run: 39968768 bytes
[2026-11-27T20:18:06Z] opens, requests and processes refused: 0
exit=0
```

#### §3.3 — `logs/33-still.log`

```
Fri Nov 27 08:18:10 PM UTC 2026
[2026-11-27T20:18:10Z] btc-recorder.service {'MainPID': '3525462', 'NRestarts': '0', 'ActiveState': 'active'} enabled
[2026-11-27T20:18:10Z] btc-rewardbook.service {'MainPID': '3525511', 'NRestarts': '0', 'ActiveState': 'active'} enabled
[2026-11-27T20:18:10Z] btc-rewardbook-archive.timer {'MainPID': None, 'NRestarts': None, 'ActiveState': 'active'} enabled
[2026-11-27T20:18:10Z] adv3-bot.service {'MainPID': '3525469', 'NRestarts': '0', 'ActiveState': 'active'} enabled
[2026-11-27T20:18:10Z] liq-guard.service {'MainPID': '3525503', 'NRestarts': '0', 'ActiveState': 'active'} enabled
[2026-11-27T20:18:10Z] still: recorded
[2026-11-27T20:18:10Z] malloc tuned: True
[2026-11-27T20:18:10Z] peak memory of this run: 28450816 bytes
[2026-11-27T20:18:10Z] opens, requests and processes refused: 0
exit=0
```

#### §3.3 — `logs/33-scratch.log`

```
Fri Nov 27 08:18:10 PM UTC 2026
[2026-11-27T20:18:10Z] running 3609544 started 2026-11-27T19:47:09Z claude
[2026-11-27T20:18:10Z] running 3609554 started 2026-11-27T19:47:11Z claude
[2026-11-27T20:18:10Z] running 3609563 started 2026-11-27T19:47:12Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-27T20:18:10Z] running 3609585 started 2026-11-27T19:47:14Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-27T20:18:10Z] running 3612254 started 2026-11-27T20:16:25Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-27T20:18:10Z] malloc tuned: True
[2026-11-27T20:18:10Z] peak memory of this run: 28459008 bytes
[2026-11-27T20:18:10Z] opens, requests and processes refused: 0
exit=0
```

#### §3.4 — `logs/34-probe.log`

```
Fri Nov 27 08:18:35 PM UTC 2026
[2026-11-27T20:18:35Z] MemAvailable 233091072 bytes, floor 136636736; free 10018455552 bytes, gate 8700000000
[2026-11-27T20:18:35Z] headers of every venue request: {"Accept": "application/json", "Accept-Encoding": "gzip", "User-Agent": "btc-5m-twap-tz56"}
[2026-11-27T20:18:35Z] kalshi exchange    GET https://api.elections.kalshi.com/trade-api/v2/exchange/status -> 200, 667 bytes, sha256 9c900e19dad1f05812a0c3c40c19253e5962c839b1739481aef3d20244c4f778, keys ['exchange_active', 'exchange_index_statuses', 'intra_exchange_transfers_active', 'trading_active']
[2026-11-27T20:18:35Z] kalshi cutoff      GET https://api.elections.kalshi.com/trade-api/v2/historical/cutoff -> 200, 188 bytes, sha256 61d3453d5919a44413b09d8739f4392372109d122232086cde0cf027799e25f2, keys ['market_positions_last_updated_ts', 'market_settled_ts', 'orders_updated_ts', 'trades_created_ts']
[2026-11-27T20:18:35Z] kalshi historical cutoff: {"market_positions_last_updated_ts": "2026-09-28T00:00:00Z", "market_settled_ts": "2026-09-28T00:00:00Z", "orders_updated_ts": "2026-11-13T00:00:00Z", "trades_created_ts": "2026-09-28T00:00:00Z"}
[2026-11-27T20:18:36Z] kalshi markets     GET https://api.elections.kalshi.com/trade-api/v2/markets?limit=1000&min_close_ts=1794438000&max_close_ts=1794531600&mve_filter=exclude -> 200, 1997939 bytes, sha256 7d6a4445fe867089c185bc1601f61fe8cdecf18858a814443524a2cf866d955e, keys ['cursor', 'markets']
[2026-11-27T20:18:36Z] kalshi trades      GET https://api.elections.kalshi.com/trade-api/v2/markets/trades?ticker=KXZEC15M-26NOV121900-00&limit=5 -> 200, 1565 bytes, sha256 f45adfe989b20d0267f4e3fd7a1e547ba1d6c132fd519833f61ca99915ad1bb4, keys ['cursor', 'trades']
[2026-11-27T20:18:36Z] kalshi series      GET https://api.elections.kalshi.com/trade-api/v2/series/KXBTCD -> 200, 1178 bytes, sha256 ab961b0bbf53c0223b3ff240f0df1a046057781417ddaa7d42f8c874ec5ba61c, keys ['series']
[2026-11-27T20:18:36Z] kalshi series fees GET https://api.elections.kalshi.com/trade-api/v2/series/fee_changes?show_historical=true -> 200, 17840 bytes, sha256 c13cb76fbcfcfcb14ae6d43c7e8841e89404062b22fc1c2f09b6bab300c8c598, keys ['series_fee_change_arr']
[2026-11-27T20:18:36Z] kalshi event fees  GET https://api.elections.kalshi.com/trade-api/v2/events/fee_changes?limit=1000 -> 200, 36 bytes, sha256 4d755a11d76cd85bec7a4758a2d226815fd2a935a5563dbafae35ee9d373da45, keys ['cursor', 'event_fee_changes']
[2026-11-27T20:18:37Z] gamma keyset       GET https://gamma-api.polymarket.com/markets/keyset?limit=100&closed=true&end_date_min=2026-11-11T23%3A00%3A00Z&end_date_max=2026-11-13T01%3A00%3A00Z -> 200, 597484 bytes, sha256 f55c12fdb9346715bbb6c629b6cd295466474fe4ff5b1ec0e0466ba6c19c88b4, keys ['markets', 'next_cursor']
[2026-11-27T20:18:37Z] data trades        GET https://data-api.polymarket.com/v2/trades?condition=0xbdc863ac40456c9cddb58e02610d985bfd08401b0d9a622ede786ed7a085e5bf&taker_only=true&limit=5 -> 200, 4124 bytes, sha256 da2eb14deb7d6afd8fb9f38f75c07b96aa1042baf03bc14da0fd1050e594a818, keys ['data', 'pagination']
[2026-11-27T20:18:37Z] retries {}
[2026-11-27T20:18:37Z] G-PROBE PASS: 9 of 9 endpoints served and parsed
[2026-11-27T20:18:37Z] malloc tuned: True
[2026-11-27T20:18:37Z] peak memory of this run: 41811968 bytes
[2026-11-27T20:18:37Z] opens, requests and processes refused: 0
exit=0
```

The instrument's commit `a8f6a89` reached `origin` at 20:17:54 UTC. `rehearse` was the first run after it, at 20:18:39 (map §7 item 63; the read ledger's one line names that head and the file's SHA-256). No label of the set was read, and `score` never ran.

### 2.4 After the BLOCK — §3.13 and §9

#### §3.13 — `logs/313-still.log`, G-STILL

```
Fri Nov 27 08:21:45 PM UTC 2026
[2026-11-27T20:21:45Z] btc-recorder.service {'MainPID': '3525462', 'NRestarts': '0', 'ActiveState': 'active'} enabled
[2026-11-27T20:21:45Z] btc-rewardbook.service {'MainPID': '3525511', 'NRestarts': '0', 'ActiveState': 'active'} enabled
[2026-11-27T20:21:45Z] btc-rewardbook-archive.timer {'MainPID': None, 'NRestarts': None, 'ActiveState': 'active'} enabled
[2026-11-27T20:21:45Z] adv3-bot.service {'MainPID': '3525469', 'NRestarts': '0', 'ActiveState': 'active'} enabled
[2026-11-27T20:21:45Z] liq-guard.service {'MainPID': '3525503', 'NRestarts': '0', 'ActiveState': 'active'} enabled
[2026-11-27T20:21:45Z] G-STILL PASS: unchanged since 2026-11-27T20:18:10Z
[2026-11-27T20:21:45Z] malloc tuned: True
[2026-11-27T20:21:45Z] peak memory of this run: 28057600 bytes
[2026-11-27T20:21:45Z] opens, requests and processes refused: 0
exit=0
```

#### §3.13 — `logs/313-host.log`

```
Fri Nov 27 08:21:53 PM UTC 2026
1795810913
1
MemTotal:         978640 kB
MemAvailable:     240836 kB
SwapTotal:       3174396 kB
SwapFree:        2604336 kB
2026-08-02 07:24:32
Filesystem       1B-blocks      Avail
/dev/vda2      31612203008 9978671104
/var/lib/btc-recorder/btc-updown-5m/1794396600/manifest.json
5
3.12.3
MainPID=3525462
NRestarts=0
Id=btc-recorder.service
ActiveState=active
UnitFileState=enabled
ActiveEnterTimestamp=Fri 2026-11-27 06:26:20 UTC

MainPID=3525511
NRestarts=0
Id=btc-rewardbook.service
ActiveState=active
UnitFileState=enabled
ActiveEnterTimestamp=Fri 2026-11-27 06:26:22 UTC

MainPID=0
NRestarts=0
Id=btc-rewardbook-archive.service
ActiveState=inactive
UnitFileState=static
ActiveEnterTimestamp=

Id=btc-rewardbook-archive.timer
ActiveState=active
UnitFileState=enabled
ActiveEnterTimestamp=Tue 2026-11-17 16:05:49 UTC

MainPID=3525469
NRestarts=0
Id=adv3-bot.service
ActiveState=active
UnitFileState=enabled
ActiveEnterTimestamp=Fri 2026-11-27 06:26:20 UTC

MainPID=3525503
NRestarts=0
Id=liq-guard.service
ActiveState=active
UnitFileState=enabled
ActiveEnterTimestamp=Fri 2026-11-27 06:26:22 UTC
disabled
exit=1
517892665	/var/lib/btc-rewardbook
359692015	/root/btc-forensics
2841
1
/root/btc-5m-twap       20e45f4 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/root/tz56-work/wt      a8f6a89 [tz-56-k0-favourite]
/tmp/claude-0/-root-btc-5m-twap/f05cea76-0be2-5057-94c5-39713a008e6e/scratchpad
total 64
drwx------ 16 root root 4096 Nov 27 20:16 .
drwx------ 48 root root 4096 Nov 27 20:16 ..
drwx------  3 root root 4096 Nov 20 18:51 0736470b-13a0-4e8d-931f-5ecf4df19205
drwx------  3 root root 4096 Nov 25 22:46 14b0bf22-9b3d-5114-ae1e-88801e8819ce
drwx------  3 root root 4096 Nov 27 19:47 2d86e605-226e-4543-82c4-0e68f00eb851
drwx------  3 root root 4096 Nov 27 19:23 54158118-b10a-4d9c-a8c6-8f105e70d6f3
drwx------  3 root root 4096 Nov 22 09:18 6c04aed0-6057-4e03-a1b5-56678f8a595f
drwx------  3 root root 4096 Nov 20 18:51 6f0f41a7-6da7-5e8a-80e1-a2a85a4a8e5c
drwx------  3 root root 4096 Nov 25 22:46 7123abac-62f9-42cc-9fa9-5198a10b37c2
drwx------  3 root root 4096 Nov 27 19:41 860e27fb-81a3-4d7c-b748-b9d5ae1cc5c8
drwx------  3 root root 4096 Nov 27 19:43 96027802-bb60-4eac-b19f-046e75ba8949
drwx------  3 root root 4096 Nov 27 19:33 b6258107-0dab-42e0-98d3-e94730b41617
drwx------  4 root root 4096 Nov 22 09:18 d8d0feb2-4f8e-5084-a026-9e20a0303c89
drwx------  3 root root 4096 Nov 27 19:41 edfd5742-e105-564d-b1bc-16a84a7355a9
drwx------  4 root root 4096 Nov 27 20:16 f05cea76-0be2-5057-94c5-39713a008e6e
drwx------  3 root root 4096 Nov 27 20:16 f22e0a97-2a88-44f5-8f8b-da5078b1ee7d
```

#### §3.13 — `logs/313-refs.log`

```
Fri Nov 27 08:21:54 PM UTC 2026
exit=0
ref lines: 265
  added since §0.5: 7058afef250471c5911f0d6f2512fa487ec081f1 refs/pull/54/merge
  added since §0.5: a8f6a8905a8d3a5c374ad33fc6ebad0d3cc56058 refs/heads/tz-56-k0-favourite
  added since §0.5: a8f6a8905a8d3a5c374ad33fc6ebad0d3cc56058 refs/pull/54/head
```

**G-STILL PASS:** the five units are unchanged from §3.3 to §3.13. Free space at the closing read was `9,978,671,104` bytes and `MemAvailable` `240,836 kB`. The refs added since §0.5 are this run's branch and pull request #54.

#### §9 step 2 — `logs/9-reclaim.log`, whole, unfiltered

```
Fri Nov 27 08:23:28 PM UTC 2026
[2026-11-27T20:23:29Z] reclaim: 4543 report tokens; forensic store holds 2841 files; the Release tz-56-k0-inputs proved 0 assets
[2026-11-27T20:23:29Z] reclaim: /root/tz56-work/wt skipped: no file but its HEAD's, and HEAD a8f6a8905a8d3a5c374ad33fc6ebad0d3cc56058 is its upstream's
[2026-11-27T20:23:29Z] R copied ab388200704c824a7065f1968cc78ab47ed20910ee4baa382215e512768f2c93 /root/btc-forensics/tz56-work--read-ledger.jsonl
[2026-11-27T20:23:29Z] R copied 5989b6e5a1c06061d3f054eac1d903895e413992f9b4cf7906611b2e9e942926 /root/btc-forensics/tz56-work--state.json
[2026-11-27T20:23:29Z] R copied 5d7bfc749b98c8d600eb1e357901f9fec08c0eb08348c70ccfb4f103b049c2eb /root/btc-forensics/tz56-work--logs--00-worktree.log
[2026-11-27T20:23:29Z] R copied 171864599f8ea4db1e553457778653acf877bb4cfbf5277b86cbeb4e6e462113 /root/btc-forensics/tz56-work--logs--01-stage.log
[2026-11-27T20:23:29Z] R copied e1045fc884b372f53e748ac208d9204c7eb8cab7d0e06637438fb7befb70829e /root/btc-forensics/tz56-work--logs--02-fingerprint.log
[2026-11-27T20:23:29Z] R copied f2792c03f84615f2a312692cbe4f5606f7a81da1f05b95084c42439fe9e56ae8 /root/btc-forensics/tz56-work--logs--03-host-gate.log
[2026-11-27T20:23:29Z] R copied 7005b65ff5c7ad08cebcd7dece209719e746076a90c07ab60fb5d204308f4c53 /root/btc-forensics/tz56-work--logs--05-number.log
[2026-11-27T20:23:29Z] R copied b3ed65cc61ddc503f71567615102e486fab543635331ae18221a91da280718c0 /root/btc-forensics/tz56-work--logs--05-refs-raw.txt
[2026-11-27T20:23:29Z] R copied ebd1848af1cfc46b9ff106a459e1edb4d6b9238ad9ea387f603247bcc3b49c97 /root/btc-forensics/tz56-work--logs--05-refs.log
[2026-11-27T20:23:29Z] R copied bda2b1c5ad732937c6c47583ac2631619f05f1681f582ef04b387dff61a6767c /root/btc-forensics/tz56-work--logs--31-branch.log
[2026-11-27T20:23:29Z] R copied 0496ba9568948bbff3447f9b71625018d55d612b3b0714dc1c752e1fb6cb24f3 /root/btc-forensics/tz56-work--logs--31-pr.log
[2026-11-27T20:23:29Z] R copied 3055fbd4b6d90d907df57ccc6e4f2a5c31fe348d04d1f5bb42987e67e5ebb454 /root/btc-forensics/tz56-work--logs--313-host.log
[2026-11-27T20:23:29Z] R copied 8ebb4bebabf61fc74034e90f9d97388592df118e009a6471fbba0bdb091eedd3 /root/btc-forensics/tz56-work--logs--313-refs-raw.txt
[2026-11-27T20:23:29Z] R copied 6238782a71e456aca6d8788fae52e603e7ccf2148115bb8d44ef07d52093426a /root/btc-forensics/tz56-work--logs--313-refs.log
[2026-11-27T20:23:29Z] R copied 6a4efe39d72188a79760d5e4a2528e37275e72bb5368591611a0aa0503dd4127 /root/btc-forensics/tz56-work--logs--313-still.log
[2026-11-27T20:23:29Z] R copied d8cd0a4cfca19fd4d08498b7e407c90e309993d6b72457cb67e2f4fcf7966733 /root/btc-forensics/tz56-work--logs--32-selftest.log
[2026-11-27T20:23:29Z] R copied 9b0067cccecc201d77f80715ae50cc4dc4ca58363b6d536e7cff6bf3313df2b3 /root/btc-forensics/tz56-work--logs--33-scratch.log
[2026-11-27T20:23:29Z] R copied 3f546249b6f559e4e0569a42bc7e937c14c3b08e0da28607bd0cc6d00000297d /root/btc-forensics/tz56-work--logs--33-still.log
[2026-11-27T20:23:29Z] R copied 1181e11824b818bdd1b4166340d791cd1236ca224addc6f28fca5e1319d127fe /root/btc-forensics/tz56-work--logs--34-probe.log
[2026-11-27T20:23:29Z] R copied 378cb37d2d71469ce347aee2345fb8ba46c7b8c23ba29031ef9bfa4fb7e46b31 /root/btc-forensics/tz56-work--logs--35-rehearse.log
[2026-11-27T20:23:29Z] R copied c015ca3c2b2e23a3647757a20bf38cdbf5086718c2cf32dd5b5573af2ebac323 /root/btc-forensics/tz56-work--logs--9-evidence-hashes.log
[2026-11-27T20:23:29Z] R copied 160b207d9f17d34621dd5331fbbbe830d9a6b5ed49de4caaa856e68c0a61a458 /root/btc-forensics/tz56-work--logs--9-reclaim.log
[2026-11-27T20:23:29Z] R copied 3fdc9fe7f548beb1c7ec706c533c47ead8e581ffdc4a92965ba7ec4600561673 /root/btc-forensics/tz56-work--rehearsal--draws-kalshi.jsonl
[2026-11-27T20:23:29Z] R copied ffa9366c8641c68f61fd708d46a650d1a2b73eec915b7f979c341bc61ef75a7f /root/btc-forensics/tz56-work--rehearsal--draws-polymarket.jsonl
[2026-11-27T20:23:29Z] R copied 83de241cfea6aeff53b8341c9d6e2668d48efae5640b8557f46474afe5b931bb /root/btc-forensics/tz56-work--rehearsal--frame-kalshi.jsonl
[2026-11-27T20:23:29Z] R copied c22fb7d561851e76cd9720e7ecf611e61fb8426078a057a6ecce864fcd66a433 /root/btc-forensics/tz56-work--rehearsal--frame-polymarket.jsonl
[2026-11-27T20:23:29Z] R copied dab24eeea64510d67558c5d82236934266232478328428330e3328d26eb5f406 /root/btc-forensics/tz56-work--rehearsal--raw-draw-kalshi.jsonl.gz
[2026-11-27T20:23:29Z] R copied f5e312b22a714982e545cc944d5774c6d7f65c8184cdb48687b18cedd5f57cde /root/btc-forensics/tz56-work--rehearsal--raw-draw-kalshi.jsonl.gz.idx
[2026-11-27T20:23:29Z] R copied 3fd4630cd5497218ff1072ac5e9b83f69caf64ae0868ad72c10973a3f84b7b75 /root/btc-forensics/tz56-work--rehearsal--raw-draw-polymarket.jsonl.gz
[2026-11-27T20:23:29Z] R copied 659745acebe3fcb0110d78bfa88f82978eabad4a6f07e8a3c07e2b0ce966d41c /root/btc-forensics/tz56-work--rehearsal--raw-draw-polymarket.jsonl.gz.idx
[2026-11-27T20:23:29Z] R copied a586e51e260b19eb37be6bc71eba67aea46878b5a4d1848d9c75c496b1453373 /root/btc-forensics/tz56-work--rehearsal--raw-frame-kalshi.jsonl.gz
[2026-11-27T20:23:29Z] R copied 199376f8b5316c6aaa88991c95951d7627078565af90e3be4eb1c1aadf8e6ca3 /root/btc-forensics/tz56-work--rehearsal--raw-frame-kalshi.jsonl.gz.idx
[2026-11-27T20:23:29Z] R copied 343d45b2707cecf24d3f3cf2dc66ca14b5cd26ef15cd41e39839b0a10e4ee291 /root/btc-forensics/tz56-work--rehearsal--raw-frame-polymarket.jsonl.gz
[2026-11-27T20:23:29Z] R copied 63c3a54f551c83f1b9629ef4b9f451627016b24a31a53335d74b291150f0b4bc /root/btc-forensics/tz56-work--rehearsal--raw-frame-polymarket.jsonl.gz.idx
[2026-11-27T20:23:29Z] R copied 1b94d50b613968df8ad9529e2c2af7d2a547d6177157367c22e1353cace1b524 /root/btc-forensics/tz56-work--stage--research--tz56-k0-favourite.py
[2026-11-27T20:23:29Z] RECLAIM PASS: 35 files considered, 34 named by a report, 1 kept by name, 35 copied, 0 already held, 0 left to the Release tz-56-k0-inputs that holds them; forensic store 2841 -> 2876 files
[2026-11-27T20:23:29Z] malloc tuned: True
[2026-11-27T20:23:29Z] peak memory of this run: 32219136 bytes
[2026-11-27T20:23:29Z] opens, requests and processes refused: 0
exit=0
```

Quoted from the work tree before B-RECLAIM-OWN removed it. Its forensic copy, `tz56-work--logs--9-reclaim.log`, holds the log's first 24 lines, `3,427` bytes, as they stood when `reclaim` copied the log while writing it.

#### §9 step 3 — B-RECLAIM-OWN, its output whole

The one paste of §9, run by the Executor and not refused. A `date -u` line comes first, and its output went to the scratchpad, `b-reclaim-own.log` (§0.0's one exception):

```
Fri Nov 27 08:23:46 PM UTC 2026
tz56-work exit=1
/root/btc-5m-twap       20e45f4 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
```

`tz56-work exit=1`. The worktree list holds the primary checkout and `/root/btc-recorder-svc` alone.

### 2.5 The files of this run

Every log is kept by name in `/root/btc-forensics/` as `tz56-work--logs--<name>` (§9).

| file | lines | bytes | SHA-256 |
|---|---|---|---|
| `logs/00-worktree.log` | 3 | 98 | `5d7bfc749b98c8d600eb1e357901f9fec08c0eb08348c70ccfb4f103b049c2eb` |
| `logs/01-stage.log` | 3 | 168 | `171864599f8ea4db1e553457778653acf877bb4cfbf5277b86cbeb4e6e462113` |
| `logs/02-fingerprint.log` | 85 | 14,024 | `e1045fc884b372f53e748ac208d9204c7eb8cab7d0e06637438fb7befb70829e` |
| `logs/03-host-gate.log` | 78 | 2,593 | `f2792c03f84615f2a312692cbe4f5606f7a81da1f05b95084c42439fe9e56ae8` |
| `logs/05-number.log` | 7 | 439 | `7005b65ff5c7ad08cebcd7dece209719e746076a90c07ab60fb5d204308f4c53` |
| `logs/05-refs-raw.txt` | 262 | 19,642 | `b3ed65cc61ddc503f71567615102e486fab543635331ae18221a91da280718c0` |
| `logs/05-refs.log` | 48 | 2,151 | `ebd1848af1cfc46b9ff106a459e1edb4d6b9238ad9ea387f603247bcc3b49c97` |
| `logs/31-branch.log` | 37 | 1,521 | `bda2b1c5ad732937c6c47583ac2631619f05f1681f582ef04b387dff61a6767c` |
| `logs/31-pr.log` | 3 | 95 | `0496ba9568948bbff3447f9b71625018d55d612b3b0714dc1c752e1fb6cb24f3` |
| `logs/313-host.log` | 79 | 2,644 | `3055fbd4b6d90d907df57ccc6e4f2a5c31fe348d04d1f5bb42987e67e5ebb454` |
| `logs/313-refs-raw.txt` | 265 | 19,832 | `8ebb4bebabf61fc74034e90f9d97388592df118e009a6471fbba0bdb091eedd3` |
| `logs/313-refs.log` | 6 | 307 | `6238782a71e456aca6d8788fae52e603e7ccf2148115bb8d44ef07d52093426a` |
| `logs/313-still.log` | 11 | 871 | `6a4efe39d72188a79760d5e4a2528e37275e72bb5368591611a0aa0503dd4127` |
| `logs/32-selftest.log` | 21 | 1,951 | `d8cd0a4cfca19fd4d08498b7e407c90e309993d6b72457cb67e2f4fcf7966733` |
| `logs/33-scratch.log` | 10 | 751 | `9b0067cccecc201d77f80715ae50cc4dc4ca58363b6d536e7cff6bf3313df2b3` |
| `logs/33-still.log` | 11 | 836 | `3f546249b6f559e4e0569a42bc7e937c14c3b08e0da28607bd0cc6d00000297d` |
| `logs/34-probe.log` | 19 | 3,345 | `1181e11824b818bdd1b4166340d791cd1236ca224addc6f28fca5e1319d127fe` |
| `logs/35-rehearse.log` | 42 | 4,718 | `378cb37d2d71469ce347aee2345fb8ba46c7b8c23ba29031ef9bfa4fb7e46b31` |
| `logs/9-evidence-hashes.log` | 22 | 1,735 | `c015ca3c2b2e23a3647757a20bf38cdbf5086718c2cf32dd5b5573af2ebac323` |
| `logs/9-reclaim.log` | 43 | 6,117 | `db37ba1008227ec79283f85636b357908060bf20d5cfd89a295a54495178f171` |
| `state.json` | 32 | 621 | `5989b6e5a1c06061d3f054eac1d903895e413992f9b4cf7906611b2e9e942926` |
| `read-ledger.jsonl` | 1 | 216 | `ab388200704c824a7065f1968cc78ab47ed20910ee4baa382215e512768f2c93` |

`release-set.json`, `verify.json` and `run/score.json` do not exist: `pack`, `verify` and `score` never ran.

### 2.6 Publication — contract §4.2's separation self-check

Run before this report's commit, against `origin/main` at `20e45f4`. The implementation commit is not on `main`, the branch differs from `main` by the instrument alone, and `main` holds no `.parquet` or `.zip`. No Release was made: B-UPLOAD's step was never reached.

```
$ git rev-list origin/main | grep -c a8f6a8905a8d3a5c374ad33fc6ebad0d3cc56058
0
$ git diff --name-only origin/main origin/tz-56-k0-favourite
research/tz56-k0-favourite.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
(exit=1)
```

## 3. Departures, named

1. **`I scratch "$S"` named no directory, so B-RECLAIM-SCRATCH was not run.**
   - `S` is the scratchpad as §0.3 defines it, `/tmp/claude-0/-root-btc-5m-twap/f05cea76-…/scratchpad`.
   - `mode_scratch` lists the directory that holds its argument. Given `$S`, that is this session's own directory, which holds no UUID directory. Map §7 item 150 means the directory one level up, `$(dirname "$(dirname "$S")")`; TZ-55 passed `"$(dirname "$S")"`.
   - §3.3 was run as written. Its rule "where `scratch` names none earlier, the block is not run" was followed.
   - §0.3's listing shows 14 UUID directories beside this session's own, among them those the map names `0736470b-…` and `6f0f41a7-…`. None was classified and none was removed.
2. **The branch's commit message has a co-author trailer after the TZ's title.** Its first line is §3.1's `TZ-56: K0's instrument - research/tz56-k0-favourite.py`, and the pull request's title is the same. The file is byte for byte §0.1's.
3. **The host gate's margin uses `du -sb` of the whole reward book store** in place of its stream files alone, which §0.3's commands do not separate. The store's other files make the margin larger by their size.
4. **`logs/05-refs.log` holds a mis-bucketed first count by prefix** from a `sed` of the Executor's, followed by the corrected count. Both are quoted whole in §2.3.
5. **Log names the TZ does not fix were chosen by the Executor:**
   - `00-worktree.log`, `01-stage.log`, `02-fingerprint.log`
   - `05-refs-raw.txt`, `31-branch.log`, `31-pr.log`
   - `313-refs.log`, `313-refs-raw.txt`, `9-evidence-hashes.log`
6. **`logs/9-evidence-hashes.log` is an extra read**, `sha256sum` and `stat` of the rehearsal's twelve files. It names them by hash so that `reclaim` keeps them as the evidence of §1, and it prints none of their content.
