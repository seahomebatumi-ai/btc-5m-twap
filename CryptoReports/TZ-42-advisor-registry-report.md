# TZ-42 report — the registry of STRONG signals, append-only and hash-chained, each walked on Binance's 1- and 5-minute candles; the model's defaults — 200,000 USDT, 0.5 % a trade, 10 % in all, a stop within 14 %; the second check at 15:07 UTC; a reply keyboard

**NUMBER PASS: 2 of 2** at §0.5 (16:50:30 UTC) and again at §3.1 (16:50:44 UTC): `CryptoTZ/` holds `TZ-42-advisor-registry.md` and no other `TZ-42-` file, `CryptoReports/` no `TZ-42-` report; the branch count `0` before the push.
**G-RULE PASS: 8 of 8** — `RULE-ADV-3.txt`, the unit file, `adv3.py` and `selftest-adv3.py` `main`'s byte for byte; `adv3-bot.py`: 16 definitions changed, 57 added, 23 removed, the 23 others identical by AST; 4 assignments changed, 21 added, 3 removed; `due` and `done_after` their docstrings alone changed; the branch's bot Appendix A's · **SELFTESTS: 57 of 57, 135 of 135, 102 of 102.**
**B-DEPLOY `exit=0`** (mark 20:34:15 UTC) · **COPY PASS: 5 of 5** · **G-RENDER PASS: 34 of 34** on live data — the scratch registry **10 events** (seed 1, open 4, fill 4, stop 1), **4 signals, all legacy: 3 open, 1 ended by a stop**, none by an exit, none expired, seeded from 28 records and 44 STRONG cards; **27 candle requests, 4 of them of 1-minute candles, 10,017 candles**; the signal check **quiet, full**, 1 part, 0 events announced, 0 signals opened; the fact check **quiet, one line**, 1 part, 0 and 0; **PEAK `72,593,408` bytes resident**, 28.59 s wall, 4.01 s processor · **P-START: served - 6 of 6 endpoints, 8 requests**.
**B-KILL `exit=0`** (mark 20:35:20 UTC), `check-done` **`2026-11-05 fact` → `2026-11-04 fact`** · **UNIT-NEW PASS: 9 of 9** — pid `3851184` → `284419`, started 20:35:50 UTC, `NRestarts` 4 → 5, the three capture units unchanged · **G-FIRST PASS: 10 of 10** — the replayed `2026-11-05 signal` of the close of 2026-11-04, **quiet, full, 1 message**, 0 events announced, 0 signals opened, STRONG at every rank 1, sent 20:36:06 UTC; `check-done` `2026-11-05 fact`; **the unit's registry seeded: 10 events, 4 signals — 4 legacy, 3 open**, from the journal of 28 records and 44 STRONG cards, `6083fd15d499…`, the kill mark's.
**No rollback ran**: B-ROLLBACK, B-KILL2, UNIT-OLD, K-42, STOPPED and B-ASIDE were not run; no gate failed.
**The unit runs the new code**: `adv3-bot.service` `active`, `enabled`, pid `284419`, the service copy's `adv3.py` `81ef0112…` and `adv3-bot.py` `c3d9fff5…`, `commit.txt` `4e6db2d16dda3da14957120d636f537dfc0bcc87` — verified by `I copy`, `I unit new` and `I first` (20:34:22 – 20:36:14 UTC) and by the Executor's own §3.7 closing reads (20:36:27 UTC: `systemctl show`, `is-enabled`, `journalctl`, `service.log`, `ls`, `check-done`).
**One command was refused by Claude Code's auto mode classifier, before it ran, and handed to the Boss unchanged:** B-RECLAIM-SCRATCH's `reclaim` (20:33 UTC, "judged this action dangerous (it gave no explanation)"), run by the Boss at 20:47:45 UTC — `RECLAIM PASS`, 0 files considered, none copied, the store `2,370` → `2,370`; both of TZ-40's directories removed, `test -e` `exit=1` each, in his log and in the Executor's own read. Every other block — B-DEPLOY, COPY, G-RENDER, P-START, B-KILL, UNIT-NEW and G-FIRST — ran in the Executor's session and was not refused; no paste of §3.6 was needed.
**Departures, all in §6:** the session interrupted for 3 h 41 min between §3.1's staged diff and its commit, by the Boss's usage limit; the remote-control directory of 2026-10-30, `238335b9…`, named **earlier** by `scratch` and left untouched; the refused `reclaim`; the logs' names for steps whose name the TZ does not fix; one helper file written and removed unread by any gate in the work tree; Appendix A's code and the map read in part, the code verified by hash; no new STRONG signal on the day of the run; `setMyCommands` logs only a refusal.

| field | value |
|---|---|
| TZ | `CryptoTZ/TZ-42-advisor-registry.md`, 5,170 lines, 431,289 bytes, SHA-256 `2a1a95a152a67cd161023675db754d6de1bfdc0acaffb1214e1330c48ef78243`, landed at `4ac4169` (2026-11-05 16:47:15 UTC), above `0ec452e` (TZ-41's specification), `494f10f` (PR #40's merge) and `a1c7ba1` (revision `2026-11-01-b`) |
| map revision | `2026-11-01-b`, equal; anchors 6 of 6; re-derived 4 of 4; rows 60; `frozen` equal 57 of 57; the map 2,033 lines, 536,884 bytes, SHA-256 `1396fa805e9eb72cc36f449c60698822f8d4c2e5314fdd6856f030e07fc46472`, the file TZ-42 §10 names |
| executor model | the model the TZ header names: `get_session` read `configured_model`, `session_context.model` and `external_metadata.last_served_model` all `claude-opus-5-5` |
| branch | `tz-42-advisor-registry` at `4e6db2d16dda3da14957120d636f537dfc0bcc87`, on `origin/main` `4ac4169`; pushed; pull request #41, open, not merged |
| service's code | `/root/adv3-bot-svc/`: `adv3.py` `81ef0112…` (unchanged, not copied), `adv3-bot.py` `c3d9fff5…` (was `9e622daf…`), `commit.txt` `4e6db2d16dda…` (was `433ce139eedc…`) |
| unit | `/etc/systemd/system/adv3-bot.service` `82acd8e4…`, unchanged; never reloaded |
| interpreter | `/root/tz04a-env/venv/bin/python` 3.12; every session mode under `nice -n 19` and `-B` |
| marks | `deploy` 20:34:15.801 UTC · `kill` 20:35:20.598 UTC (`state.json`, `t` `1793910855.8007286` and `1793910920.598368`) |
| blocks | B-RECLAIM-SCRATCH: refused to the Executor 20:33 UTC; handed to the Boss about 20:34 UTC and again at 20:40 UTC; run by the Boss 20:47:45 UTC · B-DEPLOY to G-FIRST: the Executor's, none refused · B-RECLAIM-OWN: §2.9 |
| work tree | `/root/tz42-work/`, created 16:50 UTC, removed by B-RECLAIM-OWN (§2.9) |

---

## 0. Fingerprint

`I fingerprint`, from the staged copy of the checker, against the primary checkout at `4ac4169` — revision
`2026-11-01-b`; anchors `A1` `229a944f2d51`, `A2` `6c5089330629`, `A3` `0-complete / 1-student-5tau-not-disqualified /
2-no-edge-4tau-240-undecidable`, `A4` `437b45ea196b`, `A5` `0f6c90451cbd`, `A6` `729f0bcdbee3`, each equal to the TZ
header's; `A2`, `A4`, `A5` and `A6` re-derived. **V1: `READING FINGERPRINT: PASS - 69 of 69`** (16:50:13 UTC). The map,
the `reported` row: 2,033 lines, 536,884 bytes, SHA-256 `1396fa805e9eb72cc36f449c60698822f8d4c2e5314fdd6856f030e07fc46472`.

### 0.1 The 60 rows of the map's §0 table

Built from `logs/02-fingerprint.log` by a substitution; "equal" stands for each of the 57 `ok   frozen <path>` lines the
checker asserted against the map's lines, bytes and SHA-256. The advisor rows are TZ-40's hashes, as the TZ says they
stay until its verdict.

| path | lines | bytes | state | SHA-256 | against the map |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 2,033 | 536,884 | reported | `1396fa805e9eb72cc36f449c60698822f8d4c2e5314fdd6856f030e07fc46472` | printed |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | equal |
| `research/twap-divergence.py` | 1,135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | equal |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | equal |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | printed |
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
| `research/tz39-advisor-checks.py` | 1,139 | 73,892 | frozen | `18294b0916d77b226083a18f9521f06e2fddb423bbc947a2e1100fd42b2980f3` | equal |
| `research/tz40-advisor-strong.py` | 1,436 | 95,474 | frozen | `4403b27185f7e9aaa090dedfca457af6c4f70b6b020f0d2fcd9f9fbb96b6054b` | equal |
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
| `advisor/adv3.py` | 895 | 51,834 | frozen | `81ef0112d3fe4b86566e51a51aab924d9776ff37a927e65982ecb0bb7c1f34e1` | equal |
| `advisor/adv3-bot.py` | 1,869 | 126,909 | frozen | `9e622daf2e8a5ec3e93f15c7f56e7cf859547fbd3771daad75bc6532adb2b9d1` | equal |
| `advisor/selftest-adv3.py` | 256 | 19,111 | frozen | `6f29b82f2b2ca82cd2ff4bbb370e032354dbb4743497330530777429b3af7398` | equal |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | printed |

---

## 1. Input

| input | read | size | hash or count |
|---|---|---|---|
| the TZ | `CryptoTZ/TZ-42-advisor-registry.md` at `4ac4169` | 5,170 lines, 431,289 bytes | `2a1a95a152a67cd161023675db754d6de1bfdc0acaffb1214e1330c48ef78243` |
| Appendix A, extracted (§0.1) | `advisor/adv3-bot.py`, `research/tz42-advisor-registry.py` | 2,548 lines, 157,438 bytes; 2,088 lines, 134,077 bytes | `c3d9fff54f3585cfc4c33b5f7e1f93b390e62b03e0b4725fee2d6fdda6d04c11`; `b6c45490b2f86f5c4678c645041ef1556b1199a6bc814470de904aedf7f5105f` |
| the map | `SYSTEM-MAP.md` at `4ac4169` | 2,033 lines, 536,884 bytes | `1396fa805e9eb72cc36f449c60698822f8d4c2e5314fdd6856f030e07fc46472` |
| the bot's journal | `/var/lib/adv3-bot/journal.jsonl`, by `host`, the marks, `render` (a copy into `render-state/`) and `first` | `137,540` bytes, 28 records at the host gate and both marks; `144,355` bytes at the closing read | SHA-256 `6083fd15d499…` at both marks, the journal the seed read; 44 STRONG cards with an entry, 4 coins, 25.4 coin-days (H9) |
| the unit's registry | `/var/lib/adv3-bot/registry.jsonl` and `registry-state.json`, by `first`; neither existed at the host gate or the marks | `3,772` and `328` bytes at the closing read | 10 events, 4 signals (G-FIRST) |
| Binance's public futures market | by the service copy's bot inside G-RENDER and P-START, and by the unit itself | 27 candle requests and 10,017 candles in G-RENDER | taken as served |

**Nothing was re-collected:** this TZ reads no dataset; the live market was read by the bot's own functions and the
render's copy of the journal and its scratch registry were removed with the work tree, never printed and never kept.

---

## 2. Measurements

### 2.1 Host gate (§0.3), 16:50:20 UTC — V2

The commands of §0.3 in their order, `logs/03-host.log` verbatim (the scratch listing of the block's last line is that
of the moment, before B-RECLAIM-SCRATCH):

```
Thu Nov  5 04:50:20 PM UTC 2026
1793897420
2026-08-02 07:24:32
1
MemTotal:         978640 kB
MemAvailable:     267472 kB
SwapTotal:       3174396 kB
SwapFree:        2412200 kB
check records: 11; slots 2026-11-01 s 2026-11-01 f 2026-11-01 s 2026-11-02 s 2026-11-02 f 2026-11-03 s 2026-11-03 f 2026-11-04 s 2026-11-04 f 2026-11-05 s 2026-11-05 f; delays after their instants, seconds: 0 0 0 0 0 0 1 0; check-done 2026-11-05 fact
journal: 137540 bytes, 28 records, 44 STRONG cards with an entry the seed would read, of 4 coins over 25.4 coin-days
units: {"adv3-bot.service": {"ActiveState": "active", "MainPID": "3851184", "NRestarts": "4", "SubState": "running", "UnitFileState": "enabled"}, "btc-pairbook.service": {"ActiveState": "active", "MainPID": "212450", "NRestarts": "22", "SubState": "running", "UnitFileState": "enabled"}, "btc-recorder.service": {"ActiveState": "active", "MainPID": "2388318", "NRestarts": "0", "SubState": "running", "UnitFileState": "enabled"}, "btc-rewardbook.service": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1", "SubState": "running", "UnitFileState": "enabled"}}
MemAvailable first 268447744 bytes, second not read, deciding 268447744; /dev/vda2 free 10025005056 bytes
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
ok   H5 adv3.py and adv3-bot.py are TZ-40's
ok   H5 the installed unit file is TZ-35's
ok   H5 commit.txt is 40 hex characters and a newline
ok   H6 the record holds a journal of whole lines and a check-done naming a slot
ok   H7 the check records from TZ-40's replay, the last naming 2026-11-01 signal, name strictly later slots, each once
ok   H7 every check after TZ-40's replay - at least one - stamped at or after its slot's instant
ok   H7 check-done names the last check's slot, or the fact slot its signal check covered
ok   H8 no registry yet: neither registry.jsonl nor registry-state.json in the record
ok   H8 before 2026-11-08 07:00 UTC, or TZ-41's report on main
ok   H8 TZ-41's work tree absent
ok   H9 the journal's STRONG cards span at most 120 coin-days, the span G-RENDER's memory floor was measured at
ok   memory gate: MemAvailable at least 150369520 bytes, a first read below it read again after 60 s
ok   disk gate: /dev/vda2 free at least 7400000000 bytes
READING HOST: PASS - 23 of 23
exit=0
NEXT                        LEFT LAST                         PASSED UNIT                         ACTIVATES
Fri 2026-11-06 01:30:20 UTC   8h Thu 2026-11-05 07:04:00 UTC  9h ago btc-rewardbook-archive.timer btc-rewardbook-archive.service
Fri 2026-11-06 02:23:55 UTC   9h Thu 2026-11-05 06:33:59 UTC 10h ago apt-daily.timer              apt-daily.service
Fri 2026-11-06 03:00:20 UTC  10h Thu 2026-11-05 06:44:00 UTC 10h ago btc-pairbook-archive.timer   btc-pairbook-archive.service
Fri 2026-11-06 06:15:57 UTC  13h Thu 2026-11-05 06:33:53 UTC 10h ago apt-daily-upgrade.timer      apt-daily-upgrade.service

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
total 188
drwxr-xr-x  2 root root   4096 Nov  1 18:05 .
drwx------ 31 root root   4096 Nov  5 16:49 ..
-rw-r--r--  1 root root 126909 Nov  1 18:05 adv3-bot.py
-rw-r--r--  1 root root  51834 Nov  1 18:05 adv3.py
-rw-r--r--  1 root root     41 Nov  1 18:05 commit.txt

/var/lib/adv3-bot:
total 172
drwx------  2 root root   4096 Nov  5 12:10 .
drwxr-xr-x 65 root root   4096 Oct 29 14:35 ..
-rw-r--r--  1 root root     15 Nov  5 12:10 check-done
-rw-r--r--  1 root root     10 Nov  1 06:00 daily-sent
-rw-r--r--  1 root root 137540 Nov  5 12:10 journal.jsonl
-rw-r--r--  1 root root      9 Nov  3 18:54 offset
-rw-r--r--  1 root root  10033 Nov  5 12:10 service.log
670724595	/var/lib/btc-rewardbook
946821216	/var/lib/btc-pairbook
147607	/var/lib/adv3-bot
17	/root/.claude
2370
/root/btc-5m-twap       4ac4169 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/tmp/claude-0/-root-btc-5m-twap/04a2fee5-32e8-58fa-ac2a-39fcd1a0c22a/scratchpad
total 36
drwx------  9 root root 4096 Nov  5 16:48 .
drwx------ 35 root root 4096 Nov  5 16:48 ..
drwx------  4 root root 4096 Nov  5 16:48 04a2fee5-32e8-58fa-ac2a-39fcd1a0c22a
drwx------  3 root root 4096 Nov  1 19:08 1757478d-7992-4de0-9586-07061c8d9d71
drwx------  3 root root 4096 Oct 30 13:16 238335b9-cf23-414a-8e8f-ad4705c4d19e
drwx------  3 root root 4096 Nov  1 19:08 3fffc996-af98-504e-be5f-36b76aad2f63
drwx------  3 root root 4096 Nov  5 16:48 4b8e83bc-9b2f-462a-980d-02f5bb70ea9f
drwx------  4 root root 4096 Nov  1 17:52 981b3989-c33d-580f-acc8-abc6c0ea2319
drwx------  3 root root 4096 Nov  1 17:52 e19b6910-2c25-4765-98b9-49d2a819677e
```

`READING HOST: PASS - 23 of 23`. The check records name 11 slots, from TZ-40's replay of `2026-11-01 signal` to
`2026-11-05 fact`; the eight after the replay were stamped `0 0 0 0 0 0 1 0` s after their slots' instants — the clock
fired at every slot of TZ-40's code from 2026-11-01 12:10 to 2026-11-05 12:10 UTC; no gap. The journal: `137,540` bytes,
28 records, 44 STRONG cards with an entry, 4 coins over 25.4 coin-days, under H9's 120. Memory: the checker's first read
`268,447,744` bytes, above `150,369,520`, so no second read. Disk: `10,025,005,056` bytes free on `/dev/vda2`, above
`7,400,000,000`. The forensic store held `2,370` files, map §3's; the worktrees were map §3's two.

### 2.2 Refs (§0.5) — V3

`logs/04-refs.log` verbatim: every ref line, the branch count, NUMBER and the log of `origin/main`. The 59 tags are the
archives' `pairbook-` and `rewardbook-streams-` tags.

```
2026-11-05T16:50:30.716391293Z
fetch exit=0
4ac4169de2f8798fffe5ceb33b2e489afd8ba587	HEAD
4ac4169de2f8798fffe5ceb33b2e489afd8ba587	refs/heads/main
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
d3251aa2bd312409f7b096bfd5968f3bedbd1be5	refs/tags/tz-01a-dataset
ea9290b92b9fa50c22d0560d5d01dfa392af44df	refs/tags/tz-01a-dataset^{}
e299d4e45f48b7efaa8cb18bd54b139fc0627630	refs/tags/tz-27-pairbook-streams
bce5a85be7850a33f95192265b916cc9c5e0aaf1	refs/tags/tz-27-pairbook-streams^{}
ls-remote exit=0
0
CryptoTZ/TZ-42-advisor-registry.md
ok   CryptoTZ/ holds CryptoTZ/TZ-42-advisor-registry.md and no other file of that number
ok   CryptoReports/ holds no report of that number
READING NUMBER: PASS - 2 of 2
exit=0
4ac4169 2026-11-05T20:47:15+04:00 Add files via upload

A	CryptoTZ/TZ-42-advisor-registry.md
0ec452e 2026-11-04T22:22:45+04:00 Add files via upload

A	CryptoTZ/TZ-41-l0-our-quote.md
494f10f 2026-11-01T22:59:29+04:00 Merge pull request #40 from seahomebatumi-ai/tz-40-strong-every-rank

M	advisor/adv3-bot.py
M	advisor/adv3.py
M	advisor/selftest-adv3.py
A	research/tz40-advisor-strong.py
a1c7ba1 2026-11-01T18:54:52+00:00 Update SYSTEM-MAP.md

M	SYSTEM-MAP.md
973a8db 2026-11-01T18:34:32+00:00 TZ-40 report: STRONG at every rank - NUMBER 2 of 2 twice; FINGERPRINT 68 of 68; HOST 19 of 19; SELFTESTS 57, 128 and 86; G-RULE 10 of 10; B-DEPLOY, COPY 5 of 5, G-RENDER 22 of 22 (2 STRONG at every rank, none beyond the TOP-3, 2 placed and 0 more in each allocation), P-START 5 of 5; B-KILL, UNIT-NEW 9 of 9 and G-FIRST 7 of 7, pid 3766156 to 3851184, the replayed check sent quiet with no alert; two refusals by the classifier, each run by the Boss; no rollback; the unit runs 433ce139

A	CryptoReports/TZ-40-strong-every-rank-report.md
```

`main` carries revision `2026-11-01-b`; the refs differ from map §1 by TZ-41's and TZ-42's uploads (`0ec452e`,
`4ac4169`) and the archives' tags since — recorded, not blocking.

### 2.3 Files (§0.1, §3.1) — V4

`logs/01-stage.log` and `logs/10-branch.log`, verbatim — the second with the resume read of §6 item 1 appended after the
staged diff and before the commit:

```
2026-11-05T16:50:07.589595643Z
/root/tz42-work/stage/advisor/adv3-bot.py 2548 157438 c3d9fff54f3585cfc4c33b5f7e1f93b390e62b03e0b4725fee2d6fdda6d04c11
/root/tz42-work/stage/research/tz42-advisor-registry.py 2088 134077 b6c45490b2f86f5c4678c645041ef1556b1199a6bc814470de904aedf7f5105f
exit=0
```

```
2026-11-05T16:50:44.683333241Z
fetch exit=0
CryptoTZ/TZ-42-advisor-registry.md
ok   CryptoTZ/ holds CryptoTZ/TZ-42-advisor-registry.md and no other file of that number
ok   CryptoReports/ holds no report of that number
READING NUMBER: PASS - 2 of 2
exit=0
Preparing worktree (new branch 'tz-42-advisor-registry')
branch 'tz-42-advisor-registry' set up to track 'origin/main'.
HEAD is now at 4ac4169 Add files via upload
worktree exit=0
/root/tz42-work/wt/advisor/adv3-bot.py 2548 157438 c3d9fff54f3585cfc4c33b5f7e1f93b390e62b03e0b4725fee2d6fdda6d04c11
/root/tz42-work/wt/research/tz42-advisor-registry.py 2088 134077 b6c45490b2f86f5c4678c645041ef1556b1199a6bc814470de904aedf7f5105f
extract exit=0
add exit=0
M	advisor/adv3-bot.py
A	research/tz42-advisor-registry.py
1903	1224	advisor/adv3-bot.py
2088	0	research/tz42-advisor-registry.py

--- resumed after an interruption of the session
2026-11-05T20:32:03.188446024Z
MemAvailable:     193480 kB
Filesystem       1B-blocks      Avail
/dev/vda2      31612203008 9473675264
MainPID=3851184
NRestarts=4
2026-11-05 fact
M	advisor/adv3-bot.py
A	research/tz42-advisor-registry.py
1903	1224	advisor/adv3-bot.py
2088	0	research/tz42-advisor-registry.py
2026-11-05T20:32:13.118772988Z
commit exit=0
4e6db2d16dda3da14957120d636f537dfc0bcc87 root <root@vultr.guest> 2026-11-05T20:32:13+00:00
 advisor/adv3-bot.py               | 3127 ++++++++++++++++++++++---------------
 research/tz42-advisor-registry.py | 2088 +++++++++++++++++++++++++
 2 files changed, 3991 insertions(+), 1224 deletions(-)
4ac4169de2f8798fffe5ceb33b2e489afd8ba587	HEAD
4ac4169de2f8798fffe5ceb33b2e489afd8ba587	refs/heads/main
ls-remote exit=0
remote: 
remote: Create a pull request for 'tz-42-advisor-registry' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-42-advisor-registry        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-42-advisor-registry -> tz-42-advisor-registry
branch 'tz-42-advisor-registry' set up to track 'origin/tz-42-advisor-registry'.
push exit=0
2026-11-05T20:32:36.984169768Z
https://github.com/seahomebatumi-ai/btc-5m-twap/pull/41
pr exit=0
```

2 of 2 hashes asserted at each extraction, equal to §0.1's table; `--name-status` exactly `M advisor/adv3-bot.py` and
`A research/tz42-advisor-registry.py`; `--numstat` exactly `1903 1224` and `2088 0`, read twice, before and after the
interruption.

### 2.4 Self-tests and G-RULE (§3.2) — V5, V6

`logs/11-selftests.log` verbatim:

```
2026-11-05T20:32:45.389332652Z
SELFTEST-ADV3 PASS: 57 of 57 checks passed
exit=0
2026-11-05T20:32:45.565767011Z
SELFTEST PASS: 135 of 135 checks passed
exit=0
2026-11-05T20:32:46.123177034Z
SELFTEST PASS: 102 of 102 checks passed
exit=0
2026-11-05T20:32:47.213808575Z
ok   RULE-ADV-3.txt is main's, byte for byte, hashes to the RULE constant, and is adv3.py's
ok   the unit file is main's, byte for byte, and hashes to TZ-35's
ok   adv3.py and selftest-adv3.py are main's, byte for byte - the rule, the report, the card and the ratings untouched
ok   adv3-bot.py: the definitions changed are exactly ['Telegram', 'base_record', 'candidates', 'check', 'check_record', 'compose', 'done_after', 'due', 'event_lines', 'handle', 'hello', 'probe', 'route', 'selftest', 'serve', 'zone_lines'], added ['Registry', 'advance', 'allocate', 'assess_view', 'base_fund', 'bat', 'by_side', 'card_lines', 'carded', 'ceil1', 'ceil5', 'chain_line', 'day_ms', 'ended_line', 'ensure', 'event_line', 'excluded_lines', 'first_window', 'footer', 'from_iso', 'iso', 'item_record', 'klines', 'last_check', 'legend', 'line_hash', 'live_line', 'mean_ci', 'model_plan', 'ms_at', 'new_signal', 'note_lines', 'notes_of', 'notional_of', 'open_risk', 'params', 'params_line', 'pct0', 'position', 'ranking_view', 'reconcile', 'register', 'registry_view', 'risk_line', 'second', 'seed', 'seed_line', 'sg', 'signal_view', 'signed_usdt', 'stats_lines', 'status_of', 't975', 'view_plan', 'walk', 'wilson', 'zones_of'], removed ['alerted', 'alerts_of', 'alloc_fields', 'candidate_lines', 'correlation', 'follow', 'followed_lines', 'forming_candles', 'item_lines', 'journal_scan', 'make', 'numbers', 'offers', 'plan', 'plan_parts', 'plan_strong', 'quiet_line', 'returns_of', 'strong_shares', 'top_n', 'weak_lines', 'weakened', 'zones_left']
ok   adv3-bot.py: the 23 others identical by AST, the 23 this checker names among them
ok   adv3-bot.py: the assignments changed are exactly ['CARD_KEYS', 'HELP', 'SLOTS', 'TOPN'], added ['(CAPITAL, RISK_TOTAL, STOP_MAX, NEW_MAX)', '(K1_MS, K5_MS, K5_PAGE)', '(LIQ_FRAC, Z_CAP, LIQ_DAYS)', '(MARGIN_MIN, MARGIN_MAX, MARGIN_EXC)', '(RANK_LIST, RANK_MAX)', '(REG_FILE, REG_STATE, GENESIS)', 'COMMANDS', 'DAY_MS', 'DEFAULTS', 'HELPS', 'INTERVAL', 'KEYBOARD', 'KEYWORDS', 'LABEL', 'LEGACY_KEYS', 'LOUD', 'NUMBER', 'RANKING', 'REGISTRY', 'SHOWN', 'T975'], removed ['(STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, CROWD, Z_CAP, LIQ_DAYS)', 'FOOTER', 'LIST_MAX']
ok   adv3-bot.py: due and done_after the same code, their docstrings alone changed
ok   the branch's adv3-bot.py is Appendix A's
READING RULE: PASS - 8 of 8
exit=0
```

### 2.5 B-DEPLOY and COPY (§3.4) — V7, V8

`logs/20-b-deploy.log` and `logs/21-copy.log` verbatim:

```
2026-11-05T20:34:15.738169571Z
mark deploy at 2026-11-05T20:34:15Z: bot pid 3851184 NRestarts 4, 11 check records, journal 28 lines 6083fd15d499…, registry none, check-done 2026-11-05 fact
exit=0
```

```
2026-11-05T20:34:22.902320426Z
ok   the service copy holds adv3.py, adv3-bot.py and commit.txt only
ok   adv3.py is main's, unchanged
ok   adv3-bot.py is Appendix A's
ok   commit.txt is the branch head and the worktree's HEAD
ok   the branch's two files equal the service copy's
READING COPY: PASS - 5 of 5
exit=0
```

`bot.before` hashes to `9e622daf…`, TZ-40's bot; `commit.before` holds `433ce139eedc112862ecf678cda6eaa2577d73d3`, TZ-40's
branch head. `adv3.py` was not copied, as §3.4 says.

### 2.6 G-RENDER (§3.4) — V9

`logs/22-render.log` verbatim:

```
2026-11-05T20:34:28.558185365Z
replies: 749 chars in 1 parts, 680 chars in 1 parts, 905 chars in 1 parts, 713 chars in 1 parts, 3357 chars in 1 parts, 903 chars in 1 parts, 903 chars in 1 parts; the bot's log: 8 lines; candle requests 27 - 4 of 1-minute candles - and candles 10017; allocations 6; views 2
registry: 10 events {"fill": 4, "open": 4, "seed": 1, "stop": 1}; 4 signals - 4 legacy, 3 open, 1 ended by a stop, 0 by an exit, 0 expired; the seed of 28 records and 44 cards
signal check: quiet, full, 1 parts; events announced 0; signals opened 0; STRONG at every rank 1; not taken 0, by code []; notes 1; zones 0
fact check: quiet, one line, 1 parts; events announced 0; signals opened 0; STRONG at every rank 1; not taken 0, by code []; notes 0; zones 0
replayed: 5 events walked; signals whose events differ: none
PEAK 72593408 bytes resident; 28.59 s of wall, 4.01 s of processor
ok   every command and both checks answered, no traceback and no failed request in the bot's log
ok   the markup is balanced in every part of every message (b, i)
ok   the registry's chain is whole from the genesis, every line numbered by its place, the file ending in a newline
ok   its first event is the seed, the only one
ok   the signals are numbered 1, 2, ... in the order of their opens
ok   the legacy signals are those this checker's seed opens from the same journal on the same candles, first and in that order
ok   no coin holds two signals open at once
ok   every signal's fill, targets and end, with R and USDT, are those this checker's replay finds on the candles the bot read
ok   every signal open keeps the replay's place: its first candle not walked and its last close passed
ok   the seed names the journal the bot read, by SHA-256 and its records
ok   every signal opened at the default capital, its position whole by this checker's arithmetic at its entry and stop, a legacy one at most the default 0.5 %, a model one at most 1 %
ok   every signal valid to 00:00 UTC two days after the close it is of
ok   a market entry filled at its entry at its issue, a limit never at its issue
ok   the model opens a signal only within 10 % of risk, the signals open then counted
ok   the model's signals of a close at most 7, less the legacy ones of that close
ok   allocate: each wanted risk k x the risk x min(|z|, 3) over their sum, at most 1 %, never rising along the order
ok   allocate: the risk taken within the room and within what each wanted, each at most 1 %
ok   allocate: every position whole, its loss the notional times its stop and both sides' costs, its margin within 0.5 and 4 % of the capital and covering it, its leverage 1 to the rule's, within 0.5 % of the volume
ok   allocate: an item left without a position has the room's reason or the margin's
ok   allocate: each entry and stop this checker's own, the stop within the limit
ok   each «сигнал» reply is the bot's own view sent in its parts, each position written as the plan holds it, at most N items
ok   «сигнал 50000 риск 1 лимит 2 топ 3» rests on its parameters - 50,000 USDT, 1 %, a limit of 2 %, at most 3 - the defaults unchanged
ok   «реестр»: its counts, the chain whole and its fingerprint, the figures
ok   «рейтинг»: the rule's first seven by this checker's own order, ★ exactly on STRONG at every rank
ok   «оценка»: the rung and the next readings, the six ratings, the registry's figures and that they move no rung
ok   «помощь» and an unknown text answer HELP and nothing else
ok   every reply carries the keyboard on its last part alone and a notification; no check carries it
ok   the signal check's flags agree with what it announced, opened and found
ok   the fact check's flags agree with what it announced, opened and found
ok   the check records: their slots, every coin's state ranked by this checker's order, STRONG at every rank, the cards numbered as opened with their positions, the coins not taken with their codes, the registry's head at their events, the defaults and the six ratings
ok   the scratch journal holds, after the bot's own records, request, request, registry, ranking, assess, check, check
ok   the registry's state counts every event announced by the last check and keeps a place for every signal open
ok   the bot's own journal, offset, daily-sent and check-done are as before the run, and no registry is written there
ok   the bot's constants are this TZ's: 200,000 USDT, 0.5 % and 1 % a trade, 10 % in all, a stop within 14 %, 7 new a close, a margin of 0.5 to 4 % of the capital and 3.5 % its exception, 0.5 % of the volume, |z| capped at 3, 0.1 % a side, checks at 00:10 and 15:07 UTC, the rung 1, 1.1 s between parts, |z| 1 for STRONG, candles of 1 and 5 minutes
READING RENDER: PASS - 34 of 34
exit=0
```

The seven replies — «сигнал», «сигнал 50000 риск 1 лимит 2 топ 3», «реестр», «рейтинг», «оценка», «помощь» and «привет»,
in that order — were 749, 680, 905, 713, 3,357, 903 and 903 characters, one part each. **The day held one coin STRONG at
every rank and no new signal to take:** the model opened no signal at either check, both «сигнал» replies wrote none and
no coin was named not taken, so the scratch registry's four signals are all legacy, the seed's — by §4.2's `candidates`,
the one STRONG coin is then one whose signal of this close the registry already held, the Executor's reading of the
counts, not a line the checker printed (§6 item 7). The peak, `72,593,408` bytes, is below §0.4's modelled host figure `75,184,760`;
the floor the gate used was twice that.

### 2.7 P-START (§3.5) — V10

`logs/23-probe.log` verbatim:

```
2026-11-05T20:35:04.535479981Z
P-KLINES served: 1499 closed daily candles of BTCUSDT, the last 2026-11-04 - 13 5-minute candles of the last hour and 4 1-minute candles of the last minutes
P-FUNDING served: 10 settlement days of BTCUSDT since 2026-10-27
P-MARKS served: 945 perpetuals, all 42 coins among them with a mark price
P-INTERVALS served: 820 perpetuals with an adjusted funding interval, 42 of the coins among them
P-TELEGRAM served: bot @ClaudeCryptoSignal_bot, 0 commands in its menu
READING P-START: served - 6 of 6 endpoints, 8 requests
exit=0
```

`getMyCommands` returned 0 commands: the probe ran before the restart, under which the new process calls `setMyCommands`
(§2.10).

### 2.8 B-KILL, UNIT-NEW and G-FIRST (§3.5) — V11, V12

`logs/24-b-kill.log`, `logs/25-unit-new.log` and `logs/26-first.log` verbatim — UNIT-NEW's first run, 54 s after the mark,
and G-FIRST's first, each `PASS`, so neither printed `NOT YET`:

```
2026-11-05T20:35:20.482654884Z
mark kill at 2026-11-05T20:35:20Z: bot pid 3851184 NRestarts 4, 11 check records, journal 28 lines 6083fd15d499…, registry none, check-done 2026-11-05 fact -> 2026-11-04 fact, replayed by the new process at its start
exit=0
```

```
2026-11-05T20:36:14.532913052Z
bot: pid 284419 NRestarts 5 started 2026-11-05T20:35:50Z; captures: {"btc-pairbook.service": ["212450", "22"], "btc-recorder.service": ["2388318", "0"], "btc-rewardbook.service": ["3137952", "1"]}
ok   the unit is active, running and enabled
ok   a new MainPID, one restart more
ok   the process started after the mark and within 90 s of it
ok   the process runs the unit's exact argv, alone
ok   the service copy's adv3.py is main's and adv3-bot.py the new one, and the process started after the copy
ok   the unit file is unchanged
ok   the log shows the new process serving from check-done 2026-11-04 fact
ok   no traceback in the log since the mark
ok   the three capture units unchanged, each active
READING UNIT-NEW: PASS - 9 of 9
exit=0
```

```
2026-11-05T20:36:14.655646274Z
first check: quiet, full, 1 messages; events announced 0; signals opened 0; STRONG at every rank 1; not taken 0; check-done 2026-11-05 fact; registry 10 events, 4 signals - 4 legacy, 3 open; the journal the seed read: 28 records, 44 STRONG cards, 6083fd15d499… (the kill mark's 6083fd15d499…)
ok   exactly one check record since the mark
ok   it is the day's signal check, of the close of the day before, under rule ee206e7c
ok   it was sent: its Telegram message ids
ok   it holds the 42 coins' state, the six ratings, STRONG at every rank, its cards numbered as it opened them with their positions, the coins not taken and their codes, the registry's head at its events and the seed it made; loud exactly with a new signal or an end
ok   check-done names the slot it covers: 2026-11-05 fact
ok   the log since the mark: the new process serving from check-done 2026-11-04 fact, the check sent, no check failed and no traceback
ok   the journal ends in a newline and every line since the mark parses
ok   the registry is whole from the genesis and ends in a newline; its seed first, naming by SHA-256 and its records the journal as the seed read it - its lines before that check's record
ok   every legacy signal is a STRONG card of that journal with an entry, issued at its record's instant
ok   the registry's state counts every event announced and keeps a place for every signal open
READING FIRST: PASS - 10 of 10
exit=0
```

The old process `3851184` received `SIGTERM` at 20:35:20 UTC (systemd: "Consumed 28.922s CPU time, 45.8M memory peak,
53.8M memory swap peak"); systemd restarted the unit at 20:35:50, `RestartSec=30`. The new process served from
`2026-11-04 fact` at 20:35:51, refreshed the candles to the close of 2026-11-04 at 20:35:56 and sent the replayed
`2026-11-05 signal` at 20:36:06, quiet and full, seeding the registry at it; the replay ended after 15:07 UTC, so
`done_after` marked the day's fact check done too, `check-done` `2026-11-05 fact`. **The next scheduled check is the
00:10 UTC signal check of 2026-11-06, the first the unit's clock fires under this code** — the next TZ's host gate reads it
(H7).

### 2.9 B-RECLAIM-SCRATCH (§3.3) and B-RECLAIM-OWN (§9) — V15, V16

**B-RECLAIM-SCRATCH.** `scratch` at 20:32:57 UTC named three directories **live** — `1757478d…` and `3fffc996…`,
born with the remote-control processes of 2026-11-01 19:07:55 UTC, and `4b8e83bc…`, born with this session's process
`263670` — and three **earlier**: TZ-40's `981b3989…` and `e19b6910…`, and `238335b9…`, the remote-control directory of
2026-10-30, which the Executor left untouched (§6 item 2). The Executor's `reclaim` of the two was refused by the
classifier at 20:33 UTC, before it ran; the Boss ran §3.3's one line, the two directories written in, at 20:47:45 UTC.
`logs/12-reclaim-scratch.log` verbatim — `scratch`'s listing, then the Boss's line, appended; the escape sequence his
terminal wrote at the head of his first `date` line is shown as `\x1b]133;C\x07` (§6 item 9):

```
2026-11-05T20:32:57.250067958Z
running 263670 started 2026-11-05T16:48:25.190000Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
running 3859143 started 2026-11-01T19:07:55.950000Z claude
running 3859153 started 2026-11-01T19:07:57.970000Z claude
running 3859164 started 2026-11-01T19:07:58.420000Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
running 3859205 started 2026-11-01T19:08:00.220000Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
1757478d-7992-4de0-9586-07061c8d9d71 born 2026-11-01T19:08:00.000000Z: live, process [3859143, 3859153, 3859164, 3859205]
238335b9-cf23-414a-8e8f-ad4705c4d19e born 2026-10-30T13:16:00.000000Z: earlier
3fffc996-af98-504e-be5f-36b76aad2f63 born 2026-11-01T19:08:01.000000Z: live, process [3859143, 3859153, 3859164, 3859205]
4b8e83bc-9b2f-462a-980d-02f5bb70ea9f born 2026-11-05T16:48:25.000000Z: live, process [263670]
981b3989-c33d-580f-acc8-abc6c0ea2319 born 2026-11-01T17:52:03.000000Z: earlier
e19b6910-2c25-4765-98b9-49d2a819677e born 2026-11-01T17:52:02.000000Z: earlier
exit=0
\x1b]133;C\x072026-11-05T20:47:45.077156796Z
reclaim: 3679 report tokens; forensic store holds 2370 files
RECLAIM PASS: 0 files considered, 0 named by a report, 0 kept by name, 0 copied, 0 already held; forensic store 2370 -> 2370 files
exit=0
2026-11-05T20:47:45.247391405Z
exit=0
exit=1
exit=0
exit=1
```

The Executor's own read at 20:48:15 UTC: `test -e` of each of the two `exit=1`; the scratch parent holds `04a2fee5…`
(this session's), `1757478d…`, `238335b9…`, `3fffc996…` and `4b8e83bc…`; the forensic store `2,370` files.

**B-RECLAIM-OWN**, at 20:49:28 UTC, after §3.7 and with this report drafted in the primary checkout — §9's seven
commands in their order, between a `date -u` before and after, run in the Executor's session and not refused; its
output was written to no file and is quoted here verbatim, every line of it:

```
2026-11-05T20:49:28.238311240Z
K copied 9e622daf2e8a5ec3e93f15c7f56e7cf859547fbd3771daad75bc6532adb2b9d1 /root/btc-forensics/tz42-work--bot.before
K copied edb771eeadad8377cc03283d2b0300b81a4d0b06e0c3ec91ad7ba216107b9b3c /root/btc-forensics/tz42-work--commit.before
K copied d7134aff086e2af8663797ea4098ad1c8f89f23599fe1f713d37101b9e721945 /root/btc-forensics/tz42-work--logs--00-work-tree.log
K copied 5c9de399842b1d2942abf31401af0760ce357ed2f65041845818024a20ccc493 /root/btc-forensics/tz42-work--logs--01-stage.log
K copied 95278b6bb47c4d946afde47292cf05fba8dff8a716d1712a5ec98e7d64244215 /root/btc-forensics/tz42-work--logs--02-fingerprint.log
K copied 2d5289fac54f7d3ebbc9be2b87155ff8bc43fcda86d28cffd4b41f245ce45648 /root/btc-forensics/tz42-work--logs--03-host.log
K copied a28df37920f8ec42ae8f2ea594956cb625ed18c4ed98ef43fe115909792eaf39 /root/btc-forensics/tz42-work--logs--04-refs.log
K copied 8f9678e56ec343ddfafe25087bff47b20fc8644577074bef9fa64e949f19578f /root/btc-forensics/tz42-work--logs--10-branch.log
K copied 8a717c2f1f23ad7cc6ab00247f5b55d1047f8ad86eda5baf7b4050c242d5e324 /root/btc-forensics/tz42-work--logs--11-selftests.log
K copied 14cc85ac2b1d1e32985a5c5e60b1901ba5e6544666eb8199def0c74b9ab4a33f /root/btc-forensics/tz42-work--logs--12-reclaim-scratch.log
K copied f90a6283a7c64d066124dd97a31980aab36cad441eaed7ea96e6d9156962f524 /root/btc-forensics/tz42-work--logs--20-b-deploy.log
K copied 1bb2c9f192cce1608547db0eb7af27e6d45ee734a4883e19e8df864afc047e3f /root/btc-forensics/tz42-work--logs--21-copy.log
K copied a528c101d06893a43bd20e4643af5f883d8fb787b5acc3adcdfc4bfdac7bfcd0 /root/btc-forensics/tz42-work--logs--22-render.log
K copied 5d01d71f06fdd72ccd4b2fd500b78092ef667faabf80cc89871e94fe3d70e951 /root/btc-forensics/tz42-work--logs--23-probe.log
K copied b727d6e7269d770376c609b5d54090ea05edf433d45444cd5da23ac2d3ff086f /root/btc-forensics/tz42-work--logs--24-b-kill.log
K copied b8d01e4e109a7e369f886eb7d707d07795aa196ca7d59a74b0ecd767ae7435af /root/btc-forensics/tz42-work--logs--25-unit-new.log
K copied 01a75dba59427e77d0481cb85086cae6c18255b0d832183a14fd5c93b0bf17e3 /root/btc-forensics/tz42-work--logs--26-first.log
K copied eb904493e1fdb78bb9fda56358d3800f69274a3775a3292d3f3f4387e40614cc /root/btc-forensics/tz42-work--logs--27-closing.log
K copied 6667d60a71b8c0bcd96724ecd6a7248044cc19b6f4167a6c985e950b925d1039 /root/btc-forensics/tz42-work--logs--28-separation.log
K copied 466a71163ed70475819065f3eb9b38150caf1d812ff7ca722ed9f6ff84f3e1b7 /root/btc-forensics/tz42-work--state.json
KEEP PASS: 20 files kept, 20 copied, 0 already held; forensic store 2370 -> 2390 files; worktree at 4e6db2d16dda3da14957120d636f537dfc0bcc87, its upstream's
exit=0
exit=0
exit=1
/root/btc-5m-twap       4ac4169 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
2390
Filesystem       1B-blocks      Avail
/dev/vda2      31612203008 9459564544
2026-11-05T20:49:28.368175752Z
```

`keep` copied 20 files — `bot.before`, `commit.before`, the 17 logs and `state.json` — each by exclusive create, its hash
verified; none was already held; no `*.rolled` exists, B-ASIDE not having run. `git worktree remove` needed no `--force`;
`rm -rf /root/tz42-work` `exit=0` and `test -e` `exit=1`; the worktrees are `/root/btc-5m-twap` and
`/root/btc-recorder-svc` alone. `render-state/` — the copy of the journal and the scratch registry — went with the tree,
never printed and never kept. The branch `tz-42-advisor-registry` stays on `origin` and as a local ref.

### 2.10 Closing reads (§3.7), 20:36:27 UTC — V14

`logs/27-closing.log` verbatim — `systemctl show`, `list-timers`, `is-enabled`, the unit's last 20 journal lines, the last
30 lines of `service.log`, the listings, `check-done`, `free`, `df`, `du` and `state.json`:

```
2026-11-05T20:36:27.949189308Z
MainPID=284419
Result=success
NRestarts=5
MemoryCurrent=48111616
MemoryPeak=51396608
Nice=10
Id=adv3-bot.service
ActiveState=active
ActiveEnterTimestamp=Thu 2026-11-05 20:35:50 UTC

MainPID=2388318
Result=success
NRestarts=0
MemoryCurrent=135438336
MemoryPeak=353542144
Nice=0
Id=btc-recorder.service
ActiveState=active
ActiveEnterTimestamp=Fri 2026-10-23 06:08:56 UTC

MainPID=212450
Result=success
NRestarts=22
MemoryCurrent=1818624
MemoryPeak=53182464
Nice=0
Id=btc-pairbook.service
ActiveState=active
ActiveEnterTimestamp=Thu 2026-11-05 06:48:07 UTC

MainPID=3137952
Result=success
NRestarts=1
MemoryCurrent=13750272
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
NEXT                            LEFT LAST                         PASSED UNIT                         ACTIVATES
Fri 2026-11-06 01:30:20 UTC 4h 53min Thu 2026-11-05 07:04:00 UTC 13h ago btc-rewardbook-archive.timer btc-rewardbook-archive.service
Fri 2026-11-06 03:00:20 UTC       6h Thu 2026-11-05 06:44:00 UTC 13h ago btc-pairbook-archive.timer   btc-pairbook-archive.service

2 timers listed.
enabled
exit=0
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
2026-11-01T18:05:56+00:00 vultr systemd[1]: adv3-bot.service: Sent signal SIGTERM to main process 3766156 (python) on client request.
2026-11-01T18:05:56+00:00 vultr systemd[1]: adv3-bot.service: Deactivated successfully.
2026-11-01T18:05:56+00:00 vultr systemd[1]: adv3-bot.service: Consumed 4.102s CPU time, 43.6M memory peak, 40.1M memory swap peak.
2026-11-01T18:06:27+00:00 vultr systemd[1]: adv3-bot.service: Scheduled restart job, restart counter is at 4.
2026-11-01T18:06:27+00:00 vultr systemd[1]: Started adv3-bot.service - ADV-3 advisor, the Boss's Binance Futures signals over Telegram.
2026-11-05T20:35:20+00:00 vultr systemd[1]: adv3-bot.service: Sent signal SIGTERM to main process 3851184 (python) on client request.
2026-11-05T20:35:20+00:00 vultr systemd[1]: adv3-bot.service: Deactivated successfully.
2026-11-05T20:35:20+00:00 vultr systemd[1]: adv3-bot.service: Consumed 28.922s CPU time, 45.8M memory peak, 53.8M memory swap peak.
2026-11-05T20:35:50+00:00 vultr systemd[1]: adv3-bot.service: Scheduled restart job, restart counter is at 5.
2026-11-05T20:35:50+00:00 vultr systemd[1]: Started adv3-bot.service - ADV-3 advisor, the Boss's Binance Futures signals over Telegram.
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

2026-11-05T12:10:03Z check sent: 2026-11-05 fact for the close of 2026-11-04 | alerts 0 | quiet | one line
2026-11-05T20:35:51Z serving the pinned chat: pid 284419 offset 685120830 check-done 2026-11-04 fact
2026-11-05T20:35:51Z registry: 0 events, 0 signals, 0 open | head 000000000000 | torn 0 | broken -
2026-11-05T20:35:56Z candles refreshed to the close of 2026-11-04 | missing -
2026-11-05T20:36:06Z check sent: 2026-11-05 signal for the close of 2026-11-04 | events 0 | new 0 | quiet | full
/root/adv3-bot-svc:
total 220
drwxr-xr-x  2 root root   4096 Nov  5 20:34 .
drwx------ 31 root root   4096 Nov  5 19:08 ..
-rw-r--r--  1 root root 157438 Nov  5 20:34 adv3-bot.py
-rw-r--r--  1 root root  51834 Nov  1 18:05 adv3.py
-rw-r--r--  1 root root     41 Nov  5 20:34 commit.txt

/var/lib/adv3-bot:
total 188
drwx------  2 root root   4096 Nov  5 20:36 .
drwxr-xr-x 65 root root   4096 Oct 29 14:35 ..
-rw-r--r--  1 root root     15 Nov  5 20:36 check-done
-rw-r--r--  1 root root     10 Nov  1 06:00 daily-sent
-rw-r--r--  1 root root 144355 Nov  5 20:36 journal.jsonl
-rw-r--r--  1 root root      9 Nov  3 18:54 offset
-rw-r--r--  1 root root   3772 Nov  5 20:36 registry.jsonl
-rw-r--r--  1 root root    328 Nov  5 20:36 registry-state.json
-rw-r--r--  1 root root  10424 Nov  5 20:36 service.log
2026-11-05 fact               total        used        free      shared  buff/cache   available
Mem:      1002127360   764936192    86720512       53248   315183104   237191168
Swap:     3250581504   807886848  2442694656
Filesystem       1B-blocks      Avail
/dev/vda2      31612203008 9469190144
14223554	/root/tz42-work
209313	/root/adv3-bot-svc
158913	/var/lib/adv3-bot
865164841	/var/lib/btc-rewardbook
1287172396	/var/lib/btc-pairbook
17	/root/.claude
{
 "marks": {
  "deploy": {
   "bot": {
    "ActiveState": "active",
    "MainPID": "3851184",
    "NRestarts": "4"
   },
   "caps": {
    "btc-pairbook.service": {
     "ActiveState": "active",
     "MainPID": "212450",
     "NRestarts": "22"
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
   "check_done": "2026-11-05 fact",
   "checks": 11,
   "journal_sha": "6083fd15d49964b52d9795f2b1fda4de91a8ceb86a508a96845dff5bb158afc6",
   "lines": 28,
   "records": 28,
   "registry": [],
   "t": 1793910855.8007286
  },
  "kill": {
   "bot": {
    "ActiveState": "active",
    "MainPID": "3851184",
    "NRestarts": "4"
   },
   "caps": {
    "btc-pairbook.service": {
     "ActiveState": "active",
     "MainPID": "212450",
     "NRestarts": "22"
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
   "check_done": "2026-11-05 fact",
   "checks": 11,
   "journal_sha": "6083fd15d49964b52d9795f2b1fda4de91a8ceb86a508a96845dff5bb158afc6",
   "lines": 28,
   "read_done": "2026-11-04 fact",
   "records": 28,
   "registry": [],
   "t": 1793910920.598368
  }
 }
}
```

**The traceback in `service.log`'s last 30 lines is the old process's**, before both marks: the log's dated lines put its
two `getUpdates failed` at 2026-11-05 01:12:32 and 01:13:57 UTC, each followed by a `TimeoutError` traceback, the process
surviving both and sending the 12:10:03 UTC check after them; UNIT-NEW and G-FIRST read no traceback since the mark. The
log since the mark holds four lines: the new pid serving from `2026-11-04 fact`, the registry loaded empty (`0 events,
0 signals, 0 open | head 000000000000 | torn 0 | broken -`), the candles refreshed, the check sent. **No line
`setMyCommands refused` stands since the mark:** the new code logs the call only on a refusal (`serve`, Appendix A line
1637 to 1639), so the call returned without an exception; that Telegram shows the menu is not established (§4.5). The
cgroup's `MemoryPeak` of the new process read `51,396,608` bytes, page cache included, under `MemoryMax=128M`.

### 2.11 Memory and free space, each read

| instant (UTC) | read | `MemAvailable` | free on `/dev/vda2` | bound |
|---|---|---|---|---|
| 16:50:20 | `/proc/meminfo` in §0.3's block | 267,472 kB | — | — |
| 16:50:20 | `I host`, its first read, deciding | `268,447,744` | `10,025,005,056` | `150,369,520`; `7,400,000,000` |
| 20:32:03 | the resume read, `logs/10-branch.log` (§6 item 1) | 193,480 kB = `198,123,520` | `9,473,675,264` | the same, recorded, not asserted |
| 20:36:27 | §3.7, `free -b` (`available`) and `df` | `237,191,168` | `9,469,190,144` | printed |
| 20:49:28 | §9, `df` after B-RECLAIM-OWN | — | `9,459,564,544` | printed |

### 2.12 Every file the run wrote, by SHA-256

But the bot's own root `/var/lib/adv3-bot/` — `check-done`, written by the kill mark, then by the unit — and the render's
scratch `render-state/`, never hashed into the report. `sha256sum` at 20:48:29 UTC, before `keep`:

```
d7134aff086e2af8663797ea4098ad1c8f89f23599fe1f713d37101b9e721945  /root/tz42-work/logs/00-work-tree.log
5c9de399842b1d2942abf31401af0760ce357ed2f65041845818024a20ccc493  /root/tz42-work/logs/01-stage.log
95278b6bb47c4d946afde47292cf05fba8dff8a716d1712a5ec98e7d64244215  /root/tz42-work/logs/02-fingerprint.log
2d5289fac54f7d3ebbc9be2b87155ff8bc43fcda86d28cffd4b41f245ce45648  /root/tz42-work/logs/03-host.log
a28df37920f8ec42ae8f2ea594956cb625ed18c4ed98ef43fe115909792eaf39  /root/tz42-work/logs/04-refs.log
8f9678e56ec343ddfafe25087bff47b20fc8644577074bef9fa64e949f19578f  /root/tz42-work/logs/10-branch.log
8a717c2f1f23ad7cc6ab00247f5b55d1047f8ad86eda5baf7b4050c242d5e324  /root/tz42-work/logs/11-selftests.log
14cc85ac2b1d1e32985a5c5e60b1901ba5e6544666eb8199def0c74b9ab4a33f  /root/tz42-work/logs/12-reclaim-scratch.log
f90a6283a7c64d066124dd97a31980aab36cad441eaed7ea96e6d9156962f524  /root/tz42-work/logs/20-b-deploy.log
1bb2c9f192cce1608547db0eb7af27e6d45ee734a4883e19e8df864afc047e3f  /root/tz42-work/logs/21-copy.log
a528c101d06893a43bd20e4643af5f883d8fb787b5acc3adcdfc4bfdac7bfcd0  /root/tz42-work/logs/22-render.log
5d01d71f06fdd72ccd4b2fd500b78092ef667faabf80cc89871e94fe3d70e951  /root/tz42-work/logs/23-probe.log
b727d6e7269d770376c609b5d54090ea05edf433d45444cd5da23ac2d3ff086f  /root/tz42-work/logs/24-b-kill.log
b8d01e4e109a7e369f886eb7d707d07795aa196ca7d59a74b0ecd767ae7435af  /root/tz42-work/logs/25-unit-new.log
01a75dba59427e77d0481cb85086cae6c18255b0d832183a14fd5c93b0bf17e3  /root/tz42-work/logs/26-first.log
eb904493e1fdb78bb9fda56358d3800f69274a3775a3292d3f3f4387e40614cc  /root/tz42-work/logs/27-closing.log
6667d60a71b8c0bcd96724ecd6a7248044cc19b6f4167a6c985e950b925d1039  /root/tz42-work/logs/28-separation.log
466a71163ed70475819065f3eb9b38150caf1d812ff7ca722ed9f6ff84f3e1b7  /root/tz42-work/state.json
9e622daf2e8a5ec3e93f15c7f56e7cf859547fbd3771daad75bc6532adb2b9d1  /root/tz42-work/bot.before
edb771eeadad8377cc03283d2b0300b81a4d0b06e0c3ec91ad7ba216107b9b3c  /root/tz42-work/commit.before
c3d9fff54f3585cfc4c33b5f7e1f93b390e62b03e0b4725fee2d6fdda6d04c11  /root/tz42-work/stage/advisor/adv3-bot.py
b6c45490b2f86f5c4678c645041ef1556b1199a6bc814470de904aedf7f5105f  /root/tz42-work/stage/research/tz42-advisor-registry.py
c3d9fff54f3585cfc4c33b5f7e1f93b390e62b03e0b4725fee2d6fdda6d04c11  /root/tz42-work/wt/advisor/adv3-bot.py
b6c45490b2f86f5c4678c645041ef1556b1199a6bc814470de904aedf7f5105f  /root/tz42-work/wt/research/tz42-advisor-registry.py
c3d9fff54f3585cfc4c33b5f7e1f93b390e62b03e0b4725fee2d6fdda6d04c11  /root/adv3-bot-svc/adv3-bot.py
137d4472099988aa28d35013585da36dd9acd1b2c6f8289bf58d0c4b6a4d0ab0  /root/adv3-bot-svc/commit.txt
```

---

## 3. Publication

| item | value |
|---|---|
| branch | `tz-42-advisor-registry`, pushed with `git push -u origin tz-42-advisor-registry` (no credential refused), head `4e6db2d16dda3da14957120d636f537dfc0bcc87`, one commit over `origin/main` `4ac4169` |
| commit | `4e6db2d` — `advisor/adv3-bot.py` modified, `research/tz42-advisor-registry.py` added, 3,991 insertions and 1,224 deletions by `git show --stat` |
| pull request | #41, https://github.com/seahomebatumi-ai/btc-5m-twap/pull/41, against `main`, open, not merged |
| Release | none: this TZ publishes no dataset and no asset |
| report | `CryptoReports/TZ-42-advisor-registry-report.md`, straight to `main`, committed after B-RECLAIM-OWN |

**V13 — contract §4.2's self-check**, `logs/28-separation.log` verbatim, run after the push and the pull request and before
the report's commit:

```
2026-11-05T20:37:15.565340704Z
fetch exit=0
0
advisor/adv3-bot.py
research/tz42-advisor-registry.py
grep exit=1
{"baseRefName":"main","headRefOid":"4e6db2d16dda3da14957120d636f537dfc0bcc87","mergedAt":null,"number":41,"state":"OPEN"}
```

The first line after `fetch exit=0` is `0`: the implementation commit is not on `main`. The diff names the two
implementation files only. `grep` for `.parquet` and `.zip` on `main` printed nothing (`exit=1`).

---

## 4. Gate

| gate | TZ's PASS | read | deciding number | verdict |
|---|---|---|---|---|
| G-RULE | 8 of 8 | `READING RULE: PASS - 8 of 8` | 8 / 8 = `1.000` | **PASS** |
| SELFTESTS | 57 of 57, 135 of 135, 102 of 102 | as required | `1.000`, `1.000`, `1.000` | **PASS** |
| COPY | 5 of 5 | `READING COPY: PASS - 5 of 5` | `1.000` | **PASS** |
| G-RENDER | 34 of 34 | `READING RENDER: PASS - 34 of 34` | `1.000` | **PASS** |
| P-START | `READING P-START: served - 6 of 6 endpoints, 8 requests` | the same line | 6 / 6 = `1.000` | **PASS** |
| UNIT-NEW | 9 of 9 | `READING UNIT-NEW: PASS - 9 of 9` | `1.000` | **PASS** |
| G-FIRST | 10 of 10 | `READING FIRST: PASS - 10 of 10` | `1.000` | **PASS** |

The TZ's own words: "Family-wise false failure `0`: every gate reads its quantity directly and none samples. A FAIL
before B-DEPLOY is BLOCKED and deploys nothing; a FAIL of COPY, G-RENDER, P-START, B-KILL's mark or signal, UNIT-NEW or
G-FIRST is B-ROLLBACK (§4.4)." No gate failed; nothing was tuned; no gate was reinterpreted. **What a PASS establishes
and what it does not is the TZ's §4.5**, unchanged: the registry describes the model's walk on Binance's candles and
measures nothing; that the 00:10 and 15:07 checks fire on their own clock under this code is the next TZ's host gate's to
read.

---

## 5. Validation

### V1 — fingerprint
`READING FINGERPRINT: PASS - 69 of 69` — revision 1, anchors 6, re-derived 4, frozen rows 57 of 57, the table's shape
1 (60 rows: 57 frozen, 2 tracked, 1 reported). Asserted, exit `0`.

### V2 — host gate
`READING HOST: PASS - 23 of 23`; the slots and delays, the journal's size and span, the memory figure of the first read
(no second), §2.1. Asserted.

### V3 — NUMBER
`READING NUMBER: PASS - 2 of 2` at §0.5 and at §3.1, the `TZ-42-` path printed at each; the branch count `0`. Asserted.

### V4 — files
2 of 2 hashes asserted at §0.1 and at §3.1, lines and bytes printed; the diff exactly `M`, `A`; `--numstat` exactly
`1903 1224` and `2088 0`. The hashes asserted by the extraction script; the diff's shape compared by the Executor against
the TZ's text — **recorded, not asserted** by a script, as the TZ's §3.1 writes it.

### V5 — self-tests
`SELFTEST-ADV3 PASS: 57 of 57 checks passed`, `SELFTEST PASS: 135 of 135 checks passed`, `SELFTEST PASS: 102 of 102
checks passed`. Asserted by each script, exit `0`.

### V6 — G-RULE
`READING RULE: PASS - 8 of 8`. Asserted.

### V7 — B-DEPLOY
`exit=0`; the mark printed: `mark deploy at 2026-11-05T20:34:15Z: bot pid 3851184 NRestarts 4, 11 check records, journal
28 lines 6083fd15d499…, registry none, check-done 2026-11-05 fact`. Each step chained by `&&`.

### V8 — COPY
`READING COPY: PASS - 5 of 5`. Asserted.

### V9 — G-RENDER
`READING RENDER: PASS - 34 of 34`; the counts of §2.6; `PEAK 72593408 bytes resident; 28.59 s of wall, 4.01 s of
processor`. Asserted; inside `timeout 900`.

### V10 — P-START
`READING P-START: served - 6 of 6 endpoints, 8 requests`, each of its five lines printed (§2.7). Asserted by the bot's
`probe`, exit `0`.

### V11 — B-KILL and UNIT-NEW
`exit=0`; the mark with `check-done` `2026-11-05 fact` before and `2026-11-04 fact` after; `READING UNIT-NEW: PASS - 9 of
9`; pids `3851184` and `284419`; the mark at 20:35:20.598 UTC and the new process's start at 20:35:50 UTC. Asserted.

### V12 — G-FIRST
`READING FIRST: PASS - 10 of 10`; the counts of §2.8. Asserted.

### V13 — contract §4.2's self-check
§3, run at 20:37:15 UTC after the push (20:32) and the pull request (20:32:36) and before the report's commit.

### V14 — closing reads
Every read of §3.7 printed, §2.10.

### V15 — B-RECLAIM-SCRATCH and `keep`
B-RECLAIM-SCRATCH: 0 files considered in TZ-40's two directories, 0 named by a report, 0 copied, 0 held, the store
`2,370` → `2,370` (`RECLAIM PASS`, the Boss's run). `keep`: 20 files considered and kept, 20 copied, 0 held, the store
`2,370` → `2,390` — after equal to before plus the copies, asserted by `keep` (`KEEP PASS`) and read by `find … | wc -l`,
`2390`.

### V16 — §9's removals
`git worktree remove /root/tz42-work/wt` without `--force` `exit=0`; `test -e` `exit=1` for `/root/tz42-work`, and for
`981b3989…` and `e19b6910…` in the Boss's log and in the Executor's read; `git worktree list` names `/root/btc-5m-twap`
and `/root/btc-recorder-svc` and nothing else.

### V17 — every block refused and every paste the Boss ran
One block refused: B-RECLAIM-SCRATCH's `reclaim`, 20:33 UTC, "Permission for this action was denied by the Claude
Code auto mode classifier. Reason: The server-side auto mode classifier judged this action dangerous (it gave no
explanation)." The paste, §3.3's one line with `981b3989…` and `e19b6910…` written in, handed to the Boss at about
20:34 UTC and again at 20:40 UTC; he ran it at 20:47:45 UTC. Every line it appended is quoted in §2.9. No other block
was refused; P-BOSS-A and P-BOSS-B were not handed over.

### V18 — a rollback
None ran: no gate failed, so B-ROLLBACK, B-KILL2, UNIT-OLD, K-42, STOPPED and B-ASIDE were not run, as §4.4 says under
PASS.

---

## 6. What could not be implemented as written

1. **The session was interrupted for 3 h 41 min.** Between §3.1's `git diff --cached --numstat` (16:50:44 UTC) and the
   commit (20:32:13 UTC) the Boss's usage limit stopped the session; on its reset he asked it to continue. Nothing ran
   in between. On resuming the Executor read the time, the work tree, the branch (not yet pushed), the unit (`3851184`,
   `NRestarts` `4`), `check-done` (`2026-11-05 fact`) and the record (no registry), and appended to `logs/10-branch.log`
   one read of `MemAvailable` (`198,123,520`), the free space (`9,473,675,264`), the unit, `check-done` and the staged
   diff again — the same `M`, `A`, `1903 1224` and `2088 0`. **The host gate was not run again**: its reads stand at
   16:50:20 UTC, 3 h 44 min before B-DEPLOY; the resume read is recorded, not asserted, and both floors held at it; H8's
   window and registry were asserted again by the `deploy` and `kill` marks. The band of B-DEPLOY, 15:20:00 to
   23:20:00 UTC, was open throughout.
2. **The remote-control directory of 2026-10-30, `238335b9-cf23-414a-8e8f-ad4705c4d19e`, was left untouched although
   `scratch` named it earlier.** Its process no longer runs: the remote-control `claude` restarted on 2026-11-01 at
   19:07:55 UTC (pids `3859143` to `3859205`, the directories `1757478d…` and `3fffc996…`, both live). §3.3's rule reclaims
   every directory `scratch` names earlier, and the same paragraph says "the live session of 2026-10-30 is not touched";
   map §3 calls it "live and no TZ's". `reclaim` copies only the files a report names by hash, so removing it would have
   destroyed the rest of a directory no TZ made. The Executor reclaimed the two TZ-40 directories §0.3 and map §3 name,
   `981b3989…` and `e19b6910…`, and left `238335b9…` for the Architect to decide.
3. **B-RECLAIM-SCRATCH's `reclaim` was refused by the classifier** (20:33 UTC, "The server-side auto mode classifier
   judged this action dangerous (it gave no explanation)") and handed to the Boss as §3.3's one line, with the two
   directories written in; §2.9 and V17. Nothing of §3.4 to §3.6 waited for it.
4. **Logs' names for steps the TZ does not name:** `00-work-tree.log` (§0.0, written after the `mkdir`, whose output
   could not go into a directory that did not yet exist), `01-stage.log` (§0.1), `02-fingerprint.log` (§0.2),
   `03-host.log` (§0.3), `04-refs.log` (§0.5), `10-branch.log` (§3.1, the commit, push and pull request among it),
   `11-selftests.log` (§3.2), `12-reclaim-scratch.log` (§3.3: `scratch`'s listing first, then the Boss's line, appended),
   `27-closing.log` (§3.7) and `28-separation.log` (V13). The TZ's own names — `20-b-deploy.log` to `26-first.log` —
   were used as written.
5. **One helper file in the work tree:** `/root/tz42-work/fp-table.md`, §0.1's table rows built from
   `logs/02-fingerprint.log` by a substitution and pasted into this report, removed before `keep`; no gate read it.
   The harness kept its own copy of one background command's output — the 45 s wait and the UNIT-NEW and G-FIRST polls,
   whose terminal output was `polls ended` — under this session's own directory, which no step of the session can
   remove (map §6, harness).
6. **Appendix A's code and the map were read in part.** The Executor read the TZ's §0 to §10 in full and the parts of
   Appendix A the run needed (`serve`'s `setMyCommands`); the two files were taken as the TZ sent them, by §0.1's
   SHA-256 asserts, and exercised by their self-tests and the gates, not read line by line. Of the map the Executor read
   §0 with its table, §2.7, §3's paragraph on the directories and §6's rows host identity, disk, process supervision,
   memory, both sandbox limits and the harness; `fingerprint` read the whole map mechanically. Contract §1 step 2 asks for
   both in full.
7. **The day held no new STRONG signal to take**, a case the TZ foresaw (§4.3, §4.5): one coin was STRONG at every rank, none
   was named not taken and none opened, so G-RENDER read 34 of 34 with the model opening no signal, and
   the replayed check opened none; the new views on live data rest on the four legacy signals the seed opened. That a
   new signal is written, sized and announced on a live day is established by the self-test's synthetic market alone.
8. **`setMyCommands`:** the new code logs only a refusal, and none stands; whether Telegram shows the menu is not
   established, and P-START's `getMyCommands`, read before the restart, returned 0.
9. **A terminal escape sequence at the head of the Boss's log lines:** his shell wrote `ESC ] 133 ; C BEL` (shell
   integration) before the first `date -u` of his line in `logs/12-reclaim-scratch.log`; the report shows it as
   `\x1b]133;C\x07`. The log's bytes are kept as they are in the forensic store by `keep`.
