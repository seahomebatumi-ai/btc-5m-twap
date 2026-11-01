# TZ-40 report — STRONG at every rank: the list's TOP-N and every STRONG beyond it, the allocation's first N and every other STRONG that passes its limits, each sized alone, the checks' candidates — and Telegram's pace for the longer messages

**NUMBER PASS: 2 of 2** at §0.5 (17:53:05 UTC) and again at §3.1 (17:53:11 UTC): `CryptoTZ/` holds `TZ-40-strong-every-rank.md` and no other `TZ-40-` file, `CryptoReports/` no `TZ-40-` report; the branch count `0` before the push.
**G-RULE PASS: 10 of 10** — `adv3.py`: `assessment`, `card_lines`, `message` changed, none added or removed, the 46 others identical by AST, `PIT` changed and equal to TZ-38's report cell for cell, `BEYOND` and `BEYOND_TAG` added; `adv3-bot.py`: 14 changed, 5 added, none removed, the 43 others identical (`plan` among them), `CARD_KEYS` and `HELP` changed, `PACE` added; `RULE-ADV-3.txt` and the unit `main`'s byte for byte · **SELFTESTS: 57 of 57, 128 of 128, 86 of 86.**
**B-DEPLOY `exit=0`** (mark 18:05:23 UTC) · **COPY PASS: 5 of 5** · **G-RENDER PASS: 22 of 22** on live data — **STRONG at every rank 2** (in each of the two allocations), **none beyond the TOP-3**; trades placed and more per allocation **2 and 0, 2 and 0**; the signal check quiet, full, alerts **stop 0, signal 0, candidate 0**, cards 3, extra 0; the fact check quiet, one line, alerts **0, 0, 0**, cards 0, extra 0; **PEAK `65,425,408` bytes resident**, 29.55 s wall, 3.87 s processor · **P-START: served - 5 of 5 endpoints**.
**B-KILL `exit=0`** (mark 18:05:56 UTC), `check-done` **`2026-11-01 fact` → `2026-10-31 fact`** · **UNIT-NEW PASS: 9 of 9** — pid `3766156` → `3851184`, started 18:06:26 UTC, `NRestarts` 3 → 4, the three capture units unchanged · **G-FIRST PASS: 7 of 7** — the replayed `2026-11-01 signal` of the close of 2026-10-31, **quiet, full, 1 message**, alerts **stop 0, signal 0, candidate 0**, 11 followed trades, cards 3, extra 0, 2 coins pass, STRONG at every rank 2, sent 18:06:36 UTC; `check-done` `2026-11-01 fact`.
**No rollback ran**: B-ROLLBACK, B-KILL2, UNIT-OLD, K-40 and `stopped` were not run; no gate failed.
**The unit runs the new code**: `adv3-bot.service` `active`, `enabled`, pid `3851184`, the service copy's `adv3.py` `81ef0112…` and `adv3-bot.py` `9e622daf…`, `commit.txt` `433ce139eedc112862ecf678cda6eaa2577d73d3` — verified by `I copy`, `I unit new` and `I first` inside the Boss's paste (18:05:24 – 18:06:42 UTC) and by the Executor's own §3.7 closing reads (18:30:40 UTC: `systemctl show`, `is-enabled`, `journalctl`, `service.log`).
**Two of the session's commands were refused by Claude Code's auto mode classifier, each before it ran, and handed to the Boss unchanged:** B-RECLAIM-SCRATCH's `reclaim` ("[Irreversible Local Destruction]", 17:54 UTC), run by the Boss at 18:11:55 UTC — `RECLAIM PASS`, 6 files considered, none copied, both directories removed, `test -e` `exit=1` each; and B-DEPLOY ("[Production Deploy]", 17:54 UTC), handed over as **P-BOSS-A** at about 17:55 UTC inside its band and run by the Boss 18:05:23 – 18:06:42 UTC. No checker mode was run again after the paste (map §7 item 144).
**Departures, all in §6:** the two refused blocks; the logs' names for steps whose name the TZ does not fix; a terminal escape sequence at the head of the Boss's reclaim log; one file written and removed unrun in the work tree; a day with no STRONG beyond the TOP-3.

| field | value |
|---|---|
| TZ | `CryptoTZ/TZ-40-strong-every-rank.md`, 4,973 lines, 410,093 bytes, SHA-256 `9658275c48116baf283eb06b63c6d320b4c12d5bf836e4b06e69068dd6b12869`, landed at `16a94cb` (2026-11-01 17:49:34 UTC), above `f2a3ed6` (revision `2026-11-01-a`) and `f212cd4` (PR #39's merge) |
| map revision | `2026-11-01-a`, equal; anchors 6 of 6; re-derived 4 of 4; rows 59; `frozen` equal 56 of 56; the map 2,018 lines, 520,651 bytes, SHA-256 `2b113897e3221073c073c95b64e9141a98d1227a9559912e382652772d062763`, the file TZ-40 §10 names |
| executor model | the model the TZ header names: `get_session` read `configured_model`, `session_context.model` and `external_metadata.last_served_model` all `claude-opus-5-5` |
| branch | `tz-40-strong-every-rank` at `433ce139eedc112862ecf678cda6eaa2577d73d3`, on `origin/main` `16a94cb`; pushed; pull request #40, open, not merged |
| service's code | `/root/adv3-bot-svc/`: `adv3.py` `81ef0112…` (was `c19572dc…`), `adv3-bot.py` `9e622daf…` (was `ca989b6f…`), `commit.txt` `433ce139eedc…` (was `fc687582ebc4…`) |
| unit | `/etc/systemd/system/adv3-bot.service` `82acd8e4…`, unchanged; never reloaded |
| interpreter | `/root/tz04a-env/venv/bin/python` 3.12; every session mode under `nice -n 19` and `-B` |
| marks | `deploy` 18:05:23.974 UTC · `kill` 18:05:56.862 UTC (`state.json`, `t` `1793556323.9736345` and `1793556356.861997`) |
| blocks | B-RECLAIM-SCRATCH: refused to the Executor 17:54 UTC; run by the Boss 18:11:55 UTC · B-DEPLOY: refused to the Executor 17:54 UTC; P-BOSS-A handed over about 17:55 UTC, run by the Boss 18:05:23 – 18:06:42 UTC · B-RECLAIM-OWN: §2.9 |
| work tree | `/root/tz40-work/`, created 17:52 UTC, removed by B-RECLAIM-OWN (§2.9) |

---

## 0. Fingerprint

`I fingerprint`, from the staged copy of the checker, against the primary checkout at `16a94cb` — revision
`2026-11-01-a`; anchors `A1` `229a944f2d51`, `A2` `6c5089330629`, `A3` `0-complete / 1-student-5tau-not-disqualified /
2-no-edge-4tau-240-undecidable`, `A4` `437b45ea196b`, `A5` `0f6c90451cbd`, `A6` `729f0bcdbee3`, each equal to the TZ
header's; `A2`, `A4`, `A5` and `A6` re-derived. **V1: `READING FINGERPRINT: PASS - 68 of 68`** (17:52:53 UTC). The map,
the `reported` row: 2,018 lines, 520,651 bytes, SHA-256 `2b113897e3221073c073c95b64e9141a98d1227a9559912e382652772d062763`.

### 0.1 The 59 rows of the map's §0 table

Built from `logs/02-fingerprint.log` by a substitution; "equal" stands for each of the 56 `ok   frozen <path>` lines the
checker asserted against the map's lines, bytes and SHA-256. The advisor rows are TZ-39's hashes, as the TZ says they
stay until its verdict.

| path | lines | bytes | state | SHA-256 | against the map |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 2,018 | 520,651 | reported | `2b113897e3221073c073c95b64e9141a98d1227a9559912e382652772d062763` | printed |
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
| `advisor/adv3.py` | 871 | 49,378 | frozen | `c19572dccf30a505342ca334e42c7ec347a5d29db4db20887229d2a8c7b48e31` | equal |
| `advisor/adv3-bot.py` | 1,558 | 99,958 | frozen | `ca989b6fe487d41181b32312418d6acda1e9c64fbf5cfbb3f041d54826dd108f` | equal |
| `advisor/selftest-adv3.py` | 235 | 16,470 | frozen | `09d2ba9a8361ec5ebc7f5934ebb818d1a685bb16fb3f32b7da94409d9516cc0e` | equal |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | printed |

---

## 1. Input

**Re-collected: nothing.** No dataset was read or written. What was read:

| input | size | hash / reading |
|---|---|---|
| `CryptoTZ/TZ-40-strong-every-rank.md` | 4,973 lines, 410,093 bytes | `9658275c…12869`; Appendix A extracted twice by §0.1's script, verbatim |
| `SYSTEM-MAP.md` | 2,018 lines, 520,651 bytes | `2b113897…62763` |
| the map's 58 other rows | §0.1 | 56 `frozen` equal, 2 `tracked`, 1 `reported` |
| `advisor/RULE-ADV-3.txt`, `deploy/systemd/adv3-bot.service`, `CryptoReports/TZ-38-adv3-pit-validation-report.md` at `origin/main` | — | read by `I rule`: `ee206e7c…`, `82acd8e4…`, `f4a0ac3f…` |
| `/var/lib/adv3-bot/journal.jsonl` | 32,149 bytes at §0.3; 43,367 at §3.7 | read by `host`, the marks, `unit`, `first`, and copied once into `render-state/` by `render`; never printed |
| `/var/lib/adv3-bot/check-done` | 15 bytes | `2026-11-01 fact` at §0.3 and both marks; `2026-10-31 fact` written by the kill mark; `2026-11-01 fact` at §3.7, written by the new process |
| Binance's public futures market | live | G-RENDER through the service copy's `Data`, `live_report`, `liquidity` and `forming_candles`; P-START's five endpoints |
| Telegram | live | P-START's `getMe` alone; G-RENDER's Telegram is a stand-in |

---

## 2. Measurements

### 2.1 Host gate (§0.3), 17:52:58 UTC — V2

```
date -u: Sun Nov  1 05:52:58 PM UTC 2026   (1793555578)   uptime -s: 2026-08-02 07:24:32
nproc 1; MemTotal 978640 kB; MemAvailable 219452 kB; SwapTotal 3174396 kB; SwapFree 2326124 kB
check records: 2; slots 2026-11-01 s 2026-11-01 f; delays after their instants, seconds: 0; check-done 2026-11-01 fact
units: adv3-bot active/running/enabled pid 3766156 NRestarts 3; btc-pairbook pid 3738426 NRestarts 16;
       btc-recorder pid 2388318 NRestarts 0; btc-rewardbook pid 3137952 NRestarts 1 — each active, enabled
MemAvailable first 223096832 bytes, second not read, deciding 223096832; /dev/vda2 free 10310459392 bytes
ok H1 · ok H2 ×2 · ok H3 · ok H4 ×3 · ok H5 ×6 · ok H6 · ok H7 ×3 · ok memory gate · ok disk gate
READING HOST: PASS - 19 of 19
```

H7: the check records from TZ-39's first, `2026-11-01 signal`, are two — the signal check (TZ-39's replay at 06:51:46
UTC) and the `2026-11-01 fact` check its own clock fired at 12:10:06 UTC, delay `0` s; no gap. **Memory**: `223,096,832`
bytes against the floor `140,037,206`, the first read deciding. **Disk**: `10,310,459,392` bytes free against
`7,400,000,000`. Printed without threshold: timers — apt-daily 20:37:06, rewardbook-archive 2026-11-02 01:30:20,
pairbook-archive 03:00:20, apt-daily-upgrade 06:55:02 UTC; both archive services `inactive`/`dead`, `Result=success`;
`du -sb`: `/var/lib/btc-rewardbook` 675,679,953, `/var/lib/btc-pairbook` 774,043,159, `/var/lib/adv3-bot` 37,231,
`/root/.claude` 16; the forensic store **2,344** files (map §3's count); worktrees **2**, `/root/btc-5m-twap` and
`/root/btc-recorder-svc`; the scratch parent holds `0f8f6761…`, `238335b9…`, `981b3989…` (this session), `a2827336…`
and `e19b6910…`.

### 2.2 Refs (§0.5) — V3

`git fetch origin` exit 0; `ls-remote origin` 103 lines, `HEAD` and `refs/heads/main` `16a94cb92f57e9785e1838d9f7a66cb9c3524d76`,
branches `tz-23` to `tz-39`, `refs/pull/1` to `39`, the pairbook and rewardbook stream tags and `tz-01a-dataset`,
`tz-27-pairbook-streams` — every line in `logs/04-refs-number.log`. Branch count `0`. `origin/main`'s first-parent log:
`16a94cb` (TZ-40 uploaded), `f2a3ed6` (map `2026-11-01-a`), `f212cd4` (PR #39's merge), `283c367` (TZ-39's report),
`dd65a7e` (TZ-39 uploaded). The difference from map §1 is `16a94cb` alone, this TZ's upload; `main` carries
`2026-11-01-a`.

### 2.3 Files (§0.1, §3.1) — V4

| path | lines | bytes | SHA-256 | stage | worktree |
|---|---|---|---|---|---|
| `advisor/adv3-bot.py` | 1,869 | 126,909 | `9e622daf2e8a5ec3e93f15c7f56e7cf859547fbd3771daad75bc6532adb2b9d1` | `xb` | over TZ-39's `ca989b6f…` |
| `advisor/adv3.py` | 895 | 51,834 | `81ef0112d3fe4b86566e51a51aab924d9776ff37a927e65982ecb0bb7c1f34e1` | `xb` | over TZ-39's `c19572dc…` |
| `advisor/selftest-adv3.py` | 256 | 19,111 | `6f29b82f2b2ca82cd2ff4bbb370e032354dbb4743497330530777429b3af7398` | `xb` | over TZ-39's `09d2ba9a…` |
| `research/tz40-advisor-strong.py` | 1,436 | 95,474 | `4403b27185f7e9aaa090dedfca457af6c4f70b6b020f0d2fcd9f9fbb96b6054b` | `xb` | `xb` |

4 of 4 hashes asserted at each extraction (17:52:49 and 17:53:28 UTC), both `exit=0`. `git diff --cached --name-status`:
`M advisor/adv3-bot.py`, `M advisor/adv3.py`, `M advisor/selftest-adv3.py`, `A research/tz40-advisor-strong.py`;
`--numstat`: `439 128 advisor/adv3-bot.py`, `35 11 advisor/adv3.py`, `21 0 advisor/selftest-adv3.py`,
`1436 0 research/tz40-advisor-strong.py` — exactly the TZ's.

### 2.4 Self-tests and G-RULE (§3.2) — V5, V6

```
SELFTEST-ADV3 PASS: 57 of 57 checks passed
SELFTEST PASS: 128 of 128 checks passed
SELFTEST PASS: 86 of 86 checks passed
ok   RULE-ADV-3.txt is main's, byte for byte, hashes to the RULE constant, and is the branch's adv3.py's
ok   the unit file is main's, byte for byte, and hashes to TZ-35's
ok   adv3.py: the definitions changed are exactly ['assessment', 'card_lines', 'message'], added [], removed []
ok   adv3.py: the 46 others identical by AST, the 17 this checker names among them
ok   adv3.py: the assignments changed are exactly ['PIT'], added ['BEYOND', 'BEYOND_TAG'], removed []
ok   adv3.py's PIT is TZ-38's report as committed (f4a0ac3f…), cell for cell
ok   adv3-bot.py: the definitions changed are exactly ['Telegram', 'alerts_of', 'candidate_lines', 'candidates', 'check', 'check_record', 'compose', 'event_lines', 'handle', 'item_lines', 'offers', 'plan_parts', 'selftest', 'top_n'], added ['TooMany', 'alloc_fields', 'plan_strong', 'strong_all', 'volumes'], removed []
ok   adv3-bot.py: the 43 others identical by AST, the 11 this checker names among them
ok   adv3-bot.py: the assignments changed are exactly ['CARD_KEYS', 'HELP'], added ['PACE'], removed []
ok   the branch's adv3.py, adv3-bot.py and selftest-adv3.py are Appendix A's
READING RULE: PASS - 10 of 10
```

Each `exit=0`, 17:53:55 – 17:53:57 UTC; the self-tests reached no network.

### 2.5 B-DEPLOY and COPY (§3.4, in P-BOSS-A) — V7, V8

```
2026-11-01T18:05:23.916548650Z
mark deploy at 2026-11-01T18:05:23Z: bot pid 3766156 NRestarts 3, 2 check records, check-done 2026-11-01 fact
exit=0
2026-11-01T18:05:24.045184486Z
ok   the service copy holds adv3.py, adv3-bot.py and commit.txt only
ok   adv3.py is Appendix A's
ok   adv3-bot.py is Appendix A's
ok   commit.txt is the branch head and the worktree's HEAD
ok   the branch's two files equal the service copy's
READING COPY: PASS - 5 of 5
exit=0
```

### 2.6 G-RENDER (§3.4, in P-BOSS-A) — V9

`logs/22-render.log`, 18:05:24 – 18:05:53 UTC, verbatim but for its 22 `ok` lines, which §5 lists:

```
replies: 2021 chars in 1 parts, 3853 chars in 1 parts, 2004 chars in 1 parts, 2017 chars in 1 parts, 2769 chars in 1 parts, 1143 chars in 1 parts, 1143 chars in 1 parts; the bot's log: 8 lines; STRONG at every rank: 2, 2; per allocation, placed and more: 2 and 0, 2 and 0
signal check: quiet, full, 1 parts; alerts {"candidate": 0, "signal": 0, "stop": 0}; offers read 16, followed 15; cards 3, of them extra 0; passing 2; STRONG at every rank 2; zones left 0; forming candles read 0
fact check: quiet, one line, 1 parts; alerts {"candidate": 0, "signal": 0, "stop": 0}; offers read 16, followed 15; cards 0, of them extra 0; passing 2; STRONG at every rank 2; zones left 0; forming candles read 7
PEAK 65425408 bytes resident; 29.55 s of wall, 3.87 s of processor
READING RENDER: PASS - 22 of 22
exit=0
```

The seven replies in order: «сигнал», «сигнал топ 7», «сигнал 10000 топ 3», «сигнал 15000 топ 5», «оценка», «помощь»,
«привет». **The close of 2026-10-31 holds 2 coins STRONG at every rank, both within the TOP-3**, so no card was extra
and no allocation had a «more»: the day read 22 of 22 with no extra card, the case §4.3 names, and the new views rest
on the self-tests' synthetic market of twelve STRONG (§4.5). **Peak** `65,425,408` bytes: under the TZ's modelled
`70,018,603` and the floor's half; `1.120` times the Architect's largest Python 3.13.18 figure, `58,396,672`, and
`1.115` times the largest 3.12.3 figure, `58,667,008` [computed: the ratios of the printed figures]. 29.55 s of wall
against the `timeout` of 900; 3.87 s of processor against 30.

### 2.7 P-START (§3.5, in P-BOSS-A) — V10

```
2026-11-01T18:05:53.735418981Z
P-KLINES served: 1499 closed daily candles of BTCUSDT, the last 2026-10-31 - and the candle forming since 2026-11-01
P-FUNDING served: 6 settlement days of BTCUSDT since 2026-10-27
P-MARKS served: 945 perpetuals, all 42 coins among them with a mark price
P-INTERVALS served: 820 perpetuals with an adjusted funding interval, 42 of the coins among them
P-TELEGRAM served: bot @ClaudeCryptoSignal_bot
READING P-START: served - 5 of 5 endpoints
exit=0
```

### 2.8 B-KILL, UNIT-NEW and G-FIRST (§3.5, in P-BOSS-A) — V11, V12

```
2026-11-01T18:05:56.810430946Z
mark kill at 2026-11-01T18:05:56Z: bot pid 3766156 NRestarts 3, 2 check records, check-done 2026-11-01 fact -> 2026-10-31 fact, replayed by the new process at its start
exit=0
2026-11-01T18:06:41.905026411Z
bot: pid 3851184 NRestarts 4 started 2026-11-01T18:06:26Z; captures: {"btc-pairbook.service": ["3738426", "16"], "btc-recorder.service": ["2388318", "0"], "btc-rewardbook.service": ["3137952", "1"]}
ok   the unit is active, running and enabled
ok   a new MainPID, one restart more
ok   the process started after the kill mark and within 90 s of it
ok   the process runs the unit's exact argv, alone
ok   the service copy's adv3.py and adv3-bot.py are the new ones, and the process started after the copy
ok   the unit file is unchanged
ok   the log shows the new process serving from check-done 2026-10-31 fact
ok   no traceback in the log since the mark
ok   the three capture units unchanged, each active
READING UNIT-NEW: PASS - 9 of 9
exit=0
2026-11-01T18:06:42.001990318Z
first check: quiet, full, 1 messages; alerts {"candidate": 0, "signal": 0, "stop": 0}; followed 11; cards 3, of them extra 0; passing 2; STRONG at every rank 2; check-done 2026-11-01 fact
ok   exactly one check record since the mark
ok   it is the day's signal check, of the close of the day before, under rule ee206e7c
ok   it was sent: its Telegram message ids
ok   it holds the 42 coins' state, the six ratings, its alerts, the coins that pass, the STRONG at every rank and the more, each card its extra; quiet exactly without an alert
ok   check-done names the slot it covers: 2026-11-01 fact
ok   the log since the mark: the new process serving from check-done 2026-10-31 fact, the check sent, no check failed and no traceback
ok   the journal ends in a newline and every line since the mark parses
READING FIRST: PASS - 7 of 7
exit=0
```

Both pids: `3766156` (old) → `3851184` (new); instants: kill mark 18:05:56.862, SIGTERM 18:05:56, restart 18:06:27 UTC
(systemd's `RestartSec=30`), the new process's start 18:06:26 UTC by `/proc`, the replayed check sent 18:06:36 UTC.
UNIT-NEW and G-FIRST each read PASS on the first run, neither printed `NOT YET`. The replay was **quiet**: it held no alert of any kind, and G-FIRST asserts it quiet exactly where it holds
none. It ended after 12:10 UTC and marked the day's fact slot done (`done_after`), `check-done` `2026-11-01 fact`.

### 2.9 B-RECLAIM-SCRATCH (§3.3) and B-RECLAIM-OWN (§9) — V15, V16

`scratch` (17:54:01 UTC): `0f8f6761-2295-466b-9178-9b8a0261193e` born 06:20:19 UTC **earlier**;
`238335b9-cf23-414a-8e8f-ad4705c4d19e` **live** (processes 3435609, 3435619, 3435628, 3435667, the remote-control
session of 2026-10-30); `a2827336-da6d-511b-b699-35cb76f477de` born 06:20:20 UTC **earlier**;
`e19b6910-2c25-4765-98b9-49d2a819677e` born 17:52:02 UTC **live** (process 3848490). The two earlier are map §3's two
of TZ-39's session. The Boss's run, `logs/12-reclaim-scratch.log`, every line:

```
<ESC>]133;C<BEL>2026-11-01T18:11:55.330728630Z
reclaim: 3642 report tokens; forensic store holds 2344 files
RECLAIM PASS: 6 files considered, 0 named by a report, 0 kept by name, 0 copied, 0 already held; forensic store 2344 -> 2344 files
exit=0
2026-11-01T18:11:55.547401920Z
exit=0
exit=1
exit=0
exit=1
```

Each `rm -rf` `exit=0` and each `test -e` `exit=1`: both directories are gone. The live ones were not touched.

B-RECLAIM-OWN, from the session, every line as printed, written to no file:

```
$ nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz40-work/stage/research/tz40-advisor-strong.py keep
K copied c19572dccf30a505342ca334e42c7ec347a5d29db4db20887229d2a8c7b48e31 /root/btc-forensics/tz40-work--adv3.before
K copied ca989b6fe487d41181b32312418d6acda1e9c64fbf5cfbb3f041d54826dd108f /root/btc-forensics/tz40-work--bot.before
K copied 0b963fc3c42dbd3952a8e0337d6433bdba655c9dce11a105ab4a6f38c55592db /root/btc-forensics/tz40-work--commit.before
K copied 00f3efee702ff8f9f01de72b5860d06285427501b111f15a90a320528b8bbbeb /root/btc-forensics/tz40-work--logs--00-work-tree.log
K copied 5e2e77be5547e420c748ea752a893f4e853e769ad697ecee1e27bb707b9667d5 /root/btc-forensics/tz40-work--logs--01-stage.log
K copied 185ad8bf488b37555a1bcd528c53c9387698bf3db9cfa05b70c8cb4f94ec2499 /root/btc-forensics/tz40-work--logs--02-fingerprint.log
K copied e185ed78956af7994057cabe3bc2f401a612b95d9749782db604ec2e4e4e914a /root/btc-forensics/tz40-work--logs--03-host.log
K copied 1d35c9e3eaabbae61baf741f005462a34d73b40b2ffe21f23fe2d146c051ccee /root/btc-forensics/tz40-work--logs--04-refs-number.log
K copied 005492056f4a8b5240b0bd34a16cc9a5eb4e40ed16a510e48031940ba3dd1db1 /root/btc-forensics/tz40-work--logs--10-branch.log
K copied 0821006f78095a5fc25210992e2f895755f1d9ff1edf2c9e586c06ce9af0603a /root/btc-forensics/tz40-work--logs--11a-selftest-adv3.log
K copied 61cf02e482181d9fabc024cdabd7e3f711f4bad814d830b0d34605c0a17b5a4c /root/btc-forensics/tz40-work--logs--11b-selftest-bot.log
K copied 32417bd60b018d75ce0c22ed8274ba6eb77747da5fa4af8ca21f3a3eab6ea1ab /root/btc-forensics/tz40-work--logs--11c-selftest-checker.log
K copied e3b46469a5f73d885407630066b3565c0899c9fecf801a19f8adca351166106d /root/btc-forensics/tz40-work--logs--11d-rule.log
K copied fe87c66b522b82925611e622ae03042f487ab27af603a765ffc14352bb939474 /root/btc-forensics/tz40-work--logs--12-reclaim-scratch.log
K copied 19e56f56d1e9424f5db7f00befda6b10ffd43553d0a38d5fc30a660b986955ee /root/btc-forensics/tz40-work--logs--12a-scratch.log
K copied 80f3902bac1dc246718e803e4951da13243db8a70c7ffefe2550d759e7f4f2ea /root/btc-forensics/tz40-work--logs--12b-reclaim-refused.log
K copied 554cc09cd0f26821f62bbf5b8866bd419a988ee2a15d177c11cd66dc36492855 /root/btc-forensics/tz40-work--logs--20-b-deploy.log
K copied 462376c0eba69bcd9ef5bb6c9deab36e573f00004a60801ab67a505a91322ccc /root/btc-forensics/tz40-work--logs--20a-b-deploy-refused.log
K copied 8f009cf179f7c6aef3911baa151a4277abeca8ab436c78596f7b4513dfc3473a /root/btc-forensics/tz40-work--logs--21-copy.log
K copied c2413b6fb80f81a9b8fddd436b3f2ac830d87a1e768378e3f023f178db6fbdfd /root/btc-forensics/tz40-work--logs--22-render.log
K copied e311248b445cd2b2972b28bf83a4d15842af2b7dd42c3716aaa66120bf86e766 /root/btc-forensics/tz40-work--logs--23-probe.log
K copied 847fba7d1b2d9bb8f8733ed0731a76c59acd222119b2ec02f6e17eb1fff60f02 /root/btc-forensics/tz40-work--logs--24-b-kill.log
K copied 329ba6d6645462b5340adc12d1a9ade83a8ad5ee9dad6ecf38deb7fa44e2ca64 /root/btc-forensics/tz40-work--logs--25-unit-new.log
K copied cfea7a85f7a516ece49e09e4cb0c39f6b136e4e157a101332a86bc01a8f1e8a7 /root/btc-forensics/tz40-work--logs--26-first.log
K copied 7a267b254a7fbe17f12db66c1333a09aa75f02e1bfc47148fd12159f076094fa /root/btc-forensics/tz40-work--logs--40-closing-reads.log
K copied 55e71d398ea652422550da6390fa9bc6f0a9d46e2577406d3cd916617a5a4e16 /root/btc-forensics/tz40-work--state.json
KEEP PASS: 26 files kept, 26 copied, 0 already held; forensic store 2344 -> 2370 files; worktree at 433ce139eedc112862ecf678cda6eaa2577d73d3, its upstream's
$ git -C /root/btc-5m-twap worktree remove /root/tz40-work/wt; echo "exit=$?"
exit=0
$ rm -rf /root/tz40-work; echo "exit=$?"
exit=0
$ test -e /root/tz40-work; echo "exit=$?"
exit=1
$ git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
/root/btc-5m-twap       16a94cb [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
$ find /root/btc-forensics -type f | wc -l
2370
$ df -B1 --output=source,size,avail /var/lib/btc-recorder
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10239823872
```

### 2.10 Closing reads (§3.7), 18:30:40 UTC — V14

`logs/40-closing-reads.log`, 206 lines. `systemctl show`:

| unit | MainPID | NRestarts | ActiveState | Result | Nice | MemoryCurrent | MemoryPeak | ActiveEnterTimestamp |
|---|---|---|---|---|---|---|---|---|
| adv3-bot | 3851184 | 4 | active | success | 10 | 6,094,848 | 48,095,232 | 2026-11-01 18:06:27 UTC |
| btc-recorder | 2388318 | 0 | active | success | 0 | 61,739,008 | 321,794,048 | 2026-10-23 06:08:56 UTC |
| btc-pairbook | 3738426 | 16 | active | success | 0 | 16,633,856 | 43,880,448 | 2026-11-01 03:06:45 UTC |
| btc-rewardbook | 3137952 | 1 | active | success | 10 | 23,642,112 | 78,729,216 | 2026-10-28 12:56:29 UTC |
| btc-pairbook-archive | 0 | 0 | inactive | success | 19 | not set | not set | — |
| btc-rewardbook-archive | 0 | 0 | inactive | success | 19 | not set | not set | — |

Timers: rewardbook-archive next 2026-11-02 01:30:20, last 2026-11-01 01:30:20; pairbook-archive next 03:00:20, last
03:00:20 UTC — unmoved. `systemctl is-enabled adv3-bot.service`: `enabled`, `exit=0`. The unit's journal, its last five lines:

```
2026-11-01T18:05:56+00:00 vultr systemd[1]: adv3-bot.service: Sent signal SIGTERM to main process 3766156 (python) on client request.
2026-11-01T18:05:56+00:00 vultr systemd[1]: adv3-bot.service: Deactivated successfully.
2026-11-01T18:05:56+00:00 vultr systemd[1]: adv3-bot.service: Consumed 4.102s CPU time, 43.6M memory peak, 40.1M memory swap peak.
2026-11-01T18:06:27+00:00 vultr systemd[1]: adv3-bot.service: Scheduled restart job, restart counter is at 4.
2026-11-01T18:06:27+00:00 vultr systemd[1]: Started adv3-bot.service - ADV-3 advisor, the Boss's Binance Futures signals over Telegram.
```

(the 15 lines before them are the unit's earlier signals and restarts, of 2026-10-31 08:36:43 and 13:58:13 and 2026-11-01 06:51:10 UTC).
`service.log`, its lines since the mark:

```
2026-11-01T18:06:27Z serving the pinned chat: pid 3851184 offset 685120817 check-done 2026-10-31 fact
2026-11-01T18:06:33Z candles refreshed to the close of 2026-10-31 | missing -
2026-11-01T18:06:36Z check sent: 2026-11-01 signal for the close of 2026-10-31 | alerts 0 | quiet | full
2026-11-01T18:13:27Z request answered for the close of 2026-10-31 | kind alloc
```

The 18:13:27 line is an allocation the new process answered to a request from the pinned chat after the paste; no step
of this TZ sent it. The `tail -n 30` also shows, above 2026-10-31T06:00:05Z, the end of an earlier `TimeoutError`
traceback in `ssl.py` — before both marks, the one UNIT-NEW and G-FIRST exclude by reading since the mark.
`ls -la`: `/root/adv3-bot-svc` `adv3-bot.py` 126,909, `adv3.py` 51,834, `commit.txt` 41, all 18:05;
`/var/lib/adv3-bot` `check-done` 15 (18:06), `daily-sent` 10, `journal.jsonl` 43,367, `offset` 9, `service.log` 5,412.
`check-done`: `2026-11-01 fact`. `free -b`: available `201,670,656`; `df`: `/dev/vda2` 31,612,203,008, available
`10,229,239,808`. `du -sb`: `/root/tz40-work` 13,229,430, `/root/adv3-bot-svc` 178,784, `/var/lib/adv3-bot` 48,813,
`/var/lib/btc-rewardbook` 697,758,461, `/var/lib/btc-pairbook` 809,279,299, `/root/.claude` 16. `state.json` as in §2.11.

The next scheduled check, the first the running unit's clock fires under this code, is the 00:10 UTC signal check of
2026-11-02 (the restart came after 11:50); the next TZ's host gate reads it (H7).

### 2.11 Memory and free space, each read

| instant (UTC) | read | value | bound |
|---|---|---|---|
| 17:52:58 | `MemAvailable`, `I host` first read (deciding) | 223,096,832 | ≥ 140,037,206 |
| 17:52:58 | `/dev/vda2` free, `I host` | 10,310,459,392 | ≥ 7,400,000,000 |
| 18:05:53 | G-RENDER's peak resident set | 65,425,408 | modelled 70,018,603 |
| 18:30:40 | `free -b` available | 201,670,656 | printed |
| 18:30:40 | `df` available | 10,229,239,808 | printed |
| after B-RECLAIM-OWN | `df` available (§2.9) | 10,239,823,872 | printed |

`state.json` (the marks' snapshots): `deploy` — bot `active` pid 3766156 `NRestarts` 3, the three capture units as in
§2.1, `check_done` `2026-11-01 fact`, 2 checks, 11 lines, `t` 1793556323.97; `kill` — the same, `read_done`
`2026-10-31 fact`, `t` 1793556356.86.

### 2.12 Every file the run wrote, by SHA-256

The work tree's files at 18:30 UTC, before `keep` (the bot's own root and `render-state/journal.jsonl`, 60,459 bytes,
excluded as §8 says):

| file | lines | bytes | SHA-256 |
|---|---|---|---|
| `logs/00-work-tree.log` | 3 | 125 | `00f3efee702ff8f9f01de72b5860d06285427501b111f15a90a320528b8bbbeb` |
| `logs/01-stage.log` | 6 | 522 | `5e2e77be5547e420c748ea752a893f4e853e769ad697ecee1e27bb707b9667d5` |
| `logs/02-fingerprint.log` | 130 | 10,498 | `185ad8bf488b37555a1bcd528c53c9387698bf3db9cfa05b70c8cb4f94ec2499` |
| `logs/03-host.log` | 82 | 4,465 | `e185ed78956af7994057cabe3bc2f401a612b95d9749782db604ec2e4e4e914a` |
| `logs/04-refs-number.log` | 129 | 8,483 | `1d35c9e3eaabbae61baf741f005462a34d73b40b2ffe21f23fe2d146c051ccee` |
| `logs/10-branch.log` | 41 | 1,860 | `005492056f4a8b5240b0bd34a16cc9a5eb4e40ed16a510e48031940ba3dd1db1` |
| `logs/11a-selftest-adv3.log` | 3 | 81 | `0821006f78095a5fc25210992e2f895755f1d9ff1edf2c9e586c06ce9af0603a` |
| `logs/11b-selftest-bot.log` | 3 | 78 | `61cf02e482181d9fabc024cdabd7e3f711f4bad814d830b0d34605c0a17b5a4c` |
| `logs/11c-selftest-checker.log` | 3 | 76 | `32417bd60b018d75ce0c22ed8274ba6eb77747da5fa4af8ca21f3a3eab6ea1ab` |
| `logs/11d-rule.log` | 13 | 1,204 | `e3b46469a5f73d885407630066b3565c0899c9fecf801a19f8adca351166106d` |
| `logs/12a-scratch.log` | 12 | 991 | `19e56f56d1e9424f5db7f00befda6b10ffd43553d0a38d5fc30a660b986955ee` |
| `logs/12b-reclaim-refused.log` | 3 | 405 | `80f3902bac1dc246718e803e4951da13243db8a70c7ffefe2550d759e7f4f2ea` |
| `logs/12-reclaim-scratch.log` | 9 | 297 | `fe87c66b522b82925611e622ae03042f487ab27af603a765ffc14352bb939474` |
| `logs/20a-b-deploy-refused.log` | 4 | 469 | `462376c0eba69bcd9ef5bb6c9deab36e573f00004a60801ab67a505a91322ccc` |
| `logs/20-b-deploy.log` | 3 | 148 | `554cc09cd0f26821f62bbf5b8866bd419a988ee2a15d177c11cd66dc36492855` |
| `logs/21-copy.log` | 8 | 309 | `8f009cf179f7c6aef3911baa151a4277abeca8ab436c78596f7b4513dfc3473a` |
| `logs/22-render.log` | 29 | 3,904 | `c2413b6fb80f81a9b8fddd436b3f2ac830d87a1e768378e3f023f178db6fbdfd` |
| `logs/23-probe.log` | 8 | 480 | `e311248b445cd2b2972b28bf83a4d15842af2b7dd42c3716aaa66120bf86e766` |
| `logs/24-b-kill.log` | 3 | 207 | `847fba7d1b2d9bb8f8733ed0731a76c59acd222119b2ec02f6e17eb1fff60f02` |
| `logs/25-unit-new.log` | 13 | 777 | `329ba6d6645462b5340adc12d1a9ade83a8ad5ee9dad6ecf38deb7fa44e2ca64` |
| `logs/26-first.log` | 11 | 871 | `cfea7a85f7a516ece49e09e4cb0c39f6b136e4e157a101332a86bc01a8f1e8a7` |
| `logs/40-closing-reads.log` | 206 | 8,261 | `7a267b254a7fbe17f12db66c1333a09aa75f02e1bfc47148fd12159f076094fa` |
| `state.json` | 61 | 1,204 | `55e71d398ea652422550da6390fa9bc6f0a9d46e2577406d3cd916617a5a4e16` |
| `adv3.before` | 871 | 49,378 | `c19572dccf30a505342ca334e42c7ec347a5d29db4db20887229d2a8c7b48e31` |
| `bot.before` | 1,558 | 99,958 | `ca989b6fe487d41181b32312418d6acda1e9c64fbf5cfbb3f041d54826dd108f` |
| `commit.before` | 1 | 41 | `0b963fc3c42dbd3952a8e0337d6433bdba655c9dce11a105ab4a6f38c55592db` |

The stage's and the worktree's four files are §2.3's. Outside the tree: the service copy's three (§2.5, `commit.txt`
`433ce139…` and a newline), `check-done` (the kill mark's `2026-10-31 fact`, since rewritten by the unit), and the
forensic store's copies (§2.9).

---

## 3. Publication

| item | value |
|---|---|
| branch | `tz-40-strong-every-rank`, pushed between 17:53:28 and 17:53:47 UTC with `git push -u origin tz-40-strong-every-rank`, no credential helper needed |
| implementation commit | `433ce139eedc112862ecf678cda6eaa2577d73d3`, parent `16a94cb`, four files |
| pull request | #40, https://github.com/seahomebatumi-ai/btc-5m-twap/pull/40, open, head `433ce139…`, not merged |
| Release | none — this TZ produces no dataset and no asset |
| report | `CryptoReports/TZ-40-strong-every-rank-report.md`, straight to `main` |

Contract §4.2's self-check, run at 18:31 UTC after the push and the pull request and before the report's commit — V13:

```
$ git rev-list origin/main | grep -c 433ce139eedc112862ecf678cda6eaa2577d73d3
0
$ git diff --name-only origin/main origin/tz-40-strong-every-rank
advisor/adv3-bot.py
advisor/adv3.py
advisor/selftest-adv3.py
research/tz40-advisor-strong.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
$
```

---

## 4. Gate

The TZ's gates (§4), each quoted and read:

| gate | PASS condition | read | verdict |
|---|---|---|---|
| G-RULE | 10 of 10 | 10 of 10 | **PASS** |
| SELFTESTS | 57 of 57, 128 of 128 and 86 of 86 | 57, 128, 86 | **PASS** |
| COPY | 5 of 5 | 5 of 5 | **PASS** |
| G-RENDER | 22 of 22 | 22 of 22 | **PASS** |
| P-START | `READING P-START: served - 5 of 5 endpoints` | as quoted | **PASS** |
| UNIT-NEW | 9 of 9 | 9 of 9 | **PASS** |
| G-FIRST | 7 of 7 | 7 of 7 | **PASS** |

The deciding fractions: `1.000` at every gate. Nothing was tuned and no gate reinterpreted. Under PASS neither
B-ROLLBACK nor K-40 was run. What a PASS does not establish is TZ-40 §4.5's list, unchanged — among it that a day with
STRONG beyond the TOP-3 was among G-RENDER's: it was not (§2.6).

---

## 5. Validation

Every reading below is an `assert` or an explicit non-zero exit of the script that prints it; counts are the scripts'.

- **V1 FINGERPRINT** — `68 of 68`, asserted; 59 rows, 56 of 56 `frozen` equal.
- **V2 HOST** — `19 of 19`, asserted; the memory gate decided by the first read, 223,096,832.
- **V3 NUMBER** — `2 of 2` at §0.5 and `2 of 2` at §3.1, asserted; the path `CryptoTZ/TZ-40-strong-every-rank.md` printed both times; branch count `0`.
- **V4 files** — 4 of 4 hashes at each extraction, asserted by §0.1's script; `--name-status` and `--numstat` exactly the TZ's, read against it by the Executor (recorded, compared by eye, not asserted by a script).
- **V5 SELFTESTS** — `57 of 57`, `128 of 128`, `86 of 86`, asserted.
- **V6 G-RULE** — `10 of 10`, asserted (§2.4).
- **V7 B-DEPLOY** — `exit=0`; the mark printed (§2.5).
- **V8 COPY** — `5 of 5`, asserted.
- **V9 G-RENDER** — `22 of 22`, asserted, each:
  1. every command and both checks answered, no traceback and no failed request in the bot's log;
  2. the markup balanced in every part (b, i);
  3. «сигнал»: TOP-3 ranked k of 3, every STRONG beyond them extra, ★ and «вне ТОП-3» exactly where they belong, basis, invalidation, confidence, no methodology;
  4. «сигнал топ 7»: the same at seven;
  5. «оценка»: rung, next readings, six ratings, forward record, STRONG beyond the TOP-3 not the measured strategy, `+0,51 R` against `+0,80`;
  6. the bot's constants this TZ's;
  7. each allocation reply the bot's own `plan_parts` of `plan_strong`, recomputed;
  8. the placed the first n STRONG at any rank that pass, the more the rest, in rank order;
  9. every STRONG coin placed, more or named with a reason, once;
  10. every trade an entry and a stop within 14 %;
  11. each placed loss within 1 %, all within 5 %, each more within the average risk;
  12. whole positions of at least 5 USDT, the placed within the budget, free the budget less them;
  13. leverage, margin, liquidity cap;
  14. the Boss's fields in each allocation reply, the more under their heading with the loss together, no six ratings;
  15. «сигнал 15000 топ 5» at most five, nothing of three;
  16. «помощь» and an unknown text answer `HELP` alone;
  17. the signal check's quiet condition and sections;
  18. the fact check's quiet condition and its single line;
  19. the alerts the exits of the offered trades by the checker's own walk, each once, and the new candidates;
  20. the check records' fields;
  21. the scratch journal's kinds `request, request, alloc, alloc, assess, check, check`;
  22. the bot's own journal, offset, daily-sent and check-done as before the run.

  Printed counts in §2.6; `PEAK 65425408 bytes resident; 29.55 s of wall, 3.87 s of processor`.
- **V10 P-START** — `served - 5 of 5 endpoints`, each reply asserted served and parsed; every line in §2.7.
- **V11 B-KILL and UNIT-NEW** — `exit=0`; the mark with `check-done` `2026-11-01 fact` → `2026-10-31 fact`; `9 of 9`, asserted; pids `3766156` → `3851184`; instants 18:05:56 (mark) and 18:06:26 (start).
- **V12 G-FIRST** — `7 of 7`, asserted; counts in §2.8.
- **V13 separation self-check** — §3, `0`, the four implementation files, nothing.
- **V14 closing reads** — §2.10, every read in `logs/40-closing-reads.log`.
- **V15 B-RECLAIM-SCRATCH and `keep`** — `RECLAIM PASS`, 6 files considered, 0 copied, 0 held, the store 2,344 → 2,344; `KEEP PASS`, 26 files kept, 26 copied, 0 already held, the store 2,344 → 2,370 = 2,344 + 26.
- **V16 removals** — §2.9: `git worktree remove` without `--force`, `git worktree remove` without `--force` `exit=0`; `test -e /root/tz40-work` `exit=1`, and of both scratch directories `exit=1` (the Boss's run); `git worktree list` naming `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else.
- **V17 refused blocks and the Boss's pastes** — §6 items 1 and 2.

---

## 6. What could not be implemented as written

1. **B-RECLAIM-SCRATCH was refused to the Executor.** At 17:54 UTC the `reclaim` of the two earlier directories, the
   Executor's own block, was refused by Claude Code's auto mode classifier before it ran: "Permission for this action
   was denied by the Claude Code auto mode classifier. Reason: [Irreversible Local Destruction]." Nothing ran:
   `12-reclaim-scratch.log` did not exist, both directories stood with their 06:20 birth times, the forensic store
   held no `tz40` file (`logs/12b-reclaim-refused.log`). It was handed to the Boss as §3.3's one line with both full
   paths written in, and he ran it at 18:11:55 UTC; every line it appended is quoted in §2.9. It held back nothing of
   §3.4 to §3.6.
2. **B-DEPLOY was refused to the Executor.** At 17:54 UTC, inside its band (12:20:00 – 23:20:00 UTC), the §3.4 block
   was refused before it ran: "Permission for this action was denied by the Claude Code auto mode classifier. Reason:
   [Production Deploy]." Nothing ran: `20-b-deploy.log` and `state.json` did not exist, no `.before` file existed and
   the service copy's three files kept their mtimes of 06:50:51 UTC (`logs/20a-b-deploy-refused.log`). **P-BOSS-A**,
   §3.6's text unchanged, was handed to the Boss at about 17:55 UTC, its band open; he ran it from 18:05:23 to
   18:06:42 UTC, its waits for the bands returning at once. Every log line it appended is quoted in §2.5 to §2.8.
   While it ran the Executor ran nothing reading the service copy, the unit or its record; after it, no checker mode was
   run again, and every outcome above is read from its logs and from §3.7's reads, not from the Boss's account (he
   wrote «готово»). B-KILL was therefore never tried by the Executor itself: P-BOSS-A ran it.
3. **Logs' names.** The TZ fixes `12-reclaim-scratch.log`, `20-b-deploy.log` to `26-first.log` and `30` to `34`. For
   the other steps the Executor chose: `00-work-tree`, `01-stage`, `02-fingerprint`, `03-host`, `04-refs-number`,
   `10-branch` (§3.1, the second NUMBER, the worktree, the extraction, the diff, the commit, the push and the pull
   request), `11a` to `11d` (§3.2's four), `12a-scratch`, `12b-reclaim-refused`, `20a-b-deploy-refused` and
   `40-closing-reads` (§3.7).
4. **A terminal escape in the Boss's log.** `12-reclaim-scratch.log` begins with the seven bytes `ESC ] 1 3 3 ; C BEL`
   before its first `date -u` line: a shell-integration mark of the Boss's terminal, written by his shell and not by
   the block. `keep` copies the file as it is; no gate reads it.
5. **One working file written and removed unrun.** Between 17:53:12 and 17:53:28 UTC, before the §3.1 extraction, the Executor wrote
   `/root/tz40-work/extract-wt.sh` (42 lines, §0.1's script cut from the TZ with its argument changed) and removed it
   unrun; the extraction over the worktree was then run inline from the session, verbatim but for its argument, as §3.1
   says. No other file was written outside §2.12's list.
6. **A day with no STRONG beyond the TOP-3.** The close of 2026-10-31 held 2 coins STRONG at every rank, both within the
   TOP-3: G-RENDER and the replayed check showed no extra card and no allocation had a «more». This is the case §4.3
   and §4.5 name, not a departure; the new views on live data are proved only where they are empty.
7. **The commit's author** is the host's git default, `root <root@vultr.guest>`, as TZ-39's was; the TZ names none.

Nothing else.
