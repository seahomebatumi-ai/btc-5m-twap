# TZ-54 — the liquidation guard: the Boss's Binance Futures positions watched for liquidation from the capture host — REPORT

**Status: G-DEPLOY PASS. `B-DEPLOY END exit=0` at 18:45:43 UTC on 2026-11-21. The guard's unit, `liq-guard.service`,
is installed, enabled and running on the capture host since 18:30:43 UTC (systemd's `ActiveEnterTimestamp`), MainPID `2726013`, `NRestarts` `0`.
Before it started, its own code proved every request path it uses: G-PROVE PASS, ten gates of ten. The key reads
`enableReading True`, `ipRestrict True` and every other permission `False`. The Boss confirmed in his chat that the
guard sees his positions as Binance shows them («да» after 76 s), and he acknowledged the test alarm in Pushover
after 92 s.**

- **Every gate before B-DEPLOY passed:**
  - READY `ready=1`, twice.
  - §0.1's script staged four files `created`, then wrote the branch's three `created`, each at §0.1's SHA-256.
  - FINGERPRINT PASS, revision `2026-11-21-d`, 67 of 67 `frozen` rows equal.
  - Host gate H1 to H5. `liq-guard.service` read `not-found`, and its four paths were absent.
  - NUMBER PASS 2 of 2. Refs read 208 lines, and `refs/heads/tz-54-liq-guard` was absent before the push.
  - The checker's `SELFTEST PASS: 141 checks, 141 passed; refused by the hook: 5, each a check's own`.
  - The guard's `SELFTEST PASS: 83 checks`.
  - SCRATCH: six earlier session directories reclaimed and gone, three live ones untouched.
  - SECRETS: five credentials written, `hc-url` skipped, `exit=0`, the directory `0700` and its files `0600`, root's.
  - CHAT: `FIND-CHAT updates 1, private chats that sent /start: 1, pinned`, `exit=0`.
- **B-DEPLOY, every step PASS** (`60-deploy.log`, §2.6):
  - the host; G-MEM at the first read, `246,251,520` bytes against `100,663,296`;
  - **G-INSTALL:** both files at §0.1's SHA-256 in `/root/liq-guard-svc/`, the unit file equal by `cmp`,
    `loaded`, `disabled`;
  - **G-PROVE PASS: 10 gates of 10**: G-CRED, G-TIME (`26` ms), G-KEY, G-POS (one open position, with a
    liquidation price), G-BRACKET, G-PUSH, G-TG, G-SEE, G-ALARM and G-HC (`not set - no ping`);
  - **G-UNIT PASS** at 60 s: `active`, `running`, `NRestarts=0`, `enabled`, `WatchdogUSec=5min`; `key_ok True`,
    `blind False`, `polls_ok 8`; `SERVE start: key True, positions read 1`;
  - **G-LIVE PASS** at 900 s: `active`, `running`, `NRestarts=0`, the same MainPID `2726013`; `key_ok True`, `blind False`, `polls_ok 179`, `polls_err 0`, `disk_faults 0`.
- **The unit after** (§3 step 12, `61-unit-after.log`): `active`, `running`, `NRestarts=0`, `enabled`, `WatchdogUSec=5min`, `MemoryPeak` `21,970,944` bytes; `/root/liq-guard-svc/liq-guard.py`, its copy of the unit file and `/etc/systemd/system/liq-guard.service` at §0.1's SHA-256; `prove.json` `"pass": true` with `code_sha256` `782efaa8…`.
- **G-PRINT** on every log: `G-PRINT PASS: 18 files, 10 values sought - credentials 6, the host's IPv4 addresses 4; found 0`. On this report: given to the Boss in the session before the commit
  (TZ-54 §3 step 14).
- **Branch** `tz-54-liq-guard` at `8a98166a486abf0be0abdcbed2c6065eb04d9808`: three paths, `29 0`, `1850 0` and
  `3323 0`. **Pull request #52** is open.
- **The other units of the capture host** were read by §0.3's `systemctl show` alone and were not touched.
- **The dead-man is not set:** the Boss gave no healthchecks.io address. G-HC reads `not set - no ping`, and
  nothing outside the host watches the guard.
- This report prints no credential, no chat id, no address of this host, and no symbol, price, size or margin of
  the Boss's positions.

---

## 0. Fingerprint

`C fingerprint 02-fingerprint` (`logs/02-fingerprint.log`, 15:13:17 UTC) printed §0.2's line, word for word:

```
FINGERPRINT PASS: revision 2026-11-21-d; anchors 6 of 6, 4 re-derived; rows 70: frozen 67 of 67 equal, tracked 2, reported 1; the signing page on main equal to TZ-50's Appendix B
```

**Revision string:** `2026-11-21-d`. **Anchors:**

| anchor | read | how |
|---|---|---|
| `A1` | `229a944f2d51` | the map |
| `A2` | `6c5089330629` | the map; re-derived from `research/twap-divergence.py` |
| `A3` | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` | the map |
| `A4` | `6ac6e10aeabc` | the map; re-derived from `BTC-EXECUTOR-INSTRUCTIONS.md` |
| `A5` | `0f6c90451cbd` | the map; re-derived from `research/recorder/recorder.py` |
| `A6` | `729f0bcdbee3` | the map; re-derived from `research/pfair.py` |

**Every row of the map's §0 table**, as `fingerprint` printed it: 70 rows, 67 `frozen` and each equal, 2 `tracked`,
1 `reported`. `docs/l1-sign.html` on `main` is equal to TZ-50's Appendix B, `11846` bytes, `f1d92e7d…`.

| path | lines | bytes | state | SHA-256 |
|---|---|---|---|---|
| `SYSTEM-MAP.md` | 1085 | 193239 | reported | `ca1585b360377ac1c11db7311073a76c3688392f487eb8dde1def7964459bb8c` |
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
| `advisor/RULE-ADV-3.txt` | 33 | 3203 | frozen, equal | `ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169` |
| `advisor/adv3.py` | 895 | 51834 | frozen, equal | `81ef0112d3fe4b86566e51a51aab924d9776ff37a927e65982ecb0bb7c1f34e1` |
| `advisor/adv3-bot.py` | 2548 | 157438 | frozen, equal | `c3d9fff54f3585cfc4c33b5f7e1f93b390e62b03e0b4725fee2d6fdda6d04c11` |
| `advisor/selftest-adv3.py` | 256 | 19111 | frozen, equal | `6f29b82f2b2ca82cd2ff4bbb370e032354dbb4743497330530777429b3af7398` |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` |

**The model:** TZ-54's header names Claude Opus 5.5. The session's own record, read during the run, names
`claude-opus-5-5` as configured and as last served.

---

## 1. Input

Nothing was re-collected: this TZ measures no dataset. What it read:

- **The repository at `main` `0b2e935`**, the Boss's upload of `CryptoTZ/TZ-54-liq-guard.md` on map revision
  `2026-11-21-d` (`aeaca24`):
  - TZ-54, by §0.1's script; `research/tz53-l1-account.py` by `git show origin/main:`, at
    `e4b72d0e…`, the base;
  - the map's 70 rows' files and `docs/l1-sign.html`, by `fingerprint`;
  - `CryptoTZ/` and `CryptoReports/`, by `number`; `origin`'s refs, by `refs`.
- **The staged files**, §0.1's script into `/root/tz54-work/stage/`, each `created` at §0.1's table's SHA-256
  (`01-stage.log`, §2.2).
- **The Boss's credentials**, typed by him at the host's terminal into `/etc/liq-guard/` (`30-secrets.log`), and the
  pinned chat by `find-chat` (`31-find-chat.log`). They are read by the guard's modes alone.
- **Binance, with the Boss's key, GET reads alone**, by `prove` and the unit: `/fapi/v1/time`,
  `/fapi/v3/positionRisk` (v3 served; v2 not needed), `/fapi/v1/leverageBracket` and
  `/sapi/v1/account/apiRestrictions`. The prove's record counts `fapi.binance.com` `3` and `api.binance.com` `1`.
- **Pushover**, `api.pushover.net`, `11` requests at the prove; **Telegram**, the guard's own bot, `9` at the prove.
  **`hc-ping.com`: not reached**, the dead-man not set.
- **This report prints of those reads:** counts, booleans, states and instants. No symbol, price, size or margin of
  a position, no credential and no chat id (TZ-54 §2 item 6).

---

## 2. Measurements

Every log below is quoted whole from `/root/tz54-work/logs/`, as it stood before B-RECLAIM-OWN copied it to the
forensic store (§3). Its SHA-256 is in §2.10, and B-RECLAIM-OWN's copy of each into `/root/btc-forensics/` carries the same (§3).

### 2.1 The readiness and the host gate — `00-ready.log` and `03-host-gate.log`, whole

The session's first read, before `/root/tz54-work` existed, printed:

```
ready=1: 10256875520 bytes free on /var/lib, 7450000000 needed; MemAvailable 230653952, 100663296 needed; at 1795273982 2026-11-21T15:13:02Z
```

`00-ready.log`:

```
ready=1: 10256740352 bytes free on /var/lib, 7450000000 needed; MemAvailable 229793792, 100663296 needed; at 1795273985 2026-11-21T15:13:05Z
```

`mkdir /root/tz54-work /root/tz54-work/logs; echo "exit=$?"` printed `exit=0`.

`03-host-gate.log` — the global IPv4 addresses are counted, never printed:

```
Sat Nov 21 03:13:22 PM UTC 2026
2026-08-02 07:24:32
1
MemTotal:         978640 kB
MemAvailable:     215936 kB
SwapTotal:       3174396 kB
SwapFree:        2499592 kB
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10255962112
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

MainPID=0
NRestarts=0
Id=liq-guard.service
LoadState=not-found
ActiveState=inactive
SubState=dead
UnitFileState=
/root/liq-guard-svc exit=1
/var/lib/liq-guard exit=1
/etc/liq-guard exit=1
/etc/systemd/system/liq-guard.service exit=1
global IPv4 addresses: 4
/usr/sbin/ip
/usr/bin/df
/usr/bin/systemd-run
/usr/bin/install
/usr/bin/cmp
/usr/bin/sha256sum
```

- **H1:** one path. **H2:** `/dev/vda2`, `31612203008`; `grep -c` `4`. **H3:** `3.12.3`.
- **H4:** `liq-guard.service` `LoadState=not-found`; the four paths each `exit=1`. The other units' lines are
  recorded, not judged.
- **H5:** `4` global IPv4 addresses; the six commands found.

### 2.2 The stage, the number and the refs — `01-stage.log` and `04-number.log`, whole

```
/root/tz54-work/stage/research/tz54-liq-guard.py 3323 188349 fd8f8c21d3dc5c36655a6948ce593a03d06ca8f783955ea7d18df5a57ea0e4bf created
/root/tz54-work/stage/guard/liq-guard.py 1850 93840 782efaa88e268bd6ace42e23dc192e279ae130bb7bdc23d2f4de4d628c4da66f created
/root/tz54-work/stage/deploy/systemd/liq-guard.service 29 1055 26f609134730e4b9080bcdddbf2365ba35b1f69ddc1633d538a250bd46bce920 created
/root/tz54-work/stage/b-deploy.sh 117 6554 8f59acce92292bf2afda632636e8cd80ca154dfc3d9a48315acb0de19dfba4ad created
exit=0
```

```
2026-11-21T15:13:25.828061423Z
fetch exit=0
2026-11-21T15:13:26.290782902Z
[2026-11-21T15:13:26Z] origin/main 0b2e935b72908d33d2557fcaac91a5a293fe2256: 127 paths under CryptoTZ/ and CryptoReports/; of the number TZ-54-: ['CryptoTZ/TZ-54-liq-guard.md'] and []
[2026-11-21T15:13:26Z] NUMBER PASS - 2 of 2
[2026-11-21T15:13:26Z] peak memory of this run: 34619392 bytes
[2026-11-21T15:13:26Z] refused by the hook: 0; lookups 0, requests 0
exit=0
2026-11-21T15:13:26.427718602Z
[2026-11-21T15:13:26Z] REF 0b2e935b72908d33d2557fcaac91a5a293fe2256	HEAD
[2026-11-21T15:13:26Z] REF 0b2e935b72908d33d2557fcaac91a5a293fe2256	refs/heads/main
[2026-11-21T15:13:26Z] REFS HEAD                                     1
[2026-11-21T15:13:26Z] REFS refs/heads/main                          1
[2026-11-21T15:13:26Z] REFS refs/heads/tz-*                          27
[2026-11-21T15:13:26Z] REFS refs/pull/*/head                         50
[2026-11-21T15:13:26Z] REFS refs/tags/pairbook-streams-*             59
[2026-11-21T15:13:26Z] REFS refs/tags/rewardbook-streams-*           64
[2026-11-21T15:13:26Z] REFS refs/tags/tz-01a-dataset                 1
[2026-11-21T15:13:26Z] REFS refs/tags/tz-01a-dataset^{}              1
[2026-11-21T15:13:26Z] REFS refs/tags/tz-27-pairbook-streams         1
[2026-11-21T15:13:26Z] REFS refs/tags/tz-27-pairbook-streams^{}      1
[2026-11-21T15:13:26Z] REFS refs/tags/tz-44-l0-inputs                1
[2026-11-21T15:13:26Z] REFS refs/tags/tz-45-l0-rule-w-inputs         1
[2026-11-21T15:13:26Z] REFS 208 lines; refs/heads/tz-54-liq-guard absent
[2026-11-21T15:13:26Z] peak memory of this run: 34635776 bytes
[2026-11-21T15:13:26Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

### 2.3 The branch — `10-worktree.log`, `11-push.log` and `12-pr.log`, whole

```
2026-11-21T15:13:29.535332333Z
Preparing worktree (new branch 'tz-54-liq-guard')
branch 'tz-54-liq-guard' set up to track 'origin/main'.
HEAD is now at 0b2e935 Add files via upload
exit=0
/root/tz54-work/wt/research/tz54-liq-guard.py 3323 188349 fd8f8c21d3dc5c36655a6948ce593a03d06ca8f783955ea7d18df5a57ea0e4bf created
/root/tz54-work/wt/guard/liq-guard.py 1850 93840 782efaa88e268bd6ace42e23dc192e279ae130bb7bdc23d2f4de4d628c4da66f created
/root/tz54-work/wt/deploy/systemd/liq-guard.service 29 1055 26f609134730e4b9080bcdddbf2365ba35b1f69ddc1633d538a250bd46bce920 created
exit=0
```

```
2026-11-21T15:13:36.724373525Z
commit exit=0
remote: 
remote: Create a pull request for 'tz-54-liq-guard' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-54-liq-guard        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-54-liq-guard -> tz-54-liq-guard
branch 'tz-54-liq-guard' set up to track 'origin/tz-54-liq-guard'.
push exit=0
8a98166a486abf0be0abdcbed2c6065eb04d9808	refs/heads/tz-54-liq-guard
8a98166a486abf0be0abdcbed2c6065eb04d9808
29	0	deploy/systemd/liq-guard.service
1850	0	guard/liq-guard.py
3323	0	research/tz54-liq-guard.py
```

```
2026-11-21T15:13:45.350175493Z
https://github.com/seahomebatumi-ai/btc-5m-twap/pull/52
exit=0
```

### 2.4 The self-tests — `20-checker-selftest.log`'s last lines and `21-guard-selftest.log`, whole

`20-checker-selftest.log`, 206 lines, each check named `ok`; its last six:

```
[2026-11-21T15:13:50Z] ok   the floors: a disk under its floor BLOCKS
[2026-11-21T15:13:50Z] ok   the temporary tree removed
[2026-11-21T15:13:50Z] SELFTEST PASS: 141 checks, 141 passed; refused by the hook: 5, each a check's own
[2026-11-21T15:13:50Z] peak memory of this run: 35667968 bytes
[2026-11-21T15:13:50Z] refused by the hook: 5; lookups 0, requests 18
exit=0
```

`21-guard-selftest.log` — the self-test's own stand-ins of Binance, Pushover, Telegram and healthchecks.io; no
line of it is a read of the Boss's account:

```
2026-11-21T15:13:51.016082480Z
FIND-CHAT updates 1, private chats that sent /start: 1, pinned
G-CRED PASS - 6 credentials of their form, 0600, root's; the dead-man not set
G-TIME PASS - Binance's clock less this host's: 0 ms
G-KEY PASS - enableFixApiTrade False, enableFixReadOnly True, enableFutures False, enableInternalTransfer False, enableMargin False, enablePortfolioMarginTrading False, enableReading True, enableSpotAndMarginTrading False, enableVanillaOptions False, enableWithdrawals False, ipRestrict True, permitsUniversalTransfer False
G-POS PASS - /fapi/v3/positionRisk served; open positions 2, with a liquidation price 1
G-BRACKET PASS - leverage brackets of one held symbol: 2
G-PUSH PASS - the user key and token validated
G-TG PASS - getMe and one message to the pinned chat
G-SEE PASS - the Boss answered yes to the list of 2 positions after 0 s
G-ALARM PASS - acknowledged after 10 s
G-HC PASS - not set - no ping
PROVE PASS: 10 gates of 10 passed; requests {'api.binance.com': 1, 'api.pushover.net': 3, 'api.telegram.org': 8, 'fapi.binance.com': 3}
G-CRED PASS - 7 credentials of their form, 0600, root's; the dead-man set
G-TIME PASS - Binance's clock less this host's: 0 ms
G-KEY PASS - enableFixApiTrade False, enableFixReadOnly True, enableFutures False, enableInternalTransfer False, enableMargin False, enablePortfolioMarginTrading False, enableReading True, enableSpotAndMarginTrading False, enableVanillaOptions False, enableWithdrawals False, ipRestrict True, permitsUniversalTransfer False
G-POS PASS - /fapi/v3/positionRisk served; open positions 2, with a liquidation price 1
G-BRACKET PASS - leverage brackets of one held symbol: 2
G-PUSH PASS - the user key and token validated
G-TG PASS - getMe and one message to the pinned chat
G-SEE PASS - the Boss answered yes to the list of 2 positions after 0 s
G-ALARM PASS - acknowledged after 10 s
G-HC PASS - the dead-man's ping answered OK
PROVE PASS: 10 gates of 10 passed; requests {'api.binance.com': 2, 'api.pushover.net': 6, 'api.telegram.org': 14, 'fapi.binance.com': 6, 'hc-ping.com': 1}
G-CRED PASS - 7 credentials of their form, 0600, root's; the dead-man set
G-TIME PASS - Binance's clock less this host's: 0 ms
G-KEY PASS - enableFixApiTrade False, enableFixReadOnly True, enableFutures False, enableInternalTransfer False, enableMargin False, enablePortfolioMarginTrading False, enableReading True, enableSpotAndMarginTrading False, enableVanillaOptions False, enableWithdrawals False, ipRestrict True, permitsUniversalTransfer False
G-POS PASS - /fapi/v3/positionRisk served; open positions 2, with a liquidation price 1
G-BRACKET PASS - leverage brackets of one held symbol: 2
G-PUSH PASS - the user key and token validated
G-TG PASS - getMe and one message to the pinned chat
G-SEE FAIL - the Boss answered no
PROVE FAIL: 7 gates of 8 passed; requests {'api.binance.com': 3, 'api.pushover.net': 7, 'api.telegram.org': 19, 'fapi.binance.com': 9, 'hc-ping.com': 1}
G-CRED PASS - 7 credentials of their form, 0600, root's; the dead-man set
G-TIME PASS - Binance's clock less this host's: 0 ms
G-KEY FAIL - enableFixApiTrade False, enableFixReadOnly True, enableFutures True, enableInternalTransfer False, enableMargin False, enablePortfolioMarginTrading False, enableReading True, enableSpotAndMarginTrading False, enableVanillaOptions False, enableWithdrawals False, ipRestrict True, permitsUniversalTransfer False; refused: enableFutures true
G-POS PASS - /fapi/v3/positionRisk served; open positions 2, with a liquidation price 1
G-BRACKET PASS - leverage brackets of one held symbol: 2
G-PUSH PASS - the user key and token validated
G-TG PASS - getMe and one message to the pinned chat
PROVE FAIL: 6 gates of 7 passed; requests {'api.binance.com': 4, 'api.pushover.net': 8, 'api.telegram.org': 21, 'fapi.binance.com': 12, 'hc-ping.com': 1}
SCAN /tmp/liq-guard-selftest-k802lnzu/clean.log: 60 bytes, nothing found
G-PRINT PASS: 1 files, 8 values sought - credentials 7, the host's IPv4 addresses 1; found 0
SCAN /tmp/liq-guard-selftest-k802lnzu/clean.log: 60 bytes, nothing found
SCAN /tmp/liq-guard-selftest-k802lnzu/dirty.log: 69 bytes, host-ipv4-1 1, pushover-token 1, tg-chat 1
G-PRINT FAIL: 2 files, 8 values sought - credentials 7, the host's IPv4 addresses 1; found 3
SELFTEST PASS: 83 checks
exit=0
```

### 2.5 The scratch, the credentials and the chat — `22-scratch.log`, `23-reclaim-scratch.log`, `30-secrets.log` and `31-find-chat.log`, whole

```
2026-11-21T15:13:58.977517721Z
[2026-11-21T15:13:59Z] running 2569924 started 2026-11-20T18:51:37Z claude
[2026-11-21T15:13:59Z] running 2569934 started 2026-11-20T18:51:39Z claude
[2026-11-21T15:13:59Z] running 2569943 started 2026-11-20T18:51:39Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-21T15:13:59Z] running 2569966 started 2026-11-20T18:51:41Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-21T15:13:59Z] running 2706339 started 2026-11-21T15:12:25Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-21T15:13:59Z] 0736470b-13a0-4e8d-931f-5ecf4df19205 born 2026-11-20T18:51:41Z: live, process [2569924, 2569934, 2569943, 2569966]
[2026-11-21T15:13:59Z] 162a9fb6-80c1-5fc2-8efb-0d715f44d283 born 2026-11-20T22:44:39Z: earlier
[2026-11-21T15:13:59Z] 39c2d6bf-14a5-4e2f-9855-405be6197ac5 born 2026-11-21T15:12:26Z: live, process [2706339]
[2026-11-21T15:13:59Z] 450e33c9-580a-5524-ad84-641183f6ef0c born 2026-11-20T18:55:32Z: earlier
[2026-11-21T15:13:59Z] 5b734feb-443a-4557-9e38-5fb2090365b2 born 2026-11-20T22:44:38Z: earlier
[2026-11-21T15:13:59Z] 6f0f41a7-6da7-5e8a-80e1-a2a85a4a8e5c born 2026-11-20T18:51:42Z: live, process [2569924, 2569934, 2569943, 2569966]
[2026-11-21T15:13:59Z] 8791beea-5eca-428f-970f-f69a3637e214 born 2026-11-21T07:37:41Z: earlier
[2026-11-21T15:13:59Z] d5c9cb67-8a6b-551c-9c86-d4bd7a6f3650 born 2026-11-21T07:37:42Z: earlier
[2026-11-21T15:13:59Z] dc25b96c-1173-470f-9a05-e5fdd91952fe born 2026-11-20T18:55:31Z: earlier
[2026-11-21T15:13:59Z] peak memory of this run: 34762752 bytes
[2026-11-21T15:13:59Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

```
2026-11-21T15:14:11.606346442Z
[2026-11-21T15:14:11Z] reclaim: /tmp/claude-0/-root-btc-5m-twap/162a9fb6-80c1-5fc2-8efb-0d715f44d283, an earlier session's directory of 10 files: nothing of it is kept
[2026-11-21T15:14:11Z] RECLAIM PASS: 0 files considered, 0 copied, 0 already held; the forensic store 2790 -> 2790 files
[2026-11-21T15:14:11Z] peak memory of this run: 35024896 bytes
[2026-11-21T15:14:11Z] refused by the hook: 0; lookups 0, requests 0
exit=0
exit=1
[2026-11-21T15:14:11Z] reclaim: /tmp/claude-0/-root-btc-5m-twap/450e33c9-580a-5524-ad84-641183f6ef0c, an earlier session's directory of 10 files: nothing of it is kept
[2026-11-21T15:14:11Z] RECLAIM PASS: 0 files considered, 0 copied, 0 already held; the forensic store 2790 -> 2790 files
[2026-11-21T15:14:11Z] peak memory of this run: 35024896 bytes
[2026-11-21T15:14:11Z] refused by the hook: 0; lookups 0, requests 0
exit=0
exit=1
[2026-11-21T15:14:12Z] reclaim: /tmp/claude-0/-root-btc-5m-twap/5b734feb-443a-4557-9e38-5fb2090365b2, an earlier session's directory of 0 files: nothing of it is kept
[2026-11-21T15:14:12Z] RECLAIM PASS: 0 files considered, 0 copied, 0 already held; the forensic store 2790 -> 2790 files
[2026-11-21T15:14:12Z] peak memory of this run: 35024896 bytes
[2026-11-21T15:14:12Z] refused by the hook: 0; lookups 0, requests 0
exit=0
exit=1
[2026-11-21T15:14:12Z] reclaim: /tmp/claude-0/-root-btc-5m-twap/8791beea-5eca-428f-970f-f69a3637e214, an earlier session's directory of 0 files: nothing of it is kept
[2026-11-21T15:14:12Z] RECLAIM PASS: 0 files considered, 0 copied, 0 already held; the forensic store 2790 -> 2790 files
[2026-11-21T15:14:12Z] peak memory of this run: 34897920 bytes
[2026-11-21T15:14:12Z] refused by the hook: 0; lookups 0, requests 0
exit=0
exit=1
[2026-11-21T15:14:12Z] reclaim: /tmp/claude-0/-root-btc-5m-twap/d5c9cb67-8a6b-551c-9c86-d4bd7a6f3650, an earlier session's directory of 13 files: nothing of it is kept
[2026-11-21T15:14:12Z] RECLAIM PASS: 0 files considered, 0 copied, 0 already held; the forensic store 2790 -> 2790 files
[2026-11-21T15:14:12Z] peak memory of this run: 35008512 bytes
[2026-11-21T15:14:12Z] refused by the hook: 0; lookups 0, requests 0
exit=0
exit=1
[2026-11-21T15:14:12Z] reclaim: /tmp/claude-0/-root-btc-5m-twap/dc25b96c-1173-470f-9a05-e5fdd91952fe, an earlier session's directory of 0 files: nothing of it is kept
[2026-11-21T15:14:12Z] RECLAIM PASS: 0 files considered, 0 copied, 0 already held; the forensic store 2790 -> 2790 files
[2026-11-21T15:14:12Z] peak memory of this run: 35024896 bytes
[2026-11-21T15:14:12Z] refused by the hook: 0; lookups 0, requests 0
exit=0
exit=1
```

`30-secrets.log` — `secrets`' own lines, from the Boss's paste, and then the Executor's `ls -la /etc/liq-guard`:

```
SECRETS binance-key: written, 65 bytes
SECRETS binance-secret: written, 65 bytes
SECRETS pushover-user: written, 31 bytes
SECRETS pushover-token: written, 31 bytes
SECRETS tg-token: written, 47 bytes
SECRETS hc-url: skipped
exit=0
2026-11-21T18:23:38.157123025Z
total 36
drwx------   2 root root  4096 Nov 21 18:17 .
drwxr-xr-x 131 root root 12288 Nov 21 18:15 ..
-rw-------   1 root root    65 Nov 21 18:15 binance-key
-rw-------   1 root root    65 Nov 21 18:16 binance-secret
-rw-------   1 root root    31 Nov 21 18:17 pushover-token
-rw-------   1 root root    31 Nov 21 18:17 pushover-user
-rw-------   1 root root    47 Nov 21 18:17 tg-token
```

```
2026-11-21T18:23:41.574908463Z
FIND-CHAT no /start among 0 updates; waiting up to 1800 s
FIND-CHAT updates 1, private chats that sent /start: 1, pinned
exit=0
```

### 2.6 B-DEPLOY — `59-deploy-start.log` and `60-deploy.log`, whole

```
2026-11-21T18:27:50.602696156Z
Running as unit: tz54-deploy.service; invocation ID: 65a5480367e04b1694b6b7bc12326e9c
exit=0
2026-11-21T18:45:52.896243626Z
inactive
exit=4
```

```
2026-11-21T18:27:50.628Z B-DEPLOY BEGIN pid 2725488
2026-11-21T18:27:50.764Z B-DEPLOY host: a manifest found; /dev/vda2 31612203008; runtime.jsonl names e3975b5 4 times
2026-11-21T18:27:50.781Z B-DEPLOY MemAvailable read 1: 246251520 bytes, the floor 100663296
liq-guard.py: OK
liq-guard.service: OK
liq-guard.py: OK
liq-guard.service: OK
-rw-r--r-- 1 root root 1055 Nov 21 18:27 /etc/systemd/system/liq-guard.service

/root/liq-guard-svc:
total 104
drwx------  2 root root  4096 Nov 21 18:27 .
drwx------ 32 root root  4096 Nov 21 18:27 ..
-rw-------  1 root root 93840 Nov 21 18:27 liq-guard.py
-rw-------  1 root root  1055 Nov 21 18:27 liq-guard.service
2026-11-21T18:27:51.230Z B-DEPLOY installed: WatchdogUSec=infinity MainPID=0 Result=success NRestarts=0 ExecMainStatus=0 MemoryCurrent=[not set] MemoryPeak=[not set] ActiveState=inactive SubState=dead UnitFileState=disabled 
2026-11-21T18:27:51.317Z B-DEPLOY G-PROVE: the Boss's phone rings - Pushover's test alarm, acknowledged within 15 minutes
G-CRED PASS - 6 credentials of their form, 0600, root's; the dead-man not set
G-TIME PASS - Binance's clock less this host's: 26 ms
G-KEY PASS - enableFixApiTrade False, enableFixReadOnly False, enableFutures False, enableInternalTransfer False, enableMargin False, enablePortfolioMarginTrading False, enableReading True, enableSpotAndMarginTrading False, enableVanillaOptions False, enableWithdrawals False, ipRestrict True, permitsUniversalTransfer False
G-POS PASS - /fapi/v3/positionRisk served; open positions 1, with a liquidation price 1
G-BRACKET PASS - leverage brackets of one held symbol: 10
G-PUSH PASS - the user key and token validated
G-TG PASS - getMe and one message to the pinned chat
G-SEE PASS - the Boss answered yes to the list of 1 positions after 76 s
G-ALARM PASS - acknowledged after 92 s
G-HC PASS - not set - no ping
PROVE PASS: 10 gates of 10 passed; requests {'api.binance.com': 1, 'api.pushover.net': 11, 'api.telegram.org': 9, 'fapi.binance.com': 3}
Created symlink /etc/systemd/system/multi-user.target.wants/liq-guard.service -> /etc/systemd/system/liq-guard.service.
2026-11-21T18:30:43.315Z B-DEPLOY enabled and started; read in 60 s
2026-11-21T18:31:43.330Z B-DEPLOY G-UNIT read: WatchdogUSec=5min MainPID=2726013 Result=success NRestarts=0 ExecMainStatus=0 MemoryCurrent=20119552 MemoryPeak=21970944 ActiveState=active SubState=running UnitFileState=enabled 
STATUS at 2026-11-21T18:31:13Z; started 2026-11-21T18:30:42Z; last_ok 2026-11-21T18:31:13Z; polls_ok 8; polls_err 0; positions 1; with_liquidation 1; blind False; key_ok True; key_checked 2026-11-21T18:30:42Z; dead_man False; outbox 0; disk_faults 0; thresholds [5.0, 3.0, 1.5]; pid 2726013
STATUS journal files 1; events in the last two: {'command': 1, 'key': 1, 'start': 1}
2026-11-21T18:31:43.521Z B-DEPLOY G-UNIT PASS
2026-11-21T18:31:43.535Z B-DEPLOY G-LIVE read in 840 s
2026-11-21T18:45:43.567Z B-DEPLOY G-LIVE read: WatchdogUSec=5min MainPID=2726013 Result=success NRestarts=0 ExecMainStatus=0 MemoryCurrent=3457024 MemoryPeak=21970944 ActiveState=active SubState=running UnitFileState=enabled 
STATUS at 2026-11-21T18:45:28Z; started 2026-11-21T18:30:42Z; last_ok 2026-11-21T18:45:28Z; polls_ok 179; polls_err 0; positions 1; with_liquidation 1; blind False; key_ok True; key_checked 2026-11-21T18:30:42Z; dead_man False; outbox 0; disk_faults 0; thresholds [5.0, 3.0, 1.5]; pid 2726013
STATUS journal files 1; events in the last two: {'command': 7, 'key': 1, 'pushed': 2, 'start': 1, 'test': 2, 'tick': 1}
2026-11-21T18:45:43.805Z B-DEPLOY G-LIVE PASS
2026-11-21T18:45:43.806Z B-DEPLOY END exit=0
```

**`MemAvailable` at each read:** one read, `246,251,520` bytes at 18:27:50.781, at or above the floor
`100,663,296`; no second read was needed.

### 2.7 The unit after — `61-unit-after.log`, whole, with `prove.json` whole

```
2026-11-21T18:45:52.902884452Z
WatchdogUSec=5min
MainPID=2726013
NRestarts=0
MemoryCurrent=3461120
MemoryPeak=21970944
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Sat 2026-11-21 18:30:43 UTC
782efaa88e268bd6ace42e23dc192e279ae130bb7bdc23d2f4de4d628c4da66f  /root/liq-guard-svc/liq-guard.py
26f609134730e4b9080bcdddbf2365ba35b1f69ddc1633d538a250bd46bce920  /root/liq-guard-svc/liq-guard.service
26f609134730e4b9080bcdddbf2365ba35b1f69ddc1633d538a250bd46bce920  /etc/systemd/system/liq-guard.service
/etc/liq-guard:
total 40
drwx------   2 root root  4096 Nov 21 18:27 .
drwxr-xr-x 131 root root 12288 Nov 21 18:15 ..
-rw-------   1 root root    65 Nov 21 18:15 binance-key
-rw-------   1 root root    65 Nov 21 18:16 binance-secret
-rw-------   1 root root    31 Nov 21 18:17 pushover-token
-rw-------   1 root root    31 Nov 21 18:17 pushover-user
-rw-------   1 root root    10 Nov 21 18:27 tg-chat
-rw-------   1 root root    47 Nov 21 18:17 tg-token

/root/liq-guard-svc:
total 104
drwx------  2 root root  4096 Nov 21 18:27 .
drwx------ 32 root root  4096 Nov 21 18:27 ..
-rw-------  1 root root 93840 Nov 21 18:27 liq-guard.py
-rw-------  1 root root  1055 Nov 21 18:27 liq-guard.service

/var/lib/liq-guard:
total 24
drwx------  3 root root 4096 Nov 21 18:45 .
drwxr-xr-x 66 root root 4096 Nov 21 18:27 ..
drwx------  2 root root 4096 Nov 21 18:30 journal
-rw-------  1 root root 1420 Nov 21 18:30 prove.json
-rw-r--r--  1 root root   40 Nov 21 18:30 service.log
-rw-------  1 root root  401 Nov 21 18:45 state.json
SERVE start: key True, positions read 1
STATUS at 2026-11-21T18:45:28Z; started 2026-11-21T18:30:42Z; last_ok 2026-11-21T18:45:28Z; polls_ok 179; polls_err 0; positions 1; with_liquidation 1; blind False; key_ok True; key_checked 2026-11-21T18:30:42Z; dead_man False; outbox 0; disk_faults 0; thresholds [5.0, 3.0, 1.5]; pid 2726013
STATUS journal files 1; events in the last two: {'command': 7, 'key': 1, 'pushed': 2, 'start': 1, 'test': 2, 'tick': 1}
{"at": "2026-11-21T18:30:41Z", "code_sha256": "782efaa88e268bd6ace42e23dc192e279ae130bb7bdc23d2f4de4d628c4da66f", "gates": [{"detail": "6 credentials of their form, 0600, root's; the dead-man not set", "gate": "G-CRED", "pass": true}, {"detail": "Binance's clock less this host's: 26 ms", "gate": "G-TIME", "pass": true}, {"detail": "enableFixApiTrade False, enableFixReadOnly False, enableFutures False, enableInternalTransfer False, enableMargin False, enablePortfolioMarginTrading False, enableReading True, enableSpotAndMarginTrading False, enableVanillaOptions False, enableWithdrawals False, ipRestrict True, permitsUniversalTransfer False", "gate": "G-KEY", "pass": true}, {"detail": "/fapi/v3/positionRisk served; open positions 1, with a liquidation price 1", "gate": "G-POS", "pass": true}, {"detail": "leverage brackets of one held symbol: 10", "gate": "G-BRACKET", "pass": true}, {"detail": "the user key and token validated", "gate": "G-PUSH", "pass": true}, {"detail": "getMe and one message to the pinned chat", "gate": "G-TG", "pass": true}, {"detail": "the Boss answered yes to the list of 1 positions after 76 s", "gate": "G-SEE", "pass": true}, {"detail": "acknowledged after 92 s", "gate": "G-ALARM", "pass": true}, {"detail": "not set - no ping", "gate": "G-HC", "pass": true}], "pass": true, "requests": {"api.binance.com": 1, "api.pushover.net": 11, "api.telegram.org": 9, "fapi.binance.com": 3}}
```

### 2.8 G-PRINT on the logs — `62-print.log`, whole

```
2026-11-21T18:45:56.302361201Z
SCAN /root/tz54-work/logs/00-ready.log: 141 bytes, nothing found
SCAN /root/tz54-work/logs/01-stage.log: 518 bytes, nothing found
SCAN /root/tz54-work/logs/02-fingerprint.log: 13557 bytes, nothing found
SCAN /root/tz54-work/logs/03-host-gate.log: 1157 bytes, nothing found
SCAN /root/tz54-work/logs/04-number.log: 1698 bytes, nothing found
SCAN /root/tz54-work/logs/10-worktree.log: 581 bytes, nothing found
SCAN /root/tz54-work/logs/11-push.log: 637 bytes, nothing found
SCAN /root/tz54-work/logs/12-pr.log: 94 bytes, nothing found
SCAN /root/tz54-work/logs/20-checker-selftest.log: 19535 bytes, nothing found
SCAN /root/tz54-work/logs/21-guard-selftest.log: 4304 bytes, nothing found
SCAN /root/tz54-work/logs/22-scratch.log: 1670 bytes, nothing found
SCAN /root/tz54-work/logs/23-reclaim-scratch.log: 2638 bytes, nothing found
SCAN /root/tz54-work/logs/30-secrets.log: 649 bytes, nothing found
SCAN /root/tz54-work/logs/31-find-chat.log: 159 bytes, nothing found
SCAN /root/tz54-work/logs/59-deploy-start.log: 171 bytes, nothing found
SCAN /root/tz54-work/logs/60-deploy.log: 3609 bytes, nothing found
SCAN /root/tz54-work/logs/61-unit-after.log: 3430 bytes, nothing found
SCAN /root/tz54-work/logs/62-print.log: 1207 bytes, nothing found
G-PRINT PASS: 18 files, 10 values sought - credentials 6, the host's IPv4 addresses 4; found 0
exit=0
```

### 2.9 The Boss's instants, as the logs carry them

| what | instant (UTC) | where |
|---|---|---|
| his credentials, written | `binance-key` 18:15, `binance-secret` 18:16, the Pushover pair and `tg-token` 18:17 | `30-secrets.log`'s `ls -la`, by minute |
| his «готово» | read by the Executor at 18:23:38, when it read `30-secrets.log` | `30-secrets.log`'s date line |
| his `/start` | between 18:23:41 and 18:27, `tg-chat` written at 18:27 | `31-find-chat.log`; `61-unit-after.log`'s `ls -la` |
| his «да» | `76` s after the guard's list was sent | `60-deploy.log`, G-SEE |
| his acknowledgement | `92` s after the test alarm was sent | `60-deploy.log`, G-ALARM; `prove.json` `at` `2026-11-21T18:30:41Z` |

### 2.10 The files of this run

| file | lines | bytes | SHA-256 |
|---|---|---|---|
| `inst/liq-guard.py` | 1850 | 93840 | `782efaa88e268bd6ace42e23dc192e279ae130bb7bdc23d2f4de4d628c4da66f` |
| `inst/liq-guard.service` | 29 | 1055 | `26f609134730e4b9080bcdddbf2365ba35b1f69ddc1633d538a250bd46bce920` |
| `logs/00-ready.log` | 1 | 141 | `45a01aaa8c10c5d95b7115ab69471393ee9be8a15c38e80ce72d3b14f812557b` |
| `logs/01-stage.log` | 5 | 518 | `75fa52bae1d2fb9d1dae71edef1cda1eb8cd4b7da2d58a238551bd270c139641` |
| `logs/02-fingerprint.log` | 81 | 13557 | `a740712530e4b7d2f0b25b24bc22ac8868951a71211b0c336207ae856234e467` |
| `logs/03-host-gate.log` | 60 | 1157 | `832ac2721ffffb8d5f68ed740cf000d80b786d030e1b18511a71b608005847aa` |
| `logs/04-number.log` | 27 | 1698 | `7a555f3d15ae7da9312e35d4efa6608318256d29a94c577270d4753f3fcac139` |
| `logs/10-worktree.log` | 9 | 581 | `55ec680fa09e244492472ffb3e2d39c6dfd86f40ac69a6383412bf139af7b153` |
| `logs/11-push.log` | 15 | 637 | `d534f3cf19f34df7771903986241675dd65c3410733d333f8a218adaa1e9c28e` |
| `logs/12-pr.log` | 3 | 94 | `ede1cbfa9467ca205b7212edc3d5dec244bb0952c1ac00ce4ab0790beb1f816e` |
| `logs/20-checker-selftest.log` | 206 | 19535 | `311bbfed37d2d190cb8f1c6b4ea5c4738cf9f9e539d30c18479c2b60b5557717` |
| `logs/21-guard-selftest.log` | 48 | 4304 | `8b18cde64dbaf57a01acf444bb278bea7367994507247075d1a7c19b3182e8de` |
| `logs/22-scratch.log` | 18 | 1670 | `0b5616d19a002650a29a82d0813f13f92e08bd633b8dd47de8aa22a12ef0f507` |
| `logs/23-reclaim-scratch.log` | 37 | 2638 | `b90063bb626c35db905e5dd8676dd25d7b4aa2ffa0f85acb81af9469f20f47e9` |
| `logs/30-secrets.log` | 16 | 649 | `eb14833144528a160bed8dda860b7f7f69d13b4106a3e0250f9488d4c380caa7` |
| `logs/31-find-chat.log` | 4 | 159 | `533366b1d26f3c9c90017837f8c7efc4ff2a99eccec932b1c50714cce73b66ee` |
| `logs/59-deploy-start.log` | 6 | 171 | `ccbc166311accd954c47982951f9cd0d1a5c5cf684091c6290675b550d771888` |
| `logs/60-deploy.log` | 40 | 3609 | `7fa2fd83e825670eb10a82c67f3de6e97f131d3e46c9df62b77461286576eeb9` |
| `logs/61-unit-after.log` | 43 | 3430 | `8bf3ee411cb3646ac96793c0a7979cc7eeae879873a9823e92e3cdb53c82eb9f` |
| `logs/62-print.log` | 21 | 1375 | `590e5cec1a1326570f7915fee898f92bee340eb0314c7ee6a8275592767110ea` |
| `logs/99-selfcheck.log` | 8 | 261 | `06a0f599a73941c416c1af62312e27cc737b3cddbc9f0a4f339e0008b0684edb` |
| `stage/b-deploy.sh` | 117 | 6554 | `8f59acce92292bf2afda632636e8cd80ca154dfc3d9a48315acb0de19dfba4ad` |
| `stage/deploy/systemd/liq-guard.service` | 29 | 1055 | `26f609134730e4b9080bcdddbf2365ba35b1f69ddc1633d538a250bd46bce920` |
| `stage/guard/liq-guard.py` | 1850 | 93840 | `782efaa88e268bd6ace42e23dc192e279ae130bb7bdc23d2f4de4d628c4da66f` |
| `stage/research/tz54-liq-guard.py` | 3323 | 188349 | `fd8f8c21d3dc5c36655a6948ce593a03d06ca8f783955ea7d18df5a57ea0e4bf` |

---

## 3. Publication

- **Branch** `tz-54-liq-guard`, commit `8a98166a486abf0be0abdcbed2c6065eb04d9808`, on `origin` at 15:13:37 UTC
  (`11-push.log`). It holds three files, each new, at §0.1's SHA-256: `guard/liq-guard.py`,
  `deploy/systemd/liq-guard.service` and `research/tz54-liq-guard.py`. Numstat: `29 0`, `1850 0`, `3323 0`.
- **Pull request #52**, `tz-54-liq-guard` into `main`, opened by `gh pr create` (`12-pr.log`). Merge is the Boss's,
  after the Architect's verdict.
- **No Release, no asset:** no file of this run is held by one (map §7 item 167).
- **`b-deploy.sh`** is staged and never committed. Its SHA-256 is
  `8f59acce92292bf2afda632636e8cd80ca154dfc3d9a48315acb0de19dfba4ad`. Its forensic copy is
  `/root/btc-forensics/tz54-work--stage--b-deploy.sh`, and B-DEPLOY's own copies are
  `tz54-work--inst--liq-guard.py` and `tz54-work--inst--liq-guard.service`.
- **Contract §4.2's self-check** (`99-selfcheck.log`):

```
2026-11-21T18:46:02.650013902Z
From https://github.com/seahomebatumi-ai/btc-5m-twap
 * [new tag]         rewardbook-streams-1795278620 -> rewardbook-streams-1795278620
0
deploy/systemd/liq-guard.service
guard/liq-guard.py
research/tz54-liq-guard.py
grep exit=1
```

`0`: the implementation commit is not on `main`. The branch carries the three implementation files alone. No
`.parquet` or `.zip` is on `main`.

- **§9's B-RECLAIM-OWN**, run from the session; its output went to no file and is quoted here verbatim, every line:

```
[2026-11-21T18:46:58Z] reclaim: /root/tz54-work/wt skipped: no file but its HEAD's, and HEAD 8a98166a486abf0be0abdcbed2c6065eb04d9808 is its upstream's
[2026-11-21T18:46:58Z] R copied 782efaa88e268bd6ace42e23dc192e279ae130bb7bdc23d2f4de4d628c4da66f /root/btc-forensics/tz54-work--inst--liq-guard.py
[2026-11-21T18:46:58Z] R copied 26f609134730e4b9080bcdddbf2365ba35b1f69ddc1633d538a250bd46bce920 /root/btc-forensics/tz54-work--inst--liq-guard.service
[2026-11-21T18:46:58Z] R copied 45a01aaa8c10c5d95b7115ab69471393ee9be8a15c38e80ce72d3b14f812557b /root/btc-forensics/tz54-work--logs--00-ready.log
[2026-11-21T18:46:58Z] R copied 75fa52bae1d2fb9d1dae71edef1cda1eb8cd4b7da2d58a238551bd270c139641 /root/btc-forensics/tz54-work--logs--01-stage.log
[2026-11-21T18:46:58Z] R copied a740712530e4b7d2f0b25b24bc22ac8868951a71211b0c336207ae856234e467 /root/btc-forensics/tz54-work--logs--02-fingerprint.log
[2026-11-21T18:46:58Z] R copied 832ac2721ffffb8d5f68ed740cf000d80b786d030e1b18511a71b608005847aa /root/btc-forensics/tz54-work--logs--03-host-gate.log
[2026-11-21T18:46:58Z] R copied 7a555f3d15ae7da9312e35d4efa6608318256d29a94c577270d4753f3fcac139 /root/btc-forensics/tz54-work--logs--04-number.log
[2026-11-21T18:46:58Z] R copied 55ec680fa09e244492472ffb3e2d39c6dfd86f40ac69a6383412bf139af7b153 /root/btc-forensics/tz54-work--logs--10-worktree.log
[2026-11-21T18:46:58Z] R copied d534f3cf19f34df7771903986241675dd65c3410733d333f8a218adaa1e9c28e /root/btc-forensics/tz54-work--logs--11-push.log
[2026-11-21T18:46:58Z] R copied ede1cbfa9467ca205b7212edc3d5dec244bb0952c1ac00ce4ab0790beb1f816e /root/btc-forensics/tz54-work--logs--12-pr.log
[2026-11-21T18:46:58Z] R copied 311bbfed37d2d190cb8f1c6b4ea5c4738cf9f9e539d30c18479c2b60b5557717 /root/btc-forensics/tz54-work--logs--20-checker-selftest.log
[2026-11-21T18:46:58Z] R copied 8b18cde64dbaf57a01acf444bb278bea7367994507247075d1a7c19b3182e8de /root/btc-forensics/tz54-work--logs--21-guard-selftest.log
[2026-11-21T18:46:58Z] R copied 0b5616d19a002650a29a82d0813f13f92e08bd633b8dd47de8aa22a12ef0f507 /root/btc-forensics/tz54-work--logs--22-scratch.log
[2026-11-21T18:46:58Z] R copied b90063bb626c35db905e5dd8676dd25d7b4aa2ffa0f85acb81af9469f20f47e9 /root/btc-forensics/tz54-work--logs--23-reclaim-scratch.log
[2026-11-21T18:46:58Z] R copied eb14833144528a160bed8dda860b7f7f69d13b4106a3e0250f9488d4c380caa7 /root/btc-forensics/tz54-work--logs--30-secrets.log
[2026-11-21T18:46:58Z] R copied 533366b1d26f3c9c90017837f8c7efc4ff2a99eccec932b1c50714cce73b66ee /root/btc-forensics/tz54-work--logs--31-find-chat.log
[2026-11-21T18:46:58Z] R copied ccbc166311accd954c47982951f9cd0d1a5c5cf684091c6290675b550d771888 /root/btc-forensics/tz54-work--logs--59-deploy-start.log
[2026-11-21T18:46:58Z] R copied 7fa2fd83e825670eb10a82c67f3de6e97f131d3e46c9df62b77461286576eeb9 /root/btc-forensics/tz54-work--logs--60-deploy.log
[2026-11-21T18:46:58Z] R copied 8bf3ee411cb3646ac96793c0a7979cc7eeae879873a9823e92e3cdb53c82eb9f /root/btc-forensics/tz54-work--logs--61-unit-after.log
[2026-11-21T18:46:58Z] R copied 590e5cec1a1326570f7915fee898f92bee340eb0314c7ee6a8275592767110ea /root/btc-forensics/tz54-work--logs--62-print.log
[2026-11-21T18:46:58Z] R copied 06a0f599a73941c416c1af62312e27cc737b3cddbc9f0a4f339e0008b0684edb /root/btc-forensics/tz54-work--logs--99-selfcheck.log
[2026-11-21T18:46:58Z] R copied 8f59acce92292bf2afda632636e8cd80ca154dfc3d9a48315acb0de19dfba4ad /root/btc-forensics/tz54-work--stage--b-deploy.sh
[2026-11-21T18:46:58Z] R copied 26f609134730e4b9080bcdddbf2365ba35b1f69ddc1633d538a250bd46bce920 /root/btc-forensics/tz54-work--stage--deploy--systemd--liq-guard.service
[2026-11-21T18:46:58Z] R copied 782efaa88e268bd6ace42e23dc192e279ae130bb7bdc23d2f4de4d628c4da66f /root/btc-forensics/tz54-work--stage--guard--liq-guard.py
[2026-11-21T18:46:58Z] R copied fd8f8c21d3dc5c36655a6948ce593a03d06ca8f783955ea7d18df5a57ea0e4bf /root/btc-forensics/tz54-work--stage--research--tz54-liq-guard.py
[2026-11-21T18:46:58Z] RECLAIM PASS: 25 files considered, 25 copied, 0 already held; the forensic store 2790 -> 2815 files
[2026-11-21T18:46:58Z] peak memory of this run: 35024896 bytes
[2026-11-21T18:46:58Z] refused by the hook: 0; lookups 0, requests 0
reclaim exit=0
exit=0
exit=0
exit=1
/root/btc-5m-twap       0b2e935 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
2815
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10293624832
```

`RECLAIM PASS` before the removals: 25 files copied, each hash verified; the worktree removed `exit=0`; `/root/tz54-work`
removed `exit=0` and gone, `exit=1`; two worktrees left, the primary checkout and the recorder's; the forensic store
`2,815` files; `10,293,624,832` bytes free.

---

## 4. Gate

**G-DEPLOY — `B-DEPLOY END exit=0`** (TZ-54 §4). **Read: PASS.**

| gate | as TZ-54 §4 fixes it | read | how | |
|---|---|---|---|---|
| READY | `ready=1` | `ready=1`, twice | by the Executor against the literal | PASS |
| STAGE | four lines `created`, each at its SHA-256 | four, `created` | asserted by §0.1's script | PASS |
| FINGERPRINT | §0.2's line | the line, word for word | asserted by the checker | PASS |
| HOST | H1 to H5 | H1 to H5 | read by eye against §0.3 | PASS |
| NUMBER and REFS | `NUMBER PASS - 2 of 2`; no branch of this TZ on `origin` | `2 of 2`; `absent` | asserted by the checker | PASS |
| BRANCH | three files `created`; the push at `HEAD`; the numstat's three lines | three; `8a98166…` = `8a98166…`; `29 0`, `1850 0`, `3323 0` | asserted by §0.1's script; the rest read by the Executor | PASS |
| C-SELF | `141` of `141`, the hook's refusals `5` | `141` of `141`, `5` | asserted by the checker | PASS |
| G-SELF | `SELFTEST PASS: 83 checks` | the line | asserted by the guard | PASS |
| SCRATCH | every earlier directory reclaimed and gone; none live touched | 6 earlier, each `RECLAIM PASS`, `exit=0`, `exit=1`; 3 live untouched | asserted by `reclaim`; `test -e` read by the Executor | PASS |
| SECRETS | five written or kept, the sixth written, kept or skipped; `exit=0`; `0700`, `0600`, root's | five `written`, `hc-url` `skipped`, `exit=0`; `drwx------`, five `-rw-------`, root's | asserted by `secrets`; the modes read by eye | PASS |
| CHAT | `FIND-CHAT … 1, pinned`; `exit=0` | the line, `exit=0` | asserted by `find-chat` | PASS |
| G-MEM | `MemAvailable` ≥ `100,663,296` at one of five reads | `246,251,520` at read 1 | asserted by B-DEPLOY | PASS |
| G-INSTALL | both files at SHA-256, `cmp` equal, `loaded`, `disabled` | four `OK`; `cmp` silent; `UnitFileState=disabled` | asserted by B-DEPLOY | PASS |
| G-PROVE | `PROVE PASS: 10 gates of 10 passed`, `"pass": true`, this code's SHA-256 | the line; `"pass": true`; `782efaa8…` | asserted by B-DEPLOY and the guard | PASS |
| G-UNIT | 60 s: `active`, `running`, `NRestarts` `0`, `enabled`, `5min`; `key_ok` `True`, `blind` `False`, `polls_ok` ≥ `1`; the start line | all; `polls_ok 8` | asserted by B-DEPLOY | PASS |
| G-LIVE | 900 s: `active`, `NRestarts` `0`, the same `MainPID`; `key_ok` `True`, `blind` `False`, `polls_ok` ≥ `150`, `disk_faults` `0` | `active`, `0`, `2726013` = `2726013`; `True`, `False`, `179`, `0` | asserted by B-DEPLOY | PASS |
| G-DEPLOY | `B-DEPLOY END exit=0` | the line | asserted by B-DEPLOY | PASS |
| G-AFTER | `active`, `NRestarts` `0`; files at §0.1's SHA-256; `"pass": true` | `active`, `0`; three SHA-256 equal; `"pass": true` | read by the Executor against the literal | PASS |
| G-PRINT | `G-PRINT PASS` on every log and on the report | the logs: `18 files … found 0`; the report: see §6 item 1 | asserted by `scan` | PASS |

Every reading is a count, a state or an equality, so there is no number to round. **Nothing was tuned to reach a
gate, and no gate was read again after a FAIL:** no B-RESET and no second B-DEPLOY ran.

---

## 5. Validation

TZ-54 §7's Validation is the guard's self-test, `83` checks, fixed by the Architect.

| # | check | count | asserted |
|---|---|---|---|
| V1 | the guard's self-test: the margin hint against Binance's formula, the levels over thirteen reads, the key's permissions, `secrets` at a real pseudo-terminal, `find-chat`, `prove`'s ten gates and its FAILs, the guard's pass, `scan` | `83` | asserted: each an `assert` that ends the run; `SELFTEST PASS: 83 checks`, `exit=0` |
| V2 | the checker's self-test, TZ-53's under this TZ's names | `141` of `141`; refused by the hook `5` | asserted by the checker |
| V3 | `FINGERPRINT PASS`, §0.2's line | 67 of 67 frozen | asserted by the checker |
| V4 | `NUMBER PASS - 2 of 2`; refs 208 lines; the branch absent before the push | 2 of 2 | asserted by the checker |
| V5 | §0.1's script: four `created` into the stage, three into the worktree | 4; 3 | asserted by the script |
| V6 | the branch: `HEAD` on `origin`; three paths, `29 0`, `1850 0`, `3323 0` | 3 | read by the Executor against the literal (`11-push.log`) |
| V7 | the host gate | H1 to H5 | read by eye against §0.3 |
| V8 | the scratch: 6 earlier reclaimed, 3 live untouched | 6; 3 | asserted by `scratch` and `reclaim`; `test -e` read by the Executor |
| V9 | SECRETS and CHAT | 5 written, 1 skipped; 1 pinned | asserted by the guard's modes; the modes of the files read by eye |
| V10 | B-DEPLOY: the host, G-MEM, G-INSTALL, G-PROVE, G-UNIT, G-LIVE | 6 of 6 | asserted by B-DEPLOY (`fail` on each) |
| V11 | G-PROVE's ten gates, in `PROVE_GATES`' order | 10 of 10 | asserted by the guard |
| V12 | the unit after: `active`, `NRestarts` `0`, three SHA-256, `"pass": true` | 4 of 4 | read by the Executor against the literal |
| V13 | G-PRINT on the logs and on the report | 18 files, 0 found; the report, 1 file | asserted by `scan` (exit `4` on any find) |
| V14 | contract §4.2's self-check | `0`; three paths; nothing | read by the Executor |

---

## 6. What could not be implemented as written

1. **G-PRINT on this report cannot be quoted in it.** As TZ-54 §3 step 14 says, `scan` was run on this file after
   B-RECLAIM-OWN and before the commit. Its two lines were given to the Boss in the session, and the commit followed
   only on `G-PRINT PASS`.
2. **The Boss wrote this host's IPv4 address in the session's chat** with his «готово»: he said his Binance key is
   bound to it. The Executor repeated it nowhere. It is in no log, the pull request or this report, as G-PRINT
   counts. G-KEY's `ipRestrict True`, and every read of Binance that followed served, is the measurement that the
   binding matches the host's outgoing address.
3. **One read outside §2 item 3's list.** While `find-chat` waited, the Executor read `ps` and `ss -tnp` of
   `find-chat`'s own process once, to see that its long poll to Telegram was open. The output went to the session
   alone, into no log, and it changed nothing. It showed this host's address among the socket's ends, and that
   address is repeated nowhere.
4. **The Boss was asked for `/start` while `find-chat` still waited.** §3 step 10 says the Executor tells him once,
   after a run that ends without a chat. Here `find-chat` printed `no /start among 0 updates` at 18:24, and the
   Executor told him once, in Russian, to press Start in the new bot. That run then pinned the chat with `exit=0`. It
   was not run a second time.
5. **§3 step 11's line was given once. The two asks it names were repeated, each once, as each came due.** At
   G-TG's PASS the Executor repeated in the session to answer «да» or «нет» in the bot's chat and then to press
   «Подтвердить». At G-SEE's PASS it repeated the «Подтвердить» ask alone.
6. **The scratch reclaim chained `rm -rf` after `reclaim` with `&&`.** §3 step 8 gives three separate lines a
   directory and `&&` only for the paste. Each directory was therefore removed only after its own `RECLAIM PASS`.
   The classifier refused nothing, and no paste was needed.
7. **§0.1's script was run from an extract of TZ-54's lines 66 to 137,** by `bash <(sed -n 66,137p …)`. For the
   branch, the extract's first line was rewritten by `sed` to `/root/tz54-work/wt branch` in place of
   `/root/tz54-work/stage stage`: "§0.1's script verbatim but for its arguments". Before the stage's run, the
   Executor briefly wrote that extract into the session's scratchpad. It ran nothing from it, removed it, and ran the
   extract from the TZ file instead. §0.0 asks that nothing go to the scratchpad.
8. **The logs' extra lines:**
   - `04-number.log` carries the fetch's date and `fetch exit=0`;
   - `10-worktree.log` carries `exit=0` after the `worktree add` and after §0.1's script;
   - `11-push.log` carries `commit exit=0` and `push exit=0`;
   - `12-pr.log` carries `exit=0`;
   - `30-secrets.log` carries the Executor's date line before `ls -la /etc/liq-guard`;
   - `59-deploy-start.log` also carries §3 step 11's last read, `systemctl is-active tz54-deploy.service`: `inactive`,
     `exit=4`;
   - `99-selfcheck.log` is contract §4.2's self-check, a log §3's table does not name. It was written after
     `62-print.log`'s scan, so it is not among that scan's 18 files. Its lines are quoted whole in §3, and the
     report's own scan reads them there.
9. **The dead-man is not set.** The Boss pressed Enter at `hc-url`, as step 9's block allows. G-HC read
   `not set - no ping`, `PASS` by `mode_prove`'s rule, and `state.json` reads `dead_man False`. If the host, its
   network or the guard dies, no alarm reaches him from outside the host. TZ-54 §1.3 names healthchecks.io for that. This
   run did not set it, and nothing was changed.
10. **`service.log` is `0644`.** TZ-54 §1.6 lists `/var/lib/liq-guard/` as `0700`, root's, and the guard's own
    files `0600`. systemd's `StandardOutput=append:` creates `service.log`, and it read `-rw-r--r--`, 40 bytes. It is
    inside `/var/lib/liq-guard/`, `0700`, root's, so no other user can reach it. It holds the guard's
    `SERVE start` line alone. It is named here; nothing was changed.
11. **The journal's counts at G-LIVE** show the Boss using the bot after the unit started: `command 7`, `test 2`,
    `pushed 2`. No mode of this run printed a journal line, as §2 item 3 requires.
12. **The refs differ from map §1's read** (recorded, not BLOCKING). `refs` read 208 lines: `HEAD` and `main` at
    `0b2e935`, the Boss's upload, and `refs/tags/rewardbook-streams-*` at 64, the reward book's archive's later runs.
    A further tag, `rewardbook-streams-1795278620`, was fetched at 18:46 by the self-check's fetch.
13. **The classifier refused nothing, and no block was handed to the Boss to run.** B-RECLAIM-SCRATCH, B-DEPLOY's
    `systemd-run` and B-RECLAIM-OWN all ran in the session. The Boss's hands were needed for his credentials, his
    `/start`, his «да» and his acknowledgement alone. No B-RESET and no second B-DEPLOY ran.
14. **What stays on the capture host, the guard's deployment:**
    - `/root/liq-guard-svc/`, `0700`, its two files `0600`;
    - `/etc/liq-guard/`, `0700`, its six files `0600`, root's;
    - `/var/lib/liq-guard/`, `0700`, with `prove.json`, `state.json`, `journal/` and `service.log`;
    - `/etc/systemd/system/liq-guard.service`, `0644`, and its enablement link.

    **The unit runs on**, as TZ-54 §1.7 intends. Its stop is `systemctl disable --now liq-guard.service`.
