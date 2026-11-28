# TZ-56a — K0, its second run: the favourite held to settlement, Kalshi and Polymarket — REPORT

**Status: EXECUTED. K0: Kalshi EARN, Polymarket UNDECIDABLE.** Every gate passed: FINGERPRINT, NUMBER, SELFTEST 67 of
67, G-PROBE 9 of 9, G-REHEARSAL 12 of 12, G-FRAME, G-SET 5,000 members on each venue, DETERMINISM 4 of 4 and the second
runs of `score` and `pack` byte for byte, G-UPLOAD 13 of 13, G-DOWNLOAD 13 of 13, G-TAG, G-STILL. Through §1's
decisions, **EARN on Kalshi alone takes the K track to K1.**

- Executor model: Claude Opus 5.5, the model the TZ names.
- Branch `tz-56a-k0-favourite` at `bf391748e2f975a579a4abf15b3bffc067799937`, pull request #55, open and not merged.
  TZ-56's pull request #54 closed unmerged, its branch `tz-56-k0-favourite` kept.
- Release `tz-56a-k0-inputs`, a lightweight tag at `bf391748e2f975a579a4abf15b3bffc067799937`, 13 assets,
  `343,337,168` bytes, verified anonymously.
- The host: the capture host (H1, H2). The work tree `/root/tz56a-work`, reclaimed by §9.
- Files named by SHA-256 (§8 of the TZ): `state.json` `3d5161e27a05b8b0315c9ddb68ae789b4361e32ee36fe6fc6f4cfa3908ffc2d7`,
  `release-set.json` `685ac340aa66a1cfb33a8d21fa40cfb5e92dbe8476c44d4f340cbce2fa2f74dc`, `verify.json`
  `89a08cc798f3e8947bef5c6ed539536f11d8e0b10fa98b251effee55e1d28f5d`, `run/score.json`
  `ae7e8ee6871060752b4540ed324db935c811ef2870a8a3a2f25a2de21656171e`, `read-ledger.jsonl`
  `4aedcf998e3949985762088a232da940fba6d7e47e3d75627543062f8f6f2a40`, `release-notes.md`
  `7345e8a23259b5a5bf4e739946ef27f517c67c4eb7d503101c594d880fcbe583`, `rehearsal/instrument.json` and
  `rehearsal/reference.json`, the same bytes, `53fd84736c50a36493438afe90c20042b04283b3548146d7e82f716d10e3d444`.

## 0. Fingerprint

`I0 fingerprint` (`logs/02-fingerprint.log`), contract §1 steps 3 and 4 asserted inside the instrument:

```
FINGERPRINT PASS: revision 2026-11-28-a; anchors 6 of 6, 4 re-derived; rows 74: frozen 71 of 71 equal, tracked 2, reported 1
```

Revision string read: `2026-11-28-a`. Anchors read from map §0, equal to the TZ header's six:

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

The map's §0 table, every row as `fingerprint` printed it: lines, bytes and SHA-256 of the file in the primary
checkout at `9cdf5f3`. There are 74 rows: 71 `frozen` equal, 2 `tracked`, 1 `reported`.

| path | lines | bytes | SHA-256 | state |
|---|---|---|---|---|
| `SYSTEM-MAP.md` | 1,112 | 214,292 | `f83377ed50d12b5fd924c46a87aaf58c5f144c4dd82dca915fecf0cd5eedcfc5` | reported |
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

The map itself: `SYSTEM-MAP.md 1112 lines 214292 bytes sha256 f83377ed50d12b5fd924c46a87aaf58c5f144c4dd82dca915fecf0cd5eedcfc5`.

**Staging (§0.1, `logs/01-stage.log`)**, the TZ's script verbatim, `exit=0`:

```
/root/tz56a-work/stage/reference/tz56a-k0-reference.py 416 17645 9de780a0f5744d5cceb3074c0373020cda15dd4a7ac8bee288c13f9ab7a91f6c
/root/tz56a-work/stage/research/tz56-k0-favourite.py 2269 116543 7241a14afe5bde0bdeed37fb17bb9a45d59cc88e83ac319789eebedc07b335db
```

**§0.0:** `mkdir /root/tz56a-work /root/tz56a-work/logs; echo "exit=$?"` printed `exit=0`.

**Host gate (§0.3, `logs/03-host-gate.log`), 23:03:01 UTC on 2026-11-27, epoch `1795820581`:**

| gate | read | threshold | result |
|---|---|---|---|
| H1 | `/var/lib/btc-recorder/btc-updown-5m/1794396600/manifest.json`, one path | exactly one | PASS |
| H2 | `/dev/vda2`, size `31612203008`; `grep -c` of `e3975b5…` `5` | `/dev/vda2`, `31612203008`, at least 1 | PASS |
| H3 | `3.12.3` | `3.12.` | PASS |
| H4 | `gh auth status` logins `1` | at least 1 | PASS |
| memory | `MemAvailable: 210820 kB` = `215,879,680` bytes | at least `157,499,106` | PASS |
| disk | `avail` `10,005,319,680` | at least `8,700,000,000` | PASS |

Printed, no threshold: one processor; `MemTotal 978640 kB`, `SwapTotal 3174396 kB`, `SwapFree 2587432 kB`; boot
`2026-08-02 07:24:32`. The units: the recorder pid `3525462`, the reward book `3525511`, the advisor `3525469`, the
liquidation guard `3525503`, each `active`, `NRestarts=0`, `enabled`, active since 06:26:20–22 UTC on 2026-11-27; the
reward book's archive's service `inactive` (`static`), its timer `active` since 2026-11-17 16:05:49 UTC.
`telemetry-watch.service`: `disabled`, `exit=1`. `du -sb`: the reward book's store `505,155,915`, the forensic store
`397,273,552` at `2,876` files; the reward book's stream files, the `find`'s sum, `35,037,033`. **The margin:**
`10,005,319,680 + 35,037,033 − 7,300,000,000 − 445,535,636 = 2,294,821,077` bytes. Worktrees: the primary checkout at
`9cdf5f3 [main]` and `/root/btc-recorder-svc` at `e3975b5`. The listing beside the session's directory held 17 UUID
directories (§3.3 names them).

**NUMBER (§0.5, `logs/05-number.log`):**

```
origin/main 9cdf5f3b516a49e91857a77a2ec4e168ccd4362a: 133 paths under CryptoTZ/ and CryptoReports/; of the number TZ-56a-: ['CryptoTZ/TZ-56a-k0-favourite.md'] and []
NUMBER PASS - 2 of 2
```

**Refs (`logs/05-refs.log`), 23:03 UTC:** 266 lines — `HEAD` 1, heads 31, pull 54, tags 180. Lines that differ from map
§1's read (265 lines, 179 tags, `HEAD` and `main` at `bd1eb900…`): `HEAD` and `refs/heads/main` at
`9cdf5f3b516a49e91857a77a2ec4e168ccd4362a` (the TZ's upload, above `8c88575`, the map's revision `2026-11-28-a`), and one
tag more, the newest `refs/tags/rewardbook-streams-1795818620` at `6a615257…`. No `refs/heads/tz-56a-k0-favourite`, no
`refs/tags/tz-56a-k0-inputs`; `main` carries revision `2026-11-28-a`. PASS.

## 1. Input

Nothing was read from any earlier run; every venue reply was collected by this run from the three venue hosts,
anonymously, through `Net.get`, and kept before use. Nothing was re-collected: each mode ran once, no resume was needed
(`0 replayed` in every live mode's lines).

| set | requests | kept file | bytes | SHA-256 |
|---|---|---|---|---|
| rehearsal, Kalshi frame, 2026-11-12 | 103 | `rehearsal/raw-frame-kalshi.jsonl.gz` | 6,151,553 | `c74d2d5215e8f8b9996f6dffcb8057899af6a2a1af7ad3369809912fca68881e` |
| rehearsal, Kalshi draws | 252 | `rehearsal/raw-draw-kalshi.jsonl.gz` | 2,079,840 | `6895cb492d49b9d29f1b051fba9a30002e2fa9244b1b431686043f2ac4205c81` |
| rehearsal, Polymarket frame | 288 | `rehearsal/raw-frame-polymarket.jsonl.gz` | 14,471,928 | `95d407f189e455ee8eca16ef3050e71c9707820f362c2a5ffce1f1bc2362acc1` |
| rehearsal, Polymarket draws | 170 | `rehearsal/raw-draw-polymarket.jsonl.gz` | 1,671,289 | `7410e604888a360c1af6668bb073b298f1bc404ae53a977bd4770fc765460081` |
| Kalshi frame, 2026-11-16..21 | 693 | `run/raw-frame-kalshi.jsonl.gz` | 41,042,366 | `bed859a687e6b94a85449e70cf80a60b1211be3af2951853d20b26ea9a671389` |
| Kalshi draws | 10,886 | `run/raw-draw-kalshi.jsonl.gz` | 108,392,880 | `ae5317f2fd44a59731afa17fe90d33abfef35885378d344e2414b02a26871560` |
| Polymarket frame, 2026-11-16..21 | 1,881 | `run/raw-frame-polymarket.jsonl.gz` | 91,082,077 | `ca123195f4a27821adbf445064ab1f1fd5b1dee99f1323608190a26468444602` |
| Polymarket draws | 8,956 | `run/raw-draw-polymarket.jsonl.gz` | 57,035,038 | `b005ddd4c30682d6ef46a85392202c37c76bcf8ac5a00e4551c8fef9dd33a04c` |

Plus `probe`'s 9 requests (§2.1). Every byte above is in the Release (§3). Files built from them:

| file | bytes | SHA-256 |
|---|---|---|
| `run/frame-kalshi.jsonl` | 28,502,063 | `c2e97ad87b0c88434145d4c74d34259c8da209a2185b4d03c565dc19f7a200c8` |
| `run/frame-polymarket.jsonl` | 52,172,472 | `158200993b78b61405f46ff8473c0f9c350c04e6a741ba1d784614dc01d25320` |
| `run/draws-kalshi.jsonl` | 2,319,152 | `96943fd7ec919a01d2b3babe91f84e1ab8f08807d273c257908cdbeba3eb3812` |
| `run/draws-polymarket.jsonl` | 5,437,574 | `6723e6215af2eec7eb8b7db666249a92a48e6d25dacd16191fb38ba912a68fe8` |
| `run/score.json` | 4,329 | `ae7e8ee6871060752b4540ed324db935c811ef2870a8a3a2f25a2de21656171e` |

**The read ledger** (`read-ledger.jsonl`, `4aedcf99…2f40`), each line the mode, its instant, the file's SHA-256
`7241a14a…35db` and `HEAD` `bf391748…9937`: `rehearse` 23:04:36Z, `frame` 23:07:40Z, `draw` 23:14:53Z (all 2026-11-27),
`redraw` 00:22:35Z, `score` 00:25:51Z and 00:25:54Z, `pack` 00:26:02Z and 00:26:05Z (2026-11-28). **The labels of the
set were read twice, by `score` alone.**

**Map §7 item 63:** §3.1's push reached `origin` by **23:03:51 UTC on 2026-11-27** (`logs/31-branch.log`, the `date -u`
after `push exit=0`); `score`'s first run, the first label read of the set, at **00:25:51 UTC on 2026-11-28**.

## 2. Measurements

### 2.1 G-PROBE (`logs/34-probe.log`)

```
MemAvailable 279146496 bytes, floor 157499106; free 9983430656 bytes, gate 8700000000
headers of every venue request: {"Accept": "application/json", "Accept-Encoding": "gzip", "User-Agent": "btc-5m-twap-tz56"}
kalshi exchange    GET https://api.elections.kalshi.com/trade-api/v2/exchange/status -> 200, 667 bytes, sha256 9c900e19dad1f05812a0c3c40c19253e5962c839b1739481aef3d20244c4f778, keys ['exchange_active', 'exchange_index_statuses', 'intra_exchange_transfers_active', 'trading_active']
kalshi cutoff      GET https://api.elections.kalshi.com/trade-api/v2/historical/cutoff -> 200, 188 bytes, sha256 61d3453d5919a44413b09d8739f4392372109d122232086cde0cf027799e25f2, keys ['market_positions_last_updated_ts', 'market_settled_ts', 'orders_updated_ts', 'trades_created_ts']
kalshi historical cutoff: {"market_positions_last_updated_ts": "2026-09-28T00:00:00Z", "market_settled_ts": "2026-09-28T00:00:00Z", "orders_updated_ts": "2026-11-13T00:00:00Z", "trades_created_ts": "2026-09-28T00:00:00Z"}
kalshi markets     GET https://api.elections.kalshi.com/trade-api/v2/markets?limit=1000&min_close_ts=1794438000&max_close_ts=1794531600&mve_filter=exclude -> 200, 1997939 bytes, sha256 7d6a4445fe867089c185bc1601f61fe8cdecf18858a814443524a2cf866d955e, keys ['cursor', 'markets']
kalshi trades      GET https://api.elections.kalshi.com/trade-api/v2/markets/trades?ticker=KXZEC15M-26NOV121900-00&limit=5 -> 200, 1565 bytes, sha256 f45adfe989b20d0267f4e3fd7a1e547ba1d6c132fd519833f61ca99915ad1bb4, keys ['cursor', 'trades']
kalshi series      GET https://api.elections.kalshi.com/trade-api/v2/series/KXBTCD -> 200, 1178 bytes, sha256 ab961b0bbf53c0223b3ff240f0df1a046057781417ddaa7d42f8c874ec5ba61c, keys ['series']
kalshi series fees GET https://api.elections.kalshi.com/trade-api/v2/series/fee_changes?show_historical=true -> 200, 17840 bytes, sha256 c13cb76fbcfcfcb14ae6d43c7e8841e89404062b22fc1c2f09b6bab300c8c598, keys ['series_fee_change_arr']
kalshi event fees  GET https://api.elections.kalshi.com/trade-api/v2/events/fee_changes?limit=1000 -> 200, 36 bytes, sha256 4d755a11d76cd85bec7a4758a2d226815fd2a935a5563dbafae35ee9d373da45, keys ['cursor', 'event_fee_changes']
gamma keyset       GET https://gamma-api.polymarket.com/markets/keyset?limit=100&closed=true&end_date_min=2026-11-11T23%3A00%3A00Z&end_date_max=2026-11-13T01%3A00%3A00Z -> 200, 597411 bytes, sha256 805ee81bc26659797795ef541b7a31a787c66c0cfcae6aaad9adb7139beea0e1, keys ['markets', 'next_cursor']
data trades        GET https://data-api.polymarket.com/v2/trades?condition=0xbdc863ac40456c9cddb58e02610d985bfd08401b0d9a622ede786ed7a085e5bf&taker_only=true&limit=5 -> 200, 4124 bytes, sha256 da2eb14deb7d6afd8fb9f38f75c07b96aa1042baf03bc14da0fd1050e594a818, keys ['data', 'pagination']
retries {}
G-PROBE PASS: 9 of 9 endpoints served and parsed
```

Kalshi's cutoff for markets and trades read `2026-09-28`, the Architect's of 2026-11-27, before every day of the set.

### 2.2 G-REHEARSAL (`logs/35-rehearse.log`, `logs/35-reference.log`, `logs/35-agree.log`)

`rehearse`, 2026-11-12, 23:04:36 to 23:07:09 UTC:

```
kalshi 2026-11-12T00:00:00Z: 103 pages, 102796 markets listed
rehearsal kalshi frame: 28563 rows in 517 groups; others {'outside': 10096, 'result': 735, 'volume': 63402}; 103 pages, 0 replayed, 103 new, 32 s
wrote /root/tz56a-work/rehearsal/draws-kalshi.jsonl 29738 bytes sha256 3fdc9fe7f548beb1c7ec706c533c47ead8e581ffdc4a92965ba7ec4600561673
rehearsal kalshi draws: 103 considered, 60 members, 101 markets fetched; {'None': 60, 'no_trade': 43}; 252 requests, 0 replayed, 252 new, 64 s
rehearsal kalshi retries {}, requests {'api.elections.kalshi.com': 355}
polymarket 2026-11-12T00:00:00Z: 288 pages, 28777 markets listed
rehearsal polymarket frame: 22811 rows in 302 groups; others {'late': 1, 'outside': 3116, 'result': 317, 'version': 2532}; 288 pages, 0 replayed, 288 new, 32 s
wrote /root/tz56a-work/rehearsal/draws-polymarket.jsonl 65838 bytes sha256 ffa9366c8641c68f61fd708d46a650d1a2b73eec915b7f979c341bc61ef75a7f
rehearsal polymarket draws: 179 considered, 60 members, 163 markets fetched; {'None': 60, 'no_trade': 119}; 170 requests, 0 replayed, 170 new, 24 s
rehearsal polymarket retries {}, requests {'gamma-api.polymarket.com': 288, 'data-api.polymarket.com': 170}
wrote /root/tz56a-work/rehearsal/instrument.json 1497 bytes sha256 53fd84736c50a36493438afe90c20042b04283b3548146d7e82f716d10e3d444
rehearsal: 12 figures and 8 kept-reply files written for agree
```

**The reference's output, whole** (`logs/35-reference.log`):

```
reference: MemAvailable [284434432] bytes, floor 157499106
reference: 813 kept replies indexed
reference: kalshi rows     28563
reference: kalshi keys     517
reference: kalshi reasons  {'outside': 10096, 'result': 735, 'volume': 63402}
reference: kalshi draws    103
reference: kalshi digest   5b2a880d9c7f595f48cdfc2409b453005ee21b13ba66dca71253883e8bbe33c3
reference: kalshi gross    628139564649870191653025003192713847/229113710652283845071852508980640000
reference: polymarket rows     22811
reference: polymarket keys     302
reference: polymarket reasons  {'late': 1, 'outside': 3116, 'result': 317, 'version': 2532}
reference: polymarket draws    179
reference: polymarket digest   2beb4bb36415d1f8528b51eb366c3c2643d516a6657399a760d9dfcd0ac85eef
reference: polymarket gross    185183838496465774244150701/58500928021680144000000000
reference: wrote /root/tz56a-work/rehearsal/reference.json sha256 53fd84736c50a36493438afe90c20042b04283b3548146d7e82f716d10e3d444
reference: peak memory 62562304 bytes
exit=0
```

`agree`, 23:07:35 UTC:

```
kept raw-draw-kalshi.jsonl.gz sha256 6895cb492d49b9d29f1b051fba9a30002e2fa9244b1b431686043f2ac4205c81
kept raw-draw-kalshi.jsonl.gz.idx sha256 bbca51adf2dbd77268c5038b1897f0a8491e8c196f6be1a5f82fb463ad3a55ef
kept raw-draw-polymarket.jsonl.gz sha256 7410e604888a360c1af6668bb073b298f1bc404ae53a977bd4770fc765460081
kept raw-draw-polymarket.jsonl.gz.idx sha256 e0ec11149dd87dd4e71761edcb622cfa65f8c4f98c4c5f995932a8989a00e2b3
kept raw-frame-kalshi.jsonl.gz sha256 c74d2d5215e8f8b9996f6dffcb8057899af6a2a1af7ad3369809912fca68881e
kept raw-frame-kalshi.jsonl.gz.idx sha256 95479b077cccdc59630af00ed72de287911caa54ef71b434a8261abf51beeb32
kept raw-frame-polymarket.jsonl.gz sha256 95d407f189e455ee8eca16ef3050e71c9707820f362c2a5ffce1f1bc2362acc1
kept raw-frame-polymarket.jsonl.gz.idx sha256 2c1e15f2fe5bc8dd587e8d99705fb239273b3b330abff97aabfefdc65ddeda22
G-REHEARSAL kalshi rows     28563, the reference's 28563: equal
G-REHEARSAL kalshi keys     517, the reference's 517: equal
G-REHEARSAL kalshi reasons  {'outside': 10096, 'result': 735, 'volume': 63402}, the reference's {'outside': 10096, 'result': 735, 'volume': 63402}: equal
G-REHEARSAL kalshi draws    103, the reference's 103: equal
G-REHEARSAL kalshi digest   5b2a880d9c7f595f48cdfc2409b453005ee21b13ba66dca71253883e8bbe33c3, the reference's 5b2a880d9c7f595f48cdfc2409b453005ee21b13ba66dca71253883e8bbe33c3: equal
G-REHEARSAL kalshi gross    628139564649870191653025003192713847/229113710652283845071852508980640000, the reference's 628139564649870191653025003192713847/229113710652283845071852508980640000: equal
G-REHEARSAL polymarket rows     22811, the reference's 22811: equal
G-REHEARSAL polymarket keys     302, the reference's 302: equal
G-REHEARSAL polymarket reasons  {'late': 1, 'outside': 3116, 'result': 317, 'version': 2532}, the reference's {'late': 1, 'outside': 3116, 'result': 317, 'version': 2532}: equal
G-REHEARSAL polymarket draws    179, the reference's 179: equal
G-REHEARSAL polymarket digest   2beb4bb36415d1f8528b51eb366c3c2643d516a6657399a760d9dfcd0ac85eef, the reference's 2beb4bb36415d1f8528b51eb366c3c2643d516a6657399a760d9dfcd0ac85eef: equal
G-REHEARSAL polymarket gross    185183838496465774244150701/58500928021680144000000000, the reference's 185183838496465774244150701/58500928021680144000000000: equal
G-REHEARSAL PASS: 12 of 12 figures equal to the reference's on the same kept replies
```

Recorded, compared with nothing: the members' fee coefficients' SHA-256, Kalshi
`bdc75793cb9f9ae42ac92eb975a803082ed416fed480589d1a6e6b2027e36d1a`, Polymarket
`df4f7bcc269442f80715338b9e57e669696772d59bc6a23be4eb5999a87b97fa`. The two digests equal the Architect's 20:48 and
21:00 runs of §4.1's table (Kalshi `5b2a880d…e33c3`, Polymarket `2beb4bb3…5eef`) — evidence, not a gate.

### 2.3 The frames — G-FRAME (`logs/36-frame.log`)

`now 2026-11-27T23:07:40Z, at or after 2026-11-23T12:00:00Z`; `MemAvailable 251322368 bytes, floor 157499106; free
9944076288 bytes, gate 8700000000`.

| day | Kalshi pages | Kalshi markets listed | Kalshi rows | Polymarket pages | Polymarket markets listed | Polymarket rows |
|---|---|---|---|---|---|---|
| 2026-11-16 | 125 | 124,244 | 28,397 | 236 | 23,579 | 15,099 |
| 2026-11-17 | 116 | 115,457 | 28,986 | 257 | 25,673 | 19,810 |
| 2026-11-18 | 111 | 110,436 | 26,045 | 249 | 24,808 | 14,133 |
| 2026-11-19 | 106 | 105,113 | 30,203 | 264 | 26,391 | 18,788 |
| 2026-11-20 | 119 | 118,653 | 28,283 | 304 | 30,308 | 21,891 |
| 2026-11-21 | 116 | 115,916 | 39,768 | 571 | 57,011 | 50,566 |

```
kalshi frame: 181682 rows in 3909 groups; others {'outside': 17313, 'result': 3261, 'status': 108, 'volume': 438385}; 693 pages, 0 replayed, 693 new, 211 s; retries {}
polymarket frame: 140287 rows in 1972 groups; others {'late': 458, 'outside': 6633, 'result': 485, 'version': 11894}; 1881 pages, 0 replayed, 1881 new, 205 s; retries {}
G-FRAME PASS: both venues framed, every day holding rows
```

Every day's pages stayed under the caps (`400` and `3,000`); the series-days `3,909` and `1,972` under `100,000`.

### 2.4 The draws — G-SET (`logs/37-draw.log`)

`MemAvailable 275456000 bytes, floor 157499106; free 9725661184 bytes, gate 8700000000` at 23:14:53 UTC.

| venue | considered | members | non-members by reason | markets fetched | requests | retries | time | fail-fast projection after 300 draws |
|---|---|---|---|---|---|---|---|---|
| Kalshi | 7,935 | 5,000 | `no_trade` 2,935 | 6,748 | 10,886 | none | 2,757 s | 187 members, 179 s; 8,021 draws, 4,784 s |
| Polymarket | 14,707 | 5,000 | `no_trade` 9,707 | 8,874 | 8,956 | `data-api.polymarket.com` 11 | 1,298 s | 103 members, 45 s; 14,563 draws, 2,177 s |

No draw on either venue was a non-member by `fee_type`, `fee_changed`, `fee_event` or `fee`. Polymarket's Data API
answered `500` eleven times between 00:16:06 and 00:22:23 UTC, each in its own words
`{"error":"internal server error","code":"internal","retryable":false,"trace_id":"<hex>"}`, and each served on the
second try after `2.0` s (`Net`'s retry of a `5xx`).

```
wrote /root/tz56a-work/run/draws-kalshi.jsonl 2319152 bytes sha256 96943fd7ec919a01d2b3babe91f84e1ab8f08807d273c257908cdbeba3eb3812
wrote /root/tz56a-work/run/draws-polymarket.jsonl 5437574 bytes sha256 6723e6215af2eec7eb8b7db666249a92a48e6d25dacd16191fb38ba912a68fe8
G-SET PASS: 5000 members on each venue
```

The draws' label-free digests, from `state.json`: Kalshi
`2b4647446004f68b223ab9533f00afbfc3f1e8efe9b9c22f66d6b6a99f97136a`, Polymarket
`da78edc99b5bfbbe6ca84491fccdde38f79b83f9174977528ee3805ea66d6596`.

### 2.5 DETERMINISM (`logs/38-redraw.log`)

```
frame-kalshi.jsonl c2e97ad87b0c88434145d4c74d34259c8da209a2185b4d03c565dc19f7a200c8 and c2e97ad87b0c88434145d4c74d34259c8da209a2185b4d03c565dc19f7a200c8: equal
draws-kalshi.jsonl 96943fd7ec919a01d2b3babe91f84e1ab8f08807d273c257908cdbeba3eb3812 and 96943fd7ec919a01d2b3babe91f84e1ab8f08807d273c257908cdbeba3eb3812: equal
frame-polymarket.jsonl 158200993b78b61405f46ff8473c0f9c350c04e6a741ba1d784614dc01d25320 and 158200993b78b61405f46ff8473c0f9c350c04e6a741ba1d784614dc01d25320: equal
draws-polymarket.jsonl 6723e6215af2eec7eb8b7db666249a92a48e6d25dacd16191fb38ba912a68fe8 and 6723e6215af2eec7eb8b7db666249a92a48e6d25dacd16191fb38ba912a68fe8: equal
DETERMINISM PASS: 4 of 4 files rebuilt from the kept replies, byte for byte
```

### 2.6 The score (`logs/39-score-1.log`, `logs/39-score-2.log`)

The first run, every line:

```
label gate: frames and draws as recorded; HEAD bf391748e2f975a579a4abf15b3bffc067799937 on origin; this file 7241a14afe5bde0bdeed37fb17bb9a45d59cc88e83ac319789eebedc07b335db, committed
kalshi: 5000 members of 7935 draws; mean money a contract after the fee 0.037975357150 (before it 0.045029630460, the fee 0.007054273310); log capital EARN 67.938691, NO EARN -109.053683, threshold ln 400 = 5.991465: EARN
polymarket: 5000 members of 14707 draws; mean money a contract after the fee 0.015984914135 (before it 0.018767412828, the fee 0.002782498693); log capital EARN 5.544303, NO EARN -27.951808, threshold ln 400 = 5.991465: UNDECIDABLE
wrote /root/tz56a-work/run/score.json 4329 bytes sha256 ae7e8ee6871060752b4540ed324db935c811ef2870a8a3a2f25a2de21656171e
K0: Kalshi EARN, Polymarket UNDECIDABLE
```

The second run printed the same two venue lines and the same `K0` line, and
`unchanged /root/tz56a-work/run/score.json 4329 bytes sha256 ae7e8ee6871060752b4540ed324db935c811ef2870a8a3a2f25a2de21656171e`.

#### Barred — read by no gate and deciding nothing

Each entry `[members, mean money a contract after the fee]`, as `score` printed it:

```
kalshi barred: {"by_category": {"Climate and Weather": [329, "0.052919924833"], "Commodities": [148, "-0.003265690294"], "Crypto": [256, "0.049476971857"], "Economics": [282, "0.039517467089"], "Entertainment": [70, "-0.074719735267"], "Financials": [206, "0.022918309411"], "Mentions": [52, "-0.016370387408"], "Politics": [55, "0.031642727681"], "Science and Technology": [46, "0.027458683348"], "Sports": [3544, "0.042380499986"]}, "by_day": {"2026-11-16T00:00:00Z": [700, "0.046229504853"], "2026-11-17T00:00:00Z": [688, "0.033286761697"], "2026-11-18T00:00:00Z": [625, "0.021800536728"], "2026-11-19T00:00:00Z": [595, "0.028060596559"], "2026-11-20T00:00:00Z": [1113, "0.048433781547"], "2026-11-21T00:00:00Z": [1279, "0.039395348739"]}, "mixed": [963, "-0.195659830119"], "single": [4037, "0.093707506107"], "slow": [4905, "0.026481067437"]}
polymarket barred: {"by_category": {"None": [139, "0.040779783401"], "crypto_fees_v2": [1465, "0.007818687894"], "culture_fees": [192, "0.066445990627"], "economics_fees": [55, "0.093396561759"], "finance_prices_fees": [1007, "0.002590107040"], "politics_fees": [91, "0.001567656926"], "sports_fees_v3": [953, "-0.000156058336"], "tech_fees": [113, "0.119414012893"], "weather_fees": [938, "0.027362818555"]}, "by_day": {"2026-11-16T00:00:00Z": [949, "0.027287392055"], "2026-11-17T00:00:00Z": [812, "0.043336883625"], "2026-11-18T00:00:00Z": [827, "0.032607094875"], "2026-11-19T00:00:00Z": [828, "-0.052885858434"], "2026-11-20T00:00:00Z": [918, "0.058425275726"], "2026-11-21T00:00:00Z": [666, "-0.026984525051"]}, "mixed": [740, "-0.347206698254"], "single": [4260, "0.079074536944"], "slow": [4703, "0.012715989792"]}
```

### 2.7 The Release's assets (`logs/310-pack-1.log`)

| asset | bytes | SHA-256 |
|---|---|---|
| `tz56a-frame-kalshi.jsonl.gz` | 1,364,372 | `1e1cd9128f365c9ada273600a302a08173e23eac18bbd8c38a0ad08d2c3c862b` |
| `tz56a-draws-kalshi.jsonl.gz` | 343,814 | `d3b3a03b1e9d6bc66b4c470220fba83f69839687605f37014e80e6de61429b67` |
| `tz56a-raw-frame-kalshi.jsonl.gz` | 41,042,366 | `bed859a687e6b94a85449e70cf80a60b1211be3af2951853d20b26ea9a671389` |
| `tz56a-raw-draw-kalshi.jsonl.gz` | 108,392,880 | `ae5317f2fd44a59731afa17fe90d33abfef35885378d344e2414b02a26871560` |
| `tz56a-rehearsal-raw-frame-kalshi.jsonl.gz` | 6,151,553 | `c74d2d5215e8f8b9996f6dffcb8057899af6a2a1af7ad3369809912fca68881e` |
| `tz56a-rehearsal-raw-draw-kalshi.jsonl.gz` | 2,079,840 | `6895cb492d49b9d29f1b051fba9a30002e2fa9244b1b431686043f2ac4205c81` |
| `tz56a-frame-polymarket.jsonl.gz` | 18,614,941 | `2fdd7b013c48edd8e9e65861d247b57ab451bffbc02589b455a68b01865e7156` |
| `tz56a-draws-polymarket.jsonl.gz` | 1,082,741 | `887369e65879854698b8b1de1cd055f85bb447cfd66a5f457fd1fb7873bddb35` |
| `tz56a-raw-frame-polymarket.jsonl.gz` | 91,082,077 | `ca123195f4a27821adbf445064ab1f1fd5b1dee99f1323608190a26468444602` |
| `tz56a-raw-draw-polymarket.jsonl.gz` | 57,035,038 | `b005ddd4c30682d6ef46a85392202c37c76bcf8ac5a00e4551c8fef9dd33a04c` |
| `tz56a-rehearsal-raw-frame-polymarket.jsonl.gz` | 14,471,928 | `95d407f189e455ee8eca16ef3050e71c9707820f362c2a5ffce1f1bc2362acc1` |
| `tz56a-rehearsal-raw-draw-polymarket.jsonl.gz` | 1,671,289 | `7410e604888a360c1af6668bb073b298f1bc404ae53a977bd4770fc765460081` |
| `tz56a-score.json` | 4,329 | `ae7e8ee6871060752b4540ed324db935c811ef2870a8a3a2f25a2de21656171e` |

```
PACK: 13 assets, 343337168 bytes, at commit bf391748e2f975a579a4abf15b3bffc067799937; set sha256 685ac340aa66a1cfb33a8d21fa40cfb5e92dbe8476c44d4f340cbce2fa2f74dc
```

The second run printed `unchanged` for the four gzipped assets, `release-set.json` and `release-notes.md`, and the same
`PACK` line.

### 2.8 TZ-56's pull request #54 (`logs/31-pr.log`)

```
✓ Closed pull request #54 (TZ-56: K0's instrument - research/tz56-k0-favourite.py)
exit=0
{"closedAt":"2026-11-27T23:04:00Z","headRefName":"tz-56-k0-favourite","state":"CLOSED"}
```

with the comment `TZ-56 BLOCKED at G-REHEARSAL; superseded by TZ-56a, branch tz-56a-k0-favourite.` Its branch is kept.
Pull request #55, `tz-56a-k0-favourite` into `main`, opened at the same step:
`https://github.com/seahomebatumi-ai/btc-5m-twap/pull/55`.

### 2.9 Memory, every mode (V15, recorded, not asserted)

| log | peak bytes | `malloc tuned` | refused |
|---|---|---|---|
| `02-fingerprint` | 29,724,672 | True | 0 |
| `05-number` | 28,577,792 | True | 0 |
| `32-selftest` | 39,907,328 | True | 0 |
| `33-still` | 28,712,960 | True | 0 |
| `33-scratch` | 28,708,864 | True | 0 |
| `33-reclaim-scratch` | 31,260,672 | True | 0 |
| `34-probe` | 42,086,400 | True | 0 |
| `35-rehearse` | 56,303,616 | True | 0 |
| `35-reference` | 62,562,304 | — | — |
| `35-agree` | 30,900,224 | True | 0 |
| `36-frame` | 53,878,784 | True | 0 |
| `37-draw` | 39,051,264 | True | 0 |
| `38-redraw` | 58,503,168 | True | 0 |
| `39-score-1` | 46,190,592 | True | 0 |
| `39-score-2` | 46,321,664 | True | 0 |
| `310-pack-1` | 31,809,536 | True | 0 |
| `310-pack-2` | 31,809,536 | True | 0 |
| `312-verify` | 33,447,936 | True | 0 |
| `313-still` | 28,708,864 | True | 0 |
| `9-reclaim` | 32,387,072 | True | 0 |

The largest, the reference's `62,562,304`, is under its `PEAK_BOUND` `65,679,360`. `MemAvailable` at the modes' starts read
from `251,322,368` to `284,434,432`, every one above the floor `157,499,106` on its first read.

### 2.10 The units, the closing reads and the directories beside this session

**§3.3 (`logs/33-still.log`), 23:04:07 UTC:** the recorder `3525462`, the reward book `3525511`, the advisor `3525469`,
the liquidation guard `3525503`, each `NRestarts 0`, `active`; the archive's timer `active`. **G-STILL
(`logs/313-still.log`), 00:29:05 UTC:** `G-STILL PASS: unchanged since 2026-11-27T23:04:07Z`.

**`I scratch "$(dirname "$S")"` (`logs/33-scratch.log`):** two live — `2d86e605-…` (processes `3609544`, `3609554`,
`3609563`, `3609585`, born 19:47) and `648858b7-…` (process `3628204`, born 23:02:18) — and 13 earlier:
`0736470b-13a0-4e8d-931f-5ecf4df19205`, `14b0bf22-9b3d-5114-ae1e-88801e8819ce`, `54158118-b10a-4d9c-a8c6-8f105e70d6f3`,
`6c04aed0-6057-4e03-a1b5-56678f8a595f`, `6f0f41a7-6da7-5e8a-80e1-a2a85a4a8e5c`, `7123abac-62f9-42cc-9fa9-5198a10b37c2`,
`860e27fb-81a3-4d7c-b748-b9d5ae1cc5c8`, `96027802-bb60-4eac-b19f-046e75ba8949`, `b6258107-0dab-42e0-98d3-e94730b41617`,
`d8d0feb2-4f8e-5084-a026-9e20a0303c89`, `edfd5742-e105-564d-b1bc-16a84a7355a9`, `f05cea76-0be2-5057-94c5-39713a008e6e`
and `f22e0a97-2a88-44f5-8f8b-da5078b1ee7d`. **B-RECLAIM-SCRATCH** ran in the session, unrefused
(`logs/33-reclaim-scratch.log`):

```
reclaim: 4545 report tokens; forensic store holds 2876 files; the Release tz-56a-k0-inputs proved 0 assets
RECLAIM PASS: 6 files considered, 0 named by a report, 0 kept by name, 0 copied, 0 already held, 0 left to the Release tz-56a-k0-inputs that holds them; forensic store 2876 -> 2876 files
```

and each of the 13 `test -e` printed `exit=1`.

**Closing host reads (`logs/313-host.log`), 00:29:05 UTC on 2026-11-28, epoch `1795825745`:** H1, H2, H3, H4 as at
§0.3; `MemAvailable: 232988 kB`; `avail` `9,376,092,160`; the reward book's store `577,717,153`, its stream files
`106,066,272`; the forensic store `397,273,552` at `2,876` files; the units as §3.3; the worktrees the primary checkout,
`/root/btc-recorder-svc` and `/root/tz56a-work/wt` at `bf39174`. **The margin:** `9,376,092,160 + 106,066,272 −
7,300,000,000 − 445,535,636 = 1,736,622,796` bytes, with this run's tree still on disk (§9 removes it).

**Closing refs (`logs/313-refs.log`):** 269 lines — `HEAD` 1, heads 32, pull 55, tags 181. Against §0.5's read:
`refs/pull/54/merge` gone (#54 closed); new `refs/heads/tz-56a-k0-favourite`, `refs/pull/55/head` and
`refs/tags/tz-56a-k0-inputs`, each at `bf391748e2f975a579a4abf15b3bffc067799937`, and `refs/pull/55/merge` at
`abc149ff57fd9989e92e509859bbf23b13e8983f`.

### 2.11 Reclaim (§9)

**`I reclaim /root/tz56a-work` (`logs/9-reclaim.log`), quoted whole from the work tree before B-RECLAIM-OWN** — its
forensic copy `/root/btc-forensics/tz56a-work--logs--9-reclaim.log` (`cc9a5dc3…b619`, 36 lines) was taken while the
log was being written; the whole log, 84 lines, read `acb23ced5eb37819e90c5b26705cb9396ae822432031fc9036a1c7eda0f56d1a`
with the timestamps the quote below drops:

```
reclaim: 4582 report tokens; forensic store holds 2876 files; the Release tz-56a-k0-inputs proved 13 assets
reclaim: /root/tz56a-work/wt skipped: no file but its HEAD's, and HEAD bf391748e2f975a579a4abf15b3bffc067799937 is its upstream's
R copied 4aedcf998e3949985762088a232da940fba6d7e47e3d75627543062f8f6f2a40 /root/btc-forensics/tz56a-work--read-ledger.jsonl
R copied 7345e8a23259b5a5bf4e739946ef27f517c67c4eb7d503101c594d880fcbe583 /root/btc-forensics/tz56a-work--release-notes.md
R copied 685ac340aa66a1cfb33a8d21fa40cfb5e92dbe8476c44d4f340cbce2fa2f74dc /root/btc-forensics/tz56a-work--release-set.json
R copied 3d5161e27a05b8b0315c9ddb68ae789b4361e32ee36fe6fc6f4cfa3908ffc2d7 /root/btc-forensics/tz56a-work--state.json
R copied 89a08cc798f3e8947bef5c6ed539536f11d8e0b10fa98b251effee55e1d28f5d /root/btc-forensics/tz56a-work--verify.json
R copied 3f027858575cef291c4ffdc33fe6a7d7c373413782075f8d4282a25f727aff27 /root/btc-forensics/tz56a-work--logs--00-worktree.log
R copied adb0c8870a327d76c718163921d10faa80cc23112e2a6c61eb499f3b28a0a790 /root/btc-forensics/tz56a-work--logs--01-stage.log
R copied 8e5d73d714fc7c308025a561943d72ee89392e1434e8b3227e428ee32e442785 /root/btc-forensics/tz56a-work--logs--02-fingerprint.log
R copied 2a20430acf03269a01f690cfeeddde91d1cfb1fd015325ce085da1ace9bf9fc3 /root/btc-forensics/tz56a-work--logs--03-host-gate.log
R copied 8c6c5cff12d09a00d26f4cd28af67343dd28245218e6ec35645aa6583f4c5d0e /root/btc-forensics/tz56a-work--logs--05-number.log
R copied 159ef03a8a3f03b9576bb58723410957dcdfd063ba32b4654ef34fec7f7d47bb /root/btc-forensics/tz56a-work--logs--05-refs.log
R copied 119beae60522d2d304ad45311771be686bcacf10c50d37b6fb89b94e7d26e2aa /root/btc-forensics/tz56a-work--logs--31-branch.log
R copied 57d9772f892ca32ee22c389780bb82bfe2c34f853d3ee8e6225db9c81cc6291e /root/btc-forensics/tz56a-work--logs--31-pr.log
R copied c52b0bd9f60959c9daea629a044e304360da2c131b4df816e82afbe095f40962 /root/btc-forensics/tz56a-work--logs--310-pack-1.log
R copied 91859ccd1c826b9f5c0ebbcd2bea7f1da6946371a91cf9151ccf17598610cd69 /root/btc-forensics/tz56a-work--logs--310-pack-2.log
R copied 07e0affdc118e9681d8428f2a553debbc136c7845ce60844d17b531859034a14 /root/btc-forensics/tz56a-work--logs--311-upload.log
R copied 0396260024c595b989c2240125c37364827a221690536fc61a5665c474759d7c /root/btc-forensics/tz56a-work--logs--312-verify.log
R copied 3a4707cf10fe4a8a38b2d46b76896e688b48b4f09804c65a0f9c2f4f776109ea /root/btc-forensics/tz56a-work--logs--313-host.log
R copied ab199a420c4cac4a808748c74f7e0fbe68bc90084610779d2651c907bffe3ee4 /root/btc-forensics/tz56a-work--logs--313-refs.log
R copied d6a0e9334c47a8393ae0671952930b405bfdd4f6136c48392acfab3ea74930f6 /root/btc-forensics/tz56a-work--logs--313-still.log
R copied 02e20c38bd8efc9c4e8a1ecf0a9c27ac9c838cd92ee8f14b7bf57983b2948e22 /root/btc-forensics/tz56a-work--logs--32-selftest.log
R copied c5fe159e5d9d055a66c7a012678e1bc3af6095035eeb7860a49faa993fd88695 /root/btc-forensics/tz56a-work--logs--33-reclaim-scratch.log
R copied d973d5286b61e1a810762949eeb963a44ce34a3b78a376e8994d3ffa267e02cd /root/btc-forensics/tz56a-work--logs--33-scratch.log
R copied bb0430cd65f7b17118f4cd89d1ca9a7f4c6b6749084093d338ebcb1692a75d8c /root/btc-forensics/tz56a-work--logs--33-still.log
R copied d2321d2088a466fc074857f7259dae6dee0a2439502d20d36408a6655a1706d2 /root/btc-forensics/tz56a-work--logs--34-probe.log
R copied 3fca50bedc96cc70aa47ae8a1c733d0c00e2a8544d7f0a8a6a8ac288cbaac97d /root/btc-forensics/tz56a-work--logs--35-agree.log
R copied bb5e798e46e2643325145c750d30c041558ef9b961f96ccac92726efa16311a3 /root/btc-forensics/tz56a-work--logs--35-reference.log
R copied f58fdc9721291fde74af1e36147bd210ed3ec92270c45485e117045a72ba97a8 /root/btc-forensics/tz56a-work--logs--35-rehearse.log
R copied 11669aa38a046ae5d30edf81e0e12740fc5a19c7b71097635d76e8ae4557b9f6 /root/btc-forensics/tz56a-work--logs--36-frame.log
R copied 6e257f31217b3edad420060eed293629bbfdd018d3138dcd541b4ff2d0d3c0c8 /root/btc-forensics/tz56a-work--logs--36-wait.log
R copied 790fb66545693356adcc3b717213e0a7e14842ced84c6b1b30df3bcc282167eb /root/btc-forensics/tz56a-work--logs--37-draw.log
R copied ad0085c1d950bc93d35809c84e7f88661b346c2f21d283c54a46172600936e2a /root/btc-forensics/tz56a-work--logs--38-redraw.log
R copied 62078b0dfa63e0d3f98266f176e063976ffffb82c9770d8c71b8ed63f95cf9d1 /root/btc-forensics/tz56a-work--logs--39-score-1.log
R copied dd9fee4b64538347b5addedf6fa1b7ad6b727369d33a7ba67d2a0970daaf5ee8 /root/btc-forensics/tz56a-work--logs--39-score-2.log
R copied cc9a5dc30611da175f65fbaa282b94cca9ad7e189cc1a93507bd4fb75cc6b619 /root/btc-forensics/tz56a-work--logs--9-reclaim.log
R copied 96943fd7ec919a01d2b3babe91f84e1ab8f08807d273c257908cdbeba3eb3812 /root/btc-forensics/tz56a-work--redraw--draws-kalshi.jsonl
R copied 6723e6215af2eec7eb8b7db666249a92a48e6d25dacd16191fb38ba912a68fe8 /root/btc-forensics/tz56a-work--redraw--draws-polymarket.jsonl
R copied c2e97ad87b0c88434145d4c74d34259c8da209a2185b4d03c565dc19f7a200c8 /root/btc-forensics/tz56a-work--redraw--frame-kalshi.jsonl
R copied 158200993b78b61405f46ff8473c0f9c350c04e6a741ba1d784614dc01d25320 /root/btc-forensics/tz56a-work--redraw--frame-polymarket.jsonl
R copied 3fdc9fe7f548beb1c7ec706c533c47ead8e581ffdc4a92965ba7ec4600561673 /root/btc-forensics/tz56a-work--rehearsal--draws-kalshi.jsonl
R copied ffa9366c8641c68f61fd708d46a650d1a2b73eec915b7f979c341bc61ef75a7f /root/btc-forensics/tz56a-work--rehearsal--draws-polymarket.jsonl
R copied 83de241cfea6aeff53b8341c9d6e2668d48efae5640b8557f46474afe5b931bb /root/btc-forensics/tz56a-work--rehearsal--frame-kalshi.jsonl
R copied c22fb7d561851e76cd9720e7ecf611e61fb8426078a057a6ecce864fcd66a433 /root/btc-forensics/tz56a-work--rehearsal--frame-polymarket.jsonl
R copied 53fd84736c50a36493438afe90c20042b04283b3548146d7e82f716d10e3d444 /root/btc-forensics/tz56a-work--rehearsal--instrument.json
R release 6895cb492d49b9d29f1b051fba9a30002e2fa9244b1b431686043f2ac4205c81 /root/tz56a-work/rehearsal/raw-draw-kalshi.jsonl.gz is tz56a-rehearsal-raw-draw-kalshi.jsonl.gz of tz-56a-k0-inputs
R copied bbca51adf2dbd77268c5038b1897f0a8491e8c196f6be1a5f82fb463ad3a55ef /root/btc-forensics/tz56a-work--rehearsal--raw-draw-kalshi.jsonl.gz.idx
R release 7410e604888a360c1af6668bb073b298f1bc404ae53a977bd4770fc765460081 /root/tz56a-work/rehearsal/raw-draw-polymarket.jsonl.gz is tz56a-rehearsal-raw-draw-polymarket.jsonl.gz of tz-56a-k0-inputs
R copied e0ec11149dd87dd4e71761edcb622cfa65f8c4f98c4c5f995932a8989a00e2b3 /root/btc-forensics/tz56a-work--rehearsal--raw-draw-polymarket.jsonl.gz.idx
R release c74d2d5215e8f8b9996f6dffcb8057899af6a2a1af7ad3369809912fca68881e /root/tz56a-work/rehearsal/raw-frame-kalshi.jsonl.gz is tz56a-rehearsal-raw-frame-kalshi.jsonl.gz of tz-56a-k0-inputs
R copied 95479b077cccdc59630af00ed72de287911caa54ef71b434a8261abf51beeb32 /root/btc-forensics/tz56a-work--rehearsal--raw-frame-kalshi.jsonl.gz.idx
R release 95d407f189e455ee8eca16ef3050e71c9707820f362c2a5ffce1f1bc2362acc1 /root/tz56a-work/rehearsal/raw-frame-polymarket.jsonl.gz is tz56a-rehearsal-raw-frame-polymarket.jsonl.gz of tz-56a-k0-inputs
R copied 2c1e15f2fe5bc8dd587e8d99705fb239273b3b330abff97aabfefdc65ddeda22 /root/btc-forensics/tz56a-work--rehearsal--raw-frame-polymarket.jsonl.gz.idx
R copied 53fd84736c50a36493438afe90c20042b04283b3548146d7e82f716d10e3d444 /root/btc-forensics/tz56a-work--rehearsal--reference.json
R release d3b3a03b1e9d6bc66b4c470220fba83f69839687605f37014e80e6de61429b67 /root/tz56a-work/release/tz56a-draws-kalshi.jsonl.gz is tz56a-draws-kalshi.jsonl.gz of tz-56a-k0-inputs
R release 887369e65879854698b8b1de1cd055f85bb447cfd66a5f457fd1fb7873bddb35 /root/tz56a-work/release/tz56a-draws-polymarket.jsonl.gz is tz56a-draws-polymarket.jsonl.gz of tz-56a-k0-inputs
R release 1e1cd9128f365c9ada273600a302a08173e23eac18bbd8c38a0ad08d2c3c862b /root/tz56a-work/release/tz56a-frame-kalshi.jsonl.gz is tz56a-frame-kalshi.jsonl.gz of tz-56a-k0-inputs
R release 2fdd7b013c48edd8e9e65861d247b57ab451bffbc02589b455a68b01865e7156 /root/tz56a-work/release/tz56a-frame-polymarket.jsonl.gz is tz56a-frame-polymarket.jsonl.gz of tz-56a-k0-inputs
R release ae5317f2fd44a59731afa17fe90d33abfef35885378d344e2414b02a26871560 /root/tz56a-work/release/tz56a-raw-draw-kalshi.jsonl.gz is tz56a-raw-draw-kalshi.jsonl.gz of tz-56a-k0-inputs
R release b005ddd4c30682d6ef46a85392202c37c76bcf8ac5a00e4551c8fef9dd33a04c /root/tz56a-work/release/tz56a-raw-draw-polymarket.jsonl.gz is tz56a-raw-draw-polymarket.jsonl.gz of tz-56a-k0-inputs
R release bed859a687e6b94a85449e70cf80a60b1211be3af2951853d20b26ea9a671389 /root/tz56a-work/release/tz56a-raw-frame-kalshi.jsonl.gz is tz56a-raw-frame-kalshi.jsonl.gz of tz-56a-k0-inputs
R release ca123195f4a27821adbf445064ab1f1fd5b1dee99f1323608190a26468444602 /root/tz56a-work/release/tz56a-raw-frame-polymarket.jsonl.gz is tz56a-raw-frame-polymarket.jsonl.gz of tz-56a-k0-inputs
R release 6895cb492d49b9d29f1b051fba9a30002e2fa9244b1b431686043f2ac4205c81 /root/tz56a-work/release/tz56a-rehearsal-raw-draw-kalshi.jsonl.gz is tz56a-rehearsal-raw-draw-kalshi.jsonl.gz of tz-56a-k0-inputs
R release 7410e604888a360c1af6668bb073b298f1bc404ae53a977bd4770fc765460081 /root/tz56a-work/release/tz56a-rehearsal-raw-draw-polymarket.jsonl.gz is tz56a-rehearsal-raw-draw-polymarket.jsonl.gz of tz-56a-k0-inputs
R release c74d2d5215e8f8b9996f6dffcb8057899af6a2a1af7ad3369809912fca68881e /root/tz56a-work/release/tz56a-rehearsal-raw-frame-kalshi.jsonl.gz is tz56a-rehearsal-raw-frame-kalshi.jsonl.gz of tz-56a-k0-inputs
R release 95d407f189e455ee8eca16ef3050e71c9707820f362c2a5ffce1f1bc2362acc1 /root/tz56a-work/release/tz56a-rehearsal-raw-frame-polymarket.jsonl.gz is tz56a-rehearsal-raw-frame-polymarket.jsonl.gz of tz-56a-k0-inputs
R release ae7e8ee6871060752b4540ed324db935c811ef2870a8a3a2f25a2de21656171e /root/tz56a-work/release/tz56a-score.json is tz56a-score.json of tz-56a-k0-inputs
R copied 96943fd7ec919a01d2b3babe91f84e1ab8f08807d273c257908cdbeba3eb3812 /root/btc-forensics/tz56a-work--run--draws-kalshi.jsonl
R copied 6723e6215af2eec7eb8b7db666249a92a48e6d25dacd16191fb38ba912a68fe8 /root/btc-forensics/tz56a-work--run--draws-polymarket.jsonl
R copied c2e97ad87b0c88434145d4c74d34259c8da209a2185b4d03c565dc19f7a200c8 /root/btc-forensics/tz56a-work--run--frame-kalshi.jsonl
R copied 158200993b78b61405f46ff8473c0f9c350c04e6a741ba1d784614dc01d25320 /root/btc-forensics/tz56a-work--run--frame-polymarket.jsonl
R release ae5317f2fd44a59731afa17fe90d33abfef35885378d344e2414b02a26871560 /root/tz56a-work/run/raw-draw-kalshi.jsonl.gz is tz56a-raw-draw-kalshi.jsonl.gz of tz-56a-k0-inputs
R release b005ddd4c30682d6ef46a85392202c37c76bcf8ac5a00e4551c8fef9dd33a04c /root/tz56a-work/run/raw-draw-polymarket.jsonl.gz is tz56a-raw-draw-polymarket.jsonl.gz of tz-56a-k0-inputs
R release bed859a687e6b94a85449e70cf80a60b1211be3af2951853d20b26ea9a671389 /root/tz56a-work/run/raw-frame-kalshi.jsonl.gz is tz56a-raw-frame-kalshi.jsonl.gz of tz-56a-k0-inputs
R release ca123195f4a27821adbf445064ab1f1fd5b1dee99f1323608190a26468444602 /root/tz56a-work/run/raw-frame-polymarket.jsonl.gz is tz56a-raw-frame-polymarket.jsonl.gz of tz-56a-k0-inputs
R release ae7e8ee6871060752b4540ed324db935c811ef2870a8a3a2f25a2de21656171e /root/tz56a-work/run/score.json is tz56a-score.json of tz-56a-k0-inputs
R copied 9de780a0f5744d5cceb3074c0373020cda15dd4a7ac8bee288c13f9ab7a91f6c /root/btc-forensics/tz56a-work--stage--reference--tz56a-k0-reference.py
R copied 7241a14afe5bde0bdeed37fb17bb9a45d59cc88e83ac319789eebedc07b335db /root/btc-forensics/tz56a-work--stage--research--tz56-k0-favourite.py
RECLAIM PASS: 82 files considered, 47 named by a report, 30 kept by name, 55 copied, 0 already held, 22 left to the Release tz-56a-k0-inputs that holds them; forensic store 2876 -> 2931 files
malloc tuned: True
peak memory of this run: 32387072 bytes
opens, requests and processes refused: 0
exit=0
```

**B-RECLAIM-OWN**, the TZ's paste verbatim, run in the session at 00:34 UTC on 2026-11-28, unrefused; its output, whole:

```
tz56a-work exit=1
/root/btc-5m-twap       9cdf5f3 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
```

`exit=1`, and the worktree list holds the primary checkout and `/root/btc-recorder-svc` alone. The forensic store
holds 55 files `tz56a-work--*` after it.

## 3. Publication

| item | value |
|---|---|
| branch | `tz-56a-k0-favourite` |
| commit | `bf391748e2f975a579a4abf15b3bffc067799937` — `TZ-56a: K0's instrument, its second run - research/tz56-k0-favourite.py`; the file's SHA-256 `7241a14afe5bde0bdeed37fb17bb9a45d59cc88e83ac319789eebedc07b335db`, §0.1's |
| pull request | #55, open, not merged |
| Release | `tz-56a-k0-inputs`, lightweight tag at `bf391748…9937`, target the same commit, not latest |
| assets | 13, `343,337,168` bytes; `release-set.json` `685ac340aa66a1cfb33a8d21fa40cfb5e92dbe8476c44d4f340cbce2fa2f74dc` |
| local hashes | §2.7, `pack`'s |
| API digests and downloaded hashes | `verify`, below — all 13 equal to the local ones |

**B-UPLOAD (`logs/311-upload.log`)** ran in the session, unrefused:

```
https://github.com/seahomebatumi-ai/btc-5m-twap/releases/tag/tz-56a-k0-inputs
exit=0
Sat Nov 28 12:26:25 AM UTC 2026
```

**`I verify` (`logs/312-verify.log`)**, from 00:28:35 UTC, 130 s after B-UPLOAD's date, no credential:

```
V tz56a-frame-kalshi.jsonl.gz                  api True digest sha256:1e1cd9128f365c9ada273600a302a08173e23eac18bbd8c38a0ad08d2c3c862b download True 1364372 bytes
V tz56a-draws-kalshi.jsonl.gz                  api True digest sha256:d3b3a03b1e9d6bc66b4c470220fba83f69839687605f37014e80e6de61429b67 download True 343814 bytes
V tz56a-raw-frame-kalshi.jsonl.gz              api True digest sha256:bed859a687e6b94a85449e70cf80a60b1211be3af2951853d20b26ea9a671389 download True 41042366 bytes
V tz56a-raw-draw-kalshi.jsonl.gz               api True digest sha256:ae5317f2fd44a59731afa17fe90d33abfef35885378d344e2414b02a26871560 download True 108392880 bytes
V tz56a-rehearsal-raw-frame-kalshi.jsonl.gz    api True digest sha256:c74d2d5215e8f8b9996f6dffcb8057899af6a2a1af7ad3369809912fca68881e download True 6151553 bytes
V tz56a-rehearsal-raw-draw-kalshi.jsonl.gz     api True digest sha256:6895cb492d49b9d29f1b051fba9a30002e2fa9244b1b431686043f2ac4205c81 download True 2079840 bytes
V tz56a-frame-polymarket.jsonl.gz              api True digest sha256:2fdd7b013c48edd8e9e65861d247b57ab451bffbc02589b455a68b01865e7156 download True 18614941 bytes
V tz56a-draws-polymarket.jsonl.gz              api True digest sha256:887369e65879854698b8b1de1cd055f85bb447cfd66a5f457fd1fb7873bddb35 download True 1082741 bytes
V tz56a-raw-frame-polymarket.jsonl.gz          api True digest sha256:ca123195f4a27821adbf445064ab1f1fd5b1dee99f1323608190a26468444602 download True 91082077 bytes
V tz56a-raw-draw-polymarket.jsonl.gz           api True digest sha256:b005ddd4c30682d6ef46a85392202c37c76bcf8ac5a00e4551c8fef9dd33a04c download True 57035038 bytes
V tz56a-rehearsal-raw-frame-polymarket.jsonl.gz api True digest sha256:95d407f189e455ee8eca16ef3050e71c9707820f362c2a5ffce1f1bc2362acc1 download True 14471928 bytes
V tz56a-rehearsal-raw-draw-polymarket.jsonl.gz api True digest sha256:7410e604888a360c1af6668bb073b298f1bc404ae53a977bd4770fc765460081 download True 1671289 bytes
V tz56a-score.json                             api True digest sha256:ae7e8ee6871060752b4540ed324db935c811ef2870a8a3a2f25a2de21656171e download True 4329 bytes
tag tz-56a-k0-inputs on origin: [['bf391748e2f975a579a4abf15b3bffc067799937', 'refs/tags/tz-56a-k0-inputs']]; the pack's commit bf391748e2f975a579a4abf15b3bffc067799937; the Release's target bf391748e2f975a579a4abf15b3bffc067799937; assets beyond the set []
wrote /root/tz56a-work/verify.json 4297 bytes sha256 89a08cc798f3e8947bef5c6ed539536f11d8e0b10fa98b251effee55e1d28f5d
G-UPLOAD PASS: 13 of 13 assets by name, size, state and digest; G-DOWNLOAD PASS: 13 of 13 downloads, 343337168 bytes; G-TAG PASS: tz-56a-k0-inputs at bf391748e2f975a579a4abf15b3bffc067799937
```

**Contract §4.2 separation self-check**, after `git fetch origin`, before the report's commit:

```
$ git rev-list origin/main | grep -c bf391748e2f975a579a4abf15b3bffc067799937
0
$ git diff --name-only origin/main origin/tz-56a-k0-favourite
research/tz56-k0-favourite.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
(nothing; grep exit=1)
```

The reference, Appendix B, was staged under `/root/tz56a-work/stage/` and never committed.

## 4. Gate

§4.6, quoted:

| reading | where |
|---|---|
| **EARN** | the log of the EARN capital at or above `ln 400` = `5.991464547107981986870447152285081551353203245978056460308015820921932` |
| **NO EARN** | not EARN, and the log of the NO EARN capital at or above `ln 400` |
| **UNDECIDABLE** | neither |

Filled from `score`'s lines (§2.6):

| venue | members | log EARN capital | log NO EARN capital | `ln 400` | mean money a contract after the fee | reading |
|---|---|---|---|---|---|---|
| Kalshi | 5,000 of 7,935 draws | **67.938691** | −109.053683 | 5.991465 | **0.0380** | **EARN** |
| Polymarket | 5,000 of 14,707 draws | **5.544303** | −27.951808 | 5.991465 | **0.0160** | **UNDECIDABLE** |

`α = 1/400` a venue and answer; `1/200` an answer family-wise over the two venues. Polymarket's EARN capital stands
`0.447162` in log below `ln 400`: no reading. Power qualifies a silence, never a reading (map §7 item 60); at a true
`+2` cents the Architect's simulation gave EARN on Polymarket `0.86` of the time at 5,000 members.

**§1's decision this takes: "EARN on Kalshi alone — K1."** Kalshi is EARN and Polymarket is not EARN; Kalshi is not NO
EARN, so the K track does not close, and Polymarket's UNDECIDABLE closes nothing and admits nothing.

The other gates: G-PROBE `9 of 9`; G-REHEARSAL `12 of 12`; G-FRAME PASS, six days with rows on both venues; G-SET 5,000
members on each venue within 7,935 of `20,000` and 14,707 of `40,000` draws, the fail-fast at 4,784 s and 2,177 s
against `10,800`; DETERMINISM 4 of 4, `score` and `pack` byte for byte; G-UPLOAD `13 of 13`, G-DOWNLOAD `13 of 13`,
G-TAG at `bf391748…9937`; G-STILL PASS.

## 5. Validation

Every row an assert of the mode named, which aborts the mode on failure (exit 1); quoted from its log.

| # | step | printed | count | asserted |
|---|---|---|---|---|
| V1 | §0.2 | `FINGERPRINT PASS: revision 2026-11-28-a; anchors 6 of 6, 4 re-derived; rows 74: frozen 71 of 71 equal, tracked 2, reported 1` | 71 of 71 | yes |
| V2 | §0.5 | `NUMBER PASS - 2 of 2` | 2 of 2 | yes |
| V3 | §3.2 | `SELFTEST PASS: 67 of 67 checks`; `opens, requests and processes refused: 0` | 67 of 67 | yes |
| V4 | §3.4 | `G-PROBE PASS: 9 of 9 endpoints served and parsed` | 9 of 9 | yes |
| V5 | §3.5 | `rehearsal: 12 figures and 8 kept-reply files written for agree`; the reference's twelve figures, `reference: wrote …reference.json`, `exit=0`; eight `kept … sha256` lines; twelve `G-REHEARSAL … equal` lines; `G-REHEARSAL PASS: 12 of 12 figures equal to the reference's on the same kept replies` | 12 of 12 | yes |
| V6 | §3.6 | `now 2026-11-27T23:07:40Z, at or after 2026-11-23T12:00:00Z`; twelve day lines; six days above 0 on each venue; `G-FRAME PASS` | 12 of 12 days | yes |
| V7 | §3.7 | both projection lines; `G-SET PASS: 5000 members on each venue` | 2 of 2 venues | yes |
| V8 | §3.8 | four `… equal` lines; `DETERMINISM PASS: 4 of 4` | 4 of 4 | yes |
| V9 | §3.9 | `label gate: …`; both venues' lines; `K0: Kalshi EARN, Polymarket UNDECIDABLE`; the second run `unchanged …score.json` | 1 of 1 file | yes |
| V10 | §3.10 | thirteen `asset` lines; `PACK: 13 assets`; the second run's six `unchanged` lines | 13 of 13 | yes |
| V11 | §3.11 | `exit=0`, `Sat Nov 28 12:26:25 AM UTC 2026` | — | the paste's `&&` chain |
| V12 | §3.12 | thirteen `V` lines, each `api True`, `download True`; `G-UPLOAD PASS: 13 of 13 … G-DOWNLOAD PASS: 13 of 13 … G-TAG PASS: tz-56a-k0-inputs at bf391748e2f975a579a4abf15b3bffc067799937` | 13 of 13, 13 of 13 | yes |
| V13 | §3.13 | `G-STILL PASS: unchanged since 2026-11-27T23:04:07Z` | 5 of 5 units | yes |
| V14 | §9 | `RECLAIM PASS: 82 files considered, 47 named by a report, 30 kept by name, 55 copied, 0 already held, 22 left to the Release tz-56a-k0-inputs that holds them; forensic store 2876 -> 2931 files`; B-RECLAIM-OWN `tz56a-work exit=1`; B-RECLAIM-SCRATCH 13 `exit=1` | 55 copied, 22 left to the Release; 14 of 14 `test -e` | yes |
| V15 | every mode | `peak memory of this run` (§2.9), recorded, not asserted; `malloc tuned: True` in every mode of the instrument; `opens, requests and processes refused: 0` in every one | 20 of 20 logs | recorded, not asserted |

## 6. What could not be implemented as written

1. **One command's output went to the session's scratchpad**, against §0.0. While reading the map's §7 items before
   §3.1 (contract §1 step 2), the Executor redirected a `sed | grep` of `SYSTEM-MAP.md` — map text alone, 33 lines,
   14,815 bytes — into a file in the scratchpad, then removed it with the next command and read the same lines from
   the map directly. It held no output of the TZ's steps and no venue data.
2. **`logs/00-worktree.log` was written after §0.0's `mkdir`**, since `logs/` did not exist before it; it records the
   command and its `exit=0`.
3. **The refs logs' "lines that differ" were composed by the Executor**, since no mode prints them. `logs/05-refs.log`
   holds `ls-remote`'s output whole, its counts by prefix (`awk`), and the lines that differ from map §1's read: `HEAD`
   and `main`, which the map names, and one tag, the newest `rewardbook-streams-1795818620`. The map counts 179 tags
   but names none of the reward book's after `1795332620`, so that this tag is the one new since its read is inferred
   from its being the newest. `logs/313-refs.log`'s difference from §0.5's read was computed by a short script; its
   first version counted the lines appended to `05-refs.log` twice and was rewritten in place before it was used.
4. **§3.1:** the commit message is the TZ's, verbatim, so it carries no attribution trailer; git took the committer
   identity `root@vultr.guest` by default. The TZ gives no body for pull request #55; the Executor wrote a two-line one
   naming the TZ and the file's SHA-256. `logs/31-branch.log` was written under `set -x`, and adds a `date -u` after
   the push (map §7 item 63's instant) and `git rev-parse HEAD`; `logs/31-pr.log` adds a `gh pr view 54` read of the
   closed pull request.
5. **Waits.** §3.6's clock wait has its own log, `logs/36-wait.log`; it printed `Fri Nov 27 11:07:40 PM UTC 2026` at
   once, the instant long past. §3.12's 120 s were waited by an until-loop on the clock in the same background command
   that then ran `verify` (`verify`'s first line at 00:28:35, 130 s after B-UPLOAD's date). `rehearse`, `frame`,
   `draw`, `redraw` and `verify` ran in the background (map §6, harness); the Executor polled their logs, and the
   harness kept its own copies of their output under the session's directory.
6. **The fingerprint table of §0** was built from `logs/02-fingerprint.log` by `awk` into `/root/tz56a-work/draft-fp.md`,
   a file of the work tree the TZ does not name, removed with the tree.
7. **Nothing was refused by the permission classifier**: B-RECLAIM-SCRATCH, B-UPLOAD and B-RECLAIM-OWN all ran in the
   session; nothing was handed to the Boss.
8. **Polymarket's Data API answered `500` eleven times during `draw`** (§2.4), each served on its second try by
   `Net`'s retry; the TZ provides for it, and it is listed here only because it is the run's one venue refusal.
9. **B-RECLAIM-OWN's output went to the terminal, not into the scratchpad** as §9 item 3 asks: the paste was run
   verbatim, without a redirect. Its three lines, quoted whole in §2.11, were written by the Executor to
   `b-reclaim-own.log` in the scratchpad right after, followed by a `date -u` line (`Sat Nov 28 12:34:02 AM UTC 2026`).
10. **The reclaim log's forensic copy is partial** (§2.11): `reclaim` copies `logs/9-reclaim.log` while writing it, so
    the copy holds its first 36 lines; the whole log is quoted above, as the Executor read it before B-RECLAIM-OWN.
    The quote was staged in `/root/tz56a-work/reclaim-quote.txt`, a file of the work tree the TZ does not name,
    written after `reclaim` ran and removed with the tree.
11. **The report's draft was written before `reclaim` with three gaps** — the reclaim log, B-RECLAIM-OWN's output and
    V14 — filled after them, as §9 orders; every SHA-256 it names was in the draft `reclaim` read.
