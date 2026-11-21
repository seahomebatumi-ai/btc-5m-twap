# TZ-53 — L1's unit: rule W live at the minimum size from the live host in Sofia — REPORT

**Status: G-DEPLOY PASS. `B-DEPLOY END exit=0` at 08:52:35 UTC on 2026-11-21. L1's unit, `l1-bot.service`, is
installed, enabled and running on the live host, MainPID `49171`, `NRestarts` `0`, since 08:37:35 UTC. Before it
started, its own code proved its order path and its stop: G-PROVE PASS, eight gates of eight, on the kinds CTF and
CTF negative-risk. The Boss pressed «Стоп» `7.1` s after the bot asked.**

- **Every gate before B-DEPLOY passed:**
  - FINGERPRINT PASS twice, revision `2026-11-21-c`, 64 of 64 `frozen` rows equal.
  - §0.1's script staged six files `created`, then wrote the branch's three `created`, each at §0.1's SHA-256. The
    live host's copies hash the same.
  - Host gate 7 of 7. The room margin is **2,709,101,732** bytes.
  - NUMBER PASS 2 of 2, twice. Refs read 205 lines, and the branch was absent before the push.
  - Access `exit=0`, the pinned key, `vs-2348`, `root`, both trees absent.
  - The live host gate 5 of 5. **LS held:** root's keys are the Executor's alone, the nine `PATH` lines are
    §0.6's, and `43-l1-before.log` reads §0.6's three names, `svc exit=1`, `unit exit=1`, both units `inactive`.
  - G-GEO PASS, `blocked False`, `BG`.
  - G-SSH 6 of 6, before and after.
  - The checker's `SELFTEST PASS: 141 checks, 141 passed`, `refused by the hook: 5`, on both hosts.
  - G-ENV installed PASS. The checker's `SDK SELFTEST PASS: 32 checks, 32 passed`, `refused by the hook: 2`.
  - G-KEY present, kept.
  - **E-SELF:** the engine's `SELFTEST PASS: 38 checks, 38 passed; refused by the hook: 0` and
    `SDK SELFTEST PASS: 29 checks, 29 passed; refused by the hook: 2`.
- **B-DEPLOY, every step PASS** (`60-deploy.log`, §2.1):
  - **G-INSTALL:** the four files and the unit file are installed at §0.1's SHA-256, the unit file equal to the
    code's copy by `cmp`, `loaded`, `disabled`.
  - **G-READY** failed its first read on the capital check alone: `79.962913` pUSD on chain, under `80`. The
    Boss was told once in Russian. The second read, 600 s later, gave `83.455340` and **`G-READY PASS: 6 of 6, G-GEO
    PASS`**.
  - **G-PROVE PASS** at 08:36:49, its record `/var/lib/l1-bot/prove-1.json`, `3894` bytes, `0600`:
    - G-GEO, G-READY and G-TG PASS.
    - G-SELECT PASS: 150 members, 41 candidates, 26 of them CTF and 15 negative-risk.
    - G-POLL PASS. G-WS PASS: 2 of 2 books seeded.
    - **G-RT PASS on both kinds:** each order was placed live (226 and 197 ms), seen in the wallet's open orders,
      cancelled by its id and seen gone. Neither filled, and the balance stayed `83.455340` → `83.455340`.
    - **G-HB, recorded:** a heartbeat was accepted, and the venue cancelled the order itself `13.7` s after the
      last one.
    - **G-STOP PASS:** «Стоп» was pressed after `7.1` s; 1 order cancelled, 0 open after, the stop record written.
    - Orders placed: 4. None filled.
  - **G-HOLD PASS:** started with the drill's record standing, the unit read `ExecMainStatus=3`, `NRestarts=0` and
    `failed` 45 s on. Its own lines were `SERVE the stop record stands` and `lookups 0, requests 0`.
  - **G-CLEAR:** the record was moved into `stops/`.
  - **G-UNIT PASS** at 60 s: `active`, `NRestarts=0`, `enabled`, `SERVE start: geoblock PASS BG`.
  - **G-LIVE PASS** at 900 s: `active`, `NRestarts=0`, the same MainPID, no stop record.
- **The unit after** (§3 step 11): `active`, `NRestarts` `0`, its files at §0.1's SHA-256, and its prove's record
  whole. Its start equity is `83.455340` pUSD, and the loss limit stops it `25` pUSD below that. In its first 15
  minutes its journal counted 105 orders placed and 104 cancelled, 1 fill, and 1 market held (`62-unit-after.log`).
- **Branch** `tz-53-l1-unit` at `3a2e6f293b716fdcf12d4d7089461cdcdb179c17`: three paths, `29 0`, `3656 0` and
  `3324 0`. **Pull request #51** is open. **Pull request #50** was read `open`, `merged` `false`, head `1719ff4…`,
  and closed unmerged by `gh api` at 08:23:49; its branch is kept. The §4.2 self-check read `0`, three paths, and
  nothing.
- **G-PRINT `0` and `0`.** TZ-52's copy `/var/lib/l1-bot/tz52-l1-account.py` was read at `a425e67c…` and
  removed. TZ-51's copy stays for B-REVOKE.
- **The capture host:** no unit was touched, and the recorder, the reward book and the advisor kept the same
  `MainPID`, `NRestarts` and `ActiveState`.
- **Asked of the Boss:** the top-up, once (§3 step 10), and «Стоп», whose line was given once before B-DEPLOY and
  repeated once while G-PROVE ran (§6 item 3). No block was handed over, and the classifier refused nothing.
- No address of either host, of the bot's owner, wallet or session key, and no key, token, relayer key, signature,
  order id or chat id is in this report. Of the live host's name, only its first label is given.

---

## 0. Fingerprint

`I0 fingerprint` (`logs/02-fingerprint.log`, 07:40:02 UTC) and `I fingerprint` from the branch's worktree
(`logs/12-fingerprint.log`, 08:23:31 UTC) each printed `FINGERPRINT PASS`. With the instants and the peak stripped,
their lines are equal (`diff` exit `0`).

```
FINGERPRINT PASS: revision 2026-11-21-c; anchors 6 of 6, 4 re-derived; rows 67: frozen 64 of 64 equal, tracked 2, reported 1; the signing page on main equal to TZ-50's Appendix B
```

This is §0.2's line, word for word. **Revision string:** `2026-11-21-c`. **Anchors:**

| anchor | read | how |
|---|---|---|
| `A1` | `229a944f2d51` | the map |
| `A2` | `6c5089330629` | the map; re-derived from `research/twap-divergence.py` |
| `A3` | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` | the map |
| `A4` | `6ac6e10aeabc` | the map; re-derived from `BTC-EXECUTOR-INSTRUCTIONS.md` |
| `A5` | `0f6c90451cbd` | the map; re-derived from `research/recorder/recorder.py` |
| `A6` | `729f0bcdbee3` | the map; re-derived from `research/pfair.py` |

**Every row of the map's §0 table**, as `fingerprint` printed it: 67 rows, 64 `frozen` and each equal, 2 `tracked`,
1 `reported`. `docs/l1-sign.html` on `main` is equal to TZ-50's Appendix B, `11846` bytes, `f1d92e7d…`.

| path | lines | bytes | state | SHA-256 |
|---|---|---|---|---|
| `SYSTEM-MAP.md` | 1092 | 189704 | reported | `982b56f46293bf5f137d23b13ecaed24369a6702445d2a79f1bb71d0205281a6` |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 235 | 11255 | frozen, equal | `6ac6e10aeabc3bf83926c509e6d5f868998918f34e32e7e3882e95aad83e2617` |
| `research/twap-divergence.py` | 1135 | 50928 | frozen, equal | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` |
| `research/selftest-twap-divergence.py` | 376 | 16736 | frozen, equal | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` |
| `research/tz02-distribution.py` | 334 | 14511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` |
| `research/pfair.py` | 441 | 19357 | frozen, equal | `729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68` |
| `research/selftest-pfair.py` | 619 | 32559 | frozen, equal | `b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa` |
| `research/tz06-calibration.py` | 577 | 27138 | frozen, equal | `715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f` |
| `research/tz07a-variance-time.py` | 623 | 28414 | frozen, equal | `513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771` |
| `research/tz07b-settlement-dispersion.py` | 515 | 24926 | frozen, equal | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` |
| `research/tz08a-out-of-sample.py` | 745 | 38822 | frozen, equal | `37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c` |
| `research/tz09-disk-inventory.py` | 894 | 41004 | frozen, equal | `b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6` |
| `research/tz10b-sigma-or-link.py` | 1224 | 61018 | frozen, equal | `406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088` |
| `research/tz11a-student-link.py` | 1231 | 64732 | frozen, equal | `0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839` |
| `research/tz12-sized-gate.py` | 1157 | 61637 | frozen, equal | `d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999` |
| `research/tz13-sized-gate-test3.py` | 1074 | 53901 | frozen, equal | `a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd` |
| `research/tz14-quote-inventory.py` | 2124 | 109972 | frozen, equal | `978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02` |
| `research/tz15-phase2-gate.py` | 1517 | 73799 | frozen, equal | `66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3` |
| `research/tz16a-phase2-decisive-gate.py` | 2198 | 111192 | frozen, equal | `3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125` |
| `research/tz17-settlement-chain.py` | 1102 | 38622 | frozen, equal | `e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92` |
| `research/tz18a-chainbook-capture.py` | 1683 | 69517 | frozen, equal | `e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae` |
| `research/tz20-capture-under-systemd.py` | 771 | 36528 | frozen, equal | `104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7` |
| `research/tz21-recorder-memory.py` | 1284 | 59009 | frozen, equal | `d6d2dc195809f2160fda7856980d8ccfbf0006ba0836943ff789c877f9d5795f` |
| `research/tz23-maker-m0.py` | 1184 | 54885 | frozen, equal | `6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f` |
| `research/tz24-nesting-b2.py` | 1535 | 76142 | frozen, equal | `4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b` |
| `research/tz26-nesting-b3-capture.py` | 2492 | 118466 | frozen, equal | `caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec` |
| `research/tz27-pairbook-archive.py` | 2078 | 106284 | frozen, equal | `2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673` |
| `research/tz28-pairbook-archive-timer.py` | 1438 | 74576 | frozen, equal | `46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4` |
| `research/tz29-maker-m0-second-look.py` | 1225 | 68959 | frozen, equal | `18defff93d08c13ea4638a518c88a3fec5541fcf53fb6827451e727f2204d905` |
| `research/tz30-nesting-b3-measure.py` | 2518 | 131119 | frozen, equal | `93dbbf1c4f84553a7bc041387ef92c3c0d8747c384d383b4fcd0b247fcd131ab` |
| `research/tz31-who-earns.py` | 1523 | 84775 | frozen, equal | `7073188c8fbaa19568e8c6e4d6379e40ea57cf2a1341ebde0ea6a08f2c544765` |
| `research/tz32-our-quoting.py` | 2576 | 138209 | frozen, equal | `6ec367e6ed995b315063d2d808dd6a3995878011afd76abfbb7b106b645a9c61` |
| `research/tz33-reward-book-capture.py` | 3542 | 175160 | frozen, equal | `a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670` |
| `research/tz34-rewardbook-archive-timer.py` | 1791 | 99388 | frozen, equal | `1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72` |
| `research/tz35-advisor-deploy.py` | 802 | 42049 | frozen, equal | `d50787db5113c3f748806a60a3e71211b665cb5235296e43d0e9a747a529e6f5` |
| `research/tz36-advisor-trust.py` | 582 | 32925 | frozen, equal | `a0fb9d53afe435d37354862eb8fd299256bf551fdbdb25a5c828d2cc7376d4f5` |
| `research/tz37-capital-allocation.py` | 808 | 51269 | frozen, equal | `eec1f30b971ed1d6db31e27eb0c321276c1b107a1654e013996d023b1a6a04eb` |
| `research/tz38-adv3-pit-validation.py` | 1782 | 90181 | frozen, equal | `579474b65329662f7bed735994381241a928a2c65a726cec3f933dc7afd4427b` |
| `research/tz39-advisor-checks.py` | 1139 | 73892 | frozen, equal | `18294b0916d77b226083a18f9521f06e2fddb423bbc947a2e1100fd42b2980f3` |
| `research/tz40-advisor-strong.py` | 1436 | 95474 | frozen, equal | `4403b27185f7e9aaa090dedfca457af6c4f70b6b020f0d2fcd9f9fbb96b6054b` |
| `research/tz42-advisor-registry.py` | 2088 | 134077 | frozen, equal | `b6c45490b2f86f5c4678c645041ef1556b1199a6bc814470de904aedf7f5105f` |
| `research/tz43-l0-our-quote.py` | 3056 | 152905 | frozen, equal | `48c3550b3f9a990fa8bc43ad8464b181ec2eb0a086b3b6f3a0ceed52da4a30cf` |
| `research/tz44-l0-inputs-release.py` | 1616 | 90703 | frozen, equal | `0b78807d9c5dec087138b0c9a329cb8c976157ab5c8a3fd4deee7cb31e89e190` |
| `research/tz45-l0-rule-w.py` | 4299 | 233655 | frozen, equal | `4720e78573e54b1325dd24af7c30e0de59bfb4c1879d309a23fa6bab6b32d2d4` |
| `research/tz46-capture-room.py` | 1644 | 88254 | frozen, equal | `363b269c462d14da1656feb7bad92fec43adb1593209131fe5ca6e5c9f6755f6` |
| `research/tz49-live-host.py` | 2127 | 113254 | frozen, equal | `efcc5ead077b396fe18d243f3c65fa9824baca56e6db5312058971e0dfe6049b` |
| `docs/l1-sign.html` | 218 | 11846 | frozen, equal | `f1d92e7dd8a8cd15b7b96b86b357ebf80db4e10844b3fc269e92cef0aecba528` |
| `research/recorder/recorder.py` | 651 | 27821 | frozen, equal | `0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7` |
| `research/recorder/config.py` | 112 | 4773 | frozen, equal | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` |
| `research/recorder/manifest.py` | 254 | 10002 | frozen, equal | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` |
| `research/recorder/analyze.py` | 813 | 34705 | frozen, equal | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` |
| `research/recorder/probe.py` | 227 | 9324 | frozen, equal | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` |
| `research/recorder/selftest.py` | 573 | 30591 | frozen, equal | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` |
| `deploy/systemd/btc-recorder.service` | 23 | 707 | frozen, equal | `3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1` |
| `deploy/systemd/btc-chainbook.service` | 22 | 724 | frozen, equal | `a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2` |
| `deploy/systemd/btc-pairbook.service` | 22 | 761 | frozen, equal | `ba02fe4175b961c387ea8066eb084704e69efc7fd0a48d8f623a0198334f8dd8` |
| `deploy/systemd/btc-pairbook-archive.service` | 17 | 794 | frozen, equal | `2e7fd45382af3da3b2ec29ced8d69870ef3d4481da4c6f327b90fc6cb5af78e7` |
| `deploy/systemd/btc-pairbook-archive.timer` | 13 | 417 | frozen, equal | `07581f4f331fbf9d2a1113cac42a2872d65ac69a872991bff7d2bda235eac913` |
| `deploy/systemd/btc-rewardbook.service` | 23 | 817 | frozen, equal | `7691720c7b2261a606af54bfa20b5068b89455ea54512c55dde861d6d8063bec` |
| `deploy/systemd/btc-rewardbook-archive.service` | 17 | 810 | frozen, equal | `a9abb1f092b3fb8359d37ea88df00dca8557d0f0482d04c12f0fbdd32601e33f` |
| `deploy/systemd/btc-rewardbook-archive.timer` | 12 | 435 | frozen, equal | `7b0804285af6987340838bd59573897d013cf97edc5d4132cda7f3f9ba3e3824` |
| `deploy/systemd/adv3-bot.service` | 27 | 863 | frozen, equal | `82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66` |
| `advisor/RULE-ADV-3.txt` | 33 | 3203 | frozen, equal | `ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169` |
| `advisor/adv3.py` | 895 | 51834 | frozen, equal | `81ef0112d3fe4b86566e51a51aab924d9776ff37a927e65982ecb0bb7c1f34e1` |
| `advisor/adv3-bot.py` | 2548 | 157438 | frozen, equal | `c3d9fff54f3585cfc4c33b5f7e1f93b390e62b03e0b4725fee2d6fdda6d04c11` |
| `advisor/selftest-adv3.py` | 256 | 19111 | frozen, equal | `6f29b82f2b2ca82cd2ff4bbb370e032354dbb4743497330530777429b3af7398` |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` |

**The model:** TZ-53's header names Claude Opus 5.5. The session's own record, read at the start of the run, names
`claude-opus-5-5` as configured and as last served.

---

## 1. Input

Nothing was re-collected: this TZ measures no dataset. What it read:

- **The repository at `main` `04f0a15`**, the Boss's upload of `SYSTEM-MAP.md` revision `2026-11-21-c` and
  `CryptoTZ/TZ-53-l1-unit.md`:
  - TZ-53, TZ-52 and TZ-51, and `research/tz33-reward-book-capture.py` and `research/tz45-l0-rule-w.py`, by §0.1's
    script;
  - the map's 67 rows' files and `docs/l1-sign.html`, by `fingerprint`;
  - `CryptoTZ/` and `CryptoReports/`, by `number`;
  - `origin`'s refs, by `refs`.
- **The staged files**, §0.1's script into `/root/tz53-work/stage/`, each `created` at §0.1's table's SHA-256
  (`01-stage.log`, §2.8). TZ-52's instrument was first made in a scratch directory at `a425e67c…`, then removed.
- **The live host's account**, read through the session key by the engine's `ready` and `prove` (§2.1 to §2.3):
  - the wallet's pUSD on chain and the CLOB's view of it;
  - the allowances to the three exchanges, each `max`, and the position approvals, each `True`;
  - the key's open orders, `0`, and closed-only mode;
  - the key's validity, from `account.json`.
- **The venue's anonymous reads**, by the prove and the unit:
  - the geoblock;
  - the day's selection by TZ-33's rule, 150 members from 189 requests, kept under `/var/lib/l1-bot/select/`;
  - the candidates' reward documents, under `polls/`;
  - the market channel.
- **This report prints of those reads:**
  - slugs and counts;
  - the unit's own orders, at the lowest price their tick allows;
  - the wallet's own balances and allowances.

  It prints no price, size, rate, competitiveness or outcome of another participant (TZ-53 §2 item 4).

---

## 2. Measurements

Every live host's log below is quoted whole, as §3.10's copy brought it back byte for byte (`diff exit=0`, §2.7).
Its SHA-256 is in §2.10.

### 2.1 B-DEPLOY — `59-deploy-start.log` and `60-deploy.log`, whole

The Executor started B-DEPLOY under `systemd-run` at 08:25:36. The transient unit read `inactive` after
`B-DEPLOY END exit=0` (`exit=4` is `systemctl is-active`'s code for that).

```
2026-11-21T08:25:36.240584943Z
Running as unit: tz53-deploy.service; invocation ID: 044a45829dcc4d8fba9462fb82228ac0
exit=0
2026-11-21T08:52:49.468671374Z
inactive
exit=4
```

**`60-deploy.log`, whole** (CANON hard rule 16):

```
2026-11-21T08:25:36.969Z B-DEPLOY BEGIN pid 47526 on vs-2348
l1-bot.py: OK
tz33-reward-book-capture.py: OK
tz45-l0-rule-w.py: OK
l1-bot.service: OK
l1-bot.py: OK
tz33-reward-book-capture.py: OK
tz45-l0-rule-w.py: OK
l1-bot.service: OK
-rw-r--r-- 1 root root 1014 Nov 21 08:25 /etc/systemd/system/l1-bot.service

/root/l1-bot-svc:
total 604
drwx------ 2 root root   4096 Nov 21 08:25 .
drwx------ 8 root root   4096 Nov 21 08:25 ..
-rw------- 1 root root 188968 Nov 21 08:25 l1-bot.py
-rw------- 1 root root   1014 Nov 21 08:25 l1-bot.service
-rw------- 1 root root 175160 Nov 21 08:25 tz33-reward-book-capture.py
-rw------- 1 root root 233655 Nov 21 08:25 tz45-l0-rule-w.py
2026-11-21T08:25:37.310Z B-DEPLOY installed: MainPID=0 Result=success NRestarts=0 ExecMainStatus=0 ActiveState=inactive SubState=dead UnitFileState=disabled 
[2026-11-21T08:25:37Z] MemAvailable 1440124928 bytes, floor 274917678; available on / 16911478784 bytes, floor 2447483648
[2026-11-21T08:25:39Z] G-GEO over IPv4: PASS, country 'BG', status 200
[2026-11-21T08:25:39Z] READY pUSD on chain 79.962913, the CLOB's view 79.962913; allowances {'c': 'max', 'n': 'max', 'v': 'max'}; position approvals {'c': True, 'n': True, 'v': True}; open orders of the key 0
[2026-11-21T08:25:39Z] READY kinds the unit may buy on: ['c', 'n', 'v']; may sell on: ['c', 'n', 'v']
[2026-11-21T08:25:39Z] G-READY a Deposit Wallet signed for by the session key: PASS
[2026-11-21T08:25:39Z] G-READY not in closed-only mode: PASS
[2026-11-21T08:25:39Z] G-READY the standard exchange's pUSD allowance the maximum: PASS
[2026-11-21T08:25:39Z] G-READY the key authorized 7 days ahead at least: PASS
[2026-11-21T08:25:39Z] G-READY no open order of the wallet by the key: PASS
[2026-11-21T08:25:39Z] G-READY its pUSD on chain from 80.00 to 150.00: FAIL
[2026-11-21T08:25:39Z] G-READY FAIL: 5 of 6, G-GEO PASS
[2026-11-21T08:25:39Z] peak memory of this run: 91856896 bytes; refused by the hook: 0; lookups 5, requests 8
2026-11-21T08:25:40.121Z B-DEPLOY G-READY read 1: the wallet's pUSD outside 80 to 150 alone; read again in 600 s
[2026-11-21T08:35:40Z] MemAvailable 1441431552 bytes, floor 274917678; available on / 16911491072 bytes, floor 2447483648
[2026-11-21T08:35:41Z] G-GEO over IPv4: PASS, country 'BG', status 200
[2026-11-21T08:35:42Z] READY pUSD on chain 83.455340, the CLOB's view 83.455340; allowances {'c': 'max', 'n': 'max', 'v': 'max'}; position approvals {'c': True, 'n': True, 'v': True}; open orders of the key 0
[2026-11-21T08:35:42Z] READY kinds the unit may buy on: ['c', 'n', 'v']; may sell on: ['c', 'n', 'v']
[2026-11-21T08:35:42Z] G-READY a Deposit Wallet signed for by the session key: PASS
[2026-11-21T08:35:42Z] G-READY not in closed-only mode: PASS
[2026-11-21T08:35:42Z] G-READY the standard exchange's pUSD allowance the maximum: PASS
[2026-11-21T08:35:42Z] G-READY the key authorized 7 days ahead at least: PASS
[2026-11-21T08:35:42Z] G-READY no open order of the wallet by the key: PASS
[2026-11-21T08:35:42Z] G-READY its pUSD on chain from 80.00 to 150.00: PASS
[2026-11-21T08:35:42Z] G-READY PASS: 6 of 6, G-GEO PASS
[2026-11-21T08:35:42Z] peak memory of this run: 91979776 bytes; refused by the hook: 0; lookups 5, requests 8
2026-11-21T08:35:42.852Z B-DEPLOY G-PROVE: the bot asks the Boss in Telegram to press «Стоп» once its drill's order rests
[2026-11-21T08:35:42Z] MemAvailable 1409470464 bytes, floor 274917678; available on / 16911486976 bytes, floor 2447483648
[2026-11-21T08:35:43Z] PROVE clock NTP-synchronized: True
[2026-11-21T08:36:49Z] PROVE record /var/lib/l1-bot/prove-1.json: 3894 bytes, 0600
[2026-11-21T08:36:49Z] PROVE G-GEO {'reading': 'PASS', 'country': 'BG', 'status': 200}; pUSD on chain 83.455340, the CLOB's view 83.455340; allowances {'c': 'max', 'n': 'max', 'v': 'max'}; position approvals {'c': True, 'n': True, 'v': True}; open orders of the key 0
[2026-11-21T08:36:49Z] PROVE G-READY a Deposit Wallet signed for by the session key: PASS
[2026-11-21T08:36:49Z] PROVE G-READY not in closed-only mode: PASS
[2026-11-21T08:36:49Z] PROVE G-READY the standard exchange's pUSD allowance the maximum: PASS
[2026-11-21T08:36:49Z] PROVE G-READY the key authorized 7 days ahead at least: PASS
[2026-11-21T08:36:49Z] PROVE G-READY no open order of the wallet by the key: PASS
[2026-11-21T08:36:49Z] PROVE G-READY its pUSD on chain from 80.00 to 150.00: PASS
[2026-11-21T08:36:49Z] PROVE select {'members': 150, 'candidates': 41, 'requests': 189, 'kinds': {'n': 15, 'c': 26}, 'picked': ['c', 'n']}; poll {'served': True, 'row': True}; ws {'tokens': 2, 'seeded': 2, 'frames': 2}
[2026-11-21T08:36:49Z] PROVE G-RT CTF (will-ai-solve-the-riemann-hypothesis-in-2026): placements [(0, 'live', 226, None)]; seen in 5 reads {'price': True, 'size': True, 'side BUY': True, 'the token': True, 'nothing matched': True}; cancel {'canceled': True, 'not_canceled': 0, 'words': []}; gone in 2 reads; matched 0; balance 83.455340 -> 83.455340
[2026-11-21T08:36:49Z] PROVE G-RT c placed live: PASS
[2026-11-21T08:36:49Z] PROVE G-RT c seen in the wallet's open orders: PASS
[2026-11-21T08:36:49Z] PROVE G-RT c cancelled by its id: PASS
[2026-11-21T08:36:49Z] PROVE G-RT c seen gone from them: PASS
[2026-11-21T08:36:49Z] PROVE G-RT c no fill in its trades: PASS
[2026-11-21T08:36:49Z] PROVE G-RT c the wallet's pUSD on chain unchanged: PASS
[2026-11-21T08:36:49Z] PROVE G-RT CTF negative-risk (will-dcampion-be-the-first-kick-streamer-to-finish-gta-vi-by-december-31-2026): placements [(0, 'live', 197, None)]; seen in 2 reads {'price': True, 'size': True, 'side BUY': True, 'the token': True, 'nothing matched': True}; cancel {'canceled': True, 'not_canceled': 0, 'words': []}; gone in 2 reads; matched 0; balance 83.455340 -> 83.455340
[2026-11-21T08:36:49Z] PROVE G-RT n placed live: PASS
[2026-11-21T08:36:49Z] PROVE G-RT n seen in the wallet's open orders: PASS
[2026-11-21T08:36:49Z] PROVE G-RT n cancelled by its id: PASS
[2026-11-21T08:36:49Z] PROVE G-RT n seen gone from them: PASS
[2026-11-21T08:36:49Z] PROVE G-RT n no fill in its trades: PASS
[2026-11-21T08:36:49Z] PROVE G-RT n the wallet's pUSD on chain unchanged: PASS
[2026-11-21T08:36:49Z] PROVE G-HB accepted True; sends 1, refused 0; gone after 13.7 s; {'a heartbeat accepted': 'PASS', 'placed live and seen': 'PASS', 'gone by the venue within 40 s of the last heartbeat': 'PASS', 'no fill': 'PASS', 'the balance unchanged': 'PASS'}
[2026-11-21T08:36:49Z] PROVE G-STOP pressed after 7.1 s; stop {'canceled': 1, 'open_after': 0, 'written': True}; matched 0; {'placed live and seen': 'PASS', '«Стоп» pressed': 'PASS', 'every order cancelled and read gone': 'PASS', 'the stop record written': 'PASS', 'no fill': 'PASS', 'the balance unchanged': 'PASS'}
[2026-11-21T08:36:49Z] PROVE G-GEO: PASS
[2026-11-21T08:36:49Z] PROVE G-READY: PASS
[2026-11-21T08:36:49Z] PROVE G-TG: PASS
[2026-11-21T08:36:49Z] PROVE G-SELECT: PASS
[2026-11-21T08:36:49Z] PROVE G-POLL: PASS
[2026-11-21T08:36:49Z] PROVE G-WS: PASS
[2026-11-21T08:36:49Z] PROVE G-RT: PASS
[2026-11-21T08:36:49Z] PROVE G-STOP: PASS
[2026-11-21T08:36:49Z] G-PROVE PASS; kinds proved ['c', 'n']; heartbeat accepted True; orders placed 4; last cancel_all not needed: the stop cancelled
[2026-11-21T08:36:49Z] peak memory of this run: 122187776 bytes; refused by the hook: 0; lookups 18, requests 212
2026-11-21T08:36:49.626Z B-DEPLOY started with the stop record standing, exit=0; read in 45 s
2026-11-21T08:37:34.648Z B-DEPLOY G-HOLD read: MainPID=0 Result=exit-code NRestarts=0 ExecMainStatus=3 ActiveState=failed SubState=failed UnitFileState=disabled 
[2026-11-21T08:37:34Z] UNIT hold: file installed byte for byte: True; LoadState=loaded; UnitFileState=disabled; ActiveState=failed; SubState=failed; Result=exit-code; ExecMainStatus=3; ExecMainCode=1; NRestarts=0; MainPID=0; ActiveEnterTimestamp=Sat 2026-11-21 08:36:49 UTC; InactiveEnterTimestamp=Sat 2026-11-21 08:36:49 UTC; MemoryCurrent=[not set]; MemoryPeak=[not set]; Restart=on-failure; NeedDaemonReload=no
[2026-11-21T08:37:34Z] peak memory of this run: 34807808 bytes; refused by the hook: 0; lookups 0, requests 0
[2026-11-21T08:36:49Z] SERVE the stop record stands (drill at 2026-11-21T08:36:49Z): no request, exit 3
[2026-11-21T08:36:49Z] peak memory of this run: 34680832 bytes; refused by the hook: 0; lookups 0, requests 0
2026-11-21T08:37:34.844Z B-DEPLOY G-HOLD PASS
[2026-11-21T08:37:34Z] CLEAR the stop record (drill at 2026-11-21T08:36:49Z) moved to /var/lib/l1-bot/stops/stop-1795250209.json
[2026-11-21T08:37:35Z] CLEAR the chat's pending updates consumed: 1
[2026-11-21T08:37:35Z] peak memory of this run: 45703168 bytes; refused by the hook: 0; lookups 1, requests 3
Created symlink /etc/systemd/system/multi-user.target.wants/l1-bot.service -> /etc/systemd/system/l1-bot.service.
2026-11-21T08:37:35.653Z B-DEPLOY enabled and started; read in 60 s
2026-11-21T08:38:35.674Z B-DEPLOY G-UNIT read: MainPID=49171 Result=success NRestarts=0 ExecMainStatus=0 ActiveState=active SubState=running UnitFileState=enabled 
[2026-11-21T08:38:35Z] UNIT start: file installed byte for byte: True; LoadState=loaded; UnitFileState=enabled; ActiveState=active; SubState=running; Result=success; ExecMainStatus=0; ExecMainCode=0; NRestarts=0; MainPID=49171; ActiveEnterTimestamp=Sat 2026-11-21 08:37:35 UTC; InactiveEnterTimestamp=; MemoryCurrent=88735744; MemoryPeak=103886848; Restart=on-failure; NeedDaemonReload=no
[2026-11-21T08:38:35Z] peak memory of this run: 34820096 bytes; refused by the hook: 0; lookups 0, requests 0
[2026-11-21T08:38:35Z] STATUS stop record: none
[2026-11-21T08:38:35Z] STATUS prove-1.json: code 98851b3c0df4, pass True, kinds ['c', 'n'], heartbeat accepted True, orders 4
[2026-11-21T08:38:35Z] STATUS state: start equity 83.455340 at 2026-11-21T08:37:38Z; started 2026-11-21T08:37:38Z; held 0; reports ['2026-11-20']
[2026-11-21T08:38:35Z] STATUS journal 2026-11-21.jsonl: 110 lines, last 2026-11-21T08:38:32Z; {'canceled': 18, 'clear': 1, 'geo': 1, 'place': 20, 'placed': 20, 'poll': 42, 'report': 1, 'select': 1, 'sent': 2, 'start': 1, 'stop': 1, 'stream': 2}
[2026-11-21T08:38:35Z] peak memory of this run: 34828288 bytes; refused by the hook: 0; lookups 0, requests 0
2026-11-21T08:38:36.009Z B-DEPLOY G-UNIT PASS
2026-11-21T08:38:36.025Z B-DEPLOY G-LIVE read in 839 s
2026-11-21T08:52:35.040Z B-DEPLOY G-LIVE read: MainPID=49171 Result=success NRestarts=0 ExecMainStatus=0 ActiveState=active SubState=running UnitFileState=enabled 
[2026-11-21T08:52:35Z] UNIT live: file installed byte for byte: True; LoadState=loaded; UnitFileState=enabled; ActiveState=active; SubState=running; Result=success; ExecMainStatus=0; ExecMainCode=0; NRestarts=0; MainPID=49171; ActiveEnterTimestamp=Sat 2026-11-21 08:37:35 UTC; InactiveEnterTimestamp=; MemoryCurrent=91693056; MemoryPeak=103886848; Restart=on-failure; NeedDaemonReload=no
[2026-11-21T08:52:35Z] peak memory of this run: 34803712 bytes; refused by the hook: 0; lookups 0, requests 0
[2026-11-21T08:52:35Z] STATUS stop record: none
[2026-11-21T08:52:35Z] STATUS prove-1.json: code 98851b3c0df4, pass True, kinds ['c', 'n'], heartbeat accepted True, orders 4
[2026-11-21T08:52:35Z] STATUS state: start equity 83.455340 at 2026-11-21T08:37:38Z; started 2026-11-21T08:37:38Z; held 1; reports ['2026-11-20']
[2026-11-21T08:52:35Z] STATUS journal 2026-11-21.jsonl: 450 lines, last 2026-11-21T08:52:20Z; {'cancel-refused': 2, 'canceled': 103, 'clear': 1, 'fill': 1, 'foreign': 1, 'geo': 1, 'place': 104, 'placed': 104, 'poll': 124, 'report': 1, 'select': 1, 'sent': 3, 'start': 1, 'stop': 1, 'stream': 2}
[2026-11-21T08:52:35Z] peak memory of this run: 34824192 bytes; refused by the hook: 0; lookups 0, requests 0
2026-11-21T08:52:35.391Z B-DEPLOY G-LIVE PASS
2026-11-21T08:52:35.392Z B-DEPLOY END exit=0
```

### 2.2 G-READY — every `61-ready-N.log`, whole

Read 1, 08:25:39: the capital check alone `FAIL`, `79.962913` pUSD on chain. B-DEPLOY waited 600 s, and the
Executor told the Boss once, at about 08:26 UTC, «Пополните кошелёк бота: на нём должно быть от 80 до 150 pUSD, сейчас
79.962913». Read 2, 08:35:42: `83.455340`, PASS 6 of 6.

```
[2026-11-21T08:25:37Z] MemAvailable 1440124928 bytes, floor 274917678; available on / 16911478784 bytes, floor 2447483648
[2026-11-21T08:25:39Z] G-GEO over IPv4: PASS, country 'BG', status 200
[2026-11-21T08:25:39Z] READY pUSD on chain 79.962913, the CLOB's view 79.962913; allowances {'c': 'max', 'n': 'max', 'v': 'max'}; position approvals {'c': True, 'n': True, 'v': True}; open orders of the key 0
[2026-11-21T08:25:39Z] READY kinds the unit may buy on: ['c', 'n', 'v']; may sell on: ['c', 'n', 'v']
[2026-11-21T08:25:39Z] G-READY a Deposit Wallet signed for by the session key: PASS
[2026-11-21T08:25:39Z] G-READY not in closed-only mode: PASS
[2026-11-21T08:25:39Z] G-READY the standard exchange's pUSD allowance the maximum: PASS
[2026-11-21T08:25:39Z] G-READY the key authorized 7 days ahead at least: PASS
[2026-11-21T08:25:39Z] G-READY no open order of the wallet by the key: PASS
[2026-11-21T08:25:39Z] G-READY its pUSD on chain from 80.00 to 150.00: FAIL
[2026-11-21T08:25:39Z] G-READY FAIL: 5 of 6, G-GEO PASS
[2026-11-21T08:25:39Z] peak memory of this run: 91856896 bytes; refused by the hook: 0; lookups 5, requests 8
```

```
[2026-11-21T08:35:40Z] MemAvailable 1441431552 bytes, floor 274917678; available on / 16911491072 bytes, floor 2447483648
[2026-11-21T08:35:41Z] G-GEO over IPv4: PASS, country 'BG', status 200
[2026-11-21T08:35:42Z] READY pUSD on chain 83.455340, the CLOB's view 83.455340; allowances {'c': 'max', 'n': 'max', 'v': 'max'}; position approvals {'c': True, 'n': True, 'v': True}; open orders of the key 0
[2026-11-21T08:35:42Z] READY kinds the unit may buy on: ['c', 'n', 'v']; may sell on: ['c', 'n', 'v']
[2026-11-21T08:35:42Z] G-READY a Deposit Wallet signed for by the session key: PASS
[2026-11-21T08:35:42Z] G-READY not in closed-only mode: PASS
[2026-11-21T08:35:42Z] G-READY the standard exchange's pUSD allowance the maximum: PASS
[2026-11-21T08:35:42Z] G-READY the key authorized 7 days ahead at least: PASS
[2026-11-21T08:35:42Z] G-READY no open order of the wallet by the key: PASS
[2026-11-21T08:35:42Z] G-READY its pUSD on chain from 80.00 to 150.00: PASS
[2026-11-21T08:35:42Z] G-READY PASS: 6 of 6, G-GEO PASS
[2026-11-21T08:35:42Z] peak memory of this run: 91979776 bytes; refused by the hook: 0; lookups 5, requests 8
```

### 2.3 The prove's record, and the unit after — `62-unit-after.log`, whole

§3 step 11, in order:

1. `LU status`;
2. `LU 'unit after'`;
3. `systemctl show`;
4. the SHA-256 of the installed files;
5. the listings;
6. `service.log`'s last lines;
7. **`/var/lib/l1-bot/prove-1.json`, every field of it** (CANON hard rule 16).

The record holds no address, key or order id (G-PRINT, §2.7). Its `offset` is a Telegram update's number, not a
chat's id. **No refusal of the venue was printed by any mode of this run:** every placement's `words` is `null`, and
every cancellation's `not_canceled` is `0`.

```
2026-11-21T08:52:54.539593627Z
[2026-11-21T08:52:54Z] STATUS stop record: none
[2026-11-21T08:52:54Z] STATUS prove-1.json: code 98851b3c0df4, pass True, kinds ['c', 'n'], heartbeat accepted True, orders 4
[2026-11-21T08:52:54Z] STATUS state: start equity 83.455340 at 2026-11-21T08:37:38Z; started 2026-11-21T08:37:38Z; held 1; reports ['2026-11-20']
[2026-11-21T08:52:54Z] STATUS journal 2026-11-21.jsonl: 495 lines, last 2026-11-21T08:52:53Z; {'cancel-refused': 2, 'canceled': 104, 'clear': 1, 'fill': 1, 'foreign': 1, 'geo': 2, 'place': 105, 'placed': 105, 'poll': 165, 'report': 1, 'select': 1, 'sent': 3, 'start': 1, 'stop': 1, 'stream': 2}
[2026-11-21T08:52:54Z] peak memory of this run: 34553856 bytes; refused by the hook: 0; lookups 0, requests 0
exit=0
2026-11-21T08:52:55.344041103Z
[2026-11-21T08:52:55Z] UNIT after: file installed byte for byte: True; LoadState=loaded; UnitFileState=enabled; ActiveState=active; SubState=running; Result=success; ExecMainStatus=0; ExecMainCode=0; NRestarts=0; MainPID=49171; ActiveEnterTimestamp=Sat 2026-11-21 08:37:35 UTC; InactiveEnterTimestamp=; MemoryCurrent=91742208; MemoryPeak=103886848; Restart=on-failure; NeedDaemonReload=no
[2026-11-21T08:52:55Z] peak memory of this run: 34557952 bytes; refused by the hook: 0; lookups 0, requests 0
exit=0
2026-11-21T08:53:01.522291856Z
MainPID=49171
NRestarts=0
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Sat 2026-11-21 08:37:35 UTC
98851b3c0df447ed7c846edfbf18b9ea1611d12228a4d9a3c1fda3b4f22da214  /root/l1-bot-svc/l1-bot.py
a6305d0e7a220ea88f5a4d2be612cac35f3dbe527d7c3b7ed12fd7c47f956266  /root/l1-bot-svc/l1-bot.service
a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670  /root/l1-bot-svc/tz33-reward-book-capture.py
4720e78573e54b1325dd24af7c30e0de59bfb4c1879d309a23fa6bab6b32d2d4  /root/l1-bot-svc/tz45-l0-rule-w.py
a6305d0e7a220ea88f5a4d2be612cac35f3dbe527d7c3b7ed12fd7c47f956266  /etc/systemd/system/l1-bot.service
/root/l1-bot-svc:
total 604
drwx------ 2 root root   4096 Nov 21 08:25 .
drwx------ 8 root root   4096 Nov 21 08:25 ..
-rw------- 1 root root 188968 Nov 21 08:25 l1-bot.py
-rw------- 1 root root   1014 Nov 21 08:25 l1-bot.service
-rw------- 1 root root 175160 Nov 21 08:25 tz33-reward-book-capture.py
-rw------- 1 root root 233655 Nov 21 08:25 tz45-l0-rule-w.py

/var/lib/l1-bot:
total 412
drwx------  6 root root   4096 Nov 21 08:52 .
drwxr-xr-x 41 root root   4096 Nov 20 18:10 ..
-rw-------  1 root root    310 Nov 20 19:18 account.json
drwx------  2 root root   4096 Nov 21 08:36 journal
drwx------  2 root root   4096 Nov 21 08:36 polls
-rw-------  1 root root   3894 Nov 21 08:36 prove-1.json
drwx------  2 root root   4096 Nov 21 08:36 select
-rw-r--r--  1 root root    452 Nov 21 08:37 service.log
drwx------  2 root root   4096 Nov 21 08:37 stops
-rw-------  1 root root 187351 Nov 20 19:28 tz51-l1-account.py
-rw-------  1 root root 188720 Nov 20 22:57 tz52-l1-account.py
-rw-------  1 root root    840 Nov 21 08:52 unit-state.json
[2026-11-21T08:36:49Z] SERVE the stop record stands (drill at 2026-11-21T08:36:49Z): no request, exit 3
[2026-11-21T08:36:49Z] peak memory of this run: 34680832 bytes; refused by the hook: 0; lookups 0, requests 0
[2026-11-21T08:37:35Z] MemAvailable 1442021376 bytes, floor 274917678; available on / 16910356480 bytes, floor 2447483648
[2026-11-21T08:37:38Z] SERVE start: geoblock PASS BG; kinds proved ['c', 'n'], usable ['c', 'n', 'v']; heartbeat on
{
 "at": 1795250143,
 "code_sha256": "98851b3c0df447ed7c846edfbf18b9ea1611d12228a4d9a3c1fda3b4f22da214",
 "drill": {
  "checks": {
   "every order cancelled and read gone": true,
   "no fill": true,
   "placed live and seen": true,
   "the balance unchanged": true,
   "the stop record written": true,
   "\u00ab\u0421\u0442\u043e\u043f\u00bb pressed": true
  },
  "matched": 0,
  "offset": 113889545,
  "pass_": true,
  "placements": [
   {
    "ms": 74,
    "outcome": 0,
    "result": "live",
    "words": null
   }
  ],
  "pressed_after_s": 7.1,
  "stop": {
   "canceled": 1,
   "open_after": 0,
   "written": true
  }
 },
 "gates": {
  "G-GEO": true,
  "G-POLL": true,
  "G-READY": true,
  "G-RT": true,
  "G-SELECT": true,
  "G-STOP": true,
  "G-TG": true,
  "G-WS": true
 },
 "geo": {
  "country": "BG",
  "reading": "PASS",
  "status": 200
 },
 "hb": {
  "accepted": true,
  "checks": {
   "a heartbeat accepted": true,
   "gone by the venue within 40 s of the last heartbeat": true,
   "no fill": true,
   "placed live and seen": true,
   "the balance unchanged": true
  },
  "gone_after_s": 13.7,
  "matched": 0,
  "pass_": true,
  "placements": [
   {
    "ms": 75,
    "outcome": 0,
    "result": "live",
    "words": null
   }
  ],
  "refused": 0,
  "sends": 1
 },
 "heartbeat_accepted": true,
 "kinds": [
  "c",
  "n"
 ],
 "orders": 4,
 "pass": true,
 "poll": {
  "row": true,
  "served": true
 },
 "ready": {
  "checks": {
   "a Deposit Wallet signed for by the session key": true,
   "its pUSD on chain from 80.00 to 150.00": true,
   "no open order of the wallet by the key": true,
   "not in closed-only mode": true,
   "the key authorized 7 days ahead at least": true,
   "the standard exchange's pUSD allowance the maximum": true
  },
  "facts": "pUSD on chain 83.455340, the CLOB's view 83.455340; allowances {'c': 'max', 'n': 'max', 'v': 'max'}; position approvals {'c': True, 'n': True, 'v': True}; open orders of the key 0"
 },
 "rt": {
  "c": {
   "balance": {
    "after": 83455340,
    "before": 83455340
   },
   "cancel": {
    "canceled": true,
    "not_canceled": 0,
    "words": []
   },
   "checks": {
    "cancelled by its id": true,
    "no fill in its trades": true,
    "placed live": true,
    "seen gone from them": true,
    "seen in the wallet's open orders": true,
    "the wallet's pUSD on chain unchanged": true
   },
   "gone_reads": 2,
   "kind": "c",
   "market": "will-ai-solve-the-riemann-hypothesis-in-2026",
   "matched": 0,
   "pass": true,
   "placements": [
    {
     "ms": 226,
     "outcome": 0,
     "result": "live",
     "words": null
    }
   ],
   "seen": {
    "nothing matched": true,
    "price": true,
    "side BUY": true,
    "size": true,
    "the token": true
   },
   "seen_reads": 5
  },
  "n": {
   "balance": {
    "after": 83455340,
    "before": 83455340
   },
   "cancel": {
    "canceled": true,
    "not_canceled": 0,
    "words": []
   },
   "checks": {
    "cancelled by its id": true,
    "no fill in its trades": true,
    "placed live": true,
    "seen gone from them": true,
    "seen in the wallet's open orders": true,
    "the wallet's pUSD on chain unchanged": true
   },
   "gone_reads": 2,
   "kind": "n",
   "market": "will-dcampion-be-the-first-kick-streamer-to-finish-gta-vi-by-december-31-2026",
   "matched": 0,
   "pass": true,
   "placements": [
    {
     "ms": 197,
     "outcome": 0,
     "result": "live",
     "words": null
    }
   ],
   "seen": {
    "nothing matched": true,
    "price": true,
    "side BUY": true,
    "size": true,
    "the token": true
   },
   "seen_reads": 2
  }
 },
 "select": {
  "candidates": 41,
  "kinds": {
   "c": 26,
   "n": 15
  },
  "members": 150,
  "picked": [
   "c",
   "n"
  ],
  "requests": 189
 },
 "sell_ok": {
  "c": true,
  "n": true,
  "v": true
 },
 "usable": [
  "c",
  "n",
  "v"
 ],
 "ws": {
  "frames": 2,
  "seeded": 2,
  "tokens": 2
 }
}
```

### 2.4 The unit's state at the end of this run, and its stops

- **State, 08:53:01 UTC:**
  - `l1-bot.service` `active`/`running`, `enabled`, `NRestarts` `0`, MainPID `49171`, active since 08:37:35;
  - its code `/root/l1-bot-svc/l1-bot.py` at `98851b3c…` beside the two frozen files at their SHA-256;
  - its unit file at `a6305d0e…`, byte for byte with the code's copy;
  - no stop record standing; one in `stops/`, the drill's, `stop-1795250209.json`;
  - its prove `prove-1.json`, PASS, kinds `['c', 'n']`, heartbeat accepted;
  - its start equity `83.455340` pUSD at 08:37:38 UTC;
  - `MemoryCurrent` `91,742,208`, `MemoryPeak` `103,886,848`, under `MemoryMax=384M`.
- **Its stops, as TZ-53 §4 fixes them:**
  - **«Стоп»** in the Boss's pinned Telegram chat: every open order cancelled and read gone, a stop record, exit
    `3`, not restarted. Proved by G-STOP and G-HOLD.
  - **The unit's own stops, each with the same record:**
    - the loss limit, `25` pUSD below `83.455340`;
    - a geoblock read of `blocked`;
    - the disk under `2,447,483,648` bytes;
    - an equity unread for 900 s;
    - closed-only mode;
    - the key's authorization due within a day;
    - orders that will not cancel.
  - **`systemctl disable --now l1-bot.service`** on the live host: SIGTERM, every order cancelled, exit `0`, no
    restart and no stop record.
  - **The last stops, the Boss's, not run by this TZ:** B-REVOKE, TZ-51 §4.11's line word for word with TZ-51's
    kept copy, and withdraw on polymarket.com.
- **After a stop**, `clear-stop` on the host, then a start by `systemctl`. No message starts the unit.

### 2.5 E-SELF — `57-engine-selftest.log` and `58-engine-sdk-selftest.log`, whole

```
2026-11-21T08:24:40.289548562Z
[2026-11-21T08:24:40Z] SELFTEST 1 an AF_INET6 socket refused, AF_INET and asyncio's AF_UNIX let through
[2026-11-21T08:24:40Z] SELFTEST 2 a lookup in AF_INET alone, of a host its mode names alone
[2026-11-21T08:24:40Z] SELFTEST 3 a connection to an IPv4 address this process resolved alone; an IPv6 or a path refused
[2026-11-21T08:24:40Z] SELFTEST 4 a process its mode names alone
[2026-11-21T08:24:40Z] SELFTEST 5 writes under the unit's record alone; its credentials read in their modes; no terminal; no capture's store
[2026-11-21T08:24:40Z] SELFTEST 6 a change under the unit's record alone
[2026-11-21T08:24:40Z] SELFTEST 7 gai4 asks AF_INET of a lookup that names no family, and refuses any other
[2026-11-21T08:24:40Z] SELFTEST 8 tz45's own w_targets at its own self-test's 13 cases (its lines 3932 to 3940); its W_MS_MAX 20 shares, W_COMP_MAX 1, CAP_CLIPS 1
[2026-11-21T08:24:40Z] SELFTEST 9 tz33's rule: 150 members, 1,500 walked at most, an end 15 days on, 31 tags, its endpoints
[2026-11-21T08:24:40Z] SELFTEST 10 a frozen file of other bytes refused; a name it lacks refused; a name its rules read and nothing gives refused (W_COMP_MAX reads Fr)
[2026-11-21T08:24:40Z] SELFTEST 11 rule W's targets on the touch, ours out: w_targets, nothing on a narrow or one-sided touch
[2026-11-21T08:24:40Z] SELFTEST 12 nothing before a served poll, above competitiveness 1, after the terms moved, above 20 shares
[2026-11-21T08:24:40Z] SELFTEST 13 a target outside (0, 1) quotes nothing on its side, as Day.decide's guard
[2026-11-21T08:24:40Z] SELFTEST 14 the cap: no bid at a position of one size, no ask at minus one size
[2026-11-21T08:24:40Z] SELFTEST 15 a side's order: a sell of a size held where selling is approved, else a buy - the second token's at the complement
[2026-11-21T08:24:40Z] SELFTEST 16 a buy reserves its price times its size; prices on their tick's grid; sizes to the hundredth
[2026-11-21T08:24:40Z] SELFTEST 17 a member's exchange by its tokens' reserved bits and its negative-risk flag
[2026-11-21T08:24:40Z] SELFTEST 18 the touch with our own resting sizes taken out of their levels
[2026-11-21T08:24:40Z] SELFTEST 19 a level emptied and one added; a frame as its items, PONG none
[2026-11-21T08:24:40Z] SELFTEST 20 a member's minimum size in hundredths, its spread in half-thousandths; a fraction of either refused
[2026-11-21T08:24:40Z] SELFTEST 21 a list frame seeds the first token's book and its tick; the second token's book is not read
[2026-11-21T08:24:40Z] SELFTEST 22 a price_change applied to the first token alone; a tick change read
[2026-11-21T08:24:40Z] SELFTEST 23 a trade printed at our own price asks for the open orders at once
[2026-11-21T08:24:40Z] SELFTEST 24 a poll's row: the rate in force that day, the competitiveness, the terms; a page of no row none
[2026-11-21T08:24:40Z] SELFTEST 25 poll_row equals TZ-45's own polls_of, row by row, on the same four stored replies
[2026-11-21T08:24:40Z] SELFTEST 26 the equity: the cash and the first token held marked at its best bid
[2026-11-21T08:24:40Z] SELFTEST 27 a complete set at 1; a bid level that is ours alone marks nothing
[2026-11-21T08:24:40Z] SELFTEST 28 a book not seeded - the stream down - marks the holdings at their last mark, never at 0
[2026-11-21T08:24:40Z] SELFTEST 29 G-READY's six checks on a ready account; the kinds with the maximum allowance; no address printed
[2026-11-21T08:24:40Z] SELFTEST 30 G-READY fails outside the capital's bounds, below the maximum allowance, on an open order, a key due in six days, closed-only; a later start reads no capital bound
[2026-11-21T08:24:40Z] SELFTEST 31 G-GEO: PASS, BLOCKED or UNREAD; the address never kept
[2026-11-21T08:24:40Z] SELFTEST 32 the pinned chat's commands alone; another chat's «Стоп» ignored
[2026-11-21T08:24:40Z] SELFTEST 33 the journal: a line an event, 0600
[2026-11-21T08:24:40Z] SELFTEST 34 the stop record by exclusive create: the first stands
[2026-11-21T08:24:40Z] SELFTEST 35 a prove of this code that read PASS, and none of another
[2026-11-21T08:24:40Z] SELFTEST 36 the day's selection by tz33's run_rule through the unit's fetch; TZ-33's own StoredFetch on the stored replies gives the same members
[2026-11-21T08:24:40Z] SELFTEST 37 the candidates: members of a proved kind at most 20 shares, in rank; their first tokens streamed
[2026-11-21T08:24:40Z] SELFTEST 38 a refusal in the venue's words, addresses masked, one line
[2026-11-21T08:24:40Z] SELFTEST PASS: 38 checks, 38 passed; refused by the hook: 0
[2026-11-21T08:24:40Z] peak memory of this run: 69341184 bytes; refused by the hook: 0; lookups 1, requests 0
exit=0
```

```
2026-11-21T08:24:45.687400496Z
[2026-11-21T08:24:46Z] SDK SELFTEST 1 the client loaded at its pin, its agent this unit's, its lookups through gai4
[2026-11-21T08:24:46Z] SDK SELFTEST 2 the hook live: a socket of family AF_INET6 refused
[2026-11-21T08:24:46Z] SDK SELFTEST 3 the hook live: a socket of family AF_UNIX let through
[2026-11-21T08:24:46Z] SDK SELFTEST 4 the hook live: a lookup ('localhost', 80, <AddressFamily.AF_INET6: 10>) refused
[2026-11-21T08:24:46Z] SDK SELFTEST 5 the hook live: a lookup ('example.com', 443) refused
[2026-11-21T08:24:47Z] SDK SELFTEST 6 G-READY against the stand-in: 6 of 6, a Deposit Wallet signed for by the session key, three kinds usable
[2026-11-21T08:24:48Z] SDK SELFTEST 7 an exchange's allowance below the maximum: its kind not usable
[2026-11-21T08:24:53Z] PROVE record /tmp/l1-bot-selftest/sdk-7vxl3746/var/prove-1.json: 3770 bytes, 0600
[2026-11-21T08:24:53Z] PROVE G-GEO {'reading': 'PASS', 'country': 'BG', 'status': 200}; pUSD on chain 100.000000, the CLOB's view 100.000000; allowances {'c': 'max', 'n': 'max', 'v': 'max'}; position approvals {'c': True, 'n': True, 'v': True}; open orders of the key 0
[2026-11-21T08:24:53Z] PROVE G-READY a Deposit Wallet signed for by the session key: PASS
[2026-11-21T08:24:53Z] PROVE G-READY not in closed-only mode: PASS
[2026-11-21T08:24:53Z] PROVE G-READY the standard exchange's pUSD allowance the maximum: PASS
[2026-11-21T08:24:53Z] PROVE G-READY the key authorized 7 days ahead at least: PASS
[2026-11-21T08:24:53Z] PROVE G-READY no open order of the wallet by the key: PASS
[2026-11-21T08:24:53Z] PROVE G-READY its pUSD on chain from 80.00 to 150.00: PASS
[2026-11-21T08:24:53Z] PROVE select {'members': 3, 'candidates': 2, 'requests': 5, 'kinds': {'c': 1, 'n': 1}, 'picked': ['c', 'n']}; poll {'served': True, 'row': True}; ws {'tokens': 2, 'seeded': 2, 'frames': 2}
[2026-11-21T08:24:53Z] PROVE G-RT CTF (syn-c): placements [(0, 'live', 65, None)]; seen in 1 reads {'price': True, 'size': True, 'side BUY': True, 'the token': True, 'nothing matched': True}; cancel {'canceled': True, 'not_canceled': 0, 'words': []}; gone in 1 reads; matched 0; balance 100.000000 -> 100.000000
[2026-11-21T08:24:53Z] PROVE G-RT c placed live: PASS
[2026-11-21T08:24:53Z] PROVE G-RT c seen in the wallet's open orders: PASS
[2026-11-21T08:24:53Z] PROVE G-RT c cancelled by its id: PASS
[2026-11-21T08:24:53Z] PROVE G-RT c seen gone from them: PASS
[2026-11-21T08:24:53Z] PROVE G-RT c no fill in its trades: PASS
[2026-11-21T08:24:53Z] PROVE G-RT c the wallet's pUSD on chain unchanged: PASS
[2026-11-21T08:24:53Z] PROVE G-RT CTF negative-risk (syn-n): placements [(0, 'live', 63, None)]; seen in 1 reads {'price': True, 'size': True, 'side BUY': True, 'the token': True, 'nothing matched': True}; cancel {'canceled': True, 'not_canceled': 0, 'words': []}; gone in 1 reads; matched 0; balance 100.000000 -> 100.000000
[2026-11-21T08:24:53Z] PROVE G-RT n placed live: PASS
[2026-11-21T08:24:53Z] PROVE G-RT n seen in the wallet's open orders: PASS
[2026-11-21T08:24:53Z] PROVE G-RT n cancelled by its id: PASS
[2026-11-21T08:24:53Z] PROVE G-RT n seen gone from them: PASS
[2026-11-21T08:24:53Z] PROVE G-RT n no fill in its trades: PASS
[2026-11-21T08:24:53Z] PROVE G-RT n the wallet's pUSD on chain unchanged: PASS
[2026-11-21T08:24:53Z] PROVE G-HB accepted True; sends 1, refused 0; gone after 2.2 s; {'a heartbeat accepted': 'PASS', 'placed live and seen': 'PASS', 'gone by the venue within 8 s of the last heartbeat': 'PASS', 'no fill': 'PASS', 'the balance unchanged': 'PASS'}
[2026-11-21T08:24:53Z] PROVE G-STOP pressed after 0.0 s; stop {'canceled': 1, 'open_after': 0, 'written': True}; matched 0; {'placed live and seen': 'PASS', '«Стоп» pressed': 'PASS', 'every order cancelled and read gone': 'PASS', 'the stop record written': 'PASS', 'no fill': 'PASS', 'the balance unchanged': 'PASS'}
[2026-11-21T08:24:53Z] PROVE G-GEO: PASS
[2026-11-21T08:24:53Z] PROVE G-READY: PASS
[2026-11-21T08:24:53Z] PROVE G-TG: PASS
[2026-11-21T08:24:53Z] PROVE G-SELECT: PASS
[2026-11-21T08:24:53Z] PROVE G-POLL: PASS
[2026-11-21T08:24:53Z] PROVE G-WS: PASS
[2026-11-21T08:24:53Z] PROVE G-RT: PASS
[2026-11-21T08:24:53Z] PROVE G-STOP: PASS
[2026-11-21T08:24:53Z] G-PROVE PASS; kinds proved ['c', 'n']; heartbeat accepted True; orders placed 4; last cancel_all not needed: the stop cancelled
[2026-11-21T08:24:53Z] SDK SELFTEST 8 G-PROVE PASS: geoblock, account, Telegram, selection, poll, stream, the round trip on CTF and negative-risk, the heartbeat's lapse cancelling the order, the stop's round trip; 4 orders; none left
[2026-11-21T08:24:53Z] SDK SELFTEST 9 the Boss's round trip: placed at the lowest price and the minimum order size, seen, cancelled by its id, seen gone, the balance unchanged
[2026-11-21T08:24:53Z] SDK SELFTEST 10 the heartbeat: accepted every HB_S, then silent; the venue's lapse cancels the order
[2026-11-21T08:24:53Z] SDK SELFTEST 11 the stop's round trip: the Boss's «Стоп», the order cancelled and read gone, the record written
[2026-11-21T08:24:53Z] SDK SELFTEST 12 the prove's record holds no address, no key and no order id
[2026-11-21T08:24:53Z] SERVE the stop record stands (drill at 2026-11-21T08:24:53Z): no request, exit 3
[2026-11-21T08:24:53Z] SDK SELFTEST 13 a start with the stop record standing: exit 3, no request at all
[2026-11-21T08:24:53Z] CLEAR the stop record (drill at 2026-11-21T08:24:53Z) moved to /tmp/l1-bot-selftest/sdk-7vxl3746/var/stops/stop-1795249493.json
[2026-11-21T08:24:53Z] CLEAR the chat's pending updates consumed: 2
[2026-11-21T08:24:53Z] SDK SELFTEST 14 clear-stop: the record moved into the history, the chat's pending commands consumed
[2026-11-21T08:24:54Z] SERVE start: geoblock PASS BG; kinds proved ['c', 'n'], usable ['c', 'n', 'v']; heartbeat on
[2026-11-21T08:24:57Z] SERVE end: stop («Стоп» из Telegram), exit 3; canceled 1, open after 0
[2026-11-21T08:24:57Z] SDK SELFTEST 15 the unit live to the Boss's «Стоп»: exit 3, the record written, no order left
[2026-11-21T08:24:57Z] SDK SELFTEST 16 rule W's quotes on the touch 0.30-0.42, spread 4.5 c: a buy of 20 at 0.32 and a buy of the second token at 0.60 for the ask at 0.40
[2026-11-21T08:24:57Z] SDK SELFTEST 17 its own quotes in the book, shown back by the channel, are not chased: two placed
[2026-11-21T08:24:57Z] SDK SELFTEST 18 the bid filled: the cap holds the bid back, the ask sells the 20 shares held at 0.40
[2026-11-21T08:24:57Z] SDK SELFTEST 19 a market whose touch is narrower than rule W's width quotes nothing
[2026-11-21T08:24:57Z] SDK SELFTEST 20 the Boss's chat: the start, the fill, the status, the stop
[2026-11-21T08:24:57Z] SDK SELFTEST 21 the start equity recorded at the first start; the market held kept in the unit's state
[2026-11-21T08:24:57Z] SDK SELFTEST 22 the journal: every order, cancel, fill, poll, command and the stop
[2026-11-21T08:24:57Z] CLEAR the stop record (stop at 2026-11-21T08:24:57Z) moved to /tmp/l1-bot-selftest/sdk-7vxl3746/var/stops/stop-1795249497.json
[2026-11-21T08:24:57Z] CLEAR the chat's pending updates consumed: 4
[2026-11-21T08:24:58Z] SERVE start: geoblock PASS BG; kinds proved ['c', 'n'], usable ['c', 'n', 'v']; heartbeat on
[2026-11-21T08:25:00Z] SERVE end: loss (лимит убытка), exit 3; canceled 2, open after 0
[2026-11-21T08:25:00Z] SDK SELFTEST 23 the loss limit: equity 25 pUSD below the start equity stops the unit, every order cancelled
[2026-11-21T08:25:00Z] CLEAR the stop record (loss at 2026-11-21T08:25:00Z) moved to /tmp/l1-bot-selftest/sdk-7vxl3746/var/stops/stop-1795249500.json
[2026-11-21T08:25:00Z] CLEAR the chat's pending updates consumed: 4
[2026-11-21T08:25:01Z] SDK SELFTEST 24 the geoblock read blocked at the start: the stop record, no order placed
[2026-11-21T08:25:01Z] CLEAR the stop record (geo at 2026-11-21T08:25:01Z) moved to /tmp/l1-bot-selftest/sdk-7vxl3746/var/stops/stop-1795249501.json
[2026-11-21T08:25:01Z] CLEAR the chat's pending updates consumed: 4
[2026-11-21T08:25:02Z] SERVE start: geoblock PASS BG; kinds proved ['c', 'n'], usable ['c', 'n', 'v']; heartbeat on
[2026-11-21T08:25:02Z] SERVE end: term (сигнал systemd), exit 0; canceled 2, open after 0
[2026-11-21T08:25:02Z] SDK SELFTEST 25 SIGTERM: every order cancelled, exit 0, no stop record - systemd's own stop
[2026-11-21T08:25:02Z] SDK SELFTEST 26 the day's switch: no member quoted before the day's selection is read; once read, its markets built
[2026-11-21T08:25:02Z] SDK SELFTEST 27 the day's report: the venue's paid rewards and rebates, read for the day
[2026-11-21T08:25:02Z] SDK SELFTEST 28 no order of ours read by its id: the venue answered such a read null (map section 7 item 192)
[2026-11-21T08:25:02Z] SDK SELFTEST 29 every request to the stand-in carried this unit's agent: 265
[2026-11-21T08:25:02Z] SDK SELFTEST PASS: 29 checks, 29 passed; refused by the hook: 2
[2026-11-21T08:25:03Z] peak memory of this run: 107470848 bytes; refused by the hook: 2; lookups 1, requests 126
exit=0
```

### 2.6 The live host before and after

**`43-l1-before.log`**: §0.6's three names, `svc exit=1`, `unit exit=1`, both `inactive`. `active exit=4` is
`systemctl is-active`'s exit where no unit is active.

```
2026-11-21T08:23:03.607004747Z
account.json
tz51-l1-account.py
tz52-l1-account.py
svc exit=1
unit exit=1
inactive
inactive
active exit=4
```

**`40-host-before.log`**: the gate 5 of 5, and **LS**: root's keys the Executor's alone, the nine `PATH` lines
§0.6's, line for line.

```
2026-11-21T07:40:59.118160341Z
[2026-11-21T07:40:59Z] LH1 hostname vs-2348: PASS
[2026-11-21T07:40:59Z] LH2 Ubuntu 24.04: PASS
[2026-11-21T07:40:59Z] LH3 Python 3.12: PASS
[2026-11-21T07:40:59Z] LH4 not the capture host: PASS
[2026-11-21T07:40:59Z] LH5 the host key pinned at TZ-47's first connection: PASS
[2026-11-21T07:40:59Z] LIVE HOST GATE PASS: 5 of 5
[2026-11-21T07:40:59Z] MemAvailable read 1: 1443639296 bytes, floor 86426834
[2026-11-21T07:40:59Z] available on /: 16912211968 bytes, floor 2447483648
[2026-11-21T07:40:59Z] HOST before: kernel 6.8.0-138-generic; Python 3.12.3; Ubuntu 24.04.5 LTS; MemTotal 1944465408 MemAvailable 1443639296 SwapTotal 1073737728 SwapFree 1073737728; / 20779339776 bytes, 16912211968 available
[2026-11-21T07:40:59Z] LOCALE /etc/default/locale: LANG="ru_UA.UTF-8"
[2026-11-21T07:40:59Z] LOCALE `locale` in this session, exit 0: LANG=ru_UA.UTF-8; LANGUAGE=; LC_CTYPE="C"; LC_NUMERIC="C"; LC_TIME="C"; LC_COLLATE="C"; LC_MONETARY="C"; LC_MESSAGES="C"; LC_PAPER="C"; LC_NAME="C"; LC_ADDRESS="C"; LC_TELEPHONE="C"; LC_MEASUREMENT="C"; LC_IDENTIFICATION="C"; LC_ALL=C
[2026-11-21T07:40:59Z] CLOCK exit 0: NTP=yes; NTPSynchronized=yes; TimeUSec=Sat 2026-11-21 07:40:59 UTC
[2026-11-21T07:40:59Z] SSHD authorized keys of root: [('ssh-ed25519', 'SHA256:1xbA0Mhjj0NDXcLaefl9D8run7ZKh/oo0xUOmc06Qzo')]; the Executor's among them: True
[2026-11-21T07:40:59Z] PATH /etc/l1-bot: dir mode 0700 uid 0 bytes 4096
[2026-11-21T07:40:59Z] PATH /etc/l1-bot/session-key: file mode 0600 uid 0 bytes 67
[2026-11-21T07:40:59Z] PATH /etc/l1-bot/relayer-key: file mode 0600 uid 0 bytes 105
[2026-11-21T07:40:59Z] PATH /etc/l1-bot/telegram-token: file mode 0600 uid 0 bytes 47
[2026-11-21T07:40:59Z] PATH /etc/l1-bot/chat-id: file mode 0600 uid 0 bytes 10
[2026-11-21T07:40:59Z] PATH /var/lib/l1-bot: dir mode 0700 uid 0 bytes 4096
[2026-11-21T07:40:59Z] PATH /var/lib/l1-bot/account.json: file mode 0600 uid 0 bytes 310
[2026-11-21T07:40:59Z] PATH /root/l1-env: dir mode 0755 uid 0 bytes 4096
[2026-11-21T07:40:59Z] PATH /root/tz53-work/wheels: absent
[2026-11-21T07:40:59Z] peak memory of this run: 35069952 bytes
[2026-11-21T07:40:59Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

**`79-host-after.log`**: the gate 5 of 5. Root's keys, every `PATH` line, the locale and the clock read as before.

```
2026-11-21T08:53:15.761504259Z
[2026-11-21T08:53:15Z] LH1 hostname vs-2348: PASS
[2026-11-21T08:53:15Z] LH2 Ubuntu 24.04: PASS
[2026-11-21T08:53:15Z] LH3 Python 3.12: PASS
[2026-11-21T08:53:15Z] LH4 not the capture host: PASS
[2026-11-21T08:53:15Z] LH5 the host key pinned at TZ-47's first connection: PASS
[2026-11-21T08:53:15Z] LIVE HOST GATE PASS: 5 of 5
[2026-11-21T08:53:15Z] MemAvailable read 1: 1345294336 bytes, floor 86426834
[2026-11-21T08:53:15Z] available on /: 16910192640 bytes, floor 2447483648
[2026-11-21T08:53:15Z] HOST after: kernel 6.8.0-138-generic; Python 3.12.3; Ubuntu 24.04.5 LTS; MemTotal 1944465408 MemAvailable 1345294336 SwapTotal 1073737728 SwapFree 1073737728; / 20779339776 bytes, 16910192640 available
[2026-11-21T08:53:15Z] LOCALE /etc/default/locale: LANG="ru_UA.UTF-8"
[2026-11-21T08:53:15Z] LOCALE `locale` in this session, exit 0: LANG=ru_UA.UTF-8; LANGUAGE=; LC_CTYPE="C"; LC_NUMERIC="C"; LC_TIME="C"; LC_COLLATE="C"; LC_MONETARY="C"; LC_MESSAGES="C"; LC_PAPER="C"; LC_NAME="C"; LC_ADDRESS="C"; LC_TELEPHONE="C"; LC_MEASUREMENT="C"; LC_IDENTIFICATION="C"; LC_ALL=C
[2026-11-21T08:53:15Z] CLOCK exit 0: NTP=yes; NTPSynchronized=yes; TimeUSec=Sat 2026-11-21 08:53:15 UTC
[2026-11-21T08:53:15Z] SSHD authorized keys of root: [('ssh-ed25519', 'SHA256:1xbA0Mhjj0NDXcLaefl9D8run7ZKh/oo0xUOmc06Qzo')]; the Executor's among them: True
[2026-11-21T08:53:15Z] PATH /etc/l1-bot: dir mode 0700 uid 0 bytes 4096
[2026-11-21T08:53:15Z] PATH /etc/l1-bot/session-key: file mode 0600 uid 0 bytes 67
[2026-11-21T08:53:15Z] PATH /etc/l1-bot/relayer-key: file mode 0600 uid 0 bytes 105
[2026-11-21T08:53:15Z] PATH /etc/l1-bot/telegram-token: file mode 0600 uid 0 bytes 47
[2026-11-21T08:53:15Z] PATH /etc/l1-bot/chat-id: file mode 0600 uid 0 bytes 10
[2026-11-21T08:53:15Z] PATH /var/lib/l1-bot: dir mode 0700 uid 0 bytes 4096
[2026-11-21T08:53:15Z] PATH /var/lib/l1-bot/account.json: file mode 0600 uid 0 bytes 310
[2026-11-21T08:53:15Z] PATH /root/l1-env: dir mode 0755 uid 0 bytes 4096
[2026-11-21T08:53:15Z] PATH /root/tz53-work/wheels: absent
[2026-11-21T08:53:15Z] peak memory of this run: 35053568 bytes
[2026-11-21T08:53:15Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

**G-GEO**, `41-geoblock.log`; **G-SSH** K1 to K5, `42-sshd.log` and `78-sshd-after.log`; K6, `08-methods.log` and
`88-methods-after.log`:

```
2026-11-21T08:23:10.457571738Z
[2026-11-21T08:23:10Z] MemAvailable read 1: 1444749312 bytes, floor 86426834
[2026-11-21T08:23:10Z] available on /: 16912195584 bytes, floor 2447483648
[2026-11-21T08:23:10Z] G-GEO read 1 over IPv4: status 200, 68 bytes, blocked False, country 'BG', region '22', keys ['blocked', 'country', 'ip', 'region']; the address the venue saw is the connection's own: True -> PASS
[2026-11-21T08:23:10Z] G-GEO PASS
[2026-11-21T08:23:10Z] peak memory of this run: 37818368 bytes
[2026-11-21T08:23:10Z] refused by the hook: 0; lookups 1, requests 1
exit=0
```

```
2026-11-21T08:23:11.567385467Z
[2026-11-21T08:23:11Z] K1 TZ-49's sshd drop-in, byte for byte: PASS
[2026-11-21T08:23:11Z] K2 passwordauthentication no: PASS
[2026-11-21T08:23:11Z] K3 kbdinteractiveauthentication no: PASS
[2026-11-21T08:23:11Z] K4 permitrootlogin without-password: PASS
[2026-11-21T08:23:11Z] K5 pubkeyauthentication yes: PASS
[2026-11-21T08:23:11Z] G-SSH K1 to K5 PASS: 5 of 5
[2026-11-21T08:23:11Z] peak memory of this run: 35196928 bytes
[2026-11-21T08:23:11Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

```
2026-11-21T08:23:11.756763887Z
[2026-11-21T08:23:12Z] METHODS gate: the methods the live host's sshd offers root, from outside: ['publickey']; ssh exit 255
[2026-11-21T08:23:12Z] G-SSH K6 publickey alone, from outside: PASS
[2026-11-21T08:23:12Z] peak memory of this run: 34500608 bytes
[2026-11-21T08:23:12Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

```
2026-11-21T08:53:14.308944498Z
[2026-11-21T08:53:14Z] K1 TZ-49's sshd drop-in, byte for byte: PASS
[2026-11-21T08:53:14Z] K2 passwordauthentication no: PASS
[2026-11-21T08:53:14Z] K3 kbdinteractiveauthentication no: PASS
[2026-11-21T08:53:14Z] K4 permitrootlogin without-password: PASS
[2026-11-21T08:53:14Z] K5 pubkeyauthentication yes: PASS
[2026-11-21T08:53:14Z] G-SSH K1 to K5 PASS: 5 of 5
[2026-11-21T08:53:14Z] peak memory of this run: 35069952 bytes
[2026-11-21T08:53:14Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

```
2026-11-21T08:53:14.489802085Z
[2026-11-21T08:53:15Z] METHODS after: the methods the live host's sshd offers root, from outside: ['publickey']; ssh exit 255
[2026-11-21T08:53:15Z] G-SSH K6 publickey alone, from outside: PASS
[2026-11-21T08:53:15Z] peak memory of this run: 34484224 bytes
[2026-11-21T08:53:15Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

**`81-keep.log`**: TZ-52's copy read at `a425e67c…` and removed, `exit=1`. TZ-51's copy is kept for B-REVOKE.

```
2026-11-21T08:53:23.028798750Z
a425e67cce7178e425b04f899ad245cf31a38848bd2553dfacdbbbcdf3a73366  /var/lib/l1-bot/tz52-l1-account.py
exit=1
/etc/l1-bot:
total 24
drwx------   2 root root 4096 Nov 20 22:56 .
drwxr-xr-x 107 root root 4096 Nov 20 06:25 ..
-rw-------   1 root root   10 Nov 20 22:56 chat-id
-rw-------   1 root root  105 Nov 20 18:10 relayer-key
-rw-------   1 root root   67 Nov 20 06:25 session-key
-rw-------   1 root root   47 Nov 20 18:00 telegram-token

/var/lib/l1-bot:
total 224
drwx------  6 root root   4096 Nov 21 08:53 .
drwxr-xr-x 41 root root   4096 Nov 20 18:10 ..
-rw-------  1 root root    310 Nov 20 19:18 account.json
drwx------  2 root root   4096 Nov 21 08:36 journal
drwx------  2 root root   4096 Nov 21 08:36 polls
-rw-------  1 root root   3894 Nov 21 08:36 prove-1.json
drwx------  2 root root   4096 Nov 21 08:36 select
-rw-r--r--  1 root root    452 Nov 21 08:37 service.log
drwx------  2 root root   4096 Nov 21 08:37 stops
-rw-------  1 root root 187351 Nov 20 19:28 tz51-l1-account.py
-rw-------  1 root root    840 Nov 21 08:52 unit-state.json
```

**The client and the checker on the live host:** `53-env.log` and `56-key.log`, whole. Each self-test's summary
is quoted here; each log's SHA-256 is in §2.10.

```
2026-11-21T08:24:12.789769042Z
[2026-11-21T08:24:13Z] ENV interpreter 3.12.3, prefix /root/l1-env: PASS
[2026-11-21T08:24:13Z] ENV distributions: 34 installed, 34 pinned; missing [], extra [], another version []
[2026-11-21T08:24:13Z] ENV files: 1373 RECORD entries with a SHA-256 over 1367 paths, 6 of them listed by two distributions; absent [], another hash []
[2026-11-21T08:24:13Z] ENV the client polymarket-client 0.20.0; session keys 15534000 s, a batch 600 s; selectors {'authorize': '24017fae', 'revoke': 'e63f952f'}; hosts https://clob.polymarket.com, https://relayer-v2.polymarket.com, https://gamma-api.polymarket.com
[2026-11-21T08:24:13Z] G-ENV installed PASS
[2026-11-21T08:24:13Z] peak memory of this run: 76623872 bytes
[2026-11-21T08:24:13Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

```
2026-11-21T08:24:33.737474000Z
[2026-11-21T08:24:33Z] MemAvailable read 1: 1428217856 bytes, floor 274917678
[2026-11-21T08:24:33Z] available on /: 16912146432 bytes, floor 2447483648
[2026-11-21T08:24:34Z] G-KEY /etc/l1-bot/session-key: present, kept; file mode 0600 uid 0 bytes 67
[2026-11-21T08:24:34Z] peak memory of this run: 76488704 bytes
[2026-11-21T08:24:34Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

```
logs/20-selftest.log (capture host): [2026-11-21T08:24:00Z] SELFTEST PASS: 141 checks, 141 passed; refused by the hook: 5, each a check's own
live-logs/50-selftest.log (live host): [2026-11-21T08:24:01Z] SELFTEST PASS: 141 checks, 141 passed; refused by the hook: 5, each a check's own
live-logs/54-sdk-selftest.log (live host): [2026-11-21T08:24:32Z] SDK SELFTEST PASS: 32 checks, 32 passed; refused by the hook: 2, each a check's own
```

### 2.7 The copy, G-PRINT, and the closing reads

**`80-live-copy.log`**: `scp exit=0`, `diff exit=0`, the live host's 17 logs. **G-PRINT** gives `0` lines with an
address's or a token's form, and `0` files holding the live host's address.

```
2026-11-21T08:53:28.448907912Z
scp exit=0
diff exit=0
total 128
drwxr-xr-x 2 root root  4096 Nov 21 08:53 .
drwxr-xr-x 6 root root  4096 Nov 21 08:53 ..
-rw-r--r-- 1 root root  2207 Nov 21 08:53 40-host-before.log
-rw-r--r-- 1 root root   576 Nov 21 08:53 41-geoblock.log
-rw-r--r-- 1 root root   533 Nov 21 08:53 42-sshd.log
-rw-r--r-- 1 root root   137 Nov 21 08:53 43-l1-before.log
-rw-r--r-- 1 root root 19535 Nov 21 08:53 50-selftest.log
-rw-r--r-- 1 root root   813 Nov 21 08:53 53-env.log
-rw-r--r-- 1 root root 13600 Nov 21 08:53 54-sdk-selftest.log
-rw-r--r-- 1 root root   422 Nov 21 08:53 56-key.log
-rw-r--r-- 1 root root  4657 Nov 21 08:53 57-engine-selftest.log
-rw-r--r-- 1 root root  9016 Nov 21 08:53 58-engine-sdk-selftest.log
-rw-r--r-- 1 root root 11761 Nov 21 08:53 60-deploy.log
-rw-r--r-- 1 root root  1133 Nov 21 08:53 61-ready-1.log
-rw-r--r-- 1 root root  1133 Nov 21 08:53 61-ready-2.log
-rw-r--r-- 1 root root  7356 Nov 21 08:53 62-unit-after.log
-rw-r--r-- 1 root root   533 Nov 21 08:53 78-sshd-after.log
-rw-r--r-- 1 root root  2206 Nov 21 08:53 79-host-after.log
-rw-r--r-- 1 root root  1088 Nov 21 08:53 81-keep.log
0
0
```

**`90-closing.log`**: the live host's L1 paths and the capture host's units. The recorder, the reward book and the
advisor read the same `MainPID`, `NRestarts` and `ActiveState` as at §0.3. The archive's service reads `inactive`
and its timer `active`.

```
2026-11-21T08:53:43.593630215Z
Sat Nov 21 08:53:44 UTC 2026
               total        used        free      shared  buff/cache   available
Mem:      1944465408   574652416   685961216     1466368   858238976  1369812992
Swap:     1073737728           0  1073737728
Filesystem             1B-blocks       Avail
/dev/mapper/lvm-root 20779339776 16910364672
active
/etc/l1-bot:
total 24
drwx------   2 root root 4096 Nov 20 22:56 .
drwxr-xr-x 107 root root 4096 Nov 20 06:25 ..
-rw-------   1 root root   10 Nov 20 22:56 chat-id
-rw-------   1 root root  105 Nov 20 18:10 relayer-key
-rw-------   1 root root   67 Nov 20 06:25 session-key
-rw-------   1 root root   47 Nov 20 18:00 telegram-token

/var/lib/l1-bot:
total 224
drwx------  6 root root   4096 Nov 21 08:53 .
drwxr-xr-x 41 root root   4096 Nov 20 18:10 ..
-rw-------  1 root root    310 Nov 20 19:18 account.json
drwx------  2 root root   4096 Nov 21 08:36 journal
drwx------  2 root root   4096 Nov 21 08:36 polls
-rw-------  1 root root   3894 Nov 21 08:36 prove-1.json
drwx------  2 root root   4096 Nov 21 08:36 select
-rw-r--r--  1 root root    452 Nov 21 08:37 service.log
drwx------  2 root root   4096 Nov 21 08:37 stops
-rw-------  1 root root 187351 Nov 20 19:28 tz51-l1-account.py
-rw-------  1 root root    840 Nov 21 08:52 unit-state.json
/etc/l1-bot/chat-id 10 600 root
/etc/l1-bot/relayer-key 105 600 root
/etc/l1-bot/session-key 67 600 root
/etc/l1-bot/telegram-token 47 600 root
/var/lib/l1-bot/account.json 310 600 root
/var/lib/l1-bot/journal 4096 700 root
/var/lib/l1-bot/polls 4096 700 root
/var/lib/l1-bot/prove-1.json 3894 600 root
/var/lib/l1-bot/select 4096 700 root
/var/lib/l1-bot/service.log 452 644 root
/var/lib/l1-bot/stops 4096 700 root
/var/lib/l1-bot/tz51-l1-account.py 187351 600 root
/var/lib/l1-bot/unit-state.json 840 600 root
55492611	/root/l1-env
0.20.0
permitrootlogin without-password
pubkeyauthentication yes
passwordauthentication no
kbdinteractiveauthentication no
MainPID=1555954
NRestarts=0
Id=btc-recorder.service
ActiveState=active
UnitFileState=enabled
ActiveEnterTimestamp=Sat 2026-11-14 06:11:41 UTC

MainPID=1556307
NRestarts=0
Id=btc-rewardbook.service
ActiveState=active
UnitFileState=enabled
ActiveEnterTimestamp=Sat 2026-11-14 06:11:44 UTC

MainPID=1555970
NRestarts=0
Id=adv3-bot.service
ActiveState=active
UnitFileState=enabled
ActiveEnterTimestamp=Sat 2026-11-14 06:11:41 UTC

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
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10309844992
18931008	/root/tz53-work
499004574	/var/lib/btc-rewardbook
               total        used        free      shared  buff/cache   available
Mem:      1002127360   874418176    72581120       36864   203161600   127709184
Swap:     3250581504  1177075712  2073505792
3a2e6f293b716fdcf12d4d7089461cdcdb179c17	refs/heads/tz-53-l1-unit
```

### 2.8 The capture host and the branch

```
ready=1: 10428194816 bytes free on /var/lib, 7795535636 needed; MemAvailable 93978624, 86426834 needed; at 1795246785 2026-11-21T07:39:45Z
```

```
/root/tz53-work/stage/.tz52/research/tz52-l1-account.py 3326 188720 a425e67cce7178e425b04f899ad245cf31a38848bd2553dfacdbbbcdf3a73366 created
/root/tz53-work/stage/research/tz53-l1-account.py 3324 188378 e4b72d0e285f1d8736a056012d3c9056f7f103e8e899742e10e488932c910c94 created
/root/tz53-work/stage/engine/l1-bot.py 3656 188968 98851b3c0df447ed7c846edfbf18b9ea1611d12228a4d9a3c1fda3b4f22da214 created
/root/tz53-work/stage/engine/l1-bot.service 29 1014 a6305d0e7a220ea88f5a4d2be612cac35f3dbe527d7c3b7ed12fd7c47f956266 created
/root/tz53-work/stage/engine/tz33-reward-book-capture.py 3542 175160 a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670 created
/root/tz53-work/stage/engine/tz45-l0-rule-w.py 4299 233655 4720e78573e54b1325dd24af7c30e0de59bfb4c1879d309a23fa6bab6b32d2d4 created
/root/tz53-work/stage/b-deploy.sh 135 6789 373df4093b4ba4ad4fd093a173ad4c5396a52e2231b789814aef99ca23acf069 created
```

```
Sat Nov 21 07:40:13 AM UTC 2026
1795246813
2026-08-02 07:24:32
1
MemTotal:         978640 kB
MemAvailable:     101992 kB
SwapTotal:       3174396 kB
SwapFree:        2167180 kB
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10426785792
/var/lib/btc-recorder/btc-updown-5m/1794396600/manifest.json
4
3.12.3
/usr/bin/ssh
/usr/bin/scp
/usr/bin/gh
/usr/bin/tmux
/usr/bin/timeout
MainPID=1555954
NRestarts=0
Id=btc-recorder.service
ActiveState=active
UnitFileState=enabled
ActiveEnterTimestamp=Sat 2026-11-14 06:11:41 UTC

MainPID=1556307
NRestarts=0
Id=btc-rewardbook.service
ActiveState=active
UnitFileState=enabled
ActiveEnterTimestamp=Sat 2026-11-14 06:11:44 UTC

MainPID=1555970
NRestarts=0
Id=adv3-bot.service
ActiveState=active
UnitFileState=enabled
ActiveEnterTimestamp=Sat 2026-11-14 06:11:41 UTC

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
403490954	/var/lib/btc-rewardbook
357666167	/root/btc-forensics
31825625	/root/.claude-8j
2744
disabled
exit=1
inactive
exit=3
/root/tz50-work exit=1
/root/.ssh/live-host exit=0
/tmp/tmux-0/btc-l1 exit=1
/root/btc-5m-twap       04f0a15 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/tmp/claude-0/-root-btc-5m-twap/d5c9cb67-8a6b-551c-9c86-d4bd7a6f3650/scratchpad
total 40
drwx------ 10 root root 4096 Nov 21 07:37 .
drwx------ 40 root root 4096 Nov 21 07:37 ..
drwx------  3 root root 4096 Nov 20 18:51 0736470b-13a0-4e8d-931f-5ecf4df19205
drwx------  4 root root 4096 Nov 20 22:44 162a9fb6-80c1-5fc2-8efb-0d715f44d283
drwx------  5 root root 4096 Nov 20 19:13 450e33c9-580a-5524-ad84-641183f6ef0c
drwx------  3 root root 4096 Nov 20 22:44 5b734feb-443a-4557-9e38-5fb2090365b2
drwx------  3 root root 4096 Nov 20 18:51 6f0f41a7-6da7-5e8a-80e1-a2a85a4a8e5c
drwx------  3 root root 4096 Nov 21 07:37 8791beea-5eca-428f-970f-f69a3637e214
drwx------  4 root root 4096 Nov 21 07:37 d5c9cb67-8a6b-551c-9c86-d4bd7a6f3650
drwx------  3 root root 4096 Nov 20 18:55 dc25b96c-1173-470f-9a05-e5fdd91952fe
MemAvailable read 1 07:40:14: 145682432
```

```
2026-11-21T07:40:19.746009464Z
[2026-11-21T07:40:19Z] btc-rewardbook-archive.service read 1: inactive
[2026-11-21T07:40:19Z] MemAvailable read 1: 111366144 bytes, floor 86426834
[2026-11-21T07:40:19Z] available on /var/lib: 10426638336 bytes, floor 7795535636
[2026-11-21T07:40:19Z] ROOM: 10426638336 bytes available on /var/lib; the reward book's stream files 27999032 bytes in 2 files under 25 day directories; the room 10454637368; its margin over STREAM_FLOOR 7300000000 and PEAK 445535636: 2709101732 bytes
[2026-11-21T07:40:19Z] peak memory of this run: 34615296 bytes
[2026-11-21T07:40:19Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

```
2026-11-21T07:40:22.918684699Z
[2026-11-21T07:40:23Z] origin/main 04f0a15bbc2262d6298bb75bac658e1ea381c7e5: 125 paths under CryptoTZ/ and CryptoReports/; of the number TZ-53-: ['CryptoTZ/TZ-53-l1-unit.md'] and []
[2026-11-21T07:40:23Z] NUMBER PASS - 2 of 2
[2026-11-21T07:40:23Z] peak memory of this run: 34615296 bytes
[2026-11-21T07:40:23Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

```
2026-11-21T07:40:23.061735999Z
[2026-11-21T07:40:23Z] REF 04f0a15bbc2262d6298bb75bac658e1ea381c7e5	HEAD
[2026-11-21T07:40:23Z] REF 04f0a15bbc2262d6298bb75bac658e1ea381c7e5	refs/heads/main
[2026-11-21T07:40:23Z] REFS HEAD                                     1
[2026-11-21T07:40:23Z] REFS refs/heads/main                          1
[2026-11-21T07:40:23Z] REFS refs/heads/tz-*                          26
[2026-11-21T07:40:23Z] REFS refs/pull/*/head                         49
[2026-11-21T07:40:23Z] REFS refs/pull/*/merge                        1
[2026-11-21T07:40:23Z] REFS refs/tags/pairbook-streams-*             59
[2026-11-21T07:40:23Z] REFS refs/tags/rewardbook-streams-*           62
[2026-11-21T07:40:23Z] REFS refs/tags/tz-01a-dataset                 1
[2026-11-21T07:40:23Z] REFS refs/tags/tz-01a-dataset^{}              1
[2026-11-21T07:40:23Z] REFS refs/tags/tz-27-pairbook-streams         1
[2026-11-21T07:40:23Z] REFS refs/tags/tz-27-pairbook-streams^{}      1
[2026-11-21T07:40:23Z] REFS refs/tags/tz-44-l0-inputs                1
[2026-11-21T07:40:23Z] REFS refs/tags/tz-45-l0-rule-w-inputs         1
[2026-11-21T07:40:23Z] REFS 205 lines; refs/heads/tz-53-l1-unit absent
[2026-11-21T07:40:23Z] peak memory of this run: 34631680 bytes
[2026-11-21T07:40:23Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

```
2026-11-21T07:40:35.008426815Z
exit=0
256 SHA256:1xbA0Mhjj0NDXcLaefl9D8run7ZKh/oo0xUOmc06Qzo btc-5m-twap executor, capture host to live host (ED25519)
user root
identitiesonly yes
serveraliveinterval 15
hostkeyalias live-host
identityfile /root/.ssh/live-host
# Host live-host found: line 9 
live-host ED25519 SHA256:Y14Iy6okVrEz76M/JsR9hLre/54PtMAGXd6ZKDe4ZJw
vs-2348
root
work tree exit=1
tz50 tree exit=1
```

```
2026-11-21T07:40:44.775058008Z
exit=0
scp exit=0
scp exit=0
scp exit=0
e4b72d0e285f1d8736a056012d3c9056f7f103e8e899742e10e488932c910c94  tz53-l1-account.py
373df4093b4ba4ad4fd093a173ad4c5396a52e2231b789814aef99ca23acf069  b-deploy.sh
98851b3c0df447ed7c846edfbf18b9ea1611d12228a4d9a3c1fda3b4f22da214  engine/l1-bot.py
a6305d0e7a220ea88f5a4d2be612cac35f3dbe527d7c3b7ed12fd7c47f956266  engine/l1-bot.service
a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670  engine/tz33-reward-book-capture.py
4720e78573e54b1325dd24af7c30e0de59bfb4c1879d309a23fa6bab6b32d2d4  engine/tz45-l0-rule-w.py
```

```
2026-11-21T08:23:21.107151605Z
fetch exit=0
[2026-11-21T08:23:21Z] origin/main 04f0a15bbc2262d6298bb75bac658e1ea381c7e5: 125 paths under CryptoTZ/ and CryptoReports/; of the number TZ-53-: ['CryptoTZ/TZ-53-l1-unit.md'] and []
[2026-11-21T08:23:21Z] NUMBER PASS - 2 of 2
[2026-11-21T08:23:21Z] peak memory of this run: 34762752 bytes
[2026-11-21T08:23:21Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

```
2026-11-21T08:23:26.242152644Z
Preparing worktree (new branch 'tz-53-l1-unit')
branch 'tz-53-l1-unit' set up to track 'origin/main'.
HEAD is now at 04f0a15 Add files via upload
worktree exit=0
/root/tz53-work/wt/.tz52/research/tz52-l1-account.py 3326 188720 a425e67cce7178e425b04f899ad245cf31a38848bd2553dfacdbbbcdf3a73366 created
/root/tz53-work/wt/research/tz53-l1-account.py 3324 188378 e4b72d0e285f1d8736a056012d3c9056f7f103e8e899742e10e488932c910c94 created
/root/tz53-work/wt/engine/l1-bot.py 3656 188968 98851b3c0df447ed7c846edfbf18b9ea1611d12228a4d9a3c1fda3b4f22da214 created
/root/tz53-work/wt/deploy/systemd/l1-bot.service 29 1014 a6305d0e7a220ea88f5a4d2be612cac35f3dbe527d7c3b7ed12fd7c47f956266 created
exit=0
```

```
2026-11-21T08:23:36.158391770Z
[2026-11-21T08:23:36Z] REF 04f0a15bbc2262d6298bb75bac658e1ea381c7e5	HEAD
[2026-11-21T08:23:36Z] REF 04f0a15bbc2262d6298bb75bac658e1ea381c7e5	refs/heads/main
[2026-11-21T08:23:36Z] REFS HEAD                                     1
[2026-11-21T08:23:36Z] REFS refs/heads/main                          1
[2026-11-21T08:23:36Z] REFS refs/heads/tz-*                          26
[2026-11-21T08:23:36Z] REFS refs/pull/*/head                         49
[2026-11-21T08:23:36Z] REFS refs/pull/*/merge                        1
[2026-11-21T08:23:36Z] REFS refs/tags/pairbook-streams-*             59
[2026-11-21T08:23:36Z] REFS refs/tags/rewardbook-streams-*           62
[2026-11-21T08:23:36Z] REFS refs/tags/tz-01a-dataset                 1
[2026-11-21T08:23:36Z] REFS refs/tags/tz-01a-dataset^{}              1
[2026-11-21T08:23:36Z] REFS refs/tags/tz-27-pairbook-streams         1
[2026-11-21T08:23:36Z] REFS refs/tags/tz-27-pairbook-streams^{}      1
[2026-11-21T08:23:36Z] REFS refs/tags/tz-44-l0-inputs                1
[2026-11-21T08:23:36Z] REFS refs/tags/tz-45-l0-rule-w-inputs         1
[2026-11-21T08:23:36Z] REFS 205 lines; refs/heads/tz-53-l1-unit absent
[2026-11-21T08:23:36Z] peak memory of this run: 34877440 bytes
[2026-11-21T08:23:36Z] refused by the hook: 0; lookups 0, requests 0
exit=0
commit exit=0
remote: 
remote: Create a pull request for 'tz-53-l1-unit' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-53-l1-unit        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-53-l1-unit -> tz-53-l1-unit
branch 'tz-53-l1-unit' set up to track 'origin/tz-53-l1-unit'.
push exit=0
2026-11-21T08:23:38.814546374Z
3a2e6f293b716fdcf12d4d7089461cdcdb179c17	refs/heads/tz-53-l1-unit
3a2e6f293b716fdcf12d4d7089461cdcdb179c17
29	0	deploy/systemd/l1-bot.service
3656	0	engine/l1-bot.py
3324	0	research/tz53-l1-account.py
```

```
2026-11-21T08:23:45.255245288Z
https://github.com/seahomebatumi-ai/btc-5m-twap/pull/51
exit=0
```

```
2026-11-21T08:23:49.231208065Z
{"head":"1719ff46d22444aa7a4f05e7a735cfc4856240ab","merged":false,"number":50,"state":"open"}
exit=0
{"head":"1719ff46d22444aa7a4f05e7a735cfc4856240ab","merged":false,"number":50,"state":"closed"}
exit=0
```

```
2026-11-21T08:24:06.086457453Z
[2026-11-21T08:24:06Z] running 2569924 started 2026-11-20T18:51:37Z claude
[2026-11-21T08:24:06Z] running 2569934 started 2026-11-20T18:51:39Z claude
[2026-11-21T08:24:06Z] running 2569943 started 2026-11-20T18:51:39Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-21T08:24:06Z] running 2569966 started 2026-11-20T18:51:41Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-21T08:24:06Z] running 2570476 started 2026-11-20T18:55:31Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-21T08:24:06Z] running 2593738 started 2026-11-20T22:44:37Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-21T08:24:06Z] running 2661586 started 2026-11-21T07:37:41Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-21T08:24:06Z] 0736470b-13a0-4e8d-931f-5ecf4df19205 born 2026-11-20T18:51:41Z: live, process [2569924, 2569934, 2569943, 2569966]
[2026-11-21T08:24:06Z] 162a9fb6-80c1-5fc2-8efb-0d715f44d283 born 2026-11-20T22:44:39Z: live, process [2593738]
[2026-11-21T08:24:06Z] 450e33c9-580a-5524-ad84-641183f6ef0c born 2026-11-20T18:55:32Z: live, process [2570476]
[2026-11-21T08:24:06Z] 5b734feb-443a-4557-9e38-5fb2090365b2 born 2026-11-20T22:44:38Z: live, process [2593738]
[2026-11-21T08:24:06Z] 6f0f41a7-6da7-5e8a-80e1-a2a85a4a8e5c born 2026-11-20T18:51:42Z: live, process [2569924, 2569934, 2569943, 2569966]
[2026-11-21T08:24:06Z] 8791beea-5eca-428f-970f-f69a3637e214 born 2026-11-21T07:37:41Z: live, process [2661586]
[2026-11-21T08:24:06Z] dc25b96c-1173-470f-9a05-e5fdd91952fe born 2026-11-20T18:55:31Z: live, process [2570476]
[2026-11-21T08:24:06Z] peak memory of this run: 34762752 bytes
[2026-11-21T08:24:06Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

### 2.9 §9 — B-RECLAIM-LIVE and B-RECLAIM-OWN

**B-RECLAIM-LIVE**, from the session:

```
$ date -u +%FT%T.%NZ; R 'rm -rf /root/tz53-work; test -e /root/tz53-work; echo "exit=$?"'
2026-11-21T08:57:14.073260212Z
exit=1
```

**B-RECLAIM-OWN**, every line of it, verbatim from the session (its output is written to no file, TZ-51 §9):

```
$ (cd /root/tz53-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz53-work/wt/research/tz53-l1-account.py reclaim /root/tz53-work); echo "reclaim exit=$?"
[2026-11-21T08:57:22Z] reclaim: /root/tz53-work/wt skipped: no file but its HEAD's, and HEAD 3a2e6f293b716fdcf12d4d7089461cdcdb179c17 is its upstream's
[2026-11-21T08:57:22Z] R copied fcb7039578e4a01494f28584ee73eb1700ff5e777eb44c0f622156eda19a6731 /root/btc-forensics/tz53-work--live-logs--40-host-before.log
[2026-11-21T08:57:22Z] R copied ee137d6508e6e52e94fae81df99f66912e15609aa8dd66c92ea8032452cbdbc0 /root/btc-forensics/tz53-work--live-logs--41-geoblock.log
[2026-11-21T08:57:22Z] R copied d6247bd6fd729c3b227a72c3a6720d4d201035ab52344cc679e543a823369a12 /root/btc-forensics/tz53-work--live-logs--42-sshd.log
[2026-11-21T08:57:22Z] R copied ad79e0d92ad92813304a987d93df16c5dd10c343e3413c7b22000ba899851f08 /root/btc-forensics/tz53-work--live-logs--43-l1-before.log
[2026-11-21T08:57:22Z] R copied 54fd94c86e9b8d7ad5ef530fd871eb714202b8352b27a4ae68c4585bc761d85f /root/btc-forensics/tz53-work--live-logs--50-selftest.log
[2026-11-21T08:57:22Z] R copied da9045870876dba1021007313d8059b31931dccc3154eade7a0ddb5708626f6b /root/btc-forensics/tz53-work--live-logs--53-env.log
[2026-11-21T08:57:22Z] R copied 705d879322472a1dab46bbe1e20949f5e3f9cd81d2d1e36c30f5ee80ec5a5391 /root/btc-forensics/tz53-work--live-logs--54-sdk-selftest.log
[2026-11-21T08:57:22Z] R copied 1458fb2b1a0b8c4e71b49dedee68440ee2d99ba838f684ff8c0caf4b42e7cc35 /root/btc-forensics/tz53-work--live-logs--56-key.log
[2026-11-21T08:57:22Z] R copied 97f505f52c7f36fdb57c5598423a3bd2dc34933724a78c73e1d87c59b9f5ce48 /root/btc-forensics/tz53-work--live-logs--57-engine-selftest.log
[2026-11-21T08:57:22Z] R copied 36806632b56e860ac5f6fdb2355265a9cc53292303b1812c8cf5046a6c65ad3c /root/btc-forensics/tz53-work--live-logs--58-engine-sdk-selftest.log
[2026-11-21T08:57:22Z] R copied 6ceb0175b433f4bd8e3073dcf177a882c429b93de65c1849766f8c1198a34ee6 /root/btc-forensics/tz53-work--live-logs--60-deploy.log
[2026-11-21T08:57:22Z] R copied d51540f62399541fd5afa901d40a2037bd6463c2e9b61e2e61b1a13bff5d4677 /root/btc-forensics/tz53-work--live-logs--61-ready-1.log
[2026-11-21T08:57:22Z] R copied 50cf1d9f01fdd14aa086573d5c357e39965133eb82f2b7e1dc16aab488543be1 /root/btc-forensics/tz53-work--live-logs--61-ready-2.log
[2026-11-21T08:57:22Z] R copied 5e0561e17ead8feeb08ef4713fcb4e21274ef325efc53b92384058e086a4468d /root/btc-forensics/tz53-work--live-logs--62-unit-after.log
[2026-11-21T08:57:22Z] R copied 37ce52c50ccd6dfd5fbb5a32db5d0d95a8569ea763f83defffd5700a84a87e9d /root/btc-forensics/tz53-work--live-logs--78-sshd-after.log
[2026-11-21T08:57:22Z] R copied c92df736cbed35b076ecc6195ef253ea919fd0e39a684ed56dc503401ca72cc7 /root/btc-forensics/tz53-work--live-logs--79-host-after.log
[2026-11-21T08:57:22Z] R copied 4753d8f71d9315cdecc795f56bb0922a3da860835726bd1215aff58dd450cc14 /root/btc-forensics/tz53-work--live-logs--81-keep.log
[2026-11-21T08:57:22Z] R copied f2abb1e42d1e25f54c412c77011c6bb920e6fed4f877a7ebb1c7907ecbb592d4 /root/btc-forensics/tz53-work--logs--00-ready.log
[2026-11-21T08:57:22Z] R copied 3410f1eafa7a2fabc25b94b85ee4ca5a7f94edc4a5419e67ae4108af6abe6304 /root/btc-forensics/tz53-work--logs--01-stage.log
[2026-11-21T08:57:22Z] R copied 96464d63bce87eea0c023cb99227769b57de5ac6f63897003d9df005b1a41db6 /root/btc-forensics/tz53-work--logs--02-fingerprint.log
[2026-11-21T08:57:22Z] R copied 6c4a056df4f6750e588050dce361077d5ff1ae7c5143e4f39e385266f19d60f7 /root/btc-forensics/tz53-work--logs--03-host-gate.log
[2026-11-21T08:57:22Z] R copied deda772689ebf90ca4baf4290f478c31d9b620fef7e691f63133b798647370cb /root/btc-forensics/tz53-work--logs--04-room.log
[2026-11-21T08:57:22Z] R copied 75cb24d93f09d933c7dd8c5fcb2936e427dc7aca54f961d24a55b8f2043b68b1 /root/btc-forensics/tz53-work--logs--05-number.log
[2026-11-21T08:57:22Z] R copied 853bfe59266354cddd2d4ea20596051649324f865639e85f24313671b783f1c7 /root/btc-forensics/tz53-work--logs--05-refs.log
[2026-11-21T08:57:22Z] R copied 09c7cebe2b15f06384fbfe84c745579f2cf1c354fea1ae38e4248107f773e6af /root/btc-forensics/tz53-work--logs--06-access.log
[2026-11-21T08:57:22Z] R copied 3ca8a6ba870c31d1a2e1a3a2aec20ca35bbfcc952940a4e4075c77baab26a760 /root/btc-forensics/tz53-work--logs--07-copy.log
[2026-11-21T08:57:22Z] R copied b38fa8cf59ab156110b0a4f2d3d14fd5cbb011cfaa13b7b22a33f22787193cd5 /root/btc-forensics/tz53-work--logs--08-methods.log
[2026-11-21T08:57:22Z] R copied 103653783e1a25db57a80af252634c7d5191db9a9cdfcd37659565e2ddfd2216 /root/btc-forensics/tz53-work--logs--10-number.log
[2026-11-21T08:57:22Z] R copied 51f6ee7ee76f052e638b39962e78a5a1d9ce0189828f4f918edc0ac028302f93 /root/btc-forensics/tz53-work--logs--11-worktree.log
[2026-11-21T08:57:22Z] R copied 45d5d0cc37630f7bffad072da9daa680043be57a3fd7a63d32f581fce35b76aa /root/btc-forensics/tz53-work--logs--12-fingerprint.log
[2026-11-21T08:57:22Z] R copied db53af31ba639822aedd53f4e041feb08e1edf7465a3b747ab40720adeab10c1 /root/btc-forensics/tz53-work--logs--13-push.log
[2026-11-21T08:57:22Z] R copied 5409d9d7c50ae2b0ed77cf0e8c89bc9f0a7bd7c8b42998c2d3a9847927b6a572 /root/btc-forensics/tz53-work--logs--14-pr.log
[2026-11-21T08:57:22Z] R copied 1bfae8930917508cce14525d2fadc9ac0e1aba495fc6c84f52b02e9d540e6a42 /root/btc-forensics/tz53-work--logs--15-pr50.log
[2026-11-21T08:57:22Z] R copied e1eda1121dc1ac84cd8eda2f375ad6dbfbb2a21260fbda5990c7acec5026dce0 /root/btc-forensics/tz53-work--logs--20-selftest.log
[2026-11-21T08:57:22Z] R copied a094a0a4b81dd22fda21b1e6ccb64e0169fe6bb15839254318b8267ec44cab86 /root/btc-forensics/tz53-work--logs--30-scratch.log
[2026-11-21T08:57:22Z] R copied 3d4a2d334f0dccadf2e7879c3c8669dbadbce48fd73696accb76b6e21f39cc5b /root/btc-forensics/tz53-work--logs--59-deploy-start.log
[2026-11-21T08:57:22Z] R copied 2f840e968fa3f60545c5e39710cbb55423a78a8520ba97689fd7d9b504e25e44 /root/btc-forensics/tz53-work--logs--80-live-copy.log
[2026-11-21T08:57:22Z] R copied 566accf9fd590f5ba8519054f24dbd9a4c73cde483ac4aa236344851ba901f3e /root/btc-forensics/tz53-work--logs--88-methods-after.log
[2026-11-21T08:57:22Z] R copied 3dd18915f3165ff43cac9474a3b4437fa738de8a4b52fd11ff976e03a89d2d0b /root/btc-forensics/tz53-work--logs--90-closing.log
[2026-11-21T08:57:22Z] R copied dfc62483794deaeb1dd904b617f97db8a943f7fc95f0d1008df672d85379f832 /root/btc-forensics/tz53-work--logs--99-selfcheck.log
[2026-11-21T08:57:22Z] R copied 373df4093b4ba4ad4fd093a173ad4c5396a52e2231b789814aef99ca23acf069 /root/btc-forensics/tz53-work--stage--b-deploy.sh
[2026-11-21T08:57:22Z] R copied 98851b3c0df447ed7c846edfbf18b9ea1611d12228a4d9a3c1fda3b4f22da214 /root/btc-forensics/tz53-work--stage--engine--l1-bot.py
[2026-11-21T08:57:22Z] R copied a6305d0e7a220ea88f5a4d2be612cac35f3dbe527d7c3b7ed12fd7c47f956266 /root/btc-forensics/tz53-work--stage--engine--l1-bot.service
[2026-11-21T08:57:22Z] R copied a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670 /root/btc-forensics/tz53-work--stage--engine--tz33-reward-book-capture.py
[2026-11-21T08:57:22Z] R copied 4720e78573e54b1325dd24af7c30e0de59bfb4c1879d309a23fa6bab6b32d2d4 /root/btc-forensics/tz53-work--stage--engine--tz45-l0-rule-w.py
[2026-11-21T08:57:22Z] R copied e4b72d0e285f1d8736a056012d3c9056f7f103e8e899742e10e488932c910c94 /root/btc-forensics/tz53-work--stage--research--tz53-l1-account.py
[2026-11-21T08:57:22Z] RECLAIM PASS: 46 files considered, 46 copied, 0 already held; the forensic store 2744 -> 2790 files
[2026-11-21T08:57:22Z] peak memory of this run: 35155968 bytes
[2026-11-21T08:57:22Z] refused by the hook: 0; lookups 0, requests 0
reclaim exit=0
$ cd /root/btc-5m-twap && git -C /root/btc-5m-twap worktree remove /root/tz53-work/wt; echo "exit=$?"
exit=0
$ rm -rf /root/tz53-work; echo "exit=$?"
exit=0
$ test -e /root/tz53-work; echo "exit=$?"
exit=1
$ test -e /tmp/tmux-0/btc-l1; echo "tmux socket exit=$?"
tmux socket exit=1
$ git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
/root/btc-5m-twap       04f0a15 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
$ find /root/btc-forensics -type f | wc -l
2790
$ df -B1 --output=source,size,avail /var/lib/btc-recorder
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10322591744
```

### 2.10 The files of this run

Every log of both hosts, and the stage's six files, as `reclaim` copied them into the forensic store as
`/root/btc-forensics/tz53-work--<path with / as -->`:

| file under `/root/tz53-work/` | lines | bytes | SHA-256 |
|---|---|---|---|
| `logs/00-ready.log` | 1 | 139 | `f2abb1e42d1e25f54c412c77011c6bb920e6fed4f877a7ebb1c7907ecbb592d4` |
| `logs/01-stage.log` | 7 | 915 | `3410f1eafa7a2fabc25b94b85ee4ca5a7f94edc4a5419e67ae4108af6abe6304` |
| `logs/02-fingerprint.log` | 78 | 13023 | `96464d63bce87eea0c023cb99227769b57de5ac6f63897003d9df005b1a41db6` |
| `logs/03-host-gate.log` | 76 | 2205 | `6c4a056df4f6750e588050dce361077d5ff1ae7c5143e4f39e385266f19d60f7` |
| `logs/04-room.log` | 8 | 651 | `deda772689ebf90ca4baf4290f478c31d9b620fef7e691f63133b798647370cb` |
| `logs/05-number.log` | 6 | 396 | `75cb24d93f09d933c7dd8c5fcb2936e427dc7aca54f961d24a55b8f2043b68b1` |
| `logs/05-refs.log` | 20 | 1325 | `853bfe59266354cddd2d4ea20596051649324f865639e85f24313671b783f1c7` |
| `logs/06-access.log` | 14 | 408 | `09c7cebe2b15f06384fbfe84c745579f2cf1c354fea1ae38e4248107f773e6af` |
| `logs/07-copy.log` | 11 | 597 | `3ca8a6ba870c31d1a2e1a3a2aec20ca35bbfcc952940a4e4075c77baab26a760` |
| `logs/08-methods.log` | 6 | 363 | `b38fa8cf59ab156110b0a4f2d3d14fd5cbb011cfaa13b7b22a33f22787193cd5` |
| `logs/10-number.log` | 7 | 409 | `103653783e1a25db57a80af252634c7d5191db9a9cdfcd37659565e2ddfd2216` |
| `logs/11-worktree.log` | 10 | 721 | `51f6ee7ee76f052e638b39962e78a5a1d9ce0189828f4f918edc0ac028302f93` |
| `logs/12-fingerprint.log` | 78 | 13023 | `45d5d0cc37630f7bffad072da9daa680043be57a3fd7a63d32f581fce35b76aa` |
| `logs/13-push.log` | 35 | 1944 | `db53af31ba639822aedd53f4e041feb08e1edf7465a3b747ab40720adeab10c1` |
| `logs/14-pr.log` | 3 | 94 | `5409d9d7c50ae2b0ed77cf0e8c89bc9f0a7bd7c8b42998c2d3a9847927b6a572` |
| `logs/15-pr50.log` | 5 | 235 | `1bfae8930917508cce14525d2fadc9ac0e1aba495fc6c84f52b02e9d540e6a42` |
| `logs/20-selftest.log` | 206 | 19535 | `e1eda1121dc1ac84cd8eda2f375ad6dbfbb2a21260fbda5990c7acec5026dce0` |
| `logs/30-scratch.log` | 18 | 1806 | `a094a0a4b81dd22fda21b1e6ccb64e0169fe6bb15839254318b8267ec44cab86` |
| `logs/59-deploy-start.log` | 6 | 171 | `3d4a2d334f0dccadf2e7879c3c8669dbadbce48fd73696accb76b6e21f39cc5b` |
| `logs/80-live-copy.log` | 25 | 1153 | `2f840e968fa3f60545c5e39710cbb55423a78a8520ba97689fd7d9b504e25e44` |
| `logs/88-methods-after.log` | 6 | 364 | `566accf9fd590f5ba8519054f24dbd9a4c73cde483ac4aa236344851ba901f3e` |
| `logs/90-closing.log` | 89 | 3051 | `3dd18915f3165ff43cac9474a3b4437fa738de8a4b52fd11ff976e03a89d2d0b` |
| `logs/99-selfcheck.log` | 8 | 202 | `dfc62483794deaeb1dd904b617f97db8a943f7fc95f0d1008df672d85379f832` |
| `live-logs/40-host-before.log` | 26 | 2207 | `fcb7039578e4a01494f28584ee73eb1700ff5e777eb44c0f622156eda19a6731` |
| `live-logs/41-geoblock.log` | 8 | 576 | `ee137d6508e6e52e94fae81df99f66912e15609aa8dd66c92ea8032452cbdbc0` |
| `live-logs/42-sshd.log` | 10 | 533 | `d6247bd6fd729c3b227a72c3a6720d4d201035ab52344cc679e543a823369a12` |
| `live-logs/43-l1-before.log` | 9 | 137 | `ad79e0d92ad92813304a987d93df16c5dd10c343e3413c7b22000ba899851f08` |
| `live-logs/50-selftest.log` | 206 | 19535 | `54fd94c86e9b8d7ad5ef530fd871eb714202b8352b27a4ae68c4585bc761d85f` |
| `live-logs/53-env.log` | 9 | 813 | `da9045870876dba1021007313d8059b31931dccc3154eade7a0ddb5708626f6b` |
| `live-logs/54-sdk-selftest.log` | 116 | 13600 | `705d879322472a1dab46bbe1e20949f5e3f9cd81d2d1e36c30f5ee80ec5a5391` |
| `live-logs/56-key.log` | 7 | 422 | `1458fb2b1a0b8c4e71b49dedee68440ee2d99ba838f684ff8c0caf4b42e7cc35` |
| `live-logs/57-engine-selftest.log` | 42 | 4657 | `97f505f52c7f36fdb57c5598423a3bd2dc34933724a78c73e1d87c59b9f5ce48` |
| `live-logs/58-engine-sdk-selftest.log` | 82 | 9016 | `36806632b56e860ac5f6fdb2355265a9cc53292303b1812c8cf5046a6c65ad3c` |
| `live-logs/60-deploy.log` | 115 | 11761 | `6ceb0175b433f4bd8e3073dcf177a882c429b93de65c1849766f8c1198a34ee6` |
| `live-logs/61-ready-1.log` | 12 | 1133 | `d51540f62399541fd5afa901d40a2037bd6463c2e9b61e2e61b1a13bff5d4677` |
| `live-logs/61-ready-2.log` | 12 | 1133 | `50cf1d9f01fdd14aa086573d5c357e39965133eb82f2b7e1dc16aab488543be1` |
| `live-logs/62-unit-after.log` | 251 | 7356 | `5e0561e17ead8feeb08ef4713fcb4e21274ef325efc53b92384058e086a4468d` |
| `live-logs/78-sshd-after.log` | 10 | 533 | `37ce52c50ccd6dfd5fbb5a32db5d0d95a8569ea763f83defffd5700a84a87e9d` |
| `live-logs/79-host-after.log` | 26 | 2206 | `c92df736cbed35b076ecc6195ef253ea919fd0e39a684ed56dc503401ca72cc7` |
| `live-logs/81-keep.log` | 25 | 1088 | `4753d8f71d9315cdecc795f56bb0922a3da860835726bd1215aff58dd450cc14` |
| `stage/research/tz53-l1-account.py` | 3324 | 188378 | `e4b72d0e285f1d8736a056012d3c9056f7f103e8e899742e10e488932c910c94` |
| `stage/engine/l1-bot.py` | 3656 | 188968 | `98851b3c0df447ed7c846edfbf18b9ea1611d12228a4d9a3c1fda3b4f22da214` |
| `stage/engine/l1-bot.service` | 29 | 1014 | `a6305d0e7a220ea88f5a4d2be612cac35f3dbe527d7c3b7ed12fd7c47f956266` |
| `stage/engine/tz33-reward-book-capture.py` | 3542 | 175160 | `a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670` |
| `stage/engine/tz45-l0-rule-w.py` | 4299 | 233655 | `4720e78573e54b1325dd24af7c30e0de59bfb4c1879d309a23fa6bab6b32d2d4` |
| `stage/b-deploy.sh` | 135 | 6789 | `373df4093b4ba4ad4fd093a173ad4c5396a52e2231b789814aef99ca23acf069` |

### 2.11 Every mode's peak — V21

Recorded against the models of TZ-53 §0.4. The checker's standard-library modes are each under `43,213,417`; its
client modes and the engine's are each under `137,458,839`. Every row holds, asserted by this report's own
generator. Each run that reads them read its floors at its start, and every read is in the logs above.

| host | log | code | runs | peaks, bytes | under |
|---|---|---|---|---|---|
| capture | `02-fingerprint.log` | the checker, standard library | 1 | 35,536,896 | `43,213,417` |
| capture | `04-room.log` | the checker, standard library | 1 | 34,615,296 | `43,213,417` |
| capture | `05-number.log` | the checker, standard library | 1 | 34,615,296 | `43,213,417` |
| capture | `05-refs.log` | the checker, standard library | 1 | 34,631,680 | `43,213,417` |
| capture | `08-methods.log` | the checker, standard library | 1 | 34,500,608 | `43,213,417` |
| capture | `10-number.log` | the checker, standard library | 1 | 34,762,752 | `43,213,417` |
| capture | `12-fingerprint.log` | the checker, standard library | 1 | 35,926,016 | `43,213,417` |
| capture | `13-push.log` | the checker, standard library | 1 | 34,877,440 | `43,213,417` |
| capture | `20-selftest.log` | the checker, standard library | 1 | 35,663,872 | `43,213,417` |
| capture | `30-scratch.log` | the checker, standard library | 1 | 34,762,752 | `43,213,417` |
| capture | `88-methods-after.log` | the checker, standard library | 1 | 34,484,224 | `43,213,417` |
| live | `40-host-before.log` | the checker, standard library | 1 | 35,069,952 | `43,213,417` |
| live | `41-geoblock.log` | the checker, standard library | 1 | 37,818,368 | `43,213,417` |
| live | `42-sshd.log` | the checker, standard library | 1 | 35,196,928 | `43,213,417` |
| live | `50-selftest.log` | the checker, standard library | 1 | 35,856,384 | `43,213,417` |
| live | `53-env.log` | the checker, client | 1 | 76,623,872 | `137,458,839` |
| live | `54-sdk-selftest.log` | the checker, client | 1 | 97,210,368 | `137,458,839` |
| live | `56-key.log` | the checker, client | 1 | 76,488,704 | `137,458,839` |
| live | `57-engine-selftest.log` | the engine | 1 | 69,341,184 | `137,458,839` |
| live | `58-engine-sdk-selftest.log` | the engine | 1 | 107,470,848 | `137,458,839` |
| live | `60-deploy.log` | the engine | 10 | 34,680,832 to 122,187,776 | `137,458,839` |
| live | `62-unit-after.log` | the engine | 3 | 34,553,856 to 34,680,832 | `137,458,839` |
| live | `78-sshd-after.log` | the checker, standard library | 1 | 35,069,952 | `43,213,417` |
| live | `79-host-after.log` | the checker, standard library | 1 | 35,053,568 | `43,213,417` |

---

## 3. Publication

- **Branch** `tz-53-l1-unit`, commit `3a2e6f293b716fdcf12d4d7089461cdcdb179c17`, on `origin` at 08:23:38 UTC
  (`13-push.log`). It holds three files, each new: `engine/l1-bot.py`, `deploy/systemd/l1-bot.service` and
  `research/tz53-l1-account.py`, at §0.1's SHA-256.
- **Pull request #51**, `tz-53-l1-unit` into `main`, opened by `gh pr create` (`14-pr.log`). Merge is the Boss's,
  after the Architect's verdict.
- **Pull request #50** was closed unmerged, and its branch `tz-52-l1-round-trip` is kept at `1719ff4…`
  (`15-pr50.log`).
- **No Release, no asset:** no file of this run is held by one. The logs and the stage are in the forensic store
  (§2.10).
- **`b-deploy.sh`** is staged and never committed. It is quoted by its SHA-256, `373df4093b4ba4ad4fd093a173ad4c5396a52e2231b789814aef99ca23acf069`.
- **Contract §4.2's self-check** (`99-selfcheck.log`), `C` the branch's commit:

```
2026-11-21T08:53:44.951839786Z
0
deploy/systemd/l1-bot.service
engine/l1-bot.py
research/tz53-l1-account.py
29	0	deploy/systemd/l1-bot.service
3656	0	engine/l1-bot.py
3324	0	research/tz53-l1-account.py
```

`0`: the implementation commit is not on `main`. The branch carries the three implementation files alone. No
`.parquet` or `.zip` is on `main`.

---

## 4. Gate

**G-DEPLOY — `B-DEPLOY END exit=0`: G-INSTALL to G-LIVE, each PASS** (TZ-53 §4). **Read: PASS.**

| gate | as TZ-53 §4 fixes it | read | |
|---|---|---|---|
| E-SELF | `38` of `38` and `29` of `29`, the refusals `0` and `2` | `38` of `38`, `0`; `29` of `29`, `2` | PASS |
| G-INSTALL | the four files and the unit file at §0.1's SHA-256, `cmp` equal; `loaded`, `disabled` | 8 lines `OK`; `UnitFileState=disabled`, `LoadState` `loaded` (B-DEPLOY's gate) | PASS |
| G-READY | six checks and G-GEO | read 1 `5 of 6` (capital `79.962913`); read 2 `G-READY PASS: 6 of 6, G-GEO PASS` | PASS |
| G-PROVE | `G-PROVE PASS`, eight gates, record written; G-HB recorded | `G-PROVE PASS`, 8 of 8, `prove-1.json` `3894` bytes; G-HB accepted, gone after `13.7` s | PASS |
| G-HOLD | 45 s on: `ExecMainStatus` `3`, `NRestarts` `0`, not `active`/`activating`; its two lines | `3`, `0`, `failed`; both lines | PASS |
| G-CLEAR | `clear-stop` exit `0`, the record in `stops/` | moved to `stops/stop-1795250209.json`; none standing | PASS |
| G-UNIT | 60 s: `active`, `NRestarts` `0`, `enabled`, `SERVE start: geoblock PASS` | `active`, `0`, `enabled`, the line at 08:37:38 | PASS |
| G-LIVE | 900 s: `active`, `NRestarts` `0`, the same `MainPID`, no stop record | `active`, `0`, `49171` = `49171`, none | PASS |
| G-PRINT | `0` and `0` | `0` and `0` | PASS |

Every reading is a count or an equality, so there is no number to round. **Nothing was tuned to reach the gate, and
no gate was re-read after a FAIL other than as B-DEPLOY's own G-READY loop allows** (13 reads, 600 s apart; it
passed at read 2).

---

## 5. Validation

| # | check | count | asserted |
|---|---|---|---|
| V1 | `FINGERPRINT PASS` at §0.2 and §3.1, §0.2's line | 2 of 2; 64 of 64 frozen | asserted by the checker |
| V2 | `NUMBER PASS - 2 of 2` at §0.5 and §3.1; refs 205 lines by kind; the branch absent before the push | 2 of 2 | asserted |
| V3 | §0.1's script: six `created` into the stage, three into the worktree, each at §0.1's SHA-256; the live host's six the same | 6, 3, 6 | asserted by the script; the live copy's by the Executor against §0.1's table |
| V4 | the branch: three paths, `29 0`, `3656 0`, `3324 0`; #50 read `open` and closed unmerged | 3; 1 | asserted by the Executor's reads (`13-push.log`, `15-pr50.log`) |
| V5 | the capture host gate, seven checks; the room's margin `2,709,101,732` | 7 of 7 | asserted by the Executor's reads; `room` asserts its floors |
| V6 | the access: `exit=0`, TZ-47's key, `vs-2348`, `root`, both trees absent | 6 of 6 | asserted by the Executor's reads |
| V7 | the live host gate at `host before` and `host after`; LS's nine `PATH` lines and root's one key; `43-l1-before.log`'s three names, `svc exit=1`, `unit exit=1`, both `inactive` | 5 of 5 twice; 9; 3 | the gate asserted by `host`; LS and `43` by the Executor |
| V8 | `G-GEO PASS` at §0.6, in G-READY (twice) and in G-PROVE | 4 of 4 | asserted |
| V9 | G-SSH K1 to K6, at §0.6 and §3.10 | 6 of 6 twice | asserted |
| V10 | the checker's `141 of 141`, refused `5`, on both hosts; `32 of 32`, refused `2` | 3 runs | asserted |
| V11 | the scratch directories: 7 live, 0 earlier; B-RECLAIM-SCRATCH empty, skipped | 7; 0 | asserted by `scratch` |
| V12 | `G-ENV installed PASS`: 34 of 34, 1,373 RECORD entries over 1,367 paths, absent `[]`, another hash `[]` | 1 | asserted |
| V13 | `G-KEY`: present, kept, `0600`, 67 bytes | 1 | asserted |
| V14 | E-SELF: `38` of `38`, refused `0`; `29` of `29`, refused `2` | 2 runs | asserted by the engine |
| V15 | G-INSTALL and G-READY: every line of `60-deploy.log` to them and both `61-ready-N.log`, the balance and allowances as printed | 2 reads | asserted by B-DEPLOY |
| V16 | G-PROVE: every `PROVE` line, the record's path and `3894` bytes | 8 of 8 gates; 4 orders | asserted by B-DEPLOY (`eng prove || fail`) |
| V17 | G-HOLD, G-CLEAR, G-UNIT and G-LIVE, each read with its instant; `B-DEPLOY END exit=0` | 4 of 4 | asserted by B-DEPLOY |
| V18 | §3 step 11: `active`, `NRestarts` `0`, five SHA-256 at §0.1's, `status`'s lines | 5 of 5 | asserted by the Executor's reads |
| V19 | G-PRINT: `0` and `0` | 2 counts | asserted by the Executor against `0` |
| V20 | `81-keep.log`: `a425e67c…`, `exit=1`; `scp exit=0`, `diff exit=0`; the capture host's units as at §0.3; §4.2's self-check `0`, three paths, nothing | all | asserted by the Executor's reads |
| V21 | every mode's printed peak under its model (§2.11) | every row | recorded; held by this report's generator |
| V22 | TZ-51 §9 under R′: B-RECLAIM-LIVE, `RECLAIM PASS`, both trees gone, the worktrees two (§2.9) | see §2.9 | asserted by `reclaim` and `test -e` |

---

## 6. What could not be implemented as written

1. **The session paused for 41 minutes, 07:41 to 08:22 UTC, between `host before` and `43-l1-before.log`.** The
   Executor's usage limit ran out, and the Boss resumed the session after it reset. Nothing ran in the gap. On
   resuming, the Executor read both hosts' work trees unchanged. Every step after it read its own state fresh:
   `43-l1-before.log` at 08:23:03 and G-GEO at 08:23:10.
2. **`43-l1-before.log` was written on the live host in the `L` form.** §0.6 gives its command as a bare `R '…'`
   "into `43-l1-before.log`", and §3's table puts that log among the live host's. So the command ran inside
   `cd /root/tz53-work && { date -u …; …; } >> /root/tz53-work/logs/43-l1-before.log 2>&1`. The command itself is
   §0.6's, unchanged.
3. **The Boss was told to press «Стоп» twice, where §3 step 10 says once.** §3 step 10's line, «Запускаю бота. Когда
   он напишет в Telegram «проверка кнопки «Стоп»», нажмите «Стоп» — у вас 30 минут», was given before B-DEPLOY's
   start. At 08:35:43, when G-READY passed and the prove began, the Executor repeated in the session: «Когда бот
   напишет «проверка кнопки «Стоп»», нажмите «Стоп» в Telegram.» That reminder came after the top-up ask, and before
   the bot's own message. He pressed 7.1 s after the bot asked.
4. **The engine's self-tests leave `/tmp/l1-bot-selftest/` on the live host, empty.** TZ-53 §2 item 2 and §3 step 9
   say both self-tests remove it. Each removes its own tree (`remove_tree(tmp)`, `selftest-…` and `sdk-…`). Neither
   removes the parent, which `os.makedirs(TEST_ROOT, …)` makes: it read `0700`, root's, empty, after
   `58-engine-sdk-selftest`. No step of this TZ removes it, so it stands. The unit runs with `PrivateTmp=yes` and
   never sees it.
5. **Three of the unit's files are `0644`, not `0600`.** TZ-53 §2 item 4 says the unit keeps its journal and stores
   on the host `0600`. Read by mode and size alone at 08:53:
   - `journal/2026-11-21.jsonl`, `select/1795219200.json`, `prove-1.json`, `unit-state.json` and the stop record
     are `0600`.
   - `select/1795219200.replies.jsonl.gz` and `polls/2026-11-21.jsonl.gz` are `0644`.
   - `service.log`, which systemd's `StandardOutput=append:` creates, is `0644`.

   Every one of them is under `/var/lib/l1-bot/`, `0700`, root's, so no other user can reach them. They are named
   here; nothing was changed.
6. **§0.1's script for the worktree** ran from a copy of TZ-53's lines 46 to 134 whose first line names
   `/root/tz53-work/wt branch` in place of `/root/tz53-work/stage stage`. That is "§0.1's script with the worktree
   and `branch` as its arguments", and the copy differs in that line alone (`diff` printed before it ran). The stage's
   run used an extract of the same lines, asserted equal to them by `diff` (exit `0`).
7. **The logs' extra lines and names:**
   - `10-number.log` carries `fetch exit=0`.
   - `11-worktree.log` carries `worktree exit=0`, and `exit=0` after §0.1's script.
   - `13-push.log` carries `commit exit=0` and `push exit=0`.
   - The pull request's log is `15-pr50.log`, named for the pull request it reads, as TZ-52 named `15-pr49.log`.
   - `59-deploy-start.log` also carries §3 step 10's last read, `systemctl is-active tz53-deploy.service`:
     `inactive`, `exit=4`.
   - `01-stage.log` holds the script's seven lines, TZ-52's first.
8. **The refs differ from map §1's read of 2026-11-21** (202 lines). This is recorded and not BLOCKING. This run
   read 205 lines at §0.5 and at §3.1:
   - `HEAD` and `main` read `04f0a15`, the Boss's upload, against `9a02905`;
   - `refs/tags/rewardbook-streams-*` read 62 against 59: three more runs of the reward book's archive.
9. **B-RECLAIM-SCRATCH had nothing to do.** `scratch` named all seven directories beside this session's own live,
   each made by a `claude` process still running, and none earlier (`30-scratch.log`). That includes TZ-52's
   `5b734feb-…` and `162a9fb6-…`, whose process `2593738` still runs. Nothing was reclaimed under `/tmp/`.
10. **The unit's first minutes, by counts alone.** `status` printed the journal's counts, and no mode of this run
    prints a journal line. At 08:52:54 they were:
    - 105 orders placed and 104 cancelled;
    - 1 fill, and 1 market held;
    - 2 `cancel-refused`: a cancel by id the venue did not confirm, which the unit reads as a possible fill
      (`Unit.cancel`);
    - 1 `foreign`: an open order of the key the unit did not know at one read, which it cancels
      (`Unit.reconcile`).

    What the fill cost, and what the venue pays, are L1's measurement's to read (TZ-53 §1.10). This run prints no
    price or size of them.
11. **What stays on the live host, L1's deployment:**
    - `/root/l1-env/`;
    - `/etc/l1-bot/`, unchanged;
    - `/root/l1-bot-svc/`, `0700`, its four files `0600`;
    - `/etc/systemd/system/l1-bot.service`, `0644`, and its enablement link;
    - `/var/lib/l1-bot/` with `account.json`, TZ-51's kept copy, `prove-1.json`, `unit-state.json`, `stops/`,
      `journal/`, `select/`, `polls/` and `service.log`;
    - the empty `/tmp/l1-bot-selftest/` (item 4).

    **The unit runs on, as TZ-53 §1.10 intends.** Its stops are §2.4's.
12. **The classifier refused nothing, and no paste was handed to the Boss.** B-DEPLOY's `systemd-run`, the removal
    of TZ-52's copy, B-RECLAIM-LIVE and B-RECLAIM-OWN all ran in the session. The Boss's hands were needed for the
    top-up and for «Стоп» alone.
13. **The session's scratchpad** holds:
    - the two extracts of §0.1's script (item 6);
    - a copy of Appendix A, read by the Executor;
    - this report's generator and its template, which embeds every quoted log whole from its file;
    - B-RECLAIM-LIVE's and B-RECLAIM-OWN's session output, copied verbatim for §2.9.

    Nothing else was written there.
