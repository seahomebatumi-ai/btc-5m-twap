# TZ-47 — the live host — REPORT

**Status: BLOCKED at §0.6, the live host gate, LH1.** `L` of `host before` (`40-host-before.log`, 22:17:29 UTC on
2026-11-18) stopped on its own assert, `exit=1`: `AssertionError: BLOCKED: the live host gate: ['LH1 hostname vs-2348']`.
The live host's name, as `hostname` prints it, is `vs-2348.` followed by its provider's DNS domain, not `vs-2348`.
LH1 compares `socket.gethostname()` with `vs-2348` exactly and read FAIL. LH2, LH3 and LH4 passed.

- **Not read:** G-GEO, G-SPEC, G-NET, G-LAT, the disk, G-SWAP and G-LOG. Every live host mode after `host` begins with
  `assert_live()`, and that function requires `socket.gethostname() == "vs-2348"` too (`is_live_host`). **§4.8's
  KEEP-or-REFUND rule therefore has no reading to decide on.**
- **Nothing on the live host was configured.** It now carries one line of root's `authorized_keys`, written by
  B-ACCESS. Its work tree `/root/tz47-work` was made by §0.6's copy and removed by §9's B-RECLAIM-LIVE, `exit=1`.
- **No branch, no commit of the instrument and no pull request:** the BLOCK came before §3.1. Nothing was pushed but
  this report.
- **The capture host:** no unit was started, stopped or touched, and no store was written. The Executor's access is
  kept as §9 says: `/root/.ssh/live-host` and its `.pub`, the `Host live-host` block in `/root/.ssh/config`, and the
  live host's key pinned in `/root/.ssh/known_hosts` under the alias.
- **No refusal by the classifier.** The Boss ran B-ACCESS once. The first `R true` to read `exit=0` was at
  22:16:36 UTC, 6 min 50 s after the handover at 22:09:46 UTC.
- **No address of either host, no password and no private key** is in this report. The one log line that holds the
  live host's full name is quoted with its DNS domain withheld (§3 item 1).

---

## 0. Fingerprint

`I0 fingerprint` (`logs/02-fingerprint.log`, 22:08:51 UTC) printed:

```
[2026-11-18T22:08:51Z] FINGERPRINT PASS: revision 2026-11-18-a; anchors 6 of 6, 4 re-derived; rows 65: frozen 62 of 62 equal, tracked 2, reported 1
```

**Revision string:** `2026-11-18-a`, equal to TZ-47's header. **Anchors**, map §0 against TZ-47's header, 6 of 6 equal;
`A2`, `A4`, `A5` and `A6` re-derived by the instrument as the first 12 hex characters of their files' SHA-256, 4 of 4
equal:

| anchor | TZ-47 and map §0 | re-derived |
|---|---|---|
| `A1` — observation set | `229a944f2d51` | — |
| `A2` — collector | `6c5089330629` | `research/twap-divergence.py` `6c5089330629`, equal |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` | — |
| `A4` — executor contract | `6ac6e10aeabc` | `BTC-EXECUTOR-INSTRUCTIONS.md` `6ac6e10aeabc`, equal |
| `A5` — recorder | `0f6c90451cbd` | `research/recorder/recorder.py` `0f6c90451cbd`, equal |
| `A6` — pricer | `729f0bcdbee3` | `research/pfair.py` `729f0bcdbee3`, equal |

**Every row of map §0's table, 65 of 65, as `fingerprint` printed it:** 62 `frozen`, each equal to the map in lines,
bytes and SHA-256; 2 `tracked`; 1 `reported`. The tree is the primary checkout `/root/btc-5m-twap`, `main` at
`27347cd8f1595661e0340f011ef1d41370ebb162`, which is `1519f9f` plus the upload of TZ-47.

| path | `wc -l` | bytes | `sha256sum` | state |
|---|---|---|---|---|
| `SYSTEM-MAP.md` | 1,025 | 153,764 | `7ff6f989aa09d006ae1951108e3b921a701e6b8bdb0fe6c688af45e2b833a055` | reported |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 235 | 11,255 | `6ac6e10aeabc3bf83926c509e6d5f868998918f34e32e7e3882e95aad83e2617` | frozen, equal to the map |
| `research/twap-divergence.py` | 1,135 | 50,928 | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | frozen, equal to the map |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | frozen, equal to the map |
| `research/tz02-distribution.py` | 334 | 14,511 | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | tracked |
| `research/pfair.py` | 441 | 19,357 | `729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68` | frozen, equal to the map |
| `research/selftest-pfair.py` | 619 | 32,559 | `b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa` | frozen, equal to the map |
| `research/tz06-calibration.py` | 577 | 27,138 | `715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f` | frozen, equal to the map |
| `research/tz07a-variance-time.py` | 623 | 28,414 | `513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771` | frozen, equal to the map |
| `research/tz07b-settlement-dispersion.py` | 515 | 24,926 | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` | frozen, equal to the map |
| `research/tz08a-out-of-sample.py` | 745 | 38,822 | `37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c` | frozen, equal to the map |
| `research/tz09-disk-inventory.py` | 894 | 41,004 | `b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6` | frozen, equal to the map |
| `research/tz10b-sigma-or-link.py` | 1,224 | 61,018 | `406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088` | frozen, equal to the map |
| `research/tz11a-student-link.py` | 1,231 | 64,732 | `0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839` | frozen, equal to the map |
| `research/tz12-sized-gate.py` | 1,157 | 61,637 | `d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999` | frozen, equal to the map |
| `research/tz13-sized-gate-test3.py` | 1,074 | 53,901 | `a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd` | frozen, equal to the map |
| `research/tz14-quote-inventory.py` | 2,124 | 109,972 | `978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02` | frozen, equal to the map |
| `research/tz15-phase2-gate.py` | 1,517 | 73,799 | `66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3` | frozen, equal to the map |
| `research/tz16a-phase2-decisive-gate.py` | 2,198 | 111,192 | `3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125` | frozen, equal to the map |
| `research/tz17-settlement-chain.py` | 1,102 | 38,622 | `e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92` | frozen, equal to the map |
| `research/tz18a-chainbook-capture.py` | 1,683 | 69,517 | `e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae` | frozen, equal to the map |
| `research/tz20-capture-under-systemd.py` | 771 | 36,528 | `104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7` | frozen, equal to the map |
| `research/tz21-recorder-memory.py` | 1,284 | 59,009 | `d6d2dc195809f2160fda7856980d8ccfbf0006ba0836943ff789c877f9d5795f` | frozen, equal to the map |
| `research/tz23-maker-m0.py` | 1,184 | 54,885 | `6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f` | frozen, equal to the map |
| `research/tz24-nesting-b2.py` | 1,535 | 76,142 | `4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b` | frozen, equal to the map |
| `research/tz26-nesting-b3-capture.py` | 2,492 | 118,466 | `caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec` | frozen, equal to the map |
| `research/tz27-pairbook-archive.py` | 2,078 | 106,284 | `2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673` | frozen, equal to the map |
| `research/tz28-pairbook-archive-timer.py` | 1,438 | 74,576 | `46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4` | frozen, equal to the map |
| `research/tz29-maker-m0-second-look.py` | 1,225 | 68,959 | `18defff93d08c13ea4638a518c88a3fec5541fcf53fb6827451e727f2204d905` | frozen, equal to the map |
| `research/tz30-nesting-b3-measure.py` | 2,518 | 131,119 | `93dbbf1c4f84553a7bc041387ef92c3c0d8747c384d383b4fcd0b247fcd131ab` | frozen, equal to the map |
| `research/tz31-who-earns.py` | 1,523 | 84,775 | `7073188c8fbaa19568e8c6e4d6379e40ea57cf2a1341ebde0ea6a08f2c544765` | frozen, equal to the map |
| `research/tz32-our-quoting.py` | 2,576 | 138,209 | `6ec367e6ed995b315063d2d808dd6a3995878011afd76abfbb7b106b645a9c61` | frozen, equal to the map |
| `research/tz33-reward-book-capture.py` | 3,542 | 175,160 | `a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670` | frozen, equal to the map |
| `research/tz34-rewardbook-archive-timer.py` | 1,791 | 99,388 | `1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72` | frozen, equal to the map |
| `research/tz35-advisor-deploy.py` | 802 | 42,049 | `d50787db5113c3f748806a60a3e71211b665cb5235296e43d0e9a747a529e6f5` | frozen, equal to the map |
| `research/tz36-advisor-trust.py` | 582 | 32,925 | `a0fb9d53afe435d37354862eb8fd299256bf551fdbdb25a5c828d2cc7376d4f5` | frozen, equal to the map |
| `research/tz37-capital-allocation.py` | 808 | 51,269 | `eec1f30b971ed1d6db31e27eb0c321276c1b107a1654e013996d023b1a6a04eb` | frozen, equal to the map |
| `research/tz38-adv3-pit-validation.py` | 1,782 | 90,181 | `579474b65329662f7bed735994381241a928a2c65a726cec3f933dc7afd4427b` | frozen, equal to the map |
| `research/tz39-advisor-checks.py` | 1,139 | 73,892 | `18294b0916d77b226083a18f9521f06e2fddb423bbc947a2e1100fd42b2980f3` | frozen, equal to the map |
| `research/tz40-advisor-strong.py` | 1,436 | 95,474 | `4403b27185f7e9aaa090dedfca457af6c4f70b6b020f0d2fcd9f9fbb96b6054b` | frozen, equal to the map |
| `research/tz42-advisor-registry.py` | 2,088 | 134,077 | `b6c45490b2f86f5c4678c645041ef1556b1199a6bc814470de904aedf7f5105f` | frozen, equal to the map |
| `research/tz43-l0-our-quote.py` | 3,056 | 152,905 | `48c3550b3f9a990fa8bc43ad8464b181ec2eb0a086b3b6f3a0ceed52da4a30cf` | frozen, equal to the map |
| `research/tz44-l0-inputs-release.py` | 1,616 | 90,703 | `0b78807d9c5dec087138b0c9a329cb8c976157ab5c8a3fd4deee7cb31e89e190` | frozen, equal to the map |
| `research/tz45-l0-rule-w.py` | 4,299 | 233,655 | `4720e78573e54b1325dd24af7c30e0de59bfb4c1879d309a23fa6bab6b32d2d4` | frozen, equal to the map |
| `research/tz46-capture-room.py` | 1,644 | 88,254 | `363b269c462d14da1656feb7bad92fec43adb1593209131fe5ca6e5c9f6755f6` | frozen, equal to the map |
| `research/recorder/recorder.py` | 651 | 27,821 | `0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7` | frozen, equal to the map |
| `research/recorder/config.py` | 112 | 4,773 | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | frozen, equal to the map |
| `research/recorder/manifest.py` | 254 | 10,002 | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | frozen, equal to the map |
| `research/recorder/analyze.py` | 813 | 34,705 | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` | frozen, equal to the map |
| `research/recorder/probe.py` | 227 | 9,324 | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | frozen, equal to the map |
| `research/recorder/selftest.py` | 573 | 30,591 | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` | frozen, equal to the map |
| `deploy/systemd/btc-recorder.service` | 23 | 707 | `3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1` | frozen, equal to the map |
| `deploy/systemd/btc-chainbook.service` | 22 | 724 | `a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2` | frozen, equal to the map |
| `deploy/systemd/btc-pairbook.service` | 22 | 761 | `ba02fe4175b961c387ea8066eb084704e69efc7fd0a48d8f623a0198334f8dd8` | frozen, equal to the map |
| `deploy/systemd/btc-pairbook-archive.service` | 17 | 794 | `2e7fd45382af3da3b2ec29ced8d69870ef3d4481da4c6f327b90fc6cb5af78e7` | frozen, equal to the map |
| `deploy/systemd/btc-pairbook-archive.timer` | 13 | 417 | `07581f4f331fbf9d2a1113cac42a2872d65ac69a872991bff7d2bda235eac913` | frozen, equal to the map |
| `deploy/systemd/btc-rewardbook.service` | 23 | 817 | `7691720c7b2261a606af54bfa20b5068b89455ea54512c55dde861d6d8063bec` | frozen, equal to the map |
| `deploy/systemd/btc-rewardbook-archive.service` | 17 | 810 | `a9abb1f092b3fb8359d37ea88df00dca8557d0f0482d04c12f0fbdd32601e33f` | frozen, equal to the map |
| `deploy/systemd/btc-rewardbook-archive.timer` | 12 | 435 | `7b0804285af6987340838bd59573897d013cf97edc5d4132cda7f3f9ba3e3824` | frozen, equal to the map |
| `deploy/systemd/adv3-bot.service` | 27 | 863 | `82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66` | frozen, equal to the map |
| `advisor/RULE-ADV-3.txt` | 33 | 3,203 | `ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169` | frozen, equal to the map |
| `advisor/adv3.py` | 895 | 51,834 | `81ef0112d3fe4b86566e51a51aab924d9776ff37a927e65982ecb0bb7c1f34e1` | frozen, equal to the map |
| `advisor/adv3-bot.py` | 2,548 | 157,438 | `c3d9fff54f3585cfc4c33b5f7e1f93b390e62b03e0b4725fee2d6fdda6d04c11` | frozen, equal to the map |
| `advisor/selftest-adv3.py` | 256 | 19,111 | `6f29b82f2b2ca82cd2ff4bbb370e032354dbb4743497330530777429b3af7398` | frozen, equal to the map |
| `.gitignore` | 5 | 252 | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | tracked |

**The model:** TZ-47 names Claude Opus 5.5. The session is configured for it.

---

## 1. The blocker

TZ-47 §0.6 runs `L` of `host before` as the live host's gate. Its first check, **LH1**, is `live_gate`'s
`hostname == LIVE_HOSTNAME` (Appendix A, lines 638 to 644), where `LIVE_HOSTNAME = "vs-2348"` (line 87) and `hostname`
is `socket.gethostname()` (line 1088). On the live host that call does not return `vs-2348`: §0.6's own read of
`hostname`, in `06-access.log`, printed the fully qualified name, `vs-2348.<its provider's DNS domain>`. So LH1
reads FAIL and `mode_host` asserts, `BLOCKED: the live host gate: ['LH1 hostname vs-2348']`, `exit=1`. §0.6: "any
failing is BLOCKED, `exit=1`". TZ-47 §10 C2 says where the expectation came from: "`vs-2348` and Ubuntu 24.04, the
host's identity, from the Boss's request and his screenshot of its terminal of 2026-11-18". The live host
gate cannot pass on this host as written. It is not a read that can be repeated: the host's name is a fixed fact. The
same equality sits in `is_live_host` (lines 381 and 382), which `assert_live` (line 1007) makes the first statement of `geoblock`, `net`,
`latency`, `disk`, `files` and `verify`. So no mode of the instrument that reads the venue or changes the host can run
there. Changing the host's name is outside TZ-47 §2 item 3, and changing the instrument or its constant is a new TZ
(contract §2, §6, §10). The run went to §3.9's copy and §9, as §3 says for a BLOCK before §3.1.

---

## 2. The evidence

Every log below is quoted whole, as written. Its SHA-256 is in §2.6, and its copy in the forensic store is
`/root/btc-forensics/tz47-work--<path with / as -->`. The one exception is the line of `06-access.log` that holds the
live host's full name (§3 item 1).

### 2.1 The live host gate — `40-host-before.log`, as the live host wrote it and §3.9's copy brought it back

```
2026-11-18T22:17:29.858406568Z
[2026-11-18T22:17:29Z] LH1 hostname vs-2348: FAIL
[2026-11-18T22:17:29Z] LH2 Ubuntu 24.04: PASS
[2026-11-18T22:17:29Z] LH3 Python 3.12: PASS
[2026-11-18T22:17:29Z] LH4 not the capture host: PASS
[2026-11-18T22:17:29Z] peak memory of this run: 26464256 bytes
[2026-11-18T22:17:29Z] refused by the hook: 0; lookups 0, requests 0, handshakes 0, TCP connects 0
Traceback (most recent call last):
  File "/root/tz47-work/tz47-live-host.py", line 1814, in <module>
    sys.exit(main(sys.argv[1:]))
             ^^^^^^^^^^^^^^^^^^
  File "/root/tz47-work/tz47-live-host.py", line 1802, in main
    rc = one[mode](rest[0])
         ^^^^^^^^^^^^^^^^^^
  File "/root/tz47-work/tz47-live-host.py", line 1091, in mode_host
    assert ok, "BLOCKED: the live host gate: %s" % [k for k, v in checks.items() if not v]
           ^^
AssertionError: BLOCKED: the live host gate: ['LH1 hostname vs-2348']
exit=1
```

LH1 FAIL; LH2, LH3 and LH4 PASS. `floors`, the host's facts and G-SPEC come after the assert and did not run.

### 2.2 The access — `06-access.log`

```
2026-11-18T22:09:26.125479134Z
exit=255
2026-11-18T22:09:36.955115777Z
keygen exit=0
2026-11-18T22:09:46.177305196Z
B-ACCESS handed to the Boss
2026-11-18T22:10:01.116397130Z R true exit=255
2026-11-18T22:10:31.534630095Z R true exit=255
2026-11-18T22:11:01.946480687Z R true exit=255
2026-11-18T22:11:32.357460251Z R true exit=255
2026-11-18T22:12:02.768617533Z R true exit=255
2026-11-18T22:12:33.181035569Z R true exit=255
2026-11-18T22:13:03.592850878Z R true exit=255
2026-11-18T22:13:34.006301457Z R true exit=255
2026-11-18T22:14:04.422526615Z R true exit=255
2026-11-18T22:14:34.833909232Z R true exit=255
2026-11-18T22:15:05.244633364Z R true exit=255
2026-11-18T22:15:35.655840812Z R true exit=255
2026-11-18T22:16:06.076915119Z R true exit=255
2026-11-18T22:16:36.487087104Z R true exit=0
2026-11-18T22:16:50.212816933Z
256 SHA256:1xbA0Mhjj0NDXcLaefl9D8run7ZKh/oo0xUOmc06Qzo btc-5m-twap executor, capture host to live host (ED25519)
Pseudo-terminal will not be allocated because stdin is not a terminal.
user root
identitiesonly yes
serveraliveinterval 15
hostkeyalias live-host
identityfile /root/.ssh/live-host
# Host live-host found: line 9 
live-host ED25519 SHA256:Y14Iy6okVrEz76M/JsR9hLre/54PtMAGXd6ZKDe4ZJw
vs-2348.<the provider's DNS domain — withheld from this public report, §3 item 1>
root
work tree exit=1
```

- `R true` was read 15 times: once before the key existed, then 13 reads 30 s apart from 22:10:01 to 22:16:06 UTC, all
  `exit=255`, and `exit=0` at 22:16:36 UTC. That is inside §0.6's bound of 120 minutes from the handover.
- The Executor's own `ssh-keygen` made the key at 22:09:36 UTC. Its fingerprint is
  `SHA256:1xbA0Mhjj0NDXcLaefl9D8run7ZKh/oo0xUOmc06Qzo` (ED25519).
- The alias's settings are printed without their `hostname` line. The live host's key is pinned under `live-host`:
  `SHA256:Y14Iy6okVrEz76M/JsR9hLre/54PtMAGXd6ZKDe4ZJw` (ED25519).
- The last line, `work tree exit=1`, is as §0.6 requires. The first of the last three lines is `vs-2348.` and a
  domain, where §0.6 and V6 expect `vs-2348`. `id -un` printed `root`.

### 2.3 The copy — `07-copy.log`

```
2026-11-18T22:17:19.788037400Z
exit=0
scp exit=0
5e2e7a7fbae23895589cf80a1bd032b4e2a82ba8bce0c2f469412a99b3ff2dbc  /root/tz47-work/tz47-live-host.py
 1814 91865 /root/tz47-work/tz47-live-host.py
```

`exit=0`, `scp exit=0`, and the live host's copy has §0.1's 1,814 lines, 91,865 bytes and SHA-256
`5e2e7a7fbae23895589cf80a1bd032b4e2a82ba8bce0c2f469412a99b3ff2dbc`.

### 2.4 What passed before it — §0.0 to §0.5, the capture host

**§0.0** — `00-ready.log`. The session's first read, at 22:08:33 UTC, printed `ready=1` too, with 10,370,662,400 bytes
free and `MemAvailable` 258,179,072.

```
2026-11-18T22:08:45.766139655Z
ready=1: second 79725 of the day, outside 10800 to 27000; 10370179072 bytes free on /var/lib, 7795535636 needed; MemAvailable 249991168, 70092270 needed; at 1795039725 2026-11-18T22:08:45Z
```

**§0.1** — `01-stage.log`. The instrument was extracted at Appendix A's SHA-256 (V3).

```
2026-11-18T22:08:45.779094535Z
/root/tz47-work/stage/research/tz47-live-host.py 1814 91865 5e2e7a7fbae23895589cf80a1bd032b4e2a82ba8bce0c2f469412a99b3ff2dbc created
exit=0
```

**§0.2** — `FINGERPRINT PASS`, §0 above (V1, first of its two reads; the second, §3.1's, did not run).

**§0.3** — `03-host-gate.log`. H1 one path; H2 `/dev/vda2`, `31612203008`, and `grep -c` `4`; H3 `3.12.3`; H4 four
paths. The memory gate's first read was 283,844,608 against 70,092,270. The disk gate read `avail` 10,369,458,176
against 7,795,535,636. **7 of 7** (V5). The consumer, `telemetry-watch.service`, was `disabled` (exit 1) and `inactive`
(exit 3).

```
2026-11-18T22:09:02.242254553Z
Wed Nov 18 10:09:02 PM UTC 2026
1795039742
2026-08-02 07:24:32
1
MemTotal:         978640 kB
MemAvailable:     260152 kB
SwapTotal:       3174396 kB
SwapFree:        2579024 kB
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10369458176
/var/lib/btc-recorder/btc-updown-5m/1794396600/manifest.json
4
3.12.3
/usr/bin/ssh
/usr/bin/ssh-keygen
/usr/bin/ssh-copy-id
/usr/bin/scp
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
618285288	/var/lib/btc-rewardbook
356280820	/root/btc-forensics
24704103	/root/.claude-8j
2567
disabled
exit=1
inactive
exit=3
/root/tz46-work exit=1
/root/.ssh/live-host exit=1
/root/btc-5m-twap       27347cd [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/tmp/claude-0/-root-btc-5m-twap/dd42fdcf-137f-5b9f-8a10-6f720861ab64/scratchpad
total 24
drwx------  6 root root 4096 Nov 18 22:07 .
drwx------ 40 root root 4096 Nov 18 22:07 ..
drwx------  3 root root 4096 Nov 15 10:28 95cf58d2-1ec6-4c73-a622-38d04665f5ae
drwx------  3 root root 4096 Nov 18 22:07 badf0ac4-2f71-4a1a-9c42-85675441c8ae
drwx------  4 root root 4096 Nov 17 14:14 ccca2df8-e51d-56bc-8205-06299775095a
drwx------  4 root root 4096 Nov 18 22:07 dd42fdcf-137f-5b9f-8a10-6f720861ab64
MemAvailable read 1 22:09:02: 283844608
```

**§0.3, the room** — `04-room.log`. The archive's service was `inactive` at its first read. The margin over
`STREAM_FLOOR` and `PEAK` was **`2,903,504,889`** bytes, above `1,000,000,000`.

```
2026-11-18T22:09:12.313525967Z
[2026-11-18T22:09:12Z] btc-rewardbook-archive.service read 1: inactive
[2026-11-18T22:09:12Z] MemAvailable read 1: 318939136 bytes, floor 70092270
[2026-11-18T22:09:12Z] available on /var/lib: 10369056768 bytes, floor 7795535636
[2026-11-18T22:09:12Z] ROOM: 10369056768 bytes available on /var/lib; the reward book's stream files 279983757 bytes in 12 files under 22 day directories; the room 10649040525; its margin over STREAM_FLOOR 7300000000 and PEAK 445535636: 2903504889 bytes
[2026-11-18T22:09:12Z] peak memory of this run: 25653248 bytes
[2026-11-18T22:09:12Z] refused by the hook: 0; lookups 0, requests 0, handshakes 0, TCP connects 0
exit=0
```

**§0.5** — `05-number.log`: `NUMBER PASS - 2 of 2`. `05-refs.log`: 176 lines, `refs/heads/tz-47-live-host` absent (V2,
first of its two reads). Against the Architect's read of §0.5, 176 lines at 21:34 UTC, every kind's count is equal:
`HEAD` 1, `refs/heads/main` 1, `tz-*` 22, pull heads 45, `pairbook-streams-*` 59, `rewardbook-streams-*` 42, and the
four annotated-tag lines and two lightweight tags 1 each. `main` stands at `27347cd`, the upload of TZ-47, where the
Architect read `1519f9f`.

```
2026-11-18T22:09:12.365598339Z
[2026-11-18T22:09:12Z] origin/main 27347cd8f1595661e0340f011ef1d41370ebb162: 113 paths under CryptoTZ/ and CryptoReports/; of the number TZ-47-: ['CryptoTZ/TZ-47-live-host.md'] and []
[2026-11-18T22:09:12Z] NUMBER PASS - 2 of 2
[2026-11-18T22:09:12Z] peak memory of this run: 25657344 bytes
[2026-11-18T22:09:12Z] refused by the hook: 0; lookups 0, requests 0, handshakes 0, TCP connects 0
exit=0
```

```
2026-11-18T22:09:12.563065162Z
[2026-11-18T22:09:13Z] REF 27347cd8f1595661e0340f011ef1d41370ebb162	HEAD
[2026-11-18T22:09:13Z] REF 27347cd8f1595661e0340f011ef1d41370ebb162	refs/heads/main
[2026-11-18T22:09:13Z] REFS HEAD                                     1
[2026-11-18T22:09:13Z] REFS refs/heads/main                          1
[2026-11-18T22:09:13Z] REFS refs/heads/tz-*                          22
[2026-11-18T22:09:13Z] REFS refs/pull/*/head                         45
[2026-11-18T22:09:13Z] REFS refs/tags/pairbook-streams-*             59
[2026-11-18T22:09:13Z] REFS refs/tags/rewardbook-streams-*           42
[2026-11-18T22:09:13Z] REFS refs/tags/tz-01a-dataset                 1
[2026-11-18T22:09:13Z] REFS refs/tags/tz-01a-dataset^{}              1
[2026-11-18T22:09:13Z] REFS refs/tags/tz-27-pairbook-streams         1
[2026-11-18T22:09:13Z] REFS refs/tags/tz-27-pairbook-streams^{}      1
[2026-11-18T22:09:13Z] REFS refs/tags/tz-44-l0-inputs                1
[2026-11-18T22:09:13Z] REFS refs/tags/tz-45-l0-rule-w-inputs         1
[2026-11-18T22:09:13Z] REFS 176 lines; refs/heads/tz-47-live-host absent
[2026-11-18T22:09:13Z] peak memory of this run: 25915392 bytes
[2026-11-18T22:09:13Z] refused by the hook: 0; lookups 0, requests 0, handshakes 0, TCP connects 0
exit=0
```

### 2.5 After the BLOCK — §3.9's copy and §9

**§3.9's copy** — `80-live-copy.log`. Every log of the live host is on the capture host, byte for byte: `scp exit=0`,
`diff exit=0`.

```
2026-11-18T22:17:46.253709651Z
scp exit=0
diff exit=0
total 12
drwxr-xr-x 2 root root 4096 Nov 18 22:17 .
drwxr-xr-x 5 root root 4096 Nov 18 22:17 ..
-rw-r--r-- 1 root root  924 Nov 18 22:17 40-host-before.log
```

**§9, B-RECLAIM-LIVE**, run by the Executor at 22:17:53 UTC:

```
$ ssh -o BatchMode=yes -o ConnectTimeout=20 -o LogLevel=QUIET live-host 'rm -rf /root/tz47-work; test -e /root/tz47-work; echo "exit=$?"'
exit=1
```

**§9, B-RECLAIM-OWN**, with `I0` in place of `I` and without its `git worktree remove` line, as §3 says for a BLOCK
before §3.1. Its output was written to no file and is quoted from the session, every line:

```
$ (cd /root/tz47-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz47-work/stage/research/tz47-live-host.py reclaim /root/tz47-work); echo "reclaim exit=$?"
[2026-11-18T22:20:35Z] R copied c154e7f59d7334d095ffaf254bbd1340fbf843764d34e546d652b01b45f35ed5 /root/btc-forensics/tz47-work--live-logs--40-host-before.log
[2026-11-18T22:20:35Z] R copied 3a17dc6ec0cee90432453158f526d6f6ade2b77d1a69f62991db90f7eead2a0e /root/btc-forensics/tz47-work--logs--00-ready.log
[2026-11-18T22:20:35Z] R copied 8f068ffc8cb9116922979740dffae3a0deb61fbbe8c94a0c08461c5af8d92013 /root/btc-forensics/tz47-work--logs--01-stage.log
[2026-11-18T22:20:35Z] R copied f8ce3ba03ea6b2392572ebe706bf740201c29d510da1f75735aa3ee8f8e253a4 /root/btc-forensics/tz47-work--logs--02-fingerprint.log
[2026-11-18T22:20:35Z] R copied 5a2a8026c538bc18e1ecf7228d98083e7f59a938ec49f303548dd38a3722dd80 /root/btc-forensics/tz47-work--logs--03-host-gate.log
[2026-11-18T22:20:35Z] R copied 22b1a21c84a56a1687e1369686925a01c5827260f2a19dcc957f667d7e6ca128 /root/btc-forensics/tz47-work--logs--04-room.log
[2026-11-18T22:20:35Z] R copied e4e5f6ba850ee2d264644b369b348f78468fcbb06f499131e0be54e61459d798 /root/btc-forensics/tz47-work--logs--05-number.log
[2026-11-18T22:20:35Z] R copied e12a6b05cdd5db4990d3a9c6c2641e956bf416a1a2a7170ef069f1f8e507432b /root/btc-forensics/tz47-work--logs--05-refs.log
[2026-11-18T22:20:35Z] R copied a22207fe9032e1c18d86465543fb45f63672b4155a1f90ccb7cbed9bb626b43c /root/btc-forensics/tz47-work--logs--06-access.log
[2026-11-18T22:20:35Z] R copied 6ab635c9fab98f380a69c75ee8127071f308757e829418a8b73d74259ac0b17e /root/btc-forensics/tz47-work--logs--07-copy.log
[2026-11-18T22:20:35Z] R copied 085ed339b8b0366e5a7dc1161d664bf3eeab61afea50f25aa4deea224dd52213 /root/btc-forensics/tz47-work--logs--80-live-copy.log
[2026-11-18T22:20:35Z] R copied 5e2e7a7fbae23895589cf80a1bd032b4e2a82ba8bce0c2f469412a99b3ff2dbc /root/btc-forensics/tz47-work--stage--research--tz47-live-host.py
[2026-11-18T22:20:35Z] RECLAIM PASS: 12 files considered, 12 copied, 0 already held; the forensic store 2567 -> 2579 files
[2026-11-18T22:20:35Z] peak memory of this run: 25915392 bytes
[2026-11-18T22:20:35Z] refused by the hook: 0; lookups 0, requests 0, handshakes 0, TCP connects 0
reclaim exit=0
$ rm -rf /root/tz47-work; echo "exit=$?"
exit=0
$ test -e /root/tz47-work; echo "exit=$?"
exit=1
$ git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
/root/btc-5m-twap       27347cd [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
$ find /root/btc-forensics -type f | wc -l
2579
$ df -B1 --output=source,size,avail /var/lib/btc-recorder
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10347327488
```

`RECLAIM PASS`, 12 of 12 copied, before the removals; `/root/tz47-work` gone, `test -e` `exit=1`, on both hosts
(V18). The worktrees are map §3's two, the primary checkout and `/root/btc-recorder-svc`. The forensic store holds
2,579 files, 2,567 at §0.3 plus these 12. 10,347,327,488 bytes are free on `/var/lib`. No line was refused by the
classifier.

### 2.6 The files of this run

Every regular file of `/root/tz47-work` at 22:18 UTC, before B-RECLAIM-OWN. `reclaim` copied each one into the forensic
store by exclusive create and checked its hash (§2.5):

| file | lines | bytes | SHA-256 |
|---|---|---|---|
| `logs/00-ready.log` | 2 | 220 | `3a17dc6ec0cee90432453158f526d6f6ade2b77d1a69f62991db90f7eead2a0e` |
| `logs/01-stage.log` | 3 | 171 | `8f068ffc8cb9116922979740dffae3a0deb61fbbe8c94a0c08461c5af8d92013` |
| `logs/02-fingerprint.log` | 75 | 12,414 | `f8ce3ba03ea6b2392572ebe706bf740201c29d510da1f75735aa3ee8f8e253a4` |
| `logs/03-host-gate.log` | 71 | 1,892 | `5a2a8026c538bc18e1ecf7228d98083e7f59a938ec49f303548dd38a3722dd80` |
| `logs/04-room.log` | 8 | 683 | `22b1a21c84a56a1687e1369686925a01c5827260f2a19dcc957f667d7e6ca128` |
| `logs/05-number.log` | 6 | 428 | `e4e5f6ba850ee2d264644b369b348f78468fcbb06f499131e0be54e61459d798` |
| `logs/05-refs.log` | 19 | 1,286 | `e12a6b05cdd5db4990d3a9c6c2641e956bf416a1a2a7170ef069f1f8e507432b` |
| `logs/06-access.log` | 33 | 1,272 | `a22207fe9032e1c18d86465543fb45f63672b4155a1f90ccb7cbed9bb626b43c` |
| `logs/07-copy.log` | 5 | 195 | `6ab635c9fab98f380a69c75ee8127071f308757e829418a8b73d74259ac0b17e` |
| `logs/80-live-copy.log` | 7 | 210 | `085ed339b8b0366e5a7dc1161d664bf3eeab61afea50f25aa4deea224dd52213` |
| `live-logs/40-host-before.log` | 19 | 924 | `c154e7f59d7334d095ffaf254bbd1340fbf843764d34e546d652b01b45f35ed5` |
| `stage/research/tz47-live-host.py` | 1,814 | 91,865 | `5e2e7a7fbae23895589cf80a1bd032b4e2a82ba8bce0c2f469412a99b3ff2dbc` |

**Peaks**, each under `35,046,135`: `fingerprint` 26,701,824; `room` 25,653,248; `number` 25,657,344; `refs`
25,915,392; `host before` 26,464,256 on the live host; `reclaim` 25,915,392.

---

## 3. Departures, named

1. **One line of one log is withheld from this report.** `06-access.log`'s `hostname` line is the live host's fully
   qualified name, `vs-2348.` and its provider's DNS domain. The repository is public (map §1), and that name is the
   provider's DNS record of the server, so publishing it may publish its address, which TZ-47 §1.2 and §2 item 5 keep
   out of every file of the repository. The line is quoted here with the domain replaced by a marker. So this
   report's quote of that log does not hash to `a22207fe…`. The log itself, unchanged, is in the forensic store as
   `/root/btc-forensics/tz47-work--logs--06-access.log` at that hash. The name was printed in the session's own output
   when the Executor read the log.
2. **`ssh -G live-host` printed `Pseudo-terminal will not be allocated because stdin is not a terminal.`** on its
   standard error, in `06-access.log`. The line carries no address, and its cause in the SSH configuration was not read.
3. **Who ran B-ACCESS, and whether B-ACCESS-KEY was needed, is not readable from the logs.** The Boss holds the root
   password, and the alias's block and the pinned key show that B-ACCESS ran at least as far as `ssh-copy-id`'s first
   connection. The live host's `authorized_keys` was not read: `host before` asserted before its print. The handover was
   given at 22:09:46 UTC. The Boss asked what he was to do, and it was given again, in Russian, at about 22:14:30 UTC.
4. **B-RECLAIM-OWN's first line ran in the subshell form of its paste**, `(cd /root/tz47-work && …)`, so that the
   removal after it did not run from inside the tree it removes. Its `git worktree remove` line was left out because no
   worktree was made (§3: a BLOCK before §3.1).
5. **§3.9's closing reads and §4.2's self-check did not run.** §3 sends a BLOCK to §3.9's copy and §9 alone. No branch
   and no implementation commit exist.
