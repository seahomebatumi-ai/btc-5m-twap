# TZ-39 report — the advisor's two checks a day: a monitor of the trades its cards offered, a scanner of the 42, the 14 % stop, the list to seven, «Уверенность: N/5» on every card, and a journal of every check

**NUMBER PASS: 2 of 2** at §0.5 (06:23:00 UTC) and again at §3.1 (06:23:08 UTC): `CryptoTZ/` holds `TZ-39-advisor-checks.md` and no other `TZ-39-` file, `CryptoReports/` no `TZ-39-` report; the branch count `0` before the push.
**G-RULE PASS: 10 of 10** — `adv3.py`: `card_lines`, `message`, `trust_lines` changed, `assessment`, `changes` added, the 44 others identical by `ast.dump`, the 14 rule functions among them, `PIT` equal to TZ-38's report cell for cell; `adv3-bot.py`: 9 changed, 35 added, `journal` removed, the 13 others identical; `RULE-ADV-3.txt` and the unit `main`'s byte for byte · **SELFTESTS: 53 of 53, 106 of 106, 64 of 64**.
**B-DEPLOY `exit=0`** (mark 06:50:50.99 UTC) · **COPY PASS: 5 of 5** · **G-RENDER PASS: 22 of 22** on live data — **2 STRONG coins**; trades placed per allocation **2, 2**; the signal check loud with alerts **stop 0, signal 1, candidate 2**, the fact check quiet, one line, alerts **stop 0, signal 0, candidate 0** · **P-START: served - 5 of 5 endpoints**.
**B-KILL `exit=0`** (mark 06:51:09.98 UTC) · **UNIT-NEW PASS: 9 of 9** — pid `3616193` → `3766156`, started 06:51:39 UTC, `NRestarts` 2 → 3, the three capture units unchanged · **G-FIRST PASS: 7 of 7** — the first check, `2026-11-01 signal` of the close of 2026-10-31, **loud, full, 1 message**, alerts **stop 0, signal 1, candidate 2**, 12 followed trades, 2 coins placed, sent at 06:51:46 UTC.
**No rollback ran**: B-ROLLBACK, B-KILL2, UNIT-OLD, K-39 and `stopped` were not run, no gate failed.
**The unit runs the new code**: `adv3-bot.service` `active`, `enabled`, pid `3766156`, `/root/adv3-bot-svc/adv3.py` `c19572dc…` and `adv3-bot.py` `ca989b6f…`, `commit.txt` `fc687582ebc4064b7483e2ac5cb9ca5b1af9c9f5` — verified by `I copy`, `I unit new` and `I first` in the Boss's paste (06:50:51 – 06:51:55 UTC) and again in the Boss's second paste of the Executor's refused re-reads (07:07:53 UTC: COPY 5 of 5, UNIT-NEW 9 of 9, FIRST 7 of 7), and by §3.7's `systemctl show`, `is-enabled`, `journalctl`, `service.log` and `check-done`, never from the Boss's account.
**Three of the session's commands were refused by Claude Code's auto mode classifier, each before it ran, and handed to the Boss unchanged:** B-RECLAIM-SCRATCH's `reclaim` ("[Irreversible Local Destruction]", about 06:24:45 UTC), run by the Boss at 07:07:42 UTC — `RECLAIM PASS`, 8 files considered, none copied, both directories removed, each verified gone by the Executor's `test -e` at 07:07:49; B-DEPLOY ("[Production Deploy]", about 06:26:05 UTC), so P-BOSS-A went to the Boss at the band's opening, 06:35:00, and he ran it at 06:50:50 — B-DEPLOY to G-FIRST in one paste; and the Executor's three re-reads after the paste, `I copy`, `I unit new` and `I first` ("[Production Deploy]", about 06:52:45 UTC) , run by the Boss at 07:07:53 UTC, each PASS. None was retried by the Executor in another form (§6 item 1).
**Departures, all in §6:** the refused blocks; a routing note on the package manager's run at 06:59:49 UTC; a timing wrapper on the self-tests and G-RULE; the logs' names; working files in the work tree and one in the scratchpad; reads no step names; the map read in sections.

| field | value |
|---|---|
| TZ | `CryptoTZ/TZ-39-advisor-checks.md`, 4,323 lines, 347,992 bytes, SHA-256 `d7fd02b80a788a4a6fb75ee9dbd2ceddcb0dc1373079874c96d354eaa3bfa581`, landed at `dd65a7e` (2026-11-01 06:19:13 UTC), above `17dc258` (PR #38's merge) and `30a577e` (revision `2026-10-31-c`) |
| map revision | `2026-10-31-c`, equal; anchors 6 of 6; re-derived 4 of 4; rows 58; `frozen` equal 55 of 55; the map 2,003 lines, 504,061 bytes, SHA-256 `c2a318619bfaaa215a06870f90a8e906ae077dc5ab2b90f4d7dee6646e195a31`, the file TZ-39 §10 names |
| executor model | the model the TZ header names: `get_session` read `configured_model`, `session_context.model` and `external_metadata.last_served_model` all `claude-opus-5-5` |
| branch | `tz-39-advisor-checks` at `fc687582ebc4064b7483e2ac5cb9ca5b1af9c9f5`, on `origin/main` `dd65a7e`; pushed; pull request #39, open, not merged |
| service's code | `/root/adv3-bot-svc/`: `adv3.py` `c19572dc…` (was `d73a657e…`), `adv3-bot.py` `ca989b6f…` (was `3a044d50…`), `commit.txt` `fc687582ebc4064b7483e2ac5cb9ca5b1af9c9f5` (was `6d70c6aaa545…`) |
| unit | `/etc/systemd/system/adv3-bot.service` `82acd8e4…`, unchanged; never reloaded |
| interpreter | `/root/tz04a-env/venv/bin/python` 3.12; every session mode under `nice -n 19` and `-B` |
| marks | `deploy` 06:50:50.991504 UTC · `kill` 06:51:09.983455 UTC (`state.json`) |
| blocks | B-RECLAIM-SCRATCH: refused to the Executor about 06:24:45 UTC; run by the Boss 07:07:42 UTC · B-DEPLOY: refused to the Executor about 06:26:05 UTC; P-BOSS-A handed over 06:35 UTC, run by the Boss 06:50:50 – 06:51:56 UTC · the Executor's re-reads: refused about 06:52:45 UTC; run by the Boss 07:07:53 – 07:07:54 UTC · B-RECLAIM-OWN: §2.16 |
| work tree | `/root/tz39-work/`, created 06:21:57 UTC, removed by B-RECLAIM-OWN (§2.16) |

---

## 0. Fingerprint

`I fingerprint`, from the staged copy of the checker, against the primary checkout at `dd65a7e` — revision
`2026-10-31-c`; anchors `A1` `229a944f2d51`, `A2` `6c5089330629`, `A3` `0-complete / 1-student-5tau-not-disqualified /
2-no-edge-4tau-240-undecidable`, `A4` `437b45ea196b`, `A5` `0f6c90451cbd`, `A6` `729f0bcdbee3`, each equal to the TZ
header's; `A2`, `A4`, `A5` and `A6` re-derived. **V1: `READING FINGERPRINT: PASS - 67 of 67`.** The map, the `reported`
row: 2,003 lines, 504,061 bytes, SHA-256 `c2a318619bfaaa215a06870f90a8e906ae077dc5ab2b90f4d7dee6646e195a31`.

### 0.1 The 58 rows of the map's §0 table

Built from `logs/02-fingerprint.log` by a substitution; "equal" stands for each of the 55 `ok   frozen <path>` lines the
checker asserted against the map's lines, bytes and SHA-256.

| path | lines | bytes | state | SHA-256 | against the map |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 2,003 | 504,061 | reported | `c2a318619bfaaa215a06870f90a8e906ae077dc5ab2b90f4d7dee6646e195a31` | — |
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
| `research/tz37-capital-allocation.py` | 808 | 51,269 | frozen | `eec1f30b971ed1d6db31e27eb0c321276c1b107a1654e013996d023b1a6a04eb` | equal |
| `research/tz38-adv3-pit-validation.py` | 1,782 | 90,181 | frozen | `579474b65329662f7bed735994381241a928a2c65a726cec3f933dc7afd4427b` | equal |
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
| `advisor/adv3-bot.py` | 798 | 49,783 | frozen | `3a044d50f51b16563b99bf1514ef92f35a9795b1fcc377aea6be4c23a31f7af2` | equal |
| `advisor/selftest-adv3.py` | 201 | 12,600 | frozen | `ef4ffc44e6f8bcdd5685fc1db9090957890c6e2ab762cdad8ae9826b18cf1395` | equal |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | — |

### 0.2 `logs/02-fingerprint.log`, verbatim (V1)

```
2026-11-01T06:22:36.806773955Z
reported 2003 lines 504061 bytes c2a318619bfaaa215a06870f90a8e906ae077dc5ab2b90f4d7dee6646e195a31 SYSTEM-MAP.md
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
frozen   808 lines 51269 bytes eec1f30b971ed1d6db31e27eb0c321276c1b107a1654e013996d023b1a6a04eb research/tz37-capital-allocation.py
frozen   1782 lines 90181 bytes 579474b65329662f7bed735994381241a928a2c65a726cec3f933dc7afd4427b research/tz38-adv3-pit-validation.py
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
frozen   798 lines 49783 bytes 3a044d50f51b16563b99bf1514ef92f35a9795b1fcc377aea6be4c23a31f7af2 advisor/adv3-bot.py
frozen   201 lines 12600 bytes ef4ffc44e6f8bcdd5685fc1db9090957890c6e2ab762cdad8ae9826b18cf1395 advisor/selftest-adv3.py
tracked  5 lines 252 bytes 9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b .gitignore
ok   revision 2026-10-31-c
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
ok   frozen research/tz37-capital-allocation.py
ok   frozen research/tz38-adv3-pit-validation.py
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
ok   the table holds 58 rows, 55 frozen, 2 tracked, 1 reported
READING FINGERPRINT: PASS - 67 of 67
exit=0
```

### 0.3 Contract §1, §0.0 and §0.1 — the start-up, the work tree and the files staged (V4)

Contract §1 step 1: `git checkout main && git pull` fast-forwarded `f32d0e4` → `dd65a7e` (three commits: `30a577e`, the
map's revision `2026-10-31-c`; `17dc258`, PR #38's merge; `dd65a7e`, this TZ's upload). Step 2: the TZ read — its body,
§0 to §10, in full, and Appendix A's checker at the modes the run calls; the map in sections (§6 item 7). Step 5: the TZ
names Claude Opus 5.5; the session runs `claude-opus-5-5`. §0.0's `mkdir /root/tz39-work /root/tz39-work/logs` printed
`exit=0`.

`logs/00-start.log`:

```
2026-11-01T06:21:57.912672582Z
dd65a7e7fc108585fcfa18916eafcdec3cfd2f98
dd65a7e7fc108585fcfa18916eafcdec3cfd2f98
0
mkdir /root/tz39-work /root/tz39-work/logs -> exit=0
```

`logs/01-stage.log` — §0.1's script, verbatim, over an empty `stage/`, four files created (`xb`):

```
2026-11-01T06:22:11.342205345Z
/root/tz39-work/stage/advisor/adv3-bot.py 1558 99958 ca989b6fe487d41181b32312418d6acda1e9c64fbf5cfbb3f041d54826dd108f
/root/tz39-work/stage/advisor/adv3.py 871 49378 c19572dccf30a505342ca334e42c7ec347a5d29db4db20887229d2a8c7b48e31
/root/tz39-work/stage/advisor/selftest-adv3.py 235 16470 09d2ba9a8361ec5ebc7f5934ebb818d1a685bb16fb3f32b7da94409d9516cc0e
/root/tz39-work/stage/research/tz39-advisor-checks.py 1139 73892 18294b0916d77b226083a18f9521f06e2fddb423bbc947a2e1100fd42b2980f3
exit=0
```

Equal to §0.1's table in lines, bytes and SHA-256, 4 of 4.

### 0.4 Host gate — §0.3's block, verbatim (V2)

`logs/03-host.log`, `S` the scratchpad the session's system prompt names:

```
Sun Nov  1 06:22:45 AM UTC 2026
1793514165
2026-08-02 07:24:32
1
MemTotal:         978640 kB
MemAvailable:     200948 kB
SwapTotal:       3174396 kB
SwapFree:        2338768 kB
units: {"adv3-bot.service": {"ActiveState": "active", "MainPID": "3616193", "NRestarts": "2", "SubState": "running", "UnitFileState": "enabled"}, "btc-pairbook.service": {"ActiveState": "active", "MainPID": "3738426", "NRestarts": "16", "SubState": "running", "UnitFileState": "enabled"}, "btc-recorder.service": {"ActiveState": "active", "MainPID": "2388318", "NRestarts": "0", "SubState": "running", "UnitFileState": "enabled"}, "btc-rewardbook.service": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1", "SubState": "running", "UnitFileState": "enabled"}}
MemAvailable first 217165824 bytes, second not read, deciding 217165824; /dev/vda2 free 11410116608 bytes
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
ok   H5 adv3.py is TZ-36's and adv3-bot.py is TZ-37's
ok   H5 the installed unit file is TZ-35's
ok   H5 commit.txt is 40 hex characters and a newline
ok   H6 the record holds a journal of whole lines and no check-done file
ok   memory gate: MemAvailable at least 130981888 bytes, a first read below it read again after 60 s
ok   disk gate: /dev/vda2 free at least 7400000000 bytes
READING HOST: PASS - 16 of 16
exit=0
NEXT                            LEFT LAST                              PASSED UNIT                         ACTIVATES
Sun 2026-11-01 06:59:49 UTC    37min Sat 2026-10-31 06:38:15 UTC      23h ago apt-daily-upgrade.timer      apt-daily-upgrade.service
Sun 2026-11-01 10:46:42 UTC 4h 23min Sun 2026-11-01 02:05:44 UTC 4h 17min ago apt-daily.timer              apt-daily.service
Mon 2026-11-02 01:30:20 UTC      19h Sun 2026-11-01 01:30:20 UTC 4h 52min ago btc-rewardbook-archive.timer btc-rewardbook-archive.service
Mon 2026-11-02 03:00:20 UTC      20h Sun 2026-11-01 03:00:20 UTC 3h 22min ago btc-pairbook-archive.timer   btc-pairbook-archive.service

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
total 108
drwxr-xr-x  2 root root  4096 Oct 31 13:54 .
drwx------ 31 root root  4096 Nov  1 06:21 ..
-rw-r--r--  1 root root 49783 Oct 31 13:54 adv3-bot.py
-rw-r--r--  1 root root 43274 Oct 31 08:36 adv3.py
-rw-r--r--  1 root root    41 Oct 31 13:54 commit.txt

/var/lib/adv3-bot:
total 36
drwx------  2 root root  4096 Nov  1 06:00 .
drwxr-xr-x 65 root root  4096 Oct 29 14:35 ..
-rw-r--r--  1 root root    10 Nov  1 06:00 daily-sent
-rw-r--r--  1 root root 11503 Nov  1 06:00 journal.jsonl
-rw-r--r--  1 root root     9 Oct 31 15:39 offset
-rw-r--r--  1 root root  4592 Nov  1 06:00 service.log
233728002	/var/lib/btc-rewardbook
149211432	/var/lib/btc-pairbook
16114	/var/lib/adv3-bot
16	/root/.claude
2312
/root/btc-5m-twap       dd65a7e [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/tmp/claude-0/-root-btc-5m-twap/a2827336-da6d-511b-b699-35cb76f477de/scratchpad
total 28
drwx------  7 root root 4096 Nov  1 06:20 .
drwx------ 35 root root 4096 Nov  1 06:20 ..
drwx------  3 root root 4096 Nov  1 06:20 0f8f6761-2295-466b-9178-9b8a0261193e
drwx------  3 root root 4096 Oct 30 13:16 238335b9-cf23-414a-8e8f-ad4705c4d19e
drwx------  4 root root 4096 Oct 31 19:20 716c29e7-4743-5553-ac5d-886f724de131
drwx------  4 root root 4096 Nov  1 06:20 a2827336-da6d-511b-b699-35cb76f477de
drwx------  3 root root 4096 Oct 31 19:20 f00a192e-0435-4a82-9ad0-d54ae254a648
```

**V2: `READING HOST: PASS - 16 of 16`.** The service copy held TZ-36's `adv3.py` and TZ-37's `adv3-bot.py`, the unit file
`main`'s, no `check-done`. The record's `daily-sent` was written at 06:00 UTC, the old code's message of 2026-11-01
(`service.log`, §2.9). The listing of the session directories' parent shows this session's own `a2827336…` and its
sibling `0f8f6761…`, both born 06:20 UTC, TZ-38's two and the live `238335b9…`. The timers' read shows
`apt-daily-upgrade.timer` next at 06:59:49 UTC, inside B-DEPLOY's and B-KILL's morning bands (§6 item 2).

### 0.5 Free space and `MemAvailable` — every read, its instant and its bound

| instant (UTC) | read | `MemAvailable`, bytes | floor | free on `/dev/vda2`, bytes | floor |
|---|---|---|---|---|---|
| 06:22:45 | §0.3, `grep /proc/meminfo` | 205,770,752 (`200948 kB`) | 130,981,888 | — | — |
| 06:22:45 | §0.3, `I host`'s gate, first read, deciding | 217,165,824 | 130,981,888 | 11,410,116,608 | 7,400,000,000 |
| 06:53:11 | §3.7, `free -b` (available) and `df` | 168,054,784 | — | 11,379,015,680 | — |
| 07:09:37 | §9, B-RECLAIM-OWN's `df` | — | — | 11,378,479,104 | — |

No first read fell below the floor, so no second read was made. Free space never neared `STREAM_FLOOR`,
`7,300,000,000`.

### 0.6 Refs and the number (§0.5) — `logs/04-refs.log`, verbatim (V3)

```
2026-11-01T06:23:00.049882597Z
fetch exit=0
dd65a7e7fc108585fcfa18916eafcdec3cfd2f98	HEAD
dd65a7e7fc108585fcfa18916eafcdec3cfd2f98	refs/heads/main
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
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793502020
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793263627
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793286490
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793306720
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793321975
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793323820
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793357934
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793410220
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793496620
d3251aa2bd312409f7b096bfd5968f3bedbd1be5	refs/tags/tz-01a-dataset
ea9290b92b9fa50c22d0560d5d01dfa392af44df	refs/tags/tz-01a-dataset^{}
e299d4e45f48b7efaa8cb18bd54b139fc0627630	refs/tags/tz-27-pairbook-streams
bce5a85be7850a33f95192265b916cc9c5e0aaf1	refs/tags/tz-27-pairbook-streams^{}
ls-remote exit=0
0
CryptoTZ/TZ-39-advisor-checks.md
ok   CryptoTZ/ holds CryptoTZ/TZ-39-advisor-checks.md and no other file of that number
ok   CryptoReports/ holds no report of that number
READING NUMBER: PASS - 2 of 2
exit=0
dd65a7e 2026-11-01T10:19:13+04:00 Add files via upload

A	CryptoTZ/TZ-39-advisor-checks.md
17dc258 2026-11-01T03:04:56+04:00 Merge pull request #38 from seahomebatumi-ai/tz-38-adv3-pit-validation

A	research/tz38-adv3-pit-validation.py
30a577e 2026-11-01T03:02:40+04:00 Update SYSTEM-MAP.md

M	SYSTEM-MAP.md
f32d0e4 2026-10-31T20:15:17+00:00 TZ-38 report: the rule on contracts the Boss did not pick - NUMBER 2 of 2 twice; FINGERPRINT 67 of 67; HOST 11 of 11; SELFTEST 58 of 58; P-START 4 of 4; PLAN 895 symbols, 66677 keys; FETCH 66677 files; G-DATA 42 of 42 and G-EQUAL 20 of 20 in both runs; DETERMINISM 10 of 10, all nine files equal to the rehearsal; STILL 4 of 4; E1 and E2 UNDECIDABLE, E3 REPLICATED, an exploration that moves no rung; one block refused by the classifier and run by the Boss

A	CryptoReports/TZ-38-adv3-pit-validation-report.md
f7f7deb 2026-10-31T23:20:02+04:00 Add files via upload

A	CryptoTZ/TZ-38-adv3-pit-validation.md
```

**101 ref lines**: `HEAD`; 17 branches — `main` at `dd65a7e`, equal to `HEAD`, and 16 `tz-*` heads, `tz-38-adv3-pit-validation`
at `8f37199`; 37 `refs/pull/*/head`; 35 `pairbook-streams-*` and 8 `rewardbook-streams-*` tags — `pairbook-streams-1793502020`
and `rewardbook-streams-1793496620` new since TZ-38's §0.5, the archives' calendar runs of 2026-11-01 03:00:20 and 01:30:20
UTC — and the two annotated tags with their peeled lines. The branch count `0`. **`READING NUMBER: PASS - 2 of 2`.** `main`
carries revision `2026-10-31-c` (`30a577e`). The differences from map §1's record are recorded, not blocking.

---

## 1. Input

| input | read | size | hash / state |
|---|---|---|---|
| `CryptoTZ/TZ-39-advisor-checks.md` | in full; Appendix A extracted twice by §0.1's script | 4,323 lines, 347,992 bytes | `d7fd02b8…` |
| `SYSTEM-MAP.md` | §0 in full by `fingerprint`; the sections the header names | 2,003 lines, 504,061 bytes | `c2a31861…` |
| the map's 57 other rows | `fingerprint` | §0.1 | 55 `frozen` equal |
| `origin/main`'s `adv3.py`, `adv3-bot.py`, `RULE-ADV-3.txt`, the unit file and TZ-38's report | `I rule`, `git show` | — | `d73a657e…`, `3a044d50…`, `ee206e7c…`, `82acd8e4…`, `f4a0ac3f…` |
| `/var/lib/adv3-bot/journal.jsonl` | `I host` (ends in a newline), the marks (counts), `I render` (copied to the scratch journal, never printed), `I unit`, `I first` | 11,503 bytes at §0.3; 21,773 at §3.7 | 4 `daily` and 0 `check` records at both marks, 8 lines |
| `fapi.binance.com`, `api.telegram.org` | G-RENDER and P-START, through the service copy's own functions | — | §2.5, §2.6 |

**Nothing was re-collected**: this TZ collects no dataset. No file under `/etc/adv3-bot/` was read, copied, printed or
hashed by any command of the session; the token was read by the bot's own `--probe` alone, in the Boss's paste.

---

## 2. Measurements

### 2.1 §3.1 — the branch and its files (V3, V4)

`logs/05-branch.log`:

```
2026-11-01T06:23:08.146958279Z
fetch exit=0
CryptoTZ/TZ-39-advisor-checks.md
ok   CryptoTZ/ holds CryptoTZ/TZ-39-advisor-checks.md and no other file of that number
ok   CryptoReports/ holds no report of that number
READING NUMBER: PASS - 2 of 2
exit=0
Preparing worktree (new branch 'tz-39-advisor-checks')
branch 'tz-39-advisor-checks' set up to track 'origin/main'.
HEAD is now at dd65a7e Add files via upload
worktree exit=0
```

`logs/06-extract-wt.log` — §0.1's script, verbatim but for its argument, over the worktree: the three advisor files
overwritten, each after asserting it was the committed one by hash, and the checker created:

```
2026-11-01T06:23:23.494627179Z
/root/tz39-work/wt/advisor/adv3-bot.py 1558 99958 ca989b6fe487d41181b32312418d6acda1e9c64fbf5cfbb3f041d54826dd108f
/root/tz39-work/wt/advisor/adv3.py 871 49378 c19572dccf30a505342ca334e42c7ec347a5d29db4db20887229d2a8c7b48e31
/root/tz39-work/wt/advisor/selftest-adv3.py 235 16470 09d2ba9a8361ec5ebc7f5934ebb818d1a685bb16fb3f32b7da94409d9516cc0e
/root/tz39-work/wt/research/tz39-advisor-checks.py 1139 73892 18294b0916d77b226083a18f9521f06e2fddb423bbc947a2e1100fd42b2980f3
exit=0
add exit=0
M	advisor/adv3-bot.py
M	advisor/adv3.py
M	advisor/selftest-adv3.py
A	research/tz39-advisor-checks.py
1005	245	advisor/adv3-bot.py
118	64	advisor/adv3.py
42	8	advisor/selftest-adv3.py
1139	0	research/tz39-advisor-checks.py
```

The same lines, bytes and SHA-256 as §0.1, 4 of 4. `--name-status` printed exactly four lines, `M`, `M`, `M`, `A`;
`--numstat` exactly `1005 245`, `118 64`, `42 8` and `1139 0`.

`logs/07-commit-push.log`:

```
2026-11-01T06:23:38.975319639Z
commit exit=0
fc687582ebc4064b7483e2ac5cb9ca5b1af9c9f5 dd65a7e7fc108585fcfa18916eafcdec3cfd2f98 2026-11-01T06:23:38+00:00
 advisor/adv3-bot.py             | 1250 +++++++++++++++++++++++++++++++--------
 advisor/adv3.py                 |  182 ++++--
 advisor/selftest-adv3.py        |   50 +-
 research/tz39-advisor-checks.py | 1139 +++++++++++++++++++++++++++++++++++
 4 files changed, 2304 insertions(+), 317 deletions(-)
dd65a7e7fc108585fcfa18916eafcdec3cfd2f98	HEAD
dd65a7e7fc108585fcfa18916eafcdec3cfd2f98	refs/heads/main
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
101
remote: 
remote: Create a pull request for 'tz-39-advisor-checks' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-39-advisor-checks        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-39-advisor-checks -> tz-39-advisor-checks
branch 'tz-39-advisor-checks' set up to track 'origin/tz-39-advisor-checks'.
push exit=0
```

`logs/08-pr.log`:

```
2026-11-01T06:24:01.609876608Z
https://github.com/seahomebatumi-ai/btc-5m-twap/pull/39
exit=0
```

### 2.2 §3.2 — the self-tests and G-RULE (V5, V6): **53 of 53, 106 of 106, 64 of 64; RULE 10 of 10**

`logs/09-selftest-adv3.log`, `logs/10-selftest-bot.log`, `logs/11-selftest-checker.log` and `logs/12-rule.log`, each run
under `/usr/bin/time -f` (§6 item 3):

```
2026-11-01T06:24:12.521900645Z
SELFTEST-ADV3 PASS: 53 of 53 checks passed
wall 0.14 s, user 0.10 s, sys 0.01 s, maxrss 24764 KiB
exit=0
```

```
2026-11-01T06:24:12.674891179Z
SELFTEST PASS: 106 of 106 checks passed
wall 0.46 s, user 0.41 s, sys 0.01 s, maxrss 34144 KiB
exit=0
```

```
2026-11-01T06:24:13.142274910Z
SELFTEST PASS: 64 of 64 checks passed
wall 0.36 s, user 0.32 s, sys 0.01 s, maxrss 34500 KiB
exit=0
```

```
2026-11-01T06:24:13.506920843Z
ok   RULE-ADV-3.txt is main's, byte for byte, hashes to the RULE constant, and is the branch's adv3.py's
ok   the unit file is main's, byte for byte, and hashes to TZ-35's
ok   adv3.py: the definitions changed are exactly ['card_lines', 'message', 'trust_lines'], added ['assessment', 'changes'], removed []
ok   adv3.py: the 44 others identical by AST, the 14 rule functions among them
ok   adv3.py: the assignments changed are exactly [], added ['LADDER', 'PIT'], removed []
ok   adv3.py's PIT is TZ-38's report as committed (f4a0ac3f…), cell for cell
ok   adv3-bot.py: the definitions changed are exactly ['Telegram', 'handle', 'hello', 'make', 'plan_parts', 'probe', 'route', 'selftest', 'serve'], added ['alerted', 'alerts_of', 'append', 'base_record', 'candidate_lines', 'candidates', 'check', 'check_record', 'compose', 'done_after', 'due', 'event_lines', 'follow', 'followed_lines', 'forming_candles', 'hhmm', 'item_lines', 'journal_records', 'journal_scan', 'latest_slot', 'live_report', 'next_at', 'offers', 'quiet_line', 'ranked', 'slot_at', 'slot_key', 'slot_parse', 'slot_text', 'strong_shares', 'top_n', 'weak_lines', 'weakened', 'zone_lines', 'zones_left'], removed ['journal']
ok   adv3-bot.py: the 13 others identical by AST
ok   adv3-bot.py: the assignments changed are exactly ['(STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, CROWD, Z_CAP, LIQ_DAYS)', 'HELP'], added ['(SIDE, DOT)', 'ASSESS', 'BATUMI', 'CARD_KEYS', 'FOOTER', 'LIST_MAX', 'SLOTS'], removed ['DAILY']
ok   the branch's adv3.py, adv3-bot.py and selftest-adv3.py are Appendix A's
READING RULE: PASS - 10 of 10
wall 0.22 s, user 0.18 s, sys 0.02 s, maxrss 41488 KiB
exit=0
```

Under §6's bounds of `30` s each and `5` s a run for G-RULE: `0.14`, `0.46`, `0.36` and `0.22` s of wall; peaks
`24,764`, `34,144`, `34,500` and `41,488` KiB.

### 2.3 §3.3 — the directories beside this session, and B-RECLAIM-SCRATCH (V15)

`logs/12-scratch.log`:

```
2026-11-01T06:24:36.382551410Z
running 3435609 started 2026-10-30T13:15:54.700000Z claude
running 3435619 started 2026-10-30T13:15:56.710000Z claude
running 3435628 started 2026-10-30T13:15:58.010000Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
running 3435667 started 2026-10-30T13:16:00.220000Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
running 3435954 started 2026-10-30T13:18:48.500000Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
running 3760123 started 2026-11-01T06:20:18.640000Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
0f8f6761-2295-466b-9178-9b8a0261193e born 2026-11-01T06:20:19.000000Z: live, process [3760123]
238335b9-cf23-414a-8e8f-ad4705c4d19e born 2026-10-30T13:16:00.000000Z: live, process [3435609, 3435619, 3435628, 3435667]
716c29e7-4743-5553-ac5d-886f724de131 born 2026-10-31T19:20:48.000000Z: earlier
f00a192e-0435-4a82-9ad0-d54ae254a648 born 2026-10-31T19:20:47.000000Z: earlier
exit=0
```

Two directories named **earlier**, TZ-38's `716c29e7…` and `f00a192e…`, the two map §3 expects; two named **live** and not
touched: `0f8f6761…`, born with this session's process `3760123`, and `238335b9…`, the remote-control session of
2026-10-30. This session's own directory, `a2827336…`, is the `scratch` argument's own and is not listed.

**The Executor's `reclaim` was refused** — `logs/12a-reclaim-refused.log`:

```
2026-11-01T06:24:4xZ (the attempt; the refusal came before anything ran)
B-RECLAIM-SCRATCH's reclaim, the Executor's one attempt:
{ date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/btc-5m-twap/research/tz35-advisor-deploy.py reclaim /tmp/claude-0/-root-btc-5m-twap/716c29e7-4743-5553-ac5d-886f724de131 /tmp/claude-0/-root-btc-5m-twap/f00a192e-0435-4a82-9ad0-d54ae254a648; echo "exit=$?"; } >> /root/tz39-work/logs/12-reclaim-scratch.log 2>&1
Refused by the Claude Code auto mode classifier before it ran: "Permission for this action was denied by the Claude Code auto mode classifier. Reason: [Irreversible Local Destruction]."
Read after it at 2026-11-01T06:24:54Z: no 12-reclaim-scratch.log exists; both directories still listed under /tmp/claude-0/-root-btc-5m-twap/.
Handed to the Boss as §3.3's one line, unchanged but for the two full paths.
```

It went to the Boss as §3.3's one line, unchanged but for the two full paths written in, every removal chained by `&&` to
the `reclaim`'s `exit=0`, which it reaches only after `RECLAIM PASS`. **The Boss ran it at 07:07:42 UTC** —
`logs/12-reclaim-scratch.log`, verbatim; its first line opens with his terminal's OSC 133 marker, `ESC ] 133 ; C BEL`,
shown here as `cat -v` prints it, `^[]133;C^G`:

```
^[]133;C^G2026-11-01T07:07:42.533363444Z
reclaim: 3602 report tokens; forensic store holds 2312 files
RECLAIM PASS: 8 files considered, 0 named by a report, 0 kept by name, 0 copied, 0 already held; forensic store 2312 -> 2312 files
exit=0
2026-11-01T07:07:42.702738445Z
exit=0
exit=1
exit=0
exit=1
```

`RECLAIM PASS`: 8 files considered, none named by a report, none copied; the forensic store `2,312 → 2,312`. Each
`rm -rf` `exit=0` and each `test -e` `exit=1`. **The Executor's own read at 07:07:49 UTC:** `test -e` `exit=1` for
`716c29e7-4743-5553-ac5d-886f724de131` and for `f00a192e-0435-4a82-9ad0-d54ae254a648`; the parent then listed
`0f8f6761…`, `238335b9…` and `a2827336…` alone; `find /root/btc-forensics -type f | wc -l` `2312`. By §3.3 the block held
back nothing of §3.4 to §3.6, which ran before it.

### 2.4 §3.4 — B-DEPLOY (V7), in P-BOSS-A

**The Executor's B-DEPLOY was refused** — `logs/20a-b-deploy-refused.log`:

```
2026-11-01T06:26:0xZ (the attempt; the refusal came before anything ran)
B-DEPLOY, the Executor's one attempt: TZ-39 §3.4's block, verbatim (TZ line 270), submitted as a background command.
Refused by the Claude Code auto mode classifier before it ran: "Permission for this action was denied by the Claude Code auto mode classifier. Reason: [Production Deploy]."
Read after it at 2026-11-01T06:26:15Z: no 20-b-deploy.log and no state.json exist; /root/adv3-bot-svc/adv3.py d73a657e..., adv3-bot.py 3a044d50...; adv3-bot.service MainPID 3616193, NRestarts 2, active.
By §3.6, P-BOSS-A (B-DEPLOY, COPY, G-RENDER, P-START, B-KILL, UNIT-NEW, G-FIRST) is handed to the Boss unchanged, once B-DEPLOY's band is open (06:35:00 UTC).
```

By §3.6 the Executor waited for B-DEPLOY's band — a background wait ended at 06:35:00 UTC — read the host again
(06:35:07: the service copy `d73a657e…` and `3a044d50…`, pid `3616193`, `NRestarts` 2, no new log) and handed **P-BOSS-A**
over unchanged, TZ line 303 (3,041 bytes with its newline, SHA-256 `3c4b7dd8…`). The Boss ran it at 06:50:50 UTC. Its
first step — `logs/20-b-deploy.log`:

```
2026-11-01T06:50:50.938421051Z
mark deploy at 2026-11-01T06:50:50Z: bot pid 3616193 NRestarts 2, 4 daily and 0 check records, check-done -
exit=0
```

`exit=0`. `adv3.before`, `bot.before` and `commit.before` hash to `d73a657e…`, `3a044d50…` and the old `commit.txt`'s
`e14dba8b…` (§2.11). `adv3.py.new` and `adv3-bot.py.new` existed for the `mv` alone.

### 2.5 §3.4 — COPY and G-RENDER (V8, V9): **5 of 5, 22 of 22**

`logs/21-copy.log`:

```
2026-11-01T06:50:51.064023630Z
ok   the service copy holds adv3.py, adv3-bot.py and commit.txt only
ok   adv3.py is Appendix A's
ok   adv3-bot.py is Appendix A's
ok   commit.txt is the branch head and the worktree's HEAD
ok   the branch's two files equal the service copy's
READING COPY: PASS - 5 of 5
exit=0
2026-11-01T07:07:53.866771179Z
ok   the service copy holds adv3.py, adv3-bot.py and commit.txt only
ok   adv3.py is Appendix A's
ok   adv3-bot.py is Appendix A's
ok   commit.txt is the branch head and the worktree's HEAD
ok   the branch's two files equal the service copy's
READING COPY: PASS - 5 of 5
exit=0
```

`logs/22-render.log`:

```
2026-11-01T06:50:51.130221360Z
replies: 2025 chars in 1 parts, 3854 chars in 1 parts, 1974 chars in 1 parts, 2034 chars in 1 parts, 2528 chars in 1 parts, 874 chars in 1 parts, 874 chars in 1 parts; the bot's log: 8 lines; STRONG coins: 2; trades placed per allocation: 2, 2
signal check: loud, full, 1 parts; alerts {"candidate": 2, "signal": 1, "stop": 0}; offers read 16, followed 16; placed 2; zones left 0; forming candles read 0
fact check: quiet, one line, 1 parts; alerts {"candidate": 0, "signal": 0, "stop": 0}; offers read 16, followed 15; placed 2; zones left 0; forming candles read 7
ok   every command and both checks answered, no traceback and no failed request in the bot's log
ok   the markup is balanced in every message (b, i)
ok   «сигнал»: at most three cards, each with its basis, invalidation and confidence - the rung 1 or 0 - and no methodology
ok   «сигнал топ 7»: at most seven cards ranked of 7, each with its confidence, STRONG only among the first three
ok   «оценка»: the rung and the next readings, the six ratings, the forward record; STRONG at the lists' median, never the 42's
ok   the bot's constants are this TZ's: 14 % a stop, 5 USDT, 0.1 % of the volume, 1 % and 5 % of risk, three places, 0.1 % a side, a list of 7, checks at 00:10 and 12:10 UTC, the rung 1
ok   each allocation reply is the bot's own plan_parts of the report and liquidity it was made from
ok   plan: only STRONG coins of the report, in rank order, at most n and at most three, none added to fill
ok   plan: every STRONG coin is in the plan or named with a reason, once
ok   plan: every position has an entry and a stop within 14 % of it, on current prices
ok   plan: each loss at its stop within 1 % of the budget, all together within 5 %
ok   plan: whole positions of at least 5 USDT, together within the budget, free the budget less them
ok   plan: leverage the rule's formula and at most 20, the margin covering the position, a position within its liquidity cap
ok   the Boss's fields in each allocation reply - budget, count, allocated, free, and for each trade capital, leverage, margin, loss, stop, targets, invalidation and its confidence with the note that the sizes are unproven - and no six ratings
ok   «сигнал 15000 топ 5» says that STRONG is at most three
ok   «помощь» and an unknown text answer HELP and nothing else
ok   the signal check: quiet exactly when it holds no alert, one line only where it finds nothing, else the close's cards, candidates and offered trades
ok   the fact check: quiet exactly when it holds no alert, one line where it finds neither an alert nor a zone left, no card but a new candidate's
ok   the alerts of both checks are the exits of the offered trades by this checker's own walk, each once, and the new candidates
ok   the check records: their slots, every coin's state with the TOP-3 ranked, the six ratings, the placed coins
ok   the scratch journal holds, after the bot's own records, request, request, alloc, alloc, assess, check, check
ok   the bot's own journal, offset and daily-sent are as before the run, and no check-done file was written
READING RENDER: PASS - 22 of 22
exit=0
```

**G-RENDER read live data at 06:50:51 – 06:51:08 UTC**, about 17 s of wall from its `date -u` line to P-START's, under
`timeout 900`. The seven commands answered in one part each: «сигнал» 2,025 characters, «сигнал топ 7» 3,854,
«сигнал 10000 топ 3» 1,974, «сигнал 15000 топ 5» 2,034, «оценка» 2,528, «помощь» and «привет» 874 each (`HELP`). The
report held **2 STRONG coins**; each allocation placed **2** trades. **The signal check** was loud, the close's message in
full in one part, with **3 alerts — a signal ended (1) and new STRONG candidates (2), no stop** — 16 offers read and 16
followed, 2 coins placed, no zone; **the fact check** quiet, one line, no alert, 16 offers read, 15 followed, 2 placed, no
zone left, 7 forming candles read. Check (19) read every alert against the checker's own walk of every offer, each exit
once, and the candidates against the plan of the check before. Only counts and labels are printed, as §4.3 fixes.
Check (22): the bot's own `journal.jsonl`, `offset` and `daily-sent` hashed as before the run and no `check-done` was
written. `render-state/journal.jsonl` was never printed and never kept (§2.11).

### 2.6 §3.5 — P-START (V10): **served - 5 of 5 endpoints**

`logs/23-probe.log`:

```
2026-11-01T06:51:08.198021842Z
P-KLINES served: 1499 closed daily candles of BTCUSDT, the last 2026-10-31 - and the candle forming since 2026-11-01
P-FUNDING served: 5 settlement days of BTCUSDT since 2026-10-27
P-MARKS served: 945 perpetuals, all 42 coins among them with a mark price
P-INTERVALS served: 820 perpetuals with an adjusted funding interval, 42 of the coins among them
P-TELEGRAM served: bot @ClaudeCryptoSignal_bot
READING P-START: served - 5 of 5 endpoints
exit=0
```

Six requests to five endpoints at 06:51:08 UTC, every reply served and parsed, the forming candle among them; the bot's
username printed, neither the token nor a chat id.

### 2.7 §3.5 — B-KILL, UNIT-NEW and G-FIRST (V11, V12): **9 of 9, 7 of 7**

`logs/24-b-kill.log`:

```
2026-11-01T06:51:09.940115097Z
mark kill at 2026-11-01T06:51:09Z: bot pid 3616193 NRestarts 2, 4 daily and 0 check records, check-done -
exit=0
```

`mark kill` asserted `daily-sent` today's date, 2026-11-01, before the signal; `systemctl kill --signal=SIGTERM
adv3-bot.service` exited `0`. systemd's journal: SIGTERM to `3616193` at 06:51:10, the restart job at 06:51:40 —
`RestartSec=30` — and the new process `3766156`, started 06:51:39 UTC by its `/proc` stat (§2.9).

`logs/25-unit-new.log`:

```
2026-11-01T06:51:55.025800428Z
bot: pid 3766156 NRestarts 3 started 2026-11-01T06:51:39Z; captures: {"btc-pairbook.service": ["3738426", "16"], "btc-recorder.service": ["2388318", "0"], "btc-rewardbook.service": ["3137952", "1"]}
ok   the unit is active, running and enabled
ok   a new MainPID, one restart more
ok   the process started after the kill mark and within 90 s of it
ok   the process runs the unit's exact argv, alone
ok   the service copy's adv3.py and adv3-bot.py are the new ones, and the process started after the copy
ok   the unit file is unchanged
ok   no daily record since the mark
ok   the log shows the new process serving and no traceback since the mark
ok   the three capture units unchanged, each active
READING UNIT-NEW: PASS - 9 of 9
exit=0
2026-11-01T07:07:53.938675002Z
bot: pid 3766156 NRestarts 3 started 2026-11-01T06:51:39Z; captures: {"btc-pairbook.service": ["3738426", "16"], "btc-recorder.service": ["2388318", "0"], "btc-rewardbook.service": ["3137952", "1"]}
ok   the unit is active, running and enabled
ok   a new MainPID, one restart more
ok   the process started after the kill mark and within 90 s of it
ok   the process runs the unit's exact argv, alone
ok   the service copy's adv3.py and adv3-bot.py are the new ones, and the process started after the copy
ok   the unit file is unchanged
ok   no daily record since the mark
ok   the log shows the new process serving and no traceback since the mark
ok   the three capture units unchanged, each active
READING UNIT-NEW: PASS - 9 of 9
exit=0
```

`logs/26-first.log`:

```
2026-11-01T06:51:55.140804552Z
first check: loud, full, 1 messages; alerts {"candidate": 2, "signal": 1, "stop": 0}; followed 12; placed 2; check-done 2026-11-01 signal
ok   exactly one check record since the mark
ok   it is the day's signal check, of the close of the day before, under rule ee206e7c
ok   it was sent: its Telegram message ids
ok   it holds the 42 coins' state, the six ratings, its alerts and its placed coins, quiet exactly without an alert
ok   check-done names the slot it covers: 2026-11-01 signal
ok   the log since the mark: the new process serving from no check-done, the check sent, no check failed and no traceback
ok   the journal ends in a newline and every line since the mark parses
READING FIRST: PASS - 7 of 7
exit=0
2026-11-01T07:07:54.029567709Z
first check: loud, full, 1 messages; alerts {"candidate": 2, "signal": 1, "stop": 0}; followed 12; placed 2; check-done 2026-11-01 signal
ok   exactly one check record since the mark
ok   it is the day's signal check, of the close of the day before, under rule ee206e7c
ok   it was sent: its Telegram message ids
ok   it holds the 42 coins' state, the six ratings, its alerts and its placed coins, quiet exactly without an alert
ok   check-done names the slot it covers: 2026-11-01 signal
ok   the log since the mark: the new process serving from no check-done, the check sent, no check failed and no traceback
ok   the journal ends in a newline and every line since the mark parses
READING FIRST: PASS - 7 of 7
exit=0
```

**UNIT-NEW PASS 9 of 9** at the first run, 45 s after the mark; **G-FIRST PASS 7 of 7** at its first run. The new process
found no `check-done`, ran the day's signal check of the close of 2026-10-31 at its start and sent it at 06:51:46 UTC
(`service.log`: «check sent: 2026-11-01 signal for the close of 2026-10-31 | alerts 3 | loud | full»), 6 s after it began
serving — the second message of that close the Boss received today, after the old code's of 06:00:08 UTC, as §1 foresees.
`check-done` reads `2026-11-01 signal`: the mark came before 12:10 UTC, so the day's fact check at 12:10 UTC is the first
scheduled check the running unit sends (§3.7).

**The Executor's re-reads after the paste were refused** — `logs/27a-rereads-refused.log`:

```
2026-11-01T06:52:4xZ (the attempt; the refusal came before anything ran)
§3.6's reads after the paste - I copy, I unit new and I first again, by the Executor - the one attempt, appending to 21-copy.log, 25-unit-new.log and 26-first.log:
for m in "21-copy.log:copy" "25-unit-new.log:unit new" "26-first.log:first"; do f=${m%%:*}; c=${m#*:}; { date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz39-work/stage/research/tz39-advisor-checks.py $c; echo "exit=$?"; } >> /root/tz39-work/logs/$f 2>&1; done
Refused by the Claude Code auto mode classifier before it ran: "Permission for this action was denied by the Claude Code auto mode classifier. Reason: [Production Deploy]."
Read after it at 2026-11-01T06:52:51Z: 21-copy.log 8 lines, 25-unit-new.log 13 lines, 26-first.log 11 lines - each as P-BOSS-A left it; nothing appended.
Handed to the Boss unchanged (§3.6: a refused block is handed over unchanged).
```

They went to the Boss unchanged, and **he ran them at 07:07:53 UTC**, appending to the three logs above (their lines after
the paste's `exit=0`): COPY `PASS - 5 of 5`, UNIT-NEW `PASS - 9 of 9` — pid `3766156`, `NRestarts` 3, the capture units as
at the mark — and FIRST `PASS - 7 of 7`, the same one check record and `check-done` `2026-11-01 signal`, 16 minutes after
the first read. Every outcome above is the checker's own reading on the host, read by the Executor from the logs and
from §3.7's reads, never from the Boss's account.

### 2.8 §3.7 — the closing reads (V14)

`logs/27-closing-reads.log`, verbatim:

```
2026-11-01T06:53:11.473970469Z
MainPID=3766156
Result=success
NRestarts=3
MemoryCurrent=42020864
MemoryPeak=45731840
Nice=10
Id=adv3-bot.service
ActiveState=active
ActiveEnterTimestamp=Sun 2026-11-01 06:51:40 UTC

MainPID=2388318
Result=success
NRestarts=0
MemoryCurrent=12480512
MemoryPeak=318504960
Nice=0
Id=btc-recorder.service
ActiveState=active
ActiveEnterTimestamp=Fri 2026-10-23 06:08:56 UTC

MainPID=3738426
Result=success
NRestarts=16
MemoryCurrent=1798144
MemoryPeak=43880448
Nice=0
Id=btc-pairbook.service
ActiveState=active
ActiveEnterTimestamp=Sun 2026-11-01 03:06:45 UTC

MainPID=3137952
Result=success
NRestarts=1
MemoryCurrent=14172160
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
Mon 2026-11-02 01:30:20 UTC  18h Sun 2026-11-01 01:30:20 UTC 5h 22min ago btc-rewardbook-archive.timer btc-rewardbook-archive.service
Mon 2026-11-02 03:00:20 UTC  20h Sun 2026-11-01 03:00:20 UTC 3h 52min ago btc-pairbook-archive.timer   btc-pairbook-archive.service

2 timers listed.
enabled
exit=0
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
2026-11-01T06:51:10+00:00 vultr systemd[1]: adv3-bot.service: Sent signal SIGTERM to main process 3616193 (python) on client request.
2026-11-01T06:51:10+00:00 vultr systemd[1]: adv3-bot.service: Deactivated successfully.
2026-11-01T06:51:10+00:00 vultr systemd[1]: adv3-bot.service: Consumed 5.962s CPU time, 42.9M memory peak, 45.3M memory swap peak.
2026-11-01T06:51:40+00:00 vultr systemd[1]: adv3-bot.service: Scheduled restart job, restart counter is at 3.
2026-11-01T06:51:40+00:00 vultr systemd[1]: Started adv3-bot.service - ADV-3 advisor, the Boss's Binance Futures signals over Telegram.
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
2026-10-31T15:08:23Z candles refreshed to the close of 2026-10-30 | missing -
2026-10-31T15:08:26Z request answered for the close of 2026-10-30 | kind alloc
2026-10-31T15:21:01Z help sent
2026-10-31T15:36:51Z request answered for the close of 2026-10-30 | kind alloc
2026-10-31T15:39:11Z request answered for the close of 2026-10-30 | kind alloc
2026-11-01T06:00:06Z candles refreshed to the close of 2026-10-31 | missing -
2026-11-01T06:00:08Z daily sent for the close of 2026-10-31
2026-11-01T06:51:40Z serving the pinned chat: pid 3766156 offset 685120816 check-done -
2026-11-01T06:51:44Z candles refreshed to the close of 2026-10-31 | missing -
2026-11-01T06:51:46Z check sent: 2026-11-01 signal for the close of 2026-10-31 | alerts 3 | loud | full
/root/adv3-bot-svc:
total 164
drwxr-xr-x  2 root root  4096 Nov  1 06:50 .
drwx------ 31 root root  4096 Nov  1 06:21 ..
-rw-r--r--  1 root root 99958 Nov  1 06:50 adv3-bot.py
-rw-r--r--  1 root root 49378 Nov  1 06:50 adv3.py
-rw-r--r--  1 root root    41 Nov  1 06:50 commit.txt

/var/lib/adv3-bot:
total 52
drwx------  2 root root  4096 Nov  1 06:51 .
drwxr-xr-x 65 root root  4096 Oct 29 14:35 ..
-rw-r--r--  1 root root    17 Nov  1 06:51 check-done
-rw-r--r--  1 root root    10 Nov  1 06:00 daily-sent
-rw-r--r--  1 root root 21773 Nov  1 06:51 journal.jsonl
-rw-r--r--  1 root root     9 Oct 31 15:39 offset
-rw-r--r--  1 root root  4862 Nov  1 06:51 service.log
2026-11-01 signal               total        used        free      shared  buff/cache   available
Mem:      1002127360   834072576    80605184       40960   232165376   168054784
Swap:     3250581504   953434112  2297147392
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 11379015680
12451222	/root/tz39-work
149377	/root/adv3-bot-svc
26671	/var/lib/adv3-bot
250083857	/var/lib/btc-rewardbook
149316410	/var/lib/btc-pairbook
16	/root/.claude
{
 "marks": {
  "deploy": {
   "bot": {
    "ActiveState": "active",
    "MainPID": "3616193",
    "NRestarts": "2"
   },
   "caps": {
    "btc-pairbook.service": {
     "ActiveState": "active",
     "MainPID": "3738426",
     "NRestarts": "16"
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
   "check_done": null,
   "checks": 0,
   "daily": 4,
   "lines": 8,
   "t": 1793515850.9915044
  },
  "kill": {
   "bot": {
    "ActiveState": "active",
    "MainPID": "3616193",
    "NRestarts": "2"
   },
   "caps": {
    "btc-pairbook.service": {
     "ActiveState": "active",
     "MainPID": "3738426",
     "NRestarts": "16"
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
   "check_done": null,
   "checks": 0,
   "daily": 4,
   "lines": 8,
   "t": 1793515869.9834545
  }
 }
}
```

The `service.log` tail opens inside the traceback of 2026-10-31 01:13:52 UTC, the read timeout of a Telegram poll that
map §2.7 records (TZ-36); the process survived it, and no line since this TZ's marks is a traceback (UNIT-NEW, G-FIRST).

### 2.9 The unit's journal and record, before and after

| read | `journal.jsonl` | `daily` | `check` | `daily-sent` | `check-done` | `service.log` | pid / `NRestarts` |
|---|---|---|---|---|---|---|---|
| §0.3, 06:22:45 | 11,503 bytes | — | — | written 06:00 | absent | 4,592 bytes | `3616193` / 2 |
| `deploy` mark, 06:50:50 | 8 lines | 4 | 0 | 2026-11-01 (asserted at `kill`) | absent | — | `3616193` / 2 |
| `kill` mark, 06:51:09 | 8 lines | 4 | 0 | 2026-11-01 | absent | — | `3616193` / 2 |
| §3.7, 06:53:11 | 21,773 bytes | 4 (UNIT-NEW: none since the mark) | 1 (G-FIRST: exactly one since the mark) | written 06:00 | `2026-11-01 signal` | 4,862 bytes | `3766156` / 3 |

The new process's `service.log` lines since the mark: «serving the pinned chat: pid 3766156 offset 685120816 check-done -»
(06:51:40), «candles refreshed to the close of 2026-10-31 | missing -» (06:51:44), «check sent: 2026-11-01 signal for the
close of 2026-10-31 | alerts 3 | loud | full» (06:51:46). The capture units: the recorder `2388318`/0, the pair book
`3738426`/16 (active since 03:06:45 UTC, its archive's restart of the calendar run), the reward book `3137952`/1 — at the
host gate, at both marks and at §3.7.

### 2.10 Contract §4.2's self-check (V13) — after the push and the pull request, before the report's commit

`logs/28-separation.log`:

```
2026-11-01T06:53:32.337061833Z
fetch exit=0
$ git rev-list origin/main | grep -c fc687582ebc4064b7483e2ac5cb9ca5b1af9c9f5
0
$ git diff --name-only origin/main origin/tz-39-advisor-checks
advisor/adv3-bot.py
advisor/adv3.py
advisor/selftest-adv3.py
research/tz39-advisor-checks.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
grep exit=1
dd65a7e7fc108585fcfa18916eafcdec3cfd2f98
fc687582ebc4064b7483e2ac5cb9ca5b1af9c9f5
#39 OPEN head fc687582ebc4064b7483e2ac5cb9ca5b1af9c9f5 base main merged null
```

### 2.11 Every file the run wrote, by SHA-256, but the bot's own root and the render's scratch journal

`logs/29-files-written.log`:

```
2026-11-01T07:08:08.885949192Z
d73a657ef31decad276b858c4ec9672dce1c1c5cec36f0bb1c5b3378838224a8  ./adv3.before
3a044d50f51b16563b99bf1514ef92f35a9795b1fcc377aea6be4c23a31f7af2  ./bot.before
e14dba8be544c33838f0fbb526d2409db2e3dbeb76cef71f4416f8a40c0d3198  ./commit.before
6033e5ec926519511465e870244b8f4f0ca889f29d972398a6a77924b9d55bb2  ./fp-table.md
937d9fed74a3e46c493c6385da5e7f5362a16f23696e94628f5fa707131d6810  ./logs/00-start.log
198ddcebc091b242202aa811bd6da02961e223ebdff362a053d0751359996c42  ./logs/01-stage.log
2180b662cc16579292f9e6f8f741b62672fa998ea991478be96b57466259509e  ./logs/02-fingerprint.log
b71efb15479ddcd3c1a2f5b2f9d704ec8a5a66f5119a31a021d35814369959e2  ./logs/03-host.log
5baf24ed9f1ba98ba2503455c3f29951d24097cad9c4b0cebc707bfac5b81bed  ./logs/04-refs.log
8193246acf09abdf2137459e3d5b72ce9cf5717becefb0a55a1fd73d71f9f203  ./logs/05-branch.log
1cb5b5d14789880eeb34ffc5b4fcab8e724527cb46f1680a6b5e5e42f6759230  ./logs/06-extract-wt.log
00a93419d872e32ec8d7f1b5b62c63144b505b5506db202fd23c820709ac16c5  ./logs/07-commit-push.log
8e49d857c1d8c7bc0715c1d087c3f1bda0d584127c76003523628a3ee4356e6e  ./logs/08-pr.log
bc2973e07a16f019e34e7e29c4575a23eb9a9fbdea13fb30b21afe9dc44c83de  ./logs/09-selftest-adv3.log
b69b09a2424fb13d5e2c89cc461795d6386af601f6f81997cb12abd19096a545  ./logs/10-selftest-bot.log
55e59834f8c59fbc5f86de29ee47706504ecf177fe32b912af0c763b51a8e36f  ./logs/11-selftest-checker.log
781ef9fe63a4ba19331dbfcf9cf3df7e6c78a82e8218d10754dc64514214261e  ./logs/12a-reclaim-refused.log
c7d116239d5bc04227c710b4493eed5adb97fd0d0ff3e04796590cec2cbbd8ec  ./logs/12-reclaim-scratch.log
4ce742a9e8695be7917f4a82b6f52df1838131e604d2776130a234efae357c20  ./logs/12-rule.log
c67bd71429fb83d906570938ca52c6b11f5e174a8f264959c1a8079e801be5dd  ./logs/12-scratch.log
0fd538f8d57b9ba29db6d673cd2be40fb56d66731f5c5a75ea47c44fc311036d  ./logs/20a-b-deploy-refused.log
ee608acd4d296a16f23d31e9840dfb661712638ee047141aef930cc1dc8b8b3e  ./logs/20-b-deploy.log
d0e1f67d6d287cc24a589a7af4c316b3694ac3b96f98b20c9d0ed05360ccebb9  ./logs/21-copy.log
17eecde6e8169121b67e9ef884391dbe9614dc16e880c7163aff89dbfbd68cdc  ./logs/22-render.log
b230a6b20caf9d2abacf7d3373efa0c83b8af9936f18cb48a2a674c66ccfc28e  ./logs/23-probe.log
d6582c705ed7d3f0e7edd07bd74d3f0f053485711f71a410f408799ed51dae8c  ./logs/24-b-kill.log
32b8ad5fd859791c04744b283cc02e770b466944513956ca12de9424f328ff10  ./logs/25-unit-new.log
c533794e0d4345ac5d0de4a4b864bf8d74b94df19056546d35bd4d2e5f2ffa1a  ./logs/26-first.log
01e9c267a198fa2d89f31904e764f875e96624fcfcf5a9cab98e9aeb9fda6c4a  ./logs/27a-rereads-refused.log
5165455971f30c0c507b3274587832030cc28e94ed58251f75928375041f87f3  ./logs/27-closing-reads.log
70bd72a74bfe43b604a2887c52e1fb53596c4d6d239a81857fdabd6149415f10  ./logs/28-separation.log
99118b9fab89e98de84117f1900ca38e2b655b414b5cd89f8d0b75da60a72730  ./pr-body.md
19e0c6476bca5ee771815af5234353651c160666f318671925c2fd24b3d0ca15  ./report.tmpl.md
ca989b6fe487d41181b32312418d6acda1e9c64fbf5cfbb3f041d54826dd108f  ./stage/advisor/adv3-bot.py
c19572dccf30a505342ca334e42c7ec347a5d29db4db20887229d2a8c7b48e31  ./stage/advisor/adv3.py
09d2ba9a8361ec5ebc7f5934ebb818d1a685bb16fb3f32b7da94409d9516cc0e  ./stage/advisor/selftest-adv3.py
18294b0916d77b226083a18f9521f06e2fddb423bbc947a2e1100fd42b2980f3  ./stage/research/tz39-advisor-checks.py
cfaba41278e8ebe366d85186862438854c7ca62c5ce0f01c2a3c0d970b41113e  ./state.json
--- sizes
 43274 ./adv3.before
 49783 ./bot.before
    41 ./commit.before
  8064 ./fp-table.md
   168 ./logs/00-start.log
   521 ./logs/01-stage.log
 10324 ./logs/02-fingerprint.log
  4000 ./logs/03-host.log
  8322 ./logs/04-refs.log
   428 ./logs/05-branch.log
   742 ./logs/06-extract-wt.log
  2103 ./logs/07-commit-push.log
    94 ./logs/08-pr.log
   136 ./logs/09-selftest-adv3.log
   133 ./logs/10-selftest-bot.log
   131 ./logs/11-selftest-checker.log
   872 ./logs/12a-reclaim-refused.log
   297 ./logs/12-reclaim-scratch.log
  1675 ./logs/12-rule.log
   991 ./logs/12-scratch.log
   727 ./logs/20a-b-deploy-refused.log
   146 ./logs/20-b-deploy.log
   618 ./logs/21-copy.log
  3191 ./logs/22-render.log
   480 ./logs/23-probe.log
   144 ./logs/24-b-kill.log
  1538 ./logs/25-unit-new.log
  1500 ./logs/26-first.log
   930 ./logs/27a-rereads-refused.log
  8052 ./logs/27-closing-reads.log
   520 ./logs/28-separation.log
  1577 ./pr-body.md
 27074 ./report.tmpl.md
 99958 ./stage/advisor/adv3-bot.py
 49378 ./stage/advisor/adv3.py
 16470 ./stage/advisor/selftest-adv3.py
 73892 ./stage/research/tz39-advisor-checks.py
  1172 ./state.json
--- worktree files the run wrote (tracked, committed)
c19572dccf30a505342ca334e42c7ec347a5d29db4db20887229d2a8c7b48e31  wt/advisor/adv3.py
ca989b6fe487d41181b32312418d6acda1e9c64fbf5cfbb3f041d54826dd108f  wt/advisor/adv3-bot.py
09d2ba9a8361ec5ebc7f5934ebb818d1a685bb16fb3f32b7da94409d9516cc0e  wt/advisor/selftest-adv3.py
18294b0916d77b226083a18f9521f06e2fddb423bbc947a2e1100fd42b2980f3  wt/research/tz39-advisor-checks.py
status exit=0
--- render-state: names and sizes only (scratch, never printed or kept)
40064 journal.jsonl
--- the .before files
6d70c6aaa5457365743d2fb80e13e0817af8d292
```

`logs/29-files-written.log` does not list itself; its hash, and every kept file's, is `I keep`'s line in §2.16. The
worktree's four files are the committed ones, `git status --porcelain --ignored` empty. `fp-table.md`, `pr-body.md` and
`report.tmpl.md` are the Executor's working files (§6 item 5), not kept, removed with the tree; `sections.json.py`, this
report's section texts, was written after this listing and went with the tree too. `render-state/journal.jsonl`,
`40,064` bytes, is G-RENDER's scratch journal — a copy of the bot's own and the seven records the render appended, with the
day's cards — never printed, never hashed, not kept, removed with the tree. `commit.before`, `e14dba8b…`, holds
`6d70c6aaa5457365743d2fb80e13e0817af8d292` and a newline, TZ-37's commit. **In `/root/adv3-bot-svc/`**, not hashed by the
Executor (§6 item 1): `adv3.py` and `adv3-bot.py` asserted Appendix A's — `c19572dc…` and `ca989b6f…` — and `commit.txt`
asserted 40 hex characters and a newline equal to the branch head `fc687582ebc4064b7483e2ac5cb9ca5b1af9c9f5`, by COPY twice;
`ls -la` at §3.7: 49,378, 99,958 and 41 bytes, written 06:50 UTC. `adv3.py.new` and `adv3-bot.py.new` existed for the `mv`
alone. **Written by the unit itself, not by this TZ** (§2): `/var/lib/adv3-bot/check-done` and the `check` record. On
`main`: this report. In `/root/btc-forensics/`: `I keep`'s copies, §2.16.

### 2.12 Timeline

| UTC | step |
|---|---|
| 06:20:14 | the session; contract §1: pull, the TZ and the map read |
| 06:21:57 | §0.0 the work tree |
| 06:22:11 | §0.1 staged |
| 06:22:36 | §0.2 FINGERPRINT 67 of 67 |
| 06:22:45 | §0.3 HOST 16 of 16 |
| 06:23:00 | §0.5 refs, NUMBER 2 of 2 |
| 06:23:08 – 06:23:23 | §3.1 NUMBER 2 of 2, worktree, extraction |
| 06:23:38 | commit `fc68758`, push |
| 06:24:01 | pull request #39 |
| 06:24:12 – 06:24:13 | SELFTESTS, RULE 10 of 10 |
| 06:24:36 | §3.3 scratch |
| about 06:24:45 | the Executor's `reclaim` refused; handed to the Boss |
| about 06:26:05 | the Executor's B-DEPLOY refused |
| 06:35:00 – 06:35:07 | B-DEPLOY's band open; the host read; P-BOSS-A handed to the Boss |
| 06:50:50 | P-BOSS-A, the Boss: B-DEPLOY, mark `deploy` |
| 06:50:51 | COPY 5 of 5 |
| 06:50:51 – 06:51:08 | G-RENDER 22 of 22 |
| 06:51:08 | P-START 5 of 5 |
| 06:51:09 – 06:51:10 | B-KILL: mark `kill`, SIGTERM |
| 06:51:39 – 06:51:40 | the new process, serving |
| 06:51:46 | the first check sent |
| 06:51:55 | UNIT-NEW 9 of 9, G-FIRST 7 of 7, the Boss's paste |
| about 06:52:45 | the Executor's re-reads refused; handed to the Boss |
| 06:53:11 | §3.7's closing reads |
| 06:53:32 | contract §4.2 |
| 07:07:42 | B-RECLAIM-SCRATCH, the Boss: `reclaim` and two removals |
| 07:07:49 | the Executor's verification, `test -e` |
| 07:07:53 – 07:07:54 | the re-reads, the Boss: COPY 5 of 5, UNIT-NEW 9 of 9, FIRST 7 of 7 |
| 07:08:08 | the files written |
| 07:09:37 | §9 B-RECLAIM-OWN (§2.16), with this report drafted; then this report's commit |

### 2.13 Findings, recorded and gating nothing

1. **Claude Code's auto mode classifier refused three of this session's commands before they ran** — `reclaim` ("[Irreversible
   Local Destruction]"), B-DEPLOY ("[Production Deploy]"), the Executor's three re-reads of `I copy`, `I unit new` and `I first`
   ("[Production Deploy]"), modes that only read — and let through `fingerprint`, `host`, `number`, `rule`, the self-tests,
   `scratch`, §3.7's closing reads, B-RECLAIM-OWN's seven lines and every `git` and `gh` step. TZ-37's re-read of `I unit new` by the Executor was not
   refused; this one was.
2. **The first check sounded:** 3 alerts — a signal of a trade the cards offered ended at the close of 2026-10-31, and two
   STRONG candidates placed by the allocation, no check having come before it — as §1 expected of the first check. The
   live render, minutes earlier on a copy of the same journal, read the same kinds and counts at its signal check.
3. **The render followed 16 offers where the first check followed 12.** The render's scratch journal held, before its
   checks, the request and allocation records of its own seven commands, whose cards are offers by §1's rule; the unit's
   journal held none of them. [inferred from §1's rule and the render's order; the scratch journal was not printed]
4. **`apt-daily-upgrade.timer` read 06:59:49 UTC at §0.3**, inside the morning bands the TZ calls clear of the package
   manager's morning runs; the paste ran from 06:50:50 to 06:51:56, before it, and the closing reads at 06:53 found the
   capture units as at the marks.
5. **`du` of `/root/.claude` read `16` bytes at both reads**: the sessions' configuration directory is `/root/.claude-8j`,
   not read by this TZ.
6. **The remote-control session of 2026-10-30, `238335b9…`, still runs** (processes `3435609`, `3435619`, `3435628`,
   `3435667`, `3435954`); this session's process `3760123` made `0f8f6761…` at 06:20:19 UTC, and `a2827336…` is the scratchpad
   it names — the next TZ's to reclaim once no running `claude` process made them.

### 2.14 What the old process left and what the new one keeps

The old process `3616193` sent the day's 06:00 UTC message (`daily-sent` 2026-11-01, `service.log` 06:00:08) and was
signalled at 06:51:10; the new process ignores `daily-sent` and keeps its slots in `check-done`. Its next scheduled check is
2026-11-01 12:10 UTC, the fact check; nothing in this TZ waits for it.

### 2.15 Memory

The unit's `MemoryPeak` read `45,731,840` bytes at 06:53:11 UTC, two minutes into the new process, its first check
included, under `MemoryMax=128M`. G-RENDER's own peak was not read: the paste carries no timing wrapper.

### 2.16 §9 B-RECLAIM-OWN — last, after §3.7, with this report drafted (V15, V16)

Run from the session in one call, its first line `date -u +%FT%T.%NZ`, then §9's seven lines verbatim:

```
nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz39-work/stage/research/tz39-advisor-checks.py keep
git -C /root/btc-5m-twap worktree remove /root/tz39-work/wt; echo "exit=$?"
rm -rf /root/tz39-work; echo "exit=$?"
test -e /root/tz39-work; echo "exit=$?"
git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
find /root/btc-forensics -type f | wc -l
df -B1 --output=source,size,avail /var/lib/btc-recorder
```

None was refused. Its output was written to no file and is quoted here verbatim, every line:

```
2026-11-01T07:09:37.428753980Z
K copied d73a657ef31decad276b858c4ec9672dce1c1c5cec36f0bb1c5b3378838224a8 /root/btc-forensics/tz39-work--adv3.before
K copied 3a044d50f51b16563b99bf1514ef92f35a9795b1fcc377aea6be4c23a31f7af2 /root/btc-forensics/tz39-work--bot.before
K copied e14dba8be544c33838f0fbb526d2409db2e3dbeb76cef71f4416f8a40c0d3198 /root/btc-forensics/tz39-work--commit.before
K copied 937d9fed74a3e46c493c6385da5e7f5362a16f23696e94628f5fa707131d6810 /root/btc-forensics/tz39-work--logs--00-start.log
K copied 198ddcebc091b242202aa811bd6da02961e223ebdff362a053d0751359996c42 /root/btc-forensics/tz39-work--logs--01-stage.log
K copied 2180b662cc16579292f9e6f8f741b62672fa998ea991478be96b57466259509e /root/btc-forensics/tz39-work--logs--02-fingerprint.log
K copied b71efb15479ddcd3c1a2f5b2f9d704ec8a5a66f5119a31a021d35814369959e2 /root/btc-forensics/tz39-work--logs--03-host.log
K copied 5baf24ed9f1ba98ba2503455c3f29951d24097cad9c4b0cebc707bfac5b81bed /root/btc-forensics/tz39-work--logs--04-refs.log
K copied 8193246acf09abdf2137459e3d5b72ce9cf5717becefb0a55a1fd73d71f9f203 /root/btc-forensics/tz39-work--logs--05-branch.log
K copied 1cb5b5d14789880eeb34ffc5b4fcab8e724527cb46f1680a6b5e5e42f6759230 /root/btc-forensics/tz39-work--logs--06-extract-wt.log
K copied 00a93419d872e32ec8d7f1b5b62c63144b505b5506db202fd23c820709ac16c5 /root/btc-forensics/tz39-work--logs--07-commit-push.log
K copied 8e49d857c1d8c7bc0715c1d087c3f1bda0d584127c76003523628a3ee4356e6e /root/btc-forensics/tz39-work--logs--08-pr.log
K copied bc2973e07a16f019e34e7e29c4575a23eb9a9fbdea13fb30b21afe9dc44c83de /root/btc-forensics/tz39-work--logs--09-selftest-adv3.log
K copied b69b09a2424fb13d5e2c89cc461795d6386af601f6f81997cb12abd19096a545 /root/btc-forensics/tz39-work--logs--10-selftest-bot.log
K copied 55e59834f8c59fbc5f86de29ee47706504ecf177fe32b912af0c763b51a8e36f /root/btc-forensics/tz39-work--logs--11-selftest-checker.log
K copied c7d116239d5bc04227c710b4493eed5adb97fd0d0ff3e04796590cec2cbbd8ec /root/btc-forensics/tz39-work--logs--12-reclaim-scratch.log
K copied 4ce742a9e8695be7917f4a82b6f52df1838131e604d2776130a234efae357c20 /root/btc-forensics/tz39-work--logs--12-rule.log
K copied c67bd71429fb83d906570938ca52c6b11f5e174a8f264959c1a8079e801be5dd /root/btc-forensics/tz39-work--logs--12-scratch.log
K copied 781ef9fe63a4ba19331dbfcf9cf3df7e6c78a82e8218d10754dc64514214261e /root/btc-forensics/tz39-work--logs--12a-reclaim-refused.log
K copied ee608acd4d296a16f23d31e9840dfb661712638ee047141aef930cc1dc8b8b3e /root/btc-forensics/tz39-work--logs--20-b-deploy.log
K copied 0fd538f8d57b9ba29db6d673cd2be40fb56d66731f5c5a75ea47c44fc311036d /root/btc-forensics/tz39-work--logs--20a-b-deploy-refused.log
K copied d0e1f67d6d287cc24a589a7af4c316b3694ac3b96f98b20c9d0ed05360ccebb9 /root/btc-forensics/tz39-work--logs--21-copy.log
K copied 17eecde6e8169121b67e9ef884391dbe9614dc16e880c7163aff89dbfbd68cdc /root/btc-forensics/tz39-work--logs--22-render.log
K copied b230a6b20caf9d2abacf7d3373efa0c83b8af9936f18cb48a2a674c66ccfc28e /root/btc-forensics/tz39-work--logs--23-probe.log
K copied d6582c705ed7d3f0e7edd07bd74d3f0f053485711f71a410f408799ed51dae8c /root/btc-forensics/tz39-work--logs--24-b-kill.log
K copied 32b8ad5fd859791c04744b283cc02e770b466944513956ca12de9424f328ff10 /root/btc-forensics/tz39-work--logs--25-unit-new.log
K copied c533794e0d4345ac5d0de4a4b864bf8d74b94df19056546d35bd4d2e5f2ffa1a /root/btc-forensics/tz39-work--logs--26-first.log
K copied 5165455971f30c0c507b3274587832030cc28e94ed58251f75928375041f87f3 /root/btc-forensics/tz39-work--logs--27-closing-reads.log
K copied 01e9c267a198fa2d89f31904e764f875e96624fcfcf5a9cab98e9aeb9fda6c4a /root/btc-forensics/tz39-work--logs--27a-rereads-refused.log
K copied 70bd72a74bfe43b604a2887c52e1fb53596c4d6d239a81857fdabd6149415f10 /root/btc-forensics/tz39-work--logs--28-separation.log
K copied 7fee02c0311636a8354a65a4faf5bcb81afef0e31a6b68d878a1229133c8ab1f /root/btc-forensics/tz39-work--logs--29-files-written.log
K copied cfaba41278e8ebe366d85186862438854c7ca62c5ce0f01c2a3c0d970b41113e /root/btc-forensics/tz39-work--state.json
KEEP PASS: 32 files kept, 32 copied, 0 already held; forensic store 2312 -> 2344 files; worktree at fc687582ebc4064b7483e2ac5cb9ca5b1af9c9f5, its upstream's
exit=0
exit=0
exit=1
/root/btc-5m-twap       dd65a7e [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
2344
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 11378479104
```

**KEEP PASS: 32 files kept, 32 copied, 0 already held; the forensic store `2,312 → 2,344`**, equal to before plus the
copies — `state.json`, `adv3.before`, `bot.before`, `commit.before` and the 28 logs, by name — each hash equal to §2.11's
listing (`29-files-written.log`'s own, `7fee02c0…`, is `keep`'s). The branch worktree held exactly its pushed `HEAD`,
`fc687582…`, its upstream's, `git status --porcelain --ignored` empty, so `git worktree remove` needed no `--force`: `exit=0`.
`rm -rf /root/tz39-work` `exit=0`, `test -e` `exit=1`. **The worktrees registered are two:** the primary checkout and
`/root/btc-recorder-svc`. The branch `tz-39-advisor-checks` stays on `origin` and as a local ref. **Kept:** `/root/adv3-bot-svc/`,
the running unit's code; `/var/lib/adv3-bot/`, its record — `check-done` and the `check` record among it; `/etc/adv3-bot/`,
never read. `render-state/` went with the tree. **This session leaves two directories**, `a2827336-da6d-511b-b699-35cb76f477de`,
the scratchpad it names, and `0f8f6761-2295-466b-9178-9b8a0261193e`, born at 06:20:19 UTC with its process `3760123` — the
next TZ's to reclaim once no running `claude` process made them.

---

## 3. Publication

| item | value |
|---|---|
| branch | `tz-39-advisor-checks`, pushed 06:23:38 UTC through the URL's own credential, `gh`'s route not needed |
| commit | `fc687582ebc4064b7483e2ac5cb9ca5b1af9c9f5`, parent `dd65a7e7fc108585fcfa18916eafcdec3cfd2f98`, four files, `+2304 −317` (`1005 245`, `118 64`, `42 8`, `1139 0`) |
| pull request | #39, `https://github.com/seahomebatumi-ai/btc-5m-twap/pull/39`, base `main`, open, not merged |
| Release | none: this TZ publishes no asset |
| deployment | `/root/adv3-bot-svc/adv3.py`, `adv3-bot.py` and `commit.txt` replaced by the branch's at 06:50:50 UTC and the unit signalled at 06:51:10 — the TZ's own deployment (§3.4, §3.5), run by the Boss in P-BOSS-A after the classifier refused B-DEPLOY to the Executor; the merge stays the Boss's, after the verdict |
| separation self-check | §2.10: `0`; the four implementation files; nothing |
| report | this file, to `main` after B-RECLAIM-OWN |

---

## 4. Gate

| gate | PASS as the TZ fixes it (§4) | read | ratio | verdict |
|---|---|---|---|---|
| G-RULE | 10 of 10 | 10 of 10 | 1.000 | **PASS** |
| SELFTESTS | 53 of 53, 106 of 106 and 64 of 64 | 53, 106, 64 | 1.000 each | **PASS** |
| COPY | 5 of 5 | 5 of 5 | 1.000 | **PASS** |
| G-RENDER | 22 of 22 | 22 of 22 | 1.000 | **PASS** |
| P-START | `READING P-START: served - 5 of 5 endpoints` | served 5 of 5 | 1.000 | **PASS** |
| UNIT-NEW | 9 of 9 | 9 of 9 | 1.000 | **PASS** |
| G-FIRST | 7 of 7 | 7 of 7 | 1.000 | **PASS** |

Nothing was tuned and no gate reinterpreted. Per §4.5, a PASS establishes that the service copy's `adv3.py` and
`adv3-bot.py` are Appendix A's and the unit runs them; that the rule, its fourteen functions, the rule text, the unit and
the allocation's arithmetic are what TZ-35 to TZ-37 deployed; that the seven commands and both checks were answered on live
data with the shapes §4.2 fixes and, on that data — 2 STRONG coins, 2 trades placed in each allocation, a signal ended and
two candidates at the signal check — the allocation kept its limits and every exit of a trade the cards offered was
alerted once; and that the new process ran its first check at its start and sent it. **Not established:** that the 00:10
and 12:10 checks fire on their own clock; that the Boss's Telegram shows the messages as the Architect expects and that a
quiet one stays quiet on his phone; that the followed trades are the Boss's; that the sizes or the alerts are good ones;
and anything about the market to come.

---

## 5. Validation

| # | check | count | asserted? |
|---|---|---|---|
| **V1** | §0.2's fingerprint | `READING FINGERPRINT: PASS - 67 of 67`: revision `2026-10-31-c`; 6 anchors, 4 re-derived; 58 rows, 55 of 55 `frozen` equal; the shape | asserted by the checker (`verdict` raises, exit 1) |
| **V2** | §0.3's host gate | `READING HOST: PASS - 16 of 16`; the first memory read 217,165,824 bytes, no second read | asserted by the checker |
| **V3** | NUMBER at §0.5 and §3.1 | `PASS - 2 of 2` each, the `TZ-39-` path printed; the branch count `0` | NUMBER asserted by the checker; the branch count recorded, not asserted — read `0` by the Executor |
| **V4** | §0.1's and §3.1's files | 4 of 4 hashes at each, asserted by the script; lines and bytes equal; `M`, `M`, `M`, `A`; `--numstat` `1005 245`, `118 64`, `42 8`, `1139 0` | hashes asserted; the diff's names and numstat recorded, not asserted — compared by the Executor with §3.1's text, exact |
| **V5** | the self-tests | `53 of 53`, `106 of 106`, `64 of 64` | asserted, each in its own script |
| **V6** | G-RULE | `READING RULE: PASS - 10 of 10` | asserted by the checker |
| **V7** | B-DEPLOY | `exit=0`; the mark printed | the chain's `&&` stops at the first failure; `exit` recorded |
| **V8** | COPY | `READING COPY: PASS - 5 of 5` twice — in P-BOSS-A at 06:50:51 and in the Boss's re-read paste at 07:07:53 UTC | asserted by the checker |
| **V9** | G-RENDER | `READING RENDER: PASS - 22 of 22`; the replies' sizes; 2 STRONG coins; 2, 2 trades placed; the checks' flags and alerts by kind | asserted by the checker; the sizes and counts printed, not asserted |
| **V10** | P-START | `READING P-START: served - 5 of 5 endpoints`, each line printed | asserted by `adv3-bot.py --probe` |
| **V11** | B-KILL and UNIT-NEW | `exit=0`; `READING UNIT-NEW: PASS - 9 of 9` twice — 06:51:55 in P-BOSS-A and 07:07:53 UTC in the re-read paste; pids `3616193`, `3766156`; instants 06:51:09.983455 (mark) and 06:51:39 UTC (start) | UNIT-NEW asserted by the checker; `mark kill` asserted `daily-sent`; B-KILL's `exit` recorded |
| **V12** | G-FIRST | `READING FIRST: PASS - 7 of 7` twice — 06:51:55 and 07:07:54 UTC; loud, full, 1 message; alerts stop 0, signal 1, candidate 2; 12 followed; 2 placed; `check-done` `2026-11-01 signal` | asserted by the checker; the counts printed, not asserted |
| **V13** | contract §4.2's self-check | `0`; four files; nothing — after the push and the pull request, before the report's commit | recorded, not asserted |
| **V14** | §3.7's closing reads | every read printed, §2.8 | recorded, not asserted — no threshold |
| **V15** | B-RECLAIM-SCRATCH and §9's `keep` | `reclaim`, the Boss's, 07:07:42 UTC: `RECLAIM PASS`, 8 files considered, 0 named by a report, 0 copied, the store `2,312 → 2,312`; `keep`: 32 files kept, 32 copied, 0 held, the store `2,312 → 2,344`, equal to before plus the copies | asserted by `reclaim` and `keep` (the store's count) |
| **V16** | §9's removals | `git worktree remove` without `--force` `exit=0`; `rm -rf /root/tz39-work` `exit=0`; `test -e` `exit=1` for `/root/tz39-work` and for both scratch directories (§2.3: the Boss's and the Executor's reads); `git worktree list` naming `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else | exit codes recorded, not asserted |
| **V17** | every block refused and every paste the Boss ran | §2.3, §2.4, §2.7 and §6 item 1: each refusal's text, each paste, when he ran it, every line it appended, and the Executor's reads after it | recorded |

---

## 6. What could not be implemented as written

1. **Three refusals to the Executor, each run by the Boss.** Claude Code's auto mode classifier refused B-RECLAIM-SCRATCH's
   `reclaim` ("[Irreversible Local Destruction]"), B-DEPLOY ("[Production Deploy]") and the Executor's three re-reads after
   the paste — `I copy`, `I unit new`, `I first`, modes that only read ("[Production Deploy]") — each before it ran. After
   each refusal the Executor confirmed that nothing had changed (no log, no mark, the service copy's hashes, the unit's pid,
   the three logs' line counts as before) and recorded it in a log (`12a`, `20a`, `27a`). None was retried in another form.
   Each went to the Boss unchanged by §3.6 and map §7 item 138: the `reclaim` as §3.3's one line with the two full paths
   written in; B-DEPLOY as **P-BOSS-A**, TZ line 303 verbatim, handed over only at 06:35:00 UTC once B-DEPLOY's band was open,
   about 9 minutes after the refusal (§3.6: "the Executor waits for that band before handing it over"); the re-reads as the
   Executor's own command, verbatim. He ran P-BOSS-A at 06:50:50, the `reclaim` at 07:07:42 and the re-reads at 07:07:53 UTC.
   While P-BOSS-A ran, the Executor ran nothing that read the service copy or the unit; while the re-reads waited, it ran
   §3.7's closing reads — a step of its own, not a re-run of the refused modes — and contract §4.2's check. **Because the
   re-reads were refused as a deployment's, the Executor did not hash the service copy itself afterwards**; §2.11 cites
   COPY's assertions for those three files. A push notification of the hand-over was attempted once and not sent
   (Remote Control inactive); every hand-over was in the session's own messages.
2. **A routing note beside P-BOSS-A.** §0.3 read `apt-daily-upgrade.timer` next at 06:59:49 UTC, inside the morning bands,
   which the TZ's **When** calls clear of the package manager's morning runs. With the paste the Executor asked the Boss to
   run it before about 06:55 or after 07:10 UTC, so that a package upgrade restarting a capture unit could not fall inside
   UNIT-NEW's 100 s. The paste's text and its bands are the TZ's, unchanged; it ran 06:50:50 – 06:51:56, and the capture
   units read as at the marks at UNIT-NEW, at §3.7 and at the re-reads.
3. **A timing wrapper.** The three self-tests and G-RULE ran under `/usr/bin/time -f 'wall %e s, user %U s, sys %S s, maxrss
   %M KiB'`, one more line in each log; the commands under test and their arguments are §3.2's. G-RENDER, in the Boss's
   paste, ran without one, so its host peak was not read (§2.15).
4. **The logs' names.** §0.0 fixes the names of §3.4 to §3.6 and §4.4 — `20-b-deploy.log` to `26-first.log` — and §3.3's
   `12-reclaim-scratch.log`; the rest the Executor numbered in the TZ's order: `00-start.log`, `01-stage.log`,
   `02-fingerprint.log`, `03-host.log`, `04-refs.log`, `05-branch.log`, `06-extract-wt.log`, `07-commit-push.log`,
   `08-pr.log`, `09-selftest-adv3.log`, `10-selftest-bot.log`, `11-selftest-checker.log`, `12-rule.log`, `12-scratch.log`,
   `27-closing-reads.log`, `28-separation.log`, `29-files-written.log`, and the refusal records `12a-reclaim-refused.log`,
   `20a-b-deploy-refused.log`, `27a-rereads-refused.log`. `12-rule.log` and `12-scratch.log` share §3.3's number `12` with the
   TZ's own `12-reclaim-scratch.log`: the §3.2 logs were numbered before §3.3's name was reached. `00-start.log` records the
   heads and the `mkdir`'s `exit=0` after it ran. The Executor's re-reads appended to `21-copy.log`, `25-unit-new.log` and
   `26-first.log`, the logs §3.5 names for those modes.
5. **Working files.** In the work tree beside the logs: `pr-body.md`, the pull request's body; `fp-table.md`, §0.1's table
   built from `02-fingerprint.log`; `report.tmpl.md` and `sections.json.py`, this report's template and its sections — none
   kept, all removed with the tree. **Before §0.0's `mkdir`**, one file in the session's scratchpad: a copy of the map's §7
   rows the header cites, written to read them. Claude Code keeps each background command's output under the session's own
   `tasks/` — the band's waits and the monitors of the logs — beside the scratchpad (map §6, harness).
6. **Reads no step names**, each read-only, none under `/etc/adv3-bot/` and none printing a coin, a price or a size: before
   §0.0, `git status`, `git log`, `git fetch`, `ls`, `wc`, `sha256sum` and `date`, and the reads of the TZ and the map;
   after it, `ls` of the logs and of the session directories' parent, `systemctl show adv3-bot.service` and `sha256sum` of
   the service copy after B-DEPLOY's refusal (06:26:15) and at the band's opening (06:35:07), `systemctl show` of
   `apt-daily-upgrade.service` and `apt-daily.service` (06:27:22), `wc -l` of the logs, `cat -v` of every log the pastes
   wrote, a `grep` for control characters in the logs, `git log` of TZ-38's branch for the commit's form, `gh pr view 38`
   for the pull request's form, `sed` of TZ-37's report for this report's layout, and `get_session` for the model. The first `grep -c '^ok'` of the self-tests' logs counted
   nothing — they print their totals alone.
7. **The map read in sections** (map §7 items 139 and 141): its §0 in full by `fingerprint`, §1, §2.6, §2.7, the end of §3, §6's
   rows and §7 items 118, 124, 125, 129, 131, 132 and 136 to 142 — every section the header names but §2.5, whose archive's
   calendar run §0.3's timers printed — against contract §1 step 2's "in full". Appendix A's checker was read at its constants and the modes the run calls; the
   bot and `adv3.py` were not read line by line — their bytes are fixed by §0.1's hashes and their definitions by G-RULE.
8. **B-RECLAIM-OWN** ran from the session in one call, its output written to no file and quoted in §2.16.
