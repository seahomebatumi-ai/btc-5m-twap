# TZ-36 report — the advisor's card says what it rests on: the forward book in parts, each card's basis and invalidation, and the Boss's six ratings

**NUMBER PASS: 2 of 2** at §0.5 (08:29:14 UTC) and again at §3.1 (08:29:20 UTC): `CryptoTZ/` holds `TZ-36-advisor-trust-block.md` and no other `TZ-36-` file, `CryptoReports/` no `TZ-36-` report; the branch count `0` before the push.
**G-RULE PASS: 7 of 7** — the fourteen rule functions identical by `ast.dump`, `adv3-bot.py` and `RULE-ADV-3.txt` `main`'s byte for byte · **SELFTESTS: 44 of 44, 19 of 19, 26 of 26**.
**G-HISTORY PASS: 20 of 20 equal** · `history.json` `19,434` bytes, SHA-256 `99e6a47d6aa4ac96eff0a84ca31fc720bdaf734c0f2084d3c7f9350c406b668c`, the Architect's bytes (DETERMINISM); 250.0 s wall, 24.53 s of processor, peak RSS `69,947,392` bytes.
**B-DEPLOY `exit=0`** (mark 08:36:10.294645 UTC) · **COPY PASS: 5 of 5** · **G-RENDER PASS: 10 of 10** (message 3,499 characters, 74 lines, 3 cards; report 13,348 bytes) · **P-START: served - 5 of 5 endpoints**.
**B-KILL `exit=0`** (mark 08:36:43.719500 UTC) · **UNIT-NEW PASS: 9 of 9** — pid `3404850` → `3574987`, started 08:37:13 UTC, `NRestarts` 0 → 1; the three capture units unchanged (`2388318`/0, `3530053`/15, `3137952`/1).
**No rollback ran**: B-ROLLBACK, B-KILL2, UNIT-OLD, K-36 and `stopped` were not run, no step failed.
**The unit runs the new code**: `adv3-bot.service` `active`, `running`, `enabled`, pid `3574987`, `/root/adv3-bot-svc/adv3.py` `d73a657e…`, `commit.txt` `444628905625809f24dd1fa51159b4093b763789` — verified by `I unit new` and by §3.7's `systemctl show`, `is-enabled`, `journalctl` and `service.log`, never from the Boss's account. The day's message was not sent again: `daily-sent` `2026-10-31` and 3 `daily` records at both marks and after.
**Findings, recorded and gating nothing (§2.14):** the unit was stopped and started three times on 2026-10-30, at 09:04:03, 09:21:35 and 09:23:02 UTC, by no TZ; `service.log` holds two `getUpdates failed` records at 01:12:27 and 01:13:52 UTC on 2026-10-31, the process surviving both; nine session directories of 2026-10-30 that no report names, reclaimed.
**Departures, all in §6:** the first B-RECLAIM-SCRATCH removal refused by Claude Code's built-in safety check for its shell variables and re-issued with literal paths, one tree a command; timing wrappers on G-HISTORY and G-RENDER; the logs' names; reads no step names; the map read in sections.

| field | value |
|---|---|
| TZ | `CryptoTZ/TZ-36-advisor-trust-block.md`, 2,269 lines, 154,273 bytes, SHA-256 `497d4c890ad5e4e4fed6593f4916009e3c25727a6afa9ff7f636a6c607f90cae`, landed at `369d1fa` (2026-10-31 08:25:02 UTC) |
| map revision | `2026-10-29-b`, equal; anchors 6 of 6; re-derived 4 of 4; rows 55; `frozen` equal 52 of 52 |
| executor model | the model the TZ header names: `get_session` read `configured_model`, `session_context.model` and `external_metadata.last_served_model` all `claude-opus-5-5` |
| branch | `tz-36-advisor-trust-block` at `444628905625809f24dd1fa51159b4093b763789`, on `origin/main` `369d1fa`; pushed; pull request #36, open, not merged |
| service's code | `/root/adv3-bot-svc/`: `adv3.py` `d73a657e…` (was `7f2863a5…`), `adv3-bot.py` `e65de91c…` unchanged, `commit.txt` `444628905625809f24dd1fa51159b4093b763789` (was `6c74b62b…`) |
| unit | `/etc/systemd/system/adv3-bot.service` `82acd8e4…`, unchanged; never reloaded |
| interpreter | `/root/tz04a-env/venv/bin/python` 3.12; every session mode under `nice -n 19` and `-B` |
| marks | `deploy` 08:36:10.294645 UTC · `kill` 08:36:43.719500 UTC (`state.json`) |
| blocks | B-DEPLOY 08:36:10.245 UTC, the Executor · B-KILL 08:36:43.684 UTC, the Executor · B-RECLAIM-SCRATCH's eleven removals 08:30:53 – 08:31:26 UTC and B-RECLAIM-OWN 08:41:04 – 08:41:09 UTC, the Executor · one command refused: B-RECLAIM-SCRATCH's first, a loop over shell variables, by Claude Code's built-in safety check at about 08:30:40 UTC, never run (§6 item 1) · none handed to the Boss |
| work tree | `/root/tz36-work/`, created 08:28 UTC, removed by B-RECLAIM-OWN (§2.15) |

---

## 0. Fingerprint

`I fingerprint`, from the staged copy of the checker, against the primary checkout at `369d1fa` — revision
`2026-10-29-b`; anchors `A1` `229a944f2d51`, `A2` `6c5089330629`, `A3` `0-complete / 1-student-5tau-not-disqualified /
2-no-edge-4tau-240-undecidable`, `A4` `437b45ea196b`, `A5` `0f6c90451cbd`, `A6` `729f0bcdbee3`, each equal to the TZ
header's; `A2`, `A4`, `A5` and `A6` re-derived. **V1: `READING FINGERPRINT: PASS - 64 of 64`.** The map, the `reported`
row: 1,954 lines, 464,175 bytes, SHA-256 `23fab3f5106d402277cb7394e7ccc4bfba510ae0879253be80a1ae745a7800b1`.

### 0.1 The 55 rows of the map's §0 table

| path | lines | bytes | state | SHA-256 | against the map |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 1,954 | 464,175 | reported | `23fab3f5106d402277cb7394e7ccc4bfba510ae0879253be80a1ae745a7800b1` | — |
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
| `research/tz20-capture-under-systemd.py` | 771 | 36,528 | frozen | `104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7` | equal |
| `research/tz21-recorder-memory.py` | 1,284 | 59,009 | frozen | `d6d2dc195809f2160fda7856980d8ccfbf0006ba0836943ff789c877f9d5795f` | equal |
| `research/tz23-maker-m0.py` | 1,184 | 54,885 | frozen | `6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f` | equal |
| `research/tz24-nesting-b2.py` | 1,535 | 76,142 | frozen | `4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b` | equal |
| `research/tz26-nesting-b3-capture.py` | 2,492 | 118,466 | frozen | `caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec` | equal |
| `research/tz27-pairbook-archive.py` | 2,078 | 106,284 | frozen | `2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673` | equal |
| `research/tz28-pairbook-archive-timer.py` | 1,438 | 74,576 | frozen | `46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4` | equal |
| `research/tz29-maker-m0-second-look.py` | 1,225 | 68,959 | frozen | `18defff93d08c13ea4638a518c88a3fec5541fcf53fb6827451e727f2204d905` | equal |
| `research/tz30-nesting-b3-measure.py` | 2,518 | 131,119 | frozen | `93dbbf1c4f84553a7bc041387ef92c3c0d8747c384d383b4fcd0b247fcd131ab` | equal |
| `research/tz31-who-earns.py` | 1,523 | 84,775 | frozen | `7073188c8fbaa19568e8c6e4d6379e40ea57cf2a1341ebde0ea6a08f2c544765` | equal |
| `research/tz32-our-quoting.py` | 2,576 | 138,209 | frozen | `6ec367e6ed995b315063d2d808dd6a3995878011afd76abfbb7b106b645a9c61` | equal |
| `research/tz33-reward-book-capture.py` | 3,542 | 175,160 | frozen | `a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670` | equal |
| `research/tz34-rewardbook-archive-timer.py` | 1,791 | 99,388 | frozen | `1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72` | equal |
| `research/tz35-advisor-deploy.py` | 802 | 42,049 | frozen | `d50787db5113c3f748806a60a3e71211b665cb5235296e43d0e9a747a529e6f5` | equal |
| `research/recorder/recorder.py` | 651 | 27,821 | frozen | `0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7` | equal |
| `research/recorder/config.py` | 112 | 4,773 | frozen | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | equal |
| `research/recorder/manifest.py` | 254 | 10,002 | frozen | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | equal |
| `research/recorder/analyze.py` | 813 | 34,705 | frozen | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` | equal |
| `research/recorder/probe.py` | 227 | 9,324 | frozen | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | equal |
| `research/recorder/selftest.py` | 573 | 30,591 | frozen | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` | equal |
| `deploy/systemd/btc-recorder.service` | 23 | 707 | frozen | `3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1` | equal |
| `deploy/systemd/btc-chainbook.service` | 22 | 724 | frozen | `a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2` | equal |
| `deploy/systemd/btc-pairbook.service` | 22 | 761 | frozen | `ba02fe4175b961c387ea8066eb084704e69efc7fd0a48d8f623a0198334f8dd8` | equal |
| `deploy/systemd/btc-pairbook-archive.service` | 17 | 794 | frozen | `2e7fd45382af3da3b2ec29ced8d69870ef3d4481da4c6f327b90fc6cb5af78e7` | equal |
| `deploy/systemd/btc-pairbook-archive.timer` | 13 | 417 | frozen | `07581f4f331fbf9d2a1113cac42a2872d65ac69a872991bff7d2bda235eac913` | equal |
| `deploy/systemd/btc-rewardbook.service` | 23 | 817 | frozen | `7691720c7b2261a606af54bfa20b5068b89455ea54512c55dde861d6d8063bec` | equal |
| `deploy/systemd/btc-rewardbook-archive.service` | 17 | 810 | frozen | `a9abb1f092b3fb8359d37ea88df00dca8557d0f0482d04c12f0fbdd32601e33f` | equal |
| `deploy/systemd/btc-rewardbook-archive.timer` | 13 | 428 | frozen | `bf5af0252c420d8db1579b82e5da21472cdb6bc871fa8035ecf6f1edc9720a0f` | equal |
| `deploy/systemd/adv3-bot.service` | 27 | 863 | frozen | `82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66` | equal |
| `advisor/RULE-ADV-3.txt` | 33 | 3,203 | frozen | `ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169` | equal |
| `advisor/adv3.py` | 718 | 35,479 | frozen | `7f2863a5b433ed7008c8f44af4f9c59d724d0c016c2c317f451158899c4f9adb` | equal |
| `advisor/adv3-bot.py` | 422 | 19,365 | frozen | `e65de91c7b49c6f932db91e568a5956c005e63119c1cf6fb8724ffb0438d1dcb` | equal |
| `advisor/selftest-adv3.py` | 155 | 8,909 | frozen | `76bad371727e0d4bf13c1d009f1b8f9412133a33788c456ecd53d1f83df6f0e6` | equal |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | — |

### 0.2 `logs/02-fingerprint.log`, verbatim (V1)

```
2026-10-31T08:28:58.642901346Z
reported 1954 lines 464175 bytes 23fab3f5106d402277cb7394e7ccc4bfba510ae0879253be80a1ae745a7800b1 SYSTEM-MAP.md
frozen   234 lines 11128 bytes 437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b BTC-EXECUTOR-INSTRUCTIONS.md
frozen   1135 lines 50928 bytes 6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473 research/twap-divergence.py
frozen   376 lines 16736 bytes ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a research/selftest-twap-divergence.py
tracked  334 lines 14511 bytes f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4 research/tz02-distribution.py
frozen   441 lines 19357 bytes 729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68 research/pfair.py
frozen   619 lines 32559 bytes b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa research/selftest-pfair.py
frozen   577 lines 27138 bytes 715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f research/tz06-calibration.py
frozen   623 lines 28414 bytes 513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771 research/tz07a-variance-time.py
frozen   515 lines 24926 bytes 424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc research/tz07b-settlement-dispersion.py
frozen   745 lines 38822 bytes 37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c research/tz08a-out-of-sample.py
frozen   894 lines 41004 bytes b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6 research/tz09-disk-inventory.py
frozen   1224 lines 61018 bytes 406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088 research/tz10b-sigma-or-link.py
frozen   1231 lines 64732 bytes 0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839 research/tz11a-student-link.py
frozen   1157 lines 61637 bytes d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999 research/tz12-sized-gate.py
frozen   1074 lines 53901 bytes a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd research/tz13-sized-gate-test3.py
frozen   2124 lines 109972 bytes 978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02 research/tz14-quote-inventory.py
frozen   1517 lines 73799 bytes 66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3 research/tz15-phase2-gate.py
frozen   2198 lines 111192 bytes 3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125 research/tz16a-phase2-decisive-gate.py
frozen   1102 lines 38622 bytes e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92 research/tz17-settlement-chain.py
frozen   1683 lines 69517 bytes e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae research/tz18a-chainbook-capture.py
frozen   771 lines 36528 bytes 104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7 research/tz20-capture-under-systemd.py
frozen   1284 lines 59009 bytes d6d2dc195809f2160fda7856980d8ccfbf0006ba0836943ff789c877f9d5795f research/tz21-recorder-memory.py
frozen   1184 lines 54885 bytes 6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f research/tz23-maker-m0.py
frozen   1535 lines 76142 bytes 4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b research/tz24-nesting-b2.py
frozen   2492 lines 118466 bytes caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec research/tz26-nesting-b3-capture.py
frozen   2078 lines 106284 bytes 2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673 research/tz27-pairbook-archive.py
frozen   1438 lines 74576 bytes 46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4 research/tz28-pairbook-archive-timer.py
frozen   1225 lines 68959 bytes 18defff93d08c13ea4638a518c88a3fec5541fcf53fb6827451e727f2204d905 research/tz29-maker-m0-second-look.py
frozen   2518 lines 131119 bytes 93dbbf1c4f84553a7bc041387ef92c3c0d8747c384d383b4fcd0b247fcd131ab research/tz30-nesting-b3-measure.py
frozen   1523 lines 84775 bytes 7073188c8fbaa19568e8c6e4d6379e40ea57cf2a1341ebde0ea6a08f2c544765 research/tz31-who-earns.py
frozen   2576 lines 138209 bytes 6ec367e6ed995b315063d2d808dd6a3995878011afd76abfbb7b106b645a9c61 research/tz32-our-quoting.py
frozen   3542 lines 175160 bytes a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670 research/tz33-reward-book-capture.py
frozen   1791 lines 99388 bytes 1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72 research/tz34-rewardbook-archive-timer.py
frozen   802 lines 42049 bytes d50787db5113c3f748806a60a3e71211b665cb5235296e43d0e9a747a529e6f5 research/tz35-advisor-deploy.py
frozen   651 lines 27821 bytes 0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7 research/recorder/recorder.py
frozen   112 lines 4773 bytes 8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d research/recorder/config.py
frozen   254 lines 10002 bytes 79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045 research/recorder/manifest.py
frozen   813 lines 34705 bytes eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d research/recorder/analyze.py
frozen   227 lines 9324 bytes 50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2 research/recorder/probe.py
frozen   573 lines 30591 bytes c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90 research/recorder/selftest.py
frozen   23 lines 707 bytes 3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1 deploy/systemd/btc-recorder.service
frozen   22 lines 724 bytes a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2 deploy/systemd/btc-chainbook.service
frozen   22 lines 761 bytes ba02fe4175b961c387ea8066eb084704e69efc7fd0a48d8f623a0198334f8dd8 deploy/systemd/btc-pairbook.service
frozen   17 lines 794 bytes 2e7fd45382af3da3b2ec29ced8d69870ef3d4481da4c6f327b90fc6cb5af78e7 deploy/systemd/btc-pairbook-archive.service
frozen   13 lines 417 bytes 07581f4f331fbf9d2a1113cac42a2872d65ac69a872991bff7d2bda235eac913 deploy/systemd/btc-pairbook-archive.timer
frozen   23 lines 817 bytes 7691720c7b2261a606af54bfa20b5068b89455ea54512c55dde861d6d8063bec deploy/systemd/btc-rewardbook.service
frozen   17 lines 810 bytes a9abb1f092b3fb8359d37ea88df00dca8557d0f0482d04c12f0fbdd32601e33f deploy/systemd/btc-rewardbook-archive.service
frozen   13 lines 428 bytes bf5af0252c420d8db1579b82e5da21472cdb6bc871fa8035ecf6f1edc9720a0f deploy/systemd/btc-rewardbook-archive.timer
frozen   27 lines 863 bytes 82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66 deploy/systemd/adv3-bot.service
frozen   33 lines 3203 bytes ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169 advisor/RULE-ADV-3.txt
frozen   718 lines 35479 bytes 7f2863a5b433ed7008c8f44af4f9c59d724d0c016c2c317f451158899c4f9adb advisor/adv3.py
frozen   422 lines 19365 bytes e65de91c7b49c6f932db91e568a5956c005e63119c1cf6fb8724ffb0438d1dcb advisor/adv3-bot.py
frozen   155 lines 8909 bytes 76bad371727e0d4bf13c1d009f1b8f9412133a33788c456ecd53d1f83df6f0e6 advisor/selftest-adv3.py
tracked  5 lines 252 bytes 9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b .gitignore
ok   revision 2026-10-29-b
ok   anchor A1
ok   anchor A2
ok   anchor A3
ok   anchor A4
ok   anchor A5
ok   anchor A6
ok   A2 re-derived from research/twap-divergence.py
ok   A4 re-derived from BTC-EXECUTOR-INSTRUCTIONS.md
ok   A5 re-derived from research/recorder/recorder.py
ok   A6 re-derived from research/pfair.py
ok   frozen BTC-EXECUTOR-INSTRUCTIONS.md
ok   frozen research/twap-divergence.py
ok   frozen research/selftest-twap-divergence.py
ok   frozen research/pfair.py
ok   frozen research/selftest-pfair.py
ok   frozen research/tz06-calibration.py
ok   frozen research/tz07a-variance-time.py
ok   frozen research/tz07b-settlement-dispersion.py
ok   frozen research/tz08a-out-of-sample.py
ok   frozen research/tz09-disk-inventory.py
ok   frozen research/tz10b-sigma-or-link.py
ok   frozen research/tz11a-student-link.py
ok   frozen research/tz12-sized-gate.py
ok   frozen research/tz13-sized-gate-test3.py
ok   frozen research/tz14-quote-inventory.py
ok   frozen research/tz15-phase2-gate.py
ok   frozen research/tz16a-phase2-decisive-gate.py
ok   frozen research/tz17-settlement-chain.py
ok   frozen research/tz18a-chainbook-capture.py
ok   frozen research/tz20-capture-under-systemd.py
ok   frozen research/tz21-recorder-memory.py
ok   frozen research/tz23-maker-m0.py
ok   frozen research/tz24-nesting-b2.py
ok   frozen research/tz26-nesting-b3-capture.py
ok   frozen research/tz27-pairbook-archive.py
ok   frozen research/tz28-pairbook-archive-timer.py
ok   frozen research/tz29-maker-m0-second-look.py
ok   frozen research/tz30-nesting-b3-measure.py
ok   frozen research/tz31-who-earns.py
ok   frozen research/tz32-our-quoting.py
ok   frozen research/tz33-reward-book-capture.py
ok   frozen research/tz34-rewardbook-archive-timer.py
ok   frozen research/tz35-advisor-deploy.py
ok   frozen research/recorder/recorder.py
ok   frozen research/recorder/config.py
ok   frozen research/recorder/manifest.py
ok   frozen research/recorder/analyze.py
ok   frozen research/recorder/probe.py
ok   frozen research/recorder/selftest.py
ok   frozen deploy/systemd/btc-recorder.service
ok   frozen deploy/systemd/btc-chainbook.service
ok   frozen deploy/systemd/btc-pairbook.service
ok   frozen deploy/systemd/btc-pairbook-archive.service
ok   frozen deploy/systemd/btc-pairbook-archive.timer
ok   frozen deploy/systemd/btc-rewardbook.service
ok   frozen deploy/systemd/btc-rewardbook-archive.service
ok   frozen deploy/systemd/btc-rewardbook-archive.timer
ok   frozen deploy/systemd/adv3-bot.service
ok   frozen advisor/RULE-ADV-3.txt
ok   frozen advisor/adv3.py
ok   frozen advisor/adv3-bot.py
ok   frozen advisor/selftest-adv3.py
ok   the table holds 55 rows, 52 frozen, 2 tracked, 1 reported
READING FINGERPRINT: PASS - 64 of 64
exit=0
```

### 0.3 Contract §1, §0.0 and §0.1 — the start-up, the work tree and the files staged (V4)

Contract §1 step 1 as `git pull origin main`, a fast-forward from `20a5aa1` to `369d1fa` (§6). Step 2: this TZ read in
full; the map read in the sections this TZ rests on (§6). Step 5: the model, above. Then §0.0 and §0.1:

```
2026-10-31T08:28:45.065217200Z
$ mkdir /root/tz36-work /root/tz36-work/logs; echo "exit=$?"
exit=0
```

```
2026-10-31T08:28:55.401619111Z
/root/tz36-work/stage/advisor/adv3.py 817 43274 d73a657ef31decad276b858c4ec9672dce1c1c5cec36f0bb1c5b3378838224a8
/root/tz36-work/stage/advisor/selftest-adv3.py 201 12600 ef4ffc44e6f8bcdd5685fc1db9090957890c6e2ab762cdad8ae9826b18cf1395
/root/tz36-work/stage/research/tz36-advisor-trust.py 582 32925 a0fb9d53afe435d37354862eb8fd299256bf551fdbdb25a5c828d2cc7376d4f5
exit=0
```

Three files, 3 of 3 hashes asserted by the script, lines and bytes equal to §0.1's table: `817` / `43,274`, `201` /
`12,600`, `582` / `32,925`.

### 0.4 Host gate — §0.3's block, verbatim (V2)

`S` = `/tmp/claude-0/-root-btc-5m-twap/84903452-8bf4-53c5-8169-67946f6e03f0/scratchpad`, the scratchpad the session's
system prompt names.

```
2026-10-31T08:29:04.326888873Z
Sat Oct 31 08:29:04 AM UTC 2026
1793435344
2026-08-02 07:24:32
1
MemTotal:         978640 kB
MemAvailable:     154780 kB
SwapTotal:       3174396 kB
SwapFree:        2384004 kB
units: {"adv3-bot.service": {"ActiveState": "active", "MainPID": "3404850", "NRestarts": "0", "SubState": "running", "UnitFileState": "enabled"}, "btc-pairbook.service": {"ActiveState": "active", "MainPID": "3530053", "NRestarts": "15", "SubState": "running", "UnitFileState": "enabled"}, "btc-recorder.service": {"ActiveState": "active", "MainPID": "2388318", "NRestarts": "0", "SubState": "running", "UnitFileState": "enabled"}, "btc-rewardbook.service": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1", "SubState": "running", "UnitFileState": "enabled"}}
MemAvailable 189366272 bytes, /dev/vda2 free 11058540544 bytes
ok   H1 the recorder's manifest.json is found
ok   H2 /dev/vda2 of 31612203008 bytes
ok   H2 the recorder's runtime record names e3975b5
ok   H3 the venv interpreter is Python 3.12
ok   H4 btc-recorder.service active and enabled
ok   H4 btc-pairbook.service active and enabled
ok   H4 btc-rewardbook.service active and enabled
ok   H5 the bot is active, running and enabled
ok   H5 the bot's MainPID runs the unit's argv, alone
ok   H5 the service copy holds adv3.py, adv3-bot.py and commit.txt only
ok   H5 adv3.py is TZ-35's and adv3-bot.py is TZ-35's
ok   H5 the installed unit file is TZ-35's
ok   H5 commit.txt is 40 hex characters and a newline
ok   H6 the record holds daily-sent and a journal of whole lines
ok   memory gate: MemAvailable at least 170344448 bytes
ok   disk gate: /dev/vda2 free at least 7400000000 bytes
READING HOST: PASS - 16 of 16
exit=0
NEXT                        LEFT LAST                              PASSED UNIT                         ACTIVATES
Sat 2026-10-31 17:34:37 UTC   9h Fri 2026-10-30 22:50:03 UTC       9h ago apt-daily.timer              apt-daily.service
Sun 2026-11-01 01:30:20 UTC  17h Sat 2026-10-31 01:30:20 UTC       6h ago btc-rewardbook-archive.timer btc-rewardbook-archive.service
Sun 2026-11-01 03:00:20 UTC  18h Sat 2026-10-31 03:00:20 UTC 5h 28min ago btc-pairbook-archive.timer   btc-pairbook-archive.service
Sun 2026-11-01 06:59:49 UTC  22h Sat 2026-10-31 06:38:15 UTC 1h 50min ago apt-daily-upgrade.timer      apt-daily-upgrade.service

4 timers listed.
Result=success
Id=btc-pairbook-archive.service
ActiveState=inactive
SubState=dead

Result=success
Id=btc-rewardbook-archive.service
ActiveState=inactive
SubState=dead
/root/adv3-bot-svc:
total 68
drwxr-xr-x  2 root root  4096 Oct 29 14:31 .
drwx------ 31 root root  4096 Oct 31 08:28 ..
-rw-r--r--  1 root root 19365 Oct 29 14:31 adv3-bot.py
-rw-r--r--  1 root root 35479 Oct 29 14:31 adv3.py
-rw-r--r--  1 root root    41 Oct 29 14:31 commit.txt

/var/lib/adv3-bot:
total 28
drwx------  2 root root 4096 Oct 31 06:00 .
drwxr-xr-x 65 root root 4096 Oct 29 14:35 ..
-rw-r--r--  1 root root   10 Oct 31 06:00 daily-sent
-rw-r--r--  1 root root 5181 Oct 31 06:00 journal.jsonl
-rw-r--r--  1 root root    9 Oct 29 22:22 offset
-rw-r--r--  1 root root 3883 Oct 31 06:00 service.log
299079751	/var/lib/btc-rewardbook
418711557	/var/lib/btc-pairbook
9083	/var/lib/adv3-bot
16	/root/.claude
2205
/root/btc-5m-twap       369d1fa [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/tmp/claude-0/-root-btc-5m-twap/84903452-8bf4-53c5-8169-67946f6e03f0/scratchpad
total 64
drwx------ 16 root root 4096 Oct 31 08:27 .
drwx------ 35 root root 4096 Oct 31 08:27 ..
drwx------  3 root root 4096 Oct 30 10:57 071d0d7b-ddbc-48b3-991a-390d7227eba7
drwx------  3 root root 4096 Oct 31 08:27 0bf93b31-e4ab-4a54-9db3-a06f592b7731
drwx------  3 root root 4096 Oct 30 10:50 10a2a619-2a88-453d-beb8-0858b997698e
drwx------  3 root root 4096 Oct 30 13:16 238335b9-cf23-414a-8e8f-ad4705c4d19e
drwx------  3 root root 4096 Oct 30 09:04 24fcb748-8b14-4628-b276-95cedf090169
drwx------  3 root root 4096 Oct 30 10:12 2f6bff8e-bc1d-5739-89f1-a9aa8c67fcbf
drwx------  3 root root 4096 Oct 30 10:12 38aa8f58-e5a3-4eed-b545-99f6d41def44
drwx------  3 root root 4096 Oct 29 14:12 670d0460-3b29-4949-95f8-46f94b680ab9
drwx------  3 root root 4096 Oct 30 09:04 6e88615c-345d-5a08-be99-6375cc1a1073
drwx------  4 root root 4096 Oct 31 08:27 84903452-8bf4-53c5-8169-67946f6e03f0
drwx------  4 root root 4096 Oct 29 14:12 95f1d37e-8b62-5abb-93a1-839ff07d8cf8
drwx------  3 root root 4096 Oct 30 10:21 9d963148-63a3-442a-9a55-43eefc435bef
drwx------  3 root root 4096 Oct 30 10:22 ab276d07-3a6d-45e9-b929-6c3200721aa1
drwx------  3 root root 4096 Oct 30 10:21 d8ebff7a-39f7-5a2e-a6a6-420082860b13
```

**V2: `READING HOST: PASS - 16 of 16`.** Printed, no threshold: the forensic store `2,205` files, map §3's; the
worktrees two, map §3's; the timers' next elapses 2026-11-01 01:30:20 and 03:00:20 UTC, both archives `inactive`,
`Result=success` — their last runs at 01:30:20 and 03:00:20 UTC today; the record and the service copy as listed. The
scratch directory's listing held thirteen UUID directories beside this session's own, where map §3 expected TZ-35's two
(§2.3). `du -sb /root/.claude` read 16 bytes; this session's own store is `/root/.claude-8j/`, which no step reads.

### 0.5 Free space and `MemAvailable` — every read, its instant and its bound

| instant (UTC) | read | value | bound |
|---|---|---|---|
| 08:29:04 | §0.3's `grep` of `/proc/meminfo`, printed | `MemAvailable` 154,780 kB = `158,494,720` bytes | none on this read; it is below `170,344,448` (§6) |
| 08:29:04 – 08:29:13 | `I host`, the memory gate | `189,366,272` bytes | `170,344,448` — PASS |
| 08:29:04 – 08:29:13 | `I host`, the disk gate (`df` of `/var/lib/btc-recorder`) | `11,058,540,544` bytes free on `/dev/vda2` | `7,400,000,000` — PASS |
| 08:37:35 | §3.7's `free -b` | available `197,439,488` bytes | none |
| 08:37:35 | §3.7's `df` | `11,041,579,008` bytes free | none |
| 08:41:09 | §9's `df`, B-RECLAIM-OWN | `11,045,969,920` bytes free | none |

Peaks, read by the timing wrappers (§6): `adv3.py --history` `68,308` kB = `69,947,392` bytes, under the Architect's
`85,172,224` and TZ-35's host peak `72,032,256`; `I render`'s process tree, its two runs of the service copy's
`adv3.py` included, `63,956` kB = `65,490,944` bytes. The unit's new process: `MemoryPeak` `17,403,904` at 08:37:35,
under its `MemoryMax=128M`.

### 0.6 Refs and the number (§0.5) — `logs/04-refs-number.log`, verbatim (V3)

```
2026-10-31T08:29:14.921454283Z
fetch exit=0
369d1fa3e548f6de769f18f003c4c1ad0ebc7f25	HEAD
369d1fa3e548f6de769f18f003c4c1ad0ebc7f25	refs/heads/main
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
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793263627
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793286490
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793306720
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793321975
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793323820
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793357934
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793410220
d3251aa2bd312409f7b096bfd5968f3bedbd1be5	refs/tags/tz-01a-dataset
ea9290b92b9fa50c22d0560d5d01dfa392af44df	refs/tags/tz-01a-dataset^{}
e299d4e45f48b7efaa8cb18bd54b139fc0627630	refs/tags/tz-27-pairbook-streams
bce5a85be7850a33f95192265b916cc9c5e0aaf1	refs/tags/tz-27-pairbook-streams^{}
ls-remote exit=0
0
CryptoTZ/TZ-36-advisor-trust-block.md
ok   CryptoTZ/ holds CryptoTZ/TZ-36-advisor-trust-block.md and no other file of that number
ok   CryptoReports/ holds no report of that number
READING NUMBER: PASS - 2 of 2
exit=0
369d1fa 2026-10-31T12:25:02+04:00 Add files via upload

A	CryptoTZ/TZ-36-advisor-trust-block.md
d97dd19 2026-10-29T23:19:36+04:00 Update SYSTEM-MAP.md

M	SYSTEM-MAP.md
d7909cd 2026-10-29T23:15:26+04:00 Merge pull request #35 from seahomebatumi-ai/tz-35-advisor-bot

D	.github/workflows/adv2-signal.yml
D	ADVISOR-SKILL.md
A	advisor/RULE-ADV-3.txt
A	advisor/adv3-bot.py
A	advisor/adv3.py
A	advisor/selftest-adv3.py
A	deploy/systemd/adv3-bot.service
A	research/tz35-advisor-deploy.py
20a5aa1 2026-10-29T14:59:50+00:00 TZ-35 report: the advisor's Telegram bot runs as adv3-bot.service - NUMBER 2 of 2 twice; G-SAME PASS, 546 candles, 0 mismatches; G-HISTORY 16 of 16, history.json bcee5309; COPY 4 of 4; P-START 5 of 5; G-CHAT, G-HELLO; PROPS 11 of 11; G-UNIT 18 of 18 at 0 and 1; G-DAILY 8 of 8, G-REPLY 1 of 1; G-LOAD 0.003; G-RESTART 5 of 5, G-ONCE 2 of 2; G-STILL 3 of 3; H6 failed once before the Boss's token step; B-ENABLE run by the Boss

A	CryptoReports/TZ-35-advisor-bot-report.md
c2d5fc0 2026-10-29T18:10:55+04:00 Add files via upload

A	CryptoTZ/TZ-35-advisor-bot.md
```

**93 ref lines** (`HEAD` and 92 under `refs/`). Against map §1's record of 87: PR #35's merge ref gone (−1); two more
`pairbook-streams-*` tags, `1793356734` and `1793415620` (34 in all); five more `rewardbook-streams-*` tags,
`1793306720`, `1793321975`, `1793323820`, `1793357934` and `1793410220` (7 in all); `main` at `369d1fa`, the upload of
this TZ, above `d97dd19`, revision `2026-10-29-b`. Recorded, not blocking: `main` carries revision `2026-10-29-b`.

---

## 1. Input

| input | what | read |
|---|---|---|
| `CryptoTZ/TZ-36-advisor-trust-block.md` | the TZ and Appendix A | 2,269 lines, 154,273 bytes, `497d4c89…`; §0.1's script extracted its three files twice |
| `SYSTEM-MAP.md` | revision `2026-10-29-b` | 1,954 lines, 464,175 bytes, `23fab3f5…`; its 55 table rows hashed |
| `origin/main` `advisor/adv3.py`, `advisor/adv3-bot.py`, `advisor/RULE-ADV-3.txt` | G-RULE's old side | by `git show`, `7f2863a5…`, `e65de91c…`, `ee206e7c…` |
| Binance's archive, `data.binance.vision` | G-HISTORY: the 42 coins' daily klines from 2019-09 and monthly funding through 2026-09, to the close of 2026-10-27 | re-collected by `adv3.py --history` at 08:31:41 – 08:35:51 UTC; written only as `history.json`'s derived figures, `19,434` bytes |
| `fapi.binance.com` | G-RENDER's two runs of the service copy; P-START's four requests | at 08:36:15 – 08:36:24 and 08:36:30 – 08:36:31 UTC; nothing stored |
| `api.telegram.org` | P-START's one `getMe`, by the bot's own `--probe` | 08:36:31 UTC |
| the host | units, `/proc`, `/var/lib/adv3-bot/{daily-sent,journal.jsonl,service.log}`, the service copy, `df`, `du`, the UUID directories of `/tmp/claude-0/-root-btc-5m-twap/` | as quoted |

Nothing under `/etc/adv3-bot/` was read, copied, printed or hashed by this session's own commands; the token was read by
`adv3-bot.py --probe` alone, which printed the bot's username. No dataset was re-collected but the archive's candles and
funding for G-HISTORY, which the TZ requires.

---

## 2. Measurements

### 2.1 §3.1 — the branch and its files (V3, V4)

```
2026-10-31T08:29:20.280563508Z
fetch exit=0
CryptoTZ/TZ-36-advisor-trust-block.md
ok   CryptoTZ/ holds CryptoTZ/TZ-36-advisor-trust-block.md and no other file of that number
ok   CryptoReports/ holds no report of that number
READING NUMBER: PASS - 2 of 2
exit=0
Preparing worktree (new branch 'tz-36-advisor-trust-block')
branch 'tz-36-advisor-trust-block' set up to track 'origin/main'.
HEAD is now at 369d1fa Add files via upload
worktree exit=0
```

§0.1's script over the worktree, verbatim but for its argument, then `add` and the two diffs:

```
2026-10-31T08:29:32.366119414Z
/root/tz36-work/wt/advisor/adv3.py 817 43274 d73a657ef31decad276b858c4ec9672dce1c1c5cec36f0bb1c5b3378838224a8
/root/tz36-work/wt/advisor/selftest-adv3.py 201 12600 ef4ffc44e6f8bcdd5685fc1db9090957890c6e2ab762cdad8ae9826b18cf1395
/root/tz36-work/wt/research/tz36-advisor-trust.py 582 32925 a0fb9d53afe435d37354862eb8fd299256bf551fdbdb25a5c828d2cc7376d4f5
exit=0
add exit=0
M	advisor/adv3.py
M	advisor/selftest-adv3.py
A	research/tz36-advisor-trust.py
115	16	advisor/adv3.py
48	2	advisor/selftest-adv3.py
582	0	research/tz36-advisor-trust.py
M  advisor/adv3.py
M  advisor/selftest-adv3.py
A  research/tz36-advisor-trust.py
```

The same lines, bytes and SHA-256 as §0.1's; `--name-status` exactly `M`, `M`, `A`; `--numstat` exactly `115 16`, `48 2`,
`582 0`. The commit, `ls-remote` and the push:

```
2026-10-31T08:29:40.094534532Z
commit exit=0
444628905625809f24dd1fa51159b4093b763789 2026-10-31T08:29:40+00:00 TZ-36: the advisor's card says what it rests on - advisor/adv3.py and advisor/selftest-adv3.py replaced, research/tz36-advisor-trust.py added
 advisor/adv3.py                | 131 ++++++++--
 advisor/selftest-adv3.py       |  50 +++-
 research/tz36-advisor-trust.py | 582 +++++++++++++++++++++++++++++++++++++++++
 3 files changed, 745 insertions(+), 18 deletions(-)
59
0
remote: 
remote: Create a pull request for 'tz-36-advisor-trust-block' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-36-advisor-trust-block        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-36-advisor-trust-block -> tz-36-advisor-trust-block
branch 'tz-36-advisor-trust-block' set up to track 'origin/tz-36-advisor-trust-block'.
push exit=0
```

The push went through the URL's own credential (map §6, git remote); `gh`'s route was not needed. The pull request:

```
2026-10-31T08:29:57.865553119Z
https://github.com/seahomebatumi-ai/btc-5m-twap/pull/36
exit=0
```

### 2.2 §3.2 — the self-tests and G-RULE (V5, V6): **44 of 44, 19 of 19, 26 of 26; RULE 7 of 7**

```
2026-10-31T08:30:03.942080325Z
SELFTEST-ADV3 PASS: 44 of 44 checks passed
exit=0
SELFTEST PASS: 19 of 19 checks passed
exit=0
SELFTEST PASS: 26 of 26 checks passed
exit=0
ok   the functions that changed are exactly ['card', 'card_lines', 'facts_checks', 'history', 'message', 'report']
ok   the functions added are exactly ['book_line', 'forward_book', 'signed', 'trust', 'trust_lines']
ok   no function removed
ok   the 14 rule functions are identical by AST
ok   the constants: FACTS changed, RELIABILITY and STRONG_JUSTIFIED added, nothing else
ok   adv3-bot.py is main's, byte for byte
ok   RULE-ADV-3.txt is main's and hashes to the RULE constant
READING RULE: PASS - 7 of 7
exit=0
```

### 2.3 §3.3 — the directories beside this session, and B-RECLAIM-SCRATCH (V15)

```
2026-10-31T08:30:09.468822983Z
running 3435609 started 2026-10-30T13:15:54.700000Z claude
running 3435619 started 2026-10-30T13:15:56.710000Z claude
running 3435628 started 2026-10-30T13:15:58.010000Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
running 3435667 started 2026-10-30T13:16:00.220000Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
running 3435954 started 2026-10-30T13:18:48.500000Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
running 3572807 started 2026-10-31T08:27:37.720000Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
071d0d7b-ddbc-48b3-991a-390d7227eba7 born 2026-10-30T10:57:40.000000Z: earlier
0bf93b31-e4ab-4a54-9db3-a06f592b7731 born 2026-10-31T08:27:38.000000Z: live, process [3572807]
10a2a619-2a88-453d-beb8-0858b997698e born 2026-10-30T10:50:41.000000Z: earlier
238335b9-cf23-414a-8e8f-ad4705c4d19e born 2026-10-30T13:16:00.000000Z: live, process [3435609, 3435619, 3435628, 3435667]
24fcb748-8b14-4628-b276-95cedf090169 born 2026-10-30T09:04:06.000000Z: earlier
2f6bff8e-bc1d-5739-89f1-a9aa8c67fcbf born 2026-10-30T10:12:24.000000Z: earlier
38aa8f58-e5a3-4eed-b545-99f6d41def44 born 2026-10-30T10:12:23.000000Z: earlier
670d0460-3b29-4949-95f8-46f94b680ab9 born 2026-10-29T14:12:20.000000Z: earlier
6e88615c-345d-5a08-be99-6375cc1a1073 born 2026-10-30T09:04:08.000000Z: earlier
95f1d37e-8b62-5abb-93a1-839ff07d8cf8 born 2026-10-29T14:12:21.000000Z: earlier
9d963148-63a3-442a-9a55-43eefc435bef born 2026-10-30T10:21:01.000000Z: earlier
ab276d07-3a6d-45e9-b929-6c3200721aa1 born 2026-10-30T10:22:32.000000Z: earlier
d8ebff7a-39f7-5a2e-a6a6-420082860b13 born 2026-10-30T10:21:02.000000Z: earlier
exit=0
```

Eleven **earlier**, two **live** — `0bf93b31…`, born with this session's own process `3572807`, and `238335b9…`, born
with the running `claude` processes `3435609`, `3435619`, `3435628` and `3435667` of 2026-10-30 13:15 UTC — and this
session's own, `84903452…`, not listed. The eleven: TZ-35's two, `95f1d37e…` and `670d0460…`, and nine born on
2026-10-30 between 09:04 and 10:57 UTC that no report names. One `reclaim` named all eleven:

```
2026-10-31T08:30:27.205218996Z
reclaim: 3474 report tokens; forensic store holds 2205 files
RECLAIM PASS: 4 files considered, 0 named by a report, 0 kept by name, 0 copied, 0 already held; forensic store 2205 -> 2205 files
exit=0
```

`RECLAIM PASS` printed before any removal. Then one `rm -rf` and one `test -e` a directory, each removal a command of its
own, by literal path (§6):

```
2026-10-31T08:30:53.277474236Z
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/071d0d7b-ddbc-48b3-991a-390d7227eba7
exit=0
$ test -e /tmp/claude-0/-root-btc-5m-twap/071d0d7b-ddbc-48b3-991a-390d7227eba7
exit=1
2026-10-31T08:31:26.647372720Z
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/10a2a619-2a88-453d-beb8-0858b997698e
exit=0
$ test -e /tmp/claude-0/-root-btc-5m-twap/10a2a619-2a88-453d-beb8-0858b997698e
exit=1
2026-10-31T08:31:26.692429231Z
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/24fcb748-8b14-4628-b276-95cedf090169
exit=0
$ test -e /tmp/claude-0/-root-btc-5m-twap/24fcb748-8b14-4628-b276-95cedf090169
exit=1
2026-10-31T08:31:26.720011644Z
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/2f6bff8e-bc1d-5739-89f1-a9aa8c67fcbf
exit=0
$ test -e /tmp/claude-0/-root-btc-5m-twap/2f6bff8e-bc1d-5739-89f1-a9aa8c67fcbf
exit=1
2026-10-31T08:31:26.750977063Z
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/38aa8f58-e5a3-4eed-b545-99f6d41def44
exit=0
$ test -e /tmp/claude-0/-root-btc-5m-twap/38aa8f58-e5a3-4eed-b545-99f6d41def44
exit=1
2026-10-31T08:31:26.783402363Z
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/670d0460-3b29-4949-95f8-46f94b680ab9
exit=0
$ test -e /tmp/claude-0/-root-btc-5m-twap/670d0460-3b29-4949-95f8-46f94b680ab9
exit=1
2026-10-31T08:31:26.810549841Z
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/6e88615c-345d-5a08-be99-6375cc1a1073
exit=0
$ test -e /tmp/claude-0/-root-btc-5m-twap/6e88615c-345d-5a08-be99-6375cc1a1073
exit=1
2026-10-31T08:31:26.845758845Z
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/95f1d37e-8b62-5abb-93a1-839ff07d8cf8
exit=0
$ test -e /tmp/claude-0/-root-btc-5m-twap/95f1d37e-8b62-5abb-93a1-839ff07d8cf8
exit=1
2026-10-31T08:31:26.899343323Z
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/9d963148-63a3-442a-9a55-43eefc435bef
exit=0
$ test -e /tmp/claude-0/-root-btc-5m-twap/9d963148-63a3-442a-9a55-43eefc435bef
exit=1
2026-10-31T08:31:26.931666467Z
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/ab276d07-3a6d-45e9-b929-6c3200721aa1
exit=0
$ test -e /tmp/claude-0/-root-btc-5m-twap/ab276d07-3a6d-45e9-b929-6c3200721aa1
exit=1
2026-10-31T08:31:26.965940803Z
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/d8ebff7a-39f7-5a2e-a6a6-420082860b13
exit=0
$ test -e /tmp/claude-0/-root-btc-5m-twap/d8ebff7a-39f7-5a2e-a6a6-420082860b13
exit=1
$ ls -la /tmp/claude-0/-root-btc-5m-twap
total 20
drwx------  5 root root 4096 Oct 31 08:31 .
drwx------ 35 root root 4096 Oct 31 08:27 ..
drwx------  3 root root 4096 Oct 31 08:27 0bf93b31-e4ab-4a54-9db3-a06f592b7731
drwx------  3 root root 4096 Oct 30 13:16 238335b9-cf23-414a-8e8f-ad4705c4d19e
drwx------  4 root root 4096 Oct 31 08:27 84903452-8bf4-53c5-8169-67946f6e03f0
```

Eleven removals, each `exit=0`, each `test -e` `exit=1`; the two live directories and this session's own remain. None was
handed to the Boss.

### 2.4 §3.4 — G-HISTORY and DETERMINISM (V7): **20 of 20 equal**

```
2026-10-31T08:31:41.862151445Z
history written: /root/tz36-work/history.json 19434 bytes, SHA-256 99e6a47d6aa4ac96eff0a84ca31fc720bdaf734c0f2084d3c7f9350c406b668c
G-HISTORY base trades          5265                   FACTS 5265       equal
G-HISTORY base wins            1708                   FACTS 1708       equal
G-HISTORY base mean R          0.15759304269466592    FACTS 0.1576     equal
G-HISTORY base median days     3                      FACTS 3          equal
G-HISTORY base p               0.022629314494404588   FACTS 0.0226     equal
G-HISTORY base top-5 share     0.3041848895460389     FACTS 0.3042     equal
G-HISTORY base share +1R       0.23247863247863249    FACTS 0.2325     equal
G-HISTORY base share +2R       0.12972459639126305    FACTS 0.1297     equal
G-HISTORY base share +3R       0.0818613485280152     FACTS 0.0819     equal
G-HISTORY strong trades        253                    FACTS 253        equal
G-HISTORY strong wins          83                     FACTS 83         equal
G-HISTORY strong mean R        0.5473377337624986     FACTS 0.5473     equal
G-HISTORY strong median days   19.0                   FACTS 19         equal
G-HISTORY strong p             0.05452310219275515    FACTS 0.0545     equal
G-HISTORY strong top-5 share   1.0093372174123556     FACTS 1.0093     equal
G-HISTORY strong share +1R     0.4782608695652174     FACTS 0.4783     equal
G-HISTORY strong share +2R     0.2845849802371542     FACTS 0.2846     equal
G-HISTORY strong share +3R     0.17786561264822134    FACTS 0.1779     equal
G-HISTORY gate H               NOT DISQUALIFIED       FACTS NOT DISQUALIFIED equal
G-HISTORY gate S               NOT DISQUALIFIED       FACTS NOT DISQUALIFIED equal
printed, gating nothing: base total 829.7274 R, Sharpe 0.7663, t 2.0022, p 0.022629, worst drawdown -253.7817 R
printed, gating nothing: strong total 138.4764 R, Sharpe 0.6133, t 1.6025, p 0.054523, worst drawdown -60.1030 R
READING G-HISTORY: PASS - 20 of 20 equal
	Command being timed: "nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz36-work/wt/advisor/adv3.py --history /root/tz36-work/history.json"
	User time (seconds): 21.24
	System time (seconds): 3.29
	Percent of CPU this job got: 9%
	Elapsed (wall clock) time (h:mm:ss or m:ss): 4:10.00
	Average shared text size (kbytes): 0
	Average unshared data size (kbytes): 0
	Average stack size (kbytes): 0
	Average total size (kbytes): 0
	Maximum resident set size (kbytes): 68308
	Average resident set size (kbytes): 0
	Major (requiring I/O) page faults: 996
	Minor (reclaiming a frame) page faults: 18794
	Voluntary context switches: 55803
	Involuntary context switches: 19047
	Swaps: 0
	File system inputs: 26560
	File system outputs: 48
	Socket messages sent: 0
	Socket messages received: 0
	Signals delivered: 0
	Page size (bytes): 4096
	Exit status: 0
exit=0
99e6a47d6aa4ac96eff0a84ca31fc720bdaf734c0f2084d3c7f9350c406b668c  /root/tz36-work/history.json
19434 /root/tz36-work/history.json
2026-10-31T08:35:51.884315234Z
```

**V7:** `READING G-HISTORY: PASS - 20 of 20 equal`; the file `19,434` bytes, SHA-256
`99e6a47d6aa4ac96eff0a84ca31fc720bdaf734c0f2084d3c7f9350c406b668c`, equal to §3.4's fixed value. The two additions: the
one-sided `p` `0.022629314494404588` (rule) and `0.05452310219275515` (STRONG); the top-5 share `0.3041848895460389` and
`1.0093372174123556` — each equal to the Architect's figures of §4.2 to the digits it states. Inside the `timeout 1800`:
250.0 s wall, 21.24 s user, 3.29 s system.

### 2.5 §3.5 — B-DEPLOY (V8)

Its band, seconds `23,700` to `85,500`, was open (second `30,970` of the day); the block ran verbatim but for its log's
name:

```
2026-10-31T08:36:10.245288594Z
mark deploy at 2026-10-31T08:36:10Z: bot pid 3404850 NRestarts 0, daily-sent 2026-10-31, 3 daily records
exit=0
```

### 2.6 §3.5 — COPY and G-RENDER (V9, V10): **5 of 5, 10 of 10**

```
2026-10-31T08:36:14.893108162Z
ok   the service copy holds adv3.py, adv3-bot.py and commit.txt only
ok   adv3.py is Appendix A's
ok   adv3-bot.py is unchanged
ok   commit.txt is the branch head and the worktree's HEAD
ok   the branch's adv3.py equals the service copy's
READING COPY: PASS - 5 of 5
exit=0
2026-10-31T08:36:14.950698769Z
message: 3499 characters, 74 lines; report: 13348 bytes
ok   the message run exits 0 with no traceback
ok   the message holds the forward book, the six ratings and their lines
ok   every card (3) holds its basis and its invalidation
ok   the message fits three Telegram parts
ok   the report run exits 0 with no traceback
ok   the report is the frozen rule's, of 42 coins
ok   the ratings: system 1, STRONG not justified, the data fresh, a trade 0 or 1, one for each card
ok   the books: opened is closed plus open, the total is the two parts' sum
ok   the forward days are the closes from 2026-10-28 to the report's
ok   each card carries a rank 1 to 3 and a sum of signs of 2 to 4 in size
READING RENDER: PASS - 10 of 10
render: 9.54 s wall, 2.22 s user, 0.20 s system, 63956 kB peak (the checker process tree)
exit=0
2026-10-31T08:36:24.493869188Z
```

Only counts and labels: the message 3,499 characters and 74 lines, 3 cards, under 12,000; the report 13,348 bytes.

### 2.7 §3.6 — P-START (V11): **served - 5 of 5 endpoints**

```
2026-10-31T08:36:30.269480644Z
P-KLINES served: 1499 closed daily candles of BTCUSDT, the last 2026-10-30
P-FUNDING served: 5 settlement days of BTCUSDT since 2026-10-27
P-MARKS served: 945 perpetuals, all 42 coins among them with a mark price
P-INTERVALS served: 820 perpetuals with an adjusted funding interval, 42 of the coins among them
P-TELEGRAM served: bot @ClaudeCryptoSignal_bot
READING P-START: served - 5 of 5 endpoints
exit=0
2026-10-31T08:36:31.506740343Z
```

### 2.8 §3.6 — B-KILL and UNIT-NEW (V12): **9 of 9**

B-KILL's band, seconds `23,700` to `85,800`, was open (second `31,003`); the block ran verbatim but for its log's name:

```
2026-10-31T08:36:43.684289520Z
mark kill at 2026-10-31T08:36:43Z: bot pid 3404850 NRestarts 0, daily-sent 2026-10-31, 3 daily records
exit=0
```

`I mark kill` asserted `daily-sent` today's UTC date before the signal. `I unit new` first ran at 08:37:28.886 UTC, 45.2 s
after the mark, and read PASS at its first run — no `NOT YET`:

```
2026-10-31T08:37:28.885658614Z
bot: pid 3574987 NRestarts 1 started 2026-10-31T08:37:13Z; captures: {"btc-pairbook.service": ["3530053", "15"], "btc-recorder.service": ["2388318", "0"], "btc-rewardbook.service": ["3137952", "1"]}
ok   the unit is active, running and enabled
ok   a new MainPID, one restart more
ok   the process started after the kill mark and within 90 s of it
ok   the process runs the unit's exact argv, alone
ok   the service copy is new's adv3.py, the process started after the copy
ok   the service copy's bot and the unit file are unchanged
ok   the day's message was not sent again: daily-sent and the journal's daily records as before
ok   the log shows the new process serving and no daily sent, no traceback, since the mark
ok   the three capture units unchanged, each active
READING UNIT-NEW: PASS - 9 of 9
exit=0
```

**V12:** pid `3404850` → `3574987`; the mark at 08:36:43.719500 UTC, systemd's `SIGTERM` at 08:36:43, the restart
scheduled and the process started at 08:37:13 UTC — `RestartSec=30` — 29 to 30 s after the mark, inside the 90 s;
`NRestarts` 0 → 1.

### 2.9 §3.7 — the closing reads (V14)

```
2026-10-31T08:37:35.639750188Z
MainPID=3574987
Result=success
NRestarts=1
MemoryCurrent=17137664
MemoryPeak=17403904
Nice=10
Id=adv3-bot.service
ActiveState=active
ActiveEnterTimestamp=Sat 2026-10-31 08:37:13 UTC

MainPID=2388318
Result=success
NRestarts=0
MemoryCurrent=63823872
MemoryPeak=316174336
Nice=0
Id=btc-recorder.service
ActiveState=active
ActiveEnterTimestamp=Fri 2026-10-23 06:08:56 UTC

MainPID=3530053
Result=success
NRestarts=15
MemoryCurrent=2048000
MemoryPeak=50589696
Nice=0
Id=btc-pairbook.service
ActiveState=active
ActiveEnterTimestamp=Sat 2026-10-31 03:06:30 UTC

MainPID=3137952
Result=success
NRestarts=1
MemoryCurrent=15806464
MemoryPeak=78729216
Nice=10
Id=btc-rewardbook.service
ActiveState=active
ActiveEnterTimestamp=Wed 2026-10-28 12:56:29 UTC

MainPID=0
Result=success
NRestarts=0
MemoryCurrent=[not set]
MemoryPeak=[not set]
Nice=19
Id=btc-pairbook-archive.service
ActiveState=inactive
ActiveEnterTimestamp=

MainPID=0
Result=success
NRestarts=0
MemoryCurrent=[not set]
MemoryPeak=[not set]
Nice=19
Id=btc-rewardbook-archive.service
ActiveState=inactive
ActiveEnterTimestamp=
NEXT                        LEFT LAST                              PASSED UNIT                         ACTIVATES
Sun 2026-11-01 01:30:20 UTC  16h Sat 2026-10-31 01:30:20 UTC       7h ago btc-rewardbook-archive.timer btc-rewardbook-archive.service
Sun 2026-11-01 03:00:20 UTC  18h Sat 2026-10-31 03:00:20 UTC 5h 37min ago btc-pairbook-archive.timer   btc-pairbook-archive.service

2 timers listed.
enabled
exit=0
2026-10-29T14:44:05+00:00 vultr systemd[1]: adv3-bot.service: Scheduled restart job, restart counter is at 1.
2026-10-29T14:44:05+00:00 vultr systemd[1]: Started adv3-bot.service - ADV-3 advisor, the Boss's Binance Futures signals over Telegram.
2026-10-30T09:04:03+00:00 vultr systemd[1]: Stopping adv3-bot.service - ADV-3 advisor, the Boss's Binance Futures signals over Telegram...
2026-10-30T09:04:03+00:00 vultr systemd[1]: adv3-bot.service: Deactivated successfully.
2026-10-30T09:04:03+00:00 vultr systemd[1]: Stopped adv3-bot.service - ADV-3 advisor, the Boss's Binance Futures signals over Telegram.
2026-10-30T09:04:03+00:00 vultr systemd[1]: adv3-bot.service: Consumed 5.005s CPU time, 35.3M memory peak, 33.7M memory swap peak.
2026-10-30T09:04:03+00:00 vultr systemd[1]: Started adv3-bot.service - ADV-3 advisor, the Boss's Binance Futures signals over Telegram.
2026-10-30T09:21:35+00:00 vultr systemd[1]: Stopping adv3-bot.service - ADV-3 advisor, the Boss's Binance Futures signals over Telegram...
2026-10-30T09:21:35+00:00 vultr systemd[1]: adv3-bot.service: Deactivated successfully.
2026-10-30T09:21:35+00:00 vultr systemd[1]: Stopped adv3-bot.service - ADV-3 advisor, the Boss's Binance Futures signals over Telegram.
2026-10-30T09:21:35+00:00 vultr systemd[1]: Started adv3-bot.service - ADV-3 advisor, the Boss's Binance Futures signals over Telegram.
2026-10-30T09:23:02+00:00 vultr systemd[1]: Stopping adv3-bot.service - ADV-3 advisor, the Boss's Binance Futures signals over Telegram...
2026-10-30T09:23:02+00:00 vultr systemd[1]: adv3-bot.service: Deactivated successfully.
2026-10-30T09:23:02+00:00 vultr systemd[1]: Stopped adv3-bot.service - ADV-3 advisor, the Boss's Binance Futures signals over Telegram.
2026-10-30T09:23:02+00:00 vultr systemd[1]: Started adv3-bot.service - ADV-3 advisor, the Boss's Binance Futures signals over Telegram.
2026-10-31T08:36:43+00:00 vultr systemd[1]: adv3-bot.service: Sent signal SIGTERM to main process 3404850 (python) on client request.
2026-10-31T08:36:43+00:00 vultr systemd[1]: adv3-bot.service: Deactivated successfully.
2026-10-31T08:36:43+00:00 vultr systemd[1]: adv3-bot.service: Consumed 5.029s CPU time, 36.0M memory peak, 32.0M memory swap peak.
2026-10-31T08:37:13+00:00 vultr systemd[1]: adv3-bot.service: Scheduled restart job, restart counter is at 1.
2026-10-31T08:37:13+00:00 vultr systemd[1]: Started adv3-bot.service - ADV-3 advisor, the Boss's Binance Futures signals over Telegram.
    result = func(*args)
             ^^^^^^^^^^^
  File "/usr/lib/python3.12/urllib/request.py", line 1392, in https_open
    return self.do_open(http.client.HTTPSConnection, req,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/urllib/request.py", line 1348, in do_open
    r = h.getresponse()
        ^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/http/client.py", line 1457, in getresponse
    response.begin()
  File "/usr/lib/python3.12/http/client.py", line 336, in begin
    version, status, reason = self._read_status()
                              ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/http/client.py", line 297, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/socket.py", line 707, in readinto
    return self._sock.recv_into(b)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/ssl.py", line 1252, in recv_into
    return self.read(nbytes, buffer)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/ssl.py", line 1104, in read
    return self._sslobj.read(len, buffer)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TimeoutError: The read operation timed out

2026-10-31T06:00:05Z candles refreshed to the close of 2026-10-30 | missing -
2026-10-31T06:00:07Z daily sent for the close of 2026-10-30
2026-10-31T08:37:13Z serving the pinned chat: pid 3574987 offset 685120811 daily-sent 2026-10-31
/root/adv3-bot-svc:
total 76
drwxr-xr-x  2 root root  4096 Oct 31 08:36 .
drwx------ 31 root root  4096 Oct 31 08:28 ..
-rw-r--r--  1 root root 19365 Oct 29 14:31 adv3-bot.py
-rw-r--r--  1 root root 43274 Oct 31 08:36 adv3.py
-rw-r--r--  1 root root    41 Oct 31 08:36 commit.txt

/var/lib/adv3-bot:
total 28
drwx------  2 root root 4096 Oct 31 06:00 .
drwxr-xr-x 65 root root 4096 Oct 29 14:35 ..
-rw-r--r--  1 root root   10 Oct 31 06:00 daily-sent
-rw-r--r--  1 root root 5181 Oct 31 06:00 journal.jsonl
-rw-r--r--  1 root root    9 Oct 29 22:22 offset
-rw-r--r--  1 root root 3980 Oct 31 08:37 service.log
               total        used        free      shared  buff/cache   available
Mem:      1002127360   804687872    92311552      126976   248770560   197439488
Swap:     3250581504   849932288  2400649216
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 11041579008
10896154	/root/tz36-work
62680	/root/adv3-bot-svc
9180	/var/lib/adv3-bot
303399432	/var/lib/btc-rewardbook
419504921	/var/lib/btc-pairbook
16	/root/.claude
{
 "marks": {
  "deploy": {
   "bot": {
    "ActiveState": "active",
    "MainPID": "3404850",
    "NRestarts": "0"
   },
   "caps": {
    "btc-pairbook.service": {
     "ActiveState": "active",
     "MainPID": "3530053",
     "NRestarts": "15"
    },
    "btc-recorder.service": {
     "ActiveState": "active",
     "MainPID": "2388318",
     "NRestarts": "0"
    },
    "btc-rewardbook.service": {
     "ActiveState": "active",
     "MainPID": "3137952",
     "NRestarts": "1"
    }
   },
   "daily": "2026-10-31",
   "journal": 3,
   "t": 1793435770.2946453
  },
  "kill": {
   "bot": {
    "ActiveState": "active",
    "MainPID": "3404850",
    "NRestarts": "0"
   },
   "caps": {
    "btc-pairbook.service": {
     "ActiveState": "active",
     "MainPID": "3530053",
     "NRestarts": "15"
    },
    "btc-recorder.service": {
     "ActiveState": "active",
     "MainPID": "2388318",
     "NRestarts": "0"
    },
    "btc-rewardbook.service": {
     "ActiveState": "active",
     "MainPID": "3137952",
     "NRestarts": "1"
    }
   },
   "daily": "2026-10-31",
   "journal": 3,
   "t": 1793435803.7195
  }
 }
}
```

The journal's last 20 lines are systemd's own for the unit. The tail of `service.log` opens inside a traceback; the
lines that place it, one read no step names (§6):

```
2026-10-31T08:37:55.277615938Z
$ grep -n -E "^[0-9]{4}-[0-9]{2}-[0-9]{2}T|^Traceback|^[A-Za-z.]*(Error|Exception)" /var/lib/adv3-bot/service.log
1:2026-10-29T14:38:10Z serving the pinned chat: pid 3290952 offset 0 daily-sent -
2:2026-10-29T14:38:16Z candles refreshed to the close of 2026-10-28 | missing -
3:2026-10-29T14:38:17Z daily sent for the close of 2026-10-28
4:2026-10-29T14:38:17Z help sent
5:2026-10-29T14:44:05Z serving the pinned chat: pid 3291955 offset 685120810 daily-sent 2026-10-29
6:2026-10-29T22:22:54Z candles refreshed to the close of 2026-10-28 | missing -
7:2026-10-29T22:22:56Z request answered for the close of 2026-10-28
8:2026-10-30T06:00:06Z candles refreshed to the close of 2026-10-29 | missing -
9:2026-10-30T06:00:08Z daily sent for the close of 2026-10-29
10:2026-10-30T09:04:04Z serving the pinned chat: pid 3402846 offset 685120811 daily-sent 2026-10-30
11:2026-10-30T09:21:35Z serving the pinned chat: pid 3404640 offset 685120811 daily-sent 2026-10-30
12:2026-10-30T09:23:02Z serving the pinned chat: pid 3404850 offset 685120811 daily-sent 2026-10-30
13:2026-10-31T01:12:27Z getUpdates failed
14:Traceback (most recent call last):
20:RuntimeError: telegram getUpdates: 502 Bad Gateway
22:2026-10-31T01:13:52Z getUpdates failed
23:Traceback (most recent call last):
65:TimeoutError: The read operation timed out
67:2026-10-31T06:00:05Z candles refreshed to the close of 2026-10-30 | missing -
68:2026-10-31T06:00:07Z daily sent for the close of 2026-10-30
69:2026-10-31T08:37:13Z serving the pinned chat: pid 3574987 offset 685120811 daily-sent 2026-10-31
69 /var/lib/adv3-bot/service.log
```

No token, no chat id, no coin, no price appears in either read.

### 2.10 Contract §4.2's self-check (V13) — after the push and the pull request, before the report's commit

```
2026-10-31T08:38:03.643464112Z
fetch exit=0
$ git rev-list origin/main | grep -c 444628905625809f24dd1fa51159b4093b763789
0
$ git diff --name-only origin/main origin/tz-36-advisor-trust-block
advisor/adv3.py
advisor/selftest-adv3.py
research/tz36-advisor-trust.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
grep exit=1
369d1fa3e548f6de769f18f003c4c1ad0ebc7f25
444628905625809f24dd1fa51159b4093b763789
{"baseRefName":"main","headRefName":"tz-36-advisor-trust-block","headRefOid":"444628905625809f24dd1fa51159b4093b763789","mergedAt":null,"number":36,"state":"OPEN","url":"https://github.com/seahomebatumi-ai/btc-5m-twap/pull/36"}
```

`0`; the three implementation files and nothing else; no `.parquet`, no `.zip`.

### 2.11 Every file the run wrote, by SHA-256, but the bot's own root

```
2026-10-31T08:38:12.699080878Z
7f2863a5b433ed7008c8f44af4f9c59d724d0c016c2c317f451158899c4f9adb  ./adv3.before
c7fa5d183b09e3b3fc93d7dbf78d205361d3e8d62c4162e2298f0be998021089  ./commit.before
99e6a47d6aa4ac96eff0a84ca31fc720bdaf734c0f2084d3c7f9350c406b668c  ./history.json
afcb69ae626ee6c1536b929c597ee1d0378fee061ddd342f98d43d86005090db  ./logs/00-mkdir.log
3c94a1e84fe12fa7dc3d2d7c4f32ee0cd1c5f2c6793a6e7678443a1e2f2ae737  ./logs/01-stage.log
d0130b479b7f237c7ed8768cde1c06b188bf661cc634a6e6e25b47acbdab861c  ./logs/02-fingerprint.log
9f1d713e57487b685ec4a99c8820c159621df2a2705d9e8ccee8147625df2dda  ./logs/03-host.log
dc61eec1f9926b4d1ba009fe0d058e2e549e30a9eab6fec1b535c7d85d62094e  ./logs/04-refs-number.log
613553f24328cb1ccc8f02806d8fd38524231e5555d2ec63d210660ab43e9c87  ./logs/05-branch.log
21a27effe7d248fd04dde2ed518d18b1a95d7a020db45d3c6c81079fb5ac0648  ./logs/06-extract-wt.log
72159b40001e347ae311162ab3eb10a41a4d4dee2b4c3e3373a3ce4b67d93964  ./logs/07-commit-push.log
a7885320cdaa531504ff7921cef79a7fe22bcaebc9e0224b14d0fd517fedbbb8  ./logs/08-pull-request.log
638bc16f4bc83ba5c318b2de7ced4fb8233f6d9184c4b5b9f23cd04f4f518160  ./logs/09-selftests-rule.log
4adee6a27393dc092a534fa8a09b63b86c37a2181adc380c7e26d8e4bde15639  ./logs/10-scratch.log
7a9124417ec31d2b622336449edb2edc5654e3326828e97d9c6c25d9eb171edc  ./logs/11-reclaim-scratch.log
3a68d439f373de0d1887bfb58d9d51491faf016a4c96dbf44e65a9aae82fc548  ./logs/12-rm-scratch.log
ea238a25cac81b2e275801030d4bdb5237aae4de8c2ab16637bf7eda080ad413  ./logs/13-g-history.log
2069a1e176f53709cade73cb63d0492f58d15447d99bed32e5394e1b9ba38f98  ./logs/14-b-deploy.log
932e5fb938ae893afa672cb29f60a34a74a8678400547fbde340fd54e88254c5  ./logs/15-copy-render.log
067197cede082d0c1da99a1eef325fb3c5c7306b7c376bbea656d42042607cdd  ./logs/16-p-start.log
4951473d5732a99a4d5158f2e537f801092e5d208329c537526043d445c031f2  ./logs/17-b-kill.log
c73fd366fe6e26a707d1ed1b4150750f153e027d100092a11aaf5643cadabb66  ./logs/18-unit-new.log
1e2ccf9e5f43d4d598c2856ea816f0703aa7fc11705e7aa8980ca163daffe49d  ./logs/19-closing-reads.log
8d5d30ff15aae810a81d6aea05ec0118b96b0c3b81ed34bda5f9c12f46c33f4c  ./logs/20-service-log-stamps.log
ddf120b8976d1048095ad62632a151d25e613381f97ba2feb8e2b8e753a1a5e5  ./logs/21-separation.log
a3b4bb138ddfea91763ac6dfa1913e36ac2883c5b75ab670e70240469f99222d  ./logs/22-files-written.log
d73a657ef31decad276b858c4ec9672dce1c1c5cec36f0bb1c5b3378838224a8  ./stage/advisor/adv3.py
ef4ffc44e6f8bcdd5685fc1db9090957890c6e2ab762cdad8ae9826b18cf1395  ./stage/advisor/selftest-adv3.py
a0fb9d53afe435d37354862eb8fd299256bf551fdbdb25a5c828d2cc7376d4f5  ./stage/research/tz36-advisor-trust.py
fc0a190a33d4165f32f02643e91c744e746b7e4dd4bea24cb72e4b8b32e38563  ./state.json
--- sizes
35479 ./adv3.before
41 ./commit.before
19434 ./history.json
99 ./logs/00-mkdir.log
401 ./logs/01-stage.log
9790 ./logs/02-fingerprint.log
4618 ./logs/03-host.log
7889 ./logs/04-refs-number.log
448 ./logs/05-branch.log
652 ./logs/06-extract-wt.log
929 ./logs/07-commit-push.log
94 ./logs/08-pull-request.log
687 ./logs/09-selftests-rule.log
1702 ./logs/10-scratch.log
230 ./logs/11-reclaim-scratch.log
2598 ./logs/12-rm-scratch.log
2999 ./logs/13-g-history.log
143 ./logs/14-b-deploy.log
1187 ./logs/15-copy-render.log
469 ./logs/16-p-start.log
141 ./logs/17-b-kill.log
843 ./logs/18-unit-new.log
7639 ./logs/19-closing-reads.log
1628 ./logs/20-service-log-stamps.log
655 ./logs/21-separation.log
2744 ./logs/22-files-written.log
43274 ./stage/advisor/adv3.py
12600 ./stage/advisor/selftest-adv3.py
32925 ./stage/research/tz36-advisor-trust.py
1117 ./state.json
--- worktree files the run wrote (tracked, committed)
d73a657ef31decad276b858c4ec9672dce1c1c5cec36f0bb1c5b3378838224a8  wt/advisor/adv3.py
ef4ffc44e6f8bcdd5685fc1db9090957890c6e2ab762cdad8ae9826b18cf1395  wt/advisor/selftest-adv3.py
a0fb9d53afe435d37354862eb8fd299256bf551fdbdb25a5c828d2cc7376d4f5  wt/research/tz36-advisor-trust.py
--- service copy
d73a657ef31decad276b858c4ec9672dce1c1c5cec36f0bb1c5b3378838224a8  /root/adv3-bot-svc/adv3.py
810c9ed61de6850bf05d7530d8b033396e56940a57f994dcefc4f823f2145b3e  /root/adv3-bot-svc/commit.txt
e65de91c7b49c6f932db91e568a5956c005e63119c1cf6fb8724ffb0438d1dcb  /root/adv3-bot-svc/adv3-bot.py
444628905625809f24dd1fa51159b4093b763789
6c74b62bfef7afad2c71c742411124387327a588
```

`logs/22-files-written.log` hashed itself while being written; its final hash, and every kept file's, is `I keep`'s line
in §2.15. The worktree's three files are the committed ones, `git status --porcelain --ignored` empty. On `main`: this
report. In `/root/btc-forensics/`: `I keep`'s copies, §2.15. In `/root/adv3-bot-svc/`: `adv3.py` `d73a657e…` and
`commit.txt` `810c9ed6…` (`444628905625809f24dd1fa51159b4093b763789` and a newline); `adv3.py.new` existed for the
`mv` alone.

### 2.12 The unit's journal and record, before and after

`journalctl` (§2.9): `SIGTERM` to main process `3404850` "on client request" at 08:36:43, "Consumed 5.029s CPU time,
36.0M memory peak, 32.0M memory swap peak"; "Scheduled restart job, restart counter is at 1" and "Started" at 08:37:13.
`service.log`: one line since the mark, `2026-10-31T08:37:13Z serving the pinned chat: pid 3574987 offset 685120811
daily-sent 2026-10-31`. `/var/lib/adv3-bot/`: `daily-sent` and `journal.jsonl` unchanged since 06:00 UTC (10 and 5,181
bytes), `service.log` 3,883 → 3,980 bytes.

### 2.13 Timeline

| UTC | step |
|---|---|
| 08:28:55 | §0.1 staged |
| 08:28:58 | §0.2 FINGERPRINT 64 of 64 |
| 08:29:04 | §0.3 HOST 16 of 16 |
| 08:29:14 | §0.5 refs, NUMBER 2 of 2 |
| 08:29:20 | §3.1 NUMBER 2 of 2, worktree |
| 08:29:40 | commit `4446289`, push |
| 08:29:57 | pull request #36 |
| 08:30:03 | SELFTESTS, RULE 7 of 7 |
| 08:30:09 – 08:31:26 | §3.3 scratch, reclaim, eleven removals |
| 08:31:41 – 08:35:51 | §3.4 G-HISTORY 20 of 20 |
| 08:36:10 | B-DEPLOY, mark `deploy` |
| 08:36:14 – 08:36:24 | COPY 5 of 5, G-RENDER 10 of 10 |
| 08:36:30 – 08:36:31 | P-START 5 of 5 |
| 08:36:43 | B-KILL, mark `kill` |
| 08:37:13 | the new process |
| 08:37:28 | UNIT-NEW 9 of 9 |
| 08:37:35 | §3.7's reads |
| 08:38:03 | contract §4.2 |
| after the draft | §9 B-RECLAIM-OWN (§2.15), then this report's commit |

### 2.14 Findings, recorded and gating nothing

1. **The advisor's unit was stopped and started three times on 2026-10-30, by no TZ.** The journal reads "Stopping …
   Deactivated successfully … Stopped … Started" at 09:04:03, 09:21:35 and 09:23:02 UTC — the shape of a manual stop and
   start, which resets `NRestarts`, so the host gate read `NRestarts` `0` where TZ-35 left `1` — and `service.log` a new
   process at each, `3402846`, `3404640` and `3404850`, each `daily-sent 2026-10-30`, no daily sent again. The code it ran
   was TZ-35's: the host gate read the service copy's and the unit file's hashes equal at 08:29. Who or what ran them is
   not readable to this session; the two session directories born at 09:04:06 and 09:04:08 UTC that day (§2.3) were
   reclaimed with nothing a report names.
2. **Two failed polls of Telegram on 2026-10-31**: `getUpdates failed` at 01:12:27 UTC (`RuntimeError: telegram
   getUpdates: 502 Bad Gateway`) and at 01:13:52 UTC (`TimeoutError: The read operation timed out`), each with its
   traceback in `service.log`; the process `3404850` ran on and sent the day's message at 06:00:07 UTC.
3. **Nine session directories of 2026-10-30, and a `claude` session still running from 13:15 UTC that day**
   (`238335b9…`, four processes), where map §3 expected TZ-35's two directories alone. The nine were reclaimed; 4 files
   considered, none named by a report.
4. The pair book's unit read `NRestarts` `15` at pid `3530053` (TZ-35: `3216422`, `12`), active since 03:06:30 UTC today,
   after its archive's run of 03:00:20; both archives `inactive`, `Result=success`. Unchanged across this TZ.

### 2.15 §9 B-RECLAIM-OWN — last, after §3.7, with this report drafted (V15, V16)

Run from the session in two calls, each beginning with `date -u`; its output was written to no file and is quoted here
verbatim, every line. The first call:

```
2026-10-31T08:41:04.546215100Z
K copied 7f2863a5b433ed7008c8f44af4f9c59d724d0c016c2c317f451158899c4f9adb /root/btc-forensics/tz36-work--adv3.before
K copied c7fa5d183b09e3b3fc93d7dbf78d205361d3e8d62c4162e2298f0be998021089 /root/btc-forensics/tz36-work--commit.before
K copied 99e6a47d6aa4ac96eff0a84ca31fc720bdaf734c0f2084d3c7f9350c406b668c /root/btc-forensics/tz36-work--history.json
K copied afcb69ae626ee6c1536b929c597ee1d0378fee061ddd342f98d43d86005090db /root/btc-forensics/tz36-work--logs--00-mkdir.log
K copied 3c94a1e84fe12fa7dc3d2d7c4f32ee0cd1c5f2c6793a6e7678443a1e2f2ae737 /root/btc-forensics/tz36-work--logs--01-stage.log
K copied d0130b479b7f237c7ed8768cde1c06b188bf661cc634a6e6e25b47acbdab861c /root/btc-forensics/tz36-work--logs--02-fingerprint.log
K copied 9f1d713e57487b685ec4a99c8820c159621df2a2705d9e8ccee8147625df2dda /root/btc-forensics/tz36-work--logs--03-host.log
K copied dc61eec1f9926b4d1ba009fe0d058e2e549e30a9eab6fec1b535c7d85d62094e /root/btc-forensics/tz36-work--logs--04-refs-number.log
K copied 613553f24328cb1ccc8f02806d8fd38524231e5555d2ec63d210660ab43e9c87 /root/btc-forensics/tz36-work--logs--05-branch.log
K copied 21a27effe7d248fd04dde2ed518d18b1a95d7a020db45d3c6c81079fb5ac0648 /root/btc-forensics/tz36-work--logs--06-extract-wt.log
K copied 72159b40001e347ae311162ab3eb10a41a4d4dee2b4c3e3373a3ce4b67d93964 /root/btc-forensics/tz36-work--logs--07-commit-push.log
K copied a7885320cdaa531504ff7921cef79a7fe22bcaebc9e0224b14d0fd517fedbbb8 /root/btc-forensics/tz36-work--logs--08-pull-request.log
K copied 638bc16f4bc83ba5c318b2de7ced4fb8233f6d9184c4b5b9f23cd04f4f518160 /root/btc-forensics/tz36-work--logs--09-selftests-rule.log
K copied 4adee6a27393dc092a534fa8a09b63b86c37a2181adc380c7e26d8e4bde15639 /root/btc-forensics/tz36-work--logs--10-scratch.log
K copied 7a9124417ec31d2b622336449edb2edc5654e3326828e97d9c6c25d9eb171edc /root/btc-forensics/tz36-work--logs--11-reclaim-scratch.log
K copied 3a68d439f373de0d1887bfb58d9d51491faf016a4c96dbf44e65a9aae82fc548 /root/btc-forensics/tz36-work--logs--12-rm-scratch.log
K copied ea238a25cac81b2e275801030d4bdb5237aae4de8c2ab16637bf7eda080ad413 /root/btc-forensics/tz36-work--logs--13-g-history.log
K copied 2069a1e176f53709cade73cb63d0492f58d15447d99bed32e5394e1b9ba38f98 /root/btc-forensics/tz36-work--logs--14-b-deploy.log
K copied 932e5fb938ae893afa672cb29f60a34a74a8678400547fbde340fd54e88254c5 /root/btc-forensics/tz36-work--logs--15-copy-render.log
K copied 067197cede082d0c1da99a1eef325fb3c5c7306b7c376bbea656d42042607cdd /root/btc-forensics/tz36-work--logs--16-p-start.log
K copied 4951473d5732a99a4d5158f2e537f801092e5d208329c537526043d445c031f2 /root/btc-forensics/tz36-work--logs--17-b-kill.log
K copied c73fd366fe6e26a707d1ed1b4150750f153e027d100092a11aaf5643cadabb66 /root/btc-forensics/tz36-work--logs--18-unit-new.log
K copied 1e2ccf9e5f43d4d598c2856ea816f0703aa7fc11705e7aa8980ca163daffe49d /root/btc-forensics/tz36-work--logs--19-closing-reads.log
K copied 8d5d30ff15aae810a81d6aea05ec0118b96b0c3b81ed34bda5f9c12f46c33f4c /root/btc-forensics/tz36-work--logs--20-service-log-stamps.log
K copied ddf120b8976d1048095ad62632a151d25e613381f97ba2feb8e2b8e753a1a5e5 /root/btc-forensics/tz36-work--logs--21-separation.log
K copied de11e372bf72ae1ae16fe84196a7be1f5e903c9aa9bded9a08f1a5a83d376762 /root/btc-forensics/tz36-work--logs--22-files-written.log
K copied fc0a190a33d4165f32f02643e91c744e746b7e4dd4bea24cb72e4b8b32e38563 /root/btc-forensics/tz36-work--state.json
KEEP PASS: 27 files kept, 27 copied, 0 already held; forensic store 2205 -> 2232 files; worktree at 444628905625809f24dd1fa51159b4093b763789, its upstream's
exit=0
```

The second:

```
2026-10-31T08:41:09.454985545Z
exit=0
exit=1
/root/btc-5m-twap       369d1fa [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
2232
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 11045969920
```

**V15:** `keep` considered 27 files — `state.json`, `history.json`, `adv3.before`, `commit.before` and the 23 logs — and
copied 27, none already held; the store's count after, `2,232`, is the count before, `2,205`, plus the 27 copies,
asserted by `keep` and read again by `find`. `logs/22-files-written.log`'s final hash is `de11e372…`. **V16:** `git
worktree remove` without `--force` `exit=0`; `rm -rf /root/tz36-work` `exit=0` and `test -e` `exit=1`; `git worktree
list` names `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else. Neither call was refused. The branch
`tz-36-advisor-trust-block` stays on `origin` and as a local ref.

---

## 3. Publication

| item | value |
|---|---|
| branch | `tz-36-advisor-trust-block`, pushed 08:29:40 UTC through the URL's own credential |
| commit | `444628905625809f24dd1fa51159b4093b763789`, parent `369d1fa3e548f6de769f18f003c4c1ad0ebc7f25`, three files, `+745 −18` |
| pull request | #36, `https://github.com/seahomebatumi-ai/btc-5m-twap/pull/36`, base `main`, open, not merged |
| Release | none: this TZ publishes no asset; `history.json` stays in the forensic store |
| deployment | `/root/adv3-bot-svc/adv3.py` replaced by the branch's at 08:36:10 UTC, the unit signalled at 08:36:43 — the TZ's own deployment (§3.5, §3.6); the merge stays the Boss's, after the verdict |
| separation self-check | §2.10: `0`; `advisor/adv3.py`, `advisor/selftest-adv3.py`, `research/tz36-advisor-trust.py`; nothing |
| report | this file, to `main` after B-RECLAIM-OWN |

---

## 4. Gate

| gate | PASS as the TZ fixes it (§4) | read | ratio | verdict |
|---|---|---|---|---|
| G-RULE | 7 of 7 | 7 of 7 | 1.000 | **PASS** |
| SELFTESTS | 44 of 44, 19 of 19 and 26 of 26 | 44, 19, 26 | 1.000 each | **PASS** |
| G-HISTORY | 20 of 20 facts equal to `FACTS`, and the file's bytes the Architect's | 20 of 20; `19,434` bytes, `99e6a47d…` | 1.000 | **PASS** |
| COPY | 5 of 5 | 5 of 5 | 1.000 | **PASS** |
| G-RENDER | 10 of 10 | 10 of 10 | 1.000 | **PASS** |
| P-START | `READING P-START: served - 5 of 5 endpoints` | served 5 of 5 | 1.000 | **PASS** |
| UNIT-NEW | 9 of 9 | 9 of 9 | 1.000 | **PASS** |

Nothing was tuned and no gate reinterpreted. Per §4.6, a PASS establishes that the service copy's `adv3.py` is Appendix
A's and the unit runs it; that the rule's fourteen functions, the rule text, the bot and the unit are what TZ-35 deployed;
that the twenty facts re-derive from Binance's archive; that the live message and report carry the forward book in parts,
a basis and an invalidation on every card and the six ratings, consistent with each other; and that the three capture
units are as they were. **Not established:** that the Boss's Telegram shows the message — his next «сигнал» or the
06:00 UTC message of 2026-11-01 is the first the running unit builds with the new code; the ratings' truth; anything about
the market to come.

---

## 5. Validation

| # | check | count | asserted? |
|---|---|---|---|
| **V1** | §0.2's fingerprint | `READING FINGERPRINT: PASS - 64 of 64`: revision; 6 anchors, 4 re-derived; 55 rows, 52 of 52 `frozen` equal; the shape | asserted by the checker (`verdict` raises, exit 1) |
| **V2** | §0.3's host gate | `READING HOST: PASS - 16 of 16` | asserted by the checker |
| **V3** | NUMBER at §0.5 and §3.1 | `PASS - 2 of 2` each, the `TZ-36-` path printed; the branch count `0` | NUMBER asserted by the checker; the branch count recorded, not asserted — read `0` by the Executor |
| **V4** | §0.1's and §3.1's files | 3 of 3 hashes at each, asserted by the script; lines and bytes equal; `M`, `M`, `A`; `--numstat` `115 16`, `48 2`, `582 0` | hashes asserted; the diff's names and numstat recorded, not asserted — compared by the Executor with §3.1's text, exact |
| **V5** | the self-tests | `44 of 44`, `19 of 19`, `26 of 26` | asserted, each in its own script |
| **V6** | G-RULE | `READING RULE: PASS - 7 of 7` | asserted by the checker |
| **V7** | G-HISTORY and DETERMINISM | `20 of 20 equal`; `19,434` bytes, `99e6a47d…` | the 20 asserted by `adv3.py` (exit 1 on any DIFFERENT); the bytes and hash recorded, not asserted — compared by the Executor, equal |
| **V8** | B-DEPLOY | `exit=0`; the mark printed | the chain's `&&` stops at the first failure; `exit` recorded |
| **V9** | COPY | `READING COPY: PASS - 5 of 5` | asserted by the checker |
| **V10** | G-RENDER | `READING RENDER: PASS - 10 of 10`; the message 3,499 characters, the report 13,348 bytes | asserted by the checker |
| **V11** | P-START | `READING P-START: served - 5 of 5 endpoints`, each line printed | asserted by `adv3-bot.py --probe` |
| **V12** | B-KILL and UNIT-NEW | `exit=0`; `READING UNIT-NEW: PASS - 9 of 9`; pids `3404850`, `3574987`; instants 08:36:43.719500 and 08:37:13 UTC | UNIT-NEW asserted by the checker; `mark kill` asserted `daily-sent`; B-KILL's `exit` recorded |
| **V13** | contract §4.2's self-check | `0`; three files; nothing | recorded, not asserted |
| **V14** | §3.7's closing reads | every read printed, §2.9 | recorded, not asserted — no threshold |
| **V15** | B-RECLAIM-SCRATCH and §9's `keep` | reclaim: 4 files considered, 0 copied, store 2,205 → 2,205; keep: §2.15 | asserted by `reclaim` and `keep` (the store's count) |
| **V16** | §9's removals | §2.15 | exit codes recorded, not asserted |

---

## 6. What could not be implemented as written

1. **B-RECLAIM-SCRATCH's first removal was refused, then re-issued.** The Executor first ran three removals in one
   command, a loop over shell variables (`rm -rf $D/$u`); Claude Code's built-in safety check refused it before it ran —
   a target built from variables could expand to `/` — and named a literal absolute path as the form it allows. Each of
   the eleven removals then ran as its own command, `rm -rf` and `test -e` of one literal path, which is §3.3's own form;
   none was refused, none was handed to the Boss. The refused command wrote nothing.
2. **Timing wrappers.** G-HISTORY ran as `timeout 1800 /usr/bin/time -v nice -n 19 /root/tz04a-env/venv/bin/python -B …
   --history …`, and `I render` under `/usr/bin/time -f …`, for the host peaks map §7 item 131 asks a later floor to
   take. The command under test and its arguments are the TZ's.
3. **The logs' names.** `NN` in B-DEPLOY's and B-KILL's blocks became `14` and `17`; every step's log is numbered in
   this TZ's order, `00-mkdir.log` written after the `mkdir` from its captured output. Logs this TZ does not name:
   `07-commit-push.log`, `08-pull-request.log`, `20-service-log-stamps.log`, `21-separation.log` and
   `22-files-written.log`. Each is kept by `I keep`.
4. **Contract §1.** Step 1 as `git pull origin main`, a fast-forward of four commits; before §0.0's `mkdir` the Executor
   read the repository's listing, `git log`, the map's revision line and section headings, `ls` of
   `/var/lib/btc-recorder`, `/root`, `/root/adv3-bot-svc` and `/var/lib/adv3-bot` (names and sizes) and `date`. Step 2:
   this TZ in full; the map in the sections the TZ rests on — §0, §1, §2.6, §2.7, §6's rows and §7 items 124 to 133 — not
   every line; the fingerprint read every row.
5. **Reads no step names**, none under `/etc/adv3-bot/` and none printing a coin, a price or a size from the live
   message: `get_session` for the model; `cmp` of `/etc/systemd/system/adv3-bot.service` against the repository's
   (equal); `ps` and `/proc` of the history process, and one background watch that probed it with `kill -0`, which
   delivers no signal, stopped by the Executor and replaced by a `test -d /proc/…` watch; `gh auth status`, `gh pr
   list`, `gh pr view`; `git status` of the worktree; the TZ file's hash and the refs' counts; `grep -c '"kind":
   "daily"'` of `journal.jsonl`, `3`, a count the marks also read; and §2.9's `grep` of `service.log`'s stamped and
   exception lines, to place the traceback its tail opens in.
6. **The first memory read.** §0.3's printed `grep` read `MemAvailable` `158,494,720` bytes at 08:29:04, under §0.4's
   floor `170,344,448`; `I host`'s memory gate, the read the TZ asserts, read `189,366,272` seconds later and passed. The
   TZ puts the floor on the checker's read and no threshold on the printed one; the Executor went on on the gate's
   reading. Every later read was above the floor (§0.5).
7. **The commit message and the pull request's text** are the Executor's own.
8. **The report** was written by hand with its logs inlined from their files by a substitution in the primary
   checkout, so no log line was retyped; `logs/22-files-written.log` hashes itself while being written (§2.11).
   B-RECLAIM-OWN's output, which no file holds, was typed into §2.15 from the session; its 27 `K copied` lines were then
   compared with `sha256sum` of the store's 27 copies, equal.
9. **B-RECLAIM-OWN in two calls**, a `date -u` before each: `keep` and `git worktree remove`, then the rest, every
   command §9's and in its order.

Nothing else: every gate was read by the checker's, the bot's or `adv3.py`'s own modes on Appendix A's bytes.
