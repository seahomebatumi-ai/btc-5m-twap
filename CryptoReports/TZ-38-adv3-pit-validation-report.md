# TZ-38 report — the rule on contracts the Boss did not pick: ADV-3 run unchanged on every Binance USDⓈ-M USDT perpetual that traded, an entry allowed only where the contract was liquid before the day

**NUMBER PASS: 2 of 2** at §0.5 (19:22:45 UTC) and again at §3.1 (19:22:57 UTC): `CryptoTZ/` holds `TZ-38-adv3-pit-validation.md` and no other `TZ-38-` file, `CryptoReports/` no `TZ-38-` report; the branch count `0` before the push.
**FINGERPRINT PASS: 67 of 67** (map `2026-10-31-b`, 57 rows, 54 of 54 `frozen` equal, `adv3.py` `d73a657e…` by the loader) · **HOST PASS: 11 of 11** (`MemAvailable` 211,165,184 bytes at the first read, `/dev/vda2` free 10,089,811,968).
**SELFTEST PASS: 58 of 58** · **P-START: served - 4 of 4 endpoints**, under `User-Agent: btc-5m-twap-tz38`.
**PLAN:** 895 symbols, 66,677 keys, 3,771 listing calls, `plan.json` 4,932,756 bytes SHA-256 `83eb4f03…` — the Architect's plan byte for byte · **FETCH PASS:** 66,677 files, 67,600,876 bytes in 1,862 s, no planned key absent; `manifest.tsv` 9,337,085 bytes SHA-256 `16bcf7e3…`.
**G-DATA PASS: 42 of 42** and **G-EQUAL PASS: 20 of 20 (FACTS alone)**, in run A and in run B.
**DETERMINISM PASS: 10 of 10** — the nine files of A and B equal by SHA-256, and **all nine equal to the Architect's rehearsal of §4.6, `inputs.json` included**: no difference to report.
**STILL PASS: 4 of 4** — the three capture units and the advisor's unit as the mark has them (pids `2388318`, `3530053`, `3137952`, `3616193`).
**The readings (§2.7), an exploration re-derived that moves no rung:** the rule on *G* reads **UNDECIDABLE** (72 months, `p_t` up 0.0735, `p_boot` up 0.0815); STRONG on *G* **UNDECIDABLE** (`p_t` up 0.1100, `p_boot` up 0.1319); E3 at `V` = 30,000,000 **REPLICATED** (69 months, 0.0283 and 0.0275). STRONG on 500 random lists of 42: median mean R a trade **0.2195**; the Boss's 42 under the same admissibility exceed **0.914** of the lists.
**One block refused by the classifier and run by the Boss:** B-RECLAIM-SCRATCH's `reclaim` ("[Irreversible Local Destruction]"), run by him at 19:43:14 UTC and verified by the Executor. **Departures, all in §6.**

| field | value |
|---|---|
| TZ | `CryptoTZ/TZ-38-adv3-pit-validation.md`, 2,224 lines, 149,710 bytes, SHA-256 `a5f11311ecad494cc8bc2a75ea0a1b1022cae1b53c508266e324d6971fc94108`, landed at `f7f7deb` (2026-10-31 19:20:02 UTC), above the map's revision `2026-10-31-b` at `133d57f` (14:45:00 UTC) and PR #37's merge `d099851` |
| map revision | `2026-10-31-b`, equal; anchors 6 of 6; re-derived 4 of 4; rows 57; `frozen` equal 54 of 54; the map 1,985 lines, 493,445 bytes, SHA-256 `8d33d8d21d11f16871299246474f6144f3d6d94c0ae6c80c5acbee2a7efa280c`, the file TZ-38 §10 names |
| executor model | the model the TZ header names: `get_session` read `configured_model`, `session_context.model` and `external_metadata.last_served_model` all `claude-opus-5-5` |
| branch | `tz-38-adv3-pit-validation` at `8f37199aa4f9e14cb08534b1be3b7c258af917c2`, on `origin/main` `f7f7deb`; pushed; pull request #38, open, not merged |
| interpreter | `/root/tz04a-env/venv/bin/python` 3.12; every mode under `nice -n 19` and `-B` |
| instrument | `research/tz38-adv3-pit-validation.py`, 1,782 lines, 90,181 bytes, SHA-256 `579474b65329662f7bed735994381241a928a2c65a726cec3f933dc7afd4427b`, staged at `/root/tz38-work/stage/` and committed from `/root/tz38-work/wt/` |
| advisor | `advisor/adv3.py` `d73a657e…`, loaded by its hash and written never; no unit, service copy or record of the advisor touched |
| store | `/root/tz38-work/archive/`, 66,677 files of 67,600,876 bytes from `data.binance.vision`, fetched 19:30:24 – 20:01:27 UTC |
| runs | A 20:01:27 – 20:05:20 UTC (232.71 s), B 20:05:20 – 20:09:13 UTC (232.87 s); the band 06:35:00 – 20:30:00 UTC held at every start |
| mark | `state.json` 2026-10-31T19:25:04Z |
| blocks | B-RECLAIM-SCRATCH: refused to the Executor between 19:24:12 and 19:24:57 UTC, run by the Boss 19:43:14 UTC · B-RECLAIM-OWN: §2.13 |
| work tree | `/root/tz38-work/`, created 19:22:09 UTC, removed by B-RECLAIM-OWN (§2.13) |

---

## 0. Fingerprint

`I fingerprint`, from the staged copy of the instrument, against the primary checkout at `f7f7deb` — revision `2026-10-31-b`;
anchors `A1` `229a944f2d51`, `A2` `6c5089330629`, `A3` `0-complete / 1-student-5tau-not-disqualified /
2-no-edge-4tau-240-undecidable`, `A4` `437b45ea196b`, `A5` `0f6c90451cbd`, `A6` `729f0bcdbee3`, each equal to the TZ header's;
`A2`, `A4`, `A5` and `A6` re-derived. **V1: `READING FINGERPRINT: PASS - 67 of 67`.** The map, the `reported` row: 1,985 lines,
493,445 bytes, SHA-256 `8d33d8d21d11f16871299246474f6144f3d6d94c0ae6c80c5acbee2a7efa280c`.

### 0.1 The 57 rows of the map's §0 table

Built from `logs/03-fingerprint.log` by a substitution, each `frozen` row compared with the map's by the instrument (`ok   frozen …`).

| path | state | lines | bytes | SHA-256 (computed) | the map's |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | reported | 1,985 | 493,445 | `8d33d8d21d11f16871299246474f6144f3d6d94c0ae6c80c5acbee2a7efa280c` | self-reference |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | frozen | 234 | 11,128 | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | equal (frozen) |
| `research/twap-divergence.py` | frozen | 1,135 | 50,928 | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | equal (frozen) |
| `research/selftest-twap-divergence.py` | frozen | 376 | 16,736 | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | equal (frozen) |
| `research/tz02-distribution.py` | tracked | 334 | 14,511 | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | equal (tracked, no expectation) |
| `research/pfair.py` | frozen | 441 | 19,357 | `729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68` | equal (frozen) |
| `research/selftest-pfair.py` | frozen | 619 | 32,559 | `b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa` | equal (frozen) |
| `research/tz06-calibration.py` | frozen | 577 | 27,138 | `715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f` | equal (frozen) |
| `research/tz07a-variance-time.py` | frozen | 623 | 28,414 | `513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771` | equal (frozen) |
| `research/tz07b-settlement-dispersion.py` | frozen | 515 | 24,926 | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` | equal (frozen) |
| `research/tz08a-out-of-sample.py` | frozen | 745 | 38,822 | `37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c` | equal (frozen) |
| `research/tz09-disk-inventory.py` | frozen | 894 | 41,004 | `b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6` | equal (frozen) |
| `research/tz10b-sigma-or-link.py` | frozen | 1,224 | 61,018 | `406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088` | equal (frozen) |
| `research/tz11a-student-link.py` | frozen | 1,231 | 64,732 | `0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839` | equal (frozen) |
| `research/tz12-sized-gate.py` | frozen | 1,157 | 61,637 | `d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999` | equal (frozen) |
| `research/tz13-sized-gate-test3.py` | frozen | 1,074 | 53,901 | `a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd` | equal (frozen) |
| `research/tz14-quote-inventory.py` | frozen | 2,124 | 109,972 | `978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02` | equal (frozen) |
| `research/tz15-phase2-gate.py` | frozen | 1,517 | 73,799 | `66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3` | equal (frozen) |
| `research/tz16a-phase2-decisive-gate.py` | frozen | 2,198 | 111,192 | `3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125` | equal (frozen) |
| `research/tz17-settlement-chain.py` | frozen | 1,102 | 38,622 | `e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92` | equal (frozen) |
| `research/tz18a-chainbook-capture.py` | frozen | 1,683 | 69,517 | `e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae` | equal (frozen) |
| `research/tz20-capture-under-systemd.py` | frozen | 771 | 36,528 | `104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7` | equal (frozen) |
| `research/tz21-recorder-memory.py` | frozen | 1,284 | 59,009 | `d6d2dc195809f2160fda7856980d8ccfbf0006ba0836943ff789c877f9d5795f` | equal (frozen) |
| `research/tz23-maker-m0.py` | frozen | 1,184 | 54,885 | `6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f` | equal (frozen) |
| `research/tz24-nesting-b2.py` | frozen | 1,535 | 76,142 | `4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b` | equal (frozen) |
| `research/tz26-nesting-b3-capture.py` | frozen | 2,492 | 118,466 | `caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec` | equal (frozen) |
| `research/tz27-pairbook-archive.py` | frozen | 2,078 | 106,284 | `2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673` | equal (frozen) |
| `research/tz28-pairbook-archive-timer.py` | frozen | 1,438 | 74,576 | `46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4` | equal (frozen) |
| `research/tz29-maker-m0-second-look.py` | frozen | 1,225 | 68,959 | `18defff93d08c13ea4638a518c88a3fec5541fcf53fb6827451e727f2204d905` | equal (frozen) |
| `research/tz30-nesting-b3-measure.py` | frozen | 2,518 | 131,119 | `93dbbf1c4f84553a7bc041387ef92c3c0d8747c384d383b4fcd0b247fcd131ab` | equal (frozen) |
| `research/tz31-who-earns.py` | frozen | 1,523 | 84,775 | `7073188c8fbaa19568e8c6e4d6379e40ea57cf2a1341ebde0ea6a08f2c544765` | equal (frozen) |
| `research/tz32-our-quoting.py` | frozen | 2,576 | 138,209 | `6ec367e6ed995b315063d2d808dd6a3995878011afd76abfbb7b106b645a9c61` | equal (frozen) |
| `research/tz33-reward-book-capture.py` | frozen | 3,542 | 175,160 | `a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670` | equal (frozen) |
| `research/tz34-rewardbook-archive-timer.py` | frozen | 1,791 | 99,388 | `1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72` | equal (frozen) |
| `research/tz35-advisor-deploy.py` | frozen | 802 | 42,049 | `d50787db5113c3f748806a60a3e71211b665cb5235296e43d0e9a747a529e6f5` | equal (frozen) |
| `research/tz36-advisor-trust.py` | frozen | 582 | 32,925 | `a0fb9d53afe435d37354862eb8fd299256bf551fdbdb25a5c828d2cc7376d4f5` | equal (frozen) |
| `research/tz37-capital-allocation.py` | frozen | 808 | 51,269 | `eec1f30b971ed1d6db31e27eb0c321276c1b107a1654e013996d023b1a6a04eb` | equal (frozen) |
| `research/recorder/recorder.py` | frozen | 651 | 27,821 | `0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7` | equal (frozen) |
| `research/recorder/config.py` | frozen | 112 | 4,773 | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | equal (frozen) |
| `research/recorder/manifest.py` | frozen | 254 | 10,002 | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | equal (frozen) |
| `research/recorder/analyze.py` | frozen | 813 | 34,705 | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` | equal (frozen) |
| `research/recorder/probe.py` | frozen | 227 | 9,324 | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | equal (frozen) |
| `research/recorder/selftest.py` | frozen | 573 | 30,591 | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` | equal (frozen) |
| `deploy/systemd/btc-recorder.service` | frozen | 23 | 707 | `3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1` | equal (frozen) |
| `deploy/systemd/btc-chainbook.service` | frozen | 22 | 724 | `a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2` | equal (frozen) |
| `deploy/systemd/btc-pairbook.service` | frozen | 22 | 761 | `ba02fe4175b961c387ea8066eb084704e69efc7fd0a48d8f623a0198334f8dd8` | equal (frozen) |
| `deploy/systemd/btc-pairbook-archive.service` | frozen | 17 | 794 | `2e7fd45382af3da3b2ec29ced8d69870ef3d4481da4c6f327b90fc6cb5af78e7` | equal (frozen) |
| `deploy/systemd/btc-pairbook-archive.timer` | frozen | 13 | 417 | `07581f4f331fbf9d2a1113cac42a2872d65ac69a872991bff7d2bda235eac913` | equal (frozen) |
| `deploy/systemd/btc-rewardbook.service` | frozen | 23 | 817 | `7691720c7b2261a606af54bfa20b5068b89455ea54512c55dde861d6d8063bec` | equal (frozen) |
| `deploy/systemd/btc-rewardbook-archive.service` | frozen | 17 | 810 | `a9abb1f092b3fb8359d37ea88df00dca8557d0f0482d04c12f0fbdd32601e33f` | equal (frozen) |
| `deploy/systemd/btc-rewardbook-archive.timer` | frozen | 13 | 428 | `bf5af0252c420d8db1579b82e5da21472cdb6bc871fa8035ecf6f1edc9720a0f` | equal (frozen) |
| `deploy/systemd/adv3-bot.service` | frozen | 27 | 863 | `82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66` | equal (frozen) |
| `advisor/RULE-ADV-3.txt` | frozen | 33 | 3,203 | `ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169` | equal (frozen) |
| `advisor/adv3.py` | frozen | 817 | 43,274 | `d73a657ef31decad276b858c4ec9672dce1c1c5cec36f0bb1c5b3378838224a8` | equal (frozen) |
| `advisor/adv3-bot.py` | frozen | 798 | 49,783 | `3a044d50f51b16563b99bf1514ef92f35a9795b1fcc377aea6be4c23a31f7af2` | equal (frozen) |
| `advisor/selftest-adv3.py` | frozen | 201 | 12,600 | `ef4ffc44e6f8bcdd5685fc1db9090957890c6e2ab762cdad8ae9826b18cf1395` | equal (frozen) |
| `.gitignore` | tracked | 5 | 252 | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | equal (tracked, no expectation) |

### 0.2 `logs/03-fingerprint.log`, verbatim (V1)

```
2026-10-31T19:22:31.980738124Z
reported 1985 lines 493445 bytes 8d33d8d21d11f16871299246474f6144f3d6d94c0ae6c80c5acbee2a7efa280c SYSTEM-MAP.md
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
ok   revision 2026-10-31-b
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
ok   the table holds 57 rows, 54 frozen, 2 tracked, 1 reported
ok   advisor/adv3.py hashes to the SHA-256 the instrument loads it by, d73a657e
READING FINGERPRINT: PASS - 67 of 67
exit=0
```

### 0.3 Contract §1, §0.0 and §0.1 — the start-up, the work tree and the file staged (V4)

Contract §1 step 1: `git fetch origin` and `git pull origin main` on `main`, a fast-forward from `7600235` to `f7f7deb` —
`d099851` (PR #37's merge), `133d57f` (the map) and `f7f7deb` (this TZ). Step 2: this TZ in full; the map in the sections the
TZ rests on (§6 item 6). Steps 3 and 4: `I fingerprint`, §0.2. Step 5: the model, the field table.

`logs/01-work-tree.log`, written after the `mkdir` from its captured output:

```
2026-10-31T19:22:09.222898926Z
$ mkdir /root/tz38-work /root/tz38-work/logs; echo "exit=$?"
exit=0
```

`logs/02-stage.log` — §0.1's script, verbatim, over an empty `stage/` (lines, bytes and SHA-256 equal to §0.1's table: 1782,
90,181, `579474b6…`):

```
2026-10-31T19:22:26.921474408Z
/root/tz38-work/stage/research/tz38-adv3-pit-validation.py 1782 90181 579474b65329662f7bed735994381241a928a2c65a726cec3f933dc7afd4427b
exit=0
```

### 0.4 Host gate — §0.3's block, verbatim (V2)

`S` was `/tmp/claude-0/-root-btc-5m-twap/716c29e7-4743-5553-ac5d-886f724de131/scratchpad`, the scratchpad the session's system
prompt names. `logs/04-host.log`:

```
Sat Oct 31 07:22:37 PM UTC 2026
1793474557
2026-08-02 07:24:32
1
MemTotal:         978640 kB
MemAvailable:     200548 kB
SwapTotal:       3174396 kB
SwapFree:        2339792 kB
units: {"adv3-bot.service": {"ActiveState": "active", "MainPID": "3616193", "NRestarts": "2", "SubState": "running", "UnitFileState": "enabled"}, "btc-pairbook.service": {"ActiveState": "active", "MainPID": "3530053", "NRestarts": "15", "SubState": "running", "UnitFileState": "enabled"}, "btc-recorder.service": {"ActiveState": "active", "MainPID": "2388318", "NRestarts": "0", "SubState": "running", "UnitFileState": "enabled"}, "btc-rewardbook.service": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1", "SubState": "running", "UnitFileState": "enabled"}}
MemAvailable first 211165184 bytes, second not read, deciding 211165184; /dev/vda2 free 10089811968 bytes
ok   H1 the recorder's manifest.json is found
ok   H2 /dev/vda2 of 31612203008 bytes
ok   H2 the recorder's runtime record names e3975b5
ok   H3 the venv interpreter is Python 3.12
ok   H4 btc-recorder.service active and enabled
ok   H4 btc-pairbook.service active and enabled
ok   H4 btc-rewardbook.service active and enabled
ok   H5 adv3-bot.service active, running and enabled
ok   H6 the work tree holds nothing but logs/ and stage/
ok   memory gate: MemAvailable at least 122462208 bytes, a first read below it read again after 60 s
ok   disk gate: /dev/vda2 free at least 7700000000 bytes
READING HOST: PASS - 11 of 11
exit=0
NEXT                        LEFT LAST                              PASSED UNIT                         ACTIVATES
Sun 2026-11-01 01:30:20 UTC   6h Sat 2026-10-31 01:30:20 UTC      17h ago btc-rewardbook-archive.timer btc-rewardbook-archive.service
Sun 2026-11-01 02:05:43 UTC   6h Sat 2026-10-31 17:34:39 UTC 1h 47min ago apt-daily.timer              apt-daily.service
Sun 2026-11-01 03:00:20 UTC   7h Sat 2026-10-31 03:00:20 UTC      16h ago btc-pairbook-archive.timer   btc-pairbook-archive.service
Sun 2026-11-01 06:59:49 UTC  11h Sat 2026-10-31 06:38:15 UTC      12h ago apt-daily-upgrade.timer      apt-daily-upgrade.service

4 timers listed.
627183082	/var/lib/btc-rewardbook
1067038038	/var/lib/btc-pairbook
14684	/var/lib/adv3-bot
16	/root/.claude
2267
/root/btc-5m-twap       f7f7deb [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/tmp/claude-0/-root-btc-5m-twap/716c29e7-4743-5553-ac5d-886f724de131/scratchpad
total 28
drwx------  7 root root 4096 Oct 31 19:20 .
drwx------ 35 root root 4096 Oct 31 19:20 ..
drwx------  3 root root 4096 Oct 30 13:16 238335b9-cf23-414a-8e8f-ad4705c4d19e
drwx------  3 root root 4096 Oct 31 13:14 50f7dcda-5a03-4e54-8f23-a03fd054d0b0
drwx------  4 root root 4096 Oct 31 19:20 716c29e7-4743-5553-ac5d-886f724de131
drwx------  3 root root 4096 Oct 31 19:20 f00a192e-0435-4a82-9ad0-d54ae254a648
drwx------  4 root root 4096 Oct 31 13:14 f13dd443-b053-5e1f-ab49-f3593ec7b06b
```

**V2: `READING HOST: PASS - 11 of 11`.** The memory gate read `211,165,184` bytes at its first read, above the floor
`122,462,208`, so no second read was made; the `/proc/meminfo` line the same block printed just before read `200,548 kB`. Printed, no
threshold: the forensic store `2,267` files, map §3's count; two worktrees, map §3's two; the scratch listing names
`238335b9…` (the live session of 2026-10-30), TZ-37's `50f7dcda…` and `f13dd443…`, this session's own `716c29e7…`, and
`f00a192e…`, born at 19:20:47 UTC with this session's process (§2.3).

### 0.5 Free space and `MemAvailable` — every read, its instant and its bound

| instant (UTC) | read by | `MemAvailable` bytes | `SwapFree` bytes | `/dev/vda2` free bytes |
|---|---|---|---|---|
| 19:22:37 | §0.3's `grep` | 205,361,152 (200,548 kB) | 2,395,947,008 (2,339,792 kB) | — |
| 19:22:37 | `I host`, the gate | 211,165,184 | — | 10,089,811,968 |
| between 19:30:24 and 19:43:49, instant not recorded | the Executor's read during the fetch (§6 item 7) | 186,265,600 (181,900 kB) | 2,264,317,952 (2,211,248 kB) | 9,918,144,512 |
| 19:44:54 | the Executor's read during the fetch (§6 item 7) | 152,915,968 (149,332 kB) | 2,271,428,608 (2,218,192 kB) | 9,907,232,768 |
| 20:01:27 | before run A (`16-run-A.log`) | 198,590,464 (193,936 kB) | 2,277,183,488 (2,223,812 kB) | — |
| 20:05:20 | before run B (`17-run-B.log`) | 251,850,752 (245,948 kB) | 2,211,573,760 (2,159,740 kB) | — |
| 20:09:23 | §3.7 (`19-closing.log`) | 171,147,264 (167,136 kB) | 2,248,306,688 (2,195,612 kB) | 9,709,277,184 |
| §2.13 | B-RECLAIM-OWN's `df` | — | — | 10,001,342,464 (20:13:56) |

The bounds: `MemAvailable` at least `122,462,208` (§0.4) — the lowest read, `152,915,968`, is above it; `/dev/vda2` free at
least `7,700,000,000` — the lowest read, `9,709,277,184`, is above it. The reward book's `STREAM_FLOOR`, `7,300,000,000`, was
never approached.

### 0.6 Refs and the number (§0.5) — `logs/05-refs-number.log`, verbatim (V3)

```
2026-10-31T19:22:45.309585077Z
exit=0
f7f7deb1e05bddd480c1249cb765ce83ee1296f4	HEAD
f7f7deb1e05bddd480c1249cb765ce83ee1296f4	refs/heads/main
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
CryptoTZ/TZ-38-adv3-pit-validation.md
ok   CryptoTZ/ holds CryptoTZ/TZ-38-adv3-pit-validation.md and no other file of that number
ok   CryptoReports/ holds no report of that number
READING NUMBER: PASS - 2 of 2
exit=0
f7f7deb 2026-10-31T23:20:02+04:00 Add files via upload

A	CryptoTZ/TZ-38-adv3-pit-validation.md
133d57f 2026-10-31T18:45:00+04:00 Update SYSTEM-MAP.md

M	SYSTEM-MAP.md
d099851 2026-10-31T18:42:44+04:00 Merge pull request #37 from seahomebatumi-ai/tz-37-capital-allocation

M	advisor/adv3-bot.py
A	research/tz37-capital-allocation.py
7600235 2026-10-31T14:05:16+00:00 TZ-37 report: trigger commands and capital allocation - NUMBER 2 of 2 twice; G-RULE 7 of 7; SELFTESTS 44, 67 and 50; B-DEPLOY, COPY 5 of 5, G-RENDER 16 of 16 (3 STRONG, 2 placed in each allocation), P-START 5 of 5; B-KILL and UNIT-NEW 9 of 9, pid 3574987 to 3616193; three blocks refused by the classifier and run by the Boss; no rollback; the unit runs 3a044d50

A	CryptoReports/TZ-37-capital-allocation-report.md
0e987e1 2026-10-31T17:12:23+04:00 Update SYSTEM-MAP.md

M	SYSTEM-MAP.md
```

Every ref is printed. `wc -l` printed `0`: the branch did not exist. `I number` printed `READING NUMBER: PASS - 2 of 2` with the
`TZ-38-` path. `main` at `f7f7deb` carries revision `2026-10-31-b` (`133d57f`). Against the record at the start of map §1
(2026-10-29, 15:25 UTC) the refs add `tz-36-advisor-trust-block` and `tz-37-capital-allocation`, the branches TZ-36 and TZ-37
pushed and kept, and `main` has moved on; recorded, not blocking.

---

## 1. Input

| input | what | size | hash | re-collected? |
|---|---|---|---|---|
| this TZ | `CryptoTZ/TZ-38-adv3-pit-validation.md` at `f7f7deb` | 2,224 lines, 149,710 bytes | `a5f11311…` | no |
| the map | `SYSTEM-MAP.md` at `f7f7deb` | 1,985 lines, 493,445 bytes | `8d33d8d2…` | no |
| the advisor | `advisor/adv3.py` of the primary checkout, loaded by hash | 817 lines, 43,274 bytes | `d73a657e…` | no |
| TZ-35's checker | `research/tz35-advisor-deploy.py` of `main`, for `scratch` and `reclaim` | 802 lines, 42,049 bytes | `d50787db…` | no |
| the plan | `plan.json`, the bucket's listing at 19:25:39 – 19:30:24 UTC: 895 symbols, 66,677 keys, 3,771 listing calls | 4,932,756 bytes | `83eb4f03ee3c2639894d2019a67539c5156dad97a33df2149512709dea5bb098` | **collected by this TZ**, equal to the Architect's of §3.5 |
| the store | `/root/tz38-work/archive/`, every planned key from `data.binance.vision`, verbatim | 66,677 files, 67,600,876 bytes | `manifest.tsv` 9,337,085 bytes, `16bcf7e37448b5b06033fa548178572a22ffaf4b1d407ca68d287f5250920bac` | **collected by this TZ** |

The store holds Binance's public daily candles and funding files. It was not committed, copied or quoted, and B-RECLAIM-OWN
removed it with the work tree. The plan of this day lists the same keys as the Architect's listing of the same day: October's
monthly files were not yet published at 19:25 UTC. The run reads 612 contracts: *L* 609, *G* 570, the Boss's 42, 28 contracts
in *L* that ended (`sets`, §2.6).

---

## 2. Measurements

### 2.1 §3.1 — the branch and its file (V3, V4)

`logs/06-branch.log`:

```
2026-10-31T19:22:57.954870448Z
exit=0
CryptoTZ/TZ-38-adv3-pit-validation.md
ok   CryptoTZ/ holds CryptoTZ/TZ-38-adv3-pit-validation.md and no other file of that number
ok   CryptoReports/ holds no report of that number
READING NUMBER: PASS - 2 of 2
exit=0
Preparing worktree (new branch 'tz-38-adv3-pit-validation')
branch 'tz-38-adv3-pit-validation' set up to track 'origin/main'.
HEAD is now at f7f7deb Add files via upload
exit=0
```

`logs/07-extract-wt.log` — §0.1's script again, verbatim but for its argument `/root/tz38-work/wt`; the same line, bytes and
SHA-256 as at §0.1; then `git add`, `--name-status` and `--numstat`:

```
2026-10-31T19:22:58.572801639Z
/root/tz38-work/wt/research/tz38-adv3-pit-validation.py 1782 90181 579474b65329662f7bed735994381241a928a2c65a726cec3f933dc7afd4427b
exit=0
exit=0
A	research/tz38-adv3-pit-validation.py
1782	0	research/tz38-adv3-pit-validation.py
```

`--name-status` printed exactly one line, `A` for the instrument, and `--numstat` exactly `1782	0	research/tz38-adv3-pit-validation.py`,
as §3.1 requires. `logs/08-commit-push.log` (the remote's URL printed by no line; the push went through the URL's own
credential, `gh`'s helper not needed):

```
2026-10-31T19:23:09.769972136Z
exit=0
8f37199aa4f9e14cb08534b1be3b7c258af917c2 f7f7deb1e05bddd480c1249cb765ce83ee1296f4 TZ-38: the rule on contracts the Boss did not pick - research/tz38-adv3-pit-validation.py added
 research/tz38-adv3-pit-validation.py | 1782 ++++++++++++++++++++++++++++++++++
 1 file changed, 1782 insertions(+)
f7f7deb1e05bddd480c1249cb765ce83ee1296f4	HEAD
f7f7deb1e05bddd480c1249cb765ce83ee1296f4	refs/heads/main
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
remote: 
remote: Create a pull request for 'tz-38-adv3-pit-validation' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-38-adv3-pit-validation        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-38-adv3-pit-validation -> tz-38-adv3-pit-validation
branch 'tz-38-adv3-pit-validation' set up to track 'origin/tz-38-adv3-pit-validation'.
exit=0
8f37199aa4f9e14cb08534b1be3b7c258af917c2	refs/heads/tz-38-adv3-pit-validation
```

`logs/09-pull-request.log`:

```
2026-10-31T19:23:27.105381359Z
https://github.com/seahomebatumi-ai/btc-5m-twap/pull/38
exit=0
{"baseRefName":"main","headRefOid":"8f37199aa4f9e14cb08534b1be3b7c258af917c2","number":38,"state":"OPEN","url":"https://github.com/seahomebatumi-ai/btc-5m-twap/pull/38"}
```

### 2.2 §3.2 — the self-test (V5): **58 of 58**

`logs/10-selftest.log`, under `/usr/bin/time -v` (§6 item 4):

```
2026-10-31T19:23:37.980611514Z
SELFTEST PASS: 58 of 58 checks passed
	Command being timed: "nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz38-work/stage/research/tz38-adv3-pit-validation.py selftest"
	User time (seconds): 12.35
	System time (seconds): 0.08
	Percent of CPU this job got: 94%
	Elapsed (wall clock) time (h:mm:ss or m:ss): 0:13.20
	Average shared text size (kbytes): 0
	Average unshared data size (kbytes): 0
	Average stack size (kbytes): 0
	Average total size (kbytes): 0
	Maximum resident set size (kbytes): 39720
	Average resident set size (kbytes): 0
	Major (requiring I/O) page faults: 5
	Minor (reclaiming a frame) page faults: 7582
	Voluntary context switches: 264
	Involuntary context switches: 5475
	Swaps: 0
	File system inputs: 7776
	File system outputs: 3208
	Socket messages sent: 0
	Socket messages received: 0
	Signals delivered: 0
	Page size (bytes): 4096
	Exit status: 0
exit=0
2026-10-31T19:23:51.189917614Z
```

The self-test prints its count alone. Its `ok` appends a check's name and asserts it before the next runs, so `58 of 58` means
58 asserts held. Among them, at the instrument's lines 1455–1462, are the causality check by perturbation — the volumes from index
60 on multiplied by 1,000 leave the flags up to index 60 bit-identical — and its negative control, the flags after it changing.

### 2.3 §3.3 — the directories beside this session, and B-RECLAIM-SCRATCH (V15)

`logs/11-scratch.log` — TZ-35's `scratch`, with `"$(dirname "$S")"` the session's own directory `716c29e7…`:

```
2026-10-31T19:24:12.703167797Z
running 3435609 started 2026-10-30T13:15:54.700000Z claude
running 3435619 started 2026-10-30T13:15:56.710000Z claude
running 3435628 started 2026-10-30T13:15:58.010000Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
running 3435667 started 2026-10-30T13:16:00.220000Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
running 3435954 started 2026-10-30T13:18:48.500000Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
running 3674404 started 2026-10-31T19:20:46.520000Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
238335b9-cf23-414a-8e8f-ad4705c4d19e born 2026-10-30T13:16:00.000000Z: live, process [3435609, 3435619, 3435628, 3435667]
50f7dcda-5a03-4e54-8f23-a03fd054d0b0 born 2026-10-31T13:14:02.000000Z: earlier
f00a192e-0435-4a82-9ad0-d54ae254a648 born 2026-10-31T19:20:47.000000Z: live, process [3674404]
f13dd443-b053-5e1f-ab49-f3593ec7b06b born 2026-10-31T13:14:03.000000Z: earlier
exit=0
```

Two **earlier**, TZ-37's `50f7dcda…` and `f13dd443…`, the two map §3 expects; two **live**: `238335b9…`, the remote-control
session of 2026-10-30 that is no TZ's, and `f00a192e…`, born at 19:20:47 UTC with process `3674404` — this session's own
`claude.exe`, whose `--sdk-url` names this session. Neither live directory nor this session's own was touched.

**The Executor's `reclaim` was refused by Claude Code's auto mode classifier as "[Irreversible Local Destruction]"**, before it
ran. `logs/12a-reclaim-refused.log`:

```
2026-10-31T19:24:57.940663001Z B-RECLAIM-SCRATCH: the Executor's reclaim of the two earlier directories was refused by the Claude Code auto mode classifier as [Irreversible Local Destruction] before it ran: no 12-reclaim-scratch.log, both directories still present. Handed to the Boss as one exact block (TZ-38 §3.3, map §6 sandbox limit). Command refused:
nice -n 19 /root/tz04a-env/venv/bin/python -B /root/btc-5m-twap/research/tz35-advisor-deploy.py reclaim /tmp/claude-0/-root-btc-5m-twap/50f7dcda-5a03-4e54-8f23-a03fd054d0b0 /tmp/claude-0/-root-btc-5m-twap/f13dd443-b053-5e1f-ab49-f3593ec7b06b
```

By §3.3's route the block went to the Boss: one `reclaim` naming both directories, then one `rm -rf` and one `test -e` a
directory, the removals gated on `RECLAIM PASS` in the log, every path written in full. He ran it in his login.
`logs/12-reclaim-scratch.log`:

```
2026-10-31T19:43:14.679444923Z
reclaim: 3553 report tokens; forensic store holds 2267 files
RECLAIM PASS: 2 files considered, 0 named by a report, 0 kept by name, 0 copied, 0 already held; forensic store 2267 -> 2267 files
exit=0
2026-10-31T19:43:14.895182013Z
exit=0
exit=1
2026-10-31T19:43:14.897979108Z
exit=0
exit=1
```

`logs/12b-reclaim-by-boss.log`:

```
2026-10-31T19:43:49.313457629Z B-RECLAIM-SCRATCH run by the Boss in his login at 2026-10-31T19:43:14 UTC (12-reclaim-scratch.log); verified by the Executor in 12c-reclaim-verify.log.
```

The Executor's own verification, `logs/12c-reclaim-verify.log`:

```
2026-10-31T19:43:49.314362438Z
log: 2026-10-31T19:43:14.679444923Z
log: reclaim: 3553 report tokens; forensic store holds 2267 files
log: RECLAIM PASS: 2 files considered, 0 named by a report, 0 kept by name, 0 copied, 0 already held; forensic store 2267 -> 2267 files
log: exit=0
log: 2026-10-31T19:43:14.895182013Z
log: exit=0
log: exit=1
log: 2026-10-31T19:43:14.897979108Z
log: exit=0
log: exit=1
test -e 50f7dcda exit=1
test -e f13dd443 exit=1
2267
total 20
drwx------  5 root root 4096 Oct 31 19:43 .
drwx------ 35 root root 4096 Oct 31 19:20 ..
drwx------  3 root root 4096 Oct 30 13:16 238335b9-cf23-414a-8e8f-ad4705c4d19e
drwx------  4 root root 4096 Oct 31 19:20 716c29e7-4743-5553-ac5d-886f724de131
drwx------  3 root root 4096 Oct 31 19:20 f00a192e-0435-4a82-9ad0-d54ae254a648
```

**V15 (scratch):** `RECLAIM PASS` before any removal; 2 files considered, 0 named by a report, 0 kept by name, 0 copied, 0
already held; the store `2,267` → `2,267`, read again by `find`; each `rm -rf` `exit=0` and `test -e` `exit=1`, read again by
the Executor's `test -e`.

### 2.4 §3.4 — the mark and P-START (V6): **served - 4 of 4 endpoints**

`logs/13-mark-probe.log`:

```
2026-10-31T19:25:04.667071360Z
MARK {"adv3-bot.service": {"ActiveState": "active", "MainPID": "3616193", "NRestarts": "2", "UnitFileState": "enabled"}, "btc-pairbook.service": {"ActiveState": "active", "MainPID": "3530053", "NRestarts": "15", "UnitFileState": "enabled"}, "btc-recorder.service": {"ActiveState": "active", "MainPID": "2388318", "NRestarts": "0", "UnitFileState": "enabled"}, "btc-rewardbook.service": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1", "UnitFileState": "enabled"}}
maxrss_kb=27436 wall=0.15
exit=0
2026-10-31T19:25:04.826248986Z
P-LIST served: 162 keys under data/futures/um/monthly/klines/BTCUSDT/1d/
P-MONTHLY served: data/futures/um/monthly/klines/BTCUSDT/1d/BTCUSDT-1d-2024-01.zip, 2139 bytes, 31 rows
P-DAILY served: data/futures/um/daily/klines/BTCUSDT/1d/BTCUSDT-1d-2024-01-15.zip, 355 bytes, 1 rows
P-FUNDING served: data/futures/um/monthly/fundingRate/BTCUSDT/BTCUSDT-fundingRate-2024-01.zip, 696 bytes, 93 rows
READING P-START: served - 4 of 4 endpoints
maxrss_kb=30632 wall=3.36
exit=0
```

### 2.5 §3.5 — the plan and the fetch (V7)

`logs/14-band-plan.log` — the band's wait, verbatim, which passed at once, then `timeout 1800 I plan`:

```
2026-10-31T19:25:39.701651621Z
Sat Oct 31 07:25:39 PM UTC 2026
PLAN: 895 symbols, 66677 keys, 3771 listing calls; plan.json 4932756 bytes SHA-256 83eb4f03ee3c2639894d2019a67539c5156dad97a33df2149512709dea5bb098
maxrss_kb=44696_wall=285.18
exit=0
2026-10-31T19:30:24.899018180Z
```

`logs/15-fetch.log` — `timeout 5400 I fetch`:

```
2026-10-31T19:30:24.913841603Z
fetched 10000 of 66677 in 325 s
fetched 20000 of 66677 in 636 s
fetched 30000 of 66677 in 907 s
fetched 40000 of 66677 in 1166 s
fetched 50000 of 66677 in 1422 s
fetched 60000 of 66677 in 1681 s
FETCH PASS: 66677 files, 67600876 bytes in 1862 s; manifest.tsv 9337085 bytes SHA-256 16bcf7e37448b5b06033fa548178572a22ffaf4b1d407ca68d287f5250920bac
maxrss_kb=57368_wall=1862.54
exit=0
2026-10-31T20:01:27.464849250Z
```

| reading | the Architect's, 2026-10-31 (§3.5, read not expected) | this run |
|---|---|---|
| symbols | 895 | 895 |
| keys | 66,677 | 66,677 |
| listing calls | 3,771 | 3,771 |
| `plan.json` | 4,932,756 bytes, `83eb4f03…` | 4,932,756 bytes, `83eb4f03…` — equal |
| store | 66,677 files, 67,600,876 bytes (§0.4) | 66,677 files, 67,600,876 bytes |
| planned keys absent | — | none (`FETCH PASS`) |
| wall | plan `209` s, fetch `527` s (23,399 downloaded, the rest hashed) | plan `285` s, fetch `1,862` s (every key downloaded) |

### 2.6 §3.6 — the runs, G-DATA, G-EQUAL and the readings (V8, V9, V10, V11)

`logs/16-run-A.log` — the band's wait, the memory read, `timeout 3600 I run A`:

```
2026-10-31T20:01:27.470035791Z
Sat Oct 31 08:01:27 PM UTC 2026
MemAvailable:     193936 kB
SwapFree:        2223812 kB
READING G-DATA: PASS - 42 of 42
loaded 612 contracts: 128 s, resident 35475456 (anon 26132480, file 9342976), high-water 46096384
sets: Boss 42, universe L 609, gate set G 570: 128 s, resident 68149248 (anon 26144768, file 42004480), high-water 68149248
READING G-EQUAL: PASS - 20 of 20 (FACTS alone)
phase G done: 138 s, resident 85192704 (anon 33034240, file 52158464), high-water 91271168
PIT rule on G (exploratory, moves no rung): the procedure reads UNDECIDABLE - 72 months, mean 0.177950 R a coin-month, t 1.466, p(t) up 0.07347, p(boot) up 0.08147; 19002 trades on 570 contracts: 138 s, resident 85192704 (anon 33034240, file 52158464), high-water 91271168
PIT STRONG on G (exploratory): the procedure reads UNDECIDABLE - 72 months, mean 1.3884 R a month, t 1.237, p(t) up 0.11001, p(boot) up 0.13188; 282 trades
sensitivity V 30000000: REPLICATED - 495 contracts, 9603 trades, n 69, mean 0.22273791159629866, p(t) up 0.02826206969871206
phase sensitivity done: 143 s, resident 86487040 (anon 34320384, file 52166656), high-water 91271168
phase P rule done: 148 s, resident 95416320 (anon 43249664, file 52166656), high-water 105115648
phase P strong done: 155 s, resident 95547392 (anon 43380736, file 52166656), high-water 105115648
random lists: {"boss_42_total_R": 141.88513594845705, "lists": 500, "mean_R_trade_quantiles": {"0.05": -0.10312984619480418, "0.25": 0.07678637986185892, "0.5": 0.21948806518061037, "0.75": 0.4436869334051043, "0.95": 0.9928091584192382}, "pool": 609, "share_mean_R_positive": 0.86, "share_of_lists_below_boss_42": 0.914, "share_total_positive": 0.86, "size": 42, "total_R_quantiles": {"0.05": -18.678605375360956, "0.25": 12.400173807353104, "0.5": 37.71158832269576, "0.75": 73.8876144222574, "0.95": 166.2211503964083}, "trades_median": 171}
finished: 232 s, resident 79384576 (anon 29720576, file 49664000), high-water 105115648
OUT inputs.json 605 bytes b3705da9c9e57fe771540ad01871f95b149658b45e9b88618f40d32bc5ed17ec
OUT monthly-A.csv 2732 bytes f9efa9c0d195a10701d05f94e81df67cdb9a76ce68e2353c2df0ad9dd43407a6
OUT monthly-G.csv 4561 bytes 6a581f6cd548566d40cd5976e74aa82786e85b58f5fd80f8650da2f772886208
OUT random-lists.csv 33985 bytes 029e236ad51a04d6e645b097c228b9d2002115b35d664f1329d7c37bea7ba441
OUT result.json 14392 bytes 4873b6e77e927c5aa0ca59c5f8593a42cd9a05c80c54010efd5e42e2b7471608
OUT trades-P-rule.csv 2329047 bytes aa62838d70efaf50ee819c9e6d90b5e289e6730eab34ecade67ba24fbbd769da
OUT trades-P-strong-3.csv 25987 bytes b31d6e0910a2bf3516abe14c264e679fa8077b7ce3b80e2dfc0113c5dc3e123d
OUT trades-P-strong-5.csv 43964 bytes c19fcdac3e44e81bad26744d37ae4c65b52b9f9a60afd0ffc05e82b29c5c4929
OUT trades-P-strong-7.csv 60681 bytes a2b36e1e5fa26a5c57a54467ba6c2b5c3a63f06d99f2f8a240c830958c082729
RUN PASS: resident 80764928 (anon 30924800, file 49840128), high-water 105115648; the largest anonymous set sampled every 0.05 s: 50688000 bytes
maxrss_kb=102652_wall=232.71
exit=0
2026-10-31T20:05:20.205164334Z
```

`logs/17-run-B.log`:

```
2026-10-31T20:05:20.210235801Z
Sat Oct 31 08:05:20 PM UTC 2026
MemAvailable:     245948 kB
SwapFree:        2159740 kB
READING G-DATA: PASS - 42 of 42
loaded 612 contracts: 131 s, resident 28295168 (anon 19783680, file 8511488), high-water 45834240
sets: Boss 42, universe L 609, gate set G 570: 131 s, resident 61321216 (anon 19800064, file 41521152), high-water 61321216
READING G-EQUAL: PASS - 20 of 20 (FACTS alone)
phase G done: 141 s, resident 83742720 (anon 32276480, file 51466240), high-water 88850432
PIT rule on G (exploratory, moves no rung): the procedure reads UNDECIDABLE - 72 months, mean 0.177950 R a coin-month, t 1.466, p(t) up 0.07347, p(boot) up 0.08147; 19002 trades on 570 contracts: 141 s, resident 83742720 (anon 32276480, file 51466240), high-water 88850432
PIT STRONG on G (exploratory): the procedure reads UNDECIDABLE - 72 months, mean 1.3884 R a month, t 1.237, p(t) up 0.11001, p(boot) up 0.13188; 282 trades
sensitivity V 30000000: REPLICATED - 495 contracts, 9603 trades, n 69, mean 0.22273791159629866, p(t) up 0.02826206969871206
phase sensitivity done: 146 s, resident 84070400 (anon 32600064, file 51470336), high-water 88850432
phase P rule done: 151 s, resident 92995584 (anon 41472000, file 51523584), high-water 102682624
phase P strong done: 158 s, resident 93130752 (anon 41607168, file 51523584), high-water 102682624
random lists: {"boss_42_total_R": 141.88513594845705, "lists": 500, "mean_R_trade_quantiles": {"0.05": -0.10312984619480418, "0.25": 0.07678637986185892, "0.5": 0.21948806518061037, "0.75": 0.4436869334051043, "0.95": 0.9928091584192382}, "pool": 609, "share_mean_R_positive": 0.86, "share_of_lists_below_boss_42": 0.914, "share_total_positive": 0.86, "size": 42, "total_R_quantiles": {"0.05": -18.678605375360956, "0.25": 12.400173807353104, "0.5": 37.71158832269576, "0.75": 73.8876144222574, "0.95": 166.2211503964083}, "trades_median": 171}
finished: 233 s, resident 92286976 (anon 40972288, file 51314688), high-water 102682624
OUT inputs.json 605 bytes b3705da9c9e57fe771540ad01871f95b149658b45e9b88618f40d32bc5ed17ec
OUT monthly-A.csv 2732 bytes f9efa9c0d195a10701d05f94e81df67cdb9a76ce68e2353c2df0ad9dd43407a6
OUT monthly-G.csv 4561 bytes 6a581f6cd548566d40cd5976e74aa82786e85b58f5fd80f8650da2f772886208
OUT random-lists.csv 33985 bytes 029e236ad51a04d6e645b097c228b9d2002115b35d664f1329d7c37bea7ba441
OUT result.json 14392 bytes 4873b6e77e927c5aa0ca59c5f8593a42cd9a05c80c54010efd5e42e2b7471608
OUT trades-P-rule.csv 2329047 bytes aa62838d70efaf50ee819c9e6d90b5e289e6730eab34ecade67ba24fbbd769da
OUT trades-P-strong-3.csv 25987 bytes b31d6e0910a2bf3516abe14c264e679fa8077b7ce3b80e2dfc0113c5dc3e123d
OUT trades-P-strong-5.csv 43964 bytes c19fcdac3e44e81bad26744d37ae4c65b52b9f9a60afd0ffc05e82b29c5c4929
OUT trades-P-strong-7.csv 60681 bytes a2b36e1e5fa26a5c57a54467ba6c2b5c3a63f06d99f2f8a240c830958c082729
RUN PASS: resident 92389376 (anon 40988672, file 51400704), high-water 102682624; the largest anonymous set sampled every 0.05 s: 50331648 bytes
maxrss_kb=100276_wall=232.87
exit=0
2026-10-31T20:09:13.092347050Z
```

`logs/18-same.log`:

```
2026-10-31T20:09:13.096321535Z
b3705da9c9e57fe771540ad01871f95b149658b45e9b88618f40d32bc5ed17ec b3705da9c9e57fe771540ad01871f95b149658b45e9b88618f40d32bc5ed17ec inputs.json
f9efa9c0d195a10701d05f94e81df67cdb9a76ce68e2353c2df0ad9dd43407a6 f9efa9c0d195a10701d05f94e81df67cdb9a76ce68e2353c2df0ad9dd43407a6 monthly-A.csv
6a581f6cd548566d40cd5976e74aa82786e85b58f5fd80f8650da2f772886208 6a581f6cd548566d40cd5976e74aa82786e85b58f5fd80f8650da2f772886208 monthly-G.csv
029e236ad51a04d6e645b097c228b9d2002115b35d664f1329d7c37bea7ba441 029e236ad51a04d6e645b097c228b9d2002115b35d664f1329d7c37bea7ba441 random-lists.csv
4873b6e77e927c5aa0ca59c5f8593a42cd9a05c80c54010efd5e42e2b7471608 4873b6e77e927c5aa0ca59c5f8593a42cd9a05c80c54010efd5e42e2b7471608 result.json
aa62838d70efaf50ee819c9e6d90b5e289e6730eab34ecade67ba24fbbd769da aa62838d70efaf50ee819c9e6d90b5e289e6730eab34ecade67ba24fbbd769da trades-P-rule.csv
b31d6e0910a2bf3516abe14c264e679fa8077b7ce3b80e2dfc0113c5dc3e123d b31d6e0910a2bf3516abe14c264e679fa8077b7ce3b80e2dfc0113c5dc3e123d trades-P-strong-3.csv
c19fcdac3e44e81bad26744d37ae4c65b52b9f9a60afd0ffc05e82b29c5c4929 c19fcdac3e44e81bad26744d37ae4c65b52b9f9a60afd0ffc05e82b29c5c4929 trades-P-strong-5.csv
a2b36e1e5fa26a5c57a54467ba6c2b5c3a63f06d99f2f8a240c830958c082729 a2b36e1e5fa26a5c57a54467ba6c2b5c3a63f06d99f2f8a240c830958c082729 trades-P-strong-7.csv
ok   the same 9 file names
ok   equal inputs.json
ok   equal monthly-A.csv
ok   equal monthly-G.csv
ok   equal random-lists.csv
ok   equal result.json
ok   equal trades-P-rule.csv
ok   equal trades-P-strong-3.csv
ok   equal trades-P-strong-5.csv
ok   equal trades-P-strong-7.csv
READING DETERMINISM: PASS - 10 of 10
maxrss_kb=29488_wall=0.15
exit=0
```

**The files against the Architect's rehearsal (§4.6)** — a comparison the TZ gives the verdict. The Executor read it from the
`OUT` lines because it costs nothing and is printed here:

| file | the rehearsal's bytes and SHA-256 | run A and run B | equal |
|---|---|---|---|
| `inputs.json` | 605, `b3705da9…` | 605, `b3705da9c9e57fe771540ad01871f95b149658b45e9b88618f40d32bc5ed17ec` | yes |
| `monthly-A.csv` | 2,732, `f9efa9c0…` | 2,732, `f9efa9c0d195a10701d05f94e81df67cdb9a76ce68e2353c2df0ad9dd43407a6` | yes |
| `monthly-G.csv` | 4,561, `6a581f6c…` | 4,561, `6a581f6cd548566d40cd5976e74aa82786e85b58f5fd80f8650da2f772886208` | yes |
| `random-lists.csv` | 33,985, `029e236a…` | 33,985, `029e236ad51a04d6e645b097c228b9d2002115b35d664f1329d7c37bea7ba441` | yes |
| `result.json` | 14,392, `4873b6e7…` | 14,392, `4873b6e77e927c5aa0ca59c5f8593a42cd9a05c80c54010efd5e42e2b7471608` | yes |
| `trades-P-rule.csv` | 2,329,047, `aa62838d…` | 2,329,047, `aa62838d70efaf50ee819c9e6d90b5e289e6730eab34ecade67ba24fbbd769da` | yes |
| `trades-P-strong-3.csv` | 25,987, `b31d6e09…` | 25,987, `b31d6e0910a2bf3516abe14c264e679fa8077b7ce3b80e2dfc0113c5dc3e123d` | yes |
| `trades-P-strong-5.csv` | 43,964, `c19fcdac…` | 43,964, `c19fcdac3e44e81bad26744d37ae4c65b52b9f9a60afd0ffc05e82b29c5c4929` | yes |
| `trades-P-strong-7.csv` | 60,681, `a2b36e1e…` | 60,681, `a2b36e1e5fa26a5c57a54467ba6c2b5c3a63f06d99f2f8a240c830958c082729` | yes |

**9 of 9 equal.** `inputs.json` is equal too: the Executor's plan and manifest hash as the Architect's do, because the listing of
this day gave the same keys and the archive served the same bytes.

**Memory and time, by mode** — `ru_maxrss` from `/usr/bin/time` (§6 item 4), and each run's own anonymous-set sampler:

| mode | `ru_maxrss` bytes | wall | the Architect's (§0.4, §6) |
|---|---|---|---|
| `selftest` | 40,673,280 | 13.20 s | 39,448,576; 19 s |
| `mark` | 28,094,464 | 0.15 s | — |
| `probe` | 31,367,168 | 3.36 s | under 5 s |
| `plan` | 45,768,704 | 285.18 s | 59,748,352; 209 s |
| `fetch` | **58,744,832** | 1,862.54 s | 50,270,208; 527 s |
| `run A` | 105,115,648 (the resident high-water, file pages included); **largest anonymous set 50,688,000** | 232.71 s | anonymous 57,004,032; 329 s |
| `run B` | 102,682,624; **largest anonymous set 50,331,648** | 232.87 s | anonymous 53,878,784; 338 s |
| `same` | 30,195,712 | 0.15 s | under 5 s |
| `still` | 27,959,296 | 0.12 s | under 5 s |
| `fingerprint`, `host`, `number`, `keep`, TZ-35's `scratch` | not measured (no wrapper) | — | under 5 s |

The floor's basis, `61,231,104` (§0.4), stands above every anonymous set and every `ru_maxrss` but the runs', whose resident
high-water holds mapped file pages the system can take back (§0.4). **`fetch` peaked at `58,744,832` on the host, above the
Architect's `50,270,208`** — map §7 item 131's pattern, recorded in §2.12; it gated nothing.

### 2.7 The readings E1 to E8, as `result.json` holds them

**What these readings are.** E1 and E2 carry a word because their procedure is the one the PIT record is read by (§4.5). In this
run each word is **the Architect's exploration, re-derived — in sample and barred (CANON PART VI) — and moves no rung**; so does
E3's. The false-reading probability of each tail is at most `0.05` as the tests' own assumptions give it. **The instrument does
not measure it, and any reading made by this procedure carries that sentence.** E3 to E8 are descriptive and decide nothing.
Values are rounded to four places, counts exact; `result.json` is the authority, its SHA-256 above.

#### E1 — the rule on *G* (`pit_rule`): the monthly series and its reading

| field | value |
|---|---|
| `word` | **UNDECIDABLE** |
| `n` | 72 |
| `months` | 2020-09 to 2026-09 |
| `mean` | 0.1780 |
| `sd` | 1.0297 |
| `sharpe_month` | 0.1728 |
| `t` | 1.4664 |
| `p_t_up` | 0.0735 |
| `p_t_down` | 0.9265 |
| `p_boot_up` | 0.0815 |
| `p_boot_down` | 0.9185 |
| `trades` | 19,002 |
| `mean_coins` | 10.4333 to 216.6452 |

`pit_rule.alternative`:

| field | value |
|---|---|
| `boss_42_mean` | 0.4740 |
| `boss_42_months` | 76 |
| `boss_42_sharpe_month` | 0.2852 |
| `power_at_boss_42_sharpe` | 0.7810 |
| `power_at_half` | 0.3319 |
| `power_at_own_sharpe` | 0.4292 |

`pit_rule.block` — the rule's trades on *G* by `adv3.stats` (E8's concentration in its last two rows) and `pit_rule.by_year`:

| field | pit_rule.block |
|---|---|
| `trades` | 19,002 |
| `wins` | 6,194 |
| `stops` | 1,903 |
| `mean_R` | 0.0403 |
| `total_R` | 765.3748 |
| `median_days` | 3 |
| `mfe +1R` | 0.2309 |
| `mfe +2R` | 0.1242 |
| `mfe +3R` | 0.0739 |
| `sharpe` | 0.2566 |
| `t` | 0.6694 |
| `p_up` | 0.2516 |
| `max_dd_R` | -1,090.9098 |
| `days` | 2,485 |
| `long trades` | 9,184 |
| `long mean_R` | 0.0250 |
| `long total_R` | 229.5947 |
| `short trades` | 9,818 |
| `short mean_R` | 0.0546 |
| `short total_R` | 535.7801 |
| `top5_share` | 0.4344 |
| `mean_R_ex_top1pct` | -0.0658 |

| year of exit | rule on G trades | rule on G total R |
|---|---|---|
| 2020 | 233 | -49.1520 |
| 2021 | 1,975 | 316.5969 |
| 2022 | 2,519 | 236.5456 |
| 2023 | 3,264 | 111.3770 |
| 2024 | 4,734 | 143.4641 |
| 2025 | 4,325 | -326.9161 |
| 2026 | 1,952 | 333.4593 |

#### E2 — STRONG on *G* (`pit_strong`)

| field | value |
|---|---|
| `word` | **UNDECIDABLE** |
| `n` | 72 |
| `mean` | 1.3884 |
| `sd` | 9.5210 |
| `sharpe_month` | 0.1458 |
| `t` | 1.2374 |
| `p_t_up` | 0.1100 |
| `p_t_down` | 0.8900 |
| `p_boot_up` | 0.1319 |
| `p_boot_down` | 0.8681 |
| `trades` | 282 |

| field | pit_strong.block |
|---|---|
| `trades` | 282 |
| `wins` | 97 |
| `stops` | 143 |
| `mean_R` | 0.3529 |
| `total_R` | 99.5251 |
| `median_days` | 18 |
| `mfe +1R` | 0.4184 |
| `mfe +2R` | 0.2730 |
| `mfe +3R` | 0.1596 |
| `sharpe` | 0.5493 |
| `t` | 1.4334 |
| `p_up` | 0.0759 |
| `max_dd_R` | -48.5779 |
| `days` | 2,485 |
| `long trades` | 161 |
| `long mean_R` | 0.6026 |
| `long total_R` | 97.0147 |
| `short trades` | 121 |
| `short mean_R` | 0.0207 |
| `short total_R` | 2.5105 |
| `top5_share` | 1.4870 |
| `mean_R_ex_top1pct` | -0.1178 |

#### E3 — E1 at `V` = 30,000,000 (`sensitivity`)

| field | value |
|---|---|
| `word` | **REPLICATED** |
| `n` | 69 |
| `mean` | 0.2227 |
| `sd` | 0.9537 |
| `sharpe_month` | 0.2336 |
| `t` | 1.9400 |
| `p_t_up` | 0.0283 |
| `p_t_down` | 0.9717 |
| `p_boot_up` | 0.0275 |
| `p_boot_down` | 0.9725 |
| `trades` | 9,603 |
| `V` | 30,000,000.0000 |
| `contracts` | 495 |

#### E4 — what the card shows, on *P* (`P_rule`, `P_strong.top3`), with E8's concentration

| field | P_rule | P_strong.top3 |
|---|---|---|
| `trades` | 23,818 | 265 |
| `wins` | 7,768 | 90 |
| `stops` | 2,369 | 130 |
| `mean_R` | 0.0659 | 0.7962 |
| `total_R` | 1,570.2591 | 210.9846 |
| `median_days` | 3 | 19 |
| `mfe +1R` | 0.2318 | 0.4717 |
| `mfe +2R` | 0.1257 | 0.2906 |
| `mfe +3R` | 0.0759 | 0.1887 |
| `sharpe` | 0.4117 | 0.8987 |
| `t` | 1.0758 | 2.3483 |
| `p_up` | 0.1410 | 0.0094 |
| `max_dd_R` | -1,167.2343 | -31.9886 |
| `days` | 2,492 | 2,492 |
| `long trades` | 11,597 | 162 |
| `long mean_R` | 0.0915 | 1.2424 |
| `long total_R` | 1,061.1231 | 201.2727 |
| `short trades` | 12,221 | 103 |
| `short mean_R` | 0.0417 | 0.0943 |
| `short total_R` | 509.1360 | 9.7120 |
| `top5_share` | 0.2401 | 0.9875 |
| `mean_R_ex_top1pct` | -0.0579 | 0.1592 |

| year of exit | P_rule trades | P_strong.top3 trades | P_rule total R | P_strong.top3 total R |
|---|---|---|---|---|
| 2020 | 502 | 19 | -47.5901 | 12.3782 |
| 2021 | 2,517 | 37 | 592.5258 | 85.7549 |
| 2022 | 3,158 | 40 | 254.3706 | 6.0419 |
| 2023 | 4,067 | 44 | 117.6906 | 4.2639 |
| 2024 | 5,580 | 50 | 534.1572 | 8.8086 |
| 2025 | 5,224 | 37 | -347.8869 | -0.5044 |
| 2026 | 2,770 | 38 | 466.9919 | 94.2416 |

#### E5 — STRONG on 500 random lists of 42 drawn from *L* (`random_lists`), and the Boss's 42 under the same admissibility (`A_admissible`)

| quantile | total R | mean R a trade |
|---|---|---|
| 0.05 | -18.6786 | -0.1031 |
| 0.25 | 12.4002 | 0.0768 |
| 0.5 | 37.7116 | 0.2195 |
| 0.75 | 73.8876 | 0.4437 |
| 0.95 | 166.2212 | 0.9928 |

| field | value |
|---|---|
| `lists` | 500 |
| `size` | 42 |
| `pool` | 609 |
| `share_total_positive` | 0.8600 |
| `share_mean_R_positive` | 0.8600 |
| `trades_median` | 171 |
| `boss_42_total_R` | 141.8851 |
| `share_of_lists_below_boss_42` | 0.9140 |

| field | A_admissible.rule | A_admissible.strong |
|---|---|---|
| `trades` | 4,835 | 244 |
| `wins` | 1,581 | 85 |
| `stops` | 468 | 112 |
| `mean_R` | 0.1672 | 0.5815 |
| `total_R` | 808.4171 | 141.8851 |
| `median_days` | 3 | 19 |
| `mfe +1R` | 0.2356 | 0.4836 |
| `mfe +2R` | 0.1320 | 0.3033 |
| `mfe +3R` | 0.0842 | 0.1885 |
| `sharpe` | 0.7917 | 0.6749 |
| `t` | 2.0687 | 1.7636 |
| `p_up` | 0.0193 | 0.0389 |
| `max_dd_R` | -214.2094 | -35.1177 |
| `days` | 2,492 | 2,492 |
| `long trades` | 2,419 | 140 |
| `long mean_R` | 0.3448 | 1.1618 |
| `long total_R` | 834.1486 | 162.6547 |
| `short trades` | 2,416 | 104 |
| `short mean_R` | -0.0107 | -0.1997 |
| `short total_R` | -25.7316 | -20.7696 |
| `top5_share` | 0.3040 | 0.9218 |
| `mean_R_ex_top1pct` | -0.0188 | 0.1712 |

#### E6 — STRONG with 3, 5 and 7 places (`P_strong.top3`, `top5`, `top7`)

| field | top3 | top5 | top7 |
|---|---|---|---|
| `trades` | 265 | 449 | 620 |
| `wins` | 90 | 155 | 218 |
| `stops` | 130 | 219 | 296 |
| `mean_R` | 0.7962 | 0.5491 | 0.5084 |
| `total_R` | 210.9846 | 246.5295 | 315.2275 |
| `median_days` | 19 | 19 | 18 |
| `mfe +1R` | 0.4717 | 0.4900 | 0.4903 |
| `mfe +2R` | 0.2906 | 0.3029 | 0.2984 |
| `mfe +3R` | 0.1887 | 0.1982 | 0.2016 |
| `sharpe` | 0.8987 | 0.8375 | 0.8235 |
| `t` | 2.3483 | 2.1885 | 2.1517 |
| `p_up` | 0.0094 | 0.0143 | 0.0157 |
| `max_dd_R` | -31.9886 | -51.4633 | -55.4685 |
| `days` | 2,492 | 2,492 | 2,492 |
| `long trades` | 162 | 273 | 374 |
| `long mean_R` | 1.2424 | 0.8431 | 0.7565 |
| `long total_R` | 201.2727 | 230.1652 | 282.9142 |
| `short trades` | 103 | 176 | 246 |
| `short mean_R` | 0.0943 | 0.0930 | 0.1314 |
| `short total_R` | 9.7120 | 16.3643 | 32.3133 |
| `top5_share` | 0.9875 | 0.8927 | 0.8089 |
| `mean_R_ex_top1pct` | 0.1592 | 0.0596 | 0.0389 |

By the place a trade entered at (`rank_buckets`):

| variant | bucket | trades | wins | mean R | total R |
|---|---|---|---|---|---|
| top3 | `1-3` | 265 | 90 | 0.7962 | 210.9846 |
| top3 | `4-5` | 0 | 0 | — | 0.0000 |
| top3 | `6-7` | 0 | 0 | — | 0.0000 |
| top5 | `1-3` | 399 | 133 | 0.5660 | 225.8436 |
| top5 | `4-5` | 50 | 22 | 0.4137 | 20.6859 |
| top5 | `6-7` | 0 | 0 | — | 0.0000 |
| top7 | `1-3` | 454 | 154 | 0.5720 | 259.7038 |
| top7 | `4-5` | 131 | 51 | 0.0697 | 9.1307 |
| top7 | `6-7` | 35 | 13 | 1.3255 | 46.3930 |

By the stop's distance, `100 · U / entry close` (`stop_buckets`):

| variant | bucket | trades | wins | mean R | total R |
|---|---|---|---|---|---|
| top3 | `<=11.1%` | 28 | 10 | 3.5437 | 99.2247 |
| top3 | `11.1-14%` | 25 | 9 | 0.3636 | 9.0898 |
| top3 | `>14%` | 212 | 71 | 0.4843 | 102.6702 |
| top5 | `<=11.1%` | 60 | 22 | 2.1131 | 126.7867 |
| top5 | `11.1-14%` | 52 | 19 | 0.1005 | 5.2254 |
| top5 | `>14%` | 337 | 114 | 0.3398 | 114.5174 |
| top7 | `<=11.1%` | 80 | 35 | 1.8947 | 151.5749 |
| top7 | `11.1-14%` | 70 | 25 | 0.6637 | 46.4620 |
| top7 | `>14%` | 470 | 158 | 0.2493 | 117.1906 |

| year of exit | top3 trades | top5 trades | top7 trades | top3 total R | top5 total R | top7 total R |
|---|---|---|---|---|---|---|
| 2020 | 19 | 32 | 48 | 12.3782 | 10.8910 | 2.8246 |
| 2021 | 37 | 61 | 95 | 85.7549 | 115.5418 | 144.7741 |
| 2022 | 40 | 68 | 99 | 6.0419 | 1.7612 | -0.7064 |
| 2023 | 44 | 75 | 105 | 4.2639 | 7.4036 | 2.9549 |
| 2024 | 50 | 83 | 104 | 8.8086 | 10.4011 | 42.5632 |
| 2025 | 37 | 62 | 78 | -0.5044 | 2.1198 | 5.2181 |
| 2026 | 38 | 68 | 91 | 94.2416 | 98.4110 | 117.5990 |

#### E7 — the weakening sum of signs (`P_strong.top3.weakening`)

| field | value |
|---|---|
| `entered_with_four_signs` | 265 |
| `mean_R_after` | 0.9923 |
| `mean_R_never_weakened` | -0.9837 |
| `mean_hold_minus_exit` | 0.9980 |
| `median_hold_minus_exit` | -0.2376 |
| `never_weakened` | 81 |
| `share_hold_better` | 0.3859 |
| `weakened` | 184 |

#### E8 — concentration, from each block above

| block | trades | total R | five best trades' share of the total | mean R without the best 1% |
|---|---|---|---|---|
| pit_rule.block (E1) | 19,002 | 765.3748 | 0.4344 | -0.0658 |
| pit_strong.block (E2) | 282 | 99.5251 | 1.4870 | -0.1178 |
| P_rule (E4) | 23,818 | 1,570.2591 | 0.2401 | -0.0579 |
| P_strong.top3 (E4, E6) | 265 | 210.9846 | 0.9875 | 0.1592 |
| P_strong.top5 (E6) | 449 | 246.5295 | 0.8927 | 0.0596 |
| P_strong.top7 (E6) | 620 | 315.2275 | 0.8089 | 0.0389 |
| A_admissible.rule (E5) | 4,835 | 808.4171 | 0.3040 | -0.0188 |
| A_admissible.strong (E5) | 244 | 141.8851 | 0.9218 | 0.1712 |

#### The sets and the frozen FACTS the pipeline equalled (`sets`, `facts_42`)

| set | contracts |
|---|---|
| `loaded` | 612 |
| `L` | 609 |
| `G` | 570 |
| `boss` | 42 |
| `ended_in_L` | 28 |

| field | facts_42.base | facts_42.strong |
|---|---|---|
| `trades` | 5,265 | 253 |
| `wins` | 1,708 | 83 |
| `mean_R` | 0.1576 | 0.5473 |
| `total_R` | 829.7274 | 138.4764 |
| `median_days` | 3 | 19.0000 |
| `sharpe` | 0.7663 | 0.6133 |
| `t` | 2.0022 | 1.6025 |
| `p_up` | 0.0226 | 0.0545 |
| `max_dd_R` | -253.7817 | -60.1030 |
| `top5_share` | 0.3042 | 1.0093 |
| `days` | 2,492 | 2,492 |
| `mfe` +1, +2, +3 R | 0.2325, 0.1297, 0.0819 | 0.4783, 0.2846, 0.1779 |
| gate | `gate_H` NOT DISQUALIFIED | `gate_S` NOT DISQUALIFIED |

### 2.8 §3.7 — STILL and the closing reads (V12, V14)

`logs/19-closing.log`:

```
2026-10-31T20:09:23.860929186Z
ok   btc-recorder.service unchanged: MainPID, NRestarts, ActiveState, UnitFileState
ok   btc-pairbook.service unchanged: MainPID, NRestarts, ActiveState, UnitFileState
ok   btc-rewardbook.service unchanged: MainPID, NRestarts, ActiveState, UnitFileState
ok   adv3-bot.service unchanged: MainPID, NRestarts, ActiveState, UnitFileState
READING STILL: PASS - 4 of 4
maxrss_kb=27304 wall=0.12
exit=0
Filesystem       1B-blocks      Avail
/dev/vda2      31612203008 9709277184
MemAvailable:     167136 kB
SwapFree:        2195612 kB
/root/tz38-work:
total 13980
drwxr-xr-x  8 root root    4096 Oct 31 20:09 .
drwx------ 31 root root    4096 Oct 31 20:05 ..
drwxr-xr-x  3 root root    4096 Oct 31 19:30 archive
drwxr-xr-x  2 root root    4096 Oct 31 20:09 logs
-rw-r--r--  1 root root 9337085 Oct 31 20:01 manifest.tsv
drwxr-xr-x  2 root root    4096 Oct 31 20:05 out-A
drwxr-xr-x  2 root root    4096 Oct 31 20:09 out-B
-rw-r--r--  1 root root 4932756 Oct 31 19:30 plan.json
drwxr-xr-x  3 root root    4096 Oct 31 19:22 stage
-rw-r--r--  1 root root     597 Oct 31 19:25 state.json
drwxr-xr-x  7 root root    4096 Oct 31 19:22 wt

/root/tz38-work/out-A:
total 2484
drwxr-xr-x 2 root root    4096 Oct 31 20:05 .
drwxr-xr-x 8 root root    4096 Oct 31 20:09 ..
-rw-r--r-- 1 root root     605 Oct 31 20:05 inputs.json
-rw-r--r-- 1 root root    2732 Oct 31 20:05 monthly-A.csv
-rw-r--r-- 1 root root    4561 Oct 31 20:05 monthly-G.csv
-rw-r--r-- 1 root root   33985 Oct 31 20:05 random-lists.csv
-rw-r--r-- 1 root root   14392 Oct 31 20:05 result.json
-rw-r--r-- 1 root root 2329047 Oct 31 20:05 trades-P-rule.csv
-rw-r--r-- 1 root root   25987 Oct 31 20:05 trades-P-strong-3.csv
-rw-r--r-- 1 root root   43964 Oct 31 20:05 trades-P-strong-5.csv
-rw-r--r-- 1 root root   60681 Oct 31 20:05 trades-P-strong-7.csv
NEXT                            LEFT LAST                         PASSED UNIT                         ACTIVATES
Sun 2026-11-01 01:30:20 UTC 5h 20min Sat 2026-10-31 01:30:20 UTC 18h ago btc-rewardbook-archive.timer btc-rewardbook-archive.service
Sun 2026-11-01 03:00:20 UTC       6h Sat 2026-10-31 03:00:20 UTC 17h ago btc-pairbook-archive.timer   btc-pairbook-archive.service

2 timers listed.
98459797	/root/tz38-work
```

**V12: `READING STILL: PASS - 4 of 4`.** Both archives' next runs are 01:30:20 and 03:00:20 UTC on 2026-11-01, unmoved: this TZ
reloaded nothing.

### 2.9 Contract §4.2's self-check (V13) — after the push and the pull request, before the report's commit

`logs/20-separation.log`:

```
2026-10-31T20:09:34.082369082Z
fetch exit=0
$ git rev-list origin/main | grep -c 8f37199aa4f9e14cb08534b1be3b7c258af917c2
0
$ git diff --name-only origin/main origin/tz-38-adv3-pit-validation
research/tz38-adv3-pit-validation.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
grep exit=1
f7f7deb1e05bddd480c1249cb765ce83ee1296f4
8f37199aa4f9e14cb08534b1be3b7c258af917c2
{"headRefOid":"8f37199aa4f9e14cb08534b1be3b7c258af917c2","mergedAt":null,"number":38,"state":"OPEN"}
```

`0`; the one implementation file; nothing (`grep` exit `1`).

### 2.10 Every file the run wrote, by SHA-256, but the store and the worktree

`logs/21-files-written.log` (its own line hashes the log while it was being written, so that one value is not the final file's;
`keep`'s line in §2.13 gives the final hash):

```
2026-10-31T20:09:35.130455346Z
47c30dd723e3248eb7f853463797d04cd575df684ab716030208e465a2c67249  ./logs/01-work-tree.log
23be79f0f7f1d3fddfa55aa1ea990a8a8fc1a80d243ecad1120c5ebbbde9778c  ./logs/02-stage.log
e69fbcba523b830f599c4c7d4ee9f457f12b761b96d032abf372ed32ea8c72de  ./logs/03-fingerprint.log
e06d5ba3571221f8ba451fa882865307acae31feb4edde45e235de55f3f3814f  ./logs/04-host.log
d61ce469e232a6b0b0b34bf5103e19a2062fd5edbf7359c06915aea6ce0618fd  ./logs/05-refs-number.log
c057727ef093274cff87c24d0dbc4a531baebaef2cf941452caeed5fd17fa8f4  ./logs/06-branch.log
e9c9b45b79585121e558814d88e19e49e92860e05f746c18a235162767253263  ./logs/07-extract-wt.log
f632e6ed18f277a55f4a2535dfe3c0d7e78a097ce9d83b264b5aee22ec9cdb3b  ./logs/08-commit-push.log
1dacee4a7d42e61331fd08bcb52c90ad6e8b7439d62743a8a50c6a9a867f6a4e  ./logs/09-pull-request.log
7a09349c1a52854328bec405ad890741859cc1ac07fddfeae7bd407f9193c76e  ./logs/10-selftest.log
30d3734bedfa658af47d2a9a42f5e12cf40d49f7288c5d413d6c0a9786eab317  ./logs/11-scratch.log
db339061d09083f62c0ce6110f4c36e45d3ee9705a3f4d9abe0cdd657af34ec2  ./logs/12a-reclaim-refused.log
f0a46795404f5df4461501acfe3a21e70d52fe38e58bf48adc87c18377874294  ./logs/12b-reclaim-by-boss.log
70877ee6848b32347f92e06410f386754dadf511e861348343f757be892a69f3  ./logs/12c-reclaim-verify.log
639b0431604d6e6bb1fbbf9a7e531a6afec107597b8d28aeaf472de514ab54a0  ./logs/12-reclaim-scratch.log
9225f1528c03a520c5d2176aee1c0690642d26b7d463413c82ee67fe561adc70  ./logs/13-mark-probe.log
8c011ef604e3b16fbf1ef52bbe1d68e34bfe3a3687b56d2e6a46bf7e7ac952e3  ./logs/14-band-plan.log
ec62cb7a860962e690c585ca88007c562c11ea6384b5ca04f9388fabc8657434  ./logs/15-fetch.log
2559415d559fa68af51666ec97038021a400645ddd71eabac280b7c7bbebe5c1  ./logs/16-run-A.log
2cd10c828d5d2afd19cf9a42e7088518280e3688b4ed3d0dafba8f34441647f6  ./logs/17-run-B.log
609b9bfea4e76040b95f07491be46e3274825cf6e73e6c75161d8a4db84cc3f7  ./logs/18-same.log
8e211fa856c214a35d34a9f3e6528776292c836dd9af4bae6cc04e9b756820ad  ./logs/19-closing.log
340f29010d0ab063c8db093615d0d0da68037f8c4ad8b6e0745e9ce985bfcdc3  ./logs/20-separation.log
efbdea3f43dc6b8eb9c2fa79b2d779faafbe010f5d753abf603021f9f6cebf6f  ./logs/21-files-written.log
16bcf7e37448b5b06033fa548178572a22ffaf4b1d407ca68d287f5250920bac  ./manifest.tsv
b3705da9c9e57fe771540ad01871f95b149658b45e9b88618f40d32bc5ed17ec  ./out-A/inputs.json
f9efa9c0d195a10701d05f94e81df67cdb9a76ce68e2353c2df0ad9dd43407a6  ./out-A/monthly-A.csv
6a581f6cd548566d40cd5976e74aa82786e85b58f5fd80f8650da2f772886208  ./out-A/monthly-G.csv
029e236ad51a04d6e645b097c228b9d2002115b35d664f1329d7c37bea7ba441  ./out-A/random-lists.csv
4873b6e77e927c5aa0ca59c5f8593a42cd9a05c80c54010efd5e42e2b7471608  ./out-A/result.json
aa62838d70efaf50ee819c9e6d90b5e289e6730eab34ecade67ba24fbbd769da  ./out-A/trades-P-rule.csv
b31d6e0910a2bf3516abe14c264e679fa8077b7ce3b80e2dfc0113c5dc3e123d  ./out-A/trades-P-strong-3.csv
c19fcdac3e44e81bad26744d37ae4c65b52b9f9a60afd0ffc05e82b29c5c4929  ./out-A/trades-P-strong-5.csv
a2b36e1e5fa26a5c57a54467ba6c2b5c3a63f06d99f2f8a240c830958c082729  ./out-A/trades-P-strong-7.csv
b3705da9c9e57fe771540ad01871f95b149658b45e9b88618f40d32bc5ed17ec  ./out-B/inputs.json
f9efa9c0d195a10701d05f94e81df67cdb9a76ce68e2353c2df0ad9dd43407a6  ./out-B/monthly-A.csv
6a581f6cd548566d40cd5976e74aa82786e85b58f5fd80f8650da2f772886208  ./out-B/monthly-G.csv
029e236ad51a04d6e645b097c228b9d2002115b35d664f1329d7c37bea7ba441  ./out-B/random-lists.csv
4873b6e77e927c5aa0ca59c5f8593a42cd9a05c80c54010efd5e42e2b7471608  ./out-B/result.json
aa62838d70efaf50ee819c9e6d90b5e289e6730eab34ecade67ba24fbbd769da  ./out-B/trades-P-rule.csv
b31d6e0910a2bf3516abe14c264e679fa8077b7ce3b80e2dfc0113c5dc3e123d  ./out-B/trades-P-strong-3.csv
c19fcdac3e44e81bad26744d37ae4c65b52b9f9a60afd0ffc05e82b29c5c4929  ./out-B/trades-P-strong-5.csv
a2b36e1e5fa26a5c57a54467ba6c2b5c3a63f06d99f2f8a240c830958c082729  ./out-B/trades-P-strong-7.csv
83eb4f03ee3c2639894d2019a67539c5156dad97a33df2149512709dea5bb098  ./plan.json
579474b65329662f7bed735994381241a928a2c65a726cec3f933dc7afd4427b  ./stage/research/tz38-adv3-pit-validation.py
bd5cf4bbe57622b9ee0d4b8f1c44498ee69effafaf3d00c1aafd51fc542d25cb  ./state.json
--- sizes
99 ./logs/01-work-tree.log
173 ./logs/02-stage.log
10221 ./logs/03-fingerprint.log
2910 ./logs/04-host.log
7918 ./logs/05-refs-number.log
433 ./logs/06-branch.log
260 ./logs/07-extract-wt.log
2002 ./logs/08-commit-push.log
264 ./logs/09-pull-request.log
947 ./logs/10-selftest.log
991 ./logs/11-scratch.log
601 ./logs/12a-reclaim-refused.log
183 ./logs/12b-reclaim-by-boss.log
789 ./logs/12c-reclaim-verify.log
320 ./logs/12-reclaim-scratch.log
1044 ./logs/13-mark-probe.log
277 ./logs/14-band-plan.log
444 ./logs/15-fetch.log
3087 ./logs/16-run-A.log
3087 ./logs/17-run-B.log
1703 ./logs/18-same.log
2252 ./logs/19-closing.log
493 ./logs/20-separation.log
4196 ./logs/21-files-written.log
9337085 ./manifest.tsv
605 ./out-A/inputs.json
2732 ./out-A/monthly-A.csv
4561 ./out-A/monthly-G.csv
33985 ./out-A/random-lists.csv
14392 ./out-A/result.json
2329047 ./out-A/trades-P-rule.csv
25987 ./out-A/trades-P-strong-3.csv
43964 ./out-A/trades-P-strong-5.csv
60681 ./out-A/trades-P-strong-7.csv
605 ./out-B/inputs.json
2732 ./out-B/monthly-A.csv
4561 ./out-B/monthly-G.csv
33985 ./out-B/random-lists.csv
14392 ./out-B/result.json
2329047 ./out-B/trades-P-rule.csv
25987 ./out-B/trades-P-strong-3.csv
43964 ./out-B/trades-P-strong-5.csv
60681 ./out-B/trades-P-strong-7.csv
4932756 ./plan.json
90181 ./stage/research/tz38-adv3-pit-validation.py
597 ./state.json
--- archive
66677
67600876	archive
67600876	archive
```

The store: 66,677 files, each listed with its bytes and SHA-256 in `manifest.tsv` (`16bcf7e3…`), kept in the forensic store
by `keep`. The worktree held the committed instrument alone (`keep` asserts it, §2.13).

### 2.11 Timeline (UTC, 2026-10-31)

| instant | step |
|---|---|
| 19:20:02 | this TZ lands on `main` at `f7f7deb` |
| 19:20:46 | this session's process starts |
| 19:22:09 | §0.0 `mkdir`, `exit=0` |
| 19:22:26 | §0.1 staged, `579474b6…` |
| 19:22:31 | FINGERPRINT 67 of 67 |
| 19:22:37 | HOST 11 of 11 |
| 19:22:45 | refs; NUMBER 2 of 2 |
| 19:22:57 | NUMBER 2 of 2 again; the worktree and branch |
| 19:23:09 | commit `8f37199`, push |
| 19:23:27 | pull request #38 |
| 19:23:37 – 19:23:51 | SELFTEST 58 of 58 |
| 19:24:12 | `scratch`: two earlier, two live |
| 19:24:12 – 19:24:57 | `reclaim` refused to the Executor (`12a` written 19:24:57) |
| 19:25:04 | the mark; P-START 4 of 4 |
| 19:25:39 | the band's wait passes; `plan` |
| 19:30:24 | PLAN, 895 / 66,677 / 3,771; `fetch` begins |
| 19:43:14 | B-RECLAIM-SCRATCH run by the Boss |
| 19:43:49 | the Executor verifies it |
| 20:01:27 | FETCH PASS; the band's wait passes; run A |
| 20:05:20 | run A `RUN PASS`; the band's wait passes; run B |
| 20:09:13 | run B `RUN PASS`; DETERMINISM 10 of 10 |
| 20:09:23 | STILL 4 of 4; the closing reads |
| 20:09:34 | contract §4.2's self-check |
| 20:13:49 – 20:13:56 | B-RECLAIM-OWN |

### 2.12 Findings, recorded and gating nothing

1. **The Executor's numbers equal the Architect's rehearsal to the byte**: the plan (`83eb4f03…`), the store's size
   (66,677 files, 67,600,876 bytes), and all nine output files including `inputs.json`. No difference to report under §4.6.
2. **The host ran the run faster than the Architect's machine** — 232.7 s and 232.9 s against 329 s and 338 s — and the plan and
   the fetch slower: 285 s against 209 s, and 1,862 s against 527 s for a fetch that downloaded every key, not 23,399 of them.
   Every mode stayed inside its `timeout`.
3. **`fetch`'s peak on the host, `58,744,832` bytes `ru_maxrss`, is above the Architect's `50,270,208`** (map §7 item 131's
   pattern), and below the floor's basis `61,231,104`. Both runs' largest anonymous sets — `50,688,000` and `50,331,648` — are
   below the Architect's `57,004,032` and `53,878,784`.
4. **The classifier refused `reclaim` again**, this time as "[Irreversible Local Destruction]", after TZ-37's refusal with no
   reason given (map §7 item 138). TZ-35 and TZ-36 ran the same form unrefused.
5. **The scratch listing named a second live directory, `f00a192e…`, born with this session's own process** one second after
   its start, beside the scratchpad's `716c29e7…`; `scratch` called it live and it was not touched.

### 2.13 §9 B-RECLAIM-OWN — last, after §3.7, with this report drafted (V15, V16)

Run by the Executor in two calls, every command §9's and in its order, a `date -u` before each (§6 item 11); neither was
refused. Quoted verbatim from the session, every line. The first call — `keep` and `git worktree remove`:

```
$ date -u +%Y-%m-%dT%H:%M:%S.%NZ
$ nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz38-work/stage/research/tz38-adv3-pit-validation.py keep
$ git -C /root/btc-5m-twap worktree remove /root/tz38-work/wt; echo "exit=$?"
2026-10-31T20:13:49.052071828Z
K copied 47c30dd723e3248eb7f853463797d04cd575df684ab716030208e465a2c67249 /root/btc-forensics/tz38-work--logs--01-work-tree.log
K copied 23be79f0f7f1d3fddfa55aa1ea990a8a8fc1a80d243ecad1120c5ebbbde9778c /root/btc-forensics/tz38-work--logs--02-stage.log
K copied e69fbcba523b830f599c4c7d4ee9f457f12b761b96d032abf372ed32ea8c72de /root/btc-forensics/tz38-work--logs--03-fingerprint.log
K copied e06d5ba3571221f8ba451fa882865307acae31feb4edde45e235de55f3f3814f /root/btc-forensics/tz38-work--logs--04-host.log
K copied d61ce469e232a6b0b0b34bf5103e19a2062fd5edbf7359c06915aea6ce0618fd /root/btc-forensics/tz38-work--logs--05-refs-number.log
K copied c057727ef093274cff87c24d0dbc4a531baebaef2cf941452caeed5fd17fa8f4 /root/btc-forensics/tz38-work--logs--06-branch.log
K copied e9c9b45b79585121e558814d88e19e49e92860e05f746c18a235162767253263 /root/btc-forensics/tz38-work--logs--07-extract-wt.log
K copied f632e6ed18f277a55f4a2535dfe3c0d7e78a097ce9d83b264b5aee22ec9cdb3b /root/btc-forensics/tz38-work--logs--08-commit-push.log
K copied 1dacee4a7d42e61331fd08bcb52c90ad6e8b7439d62743a8a50c6a9a867f6a4e /root/btc-forensics/tz38-work--logs--09-pull-request.log
K copied 7a09349c1a52854328bec405ad890741859cc1ac07fddfeae7bd407f9193c76e /root/btc-forensics/tz38-work--logs--10-selftest.log
K copied 30d3734bedfa658af47d2a9a42f5e12cf40d49f7288c5d413d6c0a9786eab317 /root/btc-forensics/tz38-work--logs--11-scratch.log
K copied 639b0431604d6e6bb1fbbf9a7e531a6afec107597b8d28aeaf472de514ab54a0 /root/btc-forensics/tz38-work--logs--12-reclaim-scratch.log
K copied db339061d09083f62c0ce6110f4c36e45d3ee9705a3f4d9abe0cdd657af34ec2 /root/btc-forensics/tz38-work--logs--12a-reclaim-refused.log
K copied f0a46795404f5df4461501acfe3a21e70d52fe38e58bf48adc87c18377874294 /root/btc-forensics/tz38-work--logs--12b-reclaim-by-boss.log
K copied 70877ee6848b32347f92e06410f386754dadf511e861348343f757be892a69f3 /root/btc-forensics/tz38-work--logs--12c-reclaim-verify.log
K copied 9225f1528c03a520c5d2176aee1c0690642d26b7d463413c82ee67fe561adc70 /root/btc-forensics/tz38-work--logs--13-mark-probe.log
K copied 8c011ef604e3b16fbf1ef52bbe1d68e34bfe3a3687b56d2e6a46bf7e7ac952e3 /root/btc-forensics/tz38-work--logs--14-band-plan.log
K copied ec62cb7a860962e690c585ca88007c562c11ea6384b5ca04f9388fabc8657434 /root/btc-forensics/tz38-work--logs--15-fetch.log
K copied 2559415d559fa68af51666ec97038021a400645ddd71eabac280b7c7bbebe5c1 /root/btc-forensics/tz38-work--logs--16-run-A.log
K copied 2cd10c828d5d2afd19cf9a42e7088518280e3688b4ed3d0dafba8f34441647f6 /root/btc-forensics/tz38-work--logs--17-run-B.log
K copied 609b9bfea4e76040b95f07491be46e3274825cf6e73e6c75161d8a4db84cc3f7 /root/btc-forensics/tz38-work--logs--18-same.log
K copied 8e211fa856c214a35d34a9f3e6528776292c836dd9af4bae6cc04e9b756820ad /root/btc-forensics/tz38-work--logs--19-closing.log
K copied 340f29010d0ab063c8db093615d0d0da68037f8c4ad8b6e0745e9ce985bfcdc3 /root/btc-forensics/tz38-work--logs--20-separation.log
K copied 20f27ed08ae558e294b24d84a5d8f43915500388c6862a40fb009651994d8947 /root/btc-forensics/tz38-work--logs--21-files-written.log
K copied 16bcf7e37448b5b06033fa548178572a22ffaf4b1d407ca68d287f5250920bac /root/btc-forensics/tz38-work--manifest.tsv
K copied b3705da9c9e57fe771540ad01871f95b149658b45e9b88618f40d32bc5ed17ec /root/btc-forensics/tz38-work--out-A--inputs.json
K copied f9efa9c0d195a10701d05f94e81df67cdb9a76ce68e2353c2df0ad9dd43407a6 /root/btc-forensics/tz38-work--out-A--monthly-A.csv
K copied 6a581f6cd548566d40cd5976e74aa82786e85b58f5fd80f8650da2f772886208 /root/btc-forensics/tz38-work--out-A--monthly-G.csv
K copied 029e236ad51a04d6e645b097c228b9d2002115b35d664f1329d7c37bea7ba441 /root/btc-forensics/tz38-work--out-A--random-lists.csv
K copied 4873b6e77e927c5aa0ca59c5f8593a42cd9a05c80c54010efd5e42e2b7471608 /root/btc-forensics/tz38-work--out-A--result.json
K copied aa62838d70efaf50ee819c9e6d90b5e289e6730eab34ecade67ba24fbbd769da /root/btc-forensics/tz38-work--out-A--trades-P-rule.csv
K copied b31d6e0910a2bf3516abe14c264e679fa8077b7ce3b80e2dfc0113c5dc3e123d /root/btc-forensics/tz38-work--out-A--trades-P-strong-3.csv
K copied c19fcdac3e44e81bad26744d37ae4c65b52b9f9a60afd0ffc05e82b29c5c4929 /root/btc-forensics/tz38-work--out-A--trades-P-strong-5.csv
K copied a2b36e1e5fa26a5c57a54467ba6c2b5c3a63f06d99f2f8a240c830958c082729 /root/btc-forensics/tz38-work--out-A--trades-P-strong-7.csv
K copied b3705da9c9e57fe771540ad01871f95b149658b45e9b88618f40d32bc5ed17ec /root/btc-forensics/tz38-work--out-B--inputs.json
K copied f9efa9c0d195a10701d05f94e81df67cdb9a76ce68e2353c2df0ad9dd43407a6 /root/btc-forensics/tz38-work--out-B--monthly-A.csv
K copied 6a581f6cd548566d40cd5976e74aa82786e85b58f5fd80f8650da2f772886208 /root/btc-forensics/tz38-work--out-B--monthly-G.csv
K copied 029e236ad51a04d6e645b097c228b9d2002115b35d664f1329d7c37bea7ba441 /root/btc-forensics/tz38-work--out-B--random-lists.csv
K copied 4873b6e77e927c5aa0ca59c5f8593a42cd9a05c80c54010efd5e42e2b7471608 /root/btc-forensics/tz38-work--out-B--result.json
K copied aa62838d70efaf50ee819c9e6d90b5e289e6730eab34ecade67ba24fbbd769da /root/btc-forensics/tz38-work--out-B--trades-P-rule.csv
K copied b31d6e0910a2bf3516abe14c264e679fa8077b7ce3b80e2dfc0113c5dc3e123d /root/btc-forensics/tz38-work--out-B--trades-P-strong-3.csv
K copied c19fcdac3e44e81bad26744d37ae4c65b52b9f9a60afd0ffc05e82b29c5c4929 /root/btc-forensics/tz38-work--out-B--trades-P-strong-5.csv
K copied a2b36e1e5fa26a5c57a54467ba6c2b5c3a63f06d99f2f8a240c830958c082729 /root/btc-forensics/tz38-work--out-B--trades-P-strong-7.csv
K copied 83eb4f03ee3c2639894d2019a67539c5156dad97a33df2149512709dea5bb098 /root/btc-forensics/tz38-work--plan.json
K copied bd5cf4bbe57622b9ee0d4b8f1c44498ee69effafaf3d00c1aafd51fc542d25cb /root/btc-forensics/tz38-work--state.json
KEEP PASS: 45 files kept, 45 copied, 0 already held; forensic store 2267 -> 2312 files; worktree at 8f37199aa4f9e14cb08534b1be3b7c258af917c2, its upstream's
exit=0
```

The second call — the removal, its proof, the worktrees, the store and the free space:

```
$ date -u +%Y-%m-%dT%H:%M:%S.%NZ
$ rm -rf /root/tz38-work; echo "exit=$?"
$ test -e /root/tz38-work; echo "exit=$?"
$ git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
$ find /root/btc-forensics -type f | wc -l
$ df -B1 --output=source,size,avail /var/lib/btc-recorder
2026-10-31T20:13:56.296332002Z
exit=0
exit=1
/root/btc-5m-twap       f7f7deb [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
2312
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10001342464
```

**V15 (keep):** `KEEP PASS` — 45 files kept, 45 copied, 0 already held: `state.json`, `plan.json`, `manifest.tsv`, the 24 logs
and the nine files of each of `out-A/` and `out-B/`, each hash verified after its copy; the store `2,267` → `2,312`, equal to
before plus the 45 copies, asserted by `keep` and read again by `find`; the worktree at `8f37199`, its upstream's, with nothing
in `git status --porcelain --ignored`. `21-files-written.log`'s final hash is `20f27ed0…`. The store, the stage and the
worktree were not copied, as §9 says. **V16:** `git worktree remove` without `--force`, `exit=0`; `rm -rf /root/tz38-work`
`exit=0`; `test -e` `exit=1`; `git worktree list` names `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else.
`/dev/vda2` free `10,001,342,464` bytes, against `9,709,277,184` at §3.7 and `10,089,811,968` at §0.3. The branch
`tz-38-adv3-pit-validation` stays on `origin` and as a local ref.

---

## 3. Publication

| item | value |
|---|---|
| branch | `tz-38-adv3-pit-validation`, pushed 19:23 UTC through the URL's own credential |
| commit | `8f37199aa4f9e14cb08534b1be3b7c258af917c2`, parent `f7f7deb1e05bddd480c1249cb765ce83ee1296f4`, one file, `+1782 −0` |
| pull request | #38, `https://github.com/seahomebatumi-ai/btc-5m-twap/pull/38`, base `main`, open, not merged |
| Release | none: this TZ publishes no asset |
| deployment | none: no unit, service copy or advisor file touched |
| separation self-check | §2.9: `0`; `research/tz38-adv3-pit-validation.py`; nothing |
| report | this file, to `main` after B-RECLAIM-OWN |

---

## 4. Gate

The procedural gates of §4.1, each as the TZ fixes it:

| gate | passes when (§4.1) | read | ratio | verdict |
|---|---|---|---|---|
| FINGERPRINT | `67 of 67` | 67 of 67 | 1.000 | **PASS** |
| HOST | `11 of 11` | 11 of 11 | 1.000 | **PASS** |
| NUMBER | `2 of 2` at each | 2 of 2, 2 of 2 | 1.000 | **PASS** |
| G-FILE | the file's lines, bytes and SHA-256; the diff as §3.1 | 1782, 90,181, `579474b6…` at both; `A`; `1782	0` | 1.000 | **PASS** |
| SELFTEST | `58 of 58` | 58 of 58 | 1.000 | **PASS** |
| P-START | `4 of 4` | served 4 of 4 | 1.000 | **PASS** |
| G-FETCH | `FETCH PASS`, no planned key absent | 66,677 of 66,677 | 1.000 | **PASS** |
| G-DATA | `42 of 42` | 42 of 42, in A and in B | 1.000 | **PASS** |
| G-EQUAL | `20 of 20` | 20 of 20 (FACTS alone), in A and in B | 1.000 | **PASS** |
| DETERMINISM | `10 of 10` | 10 of 10 | 1.000 | **PASS** |
| STILL | `4 of 4` | 4 of 4 | 1.000 | **PASS** |

**The readings carry no threshold of this TZ (§4.2–§4.4).** E1's procedure reads **UNDECIDABLE** — `p_t` up `0.073`,
`p_boot` up `0.081`, against `ALPHA = 0.05` for both; E2's **UNDECIDABLE** — `0.110` and `0.132`; E3's **REPLICATED** — `0.028`
and `0.028`. Each is §1's: the Architect's exploration, re-derived, which moves no rung. Nothing was tuned and nothing
reinterpreted. Per §4.7, a PASS establishes that the instrument runs on the host and that the archive's own bytes, fetched by
the Executor and listed in a manifest, give the numbers the Architect holds — here byte for byte. It does not establish that
the rule earns, on any contract, in any year to come. It moves no rung and says nothing about direction.

---

## 5. Validation

| # | check | count | asserted? |
|---|---|---|---|
| **V1** | §0.2's fingerprint | `READING FINGERPRINT: PASS - 67 of 67`: revision; 6 anchors, 4 re-derived; 57 rows, 54 of 54 `frozen` equal; the shape; the loader's hash | asserted by the instrument (`verdict` raises, exit 1) |
| **V2** | §0.3's host gate | `READING HOST: PASS - 11 of 11`; the first memory read 211,165,184 bytes, no second read | asserted by the instrument |
| **V3** | NUMBER at §0.5 and §3.1 | `PASS - 2 of 2` each, the `TZ-38-` path printed; the branch count `0` | NUMBER asserted; the branch count recorded, not asserted — read `0` by the Executor |
| **V4** | §0.1's and §3.1's file | 1 of 1 hash at each, asserted by the script; 1782 lines, 90,181 bytes at both; `A`; `--numstat` `1782	0` | hash asserted; the diff's names and numstat recorded, not asserted — compared by the Executor with §3.1's text, exact |
| **V5** | the self-test | `58 of 58`, the causality by perturbation and its negative control among them (§2.2) | asserted, each check by `ok` |
| **V6** | P-START | `READING P-START: served - 4 of 4 endpoints`, each line printed | asserted by `mode_probe` |
| **V7** | PLAN and G-FETCH | 895 symbols, 66,677 keys, 3,771 listing calls; 66,677 files, 67,600,876 bytes; manifest `16bcf7e3…`; no key absent | the fetch asserted (`assert not absent`); the plan's counts printed, not asserted |
| **V8** | G-DATA | `READING G-DATA: PASS - 42 of 42`, in A and in B | asserted |
| **V9** | G-EQUAL | `READING G-EQUAL: PASS - 20 of 20 (FACTS alone)`, in A and in B | asserted |
| **V10** | E1 to E8 | every table of `result.json` §1 names — `pit_rule`, `pit_strong`, `sensitivity`, `P_rule`, `P_strong.top3`, `top5`, `top7`, `random_lists`, `A_admissible`, `weakening` — printed in §2.7; the largest anonymous set of each run; the OUT lines | present by the run's construction; the readings recorded, not asserted — no threshold |
| **V11** | DETERMINISM | `READING DETERMINISM: PASS - 10 of 10`; the nine files' SHA-256 of A and of B, equal | asserted by `same` |
| **V12** | STILL | `READING STILL: PASS - 4 of 4` | asserted |
| **V13** | contract §4.2's self-check | `0`; one file; nothing | recorded, not asserted |
| **V14** | §3.7's closing reads | every read printed, §2.8 | recorded, not asserted — no threshold |
| **V15** | B-RECLAIM-SCRATCH and §9's `keep` | reclaim: 2 files considered, 0 copied, store 2,267 → 2,267; keep: 45 kept, 45 copied, 0 held, store 2,267 → 2,312 | asserted by `reclaim` and `keep` (the store's count) |
| **V16** | §9's removals | `git worktree remove` `exit=0` without `--force`; `rm -rf` `exit=0`; `test -e /root/tz38-work` `exit=1`; `git worktree list` the two | exit codes recorded, not asserted |

---

## 6. What could not be implemented as written

1. **One block refused to the Executor and run by the Boss.** Claude Code's auto mode classifier refused B-RECLAIM-SCRATCH's
   `reclaim` as "[Irreversible Local Destruction]" before it ran. The Executor confirmed that nothing had changed (no
   `12-reclaim-scratch.log`, both directories present), recorded it in `12a-reclaim-refused.log` and did not retry it in any
   form. It went to the Boss by §3.3's route (map §6, sandbox limit) as one `reclaim` naming both directories and one `rm -rf` and
   one `test -e` a directory — §3.3's commands, every path in full — the removals gated on `grep -q '^RECLAIM PASS'` of the log
   and every output written to it. He ran it in his login at 19:43:14 UTC, and the Executor verified it from the log, `test -e`
   and `find` (`12c`).
2. **§3.4 and §3.5 ran before §3.3 finished.** The TZ orders §3.3 before §3.4. The refusal came at 19:24 UTC with the band closing
   at 20:30, and the plan, the fetch and the two runs needed about 45 minutes. So the Executor ran the mark, P-START and the
   band-gated chain while B-RECLAIM-SCRATCH waited for the Boss, who ran it at 19:43:14, during the fetch. The block touches only
   the two earlier scratch directories under `/tmp/claude-0/`, nothing the mark, the probe, the plan, the fetch or the runs read
   or write.
3. **The band's wait before each run, and one unattended chain.** §3.5 to §3.7 wait for the band and §3.5's block alone carries
   the wait. The Executor ran §3.5's and §3.6's blocks as one background command: the wait and `plan`, `fetch`, the same wait
   loop and a `/proc/meminfo` read before each run, then `same`. Each step started only if the previous log ended in `exit=0`, so
   neither run could start outside the band. Every wait passed at once (19:25:39, 20:01:27, 20:05:20), and §3.7's reads ran at
   20:09:23.
4. **Timing wrappers.** `selftest` ran under `/usr/bin/time -v`. `mark`, `probe`, `plan`, `fetch`, both runs, `same` and `still`
   ran under `/usr/bin/time -f`, for each mode's `ru_maxrss`, which §8 asks for and which these modes do not print. The wrapper
   sat inside each `timeout`. `fingerprint`, `host`, `number`, TZ-35's `scratch` and `keep` ran bare, so their peaks were not
   measured. The commands under test and their arguments are the TZ's.
5. **The logs' names.** Every step's log is numbered in this TZ's order, and `01-work-tree.log` was written after the `mkdir` from
   its captured output. `mark` and `probe` share `13-mark-probe.log`, and the band's wait and `plan` share `14-band-plan.log`.
   Logs this TZ does not name: `08-commit-push.log`, `09-pull-request.log`, `12a-reclaim-refused.log`, `12b-reclaim-by-boss.log`,
   `12c-reclaim-verify.log`, `20-separation.log` and `21-files-written.log`. Each is kept by `I keep`.
6. **Contract §1.** Step 1 was `git fetch origin` and `git pull origin main`, a fast-forward from `7600235` to `f7f7deb`. Step 2:
   this TZ in full, its Appendix A read in the parts the run turns on (`main`, `mode_plan`, `mode_fetch`, `mode_run`,
   `run_measure`, `mode_same`, `mode_keep`, `still_reading`, the self-test's bookkeeping). The map was read in the sections the TZ
   rests on — §0, the start of §1, §6's rows (host, host identity, git remote, memory, both sandbox limits) and §7 items 125 to
   139 — not every line (map §7 item 139). The fingerprint read every row. Before §0.0's `mkdir` the Executor read the
   repository's listing and `git log`, the contract, the TZ-37 report's sections, the memory note on refused blocks, and — to learn
   whether this session ran on the capture host — `ls /var/lib/btc-recorder`, `df` of its filesystem, `hostname`,
   `systemctl is-active` of the recorder and the bot, `ls /root` and the interpreter's path.
7. **Reads no step names**, none under `/etc/adv3-bot/` and none printing a price: `get_session` for the model; the TZ's and
   the map's hashes; `ps` of the `claude` processes after `scratch`; `git config` and `gh pr view 37` for the commit's and the
   pull request's form; two reads of `/proc/meminfo`, `df` and the store's listing during the fetch (§0.5); and the comparison of
   run A's files with §4.6's hashes (§2.6), which the TZ gives the verdict.
8. **The session's scratchpad held the Executor's working files**, against §0.0's "nothing to the session's scratchpad": the
   progress monitor's state file, the script that built §2.7's tables from `out-A/result.json`, and this report's template with
   the script that inlined the logs into it by substitution, so that no log line was retyped. No step's output went there:
   every step wrote to `logs/`.
9. **The pull request's body** was written to `/root/tz38-work/pr-body.md` after `I host` had read the tree, and removed right
   after `gh pr create`. No later step reads the tree's top level.
10. **The commit message and the pull request's text** are the Executor's own.
11. **B-RECLAIM-OWN**: in two calls, a `date -u` before each — `keep` and `git worktree remove`, then the rest — every command §9's and in its order; neither was refused. Its output, written to no file, is pasted into §2.13 from the session.

Nothing else: every gate was read by the instrument's own modes on Appendix A's bytes.
