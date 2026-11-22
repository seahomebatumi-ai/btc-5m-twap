# TZ-55 — the liquidation guard, its second version, replacing the first on the capture host — REPORT

**Status: G-DEPLOY PASS. `B-DEPLOY END exit=0` at 10:16:40 UTC on 2026-11-22. The second version of
`liq-guard.service` is installed, enabled and running on the capture host since 10:01:40 UTC (systemd's
`ActiveEnterTimestamp`), MainPID `2825760`, `NRestarts` `0`. Before it started, its own code proved every request path
it uses: G-PROVE PASS, eleven gates of eleven. The Boss confirmed in his chat that the guard sees his positions as
Binance shows them («да» after 166 s), answered «да» to the two examples' colours and look (after 901 s — §6 item 2),
and acknowledged the test alarm in Pushover after 61 s. His positions were unwatched for 1,133.939 s, from the first
version's stop at 09:42:46.915 to the second's restart at 10:01:40.854.**

- **Every gate before B-DEPLOY passed:**
  - READY `ready=1`.
  - §0.1's script staged four files `created`, then wrote the branch's one `created` and two `replaced the first
    version`, each at §0.1's SHA-256.
  - FINGERPRINT PASS, revision `2026-11-21-e`, 70 of 70 `frozen` rows equal.
  - Host gate H1 to H5. The first version ran, at TZ-54's two hashes, its credentials `0600`, root's.
  - NUMBER PASS 2 of 2. Refs read 216 lines, and `refs/heads/tz-55-liq-guard-v2` was absent before the push.
  - The checker's `SELFTEST PASS: 141 checks, 141 passed; refused by the hook: 5, each a check's own`.
  - The guard's `SELFTEST PASS: 127 checks`.
  - SCRATCH: two earlier session directories reclaimed and gone, three live ones untouched besides this session's.
  - SECRETS: five required credentials and `hc-url` `kept`, `pushover-long` and `pushover-short` each
    `written, 31 bytes`, `exit=0`; the directory `0700` and its files `0600`, root's.
- **B-DEPLOY, every step PASS** (`60-deploy.log`, §2.6):
  - the host; G-FIRST, the first version installed at TZ-54's two hashes; G-MEM at the first read, `242,495,488`
    bytes against `100,663,296`; G-STAGE, four `OK` reads;
  - **G-PROVE PASS: 11 gates of 11**: G-CRED (9 credentials, the dead-man set, side applications 2), G-TIME (`26` ms),
    G-KEY (`enableReading True`, `ipRestrict True`, every other permission `False`), G-POS (one open position, with a
    liquidation price and an entry price), G-BRACKET, G-PUSH (the user key and 3 application tokens), G-TG, G-SEE,
    G-LOOK, G-ALARM and G-HC (`the dead-man's ping answered OK`);
  - **G-INSTALL:** both files at §0.1's SHA-256 in `/root/liq-guard-svc/`, the unit file equal by `cmp`, `loaded`,
    `enabled`, `service.log` `0600`;
  - **G-UNIT PASS** at 60 s: `active`, `running`, `NRestarts=0`, `enabled`, `WatchdogUSec=5min`; `key_ok True`,
    `blind False`, `polls_ok 8`; `SERVE start: key True, positions read 1`; `service.log` `600`;
  - **G-LIVE PASS** at 900 s: `active`, `running`, `NRestarts=0`, the same MainPID `2825760`; `key_ok True`,
    `blind False`, `polls_ok 176`, `polls_err 0`, `disk_faults 0`.
- **The unit after** (§3 step 11, `61-unit-after.log`): `active`, `running`, `NRestarts=0`, `enabled`,
  `WatchdogUSec=5min`, `MemoryPeak` `28,340,224` bytes; `/root/liq-guard-svc/liq-guard.py`, its copy of the unit file
  and `/etc/systemd/system/liq-guard.service` at §0.1's SHA-256; `service.log` `-rw-------`; `prove.json`
  `"pass": true` with `code_sha256` `6b851f3f…`.
- **G-PRINT** on every log: `G-PRINT PASS: 17 files, 13 values sought - credentials 9, the host's IPv4 addresses 4;
  found 0`. On this report: given to the Boss in the session before the commit (TZ-55 §3 step 13).
- **Branch** `tz-55-liq-guard-v2` at `7a9593bf1e060ab95d128ae96ca527fcfd02285b`: three paths, `3 2`, `1201 279` and
  `3323 0`. **Pull request #53** is open.
- **The other units of the capture host** were read by §0.3's `systemctl show` alone and were not touched.
- This report prints no credential, no chat id, no address of this host, and no symbol, price, size or margin of
  the Boss's positions.

---

## 0. Fingerprint

`C fingerprint 02-fingerprint` (`logs/02-fingerprint.log`, 09:18:42 UTC) printed §0.2's line, word for word:

```
FINGERPRINT PASS: revision 2026-11-21-e; anchors 6 of 6, 4 re-derived; rows 73: frozen 70 of 70 equal, tracked 2, reported 1; the signing page on main equal to TZ-50's Appendix B
```

**Revision string:** `2026-11-21-e`. **Anchors:**

| anchor | read | how |
|---|---|---|
| `A1` | `229a944f2d51` | the map |
| `A2` | `6c5089330629` | the map; re-derived from `research/twap-divergence.py` |
| `A3` | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` | the map |
| `A4` | `6ac6e10aeabc` | the map; re-derived from `BTC-EXECUTOR-INSTRUCTIONS.md` |
| `A5` | `0f6c90451cbd` | the map; re-derived from `research/recorder/recorder.py` |
| `A6` | `729f0bcdbee3` | the map; re-derived from `research/pfair.py` |

**Every row of the map's §0 table**, as `fingerprint` printed it: 73 rows, 70 `frozen` and each equal, 2 `tracked`,
1 `reported`. `docs/l1-sign.html` on `main` is equal to TZ-50's Appendix B, `11846` bytes, `f1d92e7d…`.

| path | lines | bytes | state | SHA-256 |
|---|---|---|---|---|
| `SYSTEM-MAP.md` | 1104 | 200603 | reported | `463f994b3af8cb7489108fc937f2b01613cc5692e94215712fdb621ab78e3db5` |
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
| `research/tz53-l1-account.py` | 3324 | 188378 | frozen, equal | `e4b72d0e285f1d8736a056012d3c9056f7f103e8e899742e10e488932c910c94` |
| `research/tz54-liq-guard.py` | 3323 | 188349 | frozen, equal | `fd8f8c21d3dc5c36655a6948ce593a03d06ca8f783955ea7d18df5a57ea0e4bf` |
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
| `deploy/systemd/l1-bot.service` | 29 | 1014 | frozen, equal | `a6305d0e7a220ea88f5a4d2be612cac35f3dbe527d7c3b7ed12fd7c47f956266` |
| `engine/l1-bot.py` | 3656 | 188968 | frozen, equal | `98851b3c0df447ed7c846edfbf18b9ea1611d12228a4d9a3c1fda3b4f22da214` |
| `deploy/systemd/liq-guard.service` | 29 | 1055 | frozen, equal | `26f609134730e4b9080bcdddbf2365ba35b1f69ddc1633d538a250bd46bce920` |
| `guard/liq-guard.py` | 1850 | 93840 | frozen, equal | `782efaa88e268bd6ace42e23dc192e279ae130bb7bdc23d2f4de4d628c4da66f` |
| `advisor/RULE-ADV-3.txt` | 33 | 3203 | frozen, equal | `ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169` |
| `advisor/adv3.py` | 895 | 51834 | frozen, equal | `81ef0112d3fe4b86566e51a51aab924d9776ff37a927e65982ecb0bb7c1f34e1` |
| `advisor/adv3-bot.py` | 2548 | 157438 | frozen, equal | `c3d9fff54f3585cfc4c33b5f7e1f93b390e62b03e0b4725fee2d6fdda6d04c11` |
| `advisor/selftest-adv3.py` | 256 | 19111 | frozen, equal | `6f29b82f2b2ca82cd2ff4bbb370e032354dbb4743497330530777429b3af7398` |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` |

**The model:** TZ-55's header names Claude Opus 5.5. The session's own record, read during the run, names
`claude-opus-5-5` as configured and as last served.

---

## 1. Input

Nothing was re-collected: this TZ measures no dataset. What it read:

- **The repository at `main` `037bca1`**, the Boss's upload of `CryptoTZ/TZ-55-liq-guard-v2.md` on map revision
  `2026-11-21-e` (`af529f1`, after pull request #52's merge `c7c1b5b`):
  - TZ-55, by §0.1's script; `research/tz54-liq-guard.py` by `git show origin/main:`, at `fd8f8c21…`, the base;
  - the map's 73 rows' files and `docs/l1-sign.html`, by `fingerprint`;
  - `CryptoTZ/` and `CryptoReports/`, by `number`; `origin`'s refs, by `refs`.
- **The staged files**, §0.1's script into `/root/tz55-work/stage/`, each `created` at §0.1's table's SHA-256
  (`01-stage.log`, §2.2).
- **The Boss's two side tokens**, typed by him at the host's terminal into `/etc/liq-guard/` (`30-secrets.log`); his
  other credentials and the pinned chat were kept from TZ-54. They are read by the guard's modes alone.
- **Binance, with the Boss's key, GET reads alone**, by `prove` and the unit: `/fapi/v1/time`,
  `/fapi/v3/positionRisk` (v3 served; v2 not needed), `/fapi/v1/leverageBracket` and
  `/sapi/v1/account/apiRestrictions`. The prove's record counts `fapi.binance.com` `3` and `api.binance.com` `1`.
- **Pushover**, `api.pushover.net`, `12` requests at the prove; **Telegram**, the guard's own bot, `53` at the prove;
  **`hc-ping.com`**, `17` at the prove — the dead-man kept quiet through the waits and pinged last.
- **This report prints of those reads:** counts, booleans, states and instants. No symbol, price, size or margin of
  a position, no credential and no chat id (TZ-55 §2 item 6).

---

## 2. Measurements

Every log below is quoted from `/root/tz55-work/logs/` as it stood before B-RECLAIM-OWN copied it to the forensic
store (§3): whole, except `20-checker-selftest.log` (its last lines) and `02-fingerprint.log` (tabled in §0). Its
SHA-256 is in §2.10, and B-RECLAIM-OWN's copy of each into `/root/btc-forensics/` carries the same (§3).

### 2.1 The readiness and the host gate — `00-ready.log` and `03-host-gate.log`, whole

The readiness was first read in the session, read-only, before `/root/tz55-work` existed:
`ready=1: 10332565504 bytes free on /var/lib, 7450000000 needed; MemAvailable 218279936, 100663296 needed; at 1795339106 2026-11-22T09:18:26Z`.
Then `mkdir /root/tz55-work /root/tz55-work/logs; echo "exit=$?"` printed `exit=0`, and the readiness read again
into the log:

```
ready=1: 10323038208 bytes free on /var/lib, 7450000000 needed; MemAvailable 230432768, 100663296 needed; at 1795339110 2026-11-22T09:18:30Z
```

```
Sun Nov 22 09:18:48 AM UTC 2026
2026-08-02 07:24:32
1
MemTotal:         978640 kB
MemAvailable:     221496 kB
SwapTotal:       3174396 kB
SwapFree:        2490580 kB
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10331590656
/var/lib/btc-recorder/btc-updown-5m/1794396600/manifest.json
4
3.12.3
MainPID=1555954
NRestarts=0
Id=btc-recorder.service
LoadState=loaded
ActiveState=active
SubState=running
UnitFileState=enabled

MainPID=1556307
NRestarts=0
Id=btc-rewardbook.service
LoadState=loaded
ActiveState=active
SubState=running
UnitFileState=enabled

Id=btc-rewardbook-archive.timer
LoadState=loaded
ActiveState=active
SubState=waiting
UnitFileState=enabled

MainPID=1555970
NRestarts=0
Id=adv3-bot.service
LoadState=loaded
ActiveState=active
SubState=running
UnitFileState=enabled

MainPID=2738430
NRestarts=0
Id=liq-guard.service
LoadState=loaded
ActiveState=active
SubState=running
UnitFileState=enabled
782efaa88e268bd6ace42e23dc192e279ae130bb7bdc23d2f4de4d628c4da66f  /root/liq-guard-svc/liq-guard.py
26f609134730e4b9080bcdddbf2365ba35b1f69ddc1633d538a250bd46bce920  /root/liq-guard-svc/liq-guard.service
26f609134730e4b9080bcdddbf2365ba35b1f69ddc1633d538a250bd46bce920  /etc/systemd/system/liq-guard.service
/etc/liq-guard:
total 44
drwx------   2 root root  4096 Nov 21 20:32 .
drwxr-xr-x 131 root root 12288 Nov 21 18:15 ..
-rw-------   1 root root    65 Nov 21 18:15 binance-key
-rw-------   1 root root    65 Nov 21 18:16 binance-secret
-rw-------   1 root root    57 Nov 21 20:32 hc-url
-rw-------   1 root root    31 Nov 21 18:17 pushover-token
-rw-------   1 root root    31 Nov 21 18:17 pushover-user
-rw-------   1 root root    10 Nov 21 18:27 tg-chat
-rw-------   1 root root    47 Nov 21 18:17 tg-token

/var/lib/liq-guard:
total 24
drwx------  3 root root 4096 Nov 22 09:18 .
drwxr-xr-x 66 root root 4096 Nov 21 18:27 ..
drwx------  2 root root 4096 Nov 22 00:04 journal
-rw-------  1 root root 1420 Nov 21 18:30 prove.json
-rw-r--r--  1 root root  102 Nov 21 20:33 service.log
-rw-------  1 root root  473 Nov 22 09:18 state.json
STATUS at 2026-11-22T09:18:43Z; started 2026-11-21T20:33:46Z; last_ok 2026-11-22T09:18:43Z; polls_ok 9180; polls_err 0; positions 1; with_liquidation 1; blind False; key_ok True; key_checked 2026-11-22T08:33:48Z; dead_man True; outbox 0; disk_faults 0; thresholds [4.0, 2.5, 1.5]; pid 2738430
STATUS journal files 2; events in the last two: {'command': 38, 'error': 4, 'heartbeat': 1, 'key': 4, 'pushed': 9, 'start': 2, 'stop': 1, 'test': 9, 'thresholds': 3, 'tick': 88}
global IPv4 addresses: 4
/usr/sbin/ip
/usr/bin/df
/usr/bin/systemd-run
/usr/bin/install
/usr/bin/cmp
/usr/bin/sha256sum
/usr/bin/stat
```

- **H1** — one path. **H2** — `/dev/vda2`, `31612203008`; `grep -c` `4`. **H3** — `3.12.3`.
- **H4** — `liq-guard.service` `loaded`, `enabled`, `active`; the guard `782efaa8…`, both unit files `26f60913…`;
  `/etc/liq-guard` holds the six required names, each `-rw-------`, root's. Recorded, not judged: the other units
  `active`, `NRestarts=0`; `hc-url` present; `status`'s `dead_man True`.
- **H5** — `global IPv4 addresses: 4`, counted, none printed; the seven commands found.

### 2.2 The stage, the number and the refs — `01-stage.log` and `04-number.log`, whole

```
/root/tz55-work/stage/research/tz55-liq-guard-v2.py 3323 188383 1f7e9e8393ec3efda564a2ee0ff8356228f1ab2e435acad5f6f4729a9870bf35 created
/root/tz55-work/stage/guard/liq-guard.py 2772 148628 6b851f3f93578dadcb683d33969b4d235daf2c852dbdce74c66e978946ec840a created
/root/tz55-work/stage/deploy/systemd/liq-guard.service 30 1086 11bff792d802cbf1abe9ee4f496c24517cce0e63a0dbf6aa49f277b7cdc55157 created
/root/tz55-work/stage/b-deploy.sh 147 8633 d4968301541d9c49148081d127be5951741999bf55ceb795b54513602665e814 created
exit=0
```

```
exit=0
2026-11-22T09:18:53.915723245Z
[2026-11-22T09:18:54Z] origin/main 037bca16e68d4df4343ab068bda8ff85850f5c59: 129 paths under CryptoTZ/ and CryptoReports/; of the number TZ-55-: ['CryptoTZ/TZ-55-liq-guard-v2.md'] and []
[2026-11-22T09:18:54Z] NUMBER PASS - 2 of 2
[2026-11-22T09:18:54Z] peak memory of this run: 34222080 bytes
[2026-11-22T09:18:54Z] refused by the hook: 0; lookups 0, requests 0
exit=0
2026-11-22T09:18:54.141602878Z
[2026-11-22T09:18:54Z] REF 037bca16e68d4df4343ab068bda8ff85850f5c59	HEAD
[2026-11-22T09:18:54Z] REF 037bca16e68d4df4343ab068bda8ff85850f5c59	refs/heads/main
[2026-11-22T09:18:54Z] REFS HEAD                                     1
[2026-11-22T09:18:54Z] REFS refs/heads/main                          1
[2026-11-22T09:18:54Z] REFS refs/heads/tz-*                          28
[2026-11-22T09:18:54Z] REFS refs/pull/*/head                         51
[2026-11-22T09:18:54Z] REFS refs/tags/pairbook-streams-*             59
[2026-11-22T09:18:54Z] REFS refs/tags/rewardbook-streams-*           70
[2026-11-22T09:18:54Z] REFS refs/tags/tz-01a-dataset                 1
[2026-11-22T09:18:54Z] REFS refs/tags/tz-01a-dataset^{}              1
[2026-11-22T09:18:54Z] REFS refs/tags/tz-27-pairbook-streams         1
[2026-11-22T09:18:54Z] REFS refs/tags/tz-27-pairbook-streams^{}      1
[2026-11-22T09:18:54Z] REFS refs/tags/tz-44-l0-inputs                1
[2026-11-22T09:18:54Z] REFS refs/tags/tz-45-l0-rule-w-inputs         1
[2026-11-22T09:18:54Z] REFS 216 lines; refs/heads/tz-55-liq-guard-v2 absent
[2026-11-22T09:18:54Z] peak memory of this run: 34631680 bytes
[2026-11-22T09:18:54Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

### 2.3 The branch — `10-worktree.log`, `11-push.log` and `12-pr.log`, whole

```
Preparing worktree (new branch 'tz-55-liq-guard-v2')
branch 'tz-55-liq-guard-v2' set up to track 'origin/main'.
HEAD is now at 037bca1 Add files via upload
exit=0
/root/tz55-work/wt/research/tz55-liq-guard-v2.py 3323 188383 1f7e9e8393ec3efda564a2ee0ff8356228f1ab2e435acad5f6f4729a9870bf35 created
/root/tz55-work/wt/guard/liq-guard.py 2772 148628 6b851f3f93578dadcb683d33969b4d235daf2c852dbdce74c66e978946ec840a replaced the first version
/root/tz55-work/wt/deploy/systemd/liq-guard.service 30 1086 11bff792d802cbf1abe9ee4f496c24517cce0e63a0dbf6aa49f277b7cdc55157 replaced the first version
exit=0
```

```
M  deploy/systemd/liq-guard.service
M  guard/liq-guard.py
A  research/tz55-liq-guard-v2.py
commit exit=0
remote: 
remote: Create a pull request for 'tz-55-liq-guard-v2' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-55-liq-guard-v2        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-55-liq-guard-v2 -> tz-55-liq-guard-v2
branch 'tz-55-liq-guard-v2' set up to track 'origin/tz-55-liq-guard-v2'.
push exit=0
7a9593bf1e060ab95d128ae96ca527fcfd02285b	refs/heads/tz-55-liq-guard-v2
7a9593bf1e060ab95d128ae96ca527fcfd02285b
3	2	deploy/systemd/liq-guard.service
1201	279	guard/liq-guard.py
3323	0	research/tz55-liq-guard-v2.py
exit=0
```

```
https://github.com/seahomebatumi-ai/btc-5m-twap/pull/53
exit=0
```

The hash on `origin` equals the worktree's `HEAD`, and the numstat is exactly `3 2 deploy/systemd/liq-guard.service`,
`1201 279 guard/liq-guard.py` and `3323 0 research/tz55-liq-guard-v2.py`.

### 2.4 The self-tests — `20-checker-selftest.log`'s last lines and `21-guard-selftest.log`, whole

```
[2026-11-22T09:19:23Z] MemAvailable read 1: 2 bytes, floor 1
[2026-11-22T09:19:23Z] available on /: 5 bytes, floor 6
[2026-11-22T09:19:23Z] ok   the floors: a disk under its floor BLOCKS
[2026-11-22T09:19:23Z] ok   the temporary tree removed
[2026-11-22T09:19:23Z] SELFTEST PASS: 141 checks, 141 passed; refused by the hook: 5, each a check's own
[2026-11-22T09:19:23Z] peak memory of this run: 35676160 bytes
[2026-11-22T09:19:23Z] refused by the hook: 5; lookups 0, requests 18
exit=0
```

```
2026-11-22T09:19:23.206470196Z
FIND-CHAT updates 1, private chats that sent /start: 1, pinned
G-CRED PASS - 7 credentials of their form, 0600, root's; the dead-man not set; side applications 1
G-TIME PASS - Binance's clock less this host's: 0 ms
G-KEY PASS - enableFixApiTrade False, enableFixReadOnly True, enableFutures False, enableInternalTransfer False, enableMargin False, enablePortfolioMarginTrading False, enableReading True, enableSpotAndMarginTrading False, enableVanillaOptions False, enableWithdrawals False, ipRestrict True, permitsUniversalTransfer False
G-POS PASS - /fapi/v3/positionRisk served; open positions 2, with a liquidation price 1, with an entry price 2
G-BRACKET PASS - leverage brackets of one held symbol: 2
G-PUSH PASS - the user key and 2 application tokens validated
G-TG PASS - getMe and one message to the pinned chat
G-SEE PASS - the Boss answered yes to the list of 2 positions after 0 s
G-LOOK PASS - two examples through 1 side applications; the Boss answered yes after 0 s
G-ALARM PASS - acknowledged after 10 s
G-HC PASS - not set - no ping
PROVE PASS: 11 gates of 11 passed; requests {'api.binance.com': 1, 'api.pushover.net': 6, 'api.telegram.org': 13, 'fapi.binance.com': 3}
G-CRED PASS - 8 credentials of their form, 0600, root's; the dead-man set; side applications 1
G-TIME PASS - Binance's clock less this host's: 0 ms
G-KEY PASS - enableFixApiTrade False, enableFixReadOnly True, enableFutures False, enableInternalTransfer False, enableMargin False, enablePortfolioMarginTrading False, enableReading True, enableSpotAndMarginTrading False, enableVanillaOptions False, enableWithdrawals False, ipRestrict True, permitsUniversalTransfer False
G-POS PASS - /fapi/v3/positionRisk served; open positions 2, with a liquidation price 1, with an entry price 2
G-BRACKET PASS - leverage brackets of one held symbol: 2
G-PUSH PASS - the user key and 2 application tokens validated
G-TG PASS - getMe and one message to the pinned chat
G-SEE PASS - the Boss answered yes to the list of 2 positions after 0 s
G-LOOK PASS - two examples through 1 side applications; the Boss answered yes after 0 s
G-ALARM PASS - acknowledged after 10 s
G-HC PASS - the dead-man's ping answered OK
PROVE PASS: 11 gates of 11 passed; requests {'api.binance.com': 2, 'api.pushover.net': 12, 'api.telegram.org': 24, 'fapi.binance.com': 6, 'hc-ping.com': 2}
G-CRED PASS - 8 credentials of their form, 0600, root's; the dead-man set; side applications 1
G-TIME PASS - Binance's clock less this host's: 0 ms
G-KEY PASS - enableFixApiTrade False, enableFixReadOnly True, enableFutures False, enableInternalTransfer False, enableMargin False, enablePortfolioMarginTrading False, enableReading True, enableSpotAndMarginTrading False, enableVanillaOptions False, enableWithdrawals False, ipRestrict True, permitsUniversalTransfer False
G-POS PASS - /fapi/v3/positionRisk served; open positions 2, with a liquidation price 1, with an entry price 2
G-BRACKET PASS - leverage brackets of one held symbol: 2
G-PUSH PASS - the user key and 2 application tokens validated
G-TG PASS - getMe and one message to the pinned chat
G-SEE FAIL - the Boss answered no
PROVE FAIL: 7 gates of 8 passed; requests {'api.binance.com': 3, 'api.pushover.net': 14, 'api.telegram.org': 29, 'fapi.binance.com': 9, 'hc-ping.com': 3}
G-CRED PASS - 8 credentials of their form, 0600, root's; the dead-man set; side applications 1
G-TIME PASS - Binance's clock less this host's: 0 ms
G-KEY PASS - enableFixApiTrade False, enableFixReadOnly True, enableFutures False, enableInternalTransfer False, enableMargin False, enablePortfolioMarginTrading False, enableReading True, enableSpotAndMarginTrading False, enableVanillaOptions False, enableWithdrawals False, ipRestrict True, permitsUniversalTransfer False
G-POS PASS - /fapi/v3/positionRisk served; open positions 2, with a liquidation price 1, with an entry price 2
G-BRACKET PASS - leverage brackets of one held symbol: 2
G-PUSH PASS - the user key and 2 application tokens validated
G-TG PASS - getMe and one message to the pinned chat
G-SEE PASS - the Boss answered yes to the list of 2 positions after 0 s
G-LOOK FAIL - the Boss answered no
PROVE FAIL: 8 gates of 9 passed; requests {'api.binance.com': 4, 'api.pushover.net': 18, 'api.telegram.org': 38, 'fapi.binance.com': 12, 'hc-ping.com': 4}
G-CRED PASS - 8 credentials of their form, 0600, root's; the dead-man set; side applications 1
G-TIME PASS - Binance's clock less this host's: 0 ms
G-KEY PASS - enableFixApiTrade False, enableFixReadOnly True, enableFutures False, enableInternalTransfer False, enableMargin False, enablePortfolioMarginTrading False, enableReading True, enableSpotAndMarginTrading False, enableVanillaOptions False, enableWithdrawals False, ipRestrict True, permitsUniversalTransfer False
G-POS PASS - /fapi/v3/positionRisk served; open positions 2, with a liquidation price 1, with an entry price 2
G-BRACKET PASS - leverage brackets of one held symbol: 2
G-PUSH PASS - the user key and 2 application tokens validated
G-TG PASS - getMe and one message to the pinned chat
G-SEE PASS - the Boss answered yes to the list of 2 positions after 0 s
G-LOOK PASS - two examples through 1 side applications; the Boss answered yes after 0 s
G-ALARM PASS - acknowledged after 10 s
G-HC PASS - the dead-man's ping answered OK
PROVE PASS: 11 gates of 11 passed; requests {'api.binance.com': 5, 'api.pushover.net': 24, 'api.telegram.org': 49, 'fapi.binance.com': 15, 'hc-ping.com': 6}
G-CRED PASS - 8 credentials of their form, 0600, root's; the dead-man set; side applications 1
G-TIME PASS - Binance's clock less this host's: 0 ms
G-KEY FAIL - enableFixApiTrade False, enableFixReadOnly True, enableFutures True, enableInternalTransfer False, enableMargin False, enablePortfolioMarginTrading False, enableReading True, enableSpotAndMarginTrading False, enableVanillaOptions False, enableWithdrawals False, ipRestrict True, permitsUniversalTransfer False; refused: enableFutures true
G-POS PASS - /fapi/v3/positionRisk served; open positions 2, with a liquidation price 1, with an entry price 2
G-BRACKET PASS - leverage brackets of one held symbol: 2
G-PUSH PASS - the user key and 2 application tokens validated
G-TG PASS - getMe and one message to the pinned chat
PROVE FAIL: 6 gates of 7 passed; requests {'api.binance.com': 6, 'api.pushover.net': 26, 'api.telegram.org': 51, 'fapi.binance.com': 18, 'hc-ping.com': 6}
SCAN /tmp/liq-guard-selftest-hqvjogq4/clean.log: 60 bytes, nothing found
G-PRINT PASS: 1 files, 9 values sought - credentials 8, the host's IPv4 addresses 1; found 0
SCAN /tmp/liq-guard-selftest-hqvjogq4/clean.log: 60 bytes, nothing found
SCAN /tmp/liq-guard-selftest-hqvjogq4/dirty.log: 69 bytes, host-ipv4-1 1, pushover-token 1, tg-chat 1
G-PRINT FAIL: 2 files, 9 values sought - credentials 8, the host's IPv4 addresses 1; found 3
SELFTEST PASS: 127 checks
exit=0
```

The guard's self-test prints its stand-ins' prove runs and scans, among them its own negative cases
(`G-SEE FAIL - the Boss answered no`, `PROVE FAIL: …`, `G-PRINT FAIL: …` on its `dirty.log`). Its last line is
`SELFTEST PASS: 127 checks`, `exit=0`.

### 2.5 The scratch and the credentials — `22-scratch.log`, `23-reclaim-scratch.log` and `30-secrets.log`, whole

```
2026-11-22T09:19:35.104522700Z
[2026-11-22T09:19:35Z] running 2569924 started 2026-11-20T18:51:37Z claude
[2026-11-22T09:19:35Z] running 2569934 started 2026-11-20T18:51:39Z claude
[2026-11-22T09:19:35Z] running 2569943 started 2026-11-20T18:51:39Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-22T09:19:35Z] running 2569966 started 2026-11-20T18:51:41Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-22T09:19:35Z] running 2820970 started 2026-11-22T09:18:00Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-22T09:19:35Z] 0736470b-13a0-4e8d-931f-5ecf4df19205 born 2026-11-20T18:51:41Z: live, process [2569924, 2569934, 2569943, 2569966]
[2026-11-22T09:19:35Z] 39c2d6bf-14a5-4e2f-9855-405be6197ac5 born 2026-11-21T15:12:26Z: earlier
[2026-11-22T09:19:35Z] 678335ec-9df8-5905-a595-4d556a3ac265 born 2026-11-21T15:12:27Z: earlier
[2026-11-22T09:19:35Z] 6c04aed0-6057-4e03-a1b5-56678f8a595f born 2026-11-22T09:18:01Z: live, process [2820970]
[2026-11-22T09:19:35Z] 6f0f41a7-6da7-5e8a-80e1-a2a85a4a8e5c born 2026-11-20T18:51:42Z: live, process [2569924, 2569934, 2569943, 2569966]
[2026-11-22T09:19:35Z] peak memory of this run: 34762752 bytes
[2026-11-22T09:19:35Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

```
[2026-11-22T09:19:41Z] reclaim: /tmp/claude-0/-root-btc-5m-twap/39c2d6bf-14a5-4e2f-9855-405be6197ac5, an earlier session's directory of 0 files: nothing of it is kept
[2026-11-22T09:19:41Z] RECLAIM PASS: 0 files considered, 0 copied, 0 already held; the forensic store 2815 -> 2815 files
[2026-11-22T09:19:41Z] peak memory of this run: 34889728 bytes
[2026-11-22T09:19:41Z] refused by the hook: 0; lookups 0, requests 0
exit=0
exit=1
[2026-11-22T09:19:41Z] reclaim: /tmp/claude-0/-root-btc-5m-twap/678335ec-9df8-5905-a595-4d556a3ac265, an earlier session's directory of 4 files: nothing of it is kept
[2026-11-22T09:19:41Z] RECLAIM PASS: 0 files considered, 0 copied, 0 already held; the forensic store 2815 -> 2815 files
[2026-11-22T09:19:41Z] peak memory of this run: 34893824 bytes
[2026-11-22T09:19:41Z] refused by the hook: 0; lookups 0, requests 0
exit=0
exit=1
```

```
SECRETS binance-key: kept
SECRETS binance-secret: kept
SECRETS pushover-user: kept
SECRETS pushover-token: kept
SECRETS tg-token: kept
SECRETS hc-url: kept
SECRETS pushover-long: written, 31 bytes
SECRETS pushover-short: written, 31 bytes
exit=0
total 52
drwx------   2 root root  4096 Nov 22 09:42 .
drwxr-xr-x 131 root root 12288 Nov 21 18:15 ..
-rw-------   1 root root    65 Nov 21 18:15 binance-key
-rw-------   1 root root    65 Nov 21 18:16 binance-secret
-rw-------   1 root root    57 Nov 21 20:32 hc-url
-rw-------   1 root root    31 Nov 22 09:41 pushover-long
-rw-------   1 root root    31 Nov 22 09:42 pushover-short
-rw-------   1 root root    31 Nov 21 18:17 pushover-token
-rw-------   1 root root    31 Nov 21 18:17 pushover-user
-rw-------   1 root root    10 Nov 21 18:27 tg-chat
-rw-------   1 root root    47 Nov 21 18:17 tg-token
```

Two directories named `earlier`, each `RECLAIM PASS`, `rm -rf` `exit=0`, `test -e` `exit=1`. Three named `live`
untouched; this session's own directory is not listed by `scratch`. The harness's copies of the earlier sessions' background output went with
their directories (map §6, harness — background output).

### 2.6 B-DEPLOY — `59-deploy-start.log` and `60-deploy.log`, whole

```
Running as unit: tz55-deploy.service; invocation ID: 35d0f4d0ee204422b5199f9215b63333
exit=0
inactive
exit=4
```

```
2026-11-22T09:42:46.422Z B-DEPLOY BEGIN pid 2823834
2026-11-22T09:42:46.550Z B-DEPLOY host: a manifest found; /dev/vda2 31612203008; runtime.jsonl names e3975b5 4 times
liq-guard.py: OK
liq-guard.service: OK
2026-11-22T09:42:46.568Z B-DEPLOY the first version installed: WatchdogUSec=5min MainPID=2738430 Result=success NRestarts=0 ExecMainStatus=0 MemoryCurrent=8200192 MemoryPeak=18354176 ActiveState=active SubState=running UnitFileState=enabled 
2026-11-22T09:42:46.576Z B-DEPLOY MemAvailable read 1: 242495488 bytes, the floor 100663296
liq-guard.py: OK
liq-guard.service: OK
liq-guard.py: OK
liq-guard.service: OK
2026-11-22T09:42:46.915Z B-DEPLOY the first version stopped, exit=0: the positions unwatched until the second starts: WatchdogUSec=5min MainPID=0 Result=success NRestarts=0 ExecMainStatus=0 MemoryCurrent=[not set] MemoryPeak=18354176 ActiveState=inactive SubState=dead UnitFileState=enabled 
2026-11-22T09:42:46.916Z B-DEPLOY G-PROVE: the Boss answers twice in Telegram and acknowledges the test alarm, each within 15 minutes
G-CRED PASS - 9 credentials of their form, 0600, root's; the dead-man set; side applications 2
G-TIME PASS - Binance's clock less this host's: 26 ms
G-KEY PASS - enableFixApiTrade False, enableFixReadOnly False, enableFutures False, enableInternalTransfer False, enableMargin False, enablePortfolioMarginTrading False, enableReading True, enableSpotAndMarginTrading False, enableVanillaOptions False, enableWithdrawals False, ipRestrict True, permitsUniversalTransfer False
G-POS PASS - /fapi/v3/positionRisk served; open positions 1, with a liquidation price 1, with an entry price 1
G-BRACKET PASS - leverage brackets of one held symbol: 10
G-PUSH PASS - the user key and 3 application tokens validated
G-TG PASS - getMe and one message to the pinned chat
G-SEE PASS - the Boss answered yes to the list of 1 positions after 166 s
G-LOOK PASS - two examples through 2 side applications; the Boss answered yes after 901 s
G-ALARM PASS - acknowledged after 61 s
G-HC PASS - the dead-man's ping answered OK
PROVE PASS: 11 gates of 11 passed; requests {'api.binance.com': 1, 'api.pushover.net': 12, 'api.telegram.org': 53, 'fapi.binance.com': 3, 'hc-ping.com': 17}
liq-guard.py: OK
liq-guard.service: OK
-rw-r--r-- 1 root root 1086 Nov 22 10:01 /etc/systemd/system/liq-guard.service
-rw------- 1 root root  124 Nov 22 09:42 /var/lib/liq-guard/service.log

/root/liq-guard-svc:
total 160
drwx------  2 root root   4096 Nov 22 10:01 .
drwx------ 32 root root   4096 Nov 22 09:51 ..
-rw-------  1 root root 148628 Nov 22 10:01 liq-guard.py
-rw-------  1 root root   1086 Nov 22 10:01 liq-guard.service
2026-11-22T10:01:39.812Z B-DEPLOY installed: WatchdogUSec=5min MainPID=0 Result=success NRestarts=0 ExecMainStatus=0 MemoryCurrent=[not set] MemoryPeak=18354176 ActiveState=inactive SubState=dead UnitFileState=enabled 
2026-11-22T10:01:40.854Z B-DEPLOY restarted; read in 60 s
2026-11-22T10:02:40.864Z B-DEPLOY G-UNIT read: WatchdogUSec=5min MainPID=2825760 Result=success NRestarts=0 ExecMainStatus=0 MemoryCurrent=27979776 MemoryPeak=28241920 ActiveState=active SubState=running UnitFileState=enabled 
STATUS at 2026-11-22T10:02:11Z; started 2026-11-22T10:01:40Z; last_ok 2026-11-22T10:02:10Z; polls_ok 8; polls_err 0; positions 1; with_liquidation 1; watched 0; engaged 0; alarms_open 0; side_apps 2; blind False; key_ok True; key_checked 2026-11-22T10:01:40Z; dead_man True; outbox 0; disk_faults 0; thresholds [4.0, 2.5, 1.5]; target 5.0; profit_from 7.0; pid 2825760
STATUS journal files 2; events in the last two: {'command': 38, 'error': 4, 'heartbeat': 1, 'key': 5, 'pushed': 9, 'start': 3, 'stop': 2, 'test': 9, 'thresholds': 3, 'tick': 90}
2026-11-22T10:02:41.059Z B-DEPLOY G-UNIT PASS
2026-11-22T10:02:41.073Z B-DEPLOY G-LIVE read in 839 s
2026-11-22T10:16:40.105Z B-DEPLOY G-LIVE read: WatchdogUSec=5min MainPID=2825760 Result=success NRestarts=0 ExecMainStatus=0 MemoryCurrent=6647808 MemoryPeak=28340224 ActiveState=active SubState=running UnitFileState=enabled 
STATUS at 2026-11-22T10:16:11Z; started 2026-11-22T10:01:40Z; last_ok 2026-11-22T10:16:10Z; polls_ok 176; polls_err 0; positions 1; with_liquidation 1; watched 0; engaged 0; alarms_open 0; side_apps 2; blind False; key_ok True; key_checked 2026-11-22T10:01:40Z; dead_man True; outbox 0; disk_faults 0; thresholds [4.0, 2.5, 1.5]; target 5.0; profit_from 7.0; pid 2825760
STATUS journal files 2; events in the last two: {'command': 38, 'error': 4, 'heartbeat': 1, 'key': 5, 'pushed': 9, 'start': 3, 'stop': 2, 'test': 9, 'thresholds': 3, 'tick': 91}
2026-11-22T10:16:40.331Z B-DEPLOY G-LIVE PASS
2026-11-22T10:16:40.332Z B-DEPLOY END exit=0
```

`MemAvailable` at each read of this run: `218,279,936` (the session's first readiness read, 09:18:26), `230,432,768`
(`00-ready.log`, 09:18:30), `226,811,904` (`03-host-gate.log`, `221496 kB`, 09:18:48), `242,495,488` (B-DEPLOY's read
1, 09:42:46). Every read is above the floor `100,663,296`.

### 2.7 The unit after — `61-unit-after.log`, whole, with `prove.json` whole

```
2026-11-22T10:16:51.337839481Z
WatchdogUSec=5min
MainPID=2825760
NRestarts=0
MemoryCurrent=6660096
MemoryPeak=28340224
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Sun 2026-11-22 10:01:40 UTC
6b851f3f93578dadcb683d33969b4d235daf2c852dbdce74c66e978946ec840a  /root/liq-guard-svc/liq-guard.py
11bff792d802cbf1abe9ee4f496c24517cce0e63a0dbf6aa49f277b7cdc55157  /root/liq-guard-svc/liq-guard.service
11bff792d802cbf1abe9ee4f496c24517cce0e63a0dbf6aa49f277b7cdc55157  /etc/systemd/system/liq-guard.service
/etc/liq-guard:
total 52
drwx------   2 root root  4096 Nov 22 09:42 .
drwxr-xr-x 131 root root 12288 Nov 21 18:15 ..
-rw-------   1 root root    65 Nov 21 18:15 binance-key
-rw-------   1 root root    65 Nov 21 18:16 binance-secret
-rw-------   1 root root    57 Nov 21 20:32 hc-url
-rw-------   1 root root    31 Nov 22 09:41 pushover-long
-rw-------   1 root root    31 Nov 22 09:42 pushover-short
-rw-------   1 root root    31 Nov 21 18:17 pushover-token
-rw-------   1 root root    31 Nov 21 18:17 pushover-user
-rw-------   1 root root    10 Nov 21 18:27 tg-chat
-rw-------   1 root root    47 Nov 21 18:17 tg-token

/root/liq-guard-svc:
total 160
drwx------  2 root root   4096 Nov 22 10:01 .
drwx------ 32 root root   4096 Nov 22 09:51 ..
-rw-------  1 root root 148628 Nov 22 10:01 liq-guard.py
-rw-------  1 root root   1086 Nov 22 10:01 liq-guard.service

/var/lib/liq-guard:
total 28
drwx------  3 root root 4096 Nov 22 10:16 .
drwxr-xr-x 66 root root 4096 Nov 21 18:27 ..
drwx------  2 root root 4096 Nov 22 00:04 journal
-rw-------  1 root root  122 Nov 22 10:16 memory.json
-rw-------  1 root root 1633 Nov 22 10:01 prove.json
-rw-------  1 root root  164 Nov 22 10:01 service.log
-rw-------  1 root root  505 Nov 22 10:16 state.json
SERVE start: key True, positions read 1
SERVE stop on SIGTERM
SERVE start: key True, positions read 1
SERVE stop on SIGTERM
SERVE start: key True, positions read 1
STATUS at 2026-11-22T10:16:46Z; started 2026-11-22T10:01:40Z; last_ok 2026-11-22T10:16:45Z; polls_ok 183; polls_err 0; positions 1; with_liquidation 1; watched 0; engaged 0; alarms_open 0; side_apps 2; blind False; key_ok True; key_checked 2026-11-22T10:01:40Z; dead_man True; outbox 0; disk_faults 0; thresholds [4.0, 2.5, 1.5]; target 5.0; profit_from 7.0; pid 2825760
STATUS journal files 2; events in the last two: {'command': 38, 'error': 4, 'heartbeat': 1, 'key': 5, 'pushed': 9, 'start': 3, 'stop': 2, 'test': 9, 'thresholds': 3, 'tick': 91}
{"at": "2026-11-22T10:01:38Z", "code_sha256": "6b851f3f93578dadcb683d33969b4d235daf2c852dbdce74c66e978946ec840a", "gates": [{"detail": "9 credentials of their form, 0600, root's; the dead-man set; side applications 2", "gate": "G-CRED", "pass": true}, {"detail": "Binance's clock less this host's: 26 ms", "gate": "G-TIME", "pass": true}, {"detail": "enableFixApiTrade False, enableFixReadOnly False, enableFutures False, enableInternalTransfer False, enableMargin False, enablePortfolioMarginTrading False, enableReading True, enableSpotAndMarginTrading False, enableVanillaOptions False, enableWithdrawals False, ipRestrict True, permitsUniversalTransfer False", "gate": "G-KEY", "pass": true}, {"detail": "/fapi/v3/positionRisk served; open positions 1, with a liquidation price 1, with an entry price 1", "gate": "G-POS", "pass": true}, {"detail": "leverage brackets of one held symbol: 10", "gate": "G-BRACKET", "pass": true}, {"detail": "the user key and 3 application tokens validated", "gate": "G-PUSH", "pass": true}, {"detail": "getMe and one message to the pinned chat", "gate": "G-TG", "pass": true}, {"detail": "the Boss answered yes to the list of 1 positions after 166 s", "gate": "G-SEE", "pass": true}, {"detail": "two examples through 2 side applications; the Boss answered yes after 901 s", "gate": "G-LOOK", "pass": true}, {"detail": "acknowledged after 61 s", "gate": "G-ALARM", "pass": true}, {"detail": "the dead-man's ping answered OK", "gate": "G-HC", "pass": true}], "pass": true, "requests": {"api.binance.com": 1, "api.pushover.net": 12, "api.telegram.org": 53, "fapi.binance.com": 3, "hc-ping.com": 17}}

exit=0
```

### 2.8 G-PRINT on the logs — `62-print.log`, whole

```
SCAN /root/tz55-work/logs/00-ready.log: 141 bytes, nothing found
SCAN /root/tz55-work/logs/01-stage.log: 522 bytes, nothing found
SCAN /root/tz55-work/logs/02-fingerprint.log: 14091 bytes, nothing found
SCAN /root/tz55-work/logs/03-host-gate.log: 2675 bytes, nothing found
SCAN /root/tz55-work/logs/04-number.log: 1667 bytes, nothing found
SCAN /root/tz55-work/logs/10-worktree.log: 598 bytes, nothing found
SCAN /root/tz55-work/logs/11-push.log: 729 bytes, nothing found
SCAN /root/tz55-work/logs/12-pr.log: 63 bytes, nothing found
SCAN /root/tz55-work/logs/20-checker-selftest.log: 19535 bytes, nothing found
SCAN /root/tz55-work/logs/21-guard-selftest.log: 6893 bytes, nothing found
SCAN /root/tz55-work/logs/22-scratch.log: 1290 bytes, nothing found
SCAN /root/tz55-work/logs/23-reclaim-scratch.log: 868 bytes, nothing found
SCAN /root/tz55-work/logs/30-secrets.log: 853 bytes, nothing found
SCAN /root/tz55-work/logs/59-deploy-start.log: 109 bytes, nothing found
SCAN /root/tz55-work/logs/60-deploy.log: 4660 bytes, nothing found
SCAN /root/tz55-work/logs/61-unit-after.log: 4137 bytes, nothing found
SCAN /root/tz55-work/logs/62-print.log: 1106 bytes, nothing found
G-PRINT PASS: 17 files, 13 values sought - credentials 9, the host's IPv4 addresses 4; found 0
exit=0
```

### 2.9 The Boss's instants, and the unwatched span, as the logs carry them

| what | instant (UTC) | where |
|---|---|---|
| his two side tokens, written | `pushover-long` 09:41, `pushover-short` 09:42 | `30-secrets.log`'s `ls -la`, by minute |
| his «готово» | read by the Executor at 09:42, just before B-DEPLOY's start at 09:42:46.400 (the session's date line, in no log) | `30-secrets.log`; `60-deploy.log`'s `BEGIN` at 09:42:46.422 |
| **the first version stopped** | **09:42:46.915** | `60-deploy.log`, `the first version stopped, exit=0` |
| his «да» to what the guard sees | `166` s after the list was sent | `60-deploy.log`, G-SEE |
| his «да» to the two examples | `901` s after the question was sent | `60-deploy.log`, G-LOOK |
| his acknowledgement | `61` s after the test alarm was sent | `60-deploy.log`, G-ALARM |
| the prove's record | `2026-11-22T10:01:38Z` | `prove.json`'s `at` |
| **the second version restarted** | **10:01:40.854** (`ActiveEnterTimestamp` 10:01:40) | `60-deploy.log`, `restarted; read in 60 s`; `61-unit-after.log` |
| **the span unwatched** | **1,133.939 s** (18 min 53.939 s), 10:01:40.854 − 09:42:46.915 | the two lines above |

### 2.10 The files of this run

| file | lines | bytes | SHA-256 |
|---|---|---|---|
| `first/liq-guard.py` | 1850 | 93840 | `782efaa88e268bd6ace42e23dc192e279ae130bb7bdc23d2f4de4d628c4da66f` |
| `first/liq-guard.service` | 29 | 1055 | `26f609134730e4b9080bcdddbf2365ba35b1f69ddc1633d538a250bd46bce920` |
| `inst/liq-guard.py` | 2772 | 148628 | `6b851f3f93578dadcb683d33969b4d235daf2c852dbdce74c66e978946ec840a` |
| `inst/liq-guard.service` | 30 | 1086 | `11bff792d802cbf1abe9ee4f496c24517cce0e63a0dbf6aa49f277b7cdc55157` |
| `logs/00-ready.log` | 1 | 141 | `518cb6173f4e79480459503d8a397738322aa4db19f6b8bf80ac296fca93eb9e` |
| `logs/01-stage.log` | 5 | 522 | `721483784a5db8a6b429572f1ff3e1e370a47f69a36d1655f1cac79ce6470374` |
| `logs/02-fingerprint.log` | 84 | 14091 | `2dca878a16da71c31af7f16ddd243d62af548b75d348aa97f5207df18dcc20a8` |
| `logs/03-host-gate.log` | 82 | 2675 | `7b81de90052329c37fac3831fa66723b599f4a13517ed3643ae8a680cdedf32a` |
| `logs/04-number.log` | 26 | 1667 | `46a551887c22beebe2fdb83a40630f1015d9f997a93997490fcb39b729b5d487` |
| `logs/10-worktree.log` | 8 | 598 | `5cb42e5b1b5087c4a831ac4ed69dc4d1e3e0e822cb42281b07f55dea6fafc2b6` |
| `logs/11-push.log` | 18 | 729 | `1bf89c339f37eda17cc2334b36dff1a45f9dfc45a6376e7da0992ff04d05cc4d` |
| `logs/12-pr.log` | 2 | 63 | `444a1a4cea87d753980f92bb7d25da7bc5f60cbdbfefa9c009fec3f5bf694e0a` |
| `logs/20-checker-selftest.log` | 206 | 19535 | `3378e076a2ce01a63f05c50f4abdf98b468da77a931e1751a13c88416fb1484d` |
| `logs/21-guard-selftest.log` | 72 | 6893 | `2aee29de412cb5c7888ad04ca9fafcf923d600d336997889c18b7ccc25491ae6` |
| `logs/22-scratch.log` | 14 | 1290 | `acad158d3973c8b35f04a3deafd41935afb86893a14a118300ceda5fd9a4adc7` |
| `logs/23-reclaim-scratch.log` | 12 | 868 | `35a7d883144bb14064375c62e0590d7bf77ceaa6a80bdf310ca25008dba25790` |
| `logs/30-secrets.log` | 21 | 853 | `cedd50d4112d4e83035991469370670e72c8f9e62ca6aba270f22ad581d3e199` |
| `logs/59-deploy-start.log` | 4 | 109 | `ee60ee5f94ecab7fb98ffba4631d59d5ceed89dc39b8281d5b0d9dbb9c5ed71a` |
| `logs/60-deploy.log` | 47 | 4660 | `fc3ca862d6abfee2dc4de5bd5468294173eaea006439be958a46128511707a70` |
| `logs/61-unit-after.log` | 53 | 4137 | `bd025e87629c8874ee51c454c7a67b30c00ef31cc74adf3d53022e8568db69f8` |
| `logs/62-print.log` | 19 | 1274 | `61e8bf1688e3cc9f1391e37d33300560c6e84b42f67ea04dbea0fc0c495082e2` |
| `logs/99-selfcheck.log` | 6 | 127 | `2ded68f8c0411ee8b7e8a69091863221ff8b2d5cc7efa881a9bd5d75df9a0237` |
| `stage/b-deploy.sh` | 147 | 8633 | `d4968301541d9c49148081d127be5951741999bf55ceb795b54513602665e814` |
| `stage/deploy/systemd/liq-guard.service` | 30 | 1086 | `11bff792d802cbf1abe9ee4f496c24517cce0e63a0dbf6aa49f277b7cdc55157` |
| `stage/guard/liq-guard.py` | 2772 | 148628 | `6b851f3f93578dadcb683d33969b4d235daf2c852dbdce74c66e978946ec840a` |
| `stage/research/tz55-liq-guard-v2.py` | 3323 | 188383 | `1f7e9e8393ec3efda564a2ee0ff8356228f1ab2e435acad5f6f4729a9870bf35` |

---

## 3. Publication

- **Branch** `tz-55-liq-guard-v2`, commit `7a9593bf1e060ab95d128ae96ca527fcfd02285b`, on `origin` (`11-push.log`). It
  holds three files at §0.1's SHA-256: `guard/liq-guard.py` and `deploy/systemd/liq-guard.service`, each replacing
  the first version's, and `research/tz55-liq-guard-v2.py`, new. Numstat (myers): `3 2`, `1201 279`, `3323 0`.
- **Pull request #53**, `tz-55-liq-guard-v2` into `main`, opened by `gh pr create` (`12-pr.log`). Merge is the Boss's,
  after the Architect's verdict.
- **No Release, no asset:** no file of this run is held by one (map §7 item 167).
- **`b-deploy.sh`** is staged and never committed. Its SHA-256 is
  `d4968301541d9c49148081d127be5951741999bf55ceb795b54513602665e814`. Its forensic copy is
  `/root/btc-forensics/tz55-work--stage--b-deploy.sh`. B-DEPLOY's own copies are `tz55-work--inst--liq-guard.py`
  and `tz55-work--inst--liq-guard.service` (the second's), and `tz55-work--first--liq-guard.py` and
  `tz55-work--first--liq-guard.service` (the first's, kept beside it).
- **Contract §4.2's self-check** (`99-selfcheck.log`):

```
2026-11-22T10:17:21.109671885Z
0
deploy/systemd/liq-guard.service
guard/liq-guard.py
research/tz55-liq-guard-v2.py
grep exit=1
```

`0`: the implementation commit is not on `main`. The branch differs from `main` by the three implementation files
alone. No `.parquet` or `.zip` is on `main`.

- **§9's B-RECLAIM-OWN**, run from the session; its output went to no file and is quoted here verbatim, every line:

```
[2026-11-22T10:19:35Z] reclaim: /root/tz55-work/wt skipped: no file but its HEAD's, and HEAD 7a9593bf1e060ab95d128ae96ca527fcfd02285b is its upstream's
[2026-11-22T10:19:35Z] R copied 782efaa88e268bd6ace42e23dc192e279ae130bb7bdc23d2f4de4d628c4da66f /root/btc-forensics/tz55-work--first--liq-guard.py
[2026-11-22T10:19:35Z] R copied 26f609134730e4b9080bcdddbf2365ba35b1f69ddc1633d538a250bd46bce920 /root/btc-forensics/tz55-work--first--liq-guard.service
[2026-11-22T10:19:35Z] R copied 6b851f3f93578dadcb683d33969b4d235daf2c852dbdce74c66e978946ec840a /root/btc-forensics/tz55-work--inst--liq-guard.py
[2026-11-22T10:19:35Z] R copied 11bff792d802cbf1abe9ee4f496c24517cce0e63a0dbf6aa49f277b7cdc55157 /root/btc-forensics/tz55-work--inst--liq-guard.service
[2026-11-22T10:19:35Z] R copied 518cb6173f4e79480459503d8a397738322aa4db19f6b8bf80ac296fca93eb9e /root/btc-forensics/tz55-work--logs--00-ready.log
[2026-11-22T10:19:35Z] R copied 721483784a5db8a6b429572f1ff3e1e370a47f69a36d1655f1cac79ce6470374 /root/btc-forensics/tz55-work--logs--01-stage.log
[2026-11-22T10:19:35Z] R copied 2dca878a16da71c31af7f16ddd243d62af548b75d348aa97f5207df18dcc20a8 /root/btc-forensics/tz55-work--logs--02-fingerprint.log
[2026-11-22T10:19:35Z] R copied 7b81de90052329c37fac3831fa66723b599f4a13517ed3643ae8a680cdedf32a /root/btc-forensics/tz55-work--logs--03-host-gate.log
[2026-11-22T10:19:35Z] R copied 46a551887c22beebe2fdb83a40630f1015d9f997a93997490fcb39b729b5d487 /root/btc-forensics/tz55-work--logs--04-number.log
[2026-11-22T10:19:35Z] R copied 5cb42e5b1b5087c4a831ac4ed69dc4d1e3e0e822cb42281b07f55dea6fafc2b6 /root/btc-forensics/tz55-work--logs--10-worktree.log
[2026-11-22T10:19:35Z] R copied 1bf89c339f37eda17cc2334b36dff1a45f9dfc45a6376e7da0992ff04d05cc4d /root/btc-forensics/tz55-work--logs--11-push.log
[2026-11-22T10:19:35Z] R copied 444a1a4cea87d753980f92bb7d25da7bc5f60cbdbfefa9c009fec3f5bf694e0a /root/btc-forensics/tz55-work--logs--12-pr.log
[2026-11-22T10:19:35Z] R copied 3378e076a2ce01a63f05c50f4abdf98b468da77a931e1751a13c88416fb1484d /root/btc-forensics/tz55-work--logs--20-checker-selftest.log
[2026-11-22T10:19:35Z] R copied 2aee29de412cb5c7888ad04ca9fafcf923d600d336997889c18b7ccc25491ae6 /root/btc-forensics/tz55-work--logs--21-guard-selftest.log
[2026-11-22T10:19:35Z] R copied acad158d3973c8b35f04a3deafd41935afb86893a14a118300ceda5fd9a4adc7 /root/btc-forensics/tz55-work--logs--22-scratch.log
[2026-11-22T10:19:35Z] R copied 35a7d883144bb14064375c62e0590d7bf77ceaa6a80bdf310ca25008dba25790 /root/btc-forensics/tz55-work--logs--23-reclaim-scratch.log
[2026-11-22T10:19:35Z] R copied cedd50d4112d4e83035991469370670e72c8f9e62ca6aba270f22ad581d3e199 /root/btc-forensics/tz55-work--logs--30-secrets.log
[2026-11-22T10:19:35Z] R copied ee60ee5f94ecab7fb98ffba4631d59d5ceed89dc39b8281d5b0d9dbb9c5ed71a /root/btc-forensics/tz55-work--logs--59-deploy-start.log
[2026-11-22T10:19:35Z] R copied fc3ca862d6abfee2dc4de5bd5468294173eaea006439be958a46128511707a70 /root/btc-forensics/tz55-work--logs--60-deploy.log
[2026-11-22T10:19:35Z] R copied bd025e87629c8874ee51c454c7a67b30c00ef31cc74adf3d53022e8568db69f8 /root/btc-forensics/tz55-work--logs--61-unit-after.log
[2026-11-22T10:19:35Z] R copied 61e8bf1688e3cc9f1391e37d33300560c6e84b42f67ea04dbea0fc0c495082e2 /root/btc-forensics/tz55-work--logs--62-print.log
[2026-11-22T10:19:35Z] R copied 2ded68f8c0411ee8b7e8a69091863221ff8b2d5cc7efa881a9bd5d75df9a0237 /root/btc-forensics/tz55-work--logs--99-selfcheck.log
[2026-11-22T10:19:35Z] R copied d4968301541d9c49148081d127be5951741999bf55ceb795b54513602665e814 /root/btc-forensics/tz55-work--stage--b-deploy.sh
[2026-11-22T10:19:35Z] R copied 11bff792d802cbf1abe9ee4f496c24517cce0e63a0dbf6aa49f277b7cdc55157 /root/btc-forensics/tz55-work--stage--deploy--systemd--liq-guard.service
[2026-11-22T10:19:35Z] R copied 6b851f3f93578dadcb683d33969b4d235daf2c852dbdce74c66e978946ec840a /root/btc-forensics/tz55-work--stage--guard--liq-guard.py
[2026-11-22T10:19:35Z] R copied 1f7e9e8393ec3efda564a2ee0ff8356228f1ab2e435acad5f6f4729a9870bf35 /root/btc-forensics/tz55-work--stage--research--tz55-liq-guard-v2.py
[2026-11-22T10:19:35Z] RECLAIM PASS: 26 files considered, 26 copied, 0 already held; the forensic store 2815 -> 2841 files
[2026-11-22T10:19:35Z] peak memory of this run: 35155968 bytes
[2026-11-22T10:19:35Z] refused by the hook: 0; lookups 0, requests 0
reclaim exit=0
exit=0
exit=0
exit=1
/root/btc-5m-twap       037bca1 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
2841
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10249031680
```

`RECLAIM PASS` before the removals: 26 files copied, each hash verified; the worktree removed `exit=0`;
`/root/tz55-work` removed `exit=0` and gone, `exit=1`; two worktrees left, the primary checkout and the recorder's; the
forensic store `2,841` files; `10,249,031,680` bytes free.

---

## 4. Gate

**G-DEPLOY — `B-DEPLOY END exit=0`** (TZ-55 §4). **Read: PASS.**

| gate | as TZ-55 §4 fixes it | read | how | |
|---|---|---|---|---|
| READY | `ready=1` | `ready=1`, twice | by the Executor against the literal | PASS |
| STAGE | four lines `created`, each at its SHA-256 | four, `created` | asserted by §0.1's script | PASS |
| FINGERPRINT | §0.2's line | the line, word for word | asserted by the checker | PASS |
| HOST | H1 to H5 | H1 to H5 | read by eye against §0.3 | PASS |
| NUMBER and REFS | `NUMBER PASS - 2 of 2`; no branch of this TZ on `origin` | `2 of 2`; `absent` | asserted by the checker | PASS |
| BRANCH | one `created`, two `replaced the first version`; the push at `HEAD`; the numstat's three lines | one and two; `7a9593b…` = `7a9593b…`; `3 2`, `1201 279`, `3323 0` | asserted by §0.1's script; the rest read by the Executor | PASS |
| C-SELF | `141` of `141`, the hook's refusals `5` | `141` of `141`, `5` | asserted by the checker | PASS |
| G-SELF | `SELFTEST PASS: 127 checks` | the line | asserted by the guard | PASS |
| SCRATCH | every earlier directory reclaimed and gone; none live touched | 2 earlier, each `RECLAIM PASS`, `exit=0`, `exit=1`; 3 live untouched | asserted by `reclaim`; `test -e` read by the Executor | PASS |
| SECRETS | five required `kept`; `hc-url` kept, written or skipped; each side token written or skipped; `exit=0`; `0700`, `0600`, root's | five `kept`; `hc-url` `kept`; both `written, 31 bytes`; `exit=0`; `drwx------`, nine `-rw-------`, root's | asserted by `secrets`; the modes read by eye | PASS |
| G-FIRST | the first version at TZ-54's two hashes, or the second installed and active | the first, two `OK` | asserted by B-DEPLOY | PASS |
| G-MEM | `MemAvailable` ≥ `100,663,296` at one of five reads | `242,495,488` at read 1 | asserted by B-DEPLOY | PASS |
| G-STAGE | the second's two in `inst` at §0.1's SHA-256, the first's two in `first` at TZ-54's | four `OK` | asserted by B-DEPLOY | PASS |
| G-PROVE | `PROVE PASS: 11 gates of 11 passed`, `"pass": true`, this code's SHA-256, the eleven in order | the line; `"pass": true`; `6b851f3f…`; the order of `PROVE_GATES` | asserted by B-DEPLOY and the guard | PASS |
| G-INSTALL | both files at SHA-256, `cmp` equal, `loaded`, `enabled` | two `OK`; `cmp` silent; `UnitFileState=enabled` | asserted by B-DEPLOY | PASS |
| G-UNIT | 60 s: `active`, `running`, `NRestarts` `0`, `enabled`, `5min`; `key_ok` `True`, `blind` `False`, `polls_ok` ≥ `1`; the start line; `service.log` `600` | all; `polls_ok 8` | asserted by B-DEPLOY | PASS |
| G-LIVE | 900 s: `active`, `NRestarts` `0`, the same `MainPID`; `key_ok` `True`, `blind` `False`, `polls_ok` ≥ `150`, `disk_faults` `0` | `active`, `0`, `2825760` = `2825760`; `True`, `False`, `176`, `0` | asserted by B-DEPLOY | PASS |
| G-DEPLOY | `B-DEPLOY END exit=0` | the line | asserted by B-DEPLOY | PASS |
| G-AFTER | `active`, `NRestarts` `0`; files at §0.1's SHA-256; `service.log` `0600`; `"pass": true` | `active`, `0`; three SHA-256 equal; `-rw-------`; `"pass": true` | read by the Executor against the literal | PASS |
| G-PRINT | `G-PRINT PASS` on every log and on the report | the logs: `17 files … found 0`; the report: see §6 item 1 | asserted by `scan` | PASS |

Every reading is a count, a state or an equality, so there is no number to round. **Nothing was tuned to reach a
gate, and no gate was read again after a FAIL:** no B-RESET and no second B-DEPLOY ran. `systemctl is-active
tz55-deploy.service` read `inactive`, `exit=4` after the END line (`59-deploy-start.log`).

---

## 5. Validation

TZ-55 §7's Validation is the guard's self-test, `127` checks, fixed by the Architect.

| # | check | count | asserted |
|---|---|---|---|
| V1 | the guard's self-test: the margin hint at `8`% and `5`%, the stages over thirteen reads, the key's permissions, `secrets` at a real pseudo-terminal, `find-chat`, `prove`'s eleven gates and its FAILs, the cycle, the work and the last line, the gains, the commands, the record's privacy, the texts, `scan` | `127` | asserted: each an `assert` that ends the run; `SELFTEST PASS: 127 checks`, `exit=0` |
| V2 | the checker's self-test, TZ-54's under this TZ's names | `141` of `141`; refused by the hook `5` | asserted by the checker |
| V3 | `FINGERPRINT PASS`, §0.2's line | 70 of 70 frozen | asserted by the checker |
| V4 | `NUMBER PASS - 2 of 2`; refs 216 lines; the branch absent before the push | 2 of 2 | asserted by the checker |
| V5 | §0.1's script: four `created` into the stage; one `created` and two `replaced the first version` into the worktree | 4; 3 | asserted by the script |
| V6 | the branch: `HEAD` on `origin`; three paths, `3 2`, `1201 279`, `3323 0` | 3 | read by the Executor against the literal (`11-push.log`) |
| V7 | the host gate | H1 to H5 | read by eye against §0.3 |
| V8 | the scratch: 2 earlier reclaimed, 3 live untouched | 2; 3 | asserted by `scratch` and `reclaim`; `test -e` read by the Executor |
| V9 | SECRETS | 5 kept, `hc-url` kept, 2 written | asserted by `secrets`; the modes of the files read by eye |
| V10 | B-DEPLOY: the host, G-FIRST, G-MEM, G-STAGE, G-PROVE, G-INSTALL, G-UNIT, G-LIVE | 8 of 8 | asserted by B-DEPLOY (`fail` on each) |
| V11 | G-PROVE's eleven gates, in `PROVE_GATES`' order | 11 of 11 | asserted by the guard |
| V12 | the unit after: `active`, `NRestarts` `0`, three SHA-256, `service.log` `0600`, `"pass": true` | 5 of 5 | read by the Executor against the literal |
| V13 | G-PRINT on the logs and on the report | 17 files, 0 found; the report, 1 file | asserted by `scan` (exit `4` on any find) |
| V14 | contract §4.2's self-check | `0`; three paths; nothing | read by the Executor |

---

## 6. What could not be implemented as written

1. **G-PRINT on this report cannot be quoted in it.** As TZ-55 §3 step 13 says, `scan` was run on this file after
   B-RECLAIM-OWN and before the commit. Its two lines were given to the Boss in the session, and the commit followed
   only on `G-PRINT PASS`.
2. **G-LOOK's «да» came `901` s after its question, and the gate read PASS.** TZ-55 §1.7 says «да» "within `900` s".
   The guard's `ask` in Appendix A tests `now() - t0 < wait` before each of its long polls of `LONG_POLL_S` `25` s, so
   an answer that arrives during a poll begun before `900` s is accepted, up to about `925` s. The code is the
   Architect's and its gate is the assert; the Executor changed nothing and reads G-PROVE as the code printed it. The
   departure from §1.7's words is named here for the Architect.
3. **§0.1's script was run from an extract of TZ-55's lines 64 to 143**, by `bash -c "$(sed -n 64,143p …)"`. For the
   branch, the extract's first line was rewritten by `sed` to `/root/tz55-work/wt branch` in place of
   `/root/tz55-work/stage stage`: "§0.1's script verbatim but for its arguments". Before the stage's run, the
   Executor wrote that extract once to `/tmp/x` while checking its first and last lines. It ran nothing from it and
   removed it at once, then ran the extract from the TZ file.
4. **The scratch reclaim chained `rm -rf` after `reclaim` with `&&`.** §3 step 8 gives three separate lines a
   directory and `&&` only for the paste. Each directory was therefore removed only after its own `RECLAIM PASS`.
   The classifier refused nothing, and no paste was needed.
5. **The asks were repeated in the session, each once, as each came due.** §3 step 10's line was given once, before
   the `systemd-run`. When B-DEPLOY's G-BRACKET PASS showed G-SEE waiting, the Executor said in the session that G-SEE
   was open; at G-SEE's PASS it repeated the G-LOOK ask; at G-LOOK's PASS, the «Подтвердить» ask.
6. **The logs' extra lines:**
   - `04-number.log` carries the fetch's `exit=0`;
   - `10-worktree.log` carries `exit=0` after the `worktree add` and after §0.1's script;
   - `11-push.log` carries `git status --short`'s three lines, `commit exit=0`, `push exit=0` and a last `exit=0`;
   - `12-pr.log` carries `exit=0`;
   - `30-secrets.log` carries `ls -la /etc/liq-guard` after the Boss's lines, with no date line;
   - `59-deploy-start.log` also carries the read after the END line, `systemctl is-active tz55-deploy.service`:
     `inactive`, `exit=4`;
   - `61-unit-after.log` carries a date line first, and an empty line and `exit=0` after `prove.json`;
   - `99-selfcheck.log` is contract §4.2's self-check, a log §3's table does not name. It was written after
     `62-print.log`'s scan, so it is not among that scan's 17 files. Its lines are quoted whole in §3, and the
     report's own scan reads them there.
7. **The refs differ from map §1's read** (recorded, not BLOCKING). `refs` read 216 lines: `HEAD` and `main` at
   `037bca1`, the Boss's upload, and `refs/tags/rewardbook-streams-*` at 70, the reward book's archive's later runs.
8. **The classifier refused nothing, and no block was handed to the Boss to run but step 9's.** B-RECLAIM-SCRATCH,
   B-DEPLOY's `systemd-run` and B-RECLAIM-OWN all ran in the session. The Boss's hands were needed for his two side
   tokens (step 9's line, pasted by him at about 09:41 to 09:42), his two «да» and his acknowledgement alone. No
   B-RESET and no second B-DEPLOY ran.
9. **`service.log` is now `0600`.** TZ-54's report named it `0644` (its §6 item 10). B-DEPLOY set it `0600` before
   the restart, and the unit's `UMask=0077` keeps every file it makes so: `memory.json`, new, `-rw-------`.
10. **What stays on the capture host, the guard's deployment:**
    - `/root/liq-guard-svc/`, `0700`, its two files `0600`, the second version's;
    - `/etc/liq-guard/`, `0700`, its nine files `0600`, root's — `pushover-long` and `pushover-short` new;
    - `/var/lib/liq-guard/`, `0700`, with `prove.json` (replaced), `memory.json` (new), `state.json`, `journal/` and
      `service.log`, each `0600`;
    - `/etc/systemd/system/liq-guard.service`, `0644`, the second version's, and its enablement link.

    **The unit runs on**, as TZ-55 §1.9 intends. Its stop is `systemctl disable --now liq-guard.service`.
