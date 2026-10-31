# TZ-37 report — trigger commands and capital allocation: «сигнал 10000 топ 3» divides a budget among the STRONG trades that qualify, within the risk limits

**NUMBER PASS: 2 of 2** at §0.5 (13:16:52 UTC) and again at §3.1 (13:17:11 UTC): `CryptoTZ/` holds `TZ-37-capital-allocation.md` and no other `TZ-37-` file, `CryptoReports/` no `TZ-37-` report; the branch count `0` before the push.
**G-RULE PASS: 7 of 7** — `handle`, `journal`, `selftest` changed; `correlation`, `liquidity`, `numbers`, `plan`, `plan_parts`, `returns_of`, `route` added; `parse` removed; the 13 others identical by `ast.dump`; `adv3.py`, `selftest-adv3.py`, `RULE-ADV-3.txt` and the unit `main`'s byte for byte · **SELFTESTS: 44 of 44, 67 of 67, 50 of 50**.
**B-DEPLOY `exit=0`** (mark 13:54:46.305714 UTC) · **COPY PASS: 5 of 5** · **G-RENDER PASS: 16 of 16** on live data — the report held **3 STRONG coins**; trades placed per allocation **2, 2, 2** («сигнал 10000 топ 3», «сигнал 15000 топ 5», «сигнал 10000») · **P-START: served - 5 of 5 endpoints**.
**B-KILL `exit=0`** (mark 13:58:13.720225 UTC) · **UNIT-NEW PASS: 9 of 9** — pid `3574987` → `3616193`, started 13:58:43 UTC, `NRestarts` 1 → 2; the three capture units unchanged (`2388318`/0, `3530053`/15, `3137952`/1).
**No rollback ran**: B-ROLLBACK, B-KILL2, UNIT-OLD, K-37 and `stopped` were not run, no gate failed.
**The unit runs the new code**: `adv3-bot.service` `active`, `running`, `enabled`, pid `3616193`, `/root/adv3-bot-svc/adv3-bot.py` `3a044d50…`, `commit.txt` `6d70c6aaa5457365743d2fb80e13e0817af8d292` — verified by `I unit new`, read twice (13:58:58 in the Boss's block and 13:59:12 by the Executor), and by §3.6's `systemctl show`, `is-enabled`, `journalctl` and `service.log`, never from the Boss's account. The day's message was not sent again: `daily-sent` `2026-10-31` and 3 `daily` records at both marks and after.
**Three blocks were refused by Claude Code's auto mode classifier and run by the Boss** in his login, each verified by the Executor from its log and the host: B-RECLAIM-SCRATCH (13:45:28 UTC), B-DEPLOY (13:54:46 UTC) and B-KILL with UNIT-NEW's timed reads (13:58:13 UTC). None was retried by the Executor in another form (§6 item 1).
**Departures, all in §6:** the three refused blocks; a timing wrapper on G-RENDER; the logs' names; reads no step names; the map read in sections.

| field | value |
|---|---|
| TZ | `CryptoTZ/TZ-37-capital-allocation.md`, 2,246 lines, 185,683 bytes, SHA-256 `93ce25fa28cda7923443e59adf5952a48aec95269ad3c6b822fe76310f6cb1e8`, landed at `ee2ec2b` (2026-10-31 13:10:08 UTC); the map's revision `2026-10-31-a` landed after it at `0e987e1` (13:12:23 UTC) |
| map revision | `2026-10-31-a`, equal; anchors 6 of 6; re-derived 4 of 4; rows 56; `frozen` equal 53 of 53; the map 1,971 lines, 478,552 bytes, SHA-256 `a164eb530a1d8188312e864e8256cc9405346c68e21e98b7f9cd077ebb7046ef`, the file TZ-37 §10 names |
| executor model | the model the TZ header names: `get_session` read `configured_model`, `session_context.model` and `external_metadata.last_served_model` all `claude-opus-5-5` |
| branch | `tz-37-capital-allocation` at `6d70c6aaa5457365743d2fb80e13e0817af8d292`, on `origin/main` `0e987e1`; pushed; pull request #37, open, not merged |
| service's code | `/root/adv3-bot-svc/`: `adv3-bot.py` `3a044d50…` (was `e65de91c…`), `adv3.py` `d73a657e…` unchanged, `commit.txt` `6d70c6aaa5457365743d2fb80e13e0817af8d292` (was `444628905625…`) |
| unit | `/etc/systemd/system/adv3-bot.service` `82acd8e4…`, unchanged; never reloaded |
| interpreter | `/root/tz04a-env/venv/bin/python` 3.12; every session mode under `nice -n 19` and `-B` |
| marks | `deploy` 13:54:46.305714 UTC · `kill` 13:58:13.720225 UTC (`state.json`) |
| blocks | B-RECLAIM-SCRATCH: refused to the Executor about 13:19 UTC, run by the Boss 13:45:28 – 13:45:29 UTC · B-DEPLOY: refused to the Executor about 13:46:20 UTC, run by the Boss 13:54:46 UTC · B-KILL: refused to the Executor as "[Production Deploy]" about 13:56:35 UTC, run by the Boss 13:58:13 UTC with UNIT-NEW's reads 13:58:58 UTC · B-RECLAIM-OWN: §2.14 |
| work tree | `/root/tz37-work/`, created 13:16:07 UTC, removed by B-RECLAIM-OWN (§2.14) |

---

## 0. Fingerprint

`I fingerprint`, from the staged copy of the checker, against the primary checkout at `0e987e1` — revision
`2026-10-31-a`; anchors `A1` `229a944f2d51`, `A2` `6c5089330629`, `A3` `0-complete / 1-student-5tau-not-disqualified /
2-no-edge-4tau-240-undecidable`, `A4` `437b45ea196b`, `A5` `0f6c90451cbd`, `A6` `729f0bcdbee3`, each equal to the TZ
header's; `A2`, `A4`, `A5` and `A6` re-derived. **V1: `READING FINGERPRINT: PASS - 65 of 65`.** The map, the `reported`
row: 1,971 lines, 478,552 bytes, SHA-256 `a164eb530a1d8188312e864e8256cc9405346c68e21e98b7f9cd077ebb7046ef`.

### 0.1 The 56 rows of the map's §0 table

The table below is built from `logs/03-fingerprint.log` by a substitution, each `frozen` row compared with the map's.

| path | lines | bytes | state | SHA-256 | against the map |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 1,971 | 478,552 | reported | `a164eb530a1d8188312e864e8256cc9405346c68e21e98b7f9cd077ebb7046ef` | — |
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
| `research/tz36-advisor-trust.py` | 582 | 32,925 | frozen | `a0fb9d53afe435d37354862eb8fd299256bf551fdbdb25a5c828d2cc7376d4f5` | equal |
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
| `advisor/adv3.py` | 817 | 43,274 | frozen | `d73a657ef31decad276b858c4ec9672dce1c1c5cec36f0bb1c5b3378838224a8` | equal |
| `advisor/adv3-bot.py` | 422 | 19,365 | frozen | `e65de91c7b49c6f932db91e568a5956c005e63119c1cf6fb8724ffb0438d1dcb` | equal |
| `advisor/selftest-adv3.py` | 201 | 12,600 | frozen | `ef4ffc44e6f8bcdd5685fc1db9090957890c6e2ab762cdad8ae9826b18cf1395` | equal |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | — |

### 0.2 `logs/03-fingerprint.log`, verbatim (V1)

```
2026-10-31T13:16:29.348819457Z
reported 1971 lines 478552 bytes a164eb530a1d8188312e864e8256cc9405346c68e21e98b7f9cd077ebb7046ef SYSTEM-MAP.md
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
frozen   582 lines 32925 bytes a0fb9d53afe435d37354862eb8fd299256bf551fdbdb25a5c828d2cc7376d4f5 research/tz36-advisor-trust.py
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
frozen   817 lines 43274 bytes d73a657ef31decad276b858c4ec9672dce1c1c5cec36f0bb1c5b3378838224a8 advisor/adv3.py
frozen   422 lines 19365 bytes e65de91c7b49c6f932db91e568a5956c005e63119c1cf6fb8724ffb0438d1dcb advisor/adv3-bot.py
frozen   201 lines 12600 bytes ef4ffc44e6f8bcdd5685fc1db9090957890c6e2ab762cdad8ae9826b18cf1395 advisor/selftest-adv3.py
tracked  5 lines 252 bytes 9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b .gitignore
ok   revision 2026-10-31-a
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
ok   frozen research/tz36-advisor-trust.py
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
ok   the table holds 56 rows, 53 frozen, 2 tracked, 1 reported
READING FINGERPRINT: PASS - 65 of 65
exit=0
```

### 0.3 Contract §1, §0.0 and §0.1 — the start-up, the work tree and the files staged (V4)

Contract §1 step 1: `git fetch origin` and `git pull --ff-only origin main` on `main`, a fast-forward from `a3affbb` to
`0e987e1` — `a5c66a1` (PR #36's merge), `ee2ec2b` (this TZ) and `0e987e1` (the map) among the commits. Step 2: this TZ in
full; the map in the sections the TZ rests on (§6 item 4). Steps 3 and 4: `I fingerprint`, §0.2. Step 5: the model, the
field table.

`logs/01-work-tree.log`, written after the `mkdir` from its captured output:

```
2026-10-31T13:16:07.332078003Z
$ mkdir /root/tz37-work /root/tz37-work/logs; echo "exit=$?"
exit=0
```

`logs/02-stage.log` — §0.1's script, verbatim, over an empty `stage/` (lines, bytes and SHA-256 equal to §0.1's table):

```
2026-10-31T13:16:21.229067676Z
/root/tz37-work/stage/advisor/adv3-bot.py 798 49783 3a044d50f51b16563b99bf1514ef92f35a9795b1fcc377aea6be4c23a31f7af2
/root/tz37-work/stage/research/tz37-capital-allocation.py 808 51269 eec1f30b971ed1d6db31e27eb0c321276c1b107a1654e013996d023b1a6a04eb
exit=0
```

### 0.4 Host gate — §0.3's block, verbatim (V2)

`S` was `/tmp/claude-0/-root-btc-5m-twap/f13dd443-b053-5e1f-ab49-f3593ec7b06b/scratchpad`, the scratchpad the session's
system prompt names. `logs/04-host.log`:

```
Sat Oct 31 01:16:39 PM UTC 2026
1793452599
2026-08-02 07:24:32
1
MemTotal:         978640 kB
MemAvailable:     133208 kB
SwapTotal:       3174396 kB
SwapFree:        2388328 kB
units: {"adv3-bot.service": {"ActiveState": "active", "MainPID": "3574987", "NRestarts": "1", "SubState": "running", "UnitFileState": "enabled"}, "btc-pairbook.service": {"ActiveState": "active", "MainPID": "3530053", "NRestarts": "15", "SubState": "running", "UnitFileState": "enabled"}, "btc-recorder.service": {"ActiveState": "active", "MainPID": "2388318", "NRestarts": "0", "SubState": "running", "UnitFileState": "enabled"}, "btc-rewardbook.service": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1", "SubState": "running", "UnitFileState": "enabled"}}
MemAvailable first 148074496 bytes, second not read, deciding 148074496; /dev/vda2 free 10585903104 bytes
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
ok   H5 adv3.py is TZ-36's and adv3-bot.py is TZ-35's
ok   H5 the installed unit file is TZ-35's
ok   H5 commit.txt is 40 hex characters and a newline
ok   H6 the record holds daily-sent and a journal of whole lines
ok   memory gate: MemAvailable at least 130981888 bytes, a first read below it read again after 60 s
ok   disk gate: /dev/vda2 free at least 7400000000 bytes
READING HOST: PASS - 16 of 16
exit=0
NEXT                            LEFT LAST                         PASSED UNIT                         ACTIVATES
Sat 2026-10-31 17:34:37 UTC 4h 17min Fri 2026-10-30 22:50:03 UTC 14h ago apt-daily.timer              apt-daily.service
Sun 2026-11-01 01:30:20 UTC      12h Sat 2026-10-31 01:30:20 UTC 11h ago btc-rewardbook-archive.timer btc-rewardbook-archive.service
Sun 2026-11-01 03:00:20 UTC      13h Sat 2026-10-31 03:00:20 UTC 10h ago btc-pairbook-archive.timer   btc-pairbook-archive.service
Sun 2026-11-01 06:59:49 UTC      17h Sat 2026-10-31 06:38:15 UTC  6h ago apt-daily-upgrade.timer      apt-daily-upgrade.service

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
total 76
drwxr-xr-x  2 root root  4096 Oct 31 08:36 .
drwx------ 31 root root  4096 Oct 31 13:16 ..
-rw-r--r--  1 root root 19365 Oct 29 14:31 adv3-bot.py
-rw-r--r--  1 root root 43274 Oct 31 08:36 adv3.py
-rw-r--r--  1 root root    41 Oct 31 08:36 commit.txt

/var/lib/adv3-bot:
total 28
drwx------  2 root root 4096 Oct 31 09:30 .
drwxr-xr-x 65 root root 4096 Oct 29 14:35 ..
-rw-r--r--  1 root root   10 Oct 31 06:00 daily-sent
-rw-r--r--  1 root root 5181 Oct 31 06:00 journal.jsonl
-rw-r--r--  1 root root    9 Oct 31 09:30 offset
-rw-r--r--  1 root root 4011 Oct 31 09:30 service.log
443287556	/var/lib/btc-rewardbook
714553585	/var/lib/btc-pairbook
9211	/var/lib/adv3-bot
16	/root/.claude
2232
/root/btc-5m-twap       0e987e1 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/tmp/claude-0/-root-btc-5m-twap/f13dd443-b053-5e1f-ab49-f3593ec7b06b/scratchpad
total 28
drwx------  7 root root 4096 Oct 31 13:14 .
drwx------ 35 root root 4096 Oct 31 13:14 ..
drwx------  3 root root 4096 Oct 31 08:27 0bf93b31-e4ab-4a54-9db3-a06f592b7731
drwx------  3 root root 4096 Oct 30 13:16 238335b9-cf23-414a-8e8f-ad4705c4d19e
drwx------  3 root root 4096 Oct 31 13:14 50f7dcda-5a03-4e54-8f23-a03fd054d0b0
drwx------  4 root root 4096 Oct 31 08:27 84903452-8bf4-53c5-8169-67946f6e03f0
drwx------  4 root root 4096 Oct 31 13:14 f13dd443-b053-5e1f-ab49-f3593ec7b06b
```

**V2: `READING HOST: PASS - 16 of 16`.** The forensic store held `2,232` files, map §3's count; the worktrees were map §3's
two; the session directories beside this one were the two TZ-36 left, `0bf93b31…` and `84903452…`, the live
`238335b9…`, and `50f7dcda…`, born at 13:14:02 UTC with this session's own process (§2.3).

### 0.5 Free space and `MemAvailable` — every read, its instant and its bound

| instant (UTC) | read | value, bytes | bound | |
|---|---|---|---|---|
| 13:16:39 | §0.3's printed `grep` of `/proc/meminfo`, `MemAvailable` | 136,404,992 (`133208 kB`) | — (no threshold on the printed read) | above the floor |
| 13:16:40 | `I host`'s memory gate, first read — **the read the TZ asserts** | 148,074,496 | ≥ 130,981,888 | PASS; no second read |
| 13:16:40 | `I host`'s disk gate, `/dev/vda2` free | 10,585,903,104 | ≥ 7,400,000,000 | PASS |
| 13:55:46 | `/proc/meminfo` before G-RENDER (§2.5) | 185,798,656 (`181444 kB`) | — | |
| 13:55:46 – 13:56:00 | G-RENDER's peak resident set, `/usr/bin/time -v` | 58,953,728 (`57572 kB`) | §0.4's peak `65,490,944` | below it |
| 13:59:19 | §3.6's `free -b`, available | 246,722,560 | — | |
| 13:59:19 | §3.6's `df`, `/dev/vda2` free | 10,508,689,408 | — | |
| 14:03:50 | B-RECLAIM-OWN's `df`, `/dev/vda2` free (§2.14) | 10,516,705,280 | — | |

### 0.6 Refs and the number (§0.5) — `logs/05-refs-number.log`, verbatim (V3)

```
2026-10-31T13:16:52.120801660Z
fetch exit=0
0e987e1704dc0edfe6a45ff1b59baf8d73fc1e32	HEAD
0e987e1704dc0edfe6a45ff1b59baf8d73fc1e32	refs/heads/main
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
0
CryptoTZ/TZ-37-capital-allocation.md
ok   CryptoTZ/ holds CryptoTZ/TZ-37-capital-allocation.md and no other file of that number
ok   CryptoReports/ holds no report of that number
READING NUMBER: PASS - 2 of 2
exit=0
0e987e1 2026-10-31T17:12:23+04:00 Update SYSTEM-MAP.md

M	SYSTEM-MAP.md
ee2ec2b 2026-10-31T17:10:08+04:00 Add files via upload

A	CryptoTZ/TZ-37-capital-allocation.md
a5c66a1 2026-10-31T13:03:56+04:00 Merge pull request #36 from seahomebatumi-ai/tz-36-advisor-trust-block

M	advisor/adv3.py
M	advisor/selftest-adv3.py
A	research/tz36-advisor-trust.py
a3affbb 2026-10-31T08:42:09+00:00 TZ-36 report: the advisor's card says what it rests on - NUMBER 2 of 2 twice; G-RULE 7 of 7; SELFTESTS 44, 19 and 26; G-HISTORY 20 of 20, history.json 99e6a47d; B-DEPLOY, COPY 5 of 5, G-RENDER 10 of 10, P-START 5 of 5; B-KILL and UNIT-NEW 9 of 9, pid 3404850 to 3574987; no rollback; the unit runs d73a657e

A	CryptoReports/TZ-36-advisor-trust-block-report.md
369d1fa 2026-10-31T12:25:02+04:00 Add files via upload

A	CryptoTZ/TZ-36-advisor-trust-block.md
```

The branch count `0`; **`READING NUMBER: PASS - 2 of 2`**. Map §1's record of the refs, read on 2026-10-29 at 15:25 UTC,
holds thirteen branches with `main` at `20a5aa1`; read here, fourteen — `refs/heads/tz-36-advisor-trust-block` added at
`4446289` — with `main` at `0e987e1`, 35 pull-request heads (`refs/pull/36/head` at `4446289` among them) and the archives'
tags of the days since (7 `rewardbook-streams-*`, 34 `pairbook-streams-*`). Recorded, not blocking: `main` carries revision
`2026-10-31-a`. **This TZ and the map
landed in two uploads, `ee2ec2b` and `0e987e1`, two minutes apart**, where the TZ's header names one upload carrying
both; recorded, not blocking (§2.13).

---

## 1. Input

| input | read | size / count | hash |
|---|---|---|---|
| this TZ | `CryptoTZ/TZ-37-capital-allocation.md` at `0e987e1`, Appendix A extracted twice by §0.1's script | 2,246 lines, 185,683 bytes; 2 files | `93ce25fa…`; `3a044d50…`, `eec1f30b…` |
| the map | `SYSTEM-MAP.md` revision `2026-10-31-a` and the 55 files its table hashes | 1,971 lines, 478,552 bytes; 56 rows | `a164eb53…`; §0.1 |
| `origin/main`'s files G-RULE reads | `advisor/adv3-bot.py`, `adv3.py`, `selftest-adv3.py`, `RULE-ADV-3.txt`, `deploy/systemd/adv3-bot.service`, by `git show` | 5 files | `e65de91c…`, `d73a657e…`, `ef4ffc44…`, `ee206e7c…`, `82acd8e4…` |
| the live market, by the service copy's bot (G-RENDER) | `fapi.binance.com`'s closed daily candles, funding, marks, funding intervals and the 8-day klines of the STRONG coins, 13:55:46 – 13:56:00 UTC | 42 coins; 4 reports; 3 STRONG coins' volumes per allocation | not stored but in `render-state/journal.jsonl`, scratch, 6,322 bytes, `4f753698…`, never printed, removed with the tree |
| P-START | five endpoints, one request each, 13:56:10 – 13:56:13 UTC | 1,499 candles of BTCUSDT; 5 settlement days; 945 marks; 820 intervals; `getMe` | — |
| the bot's record | `/var/lib/adv3-bot/daily-sent`, `journal.jsonl` (hashed by `I render`, counted by the marks), `service.log` (read by `I unit`, tailed by §3.6) | 10, 5,181 and 4,011 → 4,108 bytes | unchanged but `service.log` |

**Nothing was re-collected.** This TZ measures nothing about the market: the live render proves the routing, the
replies' shape and the limits on the day's report.

---

## 2. Measurements

### 2.1 §3.1 — the branch and its files (V3, V4)

`logs/06-branch.log`:

```
2026-10-31T13:17:11.642738876Z
fetch exit=0
CryptoTZ/TZ-37-capital-allocation.md
ok   CryptoTZ/ holds CryptoTZ/TZ-37-capital-allocation.md and no other file of that number
ok   CryptoReports/ holds no report of that number
READING NUMBER: PASS - 2 of 2
exit=0
Preparing worktree (new branch 'tz-37-capital-allocation')
branch 'tz-37-capital-allocation' set up to track 'origin/main'.
HEAD is now at 0e987e1 Update SYSTEM-MAP.md
exit=0
```

`logs/07-extract-wt.log` — §0.1's script again, verbatim but for its argument `/root/tz37-work/wt`; the same lines, bytes and
SHA-256 as §0.2's; it overwrote the committed bot only after asserting it TZ-35's by hash:

```
2026-10-31T13:17:23.155157294Z
/root/tz37-work/wt/advisor/adv3-bot.py 798 49783 3a044d50f51b16563b99bf1514ef92f35a9795b1fcc377aea6be4c23a31f7af2
/root/tz37-work/wt/research/tz37-capital-allocation.py 808 51269 eec1f30b971ed1d6db31e27eb0c321276c1b107a1654e013996d023b1a6a04eb
exit=0
add exit=0
M	advisor/adv3-bot.py
A	research/tz37-capital-allocation.py
405	29	advisor/adv3-bot.py
808	0	research/tz37-capital-allocation.py
M  advisor/adv3-bot.py
A  research/tz37-capital-allocation.py
```

`--name-status` exactly `M` for the bot and `A` for the checker; `--numstat` exactly `405	29	advisor/adv3-bot.py` and
`808	0	research/tz37-capital-allocation.py`, as §3.1 requires. `logs/08-commit-push.log` (the remote's URL printed by no line;
the push went through the URL's own credential, `gh`'s route not needed):

```
2026-10-31T13:17:38.652980252Z
commit exit=0
6d70c6aaa5457365743d2fb80e13e0817af8d292 2026-10-31T13:17:38+00:00 TZ-37: trigger commands and capital allocation - advisor/adv3-bot.py replaced, research/tz37-capital-allocation.py added
 advisor/adv3-bot.py                 | 434 +++++++++++++++++--
 research/tz37-capital-allocation.py | 808 ++++++++++++++++++++++++++++++++++++
 2 files changed, 1213 insertions(+), 29 deletions(-)
0e987e1704dc0edfe6a45ff1b59baf8d73fc1e32	refs/heads/main
remote: 
remote: Create a pull request for 'tz-37-capital-allocation' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-37-capital-allocation        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-37-capital-allocation -> tz-37-capital-allocation
branch 'tz-37-capital-allocation' set up to track 'origin/tz-37-capital-allocation'.
push exit=0
```

`logs/09-pull-request.log`:

```
2026-10-31T13:17:55.065624243Z
https://github.com/seahomebatumi-ai/btc-5m-twap/pull/37
pr exit=0
{"baseRefName":"main","headRefOid":"6d70c6aaa5457365743d2fb80e13e0817af8d292","number":37,"state":"OPEN","url":"https://github.com/seahomebatumi-ai/btc-5m-twap/pull/37"}
```

### 2.2 §3.2 — the self-tests and G-RULE (V5, V6): **44 of 44, 67 of 67, 50 of 50; RULE 7 of 7**

`logs/10-selftest-adv3.log`:

```
2026-10-31T13:18:08.954284591Z
SELFTEST-ADV3 PASS: 44 of 44 checks passed
exit=0
wall .156712546 s
```

`logs/11-selftest-bot.log`:

```
2026-10-31T13:18:09.115952006Z
SELFTEST PASS: 67 of 67 checks passed
exit=0
wall .256811092 s
```

`logs/12-selftest-checker.log`:

```
2026-10-31T13:18:09.376378257Z
SELFTEST PASS: 50 of 50 checks passed
exit=0
wall .059926839 s
```

`logs/13-rule.log`:

```
2026-10-31T13:18:09.439081538Z
ok   adv3.py is main's, byte for byte, and hashes to TZ-36's
ok   selftest-adv3.py is main's, byte for byte, and hashes to TZ-36's
ok   RULE-ADV-3.txt is main's, hashes to the RULE constant and is adv3.py's
ok   the unit file is main's, byte for byte, and hashes to TZ-35's
ok   the functions and classes that changed are exactly ['handle', 'journal', 'selftest']
ok   the added are exactly ['correlation', 'liquidity', 'numbers', 'plan', 'plan_parts', 'returns_of', 'route'] and the removed are ['parse']
ok   the 13 others are identical by AST and the constants differ as named
READING RULE: PASS - 7 of 7
exit=0
wall .092044938 s
```

The wall times are `date` arithmetic around each command, not a measurement the TZ asks for. The worktree's
`git status --porcelain --ignored` printed nothing after the four: the bot's self-test removed its `.selftest-*`
directories.

### 2.3 §3.3 — the directories beside this session, and B-RECLAIM-SCRATCH (V14)

`logs/14-scratch.log` — TZ-35's `scratch`, with `"$(dirname "$S")"` the session's own directory `f13dd443…`:

```
2026-10-31T13:18:18.146058879Z
running 3435609 started 2026-10-30T13:15:54.700000Z claude
running 3435619 started 2026-10-30T13:15:56.710000Z claude
running 3435628 started 2026-10-30T13:15:58.010000Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
running 3435667 started 2026-10-30T13:16:00.220000Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
running 3435954 started 2026-10-30T13:18:48.500000Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
running 3609936 started 2026-10-31T13:14:01.770000Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
0bf93b31-e4ab-4a54-9db3-a06f592b7731 born 2026-10-31T08:27:38.000000Z: earlier
238335b9-cf23-414a-8e8f-ad4705c4d19e born 2026-10-30T13:16:00.000000Z: live, process [3435609, 3435619, 3435628, 3435667]
50f7dcda-5a03-4e54-8f23-a03fd054d0b0 born 2026-10-31T13:14:02.000000Z: live, process [3609936]
84903452-8bf4-53c5-8169-67946f6e03f0 born 2026-10-31T08:27:39.000000Z: earlier
exit=0
```

Two directories **earlier**, `0bf93b31-e4ab-4a54-9db3-a06f592b7731` and `84903452-8bf4-53c5-8169-67946f6e03f0` — map §3's
two — and two **live**: `238335b9…`, the remote-control session of 2026-10-30 that is no TZ's, and `50f7dcda…`, born at
13:14:02 UTC with this session's process `3609936`. Neither live directory nor this session's own was touched.

**The Executor's `reclaim` was refused by Claude Code's auto mode classifier**, which gave no explanation, before it ran.
`logs/15a-reclaim-refused.log`:

```
2026-10-31T13:19:10.722800574Z B-RECLAIM-SCRATCH: the Executor's reclaim of the two earlier directories was refused by the Claude Code auto mode classifier (no explanation given) before it ran; handed to the Boss as one exact block (TZ-37 §3.3, map §6 sandbox limit). Command refused:
nice -n 19 /root/tz04a-env/venv/bin/python -B /root/btc-5m-twap/research/tz35-advisor-deploy.py reclaim /tmp/claude-0/-root-btc-5m-twap/0bf93b31-e4ab-4a54-9db3-a06f592b7731 /tmp/claude-0/-root-btc-5m-twap/84903452-8bf4-53c5-8169-67946f6e03f0
```

By §3.3's route the block went to the Boss: one `reclaim` naming both directories, then one `rm -rf` and one `test -e` a
directory, each removal gated on `RECLAIM PASS` in the log. He ran it in his login. `logs/15-reclaim-scratch.log`, its
first line opening with his terminal's OSC 133 prompt marker, shown as `cat -v` shows it:

```
^[]133;C^G2026-10-31T13:45:28.969650248Z
reclaim: 3512 report tokens; forensic store holds 2232 files
RECLAIM PASS: 5 files considered, 0 named by a report, 0 kept by name, 0 copied, 0 already held; forensic store 2232 -> 2232 files
exit=0
2026-10-31T13:45:29.131206958Z
exit=0
exit=1
2026-10-31T13:45:29.134454467Z
exit=0
exit=1
```

`logs/15b-reclaim-by-boss.log`:

```
2026-10-31T13:46:47.702830932Z B-RECLAIM-SCRATCH run by the Boss in his login at 2026-10-31T13:45:28 UTC (15-reclaim-scratch.log; its first line carries his terminal's OSC 133 marker); verified by the Executor in 16-reclaim-verify.log.
```

The Executor's own verification, `logs/16-reclaim-verify.log`:

```
2026-10-31T13:46:08.284909657Z
log: ^[]133;C^G2026-10-31T13:45:28.969650248Z
log: reclaim: 3512 report tokens; forensic store holds 2232 files
log: RECLAIM PASS: 5 files considered, 0 named by a report, 0 kept by name, 0 copied, 0 already held; forensic store 2232 -> 2232 files
log: exit=0
log: 2026-10-31T13:45:29.131206958Z
log: exit=0
log: exit=1
log: 2026-10-31T13:45:29.134454467Z
log: exit=0
log: exit=1
test -e 0bf93b31 exit=1
test -e 84903452 exit=1
2232
total 20
drwx------  5 root root 4096 Oct 31 13:45 .
drwx------ 35 root root 4096 Oct 31 13:14 ..
drwx------  3 root root 4096 Oct 30 13:16 238335b9-cf23-414a-8e8f-ad4705c4d19e
drwx------  3 root root 4096 Oct 31 13:14 50f7dcda-5a03-4e54-8f23-a03fd054d0b0
drwx------  4 root root 4096 Oct 31 13:14 f13dd443-b053-5e1f-ab49-f3593ec7b06b
```

**V14 (scratch):** `RECLAIM PASS` before any removal; 5 files considered, 0 named by a report, 0 kept by name, 0 copied, 0
already held; the store `2,232` → `2,232`, read again by `find`; each `rm -rf` `exit=0` and `test -e` `exit=1`, and the
Executor's `test -e` `exit=1` for both.

### 2.4 §3.4 — B-DEPLOY (V7)

At 13:46:08 UTC, second `49,568` of the day, inside the band of `23,700` to `85,500`. **The Executor's run of the block,
verbatim with `NN` `17`, was refused by the classifier**, which gave no explanation, before it ran: no mark, no
`bot.before`, the service copy's bot still `e65de91c…`. `logs/17a-b-deploy-refused.log`:

```
2026-10-31T13:46:47.701456947Z B-DEPLOY: the Executor's run of §3.4's block, verbatim with NN=17, was refused by the Claude Code auto mode classifier (no explanation given) at about 13:46:20 UTC, before it ran: no mark, no state.json, no bot.before, no 17-b-deploy.log, /root/adv3-bot-svc/adv3-bot.py still e65de91c7b49c6f932db91e568a5956c005e63119c1cf6fb8724ffb0438d1dcb. Handed to the Boss as the TZ's block (§0.0, map §6 sandbox limit).
```

The Boss ran the block verbatim. `logs/17-b-deploy.log`:

```
2026-10-31T13:54:46.255087017Z
mark deploy at 2026-10-31T13:54:46Z: bot pid 3574987 NRestarts 1, daily-sent 2026-10-31, 3 daily records
exit=0
```

`logs/17b-b-deploy-by-boss.log`:

```
2026-10-31T13:55:37.819100436Z B-DEPLOY run by the Boss in his login at 2026-10-31T13:54:46 UTC (17-b-deploy.log); verified by the Executor in 18-copy.log.
```

**V7: `exit=0`; the mark `deploy` at 13:54:46 UTC** (`state.json` `t` `1793454886.3057144`), bot pid `3574987`,
`NRestarts` `1`, `daily-sent` `2026-10-31`, 3 daily records. The running process kept the old code until B-KILL.

### 2.5 §3.4 — COPY and G-RENDER (V8, V9): **5 of 5, 16 of 16**

`logs/18-copy.log`:

```
2026-10-31T13:55:37.713444128Z
deploy log: 2026-10-31T13:54:46.255087017Z
deploy log: mark deploy at 2026-10-31T13:54:46Z: bot pid 3574987 NRestarts 1, daily-sent 2026-10-31, 3 daily records
deploy log: exit=0
3a044d50f51b16563b99bf1514ef92f35a9795b1fcc377aea6be4c23a31f7af2  /root/adv3-bot-svc/adv3-bot.py
d73a657ef31decad276b858c4ec9672dce1c1c5cec36f0bb1c5b3378838224a8  /root/adv3-bot-svc/adv3.py
e65de91c7b49c6f932db91e568a5956c005e63119c1cf6fb8724ffb0438d1dcb  /root/tz37-work/bot.before
6d70c6aaa5457365743d2fb80e13e0817af8d292
444628905625809f24dd1fa51159b4093b763789
total 108
drwxr-xr-x  2 root root  4096 Oct 31 13:54 .
drwx------ 31 root root  4096 Oct 31 13:55 ..
-rw-r--r--  1 root root 49783 Oct 31 13:54 adv3-bot.py
-rw-r--r--  1 root root 43274 Oct 31 08:36 adv3.py
-rw-r--r--  1 root root    41 Oct 31 13:54 commit.txt
ok   the service copy holds adv3.py, adv3-bot.py and commit.txt only
ok   adv3.py is unchanged, TZ-36's
ok   adv3-bot.py is Appendix A's
ok   commit.txt is the branch head and the worktree's HEAD
ok   the branch's adv3-bot.py equals the service copy's
READING COPY: PASS - 5 of 5
exit=0
```

`logs/19-render.log` — `timeout 900 I render`, under `/usr/bin/time -v` (§6 item 2), with `/proc/meminfo` read before:

```
2026-10-31T13:55:46.534145598Z
MemAvailable:     181444 kB
replies: 3493 chars in 1 parts, 2557 chars in 2 parts, 2614 chars in 2 parts, 2557 chars in 2 parts, 665 chars in 1 parts, 665 chars in 1 parts; the bot's log: 7 lines; STRONG coins of the report: 3; trades placed: 2, 2, 2
ok   every command answered, no traceback and no failed request in the bot's log
ok   the markup is balanced in every message (b, i)
ok   «сигнал»: the six ratings and the forward book, at most three cards, each with its basis and invalidation, in at most three parts
ok   the allocation's constants are the TZ's: 11.1 % a stop, 5 USDT, 0.1 % of the volume, 1 % and 5 % of risk, three places, 0.1 % a side
ok   each allocation reply is the bot's own plan_parts of the report and liquidity it was made from
ok   plan: only STRONG coins of the report, in rank order, at most n and at most three, none added to fill
ok   plan: every STRONG coin is in the plan or named with a reason, once
ok   plan: every position has an entry and a stop within 11.1 % of it, on current prices
ok   plan: each loss at its stop within 1 % of the budget, all together within 5 %
ok   plan: whole positions of at least 5 USDT, together within the budget, free the budget less them
ok   plan: leverage the rule's formula and at most 20, the margin covering the position, a position within its liquidity cap
ok   the Boss's fields are in every allocation reply: budget, qualifying count, allocated, free, and for each trade capital, leverage, margin, loss at the stop, stop, targets, invalidation, and the note that the sizes are unproven
ok   «сигнал 10000» is the three-trade view and «сигнал 15000 топ 5» says that STRONG is at most three
ok   «помощь» and an unknown text answer HELP and nothing else
ok   the scratch journal holds, in order, request, alloc, alloc, alloc, each allocation record with its plan's figures
ok   the bot's own journal and daily-sent are as before the run
READING RENDER: PASS - 16 of 16
	Command being timed: "nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz37-work/stage/research/tz37-capital-allocation.py render"
	User time (seconds): 2.30
	System time (seconds): 0.11
	Percent of CPU this job got: 17%
	Elapsed (wall clock) time (h:mm:ss or m:ss): 0:13.70
	Average shared text size (kbytes): 0
	Average unshared data size (kbytes): 0
	Average stack size (kbytes): 0
	Average total size (kbytes): 0
	Maximum resident set size (kbytes): 57572
	Average resident set size (kbytes): 0
	Major (requiring I/O) page faults: 11
	Minor (reclaiming a frame) page faults: 13141
	Voluntary context switches: 2071
	Involuntary context switches: 2044
	Swaps: 0
	File system inputs: 7848
	File system outputs: 32
	Socket messages sent: 0
	Socket messages received: 0
	Signals delivered: 0
	Page size (bytes): 4096
	Exit status: 0
exit=0
2026-10-31T13:56:00.250663822Z
```

**V9: `READING RENDER: PASS - 16 of 16`.** The replies, by text in `RENDER_CASES`' order: «сигнал» 3,493 characters in 1
part; «сигнал 10000 топ 3» 2,557 in 2; «сигнал 15000 топ 5» 2,614 in 2; «сигнал 10000» 2,557 in 2; «помощь» and «привет»
665 in 1 each. **The report held 3 STRONG coins; the three allocations placed 2, 2 and 2 trades**, so the limits of checks
(8) to (11) were read on placed positions and not only on an empty plan. The bot's log held 7 lines, none a traceback or
`request failed`. 13.70 s of wall, 2.30 s user and 0.11 s system of processor, peak resident set 57,572 kB. No coin,
price or size of the replies is printed here or in any log (§2 item 7).

### 2.6 §3.5 — P-START (V10): **served - 5 of 5 endpoints**

`logs/20-p-start.log`:

```
2026-10-31T13:56:10.736257775Z
P-KLINES served: 1499 closed daily candles of BTCUSDT, the last 2026-10-30
P-FUNDING served: 5 settlement days of BTCUSDT since 2026-10-27
P-MARKS served: 945 perpetuals, all 42 coins among them with a mark price
P-INTERVALS served: 820 perpetuals with an adjusted funding interval, 42 of the coins among them
P-TELEGRAM served: bot @ClaudeCryptoSignal_bot
READING P-START: served - 5 of 5 endpoints
exit=0
2026-10-31T13:56:13.053305231Z
```

### 2.7 §3.5 — B-KILL and UNIT-NEW (V11): **9 of 9**

At 13:56:35 UTC, inside the band of `23,700` to `85,800`. **The Executor's run of the block, verbatim with `NN` `21`, was
refused by the classifier as "[Production Deploy]"** before it ran: no `kill` mark, the unit at pid `3574987`.
`logs/21a-b-kill-refused.log`:

```
2026-10-31T13:56:48.860880290Z B-KILL: the Executor's run of §3.5's block, verbatim with NN=21, was refused by the Claude Code auto mode classifier as [Production Deploy] at about 13:56:35 UTC, before it ran: no kill mark in state.json (marks: deploy), no 21-b-kill.log, adv3-bot.service MainPID 3574987 NRestarts 1 active since 08:37:13 UTC. Handed to the Boss as the TZ's block (§0.0, map §6 sandbox limit), with UNIT-NEW's timed reads after it in the same block so that §3.5's 45 s / 15 s / 100 s schedule holds.
```

The Boss ran the block verbatim, and after it, in the same paste, UNIT-NEW's reads on §3.5's schedule — at least 45 s after
the mark, then every 15 s while `NOT YET`, at most five runs — gated on `exit=0` in the kill's log. `logs/21-b-kill.log`:

```
2026-10-31T13:58:13.676337550Z
mark kill at 2026-10-31T13:58:13Z: bot pid 3574987 NRestarts 1, daily-sent 2026-10-31, 3 daily records
exit=0
```

`logs/22-unit-new.log`, the first read, 45.1 s after the mark:

```
2026-10-31T13:58:58.771085057Z
bot: pid 3616193 NRestarts 2 started 2026-10-31T13:58:43Z; captures: {"btc-pairbook.service": ["3530053", "15"], "btc-recorder.service": ["2388318", "0"], "btc-rewardbook.service": ["3137952", "1"]}
ok   the unit is active, running and enabled
ok   a new MainPID, one restart more
ok   the process started after the kill mark and within 90 s of it
ok   the process runs the unit's exact argv, alone
ok   the service copy's adv3-bot.py is the new one, and the process started after the copy
ok   the service copy's adv3.py and the unit file are unchanged
ok   the day's message was not sent again: daily-sent and the journal's daily records as before
ok   the log shows the new process serving and no daily sent, no traceback, since the mark
ok   the three capture units unchanged, each active
READING UNIT-NEW: PASS - 9 of 9
exit=0
```

`logs/21b-b-kill-by-boss.log`:

```
2026-10-31T13:59:12.530982129Z B-KILL and UNIT-NEW's timed reads run by the Boss in his login: mark kill 2026-10-31T13:58:13.676 UTC (21-b-kill.log), UNIT-NEW 13:58:58.771 UTC, PASS 9 of 9 at the first read (22-unit-new.log); re-read by the Executor (23-unit-new-verify.log).
```

The Executor's own read, `logs/23-unit-new-verify.log`:

```
2026-10-31T13:59:12.348499405Z
bot: pid 3616193 NRestarts 2 started 2026-10-31T13:58:43Z; captures: {"btc-pairbook.service": ["3530053", "15"], "btc-recorder.service": ["2388318", "0"], "btc-rewardbook.service": ["3137952", "1"]}
ok   the unit is active, running and enabled
ok   a new MainPID, one restart more
ok   the process started after the kill mark and within 90 s of it
ok   the process runs the unit's exact argv, alone
ok   the service copy's adv3-bot.py is the new one, and the process started after the copy
ok   the service copy's adv3.py and the unit file are unchanged
ok   the day's message was not sent again: daily-sent and the journal's daily records as before
ok   the log shows the new process serving and no daily sent, no traceback, since the mark
ok   the three capture units unchanged, each active
READING UNIT-NEW: PASS - 9 of 9
exit=0
```

**V11: B-KILL `exit=0`; `READING UNIT-NEW: PASS - 9 of 9`** at both reads. Pids `3574987` → `3616193`; the mark
13:58:13.720225 UTC, the new process 13:58:43 UTC (`proc_start`, printed to the second), 29 to 30 s after it (`RestartSec=30`); `NRestarts` 1 → 2.

### 2.8 §3.6 — the closing reads (V13)

`logs/24-closing.log`:

```
2026-10-31T13:59:19.170655945Z
MainPID=3616193
Result=success
NRestarts=2
MemoryCurrent=315392
MemoryPeak=19779584
Nice=10
Id=adv3-bot.service
ActiveState=active
ActiveEnterTimestamp=Sat 2026-10-31 13:58:43 UTC

MainPID=2388318
Result=success
NRestarts=0
MemoryCurrent=172478464
MemoryPeak=316174336
Nice=0
Id=btc-recorder.service
ActiveState=active
ActiveEnterTimestamp=Fri 2026-10-23 06:08:56 UTC

MainPID=3530053
Result=success
NRestarts=15
MemoryCurrent=8413184
MemoryPeak=50589696
Nice=0
Id=btc-pairbook.service
ActiveState=active
ActiveEnterTimestamp=Sat 2026-10-31 03:06:30 UTC

MainPID=3137952
Result=success
NRestarts=1
MemoryCurrent=14118912
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
NEXT                        LEFT LAST                         PASSED UNIT                         ACTIVATES
Sun 2026-11-01 01:30:20 UTC  11h Sat 2026-10-31 01:30:20 UTC 12h ago btc-rewardbook-archive.timer btc-rewardbook-archive.service
Sun 2026-11-01 03:00:20 UTC  13h Sat 2026-10-31 03:00:20 UTC 10h ago btc-pairbook-archive.timer   btc-pairbook-archive.service

2 timers listed.
enabled
exit=0
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
2026-10-31T13:58:13+00:00 vultr systemd[1]: adv3-bot.service: Sent signal SIGTERM to main process 3574987 (python) on client request.
2026-10-31T13:58:13+00:00 vultr systemd[1]: adv3-bot.service: Deactivated successfully.
2026-10-31T13:58:13+00:00 vultr systemd[1]: adv3-bot.service: Consumed 1.064s CPU time, 16.5M memory peak, 15.7M memory swap peak.
2026-10-31T13:58:43+00:00 vultr systemd[1]: adv3-bot.service: Scheduled restart job, restart counter is at 2.
2026-10-31T13:58:43+00:00 vultr systemd[1]: Started adv3-bot.service - ADV-3 advisor, the Boss's Binance Futures signals over Telegram.
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
2026-10-31T09:30:57Z help sent
2026-10-31T13:58:43Z serving the pinned chat: pid 3616193 offset 685120812 daily-sent 2026-10-31
/root/adv3-bot-svc:
total 108
drwxr-xr-x  2 root root  4096 Oct 31 13:54 .
drwx------ 31 root root  4096 Oct 31 13:55 ..
-rw-r--r--  1 root root 49783 Oct 31 13:54 adv3-bot.py
-rw-r--r--  1 root root 43274 Oct 31 08:36 adv3.py
-rw-r--r--  1 root root    41 Oct 31 13:54 commit.txt

/var/lib/adv3-bot:
total 32
drwx------  2 root root 4096 Oct 31 09:30 .
drwxr-xr-x 65 root root 4096 Oct 29 14:35 ..
-rw-r--r--  1 root root   10 Oct 31 06:00 daily-sent
-rw-r--r--  1 root root 5181 Oct 31 06:00 journal.jsonl
-rw-r--r--  1 root root    9 Oct 31 09:30 offset
-rw-r--r--  1 root root 4108 Oct 31 13:58 service.log
               total        used        free      shared  buff/cache   available
Mem:      1002127360   755404800    81653760       36864   348172288   246722560
Swap:     3250581504   907198464  2343383040
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10508689408
11248676	/root/tz37-work
93098	/root/adv3-bot-svc
9308	/var/lib/adv3-bot
463553844	/var/lib/btc-rewardbook
757162068	/var/lib/btc-pairbook
16	/root/.claude
{
 "marks": {
  "deploy": {
   "bot": {
    "ActiveState": "active",
    "MainPID": "3574987",
    "NRestarts": "1"
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
   "t": 1793454886.3057144
  },
  "kill": {
   "bot": {
    "ActiveState": "active",
    "MainPID": "3574987",
    "NRestarts": "1"
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
   "t": 1793455093.720225
  }
 }
}
```

The traceback at the head of `service.log`'s last 30 lines is the `getUpdates` read timeout of 01:13:52 UTC that TZ-36
recorded (map §2.7); since the `kill` mark the log holds one line, `serving the pinned chat: pid 3616193`. Both archives
`inactive`, `Result=success`, their next runs 01:30:20 and 03:00:20 UTC on 2026-11-01, unmoved: this TZ reloaded nothing.

### 2.9 Contract §4.2's self-check (V12) — after the push and the pull request, before the report's commit

`logs/25-separation.log`:

```
2026-10-31T13:59:29.581034342Z
fetch exit=0
$ git rev-list origin/main | grep -c 6d70c6aaa5457365743d2fb80e13e0817af8d292
0
$ git diff --name-only origin/main origin/tz-37-capital-allocation
advisor/adv3-bot.py
research/tz37-capital-allocation.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
grep exit=1
0e987e1704dc0edfe6a45ff1b59baf8d73fc1e32
6d70c6aaa5457365743d2fb80e13e0817af8d292
{"headRefOid":"6d70c6aaa5457365743d2fb80e13e0817af8d292","mergedAt":null,"number":37,"state":"OPEN"}
```

`0`; the two implementation files; nothing (`grep` exit `1`).

### 2.10 Every file the run wrote, by SHA-256, but the bot's own root

`logs/26-files-written.log`:

```
2026-10-31T14:00:03.120053758Z
e65de91c7b49c6f932db91e568a5956c005e63119c1cf6fb8724ffb0438d1dcb  ./bot.before
810c9ed61de6850bf05d7530d8b033396e56940a57f994dcefc4f823f2145b3e  ./commit.before
cd781784479f0fca9f4a104195fdbaf8e07d85931851c360b25fbd2eb84cc799  ./logs/01-work-tree.log
a58c6cbf08b5821e726c926758f3f160d682f011b99cb0313d38269af2117411  ./logs/02-stage.log
de0b9c5a4c07d01706068369e38760080d726b7537cb492564eb0192adcd3592  ./logs/03-fingerprint.log
d9ad9ea0e4b172de8ba052e76ccb05db136c4bda368dbfeff3c5ae11225ff5c4  ./logs/04-host.log
2e5eecddd18f97d50979620a2e09c7cba67b1b77957e24fdd83e5df962c11ee0  ./logs/05-refs-number.log
3ff9df83e8c296af6344c836ec1c52912ca539cc415d8a60e4af07290a2641fd  ./logs/06-branch.log
25120ab6b582ca6bc1c4d5490f7b4ddf4026451ddf6f69baaf1188dd6aac8d7f  ./logs/07-extract-wt.log
305ec3500bb86f7e4235fa92c1c628bb8e5b3f973dab075fe4c173a484ca3fc1  ./logs/08-commit-push.log
6a88a7bca70f087ceb9dc2cfc64d66762d78c84de10705b30785d6099c538e42  ./logs/09-pull-request.log
818cdc9ef3f42375d2f07f6309cc6d1757e85f7d50410a42a0c798d52dc98e77  ./logs/10-selftest-adv3.log
48c0f9c7dfd47bfdc7df63db63f1e0cb963eb6f72cbed7b68473f297793d065c  ./logs/11-selftest-bot.log
b7a0be2cd2df7548134f3bf444b83dbfffb724c1534b6b944fb6049ce614fd72  ./logs/12-selftest-checker.log
12b7fc4581570f679cc13c062375f4bfabcefaae312c298673f540df13f42e7b  ./logs/13-rule.log
f668eab2ed7feae65d8deaf1c5b50cf33661e3545cee5698fc589305e0bbc0cb  ./logs/14-scratch.log
fb0d34cc370ef022bb975c53cd4bc78b51cadbe807b2e63f5ae5d7e5fd540e5c  ./logs/15a-reclaim-refused.log
f3168f96d5e58baade87a0576dc398c41a98d1c9124502ddf2c154c731ece3a3  ./logs/15b-reclaim-by-boss.log
0f2c9bddbb438b55ef6d440d96987ab0f1e9513aa461318ae2262f700c95ca63  ./logs/15-reclaim-scratch.log
29d3cc26af8e481a9bbc3e32155b50dc341c77f44d17389a2975b0d36a10c21d  ./logs/16-reclaim-verify.log
98e1e146dddded30c64bab1fc892cd08e8b6df8cd9b2e2b83770ecd9074b6798  ./logs/17a-b-deploy-refused.log
07016a13d5105c3081269de646a657a6fc91c08ab798dc38243e4e910faf2e32  ./logs/17b-b-deploy-by-boss.log
0b76e67919633c9c56c58b92e00e07ab0b84587d77939f87b6819ab9445faa05  ./logs/17-b-deploy.log
23c38c43871da8cfaf6fe8533df0501fb3794804a59a8b59a3e4edab1fbd4f67  ./logs/18-copy.log
df2ffae6f2f78445f26b4af310d77df6c9454d6afc81b000fd48bf2f5af855c4  ./logs/19-render.log
62ff9bead9ef6d8a257753be0633df2458cb3470900e9e4a3b5b23b87c2a6086  ./logs/20-p-start.log
02be9b37db2c3b1977f344ca8d1ca8d189dfb68647617f660848811deda56191  ./logs/21a-b-kill-refused.log
1bfd5814987525312d9aa6ef6238318a8bc7b7eeb0b69dc5a00c5a117f8b2108  ./logs/21b-b-kill-by-boss.log
50919a34b3dd4d5d2f7a2f6f9297692c7fe2be437b7482d54cb20714c1da4ece  ./logs/21-b-kill.log
9150b24163c3bd283ad402b43b3b55328f0d098314dd0ecbfa8f0fa479f10727  ./logs/22-unit-new.log
061105f8c497eb7328b0bcc6123cc4ff57d55472fdfd091346257e8d2f578ef4  ./logs/23-unit-new-verify.log
a7fedd03bc0e22a38996fd1fc81f7e1db31ecf969a555fe4dfa7e342126ce10b  ./logs/24-closing.log
5e83ecd0d6563bc461e245a4c673cde6bf8ed1d178435d0c76c36672f5526faf  ./logs/25-separation.log
4f753698a4ecf17cb7a82f252a512559734ff5d731c79710378bb9a94baa3cf9  ./render-state/journal.jsonl
3a044d50f51b16563b99bf1514ef92f35a9795b1fcc377aea6be4c23a31f7af2  ./stage/advisor/adv3-bot.py
eec1f30b971ed1d6db31e27eb0c321276c1b107a1654e013996d023b1a6a04eb  ./stage/research/tz37-capital-allocation.py
cd4bec8b5ffd15a903cbafa5da7f7ba27bbf21d7d26cbe57dcf2d95f194cc437  ./state.json
--- sizes
19365 ./bot.before
41 ./commit.before
99 ./logs/01-work-tree.log
288 ./logs/02-stage.log
9961 ./logs/03-fingerprint.log
3959 ./logs/04-host.log
7773 ./logs/05-refs-number.log
435 ./logs/06-branch.log
484 ./logs/07-extract-wt.log
926 ./logs/08-commit-push.log
267 ./logs/09-pull-request.log
99 ./logs/10-selftest-adv3.log
94 ./logs/11-selftest-bot.log
94 ./logs/12-selftest-checker.log
664 ./logs/13-rule.log
991 ./logs/14-scratch.log
529 ./logs/15a-reclaim-refused.log
236 ./logs/15b-reclaim-by-boss.log
328 ./logs/15-reclaim-scratch.log
797 ./logs/16-reclaim-verify.log
443 ./logs/17a-b-deploy-refused.log
156 ./logs/17b-b-deploy-by-boss.log
143 ./logs/17-b-deploy.log
1123 ./logs/18-copy.log
2888 ./logs/19-render.log
469 ./logs/20-p-start.log
520 ./logs/21a-b-kill-refused.log
276 ./logs/21b-b-kill-by-boss.log
141 ./logs/21-b-kill.log
863 ./logs/22-unit-new.log
863 ./logs/23-unit-new-verify.log
7694 ./logs/24-closing.log
511 ./logs/25-separation.log
6322 ./render-state/journal.jsonl
49783 ./stage/advisor/adv3-bot.py
51269 ./stage/research/tz37-capital-allocation.py
1119 ./state.json
--- worktree files the run wrote (tracked, committed)
3a044d50f51b16563b99bf1514ef92f35a9795b1fcc377aea6be4c23a31f7af2  wt/advisor/adv3-bot.py
eec1f30b971ed1d6db31e27eb0c321276c1b107a1654e013996d023b1a6a04eb  wt/research/tz37-capital-allocation.py
status exit=0
--- service copy
d73a657ef31decad276b858c4ec9672dce1c1c5cec36f0bb1c5b3378838224a8  /root/adv3-bot-svc/adv3.py
e14dba8be544c33838f0fbb526d2409db2e3dbeb76cef71f4416f8a40c0d3198  /root/adv3-bot-svc/commit.txt
3a044d50f51b16563b99bf1514ef92f35a9795b1fcc377aea6be4c23a31f7af2  /root/adv3-bot-svc/adv3-bot.py
6d70c6aaa5457365743d2fb80e13e0817af8d292
444628905625809f24dd1fa51159b4093b763789
```

`logs/26-files-written.log` does not list itself; its hash, and every kept file's, is `I keep`'s line in §2.14. The
worktree's two files are the committed ones, `git status --porcelain --ignored` empty. `render-state/journal.jsonl` is the
scratch journal of G-RENDER — the four records `request`, `alloc`, `alloc`, `alloc`, with the day's cards — never printed,
not kept, removed with the tree. In `/root/adv3-bot-svc/`: `adv3-bot.py` `3a044d50…` and `commit.txt` `e14dba8b…`
(`6d70c6aaa5457365743d2fb80e13e0817af8d292` and a newline); `adv3-bot.py.new` existed for the `mv` alone. On `main`: this
report. In `/root/btc-forensics/`: `I keep`'s copies, §2.14.

### 2.11 The unit's journal and record, before and after

`journalctl` (§2.8): `SIGTERM` to main process `3574987` "on client request" at 13:58:13, "Consumed 1.064s CPU time,
16.5M memory peak, 15.7M memory swap peak"; "Scheduled restart job, restart counter is at 2" and "Started" at 13:58:43.
`service.log`: one line since the mark, `2026-10-31T13:58:43Z serving the pinned chat: pid 3616193 offset 685120812
daily-sent 2026-10-31`. `/var/lib/adv3-bot/`: `daily-sent` and `journal.jsonl` unchanged since 06:00 UTC (10 and 5,181
bytes); `offset` unchanged since 09:30 UTC; `service.log` 4,011 → 4,108 bytes.

### 2.12 Timeline

| UTC | step |
|---|---|
| 13:15:40 | contract §1: pull, the TZ and the map read |
| 13:16:07 | §0.0 the work tree |
| 13:16:21 | §0.1 staged |
| 13:16:29 | §0.2 FINGERPRINT 65 of 65 |
| 13:16:39 | §0.3 HOST 16 of 16 |
| 13:16:52 | §0.5 refs, NUMBER 2 of 2 |
| 13:17:11 – 13:17:23 | §3.1 NUMBER 2 of 2, worktree, extraction |
| 13:17:38 | commit `6d70c6a`, push |
| 13:17:55 | pull request #37 |
| 13:18:08 – 13:18:09 | SELFTESTS, RULE 7 of 7 |
| 13:18:18 | §3.3 scratch |
| about 13:19 | the Executor's `reclaim` refused; handed to the Boss |
| 13:45:28 – 13:45:29 | B-RECLAIM-SCRATCH, the Boss: reclaim and two removals |
| 13:46:08 | the Executor's verification |
| about 13:46:20 | the Executor's B-DEPLOY refused; handed to the Boss |
| 13:54:46 | B-DEPLOY, the Boss: mark `deploy` |
| 13:55:37 | COPY 5 of 5 |
| 13:55:46 – 13:56:00 | G-RENDER 16 of 16 |
| 13:56:10 – 13:56:13 | P-START 5 of 5 |
| about 13:56:35 | the Executor's B-KILL refused; handed to the Boss |
| 13:58:13 | B-KILL, the Boss: mark `kill` |
| 13:58:43 | the new process |
| 13:58:58 | UNIT-NEW 9 of 9, the Boss's block |
| 13:59:12 | UNIT-NEW 9 of 9, the Executor |
| 13:59:19 | §3.6's reads |
| 13:59:29 | contract §4.2 |
| 14:00:03 | the files written |
| 14:03:44 – 14:03:50 | §9 B-RECLAIM-OWN (§2.14), with this report drafted; then this report's commit |

### 2.13 Findings, recorded and gating nothing

1. **Claude Code's auto mode classifier refused three of this TZ's blocks to the Executor** — `reclaim` (no explanation),
   B-DEPLOY (no explanation) and B-KILL ("[Production Deploy]") — where TZ-36's Executor ran all three forms. Each refusal
   stopped the session before the command ran; each block went to the Boss, who ran it in his login 26, 8 and 2 minutes
   later; each was verified by the Executor from its log and the host's state. `I copy`, `I render`, `--probe`, `I unit`,
   the closing reads and the git steps were not refused.
2. **The Boss's terminal writes an OSC 133 prompt marker into a file a block appends to** — `ESC ] 133 ; C BEL` at the
   start of `logs/15-reclaim-scratch.log`, his first block of the session; his later two blocks' logs open without one.
   No reading parses that line.
3. **The old bot answered one message at 09:30:57 UTC with `HELP`** (`service.log` "help sent", `offset` 685120811 →
   685120812, no journal record) — a text the TZ-35 bot's `CMD` did not match, sent before this TZ began; no TZ's.
4. **This TZ and the map's revision landed in two uploads** — `ee2ec2b` at 13:10:08 UTC and `0e987e1` at 13:12:23 UTC —
   where the header names "the one upload that carries this TZ". `main` carried revision `2026-10-31-a` at every read.
5. **The remote-control session of 2026-10-30, `238335b9…`, still runs** (processes `3435609`, `3435619`, `3435628`,
   `3435667`, and `3435954` started 13:18:48 UTC that day); this session's process `3609936` made `f13dd443…` and
   `50f7dcda…` at 13:14 UTC — the next TZ's to reclaim once no running `claude` process made them. `du` of `/root/.claude`
   read `16` bytes at both reads: the sessions' configuration directory is `/root/.claude-8j`
   (`CLAUDE_CONFIG_DIR`, the tmux command line `ps` printed), not read by this TZ.
6. The pair book's unit read `NRestarts` `15` at pid `3530053`, active since 03:06:30 UTC, as at TZ-36; unchanged across
   this TZ, as were the recorder's (`2388318`/0) and the reward book's (`3137952`/1).

### 2.14 §9 B-RECLAIM-OWN — last, after §3.6, with this report drafted (V14, V15)

Run from the session in two calls, each beginning with `date -u`; its output was written to no file and is quoted here
verbatim, every line. The first call — `I keep`, then `git worktree remove` without `--force`:

```
2026-10-31T14:03:44.882337854Z
K copied e65de91c7b49c6f932db91e568a5956c005e63119c1cf6fb8724ffb0438d1dcb /root/btc-forensics/tz37-work--bot.before
K copied 810c9ed61de6850bf05d7530d8b033396e56940a57f994dcefc4f823f2145b3e /root/btc-forensics/tz37-work--commit.before
K copied cd781784479f0fca9f4a104195fdbaf8e07d85931851c360b25fbd2eb84cc799 /root/btc-forensics/tz37-work--logs--01-work-tree.log
K copied a58c6cbf08b5821e726c926758f3f160d682f011b99cb0313d38269af2117411 /root/btc-forensics/tz37-work--logs--02-stage.log
K copied de0b9c5a4c07d01706068369e38760080d726b7537cb492564eb0192adcd3592 /root/btc-forensics/tz37-work--logs--03-fingerprint.log
K copied d9ad9ea0e4b172de8ba052e76ccb05db136c4bda368dbfeff3c5ae11225ff5c4 /root/btc-forensics/tz37-work--logs--04-host.log
K copied 2e5eecddd18f97d50979620a2e09c7cba67b1b77957e24fdd83e5df962c11ee0 /root/btc-forensics/tz37-work--logs--05-refs-number.log
K copied 3ff9df83e8c296af6344c836ec1c52912ca539cc415d8a60e4af07290a2641fd /root/btc-forensics/tz37-work--logs--06-branch.log
K copied 25120ab6b582ca6bc1c4d5490f7b4ddf4026451ddf6f69baaf1188dd6aac8d7f /root/btc-forensics/tz37-work--logs--07-extract-wt.log
K copied 305ec3500bb86f7e4235fa92c1c628bb8e5b3f973dab075fe4c173a484ca3fc1 /root/btc-forensics/tz37-work--logs--08-commit-push.log
K copied 6a88a7bca70f087ceb9dc2cfc64d66762d78c84de10705b30785d6099c538e42 /root/btc-forensics/tz37-work--logs--09-pull-request.log
K copied 818cdc9ef3f42375d2f07f6309cc6d1757e85f7d50410a42a0c798d52dc98e77 /root/btc-forensics/tz37-work--logs--10-selftest-adv3.log
K copied 48c0f9c7dfd47bfdc7df63db63f1e0cb963eb6f72cbed7b68473f297793d065c /root/btc-forensics/tz37-work--logs--11-selftest-bot.log
K copied b7a0be2cd2df7548134f3bf444b83dbfffb724c1534b6b944fb6049ce614fd72 /root/btc-forensics/tz37-work--logs--12-selftest-checker.log
K copied 12b7fc4581570f679cc13c062375f4bfabcefaae312c298673f540df13f42e7b /root/btc-forensics/tz37-work--logs--13-rule.log
K copied f668eab2ed7feae65d8deaf1c5b50cf33661e3545cee5698fc589305e0bbc0cb /root/btc-forensics/tz37-work--logs--14-scratch.log
K copied 0f2c9bddbb438b55ef6d440d96987ab0f1e9513aa461318ae2262f700c95ca63 /root/btc-forensics/tz37-work--logs--15-reclaim-scratch.log
K copied fb0d34cc370ef022bb975c53cd4bc78b51cadbe807b2e63f5ae5d7e5fd540e5c /root/btc-forensics/tz37-work--logs--15a-reclaim-refused.log
K copied f3168f96d5e58baade87a0576dc398c41a98d1c9124502ddf2c154c731ece3a3 /root/btc-forensics/tz37-work--logs--15b-reclaim-by-boss.log
K copied 29d3cc26af8e481a9bbc3e32155b50dc341c77f44d17389a2975b0d36a10c21d /root/btc-forensics/tz37-work--logs--16-reclaim-verify.log
K copied 0b76e67919633c9c56c58b92e00e07ab0b84587d77939f87b6819ab9445faa05 /root/btc-forensics/tz37-work--logs--17-b-deploy.log
K copied 98e1e146dddded30c64bab1fc892cd08e8b6df8cd9b2e2b83770ecd9074b6798 /root/btc-forensics/tz37-work--logs--17a-b-deploy-refused.log
K copied 07016a13d5105c3081269de646a657a6fc91c08ab798dc38243e4e910faf2e32 /root/btc-forensics/tz37-work--logs--17b-b-deploy-by-boss.log
K copied 23c38c43871da8cfaf6fe8533df0501fb3794804a59a8b59a3e4edab1fbd4f67 /root/btc-forensics/tz37-work--logs--18-copy.log
K copied df2ffae6f2f78445f26b4af310d77df6c9454d6afc81b000fd48bf2f5af855c4 /root/btc-forensics/tz37-work--logs--19-render.log
K copied 62ff9bead9ef6d8a257753be0633df2458cb3470900e9e4a3b5b23b87c2a6086 /root/btc-forensics/tz37-work--logs--20-p-start.log
K copied 50919a34b3dd4d5d2f7a2f6f9297692c7fe2be437b7482d54cb20714c1da4ece /root/btc-forensics/tz37-work--logs--21-b-kill.log
K copied 02be9b37db2c3b1977f344ca8d1ca8d189dfb68647617f660848811deda56191 /root/btc-forensics/tz37-work--logs--21a-b-kill-refused.log
K copied 1bfd5814987525312d9aa6ef6238318a8bc7b7eeb0b69dc5a00c5a117f8b2108 /root/btc-forensics/tz37-work--logs--21b-b-kill-by-boss.log
K copied 9150b24163c3bd283ad402b43b3b55328f0d098314dd0ecbfa8f0fa479f10727 /root/btc-forensics/tz37-work--logs--22-unit-new.log
K copied 061105f8c497eb7328b0bcc6123cc4ff57d55472fdfd091346257e8d2f578ef4 /root/btc-forensics/tz37-work--logs--23-unit-new-verify.log
K copied a7fedd03bc0e22a38996fd1fc81f7e1db31ecf969a555fe4dfa7e342126ce10b /root/btc-forensics/tz37-work--logs--24-closing.log
K copied 5e83ecd0d6563bc461e245a4c673cde6bf8ed1d178435d0c76c36672f5526faf /root/btc-forensics/tz37-work--logs--25-separation.log
K copied 63b4d179d5cbb0ef31adbabed1d8e586438da30d229a81014d57e5274bfbf2a8 /root/btc-forensics/tz37-work--logs--26-files-written.log
K copied cd4bec8b5ffd15a903cbafa5da7f7ba27bbf21d7d26cbe57dcf2d95f194cc437 /root/btc-forensics/tz37-work--state.json
KEEP PASS: 35 files kept, 35 copied, 0 already held; forensic store 2232 -> 2267 files; worktree at 6d70c6aaa5457365743d2fb80e13e0817af8d292, its upstream's
exit=0
exit=0
```

The second — `rm -rf /root/tz37-work`, `test -e`, `git worktree prune` and `list`, the store's count and `df`:

```
2026-10-31T14:03:50.913844191Z
exit=0
exit=1
/root/btc-5m-twap       0e987e1 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
2267
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10516705280
```

**V14 (keep):** `keep` considered 35 files — `state.json`, `bot.before`, `commit.before` and the 32 logs — and copied 35,
none already held; the store's count after, `2,267`, is the count before, `2,232`, plus the 35 copies, asserted by
`keep` and read again by `find`. The 35 copies were then hashed in the store, equal to the 35 `K copied` lines.
`logs/26-files-written.log`'s hash is `63b4d179…`. **V15:** `git worktree remove` without `--force` `exit=0`; `rm -rf
/root/tz37-work` `exit=0` and `test -e` `exit=1`; `git worktree list` names `/root/btc-5m-twap` and
`/root/btc-recorder-svc` and nothing else. Neither call was refused. The branch `tz-37-capital-allocation` stays on
`origin` and as a local ref.

---

## 3. Publication

| item | value |
|---|---|
| branch | `tz-37-capital-allocation`, pushed 13:17:38 UTC through the URL's own credential |
| commit | `6d70c6aaa5457365743d2fb80e13e0817af8d292`, parent `0e987e1704dc0edfe6a45ff1b59baf8d73fc1e32`, two files, `+1213 −29` (`405 29`, `808 0`) |
| pull request | #37, `https://github.com/seahomebatumi-ai/btc-5m-twap/pull/37`, base `main`, open, not merged |
| Release | none: this TZ publishes no asset |
| deployment | `/root/adv3-bot-svc/adv3-bot.py` replaced by the branch's at 13:54:46 UTC and the unit signalled at 13:58:13 — the TZ's own deployment (§3.4, §3.5), both blocks run by the Boss after the classifier refused them to the Executor; the merge stays the Boss's, after the verdict |
| separation self-check | §2.9: `0`; `advisor/adv3-bot.py`, `research/tz37-capital-allocation.py`; nothing |
| report | this file, to `main` after B-RECLAIM-OWN |

---

## 4. Gate

| gate | PASS as the TZ fixes it (§4) | read | ratio | verdict |
|---|---|---|---|---|
| G-RULE | 7 of 7 | 7 of 7 | 1.000 | **PASS** |
| SELFTESTS | 44 of 44, 67 of 67 and 50 of 50 | 44, 67, 50 | 1.000 each | **PASS** |
| COPY | 5 of 5 | 5 of 5 | 1.000 | **PASS** |
| G-RENDER | 16 of 16 | 16 of 16 | 1.000 | **PASS** |
| P-START | `READING P-START: served - 5 of 5 endpoints` | served 5 of 5 | 1.000 | **PASS** |
| UNIT-NEW | 9 of 9 | 9 of 9 | 1.000 | **PASS** |

Nothing was tuned and no gate reinterpreted. Per §4.5, a PASS establishes that the service copy's `adv3-bot.py` is
Appendix A's and the unit runs it; that the rule, its message, the bot's unit and the other advisor files are byte for
byte what TZ-36 and TZ-35 deployed, and the bot's other definitions — the daily path, the probe and the modes — tree for
tree theirs; and that the six texts of G-RENDER were answered on live data with the shapes §4.2 fixes and, on that data —
3 STRONG coins, 2 trades placed in each allocation — the allocation kept the limits §4.2 states. **Not established:** that
the allocation is a good one — the weights are the Architect's, unproven, and the forward record measures the rule, not
them; that the Boss's Telegram shows the reply as the Architect expects, which is his next «сигнал 10000 топ 3»; and
anything about the market to come.

---

## 5. Validation

| # | check | count | asserted? |
|---|---|---|---|
| **V1** | §0.2's fingerprint | `READING FINGERPRINT: PASS - 65 of 65`: revision; 6 anchors, 4 re-derived; 56 rows, 53 of 53 `frozen` equal; the shape | asserted by the checker (`verdict` raises, exit 1) |
| **V2** | §0.3's host gate | `READING HOST: PASS - 16 of 16`; the first memory read 148,074,496 bytes, no second read | asserted by the checker |
| **V3** | NUMBER at §0.5 and §3.1 | `PASS - 2 of 2` each, the `TZ-37-` path printed; the branch count `0` | NUMBER asserted by the checker; the branch count recorded, not asserted — read `0` by the Executor |
| **V4** | §0.1's and §3.1's files | 2 of 2 hashes at each, asserted by the script; lines and bytes equal; `M`, `A`; `--numstat` `405 29`, `808 0` | hashes asserted; the diff's names and numstat recorded, not asserted — compared by the Executor with §3.1's text, exact |
| **V5** | the self-tests | `44 of 44`, `67 of 67`, `50 of 50` | asserted, each in its own script |
| **V6** | G-RULE | `READING RULE: PASS - 7 of 7` | asserted by the checker |
| **V7** | B-DEPLOY | `exit=0`; the mark printed | the chain's `&&` stops at the first failure; `exit` recorded |
| **V8** | COPY | `READING COPY: PASS - 5 of 5` | asserted by the checker |
| **V9** | G-RENDER | `READING RENDER: PASS - 16 of 16`; the replies' sizes; 3 STRONG coins; 2, 2, 2 trades placed | asserted by the checker; the sizes and counts printed, not asserted |
| **V10** | P-START | `READING P-START: served - 5 of 5 endpoints`, each line printed | asserted by `adv3-bot.py --probe` |
| **V11** | B-KILL and UNIT-NEW | `exit=0`; `READING UNIT-NEW: PASS - 9 of 9` twice; pids `3574987`, `3616193`; instants 13:58:13.720225 and 13:58:43 UTC | UNIT-NEW asserted by the checker; `mark kill` asserted `daily-sent`; B-KILL's `exit` recorded |
| **V12** | contract §4.2's self-check | `0`; two files; nothing | recorded, not asserted |
| **V13** | §3.6's closing reads | every read printed, §2.8 | recorded, not asserted — no threshold |
| **V14** | B-RECLAIM-SCRATCH and §9's `keep` | reclaim: 5 files considered, 0 copied, store 2,232 → 2,232; keep: §2.14 | asserted by `reclaim` and `keep` (the store's count) |
| **V15** | §9's removals | §2.14 | exit codes recorded, not asserted |

---

## 6. What could not be implemented as written

1. **Three blocks refused to the Executor and run by the Boss.** Claude Code's auto mode classifier refused B-RECLAIM-SCRATCH's
   `reclaim` (no explanation), B-DEPLOY (no explanation) and B-KILL ("[Production Deploy]"), each before it ran — the
   Executor confirmed after each refusal that nothing had changed (no log, no mark, the service copy's hash and the unit's
   pid as before) and recorded it in a log (`15a`, `17a`, `21a`). The Executor did not retry any of them in another form.
   Each went to the Boss by the TZ's route (§0.0, §3.3; map §6, sandbox limit) and he ran it in his login:
   B-DEPLOY and B-KILL verbatim with `NN` filled in; B-RECLAIM-SCRATCH as one `reclaim` naming both directories and one
   `rm -rf` and one `test -e` a directory — §3.3's commands — each removal prefixed by `grep -q '^RECLAIM PASS'` of the log so
   that none ran without it, and every output appended to the log. **To B-KILL's block the Executor appended UNIT-NEW's
   reads** — `sleep 45`, then `I unit new` every 15 s while it printed `NOT YET`, at most five runs — so that §3.5's
   schedule held while the Boss's paste ran; §3.5 has the Executor run `I unit new`, and the Executor ran it again at
   13:59:12, 9 of 9. Every outcome was verified from the logs, `test -e`, `sha256sum`, `systemctl show` and the checker's
   own modes, never from the Boss's account.
2. **A timing wrapper.** G-RENDER ran as `timeout 900 /usr/bin/time -v nice -n 19 /root/tz04a-env/venv/bin/python -B …
   render`, for the host peak map §7 item 131 asks a later floor to take, with `/proc/meminfo`'s `MemAvailable` read
   before it. The command under test and its arguments are the TZ's.
3. **The logs' names.** `NN` in B-DEPLOY's and B-KILL's blocks became `17` and `21`; every step's log is numbered in this
   TZ's order, `01-work-tree.log` written after the `mkdir` from its captured output. Logs this TZ does not name:
   `08-commit-push.log`, `09-pull-request.log`, `15a-reclaim-refused.log`, `15b-reclaim-by-boss.log`,
   `16-reclaim-verify.log`, `17a-b-deploy-refused.log`, `17b-b-deploy-by-boss.log`, `21a-b-kill-refused.log`,
   `21b-b-kill-by-boss.log`, `23-unit-new-verify.log`, `25-separation.log` and `26-files-written.log`. Each is kept by
   `I keep`.
4. **Contract §1.** Step 1 as `git fetch origin` and `git pull --ff-only origin main`, a fast-forward from `a3affbb` to
   `0e987e1`. Before §0.0's `mkdir` the Executor read the repository's listing and `git log`, `.claude/settings.local.json`,
   the TZ-36 report's opening, and — to learn whether this session ran on the capture host — `hostname`, `uptime -s`, `ls -d`
   of `/var/lib/btc-recorder`, `/root/adv3-bot-svc`, `/var/lib/adv3-bot` and the interpreter, `df` of the recorder's
   filesystem, `systemctl is-active adv3-bot.service`, `ls /root/tz37-work` (absent) and `ls -la /tmp/claude-0/`. Step 2:
   this TZ in full; the map in the sections the TZ rests on — §0, the start of §1, §2.7, the end of §3, §6's rows (host,
   host identity, git remote, both sandbox limits, the harness) and §7 items 125 to 137 — not every line; the fingerprint
   read every row.
5. **Reads no step names**, none under `/etc/adv3-bot/` and none printing a coin, a price or a size from the live replies:
   `get_session` for the model; the map's and the TZ's hashes; `ps` of the `claude` processes after `scratch`; the source of
   TZ-35's `mode_reclaim`, to gate the Boss's removals on its last line; `ls`, `sha256sum` of the service copy, `state.json`'s
   marks and `systemctl show` of the bot after each refusal; `cat -v` of the Boss's logs' first lines; `grep` for a token
   pattern in the logs, none found; `git config`, `gh pr view 36` and the TZ-36 report's sections, for the commit's, the pull
   request's and this report's form.
6. **The commit message and the pull request's text** are the Executor's own.
7. **The report** was written by hand with its logs inlined from their files by a substitution in the session's scratchpad
   (the control characters of the Boss's OSC 133 marker shown as `cat -v` shows them), so no log line was retyped; the
   table of §0.1 was built from `logs/03-fingerprint.log` by the same script. B-RECLAIM-OWN's output, which no file holds,
   was pasted into §2.14 from the session.
8. **B-RECLAIM-OWN in two calls**, a `date -u` before each: `keep` and `git worktree remove`, then the rest, every
   command §9's and in its order; neither was refused.

Nothing else: every gate was read by the checker's or the bot's own modes on Appendix A's bytes.
